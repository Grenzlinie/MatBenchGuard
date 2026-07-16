
# Prediction of Novel Li–Ag(II)–F Compounds using Evolutionary Algorithms

Katarzyna Kuder \( ^{a,*} \) , Wojciech Grochala \( ^{a,**} \) 

 \( ^{a} \)  Centre of New Technologies, University of Warsaw, S. Banacha 2c, 02-097 Warsaw, Poland

* k.kuder@cent.uw.edu.pl
** w.grochala@cent.uw.edu.pl

This article is dedicated to Piotr J. Leszczyński at his 60 \( ^{th} \)  birthday.

## Abstract

This work provides a theoretical exploration of the thermodynamic stability and magnetic behaviour of previously unknown ternary Li–Ag(II)–F compounds. Convex-hull analysis shows that all predicted structures lie slightly above the LiF + AgF \( _{2} \)  decomposition line, indicating a natural tendency toward phase separation; nevertheless, their negative formation energies relative to AgF, LiF, and  \( F_{2}/F \)  suggest that alternative synthetic pathways may be feasible for these compounds. All studied structures show preference for antiferromagnetic ground state. Notably, the triclinic LiAgF \( _{3} \)  \( _{2} \)  is predicted to exhibit an exceptionally large superexchange constant (J = -358 meV) within  \( [Ag_{2}F_{7}] \)  dimers, placing it above the strongest known magnetic exchange interactions reported to date.

## 1 Introduction

The properties of silver(II) fluoride has been thoroughly documented since the 1960s through the 1970s  \( [1, 2] \) . This compound is distinguished by the presence of covalent Ag-F bonds  \( [3] \)  within layered structural motifs and pronounced antiferromagnetic interactions  \( [4–7] \) . Owing to its high reactivity, primarily due to facile reduction to silver(I), silver(II) fluoride has been considered more of a curiosity than a subject warranting thorough investigation. This perception began to change in the 2000s when the interest in examining Ag(II)-containing systems was rekindled. In this period, such systems were noticed to be analogues to cuprates and were thoroughly investigated  \( [8, 9] \) . One of the most striking outcomes of these studies was the realization that Ag(II) fluorides may exhibit record-breaking magnetic superexchange constants, which are comparable (and even greater) than those in copper(II) oxides  \( [10–12] \) .

A variety of silver(II)-fluoride compounds are known, many of which are binary and exhibit mixed-valence character, such as  \( Ag_{2}F_{2} \) ,  \( Ag_{2}F_{4} \) ,  \( Ag_{2}F_{5} \) , and  \( Ag_{3}F_{8} \)  [9, 13–17]. In addition, numerous ternary or more complex compounds containing silver, fluorine, and other elements have been reported, further expanding the structural and chemical diversity of Ag(II)-fluoride systems [9, 18–20]. Despite the extensive exploration of silver(II) fluorides, there is a notable absence of studies focusing on lithium–silver(II)-fluoride systems, even though related systems containing homologous sodium, potassium, caesium, and rubidium have been investigated both experimentally and theoretically [21–25]. This is particularly intriguing given the established interest in lithium fluoride (LiF) as a component in various applications, including optics and battery technologies [26–28]. The combination of lithium fluoride with silver(II) fluoride could potentially lead to novel materials with unique properties, yet this area remains largely unexplored. To fill this gap, we initiated a systematic theoretical investigation of ternary systems containing lithium, silver(II) and fluorine using density functional theory (DFT). We performed a systematic exploration of ternary Li–Ag(II)–F systems using the XtalOpt evolutionary algorithm [29, 30], aimed at identifying energetically favourable structures across a broad range of stoichiometries.

This study provides the first theoretical insights into Li–Ag(II)–F systems, revealing their structural diversity, thermodynamic stability, magnetic behaviour and their potential preparation pathways.
 

## 2 Methods

The structural screening was conducted using self-learning algorithms incorporated within the XtalOpt r.13.2 software  \( [29, 30] \) . Structures were randomly generated and augmented by those derived from previous studies on systems containing related alkali metals  \( M^{(I)}Ag^{(II)}F_{3} \) , at both ambient and elevated pressure conditions  \( [22] \) . The latter were altered by  \( M^{+} \longrightarrow Li^{+} \) substitutions. Considering that lithium is considerably smaller than the other alkali metal cations, the high-pressure polymorphs were introduced into the initial pool of structures. Similarly to the methodology applied in  \( Li_{2}AgF_{4} \) , the study also involved the incorporation of modified structures into the initial pool  \( [21, 31] \) , with subsequent alterations executed accordingly. Unit cells containing 2, 4, or 6 formula units per cell were tested. For each stoichiometry and formula units per unit cell, usually 650 structures were generated, in which 100 of them were initial starting structures.

The calculations were performed using VASP 5.4.4 (Vienna Ab initio Simulation Package) \( ^{[32-34]} \) . The projector augmented-wave (PAW) method  \( [35, 36] \) , with pseudopotentials generated within the PBE formalism, was employed to describe the interaction between valence electrons and ionic cores. The exchange-correlation potential was treated within the generalized gradient approximation (GGA) using the PBEsol functional  \( [37] \) . The cut-off energy of the plane wave basis set was equal to 600 eV with a self-consistent-field convergence criterion of  \( 10^{-7} \)  eV.

Numerous equilibrium structures were obtained. In the second stage, the most promising fifteen unique (lowest enthalpy) structures obtained from preliminary screening were optimized in various ferromagnetic and antiferromagnetic models using the DFT+U for the proper description of localized d electrons in the Dudarev formulation  \( [38] \) , with on-site Coulomb and exchange parameters of U = 5.0 eV and J = 1.0 eV applied to the relevant d orbitals of Ag. The Hubbard U correction  \( (DFT + U) \)  is essential for an accurate description of the strongly correlated 4d electrons in Ag(II)  \( [5, 10, 11] \) .

Finally, the optimized structures were symmetrized using FINDSYM v.7.1.7 [39, 40], and the superexchange constants were calculated.

## 3 Results and Discussion

## 3.1 The crystal structures

The structural search revealed a number of low-energy structures of  \( LiAgF_{3} \)  and  \( Li_{2}AgF_{4} \) . Table 1 summarizes the calculated cell parameters for the lowest energy structures predicted together with their space groups. They are either monoclinic or triclinic and two belong to polar space groups (Cc and  \( P2_{1} \) ). Importantly, all monoclinic polymorphs are unique structure types as none of them is analogous to any known polymorphs in the  \( M^{(I)}Ag^{(II)}F_{3} \)  family (M=Na, K, Rb, Cs). The triclinic one,  \( LiAgF_{3}-2 \) , however, is formally isotypic to  \( AgCuF_{3} \)  and  \( NaCuF_{3} \)  [41].

Table 1: Optimized unit cell parameters and crystallographic space groups for theoretically predicted Li–Ag–F structures of  \( LiAgF_{3} \)  and  \( Li_{2}AgF_{4} \) .

<table><tr><td>Structure</td><td>Space group</td><td>a ( \( \textup{\AA} \) )</td><td>b ( \( \textup{\AA} \) )</td><td>c ( \( \textup{\AA} \) )</td><td>\( \alpha \)  ( \( ^{\circ} \) )</td><td>\( \beta \)  ( \( ^{\circ} \) )</td><td>\( \gamma \)  ( \( ^{\circ} \) )</td></tr><tr><td>LiAgF_{3}-1</td><td>Cc</td><td>3.410</td><td>14.628</td><td>4.999</td><td>90.0</td><td>93.8</td><td>90.0</td></tr><tr><td>LiAgF_{3}-2</td><td>P \( \overline{1} \)</td><td>5.079</td><td>5.800</td><td>8.316</td><td>94.9</td><td>100.4</td><td>90.2</td></tr><tr><td>Li_{2}AgF_{4}-1</td><td>C2/c</td><td>20.986</td><td>5.739</td><td>5.009</td><td>90.0</td><td>99.4</td><td>90.0</td></tr><tr><td>Li_{2}AgF_{4}-2</td><td>P2_{1}/c</td><td>5.481</td><td>5.799</td><td>5.032</td><td>90.0</td><td>107.1</td><td>90.0</td></tr><tr><td>Li_{2}AgF_{4}-3</td><td>P2_{1}</td><td>3.294</td><td>5.205</td><td>9.778</td><td>90.0</td><td>94.6</td><td>90.0</td></tr></table>
 
![](2512.05048v1-images/2_0.jpg)

Figure 1: Crystal structures of the investigated  \( LiAgF_{3} \)  structures obtained from DFT calculations. Large dark-gray spheres – Ag(II), small gray spheres – F, green spheres – Li. (top) Ag – F sublattice, (middle) Li – F sublattice, and (bottom) polyhedral coordination spheres are shown.

The lowest-energy  \( LiAgF_{3}-1 \)  polymorph crystallises in the Cc space group. The Ag(II) cation adopts an elongated octahedral environment, with four short Ag-F bonds (2.055Å–2.090Å) and two longer ones around 2.50Å. This geometry is very similar to that found for  \( AgF_{2} \)  (four short bonds: 2.067Å 2.071Å and two long ones 2.588Å) and it is consistent with a Jahn-Teller distortion, a feature commonly observed in other Ag(II)-F systems [42–44]. The Ag-F-Ag angle between the short bonds of adjacent Ag(II) cations is 136.9°. The lithium cations exhibit disordered tetrahedral coordination, with Li-F bond lengths of 1.884Å–1.932Å, substantially shorter than those found in crystalline LiF (2.014Å, with a regular octahedral environment [45]). The Cc polymorph has not yet been observed for other alkali metal – Ag(II) fluorides. Its polar space group might indicate ferroelectric or even multiferroic properties, which are of interest for fluoride materials [46–48].

An alternative low-energy structure,  \( LiAgF_{3}-2 \) , has approximately 3.7% smaller volume than the ground state one and it belongs to the common triclinic centrosymmetric  \( P\overline{1} \)  space group. Here, the Ag(II) environment is also elongated octahedral: the four shorter Ag-F bonds (2.012Å–2.083Å) are slightly shorter, whereas the two longer ones (2.821Å–2.896Å) are about 13.8% longer than in  \( LiAgF_{3}-1 \) . Such behaviour originates from the plasticity of the Jahn-Teller effect-driven distortion of the first coordination sphere of Ag(II) [49]. The corresponding Ag-F-Ag angles are 112.1° and 180° which leads to the formation of helix-like motifs in this structure. Lithium cation adopts an elongated octahedral coordination with two 1.985Å, two 1.969Å and two 2.124Å bonds. An average Li-F bond length is 2.026Å thus not far from that for pristine LiF crystal (2.014Å).
 

In contrast to other  \( MgF_{3} \)  compounds, which exhibit a distorted perovskite structure where the alkali metal atom substantially affects the degree of distortion [10], the  \( LiAgF_{3} \)  structures explored in this work do not follow this trend. In both  \( LiAgF_{3} \)  post-perovskite structures (Figure 1), kinked  \( [AgF_{2/1+2/2}]^{-} \) chains are observed. It is worth noting that for theoretically predicted high-pressure polymorphs of  \( MgF_{3} \)  [50], increasing pressure leads to a gradual tilting of the infinite  \( [AgF_{6}]^{-} \) chains. Thus, the  \( \mathrm{LiAg}^{(II)}\mathrm{F}_{3} \)  polymorphs studied here turn out to be analogues of high-pressure phases of heavier alkali metal systems.

![](2512.05048v1-images/3_0.jpg)

Figure 2: Crystal structures of the investigated  \( Li_{2}AgF_{4} \)  structures obtained from DFT calculations. Large dark-gray spheres - Ag(II), small gray spheres - F, green spheres - Li. (top) Ag – F sublattice, (middle) Li – F sublattice, and (bottom) polyhedral coordination spheres are shown.

Within the  \( Li_{2}AgF_{4} \)  stoichiometry (Figure 2), the  \( Li_{2}AgF_{4-1} \)  polymorph is predicted to be the most stable. It crystallises in the common centrosymmetric  \( C2/c \)  space group. Again,  \( \mathrm{Ag(II)} \)  adopts a severely elongated octahedral environment typical of strong Jahn-Teller distortion. The four shorter Ag—F bonds range from 2.066Å to 2.071Å, while the two longer ones are about 2.73Å. The angle of Ag-F-Ag between the short bonds is 130.0°. Lithium cations are coordinated by nearly regular octahedra, with six Li-F distances in the 1.946Å–2.094Å range.

The structure of  \( Li_{2}AgF_{4-3} \)  is approximately 9.27% larger in volume than  \( Li_{2}AgF_{4-2} \) . The first of those belongs to the most common monoclinic  \( P2_{1}/c \)  space group, whereas the second one to a rare lower-symmetry  \( P2_{1} \)  one. The latter may give rise to diverse useful nonlinear properties typical of non-centrosymmetric crystals. In both cases, the  \( \mathrm{Ag(II)} \)  cations adopt an elongated octahedral coordination environment. In  \( Li_{2}AgF_{4-2} \) , two types of short Ag–F bonds are observed (2.058Å and 2.072Å) together with two very long ones (2.934Å). For  \( Li_{2}AgF_{4-3} \) , four short Ag–F bonds range from 2.059Å to 2.086Å, which are slightly longer than those in  \( Li_{2}AgF_{4-2} \) , whereas the two longer Ag–F bonds (2.484Å and 2.526Å) are somewhat shorter. The fact they differ from each other certifies the lack of the symmetry center at  \( \mathrm{Ag(II)} \)  site; this has also been observed for the  \( HP1 \)  structure of  \( AgF_{2} \)  at elevated pressure [51]. In  \( Li_{2}AgF_{4-2} \)  the short Ag–F bonds are almost perpendicular (98.7° angle) and in  \( Li_{2}AgF_{4-3} \)  the Ag–F–Ag angle is 134.0°.
 

The lithium coordination environment in  \( Li_{2}AgF_{4}-2 \)  can be described as an elongated octahedron with four short Li-F bonds (1.933Å–1.962Å) and two longer ones (2.043Å and 2.113Å). In contrast,  \( Li_{2}AgF_{4}-3 \)  exhibits a slightly distorted tetrahedral coordination, with Li-F bond lengths ranging from 1.878Å to 1.966Å. Such bond length difference for octahedral and tetrahedral coordination spheres is in line with the values of ionic radii of  \( Li^{+} \) in these environments (0.73Å for CN=4, 0.90Å for CN=6).

Previously studied  \( M_{2}AgF_{4} \)  compounds are characterized either by a layered perovskite structure with  \( [AgF_{4/2+2}]^{2-} \)  layers, or by a post-perovskite ( \( Na_{2}CuF_{4} \) -type) structures featuring chains of elongated  \( [AgF_{6}]^{4-} \)  octahedra [44]. In contrast (but similarly to the  \( LiAgF_{3} \)  phases), for the  \( Li_{2}AgF_{4} \)  structures explored in this work, tilted  \( [AgF_{4}]^{2-} \)  chains are present in most cases, except for  \( Li_{2}AgF_{4}-2 \) , where isolated squares  \( [AgF_{4}]^{2-} \)  are found (similar to those in  \( BaAgF_{4} \)  [52]). The preference for isolated squares over kinked chains may be explained by the higher Lewis acidity of  \( Li^{+} \) compared to  \( Na^{+} \) , which promotes stronger interactions with the fluoride ligands.

## 3.2 Magnetic properties

For all cells studied the magnetic cells are equivalent to the unit cells. Structural relaxations were carried out under both ferromagnetic (FM) and antiferromagnetic (AFM) spin orderings, with AFM proving more stable in all cases (methodology and corresponding illustrations are available in the Supplementary Information). Spin-polarised DFT+U calculations further indicate that magnetic ordering has only a minor effect on the relative energies of the polymorphs.

We have derived the magnetic superexchange constants, J, for all structures. For  \( LiAgF_{3}-1 \) , the calculated superexchange constant has a value of J = -78 meV. Among the  \( Li_{2}AgF_{4} \)  stoichiometries, the highest J value was calculated for  \( Li_{2}AgF_{4}-3 \) , with J = -95 meV, which is comparable with that found experimentally for  \( KAgF_{3} \)  [53]. On the other hand, for  \( Li_{2}AgF_{4}-2 \)  the superexchange constant was the smallest among all investigated structures: J = -4 meV. This arises from the silver(II) cations being arranged almost perpendicularly to each other and the Ag–F–Ag superexchange pathway forming between one very long and one short Ag–F bond, which strongly suppresses the magnetic coupling. The  \( Li_{2}AgF_{4}-1 \)  superexchange constant had a value of J = -62 meV due to the presence of the Ag-F-Ag chain in this structure.

LiAgF_{3}-2 is a remarkable exception here as it exhibits an immense superexchange constant of  \( J_{1} = -359 \)  meV within the  \( [Ag_{2}F_{7}] \)  dimers and a much smaller one of  \( J_{2} = -11 \)  meV between them (Figure 3a). The  \( [AgF_{4}] \)  squares are interconnected via very short Ag–F bonds (2.014Å) at a 180° angle, which enables this exceptionally strong superexchange. Other structures exhibiting similar structural motifs have been reported, such as CsAgF_{3}, AgF_{2}-HPII and Ag_{2}ZnZr_{2}F_{14} (Figure 3b) which also exhibit high J values (-161 meV, -250 meV and -313 meV, respectively, calculated using identical methodology as the one used here) [54]. The value calculated for LiAgF_{3}-2 is larger than that previously measured for Sr_{2}CuO_{3} (-240 meV) [55].

This leads to the conclusion that the  \( LiAgF_{3}-2 \)  polymorph is worth targeting in experiment, as it may host a record-breaking superexchange between transition metal cations.
 
![](2512.05048v1-images/5_0.jpg)

Figure 3: a - Local magnetic structure of  \( LiAgF_{3-1} \)  showing the orientations of the spin moments on the Ag(II) cations. The solid lines indicate the nearest-neighbor superexchange pathways  \( (J_{1}) \) , and the dashed blue lines the next-nearest-neighbor ones  \( (J_{2}) \) ; bond lengths and angles are shown; b - Comparison of different structural motifs containing the  \( [Ag_{2}F_{7}] \)  unit, including chain- and dimer-type arrangements, together with their corresponding magnetic superexchange constants.

## 3.3 Thermodynamic stability analysis and synthesis pathways

The calculations revealed that even the most energetically favourable  \( Li—Ag(II)—F \)  arrangements are slightly unstable (by 8-18 kJ/mol) with respect to decomposition into known binary phases. All candidate polymorphs considered here lie above the convex hull (Figure 4a), indicating their metastability with respect to LiF and  \( AgF_{2} \)  mixture. To assess whether temperature entropic effects could stabilise any of these phases, the entropy contribution was estimated following the approach proposed by Jenkins and Glasser [56]. The corresponding stabilisation temperatures, at which the free-energy penalty ( \( \Delta E_{form} - T\Delta S \) ) would be null, are summarised in Table 2.

The calculated stabilization temperatures are quite high and range from  \( \approx 900 \)  K for  \( Li_{2}AgF_{4}-3 \)  to  \( \approx 2400 \)  K for  \( Li_{2}AgF_{4}-1 \) . Noting that  \( AgF_{2} \)  begins to decompose thermally at approximately 600 K (ca.  \( 300\ ^{\circ}C \) ) under dynamic vacuum or inert atmosphere conditions [57, 58], these results imply that none of the proposed structures could be obtained via elevated temperature synthesis.

Table 2: Thermodynamic properties of the investigated systems, including the internal energy difference  \( \Delta E \) , volume difference per formula unit  \( \Delta V \) , and estimated absolute entropy difference as compared to binary phases  \( \Delta S \) . The entropy term was calculated based on the volume differences between the hypothetical mixture of  \( xAgF_{2} + yLiF \)  and the DFT+U-optimized structures [56]. The temperature T at which the entropy contribution compensates the internal energy difference is also reported.

<table><tr><td></td><td>\( \Delta E \)  [kJ/mol]</td><td>\( \Delta V \)  [ \( \text{\AA}^{3} \) /f.u.]</td><td>\( \Delta S \)  [J/mol·K]</td><td>T [K]</td></tr><tr><td>\( LiAgF_{3-1} \)</td><td>10.1</td><td>5.7</td><td>10.1</td><td>1004</td></tr><tr><td>\( LiAgF_{3-2} \)</td><td>11.6</td><td>3.5</td><td>6.2</td><td>1866</td></tr><tr><td>\( Li_{2}AgF_{4-1} \)</td><td>8.1</td><td>1.9</td><td>3.3</td><td>2449</td></tr><tr><td>\( Li_{2}AgF_{4-2} \)</td><td>10.5</td><td>3.9</td><td>6.9</td><td>1512</td></tr><tr><td>\( Li_{2}AgF_{4-3} \)</td><td>18.1</td><td>11.0</td><td>19.4</td><td>934</td></tr></table>

Considering that, phases with stabilisation temperatures below the decomposition point of  \( AgF_{2} \)  could, in principle, be obtained without prior breakdown of the binary fluoride precursor. In this context,  \( Li_{2}AgF_{4}-3 \)  (with  \( T \approx 934~K \) ) lies very close to the  \( AgF_{2} \)  decomposition threshold, suggesting marginal synthetic accessibility from the mixture of the binary fluorides. All other predicted phases require significantly higher temperatures, where at such conditions,  \( AgF_{2} \)  is expected to decompose, releasing  \( F_{2} \) , and therefore the formation of these ternary compounds becomes difficult under equilibrium synthesis routes. It is worth noting that although the  \( Li_{2}AgF_{4}-1 \)  structure lies closest to the stability line, the corresponding stabilisation temperature presented in Table 2
 

is the highest among the investigated phases. The high stabilization temperature is a result of the smallest difference between the predicted size of the unit cell and the sum of volumes of the substrates, which leads to a reduced entropy contribution.

On the other hand, there should be other possible ways of synthesis to obtain those compounds, such as high-temperature fluorination under fluorine pressure, followed by rapid quenching which could lead to trapping metastable arrangements that are inaccessible through conventional solid state-solid state reactions. To explore whether alternative synthetic routes are possible, we computed the formation energies of reaction pathways involving  \( AgF, LiF, \)  and either  \( F_{2} \)  (fluorine gas) or  \( F^{*} \)  (fluorine radical). Both pathways are predicted to be thermodynamically feasible, indicating that the formation of these phases is energetically accessible. The calculated formation energies  \( (\Delta E) \)  for all considered  \( LiAgF_{3} \)  and  \( Li_{2}AgF_{4} \)  polymorphs are summarised in Figure 4b. As expected, reactions involving the fluorine radical are significantly more exothermic than those with molecular fluorine, suggesting that radical fluorination could facilitate compound formation under suitable conditions. Yet another potential pathway is provided by a gentle thermal decomposition of  \( \mathrm{LiAg^{(III)}F_{4}} \) , by analogy to the route employed for the preparation of  \( KAgF_{3} \)  [53].

![](2512.05048v1-images/6_0.jpg)

Figure 4: a - Convex hull of the investigated systems as a function of the  \( AgF_{2} \)  molar fraction. All structures lie slightly above the convex hull, indicating that they are thermodynamically unstable with respect to binary fluorides; b - Schematic energy profiles ( \( \Delta E \)  [kJ/mol]) for the formation of the most stable lithium–silver(II)–fluorine compounds. The left diagram corresponds to  \( LiAgF_{3-1} \) , and the right one to  \( Li_{2}AgF_{4-1} \) . The figure indicates that the synthesis of the presented structures is feasible, though it may proceed via alternative substrates (i.e., not from  \( AgF_{2} \)  and LiF).

## 4 Conclusions

In this work, we investigated the stability and magnetic properties of hypothetical ternary compounds in the  \( \mathrm{Li}-\mathrm{Ag(II)}-\mathrm{F} \)  system. Convex hull analysis shows that all candidate phases are metastable with respect to decomposition into LiF and  \( AgF_{2} \) . Although entropic effects could theoretically stabilize these polymorphs at finite temperatures, their experimental realization may be limited by the low thermal instability of  \( AgF_{2} \) . Nevertheless, our analysis suggests that these Li–Ag–F structures could potentially be accessed via alternative synthetic routes, for instance by combining  \( AgF, LiF, \)  and fluorine gas or fluorine radicals. These findings provide motivation for experimental efforts to explore such metastable compounds, as they may exhibit interesting magnetic and structural properties despite their metastability. Indeed, our results indicate that  \( LiAgF_{3-2} \)  polymorph exhibits a record-large superexchange constant of J = -359 meV within  \( [Ag_{2}F_{7}] \)  dimers, arising from its very short bridging Ag–F bonds. Although this J is exhibited here by quasi-OD bimetallic dimers, yet it suggests that exceptionally J values could be found also for 1D and 2D  \( \mathrm{Ag(II)} \) -based systems. Thus,  \( LiAgF_{3-2} \)  represents a meaningful step towards the regime in which magnetic-fluctuations-driven room- \( T_{c} \)  superconductivity is theoretically predicted to emerge, as such behaviour is expected for 2D systems with superexchange strengths on the order of  \( J \approx 400-700 \)  meV [59]. Overall, these findings establish Li–Ag–F systems as a promising and previously unexplored family of materials, highlight the possibility of achieving unprecedented strong magnetic interactions in  \( \mathrm{Ag(II)} \) -based fluorides, and provide a foundation for future synthetic and theoretical investigations into highly-correlated quantum materials.
 

## 5 Acknowledgements

This work was supported by the Polish National Science Center (project 2024/53/B/ST5/00631). Computations were performed at the ICM (University of Warsaw, GA83-34).

## 6 Supplementary Information

The Electronic Supplementary Information file contains crystallographic information files for the lowest energy structures, the magnetic models and derivation of the J values, as well as electronic band structure and density of states together with the values of the direct and indirect band gaps.

## References

(1) J. McMillan, Chemical Reviews, 1962, 62, 65–80.

(2) P. Fischer, D. Schwarzenbach and H. Rietveld, Journal of Physics and Chemistry of Solids, 1971, 32, 543–550.

(3) W. Grochala, R. G. Egdell, P. P. Edwards, Z. Mazej and B. Žemva, ChemPhysChem, 2003, 4, 997–1001.

(4) C. Miller and A. S. Botana, Physical Review B, 2020, 101, 195116.

(5) P. Fischer, G. Roult and D. Schwarzenbach, Journal of Physics and Chemistry of Solids, 1971, 32, 1641–1647.

(6) Z. Mazej, D. Kurzydłowski and W. Grochala, in Photonic and Electronic Properties of Fluoride Materials, Elsevier, 2016, pp. 231–260.

(7) S. E. McLain, M. R. Dolgos, D. A. Tennant, J. F. C. Turner, T. Barnes, T. Proffen, B. C. Sales and R. I. Bewley, Nature Materials, 2006, 5, 561–565.

(8) W. Grochala and Z. Mazej, Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 2015, 373, 20140179.

(9) W. Grochala and R. Hoffmann, Angewandte Chemie International Edition, 2001, 40, 2742–2781.

(10) K. Koteras, J. Gawraczyński, G. Tavčar, Z. Mazej and W. Grochala, CrystEngComm, 2022, 24, 1068–1077.

(11) D. Kurzydłowski and W. Grochala, Angewandte Chemie, 2017, 129, 10248–10251.

(12) T. Jaroń and W. Grochala, physica status solidi (RRL)-Rapid Research Letters, 2008, 2, 71–73.

(13) W. J. Casteel Jr, G. Lucier, R. Hagiwara, H. Borrmann and N. Bartlett, Journal of solid state chemistry, 1992, 96, 84–96.

(14) K. Kuder, K. Koteras, Z. Mazej and W. Grochala, arXiv preprint arXiv:2408.10753, 2024.

(15) M. Belak Vivod, Z. Jaglićić, G. King, T. C. Hansen, M. Lozinšek and M. Dragomir, Journal of the American Chemical Society, 2024, 146, 30510–30517.

(16) R. Fischer and B. Müller, Zeitschrift für anorganische und allgemeine Chemie, 2002, 628, 2592–2596.

(17) B. Zemva, K. Lutar, A. Jesih, W. J. Casteel Jr, A. P. Wilkinson, D. E. Cox, R. B. Von Dreele, H. Borrmann and N. Bartlett, Journal of the American Chemical Society, 1991, 113, 4192–4198.

(18) C. Shen, B. Zemva, G. M. Lucier, O. Graudejus, J. A. Allman and N. Bartlett, Inorganic Chemistry, 1999, 38.

(19) M. Kraus, M. Müller, R. Fischer, R. Schmidt, D. Koller and B. Müller, Journal of Fluorine Chemistry, 2000, 101, 165–171.

(20) O. Graudejus, S. H. Elder, G. M. Lucier, C. Shen and N. Bartlett, Inorganic Chemistry, 1999, 38, 2503–2509.

(21) R.-H. Odenthal, D. Paus and R. Hoppe, Zeitschrift für anorganische und allgemeine Chemie, 1974, 407, 144–150.
 

(22) L. Wolański, M. Metzelaars, J. van Leusen, P. Kögerler and W. Grochala, Chemistry – A European Journal, 2022, 28, e202200712.

(23) R.-H. Odenthal, D. Paus and R. Hoppe, Zeitschrift für anorganische und allgemeine Chemie, 1974, 407, 144–150.

(24) Z. Mazej, E. Goreshnik, Z. Jaglićić, B. Gawel, W. Lasocha, D. Grzybowska, T. Jaroń, D. Kurzydłowski, P. Malinowski, W. Koźminski, J. Szydłowska, P. Leszczyński and W. Grochala, CrystEngComm, 2009, 11, 1702–1710.

(25) R.-H. Odenthal and R. Hoppe, Monatshefte für Chemie / Chemical Monthly, 1971, 102, 1340–1350.

(26) Y.-H. Tan, G.-X. Lu, J.-H. Zheng, F. Zhou, M. Chen, T. Ma, L.-L. Lu, Y.-H. Song, Y. Guan, J. Wang et al., Advanced Materials, 2021, 33, 2102134.

(27) Y. Sun, H.-W. Lee, G. Zheng, Z. W. Seh, J. Sun, Y. Li and Y. Cui, Nano Letters, 2016, 16, 1497–1501.

(28) B. Fleming, M. Quijada, J. Hennessy, A. Egan, J. D. Hoyo, B. A. Hicks, J. Wiley, N. Kruczek, N. Erickson and K. France, Applied Optics, 2017, 56, 9941–9950.

(29) S. Hajinazar and E. Zurek, Computer Physics Communications, 2024, 304, 109306.

(30) Z. Falls, P. Avery, X. Wang, K. P. Hilleke and E. Zurek, The Journal of Physical Chemistry C, 2021, 125, 1601–1620.

(31) D. Kurzydłowski, Z. Mazej and W. Grochala, Dalton Transactions, 2013, 42, 2167–2173.

(32) G. Kresse and J. Hafner, Physical review B, 1993, 47, 558–561.

(33) G. Kresse and J. Furthmüller, Computational Materials Science, 1996, 6, 15–50.

(34) G. Kresse and J. Furthmüller, Physical review B, 1996, 54, 11169–11186.

(35) G. Kresse and D. Joubert, Physical review B, 1999, 59, 1758–1775.

(36) P. E. Blöchl, Physical review B, 1994, 50, 17953–17979.

(37) J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou and K. Burke, Physical review letters, 2008, 100, 136406.

(38) S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys and A. P. Sutton, Physical review B, 1998, 57, 1505–1509.

(39) H. T. Stokes, D. M. Hatch and B. J. Campbell, FINDSYM, ISOTROPY Software Suite, https://iso.byu.edu, Brigham Young University.

(40) H. T. Stokes and D. M. Hatch, Journal of Applied Crystallography, 2005, 38, 237–238.

(41) J. Tong, C. Lee, M.-H. Whangbo, R. Kremer, A. Simon and J. Köhler, Solid state sciences, 2010, 12, 680–684.

(42) I. Sánchez-Movellán, J. Moreno-Ceballos, P. García-Fernández, J. A. Aramburu and M. Moreno, Chemistry–A European Journal, 2021, 27, 13582–13590.

(43) D. Kurzydłowski, Crystals, 2018, 8, 140.

(44) D. Kurzydłowski, T. Jaroń, A. Ozarowski, S. Hill, Z. Jaglićić, Y. Filinchuk, Z. Mazej and W. Grochala, Inorganic Chemistry, 2016, 55, 11479–11489.

(45) K. Dupre, K. Recker and F. Wallrafen, Materials research bulletin, 1992, 27, 311–318.

(46) G. Calestani and F. Mezzadri, in Photonic and Electronic Properties of Fluoride Materials, ed. A. Tressaud and K. Poeppelmeier, Elsevier, Boston, 2016, pp. 285–307.

(47) F. Ali, T. Ali, D. Lehninger, A. Sünbül, A. Viegas, R. Sachdeva, A. Abbas, M. Czernohorsky and K. Seidel, Advanced Functional Materials, 2022, 32, 2201737.

(48) J. F. Scott and R. Blinc, Journal of Physics-Condensed Matter, 2011, 23, 113202.

(49) W. Grochala, physica status solidi (b), 2006, 243, R81–R83.

(50) J. Gawraczyński, L. Wolański, A. Grzelak, Z. Mazej, V. Struzhkin and W. Grochala, Crystals, 2022, 12, 458.

(51) A. Grzelak, J. Gawraczyński, T. Jaroń, D. Kurzydłowski, A. Budzianowski, Z. Mazej, P. J. Leszczyński, V. B. Prakapenka, M. Derzsi, V. V. Struzhkin et al., Inorganic Chemistry, 2017, 56, 14651–14661.
 

(52) R.-H. Odenthal and R. Hoppe, Zeitschrift für anorganische und allgemeine Chemie, 1971, 385, 92–101.

(53) D. Kurzydlowski, Z. Mazej, Z. Jaglićić, Y. Filinchuk and W. Grochala, Chemical Communications, 2013, 49, 6262–6264.

(54) D. Kurzydlowski, M. Derzsi, P. Barone, A. Grzelak, V. Struzhkin, J. Lorenzana and W. Grochala, Chemical Communications, 2018, 54, 10252–10255.

(55) C. de Graaf and F. Illas, Physical review B, 2000, 63, 014404.

(56) H. D. B. Jenkins and L. Glasser, Inorganic Chemistry, 2003, 42, 8702–8708.

(57) W. Grochala, Journal of Fluorine Chemistry, 2008, 129, 82–90.

(58) A. Grzelak, M. Derzsi and W. Grochala, Inorganic Chemistry, 2021, 60, 1561–1570.

(59) Q. Qin and Y.-f. Yang, npj Quantum Materials, 2025, 10, 13.
 

# Prediction of Novel Li–Ag(II)–F Compounds using Evolutionary Algorithms – Supplementary information

Katarzyna Kuder, Wojciech Grochala

## Contents

S1 Plane-Wave Cutoff Energy ( \( E_{cut} \) ) and k-Point Mesh Convergence 1
S2 Crystallographic Information Files 2
S2.1  \( LiAgF_{3-1} \)  2
S2.2  \( LiAgF_{3-2} \)  3
S2.3  \( Li_{2}AgF_{4-1} \)  4
S2.4  \( Li_{2}AgF_{4-2} \)  5
S2.5  \( Li_{2}AgF_{4-3} \)  6
S3 Magnetic Configurations 7
S4 Electronic Band Structure and Density of States 10

## S1 Plane-Wave Cutoff Energy ( \( E_{cut} \) ) and k-Point Mesh Convergence

The convergence of the total energy was examined as a function of the plane-wave cutoff energy. As shown in Figure S1, the energy difference between successive cutoff values becomes negligible above approximately 500 eV. Therefore, a cutoff energy of 600 eV was employed for all calculations as it provides a balance between accuracy and computational cost.

![](2512.05048v1-images/10_0.jpg)

Figure S1: The convergence of the total energy as a function of the plane-wave cutoff energy.

Similarly, the convergence of the total energy as a function of increased k-point sampling was assessed. As presented in Figure S2, the energy variation between successive k-point spacing increments is negligible, therefore, an intermediate k-point spacing of  \( 0.065 \, \AA^{-1} \)  was adopted for all production calculations.
 
![](2512.05048v1-images/11_0.jpg)

Figure S2: Total energy convergence with respect to k-point sampling.

## S2 Crystallographic Information Files

## S2.1 LiAgF_{3}-1

# CIF file created by FINDSYM, version 7.1.3

data_findsym-output
_audit_creation_method FINDSYM
_cell_length_a 3.4101600000
_cell_length_b 14.6280813694
_cell_length_c 4.9988100000
_cell_angle_alpha 90.0000000000
_cell_angle_beta 93.7721300000
_cell_angle_gamma 90.0000000000
_cell_volume 248.8209086510

_symmetry_space_group_name_H-M "C 1 c 1"
_symmetry_Int_Tables_number 9
_space_group_reference_setting '009:C -2yc'
_space_group_transform_Pp_abc a,b,c;0,0,0

loop_
_space_group_symop_id
_space_group_symop_operation_xyz
1 x,y,z
2 x,-y,z+1/2
3 x+1/2,y+1/2,z
4 x+1/2,-y+1/2,z+1/2

loop_
_atom_type_symbol
Ag
F
Li

loop_
_atom_site_label
 

_atom_site_type_symbol
_atom_site_symmetry_multiplicity
_atom_site_Wyckoff_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
_atom_site_fract_symmform
Ag1 Ag 4 a 0.7469825000 0.1642350000 0.2922900000 1.0000000000 Dx,Dy,Dz
F1 F 4 a 0.3179150000 0.0735675000 0.1346650000 1.0000000000 Dx,Dy,Dz
F2 F 4 a 0.3073650000 0.4172975000 0.1273100000 1.0000000000 Dx,Dy,Dz
F3 F 4 a 0.1762750000 0.2519125000 0.4595050000 1.0000000000 Dx,Dy,Dz
Li1 Li 4 a 0.8195775000 0.4490700000 0.2636200000 1.0000000000 Dx,Dy,Dz

# end of cif

## S2.2 LiAgF_{3-2}

# CIF file created by FINDSYM, version 7.1.3

data_findsym-output
_audit_creation_method FINDSYM

_cell_length_a 5.0789500000
_cell_length_b 5.8001700000
_cell_length_c 8.3159200000
_cell_angle_alpha 94.8966500000
_cell_angle_beta 100.4164200000
_cell_angle_gamma 90.1959500000
_cell_volume 240.0157193444

_symmetry_space_group_name_H-M "P -1"
_symmetry_Int_Tables_number 2
_space_group.reference_setting '002:-P 1'
_space_group.transform_Pp_abc a,b,c;0,0,0

loop_
_space_group_symop_id
_space_group_symop_operation_xyz
1 x,y,z
2 -x,-y,-z

loop_
_atom_type_symbol
Ag
F
Li

loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_symmetry_multiplicity
_atom_site_Wyckoff_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
 

_atom_site_fract_symmform
Ag1 Ag 2 i 0.3114900000 0.1138500000 0.6836900000 1.0000000000 Dx,Dy,Dz
Ag2 Ag 2 i 0.8125300000 0.6124700000 0.6742600000 1.0000000000 Dx,Dy,Dz
F1 F 1 f 0.5000000000 0.0000000000 0.5000000000 1.0000000000 0,0,0
F2 F 2 i 0.3920800000 0.0139400000 0.1428400000 1.0000000000 Dx,Dy,Dz
F3 F 2 i 0.3633300000 0.5173100000 0.1434300000 1.0000000000 Dx,Dy,Dz
F4 F 2 i 0.8581800000 0.7647500000 0.1206900000 1.0000000000 Dx,Dy,Dz
F5 F 2 i 0.0221650000 0.2527300000 0.5097000000 1.0000000000 Dx,Dy,Dz
F6 F 1 h 0.5000000000 0.5000000000 0.5000000000 1.0000000000 0,0,0
F7 F 2 i 0.8842500000 0.2635300000 0.1374350000 1.0000000000 Dx,Dy,Dz
Li1 Li 2 i 0.5135900000 0.2567600000 0.0271400000 1.0000000000 Dx,Dy,Dz
Li2 Li 1 c 0.0000000000 0.5000000000 0.0000000000 1.0000000000 0,0,0
Li3 Li 1 a 0.0000000000 0.0000000000 0.0000000000 1.0000000000 0,0,0

# end of cif

## S2.3 Li₂AgF₄-1

# CIF file created by FINDSYM, version 7.1.3

data_findsym-output
_audit_creation_method FINDSYM

_cell_length_a 20.9862000000
_cell_length_b 5.7389300000
_cell_length_c 5.0092000000
_cell_angle_alpha 90.0000000000
_cell_angle_beta 99.4446700000
_cell_angle_gamma 90.0000000000
_cell_volume 595.1216834805

_symmetry_space_group_name_H-M "C 1 2/c 1"
_symmetry_Int_Tables_number 15
_space_group.reference_setting '015:-C 2yc'
_space_group.transform_Pp_abc a,b,c;0,0,0

loop_
_space_group_symop_id
_space_group_symop_operation_xyz
1 x,y,z
2 -x,y,-z+1/2
3 -x,-y,-z
4 x,-y,z+1/2
5 x+1/2,y+1/2,z
6 -x+1/2,y+1/2,-z+1/2
7 -x+1/2,-y+1/2,-z
8 x+1/2,-y+1/2,z+1/2

loop_
_atom_type_symbol
Ag
F
Li

loop_
_atom_site_label
 

_atom_site_type_symbol
_atom_site_symmetry_multiplicity
_atom_site_Wyckoff_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
_atom_site_fract_symmform
Ag1 Ag 8 f 0.4326900000 0.2508600000 -0.0462000000 1.0000000000 Dx,Dy,Dz
F1 F 8 f 0.3589900000 0.1207075000 0.6683000000 1.0000000000 Dx,Dy,Dz
F2 F 8 f 0.2498600000 0.3738700000 0.7476600000 1.0000000000 Dx,Dy,Dz
F3 F 4 e 0.0000000000 -0.0972100000 0.2500000000 1.0000000000 0,Dy,0
F4 F 4 e 0.0000000000 0.4013200000 0.2500000000 1.0000000000 0,Dy,0
F5 F 8 f 0.3595500000 0.3790200000 0.1443900000 1.0000000000 Dx,Dy,Dz
Li1 Li 8 f 0.8020800000 0.3794500000 0.4553900000 1.0000000000 Dx,Dy,Dz
Li2 Li 8 f 0.3100150000 0.3676500000 0.4530300000 1.0000000000 Dx,Dy,Dz

# end of cif

## S2.4 Li₂AgF₄-₂

# CIF file created by FINDSYM, version 7.1.3

data_findsym-output
_audit_creation_method FINDSYM

_cell_length_a 5.4808500000
_cell_length_b 5.7988100000
_cell_length_c 5.0321900000
_cell_angle_alpha 90.0000000000
_cell_angle_beta 107.0774600000
_cell_angle_gamma 90.0000000000
_cell_volume 152.8833540110

_symmetry_space_group_name_H-M "P 1 21/c 1"
_symmetry_Int_Tables_number 14
_space_group.reference_setting '014:-P 2ybc'
_space_group.transform_Pp_abc a,b,c;0,0,0

loop_
_space_group_symop_id
_space_group_symop_operation_xyz
1 x,y,z
2 -x,y+1/2,-z+1/2
3 -x,-y,-z
4 x,-y+1/2,z+1/2

loop_
_atom_type_symbol
Ag
F
Li

loop_
_atom_site_label
_atom_site_type_symbol
 

_atom_site_symmetry_multplicity
_atom_site_Wyckoff_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
_atom_site_fract_symmform
Ag1 Ag 2 d 0.5000000000 0.0000000000 0.5000000000 1.0000000000 0,0,0
F1 F 4 e 0.7910950000 0.6299700000 0.8628200000 1.0000000000 Dx,Dy,Dz
F2 F 4 e 0.7871675000 0.3722500000 0.3337975000 1.0000000000 Dx,Dy,Dz
Li1 Li 4 e 0.0304925000 0.8823725000 0.7674950000 1.0000000000 Dx,Dy,Dz
# end of cif
S2.5 Li₂AgF₄-₃
# CIF file created by FINDSYM, version 7.1.3
data_findsym-output
_audit_creation_method FINDSYM
_cell_length_a 3.2936000000
_cell_length_b 5.2045700000
_cell_length_c 9.7778550969
_cell_angle_alpha 90.0000000000
_cell_angle_beta 94.6339649251
_cell_angle_gamma 90.0000000000
_cell_volume 167.0618710437
_symmetry_space_group_name_H-M "P 1 21 1"
_symmetry_Int_Tables_number 4
_space_group.reference_setting '004:P 2yb'
_space_group.transform_Pp_abc a,b,c;0,0,0
loop_
_space_group_symop_id
_space_group_symop_operation_xyz
1 x,y,z
2 -x,y+1/2,-z
loop_
_atom_type_symbol
Ag
F
Li
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_symmetry_multplicity
_atom_site_Wyckoff_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
_atom_site_fract_symmform
Ag1 Ag 2 a 0.7815300000 0.8254950000 0.3706100000 1.0000000000 Dx,Dy,Dz
 

<table><tr><td>F1</td><td>F</td><td>2 a</td><td>0.7569450000</td><td>0.8231950000</td><td>-0.0209550000</td><td>1.0000000000</td><td>Dx,Dy,Dz</td></tr><tr><td>F2</td><td>F</td><td>2 a</td><td>0.6658400000</td><td>0.4935350000</td><td>0.7630700000</td><td>1.0000000000</td><td>Dx,Dy,Dz</td></tr><tr><td>F3</td><td>F</td><td>2 a</td><td>0.7903850000</td><td>0.5034750000</td><td>0.2485350000</td><td>1.0000000000</td><td>Dx,Dy,Dz</td></tr><tr><td>F4</td><td>F</td><td>2 a</td><td>0.2199000000</td><td>0.6470150000</td><td>0.5042900000</td><td>1.0000000000</td><td>Dx,Dy,Dz</td></tr><tr><td>Li1</td><td>Li</td><td>2 a</td><td>0.7295550000</td><td>0.4603400000</td><td>-0.0360100000</td><td>1.0000000000</td><td>Dx,Dy,Dz</td></tr><tr><td>Li2</td><td>Li</td><td>2 a</td><td>0.2840450000</td><td>0.3533400000</td><td>0.2122100000</td><td>1.0000000000</td><td>Dx,Dy,Dz</td></tr></table>

# end of cif

## S3 Magnetic Configurations

Structural relaxations were performed for both ferromagnetic (FM) and antiferromagnetic (AFM) spin configurations. In all cases, the AFM arrangement was found to be more stable. In the figures below, the magnetic models of all structures are presented.

The superexchange constants were calculated from:

 \[ H=-\frac{1}{2}\sum_{ij}J_{ij}S_{i}S_{j} \quad (1) \] 

where  \( J_{ij} \)  is the magnetic coupling constants between spin sites. Positive values of  \( J_{ij} \)  correspond to FM spin ordering and negative  \( J_{ij} \)  values correspond to AFM spin ordering.

For each structure listed in the tables below, we report the model energy expressions, spin ordering along with the superexchange constants extracted from our calculations.

Table S1: Spin configurations and corresponding energy expressions for the  \( LiAgF_{3-1} \)  models.

<table><tr><td rowspan="2">Model</td><td colspan="3">Atom</td><td rowspan="2">Energy</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>FM</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td>AFM</td><td>+</td><td>-</td><td>+</td><td>-</td></tr><tr><td></td><td></td><td></td><td>J [meV]:</td><td>-77.74</td></tr></table>

Table S2: Spin configurations and corresponding energy expressions for the  \( LiAgF_{3-2} \)  models.

<table><tr><td rowspan="2">Model</td><td colspan="3">Atom</td><td rowspan="2">Energy</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>FM</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td>AFM</td><td>+</td><td>-</td><td>+</td><td>-</td></tr><tr><td>AFM2</td><td>-</td><td>+</td><td>+</td><td>-</td></tr><tr><td></td><td></td><td></td><td>J1 [meV]:</td><td>-358.75</td></tr><tr><td></td><td></td><td></td><td>J2 [meV]:</td><td>-10.54</td></tr></table>

Table S3: Spin configurations and corresponding energy expressions for the  \( Li_{2}AgF_{4-1} \)  models.

<table><tr><td rowspan="2">Model</td><td colspan="8">Atom</td><td rowspan="2">Energy</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>FM</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>E = E0 - 2J</td><td></td></tr><tr><td>AFM</td><td>+</td><td>-</td><td>-</td><td>+</td><td>+</td><td>-</td><td>-</td><td>+</td><td>E = E0 + 2J</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>J [meV]:</td><td></td><td>-62.46</td><td></td></tr></table>
 

Table S4: Spin configurations and corresponding energy expressions for the  \( Li_{2}AgF_{4}-2 \)  models.

<table><tr><td rowspan="2">Model</td><td colspan="2">Atom</td><td rowspan="2">Energy</td></tr><tr><td>1</td><td>2</td></tr><tr><td>FM</td><td>+</td><td>+</td><td>\( E = E_{0} - 0.5J \)</td></tr><tr><td>AFM</td><td>-</td><td>+</td><td>\( E = E_{0} + 0.5J \)</td></tr><tr><td colspan="2">J [meV]:</td><td colspan="2">-4.07</td></tr></table>

Table S5: Spin configurations and corresponding energy expressions for the  \( Li_{2}AgF_{4}-3 \)  models.

<table><tr><td rowspan="2">Model</td><td colspan="2">Atom</td><td rowspan="2">Energy</td></tr><tr><td>1</td><td>2</td></tr><tr><td>FM</td><td>+</td><td>+</td><td>\( E = E_{0} - 0.5J \)</td></tr><tr><td>AFM</td><td>-</td><td>+</td><td>\( E = E_{0} + 0.5J \)</td></tr><tr><td colspan="2">J [meV]:</td><td colspan="2">-95.48</td></tr></table>

![](2512.05048v1-images/17_0.jpg)

Figure S3: Magnetic configurations of all investigated  \( LiAgF_{3} \)  systems are shown. Spin-up Ag(II) cations are represented by grey spheres, while spin-down cations are shown as black spheres. For clarity, Li atoms have been omitted from the illustrations. The calculated superexchange constants are indicated on the corresponding ground-state magnetic structures.
 
![](2512.05048v1-images/18_0.jpg)

Figure S4: Magnetic configurations of all investigated  \( Li_{2}AgF_{4} \)  systems are shown. Spin-up Ag(II) cations are represented by grey spheres, while spin-down cations are shown as black spheres. For clarity, Li atoms have been omitted from the illustrations. The calculated superexchange constants are indicated on the corresponding ground-state magnetic structures.
 

## S4 Electronic Band Structure and Density of States

![](2512.05048v1-images/19_0.jpg)

![](2512.05048v1-images/19_1.jpg)

![](2512.05048v1-images/19_2.jpg)

![](2512.05048v1-images/19_3.jpg)

Figure S5: Spin-resolved density of states (DOS) and projected DOS (pDOS) with orbital contributions for the  \( LiAgF_{3} \)  structures. Spin-up states are shown in the positive direction with solid lines, while spin-down states are shown in the negative direction with dotted lines. The Fermi level is set to 0 eV. For the electronic band structure, an RGB scheme was used, where the line color reflects the character of the band. Each element contributes either red, green, or blue, and the resulting line colour is a mixture of the corresponding contributions.

Table S6: Calculated direct and indirect band gaps for  \( LiAgF_{3} \)  structures.

<table><tr><td>Structure</td><td>Direct band gap (eV)</td><td>Indirect band gap (eV)</td></tr><tr><td>\( LiAgF_{3}-1 \)</td><td>1.608</td><td>1.499</td></tr><tr><td>\( LiAgF_{3}-2 \)</td><td>1.656</td><td>1.523</td></tr></table>
 
![](2512.05048v1-images/20_0.jpg)

![](2512.05048v1-images/20_1.jpg)

![](2512.05048v1-images/20_2.jpg)

![](2512.05048v1-images/20_3.jpg)

![](2512.05048v1-images/20_4.jpg)

![](2512.05048v1-images/20_5.jpg)

Figure S6: Spin-resolved density of states (DOS) and projected DOS (pDOS) with orbital contributions for the  \( Li_{2}AgF_{4} \)  structures. Spin-up states are shown in the positive direction with solid lines, while spin-down states are shown in the negative direction with dotted lines. The Fermi level is set to 0 eV. For the electronic band structure, an RGB scheme was used, where the line color reflects the character of the band. Each element contributes either red, green, or blue, and the resulting line color is a mixture of the corresponding contributions.
 

Table S7: Calculated direct and indirect band gaps for  \( Li_{2}AgF_{4} \)  structures.

<table><tr><td>Structure</td><td>Direct band gap (eV)</td><td>Indirect band gap (eV)</td></tr><tr><td>\( Li_{2}AgF_{4}-1 \)</td><td>1.701</td><td>1.666</td></tr><tr><td>\( Li_{2}AgF_{4}-2 \)</td><td>1.807</td><td>1.609</td></tr><tr><td>\( Li_{2}AgF_{4}-3 \)</td><td>1.631</td><td>1.385</td></tr></table>
 
