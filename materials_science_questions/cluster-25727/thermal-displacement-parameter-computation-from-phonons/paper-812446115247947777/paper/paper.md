Solid State Communications, Vol. 39, pp. 123-125
Pergamon Press Ltd. 1981. Printed in Great Britain.
0038-1098/81/010123-03$02.00/0

# A GENERAL APPROACH FOR BUILDING UP REDUCED HEATBATHS: APPLICATION TO THE DEBYE ISOTROPIC SOLID

P. Grigolini and G. Pastori-Parravicini

Istituto di Fisica, Università di Pisa, Italy
and
Gruppo Nazionale di Struttura della Materia del CNR, Pisa, Italy

(Received 13 February 1981 by F. Bassani)

It is shown that the Mori theory is a suitable theoretical tool for replacing a true phonon reservoir with an equivalent one involving only a few degrees of freedom.

## 1. INTRODUCTION

ACCORDING with the theory of nonequilibrium thermodynamics [1], the relaxation properties exhibited by a subsystem of interest are an effect of the ineluctable interaction with the remaining part (heatbath) of the system under study. Since a heatbath usually involves a huge amount of degrees of freedom, intense investigations [2, 3] are currently being performed to replace the true many-body thermal bath by an effective few-body one. The influence of a bona fide thermal bath on the subsystem of interest has to be as close as possible to that of the true one. Such a faithful simulation of the many-body heatbath is needed if one wishes to avoid the often adopted assumption of time scale separation.

The equivalent heatbath modeling method has been developed independently by two different research groups [4, 5], within apparently different theoretical frameworks. Adelman and co-workers [4] arrived at this method having in mind the problem of gas-solid collisions. In a subsequent paper [6] their approach, known as the molecular timescale generalized Langevin equation (MTGLE) theory, has been shown to be quite successfull in dealing with a phonon thermal bath such as the Debye isotropic solid. On the other hand, Grigolini and co-workers [5] developed the "reduced model theory" (RMT) having in mind a completely different subject of investigation: the radiationless transitions in molecules. More recently [7, 8] the RMT found in the Mori theory a rigorous theoretical support.

In this paper, for the first time, we apply the "reduced model theory" to describe phonon thermal baths. The results obtained suggest the equivalence between the RMT and MTGLE even in the case of a chain with a very small number of fictitious variables.

## 2. SURVEY OF THE MORI THEORY

To describe the main features of the RMT, we give a brief survey of some relevant aspects of the Mori theory [9]. Consider the standard equation of motion for an operator

$$
\frac{\mathrm{d}}{\mathrm{d} t} a=i L a
\tag{1}
$$

After defining a suitable scalar product between operators, it is possible to build up a chain of variables in the following way

$$
\begin{aligned}
f_{0} & \equiv a, \\
f_{1} & \equiv\left(1-P_{0}\right) i L f_{0}, \\
f_{2} & \equiv\left(1-P_{1}\right)\left(1-P_{0}\right) i L f_{1}, \\
f_{j+1} & \equiv\left(1-P_{j}\right)\left(1-P_{j-1}\right)...\left(1-P_{1}\right)\left(1-P_{0}\right) i L f_{j},
\end{aligned}
\tag{2}
$$

The projection operators $P_{j}$ are defined by

$$
P_{j} g \equiv\left(g, f_{j}^{+}\right)\left(f_{j}, f_{j}^{+}\right)^{-1} f_{j}.
\tag{3}
$$

Several years ago [9] Mori studied the kind of time evolution defined by

$$
f_{i}(t) \equiv \exp \left\{i L_{i} t\right\} f_{i},
\tag{4a}
$$

where

$$
L_{i}=\left(1-P_{i-1}\right) L_{i-1},
\tag{4b}
$$

$$
L_{0}=L.
\tag{4c}
$$

He showed that the corresponding correlations functions $\Phi_{i}(t) \equiv\left(f_{i}^{+}\right)\left(f_{i}, f_{i}^{+}\right)^{-1}$ satisfy a set of coupled differential equations given by

$$
\frac{\mathrm{d}}{\mathrm{d} t} \Phi_{i}(t)=i \omega_{i} \Phi_{i}(t)-\int_{0}^{t} \Delta_{i+1}^{2} \Phi_{i+1}(t-\tau) \Phi_{i}(\tau) \mathrm{d} \tau,
\tag{5a}
$$

where

$$i\omega _{i}\equiv i(Lf_{i},f_{i}^{+})(f_{i},f_{i}^{+})^{-1},$$

$$\Delta _{i}^{2}\equiv (f_{i},f_{i}^{+})(f_{i-1},f_{i-1}^{+})^{-1}.$$

To obtain a rigorous support for the RMT,
Grigolini and co-workers [3,7,8] focused their attention
on a second kind of time evolution defined by
$$a_{i}(t)=e^{i L t} f_{i}.\qquad(6)$$

This is equivalent to expanding $L$ over the basis set
$f_{0},f_{1},...f_{i},....$ If the column vector
$A \equiv(f_{0}, f_{1},..., f_{n})$ spans all the slow variables of the
physical system under study, one obtains [7,8,10,11]
$$\frac{\mathrm{d} \mathbf{A}}{\mathrm{d} t}=\boldsymbol{\Gamma} \mathbf{A}+\mathbf{F}(t),\qquad(7)$$
where
$$\boldsymbol{\Gamma}=\left(\begin{array}{cccccccc}
i \omega_{0} & 1 & 0 &. &. &. & & \\
-\Delta_{1}^{2} & i \omega_{1} & 1 &. &. &. & & \\
0 & -\Delta_{2}^{2} & i \omega_{2} &. &. &. & & \\
. &. &. &. &. &. & & \\
. &. &. &. & i \omega_{n-1} & 1 & & \\
. &. &. &. & -\Delta_{n}^{2} & i \omega_{n}-\gamma_{n}
\end{array}\right)$$
and
$$\gamma_{n}=\int_{0}^{\infty} \Delta_{n+1}^{2} \Phi_{n+1}(\tau) \mathrm{d} \tau\qquad(9)$$

Only the last component of $F, f_{n+1}(t)$ , does not vanish.
This fluctuating force can be regarded as being a white
noise related to the friction $\gamma_{n}$ by the fluctuation dissipation theorem [3,7,8].

The RMT consists in interpretating equation (7) in
terms of mechanical models. If the variable of interest
$f_{0}$ is spatial in nature $(f_{0}=x_{0})$ and $\omega_{i}=0$ , it is
straightforward to show [7,8] that fourth-order
truncation, for example, is equivalent to
$$\dot{x}_{0}=v_{0}$$

$$\dot{v}_{0}=-\Delta_{1}^{2} x_{0}+\Delta_{2}^{2}\left(x_{0}-x_{1}\right)$$

$$\dot{v}_{1}=\ddot{x}_{1}=-\Delta_{3}^{2}\left(x_{0}-x_{1}\right)-\gamma_{4} x_{1}+f_{5}(t)$$

The extension to higher order truncations is trivial.

### 3. THE CASE OF THE DEBYE ISOTROPIC SOLID

We now apply the above considerations to a solid
with a single atom of mass $M$ per unit cell. In the
harmonic approximation, the nuclear motion is
described by the Hamiltonian
$$H=\sum_{\mathbf{q}} \hbar \omega(\mathbf{q})\left(a_{\mathbf{q}}^{+} a_{\mathbf{q}}+1 / 2\right),\qquad(10)$$
where $a_{q}^{+}, a_{q}$ are the creation and annihilation
operators corresponding to the normal mode of wave
vector q, and the sum over q runs on the first Brillouin
zone (the branch index has been omitted for simplicity).
The phonon dispersion curves are assumed to be
$\omega(q)=v_{s} q$ with the same sound velocity $v_{s}$ for
longitudinal and transverse modes up to the cut-off
Debye frequency $\omega_{D}$ . The corresponding spectral
density of phonon states (normalized to 1) is then
$D(\omega)=3 \omega^{2} / \omega_{D}^{3}$ for $0 \leqslant \omega \leqslant \omega_{D}$ . In the following
we need the adiabatic frequency $\omega_{a}$ and the even
moments of the spectral density function $D(\omega)$
defined as
$$1 / \omega_{a}^{2}=\int_{0}^{\omega_{D}}\left(1 / \omega^{2}\right) D(\omega) \mathrm{d} \omega,\qquad(11a)$$

$$\left\langle\omega^{p}\right\rangle=\int_{0}^{\omega_{D}} \omega^{p} D(\omega) \mathrm{d} \omega.\qquad(11b)$$

In the Debye model, equations (11) give $\omega_{a}^{2}=\omega_{D}^{2} / 3$ ,
$\langle\omega^{2}\rangle=(3 / 5) \omega_{D}^{2},\langle\omega^{4}\rangle=(3 / 7) \omega_{D}^{4}$ , etc.

We take as our variable of interest the displacement
$u_{n x}$ along the $x$ -direction of the atom in the generical
cell $\tau_{n}$ (without loss of generality we keep $\tau_{n}=0$ ). We
can expand $u_{n x}$ in normal modes [12] with polarization
vectors in the $x$ direction
$$u_{n x} \equiv f_{0}=\frac{1}{\sqrt{ } N}\left(\frac{\hbar}{2 M \omega(\mathbf{q})}\right)^{1 / 2}\left(a_{\mathbf{q}}+a_{\mathbf{q}}^{+}\right).\qquad(12)$$

We assume that the crystal is in thermal equilibrium
with statistical density matrix $\rho=\exp \{-\beta H\} / Tr\{e^{-\beta H}\}$ .
The only non-vanishing scalar products of creation and
annihilation operators are those of the type $(a_{q}, a_{q}^{+})$
and $(a_{q}^{+}, a_{q})$ . In the classical limit of very high tempera
tures $(k_{B} T \gg \hbar \omega_{D})$ we have
$$\left(a_{\mathbf{q}}, a_{\mathbf{q}}^{+}\right)=\frac{1}{\mathrm{e}^{\hbar \omega_{\mathbf{q}} / k_{B} T}-1} \approx \frac{k_{B} T}{\hbar \omega_{\mathbf{q}}} \approx\left(a_{\mathbf{q}}^{+}, a_{\mathbf{q}}\right).\qquad(13)$$

Starting from the operator defined by equation (12)
and evaluating the scalar products by means of
equation (13), we can easily obtain the parameters
and the fictitious variables of the Mori chain. In
particular from equation (5b) and equation (5c) we
have $\omega_{i}=0$ and
$$\begin{aligned}
& \Delta_{1}^{2}=\omega_{a}^{2}, \\
& \Delta_{2}^{2}=\left\langle\omega^{2}\right\rangle-\omega_{a}^{2}, \\
& \Delta_{3}^{2}=\left(\left\langle\omega^{4}\right\rangle-\left\langle\omega^{2}\right\rangle^{2}\right) / \Delta_{2}^{2}, \\
& \Delta_{4}^{2}=\frac{\left\langle\omega^{6}\right\rangle-2\left\langle\omega^{2}\right\rangle\left\langle\omega^{4}\right\rangle+\left\langle\omega^{2}\right\rangle^{3}}{\Delta_{2}^{2} \Delta_{3}^{2}}-\Delta_{3}^{2}.
\end{aligned}\qquad(14)$$

It is interesting to verify that the (non vanishing)
proper frequencies of the non-dissipative part of our

matrix $\boldsymbol{\Gamma}$ of equation (8), at the appropriate orders of truncation, coincide with the normal mode frequencies provided by the MTGLE theory [6].

A further interesting check concerns the evaluation of the damping parameters $\gamma_{n}$, defined by equation (9). Using equations (10-13) we can easily calculate the correlation function for the atomic displacement operator $u_{n x}$
$$
\begin{aligned}
\Phi_{0}(t) & =\left(f_{0}(t), f_{0}^{+}\right)\left(f_{0}, f_{0}^{+}\right)^{-1} \\
& =\left(\sin \omega_{D} t\right) / \omega_{D} t.
\end{aligned}
$$

The Laplance transform $\hat{\Phi}_{0}(z)$ is given by
$$
\hat{\Phi}_{0}(z)=\frac{1}{\omega_{D}} \operatorname{arctg} \frac{\omega_{D}}{z}.
$$

In particular we have $\hat{\Phi}_{0}(0)=\left(1 / \omega_{D}\right)(\pi / 2)$.

Taking the Laplace transforms of equations (5a), we obtain that $\gamma_{1}=\Delta_{1}^{2} \Phi_{0}(0), \gamma_{2}=\Delta_{2}^{2} / \gamma_{1}, \gamma_{3}=\Delta_{3}^{2} / \gamma_{2}$, etc. The explicit expression of the first $\gamma_{i}$ is $\gamma_{1}=\frac{1}{6} \pi \omega_{D}=0.167 \omega_{D} ; \gamma_{2}=(8 / 5 \pi) \omega_{D}=0.162 \pi \omega_{D} ;$ $\gamma_{3}=\frac{9}{56} \pi \omega_{D}=0.161 \pi \omega_{D} ; \gamma_{4}=0.160 \pi \omega_{D}$. It is encouraging indeed that these damping parameters are the same as those provided by the MTGLE theory [6].

Before closing we can make a few remarks on the case that the variable of interest is the velocity of a given atom:
$$
f_{0}=(-i) \frac{1}{\sqrt{ } N} \sum_{\mathbf{q}} \frac{\hbar \omega(\mathbf{q})}{2 M}\left(a_{\mathbf{q}}-a_{\mathbf{q}}^{+}\right).
$$

The parameters of the new Mori chain generated by the velocity operator can be calculated in a similar way. We have $\omega_{i}=0$ and $\Delta_{1}^{2}=\left\langle\omega^{2}\right\rangle, \Delta_{2}^{2}=\left(\left\langle\omega^{4}\right\rangle-\left\langle\omega^{2}\right\rangle^{2}\right) /\left\langle\omega^{2}\right\rangle$, etc. A quite remarkable feature is that the $n+1$ th order space case seems to correspond to the $n$th order velocity case. As far as the damping parameters are concerned, we have the surprising result that they vanish. In fact the velocity correlation function is easily evaluated to be
$$
\Phi_{0}(t)=3\left\{\frac{\sin \omega_{D} t}{\omega_{D} t}+\frac{2 \cos \omega_{D} t}{\omega_{D}^{2} t^{2}}-\frac{2 \sin \omega_{D} t}{\omega_{D}^{3} t^{2}}\right\}.
$$

Since $\hat{\Phi}_{0}(0)=0$, equations (5a) imply that $\hat{\Phi}_{n}(0)=0$ for even $n$, and the Markovian assumption cannot be done at any level of truncation in this case.

The results of this paper can be extended to more realistic situations including the occurrence of optical phonons and arbitrary temperatures. The Mori theory constitutes a valuable tool in the problem of equivalent heatbath modeling.

## REFERENCES
1. See for instance R. Zwanzig, *Lectures in Theoretical Physics* (Boulder), III, 106 (1960). Interscience Publishers, New York (1961).
2. S.A. Adelman, *Adv. Chem. Phys.* 44, 143 (1980).
3. P. Grigolini, *Molecular Dynamics*. Wiley, New York (1981) (in press).
4. S.A. Adelman & B.J. Garrison, *J. Chem. Phys.* 65, 3751 (1976); S.A. Adelman & J.D. Doll, *J. Chem. Phys.* 64, 2375 (1976).
5. P. Grigolini, *Chem. Phys. Lett.* 47, 483 (1977); P. Grigolini & A. Lami, *Chem. Phys.* 30, 61 (1978).
6.- M. Berkowitz, C.L. Brooks III & S.A. Adelman, *J. Chem. Phys.* 72, 3889 (1980).
7. M. Ferrario & P. Grigolini, *J. Math. Phys.* 20, 2567 (1979).
8. M. Ferrario & P. Grigolini, *Chem. Phys. Lett.* 62, 100 (1979).
9. H. Mori, *Prog. Theor. Phys.* 34, 423 (1965); 34, 399 (1965).
10. T. Karasudani, K. Nagano, H. Okamoto & H. Mori, *Prog. Theor. Phys.* 61, 850 (1979).
11. G. Ciccotti & J.P. Ryckaert, *Molec. Phys.* 40, 141- (1980).
12. See for instance J.M. Ziman, *Electrons and Phonons*. Oxford University Press (1962).