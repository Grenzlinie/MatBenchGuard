# Phase Morphologies in Reversibly Bonding Supramolecular Triblock Copolymer Blends

Won Bo Lee,† Richard Elliott,‡ Kirill Katsov,‡ and Glenn H. Fredrickson*,†,‡,§

Department of Chemical Engineering, University of California, Santa Barbara, California 93106, Materials Research Laboratory, University of California, Santa Barbara, California 93106, and Department of Materials, University of California, Santa Barbara, California 93106

Received July 31, 2007; Revised Manuscript Received September 11, 2007

ABSTRACT: Thermoreversible, supramolecular self-assembly in multiblock copolymer melts is investigated with two microscopic approaches. We consider a blend consisting of two chemically distinct, but reactive homopolymers. One homopolymer has a single reactive end group at one of its ends, while the second has functional end groups at both ends. Reversible bonding is constrained to occur between dissimilar blocks so that this mixture is capable of forming diblocks and triblocks but no other copolymers. All copolymer concentrations are thus controlled by the bonding strength, segmental incompatibility, and the relative proportions and chain lengths of the homopolymers. Changing the ratio of homopolymer chain lengths, which controls the architecture of the copolymers, has a dramatic effect on not only the extent of reversible bonding but also the phase morphology, which is reflected in the equilibrium mesophase structures and liquidus line. Two characteristic mean-field (SCFT) phase diagrams are calculated at high bonding strength to illustrate this architectural dependence. The high-bonding strength phase behavior is explained with a mean-field analysis of the copolymer densities. Trends in the phase diagram for the weaker bonding regime, which include reentrant behavior, are investigated using the random phase approximation.

## 1. Introduction

Supramolecular polymers utilize noncovalent bonds, such as hydrogen, pi stacking, or metal−ligand interactions, to tether functional polymeric units together into larger macromolecules varying in size, architecture, and/or composition. If the bond strength is comparable to the thermal energy $k_{\text{B}}T$, the bonding is reversible and the number and the architecture of the resulting supramolecular polymer complexes may be controlled with the temperature. This is an appealing characteristic because molecular connectivity and the material properties (including processability) that depend on this connectivity can be thermally controlled.

When chemically dissimilar polymers are linked by reversible bonds into supramolecular copolymers or networks, a broad range of phase behaviors are possible including macrophase separation into homogeneous phases, microphase separation into ordered mesophases, and coexistence of homogeneous phases and mesophases. Thus, the field of *heterogeneous supramolecular polymers* offers even greater opportunities for self-assembling novel materials structures, and consequently achieving unique combinations of physical properties and thermal and processing behaviors.

In the simplest case of block copolymers assembled by reversible bonding of two dissimilar homopolymers with terminal functional groups, so-called “supramolecular diblocks”, a variety of mesophases can be produced by exploiting two physical processes with thermal controls. Specifically, a suitable bond strength creates the supramolecular copolymers, while the incompatibility between chemically dissimilar segments influences the assembly into inhomogeneous structures. The relative lengths and proportions of the homopolymers can be further adjusted to control the symmetry of a mesophase. As the bond strength and incompatibility can be independently varied by changing the chemical nature of the chains and the functional groups responsible for reversible bonding, a wide range of thermal behaviors can be achieved according to whether these energies fall above or below $k_{\text{B}}T$. Recently, the thermal control of the lamellar spacing in a supramolecular diblock copolymer system was investigated.¹ Similar inhomogeneous polymer assembly has been a topic for the thermal manipulation of the viscosity,² temperature-dependent conductivity,³ controlled drug delivery,⁴ and the development of new materials with novel thermo-, chemo-, or mechano-responses, and light-emitting properties.⁵

An early theory of systems with reversible bonding was developed by Tanaka, Matsuyama, and co-workers⁶,⁷ to describe solvation in aqueous polymer solutions. These systems can exhibit peculiar thermal behavior, including reentrant miscibility gaps provoked by the solvation. Their clustering theory was extended to supramolecular diblock and comblike copolymers,⁷,⁸ based on a Landau expansion of the free energy functional and the random phase approximation (RPA).⁹,¹⁰ Although this study was limited to an investigation of the stability of homogeneous phases, they found novel phase behavior, including a region of closed loop coexistence.

Later, in order to examine mesophase structure and stability for a model of supramolecular diblock copolymers, a mean-field analysis based on a higher-order application of the RPA was conducted by ten Brinke and co-workers.¹¹,¹² This model was developed in order to distinguish the stability regimes of different mesophases, but is quite laborious and is restricted to the weak segregation regime. Moreover, the treatment of bonding equilibrium was approximate because it utilized an equilibrium constant expressed in *concentrations* of reactants and products, rather than activities. Later, using the same approach, Hur and Jo¹³ extended the theory to a supramolecular

* Corresponding author. e-mail: ghf@mrl.ucsb.edu.
† Department of Chemical Engineering, University of California, Santa Barbara.
‡ Materials Research Laboratory, University of California, Santa Barbara.
§ Department of Materials, University of California, Santa Barbara.

10.1021/ma071714y CCC: $37.00
© 2007 American Chemical Society
Published on Web 10/23/2007

![](./images/811961987985571840_1.jpg)

Figure 1. Schematic diagram for the reversible bonding reactions in the supramolecular triblock blend.

polymer system that assembles into triblock copolymers, essentially the system we consider below.

Recently, a more complete theory of the supramolecular diblock blend has been developed,¹⁴ which exactly treats the chemical reaction equilibrium associated with bonding and makes no assumptions about the segregation strength. In this grand canonical approach, the population of supramolecular copolymers is not prescribed but is determined by constraints on the species activities (or chemical potentials) consistent with the bonding reaction equilibria. While the model and formalism transcends the mean-field approximation, phase diagrams were developed in the mean-field context using self-consistent field theory (SCFT).

In the following, we apply this new approach to study a model of a supramolecular triblock copolymer blend composed of two chemically distinct, but reactive, homopolymer species, as shown schematically in Figure 1. Reversible bonding occurs only between the chemically distinct homopolymers, one of which (species A) is monofunctional and the other (B) difunctional. As a consequence, the equilibrium system consists of a melt blend of A and B homopolymer "reactants", with two block copolymer "products": AB diblocks and ABA triblocks. The concentrations of the four species are controlled by the segmental incompatibility, the bonding strength, the homopolymer chain lengths, and the relative proportions of the homopolymer reactants.

This paper is divided into two sections. In the first, we discuss a standard field theory model for inhomogeneous polymer blends, adapting it to include chemical equilibria for reversible bonding and for the case of diblock and triblock products. We then solve the model within the framework of numerical self-consistent field theory. We examine a case of high bonding strength, which, when conditions permit, creates a large population of the copolymers in the melt. For these SCFT calculations, two cases of relative homopolymer lengths are considered, the first of which consists of two equal length reactive homopolymers, $N_{\text{Ah}} = N_{\text{Bh}}$, which form symmetric AB diblocks and asymmetric ABA triblocks. The additional subscript, "h", is added to emphasize that these quantities index the homopolymers in the blend. Next, we treat the case of $N_{\text{Bh}} = 2N_{\text{Ah}}$, which corresponds to symmetric triblocks and asymmetric diblocks as reaction products. The creation of these copolymers stabilize mesophases in some regions of the phase diagram while spurning others, a result that is a simple consequence of the architecture of the copolymers. We examine this phase behavior by monitoring the relative concentrations of diblocks, triblocks, and unreacted homopolymers.

Subsequent to the SCFT results is a section that addresses some general trends in phase behavior of the supramolecular triblock model by adapting a (grand canonical) random phase approximation analysis to this reacting system. This section focuses on three effects. First, using the $N_{\text{Ah}} = N_{\text{Bh}}$ model system at high bonding strength as a benchmark, we include an analysis of changing the homopolymer lengths continuously on the shape of the order-disorder envelope. Also, the stability boundaries that delineate regions of macrophase and microphase separation are computed for weaker bonding strengths using the same RPA analysis. Finally, we find reentrance at some weaker bonding strengths in this analysis and explore its physical origins.

## 2. The Model and Its Self-Consistent Field Solution for Strong Bonding

### 2.1. The Bonding Model for A Mono- and B Difunctional Polymers.
We consider an incompressible melt blend of two homopolymers, A and B, which respectively possess one and two functional (reactive) end groups. They are confined to a volume $V$ and are modeled as continuous Gaussian chains with polymerization indices $N_{\text{Ah}}$ and $N_{\text{Bh}}$. All dissimilar polymer segments interact with the usual Flory-Huggins local repulsion of strength $\chi$, and the incompressibility condition constrains the total density of segments to a constant value $\rho_0$ at each point in space. For nonreactive polymers, this type of blend, its corresponding field theory, and the mean-field approximation are well-documented in reviews¹⁵,¹⁶ and a recent monograph.¹⁷ Such nonreactive polymer blends are only capable of macrophase separation into coexisting homogeneous phases.

Although our supramolecular model is built upon the same chain and interaction model used to treat binary homopolymer blends, the reversible bonding at the chain ends leads to additional diblock and triblock copolymer species as depicted in Figure 1. The supramolecular blend thus contains a total of four species, two of which are composite (copolymeric) in nature. Superimposed on this four-component system is the constraint of incompressibility on the local volume fractions of A and B segments (contributed by the homopolymers and copolymers); namely, these total segment volume fractions $\phi_{\text{A}}$ and $\phi_{\text{B}}$ must sum to unity everywhere in the domain. It is convenient to formulate the model in the grand canonical ensemble, wherein control is exerted over the species chemical potentials $\mu_i$. In the binary blend, since incompressibility sustains the total monomer concentration, a single (excess) chemical potential is sufficient to control the relative concentrations of A and B polymers. The supramolecular blend includes two additional composite polymers, diblocks and triblocks, both of which have their concentrations constrained by the conditions for chemical reaction equilibria. With these additional two constraints (one for each reaction), the relative concentrations (or volume fractions) of all four species in the supramolecular blend are controlled by one chemical potential, $\mu_{\text{Ah}}$, which we arbitrarily choose to be that of the A homopolymer.

We employ the standard field-theoretic approach to convert a partition function sum over all segment configurations of the polymers to integrations over auxiliary density fields (volume fractions), $\phi_i$, and chemical potential fields, $W_i$. This particle-to-field transformation for the supramolecular triblock model largely follows the standard procedure. Here we forego most of the details, focusing instead on the relevant reaction

constraints. For reference, a field-theoretic model for the corresponding supramolecular diblock system was derived in explicit detail in a recent paper.¹⁴

In the field-theoretic representation, the grand canonical Hamiltonian for the supramolecular blend $H_{\mathrm{G}}$, scaled by a reference number of polymer chains, $\rho_{0} V / N$, can be written,
$$
f_{\mathrm{G}}=\beta \frac{N H_{\mathrm{G}}}{\rho_{0} V}=-\sum_{i} \xi_{i} z_{i} Q_{i}[W]-f[\phi, W, P] \quad(1)
$$
where $z_{i} \equiv z_{0} \exp \left(\beta \mu_{i}\right)$ and $Q_{i}$ are respectively the activities and single chain partition functions, each indexed by species: $i \in\{\mathrm{Ah}, \mathrm{Bh}, \mathrm{AB}, \mathrm{ABA}\}$. The quantity $\xi_{i}$ is a combinatorial factor that is 2 for the diblock species and 1 for the other three species. This accounts for the two ways an A homopolymer can bind to a difunctional B homopolymer to produce a diblock copolymer. The reference polymerization index $N$ employed is that of the largest species; the triblock, $N=2 N_{\mathrm{Ah}}+N_{\mathrm{Bh}}$. Finally, the functional $f[\phi, W, P]$ is given by
$$
\begin{aligned}
f[\phi, W, P]=-\frac{1}{V} \mathrm{~d} \mathbf{r}\left\{\chi N \phi_{\mathrm{A}} \phi_{\mathrm{B}}\right. & -W_{\mathrm{A}} \phi_{\mathrm{A}}-W_{\mathrm{B}} \phi_{\mathrm{B}}+ \\
& \left.P\left(\phi_{\mathrm{A}}+\phi_{\mathrm{B}}-1\right)\right\} \text { (2) }
\end{aligned}
$$

The pressure field, $P$, is a Lagrange multiplier that enforces the incompressibility constraint. As mentioned above, incompressibility also permits us to arbitrarily assign $z_{\mathrm{Bh}}=1$ and retain $z_{\mathrm{Ah}}$ as the single independent activity. The other two activities are determined from the mass-action laws for the chemical reactions,
$$
\frac{z_{\mathrm{AB}}}{z_{\mathrm{Ah}} z_{\mathrm{Bh}}}=\frac{z_{\mathrm{AB}}}{z_{\mathrm{Ah}}}=K_{\mathrm{eq}} / N=\mathrm{e}^{h-\ln N} \Rightarrow z_{\mathrm{AB}}=\frac{z_{\mathrm{Ah}} \mathrm{e}^{h}}{N} \quad(3)
$$

$$
\frac{z_{\mathrm{ABA}}}{z_{\mathrm{AB}} z_{\mathrm{Ah}}}=K_{\mathrm{eq}} / N=\mathrm{e}^{h-\ln N} \Rightarrow z_{\mathrm{ABA}}=\frac{z_{\mathrm{Ah}}^{2} \mathrm{e}^{2 h}}{N^{2}} \quad(4)
$$
where the free energy decrease for bonding in units of the thermal energy, $k_{\mathrm{B}} T$, is denoted by $h$, and $K_{e q}=\exp (h)$ is an equilibrium constant. A notable aspect of these relations is that the bonding affinity, $h$, is effectively decreased by the chain length $N, h_{\text {eff }}=h-\ln N$. At the same bond strength $h$, longer chains have proportionately fewer functional end groups and thus a lesser propensity to link and form complexes. As a consequence, the polymerization index $N$ appears as an independent parameter in theories of supramolecular polymer assembly.¹⁴ Finally, eqs 3 and 4 show that there is a single independent activity, $z_{\mathrm{Ah}}$, that determines all concentrations due to the reaction and incompressibility constraints.

Self-consistent field theory (SCFT) is the limiting theory obtained when the Hamiltonian in eq 1 is extremized with respect to its densities and fields, $\{\phi, W, P\}$. This "mean-field" approximation assumes that the partition function is dominated by a single field configuration $\left\{\phi_{\mathrm{A}}^{*}, \phi_{\mathrm{B}}^{*}, W_{\mathrm{A}}^{*}, W_{\mathrm{B}}^{*}, P^{*}\right\}$, and fluctuations around this configuration are neglected. We shall restrict our analysis to a SCFT treatment, although the supramolecular model can in principle be examined by full "field-theoretic simulations" that do not invoke the mean-field approximation.¹⁷,¹⁸

In the SCFT approximation, a simple thermodynamic correspondence is established between the optimized Hamiltonian and the osmotic pressure, $\Pi$, via
$$
\pi \equiv \beta N \Pi / \rho_{0}=-f_{\mathrm{G}}\left[\phi_{\mathrm{A}}^{*}, \phi_{\mathrm{B}}^{*}, W_{\mathrm{A}}^{*}, W_{\mathrm{B}}^{*}, P^{*}\right] \quad(5)
$$

This function is examined for stability with prescribed structural symmetries and against phase separation in the four-parameter space of $z_{\mathrm{Ah}}, h, N, N_{\mathrm{Ah}} / N_{\mathrm{Bh}}$. In the case of spatially periodic mesophases, the SCFT equations are solved in a unit cell and the energy per chain $f_{\mathrm{G}}$ in eq 5 is minimized with regard to the size and shape of the cell by a variable cell shape method.¹⁷,¹⁹ Further details of the grand canonical SCFT equations, including expressions for the single chain partition functions and volume fraction operators, are given in Appendix A. The variable cell shape method is briefly summarized in Appendix B.

2.2. SCFT Results for High Bonding Strength. To investigate the influence of the copolymer architecture in the supramolecular blend, as dictated by the ratio of reactive homopolymer lengths $N_{\mathrm{Ah}} / N_{\mathrm{Bh}}$, we consider a relatively high bonding strength, and examine two cases of homopolymer lengths. The first case corresponds to asymmetric diblocks and symmetric triblocks, complexed from homopolymers of unequal lengths, $N_{\mathrm{Bh}}=2 N_{\mathrm{Ah}}$, which we parametrize by $\alpha_{\mathrm{Ah}} \equiv N_{\mathrm{Ah}} / N=$ $1 / 4$. The second case involves homopolymers with equal lengths $N_{\mathrm{Ah}}=N_{\mathrm{Bh}}\left(\alpha_{\mathrm{Ah}}=1 / 3\right)$, thus creating the opposite situation of symmetric diblocks and asymmetric triblocks.

The computational effort to map out complete SCFT phase diagrams for the two systems investigated is very extensive since the free energies of all possible competing phases must be tracked throughout a high dimensional parameter space. To minimize the computational cost in the following, yet retain a representative free energy competition between mesophases and macrophases, we have restricted our calculations to one and two-dimensional mesophase structures. Thus, cubic structures, such as the $Im 3 m$, $Ia 3 d$, and $Pn 3 m$ phases, have not been considered. Our experience with simpler reactive polymer models such as the supramolecular diblock,¹⁴ as well as with permanently bonded block copolymers and their alloys,²⁰ suggests that the cubic phases will intervene in the compositional extremes of the SCFT phase diagrams, but the qualitative features of the order-disorder boundary and the macrophase-mesophase competition will be unaffected.

2.2.1. Asymmetric Diblocks and Symmetric Triblocks as Reaction Products. Figure 2a shows the mean-field temperature-composition phase diagram for the case of $\alpha_{\mathrm{Ah}}=1 / 4\left(N_{\mathrm{Bh}}\right.$ $=2 N_{\mathrm{Ah}}$ ), $N=300$, and the "strong bonding" condition of $h / \chi N$ $=0.627086$. The composition axis is the total volume fraction of A-segments in the system, originating from all polymers in the blend,
$$
\phi_{\mathrm{A}, \mathrm{tot}}=\phi_{\mathrm{Ah}}+\frac{\alpha_{\mathrm{Ah}}}{\alpha_{\mathrm{AB}}} \phi_{\mathrm{AB}}+2 \alpha_{\mathrm{Ah}} \phi_{\mathrm{ABA}} \quad(6)
$$
with $\alpha_{i}=N_{i} / N$ and all polymer lengths scaled by the triblock polymerization, $N=N_{\mathrm{ABA}}$. We observe that a homogeneous disordered phase (Dis) competes with three mesophases, the lamellar $(Lam)$, hexagonally packed cylinder $(Hex)$, and inverted hexagonally packed cylinder $\left(\mathrm{Hex}_{I I}\right)$ phases, throughout the $1 / \chi N-\phi_{\mathrm{A}, \text { tot }}$ (temperature-composition) plane. Two-phase coexistence is explicitly labeled for the broadest regions, and otherwise indicated by two adjacent, sometimes overlapping, lines between the labeled phases. Each of these two-phase regions terminate at low $\chi N$ (high "temperature") with triple points. In addition to the mean-field phase diagram in Figure 2a, a spinodal curve is also drawn, indicating the stability limit of the Dis phase. The spinodal is found to be interior or nearly co-incident with the melting (order-disorder) envelope, and will be discussed in more detail in a later section.

The most salient feature of this phase diagram is that the order-disorder boundary has two lobes. The interior of each

![](./images/811961987985571840_2.jpg)

Figure 2. Mean field phase diagrams in the coordinates of $1/\chi N$ vs the total volume fraction of A segments. The top figure (a) is for the case of $\alpha_{\text{Ah}}=1/4$, where symmetric triblocks and asymmetric diblocks are reaction products. The figure (b) below corresponds to $\alpha_{\text{Ah}}=1/3$, which has symmetric diblocks and asymmetric triblocks as reaction products. The length of the triblock is $N=300$ and the bond strength is $h/\chi N=0.627086$ in both diagrams. Labeled phases are $Dis$ for the A- or B-rich disordered homogeneous phases, $Hex_{\text{II}}$ for the inverted hexagonal phase, $Lam$ for the lamellar phase, and $Hex$ for the hexagonal phase. Two of the coexistence regions are labeled as $2\phi$.

lobe is dominated by a large stability region of the hexagonal or inverted hexagonal phase and these envelopes are separated by a low melting "eutectic" point which has been observed in different polymeric systems. $^{8,21}$ This point is located in the lamellar phase at roughly $\phi_{\text{A,tot}}=1/2$, which corresponds to a concentration co-incident with the stoichiometry of the triblock, and we may expect that the symmetric triblock, which favors the lamellar phase, is most present at concentrations near this architectural symmetry. The second stoichiometric composition corresponds to that of the diblock, at $\phi_{\text{A,tot}}=1/3$, which roughly corresponds with the apex of the lower concentration lobe. The asymmetric diblock also favors the curved interfaces of the inverted hexagonal phase, which dominates this low concentration envelope. Thus, a superficial explanation of the phase sequence is the following: the low (A) concentration lobe is associated with a high diblock density; there is not enough A-homopolymer to satisfy all bonds and diblock-preferred phases are formed. The second higher concentration lobe corresponds to the influence of triblocks, as all bonds are satisfied at these larger A-concentrations.

The packing of asymmetric diblock copolymers in a "solvent" of B homopolymers, while minimizing the dissimilar segment contacts, can be used to explain the phase sequence and melting trends of the low concentration lobe. Figure 3a shows the concentrations of the constituent polymers as a function of the total A-segment concentration at the inverse temperature $\chi N=18$. At low A-segment volume fractions, the system consists of nearly all unbonded B homopolymers due to the dearth of A's to satisfy the bonds. Upon increasing the number of A-homopolymers, both the diblock and triblock volume fractions grow, with the diblock concentration at nearly twice the rate. When there are enough diblocks in the blend, but not a substantial concentration of triblocks, the structure of the melt is controlled by the diblock species, whose asymmetry $N_{\text{Bh}}=2N_{\text{Ah}}$ prefers the inverted hexagonal phase that occupies a substantial portion of the low A-concentration lobe.

![](./images/811961987985571840_3.jpg)

Figure 3. Volume fractions of the four constituent polymers as a function of the total A-segment volume fraction for the supramolecular blends corresponding to Figure 2, parts a and b. The species are labeled in the legends. Diagram a depicts the species concentrations at $\chi N=18$ for the system shown in Figure 2a. Diagram b displays the species concentrations for a cut at $\chi N=19$ in Figure 2b. All other parameters and notations are the same as in Figure 2.

By increasing the A-concentration in the melt, more symmetric triblocks are formed from the diblocks, causing the population of diblocks to decrease. The inverted hexagonal phase now accepts a modest population of triblocks until they induce a transition to their preferred lamellar phase near the eutectic point at $\phi_{\text{A,tot}}\approx1/2$, and between the lobes. This portion of the diagram has the lowest melting point and the greatest triblock density. Beyond this concentration, the B-block sheets of the lamellae are separated by the A triblock tails mixed with A-homopolymer solvent; the latter swelling the lamellar structure until it reaches a stability threshold causing a transition to the hexagonal phase. Eventually the Hex phase melts into disorder via a two-phase region at large A-concentration.

The melting trend for the second "triblock" (high A-concentration) lobe can be understood as follows. A pure symmetric ABA-triblock melt has an order-disorder transition at roughly $\chi N\approx18$ ($1/\chi N\approx0.556$),$^{22}$ which is somewhat interior to the eutectic in Figure 2a at $\phi_{\text{A,tot}}\approx0.50$. We find that this middle region is comprised of greater than 90% triblock by volume (cf. Figure 3a), and melts to uniform disorder at a slightly higher $\chi N$. From this midpoint, within the stable lamellar phase, adding more A-homopolymers to the mostly triblock melt

swells the lamellar structure. This swelling often causes the order−disorder boundary to drift up to higher temperatures (lower $\chi N$), as it does in swelling an AB diblock lamellae with a shorter, A-block compatible homopolymer.²⁰ Eventually, with increasing the concentration of solvent homopolymer, the lamellar structure can no longer be sustained, and the interfaces curve into the hexagonal phase, which is stable at the highest temperatures. This eventually melts into the pure disordered state at high A-segment concentrations.

### 2.2.2. Symmetric Diblocks and Asymmetric Triblocks as Reaction Products.
This section considers the association of A and B homopolymers with equal lengths, $N_{\text{Ah}} = N_{\text{Bh}}$, which form symmetric AB diblocks and asymmetric triblocks ($\alpha_{\text{Ah}} =$ ¹/₃). The mean-field phase diagram for this case is shown in Figure 2b. The coexistence regions are indicated as before and the spinodal is also drawn for this architecture, to be discussed further in a section below. Structural swelling of the $Hex_{II}$ and Lam phases at low total A-concentration requires calculationally prohibitive resolutions and a portion of the phase boundaries in Figure 2 is determined by extrapolation, which is indicated by the dotted line. Remarkably, this diagram has a larger low A-concentration “diblock” lobe, and the second “triblock” lobe is present as a shoulder to the primary envelope. As before, both hexagonal phases are present on either side of a centrally located lamellar phase.

Proceeding from low to high total A-concentrations, Figure 3b indicates a similar trend to the previous case of $\alpha_{\text{Ah}} =$ ¹/₄ but with different growth rates for the reaction products. The diblock concentration is maximal near its stoichiometric symmetry point, $\phi_{\text{A,tot}} \approx$ ¹/₂, having increased more gradually than the previous asymmetric case. Similarly, the triblock peak concentration is close to its point of stoichiometric symmetry, at $\phi_{\text{A,tot}} =$ ²/₃, co-incident with the notch between the lobes, as before.

More remarkable in this case is the melting trend, which indicates that the phases most stable at high temperatures are associated with diblocks rather than triblocks. Previously, the mostly triblock lamellar phase was swollen with the addition of A-homopolymer in Figure 3a, which then stabilized the hexagonal phase at high temperatures in the greater A-concentration lobe. Here, the diblock is symmetric, and has a peak density at $\phi_{\text{AB}} \approx$ ¹/₂, which forms the lamellar phase inside the low A-concentration lobe, in the presence of modest amounts of asymmetric triblocks, $\phi_{\text{ABA}} \approx$ ¹/₄, and B-homopolymers, $\phi_{\text{Bh}} \approx$ ¹/₄. These lamellae are stable as the A-content of the system is decreased, which depletes the amount of triblocks and, at nearly twice the rate, increases the amount of B-homopolymer. The excess B-content induces the inverted hexagonal phase, and this phase is stable at the highest temperatures.

The diblock lamellae here swell with increased B-concentration similar to how the triblock lamellae in the previous case were swollen by increasing the A-concentration. In the $\alpha_{\text{Ah}} =$ ¹/₄ case, a short A-homopolymer, one-quarter of the triblock length, swelled the triblock lamellae. Here, the diblock lamellae are swollen with a short B-homopolymer of half the diblock length ($N_{\text{Bh}} = N_{\text{AB}}/2$). The nature of the “solvent” homopolymer has reversed, due to the architectural differences of the constituents.

To reiterate, the phase diagrams of Figure 2 show that for a set value of bonding strength, there is a remarkable sensitivity of the phase diagram of supramolecular polymers to the relative molecular weights of the two homopolymers being linked. Indeed, the molecular weight ratio influences the architecture of the block copolymer reaction products, and these architectural variations can have a large effect on the relative stability of competing mesophases. We have also seen interesting features in the order−disorder boundary, such as eutectics and stable compounds, which are familiar in metallurgy but are rather unusual in conventional polymer alloys.

## 3. Stability Analysis of the Reversibly Bonding Melt with the Random Phase Approximation
In the present section, we employ the random phase approximation (RPA) method to investigate some general features of the order−disorder envelope of supramolecular systems. Here, the RPA is employed as a simple tool for a stability analysis of the homogeneous blend (Dis phase), focusing only on trends in the spinodal. It will be used to elucidate the effects of copolymer architecture, as seen above in the full SCFT calculation, and the influence of bonding strength in this system.

The RPA method is one which utilizes an expansion of the free energy functional for an inhomogeneous system around a reference state, typically a corresponding homogeneous fluid, and is best suited for cases when the state of interest is not a considerable perturbation of the fluid state, i.e., generally for weaker segregations. At quadratic order, the coefficient in the free energy expansion is the inverse structure factor, $S^{-1}(q)$, whose minima are inspected for zeros (divergences of the scattering function $S(q) \to \infty$) that indicate an instability of the system. This threshold can occur at a finite characteristic wavenumber, $q^{*}$, signaling the onset of a periodic mesophase with periodicity, $\xi \approx 2\pi/q^{*}$.

At the heart of the RPA method, and that which encompasses its microscopic (and hence polymeric) character, is the inclusion of a molecular chain model for the individual polymer threads. The structure factor is determined by means of calculating the pair correlation functions for ideal chains, typically with a Gaussian chain model.⁹,¹⁰ Thus, the structural response of the fluid to a perturbation at roughly a distance $\xi$ away is contained in the microscopic character of the fluid, and approximated by the nonlocal character of dense, yet independent Gaussian chains. The RPA method is easily adapted for copolymers and polymer blends, for example in homopolymer/diblock ternary mixtures.²³

As a consequence of incompressibility, the free energy functional may be expanded about the homogeneous phase in terms of the total A (or B) density, $\phi_{\text{A,tot}}$, as a single order parameter. This expansion yields at quadratic order the inverse structure factor,

$$
\begin{aligned}
S(q)^{-1} &\equiv \frac{F(q)}{N} - 2\chi \\
&= \frac{S_{\text{AA}}(q) + 2S_{\text{AB}}(q) + S_{\text{BB}}(q)}{S_{\text{AA}}(q)S_{\text{BB}}(q) - S_{\text{AB}}^{2}(q)} - 2\chi
\end{aligned} \tag{7}
$$

where $S_{ij}$ is the density−density pair correlation function of Gaussian chains originating from all chains in the melt with block types $i$ and $j$, and $q$ is the scattering wavenumber. These correlation functions are linear combinations of the various chain contributions, weighted by their volume content in the blend.²⁴ They are listed in Appendix C.

The functional expansion in the density is carried out with the homogeneous fluid as a reference state, which requires a connection between the (total) A-segment concentration and the chemical potentials used in the grand canonical ensemble SCFT calculation described above. For the present RPA calculation, there is a single independent concentration that is analogous to

![](./images/811961987985571840_4.jpg)

Figure 4. Comparison of several RPA spinodals for varying architectures $\alpha_{\mathrm{Ah}}$. The spinodal with $\alpha_{\mathrm{Ah}}=0.333$ corresponds to the case in Figure $2 b$ which forms symmetric diblocks and asymmetric triblocks in the melt. Changing this architecture by decreasing $\alpha_{\mathrm{Ah}}$ diminishes the low A-concentration lobe that is populated by diblock-rich mesophases, and augments the high A-concentration lobe associated with triblock-rich mesophases. The spinodal for $\alpha_{\mathrm{Ah}}=0.25$ corresponds to the blend in Figure 2a which forms symmetric triblocks and asymmetric diblocks. Between these architectures, there is an unusual point of symmetry in the spinodal where these lobes are roughly equal in breadth, at $\alpha_{\mathrm{Ah}}=0.2660$.

the one A-homopolymer activity, $z_{\mathrm{Ah}}$, used previously. This activity-concentration correspondence is only needed for the reference fluid phase, and is discussed, along with other details of this calculation, in Appendix C.

### 3.1. Architectural Effects of the Copolymers in the Melt, Revisited.
The phase diagrams of parts a and b of Figure 2 show the shifting influence of the diblock and triblock reaction products for two block lengths of the copolymers. Within each SCFT ordered phase envelope, there is a calculated RPA spinodal that, for some regions of the phase diagram, is nearly co-incident with the melting envelope. It departs from the order-disorder boundary most significantly at high segregation and for the weak first-order transitions in these systems. Most remarkably, the RPA spinodal captures the double-lobed structure of the phase boundary.

Figure 4 compares spinodals for several architectures, indicating that the lobe structure and breadth may be adjusted with the architecture of the copolymers. We begin with the architecture of Figure $2 b$, that of homopolymers with equal lengths, $N_{\mathrm{Bh}}=N_{\mathrm{Ah}}\left(\alpha_{\mathrm{Ah}}=1 / 3\right)$, which creates symmetric diblocks under the appropriate conditions. The melting curve for this blend has a prominent low A-concentration lobe containing phases associated with the symmetric diblock, and is displayed in the figure along with the RPA spinodal as a dotted line. This spinodal is reproduced in Figure 4, along with several others for the same blend but with varying copolymer architectures. By increasing the relative length of the B- homopolymers, which shortens the end blocks of the triblocks, the secondary high A-concentration lobe is amplified while the A-depleted lobe is diminished. Increasing this ratio further to that of homopolymers with lengths $N_{\mathrm{Bh}}=2 N_{\mathrm{Ah}}\left(\alpha_{\mathrm{Ah}}=1 / 4\right), c f$. Figure $2 a$, the second lobe populated with structures formed from symmetric triblocks, is more prominent than the low A-concentration one. Remarkably, in this process, a symmetry point is passed with an unusual ratio of homopolymer lengths at $N_{\mathrm{Bh}} \approx 1.76 N_{\mathrm{Ah}}$, or $\alpha_{\mathrm{Ah}} \approx 0.2660$, where the two spinodal lobes are roughly identical.

### 3.2. Effects of Bonding Strength on the Blend.
One utility of the stability analysis with the RPA is that its numerical demands are naturally far less than those of the SCFT calculations. As a consequence, the RPA method at quadratic order also supplies much less information about the system, indicating only the onset of mesophases and not their structure or symmetry. Further expansion of the free energy functional enables an investigation of the competing inhomogeneous phases, but analysis at this higher level is extremely laborious and still much more limited in information content than full SCFT simulations. Thus, we prefer to rely on quadratic-level RPA to assess gross phase diagram topology and then fill in details in regions of particular interest with SCFT.

In the previous sections, we focused on the architectural effects of supramolecular polymer assembly, all calculated at a high, constant bonding strength of $(h / \chi N)^{*}=0.627086$. We note that since $h$ and $\chi$ are both energies referenced to the thermal energy $k_{\mathrm{B}} T$, this ratio should be approximately temperature independent assuming that entropic contributions to bonding and segmental interactions can be neglected. Because the RPA spinodal reliably reproduced the melting trends in the strong bonding case, we have some confidence to apply it more broadly. In this section, we shall consider the effects of lower bonding strengths on the supramolecular triblock system, which includes situations where unbound homopolymers play the predominant role in controlling phase behavior.

At very low bonding strength, $h \rightarrow-\infty$, the blend consists of unbound A and B homopolymers that phase separate for temperatures below the usual critical point, which in our units is $T^{c} \equiv 1 / \chi N^{c}=2 \alpha_{\mathrm{Ah}}\left(\phi_{\mathrm{A}, \mathrm{tot}}^{\mathrm{c}}\right)^{2}$, at $\phi_{\mathrm{A}, \mathrm{tot}}^{\mathrm{c}}=\sqrt{\alpha_{\mathrm{Bh}}} /(\sqrt{\alpha_{\mathrm{Ah}}}+$ $\sqrt{\alpha_{\mathrm{Bh}}}$ ), and the binodal and spinodal both fall away quadratically in the temperature-composition plane from this point. If the homopolymers are asymmetric, e.g., $N_{\mathrm{Bh}}=2 N_{\mathrm{Ah}}$, the shape of the binodal/melting curve must change significantly as the bonding strength is increased, to arrive finally at the double-lobed structure of Figure 2a. We investigate below this evolution primarily for the particular architecture $\alpha_{\mathrm{Ah}}=1 / 4\left(N_{\mathrm{Bh}}\right.$ $\left.=2 N_{\mathrm{Ah}}\right)$.

Figure 5 shows the evolution of the spinodal with the normalized bonding strength $h / \chi N$ for the $\alpha_{\mathrm{Ah}}=1 / 4$ blend. The low bonding strength behavior $(h / \chi N=0)$ is as expected, nearly that of two incompatible homopolymers with a parabolic immiscible region below the critical point. The high bonding strength behavior is the familiar double-lobed spinodal of Figure 2a.

More remarkable is the intermediate region, which shows the evolution of the envelope. Figure 6 shows all of the spinodals of Figure 5 in the temperature-composition plane. A slight increase in the bonding strength causes the parabolic two-fluid region to contract into an hourglass shape, bounded above by a liquid-liquid critical point. Stronger bonding recedes the hourglass shape to a closed loop structure, bounded above and below by critical points. Below the closed loop, there is a low- temperature mesophase region. Further increasing the bonding strength causes the closed loop to diminish and disappear, while the low-temperature region develops the two-lobe structure of Figure 2a. An interesting observation is that the asymmetry of the double-lobed structure is somewhat co-incident with the asymmetry of the critical point of the unbonded system; the more prominent A-concentration lobe at high bonding is co- incident with the liquid-liquid critical line also richer in A. Finally, it is worth noting that re-entrant homogeneous phases have been predicted in other supramolecular systems, $^{8,12,14}$ and

![](./images/811961987985571840_5.jpg)

Figure 5. RPA spinodal surface for the bonding supramolecular system with $N_{\mathrm{Bh}}=2 N_{\mathrm{Ah}}$. The individual cross sections indicate different bonding strengths specified by $h / \chi N$. The line along the top of the surface is the homogeneous critical line which terminates at a Lifshitz point denoted LS. The critical line continues beyond this point but is not indicated here. At low bonding strength, the envelope is a binodal that encloses a region of coexistence between homogeneous phases rich in the two homopolymers. The envelope is parabolic in shape near the critical point at $\chi N^{-1}=0.171573$ and $\phi_{\mathrm{A}, \mathrm{tot}}$ $=0.58579$. The cross section drawn at the highest bonding of $h / \chi N=$ $0.627086$ is the double-lobed order-disorder spinodal of Figure 2a. Between these two limiting behaviors, there is a reentrant region of two-fluid, closed loop phase coexistence in the neighborhood of the Lifshitz point.

![](./images/811961987985571840_6.jpg)

Figure 6. Spinodal cross sections from Figure 5 drawn in the temperature-composition plane. At low bonding, the spinodal has the parabolic shape of an incompatible, two homopolymer blend. As the strength of bonding increases, the two-phase envelope retracts at low and high compositions and forms a two-fluid closed loop above a low temperature order-disorder profile. Increasing the bonding strength further causes the closed loop to diminish and eventually disappear. Subsequently, the double-lobed structure at lower temperatures becomes more distinct. The high bonding strength spinodal at $h / \chi N=0.627086$ corresponds to that of Figure 2a. Critical points for the homogeneous phases are indicated with filled black circles $(\bullet)$, and the Lifshitz point, LS, is labeled.

is generally understood in reacting mixtures of simple liquids. $^{25,26}$

A variety of blends of homopolymers with permanently bonded block copolymers are known to exhibit regions in the phase diagram where mesophases, preferred by the copolymers, compete with macrophases that are preferred by the homopolymers. A stability analysis with the RPA method is robust and well suited for identifying these regions and the threshold for stable periodic structures. The onset of mesophases, when coincident with a liquid-liquid critical point, is a special type of tricritical point known as an isotropic Lifshitz point (LS). Finding such a point at the mean-field level is a straightforward calculation, although in real systems Lifshitz points are typically destroyed by thermal fluctuations, leaving a pocket of microemulsion in small region surrounding the location of the mean-field LS. $^{27}$ The RPA method is particularly suited for the mean-field calculation of Lifshitz points, and for both architectures Lifshitz parameters and compositions are listed in Table 1. For all points along the critical line at lower bonding, $(h / \chi N)<(h / \chi N)^{\mathrm{LS}}$, there is simple liquid-liquid critical behavior. Beyond mean-field theory, this line would be associated with exponents in the Ising universality class. Larger bonding strengths than $(h / \chi N)^{\mathrm{LS}}$ lead to mesophase critical points (only in mean-field theory) that are not indicated in the figures.

Before leaving this section, we remark on the sequence of phases in the vicinity of the Lifshitz point, for bond strengths $h / \chi N \approx 0.488605$, and the architectural parameters as above. Starting in the two phase region, at roughly the critical A/B composition, two homogeneous fluid phases divide the volume. Upon decreasing the temperature of this mixture below the Lifshitz point, in the context of the mean-field approximation, these fluids coalesce into a single liquid. At yet lower temperatures, mesophases appear and assemble from the homogeneous fluid. The phase sequence for cooling is thus: 1-fluid, 2-fluid, 1-fluid, mesophases. In a real system, if such a bond strength could be prescribed, fluctuations will likely alter the phase sequence to: 1-fluid, 2-fluid, microemulsion, mesophases. This is a thermotropic sequence in our supramolecular model blend that is analogous to the lyotropic sequence observed in two-homopolymer/diblock copolymer mixtures. $^{27,28}$ At the Lifshitz bond strength, the temperatureregulated bonding tunes the concentrations of the (co)polymers in way that mimics the composition control in a homopolymer/copolymer lyotropic blend. Of course, variation of the bonding strength parameter $h / \chi N$ through the Lifshitz point region of the supramolecular system will also mimic the corresponding lyotropic sequence in fixed-bonded alloys. Finally, there is also a strong likelihood of thermally re-entrant microphases in the Lifshitz region of the supramolecular triblock model. Such behavior was found in the supramolecular diblock system, $^{14}$ although the analysis of this region is beyond the scope of the RPA.

### 4. Summary and Discussion

In the present paper, we constructed a mesoscopic field-based model of the supramolecular assembly of a melt blend of monofunctional A and difunctional B homopolymers. The model assumes that only hetero-complementary, reversible bonding is possible between the functional groups on the A and B polymers, so that only two reaction products are possible: AB diblock copolymers and ABA triblocks. We applied two theoretical approaches to analyze the phase behavior of the model (both at the mean-field level): numerical SCFT simulations at high bonding strengths, and RPA calculations over a broader range of bonding strengths. These theoretical results suggest a rich variety of phase behaviors for such "supramolecular triblock" blends. In particular, the bonding strength has a dramatic effect on the concentrations and type of copolymers in the system, which in turn controls the extent and variety of mesophases in the blend. Weak bonds produce a small population of copolymers so that the thermal behavior of the system is dominated by the two homopolymers. At medium bond strengths, there is a competition between the influence of the copolymers and homopolymers, resulting in a Lifshitz point and a region of re-

<table>
<thead>
<tr><th>$\alpha_{\text{Ah}}$</th><th>$z_{\text{Ah}}$</th><th>$h/\chi N$</th><th>$\chi N$</th><th>$\phi_{\text{Ah}}$</th><th>$\phi_{\text{Bh}}$</th><th>$\phi_{\text{AB}}$</th><th>$\phi_{\text{ABA}}$</th></tr>
</thead>
<tbody>
<tr><td>$^1/_4$</td><td>2.00681</td><td>0.488605</td><td>9.33009</td><td>0.45379</td><td>0.16065</td><td>0.27837</td><td>0.10719</td></tr>
<tr><td>$^1/_3$</td><td>0.91727</td><td>0.472199</td><td>9.79553</td><td>0.21950</td><td>0.38139</td><td>0.34171</td><td>0.05740</td></tr>
</tbody>
</table>

entrant two-fluid phase coexistence. High bonding strengths produce high concentrations of copolymers, and of a type consistent with the stoichiometry of the mixture, which assemble into mesophases. A particularly interesting feature at high bond strength is the two-lobed structure of the order−disorder boundary, a consequence of the competing influence of the two reaction products, the diblock and triblock copolymers. The phase envelope in this case possesses a low melting temperature “eutectic”—a metallurgical feature not typically found in polymer alloys.

Two primary effects were investigated in this paper as they relate to the phase behavior of the supramolecular triblock system: (i) architectural variations in the copolymers caused by unequal A and B homopolymer lengths parametrized by $\alpha_{\text{Ah}}$; (ii) the influence of the bond strength $h$ relative to the A−B block interaction strength $\chi N$. We summarize these findings below and, in passing, mention a third in the ensuing discussion: the influence of the chain length, $N$. Each of these three factors have different repercussions on the phase diagram:

•The bonding strength changes the phase diagram strikingly. It determines the relative populations of homo- polymers and copolymers, which in turn determines the presence or absence of mesophases and liquid−liquid phase behavior. Low bonding yields simple liquid−liquid immiscibility and high bonding produces an unusual double-lobed liquidus line with each portion associated with a different reaction product. The two-phase envelope at low bonding strength evolves, at intermediate bonding energies, into a high-temperature (homogeneous phase) closed loop and a low-temperature structure populated with mesophases. The latter structure continuously evolves into the double lobes at high bonding strength.

•At bonding strengths that readily form both diblock and triblock copolymers, the phase behavior is contingent on the populations of the copolymers whose architectures determine the mesophases. For symmetric triblock and asymmetric diblock copolymer reaction products, a two-lobed phase diagram results. A low A-concentration lobe is co-incident with high diblock concentrations, which prefer an inverted hexagonal symmetry. A second, high A-concentration lobe was the result of a large triblock concentration swollen with excess A-homopolymers. These macroscopic lobes can thus be associated with the stable “compounds” produced by the reaction, namely diblocks and triblocks respectively, whose prominence in the phase diagram can be tuned architecturally with the relative lengths of the functional homopolymers. A second case considered, with symmetric diblocks and asymmetric triblocks as reaction products, brings about a prominent low concentration “diblock” lobe mostly populated with symmetric diblocks forming lamellae. More generally, we find that the relative size and location of the two lobes in the order−disorder envelope can be continuously tuned by varying a single parameter $\alpha_{\text{Ah}}$, which reflects the relative lengths of the two reactive homopolymers.

•The absolute, as opposed to relative, lengths of the polymers also changes the phase morphology. Although it was not explicitly shown above, the total length $N$ (here referenced to the triblock length) influences the bonding affinity, decreasing it to an effective strength, $h_{\text{eff}} = h - \log N$ (cf. eqs 3 and 4). A system composed of longer chains with the same fixed bond strength of $h/\chi N$ will not form the same amounts of copolymer, and may not exhibit the same phase morphology as the shorter chain. The longer chain lengths require a greater bonding strength to overcome the diminishing concentration of functional end groups. Thus, at moderate incompatibilities, it is readily seen that longer chain lengths effectively preserve the unbonded system—that of a binary homopolymer mixture—to greater values of $h/\chi N$. This is the origin of the closed-loop coexistence region. The two-fluid phase coexistence region characteristic of the unbonded homopolymers is shifted by an increase in $N$ from the low bonding region into the re-entrant “nose” feature above the Lifshitz point. Longer polymer chains accentuate and extend this re-entrant region. Reference 14 more explicitly demonstrates the effect of polymer length for the supramolecular diblock model.

In short, the gross features of the order−disorder boundaries and two-phase envelopes are controlled largely by the normalized bond strength $h/\chi N$, which yields topologies such as those of Figure 5. The relative lengths of the homopolymers govern the copolymer architecture, and emphasize or diminish the lobes in the order−disorder boundary at high bonding. Finally, the closed loop re-entrance behavior is accentuated with longer polymers.

We are eager to explore the implications of this work for experiment. In particular, a recent investigation of the thermal control of the lamellar spacing in the triblock supramolecular system¹ demonstrates some of the unusual nature and perhaps utility of such systems. Furthermore, the SCFT framework presented here outlines a calculational method that robustly and flexibly predicts thermal and structural behavior for supramolecular systems. Variations of the model that account for different placement of the reactive groups, or that include homo-complementary binding in addition to hetero- binding, are easily developed and treated. Less straightforward theoretically and computationally are full telechelic systems that react to form linear chains and rings of varying length. Most difficult are heterogeneous supramolecular systems that form networks with closed cycles. We hope to report on studies of these more challenging types of systems in the near future.

One potential difficulty and shortcoming of our model is that it assumes the reactive functional groups are comparable in size to the polymer segments, and that the groups do not interact strongly other than with their specific binding partners. In contrast, there is evidence of strong secondary associations among bonding groups in some supramolecular polymer systems, which can cause changes in morphology and thermal behavior,²⁹ and even lead to crystallization.³⁰,³¹ Finally, we emphasize that the SCFT and RPA techniques applied here are based on the mean-field approximation and neglect thermal fluctuations. Thus, features in the phase diagrams that are known to be susceptible to fluctuation effects, such as Lifshitz points (which give way to microemulsions), should be viewed with some skepticism. Fortunately, more advanced

"field-theoretic simulation" techniques are available for relaxing the mean-field approximation,¹⁷,¹⁸ although these computationally demanding methods have not yet been applied to supramolecular polymer models.

Acknowledgment. This work was supported by the MRSEC Program of the National Science Foundation under Award No. DMR05-20415 and by funding provided to the Complex Fluids Design Consortium at UCSB by the Dow Chemical Company and Nestle Research Center.

### Appendix
#### A. Self-Consistent Field Theory for Bonding Polymer Systems.
Applying the equilibrium constraints of eqs 3 and 4, the effective Hamiltonian for this polymer model is

$$
\begin{aligned}
f_{\mathrm{G}}= & -z_{\mathrm{Ah}} Q_{\mathrm{Ah}}-Q_{\mathrm{Bh}}-2 z_{\mathrm{Ah}} \frac{\mathrm{e}^{h}}{N} Q_{\mathrm{AB}}-z_{\mathrm{Ah}} \frac{2 \mathrm{e}^{2 h}}{N^{2}} Q_{\mathrm{ABA}}+ \\
& \frac{1}{V} \int \mathrm{d} \mathbf{r}\left\{\chi N \phi_{\mathrm{A}} \phi_{\mathrm{B}}-W_{\mathrm{A}} \phi_{\mathrm{A}}-W_{\mathrm{B}} \phi_{\mathrm{B}}+P\left(\phi_{\mathrm{A}}+\phi_{\mathrm{B}}-1\right)\right\} \quad(8)
\end{aligned}
$$

where, as mentioned before, the $W_{i}$ and $\phi_{i}$ are chemical potential and density (volume fraction) fields for the $i$th species. The single chain partition functions are $Q_{\mathrm{Ah}}, Q_{\mathrm{Bh}}$, $Q_{\mathrm{AB}}$, and $Q_{\mathrm{ABA}}$, for the A/B homopolymers, AB diblock copolymer, and ABA triblock copolymers respectively. The two indistinguishable terminal bonding sites of the B homopolymer result in the factor of 2 in the diblock coefficient. The partition functions, $Q_{i}$, can be expressed in terms of propagators, $q_{i}(\mathbf{r}, s)$, which are the single chain statistical weights for a continuous Gaussian chain of contour length $s$ at position $r$ and experiencing the $W_{i}$ potential field. All single chain partition functions may be written, $Q_{i}=1 / V \int \mathrm{d} \mathbf{r} q_{i}\left(\mathbf{r}, \alpha_{i}\right)$, for $\alpha_{i}=N_{i} / N$. The propagators satisfy the following modified diffusion equations¹⁷,³²⁻³⁴ with initial condition $q_{i}^{-}(\mathbf{r}, 0)=1$:

$$
\frac{\partial q_{\mathrm{Ah}}}{\partial s}=R_{\text {go }}{ }^{2} \nabla^{2} q_{\mathrm{Ah}}-W_{\mathrm{A}} q_{\mathrm{Ah}}, \quad 0<s<\alpha_{\mathrm{Ah}} \quad(9)
$$

$$
\frac{\partial q_{\mathrm{Bh}}}{\partial s}=R_{\text {go }}{ }^{2} \nabla^{2} q_{\mathrm{Bh}}-W_{\mathrm{B}} q_{\mathrm{Bh}}, \quad 0<s<\alpha_{\mathrm{Bh}} \quad(10)
$$

$$
\begin{aligned}
\frac{\partial q_{\mathrm{AB}}}{\partial s}=R_{\text {go }}{ }^{2} \nabla^{2} q_{\mathrm{AB}}-W_{i} q_{\mathrm{AB}}, \\
W_{i}= \begin{cases}W_{\mathrm{A}}, \text { if } 0<s<\alpha_{\mathrm{Ah}} \\
W_{\mathrm{B}}, \text { if } \alpha_{\mathrm{Ah}}<s<\alpha_{\mathrm{AB}}\end{cases}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial q_{\mathrm{ABA}}}{\partial s}=R_{\text {go }}{ }^{2} \nabla^{2} q_{\mathrm{ABA}}-W_{i} q_{\mathrm{ABA}}, \\
W_{i}= \begin{cases}W_{\mathrm{A}}, \text { if } 0<s<\alpha_{\mathrm{Ah}} \\
W_{\mathrm{B}}, \text { if } \alpha_{\mathrm{Ah}}<s<\alpha_{\mathrm{AB}} \\
W_{\mathrm{A}}, \text { if } \alpha_{\mathrm{AB}}<s<1\end{cases}
\end{aligned}
$$

where $R_{\text {go }}{ }^{2}=b^{2} N / 6$ is the ideal radius of gyration for a triblock copolymer.

The mean-field approximation is one that approximates the partition function by a single field configuration, $\{\phi_{\mathrm{A}}^{*}, \phi_{\mathrm{B}}^{*}, W_{\mathrm{A}}^{*}$, $W_{\mathrm{B}}^{*}, P^{*}$, the so-called saddle point, which is described by the following set of nonlinear equations,

$$
\begin{aligned}
\phi_{\mathrm{A}}= & z_{\mathrm{Ah}} \int_{0}^{\alpha_{\mathrm{Ah}}} \mathrm{d} s q_{\mathrm{Ah}}(\mathbf{r}, s) q_{\mathrm{Ah}}\left(\mathbf{r}, \alpha_{\mathrm{Ah}}-s\right)+ \\
& 2 z_{\mathrm{Ah}} \frac{\mathrm{e}^{h}}{N} \int_{0}^{\alpha_{\mathrm{Ah}}} \mathrm{d} s q_{\mathrm{AB}}(\mathbf{r}, s) q_{\mathrm{AB}}^{\dagger}(\mathbf{r}, s)+z_{\mathrm{Ah}} \frac{2 \mathrm{e}^{2 h}}{N^{2}}\left\{\int_{0}^{\alpha_{\mathrm{Ah}}} \mathrm{d} s\right. \\
& \left.q_{\mathrm{ABA}}(\mathbf{r}, s) q_{\mathrm{ABA}}^{\dagger}(\mathbf{r}, s)+\int_{\alpha_{\mathrm{AB}}}^{1} \mathrm{~d} s q_{\mathrm{ABA}}(\mathbf{r}, s) q_{\mathrm{ABA}}^{\dagger}(\mathbf{r}, s)\right\} \quad(13)
\end{aligned}
$$

$$
\begin{aligned}
\phi_{\mathrm{B}}= & \int_{0}^{\alpha_{\mathrm{Bh}}} \mathrm{d} s q_{\mathrm{Bh}}(\mathbf{r}, s) q_{\mathrm{Bh}}\left(\mathbf{r}, \alpha_{\mathrm{Bh}}-s\right)+2 z_{\mathrm{Ah}} \frac{\mathrm{e}^{h}}{N} \int_{\alpha_{\mathrm{Ah}}}^{\alpha_{\mathrm{AB}}} \mathrm{d} s \\
& q_{\mathrm{AB}}(\mathbf{r}, s) q_{\mathrm{AB}}^{\dagger}(\mathbf{r}, s)+z_{\mathrm{Ah}} \frac{2 \mathrm{e}^{2 h}}{N^{2}} \int_{\alpha_{\mathrm{Ah}}}^{\alpha_{\mathrm{AB}}} \mathrm{d} s q_{\mathrm{ABA}}(\mathbf{r}, s) q_{\mathrm{ABA}}^{\dagger}(\mathbf{r}, s) \quad(14)
\end{aligned}
$$

$$
\chi N \phi_{\mathrm{B}}-W_{\mathrm{A}}+P=0 \quad(15)
$$

$$
\chi N \phi_{\mathrm{A}}-W_{\mathrm{B}}+P=0 \quad(16)
$$

$$
\phi_{\mathrm{A}}+\phi_{\mathrm{B}}-1=0 \quad(17)
$$

where the asterisk has been omitted for convenience. The backward propagators, $q_{\mathrm{AB}}^{\dagger}$ and $q_{\mathrm{ABA}}^{\dagger}$, satisfy the same diffusion equations (eqs 11 and 12), but are integrated backward along the chain contour from the other chain end.

The mean field equations (eqs 13−17) are solved numerically. Initial field configurations are seeded in order to produce a unit cell for a desired mesophase and the modified diffusion equations (eqs 9−12) are solved via the pseudo-spectral method and the operator splitting scheme.³⁵ Using the calculated propagators, the volume fractions (eqs 13 and 14) are then evaluated. The other three mean field equations (eqs 15−17) are utilized in order to find the saddle point configurations of the fields by various relaxation schemes.¹⁷,³⁶,³⁷ Simultaneously, the grand canonical potential is minimized with regard to the size and the shape of the unit cell by a variable cell shape method.¹⁷,¹⁹ Related stress operators are given in Appendix B. Phase boundaries are calculated by comparing the calculated grand potentials (eq 5) of various phases at the same value of the A homopolymer activity $z_{\mathrm{Ah}}$.

#### B. Variable Cell Shape Method and Stress Operators.
A cell shape tensor, $\mathbf{h}$, constructed from the three vectors that define the edges of the simulated parallelepiped cell, is relaxed by means of the following fictitious dynamics:

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d} t} \mathbf{h}=- & \lambda_{h} \mathbf{h}\left(\Sigma_{\mathrm{Ah}}\left[W_{\mathrm{A}}, \mathbf{g}\right]+\Sigma_{\mathrm{Bh}}\left[W_{\mathrm{B}}, \mathbf{g}\right]+\right. \\
& \left.\Sigma_{\mathrm{AB}}\left[W_{\mathrm{A}}, W_{\mathrm{B}}, \mathbf{g}\right]+\Sigma_{\mathrm{ABA}}\left[W_{\mathrm{A}}, W_{\mathrm{B}}, \mathbf{g}\right]\right) \quad(18)
\end{aligned}
$$

where $\mathbf{g}$ is a metric tensor defined as $\mathbf{g} \equiv \mathbf{h}^{\mathrm{T}} \mathbf{h}$ and $\lambda_{h}$ is a relaxation parameter. The internal stress produced by the A/B homopolymers, AB, and ABA copolymers are $\Sigma_{\mathrm{Ah}}, \Sigma_{\mathrm{Bh}}$, $\Sigma_{\mathrm{AB}}$, and $\Sigma_{\mathrm{ABA}}$, which must vanish at equilibrium. They are evaluated in terms of propagators in the grand canonical ensemble by invoking a factorization of the single chain path integrals,¹⁷,¹⁹

$$
\begin{aligned}
\Sigma_{i}\left[W_{i}, \mathbf{g}\right]= & \\
& 2 \xi_{i} z_{i} R_{\text {go }}{ }^{2} \int \mathrm{d} \mathbf{X} \int_{0}^{\alpha_{i}} \mathrm{~d} s q_{i}(\mathbf{X}, s) \mathbf{g}^{-1} \nabla_{\mathbf{X}} \nabla_{\mathbf{X}} \mathbf{g}^{-1} q_{i}^{\dagger}(\mathbf{X}, s) \quad(19)
\end{aligned}
$$

where as before, $i$ indexes the four species. The activities are as specified in eqs 3 and 4, and through the $\xi_{i}$ factor, $\Sigma_{\mathrm{AB}}$ gains an extra prefactor of 2 as in eq 8 to account for the bond site degeneracy of homopolymer B. $\mathbf{X}$ is a cell-scaled position vector whose components lie in [0,1].

C. Details of the RPA Method. The $S_{ij}$ correlation functions are
$$
\begin{aligned}
S_{\mathrm{AA}}= & \phi_{\mathrm{Ah}} N_{\mathrm{Ah}} g_{\mathrm{D}}\left(\alpha_{\mathrm{Ah}} x, 1\right)+\phi_{\mathrm{AB}} N_{\mathrm{AB}} g_{\mathrm{D}}\left(\alpha_{\mathrm{AB}} x, \frac{\alpha_{\mathrm{Ah}}}{\alpha_{\mathrm{AB}}}\right)+ \\
& \phi_{\mathrm{ABA}} N\left[g_{\mathrm{D}}(x, 1)+g_{\mathrm{D}}\left(x, 1-2 \alpha_{\mathrm{Ah}}\right)+\right. \\
& \left.2\left\{g_{\mathrm{D}}\left(x, \alpha_{\mathrm{Ah}}\right)-g_{\mathrm{D}}\left(x, 1-\alpha_{\mathrm{Ah}}\right)\right\}\right](20)
\end{aligned}
$$

$$
\begin{aligned}
S_{\mathrm{BB}}= & \phi_{\mathrm{Bh}} N_{\mathrm{Bh}} g_{\mathrm{D}}\left(\alpha_{\mathrm{Bh}} x, 1\right)+\phi_{\mathrm{AB}} N_{\mathrm{AB}} g_{\mathrm{D}}\left(\alpha_{\mathrm{AB}} x, 1-\frac{\alpha_{\mathrm{Ah}}}{\alpha_{\mathrm{AB}}}\right)+ \\
& \phi_{\mathrm{ABA}} N g_{\mathrm{D}}\left(x, 1-2 \alpha_{\mathrm{Ah}}\right)(21)
\end{aligned}
$$

$$
\begin{aligned}
S_{\mathrm{AB}}= & \phi_{\mathrm{AB}} \frac{N_{\mathrm{AB}}}{2}\left\{g_{\mathrm{D}}\left(\alpha_{\mathrm{AB}} x, 1\right)-g_{\mathrm{D}}\left(\alpha_{\mathrm{AB}} x, \frac{\alpha_{\mathrm{Ah}}}{\alpha_{\mathrm{AB}}}\right)-\right. \\
& \left.g_{\mathrm{D}}\left(\alpha_{\mathrm{AB}} x, 1-\frac{\alpha_{\mathrm{Ah}}}{\alpha_{\mathrm{AB}}}\right)\right\}+\phi_{\mathrm{ABA}} N\left(g_{\mathrm{D}}\left(x, 1-\alpha_{\mathrm{Ah}}\right)-\right. \\
& \left.g_{\mathrm{D}}\left(x, \alpha_{\mathrm{Ah}}\right)-g_{\mathrm{D}}\left(x, 1-2 \alpha_{\mathrm{Ah}}\right)\right\}(22)
\end{aligned}
$$
where $g_{\mathrm{D}}(x, f)$ is the Debye function with $x=q^{2} R_{\mathrm{go}}{ }^{2}$, and $R_{\mathrm{go}}{ }^{2}$ $=b^{2} N / 6$ is the ideal radius of gyration for a triblock copolymer, and $\phi_{i}$ are the volume fractions of the homo- and copolymers in the homogeneous melt.

In the RPA method, it is necessary to expand around a reference state, which we choose to be the homogeneous fluid phase. As the SCFT calculation is carried out in grand canonical coordinates, we list here the expressions to connect this ensemble with the relevant canonical densities for the RPA calculation. The chemical potential is written,
$$
\begin{aligned}
2 \frac{\mu_{\mathrm{Ah}}}{k_{\mathrm{B}} T}=-\frac{1}{\alpha_{\mathrm{Bh}}} \ln \frac{\phi_{\mathrm{Bh}}}{\alpha_{\mathrm{Bh}}}+ & \ln \phi_{\mathrm{ABA}}-2\left(\ln \frac{\mathrm{e}^{h}}{N}\right)+ \\
& \left(1-\alpha_{\mathrm{Bh}}\right) \chi N\left(1-2 \phi_{\mathrm{A}}\right)(23)
\end{aligned}
$$

There is a single, independent density which we choose to be $\phi_{\mathrm{Ah}}$. The bonding constraints of eqs 3 and 4 as well as incompressibility determine the other densities, which are
$$
\phi_{\mathrm{Bh}}=\alpha_{\mathrm{Ah}}{ }^{2} \alpha_{\mathrm{Bh}}\left(1-\phi_{\mathrm{Ah}}\right) d^{-1}
$$

$$
\phi_{\mathrm{AB}}=2 \mathrm{e}^{h-\ln N} \frac{\alpha_{\mathrm{AB}}}{\alpha_{\mathrm{Ah}} \alpha_{\mathrm{Bh}}} \phi_{\mathrm{Ah}} \phi_{\mathrm{Bh}} d^{-1}
$$

$$
\phi_{\mathrm{ABA}}=\mathrm{e}^{h-\ln N} \frac{\phi_{\mathrm{AB}}}{2 \alpha_{\mathrm{Ah}} \alpha_{\mathrm{AB}}} \phi_{\mathrm{Ah}} d^{-1}
$$
with
$$
d=\alpha_{\mathrm{Ah}}{ }^{2} \alpha_{\mathrm{Bh}}+2 \alpha_{\mathrm{Ah}} \alpha_{\mathrm{AB}} \mathrm{e}^{h-\ln N} \phi_{\mathrm{Ah}}+\left(\mathrm{e}^{h-\ln N} \phi_{\mathrm{Ah}}\right)^{2}(27)
$$

The total A density is
$$
\phi_{\mathrm{A}}=\phi_{\mathrm{Ah}}+\frac{\alpha_{\mathrm{Ah}}}{\alpha_{\mathrm{AB}}} \phi_{\mathrm{AB}}+2 \alpha_{\mathrm{Ah}} \phi_{\mathrm{ABA}}
$$

The numerical procedure for RPA method for this system is as follows. Ultimately, we are interested in the spinodal that has the ratio $h / \chi N$ preserved for a system with a specified triblock polymerization $N$. We carry out this calculation by iterating over the bond strength $h$, which is initially guessed. For a given $h$ and also specified $\phi_{\mathrm{Ah}}$, the function $F\left(q, \phi_{\mathrm{A}, h}\right)$ of eq 7 is minimized with respect to $q$, which yields the spinodal point $(\chi N)^{\mathrm{sp}}$, and hence the ratio $h /(\chi N)^{\mathrm{sp}}$. The density $\phi_{\mathrm{Ah}}$ may then be adjusted, the minimization over $q$ reevaluated, and the process repeated until the desired ratio $h / \chi N$ is obtained. This process determines the spinodal volume fraction $\phi_{\mathrm{Ah}}{ }^{\mathrm{sp}}$, all other volume fractions from the above expressions, the inverse temperature $(\chi N)^{\mathrm{sp}}$ and the characteristic wavelength, $2 \pi / q$, for a single bond strength $h$. This determines a single point on the spinodal curve in, for example, Figure 2a or 2b.

References and Notes

(1) Huh, J.; Park, H. J.; Kim, K. H.; Kim, K. H.; Park, C.; Jo, W. H. Adv. Mater. 2006, 18, 624-629.

(2) Sijbesma, R. P.; Beijer, F. H.; Brunsveld, L.; Folmer, B. J. B.; Hirschberg, J. H. K. K.; Lange, R. F. M.; Lowe, J. K. L.; Meijer, E. W. Science 1997, 278, 1601-1604.

(3) Ruokolainen, J.; Mäkinen, R.; Torkkeli, M.; Mäkelä, T.; Serimaa, R.; ten Brinke, G.; Ikkala, O. Science 1998, 280, 557-560.

(4) Li, J.; Li, X.; Ni, X.; Wang, X.; Li, H.; Leong, K. W. Biomaterials 2006, 27, 4132-4140.

(5) Beck, J. B.; Rowan, S. J. J. Am. Chem. Soc. 2003, 125, 13922-13923.

(6) Matsuyama, A.; Tanaka, F. Phys. Rev. Lett. 1990, 65, 341-344.

(7) Tanaka, F.; Ishida, M. Macromolecules 1991, 24, 5582-5589.

(8) Tanaka, F.; Ishida, M. Macromolecules 1997, 30, 1836-1844.

(9) de Gennes, P. G. Scaling Concept in Polymer Physics; Cornell University Press: Ithaca, NY, 1979.

(10) Leibler, L. Macromolecules 1980, 13, 1602-1617.

(11) Dormidontova, E.; ten Brinke, G. Macromolecules 1998, 31, 26492660.

(12) Angerman, H. J.; ten Brinke, G. Macromolecules 1999, 32, 68136820.

(13) Huh, J.; Jo, W. H. Macromolecules 2004, 37, 3037-3048.

(14) Feng, E. H.; Lee, W. B.; Fredrickson, G. H. Macromolecules 2007, 40, 693-702.

(15) Matsen, M. J. Phys.: Condens. Matter 2002, 14, R21.

(16) Schmid, F. J. Phys.: Condens. Matter 1998, 10, 8105-8138.

(17) Fredrickson, G. H. The equilibrium theory of inhomogeneous polymers; Oxford University Press: Oxford, U.K., 2006.

(18) Fredrickson, G. H.; Ganesan, V.; Drolet, F. Macromolecules 2002, 35, 16-39.

(19) Barrat, J. L.; Fredrickson, G. H.; Sides, S. W. J. Phys. Chem. B 2005, 109, 6694-6700.

(20) Matsen, M. W. Macromolecules 1995, 28, 5765-5773.

(21) Nap, R. J.; ten Brinke, G. Macromolecules 2002, 35, 952-959.

(22) Matsen, M.; Thompson, R. B. J. Chem. Phys. 1999, 111, 7139.

(23) Broseta, D.; Fredrickson, G. H. J. Chem. Phys. 1990, 93, 2927-2938.

(24) Leibler, L.; Benoit, H. Polymer 1981, 22, 195.

(25) Corrales, L. R.; Wheeler, J. C. J. Chem. Phys. 1989, 91, 7097.

(26) Walker, J. S.; Vause, C. A. Sci. Am. 1987, 256, 98-105.

(27) Bates, F. S.; Maurer, W. W.; Lipic, P. M.; Hillmyer, M. A.; Almdal, K.; Mortensen, K.; Fredrickson, G.; Lodge, T. Phys. Rev. Lett. 1997, 79, 849.

(28) Fredrickson, G. H.; Bates, F. S. J. Polym. Sci., Polym. Phys. Ed. 1997, 35, 2775.

(29) Yamauchi, K.; Lizotte, J. R.; Hercules, D. M.; Vergne, M. J.; Long, T. E. J. Am. Chem. Soc. 2002, 124, 8599-8604.

(30) Hirschberg, J. H. K. K.; Brunsveld, L.; Ramzi, A.; Vekemans, J. A. J. M.; Sijbesma, R. P.; Meijer, E. W. Nature (London) 2000, 407, 167-170.

(31) Jonkheijm, P.; Hoeben, F. J. M.; Kleppinger, R.; van Herrikhuyzen, J.; Schenning, A. P. H. J.; Meijer, E. W. J. Am. Chem. Soc. 2003, 125, 15941-15950.

(32) Edwards, S. F. Proc. Phys. Soc. (London) 1965, 85, 613-624.

(33) de Gennes, P. G. Rep. Prog. Phys. 1969, 32, 187-206.

(34) Freed, K. Adv. Chem. Phys. 1972, 22, 1.

(35) Tzeremes, G.; Rasmussen, K. O.; Lookman, T.; Saxena, A. Phys. Rev. E 2002, 65, 041806.

(36) Sides, S. W.; Fredrickson, G. H. Polymer 2003, 44, 5859-5866.

(37) Ceniceros, H. D.; Fredrickson, G. H. Multiscale Model. Simul. 2004, 2, 452-474.

MA071714Y