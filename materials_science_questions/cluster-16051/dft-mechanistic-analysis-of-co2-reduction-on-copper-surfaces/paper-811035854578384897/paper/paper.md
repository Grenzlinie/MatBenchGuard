# PCCP

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: K. Taylor-Edinbyrd, T. Li and R. Kumar, *Phys. Chem. Chem. Phys.*, 2017, DOI: 10.1039/C7CP01704A.

![](./images/811035854578384897_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the author guidelines.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the ethical guidelines, outlined in our author and reviewer resource centre, still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/811035854578384897_2.jpg)

rsc.li/pccp

# Effect of chemical structure of S-nitrosothiols on nitric oxide release mediated by the copper sites of a metal organic framework based environment

Kiara Taylor-Edinbyrd, Tanping Li and Revati Kumar*

Department of Chemistry, Louisiana State University, Baton Rouge, LA 70803, USA

**Abstract:** The effect of chemical structure of different biologically compatible S-nitrosothiols on the solvation environment at catalytic copper sites in a metal organic frameworks (MOFs) suspended in a solution of ethanol is probed using computational methods. The use of a copper based MOF as a storage vehicle and catalyst (copper sites of the MOF) in the controlled and sustained release of chemically stored nitric oxide (NO) from S-nitrosocysteine has been shown to occur both experimentally and computationally [*J. Am. Chem. Soc.*, **2012**, *134*, 3330-3333; *Phys. Chem. Chem. Phys.*, **2015**, *17*, 23403]. Previous studies on a copper based MOF, namely HKUST-1 concluded that modifications in the R-group of s-nitrosothiols and/or organic linkers of MOFs led to a method capable of modulating NO release. In order to test the hypothesis that larger R-groups slow down NO release, four different RSNOs (R=cysteine, N-Acetylcysteine, N-Acetyl-D,L-Penicillamine or glutathione) of varying size were investigated, which in turn required the use of a larger copper based MOF. Due to its desirable copper centers and

more extensive framework, MOF-143, an analog of HKUST-1 was chosen to further explore both the effect of different RSNOs as well as MOF environments on NO release. Condensed phase classical molecular dynamics simulations are utilized to study the effect of the complex MOF environment as well as the chemical structure and size of the RSNO on the species on the catalytic reaction. The results indicate that in addition to the size of the RSNO species and the organic linkers within the MOF, the reaction rates can be modulated by the molecular structure of the RSNO and furthermore combining different RSNO species can also be used to tune the rate of NO release.

Keywords: Metal organic frameworks (MOFs), s-nitrosothiols (RSNOs), nitric oxide (NO)

*Corresponding author Email: revatik@lsu.edu

### 1. Introduction

Metal organic frameworks (MOFs) are porous materials that are highly tunable with a large range of possible metal centers and multi-dentate organic linkers. $^{2-6}$ While investigations have mainly centered on their industrial work in catalysis, $^{7-9}$ gas capture/adsorption $^{10-16}$ and separation, $^{17-22}$ these resilient nanomaterials have also shown promise as biosensors $^{23-25}$ and detoxifying agents. $^{26-29}$ Several attractive features of MOFs include their high surface area $^{30,31}$ and void space, $^{32}$ capable of acting as a molecular sieve $^{18,33}$ but flexible enough to be functionalized $^{34}$ to a researchers specific need. As MOFs have recently gained traction for their potential roles as drug storage and delivery vehicles, $^{35-40}$ the transportation of once cumbersome molecules has been made possible.

Known for its role in vasodilation, $^{41-43}$ nitric oxide (NO) is a gaseous free radical and signaling molecule (neurotransmitter) $^{44-46}$ with antianginal, $^{47,48}$ antithrombotic $^{49}$ and antibacterial properties. $^{50-53}$ Thought to be an ideal candidate in the treatment of numerous diseases, its high level of reactivity makes working with nitric oxide a laborious task. Consequently, a number of research efforts are focused on the fabrication of adequate delivery vehicles in which appreciable amounts of nitric oxide can be loaded and delivered efficiently. On the quest for adequate NO loading and delivery, many materials including nanogels, $^{54}$ micelles, $^{55}$ nanoparticles $^{56}$ and self-assembled monolayers have been used in addition to the exploration of MOFs. $^{57-59}$ Several examples of MOFs ability to load nitric oxide have been shown recently in the literature with one of the most

common being the direct loading of nitric oxide within the MOF akin to the loading of other gases including hydrogen, methane and carbon dioxide. $^{60,61}$ Vasodilation through the use of NO-loaded MOFs has been successfully demonstrated on the coronary arteries of pigs in which investigations demonstrated that vasodilation was higher with MOF-mediated nitric oxide release versus free nitric oxide control studies. $^{62}$

Another method of nitric oxide delivery within MOFs includes the functionalization of the organic linkers or metal centers with amine groups to allow the formation of NONOates $^{34,63}$ upon nitric oxide adsorption. While this allows for a great deal of control over nitric oxide release, it requires post-synthetic modification, which requires much care to accurately synthesize the desired materials. As an alternative to the direct loading of nitric oxide or the required functionalization of MOFs with secondary amines, recent experimental work has shown that nitric oxide can be stored chemically as s-nitrosocysteine (CysNO) and used in conjunction with HKUST-1. $^{64}$ The release of stored nitric oxide from CysNO is a consequence of a decomposition reaction that takes place in the presence of a catalyst, which in this case is the MOF-bound copper ion.

$$
2RSNO \xrightarrow{Cu^+, \ RSH} RSSR + 2NO
$$

This work performed by Harding *et al.* compared the rates of nitric oxide release within a free copper/ethanol solution to the HKUST-1 framework (Figure 1a). It was concluded that the presence of HKUST-1 had a tremendous role in slowing the release rate of nitric oxide from approximately 10 minutes to over 10 hours. While this study lacked the complete mechanism for which CysNO was decomposed into free nitric oxide, it provided the authors with a high level of certainty that a thiol (RSH) was necessary.

Moreover, this was the first time in which nitric oxide was chemically stored in the form of a RSNO and loaded into a MOF to demonstrate a slow, controlled and sustained level of nitric oxide release. Further work has focused on the vitality of Cu-MOF/RSNO systems within a true biological setting. The encapsulation of a Cu-BTC MOF within a polymeric material provides protection to the water-sensitive framework and was shown to release NO from various RSNO donors including CysNO, S-nitrosocysteamine (cysamNO) and S-nitrosohomocysteine (HcysNO).⁴⁹ Results of this experiment show that NO release occurs along varying timescales ranging from 2-15 hours despite the similarity in size and structure between the chosen RSNO molecules. Due to a lack in understanding the relationship between RSNO size and structure to reactivity, various works have investigated the differences in reactivity of RSNOs which can likely further affect the decomposition reaction needed for the ultimate formation of the RSSR organic byproduct and the desired NO molecule.⁶⁵,⁶⁶ Meyer *et al.* performed theoretical studies on the stability of SNAP, SNAC and GSNO, by calculating their bond dissociation energies (BDE).⁶⁶ It was determined that despite the similarities between SNAP and SNAC (SNAP contains the addition of two methyl groups at the alpha-carbon site) steric effects prevent the existence of anti and syn conformations in the tertiary RSNO SNAP, thus making SNAC, a primary RSNO more stable than the conventional stability exhibited by tertiary RSNOs like that of SNAP. The mechanism in which NO is released from RSNOs was investigated by Singh et al. through the use of photolysis, metal-ion initiated decomposition and transnitrosation. From this study it was determined that in the presence of a metal-ion catalyst, the reduced copper form (Cu⁺) was responsible for an increase in NO liberation from RSNO as opposed to the oxidized copper form (Cu²⁺).⁶⁷

Preliminary computational work by Li, Edinbyrd and Kumar to determine the mechanism in which the thiol facilitated the catalytic release of nitric oxide showed that the thiol was responsible for the first step of the catalytic cycle, namely the reduction of Cu(II) to Cu(I), as Cu(I) is the active catalyst for this reaction.¹ They also found that in addition to Cu(I), $[Cu(II)-RS]^+$ can also act as the active catalyst. While the complete catalytic cycle involves the loss of two molecules of nitric oxide and the formation of a disulfide bond, electronic structure calculations performed suggest that nitric oxide is released upon the RSNO coordination to the Cu(I) ion or the $[Cu(II)-SR]^+$ species. While ab initio molecular dynamics simulations allow for the observation of chemical reactions,⁶⁸ they are computationally intractable for the large systems under study in this work. Therefore classical molecular dynamics simulations were employed in an effort to study the approach of RSNO to the reactive site, the first step in the generation of nitric oxide from its precursor.

Previous work by Li, Edinbyrd and Kumar compared the free energy barriers of $CH_3SNO$, a simple RSNO, to that of CysNO in free copper as well as the MOF environment. Scrutiny of the free energy profiles for both CysNO and $CH_3SNO$ in free copper where one RSNO approaches the copper ion as well as the approach of a second RSNO show essentially no barrier as expected. In the presence of the MOF environment the approach of the initial RSNO to the copper center depicts a nearly barrier-less free energy profile like that of the free copper solution. On the contrary, the approach of a subsequent RSNO results in barriers on the order of 5 and 20kcal/mol for $CH_3SNO$ and

CysNO, respectively. It was concluded that these barriers were entropic in origin due to the steric hindrance experienced in the MOF environment. The effectiveness of linker substitution on catalytic efficiency has been shown in previous studies albeit not of biological relevance where the catalytic activity can be tuned by enhancements made to the metal-bound ligands.⁶⁹ The difference in the energy barriers for differing RSNO's led to the conclusion that varying the R-group and/or organic linker of the MOF has the potential to modulate the rate at which nitric oxide is released. A question that arises is whether the molecular structure of the RSNO species has an influence on the barriers of approach to the reactive site, in addition to the size of the R group.

Resulting from an interest in probing larger RSNOs, the need for a larger MOF arose and ultimately led to the utilization of MOF-143 (Figure 1b) in this work. MOF-143, like HKUST-1, is a copper based paddle wheel MOF with benzene and carboxylate containing linkers (Figure 2). The focal point of this work is to determine how modifications in the R-groups of the RSNO (present within the MOF pore) affect the catalytic activity of the copper sites and ultimately the release of nitric oxide. Therefore, classical molecular dynamics simulations (MD) simulations were performed and the results compared for different RSNO species in the MOF environment. Four biologically relevant RSNOs (Figure 3) including S-nitrosocysteine (CysNO), S-nitrosoglutathione (GSNO), S-Nitroso-N-Acetyl-D,L-Penicillamine (SNAP) and S-Nitroso-N-acetylcysteine (SNAC) were chosen since they are biologically compatible and in addition allow for the study of the effect of differences in chemical structure and size of the R group on the reaction. A modified version of the Dreiding force-field⁷⁰ was used in these simulations

and free energy calculations using the umbrella sampling method was carried out to probe the effect of the MOF environment as well as RSNO structure and size.

The paper is divided into four sections. The methodology is described briefly in section 2 and the results are discussed in section 3. The conclusions are presented in Section 4.

## 2. Models and Simulation Method

### 2.1 MOF Structure.
The crystal structure of MOF-143 was obtained from the group of Dr. Omar Yaghi. $^{71}$ MOF-143 consists of a 4,4',4''-benzene-1,3,5-triyl-tribenzoate (BTB) organic linker (see Figure 2) and copper metal center forming the copper paddle wheel structure with a pto topology unlike that of the tbo topology reported for the smaller analog HKUST-1. $^{72}$ The extended BTB linker leads to MOF-143 having a pore size diameter of $20.4\ \mathrm{\mathring{A}}$, $^{73}$ which is double that of HKUST-1. It should also be noted that the water oxygen atoms originally present in the obtained crystal structure have been removed in the simulations. In addition the system is connected periodically in all three dimensions to represent an infinite framework in the simulations. The dimensions of this cubic structure are $a$=$b$=$c$=$27.4719\ \mathrm{\mathring{A}}.^{73}$

### 2.2 Electronic Structure Calculations.
The partial charges on each RSNO was determined using CHELPG, an *ab initio* electrostatic potential fitting method, on the corresponding monomers (see Supporting Info S1). Similar calculations were carried out to determine the charge on CysNO and ethanol in previous work by Li et al. $^{1}$ To obtain

charges for MOF-143, electronic structure calculations using the same CHELPG method were performed on a representative cluster (see Figure 4) with Cu(II) based on the work by Zhao et al on HKUST-1.⁷⁴ The partial charges for the MOF-143 system are shown in Table 1. The charge for Cu(II) was found to be 1.08 e from CHELPG calculations. Shown in previously published work by Li et al.,¹ the role of the thiol is to reduce Cu(II) to Cu(I) and thus scrutiny of copper's charge is important. To further demonstrate that the loss of charge occurs at the metal center, the cluster was also probed with copper in the +1 oxidation state resulting in a highly charged system (-6 e) that is neutralized with the addition of 6 sodium ions (see Figure 4 b). Results from this show a charge of -0.007, nearly a -1.0 reduction in charge at the copper center from the initial charge whereas the O atoms remain essentially the same as before. Hence the same charges that are used for the Cu(II) sites in the MOF are used in the Cu(I) site except for the Cu(I) now having a charge of .08 e (as opposed to the 1.08 e charge at the Cu(II) site).

Electronic structure calculations in this work were performed using the Gaussian09⁷⁵ suite at the DFT level of theory,⁷⁶ using the B3LYP functional. For the different RSNO species the 6-311G(d,p) basis set was used whereas for the MOF calculations a mixed basis set consisting of LANL2DZ⁷⁷ for copper and 6-311G(d,p) for all the remaining atoms was used.

### 2.3 Condensed phase MD simulations.

Electronic structure calculations performed in previous work revealed that both Cu(I) as well as $[\mathrm{Cu(II)-SR}]^{+}$, with the RS-species coming from the thiol RSH, can act as reactive

centers.¹ In both cases the release of the NO moiety takes place as an RSNO species approaches the reactive site. This suggests that a suitable collective variable for this study is the Cu---S distance. It should be emphasized this work does not use a reactive model but rather focuses on the barriers that arise from the approach of the RSNO species to the copper site and to probe the possible effect of the environment on the reaction rate. Four RSNO species were studied, namely CysNO, SNAP, SNAC and GSNO.

In an effort to account for an array of potential pathways and thus reaction rates three sets of simulations were performed for each RSNO in the presence of the MOF. The study began with one RSNO (1RSNO) approaching the copper center (reduced to Cu(I)), once bound at the copper center a second set of simulations with a second RSNO (2RSNO) approaching the same copper center (Cu1) was studied. This latter case while interesting in itself, is a also a good approximation to understand the barriers associated with the approach of an RSNO species to $[Cu(II)-SR]^+$, the other potential reactive site in addition to Cu+. In addition, the approach of the second RSNO (RSNO2) to the adjacent copper center (referred to as Cu2, see Figure 5), which is also reduced to Cu(I) in these simulations, was also studied.

The first set of MOF simulations included the addition of one RSNO and 200 ethanol molecules in MOF-143 in a periodic cubic box length of 28 Å. One of the twelve equivalent coppers was selected as the 'reactive site' and was reduced to Cu(I), as was done in the previous study.¹ Again it was necessary to remove ethanol molecules in order to add a second RSNO molecule into the system. For the third set of simulations, the

copper site adjacent to the first reactive site was also reduced to the +1 oxidation state (see Figures 5 and 6). In addition to these, mixed RSNO simulations consisting of CysNO and GSNO were also carried out using the same scheme described above.

Free energy calculations. Umbrella sampling (US) simulations, $^{78}$ an enhanced sampling method along with the weighted histogram method (WHAM) $^{79,80}$ were used to ascertain the free energy profiles related to the above systems as a function of the Cu---S(from the SNO moiety of the RSNO) distance. 17 US simulation windows spanning the reaction coordinate $(r_{Cu-S})$ from 1.8 to $7\ \text{\AA}$ was used with a force constant of $35,000\ \text{kcal mol}^{-1}\ \text{nm}^{-2}$.

Force-field for simulations: The intermolecular interactions include the Coulomb interactions between the partial charges on the atomic sites as well as van der Waals interactions, represented using Lennard-Jones potentials. The present work includes the use of the Lennard Jones parameters obtained in previous work through electronic structure calculations for the interactions between $Cu(I)/CH_{3}SNO$ and extrapolates them for the interaction of the -CSNO group of GSNO, CysNO, SNAP and SNAC molecules with the copper (I) ion (Table 2). All other Lennard-Jones interactions are treated with the Dreiding force field. $^{70}$ Furthermore, the intramolecular parameters for the MOF were obtained from the work of Zhao and co-workers $^{74,81}$ and those of the remaining molecules with the Dreiding force-field.

All simulations were performed using the GROMACS package⁸² with periodic boundary conditions in the NPT ensemble, with a time step of 0.5 fs, at a temperature of 300K and a pressure of 1 bar using a Nose-Hoover thermostat and Parrinello-Rahman Barostat, respectively. Long-range electrostatics were addressed using the smoothed particle mesh Ewald (SPME) algorithm.⁸³ The real space cutoff distance used was 9 Å and van der Waals interaction cutoff was set at 12 Å. Each MOF simulation (including each Umbrella Sampling window) was allowed to equilibrate for 30 ns and subsequently a 60 ns production run was carried out. The error bars for the free energy profiles from the Umbrella Sampling simulations were calculated using the block averaging method with a total of six blocks per profile, each of length 10 ns.

### 3. Results and Discussion

As mentioned in the introduction, the primary goal of this work is to understand the factors that can control the slow and sustained release of nitric oxide from RSNO species in the Cu based MOF environment, thereby enabling the design of nitric oxide delivery systems with targeted release rates. Secondly, work contained herein investigates how the size and chemical composition of the RSNO species can further affect the free energy barriers associated with the approach towards the catalytic centers. In previous computational work Li, Edinbyrd and Kumar studied the reaction in the Cu-based HKUST MOF. In the current study, a Cu-based MOF with longer organic linker arms is considered. In addition, in order to study the effect of the R group in the RSNO species, four different R groups were chosen, namely cysteine, SNAP and SNAC (which are of comparable size but different chemical structure) and the much larger glutathione moiety.

All four are biologically compatible RSNO species and hence can be used in the nitric oxide delivery system discussed in this work. As mentioned in the previous section electronic structure calculations have shown that the approach of the RSNO group to the Cu(I) site or $(Cu(II)-\text{--}-SR)^+$ site results in the cleavage of the S-N bond, and hence the Cu---S distance is an appropriate reaction coordinate or collective variable to probe the barriers for the approach of the RSNO species to the reactive site using umbrella sampling. The difference in the free energy barriers encountered by the various RSNO species for different cases in the MOF environment is compared. It should be emphasized that these simulations are not reactive and hence cannot provide an accurate description in the regime where the actual cleavage of the S---N bond takes place. The purpose of this work is to study the different barriers for the approach of the RSNO species to the active copper site.

### 3.1 MOF simulations.

The approach of the first RSNO (labeled 1RSNO) in all four cases results in a free energy profile that has a relatively small barrier (Figure 7). Despite the chemical similarity between SNAP, SNAC and CysNO, the free energy profiles for SNAP shows a slight barrier that is not present for the 1CysNO case. Upon the addition of the second RSNO (labeled 2RSNO) drastic changes are observed when the second RSNO approaches the copper site to which 1RSNO is bound. Here SNAC shows the highest barrier at approximately $18\ \text{kcal mol}^{-1}$ despite being the second smallest RSNO, only slightly larger than CysNO by the addition of an acetyl group at the amine site. The barrier for the

CysNO case also displays a large barrier of 15 kcal mol⁻¹ in spite of being the smallest RSNO of the series. Although SNAP is the second to largest RSNO behind GSNO, the approach of 2SNAP results in a barrier of only 10 kcal mol⁻¹. Interestingly, SNAP and SNAC differ by the addition of two methyl groups located on the alpha-carbon of SNAP but absent in SNAC. Approach of 2GSNO portrays a surprisingly small barrier that is similar to the 1GSNO case. On the other hand, the free energy profile for the approach of the second RSNO (labeled RSNO2) towards the adjacent copper (in which 1RSNO is bound to the original copper) is quite similar to that of the 1RSNO cases for CysNO, SNAP and SNAC. The reverse is true for the GSNO case. Intriguingly, the advancement of GSNO2 towards the adjacent copper yields a large free energy barrier with respect to the 1GSNO case. It is also noteworthy to further compare results of SNAC versus that of CysNO and SNAP. The similarities in size and makeup of SNAC to SNAP likely result in the qualitative likeness of their RSNO2 free energy profiles. However, the resemblance of the free energy barriers of 2SNAC to 2CysNO rather than the 2SNAP case can be attributed to the difference in structure, mainly the absence of two methyl groups (at the alpha-carbon with respect to the nitroso group) for SNAC, a primary RSNO like CysNO as opposed to SNAP (a tertiary RSNO).

To gather further insight into the effects of the MOF environment on the RSNO species approach towards the copper, information on the solvation environment around the copper site was probed.

Figure 8 shows the Cu---O(from ethanol) radial distribution function for the various RSNO species for different Cu---S (from the SNO group) distances and Figure 9 shows the corresponding integrated coordination number. A change of -1 for the coordination number of ethanol to the catalytically active copper is observed as 1CysNO approaches a bond distance of approximately 2 Å to the copper ion (Figure 9). Although slightly larger in size, both the SNAP and SNAC systems see a similar net decrease in coordination of ethanol to copper. To further assess how the second RSNO approaches the Cu1 center for these systems, the distribution of the $S_1$-Cu-$S_2$ angle (see Figure 10) was calculated at an umbrella-sampling window of $r_{Cu-S}$ of 2 Å (the S from 2RSNO, the case where both RSNO species approach the same copper ion). From this data it is apparent that the $S_1$-Cu-$S_2$ angle of 2CysNO has a narrow distribution for its angle of approach with a peak at around $75^o$. This explains the appearance of the shoulder in the Cu----O(from ethanol) radial distribution function for MOF-143—2CysNO (Figure 8) where the small approach angle allows an additional ethanol to move between the first and second solvation shells (Figure 9, 10). The $S_1$-Cu-$S_2$ angle (Figure 10) of 2SNAP is slightly larger than that of 2CysNO and hence more restrictive in allowing ethanol to insert itself between the first and second solvation shell.. Lastly, the wide range of angles that 2SNAC and 2GSNO takes on is likely due to the availability of space as 2SNAC begins pushing the initial RSNO molecule away from the catalytic center at Cu---S(2RSNO) ~2.7 Å and for the 2GSNO case at 7 Å.

Examination of the solvation environment of 2SNAC, like 2CysNO, also shows that an ethanol molecule is present between the first and second solvation shell as is apparent by

the shoulder observed in the radial distribution function in Figure 8 for $r_{Cu-S}$ constrained to 3 and 4 Å. The approach of 2SNAC sees a reduction in coordination number at 3 and 4 Å; however, an increase in coordination to three is observed at a $r_{Cu-S}$ of ~2 Å, which is the result of 1SNAC being pushed away from the catalytic copper center which in turn allows additional coordination of ethanol to copper. The enthalpic penalty associated with the disruption of the solvation shell can be attributed to the higher barrier of approach seen in the free energy profile of 2SNAC. The coordination within the first solvation shell of 2SNAC is affected more than that of 2CysNO, resulting in a barrier larger than 2CysNO.

The approach of GSNO is quite dissimilar to that of CysNO, SNAP and SNAC. In the latter cases, the three RSNO moieties are small enough that two can occupy the pore simultaneously, but the steric hindrance results in higher barriers for the 2RSNO systems. In the GSNO case, only one GSNO moiety can coordinate to a copper site resulting in the bound GSNO being pushed away from the Cu1 ion when the second GSNO approaches the site. The approach of GSNO2 towards the adjacent copper center does see a reduction in coordination number for a net of two ethanol molecules removed from the coordination shell of the Cu1 site, similar to that of the 2CysNO, 2SNAP and 2SNAC cases. Here a high-energy barrier is seen unlike the RSNO2 cases of CysNO, SNAP and SNAC.

The high-energy barrier for the GSNO2 case arises because a second ethanol is pushed away from the Cu1 site so that GSNO2 can approach the adjacent catalytic center thereby

allowing both GSNOs to be near each other. On the other hand, for the 2GSNO case when the second GSNO approaches the same copper that is already bound to the first GSNO, the latter is pushed to over 13 Å away from the catalytic copper center even when the second GSNO is 7 Å away. To further validate the identical PMFs for 1GSNO and 2GSNO, the radial distribution functions for both are nearly identical as well, suggesting that they experience the same solvation environment and nearly identical coordination numbers. To further understand how the approach if 2RSNO affects the initially bound RSNO, the distance that 1RSNO is pushed from the copper center is shown in Figure 11.

To understand the cause of 1SNAC being pushed relatively far from the catalytic center upon the approach of 2SNAC (as compared to the approach of SNAP), the O(from ethanol)—O (of the 1RSNO carboxylic acid group) radial distribution function was calculated (Figure 12) for both SNAP and SNAC. By computing the coordination numbers (Figure 13) associated with the radial distribution function of Figure 12, it is apparent that SNAC has a tendency to be more solvated by ethanol than SNAP molecules. Due to the solvophillic nature of SNAC, it likely prefers to be away from the catalytic copper center to maximize the number of ethanol molecules coordinated to it.

### 3.2 Mixed RSNO-MOF
To further understand the effects of modifying R-groups of the RSNOs, a mixed RSNO system was simulated within MOF-143. Due to the substantial size difference in CysNO and GSNO, these two were chosen for comparison with identical RSNOs. Two scenarios were investigated: firstly, CysNO bound to the copper and allowing GSNO to

approach the identical copper (Cu1) and the adjacent copper (Cu2), referred to as CPG, secondly where GSNO is initially bound to copper and CysNO approaches Cu1 as well as Cu2, referred to as GPC.

Free energy profiles: The resulting free energy profiles are quite similar for the 2RSNO systems for both scenarios (Figure 14), namely where the RSNO moieties go to the same copper site. Scrutiny of CPG-2RSNO where CysNO is bound to copper and the GSNO is translocated towards the same copper looks somewhat similar to the profile obtained for MOF-143-1CysNO until approximately 3 Å. It is noteworthy to mention that CysNO stays bound to copper up until this distance and begins to be pushed away from this point on in CPG-2RSNO. On the other hand, for the GPC-2RSNO case the GSNO moiety is pushed out when the CysNO approaches the copper site. Essentially the 2RSNO case for both the CPG and GPC systems results in essentially the bound RSNO being pushed away when the second RSNO approaches the copper site.

Strikingly, it is observed that the approach of the second RSNO towards the adjacent copper (Cu2) leads to substantially different energy profiles when comparing both RSNOs. In the studies involving the approach of RSNO to the adjacent Cu2 site (RSNO2), a relatively lower free energy profile is observed for the case where CysNO is bound to Cu1 and GSNO approaches Cu2, the adjacent copper center (CPG-RSNO2). A different profile is seen for the case where GSNO is bound to the Cu1 site and the approach of CysNO occurs towards the adjacent Cu2 center (GPC-RSNO2). To explain this disparity between both systems, visual analysis of the immediate environment

revealed that the orientation of GSNO played a substantial role in these results. CPG-
RSNO2 simulations result in GSNO being bound to the Cu2 site while CysNO is
displaced to approximately 11 Å away from Cu1. Moreover, GPC-RSNO2 simulations
show that the Cu---S distance for GSNO and CysNO are 2.0 Å and 2.5 Å, respectively.
From this it is apparent that the approach of GSNO (CPG, Figure 15) to the same copper
causes CysNO to be pushed away and is likely due to the need for this large molecule
(GSNO) to reorient as it approaches the copper center (Figure 15), unlike the GPC-
RSNO2 case where the much smaller CysNO approaches the copper adjacent to the
GSNO bound copper.

### 4.1 Conclusion.
The effects of the MOF environment and the varying of R-groups within the RSNO
species were investigated in an effort to understand the process of nitric oxide release
through a copper catalyst. Through classical molecular dynamics simulations the process
in which RSNOs approach copper centers revealed information relevant to the chemical
storage and delivery of nitric oxide. Studies within this work suggests a range of reaction
pathways resulting in multiple release rates of nitric oxide and is illustrated by the
varying approach of the RSNO towards the copper center and their subsequent free
energies. While previously it was presumed that changes in pore size and R-group were
reliable predictors in free energy trends and thus nitric oxide delivery, results herein
discern the processes involved but ultimately depict that RSNO size alone is an
insufficient predictor. It is clear that the chemical structure can also play a role in the
reactivity of the RSNO species as slight changes in the chemical makeup of CysNO,

SNAP and SNAC results in free energy barriers that are quite distinct for CysNO and SNAP but are intermediary for SNAC as its approach can mimic that of both CysNO and SNAP. As such, the overlap of properties for SNAC can be attributed to the likeness in chemical structure to both CysNO and SNAP. It is possible that tuning of RSNO reactivity can be made possible through modifications to the RSNO structure and/or size. In this work the addition of an acetyl group to CysNO has implied a decreased rate of NO release. Further modifications to the RSNO structure, while retaining similar size, in the form of methyl groups to SNAC suggest an increase in reactivity, evident by the lower free energy barrier of SNAP compared to CysNO, a smaller RSNO. Results show that essentially no barrier is observed for 1RSNO cases in the MOF systems; however, quite a distinction can be made once a subsequent RSNO approaches the copper site. The barriers for approach of various RSNO species, including mixed RSNOs, to the copper site in the MOF can be exploited for the manufacturing of nanomaterials capable of slow, sustained and controlled drug release of highly reactive molecules like that of nitric oxide. Existing and current work continue to suggest that nitric oxide generation can be modulated through the alteration of R-groups and organic linker size. While the current work looked at evaluating the barrier for approach of the RSNO species to the catalytic sites, future work will concentrate on developing reactive models based on the empirical valence bond formalism to study the reaction pathway.⁸⁴

### 5.1 Acknowledgements.

Work contained herein was funded under the NSF EPSCoR LA-SiGMA project under award #EPS-1003897, and a Louisiana Board of Regents (BOR RCS grant #

LEQSF(2014-17)-RD-A-02) along with the startup funds provided by the Department of Chemistry and the Center of Computation Technology at LSU. Taylor-Edinbyrd would like to acknowledge the NSF LSU Bridge to Doctorate Graduate Fellowship (NSF grant #1026662). The authors would also like to acknowledge the High Performance Computing Center at LSU and the Louisiana Optical Network Initiative for computer time. Lastly, the authors would like to thank the group of Dr. Omar Yaghi for providing the crystal structure of MOF-143 and Prof. Steven Rick and Prof. Anne Milet for helpful suggestions.

## References:

1.  T. Li, K. Taylor-Edinbyrd and R. Kumar, *Physical Chemistry Chemical Physics*, 2015, **17**, 23403-23412.

2.  L. M. Aguirre-Díaz, F. Gándara, M. Iglesias, N. Snejko, E. Gutiérrez-Puebla and M. Á. Monge, *Journal of the American Chemical Society*, 2015, **137**, 6132-6135.

3.  C. E. Wilmer, M. Leaf, C. Y. Lee, O. K. Farha, B. G. Hauser, J. T. Hupp and R. Q. Snurr, *Nat Chem*, 2012, **4**, 83-89.

4.  Y.-B. Zhang, H. Furukawa, N. Ko, W. Nie, H. J. Park, S. Okajima, K. E. Cordova, H. Deng, J. Kim and O. M. Yaghi, *Journal of the American Chemical Society*, 2015, **137**, 2641-2650.

5.  J. L. C. Rowsell and O. M. Yaghi, *Microporous and Mesoporous Materials*, 2004, **73**, 3-14.

6.  Y. J. Colon and R. Q. Snurr, *Chemical Society Reviews*, 2014, **43**, 5735-5749.

7.  G. R. Jenness and J. R. Schmidt, *ACS Catalysis*, 2013, **3**, 2881-2890.

8.  A. H. Chughtai, N. Ahmad, H. A. Younus, A. Laypkov and F. Verpoort, *Chemical Society Reviews*, 2015, **44**, 6804-6849.

9.  D. Yang, S. O. Odoh, T. C. Wang, O. K. Farha, J. T. Hupp, C. J. Cramer, L. Gagliardi and B. C. Gates, *Journal of the American Chemical Society*, 2015, **137**, 7391-7396.

10. Y. He, W. Zhou, G. Qian and B. Chen, *Chemical Society Reviews*, 2014, **43**, 5657-5678.

11. Y.-S. Bae, B. G. Hauser, O. K. Farha, J. T. Hupp and R. Q. Snurr, *Microporous and Mesoporous Materials*, 2011, **141**, 231-235.

12. E. Haldoupis, J. Borycz, H. Shi, K. D. Vogiatzis, P. Bai, W. L. Queen, L. Gagliardi and J. I. Siepmann, *The Journal of Physical Chemistry C*, 2015, **119**, 16058-16071.

13. J. G. McDaniel, S. Li, E. Tylianakis, R. Q. Snurr and J. R. Schmidt, *The Journal of Physical Chemistry C*, 2015, **119**, 3143-3152.

14. P. Canepa, N. Nijem, Y. J. Chabal and T. Thonhauser, *Physical Review Letters*, 2013, **110**, 026102.

15. J. G. Vitillo, L. Regli, S. Chavan, G. Ricchiardi, G. Spoto, P. D. C. Dietzel, S. Bordiga and A. Zecchina, *Journal of the American Chemical Society*, 2008, **130**, 8386-8396.

16. P. Canepa, C. A. Arter, E. M. Conwill, D. H. Johnson, B. A. Shoemaker, K. Z. Soliman and T. Thonhauser, *Journal of Materials Chemistry A*, 2013, **1**, 13597-13604.

17. J.-R. Li, R. J. Kuppler and H.-C. Zhou, *Chemical Society Reviews*, 2009, **38**, 1477-1504.

18. H. Alawisi, B. Li, K. Alfooty, L. Wu, S. Xiang, H. Wang and B. Chen, *Inorganic Chemistry Communications*, 2014, **50**, 106-109.

19. Y.-S. Bae, K. L. Mulfort, H. Frost, P. Ryan, S. Punnathanam, L. J. Broadbelt, J. T. Hupp and R. Q. Snurr, *Langmuir*, 2008, **24**, 8592-8598.

20. K. C. Kim, C. Y. Lee, D. Fairen-Jimenez, S. T. Nguyen, J. T. Hupp and R. Q. Snurr, *The Journal of Physical Chemistry C*, 2014, **118**, 9086-9092.

21. P. Verma, X. Xu and D. G. Truhlar, *The Journal of Physical Chemistry C*, 2013, **117**, 12648-12660.

22. N. Nijem, H. Wu, P. Canepa, A. Marti, K. J. Balkus, T. Thonhauser, J. Li and Y. J. Chabal, *Journal of the American Chemical Society*, 2012, **134**, 15201-15204.

23. X.-Q. Wu, J.-G. Ma, H. Li, D.-M. Chen, W. Gu, G.-M. Yang and P. Cheng, *Chemical Communications*, 2015, **51**, 9161-9164.

24. M. D. Allendorf, R. J. T. Houk, L. Andruszkiewicz, A. A. Talin, J. Pikarsky, A. Choudhury, K. A. Gall and P. J. Hesketh, *Journal of the American Chemical Society*, 2008, **130**, 14404-14405.

25. L. E. Kreno, K. Leong, O. K. Farha, M. Allendorf, R. P. Van Duyne and J. T. Hupp, *Chemical Reviews*, 2012, **112**, 1105-1125.

26. X. Wang, X. Lu, L. Wu and J. Chen, *Biosensors and Bioelectronics*, 2015, **65**, 295-301.

27. Y. Liu, S.-Y. Moon, J. T. Hupp and O. K. Farha, *ACS Nano*, 2015, **9**, 12358-12364.

28. J. B. DeCoste, T. J. Demasky, M. J. Katz, O. K. Farha and J. T. Hupp, *New Journal of Chemistry*, 2015, **39**, 2396-2399.

29. J. E. Mondloch, M. J. Katz, W. C. Isley Iii, P. Ghosh, P. Liao, W. Bury, G. W. Wagner, M. G. Hall, J. B. DeCoste, G. W. Peterson, R. Q. Snurr, C. J. Cramer, J. T. Hupp and O. K. Farha, *Nat Mater*, 2015, **14**, 512-516.

30. R. Grunker, V. Bon, P. Muller, U. Stoeck, S. Krause, U. Mueller, I. Senkovska and S. Kaskel, *Chemical Communications*, 2014, **50**, 3450-3452.

31. O. K. Farha, A. Özgür Yazaydın, I. Eryazici, C. D. Malliakas, B. G. Hauser, M. G. Kanatzidis, S. T. Nguyen, R. Q. Snurr and J. T. Hupp, *Nat Chem*, 2010, **2**, 944-948.

32. H. Furukawa, N. Ko, Y. B. Go, N. Aratani, S. B. Choi, E. Choi, A. Ö. Yazaydin, R. Q. Snurr, M. O'Keeffe, J. Kim and O. M. Yaghi, *Science*, 2010, **329**, 424-428.

33. N. Chang, Z.-Y. Gu, H.-F. Wang and X.-P. Yan, *Analytical Chemistry*, 2011, **83**, 7094-7101.

34. A. Lowe, P. Chittajallu, Q. Gong, J. Li and K. J. Balkus Jr, *Microporous and Mesoporous Materials*, 2013, **181**, 17-22.

35. A. C. McKinlay, P. K. Allan, C. L. Renouf, M. J. Duncan, P. S. Wheatley, S. J. Warrender, D. Dawson, S. E. Ashbrook, B. Gil, B. Marszalek, T. Düren, J. J. Williams, C. Charrier, D. K. Mercer, S. J. Teat and R. E. Morris, *APL Mater.*, 2014, **2**, 124108.

36. C. Orellana-Tavra, E. F. Baxter, T. Tian, T. D. Bennett, N. K. Slater, A. K. Cheetham and D. Fairen-Jimenez, *Chemical Communications*, 2015, **51**, 13878-13881.

37. C.-Y. Sun, C. Qin, X.-L. Wang and Z.-M. Su, *Expert opinion on drug delivery*, 2013, **10**, 89-101.

38. D. A. Riccio and M. H. Schoenfisch, *Chemical Society Reviews*, 2012, **41**, 3731-3741.

39. J. L. Harding and M. M. Reynolds, *Journal of Materials Chemistry B*, 2014, **2**, 2530-2536.

40. K. Matsuyama, N. Hayashi, M. Yokomizo, T. Kato, K. Ohara and T. Okuyama, *Journal of Materials Chemistry B*, 2014, **2**, 7551-7558.

41. H. A. Liu and K. J. Balkus, *Chemistry of Materials*, 2009, **21**, 5032-5041.

42. S. H. Abman, in *Pharmacotherapy of Pulmonary Hypertension*, eds. M. Humbert, V. O. Evgenov and J.-P. Stasch, Springer Berlin Heidelberg, Berlin, Heidelberg, 2013, DOI: 10.1007/978-3-642-38664-0_11, pp. 257-276.

43. D. P. Casey, B. G. Walker, S. M. Ranadive, J. L. Taylor and M. J. Joyner, *Journal of Applied Physiology*, 2013, **115**, 446-455.

44. H. Prast and A. Philippu, *Progress in Neurobiology*, 2001, **64**, 51-68.

45. K. Raju, P.-T. Doulias, P. Evans, E. N. Krizman, J. G. Jackson, O. Horyn, Y. Daikhin, I. Nissim, M. Yudkoff, I. Nissim, K. A. Sharp, M. B. Robinson and H. Ischiropoulos, *Science signaling*, 2015, **8**, ra68-ra68.

46. G. Farrugia and J. H. Szurszewski, *Gastroenterology*, 2014, **147**, 303-313.

47. A. Blum, *Coronary artery disease*, 2015, **26**, 639-641.

48. A. Tanaka and K. Node, *Hypertension Research*, 2015, **38**, 461-462.

49. R. Knowles, M. Chan, M. Hayman, P. Armstrong, A. Tucker, A. Timmis and T. Warner, *Heart*, 2015, **101**, A90-A91.

50. K. Sharma and H. Chakrapani, *Nitric Oxide*, 2014, **43**, 8-16.

51. Y. Lu, A. Shah, R. A. Hunter, R. J. Soto and M. H. Schoenfisch, *Acta biomaterialia*, 2015, **12**, 62-69.

52. B. V. Worley, D. L. Slomberg and M. H. Schoenfisch, *Bioconjugate chemistry*, 2014, **25**, 918-927.

53. Y. Lu, D. L. Slomberg and M. H. Schoenfisch, *Biomaterials*, 2014, **35**, 1716-1724.

54. P. D. M. Amedea B. Seabra, Larissa B. de Paula, and N. Durán, *Journal of Nano Research*, 2012, **20**, 61-67.

55. Y. S. Jo, A. J. van der Vlies, J. Gantz, T. N. Thacher, S. Antonijevic, S. Cavadini, D. Demurtas, N. Stergiopulos and J. A. Hubbell, *Journal of the American Chemical Society*, 2009, **131**, 14413-14418.

56. P. Taladriz-Blanco, V. Pastoriza-Santos, J. Pérez-Juste and P. Hervés, *Langmuir*, 2013, **29**, 8061-8069.

57. E. D. Bloch, W. L. Queen, S. Chavan, P. S. Wheatley, J. M. Zadrozny, R. Morris, C. M. Brown, C. Lamberti, S. Bordiga and J. R. Long, *Journal of the American Chemical Society*, 2015, **137**, 3466-3469.

58. P. Horcajada, R. Gref, T. Baati, P. K. Allan, G. Maurin, P. Couvreur, G. Férey, R. E. Morris and C. Serre, *Chemical Reviews*, 2012, **112**, 1232-1268.

59. J. Kim, G. Saravanakumar, H. W. Choi, D. Park and W. J. Kim, *Journal of Materials Chemistry B*, 2014, **2**, 341-356.

60. A. C. McKinlay, J. F. Eubank, S. Wuttke, B. Xiao, P. S. Wheatley, P. Bazin, J. C. Lavalley, M. Daturi, A. Vimont, G. De Weireld, P. Horcajada, C. Serre and R. E. Morris, *Chemistry of Materials*, 2013, **25**, 1592-1599.

61. D. Cattaneo, S. J. Warrender, M. J. Duncan, C. J. Kelsall, M. K. Doherty, P. D. Whitfield, I. L. Megson and R. E. Morris, *RSC Advances*, 2016, **6**, 14059-14067.

62. R. C. Huxford, J. D. Rocca and W. Lin, *Current opinion in chemical biology*, 2010, **14**, 262-268.

63. K. Peikert, L. J. McCormick, D. Cattaneo, M. J. Duncan, F. Hoffmann, A. H. Khan, M. Bertmer, R. E. Morris and M. Fröba, *Microporous and Mesoporous Materials*, 2015, **216**, 118-126.

64. J. L. Harding and M. M. Reynolds, *Journal of the American Chemical Society*, 2012, **134**, 3330-3333.

65. J. M. Tullett, D. D. Rees, D. E. Shuker and A. Gescher, *Biochemical pharmacology*, 2001, **62**, 1239-1247.

66. B. Meyer, A. Genoni, A. Boudier, P. Leroy and M. F. Ruiz-Lopez, *The Journal of Physical Chemistry A*, 2016, **120**, 4191-4200.

67. R. J. Singh, N. Hogg, J. Joseph and B. Kalyanaraman, *Journal of Biological Chemistry*, 1996, **271**, 18596-18603.

68. T. D. Kühne, *Wiley Interdisciplinary Reviews: Computational Molecular Science*, 2014, **4**, 391-406.

69. X. Li, R. Van Zeeland, R. V. Maligal-Ganesh, Y. Pei, G. Power, L. Stanley and W. Huang, *ACS Catalysis*, 2016, **6**, 6324-6328.

70. S. L. Mayo, B. D. Olafson and W. A. Goddard, *The Journal of Physical Chemistry*, 1990, **94**, 8897-8909.

71. H. Furukawa, Y. B. Go, N. Ko, Y. K. Park, F. J. Uribe-Romo, J. Kim, M. O'Keeffe and O. M. Yaghi, *Inorganic Chemistry*, 2011, **50**, 9147-9152.

72. D. J. Clingerman, W. Morris, J. E. Mondloch, R. D. Kennedy, A. A. Sarjeant, C. Stern, J. T. Hupp, O. K. Farha and C. A. Mirkin, *Chemical Communications*, 2015, **51**, 6521-6523.

73. H. Furukawa, K. E. Cordova, M. O'Keeffe and O. M. Yaghi, *Science*, 2013, **341**.

74. L. Zhao, Q. Yang, Q. Ma, C. Zhong, J. Mi and D. Liu, *Journal of Molecular Modeling*, 2011, **17**, 227-234.

75. M. Frisch, G. Trucks, H. Schlegel, G. Scuseria, M. Robb, J. Cheeseman, J. Montgomery, T. Vreven, K. Kudin and J. Burant, 2008.

76. R. G. Parr, *Annual Review of Physical Chemistry*, 1983, **34**, 631-656.

77. Y. Yang, M. N. Weaver and K. M. Merz, *The journal of physical chemistry. A*, 2009, **113**, 9843-9851.

78. J. Kästner, *Wiley Interdisciplinary Reviews: Computational Molecular Science*, 2011, **1**, 932-942.

79. S. Kumar, J. M. Rosenberg, D. Bouzida, R. H. Swendsen and P. A. Kollman, *Journal of computational chemistry*, 1992, **13**, 1011-1021.

80. M. Souaille and B. t. Roux, *Computer physics communications*, 2001, **135**, 40-57.

81. Q. Yang and C. Zhong, *The Journal of Physical Chemistry B*, 2006, **110**, 17776-17783.

82. S. Pronk, S. Páll, R. Schulz, P. Larsson, P. Bjelkmar, R. Apostolov, M. R. Shirts, J. C. Smith, P. M. Kasson, D. van der Spoel, B. Hess and E. Lindahl, *Bioinformatics*, 2013, **29**, 845-854.

83. U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen, *The Journal of Chemical Physics*, 1995, **103**, 8577-8593.

84. A. Warshel and R. M. Weiss, *Journal of the American Chemical Society*, 1980, **102**, 6218-6226.

![](./images/811035854578384897_3.jpg)

Figure 1. Shows the (a) HKUST-1 MOF (b) MOF-143, an analog of HKUST-1 that has an extended linker leading to a large pore. Atomic representation is as follows: carbon (cyan and pink), oxygen (red), hydrogen (white) and copper (orange).

![](./images/811035854578384897_4.jpg)

Figure 2. MOF-143 BTB Linker. Atomic representation is as follows: carbon (cyan), oxygen (red) and hydrogen (white).

![](./images/811035854578384897_5.jpg)

Figure 3. Images of CysNO, SNAP, SNAC and GSNO for comparison.

![](./images/811035854578384897_6.jpg)

Figure 4. a) The representative cluster for MOF-143 and b) representative cluster capped with sodium ions for the Cu(I) site of MOF-143. Atomic representation is as follows: carbon (grey), oxygen (red), copper (orange), hydrogen (white) and sodium (violet).

![](./images/811035854578384897_7.jpg)

**Figure 5.** Figure reproduced from previous work.¹ Shows the two catalytic copper sites present on each arm of the MOF. For the 1RSNO simulations: Cu 1 is reduced to the I oxidation state and the first RSNO approaches the copper site. 2RSNO: With the 1ˢᵗ RSNO coordinated to the Cu 1 site, a second RSNO (2RSNO) approaches the same copper (Cu 1). RSNO2: Cu 2 is now **also** reduced to the I oxidation state and the 1ˢᵗ RSNO is coordinated to Cu1; however, the second RSNO (RSNO2) is now approaching the adjacent copper (Cu 2). Atomic representation is as follows: carbon (cyan), oxygen (red) and copper (orange).

![](./images/811035854578384897_8.jpg)

Figure 6. (Left) Illustration depicts the system with one RSNO near Cu(I) (1RSNO), (Right) depicts the second RSNO (RSNO2) towards the adjacent copper (Cu2) with the first RSNO bound to Cu 1. Atomic representation is as follows: carbon (cyan and pink), oxygen (red), hydrogen (white), sulfur (yellow), dark blue (nitrogen) and copper (blue spheres).

![](./images/811035854578384897_9.jpg)

Figure 7. Free energy profile as a function of $r_{Cu-S}$ within the MOF
environment for CysNO, SNAP, SNAC and GSNO.

![](./images/811035854578384897_10.jpg)

Figure 8. Cu---O (from ethanol) radial distribution function for the different RSNO cases in the MOF environment for different US windows (corresponding to different Cu(I)—S distances). Topmost panel shows the CysNO case, the top middle panel is for SNAP, the lower middle panel is for SNAC and the lower panel is for GSNO.

![](./images/811035854578384897_11.jpg)

Figure 9. Integrated coordination numbers for ethanol molecules coordinated around copper in the MOF environment for different US windows (corresponding to different Cu(I)—S distances). Topmost panel shows the CysNO case, the upper middle panel is for SNAP, the lower middle panel is for SNAC and the lower panel for GSNO.

![](./images/811035854578384897_12.jpg)

Figure 10. Distribution of the $S_1$-Cu-$S_2$ angle from the umbrella-sampling
window of $r_{Cu-S}$ of $2$ Å (the S from 2RSNO, the case where both
RSNO species approach the same copper ion).

![](./images/811035854578384897_13.jpg)

Figure 11. The Cu---S(from 1RSNO) distance plotted as a function of the Cu---S(from 2RSNO)_ distance for different RSNO species: 2CysNO (black circles) 2SNAP (red squares) 2SNAC (green dot dash) and 2GSNO (blue triangles).

![](./images/811035854578384897_14.jpg)

Figure 12. Radial distribution function for the carboxylic acid oxygen (O_c) of RSNO
with the ethanol oxygen (O_t) of (top) SNAP and (bottom) SNAC.

![](./images/811035854578384897_15.jpg)

Figure 13. The coordination number for the carboxylic acid oxygen $(O_c)$ of 1RSNO with the ethanol oxygen $(O_t)$ of (solid lines) SNAP and (dashed-dotted lines) SNAC.

![](./images/811035854578384897_16.jpg)

Figure 14. Free energy profile for mixed MOF simulations :(left) CysNO bound to copper while GSNO approaches the copper site (CPG case); (right) GSNO bound to copper as CysNO approaches the copper site (GPC case).

![](./images/811035854578384897_17.jpg)

Figure 15. Illustrates the orientation of both CysNO and GSNO in the MOF-mixed-RSNO simulation for the RSNO2 scenario. Only the RSNO and copper sites are shown for clarity Left: shows the resulting orientation of CysNO at the copper center and GSNO approaching Cu2, the adjacent center, pushing away CysNO (CPG case). Right: shows the resulting orientation for GSNO at the copper center and CysNO approaching Cu2, the adjacent copper (GPC case). Atomic representation is as follows: carbon (cyan), oxygen (red), hydrogen (white), nitrogen (dark blue), sulfur (yellow) and copper (cyan spheres with orange outline).

![](./images/811035854578384897_18.jpg)

Table of contents image

<table>
  <thead>
    <tr>
      <th>Atom Type</th>
      <th>Charge (e)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cu</td>
      <td>1.080</td>
    </tr>
    <tr>
      <td>O</td>
      <td>-0.731</td>
    </tr>
    <tr>
      <td>C(1)</td>
      <td>0.866</td>
    </tr>
    <tr>
      <td>C(2)</td>
      <td>-0.119</td>
    </tr>
    <tr>
      <td>C(3)</td>
      <td>-0.052</td>
    </tr>
    <tr>
      <td>H</td>
      <td>0.110</td>
    </tr>
  </tbody>
</table>

Table 1: Partial charges on the MOF-143 system. C(1) refers to the oxalate carbon, C(2) to the carbon connected to the oxalate and C(3) to the remaining carbon atoms.

<table>
  <thead>
    <tr>
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CH₃SNO</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Cu-CH₃</th>
      <td>3.5 x 10⁻⁴</td>
      <td>3.1 x 10⁻¹</td>
    </tr>
    <tr>
      <th>Cu-S</th>
      <td>4.9 x 10⁻⁷</td>
      <td>1.7 x 10⁻²</td>
    </tr>
    <tr>
      <th>Cu-N</th>
      <td>3.2 x 10⁻⁵</td>
      <td>1.1 x 10⁻¹</td>
    </tr>
    <tr>
      <th>Cu-O</th>
      <td>2.1 x 10⁻⁹</td>
      <td>5.2 x 10⁻¹</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>EtOH</th>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Cu-CH₂</th>
      <td>1.0 x 10⁻⁴</td>
      <td>1.9 x 10⁻¹</td>
    </tr>
    <tr>
      <th>Cu-O</th>
      <td>1.5 x 10⁻⁹</td>
      <td>1.6 x 10⁻⁴</td>
    </tr>
    <tr>
      <th>Cu-H</th>
      <td>1.5 x 10⁻⁶</td>
      <td>1.7 x 10⁻²</td>
    </tr>
  </tbody>
</table>

Table 2. A list of the van der Waals parameters for the non-bonded interactions. All remaining parameters were obtained from the Dreiding force field. Units: A is in kJ mol⁻¹ nm¹² and B is in kJ mol⁻¹ nm⁶