# Connecting Solute Diffusion to Morphology in Triblock Copolymer Membranes

Michael P. Howard, ⊥ Joshua Lequieu, ⊥ Kris T. Delaney, Venkat Ganesan, Glenn H. Fredrickson, and Thomas M. Truskett*

Cite This: https://dx.doi.org/10.1021/acs.macromol.0c00104

---

ABSTRACT: Block copolymers self-assemble into a variety of morphologies that can serve as templates for preparing conductive or porous materials such as batteries and membranes. These morphologies can be either thermodynamic phases at equilibrium or defective nonequilibrium states that are kinetically trapped. It is an important engineering challenge to predict key material properties from an underlying morphology, particularly when the material may have inherent defects from processing. Here, we focus on the self-diffusion of a tracer through porous membranes assembled from model triblock copolymers. We generate a large library of both equilibrium and nonequilibrium membrane structures using self-consistent field theory, and we simulate solute diffusion in these structures as a simple random walk on a lattice. We show that the solute self-diffusion coefficient strongly correlates with two of the Minkowski functionals characterizing the morphology of the pores: their volume and their integrated mean curvature. We find that, relative to the corresponding equilibrium morphologies, the structure and transport properties associated with nonequilibrium morphologies of gyroid-forming polymers are more tolerant of defects than those of lamella-forming polymers. However, the nonequilibrium morphologies of lamella-forming polymers exhibit a rich diversity of pore structures and corresponding diffusivities, which may prove helpful for designing membranes with targeted properties.

![](./images/812661076188463105_1.jpg)

## INTRODUCTION

Over the past decade, block copolymers have emerged as a promising platform for fabricating mesoporous ultrafiltration membranes.¹,² Block copolymers self-assemble into periodic morphologies, and selective removal of one of the blocks from these arrays can produce open pores that can be used for water purification. Membranes made from block copolymers are frequently referred to as isoporous because they typically have a very narrow distribution of pore sizes, resulting in desirable membrane characteristics like a sharp molecular-weight cutoff and high selectivity.² Moreover, it is straightforward to tune the average pore diameter by varying the block copolymer's molecular weight, blending with solvents, plasticizers, or homopolymers, and/or changing the processing conditions.¹,² Furthermore, the pores can be functionalized after assembly to improve membrane selectivity and/or resist fouling.³ Hence, block copolymers provide a versatile platform for designing membranes provided that the membrane's properties can be connected to the experimentally controllable polymer chemistry and processing conditions.

One approach to create an isoporous membrane is to first self-assemble the block copolymers into a morphology where one component is mechanically self-supporting and then selectively remove another component to reveal the pores percolating through the structure. Block copolymers used in such a framework typically consist of a majority glassy structural block (e.g., polystyrene) and a minority etchable block such as polylactide,⁴⁻⁸ poly(methyl methacrylate),⁹ or poly(dimethylsiloxane).¹⁰⁻¹² This procedure often yields pores that are hydrophobic, resulting in poor water uptake for water-transport membranes. Water uptake can be improved by blending with poly(ethylene oxide) copolymers,⁵ functionalizing the pore walls,¹² or using triblock architectures.⁶,⁷ Furthermore, numerous strategies have been employed to enhance the percolation of pores through the membrane.⁹,¹³⁻¹⁶ Recent work has focused on triblock copolymers with the third block chosen to improve mechanical properties¹⁷,¹⁸ or tune pore functionality.¹⁹,²⁰

A notably wide range of pore morphologies, including sphere percolation networks and spinodal networks in addition to more common structures like ordered cylinders,²¹ can be assembled by varying the processing strategy. Because the membranes of interest are usually cast as thin films that must be mechanically strengthened,¹⁵ the self-assembly process has been combined with non-solvent induced phase separation²²⁻²⁵ (SNIPS) to deposit the film on a porous substrate in a single step.² Phillip et al. found that pore structure was strongly dependent on the rate of solvent removal and that, even with optimized rates, only a small fraction of pores

Received: January 14, 2020
Revised: March 3, 2020

percolated through the membrane. $^{15}$ Polymer molecular weight, solvent composition, and casting conditions also lead to significant variation in pore ordering and the number of defects formed by SNIPS. $^{26}$ However, it is unclear which pore structures are actually desirable for a given separation since the fundamental relationships between membrane morphology and transport processes like diffusion are still poorly understood.

Experimental approaches that can characterize the three-dimensional pore network within a membrane are nascent, $^{27}$ and hence, many studies examining the relationship between morphology and transport have been theoretical. In particular, recent work has focused on the analogous ion-transport problem in diblock copolymers used as electrolytes. $^{28-30}$ Shen et al. simulated ion self-diffusion through different diblock morphologies (lamella, cylinder, and gyroid), surprisingly finding that the lamella was favored over the gyroid for transport in a minority conducting phase despite only being percolated in two dimensions; $^{28}$ this result was also independently identified by Alshammasi and Escobedo. $^{29}$ In contrast to these studies that focused on transport in idealized structures, Schneider and Müller $^{30}$ simulated large-scale nonequilibrium diblock morphologies and found slower diffusion than in equivalent equilibrium structures, despite increased percolation. They attributed this effect to the fractal structure and prevalence of dead ends through a careful analysis of the morphology. $^{30}$

These studies highlight two key challenges in designing block copolymer membranes: (1) transport depends on many characteristics of a morphology, and (2) there can be significant variability between morphologies realized for a given chemistry when synthesized or processed under nonequilibrium conditions. This problem is exacerbated for ABC triblock copolymers, which are attracting increased attention for their use in membranes $^{17-20}$ because they can assemble more exotic phases than those of diblock copolymers. Their extra block also provides a handle for additional modes of nonequilibrium manipulation, e.g., with selective solvents. Designing polymers that reliably produce a morphology with a given transport property may then require many computationally intensive calculations to map and optimize this chemistry-structure-property relationship.

To address the structure-property aspect of this challenge, we were motivated to find a low-dimensional, easily computed description of a membrane's morphology that could be correlated with transport properties such as a solute self-diffusion coefficient (i.e., membrane tortuosity) using a limited data set. We focused on equilibrium and nonequilibrium ABC triblock copolymer morphologies for their relevance to creating functional isoporous membranes $^{6,7,17-20}$ and because transport in triblock copolymers is less studied than in diblock copolymers. However, we note that our methodology readily extends to other porous materials. By correlating diffusion with geometric descriptors of the morphologies, we found that the structures and transport properties associated with nonequilibrium assemblies of gyroid-forming polymers were more robust to the presence of defects than those of lamella-forming polymers but that nonequilibrium morphologies of lamella-forming polymers yielded a richer design space. These geometric descriptors further provide an approach to rapidly screen different morphologies for their transport characteristics.

### MODEL AND METHODS

We studied a nonfrustrated ABC triblock copolymer having $\chi_{\mathrm{AC}} N=$ 35 and $\chi_{\mathrm{AB}} N=\chi_{\mathrm{BC}} N=13$ where $\chi_{i j}$ is the Flory-Huggins interaction parameter between blocks $i$ and $j$ and $N$ is the degree of polymerization. Morse and co-workers previously computed the equilibrium phase diagram for this model using self-consistent field theory (SCFT), $^{31,32}$ finding that much of it is populated by "core-shell" structures that are generalizations of known phases formed by diblock copolymers, such as lamellae, cylinders, and spheres, with additional cladding provided by the third block. For a triblock copolymer with $f_{\mathrm{A}} \geq 0.5$, the "core" C block is surrounded by a "shell" of the B block in a matrix of the A block. ( $f_{i}$ is the volume fraction of block $i$, and $f_{\mathrm{A}}+f_{\mathrm{B}}+f_{\mathrm{C}}=1$.) These core-shell structures are of particular interest for membranes because a hydrophilic or functional B block can be made to coat the pores by removing the C block, $^{6}$ while the A block provides mechanical support. However, these triblock copolymers can also form other phases at different block fractions, making them a reasonable test platform for generating morphologies.

Using SCFT, we generated both equilibrium morphologies consistent with the previously computed phase diagrams $^{31,32}$ and nonequilibrium morphologies quenched from a disordered melt. Fields for the equilibrium structures were initialized to be consistent with the morphology of interest, while fields for the nonequilibrium structures were initialized randomly. The fields were relaxed following standard procedures to the nearest saddle point, $^{33}$ which corresponds to a local free-energy minimum. The ABC triblock was represented using the incompressible multispecies exchange model $^{34}$ with continuous Gaussian chains. Field updates were performed using the semi-implicit Seidel (SIS) scheme, $^{35}$ and the modified diffusion equation was solved using a second-order operator splitting algorithm $^{36}$ with a contour step of $\Delta s=0.01 N$. We considered cubic cells with lengths $14 R_{\mathrm{g}}, 16 R_{\mathrm{g}}$, and $24 R_{\mathrm{g}}$ for the nonequilibrium morphologies where $R_{\mathrm{g}}=b(N / 6)^{1 / 2}$ is the unperturbed radius of gyration of the polymer and $b$ is the statistical segment length. The grid resolution for the fields was $0.219 R_{\mathrm{g}}$ for the smallest cell and $0.25 R_{\mathrm{g}}$ for the larger two. Though our simulation size is much smaller than that employed by Schneider and Müller, $^{30}$ we found that all diffusion coefficients and structural metrics were converged and relatively unchanged over this range of cell sizes (Figure S1). These modest cell sizes additionally permitted us to examine a larger ensemble of morphologies, consisting of 20-100 independent structures for each polymer architecture and over 5000 equilibrium and nonequilibrium morphologies in total.

We subsequently modeled the self-diffusion of a tracer solute in these morphologies. We defined the pores as the regions where $\phi_{\mathrm{B}}(\mathbf{r})$ $+\phi_{\mathrm{C}}(\mathbf{r}) \geq 0.5$ with $\phi_{i}(\mathbf{r})$ being the local volume fraction of $i$ at $\mathbf{r}$, which approximates the experimental scheme of a structural A block, pore-coating B block, and etchable C block. We focused on diffusive transport for two reasons. First, flow rates through nanometer-sized pores are typically small, and diffusive transport is expected to dominate over advective transport. Second, the self-diffusion coefficient of a tracer is intimately connected to the membrane's tortuosity, which is an important material property for continuumlevel modeling.

We digitized the SCFT-generated morphologies onto a simple cubic lattice, defining sites to be either solid or pores based on their majority composition, as described above. We found that a lattice spacing $a=0.25 R_{\mathrm{g}}$ was sufficiently small to mitigate lattice artifacts (Figure S2), effectively setting the nominal largest size for the solute. We then found all connected clusters of pore sites subject to the periodic boundary conditions, and we determined whether a cluster was percolated along each Cartesian axis by seeking a continuous path to its next periodic image. $^{37}$ A random walk was then performed on the lattice with 5000 walkers randomly placed into the connected, percolated pore sites. (A morphology was discarded from the analysis if no such sites were found.) Each walker attempted one random displacement to one of the six adjacent lattice sites per step of the algorithm, and the displacement was unconditionally accepted if the

![](./images/812661076188463105_2.jpg)

Figure 1. Self-diffusivity $D$ for a tracer in (a) equilibrium and (b) nonequilibrium morphologies displayed on the triblock copolymer's phase diagram. $^{31,32}$ For the nonequilibrium morphologies, $D$ was averaged over all obtained pore structures for a state point that were percolated in at least one dimension. Open symbols indicate points where simulations were performed but no such morphologies were obtained. The phase diagram is symmetric with respect to the A and C blocks, and we have focused mainly on the lamella (L), gyroid (G), cylinder (C), sphere (S), and disordered (D) phases in the short B-block regime. The snapshots in (a) show cylinder and lamella morphologies, while (b) shows nonequilibrium morphologies for the same state points.

result was not occupation of a solid site. The time to attempt one displacement was taken as $\tau = a^2/6D_0$ where $D_0$ is the diffusion coefficient on the unobstructed lattice.

In constructing our transport model in this way, we chose to neglect any differences in transport rates between the B-rich and C-rich regions of the pores. In a water-transport membrane, the B block can form a brush-like layer, swollen by the solvent, that coats the pores and effectively slows diffusion. $^{38}$ This effect may depend on distance from the pore surface through the polymer-concentration profile; however, we neglect this effect here for two reasons. First, if the solvent-swollen B block completely fills the pores, the diffusion coefficient is not expected to depend strongly on distance from the pore surfaces. Second, some of us have recently used molecular simulations to show that, even when the swollen B block is smaller than the pore, this effect on diffusion is secondary to morphology for structures like lamellae, cylinders, and gyroids. $^{38}$ Making this approximation allows us to focus here on the connection between morphology and diffusion in more complex geometries.

The average three-dimensional mean-squared displacement (MSD) of each walker was computed up to $10^5$ steps using a $4 \times 10^5$ step trajectory, and we determined the diffusion coefficient $D$ from the long-time limit of the time derivative of the MSD (time $t \geq 512 \tau$, Figure S3). This procedure effectively averages over the diagonal components of the diffusion tensor, which is equivalent to making an isotropic approximation for the material. Averaging has been proposed to account for random orientation of different grains over larger scales than those of our simulations, $^{39,40}$ as forming fully aligned structures is challenging in experiments. $^{15}$ For strongly aligned anisotropic materials, it would be necessary to instead consider the appropriate component of the diffusion tensor.

## RESULTS AND DISCUSSION

In order to connect with recent work, $^{28-30}$ we first simulated diffusion in core-shell equilibrium structures, namely, the lamella, cylinder, gyroid, and sphere phases (Figure 1a). Not all of these structures are useful for making membranes by etching as the material that remains must be self-supporting. For example, the A block forms the cores of the cylinders and spheres when $f_A < 0.5$ and all lamella have disconnected sheets of the A block; these structures would collapse after removing the C block. Nonetheless, we have chosen to report measurements for these morphologies as well because (1) they may be relevant to block copolymers used for batteries or nonporous membranes and (2) they give additional data that is of fundamental interest for connecting morphology to transport.

Trends fully consistent with Shen et al.'s study $^{28}$ of diblock copolymers were obtained for the equilibrium phases. When $f_A$ $> 0.5$, the diffusivities $D/D_0$ for the lamella and cylinder phases were $2/3$ and $1/3$, respectively. These values for $D$ are trivially reduced compared to $D_0$ in the isotropic average because of the connectivity of the domains. The tracer freely diffuses with coefficient $D_0$ in two (one) dimensions for the lamella (cylinder) but is confined in the other dimensions such that those components of the long-time diffusion tensor are effectively zero. In this region of the phase diagram, the changes in $D$ between phases were sharp, mostly due to differences in connectivity between the lamella (two dimensions), cylinder (one dimension), and sphere (not connected) phases. Although the gyroid is connected in three dimensions, $D/D_0$ was between $1/3$ and $2/3$ because of its more tortuous structure; the exact value depended weakly on $f_A$. On the other hand, the changes in $D$ between phases other than the lamella were smoother when $f_A < 0.5$ because the tracer diffused through the fully connected B + C phase, i.e., around the cylinders or spheres rather than inside them. Diffusion was faster for smaller $f_A$, which is qualitatively consistent with the tracer being less obstructed.

Having established the expected consistency with prior studies on diblock copolymers, we turned to the unexamined regime of nonequilibrium triblock copolymer morphologies. We performed multiple SCFT quenches on the free-energy landscape for each state point in the phase diagram. We found that there were small variations in the diffusivities across different morphologies obtained at a given state point, typically having a standard deviation between $10^{-3}D_0$ and $10^{-2}D_0$ and with more variation when $D$ was smaller; the average values are shown in Figure 1b. In contrast to the equilibrium structures (Figure 1a), these nonequilibrium structures exhibit much smoother variations in $D$ for different values of $f_A$, $f_B$, and $f_C$. For example, Figure 2a compares diffusivity as a function of $f_A$ at constant $f_B = 0.05$. The diffusivity shows sharp changes with respect to $f_A$ for the equilibrium morphologies at phase boundaries, as expected, but it varies essentially continuously with $f_A$ for the nonequilibrium morphologies.

This trend is especially apparent within the nonequilibrium morphologies of the lamella-forming polymers where now $D/$ $D_0$ varied significantly. In agreement with Schneider and Müller's study, $^{30}$ most of the nonequilibrium morphologies were percolated in three dimensions even when the

![](./images/812661076188463105_3.jpg)

Figure 2. Diffusivity along lines of constant (a) $f_{\mathrm{B}}=0.05$ and (b) $f_{\mathrm{A}}=$ 0.3,0.35,0.4,0.45 from Figure 1. In (a), the black open symbols denote the respective equilibrium phases, while the red open squares are the averages of the nonequilibrium morphologies at those state points. The symbols for the equilibrium morphologies indicate the phase: sphere (S, open circle), cylinder (C, open hexagon), lamella (L, cross) and gyroid (G, star). In (b), each solid symbol indicates the average value for nonequilibrium morphologies along a different line of constant $f_{\mathrm{A}}$ within the lamellar region of the phase diagram; the black line is the value for the lamella, $D / D_{0}=2 / 3$.

equilibrium phases at the same state point were not. The diffusivities in nonequilibrium morphologies having smaller $f_{\mathrm{A}}$ values were higher than those of the equilibrium phases, but they were lower in morphologies having larger $f_{\mathrm{A}}$ values ($\gtrsim 0.4$). The regions of increased diffusivity are likely an effect of the three-dimensional connectivity, while the decreased regions are likely due to an increasing prevalence of bottlenecks or defects. $^{30}$

Diffusion in the nonequilibrium morphologies showed clear dependence on the block fractions, particularly with respect to $f_{\mathrm{A}}$ (Figure 2a). However, the data was not trivially collapsed onto an effective diblock copolymer [A(B + C)] because $D$ also varied across lines of constant $f_{\mathrm{A}}$. Figure $2 \mathrm{~b}$ shows the diffusivity in nonequilibrium morphologies sampled from the lamellar region of the phase diagram for several values of $f_{\mathrm{A}}$. There is a clear dependence on both $f_{\mathrm{A}}$ and $f_{\mathrm{B}}$ in strong contrast to the equilibrium morphologies ($D / D_{0}=2 / 3$). The diffusivity is intimately connected to properties of the morphology like tortuosity. However, tortuosity can be computationally demanding to measure directly for complex morphologies, $^{41,42}$ while solute diffusivity can be equally difficult to determine. We accordingly sought a low-dimensional, easily computed representation of the morphology that we could use to predict diffusivity. For example, diffusion in large water channels of biological membranes was recently shown to correlate with the average Gaussian curvature of the channel's triply periodic minimal surfaces; however, the approach tended to fail for smaller channels. $^{43}$

Inspired by this geometric approach, $^{43}$ we decided to characterize the membrane pores themselves, rather than their minimal surface, using the four intensive Minkowski functionals $^{44,45}$ that are fundamental in image analysis, volume $v$, surface area $s$, integrated mean curvature $h$, and integrated Gaussian curvature $g$, normalized by the total membrane volume $V_{0}{ }^{46,47}$ The functionals are defined by integrals over the pores; the volume (fraction) and intensive surface area are easily understood. The intensive integrated mean curvature is
$$
h=\frac{1}{2 V_{0}} \int\left[\kappa_{1}(\mathbf{r})+\kappa_{2}(\mathbf{r})\right] \mathrm{d} \mathbf{r} \tag{1}
$$
and the intensive integrated Gaussian curvature is
$$
g=\frac{1}{V_{0}} \int \kappa_{1}(\mathbf{r}) \kappa_{2}(\mathbf{r}) \mathrm{d} \mathbf{r} \tag{2}
$$
where $\kappa_{1}$ and $\kappa_{2}$ are the principal curvatures at a point $\mathbf{r}$ on the pore surface. In practice, we computed the Minkowski functionals on the digitized lattice using the conventions and voxel-counting algorithm described by Michielsen and De Raedt. $^{44}$ We note that this algorithm requires voxels that are cubic, and it was necessary to adjust the grid resolution of the unit-cell SCFT simulations for the equilibrium morphologies to ensure that this condition was met.

![](./images/812661076188463105_4.jpg)

Figure 3. Correlation of the intensive Minkowski functionals, (a) volume $v$, (b) surface area $s$, (c) integrated mean curvature $h$, and (d) integrated Gaussian curvature $g$, to the simulated self-diffusivity $D$ of a tracer in the nonequilibrium triblock copolymer pore morphologies (solid circle) that were percolated in at least one dimension. The equilibrium structures are also shown using the same symbols as in Figure 2. The symbols are colored by $f_{\mathrm{A}}$, which denotes the volume fraction of the solid (i.e., inaccessible) A block within the morphology. (e) Relative importance of the different Minkowski functionals in a random forest regression for diffusivity, ranked according to the mean decrease in accuracy, using all four functionals (red) and then only the top two ( $v$ and $h$, blue). (f) Mean absolute error in the random forest regression using the same descriptors with differing numbers of nonequilibrium morphologies sampled per state point in the phase diagram (solid lines) and after dropping out roughly half the state points (dashed lines).

Figure 3a−d shows the diffusivity plotted against each of the four intensive Minkowski functionals. The data from the nonequilibrium morphologies collapsed well as a function of $f_A$ for all three simulation domain volumes when using these normalized descriptors but not their extensive values, which we believe is related to the inherent length scales set by the polymer as it microphase-separates. Most of the equilibrium diffusion data also collapsed onto the nonequilibrium diffusion data, but that of the cylinder and lamella morphologies sometimes did not (see below). For both equilibrium and nonequilibrium morphologies, $v$ was smaller when $f_A$ was larger, which is expected from mass conservation of well-separated phases. The maximum surface area $s$ was obtained when $f_A \approx 0.5$. Last, we found a wide range of mean curvatures, $h$, which tended to be positive when the pores were the minority ($f_A > 0.5$) and negative when the pores were the majority ($f_A < 0.5$). These signs are consistent with the curvature of the underlying equilibrium morphologies.

The diffusivity in the nonequilibrium morphologies was seen to be strongly correlated with both $v$ and $h$, but it was not strongly dependent on (and was not one-to-one with) either $s$ or $g$. We confirmed this by regressing $D$ with the descriptors ($v$, $s$, $h$, and $g$) using a random forest model, $^{48,49}$ which gives the mean prediction from a set of decision trees. We probed the importance of each Minkowski functional in the model (Figure 3e) by determining the mean decrease in accuracy after randomization of a descriptor in our test data set (see the Supporting Information). This analysis found that $v$ and $h$ were the dominant, equally important features required to fit the data. We further confirmed this by completely removing the $s$ and $g$ descriptors, recovering similar predictive accuracy and importance of $v$ and $h$.

It is sensible that $v$ and $h$ should be important for determining the tracer diffusivity. The volume fraction $v$ controls the accessible space in the morphology; the tracer diffuses freely in a nearly unobstructed environment when $v$ is close to 1, while its diffusion is highly hindered when $v$ is close to 0. However, there should be additional contributions from surfaces, especially when $v$ is smaller and the tracer is now confined as the tracer must move around the interfaces and the average length of this path should matter. The surface area is not a good predictor of this because it is often degenerate, e.g., both minority-A and majority-A cylinder morphologies have the same surface area. Additionally, the integrated Gaussian curvature is not always discriminating because it is intimately related to a topological property of the pore surface (the Euler characteristic $\chi = gV_0/2\pi$) rather than a geometric property $^{44,45}$ and would need to be modified or scaled. $^{29}$ For example, all ideal gyroid unit cells have the same Gaussian curvature even though the pore volume and $D$ can vary significantly. The integrated mean curvature suffers from neither of these issues, making it a good predictor of diffusivity.

Our goal is to ultimately use the regression model to quickly screen candidate morphologies for their transport properties, and for computational efficiency, we would like to use the least data possible to obtain this model. There are two ways to reduce the number of samples in the regression, simulate fewer morphologies per state point and/or simulate at fewer state points, and we tested the impact of both on model accuracy. We first selected a certain number of nonequilibrium morphologies at random from each state point in the phase diagram to use in fitting the model. We then computed the mean absolute error (MAE) of the model for the remaining nonequilibrium morphologies (Figure 3f). The MAE initially decreased when the number of samples per point was increased until there were at least 5 samples/point. The MAE was slightly lower when using all four descriptors rather than only $v$ and $h$. We repeated this procedure while dropping out roughly half of the state points from the training data. We computed the MAE from the state points not used in the fitting, obtaining comparable values. This demonstrates a viable strategy to quickly map the relationship between complex morphologies and diffusion by limited sampling from the phase diagram.

Although the equilibrium gyroid and majority B + C morphologies closely resembled the nonequilibrium morphologies in Figure 3, there were substantial differences with the minority cylinder and lamella morphologies. Diffusivity in these morphologies tended to deviate from the others because they were only connected in one or two dimensions, whereas the rest were connected in three dimensions. To better understand how defects manifest in the morphological descriptors, we computed distributions of $v$ and $h$ for the morphologies of lamella-forming and gyroid-forming polymers. In agreement with Schneider and Müller's findings, $^{30}$ the volume of the nonequilibrium pores tended to deviate by a small amount from the pore volume of the corresponding equilibrium structure (Figure 4a). However, the more significant differences were in the integrated mean curvature (Figure 4b). Due to defects, the mean curvature of lamella-forming polymers differed substantially between the equilibrium ($h = 0$) and nonequilibrium morphologies, manifesting in different values of $D$. In contrast, the curvature of the nonequilibrium morphologies of the gyroid-forming polymers was distributed closely about the equilibrium values.

![](./images/812661076188463105_5.jpg)

Figure 4. Probability distributions for the Minkowski functionals (a) $v$ and (b) $h$ for all the percolated nonequilibrium morphologies of the lamella-forming (L, solid line) and gyroid-forming (G, dotted line) polymers in Figure 1b. The symbols and vertical lines mark $v$ and $h$ for the lamella and gyroid equilibrium morphologies (Figure 1a); colors denote $f_A$ as in Figure 3.

Our measurements suggest two potential design strategies to capitalize on features of the nonequilibrium morphologies. First, although the equilibrium gyroid comprises a much smaller region of the phase diagram than the lamella (and so it may be more challenging to fabricate), transport through nonequilibrium morphologies of gyroid-forming polymers is expected to be less sensitive to defects in the assembled structure. The smoothness of the diffusivity for the non-

equilibrium morphologies with respect to polymer architecture (Figure 2a) also makes these target structures tolerant to deviations from the synthesis, which are more penalized at equilibrium. This tolerance may be related to the fact that both the gyroid and the nonequilibrium morphologies are connected in three dimensions. Second, equilibrium lamellae are not particularly useful for making porous membranes because they are not mechanically supported after removal of the C block. Nonequilibrium morphologies of lamella-forming polymers, however, were typically connected in three dimensions and gave access to a wider range of diffusivities than those of the gyroid-forming polymers. These morphologies also covered a large range of the B block length, which may be important for designing interactions inside the pores. We expect these strategies to be useful for achieving target transport properties while optimizing other membrane properties, e.g., mechanical stability or fouling resistance.

## CONCLUSIONS

In summary, we have shown that diffusion in self-assembled triblock copolymers is strongly connected with their underlying morphology. The self-diffusion coefficient of a tracer solute can be predicted in a variety of nonequilibrium morphologies using a simple geometric description based on the Minkowski functionals, namely, the volume and integrated mean curvature of the pores. (The surface area and integrated Gaussian curvature were shown to be far less significant.) Data to fit this model are easy to collect by limited sampling of nonequilibrium morphologies while achieving a mean absolute error of roughly $10^{-2}D_0$. Using the Minkowski functionals, we characterized key differences between equilibrium and nonequilibrium morphologies of lamella-forming and gyroid-forming polymers. Nonequilibrium morphologies appear to provide a robust strategy for tailoring transport, which we hope to use in the future to design membrane materials.

As a caveat, we recognize that our diffusion model simplified the internal pore structure by assuming that the solute was uniformly distributed in the pores and had a constant local diffusion coefficient. Our recent work has used more sophisticated models to show that these assumptions can be violated for solvophilic B blocks that do not swell to fill the whole pore. $^{38}$ Although these effects are largely secondary to the morphology in determining the long-time self-diffusion coefficient, they may quantitatively affect our predictions in certain regimes of the phase diagram or become more significant if the pore surfaces were functionalized to interact strongly with the solute. We intend to incorporate these effects into an improved multiscale transport model soon.

## ASSOCIATED CONTENT

### Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.macromol.0c00104.

Effects of the simulation cell size and the random-walk lattice spacing on morphology characterization and diffusivity and details of random-forest model fitting (PDF)

## AUTHOR INFORMATION

### Corresponding Author

Thomas M. Truskett − McKetta Department of Chemical Engineering and Department of Physics, University of Texas at Austin, Austin, Texas 78712, United States; <https://orcid.org/0000-0002-6607-6468>; Email: truskett@che.utexas.edu

### Authors

Michael P. Howard − McKetta Department of Chemical Engineering, University of Texas at Austin, Austin, Texas 78712, United States; <https://orcid.org/0000-0002-9561-4165>

Joshua Lequieu − Materials Research Laboratory, University of California, Santa Barbara, California 93106, United States; <https://orcid.org/0000-0001-9480-0989>

Kris T. Delaney − Materials Research Laboratory, University of California, Santa Barbara, California 93106, United States; <https://orcid.org/0000-0003-0356-1391>

Venkat Ganesan − McKetta Department of Chemical Engineering, University of Texas at Austin, Austin, Texas 78712, United States; <https://orcid.org/0000-0003-3899-5843>

Glenn H. Fredrickson − Materials Research Laboratory, Department of Chemical Engineering, and Materials Department, University of California, Santa Barbara, California 93106, United States; <https://orcid.org/0000-0002-6716-9017>

Complete contact information is available at:
https://pubs.acs.org/doi/10.1021/acs.macromol.0c00104

### Author Contributions

†M.P.H. and J.L. contributed equally to this work.

### Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

We thank Wesley Reinhart for helpful discussions on the random-forest regression. This work was supported as part of the Center for Materials for Water and Energy Systems (M-WET), an Energy Frontier Research Center funded by the U.S. Department of Energy, Office of Science, Basic Energy Sciences under Award #DE-SC0019272. V.G. and T.M.T. acknowledge financial support from the Welch Foundation (grant nos. F-1599 and F-1696). Use was made of computational facilities purchased with funds from the National Science Foundation (no. CNS-1725797) and administered by the Center for Scientific Computing (CSC). The CSC is supported by the California NanoSystems Institute and the Materials Research Science and Engineering Center (MRSEC; no. NSF DMR-1720256) at UC Santa Barbara.

## REFERENCES

(1) Hillmyer, M. A. In *Block Copolymers II*; Abetz, V., Ed.; Springer Berlin Heidelberg: Berlin, Heidelberg, 2005; pp 137−181.

(2) Abetz, V. Isoporous Block Copolymer Membranes. *Macromol. Rapid Commun.* **2015**, 36, 10−22.

(3) Gamys, C. G.; Schumers, J.-M.; Mugemana, C.; Fustin, C.-A.; Gohy, J.-F. Pore-Functionalized Nanoporous Materials Derived from Block Copolymers. *Macromol. Rapid Commun.* **2013**, 34, 962−982.

(4) Zalusky, A. S.; Olayo-Valles, R.; Wolf, J. H.; Hillmyer, M. A. Ordered Nanoporous Polymers from Polystyrene−Polylactide Block Copolymers. *J. Am. Chem. Soc.* **2002**, 124, 12761−12773.

(5) Mao, H.; Arrechea, P. L.; Bailey, T. S.; Johnson, B. J. S.; Hillmyer, M. A. Control of pore hydrophilicity in ordered nanoporous polystyrene using an AB/AC block copolymer blending strategy. *Faraday Discuss.* **2005**, 128, 149−162.

(6) Rzayev, J.; Hillmyer, M. A. Nanoporous Polystyrene Containing Hydrophilic Pores from an ABC Triblock Copolymer Precursor. *Macromolecules* **2005**, 38, 3−5.

(7) Bailey, T. S.; Rzayev, J.; Hillmyer, M. A. Routes to Alkene and Epoxide Functionalized Nanoporous Materials from Poly(styrene-b-

isoprene-b-lactide) Triblock Copolymers. *Macromolecules* **2006**, *39*, 8772−8781.

(8) Bolton, J.; Bailey, T. S.; Rzayev, J. Large Pore Size Nanoporous Materials from the Self-Assembly of Asymmetric Bottlebrush Block Copolymers. *Nano Lett.* **2011**, *11*, 998−1001.

(9) Yang, S. Y.; Ryu, I.; Kim, H. Y.; Kim, J. K.; Jang, S. K.; Russell, T. P. Nanoporous Membranes with Ultrahigh Selectivity and Flux for the Filtration of Viruses. *Adv. Mater.* **2006**, *18*, 709−712.

(10) Ndoni, S.; Vigild, M. E.; Berg, R. H. Nanoporous Materials with Spherical and Gyroid Cavities Created by Quantitative Etching of Polydimethylsiloxane in Polystyrene−Polydimethylsiloxane Block Copolymers. *J. Am. Chem. Soc.* **2003**, *125*, 13366−13367.

(11) Li, L.; Schulte, L.; Clausen, L. D.; Hansen, K. M.; Jonsson, G. E.; Ndoni, S. Gyroid Nanoporous Membranes with Tunable Permeability. *ACS Nano* **2011**, *5*, 7754−7766.

(12) Li, L.; Szewczykowski, P.; Clausen, L. D.; Hansen, K. M.; Jonsson, G. E.; Ndoni, S. Ultrafiltration by gyroid nanoporous polymer membranes. *J. Membr. Sci.* **2011**, *384*, 126−135.

(13) Jeong, U.; Ryu, D. Y.; Kho, D. H.; Kim, J. K.; Goldbach, J. T.; Kim, D. H.; Russell, T. P. Enhancement in the Orientation of the Microdomain in Block Copolymer Thin Films upon the Addition of Homopolymer. *Adv. Mater.* **2004**, *16*, 533−536.

(14) Li, X.; Fustin, C.-A.; Lefevre, N.; Gohy, J.-F.; De Feyter, S.; De Baerdemaeker, J.; Egger, W.; Vankelecom, I. F. J. Ordered nanoporous membranes based on diblock copolymers with high chemical stability and tunable separation properties. *J. Mater. Chem.* **2010**, *20*, 4333−4339.

(15) Phillip, W. A.; O’Neill, B.; Rodwogin, M.; Hillmyer, M. A.; Cussler, E. L. Self-Assembled Block Copolymer Thin Films as Water Filtration Membranes. *ACS Appl. Mater. Interfaces* **2010**, *2*, 847−853.

(16) Phillip, W. A.; Hillmyer, M. A.; Cussler, E. L. Cylinder Orientation Mechanism in Block Copolymer Thin Films Upon Solvent Evaporation. *Macromolecules* **2010**, *43*, 7763−7770.

(17) Phillip, W. A.; Dorin, R. M.; Werner, J.; Hoek, E. M. V.; Wiesner, U.; Elimelech, M. Tuning Structure and Properties of Graded Triblock Terpolymer-Based Mesoporous and Hybrid Films. *Nano Lett.* **2011**, *11*, 2892−2900.

(18) Pendergast, M. M.; Mika Dorin, R.; Phillip, W. A.; Wiesner, U.; Hoek, E. M. V. Understanding the structure and performance of self-assembled triblock terpolymer membranes. *J. Membr. Sci.* **2013**, *444*, 461−468.

(19) Jung, A.; Filiz, V.; Rangou, S.; Buhr, K.; Merten, P.; Hahn, J.; Clodt, J.; Abetz, C.; Abetz, V. Formation of Integral Asymmetric Membranes of AB Diblock and ABC Triblock Copolymers by Phase Inversion. *Macromol. Rapid Commun.* **2013**, *34*, 610−615.

(20) Mulvenna, R. A.; Weidman, J. L.; Jing, B.; Pople, J. A.; Zhu, Y.; Boudouris, B. W.; Phillip, W. A. Tunable nanoporous membranes with chemically-tailored pore walls from triblock polymer templates. *J. Membr. Sci.* **2014**, *470*, 246−256.

(21) Stegelmeier, C.; Filiz, V.; Abetz, V.; Perlich, J.; Fery, A.; Ruckdeschel, P.; Rosenfeldt, S.; Förster, S. Topological paths and transient morphologies during formation of mesoporous block copolymer membranes. *Macromolecules* **2014**, *47*, 5566−5577.

(22) Peinemann, K.-V.; Abetz, V.; Simon, P. F. W. Asymmetric superstructure formed in a block copolymer via phase separation. *Nat. Mater.* **2007**, *6*, 992−996.

(23) Nunes, S. P.; Sougrat, R.; Hooghan, B.; Anjum, D. H.; Behzad, A. R.; Zhao, L.; Pradeep, N.; Pinnau, I.; Vainio, U.; Peinemann, K.-V. Ultraporous films with uniform nanochannels by block copolymer micelles assembly. *Macromolecules* **2010**, *43*, 8079−8085.

(24) Nunes, S. P.; Behzad, A. R.; Hooghan, B.; Sougrat, R.; Karunakaran, M.; Pradeep, N.; Vainio, U.; Peinemann, K.-V. Switchable pH-Responsive Polymeric Membranes Prepared via Block Copolymer Micelle Assembly. *ACS Nano* **2011**, *5*, 3516−3522.

(25) Wang, Z.; Yao, X.; Wang, Y. Swelling-induced mesoporous block copolymer membranes with intrinsically active surfaces for size-selective separation. *J. Mater. Chem.* **2012**, *22*, 20542−20548.

(26) Rangou, S.; Buhr, K.; Filiz, V.; Clodt, J. I.; Lademann, B.; Hahn, J.; Jung, A.; Abetz, V. Self-organized isoporous membranes with tailored pore sizes. *J. Membr. Sci.* **2014**, *451*, 266−275.

(27) Zalami, D.; Grimm, O.; Schacher, F. H.; Gerken, U.; Köhler, J. Non-invasive study of the three-dimensional structure of nanoporous triblock terpolymer membranes. *Soft Matter* **2018**, *14*, 9750−9754.

(28) Shen, K.-H.; Brown, J. R.; Hall, L. M. Diffusion in Lamellae, Cylinders, and Double Gyroid Block Copolymer Nanostructures. *ACS Macro Lett.* **2018**, *7*, 1092−1098.

(29) Alshammasi, M. S.; Escobedo, F. A. Correlation between Ionic Mobility and Microstructure in Block Copolymers. A Coarse-Grained Modeling Study. *Macromolecules* **2018**, *51*, 9213−9221.

(30) Schneider, L. Y.; Müller, M. Engineering Scale Simulation of Nonequilibrium Network Phases for Battery Electrolytes. *Macromolecules* **2019**, *52*, 2050−2062.

(31) Tyler, C. A.; Qin, J.; Bates, F. S.; Morse, D. C. SCFT Study of Nonfrustrated ABC Triblock Copolymer Melts. *Macromolecules* **2007**, *40*, 4654−4668.

(32) Qin, J.; Bates, F. S.; Morse, D. C. Phase Behavior of Nonfrustrated ABC Triblock Copolymers: Weak and Intermediate Segregation. *Macromolecules* **2010**, *43*, 5128−5136.

(33) Fredrickson, G. *The Equilibrium Theory of Inhomogeneous Polymers*; Oxford University Press: Oxford, 2006.

(34) Düchs, D.; Delaney, K. T.; Fredrickson, G. H. A multi-species exchange model for fully fluctuating polymer field theory simulations. *J. Chem. Phys.* **2014**, *141*, 174103.

(35) Cenicerps, H. D.; Fredrickson, G. H. Numerical Solution of Polymer Self-Consistent Field Theory. *Multiscale Model. Simul.* **2004**, *2*, 452−474.

(36) Rasmussen, K. Ø.; Kalosakas, G. Improved numerical algorithm for exploring block copolymer mesophases. *J. Polym. Sci., Part B: Polym. Phys.* **2002**, *40*, 1777−1783.

(37) Hagberg, A. A.; Schult, D. A.; Swart, P. J. Exploring network structure, dynamics, and function using NetworkX. *Proceedings of the 7th Python in Science Conference (SciPy2008).*; Los Alamos National Lab.: United States, 2008; pp 11−15.

(38) Aryal, D.; Howard, M. P.; Samanta, R.; Antoine, S.; Segalman, R.; Truskett, T. M.; Ganesan, V. Influence of pore morphology on the diffusion of water in triblock copolymer membranes. *J. Chem. Phys.* **2020**, *152*, No. 014904.

(39) Sax, J.; Ottino, J. M. Modeling of transport of small molecules in polymer blends: Application of effective medium theory. *Polym. Eng. Sci.* **1983**, *23*, 165−176.

(40) Kinning, D. J.; Thomas, E. L.; Ottino, J. M. Effect of Morphology on the Transport of Gases in Block Copolymers. *Macromolecules* **1987**, *20*, 1129−1133.

(41) Lindquist, W. B.; Lee, S.-M.; Coker, D. A.; Jones, K. W.; Spanne, P. Medial axis analysis of void structure in three-dimensional tomographic images of porous media. *J. Geophys. Res. Solid Earth* **1996**, *101*, 8297−8310.

(42) Gommes, C. J.; Bons, A.-J.; Blacher, S.; Dunsmuir, J. H.; Tsou, A. H. Practical Methods for Measuring the Tortuosity of Porous Materials from Binary or Gray-Tone Tomographic Reconstructions. *AIChE J.* **2009**, *55*, 2000−2012.

(43) Assenza, S.; Mezzenga, R. Curvature and bottlenecks control molecular transport in inverse bicontinuous cubic phases. *J. Chem. Phys.* **2018**, *148*, No. 054902.

(44) Michielsen, K.; De Raedt, H. Integral-geometry morphological image analysis. *Phys. Rep.* **2001**, *347*, 461−538.

(45) Armstrong, R. T.; McClure, J. E.; Robins, V.; Liu, Z.; Arns, C. H.; Schlüter, S.; Berg, S. Porous Media Characterization Using Minkowski Functionals: Theories, Applications and Future Directions. *Transp. Porous Media* **2019**, *130*, 305−335.

(46) Schlüter, S.; Weller, U.; Vogel, H.-J. Soil-structure development including seasonal dynamics in a long-term fertilization experiment. *J. Plant Nutr. Soil Sci.* **2011**, *174*, 395−403.

(47) Liu, Z.; Herring, A.; Arns, C.; Berg, S.; Armstrong, R. T. Pore-Scale Characterization of Two-Phase Flow Using Integral Geometry. *Transp. Porous Media* **2017**, *118*, 99−117.

(48) Breiman, L. Random Forests. Mach. Learn. 2001, 45, 5−32.

(49) Pedregosa, F.; et al. Scikit-learn: Machine Learning in Python. J.
Mach. Learn. Res. 2011, 12, 2825−2830.

## AUTHOR INFORMATION

### Corresponding Author

Thomas M. Truskett − McKetta Department of Chemical Engineering and Department of Physics, University of Texas at Austin, Austin, Texas 78712, United States; <https://orcid.org/0000-0002-6607-6468>; Email: truskett@che.utexas.edu

### Authors

Michael P. Howard − McKetta Department of Chemical Engineering, University of Texas at Austin, Austin, Texas 78712, United States; <https://orcid.org/0000-0002-9561-4165>

Joshua Lequieu − Materials Research Laboratory, University of California, Santa Barbara, California 93106, United States; <https://orcid.org/0000-0001-9480-0989>

Kris T. Delaney − Materials Research Laboratory, University of California, Santa Barbara, California 93106, United States; <https://orcid.org/0000-0003-0356-1391>

Venkat Ganesan − McKetta Department of Chemical Engineering, University of Texas at Austin, Austin, Texas 78712, United States; <https://orcid.org/0000-0003-3899-5843>

Glenn H. Fredrickson − Materials Research Laboratory, Department of Chemical Engineering, and Materials Department, University of California, Santa Barbara, California 93106, United States; <https://orcid.org/0000-0002-6716-9017>

Complete contact information is available at:
https://pubs.acs.org/doi/10.1021/acs.macromol.0c00104

### Author Contributions

†M.P.H. and J.L. contributed equally to this work.

### Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

We thank Wesley Reinhart for helpful discussions on the random-forest regression. This work was supported as part of the Center for Materials for Water and Energy Systems (M-WET), an Energy Frontier Research Center funded by the U.S. Department of Energy, Office of Science, Basic Energy Sciences under Award #DE-SC0019272. V.G. and T.M.T. acknowledge financial support from the Welch Foundation (grant nos. F-1599 and F-1696). Use was made of computational facilities purchased with funds from the National Science Foundation (no. CNS-1725797) and administered by the Center for Scientific Computing (CSC). The CSC is supported by the California NanoSystems Institute and the Materials Research Science and Engineering Center (MRSEC; no. NSF DMR-1720256) at UC Santa Barbara.

## REFERENCES

(1) Hillmyer, M. A. In *Block Copolymers II*; Abetz, V., Ed.; Springer Berlin Heidelberg: Berlin, Heidelberg, 2005; pp 137−181.

(2) Abetz, V. Isoporous Block Copolymer Membranes. *Macromol. Rapid Commun.* **2015**, 36, 10−22.

(3) Gamys, C. G.; Schumers, J.-M.; Mugemana, C.; Fustin, C.-A.; Gohy, J.-F. Pore-Functionalized Nanoporous Materials Derived from Block Copolymers. *Macromol. Rapid Commun.* **2013**, 34, 962−982.

(4) Zalusky, A. S.; Olayo-Valles, R.; Wolf, J. H.; Hillmyer, M. A. Ordered Nanoporous Polymers from Polystyrene−Polylactide Block Copolymers. *J. Am. Chem. Soc.* **2002**, 124, 12761−12773.

(5) Mao, H.; Arrechea, P. L.; Bailey, T. S.; Johnson, B. J. S.; Hillmyer, M. A. Control of pore hydrophilicity in ordered nanoporous polystyrene using an AB/AC block copolymer blending strategy. *Faraday Discuss.* **2005**, 128, 149−162.

(6) Rzayev, J.; Hillmyer, M. A. Nanoporous Polystyrene Containing Hydrophilic Pores from an ABC Triblock Copolymer Precursor. *Macromolecules* **2005**, 38, 3−5.

(7) Bailey, T. S.; Rzayev, J.; Hillmyer, M. A. Routes to Alkene and Epoxide Functionalized Nanoporous Materials from Poly(styrene-b-

isoprene-b-lactide) Triblock Copolymers. *Macromolecules* **2006**, *39*, 8772−8781.

(8) Bolton, J.; Bailey, T. S.; Rzayev, J. Large Pore Size Nanoporous Materials from the Self-Assembly of Asymmetric Bottlebrush Block Copolymers. *Nano Lett.* **2011**, *11*, 998−1001.

(9) Yang, S. Y.; Ryu, I.; Kim, H. Y.; Kim, J. K.; Jang, S. K.; Russell, T. P. Nanoporous Membranes with Ultrahigh Selectivity and Flux for the Filtration of Viruses. *Adv. Mater.* **2006**, *18*, 709−712.

(10) Ndoni, S.; Vigild, M. E.; Berg, R. H. Nanoporous Materials with Spherical and Gyroid Cavities Created by Quantitative Etching of Polydimethylsiloxane in Polystyrene−Polydimethylsiloxane Block Copolymers. *J. Am. Chem. Soc.* **2003**, *125*, 13366−13367.

(11) Li, L.; Schulte, L.; Clausen, L. D.; Hansen, K. M.; Jonsson, G. E.; Ndoni, S. Gyroid Nanoporous Membranes with Tunable Permeability. *ACS Nano* **2011**, *5*, 7754−7766.

(12) Li, L.; Szewczykowski, P.; Clausen, L. D.; Hansen, K. M.; Jonsson, G. E.; Ndoni, S. Ultrafiltration by gyroid nanoporous polymer membranes. *J. Membr. Sci.* **2011**, *384*, 126−135.

(13) Jeong, U.; Ryu, D. Y.; Kho, D. H.; Kim, J. K.; Goldbach, J. T.; Kim, D. H.; Russell, T. P. Enhancement in the Orientation of the Microdomain in Block Copolymer Thin Films upon the Addition of Homopolymer. *Adv. Mater.* **2004**, *16*, 533−536.

(14) Li, X.; Fustin, C.-A.; Lefevre, N.; Gohy, J.-F.; De Feyter, S.; De Baerdemaeker, J.; Egger, W.; Vankelecom, I. F. J. Ordered nanoporous membranes based on diblock copolymers with high chemical stability and tunable separation properties. *J. Mater. Chem.* **2010**, *20*, 4333−4339.

(15) Phillip, W. A.; O’Neill, B.; Rodwogin, M.; Hillmyer, M. A.; Cussler, E. L. Self-Assembled Block Copolymer Thin Films as Water Filtration Membranes. *ACS Appl. Mater. Interfaces* **2010**, *2*, 847−853.

(16) Phillip, W. A.; Hillmyer, M. A.; Cussler, E. L. Cylinder Orientation Mechanism in Block Copolymer Thin Films Upon Solvent Evaporation. *Macromolecules* **2010**, *43*, 7763−7770.

(17) Phillip, W. A.; Dorin, R. M.; Werner, J.; Hoek, E. M. V.; Wiesner, U.; Elimelech, M. Tuning Structure and Properties of Graded Triblock Terpolymer-Based Mesoporous and Hybrid Films. *Nano Lett.* **2011**, *11*, 2892−2900.

(18) Pendergast, M. M.; Mika Dorin, R.; Phillip, W. A.; Wiesner, U.; Hoek, E. M. V. Understanding the structure and performance of self-assembled triblock terpolymer membranes. *J. Membr. Sci.* **2013**, *444*, 461−468.

(19) Jung, A.; Filiz, V.; Rangou, S.; Buhr, K.; Merten, P.; Hahn, J.; Clodt, J.; Abetz, C.; Abetz, V. Formation of Integral Asymmetric Membranes of AB Diblock and ABC Triblock Copolymers by Phase Inversion. *Macromol. Rapid Commun.* **2013**, *34*, 610−615.

(20) Mulvenna, R. A.; Weidman, J. L.; Jing, B.; Pople, J. A.; Zhu, Y.; Boudouris, B. W.; Phillip, W. A. Tunable nanoporous membranes with chemically-tailored pore walls from triblock polymer templates. *J. Membr. Sci.* **2014**, *470*, 246−256.

(21) Stegelmeier, C.; Filiz, V.; Abetz, V.; Perlich, J.; Fery, A.; Ruckdeschel, P.; Rosenfeldt, S.; Förster, S. Topological paths and transient morphologies during formation of mesoporous block copolymer membranes. *Macromolecules* **2014**, *47*, 5566−5577.

(22) Peinemann, K.-V.; Abetz, V.; Simon, P. F. W. Asymmetric superstructure formed in a block copolymer via phase separation. *Nat. Mater.* **2007**, *6*, 992−996.

(23) Nunes, S. P.; Sougrat, R.; Hooghan, B.; Anjum, D. H.; Behzad, A. R.; Zhao, L.; Pradeep, N.; Pinnau, I.; Vainio, U.; Peinemann, K.-V. Ultraporous films with uniform nanochannels by block copolymer micelles assembly. *Macromolecules* **2010**, *43*, 8079−8085.

(24) Nunes, S. P.; Behzad, A. R.; Hooghan, B.; Sougrat, R.; Karunakaran, M.; Pradeep, N.; Vainio, U.; Peinemann, K.-V. Switchable pH-Responsive Polymeric Membranes Prepared via Block Copolymer Micelle Assembly. *ACS Nano* **2011**, *5*, 3516−3522.

(25) Wang, Z.; Yao, X.; Wang, Y. Swelling-induced mesoporous block copolymer membranes with intrinsically active surfaces for size-selective separation. *J. Mater. Chem.* **2012**, *22*, 20542−20548.

(26) Rangou, S.; Buhr, K.; Filiz, V.; Clodt, J. I.; Lademann, B.; Hahn, J.; Jung, A.; Abetz, V. Self-organized isoporous membranes with tailored pore sizes. *J. Membr. Sci.* **2014**, *451*, 266−275.

(27) Zalami, D.; Grimm, O.; Schacher, F. H.; Gerken, U.; Köhler, J. Non-invasive study of the three-dimensional structure of nanoporous triblock terpolymer membranes. *Soft Matter* **2018**, *14*, 9750−9754.

(28) Shen, K.-H.; Brown, J. R.; Hall, L. M. Diffusion in Lamellae, Cylinders, and Double Gyroid Block Copolymer Nanostructures. *ACS Macro Lett.* **2018**, *7*, 1092−1098.

(29) Alshammasi, M. S.; Escobedo, F. A. Correlation between Ionic Mobility and Microstructure in Block Copolymers. A Coarse-Grained Modeling Study. *Macromolecules* **2018**, *51*, 9213−9221.

(30) Schneider, L. Y.; Müller, M. Engineering Scale Simulation of Nonequilibrium Network Phases for Battery Electrolytes. *Macromolecules* **2019**, *52*, 2050−2062.

(31) Tyler, C. A.; Qin, J.; Bates, F. S.; Morse, D. C. SCFT Study of Nonfrustrated ABC Triblock Copolymer Melts. *Macromolecules* **2007**, *40*, 4654−4668.

(32) Qin, J.; Bates, F. S.; Morse, D. C. Phase Behavior of Nonfrustrated ABC Triblock Copolymers: Weak and Intermediate Segregation. *Macromolecules* **2010**, *43*, 5128−5136.

(33) Fredrickson, G. *The Equilibrium Theory of Inhomogeneous Polymers*; Oxford University Press: Oxford, 2006.

(34) Düchs, D.; Delaney, K. T.; Fredrickson, G. H. A multi-species exchange model for fully fluctuating polymer field theory simulations. *J. Chem. Phys.* **2014**, *141*, 174103.

(35) Cenicerps, H. D.; Fredrickson, G. H. Numerical Solution of Polymer Self-Consistent Field Theory. *Multiscale Model. Simul.* **2004**, *2*, 452−474.

(36) Rasmussen, K. Ø.; Kalosakas, G. Improved numerical algorithm for exploring block copolymer mesophases. *J. Polym. Sci., Part B: Polym. Phys.* **2002**, *40*, 1777−1783.

(37) Hagberg, A. A.; Schult, D. A.; Swart, P. J. Exploring network structure, dynamics, and function using NetworkX. *Proceedings of the 7th Python in Science Conference (SciPy2008).*; Los Alamos National Lab.: United States, 2008; pp 11−15.

(38) Aryal, D.; Howard, M. P.; Samanta, R.; Antoine, S.; Segalman, R.; Truskett, T. M.; Ganesan, V. Influence of pore morphology on the diffusion of water in triblock copolymer membranes. *J. Chem. Phys.* **2020**, *152*, No. 014904.

(39) Sax, J.; Ottino, J. M. Modeling of transport of small molecules in polymer blends: Application of effective medium theory. *Polym. Eng. Sci.* **1983**, *23*, 165−176.

(40) Kinning, D. J.; Thomas, E. L.; Ottino, J. M. Effect of Morphology on the Transport of Gases in Block Copolymers. *Macromolecules* **1987**, *20*, 1129−1133.

(41) Lindquist, W. B.; Lee, S.-M.; Coker, D. A.; Jones, K. W.; Spanne, P. Medial axis analysis of void structure in three-dimensional tomographic images of porous media. *J. Geophys. Res. Solid Earth* **1996**, *101*, 8297−8310.

(42) Gommes, C. J.; Bons, A.-J.; Blacher, S.; Dunsmuir, J. H.; Tsou, A. H. Practical Methods for Measuring the Tortuosity of Porous Materials from Binary or Gray-Tone Tomographic Reconstructions. *AIChE J.* **2009**, *55*, 2000−2012.

(43) Assenza, S.; Mezzenga, R. Curvature and bottlenecks control molecular transport in inverse bicontinuous cubic phases. *J. Chem. Phys.* **2018**, *148*, No. 054902.

(44) Michielsen, K.; De Raedt, H. Integral-geometry morphological image analysis. *Phys. Rep.* **2001**, *347*, 461−538.

(45) Armstrong, R. T.; McClure, J. E.; Robins, V.; Liu, Z.; Arns, C. H.; Schlüter, S.; Berg, S. Porous Media Characterization Using Minkowski Functionals: Theories, Applications and Future Directions. *Transp. Porous Media* **2019**, *130*, 305−335.

(46) Schlüter, S.; Weller, U.; Vogel, H.-J. Soil-structure development including seasonal dynamics in a long-term fertilization experiment. *J. Plant Nutr. Soil Sci.* **2011**, *174*, 395−403.

(47) Liu, Z.; Herring, A.; Arns, C.; Berg, S.; Armstrong, R. T. Pore-Scale Characterization of Two-Phase Flow Using Integral Geometry. *Transp. Porous Media* **2017**, *118*, 99−117.

(48) Breiman, L. Random Forests. Mach. Learn. 2001, 45, 5−32.

(49) Pedregosa, F.; et al. Scikit-learn: Machine Learning in Python. J.
Mach. Learn. Res. 2011, 12, 2825−2830.

