![](./images/812737131637112832_1.jpg)

Subscriber access provided by The University of Melbourne Libraries

C: Energy Conversion and Storage; Energy and Charge Transport

# Computational Insights into Working
Mechanism of LiPF6-Graphite Dual-Ion Battery

Sumit Kumar, Preeti Bhauriyal, and Biswarup Pathak

J. Phys. Chem. C, Just Accepted Manuscript • DOI: 10.1021/acs.jpcc.9b07046 • Publication Date (Web): 05 Sep 2019

Downloaded from pubs.acs.org on September 6, 2019

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

---

is published by the American Chemical Society. 1155 Sixteenth Street N.W.,
Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the
course of their duties.

# Computational Insights into Working Mechanism of $LiPF_6$-Graphite Dual-Ion Battery

Sumit Kumar, $^\dagger$ Preeti Bhauriyal, $^\dagger$ Biswarup Pathak, $^\dagger$,$^\#$,$^*$

$^\dagger$Discipline of Chemistry and $^\#$Discipline of Metallurgy Engineering and Materials Science,
Indian Institute of Technology (IIT) Indore, Indore. M.P. 453552, India
Email: biswarup@iiti.ac.in

## Abstract

The emerging field of dual-ion batteries (DIBs) show quite better advantages compared to the commercial Li-ion batteries. So, the on-going experimental studies of DIBs require a clear understanding of the reaction mechanism as well as the resulting structural variation in the involved anions and cathode system. Therefore, in this work using the first principle calculations, we have studied the intercalation mechanism of $PF_6^-$ intercalation from organic electrolyte into graphite. The intercalation energy characteristics indicate the favourable intercalation of $PF_6^-$ into graphite following the staging mechanism, also confirmed by X-ray diffraction simulations. $PF_6^-$ intercalation relatively acquiring small interlayer distance in graphite than $AlCl_4^-$ and $FSI^-$ guarantees reduction in exfoliation of graphite to have long battery cycle life, which is in accordance with the experimental reports (2000 cycles with 97.9 % capacity retention). The cell voltage determined in range 5.28-5.49 V having maximum specific capacity of 124 mAhg$^{-1}$, is in good agreement with experimental values. Through charge transfer analysis, we found that there is 0.97 $|e|$ charge transfer from graphite to $PF_6^-$, which clarifies that $PF_6^-$ intercalation into graphite is charging process. Moreover, the metallic character of $PF_6^-$ intercalated graphite system and the small diffusion barrier 0.14 eV indicate towards constant electronic conductivity and better rate performance, respectively. These results provide the clear understanding of $PF_6^-$ intercalation into graphite and also describe the role of staging behaviour to obtain the precise values of electrochemical properties.

### 1. Introduction

To fulfil future energy demands, it is very necessary to look for energy sources which are cost-effective, durable and can provide high energy outputs. In this regard, rechargeable metal-ion batteries have emerged as one of the important energy sources that have attracted quite a great attention of the scientific community thanks to their high energy density, better discharge voltage and high capacity.¹⁻² Also, with the on-going developments, the rechargeable Li-ion batteries (LIBs) currently cover the battery market for mobile phones, laptops, e-readers and many other electronic gadgets. However, the cost and safety issues associated with LIBs limit their suitability for grid-scale applications.³⁻⁴ Therefore, there is a constant urge for other energy storage options, and in this consideration, the dual ion batteries (DIBs) can be the ideal choice. The DIBs offer high working voltage, high energy density, and low cost because of which they can meet the requirements of electric vehicles and grid scale applications.⁵⁻⁹ The working mechanism of DIBs involves the intercalation of anions into cathode, whereas the intercalation or electroplating of cations into anodes during charging process, and the reverse processes occur during discharge. The very first anion intercalation into graphite was reported by Rudorff and Hofmann in 1938, where the intercalation of $HSO_4^-$ and $ClO_4^-$ anions was observed from acid electrolytes.¹⁰ After that, in 1989, for the first time McCullough et al. reported a DIB, also termed as dual-graphite battery as graphite was used as both anode and cathode in the non-aqueous electrolyte involving the intercalation/deintercalation of $ClO_4^-.^{11,12}$

Because of the promising properties, the DIBs are being constantly explored and researchers are continuously trying to increase the battery performance by varying the electrodes,¹³⁻¹⁵ electrolytes¹⁶⁻¹⁹ and other important components like current collectors and separators.²⁰ With the progressive research inputs, several forms of carbon have been explored towards their cathode applicability such as soft carbon, foam graphite, mesocarbon microbead and natural graphite.²¹⁻²⁴ Whereas, for dual-ion battery anodes, both graphite and metal anodes have been

studied extensively. $^{21,25}$ The dual ion batteries with metal anodes are one of the current interests as they are the promising alternatives of graphite anode offering high voltage, cycle life, suitable storage capacity due to their new redox chemistry. $^{15,26}$ The metal anode gets alloyed/de-alloyed with cation present in the electrolyte and this alloy/de-alloy process can store more energy than the intercalation/deintercalation mechanism in graphite. $^{27}$ Till present, various metal anodes have been proposed for dual-ion batteries such as Li, Na, K, Ca, and Al, but focus has still been on Li metal anode, as the Li-dual-ion batteries can supply highest working voltage due to lowest redox potential of Li-plating/dissolution reactions. $^{28}$ Other than the exploration of anodes and cathodes, the researchers have also studied a series of anions such as $BF_4^-$, $AlCl_4^-$, $PF_6^-$, bis(fluorosulfonyl)imide (FSI⁻), bis(trifluoromethanesulfonyl) imide (TFSI⁻) towards their intercalation behaviour into cathodes in DIB applications. $^{18,19,29}$ Among these anions, the $PF_6$ anion secures an important place as this is one of the most explored anion in DIBs due to its chemical and electrochemical inertness against cell components, high anti-oxidation ability, suitable size for insertion into graphite and high diffusivity. $^{30-32}$ One of the very recent study is reported by Wang et al. proposing a Li-ion DIB which offers a very high average voltage of 4.6 V and specific capacity of 99.4 mAhg⁻¹ with superior cycling stability and very high coulombic efficiency. $^{33}$ This dual-ion battery consists of graphite cathode, Li anode and an organic liquid electrolyte (lithium hexafluorophosphate ($LiPF_6$) in ethyl methyl carbonate (EMC)), where, $PF_6^-$ reversibly intercalates and de-intercalates between the graphite layers. However, till present, most of the studies carried out in the field of $PF_6$-DIB are experimental, which do provide promising results but could not give much information about the involved reaction mechanisms, the qualitative and quantitative interaction approach of $PF_6^-$ with graphite cathode and the structural changes that occur after intercalation in both $PF_6$ anion and graphite. Therefore, at this developing stage of $PF_6$-DIBs, the theoretical prospective are highly sought that can be helpful to researchers to perfectly understand the undergoing reaction

mechanism, the role of electrodes and electrolytes in battery performance, charge transfer mechanism and theoretical voltage profile and specific capacity. So, in this work, we have used the first-principles methods within the density functional theory to investigate the $PF_6^-$ intercalation into graphite. Utilizing the staging phenomenon of anion intercalation into graphite, we have explored the properties of $PF_6$-intercalated graphite including the geometric structure, stability, and also calculated the crucial electrochemical properties such as the average voltage and storage capacity. Also, the X-ray diffraction (XRD) simulations are performed to acquire better information about the stage formation and the associated structural changes by evaluation of interlayer distance and periodic repeat distance for all four different stages. The electronic properties, density of state, charge density difference and Bader charge analysis processes are used to study the charge transfer mechanism between graphite and $PF_6$. Further, the diffusion pathways of $PF_6^-$ inside the graphite have been investigated to check the rate performance of the battery. Moreover, for the better understanding of the DIB working mechanism, the necessary comparisons of the theoretical analysis have been made with the experimental results.

## 2. Computational details

We have used the first-principles calculations as implemented in the Vienna Ab initio simulation package (VASP) for all the structures. $^{34-37}$ The exchange-correlation potential is described by using generalized gradient approximation of Perdew-Burke-Ernzerhoff (GGA-PBE)$^{38}$ and to treat the interaction between ion cores and valence electrons projector augmented-wave (PAW)$^{39}$ method is used. A cut-off energy of 470 eV is used for plane-wave basis set for all the calculations. During structural optimization, the Brillouin zone was sampled with a gamma centred k-point grid of $7×7×7$ for unit cell and $3×3×1$ for supercell calculations. All the structures are optimized with total energy convergence criteria of $10^{-5}$ eV/Å and fully

relaxing the atomic and lattice positions until the Hellmann-Feynman forces on all the atoms were less than 0.01 eV/Å. DFT-D3 approach has been used for van der Waals corrections.⁴⁰

For density of state (DOS) calculations, a 3×3×1 supercell is used with a k-point grid of 15×15×15. The Bader charge analysis⁴¹⁻⁴³ was performed for quantitative determination of charge transfer from graphite to PF₆ molecule. We have calculated the diffusion barriers using the climbing image nudge elastic band method (CI-NEB).⁴⁴ The minimum energy paths (MEP) are initialized by introducing seven image structures between initial and final geometries. The energy convergence criteria are set at 10⁻³ eV. Zero-point energy (ZPE) correction is also included in the diffusion barrier calculations which is calculated as, $ZPE = \sum \frac{h\nu_i}{2}$, where, $h$ is Planck's constant and $v$ is the vibrational frequency. ZPE is calculated by considering the degree of freedom of intercalated PF₆. Specific capacity is calculated using the equation given below,

$$
C = \frac{nxF}{M_f} \tag{1}
$$

where, n is the number of electron transferred per PF₆ molecule; x is the number of PF₆ intercalated; F is faraday constant; Mբ is the mass of formula unit.

## 3. Results and Discussion

### 3.1. Geometric structure and stable binding sites

In DIBs, it has been reported that anions get intercalated and deintercalated into the cathode electrode. This intercalation and deintercalation can lead to structural changes. So, it is quite necessary to determine the changes occurring in the geometry structure of PF₆⁻ on intercalation into graphite. We observe that after intercalation, the perfect octahedral geometry of PF₆⁻ (90° ∠ F-P-F bond angle and 1.64 Å P-F bond length) gets slightly distorted with ∠F-P-F bond angle in the range of 89.63° - 90.37° and P-F bond length of 1.63 Å. This distortion could be due to the

acting van der Waals forces between graphite layers as well as the interactions between the host graphite layers and $PF_6^-$.

Further, to investigate the $PF_6^-$ intercalation into graphite, it is crucial to examine the possible orientation and intercalation sites. $PF_6^-$ can stabilize in two different orientations on intercalation as shown in Figure 1, (a) two fluorine atoms facing host graphite layer, (c) three fluorine atoms facing host graphite layer. Out of these, the orientation with three fluorine atoms facing graphite layer is the most stable. Next, we have investigated the possible stable sites for $PF_6^-$ intercalation into graphite. We find that three intercalation sites, (a) S1 (top), (b) S2 (bridge), and (c) S3 (hollow) are stable (Figure 1). In the S1 (top) site, the phosphorus atom occupies the top of C atoms. Whereas in the S2 (bridge) site, phosphorus atom occupies the bridge position of a C-C bond and in S3 (hollow) site, phosphorus atom is present in the hollow region. The optimized geometries and relative energies of all three sites are shown in Figure 1. These sites are very close in energy with S1 (top) site being the most stable site for $PF_6$ intercalation.

![](./images/812737131637112832_2.jpg)

**Figure 1:** Different orientation on $PF_6^-$ intercalation: (a) three fluorine atoms facing graphene and (b) two fluorine atoms facing graphene. Optimized structures of $PF_6^-$ intercalation at three different sites with three fluorine atoms facing graphene: (c) S1 (top), (d) S2 (bridge), (e) S3 (hollow). RE is the relative energy of the stable sites in eV units. Phosphorus and fluorine atoms are shown by pink and yellow spheres, respectively, graphite carbon atoms are shown by grey spheres.

### 3.2. System setup

Staging phenomenon is the characteristic feature of layered materials. Graphite intercalation compounds (GICs) follow staging mechanism where guest species form repeating sequences between the graphite layers. This staging mechanism can be well described by two types of forces present during intercalation, one is attractive forces between the graphite layers and second is the repulsive forces between the intercalant species present in the same gallery. The filling of host gallery with the incoming intercalant species is determined by these two forces. If the energy required to overcome the attractive forces between the graphite layers is higher than the repulsive forces between intercalant species, then the intercalation will be assisted in the same host gallery until all sites are filled before starting to fill the adjacent host layer. In this way, the various resultant stages are labelled with respect to number of layers or number of empty host galleries between the intercalating molecules. Stage-n system corresponds to the 'n' number of graphene layers or 'n-1' empty host galleries between two intercalating species.

In a similar way, different stages are also expected to appear in DIBs during the intercalation and de-intercalation of anions into graphite. Therefore, to investigate the staging mechanism of $PF_6^-$ intercalation into graphite, we have compared the favourability of the formation of different stages for exact same $PF_6^-$ concentration. For this, we have considered the optimized geometries of stage-1, stage-2 and stage-4 systems containing four $PF_6$ (Figure 2) and have

compared their relative energies. Out of the three systems, the stage-4 system is observed to be the most stable, followed by stage-2 and stage-1 for a constant $PF_6^-$ concentration. From these results, we can conclude that the intercalation of $PF_6^-$ into graphite also follows staging mechanism and for a given concentration of $PF_6^-$, intercalation is favoured into a stage-n having highest possible n value as the energy required to overcome the repulsive forces between the intercalant species is less than the energy required to overcome the van der Waals forces between the graphite layers. And in a similar way like intercalation of $PF_6^-$ into graphite during charging, the staging mechanism is also followed for the de-intercalation during discharge process. Overall, with the help of stability calculations, we could explain the formation of different $PF_6$-intercalated stages following the staging mechanism of intercalation/deintercalation that have been observed in several experimental reports on $PF_6^-$ dual-ion batteries during the charge/discharge processes.

![](./images/812737131637112832_3.jpg)

Figure 2: Systematic representation of staging mechanism (a) stage-4, (b) stage-2, (c) stage-1.
Relative energy (RE) is in eV units for systems containing same $PF_6^-$ concentration.

Further, to investigate the staging mechanism in $LiPF_6$-graphite DIB, we have modelled four different stages (stage-1, stage-2, stage-3 and stage-4) of $PF_6$-intercalated graphite structure as shown in Figure 3. A 6×6×2 supercell containing 288 carbon atoms is used for calculations of stage-1, stage-2 and stage-4 systems and a 6×6×3 supercell containing 432 carbon atoms is used for stage-3 calculations. To get the understanding of how the structural as well as electrochemical properties vary when the intercalation takes place within the stage, different possible concentration or stoichiometries are studied for each of the $PF_6$-intercalated stage. For example, in case of stage-1, the graphite system into consideration contains 288 carbon atoms, so first; we calculate the maximum number of $PF_6^-$, which can be intercalated to give a stable GIC. The maximum number of $PF_6^-$ are observed to be 16 $PF_6^-$ per 288 carbon atoms of graphite, so represented by a formula unit of $[C_{288}(PF_6)_{16}]$. The other three lower concentrations are built to have 4, 8, and 12 $PF_6^-$ per 288 carbon atoms, but satisfying the stage-1 characteristic of having each interlayer space to be filled. Thus, the resultant formula unit becomes $[C_{288}(PF_6)_n]$ having n values as 4, 8, 12 and 16 for stage-1. Similarly, different concentration built for investigating other stages are represented by $[C_{288}(PF_6)_n]$ formula unit, where n = 2, 4, 6 and 8 for stage-2; and n = 1, 2, 3 and 4 for stage-4. As for stage-3, the constructed 6×6×3 graphite supercell contains 432 carbon atoms, so the formula unit becomes $[C_{432}(PF_6)_n]$ with n = 2, 4, 6 and 8 $PF_6^-$. Overall, in all of these modelled stages, we have tried to get the maximum load (which can form a stable $PF_6$-itercalated graphite system) to gain maximum storage capacity, which can also be comparable with the experimental value.⁴⁵ All of these optimized structures are shown in Figure S1, S2, S3 and S4 in Supporting Information.

![](./images/812737131637112832_4.jpg)

Figure 3: Schematic representation of the optimized structures of the four different $PF_6^-$ intercalated graphite stages: (a) stage-1, (b) stage-2, (c) stage-3, (d) stage-4.

### 3.3. Intercalation energy of $PF_6^-$ intercalated graphite stages

It is very important to determine, whether an intercalation is feasible or not. This feasibility of intercalation can be determined from the intercalation energy calculations using the following equation,

$$
E_{intercalation} = \frac{E[(PF_6)_x C_n] - E[C_n] - xE[PF_6]}{x} \tag{2}
$$

Here, $E[(PF_6)_x C_n]$ and $E[C_n]$ are the total energy of the graphite system with and without x number of $PF_6$ anions, respectively, and $E[PF_6]$ is the total energy of one $PF_6$ molecule in the box. The calculated intercalation energies for all different stages are listed in Table 1. According to the equation, a more negative value of intercalation energy indicates a more feasible intercalation of $PF_6^-$ into graphite. We observe that the intercalation energy values of all graphite intercalated compounds are negative indicating towards the feasibility of these $PF_6$ intercalated systems. However, in all stages, the first intercalation step is less favourable, and

the favourability of intercalation becomes more as PF₆ concentration further increases. This could be explained as the activation of graphite for the very first intercalation step, where the partially closed host graphite gallery needs to be activated to accommodate the large sized PF₆⁻. Whereas, the intercalation becomes easier for the further concentration of PF₆⁻ as the anions insert into the already expanded graphite galleries. This kind of activation of graphite for the first intercalation steps has also been observed in the several experimental studies of PF₆ intercalation into graphite.³³ Along with that many other theoretical and experimental reports on various anion intercalation studies (such as AlCl₄⁻, TFSI⁻, FSI⁻) have also observed a significant difference between first and other subsequent intercalation steps.⁴⁶,⁴⁷ However, when we particularly compare with AlCl₄⁻ intercalation, we observe that the AlCl₄⁻ intercalation requires greater activation of graphitic layers as compared to PF₆. It is reflected in the intercalation energy values for the very first intercalation, which are positive for AlCl₄⁻ and thus making it difficult to intercalate the large sized AlCl₄⁻ (5.28 Å ionic radius)⁶ into partially closed graphite layers.⁴⁶ Whereas, in case of PF₆⁻ intercalation, the activation of graphitic layers is more hassle free to accommodate small sized PF₆⁻ (4.36 Å ionic radius),⁶ which can be clearly observed from the negative values of intercalation energy for first intercalation steps resulting into a more favourable intercalation of PF₆⁻ into graphite. We observe that the intercalation of PF₆⁻ is accompanied by the volume expansion of graphite by 113 % in stage-1 PF₆⁻ intercalated system and this calculated value is little less than the experimentally obtained volume expansion of >130 %.⁴⁸ The slightly higher volume expansion observed in experiment could be because of some solvent co-intercalation along with PF₆⁻ into graphite, which does not much affect the interlayer distance but could increase the volume expansion in graphite intercalation compound.⁴⁵ We have also calculated the gallery height expansion on PF₆ intercalation for the comparative study with AlCl₄⁻ and FSI⁻ intercalation. The gallery expansion is 114 % in graphite on PF₆⁻ intercalation, while the observed expansion

for $AlCl_4^-$ intercalation $(\sim 150$-$160\%)^{25}$ and $FSI^-$ intercalation $(\sim 134\%)^{47}$ into graphite is quite large. Thus, we can conclude that the Li-PF$_6$ DIBs can provide better cycle stability and could be the promising choice as next generation dual-ion batteries.

**Table 1**: Intercalation energy (eV) per $PF_6^-$ and interlayer distance (Å) for all stages with different concentrations.

<table>
  <thead>
    <tr>
      <th>Stages</th>
      <th>Number of $PF_6^-$</th>
      <th>Intercalation energy (eV)</th>
      <th>Interlayer distance (Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Stage-1</td>
      <td>4</td>
      <td>-0.85</td>
      <td>6.94</td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>-2.22</td>
      <td>7.06</td>
    </tr>
    <tr>
      <td></td>
      <td>12</td>
      <td>-2.58</td>
      <td>7.30</td>
    </tr>
    <tr>
      <td></td>
      <td>16</td>
      <td>-2.70</td>
      <td>7.35</td>
    </tr>
    <tr>
      <td>Stage-2</td>
      <td>2</td>
      <td>-0.88</td>
      <td>7.06</td>
    </tr>
    <tr>
      <td></td>
      <td>4</td>
      <td>-2.32</td>
      <td>7.23</td>
    </tr>
    <tr>
      <td></td>
      <td>6</td>
      <td>-2.71</td>
      <td>7.32</td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>-2.86</td>
      <td>7.35</td>
    </tr>
    <tr>
      <td>Stage-3</td>
      <td>2</td>
      <td>-0.87</td>
      <td>7.07</td>
    </tr>
    <tr>
      <td></td>
      <td>4</td>
      <td>-2.33</td>
      <td>7.26</td>
    </tr>
    <tr>
      <td></td>
      <td>6</td>
      <td>-2.74</td>
      <td>7.34</td>
    </tr>
    <tr>
      <td></td>
      <td>8</td>
      <td>-2.88</td>
      <td>7.37</td>
    </tr>
    <tr>
      <td>Stage-4</td>
      <td>1</td>
      <td>-0.89</td>
      <td>7.22</td>
    </tr>
    <tr>
      <td></td>
      <td>2</td>
      <td>-2.36</td>
      <td>7.35</td>
    </tr>
    <tr>
      <td></td>
      <td>3</td>
      <td>-2.76</td>
      <td>7.38</td>
    </tr>
    <tr>
      <td></td>
      <td>4</td>
      <td>-2.91</td>
      <td>7.40</td>
    </tr>
  </tbody>
</table>

### 3.4. X-ray diffraction study of $PF_6^-$ intercalation into graphite

We have simulated the XRD pattern of optimized supercells of pristine graphite and all four stages (n=1 to 4) (Figure 4). The XRD pattern helps in the determination of structural changes on alteration in the $PF_6^-$ concentration. The XRD patterns show that the $PF_6$ intercalation into the graphite layers leads to some structural changes, and (002) peak of pristine graphite splits into two new dominant peaks corresponding to (00n+1) and (00n+2) planes of stage-n system, which is the reflective of the staging behaviour. The interlayer distance ($d_i$) and periodic repeat distance ($I_c$) of a particular stage-n are calculated using the d-spacing values as, $d_i$=(n+1)×$d_{(00n+1)}$-3.43×(n-1) and $I_c$=(n+1)$d_{(00n+1)}$=(n+2)$d_{(00n+2)}$, respectively.¹⁷⁴⁹ During charging, as the initial intercalation of $PF_6$ leads to the formation of stage-4, the two most dominant intensity peaks corresponding to planes (005) and (006) occur at 2θ=25.15° and 30.29° with the d-spacing values of 3.54 and 2.95 Å, respectively. And, the interlayer distance and periodic repeat distance are calculated to be 7.40 and 17.69 Å, respectively. We observe that for stage-3 and stage-2, the splitting separation between the two corresponding dominant peaks further increases, which could be related to the larger deviation of these stages from the graphite structure due to the increased concentration of $PF_6$ into graphite layers. For the fully charged stage-1 [$C_{18}(PF_6)$], XRD pattern shows the two dominant peaks at 2θ= 24.36° and 36.90° having the maximum splitting and thus calculated periodic repeat distance and interlayer distance of 7.30 Å ($I_c$=2×3.65=3×2.43) perfectly matches with the interlayer distance of our optimized stage-1 structure. The interlayer distance observed in our study is slightly small as compared to experimentally reported values of interlayer distance of 7.72-8.08 Å for $PF_6$-GIC having EMC solvent.⁴⁵˵⁵⁰⁻⁵³ All of these experimental reports show solvent co-intercalation along with the $PF_6^-$, which could be the reason of this small increase (0.42-0.59 Å) in interlayer distance than our observed interlayer distance of 7.30 Å (obtained from XRD simulation of stage-1) without considering solvent co-intercalation. This difference of 0.42-0.59 Å seems quite less for intercalation of additional solvent molecules; however, it can be justified by a

recent study, where Read et al. conclude that the spacing of the graphite sheets is dictated by the anion size and not the solvation sphere of the co-intercalated solvent.⁴⁵ Other than this, the interlayer distance around ~7.17 Å, which is smaller than our study has also been reported for LiPF₆-dual-ion battery Fan et al., but not with EMC solvent.⁵⁴ They observed that the reason for this comparatively smaller interlayer distance could be the intercalation of PF₆⁻ without any solvation shell, demonstrated by apparently higher potential plateaus for the anion intercalation. Moreover, in our study, the optimized interlayer distances for various concentrations studied in stage-4 to stage-1, vary in the range of 6.94-7.40 Å, which are not far from the interlayer distance (~7.17 Å) of PF₆-intercalated graphite system without solvent co-intercalation.⁵⁴ In addition, as we move from satge-4 to stage-1, the appearance of additional peaks also increases other than the dominant peaks, which is also a consequence of higher structural deformation with increased PF₆ concentration into graphite resulting into various other planes such as planes $(02\overline{2})$, $(02\overline{4})$, $(0\overline{2}\overline{4})$, and $(\overline{2}0\overline{4})$ in stage-1 and $(2\overline{2}\overline{2})$, $(02\overline{2})$, $(00\overline{4}$), and $(\overline{2}0\overline{2})$ in stage-2. Especially for stage-2, the high intensity peak at 2θ=16.51° corresponds to the two sets of planes $(00\overline{4})$ and $(\overline{2}0\overline{2})$ of equal d-spacing to give an add up of peak contributions. When comparing with FSI⁻ intercalated graphite system, we observe that both PF₆⁻ and FSI⁻ show the similar staging mechanism, but the interlayer spacing is higher in case of FSI intercalation (7.84 Å) due to its large van der Waals volume (95.00 Å³) than PF₆⁻ (69.00 Å³).⁵⁵ Therefore, exfoliation phenomenon will be less in the case of PF₆⁻ giving long cycle life, which is in accordance with the experimental reports (2000 cycles with 97.9 % capacity retention).³³

![](./images/812737131637112832_5.jpg)

Figure 4: Simulated XRD pattern of pristine graphite and different stages of $PF_6^-$ intercalated graphite supercells. The highest intensity pink coloured peak represents the (002) plane of pristine graphite supercell. All the stages show two dominant peaks corresponding to (00n+1) and (00n+2) planes for a particular stage-n.

### 3.5. Electrochemical characteristics

In this section, we have examined the much important electrochemical characteristics such as voltage and storage capacity of $LiPF_6$ DIB and have made a valuable comparison with the experimental observations. The open circuit voltage is one of the most important electrochemical properties which determines the working suitability of the battery. This $LiPF_6$ DIB operates with the electrochemical deposition of Li at anode (Lithium) and

intercalation/deintercalation of $PF_6$ into cathode (graphite), therefore the full cell reaction can be described as:

$$xLiPF_6(EMC)_4 + C_n \rightarrow C_n(PF_6)_x + xLi + 4xEMC \tag{3}$$

As shown in the above equation, the reaction mechanism of DIB also involves the contribution from the electrolyte medium. Therefore, battery voltage also depends upon desolvation energy (energy required to form separate anion from electrolyte) and intercalation energy (energy required to intercalate anion into graphite lattice) besides the oxidative potential of graphite.

Cell voltage ($V$) can be determined by Nernst equation,

$$V = \frac{-\Delta G_{cell}}{zF} \tag{4}$$

Here, z and F are the number of valence electrons and Faraday constant, respectively, and $\Delta G_{cell}$ is the change in Gibbs free energy for chemical reaction.

$$\Delta G_{cell} = \Delta H_{cell} - T\Delta S_{cell} \tag{5}$$

$$\Delta G_{cell} = \Delta E_{cell} + P\Delta V_{cell} - T\Delta S_{cell} \tag{6}$$

Here, $\Delta V_{cell}$ and $\Delta S_{cell}$ are change in volume and entropy for chemical reaction. At 0K, $\Delta V_{cell}$ and $\Delta S_{cell}$ can be neglected,

$$\Delta G_{cell} = \Delta E_{cell} \tag{7}$$

$$V = \frac{-\Delta E_{cell}}{zF} \tag{8}$$

Therefore, voltage equation can be written as,

$$V = \frac{E[C_n(PF_6)_x] + xE[Li] + 4xE[EMC] - E[C_n] - xE[LiPF_6(EMC)_4]}{x} \tag{9}$$

where, $E[C_{n}(PF_{6})_{x}]$, and $E[C_{n}]$ are the total energies of $PF_{6}$-intercalated graphite system, and bulk graphite, respectively. $E[Li]$ is the total energy of a single atom in a bulk bcc structure, whereas, $E[EMC]$ and $xE[LiPF_{6}(EMC)_{4}]$ are obtained by optimizing EMC and $LiPF_{6}[EMC]_{4}$ as a molecular species due to unavailability of their crystal structure.

![](./images/812737131637112832_6.jpg)

Figure 5: Staging voltage profile diagram for $PF_{6}$-intercalated graphite system. The inset shows the experimental voltage obtained by Wang et al.,³³ with the blue rectangle indicating the range corresponding to the calculation. Inset figure reproduced with permission from (reference number 33). Copyright (2018, WILEY-VCH).

Figure 5 shows the voltage profile for the $PF_{6}$ intercalation into graphite, *i.e.* moving from low intercalated stages to high intercalated stages and increasing the specific capacity accordingly.
It was found that on going from stage-4 to satge-1, the specific capacity increases from 31.0 mAhg⁻¹ ($PF_{6}$-$C_{72}$) to 124.0 mAhg⁻¹ ($PF_{6}$-$C_{18}$) yielding the voltage steps from 5.28 V to 5.49 V.
Voltage obtained for $LiPF_{6}$-graphite DIB is higher than that obtained for FSI-DIB (4.7 V), however both shows the similar staging mechanism and increment in voltage from stage-4 to stage-1.⁴⁷ Our calculated voltage range 5.28-5.49 V is in good accordance with the

experimental voltage range of 4.0-5.3 V.³³ The slight difference in the voltage values can be easily understood. First, on the basis of the PF₆⁻-intercalated graphite stages, which have been considered to plot the voltage profile. In case of our theoretical calculations, we could only consider upto four stages, stage-4 to stage-1, due to the involved computational time limitations, which provides a voltage profile of more concentrated graphite intercalation compounds. However, in experimental procedures, there could be the formation of lower ordered stage too, thus resulting into slightly lower working voltage range. Secondly, in experiments the maximum observed stoichiometry of PF₆⁻-GIC is C₂₀PF₆,⁴⁵ whereas in our study, the maximum stoichiometry of C₁₈PF₆ is achievable to form a stable PF₆⁻-GIC, which may cost some extra efforts, thus could be the reason of increased charging voltage. The third reason could be the consideration of PF₆⁻ intercalation without solvent co-intercalation, as the anions have to strip off solvent shell before intercalation, thus an increase in charging voltage is obtained.⁵⁴

For the case of LiPF₆-DIB storage capacity, the maximum capacity of 124 mAhg⁻¹ is obtained for theoretically accessible PF₆⁻-intercalated graphite compound with the stoichiometry of C₁₈PF₆. However, in case of experimental studies, variations in capacity value (80-110 mAhg⁻¹) can be observed for different reports⁵³,⁵⁴ and the maximum capacity to be reported is 110 mAhg⁻¹ with the stoichiometry of C₂₀PF₆.⁴⁵ Therefore, overall, we can say that theoretical feasibility of C₁₈PF₆ stoichiometry formation in our study, results into slightly higher storage capacity as well as voltage range compared to the experiments.

### 3.6. Electronic properties

In this section, we have studied the electronic behaviour of PF₆⁻ intercalated graphite system and have tried to understand the nature of interaction between the intercalated PF₆ and graphite host. The constant electronic conductivity of an electrode system is very important to get the optimum battery performance. As we assume that during the intercalation of PF₆ anion into

graphite, the anion before starting the intercalation releases an electron which is transmitted to current collectors through GICs. Therefore, $\text{PF}_\text{6}$-$\text{C}_\text{n}$ compound should possess electronic conductivity like other electrode materials. The electronic conductivity can be determined by density of state (DOS) calculations. Figure 6 (a) represents the total density of state (TDOS) and projected density of state (PDOS) of $\text{PF}_\text{6}$ intercalated graphite. It is well known that graphite shows a good in plane electronic conductivity due to the presence of $\text{p}_\text{z}$ electronic states over the Fermi level and no inter-plane conductivity due to presence of $\text{s}$, $\text{p}_\text{x}$, $\text{p}_\text{y}$ electronic states away from the Fermi level. Upon $\text{PF}_\text{6}^-$ intercalation into graphite, the electronic conductivity is retained, which can be seen from the electronic states over the Fermi level in Figure 6 (a). This metallic nature of $\text{PF}_\text{6}$ intercalated graphite arises due to some overlap between the 2p orbital of F and 2p orbital of C.

Finally, we investigate the charge density difference (CDD) calculations to look into the interaction behaviour between the $\text{PF}_\text{6}^-$ and graphite layers to clarifying the mechanism of $\text{PF}_\text{6}$ intercalation into graphite. This CDD is obtained by using the equation,

$$
\rho_{CDD}=\rho^{total}-\sum_{i}\rho_{i}^{fragments} \tag{10}
$$

Here, $\rho^{total}$ is the total charge density of the system, and $\rho_{i}^{fragments}$ represents the charge density of individual fragment. Charge density of fragments is calculated using the pseudostructure in which the fragments remains in the same structure as that in total structure, but other parts are deleted. Figure 6 (b) represents the charge density difference plot, where the yellow colour represents the electronic density accumulation and the cyan colour represents the electronic density depletion. From Figure 6 (b) it is clear that, the valence electron density of the graphene layers is transferred to the $\text{PF}_\text{6}^-$ molecule. Therefore, there is net gain of electronic charge around F atoms of $\text{PF}_\text{6}^-$ and net loss of electronic charge around neighbouring

C atoms of graphite indicating towards the ionic character of bonding between the F atoms of
$PF_6^-$ and the facing carbon atoms of the graphene layer.

For the quantitative determination of charge transfer, Bader charge analysis is performed. Upon intercalation of $PF_6^-$ into graphite, graphite layers act as the electron donor by decreasing their electronic charge per atom and $PF_6^-$ molecule plays the role of electron acceptor by increasing the electronic charge per atom of F from -0.63 |e| (in isolated state) to -0.80 |e| in GIC (Table S1, Supporting Information). Thus, on intercalation, one $PF_6^-$ accepts ~ -0.97 |e| charge from graphite, signifying the electrochemical oxidation of graphite upon $PF_6^-$ intercalation and thus concluding towards a charging process.

![](./images/812737131637112832_7.jpg)

Figure 6: (a) Total DOS and Projected DOS of $PF_6^-$ intercalated graphite. The Fermi level is set at zero. (b) Isosurface (0.002 |e| $\text{\AA}^{-3}$) for the charge density difference for $PF_6^-$-intercalated graphite system. Here, the yellow colour represents the electronic density accumulation and the cyan colour represents the electronic density depletion.

### 3.7. $PF_6^-$ diffusion and energy profile along minimum energy paths (MEPs)

The charging/discharging rate of a DIB depends critically on the speed at which involved ions migrate through electrolyte and electrodes. Therefore, an encouraging strategy to create excellent performance battery is to develop new electrode materials with high electrical conductivity for fast electron transfer and low diffusion barrier for fast ion transfer, which depends upon the mobility of intercalated ions. Here, this mobility is quantitatively estimated from the diffusion of $PF_6^-$ in the graphite lattice. The diffusion of intercalant $PF_6^-$ in graphite is limited to the 2-dimensional plane due to layered structure of graphite. To find the motion of $PF_6$ in graphite lattice, we have considered three different MEPs connecting the two most stable top sites and calculated the corresponding diffusion barrier using CI-NEB method.⁴⁴ These MEPs along with their energy profile are shown in Figure 7. Before starting the CI-NEB calculations, structures of initial and final image are fully relaxed, and seven images are inserted between initial and final image. In the path-1 direction, $PF_6^-$ diffusion in graphite lattice is required to overcome a small energy barrier of 0.15 eV. Similarly, the energy barriers for $PF_6^-$ diffusion along path-2 and path-3 are 0.16 and 0.14 eV, respectively. So, the optimal path for $PF_6^-$ diffusion in graphite is path-3. Our results show that the energy barrier of $PF_6^-$ diffusion is quite small compared to the alkali cations (like Li, Na) (0.2-0.4 eV)⁵⁶,⁵⁷ and $AlCl_4^-$ (0.33 eV) diffusions in graphite. Therefore, we can say that the diffusion barrier is low enough to provide a trouble-free diffusion for $PF_6$ anions in graphite cathode.

![](./images/812737131637112832_8.jpg)

Figure 7: (a) Systematic representation of optimized diffusion pathways of $PF_6^-$ in graphite, and (b) involved energy barriers corresponding to the diffusion pathways.

## 4. Conclusion

Based on the dispersion-corrected density functional theory calculations, we have systematically studied the staging mechanism of $PF_6^-$ intercalation in graphite to investigate charge transfer mechanism, diffusion barrier and electrochemical properties like voltage and specific capacity. We have modelled four different stages (stage-1, stage-2, stage-3 and stage-4) of $PF_6^-$ intercalated graphite to investigate the staging mechanism and to study the electrochemical properties. On studying the binding characteristics of $PF_6^-$ in graphite, we observe that $PF_6^-$ intercalates with its energetically stable octahedral form with some distortions due to van der Waals attraction between the graphite layers. Simultaneously, the interlayer spacing between the graphite layers increases from 3.34 to 7.30 Å on intercalation of $PF_6^-$, which could result into trouble free diffusion of $PF_6^-$ in graphite. Our diffusion calculations using CI-NEB methods supports this fact and we observe quite small diffusion barrier of 0.14 eV for $PF_6^-$ diffusion inside graphite. Our relative energy calculation of different stages of $PF_6^-$ intercalated system show that the intercalation starts with stage-4 system and followed by stage-3, stage-2 and stage-1. In XRD simulations, the occurrence of two dominant peaks in a sequencing pattern confirms that $PF_6^-$ intercalation into graphite follows the staging mechanism. The smaller XRD simulated interlayer distance observed for $PF_6^-$ intercalation compared to FSI indicates towards decreased exfoliation of graphite cathode for $PF_6^-$ intercalation and an overall increased cycle stability of $LiPF_6$-graphite DIB battery. Moreover, we observe that the theoretical feasibility of $C_{18}PF_6$ formation results into slightly higher storage capacity (124.0 mAhg⁻¹) as well as voltage range (5.28-5.49 V) compared to the experiments. The reason could be a higher achievable stoichiometry of $PF_6$-intercalated

graphite system $C_{18}PF_6$ in our calculations compared to $C_{18}PF_6$ in experiments, which may cost some extra efforts, or consideration of higher order stages (stage-4 to stage-1) in our theoretical calculations compared to experiment, which deals with a wide range of GIC formation, thus increasing the overall charging voltage. The metallic character of graphite before and after $PF_6^-$ intercalation confirms the excellent electronic conductivity, which is crucial for electrode material. The charge density difference calculations and quantitative Bader charge analysis show that ~ -0.97 $|e|$ charge is transferred from C atoms of host graphite to $PF_6^-$ indicating towards the electrochemical oxidation of graphite on $PF_6$ intercalation and confirming that $PF_6^-$ intercalation is a charging process. All of these results provide in-depth understanding of interaction behaviour of $PF_6^-$ and graphite and help in explaining the role of staging mechanism to obtain precise electrochemical properties such as voltage and storage capacity for $LiPF_6$-graphite DIBs.

## 5. Supporting Information

The supporting Information file contents are optimized structures for all four stages with different stoichiometries, and Bader charge analysis.

## 6. Acknowledgments

We thank IIT Indore for use of its lab and computing facilities. This work was supported by DST-SERB (EMR/2015/002057) and CSIR (01(2886)/17/EMR-II), New Delhi. S. K. thanks IIT Indore for providing research facilities and P.B. thanks MHRD for research fellowship.

## References

(1) Dunn, B.; Kamath, H.; Tarascon, J.-M. Electrical Energy Storage for the Grid: A Battery of Choices. *Science* **2011**, *334*, 928-935.

(2) Armand, M.; Tarascon J.-M. Building Better Batteries. *Nature* **2008**, *451*, 652-657.

(3) Lee, J.; Urban, A.; Li, X.; Su, D.; Hautier, G.; Ceder, G. Unlocking the Potential of Cation-Disordered Oxides for Rechargeable Lithium Batteries. *Science* **2014**, *343*, 519-522

(4) Goodenough, J. B.; Kim, Y. Challenges for Rechargeable Li Batteries. *Chem. Mater.* **2010**, *223*, 587-603

(5) Wang, M.; Tang, Y. A Review on the Features and Progress of Dual-Ion Batteries. *Adv. Energy Mater.* **2018**, *8*, 1703320.

(6) Zhou, X.; Liu, Q.; Jiang, C.; Ji, B.; Ji, xiulei; Tang, Y.; Cheng, H.-M. Beyond Conventional Batteries: Strategies towards Low-Cost Dual-Ion Batteries with High Performance. *Angew. Chem. Int. Ed.* **2019**.

(7) Heckmann, A.; Thienenkamp, J.; Beltrop, K.; Winter, M.; Brunklaus, G.; Placke, T. Towards High-Performance Dual-Graphite Batteries Using Highly Concentrated Organic Electrolytes. *Electrochim. Acta* **2018**, *260*, 514-525.

(8) Bhauriyal, P.; Bhattacharyya, G.; Rawat, K. S.; Pathak, B. Graphene/HBN Heterostructures as High-Capacity Cathodes with High Voltage for Next-Generation Aluminum Batteries. *J. Phys. Chem. C* **2019**, *123*, 3959-3967.

(9) Bhauriyal, P.; Pathak, B. Identification of Non-Carbonaceous Cathodes in Al Batteries: Potential Applicability of Black and Blue Phosphorene Monolayers. https://doi.org/10.1002/asia.201900693.

(10) Rüdorff, W.; Hofmann, U. Über Graphitsalze. *Zeitschrift für anorganische und allgemeine Chemie* **1938**, *238*, 1–50.

(11) McCullough, F. P.; Levine, C. A.; Snelgrove, R. V. Secondary Battery. US 4830938, May 16, 1989.

(12) McCullough, F. P.; Beale, A. F. Secondary Electrical Energy Storage Device and Electrode Therefor. US4865931A, 1989.

(13) Dong, S.; Li, Z.; Rodríguez-Pérez, I. A.; Jiang, H.; Lu, J.; Zhang, X.; Ji, X. A Novel Coronene//Na2Ti3O7 Dual-Ion Battery. *Nano Energy* **2017**, *40*, 233–239.

(14) Tong, X.; Zhang, F.; Chen, G.; Liu, X.; Gu, L.; Tang, Y. Core-Shell Aluminum@Carbon Nanospheres for Dual-Ion Batteries with Excellent Cycling Performance under High Rates. *Adv. Energy Mater.* **2018**, *8*, 1701967.

(15) Sheng, M.; Zhang, F.; Ji, B.; Tong, X.; Tang, Y. A Novel Tin-Graphite Dual-Ion Battery Based on Sodium-Ion Electrolyte with High Energy Density. *Adv. Energy Mater.* **2017**, *7*, 1601963.

(16) Deunf, É.; Moreau, P.; Quarez, É.; Guyomard, D.; Dolhem, F.; Poizot, P. Reversible Anion Intercalation in a Layered Aromatic Amine: A High-Voltage Host Structure for Organic Batteries. *J. Mater. Chem. A* **2016**, *4*, 6131–6139.

(17) Seel, J. A.; Dahn, J. R. Electrochemical Intercalation of PF[Sub 6] into Graphite. *J. Electrochem. Soc.* **2000**, *147*, 892.

(18) Carlin, R. T. Dual Intercalating Molten Electrolyte Batteries. *J. Electrochem. Soc.* **1994**, *141*, L73..

(19) Sutto, T. E.; Duncan, T. T.; Wong, T. C. X-Ray Diffraction Studies of Electrochemical Graphite Intercalation Compounds of Ionic Liquids. *Electrochimica Acta* **2009**, *54*, 5648–5655.

(20) Jiang, C.; Fang, Y.; Lang, J.; Tang, Y. Integrated Configuration Design for Ultrafast Rechargeable Dual-Ion Battery. *Adv. Energy Mater.* **2017**, *7*, 1700913.

(21) Liao, H.-J.; Chen, Y.-M.; Kao, Y.-T.; An, J.-Y.; Lai, Y.-H.; Wang, D.-Y. Freestanding Cathode Electrode Design for High-Performance Sodium Dual-Ion Battery. *J. Phys. Chem. C* **2017**, *121*, 24463–24469.

(22) Ji, B.; Zhang, F.; Wu, N.; Tang, Y. A Dual-Carbon Battery Based on Potassium-Ion Electrolyte. *Adv. Energy Mater.* **2017**, *7*, 1700920.

(23) Fan, L.; Liu, Q.; Chen, S.; Xu, Z.; Lu, B. Soft Carbon as Anode for High-Performance Sodium-Based Dual Ion Full Battery. *Adv. Energy Mater.* **2017**, 7, 1602778.

(24) Li, Q.; Bjerrum, N. J. Aluminum as Anode for Energy Storage and Conversion: A Review. *Journal of Power Sources* **2002**, 110, 1–10.

(25) Read, J. A.; Cresce, A. V.; Ervin, M. H.; Xu, K. Dual-Graphite Chemistry Enabled by a High Voltage Electrolyte. *Energy Environ. Sci.* **2014**, 7, 617–620.

(26) Aladinli, S.; Bordet, F.; Ahlbrecht, K.; Tübke, J.; Holzapfel, M. Compositional Graphitic Cathode Investigation and Structural Characterization Tests for Na-Based Dual-Ion Battery Applications Using Ethylene Carbonate: Ethyl Methyl Carbonate-Based Electrolyte. *Electrochimica Acta* **2017**, 228, 503–512.

(27) Wang, M.; Zhang, F.; Lee, C.-S.; Tang, Y. Low-Cost Metallic Anode Materials for High Performance Rechargeable Batteries. *Adv. Energy Mater.* **2017**, 7, 1700536.

(28) Xi, X.-T.; Li, W.-H.; Hou, B.-H.; Yang, Y.; Gu, Z.-Y.; Wu, X.-L. Dendrite-Free Lithium Anode Enables the Lithium//Graphite Dual-Ion Battery with Much Improved Cyclic Stability. *ACS Appl. Energy Mater.* **2019**, 2, 201–206.

(29) Santhanam, R.; Noel, M. Effect of Solvents on the Intercalation/de-Intercalation Behaviour of Monovalent Ionic Species from Non-Aqueous Solvents on Polypropylene-Graphite Composite Electrode. *Journal of Power Sources* **1997**, 66, 47–54.

(30) Xu, K. Nonaqueous Liquid Electrolytes for Lithium-Based Rechargeable Batteries. *Chem. Rev.* **2004**, 104, 4303–4418.

(31) Xu, K.; von Cresce, A. Interfacing Electrolytes with Electrodes in Li Ion Batteries. *J. Mater. Chem.* **2011**, 21, 9849.

(32) Miyoshi, S.; Akbay, T.; Kurihara, T.; Fukuda, T.; Staykov, A. T.; Ida, S.; Ishihara, T. Fast Diffusivity of $PF_6^-$ Anions in Graphitic Carbon for a Dual-Carbon Rechargeable Battery with Superior Rate Property. *J. Phys. Chem. C* **2016**, 120, 22887–22894.

(33) Wang, G.; Yu, M.; Wang, J.; Li, D.; Tan, D.; Löffler, M.; Zhuang, X.; Müllen, K.; Feng, X. Self-Activating, Capacitive Anion Intercalation Enables High-Power Graphite Cathodes. *Adv. Mater.* **2018**, *30*, 1800533.

(34) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for *Ab Initio* Total-Energy Calculations Using a Plane-Wave Basis Set. *Phys. Rev. B* **1996**, *54*, 11169–11186.

(35) Kresse, G.; Hafner, J. Ab Initio Molecular Dynamics for Liquid Metals. *Phys Rev B Condens Matter.* **1993**, *47*, 558.

(36) Kresse, G.; Hafner, J. Ab Initio Molecular-Dynamics Simulation of the Liquid-Metal–Amorphous-Semiconductor Transition in Germanium. *Phys. Rev. B* **1994**, *49*, 14251.

(37) Kresse, G.; Furthmüller, J. Efficiency of Ab-Initio Total Energy Calculations for Metals and Semiconductors Using a Plane-Wave Basis Set. *Comput. Mater. Sci.* **1996**, *6*, 15-20.

(38) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77* (18), 3865–3868.

(39) Blöchl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B* **1994**, *50*, 17953–17979.

(40) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A Consistent and Accurate *Ab Initio* Parametrization of Density Functional Dispersion Correction (DFT-D) for the 94 Elements H-Pu. *The Journal of Chemical Physics* **2010**, *132*, 154104.

(41) Henkelman, G.; Arnaldsson, A.; Jónsson, H. A Fast and Robust Algorithm for Bader Decomposition of Charge Density. *Computational Materials Science* **2006**, *36*, 354–360.

(42) Bader, R. F. W. A Quantum Theory of Molecular Structure and Its Applications. *Chem. Rev.* **1991**, *91*, 893–928.

(43) Sanville, E.; Kenny, S. D.; Smith, R.; Henkelman, G. Improved Grid-Based Algorithm for Bader Charge Allocation. *J. Comput. Chem.* **2007**, *28*, 899–908.

(44) Henkelman, G.; Uberuaga, B. P.; Jónsson, H. A Climbing Image Nudged Elastic Band Method for Finding Saddle Points and Minimum Energy Paths. *The Journal of Chemical Physics* **2000**, *113*, 9901–9904.

(45) Read, J. A. In-Situ Studies on the Electrochemical Intercalation of Hexafluorophosphate Anion in Graphite with Selective Cointercalation of Solvent. *J. Phys. Chem. C* **2015**, *119*, 8438–8446.

(46) Bhauriyal, P.; Mahata, A.; Pathak, B. The Staging Mechanism of AlCl₄ Intercalation in a Graphite Electrode for an Aluminium-Ion Battery. *Phys. Chem. Chem. Phys.* **2017**, *19*, 7980–7989.

(47) Kravchyk, K. V.; Bhauriyal, P.; Piveteau, L.; Guntlin, C. P.; Pathak, B.; Kovalenko, M. V. High-Energy-Density Dual-Ion Battery for Stationary Storage of Electricity Using Concentrated Potassium Fluorosulfonylimide. *Nat Commun* **2018**, *9*, 4469.

(48) Placke, T.; Schmuelling, G.; Kloepsch, R.; Meister, P.; Fromm, O.; Hilbig, P.; Meyer, H.-W.; Winter, M. In Situ X-Ray Diffraction Studies of Cation and Anion Inter-calation into Graphitic Carbons for Electrochemical Energy Storage Applications: In Situ X-Ray Diffraction Studies for Electrochemical Energy Storage Applications. *Z. anorg. allg. Chem.* **2014**, *640*, 1996–2006.

(49) Özmen-Monkul, B.; Lerner, M. M. The First Graphite Intercalation Compounds Containing Tris(Pentafluoroethyl)Trifluorophosphate. *Carbon* **2010**, *48*, 3205–3210.

(50) Zhang, L.; Zhu, D.; Wang, H. How Ethyl Methyl Carbonate Assists Ethylene Carbonate in Co-Intercalating into Graphite Electrode with $PF_6^-$. *J. Electrochem. Soc.* **2019**, *166*, A2654–A2659.

(51) Fan, H.; Qi, L.; Wang, H. Hexafluorophosphate Anion Intercalation into Graphite Electrode from Methyl Propionate. *Solid State Ionics* **2017**, *300*, 169–174.

(52) Fan, H.; Gao, J.; Qi, L.; Wang, H. Hexafluorophosphate Anion Intercalation into Graphite Electrode from Sulfolane/Ethylmethyl Carbonate Solutions. *Electrochimica Acta* **2016**, *189*, 9–15.

(53) Fan, H.; Qi, L.; Yoshio, M.; Wang, H. Hexafluorophosphate Intercalation into Graphite Electrode from Ethylene Carbonate/Ethylmethyl Carbonate. *Solid State Ionics* **2017**, *304*, 107–112.

(54) Fan, H.; Qi, L.; Wang, H. Intercalation Behavior of Hexafluorophosphate into Graphite Electrode from Propylene/Ethylmethyl Carbonates. *J. Electrochem. Soc.* **2017**, *164*, A2262–A2267.

(55) Han, H.-B.; Zhou, S.-S.; Zhang, D.-J.; Feng, S.-W.; Li, L.-F.; Liu, K.; Feng, W.-F.; Nie, J.; Li, H.; Huang, X.-J. Lithium Bis(Fluorosulfonyl)Imide (LiFSI) as Conducting Salt for Nonaqueous Liquid Electrolytes for Lithium-Ion Batteries: Physicochemical and Electrochemical Properties. *Journal of Power Sources* **2011**, *196*, 3623–3632.

(56) Nobuhara, K.; Nakayama, H.; Nose, M.; Nakanishi, S.; Iba, H. First-Principles Study of Alkali Metal-Graphite Intercalation Compounds. *Journal of Power Sources* **2013**, *243*, 585–587.

(57) Persson, K.; Hinuma, Y.; Meng, Y. S.; Van der Ven, A.; Ceder, G. Thermodynamic and Kinetic Properties of the Li-Graphite System from First-Principles Calculations. *Phys. Rev. B* **2010**, *82*, 125416.

Table of Content Graphic

![](./images/812737131637112832_9.jpg)