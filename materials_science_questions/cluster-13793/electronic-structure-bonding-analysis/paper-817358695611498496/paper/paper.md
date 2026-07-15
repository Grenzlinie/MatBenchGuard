This is an author accepted manuscript at P. Mlkvik, C. Ederer, N. Spaldin, Phys. Rev. Research, 4, 043129 (2022).

# Influence of germanium substitution on the structural and electronic stability of the competing vanadium dioxide phases

Peter Mlkvik,* Claude Ederer, and Nicola A. Spaldin
Materials Theory, Department of Materials, ETH Zürich,
Wolfgang-Pauli-Strasse 27, 8093 Zürich, Switzerland
(Dated: February 3, 2023)

We present a density-functional theory (DFT) study of the structural, electronic, and chemical bonding behavior in germanium (Ge)-doped vanadium dioxide ($\text{VO}_2$). Our motivation is to explain the reported increase of the metal-insulator transition temperature under Ge doping and to understand how much of the fundamental physics and chemistry behind it can be captured at the conventional DFT level. We model doping using a supercell approach, with various concentrations and different spatial distributions of Ge atoms in $\text{VO}_2$. Our results suggest that the addition of Ge atoms strongly perturbs the high-symmetry metallic rutile phase and induces structural distortions that partially resemble the dimerization of the experimental insulating structure. Our work, therefore, hints at a possible explanation of the observed increase in transition temperature under Ge doping, motivating further studies into understanding the interplay of structural and electronic transitions in $\text{VO}_2$.

## I. INTRODUCTION

Vanadium dioxide ($\text{VO}_2$) is a prototypical example of a system undergoing a metal-insulator transition (MIT) coupled with a structural transition. This first-order transition from a high-temperature rutile (R) to a low-temperature monoclinic (M1) phase (Figs. 1 (a) and (b)) spans several orders of magnitude in resistivity [1], making $\text{VO}_2$ an interesting target for many potential uses [2–6]. Although the transition temperature of around $T_c = 340$ K is close to room temperature, its tuning has been a major focus of research [7, 8]. Its increase could lead to possibilities in the sector of electrical switches [7, 9–11], and its decrease could lead to applications in smart windows [12, 13]. In this study, we focus on understanding the behavior under doping with germanium (Ge), which has recently been reported to increase the transition temperature [14, 15]. Specifically, we perform calculations using density-functional theory (DFT) to determine the structural, electronic, and chemical effects that Ge doping has on $\text{VO}_2$ at the DFT level.

The MIT in $\text{VO}_2$ has been widely studied in the last decades with discussions mainly about whether structural or electronic effects provide the leading physical mechanism driving the transition [16–26]. Structurally, $\text{VO}_2$ undergoes a dimerization of V atoms along the crystal $c$ axis (Figs. 1, (a) and (b)), coupled with tilting of these dimers away from $c$ upon lowering the temperature through $T_c$. This mechanism has initially been attributed to Peierls physics leading in turn to a band-gap opening [27]. Thereby, the $a_{1g}$ orbital (also called $d_{\parallel}$, due to its lobe being oriented along the chain direction, see Ref. [1]), occupied with the single $d$ electron of the $\text{V}^{4+}$ cation, splits during the transition into a bonding-antibonding pair. However, the transition is unlikely to originate only from such structural effects, and calculations using conventional DFT indicate that purely structural deformations do not cause the formation of a gap [1]. Additionally, an insulating M2 phase containing both dimerized chains and non-dimerized tilted chains exists under certain conditions [28, 29], showing that a gap is allowed to form even when half of the V atoms are equally spaced [30]. Hence, the correlation effects among the localized $d$ electrons seem to also play an important role in the material, motivating numerous dynamical mean-field theory (DMFT) [23, 31–34] and $GW$-based studies [35, 36].

In this work, we study the behavior of $\text{VO}_2$ when some V atoms are replaced with Ge atoms. Although charged dopants in $\text{VO}_2$ have been experimentally [29, 37] and computationally [38] studied before, and seem to follow a trend of increased $T_c$ with increased valence of the dopant [8], the role of charge-neutral dopants such as Ge remains unclear, with few computational studies aiming at explaining the effects under doping using DFT [39–42]. Chen *et al.* [39] conducted a large-scale DFT study of the M1 structure of $\text{VO}_2$ doped with group IV elements including Ge, focusing on absorption and reflectivity, predicting a decrease in $T_c$ for all tested elements, at odds with experiments. Lu *et al.* [40] conducted a DFT study of $\text{VO}_2$ alloying with 25% $\text{GeO}_2$, comparing it with $\text{MgO}_2$ alloying. The authors observed that the heavily Ge-doped $\text{VO}_2$ collapses from the M1 phase to the R phase due to $\text{GeO}_2$ being rutile, and they focused on magnetic ordering in the material. The same authors [41] later considered lower Ge doping concentrations, focusing on the dependence of magnetic ordering and enthalpy changes on various density-functional methodologies. Using non-collinear supercell-based parametric magnetic calculations for the R phase combined with a Heisenberg dimer model, they found an increase in $T_c$ under Ge doping in agreement with experiments.

Here, we build on these earlier works to present a combined structural, electronic, and chemical picture of the

* peter.mlkvik@mat.ethz.ch

![](./images/817358695611498496_1.jpg)

FIG. 1. (a) Double unit cell of the R and (b) single unit cell of M1 VO₂ phases in their pristine condition. (c) R phase 2 × 2 × 3 supercell used for calculations with the stationary Ge atom (orange) corresponding to the Ge₀₀ coordinate of the labeling system indicated. V (O) atoms shown in blue (red).

effects a Ge dopant has on VO₂. We focus particularly on the effect of Ge doping on the structure of VO₂, as well as on the electronic behavior of V atoms both close to and far away from the dopants, considering multiple different configurations of the dopant atoms. In addition, we consider the chemical bonding behavior of the Ge-V and V-V atom pairs near the dopant. We evaluate the structural response of the two main VO₂ phases (R and M1) to Ge doping and discuss whether this response can help explain experimental observations. The second key goal of our work is to assess to what extent the standard DFT methodology employed here and elsewhere [1] is sufficient to model this behavior.

We expect the effects of Ge dopant atoms to come from two main sources. Firstly, Ge and V have different atomic radii and oxygen octahedra sizes, so substituting V with Ge will lead to structural changes from steric effects. Secondly, Ge and V have different numbers of valence electrons, so the bonding behavior of a Ge atom could be significantly different from that of a V atom. We hence look at the structural, electronic, and chemical bonding in the doped systems.

## II. METHODS

### A. Construction of the unit cells

Structural relaxations are performed for both the low-temperature M1 phase and the high-temperature R phases with monoclinic and tetragonal primitive unit cells respectively. In their primitive cells (Figs. 1 (a) and (b)), the R structure contains two VO₂ formula units, with the shortest distance between neighboring V atoms along the c axis (a doubled unit cell of R is shown in Fig. 1 (a) for easier comparison with the M1 phase in Fig. 1 (b)). The M1 structure contains four VO₂ formula units and is formed by doubling the R cell along its c axis (and a monoclinic shear leading to a redefined b axis). In the current work, we align the M1 c axis parallel to the one of the R structure. For doped calculations, we consider two supercells; 2 × 2 × 2 and 2 × 2 × 3 relative to the M1 unit cell (the latter tripled in the chain direction, Fig. 1 (c)), containing 32 and 48 formula units respectively.

The typical doping range for Ge-doped VO₂ is between 2% and 6% [14, 43], hence we consider either one or two Ge atoms per supercell. For doping with a single Ge atom, only one inequivalent site exists in both the 2 × 2 × 2 and 2 × 2 × 3 supercells, corresponding to a dopant concentration of 3.125% and 2.08%, respectively. For the 2×2×3 case we also consider doping with two Ge atoms, corresponding to a dopant level of 4.17%. In this case, there are many distinct sets of possible positions of the two Ge dopants in the R and M1 structures.

In order to capture the disorder present in doped VO₂, we probe different possible configurations of the two Ge atoms in the 2×2×3 supercell. Thereby, the Ge positions are labeled according to their projections along the $\vec{a}$ lattice vector, as shown in Fig. 1 (c), as ${\rm Ge}_{ij}$. The labeling system follows the axes of the supercell, i.e. the M1 lattice vectors $\vec{b}$ and $\vec{c}$. The first index $i$, labels successive chains, with $i$ increasing along the positive $\vec{b}$ lattice vector, and the second index $j$ labels the positions along the chains, increasing along the positive $\vec{c}$ lattice vector. All investigated configurations have the first Ge atom located at the origin of the labeling system (i.e. Ge₀₀, orange circle in Fig. 1(c)) and are labeled according to the position of the second Ge atom. Thus, a configuration is labeled as ${\rm Ge}_{0j}$ if the second Ge atom is located within the same chain, as ${\rm Ge}_{1j}$ if it is located in a nearest-neighboring chain, and as ${\rm Ge}_{2j}$ if it is in a second nearest-neighboring chain (with $j = -2$, ... 3). Since we only consider configurations including Ge atoms in one first nearest-neighbor chain and one second nearest-neighbor chain, we do not need to report the position along $\vec{a}$. Note that the second nearest-neighbor chains are at zero $\vec{a}$, while the nearest-neighbor chains are halfway along the unit cell in the $\vec{a}$ direction. For the R structure, considering up to the second nearest-neighbor chain, this combination yields 10 possible configurations all of which we calculate. For

the M1 structure, there are 53 possible configurations, but due to computational considerations, we only treat a representative sample of 17 of these, in particular, one set of those of the R structure, adding the configurations along the chains, $Ge_{i-1}$, $Ge_{i-2}$, and $Ge_{i-3}$.

## B. Computational Details

We perform calculations using DFT with plane-wave basis sets as implemented in the QUANTUM ESPRESSO code (QE v6.4.1) [44, 45]. Calculations are performed within the generalized gradient approximation (GGA) using the Perdew-Burke-Ernzerhof (PBE) [46] exchange- correlation functional. Note that since our goal is to cap- ture the effects of the doping chemistry, and we do not aim to reproduce the MIT or Mott physics, we perform non-spin polarized calculations, without a DMFT or $GW$ treatment and also without a DFT+$U$ correction [47]. Using our setup, the lattice and cell sizes, together with the qualitative behavior of the density of states (DOS) of the two phases, are captured correctly at a computa- tional cost that is suitable for supercell calculations. Note that, as in previous standard DFT calculations [19], we do not obtain a band gap for the insulating M1 phase, and the two $VO_2$ phases have the incorrect relative ener- gies [48] (each having its own stable minimum), but since we treat each phase separately, these features do not pose problems for our analysis.

We use scalar-relativistic ultrasoft pseudopotentials for O, V, and Ge atoms taken from the SSSP library [49, 50], with $3s$ and $3p$ semi core states included as valence in V atoms, and $3d$ states included as valence for Ge atoms. Calculations are conducted with a wavefunction plane- wave kinetic energy cut-off of 40 Ry ($\sim$544 eV) increasedby a factor of 8 for the charge density and a $4 \times 4 \times 4$  $\Gamma$-centered $k$-point grid for all calculations. We converge the total energies to $10^{-6}$ eV and in structural relax ations we converge all force components to $10^{-3}$ eV/Å. During structural relaxation, both the internal positions of the atoms and the lattice vectors are relaxed. We ob- serve only very small ($\sim$0.01%) lattice parameter changes relative to the pristine structures.

We perform a band unfolding procedure to obtain a primitive cell band structure from the supercell folded band structure. We follow the procedure outlined in Ref. [51] (and previously in Refs. [52, 53]), implementedin the BANDUP code [54, 55] through the BANDUPPY [56] PYTHON interface. To determine the chemical bonding behavior from the obtained DFT results, the crystal or- bital hamiltonian population (COHP) analysis [57] is per- formed using the LOBSTER package [58-60].

## III. RESULTS AND DISCUSSION

### A. $VO_2$ cells containing an isolated Ge atom

#### 1. Electronics

We first perform self-consistent calculations for the $2 \times 2 \times 2$ unit cell with a single Ge atom and structural parameters fixed to those obtained for pristine M1 $VO_2$. This allows us to analyze the changes in the electronic structure that are solely due to the different chemistry of the Ge atom, without the potential structural changes.

The corresponding Ge DOS and unfolded band struc- ture are compared to those of the undoped structure in Fig. 2. The latter agrees well with previous DFT stud- ies [1, 19, 61, 62]. The O $2s$ bands are located at around -20 eV and the O $2p$-dominated bands (with some con- tribution of V $d$ states due to hybridization) lie between -8 and -1.5 eV. The Fermi level cuts through the bot- tom of the V $3d$-dominated bands (also containing some O $2p$ character due to hybridization). Due to the octa- hedral coordination of the V cations, the V $3d$ band is separated into lower-lying $t_{2g}$-like (from -0.5 to around2.5 eV) and higher-lying $e_g$-like (from around 2.5 to 5 eV) states.

From the projected DOS shown in the left-most panel of Fig. 2, one can see that the Ge states in the doped structure are mostly located far away from the Fermi level. In particular, the completely filled Ge $3d$ shell lies at around -26 eV. The Ge $4s$ peak at -10 eV corre- sponds to a strong hybridization with an O $2p$ band (not shown), introducing no carriers to the system, i.e., the Ge atom remains formally $Ge^{4+}$.

Thanks to the unfolding procedure, we can directly see the effect of the addition of a Ge atom on the band struc- ture (Fig. 2, center and right panels). Here, the larger the spread of a given energy eigenvalue is, the more its value varies across the different unit cells of the supercell, and hence the more it has been altered by the added Ge compared to pristine $VO_2$. The effects of Ge doping are shown through the color map smearing, with a brighter yellow color corresponding to a greater weight coming from the unfolding procedure. Most of the band energies remain in the same position as in pristine $VO_2$, with only minor shifts and smearing. There is also no noticeable change in the filling of the V $d$ states. We note that the same behavior persists even after full structural re- laxation, after which the unfolded bands become more diffuse due to the variable positions of atoms in the su- percell. We hence see that the substitution of V by Ge has very little effect on the electronic states of the system.

#### 2. Chemical bonding

Next, we examine the bonding behavior of the dopant in the supercell by calculating its COHP for the fully

![](./images/817358695611498496_2.jpg)

FIG. 2. Band structure of the Ge-doped M1 phase with the corresponding local DOS of the Ge dopant. In white, the pristine band structure is overlaid over the unfolded Ge-doped band structure, shown through a color map. The certainty of the unfolded energy eigenvalues corresponds to the color intensity. The Fermi level (dashed white line) is set to the zero of energy. Left panel: The Ge DOS shows $s$ (red), $p$ (green), and $d$ (blue) orbitals. Center panel: Band structure of the Ge-doped M1 phase. Right panel: Detail of the band structure around the Fermi level showing the pristine bands and the unfolding dispersion due to Ge states.

optimized structures (Fig. 3). The COHP of the un- doped M1 phase displays a strong bonding-antibonding feature related to the $a_{1g}$ orbital (Fig. 3, blue), due to the dimerization of two V atoms. Such a strong feature is missing in the R phase, where the bonding behavior is much weaker (Fig. 3, red line ). We also show COHPs for the Ge-doped M1 system in Fig. 3 (the R system behaves similarly although the relative changes are less strong). We see that the Ge-V bonding is significantly weaker than the previous V-V bonding. This is true for both the formerly dimerized nearest neighbor (NN), and also the nearest neighbor along the chain in the opposite di- rection (NN'), corresponding to a different dimer (dashed and solid green lines in Fig. 3). Both atoms bond weakly with the Ge atom, consistent with the absence of Ge-V dimerization and confirming the electronic inertness of the Ge dopant as seen through the band structure.

### 3. Structure

Finally, we investigate the effect of substituting a single Ge atom into the $2 \times 2 \times 2$ VO$_2$ supercell on the structure of the two phases. After a structural relaxation following the introduction of the dopant Ge atom, we qualitatively observe very little difference between the doped and un- doped M1 phases. The R phase, however, undergoes a significant distortion from its original high symmetry; see Fig. 4 for details of the structurally relaxed supercell.

![](./images/817358695611498496_3.jpg)

FIG. 3. V-V and Ge-V COHPs in the R and M1 structures. The blue (red) line shows the undoped M1 (R) V-V bond behavior. Both peak near the Fermi level (black dashed line), with predominantly bonding (positive) character below it and antibonding (negative) character above it. This behavior is strongly enhanced in the M1 phase. In green, the Ge-V COHP in the Ge-doped M1 $2 \times 2 \times 2$ supercell is shown for both the formerly dimerized nearest neighbor (solid line), and the nearest neighbor along the chain in the opposite direction (dashed line); both COHPs show similar weak bonding.

The addition of a Ge atom has strong structural effects, with the V atoms next to the Ge dopant displaced away from it along the chain direction (Fig. 4 (a)). The GeO$_6$

polyhedron distorts the lattice and causes buckling of the neighboring chains (Fig. 4 (b)). Compared to the $VO_6$ polyhedron, the equatorial oxygens in $GeO_6$ are closer to the dopant, although the apical oxygens' Ge-O distances are unchanged, and the Ge remains at the center for the octahedron (Fig. 4 (c)).

The resulting structure forms zig-zagged chains (note the ellipses in Fig. 4 (b)), not unlike the pristine M1 phase, with some V atoms relaxing into positions closer to each other than before. The structural dimers that form, indicated as bonds for V-V distances less than 2.7 Å in Fig. 4, with the smallest distances reaching 2.6 Å, are similar to those found in the M1 phase. For a more quantitative discussion using histograms of nearest-neighbor distances, also featuring typical R and M1 V-V distances, see Fig. 6. We, however, also note that due to the periodicity effects coming from the construction of the $2 \times 2 \times 2$ supercell, the distortions along the chain with the added Ge atom also lead to the formation of "trimers" (as seen in Fig. 4 (a)) throughout the cell, since there are exactly three V atoms between subsequent Ge atoms.

### B. $VO_2$ cells containing multiple Ge atoms

Due to the potential constraints related to the limited size of the periodic $2 \times 2 \times 2$ supercell, resulting in the formation of the "structural trimers" seen in Fig. 4(a), we now consider a larger $2 \times 2 \times 3$ supercell with two Ge atoms. This treatment allows us to vary the relative positions of the dopant atoms and to check for spurious effects due to the periodic boundary conditions, especially along the $Ge_{0j}$ chain. In particular, with two Ge atoms, we are able to study multiple configurations with both even and odd numbers of V atoms between subsequent Ge atoms.

#### 1. Energetics

We first consider the energetics of the different configurations of the two Ge atoms in the M1 phase after the structural relaxation (Fig. 5, left panel, overlaid on top of the unit cell structure). We begin by comparing the different relative energies of the relaxed structures. The lowest energy ($E_0$) occurs when the Ge atoms cluster, with a V-V dimer replaced by two Ge atoms ($Ge_{0-1}$). The second-lowest energy configurations have the second Ge atom in the nearest-neighbor chain ($Ge_{10}$, $Ge_{1-1}$), and are within 0.1 eV of $E_0$. In addition, the $Ge_{03}$ position, allowing even numbers of V atoms in between Ge dopants, is lower in energy than its neighboring configurations with 0.29 eV above $E_0$ compared to 0.40 eV for the surrounding positions within the chain. In this case, although dimerization is disfavored due to surrounding dimers and the zig-zag distortion orientation, the previously non-dimerized V atoms between the Ge atoms are also pushed closer together. The remaining Ge positions have similar energies at around 0.4 eV above $E_0$ (note the similar colors in Fig. 5, left panel).

![](./images/817358695611498496_4.jpg)

FIG. 4. Details of the single-Ge-doped structurally relaxed $2 \times$ $2 \times 2$ R $VO_2$ supercell. (a) View along the $\vec{a}$ lattice parameter direction. V-V bonds are indicated for V-V distances less than 2.7 Å. (b) View along the $\vec{c}$ direction. Buckled chains described in the text are highlighted with dashed ellipses. V, O, and Ge atoms shown in blue, red, and orange, respectively. Ge-O bonds are indicated for Ge-O distance less than 2.0 Å. (c) View along the $\vec{c}$ direction, now with oxygen polyhedra shown. Ge (V) centered polyhedra are shown in orange (blue).

Considering the R phase (Fig. 5, right panel), the calculated energies for the various Ge positions also show that clustering of Ge atoms in the nearest-neighbor chain (especially at $Ge_{11}$, and $Ge_{10}$ — both the $E_0$ configurations) is the most favorable. However, in the R phase,

![](./images/817358695611498496_5.jpg)

FIG. 5. Energies of supercells of the M1 (left panel) and R (right panel) VO₂ phases when doped at the indicated symmetry inequivalent positions, as viewed down the $\vec{a}$ axis. Black hexagons correspond to the positions of one of the Ge atoms in the supercell. Color mapping indicates the total energy of the relaxed supercell with the second Ge atom placed at the indicated position, relative to the lowest energy ($E_0$) M1 (left panel) and R (right panel) configurations.

the tendency for Ge atoms to disfavor an odd number of V atoms between Ge atoms in a chain is surprisingly more strongly pronounced than in the M1 phase. Leaving an unpaired lone V atom in between two Ge atoms leads to a high energy configuration even though there was originally no dimerization present in the R phase — the Ge₀₃ corresponds to almost the same low energy as Ge₁₁, whereas Ge₀₂ is a highly unfavorable position for the Ge atom, 0.63 eV higher than $E_0$ (note the bright yellow color in Fig. 5, right panel). This trend is consistent with the results for the M1 phase, where, again, the Ge atoms allow V atoms to dimerize only if an even number of them are present in a given chain between two Ge dopants. The trends in the other chains are not as prominent, but all low-energy configurations can be seen to support some form of zig-zag formation in the structurally relaxed cell as in the single-Ge-substituted case.

## 2. Structure

To quantify how Ge substitution distorts the structure, we consider the distances and angles between nearest neighbor V atoms along the $c$ direction. Figure 6 shows histograms of the distances and Fig. 7 shows histograms of the angles (relative to the $c$ axis) of the nearest V-V pairs for all considered configurations of the Ge atoms in the doped cases, together with the corresponding values in pristine VO₂. In the unperturbed M1 structure, two nearest V-V distances are present, at 2.5 Å and 3.15 Å, forming an angle of $7.65^\circ$ with the $c$ direction indicating the perfectly dimerized structure. The unperturbed R phase has a single peak at a distance of 2.76 Å, and a single peak at $0^\circ$ of the angle, corresponding to the equidistant V atoms along the $c$ direction.

Ge doping does not strongly affect the structure of the M1 phase for any of the considered configurations of the Ge atoms. From the histograms of nearest-atoms distances (Fig. 6, blue bars) in the Ge-doped supercell, we find only minimal perturbation from the undoped VO₂ M1 phase for all configurations. The nearest atom distances retain a double-peaked distribution, corresponding to the typical short and long DFT dimerization distances, respectively, indicating that dominant dimerization is still present in the structure. Broadening around the equilibrium distances is present but only rarely do some distances become similar to those in the R phase. The same behavior is observed when nearest-neighbor angles are considered (Fig. 7, blue bars). Under doping, the angle of the pristine crystal structure is essentially retained with the value of the angle becoming broadened.

In contrast to the M1 phase, in the R phase, Ge doping causes a severe structural distortion. The previously single-valued nearest-atom distance in the pristine R VO₂ crystal either splits into a two peaked distribution (e.g. Ge₀₂), or demonstrably widens for all the different configurations of two Ge atoms, essentially spanning the whole range of distances between the dimerized and non-dimerized distances of the M1 structure (Fig. 6, red bars). There are large shifts of atomic positions from those of the undoped structure, with atoms in all chains including those far from the impurity atoms, affected by the introduction of Ge dopants. This shift is observed also in the nearest-neighbor angles (Fig. 7, red bars). The angles between nearest neighbors become non-zero and show a wide distribution of angles for all configurations considered, even reaching values of up to $7^\circ$, i.e., similar to that in the pristine M1 phase. This leads to the same effects seen above in the $2 \times 2 \times 2$ supercell with one Ge atom (see Fig. 4 (b)), where we observed buckling of the V-V chains and their consequent structural dimerization. Due to the presence of two Ge atoms, in some configurations (e.g. Ge₀₃) this buckling closely resembles that of the M1 phase, with dimerization effects and a shift in the angle of the respective dimers away from zero.

## 3. Electronics and chemical bonding

Accompanying the structural distortions described above, the Ge-doped supercells also undergo electronic changes. The key change occurs in the $a_{1g}$ orbital projected density of states (PDOS), presented in Fig. 8.

In the M1 phase, we observe that the local DOS of the V atoms that remain dimerized is almost unchanged on Ge doping, as shown in the $a_{1g}$ PDOS for the Ge₀₃ config-

![](./images/817358695611498496_6.jpg)

FIG. 6. Nearest neighbor V-V distances for the various configurations upon doping in both R (red bars) and M1 (blue bars) phases. The original undoped nearest neighbor V-V distances are shown in dark colors, and the distances in the indicated structure after doping and relaxation are shown in lighter colors. The M1 distances only broaden, while the R phase distorts strongly.

![](./images/817358695611498496_7.jpg)

FIG. 7. Nearest neighbor V-V angles for the various configurations upon doping in both R (red) and M1 (blue) phases. The original undoped nearest neighbor V-V angles are shown in dark colors, and the angles in the indicated structure after doping and relaxation are shown in lighter colors. Both the M1 and R angle distributions shift towards each other.

uration (Fig. 8, top panel). The average PDOS in doped systems still exhibits the typical bonding-antibonding feature of pristine M1 $VO_2$, as previously discussed in the context of the COHP (Fig. 3), and shown in Fig. 8 as the thick blue line. The NN' (as defined in Sec. III A 2) PDOS also keeps the shape of the undoped material with only minor deviations (note that we consider the nearest neighbor in the other direction in the chain, because the nearest-neighbor PDOS displays a rotated local coordinate system). This result is consistent with the observations of the structural distortions.

In contrast, in the rutile phase, the electronic structure changes significantly compared with the undoped case (Fig. 8, bottom panel, thick red line) on Ge incorporation. Both of the V nearest neighbors to the Ge dopant become electronically extremely similar to V atoms in the M1 structure, displaying a double-peaked bonding-antibonding PDOS for the $Ge_{03}$ configuration (see solid line in Fig. 8). Additionally, large changes also occur throughout the bulk of the supercell, and also the average $a_{1g}$ PDOS changes significantly from that of the undoped R phase (dashed line in Fig. 8). The overall average PDOS broadens, and its value at $E_F$ is reduced.

![](./images/817358695611498496_8.jpg)

FIG. 8. The PDOS onto the $a_{1g}$ orbital in the M1 (top panel) and R (bottom panel) Ge-doped supercells for the $Ge_{03}$ configuration. The shaded thick blue (red) lines respresent the pristine M1 (R) phases are shown. The solid line corresponds to the nearest neighbor to the Ge dopant atom, and the dashed line shows the average of all V atoms. The black dashed line corresponds to the Fermi level, set to 0 eV. The R phase PDOS is severely perturbed from the original state, while the M1 phase shows no significant distortion.

## IV. SUMMARY AND OUTLOOK

In this work, we present a DFT study of the structural and electronic properties of Ge-doped $VO_2$ in its M1 and R structures.

We show that the electronic states of Ge atoms are not present near the Fermi level for the doped $VO_2$ phases considered. We further show that the Ge-V bonding is weak in both cases. Energetically, we observe that in both phases, the lowest energy arrangements of two Ge atoms correspond to their clustering close to each other. In both phases, the lowest energy arrangements correspond to configurations that lead only to small disruptions of the V-V pairs (since, except for $Ge_{0-1}$, all configurations do of course disrupt the V-V pairs to some extent).

However, we observe drastically different structural relaxations for the R and M1 phases. We find that the M1 phase is largely unperturbed both structurally and electronically by Ge doping. In contrast, the addition of Ge dopants to the R phase seems to push the structure towards the M1 dimerized phase. The structural distortion caused by the Ge atoms promotes structural dimer formation of the V atoms, as the buckling of the chains causes a tilt and alters the V-V distances and angles of these dimerized distances. Coupled with this are electronic changes in the R phase, in which the dimers cause an enhanced bonding-antibonding splitting in the DOS.

We conclude that the R phase is more prone to structural perturbations caused by the Ge atoms than the M1 phase, hinting at an intrinsic instability of this phase. Our results also suggest that it is the strength of the dimers that allows the robustness of the M1 phase with respect to Ge incorporation. We further note that the large structural perturbations induced in the R phase on Ge doping give it a tendency towards insulating behavior, reducing the DOS at the Fermi level, again in the direction of the M1 phase. The strong distortions in the $VO_2$ rutile phase are remarkable, given that the ground state structure of $GeO_2$ is also the rutile structure. The behavior is reminiscent of the case of $Ti_4O_7$ [63, 64], in which the $TiO_2$ rutile layers, which are interleaved with layers containing $d^1$ $Ti^{3+}$ ions, are strongly distorted.

Therefore, our results hint toward a possible explanation of the recent experimental observation of $T_c$ increase under Ge doping. First, under doping we observe the R phase to be more structurally perturbed than M1, with the doping resulting in structural distortions that resemble those present in the pristine M1 phase. Second, we observe that the M1 phase is largely robust towards Ge incorporation, which only leads to minor structural distortions. This indicates that the low-temperature M1 phase is favored by Ge doping leading in turn to an increase in the transition temperature. However, to more persuasively arrive at these conclusions and to verify the hints presented here, further research with more advanced methods is required.

## ACKNOWLEDGMENTS

We are thankful to Adrian Ionescu and Daesung Park for useful discussions and comments. Calculations were performed on the ETH Zürich Euler cluster. This work was supported by ETH Zürich. All input files available in Ref. [65].

[1] V. Eyert, The Metal-Insulator Transitions of $VO_2$: A Band Theoretical Approach, Ann. Phys. 11, 650 (2002).

[2] Z. Yang, C. Ko, and S. Ramanathan, Oxide Electronics Utilizing Ultrafast Metal-Insulator Transitions, Annu.

Rev. Mater. Res. 41, 337 (2011).

[3] Y. Ke, S. Wang, G. Liu, M. Li, T. J. White, and Y. Long, Vanadium Dioxide: The Multistimuli Responsive Mate- rial and Its Applications, Small 14, 1802025 (2018).

[4] K. Liu, S. Lee, S. Yang, O. Delaire, and J. Wu, Re- cent Progresses on Physics and Applications of Vanadium Dioxide, Mater. Today 21, 875 (2018).

[5] J. L. Andrews, D. A. Santos, M. Meyyappan, R. S. Williams, and S. Banerjee, Building Brain-Inspired Logic Circuits from Dynamically Switchable Transition-Metal Oxides, Trends in Chemistry 1, 711 (2019).

[6] E. Corti, J. A. Cornejo Jimenez, K. M. Niang, J. Robert- son, K. E. Moselund, B. Gotsmann, A. M. Ionescu, and S. Karg, Coupled VO₂ Oscillators Circuit as Analog First Layer Filter in Convolutional Neural Networks, Front. Neurosci. 15, 628254 (2021).

[7] Z. Shao, X. Cao, H. Luo, and P. Jin, Recent Progress in the Phase-Transition Mechanism and Modulation of Vanadium Dioxide Materials, NPG Asia Mater. 10, 581 (2018).

[8] R. Shi, N. Shen, J. Wang, W. Wang, A. Amini, N. Wang, and C. Cheng, Recent Advances in Fabrication Strate- gies, Phase Transition Modulation, and Advanced Appli- cations of Vanadium Dioxide, Appl. Phys. Rev. 6, 011312 (2019).

[9] M. Rini, Z. Hao, R. W. Schoenlein, C. Giannetti, F. Parmigiani, S. Fourmaux, J. C. Kieffer, A. Fujimori, M. Onoda, S. Wall, and A. Cavalleri, Optical Switch- ing in VO₂ Films by Below-Gap Excitation, Appl. Phys. Lett. 92, 181904 (2008).

[10] W. A. Vitale, L. Petit, C. F. Moldovan, M. Fernández- Bolaños, A. Paone, A. Schüler, and A. M. Ionescu, Elec- trothermal Actuation of Vanadium Dioxide for Tunable Capacitors and Microwave Filters with Integrated Micro- heaters, Sens. Actuator A Phys. 241, 245 (2016).

[11] T. Rosca, F. Qaderi, M. Riccardi, O. J. Martin, and A. M. Ionescu, An Experimental Study of the Photoresponse of 1T-1R Oscillators Based on Vanadium Dioxide: Towards Spiking Sensing Systems, in 2021 21st International Con- ference on Solid-State Sensors, Actuators and Microsys- tems (Transducers) (2021) pp. 373-376.

[12] S. Wang, M. Liu, L. Kong, Y. Long, X. Jiang, and A. Yu, Recent Progress in VO₂ Smart Coatings: Strategies to Improve the Thermochromic Properties, Prog. Mater. Sci. 81, 1 (2016).

[13] Y. Cui, Y. Ke, C. Liu, Z. Chen, N. Wang, L. Zhang, Y. Zhou, S. Wang, Y. Gao, and Y. Long, Thermochromic VO₂ for Energy-Efficient Smart Windows, Joule 2, 1707 (2018).

[14] A. Krammer, A. Magrez, W. A. Vitale, P. Mocny, P. Jeanneret, E. Guibert, H. J. Whitlow, A. M. Ionescu, and A. Schüler, Elevated Transition Temperature in Ge Doped VO₂ Thin Films, J. Appl. Phys. 122, 045304 (2017).

[15] A. Muller, R. A. Khadar, T. Abel, N. Negm, T. Rosca, A. Krammer, M. Cavalieri, A. Schueler, F. Qaderi, J. Bolten, M. Lemme, I. Stolichnov, and A. M. Ionescu, Radio-Frequency Characteristics of Ge-Doped Vanadium Dioxide Thin Films with Increased Transition Tempera- ture, ACS Appl. Electron. Mater. 2, 1263 (2020).

[16] A. Zylbersztejn and N. F. Mott, Metal-Insulator Transi- tion in Vanadium Dioxide, Phys. Rev. B 11, 4383 (1975).

[17] R. M. Wentzcovitch, W. W. Schulz, and P. B. Allen, VO₂: Peierls or Mott-Hubbard? A View from Band Theory, Phys. Rev. Lett. 72, 3389 (1994).

[18] S. Biermann, A. Poteryaev, A. I. Lichtenstein, and A. Georges, Dynamical Singlets and Correlation-Assisted Peierls Transition in VO₂, Phys. Rev. Lett. 94, 026404 (2005).

[19] V. Eyert, VO₂: A Novel View from Band Theory, Phys. Rev. Lett. 107, 016401 (2011).

[20] C. Weber, D. D. O'Regan, N. D. M. Hine, M. C. Payne, G. Kotliar, and P. B. Littlewood, Vanadium Dioxide: A Peierls-Mott Insulator Stable against Disorder, Phys. Rev. Lett. 108, 256402 (2012).

[21] R. Grau-Crespo, H. Wang, and U. Schwingenschlögl, Why the Heyd-Scuseria-Ernzerhof Hybrid Functional De- scription of VO₂ Phases Is Not Correct, Phys. Rev. B 86, 081101(R) (2012).

[22] S. Kim, K. Kim, C.-J. Kang, and B. I. Min, Correlation- Assisted Phonon Softening and the Orbital-Selective Peierls Transition in VO₂, Phys. Rev. B 87, 195106 (2013).

[23] W. H. Brito, M. C. O. Aguiar, K. Haule, and G. Kotliar, Metal-Insulator Transition in VO₂: A DFT + DMFT Perspective, Phys. Rev. Lett. 117, 056402 (2016).

[24] O. Nájera, M. Civelli, V. Dobrosavljević, and M. J. Rozenberg, Resolving the VO₂ Controversy: Mott Mechanism Dominates the Insulator-to-Metal Transition, Phys. Rev. B 95, 035113 (2017).

[25] F. Grandi, A. Amaricci, and M. Fabrizio, Unraveling the Mott-Peierls Intrigue in Vanadium Dioxide, Phys. Rev. Res. 2, 013298 (2020).

[26] J.-P. Pouget, Basic Aspects of the Metal-Insulator Tran- sition in Vanadium Dioxide VO₂: A Critical Review, Comptes Rendus Phys. 22, 37 (2021).

[27] J. B. Goodenough, The Two Components of the Crystal- lographic Transition in VO₂, J. Solid State Chem. 3, 490 (1971).

[28] N. F. Quackenbush, H. Paik, M. J. Wahila, S. Sallis, M. E. Holtz, X. Huang, A. Ganose, B. J. Morgan, D. O. Scanlon, Y. Gu, F. Xue, L.-Q. Chen, G. E. Sterbinsky, C. Schlueter, T.-L. Lee, J. C. Woicik, J.-H. Guo, J. D. Brock, D. A. Muller, D. A. Arena, D. G. Schlom, and L. F. J. Piper, Stability of the M2 Phase of Vanadium Dioxide Induced by Coherent Epitaxial Strain, Phys. Rev. B 94, 085105 (2016).

[29] M. A. Davenport, M. J. Krogstad, L. M. Whitt, C. Hu, T. C. Douglas, N. Ni, S. Rosenkranz, R. Osborn, and J. M. Allred, Fragile 3D Order in V₁₋ₓMoₓO₂, Phys. Rev. Lett. 127, 125501 (2021).

[30] J. P. Pouget, H. Launois, T. M. Rice, P. Dernier, A. Gos- sard, G. Villeneuve, and P. Hagenmuller, Dimerization of a Linear Heisenberg Chain in the Insulating Phases of V₁₋ₓCrₓO₂, Phys. Rev. B 10, 1801 (1974).

[31] J. M. Tomczak and S. Biermann, Effective Band Struc- ture of Correlated Materials: The Case of VO₂, J. Phys.: Condens. Matter 19, 365206 (2007).

[32] J. M. Tomczak, F. Aryasetiawan, and S. Biermann, Effec- tive Bandstructure in the Insulating Phase versus Strong Dynamical Correlations in Metallic VO₂, Phys. Rev. B 78, 115103 (2008).

[33] A. S. Belozerov, M. A. Korotin, V. I. Anisimov, and A. I. Poteryaev, Monoclinic M1 phase of VO₂: Mott-Hubbard versus band insulator, Phys. Rev. B 85, 045109 (2012).

[34] W. H. Brito, M. C. O. Aguiar, K. Haule, and G. Kotliar, Dynamic Electronic Correlation Effects in NbO₂ as Com- pared to VO₂, Phys. Rev. B 96, 195102 (2017).

[35] M. Gatti, F. Bruneval, V. Olevano, and L. Reining, Un-derstanding Correlations in Vanadium Dioxide from First Principles, Phys. Rev. Lett. 99, 266402 (2007).

[36] C. Weber, S. Acharya, B. Cunningham, M. Grüning, L. Zhang, H. Zhao, Y. Tan, Y. Zhang, C. Zhang, K. Liu, M. Van Schilfgaarde, and M. Shalaby, Role of the Lat-tice in the Light-Induced Insulator-to-Metal Transition in Vanadium Dioxide, Phys. Rev. Res. 2, 023076 (2020).

[37] H. Asayesh-Ardakani, A. Nie, P. M. Marley, Y. Zhu, P. J. Phillips, S. Singh, F. Mashayek, G. Sambandamurthy, K.-b. Low, R. F. Klie, S. Banerjee, G. M. Odegard, and R. Shahbazian-Yassar, Atomic Origins of Monoclinic-Tetragonal (Rutile) Phase Transition in Doped $VO_2$ Nanowires, Nano Lett. 15, 7179 (2015).

[38] B. Stahl and T. Bredow, Surfaces of $VO_2$ - Poly-morphs: Structure, Stability and the Effect of Doping, ChemPhysChem 22, 1018 (2021).

[39] L. Chen, X. Wang, D. Wan, Y. Cui, B. Liu, S. Shi, H. Luo, and Y. Gao, Energetics, Electronic and Optical Properties of X (X = Si, Ge, Sn, Pb) Doped $VO_2$(M) from First-Principles Calculations, J. Alloys Compd. 693, 211 (2017).

[40] H. Lu, Y. Guo, and J. Robertson, Electronic Structure of Metallic and Insulating Phases of Vanadium Dioxide and Its Oxide Alloys, Phys. Rev. Mater. 3, 094603 (2019).

[41] H. Lu, S. Clark, Y. Guo, and J. Robertson, Modelling the Enthalpy Change and Transition Temperature De-pendence of the Metal-Insulator Transition in Pure and Doped Vanadium Dioxide, Phys. Chem. Chem. Phys. 22, 13474 (2020).

[42] H. Lu, S. Clark, Y. Guo, and J. Robertson, The Metal-Insulator Phase Change in Vanadium Dioxide and Its Applications, J. Appl. Phys. 129, 240902 (2021).

[43] A. A. Muller, R. Khadar, K. M. Niang, G. Bai, E. Ma-tioli, J. Robertson, and A. M. Ionescu, Radio Fre-quency Temperature Transducers Based on Insulator-Metal Phase Transition in $VO_2$ and Ge-Doped $VO_2$ ALD Thin Films, in 2021 21st International Conference on Solid-State Sensors, Actuators and Microsystems (Trans-ducers) (IEEE, Orlando, FL, USA, 2021) pp. 1355–1358.

[44] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococ-cioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, QUANTUM ESPRESSO: A Modular and Open-Source Software Project for Quantum Simulations of Materials, J. Phys. Condens. Matter 21, 395502 (19pp)(2009).

[45] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. Buongiorno Nardelli, M. Calandra, R. Car, C. Cavaz-zoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carn-imeo, A. Dal Corso, S. de Gironcoli, P. Delugas, R. A. DiStasio, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli, M. Lazzeri, N. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A. Otero-de-la-Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N. Vast, X. Wu, and S. Baroni, Advanced Capabilities for Materials Modelling with Quantum ESPRESSO, J. Phys.: Condens. Matter 29, 465901 (2017).

[46] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996).

[47] B. Stahl and T. Bredow, Critical Assessment of the DFT + U Approach for the Prediction of Vanadium Dioxide Properties, J. Comput. Chem. 41, 258 (2020).

[48] T. A. Mellan, H. Wang, U. Schwingenschlögl, and R. Grau-Crespo, Origin of the Transition Entropy in Vanadium Dioxide, Phys. Rev. B 99, 064113 (2019).

[49] K. Lejaeghere, G. Bihlmayer, T. Björkman, P. Blaha, S. Blügel, V. Blum, D. Caliste, I. E. Castelli, S. J. Clark, A. Dal Corso, S. de Gironcoli, T. Deutsch, J. K. Dewhurst, I. Di Marco, C. Draxl, M. Dułak, O. Eriksson, J. A. Flores-Livas, K. F. Garrity, L. Gen-ovese, P. Giannozzi, M. Giantomassi, S. Goedecker, X. Gonze, O. Grånäs, E. K. U. Gross, A. Gulans, F. Gygi, D. R. Hamann, P. J. Hasnip, N. A. W. Holzwarth, D. Iușan, D. B. Jochym, F. Jollet, D. Jones, G. Kresse, K. Koepernik, E. Küçükbenli, Y. O. Kvashnin, I. L. M. Locht, S. Lubeck, M. Marsman, N. Marzari, U. Nitzsche, L. Nordström, T. Ozaki, L. Paulatto, C. J. Pickard, W. Poelmans, M. I. J. Probert, K. Refson, M. Richter, G.-M. Rignanese, S. Saha, M. Scheffler, M. Schlipf, K. Schwarz, S. Sharma, F. Tavazza, P. Thunström, A. Tkatchenko, M. Torrent, D. Vanderbilt, M. J. van Setten, V. Van Speybroeck, J. M. Wills, J. R. Yates, G.-X. Zhang, and S. Cottenier, Reproducibility in Density Functional Theory Calculations of Solids, Science 351, aad3000 (2016).

[50] G. Prandini, A. Marrazzo, I. E. Castelli, N. Mounet, and N. Marzari, Precision and Efficiency in Solid-State Pseudopotential Calculations, Npj Comput. Mater. 4, 1 (2018).

[51] V. Popescu and A. Zunger, Extracting $E$ versus $\vec{k}$ Ef-fective Band Structure from Supercell Calculations on Alloys and Impurities, Phys. Rev. B 85, 085201 (2012).

[52] T. B. Boykin and G. Klimeck, Practical Application of Zone-Folding Concepts in Tight-Binding Calculations, Phys. Rev. B 71, 115215 (2005).

[53] T. B. Boykin, N. Kharche, G. Klimeck, and M. Korkusin-ski, Approximate Bandstructures of Semiconductor Al-loys from Tight-Binding Supercell Calculations, J. Phys.: Condens. Matter 19, 036203 (2007).

[54] P. V. C. Medeiros, S. Stafström, and J. Björk, Effects of Extrinsic and Intrinsic Perturbations on the Electronic Structure of Graphene: Retaining an Effective Primitive Cell Band Structure by Band Unfolding, Phys. Rev. B 89, 041407(R) (2014).

[55] P. V. C. Medeiros, S. S. Tsirkin, S. Stafström, and J. Björk, Unfolding Spinor Wave Functions and Expec-tation Values of General Operators: Introducing the Unfolding-Density Operator, Phys. Rev. B 91, 041116(R) (2015).

[56] M. Iraola, J. L. Mañes, B. Bradlyn, M. K. Horton, T. Neupert, M. G. Vergniory, and S. S. Tsirkin, IrRep: Sym-metry Eigenvalues and Irreducible Representations of Ab Initio Band Structures, Comput. Phys. Commun. 272, 108226 (2022).

[57] R. Dronskowski and P. E. Bloechl, Crystal Orbital Hamil-ton Populations (COHP): Energy-Resolved Visualiza-

tion of Chemical Bonding in Solids Based on Density-
Functional Calculations, J. Phys. Chem. 97, 8617 (1993).

[58] V. L. Deringer, A. L. Tchougréeff, and R. Dronskowski, Crystal Orbital Hamilton Population (COHP) Analy-
sis As Projected from Plane-Wave Basis Sets, J. Phys.
Chem. A 115, 5461 (2011).

[59] S. Maintz, V. L. Deringer, A. L. Tchougréeff, and
R. Dronskowski, Analytic Projection from Plane-Wave
and PAW Wavefunctions and Application to Chemical-
Bonding Analysis in Solids, J. Comput. Chem. 34, 2557
(2013).

[60] S. Maintz, V. L. Deringer, A. L. Tchougréeff, and
R. Dronskowski, LOBSTER: A Tool to Extract Chem-
ical Bonding from Plane-Wave Based DFT., J. Comput.
Chem. 37, iii (2016).

[61] R. Sakuma, T. Miyake, and F. Aryasetiawan, Quasiparti-
cle Band Structure of Vanadium Dioxide, J. Phys.: Con-
dens. Matter 21, 064226 (2009).

[62] X. Yuan, Y. Zhang, T. A. Abtew, P. Zhang, and
W. Zhang, $VO_2$: Orbital Competition, Magnetism, and
Phase Stability, Phys. Rev. B 86, 235103 (2012).

[63] V. Eyert, U. Schwingenschlögl, and U. Eckern, Charge
Order, Orbital Order, and Electron Localization in the
Magnéli Phase $Ti_4O_7$, Chem. Phys. Lett. 390, 151
(2004).

[64] I. Leonov, A. N. Yaresko, V. N. Antonov, U. Schwingen-
schlögl, V. Eyert, and V. I. Anisimov, Charge Order and
Spin-singlet Pair Formation in $Ti_4O_7$, J. Phys. Condens.
Matter 18, 10955 (2006).

[65] All input files available at https://archive.
materialscloud.org/record/2023.2.