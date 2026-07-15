# Enhanced Antibiotic Pollutant Capture: Coupling Carbon Nanotubes with Covalent Organic Frameworks

Afsaneh Ghahari and Heidar Raissi*

Cite This: *J. Phys. Chem. C* 2024, 128, 17141−17152

---

ABSTRACT: Antibiotics, recognized for their toxicity and persistence in aquatic environments, are emerging pollutants, prompting extensive research into removal technologies. The exclusion mechanisms of antibiotics (NOPs) such as norfloxacin (NOR), ofloxacin (OFL), and pefloxacin (PEF) on novel covalent organic frameworks (COFs) and COF composites with carbon nanotubes (CNTs@COFs) were examined through molecular dynamics and metadynamics simulations. Our simulation results indicate that van der Waals (vdW) interactions are the primary attractive forces in the formation of NOP/COF and NOP/CNTs@COF complexes; however, electrostatic (Elec) and hydrophobic forces also play crucial roles. The energy analysis revealed that NOPs were adsorbed more rapidly onto CNTs@COFs, and the PEF-COF and CNTs@COF-OFL systems have the highest interaction energy. The total interaction energies were found to be −246.154 and −358.626 kJ mol⁻¹ for PEF-COFs and CNTs@COFs-OFL, respectively. These results from metadynamics simulations were further confirmed via molecular dynamics (MD) analysis, which showed that PEF-COFs and CNTs@COFs-OFL had higher free energy values when positioned closer to substrates.

![](./images/1056166325900017710_1.jpg)

## INTRODUCTION

Fluoroquinolones (FQs)¹ are a burgeoning group of contaminants, extensively employed in both human and veterinary medicine to combat bacterial infections. However, their pervasive use across various domains, including human healthcare, animal husbandry, and even aquaculture, leads to their constant excretion into the environment.¹ This widespread dissemination fosters the swift evolution of resistant bacteria and genes, diminishing these vital antibiotics' effectiveness. Over recent decades, FQs have garnered escalating significance in treating a wide array of bacterial infections in both human and animal populations.² In 2013, three out of the top five antibiotics utilized in human medicine were FQs: ofloxacin (OFL), norfloxacin (NOR), and pefloxacin (PEF).³ Furthermore, in the field of animal farming, the use of veterinary antibiotics reaches an astonishing amount of over 4000 tons annually for both enrofloxacin and ciprofloxacin. FQs predominantly infiltrate the natural environment through the discharge of wastewater from pharmaceutical production and the accumulation of solid waste from human and livestock sources.⁴ This ongoing release leads to the enduring presence of FQs in ecosystems, heightening the risk of bacterial resistance escalation and perturbing the vital functions of aquatic organisms, thereby posing substantial threats to ecological harmony.⁵ A range of technologies has been developed to address this challenge, encompassing adsorption,⁶ advanced oxidation processes,⁷ biodegradation, and membrane separation.⁸ Membrane separation and biodegradation, particularly ultrafiltration membranes, exhibit relatively lower removal efficiencies.⁹ Consequently, adsorption stands out as one of the most efficient technologies for pollutant elimination,¹⁰ owing to its straightforward operation and cost-effectiveness.¹¹,¹² The effectiveness of adsorption hinges on the selection of suitable adsorbents. Various materials have been employed for the removal of FQs, encompassing activated carbon,¹³,¹⁴ carbon nanotubes (CNTs),¹⁵ graphene,¹⁶ biochar porous, and resins.¹⁷ Although these adsorbents show promise in adsorbing FQs, there is a need for further enhancements in their selectivity and anti-interference capabilities. Adsorption is a fascinating and widely utilized method for removing various types of pollutants from aqueous solutions, owing to its low cost,¹⁸ wide-ranging applicability,¹⁹ simplicity,²⁰ and versatility.²¹ The effectiveness of the adsorbent is influenced by factors such as the dimensions of the adsorbent particles, its surface area,²² and the interactions occurring between the adsorbent and the target compounds. Covalent organic frameworks (COFs)²³ are structured porous materials formed through the self-assembly of organic building blocks.²⁴,²⁵ They have been studied extensively for diverse applications like membrane separa-

Received: July 11, 2024
Revised: September 18, 2024
Accepted: September 19, 2024
Published: September 25, 2024

---

© 2024 American Chemical Society
17141
https://doi.org/10.1021/acs.jpcc.4c04602
*J. Phys. Chem. C* 2024, 128, 17141−17152

tion, $^{26}$ adsorption, $^{27,28}$ sensing, $^{29}$ gas storage, $^{30}$ and catalysis. $^{31}$ COFs have displayed promise in various applications, serving as effective adsorbents for organic dyes and pharmaceuticals, $^{32,33}$ as well as carriers for drug delivery and the isolation of industrially relevant compounds. Furthermore, in recent years, the development of COF-based composites, which integrate COFs with materials like carbon nanomaterials, has introduced a novel class of porous hybrid materials. $^{34-36}$ COFs are considered favorable candidates for forming outer shell structures $^{37,38}$ (such as $Fe_{3}O_{4}@SiO_{2}@COF$ and CNT@COF) because of their inherent porosity, high activity, excellent stability, and other beneficial characteristics. The CNT composites have extensive significant interest because of the impressive mechanical strength and powerful electron transport capabilities inherent in CNTs. $^{39,40}$ CNTs represent a common form of one-dimensional material characterized by their nanoscale diameters and microscale lengths. To maximize the effectiveness of COF, it is directly integrated with CNT membranes, resulting in COF@CNT membranes with enhanced usability for practical applications. Through this straightforward coupling strategy, a high-performance membrane-type adsorbent is created. This innovation broadens the applications of COF@CNT in pollutant removal and paves the way for producing more practical adsorbents, ensuring large accessible surface areas for effective pollutant adsorption. $^{41,42}$ Recently, Thakkar and colleagues $^{43}$ synthesized a barbituric acid-based COF composites utilizing CNTs for targeted applications and effective dye exclusion. The COF-CNT composite demonstrated superior adsorption capacities, achieving 234.57 mg/g for methyl orange and 603.91 mg/g for malachite green. In tests involving binary dye mixtures, the COF showed strong potential for dye separation, while the COF@CNT composite performed exceptionally well in removing dyes simultaneously. These substrates, characterized by their high efficiency in adsorption, demonstrate potential as recyclable materials for practical applications in wastewater treatment. In our previous work, we demonstrated that COFs can efficiently capture phenol toxins $^{44}$ and pharmaceutical contaminants $^{27}$ from aqueous solutions. Over the past few decades, some research on CNTs@COF composite adsorbents for pollutant capture has been conducted to better meet practical application needs.

Liu et al. $^{45}$ synthesized COFs onto the external CNTs to create a COF-OH@CNT composite for excluding uranium from wastewater. Their results showed that the COF-OH@ CNT composite significantly improves the selectivity and adsorption capacity for uranium ions. Additionally, they found that the COFs supported by CNTs improve removal efficiency and reduce structural collapse. Hao et al. $^{46}$ fabricated the sensor COF/platinum nanoparticle (PtNP) composite for the detection of OFX in water. They found that the TAPB-TPA-COF/PtNP/glassy carbon electrode (GCE) electrochemical sensor, with its excellent performance, offers great potential for the rapid and trace detection of residual OFX. In addition, Yuan et al. $^{47}$ introduced a novel MOF/COF composite by combining $NH_{2}$-MIL-53(Fe) with triazine-containing Tp-TTA. This composite could effectively adsorb and remove four representative antibiotics (tetracycline, ciprofloxacin, OFL, and norfloxacin). Their thermodynamic findings confirmed that the adsorption processes for tetracycline and ciprofloxacin were spontaneous.

Herein, we can gain further insights into the adsorption mechanism of NOR, OFL, and PEF antibiotic molecules (NOPs) on COF-based substrates and their migration toward the adsorbent surface with MD simulations and well-tempered metadynamics. Hence, we performed a comprehensive system analysis to evaluate the suitability of COFs and CNTs@COFs as adsorbents for interacting with antibiotic molecules. This analysis included the evaluation of the energy values, root mean square deviation, root mean square fluctuation, mean square displacement, and radial distribution function. The results evidence that rationally designing the CNTs@COFs can dramatically improve antibiotic contaminant exclusion in an aqueous solution. In addition, based on this architecture, the results indicate that the CNTs@COF substrate outperforms COF materials in capturing contaminants during simulation processes, resulting in the highest exclusion of antibiotics. These adsorbents, known for their high efficiency in adsorption, hold promise as effective and recyclable materials suitable for effective wastewater treatment. This study aims to offer future insights into the design and application of COF-based composites.

## METHODS
MD Simulation Section. Molecular dynamics (MD) simulations have been utilized to gain insights into the ability of the COFs and CNTs@COFs as adsorbent materials for excluding pollutants of OFL, NOR, and PEF molecules. This work compares two key structural compositions, COFs and CNTs@COFs, as adsorbent materials for removing OFL, NOR, and PEF contaminant molecules. Notably, the initial geometry of the COF material is based on the X-ray data from Zhang et al.'s work. This study is inspired by the work of Lei et al., $^{48}$ Jin's group, $^{49}$ Kong et al., $^{50}$ Gan et al., $^{51}$ and Duan and coworkers, $^{52}$ where the condensation of 1,3,5-triformylbenzene with 2,5-diethoxyterephthalohydrazide yields a new COF, as shown in Figure 1. Afterward, CNTs are vertically integrated into the surface of the COFs to create CNTs@COF hybrid nanomaterials. The high surface area of both COFs and CNTs@COFs provides numerous active sites for molecule capture. This increased surface area enhances the interaction between molecules and the adsorbents, improving pollutant removal. The design of the COFs and CNTs@COFs as adsorbents is depicted in Figure 1. Compared to bulk COFs, CNTs@COF composites offer more active and accessible sites, resulting in faster diffusion kinetics of molecules. This simple

![](./images/1056166325900017710_2.jpg)

Figure 1. Schematic representation of COFs and CNTs@COFs. Color code: C, cyan; O, red; N, blue; and H, white.


coupling strategy has led to the fabrication of a high-performance adsorbent, providing a new method for removing pollutants from aqueous media. After an initial equilibration process, MD simulations are performed with a time step of 2 fs at a temperature of 298 K. The interactions between molecules are described using a combination of long-range Coulombic forces and an analytical function that models van der Waals forces, which include short-range repulsions. The Nosé–Hoover thermostat is utilized for temperature control. The NPT ensemble with a Parrinello–Rahman barostat is used to examine thermal expansion. Table 1 contains information regarding the dimensions of the simulation boxes and the total count of antibiotic molecules for each system. The initial atomic coordinates in the MD simulations are determined through a packing optimization technique utilizing the Packmol program. Periodic boundary conditions are applied in all three dimensions. To calculate the electrostatic energy of COFs/CNTs@COFs with NOPs, partial atomic charges are obtained from the results of natural bond orbital (NBO) analysis. The force field parameters for the COF/CNT materials and NOP molecules are derived from the CHARMM36 force field. It is noteworthy to mention that the structure and topology of the NOP molecules were acquired from data sourced from the PubChem database and the SwissParam web server. To determine the electrostatic energy of COF/CNT, the partial atomic charges are obtained from the NBO analysis results. The analysis is performed at the M06-2X/6-31G** level of theory using the Gaussian 09 package. We employed GaussView 6.0 to design the initial structures for the simulation. Subsequently, MD simulations focusing on adsorbents were carried out using the GROMACS program, incorporating three different NOPs (NOR, OLF, and PEF). Visualization of the simulations is acquired using the VMD (Visual Molecular Dynamics) software package for graphics. Following energy minimization, each system undergoes equilibration for 200 ps within an NVT ensemble, followed by an additional stabilization period of 500 ps in an NpT ensemble. Following this, MD simulations are carried out for each system throughout 50 ns, employing a time step of 0.15 fs. At the same time, the simulation systems are designed as potential adsorbent materials for NOPs.

**Table 1. Detail of the Simulation Boxes in This Study**

<table>
  <thead>
    <tr>
      <th>systems</th>
      <th>no. of NOPs</th>
      <th>no. of CNT</th>
      <th>box size (nm³)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PEF/COFs</td>
      <td>6</td>
      <td>4</td>
      <td>$6×9×14$</td>
    </tr>
    <tr>
      <td>OFL/COFs</td>
      <td>6</td>
      <td>4</td>
      <td>$6×9×14$</td>
    </tr>
    <tr>
      <td>NOR/COFs</td>
      <td>6</td>
      <td>4</td>
      <td>$6×9×14$</td>
    </tr>
    <tr>
      <td>PEF/CNTs@COFs</td>
      <td>6</td>
      <td>4</td>
      <td>$6×9×14$</td>
    </tr>
    <tr>
      <td>OFL/CNTs@COFs</td>
      <td>6</td>
      <td>4</td>
      <td>$6×9×14$</td>
    </tr>
    <tr>
      <td>NOR/CNTs@COFs</td>
      <td>6</td>
      <td>4</td>
      <td>$6×9×14$</td>
    </tr>
  </tbody>
</table>

**Metadynamics Simulations.** Metadynamics, as an atomistic simulation method, enables the acceleration of infrequent occurrences and the estimation of free energy in complex molecular systems, all within a unified framework. In this study, the effectiveness of metadynamics has been assessed for the adsorption process of NOPs toward the active sites of the framework adsorbent (COFs and CNTs@COFs), particularly around the "N" and "O" heteroatoms. The fundamental concept underlying it involves iteratively adjusting the system's potential energy through a series of Gaussians centered along the trajectory determined by a carefully selected set of collective variables (CVs). Metadynamics simulations utilize the PLUMED plugin version 2.5.2,⁵³ which is seamlessly incorporated into the GROMACS software suite (version 2019.2). In the well-tempered metadynamics approach, the Gaussian bias potential starts with an initial height of 1.0 kJ/mol and a width of 0.25 Å. In addition, a bias factor of 15 is applied, with Gaussians being deposited every 500 time steps. The metadynamics simulations were performed for 50 ns on OFL-CNTs@COF and COF, NOR-CNTs@COF and COF, and PEF-CNTs@COF and COF systems.

## RESULT AND DISCUSSION

**MD Simulation.** MD simulation is employed to assess the potential of 2D materials in designing COF and CNTs@COF adsorbents with high efficiency in adsorbing FQ antibiotic molecules. In this study, our simulation is divided into two distinct setups of systems: one involving COFs and another incorporating CNTs@COFs (along with NOPs molecules, as outlined in Table 1).

![](./images/1056166325900017710_3.jpg)

**Figure 2.** Initial snapshots of the adsorbent with pollutant drug molecules. (a) Ofloxacin; (b) norfloxacin; (c) ciprofloxacin drug molecules.

Figures 2 and 3 depict the initial and concluding snapshots of the molecular structures of the OLF-COF and CNTs@COF, NOR-COF and CNTs@COF, and PEF-COF and CNTs@COF models observed in the 50 ns MD simulations. The pore size of COFs plays a pivotal role in determining the adsorption capacity of NOP molecules, with typical sizes being approximately NOR = 13.2 Å, OFL = 14.15 Å, and PEF = 14.14 Å. The assessment of molecular interactions revealed that the composite structure, wherein COFs encapsulate the CNT nanostructure, can significantly influence both the adsorption behavior and the total energy of the adsorbate molecule.

The exceptional stability and adsorption capacity of the CNTs@COFs as adsorbents can be attributed to their hybrid nanostructure, which is achieved through rational design and integration with the CNT channels' superior electron transfer capabilities. Notably, in the presence of CNTs, NOP molecules indicate an increased tendency to adsorb and interact with the substrate materials (see Figure 3). PEF, OFL, and NOR molecules, in particular, can establish robust $\pi-\pi$ stacking interactions with the substrate via their aromatic rings. It is worth noting that when adsorbing NOPs onto the porous structure, it is essential to ensure no volume change occurs. This is critical because any volume changes could compromise the structural integrity of the substrate and pose potential safety risks in the removal of contaminants. Significantly, including CNTs did not modify the crystal structure of the

![](./images/1056166325900017710_4.jpg)

Figure 3. (a) Final snapshots of the COF and CNTs@COF materials with the NOPs: (i) PEF/COF system, (ii) OFL/COF system, and (iii) NOR/COFs system. (b) Final snapshots of the CNTs@COFs materials with the NOPs: (i) OFL/CNTs@COF system, (ii) NOR/CNTs@COF system, and (iii) PEF/CNTs@COF system.

COFs, indicating that the composite maintained excellent crystallinity (see Figure 3). The exceptional architecture and integration of the COF and CNTs@COF composite materials have exhibited remarkable stability and reliability, making them highly effective for NOPs adsorption. As shown in Figure 3 a,b, most of the NOPs migrate toward the surface areas of the substrate, increasing the surface density. For example, in the presence of the CNTs@COF substrate, OFL and NOR molecules exhibit a stronger tendency to be adsorbed into the cavities of adsorbents and interact with the substrate. In the NOR-COF and PEF-CNTs@COF systems, the repulsion between the carboxylate groups of the COF structure and the carboxylic acid group on PEF reduces adsorption efficiency. On the other hand, NOR molecules have two significant ionizable functional groups: the 3-carboxyl group and the N4 of the piperazinyl group. This could potentially reduce the adsorption of contaminants by the substrate.

It is worth noting that these adsorbents show a high tendency for adsorbing PEF and OFL by COF and CNTs@ COF substrates, respectively, compared to other contaminants. This fact can be attributed to increased charge diffusion and a higher number of accessible NOPs sites, which enhance performance in the selective adsorption of contaminants. Hence, the advancement of OLF-CNTs@COFs and PEF- COFs contributes significantly to enhancing the long-term stability of the composite structure. In conclusion, the synergistic utilization of COFs and CNTs@COFs offers a promising approach for effectively eliminating antibiotics from aquatic environments, addressing the urgent requirement for sustainable remediation strategies.

Interaction Energies. The classical molecular dynamics simulation calculation has recently gained attention among molecular researchers. These simulations show the molecular interactions at a microscopic scale and in the full atomic specification. In this context, numerous interaction mecha- nisms operate during MD simulation, facilitating contaminant adsorption onto the surface of the adsorbent. Among these, prominent forces include van der Waals interactions, electro- static attractions, and hydrogen bonding. The adsorption mechanism, a focal point of the simulation, is influenced by various factors, with molecular properties of the adsorbents being a significant parameter. For improving the performance of COFs, CNTs can be integrated to form CNTs@COF composites and enhance their overall properties. These

composites have gained popularity in environmental remediation, effectively encapsulating guest contaminants within their protective porous structures.

The interaction energies between species in simulation boxes can be determined using a combination of Lennard-Jones (LJ) and Coulombic potentials. However, the negative values observed in Table 2 and Figure 4 for the interaction energies confirm the significant potential of COFs and CNTs@COFs in excluding NOP contaminants. Moreover, the error bars are determined from statistical variance between individual simulation runs, as shown in Supplementary Figure 1. The bars represent the mean value, and the error bars depict standard deviations.

**Table 2. VdW, Elec, and Total Energies, All in kJ mol⁻¹**

| systems            | Elec    | vdW      | total    |
|--------------------|---------|----------|----------|
| PEF/COFs           | −69.05  | −177.104 | −246.154 |
| OFL/COFs           | −38.83  | −108.46  | −147.29  |
| NOR/COFs           | −44.69  | −76.95   | −121.64  |
| OFL/CNTs@COFs      | −35.32  | −323.306 | −358.626 |
| NOR/CNTs@COFs      | −63.33  | −285.44  | −348.77  |
| PEF/CNTs@COFs      | −109.394| −133.931 | −243.325 |

![](./images/1056166325900017710_5.jpg)

Figure 4. Interaction energies (electrostatic (Elec), van der Waals (vdW), and total energies) of the investigated systems, for the COFs and CNTs@COFs systems with the NOPs.

The average total interaction energies of NOPs with COF materials exhibit various negative values in the following order: COFs-PEF > COFs-OFL > COFs-NOR, with respective values of approximately $-246.154$, $-147.29$, and $-121.64$ kJ mol⁻¹. Similarly, the interaction energies of NOPs with composite structures are observed in the following order: CNTs@COFs-OFL > CNTs@COFs-NOR > CNTs@COFs-PEF, with total interaction values approximately $-358.626$, $-348.77$, and $-243.325$ kJ mol⁻¹, respectively. A comparison of the total energy values of the systems under study reveals that the COFs-PEF and CNTs@COFs-OFL configurations exhibit the highest interaction energies, indicating greater stability compared to the other systems. When considering the CNTs@COFs composite to modify the COF structure, it is important to note that its contaminant adsorption capacity is enhanced, particularly evident in the increased stability of the CNTs@COFs-OFL complex compared to the pristine COF structure. Moreover, the uniform COF layer contributes to enhancing the mechanical properties and hydrophilicity of the CNT membranes. Significantly, the amide group connected to C3 of the PEF molecule allowed the possibility of hydrogen bond interactions with the hydroxyl side chain within the active site of COFs, involving $\text{C=N}$, $\text{C=O}$, and $\text{C-H}$ bonds. The OFL molecules, belonging to the FQ family, feature a methyl group at the C-3 position of the oxazine ring, along with carboxyl and piperazinyl groups. These active site groups enhance interactions with the substrate adsorbents.

Root Mean Square Deviation (RMSD). By carrying out the RMSD analysis of the contaminant molecules and adsorbents, we further confirm the findings of our study. Stable structural features are crucial for optimizing both the adsorption process of adsorbents and enhancing recovery efficiency. According to Figure 5, the RMSD diagrams of the examined COF and CNTs@COF materials with NOPs suggest that all systems attained equilibrium within 0.2 ns. It is important to highlight that the structure and fluctuations of COFs and CNTs@COFs remained stable through the entire simulation period in all systems. Additionally, the results indicate a notable decrease in RMSD fluctuations over time. Moreover, the RMSD findings suggest that the framework of COFs remains nearly steady after the integration of CNTs,

![](./images/1056166325900017710_6.jpg)

Figure 5. RMSD for the stability of the COF and CNTs@COF systems.

![](./images/1056166325900017710_7.jpg)

Figure 6. RDF patterns, for the NOPs by COF and CNTs@COF substrates.

resulting in enhanced structural stability. Notwithstanding that, it is reasonable to anticipate that these substrates serve as suitable candidates for excluding the contaminants' NOPs.

Radial Distribution Functions. Furthermore, molecular interactions can be investigated by utilizing radial distribution functions (RDFs), which illustrate how molecules are distributed at a distance $r$ from the substrate. In this investigation, we examined the distribution of contaminant NOPs around the crystal structures through RDF analysis,⁵⁴ introduced via eq 2:

$$
g(r)=n(r)/2\pi r\Delta r\rho \tag{1}
$$

In this context, $g(r)$ denotes the RDF, offering insight into the likelihood of organic contaminant molecules being situated at a distance $r$ from a designated substrate. Meanwhile, the notation $n(r)$ denotes the number density of molecules at a specific distance $r$ from the reference species. Therefore, $r$ represents the width of the shell at distance $r$, while $\rho$ represents the total number density of molecules in the system under consideration. The findings of RDF analysis for the evaluated systems are illustrated in Figure 6. This analysis offers essential insights into the structure and interactions among the molecules under investigation. The order of peak heights in the RDF for the analyzed systems is as follows:

COFs − PEF > COFs − OFL > COFs − NOR

Additionally, with the composite materials, the order is as follows:

CNTs@COFs − OFL
> CNTs@COFs − NOR
> CNTs@COFs − PEF

As depicted in Figure 6, the PEF-COF and CNTs@COFs- OFL systems evidence the highest RDF peak, situated at distances of 0.51 and 0.46 nm from the substrates, respectively. This observation confirms that PEF and OFL molecules exhibit the strongest interaction with COFs and CNTs@ COFs, attributed to the interaction between the active sites of the materials and the aromatic rings of PEF and OFL. It is noteworthy that the highest peak of the $g(r)$ function for NOR/PEF in COF and CNTs@COF systems, respectively, is located farther away compared to other NOPs. The variation in distance may be explained by the larger size and stronger steric effects of these molecules, resulting in a more significant repulsive force. The RDF patterns depicted in Figure 6 highlight a notably strong interaction between substrates and NOPs. This may be attributed to the interaction between the hydroxyl group in NOPs and the COF and CNTs@COF adsorbents, in addition to the $\pi-\pi$ hydrophobic interactions among the aromatic ring compounds. The analysis demon- strated that the synergistic effect of CNTs@COFs significantly enhances the removal capacity of NOPs.

It is noteworthy that the noise observed in the RDFs, particularly for the COFs/NOP systems, can be attributed to the inherent characteristics of the pristine COF structure. In this structure, the presence of active sites leads to highly localized interactions, which can cause fluctuations in the RDF as these interactions are not uniformly distributed across the simulation space. Furthermore, the existence of composite structures, such as CNTs@COFs, introduces additional complexities. The CNTs within the composite can act as traps for the antibiotic molecules. During the simulation, this trapping effect can lead to variations in the spatial distribution of these molecules, resulting in a more stable RDF with fewer fluctuations in the CNTs@COFs-NOP systems. In addition, COFs with some specific functional groups can interact with NOPs to improve their performance, for example, the $\pi-\pi$ bonds of COFs (benzene, $C=C$, etc.) can improve the efficiency of electrons. Despite the noise of RDF diagrams, the peaks' locations and heights in the RDFs across Figure 6 are comparable, indicating that the essential interactions are consistent across these systems. For further analysis, the RDFs in Figure 6 provide crucial insights into the molecular distribution around the adsorbent substrate. The distinct peaks observed clearly indicate that the first coordination shell of the molecules is highly localized at the adsorbent sites, which signifies strong energy interactions between the molecules and the COF structure. Generally, the noise in the RDFs for the COFs-NOPs is primarily due to the active sites in the pristine COF structure, which leads to localized and nonuniform interactions.⁵⁵⁻⁵⁸ In contrast, the CNTs in the CNTs@COF composites help to stabilize these interactions, reducing noise. Nonetheless, the key features of the RDFs are consistent across both systems, and the analysis remains valid for understanding the molecular interactions at the adsorbent sites.

Mean Squared Displacement. The evaluation of mean squared displacement (MSD) is utilized to determine the

diffusion coefficient of molecules, employing the following equation:⁵⁹

$$
\operatorname{MSD}(\Delta t)=\left(r_{i}(\Delta t)-r_{i}(0)\right)^{2}=\left(\Delta r_{i}(\Delta t)\right)^{2} \tag{2}
$$

Here, $r_{i}(\Delta t)-r_{i}(0)$ represents the distance traveled by the center of mass (COM) of particle $i$ in a time interval of length $\Delta t$. The self-diffusion coefficient $(D_{i})$ is obtained from the long-term limit of MSD, utilizing Einstein's relation:⁶⁰

$$
D_{i}=\frac{1}{6} \lim _{\Delta t \rightarrow \infty} \operatorname{MSD}(\Delta t) \tag{3}
$$

The self-diffusion coefficients of the investigated NOP contaminants are provided in Table 3. It is noteworthy that the piperazinyl group of PEF with the active sites of the substrate materials.

The obtained results from RDF diagrams also confirm these findings, suggesting that NOR/PEF molecules are likely present at greater distances from the adsorbent in COF and CNTs@COF systems compared to other systems.

Table 3. Self-Diffusion Coefficient of NOP Molecules in the Investigated Systems

| systems | $D_{i}$ $(10^{-5}\ \text{cm}^{2}\ \text{s}^{-1})$ |
|---------|---------------------------------------------------|
| $D_{(\text{COFs-PEF})}$ | $0.0624\ (\pm\ 0.0156)$ |
| $D_{(\text{COFs-OFL})}$ | $0.0810\ (\pm\ 0.00000)$ |
| $D_{(\text{COFs-NOR})}$ | $0.1308\ (\pm\ 0.00001)$ |
| $D_{(\text{CNTs@COFs-OFL})}$ | $0.0058\ (\pm\ 0.0072)$ |
| $D_{(\text{CNTs@COFs-NOR})}$ | $0.0785\ (\pm\ 0.0322)$ |
| $D_{(\text{CNTs@COFs-PEF})}$ | $1.304\ (\pm\ 0.0000)$ |

lower slope evident in the MSD curves indicates that the adsorption of NOPs on the adsorbent disrupts the movement of contaminant molecules. In Figure 7, it is evident that the MSD curve for the COFs-PEF and CNTs@COFs-OFL systems exhibits a lower slope and a reduced self-diffusion coefficient (refer to Figure 7) compared to the others. These findings can be ascribed to the strong interaction between the NOPs and the COF/CNTs@COF substrates. Therefore, this interaction occurs due to the formation of hydrogen bonds between the active sites of NOPs and the COF/CNTs@COF adsorbents. For example, the 4-methyl-1-piperazinyl groups of PEF and the benzoxazine moiety, specifically 1,4-benzoxazine-6-carboxylic acid, of OFL molecules interact with the surface of the adsorbents. Moreover, attractive van der Waals forces, notably $\text{C}-\text{H}\cdots\pi$ and $\pi-\pi$ interactions, contribute significantly to this interaction. Our findings demonstrate that the slope of the MSD curve is higher for the COFs-NOR and CNTs@ COFs-PEF systems compared to others. This is probably owing to the repulsive interactions involving the 1-piperazinyl-3-quinoline carboxylic acid group of NOR and the 4-methyl-1-

Solvent-Accessible Surface Area. The solvent-accessible surface area (SASA) analysis in MD simulations enables the examination of the contact areas between each of the three antibiotic molecules adsorbed on the substrate surface and solvent. This analysis assesses the capacity of COFs and CNTs@COFs to offer adequate accessible areas for con- taminants removal. When NOPs adhere to adsorbents, they exhibit reduced dispersion in water, resulting in a decreased average SASA value. Meanwhile, the desirable result is the significant adsorption of more contaminant molecules, facilitated by the greater contact surface between NOPs and COF and CNTs@COF materials. In this regard, favorable conditions are created for the interaction between NOPs and substrates, which leads to a significant accumulation of OFL, PEF, and NOR around COFs/CNTs@COFs. Additionally, Figure 8 illustrates that the hydrophobic SASA decreases over time for most systems. This reduction is due to the interactions between the hydrophobic structures of COFs/CNTs@COFs and the aromatic rings of NOPs (see Figure 3 and Supplementary Figure 2). Therefore, the more effectively an adsorbent captures NOPs, the less surface area of these molecules remains exposed to the solvent. Our results indicate that the SASA values for NOR and PEF in the CNTs@COF systems were more than in the other systems, with values of approximately 45.66 and 52.78, respectively. Examination of Figure 8 reveals the hierarchy of hydrophobic solvent-accessible surface areas in CNTs@COFs and COF systems as follows:
$$
\begin{aligned}
\text { CNTs@COFs }- \text { OFL } & >\text { CNTs@COFs }- \text { NOR } \\
& >\text { CNTs@COFs }- \text { PEF, and COFs }- \text { PEF } \\
& >\text { COFs }- \text { OFL }>\text { COFs }- \text { NOR }
\end{aligned}
$$

The high SASA value observed in the CNTs@COFs-PEF system confirms its larger surface area available to interact with water molecules. Furthermore, as depicted in Figure 8, CNTs@COFs exhibit remarkable adsorption performance, evidenced by the minimal interaction area of NOPs with the

![](./images/1056166325900017710_8.jpg)

Figure 7. MSD plots, for NOR/OFL/PEF with COF and CNTs@COF materials.

![](./images/1056166325900017710_9.jpg)

Figure 8. SASA diagrams for NOPs/COFs and NOPs/CNTs@COFs.

![](./images/1056166325900017710_10.jpg)

Figure 9. Profile density of NOPs in the studied systems: (a) NOPs/COFs and (b) NOPs/CNT@COFs.

solvent. This result lines up with previous MD simulation findings.

Density. The density profile ($\rho$) along in the direction of the $z$-axis of the simulation box was analyzed to establish the positioning of NOPs to the surfaces of COFs and CNTs@ COFs. Appreciating the density profile is vital, with $\rho$ representing NOP molecule density. We have calculated the density profile of NOPs along the $z$-axis of the adsorbents for the systems being analyzed. It is important to note that the decrease in the lowest peak of the density profile could stem from a decline in the number of NOP molecules around the surface of the adsorbent. As shown in Figure 9, each system displays prominent oscillatory density peaks, indicating the presence of stacking arrangement structures and pore cavities in both COFs and CNTs@COFs, which confine NOP molecules. The first peak for the density profile (0.42 nm in PEF-COFs and 0.96 nm in CNT@COFs-OFL) can be attributed to the accumulation of molecules on the surface of the substrate due to the formation of hydrogen bonds and $\pi-\pi$ stack interaction between substrate and NOP contaminant molecules. The relevant results can be ascribed to the orientation of NOPs to find better adsorption on the substrates. Accordingly, the PEF molecules interact more with the active center of the COF structure, such as the $\mathrm{C=C}$, carbonyl group, and $\mathrm{C-CN}$, through hydrogen bonds. Additionally, these findings confirm that PEF and OFL molecules rotated to form $\pi-\pi$ interaction with COF and CNTs@COF systems.

As evident in Figure 9, the distribution of NOP molecules shows notable symmetry close to the surface, highlighting the impact of the adsorbents on the adsorption of NOP pollutant molecules in water. The results indicate that regions with lower density of NOP molecules correspond to areas where the concentration of antibiotic pollutants near the surface is lower. However, in the PEF-COF systems, it is observed that the higher contaminant density coincided with the peak adsorption of pollutant molecules. Additionally, Figure 9 illustrates the density distribution of NOPs around the CNTs@COFs, emphasizing the highest adsorption of molecules in proximity to the adsorbent surface. The inclusion of CNTs in the COF structure facilitates the migration of antibiotics to the active site, driven by their high electron transport, positioning them in proximity to the composite structure. This phenomenon not only boosts the adsorption capacity of the composite material for antibiotics but also enhances the activity of the active site substrate. It is worth noting that the overall shapes of the density profiles are similar across all systems. Moreover, the densities for the PEF-COFs and CNTs@COFs-OFL systems are approximately 120.8 and $216.21 \mathrm{~kg} \mathrm{~m}^{-3}$, respectively.

Our findings indicate that CNTs@COFs, serving as effective and customizable adsorbents, exhibit substantial promise in the removal of NOP pollutants, consistent with experimental observations. For example, Liu et al. $^{45}$ synthesized COFs on the surface of CNTs to create a composite known as CNT/ COF-OH, aimed at removing uranium from rare earth tailings wastewater. Their relevant results demonstrate that COFs with redox-active sites on the surface of CNTs, specifically in the

![](./images/1056166325900017710_11.jpg)

Figure 10. Number of hydrogen bonds for NOPs in the COF and CNTs@COF systems with the water molecules. (a) NOPs/COFs. (b) NOPs/water in COF systems. (c) NOPs/CNTs@COFs. (d) NOPs/water in CNTs@COF systems.

![](./images/1056166325900017710_12.jpg)

Figure 11. Free energy profile the NOPs with the COF and CNTs@COF substrates.

CNT/COF-OH composite, effectively improve both the selectivity for uranium ions and the adsorption capacity.

Hydrogen Bond Formation Potential. To evaluate hydrogen bond (H-bond) patterns, analyzing H-bonds requires more than just simple statistical criteria, like the number of hydrogen bonds per molecule. This requires establishing a precise probability distribution for neighboring electronegative atoms observed within simulations. The

examination of hydrogen bonds in the systems under investigation concentrated on pairs of donors and acceptors. Figure 10 depicts how hydrogen bond formation among different components changes throughout the simulation. The research recognized three types of H-bonds, each involving the hydrogen from the network hydroxyl group and one of the three acceptors. (a) Hydroxyl group oxygen (OH): this refers to a hydrogen bond formed between the oxygen and the hydrogen from a hydroxyl group of another hydroxyl group within the network. (b) Ether group oxygen (O═C): this type of hydrogen bond forms between the hydrogen of a hydroxyl group and the oxygen atom within the ether linkage of the network. (c) Nitrogen of the network tertiary amine (N−C): this hydrogen bond occurs between the hydrogen of a hydroxyl group and the nitrogen atom in the tertiary amine within the network. These interactions demonstrate how hydrogen bonding in the system is dynamic, playing a role in the network's overall stability and properties. Accordingly, this increased stability is crucial for the effective adsorption and removal of contaminants, as it enhances the binding affinity between the COFs/CNTs@COF framework and the NOP molecules. In addition, the vdW interaction, the adsorption process between adsorbent materials and antibiotic contaminants, is influenced by the formation of H-bonds, which play an essential role in their interactions. The findings in Figure 10 also show that in the PEF-COF and CNTs@COFs-OFL systems, more hydrogen bonds exist in comparison to other molecules. This is because NOP molecules, such as PEF and OFL, interact more extensively with the COF and CNTs@ COF surfaces, respectively. In other words, the COF skeleton, when supported by CNTs, improves the chemical and structural stability of the material. The adsorption of CNTs@COFs exhibited a much steeper trend, as shown in Figure 3, indicating that its adsorption affinity for NOPs was stronger than that of the COF adsorbent alone. Consequently, the presence of CNTs is covered with COFs, leading to a significant increase in the number of host−guest hydrogen bonds. Notably, in these systems, it is noted that the number of hydrogen bonds between NOP molecules and water molecules decreases, as illustrated in Figure 10. Thus, it can be deduced that hydrogen bonding played a pivotal role in driving the adsorption phenomenon of NOPs on both the CNTs@COFs and COFs' surfaces.

Metadynamics. The application of well-tempered meta- dynamics simulation not only expedites the occurrence of rare events but also provides a detailed elucidation of the free energy surface (FES), shedding light on the intricacies of complex molecular systems. In comparison to bulk COFs, the CNTs@COF composites provide more exposed and accessible active sites, enabling faster NOP diffusion and leading to enhanced adsorption capacity. For this reason, the calculation of the FES is carried out on CNTs@COF adsorbents. The diagrams depicted in Figure 11 illustrate the FES plotted against the distance between the centers of masses of the COFs@CNT adsorbents and NOP molecule contaminants. As identified in Figure 11, the free energy is set to zero when the NOP molecule is at a considerable distance from the CNTs@ COF substrate. As the NOPs migrate into the cavities of the adsorbent material during the adsorption process, the free energy surface becomes progressively negative; these systems encounter energy barriers and local minima as they move toward the global minimum. The free energy values at the global minima for the PEF, OFL, and NOR-COFs complexes are about $\sim$-400.41, -331.75, and -302.93 kJ mol⁻¹, and those for OFL, NOR, and PEF in CNTs@COFs are approximately -734.27, -287.64, and -267.76 kJ mol⁻¹, respectively. The patterns from the results shown in Figure 11 indicate that hat PEF/OFL exhibits a more negative free energy surface relative to the others in COF/CNTs@COF systems, confirming the total energy interaction (seen in Table 2). A notable active site group in OFL is the carboxylic acid moiety, which can interact with adsorbents through hydrogen bonding and electrostatic interactions, potentially facilitating surface adsorption. In addition, the fluorine atoms in the FQ ring system can also contribute to interactions, especially with specific functional groups or reactive sites on the COF surface. In addition, a piperazine ring can serve as another active site for potential interactions with covalent organic surfaces.

Furthermore, the PEF-COF and CNTs@COFs-OFL systems face relative energy barriers of approximately 86.52 and 601.09 kJ mol⁻¹, respectively, as depicted in Figure 11. These results are consistent with the findings obtained from RDF analysis in MD simulations. It is noteworthy that as the NOP molecules approach the surface of CNTs@COFs, there is a discernible decline in free energy after surpassing the initial barrier. This incremental advancement eventually stabilizes the system. Furthermore, the results demonstrate that CNTs@ COFs exhibit ultrahigh adsorption capacity for NOPs and are also more effective in removing OFL from water.

## DISCUSSION AND CONCLUSIONS
In summary, this study investigates the behavior of antibiotic pollutants when they are adsorbed on COFs and CNTs@ COFs in an aqueous environment, employing MD and metadynamics simulations. The findings reveal that integrating CNTs into the COF structure can boost the electron density of the composite, thereby augmenting the interaction energy of NOPs. The research confirms that the substrates of COFs and CNTs@COFs in all examined systems spontaneously attract NOP pollutant molecules. Moreover, it demonstrates that NOP molecules are most strongly adsorbed in the CNTs@ COFs-OFL and PEF-COF configurations compared to other systems. Due to the heightened occurrence of hydrogen bonds and $\pi-\pi$ interactions in the NOP/CNTs@COF systems, NOPs are more strongly attracted to the CNTs@COF surfaces compared to the COF system. The analysis of hydrogen bonding underscores NOPs' superior ability to form hydrogen bonds with CNTs@COFs. Consequently, $\pi-\pi$ interactions and hydrogen bonds are identified as crucial interactions in the studied systems. Additionally, the radial distribution function analysis reveals a significant peak between 0.4 and 0.5 nm, indicating the heightened affinity of PEF and OFL molecules to adsorb onto the surfaces of COFs and CNTs@COFs, respectively. As per the analysis of the free energy surface, NOP molecules need to surpass an energy barrier to reach the global minimum. Given their considerable potential, both CNTs@COFs and COFs emerge as highly promising contenders in the detection and removal of antibiotics. This marks a pivotal advancement in antimicrobial research and environmental remediation, paving the way for a new frontier in this crucial field.

## ASSOCIATED CONTENT
### Data Availability Statement
The authors can confirm that all relevant data are included in the article file.


Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpcc.4c04602.

(Figure S1) interaction energy between NOP molecules and (a) COFs and (b) CNTs@COFs; (Figure S2) vdW and Elec interaction energies between the PEF molecules and (a) COFs and (b) CNTs@COFs as a function of simulation time—MD force field (ffnonbonded.itp, structurs of.itp files, etc.) for the studied systems (PDF)

## AUTHOR INFORMATION

### Corresponding Author
Heidar Raissi − Department of Chemistry, University of Birjand, Birjand 9717434765, Iran; ⓒ orcid.org/0000-0003-1473-1501; Phone: +985632502064;
Email: hraeisi@birjand.ac.ir

### Author
Afsaneh Ghahari − Department of Chemistry, University of Birjand, Birjand 9717434765, Iran; ⓒ orcid.org/0000-0003-0679-4721

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcc.4c04602

### Author Contributions
A.G. devised the computational protocol and prepared the model systems, performed all calculations, analyzed the data, wrote and edited the original and the revised manuscript, reviewing—editing, and edited the original and revised versions of the manuscript. H.R. supervised the study, devised the computational protocol, prepared the model systems, reviewing, and editing, and edited the original and revised versions of the manuscript.

### Notes
The authors declare no competing financial interest.

## REFERENCES
(1) Thai, V.-A.; Dang, V. D.; Thuy, N. T.; Pandit, B.; Vo, T. K. Q.; Khedulkar, A. P. Fluoroquinolones: Fate, Effects on the Environment and Selected Removal Methods. J. Cleaner Prod. 2023, 418, No. 137762.
(2) Chakraborty, A.; Adhikary, S.; Bhattacharya, S.; Dutta, S.; Chatterjee, S.; Banerjee, D.; Ganguly, A.; Rajak, P. Pharmaceuticals and Personal Care Products as Emerging Environmental Contaminants: Prevalence, Toxicity, and Remedial Approaches. ACS Chem. Health Saf. 2023, 30 (6), 362−388.
(3) Meng, F.; Sun, S.; Geng, J.; Ma, L.; Jiang, J.; Li, B.; Yabo, S. D.; Lu, L.; Fu, D.; Shen, J.; Qi, H. Occurrence, Distribution, and Risk Assessment of Quinolone Antibiotics in Municipal Sewage Sludges throughout China. J. Hazard. Mater. 2023, 453, No. 131322.
(4) Adesina, M. O.; Alfred, M. O.; Olorunnisola, C. G.; Olayanju, O. K.; Oladoja, N. A.; de Camargo, A. S. S.; Unuabonah, E. I. Green Chemistry Perspective as a Driver in the Removal of Endocrine Disruptive Chemicals from Water. In Sustainable Agricultural Practices and Product Design; ACS Publications, 2023; pp 101−122.
(5) Jiang, Z.; Sun, S.; Liu, J.; Sun, X. Recent Advances of Halloysite Nanotubes in Biomedical Applications. Small 2024, 20 (2), No. 2306169.
(6) Samadi, A.; Wang, Z.; Wang, S.; Nataraj, S. K.; Kong, L.; Zhao, S. Polyaniline-Based Adsorbents for Water Treatment: Roles of Low- Cost Materials and 2D Materials. Chem. Eng. J. 2023, 478, No. 147506.
(7) Preethi; Shanmugavel, S. P.; Kumar, G.; N, Y. K.; M, G.; J, R. B. Recent Progress in Mineralization of Emerging Contaminants by Advanced Oxidation Process: A Review. Environ. Pollut. 2023, 341, No. 122842.
(8) Wang, D.; Xing, Y.; Li, J.; Dong, F.; Cheng, H.; He, Z.; Wang, L.; Giannakis, S.; Song, S.; Ma, J. Degradation of Odor Compounds in Drinking Water by Ozone and Ozone-Based Advanced Oxidation Processes: A Review. ACS ES&T Water 2023, 3 (11), 3452−3473.
(9) Qiu, Y.; Depuydt, S.; Ren, L.-F.; Zhong, C.; Wu, C.; Shao, J.; Xia, L.; Zhao, Y.; Van der Bruggen, B. Progress of Ultrafiltration-Based Technology in Ion Removal and Recovery: Enhanced Membranes and Integrated Processes. ACS ES&T Water 2023, 3 (7), 1702−1719.
(10) Wang, Y.; Zucker, I.; Boo, C.; Elimelech, M. Removal of Emerging Wastewater Organic Contaminants by Polyelectrolyte Multilayer Nanofiltration Membranes with Tailored Selectivity. ACS ES&T Eng. 2020, 1 (3), 404−414.
(11) Noah, N. M. Current Status and Advancement of Nanomaterials within Polymeric Membranes for Water Purification. ACS Appl. Nano Mater. 2023, 7, 18610.
(12) Chaudhary, M.; Sela-Adler, M.; Ronen, A.; Nir, O. Efficient PFOA Removal from Drinking Water by a Dual-Functional Mixed- Matrix-Composite Nanofiltration Membrane. npj Clean Water 2023, 6 (1), 77.
(13) Phoon, B. L.; Ong, C. C.; Mohamed Saheed, M. S.; Show, P.- L.; Chang, J.-S.; Ling, T. C.; Lam, S. S.; Juan, J. C. Conventional and Emerging Technologies for Removal of Antibiotics from Wastewater. J. Hazard. Mater. 2020, 400, No. 122961.
(14) Martín-Pozo, L.; del Carmen Gómez-Regalado, M.; García- Córcoles, M. T.; Zafra-Gómez, A. Removal of Quinolone Antibiotics from Wastewaters and Sewage Sludge. In Emerging Contaminants in the Environment; Elsevier, 2022; pp 381−406.
(15) Hassani, A.; Khataee, A. Carbon Nanomaterials for Removal of Pharmaceuticals from Wastewater. In Nanomaterials for Water Treatment and Remediation; CRC Press, 2021; pp 333−369.
(16) Ghosh, R.; Hareendran, H.; Subramaniam, P. Adsorption of Fluoroquinolone Antibiotics at the Gas−Liquid Interface Using Ionic Surfactants. Langmuir 2019, 35 (39), 12839−12850.
(17) Jia, Y.; Ou, Y.; Khanal, S. K.; Sun, L.; Shu, W.-s.; Lu, H. Biochar-Based Strategies for Antibiotics Removal: Mechanisms, Factors, and Application. ACS ES&T Eng. 2024, 4, 1256.
(18) Belaye, M.; Taddesse, A. M.; Teju, E.; Sanchez-Sanchez, M.; Yassin, J. M. Preparation and Adsorption Behavior of Ce (III)-MOF for Phosphate and Fluoride Ion Removal from Aqueous Solutions. ACS omega 2023, 8 (26), 23860−23869.
(19) Dey, S.; Manna, K.; Pradhan, P.; Sarkar, A. N.; Roy, A.; Pal, S. Review of Polymeric Nanocomposites for Photocatalytic Wastewater Treatment. ACS Appl. Nano Mater. 2024, 7, 4588.
(20) Bello, M. M.; Raman, A. A. A. Adsorption and Oxidation Techniques to Remove Organic Pollutants from Water. green adsorbents Pollut. Remov. Fundam. Des. 2018, 18, 249−300.
(21) Ukani, H.; Mehra, S.; Parmar, B.; Kumar, A.; Khan, I.; El Seoud, O. A.; Malek, N. Metal−Organic Framework-Based Aerogel: A Novel Adsorbent for the Efficient Removal of Heavy Metal Ions and Selective Removal of a Cationic Dye from Aqueous Solution. Ind. Eng. Chem. Res. 2023, 62 (12), 5002−5014.
(22) Khojastehnezhad, A.; Moeinpour, F.; Jafari, M.; Shehab, M. K.; Samih EIDouhaibi, A.; El-Kaderi, H. M.; Siaj, M. Postsynthetic Modification of Core−Shell Magnetic Covalent Organic Frameworks for the Selective Removal of Mercury. ACS Appl. Mater. Interfaces 2023, 15 (23), 28476−28490.
(23) Tan, K. T.; Ghosh, S.; Wang, Z.; Wen, F.; Rodríguez-San- Miguel, D.; Feng, J.; Huang, N.; Wang, W.; Zamora, F.; Feng, X.; Thomas, A.; Jiang, D. Covalent Organic Frameworks. Nat. Rev. Methods Primers 2023, 3 (1), 1.
(24) Dai, L.; Wu, F.; Xiao, Y.; Liu, Q.; Meng, M.; Xi, R.; Yin, Y. Template-Free Self-Assembly of Hollow Microtubular Covalent Organic Frameworks for Oral Delivery of Insulin. ACS Appl. Mater. Interfaces 2024, 16 (14), 17891−17903.

(25) Zhao, Y.; Li, S.; Fu, G.; Yang, H.; Li, S.; Wu, D.; Zhang, T. Construction of Layer-Blocked Covalent Organic Framework Heterogenous Films via Surface-Initiated Polycondensations with Strongly Enhanced Photocatalytic Properties. ACS Cent. Sci. 2024, 10, 775.

(26) Asif, M. B.; Kim, S.; Nguyen, T. S.; Mahmood, J.; Yavuz, C. T. Covalent Organic Framework Membranes and Water Treatment. J. Am. Chem. Soc. 2024, 146, 3567.

(27) Akhzari, S.; Raissi, H.; Ghahari, A. Architectural Design of 2D Covalent Organic Frameworks (COFs) for Pharmaceutical Pollutant Removal. npj Clean Water 2024, 7 (1), 31.

(28) Ghahari, A.; Raissi, H.; Farzad, F. Design of a New Drug Delivery Platform Based on Surface Functionalization 2D Covalent Organic Frameworks. J. Taiwan Inst. Chem. Eng. 2021, 125, 15−22.

(29) Xue, R.; Liu, Y.-S.; Huang, S.-L.; Yang, G.-Y. Recent Progress of Covalent Organic Frameworks Applied in Electrochemical Sensors. ACS sensors 2023, 8 (6), 2124−2148.

(30) Kumar, Y.; Ahmad, I.; Rawat, A.; Pandey, R. K.; Mohanty, P.; Pandey, R. Flexible Linker-Based Triazine-Functionalized 2D Covalent Organic Frameworks for Supercapacitor and Gas Sorption Applications. ACS Appl. Mater. Interfaces 2024, 16, 11605.

(31) Wang, T.; Li, M.; Chen, Y.; Che, X.; Bi, F.; Yang, Y.; Yang, R.; Li, C. Regioisomeric Benzotriazole-Based Covalent Organic Frame- works for High Photocatalytic Activity. ACS Catal. 2023, 13 (23), 15439−15447.

(32) Ahmed, I.; Lee, G.; Lee, H. J.; Jhung, S. H. Adsorption of Pharmaceuticals from Water Using Metal-Organic Frameworks (MOFs), MOF-Derived Carbons, Covalent-Organic Frameworks (COFs), COF-Derived Carbons: Comparison of the Four Adsorb- ents. Chem. Eng. J. 2024, 488, No. 151022.

(33) Ruidas, S.; Chowdhury, A.; Ghosh, A.; Ghosh, A.; Mondal, S.; Wonanke, A. D. D.; Addicoat, M.; Das, A. K.; Modak, A.; Bhaumik, A. Covalent Organic Framework as a Metal-Free Photocatalyst for Dye Degradation and Radioactive Iodine Adsorption. Langmuir 2023, 39 (11), 4071−4081.

(34) Li, T.; Pan, Y.; Shao, B.; Zhang, X.; Wu, T.; He, Q.; He, M.; Ge, L.; Zhou, L.; Liu, S.; Zheng, X.; Ye, J.; Liu, Z. Covalent−Organic Framework (COF)-Core−Shell Composites: Classification, Synthesis, Properties, and Applications. Adv. Funct. Mater. 2023, 33 (45), No. 2304990.

(35) Ma, M.; Yang, Y.; Huang, Z.; Huang, F.; Li, Q.; Liu, H. Recent progress in the synthesis and applications of covalent organic frameworks-based composites. Nanoscale 2024, 16, 1600.

(36) Xue, H.; Bi, Z.; Cheng, J.; Xiong, S.; Wang, Y. Coupling Covalent Organic Frameworks and Carbon Nanotube Membranes to Design Easily Reusable Photocatalysts for Dye Degradation. Ind. Eng. Chem. Res. 2021, 60 (24), 8687−8695.

(37) Li, T.; Pan, Y.; Shao, B.; Zhang, X.; Wu, T.; He, Q.; He, M.; Ge, L.; Zhou, L.; Liu, S.; Zheng, X.; Ye, J.; Liu, Z. Covalent−Organic Framework (COF)-Core−Shell Composites: Classification, Synthesis, Properties, and Applications. Adv. Funct. Mater. 2023, 33 (45), No. 2304990.

(38) Sun, X.; Di, M.; Liu, J.; Gao, L.; Yan, X.; He, G. Continuous Covalent Organic Frameworks Membranes: From Preparation Strategies to Applications. Small 2023, 19 (44), No. 2303757.

(39) Zhang, S.; Ma, Y.; Suresh, L.; Hao, A.; Bick, M.; Tan, S. C.; Chen, J. Carbon Nanotube Reinforced Strong Carbon Matrix Composites. ACS Nano 2020, 14 (8), 9282−9319.

(40) Yang, X.; Lin, C.; Han, D.; Li, G.; Huang, C.; Liu, J.; Wu, X.; Zhai, L.; Mi, L. In Situ Construction of Redox-Active Covalent Organic Frameworks/Carbon Nanotube Composites as Anodes for Lithium-Ion Batteries. J. Mater. Chem. A 2022, 10 (8), 3989−3995.

(41) Yang, C.; Wang, K.; Lyu, W.; Liu, H.; Li, J.; Wang, Y.; Jiang, R.; Yuan, J.; Liao, Y. Nanofibrous Porous Organic Polymers and Their Derivatives: From Synthesis to Applications. Adv. Sci. 2024, 11, No. 2400626.

(42) Wen, C.; Yao, Y.; Meng, L.; Duan, E.; Wang, M.; Chen, Z.; Wang, X. Photocatalytic and Electrocatalytic Extraction of Uranium by COFs: A Review. Ind. Eng. Chem. Res. 2023, 62 (44), 18230−18250.

(43) Thakkar, H.; Bhatt, M.; Thakore, S. barbituric Acid Derived Covalent Organic Framework and Its CNT Composite as High- Performance Adsorbents for Organic Dye Removal. J. Environ. Chem. Eng. 2023, 11 (3), No. 109890.

(44) Ghahari, A.; Raissi, H.; Pasban, S.; Farzad, F. Proposing Two- Dimensional Covalent Organic Frameworks Material for the Capture of Phenol Molecules from Wastewaters. npj Clean Water 2022, 5 (1)..

(45) Liu, X.; Wang, X.; Jiang, W.; Zhang, C.-R.; Zhang, L.; Liang, R.- P.; Qiu, J.-D. Covalent Organic Framework Modified Carbon Nanotubes for Removal of Uranium (VI) from Mining Wastewater. Chem. Eng. J. 2022, 450, No. 138062.

(46) Hao, J.; Huang, L.; Zheng, L.; Wang, Q.; Yin, Z.; Li, H.; Jia, L.; Liao, W.; Liu, K. A Direct Electrochemical Sensor Based on Covalent Organic Frameworks/Platinum Nanoparticles for the Detection of Ofloxacin in Water. Microchim. Acta 2024, 191 (3), 145.

(47) Yuan, N.; Zhang, C.; Zhang, X.; Zhang, R. Covalent Integration of Fe-Based Metal−Organic Framework and Triazine-Containing Covalent Organic Framework for Enhanced Adsorptive Removal of Antibiotics. J. Clean. Prod. 2024, 434, No. 140259.

(48) Lei, Z.; Yang, Q.; Xu, Y.; Guo, S.; Sun, W.; Liu, H.; Lv, L. P.; Zhang, Y.; Wang, Y. Boosting Lithium Storage in Covalent Organic Framework via Activation of 14-Electron Redox Chemistry. Nat. Commun. 2018, 9 (1), 1−13.

(49) Jin, S.; Allam, O.; Jang, S. S.; Lee, S. W. Covalent Organic Frameworks: Design and Applications in Electrochemical Energy Storage Devices. InfoMat 2022, 4 (6), 1−35.

(50) Kong, X.; Zhou, S.; Strømme, M.; Xu, C. Redox Active Covalent Organic Framework-Based Conductive Nanofibers for Flexible Energy Storage Device. Carbon 2021, 171, 248−256.

(51) Gan, Z.; Lu, S.; Qiu, L.; Zhu, H.; Gu, H.; Du, M. Fine Tuning of Supported Covalent Organic Framework with Molecular Active Sites Loaded as Efficient Electrocatalyst for Water Oxidation. Chem. Eng. J. 2021, 415, No. 127850.

(52) Duan, J.; Wang, W.; Zou, D.; Liu, J.; Li, N.; Weng, J.; Xu, L.; Guan, Y.; Zhang, Y.; Zhou, P. Construction of a Few-Layered COF@ CNT Composite as an Ultrahigh Rate Cathode for Low-Cost K-Ion Batteries. ACS Appl. Mater. Interfaces 2022, 14 (27), 31234−31244.

(53) Bonomi, M.; Branduardi, D.; Bussi, G.; Camilloni, C.; Provasi, D.; Raiteri, P.; Donadio, D.; Marinelli, F.; Pietrucci, F.; Broglia, R. A.; Parrinello, M. PLUMED: A Portable Plugin for Free-Energy Calculations with Molecular Dynamics. Comput. Phys. Commun. 2009, 180 (10), 1961−1972.

(54) Burian, A.; Koloczek, J.; Dore, J. C.; Hannon, A. C.; Nagy, J. B.; Fonseca, A. Radial distribution function analysis of spatial atomic correlations in carbon nanotubes. Diamond Relat. Mater. 2004, 13, 1261−1265.

(55) Terban, M. W.; Billinge, S. J. L. Structural Analysis of Molecular Materials Using the Pair Distribution Function. Chem. Rev. 2022, 122 (1), 1208−1272.

(56) Sun, B.; Liu, J.; Cao, A.; Song, W.; Wang, D. Interfacial Synthesis of Ordered and Stable Covalent Organic Frameworks on Amino-Functionalized Carbon Nanotubes with Enhanced Electro- chemical Performance. Chem. Commun. 2017, 53 (47), 6303−6306.

(57) Xu, J.; He, Y.; Bi, S.; Wang, M.; Yang, P.; Wu, D.; Wang, J.; Zhang, F. An Olefin-Linked Covalent Organic Framework as a Flexible Thin-Film Electrode for a High-Performance Micro-Super- capacitor. Angew. Chem. 2019, 131 (35), 12193−12197.

(58) Chen, X.; Zhang, H.; Ci, C.; Sun, W.; Wang, Y. Few-Layered Boronic Ester Based Covalent Organic Frameworks/Carbon Nano- tube Composites for High-Performance K-Organic Batteries. ACS Nano 2019, 13 (3), 3600−3607.

(59) Froemberg, D.; Barkai, E. A No-Go Theorem for Ergodicity and an Einstein Relation. Phys. Rev. E 2013, 88 (2), No. 024101.

(60) Telcs, A. Einstein Relation. Art Random Walks 2006, 1885, 83−93.