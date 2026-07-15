# Phase competition and photomagnetism in supramolecular assemblies based on octacyanomolybdates of square antiprism configuration

Shoji Yamamoto* and Jun Ohara

Department of Physics, Hokkaido University, Sapporo 060-0810, Japan

Received 2 June 2012, accepted 30 August 2012
Published online 1 November 2012

Keywords octacyanomolybdate, photomagnetism, angle resolved photoemission, group theory

* Corresponding author: e-mail yamamoto@phys.sci.hokudai.ac.jp

We construct a microscopic theory on the photomagnetism in the cyano-bridged bimetallic assemblies $\mathrm{Cu}_{2}[\mathrm{Mo}(\mathrm{CN})_{8}]\cdot x\mathrm{H}_{2}\mathrm{O}$. Going through a group-theoretical analysis on the ground-state properties, we simulate photoirradiation and the resultant magnetization dynamics with a time-dependent Hartree-Fock method.

It is not $c$-axis-polarized photons but those polarized in the $ab$ plane that induce a macroscopic magnetization. Absorption of the photon energy is double-stepped and the occurrence of a significant magnetization is simultaneous with the second stage.

© 2012 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

## 1 Introduction
Octacyanomolybdates were first synthesized by Chilesotti [1] at the beginning of the 20th century. Leipoldt *et al.* proposed an alternative efficient synthetic method [2], which is applicable to octacyanometalates [3] in general. The discovery of photomagnetism in Prussian blue analogues [4,5] has sparked renewed interest in cyano-based coordination networks and the chemical explorations of octacyanometalates have also made remarkable progress [6] in the past decade. Among others are the copper-molybdenum bimetallic assemblies $\mathrm{Cu}_{2}^{\mathrm{II}}[\mathrm{Mo}^{\mathrm{IV}}(\mathrm{CN})_{8}]\cdot x\mathrm{H}_{2}\mathrm{O}$, [7,8] which is remarkable for its phototunable magnetism [9,10]. The paramagnetic ground state is significantly magnetized by blue-laser irradiation, while it is demagnetized step by step via successive irradiation with red or near-infrared laser lights. The photoinduced magnetization is stable for hours up to 100 K or more and the photoconversion, both magnetization and demagnetization, is repeatable.

In spite of such intriguing observations, neither the photoexcitation mechanism nor the ground-state magnetism has been interpreted yet beyond a phenomenological understanding. In comparison with hexacyanometalates [11,12] octacyanometalates, have much less been studied from the physical point of view so far. An ocatacyanometalate ion adopts one of the three spacial configurations: square antiprism (SAPR-8), dodecahedron (DD-8), or bicapped trigonal prism (BTP-8) [6]. While the mixed-valent bimetallic compound $\mathrm{Cu}_{2}^{\mathrm{II}}[\mathrm{Mo}^{\mathrm{IV}}(\mathrm{CN})_{8}]\cdot8\mathrm{H}_{2}\mathrm{O}$ crystallizes in the $I4/m$ tetragonal space group with $\mathrm{C}_{4h}$ point symmetry, each constituent ion $[\mathrm{Mo}(\mathrm{CN})_{8}]^{4-}$ takes the SAPR-8 configuration with $\mathrm{D}_{4d}$ point symmetry. Its reversible magnetism originates in internal photochemical redox reactions between the copper and molybdenum sites. The supramolecular coordination network based on ocatacyanomolybdates of the SAPR-8 configuration gives unique hopping paths and they must play a major role in realizing the photoreversible itinerant ferromagnetism.

![](./images/813274124162957317_1.jpg)

© 2012 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

Table 1 Irreducible representations with an axial isotropy subgroup describing static density-wave states, where $\mathbf{C}_{2}=\{E, C_{2 z}\}$, $\mathbf{C}_{4}=\{E, C_{4 z}, C_{2 z}, C_{4 z}^{-1}\}$, $\mathbf{S}_{4}=\{E, C_{2 z}, I C_{4 z}, I C_{4 z}^{-1}\}$, $\mathbf{C}_{2 h}=\mathbf{C}_{2}+I \mathbf{C}_{2}$, $\mathbf{C}_{4 h}=\mathbf{C}_{4}+I \mathbf{C}_{4}$, $\mathbf{A}(e_{\lambda})=\{u(e_{\lambda}, \theta) ; 0 \leq \theta \leq 4 \pi\}$, and $\mathbf{M}(e_{\lambda})=\{E, t u_{2 \lambda}\}$ with $u_{2 \lambda}=u(e_{\lambda}, \pi)$.

| Irreducible representation | Axial isotropy subgroup | Descriptive abbreviation |
|-----------------------------|--------------------------|---------------------------|
| $\Gamma A_{g} \otimes \check{S}^{0} \otimes \check{T}^{0}$ | $\mathbf{C}_{4 h}$ LST | PM |
| $\Gamma B_{g} \otimes \check{S}^{0} \otimes \check{T}^{0}$ | $\mathbf{C}_{2 h}$ LST | Cu-CDW |
| $\Gamma A_{u} \otimes \check{S}^{0} \otimes \check{T}^{0}$ | $\mathbf{C}_{4}$ LST | Mo-CDW |
| $\Gamma B_{u} \otimes \check{S}^{0} \otimes \check{T}^{0}$ | $\mathbf{S}_{4}$ LST | BOW |
| $\Gamma A_{g} \otimes \check{S}^{1} \otimes \check{T}^{1}$ | $\mathbf{C}_{4 h} \mathbf{L} \mathbf{A}(e_{z}) \mathbf{M}(e_{y})$ | CuMo-(A)FM |
| $\Gamma B_{g} \otimes \check{S}^{1} \otimes \check{T}^{1}$ | $(E+C_{4 z} u_{2 x}) \mathbf{C}_{2 h} \mathbf{L} \mathbf{A}(e_{z}) \mathbf{M}(e_{y})$ | Cu-AFM |
| $\Gamma A_{u} \otimes \check{S}^{1} \otimes \check{T}^{1}$ | $(E+I u_{2 x}) \mathbf{C}_{4} \mathbf{L} \mathbf{A}(e_{z}) \mathbf{M}(e_{y})$ | Mo-AFM |
| $\Gamma B_{u} \otimes \check{S}^{1} \otimes \check{T}^{1}$ | $(E+C_{4 z} u_{2 x}) \mathbf{S}_{4} \mathbf{L} \mathbf{A}(e_{z}) \mathbf{M}(e_{y})$ | SBOW |

Thus motivated, we start our investigation with a group-theoretical analysis on the $I4/m$ cyano-bridged bimetallic assembly.

## 2 Symmetry properties and phase competition
Figure 1 depicts the crystalline structure of the dicopper octacyanomolybdate. We describe the supramolecular coordination network comprising divalent copper and tetravalent molybdenum ions in terms of a three-band extended Hubbard Hamiltonian of $2/3$ electron filling,

$$
\begin{aligned}
\mathcal{H}= & \sum_{M=\mathrm{Cu}, \mathrm{Mo}} \sum_{\boldsymbol{n}} \sum_{i=1}^{\mu_{M}} \sum_{\sigma= \pm}\left[\left(\varepsilon_{M}-\frac{\sigma}{2} g \mu_{\mathrm{B}} H\right) n_{M: \boldsymbol{n}(i), \sigma}\right. \\
& \left.+\frac{U_{M}}{2} n_{M: \boldsymbol{n}(i), \sigma} n_{M: \boldsymbol{n}(i),-\sigma}\right]+\sum_{<\boldsymbol{n}(i), \boldsymbol{m}(j)>}\left\{t_{\mathrm{CuMo}}\right. \\
& \left.\times \sum_{\sigma= \pm}\left[(-1)^{i+j+1} c_{\mathrm{Cu}: \boldsymbol{n}(i), \sigma}^{\dagger} c_{\mathrm{Mo}: \boldsymbol{m}(j), \sigma}+\text { H.c. }\right]\right. \\
& +J_{\mathrm{CuMo}} \sum_{\sigma, \tau} c_{\mathrm{Cu}: \boldsymbol{n}(i), \sigma}^{\dagger} c_{\mathrm{Mo}: \boldsymbol{m}(j), \sigma}^{\dagger} c_{\mathrm{Cu}: \boldsymbol{n}(i), \tau} c_{\mathrm{Mo}: \boldsymbol{m}(j), \sigma} \\
& +J_{\mathrm{CuMo}}^{\prime} \sum_{\sigma, \tau}\left[c_{\mathrm{Cu}: \boldsymbol{n}(i), \sigma}^{\dagger} c_{\mathrm{Cu}: \boldsymbol{n}(i), \tau}^{\dagger} c_{\mathrm{Mo}: \boldsymbol{m}(j), \tau} c_{\mathrm{Mo}: \boldsymbol{m}(j), \sigma}\right. \\
& \left.\left.+\text { H.c. }\right]+V_{\mathrm{CuMo}} n_{\mathrm{Cu}: \boldsymbol{n}(i)} n_{\mathrm{Mo}: \boldsymbol{m}(j)}\right\},
\end{aligned}
$$

with $\mu_{\mathrm{Cu}}=8$, $\mu_{\mathrm{Mo}}=4$, and $n_{M: \boldsymbol{n}(i)}=\sum_{\sigma} n_{M: \boldsymbol{n}(i), \sigma}=\sum_{\sigma} c_{M: \boldsymbol{n}(i), \sigma}^{\dagger} c_{M: \boldsymbol{n}(i), \sigma}$, where $c_{M: \boldsymbol{n}(i), \sigma}^{\dagger}$ creates an electron of spin $\sigma=\uparrow, \downarrow \equiv \pm$ in the $\mathrm{Cu} 3 d_{z x}$ ($M=\mathrm{Cu}$; $i=1,2,5,6$), $\mathrm{Cu} 3 d_{y z}$ ($M=\mathrm{Cu}$; $i=3,4,7,8$), or $\mathrm{Mo} 4 d_{z^{2}}$ ($M=\mathrm{Mo}$; $i=1,2,3,4$) orbitals labelled $i$ at unit cell $\boldsymbol{n}$. $\sum_{<\boldsymbol{n}(i), \boldsymbol{m}(j)>}$ means the sum all over neighbouring copper and molybdenum sites.

Unless the gauge symmetry is broken, the symmetry group of any lattice electron system can be written as $\mathbf{G}=\mathbf{P} \times \mathbf{S} \times \mathbf{T}$, where $\mathbf{P}$, $\mathbf{S}$, and $\mathbf{T}$ are the groups of space, spin

![](./images/813274124162957317_2.jpg)

Figure 1 (a) An overview and the projection onto the $ab$-plane of the dicopper octacyanomolybdate with explanatory notes for the present modelling. (b) Possible spin-density-wave (SDW) states: ferromagnetism/antiferromagnetism extending over the whole lattice (CuMo-FM/AFM) and antiferromagnetism within the copper/molybdenum sublattice (Cu/Mo-AFM).

![](./images/813274124162957317_3.jpg)

Figure 2 Ground-state phase diagrams as functions of the on-site Coulomb interactions $U_{\mathrm{Cu}}$ and $U_{\mathrm{Mo}}$ within the Hartree-Fock approximation, where the orbital energy difference $\varepsilon_{\mathrm{Cu}}-\varepsilon_{\mathrm{Mo}}$ and the intersite Coulomb interaction $V_{\mathrm{CuMo}}$ are fixed at $0.5 t_{\mathrm{CuMo}}$ and $0.8 t_{\mathrm{CuMo}}$, respectively, in common, while the exchange interaction $J_{\mathrm{CuMo}}$ and the pair-hopping energy $J_{\mathrm{CuMo}}^{\prime}$ are both set equal to $0.2 t_{\mathrm{CuMo}}$ (a) or $0.4 t_{\mathrm{CuMo}}$ (b). Phase transitions across a black line are of the first order, while those across a toned line are of the second order.

rotation, and time reversal, respectively. The space group is further decomposed into the translation and point groups as $\mathbf{L} \wedge \mathbf{D}$, which read, $\{\boldsymbol{l}=l_{a} \boldsymbol{a}+l_{b} \boldsymbol{b}+l_{c} \boldsymbol{c} ; l_{a}, l_{b}, l_{c} \in \mathbf{Z}\}$ and $\{E, C_{4 z}, C_{2 z}, C_{4 z}^{-1}, I, I C_{4 z}, I C_{2 z} \equiv \sigma_{h}, I C_{4 z}^{-1}\} \equiv \mathbf{C}_{4 h}$, respectively, with $\boldsymbol{a}=(e_{x}+e_{y}) / \sqrt{2}, \boldsymbol{b}=(-e_{x}+$ $e_{y}) / \sqrt{2}$, and $\boldsymbol{c}=e_{z}$, for the dicopper octacyanomolyb date tetragonal lattice. An irreducible representation of $\mathbf{G}$ over the real number field, which is referred to as $\check{G}$, consists of those of $\mathbf{P}, \mathbf{S}$, and $\mathbf{T}: \check{G}=\check{P} \otimes \check{S} \otimes \check{T}$. Once a wave vector $\boldsymbol{Q}$ is fixed, the relevant little group $\mathbf{D}(\boldsymbol{Q})$ is given. $\check{P}$ is therefore labeled as $\boldsymbol{Q} \check{D}(\boldsymbol{Q})$. Since any cell multiplied phase is of no interest under the present band filling, we consider the case of $\boldsymbol{Q}=\boldsymbol{0}$, which is labelled $\Gamma$ and whose little group is $\mathbf{C}_{4 h}$ itself. The relevant representations of $\mathbf{S}$ are given by $\check{S}^{0}(u(\boldsymbol{e}, \theta))=1$ (singlet) and $\check{S}^{1}(u(\boldsymbol{e}, \theta))=O(u(\boldsymbol{e}, \theta))$ (triplet), where $O(u(\boldsymbol{e}, \theta))$ is the $3 \times 3$ orthogonal matrix satisfying $u(\boldsymbol{e}, \theta) \boldsymbol{\sigma}^{\lambda} u^{\dagger}(\boldsymbol{e}, \theta)=$ $\sum_{\lambda^{\prime}=x, y, z}[O(u(\boldsymbol{e}, \theta))]_{\lambda \lambda^{\prime}} \boldsymbol{\sigma}^{\lambda^{\prime}}(\lambda=x, y, z)$. Those of $\mathbf{T}$ are given by $\check{T}^{0}(t)=1$ (symmetric) and $\check{T}^{1}(t)=-1$ (antisymmetric). Static density-wave solutions are derived from $\Gamma \check{D}(\boldsymbol{0}) \otimes \check{S}^{0} \otimes \check{T}^{0}$ and $\Gamma \check{D}(\boldsymbol{0}) \otimes \check{S}^{1} \otimes \check{T}^{1}$. We explain them in Table 1 and Fig. 1, where two-dimensional representations, generally available in a $\mathbf{C}_{4 h}$ Hamiltonian, are discarded, because they have no axial isotropy subgroup [13,14]. All the nonmagnetic phases but the paramagnetism, that is, charge-density-wave (CDW) and bond-order-wave (BOW = bond-centered CDW) states, are stabilized by predominant electron-lattice interactions [13,14] and are thus of no occurrence in strongly correlated magnetic materials. We further find varied magnetic phases. The spin-bond-order-wave (SBOW) state is characterized by unequal canonical ensemble averages of the bond-centered up- and down-spin densities, $\langle c_{\mathrm{Cu}: \boldsymbol{n}(i),+}^{\dagger} c_{\mathrm{Mo}: \boldsymbol{m}(j),+}\rangle \neq\langle c_{\mathrm{Cu}: \boldsymbol{n}(i),-}^{\dagger} c_{\mathrm{Mo}: \boldsymbol{m}(j),-}\rangle$. They are mathematically interesting [15] but of no occurrence under any realistic parametrization. The rest are spin-density-wave (SDW) states, including both ferromagnetism (FM) and antiferromagnetism (AFM), which are sketched in Fig. 1. CuMo-FM and CuMo-AFM belong to the same irreducible representation and are analytically indistinguishable. However, there may be a transition of the first order between them and we indeed find out such an example.

Having in mind that $\mathrm{Cu}_{2}^{\mathrm{II}}[\mathrm{Mo}^{\mathrm{IV}}(\mathrm{CN})_{8}] \cdot 8 \mathrm{H}_{2} \mathrm{O}$ stays paramagnetic (PM) without any long-ranged order down to $1.7 \mathrm{~K}$ [8], we have calculated ground-state phase diagrams, some of which are presented in Fig. 2. CuMo-FM is stabilized with the on-site Coulomb repulsions $U_{\mathrm{Cu}}$ and $U_{\mathrm{Mo}}$ increasing. The intersite Coulomb repulsion $V_{\mathrm{CuMo}}$ has the opposite effect, because it contributes toward driving all the electrons onto copper sites. The exchange interaction $J$ is most effective for CuMo-FM. We learn from the identity $\sum_{\sigma, \tau} c_{\mathrm{Cu}: \boldsymbol{n}(i), \sigma}^{\dagger} c_{\mathrm{Mo}: \boldsymbol{m}(j), \sigma}^{\dagger} c_{\mathrm{Cu}: \boldsymbol{n}(i), \tau} c_{\mathrm{Mo}: \boldsymbol{m}(j), \sigma}=$ $-2 S_{\mathrm{Cu}: \boldsymbol{n}(i), \sigma} \cdot S_{\mathrm{Mo}: \boldsymbol{m}(j), \tau}-n_{\mathrm{Cu}: \boldsymbol{n}(i), \sigma} n_{\mathrm{Mo}: \boldsymbol{m}(j), \tau} / 2$, where $S_{M: \boldsymbol{n}, i}^{\lambda}=\sum_{\sigma, \sigma^{\prime}} c_{M: \boldsymbol{n}(i), \sigma}^{\dagger} c_{M: \boldsymbol{n}(i), \sigma^{\prime}} \sigma_{\sigma \sigma^{\prime}}^{\lambda} / 2$, that positive $J$ induces on-site spin moments, suppressing the intersite repulsion $V$, and brings them into ferromagnetic arrangement. The pair-hopping correlation $J^{\prime}$ set positive indirectly supports CuMo-FM, destabilizing any other phase [16]. While CuMo-AFM, neighbouring to CuMo-FM, has no net magnetization under the present parametrizations, it may be ferrimagnetic with uncompensating sublattice magnetizations, for instance, under electron doping.

![](./images/813274124162957317_4.jpg)

Figure 3 Band structure of the PM state specified by $\times$ in Fig. 2. Occupied and vacant bands are distinguishably drawn by solid and dotted lines, respectively. $\varepsilon_{F}$ points to the Fermi level.

![](./images/813274124162957317_5.jpg)

Figure 4 Magnetization dynamics induced by the pulsed laser light $\boldsymbol{A}(t)=e^{-\gamma^{2}\left(t-t_{0}\right)^{2}} \boldsymbol{A} \cos \omega t$ with $A=\hbar v / e l, \hbar \omega=$ $3.8 t_{\text {CuMo }}, t_{0}=100 \hbar / t_{\text {CuMo }}$, and $\hbar \gamma=0.1 t_{\text {CuMo }}$ (a) or $\hbar \gamma=0.025 t_{\text {CuMo }}\left(\mathrm{a}^{\prime}\right)$, where $l$ is set equal to $a$ or $c$ according as $\boldsymbol{A}$ is parallel to $\boldsymbol{a}$ or $\boldsymbol{c}$. The vector potential [(a), (a')], absorbed photon energy [(b), (b')], and magnetization [(c), (c')] as functions of time, where $M_{\max }$ is the saturated magnetization.

![](./images/813274124162957317_6.jpg)

Figure 5 Instantaneous one-particle spectral functions corresponding to Figs. 4(a')-4(c') with $\boldsymbol{A} \parallel \boldsymbol{a}$.

3 Photomagnetism Now we consider photoexciting a PM ground state, which is fixed for $\times$ in Fig. 2(b) and whose band structure is shown in Fig. 3. There are flat bands just below the Fermi level and they are highly—six-fold at most—degenerate. The flat bands survive into a FM state but turn partially filled. The experimental observations [10,9] read as photoconversions of a gapped paramagnetism into an itinerant ferromagnetism. The photoinduced magnetization is hardly detectable at zero magnetic field, while it rapidly increases just as an external field is applied [7]. With this in mind, we apply to the system a moderate field, $g\mu_{\text{B}}H = 0.0002t_{\text{CuMo}}$. Now the spin degeneracy is lifted and higher-lying down-spin electrons may selectively be excited into conduction bands. We describe such photoexcitations by multiplying the hopping term $c_{\text{Cu}:\boldsymbol{n}(i),-}^{\dagger}c_{\text{Mo}:\boldsymbol{m}(j),-}$ by the Peierls phase factor $\text{e}^{\text{i}(e/\hbar v)\boldsymbol{A}(t)\cdot[\boldsymbol{n}(i)-\boldsymbol{m}(j)]}$, where $e$ and $v$ are the elementary charge and the light velocity, respectively, and any spatial variation of the vector potential is negligible for visible lights. We set the photon energy $\hbar\omega$ equal to the gap between the highest occupied (HO) and lowest unoccupied (LU) molecular orbitals (MOs), which measures $3.8t_{\text{CuMo}}$. Another key ingredient of the photomagnetization is a spin-mixing interaction. In an attempt at breaking the conservation law for the total magnetization, we introduce Dzyaloshinsky-Moriya interactions,

$$
\begin{aligned}
\mathcal{H}_{\text{DM}} &= \sum_{\boldsymbol{n}} \sum_{l=1}^{4} \sum_{\rho=0}^{1} \sum_{\sigma,\sigma'=0}^{1} (-1)^{\rho+\sigma} D_{l+4\rho}^{(\sigma'\sigma)} \\
&\cdot\left[\boldsymbol{S}_{\text{Mo}:\boldsymbol{n}+\boldsymbol{\delta}(l,\rho,\sigma,\sigma'),1+3\sigma'+(-1)^{\sigma'}\rho} \times \boldsymbol{S}_{\text{Cu}:\boldsymbol{n},2l-\sigma}\right], \quad (2)
\end{aligned}
$$

where $\boldsymbol{\delta}(l,\rho,\sigma,\sigma') = \sigma'\text{Re}[f(l)]\boldsymbol{a} + \sigma'\text{Im}[f(l)]\boldsymbol{b} + \rho\boldsymbol{c}$ with $f(l) = e^{\text{i}\pi/4}[1 + e^{\text{i}\pi(1-l)/2}]/\sqrt{2}$. The DM vectors should be compatible with the crystalline structure as $\boldsymbol{D}_{i}^{(\sigma'\sigma)} = g_{i} \cdot \boldsymbol{D}_{1}^{(\sigma'\sigma)}$ with $g_{i}(\in \boldsymbol{C}_{4h}) = C_{4z}^{-1}, C_{2z}, C_{4z}, \sigma_{h}, IC_{4z}, I, IC_{4z}^{-1}$ for $i = 2$ to $8$, respectively. We lay them down in the $ab$ plane with $\boldsymbol{D}_{1}^{(\sigma'\sigma)} \parallel \boldsymbol{a}$ and set their magnitude equal to $0.05t_{\text{CuMo}}$. In order to visualize photoinduced electronic excitations and the following magnetic relaxation, we solve the time-dependent Schrödinger equation

$$
\text{i}\hbar\dot{\Psi}(t) = \mathcal{H}(t)\Psi(t), \tag{3}
$$

within the Hartree-Fock scheme [17], where the instantaneous Hamiltonian $\mathcal{H}(t)$ ($t \geq 0$) consists of Eq. (1) and Eq. (2) with the Peierls phase factor switched on, while the path-integrated wave-function array $\Psi(t)$ is a square matrix of degree $4N$ with $N$ being the number of unit cells and we define $\Psi(0)$ as the complete set of wave functions for the "static" Hamiltonian (1), $\{\Psi_{\boldsymbol{k}(\nu)}(0); \boldsymbol{k}(\nu) =$

$1,\cdots,24N\}$, which are specified with momentum $\boldsymbol{k}$ and band label $\nu$. Discretizing the time variable as $t_m = m\Delta t$ $(m = 0,1,2,\cdots)$ with an interval much smaller than the electronic time scale $\hbar/t_{\text{CuMo}}$, we integrate Eq. (3) step by step:

$$
\Psi\left(t_{m+1}\right)=\exp \left[-\frac{i \mathcal{H}\left(t_{m}\right)}{\hbar} \Delta t\right] \Psi\left(t_{m}\right). \tag{4}
$$

Once we start the time integration $(m>0), \Psi(t_m)$ deviates from the eigenvectors of $\mathcal{H}(t_m)$ in general. The amplitude of the alternate DM vectors is decisive of the time scale of magnetic relaxation. We are never able to numerically reproduce actual observations of order minutes or longer [7,10] exactly as they are. We thus adopt DM interactions stronger than actual and "accelerate" the magnetization dynamics.

We try photoirradiations for two different periods of time and show the resultant magnetization dynamics in Fig. 4. Photons polarized in the $ab$ plane can induce a macroscopic magnetization, whereas $c$-axis polarized photons are much less contributive. Both irradiation time and strength, which are described by $\gamma$ and $A$, respectively, are decisive of the increase of the electronic energy, $\Delta E=\langle\Phi(t)|\mathcal{H}(t)| \Phi(t)\rangle-\langle\Phi(0)|\mathcal{H}| \Phi(0)\rangle$ with $|\Phi(t)\rangle=\prod_{\boldsymbol{k}(\nu)=1}^{16 N} \otimes\left|\Psi_{\boldsymbol{k}(\nu)}(t)\right\rangle$. There is a certain excitation-density threshold for the system being macroscopically magnetized. $\Delta E$ in the case of $\boldsymbol{A} \| a$ reads as a double-stepped function of time. The occurrence of a significant magnetization looks simultaneous with the second step of $\Delta E(t)$.

4 Discussion In order to clarify why and how the electronic excitations are double stepped, we calculate oneparticle spectral functions,

$$
\begin{aligned}
G_{\mathrm{p} / \mathrm{h}}(t ; \boldsymbol{k}, \omega)=\sum_{\boldsymbol{k}(\nu)=1}^{24 N} \delta\left(\hbar \omega-\varepsilon_{\boldsymbol{k}(\nu)}\right)\left\langle\Phi(t)\left|n_{\boldsymbol{k}(\nu)}^{(p / h)}\right| \Phi(t)\right\rangle,
\end{aligned}
\tag{5}
$$

with $n_{\boldsymbol{k}(\nu)}^{(p)}=c_{\boldsymbol{k}(\nu)}^{\dagger} c_{\boldsymbol{k}(\nu)}$ and $n_{\boldsymbol{k}(\nu)}^{(h)}=c_{\boldsymbol{k}(\nu)} c_{\boldsymbol{k}(\nu)}^{\dagger}$, where $c_{\boldsymbol{k}(\nu)}^{\dagger}$ creates an electron in the eigenstate of energy $\varepsilon_{\boldsymbol{k}(\nu)}$ for the instantaneous Hamiltonian $\mathcal{H}(t)$ and we broaden the delta function into its Lorentzian form. Figure 5 visualizes Eq. (5) in the case of irradiating the PM state $[\times$ in Fig. 2(b)] with the pulsed laser light [Fig. 4(a')] polarized parallel to the crystalline axis $a$, which correspond to the solid lines in Figs. 4(b') and 4(c'), where the sum $G_{\mathrm{p}}(t ; \boldsymbol{k}, \omega)+G_{\mathrm{h}}(t ; \boldsymbol{k}, \omega) \equiv G(t ; \boldsymbol{k}, \omega)$ reads "momentum-resolved" density of states and demonstrates a time evolution of Fig. 3. With increasing time, the degeneracy between up and down spins is so lifted as to induce a net magnetization. The double-stepped absorption of photons in Fig. 4(b') is well understandable through the careful observation of $G_{\mathrm{h}}(t ; \boldsymbol{k}, \omega)$. Photoirradiation first creates holes around point $Z$ on the top of dispersive bands (cf. Fig. 3) and then erodes the flat bands having a macroscopic number of electrons. It is the electrons lying in the constituent HOMOs of flat bands that induce a macroscopic magnetization. That is why the system is not globally magnetized until it absorbs so many photons as to sweep away the irrelevant electrons degenerating into the flat-band-forming electrons. The HOMO-LUMO interband gap gets smaller with increasing number of photons being absorbed, which sounds interesting in the context of demagnetization. Irradiation of $\mathrm{Cu}_{2}^{\mathrm{II}}\left[\mathrm{Mo}^{\mathrm{IV}}(\mathrm{CN})_{8}\right] \cdot 8 \mathrm{H}_{2} \mathrm{O}$ with a laser light of $473 \mathrm{~nm}$ drives its magnetization to increase. Subsequent irradiation with another laser light of $658 \mathrm{~nm}$ conversely reduces the produced magnetization. When the sample is further irradiated with 785-nm and 840-nm laser lights successively, the magnetization gets smaller and smaller. These observations agree with the decreasing HOMO-LUMO gap with photomagnetization. Our theory is robust and can readily be extended to the photoreversible phenomena. We hope the present calculations will stimulate photomagnetic measurements on a single-crystalline sample.

## References

[1] A. Chilesotti, Gazz. Chim. Ital. 34, 497 (1904).
[2] J. G. Leipoldt, L. D. C. Bok, and P. J. Cilliers, Z. Anorg. Allg. Chem. 409, 343 (1974).
[3] J. G. Leipoldt, L. D. C. Bok, and P. J. Cilliers, Z. Anorg. Allg. Chem. 407, 350 (1974).
[4] M. Verdaguer, Science 272, 698 (1996).
[5] O. Sato, T. Iyoda, A. Fujishima, and K. Hashimoto, Science 272, 704 (1996).
[6] P. Przychodzeń, T. Korzeniak, R. Podgajny, and B. Sieklucka, Coord. Chem. Rev. 250, 2234 (2006).
[7] S. Ohkoshi, N. Machida, Z. J. Zhong, and K. Hashimoto, Synth. Met. 122, 523 (2001).
[8] S. Ohkoshi, N. Machida, Y. Abe, Z. J. Zhong, and K. Hashimoto, Chem. Lett. 312 (2001).
[9] X.-D. Ma, T. Yokoyama, T. Hozumi, K. Hashimoto, and S. Ohkoshi, Phys. Rev. B 72, 094107 (2005).
[10] S. Ohkoshi, H. Tokoro, T. Hozumi, Y. Zhang, K. Hashimoto, C. Mathonière, I. Bord, G. Rombaut, M. Verelst, C. Cartier dit Moulin, and F. Villain, J. Am. Chem. Soc. 128, 270 (2006).
[11] M. Verdaguer, A. Bleuzen, V. Marvaud, J. Vaissermann, M. Seuleiman, C. Desplansches, A. Seuiller, C. Train, R. Garde, G. Gelly, C. Lomenech, I. Rosenman, P. Veillet, C. Cartier, and F. Villain, Coord. Chem. Rev. 190-192, 1023 (1999).
[12] H. Tokoro and S. Ohkoshi, Dalton Trans. 40, 6825 (2011).
[13] J. Ohara and S. Yamamoto, Europhys. Lett. 87, 17006 (2009).
[14] S. Yamamoto, J. Ohara, and M. Ozaki, J. Phys. Soc. Jpn. 79, 044709 (2010).
[15] S. Yamamoto and M. Ozaki, Solid State Commun. 83, 335 (1992).
[16] J. E. Hirsch, Phys. Rev. B 43, 705 (1991).
[17] S. Yamamoto, J. Phys. Soc. Jpn. 80, 084713 (2011).