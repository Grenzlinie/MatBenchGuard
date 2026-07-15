# Mail-Order Metal-Organic Frameworks (MOFs): Designing Isoreticular MOF-5 Analogues Comprising Commercially Available Organic Molecules

Richard L. Martin, $^\dagger$ Li-Chiang Lin, $^\ddagger$ Kuldeep Jariwala, $^\S$ Berend Smit, $^{\ddagger,\S,\parallel}$ and Maciej Haranczyk$^{*, \dagger}$

$^\dagger$Computational Research Division, Lawrence Berkeley National Laboratory, One Cyclotron Road, Mail Stop 50F-1650, Berkeley, California 94720-8139, United States

$^\ddagger$Department of Chemical and Biomolecular Engineering, University of California, Berkeley, California 94720, United States

$^\S$Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, California 94720-8139, United States

$^{\parallel}$Department of Chemistry, University of California, Berkeley, California 94720, United States

**Supporting Information**

## ABSTRACT:
Metal−organic frameworks (MOFs), a class of porous materials, are of particular interest in gas storage and separation applications due largely to their high internal surface areas and tunable structures. MOF-5 is perhaps the archetypal MOF; in particular, many isoreticular analogues of MOF-5 have been synthesized, comprising alternative dicarboxylic acid ligands. In this contribution we introduce a new set of hypothesized MOF-5 analogues, constructed from commercially available organic molecules. We describe our automated procedure for hypothetical MOF design, comprising selection of appropriate ligands, construction of 3D structure models, and structure relaxation methods. 116 MOF-5 analogues were designed and characterized in terms of geometric properties and simulated methane uptake at conditions relevant to vehicular storage applications. A strength of the presented approach is that all of the hypothesized MOFs are designed to be synthesizable utilizing ligands purchasable online.

![](./images/813235403430559747_1.jpg)

## INTRODUCTION
Metal−organic frameworks$^1$ (MOFs) are a class of porous materials comprised of metal or metal oxide vertices interconnected by organic bridging ligands. MOFs have enjoyed considerable research interest due largely to their open pore structures and very high internal surface areas.$^{2,3}$ Accordingly, MOFs are regarded as promising candidates for a number of critical energy-related applications, such as gas separations$^4$ including carbon capture,$^5$ hydrogen and natural gas storage,$^6$ and catalysis.$^7$ In a paradigm known as *reticular chemistry*, $^8$ the constituent metal or organic components of a MOF can be substituted for alternative chemical species. The properties of MOF materials can therefore be controlled by the selection of building blocks with the appropriate chemistry. The reticular approach illustrates that a significantly vast number of MOF materials are possible; however, this combinatorial complexity makes the discovery of MOFs with targeted properties a serious challenge.

The chemical space of possible MOFs is typically explored through the enumeration of building blocks and the exhaustive design of possible structures with a specific topology prescribed by the connectivity of the components. The archetypal MOF, and one of the most studied, $^9$ is isoreticular (IR) MOF-1, or MOF-5.$^{10}$ Isoreticular structural analogues of MOF-5 have been explored both experimentally$^{11}$ and computationally.$^{12}$ The simple, three-dimensional lattice structure of MOF-5 (pcu net$^{13}$) permits a high degree of structural variance through substitution of the constituent benzene-1,4-dicarboxylic acid for various alternative dicarboxylic acids. Typically, a single, symmetric acid molecule is used, to avoid disorder; however, recent work has explored the possibility of MOF-5 analogues comprising multiple distinct ligands.$^{14}$

In enumerating possible MOF materials, an important question is how to select an appropriate database of ligands. In the highlight study in this area, Wilmer et al. analyzed a space of possible MOF crystal structures achievable by combining metal and organic components previously utilized in the literature and permitting additional ligand functionalization;$^{15}$ their approach has enumerated approximately 137 000 hypothetical MOF structures.

In the current contribution, we present an alternative approach to MOF design, emphasizing the selection of appropriate ligands to achieve a database of readily synthesizable structures. By designing MOFs that incorporate commercially available molecules, we aim to achieve a select set of materials that can be realized without the need for synthesis of organic ligands. Focusing on isoreticular analogues of MOF-5, our approach has four main steps. (1) We explore databases of commercially available molecules$^{16}$ to identify those that fulfill the most basic requirements of MOF building blocks. (2) We then select only

---
Received: February 24, 2013
Revised: March 29, 2013
Published: April 1, 2013

![](./images/813235403430559747_2.jpg)
© 2013 American Chemical Society
12159
dx.doi.org/10.1021/jp401920y | J. Phys. Chem. C 2013, 117, 12159−12167

those ligands that are sufficiently rigid and linear and construct three-dimensional models of isoreticular MOF crystal structures. (3) We optimize the materials and remove highly distorted, unrealistic structures. (4) Finally, we characterize the resulting structures in terms of their geometric properties and simulated methane uptake at conditions relevant to vehicular methane storage applications. In the following, we elaborate on these steps and describe our database of hypothetical MOF materials that are ready to be assembled from organic components purchasable online.

## METHODS
Our workflow for enumerating and characterizing hypothetical MOF-5 analogues comprises several refining steps, as follows:

1.  Identify commercial dicarboxylic acids as potential linker molecules;
2.  Remove molecules that exhibit salts, too many atoms, etc.;
3.  Remove molecules exhibiting a flexible backbone between carboxylic acid functional groups and impose linear ligand conformations;
4.  Assemble all possible MOFs from rigid building units in the MOF-5 topology (pcu net), removing MOFs which exhibit collisions between building units;
5.  For each ligand, keep only the MOF structures exhibiting sufficiently dissimilar pore geometries, to prevent redundant calculations;
6.  Optimize MOF structures and remove those exhibiting infeasible geometry or nonporous structures;
7.  Characterize and simulate methane uptake in the resulting materials.

Steps 1–3 are described in Ligand Selection; Steps 4–6 are described in MOF Construction and Selection; and Step 7 is described in Structure Characterization.

Ligand Selection. MOF-5 analogues were systematically enumerated by substituting the constituent linear benzene-1,4-dicarboxylic acid ligands (Figure 1) for various commercially available dicarboxylic acids. As such, the pcu net of MOF-5 and the $Zn_4O$ secondary building units are preserved. However, to achieve this, only sufficiently linear and rigid ligands can be used in the substitution. Here we describe our automated process for selecting appropriate linkers for rigid MOF construction.

We identified dicarboxylic acid molecules in the eMolecules database$^{16}$ by applying the textual SMARTS$^{17}$ filter $[CX3](=O)[OX2H1]$ in the Open Babel software package.$^{18}$ Molecules consisting of salts, solvents, charged atoms, greater than 100 total atoms, or disconnected chemical fragments were rejected in this search. Overall, 2914 ligands satisfying these preliminary criteria were identified. However, although all ligands exhibit a structure of the form $HOOC-R-COOH$, many are not acceptable candidates for rigid MOF construction. In particular, commercially available dicarboxylic acids are in general not linear in their lowest energy conformation and are often quite flexible. Therefore, a critical step in our process is to select ligands that are appropriate for rigid MOF construction. Accordingly, we removed highly flexible and nonlinear molecules according to the following multistep procedure.

The Merck Molecular Force Field $94^{19}$ was utilized in the KNIME software package$^{20}$ to generate ten distinct conformers for each ligand (with the conformer diversity parameter in KNIME set to 0.5, allowing a high degree of conformational variance). The distance between the carbon atoms of the two carboxylic acid functional groups in each conformer was calculated, as an approximated index of conformational flexibility; any ligand exhibiting a greater than 0.65 Å deviation in observed carbon−carbon distance between conformers was rejected as being too flexible. This selection criterion accepts only ligands with a rigid backbone between carboxylic acid functional groups but permits the existence of flexible side chains. 1183 ligands remained after this flexibility cutoff was imposed, and their minimum energy conformations were selected.

The remaining ligands were subsequently modified from their lowest energy conformer to impose a linear arrangement; carboxylic acid functional groups were rotated about the adjacent carbon atom of the molecule to face in an opposite direction to one another (Figure 2). 345 ligands were successfully modified in this manner, the remainder being rejected due to collisions arising between constituent atoms. Having identified the most likely candidate ligands for rigid MOFs, we proceeded to construct three-dimensional models of MOF crystal structures incorporating these molecules.

$$
\mathrm{HOOC-C6H4-COOH}
$$

Figure 1. Benzene-1,4-dicarboxylic acid, the linear ligand utilized in MOF-5.

![](./images/813235403430559747_3.jpg)

Figure 2. (a) Dicarboxylate ligand in minimum energy conformation. (b) The same ligand after modification to align carboxylate groups to face in opposing directions to one another.

MOF Construction and Selection. The enforced ligand linearity allows MOFs to be automatically constructed by simply assembling the rigid metal and ligand building blocks in the pcu net conformation. MOFs were constructed from each of these 345 ligands, and their structures were then analyzed for atomic collisions. For example, the use of ligands with long side chains can cause overlap between atoms of the ligand and other components. 234 ligands resulted in MOFs with acceptable geometries.

MOF structures with distinct geometry are obtained depending on the orientation and direction in which the rigid building blocks are used to computationally generate the crystal structure. Accordingly, many distinct crystal structures can be obtained for

a single ligand; this effect is most pronounced for asymmetrical molecules, and in practice such structures may prove disordered. However, the effect of disorder can be considered by comparing the distinct structures of MOFs constructed from a single ligand. For each ligand, we used an automated procedure to compare the pore geometry of each MOF achieved. By abstracting structural geometry using Voronoi holograms,²¹ the similarity between overall shapes of pore networks can be automatically quantified by comparing these descriptors. Following the method described in reference 21, methane-accessible pore networks were determined for each MOF, and structures exhibiting a pore shape similarity score greater than 0.5 were rejected. By rejecting structures in this way, we avoid the inclusion of multiple structures based on the same ligand if they exhibit very similar pores. In all cases, it was determined that the various crystal structures obtained for each ligand were very similar. Accordingly, all but a single MOF per ligand were removed; the first MOF structure achieved with each ligand was selected arbitrarily. We note that although this pore shape similarity step removed all but one structure for each ligand it is a critical step in our workflow because (a) removing redundant material conformers avoids unnecessary further computational analysis of these materials and (b) sufficiently shape distinct conformers may in general occur within material data sets.

After eliminating geometrically redundant structures in this way, 234 MOF-5 analogues (i.e., arising from 234 distinct ligands) were achieved. However, since the constituent ligands had been forced into a linear conformation prior to framework assembly, it was necessary to relax the structures to achieve realistic framework geometry. All MOFs were relaxed using the semiempirical PM6-DH2 approach,²² and unit cell parameters were also permitted to relax. The PM6-DH2 method has been parametrized to minimize error with respect to density functional theory (DFT) calculations (average error in selected heat of formation calculations is 4.4 kcal mol⁻¹) and includes empirical corrections for dispersion interaction. The resulting crystal structures preserve the topology of MOF-5 while allowing for ligands that are not perfectly linear; hence, the crystallographic symmetry of MOF-5 is not preserved.

In certain cases, the imposition of linearity on the ligands results in MOFs with high enough strain that structural relaxation heavily distorts the structure. This distortion is typically manifested in a nontetrahedral Zn₄O building unit. Accordingly, a geometrical filter was imposed such that MOFs containing Zn₄O clusters with a higher than 0.07 tetrahedrality index²³ were rejected. Tetrahedrality index $T$

$$
T = \sum_{i}^{5} \sum_{j>i}^{6} \frac{(d_{i} - d_{j})}{15 \bar{d}^{2}} \tag{1}
$$

measures distortion from a regular tetrahedron, where $d_{i}$ and $d_{j}$ are the lengths of edges $i$ and $j$ of the tetrahedron and $\bar{d}$ is the mean edge length. Higher $T$ values indicate greater deviation in edge length from the mean, i.e., greater tetrahedral distortion. An example of a highly distorted Zn₄O building unit exhibiting $T$ = 0.18 (i.e., rejected by this criterion since $T$ > 0.07) and a low distortion Zn₄O unit ($T$ = 0.01) are provided in the Supporting Information (Figure S1). With this final quality control step, a total of 116 distinct MOF-5 analogue structures were achieved. These structures were organized into two sets based on the R group in their constituent $^{-}$OOC−R−COO⁻ dicarboxylate ligand. The first set, Hc set, consists of 30 structures based on ligands in which the R group is a hydrocarbon. The second set consists of 86 structures in which the R group contained heteroatoms and is named Ha. In the following discussion, structures are referenced by an X−Y naming convention, where X is either Hc or Ha, reflecting which set the material belongs to, and Y is the identification number of the ligand, with respect to the original set of 2914 molecules. We note that within this data set of 116 commercially available ligands there is a degree of overlap with ligands examined by Wilmer et al.;¹⁵ 12 Hc ligands occur in the set from reference 15, while a further three (one Hc and two Ha) may be present, depending on the specific positions of chemical functionalization.

Structure Characterization. The generated structures were characterized in terms of geometrical parameters describing their pores. Pore descriptors such as the largest diameter of included $(D_{i})$ and free $(D_{f})$ spheres, methane accessible volume (AV), and methane accessible surface area (ASA) were calculated using our Zeo++ code.²⁴ In these calculations, atomic radii from the Cambridge Crystallographic Data Centre²⁵ were utilized, and the probe radius was set to 1.625 Å, representing methane. The Monte Carlo sampling of AV (ASA) comprised 100 000 (3000) random samples per unit cell (per atom). Of the 116 structures, five were found to be nonporous with respect to methane, and the remainder of the discussion concerns the remaining 111 material structures.

As our protocol for generation of structures involves the semiempirical PM6-DH2 method, which to the best of our knowledge has not previously been used in the context of modeling of MOFs, we decided to further validate structures relaxed with PM6-DH2 by comparison to those relaxed with higher level electronic structure calculations. We have compared selected structures with ones optimized by DFT calculations, which were performed in the QuantumEspresso²⁶ implementation. In this study, the PBE gradient-correlated exchange-correlation functional and norm-conserving Trouller−Martins pseudopotentials were adopted. The kinetic energy cutoff of wave functions and charge density were set to be 120 Ry and 480 Ry, respectively, and the integration over the irreducible Brillouin zone was carried out over 2 × 2 × 2 Monkhorst−Pack grids. The structure optimizations were considered as converged until all components of force on each atom were smaller than 10⁻³ Ry/ Bohr.

For each of the 111 methane-accessible MOFs successfully constructed according to the previously described procedures, we performed grand canonical Monte Carlo (GCMC) simulation to determine their potential for methane storage applications.²⁷ The US Department of Energy targets a volumetric methane uptake of 180 cm³_STP/cm³ (i.e., V_STP/V) at $T$ = 298 K and $P$ = 35 bar, which was the condition we used in the calculations. In the GCMC simulations, the framework was regarded as rigid, and periodic boundary conditions were applied. The simulation box was composed of multiple unit cells with the distance in each perpendicular direction at least twice the cutoff radius ($R_{\text{cut}}$ = 12 Å). The 12-6 Lennard-Jones potential model was adopted to describe the intermolecular interaction energies, in which we used the universal force field²⁸ for the framework atoms and the TraPPE model²⁹ for the methane molecule with the Lorentz−Berthelot mixing rule to predict all the pairwise parameters. For each simulation, several million configurations through random translation, deletion, insertion, and regrow moves were sampled to obtain statistically accurate ensemble averages.

![](./images/813235403430559747_4.jpg)

Figure 3. Comparison of the methane adsorption isotherms at 298 K between unrelaxed and relaxed structures composed from the linker (a) Hc16 and (b) Ha469. The illustration of the selected linker is presented in the inset.

Table 1. Geometric Properties of Structures Hc16 and Ha469, before and after Each Relaxation Technique

<table>
<thead>
<tr>
<th>structure</th>
<th>relaxation method</th>
<th>void fraction</th>
<th>D<sub>i</sub> (Å)</th>
<th>D<sub>f</sub> (Å)</th>
<th>absolute ASA (Å²)</th>
<th>gravimetric ASA (m² g⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hc16</td>
<td>unrelaxed</td>
<td>0.421</td>
<td>12.01</td>
<td>7.57</td>
<td>605.9</td>
<td>2972.8</td>
</tr>
<tr>
<td></td>
<td>PM6-DH2</td>
<td>0.442</td>
<td>12.13</td>
<td>8.08</td>
<td>657.5</td>
<td>3225.9</td>
</tr>
<tr>
<td></td>
<td>DFT</td>
<td>0.444</td>
<td>12.57</td>
<td>7.97</td>
<td>659.2</td>
<td>3234.2</td>
</tr>
<tr>
<td>Ha469</td>
<td>unrelaxed</td>
<td>0.342</td>
<td>13.54</td>
<td>5.74</td>
<td>802.0</td>
<td>2473.0</td>
</tr>
<tr>
<td></td>
<td>PM6-DH2</td>
<td>0.350</td>
<td>12.95</td>
<td>6.56</td>
<td>863.0</td>
<td>2661.3</td>
</tr>
<tr>
<td></td>
<td>DFT</td>
<td>0.363</td>
<td>12.75</td>
<td>6.14</td>
<td>887.5</td>
<td>2736.6</td>
</tr>
</tbody>
</table>

## RESULTS

### Structural Properties.
Our study has resulted in 111 methane-accessible isoreticular MOF-5 structures, available in the Supporting Information as well as deposited at www.carboncapturematerials.org database. Our study commenced with a validation of the approach used to generate and predict 3D structures of materials. In particular, we investigated the quality of MOF geometries predicted by the semiempirical PM6-DH2 approach, by comparison to geometries predicted by DFT. We selected the two structures, one from each set, which exhibited the largest accepted distortion measured by the tetrahedrality index (eq 1). The structure based on linker Hc16 has $T = 0.064$, and the structure based on linker Ha469 has $T = 0.065$ (insets of Figure 3). PM6-DH2-relaxed and DFT-relaxed structures were achieved by applying each method to the initial structures, constructed based on the rigid geometrical approximation described above.

Parameters describing pore geometries of Hc16 and Ha469 before and after relaxation are provided in Table 1. Although the geometrical parameters describing pores in PM6-DH2-relaxed, DFT-relaxed, and initial structures are quite similar, we observed that both relaxed structures have lower CH₄ uptake in the entire range of the investigated pressures (Figure 3). This effect can be attributed to the small increase in volume exhibited in the relaxed unit cells with respect to the initial unit cells for these structures, leading to a reduction in framework density. This justifies the need for a relaxation step during our structure generation procedure. Remarkably, CH₄ adsorption isotherms for both PM6-DH2 and DFT-relaxed structures present a nearly perfect agreement. This agreement, achieved for structures exhibiting the highest permitted tetrahedral distortion in Zn₄O units following PM6-DH2 relaxation, supports the choice of the computationally less expensive PM6-DH2 method. The computational time required for PM6-DH2 relaxation of Hc16 and Ha469 was, respectively, 2 and 8 min using a single CPU, whereas approximately total 20 h and 24 CPUs were required to relax these two structures using DFT.

Having verified that the PM6-DH2-relaxed MOF structures are reliable, we proceed with characterization of geometrical parameters of all generated structures in the Hc and Ha sets. The Hc set (30 MOF materials) and the Ha set (86) exhibit a wide range of pore sizes. One structure in the Hc set and four in the Ha set exhibit restricting pore apertures too small to permit the diffusion of a CH₄ molecule into the structure and therefore were excluded from further study. The ranges of geometric properties of the remaining Hc (29) and Ha (82) materials are summarized in Table 2.

Table 2. Range of Geometric Properties in PM6-DH2-Relaxed Structures

<table>
<thead>
<tr>
<th>set</th>
<th>property</th>
<th>D<sub>i</sub> (Å)</th>
<th>D<sub>f</sub> (Å)</th>
<th>volumetric ASA (m² cm⁻³)</th>
<th>gravimetric ASA (m² g⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hc</td>
<td>largest</td>
<td>25.49</td>
<td>25.49</td>
<td>2931.06</td>
<td>5945.28</td>
</tr>
<tr>
<td></td>
<td>smallest</td>
<td>7.15</td>
<td>3.19</td>
<td>1250.10</td>
<td>2110.63</td>
</tr>
<tr>
<td>Ha</td>
<td>largest</td>
<td>31.31</td>
<td>20.76</td>
<td>2652.59</td>
<td>6871.72</td>
</tr>
<tr>
<td></td>
<td>smallest</td>
<td>6.13</td>
<td>2.53</td>
<td>916.81</td>
<td>1469.58</td>
</tr>
</tbody>
</table>

### Methane Adsorption.
As an example of how our database can be used for practical applications, we characterized the resulting set of 29 Hc and 82 Ha methane-accessible MOFs to indentify the best linkers for methane storage application. We focused on predicting CH₄ uptake at a pressure of 35 bar in the search for structures meeting DOE target specifications. Data on the highest volumetric and gravimetric uptake structures are provided in Table 3.

We observe that several structures approach the 35 bar 180 $V_{STP}$/V target. CH₄ adsorption isotherms for the three best performing structures in each set are presented in Figure 4. We observe that the best performing structures in each set are comprised of very similar ligands (Figure 5), one benzene ring in length but wide, due to additional benzene rings or functionalization. These results indicate that the highest volumetric uptake is likely to be achieved with similar linkers: short, to allow for the smallest possible unit cells, and wide, to

Table 3. Highest Volumetric and Gravimetric Methane Uptake Structures in Each Set (Simulated at 35 bar)

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">volumetric</th>
      <th colspan="2">gravimetric</th>
    </tr>
    <tr>
      <th>set</th>
      <th>highest uptake ($V_{STP}/V$)</th>
      <th>structure</th>
      <th>highest uptake (mol kg⁻¹)</th>
      <th>structure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Hc</td>
      <td>178.87</td>
      <td>Hc2075</td>
      <td>16.14</td>
      <td>Hc2558</td>
    </tr>
    <tr>
      <td>163.78</td>
      <td>Hc1821</td>
      <td>14.18</td>
      <td>Hc2368</td>
    </tr>
    <tr>
      <td>162.05</td>
      <td>Hc145</td>
      <td>14.15</td>
      <td>Hc646</td>
    </tr>
    <tr>
      <td rowspan="3">Ha</td>
      <td>157.06</td>
      <td>Ha64</td>
      <td>18.83</td>
      <td>Ha779</td>
    </tr>
    <tr>
      <td>153.73</td>
      <td>Ha1426</td>
      <td>17.63</td>
      <td>Ha1589</td>
    </tr>
    <tr>
      <td>153.48</td>
      <td>Ha712</td>
      <td>14.95</td>
      <td>Ha1239</td>
    </tr>
  </tbody>
</table>

increase surface area. Exploration of different MOF topologies with similar linkers may provide structures that exceed this target. The best uptake structures are found in the Hc set; we postulate that is simply because the fused benzene ring shapes present in this set of commercially available molecules most closely match the simplistic, optimum ligand shape.

Significantly different optimum ligand shapes are observed with respect to 35 bar gravimetric uptake (Figure 6). Since all structures are of the same topology, the highest gravimetric uptake is achieved with structures that maximize the surface area contribution from lightweight components, i.e., structures comprised of long ligands. Also in contrast to the volumetric measure, the best gravimetric uptake structures are found in the Ha set. As illustrated in Figure 6, long molecules can be achieved by incorporating nitrogen atoms and will be of lower mass than molecules in the Hc set that are extended through addition of benzene rings. Although high gravimetric surface area structures may be achievable with hypothetical Hc molecules comprising arbitrarily long acetylene fragments (including branches),³⁰ molecules containing multiple acetylenes are not present in the set of commercially available molecules. Indeed, the presence of commercially available molecules extended through addition of heteroatoms such as nitrogen indicates that this may be an easier synthetic route to achieving high gravimetric surface area frameworks than acetylene extension.

Completion of characterization of our database of MOF-5 analogues gives an opportunity to investigate structure−property relationships. The relationships between CH₄ adsorption properties (volumetric and gravimetric uptake at 1 bar, 35 bar, and Henry coefficients, as well as heats of adsorption) and geometrical descriptors (void fraction, gravimetric AV, and volumetric and gravimetric ASA) are illustrated in Figure 7 and the Supporting Information. In terms of volumetric methane adsorption performance, we observe that void fraction exhibits a striking negative correlation with adsorption properties at low pressure: uptake at 1 bar (Figure S2a, Supporting Information), Henry coefficient (Figure S3a, Supporting Information), and heat of adsorption (Figure S4a, Supporting Information); the best performing structures in these criteria consistently exhibit low void fraction. By contrast, at 35 bar a clear optimum void fraction of approximately 0.3 is observed (Figure 7a). There is no clear relationship between volumetric uptake and volumetric ASA at high pressure (Figure 7c). At low pressure, high uptake (Figure S2c, Supporting Information), Henry coefficient (Figure S3c, Supporting Information), and heat of adsorption (Figure S4c, Supporting Information) are achieved with ASA in the approximate range of 1500−2500 m² cm⁻³. However, this is not a strong correlation, as many structures within this property range also exhibit small low-pressure uptake, and it appears that volumetric ASA does not directly influence low-pressure uptake.

In terms of gravimetric methane adsorption performance, a strong correlation indicates that the highest uptake at 35 bar is achieved for structures exhibiting high gravimetric AV (Figure 7b) and ASA (Figure 7d). At 1 bar, a strong correlation with geometric properties does not occur; however, we can observe that structures with low gravimetric AV (Figure S2b, Supporting Information) and ASA (Figure S2d, Supporting Information) achieve the highest uptake; there is considerable agreement between the plots of uptake at 1 bar (Figure S2b,d, Supporting Information) and Henry coefficient (Figure S3b,d, Supporting Information). Heat of adsorption is observed to behave similarly; however, there is a considerably stronger correlation between low gravimetric AV (Figure S4b, Supporting Information) and ASA (Figure S4d, Supporting Information) and high heat of adsorption. We can rationalize these observations by noting that since all structures exhibit the same topology. Low gravimetric AV and ASA will occur in structures with small pores, which will be favorable for methane adsorption at low pressures (i.e., uptake, Henry coefficient, and heat of adsorption).

We note that certain trends observed herein for our hypothetical MOF-5 analogues differ from those presented in ref 15. For example, we observe a peak of volumetric uptake (Figure 7a) at a methane void fraction of about 0.3 (compared to 0.8 helium void fraction). Additionally, the largest volumetric CH₄ uptakes (Figure 7c) are observed across a range of volumetric ASA from 1500 to 2500 m² cm⁻³ (compared to 2000−3000 m² cm⁻³). However, the hypothetical MOFs of ref 15 contain materials with a range of topologies and diverse ligands. Therefore, observing deviation between these sets of MOFs is not surprising.

We can also observe the relationship between gravimetric and volumetric methane uptake in our data set. At 35 bar, these objectives clearly compete, and no candidate material exhibits a

![](./images/813235403430559747_5.jpg)

Figure 4. Methane adsorption isotherms for the three highest volumetric uptake structures: (a) Hc set and (b) Ha set.

![](./images/813235403430559747_6.jpg)

Figure 5. Ligands from the three highest 35 bar volumetric uptake structures: (a) Hc2075; (b) Hc1821; (c) Hc145; (d) Ha64; (e) Ha1426; and (f) Ha712.

![](./images/813235403430559747_7.jpg)

Figure 6. Ligands from the three highest 35 bar gravimetric uptake structures: (a) Hc2558; (b) Hc2368; (c) Hc646; (d) Ha779; (e) Ha1589; (f) Ha1239.

clear compromise between gravimetric and volumetric uptake. The maximum volumetric uptake occurs within the range of 8–12 mol/kg, an intermediate range of the gravimetric uptake (Figure 8b). We note the intuitive similarity between this result and the relationship between volumetric uptake and the methane

void fraction (Figure 7a); highly porous materials (i.e., lower density and higher void fraction) generally exhibit higher gravimetric uptake at high pressure, resulting in a lower volumetric uptake since the void space inside the structure per unit volume cannot be efficiently packed with methane

![](./images/813235403430559747_8.jpg)

Figure 7. Correlations between methane uptake at 35 bar and 298 K and geometric properties of structures in the Hc (comprising ligands whose R groups contain only hydrogen and carbon atoms) and Ha (R groups contain other elements) set: (a) volumetric uptake and methane void fraction; (b) gravimetric uptake and AV; (c) volumetric uptake and ASA; (d) gravimetric uptake and ASA.

![](./images/813235403430559747_9.jpg)

Figure 8. Correlations between gravimetric and volumetric methane uptake at 298 K in the Hc (ligands with only hydrogen and carbon atoms, other than carboxylate groups) and Ha (ligands containing other elements) sets at a pressure of: (a) 1 bar and (b) 35 bar.

molecules. At 1 bar, however, we observe that it is possible to achieve both high gravimetric and volumetric uptake (Figure 8a) since the adsorbed amount is dominated by the local geometry features. We note that for practical methane storage applications a high uptake at low pressure is detrimental to the working capacity of a device.

Finally, we also compared the present commercial prices of each ligand considered in this work with the geometric and methane adsorption properties of the resulting isoreticular frameworks (see Supporting Information, Figures S5 and S6). We normalized the prices listed in the eMolecules database³¹ to achieve the minimum price per gram of each ligand. We emphasize that these prices will not reflect the actual cost of purchases nor reflect the cost of large-scale, commercial-scale, or other high-volume purchase or production. A remarkably broad range of prices are observed, from approximately 0.01USD to over 170 000USD per gram. It is apparent that there is no bias in the observed price of ligands with respect to either geometric or methane adsorption properties of the resulting isoreticular MOF.

However, we note that the highest performing materials with respect to gravimetric methane uptake comprise ligands of intermediate cost and that high volumetric methane uptake can be achieved with MOFs comprising inexpensive ligands.

### CONCLUSIONS

We have presented a procedure by which a series of isoreticular MOF-5 analogues can be constructed from a database of commercially available dicarboxylic acid ligands. This procedure consists of the following steps: (i) potential ligands are investigated by means of conformational analysis to remove flexible molecules; (ii) rigid ligands are modified to achieve linear alignment of COOH groups, as observed in MOF-5; (iii) 3D structures of MOFs are built from these ligands using geometry transformations; (iv) these structures are relaxed using the semiempirical PM6-DH2 method; (v) the set is pruned to remove heavily distorted MOFs.

Following this procedure, the most likely candidate ligands for MOF synthesis were selected from a set of 2914 commercially

available dicarboxylic acids, and a database of the 116 most feasible MOF-5 analogues was constructed. By selectively constructing frameworks in this manner, our set comprises all MOF-5 analogues that can be theoretically assembled from ligands currently purchasable online and hence represents frameworks that can be constructed without the requirement for identifying synthetic routes for achieving ligands.

We have illustrated the bounds of methane storage performance achievable through the use of such readily available organic components by characterization of their pore geometry as well as methane uptake at conditions relevant to vehicular storage. Comparing adsorption performance to the approximate present commercial prices of ligands revealed that high uptake materials can be achieved without the most expensive ligands. One material in our set approached the DOE target of volumetric methane uptake at 35 bar of $180\ \mathrm{V_{STP}/V}$, illustrating that high-performance materials can be realized with existing organic components. Identification of the optimum commercially available ligands, in terms of both volumetric and gravimetric uptake, led to observation of design considerations for achieving high uptake materials. High volumetric uptake can be achieved with short, wide ligands (the best examples of which in this set were fused benzene rings); in turn, we observe a maximum of volumetric $\mathrm{CH_4}$ uptake for structures of methane void fraction of approximately 0.3. High gravimetric uptake can be achieved with very long molecules (the best examples of which comprised nitrogen-extended ligands), and moreover, there is a strong correlation between gravimetric $\mathrm{CH_4}$ uptake and both gravimetric ASA and AV.

The approach presented here for enumeration and characterization of isoreticular analogues of MOF-5 is generally applicable to MOFs of different topologies, and we envision extending this work to include analysis of MOFs comprising alternative secondary building units. We anticipate that a much broader space of MOF structures utilizing commercially available chemical species is achievable.

## ASSOCIATED CONTENT

### Supporting Information
Additional figures and 3D structures of the discussed materials. This material is available free of charge via the Internet at http://pubs.acs.org.

## AUTHOR INFORMATION

### Corresponding Author
*E-mail: mharanczyk@lbl.gov. Phone: (+1) 510-486-7749.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
The authors would like to thank Dr. James Stewart for providing the MOPAC license. This work was performed at Lawrence Berkeley National Laboratory supported by the U.S. Department of Energy under Contract No. DE-AC02-05CH11231. This research was supported by (a) the Center for Gas Separations Relevant to Clean Energy Technologies, an Energy Frontier Research Center funded by the U.S. Department of Energy, Office of Science, Office of Basic Sciences under Award Number DE-SC0001015 (to R.L.M, M.H.) and (b) the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Chemical Sciences, Geosciences and Biosciences under Award DE-FG02-12ER16362 (to L.-C.L., B.S.). This research used resources of the National Energy Research Scientific Computing Center, which is supported by the Office of Science of the U.S. Department of Energy under Contract No. DEAC02-05CH11231.

## REFERENCES
(1) Zhou, H.-C.; Long, J. R.; Yaghi, O. M. Introduction to Metal−Organic Frameworks. *Chem. Rev.* **2012**, *112*, 673−674.

(2) Chae, H. K.; Siberio-Pérez, D. Y.; Kim, J.; Go, Y.; Eddaoudi, M.; Matzger, A. J.; O'Keeffe, M.; Yaghi, O. M. A Route to High Surface Area, Porosity and Inclusion of Large Molecules in Crystals. *Nature* **2004**, *427*, 523−527.

(3) Farha, O. K.; Eryazici, I.; Jeong, N. C.; Hauser, B. G.; Wilmer, C. E.; Sarjeant, A. A.; Snurr, R. Q.; Nguyen, S. T.; Yazaydn, A. Ö.; Hupp, J. T. Metal−Organic Frameworks with Ultrahigh Surface Areas: Is the Sky the Limit? *J. Am. Chem. Soc.* **2012**, *134*, 15016−15021.

(4) (a) Li, J.-R.; Kuppler, R. J.; Zhou, H.-C. Selecting Gas Adsorption and Separation in Metal−Organic Frameworks. *Chem. Soc. Rev.* **2009**, *38*, 1477−1504. (b) Haldoupis, E.; Nair, S.; Sholl, D. S. Efficient Calculation of Diffusion Limitations in Metal Organic Framework Materials: A Tool for Identifying Materials for Kinetic Separations. *J. Am. Chem. Soc.* **2010**, *132*, 7528−7539. (c) Liu, J.; Keskin, S.; Sholl, D. S. Molecular Simulations and Theoretical Predictions for Adsorption and Diffusion of $\mathrm{CH_4/H_2}$ and $\mathrm{CO_2/CH_4}$ Mixtures in ZIFs. *J. Phys. Chem. C* **2011**, *115*, 12560−12566. (d) Sikora, B. J.; Wilmer, C. E.; Greenfield, M. L.; Snurr, R. Q. Thermodynamic Analysis of Xe/Kr Selectivity in over 137 000 Hypothetical Metal−Organic Frameworks. *Chem. Sci* **2012**, *3*, 2217−2223.

(5) (a) Keskin, S.; Sholl, D. S. Screening Metal−Organic Framework Materials for Membrane-Based Methane/Carbon Dioxide Separations. *J. Phys. Chem. C* **2007**, *111*, 14055−14059. (b) Sumida, K.; Rogow, D. L.; Mason, J. A.; McDonald, T. M.; Bloch, E. D.; Herm, Z. R.; Bae, T.-H.; Long, J. R. Carbon Dioxide Capture in Metal−Organic Frameworks. *Chem. Rev.* **2012**, *112*, 724−781.

(6) (a) Murray, L. J.; Dinc, M.; Long, J. R. Hydrogen Storage in Metal−Organic Frameworks. *Chem. Soc. Rev.* **2009**, *38*, 1294−1314. (b) Makal, T. A.; Li, J.-R.; Lu, W.; Zhou, H.-C. Methane Storage in Advanced Porous Materials. *Chem. Soc. Rev.* **2012**, *41*, 7761−7779.

(7) Lee, J.; Farha, O. K.; Roberts, J.; Scheidt, K. A.; Nguyen, S. T.; Hupp, J. T. Metal−Organic Framework Materials as Catalysts. *Chem. Soc. Rev.* **2009**, *38*, 1450−1459.

(8) Yaghi, O. M.; O'Keeffe, M.; Ockwig, N. W.; Chae, H. K.; Eddaoudi, M.; Kim, J. Reticular Chemistry and the Design of New Materials. *Nature* **2003**, *423*, 705−714.

(9) (a) Rosi, N. L.; Eckert, J.; Eddaoudi, M.; Vodak, D. T.; Kim, J.; O'Keeffe, M.; Yaghi, O. M. Hydrogen Storage in Microporous Metal-Organic Frameworks. *Science* **2003**, *300*, 1127−1129. (b) Chen, B.; Wang, X.; Zhang, Q.; Xi, X.; Cai, J.; Qi, H.; Shi, S.; Wang, J.; Yuan, D.; Fang, M. Synthesis and Characterization of the Interpenetrated MOF-5. *J. Mater. Chem.* **2010**, *20*, 3758−3767.

(10) (a) Li, H.; Eddaoudi, M.; O'Keeffe, M.; Yaghi, O. M. Design and Synthesis of an Exceptionally Stable and Highly Porous Metal-Organic Framework. *Nature* **1999**, *402*, 276−279. (b) Eddaoudi, M.; Kim, J.; Rosi, N.; Vodak, D.; Wachter, J.; O'Keeffe, M.; Yaghi, O. M. Systematic Design of Pore Size and Functionality in Isoreticular MOFs and Their Application in Methane Storage. *Science* **2002**, *295*, 469−472.

(11) Rowsell, J. L. C.; Millward, A. R.; Park, K. S.; Yaghi, O. M. Hydrogen Sorption in Functionalized Metal−Organic Frameworks. *J. Am. Chem. Soc.* **2004**, *126*, 5666−5667.

(12) Frost, H.; Düren, T.; Snurr, R. Q. Effects of Surface Area, Free Volume, and Heat of Adsorption on Hydrogen Uptake in Metal-Organic Frameworks. *J. Phys. Chem. B* **2006**, *110*, 9565−9570.

(13) (a) O'Keeffe, M.; Peskov, M. A.; Ramsden, S. J.; Yaghi, O. M. The Reticular Chemistry Structure Resource (RCSR) Database of, and Symbols for, Crystal Nets. *Acc. Chem. Res.* **2008**, *41*, 1782−1789. (b) O'Keeffe, M.; Yaghi, O. M. Deconstructing the Crystal Structures of Metal−Organic Frameworks and Related Materials into Their Underlying Nets. *Chem. Rev.* **2012**, *112*, 675−702.

(14) Deng, H.; Doonan, C. J.; Furukawa, H.; Ferreira, R. B.; Towne, J.; Knobler, C. B.; Wang, B.; Yaghi, O. M. Multiple Functional Groups of Varying Ratios in Metal−Organic Frameworks. *Science* **2010**, 327, 846−850.

(15) Wilmer, C. E.; Leaf, M.; Lee, C. Y.; Farha, O. K.; Hauser, B. G.; Hupp, J. T.; Snurr, R. Q. Large-Scale Screening of Hypothetical Metal−Organic Frameworks. *Nature Chem* **2012**, 4, 83−89.

(16) http://www.emolecules.com (accessed 10/02/12).

(17) SMARTS Theory Manual; Daylight Chemical Information Systems: Santa Fe, New Mexico.

(18) O'Boyle, N. M.; Banck, M.; James, C. A.; Morley, C.; Vandermeersch, T.; Hutchison, G. R. Open Babel: An Open Chemical Toolbox. *J. Cheminf.* **2011**, 3, 33.

(19) Halgren, T. A. Merck Molecular Force Field. I. Basic, Form, Scope, Parameterization, and Performance of MMFF94. *J. Comput. Chem.* **1996**, 17, 490−519.

(20) Berthold, M. R.; Cebron, N.; Dill, F.; Fatta, G. D.; Gabriel, T. R.; Georg, F.; Meinl, T.; Ohl, P.; Sieb, C.; Wiswedel, B. KNIME: The Konstanz Information Miner. Technical Report (http://www.knime.org).

(21) Martin, R. L.; Smit, B.; Haranczyk, M. Addressing Challenges of Identifying Geometrically Diverse Sets of Crystalline Porous Materials. *J. Chem. Inf. Model.* **2012**, 52, 308−318.

(22) (a) Stewart, J. J. P. Optimization of Parameters for Semiempirical Methods V: Modification of NDDO Approximations and Application to 70 Elements. *J. Mol. Model.* **2007**, 13, 1173−1213. (b) Korth, M.; Pitonák, M.; Pezác, J.; Hobza, P. A Transferable H-Bonding Correction for Semiempirical Quantum-Chemical Methods. *J. Chem. Theory Comput.* **2010**, 6, 344−352.

(23) Yang, S.; Lach-hab, M.; Vaisman, I. I.; Blaisten-Barojas, E. Identifying Zeolite Frameworks with a Machine Learning Approach. *J. Phys. Chem. C* **2009**, 113, 21721−21725.

(24) Willems, T. F.; Rycroft, C. H.; Kazi, M.; Meza, J. C.; Haranczyk, M. Algorithms and Tools for High-Throughput Geometry-Based Analysis of Crystalline Porous Materials. *Microporous Mesoporous Mater.* **2012**, 149, 134−141.

(25) (a) Bondi, A. van der Waals Volumes and Radii. *J. Phys. Chem.* **1964**, 68, 441−452. (b) Rowland, R. S.; Taylor, R. Intermolecular Nonbonded Contact Distances in Organic Crystal Structures: Comparison with Distances Expected from van der Waals Radii. *J. Phys. Chem.* **1996**, 100, 7384−7391. (c) Allen, F. H. The Cambridge Structural Database: a Quarter of a Million Crystal Structures and Rising. *Acta Cryst. B* **2002**, 58, 380−388.

(26) Giannozzi, P.; Baroni, S.; Bonini, N.; Calandra, M.; Car, R.; Cavazzoni, C.; Ceresoli, D.; Chiarotti, G. L.; Cococcioni, M.; Dabo, I.; et al. QUANTUM ESPRESSO: a Modular and Open-Source Software Project for Quantum Simulations of Materials. *J. Phys.: Condens. Matter* **2009**, 21, 395502.

(27) Frenkel, D.; Smit, B. *Understanding Molecular Simulation: From Algorithms to Applications*, 2nd ed.; Academic Press: San Diego, CA, 2002.

(28) Rappe, A. K.; Casewit, C. J.; Colwell, K. S.; Goddard, W. A.; Skiff, W. M. UFF, a Full Periodic Table Force Field for Molecular Mechanics and Molecular Dynamics Simulations. *J. Am. Chem. Soc.* **1992**, 114, 10024−10035.

(29) Potoff, J. J.; Siepmann, J. I. Vapor−Liquid Equilibria of Mixtures Containing Alkanes, Carbon Dioxide, and Nitrogen. *AIChE J.* **2001**, 47, 1676−1682.

(30) (a) Martin, R. L.; Haranczyk, M. Exploring Frontiers of High Surface Area Metal−Organic Frameworks. *Chem. Sci* **2013**, 4, 1781−1785. (b) Sarkisov, L. Accessible Surface Area of Porous Materials: Understanding Theoretical Limits. *Adv. Mater.* **2012**, 24, 3130−3133.

(31) http://www.emolecules.com (accessed 02/21/13).