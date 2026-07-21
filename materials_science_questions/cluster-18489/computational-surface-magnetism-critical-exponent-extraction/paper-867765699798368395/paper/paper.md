# Surface magnetization and critical behavior of aperiodic Ising quantum chains

Loïc Turban
Laboratoire de Physique du Solide, Université de Nancy I, Boîte Postale 239,
F-54506 Vandœuvre lès Nancy Cedex, France

Ferenc Iglói
Research Institute for Solid State Physics, P.O. Box 49,
H-1525 Budapest 114, Hungary

Bertrand Berche
Laboratoire de Physique du Solide, Université de Nancy I, Boîte Postale 239,
F-54506 Vandœuvre lès Nancy Cedex, France
(cond-mat/9312080)

We consider semi-infinite two-dimensional layered Ising models in the extreme anisotropic limit with an aperiodic modulation of the couplings. Using substitution rules to generate the aperiodic sequences, we derive functional equations for the surface magnetization. These equations are solved by iteration and the critical exponent $\beta_s$ can be determined exactly. The method is applied to three specific aperiodic sequences, which represent different types of perturbation, according to a relevance-irrelevance criterion. On the Thue-Morse lattice, for which the modulation is an irrelevant perturbation, the surface magnetization vanishes with a square root singularity, like in the homogeneous lattice. For the period-doubling sequence, the perturbation is marginal and $\beta_s$ is a continuous function of the modulation amplitude. Finally, the Rudin-Shapiro sequence, which corresponds to the relevant case, displays an anomalous surface critical behavior which is analyzed via scaling considerations. Depending on the value of the modulation, the surface magnetization either vanishes with an essential singularity or remains finite at the bulk critical point, i.e., the surface phase transition is of first order.

## I. INTRODUCTION

Since the discovery of quasicrystals, $^1$ one has witnessed a growing interest in understanding their structure and physical properties (for recent reviews see Refs. 2-6). The study of phase transitions on quasiperiodic lattices is now an active field of research. Since quasiperiodic and, more generally, aperiodic systems can be considered as a state of matter which interpolates between the periodic (crystalline) and the random (disordered, glassy) states, the corresponding critical behavior is very rich and theoretically challenging.

The first results obtained in this field were mainly numerical. For example, it was shown that different systems on the two-dimensional Penrose lattice (Ising model, $^{7-9}$ percolation, $^{10,11}$ self-avoiding walks$^{12}$) are universal in the sense that the critical exponents are the same as in regular, two-dimensional lattices. The same conclusion was reached for three-dimensional quasiperiodic structures, $^{13}$ although with a weaker numerical accuracy.

Exact results about critical properties can be obtained on two-dimensional, layered Ising models, where the intralayer couplings $K_1$ are kept constant, whereas the interlayer interactions $K_2(k)$ follow the aperiodic modulation of the underlying lattice. One usually works in the extreme anisotropic limit, $^{14}$ with $K_2(k)\to0$, $K_1\to\infty$, keeping fixed the ratio $\lambda_k=K_2(k)/K_1^*$ where $K_1^*$ is the dual interaction corresponding to $K_1$. In this limit the system is described by a one-dimensional quantum Ising model (QIM) with the Hamiltonian

$$
\mathcal{H}=-\frac{1}{2}\sum_{k=1}^{\infty}\left[\sigma_k^z+\lambda_k\sigma_k^x\sigma_{k+1}^x\right],\tag{1.1}
$$

where the $\sigma$'s are Pauli spin 1/2 operators.

The first exact results on the QIM were obtained for the bulk critical properties on the Fibonacci and related lattices, where the specific heat is found to have a logarithmic singularity of the Onsager type. $^{15-19}$ It was Tracy$^{20}$ who first showed examples of aperiodic layered Ising models where the logarithmic singularity in the specific heat is washed out, like in the layered Ising model with random couplings (McCoy-Wu model). $^{21}$

A systematic study of the bulk critical behavior of aperiodic QIMs has been performed recently by Luck. $^{22}$ Generalizing the Harris criterion, $^{23}$ the relevance or irrelevance of the aperiodicity is shown to be connected to the size of the fluctuations in the couplings $\lambda_k$. For bounded fluctuations (as happens for the Fibonacci lattice) the specific heat of the system diverges logarithmically as in the homogeneous one, while, for unbounded fluctuations, the critical behavior is anomalous, e.g., the specific heat displays an essential singularity like in the McCoy-Wu model. $^{21}$ In the marginal case, when the fluctuations

12695

grow on a logarithmic scale, non-universal critical behavior is expected with critical exponents depending on the strength of the aperiodicity.

The relevance-irrelevance criterion has been generalized for other systems²⁴ and higher dimensional aperiodicities.²⁵ For relevant modulations, the form of the singular quantities near the critical point has also been determined, using scaling arguments.²⁴

As far as the surface critical behavior of aperiodic systems is concerned, only a few results are available. For the QIM in the ordered phase, the asymptotic limit of the spin-spin correlation function in the surface gives the square of the surface magnetization $m_s$. This leads to the expression²⁶

$$
m_s = <1|\sigma_1^x|0 > \tag{1.2}
$$

where $|0 >$ is the ground state of $\mathcal{H}$ and $|1 >$ is the first excited state, belonging to the odd sector of the Hamiltonian, which is degenerate with the ground state in the ordered phase of the infinite system. The matrix element in Eq. (1.2) can be rewritten using a Jordan-Wigner transformation of the spin operator, followed by a canonical transformation to Fermi operators which diagonalizes the Hamiltonian as described in Ref. 27. The surface magnetization finally takes a simple form involving sums of products of the couplings²⁸

$$
m_s = \left( 1 + \sum_{j=1}^{\infty} \prod_{k=1}^{j} \lambda_k^{-2} \right)^{-1/2}, \tag{1.3}
$$

which stays valid for any distribution. The surface magnetization has been evaluated in the critical region for different sequences with bounded fluctuations in Ref. 29 and in each case it was found to vanish with a square law singularity, in agreement with scaling arguments. On the other hand it was shown in Ref. 24 that any type of marginal modulation results in a non-universal critical behavior, with a surface magnetization exponent which is a continuous function of the modulation strength.

In the present paper, we continue and extend our studies of the surface critical behavior of aperiodic quantum Ising models. To evaluate the infinite sum for $m_s$ in Eq. (1.3) we have developed a method leading to functional equations for the surface magnetization which do not contain explicitly the form of the aperiodicity. Iterating these relations, a closed form expression for the surface magnetization is obtained, from which the critical exponent as well as corrections to scaling can be determined exactly. To illustrate the method, different aperiodic sequences with irrelevant, marginal, as well as relevant modulations, are evaluated. For the Rudin-Shapiro sequence, which represents a relevant perturbation, a combination of numerical results and scaling arguments has been used. The surface magnetization is found to display a first order transition for some range of the coupling ratio, whereas the bulk transition is expected to be continuous.

The setup of the paper is the following. In Sec. II, the properties of aperiodic sequences generated through substitutions are summarized and a relevance-irrelevance criterion is deduced from scaling considerations. Then we study successively the Thue-Morse sequence (Sec. III), the period-doubling sequence (Sec. IV), and the Rudin-Shapiro sequence (Sec. V). The results are discussed in the final section.

## II. APERIODIC SEQUENCES AND SCALING CONSIDERATIONS

Aperiodic sequences can be generated through iterated substitutions on the letters $A$, $B$, ... such that $A \to \mathcal{S}(A)$, $B \to \mathcal{S}(B)$, .... The properties of a given sequence are then obtained from its substitution matrix $\underline{M}$ whose columns contain the numbers of letters $A$, $B$, ... in $\mathcal{S}(A)$, $\mathcal{S}(B)$, ..., respectively:

$$
\underline{M} = \begin{pmatrix}
n_A^{\mathcal{S}(A)} & n_A^{\mathcal{S}(B)} & \cdots \\
n_B^{\mathcal{S}(A)} & n_B^{\mathcal{S}(B)} & \cdots \\
\vdots & \vdots &
\end{pmatrix}. \tag{2.1}
$$

It follows that $\underline{M}^n$ has matrix elements giving the corresponding numbers in the sequences constructed on $A$, $B$, ... after $n$ substitutions. For example, when one starts with $A$, i.e., with the substitutions $A \to \mathcal{S}(A) \to \mathcal{S}(\mathcal{S}(A))$ ..., the number of $A$, $L_n^A$, in the sequence after $n$ steps is $(\underline{M}^n)_{11}$ whereas the length of the sequence is $L_n = \sum_i (\underline{M}^n)_{i1}$. Making use of the right eigenvectors $\mathrm{V}_\alpha$ of the substitution matrix

$$
\underline{M} \mathrm{V}_\alpha = \Lambda_\alpha \mathrm{V}_\alpha, \tag{2.2}
$$

$L_n$ and $L_n^A$ are found to be asymptotically proportional to $\Lambda_1^n$, where $\Lambda_1$ is the largest eigenvalue of the substitution matrix, whereas the asymptotic density of $A$ letters involves the components of the corresponding eigenvectors

$$
\rho_\infty^A = \frac{V_1(1)}{\sum_i V_1(i)}. \tag{2.3}
$$

Fluctuations in the numbers of letters $L_n^A$, $L_n^B$, ..., are connected to the next-to-leading eigenvalue $\Lambda_2$.

In the case of the aperiodic quantum Ising chain considered above, with a two-letter sequence $(\lambda_k = \lambda_A, \lambda_B)$ and an averaged coupling $\overline{\lambda}$, one may write

$$
\lambda_A = \overline{\lambda} + \rho_\infty^B \delta, \quad \lambda_B = \overline{\lambda} - \rho_\infty^A \delta, \tag{2.4}
$$

where $\delta = \lambda_A - \lambda_B$. Then, at a length scale $L_n \sim \Lambda_1^n$, the sum of the deviations from the averaged coupling is

$$
\Delta(L_n) = \sum_{k=1}^{L_n} (\lambda_k - \overline{\lambda}) \simeq \delta \Lambda_2^n \simeq \delta L_n^\omega \tag{2.5}
$$

and involves the wandering exponent"30,31
$$
\omega=\frac{\ln \left|\Lambda_{2}\right|}{\ln \Lambda_{1}}.\qquad(2.6)
$$

When the number of letters is greater than 2, one may have two complex conjugate next-to-leading eigenvalues and the power law in Eq. (2.5) is modified by a factor which is periodic in $n \simeq \ln L_{n} / \ln \Lambda_{1}$.

The aperiodicity introduces a thermal perturbation above $\bar{\lambda}$ which, at a length scale $L$, is given on the average by
$$
\overline{\delta \lambda}(L)=\frac{\Delta(L)}{L}=\delta L^{\omega-1}.\qquad(2.7)
$$

Under a change of scale by a factor $b=L / L^{\prime}$ this transforms according to
$$
\overline{\delta \lambda^{\prime}}\left(L^{\prime}\right)=\delta^{\prime}\left(\frac{L}{b}\right)^{\omega-1}=b^{1 / \nu} \delta L^{\omega-1},\qquad(2.8)
$$
where $\nu$ is the bulk correlation length exponent. It follows that the perturbation amplitude $\delta$ scales like $^{22,24}$
$$
\delta^{\prime}=b^{\Phi / \nu} \delta,\qquad(2.9)
$$
with a crossover exponent
$$
\Phi=1+\nu(\omega-1).\qquad(2.10)
$$

As a consequence, for the two-dimensional Ising model with $\nu=1$, the aperiodic modulation is a relevant (irrelevant) perturbation when $\omega>0$ ($\omega<0$) and it becomes marginal when $\omega=0$. In the latter case a nonuniversal behavior is expected.

For a relevant aperiodic modulation, the form of the singular thermodynamical quantities can be deduced from scaling considerations. Let us consider the surface magnetization as a function of the thermal scaling field $t=1-\left(\lambda_{c} / \lambda\right)^{2}$ and the modulation amplitude $\delta$. In a scale transformation it behaves as
$$
m_{s}(t, \delta)=b^{-\beta_{s} / \nu} m_{s}\left(b^{1 / \nu} t, b^{\Phi / \nu} \delta\right),\qquad(2.11)
$$
where $\beta_{s}$ is the surface magnetization exponent. Taking the scale factor $b$ equal to the bulk correlation length $b=\xi=t^{-\nu}$, one obtains $m_{s}$ in the form
$$
m_{s}(t, \delta)=t^{\beta_{s}} F\left(\frac{l_{a}}{\xi}\right),\qquad(2.12)
$$
where the scaling function $F(x)$ involves a new characteristic length,
$$
l_{a}=|\delta|^{-\nu / \Phi},\qquad(2.13)
$$
which is introduced by the aperiodicity and remains finite at the bulk critical point.

In the following, an aperiodic sequence will be written as a succession of digits $f_{k}=0,1$, which are images $\Im(A, B)$ of the letters considered before. Then, with $\lambda_{1}=\lambda r$, $\lambda_{0}=\lambda$, one obtains $\lambda_{k}=\lambda r^{f_{k}}$ for the $k$ th coupling and the surface magnetization in Eq. (1.3) can be rewritten as
$$
m_{s}=[S(\lambda, r)]^{-1 / 2}, \quad S(\lambda, r)=\sum_{j=0}^{\infty} \lambda^{-2 j} r^{-2 n_{j}}, \quad(2.14)
$$
where
$$
n_{j}=\sum_{k=1}^{j} f_{k}, \quad n_{0}=0.\qquad(2.15)
$$

The critical coupling, $\lambda=\lambda_{c}$, is such that $^{32}$ $\lim _{L \to \infty} \prod_{k=1}^{L} \lambda_{k c}=\lim _{L \to \infty} \lambda_{c}^{L} r^{n_{L}}=1$, so that
$$
\lambda_{c}=r^{-\rho_{\infty}}, \quad \rho_{\infty}=\lim _{L \to \infty} \frac{n_{L}}{L}.\qquad(2.16)
$$

### III. THUE-MORSE SEQUENCE

As a first example, we consider the binary Thue-Morse sequence, $^{33}$ which may be deduced from the binary representation of non-negative integers, $0,1,10,11, \ldots$, by counting the sum of their digits modulo 2,
$$0 \ 1 \ 1 \ 0 \ 1 \ 0 \ 0 \ 1 \ \ldots \ .\qquad(3.1)$$

This sequence is also generated through the substitution
$$
\begin{cases}
A \to A B \\
B \to B A
\end{cases} \quad \text { or } \quad \begin{cases}
0 \to 0 \ 1 \\
1 \to 1 \ 0
\end{cases},\qquad(3.2)
$$
with $\Im(A, B)=(0,1)$, so that one obtains, successively,
$$
\begin{aligned}
& 0 \\
& 0 \ 1 \\
& 0 \ 1 \ 1 \ 0 \\
& 0 \ 1 \ 1 \ 0 \ 1 \ 0 \ 0 \ 1 \\
& \underline{0} \ 1 \ \underline{1} \ 0 \ \underline{1} \ 0 \ \underline{0} \ 1 \ \underline{1} \ 0 \ \underline{0} \ 1 \ \underline{0} \ 1 \ \underline{1} \ 0 \\
& \ldots
\end{aligned}\qquad(3.3)
$$

The corresponding substitution matrix (2.1) has eigenvalues $\Lambda_{1}=2, \Lambda_{2}=0$. The asymptotic density, $\rho_{\infty}=1 / 2$, is deduced from Eq. (2.3) and, according to Eq. (2.16),
$$
\lambda_{c}=r^{-1 / 2}.\qquad(3.4)
$$

The form of the substitution in Eq. (3.2) immediately leads to the recursion relations
$$
f_{2 p}=1-f_{p}, \quad f_{2 p+1}=f_{p+1}.\qquad(3.5)
$$

From the second one, the sequence of odd terms, underlined in (3.3), reproduces the whole sequence. Splitting

L. TURBAN, F. IGLÓI AND B. BERCHE
Phys. Rev. B 49 (1994) 12698

the sum giving $n_j$ into even and odd parts and using (3.5), one obtains
$$
\begin{aligned}
n_{2 p}=p, \quad n_{2 p+1}=p+f_{p+1}, \quad p=0,1,2, \ldots,
\end{aligned}
\tag{3.6}
$$
so that a chain with length $L=2 p$ has a density equal to the asymptotic one, $\rho_{\infty}=1 / 2$, which explains the vanishing second eigenvalue giving $\omega=-\infty$, i.e., no wandering in this case.

![](./images/867765699798368395_1.jpg)

FIG. 1. Thue-Morse surface magnetization as a function of $1-t=(\lambda_c/\lambda)^2$ for different values of the coupling ratio $r=\lambda_1/\lambda_0$. The critical exponent keeps its value for the homogeneous Ising system $\beta_s=1/2$ whereas the critical amplitude is $r$-dependent.

The sum $S(\lambda, r)$ involved in the surface magnetization (2.14) can be rewritten as
$$
\begin{aligned}
S(\lambda, r)= & \sum_{p=0}^{\infty} \lambda^{-2(2 p)} r^{-2 n_{2 p}}+\sum_{p=0}^{\infty} \lambda^{-2(2 p+1)} r^{-2 n_{2 p+1}} \\
& =\sum_{p=0}^{\infty}\left(\lambda^{2} r\right)^{-2 p}+\sum_{p=0}^{\infty} \lambda^{-2(2 p+1)} r^{-2 p-2 f_{p+1}}. \quad(3.7)
\end{aligned}
$$

Using the identity $a^{f_k}=1+(a-1)f_k\ (f_k=0,1)$ and the value of the critical coupling in Eq. (3.4), one obtains
$$
\begin{aligned}
S(\lambda, r)= & \frac{1+r\left(\lambda_{c} / \lambda\right)^{2}}{1-\left(\lambda_{c} / \lambda\right)^{4}}+\left(r^{-1}-r\right)\left(\lambda / \lambda_{c}\right)^{2} \Sigma\left[\left(\lambda_{c} / \lambda\right)^{4}\right], \\
\Sigma(x)= & \sum_{k=1}^{\infty} f_{k} x^{k}.
\end{aligned}
\tag{3.8}
$$

The Thue-Morse series, $\Sigma(x)$, satisfies a recursion relation which follows from Eq. (3.5),
$$
\Sigma(x)=\frac{x^{2}}{1-x^{2}}+\left(x^{-1}-1\right) \Sigma\left(x^{2}\right),
\tag{3.9}
$$
so that, iterating this relation,
$$
\Sigma(x)=x \sum_{k=0}^{\infty} \frac{x^{2^{k}} \prod_{p=0}^{k}\left(1-x^{2^{p}}\right)}{\left(1-x^{2^{k}}\right)\left(1-x^{2^{k+1}}\right)},
\tag{3.10}
$$
which is convergent for $x<1$. Equations (2.14), (3.8), and (3.10) give the surface magnetization shown in Fig. 1 for any value of $\lambda \geq \lambda_c$.

Near the critical point, $\lambda \rightarrow \lambda_{c+}$, the leading contribution to $S(\lambda, r)$ comes from the first two terms in Eq. (3.8). The next ones in $\Sigma\left[\left(\lambda_{c} / \lambda\right)^{4}\right]$ give the corrections to scaling. Collecting these results, the surface magnetization finally takes the form
$$
m_{s}=\frac{2 t^{1 / 2}}{\lambda_{c}+\lambda_{c}^{-1}}\left[1+\frac{1}{4}\left(\frac{1-\lambda_{c}^{2}}{1+\lambda_{c}^{2}}\right)^{2} t+O\left(t^{2}\right)\right], \quad(3.11)
$$
where $t$ is the deviation from the critical point defined in Sec. II. The surface magnetization exponent takes the value $\beta_s=1/2$ for homogeneous Ising systems in two dimensions as expected from scaling since $\omega<0$ here and the aperiodic modulation of the couplings is an irrelevant perturbation. The critical amplitude depends on $r$ through $\lambda_c$ in agreement with previous results. $^{29}$

## IV. PERIOD-DOUBLING SEQUENCE

We now turn to the period-doubling sequence which follows from the substitution $^{33,22}$
$$
\left\{\begin{array}{l}
1 \rightarrow 1 \ 0 \\
0 \rightarrow 1 \ 1
\end{array},\right.
\tag{4.1}
$$
leading to
$$
\begin{aligned}
& 1 \\
& 1 \ 0 \\
& 1 \ 0 \ 1 \ 1 \\
& 1 \ 0 \ 1 \ 1 \ 1 \ 0 \ 1 \ 0 \\
& 1 \ \underline{0} \ 1 \ \underline{1} \ 1 \ \underline{0} \ 1 \ \underline{0} \ 1 \ \underline{0} \ 1 \ \underline{1} \ 1 \ \underline{0} \ 1 \ \underline{1} \\
& \ldots
\end{aligned}
\tag{4.2}
$$

The eigenvalues of the substitution matrix are then $\Lambda_1=2$, $\Lambda_2=-1$ and the asymptotic density $\rho_{\infty}=2/3$ gives the critical coupling
$$
\lambda_{c}=r^{-2 / 3}.
\tag{4.3}
$$

The form of the substitution is such that $f_{2 p}=1-f_{p}$, $f_{2p+1}=1$, from which one deduces
$$
\begin{aligned}
n_{2 p}=2 p-n_{p}, \quad n_{2 p+1}=2 p+1-n_{p}, \quad p=0,1,2, \ldots.
\end{aligned}
\tag{4.4}
$$

Splitting the sum in $S(\lambda, r)$ into even and odd parts as in Eq. (3.7) and using (4.4), one obtains the following recursion relation:

L. TURBAN, F. IGLOÍ AND B. BERCHE
Phys. Rev. B 49 (1994) 12699

$$
S(\lambda, r)=\left(1+\frac{1}{\lambda^{2} r^{2}}\right) S\left(\lambda^{2} r^{2}, r^{-1}\right). \quad(4.5)
$$

After $l$ iterations the arguments in $S(\lambda, r)$ are changed into
$$
\begin{aligned}
\lambda_{l} & = \begin{cases}\lambda^{2^{l}} r^{\frac{2}{3}\left(2^{l}+1\right)}, & l \text { odd, } \\
\lambda^{2^{l}} r^{\frac{2}{3}\left(2^{l}-1\right)}, & l \text { even, }\end{cases} \\
r_{l} & =r^{(-1)^{l}}, \quad l=0,1,2, \ldots,
\end{aligned}
$$
and the series can be written as an infinite product
$$
S(\lambda, r)=\prod_{k=1}^{\infty}\left[1+\lambda_{c}\left(\frac{\lambda_{c}}{\lambda}\right)^{2^{2 k-1}}\right]\left[1+\lambda_{c}^{-1}\left(\frac{\lambda_{c}}{\lambda}\right)^{2^{2 k}}\right],
$$
which, together with (2.14), gives the surface magnetiza- tion shown in Fig. 2.

![](./images/867765699798368395_2.jpg)

FIG. 2. Period-doubling surface magnetization for different values of $r$. The exponent $\beta_{s}$ varies continuously with the modulation amplitude.

In order to analyze the critical behavior of the sur- face magnetization, one may use a scaling method intro- duced by one of us. $^{34}$ Let $S(u)$ denote the series expan sion of $S(\lambda, r)$ in powers of $u=(\lambda_{c} / \lambda)^{2}$ . According to Eq. (2.14), $S(u)$ should display a power law singularitynear the critical point:
$$S(u) \sim(1-u)^{-2 \beta_{s}}.\qquad(4.8)$$

It may be shown that in this case, the truncated series $S_{L}(u)$ given by the first L terms in S(u) behaves, for large values of L, as $L^{2 \beta_{s}}$ at the critical point, u=1. Now it may be verified that the first l terms in the infinite product (4.7) just contain the $L=2^{2 l}$ first terms of the series expansion. As a consequence, one obtains
$$S_{L=2^{2 l}}(1)=\left[\left(1+\lambda_{c}\right)\left(1+\lambda_{c}^{-1}\right)\right]^{l} \sim\left(2^{2 l}\right)^{2 \beta_{s}}, \quad(4.9)$$
 from which the surface magnetization exponent
$$\beta_{s}=\frac{\ln \left[\left(1+\lambda_{c}\right)\left(1+\lambda_{c}^{-1}\right)\right]}{4 \ln 2}\qquad(4.10)$$
 follows.

The same result can be obtained by considering therecursion relation (4.5) at the next step:
$$S(\lambda, r)=\left(1+\frac{1}{\lambda^{2} r^{2}}\right)\left(1+\frac{1}{\lambda^{4} r^{2}}\right) S\left(\lambda^{4} r^{2}, r\right). \quad(4.11)$$

At this stage the new coupling on the right-hand side is $\lambda'=\lambda^{4} r^{2}$ whereas r and, as a consequence, $\lambda_{c}$ remainunchanged. When $\lambda \to \lambda_{c}, S(\lambda, r)$ behaves as in Eq. (4.8) with an amplitude A(r) and, in the same way,
$$\begin{aligned}
S\left(\lambda^{4} r^{2}, r\right) & \simeq A(r)\left[1-\left(\frac{\lambda_{c}}{\lambda^{\prime}}\right)^{2}\right]^{-2 \beta_{s}} \\
& \simeq A(r)\left[1-\left(\frac{\lambda_{c}}{\lambda}\right)^{8}\right]^{-2 \beta_{s}},
\end{aligned}\qquad(4.12)$$
 where the value of $\lambda_{c}$ given in Eq. (4.3) was used. In troducing these results into (4.11) an equation for $\beta_{s}$ is obtained which leads to (4.10).
The surface magnetization exponent depends on the amplitude of the aperiodicity r through $\lambda_{c}$ as expected for this sequence since $\omega$ vanishes and the perturbation is marginal. The variation is shown in Fig. 3.

![](./images/867765699798368395_3.jpg)

FIG. 3. Marginal variation of surface exponent $\beta_{s}$ with the coupling ratio r for the period-doubling sequence. In the ape- riodic system the singularity is always weaker than in the ho- mogeneous one and the surface transition is of second order for any value of r.

Let $m_{s}(L)$ be the matrix element in Eq. (1.2) for a chain with length L. Although the spontaneous magne- tization vanishes on a finite chain, $m_{s}(L)$ remains nonvanishing and scales with L as $L^{-x_{s}}$ at the critical point $^{35,36}$  where $x_{s}=\beta_{s} / \nu$ is the scaling dimension of the surface magnetization. To the leading order in $L, m_{s}(L)$ is still given by Eq. (1.3) with a sum over j = 1, L so that the truncated series $S_{L}(1)$ considered above also behaves as

$L^{2x_s}$. It follows that $\beta_s = x_s$ and $\nu=1$: The marginal aperiodic modulation does not change the bulk correlation length exponent.

## V. RUDIN-SHAPIRO SEQUENCE

As a final example, we consider the Rudin-Shapiro sequence, $^{33,22}$ which is generated using a four-letter sub-stitution
$$
\begin{cases}
A & \to AB \\
B & \to AC \\
C & \to DB \\
D & \to DC
\end{cases}. \tag{5.1}
$$

One may take either single-digit images of the four letters in (5.1) with $^{22} \Im(A,B,C,D)=(0,0,1,1)$ or, more naturally, two-digit images with $\Im(A,B,C,D)=(00,01,10,11)$ so that
$$
\begin{cases}
00 \to 0001 \\
01 \to 0010 \\
10 \to 1101 \\
11 \to 1110
\end{cases}. \tag{5.2}
$$

The two processes lead to the same sequence of 1 and 0 since the two-digit images are related to the single-digit ones through a substitution on the letters. Starting on $A$, one obtains
$$
\begin{aligned}
& 0 \ 0 \\
& 0 \ 0 \ 0 \ 1 \\
& 0 \ 0 \ 0 \ 1 \ 0 \ 0 \ 1 \ 0 \\
& \underline{0} \ 0 \ \underline{0} \ 1 \ \underline{0} \ 0 \ \underline{1} \ 0 \ \underline{0} \ 0 \ \underline{0} \ 1 \ \underline{1} \ 1 \ \underline{0} \ 1 \\
& \dots
\end{aligned} \tag{5.3}
$$

The substitution matrix has leading eigenvalues $\Lambda_1=2$, $\Lambda_2=\pm\sqrt{2}$ so that $\omega=1/2$ and the asymptotic density $\rho_\infty=1/2$, obtained by taking a weighted average on the densities for the different letters, gives the critical coupling
$$
\lambda_c = r^{-1/2}. \tag{5.4}
$$

From the form of the substitution in Eq. (5.2), one easily deduces the following relations:
$$
\begin{aligned}
f_{4p}=1-f_{2p}, \quad f_{4p+1}=f_{4p+2}=f_{2p+1}, \quad f_{4p+3}=f_{2p+2}.
\end{aligned} \tag{5.5}
$$

Furthermore, one may notice that odd terms, underlined in (5.3), reproduce the sequence itself whereas even terms either reproduce the sequence or its complement to one, so that:
$$
f_{2p+1}=f_{p+1}, \quad f_{2p+2}=
\begin{cases}
1-f_{p+1}, & p \text{ odd}, \\
f_{p+1}, & p \text{ even}.
\end{cases} \tag{5.6}
$$

![](./images/867765699798368395_4.jpg)

FIG. 4. Surface magnetization for the Rudin-Shapiro sequence with a coupling ratio $r \leq 1$. The enhancement of the coupling strength near to the surface leads to a first-order surface transition when $r < 1$.

![](./images/867765699798368395_5.jpg)

FIG. 5. Surface magnetization for the Rudin-Shapiro sequence with $r \geq 1$. The surface magnetization vanishes with an essential singularity at the bulk critical point when $r > 1$.

Using these properties one may write a recursion relation similar to (4.5), but here in matrix form, between the odd and even parts of $S(\lambda,r)$. Although the matrix considerably simplifies at the bulk critical point, some of its elements still depend on the iteration index $l$. As a consequence, we were unable to deduce the critical behaviour from this recursion relation like in Sec. IV.

Numerical results for the surface magnetization are shown in Figs. 4 and 5 for $r < 1$ and $r > 1$, respectively. In the first case, one obtains a first order surface transition, which is linked to a local enhancement of the couplings relative to their averaged value. On the other side, when $r > 1$, the couplings near the surface are locally weaker than the average and the surface magnetization vanishes at the bulk critical point with a singularity which is seemingly weaker than any power law. In the bulk, the situation is different since the deviations from the average have both signs with the same probability.

L. TURBAN, F. IGLÓI AND B. BERCHE
Phys. Rev. B 49 (1994) 12701

That the first order transition is indeed a surface effect can also be made plausible through the following argument: If one started the sequence with $D$ instead of $A$, the bulk properties should not change but one can check on Eqs. (5.1) and (5.2) that it would amount to exchange weak and strong couplings along the sequence, and the first order surface transition would then occur for $r>1$.

The discontinuity of the critical surface magnetization shown in Fig. 6 appears to vary linearly with the coupling ratio $r<1$. This behavior will be explained in Sec. VI using scaling arguments.

![](./images/867765699798368395_6.jpg)

FIG. 6. Surface magnetization discontinuity at the bulk critical point as a function of the coupling ratio for the Rudin-Shapiro sequence with increasing sizes, $L=2^{11}$ to $2^{18}$, from top to bottom. The variation is asymptotically linear in $r$.

## VI. DISCUSSION

The QIM on aperiodic lattices studied in this paper shows a rich critical behavior. Depending on the value of the wandering exponent $\omega$, scaling arguments show that the perturbation introduced by the aperiodic modulation can be either irrelevant, marginal or relevant. This has been verified on three specific sequences for which the different typical behaviors are observed.

For the period-doubling sequence, displaying a marginal modulation, the surface critical exponent $\beta_{s}$ and the corresponding scaling dimension $x_{s}=\beta_{s}/\nu$ are nonuniversal and show the same continuous variation with the strength of the modulation. As a consequence $\nu$ itself stays constant, keeping its value in the homogeneous system, $\nu=1$. Thus the marginality condition $1/\nu=1-\omega$ is fulfilled along the critical line, as required. On the other hand one knows from numerical studies $^{22}$ that the bulk specific heat exponent $\alpha$ does vary with $\delta$ so that the hyperscaling relation $d\nu=2-\alpha$ is violated for this marginal sequence. Such a violation of hyperscaling is likely to occur for other marginal sequences too. It may be due to the presence of a dangerous irrelevant variable in the problem. $^{37}$

![](./images/867765699798368395_7.jpg)

FIG. 7. Logarithm of the reduced surface magnetization as a function of $x^{-1}$ for the Rudin-Shapiro sequence with $r>1$ and $L=2^{16}$. The linear variation (dashed line) is in agreement with the stretched exponential form in Eq. (6.3). Deviations from scaling are mainly due to finite-size effects.

With the Rudin-Shapiro sequence, the relevant modulation was found to lead to different surface critical behaviors, depending on whether the coulings near to the surface are greater or smaller than their average. In the first case, the surface stays ordered at the bulk critical point. The variation with $r$ of surface magnetization discontinuity can be deduced from the scaling form in Eq. (2.12). For $m_{s}(0,\delta)$ to remain finite at the bulk critical point, the $t$ dependence on the right-hand side has to cancel. The scaling function then behaves as a power of its argument which follows from the cancellation, leading to

$$
m_{s}(0,\delta) \sim l_{a}^{-x_{s}} \sim|\delta|^{\beta_{s}/\Phi}. \tag{6.1}
$$

In the present case the exponent is equal to 1 and the discontinuity varies as $|\delta|=1-r$ in agreement with the numerical results in Fig. 6.

The same behavior is obtained in the the Hilhorst-van Leeuwen (HvL) model $^{38}$ in the case of an inhomogeneity decaying as $AL^{-y}$ where $L$ is the distance from the free surface. In this case the crossover exponent is $1-\nu y$ so that, according to (2.10), $y$ corresponds to $1-\omega$ which, in the present problem, is the decay exponent for the average deviation of the couplings given in Eq. (2.7). The jump of the surface magnetization in the Ising HvL model has been obtained analytically $^{28}$ for a relevant perturbation with $A>0$ and is in agreement with (6.1).

When $r>1$, the local couplings at the surface are in average weaker than the critical one and, according to the numerical results shown in Fig. 5, the surface order vanishes in an anomalous way. In order to obtain the form of the scaling function $F(x)$ in Eq. (2.12), one may use the abovementioned analogy with the HvL model as done in Ref. 24. An argument of Burkhardt, $^{39}$ going beyond scaling theory, leads to a stretched exponential behavior for the critical correlation function, from which the leading singularity of the susceptibility can be deduced, $^{24}$

$$
\chi \sim \exp \left[-C_{s} x^{\Phi /(\Phi-1)}\right]. \tag{6.2}
$$

In this expression $x = l_a/\xi$ is the scaling variable defined in Eq. (2.12). The same form is likely to occur in the temperature dependence of other singular quantities and one expects the reduced surface magnetization to behave as
$$
\frac{m_{s}}{t^{\beta_{s}}} \sim \exp \left[-C_{m} x^{1+1 / \nu(\omega-1)}\right], \tag{6.3}
$$
where $C_m$ is some constant. The scaling function may also involve some unknown power of $x$ in front of the exponential. This expression, when properly translated, is in agreement with the analytical result obtained by Peschel for the surface inhomogeneity. $^{28}$ For the aperiodic Ising model with Rudin-Shapiro modulation, $\omega=1 / 2$ and $\nu=1$, so that the argument of the exponential in Eq. (6.3) is $x^{-1}=(r-1)^{2} / t$. The numerical results shown in Fig. 7, although perturbed by finite-size effects, confirm the proposed scaling form.

All these systems containing a characteristic length, which, like $l_a$, stays finite at the bulk critical point when the perturbation is relevant, seem to display the same type of critical behaviour. Besides the two examples considered so far, one may also mention systems limited by a surface with a parabolic shape, for which the characteristic length is fixed by the geometry. $^{40}$ They also differ in some aspects: In the marginal HvL model, for instance, the surface transition is first order when the amplitude of the inhomogeneity is positive and strong enough, whereas it remains second order for the period-doubling modulation studied here, whatever the modulation amplitude.

## ACKNOWLEDGMENTS

The authors are indebted to J. M. Luck for communicating his work, prior to publication. This work was supported by the C.N.R.S. and the Hungarian Academy of Sciences through an exchange program. F.I. gratefully acknowledges support by the National Hungarian Research Fund under grant No OTKA TO12830. The Laboratoire de Physique du Solide is Unité de Recherche Associée au C.N.R.S. No 155.

$^{1}$ D. Shechtman, I. Blech, D. Gratias, and J. W. Cahn, Phys. Rev. Lett. 53, 1951 (1984).
$^{2}$ C. L. Henley, Comments Condens. Matter Phys. 13, 59 (1987).
$^{3}$ T. Janssen, Phys. Rep. 168, 55 (1988).
$^{4}$ C. Janot, J. M. Dubois, and M. de Boissieu, Am. J. Phys. 57, 972 (1989).
$^{5}$ P. Guyot, P. Kramer, and M. de Boissieu, Rep. Prog. Phys. 54, 1373 (1991).
$^{6}$ Quasicrystals: The State of the Art, edited by P. Steinhardt and D. DiVicenzo (World Scientific, Singapore, 1991).
$^{7}$ C. Godrèche, J. M. Luck, and H. J. Orland, J. Stat. Phys. 45, 777 (1986).
$^{8}$ Y. Okabe and K. Niizeki, J. Phys. Soc. Japan 57, 1536 (1988).
$^{9}$ E. S. Sørensen, M. V. Jarić, and M. Ronchetti, Phys. Rev. B 44, 9271 (1991).
$^{10}$ S. Sakamoto, F. Yonezawa, K. Aoki, S. Nosé, and M. Hori, J. Phys. A 22, L705 (1989).
$^{11}$ C. Zhang and K. De'Bell, Phys. Rev. B 47, 8558 (1993).
$^{12}$ G. Langie and F. Iglói, J. Phys. A 25, L487 (1992).
$^{13}$ Y. Okabe and K. Niizeki, J. Phys. A 23, L733 (1990).
$^{14}$ J. Kogut, Rev. Mod. Phys. 51, 659 (1979).
$^{15}$ F. Iglói, J. Phys. A 21, L911 (1988).
$^{16}$ M. M. Doria and I. I. Satija, Phys. Rev. Lett. 60, 444 (1988).
$^{17}$ G. V. Benza, Europhys. Lett. 8, 321 (1989).
$^{18}$ M. Henkel and A. Patkós, J. Phys. A 25, 5223 (1992).
$^{19}$ Z. Lin and R. Tao, J. Phys. A 25, 2483 (1992).
$^{20}$ C. A. Tracy, J. Phys. A 21, L603 (1988).
$^{21}$ B. M. McCoy and T. T. Wu, Phys. Rev. Lett. 21, 549 (1968); Phys. Rev. 176, 631 (1968); B. M. McCoy, Phys. Rev. B 2, 2795 (1970).
$^{22}$ J. M. Luck, J. Stat. Phys. 72, 417 (1993).
$^{23}$ A. B. Harris, J. Phys. C 7, 1671 (1974).
$^{24}$ F. Iglói, J. Phys. A 26, L703 (1993).
$^{25}$ J. M. Luck, Europhys. Lett. 24, 359 (1993).
$^{26}$ T. D. Schultz, D. C. Mattis, and E. H. Lieb, Rev. Mod. Phys. 36, 856 (1964).
$^{27}$ E. H. Lieb, T. D. Schultz, and D. C. Mattis, Ann. Phys. (N. Y.) 16, 406 (1961).
$^{28}$ I. Peschel, Phys. Rev. B 30, 6783 (1984).
$^{29}$ L. Turban and B. Berche, Z. Phys. B 92, 307 (1993).
$^{30}$ J. M. Dumont, in Number Theory and Physics, Springer Proceedings in Physics, Vol. 47, edited by J. M. Luck, P. Moussa, and M. Waldschmidt (Springer, Berlin, 1990), p. 185.
$^{31}$ We abandon the usual notation $\beta$ for this exponent in order to avoid a confusion with the magnetization exponent.
$^{32}$ P. Pfeuty, Phys. Lett. 72A, 245 (1979).
$^{33}$ M. Dekking, M. Mendès-France, and A. van der Poorten, Math. Intelligencer 4, 130 (1983).
$^{34}$ F. Iglói, J. Phys. A 19, 3077 (1986).
$^{35}$ C. J. Hamer, J. Phys. A 15, L675 (1982).
$^{36}$ H. Takano and Y. Saito, Prog. Theor. Phys. 73, 1369 (1985).
$^{37}$ M. E. Fisher, in Renormalization Group in Critical Phenomena and Quantum Field Theory, edited by J. D. Gunton and M. S. Green (Temple University, Philadelphia, 1974), p. 65.
$^{38}$ H. J. Hilhorst and J. M. J. van Leeuwen, Phys. Rev. Lett. 47, 1188 (1981).
$^{39}$ T. W. Burkhardt, Phys. Rev. Lett. 48, 216 (1982).
$^{40}$ F. Iglói, I. Peschel, and L. Turban, Adv. Phys. 42, 683 (1993), (cond-mat/9312077).