# Assembly of cyclic hydrocarbons from ethene and propene in acid zeolite catalysis to produce active catalytic sites for MTO conversion

Matthias Vandichel, David Lesthaeghe, Jeroen Van der Mynsbrugge, Michel Waroquier, Veronique Van Speybroeck*

Center for Molecular Modeling, QCMM Alliance Ghent – Brussels, Ghent University, Technologiepark 903, 9052 Zwijnaarde, Belgium

---

## ARTICLE INFO

**Article history:**
Received 29 October 2009
Revised 13 January 2010
Accepted 1 February 2010
Available online 15 March 2010

**Keywords:**
Cyclization
Oligomerization
Molecular modeling
DFT-D
MTO
Methanol to olefins
ZSM-5
Zeolite
Chemical kinetics
Dispersion interactions

---

## ABSTRACT

The formation of cyclic hydrocarbons from smaller building blocks such as ethene and propene is investigated in protonated ZSM-5, using a 2-layered ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d)) approach and an additional Grimme-type van der Waals dispersion correction term to account for the long-range dispersion interactions. These cyclic species form precursors for active hydrocarbon pool species and play a key role in activating the acidic zeolite host for successful methanol-to-olefin (MTO) conversion. Starting from trace amounts of ethene and propene that are formed during an initial induction period or during the active phase, dimerization reactions allow for rapid chain growth. The products of these reactions can be neutral alkenes, framework-bound alkoxide species or intermediate carbenium ions, depending on the zeolite environment taken into account. On the basis of rate constants for successive reaction steps, a viable route toward cyclization is proposed, which starts from the formation of a framework-bound propoxide from propene, followed by dimerization with an additional propene molecule to form the 2-hexyl carbenium ion which finally undergoes ring closure to yield methylcyclopentane. This cyclic species in turn forms a precursor for either an active hydrocarbon pool compound or for deactivating coke deposit.

© 2010 Elsevier Inc. All rights reserved.

---

## 1. Introduction

In this study, the formation of hydrocarbon pool compounds for methanol-to-olefin conversion (MTO) in acid zeolites [1] is taken as a practical example for the creation of bulky organic compounds trapped in a confined space. For over 30 years, there has been an ongoing dispute on the true nature of the reaction mechanism in MTO catalysis by both experimental and theoretical researchers [2–4]. Only recently, consensus has been achieved on an indirect olefin-producing cycle over direct coupling of C1 entities (like methanol or dimethylether) [5–7]. In this alternative "hydrocarbon pool" (HP) model, the active site of a typical MTO catalyst is composed of a nm-sized inorganic channel or cage with a Bronsted acid proton, containing an essential organic compound, all interacting to form a supramolecular catalyst [8]. In a typical catalytic cycle, the HP species undergoes successive methylation steps by methanol and/or dimethyl ether and subsequently eliminates light olefins like ethene and propene [9–11].

The most often observed hydrocarbon pool species to date have been typically polymethylbenzenes, though linear alkenes might also function as active organic species during the MTO cycle [12]. Various related cyclic cationic intermediates have also been identified by in situ NMR spectroscopy during MTO conversion [13–15].

It remains unclear when and how these cocatalytic hydrocarbon pool compounds are formed either (i) from impurities in the initial methanol feed, e.g., ethanol, propanol or isopropanol, or rather (ii) through the incomplete calcination of templating agents, or, once full conversion has started, even (iii) from primary MTO products like ethene and propene [11]. Fig. 1 shows compressed two-dimensional views of a catalyst particle (CHA-topology) during its lifetime [8]. The catalyst bed initially shows no activity because no cages contain any HP species. During the kinetic induction period, sufficient methylbenzenes are formed to generate an active MTO catalyst, resulting in primary formation of ethene and propene. This paper, however, will focus on the creation of secondary hydrocarbon pool compounds from these trace amounts of ethene and propene that were already generated in the preceding stage. During the active phase, a large number of HP species are present due to such secondary formation routes of cyclic intermediates. As time progresses, these species evolve into bicyclic species, which are less active toward olefin formation [16]. Finally, at the end of the catalyst lifetime, mass transport is severely restricted when as much as half of the cages contain polycyclic aromatic compounds. While the reactions studied in this paper are mainly

---

* Corresponding author. Fax: +32 9 264 66 97.
E-mail address: Veronique.VanSpeybroeck@UGent.be (V. Van Speybroeck).

0021-9517/$ - see front matter © 2010 Elsevier Inc. All rights reserved.
doi:10.1016/j.jcat.2010.02.001

![](./images/811800637799923712_1.jpg)

Fig. 1. Two-dimensional views of a catalyst particle during its lifetime [8].

targeted at generating active sites, they are ultimately also relevant for the process of deactivation.

Polymethylbenzenes (PMBs) have been commonly regarded as the most important hydrocarbon pool species, independent of the employed zeolite, though experimental evidence was mainly found in zeolites H-beta [14,17,18] and H-SAPO-34 [19,20]. In H- ZSM-5, however, recent experiments have led to the proposal of a dual cycle mechanism, in which the polymethylbenzene cycle competes with a parallel alkene cycle [12,21]: lower methylbenzenes favor the formation of ethene, while the alkene cycle, consisting of successive methylation and cracking reactions, looks more appropriate for yielding propene and higher alkenes. The role of alkenes such as propene can be twofold: various methylation and dimerization reactions can lead to the formation of secondary cyclic HP species but also to the formation of higher alkenes, which can further be cracked into the main product distribution olefins. Recently a low-energy pathway for the production of the major olefins in ZSM-5 was identified by means of theoretical calculations [22].

In this article, we will focus on the formation of cyclic hydrocarbons from primary ethene and propene molecules [21]. A range of reactions, such as alkoxide formation, oligomerization and cyclization, has been theoretically evaluated. We will deduce how various oligomerization reactions occur and weigh them off against homologation by successive methylation as studied in other work [23]. Since the HP intermediates are often cationic in nature and quite bulky compared with typical zeolite pore dimensions, the stabilizing and steric effects of the zeolite topology must be taken into account in the analysis. We have previously shown that the topology is of utmost importance: some reaction steps become feasible only when the molecular environment is taken into account [24,25]. Taking this into consideration, our results are based on large zeolite clusters which account for the MFI topology of H-ZSM-5.

Another factor that cannot be neglected is the effect of dispersion interactions. Recently, Svelle and coworkers showed that enthalpy barriers for methylation reactions of various olefins in H-ZSM-5 could be calculated with near chemical accuracy [23]. It was shown that dispersion interactions can add up to 20 kJ/mol for energy barriers and to 70 kJ/mol for physisorption energies [23,26], depending on the specific reaction under study. To account for these potentially important long-range effects, we have added an empirical dispersion term to the energies obtained from density functional theory (DFT) calculations. This approach as developed by Grimme and coworkers – often referred to as the DFT-D approach – has been shown to improve accuracy on a variety of systems [27]. All our conclusions will be drawn on reaction barriers as well as on rate coefficients.

Based on the obtained results, we will propose a new low-energy pathway to cyclization which does not assume prior dehydrogenation. While it is obvious that a myriad of reaction cycles could form cyclic intermediates, this study proposes one plausible route

without claiming exclusivity. Basically, this study is a proof of concept for the formation of secondary HP species from already formed olefinic species.

It is important to note that, next to being catalytically active species, these cyclic hydrocarbon pool compounds are also coke precursors. Formation of this species will, therefore, not only provide an active catalyst, but also ultimately deactivate it again [28] (as also illustrated in Fig. 1).

## 2. Methodology

Geometry optimizations were first performed on pentatetrahedral (5T) clusters with the Gaussian 03 package [29] at the B3LYP/6-31+g(d) level of theory [30-32]. Consequently, transition states of 5T cluster results were used as an initial guess for the transition state in the zeolite environment. Starting from transition state geometries, the quasi-IRC approach allowed the product geometries to be acquired [33]. In the quasi-IRC approach, the geometry of the transition state is slightly perturbed in the direction of the reactants and products followed by full geometry optimizations. This procedure ensures that reactants and products are linked by the same correct transition state. An 8T:46T ONIOM method was used on a cluster cut out of the MFI crystallographic structure of ZSM-5 [24,34,35]. The active site was located at the T12 position [36] at the intersection of the straight and sinusoidal channels, which allows bigger molecules to be formed through bulky transition states. The outer hydrogen atoms of the cluster were constrained in space to prevent unphysical deformations due to the neglect of the full molecular environment. All stationary points and transition states were further localized using the ONIOM(B3LYP/6-31+g(d):MNDO) method, in which the high level is composed of an 8T cluster, and the rest of the cluster is treated at the lower level. The true nature of the stationary points was confirmed by a normal mode analysis, which yields only positive frequencies for all minima and only one negative frequency for each transition state. These energies were refined by single-point energy calculations on the stationary points using the ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d)) level of theory. As shown previously by Svelle and coworkers [23] on the methylation of various olefins in H-ZSM-5, dispersion interactions cannot be neglected for the type of reactions under consideration in this paper. A computationally feasible method to introduce these energy contributions is by adding an empirical $-C_6R^{-6}$ correction to the energy obtained from the Density Functional Theory calculations. This is called the DFT-D approach and provides high accuracy in a variety of simulations [27,37]. For some of the methylation reactions studied by Svelle and coworkers [23], our method gives values that are in very good agreement with the periodic calculations using the PBE functional and augmented with the semi-empirical dispersion term.

Using standard notation LOT-E//LOT-G (LOT-E and LOT-G being the electronic levels of theory used for the energetics and geometry optimizations, respectively), all results discussed in this paper are obtained with the method which is denoted as ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d)) - D//ONIOM(B3LYP/6-31+g(d):MNDO) [38,39]. The van der Waals correction in conjunction with the B3LYP functional as developed by Grimme [37] was calculated using the ORCA program [40]. The above scheme is a viable alternative to more computationally expensive periodic calculations, as also demonstrated by other studies [16,23,41].

The 46T clusters are constrained by the outer hydrogen atoms to prevent unphysical deformation of the cluster. We used the PHVA method [42-46] as previously applied for kinetics [16,25]. This procedure is now implemented in an in-house developed software module TAMKIN, which will be released shortly [47]. Rate coefficients $k$ were obtained by using transition state theory (TST) by calculating the partition functions at 673 K. For an estimation of the uncertainties on the pre-exponential factor $A$ and activation energy $E_a$ in a temperature interval from 623 to 723 K, we refer to the Supporting Information.

## 3. Results and discussion

The cyclization of olefin-like species is not straightforward as it involves a variety of reactions that add up to a complex reaction network. Starting from the olefins already formed in the zeolite cages, following reaction families can be distinguished (as schematically shown in Fig. 2):

(i) oligomerization to higher olefins,
(ii) isomerization,
(iii) cracking of higher olefins,
(iv) cyclization and
(v) dehydrogenative aromatization.

In this paper, we will only study (i) chain growth through oligomerization and (iv) cyclization of the formed chain, labeled as reaction classes A and B, respectively, in Fig. 2. The oligomerization reactions studied in this work include the coupling of two C2 species and a variety of couplings between two C3 species.

Several other types of chain growth mechanisms have been already thoroughly investigated: methylation of alkenes by methanol [23,33,48-52] or oligomerization of ethene and propene [53]. Svelle et al. [51] found experimental proof that propene dimerization might dominate over chain growth by successive methylation. The obtained longer alkene can be dehydrogenated, followed by a diene cyclization [54-59] or can form a naphthene by cyclization prior to further dehydrogenation steps to yield catalytically active species [25].

It has been shown both experimentally [60] and theoretically [61,62] that the stable intermediates resulting from olefin chemisorption form covalent bonds with the basic oxygen atoms, leading to the formation of framework-bound alkoxides rather than free carbenium ions, depending on both olefin size and the local geometry of the active site. Therefore, alkoxide formation of ethene and

![](./images/811800637799923712_2.jpg)

Fig. 2. Overview of various reaction classes for alkene conversion in acidic zeolites.

propene will be studied as they are possible intermediate steps for the oligomerization reactions.

### 3.1. Reaction class A: alkoxide formation and oligomerization
Chain growth mainly occurs through dimerization of olefins formed during the primary induction phase [51]. The possible ethene dimerization and propene dimerization reaction steps will be investigated and serve as a general model for other oligomerization reactions. Two different mechanism types should be considered: concerted and stepwise [53]. In the concerted coupling of alkenes, protonation and C–C coupling occur simultaneously, while the stepwise oligomerization proceeds via initial alkoxide formation [63,64] followed by C–C bond formation. Dimerization reactions have been modeled earlier on 4T clusters, but it is still unclear how the surrounding framework affects the reaction kinetics [53]. Cracking reactions, which are in fact the reverse process of dimerization reactions, have also been modeled in gas phase or on small clusters [65–67]. In Fig. 3, a summary of the studied dimerization reactions is shown.

#### 3.1.1. Alkoxide formation (reactions A1, A2 and A3)
In what follows we will give a short overview of what has already been published in literature on alkoxide formation and of what can serve as a guideline for the validation of our results presented in this article.

The interaction of the olefin double bond with the zeolite Brønsted acid site results in the formation of a physisorbed π-complex. The alkoxide formation is considered at a Brønsted acid site associated with the T12 crystallographic position. Moreover, the physisorbed π-complex is located at the oxygen situated right at the intersection of the sinusoidal and straight channel and represents the most accessible site for adsorption in the ZSM-5 lattice. Earlier calculations by Bhan et al. [63] studied the influence of the location of both the framework aluminum and the charge-compensating proton on physisorption and chemisorption of propene. They confirmed that the T12 location used in this work is the most

![](./images/811800637799923712_3.jpg)

Fig. 3. Investigated oligomerization reactions with kinetic coefficients at 673 K and fitted Arrhenius parameters in the temperature interval 623–723 K calculated on a 46T cluster at the ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d)) – D level of theory including van der Waals corrections.

preferable position for the acidic proton. A recent combined experimental and theoretical study by Sklenak and coworkers showed that the actual distribution of aluminum in MFI is not random and is controlled by the actual conditions of the zeolite synthesis procedure [68]. The T12 position imposes the least steric constraints for formation of bulky intermediates and was therefore used in our theoretical calculations.

The mechanism for alkoxide formation has been studied before by a variety of theoretical models. The results are heavily dependent on the theoretical method used and the model size used to model the solid catalyst [61,62,69,70]. The mechanism of alkoxide formation is schematically depicted in Fig. 4: starting from the physisorbed complex, protonation of the olefin through a carbenium-like transition state results in the formation of chemisorbed covalently bonded alkoxide species. Previous theoretical results showed that the stability of the formed alkoxide is primarily determined by the olefin size [61,63], whereas the activation energies for protonation are determined by the order of stability of primary, secondary and tertiary carbenium-like transition states. Stabilization of the transition state is also determined by electrostatic interactions and might also be influenced by dispersion interactions, which have been unaccounted for so far in ZSM-5. Sauer and coworkers found that for the protonation of isobutene, both the dispersion corrections and the entropic contributions are important to decide on the stability of carbenium ions. At temperatures higher than 120 K, the tert-butyl cation was found to be more stable over the chemisorbed species [26,71].

Experimental evidence has been given for the existence of the physisorbed $\pi$-complex and alkoxide by studying the oligomerization reactions of ethene and propene by means of fast FTIR spectroscopy [72]. A downward shift of the O-H stretching frequency was observed of 389 1/cm by interaction of ethene with the Brønsted acidic site at small contact times during which no protonation of the olefin had occurred. Similarly, a downward shift of 11 1/cm for the C$\text{=}$C double bond frequency in ethene was noticed when brought in contact with the acidic site compared with the gas phase spectrum. Our theoretical calculations were able to fairly well reproduce these shifts: predictions of 334 and 10 1/cm were found for the O-H and C$\text{=}$C frequency shifts with respect to the corresponding vibrations in an empty zeolite and a gas phase ethene molecule. The small downward shift of the double bond frequency can be attributed to the reduced density of charge of the carbon-carbon double bond, while the O-H stretch is shifted due to interaction of the acidic proton with the carbon-carbon double bond to form hydrogen-bonded precursor complexes or physisorbed $\pi$-complexes.

The physisorption energies of ethene and propene are given in Table 1. As all physisorbed complexes were found by performing a quasi-IRC calculation from the transition state for protonation, the values for the physisorbed complex derived from the i-propoxide are slightly different than the value derived from 1-propoxide. In all geometries of the physisorbed complexes, the bridging hydroxyl is closer to the primary carbon atom that is going to be protonated than to the carbon atom that will interact with the basic oxygen (see Fig. 4). The physisorbed energies without van der Waals corrections amount to $-28.3$ and $-41.3$ kJ/mol which are in relatively good agreement with the results found by Bhan et al. [63] and Zheng et al. [73]. All of these physisorption energies are, however, too small compared to experimental data due to the neglect of dispersion interactions as will be shown later in this section [74]. The larger value for propene can be attributed to two effects. Firstly, the interaction with the acidic proton is stronger: the distance between the Brønsted acidic proton and the primary carbon atom that is going to be protonated ($\text{C}_\text{a}$ in Fig. 4) amounts to $2.341$ and $2.083$ Å for ethene and propene respectively, whereas the distance between the other carbon atom ($\text{C}_\text{b}$ in Fig. 4) and the acid site is more or less similar for ethene and propene. Secondly, coordination of the methyl group with the basic oxygen next

![](./images/811800637799923712_4.jpg)

Fig. 4. Energy diagram for alkoxide formation.

<table>
<caption>Table 1<br>Electronic energies (in kJ/mol) of various consecutive steps: alkoxide formation, dimerization and cyclization.</caption>
<tbody>
<tr>
<td>Alkoxide formation</td>
<td>$\Delta E^{\ddagger}$</td>
<td>$\Delta E_{r}$</td>
<td>$\Delta E_{\text{phys,1}}$</td>
<td>$\Delta E_{\text{chem,1}}$</td>
</tr>
<tr>
<td colspan="5">Without van der Waals correction</td>
</tr>
<tr>
<td>A1 (ethoxide formation)</td>
<td>56.3</td>
<td>−104.0</td>
<td>−28.3</td>
<td>−132.3</td>
</tr>
<tr>
<td>A2 ($n$-propoxide formation)</td>
<td>75.3</td>
<td>−69.6</td>
<td>−41.3</td>
<td>−110.9</td>
</tr>
<tr>
<td>A3 (i-propoxide formation)</td>
<td>31.3</td>
<td>−81.3</td>
<td>−38.5</td>
<td>−119.8</td>
</tr>
<tr>
<td colspan="5">With van der Waals correction</td>
</tr>
<tr>
<td>A1 (ethoxide formation)</td>
<td>47.3</td>
<td>−120.6</td>
<td>−64.6</td>
<td>−185.2</td>
</tr>
<tr>
<td>A2 ($n$-propoxide formation)</td>
<td>64.4</td>
<td>−86.9</td>
<td>−92.4</td>
<td>−179.4</td>
</tr>
<tr>
<td>A3 (i-propoxide formation)</td>
<td>22.1</td>
<td>−107.9</td>
<td>−88.1</td>
<td>−196.0</td>
</tr>
<tr>
<td>Dimerization (stepwise)</td>
<td>$\Delta E^{\ddagger}$</td>
<td>$\Delta E_{r}$</td>
<td>$\Delta E_{\text{phys,2}}$</td>
<td>
</td>
</tr>
<tr>
<td colspan="5">Without van der Waals correction</td>
</tr>
<tr>
<td>A4 (1-butene formation)</td>
<td>101.1</td>
<td>−32.6</td>
<td>−8.9</td>
<td>
</td>
</tr>
<tr>
<td>A5 (2-hexyl carbenium ion formation)</td>
<td>83.5</td>
<td>17.3</td>
<td>0.6</td>
<td>
</td>
</tr>
<tr>
<td>A6 (4-methyl-1-pentene formation)</td>
<td>94.7</td>
<td>43.1</td>
<td>−58.0</td>
<td>
</td>
</tr>
<tr>
<td colspan="5">With van der Waals correction</td>
</tr>
<tr>
<td>A4 (1-butene formation)</td>
<td>91.7</td>
<td>−30.3</td>
<td>−38.8</td>
<td>
</td>
</tr>
<tr>
<td>A5 (2-hexyl carbenium ion formation)</td>
<td>68.8</td>
<td>2.8</td>
<td>−59.6</td>
<td>
</td>
</tr>
<tr>
<td>A6 (4-methyl-1-pentene formation)</td>
<td>94.3</td>
<td>54.6</td>
<td>−119.4</td>
<td>
</td>
</tr>
<tr>
<td>Dimerization (concerted)</td>
<td>$\Delta E^{\ddagger}$</td>
<td>$\Delta E_{r}$</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="5">Without van der Waals correction</td>
</tr>
<tr>
<td>A7 (2-hexyl carbenium ion formation)</td>
<td>111.1</td>
<td>−5.4</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="5">With van der Waals correction</td>
</tr>
<tr>
<td>A7 (2-hexyl carbenium ion formation)</td>
<td>98.5</td>
<td>−26.8</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Cyclization</td>
<td>$\Delta E^{\ddagger}$</td>
<td>$\Delta E_{r}$</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="5">Without van der Waals correction</td>
</tr>
<tr>
<td>B1 (methylcyclopentene formation)</td>
<td>37.1</td>
<td>−126.5</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>B2</td>
<td>155.6</td>
<td>33.9</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>B3</td>
<td>72.3</td>
<td>3.2</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="5">With van der Waals correction</td>
</tr>
<tr>
<td>B1</td>
<td>29.1</td>
<td>−117.0</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>B2</td>
<td>165.2</td>
<td>111.7</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>B3</td>
<td>70.1</td>
<td>5.4</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

$\Delta E^{\ddagger}$ is the electronic energy difference between transition state and reactants. $\Delta E_{r}$ (reaction energy) is the energy difference between the products and reactants. $\Delta E_{\text{phys}}$ and $\Delta E_{\text{chem}}$ are the physisorption and chemisorption energies without temperature corrections calculated relative to the gas phase olefins and the empty zeolite cluster as defined in Fig. 4. $\Delta E_{\text{phys,2}}$ is the physisorption energy of the second alkene calculated relative to the gas phase olefin and the already formed alkoxide. All energies are calculated at the ONIOM(B3LYP/6-31+g(d);HF/6-31+g(d)) level of theory with and without inclusion of van der Waals corrections.

to the aluminum site results in additional stabilization. Boronat et al. found smaller values ranging from $-8$ to $-16$ kJ/mol in mordenite [61]. This confirms that the physisorption energy critically depends on the zeolite topology. The effect of dispersion interaction is considerable, contributing to an extra stabilization of $-36.2$ and $-51.2$ kJ/mol for ethene and propene, respectively. This gives final physisorption energies of $-64.6$ and $-92.4$ kJ/mol for ethene and propene. Sauer et al. also found dispersion corrections of this order of magnitude for the $\pi$-physisorbed butene complex in ferrierite ($-78$ kJ/mol) [26]. Our results also show that the dispersion interactions are dependent on the size of the hydrocarbon considered [75-78], which was also found by De Moor et al. on basis of QM-Pot(MP2//B3LYP) calculations in faujasite [79].

The reaction barriers without ZPVE corrections for alkoxide formation are also given in Table 1. For the formation of ethoxide, $n$-propoxide and i-propoxide, they amount to 56.3, 75.3 and 31.3 kJ/mol without inclusion of van der Waals corrections. The reaction is concerted: the primary carbon atom (or secondary in case of i-propoxide formation) is protonated by the zeolite, and simultaneously the positive charge on the other carbon atom of the double bond interacts with one of the basic oxygens of the zeolite, resulting in the formation of a covalently bonded alkoxide complex. The reaction barrier is directly related to the ability of this carbon atom to stabilize the positive charge. Hence, the barrier for formation of i-propoxide is smaller than for ethoxide, corresponding with a secondary and primary carbenium ion in the transition state. The effect of van der Waals interactions is quite uniform for all three alkoxide formations, lowering the reaction barriers (without ZPVE) by approximately 10 kJ/mol.

The stability of the finally formed alkoxides is marked by the olefin size, which predicts ethoxide to be more stable than i-propoxide followed by $n$-propoxide. The effect of dispersion interactions on the covalently bonded complex is substantial, yielding corrections from $-16.6$ to $-26.6$ kJ/mol. These results show that the formation of the i-propoxide is kinetically favored over the $n$-propoxide complex under the same reaction conditions. Also, thermodynamically i-propoxide is slightly preferred over $n$-propoxide, which can be deduced from the total chemisorption energies of $-179.4$ and $-196.0$ kJ/mol, respectively.

### 3.1.2. Stepwise dimerization (reactions A4, A5, A6)

Three stepwise dimerization reactions (A4-A6) were considered as shown in Fig. 3: dimerization of ethene and two dimerizations of propene. The latter reaction can start from the $n$-propoxide or i-propoxide. All three reactions require physisorption of a second alkene to the alkoxide. The physisorption energies of this step ($\Delta E_{\text{phys,2}}$) are given in Table 1 with and without van der Waals interactions. As for the physisorption of the first alkene, the values without dispersion interactions are seriously underestimated. For ethene and propene physisorption, van der Waals corrections of around 30 kJ/mol and 60 kJ/mol are found. In the work of Svelle et al. [53], values were found of around 0-5 kJ/mol with DFT schemes and 15-20 kJ/mol at the post-Hartree Fock level but with usage of a small 4T cluster. The geometries of the physisorbed complexes illustrate that various van der Waals contacts are made not only with the basic oxygen atoms next to the aluminum site but also with other framework oxygen atoms.

The various physisorption energies point toward a very stable i-propoxide co-adsorbed with a propene intermediate, from which only slow reactions can be expected.

After physisorption of the second alkene, the next step of the stepwise dimerization is the formation of a new C-C bond. For coupling between ethoxide and ethene, the reaction profile is shown in Fig. 5.

Without inclusion of an extended cluster model for the zeolite framework (but using a small 5T cluster instead), butene was not formed, but proton back donation to the cluster resulted in the formation of methylcyclopropane instead [53]. This cyclopropane species can easily undergo opening by protonation (the activation barrier for this additional reaction turns out to be 85.2 kJ/mol). These results correspond to earlier theoretical findings of Svelle et al. [53] and Frash et al. [65] who also found the cyclopropane intermediates as stable intermediates when small clusters were used. When an extended cluster model is considered, as in Fig. 5b, we did not find this methylcyclopropane intermediate, yet a similar structure did appear along the optimization of the products as corner-protonated methylcyclopropane. However, this is not a stationary point on the potential energy surface, and the proton on the edge undergoes a barrierless shift [80,81], which results in an automatic opening of the ring structure (Fig. 5b and c).

Depending on the method employed, the (protonated) methylcyclopropane might be a stable intermediate, albeit in a shallow potential well. Anderson and Klinowski [82] reported $^{13}$C MAS NMR results, in which there is a weak signal intensity for cyclopropane during the conversion of methanol in gasoline over ZSM-5. Protonated alkylcyclopropane has also been reported earlier in modeling papers on the skeletal isomerization of alkenes [80,83].

From the transition states for dimerization, at least two possible products might be envisaged: a neutral alkene by direct back

![](./images/811800637799923712_5.jpg)

Fig. 5. (a) Visualization of the stepwise ethene dimerization on a 5T cluster; (b) energy diagram of the stepwise ethene dimerization in zeolite environment (Reaction A4); (c) schematic representation of the post-transition state optimization after stepwise coupling of two ethene molecules.

donation of a proton to the zeolite or a butoxide species. We used the quasi-IRC approach to pinpoint the products corresponding to the transition state and found 1-butene as shown in Fig. 5. To compare the stability of the neutral alkene and the alkoxide, we also calculated the energy of 1-butoxide. This covalently bonded complex is 50.8 kJ/mol (not included in Table 1) more stable than the $\pi$-complex if van der Waals interactions are taken into account. Without these dispersive forces, the difference only amounts to 10.2 kJ/mol. These results are in line with the earlier results on alkoxide formation, and the transformation from the $\pi$-complex to a covalently bonded alkoxide complex should occur easily.

Similar reaction profiles were determined for stepwise dimerization of propene, starting either from $n$-propoxide or i-propoxide. The transition states for carbon-carbon bond formation demonstrate in both cases a preference for attack at the unsubstituted end of the olefin, giving rise to formally secondary carbenium ions rather than primary ones (as illustrated in Fig. 6). While calculations without explicit inclusion of the framework resulted in only neutral products [53], this was not the case when extended models for the zeolite structure were considered, which has the potential to stabilize carbenium ions [24]. The two obtained products were, respectively, the 2-hexyl carbenium ion (Reaction A5) and 4-methylpentene (Reaction A6). These results show that nature of the formed products depends on the specific hydrocarbon, the zeolite structure's ability to stabilize various intermediates and the degree at which the structure has been taken into account.

The energy barriers for the stepwise dimerizations are given in Table 1 with and without van der Waals corrections. To rationalize the importance of each of the consecutive steps, the complete potential energy surface has been shown graphically in Fig. 7.

The alkoxide formation steps are relatively fast for both ethene and propene, with formation of the i-propoxide being the fastest. Adsorption of the second alkene produces a very stable intermediate "i-propoxide + propene". The fastest oligomerization route is

![](./images/811800637799923712_6.jpg)

Fig. 6. Visualization of the transition states for propene dimerization. (TS-A5) Stepwise mechanism from a primary propoxide; (TS-A6) stepwise mechanism from a secondary propoxide; (TS-A7) concerted mechanism with a formally primary carbenium ion in the transition state.

![](./images/811800637799923712_7.jpg)

Fig. 7. Energy profiles of the alkoxide formation and subsequent oligomerization reactions of ethene and propene. The energy levels are calculated relative to the gas phase olefins and the empty zeolite cluster, based on electronic energies at the ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d)) level of theory, with (solid line) and without inclusion (dashed line) of van der Waals corrections.

the stepwise dimerization of propene producing the 2-hexylcarbenium ion. However, the oligomerization of ethene to form 1-butene is competitive taking into account alkoxide formation and second physisorption of the alkene. The stepwise oligomerization starting from i-propoxide to form the 4-methyl-1-pentene (A6) is less viable. Although the forward activation energy of 89.6 kJ/mol (see Fig. 3) suggests a rapid transformation at the considered reaction conditions, the backward reaction is much lower activated (36.3 kJ/mol), which shifts the equilibrium toward the i-propoxide. This is evidenced by the equilibrium constants ($K = k_{forward}/$$k_{backward}$) of reactions A5 and A6 which amount to, respectively, $10^{-1}$ and $10^{-4}$. Therefore, further cyclization and oligomerization from the intermediate "i-propoxide + propene" can be excluded.

From a methodological point of view, it is interesting to compare the potential energy surface with and without van der Waals interactions. In general, the activation energies and reaction energies starting from already adsorbed species (so-called intrinsic barriers) are only subject to relatively small changes. The largest influence is found for each physisorption step of a new reaction partner.

Finally, we will also compare chain growth processes via dimerization versus growth through methylation reactions. The

methylation starts from a physisorbed methanol molecule and an alkene. The respective barriers for methylation of ethene and propene with inclusion of van der Waals interactions are found to be 84.0 and 74.7 kJ/mol. It seems that chain growth will occur along both possible pathways, and for definitive conclusions also intermediate physisorption states should be considered.

### 3.1.3. Concerted propene dimerization (reaction A7)
As an alternative for the stepwise oligomerization, a concerted reaction pathway might be possible, during which the protonation of the first alkene and carbon-carbon bond formation occur simultaneously. For propene, there are two possible sites of protonation leading to the formation of a formally primary or secondary carbenium ion in the transition state. The transition state with a secondary carbenium ion, as seen on a 4T cluster [53], evolves into the transition state for stepwise dimerization when the zeolite environment is taken into account. The transition state through a formally primary carbenium ion could be located and is visualized in Fig. 7 (Reaction A7). When applying a quasi-IRC approach to the transition state, the formed product was the 2-hexyl carbenium ion which was also found as a result of the stepwise dimerization. The IRC toward the reactants evolved into a structure for which one propene molecule left the cluster. This is an artifact of our 46T cluster, which could not prevent the diffusion of one propene molecule out of the 46T cluster when applying quasi-IRC toward the reactants. To get better predictions of the forward reaction barrier of the concerted route, we used a slightly larger perturbation of the transition state in order to keep both propene molecules physisorbed inside the cluster.

The rate coefficient for the backward cracking reaction (Reaction A7 in Fig. 3) is two orders of magnitude larger than for the forward reaction. The stepwise dimerization to 2-hexylcarbenium ion (Reaction A5 in Fig. 3) will be preferred over the concerted reaction. Also, the forward reaction rate is even four orders of magnitude larger. In addition, the cracking reactions prefer a stepwise mechanism as well.

![](./images/811800637799923712_8.jpg)

Fig. 8. Cyclization reactions with kinetic coefficients at 673 K.

![](./images/811800637799923712_9.jpg)

Fig. 9. Visualization of the transition states for cyclization in this study. (TS-B1) cyclization of the 2-hexyl carbenium ion; (TS-B2) cyclization from a secondary alkoxide of hexadiene; (TS-B3) cyclization from a primary alkoxide of hexadiene.

In summary, the theoretical results indicate fast cracking steps at 673 K of alkenes (protonated or non-protonated) in the MFI topology of ZSM-5. This result is in agreement with the recent dual cycle proposal for the MTO process, in which $C_{3+}$ alkenes are possible hydrocarbon pool species [21]. For the oligomerization, our results indicate that, like for the ethene dimerization, propene dimerization also preferably proceeds via a stepwise mechanism.

### 3.2. Reaction class B: cyclization

Cyclization of the obtained $C_6$ species yields precursors to methylbenzenes, which have been proven to be active hydrocarbon pool compounds in H-ZSM-5 [12]. The previously studied oligomerization reactions starting from propene show that the 2-hexylcarbenium ion is a likely intermediate. This result allows us to propose a new route to cyclization starting from this carbenium ion and which does not assume any prior dehydrogenation. As schematically proposed by Haw et al., dehydrogenation occurs more easily after cyclization [8]. This would predominantly occur with the assistance of propene and would also explain the formation of alkanes during the MTO process.

Earlier investigations into cyclization [54,55,59] have shown that dienes or trienes might also be precursors for the cyclization reaction. Joshi et al. studied C6, C7 and C8 diene cyclization in H-ZSM-5 theoretically using a hybrid QM/MM approach [57,58]. They found that the barriers for 1,6-cyclization are lower for the larger dienes, as they proceed through a secondary carbenium ion-like transition state, whereas the C6 diene cyclization involves a primary carbenium ion-like transition state. In order to compare cyclization of the 2-hexylcarbenium ion intermediate of this work with the cyclization of the dienes, we have also calculated the cyclization starting from 1,5-hexadiene as suggested in [57] at the level of theory used for all reactions in this paper. The three cyclization reactions considered here are summarized in Fig. 8 (Reactions B1-B3). A visualization of the corresponding transition states is given in Fig. 9.

We first consider cyclization starting from the 2-hexyl carbenium ion, which is a secondary carbenium ion and is formed as a stable product for two different propene dimerization reactions (A5 and A7). A scan along the transition state coordinate was applied to find a direct cyclization route. Fig. 9B1 visualizes this direct 1,5-cyclization transition state. Prior to the transition state, the original 2-hexyl carbenium ion needs to undergo various internal rearrangements to evolve into conformation which is suitable for cyclization. This conformation is slightly less favorable in energy (27 kJ/mol) compared to the linear chain, but under the reaction conditions here these rearrangements are expected to occur easily. During the transition state a proton hops and bonds with one of the basic oxygen atoms on the aluminum tetrahedron and simultaneously the ring closes. The transition state is schematically depicted in Fig. 9. The product after cyclization is a neutral species, i.e., methylcyclopentane. The electronic reaction barriers given in Table 1 and the rate constants shown in Fig. 8 indicate a rapid and irreversible cyclization step. As matter of comparison with the work of Joshi [56,57], we also studied the cyclization of dienes. This reaction starts from a protonated hexadiene which then forms an alkoxide. Cyclization can start from a secondary hexadiene alkoxide (Reaction B2) or from a primary hexadiene alkoxide (Reaction B3). These results show that the 1,6-cyclization starting from a primary alkoxide is strongly favored over the 1,5-cyclization via a secondary alkoxide, which could be expected as secondary alkoxides are more easily formed but are also more stable [84], and thus less reactive for following cyclizations (Fig. 6). All kinetic parameters and reaction barriers show that the newly proposed cyclization starting from the 2-hexyl carbenium ion without prior dehydrogenation is preferred over cyclization of dienes.

### 3.3. Global scheme for formation of cyclic species

Fig. 10 gives an overview of the studied reactions and highlights in red a viable route toward formation of a 5-membered cyclic species, i.e., methylcyclopentane. The route involves following steps: physisorption of a first propene molecule to form a $\pi$-complex,

![](./images/811800637799923712_10.jpg)

Fig. 10. Overview of a viable route toward the formation of cyclic species starting from ethene and propene. The red cycle is the most probable pathway and involves physisorption of propene, formation of $n$-propoxide, additional physisorption of propene, dimerization to form the 2-hexylcarbenium ion and cyclization to methylcyclopentane.

alkoxide formation to form a covalently bonded complex, i.e., the n-propoxide, physisorption of a second propene and dimerization to form the 2-hexylcarbenium ion and finally cyclization toward a neutral methylcyclopentane molecule. For all steps, both forward and backward reaction rates are given at 673 K. The reaction rates are in the same order of magnitude as the ones reported in our full cycle for the production of olefins in ZSM-5 [25]. The alkoxide formation and dimerization are in the same order of magnitude as methylation reactions of aromatic species in the same topology. The ring closure itself is very rapid.

However, to form aromatic hydrocarbons from this 5-membered ring species, we need ring expansion (as studied in [25]) as well as dehydrogenation. Additional research on the dehydrogenation of those cyclic rings might be useful. This step could occur through carbenium ions which provide cracking pathways of larger hydrocarbons at MTO temperatures [80].

Two more hydrogen abstractions lead to the formation of a dimethylcyclopentadienylium ion, a species signaling the end of the induction period in the MTO process in H-ZSM-5 and starting a new working cycle toward olefin protonation [13]. Such cationic 5-membered ring species have already been shown to expand into 6-membered rings [25] and form part of the active methylbenzene hydrocarbon pool cycle. As proposed and described by Haw and Marcus [8], propene could play a crucial role in ring dehydrogenation steps. Moreover, the ultimate clue of the active nature of this species as organic cocatalyst is proven by its occurrence in a recently calculated catalytic cycle in H-ZSM-5 [25].

## 4. Conclusions
The formation of cyclic hydrocarbons from ethene and propene building blocks was investigated in protonated ZSM-5 using a 2-layered ONIOM approach and taking into account dispersive interactions. These cyclic molecules are crucial in the MTO process, as they form precursors for both active cocatalysts and deactivating coke. Once a sufficient number of initial ethene and propene molecules are formed during the induction period, the rapid formation of new hydrocarbon pool species will bring the protonated zeolite to an active working MTO catalyst, during which methanol is converted into ethene and propene, generating even more active centers, up until the catalyst deactivates.

We performed theoretical calculations to describe a preliminary pathway to cyclic species from small alkene molecules like ethene and propene. By taking the zeolite environment into account, the factual role of the methylcyclopropane intermediate in ethene dimerization could be identified. For further growth of the chain, the calculated kinetic coefficients indicate that stepwise propene dimerization occurs faster than ethene dimerization. The ethoxide formation is rapid, but the dimerization proceeds more slowly. Propene dimerization could result in stable charged species like the 2-hexyl carbenium ion, from which a new rapid cyclization route is proposed. Our calculations further demonstrate the importance of the zeolite environment and the importance of dispersion interactions on the stability of specific intermediates on the potential energy surface. It was found that without accounting for the zeolite cage, some intermediates may be identified which are not stable in the MFI topology of H-ZSM-5. The effect of dispersive interactions was most pronounced for each physisorption step where corrections varying between 30 and 60 kJ/mol were noted.

The reactions studied provide a link between both catalytic cycles proposed in the hydrocarbon pool concept, which has been deemed crucial toward product control [12,21]. Future work should be focused on the dehydrogenation step, which ultimately leads to aromatic hydrocarbon pool compounds. This type of reactions will also be of utmost importance for the formation of a second ring, creating naphthalenic coke precursors [8,28,85,86].

## Acknowledgments
This work is supported by the Fund for Scientific Research - Flanders (FWO), the research Board of Ghent University, and BEL-SPO in the frame of IAP 6/27. Computational resources and services used in this work were provided by Ghent University.

## Appendix A. Supplementary data
Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.jcat.2010.02.001.

## References
[1] M. Stocker, Microporous and Mesoporous Materials 29 (1999) 3-48.
[2] J.F. Haw, D.M. Marcus, P.W. Kletnieks, Journal of Catalysis 244 (2006) 130-133.
[3] Y.J. Jiang, W. Wang, V.R.R. Marthala, J. Huang, B. Sulikowski, M. Hunger, Journal of Catalysis 244 (2006) 134-136.
[4] Y.J. Jiang, W. Wang, V.R.R. Marthala, J. Huang, B. Sulikowski, M. Hunger, Journal of Catalysis 238 (2006) 21-27.
[5] D. Lesthaeghe, V. Van Speybroeck, G.B. Marin, M. Waroquier, Angewandte Chemie - International Edition 45 (2006) 1714-1719.
[6] D. Lesthaeghe, V. Van Speybroeck, G.B. Marin, M. Waroquier, Chemical Physics Letters 417 (2006) 309-315.
[7] W.G. Song, D.M. Marcus, H. Fu, J.O. Ehresmann, J.F. Haw, Journal of the American Chemical Society 124 (2002) 3844-3845.
[8] J.F. Haw, D.M. Marcus, Topics in Catalysis 34 (2005) 41-48.
[9] I.M. Dahl, S. Kolboe, Catalysis Letters 20 (1993) 329-336.
[10] R.M. Dessau, Journal of Catalysis 99 (1986) 111-116.
[11] J.F. Haw, W.G. Song, D.M. Marcus, J.B. Nicholas, Accounts of Chemical Research 36 (2003) 317-326.
[12] S. Svelle, F. Joensen, J. Nerlov, U. Olsbye, K.P. Lillerud, S. Kolboe, M. Bjorgen, Journal of the American Chemical Society 128 (2006) 14770-14771.
[13] J.F. Haw, J.B. Nicholas, W.G. Song, F. Deng, Z.K. Wang, T. Xu, C.S. Heneghan, Journal of the American Chemical Society 122 (2000) 4763-4775.
[14] A. Sassi, M.A. Wildman, H.J. Ahn, P. Prasad, J.B. Nicholas, J.F. Haw, Journal of Physical Chemistry B 106 (2002) 2294-2303.
[15] T. Xu, D.H. Barich, P.W. Goguen, W.G. Song, Z.K. Wang, J.B. Nicholas, J.F. Haw, Journal of the American Chemical Society 120 (1998) 4025-4026.
[16] K. Hemelsoet, A. Nollet, M. Vandichel, D. Lesthaeghe, V. Van Speybroeck, M. Waroquier, ChemCatChem 1 (2009) 373-378.
[17] M. Bjorgen, U. Olsbye, D. Petersen, S. Kolboe, Journal of Catalysis 221 (2004) 1-10.
[18] M. Bjorgen, F. Bonino, S. Kolboe, K.P. Lillerud, A. Zecchina, S. Bordiga, Journal of the American Chemical Society 125 (2003) 15863-15868.
[19] B. Arstad, S. Kolboe, Catalysis Letters 71 (2001) 209-212.
[20] W.G. Song, J.F. Haw, J.B. Nicholas, C.S. Heneghan, Journal of the American Chemical Society 122 (2000) 10726-10727.
[21] M. Bjorgen, S. Svelle, F. Joensen, J. Nerlov, S. Kolboe, F. Bonino, L. Palumbo, S. Bordiga, U. Olsbye, Journal of Catalysis 249 (2007) 195-207.
[22] D. Lesthaeghe, J. Van der Mynsbrugge, M. Vandichel, V. Van Speybroeck, M. Waroquier, manuscript in revision.
[23] S. Svelle, C. Tuma, X. Rozanska, T. Kerber, J. Sauer, Journal of the American Chemical Society 131 (2009) 816-825.
[24] D. Lesthaeghe, B. De Sterck, V. Van Speybroeck, G.B. Marin, M. Waroquier, Angewandte Chemie - International Edition 46 (2007) 1311-1314.
[25] D.M. McCann, D. Lesthaeghe, P.W. Kletnieks, D.R. Guenther, M.J. Hayman, V. Van Speybroeck, M. Waroquier, J.F. Haw, Angewandte Chemie - International Edition 47 (2008) 5179-5182.
[26] C. Tuma, J. Sauer, Physical Chemistry Chemical Physics 8 (2006) 3955-3965.
[27] S. Grimme, J. Antony, T. Schwabe, C. Muck-Lichtenfeld, Organic & Biomolecular Chemistry 5 (2007) 741-758.
[28] D. Mores, E. Stavitski, M.H.F. Kox, J. Kornatowski, U. Olsbye, B.M. Weckhuysen, Chemistry A European Journal 14 (2008) 11320-11327.
[29] M.J. Frisch, G.W. Trucks, H.B. Schlegel, G.E. Scuseria, M.A. Robb, J.R. Cheeseman, J.A. Montgomery, Jr., T. Vreven, K.N. Kudin, J.C. Burant, J.M. Millam, S.S. Iyengar, J. Tomasi, V. Barone, B. Mennucci, M. Cossi, G. Scalmani, N. Rega, G.A. Petersson, H. Nakatsuji, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, M. Klene, X. Li, J.E. Knox, H.P. Hratchian, J.B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R.E. Stratmann, O. Yazyev, A.J. Austin, R. Cammi, C. Pomelli, J.W. Ochterski, P.Y. Ayala, K. Morokuma, G.A. Voth, P. Salvador, J.J. Dannenberg, V.G. Zakrzewski, S. Dapprich, A.D. Daniels, M.C. Strain, O. Farkas, D.K. Malick, A.D. Rabuck, K. Raghavachari, J.B. Foresman, J.V. Ortiz, Q. Cui, A.G. Baboul, S. Clifford, J. Cioslowski, B.B. Stefanov, G. Liu, A. Liashenko, P. Piskorz, I. Komaromi, R.L. Martin, D.J. Fox, T. Keith, M.A. Al-Laham, C.Y. Peng, A. Nanayakkara, M. Challacombe, P.M.W. Gill, B. Johnson, W. Chen, M.W. Wong, C. Gonzalez, J.A. Pople, Gaussian 03, Revision E.01, Wallingford CT, 2004.

[30] A.D. Becke, Journal of Chemical Physics 98 (1993) 5648-5652.

[31] D. Lesthaeghe, V. Van Speybroeck, M. Waroquier, Journal of the American Chemical Society 126 (2004) 9162-9163.

[32] S.A. Zygmunt, R.M. Mueller, L.A. Curtiss, L.E. Iton, Journal of Molecular Structure - Theochem 430 (1998) 9-16.

[33] S. Svelle, S. Kolboe, U. Olsbye, O. Swang, Journal of Physical Chemistry B 107 (2003) 5251-5260.

[34] D. Lesthaeghe, G. Delcour, V. Van Speybroeck, G.B. Marin, M. Waroquier, Microporous and Mesoporous Materials 96 (2006) 350-356.

[35] C. Raksakoon, J. Limtrakul, Journal of Molecular Structure - Theochem 631 (2003) 147-156.

[36] H. Vankoningsveld, H. Vanbekkum, J.C. Jansen, Acta Crystallographica Section B - Structural Communications 43 (1987) 127-132.

[37] S. Grimme, Journal of Computational Chemistry 25 (2004) 1463-1473.

[38] J.T. Fermann, T. Moniz, O. Kiowski, T.J. McIntire, S.M. Auerbach, T. Vreven, M.J. Frisch, Journal of Chemical Theory and Computation 1 (2005) 1232-1239.

[39] X. Solans-Monfort, M. Sodupe, V. Branchadell, J. Sauer, R. Orlando, P. Ugliengo, Journal of Physical Chemistry B 109 (2005) 3539-3545.

[40] ORCA 2.6.35ed. <http://www.thch.uni-bonn.de/tc/orca/>.

[41] D. Lesthaeghe, A. Horré, M. Waroquier, G.B. Marin, V. Van Speybroeck, Chemistry - A European Journal 15 (2009) 10803-10808.

[42] A. Ghysels, V. Van Speybroeck, T. Verstraelen, D. Van Neck, M. Waroquier, Journal of Chemical Theory and Computation 4 (2008) 614-625.

[43] A. Ghysels, V. Van Speybroeck, E. Pauwels, D. Van Neck, B.R. Brooks, M. Waroquier, Journal of Chemical Theory and Computation 5 (2009) 1203-1215.

[44] A. Ghysels, V. Van Speybroeck, E. Pauwels, S. Catak, B.R. Brooks, D. Van Neck, M. Waroquier, Journal of Computational Chemistry 31 (2009) 994-1007.

[45] A. Ghysels, D. Van Neck, M. Waroquier, Journal of Chemical Physics 127 (2007) 164108.

[46] A. Ghysels, D. Van Neck, V. Van Speybroeck, T. Verstraelen, M. Waroquier, Journal of Chemical Physics 126 (2007) 224102.

[47] CMM Code 2008-2009. <http://molmod.ugent.be/code/wiki> (accessed 26.10.09).

[48] Z.M. Cui, Q. Liu, Z. Ma, S.W. Bian, W.G. Song, Journal of Catalysis 258 (2008) 83-86.

[49] S. Svelle, B. Arstad, S. Kolboe, O. Swang, Journal of Physical Chemistry B 107 (2003) 9281-9289.

[50] S. Svelle, S. Kolboe, O. Swang, U. Olsbye, Journal of Physical Chemistry B 109 (2005) 12874-12878.

[51] S. Svelle, P.A. Ronning, S. Kolboe, Journal of Catalysis 224 (2004) 115-123.

[52] S. Svelle, P.O. Ronning, U. Olsbye, S. Kolboe, Journal of Catalysis 234 (2005) 385-400.

[53] S. Svelle, S. Kolboe, O. Swang, Journal of Physical Chemistry B 108 (2004) 2953-2962.

[54] D.V. Dass, A.L. Odell, Journal of Catalysis 113 (1988) 259-262.

[55] G. Giannetto, R. Monque, R. Galiasso, Catalysis Reviews - Science and Engineering 36 (1994) 271-304.

[56] Y.V. Joshi, A. Bhan, K.T. Thomson, Journal of Physical Chemistry B 108 (2004) 971-980.

[57] Y.V. Joshi, K.T. Thomson, Journal of Catalysis 230 (2005) 440-463.

[58] Y.V. Joshi, K.T. Thomson, Journal of Physical Chemistry C 112 (2008) 12825-12833.

[59] P. Meriaudeau, C. Naccache, Catalysis Reviews - Science and Engineering 39 (1997) 5-48.

[60] J.F. Haw, B.R. Richardson, I.S. Oshiro, N.D. Lazo, J.A. Speed, Journal of the American Chemical Society 111 (1989) 2052-2058.

[61] M. Boronat, P.M. Viruela, A. Corma, Journal of the American Chemical Society 126 (2004) 3300-3309.

[62] V.B. Kazansky, Accounts of Chemical Research 24 (1991) 379-383.

[63] A. Bhan, Y.V. Joshi, W.N. Delgass, K.T. Thomson, Journal of Physical Chemistry B 107 (2003) 1047-10487.

[64] D. Lesthaeghe, V. Van Speybroeck, G.B. Marin, M. Waroquier, Journal of Physical Chemistry B 109 (2005) 7952-7960.

[65] M.V. Frash, V.B. Kazansky, A.M. Rigby, R.A. van Santen, Journal of Physical Chemistry B 102 (1998) 2232-2238.

[66] Q.B. Li, A.L.L. East, Canadian Journal of Chemistry - Revue Canadienne De Chimie 84 (2006) 1159-1166.

[67] Q.B. Li, K.C. Hunter, A.L.L. East, Journal of Physical Chemistry A 109 (2005) 6223-6231.

[68] S. Sklenak, J. Dedecek, C.B. Li, B. Wichterlova, V. Gabova, M. Sierka, J. Sauer, Angewandte Chemie - International Edition 46 (2007) 7286-7289.

[69] M. Boronat, P. Viruela, A. Corma, Journal of Physical Chemistry A 102 (1998) 982-989.

[70] X. Rozanska, R.A. van Santen, T. Demuth, F. Hutschka, J. Hafner, Journal of Physical Chemistry B 107 (2003) 1309-1315.

[71] C. Tuma, J. Sauer, Angewandte Chemie - International Edition 44 (2005) 4769-4771.

[72] G. Spoto, S. Bordiga, G. Ricchiardi, D. Scarano, A. Zecchina, E. Borello, Journal of the Chemical Society, Faraday Transactions 90 (1994) 2827-2835.

[73] A.M. Zheng, S.B. Liu, F. Deng, Microporous and Mesoporous Materials 121 (2009) 158-165.

[74] P.E. Sinclair, A. de Vries, P. Sherwood, C.R.A. Catlow, R.A. van Santen, Journal of the Chemical Society, Faraday Transactions 94 (1998) 3401-3408.

[75] F. Eder, J.A. Lercher, Zeolites 18 (1997) 75-81.

[76] F. Eder, M. Stockenhuber, J.A. Lercher, Journal of Physical Chemistry B 101 (1997) 5414-5419.

[77] J.F. Denayer, G.V. Baron, J.A. Martens, P.A. Jacobs, Journal of Physical Chemistry B 102 (1998) 3077-3081.

[78] J.F.M. Denayer, G.V. Baron, Adsorption-Journal of the International Adsorption Society 3 (1997) 251-265.

[79] B.A. De Moor, M.F. Reyniers, M. Sierka, J. Sauer, G.B. Marin, Journal of Physical Chemistry C 112 (2008) 11796-11812.

[80] A. Boronat, A. Corma, Applied Catalysis A - General 336 (2008) 2-10.

[81] K.B. Wiberg, S.R. Kass, Journal of the American Chemical Society 107 (1985) 988-995.

[82] M.W. Anderson, J. Klinowski, Journal of the American Chemical Society 112 (1990) 10-16.

[83] T. Demuth, X. Rozanska, L. Benco, J. Hafner, R.A. van Santen, H. Toulhoat, Journal of Catalysis 214 (2003) 68-77.

[84] M. Boronat, C.M. Zicovich-Wilson, P. Viruela, A. Corma, Journal of Physical Chemistry B 105 (2001) 11169-11177.

[85] F. Bleken, M. Bjørgen, L. Palumbo, S. Bordiga, S. Svelle, K.-P. Lillerud, U. Olsbye, Topics in Catalysis 52 (2009) 218-228.

[86] L. Palumbo, F. Bonino, P. Beato, M. Bjorgen, A. Zecchina, S. Bordiga, The Journal of Physical Chemistry C 112 (2008) 9710-9716.