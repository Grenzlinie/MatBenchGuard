Author's Accepted Manuscript

Pyridinic nitrogen doped nanoporous graphene as desalination membrane: molecular simulation study

Qi Chen, Xiaoning Yang

![](./images/814599190146449408_1.jpg)

www.elsevier.com

PII: S0376-7388(15)30148-4
DOI: http://dx.doi.org/10.1016/j.memsci.2015.08.052
Reference: MEMSCI13939

To appear in: *Journal of Membrane Science*

Received date: 21 April 2015
Revised date: 17 July 2015
Accepted date: 24 August 2015

Cite this article as: Qi Chen and Xiaoning Yang, Pyridinic nitrogen doped nanoporous graphene as desalination membrane: molecular simulation study, *Journal of Membrane Science*, http://dx.doi.org/10.1016/j.memsci.2015.08.052

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting galley proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Pyridinic Nitrogen doped Nanoporous Graphene as Desalination Membrane: Molecular Simulation Study

Qi Chen and Xiaoning Yang*

State Key Laboratory of Materials-Oriented Chemical Engineering, College of Chemistry and Chemical Engineering, Nanjing Tech University, Nanjing 210009, China.

## Abstract:

Functionalized nanoporous graphene has shown great promise as emerging membrane. Herein, we computationally demonstrate the separation performance using pyridinic-like nitrogen doped nanoporous graphene as reverse osmosis desalination membrane. The water permeation and salt rejection of the functionalized graphene membranes with various nitrogen-doping levels were simulated and characterized. We show that all functionalized graphenes investigated in this work exhibit higher water flux and acceptable salt rejection. In particular, the NOH graphene membrane with partial hydroxyl group inclusion shows excellent desalination efficiency. The interfacial properties of water and ions, as well as their free energy landscapes in passing through the graphene nanopores have been simulated in order to explore the desalination mechanism. The moderate free energy barriers for water passages confirm larger water fluxes in the functionalized graphene membranes. It was revealed that the salt rejection for the functionalized graphenes is the pore size exclusion of hydrated ions and the charged repulsion from pore surfaces is not the main factor. Overall, our results indicate that pyridinic-like nitrogen doped graphenes have a significant potential as nanostructured desalination membranes.

* Corresponding author (Xiaoning Yang)
E-mail: Yangxia@njtech.edu.cn

**Keywords:** Pyridinic-nitrogen, Functionalized graphene, Desalination, Nanopores, Molecular simulation.

## Introduction

Reverse osmosis (RO) with semipermeable membranes has become the leading technology for desalination because of its lower energy consumption [1,2]. However, in current RO technology, it is still required to improve water flux rate and increase membrane fouling-resistant ability [1,3], while keeping higher salt rejection level. Because polymeric RO membranes do not have well-defined pores, they generally possess lower water permeability[3]. Nanoporous membranes, such as zeolites[4,5] and carbon nanotubes (CNTs)[6-8], are expected to have great possibility as alternates to existing RO membranes. However, the water permeability of zeolite membrane is still very low due to larger membrane thickness and complex pore architecture[3,9]. For the CNT-based membranes，the fabrication of CNT alignment and CNT tip remains quiet huge challenge[10]. So, developing new membrane materials with high water flux has attracted considerable attention in order to make RO desalination process more economic.

Graphene, as a new-type two-dimensional carbon material[11], has shown potential application as separation membrane material owing to its unique properties[11-14]. In particular, the monolayer thickness of graphene can allow fast molecular penetration[15] and reduce the concentration polarization effect[16]. At present, large-scale monolayer graphene film can be prepared onto copper substrates[17]. However, the perfect graphene sheet is impermeable to molecules as small as He[18]. Therefore, it is necessary to "drill

holes" on graphene sheet[18]. Various experimental methods[19-22] for introducing nanopores on graphene surface are in progress, which accelerates the application of graphene membranes. For example, graphene with defined nanoscale pore sizes has been successfully prepared and applied in the gas separation[23]. In recent experimental report, nanoporous single-layer graphene has been successfully fabricated as desalination membrane with tremendously high water transport and almost complete salt rejection[24] .

Generally, hole formation in graphene would reduce its thermodynamic stability[25]. As a result, unsaturated carbon atoms at the pore edge of graphene are required to be passivated by functional groups in order to decrease the formation energy of graphene pore and to improve the stability of pore edge[25,26]. Furthermore, functionalization of pore edge might modify pore-size and pore-chemistry, probably improving permeation performance. It was reported that the gas separation performance of porous graphene membranes can be affected by the chemical functionalization on pore rim[27,28]. Hydrogenated and hydroxylated graphenes with fast water transport and acceptable salt rejection have been simulated as desalination membranes[29]. These studies clearly show the probability of tuning water and ions transport through functionalizing graphene pores as RO desalination membranes.

Nitrogen atom with comparable atomic size is regarded as an excellent element for the chemical doping of carbon material[30]. Three nitrogen doping configurations are commonly used for nitrogen-doped (N-doped) graphene: (1) pyridinic N (N bonding with two C atoms at the edges or defects of graphene); (2) pyrrolic N (forming a

five-membered ring); (3) quaternary N or graphitic N (nitrogen atoms replacing the C atoms inside the graphene layers)[31]. Among them, N-doped graphene sheets with pyridinic-like hexagonal hole preserve excellent intrinsic strength, cyclic stability, and thermal stability[32,33]. These properties are in favor of the application of pyridinic-like N doped nanoporous graphene as membrane materials. Up to now, extensive experimental methods[34-38] have been developed to fabricate N-doped porous graphene materials. In addition, the nitrogen atoms on the edge of graphene pore can be easily controlled by tuning experimental conditions[39]. Recently, single layer graphene doped with pure pyridinic N at its edges and defects has been successfully synthesized by thermal chemical vapor deposition of hydrogen and ethylene on Cu foils in the presence of ammonia[40]. Therefore, pyridinic-like Nitrogen doped porous graphene membranes have the great possibility of realization as desalination RO membranes. Although limited studies have been carried out for the gas[23] and isotope[41] separations using pyridinic-like N doped graphene membranes, their performance in water desalination has not yet studied, to our best knowledge.

With the above in mind, in this paper, molecular dynamics (MD) simulations were conducted to investigate the water permeation and salt rejection using single-layer porous graphene membranes with pyridinic N doped functionalization on the pore rims. Various nitrogen doping levels were considered in this work. Meanwhile, it is postulated that the neutral charged feature of the pyridinic N graphene pores will be effective for the rejection of both positive and negative ions. In order to understand the desalination mechanism, we further compute the potentials of mean forces (PMFs) for water and ions

transferring through the graphene pores. The pore size effect and the distribution of water molecules in the vicinity of the functionalized pores are discussed.

## Methods
Models and simulations details: The simulation system was illustrated in Fig. 1 (top panel), where the functionalized graphene was positioned at the cell center and two chambers were on both sides of the graphene sheet. The right chamber was designed as the feed side, representing 0.6 M NaCl aqueous solution, which is equivalent to the salt concentration in seawater. The left chamber is the permeate side, containing pure water molecules. The solution density was fixed to be $\sim 1\mathrm{g/cm^3}$ on both chambers. The dimension size of the graphene model is $34.09{	imes}34.44\ \mathrm{\mathring{A}^2}$ with the drilling pore in the center of sheet. Five functionalized nanoporous graphenes were simulated with different pyridinic-like N doping levels in the pore rim. The detailed illustration on all the structures of membrane pores was given in the bottom panel of Fig. 1. They include the N-graphene membrane with the unsaturated carbon atoms in the pore rim completely replaced by nitrogen atoms (pure pyridinic-like); the NH-graphene and the NH3-graphene with the unsaturated carbon atoms partially replaced by N atoms; the N-OH graphene membrane with N replaced and OH passivated. For comparison, we also investigated the graphene pore passivated with hydrogen atoms (H-graphene membrane).
The pore diameters for these functionalized graphene membranes are in the range of 0.75-0.89 nm, which was characterized and shown in Fig.1.

Carbon atoms in the functionalized graphene membrane were modeled as the uncharged Lennard-Jones (L-J) sphere using the reference parameters[42,43]. The

flexible OPLS-AA force field[44] was used to model the functional groups on the graphene pores. Water was modeled using the SPC/E model[45]. The electrolyte ions were described by the proposed potential[46,47], which could reproduce the ion hydration energy of ions[48]. We employed the Lorentz-Berthelot mixing rule for the L-J interactions between different particles. The particle mesh Ewald (PME) method was used to calculated the long-range electrostatic interactions. The cutoff for the L-J interaction was set to be 10 Å.

![](./images/814599190146449408_2.jpg)

Fig. 1 (Top panel) Lateral view of the simulation system, showing a functionalized graphene membrane placed in the center of the box and two chambers on the both sides of the functionalized graphene. The right chamber contained NaCl solution, while the left chamber was pure water. (Bottom panels) Top view of five functionalized graphene membranes. Carbon atoms in functionalized graphenes are shown as cyan spheres, nitrogen in blue, hydrogen in white, oxygen in red, $Na^+$ in green, and $Cl^-$ in purple. The pore diameters (red line) in the graphene membranes were defined as the diameters of a gray ball fitting the pores.

All MD simulations were performed by the LAMMPS package[49], using the

canonical ensemble (NVT) with 1 fs time step. In order to confirm the reasonability of the simulation procedure, we also conducted additional simulation run with an NPT ensemble for the pre-equilibrium step. It was found that the consistent result is obtained by using the NVT and NPT ensembles in the pre-equilibrium process. The Nose-Hoover thermostat[50] was used to keep the temperature (300 K) constant. The simulation systems were firstly equilibrated, and then we simulated the pressure-driving desalination behavior. In the permeation MD simulation, a rigid graphene plate as the piston was placed at the rightest side of the simulation cell and external force was imposed to the piston. The carbon atoms in the piston were also treated as the uncharged L-J sphere [42,43] , which is the same as that for the graphene membranes in our works. To generate the desired pressure ( $\Delta P$ ), the applied force (f) was exerted on each carbon atom of the piston based on the equation, $f=\Delta P \cdot A / n[51]$ , where A is the area of the piston and n refers to the total number of carbon atoms of the piston. The same average applied force acting on every carbon atom of graphene piston is useful for keeping the structure of the piston no change over time. The hydrostatic pressure, ranging from 50 to 530 MPa, was created along the permeation direction. In the non-equilibrium MD simulation, it was very common to apply higher pressure in order to reduce thermal noise and enhance signal/noise ratio within a nanosecond timescale[5].

**PMF simulations:** In this work, we used two different methods to compute the PMFs for ions and water, respectively. In aqueous medium, ions are generally in the form of hydrated ions and the effect of thermal noise is relatively small. Thus, for the ion passing through the graphene pores, the SMD (steered molecular dynamics) method is effective

in the calculation of the ion PMF profile. This SMD approach has been successfully used in the ion PMF computations in previous works [52,53]. In the SMD procedure, the designed ion was pulled by a spring and the pulling work was used to approximate the free energy change of ions translation through the graphene pores[54]. In order to reduce error accumulation, we adopted the previous method[55] and decomposed the SMD process into 10 windows from the position z=15 Å to z=-15 Å, and in each window the pulling distance is 3Å. The PMFs for water passing through the functionalized graphene membranes were calculated using the force integration method [56,57]. For single water molecule, the effect of thermal noise could become remarkable, which could lead to larger deviation in the PMF computation. So we choose the rigorous force integration method. The detailed simulation processes for the PMF computations of water and ions were given in the supporting information.

Quantum mechanics computation: Density functional theory (DFT) calculations with ADF package[58] were employed to compute the atomic charges of each functionalized graphene. The structure optimization of the functionalized graphene clusters (see Fig. S1) were obtained at the Perdew-Burke-Ernzerh including dispersion correction (PBE-D)[59,60] level of theory with the localized double-$\zeta$ plus polarization (DZP) basis sets. The atomic charges were represented by the Hirshfeld charges[59,61] for each functionalized nanoporous graphene, as shown in Fig. S1. The Hirshfeld charges are widely recommended because they yield chemically meaningful charges [62,63]. Meanwhile, it has been confirmed that hirshfeld charges could be effectively applied in the calculations of the charges of functionalized graphenes [64,65]. Here, we did not use

other charge computation methods. However, our computation confirmed that our simulation result is independence of the methods of atomic charge calculation. The electron density isosurfaces of the functionalized graphene pores and hydrated ions were depicted at the value of $0.02e/\AA^3$.

## Results and discussion
At first, the desalination performances for the five graphene membrane models (see Fig. 1) were simulated. Fig. 2a and Fig. 2b plot the number of net transferred water molecules $(N_w)$ as a function of simulation time for the N-graphene and H-graphene membranes, respectively. For other membranes, similar data has been shown in Fig. S2. There appears linear behavior of the time-dependence $N_w$ profiles, demonstrating stable transport of water molecules under pressure-driven force[5,66]. As expected, higher pressure leads to a larger number of $N_w$. It is noted that for the N-graphene membrane, the $N_w$ curve reaches a saturation plateau with time processing, signifying that the feed reservoir has become depleted.

![](./images/814599190146449408_3.jpg)

Fig. 2 Number of net transferred water molecules as a function of time for (a) N-grahpene and (b) H-graphene. (c) Water flux across five functionalized graphene membranes as a function of the external pressure. The arrow in Fig. 2(a) indicates decrease of pressure from upper to down.

From the slope of $N_w$ line, the water flux across the graphene membranes can be extracted. In Fig. 2c, the water permeating flux shows a linear increase with the pressure, well consistent with the observations in other nanoporous membranes[29,67]. Furthermore, as seen in Fig. 2c, under the same pressure condition, the N-graphene membrane exhibits obviously higher water flux than other graphene membranes. In general, for the five functionalized graphene membranes, larger pore can produce higher flux. However, the NOH-graphene membrane shows relatively higher flux than the H-graphene, even though it has smallest pore size and meanwhile the hydroxyl groups might hold water due to hydrogen-bonding interaction. This exception could be ascribed to the fact that the hydrophilic hydroxyl groups in the pore rim with decreased conformational order could create a smoother entropic landscape for water molecules to traverse across the pore, leading to faster water flow [29]. It should be emphasized that, although the permeation simulation was conducted under high pressure condition, the linear relation between the water flux and the pressure suggests that our simulation result can be extended to actual operating pressure (~5 MPa).

In Fig. 2c, the N-graphene membrane with complete N doping pore exhibits excellent water penetrability even under low pressure. For instance, at 130 MPa, the water flux is ~66 ns⁻¹. Under the condition of equivalent pore size, this water flux is six times higher than that using pristine graphene pore[15], three times higher than that for CNT pore[15,67]. Besides, the water flux for the H-graphene pore can also achieve 20 ns⁻¹ under this pressure, which is also comparable to other reported nanoporous membranes[68]. The obtained water fluxes indicate that all the pyridinic N doped

graphene membranes in this work possess higher water penetration ability.

The results in Fig. 2c can be used to estimate the average osmotic pressure. The transmembrane water flux is expected to reach zero when the applied pressure across the membrane is equal to the osmotic pressure of feed side. Then we can extrapolate the flux curves to the intersections with the pressure coordinate and the crossover occurs at ~2.3 MPa for all the five flux lines. This value is close to the theoretical osmotic pressure (1.5 MPa) in the initial concentration of feed side. This simple comparison might provide a straight confirmation of the rationality of permeation simulation.

![](./images/814599190146449408_4.jpg)

Fig. 3 Salt rejections for five functionalized graphene membranes vs the external pressure. The insert shows comparison of water permeability among functionalized graphene membranes.

We further evaluated the salt rejection for the five functionalized graphene membranes. The ion rejection ($R$) was calculated using the following equation[69], $R=1-N_{1/2}/N_{0}$, where $N_{0}$ is the initial ion number in the feed side and $N_{1/2}$ is the ion number in the permeate side when half amount of water have passed through the membrane. The simulated salt rejections for NaCl are about 100% for the NOH-graphene in the pressure range of 130-410 MPa, which is consistent with the observed phenomenon that no any ion has been found in the permeate side during the simulation period. The

H-graphene membrane also demonstrates higher salt rejection (>93%). Under higher pressures, the salt rejection of other graphene membranes show somewhat declined behavior. The N-graphene membrane with larger pore size has the lowest salt rejection, in accordance with its highest water flux. However, under lower pressure condition, all the five graphene membranes have 100% salt rejection. Overall, our functionalized graphene membranes have analogous salt rejection with the graphyne-3 membrane[51]. However, under similar pore size condition, the obtained salt rejection for the N-doped graphene membranes in this work is obviously higher than the salt rejection using the graphene membranes with hydrogen and hydroxyl functionalization[29].

It is observed that the salt rejection ($R$) decreases with the applied external pressure, as shown in Fig. 3. This behavior is consistent with the result observed in other graphene membranes[29]. This behavior can be explained as the large effective volume of ions in solution, which causes them to respond more sensitively to pressure increase. But an opposite result was also reported for graphyne membranes[69], in which the salt rejection efficiency increases slightly with the applied pressure at relatively high salt concentration. The cause for this difference can be ascribed to the effect of membrane pore density[70]. Hence, in actual porous graphene membranes, the increased surface porosity might improve the salt rejection.

The water permeability, defined as water permeating volume per unit membrane area per day and per unit pressure, was further calculated for each graphene membrane. We used the porosity of 10% [29] in the permeability calculation and the results are shown in the insert of Fig. 3. The highest water permeability for the N-graphene is ~22.8

$L/cm^{2}$/day/MPa, and the least water permeability is ~10.0 $L/cm^{2}$/day/MPa for the H-graphene membrane. The water permeability reported in this work should be of the same orders of magnitude as those for the graphyne membranes[51] and graphene membranes[29] in previous works. Actually, a serious comparison between various simulation results is relatively difficult, because different potential models were used in these works. More specifically, various computation methods were adopted in the pore size characterization, which probably leads to the difference in the permeating pore area. However, in our result, with the relatively conservative porosity (10%), the achieved water permeability for the NOH graphene membrane is several orders of magnitude higher than those of current commercial RO membranes[9,71], along with the 100% salt rejection. For other graphene membranes in this work, although the salt rejection is somewhat decreased with the pressure, the higher water permeability still displays the better effectiveness of desalination. According to the above analysis, the nitrogen-doped graphene membranes could achieve desalination with excellent water permeability and higher salt rejection.

We also analyzed the interfacial distribution of water molecules near the membrane pore surfaces. The density profiles of water molecules are shown in left panel of Fig. 4, where z=0 represents the pore position. The density profiles were obtained within an imaginary cylinder, with the axis perpendicular to the graphene sheet and the cylinder diameter equal to the pore diameter. As shown in Fig. 4, water molecules have an accumulation near the membrane pore[72], suggesting an enhanced surface adsorption. The NOH-graphene and H-graphene membranes that have smaller pore sizes can produce

higher interfacial density of water.

![](./images/814599190146449408_5.jpg)

Fig. 4 Five functionalized graphenes, from top to bottom, are N-graphene, NH-graphene, NH3-graphene, NOH-graphene and H-graphene, respectively. (left panel) relative density distribution of water along z axis for five functionalized graphene membranes, Herein, $\rho_o$ is the bulk water density ($\sim$0.0031 $\text{\AA}^{-3}$), and the inserts signify that the time dependence of occupying number ($N_{oc}$) of water molecules within pore for graphene membrane. 2-D distribution maps for oxygen (middle panel) and hydrogen (right panel) atoms in water in the pore regions for different functionalized graphene. Light blue and red indicate regions with the lowest and highest probability of finding an oxygen or hydrogen atoms, respectively.

The N-graphene membrane exhibits the highest water density within the pore, demonstrating more occupation of water molecules inside the pore. Comparatively, the H-graphene pore gives the least pore density. The water occupation number within the

graphene pore region ($-2\mathrm{\mathring{A}} < z < 2\mathrm{\mathring{A}}$) at any time was also shown in the inserts of Fig. 4.

These results show that higher water flux in the N-graphene membrane corresponds to the larger pore occupation number. In the right panel of Fig. 4, we show the two-dimensional (2-D) density maps of oxygen and hydrogen atoms in water that locate within the pore regions. The pore geometry and size have obvious influence on the water distribution pattern, which are expected to further affect the water transport across the pores. For the symmetrical pores in the N-graphene and H-graphene, the circular shapes are observed for the 2-D density maps. In particular, more crossing area is available for water passage in the N-graphene pore, producing larger water penetrating flux. For other graphene pores, irregular shapes can be seen in the 2-D density maps and only partial areas are effective for water penetration. This reduced effective pathways of water cause lower water flux through the pores. We further computed the residence time distributions for water molecules within the pore regions. The result in Fig. S3 shows that water molecules can stay inside the pore region for a period of time for all the graphene membranes. This pore dwelling nature suggests water transport across the graphene membranes might adopt a stepped or quantized manner, which has been reported in previous studies[69,73]. It is also shown that N-graphene pore has the smallest residence time, corresponding to fast pore crossing. The interaction between water and graphene could be further characterized by the local pressure components (normal and tangential) near the surfaces. As shown in Fig. S4, near the graphene surface, there appears obvious oscillation for the normal and tangential pressure components, which is associated with the local density fluctuation in the solid-liquid interface (for detail, see supplementary

material).

We also show the density distributions of $Na^+/Cl^-$ ions around the graphene membranes in Fig. S5. The ion distribution is overall symmetrical with respect to the membrane pore without obvious ion polarization, possibly resulting from the neutral characteristic of the N-doped graphene membranes. It is interesting to note that, as compared with the water contact layer, the ion layer is generally located relatively far away from the surface. It is expected that this interfacial ion layer might provide certain impedance against the water passage.

In order to further understand the thermodynamics mechanism in the desalination process, the PMF was used to represent the free energy landscape for a designed water molecule passing through the graphene membranes. In Fig. 5, the PMF profiles show energetic barrier when water travelling across the membrane pore. As shown in Fig. 5, the free energy barriers are found to be moderate in the range of 2.2-2.8 kcal/mol (3.7-4.6 $k_B$T, equivalently) in the order of N-graphene < NH-graphene < NH3-graphene < NOH-graphene < H-graphene. The changing trend of the PMF barriers is generally in accordance with the water flux variation among the five graphene membranes. Meanwhile, the magnitude order of these barriers is comparable with the previous results (~2.5-4.8 $k_B$T) for water spontaneously entering the (6,6) CNT[74]. This means that no significant obstruction occurs for water permeation through the N-functionalized graphene membranes. This lower PMF for these graphene membranes is consistent with the higher water penetration fluxes observed in the preceding section. Additionally, the water PMF barriers in our functionalized graphene pores are lower than that for pristine

graphene pores with the diameter range of 7.5-10.5Å[75]. This implies that functionalized or modified graphene membranes could improve water permeation.

In some PMF profiles, the existence of local minimum in the position of pore center suggests that water molecules favorably reside there[75] and this free energy well might, to some extent, reduce the molecular passing mobility[51]. Comparatively, the pore center of N-graphene membrane has the least probability for water to reside. This result is qualitatively in agreement with the 2-D density maps (Fig. 4) and the residence time distributions (Fig. S3). It is noteworthy that despite obvious higher water flux in the N-graphene membrane (see Fig. 2), as compared with other membranes, the difference among all the PMF barriers is not significant. This fact suggests that thermodynamics barrier is not the only factor determining the flow rate through the membrane pores. The pore area also has important effect on the flow. For instance, as shown in Fig. 4, the broadening cross-section area in the N-graphene pore can promote water passage. Hence, for the five functionalized graphene membranes, a change in the N-doping level might be effective in modifying the water flow rate.

![](./images/814599190146449408_6.jpg)

Fig. 5 Potential of mean force profiles along the direction perpendicular to the functionalized graphene sheets for water molecule (left) and ions (right). Five functionalized graphene membranes from top to bottom: N-graphene, NH-graphene, NH3-graphene, NOH-graphene, and H-graphene, respectively.

In Fig. 5, the water PMF profiles are not in mirror symmetry with the corresponding density profiles. This behavior is similar with the result reported earlier[75]. To further understand the energy barrier in more detail, we decomposed the PMFs into the interacting contributions from the solution medium and the graphene pores, respectively.

Fig. 5 shows the interaction force from the membranes offers an attractive action to drag water into the pores. Among them, the NOH-graphene membrane provides the strongest attractive force. However, the interaction arising from the solution environment usually plays repellence to the water permeation, which is in line with the previous results[7,74] that the solvation force has an impeding role to water passing through CNT pores.

A further split (see Fig. S6) of the solution PMF term shows that both solvent and ions provide resistance contributions. For the five graphene pores, there is no obvious difference in the solvent contribution terms, and the relatively large solvent contribution in the N-graphene membrane is probably associated with its bigger pore size, which could induce stronger solvation force[7]. Moreover, it is noted that, in the NOH-graphene and H-graphene membranes with smaller pore size, the ion contribution becomes more significant. This behavior can be explained as the enlarged ion accumulation near the two membrane pores (Fig. S5). This further confirms the fact that concentration polarization of surface ions can decrease water flow rate.

To explore the underlying mechanism of ion rejection for the five functionalized graphene membranes, we calculated the PMF profiles for ions ($\text{Na}^+$ and $\text{Cl}^-$) transferring through the membrane pores. As shown in Fig. 5, the energy barriers of $\text{Na}^+$ are in the range of 3.7-11.0 kcal/mol, and those for $\text{Cl}^-$ are generally above 15 kcal/mol. Although there is relatively low PMF barrier for $\text{Na}^+$ ion through the N-graphene membrane, these ion PMF barriers are obviously higher than those using the nanoporous graphene functionalized with $\text{COO}^-$, $\text{NH}_3^+$ and OH groups[75]. From the ion PMF profiles, the $\text{Na}^+$ usually feels the repulsive action earlier than $\text{Cl}^-$ when approaching the pores. Possible reason for this is the different resisting forces from interfacial layers between $\text{Na}^+$ and $\text{Cl}^-$. Furthermore, for the graphene membranes investigated in this work, the $\text{Na}^+/\text{Cl}^-$ ions generally face higher energy barrier upon passing through the pores, as compared with water. This result demonstrates that the N-functionalized graphenes can be effective for water desalination[73,75].

![](./images/814599190146449408_7.jpg)

Fig. 6 Comparison of distributions of hydration coordination numbers of Na⁺(a) and Cl⁻(b) ions in bulk phase and in graphene pores.

From the ion PMFs, both positive $Na^+$ and negative $Cl^-$ always feel repulsive action when traversing the membrane pores. This means that the electrostatic force is not dominant in the obstruction of ion passage. This behavior could be ascribed to the neutral feature of the functionalized groups. Additionally, the presence of the $Na^+/Cl^-$ layer in the interfacial region also screens the charged interaction[75]. It can be postulated that the steric hindrance effect on hydration ions, arising from the pores restriction, is possibly responsible for the free energy barriers of ion passage[75]. In order to realize this mechanism, we characterized average hydration number of ions, which was calculated by counting the number of water molecules in the first solvation shell of ions. As shown in Fig. 6, in bulk phase, there are ~5.0 and ~6.2 water molecules in the first hydration shell around $Na^+$ and $Cl^-$ ions, respectively, consistent with the reference results[76,77].

However, the substantial decrease in the solvent coordination numbers, within the membrane pores, means ions have to remove some of the hydration molecules, in order to pass through the membrane pores. This will make the ion translocation is energetically unfavorable, resulting in free energy barrier. In addition, it is noted that more water

molecules will be peeled off for $Cl^-$ ion, comparing to $Na^+$ ion. This is in line with the larger free energy barrier of $Cl^-$ ion observed in the PMF profiles (Fig. 5). For the N-graphene membrane pore, less water molecules are peeled off, corresponding to relatively lower energetic barrier.

![](./images/814599190146449408_8.jpg)

Fig. 7 Pore electron density isosurfaces of Hydrated $Na^+$ (a) and $Cl^-$ (b) ions, as well as (c) five functionalized graphene membranes (isovalue of $0.02e/\mathring{A}^3$). These functionalized graphene membranes from left to right are: N-graphene, NH-graphene, NH3-graphene, H-graphene, and NOH-graphene, respectively. Blue and red indicate regions with the highest and lowest probability of electron density, respectively. Gray balls indicate the inscribed circles of the graphene pores and the numbers are the corresponding diameters, which represent the effective diameters of pore.

The pore resistance for the hydration ions can be further supported by the quantum mechanics DFT computation, wherein the electron density isosurfaces for the hydrated ions ($Na^+$ and $Cl^-$) and the five functionalized graphene pores were shown in Fig. 7. On the basis of the electron density distribution, the effective pore size is defined as the smallest inner distance within the pore. The pore functionalization reduces the effective size of pore. It is observed that all the effective pore sizes of the functionalized graphene membranes are noticeably smaller than the effective diameters of hydrated ions. The hydrated ions will form clear electron overlap with the graphene pores, once they approach and pass through the pore. This electron overlap yields energetic loss. In particular, for the NOH-graphene membrane, the least pore radius will produce an

enhanced electron overlapping degree, thereby leading to the largest ion rejection.

Moreover, from Fig. 7, we observe that the effective diameter of hydrated $Cl^-$ is clearly larger than that of hydrated $Na^+$, agreeing with higher rejection for $Cl^-$ ion.

In this work, although high pressure was applied in the non-equilibrium MD simulation, this does not mean actual operation of membrane separation must run in high-pressure conditions. The obtained water permeability is based on the unit pressure (one MPa), which is comparable to the actual operation pressure. Recent study [78] has shown that nanoporous graphene is able to withstand the higher hydraulic pressure in actual desalination operation. Following this reference result, we conducted the analysis of mechanical stability (for detail, see the supplementary material), and found that the stress of our N-functionalized graphene membranes is obviously lower than the corresponding fracture stress, confirming that the graphene membranes in this work possess higher mechanical stability.

Our simulation demonstrates that pyridinic-like nitrogen doped graphenes have a potential as high-efficient desalination membranes. However, it should be emphasized that application of graphene membrane in industrialization and commercialization is still far being realized. Currently, the practical realization is impeded by several technical limitations in the membrane preparation [79,80]: firstly, the scaling up of graphene production with larger membrane area remains a significant challenge, secondly, accurate control over the size of the graphene nanopores without defect is difficult. Much effort needs to be paid in order to reduce these limitations. It is highly speculated that the practical nanoporous graphene could become a reality with the advance of modern

experimental technology.

Conclusions:

In this work, the desalination performances have been simulated for monolayer graphene nanopores with pyridinic N doped functionalization under various N-dopping levels. Our simulation results demonstrate that all N-doped graphene membranes in our work exhibit higher water flux with several orders of magnitude higher than polymeric RO membranes. Meanwhile, all functionalized graphene membranes show better salt rejection. Especially, the NOH graphene membrane with partial hydroxyl group inclusion has complete (100%) salt rejection. However, the N-graphene membrane with complete N-doping shows relatively lower salt rejection due to larger pore size. On the whole, the pyridinic nanoporous graphene with partial N-doping has excellent desalination performance.

We further simulated the PMF profiles for water and ions passing through the graphene pores. The moderate free energy barrier for water and larger free energy barrier for ions provide direct thermodynamics support that the pyridinic N doped graphenes can be effective as desalination RO membrane. The interfacial behavior near the membrane pores suggests various water fluxes among the functionalized graphene membranes are highly associated with different pore sizes. Various interfacial forces were characterized to clarify the molecular origin of water permeation and salt rejection. The ion rejection in the graphene membranes can be explained as the pore dehydration mechanism. Quantum mechanism computation also confirms this size exclusion of hydration ions in the pore. At present, although experimental realization of the graphene-based desalination process

still remains huge challenge, our simulation results provide the potential of pyridinic N doped graphene nanopores as desalination membrane. This simulation result is helpful in designing new type graphene-based nanostructured membranes.

## Acknowledgements:
This work was supported by the National Natural Science Foundation of China under Grants 21376116, 973-National Basic research Program of China (2015CB655301), Research funding from State Key Laboratory of Materials-Oriented Chemical Engineering (ZK201404), and A PAPD Project of Jiangsu Higher Education Institution.

## Appendix A. Supporting information:
Supplementary material associated with this article can be found in the online version.

## References:
[1] R.F. Service. Desalination Freshens Up, Science 313 (2006) 1088-1090.

[2] M.A. Shannon, P.W. Bohn, M. Elimelech, J.G. Georgiadis, B.J. Marinas, A.M. Mayes. Science and technology for water purification in the coming decades, Nature 452 (2008) 301-310.

[3] T. Humplik, J. Lee, S.C. O'Hern, B.A. Fellman, M.A. Baig, S.F. Hassan, M.A. Atieh, F. Rahman, T. Laoui, R. Karnik, E.N. Wang. Nanostructured materials for water desalination, Nanotechnology 22 (2011) 292001.

[4] Y. Liu, X. Chen. High permeability and salt rejection reverse osmosis by a zeolite nano-membrane, Physical chemistry chemical physics : PCCP 15 (2013) 6817-6824.

[5] Z. Hu, Y. Chen, J. Jiang. Zeolitic imidazolate framework-8 as a reverse osmosis membrane for water desalination: insight from molecular simulation, J Chem Phys 134 (2011) 134705.

[6] L. Wang, R.S. Dumont, J.M. Dickson. Nonequilibrium molecular dynamics simulation of water transport through carbon nanotube membranes at low pressure, J Chem Phys 137 (2012) 044102.

[7] B. Corry. Designing Carbon Nanotube Membranes for Efficient Water Desalination, J. Phys. Chem. B 112 (2008) 1427-1434.

[8] L. Zhao, Y. Zhao, R. Zhou. Novel Design of a Nanoflowmeter Based on Carbon Nanotubes, The Journal of Physical Chemistry C 116 (2012) 13429-13434.

[9] K.P. Lee, T.C. Arnot, D. Mattia. A review of reverse osmosis membrane materials for desalination—Development to date and future potential, Journal of Membrane Science 370 (2011) 1-22.

[10] S. Kar, R.C. Bindal, P.K. Tewari. Carbon nanotube membranes for desalination and water purification: Challenges and opportunities, Nano Today 7 (2012) 385-389.

[11] A.K. Geim. Graphene: Status and Prospects, Science 324 (2009) 1530-1534.

[12] S. Stankovich, D.A. Dikin, G.H. Dommett, K.M. Kohlhaas, E.J. Zimney, E.A. Stach, R.D. Piner, S.T. Nguyen, R.S. Ruoff. Graphene-based composite materials, Nature 442 (2006) 282-286.

[13] M.J. Allen, V.C. Tung, R.B. Kaner. Honeycomb Carbon: A Review of Graphene, Chem. Rev. , , 132-145 110 (2010) 132-145.

[14] C. Lee, X. Wei, J.W. Kysar, J. Hone. Measurement of the Elastic Properties and Intrinsic Strength of Monolayer Graphene, Science 321 (2008) 385-388.

[15] M.E. Suk, N.R. Aluru. Water Transport through Ultrathin Graphene, J. Phys. Chem. Lett 1 (2010) 1590-1594.

[16] G. Hu, M. Mao, S. Ghosal. Ion transport through a graphene nanopore, Nanotechnology 23 (2012) 395501.

[17] ZhengYan, J. Lin, Z. Peng, Z. Sun, YuZhu, L. Li, C. Xiang, E.L.c. Samue, C. Kittrell, J.M. Tour. Toward the Synthesis of Wafer-Scale Single-Crystal Graphene on Copper Foils, Acs nano 6 (2012) 9110-9117.

[18] J.S. Bunch, S.S. Verbridge, J.S. Alden, A.M.v.d. Zande, J.M. Parpia, H.G. Craighead, P.L. McEuen. Impermeable Atomic Membranes from Graphene Sheets, Nano Letters 8 (2008) 2458-2462.

[19] C.A. Merchant, K. Healy, M. Wanunu, V. Ray, N. Peterman, J. Bartel, M.D. Fischbein, K. Venta, Z. Luo, A.T. Johnson, M. Drndic. DNA translocation through graphene nanopores, Nano Letters 10 (2010) 2915-2921.

[20] M. Bieri, M. Treier, J. Cai, K. Ait-Mansour, P. Ruffieux, O. Groning, P. Groning, M. Kastler, R. Rieger, X. Feng, K. Mullen, R. Fasel. Porous graphenes: two-dimensional polymer synthesis with atomic precision, Chemical communications (2009) 6919-6921.

[21] M. Kim, N.S. Safron, E. Han, M.S. Arnold, P. Gopalan. Fabrication and characterization of large-area, semiconducting nanopatterned graphene materials, Nano Letters 10 (2010) 1125-1131.

[22] D.C. Bell, M.C. Lemme, L.A. Stern, J.R. Williams, C.M. Marcus. Precision cutting and patterning of graphene with helium ions, Nanotechnology 20 (2009) 455301.

[23] D. E. Jiang, V.R. Cooper, S. Dai. Porous Graphene as the Ultimate Membrane for Gas Separation, Nano Letters 9 (2009) 4019-4024.

[24] S.P. Surwade, G.M. Veith, S. Dai1, SergeiN.Smirnov, I. V.Vlassiouk3, R.R. Unocic, S.M. Mahurin. Water desalination using nanoporous single-layer graphene, Nature nanotechnology 10 (2015) 459.

[25] G. Luo, L. Liu, J. Zhang, G. Li, B. Wang, J. Zhao. Hole defects and nitrogen doping in graphene: implication for supercapacitor applications, ACS applied materials & interfaces 5 (2013) 11184-11193.

[26] X. Zhang, J. Xin, F. Ding. The edges of graphene, Nanoscale 5 (2013) 2556-2569.

[27] T. Wu, Q. Xue, C. Ling, M. Shan, Z. Liu, Y. Tao, X. Li. Fluorine-Modified Porous Graphene as Membrane for CO2/N2Separation: Molecular Dynamic and First-Principles Simulations, The Journal of Physical Chemistry C 118 (2014) 7369-7376.

[28] M. Shan, Q. Xue, N. Jing, C. Ling, T. Zhang, Z. Yan, J. Zheng. Influence of chemical functionalization on the CO(2)/N(2) separation performance of porous graphene membranes, Nanoscale 4 (2012) 5477-5482.

[29] D. Cohen-Tanugi, J.C. Grossman. Water desalination across nanoporous graphene, Nano Letters 12 (2012) 3602-3608.

[30] Y. Wang, Y. Shao, D.W. Matson, J. Li, Y. Lin. Nitrogen-Doped Graphene and Its Application in Electrochemical Biosensing, Acs nano 4 (2010) 1790-1798.

[31] H. Wang, T. Maiyalagan, X. Wang. Review on Recent Progress in Nitrogen-Doped Graphene: Synthesis, Characterization, and Its Potential Applications, ACS Catalysis 2 (2012) 781-794.

[32] H.-L. Guo, S. Peng, J.-H. Xu, Y.-Q. Zhao, X. Kang. Highly stable pyridinic nitrogen doped graphene modified electrode in simultaneous determination of hydroquinone and catechol, Sensors and Actuators B: Chemical 193 (2014) 623-629.

[33] M. Scardamaglia, C. Struzzi, F.J. Aparicio Rebollo, P. De Marco, P.R. Mudimela, J.-F. Colomer, M. Amati, L. Gregoratti, L. Petaccia, R. Snyders, C. Bittencourt. Tuning electronic properties of carbon nanotubes by nitrogen grafting: Chemistry and chemical stability, Carbon 83 (2015) 118-127.

[34] Z. Jin, J. Yao, C. Kittrell, J.M. Tour. Large-Scale Growth and Characterizations of Nitrogen-Doped Monolayer Graphene Sheets, Acs nano 5 (2011) 4112-4117.

[35] L.S. Panchakarla, K.S. Subrahmanyam, S.K. Saha, A. Govindaraj, H.R. Krishnamurthy, U.V. Waghmare, C.N.R. Rao. Synthesis, Structure, and Properties of Boron- and Nitrogen-Doped Graphene, Advanced Materials (2009) NA-NA.

[36] X. Li, H. Wang, J.T. Robinson, H. Sanchez, G. Diankov, H. Dai. Simultaneous Nitrogen Doping and Reduction of Graphene Oxide, J. AM. CHEM. SOC 131 (2009) 15939-15944.

[37] X. Wang, X. Li, L. Zhang, Y. Yoon, P.K. Weber, H. Wang, J. Guo, H. Dai. N-Doping of Graphene Through Electrothermal Reactions with Ammonia, Science 324 (2009) 768-771.

[38] H.M. Jeong, J.W. Lee, W.H. Shin, Y.J. Choi, H.J. Shin, J.K. Kang, J.W. Choi. Nitrogen-doped graphene for high-performance ultracapacitors and the importance of nitrogen-doped sites at basal planes, Nano Letters 11 (2011) 2472-2477.

[39] L. Sun, L. Wang, C. Tian, T. Tan, Y. Xie, K. Shi, M. Li, H. Fu. Nitrogen-doped graphene with high nitrogen level via a one-step hydrothermal reaction of graphene oxide with urea for superior capacitive energy storage, RSC Advances 2 (2012) 4498.

[40] Z. Luo, S. Lim, Z. Tian, J. Shang, L. Lai, B. MacDonald, C. Fu, Z. Shen, T. Yu, J. Lin. Pyridinic N doped graphene: synthesis, electronic structure, and electrocatalytic property, Journal of Materials Chemistry 21 (2011) 8038.

[41] A.W. Hauser, J. Schrier, P. Schwerdtfeger. Helium Tunneling through Nitrogen-Functionalized Graphene Pores: Pressure- and Temperature-Driven Approaches to Isotope Separation, The Journal of Physical Chemistry C 116 (2012) 10819-10827.

[42] W.D. Cornell, P. Cieplak, C.I. Bayly, I.R. Gould, J. Kenneth M. Merz, D.M. Ferguson, D.C. Spellmeyer, T. Fox, J.W. Caldwell, P.A. Kollman. A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules, J. Am. Chem. SOC 117 (1995) 5179-5197.

[43] J.-X. Shi, T. Natsuki, X.-W. Lei, Q.-Q. Ni. Equivalent Young's modulus and thickness of graphene sheets for the continuum mechanical models, Applied Physics Letters 104 (2014) 223101.

[44] W.L. Jorgensen, D.S. Maxwell, J. Tirado-Rives. Development and Testing of the OPLS All-Atom Force Field on Conformational Energetics and Properties of Organic Liquids, J. Am. Chem. Soc 118 (1996) 11225-11236.

[45] H.J.C. Berendsen, J.R. Grigera, T.P. Straatsma. The Missing Term in Effective Pair Potentials, J. Phys. Chem 91 (1987) 6269-6271.

[46] L.X. Dang. Mechanism and Thermodynamics of Ion Selectivity in Aqueous Solutions of 18-Crown-6 Ether: A Molecular Dynamics Study, J. Am. Chem. SOC 117 (1995) 6954-6960.

[47] D.E. Smith, L.X. Dang. Computer simulations of NaCl association in polarizable water, The

[66] D. Cohen-Tanugi, J.C. Grossman. Water permeability of nanoporous graphene at realistic pressures for reverse osmosis desalination, J Chem Phys 141 (2014) 074704.

[67] J. Su, H. Guo. Effect of nanochannel dimension on the transport of water molecules, The journal of physical chemistry. B 116 (2012) 5925-5932.

[68] T.A. Hilder, D. Gordon, S.H. Chung. Salt rejection and water transport through boron nitride nanotubes, Small 5 (2009) 2183-2190.

[69] C. Zhu, H. Li, X.C. Zeng, E.G. Wang, S. Meng. Quantized water transport: ideal desalination through graphyne-4 membrane, Scientific reports 3 (2013) 3163.

[70] K. Zhao, H. Wu. Size effects of pore density and solute size on water osmosis through nanoporous membrane, The journal of physical chemistry. B 116 (2012) 13459-13466.

[71] T. Shintani, A. Shimazu, S. Yahagi, H. Matsuyama. Characterization of methyl-substituted polyamides used for reverse osmosis membranes by positron annihilation lifetime spectroscopy and MD simulation, Journal of Applied Polymer Science 113 (2009) 1757-1762.

[72] J. Azamat, A. Khataee, S.W. Joo. Functionalized graphene as a nanostructured membrane for removal of copper and mercury from aqueous solution: A molecular dynamics simulation study, Journal of Molecular Graphics and Modelling 53 (2014) 112-117.

[73] M. Xue, H. Qiu, W. Guo. Exceptionally fast water desalination at complete salt rejection by pristine graphyne monolayers, Nanotechnology 24 (2013) 505720.

[74] C.Y. Won, S. Joseph, N.R. Aluru. Effect of quantum partial charges on the structure and dynamics of water in single-walled carbon nanotubes, J Chem Phys 125 (2006) 114701.

[75] D. Konatham, J. Yu, T.A. Ho, A. Striolo. Simulation insights for graphene-based water desalination membranes, Langmuir : the ACS journal of surfaces and colloids 29 (2013) 11884-11897.

[76] A. Bankura, V. Carnevale, M.L. Klein. Hydration structure of salt solutions from ab initio molecular dynamics, J Chem Phys 138 (2013) 014501.

[77] M. Druchok, M. Holovko. Molecular dynamics study of ion hydration under pressure, Journal of Molecular Liquids 159 (2011) 24-30.

[78] D. Cohen-Tanugi, J. C. Grossman, Mechanical Strength of Nanoporous graphene as a Desalination Membrane, Nano Letters 14 (2014) 6171-6178.

[79] D. Wei, J. Kivioja. Graphene for energy solutions and its industrialization, Nanoscale 5 (2013) 10108-10126.

[80] S.C. O'Hern, D. Jang, S. Bose, J.-C. Idrobo, Y. Song, T. Laoui, J. Kong, R. Karnik. Nanofiltration across Defect-Sealed Nanoporous Monolayer Graphene, Nano Letters 15 (2015) 3254-2360.

**Highlights:**

- we computationally demonstrate that the Pyridinic N doped graphenes have excellent desalination performance;

- The dynamics process and thermodynamics mechanism for the desalination process have been revealed;

- It was revealed that the salt rejection for the functionalized graphenes is the pore size exclusion of hydrated ions

# Graphical abstract

![](./images/814599190146449408_9.jpg)

The dynamics process and thermodynamics mechanisms for desalination process using the pyridinic-like N doped porous graphene have been computationally demonstrated.

![](./images/814599190146449408_10.jpg)

Fig. 1 (Top panel) Lateral view of the simulation system, showing a functionalized graphene membrane placed in the center of the box and two chambers on the both sides of the functionalized graphene. The right chamber contained NaCl solution, while the left chamber was pure water. (bottom panels) Top view of five functionalized graphene membranes. Carbon atoms in functionalized graphenes are shown as cyan spheres, nitrogen in blue, hydrogen in white, oxygen in red, $Na^{+}$ in green, and $Cl^{-}$ in purple. The pore diameters (red line) in the graphene membranes were defined as the diameter of a gray ball fitting the pores.

![](./images/814599190146449408_11.jpg)

Fig. 2 Number of net transferred water molecules as a function of time for (a) N-grahpene and (b) H-graphene. (c) Water flux across five functionalized graphene membranes as a function of the external pressure. The arrow in Fig. 2(a) indicates decrease of pressure from upper to down.

![](./images/814599190146449408_12.jpg)

Fig. 3 Salt rejections for five functionalized graphene membranes vs the external pressure. The insert shows comparison of water permeability among functionalized graphene membranes.

![](./images/814599190146449408_13.jpg)

Fig. 4 Five functionalized graphenes, from top to bottom, are N-graphene, NH-graphene, NH3-graphene, NOH-graphene and H-graphene, respectively. (left panel) relative density distribution of water along z axis for five functionalized graphene membranes, Herein, $\rho_o$ is the bulk water density ($\sim$0.0031 $\text{\AA}^{-3}$), and the inserts signify that the time dependence of occupying number ($N_{oc}$) of water molecules within pore for graphene membrane. 2-D distribution maps for oxygen (middle panel) and hydrogen (right panel) atoms in water in the pore regions for different functionalized graphene. Light blue and red indicate regions with the lowest and highest probability of finding an oxygen or hydrogen atoms, respectively.

![](./images/814599190146449408_14.jpg)

Fig. 5 Potential of mean force profiles along the direction perpendicular to the functionalized graphene sheets for water molecule (left) and ions (right). Five functionalized graphene membranes from top to bottom: N-graphene, NH-graphene, NH3-graphene, NOH-graphene, and H-graphene, respectively.

![](./images/814599190146449408_15.jpg)

Fig. 6 Comparison of distributions of hydration coordination numbers of $Na^{+}(a)$ and $Cl^{-}(b)$ ions in bulk phase and in graphene pores.

![](./images/814599190146449408_16.jpg)

Fig. 7 Pore electron density isosurfaces of Hydrated $Na^{+}$ (a) and $Cl^{-}$ (b) ions, as well as (c) five functionalized graphene membranes (isovalue of $0.02e/\AA^{3}$). These functionalized graphene membranes from left to right are: N-graphene, NH-graphene, NH3-graphene, H-graphene, and NOH-graphene, respectively. blue and red indicate regions with the highest and lowest probability of electron density, respectively. Gray balls indicate the inscribed circles of the graphene pores and the numbers are the corresponding diameters, which represent the effective diameters of pore.