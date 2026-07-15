# First-principles study of magnetization reorientation and large perpendicular magnetic anisotropy in $CuFe_2O_4$/MgO heterostructures

D. Odkhuu, $^{1}$ T. Tsevelmaa, $^{2}$ D. Sangaa, $^{3}$ N. Tsogbadrakh, $^{4}$ S. H. Rhim, $^{2}$ and S. C. Hong $^{2}$

$^{1}$ Department of Physics, Incheon National University, Incheon 22012, South Korea
$^{2}$ Department of Physics and EHSRC, University of Ulsan, Ulsan 44610, South Korea
$^{3}$ Institute of Physics and Technology, Mongolian Academy of Sciences, Ulaanbaatar 13330, Mongolia
$^{4}$ Department of Physics, National University of Mongolia, Ulaanbaatar 14201, Mongolia

![](./images/817403427473588225_1.jpg)
(Received 20 March 2018; revised manuscript received 5 July 2018; published 10 September 2018)

Herein, using first-principles calculations we predict magnetization reorientation and large perpendicular magnetic anisotropy (PMA) in spinel $Fe_3O_4$/MgO heterostructure by replacing the octahedral Fe ions with Cu. The substitutional $Cu^{2+}$ ions prefer the octahedral site within the $xy$-plane layer in an inverse spinel structure, which is associated with the Jahn-Teller tetragonal and $xy$-plane twisted distortions. While magnetization of $Fe_3O_4$/MgO is significantly reduced in $CuFe_2O_4$/MgO, the presence of the substitutional $Cu^{2+}$ ions reorients magnetization PMA from an in-plane to perpendicular magnetic anisotropy. More remarkably, PMA further increases gradually with the film thickness of $CuFe_2O_4$ layers in the $CuFe_2O_4$/MgO heterostructure. The underlying mechanism for this large PMA is the interplay of the spin-orbit-coupled Cu $d_{xy}$-$d_{x^2-y^2}$ states in the center layers and the Fe $d_{z^2}$-$O$ $p_z$ hybridization at the interface. These findings point toward the feasibility of reducing magnetization and enhancing PMA in spinel structures for spintronics applications.

DOI: 10.1103/PhysRevB.98.094408

## I. INTRODUCTION

Epitaxial growth of ferromagnetic (FM) materials on insulating MgO has been of interest for spintronics applications such as spin-transfer torque and magnetoelectric memory devices owing to their large magnetoresistance and perpendicular magnetic anisotropy (PMA) [1]. Nevertheless, there are still intense research efforts to reduce the critical current density $I_c$ required for magnetization switching of a free FM layer in magnetic tunnel junctions (MTJs) while retaining thermal stability $\Delta$. $\Delta$ is maintained by the large PMA according to $\Delta = KV/k_BT$, where $K$, $V$, $k_B$, and $T$ are anisotropy, volume, Boltzmann's constant, and temperature, respectively [2]. On the other hand, low saturation magnetization $M_s$ favors the reduction of $I_c$ through $I_c = \frac{2e}{\hbar}\frac{\alpha}{\eta}M_sV(H_k + 2\pi M_s)$, where $\alpha$, $\eta$, and $H_k$ represent the Gilbert damping coefficient, spin polarization factor, and Stoner-Wolfarth switching field, respectively [3]. Most materials proposed for memory applications are soft magnets, i.e., $H_k \ll M_s$; thus, $I_c \sim M_s^2V$. The utilization of low-magnetization materials [i.e., ferrimagnetic (FIM) and antiferromagnetic materials] rather than FM materials, preferably with the large PMA, in MTJs could thus provide an alternative way to minimize $I_c$ and maximize $\Delta$ at the same time [4,5] and also reduce stray fields in real devices [6,7].

Owing to these prerequisites, spinel magnetite ($Fe_3O_4$) and its doped alloys ($MFe_2O_4$, where $M$ represents a metallic element) have been recently regarded as promising candidate materials for spintronics applications [8-14]. $Fe_3O_4$ has a FIM ground state with antiparallel spin orientation on tetrahedral to octahedral sites and undergoes a first-order metal-to-insulator Verwey transition at $T_V \sim 120$ K, which is mostly attributed to the long-range charge ordering of $Fe^{2+}$ and $Fe^{3+}$ ions on octahedral sites [15]. Remarkably, in both experimental and theoretical studies, the substitution of $M$ ($M =$ Co, Ni, Mn, or Cu) atoms for the Fe sites has been shown to improve and modify dramatically the magnetic and electronic properties of $Fe_3O_4$ [16-21]. In particular, copper ferrite ($CuFe_2O_4$) exhibits intriguing physical properties [22-27], including a phase transition from tetragonal to cubic upon temperature [28,29], which depends on the degree of inversion parameter $x$ in the stoichiometric formula $(Cu_x^{2+}Fe_{1-x}^{3+})_A(Cu_{1-x}^{2+}Fe_{1+x}^{3+})_BO_4$, where A and B denote the tetrahedral and octahedral sites, respectively. The inversion parameter is equal to zero for the inverse spinel structure, and $x = 1$ when the spinel is normal. The degree of inversion changes during the cubic-to-tetragonal transition, where the redistribution of Cu atoms from A to B sites alters the ground multiplet from triplet to doublet and thus alters magnetic properties [30,31]. Nevertheless, experiments revealed that the $Cu^{2+}$ ions occupy the octahedral sites of the spinel lattice, leading to a structural formula close to $(Fe^{3+})_A(Cu^{2+}Fe^{3+})_BO_4$ and a Jahn-Teller distortion $(c/a > 1)$ [25-27]. In addition to these intriguing phenomena, the renewed interest in research targets seemingly resides in the possible PMA, a preferable magnetization direction normal to the film plane, and its tunability by the B-site $M$ substitution in $Fe_3O_4$, which remains unexplored.

In this paper, we predict the magnetization reorientation and large enhancement of PMA in $Fe_3O_4$/MgO(001) films by replacing the octahedral Fe with Cu. Using on-site correction for Coulomb interaction in density functional theory (DFT+$U$) calculations, the ground states of the structural and magnetic structures are first determined for bulk $CuFe_2O_4$ in both normal and inverse spinel structures. It is found that the substitutional $Cu^{2+}$ ions prefer the octahedral site within

the $xy$-plane layer in an inverse spinel structure. While the total magnetization of $\text{Fe}_3\text{O}_4$/MgO decreases significantly in $\text{CuFe}_2\text{O}_4$/MgO, the presence of the substitutional $\text{Cu}^{2+}$ ions leads to the magnetization reorientation from an in-plane to perpendicular magnetic anisotropy. More interestingly, PMA further increases gradually with the film thickness of $\text{CuFe}_2\text{O}_4$ layers in the $\text{CuFe}_2\text{O}_4$/MgO heterostructure. We attribute this large PMA to the spin-orbit-coupled Cu $d$ states in the Jahn-Teller distorted and in-plane twisted lattice in the center layers and the Fe $d$--O $p$ hybridization at the interface.

## II. COMPUTATIONAL METHOD

The DFT calculations were performed using the projector augmented-wave (PAW) pseudopotential method [32] as implemented in the Vienna Ab initio Simulation Package (VASP) [33,34]. The exchange and correlation interactions between electrons were described with the generalized gradient approximation (GGA) formulated by Perdew, Burke, and Ernzerhof (PBE) [35]. Previous first-principles studies [36–39] showed that the Hubbard $U$ in GGA ($\text{GGA}+U$) [40] approach explicitly describes the formation of charge ordering and experimentally observed band gap (0.14 eV) of $\text{Fe}_3\text{O}_4$, whereas the conventional DFT calculations yield a metallic solution without charge ordering [41,42]. We thus apply on-site $U_{\text{eff}}$ ($U$-$J$) parameters of 3.5 eV for Fe and 4.0 eV for the Cu site of $\text{Fe}_3\text{O}_4$ and $\text{CuFe}_2\text{O}_4$ [39]. An energy cutoff of 500 eV and $8\times8\times8$, $5\times5\times2$, and $5\times5\times1$ Brillouin zone $k$-point meshes were used to relax the lattice and ionic coordinates of bulk, superlattice, and film structures until the largest force becomes less than $10^{-2}$ eV/Å and the change in the total energy between two ionic relaxation steps is smaller than $10^{-5}$ eV, respectively. The magnetic anisotropy energy (MAE) is obtained based on the total energy difference when the magnetization directions are in the $xy$ plane ($E^\parallel$) and along the $z$ axis ($E^\perp$), $\text{MAE}=E^\parallel-E^\perp$. To obtain a reliable value for MAE, the Gaussian smearing method with a smaller smearing of 0.05 and dense $k$ points of $11\times11\times11$, $9\times9\times4$, and $9\times9\times1$ were used in noncollinear calculations for bulk, superlattice, and film structures, respectively, where the spin-orbit coupling (SOC) term was included using the second-variation method employing the scalar-relativistic eigenfunctions of the valence states [43].

## III. RESULTS AND DISCUSSION

Both $\text{Fe}_3\text{O}_4$ and $\text{CuFe}_2\text{O}_4$ have an inverse spinel structure of the fcc lattice with a space group of $Fd3m$, as shown in Fig. 1(a). The tetrahedral A sites are occupied by the eight $\text{Fe}^{3+}$ ions (denoted $\text{Fe}_A{}^{3+}$, shown by the blue tetrahedron), and the octahedral B sites are occupied by the same number of $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ ions (denoted $\text{Fe}_B{}^{2+}$ and $\text{Fe}_B{}^{3+}$, shown by the gray octahedron). For $\text{CuFe}_2\text{O}_4$, four distinctive configurations of Cu substitutional atoms for the eight octahedral B sites have been considered, which we denote types I, II, III, and IV, as schematically illustrated in Fig. 1(b), where only the octahedral Fe and Cu sites in four simple-cubic sublattices with neighboring O atoms are shown for simplicity.

![](./images/817403427473588225_2.jpg)

FIG. 1. (a) Inverse spinel structure of $\text{Fe}_3\text{O}_4$. The gray octahedron and blue tetrahedron geometries represent the octahedral $\text{Fe}^{3+}$/$\text{Fe}^{2+}$ and tetrahedral $\text{Fe}^{3+}$ sites, respectively. Oxygen atoms sitting at the corners of the octahedron and tetrahedron are not shown for simplicity. (b) Schematics for the different configurations of the substitutional Cu atoms on the octahedral sites: types I, II, III, and IV. The larger gray and pink and smaller red spheres are $\text{Fe}^{3+}$ and $\text{Cu}^{2+}$ and O atoms, respectively. The tetrahedral $\text{Fe}^{3+}$ ions are not shown for simplicity.

Optimized structural parameters $a$ ($xy$-plane lattice) and the $c/a$ ratio and the relative energy $\Delta E$ are listed in Table I for the different substitutional configurations of $\text{CuFe}_2\text{O}_4$ with respect to type II. Our total energy calculations show that type II is the ground-state structure as $\Delta E=0$ (and thus is the reference energy). For better comparison, the results for $\text{CuFe}_2\text{O}_4$ in the normal spinel and $\text{Fe}_3\text{O}_4$ in the inverse spinel structure are also shown in Table I. The presence of the substitutional $\text{Cu}_B{}^{2+}$ ions reduces the $xy$-plane lattice and elongates along the $z$ axis except for type IV. In particular, the largest reduction (enhancement) in $a$ ($c/a$) occurs for the most stable type-II structure, leading to the Jahn-Teller distortion with $c/a>1$. It is also found that the octahedral sublattices, particularly $\text{Cu}_B{}^{2+}$-centered octahedrons, are severely twisted within the $xy$ plane. Overall, our calculated structural parameters ($a=8.25$ Å and $c/a=1.077$) of the type-II structure agree well with the experimental values of $a=8.23$ Å and $c/a=1.06$ [44]. This structure (type II) is

<table>
<caption>TABLE I. Optimized $xy$-plane lattice $a$ (Å) and $c/a$ ratio, the relative energy $\Delta E$ (eV/f.u.) with respect to type II, the spin magnetic moments $\mu^X$ (in units of $\mu_B$) of the octahedral $\text{Fe}_B{}^{3+}$ and $\text{Cu}_B{}^{2+}$ and tetrahedral $\text{Fe}_A{}^{3+}$ ions, and the total magnetization per formula unit $\mu^{\text{Total}}$ ($\mu_B$/f.u.) for the type-I, -II, -III, and -IV configurations of bulk $\text{CuFe}_2\text{O}_4$. The corresponding results for the normal spinel structure of $\text{CuFe}_2\text{O}_4$ and inverse spinel structure of $\text{Fe}_3\text{O}_4$ are also shown for comparison.</caption>
<tbody>
  <tr>
    <td></td>
    <td>$a$</td>
    <td>$c/a$</td>
    <td>$\Delta E$</td>
    <td>$\mu^{Fe_A^{3+}}$</td>
    <td>$\mu^{Fe_B^{3+}}$</td>
    <td>$\mu^{Cu_B^{2+}}$</td>
    <td>$\mu^{\text{Total}}$</td>
  </tr>
  <tr>
    <td>Type I</td>
    <td>8.258</td>
    <td>1.074</td>
    <td>0.03</td>
    <td>$-4.04$</td>
    <td>4.15</td>
    <td>0.63</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Type II</td>
    <td>8.250</td>
    <td>1.077</td>
    <td>0.00</td>
    <td>$-4.04$</td>
    <td>4.16</td>
    <td>0.63</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Type III</td>
    <td>8.265</td>
    <td>1.070</td>
    <td>0.05</td>
    <td>$-4.04$</td>
    <td>4.15</td>
    <td>0.63</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Type IV</td>
    <td>8.560</td>
    <td>0.957</td>
    <td>0.14</td>
    <td>$-4.02$</td>
    <td>4.12</td>
    <td>0.62</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Normal</td>
    <td>8.465</td>
    <td>1.000</td>
    <td>0.61</td>
    <td>$-0.31$/$\text{Cu}^{3+}$</td>
    <td>4.14</td>
    <td>4.14/$\text{Fe}^{2+}$</td>
    <td>9</td>
  </tr>
  <tr>
    <td>$\text{Fe}_3\text{O}_4$</td>
    <td>8.495</td>
    <td>1.000</td>
    <td></td>
    <td>$-4.05$</td>
    <td>4.15</td>
    <td>3.66/$\text{Fe}^{2+}$</td>
    <td>4</td>
  </tr>
</tbody>
</table>

energetically favored over type-I, -III, and -IV configurations by $\Delta E = 0.03$, $0.05$, and $0.14$ eV/f.u., respectively. These small energy differences suggest that the Cu-substitutional configurations of the type-I–III structures may coexist in a real sample with a rather complex pattern. On the other hand, the normal spinel structure of ${\text{CuFe}}_{2}{\text{O}}_{4}$ has a large value of $\Delta E$ of $0.61$ eV/f.u., which indicates that the substitutional Cu atoms always prefer the octahedral site rather than the tetrahedral site. This is in agreement with experiments, where ${\text{CuFe}}_{2}{\text{O}}_{4}$ has a nearly complete inverse spinel structure and the $c/a$ ratio depends on the ${\text{Cu}}^{2+}$ distribution but is always greater than unity [30].

In Table I we show the local spin magnetic moments $\mu^{X}$ ($X = {\text{Fe}}_{A}^{3+}$, ${\text{Fe}}_{B}^{3+}$, and ${\text{Cu}}_{B}^{2+}$) of the tetrahedral and octahedral ions for the inverse spinel type-I–IV and normal spinel structures of ${\text{CuFe}}_{2}{\text{O}}_{4}$. It is found that for ${\text{Fe}}_{3}{\text{O}}_{4}$ the magnetic moments of ${\text{Fe}}_{A}^{3+}$ and ${\text{Fe}}_{B}^{3+}$ ions are $-4.05{\mu}_{B}$ and $4.15{\mu}_{B}$, respectively, and are almost retained in the favorable type-I–III phases of ${\text{CuFe}}_{2}{\text{O}}_{4}$. Furthermore, the ${\text{Cu}}_{B}^{2+}$ ions have similar induced moments of $\sim 0.63{\mu}_{B}$, in agreement with previous *ab initio* calculations [45], regardless of the Cu sites. Thus, the total magnetization is $1{\mu}_{B}$/f.u. for all type-I–IV structures. On the other hand, the normal spin structure shows a large magnetization of $9{\mu}_{B}$/f.u., where the negative magnetic moment of A site of ${\text{Fe}}_{3}{\text{O}}_{4}$ is suppressed with the occupation of the Cu atoms at the tetrahedral site.

Figures 2(a)–2(c) show the $d$-orbital projected density of states (PDOS) of the ${\text{Fe}}_{A}^{3+}$, ${\text{Fe}}_{B}^{3+}$, and ${\text{Cu}}_{B}^{2+}$ ions for the most stable type-II structure of ${\text{CuFe}}_{2}{\text{O}}_{4}$, respectively. The minority-spin PDOS of the ${\text{Fe}}_{A}^{3+}$ cation is fully occupied, while the majority-spin state is mainly localized at around $2$ eV in the unoccupied state. This is reversed for the case of ${\text{Fe}}_{B}^{3+}$ because of its antiparallel spin alignment to ${\text{Fe}}_{A}^{3+}$. Both the ${\text{Fe}}_{A}^{3+}$ and ${\text{Fe}}_{B}^{3+}$ ions have a large exchange splitting between the spin subbands of the majority-spin and minority-spin states, leading to the significant magnetic moments shown in Table I. The degeneracy of the spin subbands in the occupied region is not significant for the ${\text{Cu}}_{B}^{2+}$ site. The shift of the majority-spin Cu $3d$-orbital states toward the Fermi level reduces the spin-exchange splitting with respect to the Fe ions. Thus, the occupied and unoccupied states near the Fermi level are contributed by both the Fe and Cu $d$-orbital states. Furthermore, the inverse spinel ${\text{CuFe}}_{2}{\text{O}}_{4}$ has a spin-polarized semiconducting behavior with a band gap of $\sim 1.15$ eV, which virtually agrees with previous theoretical values [45].

![](./images/817403427473588225_3.jpg)

FIG. 2. Spin- and $d$-orbital-resolved PDOS of the (a) ${\text{Fe}}_{A}^{3+}$, (b) ${\text{Fe}}_{B}^{3+}$, and (c) ${\text{Cu}}_{B}^{2+}$ ions for the type-II structure of bulk ${\text{CuFe}}_{2}{\text{O}}_{4}$. The letters A and B in parentheses represent the octahedral and tetrahedral sites, respectively. The dashed black and orange and solid red and blue lines denote the ${d}_{xy}$, ${d}_{xz,yz}$, ${d}_{x^{2}}$, and ${d}_{x^{2}-y^{2}}$ orbital states, respectively. The Fermi level is set to zero in energy.

We next perform our calculations for ${\text{CuFe}}_{2}{\text{O}}_{4}$ films in contact with MgO. In a realistic situation, stacking a magnetic memory junction in spintronic devices necessarily involves making contacts with an insulating barrier. Thin MgO(001) layers have been used as a barrier between epitaxial magnetic layers in most experimental studies undertaken thus far [1]. With this in mind, we modeled the superlattice structures composed of the repetitive one-unit-cell [nine atomic layers (ALs)] or two-unit-cell layers (17 ALs) of the most stable type-II ${\text{CuFe}}_{2}{\text{O}}_{4}$(001) and five ALs of MgO(001). As shown in Figs. 3(a) and 3(b) for the case of the one-unit-cell superlattice, two possible interface terminations, namely, FeO and CuO interfaces, have been taken into account, respectively. At both interfaces, the octahedral B-site ${\text{Cu}}_{B}^{2+}$ and ${\text{Fe}}_{B}^{3+}$ ions placed atop of O atoms of MgO are found to have the lowest energy among several different configurations considered in the present study, including the tetrahedral ${\text{Fe}}_{A}^{3+}$ termination, analogous to the Fe/MgO-based interfaces [4,46,47]. For reference, we have also performed the same calculations for the one-unit-cell and two-unit-cell ${\text{Fe}}_{3}{\text{O}}_{4}$/MgO superlattices.

The optimized in-plane lattice constant $a$, the formation energy $H_{f}$, and the total magnetization are shown in Table II for the CuO- and FeO-interface terminations of the one-unit-cell ${\text{CuFe}}_{2}{\text{O}}_{4}$/MgO superlattice. Here, $H_{f} = \left(E_{\text{tot}}^{{\text{CuFe}}_{2}{\text{O}}_{4}/{\text{MgO}}} - E_{\text{tot}}^{{\text{CuFe}}_{2}{\text{O}}_{4}} - E_{\text{tot}}^{{\text{MgO}}}\right)/N$, where $E_{\text{tot}}^{{\text{CuFe}}_{2}{\text{O}}_{4}/{\text{MgO}}}$, $E_{\text{tot}}^{{\text{CuFe}}_{2}{\text{O}}_{4}}$, and $E_{\text{tot}}^{{\text{MgO}}}$ are the total energies of ${\text{CuFe}}_{2}{\text{O}}_{4}$/MgO, ${\text{CuFe}}_{2}{\text{O}}_{4}$, and MgO, respectively, and $N$ is the number of interfacial ions in the ${\text{CuFe}}_{2}{\text{O}}_{4}$ layers. The calculated values of $H_{f}$ are $-1.76$ and $-1.84$ eV/interface-ion for the CuO- and FeO-interface terminations, respectively. This indicates that the FeO-interface termination is more favorable than the CuO interface with MgO. Both the ${\text{CuFe}}_{2}{\text{O}}_{4}$/MgO structures

### (a) FeO-interface termination

![](./images/817403427473588225_4.jpg)

### (b) CuO-interface termination

![](./images/817403427473588225_5.jpg)

FIG. 3. Side views of the optimized atomic structure for the (a) FeO- and (b) CuO-interface-terminated one-unit-cell CuFe₂O₄/MgO superlattice. The larger gray, pink, and orange and smaller red spheres are Fe³⁺, Cu²⁺, Mg, and O atoms, respectively. The down arrows indicate the interface plane of CuFe₂O₄ layers next to MgO.

exhibit smaller in-plane lattices (8.144 Å for the CuO-interface termination and 8.368 Å for the FeO-interface termination) and magnetization (2.14$\mu_B$ and 2.57$\mu_B$) compared with the Fe₃O₄/MgO superlattice (8.496 Å and 6.0$\mu_B$). This reduced in-plane lattice is in similar phenomena, associated with the Jahn-Teller distortion, found in bulk structures (Table I). In particular, the former interface termination has an even smaller in-plane lattice and magnetization than the latter, owing to the larger number of Cu ions in the CuO-interface-terminated structure. Furthermore, for both Fe₃O₄/MgO and CuFe₂O₄/MgO superlattices the total magnetization decreases as the number of layers increases from one unit cell to two unit cells and tends to reach their bulk values of $4\mu_B$/f.u. for Fe₃O₄ and $1\mu_B$/f.u. for CuFe₂O₄. The larger magnetization at the thinner films is due to the dominant number $N$ of $\text{Fe}_B{}^{3+}$ ions compared to that of the $\text{Fe}_A{}^{3+}$ ions in the unit cell. For CuFe₂O₄/MgO (Fe₃O₄/MgO), $N(\text{Fe}_B{}^{3+})/N(\text{Fe}_A{}^{3+})=1.5$ (2.5) for the one-unit-cell thickness and 1.25 (2.25) for the two-unit-cell thickness, which in bulk is 1 (2).

<table>
<caption>TABLE II. Optimized $xy$-plane lattice $a$ (Å), the formation energy $H_f$ (eV/interface ion), the total magnetization per formula unit $\mu^{\text{Total}}$ ($\mu_B$/f.u.), and MAE (meV/f.u.) for the CuO- (CuO-int.) and FeO-interface- (FeO-int.) terminated one-unit-cell CuFe₂O₄/MgO superlattice. The corresponding results for the stable FeO-interface-terminated two-unit-cell CuFe₂O₄/MgO and one-unit-cell and two-unit-cell Fe₃O₄/MgO superlattices are also listed.</caption>
<thead>
<tr>
<th>
</th>
<th>
$a$
</th>
<th>
$H_f$
</th>
<th>
$\mu^{\text{Total}}$
</th>
<th>
MAE
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
One-unit-cell CuO-int./MgO
</td>
<td>
8.144
</td>
<td>
$-$1.76
</td>
<td>
2.14
</td>
<td>
0.05
</td>
</tr>
<tr>
<td>
One-unit-cell FeO-int./MgO
</td>
<td>
8.368
</td>
<td>
$-$1.84
</td>
<td>
2.57
</td>
<td>
0.32
</td>
</tr>
<tr>
<td>
Two-unit-cell FeO-int./MgO
</td>
<td>
8.332
</td>
<td>
$-$2.02
</td>
<td>
1.84
</td>
<td>
0.24
</td>
</tr>
<tr>
<td>
One-unit-cell Fe₃O₄/MgO
</td>
<td>
8.496
</td>
<td>
$-$2.13
</td>
<td>
6.00
</td>
<td>
0.23
</td>
</tr>
<tr>
<td>
Two-unit-cell Fe₃O₄/MgO
</td>
<td>
8.496
</td>
<td>
$-$2.28
</td>
<td>
5.08
</td>
<td>
$-$0.14
</td>
</tr>
</tbody>
</table>

![](./images/817403427473588225_6.jpg)

FIG. 4. (a) Local spin magnetic moment $\mu^X$ ($X =$ Cu, Fe, and MgO) of the individual layers for the CuO- (black squares) and FeO-interface- (red circles) terminated one-unit-cell CuFe₂O₄/MgO superlattices. (b) The planar average of the charge density difference $\Delta\Omega$ along the $z$ axis. The vertical dashed lines indicate the positions of the interface layers in CuFe₂O₄ and MgO. (c) The layer-decomposed MAE and (d) orbital magnetic moment difference $\Delta\mu_o$ for the CuO- (black squares) and FeO-interface- (red circles) terminated one-unit-cell CuFe₂O₄/MgO superlattices. The letters I and C stand for the interface and center layers, respectively.

The local spin magnetic moment $\mu^X$ ($X =$ Cu, Fe, and MgO) in the different layers and the planar average density of the charge difference $\Delta\Omega$ along the $z$ axis are shown in Figs. 4(a) and 4(b) for the CuO- and FeO-interface-terminated one-unit-cell CuFe₂O₄/MgO superlattices, respectively. $\Delta\Omega$ is calculated by subtracting the charge densities of the separated CuFe₂O₄ and MgO slabs from the charge density of the CuFe₂O₄/MgO superlattice, $\Delta\Omega = \Omega(\text{CuFe}_2\text{O}_4/\text{MgO}) - \Omega(\text{CuFe}_2\text{O}_4) - \Omega(\text{MgO})$. For both superlattices, the bulk spin moments are almost preserved in the entire layer. On the other hand, the charge density profile indicates that the interface region exhibits very different features than the center layers in CuFe₂O₄ and MgO, which is a reflection of the charge transfer and/or redistribution across the interface. The charge is accumulated around the metal layer at the interface, whereas it is depleted around the interfacial MgO layer. Moreover, the strong hybridization between the Fe/Cu $3d$ and O $2p$ states causes charge redistribution within the interface layers. These effects can modify the energy landscape of the electronic states of the interfacial magnetic atoms around the Fermi level, which in turn modulates the magnetic anisotropy.

In Table II, we show the calculated MAE for the CuO- and FeO-interface-terminated one-unit-cell $CuFe_2O_4$/MgO superlattices. Results of MAE for the FeO-interface-terminated two-unit-cell $CuFe_2O_4$/MgO and one-unit-cell and two-unit-cell $Fe_3O_4$/MgO superlattices are also tabulated. The MAE values of the one-unit-cell and two-unit-cell $Fe_3O_4$/MgO superlattices are approximately 0.23 and $-0.14$ meV/f.u. (or 1.05 and $-2.40$ meV/interface), respectively, which indicates that both the magnitude and sign of MAE are thickness dependent. The positive (negative) value in MAE indicates favorable magnetization normal (parallel) to the interface plane, i.e., PMA (in-plane magnetization). On the other hand, the FeO-interface terminated one-unit-cell and 2-unit-cell $CuFe_2O_4$/MgO superlattices exhibit MAE of $\sim 0.32$ (1.51) and 0.24 (2.07 meV/interface) meV/f.u., respectively. One can thus note that the presence of the substitutional $Cu_{B}^{2+}$ ions in $Fe_3O_4$/MgO reorients its magnetization from in-plane to the PMA from the fact that the interface layers of the $Fe_3O_4$/MgO and the FeO-interface terminated $CuFe_2O_4$/MgO are the same. The PMA also increases with the thickness of $CuFe_2O_4$ layers in $CuFe_2O_4$/MgO superlattice. In contrast to the FeO-interface termination, the presence of the CuO-layer at the interface reduces MAE significantly. Moreover, we find that the MAE value of the bulk $CuFe_2O_4$ is 0.94 meV/cell or 0.12 meV/f.u., in contrast to negligibly small MAE in bulk $Fe_3O_4$ where $c/a=1$. We attribute this large MAE in bulk $CuFe_2O_4$ to the severe Jahn-Teller (and $xy$-plane twisted) distortion and the spin-orbit coupled Cu-$d$ states with induced magnetism. It can be thus expected that the large PMA of $CuFe_2O_4$/MgO superlattice is contributed either by the Fe $d$-O $p$ hybridization at the interface[5,46,48] and the spin-orbit coupled Cu $d$-orbital states in the Jahn-Teller distorted and in-plane twisted lattice at the center. A more detailed discussion and thickness-dependent MAE will be provided later in nonperiodic thin-film calculations.

To understand the opposite trends of MAE between the different interface terminations, the contribution to MAE from individual layers is analyzed in Fig. 4(c) for the CuO- and FeO-interface terminated one-unit-cell $CuFe_2O_4$/MgO superlattices. Notably, the two terminations exhibit quite different features in MAE: for the CuO-interface termination the MAE around the interface is rather small and negative, whereas it is very large and positive for the FeO termination. In particular, for the latter termination, the interfacial $Fe_{B}^{3+}$ ions have a very large PMA, which is presumably due to the orbital hybridization between the Fe $3d$ and O $2p$ states [5,46,48]. On the other hand, the $Fe_{B}^{3+}$ ions in the center layers contribute negatively to the total MAE. It is thus expected that this negative contribution becomes more dominant than the interface contribution as thickness increases, thereby affecting in-plane magnetization for the two-unit-cell $Fe_3O_4$/MgO superlattice (Table II). Notably, for both interface terminations the substitutional $Cu_{B}^{2+}$ ions even in the center layers provide significant contributions to the PMA. This PMA of Cu is reversed in sign at the interface with MgO, in contrast to the FeO-interface termination. For both systems, the contribution of the $Fe_{A}^{3+}$ site is negligibly small. Thus, the large PMA of the FeO-interface-terminated $CuFe_2O_4$/MgO mainly comes from the interfacial $Fe_{B}^{3+}$ and central $Cu_{B}^{2+}$ sites.

![](./images/817403427473588225_7.jpg)

FIG. 5. Difference of $d$-orbital projected SOC energies $\Delta E_{soc}$ between in-plane and out-of-plane magnetization orientations of the $Cu_{B}^{2+}$ atoms at the (a) interface and (b) center layers for the CuO-interface-terminated one-unit-cell $CuFe_2O_4$/MgO superlattice. The same for the $Fe_{B}^{3+}$ atoms at the (c) interface and (d) center layers of the FeO-interface-terminated one-unit-cell $CuFe_2O_4$/MgO superlattice. The letters I and C in parentheses stand for the interface and center layers, respectively. Blue and red bars represent the negative and positive MAE, respectively.

The crucial roles of these octahedral ions in the large PMA are further inspected with the Bruno formula [49], $\text{MAE} = \frac{\xi}{4\mu_B}\Delta\mu_\text{o}$, where $\xi$ is the SOC constant and $\Delta\mu_\text{o}$ is the orbital moment anisotropy (OMA), i.e., $\Delta\mu_\text{o} = \mu_\text{o}^\parallel - \mu_\text{o}^\perp$. Indeed, this expression needs to be modified for structures consisting of multiple atomic species with strong hybridization and large spin-orbit interaction [50]. The calculated $\Delta\mu_\text{o}$ in the different layers are shown in Fig. 4(d) for the CuO- and FeO-interface-terminated one-unit-cell $CuFe_2O_4$/MgO superlattices. Notably, for both interface terminations $\Delta\mu_\text{o}$ is large only for the $Cu_{B}^{2+}$ site in the center layers, while those of the center Fe are negligibly small. On the other hand, for the FeO-interface termination, the interfacial $Fe_{B}^{2+}$ ions exhibit non-negligible $\Delta\mu_\text{o}$. From the layer-decomposed MAE and OMA, where the Bruno expression is approximately satisfied, we determine the presence of the $Cu_{B}^{2+}$ ions and interface effects, including the Fe $3d$-O $2p$ hybridization, charge transfer/redistribution, and spin and orbital moment modifications, is a main cause of the anisotropic phenomenon for the $CuFe_2O_4$/MgO superlattice. Note that a very large orbital magnetic moment is found at the $Fe_3O_4$/MgO interface in x-ray magnetic circular dichroism experiments [51-52].

To get more insights, we show the energy differences in the SOC term, $\Delta E_{\text{soc}} = E_{\text{soc}}^\parallel - E_{\text{soc}}^\perp$, projected onto the $d$-orbital matrix elements of the $Cu_{B}^{2+}$ ions at the interface and in center layers of the CuO-interface-terminated one-unit-cell $CuFe_2O_4$/MgO superlattice in Figs. 5(a) and 5(b), respectively. We also show the same $\Delta E_{\text{soc}}$ of the

$\text{Fe}_B^{3+}$ ions for the FeO-interface-terminated one-unit-cell $\text{CuFe}_2\text{O}_4$/MgO in Figs. 5(c) and 5(d), respectively. Here, $E_{\text{soc}} = \frac{\hbar^2}{2m^2 c^2} \frac{1}{r} \frac{dV(r)}{dr} L \cdot S$, where $V(r)$ is the spherical part of the effective potential within the PAW sphere and $L$ and $S$ are orbital and spin operators, respectively. These expectation values are twice the actual value of the total energy correction to the second order in SOC [53]. The other 50% of the SOC energy translates into the crystal-field energy and the formation of the unquenched orbital moment [54]. In the second-order perturbation theory, the MAE is then determined by the SOC between occupied and unoccupied bands [55],
$$
\text{MAE}^{\sigma \sigma'} = \xi^2 \sum_{o,u} \frac{|\langle \Psi_{o,\sigma}|\hat{L}_z|\Psi_{u,\sigma'}\rangle|^2 - |\langle \Psi_{o,\sigma}|\hat{L}_x|\Psi_{u,\sigma'}\rangle|^2}{E_{u,\sigma'} - E_{o,\sigma}},
$$
where $\Psi_{o,\sigma}$ ($\Psi_{u,\sigma'}$) and $E_{o,\sigma}$ ($E_{u,\sigma'}$) are the eigenstates and eigenvalues of occupied (unoccupied) states for each spin state, $\sigma, \sigma' = \uparrow, \downarrow$, respectively, and $\hat{L}_{x(z)}$ is the $x$ ($z$) component of the orbital angular momentum operator. For $\sigma \sigma' = \uparrow \uparrow$ or $\downarrow \downarrow$, the positive (negative) contribution to MAE is determined by the SOC with the same (different by 1) magnetic quantum number $m$ through the $\hat{L}_z$ ($\hat{L}_x$) operator. The relative contributions of the nonzero $\hat{L}_z$ and $\hat{L}_x$ matrix elements are $\langle xz|\hat{L}_z|yz\rangle = 1$, $\langle xy|\hat{L}_z|x^2 - y^2\rangle = 2$, $\langle xz, yz|\hat{L}_x|z^2\rangle = \sqrt{3}$, $\langle xz, yz|\hat{L}_x|xy\rangle = 1$, and $\langle xz, yz|\hat{L}_x|x^2 - y^2\rangle = 1$. For $\sigma \sigma' = \uparrow \downarrow$, MAE has the opposite sign, so the positive (negative) contribution comes from the $\hat{L}_x$ ($\hat{L}_z$) coupling.

In Figs. 6(a)-6(d), we show the PDOS of the interfacial and central $\text{Cu}_B^{2+}$ and $\text{Fe}_B^{3+}$ ions for the CuO- and FeO-interface-terminated one-unit-cell $\text{CuFe}_2\text{O}_4$/MgO superlattices. For comparison, we also show the same PDOS for the FeO-interface-terminated one-unit-cell $\text{Fe}_3\text{O}_4$/MgO superlattice in Figs. 6(e) and 6(f), respectively. By analyzing the $d$-orbital decomposed MAE along with the electronic structure, one can argue that the small negative MAE of $\text{Cu}_B^{2+}$ at the interface is the result of the competition between the positive contribution of the SOC term with the matrix element $\langle xy_\downarrow|\hat{L}_z|x^2 - y_\downarrow^2\rangle$ and the negative contribution of $\langle xz, yz_\downarrow|\hat{L}_x|z_\downarrow^2\rangle$. For the central $\text{Cu}_B^{2+}$, the SOC pairing between the occupied $d_{xy}$ and unoccupied $d_{x^2-y^2}$ orbitals in the minority-spin state becomes stronger with the downward shift of the unoccupied $d_{x^2-y^2}$ state toward the Fermi level. Thus, the positive contribution further increases approximately two times for the central $\text{Cu}_B^{2+}$, whereas the negative one disappears and thus so does the enhanced MAE at the center [Fig. 4(c)]. The other spin-channel contributions of the spin up-up ($\uparrow \uparrow$) and spin up-down ($\uparrow \downarrow$) to MAE can be simply neglected due to the completely filled majority-spin states, analogous to the freestanding Fe and Fe/MgO films [47,56]. On the other hand, the negative contribution is essentially not present for the central $\text{Cu}_B^{2+}$ site because of the absence of the minority-spin empty $d_{z^2}$ state.

For the FeO-interface-terminated $\text{CuFe}_2\text{O}_4$/MgO, the large PMA of the interfacial $\text{Fe}_B^{3+}$ is mainly predominated by the SOC states of the majority-spin filled $d_{z^2}$ state and the minority-spin empty $d_{xz,yz}$ states, which provides the positive term of $\langle z_\uparrow^2|\hat{L}_z|xz, yz_\downarrow\rangle$. One can apply this argument to the interfacial Fe atom for the $\text{Fe}_3\text{O}_4$/MgO heterostructure because of the feature similarities in band characters and SOC matrix elements. Moreover, the SOC between the occupied $d_{x^2-y^2}$ orbital in the majority-spin state and the unoccupied $d_{xy}$ orbital in the minority-spin state results in small negative MAE. This negative contribution of $\langle x^2 - y_\uparrow^2|\hat{L}_x|xy_\downarrow\rangle$ becomes even stronger in the central Fe site owing to the downward shift of the empty $d_{xy}$ state in the minority-spin state toward the Fermi level.

![](./images/817403427473588225_8.jpg)

FIG. 6. Spin and $d$-orbital resolved PDOS of the $\text{Cu}_B^{2+}$ atoms at the (a) interface and (b) center layers for the CuO-interface-terminated one-unit-cell $\text{CuFe}_2\text{O}_4$/MgO superlattice. The same for the $\text{Fe}_B^{3+}$ atoms at the (c) interface and (d) center layers of the FeO-interface-terminated one-unit-cell $\text{CuFe}_2\text{O}_4$/MgO superlattice. The same for the $\text{Fe}_B^{3+}$ atoms at the (e) interface and (f) center layers of the one-unit-cell $\text{Fe}_3\text{O}_4$/MgO superlattice. The letters I and C in parentheses stand for the interface and center layers, respectively. The dashed black and orange and solid red and blue lines denote the $d_{xy}, d_{xz,yz}, d_{x^2}$, and $d_{x^2-y^2}$ orbital states, respectively. The Fermi level is set to zero in energy.

Finally, for more feasibility and insights, we performed nonperiodic slab (along the $z$ axis) calculations for the magnetism and MAE of $\text{Fe}_3\text{O}_4$/MgO(001) and $\text{CuFe}_2\text{O}_4$/MgO(001) thin films. For comparison purposes, the same calculations for $\text{CuFe}_2\text{O}_4$(001) films without MgO were also carried out. As shown in Figs. 7(a) and 7(b), the slab supercell along the $z$ axis consists of 5-17 ALs (0.5-2 unit cells) of $\text{Fe}_3\text{O}_4$ and $\text{CuFe}_2\text{O}_4$ films on top of 5-AL MgO and an about 15-Å-thick vacuum region separating the periodic slabs, respectively. Only the most stable FeO-interface termination is chosen at the $\text{Fe}_3\text{O}_4$/MgO and $\text{CuFe}_2\text{O}_4$/MgO interfaces, while both the FeO- and CuO-surface terminations have been taken into account for the different film thicknesses. The experimental lattice constant (4.212 Å) of MgO is used for the in-plane lattice of supercells, which is matched to the optimized bulk lattices of the bulk $\text{CuFe}_2\text{O}_4$ (type II) and $\text{Fe}_3\text{O}_4$ within 2.1% and 0.8%, respectively.

![](./images/817403427473588225_9.jpg)

FIG. 7. Side views of the optimized atomic structures for the two-unit-cell (a) $Fe_3O_4$/MgO and (b) $CuFe_2O_4$/MgO(001) films. The larger gray, pink, and orange and smaller red spheres are $Fe^{3+}$, $Cu^{2+}$, Mg, and O atoms, respectively. Thickness-dependent (c) total magnetization and (d) MAE per formula unit for $CuFe_2O_4$/MgO (solid squares) and $Fe_3O_4$/MgO (solid circle)s. The corresponding results for $CuFe_2O_4$ films without MgO are also shown by open symbols. In (c) [(d)], the horizontal black and red dashed lines indicate the magnetization (MAE) of bulk $CuFe_2O_4$ and $Fe_3O_4$ [two-unit-cell (or 17-AL) $CuFe_2O_4$/MgO and $Fe_3O_4$/MgO superlattices], respectively.

The total magnetization and MAE versus the film thickness $n$ are shown in Figs. 7(c) and 7(d) for $CuFe_2O_4$/MgO and $Fe_3O_4$/MgO films, respectively. For both systems, the magnetization decreases gradually as $n$ increases, except $n=7$ for $CuFe_2O_4$/MgO, and tends to reach the bulk values of $4\mu_B$/f.u. for $Fe_3O_4$ and $1\mu_B$/f.u. for $CuFe_2O_4$, as found previously in the periodic superlattice calculations. The magnetic moments of the Cu ions at the surface next to vacuum for the seven-AL $CuFe_2O_4$/MgO films are almost diminished, which results in such a singular behavior of the smaller magnetization at $n=7$. The larger magnetization at the thinner films is due to the dominant number $N$ of $Fe_B^{3+}$ ions to that of $Fe_A^{3+}$ in the unit cell, as previously mentioned. Overall, the total magnetization of the nonperiodic thin-film structures reproduces those obtained from the periodic superlattice calculations. Moreover, results for $CuFe_2O_4$ films without MgO, as shown by the open symbols in Fig. 7(c), indicate that the total magnetization of the supercell films does not change much in the presence of MgO. Nevertheless, the presence of MgO slightly enhances the local magnetic moments of the interfacial $Fe_B^{3+}$ ions by about $0.1\mu_B$.

As shown in Fig. 7(d), the MAE values of $Fe_3O_4$/MgO films are $\sim$0.04 and 0.07 meV/f.u. and positive for $n=5$ and 7, respectively. As $n$ increases further, the MAE decreases, and its sign changes to negative (in-plane magnetization) at $n=9$ (one unit cell). The PMA of the thinner films is mainly due to the interface effects [5,46,48], while the negative contributions to the total MAE from the center layers become more dominant for the thicker films. On the other hand, for $CuFe_2O_4$/MgO films the MAE increases with $n$ and starts to saturate at $n=9$. This large PMA originates mainly from the spin-orbit-coupled Cu $d_{xy}$-$d_{x^2-y^2}$ states in the Jahn-Teller distorted and $xy$-plane twisted lattice in the center layers, as explicitly discussed before for the superlattice calculations. Furthermore, the MAE of the one-unit-cell $CuFe_2O_4$/MgO films is about 0.24 meV/f.u. (or 1.12 meV/interface), which is $\sim$30% smaller than that (0.32 meV/f.u., or 1.51 meV/interface) for the one-unit-cell-thick periodic superlattice (Table II). For the two-unit-cell thickness, this difference in MAE between the nonperiodic film (0.21 meV/f.u., or 1.81 meV/interface) and periodic superlattice (0.24 meV/f.u., or 2.07 meV/interface) structures becomes even smaller ($\sim$14%). Presumably, it is associated with the interface effects with MgO [from a comparison of MAE for $CuFe_2O_4$ with (solid squares) and without (open squares) MgO in Fig. 7(d)] and epitaxial strain [4,39,48,57]. Unlike the periodic superlattice, the nonperiodic film structure has only one interface in contact with MgO and is constrained to the in-plane lattice of MgO.

### IV. CONCLUSION

In summary, we have performed the first-principles calculations of the magnetism and MAE in the spinel $CuFe_2O_4$/MgO heterostructure. It was found that the substitutional $Cu^{2+}$ ions prefer the octahedral site within the $xy$-plane layer in an inverse spinel structure. Our calculations revealed that the B-site $Cu^{2+}$ substitution leads to the magnetization reorientation and large PMA in the $Fe_3O_4$/MgO heterostructure. More importantly, we further identified that such a large PMA can even increase substantially with the film thickness of $CuFe_2O_4$ layers in $CuFe_2O_4$/MgO. By analyzing the single-particle energy spectra with the spin-orbit Hamiltonian matrix elements, we provided physical insights into the large PMA of the $CuFe_2O_4$/MgO heterostructure in terms of the hybridization effect between Fe $d$ and O $p$ orbitals at the interface and the interplay of the spin-orbit-coupled Cu $d$ states in the Jahn-Teller distorted and in-plane twisted lattice at the center. The present model structures can act as a prototype for in-depth study of the microscopic origin of the large PMA for ferrite-based magnetic tunnel junctions in spintronic applications, which would motivate further experimental verification.

### ACKNOWLEDGMENTS

This research was supported by Future Materials Discovery Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT (2016M3D1A1027831) and Incheon National University Research Grant in 20170096.

[1] S. Ikeda, K. Miura, H. Yamamoto, K. Mizunuma, H. D. Gan, M. Endo, S. Kanai, J. Hayakawa, F. Matsukura, and H. Ohno, A perpendicular-anisotropy CoFeB-MgO magnetic tunnel junc- tion, *Nat. Mater.* **9**, 721 (2010).

[2] D. Weller and A. Moser, Thermal effect limits in ultrahigh- density magnetic recording, *IEEE Trans. Magn.* **35**, 4423 (1999).

[3] J. Z. Sun, Spin-current interaction with a monodomain magnetic body: A model study, *Phys. Rev.* **B 62**, 570 (2000).

[4] D. Odkhuu, S. H. Rhim, N. Park, K. Nakamura, and S. C. Hong, Jahn-Teller driven perpendicular magnetocrystalline anisotropy in metastable ruthenium, *Phys. Rev.* **B 91**, 014437 (2015).

[5] D. Odkhuu, Magnetization reversal of giant perpendicular mag- netic anisotropy at the magnetic-phase transition in FeRh films on MgO, *Phys. Rev.* **B 93**, 064412 (2016).

[6] S. Loth, S. Baumann, C. P. Lutz, D. M. Eigler, and A. J. Heinrich, Bistability in atomic-scale antiferromagnets, *Science* **335**, 196 (2012).

[7] X. Marti, I. Fina, C. Frontera, J. Liu, P. Wadley, Q. He, R. J. Paull, J. D. Clarkson, J. Kudrnovský, I. Turek, J. Kuneš, D. Yi, J.-H. Chu, C. T. Nelson, L. You, E. Arenholz, S. Salahuddin, J. Fontcuberta, T. Jungwirth, and R. Ramesh, Room-temperature antiferromagnetic memory resistor, *Nat. Mater.* **13**, 367 (2014).

[8] J. M. D. Coey, A. E. Berkowitz, Ll. Balcells, F. F. Putris, and F. T. Parker, Magnetoresistance of magnetite, *Appl. Phys. Lett.* **72**, 734 (1998).

[9] G. Hu and Y. Suzuki, Negative Spin Polarization of $\text{Fe}_3\text{O}_4$ in Magnetite/Manganite-Based Junctions, *Phys. Rev. Lett.* **89**, 276601 (2002).

[10] Y. S. Dedkov, U. Rudiger, and G. Guntherodt, Evidence for the half-metallic ferromagnetic state of $\text{Fe}_3\text{O}_4$ by spin-resolved photoelectron spectroscopy, *Phys. Rev.* **B 65**, 064417 (2002).

[11] J. M. D. Coey and C. L. Chien, Half-metallic ferromagnetic oxides, *MRS Bull.* **28**, 720 (2003).

[12] C. A. F. Vaz, J. Hoffman, A.-B. Posadas, and C. H. Ahn, Magnetic anisotropy modulation of magnetite in $\text{Fe}_3\text{O}_4$/BaTiO$_3$(100) epitaxial structures, *Appl. Phys. Lett.* **94**, 022504 (2009).

[13] Z.-M. Liao, H.-C. Wu, J.-J. Wang, G. L. W. Cross, S. Kumar, I. V. Shvets, and G. S. Duesberg, Magnetoresistance of $\text{Fe}_3\text{O}_4$-graphene-$\text{Fe}_3\text{O}_4$ junctions, *Appl. Phys. Lett.* **98**, 052511 (2011).

[14] O. Chichvarina, T. S. Herng, W. Xiao, X. Hong, and J. Ding, Magnetic anisotropy modulation of epitaxial $\text{Fe}_3\text{O}_4$ films on MgO substrates, *J. Appl. Phys.* **117**, 17D722 (2015).

[15] E. Verwey, Electronic conduction of magnetite ($\text{Fe}_3\text{O}_4$) and its transition point at low temperatures, *Nature (London)* **144**, 327 (1939).

[16] V. N. Antonov, B. N. Harmon, and A. N. Yaresko, Electronic structure and x-ray magnetic circular dichroism in $\text{Fe}_3\text{O}_4$ and Mn-, Co-, or Ni-substituted $\text{Fe}_3\text{O}_4$, *Phys. Rev. B* **67**, 024417 (2003).

[17] M. G. Chapline and S. X. Wang, Room-temperature spin fil- tering in a $\text{CoFe}_2\text{O}_4$/MgAl$_2\text{O}_4$/$\text{Fe}_3\text{O}_4$ magnetic tunnel barrier, *Phys. Rev.* **B 74**, 014418 (2006).

[18] Z. Szotek, W. M. Temmerman, D. Ködderitzsch, A. Svane, L. Petit, and H. Winter, Electronic structures of normal and inverse spinel ferrites from first principles, *Phys. Rev. B* **74**, 174431 (2006).

[19] J.-S. Kang, G. Kim, H. J. Lee, D. H. Kim, H. S. Kim, J. H. Shim, S. Lee, H. Lee, J.-Y. Kim, B. H. Kim, and B. I. Min, Soft x-ray absorption spectroscopy and magnetic circular dichroism study of the valence and spin states in spinel $\text{MnFe}_2\text{O}_4$, *Phys. Rev. B* **77**, 035121 (2008).

[20] D. Fritsch and C. Ederer, Epitaxial strain effects in the spinel ferrites $\text{CoFe}_2\text{O}_4$ and $\text{NiFe}_2\text{O}_4$ from first principles, *Phys. Rev. B* **82**, 104117 (2010).

[21] J. A. Moyer, C. A. F. Vaz, D. A. Arena, D. Kumah, E. Negusse, and V. E. Henrich, Magnetic structure of Fe-doped $\text{CoFe}_2\text{O}_4$ probed by x-ray magnetic spectroscopies, *Phys. Rev. B* **84**, 054447 (2011).

[22] I. Nedkov, R. E. Vandenberghe, T. S. Marinova, P. H. Thailhades, T. Merodiiska, and I. Avramova, Magnetic structure and collective JahnTeller distortions in nanostructured particles of $\text{CuFe}_2\text{O}_4$, *Appl. Surf. Sci.* **253**, 2589 (2006).

[23] C. D. Lokhande, S. S. Kulkarni, R. S. Mane, and S. H. Han, Copper ferrite thin films: Single-step non-aqueous growth and properties, *J. Cryst. Growth* **303**, 387 (2007).

[24] C. D. Lokhande, S. S. Kulkarni, R. S. Mane, and S. H. Han, Room temperature single-step electrosynthesized copper ferrite thin films and study of their magnetic properties, *J. Magn. Magn. Mater.* **313**, 69 (2007).

[25] D. Thapa, N. Kulkarni, S. N. Mishra, P. L. Paulose, and P. Ayyub, Enhanced magnetization in cubic ferrimagnetic $\text{CuFe}_2\text{O}_4$ nanoparticles synthesized from a citrate precursor: the role of $\text{Fe}^{2+}$, *J. Phys. D: Appl. Phys.* **43**, 195004 (2010).

[26] M. J. Iqbal, N. Yaqub, B. Sepiol, and I. Bushra, A study of the influence of crystallite size on the electrical and magnetic properties of $\text{CuFe}_2\text{O}_4$, *Mater. Res. Bull.* **46**, 1837 (2011).

[27] O. Mounkachi, M. Hamedoun, M. Belaiche, A. Benyoussef, R. Masrour, H. Moussaoui, and M. Sajjeddine, Synthesis and magnetic properties of ferrites spinels $\text{Mg}_x\text{Cu}_{1-x}\text{Fe}_2\text{O}_4$, *Phys. B (Amsterdam, Neth.)* **407**, 27 (2012).

[28] E. Prince and R. G. Treuting, The structure of tetragonal copper ferrite, *Acta Crystallogr.* **9**, 1025 (1956).

[29] B. J. Evans and S. Hafner, Mössbauer resonance of $\text{Fe}^{57}$ in oxidic spinels containing Cu and Fe, *J. Phys. Chem. Solids* **29**, 1573 (1968).

[30] X. X. Tang, A. Manthiram, and J. B. Goodenough, Copper ferrite revisited, *J. Solid State Chem.* **79**, 250 (1989).

[31] J. Z. Jiang, G. F. Goya, and H. R. Rechenberg, Magnetic proper- ties of nanostructured $\text{CuFe}_2\text{O}_4$, *J. Phys.: Condens. Matter* **11**, 4063 (1999).

[32] P. E. Blöchl, Projector augmented-wave method, *Phys. Rev. B* **50**, 17953 (1994).

[33] G. Kresse and J. Hafner, *Ab initio* molecular dynamics for liquid metals, *Phys. Rev. B* **47**, 558(R) (1993).

[34] G. Kresse and J. Furthmüller, Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set, *Phys. Rev. B* **54**, 11169 (1996).

[35] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, *Phys. Rev. Lett.* **77**, 3865 (1996).

[36] V. I. Anisimov, I. S. Elfimov, N. Hamada, and K. Terakura, Charge-ordered insulating state of $\text{Fe}_3\text{O}_4$ from first-principles electronic structure calculations, *Phys. Rev. B* **54**, 4387 (1996).

[37] I. Leonov, A. N. Yaresko, V. N. Antonov, M. A. Korotin, and V. I. Anisimov, Charge and Orbital Order in $\text{Fe}_3\text{O}_4$, *Phys. Rev. Lett.* **93**, 146404 (2004).

[38] A. Chainani, T. Yokoya, T. Morimoto, T. Takahashi, and S. Todo, High-resolution photoemission spectroscopy of the Ver- wey transition in $\text{Fe}_3\text{O}_4$, *Phys. Rev. B* **51**, 17976 (1995).

[39] D. Odkhuu, P. Taivansaikhan, W. S. Yun, and S. C. Hong, A first-principles study of magnetostrictions of $\text{Fe}_3\text{O}_4$ and $\text{CoFe}_2\text{O}_4$, *J. Appl. Phys.* **115**, 17A916 (2014).

[40] A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Density-functional theory and strong interactions: Orbital ordering in Mott-Hubbard insulators, *Phys. Rev. B* **52**, R5467 (1995).

[41] Z. Zhang and S. Satpathy, Electron states, magnetism, and the Verwey transition in magnetite, *Phys. Rev. B* **44**, 13319 (1991).

[42] H. T. Jeng and G. Y. Guo, First-principles investigations of the electronic structure and magnetocrystalline anisotropy in strained magnetite $\text{Fe}_3\text{O}_4$, *Phys. Rev. B* **65**, 094429 (2002).

[43] D. D. Koelling and B. N. Harmon, A technique for relativistic spin-polarised calculations, *J. Phys. C* **10**, 3107 (1977).

[44] A. M. Balagurov, I. A. Bobrikov, M. S. Maschenko, D. Sangaa, and V. G. Simkin, Structural phase transition in $\text{CuFe}_2\text{O}_4$ spinel, *Crystallogr. Rep.* **58**, 710 (2013).

[45] Z. Jiang, W. Zhang, W. Shangguan, X. Wu, and Y. Teraoka, Adsorption of NO molecule on spinel-type $\text{CuFe}_2\text{O}_4$ Surface: A first-principles study, *J. Phys. Chem. C* **115**, 13035 (2011).

[46] H. X. Yang, M. Chshiev, B. Dieny, J. H. Lee, A. Manchon, and K. H. Shin, First-principles investigation of the very large perpendicular magnetic anisotropy at Fe/MgO and Co/MgO interfaces, *Phys. Rev. B* **84**, 054401 (2011).

[47] D. Odkhuu, W. S. Yun, S. Rhim, and S. C. Hong, Theory of perpendicular magnetocrystalline anisotropy in Fe/MgO(001), *J. Magn. Magn. Mater.* **414**, 126 (2016).

[48] D. Odkhuu, Electric control of magnetization reorientation in $\text{FeRh/BaTiO}_3$ mediated by a magnetic phase transition, *Phys. Rev. B* **96**, 134402 (2017).

[49] P. Bruno, Tight-binding approach to the orbital magnetic moment and magnetocrystalline anisotropy of transition-metal monolayers, *Phys. Rev. B* **39**, 865(R) (1989).

[50] C. Andersson, B. Sanyal, O. Eriksson, L. Nordström, O. Karis, D. Arvanitis, T. Konishi, E. Holub-Krappe, and J. Hunter Dunn, Influence of Ligand States on the Relationship between Orbital Moment and Magnetocrystalline Anisotropy, *Phys. Rev. Lett.* **99**, 177207 (2007).

[51] W. Q. Liu, Y. B. Xu, P. K. J. Wong, N. J. Maltby, S. P. Li, X. F. Wang, J. Du, B. You, J. Wu, P. Bencok, and R. Zhang, Spin and orbital moments of nanoscale $\text{Fe}_3\text{O}_4$ epitaxial thin film on MgO/GaAs(100), *Appl. Phys. Lett.* **104**, 142407 (2014).

[52] W. Q. Liu, M. Y. Song, N. J. Maltby, S. P. Li, J. G. Lin, M. G. Samant, S. S. P. Parkin, P. Bencok, P. Steadman, A. Dobrynin, Y. B. Xu, and R. Zhang, X-ray magnetic circular dichroism study of epitaxial magnetite ultrathin film on MgO(100), *J. Appl. Phys.* **117**, 17E121 (2015).

[53] V. Antropov, L. Ke, and D. Aberg, Constituents of magnetic anisotropy and a screening of spin-orbit coupling in solids, *Solid State Commun.* **194**, 35 (2014).

[54] R. Skomski, A. Kashyap, and A. Enders, Is the magnetic anisotropy proportional to the orbital moment? *J. Appl. Phys.* **109**, 07E143 (2011).

[55] K. L. Wang, J. G. Alzate, and P. K. Amiri, Lower-power non-volatile spintronics memory: STT-RAM and beyond, *J. Phys. D* **46**, 074003 (2013).

[56] D. Odkhuu, S. H. Rhim, N. Park, and S. Hong, Extremely large perpendicular magnetic anisotropy of an Fe(001) surface capped by $5d$ transition metal monolayers: A density functional study, *Phys. Rev. B* **88**, 184405 (2013).

[57] D. Odkhuu, Giant strain control of magnetoelectric effect in Ta/Fe/MgO, *Sci. Rep.* **6**, 32742 (2016).