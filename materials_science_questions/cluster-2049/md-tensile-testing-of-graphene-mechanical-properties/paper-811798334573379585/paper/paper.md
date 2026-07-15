# Structure and Layer Interaction in Carbon Monofluoride and Graphane:
## A Comparative Computational Study

Vasilii I. Artyukhov and Leonid A. Chernozatonskii*

Institute of Biochemical Physics, Russian Academy of Sciences, Kosygin st. 4, Moscow, 119334 Russia

Received: January 13, 2010; Revised Manuscript Received: March 9, 2010

Carbon monofluoride $(CF)_n$ and graphane are two very different materials from the practical point of view, but the basic chemical motifs of these materials are closely related: both can be described as two-dimensional polycyclic (fluoro-/hydro-)carbons. However, the actual experimental data on the structure of these materials is ambiguous $((CF)_n)$ or scarce (graphane). Herein, we report a detailed computational study of structure of $(CF)_n$ and graphane, both in a monolayer configuration and in three-dimensional stacked arrangements. A crucial point in achieving a proper description of layer interactions is the use of a nonlocal density functional to describe long-range dispersion attraction from first principles. We find strong qualitative and quantitative similarities between the two materials in both conformational energetics (including a "gauche-chair" conformational motif not considered in previous studies) and layer stacking arrangements. A molecular mechanics force field is derived for $(CF)_n$ that performs exceptionally well at reproducing our quantum chemical results and fits into a very general OPLS/AA molecular mechanics framework. The combined results of quantum chemical calculations and classical molecular dynamics simulations using the new force field suggest a pathway to explain the too-small experimental in-plane lattice constant values observed in these materials, as well as the variation of interlayer distance in $(CF)_n$, on the common basis of conformational disorder.

## 1. Introduction

Carbon monofluoride $^{1}$ $(CF)_n$ is an important material in industry, being one of the most stable polymeric fluorocarbons. It possesses unique lubricating properties under extreme physical conditions (high temperatures and vacuum), owing to the ease of relative sliding of its layers. The properties of this material are well studied from the practical point of view. However, a detailed understanding of its structure and properties at the atomic scale is still missing. The main reason for that is the structural disorder that results from random orientation of weakly interacting layers. Because of this, fabrication of monocrystalline samples of $(CF)_n$ suitable for single-crystal X-ray diffraction studies has been unachievable, and even powder diffraction data are hard to interpret.

Graphane²-hydrogenated graphene-is a new "rising star" of carbon-based nanotechnology. The main expectations regarding this material are associated with local patterning of graphene sheets to form nanoscale circuit elements or even whole circuits. However, the first experimental studies³ have not yet succeeded in providing straightforward information on the structure of graphane.

From the computational point of view, the weakness of layer interactions in $(CF)_n$ means that traditional local or semilocal density functional calculations cannot be used to describe the three-dimensional (3D) material (although calculations have repeatedly been used to study $(CF)_n$ monolayers). On the other hand, while empirical molecular mechanics methods are generally successful at describing long-range dispersion attraction, no attention has previously been paid to parametrization of a $(CF)_n$-specific molecular mechanics force field, or even to testing the already existing force fields for perfluoroalkanes to see how well they perform for $(CF)_n$. In the present work, the former problem is solved by using a nonlocal density functional that is capable of reproducing the long-range dispersion interactions to a good accuracy, and the results of quantum chemical calculations are used to optimize a molecular mechanics force field for $(CF)_n$ to address the latter issue. Although the performance of standard alkane molecular mechanics parameters for graphane seems more-or-less satisfactory (with the exception of underestimated $C-H$ bond length), standard perfluoroalkane force fields turn out to be untransferable to $(CF)_n$, and reparametrization is indeed required in this case.

We find strong similarities between $(CF)_n$ and graphane that result in strikingly parallel qualitative trends regarding both the structure of monolayers and the stacking of layers. Both materials demonstrate three basic local conformational motifs that are in the thermodynamically accessible energy range. We suggest that the coexistence of all three conformations (particularly, the "gauche-chair" conformation not considered in previous works) could provide an explanation for small in-plane lattice constant values observed for both materials, reconciling the experiment with calculations. Additionally, this coexistence could provide an explanation for the broad range of interlayer distances in $(CF)_n$ reported in the literature; similar arguments, when transferred to graphane, allow us to make predictions regarding the layer spacing in multilayer graphane, which is a material that has yet to be observed experimentally.

## 2. Computational Details

Quantum chemical calculations for individual layers of $(CF)_n$ and graphane were performed using a generalized gradient approximation to density functional theory by Perdew et al. (PBE),⁴ which has become the "industry standard" for nonempirical DFT due to its excellent performance in describing the structure of molecules and solids across many chemical classes.⁵

* To whom correspondence should be addressed. Phone: +7 (495) 939 7172. Fax: +7 (499) 137 4101. E-mail: cherno@sky.chph.ras.ru.

10.1021/jp1003566 © 2010 American Chemical Society
Published on Web 04/06/2010

The calculations were carried out with the ABINIT code⁶ using a projector augmented wave⁷ basis set and repeated with the PWSCF code from the Quantum-ESPRESSO package⁸ using plane waves and ultrasoft pseudopotentials.⁹ The basis set cutoff used was 70 and 60 Ry, correspondingly, which corresponds to convergence of relative energies well below 0.001 eV/atom in both cases. The equivalent real space cutoff for in-plane Brillouin zone integrations was not less than 23 Å, quite sufficient for our dielectric systems (we used a 10 × 6 × 1 grid for orthogonal unit cells, corresponding roughly to a 10 × 10 × 1 grid for the primitive hexagonal cell of the chair conformation, see below). A 10 Å spacing between the periodic images of the layer turned out to be large enough to ensure total absence of interaction; in several cases, calculations were repeated at 25 and 30 Å spacing, confirming that this is indeed so.

Calculations for fully 3D periodic systems were carried out using a two-step procedure. First, the configurations were generated using molecular mechanics, and optimized at a series of fixed layer separation values using PWSCF (see above). Then, a nonself-consistent correction to the total energy from long-range correlation¹⁰ was calculated from the resulting electron density using a fully nonlocal formulation of density functional theory by Dion et al.¹¹ (vdW-DF), as implemented in the JuNoLo code.¹² The resulting energy values were plotted against the layer separation, and the minimum was found by fourth degree power interpolation. Such a procedure has been previously demonstrated to yield good results for such systems as intercalated graphite¹³ and carbon nanotube bundles.¹⁴ We have additionally checked this approach on graphite, where the regular semilocal generalized-gradient DFT fails to predict a bound state at all; the resulting value of lattice constant $c = 6.93$ Å is in good (for a DFT-based method, unprecedented) agreement with the actual value of $c \sim 6.7$ Å.

Molecular mechanics calculations were performed using the GROMACS package.¹⁵ As a starting point for the parametrization, the OPLS/AA parameter set for fluorocarbons¹⁶ was used. The OPLS/AA methodology¹⁷ was chosen because it provides molecular mechanics parameters for a wide range of chemical compounds, and the derivation of these parameters focuses not just on the gas-phase structures of molecules, but on the properties of pure liquids, as well, and these are especially sensitive to intermolecular interactions—the same as our systems of interest.

## 3. Results and Discussion

### 3.1. Structure of Isolated Layers.
Experimentally, the structural data on both $(CF)_n$ and graphane are usually interpreted within the model shown in Figure 1a. It represents a hexagonal graphene layer fully covered by adatoms (F or H). Adatoms connected to neighboring carbon atoms (belonging to different sublattices of the hexagonal skeleton) are located by the opposite sides of the carbon layer. This structure is termed "chair" $(C)$ due to the conformation of carbon hexagons.

Computational studies have also considered another possible structure shown in Figure 1b. In this structure, adatoms form alternating pairs by each side of carbon layer. The unit cell of this structure is orthogonal, and the structure is termed "bed" $(B)$ since carbon hexagons adopt bed conformation here. Finally, a third possible structure has not, to our knowledge, been previously studied; it is shown in Figure 1c. There, adatoms by each side of the carbon layer form zigzag lines. The resulting structure has a W-like corrugated shape when viewed along these zigzag lines; hence we term this structure "washboard" $(W)$ in the following. Carbon hexagons again have chair conformation, but their linking pattern is different from structure $C$, and this conformation can also be termed "gauche-chair" with respect to the conformation of XCCX (X = H, F) chains, in an analogy with the conventional notation used in polymer science. Then, within this course of thought, the chair $(C)$ structure of Figure 1a can be alternatively termed "anti-chair".

![](./images/811798334573379585_1.jpg)

Figure 1. Possible monolayer conformations of $(CX)_n$ ($X = H, F$): (a) chair, or CX-$C$, (b) bed, or CX-$B$, and (c) washboard (gauche-chair), or CX-$W$, structures. Carbon atoms are shown in yellow; blue represents fluorine/hydrogen.

![](./images/811798334573379585_2.jpg)

Figure 2. Adatom alternation patterns underlying the three possible conformations of $(CF)_n$/graphane monolayers: (a) chair, (b) bed, and (c) washboard structures. Only half of the adatoms are seen (blue), while the other half is eclipsed by carbon atoms (yellow). Black arrows (b, c) show the direction of structure relaxation leading to the optimized structures shown in Figure 1.

In summary, the three conformations described above fall into the following classification of adatom alternation patterns (see Figure 2):

$C$: for each carbon atom, the adatoms of all three carbons it is bonded to are located by the opposite side of the carbon layer relative to its own adatom;

$B$: the adatoms of two of the neighboring carbons are by the opposite side of the carbon layer, and the adatom of one neighboring carbon is by the same side as its own adatom;

$W$: one neighboring adatom by the opposite side and two adatoms by the same side.

Finally, it should be noted at this point that the boundary between two incongruent structure $C$ domains is nothing other than a region (line) with local $B$ or $W$ type conformation, depending on whether the direction of the boundary is along zigzag or armchair direction of the carbon layer ($X$ and $Y$ in Figure 2, respectively).

The results of quantum chemical calculations for all three conformations are summarized in Tables 1 (bonds and angles) and 2 (lattice parameters). The results for structures $C$ and $B$ are in good agreement with those of previous computational studies both for both $(CF)_n^{18}$ and graphane.² In both cases, the new gauche-chair conformation $W$ turns out to be energetically more favorable than structure $B$: the relative energies of the two conformations with respect to the ground-state chair conformation are $(W)$ 0.071 and $(B)$ 0.148 eV per CF unit in $(CF)_n$ and are $(W)$ 0.055 and $(B)$ 0.103 eV per CH unit in graphane. This could be explained by the less strained chairlike

Carbon Monofluoride and Graphane

J. Phys. Chem. A, Vol. 114, No. 16, 2010 5391

TABLE 1: Calculated Relative Energies Per Formula Unit (Two Atoms) and Geometrical Parameters in Isolated Monolayers of $(\text{CX})_n$ ($\text{X} = \text{F}, \text{H}$)

<table>
  <thead>
    <tr>
      <th>structure</th>
      <th>$E - E_{\text{C}}$ (eV)</th>
      <th>$R_{\text{XX}}$ (Å)</th>
      <th>$R_{\text{CX}}$ (Å)</th>
      <th>$R_{\text{CC-1}}$ (Å)</th>
      <th>$R_{\text{CC-2}}$ (Å)</th>
      <th>$\angle_{\text{CCC}}$ (°)</th>
      <th>$\angle_{\text{XCC-1}}$ (°)</th>
      <th>$\angle_{\text{XCC-2}}$ (°)</th>
      <th>$\theta_{\text{XCCC-1}}$ (°)</th>
      <th>$\theta_{\text{XCCC-2}}$ (°)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CF-$C$</td>
      <td>0.000</td>
      <td>2.61</td>
      <td>1.382</td>
      <td>1.584</td>
      <td>1.584</td>
      <td>110.9</td>
      <td>108.0</td>
      <td>108.0</td>
      <td>$-61.9$</td>
      <td>61.9</td>
    </tr>
    <tr>
      <td>CF-$W$</td>
      <td>0.071</td>
      <td>2.44</td>
      <td>1.382</td>
      <td>1.567</td>
      <td>1.602</td>
      <td>115.6</td>
      <td>103.6</td>
      <td>106.2</td>
      <td>$-65.8$</td>
      <td>$-156.6$</td>
    </tr>
    <tr>
      <td>CF-$B$</td>
      <td>0.148</td>
      <td>2.27</td>
      <td>1.377</td>
      <td>1.574</td>
      <td>1.667</td>
      <td>114.0</td>
      <td>102.7</td>
      <td>107.4</td>
      <td>$-115.9$</td>
      <td>66.9</td>
    </tr>
    <tr>
      <td>CH-$C$</td>
      <td>0.000</td>
      <td>2.53</td>
      <td>1.112</td>
      <td>1.538</td>
      <td>1.539</td>
      <td>111.4</td>
      <td>107.2</td>
      <td>107.4</td>
      <td>$-62.6$</td>
      <td>$-62.9$</td>
    </tr>
    <tr>
      <td>CH-$W$</td>
      <td>0.055</td>
      <td>2.36</td>
      <td>1.108</td>
      <td>1.546</td>
      <td>1.547</td>
      <td>112.4</td>
      <td>107.7</td>
      <td>106.4</td>
      <td>63.2</td>
      <td>168.5</td>
    </tr>
    <tr>
      <td>CH-$B$</td>
      <td>0.103</td>
      <td>2.21</td>
      <td>1.107</td>
      <td>1.572</td>
      <td>1.538</td>
      <td>112.3</td>
      <td>106.8</td>
      <td>107.0</td>
      <td>117.1</td>
      <td>$-63.0$</td>
    </tr>
  </tbody>
</table>

TABLE 2: Lattice Parameters for Isolated Layers: Absolute and Relative Values Expressed in Units of Corresponding Chair Structure Parameter

<table>
  <thead>
    <tr>
      <th>structure</th>
      <th>$E - E_{\text{C}}$ (eV)</th>
      <th>$a$ (Å)</th>
      <th>$b$ (Å)</th>
      <th>$a/a_{\text{C}}$</th>
      <th>$b/b_{\text{C}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CF-$C$</td>
      <td>0.000</td>
      <td>2.611</td>
      <td>4.521</td>
      <td>100%</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>CF-$W$</td>
      <td>0.071</td>
      <td>2.635</td>
      <td>4.200</td>
      <td>101%</td>
      <td>93%</td>
    </tr>
    <tr>
      <td>CF-$B$</td>
      <td>0.148</td>
      <td>2.585</td>
      <td>4.617</td>
      <td>99%</td>
      <td>102%</td>
    </tr>
    <tr>
      <td>experimental</td>
      <td></td>
      <td>$2.61^{19\ a}$</td>
      <td></td>
      <td colspan="2">$97\%$ ($2.54$ Å)$^{1\ b}$</td>
    </tr>
    <tr>
      <td>CH-$C$</td>
      <td>0.000</td>
      <td>2.545</td>
      <td>4.406</td>
      <td>100%</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>CH-$W$</td>
      <td>0.055</td>
      <td>2.553</td>
      <td>3.836</td>
      <td>100%</td>
      <td>87%</td>
    </tr>
    <tr>
      <td>CH-$B$</td>
      <td>0.103</td>
      <td>2.533</td>
      <td>4.314</td>
      <td>100%</td>
      <td>98%</td>
    </tr>
    <tr>
      <td>experimental</td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">$92-95\%$ ($2.34-2.43$ Å),$^{3\ b}$</td>
    </tr>
  </tbody>
</table>

$^{a}$ Largest value found in the literature. $^{b}$ Smallest value found in the literature.

carbon hexagons in this structure. In addition, relative energies of the three structures correlate with the minimum distance between neighboring adatoms (see Table 1), which is the largest for structure $C$ and the smallest for structure $B$ (in structure $W$, while neighboring carbon atoms in each zigzag line have their adatoms by the same side of the carbon layer, as in structure $B$, adatoms have more room for relaxation in the direction perpendicular to the direction of zigzag line). This indicates electrostatic repulsion between similarly charged adatoms as another possible factor that affects conformational energetics in these systems. However, analysis of partial energy contribu- tions in molecular mechanics suggests different attribution of strain energy (see below).

Another notable point is the difference between $\text{C}-\text{C}$ bond lengths in different monolayer conformations, which is more pronounced in $(\text{CF})_n$ compared to graphane. In the former, shortening of bonds along the zigzag direction and lengthening in the armchair direction is observed in strained conformations. In the latter, only lengthening (homogeneous in conformation $W$ and zigzag-only in conformation $B$) of $\text{C}-\text{C}$ bonds is observed. Overall, $\text{C}-\text{C}$ bond lengths in $(\text{CF})_n$ are greater than in graphane, which is explained by draining of electron density from the carbon layer by the more electronegative fluorine atoms. At the same time, the carbon layer in $(\text{CF})_n$ has a more planar structure: the $\text{C}-\text{C}-\text{C}$ bond angle is closer to the $120^\circ$ value of planar graphene, and the $\text{F}-\text{C}-\text{C}$ angle is closer to $90^\circ$.

The $\text{C}-\text{H}$ and $\text{C}-\text{F}$ bond lengths in the chair conformation are 1.112 and $1.382$ Å, respectively, and slightly decrease in the strained $W$ and $B$ conformations (within $0.005$ Å). These values exceed those typical for alkanes ($1.09$ Å) and perfluo- roalkanes ($1.34$ Å), which suggests that the chemistry of these layered systems is, in fact, different from that of linear polymers, and that they should not be treated as "simply" two-dimensional infinite polycyclic (perfluoro)alkanes.

We should note the excellent agreement of lattice parameter for CF-$C$ structure ($2.61$ Å) with experimental results for $(\text{CF})_n$ reported by Sato et al.$^{19}$ and by Giraudet et al.$^{20}$ Both results are on the "large end" of spectrum of lattice constant values reported in the experimental literature, and other researchers have repeatedly reported values that are smaller: in fact, as low as $2.54$ Å.$^{1}$ This is a fundamental issue in the interpretation of experimental data, and a similar problem exists in the case of graphane, where experimental observations of strong lattice contraction upon hydrogenation of graphene (lattice constant ranging from $2.34$ to $2.50$ Å$^3$) are in direct contradiction with computational results for chairlike graphane ($2.545$ Å in the present work, see Table 2).

One possible way to reconcile experimental observations with theoretical atomistic models is to assume that the real samples of $(\text{CF})_n$ and graphane could have a random structure of chaotically oriented domains with different local conformations, resulting in a pseudoperiodic structure of the skeletal carbon layer that retains the trigonal symmetry of graphene "on average". If this assumption is true, the washboard (gauche- chair) structure of both $(\text{CF})_n$ and graphane possesses sufficiently small lattice constant in at least one of the directions compared to that of structure $C$ to explain even the smallest values observed experimentally and still leaving room for other conformations (see Table 2). That is a unique feature of this conformation: the bedlike conformation demonstrates only minor lattice compression in just one crystallographic direction for graphane, and in $(\text{CF})_n$, its lattice, in fact, is expanded rather than contracted, compared the chair conformation.

Recently, an explanation of small lattice parameter values observed in graphane that bears a certain resemblance to the above discussion has been put forward by Flores et al.$^{21}$ (in particular, it is based on the concept of local structural disorder and pseudoperiodicity of the carbon layer). It involves adatom frustration on the borders between incongruent chair conforma- tion domains. The authors suggest that, due to there being no energetically preferential direction of adatom chemisorption, carbon atoms at the interface between two such domains will remain nonpassivated, forming shortened $\text{C}-\text{C}$ bonds with their neighbors (for a detailed explanation, refer to the original paper$^{21}$). However, this arrangement results in the presence of localized unpaired electrons on these nonpassivated carbon atoms, which should make such a configuration energetically unfavorable and prone to passivation from either side, resulting in the formation of local washboard or bedlike conformation regions as noted above. Our results suggest, despite the geometrical strain inherent in both conformations, the energy

<table>
<thead>
<tr>
<th>quantity</th>
<th>OPLS-1</th>
<th>OPLS-2</th>
<th>OPLS-3</th>
<th>OPLS-4</th>
<th>OPLS-5</th>
<th>DFTª</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E_{CF-W}$ (eV)</td>
<td>0.046</td>
<td>0.054</td>
<td>0.052</td>
<td>0.055</td>
<td>0.074</td>
<td>0.071</td>
</tr>
<tr>
<td>$E_{CF-B}$ (eV)</td>
<td>0.122</td>
<td>0.130</td>
<td>0.125</td>
<td>0.141</td>
<td>0.147</td>
<td>0.148</td>
</tr>
<tr>
<td>$a_{CF}$ (Å)</td>
<td>2.60</td>
<td>2.60</td>
<td>2.60</td>
<td>2.60</td>
<td>2.609</td>
<td>2.611</td>
</tr>
<tr>
<td>$c_{CF}$ (Å)</td>
<td>5.60</td>
<td>5.60</td>
<td>5.60</td>
<td>5.60</td>
<td>5.75</td>
<td>5.71</td>
</tr>
<tr>
<td>$R_{C-F}$ (Å)</td>
<td>1.33</td>
<td>1.33</td>
<td>1.33</td>
<td>1.33</td>
<td>1.389</td>
<td>1.389</td>
</tr>
<tr>
<td>$R_{C-C}$ (Å)</td>
<td>1.57</td>
<td>1.57</td>
<td>1.57</td>
<td>1.57</td>
<td>1.579</td>
<td>1.581</td>
</tr>
<tr>
<td>$\angle_{C-C-F}$ (°)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>107.5</td>
<td>107.6</td>
</tr>
<tr>
<td>$\angle_{C-C-C}$ (°)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>111.5</td>
<td>111.2</td>
</tr>
</tbody>
</table>

$^{a}$ Relative energies listed are those of $(CF)_n$ monolayer conformations; geometrical parameters correspond to a fully periodic 3D stacked system in the chair conformation.

of this strain is still insignificant compared to typical covalent bond strength values. On the other hand, the original suggestion was supported by molecular mechanics simulations, which by their very nature are unable to account for the effects of unpaired electron presence. In summary, we believe our explanation of small lattice parameter values in graphane and $(CF)_n$ to be more plausible. However, the two are not mutually exclusive, especially in the case of graphane experiments,³ where the degree of coverage of graphane by hydrogen has probably been substantially lower than the ideal 1:1 C/H atomic ratio. Another recent attempt at explaining the small lattice constant values observed for graphane attributed the effect to a "twisted-boat- chair" conformation of the bedlike structure.²² However, the reported total energy of this conformation is considerably higher than that of bed the conformation, making this structure seem prone to relaxation into the usual bed structure, and a thermo- dynamically unlikely candidate for the role of explanation of actual lattice parameter values.

### 3.2. Optimization of Molecular Mechanics Parameters for
$(CF)_n$. Molecular mechanics is an invaluable tool for simulations of atomic-scale dynamics of materials and molecules involving large numbers of atoms in the unit cell. In the context of $(CF)_n$, it is important to have such a tool to understand interactions between layers in this material, as well as those between $(CF)_n$ and other chemical substances. However, although a substantial number of studies have been dedicated to fitting of molecular mechanics force field parameters for polytetrafluoroethylene and other perfluoroalkane systems, to the best of our knowledge, no parameter sets focused specifically on $(CF)_n$ have been reported in the literature until now. At the same time, as noted above, structural parameters of $(CF)_n$, as well as those of graphane, indicate that these polycyclic materials differ chemi- cally from linear (perfluoro)alkanes, and may require separate treatment from molecular mechanics point of view.

The original OPLS/AA parameter set¹⁶ contains four sets of Fourier coefficients for C−C−C−C dihedral angles: a generic one (OPLS-1) and three molecule-specific sets optimized for linear perfluorobutane (OPLS-2), linear perfluoropentane (OPLS-3), and branched perfluoropentane, or perfluoromethylbutane (OPLS-4). At the first stage, we compared the performance of all four parameter sets at reproducing the relative conformation energies of $(CF)_n$ monolayers from the preceding section. The parameter set for the branched molecule turned out to slightly outperform the other three sets (see Table 3), which seems reasonable since the material in question bears more structural resemblance to a branched molecule than to a linear one.

At the second stage, force field parameters were varied so as to achieve best reproduction of structural parameters of $(CF)_n$ in the chair conformation in a fully periodic 3D configuration (stacked layers). We used the above-described vdW-DF pro- cedure to obtain a quantum chemical benchmark. As it turned out, tuning only the equilibrium C−F and C−C bond length and the equilibrium C−C−C angle value turned out to be sufficient to achieve excellent performance of the force field (OPLS-5 in Table 3) not only for the structural parameters from vdW-DF, but for conformational energetics of monolayers, as well (in fact, the relative energies agree to within 1−3 meV per formula unit, which nears the numeric precision of quantum chemical calculations themselves). The optimized force field parameters are presented in Table 4.

<table>
<thead>
<tr>
<th>equilibrium parameter</th>
<th>OPLS/AA¹⁴</th>
<th>optimized value</th>
</tr>
</thead>
<tbody>
<tr>
<td>$R_{C-F}$ (Å)</td>
<td>1.332</td>
<td>1.3885</td>
</tr>
<tr>
<td>$R_{C-C}$ (Å)</td>
<td>1.529</td>
<td>1.5463</td>
</tr>
<tr>
<td>$\angle_{C-C-C}$ (°)</td>
<td>112.7</td>
<td>111.2</td>
</tr>
</tbody>
</table>

Finally, Table 5 compares results from unmodified OPLS/ AA and DFT calculations for graphane. It can be seen that the agreement between bond lengths and angles is satisfactory (within 0.5%. except for the C−H bond lengths, where the underestimation in molecular mechanics reaches 2%), and the relative energies of different conformations are reproduced less successfully.

<table>
<thead>
<tr>
<th>quantity</th>
<th>OPLS/AA</th>
<th>DFT</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E_{CH-W}$ (eV)</td>
<td>0.049</td>
<td>0.055</td>
</tr>
<tr>
<td>$E_{CH-B}$ (eV)</td>
<td>0.126</td>
<td>0.103</td>
</tr>
<tr>
<td>$a_{CH}$ (Å)</td>
<td>2.547</td>
<td>2.545</td>
</tr>
<tr>
<td>$R_{C-H}$ (Å)</td>
<td>1.092</td>
<td>1.112</td>
</tr>
<tr>
<td>$R_{C-C}$ (Å)</td>
<td>1.544</td>
<td>1.539</td>
</tr>
<tr>
<td>$\angle_{C-C-H}$ (°)</td>
<td>107.7</td>
<td>107.3</td>
</tr>
<tr>
<td>$\angle_{C-C-C}$ (°)</td>
<td>111.1</td>
<td>111.5</td>
</tr>
</tbody>
</table>

While quantum chemical calculations produce a single total energy value for a given atomic configuration, molecular mechanics calculates the total energy as a sum of partial two-, three-, and four-atom terms. This makes it possible to examine the conformational energetics of $(CF)_n$ and graphane in terms of bond stretching, angle bending, bond twisting, and Coulomb/ van der Waals forces. Analysis of partial contributions to the energy of strained conformations of $(CF)_n$ monolayers shows that for the washboard structure, the most significant contribution is from angle-bending terms (0.067 eV of the total 0.074 eV, or 91%). For the bed structure, all terms except Coulombic are considerable: bond stretching accounts for 0.025 eV of the total 0.147 eV (17%); angle bending, for 0.057 eV (39%); bond twisting, 0.013 eV (9%); most of the remaining strain energy comes from atomic overlap repulsion (0.065 eV, or 44%, of which 0.037 eV comes from third-neighbor interactions).

Examination of partial energy contributions for graphane results in a somewhat different picture. In both bed and washboard conformations, the strain energy is dominated by the bond twisting term. Another interesting difference is that for the washboard conformation, the third-neighbor van der Waals term is smaller than in the chair conformation, meaning that overlap repulsion for third-neighbor atoms in this structure is superseded by dispersion attraction; we attribute this effect to the smaller atomic radius of hydrogen atom compared to fluorine. We do not report detailed magnitudes of different terms here since the force field parameters have not been optimized for graphane (see Table 5).

### 3.3. Three-Dimensional Structures: Layer Stacking.
Mo- lecular mechanics parameters from the previous section were

![](./images/811798334573379585_3.jpg)

Figure 3. Three-dimensional packings of graphane layers in (a) bed and (b) washboard conformation. For (CF)ₙ, the packing motifs are identical.

used to generate initial structures for subsequent vdW-DF calculations of fully periodic 3D structures. Immediate applica- tion of the quantum-chemical method from the very beginning would be prohibitively expensive from the computational point of view, since for the lower-symmetry washboard and bed conformations, simple orthogonal arrangement of layers in the stack (AA stacking) is geometrically unstable with respect to lateral relative shift of consecutive layers. To obtain initial configurations, we prepared a set of systems with ABAB stacking in which the B layers were shifted in the horizontal plane by a vector (x, y), where each coordinate assumed values of 0, 1/4, or 1/2 of the corresponding lattice parameter (9 initial structures for each of the two strained conformations of (CF)ₙ and multilayer graphane, 36 configurations total). Each system was optimized using damped molecular dynamics. The resulting stable packings turned out to be perfectly analogous for (CF)ₙ and multilayer graphane. Figure 3 shows the final structures for the latter material.

Bed Conformation. For the bed conformation, all nine starting systems converged to the same final stacking shown in Figure 3a. There, consecutive layers are shifted by 1/2 of the unit cell in the Y direction (the armchair direction of the hexagonal carbon layer), and the shift along the X (zigzag) direction is zero. Therefore, the final ABAB stacked structure turns out to actually be monoclinic with basis vector angles (α, 90°, 90°) with α = 51.0° and 46.8° for (CF)ₙ and graphane, respectively (according to vdW-DF results presented below).

Washboard Conformation. For the washboard (gauche-chair) conformation, two stable structures were identified (termed in the following W1 and W2, see Figure 3b). Similarly to conformation B, the relative horizontal shift of consecutive layers is zero in the zigzag direction and assumes different nonzero values for the two stable packings in the armchair direction. Furthermore, a rich variety of other stacking patterns can be generated from these two packing motifs by taking alternating shift values and directions (positive or negative) for consecutive layers, ranging from monoclinic to aperiodic.

For all three stable packings of (CF)ₙ and graphane, vdW- DF structure optimizations were carried out using a two-step procedure. First, atomic coordinates and horizontal lattice parameters were optimized using standard DFT (ESPRESSO) at a fixed interlayer distance taken from molecular mechanics relaxations. At the second step, atomic coordinate optimizations were performed with ESPRESSO at a series of c lattice parameter values with fixed horizontal lattice parameters. The resulting electron densities were used to calculate the correlation energy using vdW-DF (JuNoLo), and the corrected energies were interpolated to give the final optimal values of total energy and c lattice parameter. The results of calculations for all systems are listed in Table 6.

First of all, it can be seen from Table 6 that the two stable packing motifs for the washboard conformation are essentially degenerate in energy (the difference is below 1 meV per formula unit). This means that the actual layer stacking of (CF)ₙ/graphane monolayers in this conformation would be highly disordered with respect to horizontal arrangement of layers.

As for the agreement between molecular mechanics and quantum chemical calculations, the following conclusions can be drawn from the data in Table 6. First, strain energies and lattice parameters are reproduced with an accuracy of 0.5−1% for the whole set of (CF)ₙ conformations, which can be considered a major success. The largest discrepancy is in the value of b lattice parameter of the bed conformation. This problem has a fundamental origin: it can be seen from Table 1 that this structure effectively contains two C−C bond types with substantially different lengths (1.574 and 1.667 Å); the molecular mechanics approach, in essence, tries to describe these two different bond types by a single set of parameters.

This problem does not appear in the case of graphane: the two C−C bond lengths in the bed conformation differ less strongly, and the corresponding molecular mechanics results for lattice parameters are in better agreement with quantum chemical data. The overall agreement between the two methods for horizontal lattice parameters in graphane is similar or even better than in (CF)ₙ. However, the interlayer distance is systematically underestimated in molecular mechanics calculations. This is obviously linked to the systematically longer C−H bonds in graphane compared to the value typical for alkanes (which is

<table>
<caption>TABLE 6: Results of Molecular Mechanics and vdW-DF Calculations for 3D Systems</caption>
<thead>
<tr>
<th>quantity</th>
<th>conformation (stacking)</th>
<th>MM CF</th>
<th>DFT</th>
<th>MM/DFT</th>
<th>MM CH</th>
<th>DFT</th>
<th>MM/DFT</th>
</tr>
</thead>
<tbody>
<tr>
<td>E (eV)</td>
<td>C</td>
<td>0.000</td>
<td>0.000</td>
<td></td>
<td>0.000</td>
<td>0.000</td>
<td></td>
</tr>
<tr>
<td></td>
<td>W1</td>
<td>0.0737</td>
<td>0.0731</td>
<td>100.8%</td>
<td>0.0520</td>
<td>0.0356</td>
<td>146%</td>
</tr>
<tr>
<td></td>
<td>W2</td>
<td>0.0736</td>
<td>0.0741</td>
<td>99.3%</td>
<td>0.0518</td>
<td>0.0355</td>
<td>146%</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>0.143</td>
<td>0.158</td>
<td>90.5%</td>
<td>0.122</td>
<td>0.094</td>
<td>130%</td>
</tr>
<tr>
<td>a (Å)</td>
<td>C</td>
<td>2.609</td>
<td>2.608</td>
<td>100.0%</td>
<td>2.542</td>
<td>2.544</td>
<td>99.9%</td>
</tr>
<tr>
<td></td>
<td>W1</td>
<td>2.625</td>
<td>2.632</td>
<td>99.7%</td>
<td>2.551</td>
<td>2.549</td>
<td>100.1%</td>
</tr>
<tr>
<td></td>
<td>W2</td>
<td>2.625</td>
<td>2.631</td>
<td>99.8%</td>
<td>2.551</td>
<td>2.549</td>
<td>100.1%</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>2.595</td>
<td>2.583</td>
<td>100.5%</td>
<td>2.547</td>
<td>2.534</td>
<td>100.5%</td>
</tr>
<tr>
<td>b (Å)</td>
<td>C</td>
<td>4.519</td>
<td>4.516</td>
<td>100.1%</td>
<td>4.403</td>
<td>4.407</td>
<td>99.9%</td>
</tr>
<tr>
<td></td>
<td>W1</td>
<td>4.158</td>
<td>4.202</td>
<td>99.0%</td>
<td>3.849</td>
<td>3.835</td>
<td>100.4%</td>
</tr>
<tr>
<td></td>
<td>W2</td>
<td>4.158</td>
<td>4.202</td>
<td>99.0%</td>
<td>3.849</td>
<td>3.834</td>
<td>100.4%</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>4.325</td>
<td>4.613</td>
<td>93.8%</td>
<td>4.345</td>
<td>4.314</td>
<td>100.7%</td>
</tr>
<tr>
<td>dᵃ (Å)</td>
<td>C</td>
<td>5.749</td>
<td>5.709</td>
<td>100.7%</td>
<td>4.508</td>
<td>4.674</td>
<td>96.4%</td>
</tr>
<tr>
<td></td>
<td>W1</td>
<td>6.098</td>
<td>6.053</td>
<td>99.3%</td>
<td>4.998</td>
<td>5.098</td>
<td>98.0%</td>
</tr>
<tr>
<td></td>
<td>W2</td>
<td>6.099</td>
<td>6.060</td>
<td>100.6%</td>
<td>5.005</td>
<td>5.098</td>
<td>98.1%</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>5.700</td>
<td>5.695</td>
<td>100.9%</td>
<td>4.467</td>
<td>4.595</td>
<td>97.2%</td>
</tr>
</tbody>
</table>

ᵃ Distance between layers. In the case of conformations W and B, the value corresponds to 1/2 of the actual lattice constant c value from the corresponding calculation.

taken as the equilibrium length in the OPLS/AA parameter set used for the calculations, hence the underestimation). It is also likely that precise reproduction of quantum chemical interlayer distance in graphane would require a modification of intermolecular interaction parameters for hydrogen. The latter statement is supported by the fact that the relative conformation energies in the 3D arrangement calculated using molecular mechanics are in even worse agreement with quantum chemical results than that for isolated layers.

### 3.4. Conformational Disorder in Real Materials: A Reality Check.
It has been suggested above that the existence of a disordered structure with alternating local conformation in $(CF)_n$ and graphane could provide an explanation of the fact that the observed lattice parameters of these materials are lower than the calculated values for the chair conformation, which is the structure usually assumed by default in the interpretation of experimental data. To be able to compare our structural models with raw experimental data directly, we undertook short molecular dynamics runs for the four 3D $(CF)_n$ structures and calculated atomic radial distribution functions (RDFs) for comparison with neutron diffraction results of Sato et al. $^{19}$ The simulations were carried out for 10 ps in the NPT ensemble at $T = 300$ K and $P = 1$ bar. At this point we should note that our optimization of molecular mechanics involved equilibrium bond lengths and angles only, leaving the corresponding force constants unchanged, which could possibly affect the dynamics of the systems in an important way. However, in the present context, this only concerns RDF peak widths and not their absolute positions.

The resulting radial distributions are shown in Figure 4a. The RDFs for all three conformations are visibly different. The plots for the two washboard conformation packings, $W1$ and $W2$, coincide up to the distance on the order of layer separation, $r \sim 5$ Å, which is to be expected since the geometrical structure of the layer themselves is the same in these cases.

The experimental data of Sato et al. $^{19}$ are plotted in Figure 4b. There, the red and blue lines correspond to $(CF)_n$ samples of different origin. Of these, the first one (red) was fabricated by the authors of the paper, while the second (blue) was purchased from industrial manufacturer. The commercial sample was reported to have lower crystallinity, smaller coherent scattering length, and larger interlayer distance.

To facilitate visual comparison, calculated RDF curves were additionally broadened (Gaussian broadening with 0.1 Å half-width) to match the experimental resolution. The results are shown in Figure 4c. The green line corresponds to the raw RDF of chair conformation. The same RDF after the broadening is shown in red. Finally, the blue line corresponds to a mixture of all three conformations (averaging of broadened RDFs with a "naïve" 1:1:1 weight distribution). It can be seen that the red and blue lines in Figure 4c reproduce the behavior of the red and blue experimental lines (4b) with an excellent qualitative agreement. In fact, up to $r \sim 5$ Å, all qualitative differences in the behavior of the two curves are the same in the two plots. The discrepancies at larger distances are probably due to the more chaotic layer packing in real samples compared to ideal model systems; another possible source of discrepancy could be layer buckling at conformation domain boundaries. This detailed agreement of simulation results with raw experimental data (not subjected to refinement involving any kind of a priori assumptions regarding the actual structure of the real material) is a strong indication that the presence of different conformations in the real 3D layered $(CF)_n$ material, in relative amounts that depend on fabrication conditions, can indeed serve as an explanation of the discrepancies between different experimental studies.

![](./images/811798334573379585_4.jpg)

Figure 4. Atomic radial distribution functions for carbon monofluoride: (a) raw simulation data for all four conformations/packings; (b) experimental data of Sato et al., $^{19}$ (c) broadened simulation data for chair-(CF)$_n$ and a mixture of all three conformations. Line colors in (c) and (b) suggest correspondence between the simulated RDFs (c) and the experimental curves obtained from two samples with different fabrication conditions$^{19}$ (b).

This conclusion appears physically sound when looking on the calculated energies, as well. According to our results, the relative energies of strained conformations are comparable to $kT$ under the conditions of synthesis of the material (up to $\sim$600 °C¹), making them energetically accessible even without taking into account entropic factors disfavoring a perfect chairlike structure. On the other hand, the height of potential barrier for the transition between bed and chair conformations calculated by Charlier et al.¹⁸ is much larger: 2.6 eV. Although this is, strictly speaking, an upper estimate, the isomerization mechanism suggested by the authors involves a concerted rupture of two $C-F$ bonds in the course of adatom exchange between two neighboring carbon atoms, which at any rate should require a

![](./images/811798334573379585_5.jpg)

Figure 5. A quasirandom structure that illustrates the lattice contraction effect resulting from conformational disorder and the presence of local domains with (anti)chair and washboard (gauche-chair) conformation: (a) schematic representation and (b) a fragment of molecular mechanics-optimized structure.

substantial amount of energy for activation, compared to the energy difference between the two conformations. On the basis of this reasoning, the formation of substantial percentage of stable regions with washboard and bed conformation in the process of material preparation seems plausible and even probable.

As a direct illustration of this idea, we provide an example of a simple quasirandom conformation-disordered graphane structure. The unit cell of the system, shown schematically in Figure 5a, contains a mixture of anti-chair ($C$) and gauche-chair ($W$) domains. The 12 $W$-type carbon atoms (each having two neighbors with adatoms on the same side of the layer as its own) are clustered in 2 hexagons, and a third hexagon contains 6 $C$-type carbon atoms. The resulting structure possesses overall trigonal symmetry. After geometry optimization using molecular mechanics (Figure 5b), the carbon layer becomes buckled, and the whole system contracts; the resulting lattice parameter of the system (divided by the number of hexagons in the respective direction) is 2.547 Å, or 98.6% that of perfect chairlike graphane. Although this is insufficient to explain the full amount of lattice contraction observed experimentally (92−95%,³ see Table 2), our quasirandom structure serves its duty as a simple proof of principle. In fact, the strain energy in this system is quite high, 0.248 eV per CH unit, which means that in real materials, some other types of arrangements should exist with even smaller lattice parameter values.

### 4.5. Interlayer Distance in $(CF)_n$.
In a final note, conformational and orientational disordering of layers could also contribute to the discrepancies in the experimentally observed interlayer distance values in $(CF)_n$. The possible mechanisms here are loose contact between layers due to orientation and conformation mismatch, as well as deviations from planarity around the borders of regions with differing conformation (buckling; see Figure 5b). A precise estimate of these effects would require extensive calculations; however, rough estimates of the strength of the former effect can already be drawn from the available data.

The first source of information is the difference of interlayer distance in between the optimal $AB$ and suboptimal orthogonal $AA$ stacking in the strained conformations. This corresponds to the magnitude of relaxation of lattice parameter $c$ in the optimization, which amounts to 0.41 for CF-$B$. Second, alternation of planar $B$ and $W$ layers can increase the interlayer distance further by $d_{CF-W} - d_{CF-B} = 0.4$ Å. The sum of these two "worst-case scenario" estimates gives us an upper estimate of the "swelling" due to alternating conformations of consecutive layers of about 0.8 Å, yielding a total maximum value of interlayer distance of $d_{CF} = d_{CF-W} + 0.8$ Å $= 6.9$ Å. This value already approaches some of the largest values reported in the experiments (which can range from 5.85 to 7.34 Å¹,¹⁹,²⁰).

Similar estimates for graphane result in even stronger correction magnitudes of 0.54 and 0.53 Å, respectively. The experimental data are lacking in this case, but on the basis of our calculations, interlayer distances of about 5−6 Å should be expected from future observations of multilayer graphane.

### 4. Conclusions
We have carried out a detailed computational study of conformational energetics of carbon monofluoride $(CF)_n$ and graphane monolayers, including a gauche-chair (washboard) conformation that has not been considered in the previous studies. On the basis of the results of quantum chemical calculations employing state-of-the-art nonlocal density functional theory formulation that adequately describes long-range dispersive correlation interactions between electrons, a molecular mechanics parameter set has been derived for $(CF)_n$ that is capable to accurately reproduce quantum chemical results for both the structure and the energy of different $(CF)_n$ conformations, as well as stacking patterns of monolayers in infinite 3D systems.

A direct comparison of experimentally observed atomic radial distribution functions and those calculated using molecular dynamics provides direct support for the suggestion that the structure of $(CF)_n$ is not limited to just the chair conformation (which is usually assumed during the interpretation of experimental data), but instead, regions with different conformations must coexist in the real material. The relative energies of these conformations support the possibility of the existence of stable gauche-chair and bed regions.

Such coexistence, dependent on the actual fabrication conditions of the material, provides a possible explanation for the discrepancies of in-layer lattice constant values reported in different experiments on $(CF)_n$ and graphane: the observed small values result from a substantial content of gauche-chair regions in the real materials, resulting in a pseudoperiodic structure with an "average" lattice constant smaller than that of chair conformation. Our suggestion is further supported by a simple illustrative example of a quasirandom conformation-disordered graphane structure, which does indeed demonstrate decreased lattice parameter, while at the same time preserving the overall trigonal symmetry of graphane sheet. Further, discrepancies in the interlayer spacing of $(CF)_n$ can be attributed to loose contact between mismatching layers, as well as to buckling at the boundaries between regions with different conformation. On the basis of such reasoning, we make a rough prediction for the interlayer distance in multilayer graphane: 5−6 Å, depending on the quality of samples.

In summary, the two materials are strongly structurally similar, demonstrating essentially parallel qualitative trends in structure and energetics. We hope that the possibility of explanation of inconsistency between previous theoretical works and experiment on a common basis for both materials will not only provide the scientific communities working with carbon monofluoride and graphane with a better understanding of their respective objects of study, but will also serve as an inspiration for graphane scientists to borrow and develop ideas coming from the fluorocarbon material industry. This especially concerns the fabrication of graphane, which presently remains an extremely challenging task, contrasting sharply with industrial-scale production of $(CF)_n$.

Acknowledgment. This work was supported by the Russian Foundation for Basic Research (projects 08-02-01096-a and 08-

03-00420-a). Computational facilities were provided by the Joint Supercomputer Center of the Russian Academy of Sciences (http://www.jscc.ru).

## References and Notes
(1) Mit'kin, V. N. *J. Struct. Chem.* **2003**, *44*, 82–115.

(2) Sofo, J. O.; Chaudhari, A. S; Barber, G. D. *Phys. Rev. B* **2007**, *75*, 153401.

(3) Elias, D. C.; Nair, R. R.; Mohiuddin, T. M. G.; Morozov, S. V.; Blake, P.; Halsall, M. P.; Ferrari, A. C.; Boukhvalov, D. W.; Katsnelson, M. I.; Geim, A. K.; Novoselov, K. S. *Science* **2009**, *323*, 610–613.

(4) Perdew, J. P.; Burke, K.; Ernzerhof, M. *Phys. Rev. Lett.* **1996**, *77*, 3865. Perdew, J. P.; Burke, K.; Ernzerhof, M. *Phys. Rev. Lett.* **1997**, *78*, 1396.

(5) Haas, P; Tran, F.; Blaha, P. *Phys. Rev. B* **2009**, *79*, 085104.

(6) Gonze, X.; Beuken, J.-M.; Caracas, R.; Detraux, F.; Fuchs, M.; Rignanese, G.-M.; Sindic, L.; Verstraete, M.; Zerah, G.; Jollet, F.; Torrent, M.; Roy, A.; Mikami, M.; Ghosez, Ph.; Raty, J.-Y.; Allan, D. C. *Comput. Mater. Sci.* **2002**, *25*, 478–492.

(7) Blöchl, P. E. *Phys. Rev. B* **1994**, *50*, 17953.

(8) Quantum-ESPRESSO is a community project for high-quality quantum-simulation software, based on density-functional theory, and coordinated by Paolo Giannozzi. See http://www.quantum-espresso.org and http://www.pwscf.org.

(9) Vanderbilt, D. *Phys. Rev. B* **1990**, *41*, 7892.

(10) Thonhauser, T.; Cooper, V. R.; Li, S.; Puzder, A.; Hyldgaard, P.; Langreth, D. C. *Phys. Rev. B* **2007**, *76*, 125112.

(11) Dion, M.; Rydberg, H.; Schröder, E.; Langreth, D. C.; Lundqvist, B. I. *Phys. Rev. Lett.* **2004**, *92*, 246401.

(12) Laziæ, P.; Atodiresei, N.; Alaei, M.; Caciuc, V.; Blugel, S.; Brako, R. *arXiv* **2008**, 0810.2273v1, [cond-mat.mtrl-sci].

(13) Ziambaras, E.; Kleis, J.; Schröder, E.; Hyldgaard, P. *Phys. Rev. B* **2007**, *76*, 155425.

(14) Kleis, J.; Schröder, E.; Hyldgaard, P. *Phys. Rev. B* **2008**, *77*, 205422.

(15) van der Spoel, D.; Lindahl, E.; Hess, B.; Groenhof, G.; Mark, A. E.; Berendsen, H. J. C. *J. Comput. Chem.* **2005**, *26*, 1701.

(16) Watkins, E. K.; Jorgensen, W. L. *J. Phys. Chem. A* **2001**, *105*, 4118–4125.

(17) Jorgensen, W. L.; Maxwell, D. S.; Tirado-Rives, J. *J. Am. Chem. Soc.* **1996**, *118*, 11 22511 236.

(18) Charlier, J.-C.; Gonze, X.; Michenaud, J.-P. *Phys. Rev. B* **1993**, *47*, 16 16216 168.

(19) Sato, Y.; Itoh, K.; Hagiwara, R.; Fukunaga, T.; Ito, Y. *Carbon* **2004**, *42*, 2897.

(20) Giraudet, J.; Dubois, M.; Guérin, K.; Delabarre, C.; Hamwi, A.; Masin, F. *J. Phys. Chem. B* **2007**, *111*, 14143.

(21) Flores, M. Z. S.; Autreto, P. A. S.; Legoas, S. B.; Galvao, D. S. *Nanotechnology* **2009**, *20*, 465704.

(22) Samarkoon, D. K.; Wang, X.-Q. *ACS Nano* **2009**, *3*, 4012–4022.

JP1003566