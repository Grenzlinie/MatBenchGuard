# The magnetic reorientation transition in thin ferromagnetic films treated by many-body Green's function theory

P. Fröbrich$^+$, and P.J. Kuntz

Hahn-Meitner-Institut Berlin, Glienicker Straße 100, D-14109 Berlin,
Germany,

$^+$also: Institut für Theoretische Physik, Freie Universität Berlin
Arnimallee 14, D-14195 Berlin, Germany
e-mail: froebrich@hmi.de or kuntz@hmi.de

## Abstract
This contribution describes the reorientation of the magnetization
of thin ferromagnetic Heisenberg films as function of the temperature
and/or an external field. Working in a rotating frame allows an ex-
act treatment of the single-ion anisotropy when going to higher order
Green's functions. Terms due to the exchange interaction are treated
by a generalized Tyablicov (RPA) decoupling.

## 1. Introduction
New experimental results concerning the properties of thin magnetic films
have provided an incentive for theoretical investigations. This contribu-
tion deals with the reorientation of the magnetization of thin ferromagnetic
Heisenberg films as function of the temperature or an external magnetic
field. It is of particular importance to take into account collective exci-
tations (magnons), which influence the magnetic properties of films more
strongly than those of bulk magnets. Many-body Green's function theory
(GFT) is an appropriate tool to achieve this. In previous work, we investi-
gated the reorientation transition by applying GFT [1, 2], where a Tyablikov
(RPA)-decoupling of the exchange interaction terms and a Anderson-Callen
decoupling [3] of the single-ion anisotropy terms in the equation of motion for
the lowest-order GF was used. By comparing with Quantum Monte Carlo
(QMC) results [4] it was shown that this leads to rather good results for
small anisotropies ($K_2 \leq 0.1J$) when the magnetic field is in the direction
of the anisotropy but the approximation is not as good when the field is ap-
plied perpendicular to the anisotropy. A considerable simplification and an

improvement of the results concerning the reorientation is reported in Ref.[5], where the Anderson-Callen decoupling is made in a frame which is rotated with respect to the original one and in which the magnetization is in the direction of the new z-axis. The reorientation angle is determined from the condition that the magnetization commutes with the Hamiltonian in the rotated frame. In this connection see also Ref.[6], who also apply the approximate Anderson-Callen decoupling in a rotated frame. We realized in Ref.[7], generalizing findings of Ref.[8], that when introducing higher-order GF's a decoupling of the anisotropy terms is not necessary. By taking advantage of relations between products of spin operators [9], this leads to an automatic closure of the hierarchy of equations of motion with respect to the anisotropy terms. This procedure gives improved results (as compared to the approximate Anderson-Callen treatment) when applying a field in the direction of the anisotropy, which now can be large [7], but there are difficulties (there were zeroes in the equation of motion matrix requiring a special treatment [10, 11], and numerical instabilities occurred) when trying to calculate the reorientation induced by a field perpendicular to the anisotropy. The new result of the present paper is that these difficulties can be overcome when working in a rotated frame, in analogy to Ref.[5]. In this way, we are able to describe the field-induced spin reorientation transition for spin $S \geq 1$ with an exact treatment of the single-ion anisotropy. The exchange interaction terms are still decoupled with generalized RPA.

## 2. The Green's function formalism
We investigate a spin Hamiltonian consisting of an isotropic Heisenberg exchange interaction between nearest neighbour lattice sites with strength $J_{kl}$, a second-order single-ion lattice anisotropy with strength $K_{2,k}$ vertical to the film $(x-y)$-plane and an external magnetic field $\mathbf{B}=(B_0^x,0,B_0^z)$:

$$
\mathcal{H}=-\frac{1}{2} \sum_{<kl>} J_{kl}\left(S_k^-S_l^+ + S_k^zS_l^z\right)-\sum_{k} K_{2,k}\left(S_k^z\right)^2-\sum_{k}\left(B_0^x S_k^x+B_0^z S_k^z\right). \tag{1}
$$

In this paper, we restrict ourselves to this Hamiltonian; we dealt with the dipole-dipole interaction in Ref.[2] and with exchange anisotropies in Ref.[12].

Owing to the external $B_0^x$-field, the magnetization vector, initially in the z-direction, will rotate by an angle $\theta$ in the $x-z$-plane, pointing now in the $z'$-direction of a new frame $(x',y',z')$. As in Ref.[5], we shall do the


calculations in the primed system, in which the magnetization vector has the components $(0,0,\langle S^z\ '\rangle)$. The transformation between the frames is

$$
\left(\begin{array}{c}
\left\langle S^{x}\right\rangle \\
\left\langle S^{y}\right\rangle \\
\left\langle S^{z}\right\rangle
\end{array}\right)=\left(\begin{array}{ccc}
\cos \theta & 0 & \sin \theta \\
0 & 1 & 0 \\
-\sin \theta & 0 & \cos \theta
\end{array}\right)\left(\begin{array}{c}
\left\langle S^{x}{ }^{\prime}\right\rangle \\
\left\langle S^{y}{ }^{\prime}\right\rangle \\
\left\langle S^{z}{ }^{\prime}\right\rangle
\end{array}\right).\qquad(2)
$$

Because $\langle S^x\ '\rangle=\langle S^y\ '\rangle=0$ in the rotated frame, one needs only to calculate $\langle S^z\ '\rangle$ in order to find the components of the magnetization in the original frame provided the angle $\theta$ is known.

After transforming the Hamiltonian (1) to the primed system the following Green's functions are needed

$$
\begin{aligned}
G_{i j}^{+,-} & =\left\langle\left\langle S_{i}^{+}{ }^{\prime} ; S_{j}^{-}{ }^{\prime}\right\rangle\right\rangle, \\
G_{i j}^{(z)^{n+,-}} & =\left\langle\left\langle\left(S_{i}^{z}{ }^{\prime}\right)^{n-1}\left(2 S_{i}^{z}{ }^{\prime}-1\right) S_{i}^{+}{ }^{\prime} ; S_{j}^{-}{ }^{\prime}\right\rangle\right\rangle.
\end{aligned}\qquad(3)
$$

The single-ion anisotropy is active for spins $S \geq 1$, and one needs the first Green's function plus those for $n=1,2,3, \ldots$ to treat films with $S=1,3 / 2,2, \ldots$

In establishing the equations of motion, the exchange interaction terms are treated by a generalized Tyablikov (RPA)-decoupling, in which we do not break products of spin operators with equal indices

$$
\left\langle\left\langle\left(S_{i}^{z}{ }^{\prime}\right)^{n} S_{k}^{+}{ }^{\prime} ; S_{j}^{-}{ }^{\prime}\right\rangle\right\rangle \simeq\left\langle\left(S_{i}^{z}{ }^{\prime}\right)^{n}\right\rangle\left\langle\left\langle S_{k}^{+}{ }^{\prime} ; S_{j}^{-}{ }^{\prime}\right\rangle\right\rangle+\left\langle S_{k}^{+}{ }^{\prime}\right\rangle\left\langle\left\langle\left(S_{i}^{z}{ }^{\prime}\right)^{n} ; S_{j}^{-}{ }^{\prime}\right\rangle\right\rangle. \text { (4) }
$$

Note that in the rotated system, $\langle S_{k}^{+}\rangle=0$; i.e. the second term vanishes. After applying the decoupling procedure and performing a Fourier transform to momentum space one obtains the following set of equations of motion.

$$
\begin{aligned}
\omega G^{+,-} & =2\left\langle S^{z}{ }^{\prime}\right\rangle+\left\langle S^{z}{ }^{\prime}\right\rangle J\left(q-\gamma_{\mathbf{k}}\right) G^{+,-} \\
+ & \left(B_{0}^{x} \sin \theta+B_{0}^{z} \cos \theta\right) G^{+,-}+K_{2}\left(1-\frac{3}{2} \sin ^{2} \theta\right) G^{z+,-}, \\
\omega G^{z+,-} & =\left(6\left\langle\left(S^{z}{ }^{\prime}\right)^{2}\right\rangle-2 S(S+1)\right)-\frac{1}{2} J \gamma_{\mathbf{k}}\left(6\left\langle\left(S^{z}{ }^{\prime}\right)^{2}\right\rangle-2 S(S+1)\right) G^{+,-} \\
+ & J q\left\langle S^{z}{ }^{\prime}\right\rangle G^{z+,-}+\left(B_{0}^{x} \sin \theta+B_{0}^{z} \cos \theta\right) G^{z+,-} \\
+ & K_{2}\left(1-\frac{3}{2} \sin ^{2} \theta\right)\left(2 G^{(z)^{2}+,-}-G^{z+,-}\right), \\
\omega G^{(z)^{2}+,-} & =8\left\langle\left(S^{z}{ }^{\prime}\right)^{3}\right\rangle+3\left\langle\left(S^{z}{ }^{\prime}\right)^{2}\right\rangle-(4 S(S+1)-1)\left\langle S^{z}{ }^{\prime}\right\rangle-S(S+1) \\
+ & J \gamma_{\mathbf{k}}\left(\frac{1}{2} S(S+1)+(2 S(S+1)-1)\left\langle S^{z}{ }^{\prime}\right\rangle-\frac{3}{2}\left\langle\left(S^{z}{ }^{\prime}\right)^{2}\right\rangle-4\left\langle\left(S^{z}{ }^{\prime}\right)^{3}\right) G^{+,-}\right. \\
+ & J q\left\langle S^{z}{ }^{\prime}\right\rangle G^{(z)^{2}+,-}+\left(B_{0}^{x} \sin \theta+B_{0}^{z} \cos \theta\right) G^{(z)^{2}+,-}
\end{aligned}
$$


$$+K_{2}\left(1-\frac{3}{2} \sin ^{2} \theta\right)\left(2 G^{(z)^{3+,-}}-G^{(z)^{2+,-}}\right) ;$$

$$
\begin{aligned}
& \omega G^{(z)^{3+,-}}=10\left\langle\left(S^{z}{ }^{\prime}\right)^{4}\right\rangle+8\left\langle\left(S^{z}{ }^{\prime}\right)^{3}\right\rangle-(6 S(S+1)-5)\left\langle\left(S^{z}{ }^{\prime}\right)^{2}\right\rangle \\
& -(4 S(S+1)-1)\left\langle S^{z}{ }^{\prime}\right\rangle-S(S+1) \\
& +J \gamma_{\mathbf{k}}\left(\frac{1}{2} S(S+1)+\left(2 S(S+1)-\frac{1}{2}\right)\left\langle S^{z}{ }^{\prime}\right\rangle+\left(3 S(S+1)-\frac{5}{2}\right)\left\langle\left(S^{z}{ }^{\prime}\right)^{2}\right\rangle\right. \\
& \left.-4\left\langle\left(S^{z}{ }^{\prime}\right)^{3}\right\rangle-5\left\langle\left(S^{z}{ }^{\prime}\right)^{4}\right\rangle\right) G^{+,-} \\
& +J q\left\langle S^{z}{ }^{\prime}\right\rangle G^{(z)^{3+,-}}+\left(B_{0}^{x} \sin \theta+B_{0}^{z} \cos \theta\right) G^{(z)^{3+,-}} \\
& +K_{2}\left(1-\frac{3}{2} \sin ^{2} \theta\right)\left(2 G^{(z)^{4+,-}}-G^{(z)^{3+,-}}\right).
\end{aligned}
$$

For a square lattice with lattice contant $a=1$, the quantity $\gamma_{\mathbf{k}}=2(\cos k_{x}+$ $\cos k_{y}$ ), and $q=4$, the number of nearest neighbours.

As Ref.[5] we neglect all GF's not containing an equal number of $S^{-}$ ' and $S^{+}$ ' operators.

One observes that in the equations (5) the anisotropy terms do not yet lead to a closed system. This is, however, achieved by using formulas derived in Ref.[9], which reduce products of spin operators by one order (!). One obtains

$$
\begin{aligned}
\text { for } \mathrm{S}=1: \quad G^{(z)^{2+,-}} & =\frac{1}{2}\left(G^{z+,-}+G^{+,-}\right), \\
\text {for } \mathrm{S}=3 / 2: \quad G^{(z)^{3+,-}} & =G^{(z)^{2+,-}}+\frac{3}{4} G^{z+,-}, \\
\text {for } \mathrm{S}=2: \quad G^{(z)^{4+,-}} & =\frac{3}{2} G^{(z)^{3+,-}}+\frac{7}{4} G^{(z)^{2+,-}} \\
& -\frac{9}{8} G^{z+,-}-\frac{9}{8} G^{+,-}.
\end{aligned}
$$

When inserting these relations into the system of equations (5) one sees that the resulting system of equations is closed.

The equations of motion can be written in compact matrix notation

$$
(\omega \mathbf{1}-\boldsymbol{\Gamma}) \mathbf{G}=\mathbf{A} .
$$

The quantities $\boldsymbol{\Gamma}, \mathbf{G}$, and $\mathbf{A}$ can be read off from equation (5), where the non-symmetric matrix $\boldsymbol{\Gamma}$ is a $(2 \times 2),(3 \times 3),(4 \times 4)$-matrix for spins $S=1,3 / 2,2$, respectively. The desired correlation vector corresponding to the Green's functions (3),

$$
\mathbf{C}=\left(\begin{array}{c}
\left\langle S^{-}{ }^{\prime} S^{+}{ }^{\prime}\right\rangle \\
\left\langle S^{-}{ }^{\prime} S^{\left(z^{\prime}\right)^{n-1}}\left(2 S^{z}{ }^{\prime}-1\right) S^{+}{ }^{\prime}\right\rangle
\end{array}\right),
$$

is obtained via the spectral theorem. Using the eigenvector method of Ref.[2],
one has for the components of the correlation vector $\mathbf{C}$ after a Fourier trans-
form to configuration space

$$
\begin{aligned}
C_{i} & =\int d \mathbf{k} C_{i}(\mathbf{k})=\frac{1}{\pi^{2}} \int_{0}^{\pi} d k_{x} \int_{0}^{\pi} d k_{y} \sum_{j, k, l=1}^{2 S} R_{i j} \epsilon_{j k} L_{k l} A_{l} \\
& \quad(i=1,2,.., 2 S),
\end{aligned}\qquad(9)
$$

where the integration is over the first Brillouin zone, and $\mathbf{R}(\mathbf{L})$ are matrices
whose columns (rows) consist of the right (left) eigenvectors of the matrix $\boldsymbol{\Gamma}$,
and $\epsilon_{j k}=\delta_{j k} /(e^{\beta \omega_{j}}-1)$ is a diagonal matrix, in which $\omega_{j}$ are the eigenvalues
$(j=1,.., 2 S)$ of the $\boldsymbol{\Gamma}$-matrix.

It remains to derive an equation which determines the rotation angle.
This is again done by using the approximation that the commutator of the
magnetization with the Hamiltonian vanishes in the rotated system. This
implies that the following Green's function is zero

$$
\left\langle\left\langle\left[S_{i}^{z}{ }^{\prime}, H^{\prime}\right] ; S_{j}^{-}{ }^{\prime}\right\rangle\right\rangle=0.\qquad(10)
$$

Evaluating the commutator, one obtains

$$
\left(B_{0}^{x} \cos \theta-B_{0}^{z} \sin \theta\right) G_{i j}^{+-}-K_{2} \sin \theta \cos \theta G_{i j}^{z+,-}=0.\qquad(11)
$$

After applying the spectral theorem to this equation one obtains for the
diagonal correlations the relation which determines the reorientation angle
angle:

$$
\left(B_{0}^{x} \cos \theta-B_{0}^{z} \sin \theta\right) C^{-+}-K_{2} \sin \theta \cos \theta C^{-z+}=0.\qquad(12)
$$

This is the generalization of the angle condition of Refs. [5, 6], when treating
the single-ion anisotropy exactly instead of applying the Anderson-Callen
decoupling. Equation (12) together with the set of integral equations (9)
have to be solved self-consistently in order to obtain the magnetization $\langle S^{z}^{\prime}\rangle$
and its moments in the rotated system together with the reorientation angle
$\theta$. Applying the relations (2) yields the components of the magnetizations in
the original system in which the magnetic reorientation is measured.

## 3. Results

We solve the equations of the last section with the curve following method de-
scribed in detail in an appendix of Ref. [7]. In Ref. [5], where the Anderson-
Callen decoupling was used in the rotated frame, only cases with weak single-
ion anisotropy were considered. An example was the case of spin $S=2$ and

$K_2=0.01J$, which is a rather small anisotropy as appearing for 3d transition metals. A very good agreement with QMC calculations of Ref. [4] was obtained. Because the anisotropy is small the result with the present theory is practically indistinguishable, whereas the results of Ref.[1] are rather bad for the reorientation, because the decoupling was not done in the rotated frame. For anisotropies in the rare earth region, which can be of the order

![](./images/867770036360577529_1.jpg)

Figure 1: Normalized magnetizations $\langle S^z \rangle/S$ and $\langle S^x \rangle/S$ and the reorientation angle $\Theta$ for a spin S=2 Heisenberg monolayer as function of the external field are shown: QMC [4](solid circles), Anderson-Callen decoupling [5](triangles), present theory (open circles).

of the exchange interaction, the approximate theory of Ref. [5] should break down, and one expects the present theory to be superior. Surprisingly, the Anderson-Callen decoupling in the rotated frame still yields excellent results, when compared with the present theory and QMC results from Ref. [4] for anisotropies up to $K_2 \leq 0.2J$. This can be seen in Fig. 1 for the magnetic reorientation induced by the transversal $B^x$-field for the case of $K_2=0.2J$ and $T=100$. The result of both Green's function theories are nearly identical to each other and deviate only slightly from the exact( within the statistical

error) Quantum Monte Carlo results.

Reorientation: K₂=50 T=490 J=1 00 S=2
Anderson-Callen versus exact: K₂(<Sᶻ>)²

![](./images/867770036360577529_2.jpg)

Figure 2: Normalized magnetizations $\langle S^z \rangle/S$ and $\langle S^x \rangle/S$ and the reorientation angle $\Theta/(\pi/2)$ for a spin S=2 Heisenberg monolayer as function of a transversal field $B^x$ are shown: Anderson-Callen decoupling [5](dotted lines) and the present theory (solid lines) for $K_2=0.5J$ ($T/J=4.9$).

The reason that the magnetization curves as function of the external field of both theories are very close for T=100 is that with the present choice of the parameters the magnetizations at this temperature are still very close to each other. Both theories deviate from each other with increasing temperature, until close to the reorientation temperature the deviation is maximal. Therefore one should observe deviations between the theories in this temperature range. The differences should also increase with increasing anisotropy strength $K_2$. Therefore we have calculated the field-induced reorientation for a temperature somewhat below the reorientation temperature and for a large anisotropy $K_2=0.5J$ ($T/J=4.9$), for a Heisenberg monolayer with spin $S=2$. The result is shown in Fig. 2. In this case the

Anderson-Callen (A.C.) decoupling along the lines of [5] leads to a discontinuous transition from a certain angle $(\theta/(\pi/2) \approx 0.6)$ to full reorientation $(\theta/(\pi/2)=1)$. whereas the reorientation transition is continuous when the single-ion anisotropy is treated exactly. Such discrete transitions are also reported in Ref. [6] in a treatment which is very similar to that of Ref. [5]. The reason why this is not observed in the last reference is that there only very small anisotropies were considered. We attribute the discontinuous transition to the approximate Anderson-Callen decoupling, which is not justified when going to large anisotropies. The difference between the corresponding reorientation fields, $B_R$, increases with increasing anisotropy. For the present case it is: $B_R^{\mathrm{present}} - B_R^{\mathrm{A.C.}} \simeq 11$ (for $\mathrm{K_2}=0.5\mathrm{J}$).

Unfortunately, we cannot say how accurate the present model is because we have no QMC calculations available for large anisotropies. The most uncontrolled approximation consists in the generalised RPA decoupling of the exchange interaction terms of the higher-order GF, eqn.(4) . Previous calculations [13] have shown (by comparing with QMC) that RPA is a good approximation for a Heisenberg model (no anisotropy) with a field perpendicular to the film plane. For improving the the present approach for a field in transversal direction one may try to extend the present theory by applying the procedure of [14] which goes beyond the RPA with respect to the exchange interaction terms. It is possible by applying formulas from Ref.[9] to treat also the fourth-order anisotropy term, $-\sum_i K_{4,i}(S_i^z)^4$, exactly. Work in this direction is in progress, as well as the generalization to multilayers. We mention that the reorientation of the magnetization of a ferromagnetic film induced by the coupling to an antiferromagnetic film can also be treated with the GF formalism [15].

## References

[1] Fröbrich P, Jensen P J and Kuntz P J 2000 *Eur. Phys. J. B* **13** 477

[2] Fröbrich P, Jensen P J, Kuntz P J and Ecker A 2000 *Eur. Phys. J. B* **18** 579

[3] Anderson F B and Callen H B 1964 *Phys. Rev.* **136** A1068

[4] Henelius P, Fröbrich P, Kuntz P J, Timm C and Jensen P J 2002 *Phys. Rev. B* **66** 094407


[5] Schwieger S, Kienert J and Nolting W, 2005 *Phys. Rev.* B **71** 024428

[6] Pini M G, Politi P and Stamps R L 2005 *Phys. Rev.* B **72** 014454

[7] Fröbrich P, Kuntz P J and Saber M 2002 *Ann. Phys. (Leipzig)* **11** 387

[8] Devlin J F 1971 *Phys. Rev.* B **4** 136

[9] Jensen P J and Aguilera-Granja F 2000 *Phys. Lett.* A **269** 158

[10] Fröbrich P and Kuntz P J 2003 *Phys. Rev.* B **68** 014410

[11] Fröbrich P and Kuntz P J 2005 *J. Phys.: Condens. Matter* **17** 1167

[12] Fröbrich P and Kuntz P J 2003 *Eur. Phys. Journ.* B **32** 445

[13] Ecker A, Fröbrich P, Jensen P J and Kuntz P J 1999 *J. Phys.: Condens.
    Matter* **11** 1557

[14] Junger I, Ihle D, Richter J and Klümper A 2004 *Phys. Rev.* B **70** 104419

[15] Fröbrich P, Kuntz P J and Jensen P J 2005 *J. Phys.: Condens. Matter*
    **17** 5069