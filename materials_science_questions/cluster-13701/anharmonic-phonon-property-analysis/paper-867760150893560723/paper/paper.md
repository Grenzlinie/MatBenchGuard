ping the c.o.m.-energy, this yields:

$$
H = H_{\text{harm}} + H_{\text{anh}} + H_{\text{int}} \tag{2}
$$

with $H_{\text{anh}} = \frac{1}{m} \pi_M^2 + V(q_M)$ the Hamiltonain for the isolated anharmonic bond, the harmonic Hamiltonian $H_{harm}$, and $H_{int}$ containing the interaction of the anharmonic bond with the harmonic degrees of freedom (d.o.f.). Hamiltonian (2) is the only conserved quantity, after separation of c.o.m. Since the equation of motion is linear in the harmonic d.o.f. these can be exactly eliminated. This leads for $N \to \infty$ and $M = \mathcal{O}(N)$ to the nonlinear integro-differential equation:

$$
\ddot{q}(\tau) + \frac{1}{2C} V'(q(\tau)) - \int_{0}^{\tau} d\tau' k(\tau - \tau') \frac{1}{C} V'(q(\tau')) = 0 \tag{3}
$$

where the index $M$ has been dropped for convenience. $Q_\nu^L(0) \equiv 0$, $P_\nu^L(0) \equiv 0$ and $Q_\mu^R(0) \equiv 0$, $P_\mu^R(0) \equiv 0$ were chosen as initial conditions. $\tau = \omega_0 t$ is a dimensionless time and $\omega_0 = 2(C/m)^{1/2}$ the upper phonon band edge. The lower edge is at zero, due to translation invariance. The memory kernel is given by $k(\tau) = -k_1(\tau)$ where $k_1(\tau) = J_1(\tau)/\tau$ with $J_n$ the Bessel function of order $n$. Having determined for given initial conditions $q(0)$ and $\dot{q}(0)$ a solution $q(\tau)$ of Eq. (3) one obtains the harmonic nearest neighbor bond coordinates $q_n(\tau)$ from

$$
q_n(\tau) = \int_{0}^{\tau} d\tau' G_{|M-n|}(\tau - \tau') \frac{1}{C} V'(q(\tau')) \quad , \quad n \neq M
\tag{4}
$$

with the Green function $G_n(\tau) = 2n J_{2n}(\tau)/\tau$. As initially localized excitation we choose $q(0) = A$ and $\dot{q}(0) = 0$. Use of a "velocity excitation" $q(0) = 0$, $\dot{q}(0) = B$ will not change our results qualitatively. With this initial condition in mind the conservation of the total energy implies that $|q(\tau)| < A$ for all $\tau > 0$.

As well-known, elimination of a macroscopic number of d.o.f. induces dissipation. The frequency dependent damping constant $\gamma(\omega)$ follows from:

$$
\gamma(\omega) = \lim_{\varepsilon \to 0} \frac{1}{\omega} \Im \left( \hat{k}(\omega + i\varepsilon) \right) = \left\{
\begin{array}{cc}
\sqrt{1 - \omega^2} & , \ |\omega| < 1 \\
0 & , \ |\omega| \geq 1
\end{array}
\right.
\tag{5}
$$

with $\omega$ measured in units of $\omega_0$ and $\hat{k}$ the Laplace transform of $k(\tau)$. This exact result is obvious. For $|\omega| < 1$, i.e. for frequencies within the phonon band, the corresponding modes will be damped and consequently decay to zero, whereas all modes with frequency above that band will be undamped. If the anharmonic bond is isolated, i.e. the integral term in Eq. (3) is absent, $q(\tau)$ will perform periodic oscillations with frequency $\Omega_0(A)$, depending on the amplitude $A$. Due to $V''(q_{\text{min}}) = C$ it follows for $A \to 0$ that $\Omega_0(A) \to 1/\sqrt{2}$ in units of $\omega_0$. This frequency is within the phonon band. Since we have chosen a "hard" potential, i.e. $d\Omega_0(A)/dA > 0$, there will be a critical amplitude $A_c^{(0)}$ such that $\Omega_0(A)$ touches the upper phonon band edge:

$$
\Omega_0(A_c^{(0)}) = 1 \quad . \tag{6}
$$

Accordingly, one may speculate that for $A < A_c^{(0)}$ the initial excitation will completely delocalize and will converge to a breather for $A > A_c^{(0)}$. In the following we will chose a symmetric potential $V(x)/C = \frac{1}{2}x^2 + \frac{1}{4}x^4$ for simplicity. $x$ can be scaled such that the prefactor of the quartic term equals 1/4. In that case it is

$$
\Omega_0(A) = \frac{\pi}{4} \sqrt{2 + A^2} / K(-A^2/(2 + A^2)) \tag{7}
$$

with $K(m)$ the complete elliptic integral of first kind. Then Eq. (6) yields:

$$
A_c^{(0)} \cong 1.16715 \quad . \tag{8}
$$

In order to check the validity of our speculation above, we determine first the so-called limiting equation for the asymptotic solution $q_\infty(\tau) = \lim_{\Delta \to \infty} q(\tau + \Delta)$ [16]. The Laplace transform of Eq. (3) taking into account the initial conditions can be solved for the Laplace transform $\hat{q}(z)$ of $q(\tau)$ as function of $\hat{q^3}(z)$. Transforming back to time regime yields:

$$
q(\tau) = A J_0(\tau) - \int_{0}^{\tau} d\tau' J_1(\tau - \tau') q^3(\tau') \quad , \tag{9}
$$

which is equivalent to Eq. (3), as can be proven. For the pure harmonic chain, i.e. neglecting the nonlinear term, we obtain directly $q_{\text{harm}}(\tau) = A J_0(\tau)$, as is well-known. It is straightforward to derive the limiting equation:

$$
q_\infty(\tau) = - \int_{-\infty}^{\tau} d\tau' J_1(\tau - \tau') q_\infty^3(\tau') \quad . \tag{10}
$$

Since $q_\infty(\tau)$ is an asymptotic solution not possessing a relaxing component, its Fourier transform $\widetilde{q}_\infty(\omega)$ can not have an absolutely continuous part $\widetilde{q}_\infty^{(c)}(\omega)$. If it would, its contribution $q_\infty^{(c)}(\tau)$ to $q_\infty(\tau)$ would relax to zero for $\tau \to \infty$. Excluding a singular continuous component (which may occur for disordered systems at the mobility edge), $\widetilde{q}_\infty(\omega)$ must have a discrete support, i. e. $q_\infty(\tau)$ is either constant, periodic or quasiperiodic. If it is quasiperiodic, then there are at least two incommensurate frequencies $\omega_1$ and $\omega_2$. The anharmonicity generates Fourier modes with frequencies $m_1 \omega_1 + m_2 \omega_2$. There exists an infinite number of integer pairs $(m_1, m_2)$ such that $m_1 \omega_1 + m_2 \omega_2$ is within the phonon band. Therefore, these modes are damped (cf. Eq. (5)) and converge to zero. Accordingly, consistent with our numerical results below, Eq. (10) has two kind of solutions, only: A static one $q_\infty^{static}(\tau) \equiv q_\infty$ and a periodic one $q_\infty^{periodic}(\tau + \tau_0) \equiv q_\infty^{periodic}(\tau)$ with $2\pi/\tau_0 > 1$ in order

![](./images/867760150893560723_1.jpg)

FIG. 1: $n$-dependence of $A_{n}^{(\alpha)}$ from Eq. (13) for $\alpha = s,c$. The dashed line represents $A_{c}^{(0)} \cong 1.16715$ (cf. Eq. (8)).

to avoid an overlap with the phonon frequencies $|\omega| \leq 1$. Substituting $q_{\infty}^{static}(\tau) \equiv q_{\infty}$ into Eq. (10) yields the single solution $q_{\infty}^{static}(\tau) \equiv 0$.

So far we have argued that two types of asymptotic solutions exist, a static and a periodic one. In order to investigate the existence of a critical amplitude $A_{c}$ we solve Eq. (9) iteratively. With the asymptotic behavior of $J_{1}$ we arrive at:

$$
\begin{aligned}
q(\tau) \cong & A \sqrt{\frac{2}{\pi}}\left[\left(\tau / \tau_{s}\right)^{-\frac{1}{2}} \sin \left(\tau-\frac{\pi}{4}\right)\right. \\
& \left.-\left(\tau / \tau_{c}\right)^{-\frac{1}{2}} \cos \left(\tau-\frac{\pi}{4}\right)\right]
\end{aligned}
\tag{11}
$$

with relaxation times:

$$
\tau_{\alpha}(A)=\left[\sum_{n=0}^{\infty}(-1)^{n} \beta_{n}^{(\alpha)} A^{2 n}\right]^{2} \quad, \quad \alpha=s, c \quad. \tag{12}
$$

$\beta_{n}^{(\alpha)}$ are given by $n$-fold integrals over products of $J_{1}$ and $J_{0}$. Eq. (11) with $\tau_{\alpha}(A)$ from Eq. (12) is a formal result for $q(\tau)$ represented by a power series in $A$. It is a physical solution, only if the infinite sums in Eq. (12) do exist. The critical value $A_{c}$ is such that this is true for $A < A_{c}$. Then it is:

$$
A_{c}=min \left\{A_{c}^{(c)}, A_{c}^{(s)}\right\} \quad, \quad A_{c}^{(\alpha)}=\lim _{n \rightarrow \infty} A_{n}^{(\alpha)} \quad,
$$

$$
A_{n}^{(\alpha)}=\left|\beta_{n}^{(\alpha)} / \beta_{n+1}^{(\alpha)}\right|^{1 / 2} \quad, \quad \alpha=s, c \quad. \tag{13}
$$

An analytical calculation of these integrals seems impossible. Therefore it is done numerically which leads to $A_{n}^{(\alpha)}$ shown in Figure 1 up to $n=10$. For $n>10$ the numerical errors become significant. This result gives evidence that $A_{c}$ is close to $A_{c}^{(0)}$. For $A < A_{c}$ the asymptotic time dependence of $q(\tau)$ is similar to that of the harmonic solution $A J_{0}(\tau)$, however with a different phase and a renormalized relaxation time $\tau_{\text {rel }}(A)=\sqrt{\tau_{s}^{2}(A)+\tau_{c}^{2}(A)}$, which diverges at $A_{c}$. This behavior of $\tau_{r e l}(A)$ follows from the divergence of the alternating sums (cf. Eq. (12)) due to the quantitative difference of $\beta_{n}^{(\alpha)}$ for $n$ even and $n$ odd, which also leads to the "oscillations" of $A_{n}^{(\alpha)}$ in Figure 1. According to Eq. (11), $q(\tau)$ decays by an inverse square root law, as also observed for the original $\beta$-FPU chain [10].

![](./images/867760150893560723_2.jpg)

FIG. 2: Top panel: $A$-dependence of $q^{e n v}(\tau_{i})$ for $\tau_{i} \approx 10^{3}$ (circles), $10^{4}$ (plus signs) and $10^{5}$ (crosses) time units. The inset demonstrates the asymptotic behavior $q^{e n v}(\tau_{i}) \sim A$ (solid line). Bottom panel: DB frequency $\Omega^{num }(A)$ at $\tau_{i} \approx 10^{5}$ time units as function of $A$. The arrow indicates the critical value $A_{c}^{(0)}$ from Eq. (8) and the dashed line $A_{c}^{num } \cong 1.181$. The inset shows the asymptotic $A$-dependence $\Omega(A) \sim A$ (solid line).

In order to check these results and to access $A > A_{c}$, we have solved Eq. (3) numerically up to $\tau_{max }=10^{5}$ using an integration step of $h=0.05$. Figure 2 depicts $q^{e n v}(\tau_{i} ; A)$ for $\tau_{i} \approx 10^{3}, 10^{4}$ and $10^{5}$ where $q^{e n v}(\tau ; A)$ is the envelope function of $|q(\tau)|$ for given $A$. With increasing $\tau_{i}$ a clear sharpening of the transition is found at $A_{c}^{num } \cong 1.181$, like for a second order phase transition with finite size effects. $A_{c}^{num }$ differs from $A_{c}^{(0)}$ by about $1.2 \%$. The frequency $\Omega^{num }(A)$ close to $\tau_{max }$ is shown in Figure 2. For $A < A_{c}^{num }$ we have $\Omega^{num }(A) \cong 1$ and for $A > A_{c}^{num }$ it is well approximated by $\Omega_{0}(A)$ for the isolated bond. However, for $A$ above but close to $A_{c}^{num }$ the discrepancies are about $2 \%$, whereas for $A \gg A_{c}^{num }$ they disappear. Whether the small deviation of $A_{c}^{num }$ and $\Omega^{num }$ from $A_{c}^{(0)}$ and $\Omega_{0}(A)$, respectively, is genuine or stems from numerical inaccuracy is unclear. Hence it is not obvious that $A_{c}=A_{c}^{(0)}$. For $A > A_{c}^{num }$ the initial excitation indeed converges to a DB with frequency $\Omega^{num }(A)$. Figure 3 shows the numerically determined relaxation time $\tau_{rel }(A)$ for $A < A_{c}^{num }$, and for $A > A_{c}^{num }$ the inverse modulation frequency $2 \pi / \omega_{mod }(A)$ of a modulation of the DB, which is observed numerically. For $\tau \rightarrow \infty$ the modulation amplitude decays to zero. $\tau_{rel }$ has been determined from the criterion $q^{e n v}(\tau_{r e l})=A / 10$. Both, $\tau_{rel }$ and $2 \pi / \omega_{mod }$

![](./images/867760150893560723_3.jpg)

FIG. 3: Renormalized relaxation time $\tau_{rel}$ (circles) and modu-
lation period $2\pi/\omega_{mod}$ (crosses) as function of $A$. The dashed
line indicates $A_{c}^{num} \cong 1.181$. The solid lines represent power
law fits of $\tau_{rel}$ and $2\pi/\omega_{mod}$ with exponents 0.61 and 0.87,
respectively, which are supported by the log-log plots of the
inset.

seem to diverge at $A_{c}^{num}$ by a power law with an expo-
nent $\approx 0.61$ and $\approx 0.87$, respectively (see inset of Figure
3). A power law divergence $\tau_{rel}(A) \sim (A_{c}-A)^{-\gamma}$ im-
plies that $\beta_{n}^{(\alpha)} \sim (A_{c})^{-n}n^{-(1-\gamma/2)}$ for $n \to \infty$. Whereas
the exponential factor is strongly supported by our cal-
culations the validity of the power law part can not be
checked due to the limitation $n \leq 10$.

Finally, we have analytically determined the moments
$m_{\ell}^{({\rm pot})}(\tau) = \sum_{n=1}^{N}(n-M)^{\ell}e_{n}^{({\rm pot})}(\tau)$, $\ell=1,2,3,\dots$ of the
potential energy profile $e_{n}^{({\rm pot})}(\tau)$ in the thermodynamic
limit. As a result we find

$$
\begin{aligned}
m_{\ell}^{({\rm pot})}(\tau)= & \int_{0}^{\tau}d\tau_{1}\int_{0}^{\tau}d\tau_{2}K_{\ell}(\tau-\tau_{1},\tau-\tau_{2}) \\
& \times \frac{1}{C}V'(q(\tau_{1}))\frac{1}{C}V'(q(\tau_{2}))\ .\qquad(14)
\end{aligned}
$$

Let us restrict to $\ell=2$. $K_{2}(x,y)$ can be calculated ana-
lytically and expressed by $J_{1}(x\pm y)$ and $J_{2}(x\pm y)$. Tak-
ing into account the asymptotic expansion of $J_{n}$ we find
$m_{2}^{({\rm pot})}(\tau) \sim \tau^{2}$ for $\tau \to \infty$, for all $A$. Hence, the en-
ergy transportation is ballistic. This is expected since
the transportation is within the half infinite left and right
harmonic part of the chain. Using the profile of the ki-
netic energy will not change these results.

To summarize, based on combined analytical and nu-
merical calculations of a reduced $\beta$-FPU chain where the
anharmonicity is restricted to a single bond we have pre-
sented clear evidence for the existence of a critical ampli-
tude $A_{c}$ which separates delocalization from localization.
This demonstrates that a single conservation law is suf-
ficient for such a transition. $A_{c}^{num}$ differs slightly from
$A_{c}^{(0)}$. Therefore it is not clear whether $A_{c}$ coincides with
$A_{c}^{(0)}$ or not. Of course, no compelling arguments exist
for their equality. In addition, the divergence of the iter-
ation series is the mathematical origin of the transition
at $A_{c}$ and leads for $A < A_{c}$ to a renormalized (due to an-
harmonicity) relaxation time $\tau_{\rm rel}$ which diverges at $A_{c}$.
The numerical solution suggests a power law divergence
with exponent smaller then one. Above $A_{c}$ it yields the
convergence towards a DB with frequency very close to
$\Omega_{0}(A)$ of the isolated bond. Finally, from the large $\tau$
behavior of the second moment $m_{2}(\tau)$ we find ballistic
energy transportation for $A < A_{c}^{num}$ and $A > A_{c}^{num}$.
This proves that a divergence of $m_{2}(\tau)$ is not necessar-
ily an indication of complete energy spreading, as it has
been assumed for DNLS [17], supporting the conclusion
in [15].

This work was started when one of us (R. S.) was
a member of the Advanced Study Group 2007 at the
MPIPKS Dresden. R. S. gratefully acknowledges the
MPIPKS for its hospitality and financial support and S.
Aubry, V. Bach, N. Blümer and S. Flach for stimulating
discussions.

[1] W. Götze, “Complex Dynamics of Glass-Forming Liq-
uids, A Mode-Coupling Theory”, Oxford University
Press, Oxford UK (2008)

[2] S. P. Das, Rev. Mod. Phys. 76, 785 (2004)

[3] W. R. Hamilton, Proc. R. Irish Acad. 1, 341 (1841)

[4] G. S. Zavt et. al, Phys. Rev. E47, 4108 (1993)

[5] P. K. Datta and K. Kundu, Phys. Rev. B51, 6287 (1995)

[6] J. L. van Hemmen, Lecture Notes 93, Springer (1979)

[7] S. Flach and C. R. Willis, Phys. Rep. 295, 181 (1998);
S. Aubry, Physica D216, 1 (2006)

[8] M. I. Molina and G. P. Tsironis, Physica D65, 267
(1993); L. J. Bernstein et al., Phys. Lett. A181, 135
(1993); M. Johansson et al., Phys. Rev. B52, 231 (1995)

[9] G. P. Tsironis and S. Aubry, Phys. Rev. Lett. 77, 5225
(1996)

[10] F. Piazza et al, J. Phys. A34, 9803 (2001)

[11] R. Reigada et al, Phys. Rev. E66, 046607 (2002)

[12] J. Dorignac, J. Zhou and D. K. Campbell, Physica D327,
486 (2008)

[13] S. Flach et al., Phys. Rev. Lett. 78, 1207 (1997); M. I.
Weinstein, Nonlinearity 12, 673 (1999)

[14] A. Stefanov and P. G. Kevrekidis, Nonlinearity 18, 1841
(2005)

[15] G. Kopidakis et al. Phys. Rev. Lett. 100, 084103 (2008)

[16] R. K. Miller, “Nonlinear Volterra Integral Equations”,
W. A. Benjamin (1971)

[17] A. S. Pikovsky and D. L. Skepelyansky, Phys. Rev. Lett.
100, 094101 (2008)