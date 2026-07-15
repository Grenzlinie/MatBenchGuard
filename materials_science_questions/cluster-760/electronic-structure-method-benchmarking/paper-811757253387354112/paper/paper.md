# Water as biocatalyst in cytochrome P450†

Devesh Kumar, $^{a}$ Ahmet Altun, $^{a}$ Sason Shaik $^{b}$ and Walter Thiel $^{* a}$

Received 7th April 2010, Accepted 21st April 2010
DOI: 10.1039/c004950f

According to previous quantum mechanics/molecular mechanics (QM/MM) studies, camphor hydroxylation in cytochrome P450 is catalysed by a single water molecule which lowers the computed B3LYP/CHARMM barrier by about 4 kcal mol⁻¹. Gas-phase B3LYP model studies for a variety of different substrates show the generality of this effect. Its origin is an electrostatic enhancement of hydrogen bonding in the transition state for hydrogen abstraction. Attempts are made to correlate the slight variations in the calculated barrier lowerings with substrate properties. Individual water molecules also have a decisive influence on other reactions in cytochrome P450cam, for instance, on the relative propensity for coupling and uncoupling upon protonation of Compound 0 in the wild-type enzyme and its mutants. These and other examples are reviewed briefly. Finally, we address some methodological issues on how to handle the possible involvement of water molecules in biocatalysis at the QM/ MM level.

## 1. Introduction

Water is ubiquitous in biological systems. It is the medium in which the chemistry of life takes place. Apart from its role as bulk solvent, water can also directly participate in biochemical transformations. The biocatalytic function of individual water molecules is addressed in this contribution, using enzymatic reactions in cytochrome P450 as examples.

The cytochrome P450 enzymes are a superfamily of heme-containing oxygenases that catalyse the regio- and stereoselective oxidation of a wide variety of xenobiotics, including numerous drugs. Recent theoretical work on the structure, reactivity, and selectivity of these enzymes has been summarised in two comprehensive reviews.¹,² The commonly accepted active species in cytochrome P450 enzymes is a high-valent iron(iv)-oxo $\pi$-cation radical intermediate called Compound I (Cpd I), which is the most powerful electrophilic oxidant of all the intermediates in the catalytic cycle. The prototypical reaction in P450cam is the hydroxylation of the non-activated $C^{5}$-$H^{5exo}$ bond of camphor by Cpd I. The consensus mechanism of this reaction involves an initial hydrogen abstraction from camphor and a subsequent recombination (rebound) of the formed radical pair. The reaction can occur both on the doublet and quartet spin state (two-state reactivity) which have rate-limiting barriers of similar magnitude for hydrogen abstraction, whereas the rebound step is intrinsically more facile especially in the doublet state.¹,²

$^{a}$Max-Planck-Institut für Kohlenforschung, Kaiser-Wilhelm-Platz 1, 45470 Mülheim, Germany.
E-mail: thiel@mpi-muelheim.mpg.de
$^{b}$The Institute of Chemistry and The Lise Meitner-Minerva Center for Computational Quantum Chemistry, Hebrew University of Jerusalem, Givat Ram Campus, 91904 Jerusalem, Israel

† Electronic supplementary information (ESI) available: Detailed numerical results (Tables S1–S51) as well as optimised structures and correlation plots (Figures S1–S24). See DOI: 10.1039/c004950f

This journal is © The Royal Society of Chemistry 2011
Faraday Discuss., 2011, 148, 373–383 | 373

Several groups have studied the hydrogen abstraction step in P450cam theoreti-cally¹·² using combined quantum mechanics/molecular mechanics (QM/MM) methods,³·⁴ typically describing the QM region by density functional theory (DFT, *e.g.*, B3LYP functional) and the MM region by a standard protein force field (*e.g.*, CHARMM). The initially computed QM/MM barriers were mostly higher than expected, considering the fact that it has not yet been possible to characterise Cpd I in P450cam experimentally. This problem was at least partially resolved in later systematic QM/MM investigations,⁵·⁶ that discovered the catalytic role of a single active-site water molecule. When forming Cpd I by protonation of its precursor (Cpd 0), a water molecule is generated next to the oxo atom of the Fe(IV)=O moiety.⁷ The strength of the hydrogen bond between this water molecule and the oxo atom increases during the course of the hydrogen abstraction in P450cam simply because the oxo atom becomes more negatively charged. The associated barrier lowering in P450cam amounts to about 4 kcal mol⁻¹ at the B3LYP/ CHARMM level. This change can be rationalized in an almost quantitative fashion by a classical electrostatic model (with interaction energies computed on the basis of Mulliken charges), thus confirming that the catalytic effect of the water molecule arises from more favorable electrostatic interactions in the transition state.⁵·⁶

In this article, we explore the generality of this effect by studying the hydrogen abstraction by Cpd I for 9 substrates and a total of 12 different modes of abstraction, both in the doublet and quartet state. This computational survey is done at the DFT level for suitable gas-phase model systems since corresponding systematic QM/MM work would be much more expensive. Section 2 describes the chosen computational approach. Section 3 presents the essential results from this model study, while detailed numerical results and evaluations are documented in the electronic supplementary information (ESI†). Section 4 provides a brief overview over other enzymatic reactions in cytochrome P450 where water plays a decisive mechanistic role. Section 5 addresses the general question of how to treat water in QM/MM studies of enzymatic reactions.

## 2. Computational details
Cpd I was represented by iron-oxo-porphyrin without heme side chains and with an axial SH ligand to represent the coordinating cysteine (40 atoms, corresponding to QM region R1 in our previous QM/MM work⁵·⁶). The following substrates were considered: ethane **1**, propane **2**, phenylethane **3**, *trans*-methyl-phenyl-cyclopropane **4** (known as Me-probe), camphor **5**, propene **6**, toluene **7**, *trans*-isopropyl-phenyl-cyclopropane **8** (known as iPr-probe), and N,N-dimethylaniline **9**. The DFT calculations were carried out for systems consisting of Cpd I and substrate, either with or without an additional water molecule hydrogen bonded to the oxo atom of Cpd I.

The QM calculations employed the B3LYP hybrid functional⁸⁻¹⁰ with the VWN5-LDA correlation as implemented in the Turbomole code.¹¹ In our standard basis set B1,⁵·⁶ the iron atom was described by a small-core effective core potential together with the associated double-zeta quality LACVP basis,¹² while the other atoms were described by the 6-31G basis.¹³ Three larger basis sets were mainly used for single-point calculations: B2W⁶ combines Wachters' all-electron basis at iron¹⁴⁻¹⁶ with Pople-type basis sets¹³ elsewhere (6-31+G* on the six atoms coordinated to iron and the O atom of water, 6-31++G** at the migrating H atom and the H atoms of water, 6-31G on the remaining atoms). B3 denotes the all-electron TZVP basis.¹⁷·¹⁸ B4 consists of a polarized all-electron dzpdf basis at iron¹⁹·²⁰ and Pople-type basis sets¹³ elsewhere (6-31+G* on first-row atoms, 6-31G at all hydrogen atoms). All QM calculations were performed using Turbomole.¹¹

In the case of camphor, starting geometries were extracted from the available QM/ MM optimized structures.⁵·⁶ In the other systems, camphor was manually replaced, and the respective substrate was added in a suitable orientation. The geometries of all reactants and transition states were fully optimised at the B3LYP/B1 level using

the HDLC optimiser²¹ as implemented in the ChemShell package.²² For some of the substrates, optimisations were also done at the B3LYP/B4 level.

## 3. Results
The optimised B3LYP/B1 transition structures for the systems without and with an additional water molecule are shown in Fig. 1 and 2, respectively, which also specify the values of some key distances (for more detailed data see ESI,† Tables S46 and S47). In propane, there is a separate transition state (TS) for hydrogen abstraction from the primary (**2n**) and secondary (**2i**) carbon atoms, respectively. Likewise, in phenylethane, there are separate TS structures for the transfer of a primary (**3n**) and benzylic (**3b**) hydrogen atom.

In the water-free systems (Fig. 1), the overall shape of the transition states is similar for all substrates (both in the doublet and the quartet), with an essentially linear $\mathrm{O\cdots H\cdots C}$ arrangement at the migrating hydrogen atom (angles of 166–175°). In the presence of an additional water molecule (W903, notation as in P450cam), this shape is generally retained ($\mathrm{O\cdots H\cdots C}$ angles of 163–177°): W903

![](./images/811757253387354112_1.jpg)

Fig. 1 B3LYP/B1 optimized transition structures in the absence of W903 (see text). Key distances for the doublet (quartet) state are given in Å.

![](./images/811757253387354112_2.jpg)

Fig. 2 B3LYP/B1 optimized structure for the Cpd I-W903 complex and for the transition structures in the presence of W903 (see text). Key distances for the doublet (quartet) state are given in Å.

is normally hydrogen bonded to the oxo atom such that it does not interfere with the substrate (see Fig. 2), except in the case of N,N-dimethylaniline 9 (see further discus- sion below). The optimised distances in the $O\cdots H\cdots C$ moiety indicate that the tran sition state in the doublet always occurs somewhat earlier along the reaction coordinate than that in the quartet. Comparing the systems without and with W903, the transition state is always earlier in the latter case: in the presence of W903, the optimised $C\cdots H$ distance is shorter, typically by 0.03-0.08 (0.02-0.06) Å in the doublet (quartet), while the optimised $O\cdots H$ distance is longer, typically by 0.05-0.10 (0.02-0.06) Å in the doublet (quartet).

Table 1 lists the computed B3LYP/B1 barriers for hydrogen abstraction by the chosen Cpd I model, both in the doublet (D) and quartet (Q) spin state. The barriers in the water-free systems correspond to the differences in the energies of the transition state and the separated reactants. The barriers in the systems with W903 are obtained as the difference between the energy of the transition state and the sum of the energies of the substrate and the Cpd I-W903 complex. The energies of all species involved (see ESI,† Tables S1–S14) are evaluated at their optimised B3LYP/B1 geometries. The quoted barriers do not include any zero-point vibrational energy corrections nor any other corrections.

It should be noted that the substrates may initially form reactant complexes with Cpd I (or Cpd I–W903). The existence of such a reactant complex is the reason for the negative barrier obtained for dimethylaniline (D, with W903, see Table 1): in this case, the transition state lies above the reactant complex, but below the dissociation limit (with N,N-dimethylaniline at infinite distance). In the following, we disregard such reactant complexes.

The barriers computed in the absence of W903 cover a large range between 6 and 22 kcal mol⁻¹. For a given substrate, the values for the doublet and quartet state are usually quite close to each other, typically within 1 kcal mol⁻¹, with the barrier being normally lower in the doublet state. The strong substrate dependence of the barrier to hydrogen abstraction has been examined previously, and it has been shown that

<table>
<caption>Table 1 B3LYP/B1 barriers (kcal mol⁻¹) for hydrogen abstraction from substrates 1–9 by a Compound I model system in the gas phase<sup>a</sup></caption>
<thead>
<tr>
<th rowspan="2">Substrate</th>
<th rowspan="2">Label<sup>b</sup></th>
<th rowspan="2">Spin<sup>c</sup></th>
<th colspan="3">B3LYP/B1 barrier</th>
</tr>
<tr>
<th>Without W903</th>
<th>With W903</th>
<th>Difference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ethane</td>
<td>1</td>
<td>D</td>
<td>20.32</td>
<td>18.13</td>
<td>2.19</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>21.28</td>
<td>18.71</td>
<td>2.57</td>
</tr>
<tr>
<td>Propane</td>
<td>2n</td>
<td>D</td>
<td>20.47</td>
<td>19.06</td>
<td>1.41</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>21.62</td>
<td>20.33</td>
<td>1.29</td>
</tr>
<tr>
<td>Propane</td>
<td>2i</td>
<td>D</td>
<td>18.02</td>
<td>16.61</td>
<td>1.41</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>19.26</td>
<td>16.63</td>
<td>2.63</td>
</tr>
<tr>
<td>Phenylethane</td>
<td>3n</td>
<td>D</td>
<td>19.96</td>
<td>17.70</td>
<td>2.26</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>21.16</td>
<td>18.30</td>
<td>2.86</td>
</tr>
<tr>
<td>Phenylethane</td>
<td>3b</td>
<td>D</td>
<td>14.30</td>
<td>10.53</td>
<td>3.77</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>14.57</td>
<td>10.81</td>
<td>3.76</td>
</tr>
<tr>
<td>Me-Probe</td>
<td>4</td>
<td>D</td>
<td>17.43</td>
<td>14.85</td>
<td>2.58</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>18.46</td>
<td>14.20</td>
<td>4.26</td>
</tr>
<tr>
<td>Camphor</td>
<td>5</td>
<td>D</td>
<td>17.08</td>
<td>13.63</td>
<td>3.45</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>18.08</td>
<td>14.78</td>
<td>3.30</td>
</tr>
<tr>
<td>Propene</td>
<td>6</td>
<td>D</td>
<td>15.01</td>
<td>13.60</td>
<td>1.37</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>15.33</td>
<td>13.21</td>
<td>1.80</td>
</tr>
<tr>
<td>Toluene</td>
<td>7</td>
<td>D</td>
<td>15.78</td>
<td>12.66</td>
<td>2.67</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>15.15</td>
<td>12.05</td>
<td>3.01</td>
</tr>
<tr>
<td>iPr-Probe</td>
<td>8</td>
<td>D</td>
<td>13.68</td>
<td>13.39</td>
<td>0.29</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>14.33</td>
<td>12.92</td>
<td>1.41</td>
</tr>
<tr>
<td>Dimethylaniline</td>
<td>9</td>
<td>D</td>
<td>6.33</td>
<td>−1.57</td>
<td>7.90</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>7.79</td>
<td>2.27</td>
<td>5.52</td>
</tr>
<tr>
<td>Dimethylaniline</td>
<td>9c</td>
<td>D</td>
<td>6.33</td>
<td>3.38</td>
<td>2.95</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Q</td>
<td>7.79</td>
<td>5.28</td>
<td>2.51</td>
</tr>
</tbody>
</table>

<sup>a</sup> See text for definition of basis B1 and barrier evaluation. <sup>b</sup> 2n (2i): abstraction of primary (secondary) hydrogen atom in propane; 3n (3b): abstraction of methyl (benzyl) hydrogen atom in phenylethane; 9c: W903 constrained to be *trans* to substrate. <sup>c</sup> D doublet, Q quartet.

the bond dissociation energy (BDE) of the breaking CH bond is the decisive factor that governs the barrier. $^{1,2,23}$ Good correlations are available between computed BDEs and barriers which allow fast reactivity predictions for substrates. $^{24,25}$ Hence there is no need for further analysis of these data.

For a given substrate, the barriers computed in the presence of W903 are generally somewhat lower than those computed without W903. The B3LYP/B1 barrier lower- ings for substrates 1-8 range between 0.3 and $4.3 kcal mol^{-1}$ , while those for N,N dimethylaniline 9 are significantly larger $(5.5-7.9 kcal mol^{-1})$ . The reason is obvious when looking at the optimised TS structures (see Fig. 2): 9 is the only substrate engaged in direct interactions with W903 which can provide additional TS stabiliza- tion. To assess the magnitude of this side effect, we have performed a constrained TS optimization, with the W903 oxygen atom in trans-position to the aniline nitrogen atom, to enforce a non-interfering arrangement of W903: the resulting barrier lower- ings of $3.0(2.5) kcal mol^{-1}$ for the doublet (quartet) of $9 c$ now lie in the usual range(Table 1). Whether the extra TS stabilization afforded by W903 in the unconstrained gas-phase optimization (9 vs. 9c) is a real effect in the enzymatic environment remains an open question at this point. This could be resolved by a QM/MM study which is, however, beyond the scope of this article. Preliminary docking tests suggest that TS structure 9 (Fig. 2) might actually fit into the active site of P450 BM3.

The B3LYP/B1 gas-phase data presented so far show that W903 indeed acts as a catalyst for hydrogen abstraction by Cpd I in all cases (substrates 1-9, both doublet and quartet). The barrier lowerings are moderate, typically of the order of $2-4 kcal mol^{-1}$ , and the optimised TS structures indicate earlier transition states in the presence of W903 that are consistent with the smaller barriers. Applying the same type of classical electrostatic modelling as in our previous work on cytochrome P450cam, $^{5,6}$ we have confirmed that the calculated barrier lowering is of electrostatic origin in all cases (for detailed numerical data see ESI, $\dagger$ Tables S44 and S45). In qualitative terms, the hydrogen bond between W903 and the oxo atom of Cpd I is stronger in the transition state than in the reactant because of the increase of the negative charge at the oxo atom. This suggests that the amount of barrier lowering might be correlated with the donor strength of the substrate or with the amount of charge transfer in the transition state. We have attempted several such correlations, but without much success. There is practically no correlation between the computed(B3LYP/B1) barrier lowerings and ionisation potentials. The calculated net charges of the substrate in the transition state (as a measure of charge transfer) correlate reasonably well at first sight with the barrier lowerings for substrates 1-9. However,closer inspection shows that these net charges are generally around $0.30-0.35 e$ for $1-$ 8 and around $0.50 e$ for 9 and $9 c$ so that the correlation coefficient crucially depends on the barrier lowering for N,N-dimethylaniline (9 or 9c). As discussed above, this value is quite different in unconstrained (9) and constrained (9c) optimisations in spite of the fact that the charge transfer is essentially the same in both cases. Hence, the seemingly good correlation obtained with the data for $9$ cannot be regarded as trustworthy (for detailed data and correlation plots see ESI, $\dagger$ Tables S50-S51 and Figures S23-S24).

We now address basis set issues. We have carried out single-point B3LYP calcu- lations at the B3LYP/B1 geometries using three larger basis sets (B2W, B3, and B4, see section 2). The corresponding results are documented in the ESI $\dagger$ (Tables S16- S37). The barrier lowerings obtained with these three sets tend to be smaller than the B3LYP/B1 values and are generally similar to each other. Therefore we have per- formed additional geometry optimisations only at the B3LYP/B4 level for four representative substrates (i.e., 1, 4, 5, and 9). The B3LYP/B4 optimised geometries are given in the ESI $\dagger$ (see Figures S17-S21 and Tables S48 and S49), while the cor responding barriers are listed in Table 2. The catalytic effect of W903 is also apparent from the B3LYP/B4 results, with earlier TS geometries and smaller barriersin the presence of W903. The trends are qualitatively the same as at the B3LYP/B1 level, but less pronounced overall. The B3LYP/B4 barrier reductions amount to

<table>
<thead>
<tr><th colspan="3">Table 2 B3LYP/B4 barriers (kcal mol⁻¹) for hydrogen abstraction from substrates 1, 4, 5 and 9 by a Compound I model system in the gas phaseⁿ</th><th colspan="3">B3LYP/B4 barrier</th></tr>
<tr><th>Substrate</th><th>Label</th><th>Spinᵇ</th><th>Without W903</th><th>With W903</th><th>Difference</th></tr>
</thead>
<tbody>
<tr><td>Ethane</td><td>1</td><td>D</td><td>19.49</td><td>18.10</td><td>1.39</td></tr>
<tr><td></td><td></td><td>Q</td><td>21.67</td><td>20.02</td><td>1.67</td></tr>
<tr><td>Me-Probe</td><td>4</td><td>D</td><td>16.99</td><td>15.06</td><td>1.93</td></tr>
<tr><td></td><td></td><td>Q</td><td>19.15</td><td>16.83</td><td>2.32</td></tr>
<tr><td>Camphor</td><td>5</td><td>D</td><td>16.45</td><td>14.22</td><td>2.23</td></tr>
<tr><td></td><td></td><td>Q</td><td>18.71</td><td>16.32</td><td>2.39</td></tr>
<tr><td>Dimethylaniline</td><td>9</td><td>D</td><td>6.79</td><td>0.51</td><td>6.28</td></tr>
<tr><td></td><td></td><td>Q</td><td>8.77</td><td>5.22</td><td>3.55</td></tr>
</tbody>
<tfoot>
<tr><td colspan="6">ⁿ See text for definition of basis B4 and barrier evaluation. ᵇ D doublet, Q quartet.</td></tr>
</tfoot>
</table>

typically 60–70% of the corresponding B3LYP/B1 values for these substrates (see Tables 1 and 2).

In the case of camphor 5, additional data on the basis set dependence are available from our previous QM/MM work on the quartet state.⁵·⁶ The reported barrier lowerings (QM = B3LYP/B1, MM = CHARMM) are around 4 kcal mol⁻¹, with slight variations depending on the chosen snapshot and the protonation state of Asp297. Using QM region R1'⁶ which is equivalent to our current QM model system, QM/MM optimisations yield barrier lowerings of 4.4 and 3.7 kcal mol⁻¹ for basis sets B1 and B2W, respectively. Gas-phase single-point B3LYP/B1 calculations at QM/MM optimised geometries of R1' lead to a somewhat smaller value of 3.0 kcal mol⁻¹,⁶ which is reasonably close to the current result of 3.3 kcal mol⁻¹ at re-optimised QM geometries (see Table 1). Judging from these data, the catalytic effect of W903 on the hydrogen abstraction barrier appears to be somewhat larger in the enzyme than in the gas phase. This is related to the electronic character of the transition state:¹·² the Fe(ɪᴠ) electromer that is favored in the gas phase is expected to be less polarisable than the Fe(ɪɪɪ) electromer predominant in the enzyme, which suggests that it should be somewhat less susceptible to the influence of W903. In any event, the basic mechanism of differential electrostatic TS stabilisation by hydrogen bonding to W903 will operate in both cases.

In summary, the present QM model study shows that a single water molecule (W903) indeed acts as a general biocatalyst for hydrogen abstraction by Cpd I, in the doublet and the quartet state of each of the substrates considered (1–9). According to the B3LYP/B1 results, the barriers are reduced typically by 2–4 kcal mol⁻¹ in the presence of W903. This catalytic effect tends to be diminished when using larger QM basis sets, but should be enhanced when going from the gas phase into the protein environment (see above). Due to these counteracting trends, the computed B3LYP/B1 barrier lowerings may well be realistic estimates for the situation in the enzyme.

## 4. Brief survey of the role of water in P450 chemistry

One might suspect that the discussed biocatalytic effect of water during hydrogen abstraction by Cpd I is something odd or unusual. To put this into perspective, we briefly comment on other examples in P450 chemistry where an individual water molecule makes the difference.

Water is directly involved in several steps of the catalytic cycle in cytochrome P450cam (Fig. 3).¹·² In the resting state (S1), one water molecule serves as an axial

ligand. Upon entry of the substrate, it is replaced along with other water molecules that are present in the binding pocket. This replacement gates the catalytic cycle because the redox potential of the resulting pentacoordinate intermediate (S2) is such that it can be reduced (unlike the resting state) by the nearby reductase enzyme. After oxygen uptake and another reduction step, the formed ferric peroxo species (S5) is protonated to yield the hydroperoxo intermediate (S6, Cpd 0). According to QM/MM calculations,²⁶ the proton delivery is very facile in the wild-type enzyme, because of the presence of a hydrogen-bond network in the Asp251 channel (from protonated Asp251 *via* crystallographic water W901 and Thr252 to the FeOO

![](./images/811757253387354112_3.jpg)

Fig. 3 Catalytic cycle of cytochrome P450cam.

moiety). In the D251N mutant, the Asn251 side chain flips into a different confor- mation (thus disrupting the hydrogen-bond network and the proton-transfer pathway), and the entry of an additional water molecule into the active site of D251N is needed to regenerate the network and to enable proton delivery in the mutant. $^{26}$ Protonation of the distal oxygen atom in Cpd 0 produces water and Cpd I (S7) in wild-type P450cam, again by proton transfer in the Asp251 channel after initial O-O cleavage. $^{7}$ The alternative protonation at the proximal oxygen atom in Cpd 0 leads to the formation of hydrogen peroxide and the pentacoordi- nated ferric intermediate (S2) (uncoupling, see Fig. 3). This unproductive side reac- tion is not observed in wild-type P450cam, but is the only reaction seen in the Thr252Ala and Thr252Gly mutants. This experimental finding has been rationalized in a QM/MM study by showing for these mutants that the entry of an additional water molecule in the Asp251 channel generates an ideal hydrogen-bond networkfor uncoupling and makes this reaction more favorable than Cpd I formation. $^{27}$  This extra water molecule is not present in wild-type P450cam for steric reasons, since threonine is larger than alanine or glycine. The protonation of Cpd 0 in the wild-type and the mutant enzymes is thus an example where the presence of a single water molecule can tip the balance between two competing pathways. $^{27}$ The nextstep in the catalytic cycle of P450cam is substrate hydroxylation $(S 7 \to S 8 \to S 9)$  which is catalysed by W903 both in the quartet $^{5,6}$ and the doublet $^{28}$ state; we have shown in this article that the catalytic effect of W903 is general and also applies to other substrates (see section 3). The catalytic cycle of P450cam is closed by the release of the product alcohol and re-entry of water into the binding pocket to regen- erate the resting state (S1).

It is obvious from this brief survey that individual water molecules play a crucial mechanistic role in cytochrome P450cam and its mutants. This is also true in other P450-mediated reactions. $^{1,2}$ To quote just one striking example, P450 StaP(CYP245A1) catalyses the formation of staurosporine from chromopyrrolic acid by an intricate mechanism that has been unravelled through DFT(B3LYP)/MM calculations. $^{29}$ Three of the ten elementary steps involve the relocation of individual water molecules that make the subsequent hydrogen shifts feasible. These water molecules have therefore been called the "working bees" of this mechanism. They act as biocatalysts that enable a very complex transformation.

## 5. Methodological considerations

Having shown that individual water molecules can make a difference in enzymatic reaction mechanisms, it is of obvious importance not to miss them in theoretical investigations, for example, in QM/MM calculations. Concerning the present case study, the catalytic effect of W903 on hydrogen abstraction in P450cam had not been recognised in our early QM/MM work, $^{30}$ simply because W903 had moved away from its initial position near the iron-oxo moiety during the classical molecular dynamics (MD) simulations performed as part of the usual QM/MM setup proce- dure. The catalytic effect became obvious only in systematic later work $^{5,6}$ where the starting geometries for QM/MM optimisation included arrangements with W903 hydrogen bonded to the oxo atom.

This experience motivated a thorough study of the influence of the chosen QM/ MM setup procedures on the QM/MM results for P450cam. $^{31}$ In particular, different geometry-based hydration procedures were tested, the resulting setups were sub- jected to classical MD runs to check their feasibility, and twelve of the thus preparedsystems were optimised at the QM/MM level to assess the dependence of the QM/ MM results on the degree of hydration. Without going too much into details, $^{31}$ it was found that saturating the protein interior with water on purely geometry-based criteria is detrimental and leads to high structural flexibility and catalytically ineffi- cient active-site geometries. Classical MD simulations were confirmed to be useful tools for selecting starting geometries with reasonable water content. The

QM/MM results for the preferred hydration schemes thus obtained turned out to be rather similar, indicating that slight differences in the solvation close to the active site are not critical as long as the substrate and the crystallographic water molecules preserve their positions from the experimental X-ray structure. $^{31}$

During the QM/MM setup phase, it may also be advisable to apply more sophisticated methods such as free-energy calculations, in order to determine whether water is present in a protein cavity that is large enough, but is not occupied by a crystallographic water molecule. It may, of course, be thermodynamically more favorable for a hydrophobic cavity to be empty rather than filled with water, $^{32}$ but on the other hand, it is also possible that a mobile water molecule is present, but not detected by X-ray analysis. In practice, one may not be able to decide this issue unambiguously. If one expects such a putative water molecule close to the active site to be relevant mechanistically, it is inevitable in QM/MM optimisation work to perform the calculations with and without this molecule in order to explore all likely possibilities. $^{26-31}$

Part of the QM/MM setup is the partitioning of the system into the QM and MM regions. The safe choice is to include any mechanistically important species into the QM region, of course. For the sake of analysis, it can be worthwhile, however, to consider alternative partitionings. Concerning the current case study, separate QM/MM calculations on camphor hydroxylation by Cpd I have been done with W903 included either in the QM region or in the MM region. $^{5,6}$ W903 was found to act as a catalyst in both cases, with comparable barrier lowerings, thus indicating the electrostatic origin of the catalysis (that is also captured when treating W903 at the MM level).

### Acknowledgements
The research at the Hebrew University is supported in part by an Israeli-Science Foundation (ISF) grant (10/06) and the Ministry of Education and Research within the framework of the German-Israeli Project Cooperation (DIP-G7.1).

### References
1 S. Shaik, D. Kumar, S. P. de Visser, A. Altun and W. Thiel, *Chem. Rev.*, 2005, **105**, 2279.
2 S. Shaik, S. Cohen, Y. Wang, H. Chen, D. Kumar and W. Thiel, *Chem. Rev.*, 2010, **110**, 949.
3 H. M. Senn and W. Thiel, *Top. Curr. Chem.*, 2007, **268**, 173.
4 H. M. Senn and W. Thiel, *Angew. Chem., Int. Ed.*, 2009, **48**, 1198.
5 A. Altun, V. Guallar, R. A. Friesner, S. Shaik and W. Thiel, *J. Am. Chem. Soc.*, 2006, **128**, 3924.
6 A. Altun, S. Shaik and W. Thiel, *J. Comput. Chem.*, 2006, **27**, 1324.
7 J. Zheng, D. Wang, W. Thiel and S. Shaik, *J. Am. Chem. Soc.*, 2006, **128**, 13204.
8 A. D. Becke, *J. Chem. Phys.*, 1988, **38**, 3098.
9 C. Lee, W. Yang and R. G. Parr, *Phys. Rev. B: Condens. Matter*, 1988, **37**, 785.
10 A. D. Becke, *J. Chem. Phys.*, 1993, **98**, 5648.
11 R. Ahlrichs, M. Bär, M. Häser, H. Horn and C. Kölmel, *Chem. Phys. Lett.*, 1989, **162**, 165.
12 J. P. Hay and W. R. Wadt, *J. Chem. Phys.*, 1985, **82**, 299.
13 W. J. Hehre, L. Radom, P. v. R. Schleyer and J. A. Pople, *Ab Initio Molecular Orbital Theory*, John Wiley & Sons, New York, 1986.
14 A. J. H. Wachters, *J. Chem. Phys.*, 1970, **52**, 1033.
15 P. J. Hay, *J. Chem. Phys.*, 1977, **66**, 4377.
16 C. W. Bauschlicher, Jr., S. R. Langhoff and L. A. Barnes, *J. Chem. Phys.*, 1989, **91**, 2399.
17 A. Schäfer, H. Horn and R. Ahlrichs, *J. Chem. Phys.*, 1992, **97**, 2571.
18 A. Schäfer, C. Huber and R. Ahlrichs, *J. Chem. Phys.*, 1994, **100**, 5829.
19 E. Sigfridsson and U. Ryde, *J. Biol. Inorg. Chem.*, 1999, **4**, 99.
20 K. P. Jensen and U. Ryde, *J. Biol. Chem.*, 2004, **279**, 14561.
21 S. R. Billeter, A. J. Turner and W. Thiel, *Phys. Chem. Chem. Phys.*, 2000, **2**, 2177.
22 P. Sherwood, H. de Vries, M. F. Guest, G. Schreckenbach, C. R. A. Catlow, S. A. French, A. A. Sokol, S. T. Bromley, W. Thiel, J. Turner, S. Billeter, F. Terstegen,

---
382 | *Faraday Discuss.*, 2011, **148**, 373-383
This journal is © The Royal Society of Chemistry 2011

S. Thiel, J. Kendrick, S. C. Rogers, J. Casci, M. Watson, F. King, E. Karlsen, M. Sjørdle,
A. Fahmi, A. Schäfer and C. Lennartz, THEOCHEM, 2003, 632, 1.

23 See section 4.7 in Ref. 1 and section 5.1 in Ref. 2.

24 S. P. de Visser, D. Kumar, S. Cohen, R. Shacham and S. Shaik, J. Am. Chem. Soc., 2004, 126, 8362.

25 L. Olsen, P. Rydberg, T. H. Rod and U. Ryde, J. Med. Chem., 2006, 49, 6489.

26 D. Wang, J. Zheng, S. Shaik and W. Thiel, J. Phys. Chem. B, 2008, 112, 5126.

27 M. Altarsha, T. Benighaus, D. Kumar and W. Thiel, J. Am. Chem. Soc., 2009, 131, 4755.

28 A. Altun, S. Shaik and W. Thiel, J. Am. Chem. Soc., 2007, 129, 8978.

29 Y. Wang, H. Chen, M. Makino, S. Shiro, S. Nagano, H. Onaka and S. Shaik, J. Am. Chem. Soc., 2009, 131, 6748.

30 J. C. Schöneboom, S. Cohen, H. Lin, S. Shaik and W. Thiel, J. Am. Chem. Soc., 2004, 126, 4017.

31 J. Zheng, A. Altun and W. Thiel, J. Comput. Chem., 2007, 28, 2147.

32 V. Helms and R. C. Wade, Biophys. J., 1995, 69, 810.

---

This journal is © The Royal Society of Chemistry 2011
Faraday Discuss., 2011, 148, 373–383 | 383