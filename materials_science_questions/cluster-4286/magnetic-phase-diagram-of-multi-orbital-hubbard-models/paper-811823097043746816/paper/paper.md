# Self-consistent weak-coupling study of the three-band $CuO_2$ model

John Luo and N. E. Bickers
Department of Physics, University of Southern California, Los Angeles, California 90089
(Received 12 November 1992)

The "fluctuation-exchange" approximation, a Baym-Kadanoff theory used previously to treat the one-band Hubbard model, is used to investigate a three-band model for the $CuO_2$ planes in the cuprate superconductors. Attention is restricted to (a) nearest-neighbor copper-oxygen hopping and (b) a Hubbard-like Coulomb interaction on copper sites only. Orbital-occupancy factors are shown to be in good agreement with previous quantum simulation studies. An instability eigenvalue analysis confirms that, as in the one-band model, the most likely channel for superconductivity is a $d_{x^2-y^2}$ singlet. The scale for onset of exponentially long-ranged antiferromagnetic correlations is compared with results for the one-band model, and the role of hybridization in reducing the effective Coulomb interaction is studied using a transformation to Wannier states.

## I. INTRODUCTION

The investigation of pairing in the high-$T_c$ cuprate superconductors¹ has generally focused on the copper oxide layers, which are common to all such systems. The unit cell within the layers consists of a $CuO_2$ basis, and much effort has been devoted to studying a three-band model² for $Cu$ $3d_{x^2-y^2}$ and $O$ $2p_\sigma$ holes. Simplified one-band Hubbard models have been proposed³,⁴ to describe the single hybridized copper-oxygen band which crosses the Fermi surface. In turn, charge fluctuations have been projected out of the one-band description, leaving the so-called $t$-$J$ model,⁵ which may in some sense be considered minimal.

Attempts to calculate the low-temperature properties of these models⁶⁻⁹ have met with considerable success, but detailed results are still largely suggestive, rather than conclusive. The present paper describes new results on the behavior of the simplest three-band model. The results are obtained using a self-consistent-field approach¹⁰,¹¹ which has previously been applied to the one-band Hubbard model.¹²⁻¹⁴ This approach has alternately been termed the fluctuation-exchange (FLEX) approximation or generalized random-phase approximation (GRPA). The approach is the simplest extension of Hartree-Fock theory which (a) remains within the general Baym-Kadanoff family¹⁵ of theories and (b) includes the interaction of one-particle excitations with collective magnetic, charge, and particle-pair fluctuations. Interaction with magnetic fluctuations is expected to be particularly important in the cuprates, which display both ordered antiferromagnetic¹⁶,¹⁷ and superconducting¹ ground states.

An important advantage of the FLEX approach is that it allows the treatment of competing normal-state instabilities within an unbiased framework. The analysis may be viewed as an enlargement of the Migdal-Eliashberg theory¹⁸,¹⁹ for conventional superconductivity to examine possible transitions in two or more channels [e.g., a particle-hole channel with total spin 1 and total momentum $(\pi/a,\pi/a)$, as well as a particle-particle channel with total spin and momentum 0]. As in the Migdal-Eliashberg theory, the fluctuations which lead to ordering instabilities also alter the one-particle spectrum in a manner which must be treated self-consistently; in contrast with the Migdal-Eliashberg theory, the fluctuations are not phonons, but particle-hole and particle-particle pairs, whose spectrum is strongly affected by changes in the one-particle spectrum. The latter point, which amounts to the absence of a Migdal theorem,¹⁸ explains why the FLEX approximation has only semiquantitative accuracy in the intermediate-coupling range.²⁰ Despite this shortcoming, the FLEX approximation has provided accurate information¹²,¹³ on the dominance of competing transitions and on approximate scales for ordering in the one-band Hubbard model.²¹ It seems likely that information on the three-band model will have comparable validity.

In the present paper, we restrict our attention to the three-band model with the simplest structure for both the Coulomb interaction and the electronic kinetic energy, viz., an on-site $Cu$ $3d$ Coulomb term and near-neighbor $Cu$-$O$ hopping. The main motivation is to study changes in energy scales and transition temperatures which result from the presence of extended orbital structure not present in the one-band Hubbard model. In particular, we examine the relative tendency toward singlet pairing with $d_{x^2-y^2}$ or extended-$s$ symmetry and the size of the magnetic crossover scale in three- and one-band models.

This paper is organized as follows. In Sec. II we outline our notation and summarize preliminary results on the models under consideration. In Sec. III we describe our technique, particularly with regard to the three-band model, in greater detail. In Sec. IV we present our results, emphasizing the comparison between three- and one-band models. Finally, we summarize our conclusions in Sec. V.

## II. MODELS

The first convention to be settled upon in calculations for the $CuO_2$ lattice is the choice of $3d$ and $2p$ orbital

phases. We choose the representation illustrated in Fig. 1. This choice is convenient for describing both one- and two-hole wave functions: (a) A localized $3d$ one-hole wave function has $d_{x^{2}-y^{2}}$ symmetry under discrete rota tions and reflections. A more extended one-hole state with the same symmetry may be constructed by admixing neighboring sites with coefficients which transform as an $s$ wave under discrete rotations and reflections; this is be cause the underlying $d_{x^{2}-y^{2}}$ symmetry is built directly into the orbital representation. (b) In like manner, the symmetry of two-hole wave functions can be extracted directly from an examination of coefficients, without reference to the form of the underlying orbitals; this is be cause products of one-hole orbitals, each with $d_{x^{2}-y^{2}}$ symmetry about the lattice center, transform as $s$ waves. The last property is particularly useful for describing the evolution of pairing states between the so-called Hubbard and charge-transfer limits (see below).

The $CuO_{2}$ Hamiltonian for holes takes the form
$$
\begin{aligned}
\mathscr{H}-\mu\left(N_{d}+N_{p}\right)= & -t_{p d} \sum_{\langle i l\rangle s}\left(d_{i s}^{\dagger} p_{l s}+\text { H.c. }\right) \\
& -\mu \sum_{i s} n_{i s}+(\varepsilon-\mu) \sum_{l s} n_{l s} \\
& +U_{d} \sum_{i} n_{i \uparrow} n_{i \downarrow},
\end{aligned}
$$
where $t_{p d}$ is the (positive) copper-oxygen hopping in tegral, $\varepsilon$ is the separation between the $3d$ and $2p$ hole lev els, $U_{d}$ is the $3d$ Coulomb integral, and $\mu$ is the chemical potential. The operator $d_{i s}^{\dagger}$ creates a $3d$ hole with spin $s$ at site $i$ in the Cu lattice, while $p_{l s}^{\dagger}$ creates a $2p$ hole with spin $s$ at site $l$ in the O lattice. In the hopping term, the sum is restricted to Cu and O near-neighbor sites.

The Hamiltonian in Eq. (1) omits several features present in more realistic three-band $CuO_{2}$ models, includ ing a hopping integral between neighboring O sites, $^{22}t_{pp}$; a $2p$ Coulomb integral $U_{pp}$; and an interorbital $3d$-$2p$ Coulomb integral $U_{p d} \equiv V^{23}$ Four-band models, which include the presence of the $Cu3d_{z^{2}}$ orbital, have also been proposed. $^{24,25}$ These complications can, in principle,be addressed using the techniques developed below. $^{26}$ Our main purpose in the present paper is, however, re stricted to treating the effects of extended orbital struc ture within the simplest enlargement of the one-band Hubbard model.

![](./images/811823097043746816_1.jpg)

FIG. 1. Choice of phases for copper $3d$ and oxygen $2p$ orbit als. With this convention the hopping integral between any two adjacent orbitals is negative.

$Ab$ initio calculations $^{27-29}$ suggest the following range for the parameters in the real cuprate materials: $t_{p d} \simeq 1.3-1.6$ eV, $U_{d} \simeq 8.5$ eV, and $\varepsilon \simeq 3-5$ eV; or, in di mensionless units, $U_{d}/t_{p d} \simeq 5.3-6.5$ and $\varepsilon/t_{p d} \simeq 1.9-3.8$. We argue below that these parameters lie in an intermediate-coupling regime. Assuming quantum phase transitions do not intervene, this regime should be acces sible from either the weak- or strong-coupling limit.

Finally, at points in our discussion we refer to results for the one-band Hubbard model
$$
\mathscr{H}_{H}-\mu N=-t \sum_{\langle i j\rangle s}\left(c_{i s}^{\dagger} c_{j s}+\text { H.c. }\right)-\mu \sum_{i} n_{i}+U \sum_{i} n_{i \uparrow} n_{i \downarrow}.
$$

This model, which describes a single orbital species, has a one-electron bandwidth
$$
W=8 t \text {. } \quad \text { (3) }
$$

## III. TECHNIQUE

Diagonalization of the noninteracting $(U_{d}=0)$ Hamil tonian in Eq. (1) leads to bonding $(E_{\mathbf{k}}^{-})$, antibonding $(E_{\mathbf{k}}^{+})$, and nonbonding $(E_{\mathbf{k}}^{0})$ bands (see Fig. 2). The band dispersions are
$$
\begin{aligned}
& E_{\mathbf{k}}^{ \pm}=\frac{1}{2} \varepsilon \pm \frac{1}{2}\left[\varepsilon^{2}+\left(4 t_{p d}\right)^{2} A_{\mathbf{k}}\right]^{1 / 2}, \\
& E_{\mathbf{k}}^{0}=\varepsilon, \\
& A_{\mathbf{k}}=\cos ^{2}\left(\frac{1}{2} k_{x}\right)+\cos ^{2}\left(\frac{1}{2} k_{y}\right).
\end{aligned}
$$

![](./images/811823097043746816_2.jpg)

FIG. 2. Dispersion of the bonding $(E_{\mathbf{k}}^{-})$, antibonding $(E_{\mathbf{k}}^{+})$, and nonbonding $(E_{\mathbf{k}}^{0})$ hole bands.

Note that the minimum of the bonding band is at the
Brillouin zone center, $\mathbf{k}=0$. The bonding band has width
$$
\begin{aligned}
W^{-} & =\left[\left(\frac{1}{2} \varepsilon\right)^{2}+8 t_{p d}^{2}\right]^{1 / 2}-\frac{1}{2}|\varepsilon| \\
& \rightarrow 2 \sqrt{2} t_{p d} \quad(\varepsilon=0) \\
& \rightarrow 8 t_{p d}^{2} / \varepsilon \quad(\varepsilon \rightarrow \infty).
\end{aligned}\qquad(5)
$$

The gap from the bonding to the antibonding and non-
bonding bands is just $\varepsilon$.

The wave function describing a state in the bonding
band is
$$
\psi_{\mathbf{k} \sigma}=\alpha_{\mathbf{k}} d_{\mathbf{k} \sigma}+\beta_{\mathbf{k}} p_{\mathbf{k} \sigma}, \qquad(6)
$$
with
$$
\begin{gathered}
d_{\mathbf{k} \sigma}=\frac{1}{\sqrt{N}} \sum_{i} e^{i \mathbf{k} \cdot \mathbf{R}_{i}} d_{i \sigma}, \\
p_{\mathbf{k} \sigma}=\frac{1}{\sqrt{N}} \sum_{i} e^{i \mathbf{k} \cdot \mathbf{R}_{i}}\left[\left(\frac{1+e^{i k_{x}}}{2 \sqrt{A_{\mathbf{k}}}}\right) p_{i_{x} \sigma}\right. \\
\left.+\left(\frac{1+e^{i k_{y}}}{2 \sqrt{A_{\mathbf{k}}}}\right) p_{i_{y} \sigma}\right],
\end{gathered}\qquad(7)
$$
where $N$ is the number of unit cells and $i_{x}\left(i_{y}\right)$ is the value
of $l$ corresponding to the $x$-axis ($y$-axis) $2p$ orbital in the
$i$th unit cell. $^{30}$ Finally, the wave-function coefficients in
Eq. (6) are
$$
\begin{aligned}
& \alpha_{\mathbf{k}}=\frac{E_{\mathbf{k}}^{+}}{\left[4 t_{p d}^{2} A_{\mathbf{k}}+\left(E_{\mathbf{k}}^{+}\right)^{2}\right]^{1 / 2}}, \\
& \beta_{\mathbf{k}}=\frac{2 t_{p d} \sqrt{A_{\mathbf{k}}}}{\left[4 t_{p d}^{2} A_{\mathbf{k}}+\left(E_{\mathbf{k}}^{+}\right)^{2}\right]^{1 / 2}}.
\end{aligned}\qquad(8)
$$

In a perturbative treatment of the interaction $U_{d}$, the
Green's function for the $3d$ holes takes the form
$$
\begin{aligned}
& G_{d}\left(\mathbf{k}, i \omega_{n}\right)=\int_{0}^{\beta} d \tau e^{i \omega_{n} \tau} G_{d}(\mathbf{k}, \tau), \\
& G_{d}(\mathbf{k}, \tau)=-\left\langle T_{\tau} d_{\mathbf{k} \sigma}(\tau) d_{\mathbf{k} \sigma}^{\dagger}(0)\right\rangle.
\end{aligned}\qquad(9)
$$

The Green's function may be written in terms of a
Coulomb self-energy $\Sigma_{d}(\mathbf{k}, i \omega_{n})$:
$$
\begin{aligned}
G_{d}\left(\mathbf{k}, i \omega_{n}\right)= & {\left[i \omega_{n}+\mu-4 t_{p d}^{2} A_{\mathbf{k}} G_{p}^{0}\left(\mathbf{k}, i \omega_{n}\right)\right.} \\
& \left.-\Sigma_{d}\left(\mathbf{k}, i \omega_{n}\right)\right]^{-1},
\end{aligned}\qquad(10)
$$
where
$$
G_{p}^{0}\left(\mathbf{k}, i \omega_{n}\right)=\frac{1}{i \omega_{n}-(\varepsilon-\mu)}. \qquad(11)
$$

This rewriting is convenient since $\Sigma_{d}$, expressed as a
functional of $G_{d}$, assumes exactly the same form here as
in the one-band Hubbard problem. Green's functions for
the $2p$ bonding states, as well as mixed $3d$-$2p$ Green's
functions, may also be expressed in terms of $G_{d}$. For ex-
ample,
$$
G_{p}\left(\mathbf{k}, i \omega_{n}\right)=\left[i \omega_{n}-(\varepsilon-\mu)-4 t_{p d}^{2} A_{\mathbf{k}} G_{d}\left(\mathbf{k}, i \omega_{n}\right)\right]^{-1}.
\qquad(12)
$$

The investigation of two-particle instabilities is also
greatly simplified because of the presence of a single
Coulomb interaction: All possible periodic instabilities
can be determined by calculating eigenvalues of the ma-
trix kernel shown schematically in Fig. $3.^{10}$ The kernel
may represent either a particle-hole $(\Gamma_{d}^{ph})$ or particle-
particle $(\Gamma_{d}^{pp})$ scattering process. The vertices $\Gamma_{d}^{ph}$ and
$\Gamma_{d}^{pp}$ are two particle irreducible with respect to the hor-
izontal channel and may be diagonalized with respect to
total spin and momentum. In the low-density limit (i.e.,
in the absence of polarization effects due to the presence
of many particles), the vertices reduce to
$$
\begin{aligned}
& \Gamma_{d}^{\text {chg }}=+U_{d} \quad(S=0 \text { } p-h), \\
& \Gamma_{d}^{\text {mag }}=-U_{d} \quad(S=1 \text { } p-h), \\
& \Gamma_{d}^{\text {sing }}=+U_{d} \quad(S=0 \text { } p-p), \\
& \Gamma_{d}^{\text {trip }}=0 \quad(S=1 \text { } p-p).
\end{aligned}\qquad(13)
$$

For a many-particle system, the kernel may be approxi-
mated within a "conserving," or $\Phi$-derivable, approxima-
tion $^{15}$ by functional differentiation with respect to an ap-
propriate external field $^{31} \phi$:
$$
\overline{G}_{2} \Gamma_{d}=\frac{\delta \Sigma_{d}}{\delta \phi}. \qquad(14)
$$

An approximation which has proved useful for compar-
ing ordering tendencies in multiple channels for the one-
band Hubbard model $^{12,13}$ is the so-called fluctuation-
exchange (FLEX) approximation or generalized random
phase approximation (GRPA). This approximation,
which is of infinite order in $U_{d}$, incorporates the self-
energy diagrams shown in Fig. 4. These diagrams
represent the interaction of single $3d$ holes with magnet-
ic, charge, and singlet-pair excitations. At low tempera-
tures the magnetic-excitation spectrum becomes singular,
leading to strong temperature dependence in $\Sigma_{d}$. Note
that a self-consistent $3d$ hole propagator $G_{d}$ appears
everywhere; for this reason, the approximation is not per-
turbative in $U_{d}$, but instead constitutes a generalization
of Hartree-Fock self-consistent-field theory. Further-
more, the FLEX approximation for $\Sigma_{d}$ is conserving in
the Baym-Kadanoff sense. $^{15}$

Extensive studies of the one-band Hubbard model $^{13}$ in-
dicate that the FLEX approximation provides a semi-
quantitative picture of one- and two-particle correlation
functions for intermediate-coupling strengths. $^{32}$ In com-
parisons of particle-hole and particle-particle ordering

![](./images/811823097043746816_3.jpg)

FIG. 3. Schematic representation of the irreducible kernel
for determining ordering instabilities. $\Gamma_{d}$ is an irreducible
particle-hole or particle-particle vertex function. $\overline{G}_{2}$ is a prod-
uct of dressed one-particle Green's functions.

$$
\Sigma = \begin{aligned}
&\ \ \ \ \ \ \ \circ \ \ \ \ \ + \ \ \ \ \ovalbox{0} \\
&\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \

antiferromagnetic ordering $(T_{N})$. The FLEX approximation for these quantities requires solution of a set of nonlinear integral equations in $2+1$ dimensions. $^{10,11}$ Possible numerical error may be introduced by (a) discretization of the two-dimensional Brillouin zone and (b) imposition of an imaginary-frequency cutoff $\Omega_{c}$.

Our results are predominantly for temperatures greater than $T / t_{p d}=0.05$ in the three-band model and $T / t=0.1$ in the one-band model. In this temperature range, an $8 \times 8$ discretization and cutoff of $\Omega_{c}=10 t_{p d}$ (or $10 t$ ) is sufficient to achieve better than $5 \%$ accuracy in the quantities under consideration. This is not necessarily the case for other quantities, particularly susceptibilities. This is because the singular part of a susceptibility varies as $(1-\lambda)^{-1}$, with $\lambda$ the appropriate eigenvalue of an irreducible scattering kernel: Small errors in $\lambda$ can produce large variations in a susceptibility. A similar caveat applies to the low-frequency single-particle self-energy, whose detailed form is controlled by interaction with singular fluctuations.

To demonstrate the adequacy of our solution, we first show results in Figs. 6 and 7 for the $3 d$ and $2 p$ occupancy factors in the three-band model. The parameters $U_{d} / t_{p d}=6, \varepsilon / t_{p d}=2$ place the system in the experimentally relevant charge-transfer regime. The total unit-cell occupancy is fixed at $\langle n\rangle=1$. Results are shown for $\left\langle n_{d}\right\rangle$, the average occupancy of the $3 d$ orbital; $\left\langle n_{p}^{h}\right\rangle$, the average occupancy of the hybridizing $2 p$ combination; and $\left\langle n_{p}^{n}\right\rangle$, the average occupancy of the nonhybridizing $2 p$ combination.

The densities are calculated using the expressions
$$
\begin{aligned}
& \left\langle n_{d}\right\rangle=1+\frac{2 T}{n} \sum_{\mathbf{k}, \omega_{n}=-\Omega_{c}}^{\Omega_{c}} G_{d}\left(\mathbf{k}, i \omega_{n}\right)+\Delta n_{d}, \\
& \left\langle n_{p}^{h}\right\rangle=1+\frac{2 T}{N} \sum_{\mathbf{k}, \omega_{n}=-\Omega_{c}}^{\Omega_{c}} G_{p}\left(\mathbf{k}, i \omega_{n}\right)+\Delta n_{p}, \\
& \left\langle n_{p}^{n}\right\rangle=2 \frac{1}{e^{\beta(\varepsilon-\mu)}+1},
\end{aligned}
$$

![](./images/811823097043746816_4.jpg)

FIG. 6. Test of $\mathbf{k}$-space discretization error in average orbital occupancies. Results from a Brillouin-zone discretization with $8^{2}\left(16^{2}\right)$ points are denoted by lines (symbols).

![](./images/811823097043746816_5.jpg)

FIG. 7. Test of frequency cutoff error in average orbital occupancies. Results from a cutoff $\Omega_{c} / t_{p d}$ of $10(40)$ are denoted by lines (symbols).

where $G_{d}$ and $G_{p}$ are as in Eqs. (10) and (12); $\mu$ is determined self-consistently to yield fixed total unit-cell occupancy, in this case
$$
\langle n\rangle=\left\langle n_{d}\right\rangle+\left\langle n_{p}^{h}\right\rangle+\left\langle n_{p}^{n}\right\rangle=1 ; \quad(16)
$$
$N$ is the number of points in the Brillouin zone discretization; and $\Delta n_{d}\left(\Delta n_{p}\right)$ is a correction which effectively extends the frequency summation to infinity using the noninteracting Green's function with the same (interacting) chemical potential, e.g.,
$$
\Delta n_{p}=2 \frac{1}{e^{\beta(\varepsilon-\mu)}+1}-2 T \sum_{\omega_{n}=-\Omega_{c}}^{\Omega_{c}} \frac{1}{i \omega_{n}-(\varepsilon-\mu)}.
$$

The change in the orbital occupancies in passing from an $8^{2}$ to a $16^{2}$ discretization (Fig. 6) is less than $1 \%$.

![](./images/811823097043746816_6.jpg)

FIG. 8. Test of $\mathbf{k}$-space discretization error in instability eigenvalues. Results from a Brillouin-zone discretization with $8^{2}$ $\left(16^{2}\right)$ points are denoted by lines (symbols).

![](./images/811823097043746816_7.jpg)

FIG. 9. Test of frequency cutoff error in average orbital occupancies. Results from a cutoff $\Omega_{c}/t_{pd}$ of 10 (40) are denoted by lines (symbols).

Likewise, the change which results from increasing the cutoff from $\Omega_{c}/t_{pd}=10$ to 40 (Fig. 7) is on the order of $4\%$.

The antiferromagnetic and singlet eigenvalues display similar sensitivity to these changes. Results are shown in Figs. 8 and 9. The accuracy of the antiferromagnetic eigenvalue insures comparable accuracy in the determination of $T_{N}$, the temperature at which the eigenvalue saturates to unity.

### B. Variation of $3d$ and $2p$ occupancy factors

The variation of the occupancy factors $\langle n_{d}\rangle$ and
$$2\langle n_{p}\rangle\equiv\langle n_{p}^{h}\rangle+\langle n_{p}^{n}\rangle\qquad(18)$$
with changes in total unit-cell occupancy $\langle n\rangle$ is determined by the relative size of $U_{d}$ and $\varepsilon$. Whenever $\varepsilon>0$ the first hole introduced in the unit cell resides primarily on the $3d$ orbital, though there may be a large $2p$ admixture for small $\varepsilon$. For fillings $\langle n\rangle>1$, however, behavior depends on the size of $\varepsilon$. For $\varepsilon\gg U_{d}$ (the so-called Hubbard regime), the second hole again resides primarily on the $3d$ orbital; on the other hand, for $U_{d}\gg\varepsilon$ (the charge-transfer regime), the second hole resides primarily on the hybridized $2p$ orbital.

As shown in Fig. 10(a), for $\varepsilon/t_{pd}=8$, $U_{d}/t_{pd}=6$ (the Hubbard regime), the $2p$ occupancy remains small for $\langle n\rangle$ as large as 1.2. The $3d$ occupancy for $\langle n\rangle=1$ is approximately 0.93; $\langle n_{d}\rangle$ passes through 1.0 for $\langle n\rangle=1.08$ and continues to increase, though with a slightly negative curvature. On the other hand, for $\varepsilon/t_{pd}=2$, $U_{d}/t_{pd}=6$ (the charge-transfer regime), $\langle n_{d}\rangle$ remains well below 1.0 for $\langle n\rangle$ up to 1.2. Further, although the majority of the holes go onto the $3d$ orbital for $\langle n\rangle<1$ [Fig. 10(b)], the holes added beyond this point favor the hybridized $2p$ orbital by a factor of roughly 2:1.

The symbols in Figs. 10(a) and 10(b) are results from direct quantum simulation $^{9}$ of a $4^{2}$ real-space lattice of $CuO_{2}$ unit cells. Note that the FLEX results are in close agreement with this essentially exact calculation. This agreement is largely expected, since $\langle n_{d}\rangle$ and $\langle n_{p}\rangle$ are frequency-integrated quantities. The agreement for low-frequency quantities (e.g., singlet scattering eigenvalues) is also expected to be semiquantitative, though not at this level of accuracy.

To emphasize the manner in which the model with $\langle n\rangle=1$ crosses over to the Hubbard regime, results are shown in Fig. 11 for $\langle n_{d}\rangle$ and $\langle n_{p}\rangle$ as a function of $\varepsilon/t_{pd}$ for fixed $U_{d}/t_{pd}=8$. The $2p$ occupancy drops rapidly to zero, just as it would in the absence of the $3d$ Coulomb interaction.

It is also possible to trace the crossover to the charge-

![](./images/811823097043746816_8.jpg)

FIG. 10. Variation of average orbital occupancy with average unit cell occupancy $\langle n\rangle$. FLEX results are denoted by lines, and results from quantum simulation (Ref. 9) by symbols. Note that here $n_{p}$ is the average occupancy of a single-site $p$ orbital, rather than the hybridizing combination ($n_{p}^{h}$ in Figs. 6 and 7). (a) Hubbard regime ($\varepsilon>U_{d}$). (b) Charge-transfer regime ($\varepsilon<U_{d}$).

![](./images/811823097043746816_9.jpg)

FIG. 11. Variation of the average orbital occupancies with $\varepsilon$ for fixed unit-cell occupancy $\langle n\rangle=1$ and fixed Coulomb interaction $U_{d} / t_{p d}=8$. In this case the true Hubbard limit $(\langle n_{d}\rangle \to 1)$ requires $U_{d} / t_{p d} \sim 16$. In this figure and those which follow, the symbols represent actual calculated points, while the lines are cubic spline interpolations.

transfer regime in like manner. Results for $\langle n_{d}\rangle$ and $\langle n_{p}\rangle$ are plotted in Fig. 12 as a function of $U_{d} / t_{p d}$ for fixed $\varepsilon / t_{p d}=2$, again with $\langle n\rangle=1$. Note that as $U_{d}$ increases (i.e., the system moves deeper into the charge-transfer regime), $\langle n_{d}\rangle$ slowly decreases. This effect becomes more dramatic for smaller $\varepsilon$; on the other hand, the effect is absent for variations in $U_{d}$, which keep the system in the Hubbard regime $\varepsilon \gg U_{d}$.

### C. Irreducible singlet eigenvalues

We examine below singlet particle-particle eigenvalues $^{10}$ of the scattering kernel shown schematically in Fig. 3. Magnetic particle-hole eigenvalues are discussed in

![](./images/811823097043746816_10.jpg)

FIG. 12. Variation of the average orbital occupancies with $U_{d}$ for fixed unit-cell occupancy $\langle n\rangle=1$ and fixed orbital splitting $\varepsilon / t_{p d}=2$.

Sec. IV D. We consider two singlet channels, $d_{x^{2}-y^{2}}$ and extended-$s$, which differ only in the symmetry of the pairing eigenstate under discrete rotations. In two dimensions the $d_{x^{2}-y^{2}}$ state has nodal lines in the directions $k_{x}=\pm k_{y}$. In contrast, the extended-$s$ state has no nodal lines, but tends to change sign across the Fermi surface.

States with $d_{x^{2}-y^{2}}$ and extended-$s$ symmetry are naturally favored by the presence of strong antiferromagnetic spin fluctuations. $^{33-35}$ Such fluctuations are present in the three-band $CuO_{2}$ model (as well as the one-band Hubbard model) with $\langle n\rangle \sim 1$. While spin fluctuation exchange is intrinsically repulsive throughout momentum space, an effective attraction arises in particular pairing states with the property
$$
\begin{aligned}
& \phi(\mathbf{k}+\mathbf{Q})=-\phi(\mathbf{k}), \\
& \mathbf{Q} \sim(\pi / a, \pi / a).
\end{aligned}\qquad(19)
$$
Both $d_{x^{2}-y^{2}}$ and extended-$s$ states have this property.

Sample $d_{x^{2}-y^{2}}$ and extended-$s$ states with instantaneous correlations are
$$
\begin{aligned}
& \phi_{d}(\mathbf{k})=\cos k_{x}-\cos k_{y}, \\
& \phi_{s *}(\mathbf{k})=\cos k_{x}+\cos k_{y}.
\end{aligned}\qquad(20)
$$

In fact, the true maximum eigenvalue pairing states are strongly retarded, as a result of the sharp peaking of the antiferromagnetic fluctuation spectrum at low frequencies. Note that the extended-$s$ state takes its name from the real-space Fourier transform of $\phi_{s *}$, which localizes the holes in the pair in an "extended" configuration, at a separation of one unit-cell length.

Determination of the maximum $d_{x^{2}-y^{2}}$ eigenvalue by projection on an appropriately symmetrized test vector is straightforward. $^{10,12,13}$ Problems arise for the extended-$s$ eigenvalue, however. This is because the $s$-wave eigenstate whose eigenvalue is largest in magnitude is actually an "on-site" $s$ (i.e., a state which localizes the holes in the pair in the same unit cell). The on-site $s$ eigenvalue is repulsive and generally much larger in magnitude than the attractive extended-$s$ eigenvalue. This prevents naive use of a projection scheme.

The extended-$s$ state can still be found by projection, however, if the entire spectrum of the scattering kernel is shifted by a uniform amount, $\alpha>0$:
$$
\Gamma_{d} \bar{G}_{2} \rightarrow \Gamma_{d} \bar{G}_{2}+\alpha \mathbb{1}.\qquad(21)
$$
(Note that attractive eigenvalues of the kernel are positive.) The shift $\alpha$ can be chosen such that
$$
0<\lambda_{s}+\alpha<\lambda_{s *}+\alpha\qquad(22)
$$
for all $\lambda_{s}$ (including the troublesome on-site $s$ eigenvalue). The shifted eigenvalue $\lambda_{s *}+\alpha$ can then be found by simple projection.

A wide array of studies of the one-band Hubbard model, $^{36-39}$ including determination of transition temperatures within the FLEX scheme, $^{12,13}$ suggest that the $d_{x^{2}-y^{2}}$ channel is the most likely to exhibit superconductivity. Quantum simulations $^{8,9}$ of the three-band $CuO_{2}$

model suggest that (a) the $d_{x^{2}-y^{2}}$ channel remains a strong pairing candidate, (b) the extended-$s$ channel strongly competes with the $d_{x^{2}-y^{2}}$, and (c) the addition of a near-neighbor copper-oxygen repulsion $U_{pd}\equiv V$ relatively favors the extended-$s$ state. While the present study does not address the third point, it provides additional information on the first two.

Our principal results on the pairing eigenvalues are as follows: (a) The $d_{x^{2}-y^{2}}$ singlet eigenvalue remains largest at low temperatures in the three-band model, as in the one-band model; (b) the extended-$s$ eigenvalue is smaller by roughly a factor of 2 over the entire temperature range studied; and (c) for comparable values of $U_{d}/W^{-}$ and $U/W$ (see Secs. II and III), the three-band eigenvalues are markedly lower, indicating a reduced tendency toward pairing. The last result is echoed in the dependence of the antiferromagnetic eigenvalue (discussed in Sec. IV D).

![](./images/811823097043746816_11.jpg)

FIG. 13. Temperature variation of the $d_{x^{2}-y^{2}}$ and extended-$s$ singlet eigenvalues. (a) Three-band model with $U_{d}/W^{-}=3.6$. (b) One-band model with $U/W=0.5$. Note that the $d_{x^{2}-y^{2}}$ eigenvalue is consistently larger in both cases.

Singlet eigenvalues for a typical three-band parameter set in the charge-transfer regime $(U_{d}/t_{pd}=10$, $\varepsilon/t_{pd}=2$, $\langle n\rangle=0.875)$ are plotted in Fig. 13(a). For comparison, one-band Hubbard results for $U/t=4$, $\langle n\rangle=0.875$ are plotted in Fig. 13(b). In both cases the temperature is scaled by the relevant bandwidth $W^{-}=2.76t_{pd}$ or $W=8t$. Note that $W^{-}$ incorporates the effect of a Hartree-Fock shift in the $3d$ level. The renormalized $3d$-$2p$ level splitting is $\widetilde{\varepsilon}=\varepsilon-\frac{1}{2}U_{d}\langle n_{d}\rangle$. In the present case, the splitting is reduced from $\varepsilon/t_{pd}=2$ to $\widetilde{\varepsilon}/t_{pd}=-0.13$. After rescaling in this way, the eigenvalues are quite similar, though the scaled Coulomb energies $U_{d}/W^{-}=3.6$ and $U/W=0.5$ differ by almost an order of magnitude. The fact that the pairing tendency is much smaller in the three-band model (i.e., a much larger scaled Coulomb energy is required to generate a similar effect) can be explained by the presence of hybridization with uncorrelated $2p$ orbitals. Since holes spend reduced time in the correlated $3d$ orbitals, the effect of the interaction is reduced. The size of this reduction can roughly be estimated using Wannier states (see Sec. IV D). For the parameters chosen above, the repulsion between two holes in the same Wannier state, calculated using Hartree-Fock energy levels, is reduced by a factor of $V_{ii}/U_{d}=0.22$, giving $V_{ii}/W^{-}=0.8$. This is still considerably larger than the value of $U/W$ in Fig. 13(b), indicating that the Wannier-state description is qualitatively, but not quantitatively, predictive.

The ordering and relative size of the $d_{x^{2}-y^{2}}$ and extended-$s$ eigenvalues remains the same for varying $\varepsilon$ and fixed $U_{d}$. However, it is interesting to note that as $\varepsilon$ decreases, both eigenvalues pass through a maximum at fixed $T/t_{pd}$ (Fig. 14). This represents the resolution of two opposing tendencies: (a) The width of the Hartree-Fock bonding band $W^{-}$ increases monotonically with decreasing $\varepsilon$ and fixed $t_{pd}$ (so long as the Hartree-Fock corrected splitting $\widetilde{\varepsilon}$ remains positive), thereby decreasing

![](./images/811823097043746816_12.jpg)

FIG. 14. Variation of the $d_{x^{2}-y^{2}}$ and extended-$s$ singlet eigenvalues with $\varepsilon$ for fixed $U_{d}$ and $T$. The incipient instability is strongest in both channels for intermediate $\varepsilon$ (on the order of $t_{pd}$ in the present case).

the scaled value $T/W^-$; (b) on the other hand, a decrease in $\varepsilon$ tends to decrease $U_d/W^-$ for fixed $U_d$ and to increase the admixture of $2p$ states in the bonding band. The former effect tends to increase the strength of pairing correlations for fixed $T/t_{pd}$, while the latter effects decrease the strength. As indicated by Fig. 14 and by earlier simulations of equal-time correlation functions, $^{8}$ small (but positive) $\varepsilon$ generally favors, rather than hinders, pairing.

### D. Magnetic crossover temperature $T_N$

In two dimensions the large phase space available for low-energy fluctuations rules out the existence of true long-range magnetic order at finite temperatures. $^{40}$ Nevertheless, it is now well established that the quantum Heisenberg model exhibits a correlation length which increases exponentially with decreasing temperature. $^{41,42}$ It is generally agreed the same should be true in two-dimensional fermion models which order at $T{=}0$ with a Heisenberg order parameter $^{43,44}$ (e.g., the one-band Hubbard and three-band $CuO_2$ models with $\langle n\rangle{=}1$). In such cases the maximum eigenvalue of the irreducible particle-hole kernel (Fig. 3) should saturate to unity with the following temperature dependence [Fig. 15(a)]:

$$
\lambda_{m}(T) \sim 1-B(T) e^{-A / T}, \quad T \rightarrow 0. \tag{23}
$$

![](./images/811823097043746816_13.jpg)

FIG. 15. Schematic representation of the behavior of the two-dimensional antiferromagnetic eigenvalue in (a) an exact solution and (b) the FLEX approximation (or any other approximation with mean-field-like critical properties.)

Here $A$ is a constant and $B(T)$ a power-law prefactor. This form is assumed asymptotically and should break down at high temperatures. In general, one expects a crossover temperature $T_N$ [on the order of 0.5 in Fig. 15(a)] to separate the high- and low-temperature regimes. Such a temperature may be defined as the scale below which the correlation length exceeds some preset scale.

The FLEX approximation and all similarly defined Baym-Kadanoff theories are mean-field-like in the sense that critical behavior is classical. $^{45}$ In terms of scattering eigenvalues, this means that $\lambda_{m}(T)$ passes through unity at a finite temperature with a linear slope [Fig. 15(b)]. For this reason the magnetic crossover scale defined above shows up as a true phase transition. Despite this inadequate treatment of the critical region, the FLEX approximation provides potentially useful information on (a) the magnitude of the crossover scale and (b) its variation with model parameters. We describe below results for $T_N$ from a study of magnetic eigenvalues in the three-band $CuO_2$ model and, to a lesser extent, in the one-band Hubbard model. In most cases we restrict attention to $\langle n\rangle{=}1$.

It is convenient to begin with the half-filled one-band model, which is characterized by a single parameter $U/t$. The variation of $T_N/t$ as a function of $U/t$ within the FLEX approximation is plotted in Fig. 16. The approximation becomes invalid in the large-$U$ limit, where the natural energy scale is no longer $t$, but $4t^2/U\equiv J$. In this limit, infinite-order vertex renormalizations (which arise in "parquetlike" treatments $^{13,20}$) are essential to describe the physics starting from the weak-coupling limit. The FLEX approximation should retain at least semiquantitative validity, however, in the range $U/W\leq 1$, i.e., $U/t\leq 8$.

Note that the FLEX crossover scale rises monotonically with increasing $U$, eventually assuming the (incorrect) asymptotic form

![](./images/811823097043746816_14.jpg)

FIG. 16. Variation of the FLEX Néel temperature with $U/t$ in the one-band model with $\langle n\rangle{=}1$.

$$
\begin{aligned}
& T_{N} / t \sim \gamma U / t, \\
& \gamma \sim 0.015.
\end{aligned}\tag{24}
$$

It is worthwhile to comment on this form even though the approximation is not valid in this strong-coupling limit. The functional dependence is the same which fol- lows from a high-temperature Hartree-Fock analysis, though with a drastically reduced value of $\gamma$. In the Hartree-Fock analysis, the condition for a magnetic in- stability with wave vector $\mathbf{Q}$ is
$$
U \chi^{0}\left(\mathbf{Q}, \omega=0 ; T_{N}\right)=1.\tag{25}
$$

Since
$$
\chi^{0}\left(\mathbf{Q}, \omega=0 ; T_{N}\right) \rightarrow 1 / 4 T_{N}, \quad T_{N} \rightarrow \infty,\tag{26a}
$$
it follows that, for large $U$,
$$
T_{N} / t \sim \frac{1}{4}(U / t).\tag{26b}
$$

![](./images/811823097043746816_15.jpg)

FIG. 17. Variation of the FLEX Néel temperature in the three-band model. (a) Variation with $U_{d}$ in the extreme Hub bard limit ( $\varepsilon$ fixed and much greater than $U_{d}$ ). (b) Variation with $\varepsilon$ for fixed $U_{d} / t_{p d}=8$.

The drastic reduction of $\gamma$ from the Hartree-Fock value of $\frac{1}{4}$ results from the presence of magnetic fluctuations in the self-consistent one-particle self-energy.

The validity of the FLEX approximation is restricted even more severely in the Hubbard regime $(\varepsilon \gg U_{d})$ of the three-band $CuO_{2}$ model. In this limit the lower hy bridized band (i.e., $E_{k}^{-}$) becomes entirely $3 d$, with an effective copper-copper hopping element
$$
\tilde{t}=t_{p d}^{2} / \varepsilon.\tag{27}
$$

Since the mapping to the one-band model becomes rigorous in this limit, one expects, for large $U_{d}$,
$$
T_{N} / \tilde{t} \sim \gamma U_{d} / \tilde{t},\tag{28}
$$
with the $\gamma$ found previously. Multiplying Eq. (28) by $t_{p d} / \varepsilon$ gives
$$
T_{N} / t_{p d} \sim \gamma U_{d} / t_{p d}.\tag{29}
$$

Hence, within the FLEX approximation, the value of $T_{N}$ should be (a) linear in $U_{d}$ and (b) independent of $\varepsilon$ for $t_{p d}^{2} / \varepsilon \ll U_{d} \ll \varepsilon$. This behavior is illustrated in Figs.17(a) and 17(b). Note that the slope of the curve in Fig.17(a) is
$$
\gamma^{\prime} \sim 0.012,\tag{30}
$$
a value in good agreement with that deduced from the one-band analysis [Eq. (24)]. Note also that in analogy with the one-band model the correct asymptotic behavior is
$$
T_{N} / t_{p d} \sim 4 \tilde{t}^{2} / U_{d} t_{p d}=4 t_{p d}^{3} / \varepsilon^{2} U_{d}.\tag{31}
$$

The restriction of $U_{d}$ to values less than the bandwidth $W^{-}=8 \tilde{t}$ makes the FLEX approximation useful only for very small $U_{d}$ in the Hubbard limit of the three-band model.

In contrast, the FLEX approximation is expected to remain useful up to large values of $U_{d} / t_{p d}$ in the charge

![](./images/811823097043746816_16.jpg)

FIG. 18. Variation of the FLEX Néel temperature with $U_{d}$ in the charge-transfer limit ( $\varepsilon$ fixed and smaller than $U_{d}$ ).

transfer regime. This is because the presence of hybridi- zation with uncorrelated $2 p$ orbitals strongly reduces the effective value of $U_{d}$. Figure 18 illustrates the typical dependence of $T_{N}$ on $U_{d}$ for small $\varepsilon$ (in this case, $\varepsilon / t_{p d}=2$ ). Note that $T_{N} / t_{p d}$ exhibits a weak maximum of 0.045 for $U_{d} / t_{p d} \sim 8$. Increasing $U_{d}$ beyond this value leads to a slow decrease in the $3 d$ occupancy (see Fig. 12), as holes are transferred to uncorrelated $2 p$ states. Relat ed behavior is illustrated in Fig. 17(b), where $T_{N} / t_{p d}$ is plotted as a function of $\varepsilon / t_{p d}$ for fixed $U_{d} / t_{p d}=8$. In this case a decrease in $\varepsilon$ below the value of $U_{d}$ leads to in creased occupancy of $2 p$ orbitals: Since the $2 p$ orbitals are uncorrelated, this effectively reduces the strength of the magnetic coupling.

The value of the effective interaction between hybri- dized $3 d-2 p$ states can be roughly estimated using a Wannier-state analysis of the Fermi-surface band. The Wannier state for the $i$ th unit cell is
$$
\begin{aligned}
\Phi_{i} & =\frac{1}{\sqrt{N}} \sum_{i} e^{-i \mathbf{k} \cdot \mathbf{R}_{i}}\left(\alpha_{\mathbf{k}} d_{\mathbf{k}}+\beta_{\mathbf{k}} p_{\mathbf{k}}\right) \\
& =\frac{1}{N} \sum_{j} d_{j} \sum_{\mathbf{k}} \alpha_{\mathbf{k}} e^{-i \mathbf{k} \cdot\left(\mathbf{R}_{i}-\mathbf{R}_{j}\right)}+\frac{1}{\sqrt{N}} \sum_{\mathbf{k}} e^{-i \mathbf{k} \cdot \mathbf{R}_{i}} \beta_{\mathbf{k}} p_{\mathbf{k}}.
\end{aligned}
$$

The $2 p$ portion of the wave function is not of direct in terest here (since the $2 p$ orbitals are uncorrelated) and need not be expanded further. The direct Coulomb in- teraction between Wannier states in the $i$ th and $l$ th unit cells is
$$
V_{i l}=\sum_{\left\langle\mathbf{r r}^{\prime}\right\rangle}\left|\Phi_{i}(\mathbf{r})\right|^{2}\left|\Phi_{l}\left(\mathbf{r}^{\prime}\right)\right|^{2} V_{c}\left(\mathbf{r}-\mathbf{r}^{\prime}\right),\qquad(33)
$$
where $r$ and $r^{\prime}$ run over all sites in the $CuO_{2}$ lattice. Since
$$V_{c}\left(\mathbf{r}-\mathbf{r}^{\prime}\right)=U_{d} \delta_{\mathbf{r}, \mathbf{r}^{\prime}} \sum_{m} \delta_{\mathbf{r}, \mathbf{R}_{m}}\qquad(34)$$
with $R_{m}$ the copper sites,
$$
\begin{aligned}
V_{i l}= & U_{d} \sum_{m}\left|\Phi_{i}\left(\mathbf{R}_{m}\right)\right|^{2}\left|\Phi_{l}\left(\mathbf{R}_{m}\right)\right|^{2} \\
= & \frac{U_{d}}{N^{3}} \sum_{\mathbf{k}_{1} \mathbf{k}_{2} \mathbf{k}_{3}} \alpha_{\mathbf{k}_{1}} \alpha_{\mathbf{k}_{2}}^{*} \alpha_{\mathbf{k}_{3}} \alpha_{\mathbf{k}_{1}-\mathbf{k}_{2}+\mathbf{k}_{3}}^{*} \\
& \times e^{-i\left(\mathbf{k}_{1}-\mathbf{k}_{2}\right) \cdot\left(\mathbf{R}_{i}-\mathbf{R}_{j}\right)},
\end{aligned}\qquad(35)
$$
with $k_{i}$ restricted to the first Brillouin zone. Note that the coefficients $\alpha_{k_{i}}$ must be evaluated using the Hartree Fock renormalized level splitting $\tilde{\varepsilon}$ , rather than $\varepsilon$ .

In the Hubbard limit,
$$V_{i l} \rightarrow U_{d} \delta_{i l}, \quad(36)$$
and a one-band Hubbard model can rigorously be con-

![](./images/811823097043746816_17.jpg)

FIG. 19. Wannier-state calculation of the effective reduction $V_{i i} / U_{d}$ of the $3 d$ Coulomb integral as a function of $\varepsilon / t_{p d}$ . Re sults are shown for $\langle n\rangle=1$ and $T \to 0$ with $U_{d} / t_{p d}=6$ (solid line) and $U_{d} / t_{p d} \to 0$ (dashed line). The difference in these re sults is due to the effect of the Hartree-Fock shift in the $3 d$ ener gy level.

![](./images/811823097043746816_18.jpg)

FIG. 20. Variation of three-band model parameters with $U_{d} / W^{-}$ . The unit-cell occupancy and unrenormalized level splitting are fixed at $\langle n\rangle=1$ and $\varepsilon / t_{p d}=2$ . (a) Effective Coulomb integral $V_{i i} / W^{-}$ . (b) FLEX Néel temperature T_N/W^-.

structed from the Wannier states. On the other hand, in the charge-transfer limit it is certainly an oversimplification to use the simplest one-band description with $V_{i i} \leftrightarrow U$: (a) The direct Coulomb interaction is not strictly zero range; (b) there exists an exchange interaction between Wannier states, ignored here; and (c) virtual transitions to the upper bands are possible. The assumption of a zero-range direct Coulomb interaction is in fact quite good in the present case. Evaluation of Eq. (35) for $\tilde{\varepsilon} / t_{p d}=2$ shows that $V_{i i} / U_{d}=0.55$, while the coupling $V_{i, i+1} / U_{d}$ between near-neighbor cells has already fallen to $4 \times 10^{-4}$. In any case, $V_{i i}$ provides a straightforward estimate of the reduction of the Coulomb interaction by hybridization effects. Values of $V_{i i} / U_{d}$ for fixed $U_{d} / t_{p d}=6$ and $\langle n\rangle=1$ are plotted as a function of $\varepsilon / t_{p d}$ in Fig. 19. To indicate the effect of the HartreeFock energy level correction, which reduces $V_{i i} / U_{d}$ for large $U_{d}$ in the charge transfer regime, results are also shown for the limit $U_{d} / t_{p d} \rightarrow 0$ (in which the energy level correction tends to zero).

![](./images/811823097043746816_19.jpg)

FIG. 21. Reduction of the FLEX Néel temperature with doping. (a) One-band model with fixed $U$. (b) Three-band model with fixed $\varepsilon$ and $U_{d}$.

This effective reduction of the Coulomb integral accounts for most of the reduction in $T_{N} / W^{-}$(three-band model) in comparison with $T_{N} / W$ (one-band model) for equal values of $U_{d} / W^{-}$and $U / W$. In addition, the Coulomb reduction accounts for the behavior in Fig. 18. As $U_{d}$ increases with fixed $\varepsilon, \tilde{\varepsilon}=\varepsilon-\frac{1}{2} U_{d}\left\langle n_{d}\right\rangle$ decreases, eventually becoming negative at $U_{d} / t_{p d}=8$. At this point the "Hartree-Fock" $3 d$ level actually moves above the $2 p$. Consequently, even though $U_{d} / W^{-}$increases rapidly, the effective Coulomb integral $V_{i i} / W^{-}$saturates, leading to a saturation in the value of the magnetic crossover temperature $T_{N} / W^{-}$. Values of $V_{i i} / W^{-}$and $T_{N} / W^{-}$are plotted in Figs. 20(a) and 20(b) as functions of $U_{d} / W^{-}$.

An important point to note from Fig. 20(a) is that even when $U_{d} / W^{-}$becomes as large as 4.6 (corresponding to $U_{d} / t_{p d}=12$ ), $V_{i i} / W^{-}$does not exceed 0.75 , a value corresponding to intermediate coupling in a one-band picture. This observation lends support to the use of approximations such as the FLEX approximation for relatively large values of $U_{d} / t_{p d}$ in the charge-transfer regime (though not in the Hubbard regime, for the reasons stated previously). In particular, the choice of parameters $^{27-29}$ preferred for the high- $T_{c}$ superconductors (Sec. II) appears to lie within the range accessible from weak coupling.

Finally, we comment briefly on the reduction of the magnetic crossover scale by doping away from $\langle n\rangle=1$ in the one- and three-band models. As shown previously, $^{12,13}$ in the one-band model the commensurate antiferromagnetic instability persists at finite temperature for a limited range of fillings $\langle n\rangle \neq 1 .^{46}$ The decrease in $T_{N}$ away from half-filling is plotted in Fig. 21(a) for $U / t=8$. Note that the plot obeys strict particle-hole symmetry.

Behavior is qualitatively similar for the three-band model [Fig. 21(b)]. Note the absence of particle-hole symmetry, which is most significant for small $\varepsilon / t_{p d}$. For $\varepsilon / t_{p d}=2, U_{d} / t_{p d}=8, T_{N}$ actually peaks at $\langle n\rangle$ greater than 1. The fact that the crossover scale on the hole doping side ( $\langle n\rangle$ larger than 1 ) is consistently larger than the scale for equal electron doping ( $\langle n\rangle$ smaller than 1$)$ is consistent with previous simulation results $^{9}$ for the magnetic form factor. Note, however, that the asymmetry for realistic parameters in the charge-transfer regime is always relatively small.

## V. CONCLUSIONS

Our results confirm that in the intermediate-coupling regime the physics of the simplest $\mathrm{CuO}_{2}$ model is essentially the same as that of the one-band Hubbard model. A transformation to Wannier states, which accounts for $3 d-2 p$ hybridization in the low-energy band, yields a semiquantitative picture of the reduction of the Coulomb interaction between states near the Fermi surface. When this reduction is applied and three-band energies are scaled by the appropriate one-electron bandwidth $W^{-}$, results for the three- and one-band models come into close agreement.

In particular, our results indicate that the three-band

model (with $3d$ Coulomb interactions only) exhibits the same tendency toward $d_{x^2-y^2}$ superconductivity noted previously in one-band studies. We find no evidence for additional enhancement of extended-$s$ eigenvalues in the three-band model over those in the one-band model. The presence of a $3d$-$2p$ Coulomb interaction $U_{pd} \equiv V$ may, of course, alter this conclusion. $^{23}$

Finally, our results suggest that the accepted parameters$^{27-29}$ for the real cuprate materials ($U_d/t_{pd} \simeq 5.3-6.5$, $\varepsilon/t_{pd} \simeq 1.9-3.8$) place these systems in a weak- to intermediate-coupling regime. The presence of strong hybridization is essential to this conclusion, since the unrenormalized ratio of the Coulomb energy to the width of the bonding band, $U_d/W^-$, is considerably larger than 1. In the strong-coupling limit, the introduction of low-energy Zhang-Rice singlets$^{4,7}$ has been used to justify a one-band description for the charge-transfer regime; our results suggest that such a mapping continues to hold, at least semiquantitatively, for intermediate coupling provided the single band is composed of Wannier states with sharply reduced Coulomb interactions.

## ACKNOWLEDGMENTS
This work was supported in part by the National Science Foundation under Grant No. DMR92-12971, by the Office of Naval Research under Grant No. N00014-90-J-1747, and by the Alfred P. Sloan Foundation (N.E.B.).

$^{1}$J. G. Bednorz and K. A. Müller, Z. Phys. B 64, 18 (1986); M. K. Wu, J. R. Ashburn, C. J. Torng, P. H. Hor, R. L. Meng, L. Gao, Z. J. Huang, X. Q. Wang, and C. W. Chu, Phys. Rev. Lett. 58, 908 (1987).
$^{2}$V. J. Emery, Phys. Rev. Lett. 58, 2794 (1987).
$^{3}$P. W. Anderson, Science 235, 1196 (1987).
$^{4}$F. C. Zhang and T. M. Rice, Phys. Rev. B 37, 3759 (1988); V. J. Emery and G. Reiter, ibid., 38, 11 938 (1988).
$^{5}$For a review of work on the $t$-$J$ model, see, e.g., E. Dagotto, in Strongly Correlated Electron Systems II, edited by G. Baskaran et al. (World Scientific, Singapore, 1991), p. 77.
$^{6}$For a discussion of mean-field and perturbative approaches, see, e.g., M. Grilli, R. Raimondi, C. Castellani, C. di Castro, and G. Kotliar, in Strongly Correlated Electron Systems II (Ref. 5), p. 309.
$^{7}$C.-X Chen, H.-B. Schüttler, and A. J. Fedro, Phys. Rev. B 41, 2581 (1990).
$^{8}$G. Dopf, A. Muramatsu, and W. Hanke, Phys. Rev. B 41, 9264 (1990); Phys. Rev. Lett. 68, 353 (1992).
$^{9}$R. T. Scalettar, D. J. Scalapino, R. L. Sugar, and S. R. White, Phys. Rev. B 44, 770 (1991).
$^{10}$N. E. Bickers and D. J. Scalapino, Ann. Phys. (N.Y.) 193, 206 (1989).
$^{11}$N. E. Bickers, in Quantum and Classical Many-Body Theory in Condensed Matter Physics, edited by G. F. Giuliani and G. Vignale (World Scientific, Singapore, 1993).
$^{12}$N. E. Bickers, D. J. Scalapino, and S. R. White, Phys. Rev. Lett. 62, 961 (1989).
$^{13}$N. E. Bickers and S. R. White, Phys. Rev. B 43, 8044 (1991).
$^{14}$J. W. Serene and D. W. Hess, Phys. Rev. B 44, 3391 (1991).
$^{15}$G. Baym and L. P. Kadanoff, Phys. 124, 287 (1961); G. Baym, ibid. 127, 1391 (1962).
$^{16}$D. Vaknin, S. K. Sinha, D E. Moncton, D. C. Johnston, J. M. Newsom, C. R. Safinya, and H. E. King, Jr., Phys. Rev. Lett. 58, 2802 (1987).
$^{17}$J. M. Tranquada, D. E. Cox, W. Kunnmann, H. Moudden, G. Shirane, M. Suenaga, P. Zolliker, D. Vaknin, S. K. Sinha, M. S. Alvarez, A. J. Jacobson, and D. C. Johnston, Phys. Rev. Lett. 60, 156 (1988).
$^{18}$A. B. Migdal, Zh. Eksp. Teor. Fiz. 34, 1438 (1958) [Sov. Phys. JETP 7, 966 (1958)].
$^{19}$G. M. Eliashberg, Zh. Eksp. Teor. Fiz. 38, 966 (1960); [Sov. Phys. JETP 11, 696 (1960)].
$^{20}$Enlargements of the FLEX approximation have been proposed (see Ref. 13) which do appear quantitatively accurate for intermediate-coupling strengths. For a further discussion of these approaches, see, e.g., N. E. Bickers, in Strongly Correlated Electron Systems II (Ref. 5), p. 253.
$^{21}$In particular, the approach has furnished a useful framework for interpreting quantum Monte Carlo results and extrapolating calculations to temperature regimes not yet accessible by direct simulation.
$^{22}$As can be seen directly from Fig. 1, the direct oxygen-oxygen hopping integral $t_{pp}$ has the opposite sign from $t_{pd}$ everywhere in the lattice.
$^{23}$The potential importance of the interorbital Coulomb interaction has been particularly emphasized by C. M. Varma and collaborators. See, e.g., C. M. Varma, S. Schmitt-Rink, and E. Abrahams, Solid State Commun. 62, 681 (1987).
$^{24}$W. Weber, Z. Phys. B 70, 323 (1987).
$^{25}$D. L. Cox, M. Jarrell, C. Jayaprakash, H. R. Krishna-murthy, and J. Deisz, Phys. Rev. Lett. 62, 2188 (1989).
$^{26}$The addition of $t_{pp}$ is a trivial modification. In this case the model assumes an "Anderson-lattice" form. For describing mixed-valent and heavy-electron compounds, the choice $|t_{pp}| \gg |t_{pd}|$ would be appropriate.
$^{27}$A. K. McMahan, R. M. Martin, and S. Satpathy, Phys. Rev. B 38, 6650 (1988).
$^{28}$M. S. Hybertsen, M. Schlüter, and N. E. Christensen, Phys. Rev. B 39, 9028 (1989).
$^{29}$E. B. Stechel and D. R. Jennison, Phys. Rev. B 38, 4632 (1988).
$^{30}$A complete set of nonbonding $2p$ states $\bar{p}_{k\sigma}$ may be constructed orthonormal to $p_{k\sigma}$.
$^{31}$The self-energy $\Sigma_{d}(\phi)$ incorporates the external field to all orders and is viewed as a self-consistent functional of the (approximate) dressed Green's function $G_{d}$. For particle-hole off-diagonal, or pairing, fields, the appropriate $\Sigma_{d}$ is itself off diagonal or anomalous. For more details, see, e.g., Ref. 11.
$^{32}$More sophisticated approximations, which amount to self-consistent renormalization of the bare interaction $U_{d}$, are essential to obtain quantitative accuracy. For a discussion of results from one such approximation, the "pseudopotential parquet," see Ref. 13.
$^{33}$In two dimensions the FLEX approximation yields a mean-field-like estimate for the temperature below which the antiferromagnetic correlation length grows exponentially with decreasing temperature. We employ the notation $T_{N}$ for this scale in analogy with the three-dimensional Néel temperature.
$^{34}$D. J. Scalapino, E. Loh, and J. E. Hirsch, Phys. Rev. B 34, 8190 (1986).

$^{35}$J. Miyake, S. Schmitt-Rink, and C. M. Varma, Phys. Rev. B **34**, 6554 (1986).

$^{36}$N. E. Bickers, D. J. Scalapino, and R. T. Scalettar, Int. J. Mod. Phys. B **1**, 687 (1987).

$^{37}$G. Kotliar, Phys. Rev. B **37**, 3664 (1988).

$^{38}$C. Gros, Phys. Rev. B **38**, 931 (1988).

$^{39}$S. R. White, D. J. Scalapino, R. L. Sugar, N. E. Bickers, and R. T. Scalettar, Phys. Rev. B **39**, 839 (1989).

$^{40}$N. D. Mermin and H. Wagner, Phys. Rev. Lett. **17**, 1133 (1966); P. C. Hohenberg, Phys. Rev. **158**, 383 (1987).

$^{41}$S. Chakravarty, B. Halperin, and D. Nelson, Phys. Rev. Lett. **60**, 1057 (1988); Phys. Rev. B. **39**, 2344 (1989).

$^{42}$J. Reger and A. P. Young, Phys. Rev. B **37**, 5978 (1988).

$^{43}$J. E. Hirsch and S. Tang, Phys. Rev. Lett. **62**, 591 (1989).

$^{44}$R. T. Scalettar, E. Loh, J. Gubernatis, A. Moreo, S. R. White, D. J. Scalapino, R. L. Sugar, and E. Dagotto, Phys. Rev. Lett. **62**, 1407 (1989).

$^{45}$N. E. Bickers and D. J. Scalapino, Phys. Rev. B **46**, 8050 (1992).

$^{46}$This is not to say that the ground state is commensurate for $\langle n \rangle \neq 1$; a first-order transition to an incommensurate magnetic state presumably intervenes at $T < T_N$ for all $\langle n \rangle \neq 1$ (at least within approximations such as the FLEX approximation).