![](./images/812997670439223297_1.jpg)

Subscriber access provided by University of South Dakota

# Computational Chemistry

## AFLOW-CHULL: Cloud-Oriented Platform
for Autonomous Phase Stability Analysis

Corey Oses, Eric Gossett, David Hicks, Frisco Rose, Michael J. Mehl, Eric Perim, Ichiro Takeuchi, Stefano Sanvito, Matthias Scheffler, Yoav Lederer, Ohad Levy, Cormac Toher, and Stefano Curtarolo

J. Chem. Inf. Model., Just Accepted Manuscript • DOI: 10.1021/acs.jcim.8b00393 • Publication Date (Web): 06 Sep 2018

Downloaded from http://pubs.acs.org on September 12, 2018

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/812997670439223297_2.jpg)

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# AFLOW-CHULL: Cloud-Oriented Platform for Autonomous Phase Stability Analysis

Corey Oses, $^{1}$ Eric Gossett, $^{1}$ David Hicks, $^{1}$ Frisco Rose, $^{1}$ Michael J. Mehl, $^{2}$ Eric Perim, $^{1}$ Ichiro Takeuchi, $^{3,4}$ Stefano Sanvito, $^{5}$ Matthias Scheffler, $^{6}$ Yoav Lederer, $^{1,7}$ Ohad Levy, $^{1,7}$ Cormac Toher, $^{1}$ and Stefano Curtarolo $^{1,6, *}$

$^{1}$ Department of Mechanical Engineering and Materials Science and Center for Materials Genomics, Duke University, Durham, North Carolina 27708, USA
$^{2}$ United States Naval Academy, Annapolis, Maryland 21402, USA
$^{3}$ Department of Materials Science and Engineering, University of Maryland, College Park, Maryland 20742-4111, USA
$^{4}$ Center for Nanophysics and Advanced Materials, University of Maryland, College Park, Maryland 20742, USA
$^{5}$ School of Physics, AMBER and CRANN Institute, Trinity College, Dublin 2, Ireland
$^{6}$ Fritz-Haber-Institut der Max-Planck-Gesellschaft, 14195 Berlin-Dahlem, Germany
$^{7}$ Department of Physics, NRCN, P.O. Box 9001, Beer-Sheva 84190, Israel

(Dated: August 21, 2018)

A priori prediction of phase stability of materials is a challenging practice, requiring knowledge of all energetically-competing structures at formation conditions. Large materials repositories — housing properties of both experimental and hypothetical compounds — offer a path to prediction through the construction of informatics-based, ab-initio phase diagrams. However, limited access to relevant data and software infrastructure has rendered thermodynamic characterizations largely peripheral, despite their continued success in dictating synthesizability. Herein, a new module is presented for autonomous thermodynamic stability analysis, implemented within the open-source, ab-initio framework AFLOW. Powered by the AFLUX Search-API, AFLOW-CHULL leverages data of more than 1.8 million compounds characterized in the AFLOW.org repository, and can be employed locally from any UNIX-like computer. The module integrates a range of functionality: the identification of stable phases and equivalent structures, phase coexistence, measures for robust stability, and determination of decomposition reactions. As a proof-of-concept, thermodynamic characterizations have been performed for more than 1,300 binary and ternary systems, enabling the identification of several candidate phases for synthesis based on their relative stability criterion — including 18 promising $C15_{b}$-type structures and two half-Heuslers. In addition to a full report included herein, an interactive, online web application has been developed showcasing the results of the analysis, and is located at aflow.org/aflow-chull.

## 1. INTRODUCTION

Accelerating the discovery of new functional materials demands an efficient determination of synthesizability. In general, materials synthesis is a multifaceted problem, spanning **i.** technical challenges, such as experimental apparatus design and growth conditions, $^{1,2}$ as well as **ii.** economic and environmental obstacles, including accessibility and handling of necessary components. $^{3,4}$ Phase stability is a limiting factor. Often, it accounts for the gap between materials prediction and experimental realization. Addressing stability requires an understanding of how phases compete thermodynamically. Despite the wealth of available experimental phase diagrams, $^{5}$ the number of systems explored represents a negligible fraction of all hypothetical structures. $^{6,7}$ Large materials databases $^{8-16}$ enable the construction of calculated phase diagrams, where aggregate structural and energetic materials data is employed. The analysis delivers many fundamental thermodynamic descriptors, including stable/unstable classification, phase coexistence, measures of robust stability, and determination of decomposition reactions. $^{4,17-20}$

As with all informatics-based approaches, ab-initio phase diagrams require an abundance of data: well-converged enthalpies from a variety of different phases. Many thermodynamic descriptors computed from the AFLOW.org repository have already demonstrated predictive power in characterizing phase stability, $^{4,17,21-34}$ including one investigation that resulted in the synthesis of two new magnets — the first ever discovered by computational approaches. $^{4}$ As exploration embraces more complex systems, such analyses are expected to become increasingly critical in confining the search space. In fact, prospects for stable ordered phases diminish with every new component (dimension), despite the growing number of combinations, due to increased competition with **i.** phases of lower dimensionality, e.g., ternary phases competing with stable binary phases, $^{34}$ and **ii.** disordered (higher entropy) phases. $^{35-37}$

To address the challenge, a new module has been implemented in the autonomous, open-source $^{38}$ AFLOW (Automatic Flow) framework for ab-initio calculations. $^{21,23-25,29,39-44}$ AFLOW-CHULL (AFLOW convex hull) offers a thermodynamic characterization that can be employed locally from any UNIX-like machine, including those running Linux and macOS. Built-in data curation and validation schemes ensure results are well-converged: adhering to proper hull statistics, performing outlier detection, and determining structural equivalence. AFLOW-CHULL is powered by the AFLUX Search-API (application programming interface), $^{11}$ which enables access to more than 1.8 million compounds from the AFLOW.org repository. With AFLUX integration, data-bindings are flexible enough to serve any materials database, including large heterogeneous repositories such as NOMAD. $^{12}$

Several analysis output types have been created for

![](./images/812997670439223297_3.jpg)

FIG. 1. Example hull illustrations in 2-/3-dimensions as generated by AFLOW-CHULL: (a) Co-Ti and (b) Mn- Pd-Pt.

integration into a variety of design workflows, includ- ing plain text and JSON (JavaScript Object Notation) file types. A small set of example scripts have been included demonstrating how to employ AFLOW-CHULL from within a Python environment, much in the spirit of AFLOW-SYM.⁴⁵ The JSON output also powers an inter- active, online web application offering enhanced presen- tation of thermodynamic descriptors and visualization of 2-/3-dimensional hulls. The application can be accessed through the AFLOW.org portal under "Apps and Docs" or directly at aflow.org/aflow-chull.

As a test-bed, the module is applied to all 1.8 million compounds available in the AFLOW.org repository. After enforcing stringent hull convergence criteria, the mod- ule resolves a thermodynamic characterization for more than 1,300 binary and ternary systems. Stable phases are screened for previously explored systems and ranked by their relative stability criterion, a dimensionless quantity capturing the effect of the phase on the minimum energy surface.⁴ Several promising candidates are identified, in- cluding 18 $C15_b$-type structures ($F\overline{4}3m$ #216) and two half-Heuslers. Hence, screening criteria based on these thermodynamic descriptors can accelerate the discovery of new stable phases. More broadly, the design of more challenging materials, including ceramics⁴⁶ and metallic glasses,³¹ benefit from autonomous, integrated platforms such as AFLOW-CHULL.

## 2. METHODS

Defining thermodynamic stability. For a multicom- ponent system at a fixed temperature ($T$) and pressure ($p$), the minimum Gibbs free energy $G$ (per atom) defines the thermodynamic equilibrium:
$$
G(T,p,\{x_i\}) = H - TS \tag{1}
$$
where $x_i$ is the atomic concentration of the $i$-species, $H$ is the enthalpy, and $S$ is the entropy. A binary phase $A_{x_A}B_{x_B}$ is stable at equilibrium with respect to its com- ponents $A$ and $B$ if the corresponding formation reaction releases energy:
$$
x_A A + x_B B \xrightarrow{\Delta G<0} A_{x_A}B_{x_B}, \tag{2}
$$
where $\Delta G$ is the energy difference between the mixed phase and the sum of its components. Conversely, a pos- itive $\Delta G$ suggests the decomposition of $A_{x_A}B_{x_B}$ is pre- ferred, and is thus unstable. In general, the magnitude of $\Delta G$ quantifies the propensity for the reaction, and the sign determines the direction.

Relative stability can be visualized on a free-energy- concentration diagram — $\Delta G$ versus $\{x_i\}$ — where $\Delta G$ is depicted as the energetic vertical-distance be- tween $A_{x_A}B_{x_B}$ and the tie-line connecting $A$ and $B$ end- members (elemental phases). End-members constitute only a single pathway to formation/decomposition, and all feasible reactions should be considered for system- wide stability. Identification of equilibrium phases is mathematically equivalent to the construction of the con- vex hull — the set of the most extreme or "outside" points (Figure 1(a)). The convex hull characterizes the phase stability of the system at equilibrium and does not include kinetic considerations for synthesis. Growth con- ditions affect the final outcome leading to formation of polymorphs and/or metastable phases, which could dif- fer from the equilibrium phases. This is a formidable task for high-throughput characterization. To help iden- tify kinetic pathways for synthesis, AFLOW-CHULL in- cludes (more in future releases) potential kinetic descrip- tors, e.g., chemical decompositions, distance from sta- bility, entropic temperature,⁴⁸ glass formation ability,³¹ and spectral entropy analysis for high-entropy systems.

In the zero temperature limit (as is the case for ground- state density functional theory), the entropic term of Equation 1 vanishes, leaving the formation enthalpy term (per atom) as the driving force:
$$
H_\mathrm{f} = H_{A_{x_A}B_{x_B}} - \left(x_A H_A + x_B H_B\right). \tag{3}
$$

![](./images/812997670439223297_4.jpg)

FIG. 2. Illustration of the convex hull construction for a binary system with AFLOW-CHULL. The approach is inspired by the Qhull algorithm.⁴⁷ The points on the plot represent structures from the AFLOW.org database.⁸⁻¹¹ (a) and (g) denote the beginning and end of the algorithm, respectively. (c-f) denote the iterative loop that continues until the condition denoted by (b) is no longer satisfied. Points are marked with crosses if, by that step in the algorithm, they have been determined to be inside the hull, and otherwise are marked with circles. The furthest point from the facet in (d) is marked with a triangle. Points and facets of interest are highlighted in red and green, respectively.

By construction, formation enthalpies of stable elemental phases are zero, restricting the convex hull to the lower hemisphere. Zero-point energies are not yet included in the AFLOW.org repository and thus are neglected from the enthalpy calculations. Efforts to incorporate vibra- tional characterizations are underway.⁴⁹,⁵⁰ This contri- bution could have a large impact on compounds contain- ing light-elements, such as hydrogen,⁵¹ which comprise a small minority (less than 1%) of the overall repository.

By offsetting the enthalpy with that of the elemen- tal phases, $H_f$ quantifies the energy gain from forming new bonds between unlike components,⁵² e.g., $A-B$. Currently, the AFLOW-CHULL framework does not allow the renormalization of chemical potentials to improve the calculation of formation enthalpies when gas phases are involved. A new first-principles approach is being devel- oped and tested in AFLOW, and will be implemented in future versions of the AFLOW-CHULL software together with the available approaches.⁵³,⁵⁴

The tie-lines connecting stable phases in Figure 1(a) define regions of phase separation where the two phases coexist at equilibrium. The chemical potentials are equal for each component among coexisting phases, imply- ing the common tangent tie-line construction.⁵⁵,⁵⁶ Under thermodynamic equilibrium, phases above a tie-line will decompose into a linear combination of the stable phases that define the tie-line (Figure 4(d)). The Gibbs phase rule⁵⁷ dictates the shape of tie-lines for $N$-ary systems, which generalizes to $(N-1)$-dimensional triangles (sim- plexes) and correspond to facets of the convex hull, e.g., lines in two dimensions (Figure 1(a)), triangles in three dimensions (Figure 1(b)), and tetrahedra in four. The set of equilibrium facets define the $N$-dimensional minimum energy surface.

Hull construction. AFLOW-CHULL calculates the $N$- dimensional convex hull corresponding to an $N$-ary sys- tem with an algorithm partially inspired by Qhull.⁴⁷ The algorithm is efficient in identifying the most impor- tant points for construction of facets, which are treated as hyperplanes instead of boundary-defining inequal- ities. AFLOW-CHULL uniquely accommodates ther- modynamic hulls, i.e., data occupying the lower half hemisphere and defined by stoichiometric coordinates $(0 \leq x_i \leq 1)$. Points corresponding to individual phases are characterized by their stoichiometric and energetic coordinates:

$$
\mathbf{p} = [x_1, x_2, \dots, x_{N-1}, H_f] = [\mathbf{x}, H_f], \tag{4}
$$

![](./images/812997670439223297_5.jpg)

FIG. 3. Illustration of the AFLOW-CHULL iterative hull scheme. The convex hull and associated properties are first calculated for the binary hulls, and then propagated to the ternary hull. This is generalized for N-dimensions.

where $x_N$ is implicit $(\sum_i x_i = 1)$. Data preparation includes the i. elimination of phases unstable with respect to end-members (points above the zero $H_f$ tie-line) and ii. organization of phases by stoichiometry and sorted by energy. Through this stoichiometry group structure, all but the minimum energy phases are eliminated from the convex hull calculation.

The workflow is illustrated in Figure 2. AFLOW- CHULL operates by partitioning space, iteratively defining “inside” versus “outside” half-spaces until all points are either on the hull or inside of it. First, a simplex is initialized (Figure 2(a)) with the most extreme points: stable end-members and the globally stable mixed phase (lowest energy). A facet is described as:

$$
\mathbf{n} \cdot \mathbf{r} + D = 0, \tag{5}
$$

where $\mathbf{n}$ is the characteristic normal vector, $\mathbf{r}$ is the position vector, and $D$ is the offset. A general hyperplane is defined by $N$ points and $k = (N - 1)$ corresponding edges $\mathbf{v}_k = \mathbf{p}_k - \mathbf{p}_{\text{origin}}$. To construct $\mathbf{n}$, AFLOW-CHULL employs a generalized cross product approach,⁵⁸ where $n_{i \in \{1,...,N\}}$ (unnormalized) is the $i$-row cofactor $(C_{i,j=0})$ of the matrix $\mathbf{V}$ containing $\mathbf{v}_k$ in its columns:

$$
n_{i}=(-1)^{i+1} M_{i, j=0}\left(\left[\begin{array}{ccc}
\mid & & \mid \\
\mathbf{v}_{1} & \ldots & \mathbf{v}_{k} \\
\mid & & \mid
\end{array}\right]\right) \tag{6}
$$

Here, $M_{i,j=0} (\mathbf{V})$ denotes the $i$-row minor of $\mathbf{V}$, i.e., the determinant of the submatrix formed by removing the $i$-row.

The algorithm then enters a loop over the facets of the convex hull until no points are declared “outside”, defined in the hyperplane description by the signed point- plane distance (Figure 2(b)). Each point outside of the hull is singularly assigned to the outside set of a facet (red in Figure 2(c)). The furthest point from each facet — by standard point-plane distance — is selected from the outside set (marked with a triangle in Figure 2(d)). Each neighboring facet is visited to determine whether

the furthest point is also outside of it, defining the set of visible planes (green) and its boundary, the horizon ridges (red) (Figure 2(d)). The furthest point is combined with each ridge of the horizon to form new facets (Figure 2(e)). The visible planes — the dotted line in Figure 2(e) — are then removed from the convex hull (Figure 2(f)). The fully constructed convex hull — with all points on the hull or inside of it — is summarized in Figure 2(g).

A challenge arises with lower dimensional data in higher dimensional convex hull constructions. For example, binary phases composed of the same species all exist on the same (vertical) plane in three dimensions. A half-space partitioning scheme can make no "inside" versus "outside" differentiation between such points. These ambiguously-defined facets⁵⁹ constitute a hull outside the scope of the Qhull algorithm.⁴⁷ In the case of three dimensions, the creation of ill-defined facets with collinear edges can result. Hyper-collinearity — planes defined with collinear edges, tetrahedra defined with coplanar faces, etc. — is prescribed by the content (hyper-volume) of the facet. The quantity resolves the length of the line (1-simplex), the area of a triangle (2-simplex), the volume of a tetrahedron (3-simplex), etc., and is calculated for a simplex of $N$-dimensions via the Cayley-Menger determinant.⁶⁰ Both vertical and content-less facets are problematic for thermodynamic characterizations, particularly when calculating hull distances, which require facets within finite energetic distances and well-defined normals.

A dimensionally-iterative scheme is implemented in AFLOW-CHULL to solve the issue. It calculates the convex hull for each dimension consecutively (Figure 3). In the case of a ternary hull, the three binary hulls are calculated first, and the relevant thermodynamic data is extracted and then propagated forward. Though vertical and content-less facets are still created in higher dimensions, no thermodynamic descriptors are extracted from them. To optimize the calculation, only stable binary structures are propagated forward to the ternary hull calculation, and this approach is generalized for $N$-dimensions. The scheme is the default for thermodynamic hulls, resorting back to the general convex hull algorithm otherwise.

Thermodynamic data. Structural and energetic data employed to construct the convex hull is retrieved from the AFLOW.org⁸⁻¹¹ repository, which contains more than 1.8 million compounds and 180 million calculated properties. The database is generated by the autonomous, $ab$-initio framework AFLOW²¹,²³⁻²⁵,²⁹,³⁹⁻⁴⁴ following the AFLOW Standard for high-throughput materials science calculations.¹⁰ In particular, calculations are performed with VASP (Vienna $\underline{Ab}$ initio Simulation Package).⁶¹ Wavefunctions are represented by a large basis set, including all terms with kinetic energy up to a threshold 1.4 times larger than the recommended defaults. AFLOW also leverages a large $\mathbf{k}$-point mesh — as standardized by a $\mathbf{k}$-points-per-reciprocal-atom scheme¹⁰ — which is critical for convergence and reliability of calculated properties. Investigations show that the AFLOW Standard of at least 6,000 $\mathbf{k}$-points-per-reciprocal-atom for structural relaxations and 10,000 for the static calculations ensures robust convergence of the energies to within one meV/atom in more than 95% of systems (including metals which suffer from the discontinuity in the occupancy function at zero temperature), and within three meV/atom otherwise.⁶²

Special consideration is taken for the calculation of $H_{\text{f}}$. The reference energies for the elemental phases are calculated and stored in the LIB1 catalog for unary phases in the AFLOW.org repository, and include variations for different functionals and pseudopotentials. For consistency, AFLOW-CHULL only employs data calculated with the Perdew-Burke-Ernzerhof Generalized Gradient Approximation functional⁶³ and pseudopotentials calculated with the projector augmented wave method⁶⁴ (PAW-PBE). Calculations employing DFT+$U$ corrections to rectify self-interaction errors and energy-gap issues for electronic properties¹⁰ are neglected. In general, these corrections are parameterized and material-specific.⁶⁵ They artificially augment the energy of the system affecting the reliability of thermodynamic properties. It is possible to encounter stable (lowest energy) elemental phases with energy differences from the reference of order meV/atom, which is the result of duplicate entries (by relaxation or otherwise) as well as reruns with new parameters, e.g., a denser $\mathbf{k}$-point mesh. To avoid any issues with the convex hull calculation, the algorithm fixes the half-space plane at zero. However, a "warning" is prompted in the event that the stable elemental phase differs from the reference energy by more than 15 meV/atom, yielding a "skewed" hull.

Data is retrieved via the AFLUX Search-API,¹¹ designed for accessing property-specific datasets efficiently. The following is an example of a relevant request:

http://aflowlib.duke.edu/search/API/?species(Mn,Pd),nspecies(2),*,paging(0)

where http://aflowlib.duke.edu/search/API/ is the URL for the AFLUX server and species(Mn,Pd),nspecies(2),*,paging(0) is the query. species(Mn,Pd) queries for any entry containing the elements Mn or Pd, nspecies(2) limits the search to binaries only, * returns the data for all available fields, and paging(0) amalgamates all data into a single response without paginating (warning, this can be a

![](./images/812997670439223297_6.jpg)

FIG. 4. Illustration of various automated convex hull analyses in AFLOW-CHULL. (a) A plot showing an egregious outlier in the Al-Co convex hull. (b) The corrected Al-Co convex hull (with the outlier removed). (c) The Te-Zr convex hull with the traditional compound labels replaced with the corresponding ICSD number designations as determined by a structure comparison analysis. If multiple ICSD entries are found for the same stoichiometry, the lowest number ICSD entry is chosen (chronologically reported, usually). (d) The decomposition energy of Pd₂Pt₃ is plotted in red, and highlighted in green is the equilibrium facet directly below it. The facet is defined by ground-state phases PdPt₃ and PdPt. (e) The stability criterion δₛc is plotted in green, with the pseudo-hull plotted with dashed lines. (f) The B-Sm convex hull plotted with the ideal "iso-max-latent-heat" lines of the grand-canonical ensemble²⁹,⁴⁸ for the ground-state structures.

large quantity of data). Such queries are constructed combinatorially for each dimension, *e.g.*, a general ternary hull $ABC$ constructs the following seven queries: $\text{species}(A)$, $\text{species}(B)$, and $\text{species}(C)$ with $\text{nspecies}(1)$, $\text{species}(A,B)$, $\text{species}(A,C)$, and $\text{species}(B,C)$ with $\text{nspecies}(2)$, and $\text{species}(A,B,C)$ with $\text{nspecies}(3)$.

Validation schemes. Various statistical analyses and data curation procedures are employed by AFLOW-CHULL to maximize fidelity. At a minimum, each binary hull must contain 200 structures to ensure a sufficient sampling size for inference. There is never any guarantee that all stable structures have been identified, $^{29,66}$ but convergence is approached with larger datasets. With continued growth of LIB3 (ternary phases) and beyond, higher dimensional parameters will be incorporated, though it is expected that the parameters are best defined along tie-lines (*versus* tie-surfaces). A comprehensive list of available alloys and structure counts are included in the Supporting Information.

Outlier detection. In addition to having been calculated with a standard set of parameters, $^{10}$ database entries should also be well-converged. Prior to the injection of new entries into the AFLOW.org database, various verification tests are employed to ensure convergence, including an analysis of the relaxed structure's stress tensor. $^{11}$ Issues stemming from poor convergence and failures in the functional parameterization $^{17,66}$ can change the topology of the convex hull, resulting in contradictions with experiments. Hence, an outlier detection algorithm is applied before the hull is constructed: structures are classified as outliers and discarded if they have energies that fall well below the first quartile by a multiple of the interquartile range (conservatively set to 3.25 by default). $^{67}$ Only points existing in the lower half-space (phases stable against end-members) are considered for the outlier analysis, and hence systems need to show some miscibility, *i.e.*, at least four points for a proper interquartile range determination. Despite its simplicity, the interquartile range is the preferred estimate of scale over other measures such as the standard deviation or the median absolute deviation, which require knowledge of the underlying distribution (normal or otherwise). $^{68}$ An example hull (Al-Co) showing an outlier is plotted in Figure 4(a) and the corrected hull with the outlier removed is presented in Figure 4(b).

Duplicate detection. A procedure for identifying duplicate entries is also employed. By database construction, near-exact duplicates of elemental phases exist in LIB2, which is created spanning the full range of compositions for each alloy system (including elemental phases). These degenerate entries are detected and removed by comparing composition, prototype, and formation enthalpy. Other structures may have been created distinctly, but converge to duplicates via structural relaxation. These equivalent structures are detected via AFLOW-XTAL-MATCH (AFLOW crystal match), $^{69}$ which determines structural/material uniqueness via the Burzlaff criteria. $^{70}$ To compare two crystals, a commensurate representation between structures is resolved by **i.** identifying common unit cells, **ii.** exploring cell orientations and origin choices, and **iii.** matching atomic positions. For each description, the structural similarity is measured by a composite misfit quantity based on the lattice deviations and mismatch of the mapped atomic positions, with a match occurring for sufficiently small misfit values $(< 0.1)$. Depending on the size of the structures, the procedure can be quite expensive, and only applied to find duplicate stable structures. Candidates are first screened by composition, space group, and formation enthalpies (must be within 15 meV/atom of the relevant stable configuration). By identifying duplicate stable phases, AFLOW-CHULL can cross-reference the AFLOW.org ICSD (Inorganic Crystal Structure Database) catalog $^{71,72}$ to reveal whether the structure has already been observed. The analysis is depicted in Figure 4(c), where the Te-Zr convex hull is plotted with the compound labels replaced with the corresponding ICSD number designation.

Thermodynamic descriptors. A wealth of properties can be extracted from the convex hull construction beyond a simple determination of stable/unstable phases. For unstable structures, the energy driving the decomposition reaction $\Delta H_{\text{f}}$, *i.e.*, the energetic vertical-distance to the hull depicted in Figure 4(d), serves as a useful metric for quasi-stability. Without the temperature and pressure contributions to the energy, near-stable structures should also be considered (meta-)stable candidates, *e.g.*, those within $k_{\text{B}}T = 25$ meV (room temperature) of the hull. Highly disordered systems can be realized with even larger distances. $^{17,73}$

To calculate $\Delta H_{\text{f}}$ of phase $\mathbf{p}$ (Equation 4), AFLOW-CHULL first resolves the energy of the hull $H_{\text{hull}}$ at stoichiometric coordinates $\mathbf{x}$, and then offsets it by the phase's formation enthalpy $H_{\text{f}}$:

$$
\Delta H_{\text{f}}[\mathbf{p}] = H_{\text{hull}}[\mathbf{x}] - H_{\text{f}}. \tag{7}
$$

The procedure is depicted in Figure 4(d), which involves identifying the facet (highlighted in green) that bounds $\mathbf{x}$ and thus defines $H_{\text{hull}}(\mathbf{x})$. Despite limitations of the hyperplane description of facets (Equations 5 and 6), which lacks boundaries in the stoichiometric axes, $^{17}$ the appropriate facet is identified as that which minimizes the distance to the zero $H_{\text{f}}$ tie-line at $\mathbf{x}$:

$$
H_{\text{hull}}[\mathbf{x}] = -\min_{\text{facets}\in\text{hull}} \left|n_{N}^{-1} \left(D + \sum_{i=1}^{N-1} n_{i}x_{i} \right)\right|. \tag{8}
$$

Vertical facets and those showing hyper-collinearity (having no content) are excluded from the calculation. By this convention, unstable phases have negative distances to the hull, indicative of a decomposition reaction (compare with Equations 2 and 9).

Furthermore, the $l$ coefficients of the balanced decomposition reaction are derived to yield the full equation. The decomposition of an $N$-ary phase into $l - 1$ stable

phases defines an $(l \times N)$-dimensional chemical composition matrix $\mathbf{C}$, where $C_{j,i}$ is the atomic concentration of the $i$-species of the $j$-phase (the first of which is the unstable mixed phase). Take, for example, the decomposition of $\text{Pd}_2\text{Pt}_3$ to PdPt and $\text{PdPt}_3$ as presented in Figure 4(d):

$$
N_1 \, \text{Pd}_{0.4}\text{Pt}_{0.6} \to N_2 \, \text{Pd}_{0.5}\text{Pt}_{0.5} + N_3 \, \text{Pd}_{0.25}\text{Pt}_{0.75}, \quad (9)
$$

where $N_j$ is the balanced chemical coefficient for the $j$-phase. In this case, $\mathbf{C}$ is defined as:

$$
\begin{bmatrix}
x_{\text{Pd}} \in \text{Pd}_2\text{Pt}_3 & x_{\text{Pt}} \in \text{Pd}_2\text{Pt}_3 \\
-x_{\text{Pd}} \in \text{PdPt} & -x_{\text{Pt}} \in \text{PdPt} \\
-x_{\text{Pd}} \in \text{PdPt}_3 & -x_{\text{Pt}} \in \text{PdPt}_3
\end{bmatrix}
=
\begin{bmatrix}
0.4 & 0.6 \\
-0.5 & -0.5 \\
-0.25 & -0.75
\end{bmatrix},
\quad (10)
$$

where a negative sign differentiates the right hand side of the equation from the left. Ref. 74 shows that $N_j$ can be extracted from the null space of $\mathbf{C}$. AFLOW-CHULL accesses the null space via a full $\mathbf{QR}$ decomposition of $\mathbf{C}$, specifically employing a general Householder algorithm. $^{75}$ The last column of the $(l \times l)$-dimensional $\mathbf{Q}$ orthogonal matrix spans the null space $\mathbf{N}$:

$$
\mathbf{Q} = \begin{bmatrix}
| & | & 0.8111 \\
\mathbf{q}_1 & \mathbf{q}_2 & 0.4867 \\
| & | & 0.3244
\end{bmatrix}. \quad (11)
$$

By normalizing $\mathbf{N}$ such that the first element $N_1 = 1$, the approach yields $N_2 = 0.6$ and $N_3 = 0.4$, which indeed balances Equation 9. These coefficients can be used to verify the energetic distance $\Delta H_{\text{f}}$ observed in Figure 4(d). The formation enthalpies of $\text{Pd}_2\text{Pt}_3$, PdPt, and $\text{PdPt}_3$ are -286 meV/(10 atoms), -72 meV/(2 atoms), and -104 meV/(4 atoms), respectively. Here, $\Delta H_{\text{f}}$ is calculated as:

$$
\begin{aligned}
0.6H_{\text{f}}[\text{PdPt}] + 0.4H_{\text{f}}[\text{PdPt}_3] &- H_{\text{f}}[\text{Pd}_2\text{Pt}_3] \\
&= -3 \text{ meV/atom}, \quad (12)
\end{aligned}
$$

For a given stable structure, AFLOW-CHULL determines the phases with which it is in equilibrium. For instance, PdPt is in two-phase equilibria with $\text{Pd}_3\text{Pt}$ as well as with $\text{PdPt}_3$ (Figure 4(d)). Phase coexistence plays a key role in defining a descriptor for precipitate-hardened superalloys. Candidates are chosen if a relevant composition is in two-phase equilibrium with the host matrix, suggesting that the formation of coherent precipitates in the matrix is feasible. $^{17,76}$

An analysis similar to that quantifying instability $(\Delta H_{\text{f}})$ determines the robustness of stable structures. The stability criterion $\delta_{\text{sc}}$ is defined as the distance of a stable structure from the pseudo-hull constructed without it (Figure 4(e)). Its calculation is identical to that of $\Delta H_{\text{f}}$ for the pseudo-hull (Equations 7 and 8). This descriptor quantifies the effect of the structure on the minimum energy surface, as well as the structure's susceptibility to destabilization by a new phase that has yet to be explored. As with the decomposition analysis, $\delta_{\text{sc}}$ also serves to anticipate the effects of temperature and pressure on the minimum energy surface. The descriptor played a pivotal role in screening Heusler structures for new magnetic systems. $^{4}$ $\delta_{\text{sc}}$ calls for the recalculation of facets local to the structure and all relevant duplicates as well, thus employing the results of the structure comparison protocol.

Furthermore, AFLOW-CHULL can plot the entropic temperature envelopes characterizing nucleation in hyper-thermal synthesis methods for binary systems. $^{48}$ The entropic temperature is the ratio of the formation enthalpy to the mixing entropy for an ideal solution — a simple quantification for the resilience against disorder. $^{29}$ The ideal "iso-max-latent-heat" lines shown in Figure 4(f) try to reproduce the phase's capability to absorb latent heat, which can promote its nucleation over more stable phases when starting from large Q reservoirs/feedstock. The descriptor successfully predicts the synthesis of $\text{SmB}_6$ over $\text{SmB}_4$ with hyper-thermal plasma co-sputtering. $^{29,48}$

## 3. RESULTS

Analysis output. Following the calculation of the convex hull and relevant thermodynamic descriptors, AFLOW-CHULL generates a PDF file summarizing the results. Included in the PDF are **i.** an illustration of the convex hull as shown in Figure 1 (for binary and ternary systems) and **ii.** a report with the aforementioned calculated thermodynamic descriptors — an excerpt is shown in Figure 5.

In the illustrations, color is used to differentiate points with different enthalpies and indicate depth of the facets (3-dimensions). The report includes entry-specific data from the AFLOW.org database (prototype, auid, original and relaxed space groups, spin, formation enthalpy $H_{\text{f}}$, and entropic temperature $T_{\text{S}}$) as well as calculated thermodynamic data (distance to the hull $\Delta H_{\text{f}}$, the balanced decomposition reaction for unstable phases, the stability criterion $\delta_{\text{sc}}$ for stable phases, and phases in coexistence). Stable phases (and those that are structurally equivalent) are highlighted in green, and similar phases (comparing relaxed space groups) are highlighted in orange. Links are also incorporated in the report, including external hyperlinks to entry pages on AFLOW.org (see prototypes) and internal links to relevant parts of the report (see decomposition reaction and $N$-phase equilibria). Internal links are also included on the convex hull illustration (see Supporting Information). The information is provided in the form of plain text and JSON files. Keys and format are explained in the Appendix.

Web application. A modern web application has been developed to provide an enhanced, command-line-free platform for AFLOW-CHULL. The project includes a rich feature set consisting of binary and ternary convex hull visualizations, AFLOW.org entry data retrieval, and a convex hull comparison interface. The application is divided

<table><tbody><tr><th>prototype</th><th>auid</th><th>original<br>space group</th><th>relaxed<br>space group</th><th>spin<br>(μB/atom)</th><th>Hf<br>(meV/atom)</th><th>TS(K)</th><th>ΔHf<br>(meV/atom)</th></tr></tbody></table>

### ternaries

#### Ag₄AuCd
<table><tbody><tr><td>T0010.ABC</td><td>aflow:f01a0242937da2ae</td><td>F4̅3m#216</td><td>F4̅3m#216</td><td>0.00</td><td>87</td><td>-1170</td><td>-162</td></tr></tbody></table>

decomposition reaction:
$$\text{Ag}_{0.6667}\text{Au}_{0.1667}\text{Cd}_{0.1667} \rightarrow 0.3333\ \text{Ag} + 0.6667\ \text{Ag}_{0.5}\text{Au}_{0.25}\text{Cd}_{0.25}$$

#### Ag₂AuCd (ground state)
$\delta_{\text{sc}} = 1$ meV/atom
<table><tbody><tr><td>TFCC016.ABC</td><td>aflow:b306fb2e8866a640</td><td>P4/mmm#123</td><td>P4/mmm#123</td><td>0.00</td><td>-112</td><td>1251</td><td>0</td></tr><tr><td>TBCC016.ABC</td><td>aflow:8634edc5da7d9b0</td><td>P4/mmm#123</td><td>P4/mmm#123</td><td>0.00</td><td>-111</td><td>1234</td><td>-1</td></tr><tr><td>TFCC013.ABC</td><td>aflow:2f98e1c035b5aaaa</td><td>I4/mmm#139</td><td>I4/mmm#139</td><td>0.00</td><td>-111</td><td>1243</td><td>-1</td></tr><tr><td>TFCC008.ABC</td><td>aflow:5da326cf35c34568</td><td>I4̄m2#119</td><td>I4̄m2#119</td><td>0.00</td><td>-111</td><td>1234</td><td>-1</td></tr><tr><td>TFCC005.ABC</td><td>aflow:132a4b97141e5820</td><td>Pmm2#25</td><td>Pmm2#25</td><td>0.00</td><td>-92</td><td>1027</td><td>-20</td></tr><tr><td>TFCC011.ABC</td><td>aflow:76257f541c620495</td><td>C2/m#12</td><td>C2/m#12</td><td>0.00</td><td>-92</td><td>1024</td><td>-20</td></tr><tr><td>T0002.A2BC</td><td>aflow:331ee0a425d1f5af</td><td>F4̅3m#216</td><td>F4̅3m#216</td><td>0.00</td><td>-88</td><td>982</td><td>-24</td></tr><tr><td>TFCC010.ABC</td><td>aflow:53b2d83b7d6af7ad</td><td>Pmmm#47</td><td>Pmmm#47</td><td>0.00</td><td>-84</td><td>937</td><td>-28</td></tr><tr><td>TFCC006.ABC</td><td>aflow:2b3a7e0149b217c</td><td>Cm#8</td><td>Cm#8</td><td>0.00</td><td>-83</td><td>930</td><td>-29</td></tr><tr><td>TFCC015.ABC</td><td>aflow:a0fe092060da4e0d</td><td>Cmmm#65</td><td>Cmmm#65</td><td>0.00</td><td>-78</td><td>874</td><td>-34</td></tr><tr><td>T0001.A2BC</td><td>aflow:8f5a6e202c08fce7</td><td>Fm3̅m#225</td><td>Fm3̅m#225</td><td>0.00</td><td>-74</td><td>829</td><td>-38</td></tr><tr><td>TFCC007.ABC</td><td>aflow:62b2209e478e18d5</td><td>P4mm#99</td><td>P4mm#99</td><td>0.00</td><td>-70</td><td>780</td><td>-42</td></tr><tr><td>TBCC006.ABC</td><td>aflow:45de8e0b667b4376</td><td>P4mm#99</td><td>P4mm#99</td><td>0.00</td><td>-67</td><td>746</td><td>-45</td></tr><tr><td>TBCC011.ABC</td><td>aflow:9a39572049203457</td><td>P4/mmm#123</td><td>P4/mmm#123</td><td>0.00</td><td>-59</td><td>655</td><td>-53</td></tr><tr><td>TFCC012.ABC</td><td>aflow:4ee48aff3119af41</td><td>P4/mmm#123</td><td>P4/mmm#123</td><td>0.00</td><td>-58</td><td>644</td><td>-54</td></tr></tbody></table>

3-phase equilibria:
$\text{Ag-Ag}_4\text{Cd-Ag}_2\text{AuCd}$, $\text{Ag-Ag}_3\text{Au-Ag}_2\text{AuCd}$, $\text{Ag}_4\text{Cd-Ag}_3\text{Cd-Ag}_2\text{AuCd}$,
$\text{Ag}_3\text{Au-AgAu-Ag}_2\text{AuCd}$, $\text{Ag}_3\text{Cd-Ag}_2\text{AuCd-Au}_2\text{Cd}_3$, $\text{AgAu-Ag}_2\text{AuCd-AgAu}_2\text{Cd}$,
$\text{Ag}_2\text{AuCd-AgAu}_2\text{Cd-AuCd}$, and $\text{Ag}_2\text{AuCd-AuCd-Au}_2\text{Cd}_3$

FIG. 5. Excerpt from the Ag-Au-Cd thermodynamic analysis report. The document is generated by AFLOW-CHULL and showcases entry-specific data from the AFLOW.org database as well as calculated thermodynamic descriptors. Structures highlighted in green are structurally equivalent stable structures, and those in orange are structurally similar (same relaxed space group). The working document includes a variety of links, including hyperlinks to the entry page of each phase (see prototypes) and links to relevant parts of the report (see decomposition reaction and $N$-phase equilibria).

into four components: the periodic table, the visualization viewport, the selected entries list, and the comparison page.

The periodic table component is initially displayed. Hulls can be queried by selecting/typing in the elemental combination. As elements are added to the search, the periodic table reacts to the query depending on the reliability of the hull: green (fully reliable, $N_{\text{entries}} \geq 200$), orange (potentially reliable, $100 \leq N_{\text{entries}} < 200$), red (unreliable, $N_{\text{entries}} < 100$), and gray (unavailable, $N_{\text{entries}} = 0$). As with the command-line platform, each request triggers a fresh data download and analysis, offering the most up-to-date results given that new calculations are injected into the AFLOW.org repository daily. Once the analysis is performed and results are retrieved, the application loads the visualization viewport prompting a redirect to the URL endpoint of the selected hull, e.g., /hull/AlHfNi. The URL is ubiquitous and can be shared/cited.

When a binary convex hull is selected, the viewport reveals a traditional 2-dimensional plot (Figure 6(a)), while a ternary hull yields a 3-dimensional visualization (Figure 6(b)). The scales of both are tunable, and the 3-dimensional visualization offers mouse-enabled pan and zoom.

Common to both types is the ability to select and highlight points. When a point is selected, its name will appear within the sidebar. The information component is populated with a grid of cards containing properties of each selected point (entry), including a link to the AFLOW.org entry page (Figure 6(d)).

The application environment stores all previously selected hulls, which are retrievable via the hull comparison component (Figure 6(c)). On this page each hull visualization is displayed as a card on a grid. This grid serves as both a history and a means to compare hulls.

Candidates for synthesis. To demonstrate the capability of AFLOW-CHULL, all binary and ternary systems in the AFLOW.org repository are explored for ones yielding well-converged thermodynamic properties. Since reliability constraints are built-in, no pre-filtering is required and all potential elemental combinations are attempted. Across all catalogs present in the database, there exist materials composed of 86 elements, including: H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Ac, Th, and Pa. Hulls are eliminated if systems i. are unreliable based on count (fewer than 200 entries among binary combinations), and ii. show significant immiscibility (fewer than 50 points below the zero $H_{\text{f}}$ tie-line). Ternary systems are further screened for those containing ternary ground-state structures. The analysis resulted in the full thermodynamic characterization of 493 binary and 873 ternary systems. The results are provided in the Supporting Information.

Leveraging the JSON outputs, reliable hulls are further explored for new stable phases. Phases are first

![](./images/812997670439223297_7.jpg)

FIG. 6. The convex hull web application powered by AFLOW-CHULL. (a) An example 2-dimensional convex hull illustration (Mo-Ti). (b) An example 3-dimensional convex hull illustration (Fe-Rh-Zr). (c) The comparison component of the hull application. Each hull visualization is displayed as part of a grid of cards. From this page, new hulls can be added to the store by typing a query in the search box (sidebar). (d) The information component of the hull application. Pertinent thermodynamic data for selected points is displayed within the grid of cards. Each card includes a link to the AFLOW.org entry page and the option to remove a point. As points are selected within the visualization, more cards will be added to the grid.

screened (eliminated) if an equivalent structure exists in the AFLOW.org ICSD catalog, and candidates are sorted by their relative stability criterion, *i.e.*, $\delta_{\mathrm{sc}}/H_{\mathrm{f}}$. This dimensionless quantity captures the effect of the phase on the minimum energy surface relative to its depth, enabling comparisons across hulls. An example Python script that performs this analysis is provided in the Appendix.

The top 25 most stable binary and ternary phases are presented in Tables 1 and 2, respectively, for which extended analysis is performed based on information stored in the ASM (American Society for Metals) Alloy Phase Diagram database.⁵ The ASM database is the largest of its kind, aggregating a wealth of experimental phase diagram information: 40,300 binary and ternary alloy phase diagrams from over 9,000 systems. Upon search-

<table><thead><tr><th>compound</th><th>auid</th><th>relaxed space group</th><th>$\delta_{sc}/H_{f}$</th><th>comparison with ASM Alloy Phase Diagrams⁵</th></tr></thead><tbody><tr><td>$Hf_{5}Pb^{\dagger}$</td><td>aflow:38ecc639e4504b9d</td><td>$P4/mmm$ #123</td><td>78%</td><td>no diagram</td></tr><tr><td>$AgIn_{3}$</td><td>aflow:11ba11a3ee157f2e</td><td>$P6_{3}/mmc$ #194</td><td>54%</td><td>composition not found, nearest are $AgIn_{2}$ (space group $I4/mcm$, $\Delta H_{f}=$ -53 meV/atom) and $In$ (space group $I4/mmm$)</td></tr><tr><td>$Hf_{3}In_{4}^{\dagger}$</td><td>aflow:1da75eb5f31b6dd5</td><td>$P4/mbm$ #127</td><td>45%</td><td>no diagram</td></tr><tr><td>$AsTc_{2}^{\dagger}$</td><td>aflow:66dda41a34fe3ad6</td><td>$C2/m$ #12</td><td>41%</td><td>no diagram</td></tr><tr><td>$MoPd_{8}$</td><td>aflow:57e1a1246f813f27</td><td>$I4/mmm$ #139</td><td>40%</td><td>composition not found, nearest are $Mo_{0.257}Pd_{0.743}$ (space group $Fm\overline{3}m$, POCC structure) and $Pd$ (space group $Fm\overline{3}m$)</td></tr><tr><td>$Ga_{4}Tc^{\dagger}$</td><td>aflow:32051219452f8e0f</td><td>$Im\overline{3}m$ #229</td><td>39%</td><td>no diagram</td></tr><tr><td>$AgPt$</td><td>aflow:fdaf730b112472ba</td><td>$R\overline{3}m$#166</td><td>37%</td><td>polymorph found (space group $Fm\overline{3}m$, POCC structure)</td></tr><tr><td>$Pd_{8}V$</td><td>aflow:7bd140d7b4c65bc1</td><td>$I4/mmm$ #139</td><td>36%</td><td>composition not found, nearest are $V_{0.1}Pd_{0.9}$ (space group $Fm\overline{3}m$, POCC structure) and $VPd_{3}$ (space group $I4/mmm$, $\Delta H_{f}=$ -6 meV/atom)</td></tr><tr><td>$InSr_{3}$</td><td>aflow:e7ed70c4711eb718</td><td>$P4/mmm$ #123</td><td>35%</td><td>composition not found, nearest are $Sr_{28}In_{11}$ (space group $Imm2$) and $Sr$ (space group $Fm\overline{3}m$)</td></tr><tr><td>$CoNb_{2}$</td><td>aflow:f5cc5eaf65e692a9</td><td>$I4/mcm$ #140</td><td>35%</td><td>composition not found, nearest are $Nb_{6.7}Co_{6.3}$ (space group $R\overline{3}m$, POCC structure) and $Nb_{0.77}Co_{0.23}$ (space group $Fm\overline{3}m$, POCC structure)</td></tr><tr><td>$Ag_{3}In_{2}$</td><td>aflow:6ee057decaf093d0</td><td>$Fdd2$ #43</td><td>34%</td><td>composition not found, nearest are $Ag_{9}In_{4}$ (space group $P\overline{4}3m$, $\Delta H_{f}=$ -21 meV/atom) and $AgIn_{2}$ (space group $I4/mcm$, $\Delta H_{f}=$ -53 meV/atom)</td></tr><tr><td>$OsY_{3}$</td><td>aflow:bd3056780447faf0</td><td>$Pnma$ #62</td><td>34%</td><td>composition found, one-to-one match</td></tr><tr><td>$RuZn_{6}$</td><td>aflow:96142e32718a5ee0</td><td>$P4_{1}32$#213</td><td>33%</td><td>composition found, one-to-one match</td></tr><tr><td>$ReTa$</td><td>aflow:5c3e131ff9013a7d</td><td>$Pm\overline{3}m$#221</td><td>33%</td><td>composition not found, nearest are $Ta_{0.4}Re_{0.6}$ (space group $P4_{2}/mmm$, POCC structure) and $Ta_{0.6}Re_{0.4}$ (space group $Im\overline{3}m$, POCC structure)</td></tr><tr><td>$Ag_{2}Zn$</td><td>aflow:1ba6b4b5c0ed9788</td><td>$P\overline{6}2m$ #189</td><td>33%</td><td>composition not found, nearest are $Ag$ (space group $Fm\overline{3}m$, $\Delta H_{f}=$ -4 meV/atom) and $Ag_{4.5}Zn_{4.5}$ (space group $P\overline{3}$, POCC structure)</td></tr><tr><td>$MnRh$</td><td>aflow:87d6637b32224f7b</td><td>$Pm\overline{3}m$ #221</td><td>32%</td><td>polymorph found (space group $P4/mmm$, $\Delta H_{f}=$ -156 meV/atom)</td></tr><tr><td>$AgNa_{2}$</td><td>aflow:f08f2f61de18aa61</td><td>$I4/mcm$ #140</td><td>32%</td><td>composition not found, nearest are $NaAg_{2}$ (space group $Fd\overline{3}m$, $\Delta H_{f}=$ -208 meV/atom) and $Na$ (space group $R\overline{3}m$)</td></tr><tr><td>$BeRe_{2}$</td><td>aflow:7ce4fcc3660c16cf</td><td>$I4/mcm$ #140</td><td>31%</td><td>composition not found, nearest are $Be_{2}Re$ (space group $P6_{3}/mmc$) and $Re$ (space group $P6_{3}/mmc$)</td></tr><tr><td>$As_{2}Tc^{\dagger}$</td><td>aflow:e94ab366799a008c</td><td>$C2/m$ #12</td><td>30%</td><td>no diagram</td></tr><tr><td>$Be_{2}Mn^{\dagger}$</td><td>aflow:eec0d7b6b0d1dfa0</td><td>$P6_{3}/mmc$ #194</td><td>30%</td><td>no diagram</td></tr><tr><td>$AgAu$</td><td>aflow:6f3f5b696f5aa391</td><td>$P4/mmm$ #123</td><td>29%</td><td>polymorph found (space group $Fm\overline{3}m$, POCC structure)</td></tr><tr><td>$Nb_{5}Re_{24}$</td><td>aflow:ca051dbe25c55b92</td><td>$I\overline{4}3m$ #217</td><td>29%</td><td>composition not found, nearest are $Nb_{0.25}Re_{0.75}$ (space group $I\overline{4}3m$, POCC structure) and $Nb_{0.01}Re_{0.99}$ (space group $P6_{3}/mmc$, POCC structure)</td></tr><tr><td>$La_{3}Os^{\dagger}$</td><td>aflow:a9daa69940d3a59a</td><td>$Pnma$ #62</td><td>28%</td><td>no diagram</td></tr><tr><td>$Be_{5}Pt$</td><td>aflow:8ce84acfd6f9ea44</td><td>$F\overline{4}3m$ #216</td><td>28%</td><td>composition found, one-to-one match</td></tr><tr><td>$Ir_{8}Ru$</td><td>aflow:487f7cf6c3fb13f0</td><td>$I4/mmm$ #139</td><td>27%</td><td>composition not found, nearest are $Ir$ (space group $Fm\overline{3}m$) and $Ru_{0.3}Ir_{0.7}$ (space group $Fm\overline{3}m$, POCC structure)</td></tr></tbody></table>

ing the ASM website, many binary systems from Table 1 are unavailable and denoted by the symbol $^{\dagger}$. Among those that are available, some stable phases have already been observed, including $OsY_{3}$, $RuZn_{6}$, and $Be_{5}Pt$. For $AgPt$, $MnRh$, and $AgAu$, the composition is successfully predicted, but polymorphs (structurally distinct phases) are observed instead. For all other phases on the list, the composition has not been observed. The discrepancy may be isolated to the phase, or indicative of a more extreme contradiction in the topology of the hull, and thus, nearby phases are also analyzed. For the BeRe system, though $BeRe_{2}$ has not been observed, both $Be_{2}Re$ and $Re$ are successfully identified. Most of the remaining phases show the nearest phase to be a disor-

TABLE 2. The 25 ternary phases predicted to be most stable by AFLOW-CHULL. Phases with equivalent structures in the AFLOW ICSD catalog are excluded. The list is sorted by the ratio between the stability criterion ($\delta_{\text{sc}}$) and the formation enthalpy ($H_{\text{f}}$) (shown as a percentage). $^\dagger$ indicates no ternary phase diagram is available on the ASM Alloy Phase Diagram database, $^5$ while $^\ddagger$ indicates all three relevant binaries are available. POCC denotes a partially-occupied (disordered) structure.$^{40}$ Comparisons with the ASM database include phases that are observed at high temperatures and pressures.

<table>
<thead>
<tr>
<th>compound</th>
<th>auid</th>
<th>relaxed space group</th>
<th>$\delta_{\text{sc}}$/$H_{\text{f}}$</th>
<th>comparison with ASM Alloy Phase Diagrams$^5$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{MgSe}_2\text{Zn}_2$$^\dagger$</td>
<td>aflow:df0cdf0f1ad3110d</td>
<td>$Fmmm$ #69</td>
<td>58%</td>
<td>no diagram, two of three binary phase diagrams found (no Mg-Se)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{OsTi}^\dagger$</td>
<td>aflow:8c51c7ab71f25d11</td>
<td>$F\overline{4}3m$#216</td>
<td>38%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Os)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{OsV}^\dagger$</td>
<td>aflow:4e5711451dc4b601</td>
<td>$F\overline{4}3m$ #216</td>
<td>38%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Os)</td>
</tr>
<tr>
<td>$\text{Ag}_2\text{InZr}$</td>
<td>aflow:1684c02e75b0d950</td>
<td>$Fm\overline{3}m$ #225</td>
<td>35%</td>
<td>composition not found, nearest are $\text{Ag}_{0.8}\text{In}_{0.2}$ (space group $Fm\overline{3}m$, POCC structure), $\text{Zr}_{0.5}\text{In}_{0.5}$ (space group $Fm\overline{3}m$, POCC structure), and $\text{AgZr}_5\text{In}_3$ (space group $P6_3/mcm$)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{RuTi}^{\dagger \ddagger}$</td>
<td>aflow:b85addbb42c47ae9</td>
<td>$F\overline{4}3m$ #216</td>
<td>32%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{Be}_4\text{FeTi}^{\dagger \ddagger}$</td>
<td>aflow:cabd6decf5b6c991</td>
<td>$F\overline{4}3m$ #216</td>
<td>29%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{Be}_4\text{ReV}^{\dagger \ddagger}$</td>
<td>aflow:7010472778d429f7</td>
<td>$F\overline{4}3m$ #216</td>
<td>29%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{Ba}_2\text{RhZn}^{\dagger}$</td>
<td>aflow:e4cc9eea02d9d303</td>
<td>$Cm$ #8</td>
<td>29%</td>
<td>no diagram, two of three binary phase diagrams found (no Ba-Rh)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{HfOs}^{\dagger}$</td>
<td>aflow:2ace5c5383f8ea10</td>
<td>$F\overline{4}3m$ #216</td>
<td>27%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Os)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{ReTi}^{\dagger \ddagger}$</td>
<td>aflow:de79192a0c4e751f</td>
<td>$F\overline{4}3m$ #216</td>
<td>27%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{Be}_4\text{TcV}^\dagger$</td>
<td>aflow:d484b95ba623f9f7</td>
<td>$F\overline{4}3m$ #216</td>
<td>27%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Tc)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{TcTi}^\dagger$</td>
<td>aflow:c13660b990eb9570</td>
<td>$F\overline{4}3m$ #216</td>
<td>27%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Tc)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{RuV}^{\dagger \ddagger}$</td>
<td>aflow:07840d9e13694f7e</td>
<td>$F\overline{4}3m$ #216</td>
<td>27%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{AsCoTi}^{\dagger \ddagger}$</td>
<td>aflow:5778f3b725d5f850</td>
<td>$F\overline{4}3m$ #216</td>
<td>26%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{Be}_4\text{MnTi}^{\dagger}$</td>
<td>aflow:9a10dd8a8224e158</td>
<td>$F\overline{4}3m$ #216</td>
<td>26%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Mn)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{OsZr}^{\dagger}$</td>
<td>aflow:de412213bdefbd14</td>
<td>$F\overline{4}3m$ #216</td>
<td>26%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Os)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{IrTi}^\dagger$</td>
<td>aflow:07bcc161f57da109</td>
<td>$F\overline{4}3m$ #216</td>
<td>26%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Ir)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{MnV}^\dagger$</td>
<td>aflow:086b4a89f8d62804</td>
<td>$F\overline{4}3m$ #216</td>
<td>25%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Mn)</td>
</tr>
<tr>
<td>$\text{AuBe}_4\text{Cu}^{\dagger \ddagger}$</td>
<td>aflow:0595e3d45678a85c</td>
<td>$F\overline{4}3m$ #216</td>
<td>25%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{BiRhZr}^{\dagger \ddagger}$</td>
<td>aflow:d7fed8d4996290f4</td>
<td>$F\overline{4}3m$ #216</td>
<td>24%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{LiMg}_2\text{Zn}$</td>
<td>aflow:80bf8ad33a5bb33b</td>
<td>$Fm\overline{3}m$#225</td>
<td>21%</td>
<td>composition not found, nearest are $\text{Li}$ (space group $Im\overline{3}m$), $\text{Mg}$ (space group $P6_3/mmc$), and $\text{Li}_{0.77}\text{MgZn}_{1.23}$ (space group $Fd\overline{3}m$, POCC structure)</td>
</tr>
<tr>
<td>$\text{Be}_4\text{RhTi}^\dagger$</td>
<td>aflow:faa814b1222e8aea</td>
<td>$F\overline{4}3m$ #216</td>
<td>21%</td>
<td>no diagram, two of three binary phase diagrams found (no Be-Rh)</td>
</tr>
<tr>
<td>$\text{AuCu}_4\text{Hf}^{\dagger \ddagger}$</td>
<td>aflow:26cc4fc55644b0d8</td>
<td>$F\overline{4}3m$ #216</td>
<td>21%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
<tr>
<td>$\text{Mg}_2\text{SeZn}_2$$^\dagger$</td>
<td>aflow:ab57b1ae74f4c6d4</td>
<td>$Fmmm$ #69</td>
<td>21%</td>
<td>no diagram, two of three binary phase diagrams found (no Mg-Se)</td>
</tr>
<tr>
<td>$\text{AuCu}_4\text{Zr}^{\dagger \ddagger}$</td>
<td>aflow:6661fa448e5903a5</td>
<td>$F\overline{4}3m$ #216</td>
<td>20%</td>
<td>no diagram, all three binary phase diagrams found</td>
</tr>
</tbody>
</table>

dered (partially occupied) structure, which are excluded from the AFLOW.org repository. Addressing disorder is a particularly challenging task in ab-initio studies. However, recent high-throughput techniques$^{40}$ show promise for future investigations and will be integrated in future releases of the code.

Among the most stable ternary phases, only two systems have available phase diagrams in the ASM database, Ag-In-Zr and Li-Mg-Zn. For the Ag-In-Zr system, the composition of $\text{Ag}_2\text{InZr}$ is not observed and the nearest stable phases include disordered structures and $\text{AgZr}_5\text{In}_3$, which has not yet been included the AFLOW.org repository. For Li-Mg-Zn, the composition of $\text{LiMg}_2\text{Zn}$ is also not observed and the nearest stable phases include unaries Li, Mg and a disordered structure. All other ternary systems are entirely unexplored. In particular, ternary phases with all three binary phase diagrams available are denoted with the symbol $^\ddagger$, sug-

gesting experimental feasibility.

A striking feature of Table 2 is that most of the stable structures are found to be in space group $F\overline{4}3m$ #216. This structure has a face-centered cubic lattice with symmetry operations that include a four-fold rotation about the <001> axes, a three-fold rotation about the <111> axes, and no inversion. Further study reveals that these phases, as well as $Fm\overline{3}m$ #225 $Ag_2InZr$, can be obtained from the "quaternary-Heusler" structure, $LiMgPdSn^{77,78}$ (Figure 7(a)). The prototype can be considered a $2 \times 2 \times 2$ supercell of the body-centered cubic structure. The Sn, Mg, Au and Li atoms all occupy a different Wyckoff positions of space group $F\overline{4}3m$ and each atom has two sets of nearest neighbors, each four-fold coordinated. Various decorations of these Wyckoff positions generate the other structures:

- By decorating two second-neighbor atom sites identically, a Heusler alloy forms (Strukturbericht symbol $L2_1$).$^{43,79}$ For example, the following substitutions generate $Ag_2InZr$ (Figure 7(b)): $Pd \rightarrow Ag$, $Li \rightarrow Ag$, $Sn \rightarrow In$, and $Mg \rightarrow Zr$. Since the crystal now has an inversion center, the space group becomes $Fm\overline{3}m$ #225. As in LiMgPdSn, each atom has two sets of four-fold coordinated nearest neighbors, each arranged as a tetrahedron. Now, however, one species (Ag) has second-neighbors of the same type.
- By removing the Li atom completely, a half-Heusler forms $(C1_b)$.$^{43,80}$ There are two half-Heusler systems in Table 2: $AsCoTi$ (Figure 7(c)) and $BiRhZr$. The structure does differ from that of LiMgPdSn and $L2_1$, as the Ag and Ti atoms are four-fold coordinated, with only Co having the coordination seen in the previous structures.
- The majority of structures in Table 2 are type $C15_b$, prototype $AuBe_5^{43,81}$ (AFLOW prototype: AB5_cF24_216_a_ce$^{82}$), shown in Figure 7(d). Compared to the $C1_b$, $C15_b$ contains an (8e) Wyckoff position forming a tetrahedra centered around the (4b) Wyckoff position. Replacing the tetrahedra with a single atom returns the $C1_b$ structure.

Hence, of the 25 most stable ternary structures, 22 are of related structure.

Sampling bias likely plays a role in the high prominence of space group $F\overline{4}3m$ #216 structures in Table 2, but cannot account for the anomaly. Space group $F\overline{4}3m$ #216 constitutes about 17% of the LIB3 catalog, containing the bulk of the AFLOW.org repository (at over 1.4 million ternary systems) generated largely by small structure prototypes. For context, space group $F\overline{4}3m$ #216 is ranked about twentieth of the most common space groups in the ICSD,$^{83}$ appearing in about 1% of all entries. Further exploration of larger structure ternary prototypes covering the full range of space groups is needed to fully elucidate the nature of this structure's stability.

The regular-, inverse-, and half-Heusler prototypes were added to LIB3 for the exploration of new magnets, of which two were discovered.$^{4}$ The Heusler set includes more 236,000 structures, most of which remains unexplored. The fully sorted lists of stable binary and ternary phases are presented in the Supporting Information.

## 4. CONCLUSIONS

Thermodynamic analysis is a critical step for any effective materials design workflow. Being a collective characterization, thermodynamics requires comparisons between many configurations of the system. The availability of large databases$^{8-15}$ allows the construction of computationally-based phase diagrams. AFLOW-CHULL presents a complete software infrastructure, including flexible protocols for data retrieval, analysis, and verification.$^{12,44}$ The module is exhaustively applied to the AFLOW.org repository and identified several new candidate phases: 18 promising $C15_b$-type structures and two half-Heuslers. The extension of AFLOW-CHULL to repositories beyond AFLOW.org can be performed by adapting the open-source C++ code and/or Python module. Computational platforms such as AFLOW-CHULL are valuable tools for guiding synthesis, including high-throughput and even autonomous approaches.$^{84-87}$

## SUPPORTING INFORMATION

The material includes **i.** a snapshot (inventory) of binary and ternary alloy systems available in the AFLOW.org repository, **ii.** a full list of stable phases ranked by their relative stability criterion, **iii.** example scripts illustrating how to employ AFLOW-CHULL from within a Python environment, **iv.** a thermodynamic characterization of 493 binary systems, and **v.** 873 ternary systems. This information is available free of charge via the Internet at http://pubs.acs.org.

## ACKNOWLEDGEMENTS

We thank Drs. G. L. W. Hart, D. Usanmaz, R. Friedrich, M. Esters, P. Nath, D. Ford, P. Colinet, O. Isayev, A. Tropsha, N. Mingo, J. Carrete, and L. M. Ghiringhelli for insightful discussions. Research sponsored by the Department of Defense (ONR: N00014-17-1-2090, N00014-16-1-2583, N00014-16-1-2326, N00014-14-1-0526), and the National Science Foundation under DMREF Grants No. DMR-1436151. C. O. acknowledges support from the National Science Foundation Graduate Research Fellowship under Grant No. DGF1106401. D. H. acknowledges support from the Department of Defense through the National Defense Science and Engineering Graduate (NDSEG) Fellowship Program. S. C. acknowledges the Alexander von Humboldt-Foundation for financial support.

![](./images/812997670439223297_8.jpg)
![](./images/812997670439223297_9.jpg)
![](./images/812997670439223297_10.jpg)
![](./images/812997670439223297_11.jpg)

FIG. 7. Illustration of the most prevalent stable ternary structures. (a) The conventional cubic cell of the "quaternary- Heusler" structure, LiMgPdSn. Each species occupies a Wyckoff site of space group $F\overline{4}3m$ #216: Sn (purple) (4a), Mg (yellow)(4b), Pd (gray) (4c), and Li (blue) (4d). (b) The conventional cubic cell of the Heusler structure, here represented by $Ag_{2}InZr$. Each species occupies a Wyckoff site of space group $Fm\overline{3}m$ #225: In (pink) (4a), Zr (green) (4b), Ag (light gray) (8c). (c) The conventional cubic cell of the half-Heusler $C1_{b}$ structure, here represented by AsCoTi. Each species occupies a Wyckoff site of space group $F\overline{4}3m$ #216: Ti (light blue) (4a), As (purple) (4b), Co (dark blue) (4c). The (4d) site is empty. (d) The conventional cubic cell of the $C15_{b}$-type crystal, here represented by $Be_{4}OsTi$. Each species occupies a Wyckoff site of space group $F\overline{4}3m$ #216: Ti (light blue) (4a), Os (brown) (4c), and Be (light green) (8e). The (4d) site is empty, and the Be atoms form a tetrahedron centered around the (4b) site of (a).

## Appendix: AFLOW-CHULL manual

Command-line options. AFLOW-CHULL is an integrated module of the AFLOW ab-initio framework which runs on any UNIX-like computer, including those running macOS. The most up-to-date binary can be downloaded from aflow.org/src/aflow: current version 3.1.207. AFLOW-CHULL depends on the compiled binary executable and an internet connection, as all data is retrieved and analyzed in-situ. The default output option also requires the $L^A\TeX$ package. The results (graphics and PDF reports) presented herein are compiled using pdfTEX, Version 3.14159265-2.6-1.40.18 (TEX Live 2017).

The commands are as follows:
Primary commands:
- `aflow --chull --alloy=InNiY`
  - Calculates and returns the convex hull for system In-Ni-Y.
- `aflow --chull --alloy=InNiY --distance_to_hull=aflow:375066afdfb5a93f`
  - Calculates and returns the distance from the hull for $InNiY_{4}$.
- `aflow --chull --alloy=InNiY --stability_criterion=aflow:60a36639191c0af8`
  - Calculates and returns the stability criterion for $InNi_{4}Y$. The structure and relevant duplicates (if any) are removed simultaneously.
- `aflow --chull --alloy=InNiY --hull_formation_enthalpy=0.25,0.25`
  - Calculates and returns the formation enthalpy of the minimum energy surface at $In_{0.25}Ni_{0.25}Y_{0.5}$. The input composition is specified by implicit coordinates (refer to Equation 4), where the last coordinate offers an optional energetic shift.
- `aflow --chull --usage`
  - Prints full set of commands to the screen.
- `aflow --readme=chull`
  - Prints a verbose manual (commands and descriptions) to the screen.

General options:
- `--output=pdf`
  - Selects the output format. Options include: `pdf`, `png`, `json`, `txt`, and `full`. For multiple output, provide a comma-separated value list. A file with the corresponding extension is created, e.g., `aflow_InNiY_hull.pdf`.
- `--destination=$HOME/`
  - Sets the output path to $HOME. All output will be redirected to this destination.
- `--keep=log`
  - Creates a log file with verbose output of the calculation, e.g., `aflow_InNiY_hull.log`.

Loading options:
- `--load_library=icsd`
  - Limits the catalogs from which entries are loaded. Options include: `icsd`, `lib1`, `lib2`, and `lib3`. For multiple catalogs, provide a comma-separated value list.
- `--load_entries_entry_output`

- Prints verbose output of the entries loaded. This output is included in the log file by default.
- **`--neglect=aflow:60a36639191c0af8,aflow:3f24d2be765237f1,...`**
  - Excludes individual points from the convex hull calculation.
- **`--see_neglect`**
  - Prints verbose output of the entries neglected from the calculation, including ill-calculated entries, duplicates, outliers, and those requested via `--neglect`.
- **`--remove_extreme_points=-1000`**
  - Excludes all points with formation enthalpies below -1000 meV/atom.
- **`--include_paw_gga`**
  - Includes all entries calculated with PAW-GGA (in addition to those calculated with PAW-PBE). PAW-GGA refers to the Generalized Gradient Approximation functional⁶³ with pseudopotentials calculated with the projector augmented wave method.⁶⁴ This flag is needed to generate Figure 4(f).

**Analysis options:**
- **`--skip_structure_comparison`**
  - Avoids robust determination of structures equivalent to stable phases (speed).
- **`--skip_stability_criterion_analysis`**
  - Avoids determination of the stability criterion of stable phases (speed).
- **`--include_skewed_hulls`**
  - Proceeds to calculate the hull in the event that it is determined "skewed", *i.e.*, the stable elemental phase differs from the reference energy by more than 15 meV/atom. This flag is needed to generate Figure 4(f).
- **`--include_unreliable_hulls`**
  - Proceeds to calculate the hull in the event that it is determined unreliable (fewer than 200 entries).
- **`--include_outliers`**
  - Avoids the exclusion of outliers.
- **`--force`**
  - Forces an output, ignoring all warnings.

**PDF/LATEX options:**
- **`--image_only`**
  - Creates a PDF with the hull illustration only.
- **`--document_only`**
  - Creates a PDF with the thermodynamic report only. Default for dimensions $N>3$.
- **`--keep=tex`**
  - Saves the LATEX input file (deleted by default), allowing for customization of the resulting PDF, *e.g.*, `aflow_InNiY_hull.tex`.
- **`--latex_interactive`**
  - Displays the LATEX compilation output and enables interaction with the program.
- **`--plot_iso_max_latent_heat`**
  - Plots the entropic temperature envelopes shown in Figure 4(f). Limited to binary systems only.

**AFLOWrc options.** The `.aflow.rc` file is a new protocol for specifying AFLOW default options. The file emulates the `.bashrc` script that runs when initializing an interactive environment in Bash (Bourne again shell). A fresh `.aflow.rc` file is created in `$HOME` if one is not already present.

**Relevant AFLOW-CHULL options include:**
- **`DEFAULT_CHULL_ALLOWED_DFT_TYPES="PAW_PBE"`**
  - *Description:* Defines the allowed entries based on density functional theory (DFT) calculation type (comma-separated value). Options include: US, GGA, PAW_LDA, PAW_GGA, PAW_PBE, GW, and HSE06.⁹
  - *Type:* `string`
- **`DEFAULT_CHULL_ALLOW_ALL_FORMATION_ENERGIES=0`**
  - *Description:* Allows all entries independent of DFT calculation type.⁹
  - *Type:* `0` (`false`) or `1` (`true`)
- **`DEFAULT_CHULL_COUNT_THRESHOLD_BINARIES=200`**
  - *Description:* Defines the minimum number of entries for a reliable binary hull.
  - *Type:* `integer`
- **`DEFAULT_CHULL_PERFORM_OUTLIER_ANALYSIS=1`**
  - *Description:* Enables determination of outliers.
  - *Type:* `0` (`false`) or `1` (`true`)
- **`DEFAULT_CHULL_OUTLIER_ANALYSIS_COUNT_THRESHOLD_BINARIES=50`**

- *Description:* Defines the minimum number of entries for a reliable outlier analysis. Only phases stable with respect to their end-members are considered for the outlier analysis (below the zero $H_f$ tie-line).
- *Type:* integer

• DEFAULT_CHULL_OUTLIER_MULTIPLIER=3.25
- *Description:* Defines the bounds beyond the interquartile range for which points are considered outliers.⁶⁷
- *Type:* double

• DEFAULT_CHULL_IGNORE_KNOWN_ILL_CONVERGED=1
- *Description:* AFLOW maintains a list of (older) prototypes known to have converged poorly. These entries are likely outliers, *e.g.*, see prototype 549 in Figure 4(a). If this flag is on (1), then the entries are removed before the analysis. Turning this flag off (0) is not recommended.
- *Type:* 0 (false) or 1 (true)

• DEFAULT_CHULL_LATEX_PLOT_UNARIES=0
- *Description:* Incorporates the end-members in the convex hull illustration.
- *Type:* 0 (false) or 1 (true)

• DEFAULT_CHULL_LATEX_PLOT_OFF_HULL=-1
- *Description:* Incorporates off-hull phases in the convex hull illustration, but excludes phases unstable with respect to their end-members (above the zero $H_f$ tie-line). Only three values are accepted: -1 (default: true for 2-dimensional systems, false for 3-dimensional systems), 0 (false), 1 (true).
- *Type:* -1 (default), 0 (false), or 1 (true)

• DEFAULT_CHULL_LATEX_PLOT_UNSTABLE=0
- *Description:* Incorporates all unstable phases in the convex hull illustration.
- *Type:* 0 (false) or 1 (true)

• DEFAULT_CHULL_LATEX_FILTER_SCHEME=""
- *Description:* Defines the exclusion scheme for the convex hull illustration. In contrast to `--neglect`, this scheme is limited to the illustration, and points are still included in the analysis/report. The following strings are accepted: `Z-axis` (also `Energy-axis`) or `Distance`. `Z-axis` refers to a scheme that eliminates structures from the illustration based on their formation enthalpy. On the other hand, `Distance` refers to a scheme that eliminates structures from the illustration based on their distances from the hull. The criteria (value) for elimination is defined by DEFAULT_CHULL_LATEX_FILTER_VALUE.
- *Type:* string

• DEFAULT_CHULL_LATEX_FILTER_VALUE=50
- *Description:* Defines the value beyond which points are excluded per the scheme defined with DEFAULT_CHULL_LATEX_FILTER_SCHEME. In this case, AFLOW-CHULL would filter points with energies greater than 50 meV.
- *Type:* double

• DEFAULT_CHULL_LATEX_COLOR_BAR=1
- *Description:* Defines whether to show the color bar graphic (3-dimensional illustration only). Colors can still be incorporated without the color bar graphic.
- *Type:* 0 (false) or 1 (true)

• DEFAULT_CHULL_LATEX_HEAT_MAP=1
- *Description:* Defines whether to color the facets with heat maps illustrating their depth (3-dimensional illustration only).
- *Type:* 0 (false) or 1 (true)

• DEFAULT_CHULL_LATEX_COLOR_GRADIENT=1
- *Description:* Defines whether to incorporate a color scheme at all in the illustration. Turning this flag off will also turn off DEFAULT_CHULL_LATEX_COLOR_BAR and DEFAULT_CHULL_LATEX_HEAT_MAP.
- *Type:* 0 (false) or 1 (true)

• DEFAULT_CHULL_LATEX_COLOR_MAP=""
- *Description:* Defines the color map, options are presented in Ref. 88. Default is `rgb(0pt)=(0.035,0.270,0.809); rgb(63pt)=(1,0.644,0)`.
- *Type:* string

• DEFAULT_CHULL_CHULL_LINKS=1
- *Description:* Defines the links scheme. True/false, *i.e.*, 0/1, will toggle all links on/off. 2 enables external hyperlinks only (no links to other sections of the PDF). 3 enables internal links only (no links to external pages).
- *Type:* 0 (false), 1 (true), 2 (external-only), or 3 (internal-only)

• DEFAULT_CHULL_CHULL_LABEL_NAME=""
- *Description:* Defines the labeling scheme for phases shown on the convex hull. By default, the compound label is shown, while the prototype label can also be specified. `icsd` shows the ICSD entry number designation (lowest

for multiple equivalent ground-state structures reflecting `icsd_canonical_auid`) if appropriate, as shown in Figure 4(c). Also acceptable: both (compound and prototype) and none.

- *Type:* string
- **DEFAULT_CHULL_LATEX_META_LABELS=0**
  - *Description:* Enables verbose labels, including compound, prototype, $H_\mathrm{f}$, $T_\mathrm{S}$, and $\Delta H_\mathrm{f}$. Warning, significant overlap of labels should be expected.
  - *Type:* 0 (false) or 1 (true)
- **DEFAULT_CHULL_LATEX_LABELS_OFF_HULL=0**
  - *Description:* Enables labels for off-hull points.
  - *Type:* 0 (false) or 1 (true)
- **DEFAULT_CHULL_LATEX_HELVETICA_FONT=1**
  - *Description:* Switches the font scheme from Computer Modern (default) to Helvetica.
  - *Type:* 0 (false) or 1 (true)
- **DEFAULT_CHULL_LATEX_FONT_SIZE=""**
  - *Description:* Defines the font size of the labels on the convex hull illustration. Warning, other settings may override this default. Options include: tiny, scriptsize, footnotesize, small, normalsize, large (default), Large, LARGE, huge, and Huge.
  - *Type:* string
- **DEFAULT_CHULL_LATEX_ROTATE_LABELS=1**
  - *Description:* Toggles whether labels are rotated.
  - *Type:* 0 (false) or 1 (true)
- **DEFAULT_CHULL_LATEX_BOLD_LABELS=-1**
  - *Description:* Toggles whether labels are bolded. Three values are accepted: -1 (default: false unless phase is a ternary), 0 (false), 1 (true).
  - *Type:* -1 (default), 0 (false), or 1 (true)

Image generation. Instructions for generating the images herein are provided below. Many of these images can be generated automatically with AFLOW-CHULL.

Figure 1(a): `run aflow --chull --alloy=CoTi --image_only`.

Figure 1(b): `run aflow --chull --alloy=MnPdPt --image_only`.

Figure 2: **i.** the Pd-Pt hull was first generated by running `aflow --chull --alloy=PdPt --image_only --keep=tex`, **ii.** the resulting LATEX input file (aflow_PdPt_hull.tex) was modified by hand and compiled to get the various hull illustrations, **iii.** the overall flowchart was constructed with Microsoft PowerPoint.

Figure 3: **i.** the Al-Ni, Al-Ti, and Ni-Ti binary hulls were first generated by running `aflow --chull --alloy=AlNi,AlTi,NiTi --image_only --keep=tex`, **ii.** the resulting LATEX input files (aflow_AlNi_hull.tex, aflow_AlTi_hull.tex, and aflow_NiTi_hull.tex) were modified by hand and compiled to get the binary hull images, **iii.** a snapshot of the Al-Ni-Ti ternary hull was taken from the web application at aflow.org/aflow-chull, **iv.** the overall illustration was constructed with Adobe Illustrator.

Figure 4(a): set `DEFAULT_CHULL_IGNORE_KNOWN_ILL_CONVERGED=0` in the `.aflow.rc` and run `aflow --chull --alloy=AlCo --image_only`.

Figure 4(b): set `DEFAULT_CHULL_IGNORE_KNOWN_ILL_CONVERGED=1` in the `.aflow.rc` and run `aflow --chull --alloy=AlCo --image_only`.

Figure 4(c): set `DEFAULT_CHULL_LATEX_LABEL_NAME=''icsd''` in the `.aflow.rc` and run `aflow --chull --alloy=TeZr --image_only`.

Figure 4(d): **i.** the Pd-Pt hull was first generated by running `aflow --chull --alloy=PdPt --image_only --keep=tex`, **ii.** the resulting LATEX input file (aflow_PdPt_hull.tex) was modified by hand and compiled to get the hull illustration. $\Delta H_\mathrm{f}$ [aflow:71bc1b15525ffa35] can be calculated individually by running `aflow --chull --alloy=PdPt --distance_to_hull=aflow:71bc1b15525ffa35`.

Figure 4(e): **i.** the Pd-Pt hull was first generated by running `aflow --chull --alloy=PdPt --image_only --keep=tex`, **ii.** the resulting LATEX input file (aflow_PdPt_hull.tex) was modified by hand and compiled to get the hull illustration. $\delta_\mathrm{sc}$ [aflow:f31b0e27897cd162] can be calculated individually by running `aflow --chull --alloy=PdPt --stability_criterion=aflow:f31b0e27897cd162`.

Figure 4(f): `run aflow --chull --alloy=BSm --image_only --plot_iso_max_latent_heat --include_paw_gga --include_skewed_hulls`.

Figure 5: `run aflow --chull --alloy=AgAuCd`.

Figure 6(a): navigate to aflow.org/aflow-chull and select the Mo-Ti hull.

Figure 6(b): navigate to aflow.org/aflow-chull and select the Fe-Rh-Zr hull.

Figure 6(c): navigate to aflow.org/aflow-chull, select the Au-Cu-Zr, Au-Cu, and AuZr hulls by clicking "Periodic Ta- ble" from the navigation bar on the top right corner of the screen between selections, and click "Hull History" from the navigation bar on the top right corner of the screen.

Figure 6(d): navigate to aflow.org/aflow-chull, select the Au-Cu-Zr hull, click on several points in the 3-dimensional illustration to populate the "Select Points" table on the left side of the screen, then click on one of the points in the table.

Figures 7(a-d): the structures were visualized with the CrystalMaker X software.

Python environment. A module has been created that employs AFLOW-CHULL within a Python environment. The module and its description follow that of the AFLOW-SYM Python module.⁴⁵ It connects to a local AFLOW installation and imports the AFLOW-CHULL results into a `CHull` class. A `CHull` object is initialized with:

```
from aflow.hull import CHull
from pprint import pprint

chull = CHull(aflow_executable = './aflow')
alloy = 'AlCuZr'
output = chull.get_hull(alloy)
pprint(output)
```

By default, the `CHull` object searches for an AFLOW executable in the `$PATH`. However, the location of an AFLOW executable can be specified as follows:
`CHull(aflow_executable=$HOME/bin/aflow)`.

The `CHull` object contains built-in methods corresponding to the command line calls mentioned previously:
- `get_hull('InNiY', options = '--keep=log')`
- `get_distance_to_hull('InNiY', 'aflow:375066afdfb5a93f', options = '--keep=log')`
- `get_stability_criterion('InNiY', 'aflow:60a36639191c0af8', options = '--keep=log')`
- `get_hull_energy('InNiY', [0.25,0.25], options = '--keep=log')`

Each method requires an input alloy string and allows an additional parameters/flags string to be passed via `options`. `get_distance_to_hull` and `get_stability_criterion` require an additional string input for the auid, while `get_hull_energy` takes an array of doubles as its input for the composition.

Python module. The module to run the aforementioned AFLOW-CHULL commands is provided below. This module can be modified to incorporate additional/customized options.

```
import json
import subprocess
import os

class CHull:

    def __init__(self, aflow_executable='aflow'):
        self.aflow_executable = aflow_executable

    def aflow_command(self, cmd):
        try:
            return subprocess.check_output(
                self.aflow_executable + cmd,
                shell=True
            )
        except subprocess.CalledProcessError:
            print('Error aflow executable not found at: ' + self.aflow_executable)

    def get_hull(self, alloy, options = None):
        command = ' --chull'
        if options:
            command += ' ' + options
```

ACS Paragon Plus Environment

```python
output = ''
output = self.aflow_command(
    command + ' --print=json --screen_only --alloy=' + alloy
)
res_json = json.loads(output)
return res_json

def get_distance_to_hull(self, alloy, off_hull_point, options = None):
    command = ' --chull --distance_to_hull=' + off_hull_point
    if options:
        command += ' ' + options

    output = ''
    output = self.aflow_command(
        command + ' --print=json --screen_only --alloy=' + alloy
    )
    res_json = json.loads(output)
    return res_json

def get_stability_criterion(self, alloy, hull_point, options = None):
    command = ' --chull --stability_criterion=' + hull_point
    if options:
        command += ' ' + options

    output = ''
    output = self.aflow_command(
        command + ' --print=json --screen_only --alloy=' + alloy
    )
    res_json = json.loads(output)
    return res_json

def get_hull_energy(self, alloy, composition, options = None):
    command = ' --chull --hull_energy=' + ','.join([ str(comp) for comp in composition ])
    if options:
        command += ' ' + options

    output = ''
    output = self.aflow_command(
        command + ' --print=json --screen_only --alloy=' + alloy
    )
    res_json = json.loads(output)
    return res_json
```

Stability analysis. A Python script is provided below demonstrating how to perform the stability analysis presented in the Results section. The script gathers the most stable binary compounds generated from 2-element combinations of elements. Compounds are filtered for binary ground-state structures not in the ICSD. Only unique compositions are saved. The script writes the results to the JSON file most_stable_binaries.json and prints them to screen. The script can be adapted for ternary systems and incorporating the full set of elements. Considering the full number of combinations, it is recommended that the script be adapted to generate the hulls in parallel.

```python
from aflow_hull import CHull
import json
from pprint import pprint

elements = ['Mn', 'Pd', 'Pt'] #extend as needed
elements.sort()
```

```python
most_stable_binaries = [] #final list
saved_points_rc = []      #easy way to avoid adding duplicate compositions

chull = CHull(aflow_executable = './aflow') #initialize hull object
for i in range(len(elements)):            #generate binary alloy combinations
    for j in range(i + 1, len(elements)):    #generate binary alloy combinations
        alloy = elements[i]+elements[j]      #generate binary alloy combinations
        output = chull.get_hull(alloy)       #get hull data
        points_data = output['points_data'] #grab points data
        for point in points_data:
            #filter for binary ground-state structures not in the ICSD
            if point['ground_state'] and not point['icsd_ground_state'] and point['nspecies'] == 2:
                #easy way to avoid adding duplicate compositions
                if point['reduced_compound'] not in saved_points_rc:
                    saved_points_rc.append(point['reduced_compound'])
                    #save only what is necessary
                    abridged_entry = {}
                    abridged_entry['compound'] = point['compound']
                    abridged_entry['prototype'] = point['prototype']
                    abridged_entry['auid'] = point['auid']
                    abridged_entry['aurl'] = point['aurl']
                    abridged_entry['relative_stability_criterion'] = point['relative_stability_criterion']
                    most_stable_binaries.append(abridged_entry)

most_stable_binaries = sorted(most_stable_binaries, key=lambda point: -point['relative_stability_criterion'])    #sort in descending order

#save data to JSON file
with open('most_stable_binaries.json', 'w') as fout:
    json.dump(most_stable_binaries, fout)

#also print output to screen
pprint(most_stable_binaries)
```

Output list. This section details the output fields for the thermodynamic analysis. The lists describe the keywords as they appear in the JSON format. Similar keywords are used for the standard text output.

Points data (points_data).
- **auid**
  - *Description:* AFLOW unique ID.⁹
  - *Type:* string
- **aurl**
  - *Description:* AFLOW uniform resource locator.⁹
  - *Type:* string
- **compound**
  - *Description:* Compound name.⁹
  - *Type:* string
- **enthalpy_formation_atom**
  - *Description:* Formation enthalpy per atom ($H_{\text{f}}$).⁹
  - *Type:* double
  - *Units:* meV/atom
- **enthalpy_formation_atom_difference**
  - *Description:* Energy driving the decomposition reaction ($\Delta H_{\text{f}}$), *i.e.*, the distance to the hull.
  - *Type:* double
  - *Units:* meV/atom
- **entropic_temperature**

- *Description:* The ratio of the formation enthalpy and the ideal mixing entropy $(T_{\mathrm{S}}).^{29}$ This term defines the ideal "iso-max-latent-heat" lines of the grand-canonical ensemble. $^{29,48}$ Refer to Figure 4.
- *Type:* double
- *Units:* Kelvin

- **equivalent_structures_auid**
  - *Description:* auid of structurally equivalent entries. This analysis is limited to stable phases only.
  - *Type:* array of strings

- **ground_state**
  - *Description:* True for stable phases, and false otherwise.
  - *Type:* boolean

- **icsd_canonical_auid**
  - *Description:* auid of an equivalent ICSD entry. If there are multiple equivalent ICSD entries, the one with the lowest number designation is chosen (original usually). This analysis is limited to stable phases only.
  - *Type:* string

- **icsd_ground_state**
  - *Description:* True for stable phases with an equivalent ICSD entry, and false otherwise.
  - *Type:* boolean

- **nspecies**
  - *Description:* The number of species in the system (e.g., binary = 2 and ternary = 3).
  - *Type:* integer

- **phases_decomposition_auid**
  - *Description:* auid of the products of the decomposition reaction (stable phases). This analysis is limited to unstable phases only.
  - *Type:* array of strings

- **phases_decomposition_coefficient**
  - *Description:* Coefficients of the decomposition reaction normalized to reactant, i.e., $\mathbf{N}$ from Equation 9. Hence, the first entry is always 1. This analysis is limited to unstable phases only.
  - *Type:* array of doubles

- **phases_decomposition_compound**
  - *Description:* compound of the products of the decomposition reaction (stable phases). This analysis is limited to unstable phases only.
  - *Type:* array of strings

- **phases_equilibrium_auid**
  - *Description:* auid of phases in coexistence. This analysis is limited stable phases only.
  - *Type:* array of strings

- **phases_equilibrium_compound**
  - *Description:* compound of phases in coexistence. This analysis is limited stable phases only.
  - *Type:* array of strings

- **prototype**
  - *Description:* AFLOW prototype designation. $^{9}$
  - *Type:* string

- **relative_stability_criterion**
  - *Description:* A dimensionless quantity capturing the effect of the phase on the minimum energy surface relative to its depth, i.e., $\delta_{\mathrm{sc}} / H_{\mathrm{f}}$.
  - *Type:* double

- **space_group_orig**
  - *Description:* The space group (symbol and number) of the structure pre-relaxation as determined by AFLOW-SYM. $^{45}$
  - *Type:* string

- **space_group_relax**
  - *Description:* The space group (symbol and number) of the structure post-relaxation as determined by AFLOW-SYM. $^{45}$
  - *Type:* string

- **spin_atom**
  - *Description:* The magnetization per atom for spin polarized calculations. $^{9}$
  - *Type:* double
  - *Units:* $\mu_{\mathrm{B}} /$ atom.

- **stability_criterion**

- Description: A metric for robustness of a stable phase ($\delta_{\text{sc}}$), i.e., the distance of a stable phase from the pseudo-hull constructed without it. This analysis is limited to stable phases only.
- Type: double
- Units: meV/atom

- url_entry_page
  - Description: The URL to the entry page: http://aflow.org/material.php?id=aflow:60a36639191c0af8.
  - Type: string

Facets data (facets_data).

- artificial
  - Description: True if the facet is artificial, i.e., defined solely by artificial end-points, and false otherwise.
  - Type: boolean
- centroid
  - Description: The centroid of the facet.
  - Type: array of doubles
  - Units: Stoichiometric-energetic coordinates as defined by Equation 4.
- content
  - Description: The content (hyper-volume) of the facet.
  - Type: array of doubles
  - Units: Stoichiometric-energetic coordinates as defined by Equation 4.
- hypercollinearity
  - Description: True if the facet has no content, i.e., exhibits hyper-collinearity, and false otherwise.
  - Type: boolean
- normal
  - Description: The normal vector characterizing the facet, i.e., $\mathbf{n}$ in Equation 5.
  - Type: double
  - Units: Stoichiometric-energetic coordinates as defined by Equation 4.
- offset
  - Description: The offset in the hyperplane description of the facet, i.e., $D$ in Equation 5.
  - Type: double
  - Units: Stoichiometric-energetic coordinates as defined by Equation 4.
- vertical
  - Description: True if the facet is vertical along the energetic axis, and false otherwise.
  - Type: boolean
- vertices_auid
  - Description: auid of the phases that define the vertices of the facet.
  - Type: array of strings
- vertices_compound
  - Description: compound of the phases that define the vertices of the facet.
  - Type: array of strings
- vertices_position
  - Description: Coordinates that define the vertices of the facet.
  - Type: array of arrays of doubles
  - Units: Stoichiometric-energetic coordinates as defined by Equation 4.

AFLOW forum. Updates about AFLOW-CHULL are discussed in the AFLOW forum (aflow.org/forum): "Thermodynamic analysis".

![](./images/812997670439223297_12.jpg)

FIG. 8. TOC graphic.

* stefano@duke.edu

1 Jansen, M. A Concept for Synthesis Planning in SolidState Chemistry, *Angew. Chem. Int. Ed.* 2002, 41, 3746–3766.

2 Potyrailo, R.; Rajan, K.; Stoewe, K.; Takeuchi, I.; Chisholm, B.; Lam, H. Combinatorial and high-throughput screening of materials libraries: Review of state of the art, *ACS Comb. Sci.* 2011, 13, 579–633.

3 Kuz’mín, M. D.; Skokov, K. P.; Jian, H.; Radulov, I.; Gutfleisch, O. Towards high-performance permanent magnets without rare earths, *J. Phys.: Condens. Matter* 2014, 26, 064205.

4 Sanvito, S.; Oses, C.; Xue, J.; Tiwari, A.; Zic, M.; Archer, T.; Tozman, P.; Venkatesan, M.; Coey, J. M. D.; Curtarolo, S. Accelerated discovery of new magnets in the Heusler alloy family, *Sci. Adv.* 2017, 3, e1602241.

5 Villars, P.; Okamoto, H.; Cenzual, K. ASM Alloy Phase Diagram Database. http://www1.asminternational.org/AsmEnterprise/APD (accessed August 13, 2018).

6 Walsh, A. Inorganic materials: The quest for new functionality, *Nat. Chem.* 2015, 7, 274–275.

7 Isayev, O.; Oses, C.; Toher, C.; Gossett, E.; Curtarolo, S.; Tropsha, A. Universal fragment descriptors for predicting electronic properties of inorganic crystals, *Nat. Commun.* 2017, 8, 15679.

8 Curtarolo, S.; Setyawan, W.; Wang, S.; Xue, J.; Yang, K.; Taylor, R. H.; Nelson, L. J.; Hart, G. L. W.; Sanvito, S.; Buongiorno Nardelli, M.; Mingo, N.; Levy, O. AFLOWLIB.ORG: A distributed materials properties repository from high-throughput *ab initio* calculations, *Comput. Mater. Sci.* 2012, 58, 227–235.

9 Taylor, R. H.; Rose, F.; Toher, C.; Levy, O.; Yang, K.; Buongiorno Nardelli, M.; Curtarolo, S. A RESTful API for exchanging materials data in the AFLOWLIB.org consortium, *Comput. Mater. Sci.* 2014, 93, 178–192.

10 Calderon, C. E.; Plata, J. J.; Toher, C.; Oses, C.; Levy, O.; Fornari, M.; Natan, A.; Mehl, M. J.; Hart, G. L. W.; Buongiorno Nardelli, M.; Curtarolo, S. The AFLOW standard for high-throughput materials science calculations, *Comput. Mater. Sci.* 2015, 108 Part A, 233–238.

11 Rose, F.; Toher, C.; Gossett, E.; Oses, C.; Buongiorno Nardelli, M.; Fornari, M.; Curtarolo, S. AFLUX: The LUX materials search API for the AFLOW data repositories, *Comput. Mater. Sci.* 2017, 137, 362–370.

12 Scheffler, M.; Draxl, C.; Computer Center of the Max-Planck Society, Garching. The NoMaD Repository. http://nomad-repository.eu (accessed August 13, 2018).

13 Jain, A.; Ong, S. P.; Hautier, G.; Chen, W.; Richards, W. D.; Dacek, S.; Cholia, S.; Gunter, D.; Skinner, D.; Ceder, G.; Persson, K. A. Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, *APL Mater.* 2013, 1, 011002.

14 Saal, J. E.; Kirklin, S.; Aykol, M.; Meredig, B.; Wolverton, C. Materials Design and Discovery with High-Throughput Density Functional Theory: The Open Quantum Materials Database (OQMD), *JOM* 2013, 65, 1501–1509.

15 Landis, D. D.; Hummelshøj, J. S.; Nestorov, S.; Greeley, J.; Dulak, M.; Bligaard, T.; Nørskov, J. K.; Jacobsen, K. W. The Computational Materials Repository, *Comput. Sci. Eng.* 2012, 14, 51–57.

16 Pizzi, G.; Cepellotti, A.; Sabatini, R.; Marzari, N.; Kozin-sky, B. AiiDA: automated interactive infrastructure and database for computational science, *Comput. Mater. Sci.* 2016, 111, 218–230.

17 Nyshadham, C.; Oses, C.; Hansen, J. E.; Takeuchi, I.; Curtarolo, S.; Hart, G. L. W. A computational high-throughput search for new ternary superalloys, *Acta Mater.* 2017, 122, 438–447.

18 Bechtel, J. S.; Van der Ven, A. First-principles thermodynamics study of phase stability in inorganic halide perovskite solid solutions, *Phys. Rev. Mater.* 2018, 2, 045401.

19 Li, W.; Jacobs, R.; Morgan, D. Predicting the thermodynamic stability of perovskite oxides using machine learning models, *Comput. Mater. Sci.* 2018, 150, 454–463.

20 Balachandran, P. V.; Emery, A. A.; Gubernatis, J. E.; Lookman, T.; Wolverton, C.; Zunger, A. Predictions of new $ABO_3$ perovskite compounds by combining machine learning and density functional theory, *Phys. Rev. Mater.* 2018, 2, 043802.

21 Levy, O.; Hart, G. L. W.; Curtarolo, S. Uncovering Compounds by Synergy of Cluster Expansion and HighThroughput Methods, *J. Am. Chem. Soc.* 2010, 132, 4830–4833.

22 Levy, O.; Hart, G. L. W.; Curtarolo, S. Hafnium binary alloys from experiments and first principles, *Acta Mater.* 2010, 58, 2887–2897.

23 Levy, O.; Chepulskii, R. V.; Hart, G. L. W.; Curtarolo, S. The New Face of Rhodium Alloys: Revealing Ordered Structures from First Principles, *J. Am. Chem. Soc.* 2010, 132, 833–837.

24 Levy, O.; Hart, G. L. W.; Curtarolo, S. Structure maps for hcp metals from first-principles calculations, *Phys. Rev. B* 2010, 81, 174106.

25 Levy, O.; Jahnátek, M.; Chepulskii, R. V.; Hart, G. L. W.; Curtarolo, S. Ordered Structures in Rhenium Binary Alloys from First-Principles Calculations, *J. Am. Chem. Soc.* 2011, 133, 158–163.

26 Jahnátek, M.; Levy, O.; Hart, G. L. W.; Nelson, L. J.; Chepulskii, R. V.; Xue, J.; Curtarolo, S. Ordered phases in ruthenium binary alloys from high-throughput firstprinciples calculations, *Phys. Rev. B* 2011, 84, 214110.

27 Levy, O.; Xue, J.; Wang, S.; Hart, G. L. W.; Curtarolo, S. Stable ordered structures of binary technetium alloys from first principles, *Phys. Rev. B* 2012, 85, 012201.

28 Bloch, J.; Levy, O.; Pejova, B.; Jacob, J.; Curtarolo, S.; Hjorvarsson, B. Prediction and Hydrogen Acceleration of Ordering in Iron-Vanadium Alloys, *Phys. Rev. Lett.* 2012, 108, 215503.

29 Hart, G. L. W.; Curtarolo, S.; Massalski, T. B.; Levy, O. Comprehensive Search for New Phases and Compounds in Binary Alloy Systems Based on Platinum-Group Metals, Using a Computational First-Principles Approach, *Phys. Rev. X* 2013, 3, 041035.

30 Barzilai, S.; Toher, C.; Curtarolo, S.; Levy, O. Evaluation of the tantalum-titanium phase diagram from *ab-initio* calculations, *Acta Mater.* 2016, 120, 255–263.

31 Perim, E.; Lee, D.; Liu, Y.; Toher, C.; Gong, P.; Li, Y.; Simmons, W. N.; Levy, O.; Vlassak, J. J.; Schroers, J.; Curtarolo, S. Spectral descriptors for bulk metallic glasses based on the thermodynamics of competing crystalline phases, *Nat. Commun.* 2016, 7, 12315.

32 Barzilai, S.; Toher, C.; Curtarolo, S.; Levy, O. The effect of

lattice stability determination on the computational phase diagrams of intermetallic alloys, J. Alloys Compd. 2017, 728, 314−321.

33 Barzilai, S.; Toher, C.; Curtarolo, S.; Levy, O. Molybdenum-titanium phase diagram evaluated from ab initio calculations, Phys. Rev. Mater. 2017, 1, 023604.

34 Hever, A.; Oses, C.; Curtarolo, S.; Levy, O.; Natan, A. The Structure and Composition Statistics of 6A Binary and Ternary Crystalline Materials, Inorg. Chem. 2018, 57, 653−667.

35 Rost, C. M.; Sachet, E.; Borman, T.; Moballegh, A.; Dickey, E. C.; Hou, D.; Jones, J. L.; Curtarolo, S.; Maria, J.-P. Entropy-stabilized oxides, Nat. Commun. 2015, 6, 8485.

36 Rak, Z.; Rost, C. M.; Lim, M.; Sarker, P.; Toher, C.; Cur- tarolo, S.; Maria, J.-P.; Brenner, D. W. Charge compen- sation and electrostatic transferability in three entropy- stabilized oxides: Results from density functional theory calculations, J. Appl. Phys. 2016, 120, 095105.

37 Lederer, Y.; Toher, C.; Vecchio, K. S.; Curtarolo, S. The search for high entropy alloys: a high- throughput ab-initio approach, Acta Mater. 2018. Doi:10.1016/j.actamat.2018.07.042.

38 GNU General Public License. http://www.gnu.org/ licenses (accessed August 13, 2018).

39 Curtarolo, S.; Setyawan, W.; Hart, G. L. W.; Jahnátek, M.; Chepulskii, R. V.; Taylor, R. H.; Wang, S.; Xue, J.; Yang, K.; Levy, O.; Mehl, M. J.; Stokes, H. T.; Dem- chenko, D. O.; Morgan, D. AFLOW: An automatic frame- work for high-throughput materials discovery, Comput. Mater. Sci. 2012, 58, 218−226.

40 Yang, K.; Oses, C.; Curtarolo, S. Modeling Off- Stoichiometry Materials with a High-Throughput Ab- Initio Approach, Chem. Mater. 2016, 28, 6484−6492.

41 Carrete, J.; Mingo, N.; Wang, S.; Curtarolo, S. Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: An Ab Initio High-Throughput Statis- tical Study, Adv. Func. Mater. 2014, 24, 7427−7432.

42 Setyawan, W.; Curtarolo, S. High-throughput electronic band structure calculations: Challenges and tools, Com- put. Mater. Sci. 2010, 49, 299−312.

43 Mehl, M. J.; Hicks, D.; Toher, C.; Levy, O.; Hanson, R. M.; Hart, G. L. W.; Curtarolo, S. The AFLOW Library of Crystallographic Prototypes: Part 1, Comput. Mater. Sci. 2017, 136, S1−S828.

44 Supka, A. R.; Lyons, T. E.; Liyanage, L. S. I.; D’Amico, P.; Al Rahal Al Orabi, R.; Mahatara, S.; Gopal, P.; To- her, C.; Ceresoli, D.; Calzolari, A.; Curtarolo, S.; Buon- giorno Nardelli, M.; Fornari, M. AFLOWπ: A minimalist approach to high-throughput ab initio calculations includ- ing the generation of tight-binding hamiltonians, Comput. Mater. Sci. 2017, 136, 76−84.

45 Hicks, D.; Oses, C.; Gossett, E.; Gomez, G.; Taylor, R. H.; Toher, C.; Mehl, M. J.; Levy, O.; Curtarolo, S. AFLOW-SYM: platform for the complete, automatic and self-consistent symmetry analysis of crystals, Acta Crys- tallogr. Sect. A 2018, 74, 184−203.

46 Rohrer, G. S.; Affatigato, M.; Backhaus, M.; Bordia, R. K.; Chan, H. M.; Curtarolo, S.; Demkov, A.; Eckstein, J. N.; Faber, K. T.; Garay, J. E.; Gogotsi, Y.; Huang, L.; Jones, L. E.; Kalinin, S. V.; Lad, R. J.; Levi, C. G.; Levy, J.; Maria, J.-P.; Mattos Jr., L.; Navrotsky, A.; Orlovskaya, N.; Pantano, C.; Stebbins, J. F.; Sudarshan, T. S.; Tani, T.; Weil, K. S. Challenges in Ceramic Science: A Report from the Workshop on Emerging Research Areas in Ce- ramic Science, J. Am. Ceram. Soc. 2012, 95, 3699−3712.

47 Barber, C. B.; Dobkin, D. P.; Huhdanpaa, H. The quick- hull algorithm for convex hulls, ACM Trans. Math. Soft. 1996, 22, 469−483.

48 Yong, J.; Jiang, Y.; Usanmaz, D.; Curtarolo, S.; Zhang, X.; Li, L.; Pan, X.; Shin, J.; Takeuchi, I.; Greene, R. L. Robust Topological Surface State of Kondo insulator SmB₆ Thin Films, Appl. Phys. Lett. 2014, 105, 222403.

49 Toher, C.; Plata, J. J.; Levy, O.; de Jong, M.; Asta, M. D.; Buongiorno Nardelli, M.; Curtarolo, S. High-throughput computational screening of thermal conductivity, Debye temperature, and Grüneisen parameter using a quasihar- monic Debye model, Phys. Rev. B 2014, 90, 174107.

50 Nath, P.; Plata, J. J.; Usanmaz, D.; Al Rahal Al Orabi, R.; Fornari, M.; Buongiorno Nardelli, M.; Toher, C.; Curtarolo, S. High-Throughput Prediction of Finite- Temperature Properties using the Quasi-Harmonic Ap- proximation, Comput. Mater. Sci. 2016, 125, 82−91.

51 Majzoub, E. H.; McCarty, K. F.; Ozoliņš, V. Lattice dy- namics of NaAlH₄ from high-temperature single-crystal Raman scattering and ab initio calculations: Evidence of highly stable AlH₄⁻ anions, Phys. Rev. B 2005, 71, 024118.

52 The formation enthalpy is not to be confused with the cohesive energy, which quantifies the energy difference be- tween the phase and its fully gaseous (single atoms) coun- terpart, i.e., the energy in all bonds.

53 Wang, L.; Maxisch, T.; Ceder, G. Oxidation energies of transition metal oxides within the GGA+U framework, Phys. Rev. B 2006, 73, 195107.

54 Stevanović, V.; Lany, S.; Zhang, X.; Zunger, A. Correct- ing density functional theory for accurate predictions of compound enthalpies of formation: Fitted elemental-phase reference energies, Phys. Rev. B 2012, 85, 115104.

55 Ganguly, J. Thermodynamics in Earth and Planetary Sci- ences, Springer-Verlag Berlin Heidelberg: Berlin, 2008.

56 Darken, L. S.; Gurry, R. W. Physical Chemistry of Metals, McGraw-Hill Book Company, Inc.: New York, 1953.

57 McQuarrie, D. A. Statistical Mechanics, Harper and Row: New York, 1976.

58 Massey, W. S. Cross Products of Vectors in Higher Di- mensional Euclidean Spaces, Am. Math. Mon. 1983, 90, 697−701.

59 Ambiguously-defined facets occur when a set of $d+1$ points (or more) define a $(d-1)$-flat.⁴⁷

60 Sommerville, D. M. Y. An Introduction to the Geometry of N Dimensions, Dover Publications, Inc.: New York, 1929.

61 Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 1996, 54, 11169−11186.

62 Wisesa, P.; McGill, K. A.; Mueller, T. Efficient generation of generalized Monkhorst-Pack grids through the use of informatics, Phys. Rev. B 2016, 93, 155109.

63 Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gra- dient Approximation Made Simple, Phys. Rev. Lett. 1996, 77, 3865−3868.

64 Blöchl, P. E. Projector augmented-wave method, Phys. Rev. B 1994, 50, 17953−17979.

65 Agapito, L. A.; Curtarolo, S.; Buongiorno Nardelli, M. Re- formulation of DFT+$U$ as a Pseudohybrid Hubbard Den- sity Functional for Accelerated Materials Discovery, Phys. Rev. X 2015, 5, 011006.

66 Taylor, R. H.; Curtarolo, S.; Hart, G. L. W. Guiding the

experimental discovery of magnesium alloys, *Phys. Rev. B* **2011**, *84*, 084101.

67 Miller, J. Short Report: Reaction Time Analysis with Outlier Exclusion: Bias Varies with Sample Size, *Q. J. Exp. Psychol. A* **1991**, *43*, 907–912.

68 Leys, C.; Ley, C.; Klein, O.; Bernard, P.; Licata, L. Detecting outliers: Do not use standard deviation around the mean, use absolute deviation around the median, *J. Exp. Soc. Psychol.* **2013**, *49*, 764–766.

69 Hicks, D.; Toher, C.; De Santo, C.; Levy, O.; Mehl, M. J.; Curtarolo, S. AFLOW-XTAL-MATCH: Automated method for quantifying the structural similarity of materials and identifying unique crystal prototypes, *in preparation* **2018**.

70 Burzlaff, H.; Malinovsky, Y. A Procedure for the Classification of Non-Organic Crystal Structures. I. Theoretical Background, *Acta Crystallogr. Sect. A* **1997**, *53*, 217–224.

71 Bergerhoff, G.; Hundt, R.; Sievers, R.; Brown, I. D. The inorganic crystal structure data base, *J. Chem. Inf. Comput. Sci.* **1983**, *23*, 66–69.

72 Belsky, A.; Hellenbrandt, M.; Karen, V. L.; Luksch, P. New developments in the Inorganic Crystal Structure Database (ICSD): accessibility in support of materials research and design, *Acta Crystallogr. Sect. B* **2002**, *58*, 364–369.

73 Sato, J.; Omori, T.; Oikawa, K.; Ohnuma, I.; Kainuma, R.; Ishida, K. Cobalt-Base High-Temperature Alloys, *Science* **2006**, *312*, 90–91.

74 Thorne, L. R. An Innovative Approach to Balancing Chemical-Reaction Equations: A Simplified Matrix-Inversion Technique for Determining The Matrix Null Space, *arxiv:1110.4321* **2011**.

75 Trefethen, L. N.; Bau III, D. Numerical Linear Algebra, Society for Industrial and Applied Mathematics: Philadelphia, PA, **1997**.

76 Kirklin, S.; Saal, J. E.; Hegde, V. I.; Wolverton, C. High-throughput computational search for strengthening precipitates in alloys, *Acta Mater.* **2016**, *102*, 125–135.

77 Eberz, U.; Seelentag, W.; Schuster, H.-U. Zur Kenntnis farbiger ternärer und quaternärer Zintl-Phasen [Coloured Ternary and Quaternary Zintl-Phases], *Z. Naturforsch. B* **1980**, *35*, 1341–1343.

78 Hicks, D.; Mehl, M. J.; Gossett, E.; Toher, C.; Levy, O.; Hanson, R. M.; Hart, G. L. W.; Curtarolo, S. The AFLOW Library of Crystallographic Prototypes: Part 2, *submitted arXiv:1806.07864* **2018**.

79 Bradley, A. J.; Rodgers, J. W. The Crystal Structure of Heusler Alloys, *Proc. R. Soc. A Math. Phys. Eng. Sci.* **1934**, *144*, 340–359.

80 Nowotny, H.; Sibert, W. Ternäre Valenzverbindungen in den Systemen Kupfer(Silber)-Arsen(Antimon,Wismut)-Magnesium, *Z. Metallkd.* **1941**, *33*, 391–394.

81 von Batchelder, F. W.; Raeuchle, R. F. The tetragonal $MBe_{12}$ structure of silver, palladium, platinum and gold, *Acta Cryst.* **1958**, *11*, 122.

82 The AFLOW Library of Crystallographic Prototypes. $AuBe_5$ $(C15_b)$ Structure. http://aflow.org/CrystalDatabase/AB5_cF24_216_a_ce.html (accessed August 01, 2018).

83 Urusov, V. S.; Nadezhina, T. N. Frequency distribution and selection of space groups in inorganic crystal chemistry, *J. Struct. Chem.* **2009**, *50*, 22–37.

84 Xiang, X. D.; Sun, X.; Briceño, G.; Lou, Y.; Wang, K.-A.; Chang, H.; Wallace-Freedman, W. G.; Chen, S.-W.; Schultz, P. G. A Combinatorial Approach to Materials Discovery, *Science* **1995**, *268*, 1738–1740.

85 Takeuchi, I.; Famodu, O. O.; Read, J. C.; Aronova, M. A.; Chang, K. S.; Craciunescu, C.; Lofland, S. E.; Wuttig, M.; Wellstood, F. C.; Knauss, L.; Orozco, A. Identification of novel compositions of ferromagnetic shape-memory alloys using composition spreads, *Nat. Mater.* **2003**, *2*, 180–184.

86 Koinuma, H.; Takeuchi, I. Combinatorial solid-state chemistry of inorganic materials, *Nat. Mater.* **2004**, *3*, 429–438.

87 Curtarolo, S.; Hart, G. L. W.; Buongiorno Nardelli, M.; Mingo, N.; Sanvito, S.; Levy, O. The high-throughput highway to computational materials design, *Nat. Mater.* **2013**, *12*, 191–201.

88 Feuersänger, C. Manual for Package PGFPLOTS. http://ctan.math.utah.edu/ctan/tex-archive/graphics/pgf/contrib/pgfplots/doc/pgfplots.pdf (accessed August 13, 2018).