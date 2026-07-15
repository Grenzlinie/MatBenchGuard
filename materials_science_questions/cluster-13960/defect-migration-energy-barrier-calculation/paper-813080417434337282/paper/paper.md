![](./images/813080417434337282_1.jpg)

Subscriber access provided by READING UNIV

Article

# First-principles study of the voltage profile and mobility of Mg intercalation in a chromium oxide spinel

Tina Chen, Gopalakrishnan Sai Gautam, Wenxuan Huang, and Gerbrand Ceder

*Chem. Mater.*, Just Accepted Manuscript • DOI: 10.1021/acs.chemmater.7b04038 • Publication Date (Web): 06 Dec 2017

Downloaded from http://pubs.acs.org on December 14, 2017

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a free service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are accessible to all readers and citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/813080417434337282_2.jpg)

Chemistry of Materials is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# First-principles study of the voltage profile and mobility of Mg intercalation in a chromium oxide spinel

Tina Chen, $^{\dagger,\ddagger}$ Gopalakrishnan Sai Gautam, $^{\S,\ddagger}$ Wenxuan Huang, $^{\S,\ddagger}$ and Gerbrand Ceder, $^{\dagger,\ddagger}$

$^{\dagger}$Department of Materials Science and Engineering, University of California, Berkeley, California 94720, USA
$^{\ddagger}$Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, California 94720, USA
$^{\S}$Department of Materials Science and Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA

## Abstract

The development of Mg batteries, which can potentially achieve higher energy densities than Li-ion systems, is in need of cathodes that can reversibly intercalate $Mg^{2+}$ and exhibit a higher energy density than the state-of-the-art Chevrel and thio-spinel cathodes. Recent theoretical and experimental studies indicate that the oxide spinel family presents a set of promising Mg cathodes. Specifically, in this work, we investigate Mg intercalation into the spinel-$Mg_xCr_2O_4$ system. Using first-principles calculations in combination with a cluster expansion model and the nudged elastic band theory, we calculate the voltage curve for Mg insertion at room temperature and the activation barriers for Mg diffusion, respectively, at different Mg concentrations in the $Cr_2O_4$ structure. Our results identify a potential limitation to Mg intercalation in the form of stable Mg-vacancy orderings in the $Cr_2O_4$ lattice, which exhibit high migration barriers for Mg diffusion in addition to a steep voltage change. Additionally, we propose cation substitution as a potential mechanism that can be used to suppress the formation of the stable Mg-vacancy ordering, which can eventually enable the practical usage of $Cr_2O_4$ as a Mg-cathode.

## Introduction

Multivalent (MV) batteries, which pair a non-dendritic metal anode, such as Mg, with a high-capacity cathode, are a promising pathway to achieving higher energy density, improved safety, and reduced costs compared to conventional Li-ion batteries. However, MV batteries currently face challenges in the form of incompatible electrolytes with limited anodic stability¹ and cathodes with either poor MV ion mobility or low energy density.²,³ For example, the state-of-the-art Mg-batteries employ low-voltage sulfide cathodes, such as the Chevrel-Mo₆S₈ ⁴ or the spinel-Ti₂S₄.⁵⁻⁷ Oxide-based MV cathodes, on the other hand, offer the possibility of high energy density, albeit with generally poor MV mobility⁸ and potential conversion side-reactions.²,⁹,¹⁰

One pathway to improving MV mobility in oxides is finding frameworks that host MV ions in an "un-preferred" coordination environment, such as a spinel that hosts Mg in a tetrahedral environment instead of the preferred octahedral environment.⁸,¹¹,¹² Indeed, a recent study has demonstrated facile Mg-transport in ternary chalcogenide spinels, with potential applications as Mg solid electrolytes.¹³,¹⁴

Spinel oxides are described by a general formula of $AM_2O_4$, where A and M are the MV cation ($Mg^{2+}$ in this work) and the transition metal cation (e.g., $Cr^{3+/4+}$) respectively. They have long been used for Li cathode applications¹⁵⁻²⁰ and are also expected to exhibit both reasonable Mg diffusion and high energy density.²¹ An example of a promising spinel oxide cathode is $Mn_2O_4$, which is one of the few oxides that can intercalate $Mg^{2+}$ electrochemically,²²⁻²⁴ albeit poorly, and exhibits a good voltage (~2.9 V), high theoretical capacity (~270 mAh/g), and reasonable Mg migration barriers (~500-600 meV in the dilute vacancy limit).²¹,²⁵ However, a major issue with $Mn_2O_4$ is the tendency of the spinel to undergo "inversion", which is the exchange of the cations in octahedral sites (i.e. $Mn^{3+/4+}$) with the cations in tetrahedral sites (i.e. $Mg^{2+}$).²⁶⁻²⁹ Consequently,

inversion in the spinel structure can cause blockage of Mg percolation paths, which can severely limit both the macroscopic transport of Mg through the cathode particle and the practical capacity that can be extracted. $^{12}$ Notably, the facile disproportionation of $Mn^{3+}$ to $Mn^{4+}$ and $Mn^{2+}$ has been attributed by previous studies to aid inversion in Mn-spinels. $^{16}$

Besides $Mn_2O_4$, spinel-$Cr_2O_4$ is another promising oxide cathode, exhibiting similar theoretical capacity to $Mn_2O_4$ (~280 mAh/g), a significantly higher voltage (~3.6 V), and comparable migration barriers (~600-650 meV). $^{21}$ Furthermore, $Cr^{3+}/Cr^{4+}$ ions tend to strongly prefer 6-fold coordination $^{11,30}$ owing to large crystal field stabilization energies, $^{31,32}$ resulting in $Mg_xCr_2O_4$ being less prone to invert upon Mg (de)intercalation. However, previous studies have reported $Cr^{4+}$ disproportionation into $Cr^{3+}$ and $Cr^{6+},^{33,34}$ the latter of which tends to prefer 4-fold coordination. $^{33,35}$ Additionally, even though previous work has suggested the prevalence of conversion reactions in oxide cathodes, $^{2,9,10}$ we do not expect the $MgCr_2O_4$ system to undergo conversion reactions upon discharge due to the thermodynamic stability of spinel-$MgCr_2O_4$, as determined by the 0 K Mg-Cr-O ternary phase diagram. $^{34,35}$

Spinel $MgCr_2O_4$ has previously been studied for its magnetic properties. $^{36-43}$ In this study, we investigate the properties of Mg intercalation in the $Cr_2O_4$ spinel in detail using first principles calculations. To evaluate the free energy and Mg chemical potential in the material we use the cluster expansion approach, which has been previously used to calculate phase diagrams in Li, $^{44-}$ $^{46}$ Na, $^{47}$ and $Mg^{48}$ intercalation compounds. $^{49}$ The cluster expansion is an expansion on site occupation variables, fit to energies from first principles calculations. The cluster expansion is then combined with Monte Carlo simulations to include configurational entropy in the finite temperature free energy. In this work, we calculate the voltage curve of the $Mg_xCr_2O_4$ system at

room temperature (293 K) as well as at 60°C (333 K) since full cell Mg batteries occasionally employ elevated temperatures up to 60°C.⁴,⁶ Additionally, we evaluate the tendency of the MgₓCr₂O₄ spinel to invert at intermediate Mg concentrations. We also calculate migration barriers at several Mg concentrations in MgₓCr₂O₄ to evaluate the kinetics of the system throughout the intercalation process. Our results indicate the formation of stable Mg-vacancy orderings at cathode compositions of Mg₀.₃₃Cr₂O₄ and Mg₀.₅Cr₂O₄, which can severely limit Mg (de)intercalation owing to steep changes in the voltage and high Mg migration barriers at these compositions. To eventually enable Cr₂O₄ to be used in practical Mg batteries, we propose a few strategies, such as cation substitution, to suppress the formation of the stable orderings at Mg₀.₃₃Cr₂O₄ and Mg₀.₅Cr₂O₄.

## Structure
The MgCr₂O₄ spinel structure, as shown in Figure 1a, is composed of Mg²⁺ occupying tetrahedral 8a sites (orange polyhedra in Figure 1a) and Cr³⁺/Cr⁴⁺ occupying the octahedral 16d sites (blue polyhedra) within a cubic close-packed O²⁻ lattice (32e, vertices of orange and blue polyhedra). In a polyhedral representation, the structure consists of Cr-octahedra that are edge-sharing with other Cr-octahedra and vertex-sharing with Mg-tetrahedra. In any given <110> direction, the spinel structure can be visualized as tunnels, which intersect at regular intervals allowing 3D diffusion of Mg atoms through the structure. Low energy MgₓCr₂O₄ configurations often consist of a combination of fully-occupied, half-occupied, and empty tunnels (Figure 1b).

![](./images/813080417434337282_3.jpg)

Figure 1: (a) Structure of fully magnesiated $MgCr_2O_4$ spinel conventional cell, with Mg in tetrahedral (orange) and Cr in octahedral (blue) coordination. All vertices of polyhedra are occupied by O (not shown). (b) $MgCr_2O_4$ spinel structure demonstrating full, half full, and empty tunnels, as viewed along the <110> direction.

### Methods

To construct the 0 K phase diagram of the MgₓCr₂O₄ system, we use Density Functional Theory (DFT)⁵⁰,⁵¹ as implemented in the Vienna Ab initio Simulation Package (VASP),⁵²,⁵³ using the Perdew-Burke-Ernzerhof (PBE) parametrization⁵⁴ of the generalized gradient approximation (GGA) to describe the electron exchange and correlation. We add a Hubbard $U$ correction of 3.5 eV to the GGA Hamiltonian to remove the spurious self-interaction of the chromium $d$-electrons.⁵⁵⁻⁵⁷ The wave functions are constructed using the projector augmented wave (PAW) theory,⁵⁸ using a well-converged energy cut-off of 520 eV, and sampled on a Monkhorst⁵⁹ $k$-point mesh of density 1000/atom. Additionally, we include the semicore $3p$-electrons along with the valence $4s$ and $3d$ electrons to construct the chromium pseudopotential. Each calculation is converged to within 0.01 meV/formula unit.

To obtain the room-temperature voltage curve, we perform Grand-canonical Monte Carlo (GMC) simulations on a cluster expansion (CE) Hamiltonian, where the CE is an expansion of the total energy of the system in terms of the occupancies on a topology of sites.¹⁸,⁶⁰,⁶¹ In practice, the CE is written as the summation of the interactions of the clusters, where clusters refer to pairs, triplets, quadruplets, etc. of sites, as given in equation 1.

$$
E(\sigma)=\sum_{\alpha} m_{\alpha} V_{\alpha}\left\langle\prod_{i \in \beta} \sigma_{i}\right\rangle \tag{1}
$$

In equation 1, the energy ($E$) of a configuration ($\sigma$) of Mg ions in the Cr₂O₄ lattice is expressed in terms of symmetrically distinct clusters ($\alpha$). Each term in the sum is given by the product of the multiplicity of a cluster $\alpha$ ($m_{\alpha}$) in the spinel lattice, the effective cluster interaction of $\alpha$ ($V_{\alpha}$), and $\prod_{i \in \beta} \sigma_{i}$ , the occupation variable averaged over all clusters $\beta$ that are symmetrically

equivalent to $\alpha$. For each site $i$ within a cluster $\beta$ we assign $\sigma_i = +1$(-1) when $i$ is occupied by Mg (vacancy).

The CE is fit to the total internal energies of ~249 Mg-vacancy (Va) configurations, as obtained via DFT calculations. The Mg-Va configurations are enumerated using the Pymatgen library up to supercells of 64 oxygen at 25%, 50%, and 75% Mg, 24 oxygen at 33% and 66% Mg, and 48 oxygen at 16% and 83%.$^{62,63}$ For the 50% Mg concentration, we took only the 50 configurations with the lowest electrostatic energy, as evaluated by the Ewald sum of the supercell,$^{64}$ due to the large number of enumerations for the 64-oxygen supercell at 50% Mg. We use the split-Bregman algorithm$^{65, 66}$ to identify the set of relevant ECIs and fit them to the total internal energies. Convergence of the CE is verified using an in-house algorithm, as described by Huang *et al.*,$^{67}$ in combination with canonical Monte Carlo simulations. The root mean squared error (RMSE) and the leave-one-out cross-validation (LOOCV) scores are used to quantify the fit quality and the predicative capability, respectively, of the CE. Note that the set of Mg-Va configurations is built assuming no inversion of the spinel, i.e., the Mg/Va occupies only the $8a$ tetrahedral sites.

We perform GMC calculations on 12x12x12 supercells of the primitive rhombohedral spinel cell (corresponding to 3,456 Mg/Va sites), using the Clusters Approach to Statistical Mechanics (CASM) package.$^{68,69}$ The GMC simulations are equilibrated for 40,000 steps and sampled for 100,000 steps. The voltage curve at each temperature is calculated from the chemical potential $\mu_{Mg}$, in the GMC simulations as indicated in Equation 2.$^{70}$

$$
V(x) = -\frac{\mu_{Mg}^{cathode}(x) - \mu_{Mg}^{anode}}{2e} \tag{2}
$$

Thus, the voltage at any Mg concentration $(x)$ in $\text{Mg}_x\text{Cr}_2\text{O}_4$ is described by the difference between $\mu_{Mg}$ at the cathode ($\mu_{Mg}^{cathode}$) and $\mu_{Mg}$ at the anode ($\mu_{Mg}^{anode}$), where $\mu_{Mg}^{cathode}$ is obtained directly from GMC simulations and we consider bulk Mg metal to be the anode. Additionally, we perform thermodynamic free-energy integration as described by Hinuma$^{47}$ and Van de Walle$^{71}$ to correct for hysteresis in the Monte Carlo scans. Specifically, we perform the free energy integration between 0% Mg and 100% Mg and between 25% Mg and 50% Mg (see Supplementary Information S1.3).

We calculate the activation barriers to Mg migration in structures with 33% and 50% Mg concentration as well as in the dilute Mg and dilute vacancy limits using DFT-based Nudged Elastic Band (NEB) calculations, $^{72,73}$ with forces converged within 50 meV/Å. For the dilute Mg and dilute vacancy cases, we consider a single Mg (vacancy) migrating to a nearby empty (occupied) Mg site. For the 33% Mg and 50% Mg cases, we consider two cases, namely addition of a vacancy (+Va) and an interstitial Mg atom (+Mg) to the stable ordered structure. For +Va, we create a vacancy in one of the Mg-occupied $8a$ sites within the 33% and 50% Mg structures and consider the migration of the vacancy to an equivalent Mg-occupied $8a$ site. For +Mg, we insert an additional Mg in an $8a$ site that is unoccupied in the ground state ordering. In the case of the 33% Mg structure with +Mg, we consider specifically the migration of the +Mg in an empty tunnel so that +Mg moves to an adjacent unoccupied $8a$ site. For +Mg in the 50% Mg structure, the +Mg moves to an adjacent Mg-occupied $8a$ site concurrently with the migration of the Mg in the occupied $8a$ site to an interstitial $8a$ site (see Supplementary Information S1.6).

For the DFT-based NEB calculation, we use both the GGA functional and the GGA+$U$ (GGA with Hubbard $\underline{U}$ correction) functional. Convergence of GGA+$U$ NEB calculations can be

problematic due to the possible metastability of electronic states along the migration path in GGA+$U$, which is a functional that enforces electron localization. As an ion moves along the migration path the specific transition metal ion where the electron localizes may change. The transition of the electron from one state to another is typically not adiabatic in GGA+$U$ and due to the metastability of electron occupation in the method. In some cases, the electron even fails to localize which leads to a very large positive energy contribution from the $+U$ term. These problems with metastable charge density in GGA+$U$ can make convergence of NEB with this functional problematic. Nominally, the barriers for electrons to migrate across redox centers is lower compared to ionic migration, $^{74,75}$ indicating that ionic migration is the kinetic rate-limiting step, especially in MV systems, $^{2,21,76}$ giving some support for an adiabatic approach to the ion migration problem. Here we have successfully converged NEB calculations for the Mg-$Cr_2O_4$ system using the GGA+$U$ functional and consider both the GGA and GGA+$U$ barriers in the discussion.

## Results

### Cluster Expansion

![](./images/813080417434337282_4.jpg)

Figure 2: (a) DFT (green) and CE-predicted (yellow) formation energies and convex hulls, with the DFT convex hull delineated by a black line and the CE-predicted convex hull by a red line. The ground states are outlined in black (DFT GS) or red (CE GS). (b) Plot of CE error and DFT energy above hull per formula unit (f.u.). The blue dashed box encloses structures within 10 meV CE error and 50 meV off the convex hull, while the red dashed box encloses structures within 20 meV CE error and 100 meV off the convex hull.

Figure 2a plots the DFT (green circles) and CE-predicted (yellow circles) formation energies ($E_{\text{formation}}$) of all 249 Mg-Va configurations at different $\text{x}_{\text{Mg}}$. The energies in Figure 2a are referenced to the DFT-energies of the empty-$\text{Cr}_2\text{O}_4$ and magnesiated-$\text{MgCr}_2\text{O}_4$ configurations.

As indicated by the convex ground state hull from DFT calculations (solid black line in Figure 2a), there are several stable DFT ground states (green circles with a black outline) at various Mg concentrations. The convex hull is mainly shaped by the ground states at 33% Mg and 50% Mg (see configurations in insert of Figure 3 and more detailed crystallographic information in

Supplementary Information 1.2), with both configurations exhibiting $E_{\text{formation}}$ of $-120$ to $-130$ meV/f.u. There are also numerous ground states that appear to lie near the linear interpolation between the 16% and 33% Mg ground states and between the 50% and 83% Mg ground states (see Figure 3). The $\text{Mg}_x\text{Cr}_2\text{O}_4$ CE, described with 29 clusters, predicts a similar convex hull as compared to the DFT calculations (solid red line in Figure 2a), resulting in a RMSE of 8 meV/f.u. and a LOOCV of 13 meV/f.u., indicating both good quality and predictive capability of the CE fit. The CE energies and DFT energies and ground state hulls match relatively well, with the CE convex hull matching 6 out of the 10 ground states in the DFT convex hull. Further, of the DFT ground states that are not CE ground states and the CE ground states that are not DFT ground states, the CE predicts the $E_{\text{formation}}$ of the configurations with an error of less than 3 meV except for configurations with Mg concentration below 10%.

We further evaluate the performance of the cluster expansion by calculating the error between the CE-predicted and DFT $E_{\text{formation}}$ and plot it against the energy above hull in Figure 2b. The energy above hull ($E^{\text{hull}}$) of a structure is given by the energy of decomposition into stable ground states. Structures with $E^{\text{hull}} = 0$ are stable, while structures with low $E^{\text{hull}}$ are most important for the excitation spectrum at finite temperatures. From Figure 2b, the energies of structures within 50 meV/f.u. off the convex hull are generally predicted by the cluster expansion with an error of less than 10 meV/f.u. Notably the CE predicts $E_{\text{formation}}$ of a majority of high $E^{\text{hull}}$ (up to 100 meV/f.u.) structures with an error of less than 20 meV/f.u. Additionally, the CE tends to underestimate $E_{\text{formation}}$ of structures at low Mg concentration (Figure 2a).

In Figure 3, we plot the energy below the tie-line ($E_{\text{tie-line}}$) for each ground state configuration, where the $E_{\text{tie-line}}$ of a ground state is given by the $E_{\text{formation}}$ of the ground state referenced to the

stable states at adjacent Mg compositions. For example, the adjacent stable states for the 33% Mg ground state (with $E_{\text{formation}} \sim -128$ meV/f.u.) are the 25% Mg ($E_{\text{formation}} \sim -114$ meV/f.u.) and the 50% Mg ($E_{\text{formation}} \sim -119$ meV/f.u.) ground states. Consequently, $E_{\text{tie-line}}$ of the 33% Mg is given by the difference between $E_{\text{formation}}$ of the 33% Mg ground state and the weighted-sum of the $E_{\text{formation}}$ of 25% Mg and 50% Mg ground states, so $-128\frac{meV}{f.u.} - \left(-114\frac{meV}{f.u.} * \frac{50\%-33\%}{50\%-25\%}\right) - \left(-119\frac{meV}{f.u.} * \frac{33\%-25\%}{50\%-25\%}\right) = 12.3\frac{meV}{f.u.}$. Thus, the $E_{\text{tie-line}}$ quantifies the "depth" of a ground state since it indicates the driving force to form the ground state instead of the stable states at adjacent Mg concentrations. For example, the 33% Mg and 50% Mg ground states with $E_{\text{tie-line}} >$ 10 meV/f.u. would be considered "deep" ground states, while the 25% Mg and 66% Mg ground states with $E_{\text{tie-line}} < 5$ meV/f.u. are considered "shallow" ground states. Indeed, the data in Figure 3 indicate that the deepest ground states are at 33% Mg ($E_{\text{tie-line}} \sim$13 meV/f.u. with respect to the 25% Mg and 50% Mg ground states) and 50% Mg ($E_{\text{tie-line}} \sim$10 meV/f.u. with respect to the 33% Mg and 62.5% Mg ground states). Additionally, there are numerous shallow ($E_{\text{tie-line}} < 5$ meV) Mg-vacancy orderings such as the 16% Mg and 25% Mg orderings as well as the orderings above 50% Mg in both the DFT and CE convex hulls. Shallow ground states are more likely to disappear at elevated temperature unless they have higher entropy than the structures that define their tie-line. The Figure 3 inserts show the structures of the ground states at 33% Mg and 50% Mg, along the <110> direction, with the repeating unit outlined with the white dashed line.

![](./images/813080417434337282_5.jpg)

Figure 3: Plot of $E_{\text{tie-line}}$, which is given by the energy difference between a ground state's $E_{\text{formation}}$ and the tie-line connecting neighbor ground state configurations. The $E_{\text{tie-line}}$ of CE ground states are shown in yellow, and the $E_{\text{tie-line}}$ of DFT ground states are shown in green. The configurations of the ground states at 33% Mg and 50% Mg are also shown, with Cr octahedra and Mg tetrahedra indicated by blue and orange polyhedra, respectively, in the <110> direction. The repeating unit of the ground state configurations are outlined by the dashed white line.

Using Figure 3 to further analyze the performance of the CE vs. DFT, we find that the CE is generally able to predict the $E_{\text{tie-line}}$ of ground states within 2-3 meV/f.u. of the DFT values. In all ground states common between the CE and DFT convex hulls, the CE predicts $E_{\text{tie-line}}$ that are within 5 meV of the DFT $E_{\text{tie-line}}$. Notably, the CE does not predict the DFT ground states at

6.25% Mg, 62.5% Mg, and 75% Mg, as indicated by the lack of yellow bars at those concentrations in Figure 3, while the CE predicts spurious ground states at 78% Mg and 89% Mg.

Because the voltage curve depends primarily on the shape of the convex hull, i.e., changes in slope of $E_{\text{formation}}$ with respect to $\text{x}_{\text{Mg}}$, we choose to trade error in prediction of the exact ground state orderings for lower absolute errors in the ground state $E_{\text{formation}}$.

We additionally investigate the change in volume in the $\text{Mg}_{\text{x}}\text{Cr}_{2}\text{O}_{4}$ system during (de)intercalation in Supplementary Information S1.4.

### Spinel inversion

In building the convex hull and CE, we only considered the non-inverted normal-$\text{MgCr}_{2}\text{O}_{4}$ spinel. However in oxide spinels such as $\text{Mg}_{\text{x}}\text{Mn}_{2}\text{O}_{4}$, the structure can invert during Mg (de)intercalation whereby the Mn moves to the $8a$ tetrahedral sites and can block the percolation of Mg through the structure.$^{12}$ Analogously in $\text{Mg}_{\text{x}}\text{Cr}_{2}\text{O}_{4}$, inversion will involve the movement of a Cr in a $16d$ site to an $8a$ site. We briefly investigate the possibility of the $\text{Mg}_{\text{x}}\text{Cr}_{2}\text{O}_{4}$ spinel inverting during intercalation, which is likely either by the migration of the $\text{Cr}^{4+}$ to the $8a$ tetrahedral site$^{11}$ or by disproportionation of $\text{Cr}^{4+}$ to $\text{Cr}^{3+}$ and $\text{Cr}^{6+}$ and the subsequent migration of $\text{Cr}^{6+}$ to the $8a$ tetrahedral site.$^{33, 35}$

Since inversion tends to occur commonly at intermediate intercalant concentrations$^{12, 77}$ with disproportionation in $\text{Cr}_{2}\text{O}_{4}$ requiring the presence of $\text{Cr}^{4+}$, a likely ground state configuration that might be susceptible to inversion is $\text{Mg}_{0.33}\text{Cr}_{2}\text{O}_{4}$. As a result, we investigate the energies of potential inverted configurations$^{12, 78}$ and the kinetic barriers to Cr migration to the $8a$ site at the 33% Mg ground state. For the 33% Mg ground state, we calculate the energies of all symmetrically distinct configurations in a unit cell with 24 oxygen ions whereby one $\text{Cr}^{4+}$

exchanges with either a vacancy or a $Mg^{2+}$ in a vertex-sharing $8a$ site. We also calculate the migration barrier using NEB for Cr diffusion to the lowest energy structure among the structures resulting from a $Cr^{4+}$ exchange.

![](./images/813080417434337282_6.jpg)

Figure 4: (a) Comparison of $E_{formation}$ of the 33% Mg ground state (black) and structures with a single exchange of a $Cr^{4+}$ to an empty $8a$ Mg site (green) or an occupied 8a Mg site (yellow). The lowest Cr-Va and Cr-Mg exchanged configurations are shown in black in their respective column while higher-energy structures are shown in color. (b) Activation barrier for Cr diffusion in the 33% Mg configuration (Figure 3 insert) to the lowest-energy tetrahedral vacancy. The configuration resulting from the Cr diffusion corresponds to the black dashed line in the Cr-Vacancy exchange column in (a). The migration barrier is given by the maximum of the energy along the path in (b).

We additionally consider the possibility of $Cr^{4+}$ disproportionation ($3\ Cr^{4+} \rightarrow 2\ Cr^{3+} +\ Cr^{6+}$) as the resulting $Cr^{6+}$ ions prefer tetrahedral coordination. To this end, we initialize the Cr atom in the $8a$ site with a low magnetic moment (~0 Bohr-Magneton) in our calculations, which indicates a $Cr^{6+}$ ion. In all calculations of the inverted structures, the magnetic moment on the

inverted Cr in the tetrahedral site relaxed to ~2.3 Bohr-Magnetons, suggesting a 4+ charge indicating that disproportionation does not occur.

Figure 4a compares the formation energy of the non-inverted 33% Mg ground state (black) with the configurations resulting from all possible exchanges of a single $Cr^{4+}$ with either an empty (green) or an occupied (yellow) Mg site. Structures where $Cr^{4+}$ moves into an occupied Mg site have $E_{formation}$ ~ 60 meV/f.u. higher than that of the non-inverted ground state, while structures where $Cr^{4+}$ moves into an empty Mg site have $E_{formation}$ ~ 20-40 meV/f.u. higher than that of the ground state. Thus, inversion due to exchange between a $Cr^{4+}$ and an occupied Mg site is unlikely to occur in the 33% Mg ordering, but the inverted structure in which $Cr^{4+}$ moves to an empty Mg site may be slightly more thermodynamically accessible at room temperature.

Figure 4b shows the NEB-calculated energy profile for $Cr^{4+}$ diffusing from an octahedral site to a low energy vacancy site. The energies in Figure 4b are referenced to the initial ground state configuration (0% path distance), with the migration barrier of the given trajectory indicated by the maximum in the corresponding energy profile. From Figure 4b, the migration barrier to Cr diffusion is ~2240 meV. In general, at room temperature, we do not expect to see any hops with migration barriers over 2 eV, so we do not expect Cr inversion to occur at the 33% Mg concentration based on kinetics. Thus, despite the small energy difference (~ 20 meV) between the 33% Mg ground state and the same configuration with an additional $Cr^{4+}$ exchanged with a vacancy, the high kinetic barrier to Cr inversion makes Cr inversion unlikely.

Voltage-composition curve

![](./images/813080417434337282_7.jpg)

Figure 5: Calculated voltage curves for Mg (de)intercalation in MgₓCr₂O₄, including the theoretical DFT (0 K) voltage curve, the CE-predicted 0 K voltage curve, and the room temperature (293 K) Monte Carlo-calculated voltage curve, given by the dashed green, dashed yellow, and solid black lines, respectively.

Figure 5 plots the voltage for Mg intercalation as a function of $x_{Mg}$ in the $Cr_2O_4$ lattice at 0 K (dashed lines in Figure 5) and 293 K (solid black line). For comparison, we plot the 0 K voltage curve as obtained directly through DFT calculations (green dashed line) and our CE model (yellow dashed line) in Figure 5. Note that the voltage plateaus (such as between 33% and 50% Mg) in Figure 5 correspond to 2-phase regions while voltage steps (at 50% Mg for example) correspond to specific ground state configurations. Also, the magnitude of the voltage step at a

specific Mg concentration corresponds loosely to the depth of the ground state configuration (see Figure 3).

The DFT voltage curve has a multitude of voltage steps, with the small steps (< 0.05 V) originating from the numerous shallow ground state orderings and the largest steps of 0.42 V, 0.20 V, 0.22 V, and 0.15 V originating from the 6.25% Mg, 8.3% Mg, 33% Mg, and 50% Mg ground state configurations, respectively. The large voltage steps at 33% Mg and 50% Mg are in agreement with the deep 33% Mg and 50% Mg ground states and suggest that the 33% and 50% Mg ground states may limit intercalation.⁷⁹ The 0 K voltage curve calculated by the CE agrees broadly with the DFT curve except for absent voltage steps at 6.25% Mg, 62.5% Mg, and 75% Mg and spurious voltage steps at 78.9% Mg and 88.9% Mg, consistent with the data from Figure 2 and Figure 3.

At 293 K, the voltage curve essentially follows the trends displayed by the 0 K CE curve, with noticeable differences at low Mg (< 20%) and high Mg (> 85%) concentrations. For example, between 10% Mg and 22% Mg, the voltage steps at 8.33% and 16.67% Mg are smoothed into a continuous curve. The smoothing behavior comes from the increase in configurational entropy as temperature increases, which disorders the weakly-ordered ground states, leading to a solid-solution behavior. We additionally note that an artificial ground state appears at 75% Mg in the Monte Carlo at 293 K, indicated by the sharp voltage step at 75% Mg concentration. Specifically, the Monte Carlo calculation discovers a new CE ground state at 75% Mg that is not a part of the set of configurations used to fit the CE. Upon DFT calculation, the new 75% Mg configuration is near the convex hull ($E^{\text{hull}}$ ~ 4 meV/f.u.) but not a real DFT ground state and is actually over-stabilized by the CE by ~10 meV/f.u., which is within the 13 meV/f.u. LOOCV error of the CE.

Due to the small $E^{\text{tie-line}}$ of the ground states between 50% Mg and 83% Mg, the overstabilization of the new 75% Mg configuration causes that configuration to become a strong ground state in the CE. Thus, the 75% Mg voltage jump is an artifact of our cluster expansion. From Figure 5, we calculate the average voltage for Mg intercalation to be 3.6 V in $\text{Cr}_2\text{O}_4$, consistent with previous theoretical studies.$^{21}$ Also, the voltage curve at 333 K, as shown in Figure S6 of the Supplementary Information, appears largely unchanged from the 293 K voltage curve. Notably, the 33% and 50% Mg steps are retained even at an elevated temperature of $60^o$ C. We subsequently investigate Mg mobility within the $\text{Cr}_2\text{O}_4$ framework by calculating the migration barriers for Mg diffusion within the deep 33% and 50% Mg ground states, which will be encountered during Mg intercalation.

NEB barriers

To analyze the ease of Mg mobility in the $\text{Cr}_2\text{O}_4$ lattice at different levels of (de)intercalation, we perform NEB calculations at several Mg concentrations, including 0% Mg (dilute Mg limit), 33% Mg, 50% Mg, and 100% Mg (dilute Va limit). In each of the cases, we consider the migration path typical of Mg in tetrahedral sites of the spinel (Figure 6a). In the path depicted in Figure 6a, the Mg migrates from a tetrahedral site (A) through a triangular face (B) shared by the tetrahedral with an empty octahedral site (C) to the empty octahedral site and then through another triangular face (B', not shown in Figure 6a) to the final tetrahedral site (D). In the dilute Mg (Va) limit, we consider a single Mg (Va) diffusing through the empty (magnesiated) $\text{Cr}_2\text{O}_4$ host, along the trajectory shown in Figure 6a-b. To evaluate Mg migration in the 33% and 50% Mg configurations, we considered the ground state configurations (Figure 3 insert and Supplementary Information S1.2) and introduce either an additional vacancy (+Va) in the Mg-occupied $8a$ sites (Figure 6c-d, yellow-outlined path) or an additional Mg (+Mg) in one of the

unoccupied $8a$ sites (Figure 6c orange-outlined path and Supplementary Information S1.6). In the case where we add +Va, we evaluate the barrier for a Mg to migrate to the vacant $8a$-site added to the ground state configuration. In the case where we add +Mg, for the 33% Mg ground state, we evaluate the barrier for the +Mg to migrate to an adjacent vacant $8a$-site in the empty tunnel (see insert in Figure 3). Because the paths are symmetric (i.e., (1) to (2) is equivalent to (2) to (Va) in Figure 6b-d), we perform an NEB calculation on half of the full migration path (from (1) to (2)). For the above calculations we use 7 images to represent the migrating Mg along the diffusion paths. For the 50% Mg with +Mg, the path is slightly more complex and is explained further in Supplementary Information S1.6.

![](./images/813080417434337282_8.jpg)

Figure 6: (a) The typical migration path between tetrahedral Mg is indicated by the white dashed line, and positions of note are marked by gray circles. Mg moves from the tetrahedral site (A) through a triangular face (B) shared between the tetrahedral site and an empty octahedral site (C) to the empty octahedral site. It then migrates from the empty octahedral site through another triangular face (B', not shown) leading to the final tetrahedral site (D). (b) The migration barriers are calculated based on the path from the initial (1) to the final (2) endpoints, indicated by green labeled triangles, and represent half of the migration path. (c) The 33% Mg and (d) 50% Mg structures are shown with example migration paths, with yellow arrows in each panel indicating the direction of Mg movement. Migration paths involving an added vacancy are outlined in yellow with the added vacancy labeled 'Va', and migration paths involving an added Mg are outlined in orange with the added Mg labeled 'Mg'.

![](./images/813080417434337282_9.jpg)

Figure 7: The activation barriers for Mg diffusion in the dilute Mg, 33% Mg with additional vacancy (+Va), 33% Mg with additional Mg (+Mg), 50% Mg with additional vacancy (+Va), 50% Mg with additional Mg (+Mg), and dilute vacancy configurations are displayed. NEB barriers calculated in GGA are given by green bars while those calculated in GGA+$U$ are colored in yellow.

Figure 7 shows the NEB DFT-calculated migration barriers for all configurations (dilute Mg, 33% Mg with +Va, 33% Mg with +Mg, 50% Mg with +Va, 50% Mg with +Mg, and dilute Va) using the GGA functional (in green in Figure 7) and the GGA+$U$ functional (in yellow in Figure 7). Additionally, a direct comparison between NEB barriers and energy profiles calculated using GGA and GGA+$U$ for each configuration is shown in Figure S8 in the Supplementary Information. From Figure 7, the GGA barriers of ~730 meV and ~600 meV at the dilute Mg and dilute Va limits agree with the literature values of ~600-700 meV.²¹ The 33% Mg and 50% Mg NEB barriers, which have not been previously reported, are ~920 and ~790 meV with +Va and ~670 meV and ~970 meV with +Mg, respectively. Further, the energy profiles (Figure S5 in the

Supplementary Information) is in agreement with previous studies regarding the shape of the energy profile, with maxima at the triangular faces (B and B' in Figure 6a).$^{21}$

Based on the NEB energy profiles calculated using the GGA+$U$ functional in Figure 7, the dilute Va limit and 33% Mg with +Mg have the lowest barrier (~690 meV and ~700 meV, respectively) among the GGA+$U$ migration barriers calculated (similar to the ~600 meV and 670 meV migration barriers calculated in GGA). In the dilute Mg, 33% Mg with +Va, and 50% Mg with +Va and with +Mg configurations, GGA+$U$ predicts a significantly higher Mg migration barrier than GGA. Specifically, GGA+$U$ predicts barriers of ~930 meV for the dilute Mg configuration, ~1250 meV for the 33% Mg configuration with +Va, ~980 meV for the 50% Mg configuration with +Va, and ~1200 meV for the 50% Mg configuration with +Mg, which are respectively ~200 meV, ~320 meV, ~200 meV, and ~250 meV higher than their GGA counterparts. Further comparing the GGA and GGA+$U$ energy profiles in Supplementary Information S1.7, it is notable that the end states of the 33% Mg with +Va and 50% Mg with +Va paths are ~300-350 meV higher than the initial states in GGA+$U$ but not in GGA, reflecting the fact that GGA+$U$ and GGA tend to give quite different ordering profiles (further shown in Supplementary Information S1.8). Because of the forced charge localization in GGA+$U$, screening is not as effective as in GGA, and ordering is more pronounced, leading to stronger effective ordering interactions. Similar effects have also been seen in Na$_x$CoO$_2$.$^{47}$ In general, GGA orderings seem to be closer to experimental observations, except in systems where electron localization is very pronounced.$^{80}$

To contextualize the magnitude of migration barriers, previous work has shown that barriers around 600-750 meV and below can yield reasonable diffusivity for a 100 nm cathode particle

under Mg-electrochemical conditions.² Based on the range of reasonable migration barriers (600-750 meV), the dilute Va and 33% Mg with +Mg migration barriers are within the limits of reasonable diffusion in both GGA and GGA+$U$, indicating that initial Mg deintercalation from a chemically-synthesized MgCr₂O₄ should be facile under electrochemical conditions. However, both GGA and GGA+$U$ migration barriers at lower Mg concentrations, specifically for 50% Mg with +Mg and with +Va and 33% Mg with +Va are above the upper limit of 750 meV, signifying that Mg extraction will be difficult beyond Mg₀.₅Cr₂O₄.

## Discussion

The MgₓCr₂O₄ system is an appealing system due to its high theoretical capacity (280 mAh/g) and high average voltage (3.6 V). The NEB calculation and room temperature voltage curve suggest that initial deintercalation until the system is 50% deintercalated is largely uninhibited based on the reasonable (~690 meV in GGA+$U$) migration barrier and the smooth voltage profile at x_Mg > 0.5. Significant barriers to deintercalation appear at the 33% Mg and 50% Mg concentrations in the form of > 900 meV diffusion barriers (in GGA+$U$) and large voltage jumps of 0.22 V and 0.14 V, respectively. Similar thermodynamic barriers in the form of stable orderings have been shown to inhibit intercalation in analogous systems, such as Li in LiₓCoO₂,⁸¹ Mg in layered-V₂O₅,⁴⁸,⁷⁶ and Mg in a Chevrel phase cathode Mo₆S₈.⁸² Thus, while Mg migration may be feasible upon initial charging from the fully-magnesiated state, Mg becomes virtually immobile after ~50% of the Mg is removed. Further, the 33% and 50% Mg configurations remain stable at elevated temperatures, as the voltage steps do not decrease at the respective concentrations at 333 K (Figure S6 in Supplementary Information). Thus, while operating at elevated temperatures is one way to improve cation mobility, the operating temperature will need to be raised significantly higher than 60° C to destabilize 33% Mg and 50% Mg ground states,

which may be beyond the stability limits of current organic Mg-electrolytes. Additionally, we note the difficulties of charging $Mg_xCr_2O_4$ to low Mg concentrations (< 33%) as the voltage extends beyond the electrolyte cathodic stability limit (~3-3.5V) typical in Mg-systems. $^{1,2}$

Another potential issue is the instability of demagnesiated states of the $Mg_xCr_2O_4$ system. Based on the ternary Mg-Cr-O phase diagram calculated by the Materials Project, $^{62, 83}$ the demagnesiated spinel-$Cr_2O_4$ has a relatively high $E^{hull}$ at ~187 meV/atom with respect to rutile $CrO_2$, which is a ground state of the Mg-Cr-O phase diagram. $^{83}$ Further, the intermediate $Mg_xCr_2O_4$ phases lie on the rutile $CrO_2$-spinel $MgCr_2O_4$ tie-line, indicating that they have a driving force to decompose to those ground state phases. We calculated the intermediate $Mg_{0.33}Cr_2O_4$ and $Mg_{0.5}Cr_2O_4$ ground state orderings to have $E^{hull}$ of ~100 meV/atom and ~68 meV/atom with respect to the rutile $CrO_2$ and spinel $MgCr_2O_4$ phases. Thus, while the fully magnesiated $MgCr_2O_4$ is a stable ground state, the high $E^{hull}$ of $Cr_2O_4$ and intermediate $Mg_xCr_2O_4$ states indicate potential thermodynamically unstable states that can lead to structural transformations into rutile $CrO_2$ and spinel $MgCr_2O_4$ during deintercalation. $^{84}$ However, cathodes with metastable deintercalated states have successfully been used as intercalation compounds, such as delithiated $FePO_4$ with an $E^{hull}$ ~ 26 meV/atom and demagnesiated spinel $Mn_2O_4$ with an $E^{hull}$ ~ 32 meV/atom. $^{62, 83}$

To more accurately address the potential instability of demagnesiated $Cr_2O_4$, we calculated its energy as well as that of the ground state rutile $CrO_2$ using the recently developed non-empirical strongly constrained and appropriately normed (SCAN) functional, which has been shown to improve ground state predictions over the GGA (PBE) and GGA+$U$ functionals. $^{85}$ Based on the SCAN calculations, we find that spinel $Cr_2O_4$ is 260 meV/atom higher in energy than the rutile

$CrO_2$ ground state. We can compare the spinel vs. rutile energy difference of $CrO_2$ to that of $MnO_2$, in which the rutile form is similarly the ground state but the spinel can easily be retained at room temperature and no conversion to rutile is ever observed. $^{86,87}$ In the case of $MnO_2$, the spinel $Mn_2O_4$ phase is ~110 meV/atom above the rutile ground state using the SCAN functional, which is significantly lower than the 260 meV/atom spinel vs. rutile energy difference in $CrO_2.^{88}$ While the driving force to convert the empty spinel to rutile is much higher in $CrO_2$ than in $MnO_2$, based on the metastability of the spinel $Mn_2O_4$ phase, we cannot make a definite prediction about the stability or lack thereof of spinel $Cr_2O_4$.

A potential approach to improve the Mg migration in the $Mg_xCr_2O_4$ spinel system is destabilizing (or lowering the depth of) the 33% Mg and/or 50% Mg configurations via substitution of the anion, tetrahedral Mg, or octahedral transition metal sites. Of the possible substitutions, cation-substitution or doping on the transition metal octahedral site, such as Mn or Ni on the Cr octahedral site, appears the most promising due to the success and improved electrochemical properties of transition metal doping in Li spinel oxides. $^{89,90}$ Further, the migration barriers at the dilute vacancy limits of the $MgMn_2O_4$ and $MgNi_2O_4$ spinels are lower (~400 meV with GGA) than that of $MgCr_2O_4$ (~600 meV with GGA and ~690 meV with GGA+$U$). Thus, doping with Mn or Ni on the Cr site may result in paths with lower migration barriers. Other potential substitutions to consider are fluorine or sulfur, which have been successfully doped on the oxygen site in the $LiMn_{1.5}Ni_{0.5}O_4$ spinel $^{91-93}$ or Zn on the tetrahedral Mg sites. $^{94,95}$ We note however that cation doping on the Mg sites runs the risk of blocking the Mg percolation pathways.

## Conclusion

We investigated the intercalation of Mg in the $Cr_2O_4$ spinel in order to better evaluate the $Mg_xCr_2O_4$ system as a potential cathode by building a cluster expansion to evaluate the room temperature voltage curve and investigating the kinetics at strong intermediate Mg-Va ground state orderings. We found that initial charge and deintercalation of the Mg is facile but that the intermediate orderings at 33% Mg and 50% Mg concentrations do pose potential problems to intercalation due to the depth of the orderings and the high migration barrier of Mg at concentrations below 50% Mg. We propose doping on the transition metal site (with transition metals such as Mn or Ni) or on the anion sites (with F or S) to destabilize the deep intermediate orderings and decrease the high Mg migration barrier and large voltage steps. Given the recent improvements in cathodic stabilities of Mg electrolytes, further studies on removing the bottlenecks of reversible Mg intercalation in the high-voltage spinel-$Cr_2O_4$ cathode should enable the practical realization of high energy density Mg batteries.

## Acknowledgments

This material is based upon work supported by the National Science Foundation Graduate Research Fellowship under Grant No. DGE 1106400. The work is also supported by the Joint Center for Energy Storage Research (JCESR), an Energy Innovation Hub funded by the U.S. Department of Energy, Office of Science and Basic Energy Sciences, through Subcontract 3F-31144. The authors thank the National Energy Research Scientific Computing Center (NERSC), a DOE Office of Science User Facility supported by the Office of Science and the U.S. Department of Energy under Contract No. DE-AC02-05CH11231, and the National Science Foundation's Extreme Science and Engineering Development Environment (XSEDE), which is supported by National Science Foundation grant number ACI-1548562, for providing computing

resources. The authors declare no competing financial interests. Any opinion, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.

# Supporting info detail

Further details on the cluster expansion ECI and the 33% Mg and 50% Mg ground state orderings are provided. An explanation of the free energy integration performed to remove hysteresis in the voltage profile is also provided. The change in unit cell during Mg intercalation is provided and discussed. The $60^oC$ (333 K) voltage profile is plotted along with the DFT, CE-predicted, and $20^oC$ (293 K) voltage profiles shown in the main text. The migration path of an additional Mg in the 50% Mg structure for which migration barriers were calculated is shown. Direct comparisons between NEB migration barriers and the convex hulls of the $Mg_xCr_2O_4$ system using the GGA vs. GGA+$U$ functionals are also displayed. The material is available free of charge on the Internet at http://pubs.acs.org/.

References

1.  Lipson, A. L.; Han, S.-D.; Pan, B.; See, K. A.; Gewirth, A. A.; Liao, C.; Vaughey, J. T.; Ingram, B. J., Practical Stability Limits of Magnesium Electrolytes. *Journal of The Electrochemical Society* **2016**, *163* (10), A2253-A2257.

2.  Canepa, P.; Sai Gautam, G.; Hannah, D. C.; Malik, R.; Liu, M.; Gallagher, K. G.; Persson, K. A.; Ceder, G., Odyssey of Multivalent Cathode Materials: Open Questions and Future Challenges. *Chemical Reviews* **2017**, *117* (5), 4287-4341.

3.  Huie, M. M.; Bock, D. C.; Takeuchi, E. S.; Marschilok, A. C.; Takeuchi, K. J., Cathode materials for magnesium and magnesium-ion based batteries. *Coordination Chemistry Reviews* **2015**, *287*, 15-27.

4.  Aurbach, D.; Lu, Z.; Schechter, A.; Gofer, Y.; Gizbar, H.; Turgeman, R.; Cohen, Y.; Moshkovich, M.; Levi, E., Prototype systems for rechargeable magnesium batteries. *Nature* **2000**, *407* (6805), 724-727.

5.  Lightfoot, P.; Krok, F.; Nowinski, J. L.; Bruce, P. G., Structure of the Cubic Intercalate MgₓTiS₂. *Journal of Materials Chemistry* **1992**, *2* (1), 139-140.

6.  Sun, X.; Bonnick, P.; Duffort, V.; Liu, M.; Rong, Z.; Persson, K. A.; Ceder, G.; Nazar, L. F., A high capacity thiospinel cathode for Mg batteries. *Energy Environ. Sci.* **2016**, *9* (7), 2273-2277.

7.  Sun, X.; Bonnick, P.; Nazar, L. F., Layered TiS₂ Positive Electrode for Mg Batteries. *ACS Energy Letters* **2016**, *1* (1), 297-301.

8.  Rong, Z.; Malik, R.; Canepa, P.; Sai Gautam, G.; Liu, M.; Jain, A.; Persson, K.; Ceder, G., Materials Design Rules for Multivalent Ion Mobility in Intercalation Structures. *Chemistry of Materials* **2015**, *27* (17), 6016-6021.

9.  Ling, C.; Zhang, R.; Arthur, T. S.; Mizuno, F., How general is the conversion reaction in Mg battery cathode: a case study of the magnesiation of α-MnO2. *Chemistry of Materials* **2015**, *27* (16), 5799-5807.

10. Zhang, R.; Ling, C., Unveil the chemistry of olivine FePO4 as magnesium battery cathode. *ACS applied materials & interfaces* **2016**, *8* (28), 18018-18026.

11. Brown, I. D., What factors determine cation coordination numbers? *Acta Crystallographica Section B* **1988**, *44* (6), 545-553.

12. Gopalakrishnan, S. G.; Bo, S.-h.; Ceder, G., Influence of inversion on Mg mobility and electrochemistry in spinels. **2017**, 1-33.

13. Canepa, P.; Sai Gautam, G.; Broberg, D.; Bo, S.-H.; Ceder, G., Role of point defects in spinel Mg chalcogenide conductors. *Chemistry of Materials* **2017**.

14. Canepa, P. B., Shou-Hang; Sai Gautam, Gopalakrishnan; Key, Baris Key; Richards, William D.; Shi, Tan Shi; Tian, Yaosen; Wang, Yan; Li, Juchuan Li; Gerbrand Ceder, High magnesium mobility in ternary spinel chalcogenides. *Nature Communications (in press)* **2017**.

15. Andre, D.; Kim, S.-J.; Lamp, P.; Lux, S. F.; Maglia, F.; Paschos, O.; Stiaszny, B., Future generations of cathode materials: an automotive industry perspective. *J. Mater. Chem. A* **2015**, 3 (13), 6709-6732.

16. Reed, J.; Ceder, G.; Van Der Ven, A., Layered-to-Spinel Phase Transition in $\text{Li}_x\text{MnO}_2$. *Electrochemical and Solid-State Letters* **2001**, 4 (6), A78-A78.

17. Thackeray, M. M.; Johnson, P. J.; de Picciotto, L. A.; Bruce, P. G.; Goodenough, J. B., Electrochemical extraction of lithium from $\text{LiMn}_2\text{O}_4$. *Materials Research Bulletin* **1984**, 19 (2), 179-187.

18. Van Der Ven, A.; Marianetti, C.; Morgan, D.; Ceder, G., Phase transformations and volume changes in spinel $\text{Li}_x\text{Mn}_2\text{O}_4$. *Solid State Ionics* **2000**, 135 (1-4), 21-32.

19. Wagemaker, M.; Van Der Ven, A.; Morgan, D.; Ceder, G.; Mulder, F. M.; Kearley, G. J., Thermodynamics of spinel $\text{Li}_x\text{TiO}_2$ from first principles. *Chemical Physics* **2005**, 317 (2-3), 130-136.

20. Whittingham, M. S., Lithium batteries and cathode materials. *Chemical Reviews* **2004**, 104 (10), 4271-4301.

21. Liu, M.; Rong, Z.; Malik, R.; Canepa, P.; Jain, A.; Ceder, G.; Persson, K. A., Spinel compounds as multivalent battery cathodes: a systematic evaluation based on ab initio calculations. *Energy Environ. Sci.* **2015**, 8 (3), 964-974.

22. Feng, Z.; Chen, X.; Qiao, L.; Lipson, A. L.; Fister, T. T.; Zeng, L.; Kim, C.; Yi, T.; Sa, N.; Proffit, D. L.; Burrell, A. K.; Cabana, J.; Ingram, B. J.; Biegalski, M. D.; Bedzyk, M. J.; Fenter, P., Phase-Controlled Electrochemical Activity of Epitaxial Mg-Spinel Thin Films. *ACS Applied Materials and Interfaces* **2015**, 7 (51), 28438-28443.

23. Kim, C.; Phillips, P. J.; Key, B.; Yi, T.; Nordlund, D.; Yu, Y. S.; Bayliss, R. D.; Han, S. D.; He, M.; Zhang, Z.; Burrell, A. K.; Klie, R. F.; Cabana, J., Direct observation of reversible magnesium ion intercalation into a spinel oxide host. *Advanced Materials* **2015**, 27 (22), 3377-3384.

24. Yin, J.; Brady, A. B.; Takeuchi, E. S.; Marschilok, A. C.; Takeuchi, K. J., Magnesium-ion battery-relevant electrochemistry of MgMn 2 O 4: crystallite size effects and the notable role of electrolyte water content. *Chemical Communications* **2017**, 53 (26), 3665-3668.

25. Ling, C.; Zhang, R.; Mizuno, F., Quantitatively Predict the Potential of MnO2 Polymorphs as Magnesium Battery Cathodes. *ACS applied materials & interfaces* **2016**, 8 (7), 4508-4515.

26. K.S. Irani, A. P. B. S., A.B. Biswas, Effect of Temperature on the Structure of Manganites. *J. Phys. Chem. Solids* **1962**, 23 (458), 711-727.

27. Malavasi, L.; Ghigna, P.; Chiodelli, G.; Maggi, G.; Flor, G., Structural and Transport Properties of Mg1−xMnxMn2O4±δ Spinels. *Journal of Solid State Chemistry* **2002**, 166 (1), 171-176.

28. Radhakrishnan, N. K.; Biswas, A. B., A neutron diffraction study of the cation migration in $\text{MgMn}_2\text{O}_4$. *Physica Status Solidi (a)* **1976**, 37 (2), 719-722.

29. Rosenberg, M.; Nicolau, P., Electrical Properties and Cation Migration in $MgMn_2O_4$. 1964, 101, 101-110.

30. Reed, J.; Ceder, G., Role of electronic structure in the susceptibility of metastable transition-metal oxide structures to transformation. Chemical Reviews 2004, 104 (10), 4513-4533.

31. Glidewell, C., Cation distribution in spinels: Lattice energy versus crystals field stabilisation energy. Inorganica Chimica Acta 1976, 19 (C), 45-47.

32. Mao, H. K.; Bell, P. M., Crystal-field effects in spinel: oxidation states of iron and chromium. Geochimica et Cosmochimica Acta 1975, 39 (6-7).

33. Bo, S. H.; Li, X.; Toumar, A. J.; Ceder, G., Layered-to-Rock-Salt Transformation in Desodiated NaxCrO2 (x 0.4). Chemistry of Materials 2016, 28 (5), 1419-1429.

34. Cao, M.-H.; Wang, Y.; Shadike, Z.; Yue, J.-L.; Hu, E.; Bak, S.-M.; Zhou, Y.-N.; Yang, X.-Q.; Fu, Z.-W., Suppressing the chromium disproportionation reaction in O3-type layered cathode materials for high capacity sodium-ion batteries. Journal of Materials Chemistry A 2017, 5 (11), 5442-5448.

35. Stephens, J.; Cruickshank, D., The crystal structure of $(CrO_3)∞$. Acta Crystallographica Section B: Structural Crystallography and Crystal Chemistry 1970, 26 (3), 222-226.

36. Dutton, S. E.; Huang, Q.; Tchernyshyov, O.; Broholm, C.; Cava, R., Sensitivity of the magnetic properties of the $ZnCr_2O_4$ and $MgCr_2O_4$ spinels to nonstoichiometry. Physical Review B 2011, 83 (6), 064407.

37. Ehrenberg, H.; Knapp, M.; Baehtz, C.; Klemme, S., Tetragonal low-temperature phase of $MgCr_2O_4$. Powder diffraction 2002, 17 (3), 230-233.

38. Kant, C.; Deisenhofer, J.; Tsurkan, V.; Loidl, A. In Magnetic susceptibility of the frustrated spinels $ZnCr_2O_4$, $MgCr_2O_4$ and $CdCr_2O_4$, Journal of Physics: Conference Series, IOP Publishing: 2010; p 032032.

39. Ortega-San-Martin, L.; Williams, A.; Gordon, C.; Klemme, S.; Attfield, J., Low temperature neutron diffraction study of $MgCr_2O_4$ spinel. Journal of Physics: Condensed Matter 2008, 20 (10), 104238.

40. Rovers, M.; Kyriakou, P.; Dabkowska, H.; Luke, G.; Larkin, M.; Savici, A., Muon-spin-relaxation investigation of the spin dynamics of geometrically frustrated chromium spinels. Physical Review B 2002, 66 (17), 174434.

41. Suzuki, H.; Tsunoda, Y., Spinel-type frustrated system $MgCr_2O_4$ studied by neutron scattering and magnetization measurements. Journal of physics and chemistry of solids 2007, 68 (11), 2060-2063.

42. Xiang, H.; Kan, E.; Wei, S.-H.; Whangbo, M.-H.; Gong, X., Predicting the spin-lattice order of frustrated systems from first principles. Physical Review B 2011, 84 (22), 224429.

43. Yoshida, M.; Hirano, T.; Inagaki, Y.; Okubo, S.; Ohta, H.; Kikuchi, H.; Kagomiya, I.; Toki, M.; Kohn, K., High field ESR study of three dimensional spin frustrated system $MgCr_2O_4$. Journal of the Physical Society of Japan 2006, 75 (4), 044709.

44. Van der Ven, A.; Aydinol, M.; Ceder, G.; Kresse, G.; Hafner, J., First-principles investigation of phase stability in $Li_xCoO_2$First-principles investigation of phase stability in LixCoO2. *Physical Review B* **1998**, *58* (6), 2975.

45. de Dompablo, A. Y.; Van der Ven, A.; Ceder, G., First-principles calculations of lithium ordering and phase stability on $Li_xNiO_2$First-principles calculations of lithium ordering and phase stability on LixNiO2. *Physical Review B* **2002**, *66* (6).

46. Wolverton, C.; Zunger, A., First-principles prediction of vacancy order-disorder and intercalation battery voltages in $Li_xCoO_2$First-principles prediction of vacancy order-disorder and intercalation battery voltages in LixCoO2. *Physical review letters* **1998**, *81* (3), 606.

47. Hinuma, Y.; Meng, Y. S.; Ceder, G., Temperature-concentration phase diagram of P2-$Na_xCoO_2$ from first-principles. *Physical Review B* **2008**, *77* (22), 224111-224111.

48. Sai Gautam, G.; Canepa, P.; Abdellahi, A.; Urban, A.; Malik, R.; Ceder, G., The intercalation phase diagram of Mg in $V_2O_5$ from first-principles. *Chemistry of Materials* **2015**, *27* (10), 3733-3742.

49. Urban, A.; Seo, D.-H.; Ceder, G., Computational understanding of Li-ion batteries. *npj Computational Materials* **2016**, *2*, 16002.

50. Hohenberg, P.; Kohn, W., Inhomogeneous electron gas. *Physical Review B* **1973**, *7* (5), 1912-1919.

51. Kohn, W.; Sham, L. J., Self-consistent equations including exchange and correlation effects. *Physical Review* **1965**, *140* (4A).

52. Kresse, G.; Furthmüller, J., Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set. *Physical Review B* **1996**, *54* (16), 11169-11186.

53. Kresse, G.; Hafner, J., Ab initio molecular dynamics for liquid metals. *Physical Review B* **1993**, *47* (1), 558-561.

54. Perdew, J. P.; Burke, K.; Ernzerhof, M., Generalized Gradient Approximation Made Simple. *Physical Review Letters* **1996**, *77* (18), 3865-3868.

55. Anisimov, V. I.; Zaanen, J.; Andersen, O. K., Band theory and Mott insulators: Hubbard U instead of Stoner I. *Physical Review B* **1991**, *44* (3), 943-954.

56. Jain, A.; Hautier, G.; Ong, S. P.; Moore, C. J.; Fischer, C. C.; Persson, K. A.; Ceder, G., Formation enthalpies by mixing GGA and GGA + U calculations. *Physical Review B - Condensed Matter and Materials Physics* **2011**, *84* (4), 1-10.

57. Zhou, F.; Cococcioni, M.; Marianetti, C. A.; Morgan, D.; Ceder, G., First-principles prediction of redox potentials in transition-metal compounds with LDA + U. *Physical Review B - Condensed Matter and Materials Physics* **2004**, *70* (23), 1-8.

58. Kresse, G.; Joubert, D., From ultrasoft pseudopotentials to the projector augmented-wave method. *Physical Review B* **1999**, *59* (3), 1758-1775.

59. Monkhorst, H. J.; Pack, J. D., "Special points for Brillouin-zone integrations" - a reply. *Physical Review B* **1977**, *16* (4), 1748-1749.

60. Ceder, G., A derivation of the Ising model for the computation of phase diagrams. *Computational Materials Science* **1993**, *1*, 144-150.

61. Sanchez, J. M.; Ducastelle, F.; Gratias, D., Generalized cluster description of multicomponent systems. *Physica A: Statistical Mechanics and its Applications* **1984**, *128* (1-2), 334-350.

62. Jain, A.; Hautier, G.; Moore, C. J.; Ping Ong, S.; Fischer, C. C.; Mueller, T.; Persson, K. A.; Ceder, G., A high-throughput infrastructure for density functional theory calculations. *Computational Materials Science* **2011**, *50* (8), 2295-2310.

63. Ong, S. P.; Richards, W. D.; Jain, A.; Hautier, G.; Kocher, M.; Cholia, S.; Gunter, D.; Chevrier, V. L.; Persson, K. A.; Ceder, G., Python Materials Genomics (pymatgen): A robust, open-source python library for materials analysis. *Computational Materials Science* **2013**, *68*, 314-319.

64. Ewald, P. P., Die Berechnung optischer und elektrostatischer Gitterpotentiale. *Annalen der Physik* **1921**, *369* (3), 253-287.

65. Goldstein, T.; Osher, S., The Split Bregman Method for L1-Regularized Problems. *SIAM Journal on Imaging Sciences* **2009**, *2* (2), 323-343.

66. Nelson, L. J.; Hart, G. L. W.; Zhou, F.; Ozoli, V., Compressive sensing as a paradigm for building physics models. *Physical Review B - Condensed Matter and Materials Physics* **2013**, *87* (3), 1-12.

67. Huang, W.; Kitchaev, D. A.; Dacek, S. T.; Rong, Z.; Urban, A.; Cao, S.; Luo, C.; Ceder, G., Finding and proving the exact ground state of a generalized Ising model by convex optimization and MAX-SAT. *Physical Review B - Condensed Matter and Materials Physics* **2016**, *94* (13), 1-12.

68. Van der Ven, A.; Thomas, J. C.; Xu, Q.; Bhattacharya, J., Linking the electronic structure of solids to their thermodynamic and kinetic properties. *Mathematics and Computers in Simulation* **2010**, *80* (7), 1393-1410.

69. Van Der Ven, A.; Thomas, J. C.; Xu, Q.; Swoboda, B.; Morgan, D., Nondilute diffusion from first principles: Li diffusion in $\mathrm{Li_xTiS_2}$. *Physical Review B - Condensed Matter and Materials Physics* **2008**, *78* (10), 1-12.

70. Aydinol, M. K.; Kohan, A. F.; Ceder, G.; Cho, K.; Joannopoulos, J., Ab initio study of lithium intercalation in metal oxides and metal dichalcogenides. *Physical Review B* **1997**, *56* (3), 1354-1365.

71. Walle, A. V. D.; Asta, M., Self-driven lattice-model Monte Carlo simulations of alloy thermodynamic properties and phase diagrams. **2002**, *0393* (02), 521-538.

72. Henkelman, G.; Jónsson, H., Improved tangent estimate in the nudged elastic band method for finding minimum energy paths and saddle points. *Journal of Chemical Physics* **2000**, *113* (22), 9978-9985.

73. Sheppard, D.; Terrell, R.; Henkelman, G., Optimization methods for finding minimum energy paths. *Journal of Chemical Physics* **2008**, *128* (13).

74. Ong, S. P.; Chevrier, V. L.; Ceder, G., Comparison of small polaron migration and phase separation in olivine LiMnPO 4 and LiFePO 4 using hybrid density functional theory. *Physical Review B* **2011**, *83* (7), 075112.

75. Maxisch, T.; Zhou, F.; Ceder, G., Ab initio study of the migration of small polarons in olivine Li x FePO 4 and their association with lithium ions and vacancies. *Physical review B* **2006**, *73* (10), 104301.

76. Gautam, G. S.; Canepa, P.; Malik, R.; Liu, M.; Persson, K.; Ceder, G., First-principles evaluation of multi-valent cation insertion into orthorhombic V₂O₅. **2015**.

77. Bhattacharya, J.; Wolverton, C., Relative stability of normal vs. inverse spinel for 3d transition metal oxides as lithium intercalation cathodes. *Physical Chemistry Chemical Physics* **2013**, *15* (17), 6486-6498.

78. Kim, J. C.; Seo, D.-H.; Ceder, G., Theoretical capacity achieved in a LiMn 0.5 Fe 0.4 Mg 0.1 BO 3 cathode by using topological disorder. *Energy & Environmental Science* **2015**, *8* (6), 1790-1798.

79. Gautam, G. S.; Canepa, P.; Malik, R.; Liu, M.; Persson, K.; Ceder, G., First-principles evaluation of multi-valent cation insertion into orthorhombic V₂O₅. *Chem. Commun.* **2015**, *51* (71), 13619-13622.

80. Zhou, F.; Maxisch, T.; Ceder, G., Configurational electronic entropy and the phase diagram of mixed-valence oxides: the case of Li x FePO 4. *Physical review letters* **2006**, *97* (15), 155704.

81. Van der Ven, A.; Ceder, G., Lithium diffusion mechanisms in layered intercalation compounds. *Journal of power sources* **2001**, *97*, 529-531.

82. Ling, C.; Suto, K., Thermodynamic Origin of Irreversible Magnesium Trapping in Chevrel Phase Mo6S8: Importance of Magnesium and Vacancy Ordering. *Chemistry of Materials* **2017**, *29* (8), 3731-3739.

83. Jain, A.; Ong, S. P.; Hautier, G.; Chen, W.; Richards, W. D.; Dacek, S.; Cholia, S.; Gunter, D.; Skinner, D.; Ceder, G., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation. *Apl Materials* **2013**, *1* (1), 011002.

84. Gautam, G. S.; Sun, X.; Duffort, V.; Nazar, L. F.; Ceder, G., Impact of intermediate sites on bulk diffusion barriers: Mg intercalation in Mg₂Mo₃O₈. *Journal of Materials Chemistry A* **2016**, *4* (45), 17643-17648.

85. Sun, J.; Remsing, R. C.; Zhang, Y.; Sun, Z.; Ruzsinszky, A.; Peng, H.; Yang, Z.; Paul, A.; Waghmare, U.; Wu, X., Accurate first-principles structures and energies of diversely bonded systems from an efficient density functional. *Nature chemistry* **2016**, *8* (9), 831-836.

86. Hunter, J. C., Preparation of a new crystal form of manganese dioxide: λ-MnO2. *Journal of Solid State Chemistry* **1981**, *39* (2), 142-147.

87. Mosbah, A.; Verbaere, A.; Tournoux, M., Phases LixMnO2λ rattachees au type spinelle. *Materials research bulletin* **1983**, *18* (11), 1375-1381.

88. Kitchaev, D. A.; Peng, H.; Liu, Y.; Sun, J.; Perdew, J. P.; Ceder, G., Energetics of MnO2 polymorphs in density functional theory. *Physical Review B* **2016**, *93* (4), 045132.

89. Bellitto, C.; Bauer, E. M.; Righini, G.; Green, M. A.; Branford, W. R.; Antonini, A.; Pasquali, M., The effect of doping LiMn₂O₄ spinel on its use as a cathode in Li-ion batteries:

Neutron diffraction and electrochemical studies. *Journal of Physics and Chemistry of Solids* **2004**, *65* (1), 29-37.

90. Pistoia, G.; Antonini, a.; Rosati, R.; Bellitto, C.; Ingo, G. M., Doped Li−Mn Spinels: Physical/Chemical Characteristics and Electrochemical Performance in Li Batteries. *Chemistry of Materials* **1997**, *9* (May 1996), 1443-1450.

91. Fergus, J. W., Recent developments in cathode materials for lithium ion batteries. *Journal of Power Sources* **2010**, *195* (4), 939-954.

92. Sun, Y.-K.; Oh, S. W.; Yoon, C. S.; Bang, H. J.; Prakash, J., Effect of sulfur and nickel doping on morphology and electrochemical performance of ${\text{LiNi}}_{0.5}{\text{Mn}}_{1.5}{\text{O}}_{4-\text{x}}{\text{S}}_{\text{x}}$ spinel material in 3-V region. *Journal of power sources* **2006**, *161* (1), 19-26.

93. Yi, T.-F.; Xie, Y.; Ye, M.-F.; Jiang, L.-J.; Zhu, R.-S.; Zhu, Y.-R., Recent developments in the doping of ${\text{LiNi}}_{0.5}{\text{Mn}}_{1.5}{\text{O}}_{4}$ cathode material for 5 V lithium-ion batteries. *Ionics* **2011**, *17* (5), 383-389.

94. Choodamani, C.; Rudraswamy, B.; Chandrappa, G., Structural, electrical, and magnetic properties of Zn substituted magnesium ferrite. *Ceramics International* **2016**, *42* (9), 10565-10571.

95. Kan, A.; Takahashi, S.; Moriyama, T.; Ogawa, H., Influence of Zn substitution for Mg on microwave dielectric properties of spinel-structured (Mg1−xZnx) Ga2O4 solid solutions. *Japanese Journal of Applied Physics* **2014**, *53* (9S), 09PB03.

# Graphical TOC Entry

![](./images/813080417434337282_10.jpg)