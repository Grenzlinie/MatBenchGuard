# Geometric Origin of Phonon Magnetic Moment in Dirac Materials

Wenqin Chen, $^{1,2}$ Xiao-Wei Zhang, $^{3}$ Ting Cao, $^{3}$ Shi-Zeng Lin, $^{2,4, *}$ and Di Xiao $^{3,1, \dagger}$

$^{1}$ Department of Physics, University of Washington, Seattle, Washington 98195, USA
$^{2}$ Theoretical Division, T-4 and CNLS, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA
$^{3}$ Department of Materials Science and Engineering,
University of Washington, Seattle, Washington 98195, USA
$^{4}$ Center for Integrated Nanotechnologies (CINT),
Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA

We develop a theory for the phonon magnetic moment in doped Dirac materials, treating phonons as emergent gauge and gravitational fields coupled to Dirac fermions in curved space. By classifying electron-phonon coupling into angular momentum channels of Fermi surface deformation, we show that the phonon moment arises from two mechanisms: proportional to the electron Hall conductivity through the emergent gauge field coupling, and to the Hall viscosity through the frame field coupling. Applying our theory to $\mathrm{Cd}_3\mathrm{As}_2$ with first-principles calculations, we find quantitative agreement with experiment. Our results reveal a general mechanism for dynamically generating large phonon magnetism in metals and suggest a new route for probing Hall viscosity via phonon dynamics.

Introduction.—Phonons, the quantized vibrations of a crystal lattice, are among the most fundamental bosonic excitations in solids. Traditionally regarded as non- magnetic, phonons have recently been shown to carry orbital magnetic moments, opening up an exciting av- enue for exploring novel transport and optical phenom- ena [1–24]. Early theoretical work based on a classical picture of circulating ions predicted small phonon mo- ments on the order of the nuclear magneton due to the heavy mass of ions [25, 26]. However, recent experi- ments have reported much larger moments—approaching the Bohr magneton—in a wide range of materials [27– 32]. These findings have motivated the development of quantum theories that attribute the magnetic moment to electron-phonon coupling [33–38], though these theories have thus far focused primarily on insulating systems.

Remarkably, large phonon moments have also been ob- served in metallic systems such as doped $\mathrm{Cd}_3\mathrm{As}_2$ [27] and $\mathrm{Pb}_{1-x}\mathrm{Sn}_{x}\mathrm{Te}$ [29]. $\mathrm{Cd}_3\mathrm{As}_2$ is a Dirac semimetal with bulk Dirac fermions, while $\mathrm{Pb}_{1-x}\mathrm{Sn}_{x}\mathrm{Te}$ is a topological crys- talline insulator featuring gapless Dirac surface states. These observations suggest a strong connection between Dirac fermions and the emergence of phonon magnetic moments in gapless systems, yet the underlying mecha- nism remains poorly understood.

In addition to their experimental relevance, Dirac fermions allow an elegant framework for modeling electron-phonon coupling. Previous studies have shown that acoustic phonons and lattice strain can couple to electrons as emergent gauge and gravitational fields [33, 38–47]. More recently, it has been recognized that optical phonons can also couple to Dirac fermions as emergent gauge fields [48–50], giving rise to a phonon magnetic moment [51].

In this work, we demonstrate that optical phonons can also act as gravitational fields. Building on the frame- work of Dirac fermions in curved space, we develop a theory for the phonon magnetic moment in doped Dirac materials. By classifying electron-phonon coupling into angular momentum channels of Fermi surface deforma- tion, we link the orbital magnetic moment of phonons to electronic transport coefficients. A key result is that op- tical phonons can act as a dynamic frame field, inducing a phonon magnetic moment through feedback from the Hall viscosity of the electron fluid. Combined with first- principles calculations, we apply our theory to $\mathrm{Cd}_3\mathrm{As}_2$, which yields a phonon magnetic moment consistent with experiment [27]. Our results not only provide a micro- scopic explanation for giant phonon moments in metals, but also suggest a route for experimentally probing Hall viscosity via phonon dynamics.

Geometrization of phonons.—We begin by developing a geometric framework in which phonons act as frame fields and gauge fields in the low-energy theory of Dirac materials, effectively “geometrizing” lattice vibrations. For simplicity, we consider spinless Dirac points in three dimensions, described by the low-energy Hamiltonian $\mathcal{H}_D = v_F \mathbf{k} \cdot \boldsymbol{\sigma}$, where $\boldsymbol{\sigma}$ are the Pauli matrices, $v_F$ is the Fermi velocity, and $\mathbf{k}$ is the electron momentum. The effect of spin will be addressed later when we apply our theory to $\mathrm{Cd}_3\mathrm{As}_2$. Due to the linear band crossing, small perturbations cannot open a gap at the Dirac point; in- stead, they can only (i) shift its position in momentum space and (ii) modify the anisotropy or magnitude of the Dirac dispersion, as illustrated in Fig. 1(a). These effects are naturally encoded in a geometric language: the mo- mentum shift corresponds to a minimal coupling to an emergent gauge field $\mathbf{a}$, while the velocity renormaliza- tion corresponds to a frame field (vielbein) $e_A^\mu$ that acts as an emergent gravitational field by rescaling the local dispersion. Including these phonon-induced fields along with the external electromagnetic vector potential $\mathbf{A}$, the system is described by the Dirac Hamiltonian in curved space [40, 52, 53],

$$
\mathcal{H}_{\text{eff}} = v_F \sum_{\mu, A} (k_\mu - \chi a_\mu - A_\mu) e_A^\mu \sigma^A - \varepsilon_F, \tag{1}
$$

![](./images/1130109165553844237_1.jpg)

FIG. 1. Schematic illustration of phonon-induced gauge and
frame fields in Dirac materials. (a) Emergent gauge field
$\chi \mathbf{a}$ shifts the Dirac point, while frame field $e_{\mu}^{A}$ distorts the
Dirac cone. (b) In an $sp$-orbital lattice model, the frame
field $(\mathbf{e}_{1},\mathbf{e}_{2})$ arises from bond stretching due to phonon dis-
placement $\mathbf{u}$. Angular momentum channels contributing to
the phonon magnetic moment: (c) Trivial monopolar $(l=0)$
channel; (d) Dipolar $(l=1)$ channel: phonon displaces the
Fermi surface and drives circular motion; (e) Quadrupolar
$(l=2)$ channel: phonon distorts the Fermi surface into a ne-
matic shape and rotates it.

where $\varepsilon_{F}$ is the Fermi energy, $\chi=\pm1$ denotes the val-
ley index, $\mu=x,y,z$ labels global Cartesian coordinates,
and $A=1,2,3$ indexes the local tangent space spanned
by the frame field. In what follows, we demonstrate that
both gauge and frame fields naturally arise from opti-
cal phonons. For concreteness, we focus on zone-center
phonon modes $(\mathbf{q}=0)$ confined to the $xy$ plane.

To build intuition for the less-familiar concept of a
frame field, we begin with a heuristic argument illus-
trating how it can be parameterized in terms of phonon
modes. In a lattice distorted by a phonon mode, we can
define a set of local frame vectors $(\mathbf{e}_{1},\mathbf{e}_{2})$ based on the
atomic displacement field $\mathbf{u}$. Specifically, $\hat{e}_{1}$ is chosen to
align with the direction of $\mathbf{u}$, while $\hat{e}_{2}$ is orthogonal to it.
The transverse vector $\mathbf{e}_{2}=\hat{e}_{2}$ remains a unit vector, but
the longitudinal vector $\mathbf{e}_{1}$ is stretched or compressed by
the displacement, becoming $\mathbf{e}_{1}=(1-\beta u/a)\hat{e}_{1}$, where $a$
is the lattice constant and $\beta$ is a dimensionless parameter
characterizing the strength of the distortion. Decompos-
ing the local frame vectors into the global Cartesian basis
yields the components of the frame field tensor $e_{A}^{\mu}$:

$$
\begin{aligned}
& e_{1}^{x}=\left(1-\frac{\beta u}{a}\right)\cos\theta, \quad e_{2}^{x}=-\sin\theta, \\
& e_{1}^{y}=\left(1-\frac{\beta u}{a}\right)\sin\theta, \quad e_{2}^{y}=\cos\theta,
\end{aligned}\tag{2}
$$

where $\theta$ is the instantaneous angle between the displace-
ment vector $\mathbf{u}$ and the $x$-axis. In this way, lattice vibra-
tions dynamically modify the local geometry experienced
by electrons, with the phonon displacement field entering
the low-energy theory through the frame field.

With this intuitive understanding in hand, we now turn
to a microscopic analysis of how optical phonons induce
both emergent frame and gauge fields. To that end, we
examine a tight-binding model defined on a cubic lattice
[Fig. 1(b)], with two orbitals per site. The Hamiltonian
takes the form

$$
\begin{aligned}
H= & \frac{1}{2}\sum_{j}\sum_{\mu=x,y}\left[\psi_{j+\mathbf{a}_{\mu}}^{\dagger}\left(it\sigma^{\mu}-m_{\perp}\sigma^{z}\right)\psi_{j}+\text{H.c.}\right] \\
& -\frac{1}{2}\sum_{j}\left[\psi_{j+\mathbf{a}_{z}}^{\dagger}m_{z}\sigma^{z}\psi_{j}+\text{H.c.}\right]+m_{0}\sum_{j}\psi_{j}^{\dagger}\sigma^{z}\psi_{j},
\end{aligned}
\tag{3}
$$

where $\psi_{j}^{\dagger}=(c_{j,s}^{\dagger},c_{j,p}^{\dagger})$ creates electrons in the $s$- and
$p$-orbitals at site $j$. The parameters $m_{\perp}$ and $m_{z}$ de-
note intra-orbital hopping amplitudes in the $xy$-plane
and along the $z$-axis, respectively, while $m_{0}$ is the on-
site energy difference between the two orbitals. The
inter-orbital hopping is encoded in the terms propor-
tional to $t\sigma^{x}$ and $t\sigma^{y}$, given by Slater-Koster integrals
between nearest neighbors. In equilibrium, this model
supports two Dirac points located at $\mathbf{K}_{\pm}=(0,0,\pm k_{z0})$,
where the position $k_{z0}$ is determined by $\cos(k_{z0}a)=$
$(m_{0}+2m_{\perp})/m_{z}$.

The modulation of the inter-orbital hopping matrices
by optical phonons arises from two primary effects: bond
stretching and relative rotation of orbitals [41, 42, 46]. As
shown in Fig. 1(b), a phonon mode polarized along the
direction $\hat{e}_{1}$ stretches the bond between neighboring sites,
modifying the hopping amplitude in that direction. This
leads to a change in the inter-orbital hopping matrix:
$t(u)\sigma^{1}\approx(t+u\partial t/\partial a)\sigma^{1}=t(1-\beta u/a)\sigma^{1}$, where $a$ is
the equilibrium bond length and $\beta=-\partial\ln t/\partial\ln a$ is a
dimensionless parameter. In contrast, hopping along the
orthogonal direction $\hat{e}_{2}$ remains unaffected. To express
this modulation in the global Cartesian basis, we project
the deformed hopping terms along $\hat{x}$ and $\hat{y}$:

$$
\begin{aligned}
t\sigma^{x} & \to t\left(1-\frac{\beta u}{a}\right)\cos\theta\sigma^{1}-t\sin\theta\sigma^{2}, \\
t\sigma^{y} & \to t\left(1-\frac{\beta u}{a}\right)\sin\theta\sigma^{2}+t\cos\theta\sigma^{1}.
\end{aligned}
\tag{4}
$$

Substituting these anisotropically modified hopping ma-
trices into Eq. (3) and transforming to momentum space,
$\sum_{\mathbf{k}}\psi_{\mathbf{k}}^{\dagger}\mathcal{H}(\mathbf{k})\psi_{\mathbf{k}}$, we find that the Fermi velocity becomes
directionally renormalized near each Dirac point $\mathbf{K}_{\chi}$.
This anisotropic velocity renormalization corresponds to
the frame field $e_{A}^{\mu}$ introduced in Eq. (2).

On the other hand, the emergent gauge field arises from
the relative rotation of the $s$ and $p$ orbitals between neigh-
boring sites in the $z$ direction. To distinguish between the
inversion-even and odd optical modes, we formally dou-
ble the unit cell to include two lattice sites. The relative
rotation induced by $\mathbf{u}$ gives rise to a new inter-orbital
term along $\hat{z}$ of the form $it(\beta/a)(u_{x}\sigma^{x}+u_{y}\sigma^{y})$. For an
inversion-even mode, this hopping modifies the Hamil-
tonian by adding a term $\sum_{\mathbf{k}}\psi_{\mathbf{k}}^{\dagger}[t(\beta/a)\sin(k_{z}a)(u_{x}\sigma^{x}+$

$u_y\sigma^y)]\psi_{\bf k}$, which contributes to the emergent gauge field $\chi{\bf a}=\chi k_{z0}(\beta/a){\bf u}$, where $\chi=\pm1$ is the valley index.

By contrast, this term vanishes identically for inversion-odd phonon modes, resulting in a vanishing emergent gauge field. This difference is a consequence of symmetry. In general, the minimal coupling ${\bf k}-\chi{\bf a}$ must be compatible with the little group at the Dirac point. In our model, the little group at ${\bf K}_\chi$ includes the combined operation $T\times I$, where $T$ denotes time-reversal and $I$ denotes inversion. Since ${\bf k}$ is even under $T\times I$ and the valley index $\chi$ is also even, the phonon displacement ${\bf u}$ must be even under inversion for the coupling to be symmetry-allowed. As a result, inversion-odd modes cannot couple to electrons as a gauge field, while inversion-even modes can.

Angular momentum channels.— To further classify the effects of electron-phonon coupling, we analyze how phonon modes deform the Fermi surface. Starting from the effective Hamiltonian in Eq. (1), we solve the eigenvalue equation and set the energy to zero to obtain the Fermi surface, which is deformed by phonons as
$$
\begin{aligned}
\sum_{\mu,\nu}\delta^{\mu\nu}k_\mu k_\nu&=k_F^2\rightarrow\\
\sum_{\mu,\nu}g^{\mu\nu}({\bf u})[k_\mu-\chi a_\mu({\bf u})][k_\nu-\chi a_\nu({\bf u})]&=k_F^2,
\end{aligned}\tag{5}
$$
where $k_F=\varepsilon_F/v_F$ is the Fermi momentum, and $g^{\mu\nu}=e_A^\mu e_B^\nu\delta^{AB}$ is the spatial metric tensor [54]. The angular Fourier components of the Fermi surface deformation provide a classification scheme for the electron-phonon coupling effects: the dipolar $(l=1)$ channel, which describes a rigid shift of the Fermi surface, corresponds to the emergent gauge field, while the frame field contributes to both a monopolar $(l=0)$ deformation [Fig. 1(c)] and a quadrupolar $(l=2)$ distortion. The latter leads to a nematic Fermi surface, associated with the traceless part of the spatial metric,
$$
g^{\mu\nu,(2)}({\bf u})\approx-\frac{2\beta u}{a}\left(\hat{e}_1^\mu\hat{e}_1^\nu-\frac{1}{2}\delta^{\mu\nu}\right),\tag{6}
$$
where $(\hat{e}_1^x,\hat{e}_1^y)=(\cos\theta,\sin\theta)$ is the phonon polarization direction. This quadrupolar component shares the same tensorial form as a nematic order parameter, capturing an elliptic distortion of the Fermi surface. We note that the formation of the nematic Fermi surface is dynamically driven by the phonon excitations, which is distinct from the static nematic order that arises from spontaneous symmetry breaking via Pomeranchuk instability [55].

The angular momentum classification also clarifies the origin of the phonon orbital magnetic moment. In the dipolar $(l=1)$ channel [Fig. 1(d)], the phonon shifts the center of the Fermi surface and induces a circular motion around the Dirac point, generating an orbital magnetic moment. In the quadrupolar $(l=2)$ channel [Fig. 1(e)], the phonon distorts the Fermi surface into a nematic shape and drives its rotation, also producing an orbital moment. These two mechanisms are momentum-space analogs of the two adiabatic contributions to phonon magnetism previously identified in band insulators [34–36].

Phonon magnetic moment.— To quantify the two contributions to the phonon magnetic moment, we integrate out the Dirac fermions in the effective Hamiltonian in Eq. (1) using established low-energy field theories for emergent gauge and frame fields. In the gauge field channel, the Chern-Simons action $S_H[a_\mu]=(\sigma_{xy}/2)\int dtd^x\epsilon^{\mu\nu\rho}a_\mu\partial_\nu a_\rho$ links the phonon moment directly to the electrical Hall conductivity, yielding $\mu_{\rm ph}=(\hbar^3k_{z0}^2\beta^2/e^2v_F^2\rho_Ia^2)\sigma_{xy}/B$, where $\rho_I$ is the ion mass density and $B$ is the magnetic field [51]. (We restore $e$ and $\hbar$ hereafter.) In this work, we focus on the contribution from the frame field channel. In $(2+1)$-dimensional Chern insulators, integrating out Dirac fermions coupled to the coframe field $e_\mu^A$ leads to an effective action [44, 56]: $S_H[e_\mu^A]=(\eta_H/2)\int dtd^2x\ \epsilon^{\mu\nu\rho}e_\mu^A\partial_\nu e_\rho^B\delta_{AB}$, where $\eta_H$ is the Hall viscosity coefficient of the Dirac fluid, $\epsilon^{\mu\nu\rho}$ is the Levi-Civita symbol, and $e_\mu^A$ is the coframe field defined as the inverse of $e_A^\mu$ satisfying $e_\mu^Ae_B^\mu=\delta_B^A$ [57]. By stacking Chern insulators in momentum space, this term can also be generalized to describe the $(3+1)$-dimensional Dirac system considered here [44, 58]. This action encodes the Hall viscosity response of the Dirac system, a dissipationless transport coefficient that characterizes the transverse stress response to metric perturbations in the presence of broken time-reversal symmetry [59].

In our context, the optical phonon acts as a dynamic metric perturbation, generating a Hall viscosity response in the electron system. Expressing $e_\mu^A$ in terms of the phonon displacement ${\bf u}$, we obtain a new term in the phonon effective action, $S_{\rm eff}[{\bf u}]=S_0[{\bf u}]+S_H[{\bf u}]$, where $S_0[{\bf u}]=\int dtd^2x\ \rho_I(\dot{\bf u}^2-\omega_0^2{\bf u}^2)/2$ with $\rho_I$ the ion mass density and $\omega_0$ the bare frequency. The new term is
$$
S_H[{\bf u}]=\frac{\eta_H\beta^2}{2a^2}\int dtd^2x\ \epsilon^{\mu\nu}u_\mu\dot{u}_\nu,\tag{7}
$$
This term breaks time-reversal symmetry and leads to a splitting of the chiral phonon modes $u_\pm=(u_x\pm iu_y)/\sqrt{2}$. Physically, it reflects a feedback mechanism: the phonon motion drags the electron fluid, inducing a Hall viscosity response that in turn exerts a transverse force on the phonon—manifesting as a torque and splitting the phonon frequencies: $\omega_\pm=\sqrt{\omega_0^2+\delta\omega^2}\pm\delta\omega$, where the splitting is $\delta\omega=\eta_H\beta^2/2a^2\rho_I$ [57].

To estimate the Hall viscosity of the electron fluid, we employ a semiclassical approach. In this regime, $\eta_H$ depends on both the magnetic field $B$ and the electron transport lifetime $\tau$, and is given by $\eta_H=2\eta_0\omega_c\tau/(1+4\omega_c^2\tau^2)$, where $\eta_0=n_em^*v_F^2\tau/4$ is the zero-field shear viscosity, $\omega_c=eB/m^*$ is the cyclotron frequency, $m^*$ is the effective mass, and $n_e$ is the electron density [60–62].

TABLE I. Classification of electron-phonon coupling channels by angular momentum and inversion symmetry. The $l=1$ (gauge field) channel is forbidden for inversion-odd modes, while $l=0,2$ (frame field) channels are allowed for both parities. The phonon magnetic moment $\mu_{\text{ph}}$ is proportional to $\sigma_{xy}$ in the gauge field channel and to $\eta_H$ in the quadrupolar frame field channel.

|  | $l=0$ (Frame) | $l=1$ (Gauge) | $l=2$ (Frame) |
| --- | --- | --- | --- |
| Inversion-even | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| Inversion-odd | $\checkmark$ | $\times$ | $\checkmark$ |
| $\mu_{\text{ph}}$ | $0$ | $\sigma_{xy}$ | $\eta_H$ |

In the weak-field limit $(\omega_c\tau \ll 1)$, $\eta_H$ scales linearly with $B$, resulting in a linear splitting of the phonon frequencies: $\hbar\omega_{\pm} = \hbar\omega_0 \pm \mu_{\text{ph}}B$, which can be interpreted as a phonon Zeeman effect. The corresponding phonon magnetic moment is
$$
\mu_{\text{ph}} = \frac{\hbar\beta^2}{\rho_I a^2} \cdot \frac{\eta_H}{B}, \tag{8}
$$
where the factor $\beta/a$ quantifies the strength of electron-phonon coupling via the frame field. As $B$ approaches zero, $\eta_H \approx n_e v_F^2 \tau^2 eB/2$, implying that $\mu_{\text{ph}}$ becomes independent of $B$.

This result establishes a direct and measurable link between the phonon magnetic moment and the Hall viscosity of the electron fluid through frame field coupling—one of the central findings of this work. A summary of the angular momentum channels and their symmetry properties is provided in Table I.

Application to $Cd_3As_2$.— We now apply our theory to the Dirac semimetal $Cd_3As_2$, where a large phonon magnetic moment has been observed experimentally [27]. Thus far, we have neglected spin degrees of freedom. Including spin introduces two main effects. First, the $E_u$ phonon mode—by breaking inversion symmetry—can split each Dirac point into a pair of Weyl nodes. However, time-reversal symmetry ensures that the Weyl nodes are displaced in opposite directions in momentum space. As long as the Fermi surface encloses both nodes, their contributions to the phonon magnetic moment cancel, and the frame field mechanism remains the dominant effect. Second, strong spin-orbit coupling can enable chiral phonons to induce spin polarization, giving rise to a phonon magnetic moment with both spin and orbital components. In this work, we focus exclusively on the orbital contribution and leave spin-related effects for future investigation.

Based on these considerations, we carry out first-principles calculations. Figure 2(a) shows the phonon spectrum of $Cd_3As_2$ in the THz range. The infrared-active $E_u$ optical mode at 0.6 THz corresponds to the experimentally measured mode. Its twofold degeneracy permits the formation of circularly polarized modes. As shown in the inset of Fig. 2(a), this mode is inversion odd and thus does not generate an emergent gauge field, consistent with our symmetry analysis.

![](./images/1130109165553844237_2.jpg)

FIG. 2. First-principles analysis of the $E_u$ phonon mode in $Cd_3As_2$ and its magnetic moment. (a) Phonon spectrum showing the infrared-active $E_u$ mode at 0.6 THz, corresponding to the experimentally measured mode. Inset illustrates its displacement pattern in the $sp$-orbital model. (b) Energy contours of the Dirac cone at $\mathbf{K}_+$ in equilibrium. (c) Same as (b), but with $E_u$ phonon distortion, showing elliptical deformation consistent with a phonon-induced frame field. (d) Phonon frequency splitting versus magnetic field at $\tau=0.08$ ps. (e) Phonon magnetic moment versus electron transport lifetime $\tau$ at $\varepsilon_F=0.1$ eV. Dashed line indicates the experimental value.

Figures 2(b) and 2(c) compare the in-plane energy contours of the Dirac cone at the $\mathbf{K}_+$ valley in equilibrium and under $E_u$-mode distortion, respectively. The elliptic deformation induced by the phonon displacement confirms the emergence of a frame field and the formation of a nematic Fermi surface. Moreover, the absence of a Dirac point shift reinforces the conclusion that the emergent gauge field vanishes for this mode. These results from first-principles calculations are fully consistent with our theoretical predictions. From the slope of the Dirac cone and the averaged phonon eigenvector, we extract an estimate for the electron-phonon coupling parameter: $\beta/a \approx 632$ $\text{\AA}^{-1}$ [57].

For numerical estimates, we adopt the following parameters for $Cd_3As_2$: $v_F \approx 10^6$ m/s and $\rho_I \approx 3.03 \times 10^3$ kg/m$^3$. Figure 2(d) shows the calculated phonon frequency splitting as a function of magnetic field at a fixed

transport lifetime $\tau = 0.08$ ps. In the weak-field limit, the splitting is linear in $B$, while in the strong-field limit, it becomes inversely proportional to $B$. The asymmetric evolution of the $\omega_+$ and $\omega_-$ branches reproduces key features of the experimental data [27]. Finally, in Fig. 2(e), we plot the phonon magnetic moment as a function of $\tau$ at fixed Fermi energy $\varepsilon_F = 0.1$ eV. For the experimental sample, $\tau \sim 0.1$ ps, and the calculated phonon magnetic moment is in good agreement with the measured value. This supports the conclusion that the frame field mechanism developed here accounts for the observed phonon magnetic moment in $\text{Cd}_3\text{As}_2$.

Conclusion and discussion.— We have presented a general mechanism by which electron-phonon coupling can give rise to sizable phonon magnetic moments in Dirac materials. By analyzing the angular momentum components of phonon-induced Fermi surface deformations, we classify the phonon field as coupling to electrons via either an emergent gauge field or a frame field. In the gauge (frame) field channel, the resulting phonon magnetic moment is proportional to the electronic Hall conductivity (viscosity).

We applied the frame field mechanism to $\text{Cd}_3\text{As}_2$ and found quantitative agreement between the calculated phonon magnetic moment and experimental measurements, using realistic material parameters. Beyond explaining the observed phonon moment, our results point to a new avenue for probing the elusive Hall viscosity of electron fluids through phonon-based measurements—particularly in systems where competing effects, such as spin-phonon coupling, can be minimized or systematically disentangled.

We thank Alexander Balatsky for the helpful discussion. The work at UW was supported by DOE Award No. DE-SC0012509. The work at LANL was carried out under the auspices of the U.S. DOE NNSA under contract No. 89233218CNA000001 through the LDRD Program, and was supported by the Center for Nonlinear Studies at LANL, and was performed, in part, at the Center for Integrated Nanotechnologies, an Office of Science User Facility operated for the U.S. DOE Office of Science, under user proposals $\#2018BU0010$ and $\#2018BU0083$.

* szl@lanl.gov
† dixiao@uw.edu

[1] L. Zhang and Q. Niu, Chiral phonons at high-symmetry points in monolayer hexagonal lattices, Phys. Rev. Lett. 115, 115502 (2015).

[2] H. Zhu, J. Yi, M.-Y. Li, J. Xiao, L. Zhang, C.-W. Yang, R. A. Kaindl, L.-J. Li, Y. Wang, and X. Zhang, Observation of chiral phonons, Science 359, 579 (2018).

[3] K. Ishito, H. Mao, Y. Kousaka, Y. Togawa, S. Iwasaki, T. Zhang, S. Murakami, J.-i. Kishine, and T. Satoh, Truly chiral phonons in $\alpha$-HgS, Nature Physics 19, 35 (2023).

[4] H. Ueda, M. García-Fernández, S. Agrestini, C. P. Romao, J. van den Brink, N. A. Spaldin, K.-J. Zhou, and U. Staub, Chiral phonons in quartz probed by X-rays, Nature 618, 946 (2023).

[5] G. Grissonnanche, A. Legros, S. Badoux, E. Lefrançois, V. Zatko, M. Liziaire, F. Laliberté, A. Gourgout, J.-S. Zhou, S. Pyon, et al., Giant thermal Hall conductivity in the pseudogap phase of cuprate superconductors, Nature 571, 376 (2019).

[6] X. Li, B. Fauqué, Z. Zhu, and K. Behnia, Phonon thermal Hall effect in strontium titanate, Phys. Rev. Lett. 124, 105901 (2020).

[7] G. Grissonnanche, S. Thériault, A. Gourgout, M.-E. Boulanger, E. Lefrançois, A. Ataei, F. Laliberté, M. Dion, J.-S. Zhou, S. Pyon, et al., Chiral phonons in the pseudogap phase of cuprates, Nature Physics 16, 1108 (2020).

[8] S. Park and B.-J. Yang, Phonon angular momentum Hall effect, Nano Letters 20, 7694 (2020), pMID: 32955897.

[9] M.-E. Boulanger, G. Grissonnanche, S. Badoux, A. Allaire, É. Lefrançois, A. Legros, A. Gourgout, M. Dion, C. Wang, X. Chen, et al., Thermal Hall conductivity in the cuprate mott insulators Nd2CuO4 and Sr2CuO2Cl2, Nature communications 11, 5325 (2020).

[10] L. Chen, M.-E. Boulanger, Z.-C. Wang, F. Tafti, and L. Taillefer, Large phonon thermal Hall conductivity in the antiferromagnetic insulator Cu3Teo6, Proceedings of the National Academy of Sciences 119, e2208016119 (2022).

[11] T. Saito, K. Misaki, H. Ishizuka, and N. Nagaosa, Berry phase of phonons and thermal Hall effect in nonmagnetic insulators, Phys. Rev. Lett. 123, 255901 (2019).

[12] B. Flebus and A. H. MacDonald, Phonon Hall viscosity of ionic crystals, Phys. Rev. Lett. 131, 236301 (2023).

[13] J. Bonini, S. Ren, D. Vanderbilt, M. Stengel, C. E. Dreyer, and S. Coh, Frequency splitting of chiral phonons from broken time-reversal symmetry in $\text{CrI}_3$, Phys. Rev. Lett. 130, 086701 (2023).

[14] S. Ren, J. Bonini, M. Stengel, C. E. Dreyer, and D. Vanderbilt, Adiabatic dynamics of coupled spins and phonons in magnetic insulators, Phys. Rev. X 14, 011041 (2024).

[15] M. Hamada and S. Murakami, Conversion between electron spin and microscopic atomic rotation, Phys. Rev. Res. 2, 023275 (2020).

[16] T. F. Nova, A. Cartella, A. Cantaluppi, M. Först, D. Bossini, R. V. Mikhaylovskiy, A. V. Kimel, R. Merlin, and A. Cavalleri, An effective magnetic field from optically driven phonons, Nature Physics 13, 132 (2017).

[17] J. Luo, T. Lin, J. Zhang, X. Chen, E. R. Blackert, R. Xu, B. I. Yakobson, and H. Zhu, Large effective magnetic fields from chiral phonons in rare-earth halides, Science 382, 698 (2023).

[18] M. Basini, M. Pancaldi, B. Wehinger, M. Udina, V. Unikandanunni, T. Tadano, M. C. Hoffmann, A. V. Balatsky, and S. Bonetti, Terahertz electric-field-driven dynamical multiferroicity in SrTiO3, Nature 628, 534–539 (2024).

[19] C. Davies, F. Fennema, A. Tsukamoto, I. Razdolski, A. Kimel, and A. Kirilyuk, Phononic switching of magnetization by the ultrafast Barnett effect, Nature , 1 (2024).

[20] D. M. Juraschek, P. Narang, and N. A. Spaldin, Phonomagnetic analogs to opto-magnetic effects, Phys. Rev. Res. 2, 043035 (2020).

[21] D. M. Juraschek, T. c. v. Neuman, and P. Narang, Gi-

ant effective magnetic fields from optically driven chiral phonons in $4f$ paramagnets, Phys. Rev. Res. 4, 013129 (2022).

[22] D. Shin, H. Hübener, U. De Giovannini, H. Jin, A. Ru- bio, and N. Park, Phonon-driven spin-floquet magneto- valleytronics in MoS2, Nature communications 9, 638 (2018).

[23] Y. Ren, M. Rudner, and D. Xiao, Light-driven sponta- neous phonon chirality and magnetization in paramag- nets, Phys. Rev. Lett. 132, 096702 (2024).

[24] R. M. Geilhufe, V. Juričić, S. Bonetti, J.-X. Zhu, and A. V. Balatsky, Dynamically induced magnetism in $KTaO_3$, Phys. Rev. Res. 3, L022011 (2021).

[25] D. M. Juraschek, M. Fechner, A. V. Balatsky, and N. A. Spaldin, Dynamical multiferroicity, Phys. Rev. Mater. 1, 014401 (2017).

[26] D. M. Juraschek and N. A. Spaldin, Orbital magnetic mo- ments of phonons, Phys. Rev. Mater. 3, 064405 (2019).

[27] B. Cheng, T. Schumann, Y. Wang, X. Zhang, D. Bar- balas, S. Stemmer, and N. P. Armitage, A large effective phonon magnetic moment in a Dirac semimetal, Nano Letters 20, 5991 (2020).

[28] A. Baydin, F. G. G. Hernandez, M. Rodriguez-Vega, A. K. Okazaki, F. Tay, G. T. Noe, I. Katayama, J. Takeda, H. Nojiri, P. H. O. Rappl, E. Abramof, G. A. Fiete, and J. Kono, Magnetic control of soft chiral phonons in PbTe, Phys. Rev. Lett. 128, 075901 (2022).

[29] F. G. G. Hernandez, A. Baydin, S. Chaudhary, F. Tay, I. Katayama, J. Takeda, H. Nojiri, A. K. Okazaki, P. H. O. Rappl, E. Abramof, M. Rodriguez-Vega, G. A. Fiete, and J. Kono, Observation of interplay between phonon chirality and electronic band topology, Science Advances 9, eadj4074 (2023).

[30] F. Wu, S. Bao, J. Zhou, Y. Wang, J. Sun, J. Wen, Y. Wan, and Q. Zhang, Fluctuation-enhanced phonon magnetic moments in a polar antiferromagnet, Nature Physics 19, 1868 (2023).

[31] C. Tang, G. Ye, C. Nnokwe, M. Fang, L. Xiang, M. Mahjouri-Samani, D. Smirnov, E.-H. Yang, T. Wang, L. Zhang, R. He, and W. Jin, Exciton-activated effective phonon magnetic moment in monolayer mos2, Phys. Rev. B 109, 155426 (2024).

[32] H. Mustafa, C. Nnokwe, G. Ye, M. Fang, S. Chaud- hary, J.-A. Yan, K. Wu, C. J. Cunningham, C. M. Hemesath, A. J. Stollenwerk, P. M. Shand, E.-H. Yang, G. A. Fiete, R. He, and W. Jin, Origin of large effective phonon magnetic moments in monolayer mos2, ACS Nano 19, 11241 (2025), PMID: 40080689, https://doi.org/10.1021/acsnano.4c18906.

[33] L. Dong and Q. Niu, Geometrodynamics of electrons in a crystal under position and time-dependent deformation, Phys. Rev. B 98, 115162 (2018).

[34] L. Trifunovic, S. Ono, and H. Watanabe, Geometric or- bital magnetization in adiabatic processes, Phys. Rev. B 100, 054408 (2019).

[35] Y. Ren, C. Xiao, D. Saparov, and Q. Niu, Phonon mag- netic moment from electronic topological magnetization, Phys. Rev. Lett. 127, 186403 (2021).

[36] X.-W. Zhang, Y. Ren, C. Wang, T. Cao, and D. Xiao, Gate-tunable phonon magnetic moment in bilayer graphene, Phys. Rev. Lett. 130, 226302 (2023).

[37] S. Chaudhary, D. M. Juraschek, M. Rodriguez-Vega, and G. A. Fiete, Giant effective magnetic moments of chiral phonons from orbit-lattice coupling, Phys. Rev. B 110, 094401 (2024).

[38] Y. Su, A. V. Balatsky, and S.-Z. Lin, Quantum nonlinear acoustic hall effect and inverse acoustic faraday effect in dirac insulators, Phys. Rev. Lett. 134, 026304 (2025).

[39] H. Suzuura and T. Ando, Phonons and electron-phonon scattering in carbon nanotubes, Phys. Rev. B 65, 235412 (2002).

[40] M. Vozmediano, M. Katsnelson, and F. Guinea, Gauge fields in graphene, Physics Reports 496, 109 (2010).

[41] A. Cortijo, Y. Ferreirós, K. Landsteiner, and M. A. H. Vozmediano, Elastic gauge fields in weyl semimetals, Phys. Rev. Lett. 115, 177202 (2015).

[42] D. I. Pikulin, A. Chen, and M. Franz, Chiral anomaly from strain-induced gauge fields in dirac and weyl semimetals, Phys. Rev. X 6, 041021 (2016).

[43] A. G. Grushin, J. W. F. Venderbos, A. Vishwanath, and R. Ilan, Inhomogeneous weyl and dirac semimetals: Transport in axial magnetic fields and fermi arc surface states from pseudo-landau levels, Phys. Rev. X 6, 041046 (2016).

[44] T. L. Hughes, R. G. Leigh, and E. Fradkin, Torsional response and dissipationless viscosity in topological insu- lators, Phys. Rev. Lett. 107, 075502 (2011).

[45] M. Barkeshli, S. B. Chung, and X.-L. Qi, Dissipationless phonon Hall viscosity, Phys. Rev. B 85, 245107 (2012).

[46] H. Shapourian, T. L. Hughes, and S. Ryu, Viscoelastic response of topological tight-binding models in two and three dimensions, Phys. Rev. B 92, 165131 (2015).

[47] D. Liu and J. Shi, Circular phonon dichroism in weyl semimetals, Phys. Rev. Lett. 119, 075301 (2017).

[48] J. L. Mañes, Symmetry-based approach to electron- phonon interactions in graphene, Phys. Rev. B 76, 045430 (2007).

[49] S. Heidari, A. Cortijo, and R. Asgari, Hall viscosity for optical phonons, Phys. Rev. B 100, 165427 (2019).

[50] L.-H. Hu, J. Yu, I. Garate, and C.-X. Liu, Phonon helicity induced by electronic berry curvature in dirac materials, Phys. Rev. Lett. 127, 125901 (2021).

[51] W. Chen, X.-W. Zhang, Y. Su, T. Cao, D. Xiao, and S.- Z. Lin, Gauge theory of giant phonon magnetic moment in doped dirac semimetals, Phys. Rev. B 111, 035126 (2025).

[52] H. Weyl, Elektron und gravitation. i, Zeitschrift für Physik 56, 330 (1929).

[53] V. Fock, Geometrisierung der diracschen theorie des elek- trons, Zeitschrift für Physik 57, 261 (1929).

[54] S. Carroll, S. Carroll, and Addison-Wesley, Spacetime and Geometry: An Introduction to General Relativity (Addi- son Wesley, 2004).

[55] E. Fradkin, S. A. Kivelson, M. J. Lawler, J. P. Eisenstein, and A. P. Mackenzie, Nematic fermi fluids in condensed matter physics, Annual Review of Condensed Matter Physics 1, 153 (2010).

[56] T. L. Hughes, R. G. Leigh, and O. Parrikar, Torsional anomalies, hall viscosity, and bulk-boundary correspon- dence in topological states, Phys. Rev. D 88, 025040 (2013).

[57] See Supplemental Material at [URL] for details of Dirac fermions in curved space, tight-binding model, electron Hall viscosity, phonon dynamics, and computational de- tails.

[58] A. A. Zyuzin and A. A. Burkov, Topological response in weyl semimetals and the chiral anomaly, Phys. Rev. B 86, 115133 (2012).

[59] J. E. Avron, R. Seiler, and P. G. Zograf, Viscosity of quantum hall fluids, Phys. Rev. Lett. 75, 697 (1995).

[60] P. S. Alekseev, Negative magnetoresistance in viscous flow of two-dimensional electrons, Phys. Rev. Lett. 117, 166601 (2016).

[61] T. Scaffidi, N. Nandi, B. Schmidt, A. P. Mackenzie, and J. E. Moore, Hydrodynamic electron flow and hall viscosity, Phys. Rev. Lett. 118, 226601 (2017).

[62] F. M. D. Pellegrino, I. Torre, and M. Polini, Nonlocal transport and the hall viscosity of two-dimensional hydrodynamic electron liquids, Phys. Rev. B 96, 195401 (2017).

[63] Z. Wang, H. Weng, Q. Wu, X. Dai, and Z. Fang, Three-dimensional dirac semimetal and quantum transport in cd3as2, Phys. Rev. B 88, 125427 (2013).

[64] T. I. Tuegel and T. L. Hughes, Hall viscosity and momentum transport in lattice and continuum models of the integer quantum hall effect in strong magnetic fields, Phys. Rev. B 92, 165127 (2015).

[65] L. D. Landau and E. M. Lifshitz, Fluid Mechanics: Volume 6, Vol. 6 (Elsevier, 1987).

[66] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, et al., Quantum espresso: A modular and open-source software project for quantum simulations of materials, Journal of Physics: Condensed Matter 21, 395502 (2009).

[67] D. Hamann, Optimized norm-conserving vanderbilt pseudopotentials, Physical Review B 88, 085117 (2013).

[68] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Physical review letters 77, 3865 (1996).

[69] M. N. Ali, Q. Gibson, S. Jeon, B. B. Zhou, A. Yazdani, and R. J. Cava, The crystal and electronic structures of Cd₃As₂, the three-dimensional electronic analogue of graphene, Inorganic Chemistry 53, 4062 (2014).

[70] A. Togo, First-principles phonon calculations with phonopy and phono3py, Journal of the Physical Society of Japan 92, 012001 (2023).

[71] A. Togo, L. Chaput, T. Tadano, and I. Tanaka, Implementation strategies in phonopy and phono3py, Journal of Physics: Condensed Matter (2023).

# Supplemental Information for "Geometric Origin of Phonon Magnetic Moment in Dirac Materials"

## DIRAC FERMIONS IN CURVED SPACE

We briefly review the theory of Dirac fermions in curved space [S40, S52, S53]. In flat space, the Lagrangian density for Dirac fermions is given by $\mathcal{L}_D = \psi^\dagger \gamma^0 (i \gamma^A \partial_A - m) \psi$, where $\gamma^A$ are the gamma matrices, $m$ is the fermion mass, and $\psi$ is the Dirac spinor. In curved space, the Lagrangian is modified to incorporate the frame field and spin connection,

$$
\mathcal{L}_D = \det(\mathbf{e}) \psi^\dagger \gamma^0 \left[ i \gamma^A e_A^\mu(x) D_\mu - m \right] \psi, \tag{S1}
$$

where $e_A^\mu(x)$ is the frame field (or vielbein), $D_\mu = \partial_\mu + \Gamma_\mu$ is the covariant derivative, and $\Gamma_\mu$ is the geometric connection. The geometric connection is given by $\Gamma_\mu = \frac{1}{2} \omega_{AB\mu} \Sigma^{AB}$, where $\omega_{AB\mu}$ is the spin connection, and $\Sigma^{AB} = \frac{1}{4} [\gamma^A, \gamma^B]$ are the generators of the Lorentz group. The spin connection $\omega_{AB\mu}$ depends on the derivatives of the frame field $e_A^\mu(x)$ and ensures local Lorentz invariance in curved space.

The frame field $e_A^\mu(x)$ defines the local orthonormal basis vectors $\mathbf{e}_A$ in curved space by relating them to the global coordinate basis vectors $\hat{e}_\mu = \partial_\mu$ [S54]:

$$
\mathbf{e}_A = e_A^\mu(x) \hat{e}_\mu. \tag{S2}
$$

By construction, the $\mathbf{e}_A$ are orthonormal, such that their inner product satisfies $g(\mathbf{e}_A, \mathbf{e}_B) = \eta_{AB}$, which can be equivalently expressed as

$$
g^{\mu \nu} = e_A^\mu e_B^\nu \eta^{AB}, \tag{S3}
$$

where $g^{\mu \nu}$ is the metric tensor of the curved space and $\eta^{AB}$ is the Minkowski metric. Thus, the frame field $e_A^\mu(x)$ can be interpreted as the "square root" of the metric tensor.

The canonical momentum conjugate to the Dirac field $\psi$ is given by

$$
\Pi = \frac{\partial \mathcal{L}_D}{\partial (D_0 \psi)} = \det(\mathbf{e}) i \psi^\dagger \gamma^0 e_A^0(x) \gamma^A. \tag{S4}
$$

Using this, the Hamiltonian density can be written as

$$
\mathcal{H}_D = \Pi D_0 \psi - \mathcal{L}_D = \det(\mathbf{e}) \psi^\dagger \left[ (p_\mu - i \Gamma_\mu) e_A^\mu(x) \alpha^A + m \beta \right]. \tag{S5}
$$

For simplicity, we now restrict the global coordinates $\mu$ to two spatial dimensions $(x, y)$, and we choose the representation $\alpha^1 = \sigma^1$, $\alpha^2 = \sigma^2$, and $\beta = \sigma^3$. In this case, the Dirac Hamiltonian simplifies to

$$
H_{D}=\left(p_{\mu}-i \Gamma_{\mu}\right) e_{A}^{\mu}(x) \sigma^{A}+m \sigma^{3}. \tag{S6}
$$

Compared to the flat-space Dirac Hamiltonian, $H_D = p_\mu \sigma^\mu + m\sigma^3$, the geometric deformations in curved space are encoded in the frame field $e_A^\mu(x)$ and the geometric connection $\Gamma_\mu$, which itself is determined by the frame field.

Importantly, the geometric connection $\Gamma_\mu$ couples to the Dirac fermions in the same form as a gauge field $A_\mu$. In flat space, the gauge field enters the Dirac Hamiltonian as an explicit additional term $e\mathbf{A} \cdot \boldsymbol{\sigma}$. In curved space, however, the gauge field can be absorbed into the geometric connection by redefining $\Gamma_\mu' = \Gamma_\mu + ieA_\mu$. Thus, the Dirac Hamiltonian can be rewritten as

$$
\mathcal{H}_{D}=\left(p_{\mu}-i \Gamma_{\mu}\right) e_{A}^{\mu}(x) \sigma^{A}+m \sigma^{3}. \tag{S7}
$$

This shows that in the curved space formulation, gauge fields can be geometrized via a modified geometric connection.

In condensed matter systems, lattice distortions are the primary sources of emergent frame fields and spin connections, which provide a natural geometric framework to describe the coupling between lattice degrees of freedom and low-energy electronic excitations. These distortions can arise from both static and dynamic lattice phenomena.

One example involves topological defects in the crystal lattice, such as dislocations and disclinations [S56]. Disclinations, such as an isolated pentagon or heptagon ring in graphene, act as monopole sources of curvature in the effective geometry, giving rise to a nonzero spin connection felt by the electrons. Dislocations, which introduce a missing or extra half-plane of atoms, generate torsion fields by effectively translating the trajectory of electrons encircling the dislocation core. This torsion is mathematically described as the field strength associated with the frame field, reflecting the nontrivial topology of the lattice defect. Beyond defects, smoothly varying lattice distortions such as elastic strain can also generate effective frame fields and spin connections [S56]. Strain gradients modify the local metric and thus couple into the low-energy Dirac Hamiltonian, allowing for an elegant geometric description of strain-engineered electronic properties.

In this work, we focus on a dynamic and particularly relevant source of lattice distortion—phonons. Specifically, we consider optical phonon modes, which involve relative motions of atoms within the unit cell. In the long-wavelength limit, the distortions induced by such phonons effectively act as a uniform frame field, modifying the local geometry experienced by the electrons, while the corresponding spin connection remains negligible due to the absence of lattice curvature or torsion—like stretching a membrane without bending it.

# TIGHT-BINDING MODEL

In this section, we explicitly demonstrate how optical phonons can induce emergent gauge and frame fields coupled to Dirac fermions using a tight-binding model. We start from the $\mathbf{k} \cdot \mathbf{p}$ model for $\mathrm{Cd}_{3} \mathrm{As}_{2}$, which captures the essential band inversion between Cd-$5s$ and As-$4p$ orbitals near the $\Gamma$ point [S42, S63]. The basis consists of $\left|S_{\frac{1}{2}}, \frac{1}{2}\right\rangle,\left|P_{\frac{3}{2}}, \frac{3}{2}\right\rangle,\left|S_{\frac{1}{2}},-\frac{1}{2}\right\rangle,\left|P_{\frac{3}{2}},-\frac{3}{2}\right\rangle$, and the Hamiltonian is given by

$$
\mathcal{H}_{\Gamma}(\mathbf{k})=\varepsilon_{0}(\mathbf{k})+M(\mathbf{k}) \sigma^{z}+A k_{x} \tau^{z} \sigma^{x}+A k_{y} \sigma^{y}, \tag{S8}
$$

where $\varepsilon_{0}(\mathbf{k})=C_{0}+C_{1} k_{z}^{2}+C_{2}\left(k_{x}^{2}+k_{y}^{2}\right)$ and $M(\mathbf{k})=M_{0}+M_{1} k_{z}^{2}+M_{2}\left(k_{x}^{2}+k_{y}^{2}\right)$, with $C_{0,1,2}$ and $M_{0,1,2}$ the model parameters, and $\boldsymbol{\sigma}$ and $\boldsymbol{\tau}$ are Pauli matrices in the orbital and spin subspaces, respectively.

Due to the block-diagonal structure of the Hamiltonian, where spin-up and spin-down sectors are decoupled, we focus on the spin-up block formed by $\left|S_{\frac{1}{2}}, \frac{1}{2}\right\rangle$ and $\left|P_{\frac{3}{2}}, \frac{3}{2}\right\rangle$. By employing the standard lattice regularization:

$$
\begin{aligned}
k_{x, y} & \rightarrow \frac{1}{a} \sin \left(k_{x, y} a\right), \\
k_{x, y, z}^{2} & \rightarrow \frac{2}{a^{2}}\left[1-\cos \left(k_{x, y, z} a\right)\right],
\end{aligned} \tag{S9}
$$

we arrive at a tight-binding model on a cubic lattice with lattice constant $a$. The resulting lattice Hamiltonian is:

$$
\mathcal{H}(\mathbf{k})=\left[m_{0}+m_{z} \cos \left(k_{z} a\right)+m_{\perp} \cos \left(k_{x} a\right)+m_{\perp} \cos \left(k_{y} a\right)\right] \sigma^{z}+t \sin \left(k_{x} a\right) \sigma^{x}+t \sin \left(k_{y} a\right) \sigma^{y}, \tag{S10}
$$

where $m_0 = M_0 + 2M_1/a^2 + 4M_2/a^2$ is the on-site energy difference between the two orbitals, $m_z = -2M_1/a^2$ and $m_\perp = -2M_2/a^2$ are intra-orbital hopping amplitudes along the $z$ direction and in the $xy$ plane, respectively, and $t = A/a$ is the inter-orbital hopping amplitude.

This model features two spinless Dirac points at $\mathbf{K}_\chi = (0,0,\chi k_{z0})$, where $\chi = \pm 1$ labels the two valleys, and $\cos(k_{z0}a) = (m_0 + 2m_\perp)/m_z$ determines their location. Expanding the Hamiltonian around $\mathbf{K}_\chi$ yields:
$$
\mathcal{H}_\chi(\mathbf{k}) = \hbar v_F(k_x\sigma^x + k_y\sigma^y) + \chi\hbar v_z k_z\sigma^z, \tag{S11}
$$
where $v_F = ta/\hbar$ and $v_z = am_z\sin(k_{z0}a)/\hbar$. Despite the complexity of the actual $\text{Cd}_3\text{As}_2$ crystal structure, which has 80 atoms per unit cell, the essential low-energy physics can be captured by this minimal model with $s$- and $p$-orbitals placed on a cubic lattice.

We now transform the Hamiltonian $H = \sum_{\mathbf{k}} \psi_{\mathbf{k}}^\dagger \mathcal{H}(\mathbf{k}) \psi_{\mathbf{k}}$ into real space, yielding:
$$
\begin{aligned}
H &= \frac{1}{2} \sum_j \left[ \psi_{j+\mathbf{a}_x}^\dagger \left( it\sigma^x - m_\perp\sigma^z \right) \psi_j + h.c. \right] \\
&+ \frac{1}{2} \sum_j \left[ \psi_{j+\mathbf{a}_y}^\dagger \left( it\sigma^y - m_\perp\sigma^z \right) \psi_j + h.c. \right] \\
&+ \frac{1}{2} \sum_j \left[ \psi_{j+\mathbf{a}_z}^\dagger \left( -m_z\sigma^z \right) \psi_j + h.c. \right] + m_0 \sum_j \psi_j^\dagger \sigma^z \psi_j.
\end{aligned} \tag{S12}
$$

Here, $\psi_j^\dagger = (c_{j,s}^\dagger, c_{j,p}^\dagger)$, and $\mathbf{a}_{x,y,z}$ are the lattice vectors along each Cartesian direction.

In order to distinguish between the in-plane inversion-odd $(E_u)$ and inversion-even $(E_g)$ optical phonon modes, we formally double the unit cell along the $z$ direction to include two sites per unit cell. Phonon-induced lattice distortions affect the tight-binding model by modifying the hopping amplitudes. We focus on the modifications to the inter-orbital hoppings between the nearest neighbors, given by two-center Slater-Koster integrals $t_{ij} = \int d^3 r \, \psi_\alpha^*(\mathbf{r}-\mathbf{R}_i) H \psi_\beta(\mathbf{r}-\mathbf{R}_j)$, where $\mathbf{R}_j$ is the position of the $j$-th size, and $\psi_\alpha$ is the orbital wave function ($\alpha \neq \beta$). If the lattice is distorted, then the site positions $\mathbf{R}_j$ are replaced by $\mathbf{R}_j + \mathbf{u}_j$, where $\mathbf{u}_j$ is the displacement. Under the frozen phonon approximation and long-wavelength aprroximation, we can treat $\mathbf{u}_j$ as time-independent and site-independent.

Expanding $t_{ij}(\mathbf{u})$ to first order in $\mathbf{u}$, the modulations of the inter-orbital hopping matrices by optical phonons arises from two primary effects: bond stretching and relative rotation of the two orbitals [S41, S42, S46].

(1) Bond stretching. A phonon mode polarized along the direction $\hat{e}_1$ stretches the bond length between the neighboring sites, modifying the hopping amplitude in that direction. This leads to a change in the inter-orbital hopping matrix,
$$
t(\mathbf{u}) \sigma^1 \approx \left( t + u \frac{\partial t}{\partial a} \right) \sigma^1 = t \left( 1 - \frac{\beta u}{a} \right) \sigma^1, \tag{S13}
$$
where $a$ is the equilibrium bond length, and $\beta = -\partial \ln t / \ln a$ is the Grüneisen parameter that characterizes the strength of the bond stretching. In contrast, $t\sigma^2$—hopping along the orthogonal direction $\hat{e}_2$—is not affected by the bond-length change. If the phonon is polarized in arbitary direction not just along $x$- and $y$-axis, aside from the bond-length change, we also have the bond-angle change contribution. Since the phonon polarization is not neccessarily aligned with $x$- or $y$-axis, this contribution can be seen by projecting the deformed hopping matrices into the global Cartesian coordinates. Then the inter-orbital hopping matrices are modified as
$$
\begin{aligned}
t\sigma^x &\to t \left( 1 - \frac{\beta u}{a} \right) \cos\theta \, \sigma^1 - t \sin\theta \, \sigma^2, \\
t\sigma^y &\to t \left( 1 - \frac{\beta u}{a} \right) \sin\theta \, \sigma^1 + t \cos\theta \, \sigma^2,
\end{aligned} \tag{S14}
$$
where $\theta$ is the instantaneous angle between the displacement vector $\mathbf{u}$ and the $x$ axis. When the magnitude of the phonon displacement $u$ is zero, this modification is equivalent to a simple rotation of the Pauli matrices: $\sigma^x \to \cos\theta \sigma^1 - \sin\theta \sigma^2$ and $\sigma^y \to \sin\theta \sigma^1 + \cos\theta \sigma^2$. The bond stretching induced by nonzero phonon displacement $u$ modifies the hopping matrices anistropically.

(2) Relative rotation of the two orbitals, which only modifies the hopping amplitude between different types of orbitals. For our purpose of deriving the effects on the Dirac cones lying on the $z$-axis, the relevant modication is the

relative rotation of the $s$ and $p$ orbitals between neighboring sites in the $z$ direction. This relative rotation gives rise to a new inter-orbital hopping term along the $z$ direction, which can be expressed as

$$
\begin{aligned}
t_{i j, z}(\mathbf{u}) & \approx i \frac{\hat{y} \cdot\left(a \hat{z} \times u_{x} \hat{x}\right)}{a} \frac{\partial t}{\partial a} \sigma^{x}+i \frac{\hat{x} \cdot\left(u_{y} \hat{y} \times a \hat{z}\right)}{a} \frac{\partial t}{\partial a} \sigma^{y}, \\
& =i t \frac{\beta u_{x}}{a} \sigma^{x}+i t \frac{\beta u_{y}}{a} \sigma^{y}.
\end{aligned} \tag{S15}
$$

Inserting both the bond-stretching and orbital-rotation modifications into the original lattice Hamiltonian Eq. (S12), we obtain the deformed Hamiltonian under a phonon displacement field $\mathbf{u}$:

$$
\begin{aligned}
H(\mathbf{u}) & =\frac{1}{2} \sum_{j} \psi_{j+\mathbf{a}_{x}}^{\dagger}\left[i t\left(1-\frac{\beta u}{a}\right) \cos \theta \sigma^{1}-i t \sin \theta \sigma^{2}-m_{\perp} \sigma^{z}\right] \psi_{j}+\text { h.c. } \\
& +\frac{1}{2} \sum_{j} \psi_{j+\mathbf{a}_{y}}^{\dagger}\left[i t\left(1-\frac{\beta u}{a}\right) \sin \theta \sigma^{1}+i t \sin \theta \sigma^{2}-m_{\perp} \sigma^{z}\right] \psi_{j}+\text { h.c. } \\
& +\frac{1}{2} \sum_{j} \psi_{j+\mathbf{a}_{z}}^{\dagger}\left(i t \frac{\beta u_{x}}{a} \sigma^{x}+i t \frac{\beta u_{y}}{a} \sigma^{y}\right) \psi_{j} \pm \psi_{j-\mathbf{a}_{z}}^{\dagger}\left(i t \frac{\beta u_{x}}{a} \sigma^{x}+i t \frac{\beta u_{y}}{a} \sigma^{y}\right) \psi_{j}+\text { h.c. } \\
& +\frac{1}{2} \sum_{j} \psi_{j+\mathbf{a}_{z}}^{\dagger}\left(-m_{z} \sigma^{z}\right) \psi_{j}+\text { h.c. }+m_{0} \sum_{j} c_{j}^{\dagger} \sigma^{z} c_{j},
\end{aligned} \tag{S16}
$$

where the $\pm$ sign in the third line distinguishes the inversion-odd $E_{u}$ and inversion-even $E_{g}$ phonon modes, respectively. We now transform the Hamiltonian into momentum space. For the inversion-even $E_{g}$ mode, the resulting Hamiltonian reads:

$$
\begin{aligned}
H_{E_{g}}(\mathbf{u}) & =\sum_{\mathbf{k}} \psi_{\mathbf{k}}^{\dagger}\left[t \sin \left(k_{x} a\right)\left(1-\frac{\beta u}{a}\right) \cos \theta \sigma^{1}-t \sin \left(k_{x} a\right) \sin \theta \sigma^{2}\right] \psi_{\mathbf{k}} \\
& +\sum_{\mathbf{k}} \psi_{\mathbf{k}}^{\dagger}\left[t \sin \left(k_{y} a\right)\left(1-\frac{\beta u}{a}\right) \sin \theta \sigma^{1}+t \sin \left(k_{y} a\right) \cos \theta \sigma^{2}\right] \psi_{\mathbf{k}} \\
& +\sum_{\mathbf{k}} \psi_{\mathbf{k}}^{\dagger}\left[t \sin \left(k_{z} a\right) \frac{\beta}{a}\left(u_{x} \sigma^{x}+u_{y} \sigma^{y}\right)\right] \psi_{\mathbf{k}} \\
& +\sum_{\mathbf{k}} \psi_{\mathbf{k}}^{\dagger}\left[m_{\perp} \cos \left(k_{x} a\right)+m_{\perp} \cos \left(k_{y} a\right)+m_{z} \cos \left(k_{z} a\right)+m_{0}\right] \sigma^{z} \psi_{\mathbf{k}}.
\end{aligned} \tag{S17}
$$

Expanding the above Hamiltonian near the Dirac point $\mathbf{K}_{\chi}$, we arrive at the continuum limit:

$$
\begin{aligned}
\mathcal{H}_{E_{g}}(\mathbf{k}, \mathbf{u}) & =\hbar v_{F} k_{x}\left(1-\frac{\beta u}{a}\right) \cos \theta \sigma^{1}+\hbar v_{F} k_{x}(-\sin \theta) \sigma^{2} \\
& +\hbar v_{F} k_{y}\left(1-\frac{\beta u}{a}\right) \sin \theta \sigma^{1}+\hbar v_{F} k_{y} \cos \theta \sigma^{2} \\
& -\chi t \beta k_{z 0}\left(u_{x} \sigma^{x}+u_{y} \sigma^{y}\right)+\chi \hbar v_{z} k_{z} \sigma^{z},
\end{aligned} \tag{S18}
$$

For the inversion-odd $E_{u}$ mode, the relative rotation of the $s$ and $p$ orbitals along the $z$ direction results in the term:

$$
\frac{1}{2} \sum_{j} \psi_{j+\mathbf{a}_{z}}^{\dagger}\left(i t \frac{\beta u_{x}}{a} \sigma^{x}+i t \frac{\beta u_{y}}{a} \sigma^{y}\right) \psi_{j}+\psi_{j-\mathbf{a}_{z}}^{\dagger}\left(i t \frac{\beta u_{x}}{a} \sigma^{x}+i t \frac{\beta u_{y}}{a} \sigma^{y}\right) \psi_{j}+\text { h.c. }, \tag{S19}
$$

which cancels exactly in momentum space. This results in a vanishing emergent gauge field for the $E_{u}$ mode. The resulting momentum-space Hamiltonian for the $E_{u}$ mode is therefore:

$$
\begin{aligned}
H_{E_{u}}(\mathbf{k}, \mathbf{u}) & =\sum_{\mathbf{k}} \psi_{\mathbf{k}}^{\dagger}\left[t \sin \left(k_{x} a\right)\left(1-\frac{\beta u}{a}\right) \cos \theta \sigma^{1}-t \sin \left(k_{x} a\right) \sin \theta \sigma^{2}\right] \psi_{\mathbf{k}} \\
& +\sum_{\mathbf{k}} \psi_{\mathbf{k}}^{\dagger}\left[t \sin \left(k_{y} a\right)\left(1-\frac{\beta u}{a}\right) \sin \theta \sigma^{1}+t \sin \left(k_{y} a\right) \cos \theta \sigma^{2}\right] \psi_{\mathbf{k}} \\
& +\sum_{\mathbf{k}} \psi_{\mathbf{k}}^{\dagger}\left[m_{\perp} \cos \left(k_{x} a\right)+m_{\perp} \cos \left(k_{y} a\right)+m_{z} \cos \left(k_{z} a\right)+m_{0}\right] \sigma^{z} \psi_{\mathbf{k}}.
\end{aligned} \tag{S20}
$$

And its continuum limit becomes
$$
\begin{aligned}
\mathcal{H}_{E_{u}}(\mathbf{k}, \mathbf{u})= & \hbar v_{F} k_{x}\left(1-\frac{\beta u}{a}\right) \cos \theta \sigma^{1}+\hbar v_{F} k_{x}(-\sin \theta) \sigma^{2} \\
& +\hbar v_{F} k_{y}\left(1-\frac{\beta u}{a}\right) \sin \theta \sigma^{1}+\hbar v_{F} k_{y} \cos \theta \sigma^{2} \\
& +\chi \hbar v_{z} k_{z} \sigma^{3}.
\end{aligned}
\tag{S21}
$$

We compare the two effective Hamiltonians to the general Dirac Hamiltonian in curved space
$$
\mathcal{H}=v_{F}\left(p_{\mu}-e A_{\mu}-i \Gamma_{\mu}\right) e_{A}^{\mu} \sigma^{A},
\tag{S22}
$$
where $A_{\mu}$ is the gauge field, $e_{A}^{\mu}$ is the frame field (vierbein), and $\Gamma_{\mu}$ involves the spin connection. We find that the spin connection is zero, and both modes exhibit a frame field $e_{A}^{\mu}$, given by
$$
e_{A}^{\mu}=\left[\begin{array}{cc}
\left(1-\frac{\beta u}{a}\right) \cos \theta & \left(1-\frac{\beta u}{a}\right) \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right].
\tag{S23}
$$

In addition, only the $E_{g}$ mode supports an emergent gauge field:
$$
\chi a_{x}=\chi \frac{t \beta k_{z 0}}{v_{F}} u_{x}, \quad \chi a_{y}=\chi \frac{t \beta k_{z 0}}{v_{F}} u_{y}.
\tag{S24}
$$

This contrast between the two modes is a consequence of symmetry. In general, the emergent gauge field must be compatible with the little group at the Dirac point $\mathbf{K}_{\chi}$. In our model, the little group consists of $C_{4 z}$ and the combined operation $T \times I$, where $C_{4 z}$ is a fourfold rotation around the $z$ axis, $T$ is time-reversal, and $I$ is inversion. Both the electron momentum $\mathbf{k}$ and the phonon displacement $\mathbf{u}$ transform identically under $C_{4 z}$. Under $T \times I$, $\hbar \mathbf{k}$ is even, and the valley index $\chi$ is also even. Therefore, for the combination $\chi \mathbf{u}$ to couple as a gauge field, $\mathbf{u}$ must be inversion even. This symmetry requirement prohibits the inversion-odd $E_{u}$ mode from coupling as an emergent gauge field, while allowing the inversion-even $E_{g}$ mode.

# ELECTRON HALL VISCOSITY

## Integrating out the fermions

To quantitatively formulate how the Hall viscosity of the Dirac fluid modifies the phonon dynamics, we integrate out the Dirac fermions in the presence of a frame field using low-energy field theories. Since the frame field $e_{A}^{\mu}$ is dimensionless, the Hall viscosity coefficient $\eta_{H}$ must be scaled by $1 /[\text { length }]^{2}$. A closely related problem has been extensively studied in the context of the quantum Hall effect, where the Hall viscosity arises from integrating out electrons in a magnetic field [S59]. In that case, the Hall viscosity is found to be quantized in units of $\hbar / 8 \pi l_{B}^{2}$, with the characteristic length scale set by the magnetic length $l_{B}$.

More relevant to our case is the Dirac fermion coupled to a static frame field. Refs. [S44, S56] showed that, by integrating out massive Dirac fermions in a Chern insulator, an effective topological action for the frame field is obtained:
$$
S_{H}\left[e_{\mu}^{A}\right]=\frac{\eta_{H}}{2} \int d^{3} x, \epsilon^{\mu \nu \rho} e_{\mu}^{A} \partial_{\nu} e_{\rho}^{B} \delta_{A B},
\tag{S25}
$$
where $\epsilon^{\mu \nu \rho}$ is the Levi-Civita symbol and $\delta_{A B}$ is the Kronecker delta in the local tangent space. In this case, the Hall viscosity is given by $\eta_{H}=\hbar /\left(8 \pi l_{m}^{2}\right)$, where $l_{m}=\hbar v_{F} / m$ is the length scale associated with the time-reversal symmetry breaking Dirac mass $m$. By stacking Chern insulators in momentum space, this effective action can also be generalized to describe the (3+1)-dimensional Dirac system considered here [S58].

Additionally, the Hall viscosity for massless Dirac fermions in the presence of a magnetic field and geometric deformations has been studied in Ref. [S64]. In this setup, the contribution to the Hall viscosity from each Landau level is found to be:
$$
\eta_{H}^{(0)}=\frac{\hbar}{8 \pi l_{B}^{2}}, \quad \text { and } \quad \eta_{H}^{(n \neq 0)}=\frac{\hbar|n|}{4 \pi l_{B}^{2}}.
\tag{S26}
$$

Summing over the filled Landau levels up to a filling fraction $\nu = \hbar n_e/eB$, the total Hall viscosity becomes:

$$
\eta_H = \frac{\hbar \nu}{8\pi l_B^2}. \tag{S27}
$$

These results describe the Hall viscosity in the strong-field (quantum Hall) regime, where the Landau levels are well-resolved. They provide the foundation for our subsequent semiclassical analysis in the weak-field limit.

## Semiclassical limit of Hall viscosity

In the semiclassical regime, where the magnetic field is weak and the Landau level filling fraction is large, the Hall viscosity can be calculated using the Boltzmann transport equation [S60-S62]. Hall viscosity characterizes the antisymmetric part of the stress response of the electron fluid when time-reversal symmetry is broken. The stress tensor in such a fluid can be expressed as $-P\delta_{ij} + T_{ij}$, where $P$ is the static pressure and $T_{ij}$ is the shear stress tensor [S65]. Within the semiclassical framework, the shear stress tensor can be written as

$$
\mathbf{T} = \mathcal{N}_0 p_F v_F \int \frac{d\phi_p}{2\pi} \mathcal{F}(\mathbf{r}, \phi_p, t) \begin{pmatrix}
\cos^2 \phi_p & \cos \phi_p \sin \phi_p \\
\sin \phi_p \cos \phi_p & \sin^2 \phi_p
\end{pmatrix}, \tag{S28}
$$

where $\mathcal{N}_0$ is the density of states at the Fermi energy, $p_F$ is the Fermi momentum, and $\phi_p$ is the angular coordinate of the electron momentum $\mathbf{p}$. Here, $\mathcal{F}(\mathbf{r}, \phi_p, t)$ describes the deviation from the equilibrium distribution function $f_0(\varepsilon)$ and is defined via

$$
f(\mathbf{r}, \mathbf{p}, t) = f_0(\varepsilon) - \frac{\partial f_0}{\partial \varepsilon} \mathcal{F}(\mathbf{r}, \phi_p, t). \tag{S29}
$$

The evolution of $\mathcal{F}(\mathbf{r}, \phi_p, t)$ is governed by the linearized Boltzmann equation,

$$
\frac{\partial \mathcal{F}}{\partial t} + \mathbf{v}_p \cdot \nabla \mathcal{F} + \omega_c \frac{\partial \mathcal{F}}{\partial \phi_p} = \mathcal{I}[\mathcal{F}], \tag{S30}
$$

where $\mathbf{v}_p = \nabla_p \varepsilon$ is the electron velocity, $\omega_c = eB/m^*$ is the cyclotron frequency arising from the external magnetic field $B$, and $\mathcal{I}[\mathcal{F}]$ denotes the collision integral.

To analyze the angular momentum channels of Fermi surface deformation, we expand $\mathcal{F}(\mathbf{r}, \phi_p, t)$ in angular harmonics:

$$
\mathcal{F}(\mathbf{r}, \phi_p, t) = \sum_{l=-\infty}^{+\infty} e^{-il\phi_p} \mathcal{F}_l(\mathbf{r}, t). \tag{S31}
$$

Expressed in terms of these components, the shear stress tensor becomes

$$
\mathbf{T} = \frac{\mathcal{N}_0 p_F v_F}{4} \begin{pmatrix}
2\mathcal{F}_0 + \mathcal{F}_2 + \mathcal{F}_{-2} & i\mathcal{F}_2 - i\mathcal{F}_{-2} \\
-i\mathcal{F}2 + i\mathcal{F}-2 & 2\mathcal{F}0 - \mathcal{F}2 - \mathcal{F}-2
\end{pmatrix}. \tag{S32}
$$

In the hydrodynamic regime, the collision integral can be approximated in linearized form. By truncating the expansion at $|l| = 2$ and assuming a relaxation time approximation, we obtain

$$
\mathcal{F}_{\pm 2} = -\frac{v_F}{2} \frac{(\partial_x \mp i\partial_y) \mathcal{F}_{\pm 1}(\mathbf{r})}{1/\tau \pm 2i\omega_c}, \tag{S33}
$$

where $\tau$ is the transport lifetime. Thus, the total shear stress can be expressed as:

$$
\mathbf{T} = \frac{\mathcal{B}}{\bar{n}} n(\mathbf{r}) + \sigma'(\mathbf{r}), \tag{S34}
$$

where $\mathcal{B}$ is the bulk modulus, $\bar{n}$ is the average density, and $\sigma'$ is the traceless shear stress given by

$$
\begin{aligned}
\boldsymbol{\sigma}' = & m^* \nu_s \begin{pmatrix}
\partial_x J_x - \partial_y J_y & \partial_x J_y + \partial_y J_x \\
\partial_x J_y + \partial_y J_x & -\partial_x J_x + \partial_y J_y
\end{pmatrix} \\
& + m^* \nu_H \begin{pmatrix}
\partial_x J_y + \partial_y J_x & -\partial_x J_x + \partial_y J_y \\
\partial_x J_x - \partial_y J_y & -\partial_x J_y - \partial_y J_x
\end{pmatrix},
\end{aligned} \tag{S35}
$$


where $\mathbf{J}$ is the electron current density. The kinetic (dissipative) shear viscosity is given by

$$
\nu_{s}=\frac{v_{F}^{2}}{4} \frac{\tau}{1+4 \omega_{c}^{2} \tau^{2}}, \tag{S36}
$$

and the kinetic Hall (nondissipative) viscosity is

$$
\nu_{H}=\frac{v_{F}^{2}}{2} \frac{\omega_{c} \tau^{2}}{1+4 \omega_{c}^{2} \tau^{2}}. \tag{S37}
$$

Finally, the Hall viscosity is related to the kinetic Hall viscosity $\nu_{H}$ by

$$
\eta_{H}=n_{e} m^{*} \nu_{H} \tag{S38}
$$

By its definition, the Hall viscosity quantifies the shear stress response of the electron fluid to the quadrupolar (elliptic) deformation of the Fermi surface—captured by the $l=\pm 2$ harmonic component of $\mathcal{F}$. Phonons, when they couple to electrons as metric perturbations or frame fields in the low-energy theory, induce precisely such elliptic deformations of the Fermi surface and thus generate a Hall viscosity response in the electron fluid.

### Nematic Fermi surface

To show how the phonon-induced frame field deforms the electron fluid into a nematic Fermi surface, we consider the following effective Hamiltonian describing Dirac fermions coupled to a general frame field in two dimensions

$$
\begin{aligned}
\mathcal{H} & =\hbar v_{F}\left(k_{x} e_{1}^{x}+k_{y} e_{1}^{y}\right) \sigma^{1}+\hbar v_{F}\left(k_{x} e_{2}^{x}+k_{y} e_{2}^{y}\right) \sigma^{2}-\varepsilon_{F} \\
& =h_{1} \sigma^{1}+h_{2} \sigma^{2}-\varepsilon_{F}.
\end{aligned} \tag{S39}
$$

Here, $e_{A}^{\mu}$ represents the frame field components that encode the local deformation of the electron system, while $\sigma^{1,2}$ are Pauli matrices acting in the orbital space. The resulting energy dispersion is given by

$$
\begin{aligned}
\pm \varepsilon(\mathbf{k}) & = \pm \sqrt{h_{1}^{2}+h_{2}^{2}}-\varepsilon_{F} \\
& = \pm \sqrt{h_{A} h_{B} \delta^{A B}}-\varepsilon_{F} \\
& = \pm \hbar v_{F} \sqrt{k_{\mu} k_{\nu} e_{A}^{\mu} e_{B}^{\nu} \delta^{A B}}-\varepsilon_{F} \\
& = \pm \hbar v_{F} \sqrt{k_{\mu} k_{\nu} g^{\mu \nu}}-\varepsilon_{F},
\end{aligned} \tag{S40}
$$

where we have introduced the effective metric tensor $g^{\mu \nu}=e_{A}^{\mu} e_{B}^{\nu} \delta^{A B}$ that captures the anisotropic deformation of the Fermi surface induced by the frame field. At the Fermi energy, the electron states form a Fermi surface defined by the condition $\varepsilon(\mathbf{k})=0$, which can be compactly written as

$$
g^{\mu \nu} k_{\mu} k_{\nu}=\frac{\varepsilon_{F}^{2}}{\hbar^{2} v_{F}^{2}}. \tag{S41}
$$

Thus, the frame field modifies the Fermi surface through the induced metric tensor.

Explicitly, the metric tensor resulting from the phonon-induced frame field takes the form:

$$
g^{\mu \nu}=\left[\begin{array}{cc}
\left(1-\frac{\beta u}{a}\right)^{2} \cos ^{2} \theta+\sin ^{2} \theta & \left(1-\frac{\beta u}{a}\right)^{2} \cos \theta \sin \theta-\sin \theta \cos \theta \\
\left(1-\frac{\beta u}{a}\right)^{2} \sin \theta \cos \theta-\cos \theta \sin \theta & \left(1-\frac{\beta u}{a}\right)^{2} \sin ^{2} \theta+\cos ^{2} \theta
\end{array}\right]. \tag{S42}
$$

In the absence of phonon displacement $(u=0)$, the metric reduces to the identity matrix:

$$
g^{\mu \nu, \text { equi }}=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right], \tag{S43}
$$

which corresponds to an isotropic, circular Fermi surface. Treating the phonon displacement $u$ as a small perturbation, we expand the metric tensor to linear order in $u$:

$$
\delta g^{\mu \nu}=-\frac{2 \beta u}{a}\left[\begin{array}{cc}
\cos ^{2} \theta & \cos \theta \sin \theta \\
\sin \theta \cos \theta & \sin ^{2} \theta
\end{array}\right]. \tag{S44}
$$

The deformation of the Fermi surface encoded in $\delta g^{\mu\nu}$ can be decomposed into two distinct components:

$$
\delta g^{\mu\nu} = \delta g^{\mu\nu,(0)} + \delta g^{\mu\nu,(2)}, \tag{S45}
$$

where $\delta g^{\mu\nu,(0)}$ is the isotropic part corresponding to a uniform dilation or contraction of the Fermi surface (angular momentum $l=0$):

$$
\delta g^{\mu\nu,(0)} = -\frac{\beta u}{a} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \tag{S46}
$$

and $\delta g^{\mu\nu,(2)}$ is the traceless part corresponding to an anisotropic, elliptic deformation with angular momentum $l=2$:

$$
\delta g^{\mu\nu,(2)} = -\frac{\beta u}{a} \begin{bmatrix} \cos(2\theta) & \sin(2\theta) \\ \sin(2\theta) & -\cos(2\theta) \end{bmatrix}. \tag{S47}
$$

This quadrupolar component, $\delta g^{\mu\nu,(2)}$, describes a nematic distortion of the Fermi surface that preserves its area but breaks rotational symmetry, transforming a circular Fermi surface into an elliptical one. Such a deformation is essential for the phonon to couple to the Hall viscosity channel, as it generates the necessary $l=2$ harmonic of the Fermi surface that gives rise to the nondissipative transverse viscous stress.

## PHONON DYNAMICS

In this section, we show how the phonon dynamics is modified by the Hall viscosity of the electron fluid when the phonon acts as a dynamic frame field. In the long-wavelength limit, the phonon displacement field $\mathbf{u}$ can be described by the following effective action for an optical phonon mode

$$
S_{0}[\mathbf{u}] = \frac{1}{2} \int dtd^{2}x\ \rho_{I} \left( \dot{\mathbf{u}}^{2} - \omega_{0}^{2}\mathbf{u}^{2} \right), \tag{S48}
$$

where $\rho_I$ is the ion mass density, $\omega_0$ is the bare phonon frequency, and $\mathbf{u}$ is the in-plane phonon displacement field.

When the phonon modulates the local electronic geometry via the frame field, its effect can be encoded in the coframe field $e_{\mu}^{A}$, defined as the inverse of the frame field $e_{A}^{\mu}$, satisfying $e_{\mu}^{A}e_{B}^{\mu} = \delta_{B}^{A}$. To leading order in the phonon displacement, the coframe field can be calculated by matrix inversion:

$$
\begin{pmatrix} e_{x}^{1} & e_{x}^{2} \\ e_{y}^{1} & e_{y}^{2} \end{pmatrix} = \begin{pmatrix} e_{1}^{x} & e_{1}^{y} \\ e_{2}^{x} & e_{2}^{y} \end{pmatrix}^{-1} \approx \begin{bmatrix} \left( 1+\frac{\beta u}{a} \right)\cos\theta & -\sin\theta \\ \left( 1+\frac{\beta u}{a} \right)\sin\theta & \cos\theta \end{bmatrix}. \tag{S49}
$$

Here, the coframe field can be separated into an equilibrium part and a perturbation induced by the phonon,

$$
e_{\mu}^{A} = \delta_{\mu}^{A} + w_{\mu}^{A} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} + \begin{bmatrix} \frac{\beta u}{a}\cos\theta & 0 \\ \frac{\beta u}{a}\sin\theta & 0 \end{bmatrix}. \tag{S50}
$$

Substituting this into the effective Hall viscosity action for the frame field, we obtain

$$
\begin{aligned}
S_{H}[\mathbf{u}] &= \frac{\eta_{H}}{2} \int dtd^{2}x\ \epsilon^{\mu\nu\rho}w_{\mu}^{A}\partial_{\nu}w_{\rho}^{B}\delta_{AB} \\
&= \frac{\eta_{H}\beta^{2}}{2a^{2}} \int dtd^{2}x\ \epsilon^{\mu\nu\rho}u_{\mu}\partial_{\nu}u_{\rho},
\end{aligned} \tag{S51}
$$

where $\eta_H$ is the electron Hall viscosity coefficient, and $\epsilon^{\mu\nu\rho}$ is the Levi-Civita tensor. Because $\mu,\rho$ are restricted to spatial components $(x,y)$ and $\epsilon^{\mu\nu\rho}$ is fully antisymmetric, only the temporal derivative term survives with $\nu=t$. Thus, the Hall viscosity term contributes an additional term that couples the phonon velocity and displacement via a time-reversal symmetry breaking term.

The total phonon effective action is then given by

$$
S_{\text{eff}}[\mathbf{u}] = S_{0}[\mathbf{u}] + S_{H}[\mathbf{u}]. \tag{S52}
$$

From this, the effective Lagrangian becomes
$$
\mathcal{L}_{\text {eff }}=\frac{1}{2} \rho_{I}\left(\dot{\mathbf{u}}^{2}-\omega_{0}^{2} \mathbf{u}^{2}\right)+\frac{\eta_{H} \beta^{2}}{2 a^{2}} \mathbf{u} × \dot{\mathbf{u}}. \tag{S53}
$$

The phonon equation of motion is obtained by varying this effective action
$$
\rho_{I}\left(\ddot{\mathbf{u}}+\omega_{0}^{2} \mathbf{u}\right)=\frac{\eta_{H} \beta^{2}}{2 a^{2}} \dot{\mathbf{u}} × \hat{z}. \tag{S54}
$$

This equation describes a phonon mode subjected to a transverse force, leading to a lifting of degeneracy between left-handed and right-handed circularly polarized modes. Solving the equation of motion in the chiral basis defined by $u_{\pm} \equiv\left(u_{x} \pm i u_{y}\right) / \sqrt{2}$, the phonon frequencies are found to be:
$$
\omega_{ \pm}=\sqrt{\omega_{0}^{2}+\left(\frac{\beta^{2}}{2 a^{2} \rho_{I}} \eta_{H}\right)^{2}} \pm \frac{\beta^{2}}{2 a^{2} \rho_{I}} \eta_{H}. \tag{S55}
$$

Thus, the phonon frequency splitting is given by
$$
\delta \omega=\frac{\beta^{2}}{a^{2} \rho_{I}} \eta_{H}, \tag{S56}
$$
which is directly proportional to the electron Hall viscosity. This result reveals how the phonon dynamics, in the presence of an emergent frame field, provides a direct probe of the Hall viscosity through a measurable splitting of the chiral phonon modes.

## COMPUTATIONAL DETAILS
### First-principles methods

In this section, we present numerical details on the electron band structures, phonon spectra, and electron-phonon coupling. All DFT calculations are performed within the QUANTUM ESPRESSO package [S66]. For Cd₃As₂, we employ the optimized norm-conserving Vanderbilt (ONCV) pseudopotential [S67] and the Perdew-Burke-Ernzerhof (PBE) functional [S68]. Atomic structural parameters are obtained from Ref. [S69]. An energy cut-off of 100 Ry and a $k$-grid of $2 × 2 × 2$ are used for self-consistent calculations. The electronic band structure is shown in Fig. S1(a).

Phonon dispersions and eigenvectors are calculated based on the finite-displacement approach using the PHONONPY package [S70, S71]. We construct two linearly polarized modes from the doubly degenerate $E_{u}$ modes at the $\Gamma$ point and displace atoms along the phonon eigenvectors with an amplitude of $1$ Å. Due to the considerable computational cost, we initially use a $k$-grid of $11 × 11$ in DFT calculations to obtain the in-plane contour plot of the Dirac cone perpendicular to the $\Gamma$-$Z$ direction as in Fig. S1 (b) and (c), subsequently interpolating the map to a $100 × 100$ $k$-grid.

### Electron-phonon coupling in Cd₃As₂

We start from the many-body Hamiltonian of electrons and ions at equilibrium positions, $H = H_{\mathrm{e}} + H_{\mathrm{ion}} + H_{\mathrm{ei}}$, where $H_{\mathrm{ei}} = \sum_{i \mathbf{R} \alpha} V_{\mathrm{ei}}(\mathbf{r}_{i} - \mathbf{R} - \boldsymbol{\tau}_{\alpha})$ is the electron-ion interaction Hamiltonian. Here $\mathbf{R}$ is the lattice vector for unit cells and $\boldsymbol{\tau}_{\alpha}$ is the position of ion $\alpha$ within a unit cell. If the ions vibrate, $H_{\mathrm{ei}}$ will change to $\sum_{i \mathbf{R} \alpha} V_{\mathrm{ei}}(\mathbf{r}_{i} - \mathbf{R} - \boldsymbol{\tau}_{\alpha} + \mathbf{u}_{\mathbf{R} \alpha})$, where $\mathbf{u}_{\mathbf{R} \alpha}$ is the atomic displacement of the ion $\alpha$ in the unit cell $\mathbf{R}$ from its equilibrium position. It is usually small compared to the lattice constant, allowing us to expand the potential to the first order of $\mathbf{u}_{\mathbf{R} \alpha}$ as $\sum_{i \mathbf{R} \alpha} V_{\mathrm{ei}}(\mathbf{r}_{i} - \mathbf{R} - \boldsymbol{\tau}_{\alpha}) + \mathbf{u}_{\mathbf{R} \alpha} \cdot \nabla V_{\mathrm{ei}}(\mathbf{r}_{i} - \mathbf{R} - \boldsymbol{\tau}_{\alpha}) + O(\mathbf{u}_{\mathbf{R} \alpha}^{2})$. Thus the electron-phonon coupling Hamiltonian comes from the first-order correction,
$$
H_{e-\mathrm{ph}} = \sum_{i \mathbf{R} \alpha} \mathbf{u}_{\mathbf{R} \alpha} \cdot \nabla V_{\mathrm{ei}}(\mathbf{r}_{i} - \mathbf{R} - \boldsymbol{\tau}_{\alpha}) = \int d \mathbf{r} \rho(\mathbf{r}) \sum_{\mathbf{R} \alpha} \delta \mathbf{u}_{\mathbf{R} \alpha} \cdot \nabla V_{\mathrm{ei}}(\mathbf{r}_{i} - \mathbf{R} - \boldsymbol{\tau}_{\alpha}), \tag{S57}
$$
where $\rho(\mathbf{r})$ is the density operator of electrons, and $\rho(\mathbf{r}) = \sum_{i} \delta(\hat{\mathbf{r}}_{i} - \mathbf{r})$ in the coordinate representation. Now we move to the second quantization of density operator $\rho(\mathbf{r}) = \psi^{\dagger}(\mathbf{r}) \psi(\mathbf{r})$. The field operator projected to Bloch electronic basis

![](./images/1130109165553844237_3.jpg)

Fig. S1. (a)Electronic band structure of $Cd_3As_2$ showing one Dirac point $\boldsymbol{K}_+$ on the $\Gamma$-$Z$ axis. (b)(c) In-plane contour plots of the Dirac cone perpendicular to the $\Gamma$-$Z$ direction on a $k$-grid of $11\times11$ calculations using the DFT in equilibrium and in the presence of the $\Gamma_8(E_u)$ mode.

is $\psi^{\dagger}(\mathbf{r})=\sum_{n\mathbf{k}}\psi_{n\mathbf{k}}^{*}(\mathbf{r})c_{n\mathbf{k}}^{\dagger}$, where $n$ is the energy band index and $\mathbf{k}$ is electronic wavevector. The Bloch wavefunctions are given by $\psi_{n\mathbf{k}}(\mathbf{r})=u_{n\mathbf{k}}(\mathbf{r})e^{i\mathbf{k}\cdot\mathbf{r}}$, where $u_{n\mathbf{k}}=\langle\mathbf{r}|n\mathbf{k}\rangle$ is the periodic Bloch function within one unit cell. Under this representation, the electron-phonon coupling Hamiltonian becomes

$$
H_{e\mathrm{-ph}}=\sum_{nm}\sum_{\mathbf{k}\mathbf{k}'}\int d\mathbf{r}\psi_{n\mathbf{k}}^{*}(\mathbf{r})\sum_{\mathbf{R}\alpha}\mathbf{u}_{\mathbf{R}\alpha}\cdot\nabla V_{\mathrm{ei}}(\mathbf{r}_{i}-\mathbf{R}-\boldsymbol{\tau}_{\alpha})\psi_{m\mathbf{k}'}(\mathbf{r})c_{n\mathbf{k}}^{\dagger}c_{m\mathbf{k}'}.\tag{S58}
$$

Now we expand the atomic displacement of the ion at $\mathbf{R}+\boldsymbol{\tau}_{\alpha}$ in terms of the vibrational modes,

$$
\mathbf{u}_{\mathbf{R}\alpha}=\sum_{\mathbf{q},\nu}\sqrt{\frac{M_{0}}{NM_{\alpha}}}e^{i\mathbf{q}\cdot\mathbf{R}}\boldsymbol{\xi}_{\alpha}^{(\nu)}(\mathbf{q})u_{\mathbf{q}}^{(\nu)},\tag{S59}
$$

where $\mathbf{q}$ is the phonon wavevector, $\nu$ labels the normal modes, $\omega_{\mathbf{q}}^{(\nu)}$ is the frequency dispersion, and $M_0$ is an arbitary reference mass (typicall chosen to be the proton mass), and $u_{\mathbf{q}}^{(\nu)}$ is the complex normal coordinate of the displacement projected onto the normal mode $\nu$. The column vector $\boldsymbol{\xi}_{\alpha}^{(\nu)}(\mathbf{q})$ is the normal mode eigenvector that solves the dynamic matrix problem, $\sum_{\alpha'}D_{\alpha\alpha'}(\mathbf{q})\boldsymbol{\xi}_{\alpha'}^{(\nu)}(\mathbf{q})=\omega_{\mathbf{q}}^{(\nu)2}\boldsymbol{\xi}_{\alpha}^{(\nu)}(\mathbf{q})$, The quantization of the phonons is given by

$$
u_{\mathbf{q}}^{(\nu)}=l_{\mathbf{q}}^{(\nu)}[a_{\mathbf{q}}^{(\nu)}+a_{-\mathbf{q}}^{(\nu)\dagger}]=\sqrt{\frac{\hbar}{2M_{0}\omega_{\mathbf{q}}^{(\nu)}}}[a_{\mathbf{q}}^{(\nu)}+a_{-\mathbf{q}}^{(\nu)\dagger}],\tag{S60}
$$

where $l_{\mathbf{q}}^{(\nu)}$ is the "zero-point" displacement amplitude. We arrives at the Frölich Hamiltonian for the electron-phonon coupling,

$$
H_{e\mathrm{-ph}}=\frac{1}{\sqrt{N}}\sum_{nm\mathbf{k}}\sum_{\mathbf{q},\nu}g_{mn}^{(\nu)}(\mathbf{k},\mathbf{q})Q_{\mathbf{q}}^{(\nu)}c_{n\mathbf{k}+\frac{\mathbf{q}}{2}}^{\dagger}c_{m\mathbf{k}-\frac{\mathbf{q}}{2}},\tag{S61}
$$

where the electron-phonon coupling matrix element is given by

$$
g_{mn}^{(\nu)}(\mathbf{k},\mathbf{q})=\left\langle n\mathbf{k}+\frac{\mathbf{q}}{2}\right|(\nabla V_{\mathrm{ei}})_{\mathbf{q}}^{(\nu)}\left|m\mathbf{k}-\frac{\mathbf{q}}{2}\right\rangle_{\mathrm{uc}}.\tag{S62}
$$

We have defined $(\nabla V_{\mathrm{ei}})_{\mathbf{q}}^{(\nu)}=\sum_{\mathbf{R}\alpha}\sqrt{M_{0}/M_{\alpha}}e^{-i\mathbf{q}\cdot(\mathbf{r}-\mathbf{R})}\boldsymbol{\xi}_{\alpha}^{(\nu)}(\mathbf{q})\cdot\nabla V_{\mathrm{ei}}(\mathbf{r}-\mathbf{R}-\boldsymbol{\tau}_{\alpha})$.

Since we are interested in the low-energy effective e-ph coupling in the form of Eq. (2) in the main text, we adopt the finite-displacement approach in the first-principles calculations. We make the following approximation for phonons in $Cd_3As_2$: (i) We consider the long-wavelength limit $(\mathbf{q}=0)$, where the atomic displacements are

$$
\mathbf{u}_{\alpha}=\sqrt{\frac{M_{0}}{M_{\alpha}}}\boldsymbol{\xi}_{\alpha}^{(\nu)}l^{(\nu)}u_{0}^{(\nu)},\tag{S63}
$$

where only the zero-center contribution is kept and we only consider one phonon mode $\nu$. (ii) Since the tight-binding model used for $\text{Cd}_3\text{As}_2$ has only one $s$ and one $p$ orbital per site while the real lattice has 80 atoms per unit cell, we take the average of $|\mathbf{u}_\alpha|$ over the index $\alpha$:

$$
|\mathbf{u}|=\left|\frac{1}{N_{\alpha}} \sum_{\alpha} \mathbf{u}_{\alpha}\right|=\left|\frac{1}{N_{\alpha}} \sum_{\alpha} \sqrt{\frac{M_{0}}{M_{\alpha}}} \boldsymbol{\xi}_{\alpha}^{(\nu)} l^{(\nu)}\right| \approx\left|\frac{1}{N_{\alpha}} \sqrt{\frac{M_{0}}{\overline{M}}} l^{(\nu)} \sum_{\alpha} \boldsymbol{\xi}_{\alpha}^{(\nu)}\right| \tag{S64}
$$

where $\overline{M}$ is the average mass of the ions in the unit cell. For the $E_u$ mode we calculated, the amplitude $\sqrt{\frac{M_0}{\overline{M}}}l^{(\nu)}$ is set to be $1$ Å. The weighted average of the displacement magnitude is $|\mathbf{u}| \approx 0.0019$ Å. Then we can estimate the magnitude of the frame field $e_{\mu}^{A}$ from the deformed Dirac cone. The ratio of the Dirac cone slope between $x$ and $y$ axes is about $\beta|\mathbf{u}| / a \approx 1.211$. Thus we can make an estimate of the electron-phonon coupling parameter $\beta / a \approx 632$ Å$^{-1}$.