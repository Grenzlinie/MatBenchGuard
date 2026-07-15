# On the Relationship and Distinction Between Atomic Density and Coordination Number in Describing Grain Boundaries

Reza Darvishi Kamachali$^{1,2,*}$ , Theophilus Wallis$^{1}$

$^{1}$Federal Institute for Materials Research and Testing (BAM), 12205 Berlin, Germany
$^{2}$Institute of Materials Physics, University of Münster, 48149 Münster, Germany

Crystal defects are often rationalized through broken-bond counting via the nearest neighbor coordination number. In this work, we highlight that this perspective overlooks intrinsic heterogeneities in interatomic spacing that decisively shape defect properties. We analyze excess free volume, energy, and entropy for a large set of BCC-Fe grain boundaries relaxed by molecular statics and demonstrate that an atomic-density field, as a systematically coarse-grained field variable, provides a more comprehensive descriptor. Unlike coordination alone, the density field simultaneously captures bond depletion and spacing variations, thereby unifying structural and volumetric information. Our results establish density-based descriptors as principled surrogates for grain-boundary thermodynamics and kinetics, offer a direct bridge from atomistic data to mesoscale models, and motivate augmenting broken-bond rules in predictive theories of interfacial energetics, excess properties, segregation and phase behavior.

One of the enduring concepts in modeling defects is the notion of broken bonds. This model was originally articulated in the context of calculating surface energy and later extended to grain boundaries [1, 2]. This extension is well-justified, considering grain boundaries as two-dimensional crystallographic defects that disrupt the periodicity of the crystal lattice and involve a redistribution of atomic bonding environments. Within this framework, the reduction in atomic coordination at the boundary is used as a proxy for the energetic cost associated with grain boundary formation, and therefore, the *coordination number*—defined as the number of nearest-neighbor atoms—plays a central role.

The coordination number serves as a structural descriptor in various atomistic and empirical models, such as the broken-bond rule for grain boundary energy [3, 4], as well as in geometric and topological analyses of grain boundary networks [5]. It has also been widely applied in models of solute segregation, where it forms the basis for understanding the local chemical potential shifts near interfaces. For instance, in bond-breaking or bond-counting models of segregation [6, 7], solute atoms preferentially occupy under-coordinated sites at the grain boundary to reduce the system's energy. This principle underlies the McLean-type segregation isotherms [8] and continues to inform modern statistical-mechanical and thermodynamic models of grain boundary segregation [9, 10].

Despite its utility, the coordination number approach has inherent limitations: it discretely classifies neighbor counts but does not capture variations in interatomic spacing or local volume distortion. This fundamental limitation motivates the exploration of coarse-grained field descriptors, such as atomic density, to generalize and extend beyond coordination-based models.

In a series of recent studies, it has been proposed [11] and extensively demonstrated [12–18] that atomic density, formulated as a coarse-grained field variable, serves as a unifying variable, enabling the seamless integration of atomistic simulations, CALPHAD thermodynamics, and phase-field models in studying grain boundaries. The atomic density can be defined as

$$
\rho_{n}(\vec{r})=\sum_{I} \delta\left(\vec{r}-R_{I}\right), \tag{1}
$$

which sums over all atoms in a given system, with spatial coordination $\vec{r}$ and the position vectors of the atoms $R_{I}$. (The subscript $n$ in $\rho_{n}$ denotes the *number* density, will be dropped after Eq. (4) and should not be confused with the subscript later used in this monograph to indicate atomic coordination shells.) The delta function can then be replaced by a three-dimensional Gaussian distribution function, thus giving

$$
\rho_{n}(\vec{r})=\frac{1}{(\beta \sqrt{2 \pi})^{3}} \sum_{I} e^{-\frac{\left(\vec{r}-R_{I}\right)^{2}}{2 \beta^{2}}}, \tag{2}
$$

where $\beta$ is the smearing radius. Considering then a reference defect-free bulk system, we obtain the corresponding bulk atomic density

$$
\rho_{n}^{B}(\vec{r})=\frac{1}{(\beta \sqrt{2 \pi})^{3}} \sum_{I} e^{-\frac{\left(\vec{r}-R_{I}^{B}\right)^{2}}{2 \beta^{2}}} \tag{3}
$$

Here the superscript $B$ refers to that defect-free *bulk* system. Given that an appropriate $\beta$ value is chosen, $\rho_{n}^{B}(\vec{r})=\rho_{n}^{B}$ is a constant value within the bulk domain. Thus, the final dimensionless atomic density field is defined as

$$
\rho(\vec{r})=\frac{\rho_{n}(\vec{r})}{\rho_{n}^{B}}. \tag{4}
$$

* Corresponding author: reza.kamachali@bam.de (Reza Darvishi Kamachali)

Although Eqs. (1)-(4) do not explicitly mention any relation with the coordination number, the sum in these equations which runs over all atoms in a given system inherently encodes information about the number of neighboring atoms. To make this point clear, let us denote the number of atomic neighbors in the $n$-th coordination shell by $Z_n$, where $n=1,2,3,\dots$ corresponds to the first-, second-, third-nearest neighbors, and so on. The number of first-nearest neighbors, denoted as $Z_1$, is commonly referred to as the coordination number (a term originally coined from coordination chemistry).

In the reference bulk crystalline, the neighboring shells are defined based on the peaks in the radial distribution function, with each shell corresponding to a characteristic distance from a reference atom. Using Eq. (3) and the definitions outlined above, one can write the atomic density field in a defect-free bulk substance as

$$
\begin{aligned}
\rho_{n}^{B}(\vec{r}=R_{I}^{B}) &=\frac{1}{(\beta \sqrt{2 \pi})^{3}} \sum_{n} Z_{n}^{B} \cdot e^{-\frac{\left(R_{I}^{B}-R_{n}^{B}\right)^{2}}{2 \beta^{2}}} \\
&=\phi_{0}^{B}+Z_{1}^{B} \cdot \phi_{1}^{B}+Z_{2}^{B} \cdot \phi_{2}^{B}+Z_{3}^{B} \cdot \phi_{3}^{B}+\ldots,
\end{aligned}
\tag{5}
$$

where the summation is restructured from individual atoms $I$ to atoms in distinct coordination shells $n$, with $Z_n^B$ denoting the number of atoms in the $n$-th shell and $R_n^B$ denoting their equilibrium radial position (where $|R_I^B - R_n^B|$ is the shell radius). For instance, in a perfect body-centered cubic (BCC) structure, the first (coordination) shell contains $Z_1^B=8$ atoms, while the second shell contains $Z_2^B=6$, and the third shell $Z_3^B=12$, located at increasing radial distances. Here

$$
\phi_{n}^{B}=\frac{e^{-\frac{\left(R_{I}^{B}-R_{n}^{B}\right)^{2}}{2 \beta^{2}}}}{(\beta \sqrt{2 \pi})^{3}}
\tag{6}
$$

represents the normalized Gaussian contribution from the $n$-th shell with respect to a reference atom at $R_I^B$. $\phi_0^B$ corresponds to the center atom itself with $R_I^B=R_n^B$. Thus, $|R_I^B - R_n^B|$ is the radius of $n$th shell. This formulation implicitly assumes spherical symmetry and isotropic atomic environments, as appropriate for a perfect crystal. The physical unit of $\phi_n^B$ is $[\text{length}]^{-3}$ and the inverse of it is a *coordination volume*. Note that, for the sake of simplicity, Eq. (5) is written only at atomic positions $\vec{r}=R_I^B$, yet, the resulting value of the density field remains the same and a constant due to the translational symmetry of a defect-free crystal.

Referring now to disordered regions such as grain boundaries, the ideal shell structures become perturbed, resulting in local deviations in the number of neighboring atoms. This can be symbolically expressed as

$$
Z_n: Z_n^B \to \{Z_n\}^{GB}
\tag{7}
$$

where the bracket $\{\dots\}$ indicates a distribution and superscript GB denotes the grain boundary. This naturally induces variations in the coarse-grained atomic density field. Equation (5) demonstrates that $\rho(\vec{r})$ directly reflects on the number of neighboring atoms.

Considering the first leading term, we can see that the atomic density is proportional to the coordination number: $\rho_n^B(R_I) \approx Z_1^B \cdot \phi_1^B$. However, it is readily clear that the *interatomic spacing* between neighboring atoms must also adjust accordingly to accommodate local structural (and subsequently also chemical) inhomogeneities. In other words, not only does the discrete count of atoms in each coordination shell vary (Eq. (7)) but so too do the radial distances and the corresponding kernel weights

$$
R_n: R_n^B \to \{R_n\}^{GB},
\tag{8}
$$

$$
\phi_n: \phi_n^B \to \{\phi_n\}^{GB}.
\tag{9}
$$

The above analyses suggest that the coordination number ($Z_1$), or even an extended set of higher-order neighbor counts ($Z_2$, $Z_3$ ...), is insufficient to fully characterize defect structures. Instead, it is the combined information on both the number and spatial proximity of neighboring atoms that defines the structural nature of a defect. These aspects both are captured by the atomic density field $\rho(\vec{r})$, such that regions with reduced coordination and/or expanded interatomic spacing—typically observed near disordered interfaces or defects manifest as local depletion in $\rho(\vec{r})$. Conversely, more densely coordinated and/or compressed regions correspond to local maxima. In contrast, coordination number metrics are insensitive to variations in interatomic spacing, inherently captured in the kernel contributions ($\phi_1$, $\phi_2$, $\dots$). $\rho(\vec{r})$ encodes not only the coordination number but also the local volumetric distortion, providing a more comprehensive representation of the atomic environment than coordination numbers alone—even when considering multiple neighboring shells. This enriched descriptive power is crucial for accurately capturing grain boundary structure, long-range elastic fields, and excess volume, and is therefore essential for correctly computing the associated energy and entropy of the defect.

In the following we confront the two descriptors with data. We analyze a comprehensive set of 408 distinct BCC-Fe grain boundaries (tilt, twist and mixed), generated and relaxed by molecular statics; protocol details are given elsewhere [19, 20].

Recent analyses [20, 21] show that the *grain boundary density*, defined as the average atomic density at the grain boundary plane,

$$
\rho^{GB}=\langle\rho(\vec{r})\rangle_{\text {at the GB plane }},
\tag{10}
$$

serves as a representative scalar quantity for the overall change in the atomic density field associated with a grain boundary.

![](./images/1167070870431072293_1.jpg)

FIG. 1. Representative grain boundary examples. (a) Atomistic structures for Σ3, Σ5, and Σ9 boundaries; (b) coarse-grained atomic density fields $\rho(\vec{r})$ showing depletion at the GB plane; (c) density profiles $\rho(x)$ across the GB with $\rho^{GB}$ marked; (d) atomic coloring by first coordination number $Z_1$; (e) profiles of $(Z_1(x)-8)/8$ across the GB with reduced values at the interface. The error bars in (c) and (e) show the range of the depicted quantity in the corresponding $yz$-slice.

Analogous to $\rho^{GB}$, we can define the coordination number for every atom, average it at the GB plane
$$
Z_1^{GB} = \langle Z_1(R_I) \rangle_{\text{at the GB plane}}, \tag{11}
$$
giving a similar dimensionless value $(8-Z_1^{GB})/8$.

For each boundary we evaluate the *density deficit* $(1-\rho^{GB})$ and the *coordination deficit* $(8-Z_1^{GB})/8$, see Methods. These are then compared against three independent GB properties: the excess free volume per unit area $\Delta V$, the GB energy $\gamma^{GB}$, and two measures of configurational entropy per unit area—one obtained from the atomic- density field $S_\rho^{GB}$ and the other from shell descriptors, the *sum entropy* $\frac{1}{2}S_{Z_1,\tilde{\phi}_1,Z_2,\tilde{\phi}_2}^{GB}$. Throughout, boundaries are grouped by parent-plane family for reference. We begin with representative examples (Fig. 1), then examine the joint variation of the two deficits (Fig. 2), followed by their relations to $\Delta V$ (Fig. 3) and $\gamma^{GB}$ (Fig. 4). Finally, we consider the entropic content (Fig. 5) and demonstrate the equivalence between $S_\rho^{GB}$ and the sum entropy (Fig. 6).

Figure 1 shows representative grain-boundary structures alongside the coarse-grained density fields and coordination maps, indicating that the planar-averaged density $\rho(x)$ exhibits a clear depletion at the interface that robustly locates the GB, while the $Z_1$ maps register coordination loss only where it occurs. All three Σ3, Σ5 and Σ9 boundaries show coincident reductions in both $\rho$ and $Z_1$, however, it is clear that the density field results in a consistent definition of the grain boundary region for all three examples, whereas the variations in coordination number are rather case-specific. Figure 2 shows the scatter of the density deficit $(1-\rho^{GB})$ against the coordination deficit $(8-Z_1^{GB})/8$ at the GB plane, for

![](./images/1167070870431072293_2.jpg)

FIG. 2. Correlation between density and coordination.
Scatter plot of density deficit $(1-\rho^{GB})$ versus coordination
deficit $(8-Z_{1}^{GB})/8$ at the GB plane, across 408 BCC-Fe grain
boundaries. Grain boundaries are classified by parent plane
family, listed in the legend panel. This classification is the
same in all following figures. The broad scatter demonstrates
that $\rho^{GB}$ and $Z_{1}^{GB}$ are not equivalent descriptors. Notably,
a sizable population has $Z_{1}^{GB} \approx Z_{1}^{B}(=8)$ while exhibiting a
nonzero density deficit.

all 408 GBs, indicating a loose relation between the two
descriptors: many boundaries exhibit $(8-Z_{1}^{GB})/8 \approx 0$
while maintaining a finite density deficit, and for a given
$(1-\rho^{GB})$ the corresponding $(8-Z_{1}^{GB})/8$ spans a wide
range. This non-equivalence anticipates the trends in
Figs. 3-4, where $(1-\rho^{GB})$ proves the more predictive
scalar for $\Delta V$ and $\gamma^{GB}$. Grain boundaries are classified
and colored based on their parent atomic planes.

Recently we have demonstrated that GB atomic density
reveals a remarkable correlation with the excess free vol-
ume [20]. This is a nontrivial result as the GB density is
the single (minimum) average density value at the grain
boundary plane whereas the excess free volume is an in-
tegral property of the grain boundary. Figure 3 con-
trasts the excess free volume per unit area, $\Delta V$, with
the density deficit $(1-\rho^{GB})$ and the coordination deficit
$(8-Z_{1}^{GB})/8$. Panel (a) shows that $\Delta V$ collapses onto an
almost perfectly linear trend with $(1-\rho^{GB})$ across all 408
boundaries, with only minor family-dependent spread,
i.e. the single GB-plane quantity $\rho^{GB}$ reliably predicts
the integral excess volume. By contrast, panel (b) ex-
hibits a weak, highly scattered relation with $(8-Z_{1}^{GB})/8$,
including a sizable vertical band at $(8-Z_{1}^{GB})/8 \approx 0$ where
$\Delta V$ spans a wide range. These boundaries -with nonzero
excess volume but no coordination deficit-demonstrate
that variations in interatomic spacing and local dilation,
captured by the density field, are essential for excess vol-
ume, whereas coordination counts alone systematically
miss this contribution.

Figure 4 summarizes the energetic trends: $\gamma^{GB}$ increases
monotonically with the density deficit $(1-\rho^{GB})$ with
a comparatively clear family-dependent spread, whereas
its dependence on the coordination deficit $(8-Z_{1}^{GB})/8$
is weak and highly dispersed. Notably, many bound-
aries with $(8-Z_{1}^{GB})/8 \approx 0$ still carry substantial en-
ergy, demonstrating that elastic/dilatational contribu-
tions, captured by the density field, set the energetic scale
that broken-bond counts alone cannot capture.

In order to quantify and discern the significance of the
changes in interatomic spacing, we further our analyses
by computing the entropy due to the disorder within a
given system induced by a grain boundary. In princi-
ple, the relevant measure is the Shannon entropy, which
arises from the combined topological (bond depletion)
and distantial (variations in interatomic spacing) disor-
der within the grain boundary. These two aspects are
respectively captured in Eq. (5) where both coordination
numbers and volumes are listed. Clearly, other degrees
of disturbance can still be imagined, e.g., the shape of
closed volumes around every atom, which we omit from
our entropy calculations. For a grain boundary region,
truncating the atomic density formula to the first two
terms, we can write

$$
\rho_{n}(\vec{r}=R_{I}) \approx Z_{1}(R_{I}) \cdot \tilde{\phi}_{1}(R_{I})+Z_{2}(R_{I}) \cdot \tilde{\phi}_{2}(R_{I}) \quad (12)
$$

where $\rho_{n}(\vec{r}=R_{I})$ is computed based on Eqs. (1)-(4)
and the right-hand side can be obtained for each atom
such that $\tilde{\phi}_{1}$ and $\tilde{\phi}_{2}$ are

$$
\tilde{\phi}_{1(o r ~ 2)}(R_{I})=\frac{e^{-\frac{\left(R_{I}-\tilde{R}_{1(o r ~ 2)}\right)^{2}}{2 \beta^{2}}}}{(\beta \sqrt{2 \pi})^{3}} \quad (13)
$$

with $\tilde{R}_{1}$ and $\tilde{R}_{2}$ being effective radii computed based on
the respective effective volume of the first and second
coordination shell around a given atom.

We compute the entropy in two ways: once from the
spatial distribution of the atomic density field across the
grain boundary, $S_{\rho}^{GB}$, and once from per atom distribu-
tions of the descriptors, $S_{q}^{GB}$, with $q$: $Z_{1}, Z_{2}, \tilde{\phi}_{1}, \tilde{\phi}_{2}$. See
Methods for the precise definitions and procedure. From
the descriptor entropies, the sum entropy reads

$$
\frac{1}{2} S_{Z_{1}, \tilde{\phi}_{1}, Z_{2}, \tilde{\phi}_{2}}^{GB}=\frac{1}{2}\left(S_{Z 1}^{GB}+S_{\tilde{\phi}_{1}}^{GB}+S_{Z 2}^{GB}+S_{\tilde{\phi}_{2}}^{GB}\right) \quad (14)
$$

See Methods section for details. One of the main re-
sults of our study is the numerical equivalence of the
density-based entropy and the sum entropy, $S_{\rho}^{GB} \approx$
$\frac{1}{2} S_{Z_{1}, \tilde{\phi}_{1}, Z_{2}, \tilde{\phi}_{2}}^{GB}$, thereby confirming that the atomic-density
field compactly captures the joint topological-distantial
disorder encoded by the shell descriptors.

Figure 5 presents the sum entropy $\frac{1}{2} S_{Z_{1}, \tilde{\phi}_{1}, Z_{2}, \tilde{\phi}_{2}}^{GB}$ per unit
area against the two GB-plane descriptors. Panel (a)
in Fig. 5 shows a monotonic increase of the sum entropy
with the density deficit $(1-\rho^{GB})$, consistent with the no-
tion that combined topological-distantial disorder grows
as the atomic density depletes at the interface.

![](./images/1167070870431072293_3.jpg)

FIG. 3. GB excess free volume versus density and coordination. (a) Excess free volume per unit area $\Delta V^{GB}$ collapses onto a near-perfect line with the density deficit $(1-\rho^{GB})$ across 408 BCC-Fe grain boundaries; (b) $\Delta V^{GB}$ shows only a weak, scattered dependence on the coordination deficit $(8-Z_{1}^{GB})/8$, even for a given atomic plane family of grain boundaries.

![](./images/1167070870431072293_4.jpg)

FIG. 4. GB energy versus density and coordination. (a) Grain-boundary energy $\gamma^{GB}$ increases systematically with the density deficit $(1-\rho^{GB})$ across 408 BCC-Fe grain boundaries; (b) in contrast, $\gamma^{GB}$ shows a weak, dispersed dependence on the coordination deficit $(8-Z_{1}^{GB})/8$, including many cases with $(8-Z_{1}^{GB})/8\approx0$ but finite energy. Grain boundaries are classified by parent plane family.

Panel (b) in Fig. 5 contrasts this with a loose, het-eroscedastic relation versus the coordination deficit $(8-Z_{1}^{GB})/8$, including many boundaries with no coordination deficit that nevertheless span nearly the full entropy range. In particular, this decoupling confirms that coordination counts alone underestimate the configurational disorder when spacing fluctuations dominate, whereas the density field -by construction- captures both ingredients.

Figure 6 then compares the two entropy constructions directly. We find that $S_{\rho}^{GB}$ aligns tightly with $\frac{1}{2}S_{Z_{1},\tilde{\phi}_{1},Z_{2},\tilde{\phi}_{2}}^{GB}$ along the $y{=}x$ line, with a near-unity slope and a small intercept across all families. This validates the sum relation and shows that $S_{\rho}^{GB}$ is a compact, lossless proxy for the joint shell-descriptor information: the atomic density field encodes the combined effect of neighbor multiplicities and interatomic spacing, whereas $Z_{1}$ alone does not.

A particular point of discussion reflects in our results is about a large group of grain boundaries, of different classes, that have $Z_{1}^{GB}\approx8$. For twin and some special boundaries where the atomic coordination numbers at the grain boundaries remain the same as in the bulk lattice, DFT calculations show that segregation can still happen and the electronic contributions to the segregation energy can be significant, indicating that the chemical bonding between solute and host atoms is quite different from that of grain interior [22]. This is precisely what is expected for the vertical population at $(8-Z_{1}^{GB})/8\approx0$ observed here.

![](./images/1167070870431072293_5.jpg)

FIG. 5. Configurational entropy versus density and coordination. (a) The sum configurational entropy per unit area $\frac{1}{2} S_{Z_{1}, \tilde{\phi}_{1}, Z_{2}, \tilde{\phi}_{2}}^{G B}$ increases systematically with the density deficit $(1-\rho^{G B})$, reflecting growth of combined topological-distantial disorder with density depletion; (b) the same quantity versus the coordination deficit $(8-Z_{1}^{G B})/8$ exhibits only a loose relation with pronounced scatter, including many grain boundaries with $(8-Z_{1}^{G B})/8 \approx 0$ spanning nearly the full entropy range.

For the same populations we have $(1-\rho^{G B})>0$ and a finite $\Delta V$ and $\gamma^{G B}$ that can explain subsequent segregation behavior. In contrast, we find that the density framework is agnostic to grain boundary character and thus captures features that are generic across classes. Considering low-angle boundaries, where the structure is well-described as an array of dislocations (Read-Shockley type) with long-range elastic fields, the local coordination remains essentially bulk-like over most sites, yet the dilatational/compressional strains induce a measurable depletion in the coarse-grained density at the grain boundary plane. Conversely, in more disordered or high-angle boundaries, where substantial local volume changes and topology disruptions occur, both $Z_{1}$ and $\rho$ vary, but the density field integrates spacing heterogeneity and excess volume more faithfully, yielding the tight trends with $\Delta V$, $\gamma^{G B}$, and the growth of configurational entropy.

Taken together, the results show that $\rho(\vec{r})$ unifies long-range elastic effects (with minimal coordination change) and strongly disordered cores (with both topology and spacing changes), thereby providing a single state variable that is predictive across the full GB spectrum. These aspects motivate that the atomic density field parameter can be very useful in studying the mechanical [23–25] or electrical [26] response of grain boundaries, in the same spirit of the grain boundary excess volume. Another remarkable aspect $\rho(\vec{r})$ and $\rho^{G B}$ is their potential to link with the experimental measurements: Quantitative routes to measure local atomic density at (deformation) interfaces are developed by combining HAADF-STEM with EELS thickness calibration and 4D-STEM with machine learning techniques [27–30]. Independent radiotracer experiments revealed orders-of-magnitude enhancement of atomic diffusion inside free-volume-rich short-circuit paths [31] which can also be linked with the atomic density field.

![](./images/1167070870431072293_6.jpg)

FIG. 6. Equivalence of density and sum entropy. Areal configurational entropy from the density field, $S_{\rho}^{G B}$, plotted against the sum entropy $\frac{1}{2} S_{Z_{1}, \tilde{\phi}_{1}, Z_{2}, \tilde{\phi}_{2}}^{G B}$; data cluster tightly about the $y{=}x$ line (dashed), indicating a near-unity slope and small intercept across 408 BCC-Fe grain boundaries, thereby validating the sum relation and underscoring the information captured by the atomic-density field beyond coordination counts.

To summarize, the above analyses show that a coarse-grained atomic density field, $\rho(\vec{r})$, captures the essential grain boundary physics and more completely than coordination number. While $Z_{1}$ registers broken bonds, $\rho$ embeds both topology (neighbor multiplicity) and spacing (local dilation/compression). This distinction is not semantic: across 408 BCC-Fe boundaries the density deficit $(1-\rho^{G B})$ collapses the excess free volume $\Delta V$ onto an almost perfectly linear trend and organizes the GB energy $\gamma^{G B}$ with modest family dependent spread,

whereas $(8 - Z_1^{GB})/8$ shows broad, heteroscedastic scat- ter and admits many boundaries with no coordination deficit but finite $\Delta V$ and $\gamma^{GB}$. These cases diagnose elastic/dilatational contributions that are invisible to broken-bond counting but are, by construction, encoded in $\rho$.

A second conceptual outcome concerns configurational disorder. We show that the density-based entropy $S_{\rho}^{GB}$ is able to track the sum entropy $\frac{1}{2}(S_{Z_1}^{GB} + S_{\phi_1}^{GB} + S_{Z_2}^{GB} + S_{\phi_2}^{GB})$, nearly one-to-one. This numerical equivalence in- dicates that $\rho$ is a compact, effectively lossless proxy for the joint topological-distantial disorder. In information terms, the strong in-shell correlations (between $Z_s$ and $\tilde{\phi}_s$) imply substantial redundancy; the observed one-half prefactor reflects an effective two-mode structure domi- nated by the first two shells. Thus, $\rho$ summarizes what matters for GB thermodynamics without proliferating descriptors.

Practically, these results argue for augmenting broken- bond rules with density-based descriptors in models of GB energetics, excess properties, and segregation ther- modynamics. Because $\rho$ is a field, it interfaces naturally with continuum treatments (e.g., CALPHAD/phase- field) and can carry elastic fields and volumetric ex- cess in a consistent way. The subsumption of coordi- nation number, interatomic spacing, excess volume and isotropic elasticity within a single density-based frame- work suggests that $\rho(\vec{r})$ is a convenient surrogate and a candidate descriptor of crystalline disorder. Limita- tions remain: our dataset is BCC-Fe at 0 K (molecu- lar statics), the coarse-graining length $\beta$ sets resolution and must be chosen judiciously, and the entropies used here are information-theoretic measures rather than full thermodynamic entropies. Nonetheless, the robustness of the trends across orientations and families suggests that the density framework is structurally generic. Ex- panding the current comparative analyses to other lat- tice structures, finite temperature, multi-component al- loys with segregation, and kinetic phenomena (faceting, complexion transitions) should be particularly informa- tive, with $\rho$ providing a unifying state variable across atomistic and mesoscale descriptions. Also revisiting ex- perimental procedures to study density deficits and ex- cess volumes with diffraction, positron annihilation, high- resolution microscopy or even daring atom probe tomog- raphy measurements would provide decisive advancement in closing the loop between atomistics, mesoscale models, and experiment in studying microstructure defects.

## METHODS

### Atomistic Simulation Dataset:
We analyze a set of 408 distinct grain boundaries (GBs) in BCC-Fe generated and minimized following established protocols [19, 20].

Bicrystals are constructed with periodicity parallel to the GB and sufficient padding normal to the interface to suppress image interactions. After rigid-body scans and in-plane relaxations, structures are relaxed to a force and energy tolerance by conjugate-gradient minimiza- tion. Grain boundary energies and excess free volumes are computed using the atomistic simulations, for each grain boundary and both are per unit area. All coarse- graining and further analyses reported below are per- formed on the minimized configurations. Further details of structure generation and parameterization as well as on the methods of coarse-graining atomic density field are provided in [19, 20]; for the present study, we only summarize the definitions needed in the body of text. For visualization we group grain boundaries by parent plane families and special boundaries (e.g., $\Sigma 3$) following [20]. Symbols and colors in the figures map consistently across panels; all scalars shown with appropriate units, or are dimensionless (for the atomic density and coordination number deficit at the GB plane).

Atomic density and coordination number: In each system and at the position of each atom, we compute atomic density value $(\rho(\vec{r}=R_I))$, coordination number $(Z_1(R_I))$ and 2nd coordination number $(Z_2(R_I))$. Note the $\rho(\vec{r})$ can be computed for every position in the system. The coarse-grained atomic density computation is of course sensitive to coarse-graining length (smearing radius $\beta$ in the Gaussian distribution). This sensitivity is thoroughly discussed in [20]. We use $\beta=2.4r_{Fe}$ with $r_{Fe}=1.26$ Å being the atomic radius of iron. The GB plane is defined as the location of the minimum of the planar-averaged density along the interface normal. We compute
$$
\langle\rho\rangle(x)=\frac{1}{A} \int_{A} \rho(\vec{r}) d y d z,\qquad(15)
$$
identify $x_{\mathrm{GB}}=\arg \min _{x}\langle\rho\rangle(x)$, and evaluate GB-plane averages over a narrow slab of thickness $w$ centered at $x_{\mathrm{GB}}$,
$$
\rho^{G B}=\frac{1}{A w} \int_{x_{\mathrm{GB}}-w / 2}^{x_{\mathrm{GB}}+w / 2} \int_{A} \rho(\vec{r}) d x d y d z.\qquad(16)
$$
where $w=0.2$ Å is the bin size in saving the continu ous coarse-grained atomic density field. All GB-resolved scalar quantities below use the same slab.

Nearest-neighbor coordination numbers are obtained from a bulk-referenced cutoff at the first minimum of the bulk radial distribution function, yielding $Z_1(R_I)$ at each atom position. We form the GB-plane average
$$
Z_{1}^{G B}=\left\langle Z_{1}\right\rangle_{\text {GB slab }}, \quad \delta Z_{1}^{G B}=1-\frac{Z_{1}^{G B}}{Z_{1}^{B}}.\qquad(17)
$$
with $Z_1^B=8$.

To quantify spacing effects we use Eqs. (12) and (13) effective shell weights $\tilde{\phi}_n$ are defined. First, we compute

the local shell volume for $Z_2$, that is the Voronoi volume for BCC structure, to compute an equivalent radius $\tilde{R}_2$ and evaluating the same Gaussian kernel $\tilde{\phi}_2$. Using above computed data and Eqs. (12) we compute $\tilde{\phi}_1 \approx \frac{\rho_n - Z_2 \tilde{\phi}_2}{Z_1}$ for each atom. As $\tilde{R}_n$ is computed from the spatial coordinates $\vec{r}$ of neighbors (not from any topological count), using mid-shell boundaries between consecutive neighbor distances to define the shell volume. The pair $(Z_n, \tilde{\phi}_n)$ thus separates topology (counts) and distance (spacing).

Configurational Shannon entropy from atomic density and from Shell descriptors: We compute configurational Shannon entropies from spatial per-atom distributions that are obtained from our analyses. Note that this is not the same thing as thermodynamic entropy: Shannon entropy is the entropy merely due to the disorder in the given system. In our atomistic simulation set-up the only source of disorder is the (single) grain boundary. We thus can compute this quantity per unit area of the grain boundary. For every property $q$,

$$
p_{q}=\frac{|q|}{\sum_{J}|q|}, \quad S_{q}^{0}(J)=-k_{B} \sum_{J} p_{q} \ln p_{q}, \quad(18)
$$

where $q \in (\rho_n, \rho_n^B, Z_1, Z_1^B, \tilde{\phi}_1, \tilde{\phi}_1^B, Z_2, Z_2^B, \tilde{\phi}_2, \tilde{\phi}_2^B)$ and $J$ indicates the number of atoms in the whole system $(J=I)$ or a bulk subsystem $(J=I^B)$. Precisely, $I$ considers ALL atoms and $I^B$ indicates Bulk atoms away from the GB plane (10 Å) and also non-periodic boundaries along the $x$ axis (removed by indexing those atoms). Thus, we compute the grain boundary excess entropy

$$
\begin{aligned}
S_{q}^{G B} & =\frac{N^{G B}}{A}\left(S_{q}^{0}(\mathrm{ALL})-S_{q}^{0}(\mathrm{Bulk})\right) \\
& =\frac{N^{G B}}{A}\left(S_{q}^{0}(J=I)-S_{q}^{0}\left(J=I^{B}\right)\right).
\end{aligned} \quad(19)
$$

For example, $S_{\rho}^{G B}=\frac{N^{G B}}{A}\left(S_{\rho}^{0}-S_{\rho^{B}}^{0}\right)$ where $N^{G B}$ and $A$ are the number of atoms and area of the grain boundary.

Sum entropy and correlation analysis: To rationalize the empirical relation $S_{\rho}^{G B} \approx \frac{1}{2} \sum_{X} S_{X}$, with $X = (Z_1, \tilde{\phi}_1, Z_2, \tilde{\phi}_2)$, we analyze the Pearson cross-correlations among six descriptor pairs $r(Z_1,Z_2)$, $r(Z_1,\tilde{\phi}_1)$, $r(Z_1,\tilde{\phi}_2)$, $r(Z_2,\tilde{\phi}_1)$, $r(Z_2,\tilde{\phi}_2)$, $r(\tilde{\phi}_1,\tilde{\phi}_2)$ per each grain boundary,

$$
r(x, y)=\frac{\frac{1}{N} \sum_{I-I^{B}}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)}{\sqrt{\frac{1}{N} \sum_{I-I^{B}}\left(x_{i}-\bar{x}\right)^{2}} \sqrt{\frac{1}{N} \sum_{I-I^{B}}\left(y_{i}-\bar{y}\right)^{2}}},
$$

with $N$ the number of atoms in the corresponding $I-I^B$ region.

The resulting cross-correlations reveal a clear structure: We observe that most notably $(Z_1,\tilde{\phi}_1)$ and $(Z_2,\tilde{\phi}_2)$ are dominated by strong correlations. These results indicate that the count and spacing in each shell have high overlaps in their topological contribution. At the same time we observe that only first shell is not enough to match the accuracy obtainable by the atomic density. Taken together, these patterns indicate that the information carried by $(Z_1,\tilde{\phi}_1,Z_2,\tilde{\phi}_2)$ are contributing but with $\simeq 50\%$ redundancy. The statistical balance of strong positive and strong negative correlations gives

$$
S_{\rho}^{G B} \approx \frac{1}{2} S_{Z_{1}, \tilde{\phi}_{1}, Z_{2}, \tilde{\phi}_{2}}^{G B}=\frac{1}{2} \sum_{X \in\left(Z_{1}, \tilde{\phi}_{1}, Z_{2}, \tilde{\phi}_{2}\right)} S_{X}^{G B}, \quad(21)
$$

with the factor of 1/2 reflecting the effective redundancy among descriptors revealed by their correlation structure. Extensive details on all entropy-related calculations will be soon added as Supplementary Material.

[1] W. Read and W. Shockley, Dislocation models of crystal grain boundaries, Physical Review 78, 275 (1950).

[2] J. Hirth and J. Lothe, Theory of Dislocations (Wiley, 1982).

[3] Y. Du and L. Chen, Systematic analysis of grain boundary energy in bcc metals using the broken-bond model, Acta Materialia 53, 2539 (2005).

[4] G. Rohrer, Grain boundary energy anisotropy: A review, Journal of Materials Science 46, 5881 (2011).

[5] Y. Mishin, Atomistic modeling of grain boundary structure and segregation, Acta Materialia 58, 1117 (2010).

[6] M. Seah, Adsorption-induced interface decohesion, Acta Metallurgica 28, 955 (1980).

[7] P. Lejček, Grain Boundary Segregation in Metals (Springer, 2010).

[8] D. McLean, Grain boundary segregation in metals, Reports on Progress in Physics 18, 266 (1957).

[9] S. Foiles, Calculation of the segregation of impurities to grain boundaries in metals, Physical Review B 32, 7685 (1985).

[10] H. Murdoch and C. Schuh, Grain boundary segregation enthalpies and energies in binary alloys from atomistic simulations, Acta Materialia 61, 2121 (2013).

[11] R. Darvishi Kamachali, A model for grain boundary thermodynamics, RSC Advances 10, 26728 (2020).

[12] R. Darvishi Kamachali, A. Kwiatkowski da Silva, E. McEniry, D. Ponge, B. Gault, J. Neugebauer, and D. Raabe, Segregation-assisted spinodal and transient spinodal phase separation at grain boundaries, npj Computational Materials 6, 191 (2020).

[13] L. Wang and R. D. Kamachali, Density-based grain boundary phase diagrams: Application to Fe-Mn-Cr, Fe-Mn-Ni, Fe-Mn-Co, Fe-Cr-Ni and Fe-Cr-Co alloy systems, Acta Materialia , 116668 (2021).

[14] X. Zhou, R. D. Kamachali, B. L. Boyce, B. G. Clark, D. Raabe, and G. B. Thompson, Spinodal decomposition in nanocrystalline alloys, Acta Materialia , 117054 (2021).

[15] L. Wang and R. D. Kamachali, Incorporating elastic- ity into calphad-informed density-based grain boundary phase diagrams reveals segregation transition in al-cu and al-cu-mg alloys, Computational Materials Science 199, 110717 (2021).

[16] L. Wang and R. D. Kamachali, Calphad integrated grain boundary co-segregation design: Towards safe high- entropy alloys, Journal of Alloys and Compounds 933, 167717 (2023).

[17] T. Wallis and R. D. Kamachali, Grain boundary struc- tural variations amplify segregation transition and stabi- lize co-existing spinodal interfacial phases, Acta Materi- alia 242, 118446 (2023).

[18] R. D. Kamachali, T. Wallis, Y. Ikeda, U. Saikia, A. Ah- madian, C. H. Liebscher, T. Hickel, and R. Maaß, Giant segregation transition as origin of liquid metal embrittle-ment in the fe-zn system, Scripta Materialia 238, 115758(2024).

[19] S. Ratanaphan, D. L. Olmsted, V. V. Bulatov, E. A. Holm, A. D. Rollett, and G. S. Rohrer, Grain boundary energies in body-centered cubic metals, Acta Materialia88, 346 (2015).

[20] T. Wallis and R. Darvishi Kamachali, Linking atomistic and phase-field modelling of grain boundaries i: Coarse-graining atomistic structures, Under Review (2025).

[21] T. Wallis and R. Darvishi Kamachali, Linking atomistic and phase-field modelling of grain boundaries ii: Incor- porating atomistic potentials into free energy functional, Under Review (2025).

[22] Y.-J. Hu, Y. Wang, W. Y. Wang, K. A. Darling, L. J.Kecskes, and Z.-K. Liu, Solute effects on the $\Sigma 3111$ [11-0] tilt grain boundary in BCC Fe: Grain boundary segrega- tion, stability, and embrittlement, Computational Mate- rials Science 171, 109271 (2020).

[23] T. Frolov and Y. Mishin, Thermodynamics of coherent interfaces under mechanical stresses. i. theory, Physical Review B-Condensed Matter and Materials Physics 85,224106 (2012).

[24] T. Frolov and Y. Mishin, Thermodynamics of coherent interfaces under mechanical stresses. ii. application to atomistic simulation of grain boundaries, Physical Re- view B-Condensed Matter and Materials Physics 85,224107 (2012).

[25] G. Dehm and J. Cairney, Implication of grain-boundary structure and chemistry on plasticity and failure, MRS Bulletin 47, 800 (2022).

[26] H. Bishara, M. Ghidelli, and G. Dehm, Approaches to measure the resistivity of grain boundaries in metals with high sensitivity and spatial resolution: A case study em-ploying cu, ACS Applied Electronic Materials 2, 2049(2020).

[27] H. Rösner, M. Peterlechner, C. Kübel, V. Schmidt, and G. Wilde, Density changes in shear bands of a metallic glass determined by correlative analytical transmission electron microscopy, Ultramicroscopy 142, 1 (2014).

[28] V. Schmidt, H. Rösner, M. Peterlechner, G. Wilde, and P. M. Voyles, Quantitative measurement of density in a shear band of metallic glass monitored along its propa- gation direction, Phys. Rev. Lett. 115, 035501 (2015).

[29] Y. Buranova, H. Rösner, S. V. Divinski, R. Imlau, and G. Wilde, Quantitative measurements of grain boundary excess volume from haadf-stem micrographs, Acta Ma- terialia 106, 367 (2016).

[30] G. Cheng, K. Yin, S. J. Grutzik, S. J. Zinkle, H. Bei, S. Xia, and J. Li, Mapping free volume distributions in oxide glasses by four-dimensional scanning transmission electron microscopy, ACS Nano 15, 19435 (2021).

[31] J. Bokeloh, S. V. Divinski, G. Reglitz, and G. Wilde, Tracer measurements of atomic diffusion inside shear bands of a bulk metallic glass, Phys. Rev. Lett. 107,235503 (2011).

## ACKNOWLEDGMENTS

We acknowledge the financial support from the Ger- man research foundation (DFG) within the project $DA$1655/3-1, DA 1655/4-1 and the Heisenberg programme project $DA$ 1655/2-1.

## STATEMENT

The current version of this manuscript is released for the sake of discussion and possible feedback. Further data and codes of this study will be made soon available. Methods and additional discussions are under prepara-tion to be presented in a Supplementary Material (SM) document to be attached in the next version of the manuscript.