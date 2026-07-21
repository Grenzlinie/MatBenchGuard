![](./images/813009902459944961_1.jpg)

Subscriber access provided by Kaohsiung Medical University

# Functional Nanostructured Materials (including low-D carbon)

## Generating Sub-nanometer Pores in Single-layer MoS2 by Heavy Ion Bombardment for Gas Separation: A theoretical Perspective

Kedi Yin, Shengxi Huang, Xiaofei Chen, Xinwei Wang, Jing Kong, Yan Chen, and Jianming Xue

ACS Appl. Mater. Interfaces, **Just Accepted Manuscript** • DOI: 10.1021/acsami.8b10569 • Publication Date (Web): 31 Jul 2018

Downloaded from http://pubs.acs.org on August 2, 2018

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/813009902459944961_2.jpg)

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Generating Sub-nanometer Pores in Single-layer MoS₂ by Heavy Ion Bombardment for Gas Separation: A theoretical Perspective

Kedi Yin¹,², Shengxi Huang³,⁴, Xiaofei Chen¹, Xinwei Wang⁵, Jing Kong³*, Yan Chen²*, Jianming Xue¹*

¹ State Key Laboratory of Nuclear Physics and Technology, School of Physics, CAPT, HEDPS, and IFSA Collaborative Innovation Center of MoE, Peking University, Beijing 100871, China

² Guangzhou Key Laboratory for Surface Chemistry of Energy Materials, New Energy Research Institute, School of Environment and Energy, South China University of Technology, Guangzhou, Guangdong, 510006, China

³ Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA

⁴ Department of Electrical Engineering, The Pennsylvania State University, University Park PA 16802, USA

⁵ School of Advanced Materials, Shenzhen Graduate School, Peking University, Shenzhen 518055, China

*Corresponding author's email: jingkong@mit.edu, escheny@scut.edu.cn, jmxue@pku.edu.cn

**Keywords.** Single-layer MoS₂, molecular dynamic, density function theory, ion beam bombardment, nanopore, gas separation

## ABSTRACT

Single-layer molybdenum disulfide (MoS₂) filter with nanometer size pores has attracted

great attention recently due to its promising performance for membrane separation.
Generating nanopores in $MoS_2$ controllably, however, is still a challenging task, which greatly limits the real application of $MoS_2$ filters. In this work, the pore forming process in single-layer $MoS_2$ by heavy ion bombardment was investigated in detail using molecular dynamics simulations. We found that pores with sub-nanometer size (0.6 nm to 1.2 nm) can be created in the $MoS_2$ sheet by single ion bombardment, with a probability as high as 0.8 pores per incident ion. The size and shape of the nanopore can be tuned controllably by adjusting bombardment parameters. Furthermore, the performance of the $MoS_2$ filter with these sub-nanometer size pores for gas separation of $He$, $Ne$, $H_2$, $Ar$ and $Kr$ was evaluated by density functional theory based first-principles calculations. The $MoS_2$ filter was found to show much higher selectivity for separating $H_2$/He and He/Ne than which have been reported for graphene and other membranes. Such high selectivity was attributed to the interaction between gases and the charged edge of pores in $MoS_2$. Our results suggest the potential application of ion beam technology in single-layer $MoS_2$ for membrane separation.

### 1. Introduction
Due to its potentially low cost, environmental friendly, and high efficiency features, two-dimensional (2D) materials with nanopores have attracted great attention in membrane separation technology, $^{1-2}$ such as gas separation, $^{2-5}$ water desalination $^{6-8}$ and DNA sequencing. $^{9-11}$ Up to now, graphene is the most widely studied 2D material for these applications. $^{5,7,12-16}$ In addition to graphene, single-layer $MoS_2$ with nanosize pores recently has also become a promising candidate. $^{8,10,17}$ For instance, Heiranian *et al.* predicted a nanopore in single-layer $MoS_2$ to have good performance for water desalination with water flux that is orders of magnitude greater than that of other known nanoporous membranes. $^{8}$ By introducing mechanical strain, Li *et al.* observed the "open" and "closed" states of the $MoS_2$ filter for water desalination in their simulations, pointing

possible application as tunable nano-devices.¹⁷ Farimani *et al.* reported that a single-layer
MoS₂ showed much higher signal-to-noise ratio for DNA sequencing than graphene and
boron nitride.¹⁰ These superb performance of MoS₂ filter was attributed to the craftable
pore architecture (pore size and pore edge atoms) of MoS₂. Furthermore, in contrast to
the charge neutral edge of pores in graphene,¹⁴ the edge of nanopores in MoS₂ filter are
intrinsically charged, which can also potentially play an essential role in achieving high
efficiency.¹⁷

Generating pores with nanometer size in a controllable manner is essential for
achieving membrane separation devices with high efficiency¹⁻², ¹⁸⁻¹⁹ Many approaches
have been applied to "drill pores" in graphene,²⁰⁻²² e.g., electron beam sculpting,²⁰
self-organized growth in high temperature solvents, e.g. in zinc chloride,²¹ and
ultraviolet-induced oxidative etching.²² The large scale application of these approaches,
however, are limited by their low efficiency, high cost, and the difficulty to control below
1 nm.²⁰ In contrast to these methods, it is still a challenging task to form nanopores
controllably in single-layer MoS₂, which strongly limit its real application in membrane
separation techniques.

Utilizing irradiation effects of energetic heavy ions in materials, ion beam
technology has been successfully applied to engineer the structure and other properties of
nanomaterials.²³⁻²⁸ Our previous molecular simulation works showed that, by controlling
the bombardment parameters (energies, species, incident angles, *etc.*), nanopores with
expected size, shape and quality could be created in graphene.²⁷, ²⁹⁻³⁰ Such prediction was
confirmed experimentally by Vazquez *et al.*³⁰ Furthermore, ion bombardment can also
introduce reactive defects into the graphene lattice, which can be subsequently enlarged
into permeable pores by oxidative etching.³¹ All these successful applications
demonstrate ion beam bombardment to be a highly effective and economical way to
fabricate nanopore in graphene, and can be potentially applied to other two-dimensional
materials. Although some previous works have studied the radiation effect of heavy ions

in single-layer $MoS_2,^{32-36}$ the creation of nanopore in single-layer $MoS_2$ by ion irradiation has not been systematically explored yet.

In this work, we employed molecular dynamic (MD) simulations to investigate the formation of nanopore in single-layer $MoS_2$ by ion bombardment. MD simulation has been widely used in describing the interaction between heavy ions with two-dimensional materials. $^{23-26,37-38}$ Our group previously used MD simulations to investigate the doping and defect generating process of energetic ions in graphene. $^{25-26}$ The defect production probability predicted by MD simulation was then found to agree well with experimental values. $^{26}$ In this report, we found that pores with sub-nanometer size (0.6 nm to 1.2 nm) in $MoS_2$ sheet can be created by single ion bombardment. The probability to produce sub-nanometer pores in single-layer $MoS_2$ can be as high as 0.8 by selecting appropriate ion parameters. The pore shape and pore size can be tuned controllably by adjusting the ion mass, energy and incident angle. To demonstrate the application of the $MoS_2$ filter with sub-nanometer size pores created by heavy ion bombardment, we further used density functional theory (DFT) based first-principles calculations to evaluate its performance for gas separation. The transportation of $He, Ne, H_2, Ar$ and $Kr$ through sub-nanometer pore introduced by ion bombardment was studied in details. We found the nanopores in single-layer $MoS_2$ showed very high selectivity and permeability for separating $H_2/He$ and $He/Ne$, much higher than that have been reported for graphene and other membranes. Such high selectivity was attributed to the charge of the pore in $MoS_2$. Our results pointed out the potential application of ion beam technology in $MoS_2$ and other two-dimensional materials for membrane separation applications.

## 2. Theoretical Calculations

### 2.1 MD Simulation

Molecular dynamics simulations were performed on the large-scale/molecular massively parallel simulator (LAMMPS). $^{39}$ The Stillinger-Weber potential recently

developed by Jiang's group was used to describe the interatomic interactions within single-layer $MoS_2$ for stable molecular dynamics simulations. $^{40-41}$ To model the energetic collisions between incident ions with single-layer $MoS_2$, Ziegler-Biersack-Littmark (ZBL) $^{42-43}$ universal repulsive potential which can accurately describe the interaction at short interatomic separations $(<1Å)$ was used. Except for the noble incident ions, the Au-S interatomic interactions were also calculated with only the ZBL potential, which is based on the fact that the binding energy of Au-S are very weak compared with that of Mo-Mo, S-Mo and S-S.

Ion irradiations were conducted on a free-standing $MoS_2$ sheet consisting of 576 Mo atoms and 1152 S atoms, with a lateral size of $65 ×75Å^2$. Periodic boundary conditions (PBCs) were used during the dynamical simulations. He, Ne, Ar, Kr, Xe and Au ions were chosen to simulate the ion impacts. The incident ion was initially placed at $20Å$ above the single-layer $MoS_2$, and the direction is perpendicular to the $MoS_2$ sheet. Ion energies were in the range of 50 eV to 1000 keV. For Au ions, the incident angle was taken from $0°$ (normal direction with respect to the surface) to $60°$ . For each incident ion with a specific energy, 100 independent simulations were carried out, and the impact points were randomly distributed in a $10×10$ $Å^2$ square area located in the sample center so as to simulate as much impact points as possible. During the irradiation process, the NVE ensemble was employed and a time step of 0.1fs was used to guarantee energy conservation. After the collision, the system was maintained at 300 K for 50 ps with the Nose'-Hoover algorithm.

### 2.2 DFT Simulation
The first principle calculations were carried out based on the spin-polarized DFT $^{44}$ as implemented in the Vienna ab initio simulation package (VASP). $^{45-46}$ The electron-ion interaction is described by the projector augmented wave (PAW) $^{47-48}$ pseudopotentials. The exchange and correlation potentials are described by the generalized gradient

approximation (GGA)⁴⁹ functional of Perdew-Burke-Ernzerhof (PBE)⁴⁹. In order to account for the influence of the van der Waals (vdW)⁵⁰ interaction, the optPBE method was used as in our previous works.⁵¹⁻⁵² All calculations were performed with a supercell of single-layer MoS₂ containing 108 atoms. Periodic boundary condition was applied and a vacuum layer of 15 Å was added to avoid the interlayer interactions. The total energy was converged to better than 10 meV for a plane wave cutoff of 500 eV and 5× 5 ×1 Monkhorst-Pack⁵³ k-point sampling for the Brillouin zone. For geometry relaxation, we used the method of conjugate gradient energy minimization, and the convergence criterion for energy was 10⁻⁵ eV between two consecutive steps. The maximal force exerted on each atom was less than 0.02 eV/Å upon ionic relaxation.

In order to explore the performance of this sub-nanometer pore in gas separation, the climbing image nudged elastic band (CI-NEB) method⁵⁴ was performed to estimate the diffusion barrier for gases transporting through the pore. Hereby, the starting and the end position of the molecular diffusion pathway are placed above and below the central pore while a linear interpolation between those points was used as an initial guess of the diffusion path. Ab-initio molecular dynamics (ab-init MD) simulation was also carried out to check the thermal stability of the nanoporous MoS₂. The configuration from static calculation was used as the initial state, and a canonical NVT ensemble was simulated using the algorithm of Nose. The system was allowed to relax for 15 picoseconds in total with a time step of 3 femtoseconds.

### 3. Results and Discussion

When energetic ions bombard a single-layer MoS₂, as illustrated in Figure 1a, Mo or S atoms can obtain enough energy to escape from the single-layer MoS₂, resulting in different defect structures in MoS₂. In our simulations, six types of ions (He, Ne, Ar, Kr, Xe and Au ions) with energies ranging from 50 eV to 1000 keV were used as incident ions. The incident direction was set to be perpendicular to the MoS₂ plane. We found that,

for all these conditions, a vacancy complex containing a Mo vacancy and nearby three disulfur pairs vacancies (Vₘₒₛ₆) can be formed after the ion bombardment (Figure 1a). This Vₘₒₛ₆ defect cluster is treated as a nanopore with an effective diameter of 0.6 nm, which can potentially be used in membrane separation application. As for S vacancy, Mo vacancy and some other complex point defects, even if they are produced, they would not affect the separation application of the pore due to their small effective diameters. The formation process of Vₘₒₛ₆ defect cluster can be described as follow: first, the S atoms in the upper sub-layer which directly interact with incident ion will be sputtered away in the opposite direction of the incident ion; the knock-on Mo atom will then become the new energetic ion to hit the S atoms in the lower sub-layer downward,which finally lead to the formation of Vₘₒₛ₆ defect cluster.

![](./images/813009902459944961_3.jpg)

Figure 1. (a) Schematic presentation of the simulation setup, the perfect single-layer MoS₂ and the single-layer MoS₂ with a Vₘₒₛ₆ nanopore (defect cluster) created by ion

bombardment. (b) The probability for the production of nanopore ($\text{V}_{\text{MoS}_6}$). (c) The average number of sputtered atoms in single-layer $\text{MoS}_2$ under ion bombardment as a function of ion energy for the six types of ions revealed by MD simulations.

The dependence of pore formation process as a function of the kinetic energy of ions was investigated in detail. The nanopore production probability shows a volcano shape dependence on the kinetic energy of incident ions (**Figure 1b**). For a given ion, as the kinetic energy increases from 50 eV to 1000 keV, the possibility to create a nanopore first increases with ion kinetic energy and then decreases. The reason for such volcano shape dependence is that the formation of nanopore is mainly derived from atomic sputtering. As shown in **Figure 1c**, the number of sputtered atoms caused by energetic ion bombardment shows a very similar dependence on the kinetic energy of incident ions, indicating atomic sputtering to be the main cause of nanopore formation. It's worth noting that, besides being sputtered away from the $\text{MoS}_2$ surface, some target atoms may leave their original position but still be attached to the $\text{MoS}_2$ plane which can also contribute to the formation of nanopores. We didn't count this part into the average number of sputtered atoms. For the energy regime studied in this work, the number of sputtered atoms is mainly dominated by the energy transferred between the incident ion and the atom$^{32}$, which is positively correlated to the collision cross section. The initial increase of nanopore production probability with ion energy is because low energy ion simply cannot displace target atoms. While, the decrease of nanopore production probability originates from a drop in the cross section at high ion energies.$^{55-58}$ The ion kinetic energy which shows the maximum probability to form a $\text{V}_{\text{MoS}_6}$ pore is in the range of hundreds to thousands of electron volts for all the six types of incident ions.

The ion mass also has a significant impact on the nanopore forming process (**Figure 1b**). At a given ion energy, a heavier ion shows a greater probability to create $\text{V}_{\text{MoS}_6}$ pores in single-layer $\text{MoS}_2$. Consistent with the high pore production probability, single-layer $\text{MoS}_2$ bombarded by heavier ions shows a larger number of sputtered atoms (**Figure 1c**).

and our results in **Figure 1c** for He, Ne, Ar, Kr and Xe are consistent with early theoretical studies of single-layer $MoS_2$ subjected to ion irradiation. $^{32}$ Furthermore, as shown **Figure 1b**, the probability shows a more pronounced dependence on the kinetic energy for heavier ions. This is similar to the dependence of nuclear stopping power $(S_n)$, defined as the energy transferred to the target atoms per unit distance, on the mass of incident ion. However, the definition of nuclear stopping power is based on averaging over many collisions, which is not be useful for a two-dimensional material. $^{27}$ The $S_n$ values of the six types of ions with different energies in bulk $MoS_2$ calculated by the Stopping and Range of Ions in Matter (SRIM) $^{59}$ software are shown in **Figure S1**. The mass and energy dependence tendency shown in **Figure 1b** is also widely observed in other applications of ion beam when sputtering is involved. $^{24,27,29}$ It is worth noting that, besides $V_{MoS6}$, other defect types can also be formed in the ion bombardment, as shown in **Figure S2**. The dependence of the formation probabilities for some different defects ($V_S$, $V_{S2}$, $V_{Mo}$, $V_{MoS3}$, $V_{MoS5}$, $V_{MoS6}$ and pores larger than $V_{MoS6}$) on the kinetic energy for Au ion irradiation are shown in **Figure S3**.

Besides the mass and the kinetic energy, the incident angle of heavy ion can also strongly impact the interaction of energetic ions and 2D material. For instance, it has been reported that an increased incident angle can cause more severe damage in graphene. $^{27,60}$ Therefore, it could be expected that more atoms can be removed and a larger pore could be produced when larger incident angles were used. To study the impact of the incident angle, 500 eV Au ions were chosen as the injection ions in the following simulation due to its high possibility to create nanopore (**Figure 1b and 1c**). We keep the simulation size in the oblique incidence, and the incident angle ($\theta$) was taken from $0^\circ$ to $60^\circ$ . **Figure 2a** shows pores with various nanostructures formed by ion bombardment at different incident angles. In contrast to the above-mentioned $V_{MoS6}$ nanopore which shows regular round shape, nanopores formed by ions with large incident angles usually have complex structures featuring very rough edges. As the incident angle increases, the generated

nanopores become less circular and increasingly elliptical. Because we're considering the random impact points, the effective diameter, which is defined as an imaginary cylinder coaxial with the thread has equal space widths, was used to characterize these pores. Characterization of pore geometry by the effective diameter is shown in Supporting Information S-4. The effective diameters of the nanopores are ranging from 0.6 nm to 1.2 nm as the incident angle increasing from $0^\circ$ to $60^\circ$ (Figure 2b). This phenomenon is due to the impact of incident angle on the energy transfer process between the incident ions and the target atoms. When the incident angle increases, more energy will be deposited into the $\mathrm{MoS_2}$ sheet because of the longer interaction path between the incident ion and the $\mathrm{MoS_2}$ layer, which will lead to more severe damage, and eventually bigger nanopores in single-layer $\mathrm{MoS_2}$.

![](./images/813009902459944961_4.jpg)

Figure 2. The influence of ion incident angle on the pore forming process. (a) Final atomic configurations resulted from the incidence of 500 eV Au atom with different

incident angles. (b) The average number of removed atoms and the effective diameter of pores created by 500 eV Au bombardment with different incident angles. (c) The probability to form pores as a function of incident angle for 500 eV Au ion bombardment.

We also counted the pore production probability as a function of ion incident angle, as shown in **Figure 2c**. With the increase of incident angle, the probability to form nanopores keeps increasing except for a little drop around $30^\circ$ . This drop is because the minimum energy for atoms to escape also depends on the escape angle. For example, if there is another atom in the way of the sputtered atom, excess energy is needed to overcome this new barrier, resulting in the dropping of the sputtering efficiency. $^{27,61}$ One thing worth of mentioning is that the probability to form a nanopore can be as high as 80% for $60^\circ$ incident angle.

Among all the ions used in our simulation, Au has the largest mass and highest efficiency to drill pores in the $\text{MoS}_2$ sheet. For example, the probability of a 300 eV Au ion with vertical incident angle to create a nanopore is as high as 0.48 pore/ion. The ion flux for irradiation beam experiment is usually at least $10^{10}\ \text{cm}^{-2}/\text{s}$. This means billions of sub-nanometer pores can be produced per second by Au ion bombardment, indicating ion beam technique to be an efficient approach to generate sub-nanometer pore in single-layer $\text{MoS}_2$. One thing need to be noticed is that, when one pore is created, the probability for other pores created next to it is very low. On one hand, ion flux of $10^{10}$ $\text{cm}^{-2}/\text{s}$ in experiment means that only one ion will incident to the $10\ \text{nm} \times 10\ \text{nm}$ area of $\text{MoS}_2$ sheet per second, indicating a very low probability of pore overlapping. On the other hand, it is very easy to bombard any sample in a way that the sample is irradiated homogenously, e.g. by scanning. It is also worth noting that, in the nuclear stopping regime, Au ion can produce nanopore in the $\text{MoS}_2$ sheet with very high efficiency, whereas it is difficult to do so in graphene. $^{55, 62}$ This is because the more than one collision happen in single-layer $\text{MoS}_2$ as an analogy to the cascade collision in a bulk

system, which can introduce great damage in the target materials by incident ions, with a much higher probability compared with that in graphene. When the incident ions knock out one target atom in $MoS_2$ sample, this first knock-on atom may collide with other atoms in the $MoS_2$ sample, thus causing more atoms to be removed from $MoS_2$ sample. In this case, complex defects, such as the nanopores we observed, can even be produced by a single ion bombardment. But for graphene, damage often exists in the initial incident ion collisions, secondary collision caused by the first knock-on atoms could be hardly occur.

Among the nanopores generated by heavy ion bombardment shown above, the $V_{MoS6}$ nanopore is the most promising for the application in membrane separation. $^{17}$ On the one hand, the $V_{MoS6}$ pore has regular and stable pore edge, whereas the larger pores we get show relatively poor stability and the smaller pores have too small effective diameters and poor stability to pass through the gases. To show the thermodynamic stabilities of the $V_{MoS6}$ pore, $V_{MoS5}$ and the larger pore (e.g. $V_{Mo3S16}$), we explore the configuration change before and after the 25 ps relaxation at room temperature (300K), as shown in Figure S4, Figure S5 and Figure S6. We found that the deformation of the $V_{MoS6}$ pore is only 3％, indicating the $V_{MoS6}$ pore structure remains stable at room temperature. However, the atomic configuration of $V_{MoS5}$ and the larger pore changed continuously over time, indicating their poor stability. On the other hand, the diameter of $V_{MoS6}$ pore is about 0.6 nm, which is comparable to the size of gases. It has been reported that sub-nanometer pore is a fundamental prerequisite to achieving good selectivity for gas separation. $^{1,19,63}$ To evaluate the performance of the $MoS_2$ filter obtained by ion irradiation for gas separation, DFT calculation was applied to determine the selectivity of several gases (He, Ne, $H_2$, Ar and Kr).

First, the diffusion barriers for different gases (He, Ne, $H_2$, Ar and Kr) were calculated using the climbing image nudged elastic band CI-NEB scheme. The starting and ending positions of the molecular diffusion pathway were placed above and below

the center of the nanopore. A linear interpolation between the starting and ending points was used as an initial guess of the diffusion path.¹⁹ Twenty intermediate images were created by interpolating between the initial and final states, which are chosen as the local minima configurations obtained in the relaxation runs. It's worth noting that, H₂ passing through the nanopore in the vertical direction has the lowest diffusion barrier, as well as the highest priority. Therefore, we only did the calculation for the case that H₂ vertically passes through the nanopore, as reported in many other literature works.¹, ¹⁸, ¹⁹ By setting the energy of the initial configuration to be 0, the energy of other intermediate states relative to the initial configuration can be obtained (Figure 3a). The diffusion barrier for a given gas to pass through the MoS₂ filter is then defined to be the energy difference between the maximum energy and the minimum energy, as shown in Figure 3b.

The so called kinetic diameter, defined by the molecular distance at the minimum of the Lennard-Jones potential for non-polar molecules and the Stockmayer potential for polar molecules,⁶⁴ has been widely used for describing the transport mechanism of molecules through membranes with micropores.⁶⁵ The kinetic diameters of He, Ne, H₂, Ar and Kr are 0.26 nm⁶⁶, 0.275 nm⁶⁷, 0.289 nm⁶⁶, 0.34 nm⁶⁷ and 0.36 nm⁶⁷, respectively. However, our results demonstrate that the kinetic diameter does not correlate well with the diffusion barrier of the gas, as shown in Figure 3b. For instance, Ne has bigger kinetic diameter than He, but shows smaller diffusion barrier (0.4 eV) than He (0.64 eV). Similar inverted orders can also be found for H₂/He (0.47 eV and 0.64 eV for H₂ and He, respectively). The interaction between gases and the charged edge of MoS₂ nanopore is the reason why the kinetic diameter is not applicable to our case, which will be discussed later.

![](./images/813009902459944961_5.jpg)

Figure 3. (a) Change of the relative energy as a function of gas adsorption height as it passes through the pore. The dashline showed the position of $MoS_2$ plane. (b) Calculated diffusion barriers (red squares) of different molecular species. The diffusion barrier for a given gas to pass through the $MoS_2$ filter is defined to be the energy difference between the maximum energy and the minimum energy along the migration path. The size of the ball represents the kinetic diameter of different gases, which increases from left to right. (c) Pass through frequencies for different gases. The inset shows the transition state of the hydrogen molecule.

The selectivity $(Selectivity = A^X/A^Y = exp(-(\Delta E_x-\Delta E_y)/k_B T)$ between species X and Y) was estimated using diffusion barriers $\Delta E$ and the Arrhenius equation $A = A_0$ $exp(-\Delta E/k_B T)$, where $A$ is the diffusion rate (pass through frequency), $A_0$ is the diffusion pre-factor, $k_B$ is the Boltzmann constant and $T$ is the temperature. $^{19}$ The estimated selectivity for different molecular combinations at room temperature is listed in Table 1. We find that the single-layer $MoS_2$ with $V_{MoS6}$ pore has selectivity of nearly $10^3$ for $H_2$/He separation, which is nearly two order of magnitude higher than that of nanoporous

graphene (around 10)¹⁹ and other microporous membranes such as metal, silica, polymer, etc. (less than 10).⁵⁴ Moreover, the selectivity for the most frequent studies of He/Ne separation (>10⁴) is also much higher than that for porous silica based ultimate membranes, polyphenylene and porous graphene (several hundred to several thousand).¹⁹, ⁶³ Furthermore, the MoS₂ filter exhibits a high selectivity for Ne from other larger noble gases (selectivity > 10⁵) due to the exceptionally low diffusion barrier.

**Table 1.** Calculated selectivities at room temperature for different molecular combinations assuming a pre-factor of 10 ¹¹ s⁻¹ for all species.

<table>
<thead>
<tr>
<th>Structure</th>
<th>He</th>
<th>Ne</th>
<th>H₂</th>
<th>Ar</th>
<th>Kr</th>
</tr>
</thead>
<tbody>
<tr>
<td>He</td>
<td>---</td>
<td>1.1E+04</td>
<td>7.3E+02</td>
<td>2.2E+01</td>
<td>1.3E+02</td>
</tr>
<tr>
<td>Ne</td>
<td>9.1E-05</td>
<td>---</td>
<td>1.5E+01</td>
<td>2.5E+05</td>
<td>1.4E+06</td>
</tr>
<tr>
<td>H₂</td>
<td>1.4E-03</td>
<td>6.6E-02</td>
<td>---</td>
<td>1.6E+04</td>
<td>9.2E+04</td>
</tr>
<tr>
<td>Ar</td>
<td>4.5E-02</td>
<td>4.1E-06</td>
<td>6.1E-05</td>
<td>---</td>
<td>5.7E+00</td>
</tr>
<tr>
<td>Kr</td>
<td>7.9E-03</td>
<td>7.2E-07</td>
<td>1.1E-05</td>
<td>1.8E-01</td>
<td>---</td>
</tr>
</tbody>
</table>

The pass through frequency (the number of times that gases pass through the nanopore per second) for all gases was also estimated, using the same pre-factor A₀= 10¹¹ s⁻¹ as in other reports.¹⁹, ⁶³ We found that the diffusion barriers of Ne and H₂ can be overcome quite frequently. In contrast to the significantly low pass through frequencies (<0.1 s⁻¹) for larger gases Ar and Kr, Ne and H₂ exhibit a very high pass through frequency, with 10⁴ s⁻¹ and 10³ s⁻¹ for Ne and H₂ respectively. The pass through frequency for Ne (10⁴ s⁻¹) here is much higher than for Ne through graphene nanopores (1 s⁻¹).¹⁹ The pass through frequency of He (2 s⁻¹) also allows a good separation of this species from larger gases.

Both the selectivity and pass through frequency results indicate that the MoS₂ filter with V_MoS6 nanopores shows great potential for practical application in gas separation. As

shown in the previous section, the difference in diffusion barrier for different gases cannot be explained by their kinetic diameter. The charged edge of a nanopore in the MoS₂ sheet was reported to alter the ion selectivity and water permeability.¹⁷ Chemical functional groups such as hydroxyl groups bonded to the edges of graphene pores were also found to roughly double the water flux due to their hydrophilic character.¹⁴ Therefore, it is very likely that the charged edge of the sub-nanometer pores in MoS₂ sheet also strongly impact the penetration process of gas.

It has been shown that charge distribution can be strongly localized around the defects in single-layer MoS₂.⁶⁸⁻⁷⁰ To understand the charge transfer between the gas atom and the monolayer during the gas penetration process, we calculate the effective charge on individual atom. Here, we present a comprehensive study on the properties of various charge states based on the Bader analysis⁷¹ and the first-principles calculation⁴⁵. Using VASP code, the core charge and partition electrons amongst fragments of the system were quantified. Our results showed that He, Ne, H₂, Ar and Kr lose 0.0594, 0.1184, 0.089, 0.115, 0.0981 electrons to the MoS₂ sheet, respectively. Furthermore, we explore the charge density changes of the nanopores and the propagating gases during the penetration process. For Ar and Kr, the maximum point and the minimum point in the valley-like shaped curves have been chosen to calculate the charge density (**Figure 3a**). For other gases, the energy minimum point at the upper layer of the MoS₂ sheet and the middle of the pore in the MoS₂ sheet have been chosen to calculate the charge densities which are represented by yellow and brown isosurfaces respectively, as shown in **Figure 4**. The charge densities were clearly deformed when H₂, Ne, Ar and Kr were approaching the MoS₂ sheet, i.e., the isosurfaces level expanded toward the edge of the nanopores. This indicates that some attraction forces exist when the gas is close to the center of the pore. Combined with the quantitative charge transfer calculated by Bader analysis and the qualitative charge density map shown in **Figure 4**, we found that Ne loses more electrons compared with He, which leads to a larger polarizability. Therefore, a stronger attractive

electrostatic interaction will be formed between Ne and the $MoS_2$ sheet, as shown in **Figure 4a and 4b**. Such stronger electrostatic interaction leads to the lower energy barrier for Ne to pass through the nanopore compared with He, despite of its larger kinetic diameters. The similar explanation can be applied to the comparison between $H_2$ and He. Furthermore, the valley-like shape occurs at the top of the energy barrier for large gases, like Ar and Kr can also be explained by the electrostatic interaction between gases and the nanopores (**Figure 3a**). As shown in **Figure 4d and 4e**, the charge density has a tendency to overlap with that of the surrounding atoms when the gas travels from the maximum point to the minimum point in the valley-like shaped curve (**Figure 3a**).

![](./images/813009902459944961_6.jpg)

**Figure 4.** Charge densities of different gases and the nanopores during the penetration process are represented by yellow and brown surfaces for better comparison. The isosurface value is $0.01e/\mathring{A}^3$ for both yellow and brown surfaces. (a) He; (b) Ne; (c) $H_2$; (d) Ar; (e) Kr. The energy minimum point at the upper layer of the $MoS_2$ sheet and the middle of the pore in $MoS_2$ sheet have been chosen to calculate the charge density for He, Ne and $H_2$. The maximum point and the minimum point in the valley-like shaped curves have been chosen to calculate the charge densities for Ar and Kr. There is clear

deformation of the charge density towards the passing $H_2$, He, Ne, Ar and Kr when they get close to the $MoS_2$ sheet.

It has been reported that the separation mechanism based on kinetic diameters becomes less applicable when attractive forces beyond van der Waals interactions occur.$^{18}$ Some previous studies also have validated the feasibility and rationality of this charge polarization mechanism based on electrostatic interaction between the polarized gas and the charged edges.$^{17,19}$ Our results demonstrate that the unique characteristics of electron redistribution between Mo and S atoms at the nanopore edge of single-layer $MoS_2$ play an important role in determining the penetration process of gases, which are very likely to be the reason of the predicted high selectivity of $MoS_2$ filter.

### 4. Conclusion
In our report, MD simulations have been carried out to investigate the pore forming process in single-layer $MoS_2$ by heavy ion bombardment. Pores with sub-nanometer size (0.6 nm to 1.2 nm) in the $MoS_2$ sheet can be created by single ion bombardment. In addition, the pore size and shape can be controlled by the ion parameters including mass, energy, and incident angle. Furthermore, we found that ions with kinetic energy in the range of 200 eV to 3 keV show the highest probability to create sub-nanometer pores in $MoS_2$. The probability to create sub-nanometer pores can be as high as 0.8 pores per incident ion, indicating ion beam technology is a convenient and efficient way to create such pores in the $MoS_2$ sheet. We used DFT based first-principles calculations to demonstrate the applicability of these sub-nanometer size pores in $MoS_2$ for gas separation. The transport of He, Ne, $H_2$, Ar and Kr through the $V_{MoS6}$ pore, which is one representative of the sub-nanometer pores formed by ion bombardment, was studied in detail. We found that the $MoS_2$ filter with $V_{MoS6}$ pores show high selectivity for separating $H_2$/He and He/Ne, which is orders of magnitude higher than those which have

been reported for graphene and other membranes. The high selectivity was attributed to the interaction between gases and the charge of the pore in $MoS_2$. Our results will guide the usage of ion beam technology in single-layer $MoS_2$ for membrane applications.

## Acknowledgments
This work was supported by the National Natural Science Foundation of China (No., 11605063), Guangdong Innovative and Entrepreneurial Research Team Program (No.2014ZT05N200), Guangzhou Science and Technology Program General Projects (No. 201707010146), the Recruitment Program of Global Youth Experts, IAEA (CRP No. F11020 and Contract No. 21063). J.K. acknowledge the support from the NSF Center for Energy Efficient Electronics Science (E3S).

## Supporting Information
Nuclear stopping power ($S_n$) of the six ions with different energies in bulk $MoS_2$. Intrinsic structural defects in single-layer $MoS_2$. Dependence of the probability for different irradiation defects ($V_S$, $V_{S2}$, $V_{Mo}$, $V_{MoS3}$, $V_{MoS5}$, $V_{MoS6}$ and larger pores) on ion energy for Au ion irradiation. Characterization of pore geometry by the effective diameter. The stability of the $V_{MoS6}$ pore at room temperature. The stability of the $V_{MoS5}$ pore and the larger pore (e.g. $V_{Mo3S16}$) at room temperature. The average number of sputtered atoms in single-layer $MoS_2$ under ion bombardment as a function of ion energy. The differential charge densities for all the gases at the middle of the pore in the $MoS_2$ sheet.

## References
(1) Ambrosetti, A.; Silvestrelli, P. L. Gas Separation in Nanoporous Graphene from First
Principle Calculations. *J. Phys. Chem. C* **2014**, *118*, 19172-19179.

(2) Li, D.; Hu, W.; Zhang, J.; Shi, H.; Chen, Q.; Sun, T.; Liang, L.; Wang, Q. Separation of Hydrogen Gas from Coal Gas by Graphene Nanopores. *J. Phys. Chem.* **2015**, *119*, 25559-25565.

(3) Tsetseris, L.; Pantelides, S. T. Graphene: An impermeable or selectively permeable membrane for atomic species? *Carbon* **2014**, *67*, 58-63.

(4) Du, H.; Li, J.; Zhang, J.; Su, G.; Li, X.; Zhao, Y. Separation of Hydrogen and Nitrogen Gases with Porous Graphene Membrane. *J. Phys. Chem.* **2011**, *115*, 23261-23266.

(5) Li, H.; Song, Z. N.; Zhang, X. J.; Huang, Y.; Li, S. G.; Mao, Y. T.; Ploehn, H. J.; Bao, Y.; Yu, M. Ultrathin, Molecular-Sieving Graphene Oxide Membranes for Selective Hydrogen Separation. *Science* **2013**, *342*, 95-98.

(6) Qiu, Y.-H.; Li, K.; Chen, W.-Y.; Si, W.; Tan, Q.-Y.; Chen, Y.-F. Ion and water transport in charge-modified graphene nanopores. *Chinese Physics B* **2015**, *24*, 108201.

(7) Rollings, R. C.; Kuan, A. T.; Golovchenko, J. A. Ion selectivity of graphene nanopores. *Nat. Commun.* **2016**, *7*, 11408.

(8) Heiranian, M.; Farimani, A. B.; Aluru, N. R. Water desalination with a single-layer MoS₂ nanopore. *Nat. Commun.* **2015**, *6*, 8616.

(9) Liu, K.; Feng, J.; Kis, A.; Radenovic, A. Atomically thin molybdenum disulfide nanopores with high sensitivity for DNA translocation. *ACS nano* **2014**, *8*, 2504.

(10) Farimani, A. B.; Min, K.; Aluru, N. R. DNA Base Detection Using a Single-Layer

MoS₂. *ACS nano* **2014**, *8*, 7914-7922.

(11) Feng, J.; Liu, K.; Bulushev, R. D.; Khlybov, S.; Dumcenco, D.; Kis, A.; Radenovic, A. Identification of single nucleotides in MoS₂ nanopores. *Nat. Nano* **2015**, *10*, 1070-1076.

(12) Mishra, A. K.; Ramaprabhu, S. Functionalized graphene sheets for arsenic removal and desalination of sea water. *DESALINATION* **2011**, *282*, 39-45.

(13) Celebi, K.; Buchheim, J.; Wyss, R. M.; Droudian, A.; Gasser, P.; Shorubalko, I.; Kye, J. I.; Lee, C.; Park, H. G. Ultimate Permeation Across Atomically Thin Porous Graphene. *Science* **2014**, *344*, 289-292.

(14) Cohen-Tanugi, D.; Grossman, J. C. Water desalination across nanoporous graphene. *Nano lett.* **2012**, *12*, 3602-8.

(15) Shannon, M. A.; Bohn, P. W.; Elimelech, M.; Georgiadis, J. G.; Marinas, B. J.; Mayes, A. M. Science and technology for water purification in the coming decades. *Nature* **2008**, *452*, 301-10.

(16) Kim, H. W.; Yoon, H. W.; Yoon, S. M.; Yoo, B. M.; Ahn, B. K.; Cho, Y. H.; Shin, H. J.; Yang, H.; Paik, U.; Kwon, S.; Choi, J. Y.; Park, H. B. Selective Gas Transport Through Few-Layered Graphene and Graphene Oxide Membranes. *Science* **2013**, *342*, 91-95.

(17) Li, W.; Yang, Y.; Weber, J. K.; Zhang, G.; Zhou, R. Tunable, Strain-Controlled Nanoporous MoS₂ Filter for Water Desalination. *ACS nano* **2016**, *10*, 1829-35.

(18) Hauser, A. W.; Schwerdtfeger, P. Methane-selective nanoporous graphene membranes for gas purification. *PCCP* **2012**, 14, 13292-13298.

(19) Blankenburg, S.; Bieri, M.; Fasel, R.; Mullen, K.; Pignedoli, C. A.; Passerone, D. Porous graphene as an atmospheric nanofilter. *Small* **2010**, 6, 2266-71.

(20) Fischbein, M.; Drndić, M. Electron beam nanosculpting of suspended graphene sheets. *Appl. Phys. Lett.* **2008**, 93, 113107-113107-3.

(21) Kuhn, P.; Forget, A.; Su, D. S.; Thomas, A.; Antonietti, M. From Microporous Regular Frameworks to Mesoporous Materials with Ultrahigh surface Area: Dynamic Reorganization of Porous Polymer Networks. *J. Am. Chem. Soc.* **2008**, 130, 13333-13337.

(22) Koenig, S. P.; Wang, L.; Pellegrino, J.; Bunch, J. S. Selective molecular sieving through porous graphene. *Nature Nanotechnology* **2012**, 7, 728-732.

(23) Li, Z.; Chen, F. Ion beam modification of two-dimensional materials: Characterization, properties, and applications. *Applied Physics Reviews* **2017**, 4, 011103.

(24) Bai, Z.; Zhang, L.; Li, H.; Liu, L. Nanopore Creation in Graphene by Ion Beam Irradiation: Geometry, Quality, and Efficiency. *ACS Appl. Mater. Interfaces* **2016**, 8, 24803-9.

(25) Zhao, S.; Xue, J. Modification of graphene supported on SiO₂ substrate with swift heavy ions from atomistic simulation point. *Carbon* **2015**, 93, 169-179.

(26) Li, W.; Wang, X.; Zhang, X.; Zhao, S.; Duan, H.; Xue, J. Mechanism of the defect formation in supported graphene by energetic heavy ion irradiation: the substrate effect. *Scientific reports* **2015**, *5*, 9935.

(27) Li, W.; Liang, L.; Zhao, S.; Zhang, S.; Xue, J. Fabrication of nanopores in a graphene sheet with heavy ions: A molecular dynamics study. *J. Appl. Phys.* **2013**, *114*, 234304.

(28) Zhao, S.; Xue, J.; Wang, Y.; Yan, S. Effect of SiO₂ substrate on the irradiation-assisted manipulation of supported graphene: a molecular dynamics study. *Nanotechnology* **2012**, *23*, 285703.

(29) Zhao, S.; Xue, J.; Liang, L.; Wang, Y.; Yan, S. Drilling Nanopores in Graphene with Clusters: A Molecular Dynamics Study. *J. Phys. Chem. C* **2012**, *116*, 11776-11782.

(30) Vazquez, H.; Ahlgren, E. H.; Ochedowski, O.; Leino, A. A.; Mirzayev, R.; Kozubek, R.; Lebius, H.; Karlusic, M.; Jaksic, M.; Krasheninnikov, A. V.; Kotakoski, J.; Schleberger, M.; Nordlund, K.; Djurabekova, F. Creating nanoporous graphene with swift heavy ions. *CARBON* **2017**, *119*, 200-200.

(31) O'Hern, S. C.; Boutilier, M. S.; Idrobo, J. C.; Song, Y.; Kong, J.; Laoui, T.; Atieh, M.; Karnik, R. Selective ionic transport through tunable subnanometer pores in single-layer graphene membranes. *Nano Lett.* **2014**, *14*, 1234-41.

(32) Ghorbani-Asl, M.; Kretschmer, S.; Spearot, D. E.; Krasheninnikov, A. V. Two-dimensional MoS₂ under ion irradiation: from controlled defect production to

electronic structure engineering. *2D Materials* **2017**, *4*, 025078.

(33) Madauß, L.; Ochedowski, O.; Lebius, H.; Ban-d'Etat, B.; Naylor, C. H.; Johnson, A. T. C.; Kotakoski, J.; Schleberger, M. Defect engineering of single- and few-layer $\text{MoS}_2$ by swift heavy ion irradiation. *2D Materials* **2016**, *4*, 015034.

(34) Guo, H.; Sun, Y.; Zhai, P.; Yao, H.; Zeng, J.; Zhang, S.; Duan, J.; Hou, M.; Khan, M.; Liu, J. Swift-heavy ion irradiation-induced latent tracks in few- and mono-layer $\text{MoS}_2$. *Appl. Phys. A* **2016**, *122*, 1-7.

(35) Kim, T. Y.; Cho, K.; Park, W.; Park, J.; Song, Y.; Hong, S.; Hong, W. K.; Lee, T. Irradiation effects of high-energy proton beams on $\text{MoS}_2$ field effect transistors. *ACS nano* **2014**, *8*, 2774-81.

(36) Ma, Q.; Odenthal, P. M.; Mann, J.; Le, D.; Wang, C. S.; Zhu, Y.; Chen, T.; Sun, D.; Yamaguchi, K.; Tran, T.; Wurch, M.; McKinley, J. L.; Wyrick, J.; Magnone, K.; Heinz, T. F.; Rahman, T. S.; Kawakami, R.; Bartels, L. Controlled argon beam-induced desulfurization of monolayer molybdenum disulfide. *J. Phys.: Condens. Matter* **2013**, *25*, 252201.

(37) Bai, Z.; Zhang, L.; Liu, L. Bombarding Graphene with Oxygen Ions: Combining Effects of Incident Angle and Ion Energy To Control Defect Generation. *J. Phys. Chem. C* **2015**, *119*, 26793-26802.

(38) Zhao, S.; Xue, J.; Kang, W. Ion selection of charge-modified large nanopores in a graphene sheet. *J. Chem. Phys.* **2013**, *139*, 114702.

(39) Khare, K. S.; Khare, R. Directed Diffusion Approach for Preparing Atomistic Models of Crosslinked Epoxy for Use in Molecular Simulations. *Macromol. Theory Simul.* **2012**, *21*, 322-327.

(40) Jiang, J.-W.; Park, H. S.; Rabczuk, T. Molecular dynamics simulations of single-layer molybdenum disulphide ($\text{MoS}_2$): Stillinger-Weber parametrization, mechanical properties, and thermal conductivity. *J. Appl. Phys.* **2013**, *114*, 064307.

(41) Jiang, J. W. Parametrization of Stillinger-Weber potential based on valence force field model: application to single-layer $\text{MoS}_2$ and black phosphorus. *Nanotechnology* **2015**, *26*, 315706.

(42) Ziegler, J. F. *The stopping and range of ions in solids / J.F. Ziegler, J.P. Biersack, U. Littmark*, Pergamon: New York, 1985.

(43) Tersoff, J. New empirical approach for the structure and energy of covalent systems. *Phys. Rev. B* **1988**, *37*, 6991-7000.

(44) Hohenberg, P.; Kohn, W. Inhomogeneous Electron Gas. *Phys. Rev.* **1964**, *136*, B864-B871.

(45) Kresse, G.; Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. *Comput. Mater. Sci.* **1996**, *6*, 15-50.

(46) Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. *Phys. Rev. B* **1996**, *54*, 11169-11186.

(47) Blöchl, P. E. Projector augmented-wave method. *Phys. Rev. B* **1994**, *50*, 17953-17979.

(48) Kresse, G.; Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. *Phys. Rev. B* **1999**, *59*, 1758-1775.

(49) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 3865-3868.

(50) Klimeš, J.; Bowler, D. R.; Michaelides, A. Chemical accuracy for the van der Waals density functional. *J. Phys.: Condens. Matter* **2010**, *22* (2), 022201.

(51) Guo, X.; Zhang, X.; Zhao, S.; Huang, Q.; Xue, J. High adsorption capacity of heavy metals on two-dimensional MXenes: an ab initio study with molecular dynamics simulation. *PCCP* **2015**, *18*, 228-233,.

(52) Zhao, S.; Xue, J.; Kang, W. Gas adsorption on MoS₂ monolayer from first-principles calculations. *Chem. Phys. Lett.* **2014**, 595-596, 35-42.

(53) Monkhorst, H. J.; Pack, J. D. Special points for Brillouin-zone integrations. *Phys. Rev. B* **1976**, *13*, 5188-5192.

(54) Henkelman, G.; Uberuaga, B. P.; Jonsson, H. A climbing image nudged elastic band method for finding saddle points and minimum energy paths. *J. Chem. Phys.* **2000**, *113*, 9901-9904.

(55) Lehtinen, O.; Kotakoski, J.; Krasheninnikov, A. V.; Tolvanen, A.; Nordlund, K.; Keinonen, J. Effects of ion bombardment on a two-dimensional target: Atomistic

simulations of graphene irradiation. *Phys. Rev. B* **2010**, *81*.

(56) Krasheninnikov, A. V.; Nordlund, K.; Keinonen, J. Production of defects in supported carbon nanotubes under ion irradiation. *Physical Review B - Condensed Matter and Materials Physics* **2002**, *65*, 1654231-1654238.

(57) Pomoell, J. A. V.; Krasheninnikov, A. V.; Nordlund, K.; Keinonen, J. Ion ranges and irradiation-induced defects in multiwalled carbon nanotubes. *J. Appl. Phys.* **2004**, *96*, 2864-2871.

(58) Tolvanen, A.; Kotakoski, J.; Krasheninnikov, A. V.; Nordlund, K. Relative abundance of single and double vacancies in irradiated single-walled carbon nanotubes. *Applied Physics Letters* **2007**, *91*, 173109.

(59) Ziegler, J. F.; Ziegler, M. D.; Biersack, J. P. SRIM – The stopping and range of ions in matter (2010). *Nucl. Instrum. Methods Phys. Res., Sect. B: Beam Interactions with Materials and Atoms* **2010**, *268*, 1818-1823.

(60) Schleberger, M.; Lebius, H.; Akcöltekin, S.; Osmani, O.; Bukowska, H.; Peters, T.; Alzaher, I.; Monnet, I.; d'Etat, B. Unzipping and folding of graphene by swift heavy ions. *Appl. Phys. Lett.* **2011**, *98*, 103103-103103-3.

(61) Muszynski, R.; Seger, B.; Kamat, P. V. Decorating graphene sheets with gold nanoparticles. *J. Phys. Chem. C* **2008**, *112*, 5263-5266.

(62) Gruber, E.; Wilhelm, R. A.; Petuya, R.; Smejkal, V.; Kozubek, R.; Hierzenberger, A.; Bayer, B. C.; Aldazabal, I.; Kazansky, A. K.; Libisch, F.; Krasheninnikov, A. V.;

Schleberger, M.; Facsko, S.; Borisov, A. G.; Arnau, A.; Aumayr, F. Ultrafast electronic response of graphene to a strong and localized electric field. *Nat. Commun.* **2016**, 7, 13948.

(63) Hu, W.; Wu, X.; Li, Z.; Yang, J. Helium separation via porous silicene based ultimate membrane. *Nanoscale* **2013**, 5, 9062-6.

(64) Tsuru, T.; Igi, R.; Kanezashi, M.; Yoshioka, T.; Fujisaki, S.; iwamoto, Y. Permeation properties of hydrogen and water vapor through porous silica membranes at high temperatures. *AIChE Journal* **2011**, 57, 618-629.

(65) Kanezashi, M.; Yada, K.; Yoshioka, T.; Tsuru, T. Organic–inorganic hybrid silica membranes with controlled silica network size: Preparation and gas permeation characteristics. *J. Membr. Sci.* **2010**, 348, 310-318.

(66) Mehio, N.; Dai, S.; Jiang, D. E. Quantum Mechanical Basis for Kinetic Diameters of Small Gaseous Molecules. *J. Phys. Chem. A* **2014**, 118, 1150-1154.

(67) Breck, D. W. *Zeolite molecular sieves: structure, chemistry, and use*, Wiley: New York, **1974**.

(68) Bampoulis, P.; van Bremen, R.; Yao, Q.; Poelsema, B.; Zandvliet, H. J. W.; Sottthewes, K. Defect Dominated Charge Transport and Fermi Level Pinning in MoS₂/Metal Contacts. *ACS Appl. Mater. Interfaces* **2017**, 9, 19278-19286.

(69) Ghorbani-Asl, M.; Enyashin, A. N.; Kuc, A.; Seifert, G.; Heine, T. Defect-induced conductivity anisotropy in MoS₂ monolayers. *Phys. Rev. B* **2013**, 88.

(70) Park, J. H.; Sanne, A.; Guo, Y. Z.; Amani, M.; Zhang, K. H.; Movva, H. C. P.; Robinson, J. A.; Javey, A.; Robertson, J.; Banerjee, S. K.; Kummel, A. C. Defect passivation of transition metal dichalcogenides via a charge transfer van der Waals interface. *Sci. Adv.* **2017**, 3.

(71) Tang, W.; Sanville, E.; Henkelman, G. A grid-based Bader analysis algorithm without lattice bias. *J. Phys.: Condens. Matter* **2009**, 21, 084204.

Table of Contents

![](./images/813009902459944961_7.jpg)