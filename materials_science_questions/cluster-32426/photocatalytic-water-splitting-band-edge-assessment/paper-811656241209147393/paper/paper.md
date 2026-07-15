PHYSICAL REVIEW B 83, 235301 (2011)

# Prediction of semiconductor band edge positions in aqueous environments from first principles

Yabi Wu, $^{1}$ M. K. Y. Chan, $^{1,2}$ and G. Ceder $^{1,*}$

$^{1}$ Department of Materials Science and Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA
$^{2}$ Center for Nanoscale Materials, Argonne National Laboratory, Argonne, Illinois 60439, USA

(Received 24 January 2011; revised manuscript received 7 March 2011; published 1 June 2011)

The ability to predict a semiconductor's band edge positions in solution is important for the design of water-splitting photocatalyst materials. In this paper, we introduce a first-principles method to compute the conduction-band minima of semiconductors relative to the water $H_2O/H_2$ level using density functional theory with semilocal functionals and classical molecular dynamics. We test the method on six well known photocatalyst materials: $TiO_2$, $WO_3$, CdS, ZnSe, GaAs, and GaP. The predicted band edge positions are within 0.34 eV of the experimental data, with a mean absolute error of 0.19 eV.

DOI: 10.1103/PhysRevB.83.235301
PACS number(s): 73.20.At, 71.20.Nr, 31.15.A−, 73.40.Mr

## I. INTRODUCTION

Since the discovery of the first photocatalytic water splitting system based on $TiO_2$ and Pt in 1972 by Fujishima and Honda, $^{1,2}$ the photocatalysis of water splitting has become an active research area and a promising way to capture and store energy from the sun.

In the design of photocatalysts for water splitting, the primary objective is to find materials that can achieve the commercially viable 10% quantum efficiency for hydrogen evolution $^{3}$ upon solar illumination and without bias voltage. Meanwhile, catalyst materials should remain long-term stable in the aqueous electrolyte.

For the past three decades, over 130 inorganic materials have been experimentally discovered as photocatalysts for water splitting, but the highest quantum efficiency under visible light remains below $2.5\%^{3}$ One primary reason for the low quantum efficiency is the fact that the smallest band gap of existing photocatalysts, which enable the water-splitting reaction without a bias voltage, is $2.3\ eV,^{3}$ while the optimal range of band gap for utilizing the solar spectrum is $1.1-1.7\ eV.^{4}$ However, 2.3 eV is still well above the theoretical energy requirement to split water, which is $1.23\ eV.^{3}$ Thus, in principle, it is possible to find photocatalysts that require no bias voltage and have band gaps smaller than currently known photocatalysts so that the quantum efficiency can be improved.

Apart from an appropriate band gap, one crucial requirement for a water-splitting photocatalyst material is that its conduction-band minimum (CBM) must be more negative than the $H_2O/H_2$ level of water and its valence-band maximum (VBM) must be more positive than the $H_2O/O_2$ level of water (see Fig. 1). This requirement ensures that the water-splitting reaction is energetically favorable without a bias voltage. Therefore, the knowledge of a semiconductor's CBM and VBM band edge positions, relative to the $H_2O/H_2$ level and the $H_2O/O_2$ level in water, respectively, is important for the design of a water-splitting photocatalyst. $^{5,6}$ An $ab$ initio approach to obtain such band edge positions is important as it can be used as a scalable approach to investigate a large number of possible materials.

A straightforward attempt for this purpose is to compute both band edge positions of semiconductors and water redox levels, relate them to a common reference, and then calculate their difference. The vacuum level is a natural candidate for the common reference. The band levels of semiconductors and the water redox levels relative to the vacuum level have been computed using DFT in 7 and 8, respectively. However, the problem comes from the fact that the band realignment at a semiconductor-water interface is not equal to the difference between the band realignment at the semiconductor-vacuum and water-vacuum surfaces. This difficulty is explained in Ref. 9 for the metal-semiconductor interfacial system. The main reason is that the dipole at metal-semiconductor interface is not equal to the difference between the surface dipoles at the metal-vacuum and semiconductor-vacuum surfaces. For the semiconductor-water interfacial system, we will show later in the Discussion section that the error due to this problem is up to 0.7 eV. Apart from this approach, a few other computational methods have also been proposed in the literature. In Van de Walle's work, $^{10}$ hydrogen levels in semiconductors and insulators have been aligned by a valence-band offset method. $^{11,12}$ However, this method also avoids directly dealing with a semiconductor-water interface system and thus may have band alignment problems similar to those of the vacuum reference method. Very recently, Cheng and Sprik compute the band edge positions of $TiO_2$ relative to water redox levels $^{13}$ using the generalized gradient approximation (GGA) and $ab$ initio molecular dynamics (MD). This method deals directly with the

![](./images/811656241209147393_1.jpg)

FIG. 1. (Color online) A schematic diagram of possible band level arrangements for water-splitting photocatalysts. (a) Favorable band level arrangement; (b) unfavorable VBM position; (c) unfavorable CBM position.

---

1098-0121/2011/83(23)/235301(7)
235301-1
©2011 American Physical Society

![](./images/811656241209147393_2.jpg)

FIG. 2. A schematic diagram of the band alignment at the semiconductor-water interface. $E_{C_{bulk}}$ = CBM in the bulk of the semiconductor, $E_{C_{edge}}$ = CBM at the semiconductor-solution interface, $A_{bulk}$ = acceptor level ($\text{H}_2\text{O}/\text{H}_2$ level of liquid water in this work) in the bulk of the solution, $A_{edge}$ = acceptor level at the semiconductor-solution interface, $H_{semi\_bulk}$ = Hartree potential in the semiconductor bulk, $H_{semi\_edge}$ = Hartree potential on the semiconductor side at the semiconductor-solution interface, $H_{sol\_bulk}$ = Hartree potential in the bulk of the solution, and $H_{sol\_edge}$ = Hartree potential on the solution side at the semiconductor-solution interface.

semiconductor-water system and can be generalized to other inorganic semiconductors. The errors for TiO₂'s CBM and VBM positions found in this work were substantial, at, respectively, 0.4 and 1.6 eV. They argue that the error may come from the simplified assumption that the zero-point energy (ZPE) of a proton in a solvated $\text{H}_3\text{O}^+$ ion can be approximated by the net ZPE of a dummy proton in an isolated pseudo-$\text{H}_3\text{O}$ molecule, a molecule with the same atomic configuration as an isolated $\text{H}_3\text{O}^+$ ion but with neutral charge.¹⁴ Since the ZPE is directly added to their results and is as large as 0.5 eV, the assumption may introduce significant errors.

The purpose of this paper is to introduce a first-principles method for computing a semiconductor's conduction-band edge position relative to the $\text{H}_2\text{O}/\text{H}_2$ level in liquid water. This method has the following advantages:
(i) It is applicable for general inorganic semiconductors.
(ii) It deals directly with band realignment effects introduced by the semiconductor-water interface.
(iii) It is mainly based on total energy calculations using DFT-GGA, with reasonably low computation cost.

An approach for the computation of band edge alignments across a solid-solid interface has previously been developed. The band alignment between two semiconductors,¹⁵,¹⁶ and the Schottky barrier heights between a semiconductor and a metal¹⁷ are typically computed with DFT by a three-step method: two bulk calculations to compute the difference between the desired energy level (CBM, VBM, or Fermi energy) and the average Hartree potential of each solid, and an interfacial slab computation to compute the Hartree potential difference between the two solids.

There are several challenges when replacing one solid system by liquid water. Since liquid water lacks periodicity, and ab initio MD can produce considerable errors for water,¹⁸,¹⁹ it is nontrivial to construct a cell with accurately representative atomic configurations of liquid water in DFT. Instead, we use the idea proposed in Ref. 20 and equilibrate a classical MD computation of water at room temperature. Snapshots of the water configuration at different MD time points are then computed with DFT.

By combining the three-step method and the idea of using snapshots of classical MD water configurations for DFT, we develop a method for computing CBM band edge position relative to the water $\text{H}_2\text{O}/\text{H}_2$ level. In the next sections, we introduce our methodology in detail, and present the computational results obtained with this approach for six common water-splitting photocatalyst materials: TiO₂, WO₃, CdS, ZnSe, GaAs, and GaP. Finally, we compare the computational results to experimental data.

## II. METHODOLOGY

Figure 2 shows a schematic diagram of band alignments at an interface, and introduces the terminology we will be using. Our objective is to compute the CBM band edge position relative to the solution acceptor level ($\text{H}_2\text{O}/\text{H}_2$ level of liquid water in this work) at the interface, i.e., $E_{C_{edge}} - A_{edge}$. We assume that the band alignment is due to electrostatic effects (electron and ion redistribution near the interface due to Fermi energy realignment). So the energy levels and Hartree potential change by the same amount everywhere in space and their

TABLE I. Crystal structure information for test materials.

<table>
<thead>
<tr>
<th>Semiconductor</th>
<th>TiO₂</th>
<th>WO₃</th>
<th>CdS</th>
<th>ZnSe</th>
<th>GaAs</th>
<th>GaP</th>
</tr>
<tr>
<th>Crystal type</th>
<th>Rutile (tetragonal)</th>
<th>Tetragonal</th>
<th>Wurtzite (hexagonal)</th>
<th>Zinc blende (cubic)</th>
<th>Zinc blende (cubic)</th>
<th>Zinc blende (cubic)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Space group number</td>
<td>136</td>
<td>113</td>
<td>186</td>
<td>216</td>
<td>216</td>
<td>216</td>
</tr>
<tr>
<td>Space group name</td>
<td>$P42/mnm$</td>
<td>$P421m$</td>
<td>$P63mc$</td>
<td>$F43m$</td>
<td>$F43m$</td>
<td>$F43m$</td>
</tr>
<tr>
<td>Initial lattice</td>
<td>$a=4.598$</td>
<td>$a=7.616$</td>
<td>$a=4.137$</td>
<td>$a=5.670$</td>
<td>$a=5.654$</td>
<td>$a=5.447$</td>
</tr>
<tr>
<td>parameters (Å)</td>
<td>$b=4.598$</td>
<td>$b=7.616$</td>
<td>$b=4.137$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$c=2.956$</td>
<td>$c=3.960$</td>
<td>$c=6.714$</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/811656241209147393_3.jpg)

FIG. 3. Total DOS plots for (a) a $128$ H₂O molecules liquid system with MD atomic configurations at $t=50$ ps without DFT relaxation, with a band gap of 3.76 eV; (b) a $128$ H₂O molecules liquid system with MD atomic configurations at $t=100$ ps without DFT relaxation, with a band gap of 3.89 eV; (c) a $128$ H₂O molecules liquid system with MD atomic configurations at $t=100$ ps with DFT relaxations, with a band gap of 3.89 eV. $E_v$ is the VBM energy.

difference remains unchanged. Thus, we can use the following relations:

$$
E_{C_{\text{edge}}}-H_{\text{semi\_edge}}=E_{C_{\text{bulk}}}-H_{\text{semi\_bulk}},\tag{1}
$$

$$
A_{\text{edge}}-H_{\text{sol\_edge}}=A_{\text{bulk}}-H_{\text{sol\_bulk}}.\tag{2}
$$

<table>
<caption>TABLE II. Values of $E_{C_{\text{bulk}}}-H_{\text{semi\_bulk}}$ from semiconductor bulk computations.</caption>
<thead>
<tr>
<th>Testing semiconductor</th>
<th>TiO₂</th>
<th>WO₃</th>
<th>CdS</th>
<th>ZnSe</th>
<th>GaAs</th>
<th>GaP</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E_{C_{\text{bulk}}}-H_{\text{semi\_bulk}}$ (eV)</td>
<td>3.77</td>
<td>1.89</td>
<td>2.91</td>
<td>3.25</td>
<td>3.64</td>
<td>4.08</td>
</tr>
</tbody>
</table>

Therefore, the term $E_{C_{\text{edge}}}-A_{\text{edge}}$ can be computed by

$$
\begin{align*}
E_{C_{\text{edge}}}-A_{\text{edge}}&=\left(E_{C_{\text{edge}}}-H_{\text{semi\_edge}}\right)-\left(A_{\text{edge}}-H_{\text{sol\_edge}}\right)\\
&\quad+\left(H_{\text{semi\_edge}}-H_{\text{sol\_edge}}\right)\\
&=\left(E_{C_{\text{bulk}}}-H_{\text{semi\_bulk}}\right)-\left(A_{\text{bulk}}-H_{\text{sol\_bulk}}\right)\\
&\quad+\left(H_{\text{semi\_edge}}-H_{\text{sol\_edge}}\right).\tag{3}
\end{align*}
$$

Equation (3) indicates that the term $E_{C_{\text{edge}}}-A_{\text{edge}}$ can be obtained by the following three-step method. Step 1: compute the term $E_{C_{\text{bulk}}}-H_{\text{semi\_bulk}}$, i.e., the eigenvalue of the lowest unoccupied eigenstate relative to the average Hartree potential, in a bulk semiconductor system. Step 2: compute the term $A_{\text{bulk}}-H_{\text{sol\_bulk}}$, i.e., the eigenvalue of the molecular acceptor level relative to the average Hartree potential, in a bulk liquid water system. This is nontrivial and we adopt the idea of using MD atomic configurations for DFT. More details will be introduced in Sec. III B. Step 3: compute the term $H_{\text{semi\_edge}}-H_{\text{sol\_edge}}$, i.e., the difference in average Hartree potentials between the semiconductor versus the liquid water, in a semiconductor-water interfacial slab system. During step 3, we join the bulk cells that we compute in steps 1 and 2 and make a supercell that contains the interface. In this supercell, we compute the variation of the Hartree potential with position. By averaging the Hartree potential on both the semiconductor side and the liquid water side, we calculate $H_{\text{semi\_edge}}-H_{\text{sol\_edge}}$.

This method has two key features. One is that it includes the band realignment effect yet avoids a large supercell computation. The band realignment effect at the semiconductor-water

![](./images/811656241209147393_4.jpg)

FIG. 4. (Color online) DOS plots for a $127$H₂O + H₃O⁺ liquid system. The black solid line is the total DOS while the red dashed line is the projected DOS from the H₃O⁺ ion in this system. We enlarged the H₃O⁺ DOS 30 times to make it visible on the scale of the total DOS. The DOS peak at approximately 2.0 eV represents the LUMO of the system contributed by the H₃O⁺ ion. $E_v$ is the VBM energy.

![](./images/811656241209147393_5.jpg)

FIG. 5. (Color online) Calculated Hartree potential profile of a stoichiometric TiO₂-water slab system. The vertical green dashed line indicates the interface. The left side is semiconductor TiO₂ and the right side is water. The black solid line is the planar-averaged Hartree potential as a function of cell dimension normal to the interface. The red dashed line with square markers indicates the planar-averaged Hartree potential of TiO₂, $H_{\text{semi\_edge}}$. The blue dashed line with circular markers indicates the planar-averaged Hartree potential of liquid water, $H_{\text{sol\_edge}}$.

interface is important for computing the relative energy levels. However, it usually occurs over a distance of $100\ \mathring{\text{A}}$ to several micrometers from the interface.²⁰ As a consequence, directly computing the band alignment effect, i.e., the term $E_{C_{\text{edge}}} - E_{C_{\text{bulk}}}$ (or $A_{\text{edge}} - A_{\text{bulk}}$), in a single slab computation is not applicable, since it requires a prohibitively large supercell to converge both $E_{C_{\text{edge}}}(A_{\text{edge}})$ and $E_{C_{\text{bulk}}}(A_{\text{bulk}})$ in the same system. On the other hand, in the three-step method, the three objective terms $E_{C_{\text{bulk}}} - H_{\text{semi\_bulk}}$, $A_{\text{bulk}} - H_{\text{sol\_bulk}}$, and $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$ are either pure bulk properties or pure interface properties, so a large supercell is not required. In this approach, the band realignment effect is captured by the computation of $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$. And the longest dimension of the supercell required to converge $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$ to 0.1 eV is typically 30–40 $\mathring{\text{A}}$. The other important feature is that the three-step method only requires the Hartree potential in the interfacial slab computation but not any energy eigenvalues. This prevents the complicated problem of trying to assign electronic states to specific real-space domains of the supercell.

### III. COMPUTATIONAL DETAILS AND RESULTS

To test our approach, we select six popular photocatalyst materials: TiO₂, WO₃, CdS, ZnSe, GaAs, and GaP. The details of their crystal structures are listed in Table I.

We applied the method described in Sec. II on these materials to compute their CBM position relative to the H₂O/H₂ level in liquid water, $E_{C_{\text{edge}}} - A_{\text{edge}}$. The computational results are compared to experimental data obtained from Refs. 21 and 22. All DFT computations²³,²⁴ are performed with projector augmented wave (PAW)²⁵ potentials using the plane-wave code Vienna Ab-initio Simulation Package (VASP).²⁶,²⁷ We use the Perdew-Burke-Ernzerhof (PBE)²⁸ GGA exchange-correlation functional unless specified otherwise.

### A. Semiconductor bulk computation

To implement step 1 in Sec. II, we compute the bulk CBM relative to the average Hartree potential for each selected material in this section. For every material, we optimize the volume, cell shape, and atomic positions of the unit cell with a Monkhorst-Pack²⁹ $6 \times 6 \times 6$ $k$-point grid and plane-wave energy cutoff of 500 eV. On the optimized structures, we perform static DFT computations using a fine $\Gamma$-centered 10 $\times$ 10 $\times$ 10 $k$-point grid to compute the CBM. We also plot the Hartree potential and determine a macroscopic average over the unit cell for every material. The resulting average Hartree potential $H_{\text{semi\_bulk}}$ is zero. This is consistent with the fact that the absolute Hartree potential in an infinite periodic system is customarily set to zero in DFT codes including VASP. The results of $E_{C_{\text{bulk}}} - H_{\text{semi\_bulk}}$ are shown in Table II.

### B. Liquid water bulk computation

Step 2 in Sec. II consists of determining the H₂O/H₂ acceptor level relative to the Hartree potential in bulk liquid water. To prepare the water atomic configurations in DFT, we perform a classical MD computation by DLPOLY³⁰ and use the TIP4P³¹ potential to describe the interaction between water molecules. A water system of 128 H₂O molecules is initially equilibrated at 300 K with a relaxed cell size of $18\ \mathring{\text{A}} \times 15.6\ \mathring{\text{A}} \times 14.6\ \mathring{\text{A}}$. At the same temperature, we further perform an $NVT$ MD simulation for 100 ps and take snapshots of the atomic configurations of this TIP4P water system at $t=50$ and 100 ps. We construct two DFT cells using these two configurations.

Before proceeding, we perform two tests to verify that atomic configurations from classical MD produce consistent results in terms of DFT electronic structures. Only the $\Gamma$ $k$ point is used in the DFT calculations of liquid water cells. First, we compute the band gap and plot in Figs. 3(a) and 3(b) the density of state (DOS) by DFT using each of the two cells obtained at different MD time points without any further DFT ionic relaxations. The similar band-gap values (3.76 and 3.89 eV) and similar DOS plots between Figs. 3(a) and 3(b) indicate that the atomic configurations taken from different time points of classical MD have little difference on the DFT electronic structures. Second, we repeat the process but with

TABLE III. Values of $A_{\text{bulk}} - H_{\text{sol\_bulk}}$ from liquid water bulk computations.
<table>
<thead>
<tr>
<th>Replaced H₂O molecule</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
</tr>
</thead>
<tbody>
<tr>
<td>$A_{\text{bulk}} - H_{\text{sol\_bulk}}$ (eV)</td>
<td>−0.70</td>
<td>−0.65</td>
<td>−0.62</td>
<td>−0.75</td>
</tr>
<tr>
<td>Total energy (eV)</td>
<td>−1788.2</td>
<td>−1788.1</td>
<td>−1787.5</td>
<td>−1787.7</td>
</tr>
</tbody>
</table>

TABLE IV. Values of $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$ from interfacial slab computations.
<table>
<thead>
<tr>
<th>Testing semiconductor</th>
<th>TiO₂</th>
<th>WO₃</th>
<th>CdS</th>
<th>ZnSe</th>
<th>GaAs</th>
<th>GaP</th>
</tr>
</thead>
<tbody>
<tr>
<td>$H_{\text{semi\_edge}}$</td>
<td>−2.00</td>
<td>−1.11</td>
<td>−1.02</td>
<td>−1.05</td>
<td>−1.41</td>
<td>−1.56</td>
</tr>
<tr>
<td>$H_{\text{sol\_edge}}$</td>
<td>2.48</td>
<td>2.02</td>
<td>1.33</td>
<td>1.30</td>
<td>1.86</td>
<td>1.93</td>
</tr>
<tr>
<td>$H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$</td>
<td>−4.48</td>
<td>−3.13</td>
<td>−2.35</td>
<td>−2.35</td>
<td>−3.27</td>
<td>−3.49</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE V. Computational results of $E_{C_{\text{edge}}} - A_{\text{edge}}$ and comparison with experimental data. The experimental data are translated from $V_{\text{NHE}}$, the value reference to the normal hydrogen electrode (NHE), to $E_{C_{\text{edge}}} - A_{\text{edge}}$ by using $E_{C_{\text{edge}}} - A_{\text{edge}} = -e \times V_{\text{NHE}}$.
</caption>
<tbody><tr><td>Test semiconductor</td><td>TiO₂</td><td>WO₃</td><td>CdS</td><td>ZnSe</td><td>GaAs</td><td>GaP</td></tr>
<tr><td>$E_{C_{\text{edge}}} - A_{\text{edge}}$ (eV)</td><td>−0.01</td><td>−0.54</td><td>1.27</td><td>1.60</td><td>1.07</td><td>1.29</td></tr>
<tr><td>$-e \times V_{\text{NHE}}$ (experimental, eV)</td><td>0.00</td><td>−0.20</td><td>1.50</td><td>1.50</td><td>0.80</td><td>1.10</td></tr>
</tbody></table>

full DFT ionic relaxations (cell volume, cell shape, and atomic positions) for the $t = 100$ ps configuration, and the resulting DOS is shown in Fig. 3(c). The identical band-gap values and similar DOS plots between Figs. 3(b) and 3(c) indicate that DFT ionic relaxations do not alter the electronic structures after the liquid water system reaches equilibrium in classical MD. In addition, all DOS plots in Figs. 3(a), 3(b), and 3(c) are very similar to the DOS plots of liquid water in Ref. 20, which implies that the $\Gamma$ $k$ point alone is sufficient to give results consistent with previous work.

To compute the term $A_{\text{bulk}} - H_{\text{sol\_bulk}}$, we need to compute the lowest unoccupied molecular orbit (LUMO) level of water because this level is recognized as the acceptor level of water. While the acceptor is nominally the proton (H⁺), in an aqueous environment the H⁺ is solvated in multiple $\text{H}^+(\text{H}_2\text{O})_n$ configurations.³² The hydronium ion $\text{H}_3\text{O}^+$, being the simplest, is especially important for computing the acceptor level in a water system. We simulated the hydronium ion in water by fully relaxing an isolated $\text{H}_3\text{O}^+$ ion in DFT and then replacing one of the 128 $\text{H}_2\text{O}$ molecules in the liquid water system with this $\text{H}_3\text{O}^+$ ion. The O atom of the $\text{H}_3\text{O}^+$ is placed in exactly the same position as the O atom of the replaced $\text{H}_2\text{O}$ molecule. The orientation of the added $\text{H}_3\text{O}^+$ ion is randomized. We perform further DFT relaxation for this added $\text{H}_3\text{O}^+$ ion to optimize the atomic positions and orientation in the water system. A static DFT computation then follows to compute the energy levels of this $127\text{H}_2\text{O} + \text{H}_3\text{O}^+$ system. The DOS plot of such a system is shown in Fig. 4, which indicates that a level attributed to $\text{H}_3\text{O}^+$ is indeed the LUMO. We repeat the above process several times but replace a different $\text{H}_2\text{O}$ molecule with $\text{H}_3\text{O}^+$ to ensure that our results are not affected by the positions of the $\text{H}_3\text{O}^+$ ions in the system. The results are shown in Table III.

Table III indicates that the fluctuation in $A_{\text{bulk}} - H_{\text{sol\_bulk}}$ due to the position of $\text{H}_3\text{O}^+$ ion in the cell is less than 0.1 eV. We will use $A_{\text{bulk}} - H_{\text{sol\_bulk}} = -0.70$ eV in subsequent calculation since it corresponds to the lowest total energy among all four systems.

### C. Semiconductor-water interface computation

This section describes how the semiconductor-water interface calculation (step 3 in Sec. II) is implemented. We aim to compute the Hartree potential difference between the semiconductor bulk cell and the liquid water cell in an interfacial slab system. The interfacial cell is constructed by joining several layers of the semiconductor bulk cells in Sec. III A and the liquid water cell in Sec. III B together. For each semiconductor, we perform a convergence test in that we increase the number of layers of semiconductor cells until the Hartree potential difference between the semiconductor side and liquid water side is converged to 0.1 eV. The converged Hartree potential profile along the slab direction for TiO₂ is shown in Fig. 5 as an example. The calculated value of $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$ for each test compound is listed in Table IV. Only the $\Gamma$ $k$ point is used for these DFT computations.

![](./images/811656241209147393_6.jpg)

FIG. 6. (Color online) CBM band edge level results referenced to the NHE. Blue lines are computational results by the method in this paper. Red lines are experimental data from Refs. 21 and 22. Two dotted lines indicate the $\text{H}_2\text{O/H}_2$ and $\text{H}_2\text{O/O}_2$ levels in water.

### D. Results of conduction-band-edge positions relative to water H₂O/H₂ level

By substituting the terms $E_{C_{\text{bulk}}} - H_{\text{semi\_bulk}}$, $A_{\text{bulk}} - H_{\text{sol\_bulk}}$, and $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$ into Eq. (3), we obtain the CBM band edge position results relative to water $\text{H}_2\text{O/H}_2$ level: $E_{C_{\text{edge}}} - A_{\text{edge}}$. In Table V, we compare the computed results with experimental data in a $\text{pH} = 1$ electrolyte from Refs. 21 and 22. Note that our system is a $127\text{H}_2\text{O} + \text{H}_3\text{O}^+$ system, so it is comparable to the $\text{pH} = 1$ electrolyte in terms of H⁺ concentration. Figure 6 is plotted from the data in Table V and shows more directly the relationship between computed $E_{C_{\text{edge}}} - A_{\text{edge}}$ and experimental data.

---

## IV. DISCUSSION

From both Fig. 6 and Table V, we see that our computational results are consistent with experimental data. The WO₃ system shows the largest error. To test whether this error is related to the $d$ character of WO₃'s CBM, we repeat the computations for

<table>
<caption>TABLE VI. Computational results of $E_{C_{\text{edge}}} - A_{\text{edge}}$ using $\text{GGA} + U$ for WO₃.
</caption>
<tbody><tr><td></td><td>$E_{C_{\text{bulk}}} - H_{\text{semi\_bulk}}$</td><td>$A_{\text{bulk}} - H_{\text{sol\_bulk}}$</td><td>$H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$</td><td>$E_{C_{\text{edge}}} - A_{\text{edge}}$</td></tr>
<tr><td>WO₃ (eV)</td><td>2.35</td><td>−0.70</td><td>−3.39</td><td>−0.34</td></tr>
</tbody></table>

<table>
<caption>TABLE VII. Result of $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$ by the vacuum common reference approach.</caption>
<tbody>
<tr>
<td>
</td>
<td>
$H_{\text{semi\_edge}} - H_{\text{vacuum\_edge}}$
</td>
<td>
$H_{\text{sol\_edge}} - H_{\text{vacuum\_edge}}$
</td>
<td>
$(H_{\text{semi\_edge}} - H_{\text{sol\_edge}})_{\text{vacuum\_approach}}$
</td>
</tr>
<tr>
<td>
GaP (eV)
</td>
<td>
$-7.82$
</td>
<td>
$-3.64$
</td>
<td>
$-4.18$
</td>
</tr>
</tbody>
</table>

$\text{WO}_3$ using the $\text{GGA} + U$ approximation$^{33}$ with $U = 2.0$ for the $d$ orbitals of $W$. The result, shown in Table VI, indicates that $E_{C_{\text{edge}}} - A_{\text{edge}}$ changes from $-0.54$ to $-0.34$ eV after applying the $+U$ correction and shows better agreement with the experimental value of $-0.20$ eV.

As is well known, DFT in the GGA gives large errors for band gaps. However, our results for $E_{C_{\text{edge}}} - A_{\text{edge}}$ in Table V give an average error of 0.19 eV. We believe that the electronic level difference is in better agreement with experiment than the band gap primarily due to two reasons. One is that the computational error for band gaps comes from both CBM and VBM computations while our approach does not involve VBM computation, so that our results do not have the error from computing VBM. The other reason is that, in our approach, we are computing the energy difference between CBM and LUMO, two unoccupied energy levels. They are both typically underestimated in semilocal functionals.$^{34}$ Therefore, error cancellation may occur in their difference.

Our approach can be generalized to also compute the VBM band edge position relative to the $\text{H}_2\text{O/O}_2$ level in water. However, this may not be necessary if one has an accurate way of computing the band gap of the semiconductor, for example using the $GW$ approximation,$^{35}$ hybrid or screened hybrid functionals,$^{36-40}$ or the $\Delta\text{-sol}^{41}$ method. We can then determine the VBM from the CBM band edge position and the band gap.

We also demonstrate here that the relative band edge position at a semiconductor-water interface cannot be computed by the vacuum reference approach. We take GaP as an example. By using the same approach as in Sec. III C, we respectively compute the Hartree potential difference at the GaP-vacuum surface and the water-vacuum surface, and denoted them as $H_{\text{semi\_edge}} - H_{\text{vacuum\_edge}}$ and $H_{\text{sol\_edge}} - H_{\text{vacuum\_edge}}$ in Table VII. By subtracting them, we obtain $(H_{\text{semi\_edge}} - H_{\text{sol\_edge}})_{\text{vacuum\_approach}}$, the Hartree potential difference at the GaP-water interface by the vacuum reference method. The result is $-4.18$ eV (see Table VII). The directly computed value of $H_{\text{semi\_edge}} - H_{\text{sol\_edge}}$ for the GaP-water interfacial system is $-3.49$ eV (see Table IV). The discrepancy of the two results indicates that the vacuum reference approach is not valid.

## V. CONCLUSION

In this paper, we present a method for computing CBM band edge positions relative to the water $\text{H}_2\text{O/H}_2$ level. The method is computationally efficient since it only involves DFT calculations with a semilocal functional. The average error, over the six compounds tested, is 0.19 eV, which makes this method useful for predicting and designing photocatalyst materials. This method and an accurate band-gap DFT computation method together may provide improved knowledge of the energy levels and band gap for any photocatalyst material and can hopefully be used to design materials with little bias voltage for the splitting of water. Moreover, for an arbitrary photocatalyst material, this method can tell us how large the external bias voltage should be applied to trigger hydrogen evolution. This information is both an important reference for experimentalists and a clue for evaluating the stability in the electrolyte of the materials.

## ACKNOWLEDGMENTS

This work was supported by Eni S.p.A. under the Eni-MIT Alliance Solar Frontiers Program, the Chesonis Family Foundation under the Solar Revolution Project, and the National Science Foundation through TeraGrid resources provided by the Pittsburgh Supercomputing Center and Texas Advanced Computing Center under Grant No. TG-DMR970008S. We are grateful to Oliviero Andreussi for his help in our classical MD computation. Helpful discussions with Jeff Grossman, ShinYoung Kang, Ruoshi Sun, Rickard Armiento, and Predrag Lazic are kindly acknowledged.

$^{*}$Author to whom all correspondence should be addressed: gceder@mit.edu

$^{1}$A. Fujishima and K. Honda, *Nature* (London) **238**, 37 (1972).

$^{2}$A. Fujishima and K. Honda, *Bull. Chem. Soc. Jpn.* **44**, 1148 (1971).

$^{3}$F. E. Osterloh, *Chem. Mater.* **20**, 35 (2008).

$^{4}$A. Goetzberger, C. Hebling, and H. W. Schock, *Mater. Sci. Eng., R* **40**, 1 (2003).

$^{5}$M. Grätzel, *Nature* (London) **414**, 338 (2001).

$^{6}$A. Fujishima, X. Zhang, and D. A. Tryk, *Surf. Sci. Rep.* **63**, 515 (2008).

$^{7}$F. D. Angelis, S. Fantacci, and A. Selloni, *Nanotechnology* **19**, 424002 (2008).

$^{8}$J. V. Coe *et al.*, *J. Chem. Phys.* **107**, 6023 (1997).

$^{9}$E. H. Rhoderick, *Solid-State Electron Dev., IEE Proc. I* **129**, 1 (1982).

$^{10}$C. G. Van de Walle and J. Neugebauer, *Nature* (London) **423**, 5 (2003).

$^{11}$A. Franciosi and C. G. Van de Walle, *Surf. Sci. Rep.* **25**, 1 (1996).

$^{12}$J. A. Majewski, M. Städele, and P. Vogl, *Mat. Res. Soc. Symp. Proc.* **449**, 917 (1997).

$^{13}$J. Cheng and M. Sprik, *Phys. Rev. B* **82**, 081406 (2010).

$^{14}$J. Cheng, M. Sulpizi, and M. Sprik, J. Chem. Phys. **131**, 154504 (2009).

$^{15}$R. Shaltaf, G. M. Rignanese, X. Gonze, F. Giustino, and A. Pasquarello, Phys. Rev. Lett. **100**, 186401 (2008).

$^{16}$A. Alkauskas, P. Broqvist, F. Devynck, and A. Pasquarello, Phys. Rev. Lett. **101**, 106802 (2008).

$^{17}$M. Mrovec, J. M. Albina, B. Meyer, and C. Elsässer, Phys. Rev. B **79**, 245121 (2009).

$^{18}$J. C. Grossman, E. Schwegler, E. W. Draeger, F. Gygi, and G. Galli, J. Chem. Phys. **120**, 1 (2004).

$^{19}$E. Schwegler, J. C. Grossman, F. Gygi, and G. Galli, J. Chem. Phys. **121**, 15 (2004).

$^{20}$D. Prendergast, J. C. Grossman, and G. Galli, J. Chem. Phys. **123**, 014501 (2005).

$^{21}$J. Nozik and R. Memming, J. Phys. Chem. **100**, 13061 (1996).

$^{22}$J. Nozik, Annu. Rev. Phys. Chem. **29**, 189 (1978).

$^{23}$P. Hohenberg and W. Kohn, Phys. Rev. **136**, B864 (1964).

$^{24}$W. Kohn and L. J. Sham, Phys. Rev. **140**, A1133 (1965).

$^{25}$P. E. Blöchl, Phys. Rev. B **50**, 17953 (1994).

$^{26}$G. Kresse and J. Furthmuller, Phys. Rev. B **54**, 11169 (1996).

$^{27}$G. Kresse and D. Joubert, Phys. Rev. B **59**, 1758 (1999).

$^{28}$J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

$^{29}$H. J. Monkhorst and J. D. Pack, Phys. Rev. B **13**, 5188 (1976).

$^{30}$W. Smith and T. R. Forester, J. Mol. Graph. **14**, 136 (1996).

$^{31}$W. L. Jorgensen, J. Chandrasekhar, J. D. Madura, R. W. Impey, and W. L. Klein, J. Chem. Phys. **79**, 926 (1983).

$^{32}$J. M. Hermida-Ramón and G. Karlström, J. Mol. Struct.: THEOCHEM **712**, 167 (2004).

$^{33}$S. L. Dudarev, G. A. Botton, S. Y Savrasov, C. J. Humphreys, and A. P. Sutton, Phys. Rev. B **57**, 1505 (1998).

$^{34}$H. P. Komsa, P. Broqvist, and A. Pasquarello, Phys. Rev. B **81**, 205118 (2010).

$^{35}$L. Hedin, Phys. Rev. **139**, A796 (1965).

$^{36}$A. D. Becke, J. Chem. Phys. **98**, 5648 (1993).

$^{37}$C. Lee, W. Yang, and R. G. Parr, Phys. Rev. B **37**, 785 (1988).

$^{38}$J. P. Perdew, M. Ernzerhof, and K. Burke, J. Chem. Phys. **105**, 9982 (1996).

$^{39}$J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. **118**, 8207 (2003).

$^{40}$A. V. Krukau, O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, J. Chem. Phys. **125**, 224106 (2006).

$^{41}$M. K. Y. Chan and G. Ceder, Phys. Rev. Lett. **105**, 196403 (2010).