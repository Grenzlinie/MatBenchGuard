# THEORY OF THE SELF-CONSISTENT HARMONIC APPROXIMATION WITH APPLICATION TO SOLID NEON
Thomas R. Koehler

IBM Research Laboratory, San Jose, California
(Received 31 May 1966)

Mathematical techniques have been described$^{1,2}$ by which one can perform an exact calculation in coordinate space of the matrix elements of a crystal Hamiltonian
$$
H=-\frac{1}{2} \lambda^{2} \sum_{i} \nabla_{i}^{2}+\frac{1}{2} \sum_{i \neq j} V\left(r_{i j}\right), \tag{1}
$$
between the eigenfunctions $|a;n\rangle$ of a harmonic Hamiltonian$^{3}$
$$
H^{(1)}(a)=\frac{1}{2} \lambda^{2} \tilde{p} p+\frac{1}{2} a^{2} \tilde{q} \Phi q \tag{2}
$$
appropriate to a crystal of the same symme- try. Here $a$ is a parameter which is essential- ly a scale factor for the generation of a set of harmonic Hamiltonians whose eigenfunctions and eigenvalues are simply related, $\lambda^{2}=\hbar^{2}/(m\sigma^{2}\epsilon)$, and the Mie-Lennard-Jones potential $V(r)=4\epsilon[(\sigma/r)^{12}-(\sigma/r)^{6}]$ has been used, with $\sigma$ and $\epsilon$ as units of distance and energy, respec- tively. We will also use
$$
V=\frac{1}{2} \sum_{i \neq j} V\left(r_{i j}\right).
$$

A notation is used in which $q$ is a supervector whose components are the vectors $q_{i}$, and the Cartesian components of $q_{i}$ are denoted by $q_{i}{}^{\alpha}$.

A similar notation is used for other vectors and matrices. The coordinate of the $i$th par- ticle is given by $r_{i}$ and its equilibrium position by $R_{i}$, and $q_{i}=r_{i}-R_{i}$.
It was found that $W(a) \equiv\langle a;0|H|a;0\rangle$ and $E_{k}{}^{\alpha}(a)$ $\equiv\langle a;k|H|a;k^{\alpha}\rangle-W(a)$ were readily obtained, where $|a;0\rangle$ is the ground-state eigenfunction of $H^{(1)}(a)$, and $|a;k^{\alpha}\rangle$ is the state with one pho- non of wave vector $k$, belonging to the $\alpha$th branch, excited. Thus, a variational calculation can be performed to determine the optimum value $a_{0}$ of $a$ and the ground-state energy $W_{0}(a_{0})$ of the crystal. The $E_{k}{}^{\alpha}\equiv E_{k}{}^{\alpha}(a_{0})$ then give the phonon spectrum to first order.

In this Letter it will be shown that a logical extension of the calculation described above leads to the construction of a "self-consistent harmonic Hamiltonian" for a crystal, which we shall define as that Hamiltonian
$$
H^{(c)}=\frac{1}{2} \lambda^{2} \tilde{p} p+\frac{1}{2} \tilde{q} \Phi^{(c)} q \tag{3}
$$
in which
$$
\Phi_{i j}^{(c) \alpha \beta}=\left\langle c, 0\left|\frac{\partial^{2} V}{\partial r_{i}{ }^{\alpha} \partial r_{j}{ }^{\beta}}\right| c, 0\right\rangle. \tag{4}
$$

This intuitively appealing equation is similar to a result obtained by Nosanow and Werthamer⁴ except, here, the additional feature of self-consistency is present.

By differentiating Eq. (I-64) with respect to
$$
G_{i j}^{(c) \alpha \beta}=\left[\left(\Phi^{(c)}\right)^{1 / 2}\right]_{i j}^{\alpha \beta}
$$
one can show, after some matrix manipulation, that the relationship given by Eq. (4) is sufficient to cause the right-hand side of
$$
\partial W_{0} / \partial G_{i j}^{(c) \alpha \beta}=\frac{1}{4} \delta_{i j}^{\alpha \beta}-\left\langle c, 0\left|q_{i}{ }^{\alpha} q_{j}{ }^{\beta} V\right| c, 0\right\rangle+\frac{1}{2}\left(\tilde{T} \omega^{-1} T\right)_{i j}^{\alpha \beta}\langle c, 0|V| c, 0\rangle
\tag{5}
$$
to vanish, where $T$ is the matrix which diagonalizes⁵ $\Phi^{(c)}$. Thus,
$$
|c, 0\rangle \propto \exp \left\{-\frac{1}{2} \tilde{q} G^{(c)} q\right\}
\tag{6}
$$
is that particular correlated Gaussian wave function which minimizes the expectation value of the true crystal Hamiltonian, and, in this sense, is the optimum harmonic wave function with which one can approximate the ground-state eigenfunction of $H$. In addition, if $b$ is the nearest-neighbor distance, one can show that $\partial W_{0} / \partial b=0$ is equivalent to
$$
\langle c, 0|(\partial V / \partial b)| c, 0\rangle=0.
\tag{7}
$$

The approximation of a crystal Hamiltonian by a model harmonic Hamiltonian was first suggested by Born,⁶ and subsequent work along these lines was performed by Hooton.⁷ Equation (7) and a result similar to Eq. (4) but expressed in terms of normal-mode coordinates were obtained by these authors.

Here, because the calculations are performed in coordinate space, simpler expressions are obtained. In addition, straightforward modification of Eq. (I-53) shows that satisfaction of Eq. (4) is also sufficient to produce the result
$$
\omega_{k}^{(c) \alpha}=E_{k}^{(c) \alpha}.
\tag{8}
$$

The construction of $H^{(c)}$ is a simple iterative procedure in which a matrix $\Phi$ is used in Eq. (2) to construct $|a, 0\rangle$. Then $a_{0}$ is found and a new matrix
$$
\Phi_{i j}^{(1) \alpha \beta}=\frac{1}{2}\left(\Phi_{i j}^{\alpha \beta}+\left\langle a_{0}, 0\left|\frac{\partial^{2} V}{\partial r_{i}{ }^{\alpha} \partial r_{j}{ }^{\beta}}\right| a_{0}, 0\right\rangle\right)
$$
is constructed and used to repeat the process.

A calculation following the procedure outlined above has been made for solid neon at $0^\circ$K.
Certain of the results are shown in Table I.
The zeroth iteration results are those from the conventional harmonic approximation and are given for comparison. The self-consistent calculation begins with the first iteration, which is an energy calculation to determine the optimum uncorrelated Gaussian wave function which is then used to compute $W_{0}^{(1)}$ and $\Phi^{(1)}$. Next, $\Phi^{(1)}$ is used to construct the wave function from which $W_{0}^{(2)}$ and $\Phi^{(2)}$ are computed, etc. [In the above a superscript $(n)$ was used to indicate values appropriate to the $n$th iteration.]

This calculation was performed to illustrate certain aspects of the theory and to show that the wave function selected here gives a lower value for $W_{0}$ in a variational calculation than was obtained variationally by Bernardes⁸ (-420 cal/mole), Nosanow and Shaw⁹ (-431 cal/mole), and Mullin¹⁰ (-431 cal/mole). The values of the Lennard-Jones parameter were, therefore, taken to be $\epsilon=50.0 \times 10^{-16}$ erg and $\sigma=2.74$ Å, in agreement with Refs. 6-8. The energy was

<table>
<caption>Table I. Results for the ground-state energy $W_{0}$, nearest-neighbor ($\Phi_{01}^{\alpha \alpha}$) and second-nearest-neighbor ($\Phi_{02}^{\alpha \alpha}$) force constants, and longitudinal ($c_{l}$) and transverse ($c_{t}$) velocities of sound in the [111] direction for solid Ne at $0^\circ$K. Other components of the force constants for these two neighbors are easily obtained from the values given here.</caption>
<thead>
<tr>
<th>Iteration</th>
<th>$-W_{0}$ (cal/mole)</th>
<th>$\Phi_{01}^{xx}$</th>
<th>$\Phi_{01}^{zz}$</th>
<th>$\Phi_{02}^{xx}$</th>
<th>$\Phi_{02}^{zz}$</th>
<th>$c_{l}$ ($10^{5}$ cm/sec)</th>
<th>$c_{t}$ ($10^{5}$ cm/sec)</th>
</tr>
<tr>
<th colspan="8">(units based on $\epsilon$ and $\sigma$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>462</td>
<td>21.1</td>
<td>0.712</td>
<td>$-2.92$</td>
<td>0.469</td>
<td>0.969</td>
<td>0.516</td>
</tr>
<tr>
<td>1</td>
<td>431</td>
<td>40.6</td>
<td>$-1.65$</td>
<td>$-2.96$</td>
<td>0.481</td>
<td>1.48</td>
<td>0.673</td>
</tr>
<tr>
<td>2</td>
<td>438</td>
<td>39.8</td>
<td>$-1.51$</td>
<td>$-2.97$</td>
<td>0.483</td>
<td>1.41</td>
<td>0.679</td>
</tr>
<tr>
<td>3</td>
<td>438</td>
<td>39.7</td>
<td>$-1.49$</td>
<td>$-2.97$</td>
<td>0.483</td>
<td>1.41</td>
<td>0.678</td>
</tr>
</tbody>
</table>

Table II. Contributions to $\langle 0|H|0\rangle$ in cal/mole from
the kinetic energy $K$ and from terms proportional to
the $n$th derivative of the potential $V^{n}$ computed with the
ground-state eigenfunctions of the self-consistent
$|c, 0\rangle$ and the traditional $|h, 0\rangle$ harmonic Hamiltonians.

| Term | Computed with $|c, 0\rangle$ | Computed with $|h, 0\rangle$ |
|------|-------------------------------|-------------------------------|
| $K$  | 84.7                          | 62.3                          |
| $V^{0}$ | $-586.0$                     | $-586.0$                     |
| $V^{2}$ | 45.8                         | 62.3                          |
| $V^{4}$ | 14.5                         | 26.8                          |
| $V^{6}$ | 2.6                          | 6.5                           |
| $V^{8}$ | 0.5                          | 1.4                           |

not minimized with respect to $b$, but rather
$b=2.74$ Å was chosen to agree with the optimum
value reported in Ref. 8. Thus, this theory is
compared with other theories. A detailed com-
parison with experiment will be reported in
the future. The value of $-W_{0}$ is in reasonable
agreement with the experimental value$^{11}$ 450
$\pm 10$ cal/mole.

It should be noted that the expectation value
of the second derivative of the potential is quite
different from the second derivative for near-
est neighbors but that second-nearest-neighbor
and further force constants are not altered much.

Although space limitations do not permit an
adequate discussion of this point, an interest-
ing aspect of the numerical procedure used here
is that the contributions to $W_{0}$ from terms pro-
portional to various derivatives of the potential
$V$ are obtained almost trivially. Contributions
to $W_{0}^{(3)}$ and $W_{0}^{(0)}$ from these terms as well
as the kinetic energy $K$ are shown in Table II.

Note that in $W_{0}^{(3)}$, $K=V^{2}+2V^{4}+3V^{6}+\cdots$. The
contributions for $W_{0}^{(0)}$ show clearly that solid
neon cannot be treated adequately by the tradi-
tional harmonic approximation. Note that $W_{0}^{(0)}$
as given in Table I equals $K+V^{0}+V^{2}$ here, and
that truncation of the Hamiltonian at $V^{2}$ results
in an error of approximately 35 cal/mole.

One can also show from Eq. (I-54b) that $\langle c;$
$k^{\alpha},-k^{\beta}|H|c,0\rangle=0$. Since these matrix elements
would normally give rise to the largest correc-
tion in perturbation theory, the eigenfunction
of $H^{(c)}$ appears to be a logical set with which
to begin perturbation calculations.

The author wishes to thank W. R. Heller for
useful discussions about certain features of
this work.

$^{1}$T. R. Koehler, Phys. Rev. 144, 789 (1966); this pa-
per will be referred to as I.
$^{2}$T. R. Koehler, Bull. Am. Phys. Soc. 10, 1192 (1965).
$^{3}$A somewhat different notation is employed here than
was used in Ref. 1.
$^{4}$L. H. Nosanow and N. R. Werthamer, Phys. Rev. Let-
ters 15, 618 (1965).
$^{5}$For details concerning this diagonalization, see,
e.g., A. A. Maradudin, E. W. Montroll, and G. H.
Weiss, in Solid State Physics, edited by F. Seitz and
D. Turnbull (Academic Press, Inc., New York, 1963),
Suppl. 3, or any of several references given in I.
$^{6}$M. Born, Fest. d. Akad. Wiss. Göttingen (1951).
$^{7}$D. J. Hooton, Phil. Mag. 46, 422, 433 (1955); Z.
Physik 142, 42 (1955).
$^{8}$N. Bernardes, Phys. Rev. 112, 1534 (1958).
$^{9}$L. H. Nosanow and G. L. Shaw, Phys. Rev. 128, 546
(1962).
$^{10}$W. J. Mullin, Phys. Rev. 134, A1249 (1964).
$^{11}$E. R. Dobbs and G. O. Jones, Reports on Progress
in Physics (The Physical Society, London, 1957),
Vol. 20, p. 516.

