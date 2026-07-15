Molecular dynamics simulation study on the hydrogen adsorption and diffusion in non-interpenetrating and interpenetrating IRMOFs

Tae Bum Lee $^{\text{a}}$, Dong Hyun Jung $^{\text{a}}$, Daejin Kim $^{\text{a}}$, Jaheon Kim $^{\text{b}}$, Kihang Choi $^{\text{c}}$, Seung-Hoon Choi $^{\text{a,*}}$

$^{\text{a}}$Insilicotech Co. Ltd., A-1101 Kolontripolis, Seumgok-Dong, Bundang-Gu, Seongnam 463-943, Republic of Korea
$^{\text{b}}$Department of Chemistry, Soongsil University, Seoul 156-743, Republic of Korea
$^{\text{c}}$Department of Chemistry, Korea University, Seoul 136-701, Republic of Korea

---

### ARTICLE INFO

**Article history:**
Available online 17 January 2009

**Keywords:**
Hydrogen
Metal-organic framework
Micro-porous
Interpenetration
Molecular dynamics simulation

---

### ABSTRACT

We performed molecular dynamics simulations at 77 K on the non-interpenetrating isoreticular (having the same underlying topology) metal-organic frameworks (IRMOFs) and the interpenetrating IRMOFs to investigate the adsorption behavior of hydrogen on the surface of MOFs, catenation effect on the density of adsorbed hydrogen, and dynamic behavior of adsorbed hydrogen molecules. We tested two classical force fields, universal force field (UFF) and DREIDING force field for the simulations and found out that the UFF describes the adsorption of hydrogen more reliably than DREIDING force field. The simulations showed the density values of adsorbed hydrogen in the small pores of the interpenetrating IRMOFs are higher than those in the larger pores of the non-interpenetrating IRMOFs, and the diffusion of the hydrogen molecules in the interpenetrating IRMOFs is highly restricted compared to the non-interpenetrating IRMOFs. From the simulation results, we concluded that the small pores created by the catenation might contribute the increase of the adsorption capacity of the interpenetrating IRMOFs.

© 2008 Elsevier B.V. All rights reserved.

---

### 1. Introduction

Many researchers have researched metal-organic frameworks for their application to hydrogen storage and to date, the best experimental storage capacities at high pressure are reported as 7.5 wt% at 77 K [1] and 1.4 wt% at 298 K [2] among the selected 51 MOFs [3]. These material-based storage amounts are still far below the DOE target by the year 2010 which is 6.0 wt% based on the on-board system at operating ambient temperature ($10 \pm 40\ ^{\circ}\text{C}$) and under 100 atm [4]. The reason for the low hydrogen uptake by MOFs is that their adsorption enthalpy is mostly less than 10 kJ/mol [3]. To increase the capacity, various strategies have been suggested based on the experimental results [5]. Some supporting results were achieved by a utilization of the unsaturated metal sites by suitable activation processes [6], by making MOFs to have wavy channels with small openings [7], by an introduction of electron-donating functional groups to organic ligands [8,9], and by both efficient surface areas and pore volumes from the framework interpenetration of MOFs [9–11]. Fortunately MOFs can be prepared with various types and sizes of the pores by assembling various metal ions and organic linkers, and their syntheses in large scale became possible [12], so the key issue is to find a way to increase the interaction energy between hydrogen molecule and framework.

At the same time, to understand the adsorption phenomena at the atomic level the adsorption mechanism of the hydrogen molecules onto MOFs (especially MOF-5) has been investigated by theoretical calculations [13–19], powder X-ray diffraction, and neutron powder diffraction experiments [20]. Some of these studies also indicated the locations of the important hydrogen adsorption sites in the framework of MOF-5. In addition, a quantitative structure–property relationship (QSPR) method [21] has been applied to show that the electron delocalization and polarization of the organic linkers are associated with the hydrogen uptake capacity by analyzing various kinds of MOFs.

Among the structural features related to the hydrogen adsorption capacity, the framework interpenetration of MOFs is noticeable because the phenomenon is frequently observed with a variety of structural and functional types in MOFs [22]. The strategy based on the experimental observations may be summarized as that many small pores created by catenation might be related with the increased capacity of MOFs. As it is, the framework interpenetration is a generally applicable approach from the perspective of hydrogen storage applications supported by some represented examples. However, this proposal needs more thorough experimental investigation and their analyses that require the chemical syntheses of a series of the well-defined systems, that is, isoreticular (having the

---

* Corresponding author. Tel.: +82 31 728 0441; fax: +82 31 728 0444.
E-mail address: shchoi@insilicotech.co.kr (S.-H. Choi).

0920-5861/$ – see front matter © 2008 Elsevier B.V. All rights reserved.
doi:10.1016/j.cattod.2008.12.011

![](./images/811874379326554112_1.jpg)
![](./images/811874379326554112_2.jpg)

same underlying topology) non-interpenetrating and interpenetrating MOFs.

Isoreticular MOFs (IRMOFs) have the general formula $Zn_4OL_3$ (where L is a linear aromatic dicarboxylate) [23], and provide a good model system for experimental and theoretical adsorption analyses on the catenation effect due to their well-defined structures of both single- and doubly interpenetrating frameworks. Although the theoretical approach or modeling studies can provide the pertinent model systems, many research groups have not yet seriously studied the catenation effect. Recently, Frost et al. have extensively discussed hydrogen adsorption behaviors and isotherms of a series of 10 IRMOFs by using the grand canonical Monte Carlo (GCMC) simulations, but the interpenetrating MOFs were not included in that study [24]. A few reports on this issue include the GCMC simulations on a series of 6 IRMOFs including 3 interpenetrating MOFs, which has been carried out by us [16] and molecular dynamics (MD) simulations on hydrogen diffusion in interpenetrated MOFs by Liu and coworkers [25]. It has been elucidated in the GCMC simulations that new adsorption sites can be generated in the interpenetrating MOF compared to its non-interpenetrating one. The simulation results could also describe hydrogen adsorption behavior; the hydrogen molecules tend to form more dense packing in the small pores generated by catenation, so that the interpenetrating IRMOFs are anticipated to store more hydrogen molecules per unit volume than single framework IRMOFs. These preliminary results were coincident with the proposal suggested by Yaghi and coworkers [10]. Liu et al. emphasize in their paper that the diffusion behavior of adsorbed hydrogen molecules are influenced by the small pores in the catenated MOF chains. However, they did not give the detailed information about the relationships between the volume of each pore in the MOF structures and density of adsorbed hydrogen.

In this report, we describe simulations of the adsorption and diffusion behaviors of hydrogen molecules within 7 IRMOFs using Monte Carlo (MC) simulation and molecular dynamics methods, respectively. To examine the effects of interpenetration systematically and in more detail, we have studied quantitative distribution of hydrogen adsorbates in various types of pores generated by the interpenetration, which have not been previously described.

## 2. Simulation models and methods

### 2.1. Framework structures

Model systems used in this work consist of two groups of MOFs: non-interpenetrating IRMOFs (IRMOF-10, IRMOF-12, and IRMOF-14) and their interpenetrating counter parts (IRMOF-9, IRMOF-11, and IRMOF-13) [23]. In addition, IRMOF-1 was used as a reference system. The framework formula is $Zn_4OL_3$, and the pairs of non-interpenetrating/interpenetrating IRMOFs (IRMOF-9/-10, IRMOF-11/-12, and IRMOF-13/-14) have biphenyl-4,4'-dicarboxylate, 4,5,9,10-tetrahydropyrene-2,7-dicarboxylate, and pyrene-2,7-dicarboxylate as Ls, their organic linkers, respectively. In a framework, four Zn atoms are tetrahedrally arranged around the central oxo ion, and each organic linker is binding two Zn atoms via bi-monodentate fashion to give a simple cubic net. As there is a sufficient space, the second framework can be accommodated into the pore of the existing one to produce the catenation.

In the IRMOF-9, -11, and -13, two $Zn_4O$ moieties from two independent frameworks are close to each other while IRMOF-16 having a much longer organic link, terphenyl-4,4'-dicarboxylate has a maximal separation of two frameworks. Due to these structural differences between the IRMOF-16 and other IRMOF pairs, they, IRMOF-16 and its pair IRMOF-15 have been excluded in the model systems in this work. Furthermore, the severe statistical disorders are present in the frameworks of IRMOF-15 and -16 need more elaboration in building model configurations for the simulation studies.

The model structures of the IRMOFs were adapted from the single crystal or powder X-ray diffraction data [23]. Due to the orthorhombic or trigonal space group of interpenetrating IRMOFs, we transformed the space group symmetries to a more reduced system, triclinic P1, and the all structural disorders were cleaned up and non-framework disordered moieties were removed. Therefore, our model systems had 8 zinc oxo units for non-interpenetrating MOFs and 16 zinc oxo units for interpenetrating MOFs with same cubic type lattice.

### 2.2. Definition of pore types by partitioning pores

Before the simulation studies to examine the catenation effects, it was prerequisite to identify and designate the various pore types in the lattice that were defined as segmental zones based on their location, shape and size in the frameworks. In the case of the non-interpenetrating IRMOFs, 4 larger (A pore) and 4 smaller (B pore) pores per unit cell have been identified as described in Fig. 1. The A pore is surrounded by 12 outward oriented organic linkers, while the B pore is enclosed by 12 inward oriented organic linkers. As these two kinds of cubic pores are surrounding each other and located alternatively throughout the space, the same organic linker acts as both inward and outward directing partitions for B and A pores, respectively. This type of partition is also applied to IRMOF-10, -12, and -14.

When the frameworks are interpenetrating as in IRMOF-9, -11, and 13, the situation becomes rather complex. Unlike the single framework case, very different pore types have been generated, and the resulting five types of pores in a unit cell were designated as $4A'$, $4B'$, $24C$, $8D$ and $24E$ pores (Fig. 2). The centers of $A'$ and $B'$ pores are located at the same sites as those of A and B pores, respectively, but their pore sizes are much reduced. In addition, half the organic linkers defining each pore are originated from two independent frameworks. Besides the specific differences, the cubic arrangement patterns of the surrounding organic linkers in $A'$ and $B'$ pores are almost the same as those in A and B pores. Closely

![](./images/811874379326554112_3.jpg)

Fig. 1. Model structure of IRMOF-14 is shown as stick models where Zn atoms are drawn as tetrahedra, and hydrogen atoms are deleted for simplicity. The pores are also schematically represented as colored letters; larger pores (A) are designated by red, and smaller pores (B) are by yellow, respectively. Yellow colored moieties in the organic linkers are directing to the center of the B pores, and red colored ones are toward the outward direction of A pores. In this figure, a half unit cell of the IRMOF-14 has been shown, and thus, additional 2 A and 2 B pores are present alternatively on or below the current pores. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

![](./images/811874379326554112_4.jpg)

Fig. 2. Model structure of IRMOF-13 is shown with the pore designations as colored letters; A' pores, red; B' pores, yellow; C pores, purple; D pores, black; E pores, green. Other color codes of the framework atoms are same as those in Fig. 1. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

located organic linkers and Zn₄O moieties, respectively define the next two pores, C and D pores. C pores are defined as the space between two parallel organic linkers that are provided by different single frameworks. The aromatic planes of the organic linkers are facing each other, and slanting in opposite directions. The C pore includes the region of which chemical environment is similar to the portion of the terminal carboxylates in the organic linker of IRMOF-1. This has been indicated as the one of the primary hydrogen adsorption sites in the previous researches [10–17]. The D pore is present between two adjacent and facing Zn₄O moieties, which are imbedded in the different frameworks, respectively. It is more or less cavity-like because two corners of the cubic frameworks have made up its space. Similar to C pore, D pore is close to the known hydrogen adsorption site [10–17]. Unlike the A and B pores in the non-interpenetrating frameworks, A' and B' pores are not directly neighboring to each other, and can be interconnected by the narrow but wide space, E pore. All of the pores defined above are interconnected with each other, and A' and B' pores are surrounded by E, C, and D pores in the interpenetrating IRMOFs. The total available volume of each pore has been calculated and tabulated in Table 1. Among these various types of pores, D pore has the smallest available volume of 30–40 Å³ (Table 1). Because of this small size, D pore can hardly grasp one hydrogen molecule even if hydrogen is stored at its liquid density. Therefore, D pore has been ruled out for the further analysis.

### 2.3. Computational details

MC and MD simulations were performed using the Sorption and the Forcite program in the MS Modeling 4.0™ package [26], respectively. Both universal force field (UFF) [27] and DREIDING force field [28] were used for comparison of the results. The force field parameters of all the framework atoms and the hydrogen molecules were used as the values provided by the software. Further analysis of the framework charge has not been conducted, and the charge of the hydrogen atom was assigned to zero for our calculations.

<table>
<caption>Table 1<br>The available volume of pore in the non-interpenetrating and interpenetrating IRMOFs (Å³)ᵃ.</caption>
<thead>
<tr>
<th>Non-interpenetrating</th>
<th>IRMOF-1</th>
<th>IRMOF-10</th>
<th>IRMOF-12</th>
<th>IRMOF-14</th>
</tr>
</thead>
<tbody>
<tr>
<td>A pore</td>
<td>1894.74</td>
<td>4724.52</td>
<td>4722.52</td>
<td>4773.57</td>
</tr>
<tr>
<td>B pore</td>
<td>1516.48</td>
<td>4114.38</td>
<td>3887.62</td>
<td>3970.90</td>
</tr>
<tr>
<td>Total</td>
<td>13396.56</td>
<td>35010.87</td>
<td>33700.42</td>
<td>34655.84</td>
</tr>
<tr>
<td>Interpenetrating</td>
<td>IRMOF-9</td>
<td>IRMOF-11</td>
<td>IRMOF-13</td>
<td></td>
</tr>
<tr>
<td>A' pore</td>
<td>1453.59</td>
<td>1452.77</td>
<td>1454.52</td>
<td></td>
</tr>
<tr>
<td>B' pore</td>
<td>1300.74</td>
<td>1165.84</td>
<td>1197.88</td>
<td></td>
</tr>
<tr>
<td>C pore</td>
<td>138.85</td>
<td>114.01</td>
<td>120.45</td>
<td></td>
</tr>
<tr>
<td>D pore</td>
<td>45.90</td>
<td>45.54</td>
<td>46.36</td>
<td></td>
</tr>
<tr>
<td>E pore</td>
<td>552.07</td>
<td>504.17</td>
<td>511.07</td>
<td></td>
</tr>
<tr>
<td>Total</td>
<td>29748.96</td>
<td>27736.49</td>
<td>28291.73</td>
<td></td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">ᵃ Free volume calculation in MS Modeling 4.0 with 0.5 Å probe radius.</td>
</tr>
</tfoot>
</table>

In order to examine the distribution of hydrogen molecules in frameworks, MC simulations were performed using the fixed loading method. Each unit cell of IRMOF-1 was filled with 136 hydrogen molecules to make the system consistent with the model used in the ab initio molecular dynamics simulation study [14]. After the equilibration of 2 × 10⁶ steps, the product simulation of additional 2 × 10⁶ steps was conducted.

MD simulations of the hydrogen adsorption on IRMOF-1 were also performed using UFF and DREIDING force field, respectively. Before the MD computations, the evacuated IRMOF-1 framework was loaded with hydrogen molecules, and an energy minimization was performed with a cutoff radius of 9.5 Å. The applied minimization procedure was a smart algorithm that is a cascade of the steepest descent, conjugate gradient, and quasi-Newton methods. To generate the initial model with randomly distributed hydrogen molecules, the system was heated up to 600 K for 50 ps and quenched at 77 K for the following 50 ps. With these initial structures, 400 ps NVE dynamics was executed, and the data collected during the last 200 ps product simulation was used for the analysis of hydrogen adsorption behavior. Based on the results in IRMOF-1, the UFF was chosen as a suitable force field for further simulations for other IRMOFs. For the study of hydrogen adsorption, each IRMOF was filled with hydrogen molecules in the hydrogen content of 1.0, 2.0, 5.0 wt% and the equivalent for the liquid hydrogen density (0.09 g/cm³) based on the respective framework formula weight or the available volume in a whole unit cell, respectively. To calculate the number of hydrogen molecules required to fill IRMOFs at the liquid density, the total available volume of each MOF was divided by 47.48 Å³, the volume occupied by one hydrogen molecule in liquid phase [29].

The self-diffusivity, $D_s$ of hydrogen in IRMOFs were calculated by the Einstein relation,

$$
D_{\mathrm{s}}=\lim _{t \rightarrow \infty} \frac{1}{6t}\langle|\vec{r}(t)-\vec{r}(0)|^{2}\rangle \tag{1}
$$

where $\vec{r}(t)$ is the position of a particle at time $t$, and the angular brackets indicate an ensemble average [30].

![](./images/811874379326554112_5.jpg)

Fig. 3. Hydrogen density on a plane in IRMOF-1 calculated by GCMC at 77 K using (A) UFF and (B) DREIDING force field. The darker is the dot, the higher is the density, and the grey scale of the dot is the same in both cases (Zn, grey purple spheres; O, red spheres; C, grey spheres; H, white spheres). (C) The plane defined in the unit cell of IRMOF-1. The solid lines are benzene dicarboxylate linkers. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

## 3. Results and discussion

### 3.1. Selection of force fields

In order to select a suitable force field, simulation studies using both the UFF and DREIDING force fields were conducted for the hydrogen adsorption in IRMOF-1, and both results were examined. The hydrogen densities calculated from the MC simulations are displayed on a (1 1 0) plane of an IRMOF-1 unit cell as shown in Fig. 3.

The result from the UFF-based simulation (Fig. 3A) clearly indicates that hydrogen molecules are favorably adsorbed at the zinc oxo clusters and the organic linker sites, which is consistent with the first principle calculations by Mueller and Ceder [14]. On the other hand, the calculation using the DREIDING force field resulted that hydrogen molecules were almost evenly distributed over the pore space without showing particular adsorption sites (Fig. 3B). The molecular dynamics simulations calculated the interaction energy of hydrogen molecule with IRMOF-1 about 0.5 and 1 kcal/mol at the optimum adsorption distance by DREIDING force field and UFF, respectively. UFF also gives data that are more consistent with the value obtained from quantum mechanical calculations [13-16]. Based on the overall results UFF has been considered pertinent to describe hydrogen adsorption on IRMOFs, and further simulation studies were carried out using the force field for both non-interpenetrating and interpenetrating IRMOFs, respectively and stepwise. In fact, DREIDING force field was successfully used to model IRMOFs for adsorption simulations [24], but in their work they adapted the hydrogen molecule parameters fitted to experiments. Meanwhile, we used the parameters provided by DREIDING force field for hydrogen molecules as well as IRMOFs. Thus, this difference makes the inconsistency of the simulation results between Frost et al.'s work and ours.

### 3.2. Hydrogen adsorption on non-interpenetrating IRMOFs

The same molecular dynamics simulation procedures as that for IRMOF-1 were applied to other non-interpenetrating IRMOFs by dosing different hydrogen contents, and the calculated hydrogen densities were plotted as a function of the distances from framework components of the IRMOFs (Fig. 4). When the pore was filled with $1.0\ \text{H}_2$ wt%, the density showed a maximum peak around $3.1\ \text{\AA}$. The first peak at $3.1\ \text{\AA}$ is reasonably expectative because the distance is close to $3.055\ \text{\AA}$, a summation of van der Waals radii of $\text{H}_2$ ($1.479\ \text{\AA}$) and the average value ($1.576\ \text{\AA}$) of the other framework atoms', C ($1.70\ \text{\AA}$), H ($1.20\ \text{\AA}$), O ($1.52\ \text{\AA}$), and Zn ($1.39\ \text{\AA}$) [31].

The hydrogen adsorption capacity for each IRMOF has been examined to find delicate relationship between the adsorbed

![](./images/811874379326554112_6.jpg)

Fig. 4. The distance distribution between $\text{H}_2$ and pore surface in non-interpenetrating IRMOFs.

<table>
<caption>Table 2
The density of adsorbed hydrogen for each pore in the non-interpenetrating IRMOFs.</caption>
<thead>
<tr>
<th>MOFs</th>
<th>Pore</th>
<th colspan="4">Density of H₂ (1/Å³ × 10⁻²)</th>
</tr>
<tr>
<th></th>
<th></th>
<th>1 wt%</th>
<th>2 wt%</th>
<th>5 wt%</th>
<th>Liquid</th>
</tr>
</thead>
<tbody>
<tr>
<td>IRMOF-1</td>
<td>A</td>
<td>0.11</td>
<td>0.20</td>
<td>0.45</td>
<td>0.68</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>0.10</td>
<td>0.22</td>
<td>0.63</td>
<td>1.22</td>
</tr>
<tr>
<td></td>
<td>Total</td>
<td>0.11</td>
<td>0.21</td>
<td>0.54</td>
<td>0.94</td>
</tr>
<tr>
<td>IRMOF-10</td>
<td>A</td>
<td>0.04</td>
<td>0.08</td>
<td>0.23</td>
<td>0.71</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>0.07</td>
<td>0.12</td>
<td>0.26</td>
<td>0.59</td>
</tr>
<tr>
<td></td>
<td>Total</td>
<td>0.05</td>
<td>0.10</td>
<td>0.24</td>
<td>0.66</td>
</tr>
<tr>
<td>IRMOF-12</td>
<td>A</td>
<td>0.08</td>
<td>0.14</td>
<td>0.33</td>
<td>0.68</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>0.06</td>
<td>0.13</td>
<td>0.34</td>
<td>1.06</td>
</tr>
<tr>
<td></td>
<td>Total</td>
<td>0.07</td>
<td>0.14</td>
<td>0.34</td>
<td>0.87</td>
</tr>
<tr>
<td>IRMOF-14</td>
<td>A</td>
<td>0.06</td>
<td>0.11</td>
<td>0.24</td>
<td>0.48</td>
</tr>
<tr>
<td></td>
<td>B</td>
<td>0.06</td>
<td>0.11</td>
<td>0.32</td>
<td>0.96</td>
</tr>
<tr>
<td></td>
<td>Total</td>
<td>0.06</td>
<td>0.11</td>
<td>0.28</td>
<td>0.71</td>
</tr>
</tbody>
</table>

hydrogen molecules and the characteristics of pores. To evaluate the quantitative adsorption capacities, the hydrogen molecules within 3.1 Å from the IRMOF surface were considered as being definitely adsorbed on the framework surfaces. After identifying them and their locations, the numbers of hydrogen molecules in the A and B pores of each IRMOF and overall adsorbed hydrogen amount were counted to give their respective densities as shown in Table 2.

The density values in Table 2 were calculated based on the available volume of each pore and total available volume in Table 1. From the comparison of overall adsorbed hydrogen density, IRMOF-1 has the highest density due to the relative small available volume of IRMOF-1, even though the difference becomes dim, as the hydrogen content is increased. Meanwhile, the contribution of organic linker for adsorption behavior is clearer at the lower hydrogen content than higher hydrogen content. This means that the main contribution of organic linker for hydrogen adsorption is not from the chemical characteristics but the pore size of framework with linker.

The analyses of the density distributions in the A and B pores of each IRMOF induce three important observations and estimations. Firstly, even at 5.0 wt% of the hydrogen content, the adsorbed densities in the pores are much smaller than those of the liquid hydrogen density. Therefore, it can be deduced that all the adsorption sites are not yet occupied at 5.0 wt%. It means the hydrogen capacity of non-interpenetrating MOFs still can be improved not by pore filling but by adsorption above 5.0 wt% uptakes.

Secondly, all IRMOFs with larger organic linkers tend to have smaller densities than that of IRMOF-1 for most loading conditions. The available volumes for pores in IRMOF-1 are 36.8-40.1% of IRMOF-10, -12, -14. It means that the gain by larger organic linker cannot overcome the loss by volumetric expansion for adsorption in case of non-interpenetrating MOFs. The difference of adsorbed hydrogen density between IRMOF-10, -12, -14 is not greater than the difference between IRMOF-1, and IRMOF-10, -12, -14. Once again, the sorts of the organic linkers affect the hydrogen adsorption process noticeably not by chemical character of linker but by the larger volume induced by longer chemical moiety.

Thirdly, the hydrogen densities in B pores become larger than A pores as the hydrogen content is increased. For IRMOF-10, -12, and -14, B pores have their volumes with 80-87.1% of A pores. Nevertheless, the density of adsorbed hydrogen in the B pores range from 103 to 133% as compared to those in the respective A pores with 5.0 wt% hydrogen contents. In most cases except for IRMOF-10, the ratios of the hydrogen densities in B to those in A pores are increasing as hydrogen loadings reach to liquid density of hydrogen. The abnormal behavior of IRMOF-10 may be due to the absence of the organic moieties linking two phenyl rings in biphenyl-4,4'-dicarboxylate linkers. Even though we set the starting geometry of IRMOF-10 with flat biphenyl groups to discriminate A and B pore, the torsional angle between two phenyl rings of organic linker were naturally twisted by force field during the molecular dynamics simulation. Therefore, the discrimination of density in each pore type of IRMOF-10 is meaningless.

The favorable hydrogen adsorption in B pores rather than A pores seems to be related to the orientation of the organic linkers described in Fig. 1. The smaller B pore is surrounded by 12 edges of the aromatic organic linkers, and the larger A pores by 12 faces of the aromatic rings. Although the A pores can provide more effective framework surface area, the longer separation between the aromatic planes may not give a concerted van der Waals potential to the adsorbates present between them. On the other hand, the B pores have closer organic linkers, and may affect relatively stronger potential to the hydrogen molecules confined in a smaller pore. In this regard, it is understandable that IRMOF-12 having bulky and flexible -CH₂CH₂- bridges adsorbs more hydrogen molecules on its framework surface than other IRMOFs. In other words, the adsorbed hydrogen molecules into IRMOFs are not evenly distributed through the all framework surface, especially at high loading of hydrogen. In addition, the previous density functional calculation indicated that the stabilization effect among the adsorbed hydrogen molecules is noticeable even though its absolute values are very small, and should not be ignored as the hydrogen content increases [15]. Frost et al. suggested that the surface area and free volume of MOFs could be the important characteristics in evaluating and quick screening any potential hydrogen storage adsorbent based on the assumption of the identical monolayer adsorption [24]. However, this suggestion needs to be discerned from our results in this work because hydrogen adsorption behavior may be affected in a subtle way by the respective pore environment and characteristics at the high loading of hydrogen into MOFs.

### 3.3. Hydrogen adsorption on interpenetrating IRMOFs

Now we analyze the hydrogen densities in the pores of the interpenetrating IRMOFs. In general, the total adsorbed hydrogen

<table>
<caption>Table 3
The density of adsorbed hydrogen for each pore in the interpenetrating IRMOFs.</caption>
<thead>
<tr>
<th>MOFs</th>
<th>Pore</th>
<th colspan="4">Density of H₂ (1/Å³ × 10⁻²)</th>
</tr>
<tr>
<th></th>
<th></th>
<th>1 wt%</th>
<th>2 wt%</th>
<th>5 wt%</th>
<th>Liquid</th>
</tr>
</thead>
<tbody>
<tr>
<td>IRMOF-9</td>
<td>A'</td>
<td>0.05</td>
<td>0.14</td>
<td>0.46</td>
<td>0.75</td>
</tr>
<tr>
<td></td>
<td>B'</td>
<td>0.05</td>
<td>0.15</td>
<td>0.55</td>
<td>1.03</td>
</tr>
<tr>
<td></td>
<td>C</td>
<td>0.83</td>
<td>1.32</td>
<td>2.11</td>
<td>2.18</td>
</tr>
<tr>
<td></td>
<td>E</td>
<td>0.16</td>
<td>0.35</td>
<td>0.86</td>
<td>1.20</td>
</tr>
<tr>
<td></td>
<td>Total</td>
<td>0.18</td>
<td>0.36</td>
<td>0.83</td>
<td>1.11</td>
</tr>
<tr>
<td>IRMOF-11</td>
<td>A'</td>
<td>0.07</td>
<td>0.22</td>
<td>0.74</td>
<td>0.93</td>
</tr>
<tr>
<td></td>
<td>B'</td>
<td>0.12</td>
<td>0.34</td>
<td>1.00</td>
<td>1.42</td>
</tr>
<tr>
<td></td>
<td>C</td>
<td>1.31</td>
<td>1.84</td>
<td>2.69</td>
<td>2.88</td>
</tr>
<tr>
<td></td>
<td>E</td>
<td>0.20</td>
<td>0.48</td>
<td>1.17</td>
<td>1.41</td>
</tr>
<tr>
<td></td>
<td>Total</td>
<td>0.26</td>
<td>0.50</td>
<td>1.11</td>
<td>1.34</td>
</tr>
<tr>
<td>IRMOF-13</td>
<td>A'</td>
<td>0.06</td>
<td>0.14</td>
<td>0.51</td>
<td>0.68</td>
</tr>
<tr>
<td></td>
<td>B'</td>
<td>0.09</td>
<td>0.24</td>
<td>0.80</td>
<td>1.20</td>
</tr>
<tr>
<td></td>
<td>C</td>
<td>0.98</td>
<td>1.50</td>
<td>2.16</td>
<td>2.49</td>
</tr>
<tr>
<td></td>
<td>E</td>
<td>0.18</td>
<td>0.41</td>
<td>1.01</td>
<td>1.25</td>
</tr>
<tr>
<td></td>
<td>Total</td>
<td>0.22</td>
<td>0.41</td>
<td>0.92</td>
<td>1.15</td>
</tr>
</tbody>
</table>

densities of interpenetrating MOFs in Table 3 are greater than those of non-interpenetrating MOFs in Table 2. The gain of adsorbed hydrogen density is much greater at lower hydrogen content than that of higher hydrogen content. It clearly shows that the porous material with smaller pore can have a feasible volumetric capacity for hydrogen as shown in the previous experimental studies by Rowsell et al. [9,10]. The hydrogen molecules are adsorbed more densely in the catenation-induced C and E pores than in A' and B' pores as shown in Table 3. Actually, C pores are composed of two types, and the average volume of them has been used due to their permuting arrangement in the interpenetrating MOFs.

Although the similar relationship is observed between the pore size and the density of hydrogen adsorbed, the extent of saturation is somewhat different from that in the non-interpenetrating IRMOFs. We notice that at 2 wt% of hydrogen content the hydrogen densities in C pores are about 60% of the liquid density, whereas the average density in A and B pores in the non-interpenetrating IRMOFs is only about 50% of the liquid density even at 5 wt% of hydrogen content. The C pore is confined by a pair of organic linkers and is so narrow as to make a deep potential well between the two linkers. In our previous simulations, we suggested the overlap of the van der Waals potentials of adjacent linkers leads to the increase of adsorption capacity referring to the theoretical study on van der Waals slit [16]. This molecular dynamics simulation study supports the suggestion, and indicates that the adsorbed hydrogen molecules by the overlap potential could be more easily condensed to form a liquid like phase.

From the viewpoint of the concept of van der Waals slit, the density of E pore is intermediate due to its relatively larger slit gap than that of C pore. Now we can explain why IRMOF-11, having the smallest surface area, can achieve the maximum uptake of hydrogen at low pressure using this overlap potential induced hydrogen adsorption into non-interpenetrating MOFs [9,10].

The liquid hydrogen density, 0.0708 g/cm³ is equivalent to the number density of $2.1 \times 10^{-2}/\mathring{A}^{3}$. As the hydrogen content of our simulation increases, the adsorbed density of hydrogen in C pore exceeds the liquid hydrogen density, which may be from the hydrogen confinement due to its narrow van der Waals slit. Using more sophisticated potential function of hydrogen, we may reduce this overestimation. However, the overall observation and results would not be changed.

Comparing with the density variations of non-interpenetrating MOFs and those of interpenetrating MOFs, we can find that the hydrogen adsorption into MOFs depends on the shape and size of pore of MOFs more than the chemical characteristics of organic linker itself, in particular at low pressure. It is an agreeable conclusion with our previous experiment in which the small modification of functional group of organic linker can only get the small gain of hydrogen loading into MOFs [8]. Therefore, it is questionable that just the enlargement of pores in MOFs can be the effective way of hydrogen storage via physical adsorption mechanism even if we can store hydrogen gas under extreme conditions. Recently, it has been assumed that there is an empirical correlation between surface area and saturation H₂ uptake [10]. However, we conjecture that the higher excess H₂ uptake of IRMOF-1 than IRMOF-11 may be due to the hovering hydrogen in free volume of MOFs at high pressure rather than the higher binding ability of IRMOF-1 because at low pressure, IRMOF-11 has more capacity of H₂ [19].

### 3.4. Hydrogen diffusion in IRMOFs

We also calculated the diffusion coefficient of hydrogen molecules to investigate the dynamic behavior of the adsorbed molecules. In the calculation of diffusion coefficient, we used all hydrogen molecules in the pores, instead of the adsorbed hydrogen molecules. As summarized in Table 4, the diffusion rate of hydrogen is dramatically reduced by the catenation of IRMOFs, which indicates that the motion of hydrogen molecules in IRMOFs is disturbed by the interpenetrating chains and/or by tighter binding of hydrogen molecules on the interpenetrating IRMOFs. It is expected that diffusion of hydrogen molecules is closely related to the pore size, and dynamic motion of hydrogen molecules is restricted more in the interpenetrating MOFs with small pores. The calculated diffusion rates indicate that the hydrogen molecules adsorbed on the interpenetrating IRMOFs diffuse throughout the MOF channels as slow as in liquid hydrogen condensed at lower temperature ($1.6 \mathring{A}^{2}/\text{ps}$ at 25 K, $0.68 \mathring{A}^{2}/\text{ps}$ at 17 K) [29]. This observation is equivalent to the results of adsorbed hydrogen densities in the interpenetrating IRMOFs.

<table>
<caption>Table 4<br>The self diffusion coefficients of H₂ in IRMOFs.</caption>
<thead>
<tr>
<th>H₂ contents</th>
<th colspan="6">Self diffusion coefficients of H₂ in MOFs ($\mathring{A}^{2}$/ps)</th>
</tr>
<tr>
<th></th>
<th>IRMOF-10</th>
<th>IRMOF-12</th>
<th>IRMOF-14</th>
<th>IRMOF-9</th>
<th>IRMOF-11</th>
<th>IRMOF-13</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 wt%</td>
<td>7.92</td>
<td>4.58</td>
<td>5.51</td>
<td>0.24</td>
<td>0.09</td>
<td>0.20</td>
</tr>
<tr>
<td>2 wt%</td>
<td>7.21</td>
<td>5.25</td>
<td>5.37</td>
<td>0.56</td>
<td>0.29</td>
<td>0.33</td>
</tr>
<tr>
<td>5 wt%</td>
<td>6.70</td>
<td>6.24</td>
<td>5.63</td>
<td>0.95</td>
<td>0.95</td>
<td>0.80</td>
</tr>
<tr>
<td>Liquid</td>
<td>3.62</td>
<td>3.10</td>
<td>3.26</td>
<td>0.96</td>
<td>0.96</td>
<td>0.72</td>
</tr>
</tbody>
</table>

Recently, the diffusion of hydrogen molecules in interpenetrat- ing MOFs has been calculated using molecular dynamics simula- tions by Liu et al. [25]. Their predicted diffusion coefficients are larger than ours by one order of magnitude because they performed MD simulations at room temperature. Nevertheless, the decreasing tendency with the high loading and the small pores is consistently observed.

## 4. Conclusions

Our simulation studies showed that the adsorption char- acteristics of interpenetrating and non-interpenetrating MOFs using the analysis of the only adsorbed hydrogen into MOFs. The hydrogen molecules can be densely adsorbed in the small pores created by catenation for all kinds of organic linkers considered here. This observation indicates that a deep potential well can be created by the overlap of the van der Waals potentials of the pore walls and, as a result, the binding energy between hydrogen molecules and the walls can be increased in small pores. Using the results, we can also explain why the materials having small surface area can achieve higher hydrogen uptake at low pressure and why the trend of hydrogen uptake for MOFs may be different as the pressure condition changes. Dynamic motion of hydrogen molecules is more restricted when they are adsorbed on the interpenetrating IRMOFs than on the non-interpenetrating IRMOFs. The small diffusion coefficients of hydrogen molecules in the interpenetrating IRMOFs indicate that the state of hydrogen is similar to the condensed phase of liquid hydrogen at low temperature. All the calculation results confirm that there is a significant pore size effect on the hydrogen adsorption properties of MOFs and therefore the control of the pore size as well as its chemical structure is important to enhance the hydrogen storage capability.

### Acknowledgments

This research was performed for the Hydrogen Energy R&D Center, one of the 21st Century Frontier R&D Program, funded by the Ministry of Education, Science and Technology of Korea. We thank Accelrys Korea for the support of modeling software.

### References

[1] H. Furukawa, M.A. Miller, O.M. Yaghi, J. Mater. Chem. 17 (2007) 3197–3204.

[2] M. Dincă, A. Dailly, Y. Liu, C.M. Brown, D.A. Neumann, J.R. Long, J. Am. Chem. Soc. 128 (2006) 16876–16883.

[3] D.J. Collins, H.-C. Zhou, J. Mater. Chem. 17 (2007) 3154–3160.

[4] Energy Efficiency and Renewable Energy, Hydrogen, Fuel Cells & Infrastructure Technologies Program, http://www1.eere.energy.gov/hydrogenandfuelcells/mypp/, Multi-Year Research, Development and Demonstration Plan: Planned Program Activities for 2005–2015. 3.3 Hydrogen Storage, 2007.

[5] J.L.C. Rowsell, O.M. Yaghi, Angew. Chem. Int. Ed. 44 (2005) 4670–4679.

[6] B. Chen, N.W. Ockwig, A.R. Millward, D.S. Contreras, O.M. Yaghi, Angew. Chem. Int. Ed. 44 (2005) 4745–4749.

[7] H. Chun, D.N. Dybtsev, H. Kim, K. Kim, Chem. Eur. J. 11 (2005) 3521–3529.

[8] D. Kim, T.B. Lee, S.B. Choi, J.H. Yoon, J. Kim, S.-H. Choi, Chem. Phys. Lett. 420 (2006) 256–260.

[9] J.L.C. Rowsell, O.M. Yaghi, J. Am. Chem. Soc. 128 (2006) 1304–1315.

[10] J.L.C. Rowsell, A.R. Millward, K.S. Park, O.M. Yaghi, J. Am. Chem. Soc. 126 (2004) 5666–5667.

[11] S. Ma, D. Sun, M.W. Ambrogio, J.A. Fillinger, S. Parkin, H.-C. Zhou, J. Am. Chem. Soc. 129 (2007) 1858–1859.

[12] U. Mueller, M. Schubert, F. Teich, H. Puetter, K. Schierle-Arndt, J.J. Pastré, J. Mater. Chem. 16 (2006) 626–636.

[13] T. Sagara, J. Klassen, J. Ortony, E.J. Ganz, Chem. Phys. 123 (2005) 14701-1–14701-4.

[14] T. Mueller, G.J. Ceder, J. Phys. Chem. B 109 (2005) 17974–17983.

[15] T.B. Lee, D. Kim, D.H. Jung, S.B. Choi, J.H. Yoon, J. Kim, K. Choi, S.-H. Choi, Catal. Today 120 (2006) 330–335.

[16] D.H. Jung, D. Kim, T.B. Lee, S.B. Choi, J.H. Yoon, J. Kim, K. Choi, S.-H. Choi, J. Phys. Chem. B 110 (2006) 22987–22990.

[17] Q. Yang, C. Zhong, J. Phys. Chem. B 109 (2005) 11862–11864.

[18] Q. Yang, C. Zhong, J. Phys. Chem. B 110 (2006) 655–658.

[19] D.H. Jung, D. Kim, T.B. Lee, J. Kim, S.-H. Choi, Solid State Phenom. 124–126 (2006) 1693–1696.

[20] T. Yildirim, M.R. Hartman, Phys. Rev. Lett. 95 (2005) 215504-1–215504-4.

[21] D. Kim, J. Kim, D.H. Jung, T.B. Lee, S.B. Choi, J.H. Yoon, J. Kim, K. Choi, S.-H. Choi, Catal. Today 120 (2006) 317–323.

[22] S.R. Batten, R. Robson, Angew. Chem. Int. Ed. 37 (1998) 1460–1494.

[23] M. Eddaoudi, J. Kim, N. Rosi, D. Vodak, J. Wachter, M. O'Keeffe, O.M. Yaghi, Science 295 (2002) 469–472.

[24] H. Frost, T. Düren, R.Q. Snurr, J. Phys. Chem. B 110 (2006) 9565–9570.

[25] B. Liu, Q. Yang, C. Xue, C. Zhong, B. Smit, Phys. Chem. Chem. Phys. 10 (2008) 3244–3249.

[26] MS Modeling, Version 4.0, Accelrys Inc., San Diego, CA, USA.

[27] A.K. Rappé, C.J. Casewit, K.S. Colwell, W.A. Goddard III, W.M. Skiff, J. Am. Chem. Soc. 114 (1992) 10024–10035.

[28] S.L. Mayo, B.D. Olafson, W.A. Goddard III, J. Phys. Chem. 94 (1990) 8897–8909.

[29] J.A. Poulsen, G. Nyman, P.J. Rossky, J. Phys. Chem. B 108 (2004) 19799–19808.

[30] J. Kärger, D. Ruthven, Diffusion in Zeolites and other Microporous Materials, John Wiley & Sons, New York, 1992.

[31] A. Bondi, J. Phys. Chem. 68 (1964) 441–451 (other reference, http://en.wikipedia.org/wiki/Atomic_radii_of_the_elements_(data_page)).