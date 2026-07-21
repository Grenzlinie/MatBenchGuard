# Eccentricity valley Hall effect

Jin Cao, $^1$ Shen Lai, $^2$ Cong Xiao, $^{3,*}$ Qian Niu, $^4$ and Shengyuan A. Yang $^{1,\dagger}$

$^1$ Research Laboratory for Quantum Materials, Department of Applied Physics,
The Hong Kong Polytechnic University, Kowloon, Hong Kong, China
$^2$ Institute of Applied Physics and Materials Engineering,
Faculty of Science and Technology, University of Macau, Macau, China
$^3$ Interdisciplinary Center for Theoretical Physics and Information
Sciences (ICTPIS), Fudan University, Shanghai 200433, China
$^4$ Department of Physics, University of Science and Technology of China, Hefei, Anhui 230026, China

Valleytronics harnesses the valley degree of freedom — energy-degenerate extrema in the electronic band structure — for information storage and processing. Valley Hall effect (VHE) is a cornerstone of valleytronics, enabling electric generation of pure valley currents. While extensively studied in systems with valleys located at time-reversal-breaking points, here, we shift the paradigm to valleytronic platforms with time-reversal-invariant valleys (TRIVs), revealing a novel phenomenon: eccentricity VHE. Unlike conventional VHE, the valley Hall angle for eccentricity VHE is an intrinsic geometric property, governed solely by the eccentricity of the valley Fermi surface, rendering it highly robust against variations in temperature or carrier density. Eccentricity VHE emerges universally across all 25 layer groups supporting TRIVs. We demonstrate these distinctive features in monolayer $\text{GeS}_2$ via first-principles calculations, predicting a significant valley Hall angle of 0.74. This effect can be detected through nonlocal transport measurements exhibiting characteristic scaling behavior, or, in certain cases, through valley-layer coupling. Our findings reveal a critical overlooked facet of valley Hall physics, transcend the established VHE paradigm, and significantly broadens the scope of valleytronics.

In the valley Hall effect (VHE), a longitudinal charge current $j_{\parallel}^c$ induces a valley current $j_{\perp}^v$ flowing in the transverse direction, as illustrated in Fig. 1a, providing a key mechanism for purely electrical charge-valley conversion [1–8]. To date, the research on VHE, as well as the whole valleytronics field, has primarily focused on two-dimensional (2D) hexagonal-lattice materials, with graphene and transition metal dichalcogenides serving as paradigmatic examples [1–18]. In these conventional valleytronic systems, the two valleys reside at the corners $K$ and $K'$ of the hexagonal Brillouin zone. They are related by the time-reversal symmetry $\mathcal{T}$, yet each lies at a momentum point that does not preserve $\mathcal{T}$ (see Fig. 1b). The VHE in such systems requires breaking inversion symmetry $\mathcal{P}$, and it acquires a Berry-phase contribution [1, 2]. The associated valley Hall angle $\theta_{\text{VH}} \equiv |j_{\perp}^v/j_{\parallel}^c|$, a key indicator of VHE efficiency, scales as $\tau^{-1}$ with the scattering time $\tau$, and depends sensitively on parameters such as temperature and carrier density [4–6].

Here, we propose a paradigm shift to a novel class of valleytronic platforms featuring time-reversal-invariant valleys (TRIVs), where the valleys reside at $\mathcal{T}$-invariant momentum points (see Fig. 1c). In contrast to conventional valleytronic systems, each TRIV is preserved under $\mathcal{T}$ (and $\mathcal{P}$) operation, leading to profound differences in valley properties. Crucially, valley transport is no longer prohibited by $\mathcal{P}$ symmetry. More importantly, symmetry dictates that it arises from fundamentally distinct microscopic mechanisms. We predict a novel eccentricity VHE, in which the valley Hall angle $\theta_{\text{VH}}$ is governed solely by an *intrinsic geometric parameter* — the eccentricity $\mathfrak{e}$ of valley Fermi surface. As a result, $\theta_{\text{VH}}$ becomes independent of scattering time $\tau$ and exhibits exceptional robustness against variations in temperature and carrier density. Symmetry analysis further reveals that eccentricity VHE is universal across all 25 layer groups compatible with TRIVs. These distinctive features are explicitly demonstrated in monolayer $\text{GeS}_2$, where we predict a giant $\theta_{\text{VH}} \sim 0.74$. Experimental signatures of eccentricity VHE can be identified through its unique scaling behavior in nonlocal transport or via gate-field control through valley-layer coupling. Our proposal uncovers a previously unexplored frontier in valleytronics and may open the door to extensive research in related directions.

Symmetry character of VHE. Let us consider a 2D nonmagnetic system having two and only two energy-degenerate valleys, labeled as $V_1$ and $V_2$. Such systems can be fully classified into two categories: (i) those with $\mathcal{T}$-connected valleys and (ii) those with TRIVs. Category (i) just corresponds to the conventional case.

Consider the valley current driven by applied $E$ field: $j_a^v \equiv j_a^{V_1} - j_a^{V_2} = \sum_b \sigma_{ab}^v E_b$, where roman subscripts denote Cartesian components, $j^{V_i}$ is the current from carriers in valley $V_i$, and the valley conductivity

$$
\sigma^v = \sigma^{V_1} - \sigma^{V_2}, \tag{1}
$$

with $\sigma^{V_i}$ being the valley-resolved charge conductivity. Since the system respects $\mathcal{T}$ symmetry, the overall response coefficients must be even under $\mathcal{T}$ operation, e.g., $\sigma^v$ is a $\mathcal{T}$-even quantity. Nevertheless, the valley-resolved quantities like $\sigma^{V_i}$ is not constrained to have a definite parity under $\mathcal{T}$; in general, it contains both $\mathcal{T}$-even and $\mathcal{T}$-odd components, which have the following transforma-

![](./images/1240640232739569680_1.jpg)

FIG. 1. Valley Hall effect and two categories of valleytronic systems. a, In VHE, a longitudinal charge current $j_{\parallel}^c$ drives a transverse valley current $j_{\perp}^v$. The blue and red spheres denote electrons from two different valleys $V_1$ and $V_2$. b, Conventional valleytronic systems, such as graphene and transition metal dichalcognides materials, have a pair of valleys located at $K$ and $K'$ points of the hexagonal Brillouin zone. The two valleys are related by time-reversal $\mathcal{T}$, yet each valley is at a $k$ point that does not preserve $\mathcal{T}$. c, Valleytronic system with time-reversal-invariant valleys (TRIVs). Each valley here resides at a $\mathcal{T}$-invariant momentum point. The two valleys are not related by $\mathcal{T}$ but by some crystalline symmetry $\mathcal{Q}$.

tion behavior under $\mathcal{T}$:
$$
\mathcal{T}: \sigma_{\eta}^{V_i} \rightleftharpoons \eta \sigma_{\eta}^{\mathcal{T} V_i}, \tag{2}
$$
where $\eta=\pm$ for $\mathcal{T}$-even/odd component.

Now, one can see why the two categories make a salient difference here. For the conventional category (i) systems, $\mathcal{T}$ switches the two valleys, i.e., $\mathcal{T} V_1=V_2$. Since $\sigma^v$ is odd under switch of valley indices, one finds only the $\mathcal{T}$-odd component $\sigma_{-}^{V_i}$ of $\sigma^{V_i}$ contributes to $\sigma^v$, and we have $\sigma^v=2\sigma_{-}^{V_1}$.

In contrast, for category (ii) with TRIVs, $\mathcal{T}$ operation preserves each valley, i.e., $\mathcal{T} V_i=V_i$. It follows from (2) that $\sigma^{V_i}$ contains only $\mathcal{T}$-even component, so only $\mathcal{T}$-even contributions enter the valley conductivity $\sigma^v$, and we may write $\sigma^v=\sigma_{+}^{V_1}-\sigma_{+}^{V_2}$.

The revealed distinct symmetry characters indicate valley transport in the two categories must involve distinct mechanisms. For example, it is well known that the conventional VHE, which occurs in category (i) systems, contains a Berry-phase contribution [1], which is indeed $\mathcal{T}$-odd in each valley. However, it cannot contribute to VHE in category (ii) TRIV systems. Instead, we shall show below that valley transport in TRIV systems is mainly from the Drude contribution.

In addition, the two categories also exhibit distinct behaviors in the presence of inversion symmetry. For category (i), the constraint of $\mathcal{P}$ requires $\sigma^{V_1}=\sigma^{V_2}$, so a nonzero valley transport must require the breaking of $\mathcal{P}$ symmetry, as is well-known for conventional VHE. In comparison, $\mathcal{P}$ has no constraint on $\sigma^v$ in category (ii), indicating that VHE can in principle be realized in TRIV systems with preserved $\mathcal{P}$ symmetry. This point will be confirmed in a while.

*Eccentricity VHE.* For TRIV systems, we predict a new type of VHE. Remarkably, not only the response structure but also the expression of this VHE have a rather generic form, leading to a purely geometric valley Hall angle.

Without loss of generality, let us consider TRIVs at conduction band bottom of a semiconductor band structure. Constrained by $\mathcal{T}$ symmetry, the effective Hamiltonian $\mathcal{H}^{V_1}$ expanded around the center of valley $V_1$ is generally of a quadratic form in the momenta $\boldsymbol{k}=(k_x,k_y)$. By choosing proper coordinate axis, one can always diagonalize this form, after which $\mathcal{H}^{V_1}$ takes the following generic form
$$
\mathcal{H}^{V_1}=k_x^2/a_x^2+k_y^2/a_y^2-\mu, \tag{3}
$$
where parameters $a_x$ and $a_y$ manifest the effective mass along the two principal axis, and $\mu>0$ is the chemical potential. The generic shape of Fermi surface at such a TRIV is an ellipse, characterized by the ratio $\lambda$ between the semi-major and semi-minor axis. Figure 2(a) shows the case when the semi-major axis is along $y$, for which $\lambda=a_y/a_x$.

The $\mathcal{T}$-even $\sigma_{+}^{V_1}$, which is the component that can contribute to valley transport for TRIVs, is dominated by the Drude contribution. It is expressed as (we drop the subscript $+$ below and take $e=\hbar=1$) $\sigma_{ab}^{V_i}=-\tau \int_{V_i} v_a \partial_b f_0$, where $v_a$ is the band velocity, and $f_0$ is the Fermi distribution. For $V_1$ described by Eq. (3), one easily obtains $(\sigma_{xx}^{V_1},\sigma_{yy}^{V_1})=\frac{1}{2\pi}\mu\tau(\lambda,\lambda^{-1})$.

To have a well-defined binary valley degree of freedom, the other valley $V_2$ must be connected to $V_1$ by some crystalline symmetry $\mathcal{Q}$ (see Fig. 1c). For instance, assume the two valleys are connected by $\mathcal{Q}=C_{4z}$ symmetry (Fig. 2b), then we have $\sigma_{xx}^{V_2}=\sigma_{yy}^{V_1}$ and $\sigma_{yy}^{V_2}=\sigma_{xx}^{V_1}$. Under an in-plane electric field $\boldsymbol{E}=E(\cos\phi,\sin\phi)$, the induced charge current is purely longitudinal, i.e., parallel with $E$ field, given by
$$
j_{\parallel}^c=\frac{1}{2\pi}\mu\tau\left(\lambda+\lambda^{-1}\right)E. \tag{4}
$$

![](./images/1240640232739569680_2.jpg)

FIG. 2. Eccentricity valley Hall effect. a, The generic shape of a TRIV Fermi surface is an ellipse. Its geometry is characterized by the eccentricity $\mathfrak{e}$. Here, we illustrate the case of a TRIV Fermi surface with semi-major axis along $y$. b, Illustration of a pair of TRIVs connected by $\mathcal{Q}=C_{4 z}$ symmetry. Under a driving electric field, the valley-contrasted current response leads to a VHE determined by eccentricity of valley Fermi ellipse. c, The resulting valley Hall angle as a function of $\mathfrak{e}$ and (inset) of the orientation of the applied electric field. d, The eccentricity VHE features a valley Hall angle independent of temperature and chemical potential.

Meanwhile, in the transverse direction, the induced VHE current is

$$
j_{\perp}^{v}=\frac{1}{2 \pi} \mu \tau \sin (2 \phi)\left(\lambda-\lambda^{-1}\right) E, \quad(5)
$$

which exhibits a $\pi$-periodic angular dependence on the field direction.

Remarkably, the valley Hall angle in this case has an especially simple form and can be expressed in terms of the eccentricity $\mathfrak{e}\left(=\sqrt{1-\lambda^{-2}}\right)$ of the valley Fermi surface:

$$
\theta_{\mathrm{VH}}=\frac{\mathfrak{e}^{2}}{2-\mathfrak{e}^{2}}|\sin (2 \phi)| . \quad(6)
$$

This result is purely geometric: For a given driving field direction $\phi, \theta_{\mathrm{VH}}$ is determined by a single parameter $\mathfrak{e}$ describing the valley geometry, independent of doping, scattering time, and other system parameters (Fig. 2d). This contrasts sharply with conventional VHE, which shows the opposite behavior. This remarkable feature is due to the fact that both charge and valley responses here arise from the same mechanism (Drude mechanism here), which naturally leads to their same parametric dependence (on $\mu$ and $\tau$ ). This remarkable behavior originates from the unique character of TRIVs discussed above, i.e., it is now the $\mathcal{T}$-even mechanism, rather than the usual $\mathcal{T}$-odd ones, that contributes to VHE.

<table>
<caption>TABLE I. 2D Bravais lattices and layer groups that are compatible with TRIVs and eccentricity VHE. The second column lists the symmetry $\mathcal{Q}$ that connects the two TRIVs.</caption>
<thead>
  <tr>
    <th>TRIVs</th>
    <th>$\mathcal{Q}$</th>
    <th>Generators of little co-group at each TRIV</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="4">![](./images/1240640232739569680_3.jpg)</td>
    <td>$C_{4z}$</td>
    <td>$\{C_{2z}\}$ (for LG 49); $\{\mathcal{P}, C_{2z}\}$ (51,52);</td>
  </tr>
  <tr>
    <td></td>
    <td>$\{C_{2z}, C_{2x}\}$ (53,54); $\{C_{2z}, M_x\}$ (55,56);</td>
  </tr>
  <tr>
    <td></td>
    <td>$\{\mathcal{P}, C_{2z}, C_{2x}\}$ (61-64)</td>
  </tr>
  <tr>
    <td>$S_{4z}$</td>
    <td>$\{C_{2z}\}$ (49); $\{C_{2z}, C_{2x}\}$ (57,58);</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>$\{C_{2z}, M_x\}$ (59,60)</td>
  </tr>
  <tr>
    <td rowspan="4">![](./images/1240640232739569680_4.jpg)</td>
    <td>$C_{2x}$</td>
    <td>$\{\mathcal{P}\}$ (18); $\{C_{2z}\}$ (22); $\{\mathcal{P}, C_{2z}\}$ (47,48)</td>
  </tr>
  <tr>
    <td>$M_x$</td>
    <td>$\{C_{2z}\}$ (26)</td>
  </tr>
  <tr>
    <td>$C_{2x}$</td>
    <td>$\{E\}$ (10)</td>
  </tr>
  <tr>
    <td>$M_x$</td>
    <td>$\{E\}$ (13); $\{M_z\}$ (35,36)</td>
  </tr>
</tbody>
</table>

From Eq. (6), $\theta_{\mathrm{VH}}$ is a monotonically increasing function of $\mathfrak{e} \in[0,1)$ (see Fig. 2c). Giant valley Hall angles can be inferred by simply inspecting the valley Fermi surface of a TRIV system. For example, $\mathfrak{e} \sim 0.8$ can already give a giant $\theta_{\mathrm{VH}} \sim 0.5$. In addition, we note that for weak eccentricity, Eq. (6) can be simplified as

$$
\theta_{\mathrm{VH}} \approx \zeta|\sin (2 \phi)|, \quad(7)
$$

where $\zeta \equiv \lambda-1>0$ is another parameter characterizing eccentricity.

Universality in TRIV systems. In deriving Eq. (6), we assumed that the two TRIVs are connected by $C_{4 z}$ symmetry. Here, we show that eccentricity VHE and its key features are universal for all 2D TRIV systems.

First of all, among the five 2D Bravais lattices, only square lattice and centered rectangular lattice can support a pair of symmetry-connected TRIVs. To see this, one notes that for oblique and rectangular lattices, no symmetry can connect two TRIVs; for hexagonal lattices there are three (rather than two) $C_{3 z}$-connected TRIVs (the $M$ points). Therefore, the only possibilities left are the square lattice (TRIVs at $X$ and $X^{\prime}$ ) and the centered rectangular lattice (TRIVs at $S$ and $S^{\prime}$ ), as shown in Table I.

By screening the 25 layer groups for these two Bravais lattices (Supplementary Section I), we find that all of them can support the eccentricity VHE (see Table I). Notably, 21 out of these 25 groups contain $\mathcal{P}$ and/or $C_{2 z}$, in which the conventional VHE is strictly forbidden. This shows eccentricity VHE greatly extends the scope of valley Hall systems.

For square lattices, $X$ and $X^{\prime}$ valleys are connected by $C_{4 z}$ or $S_{4 z}$. If there is additional $M_{x}$ or $C_{2 x}$ symmetry at $X$, the principal axis of the Fermi ellipse will be fixed along $x$ and $y$, and $\theta_{\mathrm{VH}}$ is just given by Eqs. (6,7). If there is no $M_{x}$ nor $C_{2 x}$ at $X$, the principal axis of Fermi ellipse

generally has an angular offset $\phi_0$ from crystal axis. In this case, Eqs. (6,7) are merely modified by replacing $\phi$ with $(\phi+\phi_0)$ (Supplementary Section II). For example, Eq. (6) becomes

$$
\theta_{\mathrm{VH}}=\frac{\mathfrak{e}^{2}}{2-\mathfrak{e}^{2}}\left|\sin \left[2\left(\phi+\phi_{0}\right)\right]\right|. \tag{8}
$$

For centered rectangular lattices, $S$ and $S'$ valleys are connected by $M_x$ or $C_{2x}$, and the Fermi ellipse generally has a nonzero offset angle $\phi_0$. The eccentricity valley Hall angle can be found as (Supplementary Section II)

$$
\theta_{\mathrm{VH}}=\frac{\mathfrak{e}^{2}\left|\cos (2 \phi) \sin \left(2 \phi_{0}\right)\right|}{2-2 \mathfrak{e}^{2}+\mathfrak{e}^{2}\left[1+\cos (2 \phi) \sin \left(2 \phi_{0}\right)\right]}. \tag{9}
$$

In the case of weak eccentricity, it is simplified as

$$
\theta_{\mathrm{VH}} \approx \zeta\left|\cos (2 \phi) \sin \left(2 \phi_{0}\right)\right|. \tag{10}
$$

We thus see eccentricity VHE is a universal effect for all TRIV valleytronic platforms.

Material example. To examine the proposed eccentricity VHE, we evaluate the effect in a real material example, monolayer tetragonal $\mathrm{GeS}_2$, by first-principles calculations. This material belongs to the group-IV dichalcogenides family. Its bulk form has van der Waals layered structure and has been synthesized in experiments [19, 20]. Figure 3a shows the structure of monolayer $\mathrm{GeS}_2$. It has a square lattice, with each Ge at the center of tetrahedra formed by surrounding S atoms. The layer group is 59, meeting the symmetry requirement in Table I.

Figure 3b shows the calculated band structure (see Methods for calculation details). One finds there are a pair of TRIVs at $X$ and $X'$ for the valence band. The two valley's Fermi ellipses can be clearly seen in Fig. 3c (plotted at $\mu=-0.1$ eV). According to Table I, the two valleys are connected by $S_{4z}$, and each valley preserves $M_x$. Hence, the eccentricity VHE should be described by Eq. (6).

From Fig. 3b, the two TRIVs can be defined for a wide range of hole doping. Figure 3d shows the valley Hall conductivity $\sigma^v$ and valley Hall angle as functions of $\mu$ computed from the first-principles band structure, with the driving field along the [11] direction. In comparison, the solid lines are obtained from formulas (5) and (6), with eccentricity $\mathfrak{e}=0.92$. One observes an excellent agreement between them. As expected, $\theta_{\mathrm{VH}}$ is robust against change in $\mu$, and its robustness against temperature variation (up to room temperature) is shown in Supplementary Fig. S1. The obtained $\theta_{\mathrm{VH}} \sim 0.74$ is also a giant value.

![](./images/1240640232739569680_5.jpg)

FIG. 3. Results on monolayer $\mathrm{GeS}_2$. a, Crystal structure of monolayer tetragonal $\mathrm{GeS}_2$. b, Calculated band structures. The color map indicates the value of out-of-plane polarization of each state. c, Fermi surface at $\mu=-0.1$ eV. A pair of Fermi ellipses around the two valley centers at $X$ and $X'$ can be seen. d, VHE conductivity and valley Hall angle plotted as functions of chemical potential. The data points are the first-principles results, and the solid lines are results from Eqs. (5) and (6). In calculating $\sigma^v$, we take $\tau=0.1$ ps.

Discussion. We have proposed TRIVs as a new arena for valleytronics, featuring novel phenomena and innovative approaches to manipulating valley degree of freedom. A fascinating effect unveiled here is eccentricity VHE, which is determined by a geometric parameter $\mathfrak{e}$ of Fermi surface and is universal across all TRIV systems. Its distinctive features, including the robust geometric valley Hall angle independent of temperature and carrier density, manifest the distinct fundamental mechanism involved in valley transport. Notably, for conventional VHE from Berry-phase mechanism, the response reflects interband coherence hence strongly depends on the band gap, with $\theta_{\mathrm{VH}}$ quickly suppressed with increasing gap size [1]. In contrast, eccentricity VHE depends only on Fermi surface geometry and not the gap, so it can achieve giant $\theta_{\mathrm{VH}}$ even for mid- and large-gap semiconductors, as evidenced by the example $\mathrm{GeS}_2$. This is a big advantage for applications.

Interestingly, TRIV systems include the layer groups that also support valley-layer coupling [21] (including layer group 10, 22, 50, 59, and 60). In such cases, states of two TRIVs have nonzero and opposite out-of-plane charge polarizations, thus valley polarization can be controlled by a gate field [21]. Monolayer $\mathrm{GeS}_2$ is such an example, with its out-of-plane polarization (Methods) plotted in Fig. 3b. This offers an additional route for valley control.

The eccentricity VHE induces valley polarization accumulated around boundaries normal to the valley current flow direction, which can be experimentally detected via optical linear dichroism. Alternatively, valley polariza-

![](./images/1240640232739569680_6.jpg)

FIG. 4. Nonlocal transport signature. a, Experimental setup for nonlocal measurement of VHE. A charge current is applied between contacts 1 and 2, and the resulting voltage is measured between contacts 3 and 4 at a distance $x$ along the sample strip. b, Eccentricity VHE features a nonlocal resistance $R_{\text{NL}} \propto \rho$, in contrast to the $R_{\text{NL}} \propto \rho^3$ scaling for conventional VHE.

tion can be generated first, e.g., using linearly polarized light or a gate field in systems with valley-layer coupling, leading to a transverse charge current whose sign reflects the valley polarization and which is readily measurable.

Another more direct method to detect eccentricity VHE is via nonlocal measurement, with the typical setup illustrated in Fig. 4a. A driving current $I$ is applied between electrodes 1 and 2, and at a distance of $x$ away, a nonlocal voltage $V_{\text{NL}}$ is detected between 3 and 4. For eccentricity VHE, one finds the following relation for the nonlocal resistance (Supplementary Section IV)

$$
R_{\text{NL}} = V_{\text{NL}}/I \sim \rho \theta_{\text{VH}}^2 e^{-x/\ell_v}, \tag{11}
$$

where $\rho$ is the charge resistivity and $\ell_v$ is the valley diffusion length. This result is in sharp contrast to the conventional VHE which has a scaling $R_{\text{NL}} \propto \rho^3$ [4-6]. By fitting experimental data, this also offers a direct way to evaluate the eccentricity valley Hall angle $\theta_{\text{VH}}$.

Finally, beyond VHE, TRIV systems may host a broad spectrum of intriguing valley phenomena — for example, valley transport and polarization driven by thermoelectric or nonlinear mechanisms. The expanded material classes, enriched valley-layer-spin couplings, and distinct symmetry constraints together suggest a new arena for valleytronics research.

## METHODS

First-principles calculations. The band structure of $\text{GeS}_2$ was calculated using density functional theory as implemented in the VASP package [22-24]. The projector augmented-wave method was employed, with a plane-wave energy cutoff of 400 eV [25]. The Perdew-Burke-Ernzerhof treatment [26] was used to model the exchange-correction functional. The lattice constant was set to $a = 3.456$ Å [19]. A vacuum layer of thickness of 15 Å was applied to suppress the artificial interaction from periodic images. The energy convergence criterion was set as $10^{-6}$ eV. For Brillouin zone sampling, a $\Gamma$-centered $k$-point mesh with size of $16 \times 16 \times 1$ was used. The *ab initio* tight-binding models were constructed using the Wannier90 package [27]. The $s$ and $p$ orbitals of Ge atoms, and the $s$ and $p$ orbitals of S atoms were used as the initial input for the local basis.

Layer polarization. In Fig. 3b, the out-of-plane polarization for a Bloch state $|u_{n\boldsymbol{k}}\rangle$ is evaluated as $p_z = \langle u_{n\boldsymbol{k}}|\hat{z}|u_{n\boldsymbol{k}}\rangle$. Here, the origin $z = 0$ is set at the mid-dle point of the thickness, i.e., at the Ge atomic layer for the monolayer $\text{GeS}_2$ structure. Then, a state with $p_z > 0$ ($< 0$) indicates that the state has more distribution in the upper (lower) atomic layer. The little co-group of the $X$ ($X'$) valleys is generated by $C_{2z}$ and $M_x$ (see Table I), which allows a finite $p_z$ at the two valleys. Meanwhile, the two valleys are connected by the $\mathcal{Q} = S_{4z}$ symmetry, which requires the two valleys have opposite $p_z$, as shown in Fig. 3b. Based on this feature, a gate electric field can induce a valley splitting and generate a valley carrier polarization.

* congxiao@fudan.edu.cn
† shengyuan.yang@polyu.edu.hk

[1] D. Xiao, W. Yao, and Q. Niu, Valley-contrasting physics in graphene: Magnetic moment and topological transport, Phys. Rev. Lett. 99, 236809 (2007).
[2] D. Xiao, G.-B. Liu, W. Feng, X. Xu, and W. Yao, Coupled spin and valley physics in monolayers of mos2 and other group-vi dichalcogenides, Phys. Rev. Lett. 108, 196802 (2012).
[3] K. F. Mak, K. L. McGill, J. Park, and P. L. McEuen, The valley hall effect in mos2 transistors, Science 344, 1489 (2014).
[4] R. V. Gorbachev, J. C. W. Song, G. L. Yu, A. V. Kretinin, F. Withers, Y. Cao, A. Mishchenko, I. V. Grigorieva, K. S. Novoselov, L. S. Levitov, and A. K. Geim, Detecting topological currents in graphene superlattices, Science 346, 448 (2014).
[5] M. Sui, G. Chen, L. Ma, W.-Y. Shan, D. Tian, K. Watanabe, T. Taniguchi, X. Jin, W. Yao, D. Xiao, and Y. Zhang, Gate-tunable topological valley transport in bilayer graphene, Nat. Phys. 11, 1027 (2015).
[6] Y. Shimazaki, M. Yamamoto, I. V. Borzenets, K. Watanabe, T. Taniguchi, and S. Tarucha, Generation and de-

tection of pure valley current by electrically induced berry curvature in bilayer graphene, Nat. Phys. 11, 1032 (2015).

[7] J. Lee, K. F. Mak, and J. Shan, Electrical control of the valley hall effect in bilayer mos2 transistors, Nat. Nan- otechnol. 11, 421 (2016).

[8] Z. Wu, B. T. Zhou, X. Cai, P. Cheung, G.-B. Liu, M. Huang, J. Lin, T. Han, L. An, Y. Wang, S. Xu, G. Long, C. Cheng, K. T. Law, F. Zhang, and N. Wang, Intrinsic valley hall transport in atomically thin mos2, Nat. Commun. 10, 611 (2019).

[9] A. Rycerz, J. Tworzydło, and C. W. J. Beenakker, Val- ley filter and valley valve in graphene, Nat. Phys. 3, 172 (2007).

[10] W. Yao, D. Xiao, and Q. Niu, Valley-dependent optoelec- tronics from inversion symmetry breaking, Phys. Rev. B 77, 235406 (2008).

[11] T. Cai, S. A. Yang, X. Li, F. Zhang, J. Shi, W. Yao, and Q. Niu, Magnetic control of the valley degree of freedom of massive dirac fermions with application to transition metal dichalcogenides, Phys. Rev. B 88, 115140 (2013).

[12] T. Y. Hung, K. Y. Camsari, S. Zhang, P. Upadhyaya, and Z. Chen, Direct observation of valley-coupled topological current in mos2, Sci. Adv. 5, eaau6478 (2019).

[13] L. Li, L. Shao, X. Liu, A. Gao, H. Wang, B. Zheng, G. Hou, K. Shehzad, L. Yu, F. Miao, et al., Room- temperature valleytronic transistor, Nat. Nanotechnol. 15, 743 (2020).

[14] C. Jiang, A. Rasmita, H. Ma, Q. Tan, Z. Zhang, Z. Huang, S. Lai, N. Wang, S. Liu, X. Liu, et al., A room- temperature gate-tunable bipolar valley hall effect in molybdenum disulfide/tungsten diselenide heterostruc- tures, Nat. Electron. 5, 23 (2022).

[15] X. Xu, W. Yao, D. Xiao, and T. F. Heinz, Spin and pseudospins in layered transition metal dichalcogenides, Nat. Phys. 10, 343 (2014).

[16] J. R. Schaibley, H. Yu, G. Clark, P. Rivera, J. S. Ross, K. L. Seyler, W. Yao, and X. Xu, Valleytronics in 2d materials, Nat. Rev. Mater. 1, 16055 (2016).

[17] S. A. Vitale, D. Nezich, J. O. Varghese, P. Kim, N. Gedik, P. Jarillo-Herrero, D. Xiao, and M. Rothschild, Val- leytronics: Opportunities, challenges, and paths forward, Small 14, 1801483 (2018).

[18] K. F. Mak, D. Xiao, and J. Shan, Light-valley interac- tions in 2d semiconductors, Nat. Photon. 12, 451 (2018).

[19] M. Shimada and F. Dachille, Crystallization of amor- phous germanium sulfide and germanium selenide under pressure, Inorganic Chemistry 16, 2094 (1977).

[20] L. F. Kulikova, L. M. Lityagina, I. P. Zibrov, T. I. Dyuzheva, N. A. Nikolaev, and V. V. Brazhkin, High- pressure, high-temperature study of ges2 and gese2, In- organic Materials 50, 768 (2014).

[21] Z.-M. Yu, S. Guan, X.-L. Sheng, W. Gao, and S. A. Yang, Valley-layer coupling: A new design principle for valleytronics, Phys. Rev. Lett. 124, 037701 (2020).

[22] G. Kresse and J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47, 558 (1993).

[23] G. Kresse and J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6, 15 (1996).

[24] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[25] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994).

[26] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77, 3865 (1996).

[27] A. A. Mostofi, J. R. Yates, G. Pizzi, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, An updated version of wannier90: A tool for obtaining maximally-localised wannier functions, Comput. Phys. Commun. 185, 2309 (2014).