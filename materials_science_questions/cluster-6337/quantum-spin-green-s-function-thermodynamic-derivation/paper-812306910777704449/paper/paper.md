HIGHER-ORDER INTERACTIONS IN THE LINEAR ISING MODEL

I. S. Donskaya

The linear Ising model with many-particle interactions of arbitrary form is considered. By means of difference equations an exact solution is obtained for the correlation functions of the model, and the general behavior for the two-spin correlation functions in their dependence on the length of the complex of interacting particles is established. The case of a three-particle interaction is analyzed in detail.

1. Lattice statistical models play an important part in the modern theory of phase transitions. The exact solutions for the planar Ising lattice [1] and the Baxter model [2] have made it possible to answer a number of fundamentally important questions relating to cooperative phenomena. The class of investigated lattice models is fairly large and includes not only models with two-particle but also many-particle interactions. The occurrence of many-particle interactions can significantly change the behavior of systems, and the investigation of such influences has become an important and independent task. The transition from the planar Ising lattice to the Baxter model is associated with the inclusion of additional four-particle interactions [3]. The Ising model with triple interactions on a triangular lattice is also the subject of intense theoretical studies [4].

There has recently been a strong growth of interest in linear models of magnetic systems with multispin interactions. For example, four-particle interactions arise from the construction of the effective Hamiltonian of a one-dimensional spin chain contained in a three-dimensional anharmonic lattice [5].

In the present paper, we consider the linear Ising model with many-particle interac- tion of arbitrary order n, the operator of which is represented in the form

$$
H=-J \sum_{j=1}^{N} S_{j}^{z} S_{j+1}^{z} \ldots S_{j+n-1}^{z}, \tag{1}
$$

where J is the constant of the exchange interaction, and N is the number of spins in the chain. An exact solution for the correlation functions of the model is obtained. In particular, for the two-spin correlation functions we establish the dependence on the distance between the spins and show that these functions can be expressed in terms of powers of $\tanh(J/2^{n}k_{B}T)$. For the example of the case n = 3 we show that one of the specific features of the many-particle interaction is manifested in the fact that there is no correlation between certain closely spaced spins.

2. We consider the linear Ising model with spin $S=\frac{1}{2}$. Because the Hamiltonian (1) contains only the $S^{z}$ components of the spin operators, the equation of motion for $S^{\pm}$ takes the form

$$
i \frac{d}{d t} S_{k}^{ \pm}=\left[S_{k}^{ \pm} H\right]=S_{k}^{ \pm} \sigma_{k},
$$

where the operator

$$
\sigma_{k}=J\left\{S_{k}^{z}\right\}^{-1} \prod_{i=0}^{n-1} \sum_{j=0}^{n-1} S_{k+i-j}^{z} \tag{2}
$$

determines a cluster of interacting particles.

Following the method developed in [6,7], we introduce two-time Green's functions of

Physicotechnical Institute, Kazan Branch of the USSR Academy of Sciences, Kazan.
Translated from Teoreticheskaya i Matematicheskaya Fizika, Vol. 74, No. 3, pp. 474-480,
March, 1988. Original article submitted October 1, 1986.

324
0040-5779/88/7403-0324$12.50 © 1988 Plenum Publishing Corporation

order m:
$$\langle\langle S_{k}^{+}\left(\sigma_{k}\right)^{m} A | B\rangle\rangle=\theta\left(t-t^{\prime}\right)<\left[S_{k}^{+}(t) \sigma_{k}^{m}(t) A(t), B\left(t^{\prime}\right)\right]\rangle,\tag{3}$$
where $\theta(t-t')$ is the step function, $A = A(i)$ is some function of the operator $S_{i}^{z}(i \neq k)$, and the spin operator B is arbitrary.

The system of coupled equations of motion for the Fourier transforms of the Green's functions (3) is determined by the recursion relation
$$\omega\left\langle\left\langle S_{j}^{+} \sigma_{k}^{m} A | B\right\rangle\right\rangle_{\omega}=\frac{i}{2 \pi}\left\langle\left[S_{j}^{+} \sigma_{k}^{m} A, B\right]\right\rangle+\left\langle\left\langle S_{j}^{+} \sigma_{k}^{m+1} A | B\right\rangle\right\rangle_{\omega}.\tag{4}$$

A specific feature of the Ising model is that the hierarchy of equations of motion (4) permits a rigorous decoupling. The decoupling procedure is based on the fact that with increasing m only the power of $\sigma_{k}$ increases. At a certain stage the condition $S_{z}^{2}=1 / 4$ makes it possible to express $\sigma_{k}^{m}$ in terms of lower powers of $\sigma_{k}$ and obtain a "reduction relation" for this operator that closes the hierarchy of Eqs. (4) rigorously.

In the general case, the operator reduction relation is a product of m binomial terms
$$\prod_{l=1}^{m}\left(\sigma-\varepsilon_{l}\right)=0,\tag{5}$$
each of which is an eigenvalue equation for the operator $\sigma$. For the actual construction of the relation (5), it is sufficient to determine the energies of all possible configurations of the spins $(2^{n-1})$ forming the cluster of interacting particles. An analysis of this kind for the expression (2) shows that for arbitrary n
$$\varepsilon_{l}=\left\{\begin{array}{ll}
\pm J \frac{2 l+1}{2^{n-1}}, & n=2 l^{\prime}+1 \\
\pm J \frac{2 l}{2^{n-1}}, & n=2 l^{\prime}
\end{array}, \quad 0 \leqslant l \leqslant l^{\prime}.\right.\tag{6}$$

The "reduction relation" (5) makes it possible to express the Green's functions of higher order in terms of those of lower orders and rigorously close the hierarchy of Eqs. (4). The formal solution of these equations leads to many-pole Green's functions. However, by means of linear transformations one can go over to single-pole functions, the solution for which can be expressed in the form
$$\left\langle\left\langle S_{k}^{+} Q_{l} A | B\right\rangle\right\rangle_{\omega}=\frac{i}{2 \pi} \frac{\left\langle\left[S_{k}^{+} Q_{l} A | B\right]\right\rangle}{\omega-\varepsilon_{l}},\tag{7}$$
where $Q_{\ell}$ are polynomials in powers of the operators $\sigma: Q_{l}=\prod_{j=1}^{n} \frac{\sigma-\varepsilon_{j}}{\sigma-\varepsilon_{l}}$. The changes in the energy due to the reorientation of one spin $\varepsilon_{\ell}$ are the poles of the Green's functions (7) and, therefore, [8], form the spectrum of elementary excitations of the model.

For $B = S_{k}^{-}$, the Green's functions (7) lead to exact relations for the correlation functions:
$$\left\langle S_{k}^{z} Q_{l} A\right\rangle=1 /{ }_{2}\left\langle Q_{l} A\right\rangle \operatorname{th} \beta \varepsilon_{l}.\tag{8}$$

Here, $\beta=\frac{1}{2} k_{B} T$ ($k_{B}$ is Boltzmann's constant, and k is the number of the distinguished cluster of interacting particles). Because $A(i)$ is arbitrary, these relations have a recursive nature and serve to describe all the correlation functions that characterize the system. To determine a set of linearly independent relations associated with the cluster of an individual particle, it is expedient to obtain one "generating equation" from the system of equations (8). For this, we sum the relations (8) over $\ell$ with coefficients $h_{\ell}$, which we determine from the condition $\sum_{l} h_{l} Q_{l}=1$. As a result, we obtain the "generating equation," which has the form
$$\left\langle S_{k}^{z} A\right\rangle=\frac{4}{3}\left\langle\left(\sigma_{k}^{3}-\frac{1}{16} \sigma_{k}\right) A\right\rangle \operatorname{th} \frac{3 J \beta}{4}-4\left\langle\left(\sigma_{k}^{3}-\frac{9}{16} \sigma_{k}\right) A\right\rangle \operatorname{th} \frac{J \beta}{4}\tag{9a}$$
for n = 3 and

$$
\left\langle S_{k}{ }^{z} A\right\rangle=\frac{8}{3}\left\langle\left(\sigma_{k}-4 \sigma_{k}{ }^{3}\right) A\right\rangle \operatorname{th} \frac{J \beta}{4}-\frac{1}{3}\left\langle\left(\sigma_{k}-16 \sigma_{k}{ }^{3}\right) A\right\rangle \operatorname{th} \frac{J \beta}{4}
\tag{9b}
$$

for n = 4. The relation (9b) is given in [9]. Taking as A various spin operators surrounding the central particle of cluster k, we obtain the from relations (9a) and (9b) a complete system of linearly independent equations. We shall regard all r-particle correlation functions as one and the same function $\varphi_{r}^{j}$, taken for different values of the spatial variables. Then the linearly independent relations for the correlation functions represent a system of difference equations, which determine the dependence of the correla- tion functions on the spatial coordinates. The solution of these equations is associated in the first place with linear transformations, which lead to relations formed from correlation functions of the same kind. The validity of this step follows from the general theory of difference equations [10]. Most convenient for investigation are the relations that contain only "single-particle" correlation functions of the form $\langle S_{k}^{z} A^{*}\rangle$, $A^{*}=A(i)$, where $i$ is the index of a particle that does not belong to the distinguished cluster of interacting particles of particle k.

The symmetry of the linear model is such that such a difference equation can be written down in the most general case for arbitrary n:
$$
\sum_{l}(-1)^{l}\left(\begin{array}{c}
n-2 \\
l
\end{array}\right)\left\{\left\langle S_{k+n(n-l)}^{z} A^{*}\right\rangle-2\left(2 \operatorname{cth}^{2} 2 x_{n}-1\right)\left\langle S_{k+n^{2}-n(l+1)} A^{\prime}\right\rangle+\left\langle S_{k+n^{2}-n(l+2)}^{z} A^{*}\right\rangle\right\}=0,
\tag{10}
$$
where $x_{n}=J / 2^{n} k_{B} T$, and $\left(\begin{array}{c}n-2 \\ l\end{array}\right)$ are binomial coefficients.

The relation (10) is a homogeneous difference equation of order $n^{2}$. The solution of this equation has the form
$$
\left\langle S_{k}{ }^{z} A^{*}\right\rangle=\sum_{l=1}^{n^{2}} C_{l}\left(A^{*}\right) \lambda_{l}{ }^{k},
\tag{11}
$$
where $\lambda_{\ell}$ are roots of the characteristic equation, which, after the substitution $z=\lambda^{n}$, can be represented in the form
$$
(z-1)^{n-2}\left(z-\operatorname{th}^{2} x_{n}\right)\left(z-\operatorname{cth}^{2} x_{n}\right)=0.
$$

This equation can be divided into three parts, which give three basic values of the root: $z_{1}=\tanh ^{2} x_{n}, z_{2}=\operatorname{coth}^{2} x_{n}, z_{3}=1$. The relation $z=\lambda^{n}$ leads to additional phase factors $\overline{v_{1}}=\exp \left(\frac{2 \pi l}{n} i\right) ; l=0, \ldots, n-1$, whose presence makes it possible to go over in a natural manner from linear labeling of the spins in the lattice to the two-dimensional labeling (k = pn + q, p = 0, ..., N - 1, q = 0, ..., n - 1) and represent the entire model in the form of a spiral wound onto a cylinder. Each winding of the spiral includes n spins, and along the cylinder one can draw n straight lines. The indices of the two- dimensional labeling will determine, respectively, the number of the winding (p) and the number of the line along the cylinder (q). Indeed, it follows from the solution (11) that the values of the coordinates occur only as exponents of the roots $\lambda_{\ell}$. The power pn has no influence on the phase factor, and it depends only on the number of the line.

The spatial solution for any correlation function of the model must be expressed in the most general form as
$$
\left\langle S_{k}{ }^{z} A^{*}\right\rangle=\sum_{l^{\prime}=1}^{3} \sum_{l=1}^{n} C_{l}^{\left(l^{\prime}\right)}\left(A^{*}\right) z_{l^{\prime}}^{k / n} \exp \left\{i \frac{2 \pi l}{n} k\right\}.
\tag{12}
$$

To determine the constants, we specify first of all the boundary conditions. In the present paper, we consider an infinite linear chain, and this makes it necessary to consider the values of the correlation functions in the limit $k \to \infty$. By definition, the correlation functions are bounded: $\langle S_{k_{1}}^{z} S_{k_{l}}^{z} \ldots S_{k_{n}}^{z}\rangle \leqslant 2^{-n}$. From the condition of their boundedness as $k \to \infty$ it follows that in the spatial solution (12) the coefficients $C_{l}^{(2)}(A^{*})=0$. With increasing k, the terms in (12) for $\ell^{\prime}=1$ will decrease, and the absolute magnitude of the terms with $\ell^{\prime}=3$ remains unchanged, this corresponding to the existence in the system of long-range order. However, as is shown in [11], in one-dimensional systems there is in principle no spontaneous magnetization, and we must therefore impose a

condition on the constants: $C_{l}^{(3)}(A^{*})=0$. As a result, we obtain the general spatial solution in the form

$$
\left\langle S_{k}{ }^{z} A^{*}\right\rangle=\sum_{l=1}^{n} C_{l}\left(A^{*}\right)\left\{\operatorname{th} x_{n}\right\}^{2 k / n} \exp \left\{i \frac{\pi l}{n} k\right\},
\tag{13}
$$

on the basis of which we can determine the explicit form of any correlation function.

We consider the simplest case of the two-particle correlation function $\langle S_{k}^{z} S_{k'}^{z}\rangle$. In the spatial solution (13), we set $A^{*}=S_{0}^{z}$, and to determine the constants $C_{\ell}(S_{0}^{z})$ we use the system of exact relations obtained above. The simplest relation is obtained from the normalization condition

$$
\left\langle S_{0}{ }^{z} S_{0}{ }^{z}\right\rangle=\sum_{l} C_{l}\left(S_{0}{ }^{z}\right)=1 / 4.
\tag{14}
$$

It alone is sufficient to determine completely the correlations of two spins lying on one line of the cylinder. Since in this case all the phase factors vanish and a sum of constants equal to 1/4 is obtained,

$$
\left\langle S_{p n}{ }^{z} S_{0}{ }^{z}\right\rangle=1 / 4\left\{\operatorname{th} x_{n}\right\}^{2 p}.
\tag{15}
$$

It follows from the expression (15) that the structure of the simplest correlation functions (along the line on the cylinder) of the considered linear model with interactions of higher order is identical to structure of the ordinary linear Ising model and can be expressed in terms of powers of the function $\tanh (J / 2^{n} k_{B} T)$.

3. A specific feature of the many-particle interaction is manifested in the fact that the correlation functions between spins on different lines of the cylinder can have important features.

We show this for the example of the three-particle interaction (n = 3), for which the expression for the two-spin correlation functions takes the form

$$
\left\langle S_{k}{ }^{z} S_{0}{ }^{z}\right\rangle=\left\{\operatorname{th} x_{3}\right\}^{2 p+2 q / 3} \sum_{l=0,1,2} C_{l} \exp \left\{i \frac{2 \pi}{3} l q\right\}, \quad x_{3}=\frac{J}{8 k_{B} T}.
\tag{16}
$$

For q = 0, p = 1 the normalization condition (14) makes it possible to obtain the exact value of the correlation function, $\langle S_{3}^{z} S_{0}^{z}\rangle=1 / 4\{\tanh x_{3}\}^{2}$, which is used in what follows to determine the constants $C_{\ell}$.

If in the basic system (9a) we restrict the treatment to the correlation functions within one cluster, i.e., we set $A^{*}=1$ [12], then we can separate four equations determining the correlation functions $(\varphi_{2}^{(j)}(S_{0}^{z})=\langle S_{j}^{z} S_{0}^{z}\rangle, j=1,2 ; \varphi_{3}^{(j)}(S_{0}^{z})=\langle S_{j}^{z} S_{j+1}^{z} S_{0}^{z}\rangle, j=2,3)$

$$
\begin{aligned}
& \varphi_{2}^{(1)}\left(2 g+f \operatorname{th}^{2} x_{3}\right)+g \varphi_{2}^{(2)}=0, \quad g \varphi_{3}^{(2)}+f \varphi_{3}^{(3)}-\varphi_{2}^{(1)}=0, \\
& \varphi_{2}^{(1)}\left(g+f+g \operatorname{th}^{2} x_{3}\right)+g \varphi_{2}^{(2)}-4 \varphi_{3}^{(2)}=0, \quad g\left(\varphi_{3}^{(2)}+\varphi_{3}^{(3)}\right)-\varphi_{2}^{(2)}=0.
\end{aligned}
\tag{17}
$$

We have here used the fact that $\langle S_{0}^{z}\rangle=0$ and introduced the notation $g=2 \sinh x_{3} \cosh 2 x_{3} /$ $\cosh ^{3} x_{3}, f=-4 \sinh ^{3} x_{3} / \cosh 3 x_{3}$. The system (17) is homogeneous and has the trivial solution $\left.\varphi_{2}^{(j)}(S_{0}^{z})\right|_{j=1,2}=\left.\varphi_{3}^{(j)}(S_{0}^{z})\right|_{j=2,3}=0$, from which it follows that all the coefficients are equal to each other, $C_{\ell}=1 / 12$. This leads to the following result, which at the first glance is unexpected, namely, the two-spin correlation functions connecting spins on different lines on the cylinder are equal to zero.

To clarify the physical reasons for this feature, we consider the correlation function $\langle S_{j}^{z} S_{j+1}^{z}\rangle$ and the energy operator $J S_{j}^{z} S_{j+1}^{z} S_{j+2}^{z}$. It follows from the form of the operator that simultaneous change of the states of any two spins does not change its value, i.e., the four states of the spins $S_{j}^{z}, S_{j+1}^{z}$ go over into two states that are degenerate with respect to the energy. It is easy to show that this degeneracy is complete - all states associated with the two spins $S_{j}^{z}, S_{j+1}^{z}$ are equally probable, and this leads to the absence of correlation between them.

For the same reason the three-spin correlation functions in (17) are equal to zero, whereas the correlation function that determines the mean value of the energy per spin takes the form

$$\langle S_{j}^{z}S_{j+1}^{z}S_{j+2}^{z}\rangle =1/8\ \text{th}\ x_{3},$$

and also

$$\langle S_{j}^{z}S_{j+2}^{z}S_{j+4}^{z}\rangle =1/8\ \text{th}^{3}x.$$

The influence of the interactions of higher order in the linear Ising model is manifested in these particular properties of the correlation functions.

On the basis of the calculated correlation functions $\varphi_{2}^{(j)}$ we can easily determine the magnetic susceptibility of the system [13]. In the case n = 3,

$$\chi=\frac{1}{N k_{\mathrm{B}} T} \sum_{i} \sum_{j}\left\langle S_{i}{ }^{z} S_{j}{ }^{z}\right\rangle=\frac{1}{4 k_{\mathrm{B}} T} \operatorname{ch} 2 x_{3}.$$

We note that the individual correlation functions of the model can also be calculated by means of a change of the spin variables of the type $\langle S_{j}^{z} S_{j+1}^{z}\rangle=1 / 4 \tau_{j}$ [14]. However, by this method is not possible to calculate all the correlation functions and obtain for them a comprehensive spatial solution.

I thank G. O. Berim and A. R. Kessel' for fruitful discussions of the work.

## LITERATURE CITED

1. B. Kaufman, Phys. Rev., 76, 1232 (1949).
2. R. J. Baxter, Phys. Rev. Lett., 26, 832 (1971).
3. F. Y. Wu, Phys. Rev. B, 4, 2312 (1971).
4. R. J. Baxter and F. Y. Wu, Aust. J. Phys., 27, 357, 369 (1974).
5. M. Milatovic' and S. Miloševic', Phys. Status Solidi B, 82, 193 (1977).
6. M. P. Zhelifonov, Teor. Mat. Fiz., 8, 401 (1971).
7. M. P. Zhelifonov and R. T. Galiullin, Phys. Lett. A, 42, 417 (1973).
8. S. V. Tyablikov, Methods of Quantum Theory of Magnetism, Plenum Press, New York (1967).
9. R. T. Galiullin and M. P. Zhelifonov, in: Proc. International Conference on Magnetism (1973), Vol. 4 [in Russian], Nauka, Moscow (1974), p. 259.
10. A. O. Gel'fond, The Calculus of Finite Differences [in Russian], Nauka, Moscow (1967).
11. D. C. Mattis, The Theory of Magnetism, 2nd ed., rev., Springer Series in Solid-State Sci., Vol. 17, Berlin (1981).
12. A. R. Kessel' and G. O. Berim, Magnetic Resonance of Ising Magnets [in Russian], Nauka, Moscow (1982).
13. R. J. Baxter, Exactly Solved Models in Statistical Mechanics, Academic Press, New York (1982).
14. B. U. Felderhov and M. Suzuki, Physica (Utrecht), 56, 43 (1971).