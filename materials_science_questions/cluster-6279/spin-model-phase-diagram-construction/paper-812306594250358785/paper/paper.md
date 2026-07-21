Journal of Statistical Physics, Vol. 50, Nos. 1/2, 1988

# Phase Diagram of a One-Dimensional Model with Nonconvex Interactions, Using the Method of Effective Potentials

Weiren Chou¹

Received September 15, 1987

The ground states of a one-dimensional system of the Frenkel-Kontorova type, but involving piecewise parabolic potentials, including a nonconvex interatomic interaction, have been studied numerically using the method of effective potentials. Part of the phase diagram is identical to one studied earlier for a convex interaction, and part of it exhibits some new phases, first-order phase transitions, multicritical points, and an accumulation point of multicritical points, all associated with the nonconvex interaction.

KEY WORDS: Convex (nonconvex) region; multicritical point; accumulation point.

In recent years there have been a number of studies⁽¹⁾ of the ground states of one-dimensional systems of atoms with a potential energy

$$
H=\sum_{n}\left[V\left(x_{n}\right)+W\left(x_{n+1}-x_{n}\right)\right] \tag{1}
$$

where $-\infty < x_{n} < \infty$ is the position of the $n$th atom. When the interactions $V$ and $W$ compete with each other it is possible to obtain a fairly complex set of commensurate and incommensurate phases and transitions between them.

This paper presents the results of numerical calculations of the phase diagram for a particular case in which both $V$ and $W$ are piecewise parabolic functions and $W$ is nonconvex. The calculations used the method

---
¹ Department of Physics, Carnegie-Mellon University, Pittsburgh, Pennsylvania 15213.
Present address: Advanced Photon Source Division, Argonne National Laboratory, Argonne, Illinois 60439.

0022-4715/88/0100-0207$06.00/0 © 1988 Plenum Publishing Corporation
822/50/1-2-14

of effective potentials, $^{(2,3)}$ which has recently demonstrated its utility as a numerical technique in some other studies involving a nonconvex $W.^{(4,5)}$ Previous studies in the nonconvex case $^{(6,7)}$ have had to rely upon special assumptions or special properties of $W$.

Assume that
$$
V(x)=K f(x), \quad W\left(x^{\prime}-x\right)=f\left(x^{\prime}-x-\gamma\right) \tag{2}
$$
and $K$ and $\gamma$ are real parameters, and
$$
f(1+x)=f(x) \tag{3}
$$
a periodic function defined by
$$
\begin{aligned}
f(x) & =\frac{1}{2} x^{2}, & & -\frac{1}{4} \leqslant x \leqslant \frac{1}{4} \\
& =\frac{1}{16}-\frac{1}{2}\left(x-\frac{1}{2}\right)^{2}, & & \frac{1}{4} \leqslant x \leqslant \frac{3}{4}
\end{aligned} \tag{4}
$$
on the interval $-1 / 4$ to $3 / 4$, and by periodicity outside this interval; see Fig. 1. Since both $V$ and $W$ are periodic functions, it is sufficient, when considering the ground state, to assume that
$$
0 \leqslant x_{n}<1 \tag{5}
$$
and as this interval is best thought of as a circle, one can replace $x_{n}$ with an angular variable
$$
\theta_{n}=2 \pi x_{n} \tag{6}
$$
which varies from 0 to $2 \pi$. The model described by (2) is then very similar to the chiral $X Y$ model in a field studied in Ref. 4, with the cosine approximated by a piecewise parabolic function.

![](./images/812306594250358785_1.jpg)

Fig. 1. The periodic piecewise parabolic function $f(x)$; see (4).

When $V$ is periodic and $W$ is convex, a ground state of (1) has a well-defined "winding number" $\omega$, the average of the separation $x_{n+1}-x_{n}$ of successive particles. For nonconvex $W$ there is not, in general, a unique winding number, but one can define an analogous quantity for a ground state of period $Q$, i.e.,

$$
x_{n+Q}=x_{n} \tag{7}
$$

for all $n$, as the ratio $P/Q$, where

$$
P=\sum_{j=0}^{Q-1}\left\{x_{n+j+1}-x_{n+j}\right\} \tag{8}
$$

and the curly brackets mean the fractional part: an appropriate integer has been added to the difference so that it lies in the interval $[0,1)$.

The ground states of (2) were studied using a numerical solution of the eigenvalue equation

$$
V\left(x^{\prime}\right)+\min _{x}\left[W\left(x^{\prime}-x\right)+R(x)\right]=\lambda+R\left(x^{\prime}\right) \tag{9}
$$

for the unknown eigenvalue $\lambda$ and periodic eigenvector

$$
R(1+x)=R(x)
$$

Because of the periodicity of $V$, $R$, and $W$, the variables $x$ and $x'$ can be confined to the compact domain (5). In this case the continuity of $V$ and $W$ guarantees the existence of a unique eigenvalue and at least one continuous eigenvector $R.^{(8)}$ For a numerical solution the continuous interval was replaced by a grid of 100 points, and (9) was solved by successive approximations; for details, see Ref. 3.

The phase diagram of the model with the interactions given in (2) is shown in Fig. 2. The fractions denote winding numbers $P/Q$ with the denominator equal to the period. Phases of types $A$ and $B$ have different symmetries: $B$ phases always have some atoms at the maximum of $V(x)$, and this is never the case for $A$ phases. The unlabeled regions in the lower part of the figure contain a multitude of other phases.

Although the function $W$ is not convex, in a particular ground state it may be the case that $W(z)$ is locally convex (positive second derivative) when $z$ is one of the separations $x_{n+1}-x_{n}$ of adjacent atoms. In this case, following the terminology of Refs. 4 and 5, the phase is said to be "convex," otherwise it is "nonconvex." In particular, when $K$ is small one expects to find "convex" phases because the separations occur near the minimum of $W$; this can also be proved to be the case when $K$ is suf-

![](./images/812306594250358785_2.jpg)

Fig. 2. Phase diagram corresponding to (2). The dashed lines are separation lines. The points marked $C_{j}$ and $d_{1}$ are multicritical points. The crossed lines are first-order transition lines. The numbers are values of the winding number $\omega$.

ficiently small. $^{(9)}$ In Fig. 2 the dashed "separation" lines divide the "convex" from the "nonconvex" regions. The "convex" region is to the right and below the separation line except for the case $\omega=0$, where it is to the left of the vertical line $\gamma=1 / 4$. In all cases we have studied, the $B$ phases lie in the convex regions.

By shifting the $x_{n}$ by appropriate integers, the ground state of a "convex" phase may be transformed into a ground state of a model with the same $V$, but where $W(z)$ is a simple parabola, $(z-\gamma)^{2} / 2$. For this reason the lower part of the phase diagram in Fig. 2 is identical to the corresponding part of Fig. 21 in Ref. 3.

Several features of the "nonconvex" part of the phase diagram deserve comment. There are a number of first-order transitions between phases with different $\omega$, a situation that cannot occur in the "convex" region. These include all the cases where phases are separated by horizontal lines. Presumably the presence of horizontal (in place of curved) lines reflects some peculiar degeneracy arising from the fact that both $V$ and $W$ are (piecewise) parabolic. The horizontal boundaries between $\omega=1 / Q$ and $\omega=1 /(Q+1), \ Q=2,3,4,...$, become curved when they intersect the separation line of $\omega=1 /(Q+1)$ at a point where the first derivative of the

<table>
<caption>Table I. The $K$ Values of Some Bicritical and Tricritical Points of the Model Given by (2)</caption>
<thead>
  <tr>
    <th>Bicritical points</th>
    <th>$K$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$C_{1}$ (tricritical)</td>
    <td>4</td>
  </tr>
  <tr>
    <td>$C_{2}$</td>
    <td>2.27492</td>
  </tr>
  <tr>
    <td>$C_{3}$</td>
    <td>1.74400</td>
  </tr>
  <tr>
    <td>$C_{4}$</td>
    <td>1.51843</td>
  </tr>
  <tr>
    <td>$C_{5}$</td>
    <td>1.41463</td>
  </tr>
  <tr>
    <td>$C_{6}$</td>
    <td>1.36750</td>
  </tr>
  <tr>
    <td>$C_{7}$</td>
    <td>1.34709</td>
  </tr>
  <tr>
    <td>$C_{8}$</td>
    <td>1.33869</td>
  </tr>
</tbody>
</table>

phase boundary is continuous. The phase transition remains first order on the curved boundary. Moving in the other direction, the discontinuity across each horizontal boundary becomes weaker as $\gamma$ decreases and disappears entirely at the vertical line $\gamma=1 / 4$, which is a line of continuous transitions to the $\omega=0$ state. Consequently, $C_{2}, C_{3}, \ldots$ resemble bicritical points and $C_{1}$ resembles a tricritical point. The corresponding $K$ values are given in Table I; one can show that they converge exponentially to the accumulation point at $K=4 / 3$.

Along the horizontal boundary between $\omega=0$ and $\omega=1 / 2$ $(1 / 4 \leqslant \gamma \leqslant 1 / 2)$, the $\omega=1 / 2$ ground state is of the form $x, x^{\prime}, x, x^{\prime}, \ldots$, with $x^{\prime}=1-x$, and $x$ any value within the range

$$
0 \leqslant x \leqslant \frac{1}{2}\left(\gamma-\frac{1}{4}\right)
$$

that is, the ground state is continuously (infinitely) degenerate. The same is true of the $\omega=2 / 4$ phase along the horizontal boundary with $\omega=1 / 2$, where a period consists of $x_{1}, x_{2}, 1-x_{2}, 1-x_{1}$, and $x_{1}$, and $x_{2}$ can change continuously over a small range without changing the energy. At the point $d_{1}(\gamma=5 / 12, K=2)$ this boundary meets the separation line for $\omega=1 / 2$, and the extension of the separation line becomes a line of continuous transitions between $\omega=1 / 2$ and $\omega=2 / 4$. Note the close analogy in this connection between $d_{1}$ and $C_{1}$. We suspect that similar features occur in the other $\omega=1 / Q$ nonconvex regions, but these have not been studied.

A continuous degeneracy of the form noted above has not been observed in other studies in similar systems with nonconvex $W$, so it may well be peculiar to systems in which all the potentials are piecewise parabolic. This may also be the reason why some of the other features found in the

"nonconvex" region in Refs. 4 and 5, such as multiphase points and accumulation points of triple points, have not been observed in our study; however, their absence could equally well be due to the failure to look in the right places with a sufficiently fine grid.

In conclusion, we have shown that the phase diagram for (1) with the specific interactions (2) divides into a "convex" and a "nonconvex" region. The latter contains certain types of first-order transitions and multicritical points, and at least one accumulation point of multicritical points, which do not occur for convex $W$. Some of these features have been observed in other studies of nonconvex $W$ and some have not; the latter may be a consequence of using only piecewise parabolic potentials.

## ACKNOWLEDGMENTS

The research described here has been supported by the U.S. National Science Foundation through grants DMR-8108310 and DMR-8613218. I thank Prof. R. B. Griffiths for advice and for assistance in preparing the manuscript.

## REFERENCES

1. P. Bak, *Rep. Prog. Phys.* 45:587 (1982); S. Aubry, *J. Phys. (Paris)* 44:147 (1983); S. Aubry, *Physica* 7D:240 (1983); S. N. Coppersmith and D. S. Fisher, *Phys. Rev. B* 28:2566 (1983); A. Banerjea and P. L. Taylor, *Phys. Rev. B* 30:6489 (1984).
2. R. B. Griffiths and W. Chou, *Phys. Rev. Lett.* 56:1929 (1986).
3. W. Chou and R. B. Griffiths, *Phys. Rev. B* 34:6219 (1986).
4. C. S. O. Yokoi, L. Tang, and W. Chou, *Phys. Rev. B*, to appear (1988).
5. M. Marchand, K. Hood, and A. Caillé, *Phys. Rev. Lett.* 58:1660 (1987).
6. F. Axel and S. Aubry, *J. Phys. C* 14:5433 (1981).
7. S. Aubry, K. Fesser, and A. R. Bishop, *J. Phys. A* 18:3157 (1985).
8. W. Chou and R. J. Duffin, *Adv. Appl. Math.* 8:486 (1987).
9. R. B. Griffiths, unpublished.