# Structure, Metastability, and Electron Density of Al Lattices in Light of the Model of Anions in Metallic Matrices

M. Marqués, M. Flórez, and J. M. Recio*
Departamento de Química Física y Analítica, Universidad de Oviedo, E-33006 Oviedo, Spain

D. Santamaría and A. Vegas
Instituto de Química Física Rocasolano, CSIC, E-28006 Madrid, Spain

V. García Baonza
Departamento de Química Física, Universidad Complutense de Madrid, E-28040 Madrid, Spain

Received: June 21, 2006

This paper reports a theoretical investigation of the structure, stability, and electron charge density of cubic, rhombohedral, hexagonal, and monoclinic Al lattices. The equations of state and the elastic constants are computed from total energy calculations at different volumes and unit cell strains using the density functional theory approximation. The topology of the electron density is analyzed within the crystalline implementation of the atoms in molecules formalism. The results are discussed in light of the so-called anions in metallic matrices model, which permits the interpretation of the chemical bonding and the explanation of the existence of particular symmetries of inorganic crystals. First, the Al sublattices are identified as the reference building blocks of $AlX_3$ ($X = F, Cl, OH$) compounds. The calculations reveal that the equilibrium zero-pressure $Al-Al$ shortest distance is around $2.75$ Å in all of the Al matrixes, similar to the value observed in the stable face centered cubic structure of Al at room conditions. Second, at their zero-pressure equilibrium geometries, the Al sublattices are found to fulfill the mechanical stability criteria or, alternatively, to show mechanical instabilities that are compatible with the distortions observed for the structures in $AlX_3$ crystals. However, at the equilibrium volumes of the $AlX_3$ crystals, all of the Al matrices violate the spinodal condition, and the cohesion and stabilization are provided by the nonmetallic $X$ atoms. Third, the structural anisotropy of the Al sublattices seems to be the main factor to discriminate metallic matrices able to host nonmetallic elements. The inhomogeneities of the electron charge density, which favor the arrival of nonmetallic elements and the crystal formation, are notably enhanced in passing from the fcc structure of pure Al to the less isotropic Al matrices observed in $AlX_3$ compounds.

## I. Introduction

The physics and chemistry of crystalline solids can be often understood in terms of the nature and geometry of their bonding network. On the grounds of this strong correlation between properties of materials and their structure and bonding, crystal chemistry has emerged as its own area of research with applications in many other scientific fields.¹ For example, in high-pressure mineralogy, trends based on the examination of Pauling's rules and atomic sizes along a number of minerals are able to provide successful quantitative analyses, even with a predictive character, of the compressibilities and phase transformations of materials of the Earth's interior.² A central concept of this approach is that of coordination polyhedra, which originates from the traditional description of a crystal structure as an anionic sublattice with interstices partially or totally occupied by cations.³ This traditional view meets, however, several difficulties related to the impossibility of accounting for the variable coordinations that cations exhibit in different compounds or the explanation of the underlying reasons for the presence of a particular structure in the temperature- or pressure-induced polymorphic sequence of a given material. New developments in the study of both, chemical bonding formalisms and models of crystal structures, become therefore necessary to provide a better insight into the properties and behavior of inorganic solids under variable thermodynamic and chemical conditions.

Theoretical and phenomenological studies point toward the metal sublattice as the fundamental building block of crystalline structures containing metallic elements. On the one hand, analyses of the topology of the electron charge density in these materials, by means of the atoms in molecules theory (AIM)⁴,⁵ and the electron localization function (ELF),⁶,⁷ reveal the existence of inhomogeneities in the electron density maps of metals that can be associated with the actual positions of the nonmetallic atoms in the lattice.⁸,⁹ On the other hand, empirical evidence identifies structural similarities between the structures of metal sublattices in inorganic crystals and the structures exhibited by pure metals at different thermodynamic conditions.¹⁰⁻¹³ Along these lines, we have recently presented a far-reaching model that provides a rational interpretation of the particular structures shown by this kind of crystalline solid and overcomes some limitations of the previous views.¹⁴

10.1021/jp063883a CCC: $33.50 © 2006 American Chemical Society
Published on Web 08/25/2006

<table>
<caption>TABLE 1: Al Lattices Considered in This Work (See Text) [$V_{\text{exp}}$(Al) Refers to the Room Condition Experimental Volume of the Pure Al fcc Structure and Al Sublattices in $\text{Al}X_3$ Crystals (Al:$\text{Al}X_3$), and $d_{\text{exp}}$($\text{Al}–\text{Al}$) Refers to the $\text{Al}–\text{Al}$ Shortest Distance in These Systems]</caption>
<thead>
<tr>
<th></th>
<th>space group</th>
<th>Al positions</th>
<th>cell angle (deg)</th>
<th>remarks</th>
<th>$d_{\text{exp}}$($\text{Al}–\text{Al}$) (Å)</th>
<th>$V_{\text{exp}}$(Al) (Å³)</th>
<th>connectivity</th>
</tr>
</thead>
<tbody>
<tr>
<td>fcc</td>
<td>$R\overline{3}$</td>
<td>$1(a)$ (0, 0, 0)</td>
<td>60</td>
<td>RC</td>
<td>2.86ª</td>
<td>16.573ª</td>
<td>12</td>
</tr>
<tr>
<td>sc</td>
<td>$R\overline{3}$</td>
<td>$1(a)$ (0, 0, 0)</td>
<td>90</td>
<td>Al:$\alpha\text{-AlF}_3$</td>
<td>3.52ᵇ</td>
<td>43.67ᵇ</td>
<td>6</td>
</tr>
<tr>
<td>bcc</td>
<td>$R\overline{3}$</td>
<td>$1(a)$ (0, 0, 0)</td>
<td>109.47</td>
<td>HP</td>
<td></td>
<td></td>
<td>8</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$2(c)$ (¹/₄, ¹/₄, ¹/₄)</td>
<td>90</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>gra-a</td>
<td>$R\overline{3}$</td>
<td>$2(c)$ (¹/₃, ¹/₃, ¹/₃)</td>
<td>free</td>
<td></td>
<td></td>
<td></td>
<td>4</td>
</tr>
<tr>
<td>hcp</td>
<td>$P6_3/mmc$</td>
<td>$2(c)$ (¹/₃, ²/₃, ¹/₄)</td>
<td></td>
<td>HP</td>
<td></td>
<td></td>
<td>12</td>
</tr>
<tr>
<td>spinel</td>
<td>$Fd\overline{3}m$</td>
<td>$16(d)$ (¹/₂, ¹/₂, ¹/₂)</td>
<td></td>
<td>Al:$\eta\text{-AlF}_3$</td>
<td>3.40ᶜ</td>
<td>55.69ᶜ</td>
<td>6</td>
</tr>
<tr>
<td>gra-e1</td>
<td>$P6/mmm$</td>
<td>$2(d)$ (¹/₃, ²/₃, ¹/₂)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
</tr>
<tr>
<td>gra-e</td>
<td>$P2_1/n$</td>
<td>$2 × 4(e)$ ($x, y, z$)</td>
<td></td>
<td>Al:$\text{Al(OH)}_3$</td>
<td>2.93ᵈ</td>
<td>53.50ᵈ</td>
<td>3</td>
</tr>
<tr>
<td></td>
<td>$C2/m$</td>
<td>$4(g)$ (0, $y$, 0)</td>
<td></td>
<td>Al:$\text{AlCl}_3$</td>
<td>3.42ᵉ</td>
<td>89.08ᵉ</td>
<td>3</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="8">ª Reference 20. ᵇ Reference 21. ᶜ Reference 22. ᵈ Reference 23. ᵉ Reference 24.</td>
</tr>
</tfoot>
</table>

According to this anions in metallic matrices (AMM) model, the crystal structure of an inorganic compound containing metallic elements can be understood as a metallic matrix acting as a host lattice for the nonmetallic atoms, the formation and localization of the anions in the compound being driven by the geometric and electronic structures of the metallic sublattice. We have also provided a quantum mechanical verification of the main hypotheses of the AMM model by means of a detailed analysis of the calculated electron density distribution ($\rho$) of Al sublattices observed in $\text{Al}X_3$ ($X = \text{F, Cl, OH}$) crystals. As a main conclusion, the coordinates of the nonmetallic element were found to be close to zones of charge accumulation of the Al matrices, the final position of the $X$ element being also modulated by its electronegativity.

Several questions relative to the structure and metastability of the metallic arrays, the role of the nonmetallic elements, and the relationship of these aspects with the topology of the electron density of the metal need further clarification for a global quantum mechanical assessment of the AMM model. The importance of the metastability of the metallic matrixes is to be emphasized because a number of solid-state processes (progress of crystal formations, surface reconstructions, solid-state reactivity, or catalytic processes) might be described in a microscopic language taking these lattices as reference states. In all of these instances, the structure of the metallic matrix may be thought to evolve once the other atoms approach its surface or mix together to generate a new bulk material.

The aim of the present paper is twofold. First, we provide a thorough study of the structure and metastability of the crystallographic structures of Al observed in $\text{Al}X_3$ crystals (Al: $\text{Al}X_3$). This task involves first-principles calculations of total energy–volume curves, the evaluation of spinodal conditions, and the computation and examination of the dependence of elastic constants on the unit cell volume. Both unit cell volumes above and below the zero-pressure equilibrium geometries of the metallic sublattices are relevant as, on the one hand, the nonmetallic elements expand the metallic matrix upon crystal formation but, on the other hand, the $X$ elements localize the metallic electron density resembling the electron density of a compressed lattice.¹⁴,¹⁵ This discussion is pertinent to the analysis of the role of the same Al structures in $\text{Al}X_3$ crystals and to the identification of that of the $X$ elements in the stability of Al matrices. Second, we carry out an extensive analysis of the topology of $\rho$ to quantify the degree of inhomogeneity of the electron density of Al lattices. This allows us to identify distinctive features of different Al phases and to explore the connection between the inhomogeneity of $\rho$ and the structural anisotropy, thus completing the topological study presented in ref 14.

Accurate quantum mechanical calculations have been carried out within the framework of the density functional approximation using standard VASP¹⁶ and CRYSTAL packages,¹⁷ whereas equation of state fittings have been performed by means of the GIBBS code.¹⁸ Specifically, we have optimized the unit cell geometries at different volumes and unit cell strains of the following Al lattices: fcc ($Fm\overline{3}m$), bcc ($Im\overline{3}m$), hcp ($P6_3/mmc$), simple cubic ($Pm\overline{3}m$), rhombohedral ($R\overline{3}$), spinel ($Fd\overline{3}m$), eclipsed graphitic ($P6/mmm$), alternated graphitic ($R\overline{3}$), and monoclinic ($C2/m$ and $P2_1/n$), as well as the $\alpha\text{-AlF}_3$ ($R\overline{3}c$) and the hypothetical $\alpha\text{-AlCl}_3$ ($R\overline{3}c$) crystals. The topological analysis of the electron density has been carried out within the AIM formalism⁴ using the CRITIC code.¹⁹ Only the crystalline wave functions of the metal sublattices have been considered.

The paper is divided into three more sections. In the next one, we describe the unit cells of Al structures in relation to Al:$\text{Al}X_3$ sublattices and detail computational aspects concerning the calculation of total energy, equations of state, and elastic constants, as well as the analysis of the electron density of Al polymorphs considered in this work. The results are discussed in section III. The first four subsections contain general and particular analyses of the structure and metastability of the different crystal symmetries. The last subsection includes new results from our study of the topology of the electron density of Al lattices. The paper ends with a summary of the main conclusions and some prospects for future work.

### II. Computational Aspects

#### A. Crystal Description.
In Table 1 we describe the Al lattices considered in this work. The fcc one corresponds to the thermodynamic stable structure of this metal at room condition (RC),²⁰ whereas the hexagonal compact packing (hcp) and the body centered cubic (bcc) ones appear in the calculated pressure-induced polymorphic sequence of Al at room temperature (high-pressure (HP) phases).²⁵,²⁶ With the exception of the ideal graphitic-like alternate (gra-a) lattice, the other structures included in the table have been experimentally observed (slightly distorted in most cases) as Al sublattices in $\text{Al}X_3$ crystals. The simple cubic (sc) one is found in $\alpha\text{-AlF}_3$ with a slight rhombohedral distortion, the actual cationic array in this crystal having the $R\overline{3}$ symmetry ($\alpha = 88.84^\circ$).²¹ The cubic spinel one (spinel) appears in $\eta\text{-AlF}_3$,²² and the hexagonal structure with the $P6/mmm$ space group (gra-e1) can be seen as a first approach to the Al-eclipsed graphitic-like sublattices found in various phases of $\text{Al(OH)}_3$ (ref 23) and in $\text{AlCl}_3$ (ref 24), although the actual Al structure in these crystals is monoclinic ($C2/m$ and $P2_1/n$ (almost $C2/m$) space groups for $\text{AlCl}_3$ and the gibbsite structure of $\text{Al(OH)}_3$, respectively; gra-e in Table 1).

### Al Lattices
As shown in the table, the fcc, bcc, and sc lattices can be described with the same rhombohedral $R\overline{3}$ space group using different cell angles and with Al multiplicity equal to 1. We will use this $R\overline{3}$ common cell to analyze the volume dependence of the (rhombohedral) transformation path connecting these structures in relation to the analysis of the sc lattice metastability (see subsection III.B). A similar study is done for the bcc and gra-a Al lattices, which can be described with the same $R\overline{3}$ space group but with Al multiplicity equal to 2 and using different cell angles and Al positions (see Table 1).

The Al connectivity in the Al structures and $AlX_3$ crystals varies between 3 (or $3+2$, see below) (gra-e) and 12 (fcc and hcp), with a value of 6 for the sc and spinel lattices and 8 for the bcc one. The experimental $Al-Al$ distances in pure fcc Al and in $Al:AlX_3$ sublattices can be roughly grouped in two values. The first one, around $3.45$ Å (between the nearest and next nearest neighbor distances in pure Al fcc), is observed in the sc, spinel, and gra-e $(AlCl_3)$ lattices. The second one (about 20% lower) is observed in $Al(OH)_3$ and in Al fcc at RC. $^{20}$ The existence of these two different values cannot be totally rationalized using the atomic sizes of the nonmetallic elements (for example, similar $Al-Al$ distances are obtained in $\eta-AlF_3$ and $AlCl_3$). However, by taking also into account the Al connectivity and the ideas of two-center one-electron and two-center two-electron bonds of the AMM model, a satisfactory explanation of the observed $Al-Al$ distances in Al polymorphs and $AlX_3$ crystals was provided. $^{14}$

### B. Total Energy and Equations of State.
First-principles total energy calculations were performed within the formalism of the density functional theory (DFT) using a plane wave pseudopotential scheme as implemented in the VASP package. $^{16}$ The projector augmented wave (PAW) method was used to describe the electron-ion interaction. $^{27}$ Primarily, the Perdew−Wang generalized gradient (GGA) exchange correlation functional was employed. $^{28}$ In $AlX_3$ compounds, additional calculations were carried out within the local density approximation (LDA) with the exchange correlation potential of Ceperley and Alder. $^{29}$ All results relied on well-converged structures with respect to cutoff energy (301, 328, and 500 eV for $Al, AlCl_3$, and $AlF_3$ lattices, respectively) and $k$-point sampling. In particular, Brillouin zone integrals were approximated using the Monkhorst−Pack $k$-points generation scheme $^{30}$ with sufficiently dense meshes to guarantee an energy convergence of $10^{-5}$ eV. Special care was taken in the calculation of the elastic constants. In this sense, the number of $k$ points in the unreducible part of the Brillouin zone was increased to account for the lower symmetry of the strained structures.

For each lattice in Table 1, we calculated the total energy $(E)$ in a number of selected values of the volume $(V)$ ($E$ and $V$ mean the energy and volume per atom, respectively). This required the optimization of the $c/a$ ratio in the hexagonal lattices and that of the cell angle in the gra-a one. The analysis of the rhombohedral transformation connecting gra-a and bcc also required the optimization of the Al positions (one parameter) at each value of the $R\overline{3}$ cell angle. Finally, the $P2_1/n$ structure is described by 10 geometrical parameters (four cell constants and two types of Al (4e) $(x,y,z)$ positions (see Table 1)) and, then, the optimization of nine parameters is required at a given volume. All of the structure optimizations were performed via a conjugate−gradient minimization of the total energy using Methfessel−Paxton and Gaussian methods with smearings of $\sigma=0.3$ and $\sigma=0.1$ in Al an $AlX_3$ lattices, respectively. For the final calculation of the optimized crystal structures the tetrahedron method with Blöchl corrections was used.

The effect of hydrostatic pressure on the unit cell volume has been obtained by means of numerical and standard equations of state (EOS) fittings to the sets of computed $(E,V)$ points. $^{18}$ Vinet, $^{31}$ spinodal, $^{32,33}$ and Birch $^{34}$ EOS have been thoroughly used in this respect. In particular, the Vinet EOS has been used to provide bulk modulus versus volume $(B(V))$ and volume versus pressure $(V(p))$ curves in the static approximation (zero temperature and neglecting zero-point vibrational contributions). This allows the evaluation of the static spinodal conditions, that is, the values of pressure and volume ($p_{\text{sp}}$ and $V_{\text{sp}}$, respectively) at which the solid becomes mechanically unstable when a negative pressure is applied to it. It is well-known that for a solid to be mechanically stable with respect to an isotropic volumetric deformation, it must have a positive bulk modulus. When a negative pressure is applied to the solid, the volume increases and $B$ decreases until the bulk modulus vanishes at $p=p_{\text{sp}}$ (and $V=V_{\text{sp}}$). The spinodal conditions have been discussed in detail by García Baonza et al., $^{32,33}$ including their application to a simple universal equation of state valid for liquids and solids.

### C. Elastic Constants.
Following the detailed and clear presentation of Sin'ko and Smirnov, $^{26}$ we have calculated the elastic constants and their response to positive and negative hydrostatic pressures for the cubic sc and spinel and for the hexagonal gra-e1 Al lattices. Considering a crystal compressed by the hydrostatic pressure $p$ to the density $\rho_1$, the determination of the elastic constants at $p$, $C_{ijkl}$, requires the evaluation of the total energy of the crystal under small and homogeneous strains $\epsilon_{ij}$, because the expansion of the internal energy per unit mass, $\tilde{E}$, in terms of the Lagrangian strain tensor $(\eta_{ij}=\epsilon_{ij}+1/2\sum_k \epsilon_{ik}\epsilon_{kj})$ involves $C_{ijkl}$ as follows $^{35}$

$$
\tilde{E}(\rho_1,\eta_{mn})=\tilde{E}(\rho_1,0)+\frac{1}{\rho_1}\left(\sum_{ij} T_{ij}\eta_{ij}+\frac{1}{2}\sum_{ijkl} C_{ijkl}\eta_{ij}\eta_{kl}+\cdots\right)
\tag{1}
$$

where the elements $T_{ij}$ are the components of the stress tensor before deformation and the subscripts $i$ and $j$ stand for the Cartesian coordinates and are reduced following the Voigt notation: $xx\equiv1$, $yy\equiv2$, $zz\equiv3$, $yz\equiv4$, $zx\equiv5$, $yx\equiv6$.

For isotropic initial stress and representing $\epsilon_{ij}$ in the form $\epsilon_{ij}=s_{ij}\gamma+e_{ij}\gamma^2+\cdots$ (where $s_{ij}$ and $e_{ij}$ are coefficients of the power expansion in the infinitesimal parameter $\gamma$), second derivatives of the total energy with respect to $\gamma$ provide linear combinations of elastic constants, as collected in Tables 2 and 4 of ref 26 for the cubic and hexagonal Al lattices, respectively. For instance, in both symmetries the strain $\epsilon_{11}=\epsilon_{22}=\gamma$ (that is, $s_{11}=s_{22}=1$) provides $C_{11}+C_{12}-p$, and the strain $\epsilon_{13}=\epsilon_{31}=\gamma$ (that is, $s_{13}=s_{31}=1$) provides $2C_{44}-p$ (the strain parameters not listed being 0). By applying a number of independent strains to the unit cell equal at least to the number of independent elastic constants, these magnitudes can be obtained. At each pressure, we calculated the total energy of the strains appearing in Tables 2 and 4 of ref 26 for values of $\gamma$ ranging from $-0.04$ to $+0.04$ at 0.01 steps around the equilibrium geometry. To obtain the required second derivatives, fittings of polynomials to these energy versus $\gamma$ points were carried out. For the less symmetric strains it was necessary to optimize the internal parameters.

For our purposes, it is important to quote the mechanical stability conditions under hydrostatic pressure $^{26}$ for cubic

$$
\tilde{C}_{44}>0,\ \tilde{C}_{11}>|\tilde{C}_{12}|,\ \tilde{C}_{11}+2\tilde{C}_{12}>0
\tag{2}
$$

![](./images/812064006951927809_1.jpg)

Figure 1. Energy−volume curves of Al lattices according to our calculations. Symbols stand for the calculated (E,V) points.

and hexagonal crystals

$$
\tilde{C}_{44}>0, \tilde{C}_{11}>\left|\tilde{C}_{12}\right|, \tilde{C}_{33}\left(\tilde{C}_{11}+\tilde{C}_{12}\right)>2 \tilde{C}_{13}{ }^{2} \quad(3)
$$

where $\tilde{C}_{\alpha \alpha}=C_{\alpha \alpha}-p(\alpha=1,2, \ldots, 6), \tilde{C}_{12}=C_{12}+p, \tilde{C}_{13}=$ $C_{13}+p$, and $\tilde{C}_{23}=C_{23}+p$. For a cubic symmetry, the first condition refers to the stability with respect to a shear along one of the symmetry directions, the second one is related to the stability with respect to a tetragonal shear deformation, and the third one is equivalent to the condition $B>0$ previously quoted. The fulfillment of the above conditions is necessary for a given phase to be metastable but, obviously, it does not imply that the phase is the thermodynamically stable one of the system.

### D. Topology of the Electron Density.
Using Bader's AIM formalism $^{4}$ and the CRITIC program, $^{19}$ a microscopic analysis of the electron density of Al lattices has been carried out. To this end, at the VASP equilibrium geometries we have generated all electron wave functions from CRYSTAL calculations $^{17}$ using the same exchange and correlation functionals as in the pseudopotential ones. The AIM formalism allows the chemical characterization of the topology of the electron density in terms of critical points where the gradient of the electron density is 0 . Chemical bonds are identified by the existence of first-order saddle points of the electron density (where $\rho$ is minimum along one direction but maximum at the other two orthogonal directions). Cage points correspond to absolute minima of $\rho$, and for the ring points $\rho$ is maximum along one direction but minimum at the other two orthogonal directions. All of these critical points are characterized by the values of the electron density and the Laplacian of the electron density at those points. Zones of charge depletion and charge accumulation are associated with low values of $\rho$ and positive Laplacians and with high values of $\rho$ and negative Laplacians, respectively.

## III. Results

### A. General Results: Structure and Spinodal Conditions.
Computed $E-V$ curves for all of the Al lattices studied in this work are depicted in Figure 1, and the energetic, structural, equation of state, and spinodal parameters obtained from them, as well as representative experimental and theoretical data, are collected in Table 2. A comparison of our calculated values with experimental data is possible only for the fcc lattice ${ }^{20}$ and with previous theoretical values for the fcc, bcc, and hcp phases. ${ }^{25,26,36}$ On the one hand, the fcc phase is predicted to be the thermodynamically stable one at $p=0$, in agreement with experimental observations. Moreover, our computed zeropressure bulk properties for this phase agree very well with theroom condition values recently measured by Dewaele et al. $^{20}$ On the other hand, according to our zero-pressure relative volumes and energies for the fcc, bcc, and hcp phases, we predict a pressure-induced polymorphic sequence (fcc $\rightarrow$ hcp $\rightarrow$ bcc) consistent with that obtained in previous calculations at staticor low-temperature conditions. $^{25,26}$

We discuss now some results of importance for the AMM model. First, all of the $E-V$ curves show a minimum and, consequently, in a range of volumes, all of the Al lattices studied in this work are stable with respect to isotropic volumetric deformations $\left(B_{0}>0\right)$. Moreover, the $V_{0} \times B_{0}$ product keeps a rather constant value. This result provides further support for our calculated EOS, the differences between the $V_{0} \times B_{0}$ values being probably related to nonuniversal bonding features in these systems according to Hazen and Finger models. $^{1}$ We will see below that the AIM analysis of the electron density of these structures provides further insight on the chemical nature of these bonds. Second, it is clear from Figure 1 and Table 2 that $E-V$ curves corresponding to fcc, hcp, and bcc lattices are similar to each other and, in particular, show analogous zero-pressure volumes. On the contrary, those curves corresponding to sc, spinel, and gra-el Al lattices are rather different and show greater zero-pressure volumes and energies, greater spinodal volumes, and smaller zero-pressure bulk moduli than those of fcc, hcp, and bcc. As a consequence, sc, gra-el, and spinel are lower in energy than fcc, hcp, and fcc at volumes greater than $\sim 25 \AA^{3}$ (see Figure 1) and, in particular, near the room condition experimental volumes for each Al sublattice in the corresponding $\mathrm{AlX}_{3}$ crystals, $V_{\text {exp }}$ (see Table 1). Note, however, that the spinodal volumes of these Al lattices are lower

TABLE 2: Zero Pressure Energetic, Structural, and Equation of State Parameters (Subscript 0) and Spinodal Parameters (Subscript sp) of Al Lattices According to Our Calculations [Available Experimental and Theoretical Data Are Also Included; $\Delta E_0 = E_0 - E_{0(\text{fcc})}$]

<table>
  <thead>
    <tr>
      <th></th>
      <th>$V_0$ (Å³)</th>
      <th>$d_0$ (Å)</th>
      <th>$B_0$ (GPa)</th>
      <th>$B_0'$ (GPa)</th>
      <th>$\Delta E_0$ (meV)</th>
      <th>$V_{\text{sp}}$ (Å³)</th>
      <th>$p_{\text{sp}}$ (GPa)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>fcc</td>
      <td>16.58</td>
      <td>2.86</td>
      <td>75.80</td>
      <td>4.61</td>
      <td></td>
      <td>24.22</td>
      <td>−10.87</td>
    </tr>
    <tr>
      <td></td>
      <td>16.573¹</td>
      <td>2.86¹</td>
      <td>74.3 (73)¹</td>
      <td>4.47 (4.54)¹</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>16.75²</td>
      <td>2.872²</td>
      <td>72.6²</td>
      <td>4.64²</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>16.629 (16.819)³</td>
      <td>2.865 (2.876)³</td>
      <td>74.4 (72.5)³</td>
      <td>4.64 (4.15)³</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>16.240⁴</td>
      <td>2.842⁴</td>
      <td>79.66⁴</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>bcc</td>
      <td>17.10</td>
      <td>2.81</td>
      <td>63.25</td>
      <td>4.72</td>
      <td>95.2</td>
      <td>26.08</td>
      <td>−10.71</td>
    </tr>
    <tr>
      <td></td>
      <td>16.630⁴</td>
      <td>2.785⁴</td>
      <td>68.77⁴</td>
      <td></td>
      <td>113.0⁴</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>hcp</td>
      <td>16.74</td>
      <td>2.87</td>
      <td>70.62</td>
      <td>4.44</td>
      <td>32.1</td>
      <td>25.12</td>
      <td>−11.09</td>
    </tr>
    <tr>
      <td></td>
      <td>16.285⁴</td>
      <td>2.845⁴</td>
      <td>77.65⁴</td>
      <td></td>
      <td>49.5⁴</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>sc</td>
      <td>20.25</td>
      <td>2.73</td>
      <td>56.50</td>
      <td>4.56</td>
      <td>336.7</td>
      <td>30.07</td>
      <td>−8.64</td>
    </tr>
    <tr>
      <td>spinel</td>
      <td>27.71</td>
      <td>2.70</td>
      <td>37.70</td>
      <td>4.43</td>
      <td>572.4</td>
      <td>41.60</td>
      <td>−5.93</td>
    </tr>
    <tr>
      <td>gra-a</td>
      <td>22.99</td>
      <td>2.60</td>
      <td>45.35</td>
      <td>4.12</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>gra-e1</td>
      <td>24.67</td>
      <td>2.63</td>
      <td>43.77</td>
      <td>4.25</td>
      <td>448.2</td>
      <td>37.64</td>
      <td>−7.16</td>
    </tr>
    <tr>
      <td>gra-e ($P2_{1/n}$)</td>
      <td>20.68</td>
      <td>2.77</td>
      <td>57.78</td>
      <td>3.74</td>
      <td>142.0</td>
      <td>32.32</td>
      <td>−9.92</td>
    </tr>
  </tbody>
</table>

$^{a}$ Experimental (ref 20). Vinet EOS fitting by fixing $V_0$ (and $B_0$). $^{b}$ Calculated (refs 36 and 20). $p - V$ points calculated in ref 36 and fitted in ref 20 with a Vinet EOS. $^{c}$ Calculated (ref 26). Without (with) zero-point vibrations. $^{d}$ Calculated (ref 25).

![](./images/812064006951927809_2.jpg)

Figure 2. Energy of the $R\overline{3}$ Al lattice (relative to that of the fcc one) versus its unit cell angle, $\alpha$, for volumes (a) lower and equal to and (b) greater than $V_0$(Al(fcc)).

than their corresponding $V_{\text{exp}}$ values ($B < 0$ at $V_{\text{exp}}$) and, as could be expected, the $X$ elements are responsible for the stabilization of the $\text{Al}X_3$ lattices at these volumes, at least with respect to isotropic deformations. The volume dependence of the stability of these systems against less symmetric deformations is analyzed below from the results of the elastic constants. A detailed comparison between the calculated properties of the gra-e1 and gra-e structures will be done in subsection III.D.

It is finally to be emphasized that, despite the differences in the equilibrium volumes, the shortest $\text{Al}–\text{Al}$ distance, $d_0$, of all the lattices is practically the same, around $2.75 \pm 0.12$ Å. Within this range, distances are clearly sorted by the connectivity: the greater the connectivity, the greater the distance. The almost constancy of $d_0$ values and this distance–connectivity relationship illustrate the basic structural character of the Al sublattice in these compounds.

B. $R\overline{3}$ Lattices. In this subsection we pursue two main objectives: (i) to study the volume dependence of the mechanical stability of the sc Al matrix and, then, to identify the role played by the $X$ elements in the stabilization of the $\text{Al:Al}X_3$ sublattices and (ii) to study the effect of nonmetallic $X$ atoms on the geometry of the $R\overline{3}$ lattice at different volumes. With respect to point i, we use the common $R\overline{3}$ cell to explore the volume dependence of the rhombohedral transformation path connecting the fcc, sc, and bcc structures and, then, we also study the overall mechanical stability from the results of the elastic constants of the sc lattice.

In Figure 2 we show how the energy of the $R\overline{3}$ Al lattice, relative to that of the fcc one, changes with its unit cell angle, $\alpha$, for volumes ranging from $0.5V_0$ to $2V_0$, $V_0$ being our calculated zero-pressure volume of the fcc Al phase. The phase with the value of $\alpha$ giving the minimum energy, $\alpha_{\text{opt}}$, corresponds to the thermodynamically stable structure at the chosen volume (and zero temperature). We note that, at a given volume, two phases with different $\alpha$ values are in general at different pressures. As we can see in Figure 2a, at low volumes the $E$–$\alpha$ curves show two minima, at $\alpha = 60^\circ$ (the absolute minimum, fcc) and at $109.47^\circ$ (bcc), and a maximum at $\alpha = 90^\circ$ (sc). Thus, fcc and bcc phases are stable and sc is unstable with respect to angular changes at low volumes. As the volume increases (Figure 2b), the fcc and bcc minima transform into maxima, two new minima corresponding to noncubic phases emerge, and the instability of the sc structure reduces, becoming rather small for $V$ greater than $\sim$35 Å³ ($|\tilde{C}_{44}|$ smaller than about 4 GPa) and disappearing at a volume slightly smaller than $V_{\text{exp}}$ ($\text{Al:α-AlF}_3$). We note that $(\partial^2 E/\partial\alpha^2)_V$ evaluated at $\alpha = 90^\circ$ is closely related to $\tilde{C}_{44}$ of the sc phase and, then, a positive value of this second derivative corresponds to the fulfillment of one of the mechanical stability conditions mentioned above for cubic structures (see Figures 2 and 3).

Summarizing these results, if we explore $\alpha_{\text{opt}}$ as a function of the volume of the $R\overline{3}$ unit cell, we find three different regimes: (i) at low volumes, the fcc lattice is preferred; (ii) at increasing volumes $\alpha_{\text{opt}}$ changes from $60^\circ$ to $90^\circ$; and (iii) at high volumes, the sc lattice is preferred (see Figure 1). This

![](./images/812064006951927809_3.jpg)

Figure 3. Volume dependence of $B$, $\tilde{C}_{11}-\tilde{C}_{12}$, and $\tilde{C}_{44}$ for the sc structure according to our calculations.

latter structure, slightly distorted, corresponds to that of the Al sublattice experimentally observed in $\alpha$-AlF$_3$ (with $V_{\text{exp}} = 43.67$ $\text{\AA}^3$).

On the other hand, as shown in Figure 3, at low volumes the sc structure is stable with respect to tetragonal shear and isotropic volumetric deformations ($B$ and $\tilde{C}_{11}-|\tilde{C}_{12}|$ are positive near $V_0$(sc Al)). These stabilities reduce steeply as volume increases and, for volumes near $\sim$27 $\text{\AA}^3$, the system becomes (slightly) unstable with respect to the tetragonal deformation ($\tilde{C}_{11}-|\tilde{C}_{12}|$ about $-8$ GPa). For volumes near $V_{\text{exp}}(\text{Al}:\alpha\text{-AlF}_3)$, the values of $B$, $\tilde{C}_{44}$, and $\tilde{C}_{11}-|\tilde{C}_{12}|$ are about $-10$, $5$, and $-20$ GPa, respectively, thus indicating that the sc Al lattice is unstable with respect to tetragonal and isotropic deformations. We note that the only instability found at low volumes (including zero-pressure volume) for the sc lattice ($\tilde{C}_{44} < 0$) does not preclude the metastability at these volumes of the Al array found in $\alpha$-AlF$_3$ (a sc lattice with a slight rhombohedral distortion).

With respect to our second aim of this subsection, we compare the volume dependence of the optimized $R\overline{3}$ unit cell lattice parameter, $a_{\text{opt}}$, in the pure Al crystal and in the Al sublattice of $\alpha$-AlF$_3$, a fluoride with the $R\overline{3}c$ space group. Besides, to explore the effect on $a_{\text{opt}}$ of a change of the nonmetallic element in the crystal, we have also optimized the geometry of a hypothetical $R\overline{3}c$ phase of AlCl$_3$. The results of these calculations cover a volume range from around 20 to 90 $\text{\AA}^3$ and reveal that we can roughly describe simultaneously the behavior of $a_{\text{opt}}$ in the three lattices with a single curve. Al and $\alpha$-AlF$_3$ $a_{\text{opt}}$-$V$ curves nearly overlap in the computed range of volumes common to both crystals, that is, for those volumes ranging from about 27 $\text{\AA}^3$ to about 37 $\text{\AA}^3$, which correspond to negative and positive pressures applied to Al and AlF$_3$, respectively (the spinodal volume of the $R\overline{3}$ Al lattice is 24.16 $\text{\AA}^3$). In the same way, the $\alpha$-AlF$_3$ and $\alpha$-AlCl$_3$ $a_{\text{opt}}$-$V$ curves overlap for volumes ranging from about 43 $\text{\AA}^3$ to about 57 $\text{\AA}^3$, corresponding to small positive (or negative) and quite positive pressures applied to these crystals, respectively. This behavior is obtained in both LDA and GGA calculations. These results may be related to the small sensitivity of $V(R\overline{3})$ with respect to the $\alpha$ angle and to the similar values of $\alpha_{\text{opt}}$ obtained at the same volumes for different crystals. Therefore, we find that there exists a nearly common $a_{\text{opt}}$-$V$ curve for the $R\overline{3}$ Al matrix in these Al and AlX$_3$ phases, this curve being quite independent of the presence of the $X$ atoms. As a consequence, at a given crystal volume the shortest Al-Al distance in different crystals containing the $R\overline{3}$ Al matrix keeps approximately the same value regardless of the lattice anionic constituents.

![](./images/812064006951927809_4.jpg)

Figure 4. Volume dependence of $B$, $\tilde{C}_{11}-\tilde{C}_{12}$, and $\tilde{C}_{44}$ for the spinel structure according to our calculations.

Finally, as shown in Table 1, the bcc and gra-a structures can be described with the $R\overline{3}$ space group using different cell angles and Al positions and with Al multiplicity equal to 2. The bcc structure is characterized within this space group by fixing $\alpha$ and the position of Al to $90^\circ$ and ($^1/_4$, $^1/_4$, $^1/_4$), respectively, whereas only the Al position is fixed in the ideal alternate graphitic-like structure to ($^1/_3$, $^1/_3$, $^1/_3$). The alternate stacking of Al planes characteristic of the gra-a structure has not been experimentally found in any inorganic compound. Optimized $\alpha$ and Al positions have been explored as a function of the volume of the $R\overline{3}$ unit cell. We found three different regimes: (i) at low volumes $\alpha_{\text{opt}} = 90^\circ$ and the optimized Al position is ($^1/_4$, $^1/_4$, $^1/_4$), that is, the bcc structure is preferred; (ii) within a small range of intermediate volumes (between $\sim$22 and $\sim$24 $\text{\AA}^3$), $\alpha$ decreases abruptly from $90^\circ$ and, then, in the small range between $\sim$24 and $\sim$27 $\text{\AA}^3$, the Al position changes from ($^1/_4$, $^1/_4$, $^1/_4$) to near ($^1/_3$, $^1/_3$, $^1/_3$); and (iii) at volumes greater than $\sim$27 $\text{\AA}^3$ the ideal alternate graphitic-like structure (Al position ($^1/_3$, $^1/_3$, $^1/_3$) and $\alpha_{\text{opt}}$ values around $65-75^\circ$) is preferred (remember that $V_{\text{sp}}(\text{bcc})$ is about 26 $\text{\AA}^3$). Thus, as the volume increases, the bcc Al lattice transforms into the ideal gra-a one in a similar way as the fcc structure does into the sc one. This analogy might suggest the gra-a structure to be a candidate for an Al sublattice in aluminum compounds at high-pressure conditions.

### C. Spinel Lattice.
In the spinel structure, all of the stability conditions are fulfilled in a wide range of volumes including the zero-pressure equilibrium geometry (see Figure 4). Besides, around $V_0$, both, $\tilde{C}_{44}$ and $\tilde{C}_{11}-|\tilde{C}_{12}|$, decrease slightly as volume increases, in contrast to the different sign and magnitude of the slopes for the corresponding curves in the simple cubic structure. It must be remembered that the Al spinel lattice is the only actual Al matrix in an AlX$_3$ crystal whose overall mechanical stability is analyzed in this work, as this cationic array has been experimentally observed, with no distortion, in $\eta$-AlF$_3$. Therefore, the metastability of the Al spinel provides further support to the idea of a correspondence between the metallic arrays in crystals and the metastable phases of the parent metal.

As for an isotropic substance $\tilde{C}_{11} - \tilde{C}_{12} = 2\tilde{C}_{44}$, departure from unity of the ratio $r = 2\tilde{C}_{44}/(\tilde{C}_{11} - \tilde{C}_{12})$ can be considered as a measure of the degree of anisotropy of a given cubic crystal. For the fcc Al lattice, Sin'ko and Smirnov obtain $r = 1.18$ at zero pressure from their calculations without zero-point vibrations,$^{26}$ whereas the 298 K experimental value is $1.22.^{37}$ Thus, the fcc Al crystal seems to be quite isotropic. On the other hand, according to our static results, the zero-pressure value of $r$ for

Al Lattices
J. Phys. Chem. B, Vol. 110, No. 37, 2006 18615

**TABLE 3: Volume (and Pressure) Dependence of the $\tilde{C}_{ij}$ Constants for the Hexagonal $P6/mmm$ Al Structure According to Our Calculations**

| $V$ ($\mathring{\text{A}}^3$) | $p$ (GPa) | $\tilde{C}_{11}$ (GPa) | $\tilde{C}_{12}$ (GPa) | $\tilde{C}_{33}$ (GPa) | $\tilde{C}_{44}$ (GPa) | $\tilde{C}_{13}$ (GPa) |
|-------------------------------|-----------|------------------------|------------------------|------------------------|------------------------|------------------------|
| 20.81                         | 10.627    | 80.3                   | 141.5                  | 154.2                  | $-9.1$                 | 38.8                   |
| 22.43                         | 5.097     | 73.0                   | 102.5                  | 139.4                  | $-15.9$                | 22.0                   |
| 24.67                         | 0.0       | 74.2                   | 53.7                   | 137.7                  | $-19.8$                | $-2.5$                 |
| 26.85                         | $-3.080$  | 57.3                   | 25.9                   | 98.3                   | $-15.0$                | 0.5                    |
| 28.76                         | $-4.813$  | 54.5                   | 15.8                   | 68.5                   | $-10.4$                | $-1.8$                 |
| 37.34                         | $-7.161$  | 20.4                   | 8.1                    | $-19.1$                | 0.6                    | 0.2                    |

the spinel lattice is about 2.6; thus, this structure is less isotropic than the fcc one at zero pressure. This can be also correlated with our computed $G_{\text{H}}/B$ ratio ($G_{\text{H}}$ is the Hill shear modulus$^{38}$), which is higher in the Al spinel structure (0.39) than in Al fcc (0.35). We must note that, as expected, the more isotropic lattice has the greater connectivity. Furthermore, as $V$ increases, $r$(spinel) decreases to values near 2 (for $V_0 < V < V_{\text{sp}}$) and, thus, the anisotropy of this structure seems to decrease as the volume increases. The anisotropic character of the spinel lattice is relevant to the analysis of the AMM model, as a correlation between the structural anisotropy, and the lack of homogeneity in the electron density distribution is expected.$^{39}$ Because the inhomogeneities can be associated with the ability of the Al sublattice to host nonmetallic elements,$^{14}$ we infer that metal sublattices in inorganic crystals may show preference for those symmetries with structural anisotropy (see subsection III.E).

**D. Eclipsed Graphitic-like Lattices.** As indicated in subsection II.A, a hexagonal $P6/mmm$ space group (gra-e1 in Table 1) unit cell is first used to model the Al eclipsed graphitic-like sublattices of $\text{Al(OH)}_3$ and $\text{AlCl}_3$ crystals. The energy minimization process that provides optimized hexagonal unit cell parameters reveals that the $c/a$ ratio keeps an almost constant value around 0.60 in a wide range of volumes ($18$ $\mathring{\text{A}}^3$ $< V < 35$ $\mathring{\text{A}}^3$), including the zero-pressure equilibrium geometry ($V_0$-(gra-e1) $= 24.67$ $\mathring{\text{A}}^3$). This fact has several implications for the geometry and compressibility of this structure. First, it is interesting to point out that, although strictly the connectivity of Al in the gra-e1 structure is 3 (see Table 1), for the wide volume range with $c/a \sim 0.60$, the shell of the next-nearest neighbors, containing two Al atoms, lies very close to that of the nearest neighbors (it is only $5\%$ distant). In fact, the shortest and the next-shortest $\text{Al-Al}$ distances increase slightly and almost at the same rate as the volume increases up to $V$ near 35 $\mathring{\text{A}}^3$, where the difference between these two distances becomes apparent, as the shortest distance begins to decrease slightly while the next-shortest one continues to increase, now with a much higher slope. Second, the linear compressibilities along the $a$ and $c$ axes ($\kappa_a$ and $\kappa_c$, respectively) obviously have similar values in the volume range where the optimized $c/a$ ratio of the gra-e1 structure is approximately constant. For volumes near $V_{\text{sp}}$ ($= 37.64$ $\mathring{\text{A}}^3$) and higher, the $c/a$ ratio increases (abruptly) as $V$ does approaching the values of the idealized hexagonal sublattices of $\text{Al(OH)}_3$ and $\text{AlCl}_3$, indicating also that $\kappa_c > \kappa_a$ for these expanded structures.

Moreover, if the $c/a$ ratio does not depend on volume, the bulk modulus of this hexagonal structure can be expressed in terms of the $\tilde{C}_{ij}$ constants by means of the equation $B = (2\tilde{C}_{11} + 2\tilde{C}_{12} + 4\tilde{C}_{13} + \tilde{C}_{33})/9$.$^{26}$ Therefore, we have a simple procedure that allows us to check the evaluation of $B$ in the range $18$ $\mathring{\text{A}}^3$ $< V < 35$ $\mathring{\text{A}}^3$ by using the above equation and the computed elastic constants collected in Table 3. Results are very satisfactory because this procedure provides values of $B$ very close to those calculated previously from the EOS fittings to the computed $E(V)$ points.

According to the particular values of our elastic constants (see Table 3), at low volumes ($V$ around $0.8\ V_0$(gra-e1)), both $\tilde{C}_{44} > 0$ and $\tilde{C}_{11} > |\tilde{C}_{12}|$ stability conditions are violated, whereas at zero pressure, only the instability related to $\tilde{C}_{44}$ remains ($\tilde{C}_{44}$ is about $-20$ GPa at $V_0$(gra-e1)). This constant becomes positive only at a volume slightly smaller than the spinodal one ($V_{\text{sp}} = 37.64$ $\mathring{\text{A}}^3$). The zero-pressure instability of the hexagonal lattice can be associated with a monoclinic distortion. The only phase reported for $\text{AlCl}_3$ (ref 24) and the most stable of the phases reported for $\text{Al(OH)}_3$ at room condition (gibbsite)$^{23,40,41}$ have the monoclinic space groups $C2/m$ and $P2_1/n$, respectively. In these structures, the Al sublattices can be obtained from that in gra-e1 by a monoclinic distortion related to the $\tilde{C}_{44}$ elastic constant.

This fact draw us to perform complete geometrical optimizations in the monoclinic $P2_1/n$ structure of Al, where, as indicated above, at a given volume the optimization of nine parameters is required. Due to the high computational cost involved in the evaluation of the elastic constants of this monoclinic structure, the calculations were limited to isotropic volumetric deformations. The EOS fitting of the calculated $(E, V)$ points gives the zero-pressure and spinodal properties shown in the last row of Table 2. At zero pressure, this monoclinic structure is about $0.31$ eV lower in energy and has $V_0$ smaller (about $15\%$) and $B_0$ higher (about $30\%$) than the hexagonal one. Note, however, that the shortest zero-pressure $\text{Al-Al}$ distance, $d_0$, in gra-e is about $5\%$ higher than that in gra-e1. The spinodal volume in the monoclinic structure is, as $V_0$, about $15\%$ smaller than that in the hexagonal one. Overall, the zero-pressure and spinodal properties of the monoclinic Al lattice are very close to those of the simple cubic phase, with the exception of the much lower zero-pressure energy of the former. It is also interesting to point out that, according to our calculations, a hypothetical fcc $\rightarrow$ gra-e phase transition is predicted at a negative pressure of $-5.0$ GPa with a volume increase of $28\%$ and a bulk modulus decrease of $31\%$.

The analysis of the results in the hexagonal and monoclinic structures suggests that the gra-e lattice is a potential candidate structure associated with the $\tilde{C}_{44}$ instability found in the gra-e1 lattice. Therefore, the role played by the nonmetallic elements in the stabilization of the Al sublattices in $\text{Al(OH)}_3$ and $\text{AlCl}_3$ seems to be better discussed in terms of this monoclinic than with the ideal hexagonal structure. Further time-demanding computations would be necessary to evaluate elastic constants in the monoclinic structure, although in view of the above results we think that the anions might not contribute to a great extent to the mechanical stability of the monoclinic Al sublattices at zero pressure, although they may play a relevant role in the cohesion and stabilization of these matrixes in $\text{Al(OH)}_3$ and $\text{AlCl}_3$.

**E. Electron Density Inhomogeneities and Structural Anisotropy.** In Table 4, we collect information obtained from the AIM analysis of the electron density of the Al lattices that is relevant to the quantification of the degree of inhomogeneity of these lattices and to the establishment of correlations with the results obtained from the structural and stability studies. As a result, we provide a deeper insight on some of the hypotheses of the AMM model. In Table 4, we show the bond point (BP), ring point (RP), and cage point (CP) positions, as well as the values of the density at those points ($\rho_{\text{b}}$, $\rho_{\text{r}}$, and $\rho_{\text{c}}$, respectively) for the fcc, simple cubic, spinel, and eclipsed and alternated graphitic Al structures. The Laplacian of the density at the bond points is also included. All of the properties are given at the calculated zero-pressure equilibrium volumes of the Al lattices

<table><thead><tr><td>lattice</td><td>BP position</td><td>$ρ_{b}(e/bohr^{3})$</td><td>$V^{2}ρ_{b}(e/bohr^{5})×10^{-3}$</td><td>RP position</td><td>$ρ_{r}(e/bohr^{3})$</td><td>CP position</td><td>$ρ_{c}(e/bohr^{3})$</td></tr></thead><tbody><tr><td>fcc$(Fm\overline {3}m)$</td><td>$(0,^{1}/_{4},^{1}/_{4})$</td><td>2.96</td><td>−0.49</td><td>(0.282, 0.282, 0.282)</td><td>2.82</td><td>$(^{1}/_{4},^{1}/_{4},^{1}/_{4})$ $(0,0,^{1}/_{2})$</td><td>2.81 1.76</td></tr><tr><td>sc$(Pm\overline {3}m)$</td><td>$(0,0,^{1}/_{2})$</td><td>3.09</td><td>−12.3</td><td>$(0,^{1}/_{2},^{1}/_{2})$</td><td>1.74</td><td>$(^{1}/_{2},^{1}/_{2},^{1}/_{2})$</td><td>0.815</td></tr><tr><td>spinel$(Fd\overline {3}m)$</td><td>$(1/8,1/8,0.525)$</td><td>3.55</td><td>−4.54</td><td>(0.341, 0.341, 0.341)</td><td>3.33</td><td>$(3/8,3/8,3/8)$</td><td>3.25</td></tr><tr><td></td><td></td><td></td><td></td><td>$(0,^{1}/_{4},^{1}/_{4})$</td><td>0.193</td><td>$(^{1}/_{8},^{1}/_{8},^{1}/_{8})$</td><td>0.0489</td></tr><tr><td>gra-e1$(P6/mmm)$</td><td>$(0,^{1}/_{2},^{1}/_{2})$</td><td>3.62</td><td>−22.3</td><td>$(1/2,1/2,0)$</td><td>1.92</td><td>$(0,0,0)$</td><td>0.115</td></tr><tr><td></td><td>$(1/3,2/3,0)$</td><td>2.85</td><td>−7.53</td><td>$(0,0,^{1}/_{2})$</td><td>0.262</td><td></td><td></td></tr><tr><td>gra-a$(R\overline {3},hex^{a})$</td><td>$(1/6,1/3,1/3)$</td><td>3.86</td><td>−26.3</td><td>(1/3, 1/6, 1/6)</td><td>1.11</td><td>$(2/3,1/3,1/3)$</td><td>0.349</td></tr><tr><td></td><td>$(0,0,^{1}/_{2})$</td><td>3.26</td><td>−8.19</td><td></td><td></td><td></td><td></td></tr></tbody></table>

$^{a}$ "hex" indicates that the hexagonal axes of the space group considered are used.

![](./images/812064006951927809_5.jpg)

Figure 5. Electron density maps for Al in (a) the (100) plane of the fcc structure and (b) the (011) plane of the simple cubic structure at their respective zero pressure theoretical equilibrium geometries. Bond points (solid squares) and cage points (solid circles) are indicated. Isolines of the density range from$\rho=0$to$\rho=0.3\ e/bohr^{3}$at$0.005\ e/bohr^{3}$steps.

($V_{0}$in Table 1). The calculated BP crystallographic coordinates at$V_{0}$coincide with those at the experimental volumes of the Al sublattices in the$AlX_{3}$crystals ($V_{exp}$in Table 1), except in the spinel lattice. The$z$coordinate given in the table for this structure (0.525) is slightly different from the value obtained at$V_{exp}$(0.511). In the gra-e1 and gra-a structures, two different bond points corresponding to nearest (n) and next nearest (nn) neighbors are found. In gra-a, the multiplicities of these bonds are 3 and 1, respectively, the effective connectivity of Al in this structure being 4. In gra-e1, the multiplicity of the n bonds is 3 and that of the nn bonds is 2, the effective connectivity of Al in this structure being$3 + 2$near$V_{0}$and 3 near$V_{exp}$(see subsection III.D). From now on we will focus on the values for the n bonds.

Calculated$\rho_{b}$and$\nabla^{2}\rho_{b}$values are rather small.$\rho_{b}$values are similar for all of the Al lattices, and their changes can be rationalized in terms of the$\rho_{b}-d$relationship discussed by Martín Pendás et al. in ionic crystals.⁴² Thus, we observe a correlation between the zero-pressure values of$\rho_{b}$and the Al−Al nearest distances:$\rho_{b}$decreases as the shortest Al−Al distance (and, thus, the connectivity) increases. Besides, this$\rho_{b}-d$relationship also applies, slightly modulated by the connectivities, when considering the lattices both at$V_{0}$and at$V_{exp}$. In this way, the value of$\rho_{b}$for the gra-e1 lattice at$V_{exp}(Al(OH)_{3})$($\rho_{b}$$=0.0318\ e/bohr^{3},d_{exp}=2.93$Å) is slightly greater than those for the sc and fcc at$V_{0}$($d_{0}=2.73$and 2.86 Å, respectively) due to the smaller connectivity of the former (3 for gra-e1, 6 for sc, and 12 for fcc). With respect to the values of$\nabla^{2}\rho_{b}$, they are 1 or 2 orders of magnitude smaller in the fcc structure than in the Al sublattices observed in the$AlX_{3}$crystals. This result and the negative value of$\nabla^{2}\rho_{b}$point toward a less metallic (more covalent) character and, thus, a less homogeneous electron charge density of the host Al matrixes with respect to pure fcc Al. We believe that the importance of this finding deserves further analysis.

Accordingly, we recall the$f$index introduced by Mori- Sánchez et al.⁴³ to measure the degree of homogeneity of the electron density in crystals.$f$is defined as$\rho_{c}^{min}/\rho_{b}^{max}$, where$\rho_{c}^{min}$is the absolute minimum of the electron density in the crystal (located in one of the cage points) and$\rho_{b}^{max}$is the maximum electron density found among the bond point positions. Mori- Sánchez et al. showed that alkaline metals have$f$values near 1 (resembling the free electron gas model), alkaline earth metals, around 0.7, most other metallic elements, around 0.5, and typical covalent, ionic, and molecular crystals, close to 0.⁴³ According to our calculations,$f$is 0.59 for the fcc Al lattice at$V_{0}$, 0.26 at$V_{0}$, and 0.05 at$V_{exp}$for the sc one and close to 0 at both$V_{0}$and$V_{exp}$for the other lattices in Table 4. This sequence suggests a decrease of the metallic character and an increase of the bond directionality in passing from the fcc to the rest of the Al sublattices.

A nice illustration of this statement is provided in Figure 5, where the maps of the electron density of fcc and simple cubic Al lattices, at their corresponding zero-pressure equilibrium volumes, are depicted along the (100) and (011) planes, respectively. The planes were chosen to contain both bond and cage points (indicated in Figure 5 by solid squares and solid circles, respectively). As shown in Figure 5, the smaller$f$value of the simple cubic lattice is associated with a greater number

of isolines separating cage and bond points in the map of this lattice. Furthermore, the different bond directionalities in both lattices is clearly manifested by the presence of well-separated bonds and low-density channels in the simple cubic lattice, which are absent in the fcc one. The different degrees of sphericity of the isolines surrounding both nuclei and cage points should be also noted. Further insight on the degree of homo- geneity of the electron density of all of the Al crystals studied in this work can be obtained by comparing, for each lattice, the particular values of $\rho$ computed at the different critical points(see Table 4).

Thus, the slight inhomogeneities observed in the fcc structure(the thermodynamic stable structure of Al at room conditions) are notably enhanced in the Al matrixes observed in the inorganic crystals. This finding constitutes a relevant result that provides a quantum mechanical assessment of the AMM model. According to it, the existence of these compounds seems to require Al structures with regions where the electron density is accumulated to favor the arrival of the nonmetallic elements with the subsequent creation of the corresponding anion and, then, the formation of the crystal. Besides, the less homogeneous electron density of the host Al matrixes with respect to pure fcc Al correlates with the less structural isotropy previously found in the spinel lattice with respect to the fcc one. This illustrates the expected correlation between the lack of homo- geneity in $\rho$ and the structural anisotropy.

### IV. Conclusions
We reported a theoretical investigation of the structure, stability, and electron charge density of several structures of Al that have been observed, slightly distorted in some cases, in $AlX_{3}(X=F, OH, Cl)$ compounds. Our results were discussed in light of the so-called anions in metallic matrices model. We found that, in all of the Al sublattices considered, the shortest zero-pressure $Al-Al$ distance keeps a common value, thus providing further support for the cation recognition hypothesis of the AMM model. $^{14}$ We also found that, although the sc and hexagonal Al matrixes do not fulfill the mechanical stability criteria at their zero-pressure equilibrium geometries, the instabilities obtained are compatible with the slight distortions experimentally observed for these structures in $AlX_{3}$ crystals. On the other hand, all of the Al matrixes violate the spinodal condition at the equilibrium volumes of the $AlX_{3}$ crystals, the guest nonmetallic $X$ elements being responsible for the final stability of these compounds. Our AIM topological analysis of the electron density has demonstrated that the subtle inhomo- geneities of $\rho$ found in the fcc structure of Al increase notably in the less isotropic Al sublattices observed in $AlX_{3}$ crystals. Because zones of charge accumulation are clearly identified as privileged regions for the localization and formation of $F^{-}, OH^{-}$ , and $Cl^{-}$ anions, the correlation between the lack of homogeneity of $\rho$ and the structural anisotropy allows us to conclude that the latter seems to be the main factor to discriminate Al metallic matrices able to host nonmetallic elements and a relevant factor to the final stability of these compounds.

A natural extension of our work is the consideration of more complex inorganic materials containing matrices with more than one metallic element. For instance, an interesting problem that remains unsolved refers to the octahedral and tetrahedral coordinations shown by Al and Mg atoms, respectively, in spinel MgAl₂O₄. We believe that a theoretical study under the perspective of the AMM model could help to explain the anomalous behavior of Mg and Al in this compound and to correlate the particular features of the electron density of an intermetallic $(MgAl_{2})$ matrix to the actual positions of the O atoms in the crystal.

Acknowledgment. Financial support from the Spanish DGICYT (Projects BQU2003-06553, BQU2001-1695, andMAT2004-05867-C03-02) and Comunidad de Madrid (GR/ MAT/0358/2004) is gratefully acknowledged. Part of this work was performed under Project HPC-EUROPA (RII3-CT-2003-506079), with the support of the EU-Research Infrastructure Action under the FP6 "Structuring the European Research Area" program. M.M. thanks the Spanish MCYT for a graduate grant.

### References and Notes
(1) Hazen, R. M.; Finger, L. W. Comparative Crystal Chemistry; Wiley: New York, 1982.
(2) Prewitt, C. T.; Downs, R. T. In Reviews of Mineralogy; Hemley, R. J., Ed.; Mineralogical Society of America: Washington, DC, 1998; Vol.37, pp 283-317.
(3) Hyde, B. G.; Anderson, S. Inorganic Crystal Structures; Wiley: New York, 1989.
(4) Bader, R. F. W. Atoms in Molecules. A Quantum Theory; Oxford University Press: Oxford, U.K., 1990.
(5) Luaña, V.; Mori-Sánchez, P.; Costales, A.; Blanco, M. A.; Martín Pendás, A. J. Chem. Phys. 2003, 119, 6341.
(6) Becke, A. D.; Edgecombe, N. E. J. Chem. Phys. 1990, 92, 5397.
(7) Silvi, B.; Savin, A. Nature (London) 1994, 371, 683.
(8) Haüssermann, U.; Wengert, S.; Hofmann, P.; Savin, A.; Jepsen, O.; Nesper, R. Angew. Chem., Int. Ed. Engl. 1994, 33, 2069.
(9) Savin, A.; Nesper, R.; Wengert, S.; Fassler, T. F. Angew. Chem., Int. Ed. Engl. 1997, 36, 1808.
(10) O'Keefe, M.; Hyde, B. G. Structure Bonding (Berlin); Springer- Verlag: Berlin, Germany, 1985; Vol. 61, p 77.
(11) Martinez-Cruz, L. A.; Ramos-Gallardo, A.; Vegas, A. J. Solid State Chem. 1994, 110, 397.
(12) Vegas, A.; Grzechnik, A.; Syassen, K.; Loa, I.; Hanfland, M.; Jansen, M. Acta Crystallogr. B 2001, 57, 151.
(13) Vegas, A.; Jansen, M. Acta Crystallogr. B 2002, 58, 38.
(14) Vegas, A.; Santamaría-Pérez, D.; Marqués, M.; Flórez, M.; García Baonza, V.; Recio, J. M. Acta Crystallogr. B 2006, 62, 220.
(15) Vegas, A.; Mejía-López, J.; Romero, A. H.; Kiwi, M.; Santamaría- Pérez, D.; Garcia Baonza, V. Solid State Sci. 2004, 6, 809.
(16) Kresse, G.; Furthmuller, J. Phys. Rev. B 1996, 54, 11169.
(17) Saunders, V. R.; Dovesi, R.; Roetti, C.; Causá, M.; Harrison, N.M.; Orlando, R.; Zicovich-Wilson, C. M. CRYSTAL98 User's Manual; University of Torino: Torino, Italy, 1998.
(18) Blanco, M. A.; Francisco, E.; Luaña, V. Comput. Phys. Commun.2004, 158, 57.
(19) Martin Pendás, A.; Luaña, V. CRITIC code (1995-2003).
(20) Dewaele, A.; Loubeyre, P.; Mezouar, M. Phys. Rev. B 2004, 70,094112.
(21) Daniel, Ph.; Bulou, A.; Rousseau, M.; Nouet, J.; Fourquet, J. L.; Leblanc, M.; Burriel, R. J. Alloys Compd. 1990, 2, 5663.
(22) Herron, N.; Thorn, D. L.; Harlow, R. L.; Jones, G. A.; Parise, J. B.; Parise, J. A.; Vogt, T. Chem. Mater. 1995, 7, 75.
(23) Saalfeld, H.; Wedde, M. Z. Kristallogr. 1974, 139, 129.
(24) Ketelaar, J. A. A.; Macgillairy, C. H.; Renes, P. A. Recl. Trav. Chim. Pays-Bas 1948, 66, 501.
(25) Boettger, J. C.; Trickey, S. B. Phys. Rev. B 1996, 53, 3007.
(26) Sin'ko, G. V.; Smirnov, N. A. J. Phys.: Condens. Matter 2002,14,6989.
(27) Kresse, G.; Joubert, D. Phys. Rev. B 1999, 59, 1758.
(28) Perdew, J. P.; Wang, Y. Phys. Rev. B 1992, 45, 13244.
(29) Ceperley, D. M.; Alder, B. J. Phys. Rev. Lett. 1980, 45, 566.
(30) Monkhorst, H. J.; Pack, J. D. Phys. Rev. B 1976, 13, 5188.
(31) Vinet, P.; Ferrante, J.; Rose, J. H.; Smith, J. R. J. Geophys. Res.1987,92,9319.
(32) García Baonza, V.; Cáceres, M.; Núnez, J. Phys. Rev. B 1995, 51,28.
(33) García Baonza, V.; Taravillo, M.; Cáceres, M.; Núnez, J. Phys. Rev. B 1996, 53, 5252.
(34) Birch, F. Phys. Rev. 1947, 71, 809.
(35) Wallace, D. C. Solid State Physics; Academic: New York, 1970; Vol. 25, p 301.
(36) Wang, Y.; Chen, D.; Zhang, X. Phys. Rev. Lett. 2000, 84, 3220.
(37) Kamm, G. N.; Alers, G. A. J. Appl. Phys. 1964, 35, 327.
(38) Hill, R. Proc. Phys. Soc. London 1952, 65, 350.
(39) Mattesini, M.; Ahuja, R.; Johansson, B. Phys. Rev. B 2003, 68,184108.

(40) Gale, J.; Rohl, A. L.; Milman, V.; Warren, M. C. J. Phys. Chem. 2001, 105, 10236.

(41) Digne, M.; Sautet, P.; Raybaud, P.; Toulhoat, H.; Artacho, E. J. Phys. Chem. B 2002, 106, 5155.

(42) Martín Pendás, A.; Costales, A.; Luaña, V. J. Phys. Chem. B 1998, 102, 6937.

(43) Mori-Sánchez, P.; Martín Pendás, A.; Luaña, V. J. Am. Chem. Soc. 2002, 124, 14721.