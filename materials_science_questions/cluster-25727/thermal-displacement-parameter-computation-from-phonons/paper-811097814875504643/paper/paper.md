# Surface Effects in the Second-Order Doppler Shift of the Mössbauer Resonance
R. F. WALLIS
U. S. Naval Research Laboratory, Washington, D. C.
AND
D. C. GAZIS
IBM Research Center, Yorktown Heights, New York
(Received April 30, 1962)

The second-order Doppler shift in the Mössbauer effect depends upon the mean-square velocities of the emitting and absorbing atoms. On the basis of a theorem discussed by Born in connection with the lattice dynamical theory of the Debye-Waller factor, a general expression has been obtained for the mean-square velocity of an arbitrary atom in a crystal lattice, assuming harmonic forces. The result is valid for any temperature and may be applied to lattices having free surfaces or impurities. Approximate expressions are developed for the high- and low-temperature limits. The general results are applied to specific calculations of the mean-square velocity for atoms at or near a free surface. Ordinarily, the mean-square velocity turns out to be smaller for an atom at the surface than for one in the interior of the crystal. This is a consequence of the surface atom being linked to fewer neighboring atoms than is the case for an interior atom. It is concluded, however, that whether or not a crystal lattice possesses surface modes of vibration has little direct bearing on the mean-square velocity of surface atoms.

## I. INTRODUCTION
As shown by Pound and Rebka¹ and by Josephson² the Doppler effect in second order leads to a temperature-dependent shift of the Mössbauer resonance line. By using an argument based on energy conservation, Josephson concluded that the energy $E$ of a gamma ray is shifted by an amount $ΔE$ given by
$$ΔE=E\left(\left\langle v^{2}\right\rangle / 2 c\right), \quad(1)$$
where $\langle v^{2}\rangle$ is the mean-square velocity of the emitting atom. A corresponding shift occurs during absorption. An experimentally determined frequency shift is, therefore, related to the difference of the mean-square velocities of the absorbing and emitting atoms.

A lattice dynamical theory of the second-order Doppler shift for impurity atoms in a solid has recently been given by Maradudin, Flinn, and Ruby.³ These authors find that the mean-square velocity of an impurity atom is determined by the masses of the impurity atom and the host atoms and by the forces with which the impurity atom is bound to the other atoms. By making measurements on the temperature dependence of the shift in the Mössbauer resonance frequency, one can, in principle, obtain information about the force constants which link the absorbing or emitting atom to its various neighbors.

In the present paper we consider the effect of proximity to a free surface on the second-order Doppler shift. One may expect that the interatomic forces associated with an atom near a surface will be different from those associated with an atom well in the interior and that this difference will be manifested in the second-order Doppler shift. Furthermore, if surface modes of vibration exist in the crystal, one may expect that the mean-square velocity of a surface atom is influenced by the surface modes. Information about the latter may then be available from observations of the second-order Doppler shift.

## II. GENERAL FORMULATION
In this section we derive a general expression for the mean-square velocity of an atom in a crystal. We assume that the interatomic forces are harmonic, but we do not assume periodic boundary conditions. Let $\mathbf{u}_{l\kappa}$ be the vector displacement of the $\kappa$th atom in the $l$th unit cell. Then the equations of motion in the harmonic approximation can be written as
$$\ddot{\xi}_{l \kappa i}+\sum_{l^{\prime} \kappa^{\prime} j} \mathfrak{D}\left(l \kappa i ; l^{\prime} \kappa^{\prime} j\right) \xi_{l^{\prime} \kappa^{\prime} j}=0, \quad i, j=x, y, z, \quad(2)$$
where
$$\xi_{l \kappa}=m_{l \kappa}{ }^{1 / 2} \mathbf{u}_{l \kappa}, \quad(2 \mathrm{a})$$
$\mathfrak{D}(l \kappa i ; l' \kappa' j)$ is an element of the dynamical matrix of the crystal and $m_{l\kappa}$ is the mass of the atom $\kappa$. Since we are interested in calculating velocities rather than displacements, we differentiate Eq. (2) with respect to time and obtain
$$\frac{d^{3} \xi_{r i}}{d t^{3}}+\sum_{r^{\prime} j} \mathfrak{D}\left(r i ; r^{\prime} j\right) \dot{\xi}_{r^{\prime} j}=0, \quad(3)$$
where the pair of indices $l\kappa$ is replaced by the single index $r$. Setting
$$\dot{\xi}_{r i}=B_{r i} e^{i \omega t}, \quad(4)$$
and substituting into Eq. (3), one gets
$$\sum_{r^{\prime} j}\left[\mathfrak{D}\left(r i ; r^{\prime} j\right)-\omega^{2} \delta_{r r^{\prime}} \delta_{i j}\right] B_{r^{\prime} j}=0. \quad(5)$$

The amplitudes $B_{r i}$ which satisfy Eq. (5) are eigen

¹ R. V. Pound and G. A. Rebka, Jr., Phys. Rev. Letters 4, 274 (1960).
² B. D. Josephson, Phys. Rev. Letters 4, 341 (1960).
³ A. A. Maradudin, P. A. Flinn, and S. Ruby, Phys. Rev. 126, 9 (1962).

vectors of the dynamical matrix, the corresponding eigenvalues being the squares of the normal mode fre- quencies. Let us characterize the normal modes by an index $\theta$ , and let us assume that a single mode is excited. The time average of the square of a velocity com- ponent for such a mode is given by
$$\begin{aligned}
\left\langle\left[\dot{u}_{r i}(\theta)\right]^{2}\right\rangle_{\mathrm{av}} & =\left(1 / m_{r}\right)\left\langle\left[\operatorname{Re} \xi_{r i}(\theta)\right]^{2}\right\rangle_{\mathrm{av}} \\
& =\left(1 / 2 m_{r}\right)\left|B_{r i}(\theta)\right|^{2}.
\end{aligned}\qquad(6)$$

The mean kinetic energy $T_{\theta}$ in the mode $\theta$ is given by
$$\begin{aligned}
T_{\theta} & =\frac{1}{2} \sum_{r, i} m_{r}\left\langle\left[\dot{u}_{r i}(\theta)\right]^{2}\right\rangle_{\mathrm{av}} \\
& =\frac{1}{4} \sum_{r, i}\left|B_{r i}(\theta)\right|^{2}.
\end{aligned}\qquad(7)$$

Under thermal equilibrium conditions the time average of the kinetic energy specified by Eq. (7) is equal to the ensemble average specified by
$$T_{\theta}=\frac{1}{4} \hbar \omega_{\theta} \operatorname{coth}\left(\hbar \omega_{\theta} / 2 k T\right).\qquad(8)$$

It is clear from Eqs. (7) and (8) that the eigenvectors Bri(0) are not normalized to unity. A set of orthonormal eigenvectors $C_{r i}(\theta)$ is obtained by the definition
$$C_{r i}(\theta)=\left(4 T_{\theta}\right)^{-\frac{1}{2}} B_{r i}(\theta).\qquad(9)$$

By summing Eq. (6) over all modes $\theta$ and over the Cartesian components i, one obtains the following ex- pression for the complete mean square velocity ofatom r:
$$\begin{aligned}
\left\langle\left|\dot{\mathbf{u}}_{r}\right|^{2}\right\rangle & =\sum_{\theta, i}\left\langle\left|\dot{u}_{r i}(\theta)\right|^{2}\right\rangle_{\mathrm{av}} \\
& =\left(2 / m_{r}\right) \sum_{\theta, i} T_{\theta}\left|C_{r i}(\theta)\right|^{2}.
\end{aligned}\qquad(10)$$

The right-hand side of Eq. (10) contains a sum over normal modes of a function of normal mode frequencies times the square of a given element of the orthonormal eigenvector for that mode. Such sums can be simplified by means of a theorem utilized by $Born^{4}$ in his latticedymanical theory of the Debye-Waller factor. If $f(\omega^{2})$  is some function of the square of a normal mode fre- quency, then the theorem states that
$$\sum_{\theta} f\left(\omega_{\theta}^{2}\right) \mathbf{C}(\theta) \mathbf{C}^{T}(\theta)=f(\mathfrak{D}),\qquad(11)$$
 where $C^{T}(\theta)$ is the transpose of the eigenvector $C(\theta)$ . Transforming Eq. (10) by means of Eq. (11) and utilizing Eq. (8), one obtains
$$\left\langle\left|\dot{\mathbf{u}}_{r}\right|^{2}\right\rangle=\left(1 / 2 m_{r}\right) \sum_{i}\left[\hbar \mathfrak{D}^{\frac{1}{2}} \operatorname{coth} \frac{\hbar \mathfrak{D}^{\frac{1}{2}}}{2 k T}\right]_{r i, r i}, \quad(12)$$
 where the subscript ri,ri denotes a diagonal matrix element of the matrix in square brackets.
The result given by Eq. (12) for the mean-square velocity of the rth atom is restricted to harmonic forces, but is otherwise quite general. It applies over a broad range of temperature to crystal lattices containing im- purities, disorder, free surfaces, and other manifesta- tions of deviations from a perfect periodic lattice.
Useful high- and low-temperature approximations are obtained by appropriate power series expansions of the quantity $coth(\hbar \mathfrak{D}^{\frac{1}{2}} / 2 k T)$ in Eq. (12). At high tempera tures the result is
$$\begin{aligned}
\left\langle\left|\dot{\mathbf{u}}_{r}\right|^{2}\right\rangle= & \sum_{i}\left(k T / m_{r}\right) \\
& +\sum_{i}\left[\hbar^{2} \mathfrak{D} / 12 m_{r} k T\right]_{r i, r i}+\cdots, \quad(13)
\end{aligned}$$
 while at low temperatures the result is
$$\begin{aligned}
\left\langle\left|\dot{\mathbf{u}}_{r}\right|^{2}\right\rangle= & \left(1 / 2 m_{r}\right) \\
& \times \sum_{i}\left[\hbar \mathfrak{D}^{\frac{1}{2}}+2 \exp \left(-\hbar \mathfrak{D}^{\frac{1}{2}} / k T\right)+\cdots\right]_{r i, r i}. \quad(14)
\end{aligned}$$

For the high-temperature case the correction term proportional to 1/T is particularly easy to calculate, since the first power of the dynamical matrix is required, and the elements of the latter can be read off directly from the equations of motion. For example, one readily verifies that Eq. (13) leads to the same high-tempera- ture results as those obtained by Maradudin, Flinn, and Ruby $^{3}$ using a different method.
III. SURFACE EFFECTS
In this section we present the results of calculations on the mean-square velocities of atoms in monatomic and diatomic linear chains with harmonic nearest- neighbor interactions and free boundaries. The results for these simple models will give a qualitative indication of what may be expected for more complicated models. In the high-temperature case the diatomic chain is worked out for a general value of the mass ratio. In the low-temperature case the monatomic chain and the diatomic chain with mass ratio much different from unity are worked out separately.
Let us consider a diatomic linear chain consisting of N atoms of mass $m_{1}$ and N atoms of mass $m_{2}$ . For free ends the equations of motion can be written in the form
$$\begin{aligned}
m_{1} \ddot{u}_{2 j-1}+ & \left(1-\delta_{j 1}\right) \gamma\left(u_{2 j-1}-u_{2 j-2}\right) \\
- & {\left[\left(1-\delta_{j 1}-\delta_{j N}\right) \gamma+\delta_{j 1} \gamma^{\prime}+\delta_{j N} \gamma^{\prime \prime}\right] } \\
& \times\left(u_{2 j}-u_{2 j-1}\right)=0, \\
m_{2} \ddot{u}_{2 j}- & \left(1-\delta_{j N}\right) \gamma\left(u_{2 j+1}-u_{2 j}\right) \\
+ & {\left[\left(1-\delta_{j 1}-\delta_{j N}\right) \gamma+\delta_{j 1} \gamma^{\prime}+\delta_{j N} \gamma^{\prime \prime}\right] } \\
& \times\left(u_{2 j}-u_{2 j-1}\right)=0, \quad 1 \leq j \leq N.
\end{aligned}\qquad(15)$$

In Eqs. (14) we have taken into account the fact that the force constants $\gamma'$ and $\gamma^{\prime \prime}$ binding end atoms to neighboring interior atoms may be different from the force constant $\gamma$ binding two neighboring interior atoms. Other force constants near the ends may be different from $\gamma$ , in general, but such differences are neglected. The nonvanishing elements of the dynamical matrix
4 M. Born, Reports on Progress in Physics (The Physical Society, London, 1942), Vol. 9, p. 294.

corresponding to Eqs. (15) are given by
$$
\begin{aligned}
\mathcal{D}(2 j-1 ; & 2 j-1) \\
= & {\left[2\left(1-\delta_{j 1}\right) \gamma+\delta_{j 1} \gamma^{\prime}+\delta_{j N}\left(\gamma^{\prime \prime}-\gamma\right)\right] / m_{1}, } \\
\mathcal{D}(2 j ; & 2 j) \\
= & {\left[2\left(1-\delta_{j N}\right) \gamma+\delta_{j N} \gamma^{\prime \prime}+\delta_{j 1}\left(\gamma^{\prime}-\gamma\right)\right] / m_{2}, } \\
\mathcal{D}(2 j-1 ; & 2 j) \\
= & \mathcal{D}(2 j ; 2 j-1) \\
= & -\left[\left(1-\delta_{j 1}-\delta_{j N}\right) \gamma+\delta_{j 1} \gamma^{\prime}+\delta_{j N} \gamma^{\prime \prime}\right] /\left(m_{1} m_{2}\right)^{\frac{1}{2}}, \\
& \mathcal{D}(2 j ; 2 j+1)=-\left(1-\delta_{j N}\right) \gamma /\left(m_{1} m_{2}\right)^{\frac{1}{2}}, \\
& \mathcal{D}(2 j-1 ; 2 j-2)=-\left(1-\delta_{j 1}\right) \gamma /\left(m_{1} m_{2}\right)^{\frac{1}{2}}.
\end{aligned}
$$

### A. High-Temperature Case

For the high-temperature case direct substitution of Eqs. (16) into Eq. (13) yields
$$
\left\langle\left|\dot{u}_{r}\right|^{2}\right\rangle=P_{1}(r)+P_{2}(r)+\cdots, \quad(17)
$$
where
$$
\begin{aligned}
P_{1}(r)=\left(k T / m_{\alpha}\right), \quad m_{\alpha} & =m_{1} \quad \text { for } \quad r=2 j-1 \\
& =m_{2} \quad \text { for } \quad r=2 j,
\end{aligned}
$$

$$
P_{2}(2 j-1)=\frac{\hbar^{2}\left[2\left(1-\delta_{j 1}\right) \gamma+\delta_{j 1} \gamma^{\prime}+\delta_{j N}\left(\gamma^{\prime \prime}-\gamma\right)\right]}{12 m_{1}^{2} k T}, \quad(17 \mathrm{~b})
$$

$$
P_{2}(2 j)=\frac{\hbar^{2}\left[2\left(1-\delta_{j N}\right) \gamma+\delta_{j N} \gamma^{\prime \prime}+\delta_{j 1}\left(\gamma^{\prime}-\gamma\right)\right]}{12 m_{2}^{2} k T}. \quad(17 \mathrm{c})
$$

In the limit $T \rightarrow \infty$ one sees from Eqs. (17) that the mean-square velocity of a given kind of atom is independent of its position in the lattice. At finite temperatures, however, atoms sufficiently near the free ends have different mean square velocities from interior atoms.

Let us consider the simple case $\gamma^{\prime}=\gamma^{\prime \prime}=\gamma$. Then the values of $P_{1}(r)$ are still given by Eq. (17a), while those of $P_{2}(r)$ are
$$
P_{2}(1)=\hbar^{2} \omega_{1}^{2} / 24 m_{1} k T, \quad(18 \mathrm{a})
$$

$$
P_{2}(2 j-1)=\hbar^{2} \omega_{1}^{2} / 12 m_{1} k T, \quad 1<j \leq N, \quad(18 \mathrm{~b})
$$

$$
P_{2}(2 j)=\hbar^{2} \omega_{2}^{2} / 12 m_{2} k T, \quad 1 \leq j<N, \quad(18 \mathrm{c})
$$

$$
P_{2}(2 N)=\hbar^{2} \omega_{2}^{2} / 24 m_{2} k T, \quad(18 \mathrm{~d})
$$

![](./images/811097814875504643_1.jpg)

![](./images/811097814875504643_2.jpg)

where
$$
\omega_{1}^{2}=2 \gamma / m_{1}, \quad(18 \mathrm{e})
$$

$$
\omega_{2}^{2}=2 \gamma / m_{2}. \quad(18 \mathrm{f})
$$

Thus, if the force constants near the free ends are the same as in the interior, the mean-square velocity term proportional to $1 / T$ is one-half as large for an end atom as for interior atoms of the same mass. The series expansion in Eq. (13) converges very rapidly for $k T>\hbar \omega_{L}$, where $\omega_{L}$ is the largest normal mode frequency. Hence, we conclude that under the conditions of this paragraph, the mean-square velocity itself is smaller for an end atom than for an interior atom of the same mass. Qualitatively, the mean-square velocity of an atom increases as forces acting on that atom increase. An atom at a boundary is acted upon by fewer forces than an interior atom and consequently will have a smaller mean-square velocity, unless the force constants near the boundary are anomalously large. It appears to be very difficult to choose the force constants so that, for every mass occurring, the mean-square velocities of atoms of the same mass are identical regardless of proximity to a boundary. In Fig. 1 the correction $P_{2}(r)$ is plotted as a function of $r$ for the case $m_{1}=\frac{1}{4} m_{2}$ and $N=10$.

As indicated by Eqs. (18) the correction terms $P_{2}(r)$ are characterized by frequencies $\omega_{1}$ and $\omega_{2}$ which are the acoustical and optical mode frequencies at the Brillouin zone boundary. One may ask whether the corrections for the end atoms, $P_{2}(1)$ and $P_{2}(2 N)$, can be related to the known $^{5}$ surface mode frequency $\omega_{s}$ given by
$$
\omega_{s}^{2}=\gamma\left[\left(m_{1}+m_{2}\right) / m_{1} m_{2}\right]. \quad(19)
$$

It is clear from inspection of Eqs. (18) and (19) that such a correlation does not exist in general. However, for the limiting case $m_{1} \ll m_{2}$ the correction terms for the light atoms can be written in the form
$$
\begin{aligned}
P_{2}(1) & \simeq \hbar^{2} \omega_{s}^{2} / 12 m_{1} k T, \\
P_{2}(2 j-1) & \simeq \hbar^{2} \omega_{1}^{2} / 12 m_{1} k T, \quad 1<j \leq N.
\end{aligned}
$$

5 R. F. Wallis, Phys. Rev. 105, 540 (1957).

A corresponding relationship for the heavy atoms does not exist.

High-temperature expressions for the mean-square velocities of atoms in a monatomic lattice follow from Eqs. (17) through (20). For the case $\gamma'=\gamma''=\gamma$, the end atoms again have smaller mean-square velocities than the interior atoms. The correction $P_2(1)$ for an end atom is one-half the corresponding correction for the interior atoms. It is worthy of emphasis that the monatomic linear chain with nearest-neighbor interactions has no surface mode.⁵ Although equations similar to Eqs. (20) can be written down formally, the frequency $\omega_s$ so defined has no signficance as a surface mode frequency. In Fig. 2 the correction $P_2(r)$ is plotted as a function of $r$ for a monatomic linear chain with 20 atoms.

$$
\left\langle\left|\dot{u}_{1}\right|^{2}\right\rangle \simeq \hbar \omega_{s} / 2 m_{1}, \tag{21a}
$$

$$
\left\langle\left|\dot{u}_{2 j-1}\right|^{2}\right\rangle \simeq \hbar \omega_{1} / 2 m_{1}, \quad 1<j \leq N, \tag{21b}
$$

$$
\left\langle\left|\dot{u}_{2 j}\right|^{2}\right\rangle \simeq \frac{\hbar \omega_{2}}{8 N m_{2}}\left\{2 \cot (\pi / 4 N)-\frac{\sin (\pi / 2 N)}{\sin [(4 j-1) \pi / 4 N] \sin [(4 j-3) \pi / 4 N]}\right\}, \quad 1 \leq j \leq N. \tag{21c}
$$

From Eqs. (21) it follows that an end atom, whether light or heavy, has a smaller mean-square velocity than an interior atom of the same mass. In Fig. 3 the mean-square velocity for the $r$th atom is plotted as a function of $r$ for $m_1=m_2/4$ and $N=10$.

The monatomic linear chain with $\gamma'=\gamma''=\gamma$ and free ends can also be treated similarly in the low-temperature limit. The result for the mean square velocity of the $r$th atom in a chain of $2N$ atoms each with mass $m$ is given by

$$
\begin{aligned}
\left\langle\left|\dot{u}_{r}\right|^{2}\right\rangle= & {\left[\hbar \omega_{L} / 16 N m\right]\{\cot [(4 r-1) \pi / 8 N] } \\
& -\cot [(4 r-3) \pi / 8 N]+2 \cot (\pi / 8 N)\}, \quad(22)
\end{aligned}
$$

where
$$
\omega_{L}=(4 \gamma / m)^{1 / 2}. \tag{22a}
$$

![](./images/811097814875504643_3.jpg)

## B. Low-Temperature Case
We turn now to the low-temperature limit of absolute zero. If Eq. (14) is used, the elements of the square root of the dynamical matrix are required. Rather than attempt to calculate these elements from those of the dynamical matrix itself, we calculate the mean-square velocities from the eigenvectors of the dynamical matrix using Eq. (10) evaluated at $T=0^\circ$K. For the linear diatomic lattice with free ends and $\gamma'=\gamma''=\gamma$, the eigenvectors are available from previous work,⁵ but the summations over normal modes are rather cumbersome to work out for a general mass ratio. We, therefore, restrict ourselves to the case $m_1\ll m_2$ for which approximate expressions can be obtained without great effort. To lowest nonvanishing order in the ratio $m_1/m_2$, the results are

The mean-square velocity is plotted as a function of $r$ in Fig. 4 for a monatomic chain of 20 atoms.

It may be noted from Eqs. (21) and (22) that the difference between the mean-square velocities of end atoms and interior atoms is manifested in the dominant low-temperature term. At high temperatures, on the other hand, such differences appear in the first-order correction term but not in the dominant term.

## IV. CONCLUSION
The general theory developed in this paper exhibits the relation between the mean-square velocity of an atom in a crystal lattice and the forces which bind that atom to the other atoms. Atoms near a free surface are subject to different forces from those acting on atoms in the interior, and this leads to a corresponding difference in the mean square velocities. The second-order

![](./images/811097814875504643_4.jpg)

Doppler shift in the Mössbauer effect is proportional to the mean-square velocity of the emitting atom. Hence, measurements of this shift provide, in principle, a means of obtaining information about the forces acting on a surface atom compared to those acting on an interior atom. However, technical difficulties associated with preparing samples having the radioactive atoms localized in the surface layers must be surmounted.
R. F. WALLIS AND D. C. GAZIS
110
