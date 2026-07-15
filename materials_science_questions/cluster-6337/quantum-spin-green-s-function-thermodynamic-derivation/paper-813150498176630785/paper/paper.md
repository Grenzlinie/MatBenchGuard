# Cumulant Expansion and Wick's Theorem for Spins. Application to the Antiferromagnetic Ground State*

TADASHI ARAI
Argonne National Laboratory, Argonne, Illinois

AND

BERNARD GOODMAN†
University of Cincinnati, Cincinnati, Ohio

and
Argonne National Laboratory, Argonne, Illinois

(Received 22 September 1966)

A form of Wick's theorem is derived which is applicable to spin operators of arbitrary magnitude in a manner analogous to the decomposition of fermion and boson operator products. Use of the theorem together with Kubo's cumulant rearrangement of perturbation theory leads to a compact prescription for the calculation of the ground-state energy of spin systems. This method is parallel to Goldstone's linked-cluster expansion for fermions, but the expansion for spins, as well as for bosons, contains cumulant correction terms. The Green functions are shown to be expanded similarly in terms of cumulants. The method is illustrated by the calculation of the antiferromagnetic ground state, and circumvents the involved development in the previous work of Davis and Boon. It is found that our procedure gives better convergence than Davis's expansion and that Boon's final formulas as well as his numerical results contain some errors.

## 1. INTRODUCTION
$I^N$ the application of many-body perturbation theories to spin systems we encounter a number of difficulties because spins are neither fermions nor bosons. In the treatment of spin waves, for example, we observe that the spin deviations behave like bosons, but only up to a finite number $2j$ of them can be attached to a given atom at the same time. This statistical hindrance introduces Dyson's kinematical interaction between the spins. $^1$ Since the commutators of spin operators are still spin operators and not $c$ numbers, the usual Wick reduction method$^{2,3}$ for boson and fermion operator products cannot be applied to the product of spin operators and the direct use of the latter in perturbation calculations becomes difficult. Furthermore, the spin Hamiltonian describes the exchange interaction, which is inherently a two-body correlation and there is no natural division into a one-particle Hamiltonian plus interaction part.

In many cases$^4$ spin operators are transformed to boson operators and Wick's theorem for bosons is applied in the calculation. However, a one-particle Hamiltonian has to be introduced, often artificially, as the unperturbed Hamiltonian, and the resulting approximations may lead to unphysical states which violate the kinematical interaction of spins.

Using the Schwinger representation$^5$ of spin operators by coupled bosons, Davis$^6$ was able to adapt Wick's theorem for bosons to develop a linked-cluster expansion for the ground state of a spin system. In this method, the coupling of operators for the boson pair $v$ and $u$ belonging to each spin operator automatically includes the kinematical interaction. The unperturbed Hamiltonian consists of the energy of formation of isolated spin deviations from the reference spin configuration and is the part of the pair interaction which is linear in the spin deviations.

Very recently Wang and Callen$^7$ have applied Davis's formulation and obtained a Wick theorem applicable to spin systems. Here, the contractions are among the $v$ factors and the effect of the coupled $u$ factors is included by adding a special class of "locked diagrams."

Giovannini$^8$ and Doniach$^9$ have generalized Wick's theorem by using the commutation relations of spin operators directly. Since the contractions in their procedures are still spin operators, it is necessary to consider multiple contractions. This complicates the decomposition of a time-ordered product into all possible combinations of contractions.

In this paper a form of Wick's theorem is given for spin operators which retains much of the familiar form

* Based on work performed under the auspices of the U. S. Atomic Energy Commission.
† Permanent address: University of Cincinnati, Cincinnati, Ohio.
$^1$ F. J. Dyson, Phys. Rev. 102, 1217, 1230 (1956).
$^2$ G. C. Wick, Phys. Rev. 80, 268 (1950).
$^3$ A complete proof of Wick's theorem will be found in J. M. Jauch and F. Rohrlich, *The Theory of Photons and Electrons* (Addison-Wesley Publishing Company, Cambridge, Massachusetts, 1955), Appendix A4.
$^4$ See, for instance, R. B. Stinchcombe, G. Horwitz, F. Englert, and R. Brout, Phys. Rev. 130, 155 (1963); H. B. Callen, *ibid.* 130, 890 (1963); T. Morita and T. Tanaka, *ibid.* 137, A648 (1965); 138, A1395 (1965).
$^5$ J. Schwinger, Atomic Energy Commission Report NYO-3071, 1952 (unpublished). See also D. Mattis, *The Theory of Magnetism* (Harper & Row, Publishers, Inc., New York, 1965).
$^6$ H. L. Davis, Phys. Rev. 120, 789 (1960).
$^7$ Y. L. Wang and H. B. Callen, Phys. Rev. 148, 433 (1966). Also see Y. L. Wang, S. Shtrikman, and H. Callen, *ibid.* 148, 419 (1966).
$^8$ B. Giovannini, Scientific Papers of the College of General Education, University of Tokyo 15, 49 (1965). Also see B. Giovannini and S. Koide, Progr. Theoret. Phys. (Kyoto) 34, 705 (1965).
$^9$ S. Doniach, Phys. Rev. 144, 382 (1966).

155 514

for fermions and bosons and which can be applied in an analogous manner since the contractions are now quasi- $c$ numbers. The theorem is more complicated than the original form mainly because the part

$$
\sum_{h, k} J_{h k} S_{h}{ }^{z} S_{k}{ }^{z}
$$

of the exchange interaction is included in the un- perturbed Hamiltonian $H_{0}$. It is no longer necessary to introduce a one-particle Hamiltonian, and the con- vergence of the perturbation expansion of the energy is improved.

The Wick decomposition leads to a compact pre- scription for the perturbation calculation of the ground state when it is applied in connection with the cumulant expansion rearrangement of perturbation theory given by Kubo. $^{10}$ The method is parallel to Goldstone's linked cluster expansion for fermions, $^{11}$ but the expansion for spins, as well as for bosons, will contain cumulant correction terms because the clusters involved are not completely independent of each other. The spin Green's functions may be expanded similarly in terms of cumu- lants. The technique corresponds to the introduction of linked diagrams including "locks" in the method of Wang and Callen.

The prescription is illustrated by a calculation of the antiferromagnetic ground state which has been con- sidered previously by Davis $^{6}$ and Boon. $^{12}$ The use of Kubo's formulation circumvents the involved develop- ments in these two works and clarifies the fact that their apparently different cluster expansions generate cumulants in the course of the developments. Numerical comparisons are also made.

## 2. KUBO'S THEOREM ON GENERALIZED CUMULANTS

The cumulants $\langle X_{1}^{\nu_{1}} \cdots X_{N}^{\nu_{N}}\rangle_{\text {cumul }}$ for $N$ random variables $X_{1}, \cdots, X_{N}$ are defined by the relation

$$
\left\langle\exp \sum_{j=1}^{N} \rho_{j} X_{j}\right\rangle=\sum_{\nu_{1}=0}^{\infty} \cdots \sum_{\nu_{N}=0}^{\infty}\left(\prod_{j=1}^{N} \frac{\rho_{j}^{\nu_{j}}}{\nu_{j}!}\right)\left\langle X_{1}^{\nu_{1}} \cdots X_{N}^{\nu_{N}}\right\rangle=\exp \left[\sum_{\nu_{1} \cdots \nu_{N}}^{\prime}\left(\prod_{j=1}^{N} \frac{\rho_{j}^{\nu_{j}}}{\nu_{j}!}\right)\left\langle X_{1}^{\nu_{1}} \cdots X_{N}^{\nu_{N}}\right\rangle_{\text {cumul }}\right], \quad \text { (2.1) }
$$

where

$$
\sum_{\nu_{1} \cdots \nu_{N}}^{\prime}
$$

is the summations over $\nu_{1}, \cdots, \nu_{N}$, but excludes $\nu_{1}=\nu_{2}=\cdots=\nu_{N}=0$, and the bracket $\left\langle X_{1}^{\nu_{1}} \cdots X_{N}^{\nu_{N}}\right\rangle$ represents the expectation value of the random variables $X_{1}, \cdots, X_{N}$. The explicit form of the first few cumulants is

$$
\begin{aligned}
\left\langle X_{1}\right\rangle_{\text {cumul }} & =\left\langle X_{1}\right\rangle, \\
\left\langle X_{1} X_{2}\right\rangle_{\text {cumul }} & =\left\langle X_{1} X_{2}\right\rangle-\left\langle X_{1}\right\rangle\left\langle X_{2}\right\rangle, \\
\left\langle X_{1} X_{2} X_{3}\right\rangle_{\text {cumul }} & =\left\langle X_{1} X_{2} X_{3}\right\rangle-\left\langle X_{1}\right\rangle\left\langle X_{2} X_{3}\right\rangle-\left\langle X_{2}\right\rangle\left\langle X_{1} X_{3}\right\rangle-\left\langle X_{3}\right\rangle\left\langle X_{1} X_{2}\right\rangle+2\left\langle X_{1}\right\rangle\left\langle X_{2}\right\rangle\left\langle X_{3}\right\rangle,
\end{aligned}
$$

while the general formula for calculating cumulants in terms of averages $\left\langle X_{1}^{\nu_{1}} \cdots X_{N}^{\nu_{N}}\right\rangle$ has been obtained by Meeron. $^{13}$ In particular, if each argument $X_{i}$ occurs at most once, then

$$
\left\langle X_{1} \cdots X_{n}\right\rangle_{\text {cumul }}=\sum_{l=1}^{n} \sum_{\substack{\text { all possible } \\ l \text { partitions }}}(-1)^{l-1}(l-1)!\left\langle X_{i_{1}} \cdots\right\rangle\left\langle X_{i_{2}} \cdots\right\rangle \cdots\left\langle X_{i_{l}} \cdots\right\rangle .
$$

Equation (2.1) may be written as

$$
\left\langle\exp \sum_{j=1}^{N} \rho_{j} X_{j}\right\rangle=\exp \left\langle\exp \left(\sum_{j=1}^{N} \rho_{j} X_{j}\right)-1\right\rangle_{\text {cumul }},
$$

under the interpretation that the exponential function in $\langle\cdots\rangle_{\text {cumul }}$ is to be expanded in powers of $X$ 's and the cumulant average is to be taken for each product thus obtained. If we replace the set of variables $\rho_{j} X_{j}$ in (2.4) by the set of $X\left(t_{j}\right) \delta t_{j}$ 's and take the limit that max. $\delta t_{j} \rightarrow 0$, the summation in (2.4) will be converted into an integration such that

$$
\left\langle\exp \int_{a}^{b} X(t) d t\right\rangle=\exp \left\langle\exp \int_{a}^{b} X(t) d t-1\right\rangle_{\text {cumul }} .
$$

10 R. Kubo, J. Phys. Soc. Japan 17, 1100 (1962).
11 J. Goldstone, Proc. Roy. Soc. (London) A239, 267 (1957); J. Hubbard, ibid. A240, 539 (1957).
12 M. H. Boon, Nuovo Cimento 21, 885 (1961).
13 E. Meeron, J. Chem. Phys. 27, 1238 (1957).

More generally,
$$
\begin{aligned}
\left\langle\exp \int_{a}^{b} \sum_{j=1}^{N} X_{j}(t) d t\right\rangle= & \exp \left\langle\exp \int_{a}^{b} \sum_{j=1}^{N} X_{j}(t) d t-1\right\rangle_{\text {cumul }} \\
& =\exp \left[\sum_{n=1}^{\infty} \frac{1}{n!} \int_{a}^{b} d t_{n} \cdots \int_{a}^{b} d t_{1} \sum_{j_{n}} \cdots \sum_{j_{1}}\left\langle X_{j_{n}}\left(t_{n}\right) \cdots X_{j_{1}}\left(t_{1}\right)\right\rangle_{\text {cumul }}\right]. \quad(2.6)
\end{aligned}
$$

Kubo has generalized the above formalism pointing out that similar relations hold even if the variables $X_{j}$ are operators rather than $c$ numbers. If the averaging process is disregarded and $\left\langle X_{j}\right\rangle$ is simply $X_{j}$ by itself, algebraic relations like (2.1) and (2.2) hold only in a trivial sense as pure operator relations because all cumulants except those of the first order vanish identically. In the case of a many-particle system, the variables usually pertain to particles or excitations. If they are connected through interactions or through correlations existing in the state of interest, a nonzero cumulant corresponding to them will appear and the cumulant relations (2.1) to (2.6) become nontrivial.

In the present work we use the perturbation expansion of the time-development operator and the average, which will be denoted by the symbol $\operatorname{Av}\{\cdots\}$ instead of $\langle\cdots\rangle$, involves reduction of the operators when they act on the unperturbed state. If only a part of the product is reduced to $c$ numbers, the $\operatorname{Av}\{\cdots\}$ will still be a $q$ number. If a product cannot be reduced, no higher order cumulants are formed by it.

It is also necessary to introduce the time-ordered exponential function. Corresponding to (2.6), the following relation applies:
$$
\begin{aligned}
\operatorname{Av}\left\{\exp _{T} \int_{a}^{b} \sum_{j=1}^{N} X_{j}(t) d t\right\}= & \exp \operatorname{Av}\left\{\exp _{T} \int_{a}^{b} \sum_{j=1}^{N} X_{j}(t) d t-1\right\}_{\text {cumul }} \\
& =\exp \left[\sum_{n=1}^{\infty} \frac{1}{n!} \int_{a}^{b} d t_{n} \cdots \int_{a}^{b} d t_{1} \sum_{j_{n}} \cdots \sum_{j_{1}} \operatorname{Av}\left\{T X_{j_{n}}\left(t_{n}\right) \cdots X_{j_{1}}\left(t_{1}\right)\right\}_{\text {cumul }}\right], \quad(2.7)
\end{aligned}
$$
where $T$ is Dyson's time-ordering operator. In a cumulant such as
$$
\operatorname{Av}\{\cdots\}_{\text {cumul }}=\operatorname{Av}\{\cdots\}-\operatorname{Av}\{\cdots\} \operatorname{Av}\{\cdots\}, \quad(2.8)
$$
each factor $\operatorname{Av}\{\cdots\}$ on the right is obtained by reduction of the operator product acting directly on the unperturbed state, as in the previous paragraph. If the correction factor still contains operators, they should be ordered the same as in the original product, whenever necessary.

Furthermore, Kubo has proven that the following theorem on cumulants is still valid for operators:

Theorem: A cumulant
$$
\operatorname{Av}\left\{T X_{j_{n}}\left(t_{n}\right) \cdots X_{j_{1}}\left(t_{1}\right)\right\}_{\text {cumul }}
$$
is zero if the elements $X_{j_{n}}\left(t_{n}\right), \cdots, X_{j_{1}}\left(t_{1}\right)$ are divided into two or more groups which are independent of each other in calculating the average $\operatorname{Av}\{\cdots\}$.

![](./images/813150498176630785_1.jpg)
FIG. 1. An example of nonvanishing cumulants for bosons and fermions.

Use of (2.7) and the above theorem yield the cumulant generalization of the linked cluster expansion.

### 3. CUMULANT EXPANSION METHOD

Let us divide the Hamiltonian of an $N$-body system into the unperturbed Hamiltonian $H_{0}$ and the perturbation $\lambda H_{I}$ with the coupling constant $\lambda(=1)$ such that
$$
H=H_{0}+\lambda H_{I}. \quad(3.1)
$$

The dynamical properties of the system are then described by the equation of motion for the state vector
$$
i \hbar(\partial / \partial t) \psi_{\alpha}(t)=\lambda H_{I \alpha}(t) \psi_{\alpha}(t), \quad(3.2)
$$
where the perturbation $H_{I}(t)$ in the interaction representation is to be slowly switched on between $t=-\infty$ and $t=0$, and hence,
$$
H_{I \alpha}(t)=H_{I}(t) \exp (\alpha t), \quad(3.3)
$$
and
$$
H_{I}(t)=\exp \left(i H_{0} t / \hbar\right) H_{1} \exp \left(-i H_{0} t / \hbar\right). \quad(3.4)
$$

The equation of motion (3.2) can be integrated into the form
$$
\psi_{\alpha}(t)=U_{\alpha}(t,-\infty) \psi_{\alpha}(-\infty), \text { for } t \leqslant 0, \quad(3.5)
$$

by using the transformation $U_{\alpha}(t,-\infty)$:

$$
\begin{aligned}
U_{\alpha}(t,-\infty)=1+ & \sum_{n=1}^{\infty}(n!)^{-1}\left(\frac{\lambda}{i \hbar}\right)^{n} \int_{-\infty}^{t} d t_{n} \cdots \\
& \times \int_{-\infty}^{t} d t_{1} T\left[H_{I \alpha}\left(t_{n}\right) \cdots H_{I \alpha}\left(t_{1}\right)\right] \\
= & \exp _{T}\left[\left(\frac{\lambda}{i \hbar}\right) \int_{-\infty}^{t} H_{I \alpha}\left(t^{\prime}\right) d t^{\prime}\right].
\end{aligned}\qquad(3.6)
$$

We take $\psi_{\alpha}(-\infty) \equiv|a\rangle$ to be an eigenstate of $H_{0}$.
The ground-state energy of the Hamiltonian is $^{14}$

$$
E=E_{0}+\lim _{\alpha \rightarrow 0} i \hbar \alpha \lambda \frac{\partial}{\partial \lambda}\left[\left.\ln \left\langle 0\left|U_{\alpha}(0,-\infty)\right| 0\right\rangle\right|_{\lambda=1},\right.\qquad(3.7)
$$

where $E_{0}$ is the energy of the ground state $|0\rangle$ of $H_{0}$.
Since the use of the expression (3.6) for $U_{\alpha}(0,-\infty)$ in (2.7) leads to

$$
\begin{aligned}
\left\langle 0\left|\operatorname{Av}\left\{U_{\alpha}(0,-\infty)\right\}\right| 0\right\rangle & =\exp \langle 0| \operatorname{Av}\left\{\exp _{T}\left[\frac{\lambda}{i \hbar} \int_{-\infty}^{0} H_{I \alpha}\left(t^{\prime}\right) d t^{\prime}\right]-1\right\}_{\text {cumul }}|0\rangle \\
& =\exp \langle 0| \exp _{T}\left[\frac{\lambda}{i \hbar} \int_{-\infty}^{0} H_{I \alpha}\left(t^{\prime}\right) d t^{\prime}\right]-1|0\rangle_{\text {cumul }},
\end{aligned}\qquad(3.8)
$$

the energy $E$ is given in terms of cumulants

$$
\begin{aligned}
E=E_{0}+ & \left.\lim _{\alpha \rightarrow 0} i \hbar \alpha \lambda \frac{\partial}{\partial \lambda}\left\langle 0\left|\exp _{T}\left[\frac{\lambda}{i \hbar} \int_{-\infty}^{0} H_{I \alpha}\left(t^{\prime}\right) d t^{\prime}\right]-1\right| 0\right\rangle_{\text {cumul }}\right|_{\lambda=1} \\
=E_{0}+ & \left.\lim _{\alpha \rightarrow 0} i \hbar \alpha \sum_{n=1}^{\infty} \lambda \frac{\partial}{\partial \lambda}(n!)^{-1}\left(\frac{\lambda}{i \hbar}\right)^{n} \int_{-\infty}^{0} d t_{n} \cdots \int_{-\infty}^{0} d t_{1}\left\langle 0\left|T\left[H_{I \alpha}\left(t_{n}\right) \cdots H_{I \alpha}\left(t_{1}\right)\right]\right| 0\right\rangle_{\text {cumul }}\right|_{\lambda=1}.
\end{aligned}\qquad(3.9)
$$

Here matrix elements like $\langle a'|Av\{\cdots\}_{cumul }| a\rangle$ of a cumulant are denoted simply as $\langle a'|\cdots| a\rangle_{cumul }$ since it will not be necessary to indicate the intermediate process $Av\{\cdots\}$ explicitly. The expression (3.9) together with Kubo's theorem on cumulants proves the cumulant expansion.

After an integration over the time variables $t_{1}, \cdots, t_{n}$, the above expression becomes

$$
\begin{aligned}
\Delta E=E-E_{0}= & \lim _{\alpha \rightarrow 0}\left\langle 0\left|\sum_{n=1}^{\infty} H_{I} \frac{1}{E_{0}+i \hbar \alpha(n-1)-H_{0}} H_{I} \cdots H_{I} \frac{1}{E_{0}+i \hbar \alpha-H_{0}} H_{I}\right| 0\right\rangle_{\text {cumul }} \\
= & \sum_{n=0}^{\infty}\left\langle 0\left|H_{I}\left(\frac{1}{E_{0}-H_{0}} H_{I}\right)^{n}\right| 0\right\rangle_{\text {cumul }},
\end{aligned}\qquad(3.10)
$$

where the meaning of $\langle 0|\cdots| 0\rangle_{cumul }$ in (3.10) is different from the definition introduced in (3.8). This will be discussed in Sec. 6.

It is of interest to relate the expressions (3.9) and (3.10) to the linked cluster expansions developed for interacting fermion and boson systems. In both, use of Wick's theorem decomposes operator products into diagrams with contractions $\dot{A}_{\mathfrak{p}}(t_{2}) \dot{A}_{\mathfrak{p}}^{+}(t_{1})$ represented by particle lines. Two subdiagrams are independent under the averaging process described earlier if they contain no particle lines with a common $\mathfrak{p}$. If a diagram of order $S$ and one of order $S'$ each has a line $\mathfrak{p}$, there corresponds to them a nonzero cumulant of order $S+S'$, shown schematically in Fig. 1, where $f(n_{\mathfrak{p}})$ comes from operations like

$$
A_{\mathfrak{p}}+A_{\mathfrak{p}}+\left|n_{\mathfrak{p}}\right\rangle=\left[1 \pm\left(n_{\mathfrak{p}}+1\right)\right]^{1 / 2}\left(1 \pm n_{\mathfrak{p}}\right)^{1 / 2}\left|n_{\mathfrak{p}}+2\right\rangle, \quad(3.11)
$$

with + signs for bosons and - signs for fermions, and $n_{\mathfrak{p}}$ denotes the occupation number of the state $\mathfrak{p}$.

![](./images/813150498176630785_2.jpg)

FIG. 2. The exchange diagram which is generated from the diagram in Fig. 1.

For fermions, $f(n_{\mathfrak{p}}) \equiv 0$ and the nonvanishing contribution to the cumulant appears from the second term, the negative of the product of diagrams $S$ and $S'$. The value is equal to the value of the exchange diagram which would be calculated by setting $\mathfrak{p}=\mathfrak{p}'$ in the crossed lines of the diagram shown in Fig. 2, although, of course, the true value of the diagram with $\mathfrak{p}=\mathfrak{p}'$ is zero because of the Pauli principle. Thus the total value of the cumulant expansion is the same as if the cumulant corrections such as the second term in Fig. 1 are

14 M. Gell-Mann and F. Low, Phys. Rev. 84, 350 (1951).

neglected and $\mathbf{p}$ lines are summed over without restriction. This is the linked cluster expansion by Goldstone.

For bosons and spins, this sort of cancellation does not occur and the simple linked cluster expansion becomes invalid. However, the expressions (3.9) and (3.10) in the cumulant expansion are still valid. In Sec. 6, we shall show explicitly the correction to the linked cluster expansion in the case of spins.

We note that in (3.9) the terms in which the correction is needed contain more than one line for the same one-particle state (or spin site in the case of spins) which overlap in time. These terms cannot be evaluated by independent time integrations of the end points of the lines, which leads to complications in the evaluation of (3.10).

### 4. WICK'S THEOREM FOR SPIN ANGULAR MOMENTUM OPERATORS

For fermions and bosons, use of Wick's theorem simplifies and systematizes the calculation of the energy matrices involved in (3.9) and (3.10), and it is desirable to generalize this mathematical technique so that it can be applied to a system of spins. This will clarify the relation between the linked cluster expansion and the cumulant expansion.

Let $\mathbf{S}_h$ denote the spin angular momentum operator of atom $h$ and let the Hamiltonian of the spin system be assumed to have the form
$$
H=H_{0}+H_{I}, \quad(4.1)
$$
where
$$
H_{0}=\sum_{h} \lambda_{h} S_{h}{ }^{z}+\sum_{h, k} J_{h k} S_{h}{ }^{z} S_{k}{ }^{z}, \quad(4.2)
$$
and
$$
H_{I}=f\left(S_{h}^{+}, S_{k}^{+}, \cdots, S_{h}^{-}, S_{k}^{-}, \cdots\right). \quad(4.3)
$$

The constants $\lambda_{h}$ and $J_{h k}$ are the external field energy of spin $h$ and the exchange interaction between atoms $h$ and $k$, respectively. The unperturbed Hamiltonian $H_{0}$ involves only the $z$ components $S_{h}{ }^{z}$ of spin operators while, for the moment, the perturbation $H_{I}$ is assumed to be a function of $S_{h}{ }^{+}$'s and $S_{h}{ }^{-}$'s, where
$$
S_{h}{ }^{ \pm}=S_{h}{ }^{x} \pm i S_{h}{ }^{y}. \quad(4.4)
$$

This restriction on $H_{I}$ will be removed later and $f$ could become a function of $S_{h}{ }^{z}$'s.

The spin operators satisfy the following commutation relations:
$$
\left[S_{h}^{+}, S_{k}^{-}\right]=2 \hbar S_{h}{ }^{z} \delta_{h k}, \quad(4.5 \mathrm{a})
$$
$$
\left[S_{h}^{z}, S_{k}^{ \pm}\right]= \pm \hbar S_{h}^{ \pm} \delta_{h k}. \quad(4.5 \mathrm{~b})
$$

We define the spin operators $S_{h}{ }^{ \pm}(t)$ in the interaction representation by
$$
S_{h}{ }^{ \pm}(t)=\exp \left(i H_{0} t / \hbar\right) S_{h}{ }^{ \pm} \exp \left(-i H_{0} t / \hbar\right), \quad(4.6)
$$
which cannot be reduced to the usual form
$$
\exp [\text { const } \times t] S_{h}{ }^{ \pm} \text {. }
$$

Instead,
$$
S_{h}{ }^{ \pm}(t)=\left\{\exp \left[ \pm i\left(\lambda_{h} \mp \hbar J_{h h}+2 \sum_{k} J_{h k} S_{k}{ }^{z}\right) t\right]\right\} S_{h}{ }^{ \pm}, \quad(4.7)
$$
because of the pair interaction term
$$
\sum_{h, k} J_{h k} S_{h}{ }^{z} S_{k}{ }^{z}
$$
involved in $H_{0} .^{15}$ If $J_{h k} \equiv 0$ for all $h$'s and $k$'s, the $S_{h}{ }^{ \pm}(t)$ will have the usual form and the calculation of energy matrices will be simplified. $^{16}$

The preliminaries to the discussion of Wick's theorem are presented in the form of two lemmas and the definitions of the normal product and contractions.

Lemma 1: The spin operators $S_{h}{ }^{ \pm}(t)$ in the interaction representation satisfy the following commutation relation:
$$
S_{h}{ }^{u}\left(t_{2}\right) S_{k}{ }^{v}\left(t_{1}\right)-F_{h k}{ }^{u v} S_{k}{ }^{v}\left(t_{1}\right) S_{h}{ }^{u}\left(t_{2}\right)=\delta_{h, k} \delta_{u,-v} G_{h}{ }^{u}, \quad(4.8)
$$
where $u$ and $v$ each take on the values + and - for $S^{+}$ and $S^{-}$, respectively, and
$$
F_{h k}{ }^{u v}\left(t_{2}-t_{1}\right) \equiv F_{h k}=\exp \left[u v \times 2 i \hbar J_{h k}\left(t_{2}-t_{1}\right)\right], \quad(4.9 \mathrm{a})
$$
and
$$
\begin{aligned}
G_{h}{ }^{u}\left(t_{2}-t_{1}\right) & \equiv G_{h}=u \times 2 \hbar S_{h}{ }^{z} \\
& \times \exp \left[u i\left(\lambda_{h}-u \hbar J_{h h}+2 \sum_{k} J_{h k} S_{k}{ }^{z}\right)\left(t_{2}-t_{1}\right)\right]. \quad(4.9 \mathrm{~b})
\end{aligned}
$$

The quantization axis or direction of positive $S^{z}$ will be chosen for each sublattice as the negative of the magnetization direction of that sublattice in the ground state $|0\rangle$ of the Ising Hamiltonian $H_{0}$. Then
$$
S_{h}{ }^{-}|0\rangle=0, \quad \text { for all } h, \quad(4.10)
$$
so that the state $|0\rangle$ may be considered as a vacuum state and $S_{h}{ }^{-}$and $S_{h}{ }^{+}$are analogous to destruction and creation operators, respectively.

A normal product of $S^{ \pm}$operators will be one in which all $S^{-}$operators are to the right of all $S^{+}$operators. In the subsequent analysis it is useful to have a standard normal product, namely, one which is time ordered within the $S^{+}$and $S^{-}$sets, respectively:
$$
O^{n} \equiv S_{n}{ }^{+}\left(t_{n}\right) \cdots S_{r+1}{ }^{+}\left(t_{r+1}\right) S_{r}{ }^{-}\left(t_{r}\right) \cdots S_{1}{ }^{-}\left(t_{1}\right), \quad(4.11)
$$

15 Even if fermion or boson operators are used, this type of expression will be obtained as long as the unperturbed Hamiltonian includes a pair interaction term like
$$
\sum_{<h k>} V_{h k} A_{k}{ }^{+} A_{h}{ }^{+} A_{h} A_{k}
$$
and the commutation relation will have a form similar to (4.8) to (4.9) except that $G$ does not have a factor involving operators in front of
$$
\exp \left[ \pm i\left(\lambda_{h}+\sum_{k} V_{h k} A_{k}{ }^{+} A_{k}\right)\left(t_{2}-t_{1}\right) / \hbar\right].
$$

16 If only the part of (4.2) linear in the spin deviations is taken as $H_{0}$, the unperturbed Hamiltonian becomes the $H_{0 D}$ introduced by Davis. Then one-particle states are defined and $S_{h}{ }^{ \pm}(t)$ will have the form $\exp [$ const $\times t] S_{h}{ }^{ \pm}$so that $F=1$. However, the $G$ still involves operator $S_{h}{ }^{z}$. A disadvantage of using $H_{0 D}$ as the unperturbed Hamiltonian is discussed in Sec. 7.

where $t_{n} \geqslant \cdots \geqslant t_{r+1}$ and $t_{r} \geqslant \cdots \geqslant t_{1}$. If two times are equal in a set, the order is immaterial since the phase factor $F_{h k}$ given by (4.9a) is unity. The phase factors must be incorporated in the definition of the normal product $N^{n}=N\{S_{i_{n}} S_{i_{n-1}} \cdots S_{i_{1}}\}$ of operators listed in a given order, so that

$$N^{n} \equiv N\left\{S_{i_{n}} S_{i_{n-1}} \cdots S_{i_{1}}\right\}=\left(\stackrel{(n)}{\prod^{N}} F_{h k}\right) × O^{n}, \quad(4.12)$$

where $O^{n}$ is the standard normal product and a factor $F_{h k}$ comes from each pair exchange required to bring the given order of the operators to the standard order $O^{n}$.

If, for example, $t_{n+1}$ is greater than the other times,
$$N\left\{S_{n+1}{ }^{+}\left(t_{n+1}\right) N^{n}\right\} \equiv N^{n+1}=S_{n+1}{ }^{+}\left(t_{n+1}\right) N^{n}, \quad(4.13a)$$

$$
\begin{aligned}
N\left\{S_{n+1}-\left(t_{n+1}\right) N^{n}\right\} & \equiv N^{n+1} \\
= & F_{n+1, n} \cdots F_{n+1, r+1}\left(\stackrel{(n)}{\prod^{N}} F_{h k}\right) S_{n}{ }^{+}\left(t_{n}\right) \cdots \\
& × S_{r+1}+\left(t_{r+1}\right) S_{n+1}-\left(t_{n+1}\right) S_{r}-\left(t_{r}\right) \cdots S_{1}-\left(t_{1}\right) \\
= & \left(\stackrel{(n+1)}{\prod^{N}} F_{h k}\right) O^{n+1}. \quad(4.13 \mathrm{~b})
\end{aligned}
$$

In (4.13b), the labeling $n, \cdots, 1$ refers to the order of the operators in $O^{n}$ and not to their original order $i_{n}, i_{n-1}, \cdots, i_{1}$ in $N^{n}$, and
$$\stackrel{(n)}{\prod^{N}} F_{h k}$$
is the same as in (4.12).

The time-ordered product $T^{n}$ of $S^{ \pm}$ operators is defined as
$$T^{n} \equiv T\left\{S_{i_{n}} S_{i_{n-1}} \cdots S_{i_{1}}\right\}=\left(\stackrel{(n)}{\prod^{T}} F_{h k}\right) Q^{n}, \quad(4.14)$$
where
$$Q^{n} \equiv S_{n}^{ \pm}\left(t_{n}\right) S_{n-1}^{ \pm}\left(t_{n-1}\right) \cdots S_{1}^{ \pm}\left(t_{1}\right), \quad(4.15)$$
under the condition that $t_{n} \geqslant t_{n-1} \geqslant \cdots \geqslant t_{1}$ and a factor $F_{h k}$ comes from each pair interchange required to bring the original order $i_{n}, i_{n-1}, \cdots, i_{1}$ to the time order. In particular,
$$
\begin{aligned}
& T\left\{S_{h}{ }^{u}\left(t_{2}\right) S_{k}{ }^{v}\left(t_{1}\right)\right\} \\
& \quad \equiv \begin{cases}S_{h}{ }^{u}\left(t_{2}\right) S_{k}{ }^{v}\left(t_{1}\right), & \text { if } \quad t_{2} \geqslant t_{1}, \\
F_{h k}{ }^{u v}\left(t_{2}-t_{1}\right) S_{k}{ }^{v}\left(t_{1}\right) S_{h}{ }^{u}\left(t_{2}\right), & \text { if } \quad t_{1}>t_{2}.\end{cases}
\end{aligned}
$$

The contraction of two operators $S_{h}^{u}(t_{2})$ and $S_{k}^{v}(t_{1})$ is defined as the difference between the time-ordered and normal products and is denoted by dots above the two operators:
$$
\begin{aligned}
& \dot{S}_{h}{ }^{u}\left(t_{2}\right) \dot{S}_{k}{ }^{v}\left(t_{1}\right) \\
& \quad \equiv T\left\{S_{h}{ }^{u}\left(t_{2}\right) S_{k}{ }^{v}\left(t_{1}\right)\right\}-N\left\{S_{h}{ }^{u}\left(t_{2}\right) S_{k}{ }^{v}\left(t_{1}\right)\right\} \\
& \quad=\left[\theta\left(t_{2}-t_{1}\right)-\theta(u)\right] \delta_{h, k} \delta_{u,-v} G_{h}{ }^{u}\left(t_{2}-t_{1}\right), \quad(4.17)
\end{aligned}
$$
where $\theta(x)$ is the step function:
$$\theta(x)= \begin{cases}1, & \text { if } \quad x \geqslant 0 ; \\ 0, & \text { if } \quad x<0.\end{cases}\quad(4.18)$$

If, in particular, $t_{2}>t_{1}$,
$$\dot{S}_{h}-\left(t_{2}\right) \dot{S}_{k}+\left(t_{1}\right)=\delta_{h k} G_{h}-\left(t_{2}-t_{1}\right), \quad(4.19 \mathrm{a})$$
and
$$\text { the other contractions }=0 \text {. } \quad(4.19 \mathrm{~b})$$

The nonzero contractions are no longer $c$ numbers but functions of $S_{h}^{z}$. Since $S_{h}^{z}$ does not change the spin state in the basis we use, the contraction (4.17) can be considered as a quasi $c$ number whose value is a function of its position in an operator product at the time when the pair is contracted.

Lemma 2: Consider the standard normal product $O^{n}$ introduced in (4.11) and let $t_{n+1}$ be later than all the other times. Then
$$
\begin{aligned}
S_{n+1} \pm\left(t_{n+1}\right) O^{n} & =N\left\{S_{n+1} \pm\left(t_{n+1}\right) O^{n}\right\} \\
& +\sum_{l=1}^{n} N\left\{\dot{S}_{n+1} \pm\left(t_{n+1}\right) \cdots \dot{S}_{l} \pm\left(t_{l}\right) \cdots\right\}, \quad(4.20)
\end{aligned}
$$
where the singly contracted normal product is defined by
$$
\begin{aligned}
N\left\{\dot{S}_{n+1} \pm\left(t_{n+1}\right)\right. & \left.\cdots \dot{S}_{l} \pm\left(t_{l}\right) \cdots\right\} \\
\equiv & F_{n+1, n} \cdots F_{n+1, l+1} S_{n} \pm\left(t_{n}\right) \cdots \\
& × S_{l+1} \pm\left(t_{l+1}\right) \dot{S}_{n+1} \pm\left(t_{n+1}\right) \dot{S}_{l} \pm\left(t_{l}\right) \cdots, \quad(4.21)
\end{aligned}
$$
and the order $n, \cdots, l, \cdots, 1$ is the standard order.

The lemma is proven as follows: If $S_{n+1} \pm(t_{n+1})$ is a raising operator, the contractions on the right of (4.20) vanish according to (4.19). Furthermore, the product $S_{n+1}+(t_{n+1}) O^{n}$ is a normal product and the relation(4.20) is trivially satisfied.

If $S_{n+1} \pm(t_{n+1})$ is a lowering operator, the normal product $N\{S_{n+1}-(t_{n+1}) O^{n}\}$ is written as (4.13b), where
$$\left(\stackrel{(n)}{\prod^{N}} F_{h k}\right)=1.$$

Shifting $S_{n+1}-(t_{n+1})$ to the left, we obtain
$$
\begin{aligned}
N\left\{S_{n+1}-\left(t_{n+1}\right) O^{n}\right\}= & \left\{F_{n+1, n} \cdots F_{n+1, r+2} S_{n}+\left(t_{n}\right) \cdots S_{r+2}+\left(t_{r+2}\right)\left[F_{n+1, r+1} S_{r+1}+\left(t_{r+1}\right) S_{n+1}-\left(t_{n+1}\right)\right.\right. \\
& \left.-S_{n+1}-\left(t_{n+1}\right) S_{r+1}+\left(t_{r+1}\right)\right] S_{r}-\left(t_{r}\right) \cdots S_{1}-\left(t_{1}\right) \\
+ & F_{n+1, n} \cdots F_{n+1, r+3} S_{n}+\left(t_{n}\right) \cdots S_{r+3}+\left(t_{r+3}\right)\left[F_{n+1, r+2} S_{r+2}+\left(t_{r+2}\right) S_{n+1}-\left(t_{n+1}\right)\right. \\
& \left.-S_{n+1}-\left(t_{n+1}\right) S_{r+2}+\left(t_{r+2}\right)\right] S_{r+1}+\left(t_{r+1}\right) \cdots S_{1}-\left(t_{1}\right)+\cdots \\
+ & {\left[F_{n+1, n} S_{n}+\left(t_{n}\right) S_{n+1}-\left(t_{n+1}\right)-S_{n+1}-\left(t_{n+1}\right) S_{n}+\left(t_{n}\right)\right] S_{n-1}-\left(t_{n-1}\right) \cdots S_{r}-\left(t_{r}\right) \cdots S_{1}-\left(t_{1}\right) } \\
& \left.+S_{n+1}-\left(t_{n+1}\right) S_{n}+\left(t_{n}\right) \cdots S_{r}-\left(t_{r}\right) \cdots S_{1}-\left(t_{1}\right)\right\}.$$


Since
$$
\begin{aligned}
F_{n+1, l} S_{l}^{+}\left(t_{l}\right) S_{n+1}^{-}\left(t_{n+1}\right)-S_{n+1}^{-}\left(t_{n+1}\right) S_{l}^{+}\left(t_{l}\right) & \\
& =-\dot{S}_{n+1}^{-}\left(t_{n+1}\right) \dot{S}_{l}^{+}\left(t_{l}\right) \quad(4.23)
\end{aligned}
$$
and
$$
\dot{S}_{n+1}^{-}\left(t_{n+1}\right) \dot{S}_{l}^{-}\left(t_{l}\right)=0,\quad (4.24)
$$

Eq. (4.20) is proven.

The numerical value of the contraction $\dot{S}_{n+1} \pm\left(t_{n+1}\right)$ $\times \dot{S}_{l}^{ \pm}\left(t_{l}\right)$ involved in (4.20) is determined by the state
$$
|l-1, a\rangle \equiv S_{l-1} \pm\left(t_{l-1}\right) \cdots S_{1} \pm\left(t_{1}\right)|a\rangle, \quad(4.25)
$$
on which it operates to the right. Since $H_{0}$ contains $S_{h}^{z}$'s only, the state $|a\rangle$ as well as $|l-1, a\rangle$ will be an eigenfunction of all the $S_{h}^{z}$'s. Although we are interested in the vacuum state $|0\rangle$ introduced by (4.10), it is useful to consider an arbitrary $S^{z}$ eigenfunction $|a\rangle$; this permits us to arrange the Wick theorem in closer correspondence with the operator form of the theorem for fermions and bosons with $c$ number contractions. The only nonvanishing contractions are of the type (4.19a), and the numerical value in (4.20) is given by the eigenvalue equation
$$
\begin{aligned}
& \dot{S}_{n+1}^{-}\left(t_{n+1}\right) \dot{S}_{l}^{+}\left(t_{l}\right)|l-1, a\rangle \\
& \quad=\delta_{n+1, l}\left\langle G_{n+1}^{-}\left(t_{n+1}-t_{l}\right)\right\rangle_{l-1, a}|l-1, a\rangle, \quad(4.26)
\end{aligned}
$$
where the expectation value $\left\langle G_{n+1}-\left(t_{n+1}-t_{l}\right)\right\rangle_{l-1, a}$ is readily calculated from (4.9b) and (4.25) by counting the number of changes in $S_{n+1} z$ produced by the operators $S_{1}^{ \pm}, \cdots, S_{l-1}^{ \pm}$.

Lemma 2 is one step in the reduction of a time- ordered product to normal form. It is useful to have a more complete notation which incorporates the inter- change factors $F_{n+1, n} \cdots F_{n+1, l+1}$ which precede each contraction in (4.20) and to keep track of the state (4.25) to the right on which the contraction operates since subsequent contractions will remove operators on either side of it. Let
$$C_{a}{ }^{n}\{m, l\} \equiv F_{m, m-1} \cdots F_{m, l+1}\left\langle\dot{S}_{m}{ }^{ \pm}\left(t_{m}\right) \dot{S}_{l}{ }^{ \pm}\left(t_{l}\right)\right\rangle_{l-1, a},(4.27)$$
where the nonzero contractions $\dot{S}_{m}-(t_{m}) \dot{S}_{l}+(t_{l})$ , for $t_{m}>t_{l}$ , are to be evaluated from (4.26). Further, let $O^{n}\{\{n_{p}, \cdots, n_{1}\}\}$ be the standard normal product of $n-p$ operators obtained from $O^{n}$ by deleting the $p$ operators $S_{n_{p}}^{ \pm}, \cdots, S_{n_{1}}^{ \pm}$ . With this notation Lemma 2 becomes

**Corollary:**
$$
\begin{aligned}
S_{n+1} \pm\left(t_{n+1}\right) & O^{n}|a\rangle=N\left\{S_{n+1} \pm\left(t_{n+1}\right) O^{n}\right\}|a\rangle \\
& +\sum_{l=1}^{n} C_{a}{ }^{n+1}\{n+1, l\} O^{n+1}\{\{n+1, l\}\}|a\rangle. \quad(4.28)
\end{aligned}
$$

This is the analog of the lemma (A4-16) or (A4-47) of Ref. 3 leading to the usual Wick theorem.

For a time-ordered product $Q^{n}=S_{n}^{ \pm}(t_{n}) \cdots S_{1}^{ \pm}(t_{1})$ , let us define $P^{n}(2 p, a)$ as the sum over all possible combinations of $p$ pairs such that
$$
\begin{aligned}
P^{n}(2 p, a) \equiv & \sum_{\text {all } p \text { pairs }} C_{a}{ }^{n}\left\{n_{p}, l_{p}|\cdots ; n_{1}, l_{1}\rangle \cdots\right. \\
\times & C_{a}{ }^{n}\left\{n_{1}, l_{1}\right\} f^{n}\left\{n_{p}, l_{p} ; \cdots ; n_{1}, l_{1}\right\} \\
& \left.\times O^{n}\left\{\left\{n_{p}, l_{p} ; \cdots ; n_{1} l_{1}\right\}\right\}, \quad(4.29)\right.
\end{aligned}
$$
where $t_{n_{p}}>t_{n_{p-1}}>\cdots>t_{n_{1}}$ . The factor $C_{a}^{n}\{n_{p}, l_{p} \mid \cdots$ ; $n_{1} l_{1}\}$ is a generalization of $C_{a}^{n}\{m, l\}$ introduced in(4.27) but does not contain phase factors associated with any operators $S_{n_{p-1}}^{ \pm}, S_{l_{p-1}}^{ \pm}, \cdots, S_{n_{1}}^{ \pm}, S_{l_{1}}^{ \pm}$ , which are removed by previous contractions. The value of the contraction $\langle\dot{S}_{n_{p}} \pm \dot{S}_{l_{p}} \pm\rangle_{l_{p-1},\{\{\cdots\}\}, a}$ involved in the $C_{a}^{n}$ is to be evaluated by the state $|l_{p}-1,\{\{n_{p-1}, l_{p-1}\}\}$ $\cdots ; n_{1}, l_{1}\}\}, a\rangle$ which appears on the right of the opera tor $S_{l_{p}}^{ \pm}$ in $O^{n}\{\{n_{p-1}, l_{p-1} ; \cdots ; n_{1}, l_{1}\}\}|a\rangle$ . The factor $f^{n}\{n_{p}, l_{p} ; \cdots ; n_{1}, l_{1}\}$ consists of phase factors $F_{h k}$ not included in the $C_{a}^{n}$ 's. Hence the expression on the right of (4.29) is obtained from the time-ordered product $Q^{n}=S_{n} \pm(t_{n}) \cdots S_{1} \pm(t_{1})$ with the phase factor $f^{n}=1$ as follows: Starting from the operator $S_{1}^{ \pm}(t_{1})$ on the right of $Q^{n}$ , we shift all lowering operators $S_{l}-(t_{l})$ to the rightin time order and multiply $f^{n}$ by the phase factor $F_{h k}$  associated with each interchange until the operatorproduct is brought into the standard normal order $O^{n}$ defined by (4.11). If there were no contractions, $f^{n} O^{n}$ would become equal to the normal product $N\{Q^{n}\}$  introduced in (4.12). If, in the course of the rearrange- ment, an operator $S_{n^{\prime}} \pm(t_{n^{\prime}})$ is to be contracted with an operator $S_{l^{\prime}} \pm(t_{l^{\prime}})$ where $t_{n^{\prime}}>t_{l^{\prime}}$ , we replace both operators by $C_{a}^{n}\{n^{\prime}, l^{\prime} \mid \cdots\}$ after shifting the former. We indicate this removal of a pair by indices in $f^{n} O^{n}$ , that is, by $f^{n}\{\cdots ; n^{\prime}, l^{\prime} ; \cdots\} O^{n}\{\{\cdots ; n^{\prime}, l^{\prime} ; \cdots\}\}$ . The phase factors associated with bringing $S_{n^{\prime}} \pm(t_{n^{\prime}})$ to the immediate left of $S_{l^{\prime}} \pm(t_{l^{\prime}})$ before forming the contrac tion are included in $C_{a}^{n}\{n^{\prime}, l^{\prime} \mid \cdots\}$ . In practice, a normal product involving lowering operators will vanish when it operates on a vacuum state and, conse- quently, only those terms $O^{n}\{\{\cdots\}\}$ in which all spin lowering operators are contracted will contribute. The corresponding factors $f^{n}\{\cdots\}$ will then become unity because all the phase factors $F_{h k}$ associated with shifting $S^{-}$ operators are included in $C_{a}^{n}$ 's.

**Wick's Theorem:** A time-ordered product of $n$ operators can be decomposed into all possible combina- tions of contractions multiplied by normal products as follows:
$$
Q^{n}|a\rangle \equiv S_{n} \pm\left(t_{n}\right) \cdots S_{1} \pm\left(t_{1}\right)|a\rangle=\sum_{p=0}^{n / 2 \text { or }(n-1) / 2} P_{2 p}{ }^{n}|a\rangle.
$$

The theorem is proven by induction in exactly the same way as the usual Wick's theorem. It is obviously

valid for $n=2$ since (4.30) is written as
$$
\begin{aligned}
T\left\{S_{2}{ }^{ \pm}\left(t_{2}\right) S_{1}{ }^{ \pm}\left(t_{1}\right)\right\}|a\rangle= & {\left[N\left\{S_{2}{ }^{ \pm}\left(t_{2}\right) S_{1}{ }^{ \pm}\left(t_{1}\right)\right\}\right.} \\
& \left.+C_{a}{ }^{2}\{2,1\} f^{2}\{2,1\} O^{2}\{\{2,1\}\}\right]|a\rangle, \quad(4.31)
\end{aligned}
$$
but this is just the definition of the contraction $C_{a}^{2}\{2,1\}$ for the pair $S_{2}^{ \pm}(t_{2})$ and $S_{1}^{ \pm}(t_{1})$ because $f^{2}\{2,1\}$ $=O^{2}\{\{2,1\}\}=1$.

Let us assume that (4.30) is valid for $n$ and let $t_{n+1}$ be later than all the other times. Then
$$
\begin{aligned}
& T\left\{S_{n+1} \pm\left(t_{n+1}\right) Q^{n}\right\}|a\rangle \\
& \quad=\sum_{p=0}^{n / 2 \text { or }(n-1) / 2} S_{n+1} \pm\left(t_{n+1}\right) P_{2 p}{ }^{n}|a\rangle. \quad(4.32)
\end{aligned}
$$

$$
\begin{aligned}
S_{n+1} \pm & \left(t_{n+1}\right) P_{2 p}{ }^{n}|a\rangle=\sum_{\text {all } p \text { pairs }} C_{a}{ }^{n}\left\{n_{p}, l_{p} \mid \cdots ; n_{1}, l_{1}\right\} \cdots C_{a}{ }^{n}\left\{n_{1}, l_{1}\right\}\left[N\left\{S_{n+1} \pm\left(t_{n+1}\right) f^{n}\left\{n_{p}, l_{p} ; \cdots\right\} O^{n}\left\{\left\{n_{p}, l_{p} ; \cdots\right\}\right\}\right\}\right. \\
& \left.+\sum_{l_{p+1}} C_{a}{ }^{n+1}\left\{n+1, l_{p+1} \mid n_{p}, l_{p} ; \cdots\right\} f^{n+1}\left\{n+1, l_{p+1} ; n_{p}, l_{p} ; \cdots\right\} O^{n+1}\left\{\left\{n+1, l_{p+1} ; n_{p}, l_{p} ; \cdots\right\}\right\}\right]|a\rangle, \quad \text { (4.33) }
\end{aligned}
$$
where
$$
N\left\{S_{n+1} \pm\left(t_{n+1}\right) f^{n}\left\{n_{p}, l_{p} ; \cdots\right\} O^{n}\left\{\left\{n_{p}, l_{p} ; \cdots\right\}\right\}\right\}=f^{n+1}\left\{n_{p}, l_{p} ; \cdots\right\} O^{n+1}\left\{\left\{n_{p}, l_{p} ; \cdots\right\}\right\},
$$
and contractions appearing under the summation
$$
\sum_{l_{p+1}}
$$
are with the newly added operator $S_{n+1} \pm(t_{n+1})$. Hence (4.32) and (4.33) can be written in the form of (4.30), where $n$ is replaced by $n+1$. This proves the theorem.

It is evident that the method described in this section can be extended easily to the case where the perturba- tion $H_{I}$ includes the $z$ components $S_{h}^{z}$ , since the opera tors $S_{h}^{z}$ in the time-ordered product can be replaced by expectation values. This replacement should take place after a particular set of contractions and the corre- sponding diagrams have been assigned, since then the spin deviation of atom $h$ at that time is known. After this replacement the contractions may be carried out.

## 5. THE ANTIFERROMAGNETIC GROUND STATE

As an application of the cumulant expansion method for spins developed here, we shall calculate the energy of the antiferromagnetic ground state. We assume the two-sublattice structure such that the nearest neighbors of an atom on sublattice $[A]$ are on sublattice $[B]$ and vice versa. Let $\mathbf{S}_{A_{h}}$ and $\mathbf{S}_{B_{k}}$ be spin operators of atoms of types $A$ and $B$, respectively, and assume that the values of spins $|\mathbf{S}_{A_{h}}|$ in $[A]$ are all equal to $\hbar j_{A}$ and that $|\mathbf{S}_{B_{k}}|=\hbar j_{B}$. The number of atoms on each sublattice is $N$.

We assume the dynamical properties of the spin system to be described by the anisotropic exchange Hamiltonian:
$$
\begin{aligned}
H=2 J & \sum_{\langle h k\rangle}\left[S_{A_{h}}{ }^{z(c)} S_{B_{k}}{ }^{z(c)}\right. \\
& \left.+(1-\gamma)\left(S_{A_{h}}{ }^{x(c)} S_{B_{k}}{ }^{x(c)}+S_{A_{h}}{ }^{y(c)} S_{B_{k}}{ }^{y(c)}\right)\right], \quad(5.1)
\end{aligned}
$$
where $J>0$ and $\langle h k\rangle$ runs over all pairs of nearest neighbor atoms. The Hamiltonian (5.1) is the Heisenberg model for $\gamma=0$ and the Ising model for $\gamma=1$. In (5.1), the components of $\mathbf{S}_{A_{h}}$ and $\mathbf{S}_{B_{k}}$ are defined in a common coordinate fixed in the lattice and denoted by $x(c)$ etc. However, it is convenient in our discussion to rotate the coordinates $180^{\circ}$ around the $x$ axis at every atomic site in sublattice $[B]$. This yields the following transformation in the components of spin operators:
$$
\left\{\begin{array} { l } 
{ S _ { A } { } ^ { z ( c ) } = S _ { A } { } ^ { z }, } \\
{ S _ { A } { } ^ { + ( c ) } = S _ { A } { } ^ { + }, } \\
{ S _ { A } { } ^ { - ( c ) } = S _ { A } { } ^ { - }, }
\end{array} \quad \left\{\begin{array}{l}
S_{B}{ }^{z(c)}=-S_{B}{ }^{z}, \\
S_{B}{ }^{+(c)}=S_{B}{ }^{-}, \\
S_{B}{ }^{-(c)}=S_{B}{ }^{+}.
\end{array}\right.\right.
\quad(5.2)
$$

Use of the explicit expression (4.29) for $P_{2 p}{ }^{n}$ and the corollary (4.28) in $S_{n+1} \pm(t_{n+1}) P_{2 p}{ }^{n}|a\rangle$ yields

In this alternating coordinate system, $^{17}$ the Hamiltonian is written as
$$
\begin{aligned}
H=-2 J \sum_{\langle h k\rangle} & S_{A_{h}}{ }^{z} S_{B_{k}}{ }^{z}+(1-\gamma) J \\
& \times \sum_{\langle h k\rangle}\left(S_{A_{h}}{ }^{+} S_{B_{k}}{ }^{+}+S_{A_{h}}{ }^{-} S_{B_{k}}{ }^{-}\right). \quad(5.3)
\end{aligned}
$$

Let us divide the Hamiltonian into two parts $H_{0}$ and $H_{I}$ as follows:
$$
H=H_{0}+\lambda H_{I}, \quad(5.4 \mathrm{a})
$$

$$
H_{0}=-2 J \sum_{\langle h k\rangle} S_{A_{h}}{ }^{z} S_{B_{k}}{ }^{z}, \quad(5.4 \mathrm{~b})
$$

$$
H_{I}=(1-\gamma) J \sum_{\langle h k\rangle}\left(S_{A_{h}}{ }^{+} S_{B_{k}}{ }^{+}+S_{A_{h}}{ }^{-} S_{B_{k}}{ }^{-}\right), \quad(5.4 \mathrm{c})
$$
where the unperturbed Hamiltonian $H_{0}$ represents the Ising interaction and the perturbation introduces spin flips. This form of the Hamiltonian is a simplification of the one considered in Sec. 4 and will be obtained from(4.2) and (4.3) by assuming that $\lambda_{h}=0$ and $J_{h k}=J$ when atom $A_{h}$ is a nearest neighbor of atom $B_{k}$, but $J_{h k}=0$ otherwise.

The eigenfunctions of $H_{0}$ are
$$
\left|m_{A_{1}}, m_{A_{2}}, \cdots, m_{B_{1}}, m_{B_{2}}, \cdots\right\rangle,
$$

17 M. H. Boon (Ref. 12), and Y. L. Wang and H. B. Callen (Ref. 7) have used the same coordinate system.

where $\hbar m_{A_h}$ and $\hbar m_{B_k}$ are the $z$-projection quantum numbers of $S_{A_h}$ and $S_{B_k}$, respectively, in the alternating coordinate system. The ground state of $H_0$ is
$$|0\rangle\equiv|-j_A,-j_A,\cdots,-j_B,-j_B,\cdots\rangle,\quad(5.5)$$
and is antiferromagnetic. Since
$$S_{A_h}^{-}|0\rangle=S_{B_k}^{-}|0\rangle=0,\quad\text{for all }h\text{ and }k,\quad(5.6)$$
the state $|0\rangle$ is the vacuum state considered in Sec. 4.

We note that the transformation of the coordinate system introduced in (5.2) does not alter the form of the commutation relations in (4.5) since a nonvanishing contribution appears only when the two operators belong to a single atom.

## 6. THE CUMULANTS FOR THE GROUND-STATE ENERGY

To demonstrate the procedure for calculating the successive terms in the ground-state energy expansion (3.9), we consider one of the 4th order terms which results from inserting the Hamiltonian (5.4c),
$$
\begin{aligned}
4\left[\frac{(1-\gamma) J}{i \hbar}\right]^{4} & \lim _{\alpha \rightarrow+0} \frac{i \hbar \alpha}{4} \sum_{3} \sum_{2} \sum_{1} \int_{-\infty}^{0} d t_{4} \int_{-\infty}^{t_{4}} d t_{3} \\
& \times \int_{-\infty}^{t_{3}} d t_{2} \int_{-\infty}^{t_{2}} d t_{1}\left[\exp \alpha\left(t_{1}+t_{2}+t_{3}+t_{4}\right)\right] \\
& \times\left\langle 0\left|S_{A_{4}}-\left(t_{4}\right) S_{B_{4}}-\left(t_{4}\right) S_{A_{3}}-\left(t_{3}\right) S_{B_{3}}-\left(t_{3}\right)\right.\right. \\
& \left.\times S_{A_{2}}+\left(t_{2}\right) S_{B_{2}}+\left(t_{2}\right) S_{A_{1}}+\left(t_{1}\right) S_{B_{1}}+\left(t_{1}\right)\right| 0\right\rangle_{\text {cumul }}.
\end{aligned}
$$

Each of the summations is over all pairs of neighboring atoms $A_{i}$ and $B_{i}$. The factor 4 on the left results from $\lambda \partial\left(\lambda^{4}\right) / \partial \lambda$ in (3.9) and the upper limits of the time integrations replace the denominator factor 4! in (3.9). The other 4th-order terms have different numbers or sequences of $S^{+}$and $S^{-}$pairs.

Application of Wick's theorem decomposes a time-ordered product into the sum of all combinations of a normal product multiplied by $C_{0}^{n}\{m, l \mid \cdots\}$'s coming from the contraction of a pair $S_{m}{ }^{-}\left(t_{m}\right), S_{l}{ }^{+}\left(t_{l}\right)$. Such a contraction vanishes unless the sites $m$ and $l$ are the same and $t_{m}>t_{l}$. The nonzero combinations can be represented in a familiar way by diagrams. If time increases to the left, $S^{+}$and $S^{-}$will be denoted by right $(\bigcirc)$ and left $(\times)$ termini, respectively, of horizontal line segments showing the propagation in time of a spin deviation on an atom. Lines at different levels will represent different atoms and, whenever possible, neighboring atoms will be shown on neighboring lines. A contraction will give a finite segment terminated at each end while an $S^{ \pm}(t)$ in the normal product will give a segment open on the left (right) and terminated at $t$. In the perturbation expansion each terminus is connected with a like terminus on a neighboring atom to form a spin-pair excitation or de-excitation, both of which are represented as a zigzag vertical line. Each diagram will be a set of one or more subclusters with vertical and horizontal sides. A subcluster is a set of termini which are connected by (de-) excitation lines or contractions but disconnected from any other terminus in the diagram. Here overlapping contractions are not considered to be connected to each other.

If we restrict ourselves now to the vacuum-state matrix elements in (3.9), only complete contractions contribute and the diagrams consist of closed subclusters only. Figures 3(a) and 3(b) show the nonzero contribution from a time-ordered product in (6.1) for which $A_{1}=A_{2}, B_{1} \neq B_{2}$. Figure 3(a) contains two subclusters and Fig. 3(b) contains one. The respective contractions are
$$
\begin{aligned}
K_{a}=\dot{S}_{A_{4}}^{\prime}-\left(t_{4}\right) \dot{S}_{B_{4}}^{\prime}-\left(t_{4}\right) \ddot{S}_{A_{3}}-\left(t_{3}\right) \dot{S}_{B_{3}}-\left(t_{3}\right) \ddot{S}_{A_{2}}^{\prime}+\left(t_{2}\right) & \\
& \times \dot{S}_{B_{2}}^{\prime}+\left(t_{2}\right) \ddot{S}_{A_{1}}+\left(t_{1}\right) \dot{S}_{B_{1}}+\left(t_{1}\right), \quad(6.2 \mathrm{a})
\end{aligned}
$$
and
$$
\begin{aligned}
K_{b}=\ddot{S}_{A_{4}}^{\prime}-\left(t_{4}\right) \dot{S}_{B_{4}}^{\prime}-\left(t_{4}\right) \ddot{S}_{A_{3}}-\left(t_{3}\right) \dot{S}_{B_{3}}-\left(t_{3}\right) \ddot{S}_{A_{2}}+\left(t_{2}\right) & \\
& \times \dot{S}_{B_{2}}^{\prime}+\left(t_{2}\right) \ddot{S}_{A_{1}}^{\prime}+\left(t_{1}\right) \dot{S}_{B_{1}}+\left(t_{1}\right). \quad(6.2 \mathrm{~b})
\end{aligned}
$$

The sequence of the contractions in the sense of (4.29) is to be taken in the order of $\cdot, \cdot,{ }^{\prime}$, and $\cdots$. If $A_{1}=A_{2}$ and $B_{1}=B_{2}$ there are two additional nonzero diagrams.

The numerical value of $K_{a}$ is the product of the four $C_{0}^{8}$ factors
$$
\begin{aligned}
C_{0}^{8}\left\{B_{3}, B_{1}\right\} & =F_{B_{3} A_{2}}-+F_{B_{3} A_{1}}-+G_{B_{3} B_{1}}-+\delta_{B_{3} B_{1}} \\
& =2 j_{A} \hbar^{2} \exp \left[2 i \hbar J\left(2 t_{3}-t_{2}-t_{1}\right)\right] \exp \left[-(i / \hbar) \epsilon_{B}\left(t_{3}-t_{1}\right)\right] \delta_{B_{3} B_{1}},
\end{aligned}
$$

$$
\begin{aligned}
C_{0}^{8}\left\{A_{3}, A_{1} \mid B_{3}, B_{1}\right\} & =F_{A_{3} B_{2}}-+G_{A_{3} A_{1}}-+\delta_{A_{3} A_{1}} \\
& =2 j_{A} \hbar^{2} \exp \left[2 i \hbar J\left(t_{3}-t_{2}\right)\right] \exp \left[-(i / \hbar) \epsilon_{A}\left(t_{3}-t_{1}\right)\right] \delta_{A_{3} A_{1}},
\end{aligned}
$$

$$
\begin{aligned}
C_{0}^{8}\left\{B_{4}, B_{2} \mid A_{3}, A_{1} ; B_{3}, B_{1}\right\} & =F_{B_{4} A_{2}}-+G_{B_{4} B_{2}}-+\delta_{B_{4} B_{2}} \\
& =2 j_{B} \hbar^{2} \exp \left[2 i \hbar J\left(t_{4}-t_{2}\right)\right] \exp \left[-(i / \hbar) \epsilon_{B}\left(t_{4}-t_{2}\right)\right] \delta_{B_{4} B_{2}},
\end{aligned}
$$

$$
\begin{aligned}
C_{0}^{8}\left\{A_{4}, A_{2} \mid B_{4}, B_{2} ; A_{3}, A_{1} ; B_{3}, B_{1}\right\} & =G_{A_{4} A_{2}}-+\delta_{A_{4} A_{2}} \\
& =2 j_{A} \hbar^{2} \exp \left[-(i / \hbar) \epsilon_{A}\left(t_{4}-t_{2}\right)\right] \delta_{A_{4} A_{2}},
\end{aligned}
$$
(6.3d)

where
$$\epsilon=\epsilon_{A}+\epsilon_{B}, \quad \epsilon_{A, B}=2 z j_{B, A} J \hbar^{2},\qquad(6.4)$$
and $z$ is the coordination number.

In each of the time intervals $t_{21}, t_{32}, t_{43}$ of Fig. 3(a), the phase term for a given contraction contains the energy of forming that spin deviation in the presence of the spin configuration generated by the as yet uncontracted $S^{+}$ operators preceding that interval. A general rule is that in the product of the $C_{0}^{n}$'s the energy for each time interval will be the total spin-deviation energy, which is given by
$$\text { the value of }\left(H_{0}-E_{0}\right)=p \epsilon-2 q \hbar^{2} J, \quad(6.5)$$
where $2 p$ is the number of spin deviations and $q$ is the number of interactions among the spin deviations which exist during that time interval. By definition, one spin deviation is created by $S^{+}$. In Fig. 3(a) the two spin deviations on $A_{1}$ in the interval $t_{32}$ each interact with the deviations on $B_{1}$ and $B_{2}$ , giving $q=4$ .
$$\left\langle 0\left|Y_{1}\right| 0\right\rangle=4 j_{A} j_{B} \hbar^{4} \exp \left[-(i / \hbar)\left(\epsilon-2 \hbar^{2} J\right)\left(t_{3}-t_{1}\right)\right],\qquad(6.8a)$$

$$\left\langle 0\left|Y_{2}\right| 0\right\rangle=4 j_{A} j_{B} \hbar^{4} \exp \left[-(i / \hbar)\left(\epsilon-2 \hbar^{2} J\right)\left(t_{4}-t_{2}\right)\right].\qquad(6.8b)$$

The product in (6.7) is the cumulant correction to $K_{a}$ in the sense of (2.3).
When the time integrations in (6.1) are done, each intermediate state gives the value of $[(i / \hbar)(H_{0}-E_{0})]^{-1}$ , and the $4 \alpha$ is canceled by the last time integral. Figure 3(a) contributes
$$\begin{aligned}
-[(1-\gamma) J \hbar]^{4} \sum_{A_{1}} \sum_{B_{1}, B_{2}}^{\prime}\left[\left(\epsilon-2 \hbar^{2} J\right)\left(2 \epsilon-8 \hbar^{2} J\right)\left(\epsilon-2 \hbar^{2} J\right)\right]^{-1}\left(4 j_{A} j_{B} \hbar^{2}\right)^{2} & \\
& =-N z(z-1)\left[(1-\gamma) J \hbar\right]^{4}\left(4 j_{A} j_{B} \hbar^{2}\right)^{2}\left(\epsilon-2 \hbar^{2} J\right)^{-2}\left(2 \epsilon-8 \hbar^{2} J\right)^{-1}, \quad(6.9)
\end{aligned}$$
where $\sum'$ means that $B_{1}=B_{2}$ is excluded in the summation.

It is important to notice that, because of the re- striction $t_{4}>t_{3}>t_{2}>t_{1}$ in the time integrations, the cumulant correction no longer appears as a product as
![](./images/813150498176630785_3.jpg)

FIG. 3. Two diagrams belonging to a configuration in the fourth-order terms.

The prephase factor for a contraction with interval tmt is obtained from the prescription for (4.29) and is equal to
$$2 \hbar^{2}\left(j_{A, B}-n\right), \quad(6.6)$$
where n is the number of contractions for the same atom which contain the entire interval $t_{m l}$ . For $K_{a}$ these values are $2 j_{B} \hbar^{2}, 2 j_{A} \hbar^{2}, 2 j_{B} \hbar^{2}, 2 j_{A} \hbar^{2}$ , and for $K_{b}$ they are $2 j_{B} \hbar^{2}, 2(j_{A}-1) \hbar^{2}, 2 j_{B} \hbar^{2}, 2 j_{A} \hbar^{2}$ , as can be seen from inspection of Fig. 3(b). This rule as well as the rule in the preceding paragraph for the phase is now inde- pendent of the order in which a set of contractions is carried out.
The cumulant contribution of Fig. 3(a) is propor- tional to
$$K_{a}-\left\langle 0\left|Y_{1}\right| 0\right\rangle\left\langle 0\left|Y_{2}\right| 0\right\rangle,\qquad(6.7)$$
where $Y_{1}$ is the time-ordered product for the $A_{1} B_{1}$ sub cluster alone and $Y_{2}$ is for the $A_{1} B_{2}$ subcluster alone, so that it does in (6.7). The intermediate state energies are now calculated by
$$\text { the value of }\left(H_{0}-E_{0}\right)=p \epsilon-2 q^{\prime} \hbar^{2} J, \quad(6.10)$$
where q' is counted by regarding the subclusters $Y_{1}$ and $Y_{2}$ as spatially separated and hence differs from q in(6.5). This is the consequence of the separate averaging processes for $Y_{1}$ and $Y_{2}$ described in (6.7) to (6.8). Because of (6.10), the cumulant correction to (6.9) is a similar term with $(2 \epsilon-4 \hbar^{2} J)^{-1}$ replacing the last factor on the right. This correction term is comparable with the original.
Note that, since the intermediate states of Figs. 3(a) and 3(b) are identical, their spin factors combine to replace $(2 j_{A} \hbar)^{2}(2 j_{B} \hbar)^{2}$ in (6.9) by
$$\left(2 j_{B} \hbar\right)^{2} 2!\left(2 j_{A} \hbar\right)\left\{\left(2 j_{A}-1\right) \hbar\right\}, \quad(6.11)$$
in agreement with the result obtained by the usual formulas for the matrix element of
$$S_{B_{1}}-S_{B_{1}}+S_{B_{2}}-S_{B_{2}}+\left(S_{A_{1}}-\right)^{2}\left(S_{A_{1}}+\right)^{2}. \quad(6.12)$$

A set of diagrams like Figs. 3(a) and 3(b) with the same arrangement of $S^{+}$ and $S^{-}$ operators in space and time will be represented by a single configuration. The diagrams of a configuration will differ only in the

![](./images/813150498176630785_4.jpg)

FIG. 4. The second-order diagram.

combinations of overlapping contractions, but may have different numbers of subclusters and therefore different types of cumulant corrections.

The calculation of the $n$th order term $E_{n}$ in (3.10) for the ground-state energy is summarized below. For the form of $H_{I}$ in (5.4c), only even $n$'s contribute.

(1) Draw all interacting configurations consisting of $\frac{1}{2} n$ pair excitation and $\frac{1}{2} n$ pair de-excitation lines in a definite time sequence $t_{n}>\cdots>t_{1}$ and with a horizontal line indicating the existence of the spin deviations on each site. Here two spin-deviation lines are considered interacting if they coexist on neighboring sites. This introduces the factor $[(1-\gamma) J]^{n}$.

(2) The diagrams corresponding to a configuration are obtained by drawing all possible contractions for the given spin deviations. Overlapping spin deviations form more than one set of contractions.

(3) For the numerical value of a diagram before cumulant corrections: (a) Multiply by the inverse of the value of $E_{0}-H_{0}$ given in (6.5) for each intermediate state. (b) Multiply by a factor $2 \hbar^{2}(j_{A, B}-n)$ given in (6.6) for each contraction.

(4) For the cumulant correction for a diagram with more than one subcluster first form all distinct parti- tions of the diagram into subdiagrams composed of one or more subclusters. The subdiagrams are treated as spatially separated from one another. For each parti- tion: (a) Multiply by the inverse of the value of $E_{0}-H_{0}$ given in (6.10) for each intermediate state. (b) Apply 3(b) to each subdiagram and multiply together. (c) Multiply by the factor $(-)^{l-1}(l-1)$ ! coming from (2.3). Sum over all partitions and add to (3).

(5) For each type of diagram, multiply the result of (3) and (4) by $Nz$ as well as by the number of times the diagram appears in the crystal with a given $A_{1} B_{1}$ pair.

## 7. RESULTS AND DISCUSSION
### A. The Ground-State Energy
By using the prescriptions (1) to (5) just described, we have calculated the energy of the antiferromagnetic ground state up to the fourth order in the perturbation expansion. Configurations involved in this calculation are shown in Figs. 4 and 5 but, for simplicity, the different possible contractions are not shown. The result is written as
$$\begin{aligned}
E=E_{0}+E_{2}+E_{4}+\cdots= & -\left(J z N \hbar^{2}\right)\left(2 j_{A} j_{B}\right) \\
& \times\left[1+c_{1}(1-\gamma)^{2}+c_{2}(1-\gamma)^{4}+\cdots\right], \quad(7.1)
\end{aligned}$$
where
$$c_{1}=2\left(\epsilon_{0}-2\right)^{-1}, \quad(7.2 \mathrm{a})$$

$$\begin{aligned}
c_{2}=4\{ & (z-1)^{2}-\mathcal{Q}\}\left(d_{1}-d_{6}\right)+2 \mathcal{Q}\left(d_{2}-d_{0}+d_{2^{\prime}}\right) \\
& \left.+2(z-1)\left(d_{3}+d_{4}-2 d_{6}\right)+\left(d_{5}-2 d_{6}\right), \quad(7.2 \mathrm{~b})\right.
\end{aligned}$$

$$\epsilon_{0}=2 z\left(j_{A}+j_{B}\right) ; \quad(7.3)$$
and
$$\begin{aligned}
& d_{1}=\left(4 j_{A} j_{B}\right)\left(\epsilon_{0}-2\right)^{-2}\left(\epsilon_{0}-3\right)^{-1}, \\
& d_{2}=d_{2^{\prime}}=\left(4 j_{A} j_{B}\right)\left(\epsilon_{0}-2\right)^{-2}\left(\epsilon_{0}-4\right)^{-1}, \\
& d_{3}=2\left(2 j_{A}-1\right)\left(2 j_{B}\right)\left(\epsilon_{0}-2\right)^{-2}\left(\epsilon_{0}-4\right)^{-1}, \\
& d_{4}=2\left(2 j_{B}-1\right)\left(2 j_{A}\right)\left(\epsilon_{0}-2\right)^{-2}\left(\epsilon_{0}-4\right)^{-1}, \\
& d_{5}=2\left(2 j_{A}-1\right) 2\left(2 j_{B}-1\right)\left(\epsilon_{0}-2\right)^{-2}\left(\epsilon_{0}-4\right)^{-1}, \\
& d_{6}=\left(4 j_{A} j_{B}\right)\left(\epsilon_{0}-2\right)^{-3}.
\end{aligned}\qquad(7.4)$$

The factor $z N Q$ is the total number of closed chains containing four distinct atoms $A_{1}, B_{1}, A_{2}$ , and $B_{2}$ , arranged such that each one is a nearest neighbor to two others. This is different from the $Q$ used by Davis. The terms $d_{1}$ to $d_{5}$ come from the corresponding diagrams in Fig. 5 and the $d_{6}$ is the cumulant correction term. In Fig. 5, two horizontal lines linked by a dashed line represent nearest-neighbor atoms in the lattice, while the double-headed arrows mean that the diagrams obtained by interchanging the times of the indicated pairs should also be included.

The coefficients $c_{1}$ and $c_{2}$ as well as the energy $E$ are calculated using (7.1) to (7.4) for the lattices of interest and with values of $j_{A}=j_{B}=\frac{1}{2}, 1, \frac{3}{2}, 2, \frac{5}{2}$ . The results are compared with those obtained by Davis and Boon in Tables I and II.

The difference between our values of $c_{2}$ and those of Davis can be explained as follows: The unperturbed Hamiltonian used by Davis is the "independent boson" part in the Schwinger representation and is the part of $H_{0}$ which is linear in the spin deviations, $\delta S_{i}^{z}=\hbar j_{i}-S_{i}^{z}$ , so that
$$H_{0}=H_{0 D}-2 J \sum_{\langle h k\rangle} \delta S_{A_{h}}{ }^{z} \delta S_{B_{k}}{ }^{z}.\qquad(7.5)$$

The quadratic terms in (7.5) gives the $2 q \hbar^{2} J$ in (6.5)

<table><thead><tr><td colspan="10"><b>Table I. Values of$C_{1}$and$C_{2}$as functions of the lattice and the magnitude of the spin.</b></td></tr><tr><td><b>Lattice</b></td><td><b>a</b></td><td><b>Authora</b></td><td><b>$j=\frac {1}{2}$</b></td><td><b>$j=1$</b></td><td><b>$j=\frac {3}{2}$</b></td><td><b>$j=2$</b></td><td><b>$j=\frac {5}{2}$</b></td></tr></thead><tbody><tr><td rowspan="4"><b>Chain Plane</b></td><td rowspan="4"></td><td rowspan="4"></td><td colspan="5"><b>$C_{1}$</b></td></tr><tr><td><b>1.0000</b></td><td><b>0.3333</b></td><td><b>0.2000</b></td><td><b>0.1429</b></td><td><b>0.1111</b></td></tr><tr><td><b>0.3333</b></td><td><b>0.1429</b></td><td><b>0.0909</b></td><td><b>0.0667</b></td><td><b>0.0526</b></td></tr><tr><td><b>0.2000</b></td><td><b>0.0909</b></td><td><b>0.0588</b></td><td><b>0.0435</b></td><td><b>0.0345</b></td></tr><tr><td><b>bcc</b></td><td></td><td></td><td><b>0.1429</b></td><td><b>0.0667</b></td><td><b>0.0435</b></td><td><b>0.0323</b></td><td><b>0.0256</b></td></tr><tr><td rowspan="8"><b>Chain</b></td><td rowspan="4"><b></b></td><td rowspan="2"><b>Present work</b></td><td colspan="5"><b>$C_{2}$</b></td></tr><tr><td><b>-0.2500</b></td><td><b>0.0426</b></td><td><b>0.0300</b></td><td><b>0.0229</b></td><td><b>0.0185</b></td></tr><tr><td rowspan="2"><b>Davis</b></td><td><b>-0.4590</b></td><td><b>0.0292</b></td><td><b>0.0284</b></td><td><b>0.0226</b></td><td><b>0.0184</b></td></tr><tr><td rowspan="2"><b>Present work</b></td><td><b>—0.0019</b></td><td><b>0.0126</b></td><td><b>0.0099</b></td><td><b>0.0078</b></td><td><b>0.0065</b></td></tr><tr><td rowspan="2"><b>Davis</b></td><td><b>—0.0098</b></td><td><b>0.0123</b></td><td><b>0.0098</b></td><td><b>0.0078</b></td><td><b>0.0065</b></td></tr><tr><td rowspan="2"><b>Boon</b></td><td><b>0.0988</b></td><td><b>0.0002</b></td><td><b>…</b></td><td><b>…</b></td><td><b>…</b></td></tr><tr><td rowspan="2"><b>Present work</b></td><td><b>—0.0007</b></td><td><b>0.0055</b></td><td><b>0.0045</b></td><td><b>0.0037</b></td><td><b>0.0031</b></td></tr><tr><td rowspan="2"><b>Davis</b></td><td><b>—0.0015</b></td><td><b>0.0054</b></td><td><b>0.0045</b></td><td><b>0.0037</b></td><td><b>0.0031</b></td></tr><tr><td rowspan="2"><b>Boon</b></td><td><b>0.0344</b></td><td><b>0.0006</b></td><td><b>…</b></td><td><b>…</b></td><td><b>…</b></td></tr><tr><td rowspan="2"><b>Present work</b></td><td></td><td><b>0.0049</b></td><td><b>0.0050</b></td><td><b>0.0037</b></td><td><b>0.0029</b></td><td><b>0.0024</b></td></tr><tr><td rowspan="2"><b>Davis</b></td><td><b>0.0047</b></td><td></td><td><b>0.0050</b></td><td><b>0.0037</b></td><td><b>0.0029</b></td><td><b>0.0024</b></td></tr><tr><td><b>Boon</b></td><td><b>0.0088</b></td><td><b>0.0004</b></td><td><b>…</b></td><td><b>…</b></td><td><b>…</b></td></tr></tbody></table>

a The three methods give exactly the same values for the trivial term $c_{1}$ .

<table>
<caption>Table II. Ground-state energy of spins of magnitude one-half coupled by the isotropic exchange interaction, $\gamma$=0, in units of $-J_{z}N\hbar^{2}/2$.</caption>
<thead>
<tr>
<th>Lattice</th>
<th>Present work</th>
<th>Davisa</th>
<th>Boonb</th>
<th>Marshallc</th>
<th>Oguchid</th>
<th>Spin wavee</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chainf</td>
<td>1.750</td>
<td>1.736 (1.541)g</td>
<td>$\cdots$</td>
<td>1.631</td>
<td>1.692</td>
<td>1.726</td>
</tr>
<tr>
<td>Plane</td>
<td>1.331</td>
<td>1.328 (1.324)g</td>
<td>1.432</td>
<td>1.312</td>
<td>1.286</td>
<td>1.316</td>
</tr>
<tr>
<td>sc</td>
<td>1.199</td>
<td>1.200 (1.199)g</td>
<td>1.234</td>
<td>1.203</td>
<td>1.183</td>
<td>1.194</td>
</tr>
<tr>
<td>bcc</td>
<td>1.148</td>
<td>1.148 (1.148)g</td>
<td>1.152</td>
<td>1.157</td>
<td>1.134</td>
<td>1.146</td>
</tr>
</tbody>
</table>
<p>a Reference 6.
b Reference 12.
c W. Marshall, Proc. Roy. Soc. (London) A232, 48 (1955).
d T. Oguchi, J. Phys. Chem. Solids 24, 1049 (1963). Also see J. C. Fisher, ibid. 10, 44 (1959).
e P. W. Anderson, Phys. Rev. 86, 694 (1952); R. Kubo, ibid. 87, 568 (1952).
f The exact value for the energy of the linear chain has been calculated as 1.7726 by L. Hulthén, Arkiv Mat. Astron. Fysik 26A, No. 1 (1938).
g The values obtained by keeping only $c_1$ and $c_2$ but neglecting $c_3$. Those values should be compared directly with our results.</p>

and (6.10) can be included to infinite order in his perturbation expansion as Davis indicates.¹⁸ For some reason he did this only for the last time interval and considered only the lower order terms in the other intervals. Thus $E_4$, $E_5$, and the first terms in $E_6$ and $E_7$ in his equation (44) correspond to a part of our fourth-order term $E_4$ in (7.1), while the second terms in his $E_6$ and $E_7$ belong to the sixth order term $E_6$ in our notation. Conversely, the terms in (44) of Davis can be generated from the exact expressions (7.1) to (7.4) by retaining one factor $(\epsilon_0 - 2)^{-1}$ and expanding the remaining products $(\epsilon_0 - 2)^{-1}(\epsilon_0 - 3)^{-1}$, $(\epsilon_0 - 2)^{-1}(\epsilon_0 - 4)^{-1}$ and $(\epsilon_0 - 2)^{-2}$ in powers of $\epsilon_0^{-1}$. From Table I and also from the values in parentheses in Table II, we see that the Davis expansion does not converge well for the smaller and $j$ lattice dimension. The $(1 - \gamma)^6$ and higher terms will have products of four factors $(\epsilon_0 - r)^{-1}$ or more so that the expansions will be even worse. Our perturbation expansion is expected to converge more rapidly because of the quadratic terms included in $H_0$, and this is seen especially for the linear chain in Table II. The differences between our values and Boon's values of $c_2$ seem to be due to errors in his formulas (74).

![](./images/813150498176630785_5.jpg)
<p>Fig. 5. All possible configurations in the fourth-order terms.</p>

¹⁸ It is also possible to include the full interaction
$$-2J\sum_{\langle hk\rangle}S_{A_h}{}^zS_{B_k}{}^z$$
in the unperturbed Hamiltonian using the Schwinger representation. See Ref. 15.

## B. The Long- and Short-Range Order
The long-range order is defined by
$$
\begin{aligned}
\xi= & \frac{1}{2}\left[\left(N j_{A} \hbar\right)^{-1}\left\langle\sum_{h=1}^{N} S_{A_{h}}{ }^{z}\right\rangle+\left(N j_{B} \hbar\right)^{-1}\left\langle\sum_{k=1}^{N} S_{B_{k}}{ }^{z}\right\rangle\right] \\
= & 1-\frac{1}{2}\left[\left(N j_{A} \hbar\right)^{-1}\left\langle\sum_{h=1}^{N} \delta S_{A_{h}}{ }^{z}\right\rangle+\left(N j_{B} \hbar\right)^{-1}\left\langle\sum_{k=1}^{N} \delta S_{B_{k}}{ }^{z}\right\rangle\right], \\
& (7.6)
\end{aligned}
$$
where $\langle\cdots\rangle$ denotes an average with respect to the exact ground state. The value of
$$\left\langle\sum_{h=1}^{N} \delta S_{A_{h}}{ }^{z}\right\rangle$$
can be found by differentiating the energy expression $E=\langle H\rangle$ with respect to $\epsilon_A/\hbar$, keeping $J$ fixed, since $\epsilon_A \to \epsilon_A+\alpha$ is equivalent to introducing an infinitesimal external field term
$$\alpha \sum_{h=1}^{N} \delta S_{A_{h}}{ }^{z}$$
in $H$. From (7.1) and (7.6), therefore,
$$
\xi=1-\left[\left(-\frac{\epsilon_{0}}{2} \frac{\partial c_{1}}{\partial \epsilon_{0}}\right)(1-\gamma)^{2}+\left(-\frac{\epsilon_{0}}{2} \frac{\partial c_{2}}{\partial \epsilon_{0}}\right)(1-\gamma)^{4}+\cdots\right],
$$
where the $\left[-(\epsilon_0/2)(\partial c_i/\partial \epsilon_0)\right]$ for $i=1$ and $2$ are given in Table III as functions of the lattice of interest and the magnitude of the spin.

<table>
<caption>Table III. Values of $\left[-(\epsilon_0/2)(\partial c_i/\partial \epsilon_0)\right]$ for $i=1$ and $2$ as functions of the lattice and the magnitude of the spin.</caption>
<thead>
<tr>
<th>Lattice</th>
<th>Authorsa</th>
<th>$j=\frac{1}{2}$</th>
<th>$j=1$</th>
<th>$j=\frac{3}{2}$</th>
<th>$j=2$</th>
<th>$j=\frac{5}{2}$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">$-\frac{\epsilon_0}{2}\frac{\partial c_1}{\partial \epsilon_0}$</td>
</tr>
<tr>
<td>Chain</td>
<td></td>
<td>1.0000</td>
<td>0.2222</td>
<td>0.1200</td>
<td>0.0816</td>
<td>0.0617</td>
</tr>
<tr>
<td>Plane</td>
<td></td>
<td>0.2222</td>
<td>0.0816</td>
<td>0.0496</td>
<td>0.0356</td>
<td>0.0277</td>
</tr>
<tr>
<td>sc</td>
<td></td>
<td>0.1200</td>
<td>0.0496</td>
<td>0.0311</td>
<td>0.0227</td>
<td>0.0178</td>
</tr>
<tr>
<td>bcc</td>
<td></td>
<td>0.0816</td>
<td>0.0356</td>
<td>0.0227</td>
<td>0.0166</td>
<td>0.0131</td>
</tr>
<tr>
<td colspan="7">$-\frac{\epsilon_0}{2}\frac{\partial c_2}{\partial \epsilon_0}$</td>
</tr>
<tr>
<td>Chain</td>
<td>Present work</td>
<td>0.2500</td>
<td>0.1433</td>
<td>0.0687</td>
<td>0.0458</td>
<td>0.0344</td>
</tr>
<tr>
<td></td>
<td>Davis</td>
<td>−1.1260</td>
<td>0.0873</td>
<td>0.0623</td>
<td>0.0443</td>
<td>0.0340</td>
</tr>
<tr>
<td>Plane</td>
<td>Present work</td>
<td>0.0356</td>
<td>0.0270</td>
<td>0.0181</td>
<td>0.0135</td>
<td>0.0108</td>
</tr>
<tr>
<td></td>
<td>Davis</td>
<td>0.0026</td>
<td>0.0259</td>
<td>0.0180</td>
<td>0.0135</td>
<td>0.0108</td>
</tr>
<tr>
<td>sc</td>
<td>Present work</td>
<td>0.0080</td>
<td>0.0107</td>
<td>0.0079</td>
<td>0.0061</td>
<td>0.0050</td>
</tr>
<tr>
<td></td>
<td>Davis</td>
<td>0.0049</td>
<td>0.0103</td>
<td>0.0078</td>
<td>0.0061</td>
<td>0.0050</td>
</tr>
<tr>
<td>bcc</td>
<td>Present work</td>
<td>0.0129</td>
<td>0.0088</td>
<td>0.0062</td>
<td>0.0047</td>
<td>0.0038</td>
</tr>
<tr>
<td></td>
<td>Davis</td>
<td>0.0120</td>
<td>0.0089</td>
<td>0.0062</td>
<td>0.0047</td>
<td>0.0038</td>
</tr>
</tbody>
</table>
<p>a The two methods give exactly the same values for the trivial term $\left[-(\epsilon_0/2)(\partial c_1/\partial \epsilon_0)\right]$.</p>

The short-range order defined by
$$\eta=\left(N z j_{A} j_{B} \hbar^{2}\right)^{-1}\left\langle\sum_{\langle h k\rangle} S_{A_{h}}{ }^{z} S_{B_{k}}{ }^{z}\right\rangle\qquad(7.8)$$
is written as
$$\eta=-1+c_{1}(1-\gamma)^{2}+3 c_{2}(1-\gamma)^{4}+\cdots, \quad(7.9)$$
where the $c_{i}$ are given by Table I.

The comments given in connection with Table II are again applicable to the comparison of our exact values and Davis's values of the $\left[-(\epsilon_{0} / 2)(\partial c_{2} / \partial \epsilon_{0})\right]$ in Table III. In particular, Davis's expansion seems to fail in the case of a linear chain with spin $\frac{1}{2}$. Without calculating the 6th order terms in perturbation, however, it is not possible to compare our values of $\xi$ and $\eta$ with those of Davis. We note only that, for $\gamma=0$, the exact value of the short-range order $\eta$ given by Orbach $^{19}$ is -0.59, while our result in the 4th order is -0.75 and Davis's value is -1.37 or -0.39 in the 4th or 6th order, respectively.

### C. The Methods of Davis and Boon
The cluster expansions given by Davis and Boon are both obtained by rearrangement of products in each order of the perturbation expansion of $U_{\alpha}(0,-\infty)|0\rangle$ in order to permit the independent summation over factors. The rearranged theory can then be written in an exponential form.

As an example, let us consider a product with two subclusters $Y_{1}$ and $Y_{2}$ corresponding to the upper and lower subclusters in Fig. 3(a). When $A_{1}=A_{2}$, the value $\langle 0|Y_{1+2}| 0\rangle$ is different from the value $\langle 0|Y_{1}| 0\rangle$ $\langle 0|Y_{2}| 0\rangle$ of the two subclusters which are completely separated. Therefore
$$\begin{aligned}
\sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)} Y_{1} Y_{2}|0\rangle= & {\left[\sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)}^{\prime}\left\langle 0\left|Y_{1}\right| 0\right\rangle\left\langle 0\left|Y_{2}\right| 0\right\rangle\right.} \\
& \left.+\sum_{\left(i_{1} i_{2}\right)}\left\langle 0\left|Y_{1+2}\right| 0\right\rangle\right]|0\rangle, \quad(7.10)
\end{aligned}$$

$$\begin{aligned}
\sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)} Y_{1} Y_{2}|0\rangle \to \sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)} & \left\{\left(2 j_{A} \hbar\right)^{2}-2 j_{A} \hbar^{2} \delta_{A_{1} A_{2}}\right\}\left\{\left(2 j_{B} \hbar\right)^{2}-2 j_{B} \hbar^{2} \delta_{B_{1} B_{2}}\right\}|0\rangle \\
= & \sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)}\left(2 j_{A} \hbar\right)^{2}\left(2 j_{B} \hbar\right)^{2}+\sum_{\left(i_{1} i_{2}\right)}\left\{-\left(2 j_{B} \hbar\right)^{2}\left(2 j_{A} \hbar^{2}\right) \delta_{A_{1} A_{2}}\right. \\
& \left.-\left(2 j_{A} \hbar\right)^{2}\left(2 j_{B} \hbar^{2}\right) \delta_{B_{1} B_{2}}+\left(2 j_{A} \hbar^{2}\right)\left(2 j_{B} \hbar^{2}\right) \delta_{A_{1} A_{2}} \delta_{B_{1} B_{2}}\right\}|0\rangle. \quad(7.12)
\end{aligned}$$

Since the first term on the right of (7.12) obviously corresponds to
$$\sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)}\left\langle 0\left|Y_{1}\right| 0\right\rangle\left\langle 0\left|Y_{2}\right| 0\right\rangle,$$
and the second term to
$$\sum_{\left(i_{1} i_{2}\right)}\left\langle 0\left|Y_{1+2}\right| 0\right\rangle_{\text {cumul }},$$
the above expression becomes equivalent to (7.11).

19 R. Orbach, Phys. Rev. 112, 309 (1958).

where
$$\sum_{\left(i_{1} i_{2}\right)}$$
includes all connected diagrams and the corresponding terms are omitted in
$$\sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)}^{\prime}.$$

We remove the restriction on the summation by adding the omitted terms and at the same time replacing $\langle 0|Y_{1+2}| 0\rangle$ by $\langle 0|Y_{1+2}| 0\rangle_{cumul } \equiv\langle 0|Y_{1+2}| 0\rangle-\langle 0|Y_{1}| 0\rangle$ $\times\langle 0|Y_{2}| 0\rangle$ , that is,
$$\begin{aligned}
\sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)}^{\prime} Y_{1} Y_{2}|0\rangle= & \sum_{\left(i_{1}\right)} \sum_{\left(i_{2}\right)}\left\langle 0\left|Y_{1}\right| 0\right\rangle\left\langle 0\left|Y_{2}\right| 0\right\rangle \\
& +\sum_{\left(i_{1} i_{2}\right)}\left\langle 0\left|Y_{1+2}\right| 0\right\rangle_{\text {cumul }}. \quad(7.11)
\end{aligned}$$

Boon used spin operators directly, but applied time- independent perturbation theory apparently to avoid the explicit use of Wick's theorem for spin operators. The time-independent formulation complicates the discussion but, since his unperturbed Hamiltonian is the same as ours, the results should agree with ours except for mistakes, possibly, in his counting of diagrams.

Davis handles the cumulant corrections by using indicator $\delta$ functions for the confluence of spin sites. In his representation each spin line in $Y_{1}$ and $Y_{2}$ has the value $2 j_{A, B} \hbar$ . The product of the values of the spin lines for $A_{1}$ and $A_{2}$ is therefore $(2 j_{A} \hbar)^{2}$ when $A_{1} \neq A_{2}$ , but becomes $2 j_{A}(2 j_{A}-1) \hbar^{2}$ , when $A_{1}=A_{2}$ , which he writes $(2 j_{A} \hbar)^{2}-2 j_{A} \hbar^{2} \delta_{A_{1} A_{2}}$ . Doing the same for $B_{1}$ and $B_{2}$ gives

Davis did not give a diagrammatic representation ofhis procedure. This was supplied by Wang and Callen, $^{7}$  who draw each nonzero $\delta$ function as a "lock" between spin lines. Thus our cumulants are constructed directly in terms of linked diagrams which consist of a single subcluster or subclusters linked together by locks. The indicator $\delta$ functions also operate in a subcluster like that in Fig. 3(b), not to give a cumulant but to correct the value of the product of overlapping internal spin lines.

There is a trivial difference between the value

assigned by us to a set of contractions and that given by Wang and Callen in their Eq. (25), even when we use their unperturbed Hamiltonian $(=H_{0 D})$. For Fig. 3(a) with $A_{1}=A_{2}$ we have $(2 j \hbar)^{2}$ and for Fig. 3(b) we have $2 j(2 j-2) \hbar^{2}$ while their values are $(2 j)(2 j-1) \hbar^{2}$ for each. For a given configuration the totals are the same. The difference arises from the use of spin operators and boson operators, respectively.

In Schwinger's representation the indicator functions can be considered as cumulants of the $u$-boson products which appear because the ground state of these bosons is occupied. $^{20}$ To define the subclusters in this case, we need the notion of a contraction of a $u$ operator with the ground state which is represented by a line connecting those two. In addition there will be the ordinary u contractions. Each line now is a subcluster by itself whose value depends on other overlapping lines in a manner similar to the method of Wang and Callen. It can be shown that their locks are in fact cumulants in this description. Here a different type of cumulants is obtained because the averaging process taken in this method is different from ours.

### D. Spin Green's Function

The cumulant expansion is applicable to the calcu- lation of spin Green's functions also. The ground-state Green's function
$$G_{h k}\left(t-t^{\prime}\right) \equiv-i\left\langle T\left\{S_{h}^{-}(t) S_{k}^{+}\left(t^{\prime}\right)\right\}\right\rangle, \quad(7.14)$$
 where $\langle\cdots\rangle$ denotes an average of the Heisenberg operators with respect to the exact ground state, can be written in the interaction picture as
$$G_{h k}\left(t-t^{\prime}\right)=-i \lim _{\alpha \rightarrow 0} \frac{\left\langle 0\left|T\left\{S_{h}^{-}(t) S_{k}^{+}\left(t^{\prime}\right) U_{\alpha}\right\}\right| 0\right\rangle}{\left\langle 0\left|U_{\alpha}\right| 0\right\rangle}, \quad(7.15)$$
 where
$$U_{\alpha} \equiv U_{\alpha}(\infty,-\infty).\qquad(7.16)$$

The form (7.15) can be generated by functional differ- entiation with respect to auxiliary external field. Let
$$H_{I}(\zeta) \equiv H_{I}+\hbar \sum_{h}\left\{\zeta_{h}(t) S_{h}^{+}+\zeta_{h}^{*}(t) S_{h}^{-}\right\}, \quad(7.17)$$
 and let $U_{\alpha \zeta}$ be the corresponding $U$ operator. Then
$$T\left\{S_{h}^{-}(t) S_{k}^{+}\left(t^{\prime}\right) U_{\alpha}\right\}=-\left.\frac{\partial^{2}}{\partial \zeta_{h}^{*}(t) \partial \zeta_{k}\left(t^{\prime}\right)} U_{\alpha \zeta}\right|_{\zeta=0}. \quad(7.18)$$

Using (7.18) and
$$\left\langle 0\left|\operatorname{Av}\left\{U_{\alpha}\right\}\right| 0\right\rangle=\exp \left\langle 0\left|U_{\alpha}-1\right| 0\right\rangle_{\text {cumul }}, \quad(7.19)$$
 in (7.15) gives
$$G_{h k}\left(t-t^{\prime}\right)=i \lim _{\alpha \rightarrow 0} \left.\frac{\partial^{2}}{\partial \zeta_{h}^{*}(t) \partial \zeta_{k}\left(t^{\prime}\right)}\left\langle 0\left|U_{\alpha \zeta}\right| 0\right\rangle_{\text {cumul }}\right|_{\zeta=0}.$$

The first derivative terms are omitted in (7.20) because they vanish when $\zeta=0$ .
In the perturbation expansion, each $\zeta_{h}(t) S_{h}^{+}$ intro duces an external spin deviation terminus $\bigcirc$ with coefficient $\zeta_{h}(t)$ and each $\zeta_{k}^{*}(t^{\prime}) S_{k}^{-}$ gives an external terminus $X$ with coefficient $\zeta_{k}^{*}(t^{\prime})$ . The significance of the term external is that the terminus is not part of an excited pair with an exchange interaction. The differ- entiation in (7.20) picks out those cumulants with a single $S^{+}$ terminus at $k$ and a single $S^{-}$ terminus at $h$ , so that
$$G_{h k}\left(t-t^{\prime}\right)=-i \sum_{\Gamma}\left\langle 0\left|S_{h}^{-} S_{k}^{+} U^{(\Gamma)}\right| 0\right\rangle_{\text {cumul }}, \quad(7.21)$$
 where $U^{(\Gamma)}$ is a cumulant diagram having an incoming $k$ line and an outgoing $h$ line. The $S_{h}^{-}$ and $S_{k}^{+}$ give the termini. Note that those external lines have to be attached to the same subcluster in order to have a nonvanishing contraction.
If the unperturbed Hamiltonian $H_{0 D}$ is used, (7.21) agrees with the Green's function expansion (34) of Wang and Callen in terms of connected diagrams con- taining "locked" parts because of the equivalence shown earlier of the cumulants and the set of linked diagrams corresponding to a given configuration.

20 J. L. De Coen, F. Englert, and R. Brout, Physica 30, 1293(1964).