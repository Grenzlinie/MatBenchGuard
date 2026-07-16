# Structural and electronic properties of bulk $Li_2O_2$: first-principles simulations based on numerical atomic orbitals

Paul M. Masanja, $^1$ Toraya Fernández-Ruiz, $^2$ Esther J. Tarimo, $^1$ Nayara Carral-Sainz, $^2$ P.V. Kanaka Rao, $^1$ Vijay Singh, $^1$ Bernard Mwankemwa, $^1$ Juan María García-Lastra, $^3$ Pablo García-Fernández, $^2$ and Javier Junquera$^2$

$^1$Department of Physics, College of Natural and Mathematical Sciences, University of Dodoma, PO Box 259, Dodoma, Tanzania
$^2$Departamento de Ciencias de la Tierra y Física de la Materia Condensada, Universidad de Cantabria, Avenida de los Castros s/n, 39005 Santander, Spain
$^3$Department of Energy Conversion and Storage, Technical University of Denmark, Kongens Lyngby DK-2800, Denmark
(Dated: December 24, 2024)

The development of advanced materials with high specific energy is crucial for enabling sustainable energy storage solutions, particularly in applications such as lithium-air batteries. Lithium peroxide ($Li_2O_2$) is a key discharge product in non-aqueous lithium-air systems, where its structural and electronic properties significantly influence battery performance. In this work, we investigate the atomic structure, electronic band structure, and Wannier functions of bulk $Li_2O_2$ using density functional theory. The performance of different basis sets of numerical atomic orbitals are compared with respect to a converged plane-wave basis results. We analyze the material's ionic characteristics, the formation of molecular orbitals in oxygen dimers, and the band gap discrepancies between various computational approaches. Furthermore, we develop a localized Wannier basis to model electron-vibration interactions and explore their implications for polaron formation. Our findings provide a chemically intuitive framework for understanding electron-lattice coupling and offer a basis for constructing reduced models that accurately describe the dynamics of polarons in $Li_2O_2$. These insights contribute to the broader goal of improving energy storage technologies and advancing the field of materials design.

## I. INTRODUCTION

The development of materials capable of storing energy with minimal weight, i.e., achieving high specific energy, is critically important for the vehicle industry. This objective is a key milestone in the transition away from fossil fuels in the global economy [1-4]. Among the most promising technologies competing with the specific energy of gasoline (46.4 MJ/kg) are lithium/air or lithium/oxygen batteries, which exhibit typical specific energy values of approximately 40 MJ/kg [5].

In non-aqueous lithium/air batteries, where the electrolyte is not carbonate-based, the primary discharge product in the cathode is lithium peroxide ($Li_2O_2$) [6]. This compound, commonly identified in batteries via Raman spectroscopy [6], is an insulating material with a wide bandgap of approximately 5.0-6.0 eV, as determined through various *ab initio* calculation techniques [2, 7, 8]. Substantial research efforts [2, 3, 8, 9] have focused on understanding its transport properties, as the accumulation of $Li_2O_2$ near the cathode [4] can block charge flow and cause the so-called *sudden death* of the battery.

It is now widely accepted that both electron and hole polarons [8-10] form in these systems, and their hopping barriers have been characterized to estimate their mobilities [8]. However, more advanced simulations of electron and hole dynamics, such as modeling electron tunneling between distant $O_2^{2-}$ ions, have yet to be fully developed.

Our objective is to progress toward such simulations using *second-principles* methods [11]. To achieve this, we aim to characterize and model the system's main electronic bands by developing an efficient set of Wannier functions [12]. These functions serve as a basis for accurately describing the band structure while employing a small set of highly localized functions.

The most relevant orbitals for describing the behavior of $Li_2O_2$ are often associated with nearly isolated $O_2^{2-}$ ions embedded within a hexagonal lattice that also includes $Li^+$ counter-ions [8] (see Fig. 1). Previous studies have primarily relied on band structure and density-of-states analyses. However, to the best of our knowledge, there has been no direct characterization of the localization and shape of the corresponding Wannier functions.

Using our parameterized model, we will investigate how the Wannier one-electron Hamiltonian varies with changes in the system's geometry. This approach will provide a chemically intuitive understanding of the strong electron-phonon coupling present in the system, which plays a critical role in polaron formation [10].

The rest of the paper is organized as follows. The method on which the simulations are based is described in Sec. II. In Sec. III, we discuss the details of the atomic structure of bulk $Li_2O_2$. The electronic structure is presented in Sec. IV, where we also analyze the density of states. Finally, in Sec. V, we study the Wannier functions and how the Hamiltonian matrix elements expressed in this basis change with the atomic geometry.

## II. METHODOLOGY

Our calculations have been performed within density functional theory [13] (DFT) and the generalized gradient approximation (GGA). We used a numerical atomic orbital (NAO) method, as it is implemented in the SIESTA code [14, 15]. The exchange-correlation functional was approximated using the Perdew-Burke-Ernzerhof (PBE) functional [16], as implemented in the LIBXC library [17, 18].

Core electrons were replaced by ab initio norm-conserving fully separable pseudopotentials [19]. In this work the optimized norm-conserving Vanderbilt pseudopotentials proposed by Hamann [20] were used, in the PSML format [21] available in the Pseudo-Dojo periodic table [22, 23]. For Li, the semicore 1s electrons were explicitly included in the valence. For O, the valence configuration was made of the 2s and 2p orbitals.

The one-electron Kohn-Sham eigenstates were expanded in a basis of strictly localized [24] numerical atomic orbitals [25]. Basis functions were obtained by finding the eigenfunctions of the isolated atoms confined within the soft-confinement spherical potential proposed in Ref. [26]. A single-$\zeta$ basis set was applied to the 1s semicore states of Li. For the valence states of Li and O, we used basis sets of varying sizes, ranging from double-$\zeta$ to triple-$\zeta$, corresponding to two or three radial functions per occupied valence angular momentum shell in the free atom (2s for Li, and 2s and 2p for O). To enhance angular flexibility, higher angular momentum polarization orbitals (not occupied in the free atom) were included, with an additional shell of 2p orbitals for Li and 3d orbitals for O, using one (single-polarized) or two (double-polarized) radial functions per polarization shell. All parameters defining the basis functions for Li and O were optimized variationally at the relaxed structure obtained with a converged plane-wave code, following the method in Ref. [26].

The electronic density, Hartree, and exchange-correlation potentials, as well as the corresponding matrix elements between the basis orbitals, were calculated in a uniform real space grid [14]. An equivalent plane-wave cutoff of 600 Ry was used to represent the charge density. The integrals in reciprocal space were well converged, using in all the cases a sampling in reciprocal space of the same quality as the $(8 \times 8 \times 4)$ Monkhorst-Pack mesh [27].

Atomic coordinates were relaxed using a conjugate gradient algorithm until the maximum component of the force on any atom was smaller than $10\ \text{meV}/\text{\AA}$, and the maximum component of the stress tensor was below $0.0001\ \text{eV}/\text{\AA}^3$.

For a given functional and pseudopotential, the converged-basis limit is achieved by a plane-wave calculation with a very high cutoff. To assess the convergence of our NAO basis, we compared the results from SIESTA with those obtained using ABINIT [28-30]. We aimed to keep the simulations as comparable as possible.

TABLE I: Atomic positions of the symmetry inequivalent atoms of bulk $\text{Li}_2\text{O}_2$ in the hexagonal $\text{P6}_3/\text{mmc}$ space group.

| Wyckoff | Element | $x$ | $y$ | $z$ |
|---------|---------|-----|-----|-----|
| $2a$    | Li      | 0   | 0   | 0   |
| $2c$    | Li      | $1/3$ | $2/3$ | $1/4$ |
| $4f$    | O       | $1/3$ | $2/3$ | $z$ (O) |

Both codes can read identical pseudopotentials in the PSML format, using the same decomposition into a local pseudopotential operator and Kleinman-Bylander projectors. They also share the same exchange-correlation functional, drawn from the same version of the LIBXC library, as well as an identical $k$-point sampling quality and Fermi-Dirac occupation function. The only variation lies in the plane-wave basis set, for which a converged cutoff of 50 Ha was chosen.

## III. STRUCTURAL PROPERTIES

$\text{Li}_2\text{O}_2$ has traditionally been associated with two different structures (both of them hexagonal) experimentally measured in the 1950s: the one proposed by Fehér [31] (belonging to symmetry group P-6, 174) and the one proposed by Föppl [32] (belonging to the $\text{P6}_3/\text{mmc}$ space group, 194). Later experimental studies, such as the one presented in Ref. [33], using a combination of X-ray and first-principles simulations, showed that the structure proposed by Föppl [32] is the most suitable for $\text{Li}_2\text{O}_2$. This was also supported by previous first-principles density functional theory simulations [34], where symmetrized structures for both configurations were compared. Therefore, the Föppl structure within the $\text{P6}_3/\text{mmc}$ symmetry group has been used to date to conduct first-principles studies on excitonic effects and their relationship with vibronic coupling [35], as well as polaron dynamics [8, 10].

In Föppl's revised structure for $\text{Li}_2\text{O}_2$ with $\text{P6}_3/\text{mmc}$ symmetry, schematized in Fig. 1, the unit cell contains two formula units, with lithium atoms positioned between adjacent oxygen planes along the $c$-axis. The oxygen atoms are arranged into two $\text{O}_2^{2-}$ dimers, each oriented parallel to the $c$-axis and separated by lithium layers. Within this structure, the lithium ions are symmetrically coordinated between the $\text{O}_2^{2-}$ dimers, stabilizing the crystal in a layered arrangement where each dimer is aligned perpendicular to the basal plane, forming a hexagonal close-packed framework characteristic of the $\text{P6}_3/\text{mmc}$ space group. The symmetry inequivalent Wyckoff positions are summarized in Table I.

Table II illustrates the convergence of NAO basis sets for bulk $\text{Li}_2\text{O}_2$ by comparing results obtained with different optimized basis sizes. These results are benchmarked against the converged plane-wave (PW) calculations at a 50 Ha cutoff, representing the converged-basis

![](./images/1078327795207110680_1.jpg)

FIG. 1. Schematic representation of the structure of bulk $Li_2O_2$ with the $P6_3/mmc$ symmetry (Föppl's structure, [32]). (a) Lateral view. Numbers at the left represent the ordering of the layers along the $z$-direction. (b) Top view. Numbers written on the spheres make reference to the layer that a given atom occupies, according to the ordering given in panel (a). Li (respectively O) atoms are represented by green (respectively red) spheres.

TABLE II: Structural properties of bulk $Li_2O_2$ in the hexagonal $P6_3/mmc$ space group. $a$, $b$, and $c$ refers to the length of the three lattice vectors of the conventional unit cell (in Å). $\alpha$, $\beta$, and $\gamma$ represent the angles between the three lattice vectors. $z(\text{O})$ stands for the $z$-coordinate of the O atom in the Wyckoff positions, according to Table I, given in reduced coordinates. $d_{\text{OO}}$ is the oxygen-oxygen distance inside the $O_2^{2-}$ dimers (in Å). DZP, TZP, and TZDP stands for double-$\zeta$ polarized, triple-$\zeta$ polarized, and triple-$\zeta$ double polarized, respectively. PW stands for a plane wave calculation carried out with the ABINIT code, with a cutoff of 50 Ha. The experimental geometry is taken from Ref. [32]

<table>
  <thead>
    <tr>
      <th>Basis set</th>
      <th>$a$</th>
      <th>$b$</th>
      <th>$c$</th>
      <th>$\alpha$</th>
      <th>$\beta$</th>
      <th>$\gamma$</th>
      <th>$z(\text{O})$</th>
      <th>$d_{\text{OO}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DZP</td>
      <td>3.1593</td>
      <td>3.1593</td>
      <td>7.6651</td>
      <td>$90^\circ$</td>
      <td>$90^\circ$</td>
      <td>$120^\circ$</td>
      <td>0.6484</td>
      <td>1.557</td>
    </tr>
    <tr>
      <td>TZP</td>
      <td>3.1589</td>
      <td>3.1589</td>
      <td>7.6670</td>
      <td>$90^\circ$</td>
      <td>$90^\circ$</td>
      <td>$120^\circ$</td>
      <td>0.6488</td>
      <td>1.552</td>
    </tr>
    <tr>
      <td>TZDP</td>
      <td>3.1582</td>
      <td>3.1582</td>
      <td>7.6610</td>
      <td>$90^\circ$</td>
      <td>$90^\circ$</td>
      <td>$120^\circ$</td>
      <td>0.6488</td>
      <td>1.550</td>
    </tr>
    <tr>
      <td>PW</td>
      <td>3.1579</td>
      <td>3.1579</td>
      <td>7.6840</td>
      <td>$90^\circ$</td>
      <td>$90^\circ$</td>
      <td>$120^\circ$</td>
      <td>0.6496</td>
      <td>1.543</td>
    </tr>
    <tr>
      <td>Expt.</td>
      <td>3.1420</td>
      <td>3.1420</td>
      <td>7.6500</td>
      <td>$90^\circ$</td>
      <td>$90^\circ$</td>
      <td>$120^\circ$</td>
      <td>0.6510</td>
      <td>1.515</td>
    </tr>
  </tbody>
</table>

limit, while keeping all other calculation parameters identical. It is essential to distinguish this converged-basis limit from PW calculations performed at lower cutoffs, which are commonly used in many studies. The converged PW calculations, where the primary sources of error stem from the exchange-correlation functional and the pseudopotentials, slightly overestimate the lattice parameters, with deviations of approximately $0.5\%$ for $a$ and $0.4\%$ for $c$, which are typical for the PBE functional. Although the convergence of NAO basis sets is not systematically achieved by simply increasing the basis size, the sequence of bases in Table II demonstrates clear convergence trends for the in-plane lattice constant and the internal coordinate of the oxygen atom controlling the oxygen-oxygen distance inside the $O_2^{2-}$ dimers.

## IV. ELECTRONIC STRUCTURE

The electronic band structure of bulk $Li_2O_2$ in the $P6_3/mmc$ symmetry at the relaxed structure for different basis set sizes is presented in Fig. 2. This structure is consistent with that of a predominantly ionic material. The band manifolds are largely well-separated and each has a distinct dominant character. In this system, the top of the valence band and the bottom of the conduction band are primarily of O $2p$ character, representing the highest occupied energy levels and the lowest unoccupied levels of an oxygen dimer.

Indeed, the band structure depicted in Fig. 2 strongly resembles that of the molecular orbitals of the oxygen dimer. In a purely ionic model, the two Li atoms transfer their $2s$ electrons to the oxygen atoms, resulting in the formation of a $O_2^{2-}$ peroxide ion. The atomic orbitals of the oxygen atoms then hybridize to create the molecular orbitals of the dimer, as illustrated in Fig. 3. The $p_x$, $p_y$, and $p_z$ orbitals of the two oxygen atoms combine to produce six molecular orbitals, ordered by increasing energy as follows: (i) A bonding $\sigma_g$ orbital,

$$
\sigma_g = \frac{1}{\sqrt{2}} \left( p_z^{(1)} - p_z^{(2)} \right), \tag{1}
$$

a symmetric linear combination of the $p_z$ orbitals. (ii) Two degenerate bonding $\pi_u$ orbitals,

$$
\pi_u[y] = \frac{1}{\sqrt{2}} \left( p_y^{(1)} + p_y^{(2)} \right), \tag{2}
$$

symmetric combinations of the $p_y$ (or $p_x$) orbitals. (iii) Two degenerate antibonding $\pi_g^*$ orbitals,

$$
\pi_g^*[y] = \frac{1}{\sqrt{2}} \left( p_y^{(1)} - p_y^{(2)} \right), \tag{3}
$$

antisymmetric combinations of the $p_y$ (or $p_x$) orbitals. (iv) An antibonding $\sigma_u^*$ orbital,

$$
\sigma_u^* = \frac{1}{\sqrt{2}} \left( p_z^{(1)} + p_z^{(2)} \right), \tag{4}
$$

an antisymmetric linear combination of the $p_z$ orbitals.

Each oxygen atom contributes with four $p$ electrons, which, combined with the two electrons transferred from the Li atoms, totals ten electrons. These electrons occupy the five lowest-energy molecular orbitals, filling them completely (below the Fermi energy). Since this is a closed shell structure, no spin-polarized calculations are justified.

The analogy between bands and molecular orbitals would be established as follows: first, the molecular orbital $\sigma_g$ corresponds to the band manifold between -6 and -4 eV, the degenerate $\pi_u$ orbitals map to the band manifold spanning -5 to -3 eV, and the degenerate $\pi_g^*$

![](./images/1078327795207110680_2.jpg)

FIG. 2: Left panels: Electronic band structure of bulk $Li_2O_2$ with $P6_3/mmc$ symmetry at the relaxed structure (see Table II) for various basis set sizes. Black lines show the bands calculated with siesta for (a) DZP, (b) TZP, and (c) TZDP basis sets. Blue lines correspond to the bands obtained using ABINIT with a converged plane wave cutoff of 50 Ha. The energy zero point is set to the top of the valence band in each case. The projected density of states is shown to the right of each band structure plot, with black lines indicating the total density of states. The projections onto the Li $2s$, Li $2p$, O $2s$, and O $2p$ orbitals are represented by orange, blue, magenta, and green lines, respectively.

orbitals align with the top of the valence band manifold. The unoccupied sixth molecular orbital, $\sigma_u^*$, corresponds to the lowest conduction band manifold.

The overall agreement between the siesta and ABINIT bands is excellent, particularly for the valence bands and the first conduction band manifold, where differences are minimal. With a DZP-quality basis [Fig. 2(a)], slight discrepancies appear in the conduction band manifold with Li $2p$ character, but these differences are resolved when the basis set quality is increased to TZP [Fig. 2(b)] or TZDP [Fig. 2(c)].

At energies above 6 eV from the top of the valence band, the bands shift to a dominant Li $2p$ character. The computed band gap, using the PBE functional, is direct at the $\Gamma$ point and measures 2.0 eV. This value is not directly comparable to the experimental value which, to our knowledge has not been measured, due to the well- known DFT band gap misfit. The experimental opti- cal spectrum shows an absorption onset around 3.3 eV although this low-energy features are associated to ex- citonic phenomena, as proven by Bethe-Salpeter simula- tions [35]. A more accurate estimation of the band gap it- self is obtained by an average of $G_0W_0$ and self-consistent GW calculations [2] that yields a value of 6.73 eV. In Fig. 4 we show the $Li_2O_2$ band structure as calculated with the HSE06 functional [36], recently implemented in siesta [15]. We can see that, while the qualitative shape of the bands is very similar to those obtained with PBE, Fig. 2, the band gap is significantly increased to 4.18 eV although it is still smaller than the reference 6.73 eV, which can be obtained when the Hartree-Fock mixing parameter is increased from the 0.25 value in HSE06 to 0.48 [2].

## V. WANNIERIZATION

### A. Projection on atomic-like orbitals

In the previous section, we calculated the band struc- ture of bulk $Li_2O_2$ using three optimized basis sets: DZP, TZP, and TZDP, which correspond to 76, 96, and 128 or- bitals per unit cell, respectively. Diagonalizing the Kohn- Sham Hamiltonian yields the same number of bands per $k$-point in the first Brillouin zone, spanning from deeply localized semicore Li orbitals to numerous conduction band orbitals.

In many studies, it is advantageous to focus on the electronic states at the top of the valence band and the bottom of the conduction band, as these states are most relevant for capturing the underlying physics. Such an approach is particularly useful for investigating exci- tonic effects [35] or electron and hole polarons [8]. Here, this method provides insights into the strong electron- vibration coupling within the $O_2^{2-}$ ions.

A powerful way to address this problem is to con-

![](./images/1078327795207110680_3.jpg)

FIG. 3: Diagram of the molecular orbitals of the $O_2$ dimer and the atomic orbitals from which they are derived.

struct a basis of localized, orthogonal Wannier functions [12, 37], which offer a minimal and efficient representation of the bands of interest. These functions not only simplify the Hamiltonian for electronic structure analysis but also enable second-principles methods [11]. The SCALE-UP code incorporates these methods, leveraging symmetry to compute electron-lattice and electron-electron corrections within the simplified Hamiltonian in the Wannier basis. To ensure model accuracy, it is crucial for the Wannier basis to preserve the system's symmetry.

For this reason, we chose "maximally projected Wannier functions" rather than the conventional maximally localized Wannier functions [37]. These functions are created by projecting Bloch states onto atomic orbitals (used as initial guess functions) without minimizing the spread functional, as implemented in the WANNIER90 code [38]. Given that both the valence band maximum and conduction band minimum are dominated by O 2p character (see Fig. 2), it is logical to use the twelve p-type atomic orbitals in the unit cell (three per oxygen atom for the four oxygen atoms).

![](./images/1078327795207110680_4.jpg)

FIG. 4: Electronic band structure of bulk $Li_2O_2$ with P6$_3$/mmc symmetry obtained with SIESTA with the PBE functional (black lines) and the HSE06 hybrid functional with a percentage of exact exchange of 25 %. The quality of the basis set has been fixed to TZP.

![](./images/1078327795207110680_5.jpg)

FIG. 5: Representation of Wannier functions obtained by projecting Bloch orbitals onto the numerical basis orbitals of SIESTA for the Oxygen atom with p-symmetry: (a) for $p_y$, (b) for $p_z$, and (c) for $p_x$. Meaning of the balls as in Fig. 1.

Figure 5 shows the Wannier functions derived using this approach. The $p_x$ and $p_y$ orbitals, which are symmetry-equivalent in the P6$_3$/mmc space group, closely resemble p-orbitals of a hydrogen-like atom, except for small nodes near neighboring Li atoms, ensuring orthogonality with adjacent Wannier functions.

In contrast, the $p_z$-like functions, which align along the O-O bond direction in the $O_2^{2-}$ dimers, exhibit a significantly different chemical environment. Here, the changes in the localized functions due to the inter-orbital orthog-

onality condition are larger, due to the stronger overlap between $p_z$ functions and, as a result, they no longer resemble atomic orbitals as closely. These Wannier or- bitals, while showing the characteristic node of the $2p$ orbitals on the atom they are centered on, also display a lobe over the opposite O-atom in the dimer. The outer lobe, pointing away from the $O_{2}^{2-}$ dimer, is larger than the inner one, possibly reflecting on small orbital contri- butions to the wavefunction from the surrounding $Li^{+}$. The orbitals in this quasi-atomic representation are very compact with spreads of 0.75 and $0.85 \AA^{2}$ for $\pi(p_{x}, p_{y})$ and $\sigma(p_{z})$ orbitals, respectively. We have checked that these values are quite stable and do not change signifi- cantly with the quality of the basis set employed during their calculation.

### B. Projection on molecular orbitals

In the previous localization scheme all the Bloch bands with a majority weight on the oxygen $2p$ bands were mixed together in the unitary transformation that yields to the Wannier functions to provide the most compact or- bitals that describe these bands. However, this method also forces the use of all oxygen bands (twelve functions per primitive cell), and all their inter-orbital interactions, when creating a reduced model. Given that the bands of Fig. 2 associated to each of the molecular orbitals of the $O_{2}^{2-}$ ion do not cross each other they can be Wannierized individually. This means that the bands with $\sigma_{g}$ (two), $\pi_{u}$ (four), $\pi_{g}^{*}$ (four), and $\sigma_{u}^{*}$ (two) character can each be treated separately, reducing the number of bands in the electronic structure model and significantly limiting the number of inter-orbital matrix elements. For example, a Wannier model for electron polarons would require only $\sigma_{u}^{*}$ bands, while a model for hole polarons would require only $\pi_{g}^{*}$ bands. The resulting localized orbitals, illus trated in Fig. 6, have larger spreads than quasi-atomic orbitals: $1.60,1.29,1.49$, and $2.49 \AA^{2}$ for $\sigma_{g}, \pi_{u}, \pi_{g}^{*}$, and $\sigma_{u}^{*}$ bands, respectively. Bonding $\pi$-orbitals are more compact than both bonding and antibonding $\sigma$-orbitals, as well as antibonding $\pi$-orbitals. Among these, the an tibonding $\sigma$-orbitals are particularly diffuse. Compar ing panels (a) and (f) in Fig. 6 we can see that the main difference is that for the Wanniers coming from the $\sigma_{u}^{*}$ bands, outer lobes of the antibonding orbital are ex panded with respect to the former towards the $Li^{+}$ ions. This is a sensible result since these unoccupied orbitals are energetically close to the more dispersive band with Li character and take on some of their character. Thus we see that, while the character of the bands clearly corre- sponds to the molecular orbital diagram shown in Fig. 3, there are some differences with the idealized orbitals that are important to highlight. For example, close inspection of the $\pi$-type orbitals [Fig. 6(b)-6(e)], shows deformation from the ideal cylindrical-symmetry shape of a $2p$ orbital related to the presence of nearby $Li^{+}$ ions. Thus, while the main character of these orbitals is clearly molecular, their shape is clearly influenced by the embedding of the $O_{2}^{2-}$ ions in the solid and these small changes can, in turn, be important to describe other phenomena.

![](./images/1078327795207110680_6.jpg)

FIG. 6: Representation of Wannier functions associated to bands with marked molecular-orbital character. The (a)-(f) panels correspond, respectively, with Wannier or- bitals with strong $\sigma_{g}(p_{z}), \pi_{u}(p_{y}), \pi_{u}(p_{x}), \sigma_{u}^{*}(p_{z}), \pi_{g}^{*}(p_{y})$ and $\pi_{g}^{*}(p_{x})$ character.

### C. Electron-vibration coupling

We now turn our attention to examining how the one- electron Hamiltonian varies with the oxygen-oxygen dis- tance for the two Wannier function families discussed in the previous section. This is illustrated in Fig. 7, where panels (a) and (b) show the changes in the diagonal $(h_{aa})$ and off-diagonal $(h_{ab})$ elements, respectively, for quasi atomic Wannier functions, while panel (c) presents the variation of the diagonal matrix elements for molecular- type Wannier orbitals. Figure 7(a) shows that the self- energy of quasi-atomic Wannier orbitals with $p_{z}$ charac ter exhibits a strong dependence on the oxygen-oxygen distance in a dimer $(d_{OO})$, whereas the self-energy of the degenerate $p_{x}$ and $p_{y}$ orbitals shows a much weaker vari ation. This is likely due to the fact that $p_{x}$ and $p_{y^{-}}$ like orbitals are localized around only one atom of the dimer, whereas $p_{z}$-like orbitals have significant contribu tions centered on both atoms in the dimer (see Fig. 5) and exhibit rapid changes as the distance varies. Moreover, in the quasi-atomic representation, $p_{z}$ orbitals primar ily interact with each other to form the $\sigma$ bonding and antibonding bands, while $p_{x}$ and $p_{y}$ orbitals interact sim ilarly to generate the $\pi$ bands. These interactions give rise to new off-diagonal $h_{ab}$ parameters, representing the one-electron hamiltonian between Wannier functions a and b, which necessitate the simultaneous representation of both $\sigma$ (π) bonding and antibonding bands, making it impossible to separate them within this basis. At the

![](./images/1078327795207110680_7.jpg)

FIG. 7: Variation of the hamiltonian matrix elements in the Wannier basis with the change of oxygen-oxygen distance, $\Delta d_{\text{OO}}$, inside the $\text{O}_2^{2-}$ dimer. In (a) the change of self-energy ($\Delta h_{aa}$) of quasi-atomic $p_z$ (red) and $p_x/p_y$ orbitals (blue) with respect to the equilibrium position is presented. In (b), for the same basis, the interaction matrix element, $h_{ab}$, between $p_z(p_x/p_y)$ orbitals in the same $\text{O}_2^{2-}$ unit is presented in red(blue). Finally, in (c) the change of self-energy for Wannier functions with strong $\sigma_g$, $\pi_u$, $\pi_g^*$, and $\sigma_u^*$-like character with respect to the equilibrium distance is presented in red, blue, green and yellow, respectively.

equilibrium position, the $p_z$ interaction element is significantly larger (4.30 eV) than the $p_x/p_y$ element (-1.62 eV), consistent with the stronger $\sigma$ interactions compared to $\pi$ interactions. The variation of these elements with $d_{\text{OO}}$ is shown in Fig. 7(b), with red and blue representing the $p_z$ and $p_x/p_y$ orbitals, respectively. It can be observed that as the distance increases, the absolute value of the off-diagonal matrix elements decreases in both cases, ultimately approaching each other in the limit of infinite distance, where the interaction between the orbitals on each atom vanishes. Finally, Fig. 7(c) shows the variation of the self-energies in the molecular-Wannier basis, as described in Sec. V B. In this figure, we observe that the energies of the bonding orbitals (represented in red and blue for $\sigma$ and $\pi$ orbitals, respectively) decrease as the oxygen atoms move closer, while the opposite trend is seen for the antibonding orbitals (depicted in green and yellow for $\pi$ and $\sigma$ orbitals, respectively). Although one might initially expect the energy of the $\sigma$ orbitals to vary more rapidly than that of the $\pi$ orbitals, this is only true for the antibonding $\sigma$ level. The bonding $\sigma$ orbital, in contrast, exhibits a much slower variation. This slower variation arises from the $2s$-$2p$ hybridization, which affects the ordering of the $\sigma_g(p_z)$ and $\pi_u(p_x,p_y)$ molecular orbitals in homonuclear diatomic molecules across the series $\text{C}_2$, $\text{N}_2$, $\text{O}_2$, and $\text{F}_2$ [39]. This hybridization shifts much of the expected rapid variation of the primarily $\sigma_g(p_z)$ orbital to the deeper $\sigma_g$ orbital with significant $2s$ character. We also find, as expected, that only self-energies need to be described when describing the hamiltonian using a molecular-like basis.

Ultimately, we can observe that describing the variation of most Wannier Hamiltonian elements with a second-order polynomial, as shown in Fig. 7, produces accurate results. The curve where the error is larger is that corresponding to the $\sigma_u^*$ orbital where the changes in energy are larger. While the fit with a second-order polynomial clearly captures the order of magnitude and main tendencies of the curve, high-accuracy in the range -0.2 to 0.2 Å can only be achieved using a third-order polynomial. This is highly promising for developing models that incorporate precise electron-vibration interactions in this system. Notably, the results presented here clarify why, in previous calculations of the hole polaron [8], the O-O bond distance decreases—due to the removal of an antibonding electron—while for the electron polaron, where an electron is added to the $\sigma$ antibonding orbital, the O-O bond distance increases significantly. Thus, adopting a molecularly inspired Wannier basis appears to be the most suitable approach for constructing reduced models to simulate polaron motion dynamics on a large scale using second-principles. This basis is smaller and more flexible, focusing on describing only the HOMO- and LUMO-type bands (or either one), and its parameters offer a clearer and simpler physical interpretation compared to those of quasi-atomic Wannier functions. While quasi-atomic Wannier functions can sometimes be more compact, the molecularly inspired basis provides distinct advantages in interpretability and adaptability.

## VI. CONCLUSIONS

In this work, we have comprehensively investigated the structural and electronic properties of bulk lithium peroxide, a key material in lithium-air battery technologies. Our study leveraged density functional theory and second-principles approaches to provide insights into the lattice structure, electronic band structure, and electron-lattice coupling in this material.

The structural analysis was carried out for the $\text{P6}_3/\text{mmc}$ hexagonal symmetry, that provides a stable framework for $\text{Li}_2\text{O}_2$, characterized by well-defined oxygen dimers and symmetrically coordinated lithium ions. Electronic structure calculations revealed that the valence and conduction bands are dominated by oxygen $2p$ states, which exhibit clear correspondence to the molec-

ular orbitals of the peroxide ion. The results obtained with a basis set of numerical atomic orbitals of triple- zeta polarized quality present good agreement with those obtained with a converged plane-wave basis set. The cal- culated band gap, while underestimated using standard DFT, aligns qualitatively with the known insulating na- ture of $Li_{2} O_{2}$ .

Our Wannierization approach successfully localized the electronic states into both atomic-like and molecular- like Wannier functions, with the latter offering a more chemically intuitive description of the bands relevant for polaron formation and dynamics. By analyzing the variation of Hamiltonian elements in the Wannier basis as a function of geometry, we demonstrated the strong electron-phonon coupling in the system and its implica- tions for the behavior of polarons. Notably, the molec- ular Wannier basis provided an efficient and physically interpretable framework, particularly for understanding the structural changes associated with electron and hole polarons.

The findings presented here emphasize the utility of molecularly inspired Wannier functions for constructing reduced models that accurately capture the dynamics of polarons and electron-vibration interactions in $Li_{2} O_{2}$ . Such models are crucial for large-scale simulations of charge transport and could inform the design of next- generation lithium-air batteries.

## VII. ACKNOWLEDGEMENTS

P.M.M., E.J.T., P.V.K.R, B. M., and V. S. ac- knowledge financial support from Erasmus+ KA-107 action and the Vice-rectorate for Internationalisation and Global Engagement of the University of Cantabria. T.F.R., N.C.S, P.G.F, and J.J. acknowledge financial support from Grant No. PID2022-139776NB-C63 funded by MCIN/AEI/10.13039/501100011033 and by ERDF "A way of making Europe" by the European Union. T.F.R. acknowledges financial support from Ministerio de Ciencia, Innovación y Universidades (Grant PRE2019-089054). N.C.S. acknowledges financial support from "Concepción Arenal" Grant No. BDNS:524538 of the University of Cantabria funded by the Government of Cantabria.

[1] P. Albertus, G. Girishkumar, B. McCloskey, R. S. Sánchez-Carrera, B. Kozinsky, J. Christensen, and A. C. Luntz, Identifying capacity limitations in the Li/Oxygen battery using experiments and modeling, J. Electrochem. Soc. 158, A343 (2011).

[2] M. D. Radin and D. J. Siegel, Charge transport in lithium peroxide: relevance for rechargeable metal-air batteries, Energy Environ. Sci. 6, 2370 (2013).

[3] F. Tian, M. D. Radin, and D. J. Siegel, Enhanced charge transport in amorphous $Li_{2} O_{2}$ , Chem. Mater. 26, 2952(2014).

[4] P. G. Bruce, S. A. Freunberger, L. J. Hardwick, and J.- M. Tarascon, $Li-O_{2}$ and $Li-S$ batteries with high energy storage, Nat. Mater. 11, 19 (2012).

[5] A. Akhter Naqvi, Z. Awan, A. A. Shaikh, F. Ab, F. Raza, and I. Ahad, Aprotic lithium air batteries with oxygen-selective membranes, Mater. Renew. Sustain Energy 11(2022).

[6] B. P. Sousa, C. G. Anchieta, T. M. C. Nepel, A. R. Neale, L. J. Hardwick, R. M. Filho, and G. Doubek, Exploring carbon electrode parameters in $Li-O_{2}$ cells: $Li_{2} O_{2}$ and $Li_{2} CO_{3}$ formation, J. Mater. Chem. A 12, 7215 (2024).

[7] M. D. Radin, F. Tian, and D. J. Siegel, Electronic struc-ture of $Li_{2} O_{2} 0001$ surfaces, J. Mater. Sci. 47, 7564(2012).

[8] J. M. García-Lastra, J. S. G. Myrdal, R. Christensen, K. S. Thygesen, and T. Vegge, DFT + U study of pola- ronic conduction in $Li_{2} O_{2}$ and $Li_{2} CO_{3}$ : Implications for Li-Air batteries, J. Phys. Chem. C 117, 5568 (2013).

[9] S. P. Ong, Y. Mo, and G. Ceder, Low hole polaron migra-tion barrier in lithium peroxide, Phys. Rev. B 85, 081105(2012).

[10] W. H. Sio, C. Verdi, S. Poncé, and F. Giustino, Ab initio theory of polarons: Formalism and applications, Phys. Rev. B 99, 235139 (2019).

[11] P. García-Fernández, J. C. Wojdeł, J. Íñiguez, and J. Junquera, Second-principles method for materials sim- ulations including electron and lattice degrees of freedom, Phys. Rev. B 93, 195137 (2016).

[12] N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, andD. Vanderbilt, Maximally localized wannier functions:Theory and applications, Rev. Mod. Phys. 84, 1419(2012).

[13] P. Hohenberg and W. Kohn, Inhomogeneous electron gas, Phys. Rev. 136, B864 (1964).

[14] J. M. Soler, E. Artacho, J. D. Gale, A. García, J. Jun- quera, P. Ordejón, and D. Sánchez-Portal, The SIESTA method for ab initio order-N materials simulation, J. Phys.: Condens. Matter 14, 2745 (2002).

[15] A. García, N. Papior, A. Akhtar, E. Artacho, V. Blum, E. Bosoni, P. Brandimarte, M. Brandbyge, J. I. Cerdá, F. Corsetti, R. Cuadrado, V. Dikan, J. Ferrer, J. Gale, P. García-Fernández, V. M. García-Suárez, S. García, G. Huhs, S. Illera, R. Korytár, P. Koval, I. Lebedeva, L. Lin, P. López-Tarifa, S. G. Mayo, S. Mohr, P. Or- dejón, A. Postnikov, Y. Pouillon, M. Pruneda, R. Rob- les, D. Sánchez-Portal, J. M. Soler, R. Ullah, V. W.-Z. Yu, and J. Junquera, SIESTA: Recent developments and applications, J. Chem. Phys. 152 (2020).

[16] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett.77, 3865 (1996).

[17] M. A. Marques, M. J. Oliveira, and T. Burnus, LIBXC: A library of exchange and correlation functionals for densityfunctional theory, Comput. Phys. Commun. 183, 2272(2012).

[18] S. Lehtola, C. Steigemann, M. J. Oliveira, and M. A. Marques, Recent developments in LIBXC-a comprehen-

sive library of functionals for density functional theory, SoftwareX 7, 1 (2018).

[19] L. Kleinman and D. M. Bylander, Efficacious form for model pseudopotentials, Phys. Rev. Lett. 48, 1425 (1982).

[20] D. Hamann, Optimized norm-conserving Vanderbilt pseudopotentials, Phys. Rev. B 88, 085117 (2013).

[21] A. García, M. J. Verstraete, Y. Pouillon, and J. Junquera, The PSML format and library for norm-conserving pseu- dopotential data curation and interoperability, Comput. Phys. Commun. 227, 51 (2018).

[22] M. Van Setten, M. Giantomassi, E. Bousquet, M. J. Ver- straete, D. R. Hamann, X. Gonze, and G.-M. Rignanese, The PSEUDODOJO: Training and grading a 85 element optimized norm-conserving pseudopotential table, Com- put. Phys. Commun. 226, 39 (2018).

[23] The scalar relativistic ONCVPSP v0.4.1 pseudopotentials with stringent accuracy were used.

[24] O. F. Sankey and D. J. Niklewski, Ab initio multicenter tight-binding model for molecular-dynamics simulations and other applications in covalent systems, Phys. Rev. B 40, 3979 (1989).

[25] E. Artacho, D. Sánchez-Portal, P. Ordejón, A. García, and J. M. Soler, Linear-scaling ab-initio calculations for large and complex systems, Phys. Stat. Sol. (b) 215, 809 (1999).

[26] J. Junquera, O. Paz, D. Sánchez-Portal, and E. Artacho, Numerical atomic orbitals for linear-scaling calculations, Phys. Rev. B 64, 235111 (2001).

[27] H. J. Monkhorst and J. D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13, 5188 (1976).

[28] X. Gonze, B. Amadon, P.-M. Anglade, J.-M. Beuken, F. Bottin, P. Boulanger, F. Bruneval, D. Caliste, R. Cara- cas, M. Côté, T. Deutsch, L. Genovese, P. Ghosez, M. Gi- antomassi, S. Goedecker, D. Hamann, P. Hermet, F. Jol- let, G. Jomard, S. Leroux, M. Mancini, S. Mazevet, M. Oliveira, G. Onida, Y. Pouillon, T. Rangel, G.-M. Rignanese, D. Sangalli, R. Shaltaf, M. Torrent, M. Ver- straete, G. Zerah, and J. Zwanziger, ABINIT: First- principles approach to material and nanosystem prop- erties, Comput. Phys. Commun. 180, 2582 (2009).

[29] X. Gonze, F. Jollet, F. Abreu Araujo, D. Adams, B. Amadon, T. Applencourt, C. Audouze, J.-M. Beuken, J. Bieder, A. Bokhanchuk, E. Bousquet, F. Bruneval, D. Caliste, M. Côté, F. Dahm, F. Da Pieve, M. Delaveau, M. Di Gennaro, B. Dorado, C. Es- pejo, G. Geneste, L. Genovese, A. Gerossier, M. Gi- antomassi, Y. Gillet, D. Hamann, L. He, G. Jomard, J. Laflamme Janssen, S. Le Roux, A. Levitt, A. Lher- bier, F. Liu, I. Lukačević, A. Martin, C. Martins, M. Oliveira, S. Poncé, Y. Pouillon, T. Rangel, G.-M. Rig- nanese, A. Romero, B. Rousseau, O. Rubel, A. Shukri, M. Stankovski, M. Torrent, M. Van Setten, B. Van Tro- eye, M. Verstraete, D. Waroquiers, J. Wiktor, B. Xu, A. Zhou, and J. Zwanziger, Recent developments in the ABINIT software package, Comput. Phys. Commun. 205, 106 (2016).

[30] X. Gonze, B. Amadon, G. Antonius, F. Arnardi, L. Baguet, J.-M. Beuken, J. Bieder, F. Bottin, J. Bouchet, E. Bousquet, N. Brouwer, F. Bruneval, G. Brunin, T. Cavignac, J.-B. Charraud, W. Chen, M. Côté, S. Cottenier, J. Denier, G. Geneste, P. Ghosez, M. Giantomassi, Y. Gillet, O. Gingras, D. R. Hamann, G. Hautier, X. He, N. Helbig, N. Holzwarth, Y. Jia, F. Jollet, W. Lafargue-Dit-Hauret, K. Lejaeghere, M. A. Marques, A. Martin, C. Martins, H. P. Miranda, F. Nac- carato, K. Persson, G. Petretto, V. Planes, Y. Pouil- lon, S. Prokhorenko, F. Ricci, G.-M. Rignanese, A. H. Romero, M. M. Schmitt, M. Torrent, M. J. van Setten, B. Van Troeye, M. J. Verstraete, G. Zérah, and J. W. Zwanziger, The ABINIT project: Impact, environment and recent developments, Comput. Phys. Commun. 248, 107042 (2020).

[31] F. Fehér, I. Von Wilucki, and G. Dost, Beiträge zur Kenntnis des Wasserstoffperoxyds und seiner Derivate, VII. Mitteil.: Über die Kristallstruktur des Lithiumperoxyds, $Li_2O_2$, Chem. Ber. 86, 1429 (1953).

[32] H. Föppl, Die Kristallstrukturen der Alkaliperoxyde, Z. Anorg. Allg. Chem. 291, 12 (1957).

[33] M. K. Y. Chan, E. L. Shirley, N. K. Karan, M. Bala- subramanian, Y. Ren, J. P. Greeley, and T. T. Fister, Structure of lithium peroxide, J. Phys. Chem. Lett. 2, 2483 (2011).

[34] L. G. Cota and P. de la Mora, On the structure of lithium peroxide, $Li_2O_2$, Acta Crystallogr. B61, 133 (2005).

[35] J. M. García-Lastra, J. D. Bass, and K. S. Thygesen, Communication: Strong excitonic and vibronic effects determine the optical properties of $Li_2O_2$, J. Chem. Phys. 135, 121101 (2011).

[36] A. V. Krukau, O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, Influence of the exchange screening parame- ter on the performance of screened hybrid functionals, J. Chem. Phys. 125, 224106 (2006).

[37] N. Marzari and D. Vanderbilt, Maximally localized gen- eralized wannier functions for composite energy bands, Phys. Rev. B 56, 12847 (1997).

[38] G. Pizzi, V. Vitale, R. Arita, S. Blügel, F. Freimuth, G. Géranton, M. Gibertini, D. Gresch, C. Johnson, T. Koretsune, J. Ibañez-Azpiroz, H. Lee, J.-M. Lihm, D. Marchand, A. Marrazzo, Y. Mokrousov, J. I. Mustafa, Y. Nohara, Y. Nomura, L. Paulatto, S. Poncé, T. Pon- weiser, J. Qiao, F. Thöle, S. S. Tsirkin, M. Wierzbowska, N. Marzari, D. Vanderbilt, I. Souza, A. A. Mostofi, and J. R. Yates, Wannier90 as a community code: new fea- tures and applications, J. Phys.: Condens. Matter 32, 165902 (2020).

[39] P. Atkins, J. de Paula, and J. Keeler, Physical Chemistry (Oxford University Press, 2018).