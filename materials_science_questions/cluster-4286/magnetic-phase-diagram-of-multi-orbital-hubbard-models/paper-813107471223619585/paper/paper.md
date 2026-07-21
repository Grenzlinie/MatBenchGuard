![](./images/813107471223619585_1.jpg)

PAPER • OPEN ACCESS

# Charge orders in organic charge-transfer salts

To cite this article: Ryui Kaneko et al 2017 New J. Phys. 19 103033

View the article online for updates and enhancements.

## Related content

- [Quantum frustration in organic Mott insulators](https://iopscience.iop.org/article/10.1088/1367-2630/16/6/065004)
B J Powell and Ross H McKenzie

- [Quantum criticality in organic conductors? Fermi liquid versus non-Fermi-liquid behaviour](https://iopscience.iop.org/article/10.1088/1367-2630/15/12/125014)
Martin Dressel

- [Electronic ferroelectricity in molecular organic crystals](https://iopscience.iop.org/article/10.1088/1367-2630/15/5/055004)
Sumio Ishihara

This content was downloaded from IP address 80.82.77.83 on 16/01/2018 at 03:01

# New Journal of Physics
The open access journal at the forefront of physics

**PAPER**

## Charge orders in organic charge-transfer salts

Ryuikaneko1.3, Luca F Tocchio2.4, Roser Valentil and Federico Becca2

1 Institute for Theoretical Physics, Goethe University Frankfurt, Max-von-Laue-Straße 1, D-60438 Frankfurt a.M., Germany
2 Democritos National Simulation Center, Istituto Officina dei Materiali del CNR, and SISSA-International School for Advanced Studies, Via Bonomea 265, I-34136 Trieste, Italy
3 Present address: Institute for Solid State Physics, University of Tokyo, 5-1-5 Kashiwanoha, Kashiwa, Chiba 277-8581, Japan.
4 Present address: Institute for Condensed Matter Physics and Complex Systems, DISAT, Politecnico di Torino, I-10129, Italy.

E-mail: rkaneko@issp.u-tokyo.ac.jp

Keywords: strongly correlated electronic systems, organic charge-transfer salts, multiferroics, charge order, variational Monte Carlo

### Abstract
Motivated by recent experimental suggestions of charge-order-driven ferroelectricity in organic charge-transfer salts, such as $\kappa$-(BEDT-TTF)$_2$Cu[N(CN)$_2$]Cl, we investigate magnetic and charge-ordered phases that emerge in an extended two-orbital Hubbard model on the anisotropic triangular lattice at $3/4$ filling. This model takes into account the presence of two organic BEDT-TTF molecules, which form a dimer on each site of the lattice, and includes short-range intramolecular and intermolecular interactions and hoppings. By using variational wave functions and quantum Monte Carlo techniques, we find two polar states with charge disproportionation inside the dimer, hinting to ferroelectricity. These charge-ordered insulating phases are stabilized in the strongly correlated limit and their actual charge pattern is determined by the relative strength of intradimer to interdimer couplings. Our results suggest that ferroelectricity is not driven by magnetism, since these polar phases can be stabilized also without antiferromagnetic order and provide a possible microscopic explanation of the experimental observations. In addition, a conventional dimer-Mott state (with uniform density and antiferromagnetic order) and a nonpolar charge-ordered state (with charge-rich and charge-poor dimers forming a checkerboard pattern) can be stabilized in the strong-coupling regime. Finally, when electron–electron interactions are weak, metallic states appear, with either uniform charge distribution or a peculiar 12-site periodicity that generates honeycomb-like charge order.

## 1. Introduction
Orbital, charge, and spin degrees of freedom are intertwined in correlated electron systems and the search for unconventional quantum phases emerging from the interplay of these degrees of freedom is a very active field of research in condensed-matter physics. In particular, multiferroicity [1], where magnetism and ferroelectricity coexist, has received a lot of attention in recent years. Conventionally, one can divide multiferroics into two groups: In type-I multiferroics, ferroelectricity and magnetism have different origins [2], while in type-II multiferroics, ferroelectricity occurs only in the magnetically ordered state, where, for example, it is induced by helical magnetic order in geometrically frustrated antiferromagnets [3–5]. Recently, charge-order-driven ferroelectricity was proposed in organic charge transfer salts [6], such as $\kappa$-(ET)$_2$Cu[N(CN)$_2$]Cl [7] and $\alpha$-(ET)$_2$I$_3$ [8–10], where ET stands for BEDT-TTF [bis(ethylenedithio)-tetrathiafulvalene]. In the former one, ferroelectric and antiferromagnetic order appear simultaneously and the emergence of charge order is still under debate [11–13]; instead, the latter one is nonmagnetic and ferroelectricity is observed in the presence of pronounced charge order. These observations have opened a debate about the nature and interplay of charge order, ferroelectricity and magnetism in these materials, which will be at the focus of this study.

© 2017 IOP Publishing Ltd and Deutsche Physikalische Gesellschaft

The building blocks of the $\kappa$-(ET)$_2$X family (where X indicates a monovalent anion) are strongly-coupled dimers of ET molecules forming a triangular lattice. These materials have been widely studied within the half-filled single-band Hubbard model on the anisotropic triangular lattice, where only a single orbital per dimer is retained [14]. Indeed, because of the strong hybridization between ET molecules belonging to the same dimer, the gap between the bonding and anti-bonding orbitals is large; the former one is fully occupied, while the latter one is half filled, thus justifying a single-band picture. However, this coarse-grained approach cannot explain the possible emergence of ferroelectricity (or multiferroicity) in these materials, which has been suggested to arise from a charge disproportionation *within* each dimer. In this sense, the minimal model that could capture these features must include two molecular orbitals on each dimer and 3/4 filling.

In the last few decades there have been several attempts to obtain accurate values of the parameters defining microscopic models that would capture the low-energy properties of charge-transfer salts. The hopping integrals between the different molecular orbitals are found to significantly affect the nature of the ground states, as already reported in the first Hartree–Fock studies of correlated models for charge-transfer salts [15–17]. These considerations motivated a revision of the first estimates of the hopping parameters, that were based on the extended Hückel method [18], by means of density-functional calculations. Here, consistent results for the hopping parameters of the $\kappa$-(ET)$_2$X family have been reported by three independent calculations [19–21], while slightly different values have been recently proposed [22]. Besides the role of hopping parameters, the importance of Coulomb interactions between different molecules in organic systems has been intensively discussed within *ab-initio* calculations [19, 23–25]. More recently, the analysis of various (low-energy) multiorbital models also points to the key role of intermolecular Coulomb interactions in order to describe complex phases relevant for charge-transfer salts. In particular, possible stripe and non-stripe charge orderings [26, 27] and the mutual exclusion of ferroelectricity and magnetism [28] have been discussed for various models with intermolecular interactions. In addition, the existence of a dipolar spin-liquid phase has been suggested [29, 30] (possibly also explaining the dielectric anomaly in $\kappa$-(ET)$_2$Cu$_2$(CN)$_3$ [31]). Furthermore, the two-orbital Hubbard model has been claimed to be relevant for the description of superconductivity in charge-transfer salts [32–35], including its proximity to charge-ordered phases [36, 37]. In addition, spin and charge fluctuations near the metal–insulator transition in multiorbital models have been analyzed [38].

In this paper, we concentrate on the question of what kind of charge orderings are driven by competing Coulomb interactions and which is their relation to ferroelectricity and magnetism. By using variational Monte Carlo methods, we investigate the phase diagram of an extended two-orbital Hubbard model on the triangular lattice at 3/4 filling. Our results show that there exist two polar charge-ordered insulating phases, where charge disproportionation occurs within the dimer, and one nonpolar charge-ordered phase, with charge disproportionation between different dimers. All these phases are present also in the absence of magnetic order, indicating that they are not driven by magnetism. When magnetism is also included in the variational wave functions, we find that it coexists with charge order. These results could explain the observed behavior in $\kappa$-(ET)$_2$Cu[N(CN)$_2$]Cl. On the contrary, magnetism is crucial to stabilize the uniform dimer-Mott insulator (DMI), which appears in a narrow region between the two polar phases. In this respect, it has been experimentally suggested that a transition between the DMI and charge-ordered states is a common feature among organic systems [39]. Finally, when intramolecular and intermolecular Coulomb interactions are small and similar in magnitude, a metallic phase emerges, featuring charge order in the form of an effective honeycomb-lattice superstructure.

The paper is organized as follows: in section 2, we present the extended two-band Hubbard model for the organic charge transfer salts and the variational Monte Carlo method to study the phase diagram at zero temperature. In section 3, we show the numerical results and discuss the nature of charge-ordered phases. Finally, in section 4, we draw our conclusions.

## 2. Model and methods

### 2.1. The extended two-orbital Hubbard model
In the following, we will consider a model in which every site (i.e. dimer) accommodates two orbitals (hereinafter referred to as $c$ and $f$), one for each ET molecule. The original lattice is triangular, with hopping and interaction terms depicted in figure 1(a). An equivalent description is given by considering a two-orbital model on the square lattice, see figure 1(b). Here, we can define a partition in two sub-lattices $\mathcal{A}$ and $\mathcal{B}$, where the ET molecules form horizontal and vertical dimers, respectively. The full Hamiltonian, in this latter description, is given by:

$$
\mathcal{H} = \mathcal{H}_t + \mathcal{H}_V + \mathcal{H}_U, \tag{1}
$$

![](./images/813107471223619585_2.jpg)

Figure 1. (a) Dimer alignment in $\kappa$-(ET)$_2$X charge-transfer salts. (b) Equivalent square-lattice structure used in the calculations.

where

$$
\begin{aligned}
\mathcal{H}_{t} & =t_{b 1} \sum_{i, \sigma} c_{i, \sigma}^{\dagger} f_{i, \sigma}+t_{b 2} \sum_{i, \sigma} c_{i, \sigma}^{\dagger} f_{i+x+y, \sigma} \\
& +t_{q} \sum_{i, \sigma}\left(c_{i, \sigma}^{\dagger} f_{i+x, \sigma}+c_{i, \sigma}^{\dagger} f_{i+y, \sigma}\right) \\
& +t_{p} \sum_{i \in \mathcal{A}, \sigma}\left(c_{i, \sigma}^{\dagger} c_{i+x, \sigma}+c_{i, \sigma}^{\dagger} c_{i-y, \sigma}+f_{i, \sigma}^{\dagger} f_{i-x, \sigma}+f_{i, \sigma}^{\dagger} f_{i+y, \sigma}\right)+\text { h.c. },
\end{aligned}
\tag{2}
$$

$$
\begin{aligned}
\mathcal{H}_{V} & =V_{b 1} \sum_{i} n_{i}^{c} n_{i}^{f}+V_{b 2} \sum_{i} n_{i}^{c} n_{i+x+y}^{f} \\
& +V_{q} \sum_{i}\left(n_{i}^{c} n_{i+x}^{f}+n_{i}^{c} n_{i+y}^{f}\right) \\
& +V_{p} \sum_{i \in \mathcal{A}}\left(n_{i}^{c} n_{i+x}^{c}+n_{i}^{c} n_{i-y}^{c}+n_{i}^{f} n_{i-x}^{f}+n_{i}^{f} n_{i+y}^{f}\right),
\end{aligned}
\tag{3}
$$

$$
\mathcal{H}_{U}=U \sum_{i}\left(n_{i, \uparrow}^{c} n_{i, \downarrow}^{c}+n_{i, \uparrow}^{f} n_{i, \downarrow}^{f}\right).
\tag{4}
$$

Here, $c_{i, \sigma}^{\dagger}$ ($f_{i, \sigma}^{\dagger}$) creates an electron with spin $\sigma$ on the $c$($f$) molecular orbital at site $i$; $n_{i}^{c}=\sum_{\sigma} n_{i, \sigma}^{c}$ ($n_{i}^{f}=\sum_{\sigma} n_{i, \sigma}^{f}$) are the density operator for $c$($f$) electrons at site $i$. Hopping and interaction terms can be divided into those that connect $c$ and $f$ orbitals and those that connect orbitals of the same kind, see figure 1(b). Belonging to the former class, there are terms connecting orbitals within the same dimer ($b_1$-type), along $x$ and $y$ nearest-neighbor sites ($q$-type), and along the $x=y$ diagonal ($b_2$-type); instead, $p$-type terms connect orbitals at nearest-neighbor sites and belong to the latter class. Accordingly, the noninteracting Hamiltonian $\mathcal{H}_{t}$ contains four hopping parameters, i.e. $t_{b 1}, t_{b 2}, t_{q}$ and $t_{p}$. Similarly, the interacting Hamiltonian $\mathcal{H}_{V}$ contains four intermolecular Coulomb interactions, i.e. $V_{b 1}, V_{b 2}, V_{q}$, and $V_{p}$. Note that the translational symmetry and the consequent partition between $\mathcal{A}$ and $\mathcal{B}$ sub-lattices is only due to the presence of $p$-type terms. Finally, $\mathcal{H}_{U}$ describes the Hubbard-$U$ interaction on each molecule. Our calculations are performed on finite clusters of size $N_{s}=L^{2}$ (where on each site there are two molecules, i.e. orbitals), with periodic–antiperiodic boundary conditions on both directions. The filling factor is fixed to be $3/4$.

As discussed in [35], this two-orbital model reduces to the single-band Hubbard model (at half filling), when the intradimer hopping is very large (i.e. $t_{b 1} \gg t_{b 2}, t_{p}, t_{q}$). Furthermore, at $t_{b 2}=0$ and $t_{p}=0$ (or $t_{q}=0$) the Hamiltonian reduces to the recently investigated Hubbard model on the honeycomb lattice with anisotropic terms [40].

In this work, we consider the following hopping parameters (in units of $t_{b1}$):

$$
t_{b 1}=1, \quad t_{b 2}=0.359, \quad t_{p}=0.539, \quad t_{q}=0.221,
\tag{5}
$$

which are based on the results obtained by density functional theory calculations on $\kappa$-(ET)$_2$Cu[N(CN)$_2$]Cl [35, 41]. The noninteracting band structure is reported in figure 2. As far as the interaction terms are concerned, for realistic systems, one expects $U$ to be the largest Coulomb repulsion term and $V_{b1}$ to be the second largest one, while $V_{b2}$ should be comparable to $V_{p}$ and $V_{q}$.

![](./images/813107471223619585_3.jpg)

![](./images/813107471223619585_4.jpg)

### 2.2. The atomic limit
We first discuss the possible ground states in the atomic limit, i.e. for $t_{b1}=t_{b2}=t_{p}=t_{q}=0$ at 3/4 filling. If the only finite interaction is the intramolecular Hubbard-$U$ term, the ground state is highly degenerate, with all possible charge patterns having $N_s$ doubly-occupied molecules. A further degeneracy arises from the remaining $N_s$ molecules being singly-occupied, where any spin configuration gives the same energy. The charge degeneracy can be lifted by including the intermolecular interactions $V_{b1}$, $V_{b2}$, $V_p$, and $V_q$. We concentrate here on three particular relevant cases that show regular patterns of charge order (see figure 3): two of them are polar charge-order insulators (hereinafter denoted as PCOI and PCOI $'$), since there is a charge disproportionation inside each dimer, and one is a nonpolar charge-order insulator (denoted as NPCOI), since the two molecules of the same dimer have the same amount of charge. Their energies per site (i.e. per dimer) can be easily evaluated in the atomic limit:

$$
E_{\mathrm{polar}}=E+V_{q}, \tag{6}
$$

$$
E_{\mathrm{polar}'}=E+V_{p}, \tag{7}
$$

$$
E_{\mathrm{nonpolar}}=E+\frac{1}{2}\left(V_{b1}+V_{b2}\right), \tag{8}
$$

where we defined:

$$
E=U+2 V_{b1}+4 V_{p}+4 V_{q}+2 V_{b2}. \tag{9}
$$

The phase diagram in the $V_p$-$V_q$ plane is shown in figure 3. Here, $V_{b1}$ and $V_{b2}$ only modify the phase boundaries between the polar and nonpolar charge-ordered phases. The NPCOI appears when both $V_p$ and $V_q$ dominate

over $V_{b 1}$ and $V_{b 2}$. Otherwise, the two polar states are stable and the competition between $V_{p}$ and $V_{q}$ determines the detailed charge pattern. All three phases are degenerate for $V_{p}=V_{q}=\left(V_{b 1}+V_{b 2}\right) / 2$.

### 2.3. Variational wave functions
Our numerical results are obtained by means of the variational Monte Carlo method, that is based on the definition of suitable wave functions that approximate the ground-state properties beyond perturbative approaches. We consider Jastrow-Slater wave functions [42-45], which are described as:

$$
|\Psi\rangle=\mathcal{J}|\Phi\rangle. \tag{10}
$$

Here, $\mathcal{J}$ is a long-range density-density Jastrow factor given by:

$$
\mathcal{J}=\exp \left(-\frac{1}{2} \sum_{i, j, \alpha, \beta} v_{i j}^{\alpha \beta} n_{i}^{\alpha} n_{j}^{\beta}\right), \tag{11}
$$

where $n_{i}^{\alpha}$ is the electronic density at site $i$ and orbital $\alpha=c, f$, while $v_{i j}^{\alpha \beta}$ are translational invariant variational parameters, that are optimized by only imposing translational and inversion symmetry in the square lattice defined by $\boldsymbol{R}_{i}=\left(x_{i}, y_{i}\right)$. $|\Phi\rangle$ is a noninteracting fermionic state that is defined as the ground state of an auxiliary Hamiltonian with site-dependent chemical potentials and magnetic order parameters. Such a choice of an auxiliary Hamiltonian allows us to describe both charge and spin orders induced by the intermolecular Coulomb interactions [40, 46, 47]. In particular, for the insulating states, we consider:

$$
\mathcal{H}_{\text {ins }}=\mathcal{H}_{t}+\mathcal{H}_{\mathrm{COI}}+\mathcal{H}_{\mathrm{AF}}, \tag{12}
$$

where $\mathcal{H}_{t}$ is the kinetic part of equation (2) and

$$
\mathcal{H}_{\mathrm{COI}}=\sum_{i} \mathrm{e}^{\mathrm{i} \boldsymbol{Q} \cdot \boldsymbol{R}_{i}}\left(\mu^{c} n_{i}^{c}+\mu^{f} n_{i}^{f}\right), \tag{13}
$$

$$
\mathcal{H}_{\mathrm{AF}}=\sum_{i}\left[m_{i}^{c}\left(c_{i, \uparrow}^{\dagger} c_{i, \downarrow}+c_{i, \downarrow}^{\dagger} c_{i, \uparrow}\right)+m_{i}^{f}\left(f_{i, \uparrow}^{\dagger} f_{i, \downarrow}+f_{i, \downarrow}^{\dagger} f_{i, \uparrow}\right)\right]. \tag{14}
$$

Here, $\boldsymbol{Q}=(\pi, \pi)$ describes the NPCOI (with $\mu^{c}=\mu^{f}$ ) and the PCOI (with $\mu^{c}=-\mu^{f}$ ) phases of figure 3, while $\boldsymbol{Q}=(0,0)$ (with $\mu^{c}=-\mu^{f}$ ) gives the PCOI' phase of figure 3. We optimize the variational magnetic parameters at charge-rich and charge-poor molecular orbitals independently, according to the condition:

$$
m_{i}^{\alpha}= \begin{cases}m_{1}^{\alpha} & \text { if } \mathrm{e}^{\mathrm{i} \boldsymbol{Q} \cdot \boldsymbol{R}_{i}} \mu^{\alpha}<0, \\ m_{2}^{\alpha} & \text { if } \mathrm{e}^{\mathrm{i} \boldsymbol{Q} \cdot \boldsymbol{R}_{i}} \mu^{\alpha}>0,\end{cases} \tag{15}
$$

which implies that $m_{1}^{\alpha}$ and $m_{2}^{\alpha}$ are associated to the magnetization of the charge-rich and charge-poor molecular orbitals on site $i$, respectively. In general, incommensurate magnetic order may coexist with commensurate charge order; however, this is beyond the scope of the present paper, and we restrict ourselves to commensurate (and collinear) magnetic order. Notice that, within our variational description based upon an auxiliary Hamiltonian, it is particularly easy to consider nonmagnetic states, which can be described by taking $m_{i}^{c}=m_{i}^{f}=0$ in equation (14).

In order to describe metallic states, we consider the following auxiliary Hamiltonian:

$$
\mathcal{H}_{\text {met }}=\mathcal{H}_{t}+\mathcal{H}_{\text {COM }}, \tag{16}
$$

where

$$
\mathcal{H}_{\mathrm{COM}}=\sum_{i}\left[\mu_{R(i)}^{c} n_{i}^{c}+\mu_{R(i)}^{f} n_{i}^{f}\right] ; \tag{17}
$$

here, the sublattice index $R(i)$ at position $\boldsymbol{R}_{i}$ is defined as:

$$
R(i)=\bmod \left(x_{i}-y_{i}, 6\right), \tag{18}
$$

which allows a 12-sublattice charge ordering, since there are two orbitals on each site. We neglect in the calculation the possible presence of magnetic order in the metallic states.

In order to exclude the presence of further ordered phases in the explored regions of the phase diagram, we have also employed unbiased wave functions, where different charge orderings can spontaneously emerge. In particular, we constructed a noninteracting wave function $|\Phi\rangle$ as the ground state of the tight-binding Hamiltonian with site-dependent chemical potentials $\mu_{i}^{c}$ and $\mu_{i}^{f}$ :

$$
\mathcal{H}_{\text {full }}=\mathcal{H}_{t}+\sum_{i}\left(\mu_{i}^{c} n_{i}^{c}+\mu_{i}^{f} n_{i}^{f}\right), \tag{19}
$$

where the chemical potentials are variational parameters independently optimized for each site $i$ (several initial configurations of $\mu_{i}^{c}$ and $\mu_{i}^{f}$ have been chosen, in order to assess the possibility to remain stuck in local minima). Since the number of parameters to be optimized grows as $2 N_{s}$, we considered this approach only for $N_{s}=36$.

![](./images/813107471223619585_5.jpg)

Figure 4. Schematic phase diagram of model equation (1) for large $U/t_{b1}$. In addition to the phases of the atomic limit (see figure 3), the uniform dimer-Mott insulator (DMI) appears. Here, the points where we performed the variational calculations have been marked by green up-triangles (PCOI '), blue down-triangles (NPCOI), red squares (PCOI), and violet diamonds (DMI). Notice that finite nonzero hopping terms generate effective super-exchange couplings that stabilize antiferromagnetic order.

this case, we have observed that the selected charge orderings are consistent with the states described by the simpler approach above. In addition, we notice that charge order can be also generated by a translationally invariant Jastrow factor, without explicitly breaking the symmetry in the Slater determinant, as shown in [46, 47]. The advantage is that we do not need to assume *a priori* any type of charge ordering and, if long-range order exists, charge-ordered states should be selected by the optimization of the Jastrow factor. In general, for the chosen set of hoppings and interaction terms, we never found charge orders that cannot be captured by the previous parametrization of equations (13) and (16).

Given the presence of the correlation term (i.e. the Jastrow factor), an analytical evaluation of the variational energy or of any correlation function is impossible on large sizes; nevertheless, a standard Monte Carlo sampling can be employed to obtain all the physical quantities with high accuracy.

### 3. Results

#### 3.1. Phase diagram for large $U$

We now investigate how the hopping terms in equation (1) modify the phase diagram obtained for the atomic limit, in the region $U \gg t_{b1}$. The schematic phase diagram is shown in figure 4. The three charge-ordered phases obtained in the atomic limit are stable also in the presence of finite values of the hopping terms; however, magnetic order is generated from virtual hopping processes involving charge-poor molecules, which form one-dimensional patterns in the lattice and are effectively half filled in all these phases. Antiferromagnetic correlations are then expected along these one-dimensional chains, which are formed by the bonds with hopping $t_{b1}$ and $t_{b2}$ for the nonpolar state and by the bonds with hopping $t_p$ ($t_q$) for the PCOI ' (PCOI). Therefore, in the nonpolar charge-ordered state, the two spins on the molecules of the same dimer have opposite orientations, thus implying that the dimer has no net magnetization. By contrast, the two polar states show ferromagnetic spin correlations within the dimers; here, each dimer contains one charge-rich and one charge-poor molecule, the magnetization being large in the latter one. Moreover, we observe long-range antiferromagnetic order of the magnetic moments of dimers.

In addition to these three states, a uniform DMI intrudes between the polar phases. This correlated phase should appear when $U$ is much larger than all the $V$ terms, in the region where $V_p$ and $V_q$ are competing [15–17]. Here, spin correlations are ferromagnetic within each dimer, since there is an average of three electrons per site: two electrons have opposite spins and do not contribute to the magnetic moment, which is fully due to the third electron that is delocalized between the two molecules. Similarly to the two polar charge-ordered states, also here the spins of the dimers possess long-range antiferromagnetic order. We find that the transitions between the DMI and the polar charge-ordered phases (PCOI and PCOI ') are continuous (see below). Close to the boundaries between nonpolar and polar charge-ordered phases, the DMI state can also be stabilized; however its energy remains higher than the energies of the other phases, indicating that it is a metastable state.

In order to understand the nature of the charge properties of all the insulating phases, we calculate the total charge structure factor $N(q)$ and the charge-disproportionation structure factor $N_{\rm CD}(q)$, defined as:


![](./images/813107471223619585_6.jpg)

$$
N(q)=\frac{1}{N_{s}} \sum_{i, j}\left\langle\left(n_{i}^{c}+n_{i}^{f}\right)\left(n_{j}^{c}+n_{j}^{f}\right)\right\rangle \mathrm{e}^{\mathrm{i} q \cdot\left(\boldsymbol{R}_{i}-\boldsymbol{R}_{j}\right)},\qquad(20)
$$

$$
N_{\mathrm{CD}}(q)=\frac{1}{N_{s}} \sum_{i, j}\left\langle\left(n_{i}^{c}-n_{i}^{f}\right)\left(n_{j}^{c}-n_{j}^{f}\right)\right\rangle \mathrm{e}^{\mathrm{i} q \cdot\left(\boldsymbol{R}_{i}-\boldsymbol{R}_{j}\right)},\qquad(21)
$$

where $\langle...\rangle$ indicates the expectation value over the variational wave function of equation (10). Here, $N(q=0)$ is set to zero. The metallic or insulating character can be assessed by inspecting the small-$q$ limit of the total charge structure factor. Indeed, in the limit $|\boldsymbol{q}| \to 0$, $N(q) \propto|\boldsymbol{q}|$ for a metal, while $N(q) \propto|\boldsymbol{q}|^{2}$ for an insulator [48, 49]. In addition, charge order is indicated by the presence of a Bragg peak in $N(q)$ or $N_{\mathrm{CD}}(q)$. In the former case, charge order is characterized by charge-rich dimers on one sublattice and charge-poor dimers on the other one, while, in the latter case, charge disproportionation occurs within the dimers.

In the following, we fix the Coulomb interactions to $U / t_{b 1}=10, V_{b 1} / t_{b 1}=4$, and $V_{b 2} / t_{b 1}=2$, and vary $V_{p}$ and $V_{q}$. Within this choice, in the atomic limit, the polar and nonpolar phases are degenerate for $V_{p}=V_{q}=3 t_{b 1}$. As shown in figure 5, all the phases presented in the phase diagrams are insulating, since $N(q) \propto|\boldsymbol{q}|^{2}$ in the limit $|\boldsymbol{q}| \to 0$, both along the $q_{y}=0$ and the $q_{x}=q_{y}$ lines in reciprocal space. Then, each insulating phase can be fully characterized by $N(q)$ and $N_{\mathrm{CD}}(q)$, see figures 6 and 7. The DMI does not show any Bragg peak either in $N(q)$ or in $N_{\mathrm{CD}}(q)$ (figures 6(d) and 7(d)), suggesting that no long-range charge order occurs. The nonpolar charge-ordered state shows the Bragg peak at $\boldsymbol{Q}=(\pi, \pi)$ in $N(q)$ (figure 6(c)), but no sharp peaks in $N_{\mathrm{CD}}(q)$ (figure 7(c)). This implies that staggered charge disproportionation appears between different dimers, but not within the dimers. Finally, the polar charge-ordered states show the Bragg peak at $\boldsymbol{Q}=(0,0)$ (PCOI') or $\boldsymbol{Q}=(\pi, \pi)$ (PCOI) in $N_{\mathrm{CD}}(q)$ (figures 7(a) and (b)), but no sharp peaks in $N(q)$ (figures 6(a) and (b)). This fact indicates charge disproportionation within the dimers, while the number of electrons in each dimer is constant. Each orbital has the same number of electrons at each site for $\boldsymbol{Q}=(0,0)$, while each orbital alternates between charge-rich and charge-poor configurations for $\boldsymbol{Q}=(\pi, \pi)$, see figure 4.

Remarkably, all polar and nonpolar phases can be stabilized within the variational approach also without considering magnetic order in the Slater determinant. By contrast, the DMI cannot be stabilized without including the $\mathcal{H}_{\mathrm{AF}}$ of equation (14), see figure 8. The charge patterns are similar to the ones that have been obtained previously with the inclusion of magnetic order (not shown).

### 3.2. Competition between charge and magnetic orders
We focus now on the interplay between charge and spin degrees of freedom near the boundary of the polar charge-ordered phases. In particular, we show the numerical results along the $V_{p}+V_{q}=3 t_{b 1}$ line (still fixing

![](./images/813107471223619585_7.jpg)

![](./images/813107471223619585_8.jpg)

$U/t_{b1}=10$, $V_{b1}/t_{b1}=4$, and $V_{b2}/t_{b1}=2$), which crosses the two polar and the DMI phases. The absolute value of the difference between the optimized chemical potentials $|\mu^c - \mu^f|$ for orbitals $c$ and $f$(see equation (13)) can be used as a diagnostic to detect polar and nonpolar states. As shown in figure 9, we find that $|\mu^c - \mu^f|$ is finite for $V_p/t_{b1} \lesssim 1.3$ and $V_p/t_{b1} \gtrsim 1.7$, while it vanishes in a narrow but finite region for $1.4 \lesssim V_p/t_{b1} \lesssim 1.6$, indicating the existence of the DMI. In addition, $|\mu^c - \mu^f|$ does not show any evidence of discontinuities at the transition points, strongly suggesting that the three phases are continuously connected. Indeed, near the phase boundary obtained in the atomic limit ($V_p/t_{b1}=1.5$) it is not possible to stabilize metastable wave functions with higher energies.

To further investigate the connection among these three phases, we calculate the charge-disproportionation structure factor as function of $V_p$, as shown in figure 10. When $V_q(V_p)$ is sufficiently large, $N_{CD}(q)$ shows a sharp peak at $\boldsymbol{Q}=(0,0)$ ($\boldsymbol{Q}=(\pi,\pi)$) (figures 10(a) and (b), respectively). By contrast, when $V_p \approx V_q$, $N_{CD}(q)$ shows a broad crest along the $q_x + q_y=2\pi$ direction (figures 10(c)-(e)). Importantly, there are no divergences in the thermodynamic limit, since the crest remains finite when increasing the size of the cluster. The peculiar one-dimensional-like shape of $N_{CD}(q)$ might be understood in the following simple way: for $V_p \approx V_q$, the emergence of charge order is controlled only by $V_{b1}$ and $V_{b2}$, which define diagonal chains in the lattice, see figure 1. It is then natural to expect that correlations do not show any dependence on the transverse direction.

![](./images/813107471223619585_9.jpg)

![](./images/813107471223619585_10.jpg)

The absence of charge disproportionation for $1.4 \lesssim V_p/t_{b1} \lesssim 1.6$ is clearly demonstrated by performing the size scaling of $N_{\rm CD}(Q)/L^2$ for $L \to \infty$. The results are reported in figure 11. For $V_p/t_{b1} \lesssim 1.3$ and $V_p/t_{b1} \gtrsim 1.7$, we have that $N_{\rm CD}(Q)/L^2$ is finite for $\boldsymbol{Q}=(0,0)$ and $\boldsymbol{Q}=(\pi,\pi)$, respectively. Instead, for $1.4 \lesssim V_p/t \lesssim 1.6$ this quantity goes to zero for $L \to \infty$, suggesting that the DMI is stable in this region.

Even if all the charge-ordered phases are present also in the absence of magnetic order, all of them are found to possess stable magnetic order when this possibility is included in the variational state, as shown in figure 12. The DMI shows the same absolute value of the magnetic moment for the orbitals $c$ and $f$, as expected for a charge uniform state. When the intersite Coulomb interactions become anisotropic (i.e. $|V_p - V_q| > 0$), magnetic orders for the orbitals $c$ and $f$ start to deviate. This is due to the fact that the charge-rich (charge-poor) molecular orbitals possess a smaller (larger) magnetic moment in the polar charge-ordered phases. Notice that the PCOI state has a larger magnetic order than the PCOI $'$ one. This may be due to the anisotropy in the hopping terms. Indeed, in the PCOI state the singly-occupied molecules are connected by $t_q$, while in the PCOI $'$ one they are connected by $t_p$; since $t_p > t_q$ (see equation (5)) the latter case has more charge fluctuations (i.e. it is closer to a metal-insulator transition), thus implying smaller magnetic moments.

![](./images/813107471223619585_11.jpg)

![](./images/813107471223619585_12.jpg)

### 3.3. Twelve-site ordered metallic phase
Finally, we focus our attention on the charge-ordered metal (COM) that appears for small values of $U/t_{b1}$.
Therefore, we now fix $V_{b1}/t_{b1}=4$, $V_p/t_{b1}=3.5$, and $V_q/t_{b1}=3$ and vary $U/t_{b1}$ and $V_{b2}/t_{b1}$. The phase diagram is shown in figure 13(a). Here, a large metallic phase, with honeycomb-like charge ordering, appears, for relatively small values of the intramolecular interaction. This charge-ordered pattern is similar to the three-sublattice one [46, 50, 51], which has been stabilized on the triangular lattice for intermediate values of the nearest-neighbor interaction. In our case, the periodicity is extended to 12 sites due to the anisotropy of the parameters.

The emergence of the honeycomb-like COM can be easily understood when all the bonds (of $b_1$-, $b_2$-, $p$-, and $q$-type) are equivalent. In this 'isotropic' limit, when considering *each* molecule as an independent site, the underlying lattice becomes triangular, see figure 13(b). In this case, by decreasing the intramolecular Coulomb interaction $U$, there is an insulator to metal transition, with a metallic phase below the critical point. Moreover, since intermolecular Coulomb interactions screen the actual value of $U$, the metallic phase is even more stable

![](./images/813107471223619585_13.jpg)

Figure 12. Optimized magnetic order parameters for the charge-rich ($m_1^a$) and for the charge-poor ($m_2^a$) molecules, as a function of $V_p/t_{b1}$. $m_1^a < m_2^a$ in the charge-ordered phases, while they become equal in the uniform DMI. Data are shown for three lattice sizes: $L=6$ (squares), $L=8$ (circles), and $L=10$ (triangles).

![](./images/813107471223619585_14.jpg)

Figure 13. (a) Phase diagram in the $U-V_{b2}$ plane, obtained by fixing $V_{b1}/t_{b1}=4$, $V_p/t_{b1}=3.5$, and $V_q/t_{b1}=3$. Three phases are present: the nonpolar charge-ordered insulator (NPCOI), the polar charge ordered insulator (PCOI), and a 12-sublattice charge ordered metal (COM). The location of the transition between the NPCOI and PCOI phases for large $U$ is in agreement with the atomic limit, see figure 3. (b) Schematic charge configuration of the 12-sublattice charge-ordered metal.

when the $V$'s are present in the model. However, the presence of intermolecular Coulomb interactions leads to a spontaneous symmetry breaking in the translational symmetry and to charge disproportionation, that on the triangular lattice it is natural to assume with a three-sublattice ordering $A-B-C$. For an average occupation per site (i.e. molecule) $n=3/2$, the only possible choice to minimize the energy loss due to the intermolecular interactions is then to reduce the electron occupation on one sublattice and increase it on the other two (the limiting case being $n_A=0.5$ and $n_B=n_C=2$).

We investigate now the stability of the COM against a normal metal when decreasing the intermolecular interactions. In this case, we vary all the Coulomb terms together, taking $V_{b1}/t_{b1}=\alpha$, $V_{b2}/t_{b1}=0.5\alpha$, $V_p/t_{b1}=0.875\alpha$, and $V_q/t_{b1}=0.75\alpha$, while the intramolecular interaction is fixed to $U/t_{b1}=6$. As shown in figure 14, for $\alpha \lesssim 2$ the ground state is found to be a uniform metal, with no charge disproportionation. Charge order appears for $\alpha \approx 2.5$ and is characterized by the rich-rich-poor pattern. A direct comparison between the COM at $\alpha=4$ and the uniform metallic phase is presented in figure 15. Both phases are indeed metallic, since $N(q) \propto |q|$ for small momenta (figures 15(a), (b)). On the contrary, the formation of charge order in the COM phase, is signaled by the appearance of strong peaks in both the total charge structure factor $N(q)$ and the structure factor for charge disproportionation $N_{\rm CD}(q)$, corresponding to the real-space configuration illustrated in figure 13(b).

### 4. Summary and conclusions

By using variational wave functions and quantum Monte Carlo techniques, we have investigated the ground-state phase diagram of an extended two-orbital Hubbard model at 3/4 filling on the anisotropic triangular

![](./images/813107471223619585_15.jpg)

**Figure 14.** Electron density in each of the six sublattices defined in equation (18), for orbitals $c$ and $f$, as a function of $\alpha = V_{b1}/t_{b1}$, which controls the strength of the intermolecular Coulomb interactions. Data are shown on the $L = 12$ lattice size.

![](./images/813107471223619585_16.jpg)

**Figure 15.** Upper panels: charge structure factor $N(\boldsymbol{q})$, divided by $|\boldsymbol{q}|$, for the COM phase (a) and for the uniform metallic phase (b). Data are shown along the $q_{y}=0$ (red) and the $q_{x}=q_{y}$ (blue) lines in reciprocal space, for $L = 6$ (squares) and $L = 12$ (circles). Middle panels: charge structure factor $N(\boldsymbol{q})$ as a function of $\boldsymbol{q}$, for the COM phase (c) and for the uniform metallic phase (d). Lower panels: structure factor for charge disproportionation $N_{\text{CD}}(\boldsymbol{q})$ as a function of $\boldsymbol{q}$, for the COM phase (e) and for the uniform metallic phase (f).

lattice, which is relevant for the $\kappa$-(ET)$_2$X family of organic charge-transfer salts. As a representative example, we have chosen the hopping parameters that correspond to $\kappa$-(ET)$_2$Cu[N(CN)$_2$]Cl and varied the interaction terms. For large values of the intramolecular repulsion $U$ and by varying the strength of the competing intermolecular Coulomb interactions, we stabilize two polar and one nonpolar charge-ordered insulating phases, as well as a uniform DMI. All these phases posses magnetic order, which is mainly determined by the behavior of the spins at the charge-poor molecules (that are effectively at half filling). We have also found that the DMI is continuously connected to the two polar charge-ordered states: when the anisotropy between the intersite Coulomb interactions $V_{p}$ and $V_{q}$ goes to zero, the Bragg peaks of the two polar phases melt and form a one-dimensional-like structure. For smaller values of the intramolecular interaction $U$, we find a COM, that is similar to the three-sublattice (rich-rich-poor) charge order on the triangular lattice; however, the anisotropy in the intermolecular parameters modify the period of the charge ordering to a 12-sublattice structure. Although

COMs in ET organic compounds often show a stripe-like charge pattern [52, 53], the observation of the COM phase would be an intriguing proof for the possibility of stabilizing nontrivial charge orders in metallic phases.

In organic charge transfer salts, the size of the intermolecular Coulomb interactions is expected to be larger when the molecules are closer. In this respect, it is plausible to assume that $V_{b1}$ is the stronger intermolecular Coulomb interaction and that $V_p \gtrsim V_q$, see figure 1. In addition to the fact that the strongest Coulomb interaction is the intramolecular one $U$, most of the compounds should be located at the border between the PCOI and the DMI phases. Since the two phases are continuously connected, a small amount of anisotropy $V_p \gtrsim V_q$ will lead to a weak charge order, as shown for example in figure 9; this fact may explain the difficulty in finding stable charge ordering in $\kappa$-(ET)$_2$Cu[N(CN)$_2$]Cl. Nevertheless, our results indicate that the PCOI phase is polarized, suggesting that charge order is the correct mechanism to induce a finite polarization. Moreover, we observe that magnetism coexists with electronic polarization, as observed in experiments, even if it is not the driving mechanism for it, since polarization occurs also in the absence of magnetic order. In this respect, our study shows that ferroelectricity in organic charge-transfer salts is not driven by magnetism.

Finally, we would like to conclude by mentioning that superconducting pairing correlations (with unconventional pairing symmetries) may be enhanced close to charge-ordered phases in multiorbital Hubbard models [37]. Investigating possible superconductivity (also coexisting with charge ordering) is left for future studies.

### Acknowledgments

The authors would like to thank M Altmeyer, C Gros, D Guterding, A J Kim, and S M Winter for fruitful discussions. RK and RV acknowledge the support of the German Science Foundation (Deutsche Forschungsgemeinschaft) through Grant No. SFB//TR49.

### ORCID iDs

Ryui Kaneko <https://orcid.org/0000-0001-7994-6381>
Luca F Tocchio <https://orcid.org/0000-0002-0921-8554>
Roser Valentí <https://orcid.org/0000-0003-0497-1165>
Federico Becca <https://orcid.org/0000-0002-6142-2050>

### References

[1] van den Brink J and Khomskii D I 2008 *J. Phys.: Condens. Matter* **20** 434217
[2] Khomskii D I 2006 *J. Magn. Magn. Mater.* **306** 1
[3] Fiebig M 2005 *J. Phys. D: Appl. Phys.* **38** R123
[4] Katsura H, Nagaosa N and Balatsky A V 2005 *Phys. Rev. Lett.* **95** 057205
[5] Mostovoy M 2006 *Phys. Rev. Lett.* **96** 067601
[6] Lunkenheimer P and Loidl A 2015 *J. Phys.: Condens. Matter* **27** 373001
[7] Lunkenheimer P et al 2012 *Nat. Mater.* **11** 755
[8] Takahashi T, Nogami Y and Yakushi K 2006 *J. Phys. Soc. Japan* **75** 051008
[9] Yakushi K 2012 *Crystals* **2** 1291
[10] Lunkenheimer P, Hartmann B, Lang M, Müller J, Schweitzer D, Krohns S and Loidl A 2015 *Phys. Rev. B* **91** 245132
[11] Sedlmeier K, Elsässer S, Neubauer D, Beyer R, Wu D, Ivek T, Tomić S, Schlueter J A and Dressel M 2012 *Phys. Rev. B* **86** 245103
[12] Tomić S, Pinterić M, Ivek T, Sedlmeier K, Beyer R, Wu D, Schlueter J A, Schweitzer D and Dressel M 2013 *J. Phys.: Condens. Matter* **25** 436004
[13] Lang M, Lunkenheimer P, Müller J, Loidl A, Hartmann B, Hoang N H, Gati E, Schubert H and Schlueter J A 2014 *IEEE Trans. Magn.* **50** 2700107
[14] Powell B J and McKenzie R H 2011 *Rep. Prog. Phys.* **74** 056501
[15] Kino H and Fukuyama H 1995 *J. Phys. Soc. Japan* **64** 2726
[16] Kino H and Fukuyama H 1995 *J. Phys. Soc. Japan* **64** 4523
[17] Kino H and Fukuyama H 1996 *J. Phys. Soc. Japan* **65** 2158
[18] Komatsu T, Matsukawa N, Inoue T and Saito G 1996 *J. Phys. Soc. Japan* **65** 1340
[19] Nakamura K, Yoshimoto Y, Kosugi T, Arita R and Imada M 2009 *J. Phys. Soc. Japan* **78** 083710
[20] Kandpal H C, Opahle I, Zhang Y-Z, Jeschke H O and Valentí R 2009 *Phys. Rev. Lett.* **103** 067004
[21] Scriven E P and Powell B J 2012 *Phys. Rev. Lett.* **109** 097206
[22] Koretsune T and Hotta C 2014 *Phys. Rev. B* **89** 045102
[23] Scriven E and Powell B J 2009 *Phys. Rev. B* **80** 205107
[24] Nakamura K, Yoshimoto Y and Imada M 2012 *Phys. Rev. B* **86** 205117
[25] Shinaoka H, Misawa T, Nakamura K and Imada M 2012 *J. Phys. Soc. Japan* **81** 034701
[26] Seo H 2000 *J. Phys. Soc. Japan* **69** 805
[27] Mori T 2016 *Phys. Rev. B* **93** 245104
[28] Naka M and Ishihara S 2010 *J. Phys. Soc. Japan* **79** 063707
[29] Hotta C 2010 *Phys. Rev. B* **82** 241104(R)

[30] Gomi H, Inagaki T J and Takahashi A 2016 *Phys. Rev. B* **93** 035105

[31] Abdel-Jawad M, Terasaki I, Sasaki T, Yoneyama N, Kobayashi N, Uesu Y and Hotta C 2010 *Phys. Rev. B* **82** 125119

[32] Gomes N, De Silva W W, Dutta T, Clay R T and Mazumdar S 2016 *Phys. Rev. B* **93** 165110

[33] De Silva W W, Gomes N, Mazumdar S and Clay R T 2016 *Phys. Rev. B* **93** 205111

[34] Guterding D *et al* 2016 *Phys. Rev. Lett.* **116** 237001

[35] Guterding D, Altmeyer M, Jeschke H O and Valentí R 2016 *Phys. Rev. B* **94** 024515

[36] Sekine A, Nasu J and Ishihara S 2013 *Phys. Rev. B* **87** 085133

[37] Watanabe H, Seo H and Yunoki S 2017 *J. Phys. Soc. Japan* **86** 033703

[38] Sato N, Watanabe T, Naka M and Ishihara S 2017 *J. Phys. Soc. Japan* **86** 053701

[39] Okazaki R, Ikemoto Y, Moriwaki T, Shikama T, Takahashi T, Mori H, Nakaya H, Sasaki T, Yasui Y and Terasaki I 2013 *Phys. Rev. Lett.*
**111** 217801

[40] Kaneko R, Tocchio L F, Valentí R and Gros C 2016 *Phys. Rev. B* **94** 195111

[41] Altmeyer M and Guterding D 2016 private communications

[42] Yokoyama H and Shiba H 1987 *J. Phys. Soc. Japan* **56** 1490

[43] Gros C 1988 *Phys. Rev. B* **38** 931(R)

[44] Capello M, Becca F, Fabrizio M, Sorella S and Tosatti E 2005 *Phys. Rev. Lett.* **94** 026406

[45] Tocchio L F, Arrigoni F, Sorella S and Becca F 2016 *J. Phys.: Condens. Matter* **28** 105602

[46] Tocchio L F, Gros C, Zhang X-F and Eggert S 2014 *Phys. Rev. Lett.* **113** 246405

[47] Kaneko R, Tocchio L F, Valentí R, Becca F and Gros C 2016 *Phys. Rev. B* **93** 125127

[48] Feynman R P 1954 *Phys. Rev.* **94** 262

[49] Tocchio L F, Becca F and Gros C 2011 *Phys. Rev. B* **83** 195138

[50] Hotta C and Furukawa N 2006 *Phys. Rev. B* **74** 193107

[51] Février C, Fratini S and Ralko A 2015 *Phys. Rev. B* **91** 245111

[52] Watanabe M, Noda Y, Nogami Y and Mori H 2003 *Synth. Met.* **135** 665

[53] Kakiuchi T, Wakabayashi Y, Sawa H, Takahashi T and Nakamura T 2007 *J. Phys. Soc. Japan* **76** 113702