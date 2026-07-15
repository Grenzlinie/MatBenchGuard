# Correlation functions for interacting fermions in the Gutzwiller ansatz

Florian Gebhard and Dieter Vollhardt
Institut für Theoretische Physik C, Technische Hochschule Aachen, Sommerfeldstr 26/28, D-5100 Aachen,
Federal Republic of Germany
(Received 22 February 1988)

We make use of a recently developed diagrammatic theory to calculate correlation functions for interacting fermions of Hubbard-type models in terms of the Gutzwiller wave function. Of the eleven nontrivial correlation functions involving the spin, density, empty and doubly occupied sites, and local Cooper pairs, four are shown to be independent. They are expressed as a power series in a suitably chosen correlation parameter, whose terms are represented diagrammatically. In one dimension these terms may be evaluated to arbitrary order by employing symmetry relations. This allows for an analytic, approximation-free calculation of the correlation functions for arbitrary momentum, particle density, and interaction strength. In the atomic limit the momentum-dependent spin-correlation function shows an antiferromagnetic divergence at half filling in all dimensions. In one dimension the behavior is in very good agreement with all exact analytic and numerical results for the antiferromagnetic Heisenberg chain. Hole-hole correlations also compare very well with exact results. However, correlations between holes and doubly occupied sites appear insufficient. Superconducting correlations involving on-site, singlet Cooper pairs are suppressed. The results allow for an analytic evaluation of the ground-state energy of a large class of extended Hubbard models in terms of the Gutzwiller wave function. Thus they provide exact upper bounds for their ground-state energies.

## I. INTRODUCTION

Investigations of strongly correlated Fermi systems in recent years have been a particularly vital field of research in condensed-matter physics. However, the intense interest is in striking contrast to what is actually reliably known about these systems. This has become very clear again in the case of the well-known Hubbard model, $^{1-3}$ whose two-dimensional version is hoped to provide insight into the pairing mechanism of high-$T_c$ superconductivity. $^{4}$ Although this is about the simplest model for interacting fermions on a lattice, details about the correlations between the particles are not yet well understood. Even in one dimension $(d=1)$ where Lieb and $\mathrm{Wu}^5$ have obtained the ground-state energy by the Bethe ansatz, correlation functions are essentially unknown except for limiting cases, i.e., the nearest-$^{6}$ and next-nearest-neighbor $^7$ spin-correlation function at infinite interaction and half-filled band. In higher than one dimension not even this is known. Here numerical Monte Carlo methods have proved to be very valuable and, indeed, have yielded important insight into the ground-state and thermodynamic properties of Hubbard-type models in $d=1,2,3.^{8-10}$ On the other hand, their applicability is naturally limited to rather small systems, i.e., particle numbers. In this situation variational methods, which work with explicit wave functions, are among the very few analytic tools available for the study of correlated fermions in the thermodynamic limit.

The simplest variational wave function for Hubbard-type models is the Gutzwiller wave function (GWF). $^1$ In spite of its simplicity an exact evaluation of expectation values in terms of the GWF was not possible until recently. Instead, the results of an approximate calculation of the ground-state energy, also due to Gutzwiller, $^{11}$ were used. The Gutzwiller approximation $^{11}$ (GA) yields very simple results in a number of cases [metal-insulator transition (Refs. 12 and 13), normal liquid $^3$He (Refs. 14-16), heavy fermions (Refs. 17-20)], which allow contact to be made with well-established theories like Fermi-liquid theory, and which are therefore generally acknowledged as very "physical." To establish the reasonableness of the GWF itself, one has to calculate expectation values without making further approximation. Such evaluations of the ground-state energy and correlation functions were first performed by Kaplan, Horsch, and Fulde $^{21}$ and Kaplan and Horsch $^{22}$ for finite rings using numerical techniques. Hashimoto $^{23}$ combined analytic and numerical methods to derive results for the thermodynamic limit and Horsch, $^{24}$ Baeriswyl and Maki, $^{25}$ and Baeriswyl, Carmelo, and Maki $^{26}$ calculated the ground-state energy of the Hubbard model analytically for small interaction strengths. Significant progress was then made by Gros, Joynt, and Rice $^{27}$ who obtained detailed numerical results for spin-spin and hole-hole correlations in terms of the GWF for $d=1$ and infinite repulsion, and independently by Yokoyama and Shiba $^{28}$ who calculated the spin-spin correlations, density-density correlations and the momentum distribution in $d=1$, as well as the ground-state energy in $d=1,2,3$ for general interaction strengths.

Most recently, Metzner and Vollhardt $^{29,30}$ developed an analytic approach which, for the first time, allowed for an exact evaluation of expectation values in terms of the GWF for arbitrary particle density and interaction strength, at least in $d=1$ and $d=\infty$. (In the latter case the results of the GA obtained for the GWF are found to

be exact. $^{30}$ The evaluations are made tractable by (i) a suitable choice of expansion parameter and (ii) the introduction of special (" $\delta$-less") contractions, which only involve anticommuting numbers. In this way the variational ground-state energy of the Hubbard model and the momentum distribution in $d=1$ were obtained without approximation. $^{29,30}$

The method is equally applicable to the evaluation of correlation functions in terms of the GWF for arbitrary band filling and interaction strength in $d=1 .^{31}$ In this paper we give a detailed description of how this is achieved. In particular, we show how to make use of symmetries to relate different correlation functions (Sec. III). In Sec. IV the diagrammatic analysis is explained and in Sec. V the polynomial structure of correlation functions in one dimension is identified. In Secs. VI-IX the cooperation of symmetry and structure is shown to allow for the exact evaluation in one dimension. In Sec. $\mathrm{X}$ the extended Hubbard model is addressed and in Sec. XI higher dimensions are discussed.

## II. DEFINITIONS

We consider the Hubbard model $^{1-3}$
$$
\hat{H}=\sum_{i, j, \sigma} t_{i j} \hat{c}_{i \sigma}^{\dagger} \hat{c}_{j \sigma}+U \sum_{i} \hat{n}_{i \uparrow} \hat{n}_{i \downarrow},
$$
where $\hat{c}_{i \sigma}^{\dagger}$ creates a $\sigma$ spin on site $i$, etc. and $\hat{n}_{i \sigma}=\hat{c}_{i \sigma}^{\dagger} \hat{c}_{i \sigma}$. The on-site interaction in (1) may also be written as $U \sum_{i} \hat{D}_{i}=U \hat{D}$, where $\hat{D}_{i}=\hat{n}_{i \uparrow} \hat{n}_{i \downarrow}$ is the number operator for double occupancy at site $i$. More complicated interactions (e.g., nearest neighbor) have been neglected in (1); they are discussed in Sec. X. The Gutzwiller wavefunction $^{1,11}$ (GWF)
$$
\begin{aligned}
\left|\Psi_{G}\right\rangle & =\prod_{i}\left[1-(1-g) \hat{D}_{i}\right]\left|\Psi_{0}\right\rangle \\
& =g^{\hat{D}}\left|\Psi_{0}\right\rangle
\end{aligned}
$$
is custom-tailored to treat the effect of the on-site interaction in (1) and is thus the simplest correlated wavefunction. Here $0 \leq g \leq 1$ is a variational parameter and $\left|\Psi_{0}\right\rangle$ is the noninteracting ground state (Slater determinant). The correlation factor in (2) reduces local density fluctuations in a global fashion. In the Hubbard model (1) a lattice may be empty, singly occupied by either $\uparrow$ or $\downarrow$, or doubly occupied. The correlations between these entities is described by the general correlation function (CF)
$$
C_{j}^{X Y}=\frac{1}{L} \sum_{i}\left\langle\hat{X}_{i} \hat{Y}_{i+j}\right\rangle-\langle\hat{X}\rangle\langle\hat{Y}\rangle,
$$
where $L$ is the number of lattice sites and
$$
\langle\hat{O}\rangle=\frac{\left\langle\Psi_{G}|\hat{O}| \Psi_{G}\right\rangle}{\left\langle\Psi_{G} \mid \Psi_{G}\right\rangle}.
$$

Here the operators $\hat{X}_{i}, \hat{Y}_{i}$ [with $\hat{X}=(1 / L) \sum_{i} \hat{X}_{i}$, etc.] are any one of the following local operators
$$
\hat{S}_{i}^{z} \equiv \hat{n}_{i \uparrow}-\hat{n}_{i \downarrow} \quad(\text { spin }),
$$

$$
\hat{N}_{i} \equiv \hat{n}_{i \uparrow}+\hat{n}_{i \downarrow} \quad(\text { density }),
$$

$$
\hat{D}_{i} \equiv \hat{n}_{i \uparrow} \hat{n}_{i \downarrow} \quad \text { (doubly occupied site) },
$$

$$
\hat{H}_{i} \equiv\left(1-\hat{n}_{i \uparrow}\right)\left(1-\hat{n}_{i \downarrow}\right) \quad \text { (empty site or "hole") }.
$$

Furthermore, to study the role of superconducting fluctuations in $\left|\Psi_{G}\right\rangle$ we investigate the correlation function
$$
C_{j}^{\text {sup }}=\frac{1}{L} \sum_{i}\left\langle\hat{c}_{i \uparrow} \hat{c}_{i \downarrow} \hat{c}_{i+j \uparrow}^{\dagger} \hat{c}_{i+j \downarrow}^{\dagger}\right\rangle
$$
which probes local Cooper pairs with spin $s=0 .^{8}$

In the following we consider a nonmagnetic ground state with fixed particle number $N_{\sigma}=n_{\sigma} L$
$$
n_{\uparrow}=n_{\downarrow}=\frac{n}{2} \leq \frac{1}{2},
$$

$$
d=\frac{1}{L}\langle\hat{D}\rangle,
$$
where $d$ is the density of doubly occupied sites (not the dimension). $\left|\Psi_{G}\right\rangle$ is not an eigenfunction of $\hat{D}$; hence $d$ represents the most probable value of doubly occupied sites in $\left|\Psi_{G}\right\rangle$. Subtracting $\langle\hat{X}\rangle\langle\hat{Y}\rangle$ in (3) implies that the CF's vanish for $j \rightarrow \infty$ unless a symmetry is broken.

For $n_{\uparrow}=n_{\downarrow}$ the definition (3) with (5a)-(5d) yields ten CF's, which, however, are not independent. For example, the following relations hold:
$$
C_{j}^{D H}=C_{j}^{D D}-C_{j}^{N D},
$$

$$
C_{j}^{H H}=C_{j}^{N N}-2 C_{j}^{N D}+C_{j}^{D D}.
$$

Altogether there are only four independent CF's. These CF's depend explicitly on the particle density $n$ and the interaction of the model under consideration (e.g., $U$ in the Hubbard model). We note that in the present approach based on the GWF the interaction strength is parametrized by the correlation parameter $g$ in (2). In the following we will therefore express the CF's as functions of $g$. The connection of $g$ to explicit interaction parameters is achieved by diagonalizing the respective model Hamiltonian [e.g., the Hubbard model (1) as done in Refs. 29 and 30] and minimizing the energy with respect to $g$.

## III. SYMMETRIES

The CF's defined above are related by special particle-hole $(p-h)$ symmetries. Exploiting these symmetries introduces great simplifications. To this end we consider alternating (i.e., $A B$-type lattices) such as simple cubic or bcc lattices, which yield a connected Fermi surface for the noninteracting ground state. We now define two $p-h$ transformations $T_{1}$ and $T_{2}$.

(1) The transformation $T_{1}$ acts on both spins at site $i$
$$
\begin{aligned}
& \hat{c}_{i \sigma} \rightarrow(-1)^{i} \hat{c}_{i \sigma}^{\dagger}, \\
& \hat{c}_{i \sigma}^{\dagger} \rightarrow(-1)^{i} \hat{c}_{i \sigma},
\end{aligned}
$$
where
$$
(-1)^{i}= \begin{cases}-1 & \text { if } i \in A \text { lattice } \\ 1 & \text { if } i \in B \text { lattice }.\end{cases}
$$

This implies

$$
\hat{S}_{i}^{z} \rightarrow-\hat{S}_{i}^{z},
\tag{11a}
$$

$$
\hat{N}_{i} \rightarrow 2-\hat{N}_{i},
\tag{11b}
$$

$$
\hat{D}_{i} \rightarrow 1-\hat{N}_{i}+\hat{D}_{i}=\hat{H}_{i},
\tag{11c}
$$

$$
\hat{H}_{i} \rightarrow \hat{D}_{i}.
\tag{11d}
$$

The transformation (9) leaves the correlation factor in the GWF invariant (up to a trivial normalization factor), such that
$$
g^{\hat{D}}\left|\Psi_{0}(n)\right\rangle \rightarrow g^{\hat{D}}\left|\Psi_{0}(\bar{n})\right\rangle,
\tag{12}
$$
where $\bar{n}=2-n$. Writing the $g$ and $n$ dependence of $C_{j}^{X Y}$ explicitly, the following relations hold:

$$
C_{j}^{S S}(g, n)=C_{j}^{S S}(g, \bar{n}),
\tag{13a}
$$

$$
C_{j}^{N N}(g, n)=C_{j}^{N N}(g, \bar{n}),
\tag{13b}
$$

$$
C_{j}^{D D}(g, n)=C_{j}^{H H}(g, \bar{n}),
\tag{13c}
$$

$$
C_{j}^{N D}(g, n)=\frac{1}{2}\left[C_{j}^{N N}(g, n)+C_{j}^{D D}(g, n)-C_{j}^{D D}(g, \bar{n})\right],
\tag{13d}
$$

$$
C_{j}^{\text {sup }}(g, n)=(n-1) \delta_{j, 0}+C_{j}^{\text {sup }}(g, \bar{n}).
\tag{13e}
$$

(2) The transformation $T_{2}$ is only defined for a half-filled band ($n=1$) and only acts on one spin component (say, on $\uparrow$) while leaving the other unchanged:
$$
\begin{aligned}
& \hat{c}_{i \uparrow}^{\dagger} \rightarrow(-1)^{i} \hat{c}_{i \uparrow}, \\
& \hat{c}_{i \uparrow} \rightarrow(-1)^{i} \hat{c}_{i \uparrow}^{\dagger}, \\
& \hat{c}_{i \downarrow}^{\dagger}, \hat{c}_{i \downarrow}, \quad \text { unchanged }.
\end{aligned}
\tag{14}
$$

This implies
$$
\hat{S}_{i}^{z} \rightarrow 1-\hat{N}_{i},
\tag{15a}
$$

$$
\hat{N}_{i} \rightarrow 1-\hat{S}_{i}^{z},
\tag{15b}
$$

$$
\hat{D}_{i} \rightarrow \hat{n}_{i \downarrow}-\hat{D}_{i},
\tag{15c}
$$
and hence the GWF transforms as
$$
\left|\Psi_{G}(g, n=1)\right\rangle \rightarrow\left|\Psi_{G}\left(\frac{1}{g}, n=1\right)\right\rangle,
\tag{16}
$$
thereby connecting states with $0 \leq g \leq 1$ and $1 \leq g \leq \infty$.
This transformation relates the CF's as
$$
C_{j}^{S S}(g, 1)=C_{j}^{N N}\left(\frac{1}{g}, 1\right),
\tag{17a}
$$

$$
C_{j}^{D D}(g, 1)=\frac{1}{4}\left[C_{j}^{N N}(g, 1)-C_{j}^{S S}(g, 1)\right]+C_{j}^{D D}\left(\frac{1}{g}, 1\right),
\tag{17b}
$$
and the double occupancy at $n=1$ as $d(g)=\frac{1}{2}-d(1 / g)$.
Furthermore, applying a unitary transformation
$$
\hat{\alpha}_{i}^{\dagger}=\frac{1}{\sqrt{2}}\left(\hat{c}_{i \uparrow}^{\dagger}+\hat{c}_{i \downarrow}^{\dagger}\right),
\tag{18a}
$$

$$
\hat{\beta}_{i}^{\dagger}=\frac{1}{\sqrt{2}}\left(\hat{c}_{i \uparrow}^{\dagger}-\hat{c}_{i \downarrow}^{\dagger}\right),
\tag{18b}
$$

$$
\hat{n}_{i \alpha} \equiv \hat{\alpha}_{i}^{\dagger} \hat{\alpha}_{i}, \text { etc. },
\tag{18c}
$$
before letting $T_{2}$ act, leads to
$$
C_{j}^{\text {sup }}(g, n=1)=-\frac{1}{2}(-1)^{j} C_{j}^{N N}(g, n=1),
\tag{19}
$$
in fact, as will be shown later, for general $n, C_{j}^{\text {sup }}$ is completely determined by $C_{j}^{S S}$. Therefore we may limit ourselves to the calculation of altogether only four CF's, i.e., $C_{j}^{S S}, C_{j}^{N N}, C_{j}^{D D}, C_{j}^{N D}$. Equation (19) immediately implies that for $n=1$ and a strong, short-range repulsion $U$ the superconducting fluctuations for on-site Copperpairs are just as suppressed as the density fluctuations.

The fact that for $n=1$, spin and density fluctuations are closely related and change their role for $g \rightarrow 1 / g$ was already observed by Vollhardt $^{15}$ for the results of the GA. There the Landau parameters $F_{0}^{a}, F_{0}^{s}$ entering the spin and density susceptibility where found to be related by $F_{0}^{a}(U)=F_{0}^{s}(-U)$. Since in the GA, $g$ is given by
$$
g=\frac{1-\bar{U}}{1+\bar{U}},
\tag{20}
$$
where $\bar{U}=U /\left(8\left|\varepsilon_{0}\right|\right)$, with $\left|\varepsilon_{0}\right|$ the average energy of the uncorrelated particles, a change of $U \rightarrow-U$ does indeed imply $g \rightarrow 1 / g$.

## IV. DIAGRAMMATIC REPRESENTATION OF CORRELATION FUNCTIONS

To obtain $C_{\mathfrak{f}}^{S S}, C_{\mathfrak{f}}^{N N}, C_{\mathfrak{f}}^{D D}, C_{\mathfrak{f}}^{N D}$, where $\mathfrak{f}$ is a $d$-dimensional lattice vector, the expectation values of four different operators have to be evaluated:
$$
\hat{O}_{\mathfrak{f}}^{(1)}=\frac{1}{L} \sum_{\mathfrak{h}} \hat{n}_{\mathfrak{h} \uparrow} \hat{n}_{\mathfrak{f}+\mathfrak{h} \uparrow},
\tag{21a}
$$

$$
\hat{O}_{\mathfrak{f}}^{(2)}=\frac{1}{L} \sum_{\mathfrak{h}} \hat{n}_{\mathfrak{h} \uparrow} \hat{n}_{\mathfrak{f}+\mathfrak{h} \downarrow},
\tag{21b}
$$

$$
\hat{O}_{\mathfrak{f}}^{(3)}=\frac{1}{L} \sum_{\mathfrak{h}} \hat{n}_{\mathfrak{h} \uparrow} \hat{D}_{\mathfrak{f}+\mathfrak{h}},
\tag{21c}
$$

$$
\hat{O}_{\mathfrak{f}}^{(4)}=\frac{1}{L} \sum_{\mathfrak{h}} \hat{D}_{\mathfrak{h}} \hat{D}_{\mathfrak{f}+\mathfrak{h}}.
\tag{21d}
$$

All other contributions are obtained by the inversion symmetry $C_{\mathfrak{f}}^{X Y}=C_{-\mathfrak{f}}^{X Y}$ and spin-flip symmetry.

The calculation of $\left\langle\hat{O}_{\mathfrak{f}}^{(i)}\right\rangle, i=1, \ldots, 4$, will now be exemplified in the case of $\left\langle\hat{O}_{\mathfrak{f}}^{(1)}\right\rangle$. To make use of the formalism developed earlier $^{29,30}$ for the evaluation of expectation values as in (4), we first treat the numerator in (4). We note that all operators $\hat{O}_{\mathfrak{f}}^{(i)}$ in (21) commute with $\hat{D}_{\mathfrak{h}}$. Expanding the correlation factor of the GWF in (2a) as a sum over different lattice sites (prime on summation symbol), the numerator may be written as

$$
\left\langle\Psi_{G}\left|\hat{O}_{\mathbf{f}}^{(1)}\right| \Psi_{G}\right\rangle=\left\langle\hat{O}_{\mathbf{f}}^{(1)}\right\rangle_{0}+\frac{1}{L} \sum_{m=1}^{L} \frac{\left(g^{2}-1\right)^{m}}{m!} \sum_{\mathbf{f}_{1} \ldots \mathbf{f}_{m}}^{\prime} \sum_{\mathbf{h}}^{\prime}\left\langle\hat{n}_{\mathbf{h} \uparrow} \hat{n}_{\mathbf{f}+\mathbf{h} \uparrow} \hat{D}_{\mathbf{f}_{1}}, \ldots, \hat{D}_{\mathbf{f}_{m}}\right\rangle_{0},
\tag{22}
$$

where $\langle\ldots\rangle_{0}$ implies the expectation value in the noninteracting ground state. Since $\hat{O}_{\mathbf{f}}^{(1)}$ is itself a sum over lattice sites we first separate out the case $\mathbf{f}=0$, with $\left\langle\hat{O}_{0}^{(1)}\right\rangle_{0}=n / 2$, and in the following assume $\mathbf{f} \neq 0$; hence $\mathbf{h} \neq \mathbf{f}+\mathbf{h}$ in (22). We now want to make all site indices on the right-hand side (rhs) of (22) different, because then the calculation of $\langle\ldots\rangle_{0}$ via Wick's theorem only involves contractions without the usual $\delta_{i j}$ terms (" $\delta$-less contractions"). ${ }^{29,30}$ This is an essential feature without which an analytic evaluation would not be tractable. In (22) three cases have to be distinguished: (a) neither $\mathbf{h}$ nor $\mathbf{f}+\mathbf{h}$ belong to $\mathbf{f}_{i}, i=1, \ldots, m$; (b) either $\mathbf{h}$ or $\mathbf{f}+\mathbf{h}$ belongs to $\mathbf{f}_{i}$; (c) $\mathbf{h}$ and $\mathbf{f}+\mathbf{h}$ belong to $\mathbf{f}_{i}$ ( $m \geq 2$ necessary). Accordingly, the second term on the rhs of (22) involves the terms

$$
\begin{aligned}
X_{\mathbf{f}}^{(a)}= & \sum_{m=0}^{L} \frac{\left(g^{2}-1\right)^{m}}{m!} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m+1}}^{\prime}\left\langle\hat{n}_{\mathbf{f}_{1} \uparrow} \hat{n}_{\mathbf{f}_{1}+\mathbf{f} \uparrow} \hat{D}_{\mathbf{f}_{2}}, \ldots, \hat{D}_{\mathbf{f}_{m+1}}\right\rangle_{0},
\end{aligned}
\tag{23a}
$$

$$
\begin{aligned}
X_{\mathbf{f}}^{(b)}= & \sum_{m=1}^{L+1} \frac{\left(g^{2}-1\right)^{m}}{(m-1) !} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m}}^{\prime}\left\langle\hat{n}_{\mathbf{f}_{1} \uparrow} \hat{D}_{\mathbf{f}_{1}+\mathbf{f}} \hat{D}_{\mathbf{f}_{2}}, \ldots, \hat{D}_{\mathbf{f}_{m}}\right\rangle_{0},
\end{aligned}
\tag{23b}
$$

$$
\begin{aligned}
X_{\mathbf{f}}^{(c)}= & \sum_{m=2}^{L+2} \frac{\left(g^{2}-1\right)^{m}}{(m-2) !} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m-1}}^{\prime}\left\langle\hat{D}_{\mathbf{f}_{1}} \hat{D}_{\mathbf{f}_{1}+\mathbf{f}} \hat{D}_{\mathbf{f}_{2}}, \ldots, \hat{D}_{\mathbf{f}_{m-1}}\right\rangle_{0}.
\end{aligned}
\tag{23c}
$$

Now Wick's theorem is applied to calculate the expectation values in (23). It transforms the $\langle\ldots\rangle_{0}$ into $\{\ldots\}_{0}$, i.e., the sum over all possible fully contracted products. ${ }^{29,30}$ For example, in the case of (23a) we have

$$
\begin{aligned}
X_{\mathbf{f}}^{(a)}= & \sum_{m=0}^{L} \frac{\left(g^{2}-1\right)^{m}}{m!} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m+1}}^{\prime}\left\{n_{\mathbf{f}_{1} \uparrow} n_{\mathbf{f}_{1}+\mathbf{f} \uparrow} D_{\mathbf{f}_{2}}, \ldots, D_{\mathbf{f}_{m+1}}\right\}_{0}
\end{aligned}
\tag{24}
$$

The only nonvanishing contractions are given by the one-particle density matrix and are defined as

$$
\left\{c_{i \sigma}^{\dagger} c_{j \sigma}\right\}_{0} \equiv\left\langle\hat{c}_{i \sigma}^{\dagger} \hat{c}_{j \sigma}\right\rangle_{0} \equiv P_{i j, \sigma}
\tag{25a}
$$

and, in particular,

$$
\left\{c_{j \sigma} c_{i \sigma}^{\dagger}\right\}_{0} \equiv\left\langle\hat{c}_{j \sigma} \hat{c}_{i \sigma}^{\dagger}\right\rangle_{0} \equiv-P_{i j, \sigma}.
\tag{25b}
$$

We note that in (25b) the usual $\delta_{i j}$ term does not appear since $i \neq j$ (" $\delta$-less contractions"). However, $\{\ldots\}_{0}$ as defined by (25) corresponds to a product of two determinants (one for $\uparrow$, one for $\downarrow$ ) and hence $\{\ldots\}_{0}=0$ if any two site-indices are put equal. Therefore we may formally extend the sum in (24) to an unrestricted lattice sum since this does not create even contributions. ${ }^{29,30}$ [Of course, the definition of $\{\ldots\}_{0}$ is still given by (25)]. Hence the prime on the sum in (24) may be dropped

$$
\begin{aligned}
X_{\mathbf{f}}^{(a)}= & \sum_{m=0}^{L} \frac{\left(g^{2}-1\right)^{m}}{m!} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m+1}}\left\{n_{\mathbf{f}_{1} \uparrow} n_{\mathbf{f}_{1}+\mathbf{f} \uparrow} D_{\mathbf{f}_{2}}, \ldots, D_{\mathbf{f}_{m+1}}\right\}_{0}.
\end{aligned}
\tag{26}
$$

The same holds true for $X_{\mathbf{f}}^{(b)}$ and $X_{\mathbf{f}}^{(c)}$ in (23b) and (23c). Note, that the objects in $\{\ldots\}_{0}$ are no longer operators but are anticommuting numbers similar to Grassmann variables. This becomes obvious if we write $\{\ldots\}_{0}$ in (26) as a product of determinants (with $\mathbf{f}_{1} \equiv 1$ and $\mathbf{f}_{1}+\mathbf{f} \equiv 1^{\prime}$ )

$$
\left\{n_{1 \uparrow} n_{1^{\prime} \uparrow} D_{2}, \ldots, D_{m+1}\right\}_{0}=\left|\begin{array}{ccccc}
P_{1,1, \uparrow} & P_{1,1^{\prime}, \uparrow} & P_{1,2, \uparrow} & \cdots & P_{1, m+1, \uparrow} \\
P_{1^{\prime}, 1, \uparrow} & P_{1^{\prime}, 1^{\prime}, \uparrow} & P_{1^{\prime}, 2, \uparrow} & \cdots & P_{1^{\prime}, m+1, \uparrow} \\
\vdots & & & & \vdots \\
P_{m+1,1, \uparrow} & & & \cdots & P_{m+1, m+1, \uparrow}
\end{array}\right| \times\left|\begin{array}{ccccc}
P_{2,2, \downarrow} & P_{2,3, \downarrow} & \cdots & P_{2, m+1, \downarrow} \\
P_{3,2, \downarrow} & P_{3,3, \downarrow} & \cdots & P_{3, m+1, \downarrow} \\
\vdots & & & \vdots \\
P_{m+1,2, \downarrow} & & \cdots & P_{m+1, m+1, \downarrow}
\end{array}\right| .
\tag{27}
$$


This shows, in particular, for $\mathbf{f}=0$ (26) vanishes. The contractions defined above may be represented graphically. One simply assigns a line to every $P_{\mathbf{f g}, \sigma}$ (solid line for $\uparrow$; broken line for $\downarrow$ ) which connects the points $\mathbf{f}$ and $\mathbf{g}$. The points $\mathbf{f}_{1}$ and $\mathbf{f}+\mathbf{f}_{1}$ are chosen as the two external lattice points of the graph, i.e., they mark the left and right vertex of the graph, respectively [see Fig. 1 for (27) with $m=1$ ]. The evaluation of the graphs in the thermodynamic limit $(L \rightarrow \infty)$ is done most conveniently in $\mathbf{k}$ space, using

$$
P_{\mathbf{f g}, \sigma}=\int \frac{d \mathbf{k}}{(2 \pi)^{d}} e^{-i \mathbf{k}(\mathbf{f}-\mathbf{g})} n_{\mathbf{k} \sigma}^{0},
$$

where $n_{\mathbf{k} \sigma}^{0}$ is the momentum distribution of the noninteracting $\sigma$ spins. Here the lattice spacing is chosen such that the volume of the primitive unit cell is $V_{c}=1$, while in $\mathbf{k}$ space the volume of the primitive unit cell is $V_{c}^{*}=(2 \pi)^{d}$. The resulting graphs are either "connected" [Figs. 1(b)-1(f)] or disconnected [Figs. 1(a)-1(c)], with a connected graph defined as one where it is possible to go from any internal lattice point to $\mathbf{f}_{1}$ or $\mathbf{f}+\mathbf{f}_{1}$ on a continuous fermion line. As usual the disconnected diagrams of any expectation value are canceled by the norm $\left\langle\Psi_{G} \mid \Psi_{G}\right\rangle$ ("linked cluster theorem"32,33) in the thermodynamic limit. Hence only connected diagrams in $\{\ldots\}_{0}$, indicated by $\{\ldots\}_{0}^{c}$, need to be taken into account.

The connected graphs may themselves be classified into "half-connected" (HC) and "fully-connected" (FC) diagrams; see Figs. 1(b) and 1(f) and Figs. 1(d) and 1(e) respectively. Here an FC graph is one where it is possible to go from any internal lattice point to both $\mathbf{f}_{1}$ and $\mathbf{f}+\mathbf{f}_{1}$ on a continuous fermion line. The HC graphs are trivial since the summation indices may always be rearranged such that $\mathbf{f}$ no longer occurs, i.e., one obtains $\mathbf{f}$ independent contributions to $C_{\mathbf{f}}^{X Y}$. These are precisely the terms which are subtracted by $\langle\hat{X}\rangle\langle\hat{Y}\rangle$ in $C_{\mathbf{f}}^{X Y}$ [see (3)]. Physically this corresponds to $C_{\mathbf{f}}^{X Y} \rightarrow 0$ for $|\mathbf{f}| \rightarrow \infty$. Hence we only have to consider the FC contributions to $\{\ldots\}_{0}^{c}$, indicated by $\{\ldots\}_{0}^{\mathrm{FC}}$, and may then ignore the $\langle\hat{X}\rangle\langle\hat{Y}\rangle$ term.

![](./images/811683925553315842_1.jpg)

FIG. 1. Graphs corresponding to the contractions of $\left\{n_{1 \uparrow} n_{1^{\prime} \uparrow} D_{2}\right\}_{0}$, i.e., (27) with $m=1$, where 1 and $1^{\prime}$ are the external vertices and 2 is an internal vertex. (a),(c): disconnected diagrams; (b),(f): half-connected diagrams. (d),(e): fully-connected diagrams.

For example, the expectation value of $\hat{O}_{\mathbf{f}}^{(1)},(21 \mathrm{a})$ is altogether given by

$$
\begin{aligned}
\left\langle\hat{O}_{\mathbf{f}}^{(1)}\right\rangle= & \frac{1}{L} \sum_{\mathbf{h}}\left\langle\hat{n}_{\mathbf{h} \uparrow} \hat{n}_{\hat{f}+\mathbf{h} \uparrow}\right\rangle \\
= & \delta_{\mathbf{f}, 0} \frac{n}{2}+\left\lfloor\frac{n}{2}\right\rceil^{2} \\
& +\sum_{m=0}^{\infty}\left(g^{2}-1\right)^{m}\left(Y_{\mathbf{f}, m}^{(1)}+2 Y_{\mathbf{f}, m}^{(2)}+Y_{\mathbf{f}, m}^{(3)}\right), \quad(29 \mathrm{~b})
\end{aligned}
$$

where the second term on the right-hand side of (29b) is due to the HC diagrams and the third term is given by

$$
\begin{aligned}
Y_{\mathbf{f}, m}^{(1)}= & \frac{1}{L} \frac{1}{m !} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m+1}}\left\{n_{\mathbf{f}_{1} \uparrow} n_{\mathbf{f}_{1}+\mathbf{f} \uparrow} D_{\mathbf{f}_{2}}, \ldots, D_{\mathbf{f}_{m+1}}\right\}_{0}^{\mathrm{FC}}, \\
& m \geq 0 \quad(30 \mathrm{a}) \\
Y_{\mathbf{f}, m}^{(2)}= & \frac{1}{L} \frac{1}{(m-1) !} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m}}\left\{n_{\mathbf{f}_{1} \uparrow} D_{\mathbf{f}_{1}+\mathbf{f}} D_{\mathbf{f}_{2}}, \ldots, D_{\mathbf{f}_{m}}\right\}_{0}^{\mathrm{FC}}, \\
& m \geq 1 \quad(30 \mathrm{~b}) \\
Y_{\mathbf{f}, m}^{(3)}= & \frac{1}{L} \frac{1}{(m-2) !} \\
& \times \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m-1}}\left\{D_{\mathbf{f}_{1}} D_{\mathbf{f}_{1}+\mathbf{f}} D_{\mathbf{f}_{2}}, \ldots, D_{\mathbf{f}_{m-1}}\right\}_{0}^{\mathrm{FC}}, \\
& m \geq 2 \quad(30 \mathrm{c})
\end{aligned}
$$

and $Y_{\mathbf{f}, 0}^{(1)}=Y_{\mathbf{f}, 0}^{(2)}=Y_{\mathbf{f}, 0}^{(3)}=0$. Similarly, the expectation value of $\hat{O}_{\mathbf{f}}^{(2)},(21 \mathrm{a})$, is given by

$$
\begin{aligned}
\left\langle\hat{O}_{\mathbf{f}}^{(2)}\right\rangle= & \frac{1}{L} \sum_{\mathbf{h}}\left\langle\hat{n}_{\mathbf{h} \uparrow} \hat{n}_{\mathbf{f}+\mathbf{h} \downarrow}\right\rangle \\
= & \delta_{\mathbf{f}, 0} \sum_{m=1}^{\infty}\left(g^{2}-1\right)^{m} c_{m}+\left\lfloor\frac{n}{2}\right\rceil^{2} \\
& +\sum_{m=0}^{\infty}\left(g^{2}-1\right)^{m}\left(2 Y_{\mathbf{f}, m}^{(2)}+Y_{\mathbf{f}, m}^{(3)}+Y_{\mathbf{f}, m}^{(4)}\right)
\end{aligned}
$$

with

$$
\begin{aligned}
Y_{\mathbf{f}, m}^{(4)}=\frac{1}{L} \frac{1}{m !} \sum_{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m+1}}\left\{n_{\mathbf{f}_{1} \uparrow} n_{\mathbf{f}_{1}+\mathbf{f} \downarrow} D_{\mathbf{f}_{2}}, \ldots, D_{\mathbf{f}_{m+1}}\right\}_{0}^{\mathrm{FC}} & \\
& (32)
\end{aligned}
$$

The coefficients $c_{m}$ in (31b) determine the density of doubly occupied sites $d,(7 \mathrm{~b})$, i.e., the interacting part of the Hubbard Hamiltonian (1), by

$$
d=g^{2} \sum_{m=1}^{\infty}\left(g^{2}-1\right)^{m-1} c_{m}
$$

which enter in (31a) since $\hat{O}_{\mathbf{f}}^{(2)}$ is given by $\hat{D}$ and a contri

bution of a determinant as in (26) and (27) with f=0. In
one dimension they have already been determined as $^{29,30}$
$$
c_{m}=\frac{(-1)^{m+1}}{2} \frac{n^{m+1}}{m+1}, \quad n \leq 1\qquad(34)
$$
yielding
$$
d=\frac{1}{2} \frac{g^{2}}{1-g^{2}}\left(-\frac{1}{1-g^{2}} \ln \left[1-\left(1-g^{2}\right) n\right]-n\right). \quad(35)
$$

The other parts of the CF's, i.e., $\langle\hat{O}_{f}^{(3)}\rangle,\langle\hat{O}_{f}^{(4)}\rangle$ in (21c)
and (21d), may also be expressed in terms of $Y_{f, m}^{(2)}, Y_{f, m}^{(3)}$.

The expectation values of the $\hat{O}_{f}^{(l)}$ in (21) for
$l=1,2,3,4$ have now been expressed for arbitrary lattice
points f. Therefore they may be Fourier-transformed
$$
Y_{m}^{(l)}(\mathbf{q})=\frac{1}{L} \sum_{\mathbf{f}} e^{-i \mathbf{f q}} Y_{\mathbf{f}, m}^{(l)}, \quad l=1, \ldots, 4.\qquad(36)
$$

Altogether the momentum dependent CF's (13a)-(13d)
are found as
$$
C^{S S}(\mathbf{q})=2 \sum_{m=0}^{\infty}\left(g^{2}-1\right)^{m}\left(Y_{m}^{(1)}(\mathbf{q})-Y_{m}^{(4)}(\mathbf{q})-c_{m}\right),\qquad(37a)
$$

$$
\begin{aligned}
C^{N N}(\mathbf{q})=2\left\lceil\frac{n}{2}+Y_{0}^{(1)}(\mathbf{q})\right. & +Y_{0}^{(4)}(\mathbf{q}) \\
+\sum_{m=1}^{\infty}\left(g^{2}-1\right)^{m}[ & Y_{m}^{(1)}(\mathbf{q})+4 Y_{m}^{(2)}(\mathbf{q}) \\
& \left.\left.+2 Y_{m}^{(3)}(\mathbf{q})+Y_{m}^{(4)}(\mathbf{q})+c_{m}\right]\right],
\end{aligned}
$$

$$
C^{N D}(\mathbf{q})=\frac{2 g^{2}}{g^{2}-1} \sum_{m=1}^{\infty}\left(g^{2}-1\right)^{m}\left[Y_{m}^{(2)}(\mathbf{q})+Y_{m}^{(3)}(\mathbf{q})+c_{m}\right],\qquad(37c)
$$

$$
C^{D D}(\mathbf{q})=d+\left(\frac{g^{2}}{g^{2}-1}\right)^{2} \sum_{m=2}^{\infty}\left(g^{2}-1\right)^{m} Y_{m}^{(3)}(\mathbf{q}).\qquad(37d)
$$

The functions $Y_{m}^{(l)}(\mathbf{q})$, given by (30) and (32), may be
represented diagrammatically. The $m$ th-order diagrams
are constructed by drawing all topologically different, ful-
ly connected graphs with two external vertices and $m$
internal vertices in the case of $Y_{m}^{(1)}, Y_{m}^{(4)}, m-1$ internal
vertices for $Y_{m}^{(2)}$ and $m-2$ such vertices for $Y_{m}^{(3)}$. At
every internal vertex four fermion lines intersect. At the
external vertices a momentum $\mathbf{q}$ enters and leaves the
graph, respectively. At every vertex, momentum conser-
vation is obeyed. Every fermion line with momentum $\mathbf{k}$
is associated with a (step-) distribution function $n_{\mathbf{k}, \sigma}^{0}$ and
integration is performed over all internal moments. This
yields the "value" $v_{\mathbf{q}}(G_{m})$ of a graph $G_{m}$. Since every
graph of order $m$ may occur more than once, the value
$v_{\mathbf{q}}(G_{m})$ has to be multiplied by the "weight" $w(G_{m})$
which is defined as the number of times a graph appears
according to Wick's theorem, divided by $m$ ! in the case
of $Y_{m}^{(1)}, Y_{m}^{(4)}$, by $(m-1)$ ! for $Y_{m}^{(2)}$ and by $(m-2)$ ! for $Y_{m}^{(3)}$.
Lastly, the sign of a graph is given by $(-1)^{f(G_{m})}$, where
$f(G_{m})$ is the number of closed fermion loops in the graph
$G_{m}$. In this way the functions $Y_{m}^{(l)}(\mathbf{q})$ are calculated di-
agrammatically by
$$
Y_{m}^{(l)}(\mathbf{q})=\sum_{G_{m}^{l}}(-1)^{f\left(G_{m}^{l}\right)} w\left(G_{m}^{l}\right) v_{\mathbf{q}}\left(G_{m}^{l}\right),\qquad(38)
$$
where the sum extends over all topologically distinct
graphs $G_{m}^{l}$ contributing to the $m$ th order. The diagrams
to $Y_{m}^{(l)}(\mathbf{q})$ are shown in Figs. $2-5$ up to $m=3$. Since we
limit ourselves to $n_{\uparrow}=n_{\downarrow}$, the $\uparrow$ and $\downarrow$ lines do not have
to be distinguished.

In general there are three different classes of FC dia-
grams depending on whether an external vertex is con-
nected to two or to four lines (referred to as $\Gamma_{2}$ or $\Gamma_{4}$ ver-
tex, respectively), (i) those with two $\Gamma_{2}$ vertices as the
graphs in Figs. 2 and 5, (ii) those with one $\Gamma_{2}$ and one $\Gamma_{4}$
vertex (graphs in Fig. 3), and (iii) those with two $\Gamma_{4}$ ver-
tices (graphs in Fig. 4).

## V. POLYNOMIAL STRUCTURE OF CORRELATION FUNCTIONS IN ONE DIMENSION

In one dimension the shape of the Fermi "surface" is
density independent; this makes an evaluation of graphs
quite simple. It is easy to show that the graphs have the
following properties $(n \leq 1)$.

(1) They only depend on $|q|$, i.e., the magnitude of
the momentum $q$.

![](./images/811683925553315842_2.jpg)

FIG. 2. Diagrams to $Y_{m}^{(1)}(\mathbf{q})$, (30a), up to $m=3$.

![](./images/811683925553315842_3.jpg)

FIG. 3. Diagrams to $Y_{m}^{(2)}(\mathbf{q})$, (30b), up to $m=3$.

(2) A $\Gamma_{2}$ vertex limits momenta to $|q| \leq 2 k_{F}=\pi n$.

(3) A $\Gamma_{4}$ vertex limits momenta to $|q| \leq 4 k_{F}=2 \pi n$
(for $|q| \geq \pi$, i.e., $\frac{1}{2} \leq n \leq 1$, one should use an extended
zone scheme).

(4) Since the integration over the internal momenta of
an $m$ th-order graph is equivalent to the calculation of the
$$
Y_{m}^{(l)}(q)=\left\{\begin{array}{lll}
n^{m+1} \sum_{r=0}^{m+1} y_{m}^{(l)}(r)\left(\frac{|q|}{2 k_{F}}\right)^{r} ; & 0 \leq|q| \leq 2 k_{F}, \quad l=1,2,3,4 \\
0 ; & 2 k_{F} \leq|q| \leq 4 k_{F}, \quad l=1,2,4 \\
n^{m+1} \sum_{r=0}^{m+1} z_{m}(r)\left(2-\frac{|q|}{2 k_{F}}\right)^{r} ; & 2 k_{F} \leq|q| \leq 4 k_{F}, \quad l=3 \\
0 ; \quad 4 k_{F} \leq|q| \leq 2 \pi, & l=1,2,3,4.
\end{array}\right.
$$

The contributions for $L=1,2,4$ vanish for $|q| \geq 2 k_{F}$
since the corresponding graphs contain $\Gamma_{2}$ vertices, while
$Y_{m}^{(3)}(q)$ contains two $\Gamma_{4}$ vertices and thus contributes also
for $2 k_{F} \leq|q| \leq 4 k_{F}$. As can be seen from Fig. 4, for
some graphs the $\Gamma_{4}$ vertices degenerate to $\Gamma_{2}$ vertices due
to trivial loops. Therefore one gets two different polyno-
mials for $0 \leq|q| \leq 2 k_{F}$ and $2 k_{F} \leq|q| \leq 4 k_{F}$, respec-
tively. Hence, by merely considering the structure of the
graphs to $Y_{m}^{(l)}(q)$ we are able to conclude that these four
functions are determined by five sets of coefficients
$y_{m}^{(1)}(r), \ldots, y_{m}^{(4)}(r)$ and $z_{m}(r)$ as seen from (40).

(5) All graphs are continuous in $|q|$ and discontinui-
ties in the derivatives of $Y_{m}^{(l)}(q)$ with respect to $|q|$ may
only occur at $|q|=2 k_{F}$ or $4 k_{F}$.

(6) The first two derivatives of $v\left(G_{m}\right)$ with respect to $n$
are continuous, in particular at $n=1$.

The explicit results for the graphs contributing to $Y_{m}^{(l)}(q)$
up to $m=2$ in Figs. $2-5$ are listed in Tables I-IV, to-
gether with the respective results for $Y_{m}^{(l)}(q)$. The latter
![](./images/811683925553315842_4.jpg)

FIG. 4. Diagrams to $Y_{m}^{(3)}(\mathbf{q})$, (30c), up to $m=3$.

volume of a polyeder in the $(m+1)$-dimensional space of
momenta $k_{1}, \ldots, k_{m+1}$, the values of all graphs have the
structure $^{30}$
$$v_{q}\left(G_{m}\right) \propto n^{m+1} \mathcal{P}\left(\frac{|q|}{2 k_{F}}\right),\qquad(39)$$
where $\mathcal{P}(x)$ is a polynomial of degree $\leq m+1$. Hence
the $Y_{m}^{(l)}(q)$ in (36) may be expressed as

![](./images/811683925553315842_5.jpg)

FIG. 5. Diagrams to $Y_{m}^{(4)}(\mathbf{q})$, (32), up to $m=3$.

<table>
<caption>TABLE I. Results in one dimension for the graphs in Fig. 2 contributing to $Y_{m}^{(1)}(q)$ up to $m=2$. The labels (a), (b), etc. refer to the diagrams for $m=2$.</caption>
<thead>
  <tr>
    <th colspan="2">$G_{m} \in \{ Y_{m}^{(1)}(q) \}$</th>
    <th>$f(G_{m})$</th>
    <th>$w(G_{m})$</th>
    <th>$v(G_{m})$, $z=1-|q|/2k_{F}$</th>
    <th>$Y_{m}^{(1)}(q)$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="2">$m=0$</td>
    <td>1</td>
    <td>1</td>
    <td>$(n/2)z$</td>
    <td>$-\dfrac{n}{2}z$</td>
  </tr>
  <tr>
    <td colspan="2">$m=1$</td>
    <td>2</td>
    <td>2</td>
    <td>$(n/2)^{2}z$</td>
    <td>$\dfrac{n^{2}}{2}z$</td>
  </tr>
  <tr>
    <td>$m=2$</td>
    <td>(a)</td>
    <td>3</td>
    <td>3</td>
    <td>$(n/2)^{3}z$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>(b)</td>
    <td>3</td>
    <td>2</td>
    <td>$(n/2)^{3}z$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>(c)</td>
    <td>2</td>
    <td>2</td>
    <td>$(n/2)^{3}(\frac{1}{2}z+\frac{1}{2}z^{2}-\frac{1}{3}z^{3})$</td>
    <td>$-(n^{3}/4)z(z^{2}-z+2)$</td>
  </tr>
  <tr>
    <td></td>
    <td>(d)</td>
    <td>3</td>
    <td>1</td>
    <td>$(n/2)^{3}z^{3}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>(e)</td>
    <td>2</td>
    <td>1</td>
    <td>$(n/2)^{3}(z^{2}-\frac{1}{3}z^{3})$</td>
    <td></td>
  </tr>
</tbody>
</table>

<table>
<caption>TABLE II. Results in one dimension for the graphs in Fig. 3 contributing to $Y_{m}^{(2)}(q)$ up to $m=2$. The labels (a), (b), etc. refer to the diagrams for $m=2$.</caption>
<thead>
  <tr>
    <th colspan="2">$G_{m} \in \{ Y_{m}^{(2)}(q) \}$</th>
    <th>$f(G_{m})$</th>
    <th>$w(G_{m})$</th>
    <th>$v(G_{m})$, $z=1-|q|/2k_{F}$</th>
    <th>$Y_{m}^{(2)}(q)$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="2">$m=0$</td>
    <td></td>
    <td></td>
    <td></td>
    <td>0</td>
  </tr>
  <tr>
    <td colspan="2">$m=1$</td>
    <td>3</td>
    <td>1</td>
    <td>$(n/2)^{2}z$</td>
    <td>$-(n^{2}/4)z$</td>
  </tr>
  <tr>
    <td>$m=2$</td>
    <td>(a)</td>
    <td>4</td>
    <td>2</td>
    <td>$(n/2)^{3}z$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>(b)</td>
    <td>4</td>
    <td>1</td>
    <td>$(n/2)^{3}z$</td>
    <td>$(n^{3}/4)z(1+\frac{1}{3}z)$</td>
  </tr>
  <tr>
    <td></td>
    <td>(c)</td>
    <td>4</td>
    <td>1</td>
    <td>$(n/2)^{3}z^{2}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>(d)</td>
    <td>3</td>
    <td>2</td>
    <td>$(n/2)^{3}(\frac{1}{2}z+\frac{1}{2}z^{2}-\frac{1}{3}z^{3})$</td>
    <td></td>
  </tr>
</tbody>
</table>

<table>
<caption>TABLE III. Results in one dimension for the graphs in Fig. 4 contributing to $Y_{m}^{(3)}(q)$ up to $m=2$. The labels (a), (b), (c) refer to the diagrams for $m=2$.</caption>
<thead>
  <tr>
    <th colspan="3">$G_{m} \in \{ Y_{m}^{(3)}(q) \}$</th>
    <th colspan="2">$v(G_{m})$, $z=1-|q|/2k_{F}$</th>
    <th colspan="2">$Y_{m}^{(3)}(q)$</th>
  </tr>
  <tr>
    <th></th>
    <th>$f(G_{m})$</th>
    <th>$w(G_{m})$</th>
    <th>$0\leq|q|\leq2k_{F}$</th>
    <th>$2k_{F}\leq|q|\leq4k_{F}$</th>
    <th>$0\leq|q|\leq2k_{F}$</th>
    <th>$2k_{F}\leq|q|\leq4k_{F}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$m=0$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$m=1$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$m=2$ (a)</td>
    <td>3</td>
    <td>1</td>
    <td>$(n/2)^{3}z$</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>(b)</td>
    <td>3</td>
    <td>1</td>
    <td>$(n/2)^{3}z$</td>
    <td></td>
    <td>$(n^{3}/16)(\frac{1}{3}-3z+z^{2}-z^{3})$</td>
    <td>$(n/2)^{3}\frac{1}{6}(1+z)^{3}$</td>
  </tr>
  <tr>
    <td>(c)</td>
    <td>2</td>
    <td>1</td>
    <td>$(n/2)^{3}(\frac{1}{2}z+\frac{1}{2}z^{2}-\frac{1}{2}z^{3}+\frac{1}{6})$</td>
    <td>$(n/2)^{3}\frac{1}{6}(1+z)^{3}$</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

<table>
<caption>TABLE IV. Results in one dimension for the graphs in Fig. 5 contributing to $Y_{m}^{(4)}(q)$ up to $m=2$. The labels (a), (b), (c) refer to the diagrams for $m=2$.</caption>
<thead>
  <tr>
    <th colspan="2">$G_{m} \in \{ Y_{m}^{(4)}(q) \}$</th>
    <th>$f(G_{m})$</th>
    <th>$w(G_{m})$</th>
    <th>$v(G_{m})$, $z=1-|q|/2k_{F}$</th>
    <th>$Y_{m}^{(4)}(q)$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="2">$m=0$</td>
    <td></td>
    <td></td>
    <td></td>
    <td>0</td>
  </tr>
  <tr>
    <td colspan="2">$m=1$</td>
    <td>2</td>
    <td>1</td>
    <td>$(n/2)^{2}z^{2}$</td>
    <td>$\left\lfloor \dfrac{n}{2} \right\rfloor ^{2}z^{2}$</td>
  </tr>
  <tr>
    <td>$m=2$</td>
    <td>(a)</td>
    <td>3</td>
    <td>2</td>
    <td>$(n/2)^{3}z^{2}$</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>(b)</td>
    <td>3</td>
    <td>2</td>
    <td>$(n/2)^{3}z^{2}$</td>
    <td>$-(n^{3}/4)z^{2}(1+\frac{1}{3}z)$</td>
  </tr>
  <tr>
    <td></td>
    <td>(c)</td>
    <td>2</td>
    <td>2</td>
    <td>$(n/2)^{3}(z^{2}-\frac{1}{3}z^{3})$</td>
    <td></td>
  </tr>
</tbody>
</table>

are seen to be rather complicated polynomials without apparent building principle.

The above results imply that the CF's in (37) also have a polynomial structure
$$
C^{X Y}(q)=\sum_{m=0}^{\infty}\left(g^{2}-1\right)^{m} C_{m}^{X Y}(q)
\tag{41}
$$
given by the polynomials $Y_{m}^{(l)}(q)$ in (40). To determine the five sets of coefficients $y_{m}^{(1)}(r), \ldots, y_{m}^{(4)}(r), z_{m}(r)$ in (40) explicitly, we need five equations or conditions. These are provided by the five $p$-$h$ symmetry relations (13a)-(13d) and (17a).

## VI. SPIN CORRELATIONS

As seen from (37a) and (40), the graphs to $C_{m}^{S S}(q)$ in (41) only contribute for $|q| \leq 2 k_{F}$, such that
$$
C_{m}^{S S}(q)= \begin{cases}\sum_{r=0}^{m+1} a_{m}(r) n^{m+1-r}\left(\frac{|q|}{\pi}\right)^{r}, & 0 \leq|q| \leq 2 k_{F} \\ -2 c_{m}, & 2 k_{F} \leq|q| \leq \pi\end{cases}
\tag{42}
$$
where
$$
a_{m}(r)=2\left[y_{m}^{(1)}(r)-y_{m}^{(4)}(r)-\delta_{r, 0} \frac{(-1)^{m+1}}{2(m+1)}\right]. \tag{43}
$$

The symmetry relation (13a) then implies $a_{m}(r)(n^{m+1-r}-\bar{n}^{m+1-r})=0$ and hence
$$
a_{m}(r)=a_{m}(m+1) \delta_{r, m+1}. \tag{44}
$$

The continuity of $C^{S S}(q)$ at $|q|=\pi n$ links the coefficient $a_{m}(m+1)$ with the known coefficient $c_{m},(34)$, and yields
$$
a_{m}(m+1)=\frac{(-1)^{m}}{m+1}. \tag{45}
$$

$C^{S S}(q)$ is then explicitly obtained by inserting (44) and (45) into (42) and summing the series in (41). Introducing the function
$$
F(x) \equiv 1-\left(1-g^{2}\right) x, \tag{46}
$$
$C^{S S}(q)$ is found as
$$
C^{S S}(q)= \begin{cases}-\frac{1}{1-g^{2}} \ln F\left(\frac{|q|}{\pi}\right), & 0 \leq|q| \leq 2 k_{F} \\ -\frac{1}{1-g^{2}} \ln F(n), & 2 k_{F} \leq|q| \leq \pi\end{cases}
\tag{47}
$$
which is valid for arbitrary momentum $q$, density $n \leq 1$, and correlation parameter $g$. Note that for $|q| \leq 2 k_{F}$, $C^{S S}(q)$ is a universal function of $|q|$, i.e., is density in dependent. Using (35) we see that
$$
C^{S S}\left(2 k_{F} \leq|q| \leq \pi\right)=n+\frac{2\left(1-g^{2}\right)}{g^{2}} d \tag{48}
$$
is $q$ independent. In real space, the spin CF is then given by
$$
\begin{aligned}
C_{j}^{S S}=-\frac{p}{(\pi j)^{2}}\{ & \sin (\pi j) \ln F(n) \\
& +\sin p[\operatorname{Ci}(p)-\operatorname{Ci}(p F(n))] \\
& +\cos p[\operatorname{Si}(p F(n))-\operatorname{Si}(p)]\},
\end{aligned}
\tag{49}
$$
where $p=\pi j /\left(1-g^{2}\right)$. Here Ci and Si are the cosine and sine integrals, respectively. Since we consider a discrete lattice, only integer $j$ is allowed; in this case the first term on the rhs of (49) drops out for $j>0$. In particular, for half-filling $(n=1)$ a simple expression is found
$$
\left.C_{j}^{S S}\right|_{n=1}=-\frac{1}{\pi j} \int_{0}^{1} d y \frac{\sin (\pi j y)}{F(y)}, \quad j>0. \tag{50}
$$

The resulting spin CF in $q$ space is shown in Fig. 6 for different particle densities $n$ and correlation parameters $g$. The main feature is that for increasing repulsive interaction the spin correlations strongly increase. The numerical result of Yokoyama and Shiba $^{28}$ are seen to be excellent. In particular, in the atomic limit $(g=0)$
$$
C^{S S}(q ; g=0, n)= \begin{cases}-\ln \left(1-\frac{|q|}{\pi}\right), & 0 \leq|q| \leq 2 k_{F} \\ -\ln (1-n), & 2 k_{F} \leq|q| \leq \pi.\end{cases}
\tag{51}
$$

At $|q|=2 k_{F}$ and $n \leq 1 C^{S S}$ always has a kink as in the noninteracting case but does not diverge; this is in contrast to numerical findings of Hirsch and Scalapino. $^{10}$ In particular, for $n=1$ the spin CF has a logarithmic divergence at $|q|=2 k_{F}$ and in real space is given by
$$
C_{j \geq 1}^{S S}(g=0, n=1)=(-1)^{j} \frac{\operatorname{Si}(\pi j)}{\pi j}. \tag{52}
$$

The numerical results for $j=1$ (Refs. 21 and 27) and $j=2$ (Ref. 22) agree very well with this approximationfree result. The logarithmic divergence at $|q|=2 k_{F}$ implies an antiferromagnetic correlation of the spins in the ground state. The $(-1)^{j} / j$ separation dependence for $j \rightarrow \infty$ (suggested by Horsch and Kaplan $^{22}$ ) reproduces the result for the antiferromagnetic Heisenberg chain $^{34}$ (AFHC); the AFHC is known to describe the Hubbard model in the atomic limit. $^{35}$

In Fig. $7\left|C_{j}^{S S}(g, n=1)\right|$ is shown for different $g$. For $0<g<1$ and for $j \lesssim 1 / d$, with $d$ the number of doubly occupied sites, it decreases as $1 / j$. On the other hand, for $j \gtrsim 1 / d$, it decreases as $1 / j^{2}$ as in the noninteracting case:
$$
C_{j}^{S S}(g \rightarrow 0) \simeq \begin{cases}\frac{(-1)^{j}}{\pi j} \operatorname{Si}(\pi j)+2 d, & \\ & \pi j \ll \frac{1}{g^{2}} \text { and } \pi j \gg 1 \\ \frac{1}{(\pi j)^{2}}\left(\frac{(-1)^{j}}{g^{2}}-1\right), & \\ & \pi j \gg \frac{1}{g^{2}} \text { and } \pi j \gg 1.\end{cases}
\tag{53}
$$

The existence of a "correlation length" proportional to $1 / d$ is typical for the present variational ansatz which

![](./images/811683925553315842_6.jpg)

![](./images/811683925553315842_7.jpg)

FIG. 6. Momentum dependence of the spin- and density-correlation functions $C^{SS}(q)$ and $C^{NN}(q)$ in one dimension for different correlation parameters $g$ and different densities $n$. (a) $n=0.7$; (b) $n=1.0$. For $g=1$ (noninteracting case) the two functions coincide.

![](./images/811683925553315842_8.jpg)

FIG. 7. Magnitude of the spin-correlation function $|C_{j}^{SS}|$ as a function of separation $j$ for $n=1$ and different correlation parameters $g$.

only controls the wave function $|\Psi_{0}\rangle$ globally in terms of $d$.

It is interesting to compare our analytic result for $C_{j}^{SS}(g=0, n=1)$ in (52), obtained from the GWF, with exact analytic $^{6,7}$ and numerical $^{36,37}$ (Monte Carlo) results for the AFHC (see Table V). Evidently the GWF describes spin correlations in one dimension very well indeed, as observed earlier on the basis of numerical results. $^{21,22}$ (It should be noted, however, that numerical approaches necessarily have to make use of an explicit extrapolation scheme to conclude about the $j \to \infty$ behavior, which may lead to discrepancies among each other. $^{38}$ ) Most recently Haldane $^{39}$ and, independently, Shastry $^{40}$ have shown that the GWF for $g=0, n=1$ is indeed the exact ground-state wave function of a spin-$\frac{1}{2}$ Heisenberg chain with antiferromagnetic, isotropic coupling, which decreases with the inverse square of the spin separation. This clarifies the rather surprising finding, that the GWF yields "physical", i.e., antiferromagnetic, correlations, in a limit where its applicability is far from clear.

### VII. SUPERCONDUCTING CORRELATIONS

Superconducting correlations between local Cooper pairs are described by (6). A treatment formally identical to the one described in Sec. IV allows one to rewrite (6) in terms of contractions
$$
\begin{aligned}
C_{\mathfrak{f}.}^{\text {sup }}= & (n-1+d) \delta_{\mathfrak{f}, 0} \\
& -\left(1-\delta_{\mathfrak{f}, 0}\right) g^{2} \sum_{m=0}^{\infty}\left(g^{2}-1\right)^{m} C_{\mathfrak{f}, m}^{\text {sup }},
\end{aligned}\qquad(54a)
$$
where

TABLE V. Comparison of the spin-correlation function $C_{j}^{S S}$ in the atomic limit ($g=0$) for $n=1$ obtained from the Gutzwiller wave function (GWF), (52), with the exact and numerical results for the antiferromagnetic Heisenberg chain (AFHC). Uncertainties of numerical results in the last digit are indicated in parentheses.

<table>
<thead>
<tr>
<th>$j$</th>
<th>$C_{j}^{SS}|_{GWF,\ g=0}$<br>Eq. (52)</th>
<th>Exact</th>
<th>$C_{j}^{SS}|_{AFHC}$<br>Numerical (Ref. 36)</th>
<th>Numerical (Ref. 37)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>$-0.589490$</td>
<td>$-0.590863^{a}$</td>
<td>$-0.59084(1)$</td>
<td>$-0.5908(2)$</td>
</tr>
<tr>
<td>2</td>
<td>$0.225706$</td>
<td>$0.242719^{b}$</td>
<td>$0.24260(2)$</td>
<td>$0.24265(20)$</td>
</tr>
<tr>
<td>3</td>
<td>$-0.177698$</td>
<td></td>
<td>$-0.20047(8)$</td>
<td>$-0.2009(1)$</td>
</tr>
<tr>
<td>4</td>
<td>$0.118742$</td>
<td></td>
<td>$0.13798(8)$</td>
<td>$0.1386(3)$</td>
</tr>
<tr>
<td>5</td>
<td>$-0.104021$</td>
<td></td>
<td>$-0.1211(4)$</td>
<td>$-0.1235(3)$</td>
</tr>
<tr>
<td>6</td>
<td>$0.080534$</td>
<td></td>
<td>$0.0943(6)$</td>
<td>$0.0982(4)$</td>
</tr>
<tr>
<td>7</td>
<td>$-0.073488$</td>
<td></td>
<td>$-0.082(1)$</td>
<td>$-0.0899(6)$</td>
</tr>
<tr>
<td>8</td>
<td>$0.060922$</td>
<td></td>
<td>$0.069(1)$</td>
<td>$0.0760(6)$</td>
</tr>
</tbody>
</table>

$^{a}$Reference 6.
$^{b}$Reference 7.

$$
C_{\mathfrak{f}, m}^{\text {sup }}=\frac{1}{m!} \frac{1}{L} \sum_{\mathfrak{f}_{1}, \ldots, \mathfrak{f}_{m+1}}\left\{c_{\mathfrak{f}_{1}+\mathfrak{f} \uparrow}^{\dagger} c_{\mathfrak{f}_{1} \uparrow} c_{\mathfrak{f}_{1}+\mathfrak{f} \downarrow}^{\dagger} c_{\mathfrak{f}_{1} \downarrow} D_{\mathfrak{f}_{2}}, \ldots, D_{\mathfrak{f}_{m+1}}\right\}_{0}^{c}.\qquad(54b)
$$

Because of the $\delta$-less contractions and inversion symmetry, (54b) can be written as

$$
C_{\mathfrak{f}, m}^{\text {sup }}=\frac{1}{m!} \frac{1}{L} \sum_{\mathfrak{f}_{1}, \ldots, \mathfrak{f}_{m+1}}\left\{c_{\mathfrak{f}_{1} \uparrow}^{\dagger} c_{\mathfrak{f}_{1}+\mathfrak{f} \uparrow} c_{\mathfrak{f}_{1}+\mathfrak{f} \downarrow}^{\dagger} c_{\mathfrak{f}_{1} \downarrow} D_{\mathfrak{f}_{2}}, \ldots, D_{\mathfrak{f}_{m+1}}\right\}_{0}^{c}.\qquad(55)
$$

Using the transformation (18a) and (18b) yields

$$
C_{\mathfrak{f}, m}^{\text {sup }}=-\frac{1}{2} \frac{1}{m!} \frac{1}{L} \sum_{\mathfrak{f}_{1}, \ldots, \mathfrak{f}_{m+1}}\left\{\left(n_{\mathfrak{f}_{1} \alpha}-n_{\mathfrak{f}_{1} \beta}\right)\left(n_{\mathfrak{f}_{1}+\mathfrak{f} \alpha}-n_{\mathfrak{f}_{1}+\mathfrak{f} \beta}\right) D_{\mathfrak{f}_{2}}, \ldots, D_{\mathfrak{f}_{m+1}}\right\}_{0}^{c}.\qquad(56)
$$

This expression is familiar from the spin-correlation func- tion and hence (54a) yields

$$
C_{\mathfrak{f}}^{\text {sup }}=\delta_{\mathfrak{f}, 0}\left(n-1-\left(1-g^{2}\right) d-\frac{n g^{2}}{2}\right)+\frac{g^{2}}{2} C_{\mathfrak{f}}^{S S}.\qquad(57)
$$

Equation (57) is valid for arbitrary lattices with inversion symmetry. Hence, the superconducting correlations are suppressed for increasing repulsion by the additional fac- tor $g^{2}$ for all $n \leq 1$ and vanish altogether for $g \to 0$ (see also Ref. 41) as should be expected. For $0<g<1 C_{j}^{sup }$ decays algebraically as discussed in (53).

## VIII. DENSITY CORRELATIONS

The evaluation of $C^{NN}(q)$ in one dimension is more complicated than that of $C^{SS}(q)$ since it involves $Y_{m}^{(3)}$, which also contributes for $2 k_{F} \leq|q| \leq 4 k_{F}$ [see (40)]. While for $n \leq \frac{1}{2}$ one has $4 k_{F} \leq \pi$, such that momenta always lie in the first Brillouin zone, this is no longer true for $n \geq \frac{1}{2}$, where momenta $\pi \leq|q| \leq 4 k_{F}$ occur which have to be folded back into the first Brillouin zone ("Umklapp process", $|q| \to 2 \pi-|q|$ ). For $n \geq \frac{1}{2}$ there are then three nontrivial momentum regimes. For $\frac{2}{3} \leq n \leq 1$ they are given by (i) $0 \leq|q| \leq 2 \pi-4 k_{F}$, (ii) $2 \pi-4 k_{F}$ $\leq|q| \leq 2 k_{F}$, and (iii) $2 k_{F} \leq|q| \leq \pi$; for $\frac{1}{2} \leq n \leq \frac{2}{3}$ the boundaries $2 \pi-4 k_{F}$ and $2 k_{F}$ simply have to be interchanged. In the following we explicitly consider $\frac{2}{3} \leq n \leq 1$.

According to (37b), (40), and (41) the $m$th order of $C^{NN}(q)$ is given by $(m \geq 1)$

$$
C_{m}^{N N}(q)= \begin{cases}4 n^{m+1} \sum_{r=0}^{m+1} d_{m}(r)\left(\frac{|q|}{2 k_{F}}\right)^{r}, & 0 \leq|q| \leq 2 \pi-4 k_{F} \\ 4 n^{m+1} \sum_{r=0}^{m+1}\left[d_{m}(r)\left(\frac{|q|}{2 k_{F}}\right)^{r}+z_{m}(r)\left(2-\frac{2 \pi-|q|}{2 k_{F}}\right)^{r}\right], & 2 \pi-4 k_{F} \leq|q| \leq 2 k_{F} \\ 4 n^{m+1} \sum_{r=0}^{m+1}\left[\left(2-\frac{|q|}{2 k_{F}}\right)^{r}+\left(2-\frac{2 \pi-|q|}{2 k_{F}}\right)^{r}\right] z_{m}(r)+2 c_{m}, & 2 k_{F} \leq|q| \leq \pi\end{cases}
\qquad(58)
$$


where
$$
\begin{aligned}
d_{m}(r)=\frac{1}{2} & \left\lfloor y_{m}^{(1)}(r)+4 y_{m}^{(2)}(r)+2 y_{m}^{(3)}(r)\right. \\
& \left.+y_{m}^{(4)}(r)+\delta_{r, 0} \frac{(-1)^{m+1}}{2(m+1)}\right]
\end{aligned}
\tag{59}
$$
[note that $C_{0}^{N N}(q)=C_{0}^{S S}(q)$]. The two sets of unknown coefficients $d_{m}(r)$ and $z_{m}(r)$ may be determined by employing the symmetry relations (13b) and (17a) and restricting oneself to $n=1$. Using (47), (17a) yields $(m \geq 1)$
$$
\begin{aligned}
C_{m}^{N N}(q ; m=1)= & \sum_{l=0}^{1} \frac{(-1)^{m+1-l}}{m+1-l} \\
& \times\left\lceil\left(1-\frac{|q|}{\pi}\right)^{m+1-l}-1\right\rceil.
\end{aligned}
\tag{60}
$$

Comparison with (58) leads to a relation between $d_{m}(r)$ and $z_{m}(r)$
$$
d_{m}(r)+z_{m}(r)= \begin{cases}0, \quad r=0,1 \\
\frac{1}{4 r}\left\lfloor\begin{array}{l}
m-1 \\
r-2
\end{array}\right\rfloor(-1)^{m+1-r}, & 2 \leq r \leq m+1\end{cases}
\tag{61}
$$
and the continuity at $|q|=2 \pi n$ implies $z_{m}(0)=0$ and hence $d_{m}(0)=0$. A second relation is obtained by observing that the first two derivatives of (13b) with respect to $n$ are continuous at $n=1$. Hence
$$
\frac{\partial}{\partial n}\left[C^{N N}(q)\right]_{n=1}=0.
\tag{62}
$$

This leads to the relation
$$
\begin{aligned}
(m+1-r)\left[d_{m}(r)+z_{m}(r)\right]+2(r+1) z_{m}(r+1) & =0, \\
0 & \leq r \leq m
\end{aligned}
\tag{63}
$$
which, together with (61), yields the coefficients as
$$
d_{m}(r)= \begin{cases}0, \quad r=0,1 \\
(-1)^{m+1-r} \frac{1}{8 m}\left\lfloor\begin{array}{c}
m \\
r-1
\end{array}\right\rfloor, & 2 \leq r \leq m+1\end{cases}
\tag{64a}
$$
$$
z_{m}(r)=\frac{r-2}{r} d_{m}(r).
\tag{64b}
$$

This determines the density CF completely. Inserting (64) into (58) and performing the sums over $r$ and $m$, yields for $\frac{2}{3} \leq n \leq 1$ (here $Q \equiv|q| / \pi$)
$$
C^{N N}(q)= \begin{cases}Q\left\lfloor 1-\frac{1}{2} \ln \frac{F(n-Q)}{F(n)}\right\rfloor, & 0 \leq|q| \leq 2 \pi(1-n) \\
2(1-n)+\frac{Q}{2} \ln \frac{F(\bar{n}-Q)}{F(n-Q)}+\frac{g^{2}}{1-g^{2}} \ln \frac{F(\bar{n}-Q)}{F(n)}, & 2 \pi(1-n) \leq|q| \leq \pi n \\
2(1-n)+\frac{Q}{2} \ln \frac{F(\bar{n}-Q)}{F(Q-n)}+\frac{g^{2}}{1-g^{2}} \ln \frac{F(\bar{n}-Q)}{F(n)}+\frac{1}{1-g^{2}} \ln F(Q-n), & n \pi \leq|q| \leq \pi.\end{cases}
\tag{65}
$$

In particular, for $n=1$, (65) reduces to
$$
C^{N N}(q ; g, n=1)=\frac{g^{2}}{1-g^{2}} \ln F\left\lfloor-\frac{Q}{g^{2}}\right\rfloor,
\tag{66}
$$
as implied by (17a) and (47). In real space (66) reads as
$$
\begin{aligned}
C_{j}^{N N}=-\frac{\bar{p}}{(\pi j)^{2}} & \left\{\sin (\pi j) \ln g^{2}+\sin \bar{p}[\operatorname{Ci}(\bar{p})-\operatorname{Ci}(p)]\right. \\
& \left.+\cos \bar{p}[\operatorname{Si}(p)-\operatorname{Si}(\bar{p})]\right\},
\end{aligned}
\tag{67}
$$
where $\bar{p}=g^{2} p=\pi j g^{2} /\left(1-g^{2}\right)$.

The $q$ dependence of $C^{N N}(q)$ is shown in Figs. 6(a) and 6(b) for $n=0.7$ and $n=1$ in comparison with that of $C^{S S}(q)$. At $|q|=2 \pi(1-n)$ and $|q|=\pi n$, i.e., at the boundaries of the three momentum regimes for $n \leq 1$, the third and first derivatives with respect to $q$, respectively, are discontinuous. For $\pi n \leq|q| \leq \pi$, the curve has a downward curvature, i.e., is not constant as in the case of $C^{S S}(q)$, owing to the Umklapp processes. The numerical results of Yokoyama and Shiba $^{28}$ are seen to be in excellent agreement with (65). For $n=1 C^{N N}(q)$ vanishes in the atomic limit $g \rightarrow 0$, as should be expected. This is also apparent from Fig. 8, where the real-space behavior is plotted for $n=1$. The correlations suppress density fluctuations and smooth out the spatial distribution of the particles. As in the case of $C_{j}^{S S}$, the density CF decays algebraically and is proportional to $1 / j$ for distances $j \lesssim 1 / d$ and to $1 / j^{2}$ for $j \gtrsim 1 / d$.

Although there exist no exact results for $C_{j}^{N N}$ for the Hubbard-model that would allow us to compare our result with, we may test (65) in the atomic limit. As pointed out by Gros, Joynt, and Rice $^{27}$ the hole-hole CF, (8b), is related to the density CF in this limit by
$$
C^{H H}(q ; g=0, n)=C^{N N}(q ; g=0, n),
\tag{68}
$$
since there are no doubly occupied sites. For $n<1$ the holes then act as free spinless fermions whose exact CF is of course known, and is given by (65) with $g=1$ and the replacement $n \rightarrow n_{h}=1-n, k_{F} \rightarrow k_{F}^{h}=\pi n_{h}$, i.e.,


![](./images/811683925553315842_9.jpg)

FIG. 8. Density correlation function $C_{j}^{NN}$ as a function of separation $j$ for $n=1$ and different correlation parameters $g$.

$$
C_{\text{exact}}^{HH}(q;g=0,n_{h})=\left\{
\begin{array}{l}
\frac{|q|}{2\pi}\ ,\ 0\leq|q|\leq2k_{F}^{h} \\
\\
n_{h}\ ,\ 2k_{F}^{h}\leq|q|\leq\pi\ .
\end{array}
\right. \tag{69}
$$

A comparison of (69) with $C^{NN}(q;g=0,1-n_{h})$ as given by (65) is shown in Fig. 9. The agreement is remarkable and becomes increasingly better for $n_{h}\to0$. Although there is no sharp kink at $|q|=2k_{F}$ (since the GWF is based on free fermions, not holes) the overall feature is very well borne out. There is, however, a kink at $|q|=2k_{F}$ reflecting the Fermi momentum of the free Fermi gas. $^{27}$

### IX. CORRELATIONS INVOLVING DOUBLY OCCUPIED SITES

The remaining two CF's, i.e., $C^{ND}(q)$ and $C^{DD}(q)$ defined in (37c) and (37d), also involve $Y_{m}^{(3)}(q)$ and hence also contribute for $2k_{F}\leq|q|\leq4k_{F}$. Therefore they have the same analytic structure as $C^{NN}(q)$, i.e., the $m$th-order expressions $C_{m}^{ND}(q)$ and $C_{m}^{DD}(q)$ have the same form as (58).

![](./images/811683925553315842_10.jpg)

FIG. 9. Momentum dependence of the hole-correlation function $C^{HH}(q)$ in the atomic limit ($g=0$) as compared with the exact result for different hole concentrations $n_{h}$.

As seen from (37c), $C^{ND}(q)$ is given by (58) multiplied by an overall factor $g^{2}/2(g^{2}-1)$ and $d_{m}(r)$ replaced by a new set of coefficients $l_{m}(r)\equiv y_{m}^{(2)}(r)+y_{m}^{(3)}(r)$. To determine $l_{m}(r)$ we employ the symmetry relation (13d) at $n=1$
$$
C^{ND}(q;g,n=1)=\frac{1}{2}C^{NN}(q;g,n=1)\ . \tag{70}
$$

Employing (66) yields the explicit $C_{m}^{ND}(q)$ for $m\geq1$ as
$$
C_{m}^{ND}(q;n=1)=\frac{g^{2}}{2(g^{2}-1)}\frac{(-1)^{m}}{m}\left[(1-Q)^{m}-1\right] , \tag{71}
$$
where $Q=|q|/\pi$. Comparing with the general form in terms of $l_{m}(r)+z_{m}(r)$ and using (64b) leads to
$$
\sum_{r=0}^{m+1}l_{m}(r)|y|^{r}=\frac{(-1)^{m}}{2m}|y|\left[(1-|y|)^{m}-1\right]-\frac{(-1)^{m+1}}{m+1}\left[(1-|y|)^{m+1}-1\right] \tag{72}
$$
for general $n$ with $y=q/2k_{F}$. Summation on $m$ then yields the full result for $C^{ND}(q)$. For $\frac{2}{3}\leq n\leq1$,
$$
C^{ND}(q)=-\frac{g^{2}}{2(1-g^{2})}\tilde{C}^{ND}(q) \tag{73a}
$$
with

$$
\tilde{C}^{N D}(q)= \begin{cases}
Q\left[1-\frac{1}{2} \ln \frac{F(n-Q)}{F(n)}\right]-\frac{1}{1-g^{2}} \ln \frac{F(n-Q)}{F(n)}, & 0 \leq|q| \leq 2 \pi(1-n) \\
2(1-n)+\left(\frac{Q}{2}+\frac{1}{1-g^{2}}\right) \ln \frac{F(\bar{n}-Q)}{F(n-Q)}-\ln \frac{F(\bar{n}-Q)}{F(n)}, & 2 \pi(1-n) \leq|q| \leq \pi n \\
2(1-n)+\frac{Q}{2} \ln \frac{F(\bar{n}-Q)}{F(Q-n)}+\frac{g^{2}}{1-g^{2}} \ln \frac{F(\bar{n}-Q)}{F(n)}+\frac{1}{1-g^{2}} \ln F(Q-n), & n \pi \leq|q| \leq \pi.
\end{cases}
\tag{73b}
$$

Lastly, we calculate the CF between doubly occupied sites. As seen from (37a), $C_{m}^{D D}(q)-d$ is given by (58) multiplied by an overall factor $\left[g^{2} / 2\left(1-g^{2}\right)\right]^{2}$, with $d_{m}(r)$ replaced by a new set of coefficients $e_{m}(r) \equiv y_{m}^{(3)}(r)$ and without the $c_{m}$ in the third momentum regime. To determine $e_{m}(r)$ we employ the continuity of the first derivative of the symmetry relation (13d) with respect to $n$ at $n=1$, i.e.,
$$
\left.\frac{\partial}{\partial n} C^{D D}(q)\right|_{n=1}=\left.\frac{\partial}{\partial n} C^{N D}(q)\right|_{n=1}.
\tag{74}
$$

The rhs of (74) may be explicitly determined from the second momentum regime of (73) such that
$$
\left.\frac{\partial}{\partial n}\left[E_{m}(q, n)+Z_{m}(2 \pi-|q|, n)\right]\right|_{n=1}=2(-1)^{m} \frac{1-Q}{Q}\left[(1-Q)^{m-1}-1\right]
\tag{75}
$$
with [see (58)]
$$
E_{m}(q, n)=4 n^{m+1} \sum_{r=0}^{m+1} e_{m}(r)|y|^{r},
\tag{76a}
$$
$$
\begin{aligned}
Z_{m}(q, n) & =4 n^{m+1} \sum_{r=0}^{m+1} z_{m}(r)(2-y)^{r} \\
& =n^{m+1}\left(\sum_{l=0}^{1} \frac{1}{m+1-l}\left[(1-y)^{m+1-l}-(-1)^{m+1-l}\right]-\frac{2-y}{2 m}\left[(1-y)^{m}-(-1)^{m}\right]\right),
\end{aligned}
\tag{76b,76c}
$$
and $m \geq 1$. Equation (76a) has the property
$$
\left.\frac{\partial E_{m}(q, n)}{\partial n}\right|_{n=1}=(m+1) E_{m}(q, 1)-Q \frac{\partial E_{m}(q, 1)}{\partial Q}
\tag{77}
$$
which allows us to rewrite (75) as a first-order differential equation for $E_{m}(q, 1)$ in $q$, with the integration constant determined by the continuity of $C_{m}^{D D}$ at $|q|=n \pi$, i.e., $E_{m}(\pi, 1)=[1 /(m+1)-1 / 2 m](-1)^{m}$. This yields $E_{m}(q, n)$ for general $n$:
$$
\begin{aligned}
E_{m}(q, n)=4(-n)^{m+1} & \left(\frac{|y|}{2 m} T_{m}(|y|)-\frac{4}{m+1}-\frac{m}{(m+1)(m+2)}|y|^{m+1}\right. \\
& \left.+\frac{2}{m+1} T_{m+1}(|y|)+\frac{2}{m+2} \frac{1}{|y|} T_{m+2}(|y|)\right)
\end{aligned}
\tag{78}
$$
where $T_{m}(x)=1-(1-x)^{m}$. Summation on $m$ results in the complete expression for $C^{D D}(q)$. For $\frac{2}{3} \leq n \leq 1$
$$
C^{D D}(q)=d+\left(\frac{g^{2}}{2\left(1-g^{2}\right)}\right)^{2} \tilde{C}^{D D}(q)
\tag{79a}
$$
with

$$
\tilde{C}^{D D}(q)=\left\{\begin{aligned}
-2 n+Q\left(1-\frac{1}{2} \ln \frac{F(n-Q)}{F(n)}\right)-\frac{1}{1-g^{2}} \ln \frac{F^{2}(n-Q) F^{2}(n)}{F(Q)}-\frac{2}{\left(1-g^{2}\right)^{2} Q} \ln \frac{F(Q) F(n-Q)}{F(n)}, & \\
& 0 \leq|q| \leq 2 \pi(1-n) \\
2(1-2 n)-\ln \frac{F(\bar{n}-Q)}{F(n)}-\frac{1}{1-g^{2}} \ln \frac{F^{2}(n-Q) F^{3}(n)}{F(\bar{n}-Q) F(Q)}+\frac{Q}{2} \ln \frac{F(\bar{n}-Q)}{F(n-Q)}-\frac{2}{\left(1-g^{2}\right)^{2} Q} \ln \frac{F(Q) F(n-Q)}{F(n)}, & \\
& 2 \pi(1-n) \leq|q| \leq \pi n \\
2(1-2 n)+\frac{1}{1-g^{2}} \ln \frac{F(\bar{n}-Q) F(Q-n)}{F^{2}(n)}-\ln \frac{F(\bar{n}-Q)}{F(n)}+\frac{Q}{2} \ln \frac{F(\bar{n}-Q)}{F(Q-n)}, & n \pi \leq|q| \leq \pi .
\end{aligned}\right.
\tag{79b}
$$

We have thereby calculated all four independent correlation functions $C^{S S}, C^{N N}, C^{N D}$, and $C^{D D}$ in terms of GWF for arbitrary momenta $q$, densities $n$, and correlation strengths $g$ in one dimension. Other CF's may be composed of these four functions, e.g., $C^{D H}$ and $C^{H H}$ are given by (8). In particular,
$$
\begin{aligned}
C^{H H}(q, n=1) & =C^{D D}(q, n=1) \\
& =\frac{2 d\left(1-g^{4}\right)+g^{4}}{\left(1-g^{2}\right)^{2}}+\frac{g^{4}}{4\left(1-g^{2}\right)^{3}}\left\{\ln F(q)-\left(2-g^{2}\right) \ln F\left(-\frac{Q}{g^{2}}\right)-\frac{2}{\left(1-g^{2}\right) Q}\left[\ln F(Q)+\ln F\left(-\frac{Q}{g^{2}}\right)\right]\right\},
\end{aligned}
\tag{80a}
$$
$$
C^{D H}(q, n=1)=C^{H H}(q, n=1)-\frac{g^{2}}{2\left(1-g^{2}\right)} \ln F\left(-\frac{Q}{g^{2}}\right).
\tag{80b}
$$

We note that $C^{D D}(q=0)$ and $C^{H H}(q=0)$ do not vanish while $C^{S S}(q=0)=C^{N N}(q=0)=0$. This is clear since $C^{X X}(q=0)=\left\langle\hat{X}^{2}\right\rangle-\langle\hat{X}\rangle^{2}$ is a measure of the fluctuations of $\langle\hat{X}\rangle$ around the average. In contrast to the total spin $\left\langle\hat{S}^{z}\right\rangle$ and the particle number $\langle\hat{N}\rangle$, the total number of holes $\langle\hat{H}\rangle$ or doubly occupied sites $\langle\hat{D}\rangle$ is not conserved.

![](./images/811683925553315842_11.jpg)
FIG. 10. Probability for finding an empty site at separation $j$ from a doubly occupied site, normalized to the noninteracting case, for $n=1$ and different correlation parameters $g$.

Of particular interest is the CF between doubly occupied and empty sites, $C^{D H}(q)$, which is already a rather subtle correlation. In Fig. 10 we have plotted the probability for finding an empty site at separation $j$ from a doubly occupied site, $P_{j}^{D H}(g)=(C_{j}^{D H}+d^{2}) / d$, normalized to its noninteracting value, i.e.,
$$
\bar{C}_{j}^{D H}=P_{j}^{D H}(g) / P_{j}^{D H}(g=1).
$$

For increasing correlation this probability strongly decreases as can be inferred from $C_{j}^{D H} \simeq-\frac{1}{2} C_{j}^{N N}$ for $g \to 0$. On the other hand, one should expect this probability to increase, $^{21}$ since this would allow for an easy dissociation of a doubly occupied site which carries a large energy $U$. The missing correlation originates in the ansatz of GWF itself, which controls only the number of doubly occupied sites and holes but not their mutual correlation. As first noted by Kaplan, Horsch, and Fulde $^{21}$ this improvement in the variational wave function which takes this particular correlation into account improves the ground-state energy $E$ of the Hubbard model for large $U$ substantially. It may therefore be possible that this missing correlation in the GWF is specifically responsible for the logarithmic correction to the $(-t^{2}/U)$ term in $E$ found by Metzner and Vollhardt $^{29,30}$ in their exact diagonalization of the Hubbard model with the GWF.

## X. EXTENDED HUBBARD MODELS

Generalizations of the Hubbard model containing more refined interaction terms than $\hat{H}$ in (1), e.g.,

$$
\hat{H}_{\mathrm{ext}}=\hat{H}+\sum_{i, j} \sum_{\sigma, \sigma^{\prime}} V_{i j}^{\sigma \sigma^{\prime}} \hat{n}_{i \sigma} \hat{n}_{i+j \sigma^{\prime}},
\tag{81}
$$

may easily be constructed. For the expectation value $\langle\hat{H}_{\text {ext }}\rangle$, the additional term in (81) can be completely expressed by the correlation functions $C_{j}^{S S}$ and $C_{j}^{N N}$. The simplest extention corresponds to $V_{i j}^{\sigma \sigma^{\prime}}=V$ for nearestneighbor sites and zero otherwise, i.e.,

$$
\left\langle\hat{H}_{\mathrm{ext}}\right\rangle=\langle\hat{H}\rangle+2 V\left(C_{j=1}^{N N}+n^{2}\right).
\tag{82}
$$

Exact solutions of (81) and (82) do not exist. However, since we have determined all CF's in one dimension for the GWF we are now able to diagonalize $\hat{H}_{\text {ext }}$ analytically for arbitrary densities and correlation strengths, too. This yields an exact, analytic upper bound for any extended Hubbard model of the form as in (81). For the evaluation we have to make use of the expectation value of the kinetic energy of $\hat{H}$ calculated in Refs. 29 and 30 . The result of the minimization of $\langle\hat{H}_{\text {ext }}\rangle$ in (82) with respect to $g$ is shown in Fig. 11 for different values of $V / t$. The curves all have a very similar shape since the $g$ dependence of the total interaction energy $U\langle\hat{D}\rangle+2 V(C_{j=1}^{N N}+n^{2})$ is itself qualitatively very similar for all $V / U$. The existence of only a single variational parameter clearly rules out a detailed description of the properties of $\hat{H}_{\text {ext }}$ in terms of the GWF.

## XI. HIGHER DIMENSIONS

In higher dimensions graphs no longer have a simple polynomial structure in $n$ and $|q|$, owing to the nontrivial density dependence of the Fermi body even in the noninteracting case. In general the evaluation of the diagrams has to be done numerically.

![](./images/811683925553315842_12.jpg)

FIG. 11. Ground-state energy of the extended Hubbard model, (82), for the GWF for different values of $V / t$.

An important question is, whether the antiferromagnetism of the GWF at half-filling found in one dimension also exists in higher dimensions. From (48), which is valid in all dimensions, we may infer that the limiting value of the spin CF for $n=1$ at $|\mathbf{q}|=2 k_{F}$ in the atomic limit is determined by

$$
C^{S S}\left(|\mathbf{q}|=2 k_{F}, g=0, n=1\right)=1+\lim _{g \rightarrow 0}\left\lceil\frac{2 d}{g^{2}}\right\rceil.
\tag{83}
$$

In one dimension this limit diverges as given by (51). The same is true in infinite dimensions, where the Gutzwiller approximation has been found to be the exact result for the GWF, $^{30}$ and where $d \propto g$ for $g \rightarrow 0$.

Indeed the rules for evaluating graphs in infinite dimensions $^{30}$ may also be applied to the CF's. One finds that, owing to the particular structure of graphs contributing to $C^{S S}(\mathbf{q})$ which carry an external momentum $\mathbf{q}$, all diagrams in Figs. 2 and 5 reduce to ring diagrams as in Fig. 2(d), with maximally $(m+1)$ rings in $m$ th order. A ring is determined by $\prod_{0}(\mathbf{q})=1 / L \sum_{\mathbf{k}} n_{\mathbf{k}}^{0} n_{\mathbf{k}-\mathbf{q}}^{0}$. Even in infinite dimensions $\prod_{0}(\mathbf{q})$ has a nontrivial structure.

In view of these results for one and infinite dimensions one may conclude that for $n>1$ and in the atomic limit the spin correlations in the GWF have an antiferromagnetic divergence in any finite dimension, but that the prefactor vanishes in the limit of the infinite dimensions.

## XII. CONCLUSION

We have presented the analytic, approximation-free evaluation of four independent correlation functions for Hubbard-type models in one dimension in terms of the Gutzwiller wave function (GWF). The results are not only valid for arbitrary momentum (or spatial separation) but also for arbitrary particle density and correlation strength. In the atomic limit the density correlation function for small hole concentrations is found to be in very good agreement with the exact results. In the same limit the spin-correlation function is also in very good agreement with all available exact analytic and numerical results for the antiferromagnetic Heisenberg chain. Hence the GWF contains surprisingly accurate correlations in spite of its great simplicity. In fact, Haldane $^{39}$ and Shastry $^{40}$ recently proved than in the atomic limit the GWF is the exact solution of a spin-$\frac{1}{2}$ model with antiferromagnetic exchange coupling that falls off with the inverse square of the spin separation. The accuracy of the spin correlations in the GWF is somewhat surprising in view of the fact that the GWF does not describe the ground-state energy of the Hubbard model for $n=1$ and large $U / t$ very accurately, $^{21}$ i.e., causes logarithmic corrections in $t / U$ to the $(-t^{2} / U)$ behavior. $^{29,30}$ On the other hand, these deficiencies appear to be due to the lack of a subtle correlation between doubly occupied and empty sites in the strong-coupling limit, which are clearly

outside the scope of the GWF.²¹ It is therefore instruc- tive to learn that, in contrast to conventional wisdom, a variational wave function may describe a certain class of important correlations very well although it does not reproduce the ground-state energy very well.

The quality of the GWF in higher dimensions is not clear at present. Nonetheless we may conclude that the spin correlations in the atomic limit have an antiferro- magnetic divergence for $n=1$ in all dimensions. Even if an evaluation of correlation functions is no longer analyt- ically tractable, they may be calculated numerically by explicit calculation of the graphs in finite orders (see Figs. $2-5$ for $m \leq 3)$. This allows one to go up to order $(U / t)^{5}$ for arbitrary density or $n^{5}$ for arbitrary correlation strength, without too much effort.

Concerning superconducting fluctuations we found that correlations involving on-site, singlet Cooper pairs are suppressed in any dimension. More general types of pairing are being investigated now. The results for the correlation functions yield exact upper limits for the ground state energy of a large class of extended Hubbard models in one dimension, which may now all be evaluated with the GWF.

## ACKNOWLEDGMENT

We are grateful to W. Metzner for valuable discus- sions.

¹M. C. Gutzwiller, Phys. Rev. Lett. 10, 159 (1963).
²J. Hubbard, Proc. R. Soc. London Ser. A 276, 238 (1963).
³J. Kanamori, Prog. Theor. Phys. 30, 275 (1963).
⁴See, for example, G. Baskaran, Z. Zou, and P. W. Anderson, Solid State Commun. 63, 973 (1987); A. E. Ruckenstein, P. J. Hirschfeld, and J. Appel, Phys. Rev. B 36, 857 (1987); P. W. Anderson, G. Baskaran, Z. Zou, and T. Hsu, Phys. Rev. Lett.58, 2790 (1987); V. J. Emery, ibid. 58, 2794 (1987); S. Kivel-son, D. S. Rokhsev, and J. P. Sethna, Phys. Rev. B 35, 8865(1987).
⁵E. H. Lieb and F. Y. Wu, Phys. Rev. Lett. 20, 1445 (1968).
⁶H. Bethe, Z. Phys. 71, 205 (1931); L. Hulthén, Ark. Mat. Ast- ron. Fyz. 26A, No. 11 (1938).
⁷M. Takahashi, J. Phys. C 10, 1289 (1977).
⁸J. E. Hirsch, R. L. Sugar, D. J. Scalapino, and R. Blanken- becler, Phys. Rev. B 26, 5033 (1982).
⁹J. E. Hirsch, Phys. Rev. B 28, 4059 (1983); 31, 4403 (1983); 34,3216 (1986); H. Q. Lin and J. E. Hirsch, ibid. 35, 3359 (1987).
¹⁰J. E. Hirsch and D. J. Scalapino, Phys. Rev. B 27, 7169 (1983).
¹¹M. C. Gutzwiller, Phys. Rev. A 137, 1726 (1965).
¹²W. F. Brinkman and T. M. Rice, Phys. Rev. B 2, 4302 (1970).
¹³T. M. Rice, Philos. Mag. B 35, 419 (1985).
¹⁴P. W. Anderson and W. F. Brinkman, in The Helium Liquids, edited by J. G. M. Armitage and I. E. Farqar (Academic, New York, 1975), p. 315.
¹⁵D. Vollhardt, Rev. Mod. Phys. 56, 99 (1984).
¹⁶D. Vollhardt, P. Wölfle, and P. W. Anderson, Phys. Rev. B35, 6703 (1987).
¹⁷T. M. Rice and K. Ueda, Phys. Rev. Lett. 55, 995 (1985); Phys. Rev. B 34, 6420 (1986).
¹⁸C. M. Varma, W. Weber, and L. J. Randall, Phys. Rev. B 33,1015 (1986).
¹⁹P. Fazekas, J. Magn. Magn. Mater. 63&64, 545 (1987).
²⁰P. Fazekas and B. H. Brandow, Phys. Scr. 36, 809 (1987).
²¹T. A. Kaplan, P. Horsch, and P. Fulde, Phys. Rev. Lett. 49,889 (1982).
²²P. Horsch and T. A. Kaplan, J. Phys. C 16, L1203 (1983).
²³K. Hashimoto, Phys. Rev. B 31, 7368 (1985).
²⁴P. Horsch, Phys. Rev. B 24, 7351 (1981).
²⁵D. Baeriswyl and K. Maki, Phys. Rev. B 31, 6633 (1985).
²⁶D. Baeriswyl, J. Carmelo, and K. Maki, Synth. Met. (to be published).
²⁷C. Gros, R. Joynt, and T. M. Rice, Phys. Rev. B 36, 381(1987).
²⁸H. Yokoyama and H. Shiba, J. Phys. Soc. Jpn. 56, 1490 (1987).
²⁹W. Metzner and D. Vollhardt, Phys. Rev. Lett. 59, 121 (1987).
³⁰W. Metzner and D. Vollhardt, Phys. Rev. B 37, 7382 (1988).
³¹F. Gebhard and D. Vollhardt, Phys. Rev. Lett. 59, 1472(1987).
³²See, for example, A. A. Abrikosov, L. P. Gorkov and Y. E. Dzyaloshinskii, Quantum Field Theoretical Methods in Sta- tistical Physics (Pergamon, Oxford, 1965).
³³P. Horsch and P. Fulde, Z. Phys. B 36, 23 (1979).
³⁴A. Luther and I. Peschel, Phys. Rev. B 12, 3908 (1975); itshould be noted, however, that the derivation of the $(-1)^{j} / j$  behavior obtained by these authors is not rigorous. In fact, there might be logarithmic corrections to this result due to spin-Umklapp processes. A clear exposition has been given by F. D. M. Haldane, Phys. Rev. B 25, 4925 (1982); 26,5257(E)(1982).
³⁵P. W. Anderson, Phys. Rev. 115, 2 (1959).
³⁶M. Betsuyaku and I. Yokota, Phys. Rev. B 33, 6505 (1986).
³⁷T. A. Kaplan, P. Horsch, and J. Borysowicz, Phys. Rev. B 35,1877 (1987).
³⁸K. Kubo, T. A. Kaplan, and J. Borysowicz (unpublished).
³⁹F. D. M. Haldane, Phys. Rev. Lett. 60, 635 (1988).
⁴⁰B. S. Shastry, Phys. Rev. Lett. 60, 639 (1988).
⁴¹G. Stollhoff, Z. Phys. B 69, 61 (1987).
⁴²W. Metzner and D. Vollhardt (unpublished).