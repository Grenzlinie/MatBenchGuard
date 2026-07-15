# Modeling the Competitive Adsorption of Water and Methanoic Acid on Calcite and Fluorite Surfaces

N. H. de Leeuw*,† and S. C. Parker‡

School of Chemistry, University of Bath, Claverton Down, Bath BA2 7AY, U.K.

K. Hanumantha Rao

Division of Mineral Processing, Luleå University of Technology S-97187 Luleå, Sweden

Received March 6, 1998. In Final Form: July 16, 1998

Atomistic simulation techniques were used to investigate the interaction between the minerals calcite and fluorite with water and methanoic acid. The relative adsorption energies suggest that methanoic acid preferentially adsorbs onto fluorite surfaces, while adsorption of water is energetically preferred over methanoic acid on the calcite cleavage plane in agreement with experiment. The coverage and configuration of adsorbed methanoic acid on the surfaces depends largely on lattice spacing between the cations, and bridging between surface calcium atoms is highly favored. These findings have given an insight into interactions at the atomic level which indicate that modeling techniques should be capable of predicting adsorption behavior and designing collector molecules, which is of central importance to the mineral processing technique of flotation.

## Introduction

Flotation is the process of attachment of mineral particles to the liquid/gas interface whereby the conditions of equilibrium are based on a comparison of the magni- tudes of the initial and final free energies for attachment of a bubble to a particle in an isolated system.¹ Originally used in the mining industry for the concentration of mineral ores,²,³ the depletion of mineral ores and envi- ronmental concern has made it an important separation process in many fields, from mineral processing⁴ to water purification and the treatment of industrial wastewater⁵ and sewage,⁶ and hydrometallurgy.⁷,⁸ In view of its significance it is important to understand the underlying processes which influence the efficiency of the flotation process.

The separation is based on the selective adsorption of collectors (surfactants) to the component of interest thereby giving it a hydrophobic surface.⁹ The hydrophobic solid particles thus obtained attach to bubbles dispersed through the liquid, which can be generated in a variety of methods,⁷,⁸,10−13 and then rise to the surface where they are skimmed off.³ Minerals can often be floated using a range of different collectors as for instance in the work of Zhao et al.,¹⁴ who used both ion flotation and adsorbing colloid flotation when removing molybdate and arsenate from aqueous solution. However, different minerals have different flotation rates for certain collectors and when separating more than one mineral from a solution, selective hydrophobisation is a critical factor in an effective flotation scheme.¹⁵

It is often difficult to determine experimentally the fundamental processes affecting the separation process. Computational techniques, however, are well placed to investigate at the atomic level the interactions between solid and adsorbate. Atomistic simulations have been successful in accurately predicting the structures and properties of a wide range of minerals, including crystal morphology,¹⁶,¹⁷ surface structure,¹⁸−²⁰ and adsorption behavior.²¹−²³ The aim of this study is therefore to use atomistic simulations to investigate the interactions of adsorbing species with the surfaces of two important minerals, namely calcite, $CaCO_3$, and fluorite, $CaF_2$. Calcite especially has been the subject of several experi- mental flotation studies, for example, surfactant adsorp- tion on apatite and calcite¹⁵ and flotation rates of calcite.²⁴ One of the most widely used surfactants for collecting

* To whom correspondence should be addressed.
† E-mail: n.h.deleeuw@bath.ac.uk.
‡ E-mail: s.c.parker@bath.ac.uk.

(1) Singh, B. P. *Langmuir* **1994**, *10*, 510.
(2) Zouboulis, A. I.; Kydros, K. A.; Matis, K. A. *Sep. Sci. Technol.* **1992**, *27*, 2143.
(3) Loewenberg, M.; Davis, R. H. *Chem. Eng. Sci.* **1994**, *49*, 3923.
(4) Moolman, D. W.; Aldrich, C.; Van Deventer, J. S. J. *Chem. Eng. Sci.* **1995**, *50*, 3501.
(5) Cabezon, L. M.; Caballero, M.; Perez-Bustamante, J. A. *Sep. Sci. Technol.* **1994**, *29*, 1491.
(6) Kydros, K. A.; Gallios, G. P.; Matis, K. A. *Sep. Sci. Technol.* **1994**, *29*, 2263.
(7) Zouboulis, A. I.; Zamboulis, D.; Matis, K. A. *Sep. Sci. Technol.* **1991**, *26*, 355.
(8) Lazaridis, N. K.; Matis, K. A.; Stalidis, G. A.; Mavros, P. *Sep. Sci. Technol.* **1992**, *27*, 1743.
(9) Miller, J. D.; Yalamanchili, M. R. *Langmuir* **1992**, *8*, 1464.
(10) Peng, F. F.; Di, P. *Ind. Eng. Chem. Res.* **1994**, *33*, 922.
(11) Armstrong, D. W.; Zhou, E. Y.; Chen, S.; Le, K.; Tang, Y. *Anal. Chem.* **1994**, *66*, 4278.

(12) Kydros, K. A.; Gallios, G. P.; Matis, KA., *J. Chem. Technol. Biotechnol.* **1994**, *59*, 223.
(13) Sadowski, Z. *Powder Technol.* **1994**, *80*, 93.
(14) Zhao, Y.; Zouboulis, A. I.; Matis, K. A. *Sep. Sci. Technol.* **1996**, *31*, 769.
(15) Bjorklund, R. B.; Arwin, H. *Langmuir* **1992**, *8*, 1709.
(16) Didymus, J. M.; Oliver, P.; Mann, S.; De Vries, A. L.; Hauschka, P. V.; Westbroek, P. J. *Chem. Soc., Faraday Trans.* **1993**, *89*, 2891.
(17) Oliver, P. M.; Parker, S. C.; Mackrodt, W. C. *Modell. Simul. Mater. Sci. Eng.* **1993**, *1*, 755.
(18) Parker, S. C.; Kelsey, E. T.; Oliver, P. M.; Titiloye, J. O. *Faraday Discuss.* **1993**, *95*, 75.
(19) Davies, M. J.; Parker, S. C.; Watson, G. W. *J. Mater. Chem.* **1994**, *4*, 813.
(20) Purton, J.; Bullett, D. W.; Oliver, P. M.; Parker, S. C. *Surf. Sci.* **1995**, *336*, 166.
(21) de Leeuw, N. H.; Watson, G. W.; Parker, S. C. *J. Phys. Chem.* **1995**, *99*, 17219.
(22) de Leeuw, N. H.; Watson, G. W.; Parker, S. C. *J. Chem. Soc., Faraday Trans.* **1996**, *92*, 2081.
(23) de Leeuw, N. H.; Parker, S. C. *J. Chem. Soc., Faraday Trans.* **1997**, *93*, 467.

SO743-7463(98)00269-8 CCC: $15.00
© 1998 American Chemical Society
Published on Web 09/12/1998

mineral particles is sodium oleate $^{25-27}$ which floats fluorite preferentially from a solution containing both calcite and fluorite. Adsorption on calcite, for example, occurs at an equilibrium concentration of nearly two orders of mag- nitude greater than that on fluorite. $^{28-30}$ Apart from relative concentrations $^{14}$ and the occurrence of cross linking between adsorbed collector molecules, $^{31}$ the in teractions between collector molecules and the mineral surface have been shown to be mainly electrostatic in nature. $^{32}$ In our first computational study of adsorption of collector molecules to mineral surfaces, we have concentrated on the competitive adsorption of water molecules and methanoic acid molecules. Methanoic acid was chosen because it has the same functional group as oleic acid except that it does not have the long hydrocarbon tail and should therefore be a good model to study electrostatic interactions between mineral and collector.

## Theoretical Methods

Atomistic simulation techniques are currently more appropriate than full electronic structure calculations for modeling the geometry and energies of adsorption of molecules on the mineral surfaces because the necessity to study partial coverages requires us to consider large numbers of atoms which makes ab initio calculations computationally prohibitive. Atomistic simulation tech- niques are based on the Born model of solids, $^{33}$ which assumes that the atoms interact via long-range electro- static forces and short-range forces which include both the repulsions and van der Waals attractions between neighboring electron charge clouds. The electronic po- larizability of the atoms is included via the shell model of Dick and Overhauser $^{34}$ in which each polarizable atom, in our case oxygen and fluorine, is represented by a core and a massless shell, connected by a spring. The polar- izability of the model atom is then determined by the spring constant and the charges of core and shell. These are usually obtained by fitting to experimental dielectric data when available. In addition, it is often necessary to include angle-dependent forces to allow for directionality of (partially) covalent bonds, as for example in the carbonate anion. In this study of the adsorption of organic molecules to mineral surfaces, we have used static energy minimi- zation techniques which are most efficient in identifying the strength of interaction with specific surface features. The simulation code METADISE $^{35}$ was employed which is designed to model dislocations, surfaces, and inter-faces. In this code, following the approach by Tasker, $^{36}$  the crystal comprises two blocks, each consisting of two regions which are periodic in two dimensions. The two blocks together model the bulk crystal while a single block represents the surface. Region I contains those atoms near the extended defect, in this case the surface layer and a few layers immediately below, while region II contains those atoms further away and represents the rest of the crystal. The ions in region I are allowed to relax to their mechanical equilibrium, but those in region II are kept fixed at their bulk equilibrium position although the region as a whole is allowed to move with respect to region I. Both region I and region II need to be sufficiently large to ensure convergence of the energies. The energies of the blocks are essentially the sum of the energies of interaction between all atoms. The long-range Coulombicinteractions are calculated by the Parry method, $^{37,38}$  whereas the short-range terms are described by param- etrized analytical expressions.

The stability of the mineral surfaces is determined by the surface energy, $\gamma$ , which is evaluated from the energy of the surface block of the crystal $U_{s}$ and the energy of a portion of bulk crystal $U_{b}$ , containing the same number of atoms as the surface block

$$
\gamma=\frac{U_{\mathrm{s}}-U_{\mathrm{b}}}{A} \tag{1}
$$

where $A$ is the surface area. The adsorption energies $(U_{ads})$ were calculated by comparing the energy of the pure surface $(U_{s})$ and that of an isolated water or methanoic acid molecule $(U_{mol})$ with the energy of the covered surface(Udef):

$$
U_{\mathrm{ads}}=U_{\mathrm{def}}-\left(U_{\mathrm{s}}+U_{\mathrm{mol}}\right) \tag{2}
$$

We need to be confident that the most stable adsorption configuration is located, particularly as the coverage may be varied due to the various lattice spacings on the different surfaces and the size of the adsorbing molecules. As such, many configurations needed to be investigated, and the energies quoted in later sections refer to the energetically most stable configuration obtained.

The potential parameters used for the simulation of the calcite crystal are those derived by Pavese et al. $^{39}$ in their study of the thermal dependence of structural and elastic properties of calcite while the potential model used for fluorite was derived by Catlow et al. $^{40}$ The inter- and intramolecular interactions of the water molecules were derived by ourselves, $^{41}$ while the interactions between water and mineral surfaces were fitted following the approach by Schroder et al. $^{42}$ allowing for the fractional charges of the atoms in the water molecule. The calcite/ water interactions were verified against the structure of the calcium carbonate hexahydrate ikaite as described previously, $^{43}$ and the close agreement between experi mental and calculated structure and formation energies means that we may be confident that the potential parameters describe the water/surface interactions ad- equately. The methanoic acid molecule was modeled using the cvff force field from the Insight II package as supplied by Molecular Simulations Inc. The interactions between

(24) De Castro, F. H. B.; De Hoces, M. C. Chem. Eng. Sci. 1996, 51,119.
(25) Ince, D. E.; Johnston, C. T.; Moudgil, B. M. Langmuir 1991, 7,1453.
(26) De Castro, F. H. B.; Borrego, A. G. J. Colloid Interface Sci. 1995,173,8.
(27) Ghazy, S. E.; Kabil, M. A.; Abeidu, A. M.; El-Metwally, N. M. Sep. Sci. Technol. 1996, 31, 829.
(28) Hanumantha Rao, K.; Antti, B.-M.; Forssberg, K. S. E. Colloid Surf. 1988/89, 34, 227.
(29) Hanumantha Rao, K.; Cases, J. M.; de Donato, P.; Forssberg, K. S. E. J. Colloid Interface Sci. 1991, 145, 314.
(30) Hanumantha Rao, K.; Cases, J. M.; Forssberg, K. S. E. J. Colloid Interface Sci. 1991, 145, 330.
(31) Arad, D.; Kaftory, M.; Zolotoy, A. B.; Finkelstein, N. P.; Weissman, A. Langmuir 1993, 9, 1446.
(32) Hancer, M.; Celik, S. Sep. Sci. Technol. 1993, 28, 1703.
(33) Born, M.; Huang, K. Dynamical Theory of Crystal Lattices, Oxford University Press: Oxford, England, 1954.
(34) Dick, B. G.; Overhauser, A. W. Phys. Rev. 1958, 112, 90.
(35) Watson, G. W.; Kelsey, E. T.; de Leeuw, N. H.; Harris, D. J.; Parker, S. C. J. Chem. Soc., Faraday Trans. 1996, 92, 433.
(36) Tasker, P. W. Philos. Mag. A. 1979, 39, 119.

(37) Parry, D. E. Surf. Sci. 1975, 49, 433.
(38) Parry, D. E. Surf. Sci. 1976, 54, 195.
(39) Pavese, A.; Catti, M.; Parker, S. C.; Wall, A. Phys. Chem. Miner.1996, 23, 89.
(40) Catlow, C. R. A.; Norgett, M. J.; Ross, A. J. Phys. C 1977, 10,1630.
(41) de Leeuw, N. H.; Parker, S. C. Phys. Rev. B 1998, in press.
(42) Schroder, K. P.; Sauer, J.; Leslie, M.; Catlow, C. R. A. Chem. Phys. Lett. 1992, 188, 320.
(43) de Leeuw, N. H.; Parker, S. C. J. Phys. Chem. B 1998, 102, 2914.

![](./images/812745808322494468_1.jpg)

Figure 1. (a) Sideview of the calcite $\{10\overline{1}4\}$ surface, showing the calcium atoms as balls and the carbonate groups as three-spoked wheels. (b) Plan view showing the interatomic spacings between surface calcium atoms. Key: Ca = medium gray; O = black; C = light gray.

the minerals and the methanoic acid molecules were again adapted according to the charges on the atoms.

## Results

### Pure Surfaces of Calcite and Fluorite.
Calcite has a rhombohedral crystal structure with space group $R\overline{3}c$ and a cleavage structure not unlike distorted rock salt. $^{44}$ The $\{10\overline{1}4\}$ cleavage plane is by far the most stable surface of calcite and dominates the morphology, usually to the exclusion of other surfaces both under ultrahigh vacuum conditions $^{16,45,46}$ and in an aqueous environment. $^{23,47,48}$ We may therefore expect the calcite crystals in the mineral mixture to mainly show the $\{10\overline{1}4\}$ surface and as such we have concentrated on this surface. The surface consists of layers of both calcium atoms and two differently oriented but otherwise equivalent carbonate groups (Figure 1). The calcium, carbon, and one of the carbonate oxygen atoms lie in the same plane while the other two oxygen atoms protrude above and below this plane (Figure 1a). Both calcium atoms and oxygen atoms are easily accessible to adsorbing molecules from solution.

Fluorite has a cubic crystal structure with spacegroup $Fm\overline{3}m$. Three surfaces were considered: the $\{111\}$ cleavage plane, and also the $\{011\}$ and the $\{310\}$ surfaces. The $\{111\}$ surface (Figure 2) consists of planes of calcium ions in a hexagonal array with a layer of fluorine ions both above and below. The surface is thus terminated with fluorine atoms although the calcium ions are still accessible to adsorbing molecules. The $\{011\}$ (Figure 3a) and $\{310\}$ (Figure 3b) surfaces have both calcium ions and fluorine ions in the surface layer. The surface energies of the pure surfaces were calculated and are collected in Table 1. It is clear that of the fluorite surfaces the $\{111\}$ cleavage plane is as expected the most stable surface with the lowest surface energy. The $\{011\}$ also has a fairly low surface energy but the $\{310\}$ surface has a much higher surface energy and is thus a relatively unstable surface in fluorite.

![](./images/812745808322494468_2.jpg)

Figure 2. (a) Side view of the fluorite $\{111\}$ surface, showing the crystal as a framework. (b) Plan view showing the interatomic spacing between surface calcium atoms. Key: Ca = medium gray; F = light gray.

### Hydration of the Calcite and Fluorite Surfaces.
Associative adsorption of water molecules onto the calcite $\{10\overline{1}4\}$ plane has stabilized the surface to a large extent and it remains the dominant surface. $^{23,43}$ The surface energy of the hydrated surface $(\gamma = 0.17\ \text{J m}^{-2})$ is in good agreement with the surface energy found experimentally for the cleavage plane of calcite of $0.23\ \text{J m}^{-2}^{49}$ particularly when taking into account that the experimental surface was mechanically cut and will contain steps and other dislocations which will increase the surface energy. The lattice spacing (Ca-Ca = 4.0 and 4.8 Å (Figure 1b)) is large enough for a water molecule to adsorb by its oxygen atom to each calcium atom in a herringbone pattern (Figure 4). Both hydrogen atoms are hydrogen-bonded to two lattice oxygen atoms and at full monolayer coverage the two differently oriented carbonate groups are still equivalent. The surface exhibits $1 \times 1$ symmetry in accordance with the AFM images of the $\{10\overline{1}4\}$ plane of calcite in water by Ohnesorge and Binnig. $^{47}$ The hydration energy of $-92.2\ \text{kJ mol}^{-1}$ is in good agreement with the binding energy of $-110.9\ \text{kJ mol}^{-1}$ quoted by Liang et al. (1996) for water molecules adsorbed onto calcite.

(44) Liang, Y.; Lea, A. S.; Baer, D. R.; Engelhard, M. H. *Surf. Sci.* 1996, 351, 172.
(45) Beruto, D.; Giordani, M. *J. Chem. Soc., Faraday Trans.* 1993, 89, 2457.
(46) Goni, S.; Sobrados, L.; Hernandez, M. S. *Solid State Ionics* 1993, 63-65, 786.
(47) Ohnesorge, F.; Binnig, G. *Science* 1993, 260, 1451.
(48) Heywood, B. R.; Mann, S. *Chem. Mater.* 1994, 6, 311.

(49) Gilman, J. J. *J. Appl. Phys.* 1960, 31, 2208.

![](./images/812745808322494468_3.jpg)

Figure 3. Plan view of (a) the fluorite {011} and (b) the fluorite {310} surfaces, showing the interatomic spacing between surface calcium atoms. Key: Ca = medium gray; F = light gray.

![](./images/812745808322494468_4.jpg)

Figure 4. Plan view of the calcite {10$\overline{1}$4} surface with adsorbed water molecules, showing the calcium atoms as balls and the carbonate groups as three-spoked wheels and the water molecules space-filled. Key: Ca = medium gray; $O_{lattice}$ = black; C = light gray; $O_{water}$ = very light gray; H = white.

<table>
<caption>Table 1. Surface Energies of Pure and Hydrated Calcite and Fluorite</caption>
<thead>
<tr>
<th rowspan="2">mineral</th>
<th rowspan="2">surface</th>
<th colspan="2">surface energies/J m⁻²</th>
</tr>
<tr>
<th>unhydrated</th>
<th>hydrated</th>
</tr>
</thead>
<tbody>
<tr>
<td>calcite</td>
<td>{10$\overline{1}$4}</td>
<td>0.59</td>
<td>0.17</td>
</tr>
<tr>
<td>fluorite</td>
<td>{011}</td>
<td>0.82</td>
<td>0.90</td>
</tr>
<tr>
<td></td>
<td>{111}</td>
<td>0.52</td>
<td>0.40</td>
</tr>
<tr>
<td></td>
<td>{310}</td>
<td>1.56</td>
<td>0.67</td>
</tr>
</tbody>
</table>

After hydration of the fluorite surfaces, the trend in surface energies with respect to the pure surfaces has reversed. The {111} surface is still the dominant surface, but while the surface energy of the {011} surface has risen indicating that hydration of this surface has a destabilizing effect, the surface energy of the {310} surface has decreased considerably and thus hydration of this surface has a stabilizing effect.

![](./images/812745808322494468_5.jpg)

Figure 5. Plan view of the fluorite (a) {111}, (b) {011}, and (c) {310} surfaces with adsorbed water molecules, showing the crystal as a framework and the water molecules space-filled. Key: Ca = medium gray; F = light gray; O = black; H = white.

On both the {011} and the {310} surfaces the spacings between the calcium atoms, at 3.85 and 5.44 Å for the {011} (Figure 3a) and 5.44 and 8.60 Å for the {310} (Figure 3b) surface, are sufficient to allow a water molecule to adsorb to each calcium atoms by its oxygen atom at 2.4 Å. On the {011} surface the water molecules adsorb in an upright fashion with their hydrogen atoms directed away from the surface and no hydrogen-bonding to the surface or intermolecular interactions between the water molecules occur (Figure 5b). On the {310} surface the water molecules adsorb in a flat fashion and hydrogen-bonding occurs to the surface fluorine atoms at a distance of about 2.15 Å (Figure 5c). The difference in hydration energies and the destabilization of the {011} surface is probably due to this different mode of adsorption. The hydrated {310} surface is a much smoother plane than the hydrated {011} surface, and the presence of extensive hydrogen bonding of both hydrogen atoms to surface fluorine atoms in addition to the calcium−oxygen interactions on the {310} surface leads to the particularly large hydration energy.

On the {111} surface however, the hexagonal pattern of surface calcium atoms (and fluorine atoms) with interatomic spacing of 3.85 Å is too small for a water molecule to adsorb on each calcium atom, and instead only 50% of the available adsorption sites are covered by water molecules (Figure 5a). The calcium−oxygen distance at 2.47 Å is somewhat larger than on the other surfaces, due to the fact that the topmost plane is a layer of fluorine atoms. The water molecules adsorb flat onto the surface while hydrogen-bonding to the surface fluorine atoms at 2.13 and 2.18 Å.

**Adsorption of Methanoic Acid on Calcite and Fluorite Surfaces.** We next considered adsorption of methanoic acid molecules to the various surfaces. On

![](./images/812745808322494468_6.jpg)

Figure 6. Plan view of the calcite $\{10\overline{1}4\}$ surface with adsorbed methanoic acid, showing the calcium atoms as balls and the carbonate groups as three-spoked wheels and the methanoic acid molecules space-filled. Key: Ca = medium gray; O = black; C = light gray; H = white.

![](./images/812745808322494468_7.jpg)

Figure 7. Side view of the fluorite {011} surface, showing the crystal as a lattice framework (Ca = black; F = light gray) and the methanoic acid molecule (space-filled O = dark gray; C = very light gray; H = white) coordinated by its oxygen atoms to two surface calcium atoms.

calcite the lattice spacing was large enough to allow full monolayer coverage of water molecules onto the $\{10\overline{1}4\}$ surface. However, the methanoic acid molecules are too large for one molecule to be accommodated per calcium atom. Instead, only one methanoic acid molecule is adsorbed for each two surface calcium atoms in a regular pattern (Figure 6). The doubly bonded oxygen atom becomes bonded to a surface calcium atom at $2.2$ Å, and the oxygen of the hydroxyl group is directed toward a neighboring surface calcium atom while its hydrogen atom coordinates to a surface oxygen atom $(2.5$ Å). The other hydrogen atom is situated above another surface oxygen atom $(2.6$ Å).

The methanoic acid molecules adsorb onto the fluorite surfaces in three distinctly different fashions. On the {011} surface the lattice spacing is large enough to allow full monolayer coverage with one methanoic acid molecule per surface calcium. The methanoic acid molecule adsorbs with both oxygen atoms to two surface calcium atoms, bridging between them (Figure 7). The doubly bonded oxygen atom closely coordinates to the calcium atom at a distance of $2.2$ Å while the oxygen atom of the hydroxyl group is at $2.65$ Å from the second calcium atom. The hydrogen atom of the hydroxyl group relaxes into the fluorite surface and coordinates to a fluorine atom at $2.4$ Å.

![](./images/812745808322494468_8.jpg)

Figure 8. Plan view of the fluorite {111} surface with adsorbed methanoic acid molecule showing the crystal as a lattice framework (Ca = black; F = light gray) and the methanoic acid molecule space filled (O = dark gray; C = very light gray; H = white).

![](./images/812745808322494468_9.jpg)

Figure 9. Sideview of the fluorite {310} surface, showing the crystal as a lattice framework (Ca = black; F = light gray) and the methanoic acid molecule (space-filled O = dark gray; C = very light gray; H = white) closely coordinated by its doubly bonded oxygen atom to a surface calcium atom, while being hydrogen-bonded to a surface fluorine by one of its hydrogen atoms.

On the {111} surface, the interatomic distance is much smaller and only a 50% coverage can be accommodated. The methanoic acid molecules adsorb in a fairly flat configuration onto the surface, bridging between two calcium atoms with both oxygen atoms coordinated to a calcium at $2.2$ Å for the doubly bonded oxygen atom and at $2.9$ Å for the oxygen atom of the hydroxyl group (Figure 8). The hydrogen atom of the hydroxyl group coordinates to two surface fluorine atoms at $2.5$ and $2.7$ Å.

The lattice spacing on the {310} surface is again large enough to accommodate full monolayer coverage of the methanoic acid molecules (Figure 9). The doubly bonded oxygen atom is bonded to a surface calcium atom at $2.15$ Å, while more loosely coordinated to calcium atoms farther away in the next layer $(3.93$ Å). Furthermore, the doubly bonded oxygen atoms coordinate intramolecularly to hydroxyl hydrogen atoms of other adsorbed methanoic acid molecules $(2.4$ Å). The hydrogen atoms bonded to the carbon atoms coordinate attractively to surface fluorine atoms $(2.35$ Å).

<table>
<caption>Table 2. Adsorption Energies for Water and Methanoic Acid onto Calcite and Fluorite</caption>
<thead>
<tr>
<th rowspan="2">mineral</th>
<th rowspan="2">surface</th>
<th colspan="2">adsorption energies/kJ mol⁻¹</th>
</tr>
<tr>
<th>water</th>
<th>methanoic acid</th>
</tr>
</thead>
<tbody>
<tr>
<td>calcite</td>
<td>{10$\overline{1}$4}</td>
<td>−92.2</td>
<td>−84.2</td>
</tr>
<tr>
<td>fluorite</td>
<td>{011}</td>
<td>−33.4</td>
<td>−97.3</td>
</tr>
<tr>
<td></td>
<td>{111}</td>
<td>−61.8</td>
<td>−102.4</td>
</tr>
<tr>
<td></td>
<td>{310}</td>
<td>−250.7</td>
<td>−110.9</td>
</tr>
</tbody>
</table>

## Discussion

The adsorption energies for both water and methanoic acid onto the mineral surfaces are collected in Table 2. The hydration energies for the different fluorite surfaces vary considerably due to the presence (or absence) of hydrogen-bonding to the surface fluorine atoms, in addition to the calcium−oxygen interactions. The adsorption energies for methanoic acid onto the mineral surfaces are larger for fluorite than for calcite, and as such methanoic acid would preferentially adsorb to fluorite over calcite when both minerals are present in the mixture.

Furthermore, the adsorption energy for water on calcite is larger than for methanoic acid, probably due to both the very regular pattern of water adsorption with a network of hydrogen-bonding to surface oxygen atoms and some steric effects of the larger acid molecules. Hence, the methanoic acid, which as a collector molecule would be added to the minerals in the aqueous medium, would not be capable of displacing water from the calcite surface. Similarly, the very large hydration energy for the fluorite {310} surface means that on this plane the methanoic acid molecules are not capable of displacing water from the surface. However, for both the fluorite {011} and the dominant {111} surfaces, the adsorption energies for methanoic acid are considerably larger than that for water due to the capability of the acid molecules to bridge by their oxygen atoms between two surface calcium atoms and the close hydrogen-bonding to surface fluorine atoms. Thus, on thermodynamic grounds, it is energetically preferential for the methanoic acid molecules to adsorb to these surfaces, displacing the water molecules from the adsorption sites.

On all surfaces the methanoic acid molecules adsorb in such a way that the hydrogen atom bonded to the carbon atom is either directed away from the surface (fluorite {011} and {111} surfaces) or at least is accessible from above the surface (calcite {10$\overline{1}$4} and fluorite {310} surfaces). Of course, methanoic acid is studied as a model adsorbate for long-chain collector molecules such oleic acid, in which case the hydrogen atom would be the beginning of the hydrocarbon tail of the molecule. On the calcite plane and the fluorite {310} surface, substitution of the hydrogen atom by a hydrocarbon tail would result in fewer interactions with the surface fluorine atoms. Hence we could expect the adsorption energies for methanoic acid on those surfaces to be somewhat smaller, and thus the long-chain molecule would be even less likely to displace water molecules from the calcite {10$\overline{1}$4} and fluorite {310} surfaces. However, as the carbon atom's hydrogen atom is not involved in interactions to surface fluorine atoms on the fluorite {011} and {111} surfaces, the adsorption energies should not be significantly affected. Thus, the hydrocarbon tail of oleic acid should even enhance the effect of preferential adsorption to fluorite over calcite.

## Conclusion

We have used atomistic simulation techniques to model the adsorption of water and methanoic acid on the {10$\overline{1}$4} surface of calcite and the {011}, {111}, and {310} surfaces of fluorite. As a result we can make the following observations.

In general the lattice spacing of a crystal surface is important in that it determines the configuration and optimum coverage of adsorbates.

The {10$\overline{1}$4} cleavage plane of calcite is stabilized to a large extent by the adsorption of water. The water molecules adsorb in a regular herringbone pattern to full monolayer coverage with one water molecule per surface calcium atom. Adsorption of methanoic acid is only possible to 50% coverage. The adsorption energy of methanoic acid is less than that for water. Hence, on thermodynamic grounds the methanoic acid molecules are unlikely to displace water from this surface.

Hydration of all three fluorite surfaces is energetically possible, although the {011} surface is destabilized by hydration. The hydration energy of the {310} surface is particularly large. Adsorption of methanoic acid up to full monolayer coverage is possible on both {011} and {310} surfaces, but on the {111} surface due to the smaller calcium−calcium distance, only adsorption up to 50% is possible. On this surface, the methanoic acid molecules adsorb by their oxygen atoms to two calcium atoms, forming a bridge between them. This mode of adsorption is particularly favorable with a large adsorption energy. On both the {011} and the dominant {111} fluorite surfaces the energies of adsorption of methanoic acid compared to water show that adsorption of methanoic acid is energetically far more favorable, and hence methanoic acid molecules would displace water molecules.

Thus our calculations show that in a mixture of the two hydrated minerals methanoic acid would preferentially adsorb to fluorite rather than calcite. Not only are the adsorption energies for methanoic acid in absolute terms larger for the fluorite surfaces than for the calcite {10$\overline{1}$4} surface but also, the methanoic acid would not energetically be capable of easily displacing the water molecules from the calcite surface.

Due to the geometry of the adsorbed methanoic acid molecules, we would expect the effect of preferential adsorption to fluorite rather than calcite to be enhanced for long-chain molecules with the same carboxylic acid functional group but a hydrocarbon tail.

As the flotation process of separation of minerals depends on the selective adsorption of collector molecules to minerals in solution, our calculations show that selective hydrophobization of fluorite over calcite would occur if methanoic acid were the collector molecule. As electrostatic interactions between mineral surface and collector molecules are the main consideration of the selective adsorption, we would suggest that collectors with the same functional group as methanoic acid, such as oleic acid, provided there are no significant interactions between the hydrocarbon tails, should thus also float fluorite preferentially over calcite as is found experimentally.28-30,50

We have shown that atomistic simulation techniques are well placed to provide an insight at the atomic level into the interactions between substrate and adsorbate molecules. Our calculations, albeit on this model system, do provide an explanation for the experimental findings. Thus, further study using atomistic simulations is worthwhile, and we aim to develop it as a predictive tool in the search for ever more selective separation techniques to match and design collector molecules to particular minerals. We also intend to further investigate the competitive adsorption of water and methanoic acid on the calcite/

(50) Sorensen, E. J. Colloid Interface Sci. 1973, 45, 601.

fluorite system using molecular dynamics simulations in order to include temperature into the calculations. Fur- thermore, MD simulations will enable us to study a larger system containing both water and methanoic acid in a mixture which is closer to the experimental situation.

**Acknowledgment.** We thank EPSRC and NERC for financial support and Molecular Simulations Inc. for the use of Insight II and the Catalysis package.

LA980269K