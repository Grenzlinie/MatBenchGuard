# Adsorption of histidine and histidine-containing peptides on Au(1 1 1):
A molecular dynamics study

Zhen Xu, Shi-Ling Yuan*, Hui Yan, Cheng-Bu Liu**

Key Laboratory of Colloid and Interface Chemistry, Shandong University, Jinan 250100, China

---

## ARTICLE INFO

**Article history:**
Received 4 December 2010
Received in revised form 10 January 2011
Accepted 21 February 2011
Available online 5 March 2011

**Keywords:**
Molecular dynamics
Adsorption
Au(1 1 1) surface
Histidine

## ABSTRACT

The adsorption behavior of histidine (His) and three His-derived peptides, glycyl-histidine (Gly-His), glycyl-histidine-glycine (Gly-His-Gly), and glycyl-glycyl-histidine (Gly-Gly-His) on the Au(1 1 1) surface has been studied using molecular dynamics simulations. All the four kinds of amino acids adsorbed from the liquid phase onto the Au(1 1 1) surface after a 3 ns MD run, as expected. Many statistical properties of His and His-derived peptides, like the interaction energy of adsorption, were analyzed after the systems reaching equilibrium. We have proven that His and His-derived peptides adsorbed on Au(1 1 1) via the imino nitrogen in the imidazole (IM) ring and the carboxylic acid group at the molecular level. Au(1 1 1) surface first adsorb the dipeptide Gly-His among the four amino acids and the sequence of residues in a peptide can significantly influence adsorption geometry of amino acids rather than the adsorption rate. Our work agrees well with available experimental data and shows a clear insight into the interaction between His-containing amino acids and Au(1 1 1) surface at a microscopic level, which is helpful to future rational design efforts of gold-binding polypeptides.

© 2011 Elsevier B.V. All rights reserved.

---

### 1. Introduction

Interfaces between metals and biologically active molecules are important topics in bio-catalysis, biocompatibility, biosensors, and also in several biological processes [1] such as hard-tissue growth [2], cell-surface adhesion [3] and inhibition of ice formation inside cells [4], to name a few. There are many such organic molecules and amino acids, of which oligomers (peptides) and polymers (proteins) represent an important class. These complex molecules, such as mono-peptides, can be deposited on well-characterized metal surfaces from the liquid phase [5–9], while some di- and tripeptides have been successfully evaporated under UHV conditions [10–12].

Because of the interaction between protein and metal surfaces is of considerable technological and fundamental interests, much effort has been derived into the development of protein adsorption experiments. A variety of experimental surface science techniques such as nuclear magnetic resonance (NMR), confocal laser scanning microscopy (CLSM), reflection–absorption infrared spectroscopy (RAIRS), photoelectron diffraction, XPS, and NEXAFS, have been used to study the adsorption of amino acids on gold or copper surfaces [13–24]. In theses experiments, gold is the least reactive of the noble metals [25], while copper is an interesting metal to compare with gold due to its higher reactivity [14,19,20].

Among so many possible applications of the adsorption of amino acids onto the metals, one example is the electrochemical detection of metal ions, demonstrated by Yang et al. [26]. They made a sensor with sub-ppt detection limits by attachment of the tripeptide Gly-Gly-His to a gold electrode. In this device, His is of prime importance as it forms a complex with the metal ion, which is of general biochemical interest and a biogenic amine involved in local immune responses, not only in proteins but also as a precursor of histamine. Because of the presence of the imidazole side chain, His and its peptides may also have important applications as corrosion inhibitors. Very recently, Feyer et al. [27] studied the adsorption of histidine (His) and three His-derived peptides on Au(1 1 1) by soft X-ray photoelectron spectroscopy (XPS) and near-edge X-ray absorption fine structure spectroscopy (NEXAFS) at the nitrogen and oxygen K edges, and they concluded that the His-derived peptides bond to the gold surface in a model similar to the single His molecule, via the imino N and carboxylate groups.

Despite the above mentioned excellent contributions from experiments, the underlying physicochemical principles the adsorption of His and His-derived peptides on Au(1 1 1) are still not fully understood. Several important questions can be still addressed, such as the priorities of the adsorption of His and His-derived peptides onto Au(1 1 1), the effect of the sequence of residues in His-derived tripeptide on the adsorption geometry, and so on.

---

\* Corresponding author. Tel.: +86 531 88365896; fax: +86 531 88564464.
\*\* Corresponding author. Tel.: +86 531 88361398; fax: +86 531 88564464.
E-mail addresses: shilingyuan@sdu.edu.cn (S.-L. Yuan), cbliu@sdu.edu.cn (C.-B. Liu).

0927-7757/$ – see front matter © 2011 Elsevier B.V. All rights reserved.
doi:10.1016/j.colsurfa.2011.02.046

![](./images/811677479667236865_1.jpg)

Fig. 1. Schematic structure of His and His-derived peptides.

Due to the substantial increase in computational power over the past few years, computational methods have proven to be valuable tools to provide deepened insight into the atomistic foundations of protein-surface interactions [28,29]. It can provide a detailed, atomistic level insight into the three-dimensional structure of the studied model system. These kinds of studies allow us to extract information about dynamic and structural properties at a microscopic level which is not easy to get from experiments. In these computational methods, due to computationally demanding, few quantum mechanics approach was used for even the single amino acids on surfaces in vacuum [30-33]. Another alternative approach is using all-atomic molecular dynamics (MD) simulation. Despite the MD simulations also have limitations those cannot be overcome with present technology, such as if the interactions with other molecules or atoms affect the charge distribution of a molecule being simulated, it cannot be captured in the simulations. It is still proven to be a valuable tool to study the adsorption of peptides or amino acids on gold surfaces [34-38], mainly due to the MD results' high degree of consistency with the experimental conclusion.

In our study, we have performed molecular dynamics (MD) studies on the adsorption of His and three His-derived peptides on the gold (1 1 1) surface, depending on the experimental phenomena [27]. In their experiment, they mainly reported a model for the adsorption of histidine and its peptides bonding to Au(1 1 1) via the imino nitrogen and the carboxylic acid group based on the N and O K-edge NEXAFS spectra. Histidine consists of three functional groups, amino, imidazole (IM), and carboxylic acid, and all they are potential binding sites to surfaces. In addition, we choose three kinds of its peptides, Gly-His, Gly-Gly-His and Gly-His-Gly (shown in Fig. 1) which may also play a significant role in molecular bonding with gold surface and be studied widely in experiments. In the simulation, we expected that the adsorption geometry of the four amino acids on Au(1 1 1) can be obtained from the molecular level, meanwhile, the priorities of the adsorption of His and His-derived peptides onto Au(1 1 1), which is not easily understand in experiments can be replied. Many statistical properties of the four amino acids adsorbed onto Au(1 1 1) surface were analyzed, such as the free energy of adsorption, the self-diffusion coefficients, atomic density profiles and length distribution the imino N of IM ring and the group COO. We found that His and His-derived peptides indeed adsorbed on Au(1 1 1) with the imino nitrogen and the carboxylic acid group. Au(1 1 1) surface adsorb the dipeptide Gly-His of first importance among the four amino acids and the sequence of residues in a peptide can significantly influence adsorption geometry of amino acids rather than the adsorption rate. Our results correlate with available experimental data and show a clear dependency of the interaction between the four kinds of amino acids and Au(1 1 1) surface.

![](./images/811677479667236865_2.jpg)

Fig. 2. Model of solution containing each of the four amino acids (b); the simulation model of the adsorption of His and His-derived peptides on Au(1 1 1) (a).

## 2. Simulation details

First, four solution models, each model containing one kind of the four amino acids and 2000 molecules, were built and shown in Fig. 2a. After energy minimization to remove potential overlaps between water and amino molecules, 1 ns simulations of the four solutions were performed in order to obtain the structural characteristics of histidine and three His-derived peptides. And then the four solutions were manually placed next to the Au(1 1 1) surface. So four solid-liquid systems (each system contains one kind of the four amino acids) were built in a rhombic simulation box, of which the dimensions was $x=57.6\mathring{A}$, $y=57.6\mathring{A}$, and $z=102.3\mathring{A}$, respectively. During the simulation, periodic boundary conditions were applied in all three dimensions. Two layers of gold atoms composed the gold (1 1 1) surface, consisting of 800 atoms totally. The z-dimension thickness of each solution containing one kind of the four amino acids was approximately $20\mathring{A}$. There is a vacuum layer of $80\mathring{A}$ high on the top of each solution to weaken the affect of gold surface in the upper periodic lattice. So four systems containing one kind of the four amino acid molecules, respectively, were prepared, and shown in Fig. 2b.

The MD simulation of different systems can be performed after charges and potentials are assigned to each atom. The simple point charge (SPC) model is adopted for the water molecule. The SPC model has been proven to be one of the most reasonable models for describing liquid phase water molecules in studying similar systems [39,40], even if it's limitation unable to overcome with

![](./images/811677479667236865_3.jpg)

Fig. 3. Snapshots of the configurations of the four systems at (a) t=0 ns and (b) t=3 ns.

![](./images/811677479667236865_4.jpg)

Fig. 4. The temperature (a) and energy (b) profiles of the simulated system of Gly-Gly-His.

present technology for explaining properties of the water adsorbed on interfaces. The long-range electrostatic interactions have been accounted for using the Ewald method. The total energy is written as a combination of valence terms including diagonal and off-diagonal cross-coupling terms and nonbond interaction terms, which include the Coulombic and Lennard-Jones functions for electrostatic and van der Waals interactions [41]

$$
E=E_{\text {bonds }}+E_{\text {angles }}+E_{\text {dihedrals }}+E_{\text {cross }}+E_{\text {VDW }}+E_{\text {elec }} \tag{1}
$$

where $E_{\text {VDW }}$ and $E_{\text {elec }}$ are given by Eq. (2):

$$
\begin{aligned}
E_{\text {non-bond }}= & E_{\text {VDW }}+E_{\text {elec }}=\sum \varepsilon_{i j}\left[2\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{9}-3\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{6}\right] \\
& +\sum \frac{q_{i} q_{j}}{r_{i j}} \tag{2}
\end{aligned}
$$

The parameters for each like-site interaction are given by the COMPASS force field [42,43]. All gold atoms were constrained during the simulation. The energies of the initial configurations are minimized with the Smart Minimizer method. After the minimization, all simulations are equilibrated at constant temperature and volume (NVT) for about 3 ns. Atomic coordinates were saved for every 20 ps. The analysis was performed by averaging over the final 1 ns of each trajectory.

**Table 1**
Self-diffusion coefficients of the His and His-derived peptides during the adsorption onto Au(111) as obtained from their MSDs (Dxy: in-xy-plane; Dz: along z).

| System       | $D_{z}$ (amino acid)$/10^{-6}\ \text{cm}^{2}\ \text{s}^{-1}$ | $D_{xy}$ (amino acid)$/10^{-6}\ \text{cm}^{2}\ \text{s}^{-1}$ |
|--------------|-------------------------------------------------------------|---------------------------------------------------------------|
| His          | 0.96                                                        | 0.27                                                          |
| Gly-His      | 3.24                                                        | 0.8                                                           |
| Gly-His-Gly  | 0.34                                                        | 0.09                                                          |
| Gly-Gly-His  | 0.36                                                        | 0.10                                                          |

### 3. Results and discussion

#### 3.1. Adsorption structure and equilibration

The macroscopic depositing behavior of the His and His-derived peptides on Au(111) surface is obtained by investigating the adsorption structure. The snapshots of the configurations of the four amino acids at the beginning of the initial dynamics run and at the end of equilibrium NVT run are shown in Fig. 3. From the figures, it is found that all the four kinds of amino acids were adsorbed onto the Au(111) surface after a long MD run, as expected. By monitoring the trajectories, the micelles are found to remain stable throughout the production run.

![](./images/811677479667236865_5.jpg)

Fig. 5. Total interaction energies ($E_{\text{amino/Au(111)}}$) by the contribution of van der Waals ($E_{\text{vdW}}$) and electrostatic ($E_{\text{elec}}$) potentials varied among the four kinds of amino acids.

![](./images/811677479667236865_6.jpg)

Fig. 6. Time evolution of mean square displacements of the four amino acids adsorbed onto Au(1 1 1) surface, the in-plane (i.e., in-xy-plane) (a) and the out-of-plane (i.e., along z) (b).

The equilibration of the four simulation systems are determined by monitoring the fluctuation of temperature and energy. As an example, the temperature and energy profiles of the system containing Gly-Gly-His from 2 to 3 ns (the last 1 ns) are shown in Fig. 4. It can be noted that the relative deviation of temperature and energy is less than 10% and 0.1%, respectively. This indicates that after the amino acids adsorption on Au(1 1 1) surface, all the four systems remain stable throughout the course of the production run. Next, further analysis will be done and the results are compared over all simulation systems.

### 3.2. Interaction energy

A crucial question in understanding the interaction of His and His-derived peptides with Au(1 1 1) surface is the interaction energy. The systems in equilibrium were chosen and energy-minimized to obtain the direct interaction energy between the four amino acids and the Au(1 1 1) surface. The interaction energy $E_{\text{amino/Au(1 1 1)}}$ is obtained from the following equation [44]:

$$
E_{\text{amino/Au(1 1 1)}} = \frac{E_{\text{total}} - (E_{\text{amino+water}} + E_{\text{Au(1 1 1)}})}{N_{\text{amino}}} \tag{3}
$$

![](./images/811677479667236865_7.jpg)

Fig. 7. Distribution of the length between the imino N of IM ring and group COO of His and His-derived peptides in aqueous solution (in dark line), and that during the adsorption of the four amino acids onto Au(1 1 1) surface (in red line). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

![](./images/811677479667236865_8.jpg)

Fig. 8. Number density profiles of water molecules (in dark), O atom of carboxylate (COO-) group (in red), imino N atom of IM ring (in blue), in the direction normal to the plane of Au(1 1 1) surface (i.e., along the z direction). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

where the $N_{amino}$ is the number of the amino molecules, $E_{amino/Au(111)}$ is the interaction energy between amino acids and the Au(1 1 1) surface, $E_{total}$ is the potential energy of the energy-minimized adsorption-system in equilibrium, $E_{amino+water}$ and $E_{Au(111)}$ are the potential energies of the amino acid solution and the pure Au(1 1 1) surface, respectively.

Interaction energies were calculated to indicate the capacity of His and His-derived peptides adsorption onto the Au(1 1 1) surface. It indicates that the system is relatively more stable with greater negative energy. Total interaction energies ($E_{amino/surface}$) contain contributions of van der Waals ($E_{vdW}$) and electrostatic potentials ($E_{electrostatic}$) which are shown separately in Fig. 5. It is noted that electrostatic interaction plays a decisive role in the adsorption of His and His-derived peptides on Au(1 1 1) surface, which varies consistent with the $E_{amino/Au(111)}$. In contrary, the van der Waals interaction energies between the four amino acids and Au(1 1 1) surface do not show significant differences. The adsorption of Gly-His on Au(1 1 1) surface is the most stable adsorption structure due to the most negative interfacial interaction energy among the four kinds of amino acids. Compared the adsorption energies between two kinds of tripeptides (Gly-Gly-His and Gly-His-Gly) on Au(1 1 1) surface, no apparent changes display. We can conclude that the sequence of residues in a peptide can hardly influence the adsorption of His-derived tripeptides on Au(1 1 1) surface.

### 3.3. Peptides dynamics

To obtain a more complete microscopic understanding of the properties of histidine (His) and three His-derived peptides adsorbed on Au(1 1 1), one should investigate the dynamics of the four amino acids as well as the water around them. In this section, we discuss the dynamical behavior of the four molecules and water molecules.

#### 3.3.1. Adsorption rate

The adsorption rate of the four amino acids can be studied by measuring their diffusion coefficients. This is done by directly measuring the mean square displacements (MSD) of the center of mass of the four amino acids from the MD trajectory. Fig. 6 shows MSD of His and His-containing peptides on Au(1 1 1) in a direction perpendicular to Au(1 1 1) surface plane from simulations, which are calculated from Eq. (4):

$$
\operatorname{MSD}(t)=\left\langle\frac{1}{N} \sum_{i=1}^{N}\left|r_{i}(t)-r_{i}(0)\right|^{2}\right\rangle \tag{4}
$$

where $N$ is the number of target molecules and $r_{i}(t)$ is the position of molecule $i$ at time $t$. The self-diffusion coefficient represents the mobility of the transference for different amino molecules in solution. Diffusion coefficients ($D$) can then be obtained from the slope of the mean square displacement versus time curve, using the well-known Einstein relation,

$$
D_{\alpha}=\frac{1}{6 N_{\alpha}} \lim _{t \rightarrow \infty} \frac{d}{d t} \sum_{i=1}^{N_{\alpha}}\left\langle\left[r_{i}(t)-r_{i}(0)\right]^{2}\right\rangle \tag{5}
$$

where $d$ is the dimensionality of the system, $r_{i}(t)$ and $r_{i}(0)$ are the center-of-mass coordinates of the $i$th amino acids at times $t$ and $t=0$, respectively.

To obtain an accurate understanding for the mobility of His and His-containing peptides during the adsorption on Au(1 1 1) surface, we have separately calculated the mean square displacements of the four amino acids in the plane of the interface (i.e., the $xy$ plane) and in the direction perpendicular to it (i.e., the $z$ direction). These are shown in Fig. 6. It is clear from the comparison between Fig. 6a and b that all the four amino acids are more mobile in the direction normal to the interfacial plane. However, they exhibit a more restricted motion in the plane of the Au(1 1 1) surface. Using appropriate Einstein relations (Eq. (5)), we have obtained the diffusion coefficients ($D_{xy}$ and $D_{z}$) of the four amino acids. The calculated values of $D_{xy}$ are much less than $D_{z}$ for all the four amino acids, clearly shown in Table 1. From the above analysis, we can conclude that His and His-containing peptides are all adsorbed onto the Au(1 1 1) surface and are then firmly fixed on the surface.

![](./images/811677479667236865_9.jpg)

Fig. 9. The final snapshot of adsorption structures of histidine molecules on Au(1 1 1). (a) The upper-left inset shows an enlarged scale and a clear comparison for Fig. 7a. (b)
The upper-right inset shows the area highlighted by the dark circled area on an enlarged scale.

Table 1 gives the corresponding self-diffusion coefficients from Eq. (5). The data, shown in Fig. 6 and Table 1, reveals that the mobility along the z direction of dipeptide Gly-His is generally the strongest among all the four molecules during the adsorption of His and His-containing peptides on Au(1 1 1). The calculated value of $D_{Gly-His}$ is $3.24×10^{-6}\, \text{cm}^2\text{s}^{-1}$, which is significantly greater than those of other three amino acids ($D_{His}=0.96×10^{-6}\, \text{cm}^2\text{s}^{-1}$, $D_{Gly-His-Gly}=0.34×10^{-6}\, \text{cm}^2\text{s}^{-1}$ and $D_{Gly-Gly-His}=0.36×10^{-6}\, \text{cm}^2\text{s}^{-1}$). It indicated that the adsorption rate of Gly-His on Au(1 1 1) surface is the fastest among the four amino acids. Furthermore, the value of $D_{Gly-His-Gly}$ is very close to $D_{Gly-Gly-His}$ shown in Table 1, indicating that the mobility of two tripeptides (Gly-His-Gly and Gly-Gly-His) along the z direction are nearly the same. On the basis of the above, the following conclusions can be obtained: The adsorption rate of histidine and three His-derived peptides onto the Au(1 1 1) surface follows the series: Gly-His > His > Gly-Gly-His = Gly-His-Gly. The sequence of residues in a peptide can hardly influence the adsorption rate His-containing peptides on Au(1 1 1).

From the above analysis of the interaction energy of adsorption and the adsorption rate of His and His-derived peptides on Au(1 1 1) surface, we can conclude that Au(1 1 1) surface adsorb easily the dipeptide Gly-His in the four amino acids, and for other His-derived tripeptides, the sequence of residues in a peptide cannot influence the selective adsorption of Au(1 1 1) surface. It agrees well with the conclusion of Feyer's group about the influence of sequence of residues in a peptide on the priority of amino acids adsorbed on Au(1 1 1) [27].

### 3.3.2. Conformational changes of amino acids
Previous experimental works [21,27] provided the information that the nature of the bonding of His to gold is via the imino nitrogen atom in the IM ring and the carboxylate (COO–) group. The distance between the two groups mentioned above is a key factor affecting the adsorption geometry of His and His-containing peptides on Au(1 1 1). In addition to examining the conformational changes of His and His-derived peptides during the adsorption on the Au(1 1 1) surface, it is highly interesting to explore the distance between the imino nitrogen atom in the IM ring and the carboxylate (COO–) group in solution, compared that of the four amino acids during the adsorption process onto the surface, as shown in Fig. 8.

From Fig. 7a, it is clear that there is nearly no change for the distance between the two groups of histidine during the adsorption on the Au(1 1 1) surface. The average length between the imino N and group COO of histidine in aqueous solutions is approximately $2.55\,\text{Å}$, nearly equal to that of histidine adsorbed on the Au(1 1 1) surface. We can conclude that very small structural changes happened during the adsorption of histidine onto Au(1 1 1). For the dipeptide Gly-His, the value of distance between the imino N and group COO is changed from $5.5\,\text{Å}$ (calculated in aqueous solutions) to the range of $4.75$–$5.5\,\text{Å}$ (calculated after the adsorption), as displayed in Fig. 7b. It is indicated that the length between the imino N and group COO of Gly-His has the trend becoming shorter during the adsorption. Furthermore, we can conclude that this length of His-derived dipeptide is more susceptible and easily shortens during deposited from aqueous solutions onto Au(1 1 1), compared to histidine.

As shown in Fig. 7c and d, this trend of the distance between the imino N and group COO becoming shorter during the adsorption is more obvious for His-derived tripeptides. The value of length respectively decreased approximately $1\,\text{Å}$ from $8.5\,\text{Å}$ to $7.5\,\text{Å}$ for Gly-His-Gly (as displayed in Fig. 7c), and decreased $0.75\,\text{Å}$ from $8.5\,\text{Å}$ to $7.75\,\text{Å}$ for Gly-Gly-His (as displayed in Fig. 7d). Considering this trend displayed in Fig. 8, we find that significant effect on the length of distance between the imino N and group COO of His and His-derived peptides may show more obviously as adding residues in the amino acid during the adsorption on Au(1 1 1).

### 3.3.3. The adsorption geometry
To further investigate the adsorption geometry of His and His-containing peptides, we provide the number density profiles of the imino N in the IM ring, the O atoms in carboxylate group and water molecules as a function of the distance along the z direction. Fig. 8 shows the number density profiles obtained from the four systems. The water density profiles near the Au(1 1 1) surfaces are remarkably similar in all four systems. For each system, there are two peaks of the water density profile appearing in the vicinity of the Au(1 1 1) surface similarly, and the first peak next to the surface is higher and narrower compared to the subsequent one. It indicated that the water density profiles display oscillations during the process of adsorption of amino acids onto the Au(1 1 1) surface, and eventually induce two layers of water are structured by interaction with the surface. For histidine and three His-derived peptides, the peaks of the imino N in the IM ring and the O atoms in carboxylate group

appear near the Au(1 1 1) surface, and located at a same z value compared to the first peak of water density profile. It indicated that the imino N in the IM ring and the carboxylate group of the four amino acids penetrate into the first layer of aqueous solution after the adsorption on the Au(1 1 1) surface.

In order to clearly display the adsorption geometry of the four amino acids on Au(1 1 1) surface, we take the snapshot of the final configuration of His adsorbed on Au(1 1 1) as an example, shown in Fig. 9. From Fig. 9a, we can clearly find that density profile peaks of the imino N in the IM ring, the O atoms in carboxylate group located at the $z \approx 3\mathring{A}$ position, where is the same to the first layer peak of aqueous solution. The upper-right inset of Fig. 9 shows the area highlighted by the dark circled area on an enlarged scale, where is commonly found in the final configuration. Fig. 9b clearly shows that the His molecule was adsorbed on Au(1 1 1) via the imino N of the IM ring and two O atoms of carboxylate group, and the distance between the three atoms and Au(1 1 1) surface is approximately $3\mathring{A}$. Around the three atoms, lots of water molecules formed a layer parallel to the gold surface. The final adsorption geometry of the histidine obtained from our simulations is observed in excellent agreement with the model for the adsorption of histidine adsorbed on Au(1 1 1) based on the experiments of Feyer et al. [27]. The phenomenon that His and His-derived peptides adsorb on Au(1 1 1) via the imino nitrogen and the carboxylic acid group has been strongly proven at a microscopic level.

## 4. Conclusions

In this paper, we investigated the adsorption mechanism of His and His-derived peptides onto the gold (1 1 1) surface by means of molecular dynamics simulations. The final adsorption geometry of the His and His-derived peptides obtained from our simulations is observed in excellent agreement with the model for that based on the experiments of Feyer et al. [27]. It has been strongly proven that His and His-derived peptides adsorbed on Au(1 1 1) via the imino nitrogen and the carboxylic acid group from the molecular level. The system containing Gly-His has the most negative adsorption energy among the four systems. The adsorption rate of the four amino acids onto the Au(1 1 1) surface follows the series: Gly-His > His > Gly-Gly-His ≈ Gly-His-Gly. Simulation results reveal that Au(1 1 1) surface adsorb the dipeptide Gly-His in the first place among the four amino acids, and for His-derived tripeptides, the sequence of residues in a peptide cannot influence the selective adsorption of Au(1 1 1) surface. The simulated data support a previous experimental suggestion that it is impossible to clearly distinguish among the four kinds of amino acids.

From the analysis of density profiles and distance distribution between imino N of IM ring and carboxyl group of the four amino acids, we found that the sequence of residues in a peptide can significantly influence the adsorption geometry. They reasonably correlate with the previous experimental findings in related systems [27]. Simulations of individual amino acids provided are a crucial first step in describing the interactions of more complex biomolecular systems with inorganic surfaces. An important next step is the investigation of potential cooperative effects between amino acids [45,46] and of whole peptides and proteins. However, this basic level study reveals an important insight into future rational design of gold-binding polypeptides.

## Acknowledgments

This work was supported by the National Science Foundation of China (Nos. 20873074 and 21043008). The author thanks for the study visit to Germany supported by the DAAD.

## References

[1] J.J. Gray, The interaction of proteins with solid surfaces, Curr. Opin. Struct. Biol. 14 (2004) 110–115.

[2] L. Addadi, S. Weiner, Control and design principles in biomineralization, Angew. Chem. Int. Ed. Engl. 31 (1992) 153–169.

[3] D.J. Iuliano, S.S. Saavedera, G.A. Truskey, Effect of the conformation and orientation of adsorbed fibronectin on endothelial cell spreading and the strength of adhesion, J. Biomed. Mater. Res. 27 (1993) 1103–1113.

[4] Y. Yeh, R.E. Feeney, Antifreeze proteins: structures and mechanisms of function, Chem. Rev. 96 (1996) 601–618.

[5] T. Baas, L. Gamble, K.D. Hauch, D.G. Castner, T. Sasaki, Characterization of a cysteine-containing peptide tether immobilized onto a gold surface, Langmuir 18 (2002) 4898–4902.

[6] E. Chow, E.L.S. Wong, T. Böcking, Q.T. Nguyen, D.B. Hibbert, J.J. Gooding, Analytical performance and characterization of MPA-Gly-Gly-His modified sensors, Sensor Actuat. B 111 (2005) 540–547.

[7] Y. Cho, A. Ivanisevic, TAT peptide immobilization on gold surfaces: a comparison study with a thiolated peptide and alkylthiols using AFM, XPS, and FT-IRRAS, J. Phys. Chem. B 109 (2005) 6225–6232.

[8] S. Monti, V. Carravetta, C. Battocchio, G. Iucci, G. Polzonetti, Peptide/TiO₂ surface interaction: a theoretical and experimental study on the structure of adsorbed ALA-GLU and ALA-LYS, Langmuir 24 (2008) 3205–3214.

[9] G. Polzonetti, C. Battocchio, M. Dettin, R. Gambaretto, C. Di Bello, V. Carravetta, S. Monti, G. Iucci, Self-assembling peptides: a combined XPS and NEXAFS investigation on the structure of two dipeptides Ala-Glu, Ala-Lys, Mater. Sci. Eng. C 28 (2008) 309–315.

[10] S.M. Barlow, S. Haq, R. Raval, Bonding, organization, and dynamical growth behavior of tripeptides on a defined metal surface: tri-l-alanine and tri-l-leucine on Cu(1 1 0), Langmuir 17 (2001) 3292–3300.

[11] A. Vallée, V. Humblot, C. Méthivier, C.M. Pradier, Adsorption of a tripeptide, GSH, on Au(1 1 1) under UHV conditions; PM-RAIRS and low T-XPS characterisation, Surf. Sci. 602 (2008) 2256–2263.

[12] A. Vallée, V. Humblot, C. Méthivier, C.M. Pradier, Adsorption of di- and tripeptides on Au(1 1 0) under ultrahigh vacuum conditions. 1. Polarization modulation reflection-absorption infrared spectroscopy and X-ray photoelectron spectroscopy characterization, J. Phys. Chem. C 113 (2009) 9336–9344.

[13] G. Xue, J. Dong, Y. Sun, Complex-induced activating effect on surface species: reactions of imidazole on zero oxidation state metal surfaces, Langmuir 10 (1994) 1477.

[14] B. Liedberg, C. Carlsson, I. Lundström, An infrared reflection-absorption study of amino acids adsorbed on metal surfaces: -histidine and -phenylalanine on gold and copper, J. Colloid Interface Sci. 120 (1987) 64–75.

[15] J. Hasselström, O. Karis, M. Weinelt, N. Wassdahl, A. Nilsson, M. Nyberg, L.G.M. Pettersson, M.G. Samant, Stöhr, The adsorption structure of glycine adsorbed on Cu(1 1 0); comparison with formate and acetate/Cu(1 1 0), J. Surf. Sci. 407 (1998) 221–236.

[16] M. Nyberg, J. Hasselström, O. Karis, N. Wassdahl, M. Weinelt, A. Nilsson, L.G.M. Pettersson, The electronic structure and surface chemistry of glycine adsorbed on Cu(1 1 0), J. Chem. Phys. 112 (2000) 5420–5428.

[17] G. Dodero, L. De Michieli, O. Cavalleri, R. Rolandi, L. Oliveri, A. Daccà, R. Parodi, High resolution X-ray photoelectron spectroscopy of l-cysteine self-assembled films, Colloids Surf. A 175 (2000) 121.

[18] S.M. Barlow, R. Raval, Supramolecular assembly of strongly chemisorbed size-and shape-defined chiral clusters: S- and R-alanine on Cu(1 1 0), Surf. Sci. Rep. 50 (2003) 201–341.

[19] M.E. Marti, Ch. Methivier, P. Dubot, C.M. Pradier, Adsorption of (S)-histidine on Cu(1 1 0) and oxygen-covered Cu(1 10), a combined Fourier transform reflection adsorption infrared spectroscopy and force field calculation study, J. Phys. Chem. B 107 (2003) 10785–10792.

[20] M.E. Marti, A. Quash, Ch. Methivier, P. Dubot, C.M. Pradier, Interaction of s-histidine, an amino acid, with copper and gold surfaces, a comparison based on rairs analysis, Colloids Surf. A 249 (2004) 85–89.

[21] Y. Zubavichus, M. Zharnikov, Y. Yang, O. Fuchs, C. Heske, E. Umbach, G. Tzvetkov, F.P. Netzer, M. Grunze, Surface chemistry of ultrathin films of histidine on gold as probed by high-resolution synchrotron photoemission, J. Phys. Chem. B 109 (2005) 884–891.

[22] J.J. L.B. Jones, F. Thibault-Starzyyk, E.A. Seddon, R. Raval, S.J. Jenkins, G. Held, The local adsorption geometry and electronic structure of alanine on Cu{1 1 0}, Surf. Sci. 600 (2006) 1924–1935.

[23] F. Iori, S. Corni, R. Di Felice, Unraveling the interaction between histidine side chain and the Au(1 1 1) surface: a DFT study, J. Phys. Chem. C 112 (2008) 13540–13545.

[24] V. Feyer, O. Plekan, T. Skála, V. Cháb, V. Matoín, K.C. Prince, The electronic structure and adsorption geometry of L-histidine on Cu(1 1 0), J. Phys. Chem. B 112 (2008) 13655–13660.

[25] B. Hammer, J.K. Nørskov, Why gold is the noblest of all the metals, Nature 376 (1995) 238–240.

[26] W. Yang, D. Jaramillo, J.J. Gooding, D.B. Hibbert, R. Zhang, G.D. Willett, K.J. Fisher, Sub-ppt detection limits for copper ions with Gly-Gly-His modified electrodes, Chem. Commun. 19 (2001) 1982–1983.

[27] V. Feyer, O. Plekan, N. Tsud, V. Cháb, V. Matoín, K.C. Prince, Adsorption of histidine and histidine-containing peptides on Au(1 1 1), Langmuir 26 (2010) 8606.

[28] J.H. Harding, D.M. Duffy, M.L. Sushko, P.M. Rodger, D. Quigley, J.A. Elliott, Com- putational techniques at the organic–inorganic interface in biomineralization, Chem. Rev. 108 (2008) 4823–4854.

[29] M. Hoefling, F. Iori, S. Corni, K.E. Gottschalk, Interaction of amino acids with the Au(1 1 1) surface: adsorption free energies from molecular dynamics simula- tions, Langmuir 26 (2010) 8347–8351.

[30] L.M. Ghiringhelli, L. Delle Site, Phenylalanine near inorganic surfaces: con- formational statistics vs. specific chemistry, J. Am. Chem. Soc. 130 (2008) 2634–2638.

[31] G.Y. Hong, H. Heinz, R.R. Naik, B.L. Farmer, R. Pachter, Toward understanding amino acid adsorption at metallic interfaces: a density functional theory study, Appl. Mater. Interfaces 1 (2009) 388–392.

[32] A. Rimola, M. Corno, C.M. Zicovich-Wilson, P. Ugliengo, Ab initio modeling of protein/biomaterial interactions: glycine adsorption at hydroxyapatite sur- faces, J. Am. Chem. Soc. 130 (2008) 16181–16183.

[33] A. Rimola, M. Corno, C.M. Zicovich-Wilson, P. Ugliengo, Ab initio modeling of protein/biomaterial interactions: competitive adsorption between glycine and water onto hydroxyapatite surfaces, Phys. Chem. Chem. Phys. 11 (2009) 11662–111662.

[34] R. Braun, M. Sarikaya, K. Schulten, Genetically engineered gold-binding polypeptides: structure prediction and molecular dynamics, J. Biomater. Sci. 13 (2002) 747–756.

[35] L.M. Ghiringhelli, B. Hess, N.F.A. van der Vegt, L. Delle Site, Competing adsorp- tion between hydrated peptides and water onto metal surfaces: from electronic to conformational properties, J. Am. Chem. Soc. 130 (2008) 13460–13464.

[36] H. Heinz, B.L. Farmer, R.B. Pandey, J.M. Slocik, S.S. Patnaik, R. Pachter, R.R. Naik, Nature of molecular interactions of peptides with gold, palladium, and Pd–Au bimetal surfaces in aqueous solution, J. Am. Chem. Soc. 131 (2009) 9704–9714.

[37] P. Schravendijk, L.M. Ghiringhelli, L. Delle Site, N.F.A. van der Vegt, Interaction of hydrated amino acids with metal surfaces: a multiscale modeling description, J. Phys. Chem. C 111 (2007) 2631–2642.

[38] A.V. Verde, J.M. Acres, J.K. Maranas, Investigating the specificity of peptide adsorption on gold using molecular dynamics simulations, Biomacromolecules 10 (2009) 2118–2128.

[39] A.K. Shaytan, V.A. Ivanov, K.V. Shaitan, A.R. Khokhlov, Free energy profiles of amino acid side chain analogs near water–vapor interface obtained via MD simulations, J. Comput. Chem. 31 (2010) 204–216.

[40] C.Y. Wu, M.J. Chen, C.Q. Guo, Peptide–TiO₂ interaction in aqueous solution: conformational dynamics of RGD using different water models, J. Phys. Chem. B 114 (2010) 4692–4701.

[41] J.Y. Pang, G.Y. Xu, S.L. Yuan, Y.B. Tan, A dispersing carbon nanotubes in aque- ous solutions by a silicon surfactant: experimental and molecular dynamics simulation study, Colloids Surf. 350 (2006) 101–108.

[42] H. Sun, P. Ren, J.R.A. libai, J.G. simmons, The compass force field: parameter- ization and validation for phosphazenes, Comput. Theor. Polym. Sci. 8 (1998) 229.

[43] H. Sun, COMPASS: an ab initio force-field optimized for condensed-phase appli- cations overview with details on alkane and benzene compounds, J. Phys. Chem. B 102 (1998) 7338–7364.

[44] K.D. Danov, S.D. Kralchevska, P.A. Kralchevsky, K.P. Ananthapadmanabhan, A. Lips, A mixed solutions of anionic and zwitterionic surfactant (Betaine): surface-tension isotherms, adsorption, and relaxation kinetics, Langmuir 20 (2004) 5445–5453.

[45] B.R. Peelle, E.M. Krauland, K.D. Wittrup, A.M. Belcher, Design criteria for engineering inorganic material-specific peptides, Langmuir 21 (2005) 6929–6933.

[46] A. Serr, D. Horinek, R.R.J. Netz, Polypeptide friction and adhesion on hydropho- bic and hydrophilic surfaces: a molecular dynamics case study, J. Am. Chem. Soc. 130 (2008) 12408–12413.