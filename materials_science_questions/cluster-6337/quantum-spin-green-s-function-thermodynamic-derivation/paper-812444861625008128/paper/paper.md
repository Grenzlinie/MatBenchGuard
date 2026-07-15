# COMPUTING THE COUPLINGS OF ISING SYSTEMS FROM SCHWINGER-DYSON EQUATIONS ★

A. GONZÁLEZ-ARROYO and J. SALAS

Departamento de Física Teòrica, Universidad Autónoma de Madrid, E-28049 Madrid, Spain

Received 3 August 1988

We study the problem of determining the couplings of Ising systems in terms of expectation values. We find that all previously known methods can be based on Schwinger-Dyson equations. Indeed, new methods can be derived with relative advantages with respect to all of them. Application for the renormalization group flow of the Ising model on a square lattice is presented.

## 1. Introduction

In this paper we will study the problem of the determination of the couplings for spin (or gauge) Ising systems, given the knowledge of the expectation values of arbitrary products of spins (the moment problem). This problem becomes physically interesting in the context of the renormalization group. The point is to determine the flow in coupling constant space under a renormalization group transformation. Monte Carlo simulations can be used to determine not only the expectation values of products of the original spins, but also those involving block-spins [1]. As explained in ref. [2] one can use these results to obtain the renormalized hamiltonian or couplings by making use of any solution of the moment problem.

In the last years several authors have devised some methods of determining the renormalized coupling constants by Monte Carlo renormalization group techniques. Swendsen [3] gave a recipe which indeed amounts to giving a method for solving the moment problem. The idea is based on DLR equations [4]. Simultaneously Callaway and Petronzio [5] devised a completely different approach to the problem. Their method has a few practical drawbacks compared to that of Swendsen. Indeed, one must perform a different Monte Carlo simulation for each coupling and each blocking level. In addition one must modify the renormalization group transformation to make the simulation effective, although presumably one can approach sufficiently to the results of the original renormalization group transformation.

Recently, it was suggested that Schwinger-Dyson equations (SD) can provide a solution to the problem at hand [2,6,7]. Application of this idea to Ising spin [8] and gauge systems [9] followed. The equations used in these last works are very similar to the ones used by Swendsen in ref. [3]. They are non-linear equations involving expectation values of operators which depend explicitly on the couplings. In order to turn these equations into a practical method of determining the couplings one must apply an iterative method of the Newton type. This involves performing several Monte Carlo simulations with trial values for the couplings. Each simulation allows the computation of a better approximation to the couplings which enters as a trial value in the next simulation. The iteration stops when the new and old values of the couplings are consistent within statistical errors. No arguments are given by the authors concerning the general convergence of the iterative procedure to the correct solution, but in practice for the cases studied the procedure worked fast and satisfactorily. It is to be expected that the convergence becomes worse for large couplings (low temperature).

In this paper we make an extensive study of the set of SD equations for Ising systems. In the next section we present our notation and we show that both the equations of Swendsen as well as those of ref. [8] can

---
$\star$ Work partially supported by CICyT.

418
0370-2693/88/$ 03.50 © Elsevier Science Publishers B.V.
(North-Holland Physics Publishing Division)

be derived alternatively from either SD equations or DLR equations. Indeed, a more general class of equa- tions including both follows. We also investigate which of these equations follow from the variational problem of minimizing some prescribed functional. Convexity of the functional implies that the equa- tions have a unique solution and that the iterative method converges to it. This has also influence on the truncation issue: What is the effect of assuming that some of the couplings are zero? For scalar theories the problem of truncation in relation with SD equa- tions was studied in refs. [7,10] (see also ref. [11]).

Next, we show that the SD equations can be solved (for a finite lattice) and a compact formula given for the couplings in terms of expectation values. This formula is of theoretical interest in investigating the thermodynamic limit for instance, but it is of little practical interest since one needs a very large amount of expectation values in order to determine the equally large amount of possible couplings. Assuming that only a small finite number of couplings are non-zero it is possible to use the equations to derive a practical method of computing the couplings, which is inti- mately related to the method of Callaway and Petronzio [5], but is free of all the disadvantages mentioned previously. In addition, it is superior to the methods of refs. [3,8] in not requiring any itera- tive procedure: a single Monte Carlo is enough.

In the last section we show the practical usefulness of the method by applying to the renormalization group flow of the Ising model in a two dimensional square lattice starting at the critical point with only nearest neighbour interaction. Our results have sta- tistical errors equal or smaller than previous deter- minations with essentially the same statistics. Far larger than these errors are the systematic errors re- lated to truncation. An estimate of their size is also given and they explain the differences among our re- sults and those of refs. [3,8]. To conclude the paper we comment on the extension of our formulae to the case of Ising gauge systems and Potts-type spin and gauge systems.

### 2. Schwinger-Dyson equations for Ising spins

Let us consider a system of Ising spins $\sigma_{i}=\pm 1$, where the index $i$ runs over a lattice $\mathscr{L}$ of points. The partition function of these systems is of the form

$$
Z=\prod_{i \in \mathscr{L}}\left(\sum_{\sigma_{i}= \pm 1}\right) \mathrm{e}^{-S},\quad(1)
$$

where $S=\mathscr{H} / k T$ is the euclidean action (or hamil- tonian) of the system. The physical observables of the system are arbitrary functionals of the spins which we will refer to as "operators". The set of all opera- tors constitutes a vector space with a basis $\{O_{\alpha}\}$. The dimensionality of the vector space is $2^{l}$, where $l$ is the number of points of $\mathscr{L}$. With the operation of multi- plication, the set of operators becomes an algebra. For every subset $\mathscr{B}$ of $\mathscr{L}$ we have a subalgebra $\mathscr{A}(\mathscr{B})$ $\subset \mathscr{A}(\mathscr{L})$ which is given by all functionals of the spins in $\mathscr{B}$.

The most important basis of $\mathscr{A}(\mathscr{L})$ is given by the monomials $L(\mathscr{B})$

$$
L(\mathscr{B})=\prod_{i \in \mathscr{B}} \sigma_{i},\quad(2)
$$

where $\mathscr{B}$ is any subset of $\mathscr{L}$. They satisfy

$$
L(\mathscr{B}) \cdot L\left(\mathscr{B}^{\prime}\right)=L\left(\mathscr{B} \triangle \mathscr{B}^{\prime}\right),\quad(3)
$$

where $\mathscr{B} \triangle \mathscr{B}^{\prime}$ is the symmetric difference of the sets $\mathscr{B}$ and $\mathscr{B}^{\prime}$. The algebra is thus abelian. Another im- portant basis of operators is given by $\hat{L}([s])$, where $[s]$ stands for a particular assignment $s_{i}=\pm 1$ for all spins $i \in \mathscr{L}$. The operators are products of $\delta$ functions

$$
\begin{aligned}
\hat{L}([s]) & =\prod_{i \in \mathscr{L}} \delta_{\sigma_{i}, s_{i}}=\prod_{i \in \mathscr{L}} \frac{1}{2}\left(1+\sigma_{i} \cdot s_{i}\right) \\
& =\sum_{\mathscr{B} \subseteq \mathscr{L}} L(\mathscr{B})\left(\frac{1}{2}\right)^{l}\left(\prod_{i \in \mathscr{B}} s_{i}\right).\quad(4)
\end{aligned}
$$

Analogously one can write $L(\mathscr{B})$ in terms of $\hat{L}([s])$:

$$
L(\mathscr{B})=\prod_{i \in \mathscr{L}}\left(\sum_{s_{i}}\right) \hat{L}([s])\left(\prod_{i \in \mathscr{B}} s_{i}\right).\quad(5)
$$

The operators $\hat{L}([s])$ satisfy the following relations:

$$
\hat{L}([s]) \cdot \hat{L}\left(\left[s^{\prime}\right]\right)=\hat{L}([s]) \cdot \delta_{[s],\left[s^{\prime}\right]},\quad(6)
$$

where the meaning of the $\delta$ function is obvious. For each subalgebra $\mathscr{A}(\mathscr{B})$ we have a corresponding ba- sis of operators $L$ and another basis $\hat{L}$.

Now let us turn our attention to the general form of the action $S$. We will have

$$
S=-\sum_{\alpha} \beta_{\alpha} \cdot O_{\alpha},\quad(7)
$$


where $\{O_{\alpha}\}$ is a particular basis. The monomial basis $L$ turns out to be more common and useful. We will impose additional physical requirements on the form of the action: (a) locality, (b) invariance under symmetries (translations, reflections and rotations). The first condition implies that the couplings $\beta$ tend to zero as the operators $\{O_{\alpha}\}$ involve more and more distant away spins. We are implicitly assuming a distance operation between lattice points. Any pair of spins can be classified as first neighbours, second neighbours, etc., in order of increasing distances. The invariance condition implies relations among the couplings. An interesting symmetry is the one obtained by flipping the sign of the spins. One frequently considers restricting oneself to actions belonging to the subalgebra of even operators.

For future use it is worthwhile to select one particular point $i_{0} \in \mathscr{L}$ and consider the splitting
$$
S=-\sigma_{i_{0}} W_{i_{0}}(\{\sigma\})+V(\{\sigma\}), \quad(8)
$$
where neither $W$ nor $V$ depend on the particular spin $\sigma_{i_{0}}$. They depend on the remaining spins $\{\sigma\}$ which correspond to the sublattice $\mathscr{L}_{i_{0}}^{\prime}=\mathscr{L} \triangle\left\{i_{0}\right\}$ of points. We will not need the form of $V$ but simply the fact that assuming translational invariance it can be computed in terms of $W_{i_{0}}$. This last quantity can be expanded in terms of a given basis $\{O_{\alpha}^{\prime}\}$ of the algebra $\mathscr{A}\left(\mathscr{L}_{i_{0}}^{\prime}\right)$
$$
W_{i_{0}}=\sum_{\alpha} \tilde{\beta}_{\alpha} O_{\alpha}^{\prime}, \quad(9)
$$
where the couplings $\tilde{\beta}_{\alpha}$ can be computed in terms of $\beta$ of eq. (7) and vice versa. Notice that the operators $O_{\alpha}^{\prime}$ do implicitly depend on the point $i_{0}$ but the couplings $\tilde{\beta}$ are independent.

We can consider the subsets of $\mathscr{C}^{(k)} \subset \mathscr{L}_{i_{0}}$ which involve points only up to the $k$ th neighbour of $i_{0}$. Correspondingly there is a chain of algebras $\mathscr{A}\left(\mathscr{C}^{(1)}\right) \subset$ $\mathscr{A}\left(\mathscr{C}^{(2)}\right) \subset \ldots \subset \mathscr{A}\left(\mathscr{L}_{i_{0}}^{\prime}\right)$. A strong form of locality implies that $W_{i_{0}}$ belongs to $\mathscr{A}\left(\mathscr{C}^{1}\right)$ (or any other of the subalgebras). However, renormalization group transformations are in principle expected to violate this strong requirement but not the general locality condition.

Let us now derive the SD equations for this system [12]. These equations follow from the invariance of the integration measure in the path integral. In our case it reduces to the invariance of the sums $\sum_{\sigma}$ under a redefinition of $\sigma \rightarrow-\sigma$. Let us consider one point of the lattice labelled $i_{0}$; the corresponding spin is $\sigma_{i_{0}}$. Let $F(\sigma_{i_{0}},\{\sigma\})$ be a functional (operator) of this spin and of the remaining ones $\{\sigma\}$. Performing the change of variables $\sigma_{i_{0}} \rightarrow-\sigma_{i_{0}}$ we get
$$
\begin{aligned}
& \left\langle F\left(\sigma_{i_{0}},\{\sigma\}\right)\right\rangle \\
& \quad=\left\langle F\left(-\sigma_{i_{0}},\{\sigma\}\right) \exp \left[-2 \sigma_{i_{0}} W_{i_{0}}(\{\sigma\})\right]\right\rangle, \quad(10)
\end{aligned}
$$
where $W_{i_{0}}(\{\sigma\})$ is defined in eq. (8). Using the basis $\{O_{\alpha}^{\prime}\}$ of $\mathscr{A}\left(\mathscr{L}_{i_{0}}^{\prime}\right)$ we obtain
$$
\begin{aligned}
& \left\langle O_{\alpha}^{\prime} \sigma_{i_{0}} \exp \left(-\sigma_{i_{0}} W_{i_{0}}\right) \cosh W_{i_{0}}\right\rangle=0, \\
& \left\langle O_{\alpha}^{\prime} \sigma_{i_{0}} \exp \left(-\sigma_{i_{0}} W_{i_{0}} \sinh W_{i_{0}}\right\rangle=0,\right.
\end{aligned}
$$
where the dependence of $O_{\alpha}^{\prime}$ and $W_{i_{0}}(\{\sigma\})$ on the spins $\sigma_{i}$ for $i \in \mathscr{L}_{i_{0}}^{\prime}$ is not explicitly shown. The first set of equations (11a) follows from eq. (10) by substituting $F$ by $\sigma_{i_{0}} \cdot O_{\alpha}^{\prime}$. The second set follows by substituting $F$ by $O_{\alpha}^{\prime}$. The first set of SD equations (11a) are indeed the same set used in ref. [8].

Let us now consider the DLR equations. As before $F$ will stand for an arbitrary functional of $\sigma_{i_{0}}$ and the remaining spins $\{\sigma\}$. Computing the expectation value of $F$ in two different ways we get
$$
\begin{aligned}
& \left\langle F\left(\sigma_{i_{0}},\{\sigma\}\right)\right\rangle=\frac{1}{Z} \sum_{\sigma_{i_{0}}} \sum_{i \in \mathscr{L}^{\prime}} \prod_{\sigma_{i}} \sum \exp \left(\sigma_{i_{0}} W_{i_{0}}-V_{i_{0}}\right) F \\
& =\frac{1}{Z} \prod_{i \in \mathscr{L}^{\prime}} \sum_{\sigma_{i}} \exp \left(-V_{i_{0}}\right) \sum_{\sigma_{i_{0}}} \exp \left(\sigma_{i_{0}} W_{i_{0}}\right) F\left(\sigma_{i_{0}},\{\sigma\}\right) \\
& \quad × \frac{\sum_{\tilde{\sigma}_{i_{0}}} \exp \left(\tilde{\sigma}_{i_{0}} W_{i_{0}}\right)}{\sum_{\tilde{\sigma}_{i_{0}}} \exp \left(\tilde{\sigma}_{i_{0}} W_{i_{0}}\right)} \\
& =\left\langle\frac{\sum_{\tilde{\sigma}_{i_{0}}} \exp \left(\tilde{\sigma}_{i_{0}} W_{i_{0}}\right) F\left(\tilde{\sigma}_{i_{0}},\{\sigma\}\right)}{\sum_{\tilde{\sigma}_{i_{0}}} \exp \left(\tilde{\sigma}_{i_{0}} W_{i_{0}}\right)}\right\rangle.
\end{aligned}
$$

Choosing $F=\sigma_{i_{0}} O_{\alpha}^{\prime}$ we arrive at the Swendsen equations [3]:
$$
\left\langle O_{\alpha}^{\prime} \sigma_{i_{0}} \exp \left(-\sigma_{i_{0}} W_{i_{0}}\right) \frac{1}{\cosh W_{i_{0}}}\right\rangle=0,
$$
written in some unusual form which emphasizes the similarity with (11a), (11b).

It is clear that one can generalize eqs. (11) and (13) to a more general form:
$$
\left\langle O_{\alpha}^{\prime} \sigma_{i_{0}} \exp \left(-\sigma_{i_{0}} W_{i_{0}}\right) g\left(W_{i_{0}}\right)\right\rangle=0, \quad(14)
$$


where $g$ is some non-singular function of $W_{i_{0}}(\{\sigma\})$.
Eq. (14) can be deduced both from the general SD equations (10) and from the DLR equation (12).
Thus, it is clear that there is the same physical information contained in both classes of equations. Eqs.
(11a), (11b) are simply more natural in the SD scheme as (13) for the DLR one. Furthermore, if all the possible operators $O_{\alpha}^{\prime}$ are included, it turns out that all different sets of equations (14) with different $g$ functions are equivalent provided $g$ does not vanish for the range of possible values of $W_{i_{0}}(\{\sigma\})$. In particular solving eq. (10a) is equivalent to solving eq. (12) ( but eq. (10b) is less strong).

In summary, there are altogether $l \cdot 2^{l-1}$ different equations: the set of equations (14) with all possible values of $\alpha$ and $i_{0}$. The choice of function $g$ is irrelevant, since the set of equations for one particular $g$ are linear combinations of those for other choices.
Using these equations, one can solve for the unknown $\tilde{\beta}$ in eq. (9) as we will see later.

The situation is modified if it is known or assumed that some of the couplings $\tilde{\beta}$ are zero. In this case, it is enough to take a subset of eq. (14) to determine the non-zero couplings. A typical example is to consider that $W_{i_{0}} \in \mathscr{A}(\mathscr{C}^{(k)})$. In this case, one can take into account a subset of equations which is formally identical to eq. (14) but with $\{O_{\alpha}^{\prime}\}$ now being a basis of $\mathscr{A}(\mathscr{C}^{(k)})$. Again the choice of $g$ would be irrelevant. However, there are still more equations than unknowns. The authors of refs. [3,8,9] chose to work with the same number of equations as unknowns, and they proceed to make use of eq. (14) with the same operators $O_{\alpha}^{\prime}$ which appear in the expansion of $W$ (and summing the equations over $i_{0}$ ). We will now show that provided $g$ satisfies some properties it can be shown that this restricted set of equations does have one and only one solution.

Let us consider the following functional of the couplings

$$
\mathscr{F}\left(\tilde{\beta}, \tilde{\beta}^{\prime}\right)=-\sum_{i_{0}}\left\langle\sigma_{i_{0}} \tilde{g}\left(W_{i_{0}}^{\prime}\right)\right\rangle, \quad(15)
$$

where $W_{i_{0}}^{\prime}=\sum_{\alpha} \tilde{\beta}_{\alpha}^{\prime} O_{\alpha}^{\prime}$ is in principle different from $W_{i_{0}}$. The function $\tilde{g}$ satisfies

$$
\frac{\mathrm{d} \tilde{g}(z)}{\mathrm{d} z}=\exp \left(\sigma_{i_{0}} z\right) g(z). \quad(16)
$$

The functional $\mathscr{F}$ depends implicitly on $\tilde{\beta}$ through the expectation value and explicitly on $\tilde{\beta}^{\prime}$ through $\tilde{g}\left(W^{\prime}\right)$.
The set of equations (14) now implies that $\mathscr{F}$ has an extremum at $\tilde{\beta}_{\alpha}^{\prime}=\tilde{\beta}_{\alpha}$. Differentiating $\mathscr{F}$ twice with respect to $\tilde{\beta}^{\prime}$ we get

$$
\begin{aligned}
& \frac{\partial \mathscr{F}}{\partial \tilde{\beta}_{\alpha}^{\prime} \partial \tilde{\beta}_{\gamma}^{\prime}}=\sum_{i_{0}}\left\langle O_{\alpha}^{\prime} O_{\gamma}^{\prime} \exp \left(-\sigma_{i_{0}} W_{i_{0}}^{\prime}\right)\right. \\
& \left.\quad \times\left[g\left(W^{\prime}\right)-\sigma_{i_{0}} \dot{g}\left(W^{\prime}\right)\right]\right\rangle, \quad(17)
\end{aligned}
$$

where $\dot{g}$ is the derivative of $g$. At $\tilde{\beta}^{\prime}=\tilde{\beta}$ the term in $\dot{g}$ vanishes as a consequence of eq. (14) and the sign of $g(W)$ determines whether we have a minimum or a maximum. If $g$ is positive definite we necessarily have a minimum and furthermore if $|\dot{g}| \leqslant g$ the functional $\mathscr{F}$ is convex. Indeed for $g(W)=\cosh W$ and $g(W)=1 / \cosh W$ which correspond to eqs. (11a) and (13) both conditions are met. Another example is $g(W)=1$.

If we restrict ourselves to a family of truncated $W^{\prime}$ where only a given number of couplings are non-zero and if we consider the corresponding set of equations, we obtain a solution $\bar{W}^{\prime}$ which is the minimum of $\mathscr{F}$ within the restricted set. Different functions $g$ correspond to different functionals $\mathscr{F}$. This is indeed the meaning of the truncated solution. The convexity of $\mathscr{F}$ ensures that the solution is unique and coincides with the functional $W$, if this one is contained in the space of trial functionals. The convexity of $\mathscr{F}$ also ensures that as we increase the trial space we come closer and closer to the right solution $\tilde{\beta}$. Finally this property also has implications on the convergence of the iteration procedure as one can easily realize.

Now we go back to the full set of equations (14) for all possible operators $O_{\alpha}^{\prime}$ which are the basis of $\mathscr{A}\left(\mathscr{L}_{i_{0}}^{\prime}\right)$. We will see that one can solve for the couplings in these equations. We are going to use the two different bases used at the beginning of this section.
The coefficients of $W$ in these basis are

$$
\begin{aligned}
W_{i_{0}} & =\sum_{\mathscr{B} \subset \mathscr{L}_{i_{0}}^{\prime}} \tilde{J}(\mathscr{B}) L(\mathscr{B}) \\
& =\prod_{i \in \mathscr{L}_{i_{0}}^{\prime}}\left(\sum_{s_{i}}\right) W([s]) \hat{L}([s]).
\end{aligned}
$$

Using the basis of operators $\hat{L}([s])$ in eq. (14) we get

$$
\left\langle\hat{L}([s]) \sigma_{i_{0}} \exp \left[-\sigma_{i_{0}} W([s])\right] g(W([s]))=0 .\right.
$$

It is clear that the set of equations is independent of $g$ provided it does not vanish. Solving for $W([s])$ we get
$$
W([s])=\frac{1}{2} \ln \frac{\left\langle\tilde{L}([s]) \delta_{\sigma_{i_{0}, 1}}\right\rangle}{\left\langle\tilde{L}([s]) \delta_{\sigma_{i_{0},-1}}\right\rangle}. \tag{20}
$$

Using translational invariance one could sum the expectation values in the numerator and denominator over all points $i_{0}$. However, notice that $\tilde{L}([s])$ depends implicitly on $i_{0}$ and must be translated also. Using the relations among the operators $L(\mathscr{B})$ and $\tilde{L}([s])$ we obtain
$$
\begin{aligned}
\tilde{J}(\mathscr{B}) & =\prod_{i \in \mathscr{Y}_{i_{0}}^{\prime}}\left(\sum_{s_{i}}\right)\left(\frac{1}{2}\right)^{l}\left(\prod_{j \in \mathscr{B}} s_{j}\right) \ln \frac{\left\langle\tilde{L}([s]) \delta_{\sigma_{i_{0}, 1}}\right\rangle}{\left\langle\tilde{L}([s]) \delta_{\sigma_{i_{0},-1}}\right\rangle} \\
& =\prod_{i \in \mathscr{Y}^{\prime}}\left(\sum_{s_{i}}\right)\left(\frac{1}{2}\right)^{l} \prod_{j \in \mathscr{A} \cup\left\{i_{0}\right\}} s_{j} \ln \left\langle\tilde{L}\left(\left[s, s_{i 0}\right]\right)\right\rangle. \quad(21)
\end{aligned}
$$

This formula is of theoretical interest only. It can be used to study the thermodynamic limit. From a practical point of view eq. (21) involves computing $2^{l}$ expectation values in order to obtain the $2^{l-1}$ couplings $\tilde{J}(\mathscr{B})$. The formulas become useful if it is known or assumed that only a small number (compared to $2^{l}$ ) of couplings are non-zero. Then one can take as many equations (20) as unknowns. Each of the selected configurations $[s]$ is associated with a particular value of $W([s])$ which is a linear combination of the unknown couplings. Taking configurations yielding as many linearly independent combinations as couplings one can determine these couplings. This is exactly the method devised by Callaway and Petronzio [5]. However, it is possible to proceed in a different fashion. Given that it is assumed that there is only a small number of couplings, the given spin at $i_{0}$ will only interact with those in a subset $\mathscr{B}$ of the lattice $\mathscr{L}$. then $W_{i_{0}} \in \mathscr{A}(\mathscr{B})$ and we can rewrite formulas (19) and (20) but now restricted to $\mathscr{A}(\mathscr{B})$. The different couplings can now determined in terms of the expectation values of the operators $\tilde{L}([s])$, where $[s]$ is now a possible configuration for the spins in $\mathscr{B}$. As an example one can consider the equations for a hypercubical Ising model in $D$ dimensions with nearest neighbour interactions. There are two couplings: the nearest neighbour 2-spin coupling $J$ and the one-spin magnetic field $h$. There are $2^{2 D}$ equations of type (20), one for each configuration of the $2 D$ nearest neighbours of the spin $i_{0}$. There are only $2 D$ possible linear combinations of couplings appearing in $W([s])$. These combinations are $k J+h$, where $k=-2 D,-2 D+2, ..., 2 D$. Then we can collect the equations into $2 D+1$ different ones:
$$
k J+h=\frac{1}{2} \ln \frac{\sum_{[s] \in \mathscr{S}_{k}}\left\langle\tilde{L}([s]) \delta_{\sigma_{i_{0}, 1}}\right\rangle}{\sum_{[s] \in \mathscr{S}_{k}}\left\langle\tilde{L}([s]) \delta_{\sigma_{i_{0},-1}}\right\rangle}, \tag{22}
$$
where the sum is over the set $\mathscr{S}_{k}$ of configurations with $W([s])=k J+h$. We can include in the sum in numerator and denominator all configurations obtained by translating $i_{0}$ and $[s]$ over the lattice.

The set of equations (22) can now be used to determine the couplings $J$ and $h$. One can select a couple of equations or use the full set. The compatibility of the set can be used to check the assumption that only interactions between nearest neighbour spins are present.

In general the procedure we suggest to determine the couplings is as follows. First decide which are the couplings taken to be non-zero $\beta_{1}, ..., \beta_{M}$. These couplings are such that only the spins at the sublattice $\mathscr{B}$ interact with the spin at $i_{0}$. If $b$ is the number of spins in $\mathscr{B}$, there are $2^{b}$ different configurations, but many of them give rise to the same value of $W([s])=W_{r}$. Each of the $W_{r}$ is a different linear combination of the $M$ couplings. All configurations giving the same $W_{r}$ are belonging to the class $\mathscr{S}_{r}$. We then write the equations
$$
W_{r}=\frac{1}{2} \ln \frac{\sum_{[s] \in \mathscr{S}_{r}}\left\langle\tilde{L}([s]) \delta_{\sigma_{i 0,1}}\right\rangle}{\sum_{[s] \in \mathscr{S}_{r}}\left\langle\tilde{L}([s]) \delta_{\sigma_{i_{0},-1}}\right\rangle}. \tag{23}
$$

Indeed, we can get a better determination by summing in numerator and denominator over all translations and by summing in the numerator the configurations obtained by flipping $s \rightarrow-s$ and $\sigma_{i 0} \rightarrow$ $\sigma_{i 0}$ and the same for the denominator.

Instead of using a subset of $M$ equations (23) to solve for the couplings $\beta_{1}, ..., \beta_{M}$, we prefer to determine the couplings by minimizing a $\chi^{2}$ function
$$
\chi^{2}=\sum_{r} \frac{1}{\sigma^{2}(r)}\left(\xi_{r}-W_{r}\right)^{2}, \tag{24}
$$
where $\xi_{r}$ are the Monte Carlo estimates of the RHS of eq. (23), $\sigma(r)$ their corresponding statistical errors and $W_{r}$ the predicted linear combinations of the couplings $\beta_{1}, ..., \beta_{M}$.

We emphasize that our method resembles that of Callaway and Petronzio, but we have the advantage that all renormalized couplings for all blocking levels can be determined in a single Monte Carlo simulation. With respect to the methods of refs. [3,8], this one has the advantage that no iteration is necessary.

## 3. Numerical results
In this section we will consider the application of the method developed previously to the case of the Ising model on a square lattice (two dimensions). In this case there are two previous determinations [3,8] of the renormalization group flow. As in those papers we will consider the original action to be the pure nearest neighbour one at the critical point $J_c$=0.440687. Then we consider the renormalization group transformation given by the majority rule. We will start with a 32×32 lattice and consider three blocking levels. We will restrict the space of operators to linear combinations of the seven operators shown in table 1.

Our results were obtained in an IBM 4381.13 machine using a heat-bath Monte Carlo algorithm. A total of $2.4×10^6$ sweeps over the lattice were performed and averages were taken once every 20 sweeps. The whole sample was divided into 24 groups of equal size in order to study the fluctuations in the values of the couplings.

The method of analysis is as follows. We select one

<table>
<caption>Table 1 The seven operators used in the MCRG analysis.</caption>
<thead>
  <tr>
    <th>$\alpha$</th>
    <th>Operators $O'_\alpha$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>nearest neighbour (1,0)</td>
  </tr>
  <tr>
    <td>2</td>
    <td>next to nearest neighbour (1,1)</td>
  </tr>
  <tr>
    <td>3</td>
    <td>third neighbour (2,0)</td>
  </tr>
  <tr>
    <td>4</td>
    <td>fourth neighbour (2,1)</td>
  </tr>
  <tr>
    <td>5</td>
    <td>fifth neighbour (2,2)</td>
  </tr>
  <tr>
    <td>6</td>
    <td>four-spin coupling around a plaquette (1.0), (1,1), (0.1)</td>
  </tr>
  <tr>
    <td>7</td>
    <td>four-spin coupling on a sublattice plaquette (1,1), (0,2), $(-1,1)$</td>
  </tr>
</tbody>
</table>

lattice point $i_0$ and observe the configuration $[s]$ of the neighbouring spins. The quantities $N_r^+$ and $N_r^-$ count the number of times $[s] \in \mathscr{S}_r$ and $\sigma_{i_0}=\pm1$ respectively (including all points $i_0 \in \mathscr{L}$). There are altogether 6863 different values of $r$. The output of the Monte Carlo simulation is the value of $N_r^+$ and $N_r^-$ for the total statistics as well as for each of the 24 groups in which this sample is divided. In formula (24) $\xi_r=1/2\ln(N_r^+/N_r^-)$ and $\sigma^2(r)$ is the dispersion in the value of $\xi_r$ estimated from the analysis of the 24 groups. Indeed the value of $\sigma^2(r)$ fits quite well with the expectation of a binomial distribution for $\sigma^2(r)$ small enough

$$
\sigma^{2}(r)=\frac{N_{r}^{+}+N_{r}^{-}}{4 N_{r}^{+} N_{r}^{-}}. \qquad (25)
$$

If the variables $\xi_r$ were uncorrelated gaussians with dispersion $\sigma^2(r)$ then minimizing eq. (24) yields the

<table>
<caption>Table 2 Our estimate for the value of the couplings (A) for each level blocking LB compared to the results of ref. [8] (B) and ref. [3] (C). The value of $\chi^2$ and the number of degrees of freedom (DF) are indicated. The statistical errors affecting the last digit are quoted in parentheses.</caption>
<thead>
  <tr>
    <th>LB</th>
    <th></th>
    <th>$J_1$</th>
    <th>$J_2$</th>
    <th>$J_3$</th>
    <th>$J_6$</th>
    <th>$J_7$</th>
    <th>$J_4$</th>
    <th>$J_5$</th>
    <th>$\chi^2$/DF</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>A</td>
    <td>0.4404(3)</td>
    <td>0.0004(2)</td>
    <td>0.0002(1)</td>
    <td>0.0002(1)</td>
    <td>--0.0001(1)</td>
    <td>--0.0002(1)</td>
    <td>0.0000(1)</td>
    <td>3439/3072</td>
  </tr>
  <tr>
    <td>1</td>
    <td>A</td>
    <td>0.3640(2)</td>
    <td>0.0820(2)</td>
    <td>--0.0072(1)</td>
    <td>--0.0107(1)</td>
    <td>0.0014(1)</td>
    <td>--0.0034(1)</td>
    <td>--0.0021(1)</td>
    <td>50833/3469</td>
  </tr>
  <tr>
    <td></td>
    <td>B</td>
    <td>0.3609(3)</td>
    <td>0.0798(2)</td>
    <td>--0.0062(2)</td>
    <td>0.0006(2)</td>
    <td>0.0059(2)</td>
    <td>0.0035(1)</td>
    <td>--0.0020(2)</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>C</td>
    <td>0.3643(3)</td>
    <td>0.0814(2)</td>
    <td>--0.0068(2)</td>
    <td>--0.0075(2)</td>
    <td>0.0026(2)</td>
    <td>--0.0038(1)</td>
    <td>--0.0023(2)</td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>A</td>
    <td>0.3538(3)</td>
    <td>0.0955(3)</td>
    <td>--0.0094(2)</td>
    <td>--0.0146(3)</td>
    <td>0.0011(3)</td>
    <td>--0.0042(1)</td>
    <td>--0.0024(2)</td>
    <td>32763/3403</td>
  </tr>
  <tr>
    <td></td>
    <td>B</td>
    <td>0.3511(3)</td>
    <td>0.0923(2)</td>
    <td>--0.0096(4)</td>
    <td>--0.0003(9)</td>
    <td>0.0063(2)</td>
    <td>--0.0043(1)</td>
    <td>--0.0017(4)</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>C</td>
    <td>0.3527(7)</td>
    <td>0.0944(10)</td>
    <td>--0.0094(6)</td>
    <td>--0.0075(9)</td>
    <td>0.0043(5)</td>
    <td>--0.0046(4)</td>
    <td>--0.0019(9)</td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>A</td>
    <td>0.3542(2)</td>
    <td>0.0970(2)</td>
    <td>--0.0099(2)</td>
    <td>--0.0129(1)</td>
    <td>0.0040(1)</td>
    <td>--0.0054(1)</td>
    <td>--0.0022(1)</td>
    <td>7727/614</td>
  </tr>
  <tr>
    <td></td>
    <td>B</td>
    <td>0.3511(8)</td>
    <td>0.0899(6)</td>
    <td>--0.0126(4)</td>
    <td>0.0028(6)</td>
    <td>0.0095(4)</td>
    <td>--0.0040(6)</td>
    <td>--0.0014(6)</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>C</td>
    <td>0.353(3)</td>
    <td>0.095(3)</td>
    <td>--0.013(2)</td>
    <td>--0.004(3)</td>
    <td>0.005(2)</td>
    <td>--0.002(2)</td>
    <td>--0.005(2)</td>
    <td></td>
  </tr>
</tbody>
</table>

### Table 3
Best solution for the couplings obtained by restricting eq. (24) to $5 \times 10^{-5} < \sigma^2(r) < 10^{-2}$(B) and $\sigma^2(r) < 5 \times 10^{-5}$(A). The statistical errors are typically 1.5 times the one in table 2.

<table>
  <thead>
    <tr>
      <th>LB</th>
      <th></th>
      <th>$J_1$</th>
      <th>$J_2$</th>
      <th>$J_3$</th>
      <th>$J_5$</th>
      <th>$J_7$</th>
      <th>$J_4$</th>
      <th>$J_5$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>A</td>
      <td>0.4409</td>
      <td>0.0001</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>--0.0002</td>
      <td>0.0002</td>
    </tr>
    <tr>
      <td></td>
      <td>B</td>
      <td>0.4402</td>
      <td>0.0006</td>
      <td>0.0006</td>
      <td>0.0004</td>
      <td>--0.0001</td>
      <td>--0.0002</td>
      <td>--0.0002</td>
    </tr>
    <tr>
      <td>1</td>
      <td>A</td>
      <td>0.3694</td>
      <td>0.0795</td>
      <td>--0.0094</td>
      <td>--0.0095</td>
      <td>0.0033</td>
      <td>--0.0035</td>
      <td>--0.0030</td>
    </tr>
    <tr>
      <td></td>
      <td>B</td>
      <td>0.3580</td>
      <td>0.0819</td>
      <td>--0.0066</td>
      <td>--0.0181</td>
      <td>--0.0032</td>
      <td>--0.0037</td>
      <td>--0.0019</td>
    </tr>
    <tr>
      <td>2</td>
      <td>A</td>
      <td>0.3605</td>
      <td>0.0928</td>
      <td>--0.0126</td>
      <td>--0.0129</td>
      <td>0.0038</td>
      <td>--0.0039</td>
      <td>--0.0035</td>
    </tr>
    <tr>
      <td></td>
      <td>B</td>
      <td>0.3480</td>
      <td>0.0952</td>
      <td>--0.0082</td>
      <td>--0.0209</td>
      <td>--0.0023</td>
      <td>--0.0045</td>
      <td>--0.0021</td>
    </tr>
    <tr>
      <td>3</td>
      <td>A</td>
      <td>0.3546</td>
      <td>0.0976</td>
      <td>--0.0123</td>
      <td>--0.0092</td>
      <td>0.0061</td>
      <td>--0.0057</td>
      <td>--0.0023</td>
    </tr>
    <tr>
      <td></td>
      <td>B</td>
      <td>0.3489</td>
      <td>0.0935</td>
      <td>--0.0100</td>
      <td>--0.0222</td>
      <td>--0.0033</td>
      <td>--0.0053</td>
      <td>--0.0033</td>
    </tr>
  </tbody>
</table>

smallest statistical errors for the couplings. Our results are presented in table 2 together with those of refs. [3,8]. We only included those combinations for which $\sigma^2(r) < 0.01$. The values of $\chi^2$ for the minimum solution are indicated together with the values of $r$ entering in the determination. Notice that for the zeroth blocking level the results are completely satisfactory as well as the value of $\chi^2$. For higher blocking levels the values of $\chi^2$ are quite high which we take as an indication for the presence of truncation errors larger than the purely statistical ones. Indeed, the different determinations of the couplings using different methods are seen to differ by much larger values than the statistical errors.

In order to estimate the size of truncation errors, we partition the set of equations (14) into two disjoint sets. The first is selected by requiring $5 \times 10^{-5} < \sigma^2(r) < 10^{-2}$ and the second given by $\sigma^2(r) < 5 \times 10^{-5}$. The results shown in table 3 are reasonably consistent, but they indicate truncation errors much larger than statistical errors.

To conclude, we comment that the procedure described in this paper can be easily generalized to the case of discrete gauge systems by changing the points of the lattice by the links and imposing gauge invariance of the action. In addition the procedure can also be generalized to $n$-state Potts systems.

## Acknowledgement
The authors are grateful to CICyT for financial support. One of us (A.G.-A.) acknowledges useful conversations with A. Sokal and M. Okawa.

## References
[1] S.K. Ma, Phys. Rev. Lett. 37 (1976) 461;
R.H. Swendsen, Phys. Rev. Lett. 42 (1979) 859.
[2] A. González-Arroyo and M. Okawa, Phys. Rev. B 35 (1987) 2108.
[3] R.H. Swendsen, Phys. Rev. Lett. 52 (1984) 1165.
[4] H.B. Callen, Phys. Lett. 4 (1963) 161;
R.L. Dobrushin, Theor. Prob. Appl. 13 (1969) 387;
D.E. Landford III and D. Ruelle, Commun. Math. Phys. 13 (1969) 194.
[5] D.J.E. Callaway and R. Petronzio, Phys. Lett B 139 (1984) 189.
[6] M. Falcioni et al., Nucl. Phys. B 265 [FS15] (1986) 187.
[7] A. González-Arroyo and M. Okawa, Phys. Rev. D 35 (1987) 672.
[8] A. González-Arroyo and M. Okawa, Phys. Rev. Lett. 58 (1987) 2165.
[9] A. González-Arroyo, M. Okawa and Y. Shimizu, Phys. Rev. Lett. 60 (1988) 437.
[10] A. González-Arroyo and J. Salas, in preparation.
[11] A. González-Arroyo, Nucl. Phys. (Proc. Suppl.) B 4 (1988) 537.
[12] F. Schwabl, Ann. Phys. (NY) 54 (1969) 1.
