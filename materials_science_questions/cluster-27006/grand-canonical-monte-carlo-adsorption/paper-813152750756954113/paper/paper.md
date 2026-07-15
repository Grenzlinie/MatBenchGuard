PAPER
View Article Online
View Journal | View Issue

# Zeolite screening for the separation of gas mixtures containing $\mathrm{SO}_{2}, \mathrm{CO}_{2}$ and $\mathrm{CO} \dagger$

I. Matito-Martos, $^{a}$ A. Martin-Calvo, $^{a}$ J. J. Gutiérrez-Sevillano, $^{b}$ M. Haranczyk, $^{c}$ M. Doblare, $^{d}$ J. B. Parra, $^{e}$ C. O. Ania $^{e}$ and S. Calero*a

We used a combination of experiments and molecular simulations to investigate at the molecular level the effects of zeolite structure on the adsorption and diffusion of sulfur dioxide, carbon dioxide and carbon monoxide as well as separation processes of their mixtures. Our study involved different zeolite topologies and revealed numerous structure-property trends depending on the temperature and pressure conditions. Sulfur dioxide, which has the strongest interactions with zeolites due to its size and polarity, showed the largest adsorption across investigated temperatures and pressures. Our results indicate that structures with channel-type pore topology and low pore volume are the most promising for selective adsorption of sulfur dioxide over carbon dioxide and carbon monoxide under room conditions, while structures with higher pore volume exhibit better storage capacity at higher pressure. Our results emphasize the need for considering both adsorption and diffusion processes in the selection of the optimal structure for a given separation process. Our findings help to identify the best materials for effective separation processes under realistic operating conditions.

## 1. Introduction
Sulfur dioxide ($\mathrm{SO}_{2}$) is an ubiquitous component of fuel combustion exhausts and a gas of relevant environmental impact whose control remains a challenging issue. $^{1}$ Aside from the toxicity of sulfur dioxide itself, $\mathrm{SO}_{2}$ emissions also affect the efficiency of carbon dioxide capture processes$^{2,3}$ where investigations have been particularly intense over the last few years to fight the global warming and reduce greenhouse gas emissions. The trace amounts of $\mathrm{SO}_{2}$ in the flue gas from coal fired plants (typical composition contains 10-15% $\mathrm{CO}_{2}$, and many other contaminants as $\mathrm{O}_{2}$, $\mathrm{H}_{2}\mathrm{O}$, $\mathrm{SO}_{2}$, $\mathrm{NO}_{x}$, $\mathrm{H}_{2}$ at different levels of concentration) are known to undergo parasitic reactions with current methods for $\mathrm{CO}_{2}$ capture (namely amines and calcium sorbents). For instance, in the separation of $\mathrm{CO}_{2}$ by adsorption in amines it is necessary to lower the $\mathrm{SO}_{2}$ concentration in the gas influent below 10 ppm to minimize the loss of the solvent associated with thermally stable salts of the amine with $\mathrm{SO}_{2}\ ^{4,5}$ The sulfation of calcium based sorbents is also a competing process that affects the regeneration temperature of CaO, decreasing the regenerative capacity of the sorbent over subsequent cycles.$^{6,7}$ Whereas research on the simultaneous removal of $\mathrm{SO}_{2}/\mathrm{CO}_{2}$ mixtures is still under development, $^{8}$ separation of these gases is crucial to achieve high carbon capture efficiencies.

Over the past few decades, a number of technologies have been developed to prevent the generation and release of $\mathrm{SO}_{2}$ during combustion processes. They are based on different approaches: before (fuel desulfurization before combustion), during (fluidized bed combustion coupled to integrated gasification combined cycle (IGCC) systems) or post-combustion (flue gas desulfurization).$^{9,10}$ Sulfur dioxide removal *via* scrubbing is the most widely applied approach for the post-combustion process due to the availability of efficient scrubber systems and their relatively low cost. However, this process still generates large amounts of solid wastes and off-gas streams, further management and disposal of which entail an important cornerstone of this technology. For instance, the catalytic reduction of $\mathrm{SO}_{2}$ to elemental sulfur by CO ($2\mathrm{CO} + \mathrm{SO}_{2} \to 1/2\ \mathrm{S}_{2} + 2\mathrm{CO}_{2}$)$^{11-13}$ is used to process the off-gas stream generated in flue gas desulfurization systems, to obtain high added value by-products such as elemental sulfur or sulfuric acid. Adsorption of $\mathrm{SO}_{2}$ in nanoporous materials is a potential alternative technology to reduce or eliminate the emissions of $\mathrm{SO}_{2}$ and other pollutants, as well as reducing the generation of solids in flue gas desulfurization systems. This would avoid the management and disposal of solid wastes,

---
$^{a}$ Department of Physical, Chemical, and Natural Systems, University Pablo de Olavide, Ctra. de Utrera, km. 1, 41013 Seville, Spain. E-mail: scalero@upo.es
$^{b}$ Department of Process and Energy, Delft University of Technology, Leeghwaterstraat 44, 2628 CA Delft, The Netherlands
$^{c}$ Lawrence Berkeley National Laboratory, One Cyclotron Road, MS 50F-1650, Berkeley, CA 94720, USA
$^{d}$ Abengoa Research, Campus Palmas Altas, Energía Solar, 1. (Palmas Altas), 41014 Seville, Spain
$^{e}$ Instituto Nacional del Carbón, INCAR, CSIC, P.O. 73, 33080 Oviedo, Spain
$\dagger$ Electronic supplementary information (ESI) available. See DOI: 10.1039/c4cp00109e

thereby decreasing the cost and accelerating the implementation of this technology.

In the present work, the separation efficiency of $SO_2$-containing binary and ternary mixtures ($CO_2/SO_2$, $CO/SO_2$, $CO/CO_2/SO_2$) was studied through experimental measurements and molecular simulation calculations. We focus on systems containing $SO_2$ for which available data in the literature are rather scarce. $^{14,15}$

Among nanoporous sorbents, zeolites are promising candidates for this application as molecular sieves. $^{16-19}$ Zeolites are crystalline aluminosilicates consisting of tetrahedral units with four oxygen atoms (O atoms) bonded to one atom of silicon, aluminium, or the other four-fold coordinated metal (T atoms). Each aluminium that replaces an atom of silicon generates a negative net charge in the structure that can be balanced by the addition of protons and cations in the system. $^{20,21}$ Tetrahedra are connected *via* oxygen atoms, generating 3D structures with cages and/or channels. The shape and size of these channels and cages, as well as the silicon/aluminium ratio, and the presence of cations are very important because they influence the adsorption, diffusion, and separation properties. $^{22-28}$ Highly ordered zeolite structure have many desirable properties, $^{20,29,30}$ such as high surface area or thermal stability, which make them promising materials for the storage, separation, and purification of gas mixtures. $^{31-33}$

The large amount of available zeolitic structures (about 200 unique topologies) and the corrosive nature of sulfur dioxide – hindering their handling – pose a challenge to experimentally screen many structures to identify the most adequate material(s) for the selective separation of sulfur dioxide from post-combustion streams containing carbon dioxide and carbon monoxide. In this study, we aim to guide experimental work by performing a molecular simulation screening of different zeolites, and predict their $SO_2$ adsorption and separation potential. We provide the molecular level understanding of the effect of the structural features of zeolites, such as the pore topology or accessible pore volume, on the adsorption, diffusion, and separation of sulfur dioxide from carbon dioxide and carbon monoxide. Our study focused on a set of zeolites with a diverse porosity (in terms of pore size, shape and topology) selected from 194 all silica zeolite structures from the IZA database. $^{34}$ For these selected structures we have computed adsorption properties and diffusion coefficients of the three gasses under study, and we have compared our simulations with the experimental data available from the literature. We describe the models for zeolites and adsorbates as well as the simulation techniques in Section 2. The obtained results are discussed in Section 3 and we summarize the most relevant conclusions in Section 4.

## 2. Methodology
### 2.1. Computational details
Adsorption isotherms were computed using Monte Carlo simulations in the Grand Canonical ensemble (GCMC), where the temperature, the volume, and the chemical potential remain fixed. Chemical potential is associated with the fugacity, and fugacity is directly related to pressure with the fugacity coefficient. Simulations were performed at 298 K. Based on the type of gas and on the operating conditions, in this work we equate pressure with fugacity, *i.e.* the fugacity coefficient is 1. To compare simulated and experimental isotherms, absolute adsorption is converted to excess adsorption. $^{35,36}$ Simulations were performed using our in-house code RASPA. $^{37}$ This code has been extensively tested and validated with a large number of experimental and simulation data. $^{17,38-41}$ Isosteric heats of adsorption and Henry coefficients were computed using the Widom test particle method. $^{42}$ Self-diffusion coefficients were computed from the mean square displacements of the adsorbates calculated from molecular dynamic simulations in the canonical ensemble. Simulations start from equilibrium conditions previously achieved using GCMC simulations for ternary mixtures. Successive configurations of the system were generated by integrating Newton's laws of motion using the Verlet algorithm. We use the Nosé–Hoover thermostat with a time scale on which the system thermostat evolves of 0.15 ps. The self-diffusion coefficients were computed at 298 K from the slope of the mean-square displacement at long times. Simulations have been run for 1000–10 000 ps using an integration time step of $\tau = 5 \times 10^{-4}$ ps. Before starting collecting data we perform a short MC simulation to obtain a sensible configuration. Other properties of the structures such as surface area and pore volume were also computed for later analysis.

Atomic interactions were described by Lenard-Jones and Coulomb potentials. We use a cutoff distance of 12 Å, and Ewald summation to calculate Coulombic interactions. We used previously published models for carbon dioxide and carbon monoxide. $^{38,40}$ Sulfur dioxide molecules are modeled rigid with a S–O bond length of 1.431 Å and an O–S–O bond angle of 119°. To mimic the dipole moment of the molecule (1.62 Debye) $^{43}$ we assigned point charges to the sulfur atom $(0.402\ e^-)$ and to the oxygen atoms $(-0.201\ e^-)$. The Lennard-Jones parameters for sulfur dioxide were obtained by fitting to the vapour–liquid equilibrium curve $^{44}$ (Fig. S1 in the ESI†). To compute this curve we used Gibbs-ensemble Monte Carlo simulations. $^{42}$ Interactions between adsorbates are computed using Lorentz-Berthelot mixing rules. $^{45,46}$ Since zeolites not always obey the Lorentz-Berthelot mixing rules $^{17,38}$ for the adsorbate–adsorbent interactions Lennard-Jones parameters have to be adjusted independently to reproduce the experimental data. $^{17,38}$ We define the adsorbate–adsorbent interactions by those of the oxygen atoms of the framework (Ozeo) with all the atoms from the adsorbed molecules. We use the Lennard-Jones parameters proposed by Garcia-Sanchez *et al.* $^{38}$ to reproduce the interactions with carbon dioxide. The Lennard-Jones parameters to reproduce the interactions between the other two adsorbates (sulfur dioxide and carbon monoxide) and the zeolites were developed in this work. Lennard-Jones parameters and partial charges of the molecules are summarized in Table 1.

A set of 194 all silica zeolite structures from the International Zeolite Association (IZA) $^{34}$ was characterized in terms of pore geometry and topology using Zeo++ software. $^{47,48}$ Zeo++ performs segmentation of the void space to identify pore

<table><caption>Table 1 Lennard-Jones parameters and partial charges of the adsorbates and the structure</caption>
<thead>
<tr>
<th>Atom 1</th>
<th>Atom 2</th>
<th>$\varepsilon/k_\text{B}$ (K)</th>
<th>$\sigma$ (Å)</th>
<th>Charge ($e^-$)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5">Adsorbed molecules</td>
</tr>
<tr>
<td>C(CO₂)</td>
<td>C(CO₂)</td>
<td>29.933</td>
<td>2.745</td>
<td>0.651</td>
</tr>
<tr>
<td>O(CO₂)</td>
<td>O(CO₂)</td>
<td>85.671</td>
<td>3.017</td>
<td>−0.326</td>
</tr>
<tr>
<td>C(CO)</td>
<td>C(CO)</td>
<td>16.141</td>
<td>3.658</td>
<td>−0.242</td>
</tr>
<tr>
<td>O(CO)</td>
<td>O(CO)</td>
<td>98.014</td>
<td>2.979</td>
<td>−0.274</td>
</tr>
<tr>
<td>Dum(CO)</td>
<td>Dum(CO)</td>
<td>—</td>
<td>—</td>
<td>0.517</td>
</tr>
<tr>
<td>S(SO₂)</td>
<td>S(SO₂)</td>
<td>189.353</td>
<td>3.41</td>
<td>0.402</td>
</tr>
<tr>
<td>O(SO₂)</td>
<td>O(SO₂)</td>
<td>58.725</td>
<td>3.198</td>
<td>−0.201</td>
</tr>
<tr>
<td colspan="5">Zeolite</td>
</tr>
<tr>
<td>O(zeo)</td>
<td>O(zeo)</td>
<td>—</td>
<td>—</td>
<td>−0.393</td>
</tr>
<tr>
<td>Si(zeo)</td>
<td>Si(zeo)</td>
<td>—</td>
<td>—</td>
<td>0.786</td>
</tr>
<tr>
<td colspan="5">Zeolite – adsorbed molecules</td>
</tr>
<tr>
<td>C(CO₂)</td>
<td>O(zeo)</td>
<td>37.595</td>
<td>3.511</td>
<td>—</td>
</tr>
<tr>
<td>O(CO₂)</td>
<td>O(zeo)</td>
<td>78.98</td>
<td>3.237</td>
<td>—</td>
</tr>
<tr>
<td>C(CO)</td>
<td>O(zeo)</td>
<td>40.109</td>
<td>3.379</td>
<td>—</td>
</tr>
<tr>
<td>O(CO)</td>
<td>O(zeo)</td>
<td>98.839</td>
<td>3.057</td>
<td>—</td>
</tr>
<tr>
<td>Dum(CO)</td>
<td>O(zeo)</td>
<td>—</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>S(SO₂)</td>
<td>O(zeo)</td>
<td>138.555</td>
<td>3.168</td>
<td>—</td>
</tr>
<tr>
<td>O(SO₂)</td>
<td>O(zeo)</td>
<td>77.161</td>
<td>3.066</td>
<td>—</td>
</tr>
</tbody>
</table>

systems accessible to a given probe. For each pore system Zeo++ calculates dimensionality of the pore system, the diameter of the largest included sphere (Di), the largest free sphere (Df), and the largest included sphere along the free sphere path (Dif). Di measures the largest opening in the structure while Df measures the restriction along the diffusion pathway of the largest spherical probe. All calculations performed with Zeo++ involve hard sphere approximation for atoms. A radius of 1.35 Å was assumed for both O and Si atoms⁴⁹ while a probe radius of 1.4 Å was used for the void space segmentation to detect pore systems. Additionally, each characterized material is classified as either a channel or an interconnected cage system based on the ratio of Dif and Df, where a channel is recognized for structures with $\text{Dif/Df} < 1.5$, and an interconnected cage system otherwise. The results of the above characterization for the selected zeolites are collected in Tables S1–S6 in the ESI.† Thus, the structures were classified according to their channel or interconnected cage character, and the corresponding directionality, 1–3, of the pore space. We selected structures within each of these six classes to obtain representative sets: 1D channels (ASV, DON, ITW, JRY, LAU, LTL, MOR, NAT, PON), 2D channels (AFR, FER, IWV, NES, SFO, SFG, TER), 3D channels (AFY, BEC, BOG, MEL, MFI, ITR, SBT, STW, SZR), 1D interconnected cages (ITE, MTF, SAS), 2D interconnected cages (DDR, LEV, MWW), 3D interconnected cages (CHA, ERI, FAU, LTA, KFI, PAU, RHO, SBE). The pore landscapes of representative structures of each group are shown in Fig. 1. The pore landscapes for all the selected structures are shown in Fig. S2–S4 in ESI.†

We considered all zeolites under study as all silica, rigid models.³⁴,⁵⁰⁻⁶⁷ The set of charges of the frameworks are taken from Garcia-Sanchez et al.³⁸ A summary of some characteristics of the different zeolites, such as their unit cell lengths, angles, computed pore volumes, and computed surface areas can be found in Table S7 in the ESI.†

![](./images/813152750756954113_1.jpg)

Fig. 1 Pore landscapes of representative zeolites used in this work. Channels: 1D, 2D and 3D – ASV, FER and BOG, respectively; interconnected cages: 1D, 2D and 3D – MTF, DDR and SBE, respectively. The inner surface of the pores is highlighted in yellow. The color codes for atoms are red and beige for oxygen and silicon, respectively.

### 2.2. Experimental details
All silica ($\text{Si/Al} \approx \infty$) MFI was kindly supplied by the Instituto de Tecnología Química (ITQ) belonging to the Consejo Superior de Investigaciones Científicas (CSIC). Experimental adsorption isotherms of CO at temperatures near ambient conditions were performed in a volumetric analyzer (ASAP 2020, Micromeritics) in the pressure range from $10^{-2}$ up to 120 kPa; the instrument was equipped with a turbo molecular vacuum pump and three pressure transducers (0.13, 1.33, and 133 kPa, uncertainty within 0.15% of each reading) to enhance the sensitivity in the low pressure range. Prior to the adsorption measurements, the zeolite was *in situ* outgassed under vacuum ($ca$. $10^{-3}$ kPa) at 673 K overnight. All of the isotherms were done in triplicate, and the data are reproducible with an error below 0.1%. The temperature of the isotherms was controlled using a thermostatic circulating oil bath. Ultrahigh purity CO (*i.e.*, 99.995%) was supplied by Air Products.

## 3. Results and discussion
The adsorption loadings computed for sulfur dioxide, carbon dioxide, and carbon monoxide, as pure components, as well as for the 20:40:40 ternary mixture (SO₂/CO₂/CO), and the CO₂/CO equimolar binary mixture were obtained at a pressure span from $10^{-1}$ to $10^{4}$ kPa. Self-diffusion coefficients were obtained from the adsorption isotherms of ternary mixtures under ambient conditions. The adsorption properties in the low coverage regime (Isosteric heats of adsorption and Henry coefficients) were computed for the three adsorbates in all the zeolites under study. In the case of mixtures we studied (a) the selective adsorption and diffusion behavior of the ternary mixture at atmospheric pressure and room temperature, and (b) the selective adsorption behavior of the CO₂/CO binary equimolar mixture. Based on our findings we have discussed

separation performance in terms of both pore volume and permselectivity.

### 3.1. Adsorption of pure components for forcefield validation
Pure component gas adsorption isotherms were computed and compared to available experimental data to validate the force-field parameters developed in this work for CO and $SO_2$ accounting for the gas-adsorbent interactions. The parameters describing $CO_2$-zeolite interactions have been validated in a previous work. $^{38}$ Simulated and experimental adsorption isotherms of $SO_2$ and CO as pure components on MFI are shown in Fig. 2. In order to compare with experimental data we performed additional adsorption isotherms in the range of temperature that spans from 258 K to 373 K. It should be mentioned that available experimental data for $SO_2$ adsorption on nanoporous materials are rather scarce, due to the corrosive nature of this gas that makes difficult its handling. Anyhow, Fig. 2a shows a comparison of our simulated $SO_2$ adsorption isotherms in MFI at 298-373 K with the available experimental data from Deng and Lin. $^{68}$ Simulations are in good agreement with experiments at all three temperatures, with a slight over-estimation of the adsorption capacity at 298 K. This could be attributed to the fact that simulations are computed considering rigid and clean zeolite structures while zeolites can exhibit some flexibility, and experimental data are recorded on materials that may often present structural defects or impurities (i.e. adsorbed water and/or other residues from the synthesis) that would lead to a lower gas adsorption capacity. Fig. 2b shows the perfect match between our experimental and computed adsorption isotherms of CO in MFI. The good agreement at several temperatures obtained for both CO and $SO_2$ validates the forcefields used in this study for both gases.

![](./images/813152750756954113_2.jpg)

Fig. 2 Comparison of simulated (open symbols) and experimental (closed symbols) pure component adsorption isotherms of (a) sulfur dioxide and (b) carbon monoxide in MFI at various temperatures. Experimental values of sulfur dioxide are taken from Deng and Lin. $^{68}$ The experimental values for carbon monoxide were measured in this work.

### 3.2. Isosteric heats of adsorption and Henry coefficients
Computed isosteric heats of adsorption for sulfur dioxide, carbon dioxide, and carbon monoxide as a function of the pore volume of the zeolites at 298 K are shown in Fig. 3. The results show higher absolute values of sulfur dioxide, following the trend $SO_2 > CO_2 > CO$ regardless of the zeolite. Similar trends were reported by Ding and Yazaydin $^2$ for several MOFs.

![](./images/813152750756954113_3.jpg)

Fig. 3 Computed isosteric heats of adsorption of carbon monoxide (red), carbon dioxide (blue), and sulfur dioxide (green) as a function of the pore volume of the structures at 298 K. Open symbols show the results obtained for channel-type zeolites and closed symbol for the interconnected cage-type zeolites. The directionality of the pore space is represented by circles (1D), squares (2D) or diamonds (3D).

---

This journal is © the Owner Societies 2014
Phys. Chem. Chem. Phys., 2014, 16, 19884-19893 | 19887

This behaviour can be related to the shape and size of the molecules in combination with the Coulombic interactions between the adsorbate and the adsorbent. Among the three gases, $SO_2$ is not only the biggest molecule (molecular diameter, 4.11–4.29 Å)⁴³,⁶⁹ but also has the highest dipole moment. More specifically, molecular size seems to be more important than polarity since the interaction with all zeolites is stronger for carbon dioxide (i.e., 3.90 Å)⁶⁹,⁷⁰ than for carbon monoxide (i.e., 3.69 Å).⁶⁹,⁷⁰ We also observed bigger differences among the values obtained for $SO_2$ since the fitting of the bulkier molecules is more dependent on the pore system. In a similar way, differences between the heats of adsorption of structures with similar topology and pore volume are larger for sulfur dioxide than for the other two molecules. As a general rule, zeolitic frameworks with high pore volumes exhibit low heats of adsorption for all three studied gases. Some structures such as MOR, AFY, and TER escape from this trend. To understand this anomalous behaviour we computed the average occupation profiles of the gases inside the structures.

For instance, the isosteric heats of adsorption of $SO_2$ and CO in MOR (1D channel-type zeolite) are higher than expected; the corresponding average occupation profiles depicted in Fig. 4 show that this is linked to the confinement effect of these gases at low coverage in the side pockets of MOR, being the preferential sites of adsorption.¹⁷ $SO_2$ and CO commensurate better than $CO_2$ in the pockets for a combined effect of geometry and polarity, thus the occupation density of the side pockets is larger for $SO_2$ followed by CO and $CO_2$. The average occupation profiles obtained for AFY (Fig. 4) also revealed the existence of specific adsorption sites for sulfur dioxide and carbon monoxide, while carbon dioxide is only adsorbed in the big straight channels of the host where the interaction with the structure is weaker.

The different behaviour of the heat of adsorption is due to the preferential sites of adsorption in which bulkier molecules fit better due to a mere size entropy effect (i.e., confinement).²⁷ In TER, a 2D channel-type structure, sulfur dioxide shows the highest occupation density of the sites, followed by carbon dioxide and carbon monoxide (Fig. S5 in ESI†). In zeolite TER, the intersections between the channels are the preferential adsorption sites, as opposed to other zeolites of the same group (SFG and NES) where molecules are preferentially adsorbed in the wide channels (Fig. S6 and S7 in ESI†). The aforementioned effect can also explain the differences in the heats of adsorption obtained for the three gases in LTL and DON (1D channel-type) or those found in MEL, MFI, ITR, and SZR (3D channel-type). As shown in the average occupation profiles obtained for MEL (Fig. 5) sulfur dioxide is preferentially adsorbed in the main straight interconnecting channels, whereas the molecules of carbon dioxide and carbon monoxide can also be found in the

![](./images/813152750756954113_4.jpg)

Fig. 4 Average occupation profiles obtained in AFY (top), and MOR (bottom) for one molecule of carbon monoxide (top right), carbon dioxide (bottom left), and sulfur dioxide (bottom right). The figure shows the projection of the center of mass of the molecules over $x-y$ (AFY) and $y-z$ (MOR) planes. The color graduation indicates the occupational density (from black to yellow). To guide the view we add a representation of the structures. The atomic structures are represented by the oxygen and silica atoms in red and yellow respectively. Grid surfaces where the accessible part appears in blue and the non-accessible part is colored in gray are also depicted.

![](./images/813152750756954113_5.jpg)

Fig. 5 Average occupation profiles obtained for one molecule of carbon monoxide (top right), carbon dioxide (bottom left), and sulfur dioxide (bottom right) in (a) MEL, (b) KFI and (c) SBE zeolites. The figures show the projections of the center of mass of the molecules over the $x-y$ plane. The color graduation indicates the occupational density (from black to yellow). To guide the view we add a representation of the structure (top left). The atomic structure is represented by the oxygen and silica atoms in red and yellow respectively. A grid surface is also depicted (where the accessible part is colored in blue and the non-accessible part is colored in gray).

intersections of the channels. For MFI the three gases follow the same trend as in MEL (Fig. S8 in ESI†), while the prefer- ential adsorption sites in ITR and SZR are the intersecting channels and the big straight channels respectively (Fig. S9 and S10 in ESI†).

A number of investigated structures have $SO_{2}$ and $CO_{2}$ preferential adsorption sites that are neither side pockets, straight channels nor intersecting channels. For example, the preferential sites of adsorption in the 2D cage-type structures MWW and KFI are the windows that communicate cages (Fig. S11 in ESI†). As a result, the heats of adsorption of $SO_{2}$ and $CO_{2}$ in KFI are higher than expected from general trends, since the gases are not adsorbed in the big cages but in a small cavity created by the windows between cages (Fig. 5). Similarly, the preferential adsorption sites for SBE (Fig. 5) and FAU (Fig. S12 in the ESI†) are the windows connecting big cages. Despite these two structures displaying among the highest pore volumes analyzed in this work, they also exhibit the highest values of heat of adsorption. This is contrary to the general trend: the larger the pore volume the lower the heat of adsorption. On the other hand, we did not observe a direct correlation between the topology of the zeolites and the iso- steric heats of adsorption. An observation that a local structure feature can dominate adsorption properties such as heat of adsorption and the Henry coefficient was recently used to develop an efficient screening approach for carbon capture materials. $^{71-74}$

The selectivity of the zeolites at low pressure for gas compo- nent i over j at a given temperature can be estimated using the ratio between the Henry coefficient of each gas $(K_{Hi}/K_{Hj})$ . The dependence of the selectivity at low coverage on the pore volume of the structure for $SO_{2}$ over $CO_{2}$ and $CO_{2}$ over CO at298 K is shown in Fig. 6a and 7a, respectively. The trends are similar to those obtained for the heats of adsorption, with higher selectivities obtained for the structures showing the lowest pore volumes. Again, MOR and AFY follow an anomalous trend of selectivity, with values for $SO_{2}/CO_{2}$ and $CO_{2}/CO$ larger and lower, respectively, than those of other structures with similar pore volumes. Also, those structures where bulky molecules fit better (MEL, MWW, SBE and FAU) exhibit higher selectivity of sulfur dioxide over carbon dioxide. In the case of $CO_{2}/CO$ selectivity, it follows the trend: 3D >2D > 1D for structures with similar pore volumes due to the appearance of preferential sites of adsorption at the inter- sections of the channels. In addition, the fact that the occupa- tion density of the preferential adsorption sites is higher in FAU than in SBE is the reason that leads to higher values of selectivity for the former than for the latter.

In summary: the highest values of heat of adsorption for carbon monoxide were found for JRY, FER, and FAU. These three structures also exhibit the strongest interaction with carbon dioxide. FER and MTF are the structures with higher selectivity of carbon dioxide over carbon monoxide. MOR and FAU are the structures with higher heats of adsorption for sulfur dioxide, and therefore with higher selectivity of sulfur dioxide over carbon dioxide.

![](./images/813152750756954113_6.jpg)

Fig. 6 (a) Computed Henry coefficients of sulfur dioxide over carbon dioxide at room temperature and (b) adsorption selectivity of sulfur dioxide over carbon dioxide, from the ternary mixture $(SO_{2},CO_{2}$ , and CO with ratio20:40:40) at room pressure and temperature. Both as a function of the pore volume of the structures. Open symbols show the results obtained for channel-type zeolites and closed symbols to the interconnected cage- type zeolites. The directionality of the pore space is represented by circles(1D), squares (2D), or diamonds (3D).

### 3.3. Adsorption selectivity from the ternary mixture
In a multicomponent system the adsorption selectivity of acomponent i over a component $j(S_{ij})$ is defined as $(x_{i}/y_{i})/(x_{j}/y_{j})$ where $x_{i, j}$ are the molar fractions in the adsorbed phase and $y_{i, j}$  the molar fractions in the bulk phase. Fig. 6b shows the adsorption selectivities of sulfur dioxide over carbon dioxide computed from the mixture $20 \% SO_{2}, 40 \% CO_{2}$ , and $40 \% CO$ at room temperature and atmospheric pressure. Table S8 in the ESI $\dagger$ collects the computed loading for each component in terms of mol of adsorbate per kilogram of structure, and the obtained values for the selectivity for each structure.

For the ternary mixture the highest adsorption was obtained for sulfur dioxide, the gas in the lowest proportion in the bulk, regardless of the zeolite structure. The adsorption of carbon dioxide is drastically reduced by the presence of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of of

![](./images/813152750756954113_7.jpg)

Fig. 7 (a) Computed Henry coefficients of carbon dioxide over carbon monoxide at room temperature and (b) adsorption selectivity of carbon dioxide over carbon monoxide, from the binary equimolar mixture at room pressure and temperature. Both as a function of the pore volume of the structures. Open symbols show the results obtained for channel-type zeolites and closed symbols to the interconnected cage-type zeolites. The directionality of the pore space is represented by circles (1D), squares (2D), or diamonds (3D).

Due to their low pore volumes, a few structures such as JRY, PON and ITW (1D channel-type), FER (2D channel-type), or STW (3D channels-type) show extremely high $SO_2/CO_2$ selectivities. In these structures the loading of carbon dioxide is extremely low, and the confinement effect of $SO_2$ (main component in the adsorbed phase) also enhances the $SO_2/CO_2$ selectivity. The packing effect of the gases gradually disappears in structures with higher pore volumes, leading to lower values of selectivity, with the exception of AFY (structure with high pore volume showing high selectivity). The heat of adsorption of sulfur dioxide in this zeolite was higher than in other structures with similar pore volume. This stronger interaction of $SO_2$ with the structure also implies higher loading of sulfur dioxide. The high heat of adsorption in combination with the size entropy effect previously described$^{27}$ explains the high selectivity for AFY. Due to the large pore volume of this structure this selectivity could be enhanced with a slight increase of the pressure.

At this stage it is important to highlight that some of the aforementioned different heats of adsorption at low coverage are not observed at higher coverages. As the preferential sites of adsorption at low coverage are filled and the gas loading rises (increasing pressure), molecules are adsorbed in other sites where the gas-host interaction is weaker. A good example of this behaviour is found in FAU, which exhibits an extremely high heat of adsorption for sulfur dioxide at zero loading. The preferential adsorption sites at low coverage for FAU are the windows that interconnect the big cages. The strength of the interaction is very high at the windows but not at the big cages. At higher loadings most molecules tend to be adsorbed in the latter and it is for this reason that the loading of sulfur dioxide and carbon dioxide at room pressure in the ternary mixtures is low and therefore the selectivity is also very low.

The $CO_2/CO$ selectivity for the ternary mixture under the studied conditions (ca. 20% $SO_2$, 40% $CO_2$, and 40% CO at room temperature and atmospheric pressure) cannot be obtained since the adsorption of carbon dioxide is drastically reduced by the presence of sulfur dioxide and the adsorption of carbon monoxide is almost negligible. For a good understanding of the competition of carbon dioxide and carbon monoxide, we performed adsorption isotherms for the equimolar binary mixture at room temperature and atmospheric pressure using the most representative structures of each group.

### 3.4. Adsorption selectivity from $CO_2/CO$ binary mixtures
Fig. 7b shows the $CO_2/CO$ adsorption selectivity for equimolar binary mixtures in several zeolites at atmospheric pressure and room temperature. Table S9 in the ESI† summarizes the loading of each gas in each structure as well as the adsorption selectivity. As predicted from the low coverage regime (Fig. 7b), $CO_2$ is selectively adsorbed over CO in all the structures, which is attributed to the bigger size of $CO_2$ that allows a better fit in the structures. Comparatively, carbon dioxide loading in the studied structures is lower than that of sulfur dioxide under the same conditions of pressure and temperature in the ternary mixture. Differences in the adsorbed amount between carbon monoxide from the binary mixture and sulfur dioxide from the ternary were about 1-3 mol kg⁻¹ lower in channel-type zeolites and 0.5-2 mol kg⁻¹ in interconnected cage-type. As in the case of the ternary mixtures, the selectivity is higher for the zeolites displaying low pore volumes. In addition, for a given pore volume it follows the trend: 3D > 2D > 1D due to the effect of the channel intersection previously explained.

In the binary $CO_2/CO$ mixture, the adsorption selectivity of all the structures shows the same trend described for the Henry coefficient selectivities. Unlike sulfur dioxide, the weaker interaction of $CO_2$ and CO with the structures reduces the loading, thus just low-medium coverage is reached under the given conditions of pressure and temperature. Therefore the behaviour is similar to that shown with the Henry coefficients. Only FAU showed lower adsorption selectivity than that expected from the Henry coefficients. This is due to the high pore volume of the zeolite and the low gas loading, avoiding the competition between both gases for the preferential sites of adsorption of the structure.

### 3.5. Self-diffusion and permselectivity from the ternary mixture
Table 2 shows the averaged self-diffusion coefficients, calculated for sulfur dioxide and carbon dioxide from the slope of the mean square displacement of the adsorbed molecules from

Table 2 Average self-diffusion coefficients for sulfur dioxide and carbon dioxide from the ternary mixture at fixed temperature (298 K), volume, and number of molecules. The number of molecules was taken from previous GCMC simulations of the ternary mixture at room pressure and temperature

<table>
  <thead>
    <tr>
      <th>Zeolite</th>
      <th>SO₂ self-diff. ($10^{-8}$ m² s⁻¹)</th>
      <th>CO₂ self-diff. ($10^{-8}$ m² s⁻¹)</th>
      <th>Zeolite</th>
      <th>SO₂ self-diff. ($10^{-8}$ m² s⁻¹)</th>
      <th>CO₂ self-diff. ($10^{-8}$ m² s⁻¹)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ASV</td>
      <td>0.047</td>
      <td>0.061</td>
      <td>MFI</td>
      <td>0.042</td>
      <td>0.035</td>
    </tr>
    <tr>
      <td>DON</td>
      <td>0.672</td>
      <td>0.916</td>
      <td>ITR</td>
      <td>0.126</td>
      <td>0.117</td>
    </tr>
    <tr>
      <td>ITW</td>
      <td>0.007</td>
      <td>0.007</td>
      <td>SBT</td>
      <td>0.545</td>
      <td>0.654</td>
    </tr>
    <tr>
      <td>JRY</td>
      <td>0.011</td>
      <td>0.01</td>
      <td>STW</td>
      <td>0.004</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>LAU</td>
      <td>0.005</td>
      <td>0.004</td>
      <td>SZR</td>
      <td>0.013</td>
      <td>0.029</td>
    </tr>
    <tr>
      <td>LTL</td>
      <td>0.049</td>
      <td>0.081</td>
      <td>ITQ-3</td>
      <td>0.004</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>MOR</td>
      <td>0.037</td>
      <td>0.111</td>
      <td>MTF</td>
      <td>0.003</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>NAT</td>
      <td>0.028</td>
      <td>0.024</td>
      <td>SAS</td>
      <td>0.031</td>
      <td>0.025</td>
    </tr>
    <tr>
      <td>PON</td>
      <td>0.002</td>
      <td>0</td>
      <td>DDR</td>
      <td>0.01</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>AFR</td>
      <td>0.069</td>
      <td>0.117</td>
      <td>LEV</td>
      <td>0.005</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>FER</td>
      <td>0.029</td>
      <td>0.057</td>
      <td>MWW</td>
      <td>0.149</td>
      <td>0.157</td>
    </tr>
    <tr>
      <td>IWV</td>
      <td>0.122</td>
      <td>0.179</td>
      <td>CHA</td>
      <td>0.016</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>NES</td>
      <td>0.146</td>
      <td>0.192</td>
      <td>ERI</td>
      <td>0.007</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>SFO</td>
      <td>0.066</td>
      <td>0.129</td>
      <td>FAU</td>
      <td>1.08</td>
      <td>1.43</td>
    </tr>
    <tr>
      <td>SFG</td>
      <td>0.067</td>
      <td>0.074</td>
      <td>ITQ-29</td>
      <td>0.035</td>
      <td>0.021</td>
    </tr>
    <tr>
      <td>TER</td>
      <td>0.073</td>
      <td>0.074</td>
      <td>KFI</td>
      <td>0.001</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>AFY</td>
      <td>0.028</td>
      <td>0.055</td>
      <td>PAU</td>
      <td>0.003</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>BEC</td>
      <td>0.417</td>
      <td>0.484</td>
      <td>RHO</td>
      <td>0.005</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>BOG</td>
      <td>0.175</td>
      <td>0.237</td>
      <td>SBE</td>
      <td>0.241</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td>MEL</td>
      <td>0.038</td>
      <td>0.034</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

![](./images/813152750756954113_8.jpg)

Fig. 8 Permselectivity of sulfur dioxide over carbon dioxide from the ternary mixture (SO₂, CO₂, and CO with a ratio of 20:40:40) at room pressure and temperature, as a function of the pore volume of the structures. Open symbols show the results obtained for channel-type zeolites and closed symbols to the interconnected cage-type zeolites. The directionality of the pore space is represented by circles (1D), squares (2D), or diamonds (3D). Zeolites with self-diffusion coefficients in orders between $10^{-8}$ and $10^{-9}$ m² s⁻¹ are colored in green, those around $10^{-10}$ m² s⁻¹ in red, and the rest in grey.

the ternary mixture as described above. This parameter was used to discard the zeolites in which the diffusion of sulfur dioxide and carbon dioxide is very low. Thus only zeolites with self-diffusivity values between $10^{-10}$ and $10^{-8}$ m² s⁻¹ were selected to analyze permselectivity. Permselectivity for SO₂ over CO₂ in these structures is depicted in Fig. 8, defined as the product of the adsorption selectivity and the diffusion selectivity.

In agreement with the results previously described, perm-selectivity is higher in structures with lower pore volume, showing JRY and NAT as the best structures for the separation of SO₂ from gas mixtures containing CO₂ and CO. It is interesting to highlight that there are some structures with low pore volume in which the packing effect made them to have extremely high adsorption selectivity. The synergy between the adsorption and diffusion of a mixture in zeolites for separation processes has been recently proven using both simulations and experiments.⁷⁵ Therefore, zeolites such as ITW, PON, and STW, which were initially considered good candidates based on their adsorption selectivity, are further discarded due to the poor diffusion. On the other hand, zeolite with high pore volume and high storage capacity, also has reasonable diffusion and shows high permselectivity. Therefore, this structure raises as a good candidate for the selective adsorption of sulfur dioxide over carbon dioxide, perhaps working at slightly higher pressures in order to improve its adsorption selectivity.

## 4. Conclusions

We employed a combination of experiments and molecular simulations to study adsorption and diffusion processes of sulfur dioxide, carbon dioxide, and carbon monoxide in zeolites. Our work shows that out of the three molecules, sulfur dioxide has the strongest interaction with the frameworks due to its largest size and polarity. We screened zeolite structures

taking into account not only low coverage adsorption properties but also the adsorption capacity, selectivity, and so forth at the temperature and/or pressure relevant to the separation process. This study outperforms previous studies and demonstrates that the prediction of materials for separation uses should be based on both adsorption and diffusion performance.

For the selective adsorption of $SO_2$ over $CO_2$ and CO at atmospheric pressure and room temperature, zeolitic structures with channel-type pore topology and low pore volumes, such as JRY or NAT, are the most adequate. However, to separate carbon dioxide from carbon monoxide as a second step of this removal process, higher pressures (or lower temperatures) would be necessary to improve the selectivity and adsorption capacity. On the other hand, structures with high pore volumes, such as AFY, FAU or SBE, could exhibit better storage capacity also working at higher pressure.

We reemphasize that each of the studied structures performs better under different conditions, and pose different opportunities for applications in adsorption, diffusion, and separation. Our study provides an interesting perspective to obtain useful information on their optimum working conditions in terms of pressure and temperature to achieve high gas adsorption capacities and $SO_2$ selectivity. This knowledge could be used for further enhancement of a variety of adsorption-separation processes.

## Acknowledgements
This work was supported by the Spanish "Ministerio de Ciencia e Innovación" (CTQ2010-16077/BQU), and the European Research Council through an ERC Starting Grant (ERC-StG'11 RASPA-project). A. Martín-Calvo thanks the Spanish "Ministerio de Educación" for her predoctoral fellowship. M. Haranczyk was supported by the Nanoporous Materials Genome Center for the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Chemical Sciences, Geosciences and Biosciences under Award DE-FG02-12ER1636.

## Notes and references
1 V. Gauci, N. Dise and S. Blake, *Geophys. Res. Lett.*, 2005, 32, L12804.

2 L. F. Ding and A. O. Yazaydin, *J. Phys. Chem. C*, 2012, 116, 22987-22991.

3 J. Yu, Y. Ma and P. B. Balbuena, *Langmuir*, 2012, 28, 8064-8071.

4 A. B. Rao and E. S. Rubin, *Environ. Sci. Technol.*, 2002, 36, 4467-4475.

5 D. Singh, E. Croiset, P. L. Douglas and M. A. Douglas, *Energy Convers. Manage.*, 2003, 44, 3073-3091.

6 M. V. Iyer, H. Gupta, B. B. Sakadjian and L.-S. Fan, *Ind. Eng. Chem. Res.*, 2004, 43, 3939-3947.

7 M. Hartman and O. Trnka, *AIChE J.*, 1993, 39, 615-624.

8 J. Y. Park, I. Tomicic, G. F. Round and J. S. Chang, *J. Phys. D: Appl. Phys.*, 1999, 32, 1006.

9 K. Oikawa, C. Yongsiri, K. Takeda and T. Harimoto, *Environ. Prog.*, 2003, 22, 67-73.

10 R. K. Srivastava, W. Jozewicz and C. Singer, *Environ. Prog.*, 2001, 20, 219-228.

11 V. C. Okay and W. L. Short, *Ind. Eng. Chem. Process Des. Dev.*, 1973, 12, 291-294.

12 S. C. Paik, H. Kim and J. S. Chung, *Catal. Today*, 1997, 38, 193-198.

13 H. Kim, D. Won Park, H. Chul Woo and J. Shik Chung, *Appl. Catal., B*, 1998, 19, 233-243.

14 V. Lachet, T. de Bruin, P. Ungerer, C. Coquelet, A. Valtz, V. Hasanov, F. Lockwood and D. Richon, *Energy Procedia*, 2009, 1, 1641-1647.

15 E. El Ahmar, B. Creton, A. Valtz, C. Coquelet, V. Lachet, D. Richon and P. Ungerer, *Fluid Phase Equilib.*, 2011, 304, 21-34.

16 S. Himeno, T. Tomita, K. Suzuki, K. Nakayama, K. Yajima and S. Yoshida, *Ind. Eng. Chem. Res.*, 2007, 46, 6989-6997.

17 E. Garcia-Perez, J. B. Parra, C. O. Ania, A. Garcia-Sanchez, J. M. van Baten, R. Krishna, D. Dubbeldam and S. Calero, *Adsorption*, 2007, 13, 469-476.

18 R. Krishna, J. M. van Baten, E. Garcia-Perez and S. Calero, *Chem. Phys. Lett.*, 2006, 429, 219-224.

19 R. Krishna, J. M. van Baten, E. Garcia-Perez and S. Calero, *Ind. Eng. Chem. Res.*, 2007, 46, 2974-2986.

20 M. D. Romero, G. Ovejero, A. Rodríguez and J. M. Gómez, *Microporous Mesoporous Mater.*, 2005, 81, 313-320.

21 J. García Martínez and J. Pérez Pariente, PhD thesis, Universidad de Alicante, 2003.

22 V. R. Choudhary, S. Mayadevi and A. P. Singh, *J. Chem. Soc., Faraday Trans.*, 1995, 91, 2935-2944.

23 V. R. Choudhary and S. Mayadevi, *Zeolites*, 1996, 17, 501-507.

24 J. A. Dunne, R. Mariwals, M. Rao, S. Sircar, R. J. Gorte and A. L. Myers, *Langmuir*, 1996, 12, 5888-5895.

25 J. A. Dunne, M. Rao, S. Sircar, R. J. Gorte and A. L. Myers, *Langmuir*, 1996, 12, 5896-5904.

26 O. Talu, M. S. Sun and D. B. Shah, *AIChE J.*, 1998, 44, 681-694.

27 R. Krishna, B. Smit and S. Calero, *Chem. Soc. Rev.*, 2002, 31, 185-194.

28 M. Schenk, S. Calero, T. L. M. Maesen, L. L. van Benthem, M. G. Verbeek and B. Smit, *Angew. Chem., Int. Ed.*, 2002, 41, 2499-2502.

29 G. N. Altshuler and G. Y. Shkurenko, *Bull. Acad. Sci. USSR, Div. Chem. Sci.*, 1990, 39, 1331.

30 J. P. Anerousis, *Chem. Eng.*, 1976, 83, 128.

31 X. Y. Zhang, Q. Shen, C. He, C. Y. Ma, J. Cheng and Z. P. Hao, *Catal. Commun.*, 2012, 18, 151-155.

32 M. P. Bernal, J. Coronas, M. Menendez and J. Santamaria, *AIChE J.*, 2004, 50, 127-135.

33 J. A. Delgado, M. A. Uguina, J. M. Gomez and L. Ortega, *Sep. Purif. Technol.*, 2006, 48, 223-228.

34 C. Baerlocher, L. B. McCusker and D. H. Olson, *Atlas of Zeolite Framework types*, Elsevier, London, 2007.

35 T. Düren, L. Sarkisov, O. M. Yaghi and R. Q. Snurr, *Langmuir*, 2004, 20, 2683-2689.

36 T. Düren and R. Q. Snurr, *J. Phys. Chem. B*, 2004, **108**, 15703-15708.

37 D. Dubbeldam, S. Calero, D. E. Ellis and R. Q. Snurr, *RASPA*, version 1.0, Northwestern University, Evanston, IL, 2008.

38 A. Garcia-Sanchez, C. O. Ania, J. B. Parra, D. Dubbeldam, T. J. H. Vlugt, R. Krishna and S. Calero, *J. Phys. Chem. C*, 2009, **113**, 8814-8820.

39 S. Calero, A. Martin-Calvo, S. Hamad and E. Garcia-Perez, *Chem. Commun.*, 2011, **47**, 508-510.

40 A. Martin-Calvo, F. D. Lahoz-Martin and S. Calero, *J. Phys. Chem. C*, 2012, **116**, 6655-6663.

41 J. J. Gutierrez-Sevillano, D. Dubbeldam, F. Rey, S. Valencia, M. Palomino, A. Martin-Calvo and S. Calero, *J. Phys. Chem. C*, 2010, **114**, 14907-14914.

42 D. Frenkel and B. Smit, *Understanding Molecular Simulations: From Algorithms to Applications*, 2nd edn, 2002.

43 J.-R. Li, R. J. Kuppler and H.-C. Zhou, *Chem. Soc. Rev.*, 2009, **38**, 1477-1504.

44 National Institute of Standards and Technology, http://www.nist.gov/index.html, Accessed January, 2013.

45 M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids*, Oxford Clarendon Press, 1987.

46 C. Vega, B. Garzon, L. G. MacDowell, P. Padilla, S. Calero and S. Lago, *J. Phys.: Condens. Matter*, 1996, **8**, 9643.

47 T. F. Willems, C. H. Rycroft, M. Kazi, J. C. Meza and M. Haranczyk, *Microporous Mesoporous Mater.*, 2012, **149**, 134-141.

48 Zeo++, www.carboncapturematerials.org/Zeo++ Accessed May 2013.

49 M. D. Foster, I. Rivin, M. M. J. Treacy and O. Delgado Friedrichs, *Microporous Mesoporous Mater.*, 2006, **90**, 32-38.

50 T. Wessels, C. Baerlocher, L. B. McCusker and E. J. Creyghton, *J. Am. Chem. Soc.*, 1999, **121**, 6242-6247.

51 G. Artioli and K. Stahl, *Zeolites*, 1993, **13**, 249-255.

52 J. M. Newsam, *J. Phys. Chem.*, 1989, **93**, 7689-7694.

53 V. Gramlich, PhD thesis, ETH, Zürich, Switzerland, 1971.

54 R. E. Morris, S. J. Weigel, N. J. Henson, L. M. Bull, M. T. Janicke, B. F. Chmelka and A. K. Cheetham, *J. Am. Chem. Soc.*, 1994, **116**, 11849-11855.

55 J. J. Pluth and J. V. Smith, *Am. Mineral.*, 1990, **75**, 501-507.

56 C. A. Fyfe, H. Gies, G. T. Kokotailo, C. Pasztor, H. Strobl and D. E. Cox, *J. Am. Chem. Soc.*, 1989, **111**, 2470-2474.

57 H. van Koningsveld, H. van Bekkum and J. C. Jansen, *Acta Crystallogr., Sect. B: Struct. Crystallogr. Cryst. Chem.*, 1987, **43**, 127-132.

58 M. A. Camblor, A. Corma, P. Lightfoot, L. A. Villaescusa and P. A. Wright, *Angew. Chem., Int. Ed. Engl.*, 1997, **36**, 2659-2661.

59 H. Gies, *Z. Kristallogr.*, 1986, **175**, 93-104.

60 S. Merlino, E. Galli and A. Alberti, *Tschermaks Mineral. Petrogr. Mitt.*, 1975, **22**, 117-129.

61 M. Calligaris, G. Nardin and L. Randaccio, *Zeolites*, 1983, **3**, 205-208.

62 J. A. Gard and J. M. Tait, *Proc., 3rd, Int. Conf. Molecular Sieves*, 1973, 94-99.

63 J. A. Hriljac, M. M. Eddy, A. K. Cheetham, J. A. Donohue and G. J. Ray, *J. Solid State Chem.*, 1993, **106**, 66-72.

64 A. Corma, F. Rey, J. Rius, M. J. Sabater and S. Valencia, *Nature*, 2004, **431**, 287-290.

65 J. B. Parise, R. D. Shannon, E. Prince and D. E. Cox, *Z. Kristallogr.*, 1983, **165**, 175-190.

66 E. K. Gordon, S. Samson and W. B. Kamb, *Science*, 1966, **154**, 1004-1007.

67 L. B. McCusker and C. Baerlocher, *J. Solid State Chem.*, 1984, **812-822**.

68 S. G. Deng and Y. S. Lin, *Ind. Eng. Chem. Res.*, 1995, **34**, 4063-4070.

69 J. O. Hirschfelder, C. F. Curtiss and R. B. Bird, *Molecular theory of gases and liquids*, Wiley, New York, 1954.

70 S. Sircar, *Ind. Eng. Chem. Res.*, 2006, **45**, 5435-5448.

71 J. Kim, M. Abouelnasr, L.-C. Lin and B. Smit, *J. Am. Chem. Soc.*, 2013, **135**, 7545-7552.

72 L.-C. Lin, A. H. Berger, R. L. Martin, J. Kim, J. A. Swisher, K. Jariwala, C. H. Rycroft, A. S. Bhown, M. Deem, M. Haranczyk and B. Smit, *Nat. Mater.*, 2012, **11**, 633-641.

73 R. L. Martin, T. F. Willems, L. C. Lin, J. Kim, J. A. Swisher, B. Smit and M. Haranczyk, *ChemPhysChem*, 2012, **13**, 3595-3597.

74 J. Kim, L.-C. Lin, J. A. Swisher, M. Haranczyk and B. Smit, *J. Am. Chem. Soc.*, 2012, **134**, 18940-18943.

75 T. Titze, C. Chmelik, J. Kärger, J. M. van Baten and R. Krishna, *J. Phys. Chem. C*, 2014, **118**, 2660-2665.