# Journal of Materials Chemistry C

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: Y. Wang, S. Li, C. Zhang and P. Wang, J. Mater. Chem. C, 2018, DOI: 10.1039/C8TC02500B.

![](./images/813000194755919873_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the author guidelines.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the ethical guidelines, outlined in our author and reviewer resource centre, still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/813000194755919873_2.jpg)

rsc.li/materials-c

# High-Temperature Dirac Half-Metal PdCl₃: A Promising Candidate for Realizing Quantum Anomalous Hall Effect
Ya-ping Wang, $^{1,3}$ Sheng-shi Li, $^{1,2}$ Chang-wen Zhang, $^{1,*}$ and Pei-ji Wang $^{1}$

1 School of Physics and Technology, University of Jinan, Jinan, Shandong, 250022, People's Republic of China
2 School of Physics, State Key laboratory of Crystal Materials, Shandong University, Jinan, Shandong, 250100, People's Republic of China
3 Advanced Materials Institute, Qilu University of Technology (Shandong Academy of Science), Jinan, Shandong, 250014, People's Republic of China

The prospect of the Dirac half-metal (DHM) and the realization of quantum anomalous Hall effect (QAHE) on a honeycomb lattice without external fields is a great challenge in experiments due to the structural complexities of two-dimensional (2D) crystals. Here, based on density-functional theory calculations, we propose an ideal candidate material for realizing these exotic quantum states in 2D honeycomb metal-halogen lattice, single-layer PdCl₃. We find that the ground state of PdCl₃ is a 100% spin-polarized DHM with a ferromagnetic Curie temperature $T_C = 528$ K predicted from Monte Carlo simulations. Upon including spin-orbit coupling (SOC), PdCl₃ reveals QAHE due to the splitting of manifold of Pd $|d_{xz}>$ and $|d_{yz}>$ bands near the Fermi level, which is characterized by the nontrivial Chern number ($C = -1$) and chiral edge states. Especially, the origin of topological properties of PdCl₃ honeycomb lattice is explained by the tight-binding model. The sensitivity of nontrivial topology on cooperative effect of the electron correlation of Pd-4d electrons and SOC is demonstrated: when increasing the on-site Coulomb repulsion $U$, a sizable nontrivial band gap $E_g = 68.6$ meV is obtained. Additionally, we explore the mechanical and dynamical stability, as well as strain response of PdCl₃ for possible epitaxial growth conditions in experiments. The coexistence of high temperature DHM and QAHE in PdCl₃ presents a promising platform for the emerging area of spintronics devices with dissipationless edge states.

## I. INTRODUCTION

During the last few years, two-dimensional (2D) crystals have been attracting enormous attention because they are considered as potential candidates for future application in high density information storage and quantum computational devices.[1] Electron spins in 2D crystals provide an additional degree of freedom to tailor their properties for spintronics. [2] Especially, the occurrence of quantum anomalous effect (QAHE) in Chern insulator [3,4], a quantized version of anomalous Hall effect (QAH) [5], arising from spin-orbit coupling (SOC) and time-reversal symmetry (TRS) broken in the presence of magnetic order [including ferromagnetic(FM) and antiferromagnetic (AFM) states], which conspires to generate energy gap $E_g$ in the bulk and gapless chiral edge states, is of great interest. QAHE is generally characterized by a nonzero Chern number ($C \neq 0$) whose energy-momentum dispersion threads the gap of finite-width wires, while their wave functions have finite spatial extent around the ribbon edges. Distinct from spin-polarized helical edge states observed in 2D quantum spin Hall (QSH) effect, [6-9] the edge states in Chern insulator allow only one spin species to flow unidirectionally, resulting in a quantized Hall conductance $\sigma_{xy} = (e^2/h)C$, which is robust against defects and disorders. Thus, the quantum transport of surface (edge) contamination over hundreds of micrometers makes them superior to QSH insulators where the electrons can be backscattered by breaking TRS. [10] The zero-field dissipationless chiral edge transport channels in Chern insulators establish a solid foundation for understanding this new type of topologically driven phase transition in 2D materials. Experimentally, the quantized conductance $\sigma_{xy} = e^2/h$ in Cr (V)-doped (Bi, Sb)₂Te₃ thin films have been observed at $T \lesssim 0.5$ K, with a FM Curie temperature $T_C \approx$ 15-20 K [10,11], which opens up a brand new for applications in next-generation electronic and spintronics devices with low power consumption. [12, 13]

*Email: ss_zhangchw@ujn.edu.cn;

The idea of quantized Hall conductance without Landau levels on a honeycomb lattice is first introduced by F. D. M. Haldane in the absence of an external magnetic field, which is a toy model of QAHE. [14] Although THM model is unlikely to be directly physically realized, his vision on topological order inspires extensive attentions for realistic materials exhibiting QAHE, where the honeycomb lattice is suggested as a first ingredient [15,16], *e.g.*, graphene decorated with heavy transition metals [17] or graphene/FM heterostructure [18]. Honeycomb lattices including silicene, germanene, and stanene, which possess a relatively strong intrinsic SOC, could also show QAHE by introducing exchange interaction *via* magnetic adatoms [19] or surface functionalization [20]. Their realization could open access to low power consumption electronics as well as many fundamental phenomena like image magnetic monopoles, Majorana fermions, and topological magnetoelectric effects (TME). These proposals share a common feature of topologically nontrivial bands derived from $s$ and $p$ orbitals. Unfortunately, all these 2D stoichiometric magnetic lattices exist rarely in nature, thus are difficult to be fabricated experimentally due to their structural complexity and to keep the topology of these systems unaffected simultaneously.

Unlike the $s$ or $p$ orbital based systems, [9-11] 2D thin crystals with $d$ or $f$ orbital dominated electronic structures have the possibility of high temperature realizations due to their strong SOC. Systems predicted to realize this concept include perovskite bilayers along the [111] crystallographic direction with a buckled honeycomb structure and SOC has been predicted as a 2D time-reversal invariant topological insulators in $t_{2g}$ bands in $SrIrO_3$ and $LaOsO_3$ crystals. [21-24] Ultrathin 2D crystals hosting nickelate $e_g$ orbitals [25-27] and pyrocholre iridated $j_{eff}=1/2$ orbitals have also been proposed to exhibit QAHE with Chern number $C=1$. However, an important challenge in these 2D crystals is fact that the correlations are too weak to drive magnetism and break TRS. On the other hand, QAHE in Kagome lattice has been observed including, for example, 2D Mn-DCA lattice[28], triphenyl-manganese (TMn) [29], $Nb_2O_3$ [30], and so on, but the nontrivial band gaps of these 2D lattices are too small to impede the observations of QAHE. Beyond that, the Dirac half-metal (DHM), a combination of single-spin massless Dirac fermions and half-metal with broken TRS, also provides a design concept of Chern insulator. When the SOC effect is included, a band gap opening occurs in one spin channel, which would lead towards the QAHE. To date, the DHM only exists in few 2D structures, such as $YN_2$, $C_7N_6$, $VCl_3$, $FeBr_3$ and $NiCl_3$, [31-35] and some of them have been theoretically demonstrated as QAH insulator with sizable global gap. Hence, searching for materials with intrinsic DHM states is of great important for the realization of QAHE.

View Article Online
DOI: 10.1039/C8TC02500B

The layered crystals of transition-metal trichloride, $MCl_3$ ($M$ = Ti, V, Cr, Fe, Mo, Ru, Rh, Ir), [36] have been investigated long before the present focus on the layered materials like honeycomb graphene. Due to the weak interlayer van der Waals interactions, the 2D crystal can be easily exfoliated from the corresponding 3D layered materials [37], where the transition-metal atoms are uniformly distributed in a honeycomb structure. Especially, M. Ziatdinov [38] find that a pseudospin 1/2 Mott phase of a honeycomb $RuCl_3$ can host the celebrated 2D Kitaev model, an elusive quantum spin liquid ground state, which motivate us to wonder whether these type systems become the nontrivial topological materials. In this context, using first-principles calculations and tight-binding (TB) model, we propose a new 2D honeycomb metal-halogen lattice, single-layer $PdCl_3$, as an ideal material candidate for realizing both DHM and QAHE. The structural stability of $PdCl_3$ has been examined by elastic constants, phonon spectrum and molecular dynamics simulations, which demonstrates that it is both mechanically and dynamically stable. Self-consistent spin-polarized calculations indicate that the $PdCl_3$ hosts a DHM feature with spin-down band gaps of 1.2 eV. Based on Monte Carlo (MC) simulations in 2D Ising model, we find that $PdCl_3$ exhibits a higher Curie temperature of $T_C=528$ K, far beyond the room temperature. The origin of FM order can be attributed to the superexchange coupling between magnetic Pd ions *via* the bridging Cl atoms, which is consistent with the Goodenough-Kanamori-Anderson (GKA) rules. [39-41] Upon including the effect of SOC, $PdCl_3$ becomes a Chern insulator due to TRS breaking, which is characterized by nonzero Chern number ($C=-1$) and chiral edge states. The nontrivial topology is robust against biaxial strain, with its band gap reaching up to 68.6 meV, which is large enough to observation in experiments. In comparison to Cr or V doped (Bi, Sb)$_2$Te$_3$ thin films[9-11], such a lattice without any magnetic doping is easier to synthesize and has a much higher homogeneity. These findings indicate that $PdCl_3$ is an experimentally feasible candidate for topotronics devices without an external magnetic field.

## II. COMPUTATIONAL DETAILS

All the calculations on electronic and topological properties are based on density-functional theory (DFT) as implemented in the Vienna ab initio simulation package (VASP).[42] The projector-augmented-wave (PAW) potential, Perdew-Burke -Ernzerhof (PBE) exchange-correlation functional [43,44] and the plane-wave basis with a kinetic energy cutoff of 500 eV are employed. The Brillouin zone is sampled by using an $11\times11\times1$

$\Gamma$-centered Monkhorst-Pack grid. SOC is included by a second variational procedure on a fully self-consistent basis. During structural optimization, all atomic positions and lattice parameters are fully relaxed, and the maximum force allowed on each atom is less than 0.02 eV/ Å. Furthermore, the screened exchange hybrid density functional by Heyd-Scuseria -Ernzerhof (HSE06) [45] is adopted to check the electronic structure. The Pd-$4d$ orbitals have generally important correlation effects, so we validate our results by using the DFT+$U$ following the approach of Dudarev *et al.* [46], in which several on-site Hubbard $U$ parameters are selected for Pd-$4d$ orbital. The phonon spectrum calculations are carried out by using DFT perturbation theory as implemented in the PHONOPY code [47] combined with VASP.

## III. RESULTS AND DISCUSSION

### A. Crystal structure and stability

In the present work, we study 2D honeycomb lattice PdCl₃ consisting of a *trilayer* Cl-Pd-Cl, where a sheet of Pd atoms is sandwiched between two sheets of Cl atoms, as illustrated in Fig. 1(a). From the calculations of total energy of the system we find that the optimal structure corresponds to $a = 6.34$ Å with the Pd-Pd distance of 3.62 Å. Structural stability of PdCl₃ is examined by the formation energy expressed as

$$
E_{\mathrm{f}}=E\left(\mathrm{PdCl}_{3}\right)-E(\mathrm{Pd})-3 / 2 \mu\left(\mathrm{Cl}_{2}\right), \tag{1}
$$

where $E\left(\mathrm{PdCl}_{3}\right)$ and $E(\mathrm{Pd})$ are the total energies of the PdCl₃ and Pd crystals, respectively, while $\mu$ (Cl₂) is the chemical potential of Cl₂ gas. The obtained negative value, $E_{\mathrm{f}}=-4.27$ eV, indicates that PdCl₃ is a strongly bonded network. Additionally, we calculate the phonon spectrum of PdCl₃, as shown in Fig. 1(c). The absence of imaginary phonon modes confirms the dynamical stability of this structure. The thermal stability of single-layer PdCl₃ is further assessed by performing molecular dynamics simulations with a 3×3×1 supercell at 300K. As can be seen from Fig. 1(d), the total energy fluctuates smoothly with small amplitudes after preheating process, revealing a favorable thermal stability. Therefore, this structure can be verified potentially by using a standard angle-resolved photoemission spectroscopy in experiments.

![](./images/813000194755919873_3.jpg)

FIG. 1 (a) Top and side view of PdCl₃ lattice with lattice vectors $a_1$ and $a_2$ in the $xy$ plane. Rhombus shows the unit cell. (b) The first Brillouin zone of PdCl₃ lattice with reciprocal lattice vectors $b_1$ and $b_2$. (c) The calculated phonon spectrum. (d) Variation of the energy from 1000 to 5000 fs during molecular dynamics simulations at a temperature of 300 K for PdCl₃ lattice.

![](./images/813000194755919873_4.jpg)

FIG. 2 (a) Energy level diagram of Pd³⁺ in PdCl₃. (b) and (c) superexchange coupling mechanism of PdCl₃.

### B. Magnetic properties and Curie temperature

Now we turn to the magnetic properties at the ground state for PdCl₃. Self-consistent DFT calculations give a spin-polarized state with an integer magnetic moment of $2.0\ \mu_B$ per unit cell arising mainly from Pd atom ($0.72\ \mu_B$). To understand the origin of magnetic moment, we begin to analysis the crystal symmetry of the Pd-$4d$ orbital. As shown in Fig. 2(a), each Pd atom is coordinated by six Cl atoms with the space group P31M, forming a distorted *octahedral* crystal field. In a perfect *octahedral* crystal field, the Pd-$4d$ state split into three $t_{2g}$ and two $e_g$ sub-states, as illustrated in stage (II) in Fig. 2(a). Due to the $D_{3d}$ point-group symmetry at the $\Gamma$ point, structural distortion of PdCl₆ *octahedron* makes the $t_{2g}$ state further split into the $a$ and double-generated $e_g'$ states, which is distinctly different from that in transition-metal oxides, [48-50] while they are still energetically lower than that of $e_g$ states (see stage (III) Fig. 2(a)). When an exchange filed, $E_{\text{ex}}$, is introduced by

internal magnetism, the degenerate $e_g$, $e_g'$, and $a$ states split significantly due to Hund's coupling. Hence, for a nominal $\text{Pd}^{3+}$ state, six electrons with both spin-up and spin-down fully occupy $e_g'$ and $a$ states, while only one electron is left in the $e_g$ spin-up channel, resulting in an integer magnetic moment. These are consistent with the DFT calculated band structure of $\text{PdCl}_3$, which would discuss in section C in the following.

In order to identify its preferred magnetic ground state, a FM and two AFM magnetic configurations are constructed based on a 2×2×1 supercell, as depicted in Fig. 3(a). In comparison, the FM coupling is more favorable than AFM1 and AFM2 structures with energy differences ($\Delta E$) of 644.68 meV and 525.76 meV per supercell, respectively. Actually, the non-collinear AFM configuration, *i. e.* $120^\circ$ AFM, is also checked, where such magnetic phase has a higher energy. To realize spintronics applications for $\text{PdCl}_3$, it is necessary to obtain the change trend of local magnetism with temperature. We thus employ MC simulations to predict the FM transition temperature of $\text{PdCl}_3$. The magnetocrystalline anisotropic energy (MAE), which is defined as the energy difference of the magnetic moments constrained in $x$ and $z$ axis, is calculated to be 5.3 meV/f.u., indicating that the $z$ axis is the easy one for the magnetization in $\text{PdCl}_3$. Taking into account the exchange-coupling parameters of the nearest- ($J_1$), next-nearest- ($J_2$), and next-next-nearest-neighbors ($J_3$), the Hamiltonian in 2D Ising model is written as:

$$
H = -\sum_{i,j} J_1 M_i M_j -\sum_{i,k} J_2 M_i M_k -\sum_{i,l} J_3 M_i M_l \tag{2}
$$

where $M$ is the spin magnetic moment per Pd atom, and $(i,j)$, $(i,k)$, and $(i,l)$ denote the nearest, next-nearest, and next-next-nearest sites pairs. The calculated $J_1$ and $J_2$ are 26.86 meV and 3.00 meV, while the $J_3$ of 0.12 meV is too small that can be neglected. Here, the Curie temperature is evaluated by MC simulation in which a 200 × 200 supercell with the periodic boundary conditions is employed and lasted for $1 \times 10^9$ loops. Figure 3 gives the relationship of temperature dependent magnetic moment per chemical formula. Note that the magnetic moment decreases to $0.0\ \mu_B$ when the temperature is higher than 528 K. To make the FM-paramagnetic transition more clear, we calculate the heat capacity $(C_V)$ expressed as:

$$
C_{\mathrm{v}}=\lim _{\Delta T \rightarrow 0} \frac{\Delta E_{\mathrm{T}}}{\Delta T} \tag{3}
$$

where $\Delta E_T$ is the change of the total energy as the temperature increases from $T$ to $T+\Delta T$. From the plot of $C_v$ with temperature in Fig. 3, we obtain the Curie temperature is indeed 528 K and the FM-paramagnetic transition is a second-order phase transition. This implies the possibility of stabilize FM order of $\text{PdCl}_3$ at finite temperature.

We then ask what is the mechanism behind the FM coupling with regards to the localized magnetic moments of Pd ions? It is generally assumed that the direct exchange interaction, which favors FM phase, may be possible main reason for FM materials. However, by checking the distributions of spin-polarized electron wave functions, we find that both the spin-up and spin-down channels are identical without mutual influence of the localized moments. So the direct interactions of spin wave functions between Pd atoms are excluded. Interestingly, superexchange interaction, which generally gives rise to AFM phase for systems with cation-anion-cation bond angles of $180^0$, can provide an alternative way for systems with cation-anion-cation bond angles of $90^0$, which favors FM phase based on GKA rules. [39-41]. As illustrated in Figs. 2(b) and (c), $\text{PdCl}_3$ belongs to this case because the optimized Pd-Cl-Pd bond angles is $94.6^0$, which is near the ideal $90^0$ bond angle. In this respect, the Cl-$p_\sigma$ orbitals are orthogonal to $4d$ orbitals of the two neighboring Pd ions, thus gives rise to zero overlap integral $S$. According to the Heitler-London model [51], $J=2k +4\beta S$, where $k$ and $\beta$ are potential exchange and hopping integral, respectively, we obtain $J=2k$, which is positive because of Hund's rule reflected by the parallel spins as shown in Fig. 2(c). As a result, $\text{PdCl}_3$ exhibits FM order.

![](./images/813000194755919873_5.jpg)

FIG. 3 (a) Schematics of different magnetic configurations: FM, AFM1 and AFM2. (b) Monte Carlo simulations on the average magnetic moment and heat capacity ($C_V$) of $\text{PdCl}_3$.

### C. Dirac half-metal behavior

Having established the ground-state magnetic structure of $\text{PdCl}_3$, in Figs. 4(a) and (b) we proceed to explore spin-resolved band structures and corresponding local density of states (LDOS) in the absence of SOC, where the spin-up and spin-down channels are shown in different colors, respectively. Note that $\text{PdCl}_3$ exhibits nonzero exchange splitting of 0.47 eV

between up and down spin bands, i.e., the spin-down channel maintains the insulating character, while the valence band maximum (VBM) with up-spin shifts down and crosses the Fermi level, demonstrating a half-metal, as shown in Fig. 4(a). In terms of Griffith's crystal field theory, we also obtain the relative strength of crystal field splitting $\Delta E_{\text{cf}} \simeq 0.86$ eV in octahedral crystal field PdCl₆. More interestingly, as plotting 3D band profile at K point (see Fig. 4(d)), there is a spin-polarized Dirac fermion near $E_F$ in spin-up channel, called as DHM with 100% spin polarization. Unlike conventional Dirac cone systems, here an excited Dirac fermion can be fully spin polarized. On this occasion, the Fermi velocity $(v_F)$, $v_F = E(q)/h|q|$, can be valuated by fitting the Dirac bands at $k = \text{K} + q$ to the expression of $v_F$. We find $v_F = 3.9 \times 10^5$ m/s, which is approximately 39 % of that of graphene. However, it is almost of the same order as the electron saturation velocity in silicon crystal ($\sim 10^5$ m/s), implying the high electron mobility in the conducting spin channel. High electron mobility in one spin channel (spin-up) and relatively large insulating gap (spin-down) in the opposite spin meet the demand of filtering the current into a single spin channel, thus are unique advantages in polarization optics and spintronics [52]. Additionally, we must point out that the previous reported Dirac materials, such as IV-based 2D honeycomb lattice, [53-55] are characterized by Dirac states composed of p-orbital with week SOC. However, the Dirac states of PdCl₃ are mainly derived from the d orbital.

Upon the inclusion of SOC, despite the Dirac cone feature is preserved, a nontrivial energy band gap opens in spin-up channel around $E_F$, as illustrated in Fig. 4(c). To overcome the underestimation of band gap, we further employ HSE06 to check the band gap, see Fig. S1. Note that the nontrivial gap at Fermi level is enhanced to 63.2 meV, which is comparable to the result form $U = 3.5$ eV in the GGA+U calculations. The SOC-induced band gap opening suggests an indicator of the appearance of QAHE, which is discussed in the following section.

### D. Tight-binding Hamiltonian

To well understand the origin behind FM order, we further carry out analysis on the Pd honeycomb lattice in terms of an effective TB model for d state, in that the Dirac bands near $E_F$ are mainly composed of $|d_{xz} >$ and $|d_{yz} >$ orbitals. Since the $z$-component of the spins $(\sigma^z)$ perpendicular to PdCl₃ plane is a conserved quantum number, we only consider the spin-up bands with and without SOC near the Fermi level. The TB Hamiltonian in the absence of SOC in momentum space can be given by

$$
H = \sum_{\vec{k}} \psi_{\vec{k}}^{\dagger} \left( H_{00} + \sum_{\vec{\delta}_j} H_{0\vec{\delta}_j} e^{i\vec{k}\cdot\vec{\delta}_j} \right) \psi_{\vec{k}}
$$

where the wave functions of Pd atoms can be expressed as
$$
\psi = \left( \text{c}_{\text{A}\mu}, \text{c}_{\text{B}v}, ... \right)^{\text{T}}
$$

$$
\psi^{\dagger} = \left( \text{c}_{\text{A}\mu}^{\dagger}, \text{c}_{\text{B}v}^{\dagger}, ... \right) \tag{5}
$$

where the $i$ and $j$ denotes the lattice point of PdCl₃ lattice in real space, $\mu$ and $v$ represents the Pd atom in $A$-th (First) and $B$-th (Second) sites, respectively.

![](./images/813000194755919873_6.jpg)

FIG. 4 (a) Spin-polarized band structures and spin-resolved local density of states (LDOS) (b) without SOC. The red and blue lines represent spin up and down channels, respectively. (c) Band structure with SOC. (d) 3D band profile around the Fermi level corresponding to Dirac point.

In the basis of $( d_{A,xz}, d_{A,yz}, d_{B,xz}, d_{B,yz}, )$ , we can define the TB Hamiltonian as $H = H_0 + H_{\text{soc}}$, which are given by

$$
\begin{aligned}
H_{SOC} = i\lambda \sum_{i} \Bigg[& \left( \text{d}_{xz,\vec{R}_i}^{\dagger} d_{yz,\vec{R}_i} - \text{d}_{yz,\vec{R}_i}^{\dagger} d_{xz,\vec{R}_i} \right) + \\
& \left( \text{d}_{xz,\vec{R}_i^{(B)}}^{\dagger} d_{yz,\vec{R}_i^{(B)}} - \text{d}_{yz,\vec{R}_i^{(B)}}^{\dagger} d_{xz,\vec{R}_i^{(B)}} \right) \Bigg]
\end{aligned} \tag{6}
$$

Here, the effect of SOC is a relativistic effect of the Schrödinger equation, which can significantly affect the electronic properties of PdCl₃ that turn it into a nontrivial phase. $\lambda$ represents the strength of SOC whose value depends on the type of atomic species. In this case, we obtain the Hamiltonian, $H(\vec{k}) =$

$$
\begin{pmatrix}
-\lambda & 0 & \frac{1}{2}t \sum_j b_j & \frac{1}{2}t \sum_j e^{-2i\theta_j} b_j \\
0 & \lambda & \frac{1}{2}t \sum_j e^{2i\theta_j} b_j & \frac{1}{2}t \sum_j b_j \\
\frac{1}{2}t \sum_j b_j^* & \frac{1}{2}t \sum_j e^{-2i\theta_j} b_j^* & -\lambda & 0 \\
\frac{1}{2}t \sum_j e^{2i\theta_j} b_j^* & \frac{1}{2}t \sum_j b_j^* & 0 & \lambda
\end{pmatrix} \tag{7}
$$

The diagonalization of Eq. (8) in reciprocal space for the band structure reveals rich underlying physics. When only the nearest-neighbor hopping is present, a linear Dirac point from $|d_{xz} >$ and $|d_{yz} >$ bands appears along the high symmetry line at K point without SOC. The flat bands and dispersive bands touch at the center of the first BZ, typical for a four-band model. However, if the next-nearest-neighbor hopping is present, the flat bands become anisotropic, while the Dirac band changes slightly, as illustrated in Fig. 5(a). Turning on SOC, $\lambda_{SO} \neq 0$, breaks $T$ and a sizable gap opens from band touching point. The obtained parameters $\lambda_{SO} = 6.0$ meV, which can fit very well with the DFT band structures. These also demonstrate that the intrinsic SOC in PdCl₃ lattice is responsible for gap opening at the Dirac bands, which is of importance to realize the QAHE.

## E. Berry curvature and Chern number
To determine the nontrivial band topology of PdCl₃, with help of the Kubo formula [56,57]
$$
\Omega(k) = \sum_n f_n \Omega_n(k) \tag{8}
$$

$$
\Omega_n(k) = -2\mathrm{Im} \sum_{m\neq n} \frac{\langle \Psi_{nk}|v_x|\Psi_{mk}\rangle\langle \Psi_{mk}|v_y|\Psi_{nk}\rangle\hbar^2}{(E_m - E_n)^2}, \tag{9}
$$
we calculate the Berry curvature $\Omega(k_x, k_y)$, where the summation is over all of the occupied states. Here, $E_n$ represents the eigenvalue of Bloch function $|\Psi_{nk} >$ and $f_n$ the Fermi-Dirac distribution function, while both the $v_x$ and $v_y$ are velocity operator in the $x$ and $y$ directions, defined as $v_x = \frac{1}{\hbar} \frac{\partial H}{\partial k_x}$ and $v_y = \frac{1}{\hbar} \frac{\partial H}{\partial k_y}$ . In terms of the TB Hamiltonian parameterization of Wannier functions [58,59], we obtain the Berry curvature for the whole valence bands along the high-symmetry directions in Fig. 5(b), in which the nonzero Berry curvatures are localized around $K$ and $K'$ points with the same sign.

Finally, by integrating the Berry curvatures over the first BZ, the Chern number ($C$), written by
$$
C = \frac{1}{2\pi} \sum_n \int_{BZ} d^2 k \Omega_n \tag{10}
$$
yields a nonzero -1 with each Dirac cone ($K$ and $K'$) contributing -0.5. In this case, the anomalous Hall conductivity $\sigma_{xy}$, $\sigma_{xy} = (e^2/h)C$, shows a quantized charge Hall plateau of at a value of $e^2/h$ located in the insulating gap of spin-up Dirac cone. It is known that, although the QAHE in magnetic doped topological insulators has been realized experimentally, the observation in a 2D system is rare. [9,10] Realization of QAHE on a 2D realistic crystal is of both scientific and practical interest.

![](./images/813000194755919873_7.jpg)

FIG. 5 (a) The TB band structure near the Fermi level obtained from TB model. (b) The Berry curvature with SOC in the momentum space. The red-white-blue color gives distribution of Berry curvature from positive to negative value in arbitrary unit, and the black dash lines show the first BZ. (c) The calculated chiral edge states of PdCl₃.

## F. Edge states of PdCl₃
Since the existence of chiral edge states is an important signature of 2D Chern insulaor ($C = 1$), we calculate the edge states of PdCl₃ by employing WANNIER90 package [58,59]. On the basis of a recursive strategy, we establish the maximally localized Wannier functions (MLWFs) [60] using $|d_{xz} >$ and $|d_{yz} >$ orbitals of Pd atom, and the LDOS of the edges from the Green's function are obtained in Fig. 5(c). One can see that the bulk states are connected by the topologically nontrivial states, which is a main feature of QAHE. In this respect, the PdCl₃ ribbon will carry quantized spin-up currents along the edges characterized by anomalous Hall conductance (AHC), together with current in the opposite spin direction in the interior region arising from the conducting band. These unique electron transport properties offer new opportunities for the design of spin filters and spintronics devices.

## G. Strain effect on electronic properties
After confirming the nontrivial topology of the PdCl₃, we further check the robustness of the topological properties against external strain, since the strain generally changes the SOC-induced bulk gap and spin exchange-coupling constant. Figure 6 plots the evolution of band gap $E_g$ and FM exchange energy with respect to strain $\varepsilon$, which is defined as $(a - a_0)/a_0$, where $a$ ($a_0$) is the strained (equilibrium) lattice constants. The nontrivial topological states are preserved within the strain range up to 11%, suggesting a favorable robustness against lattice stretch. The gap $E_g$ increases with the strain,

becoming 19.6 meV at the strain of 11.0 %. Unlike the significant strain effects on band gaps, strains trivially affect the $T_C$ of PdCl₃ with respect to tensile strain. The employment of 6% tensile strain changes the exchange-coupling slightly with the critical temperature around 303 K, which is still higher than room temperature. This strain effect provides a useful route to control the band gap and Curie temperature by design via epitaxy.

![](./images/813000194755919873_8.jpg)

FIG. 6 The calculated band gap $E_g$ and FM exchange energy as a function of the biaxial strain.

### H. Effect of Hubbard $U$ on topological properties

For an experimental observation of edge states, the size of topologically nontrivial bulk gap plays a crucial role. However, the gap size in PdCl₃ confines the prospective QAHE to low temperature and impedes its experimental observation. Interestingly, the *correlation* effect in $4d$ electrons of Pd ions is of importance for band gap opening. To obtain more accurate bulk gap, we thus perform $GGA+U$ calculations by varying Hubbard $U$, since the accurate value of $U$ has not been determined in PdCl₃. Due to the poor screening of Coulomb interaction in 2D crystals, it is expected that the Hubbard $U$ would be larger, thus its real band gap should be enhanced significantly. Figure 7 gives the size dependence of band gap $E_g$ on Harbbard $U$ value. Note that the QAHE remains up to $U = 4.0$ eV, for which a gap of $E_g = 68.6$ meV is obtained.

On the other hand, when the SOC is switched off, the system still keeps DHM feature even if considering the effect of Hubbard $U$. The band gap opening is a result of cooperative effect of electron correlation and SOC, which has also been observed in Sr₂IrO₄ and LaCoO₃ [21-24]. It is noticeable that, though the bulk gap is enhanced for Hubbard $U$, the $d_{xz}$ and $d_{yz}$ band character is not altered near the Fermi level, indicating the robustness of nontrivial topology against the *correlation* effect in $4d$ electrons of Pd ions.

![](./images/813000194755919873_9.jpg)

FIG. 7 The calculated band gap $E_g$ with respect to Hubbard $U$ value.

### I. Substrate effect on band structure

To show the practical applications in quantum devices, we explore the possibility of forming heterostructure on MoS₂ substrate, in that semiconductor substrates are inevitable experimentally. [61-65] In this work, we place 2D PdCl₃ on MoS₂ substrate to form a PdCl₃/MoS₂, as shown in Fig. 8(a). Structural optimizations suggest that the layered distance of PdCl₃ and MoS₂ is 3.87 Å with a weaker binding energy of -38 meV, suggesting a van der Waals interaction. In Figure 8(b) we display the band structure with considering the effect of SOC. Interestingly, a SOC induced nontrivial bulk gap at the Dirac point remains with states dominantly contributed by $|d_{xz}>$ and $|d_{yz}>$ states. Thus, the experimental observations of parallel chiral edge channels from being gapped by interlayer hybridization can be realized and, further, PdCl₃/MoS₂ heterostructure enhances greatly the number of edge transport channels to support the low power consumption transport properties in 2D materials, as illustrated in model quantum device constructed with PdCl₃/MoS₂ heterostructure in Fig. 8(c).

### IV. CONCLUSIONS

In conclusion, we demonstrate the possibility of realizing intrinsic QAHE in 2D hexagonal PdCl₃, which is bought about by the combination of the strong SOC and FM order of magnetic moments. We show that 2D PdCl₃ is mechanically and dynamically stable. We further reveal that the PdCl₃ shows a higher Curie temperature $T_C = 528$ K than the remaining members of 2D materials which is derived from the increased superexchange coupling between Pd atoms due to the relatively enhanced iconicity in Pd and Cl bonds. Also, the nontrivial properties in Dirac bands are confirmed by a nonzero Chern number ($C = -1$), quantized Hall conductivity, and gapless chiral edge states. A TB model is constructed to explain the origin of

nontrivial topology. Benefited from the high Curie temperature and large topological gap, the predicted QAHE is expected to work safely above the room temperature and thus enabling PdCl₃ more promising platform for the realizing low-dissipation topotronics devices.

![](./images/813000194755919873_10.jpg)

FIG. 8 (a) Top and side view of the epitaxial growth of the PdCl₃ lattice on MoS₂ substrate. (b) The corresponding energy band structure with SOC, where a sizable band gap is obtained. (c) Schematic device model for proposed PdCl₃/MoS₂ heterostructure for quantum state measurement. Vertical arrows show the spin orientation of electrons in the edge states and horizontal arrows show their transport directions.

## ACKNOWLEDGMENTS
This work was supported by National Natural Science Foundation of Shandong province (Grant No. ZR2018MA033).

[1] H. J. Zhang, J. Wang, G. Xu, Y. Xu, and S. C. Zhang, Phys. Rev. Lett. 112, 096804 (2014).

[2] J. G. Checkelsky, R. Yoshimi, A. Tsukazaki, K. S. Takahashi, Y. Kozuka, J. Falson, M. Kawasaki, and Y. Tokura, Nat. Phys. 10, 731 (2014).

[3] J. Wu, J. Liu, and X. J. Liu, Phys. Rev. Lett. 113, 136403 (2014).

[4] Z. Qiao, W. Ren, H. Chen, L. Bellaiche, Z. Zhang, A. H. MacDonald, and Q. Niu, Phys. Rev. Lett. 112, 116404 (2014).

[5] M. Onoda and N. Nagaosa, Phys. Rev. Lett., 90, 206601 (2013).

[6] Y. P. Wang, W. X. Ji, C. W. Zhang, P. Li, S. F. Zhang, P. J. Wang, S. S. Li and S. S. Yan, Appl. Phys. Lett. 110 213101(2017).

[7] W. Luo, and H. J. Xiang, Nano Lett. 15, 3230 (2015).

[8] S. S. Li, W.X. Ji, S. J. Hu, C. W. Zhang, and S. S. Yan, ACS Appl. Mater. Inter. 9 41443 (2017).

[9] H. Zhao, C. W. Zhang, W. X. Ji, R. W. Zhang, S. S. Li, S. S. Yan, B. M. Zhang, P. Li, and P. J. Wang, Sci. Rep. 6 20152 (2016).

[10] C. Z. Chang, J. Zhang, X. Feng, J. Shen, Z. Zhang, M. Guo, K. Li, Y. Ou, P. Wei, L. L. Wang, Z. Q. Ji, Y. Feng, S. Ji, X. Chen, J. Jia, X. Dai, Z. Fang, S.C. Zhang, K. He, Y. Wang, L. Lu, X.C. Ma, and Q. K. Xue, Science 340, 167 (2013).

[11] X. Kou, S.T. Guo, Y. Fan, L. Pan, M. Lang, Y. Jiang, Q. Shao, T. Nie, K. Murata, J. Tang, Y. Wang, L. He, T. K. Lee, W. L. Lee, and K. L. Wang, Phys. Rev. Lett. 113, 137201 (2014).

[12] J. Zhang, B. Zhao, Y. Yao, and Z. Yang, Phys. Rev. B 92, 165418 (2015).

[13] C. X. Liu, S.C. Zhang, and X. L. Qi, Annu. Rev. Condens. Matter Phys. 7, 301 (2016).

[14] F. D. M. Haldane, Phys. Rev. Lett. 61, 2015 (1988).

[15] S. C. Wu, G. Shan, and B. Yan, Phys. Rev. Lett. 113, 256401 (2014).

[16] D. Xiao, W. Zhu, Y. Ran, N. Nagaosa, and S. Okamoto, Nat. Commun. 2, 596 (2011).

[17] H. Zhang, C. Lazo, S. Blügel, S. Heinze, and Y. Mokrousov, Phys. Rev. Lett. 108, 056802 (2012).

[18] Z. Wang, C. Tang, R. Sachs, Y. Barlas, and J. Shi, Phys. Rev. Lett. 114, 016603 (2015).

[19] X. L. Zhang, L. F. Liu, and W. M. Liu, Sci. Rep. 3, 2908 (2013).

[20] Y. P. Wang, W.X. Ji, C. W. Zhang, P. Li, F. Li, P. J. Wang, S. S. Li, and S. S. Yan, Appl. Phys. Lett., 108, 073104 (2016).

[21] K. Y. Yang, W. Zhu, D. Xiao, S. Okamoto, Z. Wang, and Y. Ran, Phys. Rev. B 84, 201104 (2011).

[22] A. R"uegg, C. Mitra, A. A. Demkov, andG. A. Fiete, Phys. Rev. B 85, 245131 (2012).

[23] A. R"uegg, C. Mitra, A. A. Demkov, andG. A. Fiete, Phys. Rev. B 88, 115146 (2013).

[24] S. Okamoto, W. Zhu, Y. Nomura, R. Arita, D. Xiao, and N. Nagaosa, Phys. Rev. B 89, 195121 (2014).

[25] X. Hu, A. R"uegg, and G. A. Fiete, Phys. Rev. B 86, 235141 (2012).

[26] M. Kargarian and G. A. Fiete, Phys. Rev. Lett. 110, 156403 (2013).

[27] Q. Chen, H.-H. Hung, X. Hu, and G. A. Fiete, Phys. Rev. B 92, 085145 (2015).

[28] Y. P. Wang, W. X. Ji, C. W. Zhang, P. Li, P. J. Wang, B. Kong, S. S. Li, S. S. Yan, and K. Liang , Appl. Phys. Lett. 110, 233107 (2017).

[29] Z. F. Wang, Z. Liu, and F. Liu, Phys. Rev. Lett. 110, 196801 (2013).

[30] S. J. Zhang, C. W. Zhang , S. F. Zhang, W. X. Ji, P. Li, P. J. Wang, S. S. Li, and S. S. Yan, Phys. Rev. B 96 205433 (2017).

[31] Z. Liu, J. Liu, and J. Zhao, Nano Res. 10, 1972 (2017).

[32] X. Zhang, A. Wang, and M. Zhao, Carbon 84, 1 (2015).

[33] J. He, S. Ma, P. Lyu, and P. Nachtigall, J. Mater. Chem. **C 4**, 2518 (2016).

[34] S. Zhang, and B. Liu, arXiv:1706.08943v2 (2017).

[35] J. He, X. Li, P. Lyu and P. Nachtigall, Nanoscale **9**, 2246 (2017).

[36] H. Bengel, H.-J. Cantow, S. N. Maganov, H. Hillebrecht, G. Thiele, W. Liang, and M.-H. Whangbo, Surf. Sci. **343**, 95 (1995).

[37] Nicolosi, V., Chhowalla, M., Kanatzidis, M. G., Strano, M. S. & Coleman, J. N., Science **340**, 1226419 (2013).

[38] M. Ziatdinov, A. Banerjee, A. Maksov, T. Berlijn, W. Zhou, H.B. Cao, J. Q. Yan, C.A. Bridges, D.G. Mandrus, S.E. Nagler, A.P. Baddor, S.V. Kalinin, Nat. Comm. **7**, 13774 (2016).

[39] J. B. Goodenough, Phys. Rev. **100**, 564 (1955).

[40] J. Kanamori, J. Appl. Phys. **31**, S14 (1960).

[41] P. W. Anderson, Phys. Rev. **115**, 2 (1959).

[42] G. Kresse, and J. Furthmüller, Phys. Rev. B **54**, 11169 (1996).

[43] P. E. Blöchl, Phys. Rev. B **50**, 17953 (1994).

[44] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

[45] J. Paier, M. Marsman, K. Hummer, G. Kresse, I. C. Gerber, and J. G. Ángyán. J. Chem. Phys. **124**, 154709 (2006).

[46] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Phys. Rev. B **57**, 1505 (1998).

[47] A. Togo, F. Oba, and I. Tanaka, Phys. Rev. B **78**, 134106 (2008).

[48] R. C. Andrew, R. E. Mapasha, A. M. Ukpong, and N. Chetty, Phys. Rev. B **85**, 125428 (2012).

[49] B. J. Kim, H. Jin, S. J. Moon, J. Y. Kim, B. G. Park, C. S. Leem, J. Yu, T. W. Noh, C. Kim, S. J. Oh, J. H. Park, V. Durairaj, G. Cao, and E. Rotenberg, Phys. Rev. Lett. **101**, 076402 (2008).

[50] W. Ju, G. Liu, and Z. Yang, Phys. Rev. B **87**, 075112 (2013).

[51] W. Heitler and F. London, Z. Phys. **44**, 455 (1927).

[52] X. L. Wang, Phys. Rev. Lett. **100**, 156404 (2008).

[53] C. C. Liu, W. X. Feng, and Y. G. Yao, Phys. Rev. Lett. **107**, 076802 (2011).

[54] R. W. Zhang, C. W. Zhang, W. X. Ji, S. S. Li, S. J. Hu, S. S. Yan, P. Li, P. J. Wang, and F. Li, New J. Phys. **17**, 083036 (2015).

[55] Y. Xu, B. Yan, H. Zhang, J. Wang, G. Xu, P. Tang, W. Duan, and S. Zhang, Phys. Rev. Lett. **111**, 136804 (2013).

[56] Y. G. Yao, L. Kleinman, A. H. MacDonald, J. Sinova, T. Jungwirth, D. S. Wang, E. Wang, and Q. Niu, Phys. Rev. Lett. **92**, 037204 (2004).

[57] Y. G. Yao, and Z. Fang, Phys. Rev. Lett. **95**, 156601 (2005).

[58] Y. Guo, Y. F. Zhang, X. Y. Bao, T. Z. Han, Z. Tang, L. X. Zhang, W. G. Zhu, E. G. Wang, Q. Niu, Z. Q. Qiu, J. F. Jia, Z. X. Zhao, and Q. K. Xue, Science **306**, 1915 (2004).

[59] L. Ju, J. Velasco Jr, E. Huang, S. Kahn, C. Nosiglia, H.Z. Tsai, W. Yang, T. Taniguchi, K. Watanabe, Y. Zhang, G. Zhang, M. Crommie, A. Zettl, and F. Wang, Nat. Nanotechnol. **9**, 348 (2014).

[60] M. P. L.Sancho, J. M. L. Sancho, and J. Rubio, J. Phys. F: Met. Phys. **15**, 851 (1985).

[61] L. Li and M. W. Zhao, J. Phys. Chem. C **118**, 19129 (2014).

[62] R. W. Zhang, C. W. Zhang, W. X. Ji, S. S. Yan and Y. G. Yao, Nanoscale, 9, 8207 (2017).

[63] S. S. Li, W. X. Ji, P. Li, S. J. Hu, L. Cai, C. W. Zhang, and S. S. Yan, ACS Appl. Inter., 9, 21515 (2017).

[64] T. Hirahara, G. Bihlmayer, Y. Sakamoto, M. Yamada, H. Miyazaki, S. Kimura, S. Blugel, S. Hasegawa, Phys. Rev. Lett. **107**, 166801 (2011).

[65] R. W. Zhang, C. W. Zhang, W. X. Ji, P. Li, P. J. Wang, S. S. Li, and S. S. Yan, Appl. Phys. Lett., 109, 182109 (2016).