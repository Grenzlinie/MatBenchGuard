Mat. Res. Soc. Symp. Proc. Vol. 651 © 2001 Materials Research Society

# Computational Study of Polymerization in Carbon Nanotubes

Steven J. Stuart, Brad M. Dickson, Bobby G. Sumpter¹, and Donald W. Noid¹
Department of Chemistry, Clemson University, Clemson, SC 29634-0973, USA.
¹Chemical and Analytical Science Division, Oak Ridge National Laboratory, Oak Ridge, TN 37830, USA.

## ABSTRACT

Molecular dynamics simulations of ethylene polymerization have been performed using a chemically realistic, reactive potential. These simulations have been performed in the bulk liquid and in the interior of both (10,10) and (7,7) nanotubes as a means of investigating the effects of nanoscale confinement on the polymerization reaction. The structure of the resulting polymer was found to be similar in the bulk and in the (10,10) tube at the elevated temperatures investigated, while only very small oligomers were formed in the (7,7) tube. The reaction rate was substantially reduced in the nanotubes, when compared to the bulk, primarily as a result of spatial interference due to reaction products. These simulations have implications for the possible use of nanotubes as synthetic reaction vessels, as well as for the general understanding of association reactions in confined spaces.

## INTRODUCTION

Carbon nanotubes are under investigation for a number of their remarkable properties. Among these is their ability to be filled via capillary forces in order to create nanoparticles, nanowires, and other novel structures.[1-5] Although most applications involve filling nanotubes with aqueous solutions, molten salts, or molten metals, previous work using mesoporous silica fibers as a synthetic support for polyethylene[6] suggests that polymerization in nanoscale geometries will also generate unique structures. In addition to the likelihood of forming novel polymeric structures, there is also the interesting possibility of observing fractal kinetics for association reactions in spaces of reduced dimensionality.[7] For these reasons, the polymerization of ethylene was studied in the confined geometry of nanotubes of two different diameters, and compared to comparable simulations in the bulk liquid phase.

## MODEL AND COMPUTATIONS

Because the reactivity of the hydrocarbons was of critical importance, it was crucial to perform the simulations a model that is capable of accurately modeling dissociation and formation reactions in hydrocarbons. For this reason, the AIREBO (adaptive intermolecular reactive empirical bond-order) potential[8] was selected. This is a bond-order potential based on Brenner’s well-known REBO potential for hydrocarbons[9,10]. The AIREBO potential preserves the treatment of C—C, C—H, and H—H covalent bonding interactions that has been validated in numerous studies with the REBO potential, while introducing terms corresponding to dispersion, torsional, and exchange repulsion interactions in a way that does not interfere with the covalent bonding potential.

The focus in this study is on the geometric effects of confinement within a carbon nanotube, rather than any potential reactions with the nanotube walls. For this reason, and in order to make

T1.8.1

the simulations more efficient, a cylindrically symmetric confining potential was used to represent the carbon nanotubes. This potential had the form

$$
V(r)=A\left(\frac{\sigma}{R-r}\right)^{2 p+q}-B\left(\frac{\sigma}{R-r}\right)^{p+q}+C\left(\frac{\sigma}{R-r}\right)^{q}+D \tag{1}
$$

where $r$ is the distance from the center of the nanotube. Equation (1) represents the simplest soft-wall cylindrical confining potential that results in an adsorption minimum near the tube wall, a local maximum at the center of the tube, and an infinite interaction as the particle approaches the tube wall ($r$=$R$). Taking $R$ as the tube radius from 0 K simulations with the AIREBO potential, and selecting $p$=4 arbitrarily, the remaining parameters were chosen to fit to the cylindrically averaged interaction of C and H atoms with a single-walled nanotube under the AIREBO potential.

Simulations of the polymerization of ethylene were performed in three separate geometries: a bulk system, a (10,10) carbon nanotube (6.6 Å radius), and a (7,7) carbon nanotube (4.7 Å radius). All systems were simulated at a density of approximately $0.75\ \text{g/cm}^3$. The bulk system consisted of 128 ethylene monomers in a cubic box of side 19.9 Å, with periodic boundary conditions. The (10,10) nanotube system contained 78 ethylene monomers in a nanotube of length 60 Å, and the (7,7) nanotube system contained 100 monomers in a nanotube of length 557 Å. One-dimensional periodic boundary conditions were applied to these systems. (Note that the volume of the soft-walled carbon nanotube is not uniquely defined. The ½ kT radius of approximately 3.9 Å for the (10,10) tube and 1.9 Å for the (7,7) tube at 3000 K was used to determine the tube volume.) All simulations were performed under the canonical ensemble. The temperature was controlled using a generalized Langevin thermostat.[11] At the constant density studied, the pressure of the liquid phase before polymerization was approximately 75-80 kbar (depending on the temperature examined).

## RESULTS

To simulate the polymerization process, the systems were heated to elevated temperatures of between 2800 K and 3400 K, causing thermal generation of radicals and subsequent polymerization. Note that at these temperatures the polymerization does not result in strictly saturated polyethylene, but also polyacetylene and other unsaturated species. Indeed, the equilibrium product at long times would be glassy or graphitic carbon, if the hydrogen byproducts were allowed to escape from the closed system.

For each of the three system geometries (bulk; (10,10) tube; (7,7) tube), polymerization was simulated at each of four temperatures, and the change in molecular structure was monitored. At each temperature the polymerization was allowed to proceed for at least 20 ns in the tube geometries and 5 ns in the bulk, for a total of over 180 ns of dynamics.

The progress of the polymerization was monitored via average molecular weights. Figure 1 illustrates the change in weight-averaged molecular weight, $M_w$, with time for the three different systems at 3200 K. The growth rate of the polymer is considerably greater in the bulk system than it is in either confined geometry, and is larger in the (10,10) nanotube than the (7,7) nanotube. Another difference that is apparent from Figure 1 is that the polymerization reaction reaches a plateau at 3200 K in both of the confined systems, but not in the bulk. The polymer growth saturates at an average molecular weight of about twice the monomer weight (28 g/mol) in the (7,7) tube and about four times the monomer weight in the (10,10) tube. The bulk system,

![](./images/811671545733709825_1.jpg)

Figure 1. Weight-averaged molecular weight, $M_w$, during polymerization for three different system geometries. The bulk system is represented by diamonds (red); the (10,10) nanotube by crosses (green), and the (7,7) nanotube by squares (blue). The unreacted initial system has $M_w$=28 g/mol.

on the other hand, shows no sign of saturation at an average molecular weight of over 15 times the monomer weight. Indeed, the configuration sampled at 5.5 ns includes a single $C_{94}$ oligomer chain that includes over a third of all of the carbons in the system (not quite at the percolation threshold indicative of an infinite molecular weight in this periodic system). The behavior is qualitatively quite similar at the other temperatures studied.

Figures 2 and 3 illustrate representative geometries of the growing polymer chain at late stages of their growth. While the polymers confined to the nanotubes are generally confined to the linear shape of the nanotube, the morphology is surprisingly similar in the confined and non-confined systems. In particular, the polymer is not in a highly linear (all-trans) configuration. In general, the polymer growth proceeds via thermal initiation and radical chain propagation, as would be expected for ethylene under these high-temperature, non-catalyzed conditions.
Because of the high reaction temperatures, the polymer that is formed has a high degree of branching and ring formation. Note that this is true in both the bulk and the (10,10) nanotube; the tube diameter is large enough to support short branches and cyclic groups (see Figure 3).
Analysis of pair correlation functions (not shown here) also indicates that the structure in the (10,10) and bulk systems is largely similar, differing mainly in the average chain length and the distribution of dihedral angles. The limited statistics available from these single runs do not permit an in-depth analysis of branching ratios or ring formation. Likewise, the statistics for individual runs do not permit any quantitative comparison of reaction order, preventing any conclusions regarding the existence of fractal kinetics or time-dependent rate constants in these systems. In the smaller, (7,7) tube, there is little branching and negligible ring formation due to both the limited degree of polymerization in that system and the extremely narrow ($\sim4$ Å) inner diameter of that tube.

The dependence of reaction rate on system temperature is presented in Figure 4. The rate constant was obtained by fitting the observed $M_w$ behavior for each system and temperature with that expected assuming second-order kinetics. As seen from Figure 4, the temperature

T1.8.3

![](./images/811671545733709825_2.jpg)

Figure 2. Conformation of bulk system after 5.5 ns of polymerization at 3400 K. Only carbon-carbon bonds are displayed, for clarity. The figure shows several independently growing oligomer chain, the largest of which contains a $C_{143}$ chain. Note the presence of short branches, as well as small ring structures.

dependence shows the expected Arrhenius behavior. The slopes for each curve are similar, with activation energies of 65±13 kcal/mol in the bulk, 52±8 kcal/mol in the (10,10) tube, and 54±5 kcal/mol in the (7,7) tube. Any contribution to the rate decrease due to energetic interactions with the confining tube wall is thus minor, if present at all, and the primary reason for the decrease of reaction rate in the confined geometries is entropic in nature.

The magnitude of the rate decrease is quite significant, with the polymerization in the (10,10) tube proceeding at an average rate 18 times slower than in the bulk, and the polymerization in the (7,7) tube proceeding fully 50 times slower than in bulk. It is to be expected that the rate will decrease somewhat upon confinement, due to nonproductive collisions

![](./images/811671545733709825_3.jpg)

Figure 3. Conformation of system in (10,10) nanotube after 28 ns of polymerization at 3400 K. Note the presence of short branches, as well as small ring structures. Small bubble-like phases of hydrogen gas and gaseous hydrocarbon fragments are visible to the far left and far right.

T1.8.4

![](./images/811671545733709825_4.jpg)

Figure 4. Arrhenius plot of polymerization rate (assumed $2^{nd}$ order) in various geometries. The bulk system is represented by diamonds (red); the (10,10) nanotube by crosses (green); and the (7,7) nanotube by squares (blue)

with the nonreactive wall, but the magnitude of this decrease is surprising. Surface area arguments alone cannot account for the 18-fold decrease in reaction rate in the (10,10) tube, for example, since only ~50% of the surface area of each monomer is occupied by nanotube wall.

An explanation for the large decrease in reaction rate, as well as the observed plateau in average molecular weight, is found upon examining the reaction trajectories in detail. Figure 3 illustrates the conformation of the polymer in a (10,10) nanotube after 28 ns at 3400 K. Notice that the H radicals that dissociated in the thermal initiation step, as well as in subsequent formation of unsaturated polymer units, have associated into $H_2$ molecules and separated into a separate phase of hydrogen gas. These nanoscale "bubbles" of hydrogen form high-pressure barriers between individual islands of growing oligomer chains, and act to prevent the diffusion and formation of large molecular-weight polymer chains. Thus the reaction is self-limiting, with the $H_2$ reaction product inhibiting the continued growth of the polymer. Hydrogen molecules also form and associate into bubbles, in the three-dimensional system. This does not substantially inhibit the growth of the polymer, however, as the bubbles are not large enough to span any dimension of the system. Note that the self-limiting nature of the reaction in the carbon nanotubes due to reaction byproducts is very similar to that observed in many experimental studies of filled carbon nanotubes. When the nanotube contents are subsequently reacted, the presence of a gaseous reaction byproduct tends to result in the formation of small nanoparticles, rather than nanowires.[4,5,12]

## CONCLUSIONS

Polymerization of ethylene has been observed via computer simulation at elevated temperatures of near 3000 K and pressures of near 75 kbar in both confined and bulk geometries, using a reactive potential. This is significant because it is one of very few all-atom simulations of bulk-scale polymerization with a chemically realistic potential. Future simulations of

T1.8.5

polymerization with this potential are expected to provide valuable insights into the polymerization process.

The focus in this study was on the difference in polymerization between confined and bulk geometries. The polymer morphology was fairly similar in the interior of a (10,10) to that in the bulk, but the (7,7) nanotube was small enough to substantially restrict branching and ring formation. The polymerization reaction was kinetically inhibited in both nanotube geometries, due to interference with H₂ reaction products that could not diffuse away from the reaction site. This is reminiscent of experimental observations on filled nanotubes.

Because the confining nanotube potential used here was rigid and nonreactive, these are purely geometric confinement effects that have nothing to do with the chemical nature of the carbon nanotube. Additional effects are possible, due to reactions with the tube, thermal motion of the tube walls, and atomic structure (including chirality) of the tube wall; these will be treated in future studies.

The simulations described here were performed at elevated temperatures of 2800 to 3200 K, because the polymerization was required to be well underway within the ~10 ns timescale of the simulations. While the observations made here, particularly those concerning relative reaction rates, are expected to be general, it will be useful to extend the timescales of these simulations to the microsecond regime in order to be able to make use of more moderate temperatures.

## ACKNOWLEDGEMENTS

Acknowledgement is made to the donors of the Petroleum Research Fund, administered by the ACS, and to the Research Corporation for partial support of this research. Thomas Zacharia of Oak Ridge National Laboratory is also acknowledged for a generous donation of computer time.

## REFERENCES

1. M. R. Pederson and J. Q. Broughton, *Phys. Rev. Lett.*, **69**, 2689 (1992).
2. P. M. Ajayan and S. Iijima, *Nature*, **361**, 333 (1993).
3. E. Dujardin, T. W. Ebbesen, H. Hiura, and K. Tanigaki, *Science*, **265**, 1850 (1994).
4. D. Ugarte, A. Châtelain, and W. A. de Heer, *Science*, **274**, 1897 (1996).
5. M. Terrones, N. Grobert, W. K. Hsu, Y. Q. Zhu, W. B. Hu, H. Terrones, J. P. Hare, H. W. Kroto, and D. R. M. Walton, *MRS Bull.*, **24** (8), 43 (1999).
6. K. Kageyama, J. I. Tamazawa, and T. Aida, *Science*, **285**, 2113 (1999).
7. R. Kopelman, *Science*, **241**, 1620 (1988).
8. S. J. Stuart, A. B. Tutein, and J. A. Harrison, *J. Chem. Phys.*, **112**, 6472 (2000).
9. D. W. Brenner, *Phys. Rev. B*, **42**, 9458 (1990); **46**, 1948, (1992).
10. D. W. Brenner, J. A. Harrison, C. T. White, and R. J. Colton, *Thin Solid Films*, **206**, 220 (1991).
11. S. A. Adelman and J. D. Doll, *J. Chem. Phys.*, **64**, 2375 (1976).
12. A. Chu, J. Cook, R. J. R. Heesom, J. L. Hutchison, M. L. H. Green, and J. Sloan, *Chem. Mater.*, **8**, 2751 (1996).

T1.8.6