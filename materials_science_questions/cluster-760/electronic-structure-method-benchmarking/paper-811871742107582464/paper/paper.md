# Modeling the Reaction of Fe Atoms with $CCl_4$

Donald M. Camaioni,* Bojana Ginovska, and Michel Dupuis

Chemical and Materials Sciences Division, Pacific Northwest National Laboratory,
Richland, Washington 99352

Received: August 26, 2008; Revised Manuscript Received: October 29, 2008

The reaction of iron atoms with carbon tetrachloride ($CCl_4$) in gas phase was studied using density functional theory. A recent experimental study (Parkinson, G. S.; Dohnálek, Z.; Smith, R. S.; Kay, B. D. *J. Phys. Chem. C* 2009, 113, 1818) of this reaction, performed by dropping Fe atoms into $CCl_4$ deposited on a cold FeO(111) surface, demonstrates rich chemistry with several products ($C_2Cl_4$, $C_2Cl_6$, $OCCl_2$, CO, $FeCl_2$, and $FeCl_3$) observed. The reactions of Fe with $CCl_4$ was studied under three stoichiometries, one Fe with one $CCl_4$, one Fe with two $CCl_4$ molecules, and two Fe with one $CCl_4$, modeling the stoichiometric, $CCl_4$-rich, and Fe-rich environments of the experimental work. The electronic structure calculations give insight into the reactions leading to the experimentally observed products, in particular with regard to the formation of $FeCl_3$ and other oxygen containing compounds that are not predicted from the simplest reactive model of successive Cl atom abstractions. They rather suggest that novel Fe−C−Cl containing species are important intermediates in these reactions. The intermediate complexes are formed in highly exothermic reactions, in agreement with the experimentally observed reactivity on the surface at low temperature (30 K). This initial survey of the reactivity of Fe with $CCl_4$ identifies some potential reaction pathways that are important in the effort to use Fe nanoparticles to differentiate harmful pathways that lead to the formation of contaminants like chloroform ($CHCl_3$) from harmless pathways that lead to products such as formate ($HCO_2^-$) or carbon oxides in water and soil.

## Introduction

Iron in various forms can interact with and reduce or immobilize a variety of contaminants. $^{1-4}$ The low cost, general availability, and environmental compatibility of iron along with the range of potential contaminant interactions, make the use of iron as a remediation tool very attractive. There is interest in the use of granular zero valent iron metal in various forms for the removal of contaminants from soil and water. $^{5}$ Among these, the use of nanosized particles of Fe (or bimetallic combinations of Fe and catalytic metals such as Pd) is currently getting the most attention. $^{6}$ The underlying expectation is that nanoparticles might alter the iron reactivity with chlorinated hydrocarbon molecules (e.g., carbon tetrachloride, chloro-ethenes, etc.). The enhanced rate of reactivity often attributed to nanoparticles could accelerate the breakdown of potential contaminants. This effect might stem simply from the presence of more reactive surface area or from fundamental changes in the reactive properties of iron as particle size decreases. However, of potentially greater importance is the ability to alter the nature of the reduction products by changing the reaction pathway. There is interest in understanding and differentiating harmful pathways that lead to the formation of chloroform $CHCl_3$ from harmless pathways that lead to formate ($HCO_2^-$), carbon oxides (CO, $CO_2$, and $CO_3^{2-}$), and $Cl^-$. Although reduction rates for chlorinated hydrocarbons appear to be significantly greater for microscale and nanoscale Fe than for magnetite or other Fe(II) containing mineral phases, the reactions do not yield completely dechlorinated products. This is true even for relatively simple compounds such as carbon tetrachloride, $CCl_4$, where $CHCl_3$ is often the major product and $CH_2Cl_2$ or $CH_3Cl$ are rarely even detected. The resistance of the less-chlorinated methanes to degradation by the zero valent metals is a serious limitation to the application of zero valent metals to catalyze the degradation. Understanding the factors that influence both rate and reaction path may facilitate approaches to optimize them.

In a companion paper (preceding paper in this issue), Parkinson et al. $^{7}$ report on the reaction of simple Fe clusters and individual atoms with $CCl_4$. Their experiment involves condensing layers of $CCl_4$ onto a monolayer of FeO(111) on a Pt(111) surface, followed by deposition of Fe atoms onto the $CCl_4$ film at 30 K. The experiments show that, while $CCl_4$ is inert to the oxygen terminated FeO(111) surface, $^{8}$ the addition of small amounts of iron atoms leads to formation of reactive intermediates capable of attacking FeO(111) and removing O to form phosgene ($OCCl_2$) and CO. In addition, small amounts of $C_2Cl_4$ and $C_2Cl_6$ are produced along with the iron chloride species $FeCl_2$ and $FeCl_3$.

A simple kinetic model of reactivity might involve successive Cl abstraction reactions

$$\mathrm{Fe} + \mathrm{CCl}_4 \rightarrow \mathrm{FeCl} + ^\cdot\mathrm{CCl}_3 \tag{1}$$

$$\mathrm{FeCl} + ^\cdot\mathrm{CCl}_3 \rightarrow \mathrm{FeCl}_2 + :\mathrm{CCl}_2 \tag{2}$$

$$\mathrm{FeCl} + \mathrm{CCl}_4 \rightarrow \mathrm{FeCl}_2 + ^\cdot\mathrm{CCl}_3 \tag{3}$$

and other reactions involving the comproportionation of iron chloride species and dimerization of the trichloromethyl radicals and dichlorocarbene radicals.

$$2\ ^\cdot\mathrm{CCl}_3 \rightarrow \mathrm{C}_2\mathrm{Cl}_6 \tag{4}$$

$$2\ :\mathrm{CCl}_2 \rightarrow \mathrm{C}_2\mathrm{Cl}_4 \tag{5}$$

* To whom correspondence should be addressed. Phone: (509) 375-2739.
Fax: (509) 375-6660. E-mail: Donald.Camaioni@pnl.gov.

10.1021/jp807604f CCC: $40.75
© 2009 American Chemical Society
Published on Web 01/07/2009

$$:\mathrm{CCl}_{2}+\mathrm{CCl}_{4} \rightarrow \mathrm{C}_{2} \mathrm{Cl}_{6} \tag{6}$$

These reactions are able to rationalize most but not all of the product species observed in the atom dropping experiments reported in the companion paper. For example, the formation of $\mathrm{FeCl}_{3}$, which occurs only with low doses of Fe atoms, is unexpected since $\mathrm{FeCl}_{2}$ does not react with $\mathrm{CCl}_{4}$ under the experimental conditions. Also, the amount of phosgene formed is independent of the thickness of the $\mathrm{CCl}_{4}$ layer. If phosgene were simply due to $: \mathrm{CCl}_{2}$ being formed in reaction 2 followed by adsorption onto the $\mathrm{FeO}(111)$ surface, then the yield of $\mathrm{COCl}_{2}$ should vary inversely with the thickness of $\mathrm{CCl}_{4}$ layer; reactions 5 and 6 being in competition with $\mathrm{O}$ abstraction from the $\mathrm{FeO}$ surface. Therefore, a more complete and probably complex reaction scheme is required. In the present paper we give a full account of Density Functional Theory (DFT) electronic structure calculations that were carried out to elucidate the thermochemistry and reaction pathways in the reactions of $\mathrm{Fe}$ with $\mathrm{CCl}_{4}$, including the characterization of reaction intermediates that might form from dosing the $\mathrm{CCl}_{4}$ layer with $\mathrm{Fe}$, and would lead to products detected following desorption.

In light of what the present computational study reveals, we note that complexes formed during oxidative addition reactions where $\mathrm{Fe}$ inserts into an $\mathrm{X}-\mathrm{Y}$ bond $(\mathrm{X}=\mathrm{C}, \mathrm{Y}=\mathrm{Cl}$ or $\mathrm{X}=$ $\mathrm{O}, \mathrm{Y}=\mathrm{H}$ ) have been previously reported. $^{9}$ Reactions of $\mathrm{Fe}$ complexes with $\mathrm{CCl}_{4}$ have been reported to produce dichlorocarbene complexes. Indeed, the crystal structure of a porphyrin complex has been reported. $^{10}$ Andrews and co-workers have reported the generation of metal alkyl, carbene, and carbyne complexes from reaction of metal atoms with methane and halomethanes. $^{11}$ The complexes, trapped in inert gas matrices, were identified using infrared spectroscopy and characterized using molecular orbital and density functional theory computational methods. $^{11}$ The work of Andrews et al. $^{11}$ and our calculations presented here show that such complexes may be formed in highly exothermic reactions of $\mathrm{Fe}$ and $\mathrm{CCl}_{4}$. They provide a theoretical framework that agrees with the observed products in the experimental work.

The paper is organized as follows: after the Introduction in section I, we describe the computational methods in section II, present and discuss the results in section III, and we conclude in section IV. The Results and Discussion section is broken down into subsections dealing with structures and energetics of complexes containing $\mathrm{C}, \mathrm{Fe}$, and $\mathrm{Cl}$ that theory predicts to be formed during the reaction. The subsections correspond to different reactivity situations. The first one deals with the species formed when one $\mathrm{Fe}$ atom reacts with one $\mathrm{CCl}_{4}$ molecule; we refer to this as the (1:1) case. The next one deals with one $\mathrm{Fe}$ atom reacting with two $\mathrm{CCl}_{4}$ molecules, as a model of the experimental conditions of excess $\mathrm{CCl}_{4}$ and allowing the species from the (1:1) case to further react with a second $\mathrm{CCl}_{4}$ molecule; we refer to this as the (1:2) case. The next section deals with what we refer to as the (2:1) case of two $\mathrm{Fe}$ atoms reacting with one $\mathrm{CCl}_{4}$ molecule as a model of the experimental conditions of excess $\mathrm{Fe}$ and allowing the species from the (1:1) to react with a second $\mathrm{Fe}$ atom. For each case we outline the findings that are consistent with the experimentally observed species and those that result from reaction pathways more complex than the simple chlorine atom abstractions. New chemical species that contain $\mathrm{Fe}-\mathrm{C}$ bonds, are predicted to form by the more complex reactions pathways. One more subsection is dedicated to discussing the chemical bonding characteristics of these species. In section IV we summarize the insights to the experiments by Parkinson et al. $^{7}$ gained from these calculations.

<table><caption>TABLE 1: Thermochemistry for Benchmark Reactions Calculated Using B3LYP Density Functional and Alhrichs TZV Basis Set with Polarization Functions</caption>
<thead>
  <tr>
    <th rowspan="2">reaction</th>
    <th colspan="2">$\Delta H^{\circ}_{298}$ (kcal/mol)</th>
  </tr>
  <tr>
    <th>calculated</th>
    <th>measured$^{a}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\mathrm{FeCl} \rightarrow \mathrm{Fe} + \mathrm{Cl}$</td>
    <td>77.9</td>
    <td>78.8</td>
  </tr>
  <tr>
    <td>$\mathrm{Fe} + \mathrm{CCl}_{4} \rightarrow \mathrm{FeCl} + \cdot \mathrm{CCl}_{3}$</td>
    <td>−19.8</td>
    <td>−7.9</td>
  </tr>
  <tr>
    <td>$\mathrm{Fe} + \mathrm{CCl}_{4} \rightarrow \mathrm{FeCl}_{2} + :\mathrm{CCl}_{2}$</td>
    <td>−54.6</td>
    <td>−52.5</td>
  </tr>
  <tr>
    <td>$\mathrm{CCl}_{4} \rightarrow \mathrm{Cl} + \cdot \mathrm{CCl}_{3}$</td>
    <td>58.2</td>
    <td>70.9</td>
  </tr>
  <tr>
    <td>$2\mathrm{FeCl} \rightarrow \mathrm{FeCl}_{2} + \mathrm{Fe}$</td>
    <td>−19.0</td>
    <td>−32.8</td>
  </tr>
  <tr>
    <td>$:\mathrm{CCl}_{2} + \mathrm{CCl}_{4} \rightarrow \mathrm{C}_{2}\mathrm{Cl}_{6}$</td>
    <td>−56.3</td>
    <td>−66.2</td>
  </tr>
  <tr>
    <td>$\mathrm{FeCl} + \mathrm{CCl}_{4} \rightarrow \mathrm{FeCl}_{2} + \cdot \mathrm{CCl}_{3}$</td>
    <td>−38.7</td>
    <td>−40.7</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="3">$^{a}$ Reference 27 for $\mathrm{FeCl}$ and $\mathrm{FeCl}_{2}$; ref 28 for all others.</td>
  </tr>
</tfoot>
</table>

## Computational Methods

In this section, we give details of the method used and follow this description with a benchmarking assessment of the accuracy of the level of theory for the type of system investigated here.

Minimum energy structures on the potential energy surface for the reaction products resulting from the reaction of one or two $\mathrm{Fe}$ atoms with one or two $\mathrm{CCl}_{4}$ molecules were optimized using the DFT$^{12,13}$ level of theory, the B3LYP functional, $^{14}$ and Ahlrichs basis set$^{15}$ with polarization (d functions on $\mathrm{C}$ and $\mathrm{Cl}$, and p functions on $\mathrm{Fe}$) using the NWChem $5.0^{16}$ code. All of the images of molecular structures were made with MacMolPlot. $^{17}$ All the calculations are for the "gas" phase, a reasonable model for the experimental conditions of a condensed phase of $\mathrm{CCl}_{4}$ molecules. Energy level diagrams are given below for many reactions involving one or two $\mathrm{Fe}$ atoms and one or two $\mathrm{CCl}_{4}$ molecules. We note that all of the species or complexes shown on the diagrams are (local) minima on the potential energy surface. Only one reaction transition state and associated barrier height was characterized, the one for the initial abstraction of a $\mathrm{Cl}$ atom by an $\mathrm{Fe}$ atom. The activation energy was found to be small (approximately a few kcal/mol) for an elementary step that is slightly exothermic. In general, for highly exothermic elementary reactions, as many are in these diagrams, we expect the reactions to exhibit small activation energies consistent with the Bell−Evans−Polanyi principle, $^{18}$ albeit the actual values of the energy barriers would require detailed computational characterizations of the transition states.

We benchmarked the level of theory used here against a limited number of experimental enthalpies of reactions $(\Delta H_{298})$ for a number of relevant reactions. In these benchmarks none of the reactions contained $\mathrm{FeCl}_{3}$ as a reactant or product due to the uncertainty in the experimental enthalpy of this species. The results are provided in Table 1. The calculations, with average unsigned error of 7.6 kcal/mol, are in approximate agreement with experiment. The ground electronic states of $\mathrm{Fe}, \mathrm{FeCl}, \mathrm{FeCl}_{2}$, and $\mathrm{CCl}_{2}$ are quintet, sextet, quintet, and singlet, respectively. Thus, entries 1, 3, and 7, which exhibit smaller than average errors, are isogyric reactions. Entries 2, 4, and 5 are not isogyric reactions. Entry 6, though an isogyric reaction, is not an isodesmic reaction. These reactions all exhibit higher than average errors. This analysis suggests that electron correlation effects are major factors. With this understanding, the agreement is sufficient for the purpose of this work.

Bauschlicher et al. $^{19}$ have pointed out the inadequacy of B3LYP in the description of $\mathrm{Fe}_{2}$, a failure that they assigned to a poor description of $\mathrm{Fe}$ by B3LYP. However, in their work dealing with the reaction of a $\mathrm{C}$ atom with $\mathrm{Fe}_{n}$ clusters, they found that B3LYP gives dissociation energies in better agreement with experiments than other functionals. $^{20}$ In contrast,

![](./images/811871742107582464_1.jpg)

Figure 1. Energy level diagram for Fe + CCl₄. The spin multiplicity of the species is reported without considering point group symmetry. The dotted lines show energy differences between states, they are not intended to suggest the absence of reaction barrier.

B3LYP accounts quantitatively for the bond energy of the FeCl molecule, a finding that we attribute to the strong ionic character of the Fe−Cl bond. Recent work by Sorkin et al.²¹ on iron dimers and FeO⁺, shows that this functional performs well in capturing the ground and low-lying excited states for these species. Nielsen and Allendorf²² have also found that B3LYP is appropriate for describing the geometries and frequencies of a number of transition-metal fluorides and chlorides. Mebel and Hwang used the B3LYP functional to study the reactions of Fe atom with H₂O, H₂S, O₂, and H⁺.²³ Andrews and co-workers have substantiated the use of B3LYP to describe systems involving metal−carbon bonds.¹¹ These published findings coupled with our comparisons with experimental enthalpies of formation for selected representative species suggest that the level of theory used here is qualitatively sufficient for our analysis.

## Results and Discussion

In what follows, we present the energy level diagrams for species formed in (1:1), (1:2), and (2:1) reactions between Fe atoms and CCl₄ molecules. Calculated structures are shown on the energy level diagrams in Figures 1−3. Coordinates and absolute energies including zero point and thermal correction energies are available in the Supporting Information. In the subsections that follow we discuss the energetics and possible pathways for forming complexes and products relative to the reactant asymptote Fe + CCl₄ to which we assigned the zero of energy. A number of Fe−C bonded complexes are identified as possible intermediates in the reactions of one or two Fe atoms with CCl₄ molecules. For example in the (1:1) case Fe + CCl₄, minimum energy structures were found of the type ClₙFeCCl₄₋ₙ corresponding to trichloromethyl (n = 1), dichlorocarbene (n = 2), and chlorocarbyne (n = 3) complexes. Trichloromethyl and dichlorocarbene structures containing five Cl atoms were also found in the (1:2) case: e.g., Cl₂FeCCl₃ and Cl₃FeCCl₂. In the (2:1) case, Fe + Fe + CCl₄ a novel allene-like structure Cl₂FeCFeCl₂ and a cyclic structure with a bridging dichlorocarbene were predicted to be formed. It is informative to understand the nature of the chemical bonding for the species containing Fe−C bonds. Such an analysis is presented at the end of this section. The bond lengths and bond orders obtained from Mayer's bond order analysis²⁴ are given in Table 2.

### (1:1) Case: Reaction of One Fe Atom and One CCl₄ Molecule.
Figure 1 shows an energy diagram for the (1:1) reactions of one Fe atom with one CCl₄ molecule. The energies reported are electronic energies with zero point energy correction. The zero of energy is taken as the energy of the infinitely separated Fe atom and CCl₄ molecule. The reaction of Fe (⁵D) and CCl₄ (¹A₁) leads to the formation of a Fe−CCl₄ long-range complex that is a local minimum energy structure on the potential energy surface (PES) that precedes a Cl atom abstraction by Fe to form a [FeCl•CCl₃] complex. That complex is energetically more stable than the infinitely separated reactant pair Fe + CCl₄ by 19 kcal/mol. In this complex, FeCl interacts weakly with the C atom of •CCl₃. This complex is slightly more stable (by ~2.1 kcal/mol) than the FeCl + •CCl₃ separated products. The experimental value of $\Delta H^{\circ}_{298}$ for the Cl abstraction reaction is −8 kcal/mol. The computational error is largely associated with the error in the calculated C−Cl bond energy in CCl₄. The [FeCl•CCl₃] complex is probably less stable than the calculations suggest, but still more stable than the separated reactants or the precursor complex.

Subsequent reactions involving FeCl and also of the complex [FeCl•CCl₃] are suggested from Figure 1. These reactions are

$$\mathrm{Fe}+\mathrm{CCl}_{4} \rightarrow\left[\mathrm{FeCl}^{\bullet} \mathrm{CCl}_{3}\right] \rightarrow \mathrm{ClFeCCl}_{3} \tag{7}$$

$$\left[\mathrm{FeCl}^{\bullet} \mathrm{CCl}_{3}\right] \rightarrow \mathrm{FeCl}_{2}+: \mathrm{CCl}_{2} \rightarrow \mathrm{Cl}_{2} \mathrm{FeCCl}_{2} \tag{8}$$

$$\mathrm{ClFeCCl}_{3} \rightarrow \mathrm{Cl}_{2} \mathrm{FeCCl}_{2} \tag{9}$$

In eq 7, a chlorine atom abstraction produces a weakly bound radical pair [FeCl•CCl₃] (multiplicity 5) that, following reorientation/reencounter, reacts to form ClFeCCl₃, which in the quintet electronic state is 81 kcal/mol more stable than Fe + CCl₄. A fragmentation reaction of [FeCl•CCl₃] shown in eq 8 leads to FeCl₂ + :CCl₂ with an exothermicity of 36 kcal/mol, or ~55 kcal/mol downhill with respect to Fe + CCl₄. Reencounter of the FeCl₂ and :CCl₂ species yields the carbene complex Cl₂FeCCl₂ directly with release of 40 kcal/mol. The quintet electronic state is 95 kcal/mol downhill from Fe + CCl₄ and this is the most stable structure that can be derived from the reaction of Fe with CCl₄. The carbene complex may also form as shown in eq 9 by Cl atom transfer from C to Fe in the ClFeCCl₃ complex, a reaction that is ~15 kcal/mol downhill. Another possibility is that the [FeCl•CCl₃] pair may generate this product directly if a Cl atom migrates from C to Fe in concert with formation of the Fe−C bond. This reaction is downhill by more than 76 kcal/mol. These reaction paths are all highly exothermic and therefore we expect them to occur with small activation energies.

Modeling the Reaction of Fe Atoms with CCl₄

The path to the chloro-carbyne complex Cl₃FeCCl is not so clear. It is 66 kcal/mol downhill from the separated reactants Fe + CCl₄ but 29 kcal/mol above the Cl₂FeCCl₂ complex. There is an [FeCl˙CCl₃] complex of multiplicity 3 that is approximately the same energy as the quintet state. There is also a twisted structure for the Cl₂FeCCl₂ complex with a Cl−Fe−C−Cl torsion angle of 90.1°, compared to 179.8° in the quintet, that is ~66 kcal/mol lower than the triplet [FeCl˙CCl₃] complex pair or ~21 kcal/mol lower than the triplet Cl₃FeCCl.

In summary, we note that the (1:1) reaction scheme of one Fe atom and one CCl₄ molecule can help rationalize the formation of ˙CCl₃, :CCl₂, FeCl, and FeCl₂. These findings are consistent with the direct experimental observation of these species or with the observation of species resulting from their further reaction. The most stable species predicted by the calculations involve new structures with Fe−C bonds, and those have not been directly identified in the experiment. Finally we note that the FeCl₃ + CCl channel is exothermic compared to Fe + CCl₄. The reaction path is likely to occur through formation of the slightly more stable FeCl₂ + :CCl₂ channel which then leads further to highly exothermic products. The FeCl₃ channel is thus in direct competition with much more exothermic channels. For this reason, it seems unlikely that the Cl₃FeCl complex is an important precursor to FeCl₃ that is formed in Parkinson et al.’s experiments by low doses of Fe atoms dropped into CCl₄ at 30 K. The experimental condition leading to FeCl₃ is better modeled by complexes produced from reactions of Fe atoms with more than one molecule of CCl₄.

(1:2) Case: Reaction of Fe Atom and Two CCl₄ Molecules.
Figure 2 shows the energy level diagram for species that result from reactions involving one Fe atom and two CCl₄ molecules. The energies reported are electronic energies corrected for zero point energy and the zero of energy is taken as the sum of the energies of the separated species, i.e., Fe + CCl₄ + CCl₄. Here as in Figure 1, the dotted lines simply indicate the energy change between the connected states. They do not imply a barrier-less pathway between the connected states. In the atom dropping experiments of Parkinson et al.,⁷ lower doses of Fe and thicker layers of CCl₄ should enable formation of Fe complexes with a ratio of Cl atoms to C greater than 4. Reactions postulated to produce these compounds are shown in eqs 10−15.

$$\mathrm{Fe}+2\ \mathrm{CCl}_{4}\to\mathrm{FeCl}_{2}+2\ {}^{\bullet}\mathrm{CCl}_{3}\to\mathrm{FeCl}_{2}+\mathrm{C}_{2}\mathrm{Cl}_{6}\quad(10)$$

$$\mathrm{FeCl}_{2}+{}^{\bullet}\mathrm{CCl}_{3}\to\mathrm{Cl}_{2}\mathrm{FeCCl}_{3}\quad(11)$$

$$\mathrm{FeCl}_{2}+{}^{\bullet}\mathrm{CCl}_{3}\to\left[\mathrm{FeCl}_{3}:\mathrm{CCl}_{2}\right]\to\mathrm{Cl}_{3}\mathrm{FeCCl}_{2}\quad(12)$$

$$\mathrm{Cl}_{2}\mathrm{FeCCl}_{3}+{}^{\bullet}\mathrm{CCl}_{3}\to\mathrm{FeCl}_{2}+\mathrm{C}_{2}\mathrm{Cl}_{6}\quad(13)$$

$$\mathrm{Cl}_{3}\mathrm{FeCCl}_{2}+{}^{\bullet}\mathrm{CCl}_{3}\to\mathrm{FeCl}_{3}+{}^{\bullet}\mathrm{C}_{2}\mathrm{Cl}_{5}\quad(14)$$

$$\mathrm{Cl}_{2}\mathrm{FeCCl}_{2}+\mathrm{CCl}_{4}\to\mathrm{FeCl}_{2}+\mathrm{C}_{2}\mathrm{Cl}_{6}\quad(15)$$

Comparison of the energy diagrams of Figures 1 and 2 shows that the intermediates Cl₂FeCCl₂ and ClFeCCl₃ formed in the reaction of one Fe atom and one CCl₄ molecule are more exothermic than the complexes containing five Cl atoms. This observation suggests that it is unfavorable for Cl₃FeCCl₂ and Cl₂FeCCl₃ to be formed by abstraction of a chlorine atom from a second CCl₄ molecule (eqs 16 and 17).

$$\mathrm{ClFeCCl}_{3}+\mathrm{CCl}_{4}\to\mathrm{Cl}_{2}\mathrm{FeCCl}_{3}+{}^{\bullet}\mathrm{CCl}_{3}\quad(16)$$

$$\mathrm{Cl}_{2}\mathrm{FeCCl}_{2}+\mathrm{CCl}_{4}\to\mathrm{Cl}_{3}\mathrm{FeCCl}+{}^{\bullet}\mathrm{CCl}_{3}\quad(17)$$

More energetically favorable pathways, as suggested by eqs 10−12, involve reactions of a FeCl molecule with a second CCl₄ molecule to form an FeCl₂ and a ˙CCl₃ radical pair. In reaction 10, the Fe atom abstracts a Cl atom from each of the two CCl₄ molecules to form FeCl₂ and two ˙CCl₃ radicals. This reaction is ~59 kcal/mol downhill from the infinitely separated reactant species Fe + CCl₄ + CCl₄. The combination of FeCl₂ and ˙CCl₃, reaction 11, releases another 18.5 kcal/mol, to form the Cl₂FeCCl₃ complex. It is also favorable for the FeCl₂ and ˙CCl₃ pair to disproportionate into an FeCl₃ and :CCl₂ pair that then combines to form Cl₃FeCCl₂ (eq 12). This sequence might occur with transfer of Cl from ˙CCl₃ to FeCl₂ concerted with Fe−C bond formation, i.e., insertion of Cl₂Fe into the Cl−CCl₂ bond. Once these complexes are formed they can react with ˙CCl₃ radicals (eqs 13−14), giving perchlorinated-C₂ products.

In summary, the calculations suggest the formation of highly stable complexes including Fe−C bonds as well as producing species such as FeCl₂ and FeCl₃ along with perchloroethane or perchloroethyl radical. This (1:2) set of reactions can now explain the formation of FeCl₃, contrary to the (1:1) set of reactions, albeit complexes that include Fe−C bonds are predicted to be very stable.

(2:1) Case: Reactions of Two Fe Atoms and One CCl₄ Molecule. The experiments of Parkinson et al.⁷ that used higher Fe doses and thinner layers of CCl₄ may favor reactions with Fe:CCl₄ stoichiometries greater than 1:1. We calculated a variety of structures containing two Fe atoms, one to four Cl atoms, and zero or one C atom as a simple model of what products may form when CCl₄ reacts with excess Fe or with iron clusters. Figure 3 shows the energy level diagram for these structures. The energies reported are electronic energies corrected for zero point energy and the zero of energy taken as the sum of the energies of the separated reactants, i.e., Fe + Fe + CCl₄. The complexes may form either by reaction of an Fe atom with CCl₄ followed by reaction with another Fe atom, or by formation of an iron dimer (Fe₂) which then reacts with a CCl₄ molecule. The measured energy for association of two Fe atoms is −27.2 kcal/mol,²⁵ so that the formation of all the complexes in Figure 3 are favorable with respect to Fe₂ + CCl₄.

The most stable structures are the two Cl₂Fe−C−FeCl₂ isomers with Fe−C−Fe bond angle of 180° and spin multiplicity 5. They are 150 kcal/mol more stable than the separated species Fe + Fe + CCl₄. Their structures differ mainly in the conformations of the trigonal planar FeCl₂ groups. In one, the groups lie nearly in the same plane. In the other, the groups are twisted so that their planes are perpendicular. The twisted or allene-like conformer is only 0.1 kcal/mol higher in energy than the planar conformer. Given the large stability of these structures, they could be formed by a variety of pathways including reaction of one Fe atom with the (1:1) complexes ClFeCCl₃ and Cl₂FeCCl₂ discussed above and shown in Figure 1. Another isomer, the cyclopropene-like ClFeCCl₂FeCl complex with an Fe−Fe bond and a bridging carbene, is a local minimum on the singlet surface. Although this structure is much higher in energy (~94 kcal/mol) than the quintet structures, it is still 55 kcal/mol more stable than the separated reactants such that, allowing for intersystem crossing, it could in principle be formed by reaction of :CCl₂ with (FeCl)₂ dimer.

The zero point corrected energies of the reactions reported above, for all three stoichiometries, are displayed in the energy level diagrams. The general trend observed is that all of the reactions are either very exothermic, or slightly endothermic, demonstrating that there are a variety of pathways leading to the observed products. The high exothermicity of these reactions suggests low barriers to reaction, consistent with the observed reactivity at low temperatures.

![](./images/811871742107582464_2.jpg)

Figure 2. Energy level diagram for Fe + 2CCl₄. The spin multiplicity of the species is reported without considering point group symmetry. The dotted lines show energy differences between states, they are not intended to suggest the absence of reaction barrier.

![](./images/811871742107582464_3.jpg)

Figure 3. Energy level diagram for 2 Fe + CCl₄. The spin multiplicity of the species is reported without considering point group symmetry. The dotted lines show energy differences between states, they are not intended to suggest the absence of reaction barrier.

<table>
<caption>TABLE 2: Bond Lengths and Mayer's Bond Order Analysis for Fe−C−Cl Containing Compounds Calculated Using DFT (B3LYP) with Ahlrichs TZV Basis Set with Polarization Functions</caption>
<thead>
<tr>
<th rowspan="2">structure, multiplicity</th>
<th colspan="4">bond length in Å (bond order)</th>
</tr>
<tr>
<th>Fe−Cl</th>
<th>Fe−C</th>
<th>C−Cl</th>
<th>Fe−Fe</th>
</tr>
</thead>
<tbody>
<tr>
<td>FeCl, sextet</td>
<td>2.216 (1.01)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>FeCl₂, quintet</td>
<td>2.140 (1.14)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>FeCl₃, sextet</td>
<td>2.157 (1.21)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ClFeCCl₃, quintet</td>
<td>2.166 (1.06)</td>
<td>2.021 (0.77)</td>
<td>1.814 (1.05)<sup>a</sup></td>
<td></td>
</tr>
<tr>
<td>Cl₂FeCCl₂, quintet</td>
<td>2.181 (1.09)</td>
<td>1.983 (0.97)</td>
<td>1.720 (1.22)</td>
<td></td>
</tr>
<tr>
<td>Cl₃FeCCl, triplet</td>
<td>2.183 (1.08)</td>
<td>1.638 (1.82)</td>
<td>1.612 (1.33)</td>
<td></td>
</tr>
<tr>
<td>Cl₂FeCCl₃, quartet</td>
<td>2.157 (1.08)</td>
<td>2.065 (0.64)</td>
<td>1.758 (1.16)</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>1.801 (1.00)<sup>b</sup></td>
<td></td>
</tr>
<tr>
<td>Cl₃FeCCl₂, quartet</td>
<td>2.173 (1.17)<sup>c</sup></td>
<td>1.848 (1.13)</td>
<td>1.692 (1.24)<sup>a</sup></td>
<td></td>
</tr>
<tr>
<td></td>
<td>2.185 (1.05)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Cl₂FeCFeCl₂, quintet</td>
<td>2.122 (1.17)</td>
<td>1.749 (1.28)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>ClFeCCl₂FeCl, singlet</td>
<td>2.105 (1.12)</td>
<td>1.900 (0.92)</td>
<td>1.766 (1.10)</td>
<td>2.008 (1.94)</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5"><sup>a</sup> Average value. <sup>b</sup> Bridging Cl. <sup>c</sup> In plane of :CCl₂ fragment.</td>
</tr>
</tfoot>
</table>

Bonding in Complexes from Reactions of Fe atoms with CCl₄. A number of new structures are predicted in this study. They include structures of the type ClₙFeCCl₄₋ₙ corresponding to trichloromethyl ($n=1$), dichlorocarbene ($n=2$), and chlorocarbene ($n=3$) complexes, trichloromethyl and dichlorocarbene structures containing five Cl atoms i.e., Cl₂FeCCl₃ and Cl₃FeCCl₂, and in the case of two Fe plus CCl₄, a novel allene-like structure Cl₂FeCFeCl₂ and a cyclic structure with a bridging dichloro-carbene. To provide understanding of the chemical bonding in these species, we present a bond order analysis following the theory of Mayer²⁴ and report key vibrational frequencies.

The Fe−Cl bonds in these complexes are little sensitive to the presence of Fe−C bonds. The Fe−Cl bonds range between 2.1 and 2.2 Å, similar to the bonds in FeCl, FeCl₂ and FeCl₃. While Fe−Cl bond lengths and bond orders increase with the number of Fe−Cl bonds in FeClₙ compounds, the trend is absent in ClₓFeCClᵧ complexes. The Mayer bond order analysis shows the Fe−Cl bonds are essentially single bonds with contributions from both $\sigma$- and $\pi$-type interactions.²⁶

The Fe−C bonds and C−Cl bonds are more sensitive to the structure of the complexes. In ClFeCCl₃, the Fe−C and C−Cl bond lengths (bond orders) are 2.02 Å (0.8) and 1.82 Å (1.0), respectively. The stretching frequency of the Fe−C bond is 806 cm⁻¹. The bond order of less than unity for the Fe−C bond of Fe−CCl₃ compared to the Fe−Cl bond is a result of the hyperconjugative interaction between Fe d$\pi$ and C−Cl $\sigma$ bond being weaker than Fe−Cl d$\pi$-p$\pi$ interactions. In Cl₂FeCCl₂, the

Modeling the Reaction of Fe Atoms with CCl₄

J. Phys. Chem. C, Vol. 113, No. 5, 2009 1835

Fe−C and C−Cl bond lengths (bond orders) are 1.98 Å (1.0) and 1.72 Å (1.2), respectively. The shorter bond lengths and larger bond orders are consistent with Fe−C $d\pi-p\pi$ and C−Cl $p\pi-p\pi$ bonding in the carbene complex. A full double bond is not realized due to mismatches in orbital energies and size of Fe d and carbon p orbitals. In the $Cl_2FeCCl_2$ structure, similar to $ClFeCCl_3$, the Fe−C stretch corresponds to the highest frequency mode (849 cm⁻¹). In $Cl_3FeCCl$, the Fe−C and C−Cl bond lengths (bond orders) are 1.64 Å (1.8) and 1.61 Å (1.3), respectively. Whereas the trichloromethyl and carbene complexes are quintet ground states, the carbyne complex has a triplet ground state, with the paired electrons populating a Fe−C $d\pi-p\pi$ bond, such that the bond length is shorter and the bond order higher than in the carbene. In this compound, the Fe−C stretch has a frequency of 1247 cm⁻¹ and it is the highest frequency mode in all of the species. These Fe−C complexes have frequencies that are much higher than those in the iron-chloride compounds and they can be clearly distinguished. For example, both $FeCl_2$ and $FeCl_3$ have highest frequencies that are less than 500 cm⁻¹. Unfortunately, some of the Fe−C bands nearly overlap with the C−C band in $C_2Cl_6$ (940 cm⁻¹) such that experimental identification may be difficult. For complexes containing five Cl atoms, i.e., $Cl_2FeCCl_3$ and $Cl_3FeCCl_2$, the Fe−C bonding is like the analogous $-CCl_3$ and $-CCl_2$ complexes described above that have one less Cl atom bonded to Fe. In $Cl_2FeCCl_3$, the $^\bullet CCl_3$ group is strongly distorted with one Cl atom bonded to C closer to Fe (2.799 Å, Fe−C−Cl $\angle = 92.5$), than the other two (3.188 Å, Fe−C−Cl $\angle = 112.7$). The latter C−Cl bonds have bond lengths and bond orders that are in-between the C−Cl bonds in the analogous $ClFeCCl_3$ and $Cl_2FeCCl_2$ complexes. In $Cl_3FeCCl_2$, one of the Cl atoms is in an eclipsed conformation with the $CCl_2$ group. For the $Cl_3FeCCl_2$ and $Cl_2FeCCl_3$ species, the Fe−C stretches are coupled with other modes, making it difficult to assign them uniquely to a single normal mode. The highest frequency modes are 770 cm⁻¹ for $Cl_2FeCCl_3$ and 908 cm⁻¹ for $Cl_3FeCCl_2$, closely resembling some of the modes in $C_2Cl_4$ and $C_2Cl_6$. The same is the case for the complexes derived from combining two Fe atoms with $CCl_4$, for which their largest modes are 677 cm⁻¹ for $Cl_2FeCFeCl_2$ and 878 cm⁻¹ for the $ClFeCCl_2FeCl$ complex. The Fe−C bonds in the complex $Cl_2FeCFeCl_2$ have lengths (1.75 Å) and bond orders (1.3) that are intermediate between the values for the carbene and carbyne complexes described above and consistent with the allene-like structure and quintet electronic state. In the $ClFeCCl_2FeCl$ complex, there is an Fe−Fe double bond and two Fe−C bonds with single bond character, consistent with its singlet electronic and cyclopropene-like structure.

### Conclusion

This study and the study by Parkinson et al.⁷ are first steps to understanding the role of Fe atoms in reduction of $CCl_4$ in the environment. The experiments involved only the interaction of Fe atoms and clusters with $CCl_4$ on the FeO(111) substrate. Parkinson et al. identified $COCl_2$, $CO$, $FeCl_2$, and $FeCl_3$ as products along with small amounts of $C_2Cl_4$ and $C_2Cl_6$.⁷

Our calculations, which model the products of isolated iron atoms reacting with $CCl_4$, have been helpful in interpreting the atom dropping experiments. Although many of the products observed may be explained by simple Cl abstraction and recombination of C−Cl containing radicals, the formation of $FeCl_3$ cannot be rationalized by such simple mechanisms. In the exploration of possible reaction pathways that would give this product, we found that pathways involving formation of Fe−C bonded intermediates following Cl atom transfers are favorable. In particular, the formation of carbene complexes is most favorable. Transfer/abstraction of a Cl atom yields FeCl and $^\bullet CCl_3$ species that may re-encounter and react via an exothermic step to form a complex such as $ClFeCCl_3$. Cl atom migration from C to Fe is a favorable step leading to $Cl_2FeCCl_2$ as a product. It is also possible for a second Cl atom to be abstracted by FeCl, and form $FeCl_2$ and $:CCl_2$. The formation of $C_2Cl_6$ and $C_2Cl_4$ is thermodynamically favorable although mechanisms for C−C bond formation are not elucidated. The simplest mechanism would involve thermal dissociation of $^\bullet CCl_3$ and:$CCl_2$ during TPD followed by dimerization. Alternatively, the Fe−C complexes may aggregate into clusters from which reductive elimination of $C_2Cl_6$ and $C_2Cl_4$ may occur without generation of $:CCl_2$ and $^\bullet CCl_3$. The reaction of two $CCl_4$ molecules with Fe also allows for formation of $Cl_3FeCCl_2$ and $Cl_3FeCCl_3$ complexes. Decomposition of both of these complexes to $FeCl_3$ and $:CCl_2$ and $FeCl_2$ and $^\bullet CCl_3$, followed by recombination with excess $^\bullet CCl_3$ and $:CCl_2$ radicals, leads to additional reaction pathways with production of $FeCl_2$, $FeCl_3$, $C_2Cl_4$, and $C_2Cl_6$.

Experimental observations under conditions of high Fe doses to thin layers of $CCl_4$ suggest that nearly two $FeCl_2$ molecules are formed per reacted $CCl_4$, indicating that all Cl atoms are stripped from the carbon and transferred to Fe atoms. As a model of these experiments, the calculations allowing for complexes with two Fe atoms showed that both reactions of a second Fe with the Fe−C−Cl complexes and reaction of $Fe_2$ with $CCl_4$ are favored to form $C(FeCl_2)_2$ complexes. The changes that are observed in the Fe and Cl XPS spectra, before and after 400 K annealing, are also consistent with Fe−C−Cl complexes as intermediates in the experiments. These complexes are very stable ($\sim -70$ to $-150$ kcal/mol relative to the separated $CCl_4$ and Fe species), in accord with the experimental observation of reactivity at low temperature. As such, they may interact with FeO surface and during TPD undergo reactions with the surface bound oxygen to generate $COCl_2$ and $CO$. In any case, while the results of the present computational study provide a plausible basis for interpreting the experimental observations, direct spectroscopic characterization of the Fe−C−Cl intermediate species would serve to validate further the theoretical predictions.

**Acknowledgment.** The authors acknowledge valuable discussions with our collaborators, Gareth S. Parkinson, Zdenek Dohnálek, R. Scott Smith, Bruce D. Kay and Don Baer and their enthusiasm for pursuing fundamental experiments that facilitate theoretical analysis. This work was sponsored by the U.S. Department of Energy Office of Basic Energy Sciences, Chemical Sciences Division and Biological and Environmental Research, Environmental Research Sciences Program.. Pacific Northwest National Laboratory is operated for the U.S. Department of Energy by Battelle under Contract No. DE-AC06-76RLO 1830.

**Supporting Information Available:** Table 1S. Energies, zero point corrected energies, and enthalpies (in hartree) for all the species in this work. Cartesian coordinates for all of the optimized structures used in this work (in Å). This material is available free of charge via the Internet at http://pubs.acs.org.

### References and Notes
(1) Tratnyek, P. G.; Johnson, R. L. *Nano Today* **2006**, *1*, 44.
(2) Elliott, D. W.; Zhang, W. X. *Environ. Sci. Technol.* **2001**, *35*, 4922.
(3) Johnson, T. L.; Scherer, M. M.; Tratnyek, P. G. *Environ. Sci. Technol.* **1996**, *30*, 2634.

(4) Preis, S.; Kallas, J. *Environ. Chem. Lett.* **2004**, 2, 9.

(5) Tratnyek, P. G.; Scherer, M. M.; Johnson, T. J.; Matheson, L. J. Permeable reactive barriers of iron and other zero-valent metals. In *Chemical Degradation Methods for Wastes and Pollutants: Environmental and Industrial Applications*; Tarr, M. A., Ed.; Marcel Dekker: New York, 2003; pp 371−421.

(6) Glazier, R.; Venkatakrishnan, R.; Gheorghiu, F.; Walata, L.; Nash, R.; Zhang, W. X. *Civ. Eng.* **2003**, 73, 64.

(7) Parkinson, G. S.; Dohnálek, Z.; Smith, R. S.; Kay, B. D. *J. Phys. Chem. C* **2009**, 113, 1818.

(8) Liu, S. R.; Dohnalek, Z.; Smith, R. S.; Kay, B. D. *J. Phys. Chem. B* **2004**, 108, 3644.

(9) Cedeno, D. L.; Weitz, E. *J. Phys. Chem. A* **2000**, 104, 8011.

(10) Mansuy, D.; Lange, M.; Chottard, J. C.; Bartoli, J. F.; Chevrier, B.; Weiss, R. *Angew. Chem., Int. Ed. Engl.* **1978**, 17, 781.

(11) Lyon, J. T.; Andrews, L. *Organometallics* **2007**, 26, 2519. Lyon, J. T.; Andrews, L.; Cho, H. G. *Organometallics* **2006**, 25, 4040. Andrews, L. *Inorg. Chem.* **2006**, 45, 9858. Cho, H. G.; Lyon, J.; Andrews, L. *Organometallics* **2008**, 27, 5241.

(12) Hohenberg, P.; Kohn, W. *Phys. Rev.* **1964**, 136, B864.

(13) Kohn, W.; Sham, L. J. *Phys. Rev.* **1965**, 140, A1133.

(14) Becke, A. D. *J. Chem. Phys.* **1993**, 98, 5648.

(15) Schafer, A.; Huber, C.; Ahlrichs, R. *J. Chem. Phys.* **1994**, 100, 5829.

(16) Straatsma, T. P.; Aprà, E.; Windus, T. L.; Bylaska, E. J.; de Jong, W.; Hirata, S.; Valiev, M.; Hackler, M.; Pollack, L.; Harrison, R.; Dupuis, M.; Smith, D. M. A.; Nieplocha, J.; Tipparaju, V.; Krishnan, M.; Auer, A. A.; Brown, E.; Cisneros, G.; Fann, G.; Früchtl, H.; Garza, J.; Hirao, K.; Kendall, R.; Nichols, J.; Tsemekhman, K.; Wolinski, K.; Anchell, J.; Bernholdt, D.; Borowski, P.; Clark, T.; Clerc, D.; Dachsel, H.; Deegan, M.; Dyall, K.; Elwood, D.; Glendening, E.; Gutowski, M.; Hess, A.; Jaffe, J.; Johnson, B.; Ju, J.; Kobayashi, R.; Kutteh, R.; Lin, Z.; Littlefield, R.; Long, X.; Meng, B.; Nakajima, T.; Niu, S.; Rosing, M.; Sandrone, G.; Stave, M.; Taylor, H.; Thomas, G.; van Lenthe, J.; Wong, A.; Zhang, Z.; *NWChem, A Computational Chemistry Package for Parallel Computers, Version 5.0*; Pacific Northwest National Laboratory: Richland, WA, 2006. Kendall, R. A.; Aprà, E.; Bernholdt, D. E.; Bylaska, E. J.; Dupuis, M.; Fann, G. I.; Harrison, R. J.; Ju, J.; Nichols, J. A.; Nieplocha, J.; Straatsma, T. P.; Windus, T. L.; Wong, A. T. High Performance Computational Chemistry: an Overview of NWChem a Distributed Parallel Application. *Comput. Phys. Commun.* **2000**, 128, 260.

(17) Bode, B. M.; Gordon, M. S. *J. Mol. Graphics Mod.* **1998**, 16, 133.

(18) (a) Bell, R. P. *Proc. R. Soc. London Ser. A* **1936**, 154, 414. (b) Bell, R. P.; Lidwell, O. M. *Proc. R. Soc. London Ser. A* **1940**, 176, 114. (c) Ogg, R. A., Jr.; Polanyi, M. *Trans. Faraday Soc.* **1935**, 31, 604. (d) Evans, M. G.; Polanyi, M. *Trans. Faraday Soc.* **1935**, 31, 875. (e) Evans, M. G.; Polanyi, M. *Trans. Faraday Soc.* **1936**, 32, 1333. (f) Evans, M. G.; Polanyi, M. *Trans. Faraday Soc.* **1937**, 33, 448. (g) Evans, M. G.; Polanyi, M. *Trans. Faraday Soc.* **1938**, 34, 11. (h) Evans, M. G.; Warhurst, E. *Trans. Faraday Soc.* **1938**, 34, 614. (i) Evans, M. G. *Trans. Faraday Soc.* **1939**, 35, 824. (j) Baughan, E. C.; Evans, M. G.; Polanyi, M. *Trans. Faraday Soc.* **1941**, 37, 377. (k) Baughan, E. C.; Polanyi, M. *Trans. Faraday Soc.* **1941**, 37, 648. (l) Evans, M. G. *Trans. Faraday Soc.* **1946**, 42, 719. (m) Warhurst, E. *Trans Faraday Soc.* **1949**, 45, 461. (n) Warhurst, E. *Proc. R. Soc. London Ser. A* **1951**, 207, 32.

(19) Gutsev, G. L.; Bauschlicher, C. W., Jr. *J. Phys. Chem. A* **2003**, 107, 7013.

(20) Gutsev, G. L.; Bauschlicher, C. W. *Chem. Phys.* **2003**, 291, 27.

(21) Sorkin, A.; Iron, M. A.; Truhlar, D. G. *J. Chem. Theory Comput.* **2008**, 4, 307.

(22) Nielsen, I. M. B.; Allendorf, M. D. *J. Phys. Chem. A* **2005**, 109, 928.

(23) Mebel, A. M.; Hwang, D. Y. *J. Phys. Chem. A* **2001**, 105, 7460.

(24) Mayer, I. *Chem. Phys. Lett.* **1983**, 97, 270.

(25) Armentrout, P. B. *Annu. Rev. Phys. Chem.* **2001**, 52, 423.

(26) For example, see. Bridgeman, A. J.; Cavigliasso, G.; Ireland, L. R.; Rothery, J. *J. Chem. Soc., Dalton Trans.* **2001**, 2095.

(27) Hildenbrand, D. L. *J. Chem. Phys.* **1995**, 103, 2634.

(28) Linstrom, P. J., Mallard, W. G., Eds., *NIST Chemistry WebBook, NIST Standard Reference Database Number 69*; National Institute of Standards and Technology: Gaithersburg, MD, 2005; http://webbook.nist.gov.

JP807604F