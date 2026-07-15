![](./images/812398974567710721_1.jpg)

Available online at www.sciencedirect.com
![](./images/812398974567710721_2.jpg)

Applied Surface Science 219 (2003) 47-55

![](./images/812398974567710721_3.jpg)

# Theoretical description of the interdiffusion of Al in the U-Mo solid solution

Jorge E. Garcés$^{a,b}$, Armando C. Marino$^{a}$, Guillermo Bozzolo$^{b,c,*}$

$^{a}$Centro Atómico Bariloche, 8400 Bariloche, Argentina
$^{b}$Ohio Aerospace Institute, 22800 Cedar Point Road, Cleveland, OH 44142, USA
$^{c}$NASA Glenn Research Center, Mail Stop 23-2, 21000 Brookpark Road, Cleveland, OH 44135, USA

Received 21 August 2002; accepted 10 December 2002

## Abstract
The Bozzolo-Ferrante-Smith (BFS) method for alloys was applied to the analysis of Al interdiffusion in the U-Mo solid solution system as a function of Mo concentration. The binary Al/U and Al/Mo systems show opposite behavior, which in the ternary case Al/U-Mo, translates into the role of regions rich in Mo acting as interdiffusion barriers to Al, in excellent agreement with experimental evidence.
© 2003 Elsevier Science B.V. All rights reserved.

Keywords: Adatoms; Alloys; Computer simulations; Uranium; Molybdenum; Aluminum; Semi-empirical methods and model calculations; Single crystal surfaces; Surface structure

## 1. Introduction

In recent years, the development of low enrichment uranium fuel has been a subject of interest for many researchers from different experimental fields. The development of high density U-alloys with an increased concentration of U is one of the key problems for developing high neutron flux research reactors with low enrichment uranium fuel [1]. The U-Mo alloy system is one of the prospective candidates because a solid solution of Mo in bcc $\gamma$-U has acceptable irradiation properties for reactor fuels. The prospect of using a U-Mo alloy as a reactor fuel is closely connected with the possibility of retaining a metastable $\gamma$ phase state in alloys at temperatures below $560\ ^{\circ}\text{C}$ during fuel element fabrication and irradiation. The reactor fuel consists of atomized U-Mo particles dispersed in an aluminum matrix. Interdiffusion or interfacial reaction, which affects the performance of nuclear fuel materials, is observed in the U-Mo/Al composites for low Mo composition. The experimental results show a large volume increase (26%) for U-2 wt.% Mo/Al mainly due to the formation of voids and cracks resulting from nearly complete interdiffusion or an interfacial reaction with uranium aluminide formation. However, no significant dimensional changes are observed in the U-10 wt.% Mo/Al system. This difference in behavior can be understood if it is assumed that Mo atoms supersaturated at the grain boundaries inhibit the diffusion of aluminum atoms [2].

From the theoretical standpoint, the description of actinide metals and their alloys poses a severe challenge to the modern electronic-structure theory [3] and

*Corresponding author. Tel.: +1-216-4335824;
fax: +1-216-4335170.
E-mail address: guillermo.h.bozzolo@grc.nasa.gov (G. Bozzolo).

0169-4332/$ - see front matter © 2003 Elsevier Science B.V. All rights reserved.
doi:10.1016/S0169-4332(03)00631-7

has eluded accurate treatment by semi-empirical or quantum approximate methods. As a consequence, theoretical modeling efforts to describe the complex behavior observed experimentally in these systems have been limited, both in number and scope. How- ever, recently developed computational methods have become a viable tool to assist in alloy development programs. While first-principles approaches provide the most accurate framework for such studies, the complexity of the problems at hand and their substantial computational requirements impose lim- itations that still prevent these approaches from becoming economical predictive tools. On the other hand, recent developments in the area of quantum approximate methods have contributed to progress in the field of alloy structure analysis and design. The purpose of these methods is to provide an efficient and accurate way to compute the total energy of arbitrary atomic systems in terms of their geometrical config- uration. In most cases, the existing techniques are restricted to a few systems for which a specific (and therefore non-transferable) parameterization is devel- oped, thus limiting their use. However, the recent trend of combining first-principles with quantum approx- imate methods has opened up new possibilities in the field of atomistic simulations, as they provide accurate and valuable input for the determination of para- meters. This approach is particularly useful when experimental data are not available, as are the cases of bcc-U and bcc-Al.

One of these quantum approximate methods, the Bozzolo-Ferrante-Smith (BFS) method for alloys [4] can deal with complex systems and geometries, as it has no theoretical constraints regarding the type and number of elements, or on the number or type of phases it can handle. In addition, the particular way in which BFS models the process of alloy formation guarantees reliable results for bulk properties as well as for extended defects, surfaces, or interfaces.

The purpose of this work is, for the first time, to introduce atomistic modeling to understand the inter- diffusion of Al along the grain boundaries of the U- Mo solid solution. As a first step, we present preli- minary results of a modeling effort dealing with the interdiffusion of Al in the (1 0 0) and (1 1 0) surfaces of a bcc-based U-Mo solid solution. We show the basic features needed by BFS to describe a ternary system and how it is implemented in systems where the elements are not in their stable state like bcc-U and bcc-Al. The results for the ternary system are dis- cussed within the framework of the results obtained for the binary cases, Al/Mo and Al/U. Besides the fundamental features identified in these cases, the full ternary Al-U-Mo system is analyzed and its behavior compared with experimental observations.

## 2. The BFS method

The BFS method [4] is based on the concept that the energy of formation of a given atomic configuration is the superposition of the individual atomic contribu- tions $\Delta H=\Sigma \varepsilon_{i}$. Each contribution $\varepsilon_{i}$ is the sum of two terms: a strain energy, $\varepsilon_{i}^{S}$ computed in the actual lattice as if every neighbor of the atom $i$ was of the same atomic species $i$, and a chemical energy, $\varepsilon_{i}^{C}$, computed as if every neighbor of the atom $i$ was in an equilibrium lattice site of a crystal of species $i$, but retaining its actual chemical identity. The computation of $\varepsilon_{i}^{S}$, using Equivalent Crystal Theory (ECT) [5], involves three pure element properties for atoms of species $i$: cohe- sive energy, lattice parameter and bulk modulus. The chemical energy, $\varepsilon_{i}^{C}$ includes two BFS perturbative parameters ( $\Delta_{ij}$ and $\Delta_{ji}$, with $i,j=$ Al, U, Mo). A reference chemical energy, $\varepsilon_{i}^{C_{0}}$, is also included to insure a complete decoupling of structural and che- mical features. In this work, all the necessary para- meters were determined using the linearized augmented plane wave method (LAPW) [6], by com- puting the equilibrium properties of Al, Mo, and U in the bcc phase, as well as the equilibrium properties of AlMo, UMo and AlU ordered alloys in the B2 phase. All the calculations for pure elements and their alloys were performed using the generalized gradient approximation (GGA) for the exchange-correlation energy functional [7]. Finally, the strain and chemical energies are linked with a coupling function $g_{i}$, which ensures the correct volume dependence of the BFS chemical energy contribution. Therefore, the contri- bution of atom $i$ to the energy of formation of the system is given by

$$
\varepsilon_{i}=\varepsilon_{i}^{\mathrm{S}}+g_{i}\left(\varepsilon_{i}^{\mathrm{C}}-\varepsilon_{i}^{\mathrm{C}_{0}}\right) \tag{1}
$$

Table 1 lists the single element parameters and Table 2 lists the BFS parameters $\Delta$ needed for apply- ing the BFS method to the Al-U-Mo system. We refer

Table 1
LAPW results for the lattice parameter, cohesive energy, and bulk modulus for the bcc phases of Al, Mo, and U

<table>
<thead>
<tr>
<th></th>
<th>Lattice parameter (Å)</th>
<th>Cohesive energy (eV)</th>
<th>Bulk modulus (GPa)</th>
<th>$p$</th>
<th>$\alpha$ (Å$^{-1}$)</th>
<th>$l$ (Å)</th>
<th>$\lambda$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Al</td>
<td>3.2381</td>
<td>3.44</td>
<td>69.14</td>
<td>4</td>
<td>1.7639</td>
<td>0.3641</td>
<td>1.0232</td>
</tr>
<tr>
<td>Mo</td>
<td>3.1616</td>
<td>6.67</td>
<td>260.61</td>
<td>8</td>
<td>3.4773</td>
<td>0.2641</td>
<td>0.7422</td>
</tr>
<tr>
<td>U</td>
<td>3.4501</td>
<td>5.55</td>
<td>141.40</td>
<td>12</td>
<td>4.8689</td>
<td>0.3132</td>
<td>0.8801</td>
</tr>
</tbody>
</table>

The resulting Equivalent Crystal Theory (ECT) [5] parameters $p$, $\alpha$, $l$ and $\lambda$ are also listed (see text and [4,5]).

Table 2
BFS parameters $\Delta_{\mathrm{ij}}$ (in Å$^{-1}$) for all the binary combinations (i,j) of Al, Mo, and U

<table>
<thead>
<tr>
<td>i\j</td>
<td>Al</td>
<td>Mo</td>
<td>U</td>
</tr>
</thead>
<tbody>
<tr>
<td>Al</td>
<td></td>
<td>$-$0.03351</td>
<td>0.15351</td>
</tr>
<tr>
<td>Mo</td>
<td>0.10065</td>
<td></td>
<td>$-$0.06189</td>
</tr>
<tr>
<td>U</td>
<td>$-$0.03909</td>
<td>0.09261</td>
<td></td>
</tr>
</tbody>
</table>

the reader to [4] for a detailed discussion of the BFS method, its definitions, operational equations and their implementation.

## 3. Experimental background

### 3.1. Al/Mo(1 1 0)

Auger electron spectroscopy (AES), low energy electron diffraction (LEED) and electron energy loss spectroscopy (EELS) experiments [8] show that a layer-by-layer growth mechanism of the adsorbate is primary at room temperature. For coverage lower than 0.34 ML, the adsorbate is formed as a two-dimensional gas on the surface. Al atoms occupy random positions on the surface, a behavior which is probably responsible for the appearance of the $(1\times1)$ pattern of the substrate. All the LEED patterns observed at room temperature originated from more or less deformed, hexagonal layers of aluminium which had different crystallographic orientations with respect to the substrate. Most probably no alloys are formed though the possibility is not fully excluded [8].

### 3.2. Al/U

In contrast with the behavior observed in Al/Mo, experimental observations indicate that there is strong interdiffusion of Al and intermetallic formation with different stoichiometries [2,9–11].

### 3.3. Al/(U,Mo)

The experimental results show that the U–2 wt.% Mo/Al dispersions increase in volume by 26% at 400 °C after 2000 h. This large volume change is mainly due to the formation of voids and cracks resulting from nearly complete interdiffusion of U–Mo and Al. No significant dimensional change occurs in the U–10 wt.% Mo/Al dispersions. Interdiffusion between U–10 wt.% Mo and aluminum is found to be minimal. The differences in diffusion behavior are primarily due to the fact that U–10 wt.% Mo particles are supersaturated with substitutional molybdenum, more so than the U–2 wt.% Mo particles. Al diffuses into the U–2 wt.% Mo particles relatively rapidly along grain boundaries with nearly pure U forming $\mathrm{UAl}_{3}$ almost fully throughout the 20:00 h anneal, whereas the supersaturated Mo in the U–10 wt.% Mo particles inhibits the diffusion of Al atoms [2].

## 4. Results and discussion

The deposition of Al on a Mo substrate can be easily studied by considering a few basic configurations where the Al atom occupies sites in the overlayer, surface, or planes immediately below the surface plane. Fig. 1 shows the results for such configurations, plotted as a function of increasing difference in energy with respect to the lowest energy state. For Al/Mo(1 0 0), the sequence starts with the Al atom in the overlayer (Al(O)), followed by states describing the penetration of Al into the Mo slab: $\mathrm{Al(S)Mo(O)_{f}}$, where the ejected $\mathrm{Mo(O)}$ atom locates itself far from the surface $\mathrm{Al(S)}$ atom; $\mathrm{Al(S)Mo(O)_{n}}$,

![](./images/812398974567710721_4.jpg)

Fig. 1. Energy level spectrum for Al deposition on Mo. The first column shows results for the $N_{\text{Al}}=1$ case listing, for each configuration and for each Mo crystal face, the difference in energy (in eV) with respect to the lowest energy state (bottom). The adatom can either be located in the overlayer (on top of the cube), in a surface site (crossing the top edge of the cube), in the first layer (1b) below the surface (immediately below the top edge of the cube) and two layers (2b) below the surface (in the center of the cube). The center and right columns show similar results for $N_{\text{Al}}=2$ in the (1 0 0) and (1 1 0) faces, respectively. Al and Mo atoms are indicated with solid black disks and open circles, respectively. The arrows indicate a reversal of ordering for the (1 1 0) case relative to the order characteristic of the (1 0 0) case.

where they locate themselves in nearest-neighbor sites; $\text{Al(1b)Mo(O)}_{\text{n}}$, where the Al atom goes to a site in the first layer below the surface (1b) and the $\text{Mo(O)}$ atom remains close, followed by a similar configuration where $\text{Mo(O)}$ migrates somewhere else on the surface $(\text{Al(1b)Mo(O)}_{\text{f}})$, and lastly, $\text{Al(2b)-Mo(O)}$, where the Al atom interdiffuses to the second layer below the surface (2b) in the Mo substrate. Fig. 1 also lists the corresponding results for Al deposition on $\text{Mo(1 1 0)}$, which show the same qualitative behavior observed in the $\text{Mo(1 0 0)}$ case. From the onset, it is clear that there is no penetration of Al in the inner layers of Mo. BFS results indicate that the formation of a surface alloy is more likely on the (1 0 0) than in the (1 1 0) face, due to the larger energy gap between states with $\text{Al(O)}$ and $\text{Al(S)}$ in the second case. The case for two Al atoms is also shown in Fig. 1. Increasing coverage leads to the formation of $\text{Al(O)}$ chains

along the close-packed direction both for Mo(1 0 0) and Mo(1 1 0).

Quite the opposite behavior occurs for deposition of Al on U. Fig. 2 summarizes the results for deposition of one single Al atom on a U(1 0 0) or U(1 1 0) slab. In both cases, the lowest energy state corresponds to Al in the bulk. The energy of the computational cell increases steadily as the Al atom approaches the surface, clearly indicating that Al has high solubility in U. The small differences in the ordering of the energy levels for U(1 1 0) in comparison to U(1 0 0) are indicated by arrows in Fig. 2. Similar results are observed for two Al atoms, where the lowest energy state consists of two Al atoms in solution in the U bulk. There is, however, a close low energy state (0.03 eV per atom above the lowest energy configuration) where the two Al atoms are located at third neighbor distance. This can be seen as an emerging trend for ordering with increasing Al concentration. Further

![](./images/812398974567710721_5.jpg)

Fig. 2. Energy level spectrum for Al deposition on U. For the (1 0 0) and (1 1 0) surfaces of U, the diagram shows the difference in energy (in eV) with respect to the lowest energy state (bottom). The configurations are ordered by increasing energy difference according to the (1 0 0) face results. The arrows on the right hand side of the figure indicate those states and energies that are in reverse order than that obtained for the (1 0 0) case. Al and U atoms are indicated with solid black disks and open circles, respectively.

![](./images/812398974567710721_6.jpg)

Fig. 3. Energy level spectrum for Mo deposition on U. For the (1 0 0) and (1 1 0) surfaces of U, the diagram shows the difference in energy (in eV) with respect to the lowest energy state (bottom). The configurations are ordered by increasing energy difference according to the (1 0 0) face results. The arrows on the right hand side of the figure indicate those states and energies that are in reverse order than that obtained for the (1 0 0) case. Mo and U atoms are indicated with solid black disks and open circles, respectively.

analysis of this feature, beyond the scope of this paper, will be performed in future efforts. As one last note on the Al/U system, it is interesting to point out that the (1 1 0) face inhibits interdiffusion due to the large energy barrier when an Al atom occupies a surface site (right column in Fig. 2).

The deposition of Mo on U, shown in Fig. 3, is slightly more complex, compared to the previous two cases. The lowest energy state corresponds to the Mo(1b)U(O) case, followed by Mo(2b)U(O). These results are consistent with the existence of a U-Mo solid solution, indicated by the preference of Mo for an U bulk-like environment. For U(1 0 0), the pre- sence of a surface, however, triggers a segregation process by which the Mo atom migrates to layers in the sub-surface, but not to the actual surface plane, for which it has to overcome a small energy barrier. No such barrier exists in the U(1 1 0) case. Besides this single effect, there are minimal differences between the computed behavior in the (1 0 0) and (1 1 0) face of U.

The results shown in Figs. 1-3 are, in all cases, in agreement with experiment. This is indicative of the robustness of the BFS parameters used to describe the interactions between the different pairs of atoms. Having raised the necessary confidence on this set of BFS parameters, we now apply them to the study of the ternary Al-U-Mo system.

![](./images/812398974567710721_7.jpg)

Fig. 4. Energy level spectrum for Al deposition on a U slab in the presence of a Mo atom in a (a) surface site, (b) 1b site, and (c) 2b site. In each case, two different situations are examined: when the deposited Al atom is close or far from the Mo atom. The configurations are ordered, top to bottom, in terms of decreasing difference in energy with the lowest energy state. Mo, Al and U atoms are indicated with solid black disks, grey disks, and open circles, respectively.

The energy gaps in all these spectra are of comparable magnitude and it is difficult to predict the three-element behavior from the binary cases. The competing behaviors observed for Al/Mo and Al/U will result in a specific behavior of the ternary system that can only be described by a proper accounting of the interaction between the different pairs and how such interactions are modified by the presence of a third element. Following the style of Figs. 1-3, the deposition of Al on a U-Mo substrate is summarized in Fig. 4.

To simplify the analysis, we first examine the deposition of a single Al atom on a U-Mo(1 0 0) substrate as a function of the distance between Al and Mo and as a function of the location of the Mo atom. For completeness, the corresponding results for U-Mo(1 1 0) are also shown.

When the Mo atom is located in a surface site, Mo(S), the lowest energy state for both crystal faces is Al(2b)+Mo(S)+U(O). This is true both for the case in which Mo(S) is close (left column) or far

![](./images/812398974567710721_8.jpg)

Fig. 5. Top view of different configurations showing an Al atom (black disk) in different overlayer (left column), surface (center column) and subsurface sites (right column) in the vicinity of a cluster of Mo atoms (grey disks) in an U substrate. Ejected U atoms are denoted with an open circle. Each configuration is labeled by the difference in energy (in eV) with the reference state in which an Al adatom is located away from the Mo patch (top left corner). The horizontal or vertical arrows indicate those transitions that are energetically favored.

(right column) from the deposited Al atom. Clearly, the presence of a single Mo atom, whether it is close or far to Al, does not change the trend observed for Al/U(1 0 0) or Al/U(1 1 0), where Al interdiffusion dominates.

In the case when the Mo atom is located in a 1b site, Mo(1b), once again the lowest energy state is that where Al interdiffuses in the substrate, regardless of the separation between Al and Mo. The lowest energy state is always $[Al(2b)Mo(1b)]_n + U(O)$, except for the (1 0 0) face, when Al and Mo atoms are close to each other. This introduces a small energy barrier (0.0571 eV per atom) that would slow, but not inhibit, interdiffusion of Al to deeper layers. A similar situation is found in the case when the Mo atom is located in a 2b site (which is, in essence, far enough as to not feel the presence of the surface).

The results in Fig. 4 show, in conclusion, that for both substrate terminations Al diffuses into the U-Mo substrate, in spite of the presence of an energy barrier, when Al occupies surface sites, as seen in the (1 1 0) surface. However, a close examination of the magnitude of the energy gaps between the configurations whose ordering led to this conclusion indicates that such effect is facilitated in regions with low Mo concentration. These regions are modeled by configurations where Mo is far from Al. In summary, the presence of Mo favors the location of Al in surface or overlayer sites, thus affecting, but not inhibiting, Al interdiffusion in the bulk of U-Mo solid solution for this level of coverage, i.e. in the very dilute limit.

More insight on this behavior can be obtained by analyzing a set of configurations that model the penetration of Al into subsurface layers in regions of high Mo surface concentration. The 15 configurations in Fig. 5 describe the process in different ways: (a) from top to bottom, showing the evolution of an Al atom in the overlayer (left column), surface layer (center column) and 1b layer (right column), in the presence of a cluster of Mo(S) atoms, and (b) from left to right, showing the evolution of the Al atom as it moves from the overlayer site, to the surface site, and to the 1b layer. This is shown for different locations of Al relative to the Mo(S) patch: far from the patch (top row), as a nearest neighbor of a 'corner' Mo(S) atom (second row), with two, three and four (third, fourth and fifth row, respectively) nearest neighbors in the Mo patch.

The top row indicates that the penetration of Al (when deposited far from the Mo patch) in subsurface layers is energetically favored, an effect that is less pronounced as Al(O) approaches the Mo patch: the second row indicates that the process is still possible if Al(O) connects to the Mo(S) patch via one Mo(S) atom, but unlikely when the number of Al(O)-Mo(S) bonds increases (third, fourth, and fifth row). However, regardless of their proximity to the patch, Al atoms tend to migrate to Mo-rich regions. All three columns in Fig. 5 represent, from top to bottom, the process of Al diffusion towards the Mo patch. In all three cases, whether Al is in an overlayer, surface or 1b site, the lowest energy state is characterized by maximum coordination between the Al atom, the Mo patch and the surrounding U environment. This analysis shows that, in agreement with experiment, Al interdiffusion is prevalent in Mo-deficient regions of the U-Mo substrate.

## 5. Conclusions

The development of new alloys or small improvements to current alloys are usually made through extensive experimental trial and error work. One example of the current methodology is the development of low enrichment uranium fuel for research reactors. However, recently developed computational methods have become a viable tool to assist in alloy development programs. In particular, the method presented in this work, the BFS method for alloys, has been proven to be highly effective in the study of multicomponent systems or surface alloys but was never applied to the study of an actinide-based multicomponent alloy. In this work, we applied the BFS method to the atomistic modeling of Al interdiffusion in U-Mo as a function of Mo concentration. The method was applied first to the deposition of Al in the (1 0 0) and (1 1 0) surfaces of Mo and U substrates. Two opposite behaviors were found: while in Al/U Al atoms show a noticeable tendency to interdiffuse in the bulk, in Al/Mo the same atoms show a tendency for layer-by-layer growth and the formation of structures in the overlayer. In excellent agreement with experimental evidence, the atomistic modeling results show that these two opposite behaviors translate in the ternary system Al/U-Mo to the role of regions rich in Mo acting as an interdiffusion barrier for Al atoms.

### Acknowledgements

Fruitful discussions with N. Bozzolo are gratefully acknowledged. This work was supported by the International Computational Materials Science Consortium (OAI/NASA) through the HOTPC project at NASA Glenn Research Center, and by the Comisión Nacional de Energía Atómica (CNEA), Argentina.

### References

[1] G.L. Hofman, L.C. Walters, in: Nuclear Materials, vol. 10A, VCH, NY, 1994.

[2] D.B. Lee, K.H. Kim, C.K. Kim, J. Nucl. Mater. 250 (1997) 79.

[3] M.D. Jones, J.C. Boettger, R.C. Albers, D.J. Singh, Phys. Rev. B 61 (2000) 4644.

[4] G. Bozzolo, J. Ferrante, E.D. Noebe, F. Honecy, P. Abel, Comp. Mater. Sci. 15 (1999) 169.

[5] J.R. Smith, T. Perry, A. Banerjea, J. Ferrante, G. Bozzolo, Phys. Rev. B 44 (1991) 6444.

[6] P. Blaha, K. Schwartz, J. Luitz, WIEN97, in: P. Blaha, P. Schwartz, P. Sorantin, S. Trickey (Eds.), Improved and Updated Unix Version of the Copyrighted WIEN Code, Vienna University of Technology.

[7] J.P. Perdew, K. Burk, M. Ernzerhof, Phys. Rev. Lett. 77 (1966) 3865B;
J.P. Perdew, K. Burk, M. Ernzerhof, Comput. Phys. Commun. 59 (1990) 399.

[8] J. Kolaczkiewicz, M. Hochol, S. Zuber, Surf. Sci. 247 (1991) 284.

[9] D. Subramanyam, M. Notis, J. Goldstein, Met. Trans. 16A (1985) 589.

[10] R. Pearce, R. Giles, L. Tavender, J. Nucl. Mater. 24 (1967) 129.

[11] J. Buddery, M. Clark, R. Pearce, J. Stobbs, J. Nucl. Mater. 13 (1964) 169.