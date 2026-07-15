![](./images/812702486304391170_1.jpg)

Subscriber access provided by BIU Pharmacie | Faculté de Pharmacie, Université Paris V

B: Fluid Interfaces, Colloids, Polymers, Soft Matter, Surfactants, and Glassy Materials

# The Impact of Salinity on the Interfacial Structuring of an Aromatic Acid at Calcite/Brine Interface: An Atomistic View on Low Salinity Effect

Mohammad Mehdi Koleini, Mohammad Hasan Badizad, Remco
Hartkamp, Shahab Ayatollahi, and Mohammad Hossein Ghazanfari

J. Phys. Chem. B, Just Accepted Manuscript • DOI: 10.1021/acs.jpcb.9b06987 • Publication Date (Web): 09 Dec 2019

Downloaded from pubs.acs.org on December 9, 2019

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W.,
Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# The Impact of Salinity on the Interfacial Structuring of an Aromatic Acid at Calcite/Brine Interface: An Atomistic View on Low Salinity Effect

Mohammad Mehdi Koleini¹,*,², Mohammad Hasan Badizad²,†,², Remco Hartkamp³,‡, Shahab Ayatollahi¹,‡, Mohammad Hossein Ghazanfari²

¹ Sharif Upstream Petroleum Research Institute (SUPRI), Department of Chemical and Petroleum Engineering, Sharif University of Technology, Tehran, Iran.
² Department of Chemical and Petroleum Engineering, Sharif University of Technology, Tehran, Iran.
³ Process & Energy Department, Faculty of Mechanical, Maritime and Materials Engineering, Delft University of Technology, Leeghwaterstraat 39, 2628CB Delft, The Netherlands.
* Corresponding Author; Email: mmkoleini@che.sharif.edu & mmkoleini@gmail.com
† Email: mohammadhasan.badizad@che.sharif.edu & badizad@gmail.com
‡ Email: shahab@sharif.edu
‡ Email: r.m.hartkamp@tudelft.nl
² Both authors contributed equally to this work.

### Abstract

This study aims to elucidate the impact of salinity on the interactions governing the adsorption of polar aromatic oil compounds onto calcite. To this end, molecular dynamics simulations were employed to assess adsorption of a model polar organic molecule (deprotonated benzoic acid, benzoate) on calcite surface in NaCl brines of different concentration levels, namely, de-ionized (DW), low salinity (LS, 5,000 ppm) and sea water (SW; 45,000 ppm). Calcite was found to be completely covered by several well-ordered water layers. The top hydration layer is very compact and prevents direct adsorption of benzoates onto the substrate. Instead, Na⁺ ions form a distinct positively charged layer by adhering on the calcite substrate through inner-sphere complexion mode. Cl⁻ ions mostly lodge upper the adsorbed sodium cations, forming a negatively charged layer. The distribution of ions at the calcite/brine interface thus exhibits the features of an electrical double layer, composed of a Stern-like positive layer followed by a negative one. The positive charged layer attracts benzoates toward the surface. As such, the sodium ions attached onto the calcite can act as adsorption sites to connect benzoates to the surface. By increasing salinity, more Na⁺ ions adsorb onto the calcite surface and the density of benzoate molecules at the interface is enhanced as a result of more Na⁺ bridging ions. The monotonic salinity-dependent adsorption of benzoate molecules on calcite offers a mechanism driving additional oil recovery upon injection of diluted brine into sub-surface carbonate reservoirs.


## INTRODUCTION

Solid/liquid interface is a matter of interest in diverse scientific and industrial disciplines. It covers numerous phenomena relevant to minerals, from biomineralization to enhanced oil recovery operation. To date, different types of mineral have been studied in the context of solid/liquid interface.¹⁻⁴ Especially calcite ($\text{CaCO}_3$) has been actively investigated,⁵⁻⁸ largely owing to its presence in many oil reservoirs.⁹ Despite strong water-favoring virtue of carbonates, those kinds of reservoirs are widely found to be oil-wet due to adhesion of polar hydrocarbons, typically carboxylic-end compounds, from crude oil onto the pore surfaces ¹⁰. This process takes place over the geological years, leading to coverage of rock surface by amphiphilic compounds of crude oil and hence, turning the wetting preference of pore walls to oil-wet state ¹¹. Little is known about interactions governing oil-wetness of calcite reservoirs as well as relevant controlling factors.

Injection of low salinity brines introduced about two decades ago as an efficient, economic and also environmental-friendly method for enhancing oil production from sub-surface reservoirs ¹². Unlike traditional waterflooding operations carried out by exploiting sea water (SW), it has been observed that oil displacement by diluted SW provides additional oil recovery ¹³. The working mechanism(s) of such production enhancement is not well understood yet; it is unanimously conceived that injection of low salinity (LS) saltwater alters the wettability of oil-bearing rocks to favoring, water-wet condition ¹⁴. In this sense, ions act as mediating agents, facilitating adsorption of charged hydrocarbons on rock substrates ¹⁵. Upon reducing salinity of pore space, the ions will release from

the pore walls and at the same time, detaching oil species. This notion has been corroborated via extensive nano-scale observations and also, a few atomistic investigations on clay and quartz surface $^{16,17}$. In general, the wettability alteration by salinity modification is in essence of adsorption/desorption process. This general concept is yet obscure, especially for calcite minerals, needing deep analysis to explore how ions come to the play for the access of oil compounds to a naturally water-wet mineral. This stems from the molecular complexity of oil, so that one cannot definitely discern the contribution of chemical structures and functional groups into wettability of the reservoir rock.⁹ However, It has been well-established that the interaction of polar –COOH groups from the oil with calcite is the most decisive for wettability changes since organic molecules with carboxyl groups strongly bind to calcite substrate and render the surface oil-wet. $^{18-24}$ Molecular-level insight is needed to understand the complex competitive interactions between brine, calcite and organic molecules.

In this paper, molecular dynamics (MD) simulation was employed to unveil the interfacial behavior of a mixture of brine and model oil (mimicked by benzoate molecules; as a typical hydrolyzed aromatic acid) confined by calcite slabs. Brines with $Na^{+}$ and $Cl^{-}$ ions at different salinities are compared to study the impact of salinity on the interactions at the calcite/fluid interface. Specifically, we study how the distribution of ions at different salinities at the calcite/brine interface and in the bulk affects the interactions of organic molecules with the mineral.

# METHODS

MD simulations were carried out to simulate an oil-brine mixture enclosed between two parallel calcite slabs (Figure S1; Supporting Information). Various monovalent and divalent ions are commonly present in brines (e.g.; $Na^+$, $Cl^-$, $Ca^{2+}$, $Mg^{2+}$, $SO_4^{2-}$), resulting in a complicated interplay between competing interactions at the calcite/brine interface.²⁵ We here focus our attention on $Na^+$ and $Cl^-$ ions, which are the prevalent electrolytes in sea and ground water²⁶ and are expected to play a determining role in preferred wettability of calcite surface. In a conventional waterflooding operation, sea water (with typical salinity 30,000-70,000 ppm⁸) is utilized as the injecting fluid, because of its availability and accessibility by off-shore drilling rigs. In a normal lab practice, diluted aliquots of SW (5 to 100 times dilution) is normally utilized to examine wettability response of a rock sample to decreasing salinity. With this regard, we probe the impact of $Na^+$ and $Cl^-$ at salinities 0.0, 5,000 and 45,000 ppm corresponding to typical concentrations for de-ionized water (DW), low-salinity water (LS) and sea water (SW), respectively. It should be emphasized that 24 sodium ions were added as background ions to each model in order to satisfy neutrality of the model. It is critical to take charge balancing cations in conjunction with negatively charged benzoates.

Benzoic acid is a proper candidate for mimicking polar fraction of crude oil, having enough solubility in water to in effect being adhered on minerals in aqueous solutions ¹⁸,²⁷,²⁸.The saline brine in carbonate reservoirs is known to be buffered to a basic pH, normally at 8.¹⁷,²⁹ At such basic condition, it is expected that carboxylic acids (with $pK_a$=4.2 ³⁰) are largely deprotonated to the carboxylate

$(-\text{COO}^-)$ form.$^{16}$ This is the reason behind the selection of benzoate, rather than benzoic acid. Though heavy compounds, viz. asphaltene and resin, are supposed to comprise major polar fraction of crude oil, the hydrocarbon model (benzoate) in this study was taken as simple as possible in order to avoid potential intricacies coming with self-interaction (often laterally) of adsorbed molecules, as pointed out by Legens et al. $^{27}$, and their self-assembly in the bulk, for example, well-known asphaltene aggregation. In this manner, we focus specifically on the impact of salinity on surface adsorption of polar compounds.

The calcite $\{10\overline{1}4\}$ plane was considered as the adsorption surface of the mineral in contact with the brine. The charge-neutral $\{10\overline{1}4\}$ plane of calcite is known as the most stable cleavage plane of the mineral.$^{31}$ The planar surface is oriented orthogonally to the z-direction. The calcite slab dimensions are 56.67 Å x 54.89 Å x 19.77 Å, with a total of 1078 ${\text{CaCO}}_3$ units. The periodic boundary condition was set to all directions, while having two 5nm-thick vacuum spaces were placed above and below the calcite slabs in order to avoid unwanted interaction of period images along the z-direction. In each of the simulations, 24 benzoate molecules were placed in ordered arrangement near the middle of the 60 Å slit pore (see Figure S2). Next, the slit was filled by 6183 water molecules, to achieve a water density of approximately $1\ \text{g.cm}^{-3}$, using the PACKMOL package.$^{32}$ Subsequently, the required number of ions to satisfy each desired salinity was randomly inserted into the ensemble. Sufficient excess $\text{Na}^+$ ions were added to balance the negative charge of benzoates.

We adopted interatomic potentials derived by Xiao et al.$^{33}$ for calcite and water was treated using the flexible TIP3P/Fw model.$^{34}$ This force-field has found

its popularity in recent studies on interface characteristics of organic compounds contacting calcite $^{35,36,37}$. The water model and the C-O bond of carbonate in calcite are flexible for a more realistic description of interactions of calcite with water and benzoates at the interface. $^{38}$ We used the OPLS-AA$^{39,40}$ forcefield to describe the interaction of benzoates and the interaction parameters of $Na^+$ and $Cl^-$ ions. This parameter set is verified to be consistent with that of $CaCO_3$ $^{33}$.

Interactions between different species were modeled using a geometric mixing rule:

$$
\begin{align}
A_{ij} &= \sqrt{A_i \times A_j} \\
B_{ij} &= \sqrt{B_i \times B_j}
\end{align}
$$

where A and B are the parameters of Lennard-Jones (LJ) potential in equation 2.

The LJ 12-6 and Coulomb potential describe the van der Waals and electronic contributions, respectively:

$$
E_{LJ + Coul} = \left[ \frac{A}{r_{ij}^{12}} - \frac{B}{r_{ij}^6} \right] + \frac{e^2}{4\pi\varepsilon_0} \cdot \frac{q_i q_j}{r_{ij}}
$$

where $r_{ij}$ is the distance between the atoms i and j, $q$ is the atomic charge and $\varepsilon_0$=8.854 187 82 × $10^{-13}$ F.nm$^{-1}$ is the vacuum permittivity. The energies of covalent bonds, bond angles and dihedral angles are described by:

$$
E_{bond} = \sum_i K_i^r (r_i - r_{i0})^2
$$

$$
E_{angle} = \sum_i K_i^\theta (\theta_i - \theta_{i0})^2
$$

$$
E_{dihedral} = \frac{1}{2} \sum_i \sum_{n=1}^4 V_{n,i} \left[ 1 + (-1)^{n+1} \cos\left(n\varphi_i\right) \right]
$$


where $r_{i0}$ and $\theta_{i0}$ are the equilibrium bond lengths and equilibrium covalent angles, while the $K$ values are their respective stiffnesses and $\varphi_{i}$ is the dihedral angle.

The simulations were performed using the LAMMPS⁴¹ package with a simulation time-step of 1 fs. Van der Waals interactions were truncated at a cut-off distance of 15.0 Å. Long-range Coulomb interactions were resolved using the particle-particle/particle-mesh (PPPM) method in reciprocal space beyond 15.0 Å with an accuracy of $10^{-5}$. All simulations were performed by keeping the box volume constant, with the Nosé-Hoover⁴²,⁴³ thermostat coupled to the fluid particles to set the fluid’s temperature to 80 °C. Equilibrium conditions were reached by firstly running simulation for 0.5 ns; meanwhile the bottom calcite slab was held in place by freezing its constituting atoms whereas the top one was made rigid, i.e., treated as a whole single entity. This allowed the upper slab to freely move up and down in response to the thermal expansion/compression of confined brine solution coupled to a thermostat at 80 °C. In this sense, the top slab floats up and down like a solid free piston above the brine solution. It should be emphasized that the presence of 5 nm-thick vacuum layer above the calcite slit allows the upward/downward movement of the top slab and consequently, the volume change of the confined solution. By then, during the next 1.5 ns, a 30 MPa equivalent force was exerted on the upper slab at the same temperature. In this case, the slab acts as a piston by applying the desired reservoir pressure on the brine. At the end of this stage, the upper slab was made fixed (as the lower one) and the production run began. This procedure is schematically shown in the Appendix of the supporting information. The production run simulations were performed for 50 ns, with atom’s trajectories being printed every 0.5 ps for post-

analysis. The simulation protocol is presented in detail in the appendix of Supporting Information together with discussion on verifying sufficiency of equilibration timespans.

# RESULTS

In this section, we present the results of our analysis using trajectory data gathered from the last 20 ns timeframe of the production run. In the following, firstly, mean square displacement (MSD) of benzoates was monitored vs. time to infer equilibrium timeframe for gathering statistics (see Supporting Information for the details). Molecular densities are displayed to analyze the impact of salinity on the distribution of benzoates across the calcite slit. The distribution of ions in different salinities is also explored to study the influence of charge distribution on benzoate-calcite interplay. This interaction is then verified via radial distribution functions. The persistence of benzoates within the calcite/brine interfacial region is analyzed with the aid of survival probability and residence time. Finally, the spatial arrangement and orientation of benzoates are scrutinized nearby the substrate. All analyses are purposed to probe the effect of salinity level on the interactions between the model organics molecules (represented by benzoates) with the calcite surface.

## Density distribution of species

### a. Water density

The number density profile of water's oxygen (Ow) and hydrogen (Hw), shown in Figure 1a-c, indicates well-structured hydration layers within the calcite/brine interfacial region. Note all distribution profiles are symmetrized over


calcite surfaces. As seen, these rugged layering of Ow density are followed by a nearly smooth profile toward the bulk of the brine. We recently verified that the formation of such well-ordered hydration layers is a consequence of the crystal structure of the calcite substrate.⁴⁴ The appearance of two distinguishable water layers is in agreement with the observation made by Fenter.⁴⁵,⁴⁶ Mutisya et al.³⁸ reported that this ordering is the result of direct interaction of water molecules with calcite. This has been validated by Ukrainczyk et al.,⁴⁷ who pointed out that the water molecules in the first hydration layer directly bind to the outermost Ca atoms. Our previous results from density functional theory calculations are in agreement with their findings.⁴⁸

The water atomic densities in Figure 1 are interpreted from our recently published results.⁴⁴ The water molecules closest to the calcite surface, as implied by sharp peak of Ow profile, orient such that establishing strongest interactions with surface calcium while maintaining H-bonding with upper (secondary) water layer. At the same time, the second layer of water molecules form hydrogen bonds with outmost oxygen of surface carbonate groups. This arrangement is well reflected in the broad first peak of Hw, standing between the two Ow layers. The first hydration layer, directly on top of the substrate, is the precursor of all adsorbing layers onto the calcite substrate. The density profiles in Figure 1a-c reveal that organic species locate beyond dense hydration layers. Kirch et al.⁴⁹ recently identified a hydrogen bonding network in the hydration layer that results in a persisting thin water film wetting carbonate reservoirs.¹² The density of the second hydration layer is much lower than that of the first one. The more likely permeation of ions into layer lowers its density at higher salinities, as shown in

Figure 1a-c. This was found to disturb the hydrogen bonding network in this second layer.⁴⁹

Following two dense hydration layers bordering the calcite slab, there are some contiguous, modest layers, henceforth called "transition zone", coming before the bulk-like fluid region. This somehow broad zone is easily permeable to ions and benzoate molecules. Regarding this definition, the space enclosed by calcite slabs was partitioned into interfacial and bulk space, with former (around 1 nm outward the solid surface) indicating the regions of oscillatory Ow density adjacent to solid surface and latter, the space in middle of interfacial zones, both sketched in Figure S3.

### b. Ions
The ion distribution profiles in Figure 1d-e indicate that most of $Na^+$ ions are located immediately above the calcite substrate. The sharp narrow peak of sodium ions are so close to first hydration layer, suggesting that sodium ions bind directly to the basal (upper) oxygen atoms of calcite substrate with no intervening water molecule, which was visually identified as well, Figure S1. In this fashion, electrostatic interaction is so strong that allow outmost carbonate oxygen to be contained in the first coordination shell of adsorbed $Na^+$ ions. As a further corroboration, the RDF profiles of sodium was obtained with respect to oxygen atoms of carbonate and water within the interface as well as regarding the water oxygen in the bulk phase, shown for varying salinities in Figure 2a. In all salinities, the first peak of g(r) ($Na^+$-Ow) for both interface and bulk region coincide, nearly at 2.4 Å, but with greater height in the latter case which means the partial solvation of $Na^+$ ions at interface due to carbonate oxygen sharing with water in

the first hydration shell compared to the complete hydration of the ion expected in the bulk. Additionally, the sharp peak of RDF for $Na^+-O_{calcite}$ results by extreme localization of sodium ions at close separation to the calcite surface.

Though some of the $Cl^-$ ions lodge together with the $Na^+$ cations directly on the basal calcite surface, they are mostly concentrated within the transition zone between hydration layers and bulk water. By increasing salinity, the number of ions in the interface also increases, and an electrical double layer (EDL) will appear at the interface in LS and SW solutions (Figure 2b). The development of such an EDL close to a neutral surface supports the idea that a double layer does not necessarily require the surface to be charged. $^{25,50}$ The sharp density peak of $Na^+$ ions, as shown in Figure 1d-e, exceeds that of the $Cl^-$ ions in the same layer, resulting in a net positively charged layer in proximity to the calcite surface. Such a compact layer of ions resembles the concept of Stern layer that would form adjacent to a charged surface. $^4$ The position of the positive peak between two monolayers of water at the interface is in agreement with observed locations of counterions in the Stern layer near multiple smooth charged surfaces. $^{51,52}$ The broader negative layer is analogous to a diffuse layer, which balances the positive charge of the positive layer. $^{53}$

### c. Benzoate
The number density distribution of benzoates, Figure 1a-c, was acquired by tracing z-coordinate of the phenyl carbon attached to the carboxylate group in each molecule. Benzoate molecules mostly appear within the edge of the transition zone of the calcite/water interface. The strong density peak of these molecules implies an adsorption mechanism, whereby benzoates penetrate into

the interfacial transition zone to approach the calcite surface. That peak is followed by a faint one at ≈8.5 Å denoting the occasional hydrophobic contact of bulk benzoates with those adsorbed on the surface. Beyond this, the density of benzoates decays towards the bulk region. Note that the peak height of benzoate density in the interfacial region increases proportional to salinity, with the highest value at SW brine. This increasing trend suggests that the benzoate adsorption on calcite is governed by ions at the interface, with greatest adsorption at highest salinity, SW.

Radial distribution function

Radial distribution functions (RDF, $g^{(r)}$) were analyzed to investigate the probability of molecules or ions to form pairs. The RDFs for benzoates in Figure 3 show a clear difference between the self-interaction of the polar molecules inside the interface and bulk regions at different salinities. Within both regions, the highest probability of benzoates interaction is due to SW, in accordance with their highest population (density) at that salinity, already seen in Figure 1. In the RDF profile of benzoate-Na⁺ (Figure 4), there is a significant peak at ≈4.5 Å, suggesting the emergence of direct pairing. The greater potential for ion-benzoate pairing is clearly deduced by greater peak of RDF at the interface, with the most plausible interactions at LS brine. The probability of Na⁺-Cl⁻ pairing is totally distinct for LS and SW at the interface and bulk space (Figure 5). The first pronounced peak at 2.75 Å corresponds to formation of Na-Cl contact ion pair which is in agreement with the literature.⁵⁴,⁵⁵ The literature also confirms the second peak at 5.2 Å for bulk space which belongs to solvent separated ion pairs.⁵⁵,⁵⁶ As shown in Figure 5, it is more probable to observe Na⁺-Cl⁻ pairs in the bulk SW, whereas in the

interface of LS that type of ion-pairing is more plausible. The RDF between benzoates and water reflects strong interaction between these molecules, indicated by the formation of multiple hydration shells around benzoates (Figure S4). Seemingly, benzoate-water interaction slightly diminishes by salinity. It might be ascribed to the greater extent of benzoate-Na⁺ complexion at higher salinities.

## Survival probability and residence time

At this stage, we examine the tendency of benzoates for staying in the bulk and interface regions. Residence time is a proper analysis for this purpose, obtained by the time integration of survival probability function, defined by ⁵⁷:

$$
p(t)=\frac{1}{T} \sum_{t_{0}=1}^{T} \frac{N\left(t_{0} . t_{0}+t\right)}{N\left(t_{0}\right)}
$$

The survival probability, $p(t)$, is the number of benzoate molecules $N(t_o, t_o$+$t)$ that remains adsorbed within time interval $[t_o, t_o$+$t]$ relative to the total number of benzoates, $N(t_o)$, present at the interface at the initial time, $t_o$, averaged over all timesteps, $T.^{38}$ Figure 6a-b displays the survival probability for interface and bulk space, smoothed by fitting to exponential curves. In both cases, the survival probability of benzoates decay faster at DW compared to other solutions.

Accordingly, the longest residence time belongs to highest salinity solution, SW (Figure 6c). The salinity-dependence of residence time is rationalized by the fact that at higher salinity the benzoates find more Na⁺ ions near the interface and within the bulk to pair with and thus, prefer staying in each region longer. Let's think of benzoates dynamically exchanging between bulk and interface spaces. There would be greater Na⁺ ions on the calcite surface at higher salinity which will entangle a higher fraction of benzoates at the interface. Hence, benzoates tend

staying nearby the calcite surface at concentrated solutions which in turn slowdowns the bulk-interface transfer process.

Orientation of benzoates

So far, we have observed that the behavior of benzoates at the interface is largely affected by salinity of the brine. It is also expected that the salinity of the brine impacts the orientation of benzoates with respect to the surface. To inspect such impact two orientation angles were probed:

a. Orientation of –COO functional group

We defined a vector that passes through the phenyl ring and the carbon atom of the –COO functional group (see Figure 7a). $\theta$ is the angle of the intersection of this vector with any plane parallel to the calcite surface. The value of $\theta$ is close to 50°, which reflects that the polar molecules are oriented with their –COO head group inclined to the surface normal vector (Figure 7b).

b. Orientation of the aromatic ring

To scrutinize the orientation of the aromatic ring with respect to the surface, we defined $\phi$ as the angle between the normal vector to the phenyl ring and the plane parallel to the calcite surface, as depicted in Figure 7a. The dominant distribution of angles around 0°, extending between -20° and 20°, reveals the nearly perpendicular orientation of the phenyl ring with respect to the calcite surface (Figure 7c).

The orientation analysis of benzoates supports the idea of pairing between the negative functional group of benzoate ($\text{–COO}^-$) and the interfacial $\text{Na}^+$ ions. Note that in both maps of benzoate orientations, the salinity does not totally change the orientation of the molecules with respect to the substrate. However,

in the SW brine the orientation of benzoates is the most well-ordered among all salinities to afford the most efficient interaction between benzoates and hydrated calcite surface via positive sodium ions. Thus sufficient number of $Na^+$ ions adsorbed onto hydrated calcite can regulate the orientation of benzoates with respect to surface.

Lateral density profile

Thus far, different analyses suggested that $Na^+$ ions residing on the calcite surface act as adsorption sites for linking benzoate molecules to the solid substrate. As a complement to that deduction, we need a statistically-sound analysis to evaluate the average positioning of species in the calcite interface. For this purpose, lateral density map was obtained for benzoate and ions in the interface regions, shown as superimposed in Figure 8. The results reveal that $Na^+$ ions tightly lodge onto calcite that is inferred by dense blue marks in all salinities. Together, in LS and SW brines, there are some sporadic green signs, indicating the direct adsorption of $Cl^-$ assisted by in situ $Na^+$ ions. This recalls the multi-modal density profile of chloride, already depicted in Figure 1, having one peak coinciding with that of $Na^+$. It is interesting to note that the protruding oxygen atoms of surface carbonates act as adsorbing sites for sodium cations. This is clearly recognized by comparing lateral density map of $Na^+$ in the interfaces and the structure of outermost layer of calcite substrates (Figure 9).

The pink background of Figure 8 shows the accessibility of benzoate to any planar coordinate within the calcite interface. However, it is noticed that benzoate do not uniformly visit the whole calcite surface. There are some preferred locations, dense marks in Figure 8, for surface accumulation of benzoates. The clear overlap

of those portions with densely occupied Na⁺ points, provides an additional evidence for concluding that adsorbed sodium cations are potential sites for pining wandering benzoates to the calcite surface. The density maps reveal that benzoates mostly appear nearby adsorbed Na⁺ ions (encircled by dashes). The accumulated population of benzoates that adsorb at the interface is the largest at SW. While adsorbed cations potentially link benzoates to the surface, the adsorbed Cl⁻ anions do not so, as can be expected. As well, the ratio of benzoates that pair with Na⁺ ions is highest at SW (Figure 10).

## DISCUSSION

The formation of stratified hydration layers over calcite, as shown by the density profiles, is in agreement with layered structuring of water observed in previous works.³⁸,⁴⁹ A monolayer of water molecules compactly covers the immediate vicinity of calcite. The persisting monolayer of water wetting the calcite surface consolidates water wetness of the substrate.¹² This dense water layer, nonetheless, could be penetrated by sodium cations to establish inner-sphere complexion with outmost oxygen atoms of basal carbonate groups. In this circumstance, Na⁺ cations adhere on the calcite substrate by partially persevering their coordinating shell.⁵⁸ Cl⁻ ions partly adsorb alongside the cations and stay beyond the first two hydration layers as well. This type of uneven ion distribution leads to the development of an EDL, consisting of a positively charged Stern-like layer, followed by a negatively charged layer. The induced positive charge on the hydrated calcite agrees with the observed positive zeta potential of carbonates, especially by increasing NaCl concentration.⁵⁹,⁶⁰ Observing positive zeta potential is, in effect, the consequence of the permeation of Na⁺ ions into the hydration

layer on top of the calcite. As such, the electrostatic field induced by the positive layer encourages benzoates toward the interface. Upon Visual inspection and several quantitative analyses, it was judged that $Na^+$ ions adsorbed on calcite, potentially act as adsorption sites for capturing benzoates migrated to the interface. The interaction between $Na^+$ ions and benzoates also regulates the orientation of the polar organic molecules with respect to the substrate. By increasing salinity, the number of sodium ions adsorbed onto the hydrated calcite is increased, providing more adsorption sites for the benzoates. This, in turn, enhances stay-time of benzoates near the interface. This finding offers a clue for understanding the nano-scale mechanism behind wettability alteration and additional oil recovery when flooding oil-bearing strata by diluted brines. Sea water is the most available solution used for displacing and pressurizing oil inside subsurface reservoirs $^{12}$. In keep with empirical observations, the atomic-resolved results obtained in this study, suggests a direct correlation between salt content in pore spaces and extent of oil-wetness of calcite rocks. This was rationalized by recalling that adsorption of amphiphilic compounds on a calcite surface could effectively modulate its wetting character to oil-wetting state.

## CONCLUSION

In this research, molecular simulation was carried out to evaluate impact of salinity on adsorption tendency of benzoate molecule, a typical model for aromatic acids, within a calcite slit. A water monolayer was found to persistently wet the calcite surface, preventing direct adsorption of benzoates onto the mineral. On top of the compact wetting monolayer, an electrical double layer (EDL) is formed. This EDL is composed of a positive layer close to calcite basal

surface followed by a negatively charged layer. The positive layer appears due to net accumulation of $Na^+$ as inner-sphere charged points above calcite substrate, whereas $Cl^-$ anions dominate within the next hydration layers. Such net positively charged layer effectively entices the polar benzoates toward the interface. By this effect, the benzoates permeate toward the interface with their $-COO^-$ functional group pointing to the substrate. This orientation enables the molecules to interact directly with $Na^+$ ions within the interface region. As a consequence, the benzoates adsorb indirectly onto the hydrated mineral, with $Na^+$ serving as bridging ions. The number of potential adsorption sites for the benzoates increases proportional to salinity. The results presented in our study suggest a nano-metric mechanism driving salinity-dependent wettability of calcite minerals.

# ASSOCIATED CONTENT

## Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI:

Snapshot of configuration of simulation ensembles, a graphical definition of different layers of brine, RDF of benzoate-water interaction and an appendix describing the equilibrium state criteria of the simulation along with simulation procedure.

# AUTHOR INFORMATION

## Corresponding Author
*Email: mmkoleini@che.sharif.edu & mmkoleini@gmail.com

## ORCID
Mohammad Mehdi Koleini: 0000-0001-7950-951X

Mohammad Hasan Badizad: 0000-0001-8144-6896

Remco Hartkamp: 0000-0001-8746-8244

Shahab Ayatollahi: 0000-0001-7561-6393

Notes

The authors declare no competing financial interest.

ACKNOWLEDGMENTS

The authors are thankful to the Research and Technology Deputy of the Sharif University of Technology for the financial supports.

<br>

## References

(1) Mohammadpour, F.; Dokoohaki, M. H.; Zolghadr, A. R.; Ghatee, M. H.; Moradi, M. Confinement of Aqueous Mixtures of Ionic Liquids between Amorphous TiO 2 Slit Nanopores: Electrostatic Field Induction. *Phys. Chem. Chem. Phys.* **2018**, *20* (46), 29493–29502.

(2) Adapa, S.; Swamy, D. R.; Kancharla, S.; Pradhan, S.; Malani, A. Role of Mono-and Divalent Surface Cations on the Structure and Adsorption Behavior of Water on Mica Surface. *Langmuir* **2018**, *34* (48), 14472–14488.

(3) Zhang, L.; Lu, X.; Liu, X.; Yang, K.; Zhou, H. Surface Wettability of Basal Surfaces of Clay Minerals: Insights from Molecular Dynamics Simulation. *Energy Fuels* **2016**, *30* (1), 149–160.

(4) Hocine, S.; Hartkamp, R.; Siboulet, B.; Duvail, M.; Coasne, B.; Turq, P.; Dufrêche, J.-F. How Ion Condensation Occurs at a Charged Surface: A Molecular Dynamics Investigation of the Stern Layer for Water--Silica Interfaces. *J. Phys. Chem. C* **2016**, *120* (2), 963–973.

(5) Freeman, C. L.; Harding, J. H. Entropy of Molecular Binding at Solvated Mineral Surfaces. *J. Phys. Chem. C* **2014**, *118* (3), 1506–1514.

(6) Chang, X.; Xue, Q.; Li, X.; Zhang, J.; Zhu, L.; He, D.; Zheng, H.; Lu, S.; Liu, Z. Inherent Wettability of Different Rock Surfaces at Nanoscale: A Theoretical Study. *Appl. Surf. Sci.* **2018**, *434*, 73–81.

(7) Xue, Z.; Shen, Q.; Liang, L.; Shen, J.-W.; Wang, Q. Adsorption Behavior and Mechanism of SCA-1 on a Calcite Surface: A Molecular Dynamics Study. *Langmuir* **2017**, *33* (42), 11321–11331.

(8) Budi, A.; Stipp, S. L. S.; Andersson, M. P. The Effect of Solvation and Temperature on the Adsorption of Small Organic Molecules on Calcite. *Phys. Chem. Chem. Phys.* **2018**, *20* (10), 7140–7147.

(9) Walker, S. M.; Marcano, M. C.; Kim, S.; Taylor, S. D.; Becker, U. Understanding Calcite Wettability Alteration through Surface Potential Measurements and Molecular Simulations. *J. Phys. Chem. C* **2017**, *121* (50), 28017–28030.

(10) Austad, T.; Shariatpanahi, S. F.; Strand, S.; Black, C. J. J.; Webb, K. J. Conditions for a Low-Salinity Enhanced Oil Recovery (EOR) Effect in Carbonate Oil Reservoirs. *Energy and Fuels* **2012**, *26*, 569–575.

(11) Mohammed, M.; Babadagli, T. Wettability Alteration: A Comprehensive Review of Materials/Methods and Testing the Selected Ones on Heavy-Oil Containing Oil-Wet Systems. *Advances in Colloid and Interface Science.* **2015**, 54–77.

(12) Sheng, J. J. Critical Review of Low-Salinity Waterflooding. *Journal of Petroleum Science and Engineering.* **2014**, 216–224.

(13) Koleini, M. M.; Badizad, M. H.; Kargozarfard, Z.; Ayatollahi, S. Interactions between Rock/Brine and Oil/Brine Interfaces within Thin Brine Film Wetting Carbonates: A Molecular Dynamics Simulation Study. *Energy Fuels* **2019**, *33*, 7983–7992.

(14) Hao, J.; Mohammadkhani, S.; Shahverdi, H.; Esfahany, M. N.; Shapiro, A. Mechanisms of Smart Waterflooding in Carbonate Oil Reservoirs - A Review. *Journal of Petroleum Science and Engineering.* **2019**.

(15) Ayirala, S. C.; Yousef, A. A. A Critical Review of Alternative Desalination Technologies for Smart Waterflooding. *Oil Gas Facil.* **2016**, 5.

(16) Rios-Carvajal, T.; Pedersen, N. R.; Bovet, N.; Stipp, S. L. S.; Hassenkam, T. Specific Ion Effects on the Interaction of Hydrophobic and Hydrophilic Self-Assembled Monolayers. *Langmuir* **2018**, *34* (35), 10254–10261.

(17) Liu, Z. L.; Rios-Carvajal, T.; Andersson, M. P.; Ceccato, M.; Stipp, S. L. S.; Hassenkam, T. Insights into the Pore-Scale Mechanism for the Low-Salinity Effect: Implications for Enhanced Oil Recovery. *Energy and Fuels* **2018**, *32* (12), 12081–12090.

(18) Lagerge, S.; Rousset, P.; Zoungrana, T.; Douillard, J. M.; Partyka, S. Adsorption of Benzoic Acid from Organic Solvents on Calcite and Dolomite: Influence of Water. *Colloids Surfaces A Physicochem. Eng. Asp.* **1993**, *80* (2–3), 261–272.

(19) Frye, G. C.; Thomas, M. M. Adsorption of Organic Compounds on Carbonate Minerals. 2. Extraction of Carboxylic Acids from Recent and Ancient Carbonates. *Chem. Geol.* **1993**, *109* (1–4), 215–226.

(20) Maruyama, M.; Tsukamoto, K.; Sazaki, G.; Nishimura, Y.; Vekilov, P. G. Chiral and Achiral Mechanisms of Regulation of Calcite Crystallization. *Cryst. Growth Des.* **2008**, *9* (1), 127–135.

(21) Nada, H. Difference in the Conformation and Dynamics of Aspartic Acid on the Flat Regions, Step Edges, and Kinks of a Calcite Surface: A Molecular Dynamics Study. *J. Phys. Chem. C* **2014**, *118* (26), 14335–14345.

(22) Okhrimenko, D. V.; Nissenbaum, J.; Andersson, M. P.; Olsson, M. H. M.; Stipp, S. L. S. Energies of the Adsorption of Functional Groups to Calcium Carbonate Polymorphs: The Importance of -OH and -COOH Groups. *Langmuir* **2013**, *29* (35), 11062–11073.

(23) Sedghi, M.; Piri, M.; Goual, L. Atomistic Molecular Dynamics Simulations of

Crude Oil/Brine Displacement in Calcite Mesopores. *Langmuir* **2016**, 32 (14), 3375−3384.

(24) Ghatee, M. H.; Koleini, M. M.; Ayatollahi, S. Molecular Dynamics Simulation Investigation of Hexanoic Acid Adsorption onto Calcite (1014)Surface. *Fluid Phase Equilib.* **2015**, 387, 24−31.

(25) Liu, J.; Wani, O. B.; Alhassan, S. M.; Pantelides, S. T. Wettability Alteration and Enhanced Oil Recovery Induced by Proximal Adsorption of Na+, Cl-, Ca2+, Mg2+, and SO42- Ions on Calcite. *Phys. Rev. Appl.* **2018**, 10 (3), 34064.

(26) Yousef, A. A.; Al-Saleh, S. H.; Al-Kaabi, A.; Al-Jawfi, M. S. Laboratory Investigation of the Impact of Injection-Water Salinity and Ionic Content on Oil Recovery From Carbonate Reservoirs. *SPE Reserv. Eval. Eng.* **2011**, 14 (05), 578−593.

(27) Legens, C.; Toulhoat, H.; Cuiec, L.; Villiéras, F.; Palermo, T. Wettability Change Related to Adsorption of Organic Acids on Calcite: Experimental and Ab Initio Computational Studies. *SPE J.* **1999**.

(28) Zeng, H.; Zou, F.; Horvath-Szabo, G.; Andersen, S. Effects of Brine Composition on the Adsorption of Benzoic Acid on Calcium Carbonate. *Energy and Fuels*; **2012**, 26(7), 4321-4327.

(29) Puntervold, T.; Strand, S.; Austad, T. Water Flooding of Carbonate Reservoirs: Effects of a Model Base and Natural Crude Oil Bases on Chalk Wettability. *Energy and Fuels* **2007**, 21 (3), 1606−1616.

(30) Hollingsworth, C. A.; Seybold, P. G.; Hadad, C. M. Substituent Effects on the Electronic Structure and PKa of Benzoic Acid. *Int. J. Quantum Chem.* **2002**.

(31) Heberling, F.; Trainor, T. P.; Lützenkirchen, J.; Eng, P.; Denecke, M. A.; Bosbach, D. Structure and Reactivity of the Calcite-Water Interface. *J. Colloid Interface Sci.* **2011**, *354* (2), 843–857.

(32) Martínez, L.; Andrade, R.; Birgin, E. G.; Martínez, J. M. Software News and Update Packmol: A Package for Building Initial Configurations ForMolecular Dynamics Simulations. *J. Comput. Chem.* **2009**, *30* (13), 2157–2164.

(33) Xiao, S.; Edwards, S. A.; Gräter, F. A New Transferable Forcefield for Simulating the Mechanics of CaCO 3 Crystals. *J. Phys. Chem. C* **2011**, *115* (41), 20067–20075.

(34) William, L. J.; Jayaraman, C.; Jeffry, D. M.; Roger, W. I.; Michael, L. K. Comparison of Simple Potential Functions for Simulating Liquid Water. *J. Chem. Phys.* **1983**, *79* (2), 926–935.

(35) Wang, S.; Feng, Q.; Zha, M.; Javadpour, F.; Hu, Q. Supercritical Methane Diffusion in Shale Nanopores: Effects of Pressure, Mineral Types, and Moisture Content. *Energy and Fuels* **2018**, 32(1), 169-180.

(36) Chen, H.; Panagiotopoulos, A. Z.; Giannelis, E. P. Atomistic Molecular Dynamics Simulations of Carbohydrate-Calcite Interactions in Concentrated Brine. *Langmuir* **2015**, *31* (8), 2407–2413.

(37) Santos, M. S.; Franco, L. F. M.; Castier, M.; Economou, I. G. Molecular Dynamics Simulation of N-Alkanes and CO2 Confined by Calcite Nanopores. *Energy and Fuels* **2018**, 32(2), 1934-1941.

(38) Mutisya, S. M.; Kirch, A.; De Almeida, J. M.; Sánchez, V. M.; Miranda, C. R. Molecular Dynamics Simulations of Water Confined in Calcite Slit Pores: An NMR Spin Relaxation and Hydrogen Bond Analysis. *J. Phys. Chem. C*

2017, 121 (12), 6674−6684.

(39) Damm, W.; Frontera, A.; Tirado-Rives, J.; Jorgensen, W. L. OPLS All-Atom Force Field for Carbohydrates. *J. Comput. Chem.* 1997, 18 (16), 1955−1970.

(40) Jorgensen, W. L.; Maxwell, D. S.; Tirado-Rives, J. *Development and Testing of the OPLS All-Atom Force Field on Conformational Energetics and Properties of Organic Liquids*; 1996, 118, 11225−11236.

(41) Steve Plimton. Fast Parallel Algorithms for Short-Range Molecular Dynamics. *J. Comput. Phys.* 1995, 117 (1), 1−19.

(42) Nosé, S. A Unified Formulation of the Constant Temperature Molecular Dynamics Methods. *J. Chem. Phys.* 1984, 81 (1), 511.

(43) Hoover, W. G. Canonical Dynamics: Equilibrium Phase-Space Distributions. *Phys. Rev. A* 1985, 31 (3), 1695−1697.

(44) Koleini, M. M.; Badizad, M. H.; Ayatollahi, S. An Atomistic Insight into Interfacial Properties of Brine Nanofilm Confined between Calcite Substrate and Hydrocarbon Layer. *Appl. Surf. Sci.* 2019, 490, 89−101.

(45) Fenter, P.; Sturchio, N. C. Calcite (1 0 4)--Water Interface Structure, Revisited. *Geochim. Cosmochim. Acta* 2012, 97, 58−69.

(46) Fenter, P.; Kerisit, S.; Raiteri, P.; Gale, J. D. Is the Calcite-Water Interface Understood? Direct Comparisons of Molecular Dynamics Simulations with Specular X-Ray Reflectivity Data. *J. Phys. Chem. C* 2013, 117 (10), 5028−5042.

(47) Ukrainczyk, M.; Greiner, M.; Elts, E.; Briesen, H. Simulating Preferential Sorption of Tartrate on Prismatic Calcite Surfaces. *CrystEngComm* 2015, 17(1), 149-159.

(48) Ghatee, M. H.; Koleini, M. M. Bonding, Structural and Thermodynamic Analysis of Dissociative Adsorption of H3O+ Ion onto Calcite (10 1 ¯ 4) Surface: CPMD and DFT Calculations. *J. Mol. Model.* 2017, 23 (12), 331.

(49) Kirch, A.; Mutisya, S. M.; Sánchez, V. M.; De Almeida, J. M.; Miranda, C. R. Fresh Molecular Look at Calcite-Brine Nanoconfined Interfaces. *J. Phys. Chem. C* 2018, 122 (11), 6117−6127.

(50) Spagnoli, D.; Cooke, D. J.; Kerisit, S.; Parker, S. C. Molecular Dynamics Simulations of the Interaction between the Surfaces of Polar Solids and Aqueous Solutions. *J. Mater. Chem.* 2006, 16 (20), 1997.

(51) Bourg, I. C.; Lee, S. S.; Fenter, P.; Tournassat, C. Stern Layer Structure and Energetics at Mica--Water Interfaces. *J. Phys. Chem. C* 2017, 121 (17), 9402−9412.

(52) Cazade, P. A.; Hartkamp, R.; Coasne, B. Structure and Dynamics of an Electrolyte Confined in Charged Nanopores. *J. Phys. Chem. C* 2014, 118 (10), 5061−5072.

(53) Koleini, M. M. M. M.; Mehraban, M. F. M. F.; Ayatollahi, S. Effects of Low Salinity Water on Calcite/Brine Interface: A Molecular Dynamics Simulation Study. *Colloids Surfaces A Physicochem. Eng. Asp.* 2018, 537, 61−68.

(54) Brodholt, J. P. Molecular Dynamics Simulations of Aqueous NaCl Solutions at High Pressures and Temperatures. *Chem. Geol.* 1998, 151 (1−4), 11−19.

(55) Wang, P.; Jia, Y.; Li, T.; Hou, D.; Zheng, Q. Molecular Dynamics Study on Ions and Water Confined in the Nanometer Channel of Friedel’s Salt: Structure, Dynamics and Interfacial Interaction. *Phys. Chem. Chem. Phys.* 2018, 20 (42), 27049−27058.

(56) Dongshuai, H.; Zeyu, L.; Peng, Z.; Qingjun, D. Molecular Structure and Dynamics of an Aqueous Sodium Chloride Solution in Nano-Pores between Portlandite Surfaces: A Molecular Dynamics Study. *Phys. Chem. Chem. Phys.* **2016**, *18* (3), 2059–2069.

(57) Franco, L. F. M.; Castier, M.; Economou, I. G. Anisotropic Parallel Self-Diffusion Coefficients near the Calcite Surface: A Molecular Dynamics Study. *J. Chem. Phys.* **2016**, *145* (8).

(58) Ricci, M.; Spijker, P.; Stellacci, F.; Molinari, J. F.; Voïtchovsky, K. Direct Visualization of Single Ions in the Stern Layer of Calcite. *Langmuir* **2013**, *29* (7), 2207–2216.

(59) Al Mahrouqi, D.; Vinogradov, J.; Jackson, M. D. Zeta Potential of Artificial and Natural Calcite in Aqueous Solution. *Advances in Colloid and Interface Science.* **2017**, *240*, 60–76.

(60) Alroudhan, A.; Vinogradov, J.; Jackson, M. D. Zeta Potential of Intact Natural Limestone: Impact of Potential-Determining Ions Ca, Mg and SO4. *Colloids Surfaces A Physicochem. Eng. Asp.* **2016**, *493*, 83–98.

![](./images/812702486304391170_2.jpg)

Figure 1. Density profile of: a-c. oxygen and hydrogen atoms of water (Ow/Hw), benzoates (Bz) and, d-e. $Na^+/Cl^-$ ions in different brines. Maxima of water density (based on Ow) and Bz are outlined in figures d and e for the sake of clarification of position of ions. The data was averaged over both calcite slabs but presented for one of the interfaces.

![](./images/812702486304391170_3.jpg)

Figure 2. a. The RDF between sodium ion and different O-atoms. b. Charge density variation over the calcite slab at different brine salinities (the values are averaged over both slabs and presented for one; the negative layer is closed up to show the smooth charge of LS).

![](./images/812702486304391170_4.jpg)

Figure 3. Radial distribution function revealing interaction between benzoates at the
calcite/brine a. at the interface and b. in the bulk.

![](./images/812702486304391170_5.jpg)

Figure 4. Radial distribution function for the interactions between Na⁺ ions and benzoates a. at the interface and b. in the bulk of calcite/brine system.

![](./images/812702486304391170_6.jpg)

Figure 5. Radial distribution function of $Na^+-Cl^-$ interactions at the interface and bulk of calcite/brine system.

![](./images/812702486304391170_7.jpg)

Figure 6. The survival probability of benzoates at the
a. calcite/brine interface and b. bulk along with
corresponding residence times (c).

![](./images/812702486304391170_8.jpg)

Figure 7. a. Schematic representation of angles $\theta$ and $\phi$ definition; The distribution of angles b. $\theta$ and c. $\phi$ over the calcite surface.

![](./images/812702486304391170_9.jpg)

Figure 8. 2D lateral density profile of $Cl^-$, $Na^+$, and benzoates at the calcite/brine interface.

![](./images/812702486304391170_10.jpg)

Figure 9. The superposition of Na⁺ lateral distribution over the outermost calcite layer.

![](./images/812702486304391170_11.jpg)

Figure 10. Fraction of benzoates at the interface that pair to $Na^+$ ions of the Stern layer. (inset: Schematic representation of the ability of $Na^+$ ions to serve as a potential adsorption site for benzoates onto calcite.)

![](./images/812702486304391170_12.jpg)

TOC Graphic