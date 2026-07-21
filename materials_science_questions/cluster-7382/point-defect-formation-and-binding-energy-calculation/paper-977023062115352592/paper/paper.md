PHYSICAL REVIEW MATERIALS 8, 033605 (2024)

# Effect of Sn on stacking fault energies in zirconium and its hydrides

P. Chakraborty, $^{1, *}$ I. Mouton, $^{1,2}$ B. Gault, $^{1,3}$ A. Tehranchi, $^{1}$ J. Neugebauer, $^{1}$ and T. Hickel $^{1,4}$

$^{1}$ Max-Planck-Institut für Eisenforschung GmbH, D-40237 Düsseldorf, Germany
$^{2}$ University Grenoble Alpes, CNRS, Grenoble INP, SIMAP, F-38000 Grenoble, France
$^{3}$ Department of Materials, Imperial College London, South Kensington, London SW7 2AZ, United Kingdom
$^{4}$ BAM Federal Institute for Materials Research and Testing, 12489 Berlin, Germany

![](./images/977023062115352592_1.jpg)
(Received 26 August 2023; accepted 27 February 2024; published 18 March 2024)

Hydrogen embrittlement in Zr-alloy fuel cladding is a primary safety concern for water-based nuclear reactors. Here we investigated the stabilization of planar defects within the forming hydrides by Sn, the primary alloying element of Zircaloy-4 used in the cladding. In order to explain the formation of hydrides and planar defects observed in our experiments, we performed atomic-scale ab initio calculations focusing on the solute interactions with generalized stacking faults in hcp $\alpha$-Zr and fcc zirconium hydrides. Our calculations showed that an increase in Sn concentration leads to a stabilization of stacking faults in both the $\alpha$-Zr and hydride phases. However, the solution enthalpy of Sn is lower in the $\alpha$-Zr as compared to the other hydride phases, indicative of two competing processes of Sn depletion/enrichment at the Zr hydride/matrix interface. This is corroborated by experimental findings, where Sn is less soluble in hydrides and is mostly found trapped at interfaces and planar defects, indicative of stacking faults inside the hydride phases. Our systematic investigation enables us to understand the presence and distribution of solutes in the hydride phases, which provides a deeper insight into the microstructural evolution of such alloy's properties during its service lifetime.

DOI: 10.1103/PhysRevMaterials.8.033605

## I. INTRODUCTION

Zirconium-based alloys are commonly used as fuel cladding material in the core of nuclear power reactors because of their low thermal neutron capture cross section and good corrosion resistance [1]. While in operation, the fuel cladding is in contact with water, which promotes the oxidation of Zr [2]. This process releases free hydrogen, part of which enters the alloy and gives rise to the formation of hydrides once the solid solubility limit has been exceeded [3]. The formation of brittle hydrides can have a detrimental effect on the integrity and longevity of the material, as it can lead to the degradation of the mechanical strength through various defect nucleation processes and defect evolution leading to embrittlement [4-6]. The wide use of zirconium alloys in nuclear power reactors has motivated numerous studies on pure zirconium and zirconium hydrides over the past few decades [3,7-9].

At low temperatures and pressures, zirconium is known to have a hexagonal-close-packed (hcp) structure that is commonly referred to as the $\alpha$ phase. The low H solubility limit in zirconium and the thermodynamics of the Zr-H alloy system favors the formation of brittle hydrides, which gives rise to severe safety issues [10-17]. Three main hydride phases have been reported. The $\delta$ phase is a nonstoichiometric phase with a face-centered-cubic (fcc) structure, in which the regular lattice sites are occupied by the Zr atoms and the tetrahedral interstitial sites are randomly occupied by hydrogen. Depending on the temperature, the hydrogen content of the $\delta$-ZrH$_x$ phase varies in the interval $1.4 < x < 1.7$. Increasing the H content beyond this upper limit leads to the formation of $\varepsilon$-ZrH$_2$, which is a face-centered-tetragonal (fct) structure with a unit cell having $c < a$. Another well-known phase is the $\gamma$-ZrH phase, which is a fct structure with $c > a$, usually considered as metastable. It is also frequently observed in nonequilibrium precipitation after quenching from a solid solution. Recent works [18-20] have identified a new hydride phase $\zeta$ probably with a composition close to Zr$_2$H. Fully coherent hcp $\zeta$ hydrides typically evolve into metastable fct $\zeta$ hydrides before a phase transformation occurs to produce fct $\gamma$ hydrides.

Hydride nucleation and growth processes involve dislocation behaviors, including dissociation, spreading motion, recombination and cross slip, in the basal plane of the $\alpha$-Zr lattice [3,17,21,22]. Our recent atom probe tomography (APT) studies [23] on Zircaloy-4 following electrochemical hydrogen charging motivated the extensive ab initio calculations of the present work. We sought to explain the distribution of the primary alloying element of Zircaloy-4, i.e., Sn, in a microstructure containing a hcp Zr lattice and with zirconium hydrides by focusing, in particular, on the solute interactions with stacking faults. Our results shed light on the stabilization of crystalline defects by alloying elements during the growth of hydrides that can further contribute to the material's embrittlement.

*chakraborty@mpie.de

Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI. Open access publication funded by the Max Planck Society.

2475-9953/2024/8(3)/033605(9)
033605-1
Published by the American Physical Society

## II. MATERIALS AND METHODS

### A. Experimental details

Details of the experiments underlying this work can be found in Refs. [23,24]. In short, plates of Zircaloy-4 with a composition of Zr-1.5Sn-0.2Fe-0.1Cr wt% having a blocky-$α$ microstructure [25] were electrochemically charged by using a solution of 1.5 wt.% $H_2SO_4$ in $H_2O$ at $65\,^\circ\text{C}$ for 24 h (all experimental details can be found in [24]). The thick hydride surface layer was dissolved and the hydrogen homogenized throughout the alloy by annealing at $400\,^\circ\text{C}$ for 5 h. The sample was left to cool in the furnace, cooling at approximately $0.5\,^\circ\text{C}/\text{min}$ to promote the formation of both intra- and intergranular hydrides. Specimens for atom probe tomography analysis were prepared using a FEI Helios dual-beam xenon plasma focused ion beam (PFIB), using the protocol proposed in Ref. [26], with the final stage of sharpening performed at a cryogenic temperature to avoid hydride formation during the preparation, as reported previously [23,27]. APT analyses were performed on a CAMECA LEAP 5000 XR, operated in laser pulsing mode, with specimens maintained at a base temperature of 50 K.

### B. Computational details

The theoretical investigations were designed to be directly compared to the experimental results. The calculations were carried out using projector augmented wave (PAW) potentials as implemented in the Vienna Ab initio Simulation Package (VASP) [28,29]. The Perdew–Burke–Ernzerhof (PBE) [30] exchange-correlation functional was chosen. A plane-wave cutoff of 500 eV is considered for all calculations. The convergence tolerance of atomic forces is $0.01\,\text{eV}/\mathring{\text{A}}$ and of total energies it is $10^{-6}\,\text{eV}$. The $\mathbf{k}$-point sampling was conducted by a $\Gamma$-centered Monkhorst-Pack scheme. The sampling density was set large enough that the convergence of total energies was within 2 meV per atom. A supercell size of $5{\times}5{\times}5$ was considered for all bulk calculations. The Brillouin zone integration was carried out using Methfessel-Paxton smearing, with a smearing width of 0.1 eV.

In the present work, bulk properties of $\alpha$-Zr, such as the lattice constant and the solution enthalpy of Sn, were calculated as a function of its concentrations. The solution enthalpy $\Delta E_\text{s}$ of $m$ Sn atoms in the hydride was calculated as
$$
\begin{aligned}
\Delta E_\text{s} &= E(\text{Zr}_{n-m}\text{Sn}_m\text{H}_{nx}) - (n-m)E(\text{ZrH}_x) \\
&\quad - mxE(\text{H}) - mE(\text{Sn}),
\end{aligned}
\tag{1}
$$
where $E(\text{Zr}_{n-m}\text{Sn}_m\text{H}_{nx})$ is the total energy of a $\alpha$-Zr or a Zr-hydride system consisting of $n-m$ Zr atoms and $m$ substitutional Sn atoms. The chemical potential of hydrogen, $E(\text{H})$, has been determined by the following energy difference in the $\delta$-hydride: $E(\text{Zr}_n\text{H}_{1.5n} + \text{H}) - nE(\text{ZrH}_{1.5})$. The same chemical potential of hydrogen has been assumed for the other hydrides because its determination is more complex in ordered phases. Alternatively, the solution enthalpy can be determined by
$$
\Delta E_\text{s} = E(\text{Zr}_{n-m}\text{Sn}_m\text{H}_{nx}) - nE(\text{ZrH}_x) + mE(\text{Zr}) - mE(\text{Sn}).
\tag{2}
$$

In this approach, the chemical potential of Zr is required. If it is determined from the hydride phase itself, the equation is identical to the first version. If a chemical equilibrium with the bulk Zr phase is assumed instead, then the second equation has the advantage not to require an independent H chemical potential. Even though changing the two references changes the absolute values for the solution enthalpy by up to 1 eV, the strongly repulsive Sn-H energy contribution to the solution enthalpy of Sn ensures that the much smaller Zr-H interaction energies entering the first Zr reference do not affect the overall conclusions of this study. The energy $E(\text{Sn})$ is determined for the $I4_1/amd$ $\beta$-Sn system, but this choice is not relevant as it cancels when comparing the Sn solubility in different phases.

Full volume relaxation was performed in these calculations.

A slab supercell was constructed, separated by $10\,\mathring{\text{A}}$ of vacuum from its periodic image, to calculate the generalized stacking fault (GSF) energies. The slab is divided into two equal blocks containing the same number of atomic layers. When the upper block is subject to a relative displacement by an arbitrary vector $\mathbf{f}$, parallel to the slip plane as shown in Fig. 2(a), the shifted structure will have a fault energy $E(\mathbf{f})$. When various slip displacements $\mathbf{f}$ are applied in the plane of the cut, $E(\mathbf{f})$ generates a surface which represents the fault-energy map against the applied displacements. This fault-energy map is the GSF energy surface,
$$
E_{GSF}(\mathbf{f}) = \frac{E(\mathbf{f}) - E(\mathbf{f}=\mathbf{0})}{A},
\tag{3}
$$
where $A$ is the area of the glide plane of the supercell. The size and shape of the supercell were never changed with slip displacements. For a proper mapping of the GSF surface, we only consider atomic relaxations perpendicular to the fault plane in all the calculations. Therefore, the relaxation of atomic positions within the fault plane due to chemical disorder is not taken into account. For further reference, the coverage ratio $C$ is defined for substitutional atoms in a layer adjacent to the slip plane. For example, when $C$ is equal to 0.25, in Fig. 2(a), one out of four atoms in the glide plane is substituted. For the GSF calculations in the $\alpha$-Zr phase, the simulations are performed on rectangular simulation cells having periodic boundary conditions for the $x$ and $y$ axes oriented along $[01\bar{1}0]$, $[2110]$ and a free surface in the $z$ ($[0001]$) direction. The calculation of Sn solution energy was done with the same supercell vectors as taken for the GSF calculations. The number of Zr atoms in the supercell is 95, with 8 atoms in the plane at the stacking fault, out of which one is substituted by a Sn atom, i.e., $C = 0.125$.

In this study, we consider three different hydride phases; the metastable $\zeta$ phase, which later transforms into $\delta$-ZrH$_x$, is also observed in experiments [31]. The $\delta$ phase is known to have an fcc structure with tetrahedral interstitial sites being randomly occupied by hydrogen. To model such compounds at finite temperatures, one can employ configurational cluster expansion techniques [32,33]. However, for consistency with the other considered phases in this work, we approximate the $\delta$ phase to be a disordered alloy model based on $\text{ZrH}_2$ hydride, where the H atoms occupy only six tetrahedral sites, keeping the remaining two tetrahedral sites vacant. However, to achieve, with a limited periodic supercell, a sampling of the chemical configuration space that approximates a true

![](./images/977023062115352592_2.jpg)

FIG. 1. (a) APT reconstructed image of a sample that shows an intergranular hydride packet in between the two grains denoted as alpha 1 and alpha 2. From this perspective, the region marked as Grain alpha 1 may appear as a single hydride; however, the hydride is just on the edge of the dataset and the rest of the reconstruction in this region is made of a $\alpha$-Zr grain (towards higher $y$). (b) Thin slice through the marked section of the reconstructed data delineated by a red box in (a). In this slice, the Zr and H atoms are represented as a purple and yellow dot, respectively, and Sn is the green isosurface similar to (a). The arrow indicates the direction and location of the region of interest along which the composition profile of Sn is evaluated. (c) Composition profile of Sn is taken perpendicular to the Sn-rich plates, which shows the Sn-rich regions in the $\zeta$ hydride. (d) A separate APT needle is shown which contains the trapped Sn-rich plates (green) inside the interconnected hydride regions (yellow). (e) The composition profile of Sn is shown relevant to the APT needle shown in the left figure, which depicts that Sn is trapped inside the $\delta$ hydride.

random alloy as accurately as possible, we employ special quasirandom structures (SQSs) [34]. We have taken large enough supercells to ensure that sufficiently many statistical configurations are captured. While we only consider one specific concentration instead of a range of H concentrations, we expect this approximation to be sufficient as a representative example for the $\delta$ phase. The hydride phases $ZrH_x$ are studied as a function of the H content $x$, where $x = 1$ is for the $\gamma$ phase, $x = 1.5$ is for the $\delta$ phase, and $x = 2$ is for the $\varepsilon$-hydride phase. For the zirconium hydrides, the simulation box is periodic in the $x$ ([1$\overline{1}$0]) and $y$ ([11$\overline{2}$]) directions, and bounded by a free surface in the $z$ ([111]) direction. For the hydrides, the number of H atoms varied according to the value of $x$ in $ZrH_x$. The number of Zr atoms for $\gamma$ hydride and $\varepsilon$ hydride is 71, with 6 atoms at the stacking fault, i.e., the solution energy of Sn is calculated for $C = 0.166$. For $\delta$ hydride, the solution energy of Sn is calculated for $C = 0.125$ with 95 Zr atoms, 8 at the stacking fault, and one Sn atom.

![](./images/977023062115352592_3.jpg)

FIG. 2. Left: Schematic view of GSF calculations for the basal plane in $\alpha$-Zr. The figure represents the shifted structure when the upper part of the initial configuration has glided along the [01$\overline{1}$0] direction in the (0001} basal plane. The coverage ratio $C$ of the glide plane (GP) is evaluated inside the marked plane. Right: The GSF energies are calculated along the [01$\overline{1}$0] $\gamma$ line for pure $\alpha$-Zr and $\alpha$-Zr with Sn atoms. The glide plane is the atomic layer where Sn atoms are substituted and the plane above it consists of only Zr atoms and has a relative displacement opposite to the glide plane. The coverage $C$ is evaluated as the ratio of the total number of Sn atoms vs all atoms in the glide plane. The dashed lines for Sn coverage at $C$ 0.375 and at $C$ 0.5 at the glide plane denote the Boltzmann average at each slip displacement at $400\,^{\circ}\text{C}$ [23,24]. The data points are connected using spline fitting.

## III. RESULTS AND DISCUSSIONS

### A. Experimental results

Figure 1 shows an APT dataset from the same set of analyses as reported in Ref. [23]. This data were obtained from the region ahead of the growth front of an intergranular hydride that has grown perpendicularly to a GB. Sn is less soluble in the growing hydrides and segregates in a few layers of the blocky-$\alpha$ Zircaloy-4 matrix at the interface to the $\delta$ hydrides. This agrees with existing experimental studies [23,35] that also reported the repulsion of Sn from hydrides and the presence of an intermediate $\zeta$ Zr-hydride layer at the interface between the $\delta$ hydride and the $\alpha-\text{Zr}$ matrix. We have observed a series of planar features at the hydride/matrix interface, which appear segregated with Sn and were interpreted as stacking faults in the $\alpha-\text{Zr}$ matrix [23], as readily visible in Fig. 1(a).

Hence, the composition profile in Fig. 1(c) shows that while Sn is locally less soluble in the hydrides as they grow, it eventually gets trapped in planar features present in the hydrides. It is to be noted that even though a quantitative H measurement is challenging in APT, it is, in the case of hydrides, possible to plot the variation in the H composition (in arb. units), indicating the presence of an intermediate, metastable $\zeta$-hydride phase [23]. Figure 1(e) demonstrates that the trapping of Sn to planar features is not limited to the $\zeta$ hydride, but applies to the $\delta$ hydride as well. It is further documented from transmission electron microscopy (TEM) that the stacking faults start growing ahead of the hydrides [35]. The crucial question we ask here is the reason behind such an increase in the accumulation of Sn in planar features, while the solubility inside the hydrides is apparently small (Fig. 1). Henceforth, the interaction of Sn with the $\alpha$-Zr matrix and with the hydrides is evaluated separately in the presence of stacking faults and the comparison is used to explain the mechanisms behind the observations.

<table>
<caption>Table I. Lattice parameters ($\text{\AA}$) of $\alpha$-Zr and $\beta$-Sn compared to other DFT works [36] and experimental values [37].</caption>
<thead>
<tr>
<th>System</th>
<th>Present</th>
<th>Theory</th>
<th>Expt.</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\alpha$-Zr ($a/c$)</td>
<td>3.23/5.17</td>
<td>3.23/5.17</td>
<td>3.23/5.14</td>
</tr>
<tr>
<td>$\beta$-Sn ($a/c$)</td>
<td>5.95/3.21</td>
<td>5.94/3.21</td>
<td>5.83/3.18</td>
</tr>
</tbody>
</table>

### B. Simulation results

#### 1. $\boldsymbol{\alpha}$-Zr and Sn solid solution

To understand and explain why our experiments show a lower solubility of Sn inside the hydrides as compared to the Zr matrix, but at the same time show a substantial increase in the Sn concentration along planar features, we have performed $ab$ initio simulations. As a first step, the bulk phase of $\alpha$-Zr and a Sn solid solution are considered. Table I shows the lattice constants of $\alpha$-Zr and $\beta$-Sn obtained using the present density functional theory (DFT) calculations, which are in good agreement with reported values in the literature [36,37]. All supercells have been constructed by using these lattice parameters as the initial values. Subsequently, the effect of changing the atomic concentration of Sn from 1.04 to 8.33 atomic percents (at.%) has been studied. The solution enthalpy of Sn in $\alpha$-Zr is calculated to be $-1.15\text{eV}$, which is the energy gained by the Sn atom with reference to its bulk phase. Here, the supercell is chosen such that one Zr atom is substituted by Sn in a (0001) plane containing eight Zr atoms.

In order to understand the interaction of Sn with planar defects, we follow the above-mentioned assumptions and analyze the GSF energies obtained by inducing a translational slip along the [01$\overline{1}$0] direction. Doing this, the system encounters a high-symmetry configuration at translation $\text{b}/3$, with $\text{b}$ the Burgers vector in the [01$\overline{1}$0] direction. The corresponding local minimum is commonly known as the stable stacking fault (SSF). The energy barrier that precedes the SSF is termed as unstable stacking fault (USF) energy. The SSF is of significant importance in determining the quantitative character of the plastic deformation. A reduction in the SSF indicates enhanced dissociation of the dislocation core in the basal plane, while for the USF energy, it indicates a reduction of lattice resistance to dislocation motion.

The impact of Sn atoms that are substituted in the glide plane only is shown in Fig. 2. For 50% coverage of Sn atoms at the glide plane, we have considered the results for three stable configurations, as shown in Fig. 3. For 37.5% coverage, a larger simulation cell is considered in which 3 out of 8 atoms on the plane are Sn atoms. Accordingly, there can be several configurations, among which we have compared five configurations with different energies. For these two cases, the GSF energy plots in Fig. 2 represent the mean of the possible configurations for each displacement. In comparison to the SF structure without any Sn atoms, the probability for a certain

![](./images/977023062115352592_4.jpg)

FIG. 3. SSF energy for various configurations of Sn atoms belonging to a coverage ratio of $C\_0.375$ (left) and $C\_0.5$ (right). A snapshot of the fault plane at the stacking fault is shown for each configuration. The green spheres represent the host Zr atoms and red spheres are the Sn atoms; two different atomic planes are shown with the lighter shade corresponding to the fixed atomic plane with Sn atoms. The plot provides the stability of the stable stacking fault energy of Zr-Sn binary systems with respect to a clustering of Sn atoms in the glide plane. The horizontal dashed line is the Boltzmann average of the data points at $400\,^\circ\text{C}$ (annealing temperature [23,24]).

SF configuration is determined by the energy-dependent statistics of Sn segregation and is therefore approximated by a Boltzmann average for each displacement. Here, the segregation energies of the atomic configurations to the stacking faults with respect to a constant chemical potential and the annealing temperature $400\,^\circ\text{C}$ [23,24] enter the Boltzmann weights. A more rigorous thermodynamic approach using, e.g., Monte Carlo methods, is neither feasible for the small systems and long calculation times connected with DFT nor expected to have a strong qualitative impact on the results.

The dependence of the unstable and stable stacking fault energies on Sn coverage is depicted in Fig. 4. With the substitution of Sn atoms in pure Zr, we notice a monotonous decrease of the energy for stacking fault configurations with $C<0.4$. This indicates that the presence of Sn stabilizes the stacking fault structure in $\alpha$-Zr. At the same time, this means that Sn tends to segregate to these planar defects. This is shown in the inset of Fig. 4, where one has to take into account that the coverage here corresponds to the situation prior to segregation. Indeed, the solution enthalpy of single Sn in the (0001) plane with 8 atoms ($C=0.125$) is lower at the SF ($-1.45\,\text{eV}$) compared to pure Zr without fault ($-1.15\,\text{eV}$). Figure 2 indicates that this segregation effect is strongest for the translation $\mathbf{b}/3$ and, for example, much smaller at the USF (see Fig. 4). The consistent decrease in the fault energy until $C=0.375$ in Fig. 2 is due to the stabilization of the SSF. At any of the other defect configurations along the glide plane, the stabilization effect is small and can be neglected. This is further supported by the segregation energy profile of Sn atoms with planar coverage $C$ in the glide plane (GP), as seen in the inset of Fig. 4. Furthermore, both USF energy and SSF energy increase again significantly towards $C=1$, and there is an optimum coverage of the glide plane for less than half of a monolayer of Sn atoms.

![](./images/977023062115352592_5.jpg)

FIG. 4. Fault energies of the stable stacking fault (SSF, red circles) and unstable stacking fault (USF, blue squares) of an $\alpha$-Zr lattice in the basal plane as a function of the coverage ratio $C$ with Sn. Inset: The segregation energy of Sn atoms with the corresponding coverage ratio $C$ to the SSF, where negative values indicate attraction. The coverage ratios $C$ in the inset correspond to the situation prior to segregation, while those in the main plot include the segregated Sn atoms.

### 2. Zirconium hydrides and Sn
We will now focus on the effect of Sn on the GSF in the different hydride systems. Similar to the previous analysis in $\alpha$-Zr, Zr is substituted by Sn on the GP in the hydrides for various coverage ratios. We first note that the calculated solution enthalpy of Sn in $\delta$ hydride is $1.81\,\text{eV}$, which is positive, clearly supporting our earlier statement of the larger solubility in $\alpha$-Zr, where the value was $-1.15\,\text{eV}$.

The GSF energy profiles are plotted along the $\langle\bar{2}11\rangle$ direction in the fcc $\{111\}$ plane for the hydrides. As shown in Fig. 5(b), the GSF energy is found to be the highest for the $\varepsilon$ hydride, followed by $\delta$-ZrH$_{1.5}$. This correlates almost linearly with the H concentration in these phases, while there is, at the same time, an inverse correlation with the $c/a$ ratio in the different phases. Atoms are closely packed in the fcc structure. However, H occupies all its tetrahedral positions in ZrH$_2$, whereas $\delta$-ZrH$_{1.5}$ has, in our calculations, two H vacancies in the supercell. This increases the chance of a

![](./images/977023062115352592_6.jpg)

FIG. 5. GSF energy profiles along the $[\overline{2}11]$ direction in the fcc $\{111\}$ plane. (a) Comparison of the USF energy and the SSF energy between the three hydrides without any solute atoms. (b)-(d) GSF energy profile for $\varepsilon$-ZrH$_2$, $\delta$-Zr$_2$H$_3$, and $\gamma$-ZrH for pure hydride and with substituted Sn atoms with different coverage ratio in the GP, respectively.

distortion of the lattice along the low-energy $\{111\}$ path by reducing the repulsive forces between the H atoms observed in the $\delta$-hydride phase, rendering a lower fault energy.

The GSF energy profiles of the three hydrides are plotted in Fig. 5 for glides along the fcc (111) plane with and without Sn atoms. In the case of the $\varepsilon$ hydride, it is seen from Fig. 5(b) that the GSF has the highest energies among all the other hydrides without any Sn atom, while the changes in the absolute values of the SSF energy with increasing Sn concentration are almost the same for $\varepsilon$ and $\delta$ hydride and Sn coverages in the range $C=0$-$0.25$ at.%. The trend remains qualitatively the same up to coverages of $C=0.5$, though these values are unrealistically high.

For the case of $\gamma$-ZrH, as shown in Fig. 5(d), the USF and SSF are less prominent compared to $\varepsilon$-ZrH$_2$. The introduction of Sn in the lowest concentration further results in flattening of the energy curve. This may be attributed to the fact that H is only occupying $50\%$ of the available interstitial sites, thereby resulting in reduced repulsion and enhanced mobility in the lattice structure. The GSF energy profiles of $\gamma$ hydride show a less systematic dependence on the Sn content compared to the other hydrides since Sn increases the GSF energies for small displacements and the typical decrease is only observed for the SSF as well as larger displacements. An unrealistically high coverage ratio of $C=0.5$ even yields a structural instability.

Since the absolute stacking fault energy (SFE) reduction by Sn is more substantial for the ordered $\varepsilon$-ZrH$_2$ hydride and its SSF than for the $\gamma$-ZrH hydride, we conclude that Sn has a strong segregation effect to stacking faults, in particular in regions with high H concentrations. To convince ourselves that the amount of hydrogen is decisive for the differences between the hydrides and not, for example, the $c/a$ ratio, we have analyzed the Sn impact in $\varepsilon$-ZrH$_2$ with and without a hydrogen vacancy. Figure 6(a) compares the GSF energy profiles with $16.6$ at.% coverage of Sn with the pristine case of the hydride without Sn and with/without a H vacancy at the GP. The fault energy for the pristine hydride is more strongly lowered by Sn in the absence of a H vacancy (approx. $40\%$) compared to the presence of a vacancy (approx. $30\%$).

Another way to interpret these results is the explicit evaluation of the H vacancy formation energy of $\varepsilon$-ZrH$_2$ with and without Sn, as shown in Fig. 6(b). It is seen that independent of the deformation, the vacancy formation energy of H is much lower in the presence of Sn compared to pristine $\varepsilon$-ZrH$_2$. This is a strong proof for the fact that the nearest-neighbor configuration of Sn and H in Zr is energetically highly unfavorable. Vice versa, it indicates that Sn is strongly attracted by these vacancies. The segregation to the stacking faults is, therefore, mainly a consequence of avoiding H-rich environments as present in the bulk hydride phases. Indeed, the positive solution enthalpy of Sn in $\delta$ hydride ($1.81$ eV) is

![](./images/977023062115352592_7.jpg)

FIG. 6. (a) Comparison of the influence of H vacancy in pure $\varepsilon$-ZrH$_2$ and hydride with Sn coverage of 0.166 at the glide plane. (b) The corresponding vacancy formation energy.

substantially reduced to $-0.59\mathrm{eV}$, when stacking faults are present inside the hydride.

### IV. DISCUSSIONS

The results outlined in the previous section suggest a complex interplay of the composition-dependent formation energies of planar defects and the segregation behavior of Sn solutes in all relevant phases. Together, these insights explain the experimentally observed phenomena reported above, in particular the accumulation of Sn at planar features in the hydrides. As outlined in the last section, the direct segregation of Sn atoms solved in the hydride to the forming stacking faults is one possible mechanism. The moderate annealing at $400\ ^{\circ}\mathrm{C}$ for 5 h will, however, limit the kinetics of segregation.

An alternative mechanism for the microstructural evolution next to a grain boundary (GB) is schematically depicted in Fig. 7. Since hydrogen accumulates at the GB, it leads to the growth of a local hydride phase. Based on the variation in the H concentration, the experiments indicate the presence of an intermediate, metastable $\zeta$ phase in addition to the stable hydride phases. Our simulations show, however, that the qualitative conclusions are largely independent of the hydrogen concentration. We consistently observe, for all hydride phases, that the solution enthalpy of Sn is larger than in the $\alpha$-Zr phase (Fig. 8). The resulting local Sn depletion in the region of the forming hydride can be accommodated by a Sn enrichment in the moving interface to the matrix, as depicted by the green arrows in Fig. 7(c). This is also confirmed by the APT composition profile of Sn shown in Fig. 1(c). It is assumed that this process is kinetically more likely than the diffusion in the bulk hydride phase itself.

Next to the hydrides, the formation of planar defects has been observed. The presence of stacking faults could be explained by a strain accumulation, originating from the lattice mismatch between the forming hydride and $\alpha$-Zr matrix. *Wang et al.* [38] previously showed that $\alpha$-Zr grains within such hydride packets exhibit a difference in orientation compared to the parent grain. Therefore, further growth of the hydride can be attributed to a large strain-induced deformation, which causes stacking faults to propagate from the interface into the matrix. In addition, *Udagawa et al.* [36] discussed how the local change in atomic configuration from hcp to fcc at the stacking fault facilitates the nucleation of hydride. Such phase transformation, which is favored thermodynamically via slip on the basal plane, is also mentioned in a relatively recent work [17]. *Zhang et al.* [17] discuss the decomposition of the $\zeta$ phase into $\gamma$ layers and layers of pure

![](./images/977023062115352592_8.jpg)

FIG. 7. Schematic illustration of a mechanism for the evolving microstructure showing a time evolution of hydrides (yellow shading) and the role of stacking faults (black symbols). The distribution and interaction of Sn are depicted by green dots and green arrows. The labels 1, 2, and 3 correspond to the steps indicated in Fig. 8.

![](./images/977023062115352592_9.jpg)

FIG. 8. Solution enthalpy of Sn in pure Zr and the considered hydride phases with different H content ZrH$_x$. The solution enthalpy in the corresponding bulk phases (red symbols) and at the stacking faults (blue symbols) is compared. Two possible mechanisms are indicated by a yellow arrow with label 0 and green arrows for the steps 1, 2, and 3 underlying the schematic process in Fig. 7.

Zr. This is similar to the layered structure that we observe in the stacking faults in $\gamma$ hydride.

As the stacking faults grow into $\alpha$-Zr, they get stabilized by the presence of Sn, as suggested by the above calculations. As a consequence, the Sn atoms that are accumulated locally at the growth front of the hydride are attracted to the stacking faults, as depicted schematically in Fig. 7(b) (step 2). The DFT results have shown (Fig. 4) that the trapping of Sn occurs up to an optimum coverage well below 50 at.%. While the hydride continues growing, this enrichment of Sn in certain layers will be transferred into this phase. Since an attractive interaction of Sn and SFs is observed for the hydride phases, the planar distribution of Sn atoms will impose the formation of stacking faults (step 3).

The energetics of this mechanism is depicted in terms of the Sn solution enthalpy in Fig. 8. The yellow arrow with label “0” indicates the direct segregation of Sn atoms solved in the hydrides to stacking faults within the same phases.

In the alternative multistep mechanism, step 1 indicates the thermodynamic driving force for Sn redistribution into $\alpha$-Zr during the structural transformation from Zr to the hydride phase. The segregation to stacking faults at the interface happens in step 2. Hence, there is an expected accumulation of Sn atoms at the interface due to the atomic rearrangements. Step 3 is the transfer of Sn from a stacking fault in $\alpha$-Zr into a stacking fault in the $\delta$ hydride. It is denoted by a dashed arrow because the increase in solution enthalpy indicates a missing driving force for Sn diffusion in this direction. Instead, the step is determined by the transformation of the matrix phase into the hydride phase and the subsequent formation of stacking faults therein due to the Sn enrichment. We note that due to the missing driving force, there is no diffusion of Sn into the hydride, but it is the expansion of the hydride which modifies the local environment of Sn to become a hydride. Further, the driving force for Sn to find its way out of the hydride again (opposite direction of arrow 3) is much reduced as compared to the one in step 1. Additionally, the corresponding kinetics of the Sn atoms is assumed to be slower because they are now trapped in the stacking faults and blocked by the presence of other Sn atoms.

The overall change in the solution enthalpy is the same for both mechanisms. However, the comparison of the solution enthalpies of Sn in stacking faults of $\alpha$-Zr and hydrides (Fig. 8) reveals that the driving force for Sn to stacking faults is much stronger in the hydrides (step 0) than in the Zr matrix (step 2). As a consequence, Sn atoms effectively push the SFs into the hydrides. This explains the experimentally observed planar defects covered with Sn inside the hydrides, as schematically depicted in Fig. 7(d). The orientation relationship between the matrix and the hydride as observed in the experiments is $\{0001\}_\alpha||\{111\}_\delta$, similar to the SF planes considered for DFT calculations. However, since the stacking sequence of basal planes in the SSF of hcp Zr is fcc like and the stacking sequence of the (111) planes in the SSF of fct hydrides is hcp like, there is not a simple continuation of the SFs between the two phases. It is more likely that the Sn enrichment stabilizes some of the hcp Zr structure in the vicinity of the original stacking faults.

The fact that, despite the prediction of the Sn-Zr phase diagrams [39], the system favors the formation of Sn-rich SFs rather than the formation of a bulk $Zr_4Sn$ phase could be seen as an example of chemically driven defect phase formation [40]. This phenomenon happens when the nucleation barrier associated with the precipitation is high enough to kinetically suppress the formation of a phase in the alloy within experimentally relevant timescales. To lower the energy of the oversaturated alloy, the excess solute atoms form a multitude of solute-rich microstructural features, especially decorated defects. The subsequent state of the alloy, which is metastable in comparison to a phase separation into precipitates, can be described by the concept of metastable defect phase diagrams [41]. In this regard, the presence of hydrides in the Zircaloy further contributes to the kinetics of Sn-rich defect phase formation rather than supporting $Zr_4Sn$ precipitation.

In general, the introduction of Sn in hydrides lowers the SSF energy depending on the structural symmetry and therefore reduces the structural stability. The reduction effect by Sn increases with the hydrogen content in the hydride phases. At the same time, the stacking fault energy under Sn-free conditions also increases with the Sn content. Therefore, the resulting destabilization of the structure with the introduction of Sn atoms remains consistent in all the hydrides even though the magnitudes of the effects vary.

Finally, over the course of the service life of the components (i.e., cladding in the nuclear industry), the pickup of hydrogen and subsequent possible nucleation of hydrides can lead to irrecoverable microstructural changes. Even if one could imagine applying a thermal treatment to dissolve nucleated hydrides, and rejuvenate alloys, the trapped Sn may not be freed and rehydriding would then take place in an alloy with relatively less Sn, in particular in the vicinity of the grain boundaries. There are current developments of an alternative to Zr-Sn-based alloys, in particular by using Nb [42], yet the respective behavior of Nb with respect to hydrides and stacking faults would require a dedicated study and falls outside the scope of the present article.

### V. CONCLUSION

In summary, using *ab initio* simulations of the effect of Sn on the stacking faults in hcp $\alpha$-Zr and in fcc zirconium hydrides allowed us to propose an interesting multistep mechanism for the microstructure formation during hydride growth in Zircaloy-4. The DFT simulations of the hcp $\alpha$-Zr phase showed that an increase in Sn concentration leads to a stabilization of the stacking fault structure up to an optimal coverage of 40 at.% of the glide plane. A similar attraction to stacking faults is also observed in the fcc hydride phases.

The dominant contribution to the thermodynamic driving force of Sn to segregate to stacking faults is its interaction with H. Sn shows a much lower solubility in Zr hydrides than in pure $\alpha$-Zr, while the presence of H vacancies improves the solubility $\varepsilon$-ZrH$_2$. The trend continues with an increasing number of H vacancies in the hydrides, yielding lower stacking fault energies in $\gamma$-ZrH as compared to $\varepsilon$-ZrH$_2$.

From the experiment, it is seen that a series of hydrides is formed at each side of the GB. Small packets of pure Zr are found next to the hydride phases. With our analysis, we understand not only a Sn decoration of stacking faults, but also the reason for the formation of stacking faults inside

the hydride. The present study highlights the effects of Sn in promoting hydrogen trapping sites through planar defects. The GSF curves give the energy barriers associated with the hcp-fcc transformations, which are stabilized by the addition of Sn. Such possible phase transformations via slip systems can be enhanced with the local solute redistribution, which might give further insight into the understanding of the growth and stabilization of hydrides in Zr alloys used in fuel cladding.

## ACKNOWLEDGMENTS
I.M. and B.G. are grateful for the Max-Planck Society and the BMBF for the funding of the Laplace and the UGSLIT projects, respectively, for both instrumentation and person- nel. B.G. and P.C. are grateful for financial support from the ERC-CoG-SHINE-771602. Professor Ben Britton and Dr. Siyang Wang are gratefully acknowledged for the collaborative experimental work on Zr hydrides and deuterides, which were prepared and analyzed in depth as part of HexMat (Grant No. EP/K034332/1) and MIDAS (Grant No. EP- SRC EP/SO1702X/1) programme grants. A.T., T.H., and J.N. acknowledge financial support by the Deutsche Forschungs- gemeinschaft within the SFB1394 "Structural and chemical atomic complexity-from defect phase diagrams to material properties."

[1] C. Lemaignan and A. T. Motta, *Materials Science and Tech- nology, Part II: Nuclear Materials*, 3rd ed., Vol. 10B (VCH Verlagsgesellschaft mbH, 1994).
[2] C. Proff, S. Abolhassani, and C. Lemaignan, J. Nucl. Mater. 416, 125 (2011).
[3] J. Bradbrook, G. Lorimer, and N. Ridley, J. Nucl. Mater. 42,142 (1972).
[4] T. P. Chapman, D. Dye, and D. Rugg, Philos. Trans. R. Soc. A375, 20160418 (2017).
[5] H. Zhang, C. Leygraf, L. Wen, F. Huang, H. Chang, and Y. Jin, Intl. J. Hydrogen Energy 48, 36169 (2023).
[6] W. Qin, J. Szpunar, N. Kiran Kumar, and J. Kozinski, Acta Mater. 81, 219 (2014).
[7] K. G. Barraclough and C. J. Beevers, J. Mater. Sci. 4, 518(1969).
[8] J.-J. Won, S.-J. Min, and K.-T. Kim, Metals Mater. Intl. 21, 31(2015).
[9] D. O. Northwood and U. Kosasih, Intl. Metals Rev. 28, 92(1983).
[10] M. P. Puls, *The Effect of Hydrogen and Hydrides on the Integrity of Zirconium Alloy Components*, 1st ed. (Springer, London,2012).
[11] S. Banerjee and P. Mukhopadhyay, *Phase Transformations*(Elsevier, Amsterdam, 2007), Vol. 12.
[12] J. Bair, M. A. Zaeem, and M. Tonks, J. Nucl. Mater. 466, 12(2015).
[13] M. P. Puls, Acta Metall. 32, 1259 (1984).
[14] V. Perovic, G. Weatherly, and C. Simpson, Scr. Metall. 16, 409(1982).
[15] J. Bai, C. Prioul, and D. Francois, Metall. Mater. Trans. A 25,1185 (1994).
[16] R. A. Antunes and M. C. L. de Oliveira, Innovat. Corrosion Mater. Sci. 4, 96 (2015).
[17] Y. Zhang, X.-M. Bai, J. Yu, M. R. Tonks, M. J. Noordhoek, and S. R. Phillpot, Acta Mater. 111, 357 (2016).
[18] Z. Zhao, Identification and characterization of a new zirconium hydride and mesoscopic-scale modeling of its precipitation us- ing a phase field approach, Ph.D. thesis, University of Lille,2008.
[19] Z. Zhao, J.-P. Morniroli, A. Legris, A. Ambard, Y. Khin, L. Legras, and M. Blat-Yrieix, J. Microsc. 232, 410 (2008).
[20] Z. Zhao, M. Blat-Yrieix, J. Morniroli, A. Legris, L. Thuinet, Y. Kihn, A. Ambard, and L. Legras, J. ASTM Int. 5, 1 (2008).
[21] G. Carpenter, J. Watters, and R. Gilbert, J. Nucl. Mater. 48, 267(1973).
[22] Y. Li, S. Chatterjee, E. Martinez, N. Ghoniem, and G. Po, Acta Mater. 208, 116764 (2021).
[23] I. Mouton, Y. Chang, P. Chakraborty, S. Wang, L. T. Stephenson, T. B. Britton, and B. Gault, Materialia 15, 101006(2021).
[24] R. Birch, S. Wang, V. S. Tong, and T. B. Britton, J. Nucl. Mater.513, 221 (2019).
[25] V. S. Tong and T. B. Britton, Acta Mater. 129, 510 (2017).
[26] K. Thompson, D. Lawrence, D. Larson, J. Olson, T. Kelly, and B. Gorman, UItramicroscopy 107, 131 (2007).
[27] Y. Chang, W. Lu, J. Guénolé, L. T. Stephenson, A. Szczepaniak, P. Kontis, A. K. Ackerman, F. F. Dear, I. Mouton, X. Zhong et al., Nat. Commun. 10, 942 (2019).
[28] G. Kresse and J. Hafner, Phys. Rev. B 47, 558 (1993).
[29] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).
[30] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77,3865(1996).
[31] A. Aladjem, Zirconium-Hydrogen, in Solid State Phenomend(Trans Tech Publications, 1996), Vol. 49-50, pp. 281-330.
[32] A. Van de Walle, Nat. Mater. 7, 455 (2008).
[33] D. Lerch, O. Wieckhorst, G. L. Hart, R. W. Forcade, and S. Müller, Model. Simul. Mater. Sci. Eng. 17, 055003 (2009).
[34] A. Zunger, S.-H. Wei, L. G. Ferreira, and J. E. Bernard, Phys. Rev. Lett. 65, 353 (1990).
[35] A. J. Breen, I. Mouton, W. Lu, S. Wang, A. Szczepaniak, P. Kontis, L. Stephenson, Y. Chang, A. K. da Silva, C. Liebscher et al., Scr. Mater. 156, 42 (2018).
[36] Y. Udagawa, M. Yamaguchi, T. Tsuru, H. Abe, and N. Sekimura, Philos. Mag. 91, 1665 (2011).
[37] R. Russell, J. Appl. Phys. 24, 232 (1953).
[38] S. Wang, F. Giuliani, and T. B. Britton, Microsc. Microanal. 25,1588 (2019).
[39] R. J. Pérez, C. Toffolon-Masclet, J.-M. Joubert, and B. Sundman, Calphad 32, 593 (2008).
[40] S. Korte-Kerzel, T. Hickel, L. Huber, D. Raabe, S. Sandlbes-Haut, M. Todorova, and J. Neugebauer, Intl. Mater. Rev. 67, 89(2022).
[41] A. Tehranchi, S. Zhang, A. Zendegani, C. Scheu, T. Hickel, and J. Neugebauer, arXiv:2303.07504.
[42] K. K. Saxena and V. Pancholi, Metals Mater. Intl. 27, 2106(2021).
