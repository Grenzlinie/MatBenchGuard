# PHYSICAL REVIEW
VOLUME 111, NUMBER 3
AUGUST 1, 1958

# Ground-State Energy and Effective Mass of the Polaron
ELLIOTT H. LIEB, Physics Department, University of Illinois, Urbana, Illinois
AND
KAZUO YAMAZAKI,* Max Planck Institut fir Physik, Gottingen, Germany
(Received February 20, 1958)

The polaron Hamiltonian would be easily soluble were it not for the quartic term appearing therein. It is proposed to substitute for the quartic term a quadratic term having roughly the same properties, and in such a way that the ground-state energy of the new Hamiltonian is rigorously a lower bound for the true energy. With a very small amount of work one can obtain a lower bound as a continuous function of $\alpha$ for all values of $\alpha$ . The result agrees fairly well with the results obtained by other methods. Using the equivalent Hamiltonian one can also obtain an analytic expression for the effective mass, although one cannot say it is a bound for the true effective mass. Futhermore, once one has obtained a lower bound for the energy as a continuous function of the parameters of the Hamiltonian, one can rigorously derive upper and lower bounds for the ground-state expectation values of various oper- ators. For example, it can be shown that for large $\alpha$ and large k, $< a_{k}^{*} a_{k}> k^{-6}$ and not $k^{-2} \exp (-k^{2})$ as in Pekar's solution. Because of its simplicity, it is possible that this method may have appli- cation to other ground-state problems.

## 1. INTRODUCTION AND ILLUSTRATION
T has become common in recent years for field theorists to turn their attention to the field-theory- like problems which are to be found in solid-state theory. But rather than employing standard field- theory techniques, as might have been expected, most of the papers have tended to present entirely new methods and points of view, and have ended with the hope that the methods developed for solid-state theory may have some application to field theory. It is from this point of view that we should like to present a new method for estimating the ground-state energy $E_{0}$ and the effective mass $m^{*}$ of the polaron.

It will be recalled that all the methods given so far result in an upper bound for $E_{0}$ . There is Lee, Low, and Pines' weak-coupling variational calculation, as well as Pekar's variational calculation for strong coupling. There is every reason to believe that these answers are correct. Feynman $^{1}$ has shown how to use the functional integral to connect these two approximations. However, Feynman's method is rather complicated, requiring the services of the Massachusetts Institute of Technology Whirlwind computer, $^{2}$ and moreover suffers from lack of directness. It is not clear how to relate his method to more pedestrian manipulations of Hamiltonians and wave functions, although some attempts were made to fill this gap. $^{3}$ It is in fact possible to find a trial function suitable for all coupling, $^{4}$ but here again it is not clear what the changes in the trial function with coupling constant mean. Finally, although a product function such as is used for large coupling gives the asymptotic dependence of $E_{0}$ on $\alpha$ correctly, it yields patently wrong answers in many cases if one tries to calculate the expectation values of various operators in theground state. As a trivial example, one obtains $< H^{2}>=\infty$  with a product function.
It is not our intention to critize the variational calculations but to present an entirely different method which exploits the properties of the Hamiltonian rather than its wave function and at the same time gives a

* On leave of absence from the Research Institute for Funda- mental Physics, Kyoto, Japan.
1 R. P. Feynman, Phys. Rev. 97, 660 (1955).
2 T. D. Schultz, Technical Report No. 9, Solid State and Molecular Theory Group, Massachusetts Institute of Technology(unpublished).
3 For example, K. Yamazaki, Progr. Theoret. Phys. (Japan)16, 508 (1956), and G. Hohler, Nuovo cimento 2, 691 (1955).
4 G. Hohler, Z. Physik 140, 192 (1955).

lower bound for $E_0$. Unfortunately, for large coupling our $E_0$ differs from Pekar's by a factor of 3, but we believe the method is of interest because of its trans- parency and mathematical simplicity. Furthermore, a lower bound for $E_0$ that is an analytic function of the parameters of the Hamiltonian will yield rigorous upper and lower bounds for ground-state expectation values by a method which will be discussed subsequently. The expectation value of a Schrödinger operator is of interest in field theory since a propagator, which is the ex- pectation value of a Heisenberg operator, may be found from the expectation value of the corresponding Schrödinger operator; the time dependence may be derived by analytic continuation from the spatial dependence. $^{5}$

The method to be employed is suitable for a non- linear Hamiltonian, the nonlinear part of which is positive definite, say quartic. To fix ideas consider the anharmonic oscillator $^{6}$:
$$H=p^{2}+x^{2}+\lambda x^{4}, \quad \lambda \geq 0. \quad(1)$$

We first observe that if a Hamiltonian $H=H_{1}+H_{2}$, then
$$E_{0} \geq E_{0}^{1}+E_{0}^{2}, \quad(2)$$
where $E_{0}, E_{0}^{1}$, and $E_{0}^{2}$ are the ground-state energies of $H, H_{1}$, and $H_{2}$, respectively. We introduce a constant, c, such that
$$\lambda x^{4} \equiv \lambda\left(x^{2}-c\right)^{2}+2 \lambda c x^{2}-\lambda c^{2} \equiv H_{2}+2 \lambda c x^{2}-\lambda c^{2}, \quad(3)$$
and
$$H_{1} \equiv p^{2}+x^{2}+2 \lambda c x^{2}-\lambda c^{2}. \quad(4)$$

Since $E_{0}^{2}=0$ we have
$$E_{0} \geq E_{0}^{1}=-\lambda c^{2}+(1+2 c \lambda)^{\frac{1}{2}}.$$

Maximizing with respect to c, we find that
$$E_{0} \geq E_{0}^{1}=3 \lambda c^{2}+2 c, \quad(5)$$
where
$$8 \lambda c^{3}+4 c^{2}-1=0. \quad(6)$$

If a Gaussian function is used to obtain an upper bound, equations very similar to (5) and (6) result; in the worst possible case, large $\lambda$ , the two results have the same asymptotic form and agree to within $30 \%$ . The point we wish to emphasize is that we have ob- tained a lower bound with the correct dependence upon $\lambda$ and $\omega$ which can serve to check the variational calculation.

## 2. GROUND-STATE ENERGY
We take the polaron Hamiltonian in the form $^{7}$ 
$$H=\left(\mathbf{P}-\sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}\right)^{2}+\sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}+\sum_{\mathbf{k}} J_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}+\text { H.C., (7) }$$
where $P=$ total momentum ( $c$ number) and
$$J_{\mathbf{k}}=(4 \pi \alpha / V)^{\frac{1}{2}}|\mathbf{k}|^{-1}.$$

As regards $E_{0}$ , what follows could equally well be done with the Hamiltonian in the more usual form
$$H=\mathbf{p}^{2}+\sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}+\sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} J_{\mathbf{k}} e^{i \mathbf{k} \cdot \mathbf{x}}+\text { H.c., } \quad(7 \mathrm{a})$$
p being the electron momentum, but for estimating m* it is easier to have the total momentum expressed as a c number.
For $P=0$ we proceed as follows: define the vector operator
$$\mathbf{Z}=\sum_{\mathbf{k}} \mathbf{Z}(\mathbf{k}) a_{\mathbf{k}},\qquad(8)$$
 $Z(k)$ being a $c$ number, and
$$\begin{aligned}
H_{2} \equiv\left[\sum_{\mathbf{k}} \mathbf{k} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}+\frac{1}{2}\left(\mathbf{Z}-\mathbf{Z}^{*}\right)\right] \\
\cdot\left[\sum_{\mathbf{k}} \mathbf{k} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}-\frac{1}{2}\left(\mathbf{Z}-\mathbf{Z}^{*}\right)\right] \geq 0. \quad(9)
\end{aligned}$$

Then if $H \equiv H_{2}+H_{1}$ as before, we obtain
$$H_{1}=\sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}+\sum_{\mathbf{k}} J_{\mathbf{k}}{ }^{\prime} a_{\mathbf{k}}+\text { H.c. }+\frac{1}{4}\left(\mathbf{Z}-\mathbf{Z}^{*}\right)^{2},(10)$$
 where
$$J_{\mathbf{k}}{ }^{\prime}=J_{\mathbf{k}}-\frac{1}{2} \mathbf{k} \cdot \mathbf{Z}(\mathbf{k}).\qquad(11)$$

To find $E_{0}^{1}$ , we displace $a_{k}: a_{k} \to a_{k}-J_{k}^{\prime}$ . Hence
$$\begin{aligned}
H_{1}=\sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}+\frac{1}{4}\left(\mathbf{Z}-\mathbf{Z}^{*}\right)^{2}-\sum_{\mathbf{k}}\left|J_{\mathbf{k}}{ }^{\prime}\right|^{2} \\
\equiv H_{3}-\sum_{\mathbf{k}}\left|J_{k}{ }^{\prime}\right|^{2}. \quad(12)
\end{aligned}$$

Let us assume that $[Z_{i}, Z_{j}^{*}]=0$ for $i \neq j(i, j=1,2,3)$  and denote
$$t_{i}=\left[Z_{i}, Z_{i}{ }^{*}\right]=\sum_{\mathbf{k}}\left|Z_{i}(\mathbf{k})\right|^{2}.\qquad(13)$$

We note that $(Z-Z^{*})^{2}$ is negative definite and if $Z(k)$  becomes too large the ground state of $H_{3}$ will not exist. It is easy to show that the condition for the existence of $E_{0}^{3}$ is
$$t_{i}<1 \quad \text { (all } i) \text {. } \quad(14)$$

In fact, if we define $r_{i}$ by
$$r_{i}^{2}-\left[\left(4 / t_{i}\right)-2\right] r_{i}+1=0,\qquad(15)$$
 with the further condition
$$0 \leq r_{i} \leq 1, \quad \text { or } \quad 0 \leq t_{i} \leq 1, \quad(16)$$
 then it is a simple matter to diagonalize $H_{3}$ , with the result
$$E_{0}^{3}=-\sum_{i=1}^{3} r_{i}\left(1+r_{i}\right)^{-1}.\qquad(17)$$

Hence, by Eq. (12), $E_{0}^{1}$ is the sum of an integral of $Z(k)$ and a function, $E_{0}^{3}$ , of another integral, (13), of Z(k). Since
$$E_{0} \geq E_{0}^{1}=E_{0}^{3}-\sum_{\mathbf{k}}\left|J_{\mathbf{k}}{ }^{\prime}\right|^{2},\qquad(18)$$
 we wish to find the functional form of $Z(k)$ which maximizes $E_{0}^{1}$ . This is simply done by the condition
$$\frac{\delta}{\delta \mathbf{Z}(\mathbf{k})}\left\{-\sum_{\mathbf{k}}\left|J_{\mathbf{k}}{ }^{\prime}\right|^{2}+\sum_{i=1}^{3} \lambda_{i} t_{i}\left(\mathbf{Z}_{i}(\mathbf{k})\right)\right\}=0, \quad(19)$$
 where the $\lambda_{i}$ are Lagrange multipliers. It is then found

$^{5}$ A. S. Wightman, Phys. Rev. 101, 860 (1956).
 $^{6} \hbar=2 m=\omega=1$ .
 $^{7} \sum_{k} \to V(2 \pi)^{-3} \int d^{3} k$ .

that $Z_{i}(\mathbf{k})$ has the form
$$Z_{i}(\mathbf{k})=k_{i} c\left(\mathbf{k}^{2}\right).\qquad(20)$$

The scalar function, $c$, is found to be of the form
$$c\left(\mathbf{k}^{2}\right)=2 J_{\mathbf{k}}\left(\mathbf{k}^{2}+p^{2}\right)^{-1},\qquad(21)$$
$p$ being a constant.

Performing a few simple integrals, we obtain
$$t_{1}=t_{2}=t_{3}=\frac{2}{3}(\alpha / p) \equiv t,\qquad(22)$$
and
$$\sum_{\mathbf{k}}\left|J_{\mathbf{k}}{ }^{\prime}\right|^{2}=\frac{1}{2} p \alpha.\qquad(23)$$

The $t_{i}$ are all equal as they must be from the symmetry of the problem, but for $\mathbf{P} \neq 0$ this will not be the case. Denoting all the $r_{i}$, which are equal for $\mathbf{P}=0$, by $r$, we note that $r, p$, and $t$ are all functions of each other and anyone of them may be chosen as the independent variable. Choosing $p$, and recalling the condition, (16), which implies that
$$\frac {2}{3}\alpha \leq p\leq \infty,$$
it is found that
$$E_{0}^{1}=-\frac{3}{2}\left[1-\left(1-\frac{2 \alpha}{3 p}\right)^{\frac{1}{2}}\right]-\frac{1}{2} p \alpha.\qquad(24)$$

It is left to determine $p$. Maximizing (24) gives
$$p^{4}[1-(2 \alpha / 3 p)]=1.\qquad(25)$$

It was understood in (22) and (23) that $p$ is positive;with this convention we see that maximizing $E_{0}^{1}$ automatically satisfies (16). Using (25), we may express $E_{0}^{1}$ as a function of $p$ only:
$$E_{0} \geq E_{0}^{1}=-3\left(p^{2}-1\right)\left(p^{2}+3\right) / 4 p^{2}.\qquad(26)$$

Thus, (25) and (26) taken together constitute a lower-bound solution for $E_{0}$, in which $\alpha$ and $E_{0}$ are expressed by a parametric equation. If the solution is investigated numerically, it is found that it agrees with Feynman's solution up to approximately $\alpha=1$ and then departs from it radically. In the worst case, large $\alpha$, the asymptotic solution of (25) and (26) is
$$E_{0}^{1}=-\frac{1}{3} \alpha^{2},\qquad(27)$$
which differs from Feynman's or Pekar's solution by nearly a factor of 3.

To recapitulate, we have seen that the positive definite character of the momentum may be used to reduce the effective coupling by the term $\frac{1}{2} \mathbf{k} \cdot \mathbf{Z}(\mathbf{k})$[Eq. (11)] at the expense of introducing the negative definite term $\frac{1}{4}(Z-Z^{*})^{2}$ which has the character of the square of a momentum operator. Furthermore, the calculation involves only algebraic manipulations and the evaluation of a few simple integrals. But the point we wish to emphasize is that had we taken the Hamiltonian in the form (7a) we should change Eq. (8) to
$$\mathbf{Z}=\sum_{\mathbf{k}} \mathbf{Z}(\mathbf{k}) a_{\mathbf{k}} e^{i \mathbf{k} \cdot \mathbf{x}}\qquad(8a)$$
to obtain the same result; and the modified $H_{1}$ would then still commute with the total momentum operator, $P=p+\sum_{k} k a_{k}^{*} a_{k}$ . This being the case, when we attempt to evaluate (7) with $P \neq 0$ to obtain $m^{*}$ , the resulting $H_{1}$ which we propose to evaluate instead of the true $H$ may, owing to its having the correct invariant variance properties, yield a sensible result for $m^{*}$.

## 3. EFFECTIVE MASS
When we come to consider (7) for $P \neq 0$ , the lack of symmetry in $k$ space permits us to choose a slightly different $H_{2}$ and of course a different $Z(k)$ . We may change (9) to
$$\begin{aligned}
H_{2} \equiv\left[\sum_{\mathbf{k}} \mathbf{k} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}+\frac{1}{2}\left(\mathbf{Z}-\mathbf{Z}^{*}\right)+\mathbf{R}\right] & \\
\cdot\left[\sum_{\mathbf{k}} \mathbf{k} a_{\mathbf{k}} a_{\mathbf{k}}-\frac{1}{2}\left(\mathbf{Z}-\mathbf{Z}^{*}\right)+\mathbf{R}\right] & \geq 0, \quad(9 \mathrm{a})
\end{aligned}$$
where $R$ is a $c$ number vector. Consequently, $H_{1}$ becomes
$$\begin{aligned}
H_{1}=\sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}(1+\mathbf{S} \cdot \mathbf{k})+\sum_{\mathbf{k}} J_{\mathbf{k}}{ }^{\prime} a_{\mathbf{k}} & \\
& + \text { H.c. }+\mathbf{P}^{2}-\mathbf{R}^{2}, \quad(10 \mathrm{a})
\end{aligned}$$
where $S=2(R-P). J_{k}^{\prime}$ is still defined as in (11). In addition to maximizing $E_{0}^{1}$ with respect to $Z(k)$ , we must now also maximize it with respect to $R$ .

Strictly speaking, however, the ground-state energy of $H_{1}$ is unbounded, because for sufficiently large $k$ the factor $(1+S \cdot k)$ will become negative. Were this not the case, we could hope to use (10a) to get some idea of the curve $E_{0}(P)$ for all $P$ . But we can in fact use(10a) to evaluate $E_{0}(P)$ for very small $P$ in the following way: clearly as $P \to 0$ we will wish to choose $R \to 0$ and hence $S \to 0$ . We may therefore imagine the summation in the $S \cdot k$ term of $H_{1}$ to be cut off at some $k^{\prime}$  such that $S \cdot k^{\prime}<1$ . Hence,
$$E_{0} \geq E_{0}^{2}+E_{0}^{1}+\left\langle 0\left|\sum_{\mathbf{k}=\mathbf{k}^{\prime}}^{\infty} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}} \mathbf{S} \cdot \mathbf{k}\right| 0\right\rangle,\qquad(28)$$
where $|0\rangle$ is the true ground-state wave function. Since $k^{\prime} \to \infty$ as $|P|^{-1}$ , it is quite apparent that the last term in (28) vanishes at least of order $P^{4}$ and can be neglected. It might be supposed that for any $P$ we could always choose $R$ such that the last term in (28) vanishes or becomes negligible. But this would be contrary to the philosophy of the method which is to let the Hamiltonian speak for itself as it were; that is to say, to determine all the parameters in $H_{1}$ by a minimum principle. We have no other guide to the effective mass but that $H_{1}$ is a linear Hamiltonian which has been shown to be very similar to the true Hamiltonian, $H$ .

If we admit the cutoff into $H_{1}$ , then its effect will bethat integrals of the form $\int_{0}^{\infty} d k(p^{2}+k^{2})^{-1}(1-k^{2} l^{2})^{-1}$  are to be considered as principal-value integrals. The calculation is straightforward but somewhat more complicated algebraically than in Sec. 2; the lack of symmetry in $k$ space introduces many more parameters with respect to which $E_{0}^{1}$ must be minimized. The direction of $R$ will obviously be that of $P$ so that if we

let $\mathbf{P}=(0,0,P)$ and $\mathbf{S}=(0,0,S)$, and furthermore displace $a_{\mathbf{k}}$ to $a_{\mathbf{k}} \to a_{\mathbf{k}}-J_{\mathbf{k}}{ }^{\prime}\left(1+S k_{3}\right)^{-1}$, we find that
$$
\begin{aligned}
E_{0}^{1}=-\sum_{i=1}^{3} r_{i}\left(1+S C_{i}\right)(1+ & r_{i})^{-1} \\
& -\sum_{\mathbf{k}}\left|J_{\mathbf{k}}{ }^{\prime}\right|^{2}\left(1+S k_{3}\right)^{-1}, \quad(29)
\end{aligned}
$$
where
$$
C_{i}=t_{i}^{-1} \sum_{\mathbf{k}} k_{3}\left|Z_{i}(\mathbf{k})\right|^{2}, \quad(30)
$$
$$
r_{i}^{2}=\left[\frac{4\left(1+S C_{i}\right)}{t_{i}}-2\right] r_{i}+1=0, \quad 0 \leq r_{i} \leq 1, \quad(31)
$$
and $t_{i}$ is still defined by (13). Equation (29) is correct only to second order in $S$ since we have used perturbation theory to obtain it. It turns out that the optimum $\mathbf{Z}(\mathbf{k})$ is of the form
$$
Z_{i}(\mathbf{k})=k_{i} c(\mathbf{k})+S \delta_{i 3} d(\mathbf{k}), \quad(32)
$$
where
$$
c(\mathbf{k})=2 J_{\mathbf{k}}\left(\mathbf{k}^{2}+p^{2}+\lambda S k_{3}+q S^{2} k_{3}^{2}+n S^{2}\right)^{-1} \quad(33)
$$
and
$$
d(\mathbf{k})=b S k_{3} c(\mathbf{k}). \quad(34)
$$
$p, q, \lambda, n$, and $b$ are parameters; the dependence upon $S$ has been explicitly included, which means that $p$ is still defined as in (25) for $\mathbf{P}=0$.

Maximizing with respect to all parameters, we find that
$$
E_{0}(\mathbf{P}) \geq E_{0}^{1}+\mathbf{P}^{2} / 2 m^{*}, \quad(35)
$$
where
$$
m^{*}=\left\{\frac{\left(p^{2}-1\right)\left(p^{4}+2 p^{2}-2\right)}{p^{2}+1}+1\right\} m. \quad(36)
$$

The dimensional dependence of $m^{*}$ on $m$ has been explicitly included in (35) and (36). $E_{0}^{1}$ is defined by (24) and $p$ by (25).

For small $\alpha$, we get
$$
m^{*} / m=\left(1+\frac{1}{6} \alpha\right), \quad(37)
$$
which is correct, but for large $\alpha$ we obtain
$$
m^{*} / m=(16 / 81) \alpha^{4}, \quad(38)
$$
a result which is about a factor of 9 greater than Pekar's. It is not understood why the error in the effective mass is the square of that for $E_{0}$.

Since a variational principle for the effective mass does not exist, the fact that we have obtained a result substantially the same as Pekar's by a completely independent method serves to increase our confidence in Pekar's result. For the bare polaron (i.e., with no periodic potential present) with strong coupling it is fairly certain that the effective mass is as large as Pekar has claimed it is.

We should also like to point out that inasmuch as the integrals appearing in the calculation are all integrals of rational functions, it is a very simple matter to introduce a Debye cutoff and still be able to carry through the calculation analytically.

## 4. GROUND-STATE EXPECTATION VALUES

If one wishes to find the expectation value of a Hermitian operator, $O$, in the ground state (denoted by $\langle O\rangle$ ), then in principle one could proceed as follows: define the Hamiltonian
$$
H(\mu)=H+\mu O ; \quad(39)
$$
then, if $E_{0}(\mu)$ is the ground-state energy of $H(\mu)$, one has
$$
\langle O\rangle=\lim _{\mu \rightarrow 0} \frac{d E_{0}}{d \mu}. \quad(40)
$$

Now, what is often done is to estimate $E(\mu)$ by a variational calculation; but since a variational calculation only yields information about a particular integral of the wave function, for a general operator, $O$, differentiating the variational result according to (40) is a procedure of doubtful validity. However, if $\mu$ is a parameter which appears naturally in $H$, the variational procedure may be justified insofar as a differentiation with respect to $\mu$ is included in the variational calculation. Otherwise another method must be found. In the following discussion we shall try to clarify the above statement and present a workable method for estimating $\langle O\rangle$ for the general case.

Consider (7) in the slightly generalized form
$$
\begin{aligned}
H=\beta\left(\mathbf{P}-\sum_{\mathbf{k}} \mathbf{k} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}}\right)^{2}+ & \gamma \sum_{\mathbf{k}} a_{\mathbf{k}}{ }^{*} a_{\mathbf{k}} \\
& +\delta\left(\sum_{\mathbf{k}} J_{\mathbf{k}} a_{\mathbf{k}}+\text { H.c. }\right), \quad(41)
\end{aligned}
$$
where $\beta, \gamma$, and $\delta$ are constants. For $\mathbf{P}=0$, a ratio of some physical interest is
$$
\begin{aligned}
\left\langle\left(\sum_{\mathbf{k}} \mathbf{k} a_{\mathbf{k}} * a_{\mathbf{k}}\right)^{2}\right\rangle:\left\langle\sum_{\mathbf{k}} a_{\mathbf{k}} * a_{\mathbf{k}}\right\rangle: & \left\langle\sum_{\mathbf{k}} J_{\mathbf{k}} a_{\mathbf{k}}+\text { H.c. }\right\rangle\left.\right|_{\beta, \gamma, \delta=1} \\
& =\lim _{\beta, \gamma, \delta \rightarrow 1} \frac{\partial E}{\partial \beta}: \frac{\partial E}{\partial \gamma}: \frac{\partial E}{\partial \delta}. \quad(42)
\end{aligned}
$$

For large coupling, the product trial function gives
$$
E_{0} \leq-\frac{1}{3} \pi^{-1} \alpha^{2}\left(\delta^{4} \gamma^{-2} \beta^{-1}\right), \quad(43)
$$
from which it may be supposed that the ratio (42) is $1: 2:(-4)$.

How correct is this result? Since $\beta, \gamma$, and $\delta$ are parameters which occur naturally in $H$, it is found that the $1: 2:(-4)$ ratio is obtained not only from differentiation of (43) but also from the expectation values of the trial function itself after $E$ has been minimized. In other words, the fact that (40) agrees with the expectation values obtained with the trial function is a direct consequence of the variational method. However, a far more convincing argument is the following: by the method of Sec. 2 we find that
$$
E \geq-\frac{1}{3} \alpha^{2}\left(\delta^{4} \gamma^{-2} \beta^{-1}\right). \quad(44)
$$

Since it appears both in the upper and lower bound, the factor $\left(\delta^{4} \gamma^{-2} \beta^{-1}\right)$ must be correct except possibly for an oscillating factor. If we assume that the ratio,

(42), is asymptotically independent of $\alpha$ then the oscillating factor cannot be present and we may be said to have proved the $1: 2:(-4)$ ratio.

If $\alpha$ is not large, the method of Sec. 2 gives
$$E_{0}(\mathbf{P}) \geq E_{0}+\mathbf{P}^{2} / 2 m^{*},\qquad(45)$$
where
$$E_{0}=-\frac{3}{4} \gamma \frac{\left(p^{2}-1\right)\left(p^{2}+3\right)}{p^{2}},\qquad(46)$$

$$\frac{m^{*}}{m}=\frac{1}{\beta}\left\{\frac{\left(p^{2}-1\right)\left(p^{4}+2 p^{2}-2\right)}{\left(p^{2}+1\right)}+1\right\},\qquad(47)$$
and
$$p^{4}\left(1-\frac{2 \alpha \delta^{2}}{3 p\left(\beta \gamma^{3}\right)^{\frac{1}{2}}}\right)=1.\qquad(48)$$

For small $\alpha$ these equations give the correct ratio $1: 1:(-4)$ in (42). The dependence of $m^{*}$ on $\beta, \gamma$, and $\delta$ is also correct in the strong- and weak-coupling limits insofar as it agrees with previous results. We may therefore conclude that insofar as the dependence of $E_{0}$ on $\beta, \gamma$, and $\delta$ is concerned, the variational calculations are asymptotically correct, and for intermediate coupling they are probably substantially correct.

However, when we come to consider quantities such as $\langle a_{k}^{*}+a_{k}\rangle$ or $\langle\sum_{k, k^{\prime}} k \cdot k^{\prime} a_{k}^{*} a_{k^{\prime}}^{*} a_{k} a_{k^{\prime}}\rangle$ , the results obtained from trial functions are very much in error. For the latter quantity, the product ansatz gives zero, whereas it is easy to see that it is of order $\alpha^{2}$ ; there is no way, within the framework of the product ansatz, to obtain a nonzero result. For the former quantity, the product ansatz with a Gaussian function gives
$$\left\langle a_{\mathrm{k}}^{*}+a_{\mathrm{k}}\right\rangle=-2 J_{\mathrm{k}} \exp \left(-\frac{9 \pi}{8 \alpha^{2}} \mathbf{k}^{2}\right),\qquad(49)$$
a result which, as we shall show, is definitely incorrect for large $k$ . It is true that in this latter case it is possible to choose a product function to give the correct result for $\langle a_{k}^{*}+a_{k}\rangle$ , but there is no way of knowing how to find it by using a variational treatment. The difficulty lies in the fact that the expectation values of the above two operators involve a detailed knowledge of the wave function which cannot be obtained from a variational calculation.

At this point a lower bound becomes useful. The equation
$$\mu^{-1}\left[E_{0}(\mu)-E_{0}\right] \leq\langle O\rangle \leq \mu^{-1}\left[E_{0}-E_{0}(-\mu)\right], \quad(50)$$
where $E_{0}$ is the ground-state energy of $H$ , can be derived from the simple equation
$$E_{0}(\mu) \leq\langle H\rangle+\mu\langle O\rangle=E_{0}+\mu\langle O\rangle,\qquad(51)$$
and may be considered to be a difference-equation generalization of (40). Equation (50) may be extended to
$$\mu^{-1}\left[E_{0}^{L}(\mu)-E_{0}^{U}\right] \leq\langle O\rangle \leq \mu^{-1}\left[E_{0}^{U}-E_{0}^{L}(-\mu)\right],(52)$$
where $U$ and $L$ refer to upper and lower bounds, respectively. It will be seen that to use (50) it is necessary to have a lower and not an upper bound as a function of $\mu$ . If one can find such a lower bound as an analytic function of $\mu$ , one can then maximize (50) with respect to $\mu$ . Equation (40) tells us that the best $\mu$ is $\mu \to 0$ , but since there will in general be a finite difference between the upper and lower bounds at $\mu=0$ one must choose a nonzero $\mu$ . In any case one can obtain definite limits on $\langle O\rangle$ .

As an illustration let us try to evaluate $\langle a_{k}^{*}+a_{k}\rangle$ for arbitrary $k$ in the strong-coupling limit. Equation(39) reads
$$\begin{aligned}
H(\mu)=\left(\sum_{\mathrm{k}} \mathbf{k} a_{\mathrm{k}}^{*} a_{\mathrm{k}}\right)^{2}+\sum_{\mathrm{k}} a_{\mathrm{k}}^{*} a_{\mathrm{k}}+\mu\left(a_{\mathrm{k}}^{*}+a_{\mathrm{k}}\right) \\
+\sum_{\mathrm{k}} J_{\mathrm{k}} a_{\mathrm{k}}+\text { H.c. }(53)
\end{aligned}$$

The method of Sec. 2 is directly applicable to (53). Proceeding as before, we find
$$E_{0}{ }^{L}(\mu)=-\frac{1}{2} p \alpha-\frac{2 \mu p^{4}}{\left(p^{2}+\mathbf{k}^{2}\right)} J_{\mathbf{k}^{2}}\qquad(54)$$
[the first term in (24) may be dropped for large $\alpha$ ], and
$$1-O\left(\alpha^{-1}\right)=t(\mu)=\frac{\alpha}{p} \frac{8}{3}+\frac{\mathbf{k}^{2} \mu}{\left(p^{2}+\mathbf{k}^{2}\right)} J_{\mathbf{k}}.\qquad(55)$$

Hence $p$ is not equal to $\frac{2}{3} \alpha$ as formerly but is now a function of $\mu$ and $k$ . Upon solving for $\mu$ in terms of $p$ , Eq. (52) reads
$$\begin{aligned}
\left\langle a_{\mathbf{k}}{ }^{*}+a_{\mathbf{k}}\right\rangle \leq \text { or } \geq & \frac{-2 p^{4} J_{\mathbf{k}}}{\left(p^{2}+\mathbf{k}^{2}\right)^{2}} \\
& +\frac{4\left(2 E_{0} p+\alpha p^{2}\right)}{(2 \alpha-3 p)\left(p^{2}+\mathbf{k}^{2}\right)^{2}} \mathbf{k}^{2} J_{\mathbf{k}}, \quad(56)
\end{aligned}$$
where the $\leq$ sign holds if $p \leq \frac{2}{3} \alpha$ and the $\geq$ sign holds for $p \geq \frac{2}{3} \alpha$ . To find the best $p$ we must differentiate (56), which leads to a ninth-order polynomial equation in $p$ which will have two roots greater and less than $\frac{2}{3} \alpha$ , respectively. For small $k$ , these two roots coincide and we find that
$$\left\langle a_{\mathrm{k}}^{*}+a_{\mathrm{k}}\right\rangle=-2 J_{\mathrm{k}}.\qquad(57)$$

For large $k$ , the equation reduces to second order and we find
$$\left\langle a_{\mathrm{k}}^{*}+a_{\mathrm{k}}\right\rangle \leq \text { or } \geq \frac{-2 J_{k}}{3 k^{2}}\left[\alpha \mp\left(\alpha^{2}+3 E_{0}\right)^{\frac{1}{2}}\right]^{2}. \quad(58)$$

Equation (57) is exact and is in fact true for all $\alpha$ as may be seen from the functional integral representation. For large $k$ , if we take $E_{0}^{U}=-\alpha^{2} / 3 \pi$ as given by the product trial function, we obtain
$$-0.034 \alpha^{2} J_{\mathrm{k}} / \mathbf{k}^{2} \geq\left\langle a_{\mathrm{k}}+a_{\mathrm{k}}\right\rangle \geq-3.0 \alpha^{2} J_{\mathrm{k}} / \mathbf{k}^{2}. \quad(59)$$

G R O U N D - S T A T E E N E R G Y

Thus, although the two coefficients in (59) differ by a factor of 100, we have established the asymptotic dependence of $\langle a_{\mathbf{k}}^{*}+a_{\mathbf{k}}\rangle$ on $\mathbf{k}$ (aside, of course, from an oscillating factor which undoubtedly is not present), and shown it to be quite different from (49). It is interesting to note that (59) agrees with the asymptotic dependence of $\langle a_{\mathbf{k}}^{*}+a_{\mathbf{k}}\rangle$ in $H_{1}$ of Sec. 2 and hence tends to increase our confidence in the result for $m^{*}$ found in Sec. 3.

The same procedure can be used to calculate $\langle a_{\mathbf{k}}^{*} a_{\mathbf{k}}\rangle$ although the algebra is a trifle more involved. It is found that the asymptotic dependence of $\langle a_{\mathbf{k}}^{*} a_{\mathbf{k}}\rangle$ is the square of (59) aside from a numerical factor of order unity, a result which is anticipated by the adiabatic hypothesis.

Thus, by numerical methods one can obtain upper and lower bounds for $\langle a_{\mathbf{k}}^{*} a_{\mathbf{k}}\rangle$ for all $\alpha$ and all $\mathbf{k}$, the two bounds being farthest apart for large $\alpha$ and large $\mathbf{k}$. In field theory a quantity such as $\langle a_{\mathbf{k}}^{*} a_{\mathbf{k}}\rangle$ is, aside from an additional time dependence which can be deduced from relativistic considerations, a propagator of im- mediate physical interest. Unfortunately, in field theory one must face the two problems of renormalization and the fact that a ground state does not strictly speaking exist, both of which would make a lower bound a somewhat unrigorous mathematical concept. Still, the nonlinear elements in the usual field-theory Hamil- tonian are positive definite so that the method of Sec.2 may have some validity.

## ACKNOWLEDGMENTS
This work was done while both authors were at the Research Institute for Fundamental Physics (Yukawa Hall), Kyoto, Japan. E. Lieb is indebted to the Japan Fulbright Commission for a grant which made his stay in Japan possible, and to Professor Yukawa and the other members of the Institute for their kind hospitality.
