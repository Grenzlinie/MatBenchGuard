# Antisite defects at oxide interfaces
Hanghui Chen $^{1,2}$ and Andrew Millis $^{1}$
$^{1}$Department of Physics, Columbia University, New York, New York 10027, USA
$^{2}$Department of Applied Physics and Applied Math, Columbia University, New York, New York 10027, USA

(Received 21 June 2015; revised manuscript received 3 March 2016; published 31 March 2016)

We use *ab initio* calculations to estimate the formation energies of cation (transition-metal) antisite defects at oxide interfaces and to understand the basic physical effects that drive or suppress the formation of these defects. Antisite defects are found to be favored in systems with substantial charge transfer across the interface, while Jahn-Teller distortions and itinerant ferromagnetism can prevent antisite defects and help stabilize atomically sharp interfaces. Our results enable identification of classes of systems that may be more and less susceptible to the formation of antisite defects, and they motivate experimental studies and further theoretical calculations to elucidate the local structure and stability of oxide interface systems.

DOI: 10.1103/PhysRevB.93.104111

## I. INTRODUCTION
The remarkable electronic properties of transition-metal oxides, including high transition temperature superconductivity [1], colossal magnetoresistance [2], and metal-insulator transitions [3], make them of fundamental importance for condensed-matter physics. Interest increased significantly following the fabrication of atomic-precision heterointerfaces, which bring together different transition-metal oxides with different bulk properties [4–10]. This ability to control materials at the atomic scale holds out the promise of creating systems with entirely new properties and functionalities [11–18].

Realizing these exciting possibilities requires atomically precise interfaces. However, studies of interfaces separating simpler semiconducting materials [19–22] show that antisite defects (exchange of atoms across the interface) may occur and can have crucial (and typically degrading) effects on near-interface electronic properties. In particular, emergent phenomena such as $d$-wave superconductivity and Weyl metal behavior are typically sensitive to disorder, and clean samples are required for a convincing observation [23–25]. Although important work, in particular on defects at interfaces characterized by polar discontinuities, has appeared [26–29], the subject of antisite defects at oxide interfaces has received relatively little attention.

In this paper, we consider antisite defects at $AMO_3/AM'O_3$ interfaces separating different members of the $AMO_3$ class of perovskite transition-metal oxides. In these materials, the $A$ site is occupied by a lanthanide or an alkali earth ion (we consider $A = \text{La}$ or $A = \text{Sr}$), and the $M$ site is occupied by a transition-metal ion (we consider $M,M'$ drawn from the first transition-metal row). We focus on the situation in which the $A$ site is occupied by the same ion throughout and a change in the $M$-site ion defines the interface, so an antisite defect corresponds to an exchange of $M$ and $M'$ ions across the interface [30]. For all relevant combinations of $M$ and $M'$ we compute the defect formation energy, and then we provide a physical understanding of the results in terms of the relative importance of charge transfer across the interface (leading to octahedral volume disproportionation that favors defects) and Jahn-Teller distortions (which inhibit defect formation). For metallic systems, itinerant ferromagnetism emerges as an additional factor inhibiting antisite defects.

The rest of this paper is organized as follows. Section II outlines the methods used; Sec. III presents our principal results, namely energies and local lattice structure for different antisite defect combinations; Sec. IV gives an interpretation of the results in terms of charge transfer, structural distortions, and itinerant ferromagnetism; Sec. V contains a summary and conclusion.

## II. COMPUTATIONAL DETAILS
We perform density functional theory calculations [31,32] within the *ab initio* supercell plane-wave approach [33], as implemented in the Vienna Ab-initio Simulation Package (VASP) [34]. We employ the Perdew, Burke, and Ernzerhof (PBE) parametrization [35] of the generalized gradient approximation (GGA) to the Kohn-Sham potential and projector augmented wave pseudopotentials [36,37]. The energy cutoff is 600 eV. We employ three different types of simulation cells. For most of the calculations, we use a $\sqrt{2} \times \sqrt{2} \times 2$ supercell; to test the effects of interfedefect interactions we use a $2 \times 2 \times 2$ supercell, and to understand the effects of interface-interface separations a $\sqrt{2} \times \sqrt{2} \times 8$ supercell is used. An $8 \times 8 \times 6$ Monkhorst-Pack grid is used to sample the Brillouin zone of the $\sqrt{2} \times \sqrt{2} \times 2$ supercell. A $5 \times 5 \times 5$ Monkhorst-Pack grid is used to sample the Brillouin zone of the $2 \times 2 \times 2$ supercell. An $8 \times 8 \times 2$ Monkhorst-Pack grid is used to sample the Brillouin zone of the $\sqrt{2} \times \sqrt{2} \times 8$ supercell. Both cell and internal coordinates are fully relaxed until each force component is smaller than $10\ \text{meV}/\mathring{\text{A}}$ and the stress tensor is smaller than 10 kbar. Convergence of the key results was tested with a higher energy cutoff and a denser $k$-point sampling, and no significant changes were found. Correlation effects on the $3d$ orbitals are included using the VASP implementation of the rotationally invariant GGA+$U$ approximation introduced in Ref. [38]. We use $U = 5.0\ \text{eV}$ on the $d$ orbitals for all the transition-metal ions considered. For early transition-metal ions ($M = \text{Ti, V, and Cr}$) we choose $J = 0.65\ \text{eV}$ on the $d$ orbitals, and for late transition-metal ions ($M = \text{Mn, Fe, Co, and Ni}$) we choose $J = 1\ \text{eV}$ on the $d$ orbitals. To shift the empty La $4f$ states to higher energy, we also use $U_{\text{La}} = 9.0\ \text{eV}$ on the $f$ orbital, following the value used in previous work [39]. While the

![](./images/814542081107165186_1.jpg)

FIG. 1. Panel A: $2 \times 2 \times 2$ supercell. Panel B: $\sqrt{2} \times \sqrt{2} \times 8$ supercell. Column 1: ideal interfaces with no antisite defects. Column 2: one antisite defect in the supercell. Column 3: two antisite defects in the supercell. Antisite defects are highlighted by the black ellipses.

GGA+$U$ method is only an approximate solution of the correlated electron problem posed by transition-metal oxides, it is generally accepted as a robust method that captures the important trends in ground-state energy and is computationally tractable, permitting surveys of wide ranges of interfaces. The most significant errors are in dynamical quantities that are not important for this work.

## III. RESULTS
### A. Interdefect and interface-interface interactions

We define the defect formation energy as the difference between the energy of systems with and without antisite defects. Computing the energy of a single antisite defect at an isolated interface would require an infinitely large computational cell. Practical calculations employ finite supercells and therefore involve both a nonvanishing defect density and a finite spacing between interfaces. To assess the degree to which our finite supercell calculations are affected by nonvanishing defect densities, we studied a $2 \times 2 \times 2$ supercell (40 atom in total, see Fig. 1 A1), which can accommodate either one or two antisite defects (see Fig. 1 A2 and A3). This corresponds to 25% or 50% defect concentration per interface. We restricted attention to ferromagnetic states to avoid issues of interplay between interdefect spacing and magnetic ordering wave vectors. Results for three representative choices of $A$, $M$, and $M'$ are shown in panel A of Fig. 2. The symbols are the calculated energy differences between a system with $N$ defects and a system with none; the slopes of the dashed lines give the formation energies estimated from the 50% defect concentration calculations. We see that using the higher defect concentration (50%) provides a formation energy that slightly overestimates that from the lower concentration (25%). The higher defect concentration (50%) can be accommodated in a smaller $\sqrt{2} \times \sqrt{2} \times 2$ simulation cell.

To assess the consequences of a finite distance between interfaces, we study a $\sqrt{2} \times \sqrt{2} \times 8$ supercell (80 atoms in total) in which the two interfaces are separated by four unit cells. We consider three configurations: (i) both interfaces are ideal (Fig. 1 B1); (ii) one interface is ideal and the other interface has antisite defects (50% concentration per interface), and (iii) both interfaces have antisite defects (50% concentration per interface). We compare in panel B of Fig. 2 results obtained on a $\sqrt{2} \times \sqrt{2} \times 8$ supercell to results obtained on a $\sqrt{2} \times \sqrt{2} \times 2$ supercell. Isolating the interfaces does not change the sign of the energy difference, but it does increase the magnitude somewhat. These results indicate that a $\sqrt{2} \times \sqrt{2} \times 2$ supercell can be used as a conservative estimator of antisite defect formation energy.

![](./images/814542081107165186_2.jpg)

FIG. 2. Solid symbols (solid lines are there to guide the eye): total energies (with respect to the total energy of ideal interfaces) of various antisite defect configurations (see Fig. 1) calculated (a) in a $2 \times 2 \times 2$ supercell (40 atoms) and (b) in a $\sqrt{2} \times \sqrt{2} \times 8$ supercell (80 atoms). Dashed lines: estimation of defect formation energies calculated in a $\sqrt{2} \times \sqrt{2} \times 2$ supercell (20 atoms). $N$ is the number of antisite defects in the supercell.

### B. Energetics

We use the $\sqrt{2} \times \sqrt{2} \times 2$ supercell to survey 21 $LaMO_3$/$LaM'O_3$ interfaces ($M,M'$=Ti, V, Cr, Mn, Fe, Co, Ni) and 15 $SrMO_3$/$SrM'O_3$ interfaces ($M,M'$=Ti, V, Cr, Mn, Fe, Co). The $\sqrt{2} \times \sqrt{2} \times 2$ simulation cell is illustrated in Fig. 3; it consists of four perovskite primitive cells (20 atoms in total) and is large enough to accommodate both Jahn-Teller [40] and $GdFeO_3$ distortions [41] as well as Néel antiferromagnetic ordering. The stacking direction of the layered structure is along the $z$ axis.

We estimate the defect formation energy for a given $MM'$ combination as
$$
E_{\text{formation}} \simeq \Delta E_{MM'}^{\text{DFT}} = E_{MM'}(R) - E_{MM'}(L), \tag{1}
$$
where $L$ is the configuration of an ideal interface and $R$ is the configuration of one antisite defect, which for the computational unit cell used here corresponds to a rocksalt or double perovskite structure in which the $M$ and $M'$ ions populate alternate unit cells. We consider both ferromagnetic (Fig. 2 A1 and B1) and checkerboard $G$-type antiferromagnetic ordering (Fig. 2 A2 and B2). For the $L$ configuration, we also test $A$-type antiferromagnetic ordering (ferromagnetic planes with magnetization alternating between layers), since this magnetic ordering naturally fits the $L$ configuration (Fig. 2 B3). We always select the magnetic ordering that yields the lowest energy state.

![](./images/814542081107165186_3.jpg)

FIG. 3. Sketch of atomic and magnetic structures considered in this work. Panels A: rocksalt configuration. Panels B: layered configuration. Large orange balls denote A-site ions La or Sr; small red balls denote O ions; shaded octahedra denote octahedra containing transition-metal $M$ (darker shade) and $M'$ (lighter shade) ions, respectively. A1 and B1 are ferromagnetic ordering; A2 and B2 are checkerboard $G$-type antiferromagnetic ordering; B3 is $A$-type antiferromagnetic ordering (spins are parallel in each layer and antiparallel between adjacent layers). Magnetic moments are schematically indicated by green/yellow arrows.

The energetics of antisite defects at oxide interfaces from our calculations are summarized in Fig. 4 A1 and B1 (numerical results for energy differences together with information about the magnetic ordering and whether the system is metallic or insulating are provided in the Appendix). Blue indicates negative defect formation energies; for these cases we expect that the corresponding $MM'$ heterointerfaces are susceptible to antisite defects. Red indicates positive defect formation energies, suggesting those interfaces would be stable against defect formation.

### IV. LOCAL LATTICE DISTORTIONS AND MAGNETISM

#### A. Definitions

In the previous section, we found that for many but not all $M/M'$ combinations, antisite defects were favored. To gain insight into the factors favoring or disfavoring the appearance of antisite defects, we examine the correlation of the defect formation energy with other observables.

A basic motif of the perovskite $AMO_3$ structure is the volume $V_M$ of an $MO_6$ octahedron. Differences in octahedral volume between $MO_6$ and $M'O_6$ octahedra are most easily accommodated in the $R$ configuration, so we define the $MO_6$, $M'O_6$ volume difference as

$$
\lambda_{MM'} = 2\frac{|V_M - V_{M'}|}{V_M + V_{M'}} \tag{2}
$$

with $V_M$ and $V_{M'}$ evaluated in the $R$ configuration.

A second important structural variable is a volume-preserving $Q_2$-type Jahn-Teller distortion of octahedron $MO_6$ in which one pair of $M$-O bonds increases in length and the other decreases; both pairs of bonds alternate in the plane (see the left panel of Fig. 5 B1). As will be shown, the mismatch of $Q_2$-type Jahn-Teller distortions (in-plane octahedral bond disproportionation) between $MO_6$ and $M'O_6$ octahedra makes an important contribution to the stability of the $L$ configuration. To quantify this, we define the bond-length

![](./images/814542081107165186_4.jpg)

FIG. 4. A: $LaMO_3/LaM'O_3$. (A1) DFT-calculated defect formation energy $\Delta E^{\text{DFT}}$ for each combination. The unit is eV per defect. (A2) Structural parameters $\lambda$ and $Q$ for each combination with the most favorable magnetic structure. $\lambda$ is shown in blue in the lower-right triangle and $Q$ is shown in red in the upper-left triangle. The unit on the color bar for $\lambda$ and $Q$ is $\%$. (A3) Comparison between the fitted defect formation energy $\Delta E^{\text{fit}}$ and the DFT-calculated defect formation energy $\Delta E^{\text{DFT}}$. $\Delta E^{\text{fit}}$ are obtained by minimizing $\Omega$ of Eq. (4). B: $SrMO_3/SrM'O_3$. (B1) Same as A1. (B2) Same as A2. The red (blue) backslash denotes those combinations in which $S_{MM'}$ is $-1$ $(+1)$. The other combinations without a backslash have a zero value of $S_{MM'}$. (B3) Same as A3. The solid squares denote $\Delta E^{\text{fit}}$ that are obtained by minimizing $\Omega_{\text{Sr}}$ of Eq. (5). The open squares denote $\Delta E^{\text{fit}}$ that are obtained by minimizing $\Omega$ of Eq. (4). The combinations with a red or blue slash are explicitly labeled.

![](./images/814542081107165186_5.jpg)

FIG. 5. (A1) Top view of two vertically adjacent layers in the $R$ configuration with a large oxygen octahedron (blue) and a small oxygen octahedron (purple). (A2) Top view of two vertically adjacent layers in the $L$ configuration with a naturally large oxygen octahedron (blue) and a naturally small oxygen octahedron (purple). Compatibility with the geometry of the $L$ configuration imposes strains (green arrows) on the system, compressing the large octahedra and expanding the small ones. (B1) Top view of two vertically adjacent layers in the $L$ configuration with one anisotropic oxygen octahedron (purple) and one isotropic oxygen octahedron (blue). (B2) Top view of two vertical adjacent layers in the $R$ configuration with one naturally anisotropic oxygen octahedron (purple) and one naturally isotropic oxygen octahedron (blue). Compatibility with the geometry of the $R$ configuration imposes strains (green arrows) reducing the bond disproportionation of the anisotropic material and inducing a disproportionation in the isotropic one. Rotations and tilts of oxygen octahedra are suppressed for clarity.

disproportionation for ion $M$ as $Q_M=2|l_1-l_2|/(l_1+l_2)$, where $l_1$ and $l_2$ are the two in-plane $M$-O bond lengths for ion $M$ in the $L$ structure, and then we define the bond disproportionation mismatch $Q_{MM'}$ as
$$
Q_{MM'}=|Q_M-Q_{M'}| \tag{3}
$$
for $MO_6$ and $M'O_6$ in two adjacent layers in the $L$ configuration.

### B. Analysis: La-based interfaces

We begin our analysis with the $LaMO_3/LaM'O_3$ interfaces, where for most $MM'$ combinations the ground state is insulating and the GGA+$U$ method is expected to be reliable. Results for $\lambda$ are presented in a color scale in the lower right portion of the boxes in Fig. 4 A2. Comparison to Fig. 4 A1 shows that a large octahedral volume difference is associated with a positive defect formation energy $\Delta E_{MM'}^{\text{DFT}}$. This correlation naturally arises from a strain effect. Figure 5 A1 shows that in the $R$ configuration, the large and small oxygen octahedra can be naturally accommodated. However, the geometry of the $L$ configuration (Fig. 5 A2) requires that the two oxygen octahedra have equivalent in-plane metal-oxygen bond lengths, inducing internal strain (represented by green arrows in Fig. 5 A2) relative to the bond lengths preferred by the given charge configurations, thereby increasing the elastic energy of the $L$ configuration. We note that although rotations of oxygen octahedra can accommodate different octahedral volumes, our calculations on fully relaxed structures show that octahedral rotations cannot reduce enough strain to favor the $L$ configuration.

For bulk $LaMO_3$, the octahedral volumes change $\lesssim10\%$ (the variation of the lattice constant is $\lesssim3\%$) as $M$ is varied over the whole first transition-metal row, but larger volume differences may occur in the superlattices. For example, $\lambda=15.1\%$ for $LaTiO_3/LaNiO_3$ [13] and $\lambda=19.4\%$ for $LaTiO_3/LaFeO_3$ [18]. These very large $MO_6$ volume differences are associated with complete charge transfer from $M$ to $M'$ ions, i.e., $M^{3+}+M'^{3+}\rightarrow M^{4+}+M'^{2+}$ (La systems) or $M^{4+}+M'^{4+}\rightarrow M^{5+}+M'^{3+}$ (Sr systems). The $MO_6$ octahedral volume of electron acceptors expands while that of electron donors contracts. These substantial charge transfers are driven by large electronegativity differences between $M$ and $M'$ ions [12-14]. A full list of the combinations in $LaMO_3/LaM'O_3$ that have a complete charge transfer from $M$ to $M'$ is given in Table I. We see that interfaces at which significant charge transfer occurs are expected to be more susceptible to antisite defects.

While charge transfer leads to octahedral volume changes that favor defects, the mismatch of $Q_2$-type Jahn-Teller distortions between $MO_6$ and $M'O_6$ tends to inhibit defects. As can be seen from Fig. 5 B2, if a volume-preserving octahedral distortion has different amplitudes on the $M$ and $M'$ sites, it cannot naturally be accommodated in the $R$ configuration (green arrows indicate strain). However, as Fig. 5 B1 shows, as long as the $MO_2$ and $M'O_2$ sheets have similar mean in-plane bond lengths, arbitrary layer-dependent $Q_2$-type Jahn-Teller distortions can be accommodated without strain in the $L$ configuration. $Q_{MM'}$, which mathematically defines the mismatch of $Q_2$-type distortions in Eq. (3), is calculated for different $MM'$ combinations using the $L$ configuration, and the results for $Q_{MM'}$ are presented in a color scale in the upper left portion of the boxes in Fig. 4 A2. Comparison to Fig. 4 A1 shows that a large Jahn-Teller mismatch is associated with a negative defect formation energy $\Delta E_{MM'}^{\text{DFT}}$. Among La compounds, $LaMnO_3$ has the strongest $Q_2$-type Jahn-Teller distortion [2]. Our calculations confirm that the combinations $LaVO_3/LaMnO_3$, $LaCrO_3/LaMnO_3$, and $LaMnO_3/LaFeO_3$, in which the Mn is in a $d^4$ high-spin state, all favor the $L$ configuration, thereby tending to suppress antisite defects. We notice that in all three cases, $Q_{\text{Mn}}$ exceeds 10%, a value much larger than that found for other ions (see Table I).

As with the volume change, the relevant question for the $Q_2$-type distortion is the occupancy and spin state in a given structure, after any charge transfer has occurred. Usually large $Q_2$-type distortions are associated with negligible charge transfer, because charge transfer tends to create empty/half-filled/filled $d$ shells that are not Jahn-Teller active. Examples include $LaMnO_3/LaNiO_3$ ($d^4+d^7\rightarrow d^3+d^8$) and $LaTiO_3/LaMnO_3$ ($d^1+d^4\rightarrow d^0+d^5$). In both cases, the charge transfer moves the Mn configuration away from the high-spin $d^4$ state that favors Jahn-Teller distortions.

The volume difference and Jahn-Teller effects will typically coexist and compete. To understand how this plays out in practice, we introduce a cost function
$$
\Omega=\sum_{(MM')}\left[\Delta E_{MM'}^{\text{DFT}}-\left(\alpha\lambda_{MM'}+\beta Q_{MM'}\right)\right]^2, \tag{4}
$$

<table>
<caption>Table I: The combinations in La₂MM′O₆, which have a complete charge transfer from M to M′ ions (upper part) and which have a high-spin d⁴ configuration (lower part). ΔEᵐₘ′ᴰᴱᵀ is the defect formation energy [Eq. (1) in the main text] using the most favorable magnetic ordering. The unit is eV per defect. λₘₘ′ is the MO₆ octahedral volume difference using the R configuration [Eq. (2)]. Qₘ describes the magnitude of Q₂-type Jahn-Teller distortions of ion M using the L configuration [Eq. (3)].</caption>
<tbody>
<tr>
<td colspan="4">The combinations with a complete charge transfer</td>
</tr>
<tr>
<td>Charge configuration</td>
<td>Materials system</td>
<td>ΔEᵐₘ′ᴰᴱᵀ</td>
<td>λₘₘ′ of the R configuration</td>
</tr>
<tr>
<td>d¹−d²→d⁰−d³</td>
<td>La₂TiVO₆</td>
<td>−0.35</td>
<td>23.9%</td>
</tr>
<tr>
<td>d¹−d⁴→d⁰−d⁵</td>
<td>La₂TiMnO₆</td>
<td>−1.03</td>
<td>27.0%</td>
</tr>
<tr>
<td>d¹−d⁵→d⁰−d⁶</td>
<td>La₂TiFeO₆</td>
<td>−1.24</td>
<td>19.4%</td>
</tr>
<tr>
<td>d¹−d⁶→d⁰−d⁷</td>
<td>La₂TiCoO₆</td>
<td>−0.56</td>
<td>18.4%</td>
</tr>
<tr>
<td>d¹−d⁷→d⁰−d⁸</td>
<td>La₂TiNiO₆</td>
<td>−0.44</td>
<td>15.1%</td>
</tr>
<tr>
<td>d²−d⁶→d¹−d⁷</td>
<td>La₂VCoO₆</td>
<td>−0.37</td>
<td>20.4%</td>
</tr>
<tr>
<td>d⁴−d⁶→d³−d⁷</td>
<td>La₂MnCoO₆</td>
<td>−0.23</td>
<td>24.0%</td>
</tr>
<tr>
<td>d⁴−d⁷→d³−d⁸</td>
<td>La₂MnNiO₆</td>
<td>−0.78</td>
<td>18.0%</td>
</tr>
<tr>
<td colspan="4">The combinations with a high-spin d⁴ configuration</td>
</tr>
<tr>
<td>Charge configuration</td>
<td>Materials system</td>
<td>ΔEᵐₘ′ᴰᴱᵀ</td>
<td>Qₘ of the L configuration</td>
</tr>
<tr>
<td>d²−d⁴</td>
<td>La₂VMnO₆</td>
<td>0.26</td>
<td>Qₘₙ=11.1%, Qᵥ=0.5%</td>
</tr>
<tr>
<td>d³−d⁴</td>
<td>La₂CrMnO₆</td>
<td>0.20</td>
<td>Qₘₙ=10.3%, Q_cᵣ=0.0%</td>
</tr>
<tr>
<td>d⁴−d⁵</td>
<td>La₂MnFeO₆</td>
<td>0.28</td>
<td>Qₘₙ=14.9%, Qբₑ=1.0%</td>
</tr>
</tbody>
</table>

where the sum is over all the combinations MM′. λₘₘ′ are calculated using the R configuration and Qₘₘ′ using the L configuration. Minimizing Eq. (4) yields $\alpha = -3.0$ eV and $\beta = 2.7$ eV for the La-based heterostructures. The opposite signs of $\alpha$ and $\beta$ indicate that the volume change ($\lambda_{MM'}$) and Jahn-Teller effect ($Q_{MM'}$) compete, as expected. The comparison between $\Delta E_{MM'}^{\text{DFT}}$ and $\Delta E_{MM'}^{\text{fit}} = \alpha \lambda_{MM'} + \beta Q_{MM'}$ is shown in Fig. 4 A3. While there is non-negligible scatter, the fit is reasonably good. In particular, the crude model correctly predicts the stability against defect formation (i.e., the sign of $\Delta E_{MM'}^{\text{DFT}}$) for most cases.

### C. Sr-based compounds

Next we consider the Sr-based compounds. The defect formation energy $\Delta E_{MM'}^{\text{DFT}}$ for SrMO₃/SrM′O₃ is shown in Fig. 4 B1. The λₘₘ′ and Qₘₘ′ for Sr-based heterostructures are calculated and displayed in Fig. 4 B2. As for the La-based heterostructures, substantial charge transfer leads to large octahedral volume differences and favors the R configuration (examples include SrVO₃/SrCrO₃: $d^{1} - d^{2} \rightarrow d^{0} - d^{3}$ and $\lambda = 5.6\%$; SrVO₃/SrFeO₃: $d^{1} - d^{4} \rightarrow d^{0} - d^{5}$ and $\lambda = 5.6\%$) while a large mismatch of Q₂-type Jahn-Teller distortions stabilizes the L configuration, for example SrFeO₃/SrCoO₆. However, we notice that the combinations (SrTiO₃/SrFeO₃, SrTiO₃/SrCoO₃, SrVO₃/SrMnO₃, and SrCrO₃/SrFeO₃) that strongly favor the L configuration have a nearly vanishing Q₂ mismatch, suggesting the presence of an additional mechanism in the Sr-based heterostructures.

We believe the additional mechanism acting in the Sr-based heterostructures is itinerant ferromagnetism, which if present in the L configuration but not in the R configuration, stabilizes the L configuration. The MM′ combinations with a ferromagnetic-metallic ground state in the L configuration and a nonferromagnetic-metallic ground state in the R configuration are labeled by a red slash in Fig. 4 B2. Comparison of Fig. 4 B2 to Fig. 4 B1 makes the stabilization effect evident. There is one case (SrCrO₃/SrCoO₃) in which the R configuration is ferromagnetic metallic and the L configuration is not. As we will show below, in this case (labeled by a blue slash in Fig. 4 B2) itinerant ferromagnetism does not significantly contribute to the stabilization of the R configuration.

To model the effects of metallic ferromagnetism, we define $S_{MM'} = S_{MM'}^{R} - S_{MM'}^{L}$, where $S_{MM'}^{R}$ and $S_{MM'}^{L}$ take the value 1 for ferromagnetic metallic states and 0 otherwise for the R and L configurations, respectively. We include this term in the cost function, obtaining

$$
\Omega_{\mathrm{Sr}}=\sum_{\left(M M^{\prime}\right)}\left[\Delta E_{M M^{\prime}}^{\mathrm{DFT}}-\left(\alpha \lambda_{M M^{\prime}}+\beta Q_{M M^{\prime}}+\gamma S_{M M^{\prime}}\right)\right]^{2}.
\tag{5}
$$

Minimizing the cost Ω_Sr yields $\alpha = -1.8$ eV, $\beta = 2.0$ eV, and $\gamma = -0.4$ eV. We comment that both in La compounds and in Sr compounds, $\alpha$ and $\beta$ are very close in magnitude and of opposite signs, implying that the physical effects from the volume mismatch ($\lambda_{MM'}$) and the Jahn-Teller distortion mismatch ($Q_{MM'}$) are comparable, and the competition between the two effects is a general phenomenon. The fit with S_MM' is shown in Fig. 4 B3 as solid symbols and is clearly superior to the fit performed without S_MM' (open symbols). Inclusion of S_MM' makes the $\Delta E^{\text{fit}}$ of the combinations with a red slash much closer to $\Delta E^{\text{DFT}}$, indicating a key role of itinerant ferromagnetism in stabilizing the L configuration. However, for the case with a blue slash, inclusion of S_MM' drives $\Delta E^{\text{fit}}$ farther away from $\Delta E^{\text{DFT}}$, implying that itinerant ferromagnetism does not significantly contribute to the stabilization of the R configuration.

We make two comments concerning the Sr-based compounds. First, GGA+$U$ predicts charge ordering in a number of SrMO₃/SrM′O₃ cases. Two-sublattice charge ordering is

compatible with the $\sqrt{2} \times \sqrt{2} \times 2$ computational cell used here. It leads to an additional contribution to the energy difference that is not taken into account in Eq. (5). However, Eq. (5) works reasonably well, indicating that charge ordering does not substantially affect energetics. A more accurate many-body method (beyond GGA+$U$) is needed to study the delicate effects of long-range orderings [42]. Second, $\text{SrFeO}_3$, which in bulk is in the high-spin $d^4$ configuration, is not Jahn-Teller active (unlike $\text{LaMnO}_3$), presumably due to the enhanced covalency of Fe-O bonding [43].

## V. CONCLUSION

In conclusion, we have shown that $M/M'$ antisite defects are energetically favored in wide classes of $AMO_3/AM'O_3$ heterostructures. The key driver of defect formation is a high degree of charge transfer across oxide interfaces, leading to large differences in equilibrium octahedral volume, which in turn are most easily accommodated by antisite defect formation. On the other hand, a large mismatch of $Q_2$-type Jahn-Teller distortion tends to inhibit antisite defects due to geometry constraints, as does itinerant ferromagnetism, which in these systems is a signature of coherent metallic behavior across the interface. The association of defects with charge transfer is unfortunate, as charge transfer is an important route to obtaining new physics [12–14].

Experimentally, near-interface "dead layers" of transition-metal oxides are frequently reported [44,45], suggesting a possible relevance of the present calculations to the behavior of real interfaces. On the other hand, high-quality $\text{LaTiO}_3/\text{LaNiO}_3$ [16] and $\text{LaTiO}_3/\text{LaFeO}_3$ [18] interfaces have been reported. Further experimental studies of transition-metal antisite defects at oxide interfaces would be very valuable for shedding light on this physics. On the theoretical side, we note that our calculations are based on the GGA+$U$ approximation. While this method is believed to be a good approximation to the energetics of insulating systems, further investigation of selected cases using more sophisticated (but much more computationally expensive) methods such as dynamical mean-field theory would also be desirable (although we emphasize that getting the local lattice structure correct is essential), and it is also interesting that our conclusions for the more metallic Sr compounds might also be revisited with other methods. We also note that we have used the same $U$ value for all compounds. This choice is motivated by a desire to investigate chemical systematics without additional confounding factors, but we note that our experience is that as long as $U$ is not too small ($\gtrsim4$ eV) and not too large ($\lesssim10$ eV), the basic physics of importance here (charge transfer, octahedral volume, and Jahn-Teller distortions) is not particularly sensitive to $U$.

## ACKNOWLEDGMENTS

H.C. is supported by the National Science Foundation under Grant No. DMR-1120296. A.J.M. is supported by the Department of Energy under Grant No. DOE-ER-046169. Computational facilities are provided via Extreme Science and Engineering Discovery Environment, through Award No. TG-PHY130003 and via the National Energy Research Scientific Computing Center.

## APPENDIX: ENERGY DIFFERENCE, MOST FAVORABLE MAGNETIC ORDERING, AND TRANSPORT PROPERTIES

We show in Tables II and III the DFT-calculated energy differences $\Delta E_{MM'}^{\text{DFT}}$, defined in Eq. (1) in the main text. Table II is for La compounds and Table III is for Sr compounds. For each combination $MM'$, we also show the most favorable magnetic ordering and transport properties for the rocksalt ($R$) and layered ($L$) configurations. Text in blue (red) indicates those combinations that favor the rocksalt configuration (layered configuration).

<table>
<caption>TABLE II. $\text{La}_2MM'\text{O}_6$, where $M,M'$ = Ti, V, Cr, Mn, Fe, Co, and Ni. The lower half is the energy difference between the $R$ and $L$ configurations $\Delta E = E(R) - E(L)$. The unit is eV per supercell (20 atoms). The upper half shows the most favorable magnetic ordering and transport properties for each configuration. $F$ denotes ferromagnetic ordering, $G$ denotes $G$-type antiferromagnetic ordering, $A$ denotes $A$-type antiferromagnetic ordering, $M$ denotes metallic, $I$ denotes insulating, and CO denotes charge ordering.</caption>
<tbody><tr><td></td><td>$\text{LaTiO}_3$ ($d^1$)</td><td>$\text{LaVO}_3$ ($d^2$)</td><td>$\text{LaCrO}_3$ ($d^3$)</td><td>$\text{LaMnO}_3$ ($d^4$)</td><td>$\text{LaFeO}_3$ ($d^5$)</td><td>$\text{LaCoO}_3$ ($d^6$)</td><td>$\text{LaNiO}_3$ ($d^7$)</td></tr>
<tr><td>$\text{LaTiO}_3$ ($d^1$)</td><td>bulk</td><td>$R$ : $G$-$I$<br>$L$ : $A$-$I$</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $G$-$I$<br>$L$ : $F$-$M$</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td></tr>
<tr><td>$\text{LaVO}_3$ ($d^2$)</td><td>$-0.348$</td><td>bulk</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $F$-$I$<br>$L$ : $F$-$I$</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $F$-$I$<br>$L$ : $G$-$I$</td></tr>
<tr><td>$\text{LaCrO}_3$ ($d^3$)</td><td>$0.036$</td><td>$-0.024$</td><td>bulk</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $F$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $F$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $F$-$M$<br>$L$ : $F$-$M$</td></tr>
<tr><td>$\text{LaMnO}_3$ ($d^4$)</td><td>$-1.028$</td><td>$0.264$</td><td>$0.196$</td><td>bulk</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $G$-$I$<br>$L$ : $A$-$I$-CO</td><td>$R$ : $F$-$I$<br>$L$ : $F$-$M$</td></tr>
<tr><td>$\text{LaFeO}_3$ ($d^5$)</td><td>$-1.244$</td><td>$0.144$</td><td>$0.144$</td><td>$0.276$</td><td>bulk</td><td>$R$ : $G$-$I$<br>$L$ : $G$-$I$</td><td>$R$ : $F$-$M$<br>$L$ : $F$-$M$</td></tr>
<tr><td>$\text{LaCoO}_3$ ($d^6$)</td><td>$-0.556$</td><td>$-0.368$</td><td>$0.304$</td><td>$-0.232$</td><td>$-0.012$</td><td>bulk</td><td>$R$ : $F$-$I$<br>$L$ : $G$-$I$</td></tr>
<tr><td>$\text{LaNiO}_3$ ($d^7$)</td><td>$-0.444$</td><td>$-0.264$</td><td>$0.476$</td><td>$-0.784$</td><td>$-0.104$</td><td>$-0.492$</td><td>bulk</td></tr>
</tbody></table>

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    SrTiO₃ ($d^{0}$)
   </th>
   <th>
    SrVO₃ ($d^{1}$)
   </th>
   <th>
    SrCrO₃ ($d^{2}$)
   </th>
   <th>
    SrMnO₃ ($d^{3}$)
   </th>
   <th>
    SrFeO₃ ($d^{4}$)
   </th>
   <th>
    SrCoO₃ ($d^{5}$)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    SrTiO₃ ($d^{0}$)
   </th>
   <td>
    bulk
   </td>
   <td>
    $R:G(I)$
    <br/>
    $L:F(I)$
   </td>
   <td>
    $R:F(I)$
    <br/>
    $L:G(I)$
   </td>
   <td>
    $R:G(I)$
    <br/>
    $L:G(I)$
   </td>
   <td>
    $R:G(M)$
    <br/>
    $L:F(M)$
   </td>
   <td>
    $R:G(M)$
    <br/>
    $L:F(M)$
   </td>
  </tr>
  <tr>
   <th>
    SrVO₃ ($d^{1}$)
   </th>
   <td>
    0.056
   </td>
   <td>
    bulk
   </td>
   <td>
    $R:G(I)$
    <br/>
    $L:F$-$CO(I)$
   </td>
   <td>
    $R:G(M)$
    <br/>
    $L:F$-$CO(M)$
   </td>
   <td>
    $R:G(I)$
    <br/>
    $L:A(M)$
   </td>
   <td>
    $R:F(I)$
    <br/>
    $L:G(M)$
   </td>
  </tr>
  <tr>
   <th>
    SrCrO₃ ($d^{2}$)
   </th>
   <td>
    $- 0.072$
   </td>
   <td>
    $- 0.644$
   </td>
   <td>
    bulk
   </td>
   <td>
    $R:G(M)$
    <br/>
    $L:G$-$CO(M)$
   </td>
   <td>
    $R:G$-$CO(M)$
    <br/>
    $L:F(M)$
   </td>
   <td>
    $R:F(M)$
    <br/>
    $L:A$-$CO(M)$
   </td>
  </tr>
  <tr>
   <th>
    SrMnO₃ ($d^{3}$)
   </th>
   <td>
    $- 0.396$
   </td>
   <td>
    0.476
   </td>
   <td>
    $- 0.088$
   </td>
   <td>
    bulk
   </td>
   <td>
    $R:F(M)$
    <br/>
    $L:F(M)$
   </td>
   <td>
    $R:F(M)$
    <br/>
    $L:F(M)$
   </td>
  </tr>
  <tr>
   <th>
    SrFeO₃ ($d^{4}$)
   </th>
   <td>
    0.456
   </td>
   <td>
    $- 0.468$
   </td>
   <td>
    0.244
   </td>
   <td>
    $- 0.184$
   </td>
   <td>
    bulk
   </td>
   <td>
    $R:F(M)$
    <br/>
    $L:F(M)$
   </td>
  </tr>
  <tr>
   <th>
    SrCoO₃ ($d^{5}$)
   </th>
   <td>
    0.312
   </td>
   <td>
    $- 0.008$
   </td>
   <td>
    $- 0.084$
   </td>
   <td>
    $- 0.460$
   </td>
   <td>
    0.268
   </td>
   <td>
    bulk
   </td>
  </tr>
 </tbody>
</table>

TABLE III. Sr₂$MM^{\prime}$O₆, where $M,{M^{\prime}} =$ Ti, V, Cr, Mn, Fe, and Co. The lower half is the energy difference between the $R$ and $L$ configurations $\Delta E = {E(R) - E(L)}$. The unit is eV per supercell (20 atoms). The upper half shows the most favorable magnetic ordering and transport properties for each configuration. $F$ denotes ferromagnetic ordering, $G$ denotes $G$-type antiferromagnetic ordering, $A$ denotes $A$-type antiferromagnetic ordering, $M$ denotes metallic, $I$ denotes insulating, and CO denotes charge ordering.

[1] P. A. Lee, N. Nagaosa, and X.-G. Wen, Rev. Mod. Phys. 78, 17 (2006).

[2] M. B. Salamon and M. Jaime, Rev. Mod. Phys. 73, 583 (2001).

[3] M. Imada, A. Fujimori, and Y. Tokura, Rev. Mod. Phys. 70, 1039 (1998).

[4] A. Ohtomo, D. A. Muller, J. L. Grazul, and H. Y. Hwang, Nature (London) 419, 378 (2002).

[5] A. Ohtomo and H. Y. Hwang, Nature (London) 427, 423 (2004).

[6] J. Chakhalian, J. W. Freeland, G. Srajer, J. Strempfer, G. Khaliullin, J. C. Cezar, T. Charlton, R. Dalgliesh, C. Bernhard, G. Cristiani et al., Nat. Phys. 2, 244 (2006).

[7] J. Chakhalian, J. W. Freeland, H.-U. Habermeier, G. Cristiani, G. Khaliullin, M. van Veenendaal, and B. Keimer, Science 318, 1114 (2007).

[8] K. Yoshimatsu, K. Horiba, H. Kumigashira, T. Yoshida, A. Fujimori, and M. Oshima, Science 333, 319 (2011).

[9] E. J. Monkman, C. Adamo, J. A. Mundy, D. E. Shai, J. W. Harter, D. Shen, B. Burganov, D. A. Muller, D. G. Schlom, and K. M. Shen, Nat. Mater. 11, 855 (2012).

[10] S. J. May, P. J. Ryan, J. L. Robertson, J.-W. Kim, T. S. Santos, E. Karapetrova, J. L. Zarestky, X. Zhai, S. G. E. te Velthuis, J. N. Eckstein et al., Nat. Mater. 8, 892 (2009).

[11] J. Mannhart, D. H. A. Blank, H. Y. Hwang, A. J. Millis, and J. M. Triscone, MRS Bull. 33, 1027 (2011).

[12] H. Chen, D. P. Kumah, A. S. Disa, F. J. Walker, C. H. Ahn, and S. Ismail-Beigi, Phys. Rev. Lett. 110, 186402 (2013).

[13] H. Chen, A. J. Millis, and C. A. Marianetti, Phys. Rev. Lett. 111, 116403 (2013).

[14] H. Chen, H. Park, A. J. Millis, and C. A. Marianetti, Phys. Rev. B 90, 245138 (2014).

[15] A. S. Disa, D. P. Kumah, A. Malashevich, H. Chen, D. A. Arena, E. D. Specht, S. Ismail-Beigi, F. J. Walker, and C. H. Ahn, Phys. Rev. Lett. 114, 026801 (2015).

[16] Y. Cao, X. Liu, M. Kareev, D. Choudhury, S. Middey, D. Meyers, J.-W. Kim, P. Ryan, J. W. Freeland, and J. Chakhalian, Nat. Commun. 7, 10418 (2016).

[17] M. Karolak, M. Edelmann, and G. Sangiovanni, Phys. Rev. B 91, 075108 (2015).

[18] J. E. Kleibeuker, Z. Zhong, H. Nishikawa, J. Gabel, A. Müller, F. Pfaff, M. Sing, K. Held, R. Claessen, G. Koster et al., Phys. Rev. Lett. 113, 237402 (2014).

[19] G. B. Bachelet, M. Schlüter, and G. A. Baraff, Phys. Rev. B 27, 2545 (1983).

[20] G. A. Baraff and M. Schlüter, Phys. Rev. Lett. 55, 1327 (1985).

[21] B. K. Meyer, J. M. Spaeth, and M. Scheffler, Phys. Rev. Lett. 52, 851 (1984).

[22] T. Mattila and R. M. Nieminen, Phys. Rev. Lett. 74, 2721 (1995).

[23] J. Chakhalian, J. W. Freeland, A. J. Millis, C. Panagopoulos, and J. M. Rondinelli, Rev. Mod. Phys. 86, 1189 (2014).

[24] S. Adam, E. H. Hwang, V. M. Galitski, and S. Das Sarma, Proc. Natl. Acad. Sci. (U.S.A.) 104, 18392 (2007).

[25] S. Das Sarma, S. Adam, E. H. Hwang, and E. Rossi, Rev. Mod. Phys. 83, 407 (2011).

[26] N. Nakagawa, H. Y. Hwang, and D. A. Muller, Nat. Mater. 5, 204 (2006).

[27] S. Chambers, M. Engelhard, V. Shutthanandan, Z. Zhu, T. Droubay, L. Qiao, P. Sushko, F. T., H. Lee, T. Gustafsson et al., Surf. Sci. Rep. 65, 317 (2010).

[28] C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer, G. Kresse, A. Janotti, and C. G. Van de Walle, Rev. Mod. Phys. 86, 253 (2014).

[29] L. Yu and A. Zunger, Nat. Commun. 5, 5118 (2014).

[30] The alternative interfaces $AMO_{3}$/$A^{\prime}MO_{3}$ and the corresponding ($AA^{\prime}$) antisite defects are considered in [10] and references therein.

[31] P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964).

[32] W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).

[33] M. C. Payne, M. P. Teter, D. C. Allan, T. A. Arias, and J. D. Joannopoulos, Rev. Mod. Phys. 64, 1045 (1992).

[34] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[35] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[36] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

[37] G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

[38] A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, *Phys. Rev. B* **52**, R5467 (1995).

[39] R. Chen, S. B. Lee, and L. Balents, *Phys. Rev. B* **87**, 161119 (2013).

[40] H. Jahn and E. Teller, *Proc. R. Soc. London, Ser. A* **161**, 220 (1937).

[41] F. S. Gallasso, *Structure, Properties and Preparation of Perovskite Type Compounds* (Pergamon, Oxford, 1969).

[42] C.-K. Chan, P. Werner, and A. J. Millis, *Phys. Rev. B* **80**, 235114 (2009).

[43] P. Adler, A. Lebon, V. Damljanović, C. Ulrich, C. Bernhard, A. V. Boris, A. Maljuk, C. T. Lin, and B. Keimer, *Phys. Rev. B* **73**, 094451 (2006).

[44] M. Huijben, L. W. Martin, Y.-H. Chu, M. B. Holcomb, P. Yu, G. Rijnders, D. H. A. Blank, and R. Ramesh, *Phys. Rev. B* **78**, 094413 (2008).

[45] A. Tebano, C. Aruta, S. Sanna, P. G. Medaglia, G. Balestrino, A. A. Sidorenko, R. De Renzi, G. Ghiringhelli, L. Braicovich, V. Bisogni *et al.*, *Phys. Rev. Lett.* **100**, 137401 (2008).