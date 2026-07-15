PHYSICAL REVIEW MATERIALS 4, 063609 (2020)

# Role of dislocations in the bcc-hcp transition under high pressure:
## A first-principles approach in beryllium

Vanessa Riffet $\mathbb{D},^{1}$ Bernard Amadon $\mathbb{D},^{1,2}$ Nicolas Bruzy $\mathbb{D},^{1}$ and Christophe Denoual $\mathbb{D}^{1,2, *}$

$^{1}$ CEA, DAM, DIF, F-91297 Arpajon, France
$^{2}$ Université Paris-Saclay, CEA, Laboratoire Matière sous Conditions Extrêmes, 91680 Bruyères-Le-Châtel, France

![](./images/812595251607764993_1.jpg)
(Received 9 March 2020; accepted 1 June 2020; published 30 June 2020)

We study the impact of dislocations on the bcc-to-hcp-to-bcc phase transition cycle using density-functional theory. The transformation is studied under two external constraints: first under pressure, and second under uniaxial shear. In both cases, we find that the elastic strain created by $\pm\frac{1}{2}[111]$ screw dislocations induces a shear deformation which initiates the bcc-to-hcp transformation through the Burgers mechanism, as suggested by the location of the phases and their orientations. For the pressure-induced transformation, a hysteresis appears in the $P$-$V$ curve and the analysis of structures reveals that only the three hcp variants topologically compatible with the screw dislocations emerge. Our calculations thus capture characteristics of microstructures containing grains (variant hcp) and defects (triple junction and grain boundaries). Interestingly, a small bcc inclusion is present in the parent bcc after reversion. A careful analysis of the underlying deformation reveals that its origin is explained by three reversion transformations which are self-accommodating and thus stable. Under shear, the strain field induced by the dislocation decreases the energetic barrier considerably.

DOI: 10.1103/PhysRevMaterials.4.063609

## I. INTRODUCTION
The martensitic transformation is a complex process from the point of view of thermodynamics and microscopic mechanisms [1,2]. One of the most known is the pressure-induced or temperature-induced bcc-to-hcp transition which is frequent in pure elements such as Be, Mg, Fe, Ti, Zr, Hf, Ba, Mo, and Nb [3–7].

For the direct bcc-to-hcp transition, the calculated thermodynamical transition pressures from the first-principles methods are consistent with the experimental transition pressures for, e.g., Mg [8] and Fe [9–11]. Turning to the mechanism of the transition, the Burgers path [12] describes the transformation from bcc to hcp: Zr [12], Ba [13], Fe [14,15], Ti [16], and Mg [17]. Indeed, the volume-conserving shear deformation transforms $\{110\}_{bcc}$ into $\{0001\}_{hcp}$ and $\langle 001\rangle_{bcc}$ into $\langle 2\overline{1}\overline{1}0\rangle_{hcp}$, and simultaneously the shuffle restores the hcp stacking (Fig. 1) [18]. However, the methodology to calculate the minimum energy path, via two-dimensional potential-energy (enthalpy) surfaces (PES) depending on shear deformation and shuffle as order parameters, is still in debate [9,11,19,20]. More importantly, and according to first-principles methods, required pressures for the transition to happen along the Burgers mechanism (e.g., for Fe [9,19]) are far from the ones observed under purely hydrostatic loading [15]. A limited number of studies at the atomic scale were devoted to explaining this theory/experiment disagreement by using dislocations to foster the martensitic transformation [21–26].

Phase-field models [27] and some atomistic simulations [21–26] have highlighted that preexisting dislocations are possible nucleation sites, with a stress field inducing a strong variant selection [25]. A spreading of the dislocation core is also observed after the transformation [28,29]. Although numerical potentials could be used to achieve density-functional theory (DFT) calculation accuracy for both phase transformation and dislocation structures [30], no potential of this kind is available for beryllium under pressure.

In this work, we study beryllium, for which the stable phase is hcp at ambient conditions [31]. However, the phase diagram of beryllium is an experimental and theoretical challenge [32–34]. Experimentally, the alleged stability domain of the bcc phase at very high pressure has not been reached yet. The large spreading of the hcp-to-bcc thermodynamic transition pressure from first-principles calculations (from 100 up to 510 GPa [6,33,35–43]) is probably due to the very low energy difference between hcp and bcc structures (less than 100 meV per beryllium, see Fig. 2), making the determination of the transition pressure tricky.

As for iron, first-principles calculations show that the thermodynamical transition pressure and the transition pressure required to follow the Burgers path are very different (see Sec. III A.). For this reason, in this paper we investigate the role of dislocations on the phase transition. Contrary to iron, beryllium has no magnetism. However, it has the particularity that, according to $ab$ $initio$ calculations, the transition occurs thermodynamically at much higher pressure ($\sim$400 GPa) with a very small volume variation ($\Delta V=0.18$ bohr$^3$). The energy difference between the bcc and hcp phases at the transition pressure is very small ($\sim$2.5 meV/atom) in comparison with the energy barrier for the transition following the Burgers path ($\sim$33 meV/atom, see Sec. III A). Consequently, studying the transition path at constant pressure or constant volume should lead to similar results. Because the energy difference between

*Corresponding author: christophe.denoual@cea.fr

2475-9953/2020/4(6)/063609(12)
063609-1
©2020 American Physical Society

![](./images/812595251607764993_2.jpg)

FIG. 1. Burgers path describing the bcc-to-hcp transformation path. The volume-conserving shear deformation in the $[001]_{\text{bcc}}$ direction is the combination of a compression and a dilatation along $[001]_{\text{bcc}}$ and $[1\overline{1}0]_{\text{bcc}}$ (blue arrows), respectively. The hcp stacking is due to an atom shuffling of $\sqrt{2}a_0/6$ in the $[1\overline{1}0]_{\text{bcc}}$ direction (red arrows).

hcp and bcc phases is very small, beryllium could be seen as a model material to highlight the role of deformation induced by defects like dislocations to help the transition and its influence on the transition pressure. In the following, all simulations are performed at constant volume.

We emphasize that this study has been designed to under- stand how dislocations facilitate the direct bcc-to-hcp transi- tion and what consequences they have on the hcp microstruc- ture, and subsequently how the hcp-to-bcc inverse transition is impacted.

Through $ab$ initio calculations we examine the bcc-to- hcp-to-bcc pressure-induced martensitic transformation in Be containing a lattice of screw dislocations. Two approaches have been employed. The first one, so-called "shear-induced bcc-to-hcp-to-bcc transformation," consists of constraining the supercell to follow the shear deformation of the Burgers path at constant volume around the thermodynamic transition pressure. In the second one, so-called "pressure-induced bcc- to-hcp-to-bcc transformation," the supercell follows an im- posed deformation in volume. For all calculations, the ABINIT package was used [44,45]. The analysis of local strain, elastic deformation, and local atomic order was performed using the OVITO package [46]. Section II involves a description of the computational methods employed: cell construction, compu- tational details, and description of the bcc-hcp transformation. An additional convergence study of the transition pressure is reported in Appendix A. Section III contains the main results and discussion. First, a transition pathway without dis- locations (used as reference) is proposed and compared with literature data. Secondly, we present a description of the core structure of dislocations for both hcp and bcc phases. Thirdly, we discuss the transition under either hydrostatic pressure or uniaxial stress. Section IV is devoted to the conclusion.

![](./images/812595251607764993_3.jpg)

FIG. 2. Static atomic energy curves (eV/atom) as a function of atomic volume [bohr$^3$/atom] associated to bcc (Im3m), hcp (P6₃/mmc), and fcc (Fm3m) phases of perfect crystal Be. The hcp lattice is fully relaxed following the procedure described in Appendix A. The static energy differences (meV/atom) are reported in the inset.

## II. METHODS AND PRELIMINARY STUDIES

### A. Preparation of supercells

A nonorthogonal supercell with a quadrupolar arrange- ment of dislocations is defined following Ref. [47]. This arrangement was chosen for its ability to minimize the elastic interactions between dislocations [48]. The Bravais vectors of the supercell are defined by: $\overrightarrow{C}_{1}=n/3[11\overline{2}]$, $\overrightarrow{C}_{2}=\overrightarrow{C}_{1}/2+m/2[\overline{1}10]$ and $\overrightarrow{C}_{3}={^1/_2}[111]=\overrightarrow{b}$, where the $\text{C}_{1z}$ and $\text{C}_{2z}$ components are adjusted by choosing the integers $m$ and $n$, in order to ensure the periodicity of the bcc lattice. Only an even number of atoms in the $\overrightarrow{C}_{2}$ direction is compatible with the shuffle mechanism. The pairs $(m=17, n=10)$ and $(m=30$, $n=18$) are considered, thus leading to the construction of supercells containing 170 and 540 Be-atoms. A dipole of screw dislocations with antiparallel Burgers vectors $(-\overrightarrow{b}$ and $+\overrightarrow{b})$ is inserted into the bcc crystal in an easy core configuration using a quadrupolar arrangement. The volume of the supercell is equal to $V=a_0^3(\overrightarrow{C}_{1}, \overrightarrow{C}_{2}, \overrightarrow{C}_{3})$ where $a_0$ is the lattice parameter of bcc lattice and $(\overrightarrow{C}_{1}, \overrightarrow{C}_{2}, \overrightarrow{C}_{3})$ the triple product between vectors. Volume changes are prescribed by modifying $a_0$, whereas strain are imposed through modifica- tions of the Bravais vectors supercell, following a methodol- ogy described in Sec. II C.

### B. Computational details

The bcc-to-hcp martensitic transformation is pressure in- duced and supposed to be athermal [49]. All calculations are

performed at 0 K with the ABINIT 8.10.1 package [44,45,50]. The projector-augmented wave formalism [50] is used to expand the wave function. The valence electrons Be : $1s^22s^2$ and the Jollet–Torrent–Holzwarth [51] atomic data are used. The energy cutoff for the plane-wave expansion is 20 hartree. We use the Perdew-Burke-Ernzerhof exchange and correlation energy. The electronic and ionic convergences are performed for thresholds of $1 \times 10^{-9}$ hartree for the energy and $5 \times 10^{-4}$ hartree/bohrs for forces. A Gaussian smearing of 0.01 hartree is used. The simulation boxes containing screw dislocations are 170 and 540 Be-atom supercells with periodic boundary conditions as described above. $1 \times 2 \times 16$ and $1 \times 1 \times 16$ $k$-point grids are used for the Brillouin-zone sampling, respectively. Note that additional tests on the plane-wave energy cutoff and $k$ points are done to ensure the convergence of the transition pressure (see Appendix A). The numerical errors on calculated pressures, transition pressures, and total energies are estimated to be less than 0.05 GPa, 0.5 GPa, and 0.03 mhartree/atom, respectively.

In order to calculate the elastic constants associated with bcc and hcp lattices under high pressure and at 0 K, the stress tensor components for small strains are calculated using the method presented in Refs. [52,53]. The elastic constants are calculated using the local-density approximation (LDA). $40 \times 40 \times 40$ and $40 \times 40 \times 28$ $k$-point grids are used for the Brillouin-zone sampling for the bcc and hcp lattices, respectively. The ionic convergence is performed for a threshold of $1 \times 10^{-9}$ hartree/bohr. Unless otherwise stated, the conventional two-atom cells of the bcc and hcp lattices are considered at the generalized gradient approximation (GGA) transition volume, (i.e., isoenergetic bcc and hcp): $23.177$ bohr$^3$/atom at 0 K. The lattice parameters of the conventional hcp cell fully optimized in LDA are $a = 3.20997$ bohrs, $c = 5.19464$ bohrs, and $c/a = 1.618$.

### C. Shear-induced bcc-to-hcp transformation

Given a set of atoms in the bcc cell, we describe in this section their positions during the bcc-to-hcp transformation as a function of reaction coordinates for the shear deformation and the shuffle, according to the Burgers mechanism illustrated in Fig. 1 [12,18]. Let $p$ be the position of a given atom; the corresponding transformation reads $p \mapsto Up + t(p)$, where $U$ is the stretch tensor associated with shear and $t$ is the shuffle vector. The expression of the tensor $U$, in the reference bcc configuration, is defined as follows:

$$
U = \begin{bmatrix}
\frac{3}{4\sqrt{2}} + \frac{\sqrt{3}}{4\sqrt{2}}c/a & -\frac{3}{4\sqrt{2}} + \frac{\sqrt{3}}{4\sqrt{2}}c/a & 0 \\
-\frac{3}{4\sqrt{2}} + \frac{\sqrt{3}}{4\sqrt{2}}c/a & \frac{3}{4\sqrt{2}} + \frac{\sqrt{3}}{4\sqrt{2}}c/a & 0 \\
0 & 0 & \frac{\sqrt{3}}{2}
\end{bmatrix},
$$

where $c/a$ is the lattice ratio of the hcp cell. The shuffle is a translation that applies to one in two $\{110\}_{\text{bcc}}$ planes:

$$
t(p) = 0 \quad \text{ if } Up \in \{0001\}_{\text{hcp}}
$$

$$
t(p) = \frac{\sqrt{2}}{6}Uu \quad \text{ if not},
$$

where $u$ is a unit vector that gives the shuffle direction, i.e., the $\langle 1\overline{1}0 \rangle$ direction in the $\{110\}_{\text{bcc}}$ plane of interest. Depending on the initial $\{110\}_{\text{bcc}}$ plane, different specific orientations of hcp, so-called “variants,” can be generated. Since the shuffle direction is related to the shear mechanism, only the given of $U$ is relevant to identify a variant. Thereby, the method described in Ref. [54] is used to reach all possible hcp variants. In practice, it consists of rotating the tensor $U$ of a given variant, using point-group symmetries of the bcc lattice. Six distinct hcp variants are accessible from a unique bcc variant (see Table I).

<table>
<caption>Table I. Variants obtained for the bcc-to-hcp transformation.</caption>
<thead>
<tr>
<th>Variant</th>
<th>Plane of shear</th>
<th>Shuffle direction</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>(110)</td>
<td>$[1\overline{1}0]$</td>
</tr>
<tr>
<td>1</td>
<td>$(1\overline{1}0)$</td>
<td>$[\overline{1}10]$</td>
</tr>
<tr>
<td>2</td>
<td>(101)</td>
<td>$[10\overline{1}]$</td>
</tr>
<tr>
<td>3</td>
<td>$(\overline{1}01)$</td>
<td>$[\overline{1}0\overline{1}]$</td>
</tr>
<tr>
<td>4</td>
<td>(011)</td>
<td>$[01\overline{1}]$</td>
</tr>
<tr>
<td>5</td>
<td>$(0\overline{1}1)$</td>
<td>$[0\overline{1}\overline{1}]$</td>
</tr>
</tbody>
</table>

Intermediate states are obtained by a simple interpolation which is governed by the two order parameters $s$ and $\eta$, from 0 to 1:

$$
p \mapsto [I + s(U - I)][p + \eta U^{-1}t(p)].
$$

In this equation $I$ is the identity tensor. The determinant of $I + s(U - I)$ is not necessarily equal to 1 as written, hence the transformation from this tensorial representation is not isochoric. To study the transformation at constant volume, the tensor $I + s(U - I)$ is normalized at each step with respect to its determinant.

The couple $(s, \eta) = (0, 0)$ corresponds to the bcc phase, while $(1,1)$ corresponds to the hcp phase. Additional calculations are done to study the effect of the $c/a$ ratio. Only the conclusions are presented here. In the case of a dislocation-free bcc phase, the minimum energy path characterized by the $s$ and $\eta$ order parameters is marginally modified if one considers the ideal ($c/a = \sqrt{8/3}$) or calculated ($c/a = 1.6175$ at 405 GPa) $c/a$ ratio, the difference between these two paths being less than 4 meV/atom. In the case of a bcc phase containing a screw dislocation dipole and stating that the dislocation core structure is unchanged after the complete transformation, a $c/a$ ratio close to the ideal value has been calculated (1.638 for the variant 1 hcp at 254 GPa). For these reasons, only $c/a = \sqrt{\frac{8}{3}}$ is considered in this work to study the transition path of the bcc-hcp transformation.

## III. RESULTS AND DISCUSSION

### A. Dislocation-free bcc-to-hcp transformation

To identify the minimum energy path (MEP) associated with the dislocation-free bcc-to-hcp transformation, the two-dimensional PES at different volumes depending on $s$ and $\eta$ are calculated. The following lattice parameters $(a_0)$ for the bcc lattice are considered: 3.592, 3.786, and 4.110 bohrs. The associated pressures (before transformation) are equal to 395, 246, and 103 GPa, respectively. Only the energy surface for which the bcc and hcp phases are isoenergetic (3.592 bohrs), i.e., at the transition volume, is discussed in detail. For other


![](./images/812595251607764993_4.jpg)

FIG. 3. (a) A contour plot of the PESs as a function of shear $(s)$ and shuffle $(\eta)$ for $a_0 = 3.592$, 3.786, and 4.110 bohrs, respectively. The color scale corresponds to $\Delta E = E(s,\eta)-E_{\text{bcc}}$ (meV/atom). The white dotted curves show the MEPs. (b) Evolution of the energetic barrier with the supercell volume. The values in the plots (a) and (b) correspond to the lattice parameter $a_0$ (bohr).

$a_0$, only the MEP is considered. The variant 1, with a $(1\overline{1}0)$ shear plane and a $[\overline{1}\overline{1}0]$ shuffle direction, is considered in this section, but using another variant would be equivalent due to symmetry.

Figures 3(a) and 4 show the contour plot and the MEP characteristics (energy barrier, pressure, and von Mises stress) at the transition volume. The PES has two minima at (0,0) and (1,1) corresponding to bcc and hcp, respectively.

The two dimensions of the PES are not commensurate in our case (proportional to a shear angle for the $x$ axis, and proportional to a displacement for the $y$ axis), so that the gradient of the surface, $\nabla E(s,\eta)$, has no particular meaning. We therefore choose not to use a gradient-based method (e.g., string method or nudged elastic band) for the MEP. Instead, we define this path by imposing the shear (noted $s$), and by minimizing, for every $s$, the shuffle $\eta$. This is consistent with the hypothesis of a timescale shorter for the shuffle evolution than for the shear one [20], as discussed in Ref. [55]. The simulations discussed in Sec. III D seem to confirm this hypothesis.

The MEP can be decomposed in three stages. The first one, for $s$ from 0 to 0.42, is a step of pure shear. There is no shuffle and the system energy increases from 0 to 26.18 meV/atom. The pressure slightly increases by $\sim 1$ GPa (394.82 to 395.81) and the associated von Mises stress increases rapidly to 63.2 GPa. At this step, the intermediate structures are distorted bcc lattices. The bcc-to-hcp transition is thereby initiated by a pure shear deformation. This result is in agreement with that of Lu et al. [11], which considers the enthalpy surface at constant pressure in the $\alpha$(bcc)-$\varepsilon$(hcp) iron case. The partial shuffle at $s=0.43$ initiates the second stage which ends at $s=0.6$. This step is associated with a pressure increase (396 to 403 GPa) and a drop of the shear stress (from 63.2 to 9.4 GPa) probably because 76.7% of shuffle happens at this step. The transition state (TS) is reached for $s=0.5$ and corresponds to a local minimum of the von Mises stress. During the third stage ($s=0.6$–1.0), the coupled shear-shuffle process occurs smoothly, and the associated pressure is stabilized around 403 GPa, the maximum pressure being reached at $s=0.8$. The von Mises stress decreases progressively from 37.1 to 16.4 GPa.

The MEP at $a_0=3.592$ bohrs has an energy barrier ($\Delta E_{\text{MEP}}$) of 33.19 meV/atom and the range of transformation pressure ($\Delta P_{\text{MEP}}$) is equal to 8.5 GPa. The evolution upon decompression of the energetic barrier is reported in Fig. 3(b). $\Delta E_{\text{MEP}}$ and $\Delta P_{\text{MEP}}$ tend to decrease under decompression. Indeed, for $a_0=3.592\rightarrow3.786\rightarrow4.110$ bohrs, $\Delta E_{\text{MEP}}$ and $\Delta P_{\text{MEP}}$ evolve as follows: $33.19\rightarrow18.11\rightarrow3.31$ meV/atom and $8.5\rightarrow6.2\rightarrow3.9$ GPa, respectively. Benedict et al. calculated using DFT (GGA) an energy barrier of $\sim23$ meV/atom at $a_0=3.699$ bohrs ($\sim300$ GPa) [42], which is in agreement with our study. The existence of a barrier on the MEP around

![](./images/812595251607764993_5.jpg)

FIG. 4. MEP characteristics of the bcc-hcp transformation at $a_0=3.592$ bohrs and 0 K: (a) $\Delta E$ (meV/atom), (b) pressure (GPa), and (c) von Mises stress, noted as $\sigma^{\text{VM}}$ [GPa] as a function of shear. The blue dashed lines delimit the three stages of the MEP (see text) and the red circles indicate the position of the transition state.

250 and 100 GPa ($a_0=3.786$ and 4.110 bohrs, respectively) shows that the bcc phase is metastable at 100 GPa (i.e., 300 GPa lower than the transition pressure) with however an important decrease in the transformation energy [from 0 to $-57.09$ meV/atom; see Fig. 3(b)]. Otherwise, we stress that the bcc structure is mechanically stable: the calculated elastic constants for the bcc lattice at $a_0=4.110$ bohrs fulfill the following mechanical stability criteria: $C_{11}-C_{12}>0$ and $C_{33}(C_{11}+C_{12})-2C_{13}^2>0$ with $C_{11}=4.926$, $C_{12}=3.467$, and $C_{44}=4.657$ Mbar. From Fig. 3(a), we observe that the energetic barrier maximum associated with the MEP is shifted towards the low $s$ and $\eta$ values $[(0.5,0.567)\to(0.4,0.4)\to(0.25,0.367)]$, respectively. All the transformations can be induced by a pure shear, with the shear to transformation decreasing with decreasing pressure.

At the transition volume ($a_0=3.592$ bohrs), the elastic constants of the bcc and hcp lattices fulfill the mechanical stability criteria mentioned above: (i) in the bcc lattice, $C_{11}=13.830$; $C_{12}=9.566$; $C_{44}=9.188$ Mbar, and (ii) in the hcp lattice: $C_{11}=18.073$; $C_{33}=23.490$; $C_{12}=9.438$; $C_{13}=5.412$; $C_{44}=5.364$; $C_{66}=4.317$ Mbar. The Universal Elastic Anisotropy Index [56], denoted $A_U$, quantifies the degree of anisotropy of single crystals (with $A_U=0$ for isotropic materials). $A_U$ is equal to 3.05 for the bcc lattice. This rather high anisotropy index indicates that the results mentioned in the next section could be altered by the dislocation arrangement (here a quadrupolar arrangement), as discussed in the next section. The Universal Elastic Anisotropy Index of hcp lattice is nearly zero ($A_u=0.06$) as for ambient pressure hcp Be [56], thereby indicating a nearly perfectly isotropic behavior for the low-pressure phase.

### B. Core structure of dislocations under high pressure

In this part, we describe the core structure of dislocations in the bcc and hcp supercells under pressure. Their roles during the bcc-to-hcp-to-bcc transformation are presented in Secs. III C and III D.

#### 1. Bulk-cubic-centered phase

Figure 5 illustrates the elastic strain (obtained as the norm of the Green-Lagrange elastic strain measure, as provided by OVITO) at each Be atom in the relaxed bcc phase containing a screw dislocation dipole. The elastic strain magnitude is maximal at the dislocation core and it decreases away from the core. Although the shape of the dislocation core is compatible with the trifold symmetry imposed by the $\{110\}$ gliding planes, the quadrupolar interactions between dislocations modify the long range interactions, with noticeable strain localization along $[\overline{1}10]$ that can alter the onset of the transformation. This effect can be removed by using flexible boundary conditions [57,58], but only for dislocation flex in a homogeneous crystal and thus not for the onset of a phase transformation with dislocations.

![](./images/812595251607764993_6.jpg)

FIG. 5. Norm of the Green-Lagrange elastic strain, as defined by Ovito [46] in the relaxed 540-Be-atom supercell at 396 GPa.

![](./images/812595251607764993_7.jpg)

FIG. 6. (a) Differential displacement map on the (111) plane at the screw dislocation core $+\vec{b}$ for the 540-atom supercell at 396 GPa. The atoms of defect-free bcc crystals are represented by circles and the color indicates the relative position of the successive (111) atomic planes. (b) Notation used to calculate the polarization index. (c) Evolution of the polarization index as a function of pressure (GPa) and the size of the supercell.

We investigated the equilibrium core structure of dislocations in the bcc phase at 0 K and different pressures. The differential displacement (DD, see for a definition Ref. [59]) map of the screw component, presented in Fig. 6(a) and obtained after minimizing the energy with respect to atom positions, reveals a strongly polarized core structure.

To quantify the polarization, we also calculated the polarization index $p$ [Figs. 6(b) and 6(c)]:

$$
p=\frac{|d(AB)-d(AF)|+|d(CD)-d(CB)|+|d(EF)-d(ED)|}{|\vec{b}|},
$$

where $d(ij)$ represents the differential displacement along the [111] direction between atoms $i$ and $j$ with respect to the perfect bcc lattice. A fully symmetric (=compact) and an asymmetric (=polarized) dislocation core are characterized by $p=0$ and 1, respectively. This polarization is plotted as a function of pressure for the 170- and 540-atom supercells in Fig. 6(c). At 427 GPa, $p=0.86$ and increases with decreasing pressure, reaching a full polarization ($p=1$) at approximately 200 GPa. Interestingly, this evolution is strongly dependent on

![](./images/812595251607764993_8.jpg)

FIG. 7. (a) Differential displacement map (the atoms of the defect-free hcp crystal are represented by circles and the color indicates their relative positions), and (b) adaptive common neighbor analysis [46] associated with one extended dislocation in the variant 5 for the 540-atom supercell at 403 GPa.

the supercell size, with the 170-atom supercell giving stronger $p$, a possible consequence of dislocations interaction.

Note that beryllium (this study) and magnesium [29], both alkaline earth metals, have a strongly polarized core structure, while a compact core structure is identified in many transition metals such as Ta, Mo, Fe, W, V, Nb, and Cr using $ab$ initio calculations [60–64].

### 2. Hexagonal close-packed phase
In order to identify the core structure of dislocations in the hcp phase, we apply for $a_0=3.592$ bohrs the complete bcc-to-hcp transformation (e.g., we use the variant 5 of Table I), as described in Sec. II C, on nonrelaxed (compact core) and relaxed (polarized core) bcc structures. Then, the obtained structures are relaxed. In both cases, the dislocation core dissociates in the basal plane into two partial dislocations of type $\frac{1}{3}\langle 1\overline{1}00\rangle_{\text{hcp}}$ connected together by a stacking fault ribbon (see Fig. 7), as previously observed in another study in the hcp phase of Mg [65,66]. During the bcc-to-hcp transformation, the shuffle has to be applied to one in two shuffle planes, which is not possible for screw dislocations connecting these planes through the lattice distortion. For $\pm\frac{1}{2}[111]$ screw dislocations, this limits the topologically acceptable transformations to variants $n^\circ 1,3$, and 5 (see Table I) [67]. For these three variants, a dipole of extended dislocations is observed.

Obtaining a basal stacking fault for the hcp dislocation core from the initial bcc trifold core is an indication that this structure is probably amongst the most stable one for this phase. It is however important to notice that this core is inherited from the initial bcc core and the Burgers path; both could have influenced the selection of this particular structure. Assessing the stability of all core structures would require a dedicated study, as discussed for example in Ref. [68].

We apply the hcp-to-bcc shear deformation (same variant as the dislocation-free bcc-to-hcp transformation) on the relaxed hcp structure containing a dipole of extended dislocations. During the relaxation of this structure, the reverse shuffle occurs and the core structure of the dislocations evolves into the initial polarized core structure, thus demonstrating a fully reversible behavior. This evolution is detailed for all the range of shear components $(s)$ in the next section.

### C. Shear-induced bcc-to-hcp-to-bcc transformation
In this section, only the shear deformation is prescribed so that both dislocation core structure and shuffle are outputs of the relaxation. For the bcc-to-hcp transition, one important aspect is that the dislocations could move during the relaxation when a low shear is applied due to the very low Peierls stress of basal dislocations in hcp. In order to limit the effects of elastic interactions on the energy barrier, we consider the fully transformed bcc and hcp phases as a starting point for all shears (for the direct and reverse paths, respectively) [69]. The local structural environment of each atom is identified with the adaptive Common Neighbor Analysis as implemented in OVITO [46].

We apply a global shear deformation on the $(1\overline{1}0)$ plane, which favors the variant 1 (see Table I). The bcc-to-hcp transformation is initiated at $s=0.27$. Contrary to the dislocation-free case in which the shuffle occurs homogeneously in the supercell under shear, the variant 1 hcp nucleates between the two dislocations at $s=0.27$ [see the relevant snapshot in Fig. 8(a)], with the corresponding shuffle. In this figure, only the nearest lattice structures (hcp, fcc, or bcc) are plotted without indicating the elastic lattice strain. The interfaces between different phases are thus indicative only. Then, the increase of $s$ induces the propagation of hcp around dislocations. The intermediate structure at $s=0.825$ shows that the propagation ends before full transformation, leaving a zone around the dislocation core untransformed. The inverse mechanism (nucleation and propagation) occurs during the reversion (hcp-to-bcc), inducing a complete reconstruction of the polarized dislocation core structure (see Sec. III B). Finally, Fig. 8(b) shows that the direct and reverse pressure-shear (or $P$-$s$) curves are not equivalent, which originates from the fact that the nucleation starts in the direct and reverse paths from dislocations of different natures, i.e., from trifold symmetry dislocations in bcc for the direct path and from two dislocation partials in hcp for the reverse path. In particular, the intensities of shear induced by these two dislocations are

![](./images/812595251607764993_9.jpg)

FIG. 8. (a) Energy profiles (eV) associated with the bcc-to-hcp transformation (blue) and its reversion (orange) with (blue and orange) and without (black) dislocations in the 540-atom supercell. Atoms are colored according to their local structural environment. (b) Pressure (GPa) change during the bcc-to-hcp and hcp-to-bcc transition processes.

different. The presence of dislocations slightly reduces the variation of pressure during the transition by 0.6 GPa: from 8.5 to 7.9 GPa.

The energy barriers are reported in Fig. 8(a) as a function of the shear intensity $s$. The bcc-to-hcp and hcp-to-bcc energy profiles are similar despite some dislocation motions, in particular in the direct path. Although the energies of bcc and hcp were equal without dislocations, the simulations [Fig. 8(a)] show that the excess energy induced by dislocations is higher (+0.715 eV/dislocation) for the hcp phase. This could be explained by stronger elastic interactions, an effect that cannot be easily quantified through our $ab$ initio results.

To identify the strain that drives the transformation, we calculated the local von Mises shear strain [46] at each atom. The deformation induced by the dislocation adds to the imposed shear deformation from the Burgers mechanism. This creates important inhomogeneous shear regions that foster the transition. Notably and interestingly, considering the MEP of the dislocation-free case (see Fig. 3), no atomic shuffle is visible when the shear is below $\sim$0.4. With dislocations, the local shear appears to be larger than the imposed shear, so that the atomic shuffle in those regions starts at lower imposed shears [below 0.3, see Fig. 8(a)].

Our results thus prove that the dislocations foster the phase transition. We focused on shear-induced transformations which obviously favored one variant. In what follows, we study the transformation under pressure without the imposed shear from the Burgers mechanism. The variants nucleate directly from the relaxation.

### D. Pressure-induced bcc-to-hcp-to-bcc transformation

The P-V curve associated with the bcc-to-hcp transformation and its reversion are reported in Fig. 9. The starting point is the bcc phase at 396 GPa ($a_0 = 3.592$ bohrs). Then, an increase in the $a_0$ parameter decreases the pressure down to 1 GPa ($a_0 = 4.740$ bohrs). The transformation reversion starts at 59 GPa ($a_0 = 4.300$ bohrs) and ends at 396 GPa ($a_0 = 3.592$ bohrs).

![](./images/812595251607764993_10.jpg)

FIG. 9. $P$-$V$ hysteresis of the bcc-to-hcp-to-bcc transformation under homogeneous deformation for the 540-atom supercell. The bcc-to-hcp and hcp-to-bcc transformations are in blue and red, respectively.

First, the transition takes place with dislocations, whereas it does not happen without dislocations. Secondly, a hysteresis is observed on the $P$-$V$ curve in the presence of dislocations.

Let us discuss the transition under decreasing pressure, using Fig. 9: at 93 GPa, the bcc-to-hcp transformation starts and occurs partially only. At 72 GPa, the transformation is completed. As shown in the dislocation-free case in Fig. 3, the energy barrier decreases (from 33.2 to 3.3 meV) when the pressure decreases (from 395 to 103 GPa). Despite this, the transformation did not take place spontaneously in the dislocation-free bcc phase. Moreover, we observed that the energy barrier maximum is shifted toward the low $s$ (Fig. 3). Here, the decisive point is that the shear deformation of

![](./images/812595251607764993_11.jpg)

FIG. 10. (a) Structural description of the phase at 59 GPa for the 540-atom supercell. (b) Schematization of this supercell: twin boundaries and other grain boundaries are in blue and orange, respectively. Labels (1, 3, and 5) correspond to hcp variants as defined in Table I and green lines correspond to the trace of the (0001) hcp variant basal planes.

dislocations initiates the bcc-to-hcp transformation when the energy barrier tends to disappear. The final structure has three grains, corresponding to the three variants topologically compatible with the dislocation orientation (see Fig. 10). Some grain boundaries can be interpreted as twin boundaries represented in blue in Fig. 10(b), as shown by the trace of the (0001) hcp basal planes. Interestingly, Poschmann *et al.* [25] also observed the coexistence of variants in titanium using a large number of atoms and a semiempirical potential. We obtain similar results despite a limited number of atoms but using *ab initio* calculations.

Turning to the transformation reversion, it starts at around 120 GPa. The hcp-to-bcc transformation initiates at grain boundaries and triple junctions, as shown in the intermediate structure obtained at 215 GPa (Fig. 9). At 306 GPa, the transformation is not finished but a bcc variant emerges. At 396 GPa, the reversion is completed and the final structure is stabilized into the initial bcc lattice containing a small inclusion of bcc, discernible through the non-bcc surrounding atoms (in blue in Fig. 9), without any visible dislocation.

The hysteresis in pressure comes from the fact that the microstructure produced at 72 GPa is particularly stable, and it requires a very high pressure to transit into the bcc phase.

To understand the microstructure at 396 GPa, we calculated the transformation gradient $F_i$ by defining the displacement as the difference between this final (reverted) state and a defect-free bcc lattice. The Green-Lagrange deformation tensors $E_i = \frac{1}{2}(F^T \cdot F - I)$, calculated for all atoms $i$, are then compared to one of the 13 theoretical deformations $F_r$ (with $r$ between 0 and 12) for reverted bcc (see Appendix B). For an atom $i$, the best matching reversion index $r$ is the argmin of the distance $d(r) = |E_i - E_r|$, with $E_r$ the Green-Lagrange deformation of $F_r$. Figure 11 shows both indexes $r$ and distances, the latter indicating the quality of the match, bright colors standing for a short distance and thus a good match. Surprisingly, the bcc inclusion is made of three zones, each associated with a reversion matrix at an acceptable accuracy, although only one crystalline orientation can be detected in the inclusion. The triple junction where these three zones meet (at the inclusion center in Fig. 11) corresponds to the grain triple junction of the hcp basis (see Fig. 10), with a different orientation for each grain. These vestigial deformations are then the result of three complex transformation pathways, which in the end turn out to lead to one single bcc orientation. Determining the transformation path only by using the final lattice orientation (e.g., from experimental results) thus proves to be sometimes insufficient to establish the transformation paths.

![](./images/812595251607764993_12.jpg)

FIG. 11. Top: nearest deformation matrices represented in color by their indexes and shades (distance to the transformation best match). Atoms in black correspond to deformations absent of the reversions list (e.g., the black horizontal line on the left part of the figure, which corresponds to the deformation left by the destruction of a dislocation dipole). The three main reversions (5 in purple, 8 in blue, and 10 in green) are arranged in a self-equilibrated zone, as discussed in the main text. Bottom: a slice (highlighted in red in the top view) shows that the inclusion is composed of two deformations (teal and purple), but one single lattice orientation.

The transformation tensors associated with these reverted zones have no volume deformation $[\det(F_r) = 1]$, i.e., are mainly of deviatoric nature. Since the deformations are important ($|E| \approx 0.25$), the question of their stability can be posed. The reverted zones are spread over equivalent volumes, and the average deformation for the inclusion $\tilde{E}$, approximated by $\tilde{E} = (E_5 + E_8 + E_{10})/3$, is very small $(|\tilde{E}| = 0.03)$. These three reversion transformations are thus self-accommodating and stable (in our calculation), at least at 0 K.

### IV. SUMMARY AND CONCLUSIONS

To better understand the mechanism by which bcc transits towards hcp under high pressure, we have first analyzed the dislocation-free bcc-to-hcp transformation. A simple tensorial representation permits us to transform the square lattice into a hexagonal one with no volume change. The atomic shuffle restores the hcp stacking. We report a two-dimensional energy surface depending on shear and shuffle as order parameters. A decomposition of the minimum energy path in three steps highlights, prior to complete transition: (i) a pure shear which is characterized by a high increase in von Mises stress (up to 63.2 GPa), (ii) a sudden atomic shuffle during which the pressure increases strongly, and (iii) a coupled shear-shuffle process occurring smoothly with a stabilization of the pressure. This transition, based on a homogeneous shear deformation at each atom and a simultaneous atomic shuffle, cannot spontaneously occur because of the energetic barrier of $33.2^*n_{\text{Be}}$ meV, with $n_{\text{Be}}$ the number of Be atoms in the supercell.

We propose a study dealing with dislocations-bcc/hcp transformation coupling. Two bcc-to-hcp-to-bcc transition modes are investigated:

(i) The reversible shear-induced transformation at constant volume

The elastic strain due to screw dislocations adds to the shear deformation from the Burgers mechanism. The consequence is that the shuffle occurs earlier under shear compared with the dislocation-free case because of local concentration of shear deformation. This results in a gradual bcc-to-hcp/hcp-to-bcc transformation (nucleation and propagation) around dislocations. Our results prove that the dislocations induce unambiguously a decrease in the global energy barrier. In the hcp phase, the screw dislocations dissociate in the basal plane into extended dislocations. The parent bcc and the screw dislocation core are regenerated after a complete cycle (bcc-to-hcp-to-bcc). Only the variant compatible with the applied shear deformation appears in the supercell.

(ii) The irreversible pressure-induced transformation

The dislocations clearly facilitate the bcc-to-hcp transformation because it happens spontaneously at around 90 GPa. In particular, the shear deformation of dislocations allows initiating the bcc-to-hcp transformation when the energy barrier tends to disappear. Furthermore, this study demonstrates that the screw dislocations impose a variant selection (orientation, position). The obtained structures after complete transformation have structural characteristics similar to those of microstructures (grain, grain boundary, triple junction). During the hcp-to-bcc reversion, the created defaults, i.e., grain boundaries and triple junctions, also become nucleation sites for the bcc phase. Our analysis of the bcc child (after reversion) proves that the transformation paths connecting the final and initial lattice orientations can be more complex.

Our results also show that a supercell with 540 atoms containing a dipole of screw dislocations can be used, despite its reduced sizes, for an extended analysis of the coupling between dislocations and bcc-hcp transformation. The reliability of the *ab initio* calculations for beryllium, for both dislocation core structure and the mechanism of phase transformation, allows for a discussion about this coupling, without adding the difficulty of the fitting of a molecular-dynamics potential. From this point of view, these first-principles calculations, and especially the microstructure induced by the dislocations, are of high interest for bcc-hcp transformations in general.

<table>
<caption>TABLE II. Convergence study of $P_{\text{trans}}$ in function of the plane-wave energy cutoff and $k$-point grids.</caption>
<thead>
  <tr>
    <th colspan="2">$k$-point grid</th>
    <th colspan="4">Cutoff energy (hartree)</th>
  </tr>
  <tr>
    <th>bcc</th>
    <th>hcp</th>
    <th>16</th>
    <th>20</th>
    <th>30</th>
    <th>40</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>10 10 10</td>
    <td>10 10 7</td>
    <td>308</td>
    <td>320a</td>
    <td>326.5</td>
    <td>328</td>
  </tr>
  <tr>
    <td>20 20 20</td>
    <td>20 20 14</td>
    <td>388.5</td>
    <td>414</td>
    <td>412</td>
    <td>413</td>
  </tr>
  <tr>
    <td>30 30 30</td>
    <td>30 30 21</td>
    <td>383.5</td>
    <td>408.5</td>
    <td>406.5</td>
    <td>407.5</td>
  </tr>
  <tr>
    <td>40 40 40</td>
    <td>40 40 28</td>
    <td>380</td>
    <td>405</td>
    <td>403</td>
    <td>404</td>
  </tr>
  <tr>
    <td>50 50 50</td>
    <td>50 50 35</td>
    <td>379.5</td>
    <td>404.5</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="6">aCalculated using the plane-wave energy cutoff of 18 hartree.</td>
  </tr>
</tfoot>
</table>

### ACKNOWLEDGMENT

This work was supported by the SMICE Project, which was funded by BPI France.

### APPENDIX A: TRANSITION PRESSURE AND CONVERGENCE TESTS

We have assessed the impact of the plane-wave energy cutoff and $k$ points on the thermodynamic transition pressure, noted as $P_{\text{trans}}$. At 0 K, $P_{\text{trans}}$ corresponds to the pressure at which the bcc and hcp enthalpies are equal.

We set the space group to $Im3m$ for the bcc unit cell with one atom (primitive cell) and to $P6_3/mmc$ for the hcp cell with two atoms (conventional cell). The hcp lattice is fully relaxed at constant volume. The transitions pressures, defined by the transition hcp-to-bcc for decreasing volume, are reported in Table II. We have also checked that the fcc phase ($Fm3m$) is never the most stable phase for all pressures (see Fig. 2).

Our convergence study shows that the 20-hartree and $40 \times 40 \times 40$ grid parameters give a $P_{\text{trans}}$ value (405 GPa) sufficiently converged. 405 GPa is used as reference to verify that the $1 \times 2 \times 16$ grid used for the 170-Be-atom supercell is sufficient. A value of 406 GPa has been calculated for the 170-Be-atom supercell validating the convergence of data in using the $1 \times 2 \times 16$ grid. We have also studied the effect of the $c/a$ ratio on $P_{\text{trans}}$ for the Be two-atom cell (hcp structure) and the 170-Be-atom supercell. In both cases, an ideal value of $c/a$, i.e., $\sqrt{\frac{8}{3}}$, reduces the $P_{\text{trans}}$ value by 6 GPa.

### APPENDIX B: CALCULATION OF THE REVERSION MATRICES

The methodology used to generate the reversion matrices from a martensitic transformation is presented in details in Refs. [54] and [70]. We considered the Burgers transformation $U$ given in Sec. II C with a $c/a$ ratio of 1.618. This transformation was then expressed in the frame used for the *ab initio* calculations: $[11\bar{2}]\parallel x$, $[\bar{1}10]\parallel y$, and $[111]\parallel z$ (this transformation is noted as $\bar{U}$). The point-group rotations $R_{i,\ \text{bcc}}$ for the bcc phase, in this latter basis, is used to generate all variants hcp (defined by their transformations $\bar{U}_i$), starting from $\bar{U}$, by using $\bar{U}_i = R_{i,\text{bcc}}^T \cdot \bar{U} \cdot R_{i,\text{bcc}}$. The point-group rotations $R_{j,\ \text{hcp}}$

of the hcp basis induced by a Burgers transformation (thus expressed so that $(0001)_{\mathrm{hcp}} \|(\overline{1} 10)_{\mathrm{bcc}}$ and $[\overline{2} 110]_{\mathrm{hcp}} \|[001]_{\mathrm{bcc}}$, with the bcc lattices defined after the rotation $R_{i, \text { bcc }}$ ) is used to generate the reversions transformations: $\bar{V}_{j}=R_{j, \text { hcp }}^{T} \cdot \bar{U}_{j}^{-1}$.
$R_{j, \mathrm{hcp}} \cdot \bar{U}_{j}$. Due to the transformation symmetries, only 6 forward transformations are unique, leading to 13 (or $12+1$ ) possible bcc orientations after reversion. Transformation strain tensors for bcc variants are given in Ref. [70].

[1] Z. Nishiyama, *Martensitic Transformation* (Academic Press, New York, 1978).

[2] A. L. Roytburd, Kurdjumov and his school in martensite of the $20^{\text {th }}$ century, *Mater. Sci. Eng. A* **273-275**, 1 (1999).

[3] H. L. Skriver, Calculated Structural Phase Transitions in the Alkaline Earth Metals, *Phys. Rev. Lett.* **49**, 1768 (1982).

[4] A. Moriarty and A. K. McMahan, High-Pressure StructuralPhase Transitions in Na, Mg, and Al, *Phys. Rev. Lett.* **48**, 809(1982).

[5] W. Petry and J. Neuhaus, *Martensitic Phase Transitions, PSI- Proceedings 96-02*, edited by A. Furrer (Paul Scherrer Institut, Villigen, 1996), pp. 293–315.

[6] G. Robert, P. Legrand, and S. Bernard, Multiphase equation of state and elastic moduli of solid beryllium from first principles, *Phys. Rev. B* **82**, 104118 (2010).

[7] G. Grimvall, B. Magyari-Köpe, K. A. Persson, and Ozolinš, Lattice instabilities in metallic elements, *Rev. Mod. Phys.* **84**,945 (2012).

[8] H. Olijnyk and W. B. Holzapfel, High-pressure structural phase transition in Mg, *Phys. Rev. B* **31**, 4682 (1985).

[9] M. Ekman, B. Sadigh, K. Einarsdotter, and P. Blaha, Ab initio study of the martensitic bcc-hcp transformation in iron, *Phys. Rev. B* **58**, 5296 (1998).

[10] M. Friák and M. Šob, Ab initio study of the bcc-hcp transfor- mation in iron, *Phys. Rev. B* **77**, 174117 (2008).

[11] Z. Lu, W. Zhu, T. Lu, and W. Wang, Does the fcc phase exist in the Fe bcc-hcp transition? A conclusion from first-principles studies, *Model. Simul. Mater. Sci. Eng.* **22**, 025007 (2014).

[12] W. G. Burgers, On the process of transition of the cubic-body- centered modification into the hexagonal-close-packed modifi- cation of zirconium, *Physica* **1**, 561 (1934).

[13] Y. Chen, K. M. Ho, and B. N. Harmin, First-principles study of the pressure-induced bcc-hcp transition in Ba, *Phys. Rev. B* **37**,283 (1988).

[14] H. G. Bowden and P. M. Kelly, The crystallography of the pressure induced phase transformations in iron alloys, *Acta Metall.* **15**, 1489 (1967).

[15] A. Dewaele, C. Denoual, S. Anzellini, F. Occelli, M. Mezouar, P. Cordier, S. Merkel, M. Véron, and E. Rausch, Mechanism of the $\alpha-\varepsilon$ phase transformation in iron, *Phys. Rev. B* **91**, 174105(2015).

[16] S. R. Nishitani, H. Kawabe, and M. Aoki, First-principles calculations on bcc-hcp transition of titanium, *Mater. Sci. Eng. A* **312**, 77 (2001).

[17] A. Junkaew, B. Ham, X. Zhang, A. Talapatra, and R. Arróyave, Stabilization of bcc Mg in thin films at ambient pressure: Experimental evidence and *ab initio* calculations, *Mater. Res. Lett.* **1-3**, 161 (2013).

[18] H.-K. Mao, W. A. Bassett, and T. Takahashi, Effect of pres- sure on crystal structure and lattice parameters of iron up to300 kbar, *J. Appl. Phys.* **38**, 272 (1967).

[19] J. B. Liu and D. D. Johnson, bcc-to-hcp transformation path- ways for iron versus hydrostatic pressure: Coupled shuffle and shear modes, *Phys. Rev. B* **79**, 134113 (2009).

[20] D. F. Johnson and E. A. Carter, Nonadiabaticity in the iron bcc to hcp phase transformation, *J. Chem. Phys.* **128**, 104703(2008).

[21] V. V. Dremov, G. V. Ionov, F. A. Sapozhnikov, N. A. Smirnov, A. V. Karavaev, M. A. Vorobyova, and M. V. Ryzhkov, MD modeling of screw dislocation influence upon initiation and mechanism of BCC-HCP polymorphous transition in iron, *EPJ Web Conf.* **94**, 04023 (2015).

[22] Y. Huang, Y. Xiong, P. Li, X. Li, S. Xiao, H. Deng, W. Zhu, and W. Hu, Atomistic studies of Shick-induced plasticity and phase transition in iron-based single crystal with coin dislocation, *Int. J. Plast.* **114**, 215 (2019).

[23] J. Meiser and H. M. Urbassek, Dislocations help initiate the $\alpha-\gamma$ phase transformation in iron-an atomistic study, *Metals* **9**, 90(2019).

[24] B. Li, X. M. Zhang, P. C. Clapp, and J. A. Rifkin, Molecular dynamics simulations of the effects of defects on martensite nucleation, *J. Appl. Phys.* **95**, 1698 (2004).

[25] M. Poschmann, J. Lin, H. Geerlings, I. S. Winter, and D. C. Chrzan, Strain-induced variant selection in heterogeneous nucleation of $\alpha$-Ti at screw dislocations in $\beta$-Ti, *Phys. Rev. Mater.* **2**, 083606 (2018).

[26] H. T. Luu, R. G. A. Veiga, and N. Gunkelmann, Atomistic study of the role of defects on $\alpha \to \varepsilon$ phase transformations in iron under hydrostatic compression, *Metals* **9**, 1040 (2019).

[27] Y. Wang and A. G. Khachaturyan, Multi-scale phase field approach to martensitic transformations, *Mater. Sci. Eng.: A* **438-440**, 55 (2006).

[28] D. C. Chrzan, M. P. Sherburne, Y. Hanlumyuang, T. Li, and J. W. Jr Morris, Spreading of dislocation cores in elastically anisotropic body-centered-cubic materials: The case of gum metal, *Phys. Rev. B* **82**, 184202 (2010).

[29] I. S. Winter, M. Poschmann, T. Tsuru, and D. C. Chrzan, Dislo- cations near elastic instability in high-pressure body-centered- cubic magnesium, *Phys. Rev. B* **95**, 064107 (2017).

[30] D. Dragoni, T. D. Daff, G. Csányi, and N. MarzariAchieving DFT accuracy with a machine-learning interatomic potential: Thermomechanics and defects in bcc ferromagnetic iron, *Phys. Rev. Mater.* **2**, 013808 (2018).

[31] D. A. Young, *Phase Diagrams of the Elements* (University of California Press, Oxford, England, 1991).

[32] Y. Lu, T. Sun, Ping Zhang, P. Zhang, D. B Zhang, and R. M. Wentzcovitch, Premelting hcp to bcc Transition in Beryllium, *Phys. Rev. Lett.* **118**, 145702 (2017).

[33] J. W. Xian, J. Yan, H. F. Liu, T. Sun, G. M. Zhang, X. Y. Gao, and H.-F. Song, Effect of anharmonicity on the hcp to bcc transition in beryllium at high-pressure and high-temperature conditions, *Phys. Rev. B* **99**, 064102 (2019).

[34] A. Lazicki, A. Dewaele, P. Loubeyre, and M. Mezouar, High- pressure-temperature phase diagram and the equation of state of beryllium, Phys. Rev. B 86, 174118 (2012).

[35] K. Kádas, L. Vitos, B. Johansson, and J. Kollár, Structural stability of $\beta$-beryllium, Phys. Rev. B 75, 035132 (2007).

[36] J. Meyer-ter-Vehn and W. Zittel, Electronic structure of mat- ter at high compression: Isostructural transitions and ap- proach of the Fermi-gas limit, Phys. Rev. B 37, 8674 (1988).

[37] B. Palanivel, R. S. Rao, B. K. Godwal, and S. K. Sikka, On the relative stability of orthorhombic and hcp phases of beryllium at high pressures, J. Phys.: Condens. Matter 12, 8831 (2000).

[38] P. K. Lam, M. Y. Chou, and M. L. Cohen, Temperature-induced and pressure-induced crystal phase-transitions in Be, J. Phys. C: Solid State Physics 17, 2065 (1984).

[39] A. Hao and Y. Zhu, First-principle investigations of structural stability of beryllium under high pressure, J. Appl. Phys. 112, 023519 (2012).

[40] G. Robert and A. Sollier, Equation of state and elastic properties of beryllium from first principles calculations, J. Phys. IV France 134, 257 (2006).

[41] F. Luo, L.-C. Cai, X.-R. Chen, F.-Q. Jing, and D. Alfe, Ab initio calculation of lattice dynamics and thermodynamic properties of beryllium, J. Appl. Phys. 111, 053503 (2012).

[42] L. X. Benedict, T. Ogitsu, A. Trave, C. J. Wu, P. A. Sterne, and E. Schwegle, Calculations of high-pressure properties of beryllium: Construction of a multiphase equation of state, Phys. Rev. B 79, 064106 (2009).

[43] Y. Cheng, H.-H. Chen, F.-X. Xue, G.-F. Ji, and M Gong, Phase transition, elastic and thermodynamic properties of beryl- lium via first principles, Int. J. Mod. Phys. B 27, 1350130 (2013).

[44] X. Gonze, F. Jollet, F. Abreu Araujo, D. Adams, B. Amadon, T. Appelencourt, C. Audouze, J. M. Beuken, J. Bieder, A. Bokhanchuk, E. Bousquet, F. Bruneval, D. Caliste, M. Côté, F. Dahm, F. Da Pieve, M. Delaveau, M. Di Gennaro, B. Dorado, C. Espejo, G. Geneste, L. Genovese, A. Gerossier, M. Giantomassi, Y. Gillet, D. R. Hamann, L. He, G. Jomard, J. Laffamme Janssen, S. Le Roux, A. Levitt, A. Lherbier, F. Liu, I. Lukačević, A. Martin, C. Martins, M. J T Oliveira, S. Poncé, Y. Pouillon, T. Rangel, G. M. Rignanese, A. H. Romero, B. Rousseau, O. Rubel, A. A. Shukri, M. Stankovski, M. Torrent, M. J. Van Setten, B. Van Troeye, M. J. Verstraete, D. Waroquiers, J. Wiktor, B. Xu, A. Zhou, and J. W. Zwanziger, Recent developments in the ABINIT software pack- age, Comput. Phys. Commun. 205, 106 (2016).

[45] X. Gonze, B. G. Amadon, F. Antonius, L. Arnardi, J.-M. Baguet, J. Beuken, F. Bieder, J. Bottin, E. Bouchet, N. Bousquet, F. Brouwer, G. Bruneval, T. Brunin, J.-B. Cavignac, W. Charraud, M. Chen, S. Côté, J. Cottenier, G. Denier, P. Geneste, M. Ghosez, Y. Giantomassi, O. Gillet, D. R. Gingras, G. Hamann, X. Hautier, N. N, A. W. Helbig, Y. Holzwarth, F. Jia, W. Jollet, L. Lafargue-Dit-Hauret, M. A. L. Lejaeghere, A. Marques, C. Martin, H. P. C. Martins, F. Miranda, K. Naccarato, G. Persson, V. Petretto, Y. Planes, S. Pouillon, F. Prokhorenko, G.-M. Ricci, A. H. Rignanese, M. M. Romero, M. Schmitt, M. J. Torrent, B. van Setten, Van Troeye, M. J. G. Verstraete, and J. W. Zérah, Zwanziger The ABINIT project: Impact, environment and recent developments, Comput. Phys. Commun. 248, 107042 (2020).

[46] A. Stukowski, Visualization and analysis of atomistic simu- lation data with OVITO-the Open Visualization Tool, Model. Simul. Mater. Sci. Eng. 18, 015012 (2010).

[47] E. Clouet, L. Ventelon, and F. Willaime, Dislocation Core Energies and Core Fields from First Principles, Phys. Rev. Lett. 102, 055502 (2009).

[48] E. Clouet, in Ab Initio Models of Dislocations in Handbook of Materials Modeling, edited by W. Andreoni and S. Yip (Springer International Publishing, Cham, 2019), pp. 1-22.

[49] D. E. Laughlin, N. J. Jones, A. J. Schwartz, and T. B. Massalski, Thermally activated martensite: Its relationship to non-thermally activated (athermal) martensite, in Proceedings of ICOMAT-08, edited by G. B. Olsen, D. S. Lieberman, and A. Saxena (The Minerals, Metals & Materials Society, Carnegie Institute of Technology, 2009), pp. 141-144.

[50] M. Torrent, F. Jollet, F. Bottin, G. Zerah, and X. Gonze, Im- plementation of the projector augmented-wave method in the ABINIT code, Comput. Mater. Sci. 42, 337 (2008).

[51] F. Jollet, M. Torrent, and N. Holzwarth, Generation of pro- jector augmented-wave atomic data: A 71 element validated table in the XML format, Comput. Phys. Commun. 185, 1246 (2014).

[52] D. R. Hamann, X. Wu, K. M. Rabe, and D. Vanderbilt, Metric tensor formulation of strain in density-functional perturbation theory, Phys. Rev. B 71, 035117 (2005).

[53] A. Martin, M. Torrent, and R. Caracas, Projector augmented- wave formulation of response to strain and electric-field pertur- bation within density functional perturbation theory, Phys. Rev. B 99, 094112 (2019).

[54] C. Denoual and A. Vattré, A phase field approach with a reac- tion pathways-based potential to model reconstructive marten- sitic transformations with a large number of variants, J. Mech. Phys. Solids 90, 91 (2016).

[55] B. Dupé, B. Amadon, Y. P. Pellegrini, and C. Denoual, Mech- anism for the $\alpha \to \varepsilon$ phase transition in iron, Phys. Rev. B 87, 024103 (2013).

[56] S. I. Ranganathan and M. Ostoja-Starzewski, Universal Elastic Anisotropy Index, Phys. Rev. Lett. 101, 055504 (2008).

[57] M. R. Fellinger, A. M. Z. Tan, L. G. Hector Jr., and D. R. Trinkle, Geometries of edge and mixed dislocations in bcc Fe from first-principles calculations, Phys. Rev. Mater. 2, 113605 (2018).

[58] A. M. Z. Tan, C. Woodward, and D. R. Trinkle, Dislocation core structures in Ni-based superalloys computed using a density functional theory based flexible boundary condition approach, Phys. Rev. Mater. 3, 033609 (2019).

[59] V. Vitek, R. C. Perrin, and D. K. Bowen, The core structure of $1/2\langle111\rangle$ screw dislocations in bcc crystals, Philos. Mag. 21, 1049 (1970).

[60] C. Woodward and S. I. Rao, Flexible Ab Initio Boundary Conditions: Simulating Isolated Dislocations in bcc Mo and Ta, Phys. Rev. Lett. 88, 216402 (2002).

[61] L. Ventelon and F. Willaime, Core structure and Peierls poten- tial of screw dislocations in $\alpha$-Fe from first principles: Cluster versus dipole approaches, J. Comput. Aided Mater. Des. 14, 85 (2007).

[62] H. Li, S. Wurster, C. Motz, L. Romaner, C. Ambrosch-Draxl, and R. Pippan, Dislocation-core symmetry and slip planes in tungsten alloys: Ab initio calculations and microcantilever bending experiments, Acta Mater. 60, 748 (2012).

[63] C. R. Weinberger, B. L. Boyce, and C. C. Battaile, Slip planes in bcc transition metals, Int. Mater. Rev. 58, 296 (2013).

[64] L. Dezerald, L. Ventelon, E. Clouet, C. Denoual, D. Rodney, and F. Willaime, Ab initio modeling of the two-dimensional energy landscape of screw dislocations in bcc transition metals, Phys. Rev. B 89, 024104 (2014).

[65] A. Ostapovets and A. Serra, Slip dislocation and twin nucleation mechanisms in hcp metals, J. Mater. Sci. 52, 533 (2017).

[66] A. Ostapovets and O. Vatazhuk, Peierls barriers of a-type edge and screw dislocations moving on basal and prismatic planes magnesium, Low Temp. Phys. 43, 421 (2017).

[67] Note that the extended dislocations in the variant 1 are unstable for geometrical reasons at very high pressure including ~400 GPa. Indeed, the dislocations recombine, leading to fcc stacking faults. However, the extended dislocations are stable for lower pressures, e.g., 40 GPa.

[68] D. Rodney, L. Ventelon, E. Clouet, L. Pizzagalli, and F. Willaime, Ab initio modeling of dislocation core properties in metals and semiconductors, Acta Mater. 124, 633 (2017).

[69] Note that for $s=0.9$ and 1.0 (variant 1 hcp), the energy points are taken from the variant 5 because, as a reminder, the dislocations in the variant 1 are unstable for geometrical reasons at ~400 GPa.

[70] A. Vattré and C. Denoual, Polymorphism of iron at high pressure: A 3D phase-field model for displacive transitions with finite elastoplastic deformations, J. Mech. Phys. Solids 92, 1 (2016).