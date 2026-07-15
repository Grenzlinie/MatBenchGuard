![](./images/813094360756256769_1.jpg)

# Correlation functions in fully frustrated Ising models

J.R. Gonçalves ${ }^{a, *}$, J. Poulter ${ }^{\mathrm{b}}$, J.A. Blackman ${ }^{\mathrm{a}}$

${ }^{\text {a }}$ Dept. of Physics, University of Reading, Reading RG6 2AF, UK
${ }^{\mathrm{b}}$ Dept. of Mathematics, Faculty of Science, Mahidol University, Bangkok 10400, Thailand

## Abstract

The spin-spin correlation functions in the ground state of certain 2D fully frustrated Ising models fall off with distance with exponent $\eta=\frac{1}{2}$. This is known both numerically and from calculations that are special to each model. This value of the exponent contrasts with $\eta=\frac{1}{4}$ for the unfrustrated systems at $T_{\mathrm{c}}$. The purpose of this paper is to develop a common method that is applicable to both frustrated and unfrustrated systems.

A number of years ago it was realized that the spin-spin correlation functions of some two-dimensional fully frustrated Ising spin models are long-ranged at $T=0$ and decay as $R^{-\eta}$, where $R$ is the distance between the spins, and $\eta$ appears to take the common value of $\eta=\frac{1}{2}$ for a number of systems. This contrasts with the value $\eta=\frac{1}{4}$ for the two-dimensional Ising ferromagnet at temperature $T_{\mathrm{c}}$.

The systems studied include the triangular antiferromagnet [1], the Villain model [2] and the fully frustrated union-jack lattice [3]. Besides numerical calculations, a number of analytical techniques were used. Forgacs [4] mapped the Villain model onto a special Baxter model, Peschel [5] mapped all three models onto the quantum XY-chain and Stephenson [6-8] and Gabay [9] studied asymptotic expansion of Toeplitz determinants after the fashion of Wu (see McCoy and Wu [10]).

More recently Dotsenko and Dotsenko [11] have shown how the correlation functions of 2D Ising systems can be expressed in the form of a propagator expansion and have demonstrated the use of the method in rederiving $\eta=\frac{1}{4}$ for the Ising ferromagnet.

In essence the Dotsenko and Dotsenko method is no more than a reformulation of the Toeplitz determinant expansion. It does, however, provide a particularly transparent way of comparing and contrasting the $\eta=\frac{1}{4}$ and $\eta=\frac{1}{2}$ systems. Applied to disordered systems, the Dotsenko and Dotsenko method has been somewhat controversial [12], but it does appear to be useful for regular systems.

It is well known that the spin-spin correlation function (between spins at sites 0 and $R$ ) can be written as
$$\overline{S_{0} S_{R}}=\operatorname{det} M.\qquad(1)$$

For diagonal correlations at $T_{\mathrm{c}}$ on the unfrustrated square lattice, the elements of $M$ [10] are $M_{i j}=\pi^{-1}\left(i-j+\frac{1}{2}\right)^{-1}$. If we write
$$M=I+g, \quad(2)$$
where $I$ is the unit matrix, then a formal expansion of the determinant is possible:
$$\ln \overline{S_{0} S_{R}}=-\sum_{n=1}^{\infty} \frac{(-1)^{n}}{n} \Pi_{n},\qquad(3)$$
where
$$\Pi_{n}=\sum_{m_{1}=1}^{R} \sum_{m_{2}=1}^{R} \cdots \sum_{m_{n}=1}^{R} g_{m_{1} m_{2}} g_{m_{2} m_{3}} \cdots g_{m_{n} m_{1}}.\qquad(4)$$

Dotsenko and Dotsenko [11] have applied this formalism to the Ising ferromagnet at $T_{\mathrm{c}}$. They argue that the dominant $R$ dependence in Eq. (3) comes from the asymptotic $(|i-j| \rightarrow \infty)$ behaviour of the Green's functions,
$$g_{i j} \sim \pi^{-1}(i-j)^{-1} \text {. }\qquad(5)$$

The leading contributions to the $\Pi_{n}$ are of order $R$ but these can easily be shown to sum to zero. The important $\Pi_{n}$ are those with even $n$, and they have contributions which vary with $R$ as $\ln R$. Dotsenko and Dotsenko evaluated these terms and showed that the right hand side of Eq. (3) yielded $-\frac{1}{4} \ln R$. Thus they obtained the well known result $\overline{S_{0} S_{R}} \sim R^{-1 / 4}$, and a correlation function exponent of $\eta=\frac{1}{4}$. For convenience in what follows, the $\Pi_{n}$ defined by Eqs. (3) and (4) (that is the value for the square ferromagnetic lattice) will be denoted by $\bar{\Pi}_{n}$.

The key quantity in determining the correlations is the Green's functions $g_{i j}$. For the fully frustrated systems, the asymptotic form is similar to Eq. (5), but with an additional factor $Q$ :
$$g_{i j} \sim \pi^{-1} Q_{i j}(i-j)^{-1}.\qquad(6)$$

* Corresponding author. Fax: +44-734-750203; email: j.r.goncalves@reading.ac.uk.

In the case of the Villain model [2,4] (horizontal or vertical correlations), $Q_{ij}=2$ if $i-j=2m+1$, $Q_{ij}=0$ if $i-j=2m$. For the triangular antiferromagnet [1], $Q_{ij}=\pm\sqrt{3}$ if $i-j=3m\pm1$, $Q_{ij}=0$ if $i-j=3m$. In these definitions, $m$ is any integer.

This can be expressed more conveniently if we give explicit recognition that the Villain model is a two sublattice system and the triangular antiferromagnet is a three sublattice one. Let us denote the number of sublattices by $d$. Using Greek letters to label sublattices, Eq. (6) becomes
$$
g_{i j}^{\alpha \beta} \sim \pi^{-1} \bar{Q}^{\alpha \beta}(i-j)^{-1},
\tag{7}
$$
where $\bar{Q}$ is a matrix of order $d$. Specifically, for the Villain model,
$$
\bar{Q}=\left(\begin{array}{ll}
0 & 2 \\
2 & 0
\end{array}\right),
\tag{8}
$$
while for the triangular antiferromagnet,
$$
\bar{Q}=\left(\begin{array}{ccc}
0 & \sqrt{3} & -\sqrt{3} \\
-\sqrt{3} & 0 & \sqrt{3} \\
\sqrt{3} & -\sqrt{3} & 0
\end{array}\right).
\tag{9}
$$

It is then relatively trivial to relate the general $\Pi_{n}$ to $\bar{\Pi}_{n}$ (the $n$th term in the expansion for the square ferromagnet) as defined earlier:
$$
\Pi_{n}=d^{-n} \operatorname{Tr} \bar{Q}^{n} \bar{\Pi}_{n}.
\tag{10}
$$

The $d^{-n}$ arises because the summations over $m_{1}$, $m_{2},\dots,m_{\text{n}}$ in Eq. (4) are now over unit cells rather than sites. The summation over sites in the unit cells is effected by the trace over powers of $\bar{Q}$. The eigenvalues of $\bar{Q}$ are $\pm2$ (Eq. (8)) and $\pm3,0$ (Eq. (9)) and so, for even $n$, $\operatorname{Tr} \bar{Q}^{n}$ is easily shown to be $2d^{n}$ for both models. Thus Eq. (10) simplifies to
$$
\Pi_{n}=2 \bar{\Pi}_{n}.
\tag{11}
$$
Term by term, $\Pi_{n}$ has double the value that occurs in the ferromagnetic case leading immediately to the well known result $\eta=\frac{1}{2}$. Thus it is the factor $d^{-n} \operatorname{Tr} \bar{Q}^{n}$ that is the key for determining $\eta$.

The correlation function is one of the hardest thermodynamic quantities to calculate and there is a clear advantage in having a method that is applicable to a range of systems rather than using one that is model specific. We will explore these matters in more detail elsewhere and also focus on the frustrated hexagonal lattice which does not show power law behaviour [13].

Acknowledgement: One of us (J.R.G.) acknowledges the support of the Brazilian Agency CNPq.

## References

[1] J. Stephenson, J. Math. Phys. 5 (1964) 1009.
[2] J. Villain, J. Phys C 10 (1977) 1717.
[3] G. André, R. Bidaux, J. P. Carton, R. Conte and L. de Seze, J. Physique 40 (1979) 479.
[4] G. Forgacs, Phys. Rev. B 22 (1980) 4473.
[5] I. Peschel, Z. Phys. B 45 (1982) 339.
[6] J. Stephenson, J. Math. Phys. 11 (1970) 413.
[7] J. Stephenson, J. Math. Phys. 11 (1970) 420.
[8] J. Stephenson, Phys. Rev. B 1 (1970) 4405.
[9] M. Gabay, J. Physique Lett. 41 (1980) 427.
[10] B. M. McCoy and T.T Wu, The two dimensional Ising model (Harvard University Press, 1973).
[11] V.S. Dotsenko and V.S. Dotsenko, Adv. Phys. 32 (1983) 129.
[12] R. Shankar, Phys. Rev. Lett. 58 (1987) 2466.
[13] W.F. Wolff and J. Zittartz, Z. Phys. B 49 (1982) 229.