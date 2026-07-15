# Dynamical Response of the Kitaev Spin Liquid under Third-Nearest-Neighbor Heisenberg Interaction

Chuan Chen$^{1,2}$ and Jiucai Wang$^{3,*}$

$^{1}$School of Physical Science and Technology, Lanzhou University, Lanzhou 730000, China
$^{2}$Lanzhou Center for Theoretical Physics, Key Laboratory of Quantum Theory and Applications of MoE, Key Laboratory of Theoretical Physics of Gansu Province, Gansu Provincial Research Center for Basic Disciplines of Quantum Physics, Lanzhou University, Lanzhou 730000, China
$^{3}$School of Physics, Hangzhou Normal University, Hangzhou 311121, China
(Dated: March 27, 2026)

Motivated by growing evidence for the significance of the third-nearest-neighbor Heisenberg ($J_3$) interaction in candidate Kitaev materials, we investigate the dynamical properties of the Kitaev spin liquid (KSL) under a $J_3$ perturbation, focusing on its spin dynamical structure factor (DSF) and Raman scattering. Within a self-consistent parton mean-field plus random-phase approximation framework, we find that $J_3$ induces coherent, paramagnon-like collective modes that coexist with a high-energy Majorana continuum in the spin DSF. The softening of these modes with increasing $|J_3|$ signals a quantum phase transition to magnetic order. Remarkably, magnetic ordering sets in at a common critical $J_3$ for both ferromagnetic ($K<0$) and antiferromagnetic ($K>0$) Kitaev models, with the resulting ordered states forming exact dual pairs under a four-sublattice duality transformation that maps $(K,J_3)\to(-K,J_3)$. An external magnetic field further softens the pre-existing paramagnon modes, thereby enhancing magnetic order. Perturbative Raman calculations show that while the Kitaev-like Raman vertex probes only itinerant matter Majorana fermions, the response from the $J_3$-like vertex features both matter Majoranas and visons. Four-vison excitations produce a sharp peak accompanied by a two-fermion continuum, whereas two-vison excitations yield a continuum closely resembling the single-matter-fermion density of states. These results provide a unified perspective on the dynamical signatures of $J_3$-perturbed KSL and are helpful for interpreting experimental spectra in candidate Kitaev materials with sizable $J_3$ interactions.

## I. INTRODUCTION

Quantum spin liquids (QSLs) are exotic phases of matter characterized by long-range entanglement and fractionalized excitations. They typically emerge in strongly frustrated quantum spin systems, where geometric frustration or quantum fluctuations preclude the formation of long-range magnetic order [1-5]. A paradigmatic example is the exactly solvable Kitaev honeycomb model [6], in which bond-dependent interactions stabilize a $\mathbb{Z}_2$ QSL hosting itinerant matter Majorana fermions coupled to static $\mathbb{Z}_2$ gauge-flux excitations (visons). A key step toward materials realization was taken by Jackeli and Khaliullin [7], who showed that such anisotropic interactions can naturally arise in spin-orbit-coupled transition-metal compounds. This insight sparked extensive efforts to identify and investigate candidate Kitaev materials over the past decade. Prominent examples include the iridates $\rm A_2IrO_3$ ($\rm A$=Li, Na), $\alpha$-RuCl$_3$, and cobaltates such as $\rm Na_2Co_2TeO_6$ (for reviews, see Refs. [8-13]). In practice, however, these materials host substantial non-Kitaev interactions—most notably nearest-neighbor (NN) Heisenberg and off-diagonal $\Gamma$ and $\Gamma'$ couplings—which typically drive magnetic ordering at low temperatures. An external magnetic field can suppress the magnetic order and drive the system into a quantum-disordered regime prior to full spin polarization at high fields. For example, $\alpha$-RuCl$_3$ exhibits a field-induced disordered phase with signatures suggestive of a proximate QSL, although its precise nature remains under active debate [14-24].

To determine whether a particular QSL is realized in a perturbed Kitaev material, it is essential to identify the underlying microscopic spin model and clarify how non-Kitaev interactions affect the Kitaev spin liquid (KSL). While substantial progress has been made in understanding the effects of NN non-Kitaev interactions, such as Heisenberg and off-diagonal $\Gamma$ and $\Gamma'$ couplings [25-38], increasing evidence points to an essential role of the third-NN Heisenberg interaction. In several candidate materials, this term is comparable to, or even exceeds, the NN Heisenberg coupling [37, 39-44]. For instance, it is crucial for stabilizing the zigzag order in ferromagnetic (FM) Kitaev systems such as $\alpha$-RuCl$_3$ [37], and for reproducing experimentally observed spin dynamical signatures in iridates and cobaltates [39, 41-48]. These observations motivate a systematic investigation of the impact of third-NN Heisenberg interaction on the KSL.

In this work, we study the Kitaev-$J_3$ ($K$-$J_3$) model, which comprises Kitaev ($K$) and third-NN Heisenberg ($J_3$) interactions. We focus in particular on how the $J_3$ term modifies the signatures of the KSL in two experimentally relevant dynamical probes: the spin dynamical structure factor (DSF) and Raman scattering.

First, we compute the spin DSF using a recently developed self-consistent parton mean-field plus random-phase approximation (RPA) framework [49]. We find that the

* Correspondence to: jcwangphys@hznu.edu.cn

$J_3$ interaction induces novel low-energy paramagnon-like collective modes below the Majorana continuum. The excitation gaps of these modes collapse at a critical $J_3$, signaling the onset of long-range magnetic order, whose ordering pattern can be inferred from the momenta of the soft modes. Specifically, in the FM Kitaev model, the KSL evolves into a zigzag phase for large positive $J_3$, whereas for large negative $J_3$, the soft-mode pattern suggests competing tendencies toward ferromagnetic and stripe order (hereafter referred to as FM+stripe regime). In the AFM Kitaev model, stripe order emerges for large negative $J_3$, while for large positive $J_3$, the soft modes suggest competing tendencies toward Néel AFM and zigzag order (referred to as AFM+zigzag regime). In both the FM+stripe and AFM+zigzag regimes, the soft modes may correspond either to nearly degenerate single-$\mathbf{Q}$ orders—where a single wavevector is ultimately selected—or to multi-$\mathbf{Q}$ states, depending on the underlying energetics. Importantly, the AFM+zigzag (FM+stripe) ordering tendencies are related to the zigzag (stripe) phases through a duality transformation of the model that maps $K \to -K$. We further investigate the effect of an external magnetic field applied along different crystallographic directions and find that it consistently enhances the tendency toward magnetic ordering.

Second, we study Raman scattering using perturbation theory combined with the exact solution of the Kitaev model. Although the pure Kitaev interaction yields a two-Majorana-fermion continuum [50, 51], the $J_3$ term introduced two additional contributions. One arises from intermediate four-vison excitations and resembles the response of the NN Heisenberg interaction [50], while the other originates from intermediate two-vison excited states. Interestingly, the Raman response associated with the latter process mimics the single-particle density of states of the itinerant matter Majorana fermions, even though a local probe cannot excite an isolated matter fermion.

The remainder of this paper is organized as follows. In Sec. II, we introduce the $K$-$J_3$ model and discuss its symmetries. In Sec. III, we present the mean-field analysis of the KSL and compute the spin DSF within a mean-field plus RPA framework, covering different $(K, J_3)$ regimes and the effect of an external magnetic field. The Raman response of the $J_3$-perturbed KSL is analyzed in Sec. IV. Finally, we conclude with a discussion in Sec. V. Additional technical details are provided in the Appendices.

## II. THE MODEL AND ITS SYMMETRIES

The $K$-$J_3$ model is defined on a honeycomb lattice, with NN Kitaev $(K)$ and third-NN Heisenberg $(J_3)$ interactions:

$$
H = \sum_{\langle i,j\rangle_\alpha} K \sigma_i^\alpha \sigma_j^\alpha + \sum_{\langle\langle\langle i,j\rangle\rangle\rangle} J_3 \boldsymbol{\sigma}_i \cdot \boldsymbol{\sigma}_j - \sum_i \mathbf{h} \cdot \boldsymbol{\sigma}_i. \quad (1)
$$

![](./images/1244230649909346316_1.jpg)

FIG. 1. (a) Schematic of the honeycomb lattice and spin axes. The A and B sublattices are indicated by black and white dots, respectively. The gray shaded region indicates a unit cell. The $\alpha$-type bonds are aligned parallel to $\boldsymbol{\delta}_\alpha$. The spin axes are illustrated by blue arrows labeled $\mathbf{e}_\alpha$. The crystal axes $\mathbf{a}$, $\mathbf{b}$, and $\mathbf{c}$ are also shown. The dashed line indicates the mirror plane associated with the transformation $\mathcal{M}_b$. (b) Brillouin zone and high-symmetry $k$ points. The red contour indicates the momentum path used to plot the spin DSF. (c) Magnetic orders induced by the $J_3$ interaction in both the FM $(K=-1)$ and AFM $(K=1)$ Kitaev models. For the FM Kitaev interaction, zigzag order emerges when $J_3 \geq 0.094$, while for $J_3 \leq -0.094$, the soft modes indicate competing tendencies toward FM and stripe order (FM+stripe). For the AFM Kitaev interaction, stripe order emerges when $J_3 \leq -0.094$, whereas for $J_3 \geq 0.094$, the soft modes suggest competing tendencies toward Néel AFM and zigzag order (AFM+zigzag). The critical values of $J_3$ coincide in the two models due to the $\mathcal{T}_4$ duality transformation $K \to -K$, under which the corresponding states are related. Note that the zigzag (stripe) configuration illustrated here is shown with equal spin-$x$ and spin-$y$ components as an example; under the $\mathcal{T}_4$ duality, this maps to a state with spin $x$ AFM (FM) and spin $y$ zigzag (stripe) components. This example is intended solely to illustrate the mapping and does not imply that the corresponding phase is necessarily a multi-$\mathbf{Q}$ state. The spin $z$ component is set to zero based on energetic considerations.

Here $\langle i,j\rangle_\alpha$ denotes a NN $\alpha$-bond $(\alpha=x,y,z)$, while $\langle\langle\langle i,j\rangle\rangle\rangle$ denotes a third-NN bond. A Zeeman term is also included to account for the effect of an external magnetic field. In this work, we consider magnetic fields applied along the three crystallographic axes $\mathbf{a}$, $\mathbf{b}$, and $\mathbf{c}$. A schematic of the honeycomb lattice and spin axes is shown in Fig. 1(a).

The model exhibits several symmetries that simplify

<table>
<caption>Table 1: Symmetries of the $K$-$J_3$ model for magnetic fields applied along different crystallographic directions.</caption>
<thead>
  <tr>
    <th>
    </th>
    <th>
      $T_{1,2}$
    </th>
    <th>
      $C_6$
    </th>
    <th>
      $\mathcal{M}_b$
    </th>
    <th>
      $\mathcal{T}$
    </th>
    <th>
      $\mathcal{T}\mathcal{M}_b$
    </th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>
      $\mathbf{h} = 0$
    </th>
    <td>
      $✓$
    </td>
    <td>
      $✓$
    </td>
    <td>
      $✓$
    </td>
    <td>
      $✓$
    </td>
    <td>
      $✓$
    </td>
  </tr>
  <tr>
    <th>
      $\mathbf{h} \parallel \mathbf{a}$
    </th>
    <td>
      $✓$
    </td>
    <td>
      $\times$
    </td>
    <td>
      $\times$
    </td>
    <td>
      $\times$
    </td>
    <td>
      $✓$
    </td>
  </tr>
  <tr>
    <th>
      $\mathbf{h} \parallel \mathbf{b}$
    </th>
    <td>
      $✓$
    </td>
    <td>
      $\times$
    </td>
    <td>
      $✓$
    </td>
    <td>
      $\times$
    </td>
    <td>
      $\times$
    </td>
  </tr>
  <tr>
    <th>
      $\mathbf{h} \parallel \mathbf{c}$
    </th>
    <td>
      $✓$
    </td>
    <td>
      $✓$
    </td>
    <td>
      $\times$
    </td>
    <td>
      $\times$
    </td>
    <td>
      $✓$
    </td>
  </tr>
</tbody>
</table>

the mean-field analysis by reducing the number of independent mean-field parameters. In the absence of a magnetic field, the model is invariant under the following symmetry operations (c.f. Fig. 1(a)): (i) lattice translations $T_1$ and $T_2$ along the primitive vectors $\mathbf{a}_1$ and $\mathbf{a}_2$, respectively; (ii) a sixfold rotation about the $c$ axis followed by a mirror reflection with respect to the $a$-$b$ plane (denoted by $C_6$); (iii) time-reversal symmetry $\mathcal{T}$; and (iv) mirror reflection across the plane perpendicular to the $b$-axis (denoted by $\mathcal{M}_b$).

When an external magnetic field is applied, the symmetry of the model is reduced. The $C_6$ rotation is preserved when $\mathbf{h} \parallel \mathbf{c}$, whereas the mirror symmetry $\mathcal{M}_b$ remains intact for $\mathbf{h} \parallel \mathbf{b}$. Notably, for $\mathbf{h} \parallel \mathbf{a}$ and $\mathbf{h} \parallel \mathbf{c}$, although both $\mathcal{T}$ and $\mathcal{M}_b$ are individually broken, their product $\mathcal{T}\mathcal{M}_b$ remains a symmetry of the system [52]. A complete list of the model’s symmetries for fields applied along different crystallographic directions is given in Table I.

Besides these symmetries, the model also possesses an exact duality $(\mathcal{T}_4)$, a four-sublattice unitary transformation that maps $(K,J_3) \rightarrow (-K,J_3)$ (see Appendix B for its explicit form) [12]. This implies that the FM and AFM KSLs undergo phase transitions at the same critical value of $J_3$, with the resulting phases related by the $\mathcal{T}_4$ transformation. This further indicates that the FM and AFM KSLs share a common robustness against the $J_3$ interaction, unlike their differing repsonse to other non-Kitaev interactions. For example, the FM (AFM) KSL is more stable against the NN Heisenberg ($\Gamma$) interaction. As will be shown below, the phase diagram obtained from our spin DSF calculations is fully consistent with this property of the model.

## III. SPIN DYNAMICAL STRUCTURE FACTOR FROM MEAN-FIELD PLUS RPA

The spin DSF, measurable via inelastic neutron scattering and resonant inelastic X-ray scattering experiments, encodes the dynamical properties of a magnetic system and provides a direct window into the fractionalized excitations (e.g., spinons) of QSLs [3, 9]. While the DSF can be computed exactly for the pure Kitaev model [53, 54], non-Kitaev interactions in real materials render an exact evaluation intractable. We therefore employ a recently developed self-consistent parton mean-field plus RPA framework [49], previously shown to qualitatively capture the ordered phases induced by NN non-Kitaev couplings such as Heisenberg and $\Gamma$ interactions, and apply it here to compute the spin DSF of the $J_3$-perturbed KSL.

### A. Mean-field theory of the KSL

The mean-field theory of the KSL is most conveniently formulated using the Majorana representation of the spin operators, in which a local spin operator is expressed as a bilinear of Majorana fermions, $\sigma_j^\mu \leftrightarrow i\gamma_{j,\mu}\gamma_{j,0}$, subject to the constraint $\gamma_{j,x}\gamma_{j,y}\gamma_{j,z}\gamma_{j,0} = \hat{1}$. Here $\gamma_{x,y,z}$ and $\gamma_0$ are equivalent to the $b^{x,y,z}$ and $c$ operators introduced in the original work by Kitaev [6]. Under this representation, a two-spin term in the Hamiltonian is mapped onto a four-Majorana interaction, which is subsequently decoupled into bilinears of Majorana operators within the mean-field approximation. For example, the Kitaev interaction on a bond $\langle i,j\rangle_\alpha$ (with $i \in A$) is written as $\sigma_i^\alpha\sigma_j^\alpha \leftrightarrow i\gamma_{i,\alpha}\gamma_{i,0}i\gamma_{j,\alpha}\gamma_{j,0}$, which is decoupled as
$$
\begin{aligned}
& u_{\alpha,\alpha} i\gamma_{i,0}\gamma_{j,0} + u_{\alpha,0}\left(-i\gamma_{i,\alpha}\gamma_{j,\alpha}\right) - u_{\alpha,\alpha}u_{\alpha,0} \\
& + m_\alpha\left(i\gamma_{i,\alpha}\gamma_{i,0} + i\gamma_{j,\alpha}\gamma_{j,0}\right) - m_\alpha^2.
\end{aligned}
\tag{2}
$$

The mean-field parameters above are determined self-consistently as
$$
\begin{aligned}
u_{\alpha,\alpha} &\equiv \langle -i\gamma_{i,\alpha}\gamma_{j,\alpha}\rangle, & u_{\alpha,0} &\equiv \langle i\gamma_{i,0}\gamma_{j,0}\rangle,
\tag{3a}
\end{aligned}
$$
$$
\begin{aligned}
m_\alpha &\equiv \langle i\gamma_{i,\alpha}\gamma_{i,0}\rangle = \langle i\gamma_{j,\alpha}\gamma_{j,0}\rangle.
\tag{3b}
\end{aligned}
$$

Here we have invoked the translational symmetry of the KSL and assumed a uniform magnetization throughout the system.

Similarly, for the Heisenberg interaction on a third-NN bond $\langle\langle\langle i,j\rangle\rangle\rangle \in \alpha$ (with $i \in A$ and the bond oriented along the $\alpha$ direction), $\boldsymbol{\sigma}_i \cdot \boldsymbol{\sigma}_j$ is decoupled as
$$
\begin{aligned}
\sum_{\mu=x,y,z} \Bigg[ & v_{\alpha,\mu} i\gamma_{i,0}\gamma_{j,0} + v_{\alpha,0}\left(-i\gamma_{i,\mu}\gamma_{j,\mu}\right) - v_{\alpha,\mu}v_{\alpha,0} \\
& +m_\mu\left(i\gamma_{i,\mu}\gamma_{j,0} + i\gamma_{j,\mu}\gamma_{j,0}\right) - m_\mu^2 \Bigg].
\end{aligned}
\tag{4}
$$

The parameters $v_{\alpha,\mu}$ and $v_{\alpha,0}$ are determined through:
$$
v_{\alpha,\mu} \equiv \langle -i\gamma_{i,\mu}\gamma_{j,\mu}\rangle,\ v_{\alpha,0} \equiv \langle i\gamma_{i,0}\gamma_{j,0}\rangle.
\tag{5}
$$

Finally, the constraint $\gamma_x\gamma_y\gamma_z\gamma_0 = 1$, which is equivalent to $i\gamma_x\gamma_0 + i\gamma_y\gamma_z = 0$ (and all cyclic permutations of $x$, $y$, and $z$), is imposed on-average by adding the following term to the mean-field Hamiltonian
$$
\begin{aligned}
\sum_i \lambda_x(&i\gamma_{i,x}\gamma_0 + i\gamma_{i,y}\gamma_{i,z}) + \lambda_y(i\gamma_{i,y}\gamma_0 + i\gamma_{i,z}\gamma_{i,x}) \\
& + \lambda_z(i\gamma_{i,z}\gamma_0 + i\gamma_{i,x}\gamma_{i,y}).
\end{aligned}
\tag{6}
$$

Here the $\lambda_x$ is a Lagrange multiplier which is determined by $\langle i\gamma_{i,x}\gamma_{i,0} + i\gamma_{i,y}\gamma_{i,z}\rangle = 0$, while $\lambda_y$ and $\lambda_z$ are fixed analogously.

For the ideal Kitaev model, the KSL ground state satisfies (for $\alpha = x,y,z$):
$$
u_{\alpha,\alpha} = 1,\ u_{\alpha,0} \approx -\text{sgn}(K) \times 0.525,\ m_\alpha = \lambda_\alpha = 0.
\tag{7}
$$

![](./images/1244230649909346316_2.jpg)

FIG. 2. Mean-field fermion band dispersions at selected $J_3$ for an FM Kitaev interaction ($K=-1$). (a) Fermion bands for the pure FM Kitaev model ($J_3=0$). The gauge fermions are static and form degenerate flat bands. (b) A finite $J_3$ term ($J_3=0.04$) induces gauge fluctuations, rendering the gauge-fermion bands dispersive. (c) The gauge-fermion bands become more dispersive at larger $J_3=0.092$. (d) Fermion bands at $J_3=0.092$ in the presence of a magnetic field $\mathbf{h}=0.2\,\mathbf{a}$. Hybridization between gauge and matter fermions further enhances the band dispersion and gaps out the Dirac cone at the K point.

![](./images/1244230649909346316_3.jpg)

FIG. 3. Mean-field [(a), (c)] versus RPA-corrected [(b), (d)] spin DSFs: (a)-(b) for the ferromagnetic Kitaev model $(K,J_3)=(-1,0)$; (c)-(d) for $(K,J_3)=(-1,0.04)$. The structure factors are plotted on a logarithmic scale, $\ln[1+S(\omega,\mathbf{q})]$.

The projective symmetry group (PSG) [55] of the associated parton mean-field Hamiltonian can then be deduced, which encodes how the Majorana fermions transform under the various symmetry operations listed in Sec. II (see Table I of Ref. [56]). In this study, we focus on the KSL perturbed by a $J_3$ interaction and an external magnetic field, whose PSG is a subgroup of that of the ideal KSL. The projective implementations of the remaining symmetries therefore coincide with those in the ideal case.

The symmetry of the mean-field Hamiltonian will impose constraints that reduce the number of independent mean-field parameters. In the absence of an external magnetic field, the time-reversal symmetry enforces $m_\alpha=\lambda_\alpha=0$ ($\alpha=x,y,z$), while the $C_6$ and $\mathcal{M}_b$ symmetries require

$$
u_{x,0}=u_{y,0}=u_{z,0}, u_{x,x}=u_{y,y}=u_{z,z}, \tag{8a}
$$

$$
v_{x,0}=v_{y,0}=v_{z,0}, v_{x,x}=v_{y,y}=v_{z,z}, \tag{8b}
$$

$$
v_{x,y}=v_{y,z}=v_{z,x}=v_{x,z}=v_{y,x}=v_{z,y}. \tag{8c}
$$

As a result, only five independent mean-field parameters remain to be determined self-consistently.

The mean-field Hamiltonian can be diagonalized in momentum space by defining

$$
\gamma_{\mathbf{k},A/B,\mu}=\frac{1}{\sqrt{2N}}\sum_{\mathbf{r}\in A}e^{-i\mathbf{k}\cdot\mathbf{r}}\gamma_{\mathbf{r},A/B,\mu}, \tag{9}
$$

where $N$ is the number of unit cells in the system. We adopt the convention of labeling a B site (located at $\mathbf{r}+\boldsymbol{\delta}_x$) by the coordinate $\mathbf{r}$ of the A site in the same unit cell (see Fig. 1(a)). The mean-field Hamiltonian is then written as

$$
H=\frac{1}{2}\sum_{\mathbf{k}}\left(\Gamma_{\mathbf{k},A}^{\dagger},\Gamma_{\mathbf{k},B}^{\dagger}\right)h(\mathbf{k})\begin{pmatrix}\Gamma_{\mathbf{k},A}\\\Gamma_{\mathbf{k},B}\end{pmatrix}+\text{const.,} \tag{10}
$$

where $\Gamma_{\mathbf{k},a}^{\dagger}=\left(\gamma_{\mathbf{k},a,0}^{\dagger},\gamma_{\mathbf{k},a,x}^{\dagger},\gamma_{\mathbf{k},a,y}^{\dagger},\gamma_{\mathbf{k},a,z}^{\dagger}\right)$, $(a=A,B)$.
Since $h(-\mathbf{k})=-h(\mathbf{k})^T=-h(\mathbf{k})^*$, the Hamiltonian can

be diagonalized as
$$
H = \sum_{\mathbf{k}} \sum_{n=1}^{4} E_{n,\mathbf{k}} \alpha_{\mathbf{k},n}^{\dagger} \alpha_{\mathbf{k},n} + \text{const}, \tag{11}
$$
where $E_{n,\mathbf{k}} \geq 0$. The quasiparticles are defined as
$$
\left(\alpha_{\mathbf{k},1}^{\dagger}, \dots, \alpha_{\mathbf{k},4}^{\dagger}\right) = \left(\Gamma_{\mathbf{k},A}^{\dagger}, \Gamma_{\mathbf{k},B}^{\dagger}\right) u(\mathbf{k}), \tag{12a}
$$
$$
h(\mathbf{k}) u(\mathbf{k}) = u(\mathbf{k}) \begin{pmatrix} E_{1,\mathbf{k}} & & \\ & \ddots & \\ & & E_{4,\mathbf{k}} \end{pmatrix}. \tag{12b}
$$

The fermion band dispersions for an FM Kitaev interaction at selected $J_3$ values are shown in Fig. 2. For the pure Kitaev model, the gauge fermions have flat bands, reflecting the fact that the vison excitations are gapped and static. As $J_3$ is turned on, these bands become dispersive, indicating that the $J_3$ term induces gauge fluctuations. In the absence of an external magnetic field, the itinerant Majorana fermions $\gamma_0$ are decoupled from the gauge fermions $\gamma_{x,y,z}$, and the Dirac cones of the itinerant Majorana fermions are preserved. In contrast, when $\mathbf{h} \neq 0$, the hybridization between the two types of fermions can gap the spectrum. An analysis of the mean-field Hamiltonian in the presence of a magnetic field is presented in Appendix A.

### B. RPA calculation of the spin susceptibility

The spin DSF is defined as
$$
S_{\mu,\nu}(\omega, \mathbf{q}) = \frac{1}{N} \int dt e^{i\omega t} \langle \sigma_{\mathbf{q}}^{\mu}(t) \sigma_{-\mathbf{q}}^{\nu}(0) \rangle. \tag{13}
$$

According to the fluctuation-dissipation theorem [57], it is related to the spin susceptibility through
$$
S_{\mu,\nu}(\omega, \mathbf{q}) = \frac{-2}{1 - e^{-\beta \omega}} \text{Im} \chi_{\mu,\nu}(i\Omega_n \to \omega + i\eta, \mathbf{q}), \tag{14}
$$
where the prefactor reduces to $-2$ in the zero-temperature limit and for $\omega > 0$. The imaginary-time spin susceptibility can be written as
$$
\chi_{\mu,\nu} = \left(1, e^{-i\mathbf{q} \cdot \boldsymbol{\delta}_x}\right) \begin{pmatrix} \chi_{A\mu,A\nu} & \chi_{A\mu,B\nu} \\ \chi_{B\mu,A\nu} & \chi_{B\mu,B\nu} \end{pmatrix} \begin{pmatrix} 1 \\ e^{i\mathbf{q} \cdot \boldsymbol{\delta}_x} \end{pmatrix}, \tag{15}
$$
where the argument $(i\Omega_n, \mathbf{q})$ has been suppressed for brevity. The sublattice-resolved spin susceptibility is defined as
$$
\chi_{a\mu,b\nu}(i\Omega_n, \mathbf{q}) = \int d\tau e^{i\Omega_n \tau} \chi_{a\mu,b\nu}(\tau, \mathbf{q}), \tag{16a}
$$
$$
\chi_{a\mu,b\nu}(\tau, \mathbf{q}) = -\frac{1}{N} \langle T \sigma_{\mathbf{q},a}^{\mu}(\tau) \sigma_{-\mathbf{q},b}^{\nu}(0) \rangle. \tag{16b}
$$

Utilizing the Majorana representation of spins, the spin susceptibility at the mean-field level reduces to a convolution of two single-particle Green's functions
$$
\begin{aligned}
& \chi_{a\mu,b\nu}^0(i\Omega_n, \mathbf{q}) \\
& = -\frac{(2i)^2}{N\beta} \sum_{\omega_n,\mathbf{k}} \bigg[ G_{a\mu,b\nu}^0(i\omega_n + i\Omega_n, \mathbf{k} + \mathbf{q}) G_{b0,a0}^0(i\omega_n, \mathbf{k}) \\
& \quad - G_{a\mu,b0}^0(i\omega_n + i\Omega_n, \mathbf{k} + \mathbf{q}) G_{b\nu,a0}^0(i\omega_n, \mathbf{k}) \bigg], \tag{17}
\end{aligned}
$$
where the single-particle Green's function is defined as $(\mu, \nu = 0, x, y, z)$
$$
G_{a\mu,b\nu}^0(\tau, \mathbf{k}) = -\langle T \gamma_{\mathbf{k},a,\mu}(\tau) \gamma_{\mathbf{k},b,\nu}^{\dagger}(0) \rangle_0. \tag{18}
$$

Transforming to Matsubara frequency leads to
$$
\begin{aligned}
& G_{a\mu,b\nu}^0(i\omega_n, \mathbf{k}) \\
& = \sum_{l=1}^{4} \left[ \frac{u(\mathbf{k})_{a\mu,l} u(\mathbf{k})_{l,b\nu}^{\dagger}}{i\omega_n - E_{l,\mathbf{k}}} + \frac{u(-\mathbf{k})_{a\mu,l}^{*} u(-\mathbf{k})_{l,b\nu}^{T}}{i\omega_n + E_{l,\mathbf{k}}} \right]. \tag{19}
\end{aligned}
$$

Eqs. (17) and (19) indicate that the mean-field spin DSF forms a two-particle continuum, as shown in Fig. 3(a).

To go beyond the mean-field approximation, we adopt the RPA formalism of Ref. [49], which partially incorporates the fluctuations around the saddle point and provides a quantitatively good approximation to the spin DSF of the ideal Kitaev model. Within the RPA calculation, the original spin-spin interactions—expressed in terms of Majorana fermions—are reintroduced. For the $K$-$J_3$ model, the interaction term reads
$$
\frac{-(2i)^2}{N} \sum_{\mathbf{k},\mathbf{k}',\mathbf{p}} \sum_{a,b,\mu,\nu} U(\mathbf{p})_{a\mu,b\nu} \gamma_{\mathbf{k},a,\mu}^{\dagger} \gamma_{\mathbf{k}-\mathbf{p},a,0} \gamma_{\mathbf{k}',b,\nu}^{\dagger} \gamma_{\mathbf{k}'+\mathbf{p},b,0}, \tag{20}
$$
where the interaction matrix $U(\mathbf{p})$ takes the form
$$
U(\mathbf{p}) = \begin{pmatrix} U(\mathbf{p})_{AA} & U(\mathbf{p})_{AB} \\ U(\mathbf{p})_{BA} & U(\mathbf{p})_{BB} \end{pmatrix}, \tag{21a}
$$
$$
\begin{aligned}
& U(\mathbf{p})_{AB} = U(\mathbf{p})_{BA}^{\dagger} = \frac{-K}{2} \begin{pmatrix} 1 & 0 & 0 \\ 0 & e^{i\mathbf{p} \cdot \mathbf{a}_1} & 0 \\ 0 & 0 & e^{i\mathbf{p} \cdot \mathbf{a}_2} \end{pmatrix} \\
& - \frac{J_3}{2} \left(e^{i\mathbf{p} \cdot (\mathbf{a}_1+\mathbf{a}_2)} + e^{i\mathbf{p} \cdot (\mathbf{a}_2-\mathbf{a}_1)} + e^{i\mathbf{p} \cdot (\mathbf{a}_1-\mathbf{a}_2)}\right) \mathbb{1}_3, \tag{21b}
\end{aligned}
$$
$$
U(\mathbf{p})_{AA} = U(\mathbf{p})_{BB} = 0. \tag{21c}
$$

The RPA susceptibility is related to the mean-field susceptibility in in Eq. (17) through
$$
\chi(i\Omega_n, \mathbf{q}) = \left[1 + \chi^0(i\Omega_n, \mathbf{q}) \tilde{U}(\mathbf{q})\right]^{-1} \chi^0(i\Omega_n, \mathbf{q}), \tag{22a}
$$
$$
\tilde{U}(\mathbf{q}) = U(\mathbf{q}) + U(-\mathbf{q})^T. \tag{22b}
$$

The spin DSF is then obtained from Eq. (13). Throughout this paper, we focus on its diagonal components, defined as $S(\omega, \mathbf{q}) = \sum_{\alpha} S_{\alpha,\alpha}(\omega, \mathbf{q})$, and present them on a logarithmic scale, $\ln[1 + S(\omega, \mathbf{q})]$.

![](./images/1244230649909346316_4.jpg)

FIG. 4. RPA spin DSFs in different regimes of $(K,J_3)$. For the AFM Kitaev model, the gap closing of the $M'$ and M modes at (a) $J_3=-0.094$ signals a transition to the stripe order, while the gap closing of the $\Gamma'$ and M modes at (b) $J_3=0.094$ indicates the emergence of the AFM+zigzag regime. For the FM Kitaev model, at (c) $J_3=-0.094$, the gap closing of a sharp $\Gamma$ mode together with additional closings at $\Gamma'$, $M'$, and M signals a transition to the FM+stripe regime, whereas the "condensation" of the M mode at (d) $J_3=0.094$ indicates a transition to the zigzag order.

The RPA correction to the spin dynamics is dramatic. Fig. 3 shows the comparison between the mean-field and RPA spin DSFs for the pure FM Kitaev model $(K,J_3)=(-1,0)$ and for $(K,J_3)=(-1,0.04)$. In Fig. 3(a), the peak in the mean-field structure factor originates from the enhanced density of states of the itinerant Majorana fermions. The RPA correction, however, shifts most of the spectral weight to the bottom of the continuum, mimicking the effect of local vison excitations on the itinerant Majoranas (see Fig. 3(b)). Remarkably, the RPA susceptibility quantitatively reproduces the exact result of the Kitaev model once the spectrum is shifted downward to compensate for the mean-field overestimation—by about a factor of four—of the vison-pair excitation energy [49]. In Fig. 3(c), the peak in the mean-field structure factor at $J_3=0.04$ becomes dispersive, reflecting fluctuations of the gauge fermions induced by the $J_3$ interaction (c.f. Fig. 2(b)). While the mean-field spectrum remains qualitatively similar to that of the ideal Kitaev model, the RPA-corrected result differs markedly, as presented in Fig. 3(d). Although the RPA correction still shifts most of the spectral weight to the bottom of the continuum, it now forms a dispersive feature. A large fraction of the weight accumulates near the band minimum at the M point, reminiscent of a coherent paramagnon-like collective mode. The emergence of such collective excitations, together with a featureless higher-energy continuum resembling that of the ideal KSL, turns out to be a universal feature of the $J_3$-perturbed KSL, independent of the signs of $J_3$ and $K$. As $J_3$ increases, the dispersive collective excitations gradually separate from the Majorana continuum by moving to lower energies and becoming increasingly sharp. At a critical value of $J_3$, their excitation gaps close at certain high-symmetry momenta, signaling an instability of the KSL toward long-range magnetic order. The resulting ordering pattern can be inferred from the momenta of the condensed soft modes and the associated spectral-weight distribution.

Fig. 4 shows the spin DSFs for both FM $(K=-1)$ and AFM $(K=1)$ Kitaev interactions at $J_3=\pm0.094$. In the FM Kitaev model, at $J_3=0.094$, the sharp collective mode at momentum M undergoes gap closing, indicating a transition to zigzag order. While the same transition has been reported in previous numerical studies [42], the critical value of $J_3$ obtained here differs slightly, most likely due to the overestimation of the vison-pair excitation energy within the mean-field treatment [28]. By contrast, in the AFM Kitaev model at the same $J_3$, two sharp modes at the $\Gamma'$ and M points simultaneously soften and close their gaps, with the dominant spectral weight at $\Gamma'$. This reflects competing tendencies toward Néel AFM and zigzag order. Based on the underlying energetics, the system may select either a single-$\mathbf{Q}$ order (AFM or zigzag) or realize a multi-$\mathbf{Q}$ state involving both. We therefore refer to this regime as AFM+zigzag for brevity. The emergence of the AFM+zigzag regime follows naturally from the four-sublattice duality transformation $\mathcal{T}_4$, which maps $(K,J_3)\to(-K,J_3)$ [12]. As illustrated in Fig. 1(c), applying $\mathcal{T}_4$ to a zigzag order with wave vector $\text{M}_2$, whose ordering moment lies in the $x$-$y$ plane (with the spin $z$ component suppressed due to its energetic unfavorability under the FM Kitaev interaction), yields a state in which the spin $x$ components form a Néel AFM pattern while the spin $y$ components exhibit

a zigzag modulation. Depending on whether the original zigzag order has one or two finite spin components, the $\mathcal{T}_4$-mapped phase corresponds to a single-$\mathbf{Q}$ order (AFM or zigzag) or a multi-$\mathbf{Q}$ state with coexisting AFM and zigzag orders (see Appendix B).

For $J_3 < 0$, a similar pair of $\mathcal{T}_4$-related phases emerges. In the AFM Kitaev model at $J_3 = -0.094$, two sharp modes at $M'$ and M close their gaps, with stronger spectral weight at $M'$, indicating a transition to the stripe order. By contrast, in the FM Kitaev model at the same $J_3$, in addition to these two modes, two further modes at $\Gamma$ and $\Gamma'$ also close their gaps simultaneously, with the $\Gamma$ mode carrying the dominant spectral weight, reflecting competing FM and stripe tendencies. Based on the energetics, the system may select a single-$\mathbf{Q}$ order (FM or stripe) or realize a multi-$\mathbf{Q}$ state combining both. We therefore refer to this regime as FM+stripe. The FM+stripe regime can also be understood via the $\mathcal{T}_4$ duality transformation: applying $\mathcal{T}_4$ to a stripe order with wave vector $M_2'$ (see Fig. 1(c)), whose spins lie in the $x$-$y$ plane (with the spin $z$ component suppressed for energetic reasons), yields a state in which the spin $x$ components align ferromagnetically while the spin $y$ components exhibit a stripe modulation. Depending on whether the original stripe order has one or two finite spin components, the $\mathcal{T}_4$-mapped phase corresponds to a single-$\mathbf{Q}$ order (FM or stripe) or a multi-$\mathbf{Q}$ state with coexisting FM and stripe orders (see also Appendix B).

Therefore, our mean-field plus RPA calculations of the spin DSF for KSL reveal both the high-energy Majorana continuum and low-energy paramagnon-like collective modes, whose condensation reliably characterizes the system's tendency toward magnetic ordering. Remarkably, at the same critical value of $J_3$, a pair of $\mathcal{T}_4$-related magnetic orders emerge in the FM and AFM Kitaev models, in full agreement with the exact $\mathcal{T}_4$ duality of the model. While the precise nature (single-$\mathbf{Q}$ or multi-$\mathbf{Q}$) of the AFM+zigzag and FM+stripe regimes cannot be resolved from our RPA calculations, preliminary variational Monte Carlo results suggest that single-$\mathbf{Q}$ states are favored [58].

### C. Magnetic-field effects

We have also examined the effect of magnetic fields on the $J_3$-perturbed KSL by computing the spin DSF in the presence of an external field applied along each of the three crystallographic directions. It was found that the field generally destabilizes the KSL and enhances the tendency toward magnetic ordering by softening some or all of the existing low-energy collective modes.

Fig. 5 shows the impact of a magnetic field on the spin DSF in the FM Kitaev model at $J_3 = 0.092$, just below the critical value for the zigzag transition. For fields applied along any of the three crystallographic directions, the gap of the M mode is reduced, signaling a field-induced tendency toward the zigzag order. On the opposite side of the $J_3$ axis, at $J_3 = -0.092$, before entering the FM+stripe phase, the effect of the field depends strongly on its direction (see Fig. 6). A field along the $\mathbf{b}$ direction softens all collective modes at $\Gamma$, $\Gamma'$, $M'$, and M, promoting the transition to the FM+stripe phase. In contrast, fields along the $\mathbf{a}$ or $\mathbf{c}$ directions only soften the $\Gamma$ and $\Gamma'$ modes while lifting the $M'$ and M modes, favoring an FM order.

![](./images/1244230649909346316_5.jpg)

FIG. 5. Spin DSF for $(K,J_3)=(-1,0.092)$ in the presence of a finite external magnetic field. For fields applied along each of the three crystallographic directions, the M mode softens under the magnetic field, signaling a field-induced transition to the zigzag order.

Similar field effects are observed in the AFM Kitaev model. Fig. 8 shows the spin DSF at $J_3 = -0.092$, just before the transition to the stripe phase. For fields applied along any crystallographic direction, the gaps at both the $M'$ and M points vanish at $|\mathbf{h}| \approx 0.2$, indicating a field-induced transition to the stripe order. At $J_3 = 0.092$, below the critical value for the AFM+zigzag transition, both the $\Gamma'$ and M modes are softened by a magnetic field, but the order in which their gaps close depends on the field direction, as shown in Fig. 7. For a field along $\mathbf{a}$, the gap of the $\Gamma'$ mode closes first at $\mathbf{h}=0.24\mathbf{a}$, signaling a transition to a Néel AFM phase. In contrast, for fields along $\mathbf{b}$ and $\mathbf{c}$, the M mode condenses first, indicating a transition to the zigzag order.

### IV. RAMAN SCATTERING SIGNATURES

Raman scattering provides a complementary dynamical probe of QSLs. In general, QSLs are expected to

![](./images/1244230649909346316_6.jpg)

FIG. 6. Spin DSF for $(K,J_3)=(-1,-0.092)$ in the presence of a finite external magnetic field. For fields applied along both (a) $\mathbf{a}$ and (c) $\mathbf{c}$ directions, the $\Gamma$ and $\Gamma'$ modes soften while the M and M$'$ modes get lifted, indicating a transition into the FM order. In contrast, for (b) $\mathbf{h}\parallel\mathbf{b}$, all modes get softened, signaling a field-induced transition to the FM+stripe regime.

![](./images/1244230649909346316_7.jpg)

FIG. 7. Spin DSF for $(K,J_3)=(1,0.092)$ in a finite magnetic field. Both the $\Gamma'$ and M modes soften, but the order in which their gaps close depends on the field direction. For a field along (a) $\mathbf{a}$, the $\Gamma'$ mode condenses first, indicating a transition to a Néel AFM phase. For fields along (b) $\mathbf{b}$ and (c) $\mathbf{c}$, the M gap closes first, signaling a transition to the zigzag phase.

exhibit only a weak dependence of the Raman intensity on the polarization angle, in contrast to magnetically ordered states [59, 60]. More importantly, fractionalized excitations can also manifest themselves in the Raman response. For example, in the pure Kitaev model the Raman operator excites only the itinerant Majorana fermions, making Raman scattering an ideal probe of their fermionic nature [51]. In this section, we analyze the Raman response of the KSL under a weak $J_3$ perturbation.

### A. Raman operator

We begin by introducing the Raman operator for the $K$-$J_3$ model. Within the Loudon-Fleury approximation [61], the Raman operator for the $K$-$J_3$ model contains two parts, $\mathcal{R}=\mathcal{R}_K+\mathcal{R}_{J_3}$, where

$$
\mathcal{R}_K = \sum_{\langle i,j\rangle_\alpha} \lambda_K \left(\boldsymbol{\epsilon}_{\rm in}\cdot\mathbf{d}_{i,j}\right)\left(\boldsymbol{\epsilon}_{\rm out}\cdot\mathbf{d}_{i,j}\right)\sigma_i^\alpha\sigma_j^\alpha, \tag{23a}
$$

$$
\mathcal{R}_{J_3} = \sum_{\langle i,j\rangle_3} \lambda_{J_3} \left(\boldsymbol{\epsilon}_{\rm in}\cdot\mathbf{d}_{i,j}\right)\left(\boldsymbol{\epsilon}_{\rm out}\cdot\mathbf{d}_{i,j}\right)\sigma_i\cdot\sigma_j. \tag{23b}
$$

Here $\boldsymbol{\epsilon}_{\rm in}$ ($\boldsymbol{\epsilon}_{\rm out}$) denotes the polarization vector of the incoming (outgoing) light, which is taken to lie within the honeycomb plane. $\mathbf{d}_{i,j}$ is the relative position vector between sites $i$ and $j$. The constants $\lambda_K$ and $\lambda_{J_3}$ are proportional to $K$ and $J_3$, respectively. Their ratio $g\equiv\lambda_{J_3}/\lambda_K=J_3/K$ therefore serves as a small parameter in the $J_3$-perturbed KSL. For simplicity, we factor out the overall coupling constant $\lambda_K$, equivalent to setting $\lambda_K=1$ and $\lambda_{J_3}=g$. To ensure the validity of our perturbative analysis, which assumes the KSL remains stable under the small $J_3$ interaction, we choose $g=0.05$, safely below the critical value $|J_3/K|=0.094$ for the transition into ordered phases determined from our mean-field plus RPA calculation.

The two contributions to the Raman operator generate different types of excitations in the KSL. While the Kitaev term $(\mathcal{R}_K)$ excites only the itinerant Majorana fermions $\gamma_0$, the $J_3$ term $(\mathcal{R}_{J_3})$ inevitably creates vison excitations, i.e., excites the gauge Majoranas $\gamma_{x,y,z}$. As a consequence, their Raman responses display qualitatively different features, which will be analyzed in the following.

### B. Raman signals

The Raman response of the model is defined as

$$
I(\omega)=\int dt\,e^{i\omega t}\langle\mathcal{R}(t)\mathcal{R}(0)\rangle. \tag{24}
$$

![](./images/1244230649909346316_8.jpg)

FIG. 8. Spin DSF for $(K,J_{3})=(1,-0.092)$ in the presence
of a finite external magnetic field. For fields applied along
each of the three crystallographic directions, both the $M'$ and
M modes soften under the magnetic field, signaling a field-
induced transition to the stripe order.

At zero temperature, the expectation value is evaluated
with respect to the ground state $|\Phi_{0}\rangle$. Since our focus is
the small-$J_{3}$ regime, where the ground state $|\Phi_{0}\rangle$ is adia-
batically connected to that of the pure Kitaev model $|\Omega\rangle$,
the correlator $\langle\mathcal{R}(t)\mathcal{R}(0)\rangle$ can be evaluated by treating
the $J_{3}$ interaction $(H_{J_{3}})$ as a perturbation to the Kitaev
Hamiltonian $(H_{K})$ [50]. In the interaction picture, it can
be written as
$$\langle\Omega|U_{I}(-\infty,t)\mathcal{R}^{(0)}(t)U_{I}(t,0)\mathcal{R}^{(0)}(0)U_{I}(0,-\infty)|\Omega\rangle.\ (25)$$

Here $\mathcal{R}^{(0)}(t)=e^{iH_{K}t}\mathcal{R}e^{-iH_{K}t}$, and the time-evolution
operator is
$$
\begin{aligned}
U_{I}\left(t, t^{\prime}\right) & =T \exp \left(-i \int_{t^{\prime}}^{t} d t_{1} H_{J_{3}}^{(0)}\left(t_{1}\right)\right) \\
& =1-i \int_{t^{\prime}}^{t} d t_{1} H_{J_{3}}^{(0)}\left(t_{1}\right)+\cdots
\end{aligned}\quad(26)
$$

To leading order in $g$, and retaining only terms involv-
ing the lowest-order multi-$\gamma_{0}$ correlation functions [62],
the Raman response is dominated by two contributions
$I(\omega)=I_{K}(\omega)+I_{J_{3}}(\omega)$, with
$$
I_{K}(\omega)=\int d t e^{i \omega t}\left\langle\Omega\left|\mathcal{R}_{K}^{(0)}(t) \mathcal{R}_{K}^{(0)}(0)\right| \Omega\right\rangle, \quad(27 \mathrm{a})
$$

$$
I_{J_{3}}(\omega)=\int d t e^{i \omega t}\left\langle\Omega\left|\mathcal{R}_{J_{3}}^{(0)}(t) \mathcal{R}_{J_{3}}^{(0)}(0)\right| \Omega\right\rangle. \quad(27 \mathrm{~b})
$$

Since the correlators above involve time evolution gov-
erned solely by the Kitaev Hamiltonian, they can be eval-
uated using the exact solutions of $H_{K}$. In the Majorana
representation,
$$
H_{K}=\sum_{\langle i, j\rangle_{\alpha}} K \hat{u}_{i, j} i \gamma_{i, 0} \gamma_{j, 0}, \quad(28)
$$
where for a bond $\langle i, j\rangle_{\alpha}$ with $i \in A$, we define a com-
plex gauge fermion $\chi_{i, \alpha} \equiv\left(\gamma_{i, \alpha}+i \gamma_{j, \alpha}\right)$, whose parity
corresponds to the $\mathbb{Z}_{2}$ gauge field $\hat{u}_{i, j} \equiv-i \gamma_{i, \alpha} \gamma_{j, \alpha}=$
$1-2 \chi_{i, \alpha}^{\dagger} \chi_{i, \alpha}$. We also introduce a complex matter
fermion within each unit cell, $a_{\mathbf{r}}=\left(\gamma_{\mathbf{r}, A, 0}+i \gamma_{\mathbf{r}, B, 0}\right)$ (see
Fig. 1(a)). Since $\left[H_{K}, \hat{u}_{i, j}\right]=0, H_{K}$ can be diagonalized
within each fixed gauge-field sector $\left\{u_{i, j}\right\}$, where it re-
duces to a matter-fermion Bogoliubov-de Gennes (BdG)
Hamiltonian
$$
H^{a}\left[\left\{u_{i, j}\right\}\right] \equiv \sum_{\langle i, j\rangle_{\alpha}} K u_{i, j} i \gamma_{i, 0} \gamma_{j, 0}. \quad(29)
$$

The ground state of $H_{K}$ lies in the vacuum sector of $\chi$
fermions, satisfying $\hat{u}_{i, j}\left|0_{\chi}\right\rangle=\left|0_{\chi}\right\rangle$. In this sector, the
matter-fermion BdG Hamiltonian takes the form
$$
\begin{aligned}
H^{a}[\{1\}] & =\frac{1}{2} \sum_{\mathbf{k}}\left(a_{\mathbf{k}}^{\dagger}, a_{-\mathbf{k}}\right)\left(\begin{array}{cc}
\operatorname{Re} f_{\mathbf{k}} & -i \operatorname{Im} f_{\mathbf{k}} \\
i \operatorname{Im} f_{\mathbf{k}} & -\operatorname{Re} f_{\mathbf{k}}
\end{array}\right)\left(\begin{array}{c}
a_{\mathbf{k}} \\
a_{-\mathbf{k}}^{\dagger}
\end{array}\right) \\
& =\sum_{\mathbf{k}} \epsilon_{\mathbf{k}}\left(\alpha_{\mathbf{k}}^{\dagger} \alpha_{\mathbf{k}}-\frac{1}{2}\right),
\end{aligned}\quad(30)
$$
where $f_{\mathbf{k}}=2 K\left(1+e^{i \mathbf{k} \cdot \mathbf{a}_{1}}+e^{i \mathbf{k} \cdot \mathbf{a}_{2}}\right)$, and $\epsilon_{\mathbf{k}}=\left|f_{\mathbf{k}}\right|$ is the
energy of the Bogoliubov quasiparticle $\alpha_{\mathbf{k}}$. Its ground
state $\left|\Psi_{0}^{a}\right\rangle$ satisfies $\alpha_{\mathbf{k}}\left|\Psi_{0}^{a}\right\rangle=0$. The ground state of
$H_{K}$ is then $|\Omega\rangle \propto P\left|0_{\chi} ; \Psi_{0}^{a}\right\rangle$, where the projector $P=$
$\prod_{j} \frac{1}{2}\left(1+\gamma_{j, x} \gamma_{j, y} \gamma_{j, z} \gamma_{j, 0}\right)$ enforces the physical constraint
$\gamma_{j, x} \gamma_{j, y} \gamma_{j, z} \gamma_{j, 0}=1$.

Since $\mathcal{R}_{K}$ does not excite gauge fluxes, the correla-
tor in Eq. (27a) reduces to a matter-fermion correlation
function,
$$
\begin{aligned}
& \left\langle\Psi_{0}^{a}\right| e^{i t H_{0}^{a}} \sum_{\langle i, j\rangle_{\alpha}}\left(\boldsymbol{\epsilon}_{\mathrm{in}} \cdot \mathbf{d}_{i, j}\right)\left(\boldsymbol{\epsilon}_{\mathrm{out}} \cdot \mathbf{d}_{i, j}\right) i \gamma_{i, 0} \gamma_{j, 0} \\
& e^{-i t H_{0}^{a}} \sum_{\langle k, l\rangle_{\beta}}\left(\boldsymbol{\epsilon}_{\mathrm{in}} \cdot \mathbf{d}_{k, l}\right)\left(\boldsymbol{\epsilon}_{\mathrm{out}} \cdot \mathbf{d}_{k, l}\right) i \gamma_{k, 0} \gamma_{l, 0}\left|\Psi_{0}^{a}\right\rangle. \quad(31)
\end{aligned}
$$

Here we denote $H_{0}^{a} \equiv H^{a}[\{1\}]$ for brevity. Evaluating
this correlator yields [50]
$$
I_{K}(\omega)=4 \pi \sum_{\mathbf{k}} \delta\left(\omega-2 E_{\mathbf{k}}\right) \frac{\operatorname{Im}\left[f_{\mathbf{k}} v_{\mathbf{k}}^{*}\right]^{2}}{E_{\mathbf{k}}^{2}}, \quad(32)
$$
with $v_{\mathbf{k}}=\left(\boldsymbol{\epsilon}_{\mathrm{in}} \cdot \boldsymbol{\delta}_{x}\right)\left(\boldsymbol{\epsilon}_{\mathrm{out}} \cdot \boldsymbol{\delta}_{x}\right)+\left(\boldsymbol{\epsilon}_{\mathrm{in}} \cdot \boldsymbol{\delta}_{y}\right)\left(\boldsymbol{\epsilon}_{\mathrm{out}} \cdot \boldsymbol{\delta}_{y}\right) e^{i \mathbf{k} \cdot \mathbf{a}_{1}}+$
$\left(\boldsymbol{\epsilon}_{\mathrm{in}} \cdot \boldsymbol{\delta}_{z}\right)\left(\boldsymbol{\epsilon}_{\mathrm{out}} \cdot \boldsymbol{\delta}_{z}\right) e^{i \mathbf{k} \cdot \mathbf{a}_{2}}$.

Eq. (32) suggests that the overall behavior of $I_{K}(\omega)$
reflects the two-particle density of states of the matter
fermions. As shown in Fig. 10(a), it increases linearly
from $\omega=0$, forms a broad continuum peaked around

![](./images/1244230649909346316_9.jpg)

FIG. 9. Examples of intermediate vison configurations (gray hexagons) generated by $\mathcal{R}_{J_{3}}$. (a) Four-vison configuration generated by $\sigma_{1}^{z} \sigma_{4}^{z}$. (b) Two-vison configuration generated by $\sigma_{5}^{z} \sigma_{8}^{z}$ and $\sigma_{7}^{z} \sigma_{6}^{z}$.

$\omega=4|K|$, and terminates at $\omega=12|K|$. Fig. 10(b) shows the total intensity versus polarization angle, which is independent of polarization, as expected.

Unlike $\mathcal{R}_{K}, \mathcal{R}_{J_{3}}$ creates vison excitations. Depending on the orientation of $\langle i, j\rangle_{3}$ and the spin components of the bilinear terms in Eq. (23b), either two- or four-vison states are generated. In the former case the visons reside on next-NN plaquettes, while in the latter they form two NN vison pairs (see Fig. 9). Accordingly, the $\mathcal{R}_{J_{3}}$ correlator in Eq. (27b) can be decomposed as
$$
\left\langle\Omega\left|\mathcal{R}_{J_{3}}^{(0)}(t) \mathcal{R}_{J_{3}}^{(0)}(0)\right| \Omega\right\rangle=g^{2} \sum_{\mathbf{r} \in A, \alpha} F_{\mathbf{r}, \alpha}^{2 \mathrm{v}}(t)+F_{\mathbf{r}, \alpha}^{4 \mathrm{v}}(t). \quad(33)
$$

In $F_{\mathbf{r}, \alpha}^{2 \mathrm{v}}(t)$, the two next-NN visons are separated by two $\alpha$ bonds emanating from $\mathbf{r}$ and $\mathbf{r}+\varepsilon_{\alpha \beta \gamma}\left(\boldsymbol{\delta}_{\beta}-\boldsymbol{\delta}_{\gamma}\right) / 2$, respectively. In $F_{\mathbf{r}, \alpha}^{4 \mathrm{v}}(t)$, the two NN vison pairs reside on the $\alpha$ bonds emanating from $\mathbf{r}$ and $\mathbf{r}-3 \boldsymbol{\delta}_{\alpha}$, respectively. Fig. 9 shows typical vison configurations associated with $F_{\mathbf{r}, z}^{2 \mathrm{v}}$ and $F_{\mathbf{r}, z}^{4 \mathrm{v}}$, whose expression are derived below. The results for other orientations of visons can be obtained similarly.

The four visons in $F_{1, z}^{4 \mathrm{v}}(t)$ (c.f. Fig. 9(a)) are created by $\sigma_{1}^{z} \sigma_{4}^{z}$. Therefore
$$
F_{1, z}^{4 \mathrm{v}}(t)=\left(2 \boldsymbol{\delta}_{z} \cdot \boldsymbol{\epsilon}_{\mathrm{in}}\right)^{2}\left(2 \boldsymbol{\delta}_{z} \cdot \boldsymbol{\epsilon}_{\mathrm{out}}\right)^{2} C_{1, z}^{4 \mathrm{v}}(t), \quad(34 \mathrm{a})
$$
$$
C_{1, z}^{4 \mathrm{v}}(t)=\left\langle\Omega\left|e^{i H_{K} t} \sigma_{1}^{z} \sigma_{4}^{z} e^{-i H_{K} t} \sigma_{1}^{z} \sigma_{4}^{z}\right| \Omega\right\rangle. \quad(34 \mathrm{~b})
$$

Utilizing the Majorana fermion representation, the correlator can be written as
$$
C_{1, z}^{4 \mathrm{v}}(t)=\left\langle\Psi_{0}^{a}\left|e^{i H_{0}^{a} t} e^{-i\left[H_{0}^{a}+V^{4 \mathrm{v}}\right] t}\right| \Psi_{0}^{a}\right\rangle. \quad(35)
$$

Here the local perturbation $V^{4 \mathrm{v}}$, corresponding to four additional visons, is given by
$$
V^{4 \mathrm{v}}=-2 K\left[i \gamma_{1,0}\left(\gamma_{6,0}+\gamma_{8,0}\right)+i\left(\gamma_{5,0}+\gamma_{7,0}\right) \gamma_{4,0}\right]. \text { (36) }
$$

The problem thus reduces to that of a local quantum quench, which can be evaluated by inserting a complete set of eigenbasis $\{|\psi\rangle\}$ of $H_{0}^{a}+V^{4 \mathrm{v}}$. The Fourier transform of $C_{1, z}^{4 \mathrm{v}}$ is then
$$
C_{1, z}^{4 \mathrm{v}}(\omega)=\sum_{\psi} 2 \pi \delta\left(\omega-\left[E_{\psi}-E_{0}\right]\right)\left|\left\langle\Psi_{0}^{a} \mid \psi\right\rangle\right|^{2}. \quad(37)
$$

Since the ground state $\left|\Psi_{0,4 \mathrm{v}}^{a}\right\rangle$ of $H_{0}^{a}+V^{4 \mathrm{v}}$ has the same fermion parity as $\left|\Psi_{0}^{a}\right\rangle$, states with an even number of Bogoliubov quasiparticle of $H_{0}^{a}+V^{4 \mathrm{v}}$ (with annihilation operators $\alpha_{i, 4 \mathrm{v}}, i=1, \ldots, N$ ) contribute to the sum over $\psi$ in Eq. (37). However, because the fermionic density of states vanishes at low energies, contributions from states with many quasiparticles are strongly suppressed. We therefore retain only the leading contributions from the (zero-quasiparticle) ground state $\left|\Psi_{0,4 \mathrm{v}}^{a}\right\rangle$ and the twoquasiparticle states $\alpha_{i, 4 \mathrm{v}}^{\dagger} \alpha_{j, 4 \mathrm{v}}^{\dagger}\left|\Psi_{0,4 \mathrm{v}}^{a}\right\rangle$ [63]:
$$
\begin{aligned}
C_{1, z}^{4 \mathrm{v}}(\omega)= & 2 \pi \delta\left(\omega-\Delta^{4 \mathrm{v}}\right)\left|\left\langle\Psi_{0}^{a} \mid \Psi_{0,4 \mathrm{v}}^{a}\right\rangle\right|^{2} \\
& +\sum_{i \neq j} 2 \pi \delta\left(\omega-\left[\Delta^{4 \mathrm{v}}+\epsilon_{i}^{4 \mathrm{v}}+\epsilon_{j}^{4 \mathrm{v}}\right]\right) \\
& \times\left|\left\langle\Psi_{0}^{a}\left|\alpha_{i, 4 \mathrm{v}}^{\dagger} \alpha_{j, 4 \mathrm{v}}^{\dagger}\right| \Psi_{0,4 \mathrm{v}}^{a}\right\rangle\right|^{2}.
\end{aligned}\qquad(38)
$$

Here, $\Delta^{4 \mathrm{v}} \equiv E_{0}^{4 \mathrm{v}}-E_{0} \approx 0.44|K|$ is the four-vison excitation energy, and $\epsilon_{i}^{4 \mathrm{v}}$ denotes the energy of quasiparticle $\alpha_{i, 4 \mathrm{v}}$. The overlaps $\left\langle\Psi_{0}^{a} \mid \Psi_{0,4 \mathrm{v}}^{a}\right\rangle$ and $\left\langle\Psi_{0}^{a}\left|\alpha_{i, 4 \mathrm{v}}^{\dagger} \alpha_{j, 4 \mathrm{v}}^{\dagger}\right| \Psi_{0,4 \mathrm{v}}^{a}\right\rangle$ are given in Appendix C.

Fig. 10(a) presents the Raman response $I_{J_{3}}^{4 \mathrm{v}}(\omega)$ from $g^{2} \sum_{\mathbf{r}, \alpha} F_{\mathbf{r}, \alpha}^{4 \mathrm{v}}$. The ground state $\left|\Psi_{0,4 \mathrm{v}}^{a}\right\rangle$ produces a sharp peak at $\Delta^{4 \mathrm{v}}$, while the two-quasiparticle states form a continuum with broad maxima near $\omega \approx 1.5|K|$ and $\omega \approx 6|K|$. Interestingly, a similar Raman response featuring both a sharp peak and a two-quasiparticle continuum—has been reported for the NN Heisenberg interaction [50], which also excites four visons, albeit with a different spatial distribution. However, unlike the NN Heisenberg case, the $J_{3}$ interaction can additionally generate two-vison excitations, which we discuss next.

In $F_{7, z}^{2 \mathrm{v}}$, two visons can be created either by $\sigma_{5}^{z} \sigma_{8}^{z}$ and $\sigma_{7}^{z} \sigma_{6}^{z}$ (c.f. Fig. 9(b)). This leads to
$$
\begin{aligned}
F_{7, z}^{2 \mathrm{v}}(t)= & \sum_{\alpha, \beta=x, y}\left(2 \boldsymbol{\delta}_{\alpha} \cdot \boldsymbol{\epsilon}_{\mathrm{in}}\right)\left(2 \boldsymbol{\delta}_{\alpha} \cdot \boldsymbol{\epsilon}_{\mathrm{out}}\right) C_{7, z ; \alpha \beta}^{2 \mathrm{v}}(t) \\
& \times\left(2 \boldsymbol{\delta}_{\beta} \cdot \boldsymbol{\epsilon}_{\mathrm{in}}\right)\left(2 \boldsymbol{\delta}_{\beta} \cdot \boldsymbol{\epsilon}_{\mathrm{out}}\right),
\end{aligned}\qquad(39)
$$
with the correlators defined as
$$
C_{7, z ; x x}^{2 \mathrm{v}}(t)=\left\langle\Omega\left|e^{i H_{K} t} \sigma_{5}^{z} \sigma_{8}^{z} e^{-i H_{K} t} \sigma_{5}^{z} \sigma_{8}^{z}\right| \Omega\right\rangle, \quad(40 \mathrm{a})
$$
$$
C_{7, z ; x y}^{2 \mathrm{v}}(t)=\left\langle\Omega\left|e^{i H_{K} t} \sigma_{5}^{z} \sigma_{8}^{z} e^{-i H_{K} t} \sigma_{7}^{z} \sigma_{6}^{z}\right| \Omega\right\rangle, \quad(40 \mathrm{~b})
$$
$$
C_{7, z ; y x}^{2 \mathrm{v}}(t)=\left\langle\Omega\left|e^{i H_{K} t} \sigma_{7}^{z} \sigma_{6}^{z} e^{-i H_{K} t} \sigma_{5}^{z} \sigma_{8}^{z}\right| \Omega\right\rangle, \quad(40 \mathrm{c})
$$
$$
C_{7, z ; y y}^{2 \mathrm{v}}(t)=\left\langle\Omega\left|e^{i H_{K} t} \sigma_{7}^{z} \sigma_{6}^{z} e^{-i H_{K} t} \sigma_{7}^{z} \sigma_{6}^{z}\right| \Omega\right\rangle. \quad(40 \mathrm{~d})
$$

Under the Majorana representation, they can be written as
$$
C_{7, z ; x x}^{2 \mathrm{v}}(t)=e^{i E_{0} t}\left\langle\Psi_{0}^{a}\left|e^{-i\left[H_{0}^{a}+V_{1}^{2 \mathrm{v}}\right] t}\right| \Psi_{0}^{a}\right\rangle, \quad(41 \mathrm{a})
$$
$$
C_{7, z ; x y}^{2 \mathrm{v}}(t)=-e^{i E_{0} t}\left\langle\Psi_{0}^{a}\left|e^{-i\left[H_{0}^{a}+V_{1}^{2 \mathrm{v}}\right] t} \mathcal{O}_{7, z}\right| \Psi_{0}^{a}\right\rangle, \quad(41 \mathrm{~b})
$$
$$
C_{7, z ; y x}^{2 \mathrm{v}}(t)=-e^{i E_{0} t}\left\langle\Psi_{0}^{a}\left|O_{7, z} e^{-i\left[H_{0}^{a}+V_{1}^{2 \mathrm{v}}\right] t}\right| \Psi_{0}^{a}\right\rangle, \quad(41 \mathrm{c})
$$
$$
C_{7, z ; y y}^{2 \mathrm{v}}(t)=e^{i E_{0} t}\left\langle\Psi_{0}^{a}\left|e^{-i\left[H_{0}^{a}+V_{2}^{2 \mathrm{v}}\right] t}\right| \Psi_{0}^{a}\right\rangle, \quad(41 \mathrm{~d})
$$
where $\mathcal{O}_{7, z} \equiv\left(i \gamma_{5,0} \gamma_{8,0}\right)\left(i \gamma_{7,0} \gamma_{6,0}\right)$. Both $V_{1}^{2 \mathrm{v}}$ and $V_{2}^{2 \mathrm{v}}$ correspond to the same two-vison configuration, but are

different by a gauge transformation:

$$
\begin{aligned}
V_{1}^{2 \mathrm{v}}= & -2 K\left[i \gamma_{5,0}\left(\gamma_{12,0}+\gamma_{4,0}\right)+i\left(\gamma_{1,0}+\gamma_{9,0}\right) \gamma_{8,0}\right], \\
& (42 \mathrm{a}) \\
V_{2}^{2 \mathrm{v}}= & -2 K\left[i \gamma_{7,0}\left(\gamma_{4,0}+\gamma_{10,0}\right)+i\left(\gamma_{11,0}+\gamma_{1,0}\right) \gamma_{6,0}\right]. \\
& (42 \mathrm{~b})
\end{aligned}
$$

The correlation functions in Eqs. (41a) to (41d) can also be evaluated by inserting the complete eigenbasis of $H_{0}^{a}+V_{1}^{2 \mathrm{v}}$ or $H_{0}^{a}+V_{2}^{2 \mathrm{v}}$. However, since their ground states $|\Psi_{0,2 \mathrm{v}, 1}^{a}\rangle$ and $|\Psi_{0,2 \mathrm{v}, 2}^{a}\rangle$ have opposite fermion parity relative to $|\Psi_{0}^{a}\rangle$, the leading contributions come from single-quasiparticle states $\alpha_{i, 2 \mathrm{v}, n}^{\dagger}|\Psi_{0,2 \mathrm{v}, n}^{a}\rangle$ $(n=1,2)$. Their Fourier transforms are then given by

$$
\begin{aligned}
C_{7, z ; x x}^{2 \mathrm{v}}(\omega)= & 2 \pi \sum_{i} \delta\left(\omega-\Delta^{2 \mathrm{v}}-\epsilon_{i}^{2 \mathrm{v}}\right)\left|\left\langle\Psi_{0}^{a}\left|\alpha_{i, 2 \mathrm{v}, 1}^{\dagger}\right| \Psi_{0,2 \mathrm{v}, 1}^{a}\right\rangle\right|^{2}, \\
& (43 \mathrm{a}) \\
C_{7, z ; x y}^{2 \mathrm{v}}(\omega)= & -2 \pi \sum_{i} \delta\left(\omega-\Delta^{2 \mathrm{v}}-\epsilon_{i}^{2 \mathrm{v}}\right) \\
& \left\langle\Psi_{0}^{a}\left|\alpha_{i, 2 \mathrm{v}, 1}^{\dagger}\right| \Psi_{0,2 \mathrm{v}, 1}^{a}\right\rangle\left\langle\Psi_{0,2 \mathrm{v}, 1}^{a}\left|\alpha_{i, 2 \mathrm{v}, 1} \mathcal{O}_{7, z}\right| \Psi_{0}^{a}\right\rangle, \\
& (43 \mathrm{~b}) \\
C_{7, z ; y z}^{2 \mathrm{v}}(\omega)= & -2 \pi \sum_{i} \delta\left(\omega-\Delta^{2 \mathrm{v}}-\epsilon_{i}^{2 \mathrm{v}}\right) \\
& \left\langle\Psi_{0}^{a}\left|\mathcal{O}_{7, z} \alpha_{i, 2 \mathrm{v}, 1}^{\dagger}\right| \Psi_{0,2 \mathrm{v}, 1}^{a}\right\rangle\left\langle\Psi_{0,2 \mathrm{v}, 1}^{a}\left|\alpha_{i, 2 \mathrm{v}, 1}\right| \Psi_{0}^{a}\right\rangle, \\
& (43 \mathrm{c}) \\
C_{7, z ; y y}^{2 \mathrm{v}}(\omega)= & 2 \pi \sum_{i} \delta\left(\omega-\Delta^{2 \mathrm{v}}-\epsilon_{i}^{2 \mathrm{v}}\right)\left|\left\langle\Psi_{0}^{a}\left|\alpha_{i, 2 \mathrm{v}, 2}^{\dagger}\right| \Psi_{0,2 \mathrm{v}, 2}^{a}\right\rangle\right|^{2} . \\
& (43 \mathrm{~d})
\end{aligned}
$$

Here, $\Delta^{2 \mathrm{v}} \equiv E_{0}^{2 \mathrm{v}}-E_{0} \approx 0.30|K|$ is the two-vison excitation gap, and the overlaps appearing above are given in Appendix C.

The Raman response $I_{J_{3}}^{2 \mathrm{v}}(\omega)$ from $g^{2} \sum_{\mathbf{r}, \alpha} F_{\mathbf{r}, \alpha}^{2 \mathrm{v}}$ is shown in Fig. 10(a). Notably, the continuum mirrors the matter-fermion density of states: it rises linearly above $\Delta^{2 \mathrm{v}}$ and exhibits a broad peak near $\omega \approx 2|K|$, close to the van Hove singularity. This is particularly interesting because a single matter fermion cannot be created by a local probe. Notably, the Raman signal from $\mathcal{R}_{K}$ contains only the isotropic $E_{g}$ channel, whereas that from $\mathcal{R}_{J_{3}}$ contains both a polarization-dependent $A_{1 g}$ channel, proportional to $\cos ^{2}\left(\theta_{\text {in }}-\theta_{\text {out }}\right)$, and a polarizationindependent $E_{g}$ channel (see Fig. 10(b)) [60].

## V. DISCUSSION

In this work, we have investigated the dynamical responses of the KSL in the presence of a third-NN Heisenberg $(J_{3})$ interaction. In particular, we calculate its spin DSF and Raman response.

Within a self-consistent parton mean-field plus RPA framework, we find that a hallmark of the $J_{3}$-perturbed KSL is the emergence of coherent paramagnon-like collective modes coexisting with the high-energy Majorana continuum, even though such modes typically being associated with proximate magnetic order. These paramagnon modes soften with increasing $J_{3}$ and eventually condense at a critical coupling, providing a natural explanation for the transition from the KSL to magnetically ordered states.

![](./images/1244230649909346316_10.jpg)

FIG. 10. (a) Raman response from $\mathcal{R}_{K}$ ($I_K$) and $\mathcal{R}_{J_3}$. The latter can be further decomposed into contributions from two-vison ($I_{J_3}^{2\mathrm{v}}$) and four-vison ($I_{J_3}^{4\mathrm{v}}$) excitations. Here, we take $\boldsymbol{\epsilon}_\text{in} = \boldsymbol{\epsilon}_\text{out} \parallel \mathbf{b}$ and $g=0.05$. (b) Total intensity as a function of the angle between $\boldsymbol{\epsilon}_\text{in}$ and $\boldsymbol{\epsilon}_\text{out}$, with $\boldsymbol{\epsilon}_\text{in} \parallel \mathbf{b}$.

A central result is that both FM and AFM Kitaev-$J_3$ models develop magnetic order at a common critical value $|J_3|=0.094|K|$. Specifically, at $J_3=0.094|K|$, the FM Kitaev model transitions to a zigzag phase, while in the AFM Kitaev model, the softening of modes at the $\Gamma'$ and M points signals the emergence of an AFM+zigzag regime, which may correspond either to a near-degenerate single-$\mathbf{Q}$ phase (AFM or zigzag) or to a multi-$\mathbf{Q}$ phase with coexisting AFM and zigzag orders. Correspondingly, at $J_3=-0.094|K|$, the AFM Kitaev model exhibits stripe order, while the FM Kitaev model enters the FM+stripe regime characterized by competing tendencies toward FM and stripe order. Remarkably, in each case, the phases realized in the FM and AFM Kitaev models are related by the exact $\mathcal{T}_4$ duality of the model ($K \to -K$), confirming that our predictions fully respect this exact symmetry. Resolving the precise nature of the AFM+zigzag and FM+stripy regimes lies beyond the scope of present framework and requires further numerical investigation, for example via exact diagonalization or density-matrix renormalization group calculations. Moreover, external magnetic fields could soften some or all of the low-energy paramagnon modes present at zero field, thereby facilitating the transition from the

KSL to magnetic order.

Complementary to the spin DSF, the Raman scattering provides another experimental probe of fractionalized excitations. A perturbative analysis shows that the Raman intensity receives separate contributions from a Kitaev-like vertex $\mathcal{R}_K$ and a $J_3$-like vertex $\mathcal{R}_{J_3}$. While the response from $\mathcal{R}_K$ originates solely from the itinerant matter Majorana fermions, the $\mathcal{R}_{J_3}$ contribution reflects both the matter Majoranas and vison excitations.

Furthermore, the $\mathcal{R}_{J_3}$ contribution can be decomposed into two components associated with two-vison ($I_{J_3}^{2\text{v}}$) and four-vison ($I_{J_3}^{4\text{v}}$) processes. The four-vison component exhibits a sharp peak at the four-vison excitation gap, accompanied by a broad two-fermion continuum, similar to the Raman response induced by a NN Heisenberg interaction [50]. In contrast, the two-vison channel forms a continuum reminiscent of the single-fermion density of states—an intriguing result, given that a local probe cannot excite an isolated matter fermion. Meanwhile, the polarization-dependent Raman response offers a direct experimental signature of fractionalized excitations modified by the $J_3$ interaction, revealing distinct contributions from itinerant Majorana fermions and visons.

Overall, our results provide a unified dynamical picture of the $J_3$-perturbed KSL, in which both the spin DSF and Raman response reveal the interplay between fractionalized excitations. The emergence and softening of paramagnon modes capture the tendency of KSL toward magnetic ordering and yield a phase diagram, while the Raman response further resolves the underlying vison excitations. We expect that these results offer useful guidance for interpreting dynamical responses in field-induced disordered regimes of candidate Kitaev materials, particularly in systems with sizable $J_3$ interactions, such as $\text{Na}_2\text{Co}_2\text{TeO}_6$.

## ACKNOWLEDGMENTS

We thank Peng Rao for fruitful discussions. C.C. acknowledges support from the National Natural Science Foundation of China (Grants No. 12404175 and No. 12247101), the Fundamental Research Funds for the Central Universities (Grant No. lzujbky-2025-jdzx07), the Natural Science Foundation of Gansu Province (No. 22JR5RA389, No. 25JRRA799). J.W. acknowledges support from the National Natural Science Foundation of China under Grant No. 12404170 and the start-up grant at HZNU. We thank Beijing Paratera Co., Ltd. for providing HPC resources that contributed to the numerical results reported in this paper.

## Appendix A: Mean-field Hamiltonian in an external magnetic field

In this section, we discuss the mean-field Hamiltonian for the KSL in the presence of an external magnetic field, which may be applied along any of the three crystallographic directions. For each case, the symmetries preserved by the model (see Table I) constrain the number of independent mean-field parameters. The mean-field Hamiltonian consists of three parts, given in Eqs. (2), (4) and (6).

1). $\mathbf{h} \parallel \mathbf{a}$. In this case, the system preserves the translations $T_{1,2}$ and $\mathcal{T}\mathcal{M}_b$ symmetry. This implies
$$
\begin{aligned}
& u_{x,0}=u_{y,0}, u_{x,x}=u_{y,y}, v_{x,0}=v_{y,0}, \\
& v_{x,x}=v_{y,y}, v_{x,y}=v_{y,x}, v_{x,z}=v_{y,z}, v_{z,x}=v_{z,y}, \\
& m_x=m_y, \lambda_x=\lambda_y.
\end{aligned} \tag{A1}
$$

Thus, 15 independent mean-field parameters must be determined self-consistently.

2). $\mathbf{h} \parallel \mathbf{b}$. In this case, the system preserves the translations $T_{1,2}$ and mirror symmetry $\mathcal{M}_b$, leading to
$$
\begin{aligned}
& u_{x,0}=u_{y,0}, u_{x,x}=u_{y,y}, v_{x,0}=v_{y,0}, \\
& v_{x,x}=v_{y,y}, v_{x,y}=v_{y,x}, v_{x,z}=v_{y,z}, v_{z,x}=v_{z,y}, \\
& m_x=-m_y, m_z=0, \lambda_x=-\lambda_y, \lambda_z=0.
\end{aligned} \tag{A2}
$$

Accordingly, there are 13 independent mean-field parameters.

3). $\mathbf{h} \parallel \mathbf{c}$. In this case, the system preserves the translation $T_{1,2}$, the $C_6$ rotation, and the $\mathcal{T}\mathcal{M}_b$ symmetry. This yields
$$
\begin{aligned}
& u_{x,0}=u_{y,0}=u_{z,0}, u_{x,x}=u_{y,y}=u_{z,z}, \\
& v_{x,0}=v_{y,0}=v_{z,0}, v_{x,x}=v_{y,y}=v_{z,z}, \\
& v_{x,y}=v_{y,z}=v_{z,x}=v_{x,z}=v_{y,x}=v_{z,y}, \\
& m_x=m_y=m_z, \lambda_x=\lambda_y=\lambda_z.
\end{aligned} \tag{A3}
$$

In this case, 7 independent mean-field parameters are to be determined self-consistently.

In the presence of a finite magnetic field, $m_\alpha$ and $\lambda_\alpha$ ($\alpha=x,y,z$) can become finite, leading to hybridization between the matter fermions $(\gamma_0)$ and gauge fermions $(\gamma_{x,y,z})$, which gaps out the Dirac cone for fields applied along the $\mathbf{a}$ and $\mathbf{c}$ directions.

## Appendix B: The four-sublattice duality transformation

In the $K$-$J_3$ model, there exists a four-sublattice duality transformation that maps $(K,J_3)\to(-K,J_3)$ [12]. The four sublattices are labeled by gray (1), red (2), green (3), and blue (4) in Fig. 11. The transformation of spin operators on each sublattice under $\mathcal{T}_4$ is summarized in Table II.

The existence of the $\mathcal{T}_4$ duality implies that the critical values of $J_3$ for the onset of magnetic order are identical in the FM and AFM Kitaev models, with the corresponding ordered phases related by $\mathcal{T}_4$. Our mean-field plus RPA calculations of the spin dynamical structure factor confirm this expectation.

![](./images/1244230649909346316_11.jpg)

FIG. 11. Magnetic order patterns induced by the $J_3$ interaction and related by the $\mathcal{T}_4$ transformation. The four sublattice involved in $\mathcal{T}_4$ are indicated by gray (sublattice-1), red (sublattice-2), green (sublattice-3), and blue (sublattice-4) colors. (a) Zigzag order with wave vector $\text{M}_2$ and the corresponding phase obtained via the $\mathcal{T}_4$ transformation. In the latter, the spin $x$ components form a Néel AFM pattern, while the spin $y$ and spin $z$ components form zigzag patterns with wave vectors $\text{M}_1$ and $\text{M}_3$, respectively (see Fig. 1). (b) stripe order with wave vector $\text{M}_2'$ and the corresponding phase exhibiting both FM and stripe components. In the latter, the spin $x$ components form a uniform FM pattern, whereas the spin $y$ and spin $z$ components develop stripe modulations with wave vectors $\text{M}_1' = \text{M}_1 + \mathbf{b}_2$ and $\text{M}_3' = \text{M}_3 + \mathbf{b}_2$, respectively (see Fig. 1). For the specific zigzag and stripe patterns considered above, $z$ is expected to vanish from on energetic grounds.

<table>
<caption>TABLE II. Transformation of spin operators under $\mathcal{T}_4$.</caption>
<thead>
<tr>
<th>Sublattice</th>
<th>$\sigma_i^x$</th>
<th>$\sigma_i^y$</th>
<th>$\sigma_i^z$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>$\sigma_1^x$</td>
<td>$\sigma_1^y$</td>
<td>$\sigma_1^z$</td>
</tr>
<tr>
<td>2</td>
<td>$-\sigma_2^x$</td>
<td>$\sigma_2^y$</td>
<td>$-\sigma_2^z$</td>
</tr>
<tr>
<td>3</td>
<td>$-\sigma_3^x$</td>
<td>$-\sigma_3^y$</td>
<td>$\sigma_3^z$</td>
</tr>
<tr>
<td>4</td>
<td>$\sigma_4^x$</td>
<td>$-\sigma_4^y$</td>
<td>$-\sigma_4^z$</td>
</tr>
</tbody>
</table>

Fig. 11(a) illustrates a representative zigzag order with wave vector $\text{M}_2$ and its $\mathcal{T}_4$-transformed counterpart, the phase with coexisting AFM and zigzag orders. In the latter, the spin $x$ components form a Néel AFM pattern, while the spin $y$ and spin $z$ components form zigzag patterns with different wave vectors. Fig. 11(b) shows a stripe order with wave vector $\text{M}_2'$ and the corresponding $\mathcal{T}_4$-transformed phase with coexisting FM and stripe orders. In this case, the spin $x$ components form a uniform FM pattern, whereas the spin $y$ and spin $z$ components form stripe patterns with different wave vectors. It should be noted that, from energetic considerations, the spin $z$ components in the zigzag (with an FM Kitaev interaction) and stripe orders (with an AFM Kitaev interaction) shown in Fig. 11 are expected to vanish.

## Appendix C: Matrix elements in the $\mathcal{R}_{J_3}$-induced Raman response

In this section, we derive the expression for the matter-fermion matrix elements appearing in Eqs. (35) and (43a) to (43d).

First, we discuss those from $C^{4\text{v}}$. The Hamiltonian $H_0^a + V^{4\text{v}}$ can be represented in terms of the Bogoliubov

quasiparticle $\alpha_i$ of $H_0^a$:

$$
H_0^a + V^{4\mathrm{v}} = \frac{1}{2}
\left(
\alpha_1^\dagger, \dots, \alpha_1, \dots
\right)
h^{4\mathrm{v}}
\begin{pmatrix}
\alpha_1 \\
\vdots \\
\alpha_1^\dagger \\
\vdots
\end{pmatrix}
, \tag{C1}
$$

$$
h^{4\mathrm{v}} =
\begin{pmatrix}
u & v^* \\
v & u^*
\end{pmatrix}
\begin{pmatrix}
\epsilon_1^{4\mathrm{v}} & & & \\
& \ddots & & \\
& & -\epsilon_1^{4\mathrm{v}} & \\
& & & \ddots
\end{pmatrix}
\begin{pmatrix}
u^\dagger & v^\dagger \\
v^T & u^T
\end{pmatrix}
, \tag{C2}
$$

$$
\left(
\alpha_{1,4\mathrm{v}}^\dagger, \dots, \alpha_{1,4\mathrm{v}}, \dots
\right)
=
\left(
\alpha_1^\dagger, \dots, \alpha_1, \dots
\right)
\begin{pmatrix}
u \\
v
\end{pmatrix}
. \tag{C3}
$$

Because the ground state $|\Psi_{0,4\mathrm{v}}^a\rangle$ of $H_0^a + V^{4\mathrm{v}}$ has the same fermion parity as $|\Psi_0^a\rangle$, $|\Psi_{0,4\mathrm{v}}^a\rangle$ can be written as a BCS state of $\alpha_i$ [64]:

$$
|\Psi_{0,4\mathrm{v}}^a\rangle = \sqrt{|\det(u)|} \exp\left(
\frac{1}{2} \sum_{i,j} F_{i,j} \alpha_i^\dagger \alpha_j^\dagger
\right) |\Psi_0^a\rangle, \tag{C4}
$$

$$
F = v^* (u^*)^{-1} = -F^T. \tag{C5}
$$

In calculating the matrix element of an operator $O$ between states $|\Psi_0^a\rangle$ and $\exp\left(
\frac{1}{2} \sum_{i,j} F_{i,j} \alpha_i^\dagger \alpha_j^\dagger
\right) |\Psi_0^a\rangle$, it is useful to define

$$
\begin{aligned}
\langle O \rangle &\equiv
\langle \Psi_0^a | O \exp\left(
\frac{1}{2} \sum_{i,j} F_{i,j} \alpha_i^\dagger \alpha_j^\dagger
\right) | \Psi_0^a \rangle / \mathcal{Z}, \\
\mathcal{Z} &=
\langle \Psi_0^a | \exp\left(
\frac{1}{2} \sum_{i,j} F_{i,j} \alpha_i^\dagger \alpha_j^\dagger
\right) | \Psi_0^a \rangle = 1. \tag{C6}
\end{aligned}
$$

There is then

$$
\left\langle
\begin{pmatrix}
\alpha_1^\dagger \\
\vdots \\
\alpha_1 \\
\vdots
\end{pmatrix}
\right)
\left(
\alpha_1^\dagger, \dots, \alpha_1, \dots
\right)
\rangle
=
\begin{pmatrix}
0 & 0 \\
\mathbb{I}_N & -F
\end{pmatrix}
. \tag{C7}
$$

Expressing $\alpha_{i,4\mathrm{v}}^\dagger$ as a linear combination of $\alpha_i$ and $\alpha_i^\dagger$, and then applying Eq. (C7), one obtains

$$
\begin{aligned}
& \langle \Psi_0^a | \alpha_{i,4\mathrm{v}}^\dagger \alpha_{j,4\mathrm{v}}^\dagger | \Psi_{0,4\mathrm{v}}^a \rangle \\
& = \sqrt{|\det(u)|}
\left(
u_{1,i}, \dots, u_{N,i}, v_{1,i}, \dots, v_{N,i}
\right) \\
& \begin{pmatrix}
0 & 0 \\
\mathbb{I}_N & -F
\end{pmatrix}
\begin{pmatrix}
u_{1,j} \\
\vdots \\
u_{N,j} \\
v_{1,j} \\
\vdots \\
v_{N,j}
\end{pmatrix}
. \tag{C8}
\end{aligned}
$$

Next, we discuss the matrix elements in $C^{2\mathrm{v}}$. As an example, we consider $H_0^a + V_1^{2\mathrm{v}}$; the results for $H_0^a + V_2^{2\mathrm{v}}$ can be obtained in the same way. For brevity, we denote the ground state of $H_0^a + V_1^{2\mathrm{v}}$ by $|\Psi_{0,2\mathrm{v}}^a\rangle$, and its Bogoliubov quasiparticle by $\alpha_{i,2\mathrm{v}}$. Because the ground state $|\Psi_{0,2\mathrm{v}}^a\rangle$ has opposite fermion parity relative to $|\Psi_0^a\rangle$, it cannot be written as a BCS state of $\alpha_i$. By contrast, any single-quasiparticle excited state $\alpha_{i,2\mathrm{v}}^\dagger |\Psi_{0,2\mathrm{v}}^a\rangle$ has the same parity as $|\Psi_0^a\rangle$ and therefore can be represented as a BCS state of $\alpha_i$. Here we take the first excited state $|\Psi_{1,2\mathrm{v}}^a\rangle \equiv \alpha_{1,2\mathrm{v}}^\dagger |\Psi_{0,2\mathrm{v}}^a\rangle$ as a reference state and express it as BCS state of $\alpha_i$. Any single-quasiparticle state can then be written as $\alpha_{l,2\mathrm{v}}^\dagger |\Psi_{0,2\mathrm{v}}^a\rangle = \alpha_{l,2\mathrm{v}}^\dagger \alpha_{1,2\mathrm{v}} |\Psi_{1,2\mathrm{v}}^a\rangle$ ($l=1,\dots,N$).

$H_0^a + V^{2\mathrm{v}}$ can be written as

$$
H_0^a + V^{2\mathrm{v}} = \frac{1}{2}
\left(
\alpha_1^\dagger, \dots, \alpha_1, \dots
\right)
h^{2\mathrm{v}}
\begin{pmatrix}
\alpha_1 \\
\vdots \\
\alpha_1^\dagger \\
\vdots
\end{pmatrix}
, \tag{C9}
$$

$$
h^{2\mathrm{v}} =
\begin{pmatrix}
\tilde{u} & \tilde{v}^* \\
\tilde{v} & \tilde{u}^*
\end{pmatrix}
\begin{pmatrix}
\epsilon_1^{2\mathrm{v}} & & & \\
& \ddots & & \\
& & -\epsilon_1^{2\mathrm{v}} & \\
& & & \ddots
\end{pmatrix}
\begin{pmatrix}
\tilde{u}^\dagger & \tilde{v}^\dagger \\
\tilde{v}^T & \tilde{u}^T
\end{pmatrix}
, \tag{C10}
$$

$$
\left(
\alpha_{1,2\mathrm{v}}^\dagger, \dots, \alpha_{1,2\mathrm{v}}, \dots
\right)
=
\left(
\alpha_1^\dagger, \dots, \alpha_1, \dots
\right)
\begin{pmatrix}
\tilde{u} \\
\tilde{v}
\end{pmatrix}
. \tag{C11}
$$

In order to represent $|\Psi_{1,2\mathrm{v}}^a\rangle$ as a BCS state of $\alpha_i$, one needs to construct a new BdG Hamiltonian $H'$ whose ground state is $|\Psi_{1,2\mathrm{v}}^a\rangle$. This can be done by simply replacing $\epsilon_1^{2\mathrm{v}} \to -\epsilon_1^{2\mathrm{v}}$ in Eq. (C10), which gives rise to

$$
\begin{aligned}
H' =&\frac{1}{2}
\left(
\alpha_1^\dagger, \dots, \alpha_1, \dots
\right)
\begin{pmatrix}
\tilde{u}' & \tilde{v}'^* \\
\tilde{v}' & \tilde{u}'^*
\end{pmatrix}
\begin{pmatrix}
\epsilon_1^{2\mathrm{v}} & & & \\
& \ddots & & \\
& & -\epsilon_1^{2\mathrm{v}} & \\
& & & \ddots
\end{pmatrix} \\
&\begin{pmatrix}
\tilde{u}'^\dagger & \tilde{v}'^\dagger \\
\tilde{v}'^T & \tilde{u}'^T
\end{pmatrix}
\begin{pmatrix}
\alpha_1 \\
\vdots \\
\alpha_1^\dagger \\
\vdots
\end{pmatrix}
. \tag{C12}
\end{aligned}
$$

The $\tilde{u}'$ and $\tilde{v}'$ are related to $\tilde{u}$ and $\tilde{v}$ through

$$
\tilde{u}' =
\begin{pmatrix}
\tilde{v}_{1,1}^* & \tilde{u}_{1,2} & \dots & \tilde{u}_{1,N} \\
\vdots & \vdots & \ddots & \vdots \\
\tilde{v}_{N,1}^* & \tilde{u}_{N,2} & \dots & \tilde{u}_{N,N}
\end{pmatrix}
, \tag{C13}
$$

$$
\tilde{v}' =
\begin{pmatrix}
\tilde{u}_{1,1}^* & \tilde{v}_{1,2} & \dots & \tilde{v}_{1,N} \\
\vdots & \vdots & \ddots & \vdots \\
\tilde{u}_{N,1}^* & \tilde{v}_{N,2} & \dots & \tilde{v}_{N,N}
\end{pmatrix}
. \tag{C14}
$$

As the ground state of $H'$, $|\Psi_{1,2\mathrm{v}}^a\rangle$ can be written as

$$
\begin{aligned}
|\Psi_{1,2\mathrm{v}}^a\rangle &\equiv \alpha_{1,2\mathrm{v}}^\dagger|\Psi_{0,2\mathrm{v}}^a\rangle \\
&= \sqrt{|\det(\tilde{u}')|} \exp\bigl(\frac{1}{2} \sum_{i,j} \tilde{F}_{i,j}' \alpha_i^\dagger \alpha_j^\dagger\bigr)|\Psi_0^a\rangle, \quad \mathrm{(C15)}
\end{aligned}
$$

$$
\tilde{F}' = \tilde{v}'{}^* (\tilde{u}'{}^*)^{-1}. \tag{C16}
$$

Using Eq. (C7), with the replacement $F \to \tilde{F}'$, one ob-
tains

$$
\begin{aligned}
&\langle\Psi_0^a|\alpha_{l,2\mathrm{v}}^\dagger|\Psi_{0,2\mathrm{v}}^a\rangle \\
&= \langle\Psi_0^a|\alpha_{l,2\mathrm{v}}^\dagger \alpha_{1,2\mathrm{v}}|\Psi_{1,2\mathrm{v}}^a\rangle \\
&= \sqrt{|\det(\tilde{u}')|}(\tilde{u}_{1,l}, \dots, \tilde{u}_{N,l}, \tilde{v}_{1,l}, \dots, \tilde{v}_{N,l}) \\
&\qquad \begin{pmatrix} 0 & 0 \\ \mathbb{1}_N & \tilde{F}' \end{pmatrix} \begin{pmatrix} \tilde{v}_{1,1}^* \\ \vdots \\ \tilde{v}_{N,1}^* \\ \tilde{u}_{1,1}^* \\ \vdots \\ \tilde{u}_{N,1}^* \end{pmatrix}. \tag{C17}
\end{aligned}
$$

The multi-fermion matrix elements in Eqs. (43b)
and (43c) can be evaluated using a generalized Wick's
theorem [65].

$$
\begin{aligned}
&\langle\Psi_0^a|\gamma_{i_1,0} \gamma_{i_2,0} \gamma_{i_3,0} \gamma_{i_4,0} \alpha_{l,2\mathrm{v}}^\dagger \alpha_{1,2\mathrm{v}} \exp\bigl(\frac{1}{2} \sum_{i,j} \tilde{F}_{i,j}' \alpha_i^\dagger \alpha_j^\dagger\bigr)|\Psi_0^a\rangle \\
&= \mathcal{Z} \langle\gamma_{i_1,0} \gamma_{i_2,0} \gamma_{i_3,0} \gamma_{i_4,0} \alpha_{l,2\mathrm{v}}^\dagger \alpha_{1,2\mathrm{v}}\rangle \\
&= \mathcal{Z} \bigl[\langle\gamma_{i_1,0} \gamma_{i_2,0}\rangle\langle\gamma_{i_3,0} \gamma_{i_4,0}\rangle\langle\alpha_{l,2\mathrm{v}}^\dagger \alpha_{1,2\mathrm{v}}\rangle \\
&+ (-1)\langle\gamma_{i_1,0} \gamma_{i_2,0}\rangle\langle\gamma_{i_3,0} \alpha_{l,2\mathrm{v}}^\dagger\rangle\langle\gamma_{i_4,0} \alpha_{1,2\mathrm{v}}\rangle + \dots\bigr]. \quad \mathrm{(C18)}
\end{aligned}
$$

In total, there are 15 possible contractions in Eq. (C18).
The expectation value of each fermion bilinear can be
evaluated by first expressing the fermionic operators as
linear combinations of $\alpha_i$ and $\alpha_i^\dagger$, and then applying
Eq. (C7).

---

[1] P. A. Lee, N. Nagaosa, and X. G. Wen, Doping a mott in-
sulator: Physics of high-temperature superconductivity,
Rev. Mod. Phys. **78**, 17 (2006).

[2] L. Balents, Spin liquids in frustrated magnets, *Nature*
**464**, 199 (2010).

[3] L. Savary and L. Balents, Quantum spin liquids: a re-
view, Rep. Prog. Phys. **80**, 016502 (2017).

[4] Y. Zhou, K. Kanoda, and T.-K. Ng, Quantum spin liquid
states, Rev. Mod. Phys. **89**, 025003 (2017).

[5] C. Broholm, R. J. Cava, S. A. Kivelson, D. G. Nocera,
M. R. Norman, and T. Senthil, Quantum spin liquids,
*Science* **367**, 10.1126/science.aay0668 (2020).

[6] A. Kitaev, Anyons in an exactly solved model and be-
yond, *Ann. Phys. (N. Y.)* **321**, 2 (2006).

[7] G. Jackeli and G. Khaliullin, Mott insulators in the
strong spin-orbit coupling limit: from heisenberg to a
quantum compass and kitaev models, *Phys. Rev. Lett.*
**102**, 017205 (2009).

[8] M. Hermanns, I. Kimchi, and J. Knolle, Physics of the ki-
taev model: Fractionalization, dynamic correlations, and
material connections, *Annu. Rev. Condens. Matter Phys.*
**9**, 17 (2018).

[9] J. Knolle and R. Moessner, A field guide to spin liquids,
*Annu. Rev. Condens. Matter Phys.* **10**, 451 (2019).

[10] H. Takagi, T. Takayama, G. Jackeli, G. Khaliullin, and
S. E. Nagler, Concept and realization of kitaev quantum
spin liquids, *Nature Reviews Physics* **1**, 264 (2019).

[11] S. Trebst and C. Hickey, Kitaev materials, *Physics Re-
ports* **950**, 1 (2022).

[12] I. Rousochatzakis, N. B. Perkins, Q. Luo, and H.-Y. Kee,
Beyond kitaev physics in strong spin-orbit coupled mag-
nets, *Rep. Prog. Phys.* **87**, 026502 (2024).

[13] Y. Matsuda, T. Shibauchi, and H.-Y. Kee, Kitaev quan-
tum spin liquids, Rev. Mod. Phys. **97**, 045003 (2025).

[14] A. Banerjee, C. A. Bridges, J.-Q. Yan, A. A. Aczel, L. Li,
M. B. Stone, G. E. Granroth, M. D. Lumsden, Y. Yiu,
J. Knolle, S. Bhattacharjee, D. L. Kovrizhin, R. Moess-
ner, D. A. Tennant, D. G. Mandrus, and S. E. Nagler,
Proximate kitaev quantum spin liquid behaviour in a
honeycomb magnet, *Nat. Mater.* **15**, 733 (2016).

[15] A. Banerjee, J. Yan, J. Knolle, C. A. Bridges, M. B.
Stone, M. D. Lumsden, D. G. Mandrus, D. A. Tennant,
R. Moessner, and S. E. Nagler, Neutron scattering in the
proximate quantum spin liquid $\alpha$-RuCl$_3$, *Science* **356**,
1055 (2017).

[16] A. Banerjee, P. Lampen-Kelley, J. Knolle, C. Balz, A. A.
Aczel, B. Winn, Y. Liu, D. Pajerowski, J. Yan, C. A.
Bridges, A. T. Savici, B. C. Chakoumakos, M. D. Lums-
den, D. A. Tennant, R. Moessner, D. G. Mandrus, and
S. E. Nagler, Excitations in the field-induced quantum

spin liquid state of $\alpha$-RuCl₃, npj Quantum Materials 3,
1 (2018).

[17] Y. Kasahara, T. Ohnishi, Y. Mizukami, O. Tanaka,
S. Ma, K. Sugii, N. Kurita, H. Tanaka, J. Nasu, Y. Mo-
tome, T. Shibauchi, and Y. Matsuda, Majorana quanti-
zation and half-integer thermal quantum hall effect in a
kitaev spin liquid, Nature 559, 227 (2018), 1805.05022.

[18] T. Yokoi, S. Ma, Y. Kasahara, S. Kasahara, T. Shibauchi,
N. Kurita, H. Tanaka, J. Nasu, Y. Motome, C. Hickey,
S. Trebst, and Y. Matsuda, Half-integer quantized
anomalous thermal hall effect in the kitaev material can-
didate $\alpha$-RuCl₃, Science 373, 568 (2021).

[19] P. Czajka, T. Gao, M. Hirschberger, P. Lampen-Kelley,
A. Banerjee, J. Yan, D. G. Mandrus, S. E. Nagler, and
N. P. Ong, Oscillations of the thermal conductivity in the
spin-liquid state of $\alpha$-RuCl₃, Nat. Phys. 17, 915 (2021).

[20] P. Czajka, T. Gao, M. Hirschberger, P. Lampen-Kelley,
A. Banerjee, N. Quirk, D. G. Mandrus, S. E. Nagler,
and N. P. Ong, Planar thermal hall effect of topological
bosons in the kitaev magnet $\alpha$-RuCl₃, Nat. Mater. 22,
36 (2023).

[21] E. Lefrançois, G. Grissonnanche, J. Baglo, P. Lampen-
Kelley, J.-Q. Yan, C. Balz, D. Mandrus, S. E. Nagler,
S. Kim, Y.-J. Kim, N. Doiron-Leyraud, and L. Taillefer,
Evidence of a phonon hall effect in the kitaev spin liquid
candidate $\alpha$-RuCl₃, Phys. Rev. X 12, 021025 (2022).

[22] E. Lefrançois, J. Baglo, Q. Barthélemy, S. Kim, Y.-J.
Kim, and L. Taillefer, Oscillations in the magnetothermal
conductivity of $\alpha$-RuCl₃: Evidence of transition anoma-
lies, Phys. Rev. B 107, 064408 (2023).

[23] I. S. Villadiego, Pseudoscalar U(1) spin liquids in $\alpha$-
RuCl₃, Phys. Rev. B 104, 195149 (2021).

[24] L. E. Chern, E. Z. Zhang, and Y. B. Kim, Sign structure
of thermal hall conductivity and topological magnons for
in-plane field polarized kitaev magnets, Phys. Rev. Lett.
126, 147201 (2021).

[25] J. Chaloupka, G. Jackeli, and G. Khaliullin, Kitaev-
heisenberg model on a honeycomb lattice: possible exotic
phases in iridium oxides A₂IrO₃, Phys. Rev. Lett. 105,
027204 (2010).

[26] J. Chaloupka, G. Jackeli, and G. Khaliullin, Zigzag mag-
netic order in the iridium oxide Na₂IrO₃, Phys. Rev. Lett.
110, 097204 (2013).

[27] I. Kimchi and Y.-Z. You, Kitaev-heisenberg-J₂-J₃ model
for the iridates A₂IrO₃, Phys. Rev. B 84, 180407 (2011).

[28] J. Knolle, S. Bhattacharjee, and R. Moessner, Dy-
namics of a quantum spin liquid beyond integrability:
The kitaev-heisenberg-$\gamma$ model in an augmented parton
mean-field theory, Phys. Rev. B 97, 134432 (2018).

[29] J. G. Rau, E. K.-H. Lee, and H.-Y. Kee, Generic spin
model for the honeycomb iridates beyond the kitaev
limit, Phys. Rev. Lett. 112, 077204 (2014).

[30] J. S. Gordon, A. Catuneanu, E. S. Sørensen, and H.-Y.
Kee, Theory of the field-revealed kitaev spin liquid, Nat.
Commun. 10, 2470 (2019).

[31] E. S. Sørensen, A. Catuneanu, J. S. Gordon, and H.-Y.
Kee, Heart of entanglement: Chiral, nematic, and incom-
mensurate phases in the kitaev-gamma ladder in a field,
Phys. Rev. X 11, 011013 (2021).

[32] H.-Y. Lee, R. Kaneko, L. E. Chern, T. Okubo, Y. Yamaji,
N. Kawashima, and Y. B. Kim, Magnetic field induced
quantum phases in a tensor network study of kitaev mag-
nets, Nat. Commun. 11, 1639 (2020).

[33] J. Wang, B. Normand, and Z.-X. Liu, One proximate
kitaev spin liquid in the K-J-$\Gamma$ model on the honeycomb
lattice, Phys. Rev. Lett. 123, 197201 (2019).

[34] J. Wang, B. Normand, and Z.-X. Liu, Multinode quan-
tum spin liquids in extended kitaev honeycomb models,
npj Quantum Mater. 9, 1 (2024).

[35] S.-S. Zhang, G. B. Halász, W. Zhu, and C. D. Batista,
Variational study of the kitaev-heisenberg-gamma model,
Phys. Rev. B 104, 014411 (2021).

[36] C. Chen and I. S. Villadiego, Anyon polarons as
a window into the competing phases of the Kitaev-
Gamma-Gamma' model, arXiv [cond-mat.str-el] (2025),
arXiv:2508.21129.

[37] P. A. Maksimov and A. L. Chernyshev, Rethinking $\alpha$-
RuCl₃, Phys. Rev. Res. 2, 033011 (2020).

[38] M. Möller, P. A. Maksimov, S. Jiang, S. R. White,
R. Valenti, and A. L. Chernyshev, The saga of $\alpha$-RuCl₃:
Parameters, models, and phase diagrams, arXiv [cond-
mat.str-el] (2025), arXiv:2502.08698.

[39] S. K. Choi, R. Coldea, A. N. Kolmogorov, T. Lancaster,
I. I. Mazin, S. J. Blundell, P. G. Radaelli, Y. Singh,
P. Gegenwart, K. R. Choi, S.-W. Cheong, P. J. Baker,
C. Stock, and J. Taylor, Spin waves and revised crystal
structure of honeycomb iridate Na₂IrO₃, Phys. Rev. Lett.
108, 127204 (2012).

[40] Y. Singh, S. Manni, J. Reuther, T. Berlijn, R. Thomale,
W. Ku, S. Trebst, and P. Gegenwart, Relevance of the
heisenberg-kitaev model for the honeycomb lattice iri-
dates A₂IrO₃, Phys. Rev. Lett. 108, 127203 (2012).

[41] C. Kim, J. Jeong, G. Lin, P. Park, T. Masuda, S. Asai,
S. Itoh, H.-S. Kim, H. Zhou, J. Ma, and J.-G. Park, An-
tiferromagnetic Kitaev interaction in $J_{eff}=1/2$ cobalt
honeycomb materials Na₃Co₂SbO₆ and Na₂Co₂TeO₆, J.
Phys.: Condens. Matter 34, 045802 (2021).

[42] B. H. Kim, S. Sota, T. Shirakawa, S. Yunoki, and Y.-W.
Son, Proximate kitaev system for an intermediate mag-
netic phase in in-plane magnetic fields, Phys. Rev. B.
102, 140402 (2020).

[43] G. Lin, J. Jeong, C. Kim, Y. Wang, Q. Huang, T. Ma-
suda, S. Asai, S. Itoh, G. Günther, M. Russina, Z. Lu,
J. Sheng, L. Wang, J. Wang, G. Wang, Q. Ren, C. Xi,
W. Tong, L. Ling, Z. Liu, L. Wu, J. Mei, Z. Qu, H. Zhou,
X. Wang, J.-G. Park, Y. Wan, and J. Ma, Field-induced
quantum spin disordered state in spin-1/2 honeycomb
magnet Na₂Co₂TeO₆, Nat. Commun. 12, 5559 (2021).

[44] W. Yao, K. Iida, K. Kamazawa, and Y. Li, Excitations in
the ordered and paramagnetic states of honeycomb mag-
net Na₂Co₂TeO₆, Phys. Rev. Lett. 129, 147202 (2022).

[45] M. Songvilay, J. Robert, S. Petit, J. A. Rodriguez-Rivera,
W. D. Ratcliff, F. Damay, V. Balédent, M. Jiménez-Ruiz,
P. Lejay, E. Pachoud, A. Hadj-Azzem, V. Simonet, and
C. Stock, Kitaev interactions in the Co honeycomb anti-
ferromagnets Na₃Co₂SbO₆ and Na₂Co₂TeO₆, Phys. Rev.
B 102, 224429 (2020).

[46] A. M. Samarakoon, Q. Chen, H. Zhou, and V. O. Garlea,
Static and dynamic magnetic properties of honeycomb
lattice antiferromagnets Na₂M₂TeO₆, $M=$ Co and Ni,
Phys. Rev. B 104, 184415 (2021).

[47] A. L. Sanders, R. A. Mole, J. Liu, A. J. Brown, D. Yu,
C. D. Ling, and S. Rachel, Dominant Kitaev inter-
actions in the honeycomb materials Na₃Co₂SbO₆ and
Na₂Co₂TeO₆, Phys. Rev. B 106, 014413 (2022).

[48] G. Lin, M. Shu, Q. Zhao, G. Li, Y. Ma, J. Jiao, Y. Li,
G. Duan, Q. Huang, J. Sheng, et al., Evidence for
field induced quantum spin liquid behavior in a spin-

1/2 honeycomb magnet, The Innovation Materials 2,
10.59717/j.xinn-mater.2024.100082 (2024).

[49] P. Rao, R. Moessner, and J. Knolle, Dynamical response theory of interacting majorana fermions and its appli- cation to generic kitaev quantum spin liquids in a field, Phys. Rev. B. 112, 024440 (2025).

[50] J. Knolle, G.-W. Chern, D. L. Kovrizhin, R. Moessner, and N. B. Perkins, Raman scattering signatures of kitaev spin liquids in $A_2IrO_3$ iridates with A=Na or Li, Phys. Rev. Lett. 113, 187201 (2014).

[51] J. Nasu, J. Knolle, D. L. Kovrizhin, Y. Motome, and R. Moessner, Fermionic response from fractionalization in an insulating two-dimensional magnet, Nat. Phys. 12, 912 (2016).

[52] L. Zou and Y.-C. He, Field-induced $QCD_3$-chern-simons quantum criticalities in kitaev materials, Phys. Rev. Res. 2, 013072 (2020).

[53] J. Knolle, D. L. Kovrizhin, J. T. Chalker, and R. Moess- ner, Dynamics of a two-dimensional quantum spin liquid: Signatures of emergent majorana fermions and fluxes, Phys. Rev. Lett. 112, 207203 (2014).

[54] J. Knolle, D. L. Kovrizhin, J. T. Chalker, and R. Moess- ner, Dynamics of fractionalization in quantum spin liq- uids, Phys. Rev. B. 92, 115127 (2015).

[55] X.-G. Wen, Quantum orders and symmetric spin liquids, Phys. Rev. B. 65, 165113 (2002).

[56] Y.-Z. You, I. Kimchi, and A. Vishwanath, Doping a spin- orbit mott insulator: Topological superconductivity from the kitaev-heisenberg model and possible application to ($Na_2/Li_2$)$IrO_3$, Phys. Rev. B 86, 085145 (2012).

[57] A. Auerbach, Interacting electrons and quantum mag- netism, 1st ed., Graduate Texts in Contemporary Physics (Springer, New York, NY, 1998).

[58] J. Wang and C. Chen, Manuscript in preparation (2026).

[59] T. P. Devereaux and R. Hackl, Inelastic light scatter- ing from correlated electrons, Rev. Mod. Phys. 79, 175 (2007).

[60] O. Cépas, J. O. Haerter, and C. Lhuillier, Detection of weak emergent broken-symmetries of the kagome anti- ferromagnet by raman spectroscopy, Phys. Rev. B. 77, 172406 (2008).

[61] P. A. Fleury and R. Loudon, Scattering of light by one- and two-magnon excitations, Phys. Rev. 166, 514 (1968).

[62] The multi-$\gamma_0$ correlation function scales with a higher power of the density of states of the matter fermions. Consequently, terms involving higher-order $\gamma_0$ correlators mainly contribute to a broad continuum and are strongly suppressed at low energies [50].

[63] In calculating the spin DSF of the Kitaev model, this type of approximation has been shown to reproduce the exact results accurately [50, 54].

[64] L. M. Robledo, Sign of the overlap of hartree-fock- bogoliubov wave functions, Phys. Rev. C 79, 021302 (2009).

[65] P. Ring and P. Schuck, The nuclear many-body problem, Theoretical and Mathematical Physics (Springer, Berlin, Germany, 2004).