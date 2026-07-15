# Theoretical Models of Eumelanin Protomolecules and their Optical Properties

Sheng Meng and Efthimios Kaxiras

Department of Physics and School of Engineering and Applied Sciences, Harvard University, Cambridge, Massachusetts

ABSTRACT The molecular structure of melanin, one of the most ubiquitous natural pigments in living organisms, is not known and its multifaceted biological role is still debated. We examine structural models for eumelanin protomolecules, based on tetramers consisting of four monomer units (hydroquinone, indolequinone, and its two tautomers), in arrangements that contain an interior porphyrin ring. These models reproduce convincingly many aspects of eumelanin's experimentally observed behavior. In particular, we present a plausible synthetic pathway of the tetramers and their further complexation through interlayer stacking, or through formation of helical superstructures, into eumelanin macromolecules. The unsaturated nature of C-C bonds in indolequinone units and the finite size of protomolecules introduce covalent bond formation between stacked layers. We employ time-dependent density functional theory to calculate the optical absorption spectrum of each molecule along the eumelanin synthesis pathway, which gradually develops into the characteristic broad-band adsorption of melanin pigment due to electron delocalization. These optical spectra may serve as signatures for identifying intermediate structures.

## INTRODUCTION

Melanin is a ubiquitous pigment encountered widely in hair, skin, eye, brain, and the inner ear of the human body, and in animals, plants, and microorganisms. It is usually classified into two main groups, the brown-black eumelanin and the reddish-yellow pheomelanin. Melanin synthesis in the organelle melanosome begins with hydroxylation and oxidation of tyrosine leading to polymerization of indole units (in eumelanin) and benzothiazine derivatives (in pheomelanin) through the Raper-Mason scheme (1). The biological functions of melanin remain controversial (2,3). Several functions have been proposed, the most widely accepted one being the photoprotection of cells from solar ultraviolet radiation (4,5). Other suggested functions include skin and feather coloration and camouflage, thermoregulation, antioxidation, vitamin-D synthesis regulation, drug and metal-ion binding, and conversion of optical energy to electricity and heat (2,3). Melanin has also been implicated in Parkinson's disease (6,7), age-related macular degeneration (8), and malignant melanoma (9), the most aggressive type of skin cancer. But the underlying mechanisms for all these functions have not been adequately described. The lack of detailed knowledge of the structure of melanin, especially at the molecular level, is a factor contributing greatly to the uncertainties related to its functions. Native melanin cannot be crystallized or dissolved in any solvent without disrupting its structure and is therefore difficult to isolate and study (10-12). Alternative types including synthetic melanin, melanin from the ink sack of the cuttlefish *Sepia officinalis*, melanin extracted from hair or uvea employing aggressive treatment with acids or bases and/or enzymatical extraction methods, have been employed as prototypical models (12,13).

Eumelanin is the most prevalent and important form of melanin, and has been the most intensively studied (7,14). Two qualitatively different models, the crossed-linked heteropolymer model (15) and the stacked oligomer model (16,17) have been proposed to account for the observed melanin properties, but neither of them has been firmly verified from experimental data. However, there is increasingly more evidence (18-20) in support of the finite size of melanin constituent particles or protomolecules, presumably composed of melanin oligomers. Eumelanin oligomers comprise 5, 6-dihydroxyindolequinone (DHI, or hydroquinone, denoted in the following as HQ), 5,6-dihydroxyindole 2-carboxylic acid (denoted as DHICA), and their derived redox forms. For instance, indolequinone (denoted as IQ), the redox form of HQ (21), and its tautomers (denoted generically as QIs) including quinone-methide (MQ) and quinone-imine (NQ), are all believed to be essential components of melanin (22-24). These molecular units or monomers serve as the building blocks of eumelanin. How these units are put together to form the oligomers (also referred to as protomolecules) and eventually the pigment structure, has not yet been established, leaving a basic gap in our understanding of its structure.

Recent experiments have revealed new concrete facts related to the structural features of eumelanin, providing important constraints for a structural model. We summarize the important characteristics of eumelanin observed in experiments, which a realistic structural model should be able to reproduce:

1. Melanin isolated from different types of organisms has different DHI/DHICA ratios with DHI being dominant (25); however, pure DHI or DHICA melanin can be synthesized in laboratories (14). For clarity, we will focus on

Submitted August 31, 2007, and accepted for publication October 24, 2007.
Address reprint requests to Efthimios Kaxiras, Tel.: 617-495-7977; E-mail: kaxiras@physics.harvard.edu.
Editor: Steven D. Schwartz.
© 2008 by the Biophysical Society
0006-3495/08/03/2095/11 $2.00

doi: 10.1529/biophysj.107.121087

DHI eumelanin first and discuss related aspects of the DHICA structure later.

2. X-ray diffraction studies (16,17) and many measurements that followed using scanning tunneling microscopy (STM) (18–20) on synthetic melanin and sepia melanin provide important clues about the microscopic structure of melanin. First, protomolecules of very small size (15–20 Å) can be inferred from x-ray data and have been isolated and observed in STM, which were interpreted to be tetramers or pentamers formed by covalently bonded monomers. Second, the protomolecules appear to be stacked in planar arrangements. On the other hand, species of molecular weight ranging from <1000 to >10,000 were obtained by ultrafiltration (12). The connections between the oligomers and these larger species are not known. Although these studies cannot uniquely determine the structure, they impose strict constraints on structural models of eumelanin. Existing atomic-scale models (17,18,26–29) are not able to explain the finite size of the protomolecules. They merely randomly link the monomers to form constructs artificially restricted to tetramers, pentamers, hexamers, and octamers.

3. Since the QIs (MQ or NQ) are present in chemical analysis of the melanin particles (22–24), they can be also components of the melanin protomolecules. However, in isolated form, these tautomeric monomers are less stable and have small to negligible concentration (13% for the methide form and 0.1% for the imine form, relative to IQ, at 300 K) from theoretical analysis (30,31). On the other hand, these tautomers alone cannot constitute melanin protomolecules, as has been shown by experiment (23).

4. Melanin can capture and release metal ions without apparent morphology changes (11,32). This might suggest a structure containing efficient ion-transport channels. The binding of metal ions to melanin reaches a saturation point: a maximum capacity of one ion per 3–4 monomer units has been established for $Fe^{3+}$, $Mg^{2+}$, and $Ca^{2+}$ (32).

5. The most striking characteristic of melanin concerns its optical properties. Melanin has a broad, monotonic absorption spectrum over a large wavelength range, 700–200 nm (1.7–6.2 eV), whose intensity decays exponentially with the incident photon wavelength. This behavior might play a central part in its photoprotection role. However, this is puzzling, as it lacks any of the sharp features typical of all other biomolecules including proteins and nucleic acids. To explain this behavior, a chemical disorder model of eumelanin was recently proposed (33), which hypothesizes that all or certain different kinds of melanin oligomers-monomers, dimers, trimers, etc., may all exist in a real melanin sample.

Recently Kaxiras et al. (34) proposed a new, detailed, structural model for the eumelanin protomolecules, based on the tetramer structure consisting of four basic molecular units (HQ; IQ; and the two tautomers MQ and NQ), in arrangements that contain an inner porphyrin ring. This model provides a natural explanation of the finite size of eumelanin protomolecules and their metal-binding properties. The experimental x-ray diffraction data is also successfully reproduced by the model. Most importantly, the broad-band absorbance of eumelanin is reproduced by superposition of the spectra of all likely tetramer structures in agreement with the chemical disorder model. However, many questions still remain to be answered concerning the actual structure of eumelanin; for instance:

How are the tetramers formed from monomers?
How are the protomolecules connected to form the melanin polymers?
How does the intrinsically featureless UV absorbance of melanin arise from the structure of the polymers?
How do the protomolecules and polymers interact with their environment, and in particular with metal cations?

In this work, we extend these studies to address the above questions by using state-of-the-art, first-principles calculations of the structural, electronic, and optical properties of the protomolecules. In particular, we focus on the structural evolution from monomers to the protomolecule oligomers and the ensuing polymerization into larger units. We present a plausible synthetic pathway for the tetramer molecule, and its further complexation, either through interlayer stacking or through the formation of a long helix, which eventually form the eumelanin macromolecules. We find that unusual interlayer covalent bonds start to form during the complexation of eumelanin oligomers, due to the unsaturated nature of indoquinones and the finite size of the protomolecules. The strength of these bonds depends on the HQ-IQ composition, which might be used to tailor melanin structure to specific needs. Moreover, our calculations show that the melanin molecules gradually develop a broadband absorption in the process of in-plane bonding, interlayer stacking, helix formation, interlayer covalent bonding, and metal binding. The underlying mechanism is the electronic delocalization and band mixture. The calculated properties of these structures are in good agreement with available experimental data, and provide fresh insight into the variety of special properties of the melanin pigment.

## METHODS

The first-principles calculations were carried out with the SIESTA code (35) in the framework of density functional theory (DFT). We used pseudopotentials of the Troullier-Martins type (36), the local density approximation (LDA) or the PBE version of the gradient approximation for the exchange-correlation functional (37), and a basis of double-$\zeta$ polarized orbitals (13 atomic orbitals for C, N, and O; 5 orbitals for H). We will quote LDA results unless otherwise specified. For the optical absorbance calculations within time-dependent DFT in the linear response formulation (38), we typically used 6107 steps in time to propagate the wavefunctions with a time step of $3.4 \times 10^{-3}$ fs, which gives an energy resolution of 0.1 eV. The perturbing external electric field is 0.1 V/Å. This computational scheme gives optical

absorption spectra that are in good agreement with experiment for a range of biologically relevant molecules such as DNA bases (39).

## RESULTS AND DISCUSSION
### Tetramer model of eumelanin
The basic idea behind our model is illustrated in Fig. 1: the four constituent eumelanin monomers IQ, HQ, MQ, and NQ, are covalently bonded together between the C2 and C7 sites, exclusively. An interior ring where all the N atoms reside, in an arrangement similar to porphyrin, is thus formed. That is, the four N atoms are separated by three successive covalently bonded C atoms in the inner ring: these are atoms C7 and C8 of the same monomer to which a given N belongs, and atom C2 of the next monomer, going through the inner ring in the counterclockwise direction, as shown in Fig. 1. The long axes of adjacent monomer units in the tetramer are perpendicular to each other.

We note that both a tetramer and a pentamer can be formed in this manner though the latter is less stable. A trimer or hexamer would place the long axes of adjacent monomers at an angle of $60^\circ$ or $120^\circ$, respectively, creating significant strain in the inner ring which renders both of these alternative structures unstable. Thus, the rule for creating rings in the manner described above naturally explains why the smallest protomolecule consists of four or five monomers, as suggested by the x-ray diffraction data (16,17) and STM images (18,19). The lateral size of the tetramer structure is $15\ \mathring{A} \times 15\ \mathring{A}$, assuming an intermolecular distance of $3\ \mathring{A}$, which is in excellent agreement with the presence of a peak at $q = 0.45\ \mathring{A}^{-1}$ (corresponding to a length scale of 13–16 $\mathring{A}$) in the x-ray data (16). For simplicity, we will concentrate on the tetramer structure for the eumelanin protomolecules.

![](./images/811958667669667840_1.jpg)

FIGURE 1 Monomer components of DHI-eumelanin and a tetramer composed of them: HQ-MQ-IQ-MQ or HMIM (green, C, red, O, blue, N, and white, H). Atoms in the IQ monomer are numbered in the standard notation.

There are many possible arrangements of the four different monomer units in a tetramer. Our calculations indicate that among the possible arrangements, those containing two or three QIs have large and positive formation energy (exothermic reaction), while the ones containing no QI units or comprising solely QI units have negative formation energy (endothermic reaction), strongly suggesting that the presence of QI stabilizes the eumelanin protomolecules (34). The presence of more than one type of tetramer is consistent with the recently proposed chemical disorder model for melanin (33). Indeed, we have shown that although each individual tetramer has characteristic absorbance peaks, the averaged adsorption over all dominant species gives a broad, featureless spectrum that is close to experimental results (34). Taken together with the stacking of tetramer units and their ion binding properties discussed below, these facts provide strong evidence that the porphyrinlike protomolecule structure can account for the basic properties of eumelanin mentioned above. Moreover, we find that protomolecules containing MQ units typically have a lower energy by 0.2–0.3 eV than the corresponding structures containing NQ units; accordingly, we will use the former as representative structures in our discussion. In matrix-assisted laser ionization mass spectrometry, tetramers are one of the dominant DHI oligomers found, indicating their relatively high stability (40).

### Formation pathway of the tetramer
An important issue is whether or not there exists a favorable formation pathway for the tetramers, beginning with the individual monomer units, under in vivo or in vitro conditions. It has been suggested that the C4 and C7 sites of the monomer are the two most favorable positions for bonding (with a slight preference for the C4-site), followed by the nitrogen site and the C3 and C2 sites (14,24). First-principles calculations show that among several possible dimer arrangements including some nonplanar ones, the most stable structures have a covalent bond between C2 of one DHI unit and C7 of the next (referred to as C2-C7$'$ binding) (41). Our calculations confirm that this dimer structure, and the one with C2-C4$'$ binding, is 0.23 eV more-favorable than two isolated IQs using an $\text{H}_2$ molecule as the reservoir for the removed H atoms (Fig. 2). A hydrogen bond between the N-H and O6$'$ groups is also formed, which further stabilizes the structure. This dimer is very likely to be formed. All other

![](./images/811958667669667840_2.jpg)

FIGURE 2 Proposed formation pathway of the IMIM tetramer, as a representative example.

dimers have low or negative formation energies. After formation, we found that one IQ component in the dimer is likely to transfer its proton from N to the O atom bonded at C5 (or C6) forming MQ (or NQ); the resulting IQ-MQ dimer (referred to as IM) is 0.10 eV more stable than the IQ-IQ dimer (referred to as II). This is interesting because MQ and NQ in the monomer form are less stable than IQ (by 0.09 eV and 0.29 eV in our calculations, respectively). This result suggests that the presence of QIs is important in eumelanin synthesis, consistent with experimental findings on the presence of QI species produced upon one-electron oxidation of DHI monomers (22,23). Hereafter we will label each dimer and oligomers by the first letters of its constituent monomers in order, as in the cases IM (for the IQ-MQ dimer) and II (for the IQ-IQ dimer) above.

It is interesting that the IQ-unit in the original IM dimer (labeled IMa in Fig. 2) can rotate by $180^\circ$ around its long axis to form a $\text{NH}\cdots\text{N}$ hydrogen bond with the N atom of the MQ unit (IMb in Fig. 2), because this bond is stronger than the $\text{NH}\cdots\text{O}$ bond. This lowers the energy by 0.11 eV. As a result, the stable dimer structure would have two N atoms on the same side. Two such dimers can form an IMIM tetramer in the same manner, with four N atoms forming an interior ring that resembles the porphyrin structure. Thus, we have presented a plausible pathway for the synthesis of the porphyrinlike tetramer structure. Other tetramers with different monomeric components could form in a similar way or by further modification of the already-formed tetramers through proton transfer and chemical reactions. In the $^1\text{H}$ NMR experiment (42) on human hair melanin and sepia melanin, signals for the hydrogen atoms at C2 and C7 sites are significantly weaker than H at other sites, suggesting the dominance of the C2-C7 linkage between monomers, consistent with our structural model. Very recently, a similar tetramer structure composed of two C2-C4$'$ coupled dimers linked through C2-C3$'$ sites has been synthesized by peroxidase/ $\text{H}_2\text{O}_2$-induced oxidation in the presence of $\text{Zn}^{2+}$ ions (43). We expect that the porphyrinlike tetramers proposed in this work might soon be obtained under appropriate conditions.

The oligomerization of melanin monomers to form tetramers results in significant changes in the electronic structure. Fig. 3 shows the absorption spectra of the IQ monomer, various intermediate dimers, and the final tetramer. The main feature is the overall red shift of major absorption peaks, suggesting electron delocalization due to polymerization upon forming the C2-C7$'$ covalent bonds between the monomers. The IQ monomer shows three major peaks at 274, 301, and 347 nm and a small, broad peak at $\sim$750 nm. When two IQs combine to form an II dimer, major peaks with large intensity in the range of 350-700 nm develop. The formation of the IMa dimer and molecular-plane rotation leading to the IMb dimer introduce a gradual blue shift of the first peak on the right, from 620 nm to 510 nm, indicating that the dimer is further stabilized (the blue shift indicates larger separation between occupied bonding states and unoccupied antibonding states). However, all dimers show the same peak at wavelength $\lambda = 350$ nm, regardless of their detailed structure and relative orientation of the dimer units. The tetramer structure formed by combining two IMb dimers preserves the two major peaks of the IMb dimer, at 350 nm and 480 nm, respectively. Nevertheless, in the tetramer spectrum the latter peak has a larger relative intensity and is slightly blue-shifted, which may reflect the formation of the porphyrin ring.

These arguments are supported by the character of the wavefunctions of the corresponding orbitals, between which the transitions take place. Fig. 4 shows the dipole moment directions for the two transitions and the wavefunctions of the orbitals with which the transitions are mainly associated. Both transitions are of $\pi \rightarrow \pi^*$ type, with the transition dipole moments strictly confined in the molecular plane. Clearly, the transition at 480 nm has a major contribution from the four intermonomer C2-C7$'$ bonds. It demonstrates the de-

![](./images/811958667669667840_3.jpg)

FIGURE 3 Evolution of optical absorbance spectrum along the proposed formation pathway of the IMIM tetramer. These spectra are not renormalized to each other.

![](./images/811958667669667840_4.jpg)

FIGURE 4 (a) Dipole moment directions for transitions at 480 nm and 350 nm in the IMIM tetramer. (b) The wavefunctions corresponding to states between which the transitions take place. (c) Total density of states (DOS) of IMIM; the Fermi level is set to zero and the 480 nm and 350 nm transitions between states are indicated by horizontal arrows.

localization effect due to C2-C7' bond formation. On the other hand, the transition at 350 nm is mainly related to intramonomer bonds and transitions to the corresponding antibonding states. As a result, the 480-nm transition is more dependent on the intermonomer bonding environment in the polymerization process while the 350-nm transition is related to the intrinsic character of IQ monomers and is less influenced by the polymerization, consistent with the above structural analysis.

The features in Fig. 3 could serve as fingerprints for identifying intermediate structures of the oligomers during melanin synthesis. To this end, we compare our calculated spectra with available experiments. Experimental HQ spectra show bands at 270 and 300 nm (44). This is consistent with our calculations for the spectra of HQ (300 nm) and IQ (274, 301, and 347 nm) taken together, suggesting that the measurements may correspond to a mixture of the two forms. Oxidation experiments of indolic melanin have revealed the presence of methide/imine as intermediates in the polymerization process, and the dimer products are characterized by a broad peak at 500-700 nm (23,45), consistent with our theoretical model. Indeed, the C2-C4' (and C2-C7') forms of dimers were successfully synthesized in solution and in crystalline form, and were found to be dominant during eumelanin biosynthesis, exhibiting a blue fluorescence (46,47). A recent study (44) further demonstrated that among the three dominant dimer forms, dimers coupled at C2-C7' have the highest formation yield (12% molar yield, three times higher than that of the C2-C4' coupling) in the organic solvents. The resulting transient absorption spectra upon pulse radiolytic one-electron oxidation show peaks at 380 nm and 530 nm, in agreement with our results. Excitation spectra show peak maxima at 275 nm and 330-370 nm in the range of 250-450 nm for eumelanin species of molecular weight < 1000 (48); the corresponding emission shows peaks at 414 nm and 500 nm (48). All these features are consistent with the calculated optical properties of the tetramer species (molecular weight = 580), with peaks at 277, 350, and 480 nm as shown in Fig. 3.

It should be noted that the present ab initio calculations do not include solvent effects. In real melanin synthesis in vivo and in vitro, solvent molecules are very important to act as hydrogen reservoirs, to disrupt hydrogen-bonding patterns around melanin oligomers, and to assist excited-state proton transfer (49); all may have a significant effect on the stability of various oligomers and the formation pathway. In addition, the solvent interactions may drive important features such as the proportion of various redox states (44), the extent of protomolecular sheet, and even the aggregate size (12) (given that the aggregate size and shape may be determined by the entropic need to minimize the surface energy in poor solvents). However, inclusion of solvent molecules explicitly is very challenging given the current capabilities of ab initio calculations and existing computational resources, due to the long simulation time required to fully account for the dynamical effects of the solvated structure and the very large system size. Our calculations represent a realistic model of possible melanin structures in vacuum, with the main focus on the structural features arising from strong covalent bonds. We also discuss the resulting electronic and optical properties of these models, which are only marginally affected by the solvents. The general agreement between our results and existing experimental evidence justifies our choice to focus on these structural features, at least as a first attempt to address the large scale structure of melanin.

Biophysical Journal 94(6) 2095-2105

### Planar stacking

Beyond the finite lateral size of 15–20 Å for melanin protomolecules, x-ray diffraction experiments also found evidence for aromatic stacking of 3–4 layers of planar oligomers (17). STM measurements determined a height variation of ~10 Å when imaging melanin protomolecules (18). Our tetramer molecules can be easily stacked to form layered structures (Fig. 5). The main feature is the van der Waals interaction between neighboring layers. As a result, the average interlayer distance is ~3.0–3.3 Å, typical in DFT/LDA modeling of van der Waals systems. However, we find that additional covalent bonds form at certain sites between two neighboring tetramers when they are stacked. Such bonds would further stabilize the stacked structure. For example, when two planar HMHM tetramers are stacked, each retains its basic planar structure, but the C4 atom of each MQ unit deviates from the plane to form two covalent bonds between the MQs belonging to the upper and lower tetramers as shown in Fig. 5, *a* and *b*. Stacking and formation of these interlayer bonds lower the total energy of the HMHM-HMHM octamer by 1.75 eV relative to the two isolated tetramers. This energy comprises both interlayer covalent bonding and the van der Waals interaction energy; the latter is known to be underestimated significantly in DFT/LDA. The interlayer C-C bond has a length of 1.65 Å, significantly longer than typical C-C bonds in graphite (1.42 Å) and diamond (1.54 Å), and its strength is much weaker than those bonds: the atomization energy is 4.95 eV/bond in graphite for comparison. Analysis of the equilibrium structural parameters reveals that the interlayer distance averaged over all heavy atoms except those forming interlayer bonds is 3.06 Å for the MQ-MQ pairs (where the interlayer bonds are formed), and 3.35 Å for the HQ-HQ pairs (where no interlayer bonds form). The latter value is identical to the interlayer distance in graphite. This fact suggests that the formation of interlayer covalent bonds leads to the compression of interlayer spacing to the lower limit of the typical aromatic stacking distance, thus increasing the stability of the aggregate structure. We have also calculated the properties of other stacked-tetramer structures. In the IMIM-IMIM structure, four interlayer C-C bonds are formed, all on the C4 sites of each monomer, resulting in a net gain in energy of 3.58 eV due to stacking (including covalent bonding and van der Waals interaction). In the HMIM-HMIM structure, only three interlayer covalent bonds are formed, with a total stacking energy of 2.99 eV.

![](./images/811958667669667840_5.jpg)

FIGURE 5 Stacking structures of two tetramers: (a) top and (b) side views of the planar stacking of the HMHM-HMHM structure; (c) top and (d) side views of the helical stacking of an IMIM-IMIM structure.

This result seems to suggest that IQ-IQ and MQ-MQ stacking will likely lead to covalent bond formation between these pairs of monomers while stacking of HQ-HQ will not. Our calculations of two individual monomers stacked on top of each other indeed confirm this: two IQs form strong covalent bonds between C4-C4′ and C7-C7′ sites with a total binding energy of 1.94 eV. Similarly, two MQs also form interlayer bonds with energy gain of 1.38 eV, while two HQs do not form covalent bonds when stacked, with the van der Waals energy gain in this case being only 0.20 eV. It is also possible that bonds between stacked IQ and MQ, or IQ and HQ, will be formed. These results suggest that the tendency of forming interlayer bonds is in the order of IQ > MQ(NQ) > HQ, with a tunable strength depending on the chemical composition. The interlayer covalent bonds in melanin-layered structures are unusual and may explain the finite size of planar and stacked melanin protomolecules. Interlayer bonds at C4 sites, whose bond-formation tendency is as high as C7 sites, block further lateral polymerization at this site. After forming two interlayer bonds between two HMHM tetramers, the capacity of the molecules to form covalent bonds is saturated and further increase in the size of the oligomer is inhibited, as confirmed from our calculations on the three-layered structure. Thicker stacks could be formed by alternating interlayer bond formation. The formation of covalent bonds between layers in melanin was first postulated by Cheun et al. (10), but was subsequently considered to be unlikely (11). The interlayer bond formation at specific sites makes the bonded and stacked structures of melanin protomolecules more stable than the regular van der Waals stacking, and could be responsible for the insolubility of melanin in any solvent without disturbing its structure (12).

### Helical stacking

Instead of the planar stacking, it is possible to construct an arrangement of the tetramer protomolecules which maintains the essential features of stacking in what concerns the in-

termolecule spacing. This alternative structure consists of a helix, shown in Fig. 5, c and d, formed by connecting successive tetramer units through bonding of the C7 site of the first monomer in a tetramer to the C2 site of the fourth monomer in the next tetramer. The plane of each monomer is tilted by $\sim 10^\circ$, so that the fourth monomer does not close the tetramer ring to form a planar structure as in Fig. 1, but the chain of monomers continues to grow, with the fifth monomer situated directly above the first, forming a helix. In principle, this can be continued indefinitely; we show in Fig. 5 only a short segment containing a total of eight monomers (equivalent in size to the two planar stacked tetramers). In close analogy to the planar stacking between tetramers, interlayer bonds between monomer units directly above each other are also formed in the helical structure. In the (IM)$_4$ helix shown in Fig. 5, c and d, there is one interlayer bond at the C4 site per monomer. The stacking distance in the helix averaged over all heavy atoms except those bonded by the interlayer bonds is 3.03 Å; this value is slightly larger, 3.16 Å, if only the 16 atoms sitting on the inner porphyrin ring are considered. Both numbers are almost identical to those of the planar stacked IMIM-IMIM octamers, 3.05 Å and 3.16 Å, respectively. Accordingly, the two stacking pathways would probably lead to indistinguishable structural parameters and images in experimental observations. Other helices such as (HM)$_4$ and (HMIM)$_2$ exhibit the same behavior as the planar stacked tetramers, that is, covalent bonds form between the IQ-IQ and MQ-MQ units that are situated above each other.

The energies of the helical structures are comparable to the corresponding planar stacked structures. For instance, the energy difference between two planar stacked tetramers and the corresponding helical structure is only 0.09 eV for two HMHM tetramers, 0.15 eV for two HMIM tetramers and 1.36 eV for two IMIM tetramers, respectively, with the planar stacking always favored. Both types of stacking could be viable candidates for a hierarchy of structures formed in eumelanin synthesis. Experimentally, one-dimensional nanofilaments with a width of 15-50 nm and a height of 3-6 nm spreading over several microns in length are observed in atomic force microscopy images of sepia eumelanin formed from species with molecular weight of 1000-3000 (12). This is consistent with the helical structure we propose here, which could be the basic unit of nanofilaments. The linear connection between monomers in a helix also agrees with the dominant molecular weights of 444, 591, and 738 observed in laser ionization mass spectrometry, which correspond to three, four, and five DHI molecules linearly connected plus an extra H$^+$ (40).

When the tetramers are stacked, either in the planar or in the helical structure, we expect the electrons to be more delocalized. Correspondingly, the optical absorption spectra of both planar-stacked and helical protomolecules should have fewer sharp features. This expectation is borne out by our calculations, the results of which are shown in Fig. 6. For example, instead of the four to five sharp peaks as for the IMIM tetramer, only a single broad peak at 400 nm is present in the range $\lambda > 200$ nm for the two stacked tetramers. This is a good indication that stacking of tetramers is a realistic representation of the eumelanin structure, which has a broad and featureless absorption band. The characteristic features of the spectra in Fig. 6 are very similar to the diminishing single absorption peak at 330 nm during DHICA-melanin synthesis (33). Human iris melanin also shows a single absorption peak at 340 nm (4). Indeed, although dependent on excitation wavelength, the emission of various eumelanin materials all show a peak at $\sim$400-500 nm (48,50), suggesting that stacked tetramers may be dominant in a variety of protomolecules.

## Dipole moment strength

Riesz et al. (51) recently measured the transition dipole strength during eumelanin polymerization in DHICA solution and found $\sim$20% hyperchroism of eumelanin relative to its DHICA monomer. In addition, the dipole strength first increases rapidly by 26% then decreases slowly by a small amount ($\sim$5%) during polymerization. Integrating the absorbance spectra in Figs. 3 and 6, we obtain the transition dipole strength for each melanin species that can be directly compared to the experimental measurements of Riesz et al. We observed exactly the same behavior during the proposed polymerization and stacking process described in Figs. 3 and 6. The calculated dipole strength for the IQ monomer, the IMb dimer, the IMIM tetramer, and the planar and helical stacked two-tetramer structures, is 13.9, 38.4, 50.2, 47.7, and 45.4 Debye$^2$ per monomer unit, respectively, in the 250-600 nm wavelength range. Experimental data in the same UV-vis range are 31 Debye$^2$ for DHICA and 37 Debye$^2$ per monomer for eumelanin (assuming averaged DHI and DHICA molar weight as the monomer weight). The measured dipole strength for DHICA is larger than our calculated value for the DHI monomer, but close to that for the IM dimer. The

![](./images/811958667669667840_6.jpg)

FIGURE 6 Optical absorbance spectrum of two stacked IMIM tetramers in the planar and helical arrangements. The spectrum of constituent IMIM tetramer (magnified by a factor of 2) is also shown for comparison.

calculated dipole strength for oligomers ranging from the dimer to the helical or planar stacked octamer is generally in good agreement with the measured values for eumelanin. More importantly, the theoretical values follow the same trend as in experiment, i.e., going from the monomer to the tetramer, the dipole strength increases by $20\sim30\%$ because of polymerization, and then it decreases by $5\sim10\%$ due to stacking. This is additional evidence in support of the proposed oligomer structures and the polymerization pathway.

Metal ion binding

Our model also accounts naturally for the capture and release of metal ions by melanin, without any apparent change in structure. The inner ring of the tetramer structure we propose is identical to that in porphyrin, especially if the tetramer contains exactly two QIs that are not adjacent. It is well known that porphyrin can capture and release a variety of metal ions without being affected in structure. Consequently, the tetramers in our proposed model, which have H atoms in the same positions as porphyrin, should exhibit similar behavior. Three tetramers, HMHM, HMIM, and IMIM, satisfy this condition. We note that some of the porphyrin-type tetramers are actually the ones with the highest formation energy, and thus may be found in higher proportion. This provides a natural explanation of the number-4 characteristic of melanin discussed earlier (see Introduction). Indeed, the binding capacity of one ion per 3–4 monomer units is in agreement with our model (32).

We performed calculations to investigate the ion binding properties of the porphyrinlike tetramers. Our results show that the most favorable site for ion chelation is the inner N ring, just as expected by analogy to the behavior of porphyrin (Fig. 7). For example, the binding energy for a Fe atom at the inner ring of HMHM, HMIM, and IMIM tetramers is 3.98, 4.32, and 4.42 eV (using the PBE exchange-correlation functional), respectively, with the reference configuration being the isolated tetramer, a free Fe atom, and $\text{H}_2$ molecules as the reservoir for the removed H atoms from the NH groups. Attaching Fe at the catechol sites of HQ, MQ, and IQ components gives binding energies of 0.90, 1.67, and 3.14 eV, respectively, which are less stable. Experiments show evidence for amine groups as the possible ion-binding sites besides the carboxyl and catechol sites (for DHICA-containing melanin) (52). Our calculations also show that after iron binding, the absorbance is enhanced in the long wavelength region $500\ \text{nm}>\lambda>900\ \text{nm}$ and decreased in the short wavelength region $200\ \text{nm}>\lambda>500\ \text{nm}$, resulting in a more broad, featureless adsorption spectrum (Fig. 7), in agreement with experiment (53).

Incorporation of DHICA

The preceding discussion was based on the tetramer structure built from the DHI component together with its redox forms (IQ, MQ, and NQ). It is also possible to construct tetramer structures which incorporate a mixture of the DHI and the DHICA components. Fig. 8 shows two such structures with DHI/DHICA ratios of 3:1 and 1:1, respectively. In this construction, the COOH group in the DHICA units forms a peptide bond with the NH group in the DHI units and releases a $\text{H}_2\text{O}$ molecule. The four-atom inner ring of the tetramer structure is maintained but some N atoms are replaced by C atoms. In the molecule which has DHI-DHICA = 1:1, it is also possible to form a six-membered sugar ring between adjacent units by eliminating a H atom, as shown in the third structure of Fig. 8; this structure is slightly more favorable energetically by 0.65 eV. The three molecules with DHICA components also exhibit characteristic absorption peaks in the range of $300\ \text{nm}<\lambda<900\ \text{nm}$, as shown in Fig. 8. These structures are offered as plausible models for the DHICA-containing melanin, which follows the same structural pattern as the tetramer model for DHI-melanin. Other structures such as a DHICA chain (54) may also be possible, and direct experimental measurements are necessary to establish their validity.

CONCLUSIONS

To explore the microscopic structure and the structure-function relationship of the melanin pigment, we have focused on two basic questions of fundamental importance:

1. How are melanin macromolecules formed starting from monomer polymerization?

![](./images/811958667669667840_7.jpg)

FIGURE 7 The effect of Fe binding on the optical absorption of the HMHM tetramer: (a) molecular structure; (b) optical spectra.

![](./images/811958667669667840_8.jpg)

FIGURE 8 Incorporation of DHICA component in the tetramer model of eumelanin, in the DHI/DHICA 3:1 ratio (left panel) and 1:1 ratio (middle and right panels). The middle and right panels differ only by the presence of two sugar rings in the latter structure. The optical absorbance for individual molecules is also shown under each structure.

2. From what source do the characteristic broad-band absorption features arise?

To answer these questions, we have introduced a model for the structure of eumelanin protomolecules, based on the premise that they contain an inner ring resembling the structure of porphyrin. This leads directly to the tetramer structure that we discussed in detail, including a plausible formation pathway and the structural and optical properties of intermediate and final structures for the protomolecules, with an ultimate planar or helical stacking character. This model provides a natural explanation for a variety of experimental observations on the properties of melanin, including structural features deduced from x-ray studies, the presence of the tautomers of indolequinone (which are energetically disfa- vored but detected to be present during melanin synthesis), the insolubility of protomolecules, the ability to capture and release metal ions, and the different DHI/DHICA ratios in natural melanin. The calculated dipole strength during this process agrees with observed trends in a recent experiment: first, there is hyperchroism due to polymerization, and then, slight hypochroism due to stacking.

As far as the broad-band optical absorption is concerned, we conclude that two major factors are responsible:

1. We have shown that electron delocalization and elec- tronic band mixture during the in-plane polymerization of monomers to form oligomers, formation of stacked layers or helices (especially through interlayer covalent bonding), and metal binding, all lead to the extension of absorption spectrum to longer wavelengths and the soften- ing of strong absorption bands. As a result, a smooth broader adsorption spectrum develops.

2. The possibility of constructing oligomers, including pro- totype tetramers in a variety of ways starting with hydro- quinone and its three redox forms, suggests a featureless spectrum when an average is taken over the many pos- sible structures (34). Additional smaller variations in the overall structure due to stacking of the protomolecules and interaction with different metal ions will further contribute to the absence of any features in the absorption spectrum.

Two key notions, presented here for the first time to our knowledge, are crucial for understanding the protomolecule structure of eumelanin: the possibility of a helical structure to account for the apparent stacking of protomolecules, and the fact that strong covalent bonds exist between the stacked monomers. The stacking of monomers in the helical structure is indistinguishable from that in planar stacking of tetramers, and thus consistent with experimental structural studies. The strong covalent bonds between the stacked monomers, which are identical in the planar-stacked and the helical structures, may explain the inertness and insolubility of the resulting units; it may also account for the finite size of these units, as opposed to infinitely extended structures. Because these interlayer bonds are much weaker than the in-plane graphitic bonds and their strength is tunable depending on the relative HQ/IQ composition, they can be easily modified under different conditions in vivo, introducing further structural variability or even tailoring melanin structures to satisfy the needs in different circumstances and organisms (25).

While our model explains a range of melanin properties, it is probably a rather simplified version of the actual structure of this important substance, because the presence of proteins, water molecules, and other factors may also contribute in important ways to the structure that exists in the biological environment. In this sense, our model may constitute the first step toward the construction of a complete picture which could explain the full range of properties and biological functions of melanin.

We are grateful to G. Zonios, P. Meredith, and J. Riesz for many useful discussions on the experimentally observed properties of melanin.

Biophysical Journal 94(6) 2095-2105

REFERENCES

1. Ito, S. 2003. A chemist's view of melanogenesis. *Pigment Cell Res.* 16:230–236.

2. Morison, W. L. 1985. What is the function of melanin? *Arch. Dermatol.* 121:1160–1163.

3. Hill, H. Z. 1992. The function of melanin. *Bioessays.* 14:49–56.

4. Kollias, N., R. M. Sayre, L. Zeise, and M. R. Chedekel. 1991. Photoprotection by melanin. *J. Photochem. Photobiol.* B. 9:135–160.

5. Ortonne, J.-P. 2002. Photoprotective properties of skin melanin. *Br. J. Dermatol.* 146:7–10.

6. Zucca, F. A., G. Giaveri, M. Gallorini, A. Albertini, M. Toscani, G. Pezzoli, R. Lucius, H. Wilms, D. Sulzer, S. Ito, K. Wakamatsu, and L. Zecca. 2004. The neuromelanin of human *Substantia nigra*: physio- logical and pathogenic aspects. *Pigment Cell Res.* 17:610–617.

7. Bush, W. D., J. Carguilo, F. A. Zucca, A. Albertin, L. Zecca, G. S. Edwards, R. J. Nemanich, and J. D. Simon. 2006. The surface oxidation potential of human neuromelanin reveals a spherical architecture with a pheomelanin core and a eumelanin surface. *Proc. Natl. Acad. Sci. USA.* 103:14785–14789.

8. Berendschot, T. T. J. M., J. J. M. Willemse-Assink, M. Bastiaanse, P. T. V. M. de Jong, and D. van Norren. 2002. Macular pigment and melanin in age-related maculopathy in a general population. *Invest. Ophthalm. Vis. Sci.* 43:1928–1932.

9. Pavel, S., F. van Nieuwpoort, H. van der Meulen, C. Out, K. Pizinger, P. Cetkovska, N. P. M. Smit, and H. K. Koerten. 2004. Distributed melanin synthesis and chronic oxidative stress in dysplastic nevi. *Eur. J. Cancer.* 40:1423–1430.

10. Cheun, W. L., K. Kim, and J. Shao. 2004. The chemical structure of melanin. *Pigment Cell Res.* 17:422–423.

11. Simon, J. D., and S. Ito. 2004. The chemical structure of melanin. *Pigment Cell Res.* 17:423–424.

12. Liu, Y., and J. D. Simon. 2003. Isolation and biophysical studies of natural eumelanins: applications of imaging technologies and ultrafast spectroscopy. *Pigment Cell Res.* 16:606–618.

13. Ito, S., and K. Wakamatsu. 2003. Quantitative analysis of eumelanin and pheomelanin in humans, mice and other animals: a comparative review. *Pigment Cell Res.* 16:523–531.

14. Meredith, P., and T. Sarna. 2006. The physical and chemical properties of eumelanin. *Pigment Cell Res.* 19:572–594.

15. McGinness, J., P. Corry, and P. Proctor. 1974. Amorphous semicon- ductor switching in melanins. *Science.* 183:853–855.

16. Cheng, J., S. C. Moss, and M. Eisner. 1994. X-ray characterization of melanins—I. *Pigment Cell Res.* 7:255–262.

17. Cheng, J., S. C. Moss, M. Eisner, and P. Zschack. 1994. X-ray characterization of melanins—II. *Pigment Cell Res.* 7:263–273.

18. Zajac, G. W., J. M. Gallas, J. Cheng, M. Eisner, S. C. Moss, and A. E. Alvarado-Swaisgood. 1994. The fundamental unit of synthetic mela- nin: a verification by tunneling microscopy of x-ray scattering results. *Biochim. Biophys. Acta.* 1199:271–278.

19. Zajac, G. W., J. M. Gallas, and A. E. Alvarado-Swaisgood. 1994. Tunneling microscopy verification of an x-ray scattering-derived molecular model of tyrosine-based melanin. *J. Vac. Sci. Technol.* B. 12:1512–1516.

20. Diaz, P., Y. Gimeno, P. Carro, S. Gonzalez, P. L. Schilardi, G. Benitez, R. C. Salvarezza, and A. H. Creus. 2005. Electrochemical self- assembly of melanin films on gold. *Langmuir.* 21:5924–5930.

21. Bertazzo, A., C. V. L. Costa, G. Allegri, M. Schiavolin, D. Favretto, and P. Traldi. 1999. Enzymatic oligomerization of tyrosine by tyrosinase and peroxidase studied by matrix-assisted laser desorption/ ionization mass spectrometry. *Rapid Commun. Mass Spectrom.* 13:542–547.

22. Lambert, Ch., J. N. Chacon, M. R. Chedekel, E. J. Land, P. A. Riley, A. Thompson, and T. G. Truscott. 1989. A pulse radiolysis investi- gation of the oxidation of indolic melanin precursors: evidence for indolequinones and subsequent intermediates. *Biochim. Biophys. Acta.* 993:12–20.

23. Lambert, Ch., E. J. Land, P. A. Riley, and T. G. Truscott. 1990. A pulse radiolysis investigation of the oxidation of methoxylated metabolites of indolic melanin precursors. *Biochim. Biophys. Acta.* 1035:319–324.

24. Al-Kazwini, A. T., P. O'Neil, G. E. Adams, R. B. Cundall, B. Jaquet, G. Lang, and A. Junino. 1990. One-electron oxidation of methoxylated and hydroxylated indoles by $N_3$: 1. Characterization of the primary indolic radicals. *J. Phys. Chem.* 94:6666–6670.

25. Hong, L., J. D. Simon, and T. Sarna. 2006. Melanin structure and the potential functions of uveal melanosomes. *Pigment Cell Res.* 19:465–466.

26. Bu'Lock. J. D., and J. Harley-Mason. 1951. Melanin and its precursors: 2. Model experiments on the reactions between quinones and indoles, and consideration of a possible structure for the melanin polymer. *J. Chem. Soc. London.* 1951:703–712.

27. Galvao, D. S., and M. J. Caldas. 1990. Theoretical investigation of model polymers for eumelanins. I. Finite and infinite polymers. *J. Chem. Phys.* 92:2630–2636.

28. Stark, K. B., J. M. Gallas, G. W. Zajac, M. Eisner, and J. T. Golab. 2003. Spectroscopic study and simulation from recent structural models for eumelanin: II. Oligomers. *J. Phys. Chem. B.* 107:11558–11562.

29. Stark, K. B., J. M. Gallas, G. W. Zajac, J. T. Golab, S. Gidianian, T. McIntire, and P. J. Farmer. 2005. Effect of stacking and redox state on optical absorption spectra of melanins—comparison of theoretical and experimental results. *J. Phys. Chem. B.* 109:1970–1977.

30. Il'ichev, Y. V., and J. D. Simon. 2003. Building blocks of eumelanin: relative stability and excitation energies of tautomers of 5,6-dihydrox- yindole and 5,6-indolequinone. *J. Phys. Chem.* 107:7162–7171.

31. Powell, B. J., T. Baruah, N. Bernstein, K. Brake, R. H. McKenzie, P. Meredith, and M. R. Pederson. 2004. A first-principles density- functional calculation of the electronic and vibrational structure of the key melanin monomers. *J. Chem. Phys.* 120:8608–8615.

32. Liu, Y., L. Hong, V. R. Kempf, K. Wakamatsu, S. Ito, and J. D. Simon. 2004. Ion exchange and adsorption of $Fe^{III}$ by sepia melanin. *Pigment Cell Res.* 17:262–269.

33. Tran, M. L., B. J. Powell, and P. Meredith. 2006. Chemical and structural disorder in eumelanins: a possible explanation for broadband absorbance. *Biophys. J.* 90:743–752.

34. Kaxiras, E., A. Tsolakidis, G. Zonios, and S. Meng. 2006. Structural model of eumelanin. *Phys. Rev. Lett.* 97:218102.

35. Soler, J. M., E. Artacho, J. D. Gale, A. García, J. Junquera, P. Ordejón, and D. Sánchez-Portal. 2002. The SIESTA method for ab initio order- N materials simulation. *J. Phys. Condens. Matter.* 14:2745–2779.

36. Troullier, N., and J. L. Martins. 1991. Efficient pseudopotentials for plane-wave calculations. *Phys. Rev. B.* 43:1993–2006.

37. Ceperley, D. M., and B. J. Alder. 1980. Ground-state of the electron- gas by a stochastic method. *Phys. Rev. Lett.* 45:566–569.

38. Tsolakidis, A., D. Sánchez-Portal, and R. M. Martin. 2002. Calculation of the optical response of atomic clusters using time-dependent density functional theory and local orbitals. *Phys. Rev. B.* 66:235416.

39. Tsolakidis, A., and E. Kaxiras. 2005. A TDDFT study of the optical response of DNA bases, base pairs, and their tautomers in the gas phase. *J. Phys. Chem. A.* 109:2373–2380.

40. Bertazzo, A., D. Favretto, C. V. L. Costa, G. Allegri, and P. Traldi. 2000. Effects of ultraviolet irradiation on melanogenesis from tyrosine, dopa and dopamine: a matrix-assisted laser desorption/ionization mass spectrometric study. *Rapid Commun. Mass Spectrom.* 14:1862–1868.

41. Stark, K. B., J. M. Gallas, G. W. Zajac, M. Eisner, and J. T. Golab. 2003. Spectroscopic study and simulation from recent structural models for eumelanin: I. Monmer, dimers. *J. Phys. Chem. B.* 107:3061–3067.

42. Katritzky, A. R., N. G. Akhmedov, S. N. Denisenko, and O. V. Denisko. 2002. $^1$H NMR spectroscopic characterization of solutions of sepia melanin, sepia melanin free acid and human hair melanin. *Pigment Cell Res.* 15:93–97.

43. Panzella, L., A. Pezzella, A. Napolitano, and M. d'Ischia. 2007. The first 5,6-dihydroxyindole tetramer by oxidation of 5,5',6,6'-tetrahy- droxy-2,4'-biindolyl and an unexpected issue of positional reactivity en route to eumelanin-related polymers. *Org. Lett.* 7:1411-1414.

44. Zhang, X., C. Erb, J. Flammer, and W. M. Nau. 2000. Absolute rate constants for the quenching of reactive excited states by melanin and related 5,6-dihydroxyindole metabolites: implications for their antiox- idant activity. *Photochem. Photobiol.* 71:524-533.

45. Pezzella, A., L. Panzella, O. Crescenzi, A. Napolitano, S. Navaratman, R. Edge, E. J. Land, V. Barone, and M. d'Ischia. 2006. Short-lived quinonoid species from 5,6-dihydroxyindole dimers en route to eumelanin polymers: integrated chemical, pulse radiolytic, and quan- tum mechanical investigation. *J. Am. Chem. Soc.* 128:15490-15498.

46. d'Ischia, M., and G. Prota. 1987. Photooxidation of 5,6-dihydroxyl-1- methyl-indole. *Tetrahedron.* 43:431-434.

47. Corradini, M. G., A. Napolitano, and G. Prota. 1986. A biosynthetic approach to the structure of eumelanin. The isolation of oligomers from 5,6-dihydroxyl-1-methylindole. *Tetrahedron.* 42:2083-2088.

48. Nofsinger, J. B., and J. D. Simon. 2001. Radiative relaxation of sepia eumelanin is affected by aggregation. *Photochem. Photobiol.* 74:31-37.

49. Olsen, S., J. Riesz, I. Mahadevan, A. Coutts, B. J. Powell, R. H. McKenzie, S. C. Smith, and P. Meredith. 2007. Convergent proton transfer photocycles violate mirror-image symmetry in a key melanin monomer. *J. Am. Chem. Soc.* 129:6672-6673.

50. Meredith, P., B. J. Powell, J. Riesz, S. P. Nighswander-Rempel, M. R. Pederson, and E. G. Moore. 2006. Towards structure-property-function relationships for eumelanin. *Soft Matter.* 2:37-44.

51. Riesz, J. J., J. B. Gilmore, R. H. McKenzie, B. J. Powell, M. R. Pederson, and P. Meredith. 2007. Transition dipole strength of eumelanin. *Phys. Rev. E.* 76:021915.

52. Hong, L., and J. D. Simon. 2006. Insight into the binding of divalent cations to sepia eumelanin from IR absorption spectroscopy. *Photochem. Photobiol.* 82:1265-1269.

53. Samokhvalov, A., Y. Liu, and J. D. Simon. 2004. Characterization of the $Fe^{III}$-binding site in sepia eumelanin by resonance Raman confocal microspectroscopy. *Photochem. Photobiol.* 80:84-88.

54. Pezzella, A., D. Vogna, and G. Prota. 2003. Synthesis of optically active tetrameric melanin intermediates by oxidation of the melano- genic precursor 5,6-dihydroxyindole-2-carboxylic acid under biomi- metic conditions. *Tetrahedron Asymmetry.* 14:1133-1140.
