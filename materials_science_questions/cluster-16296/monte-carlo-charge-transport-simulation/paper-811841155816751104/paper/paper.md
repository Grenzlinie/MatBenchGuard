# Critical exponents in localisation theory

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1986 J. Phys. C: Solid State Phys. 19 3855

(http://iopscience.iop.org/0022-3719/19/20/019)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 155.69.4.4
This content was downloaded on 20/08/2015 at 18:17

Please note that terms and conditions apply.

J. Phys. C: Solid State Phys. 19 (1986) 3855-3862. Printed in Great Britain

# Critical exponents in localisation theory

J B Pendry
The Blackett Laboratory, Imperial College of Science and Technology, London SW7 2BZ,
UK

Received 20 January 1986

Abstract. Scaling theories of localisation in disordered materials predict that the conductance and localisation lengths respectively vary as $|E-E_{c}|$ above and below the mobility edge. On the other hand some experiments have observed conductances varying as $|E-E_{c}|^{1 / 2}$. In this paper it is shown that for systems having highly anisotropic effective mass tensors, localisation occurs for small values of disorder, which enables an analytic theory to be developed. This anisotropic theory gives an exponent of 1/2. The theory is applicable to n-type silicon provided that inter-valley scattering can be neglected, a result which accords with recent observations. The theory also shows in a natural way how the 1D and 2D limits of localisation theory can be taken by increasing the effective mass in one or two directions. The well known result that all states are localised in 2D is reproduced and can be ascribed to underlying symmetries in the system.

## 1. Introduction

The application of the ideas of scaling theory to transport in disordered systems has given two remarkable predictions: that in 1D and 2D all states are localised; and that in 3D there is a transition from localised to delocalised behaviour with the localisation length varying near the transition with critical exponent 1 (Edwards and Thouless 1972, Abrahams *et al* 1979, Wegner 1979, Apel and Rice 1983). For example as a function of the disorder parameter, $\delta^{2}$:

$$
\eta^{-1}=\left(\delta^{2}-\delta_{\mathrm{c}}^{2}\right) \tag{1}
$$

with the conductance necessarily having the same exponent on the other side of the transition. For our purposes it will be simpler to work in terms of the localisation length with the understanding that all results for $\eta^{-1}$ also hold for the conductance.

These elegantly derived results have so far had a mixed interaction with experiment. Computer simulations do not appear to confirm the exponent of 1, but show instead an exponent of 3/2 (MacKinnon and Kramer 1983). In contrast, recent experimental results on doped semiconductors agree with the scaling theory in some cases, but in others an exponent of 1/2 fits the experiments (Thomas 1985). There has been a suggestion that an exponent of 1/2 indicates a two-parameter scaling theory in some materials, because of the influence of magnetic effects (Anderson 1985). In this paper I show that there is an alternative explanation.

The key to the new theory is that in systems that are very anisotropic, i.e. tending towards the 1D or 2D limits, localisation occurs for relatively small values of disorder,

0022-3719/86/203855 + 08 $02.50 © 1986 The Institute of Physics

which allows us to make appoximations leading to an analytical solution for the critical exponent of 1/2. The analytic solution is not valid in the case of an isotropic effective mass and I speculate that in this instance higher-order terms enter my expansion and the slope with which $\eta^{-1}$ tends to zero is no longer infinity, as for the exponent of 1/2, but is finite. Experiments would need to have very high precision to distinguish a critical exponent of one-half from one of unity but with a very steep slope at the critical point. It is significant that an exponent of 1/2 has been seen in phosphorus-doped silicon, which has a highly anisotropic effective mass tensor, whereas GaAs samples show an exponent of 1 and have an isotropic effective mass.

To address this problem we need to find a theory that goes beyond scaling so as not to be confined to the immediate vicinity of the mobility edge. Such a theory is available (Pendry 1982a, 1984), based on transfer matrix techniques, and is ideally suited to our purposes. The theory specifically addresses the question of anisotropy, which is a simplifying ingredient enabling analytic expressions to be obtained for the mobility edge and the localisation length.

## 2. Transfer matrix theory

The central ingredient of the model is a cubic lattice of atoms with one orbital per site, described by a tight-binding Hamiltonian:

$$
\left(E-E_{n r}\right) a_{n r}-V_{x}\left(a_{n r+x}+a_{n r-x}\right)-V_{y}\left(a_{n r+y}+a_{n r-y}\right)-V_{z}\left(a_{n+1 r}+a_{n-1 r}\right)=0.
\tag{2}
$$

The lattice has been divided into planes of atoms perpendicular to the direction of transport (the $+z$ axis), labelled by $n$. Within each plane the atoms are labelled by the 2D vector, $\boldsymbol{r}$, with the vectors $\boldsymbol{x}$, and $\boldsymbol{y}$, forming the sides of the unit 2D cell. By dividing through by $V_{z}$ and rearranging, it is possible to express the amplitudes on the $(n+1)$ th plane in terms of the amplitudes on the two previous planes, the $n$th and $(n-1)$ th. This relationship defines the transfer matrix. The parameters in the matrix are

$$
\begin{aligned}
& \beta_{x}=V_{x} / V_{z}=m_{z}^{*} / m_{x}^{*} \quad \beta_{y}=V_{y} / V_{z}=m_{z}^{*} / m_{y}^{*} \\
& D_{n r}=\left(E-E_{n r}\right) / V_{z}.
\end{aligned}
\tag{3}
$$

Disorder is introduced into the problem through a distribution of site energies, $D_{n r}$, defined by

$$
\delta^{2}=\left\langle D_{n r}^{2}\right\rangle-\left\langle D_{n r}\right\rangle^{2}.
\tag{4}
$$

Omitting the subscripts $\boldsymbol{r}$, the transfer matrix equations become

$$
\left[\begin{array}{l}
a_{n+1} \\
a_{n}
\end{array}\right]=\mathbf{M}_{n}\left[\begin{array}{l}
a_{n} \\
a_{n-1}
\end{array}\right].
\tag{5}
$$

The transfer matrix has the property that

$$
\left[\begin{array}{l}
a_{L+1} \\
a_{L}
\end{array}\right]=\prod_{n=1}^{L} \mathbf{M}_{n}\left[\begin{array}{l}
a_{1} \\
a_{0}
\end{array}\right].
\tag{6}
$$

Imagine an infinite lattice which is everywhere ordered with
$$D_{nr} = \Gamma \tag{7}$$
for all $n$ and $r$, except between the planes $n = 0$ and $n = L$. A wavepacket coming from $n = -\infty$ is incident on the disordered region, and is partly reflected and partly transmitted. If the transmission and reflection of Bloch waves through the disordered region is described by matrices $\mathbf{T}$ and $\mathbf{R}$, it can easily be shown that
$$\operatorname{ave}\left[\begin{array}{c|c}
\mathbf{T}^{-1} & \mathbf{T}^{-1} \mathbf{R} \\
\hline\left(\mathbf{T}^{-1} \mathbf{R}\right)^{+} & \left(\mathbf{T}^{-1}\right)^{+}
\end{array}\right]=\prod_{n=1}^{L} \operatorname{ave} \tilde{\mathbf{M}}_{n} \tag{8}$$
where $\tilde{\mathbf{M}}_{n}$ is simply the transfer matrix expressed in a Bloch wave representation.
Formulations in terms of transfer matrices have been much used in 1D, see Pendry (1982b), Kirkman and Pendry (1984a, b) for further references, and have also been applied to 3D (Stephen 1981, Pendry 1982a, 1984). The important point is that using (8) we can average, not only $\mathbf{T}^{-1}$, but also any positive integer power thereof. In particular the quantity
$$\operatorname{tr}\left(\mathbf{T} \mathbf{T}^{+}\right)^{-N} \tag{9}$$
can be expressed in terms of a $2N$th-order direct product of the $\mathbf{M}$s
$$\operatorname{ave} \operatorname{tr}\left(\mathbf{T} \mathbf{T}^{+}\right)^{-N}=\left\langle N\left|\left(\mathbf{X}_{N}\right)^{L}\right| N\right\rangle \tag{10}$$
where
$$\mathbf{X}_{N}=\operatorname{ave}\{\mathbf{M} \otimes \mathbf{M} \otimes \mathbf{M} \otimes \ldots(2 N \text { terms })\} \tag{11}$$
and the vector $|N\rangle$ is chosen to select the required elements in the direct product.

The approach is then to express (10) as an analytic function of $N$ and set $N=-1$ to obtain the conductance,
$$G(L)=\left(2 e^{2} / h\right) \operatorname{ave} \operatorname{tr}\left(\mathbf{T} \mathbf{T}^{+}\right)^{+1}. \tag{12}$$

Arguments about the precise formula which relates the transmission coefficient to the conductance do not affect conclusions about the exponents.

The next step is to recognise that by making either or both of $m_{x}, m_{y}$ very large the system is forced towards the 2D or 1D limit and, because all systems are localised in 1D and 2D, even a small value of $\delta^{2}$ will localise the states. I exploit this fact to retain only terms of order $\delta^{2}$ in an expansion of (10). I identify the crucial terms as those due to pairwise averaging of the $\mathbf{M}$'s in (11), with the pairs chosen so that the first $\mathbf{M}$ is paired with the $N$th, the second with the $(N+1)$ th $\ldots$ and the $(N-1)$ th with the $2 N$th. These can be shown to be the important terms, but the argument is complex and has been given in a previous paper (Pendry 1984). A more rigorous derivation of the result will be given in a subsequent paper. This approximation enables the eigenvalues of $\mathbf{X}_{N}$ to be written as products of the eigenvalues of
$$\mathbf{X}_{N=1}=\langle 1|\operatorname{ave} \mathbf{M} \otimes \mathbf{M}| 1\rangle. \tag{13}$$

Since the averaged system is translationally invariant, these pair eigenvalues are char- acterised by a momentum of the pair parallel to the planes, $q$. One crucial condition emerges from the theory: only for $N=3,5,7$ etc do we find a contribution to the conductance.

Only one of the many eigenvalues of the pair spectrum is of importance; let us label it $\mu_{q}$, so that the relevant eigenvalues of, for example, $\mathbf{X}_{3}$ are given by
$$
\mu_{3}=\mu_{q} \mu_{q^{\prime}} \mu_{q^{\prime \prime}} \tag{14}
$$
for all possible values of the $q$ s such that
$$
q+q^{\prime}+q^{\prime \prime}=0. \tag{15}
$$

The last condition comes about because we are dealing with an averaged matrix for which total crystal momentum is conserved. This latter condition, taken with the existence of only odd-order contributions, leads to the result that all states are localised in 2D. Following the earlier paper (Pendry 1984) the conductance can be written
$$
G(L) \approx\left(\sum_{q_{1}, q_{2}, q_{3} \ldots} b\left(q, q^{\prime}, q^{\prime \prime} \ldots N \text { terms) } \mu_{q}^{L} \mu_{q^{\prime}}^{L} \mu_{q^{\prime \prime}}^{L} \ldots N \text { terms }\right)_{\substack{(\text { odd } N) \\ N=-1}}\right.
$$

The pair spectrum can easily be found from the expression:
$$
\delta^{-2}=F_{q}(\mu). \tag{17}
$$
where
$$
F_{q}(\mu)=\sum_{k_{x}=1}^{L_{x}} \sum_{k_{y}=1}^{L_{y}} \frac{L_{x}^{-1} L_{y}^{-1} \mu\left(\mu^{2}-1\right)}{\left(\mu-\mu_{k q++}\right)\left(\mu-\mu_{k q+-}\right)\left(\mu-\mu_{k q-+}\right)\left(\mu-\mu_{k q--}\right)}. \tag{18}
$$
$L_{x}, L_{y}$ , are the number of unit cells in the planes in the $x$ and $y$ directions, and
$$
\mu_{k q a b}=\exp \left(\mathrm{i} a K_{k}+\mathrm{i} b K_{-k+q}\right) \tag{19}
$$
$$
\exp \left(\mathrm{i} K_{k}\right)=0.5\left(\Gamma_{k}+\mathrm{i}\left(-\Gamma_{k}^{2}+4\right)^{1 / 2}\right) \tag{20}
$$
$$
\Gamma_{k}=\Gamma-2 \beta_{x} \cos (2 \pi k \cdot x / L)-2 \beta_{y} \cos (2 \pi k \cdot y / L). \tag{21}
$$

### 3. Critical exponents
Localisation occurs if all the $\mu_{q}$ s are greater than unity (they are required to be real and greater than or equal to unity by other constraints). Then the length dependence of
$$
\operatorname{ave} \operatorname{tr}\left(\boldsymbol{\Pi} \boldsymbol{\Pi}^{+}\right)^{-N} \tag{22}
$$
is of the form
$$
\left(\mu_{\min }\right)^{N L}. \tag{23}
$$

Analytic continuation gives an inverse localisation length
$$
\eta^{-1}=\ln \left(\mu_{\min }\right). \tag{24}
$$

For small values of $\delta^{2}, \mu_{q}$ attains the value unity on a critical contour in the 2D space of $q$; beyond this contour $\mu_{q}$ does not exist. This sharp cut-off in the spectrum gives terms proportional to $L^{-1}$ and hence a conventional diffusive conductance.

First we take the case of $m_{x}^{*}=m_{y}^{*} \gg m_{z}^{*}$. To find whether the system is delocalised we plot $F_{q}(\mu=1)$ in figure 1 for the case
$$
m_{x}^{*} / m_{z}^{*}=m_{y}^{*} / m_{z}^{*}=4.0. \tag{25}
$$

![](./images/811841155816751104_1.jpg)

Figure 1. $F_{\boldsymbol{q}}(\mu=1)$ for $m_{x}^{*} / m_{z}^{*}=m_{y}^{*} / m_{z}^{*}=4$. Note the minima at the Brillouin zone boundaries. If $1 / \delta^{2}$ intersects this function at three values of $\boldsymbol{q}$ such that $\boldsymbol{q}_{1}+\boldsymbol{q}_{2}+\boldsymbol{q}_{3}=0$, then delocalisation results. Three typical $\boldsymbol{q}$-vectors are shown.

Note that $F_{\boldsymbol{q}}$ shows the reciprocal lattice symmetry and it is only necessary to plot inside the first Brillouin zone. For small disorder $1 / \delta^{2}$ intersects $F$ near the origin and there are delocalised solutions, $\mu=1$. As the disorder increases, $1 / \delta^{2}$ decreases, the contour of $F$ intersected is driven towards the zone boundary, where $F$ is a minimum at $\boldsymbol{q}=(L / 2,0)$ and the three other degenerate points. For values of $1 / \delta^{2}$ less than this minimum value of $F$, no $\mu=1$ solutions exist and localisation sets in. The value of $F$ near the minimum at $\boldsymbol{q}=(L / 2,0)$ is approximately

$$
F_{\min } \approx \frac{1}{4 \sin \left(K_{0}\right)} \frac{m_{x}^{*}}{m_{z}^{*}}\left(1-\frac{m_{x^{* 2}}}{m_{z^{* 2}}} \frac{(\mu-1)^{2} \sin ^{2}\left(K_{0}\right)}{8}+\frac{\pi^{2}}{4 L^{2}}\left[q_{y}^{2}+2\left(q_{x}-L / 2\right)^{2}\right]\right) \quad(26)
$$

where
$$
\sin ^{2}\left(K_{0}\right)=\left(4-\Gamma^{2}\right) / 4. \quad(27)
$$

The point I make here is that as $m_{x}^{*}$ is made larger the minimum of $F$ is increased. In the limit of $m_{x}^{*} \rightarrow \infty$ the system comprises a set of independent 1D chains, and whatever the value of $1 / \delta^{2}$ a value of $m_{x}^{*}$ can be found which localises the system. Thus it is possible to choose $1 / \delta^{2}$ sufficiently large compared to $m_{z}^{*}$ to ensure the validity of our expansion, and yet small compared to $m_{x}^{*}$ so that localisation can be observed.

When the system is just localised we can use (26) to find the minimum value of $\mu$:
$$
\mu_{\min }=1+\left[4 m_{z}^{*} /\left(\delta \sin \left(K_{0}\right) m_{x}^{*} \sqrt{ } 2\right)\right]\left(\delta^{2}-\delta_{\mathrm{c}}^{2}\right)^{1 / 2} \quad(28)
$$

where
$$
\delta_{\mathrm{c}}^{2}=4 \sin \left(K_{0}\right) m_{z}^{*} / m_{x}^{*}. \quad(29)
$$

Clearly we have a critical exponent of $1 / 2$.

![](./images/811841155816751104_2.jpg)

Figure 2. $F_{\boldsymbol{q}}(\mu=1)$ for $m_{x}^{*} / m_{z}^{*}=5 m_{y}^{*} / m_{z}^{*}=10$. The minima at the Brillouin zone boundaries are now non-degenerate between $q_{x}$ and $q_{y}$. If $1 / \delta^{2}$ intersects this function at three values of $\boldsymbol{q}$ such that $\boldsymbol{q}_{1}+\boldsymbol{q}_{2}+\boldsymbol{q}_{3}=0$, then delocalisation results. Note that this necessarily excludes all those contours far from the $q_{y}$ axis. Three typical $\boldsymbol{q}$-vectors are shown.

The case of $m_{y}^{*} \gg m_{y}^{*}$ is more complicated. Figure 2 shows $F_{\boldsymbol{q}}(\mu=1)$ for the case
$$
m_{z}^{*} / m_{x}^{*}=0.2 \quad m_{z}^{*} / m_{y}^{*}=0.1. \quad(30)
$$

The structure is now asymmetrical in $x$ and $y$, and there are now two separate minima;
the deeper of the two lying at $\boldsymbol{q}=(L / 2,0)$, has a value
$$
F_{\min x}=m_{x}^{*} /\left(4 \sin \left(K_{0}\right) m_{z}^{*}\right)\quad(31)
$$
whereas the less deep minimum at $\boldsymbol{q}=(0, L / 2)$ has a value
$$
F_{\min y}=m_{y}^{*} /\left(4 \sin \left(K_{0}\right) m_{z}^{*}\right).\quad(32)
$$

The problem is: how do we drive the system to localisation by increasing only $m_{y}^{*}$, since
the overall minimum of $F$ is determined by the smaller of $m_{x}^{*}$ and $m_{y}^{*}$? The answer is
that in order for a contour to contribute to delocalisation it has to accommodate three
$\boldsymbol{q}$-vectors (or in fact any odd number $>1$ ) whose sum is zero. This is the momentum
conservation condition imposed by equation (15) and is crucial to the understanding of
localisation in 2D. Inspection of the contours in figure 2 shows that the momentum
conservation argument can be satisfied only for those contours near the $q_{y}$ axis. The
minimum value of $F$ in this region is dictated by $m_{y}^{*}$, and the overall minimum is
inaccessible. Thus momentum conservation ensures that it is only necessary to make
$m_{y}^{*}$ large and the system can be localised with an arbitrarily small degree of disorder. In
other words we retrieve the well known result that all states are localised in 2D.

This being the case we can assume that for large $m_{y}^{*}$ the system will localise at a
degree of disorder small enough for our approximations to be valid and we can again
use our analytic results to obtain the variation of the inverse localisation length near the
transition. Again we find that the critical exponent is $1 / 2$.

It should be pointed out that even in the case $m_x^* = m_y^*$ the minimum of $F$ is not accessible because of momentum conservation, but in this case the corrections are small.

## 4. Conclusions

I have explicitly demonstrated that my theory of localisation correctly reproduces the localisation of states in 1D and 2D. In doing so I also showed that for systems in which the effective mass tensor is either an oblate or a prolate spheroid an approximate analytic theory is valid, and this theory predicts a critical exponent of $1/2$. This conclusion disagrees with conventional scaling theory (Abrahams *et al* 1979, Apel and Rice 1983) and it is of interest to speculate how this discrepancy may be resolved. I have searched for other terms within the weak scattering approximation that would give corrections to the exponent and cannot find any. My conclusion is that linear behaviour of the exponent can occur only when strong scattering is taken into account. There are several ways in which the strong scattering corrections could present themselves: possibly the exponent varies continuously from $1/2$ to $1$; more probably in the context of the mathematics of my theory the unit exponent could have steeper and steeper slope as the anisotropy is increased. We might suspect a relationship of the form

$$
\eta^{-1}=(\delta^{2}-\delta_{\mathrm{c}}^{2}+a^{2})^{1/2}-a \quad \delta^{2}>\delta_{\mathrm{c}}^{2} \tag{33}
$$

$a$ diminishing with increasing anisotropy. I stress that this equation is pure speculation as the strong scattering terms needed to produce such a correction have not yet been evaluated.

Application to real systems requires some further assumptions. Silicon doped with phosphorus, which is n-type and has $m_y^* \gg m_x^* = m_z^*$ would seem an obvious candidate. Even if, as has been suggested by Mott (1985), the conduction takes place in an impurity band there will be substantial anisotropy. The impurity states lie close in energy to the conduction bands and their wavefunctions decay away from the impurity in a manner dictated by the Green function of the host. Because of the proximity in energy of the conduction bands the Green function is also highly anisotropic being derived mainly from these bands. Thus the impurity wavefunction will not have spherical character and will have preferred directions of overlap with other impurity states in the same manner that the conduction states do. However we must further assume that there is no sub- stantial inter-valley scattering which would tend to make the system more isotropic and invalidate our theory. In the cases where this assumption is true the prediction would be that silicon should show a critical exponent of $1/2$. Significantly, experiments on phosphorus-doped silicon do give this result (Thomas 1985). Other experiments on compensated samples show an exponent of unity: the scattering being stronger in these systems I expect inter-valley scattering to play a role and invalidate my theory. On the other hand gallium arsenide has an isotropic effective mass tensor and certainly cannot be described by the analytic theory: it has critical exponent of unity (Morita *et al* 1985).

## Acknowledgments

This work was supported by the BP Venture Research Unit. I thank Gordon Thomas for several illuminating conversations on this subject and Sir Neville Mott for helpful comments on the manuscript.

### References

Abrahams E, Anderson P W, Licciardello D C and Ramakrishnan T V 1979 *Phys. Rev. Lett.* **42** 673-6

Anderson P W 1985 *Proc. Conf. Solid State Electronics (Santa Cruz)* 1985 to appear

Apel W and Rice T M 1983 *J. Phys. C: Solid State Phys.* **16** L1151-4

Edwards J T and Thouless D J 1972 *J. Phys. C: Solid State Phys.* **5** 807-20

Kirkman P D and Pendry J B 1984a *J. Phys. C: Solid State Phys.* **17** 4327-43
—— 1984b *J. Phys. C: Solid State Phys.* **17** 5707-28

MacKinnon A and Kramer B 1983 *Z. Phys.* B **53** 1-13

Morita S *et al* 1985 *Proc. Conf. Solid State Electronics (Santa Cruz)* 1985 to appear

Mott N F 1985 *Proc. Conf. Solid State Electronics (Santa Cruz)* 1985 to appear

Mott N F and Kaveh M 1985 *Adv. Phys.* **34** 330-401

Pendry J B 1982a *J. Phys. C: Solid State Phys.* **15** 3493-511
—— 1982b *J. Phys. C: Solid State Phys.* **15** 4821-34
—— 1984 *J. Phys. C: Solid State Phys.* **17** 5317-36

Stephen M G 1981 *J. Stat. Phys.* **25** 663-8

Thomas G A 1985 *Phil. Mag.* to appear

Wegner F 1979 *Phys. Rev.* B **19** 783-92