# Equilibration in long-range quantum spin systems from a BBGKY perspective

Rytis Paškauskas $^1$ and Michael Kastner $^{1,2}$

$^1$ National Institute for Theoretical Physics (NITheP), Stellenbosch 7600, South Africa
$^2$ Institute of Theoretical Physics, University of Stellenbosch, Stellenbosch 7600, South Africa

E-mail: rytis.paskauskas@gmail.com,kastner@sun.ac.za

**Abstract.** The time evolution of $\ell$-spin reduced density operators is studied for a class of Heisenberg-type quantum spin models with long-range interactions. In the framework of the quantum Bogoliubov-Born-Green-Kirkwood-Yvon (BBGKY) hierarchy, we introduce an unconventional representation, different from the usual cluster expansion, which casts the hierarchy into the form of a second-order recursion. This structure suggests a scaling of the expansion coefficients and the corresponding time scales in powers of $N^{1/2}$ with the system size $N$, implying a separation of time scales in the large system limit. For special parameter values and initial conditions, we can show analytically that closing the BBGKY hierarchy by neglecting $\ell$-spin correlations does never lead to equilibration, but gives rise to quasi-periodic time evolution with at most $\ell/2$ independent frequencies. Moreover, for the same special parameter values and in the large-$N$ limit, we solve the complete recursion relation (the full BBGKY hierarchy), observing a superexponential decay to equilibrium in rescaled time $\tau = tN^{-1/2}$.

## 1. Introduction

Equilibration and thermalization in closed quantum systems have recently seen renewed interest, triggered by the impressive progress in performing experiments with ultracold atoms and ions [1]. In these experiments the coupling to the environment is negligible on the accessible timescales, and they can therefore be regarded to a very good approximation as closed systems. Typically, equilibration (in a suitable sense) is expected to take place in closed quantum systems [2, 3, 4], but important exceptions are known to exist. Failure of equilibration in systems close to integrability has been observed experimentally by Kinoshita *et al.* [5], and a substantial body of theoretical and numerical work has been devoted to this problem over the last years (see [6] for a review).

Studying the long-time dynamics of many-body quantum systems in general is a daunting task. For numerical work, one is usually restricted to fairly small system sizes, much smaller than most experimental realizations and not anywhere close to the macroscopic regime. The situation is different for integrable systems where analytic solutions may exist and larger systems may be studied. However, these systems are known to show atypical behavior, possibly very different from the non-integrable systems one is often interested in [7].

One solvable model (a quantum spin model with Ising-type interactions and subjected to an external magnetic field) for which the long-time evolution can be studied analytically, was proposed by Emch [8] in 1966 and later studied by Radin [9] in more detail. For a certain class of initial conditions, the time evolution of the expectation values of operators $A$ of a certain kind can be calculated analytically for arbitrary system sizes $N$, showing non-Markovian relaxation to the thermal average in the thermodynamic limit $N \to \infty$ [8]. This model has been extended by one of us to the case of long-range interactions, i.e. spin-spin interactions decaying like $r^{-\alpha}$ with the distance $r$ on a $d$-dimensional lattice, where the exponent $\alpha$ satisfies $0 \leqslant \alpha \leqslant d$ [10, 11]. As in the short-range case, the expectation values of the operators $A$ relax to thermal equilibrium, but they do so on a time scale that diverges with the system size $N$: The larger the system is, the longer it takes to thermalize. In fact, the relaxation dynamics becomes so slow that, within a given experimental resolution and for large enough $N$, no deviation from the initial state will be observed.

A similar phenomenon, going under the name of quasi-stationary states, has received considerable attention in the field of classical long-range interacting systems [12, 13], and in particular in classical gravity [14]. In the classical context, kinetic theory, and in particular the Vlasov (or the collisionless Boltzmann) equation, has been successfully applied to describe these quasi-stationary states [15, 16, 12, 13, 17]. Such a Vlasov description is known to become exact for long-range systems in the thermodynamic limit, and is therefore also expected to be a good starting point for a description of large but finite systems [18]. The main goal of the present work is to study, similarly to the classical case, the long-time persistence of quasi-stationary non-equilibrium states and their final relaxation to equilibrium for long-range quantum spin systems within the framework of quantum kinetic theory. We can then test the predictions of the quantum kinetic theory against the analytic result for the Emch- Radin model reported in [10, 11], but the scope of such a kinetic theory goes beyond this model: On the basis of a tested and well-working kinetic theory, equilibration can then be studied for non-integrable generalizations of the Emch-Radin model, or non-integrable long-range variants of the Heisenberg model for which exact solutions are not known.

In addition to providing a tool for investigating the dynamics of quantum spin models, our results also shed light on more general features regarding the role of closure conditions when truncating the BBGKY hierarchy: The particularly simple structure of spin-1/2 lattice models facilitates analytic calculations beyond what can be achieved in continuum systems, and an understanding of the effect of approximation schemes is easier to attain.

The article is structured as follows: In section 2 we introduce a fairly general class of long-range interacting quantum Heisenberg models with anisotropic interactions, subjected to an external magnetic field, and discuss its relation to the exactly solvable long-range Emch-Radin model. A short introduction to the quantum BBGKY hierarchy is given in section 3, with special emphasis paid to the role of closure conditions when truncating the hierarchy. In section 4.1, we introduce a representation of the hierarchy, i.e. a certain choice of basis in the underlying Hilbert space, different from the conventional cluster expansion. In section 4.3, the BBGKY hierarchy is expressed in terms of this representation, and we find that it has the form of a second- order recursion relation. This structure turns out to be crucial for the derivation of our results. First, as discussed in section 5, the recursion relation suggests a scaling of the expansion coefficients and the corresponding time scales in powers of $N^{1/2}$ with

the system size $N$, implying a separation of time scales in the large system limit.
The largest time scale is found to diverge proportionally to $N^{1/2}$ in the large system
limit. As a consequence, equilibration is expected on a time scale that diverges in the
thermodynamic limit, in agreement with what is known about the long-range Emch-
Radin model. In section 6, we consider the long-range anisotropic quantum Heisenberg
model for a special set of parameter values and initial conditions for which calculations
are easier to perform. Under these restrictions, we can show analytically in section 6.1
that closing the BBGKY hierarchy by neglecting $\ell$-spin correlations does never lead
to equilibration, but gives rise to quasi-periodic time evolution with at most $\ell/2$
independent frequencies. Moreover, in section 6.2 we solve the untruncated recursion
relation (full BBGKY hierarchy) in the large-$N$ limit, observing a superexponential
decay to equilibrium in rescaled time $\tau = tN^{-1/2}$. This behavior and the observed
time scale are exact analytic results which are in a perfect agreement with the Emch-
Radin model. A more detailed discussion of these results and their implications on
the general considerations of section 5 is given in section 7, and we summarize our
findings in section 8.

## 2. Long-range anisotropic quantum spin model

Two quantum spin models are introduced in this section. The first one, an anisotropic
quantum Heisenberg model with Curie-Weiss type interactions, is the one actually
studied in this work. The second one, named after Emch and Radin, is an Ising type
quantum spin model in a longitudinal magnetic field, with two-body interactions that
decay with the distance as a power law. For special choices of the parameters, both
models agree, and the known exact results on the dynamics of the Emch-Radin model
can be used to test the validity of our results regarding relaxation to equilibrium in
the anisotropic quantum Heisenberg model.

### 2.1. Curie-Weiss anisotropic quantum Heisenberg model

Consider $N$ identical spin-$1/2$ particles, attached to the sites of a $d$-dimensional lattice.
The corresponding quantum dynamics takes place on the Hilbert space

$$
\mathscr{H}_{N}=\bigotimes_{i=1}^{N} \mathbb{C}_{i}^{2},
\tag{1}
$$

where the $\mathbb{C}_{i}^{2}$ are identical replicas of the two-dimensional Hilbert space of a single
spin-$1/2$ particle. The unitary time evolution on $\mathscr{H}_{N}$ is generated by the $N$-body
Hamiltonian

$$
H_{1 \ldots N}=\sum_{i=1}^{N} H_{i}+\sum_{\substack{i, j=1 \\ i<j}}^{N} V_{i j}
\tag{2}
$$

consisting of an on-site potential and a spin-spin interaction potential,

$$
H_{i}=-\sum_{a \in \mathcal{I}} h^{a} \sigma_{i}^{a}, \quad V_{i j}=-\frac{1}{N} \sum_{a, b \in \mathcal{I}} J^{a b} \sigma_{i}^{a} \sigma_{j}^{b},
\tag{3}
$$

where $\sigma_{i}^{a}$ denotes the Pauli operators at a lattice site $i$ and

$$
\mathcal{I}=\{x, y, z\}
\tag{4}
$$

is the set of component indices. The spin-spin interaction $V_{ij}$ is of Curie-Weiss type, coupling each spin to every other on the lattice, and the strength of the coupling is determined by a $3 \times 3$ matrix $J$ of coupling constants with matrix elements $J^{ab}$. The $1/N$ prefactor in (3) is introduced to render the energy per spin finite in the thermodynamic limit. The long-range interactions, and the $N$-dependent prefactor they are necessitating, can lead to peculiar properties. In equilibrium, it may happen that different statistical ensembles (like the microcanonical and the canonical one) are nonequivalent in the thermodynamic limit, and issues of this kind have been discussed in [19, 20]. In the present article, we will focus on peculiarities of the non-equilibrium behavior of this model.

### 2.2. Emch-Radin model

The Emch-Radin model [8, 9] has a Hamiltonian similar to (3), but with a two-body potential
$$
V_{i j}=-\frac{1}{N} J_{i j}^{z z} \sigma_{i}^{z} \sigma_{j}^{z} \tag{5}
$$

So in contrast to the anisotropic Heisenberg model's two-body potential (3), $J^{zz}$ is the only nonzero element of the coupling matrix $J$. Moreover, the spins are associated to the sites of a $d$-dimensional lattice, and the coupling between spins $\sigma_{i}^{z}$ and $\sigma_{j}^{z}$ depends algebraically on their distance $D(i, j)$ on the lattice, i.e. $J_{i j}^{z z} \propto D(i, j)^{-\alpha}$ with some nonnegative exponent $\alpha$. The on-site potential potential is of the same form as in (3), but with an external magnetic field $h=(0,0, h^{z})$ pointing in $z$-direction. It follows from these definitions that the Hamilton operators of the anisotropic Heisenberg model and the Emch-Radin model have a special case in common: For $\alpha=0$ the distance dependence of the Emch-Radin coupling $J_{i j}^{z z}$ is eliminated and the Hamiltonian is identical to that of the Curie-Weiss anisotropic quantum Heisenberg model with $J=\operatorname{diag}(0,0, J^{z z})$ and $h=(0,0, h^{z})$.

The permissible initial states in the Emch-Radin model are restricted to density operators which are diagonal in the $\sigma^{x}$ tensor product eigenbasis of $\mathscr{H}_{N}$. Under this condition, an analytic expression can be obtained for the time evolution of expectation values of operators of the form
$$
A=\sum_{i=1}^{N} a_{i} \sigma_{i}^{x} \tag{6}
$$
with real coefficients $a_{i}$ [8]. In the case of short-range interactions, i.e. for exponents $\alpha>d$, the time evolution of the expectation values $\langle A\rangle(t)$ was analyzed in the thermodynamic limit $N \rightarrow \infty$ in [8]. The system was found to relax to equilibrium, and the process of relaxation was shown to be non-Markovian. The long-range scenario with $0 \leqslant \alpha \leqslant d$, analyzed in $[10,11]$, was shown to display a remarkably different behavior: The time scale at which equilibration appears to occur was found to increase proportionally to $N^{r}$ with $r=\min \{1 / 2,1-\alpha\}$. This finding implies a diverging equilibration time scale in the thermodynamic limit (see figure 1 for an illustration).

The analytic results in [8] and $[10,11]$ are not easily extended to other parameter values, different initial conditions, or more general observables. We believe, however, that similar quasi-stationary behavior (i.e. long-lived non-equilibrium behavior persist- ing on a time scale that diverges with increasing system size) shows up under much more general conditions. The aim of this work is to employ quantum kinetic theory

![](./images/867752764254453911_1.jpg)

Figure 1. Time evolution of the expectation value of the observable $A$ for magnetic field $h=0$, coupling matrix $J=\mathrm{diag}(0,0,1)$, and exponent $\alpha=0$. The plot was obtained by evaluating with MATHEMATICA the analytic formula (9) of reference [10] for various system sizes $N$. The result is valid for arbitrary initial states and arbitrary coefficients $a_i$ in the expansion (6) of $A$. The expectation value shows an apparent decay towards its zero equilibrium value, but on a time scale that depends strongly on the system size $N$ (note the logarithmic time scale). The decay is only apparent as, on time scales much longer than shown, recurrent behavior (Loschmidt echos) occur due to the system's finite size. Similar behavior is observed for other values of $\alpha$ between zero and the lattice dimension $d$.

to study the long-time dynamics of long-range interacting quantum spin systems of the Heisenberg type (2) and (3). For the moment, we restrict the analysis to Curie- Weiss-type potentials as in (3), but we expect qualitatively similar results to hold for algebraically decaying long-range potentials with exponents $\alpha$ between zero and the lattice dimension $d$.

### 3. BBGKY hierarchy

The density operator $\rho_N$ of an $N$-spin system is a self-adjoint, positive, trace-class operator, acting on the Hilbert space $\mathscr{H}_N$. We use the normalization convention
$$
\operatorname{Tr}_{1 \ldots N} \rho_N=1, \tag{7}
$$
where $\operatorname{Tr}_{1 \ldots N}$ denotes a trace over all $N$ factors of the tensor product Hilbert space (1). The expectation value of an operator $A$ with respect to $\rho_N$ is given by
$$
\langle A\rangle=\operatorname{Tr}_{1 \ldots N}\left(\rho_N A\right). \tag{8}
$$

The time evolution of the density operator is governed by the von Neumann equation
$$
\mathrm{i} \hbar \partial_t \rho_N=\left[H_{1 \ldots N}, \rho_N\right]. \tag{9}
$$

Reduced $\ell$-particle density operators are derived from $\rho_N$ by tracing out $(N-\ell)$ of the factors of $\mathscr{H}_N$,
$$
F_{1 \ldots \ell}=\operatorname{Tr}_{\ell+1 \ldots N} \rho_N, \tag{10}
$$
where $\operatorname{Tr}_{\ell+1 \ldots N}$ denotes such a partial trace. The $F_{1 \ldots \ell}$ are again density operators, i.e. self-adjoint, positive operators of trace-class. Since they are all derived from the same $\rho_N$, the reduced density operators are not independent, but satisfy a collection of consistency conditions of the form
$$
\operatorname{Tr}_{\ell} F_{1 \ldots \ell}=F_{1 \ldots \ell-1} \tag{11}
$$

(with the convention of $F_0 \equiv 1$) which we will refer to as the trace property of $F_{1...\ell}$.

We will assume in the following that all reduced density operators $F_{1...\ell}$ are invariant under $\ell$-permutations of their indices from the set $\{1,\dots,N\}$. For $\ell=1$, for example, this means simply that
$$
F_1 = F_2 = \cdots = F_N, \tag{12}
$$
and for $\ell=2$ this property amounts to
$$
F_{ij} = F_{kl} \quad \forall i,j,k,l \in \{1,\dots,N\}, \quad i \neq j, \quad k \neq l. \tag{13}
$$

In the context of continuum (off-lattice) systems, permutation invariance is usually justified by the indistinguishability of particles. For the lattice systems investigated in the present article, the spin degrees of freedom can of course be distinguished by the lattice site they are attached to. Instead, in that context the assumption of permutation invariance amounts to assuming that the system is in a homogeneous state, i.e. different subsystems behave similarly. This assumption is expected to be justified in the Heisenberg model (3) with ferromagnetic coupling $J^{ab} \geqslant 0$, but will be violated in the presence of anti-ferromagnetism. Since the Hamiltonian (2) and (3) is permutation invariant as well, the homogeneity of an initial state will be preserved under time evolution.

Under the assumption of permutation invariance, the Bogoliubov-Born-Green-Kirkwood-Yvon (BBGKY) hierarchy is obtained by applying the partial trace $\mathrm{Tr}_{\ell+1...N}$ to the von Neumann equation (9). For a Hamiltonian of the form (2), the hierarchy can be written as
$$
\mathrm{i}\hbar\partial_t F_{1...\ell} = \sum_{i=1}^{\ell} [H_i, F_{1...\ell}] + \sum_{\substack{i,j=1 \\ i<j}}^{\ell} [V_{ij}, F_{1...\ell}] + (N-\ell)\mathrm{Tr}_{\ell+1} \sum_{i=1}^{\ell} [V_{i,\ell+1}, F_{1...\ell+1}]. \tag{14}
$$

For a given number $N$ of spins, this is a finite set of equations, and it is fully equivalent to the von Neumann equation (9) from which it was derived: A solution of the BBGKY hierarchy is equivalent to an exact solution for the density operator $\rho_N$, from which the reduced density operators $F_{1...\ell}$ can be obtained via equation (10).

### 3.1. Closure conditions
In the form (14), the hierarchy is not yet particularly useful: Solving the full hierarchy is as difficult as solving the von Neumann equation (and therefore impossible for most cases of interest). For many physical problems, it turns out that $n$-particle correlations are naturally ordered by decreasing relevance, and only those with $n \leqslant \ell$ have to be considered (where $\ell$ is some small number, usually not larger than 4, depending on the system under investigation and the quantity of interest). It is therefore often sufficient to consider only the time evolution of the first $\ell$ reduced density operators. Hence a useful computational tool may be derived by truncating the hierarchy at the level of the $\ell$-spin reduced density operator. However, the achieved simplification of such a truncation comes at the expense of an approximation.

Simply truncating the set (14) after the first $\ell$ equations results in an ill-defined problem: The $\ell$th equation, which determines the time evolution of $F_{1...\ell}$, requires $F_{1...\ell+1}$ as an input, but the equation determining $F_{1...\ell+1}$ has been eliminated by truncation. To obtain a well-defined system of $\ell$ equations, a closure condition has to be postulated between $F_{1...\ell+1}$ and the lower order reduced density operators. We

refer to such a relation among $F_{1 \ldots \ell+1}$ and all of the $\{F_{1 \ldots j}\}_{j=1}^{\ell}$ as an $\ell$th order closure condition.

A frequently used truncation scheme of the BBGKY hierarchy is based on the so- called cluster expansion [21], where correlation operators $G_{1 \ldots \ell}$ are defined according to the following scheme,

$$
F_{12}=F_{1} F_{2}+G_{12}, \quad(15 a)
$$

$$
F_{123}=F_{1} F_{2} F_{3}+F_{1} G_{23}+F_{2} G_{31}+F_{3} G_{12}+G_{123}, \quad(15 b)
$$

$$
\begin{aligned}
F_{1234}= & F_{1} F_{2} F_{3} F_{4}+F_{1} F_{2} G_{34}+F_{1} F_{3} G_{24}+F_{1} F_{4} G_{23}+F_{2} F_{3} G_{14} \\
& +F_{2} F_{4} G_{13}+F_{3} F_{4} G_{12}+G_{12} G_{34}+G_{13} G_{24}+G_{14} G_{23} \\
& +F_{1} G_{234}+F_{2} G_{134}+F_{3} G_{124}+F_{4} G_{123}+G_{1234}, \quad(15 c)
\end{aligned}
$$

and so on. Based on this expansion, a straightforward way to close the BBGKY hierarchy at $\ell$th order is to express (14) in terms of the correlation operators and set

$$
G_{1 \ldots \ell+k}=0 \quad \forall 1 \leqslant k \leqslant N-\ell. \quad(16)
$$

We shall refer to this approximation as the $\ell$th order correlation closure.

Needless to say that the accuracy of the approximation will depend on the "quality" of the closure condition. Regardless of the details of the closure, it seems plausible to expect an improvement in the accuracy with increasing order $\ell$ of the truncation. We have tested this expectation by numerically investigating the BBGKY hierarchy truncated by correlation closures of various orders. The density operators were expanded in the basis of Pauli matrices and the evolution was performed for the coefficients of the expansion (discussed in detail in section 4). The one-spin reduced density operator in this expansion reads

$$
F_{1}=\frac{1}{2}\left(\mathbb{1}_{1}+\sum_{a \in \mathcal{I}} f_{1}^{a} \sigma_{1}^{a}\right), \quad(17)
$$

where $\mathbb{1}_{1}$ denotes the identity operator on the one-spin Hilbert space. The real expansion coefficients $f_{1}^{a}$ are related to the mean spin expectation value, as

$$
\overline{\sigma^{a}} \equiv\left\langle\frac{1}{N} \sum_{i=1}^{N} \sigma_{i}^{a}\right\rangle=\operatorname{Tr}_{1 \ldots N} \frac{1}{N} \sum_{i=1}^{N} \sigma_{i}^{a} \rho_{N}=\operatorname{Tr}_{1} \sigma_{1}^{a} F_{1}=f_{1}^{a}. \quad(18)
$$

The time evolution of the modulus

$$
\left|f_{1}\right|=\sqrt{\left(f_{1}^{x}\right)^{2}+\left(f_{1}^{y}\right)^{2}+\left(f_{1}^{z}\right)^{2}} \quad(19)
$$

is displayed in figure 2 for correlation closures of orders $\ell=2,3,4$. To summarize the simulations, the effect of increasing the order of the truncation is rather disastrous and the long-time evolution is badly predicted at either order: According to definition (10), density operators $F_{1 \ldots \ell}$ have to be positive operators, and this property is conserved by the von Neumann equation (9). In the Pauli representation (17), positivity of $F_{1}$ amounts to the condition

$$
\left|f_{1}\right| \leqslant 1 \quad(20)
$$

which, as is evident from figure 2, is violated for the correlation closures of order $\ell \geqslant 3$ after relatively short times. So the higher-order correlation closures not only fail to improve on the lower-order ones regarding the relaxation to equilibrium, but they even fail to preserve the basic features of the density operators. We will see in the forthcoming sections that the latter is an artefact of numerics, caused by the presence

![](./images/867752764254453911_2.jpg)

of oscillatory degrees of freedom with several fundamentally different time scales. This problem will be dealt with in section 5, where an averaging procedure is defined that eliminates the fast oscillations while correctly reproducing the evolution on the slow time scale.

It is the main objective of the present paper to investigate and better understand the effect of the correlation closures at various orders, and in particular the question of whether and how this type of closure condition can correctly describe the relaxation to equilibrium in a long-range quantum spin system in the thermodynamic limit.

## 4. Representation of the BBGKY hierarchy

The derivation of the results reported in this article depends crucially on a particular expansion of the reduced $\ell$-spin density operators in the basis of Pauli operators. Expressed in terms of this expansion, the BBGKY hierarchy reveals a recursive structure which is at the basis of the analytical results obtained.

### 4.1. Definition of the expansion

Inspecting the BBGKY hierarchy (14), one might at a first glance get the impression that the reduced density operators $F_{1 \ldots \ell}$ are coupled by a first order recursion, in the sense that the time evolution equation of $F_{1 \ldots \ell}$ contains only one further reduced density operator, $F_{1 \ldots \ell+1}$. However, this is not really true, as in fact the various $F_{1 \ldots \ell}$ are dependent on each other through trace properties (11). The crucial idea behind

the expansion introduced in this section is to choose the expansion coefficients such that the trace property is automatically satisfied. Then the resulting coefficients are independent variables, on the basis of which the "true" structure of the equations can be studied.

Expanding the first few reduced density operators in the Pauli basis $\{\mathbb{1},\sigma^x,\sigma^y,\sigma^z\}$, one can verify by inspection that the following choice of expansion coefficients satisfies the trace properties (11),

$$
F_{1} \ =\frac{1}{2}\left(\mathbb{1}_{1}+\sum_{a \in \mathcal{I}} f_{1}^{a} \sigma_{1}^{a}\right), \tag{21a}
$$

$$
F_{12} \ =\frac{1}{4}\left(\mathbb{1}_{12}+\sum_{a \in \mathcal{I}} f_{1}^{a}(\sigma_{1}^{a}+\sigma_{2}^{a})+\sum_{a,b \in \mathcal{I}} f_{2}^{a b} \sigma_{1}^{a} \sigma_{2}^{b}\right), \tag{21b}
$$

$$
\begin{aligned}
F_{123}= & \frac{1}{8}\left(\mathbb{1}_{123}+\sum_{a \in \mathcal{I}} f_{1}^{a}(\sigma_{1}^{a}+\sigma_{2}^{a}+\sigma_{3}^{a})\right. \\
& \left.+\sum_{a,b \in \mathcal{I}} f_{2}^{a b}(\sigma_{1}^{a} \sigma_{2}^{b}+\sigma_{2}^{a} \sigma_{3}^{b}+\sigma_{3}^{a} \sigma_{1}^{b})+\sum_{a,b,c \in \mathcal{I}} f_{3}^{a b c} \sigma_{1}^{a} \sigma_{2}^{b} \sigma_{3}^{c}\right). \tag{21c}
\end{aligned}
$$

We introduce several definitions to facilitate the general formulation. For the purpose of counting the particle (subscript) indices, we define, for $1 \leqslant n \leqslant \ell \leqslant N$, the set $\mathfrak{P}_{n}(\ell)$ consisting of all $n$-element permutations $(p_{1},\dots,p_{n})$ of particle labels $p_{i} \in \{1,\dots,\ell\}$ such that $p_{i} < p_{j}$ for all $1 \leqslant i < j \leqslant n$ (i.e. all sequences are strictly increasing). Considering for example $n=2$, we have $\mathfrak{P}_{2}(\ell)=\{(1,2),(1,3),\dots,(1,\ell),(2,3),\dots,(\ell-1,\ell)\}$. Moreover, we use the notation

$$
\sigma_{p}^{a}=\prod_{i=1}^{n} \sigma_{p_{i}}^{a_{i}} \tag{22}
$$

with $p \in \mathfrak{P}_{n}(\ell)$ and the component multi-index $a=(a_{1},a_{2},\dots,a_{n})$ with $a_{i} \in \mathcal{I}$. With these definitions, the general pattern behind (21a)-(21c) can be captured by the formula

$$
F_{1 \dots \ell}=2^{-\ell} \sum_{n=0}^{\ell} \sum_{a \in \mathcal{I}^{n}} f_{n}^{a} \sum_{p \in \mathfrak{P}_{n}(\ell)} \sigma_{p}^{a}, \tag{23}
$$

with the convention $f_{0}^{a} \equiv 1$.

By inspection of the last terms in (21b) and (21c), it follows that $f_{2}^{a b}$ and $f_{3}^{a b c}$ have to be symmetric with respect to permutations of their superscript indices in order to make sure that the resulting expressions for $F_{12}$ and $F_{123}$ are symmetric under particle exchange. As a result, not all components $f_{\ell}^{a}$ are independent variables. In particular, any element $f_{\ell}^{a'}$ is equal to the element $f_{\ell}^{a(m)}$, where

$$
a(m)=(\underbrace{x,\dots,x}_{m_{x} \text{ elements}},y,\dots,y,z,\dots,z) \tag{24}
$$

is a permutation of $a'$ with the components $x,y,z$ arranged in contiguous blocks of $m_{x}$, $m_{y}$, and $m_{z}$ labels. Hence, all independent components of $f_{\ell}$ can be labelled uniquely by a triple of nonnegative integers

$$
m=(m_{x},m_{y},m_{z}), \quad m_{i} \geqslant 0, \tag{25}
$$

where $m_{x}+m_{y}+m_{z}=\ell$. In the following, notation in terms of $a$ and $m=m(a)$ will be considered as equivalent, $f_{\ell}^{a} \equiv f_{\ell}^{m}$.

The number of independent components of $f_\ell^m$ is equal to $d(\ell)=(\ell+1)(\ell+2)/2$.
Therefore the $N$-spin density operator is described by
$$
D(N)=\sum_{\ell=1}^N d(\ell)=\frac{1}{6}(N+1)(N+2)(N+3)-1\tag{26}
$$
independent real variables, a number substantially smaller than the $4^N$ real variables
necessary to parameterize an arbitrary Hermitian operator on the $N$-spin Hilbert space
$\mathscr{H}_N$ given in (1).

### 4.2. Relation to the cluster expansion
In order to implement the correlation closures (16), we need to express the correlation
operators $G_{1\ldots\ell}$ in terms of the expansion coefficients $f_\ell^{a_1\ldots a_\ell}$. Substitution of the
expansion (23) of $F_{1\ldots\ell}$ into the cluster expansion (15a)-(15c) leads to
$$
G_{1\ldots\ell}=2^{-\ell}\sum_{a\in\mathcal{I}^\ell}g_\ell^a\boldsymbol{\sigma}_{(1,\ldots,\ell)}^a,\tag{27}
$$
where $g_\ell^a$ are expressed in terms of $f_\ell^a$ by relations of the type
$$
f_2^{ab}\ =g_2^{ab}+f_1^a f_1^b,\tag{28a}
$$
$$
f_3^{abc}\ =g_3^{abc}+f_1^a f_2^{bc}+f_1^b f_2^{ca}+f_1^c f_2^{ab}-2f_1^a f_1^b f_1^c,\tag{28b}
$$
$$
\begin{aligned}
f_4^{abcd}=g_4^{abcd}&+f_1^a f_3^{bcd}+f_1^b f_3^{acd}+f_1^c f_3^{abd}+f_1^d f_3^{abc}\\
&+f_2^{ab} f_2^{cd}+f_2^{ac} f_2^{bd}+f_2^{ad} f_2^{bc}\\
&-2f_1^a f_1^b f_2^{cd}-2f_1^a f_1^c f_2^{bd}-2f_1^a f_1^d f_2^{bc}-2f_1^b f_1^c f_2^{ad}\\
&-2f_1^b f_1^d f_2^{ac}-2f_1^c f_1^d f_2^{ab}+6f_1^a f_1^b f_1^c f_1^d.
\tag{28c}
\end{aligned}
$$
The correlation closures of orders $\ell=2,3,4$ discussed in section 3.1 are obtained by
setting $g_{\ell+1}=0$.

### 4.3. BBGKY in terms of the expansion coefficients
Substituting the expansions (23) into the BBGKY hierarchy (14), the time evolution
equations for the coefficients $f_\ell$ can be obtained. After a cumbersome but rather
straightforward calculation which is reported in Appendix A, one finds the BBGKY
hierarchy in terms of the coefficients $f_\ell$ to be
$$
\frac{\hbar}{2}\partial_t f_\ell^a=v_{\ell0}^a(f_\ell)+\lambda v_{\ell-}^a(f_{\ell-1})+(1-\ell\lambda)v_{\ell+}^a(f_{\ell+1}),\tag{29}
$$
where the definition $\lambda=1/N$ has been introduced. Moreover, we defined
$$
v_{\ell0}^a(f_\ell)\ \ =-\sum_{b,c\in\mathcal{I}}h^b\sum_{i=1}^\ell\varepsilon^{a_i bc}f_\ell^{a-a_i+c},\tag{30a}
$$
$$
v_{\ell-}^a(f_{\ell-1})=-\sum_{b,c\in\mathcal{I}}\sum_{\substack{i,j=1\\i\neq j}}^\ell\varepsilon^{a_i bc}J^{ba_j}f_{\ell-1}^{a-a_i+c-a_j},\tag{30b}
$$
$$
v_{\ell+}^a(f_{\ell+1})=-\sum_{b,c,d\in\mathcal{I}}J^{bd}\sum_{i=1}^\ell\varepsilon^{a_i bc}f_{\ell+1}^{a-a_i+c+d},\tag{30c}
$$

where $\varepsilon^{abc}$ is the Levi-Civita symbol defined according to the convention $\varepsilon^{xyz}=1$.
With an abominable abuse of notation,
$$
a-a_{i}+c=\left(a_{1}, \ldots, a_{i-1}, c, a_{i+1}, \ldots, a_{\ell}\right)\qquad(31a)
$$
in (30a) denotes the multi-index which is obtained from $a$ by replacing its $i$th element by $c$. Similarly,
$$
a-a_{i}+d-a_{j}=\left(a_{1}, \ldots, a_{i-1}, d, a_{i+1}, \ldots, a_{j-1}, a_{j+1}, \ldots, a_{\ell}\right)\qquad(31b)
$$
in (30b) is derived from $a$ by replacing the $i$th element by $d$ and then deleting the $j$th entry of $a$, and
$$
a-a_{i}+d+c=\left(a_{1}, \ldots, a_{i-1}, d, a_{i+1}, \ldots, a_{\ell}, c\right)\qquad(31c)
$$
in (30c) is obtained from $a$ by replacing the $i$th element by $d$ and then appending $c$.

All the terms in $v_{\ell 0}$ and $v_{\ell \pm}$ are linear in the coefficients $f_{\ell}$ and $f_{\ell \pm 1}$. As inherited from the Hamiltonian, $v_{\ell 0}$ contains only the local field components $h^{a}$, while $v_{\ell \pm}$ contain the spin interaction matrix $J$. Equation (29) shows that the $\ell$th order coefficients $f_{\ell}^{a}$ are coupled to coefficients of orders $\ell \pm 1$, but not to coefficients $f_{n}^{a}$ with $|n-\ell|>1$. It is this second-order recursion structure that is at the basis of the results derived in the following.

## 5. The thermodynamic Limit

The thermodynamic limit is a delicate issue in general, especially in the presence of long-range interactions. Recent work, mostly on classical systems, has taught us that complications increase further when one is interested in long-time asymptotics (or long-time averages) of long-range interacting systems, and their thermodynamic limit. The issue is illustrated by the time evolution of the expectation value $\langle A\rangle(t)$ in figure 1 where, for the Emch-Radin model, it was observed that relaxation to equilibrium takes place on a time scale that diverges with the system size $N$ as $N^{r}$, with an exponent $r=\min \{1 / 2,1-\alpha\}>0$. As a consequence, depending on the order in which the long-time average and the large-system limit are taken, different limit values are obtained: Performing first the long-time average $\ddagger$ and then the large system limit yields the equilibrium value $\langle A\rangle=0$, whereas the reverse order of the limits results in $\langle A\rangle=\langle A\rangle(0)$. More generally, instead of taking one limit after the other, one can consider any path to infinity in the $(N, t)$ plane and take both limits simultaneously along this path. It will depend on the physical question of interest which limiting procedure and which path is the suitable one. In this section we discuss one such path which, as we shall see, is appropriate for studying the approach to thermodynamic equilibrium of the long-range interacting spin system (2) and (3).

As always when performing a thermodynamic limit, it is essential to identify suitably defined quantities for which this limit is well-defined and nontrivial. With this aim in mind, consider the scaling transformations
$$
t=\hbar \tau \lambda^{-r} / 2,\qquad(32a)
$$
$$
f_{\ell}=f_{\ell}^{\prime} \lambda^{s \ell},\qquad(32b)
$$

$\ddagger$ For finite system sizes, the long-time limit is not well defined, as the time evolution is periodic and recurrences (Loschmidt echos) occur. The period of these recurrences, however, is exceedingly long for reasonably large systems, and the excursions away from the ensemble average are short-lived. For these reasons, the time-average of the expectation value $\langle A\rangle(t)$ has a well-defined long-time limit which, for large $N$, is close to the ensemble average. When the large-system limit is taken first, these problems do not occur, the long-time limit exists and is equal to the long-time average.

where the parameters $r$ and $s$ are still to be determined. Substitution into (29) and multiplication by $\lambda^{-r-s\ell}$ yields the BBGKY hierarchy in the scaled variables,
$$
\partial_{\tau} f_{\ell}^{\prime}=\lambda^{-r} v_{\ell 0}\left(f_{\ell}^{\prime}\right)+\lambda^{1-r-s} v_{\ell-}\left(f_{\ell-1}^{\prime}\right)+\lambda^{s-r}(1-\ell \lambda) v_{\ell+}\left(f_{\ell+1}^{\prime}\right). \quad(33)
$$

The first term on the right-hand side of this equation depends, via $v_{\ell 0}$, on the magnetic field components $h^{a}$ (i.e. on the on-site potential), but not on the spin-spin coupling $J$. The effect of such a constant field on the dynamics is known to be a simple spin precession, unrelated to the relaxation to equilibrium our analysis is focussing on. Moreover, as we will see later, its frequency turns out to be divergent on the time scale of equilibration.

It is therefore convenient to hide the presence of the first term on the right-hand side of (33) by writing the BBGKY hierarchy (14) in some kind of interaction picture. This amounts to absorbing the unitary time evolution, caused by the one-spin terms $H_{i}$ in the Hamiltonian (2), in the definition of a new set of reduced density operators,
$$
U_{1 \ldots \ell}=\exp \left[\frac{\mathrm{i} t}{\hbar} \sum_{i=1}^{\ell} H_{i}\right] F_{1 \ldots \ell} \exp \left[-\frac{\mathrm{i} t}{\hbar} \sum_{i=1}^{\ell} H_{i}\right].\qquad(34)
$$

The BBGKY hierarchy in the interaction picture is then given by
$$
\mathrm{i} \hbar \partial_{t} U_{1 \ldots \ell}=\sum_{\substack{i, j=1 \\ i<j}}^{\ell}\left[\tilde{V}_{i j}(t), U_{1 \ldots \ell}\right]+(N-\ell) \operatorname{Tr}_{\ell+1} \sum_{i=1}^{\ell}\left[\tilde{V}_{i, \ell+1}(t), U_{1 \ldots \ell+1}\right],\qquad(35)
$$
where the two-body potential now is explicitly time-dependent,
$$
\tilde{V}_{i j}(t)=\exp \left[\frac{\mathrm{i} t}{\hbar}\left(H_{i}+H_{j}\right)\right] V_{i j} \exp \left[-\frac{\mathrm{i} t}{\hbar}\left(H_{i}+H_{j}\right)\right].\qquad(36)
$$

To compute the explicit form of $\tilde{V}_{i j}$, note that Pauli operators on different lattice sites commute, and therefore the exponentials of sums in (36) can be factorized into a product of exponentials. Define the matrix $B(b)$ as
$$
\begin{aligned}
B(b) \sigma & =e^{-\mathrm{i} \sigma b} \sigma e^{\mathrm{i} \sigma b} \\
& =\sigma \cos |2 b|+2 \hat{b}(\hat{b} \cdot \sigma) \sin ^{2}|b|+(\sigma \times \hat{b}) \sin |2 b|,
\end{aligned}\qquad(37)
$$
with $b=(b^{x}, b^{y}, b^{z}), \sigma=(\sigma^{x}, \sigma^{y}, \sigma^{z}),|b|=[(b^{x})^{2}+(b^{y})^{2}+(b^{z})^{2}]^{1 / 2}$, and $\hat{b}=b /|b|$.
Applying (37) to the exponential factors in (36) yields
$$
\tilde{V}_{12}=-\frac{1}{N} \sum_{a, b \in \mathcal{I}} \tilde{J}^{a b} \sigma_{i}^{a} \sigma_{j}^{b}\qquad(38)
$$
in a form that is equivariant to $V_{12}$ in (3), with a transformed, time-dependent coupling matrix
$$
\tilde{J}=B(h t / \hbar)^{T} J B(h t / \hbar).\qquad(39)
$$

Time appears only in the trigonometric functions in $B$, therefore $B(h t / \hbar)$ is periodic with period $T=\pi \hbar /|h|$. The elements of $B(b)$ can be represented in the form
$$
B(b)=\left(\begin{array}{ccc}
c^{0}+c^{x x} & c^{x y}+c^{z} & c^{x z}-c^{y} \\
c^{x y}-c^{z} & c^{0}+c^{y y} & c^{y z}+c^{x} \\
c^{x z}+c^{y} & c^{y z}-c^{x} & c^{0}+c^{z z}
\end{array}\right),\qquad(40)
$$
where $c^{0}=\cos |2 b|, c^{i}=\hat{b}^{i} \sin |2 b|$, and $c^{i j}=2 \hat{b}^{i} \hat{b}^{j} \sin ^{2}|b|$ with $i, j \in \mathcal{I}$.

Comparing the original BBGKY hierarchy (14) to the one in the interaction picture (35), we observe that the single-spin term—whose diverging frequency might be bothering us in the thermodynamic limit—can be eliminated from the BBGKY hierarchy by passing to the interaction picture, at the expense of a time-periodic interaction potential (36). Next we introduce, entirely analogous to equation (23), an expansion of $U_{1\ldots\ell}$ in terms of coefficients $u_\ell^a$,

$$
U_{1 \ldots \ell}=2^{-\ell} \sum_{n=0}^{\ell} \sum_{a \in \mathcal{I}^{n}} u_{n}^{a} \sum_{p \in \mathfrak{P}_{n}(\ell)} \sigma_{p}^{a}.\qquad(41)
$$

Writing the BBGKY hierarchy in the interaction picture (35) in terms of these expansion coefficients, we obtain

$$
\partial_{\tau} u_{\ell}^{\prime}=\lambda^{1-r-s} \tilde{v}_{\ell-}\left(u_{\ell-1}^{\prime}, \tau\right)+\lambda^{s-r}(1-\ell \lambda) \tilde{v}_{\ell+}\left(u_{\ell+1}^{\prime}, \tau\right).\qquad(42)
$$

where $u_\ell = u_\ell'\lambda^{s\ell}$. The $\tilde{v}_{\ell\pm}(u_{\ell\pm1}',\tau)$ terms are obtained from the corresponding $v_{\ell\pm}$ terms in (30b) and (30c) by replacing $J$ with

$$
\tilde{J}(\tau)=B\left(\lambda^{-1 / 2} h \tau / 2\right)^{T} J B\left(\lambda^{-1 / 2} h \tau / 2\right)\qquad(43)
$$

as defined in (39). Inspection of (42) suggests that the leading-order $\lambda$-dependent factors can be scaled to unity§ by choosing $1-r-s=0$ and $s-r=0$. The solution $r=s=1/2$ determines the scaling exponents in (32a) and (32b),

$$
t=\hbar \tau \lambda^{-1 / 2} / 2,\qquad(44a)
$$

$$
f_{\ell}=f_{\ell}^{\prime} \lambda^{\ell / 2},\qquad(44b)
$$

and the BBGKY hierarchy simplifies to

$$
\partial_{\tau} u_{\ell}^{\prime}=\tilde{v}_{\ell-}\left(u_{\ell-1}^{\prime}, \tau\right)+(1-\ell \lambda) \tilde{v}_{\ell+}\left(u_{\ell+1}^{\prime}, \tau\right).\qquad(45)
$$

The frequency of the modulation of $\tilde{J}(\tau)$ in (43) has a singular $\lambda \to 0$ limit, which is a hallmark of the fundamentally different time scales involved: The fixed time scale of the single-spin interaction, contained in the term $v_{\ell 0}(f)$ in (29) in the $(t,N)$-plane, appears as a variable frequency oscillation with a singular $\lambda=0$ limit in the parameter space $(\tau,\lambda)$. Since this frequency diverges on the $\tau$-time scale we are interested in, it is reasonable to eliminate the high-frequency oscillations by applying an averaging procedure to equation (45). To this purpose, we apply on both sides of (45) the finite-time averaging operator

$$
\frac{1}{T} \int_{\tau}^{\tau+T} d \tau^{\prime},\qquad(46)
$$

where $T=\pi \sqrt{\lambda} /|h|$ is the period of $\tilde{J}(\tau)$. For small $\lambda$, $u_\ell$ is slowly varying over a period $T$, and by making use of the definitions (30b) and (30c) we can write

$$
\begin{aligned}
\frac{u_{\ell}^{\prime a}(\tau+T)-u_{\ell}^{\prime a}(\tau)}{T} \approx & -\sum_{b, c \in \mathcal{I}} \sum_{\substack{i, j=1 \\
i \neq j}}^{\ell} \varepsilon^{a_{i} b c} \bar{J}^{b a_{j}} u_{\ell-1}^{\prime a-a_{i}+c-a_{j}}(\tau) \\
& -(1-\ell \lambda) \sum_{b, c, d \in \mathcal{I}} \bar{J}^{b d} \sum_{i=1}^{\ell} \varepsilon^{a_{i} b c} u_{\ell+1}^{\prime a-a_{i}+c+d}(\tau),
\end{aligned}\qquad(47)
$$

§ This argument is based on the assumption that $\tilde{v}_\ell^-$ and $\tilde{v}_\ell^+$ are of order unity in $\lambda$. It will be made explicit for the special case discussed in section 6.

where the averaged coupling matrix is defined as

$$
\bar{J}=\frac{1}{T} \int_{0}^{T} B(\theta)^{T} J B(\theta) \mathrm{d} \theta.
\tag{48}
$$

Performing the limit $\lambda \to 0$ (which implies $T \to 0$), we obtain the averaged BBGKY equations

$$
\partial_{\tau} u_{\ell}^{\prime}=\bar{v}_{\ell-}\left(u_{\ell-1}^{\prime}\right)+\bar{v}_{\ell+}\left(u_{\ell+1}^{\prime}\right),
\tag{49}
$$

where $\bar{v}_{\ell \pm}$ is obtained from the corresponding $v_{\ell \pm}$ by replacing $J$ with $\bar{J}$.

Comparing the original (non-averaged) equations (33) with the averaged ones in (49), the outcome of the averaging procedure can be summarized as follows:

(i) The presence of a single-spin potential $H_i$ in the Hamiltonian leads to a fast oscillating term.

(ii) Going to the interaction picture and averaging-out the fast oscillations, the averaged BBGKY hierarchy (49) is formally identical to the original one (33) in the absence of a single-spin potential, but with the original coupling matrix $J$ replaced by the averaged one $\bar{J}$ defined in (48).

(iii) For the investigation of the long-time dynamics in the thermodynamic limit it is therefore sufficient to study the Hamiltonian (2) in the absence of a single-spin potential $H_i$, thereby avoiding the problem of fast oscillations in the rescaled BBGKY hierarchy (33).

(iv) Our scaling ansatz (32a) and (32b) suggests to define the thermodynamic limit as $1/N = \lambda \to 0$ at fixed rescaled time $\tau$, and this suggestion will be further investigated in section 6. This limit corresponds to a non-trivial path to infinity in the $(t, N)$ plane.

Taking for example the special case discussed in section 3.1, $J = \mathrm{diag}(J^x, J^y, J^z)$ and $h=(0,0,h^z)$, it is straightforward to calculate the averaged coupling matrix

$$
\bar{J}=\operatorname{diag}\left(\left(J^{x}+J^{y}\right) / 2,\left(J^{x}+J^{y}\right) / 2, J^{z}\right).
\tag{50}
$$

The above results then assert that, on the $\tau$-time scale defined in (44a), equilibration of a system with coupling $\bar{J}$ and zero magnetic field will look identical to that of a system with the original couplings and a non-zero field in $z$-direction. For the special case studied in section 6 where an exact solution (without averaging) is feasible, these considerations will be nicely confirmed and illustrated.

As a consequence of the elimination of the fast oscillations, the averaged time evolution equations (49) are much more suitable for numerical computations, yielding more stable results. Comparing the results with and without averaging, we observe that the reduced one-spin density operator retains positivity over the period of time shown in figure 2. Moreover, the solution appears periodic, which is in agreement with the analytic prediction for the special case investigated in section 6.

## 6. Case study

In this section we derive, for the choice of parameters

$$
J=\operatorname{diag}\left(J^{\perp}, J^{\perp}, J^{z}\right), \quad h=\left(0,0, h^{z}\right),
\tag{51}
$$


the time-evolution of certain coefficients $f_\ell$ in the BBGKY hierarchy (33). This is achieved for correlation closures of arbitrary order, and also for the full (untruncated) hierarchy. As for initial conditions, we set
$$
\left(f_{1}^{x}, f_{1}^{y}, f_{1}^{z}\right)(0)=\left(s^{x}, s^{y}, s^{z}\right), \quad |s| \leqslant 1. \tag{52}
$$

The parameters (51) and the initial conditions (52) are more general than the ones used in the Emch-Radin model (where $J^{\perp}=0$ and the initial density operator is diagonal in the $\sigma^{x}$ eigenbasis, implying $f_{1}^{y}=f_{1}^{z}=0$ ). For the higher order coefficients we require
$$
f_{\ell}^{a}(0)=s_{\ell}^{a}=0 \quad \forall \ell>1. \tag{53}
$$

A study of more general initial conditions and parameters will be presented elsewhere. The results we will obtain in this section are found to be in agreement with the known exact solution of the Emch-Radin model. This can be seen as an a posteriori justification of the scaling assumptions (44a)-(44b) and of the limiting procedure proposed in section 5. Apart from this reassuring result, the derivation is interesting to follow as it resorts to a number of beautiful mathematical concepts, including recurrence relations, continued fractions, and orthogonal polynomials.

### 6.1. Finite system size
Unless stated otherwise, we will drop from now on the prime in the rescaled coefficients (32b), writing $f$ instead of $f'$. We start by analyzing the hierarchy (33), and the terms $v_{\ell 0}$ and $v_{\ell \pm}$ contained therein, for the above parameter values and initial conditions (51)-(53). In the following, whenever convenient, we will label the coefficients $f_{\ell}^{m}$ by a triple $m=(m_{x}, m_{y}, m_{z})$ as introduced in section 4.1. Considering $m=(0,0, \ell)$, we find $v_{\ell 0}=0$ and
$$
\partial_{\tau} f_{\ell}^{(0,0, \ell)}=\ell\left(J^{\perp}-J^{\perp}\right) f_{\ell+1}^{(1,1, \ell-1)}=0, \tag{54}
$$
from which we can conclude that
$$
f_{\ell}^{(0,0, \ell)}(\tau)=f_{\ell}^{(0,0, \ell)}(0)=s^{(0,0, \ell)} \tag{55}
$$
for all $\ell$. In particular, for $\ell=1$ we have
$$
f_{1}^{z}(\tau)=f_{1}^{z}(0)=s^{z}. \tag{56}
$$

From (55), we also note that the initial conditions (53) may be generalized to nonzero $s^{(0,0, \ell)}$ at no additional expense. Next we discuss the time evolution of coefficients $f_{\ell}^{m}$ for two families of superscript indices, $m=(1,0, \ell-1)$ and $m=(0,1, \ell-1)$,
$$
\partial_{\tau} f_{\ell}^{(1,0, \ell-1)}=\lambda^{-1 / 2} h^{z} f_{\ell}^{(0,1, \ell-1)}-(\ell-1) K f_{\ell-1}^{(0,1, \ell-2)}-(1-\lambda \ell) K f_{\ell+1}^{(0,1, \ell)}, \tag{57a}
$$
$$
\partial_{\tau} f_{\ell}^{(0,1, \ell-1)}=-\lambda^{-1 / 2} h^{z} f_{\ell}^{(1,0, \ell-1)}+(\ell-1) K f_{\ell-1}^{(1,0, \ell-2)}+(1-\lambda \ell) K f_{\ell+1}^{(1,0, \ell)}, \tag{57b}
$$
where $K=J^{z}-J^{\perp}$. The regularity behind this set of differential equations can be captured with the help of a few definitions. Define the sequences of component labels
$$
\mathfrak{a}^{x}=(x, y z, x z z, y z z z, x z z z z, \ldots), \tag{58a}
$$
$$
\mathfrak{a}^{y}=(y, x z, y z z, x z z z, y z z z z, \ldots), \tag{58b}
$$
and denote by $\mathfrak{a}_{n}^{x}$ and $\mathfrak{a}_{n}^{y}$ the $n$th element of the corresponding sequence, $1 \leqslant n \leqslant N$. Furthermore, define a sequence of complex functions
$$
u_{n}(\tau)=\mathrm{e}^{\mathrm{i} \lambda^{-1 / 2} h^{z} \tau}\left[(-1)^{\lfloor n / 2\rfloor} f_{n}^{\mathfrak{a}_{n}^{x}}(\tau)+\mathrm{i}(-1)^{\lfloor(n-1) / 2\rfloor} f_{n}^{\mathfrak{a}_{n}^{y}}(\tau)\right], \tag{59}
$$

where $\lfloor n/2 \rfloor$ denotes the integral part of $n/2$. With these definitions, the BBGKY equations (57a) and (57b) can be expressed in terms of the functions $u_n$,
$$
\partial_{\tau} u_n=K(n-1) u_{n-1}-K(1-n \lambda) u_{n+1}, \quad 1 \leqslant n \leqslant N. \tag{60}
$$

This equation may be further simplified by another scaling of time $\tau'=\tau / K$, yielding
$$
\partial_{\tau} u_n=(n-1) u_{n-1}-(1-n \lambda) u_{n+1}, \quad 1 \leqslant n \leqslant N, \tag{61}
$$
where we have dropped the prime from $\tau'$ for the sake of a simpler notation. Translating the initial conditions (52) and (53) to our new variables, we obtain
$$
u(0)=\left(s^x+\mathrm{i} s^y, 0, \ldots, 0\right). \tag{62}
$$

Inspecting equation (59), we observe that indeed the singular term $\lambda^{-1 / 2} v_{\ell 0}$ in (33) results in a high-frequency oscillation superimposed on the much slower dynamics induced by the spin-spin interactions. Incorporating this oscillation into the definition of $u$ corresponds to a change of variables to the co-moving frame, i.e. to the interaction picture defined in section 5. Furthermore, (59) justifies the assumption, mentioned in a footnote in section 5, that $\tilde{v}_{\ell-}$ and $\tilde{v}_{\ell+}$ are of order unity in $\lambda$. This gives support to the reasoning behind the choice of the exponents $r$ and $s$ in the scaling ansatz (32a)-(32b). However, it also implies that, on the $\tau$-time scale, no truncation of the BBGKY hierarchy can be justified by the smallness of the parameter $\lambda$.

Finally, the particular choices of parameter values (51) and initial conditions (52) and (53) led to a simplification of the BBGKY hierarchy. The simplification becomes even more pronounced if one focusses, as we did in the preceding paragraph, onto a certain subset of the coefficients $f_{\ell}^a$ in the expansion (23). For example, in order to compute expectation values of single-particle observables, it is sufficient to determine the time-evolution of $f_1^x$, $f_1^y$, and $f_1^z$. From (61), we can read off that $f_1^x+\mathrm{i} f_1^y$ is determined as a solution of $N$ equations with $N$ independent variables, which is a tiny fraction of the total number of degrees of freedom $D(N)$ of the full BBGKY hierarchy $[D(N) \sim N^3 / 6$ as given by (26)]. It is important to note that this reduction of complexity is obtained without truncation of the hierarchy, but is a consequence of the decoupling of certain subsets of the expansion coefficients introduced in (23).

The initial value problem specified by (61) and (62) can be solved in Laplace space. The Laplace transform of a function $u$ of a real variable $\tau$ is a complex function $\hat{u}$ of a complex variable $z$, defined by
$$
\hat{u}(z)=\mathscr{L}[f] \equiv \int_0^{\infty} u(\tau) \mathrm{e}^{-z \tau} \mathrm{d} \tau. \tag{63}
$$

The inverse of the Laplace transform is defined as
$$
u(\tau)=\mathscr{L}^{-1}[\hat{u}] \equiv \frac{1}{2 \pi \mathrm{i}} \int_{\gamma} \hat{u}(z) \mathrm{e}^{z \tau} \mathrm{d} z, \tag{64}
$$
where $\gamma$ denotes the so-called Bromwich contour in the complex $z$ plane, which runs from $-\mathrm{i} \infty$ to $+\mathrm{i} \infty$ and stays to the right of all of the poles of $\hat{u}(z)$. The Laplace transformation of a derivative is
$$
\mathscr{L}\left[\partial_{\tau} u(\tau)\right]=z \hat{u}(z)-u(0). \tag{65}
$$

By virtue of this rule, we can write (61) in Laplace space,
$$
z \hat{u}_n(z)=u_n(0)+(n-1) \hat{u}_{n-1}(z)-(1-n \lambda) \hat{u}_{n+1}(z). \tag{66}
$$

From equation (66) with $n=1$ we obtain||
$$
u_{1}(0) / \hat{u}_{1}(z)=z+(1-\lambda)\left[\hat{u}_{2}(z) / \hat{u}_{1}(z)\right],\qquad(67)
$$
and for $n>1$ it can be rearranged to
$$
z=(n-1)\left[\hat{u}_{n-1}(z) / \hat{u}_{n}(z)-(1-n \lambda)\left[\hat{u}_{n+1}(z) / \hat{u}_{n}(z)\right].\right.\qquad(68)
$$

We can then write the ratio of subsequent $\hat{u}_{n}$ as
$$
\frac{\hat{u}_{n}(z)}{\hat{u}_{n-1}(z)}=\frac{n-1}{z+(1-n \lambda)\left[\hat{u}_{n+1}(z) / \hat{u}_{n}(z)\right]}.\qquad(69)
$$

Applying this expression iteratively, we arrive at
$$
\hat{u}_{1}(z)=\left(s^{x}+\mathrm{i} s^{y}\right) \frac{1}{z+} \frac{\beta_{1}}{z+} \cdots \frac{\beta_{N-1}}{z}\qquad(70)
$$
with
$$
\beta_{n}=n(1-n \lambda), \quad 1 \leqslant n \leqslant N,\qquad(71)
$$
where
$$
\frac{a_{1}}{b_{1}+} \frac{a_{2}}{b_{2}+} \cdots \equiv \frac{a_{1}}{b_{1}+\frac{a_{2}}{b_{2}+\cdots}}\qquad(72)
$$
is a standard notation for continued fractions.

From $\hat{u}_{1}$, the coefficients $\hat{u}_{n}$ with $n>1$ are obtained via the equation (66). For a finite number $N=1 / \lambda$ of spins, the solution (70) contains a finite number of terms, terminating at $\beta_{N}=N(1-N \lambda)=0$. Hence we can write
$$
\hat{u}_{1}(z)=\left(s^{x}+\mathrm{i} s^{y}\right) \frac{A_{N}(z)}{B_{N}(z)},\qquad(73)
$$
where $A_{N}(z)$ and $B_{N}(z)$ are polynomials in $z$ of degree $N-1$ and $N$, respectively.

From $\hat{u}_{1}$ we reconstruct the coefficients $f_{1}^{x}$ and $f_{1}^{y}$ in the time domain via the inverse Laplace transform (64),
$$
f_{1}^{x}(\tau)+\mathrm{i} f_{1}^{y}(\tau)=\mathrm{e}^{-\mathrm{i} \lambda^{-1 / 2} h^{z} \tau} \mathscr{L}^{-1}\left[\hat{u}_{1}(z)\right](\tau).\qquad(74)
$$

Properties of (74) depend crucially on the properties of $\mathscr{L}^{-1}[\hat{u}_{1}(z)]$, and therefore on the structure of the singularities of $\hat{u}_{1}(z)$. Owing to the form of the expression (73), these singularities are poles, originating from the zeros of $B_{N}(z)$. We shall study these zeros in the following and discuss the effect of correlation closures of various orders $\ell$ on the solutions. For this purpose, consider what is called the $\ell$th convergent of the continued fraction (70),
$$
\hat{u}_{1}^{(\ell)}(z)=\left(s^{x}+\mathrm{i} s^{y}\right) \frac{1}{z+} \frac{\beta_{1}}{z+} \cdots \frac{\beta_{\ell-1}}{z},\qquad(75)
$$
defined as the truncation of (70) after $\ell$ terms. The same $\hat{u}_{1}^{(\ell)}$ could also be obtained as a solution of a truncated version of the recurrence relation (66) where $\hat{u}_{\ell+k}=0$ for all $1 \leqslant k \leqslant N-\ell$. For this reason, the convergent (75) is closely related to the $\ell$th order correlation closure of the BBGKY hierarchy, as given by (28a)-(28c) with $g_{\ell+k}=0$. This can be seen by applying the correlation closure condition to the coefficients $f_{\ell+1}^{\mathfrak{a}^{x}}$, $f_{\ell+1}^{\mathfrak{a}^{y}}$ with component indices from the sets (58a) or (58b): Because of the $(n-1)$-fold

|| We disregard the problem of zero denominators in the following, as it can be circumvented and does not cause serious problems.

occurrence of $z$-indices in the elements $\mathfrak{a}_{n}^{x}$ and $\mathfrak{a}_{n}^{y}$, the cluster expansions (28a)-(28c)
are particularly simple. The coefficient $f_{4}^{\mathfrak{a}_{4}^{y}}$ for example can be written as

$$
f_{4}^{\mathfrak{a}_{4}^{y}}=f_{4}^{x z z z}=f_{1}^{x}\left[f_{3}^{z z z}-6 f_{1}^{z} f_{2}^{z z}+6\left(f_{1}^{z}\right)^{3}\right]+3 f_{2}^{x z}\left[f_{2}^{z z}-2\left(f_{1}^{z}\right)^{2}\right]+3 f_{3}^{x z z} f_{1}^{z}+g_{4}^{x z z z}.(76)
$$

In third order correlation closure, i.e. setting $g_{4}^{x z z z}=0$, the right-hand side of (76)
consists of only two kinds of coefficients $f_{n}^{a}$: either with $a \in \mathfrak{a}^{x} \cup \mathfrak{a}^{y}$, or with $a=z \ldots z$.
The latter ones, as we have shown in (55), do not vary in time, and $f_{4}^{x z z z}$ is therefore
linear in the time-dependent coefficients $f_{n}^{\mathfrak{a}^{x}}, f_{n}^{\mathfrak{a}^{y}}$. Translating this observation via
definition (59) into the interaction picture, we find the closure condition

$$
u_{4}(\tau)=\sum_{n=1}^{3} c_{n} u_{n}(\tau),\qquad(77)
$$

where the $c_{n}$ are determined by the time-independent coefficients $f_{k}^{m}$ with $m=$
$(0,0, k)$. The same kind of pattern emerges also for correlation closures of arbitrary
order $\ell$, where

$$
u_{\ell+1}(\tau)=\sum_{n=1}^{\ell} c_{n} u_{n}(\tau)\qquad(78)
$$

is again linear in the time-dependent coefficients $u_{n}(\tau)$. In the special case of initial
conditions $s^{(0,0, k)}=f^{(0,0, k)}=0$, we have $c_{n}=0$ and the $\ell$ th order correlation closure
is equivalent to setting $u_{n}=0$ for $n>\ell$. This condition translates into the condition
$\hat{u}_{\ell+k}=0$ for the coefficients in Laplace space, and (75) is therefore the solution of
the $\ell$ th order correlation closure for initial conditions given by (53). In case of more
general initial conditions with $s^{(0,0, k)} \neq 0$, the correlation closure amounts to a linear
relation between $u_{\ell+1}$ and all the lower order coefficients.

Having understood the relation between correlation closures (16) and convergents
(75), we proceed with the analysis of the latter. Similar to the full continued fraction
in (73), also the convergent can be written as a ratio of polynomials $A_{\ell}$ and $B_{\ell}$ of
degrees $\ell-1$, respectively $\ell$,

$$
\hat{u}_{1}^{(\ell)}(z)=\left(s^{x}+\mathrm{i} s^{y}\right) \frac{A_{\ell}(z)}{B_{\ell}(z)}.\qquad(79)
$$

From (75), Wallis-type [22] second-order recursion relations for $B_{n}$ and $A_{n}$ can be
derived,

$$
\begin{aligned}
& z A_{n}(z)=\beta_{n} A_{n-1}(z)-A_{n+1}(z), \quad(80 a) \\
& z B_{n}(z)=\beta_{n} B_{n-1}(z)-B_{n+1}(z), \quad(80 b)
\end{aligned}
$$

where $\beta_{n}$ is defined as in (71). Although of the same form, the two recursion relations
(80a) and (80b) have different initial conditions, $B_{-1}=0, B_{0}=1$, and $A_{0}=0$,
$A_{1}=-1$. Anticipating that the zeros of $B_{n}$ and $A_{n}$ are imaginary, we make a
coordinate transformation $x=-\mathrm{i} z$ that brings $A_{n}$ and $B_{n}$ into the conventional real
form. In these new variables, the convergent can be written as

$$
\hat{u}_{1}^{(\ell)}(\mathrm{i} x)=-\mathrm{i}\left(s^{x}+\mathrm{i} s^{y}\right) \frac{p_{\ell-1}^{(1)}(x)}{p_{\ell}^{(0)}(x)},\qquad(81)
$$

with polynomials

$$
p_{n}^{(1)}(x)=-\mathrm{i}^{n} A_{n+1}(\mathrm{i} x), \quad p_{n}^{(0)}(x)=\mathrm{i}^{n} B_{n}(\mathrm{i} x).\qquad(82)
$$

Equilibration in long-range quantum spin systems from a BBGKY perspective
19

From (80a) and (80b), recursion relations for the new polynomials are obtained,
$$
x p_{n}^{(j)}(x)=\beta_{n+j} p_{n-1}^{(j)}(x)+p_{n+1}^{(j)}(x), \quad j=0,1,\qquad(83)
$$
with initial conditions $p_{-1}^{(j)}=0$ and $p_{0}^{(j)}=1$. It follows from Favard's theorem [22] that the sequences of polynomials $\{p_{n}^{(j)}\}_{n=0}^{N-j}$ generated by (83) are positive definite and orthogonal, in the sense that there exists a nonnegative weight function $w_{N}^{(j)}(x)$ such that, for any $0 \leqslant n<m \leqslant N-j$,
$$
\int_{-\infty}^{\infty} p_{n}^{(j)}(x) p_{m}^{(j)}(x) w_{N}^{(j)}(x) \mathrm{d} x=0.\qquad(84)
$$

It follows from the positive definiteness and orthogonality of the $p_{n}^{(j)}$ that all $\ell$ zeros $x_{\ell k}^{j}$ of $p_{\ell}^{(j)}(x)$ are real, simple, and isolated. Most importantly, the following decomposition formula holds,
$$
\frac{p_{\ell-1}^{(1)}(x)}{p_{\ell}^{(0)}(x)}=\sum_{k=1}^{\ell} \frac{a_{\ell k}}{x-x_{\ell k}}, \quad a_{\ell k}=\frac{p_{\ell-1}^{(1)}\left(x_{\ell k}\right)}{p_{\ell}^{\prime(0)}\left(x_{\ell k}\right)},\qquad(85)
$$
where the prime denotes a derivative.

Equation (85) can be used to perform the integral in the inverse Laplace transform (64). Since we have to undo the coordinate transform $z=\mathrm{i} x$, the Bromwich integration contour $\gamma$ in the complex $z$-plane has to be modified to $\gamma^{\prime}$ in the complex $x$-plane, running parallel to the real axis and below all the zeros of $p_{\ell}^{(0)}(x)$, i.e. below the real axis. The exponential $\mathrm{e}^{\mathrm{i} x \tau}$ in (64) introduces a damping factor if $\Im x>0$, and the integration path $\gamma^{\prime}$ can therefore be closed in the upper half plane by a path $\gamma^{\prime}$ without changing the value of the integral. As a result, the path encloses all $\ell$ zeros of $p_{\ell}^{(0)}(x)$ and we can apply the residue theorem,
$$
\begin{aligned}
u_{1}^{(\ell)}(\tau) & =\frac{-\mathrm{i}\left(s^{x}+\mathrm{i} s^{y}\right)}{2 \pi} \int_{\gamma^{\prime}} \frac{p_{\ell-1}^{(1)}(x) e^{\mathrm{i} x \tau}}{p_{\ell}^{(0)}(x)} \mathrm{d} x \\
& =\left(s^{x}+\mathrm{i} s^{y}\right) \sum_{j=1}^{\ell} \operatorname{Res}_{x=x_{\ell j}}\left(\frac{p_{\ell-1}^{(1)}(x)}{p_{\ell}^{(0)}(x)}\right) \mathrm{e}^{\mathrm{i} x_{\ell j} \tau} \\
& =\left(s^{x}+\mathrm{i} s^{y}\right) \sum_{j=1}^{\ell} a_{\ell j} \mathrm{e}^{\mathrm{i} x_{\ell j} \tau}.
\end{aligned}\qquad(86)
$$

By inspection of (83), it is not too difficult to observe that the polynomials generated by this recursion relation are alternatingly odd and even functions. Their zeros are therefore distributed symmetrically around the origin. Sorting the zeros in increasing order, (86) can be simplified to
$$
u_{1}^{(\ell)}(\tau)=2\left(s^{x}+\mathrm{i} s^{y}\right) \sum_{j=1}^{\ell / 2} a_{\ell j} \cos \left(x_{\ell j} \tau\right),\qquad(87)
$$
where we have assumed that $\ell$ is even. (If $\ell$ is odd, a constant term must be added to the sum.)

Equation (87) is the main result of this section. Since it consists of a finite sum of oscillatory terms, the solution $u_{1}^{(\ell)}(\tau)$ is either periodic or quasi-periodic in time.

![](./images/867752764254453911_3.jpg)

Figure 3. For parameter values $h=0$, $J=\mathrm{diag}(0,0,1)$, and $N=1/\lambda=10$, the real part $\Re(u_{1}^{(\ell)})=f_{1}^{x}$ is plotted as a function of rescaled time $\tau$ for various orders $\ell=2,3,4,5,9$ of the correlation closure. Recurrent behavior is evident from the plot, both for the full solution and for the truncations of various orders.

For example, by setting $\lambda=0$ in the polynomials $p_{\ell-j}^{(j)}$ with $\ell=2,3,4$, we find
$$
u_{1}^{(2)}(\tau)=\left(s^{x}+\mathrm{i} s^{y}\right) \cos \tau,\qquad(88a)
$$
$$
u_{1}^{(3)}(\tau)=\frac{\left(s^{x}+\mathrm{i} s^{y}\right)}{3}\left[2+\cos \left(\sqrt{3 / 2} \tau\right)\right],\qquad(88b)
$$
$$
\begin{aligned}
u_{1}^{(4)}(\tau)=\frac{\left(s^{x}+\mathrm{i} s^{y}\right)}{2 \sqrt{6}} & {\left[(\sqrt{6}+2) \cos \left(\sqrt{3-\sqrt{6}} \tau\right)\right.} \\
+ & \left.(\sqrt{6}-2) \cos \left(\sqrt{3+\sqrt{6}} \tau\right)\right].
\end{aligned}\qquad(88c)
$$

The behavior of the solutions in (87) is illustrated in figure 3 for various orders $\ell$ of the truncation of the continued fraction (75). Initial conditions satisfying $s^{z}=0$ were chosen, and therefore the truncations correspond to $\ell$th order correlation closures. The recurrences, or Loschmidt echos, of the solutions, expected from the result in (87), are evident in the plots, both for the full solution for $N=10$ spins as well as for the truncations at orders $\ell<N$.

### 6.2. Thermodynamic limit
Having observed that, for any finite system size and/or finite order correlation closure, the dynamics is periodic or quasi-periodic, we next want to investigate the effect of the thermodynamic limit $\lambda \to 0$. The reader is reminded that this limit, due to the $\lambda$-scaling of time (32a), corresponds to simultaneously taking long-time and large-system limits along a nontrivial path in the $(t, N)$ plane. For the special case studied in this section 6, this limit can be performed within the framework developed in section 6.1 by studying $p_{N-1}^{(1)} / p_{N}^{(0)}$ in the limit $\lambda \to 0$. Here, however, we prefer to take a shortcut and investigate the $\lambda=0$ case directly in the time domain. Indeed, setting $\lambda=0$ in (61), we obtain
$$
u_{n+1}(\tau, 0)=(n-1) u_{n-1}(\tau, 0)-\partial_{\tau} u_{n}(\tau, 0),\qquad(89)
$$
which is solved by
$$
u_{n}(\tau, 0)=\left(s^{x}+\mathrm{i} s^{y}\right) \tau^{n-1} \mathrm{e}^{-\tau^{2} / 2}.\qquad(90)
$$

Translating this result to the original coefficients $f_{n}^{a^{x}}$ by (59), we encounter a term $\mathrm{e}^{-\mathrm{i} \lambda^{-1 / 2} h^{z} \tau}$, oscillating at infinite frequency in the $\lambda \to 0$ limit. This oscillation is irrelevant for the relaxation to equilibrium, as it happens on a fundamentally different timescale. Therefore we will disregard this oscillating term, obtaining

$$
f_{1}^{x}(\tau, 0)+\mathrm{i} f_{1}^{y}(\tau, 0)=\left(s^{x}+\mathrm{i} s^{y}\right) \mathrm{e}^{-\tau^{2} / 2}
\tag{91}
$$

for $n=1$.

The solutions (90) or (91) display Gaussian (superexponential) relaxation as a function of rescaled time $\tau$, and no recurrent behavior is observed. This is in stark contrast to the periodic or quasi-periodic dynamics (88a) we found, as illustrated in figure 3, for finite system sizes. Moreover, the result in (91) is in exact agreement with the $N \to \infty$ limit of the Emch-Radin model with exponent $\alpha=0$ as reported in equation (32) of [11].

### 7. Discussion of the results

The special case treated in section 6 illustrates and confirms some of the aspects that have been discussed in sections 3.1 and 5 in greater generality, and it also can substantiate some of assumptions made. In particular, we would like to discuss the following aspects.

#### 7.1. Symmetry-induced causal relations

We have seen that, for the special case of section 6, not all of the expansion coefficients $u_{\ell}^{a}$ (or $f_{\ell}^{a}$) influence the time evolution of each other. Instead, we observed that the time evolution of, say, $f_{1}^{x}$ is affected by only a small subset of the other coefficients. This decoupling, which is a property of the structure of BBGKY hierarchy of equations, is particularly pronounced in the case discussed in section 6 but, as will be shown in a forthcoming paper [23], similar (but more involved) relations hold true for general parameter values of the model.

#### 7.2. Shortcomings of the correlation closure

For the special values of parameters and initial conditions of section 6, we found that, for any $\ell \geqslant 1$, the correlation closure of order $\ell$ [as defined in (16)] gives rise to periodic or quasi-periodic behavior. There are, of course, many other types of closures of the BBGKY hierarchy one might consider, and the question is whether others might be more suitable for studying the relaxation to equilibrium we are interested in.

One way to improve on the correlation closure might consist in taking into consideration the symmetries imposed by the BBGKY hierarchy as mentioned in section 7.1. Since symmetries are respected by the exact dynamics, one may hope that a closure which takes into account this structure might be superior to the one that does not. Preliminary numerical studies of ours seem to be in favor of this conjecture. However, it is clear from these results that for our main objective, i.e. the study of relaxation to equilibrium, such a modified closure does at best lead to marginal improvements and we will hence not pursue this aspect further in the present article.

A kinetic theory appropriate for studying relaxation to equilibrium is expected to require a more complicated closure relation in the form of a collision integral. Such a theory will be developed in a forthcoming paper.

Equilibration in long-range quantum spin systems from a BBGKY perspective
22

### 7.3. Thermodynamic limit and the definition of rescaled time $\tau$

A crucial step for obtaining a nontrivial long-time asymptotics was the definition of a suitable kind of thermodynamic limit as elaborated on in section 5. This limit reflects in the choice of the exponent $r$ when defining the rescaled time variable $\tau$ in (32a) ¶. In the general considerations in section 5, the choice $r=1/2$ was based on the scaling properties in $\lambda$ of the BBGKY hierarchy (42) in the coefficient expansion. With this choice, and for the special case of section 6, we were able to derive, in (91), the exact Gaussian relaxation to equilibrium, which gives support not only to the choice $r=1/2$, but also to the guiding principle based on the scaling properties of (42).

## 8. Conclusions

We have studied, via a BBGKY-type approach, the time evolution of $\ell$-spin reduced density operators $F_{1\ldots\ell}$ for Heisenberg-type quantum spin models with Curie Weiss-type long-range interactions. Our analysis is based on a particular expansion of $F_{1\ldots\ell}$ in terms of coefficients $f_{\ell}^{a}$, as introduced in (23), which casts the BBGKY hierarchy into the form of a second-order recursion (29).

Originally our study was motivated by the observation of quasi-stationary behavior in the long-range Emch-Radin model, i.e. the fact that relaxation to equilibrium takes place on a time scale which diverges with the system size. As a consequence of this diverging time scale, for studying the long-time asymptotics of quantum spin models in the thermodynamic limit it is therefore necessary to consider a suitably defined thermodynamic limit where, with increasing system size $N$, time is scaled appropriately such that nontrivial dynamics can be observed. Remarkably, the structure of the BBGKY hierarchy (42) when expressed in terms of the expansion coefficients $f_{\ell}^{a}$ suggests a definition of rescaled time $\tau=2t\lambda^{r}/\hbar$ which, as turns out, leads to a nontrivial exact result and reproduces the Gaussian relaxation (90) of the Emch-Radin model.

When dealing with the BBGKY hierarchy (42) in rescaled time, we noticed that the on-site potential (or single-spin potential) $H_{i}$ in the Hamiltonian (2) gives rise to an oscillating term whose frequency diverges on the $\tau$-time scale in the thermodynamic limit. Since this time scale of oscillation is strongly (infinitely) separated from the time scale of relaxation to equilibrium, an averaging procedure is introduced to eliminate the high-frequency dynamics. The averaged BBGKY hierarchy (49) leads to a well-defined $\lambda\rightarrow0$ limit of the hierarchy, but also to a significant improvement of numerical results as shown in figure 2.

A general BBGKY hierarchy cannot be solved exactly, as this would correspond to an exact solution of the full $N$-spin problem. The problem becomes more tractable by truncating the hierarchy. The resulting set of equations is ill-defined, but it can be turned into a well-defined one by postulating a closure condition. For the long-range spin models discussed in the present work, we have defined what we call the correlation closure of $\ell$th order in (16), and the effect of these closures on the long-time dynamics has been discussed. For the special parameter values and initial conditions considered in section 6, we have shown analytically that closing the BBGKY hierarchy by neglecting $\ell$-spin correlations does never lead to equilibration, but gives rise to quasi-periodic time evolution with at most $\ell/2$ independent frequencies, as is

¶ Without rescaling of time, the time evolution of the variables $u_{\ell}$ in the interaction picture would just be constant in the thermodynamic limit, with no sign of relaxation to equilibrium [11].

evident from (87). We must therefore conclude that, in order to construct a kinetic theory appropriate for studying relaxation to equilibrium, a more complicated closure relation, presumably in the form of a collision integral, will be needed. Once such a theory is properly benchmarked against the exact results available for the Emch- Radin model, it should allow us to study the approach to equilibrium in non-integrable generalizations of the Emch-Radin model, or non-integrable long-range variants of the Heisenberg model for which exact solutions do not exist.

In addition to providing a tool for investigating the dynamics of quantum spin models, our results also shed light on more general features regarding the role of closure conditions when truncating the BBGKY hierarchy: The particularly simple structure of spin-1/2 lattice models facilitates analytic calculations beyond what can be achieved in continuum systems, and an understanding of the effect of approximation schemes is easier to attain. We tend to believe that, at least on a qualitative level, several of our observations apply not only to spin-1/2 systems, but should hold more generally for closed quantum systems on finite-dimensional Hilbert spaces.

We want to conclude with a comment on an interesting related work by Sciolla and Biroli [24] which also deals with the dynamics of Curie-Weiss-type (or completely connected) quantum systems, i.e. with Hamiltonians of type (2), but with arbitrary $H_i$ and $V_{ij}$. Their analysis yields exact analytical results in the thermodynamic limit for a much larger class of Hamiltonians, but is more restrictive with respect to initial conditions, allowing only wave packets whose width shrinks to zero in the thermodynamic limit. Moreover, their analysis is bound to fail on the rescaled time scales $\tau$ studied in the present work, and is therefore unsuitable for investigating thermalization. In a future work we will study thermalization in rescaled time for more general models by approximative methods, and the results by Sciolla and Biroli should prove useful for benchmarking the short-time dynamical behavior.

## Appendix A. Derivation of equation (29)

In the course of the proof, we will refer to the following elementary identities for Pauli operators on lattice sites $i=1,2$.

$$
\left[\sigma_{i}^{a}, \sigma_{i}^{b}\right] \quad=2 \mathrm{i} \sum_{c} \varepsilon^{a b c} \sigma_{i}^{c},\tag{A.1}
$$

$$
\left[\sigma_{1}^{a} \sigma_{2}^{u}, \sigma_{1}^{b} \sigma_{2}^{v}\right] \quad=2 \mathrm{i} \sum_{c}\left(\delta^{u v} \varepsilon^{a b c} \sigma_{1}^{c}+\delta^{a b} \varepsilon^{u v c} \sigma_{2}^{c}\right),\tag{A.2}
$$

$$
\operatorname{Tr}_{2}\left[\sigma_{1}^{a} \sigma_{2}^{u}, \sigma_{1}^{b} \sigma_{2}^{v}\right]=4 \mathrm{i} \delta^{u v} \sum_{c} \varepsilon^{a b c} \sigma_{1}^{c},\tag{A.3}
$$

with component (superscript) indices $a, b, c, u, v \in \mathcal{I}$. We use the notation $\delta^{a b}$ for the Kronecker tensor, and $\varepsilon^{a b c}$ for the Levi-Civita tensor (with $\varepsilon^{x y z}=1$ ). In the identities involving Pauli operators on different lattice sites, the identity operator is implied on each single-spin Hilbert space $\mathcal{H}_{i}$ not acted upon by any of the Pauli operators [as on the right-hand side of (A.2)].

The starting point of the proof is the BBGKY hierarchy in the form (14) with a fixed value of $\ell$. Inserting the expansion (23) into the left-hand side of (14), we obtain

$$
2^{-\ell} \mathrm{i} \hbar \sum_{n=0}^{\ell} \sum_{a \in \mathcal{I}^{n}} \partial_{t} f_{n}^{a} \sum_{p \in \mathfrak{P}_{n}(\ell)} \sigma_{p}^{a},\tag{A.4}
$$

where $\mathcal{I} = \{x, y, x\}$ denotes the set of component indices. Since the operators $\boldsymbol{\sigma}_p^a$ are linearly independent among each other, we can separately equate their coefficients in (A.4) to those which result from expanding also the right-hand side of (14) in terms of (23). We will in the following set $n = \ell$, as this will be sufficient in order to obtain time evolution equations for all coefficients $f_n^a$. Since $\mathfrak{P}_\ell(\ell) = \{(1, \dots, \ell)\}$ contains only a single element, the sum over $p$ in (A.4) consists only of one term, $\boldsymbol{\sigma}_{(1,\dots,\ell)}^a$. The rest of this appendix will therefore be devoted to computing, from an expansion of the right-hand side of (14), all the terms proportional to $\boldsymbol{\sigma}_{(1,\dots,\ell)}^a$, and then equate them to

$$
2^{-\ell} \mathrm{i}\hbar\partial_t f_\ell^a \boldsymbol{\sigma}_{(1,\dots,\ell)}^a \tag{A.5}
$$

in order to obtain the time evolution equation of $f_\ell^a$. We will discuss the three terms on the right-hand side of (14) separately, showing that

$$
(\text{A.5}) = (\text{A.13}) + (\text{A.20}) + (\text{A.23}) \tag{A.6}
$$

We start by inserting the expansion (23) into the first term on the right-hand side of (14), yielding

$$
\sum_{i=1}^\ell [H_i, F_{1\ldots\ell}] = -2^{-\ell} \sum_{b\in\mathcal{I}} h^b \sum_{i,n=1}^\ell \sum_{a\in\mathcal{I}^n} f_n^a \sum_{p\in\mathfrak{P}_n(\ell)} \left[\sigma_i^b, \boldsymbol{\sigma}_p^a\right]. \tag{A.7}
$$

For the commutator in (A.7) we find

$$
\left[\sigma_i^b, \boldsymbol{\sigma}_p^a\right] = \sum_{j=1}^n \delta_{i,p_j} \boldsymbol{\sigma}_{p-p_j}^{a-a_j} \left[\sigma_i^b, \sigma_i^{a_j}\right] = -2\mathrm{i} \sum_{j=1}^n \delta_{i,p_j} \sum_{c\in\mathcal{I}} \varepsilon^{a_j b c} \boldsymbol{\sigma}_p^{a-a_j + c}, \tag{A.8}
$$

where (A.1) has been used. Here, $p - p_j$ and $a - a_j$ denote the sequences obtained from $p$ and $a$ by deleting their $j$th elements, and

$$
a - a_j + c = (a_1, \dots, a_{j-1}, \underbrace{c}_{j\text{th element}}, a_{j+1}, \dots, a_n) \tag{A.9}
$$

is the sequence where the $j$th element has been replaced by $c$. We observe that, for a given $p = (p_1, \dots, p_n)$ with $n$ elements, the commutator in (A.8) is again a product of $n$ Pauli operators acting on different lattice sites. Since, as explained above, we can restrict our attention to the terms proportional to a fixed $\boldsymbol{\sigma}_{(1,\dots,\ell)}^a$, it is sufficient to consider the terms with $n = \ell$ in (A.7),

$$
2^{1-\ell}\mathrm{i} \sum_{b,c\in\mathcal{I}} h^b \sum_{i,j=1}^\ell \sum_{p\in\mathfrak{P}_\ell(\ell)} \delta_{i,p_j} \sum_{a\in\mathcal{I}^\ell} f_\ell^a \varepsilon^{a_j b c} \boldsymbol{\sigma}_p^{a-a_j + c}, \tag{A.10}
$$

where the expression (A.8) for the commutator has been inserted. Since $\mathfrak{P}_\ell(\ell) = \{(1, \dots, \ell)\}$ consists of only a single element, the sum over $p$ disappears. Moreover, for the same reason, we have $\delta_{i,p_j} = \delta_{i,j}$, which allows us to execute the sum over $j$, yielding

$$
2^{1-\ell}\mathrm{i} \sum_{b,c\in\mathcal{I}} h^b \sum_{a\in\mathcal{I}^\ell} f_\ell^a \sum_{i=1}^\ell \varepsilon^{a_i b c} \boldsymbol{\sigma}_{(1,\dots,\ell)}^{a-a_i + c}. \tag{A.11}
$$

Swapping names of the summation indices $a_i$ and $c$ and making use of the cyclic property of the Levi-Civita tensor, we can rewrite (A.11) as

$$
- 2^{1-\ell}\mathrm{i} \sum_{a\in\mathcal{I}^\ell} \boldsymbol{\sigma}_{(1,\dots,\ell)}^a \sum_{b,c\in\mathcal{I}} h^b \sum_{i=1}^\ell \varepsilon^{a_i b c} f_\ell^{a-a_i + c}. \tag{A.12}
$$

Owing to the mutual independence of the $\boldsymbol{\sigma}_p^a$, we now can pick, for a given $a$, the term
$$
-2^{1-\ell} \mathrm{i} \boldsymbol{\sigma}_{(1, \ldots, \ell)}^{a} \sum_{b, c \in \mathcal{I}} \sum_{i=1}^{\ell} h^{b} \varepsilon^{a_{i} b c} f_{\ell}^{a-a_{i}+c}
\tag{A.13}
$$
which gives the first contribution to the time evolution equation (A.6) for the coefficient $f_{\ell}^{a}$.

To deal with the second term on the right-hand side of (14), we again replace the $\ell$-spin reduced density operator $F_{1 \ldots \ell}$ by the expansion (23), obtaining
$$
\sum_{j<i=1}^{\ell}\left[V_{i j}, F_{1 \ldots \ell}\right]=-\sum_{b, c \in \mathcal{I}} \frac{J^{b c}}{2^{\ell+1} N} \sum_{\substack{i, j=1 \\ i \neq j}}^{\ell} \sum_{n=1}^{\ell} \sum_{a \in \mathcal{I}^{n}} f_{n}^{a} \sum_{p \in \mathfrak{P}_{n}(\ell)}\left[\sigma_{i}^{b} \sigma_{j}^{c}, \boldsymbol{\sigma}_{p}^{a}\right].
\tag{A.14}
$$

Under the condition $i \neq j$, we can write
$$
\begin{aligned}
{\left[\sigma_{i}^{b} \sigma_{j}^{c}, \boldsymbol{\sigma}_{p}^{a}\right]=} & \sum_{k, l=1}^{n} \delta_{i, p_{k}} \delta_{j, p_{l}} \boldsymbol{\sigma}_{p-p_{k}-p_{l}}^{a-a_{k}-a_{l}}\left[\sigma_{i}^{b} \sigma_{j}^{c}, \sigma_{i}^{a_{k}} \sigma_{i}^{a_{l}}\right] \\
& +\sum_{k=1}^{n}\left(\delta_{i, p_{k}} \delta_{j \notin p} \sigma_{j}^{c}\left[\sigma_{i}^{b}, \sigma_{i}^{a_{k}}\right]+\delta_{j, p_{k}} \delta_{i \notin p} \sigma_{i}^{c}\left[\sigma_{j}^{b}, \sigma_{j}^{a_{k}}\right]\right) \boldsymbol{\sigma}_{p-p_{k}}^{a-a_{k}}
\end{aligned}
\tag{A.15}
$$
for the commutator in (A.14), where we have used the short-hand notation $\delta_{j \notin p}=$ $\prod_{m=1}^{n}\left(1-\delta_{j, p_{m}}\right)$. The first term on the right-hand side accounts for the cases where both, $i$ and $j$, have a counterpart in $\boldsymbol{\sigma}_{p}^{a}$, the second term for when only one of them has. (If neither $i$ nor $j$ have a counterpart in $\boldsymbol{\sigma}_{p}^{a}$ then the commutator is zero.) Applying (A.2) to the commutator in the first sum in (A.15), all summands will consist of products of $n-1$ Pauli operators. Since $n \leqslant \ell$, none of these terms can give a contribution to (A.14) which is proportional to $\boldsymbol{\sigma}_{(1, \ldots, \ell)}^{a}$, and the first sum in (A.15) can therefore be neglected. Applying (A.1) to the commutator in the second sum in (A.15), however, results in products of $n+1$ Pauli operators. Hence, inserting (A.15) into (A.14), we can restrict the summation to the $n=\ell-1$ terms, as only those may lead to contributions proportional to $\boldsymbol{\sigma}_{(1, \ldots, \ell)}^{a}$,
$$
\begin{aligned}
\sum_{b, c \in \mathcal{I}} & \frac{J^{b c}}{2^{\ell} N} \sum_{a \in \mathcal{I}^{\ell-1}} f_{\ell-1}^{a} \sum_{p \in \mathfrak{P}_{\ell-1}(\ell)} \sum_{\substack{i, j=1 \\ i \neq j}}^{\ell} \sum_{k=1}^{\ell-1} \boldsymbol{\sigma}_{p-p_{k}}^{a-a_{k}} \\
& \times\left(\delta_{i, p_{k}} \delta_{j \notin p} \sigma_{j}^{c}\left[\sigma_{i}^{b}, \sigma_{i}^{a_{k}}\right]+\delta_{j, p_{k}} \delta_{i \notin p} \sigma_{i}^{c}\left[\sigma_{j}^{b}, \sigma_{j}^{a_{k}}\right]\right).
\end{aligned}
\tag{A.16}
$$

The terms in the round brackets in (A.16) are symmetric to each other under the exchange of $i \leftrightarrow j$, and their contributions to the overall sum are therefore identical. Hence we can write
$$
\sum_{b, c, d \in \mathcal{I}} \frac{\mathrm{i} J^{b c}}{2^{\ell-1} N} \sum_{a \in \mathcal{I}^{\ell-1}} f_{\ell-1}^{a} \sum_{p \in \mathfrak{P}_{\ell-1}(\ell)} \sum_{\substack{i, j=1 \\ i \neq j}}^{\ell} \sum_{k=1}^{\ell-1} \delta_{i, p_{k}} \delta_{j \notin p} \varepsilon^{a_{k} b d} \boldsymbol{\sigma}_{p+j}^{a-a_{k}+d+c},
\tag{A.17}
$$
where (A.1) has been applied to the commutators in (A.16). The set $\mathfrak{P}_{\ell-1}(\ell)$ consists of all sequences where precisely one of the numbers $1, \ldots, \ell$ is omitted. For example, for $\ell=4$, we have $\mathfrak{P}_{3}(4)=\{(1,2,3),(1,2,4),(1,3,4),(2,3,4)\}$. Due to the constraint $\delta_{j \notin p}$ in (A.17), $j$ has to equal this omitted number for all non-vanishing contributions to the sum. We can therefore combine every $p \in \mathfrak{P}_{\ell-1}(\ell)$ together with $j \notin p$ into a

new summation index $p' \in \mathfrak{P}_{\ell}(\ell)$, and then use the sum over $j$ to count through the previously omitted elements of the sequence. With these new summation indices, we can rewrite (A.17) in the form

$$
\frac{2^{1-\ell} \mathrm{i}}{N} \sum_{b, d \in \mathcal{I}} \sum_{\substack{i, j=1 \\ i \neq j}}^{\ell} \sum_{a \in \mathcal{I}^{\ell}} \varepsilon^{a_{i} b d} J^{b a_{j}} f_{\ell-1}^{a-a_{j}} \sum_{p^{\prime} \in \mathfrak{P}_{\ell}(\ell)} \sigma_{p^{\prime}}^{a-a_{i}+d}, \tag{A.18}
$$

where the former component index $c$ has now been included into the multi-index $a$. Observing that $\mathfrak{P}_{\ell}(\ell)=\{(1, \ldots, \ell)\}$ consists of only a single element and after some renaming of indices, we can write (A.18) as

$$
-\frac{2^{1-\ell} \mathrm{i}}{N} \sum_{a \in \mathcal{I}^{\ell}} \sigma_{(1, \ldots, \ell)}^{a} \sum_{b, d \in \mathcal{I}} \sum_{\substack{i, j=1 \\ i \neq j}}^{\ell} \varepsilon^{a_{i} b d} J^{b a_{j}} f_{\ell-1}^{a-a_{i}+d-a_{j}}. \tag{A.19}
$$

Owing to the mutual independence of the $\sigma_{p}^{a}$, we now can pick, for a given $a$, the term

$$
-\frac{2^{1-\ell} \mathrm{i}}{N} \sigma_{(1, \ldots, \ell)}^{a} \sum_{b, d \in \mathcal{I}} \sum_{\substack{i, j=1 \\ i \neq j}}^{\ell} \varepsilon^{a_{i} b d} J^{b a_{j}} f_{\ell-1}^{a-a_{i}+d-a_{j}}. \tag{A.20}
$$

which gives the second contribution to the time evolution equation (A.6) for the coefficient $f_{\ell}^{a}$. Similar to the notation introduced in (A.9), the multi-index

$$
a-a_{i}+d-a_{j}=\left(a_{1}, \ldots, a_{i-1}, d, a_{i+1}, \ldots, a_{j-1}, a_{j+1}, \ldots, a_{\ell}\right) \tag{A.21}
$$

in (A.20) is derived from $a$ by replacing the $i$ th element by $d$ and then deleting the $j$ th entry of $a$.

The contribution from the third term on the right-hand side of (14) is derived in a very similar way, so we will only sketch the calculation here. Replacing the $(\ell+1)$-spin reduced density operator $F_{1 \ldots \ell+1}$ by the expansion (23), we obtain

$$
\begin{aligned}
& (N-\ell) \sum_{i=1}^{\ell} \operatorname{Tr}_{\ell+1}\left[V_{i, \ell+1}, F_{1 \ldots \ell+1}\right] \\
& \quad=-\frac{N-\ell}{2^{\ell+1} N} \sum_{b, c \in \mathcal{I}} J^{b c} \sum_{n=1}^{\ell+1} \sum_{a \in \mathcal{I}^{n}} f_{n}^{a} \sum_{p \in \mathfrak{P}_{n}(\ell+1)} \sum_{i=1}^{\ell} \operatorname{Tr}_{\ell+1}\left[\sigma_{i}^{b} \sigma_{\ell+1}^{c}, \sigma_{p}^{a}\right].
\end{aligned} \tag{A.22}
$$

Applying (A.3) to the partial trace of the commutator in (A.22) one finds, similarly to the discussion of the second term, that only summands with $n=\ell+1$ can lead to terms proportional to $\sigma_{(1, \ldots, \ell)}^{a}$ in (A.22). As a consequence, the sum over $p$ again consists of only a single term and, after some reshuffling of summation indices, we obtain

$$
\frac{N-\ell}{2^{\ell-1} \mathrm{i} N} \sigma_{(1, \ldots, \ell)}^{a} \sum_{b, c, d \in \mathcal{I}} J^{b c} \sum_{i=1}^{\ell} \varepsilon^{a_{i} b d} f_{\ell+1}^{a-a_{i}+d+c} \tag{A.23}
$$

as the contribution to (A.22) which is proportional to a given $\sigma_{(1, \ldots, \ell)}^{a}$. The multi-index

$$
a-a_{i}+d+c=\left(a_{1}, \ldots, a_{i-1}, d, a_{i+1}, \ldots, a_{\ell}, c\right) \tag{A.24}
$$

in (A.23) is obtained from $a$ by replacing the $i$ th element by $d$ and then appending $c$.

This completes the proof.

Equilibration in long-range quantum spin systems from a BBGKY perspective
27

[1] I. Bloch, J. Dalibard, and W. Zwerger. Many-body physics with ultracold gases. Rev. Mod. Phys., 80:885-964, 2008.

[2] J. v. Neumann. Beweis des Ergodensatzes und des H-Theorems in der neuen Mechanik. Z. Phys., 57:30-70, 1929.

[3] P. Reimann. Foundation of statistical mechanics under experimentally realistic conditions. Phys. Rev. Lett., 101:190403(1-4), 2008.

[4] S. Goldstein, J. L. Lebowitz, C. Mastrodonato, R. Tumulka, and N. Zanghì. Approach to thermal equilibrium of macroscopic quantum systems. Phys. Rev. E, 81:011109(1-9), 2010.

[5] T. Kinoshita, T. Wenger, and D. S. Weiss. A quantum Newton's cradle. Nature (London), 440:900-903, 2006.

[6] A. Polkovnikov, K. Sengupta, A. Silva, and M. Vengalattore. Colloquium: Nonequilibrium dynamics of closed interacting quantum systems. Rev. Mod. Phys., 83:863-883, 2011.

[7] M. Rigol, V. Dunjko, V. Yurovsky, and M. Olshanii. Relaxation in a completely integrable many-body quantum system: An ab initio study of the dynamics of the highly excited states of 1d lattice hard-core bosons. Phys. Rev. Lett., 98:050405(1-4), 2007.

[8] G. G. Emch. Non-Markovian model for the approach to equilibrium. J. Math. Phys., 7:1198-1206, 1966.

[9] C. Radin. Approach to equilibrium in a simple model. J. Math. Phys., 11:2945-2955, 1970.

[10] M. Kastner. Diverging equilibration times in long-range quantum spin models. Phys. Rev. Lett., 106:130601(1-4), 2011.

[11] M. Kastner. Long-time asymptotics of the long-range Emch-Radin model. arXiv:1110.4721.

[12] A. Campa, T. Dauxois, and S. Ruffo. Statistical mechanics and dynamics of solvable models with long-range interactions. Phys. Rep., 480:57-159, 2009.

[13] F. Bouchet, S. Gupta, and D. Mukamel. Thermodynamics and dynamics of systems with long-range interactions. Physica A, 389:4389-4405, 2010.

[14] M. Joyce and T. Worrakitpoonpon. Relaxation to thermal equilibrium in the self-gravitating sheet model. J. Stat. Mech., 2010:P10012(1-34), 2010.

[15] J. Barré, F. Bouchet, T. Dauxois, S. Ruffo, and Y. Y. Yamaguchi. The Vlasov equation and the Hamiltonian mean-field model. Physica A, 365:177-183, 2006.

[16] A. Antoniazzi, D. Fanelli, J. Barré, Chavanis, P. H., T. Dauxois, and S. Ruffo. Maximum entropy principle explains quasistationary states in systems with long-range interactions: The example of the Hamiltonian mean-field model. Phys. Rev. E, 75:011112(1-4), 2007.

[17] P.-H. Chavanis, F. Baldovin, and E. Orlandini. Noise-induced dynamical phase transitions in long-range systems. Phys. Rev. E, 83:040101(1-4), 2011.

[18] W. Braun and K. Hepp. The Vlasov dynamics and its fluctuations in the $1/N$ limit of interacting classical particles. Commun. Math. Phys., 56:101-113, 1977.

[19] M. Kastner. Nonequivalence of ensembles for long-range quantum spin systems in optical lattices. Phys. Rev. Lett., 104:240403(1-4), 2010.

[20] M. Kastner. Nonequivalence of ensembles in the Curie-Weiss anisotropic quantum Heisenberg model. J. Stat. Mech., 2010:P07006(1-25), 2010.

[21] M. Bonitz. Quantum Kinetic Theory. Teubner, Stuttgart, 1998.

[22] T. S. Chihara. An Introduction to Orthogonal Polynomials. Gordon and Breach, New York, 1978.

[23] R. Paškauskas. Long-range interacting spins on a lattice. In preparation.

[24] B. Sciolla and G. Biroli. Dynamical transitions and quantum quenches in mean-field models. J. Stat. Mech., 2011:P11003, 2011.