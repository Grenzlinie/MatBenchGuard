![](./images/812759011177791488_1.jpg)

![](./images/812759011177791488_2.jpg)

# Nanoscale

## Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: G. Wang, B. Xu, J. Shi, M. wu, H. Su and C. Y. Ouyang, *Nanoscale*, 2019, DOI: 10.1039/C9NR03986D.

![](./images/812759011177791488_3.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/812759011177791488_4.jpg)

rsc./li/nanoscale

# ARTICLE

## New insights into Li diffusion in Li-Si alloy for Si anode materials: Role of Si microstructure

Guoqing Wang, $^{ab}$ Bo Xu, $^{*a}$ Jing Shi, $^{a}$ Musheng Wu, $^{a}$ Haibin Su, $^{c}$ and Chuying Ouyang*a

Li ion transport is very important to the rate capability of electrode materials in Li ion batteries. For Si anode, due to huge structural changes of Si structures during the process of charging and discharging, Li ion transport is essentially affected by the Si internal microstructures. Herein, we studied the effect of Si microstructures on Li ion diffusion in Li-Si alloys using the first-principles molecular dynamics calculations. Our results demonstrate that the Li diffusion coefficients are closely related with the aggregation degree of Si atoms, regardless of the low Li concentration phase LiSi or the high Li concentration phase $Li_{15}Si_{4}$. Furthermore, through counting the number of Si microstructures, such as rings, chains and small clusters, the relationship between the aggregation degree of Si atoms and the number of Si microstructures is established. Large number of Si microstructures corresponds to the low aggregation degree of Si atoms, thus resulting in the small Li diffusion coefficients due to the strong interaction between Li and Si atoms. Conversely, small number of Si microstructures originates from the high aggregation degree of Si atoms, consequently leading to the large Li diffusion coefficients. Our study provides a deep insight into the relationship between the Li ion diffusion and the Si distribution, which facilitates the performance improvement of the future Si anode materials.

### Introduction

The fast-growing demand for high-energy-density Li-ion batteries (LIBs) used in portable devices and electric vehicles urges the development of the next-generation electrode materials with high-energy-capacity.[1-5] For instance, Si-based anodes have a high theoretical specific capacity of $4200\ \text{mAh/g}\ (\text{Li}_{4.4}\text{Si})$, which is 10-fold higher than that of graphite $372\ \text{mAh/g}\ (\text{LiC}_{6})$.[6,7] This high capacity, however, is associated with massive volume change (~300%) and morphology change during the charging and discharging process, which leads to mechanical fracture, disconnection between the particles of negative electrode materials, and thus affecting the transport properties of Li ions in anode materials.[8,9] As a result, in order to solve the problems existing in Si anode materials and improve the performance of LIBs, researchers have adopted some methods e.g. employing porous structure,[10-12] carbon coating,[13-15] nanowires,[16] and nanoparticles,[17] alloying Si with active/inactive elements,[18,19] using new additives,[20-22] or designing new flexible electrodes.[23-25] Additionally, to further improve the rate performance of LIBs, it is necessary to explore the deep relationship between Si structures and Li ion diffusion during the process of Li ion intercalation and deintercalation in Si anode materials.

So far, the studies on the Li-Si alloy for Si anode mainly focus on the Si structural evolution during lithiation. For example, Ostadhossein *et al.*[26] performed large-scale molecular dynamics (MD) simulations to study the Li insertion into Si nanowires. The results of lithiation at high temperature (about 1200 K) show that in the process of Li ion implantation into Si nanowires, the six-membered and eight-membered rings consisting of four-coordinated Si atoms are broken into smaller rings and atomic chains, thus resulting in the transition from crystalline to amorphous state of Si materials. Kim *et al.*[27] studied the structural properties of Li-Si alloys with different Li concentrations by *ab initio* molecular dynamics (AIMD). It is demonstrated that the tetrahedral Si structure is decomposed into various types of small clusters with the increase of Li concentration, such as monomer, dumbbell and so forth. Besides, Johari *et al.*[28] also used AIMD method to investigate the mechanism of phase transition of Si anode material during Li ion intercalation. Their results show that Li ions could break the rings and chains formed by Si atoms during the lithiation process, produce the

---
$^{a}$ Department of Physics, Laboratory of Computational Materials Physics, Jiangxi Normal University, Nanchang 330022, PR China.
E-mail: [bxu4@mail.ustc.edu.cn](mailto:bxu4@mail.ustc.edu.cn), [cuouyang@hotmail.com](mailto:cuouyang@hotmail.com)
$^{b}$ Institute of Fundamental and Frontier Sciences, University of Electronic Science and Technology of China, Chengdu, 610054, PR China.
$^{c}$ Department of Chemistry, Hongkong University of Science and Technology, Hongkong, PR China.
E-mail: [haibinsu@ust.hk](mailto:haibinsu@ust.hk)
$^{\dagger}$ Footnotes relating to the title and/or authors should appear here.
Electronic Supplementary Information (ESI) available: [details of any supplementary information available should be included here]. See DOI: 10.1039/x0xx00000x

intermediate structures of stars and boomerangs, and eventually form dumbbells and isolated Si atoms.

The works mentioned above suggest that Li insertion significantly affects the microscopic structures of Si anode materials. Actually, the Si structures can in turn affect the migration of Li ions. Pan *et al.*[29] combined experiments and calculations to investigate the effect of stress in Si anode on Li ion diffusion. They found that the stress can increase Li diffusion either through increasing free volume under tension or by changing local structure under compression. Moreover, our previous work[30] also demonstrates that the tensile strain on bulk Li-Si alloy can improve the mobility of Li ions. The application of tensile strain increases the distances of Si-Si bonds, and decreases the interaction between Li atoms and Si atoms, thus reducing the transport barriers of Li ions. Besides, Zhao *et al.*[31] and Wang *et al.*[32] also studied the properties of Li ion diffusion in Si anode materials under stress conditions.

As we know, the external stresses only change the bond lengths to some extent, which remain the fundamental configurations of Li-Si alloy unchanged. However, the Si-Si bonds would be broken with the increase of Li concentrations. As a result, more smaller Si clusters or chains appear. Compared with the variation of Li-Si bond lengths under stress, the effect of size and distribution of the small Si microstructures (ring, cluster, chain, and so on), which results from the variation of Li concentration, might be more distinct due to the more complicated Li-Si interactions. Unfortunately, the influence of the Si microstructure on the diffusion properties of Li ions is less studied. Motivated by this, in this work, we performed the AIMD calculations to study Li ion diffusion in Li-Si alloy with different Si microstructures. The purpose is to further explore the diffusion mechanism of Li ions in Si anode materials. Through analysing Li diffusion coefficient in different Li-Si alloys, we established the relationship between Li ion diffusion and Si microstructures. This work provides the deep insight into the diffusion mechanism of Li ions in Si anode materials, and is helpful to modify or design future Si-based anode materials.

## Computational methods
All first-principles calculations in this study were performed by using density functional theory (DFT) method as implemented in Vienna *ab initio* Simulation Package (VASP) code with a plane wave basis set.[33,34] The electron-ion interaction was described by projected augmented wave (PAW) potentials.[35] The exchange-correlation functional was described by the generalized gradient approximation (GGA) parameterized by Perdew-Wang terms (PW91).[36] The energy cut-off of 450 eV was employed for the plane wave expansion.

The migrations of Li and Si atoms in the Li-Si alloy were simulated by using AIMD method in the canonical ensemble (NVT). A Verlet algorithm was employed to solve the Newton's equations of motion at a time step of 1.5 fs for a total simulation time of 15 ps, i.e. 10000 steps. The temperature was controlled via Nosé-Hoover thermostat during the whole simulations. In addition, for the AIMD simulations the Brillouin zone sampling was done with $\Gamma$-point.

From the statistical physics point of view, mean-square displacement (MSD) is usually used to describe the random migration of ions in materials. Generally, a poor ionic conductor exhibits a plateau feature in the plot of MSDs for all ions, which is independent of time. In contrast, a good ionic conductor has a monotonic increase trend of MSD curve with the increase of time. The degree of Li ion migration can be described by a time-dependent MSD,

$$
\begin{aligned}
\text{MSD} = \langle \delta r^2 \rangle = \langle [r_m(t + t_0) - r_m(t_0)]^2 \rangle = \frac{1}{N}\sum_m [r_m(t + t_0) - r_m(t_0)]^2
\tag{1}
\end{aligned}
$$

where $N$ is the total number of ions, $r_m$ ($t + t_0$) and $r_m$ ($t_0$) are the displacements of the $m^{\text{th}}$ ion at $t + t_0$ and $t_0$ time, respectively. The angle brackets stand for the statistical average. The average self-diffusion coefficient ($D$) of each ion is then given by the slope of the average MSD plots,

$$
D = \lim_{t \to \infty} \frac{\text{MSD}(t)}{6t}
\tag{2}
$$

However, the $D$ herein is not a chemical diffusion coefficient in Fick's equation to describe the migration flux of species under a chemical concentration gradient. Instead, it is a self-diffusion coefficient, which describes the migration ability of ions without concentration gradient.

To study the diffusion of Li ions in Li-Si alloys with different Li concentrations, two kinds of Li/Si ratio is used in our calculations, i.e. LiSi and $\text{Li}_2\text{Si}$. As a start, we first selected the crystal structures of LiSi and $\text{Li}_2\text{Si}$. The optimized coordinates and lattice parameters of LiSi and $\text{Li}_2\text{Si}$ were taken from our previous calculations.[30] Then a 2×1×2 supercell of LiSi and a 3×2×2 supercell of $\text{Li}_2\text{Si}$ were constructed. Since the original structure of crystalline $\text{Li}_2\text{Si}$ is monoclinic, we transformed it into an orthorhombic system with the equal volume in order to facilitate the later AIMD simulations. In our calculations, $\text{Li}_2\text{Si}$ was used as the Li-rich state for Li-Si alloy, while LiSi as Li-deficient state. We adopted the simulated annealing method to search a series of amorphous structures of LiSi and $\text{Li}_2\text{Si}$ with different Li/Si arrangement. Fig. 1(a) shows one of the amorphous LiSi. For the amorphous LiSi structure, the lattice constants of the

supercell are $a = 18.706$ Å, $b = 9.353$ Å, and $c = 11.486$ Å, respectively. There are 64 Li and 64 Si atoms in the amorphous LiSi structure. Fig. 1(b) shows one of the amorphous $\text{Li}_2\text{Si}$. The corresponding lattice constants are $a = 15.40$ Å, $b = 13.23$ Å, and $c = 12.01$ Å, respectively. It contains 96 Li and 48 Si atoms. It is noted that the supercells of the others amorphous structures for LiSi and $\text{Li}_2\text{Si}$ have the same sizes as those in Fig. 1(a) and 1(b), respectively. The difference only exists in the distribution of Li and Si atoms.

![](./images/812759011177791488_5.jpg)

Fig. 1 (a) Structure of amorphous LiSi, (b) structure of amorphous $\text{Li}_2\text{Si}$. Blue spheres represent Si atoms, and green spheres represent Li atoms.

A plenty of Si primitive rings (enclosed ring formed by Si atoms) and other Si microstructures (atomic cluster) can be found during the lithiation process. The number of rings was analysed by the R.I.N.G.S. code [37], while other Si microstructures were counted by using a home-built code. These microstructures include chains and small clusters, e.g., isolated atoms, dumbbells, boomerangs, star (see Fig. 2).

![](./images/812759011177791488_6.jpg)

Fig. 2 Representative microstructures in the amorphous Li-Si alloy, including (a) isolated atom, (b) dumbbell, (c) boomerang, (d) and (e) stars, (f) and (g) chains, (h), (i), and (j) primitive rings.

## Results and Discussion

### LiSi structures
For amorphous LiSi, we first selected two different initial configurations, labelled as LiSi-St-1 and LiSi-St-2. After the AIMD simulation of 15 ps at 800 K, diffusion coefficients, which reflect the ability of ionic movement, were calculated through the MSD profiles according to eqn (1) and eqn (2). Generally, for LIBs, the working temperature should be room temperature. We selected the simulation temperature of 800 K due to the following reason. For the finite simulation time, higher temperature is beneficial to the ionic movement, which facilitates to observe the ionic diffusion. Actually, we had tested the case at room temperature (300 K). The results show that the relationship between Si microstructures and Li ion diffusion coefficients mentioned in this work can also be obtained at room temperature. However, the results are more obvious at 800 K when compared with the case at 300 K. Therefore, we selected 800 K as the simulation temperature in our AIMD calculations. Similar simulation temperature can also be found in other literatures[27,28], which studied amorphous Li-Si alloys in LIBs at relatively high temperatures.

Fig. 3(a) and 3(b) show the MSD profiles of all Li ions in LiSi-St-1 and LiSi-St-2. The projected MSD profiles along $x, y, z$ directions are also given. According to Fig. 3(a) and 3(b), it is found that the MSD of Li ions along $x$ direction contributes the most to the total MSD. Moreover, the total MSD of Li ions in LiSi-St-1 is obviously smaller than that in LiSi-St-2 at the same time scale. Consequently, the linear fitting over the time interval yields the Li diffusion coefficient $D_{\text{Li}} = 5.0 \times 10^{-6}$ cm²/s in LiSi-St-1, which is significantly smaller than that in LiSi-St-2 with $D_{\text{Li}} = 11.3 \times 10^{-6}$ cm²/s.

![](./images/812759011177791488_7.jpg)

Fig. 3 Total and projected MSD profiles along $x, y$, and $z$ directions for all Li ions in (a) LiSi-St-1 and (b) LiSi-St-2 at 800 K. The density map of the projected plane of Si atoms along $x$ direction in (c) LiSi-St-1 and (d) LiSi-St-2, the brighter the region is, the denser the Si distribution is.

To explore the reasons for the different Li diffusion rates in the two different LiSi configurations, we analysed the projected atomic density map of all Si atoms along $x$ direction because the $x$ direction is the primary direction for Li ion diffusion, as shown in Fig. 3(c) and 3(d). Each picture contains the structural information of Si atoms at the first 1000 steps in the whole AIMD process. The projected density map distinctly reflects the movement range of Si atoms. The dark blue

region (without Si distribution) is surrounded by the distribution of Si atoms, which can be used as a descriptor of channel for Li ions diffusion. To further explore why the diffusion coefficients of Li ions along the $x$ direction is distinct in the two completely different amorphous LiSi structures, we calculated the cross-section area of Li diffusion channel for the two cases. In other word, we evaluated the area of dark blue region. It is found that the proportion of the channel area of LiSi-St-1 and LiSi-St-2 are 67.2% and 73.4%, respectively. Combined with the diffusion coefficients of Li ions, it is found that small channel area corresponds to small diffusion coefficient, e.g., LiSi-St-1, whereas large channel area corresponds to large diffusion coefficient, e.g., LiSi-St-2. According to the information from LiSi-St-1 and LiSi-St-2, we inferred that the cross-section area of the channel is proportional (a strong positive correlation) to the diffusion coefficients of Li ions. In fact, the channel area reflects the aggregation degrees of Si atoms (localized and delocalized). Large channel area represents the high aggregation degree of Si atoms, and vice versa. As a result, we speculated that the aggregation degree of Si atoms affects the diffusion performance of Li ions to some extent.

To verify the conjecture mentioned above, we artificially modified the Si distribution in amorphous LiSi. Based on the structure of LiSi-St-1, we drew some Si atoms close to each other, thus increasing the aggregation degree of Si atoms. The new structure is named as LiSi-St-1'. Similarly, we reduce the aggregation degree of Si atoms to obtain the structure of LiSi-St-2'. After the AIMD simulation, the proportion of the channel area increases (decreases) to 71.1% (69.9%) for LiSi-St-1' (LiSi-St-2'). Consequently, the calculated Li diffusion coefficient are $7.5 \times 10^{-6}$ and $8.4 \times 10^{-6}$ cm²/s for LiSi-St-1' and LiSi-St-2', respectively. The MSD profiles of Li ions and projected density of Si atoms after structural modification are shown in Fig. S1† (see Supplementary Information). Compared with LiSi-St-1, the channel area of Li ions in LiSi-St-1' is larger, and accordingly the diffusion coefficient of Li ions increases. However, the channel area of Li ions in LiSi-St-2' is smaller than that in LiSi-St-2. Therefore, the smaller diffusion coefficient of Li ions in LiSi-St-2' is obtained. Obviously, such results validate our preliminary conclusions.

To further generalize our conclusions, we selected three other LiSi configurations with different Si distribution, which are named as LiSi-St-3, LiSi-St-4, and LiSi-St-5. The calculated diffusion coefficients of Li ions and the proportion of the channel areas are shown in Fig. 4 and Table S1† (see Supplementary Information). Compared Fig. 4(a) with Fig. 4(b), it is found that the Li diffusion coefficients are positively related with the channel areas. Specifically, the larger the channel area is, the larger the Li diffusion coefficient is, which is in agreement with our previous conclusion.

![](./images/812759011177791488_8.jpg)

Fig. 4 (a) Li diffusion coefficients and (b) proportion of the channel area in different LiSi configurations.

![](./images/812759011177791488_9.jpg)

Fig. 5 Positions of No. 46 and No. 52 Li ions in LiSi-St-1.

Based on the aforementioned results, the aggregation degree of Si atoms is closely related with the transport of Li ions. In other word, the interaction between Si atoms and Li ions significantly affects the diffusion of Li ions. To understand the influence of Si distribution on the Li diffusion at atomic level, we examined the velocities of all Li ions in LiSi-St-1 at each time step. After that, the standard deviation of velocity for each Li ion was able to be obtained. Two representative Li ions were chosen in LiSi-St-1, which were labelled as No. 46 and No. 52, as shown in Fig. 5. From this figure, we could find that No. 52 Li ion is surrounded by more Si atoms with respect to No. 46 Li ion. Fig. 6(a) and 6(c) show the velocities of No. 46 and No. 52 Li ions at each time step. Accordingly, the average velocities and the standard deviations of velocities could be calculated. The calculated average velocities of No. 46 and No. 52 Li ions are $1.641 \times 10^{3}$ and $1.543 \times 10^{3}$ m/s, respectively. The standard deviations of velocities are 687.08 and 605.13 for No. 46 and No. 52 Li ions, respectively. Obviously, the average velocity and the standard deviation of velocity for No. 46 Li ion are larger than those for No. 52 Li ion, which means that the restriction degree of No. 46 Li ion is weaker than that of No. 52 Li ion. Such result is consistent with the structural information from Fig. 5, where the number of the neighbouring Si atoms of No. 46 Li ion is less than that of No. 52 Li ion. In this situation, the interaction between Si atoms and the No. 46 Li ion is naturally weaker than that between Si atoms and the No. 52 Li ion. To further confirm

the limitation effect of Si atoms on Li ions, we plotted the trajectories of No. 46 and No. 52 Li ions during the whole simulation process, which are shown in Fig. 6(b) and 6(d). Clearly, the movement range is localized for No. 52 Li ion, whereas dispersed for No. 46 Li ion. Therefore, when the distribution of Si atoms around the Li ion is dense, the interaction between Si atoms and the Li ion is strong, thus restricting the Li diffusion, e.g., No. 52 Li ion. On the contrary, sparse distribution of Si atoms around the Li ion would slightly affect the Li diffusion, e.g., No. 46 Li ion.

According to the results mentioned above, it is better to enable Si atoms accumulating so that more Li ions could escape the bound of Si atoms. During the process of charging (lithiation) and discharging (delithiation), however, the structural evolution of Si frame would take place. For different Li-Si alloy structures, how to describe the aggregation degree of Si atoms is very important, which could be directly used to estimate the Li diffusion coefficient. In order to do this, we analysed the microstructures formed by Si atoms. In Li-deficient amorphous phase of LiSi, it is found that the Si frame is mainly formed by the 3~8 member rings. Therefore, we counted the number of rings with different sizes using the R.I.N.G.S. code. Fig. 7(a) shows a representative LiSi structure and the statistical number of various Si rings. Herein, the periodic boundary conditions were taken into account.

![](./images/812759011177791488_10.jpg)

Fig. 6 Velocity and moving trajectory of Li ions at each time step, (a), (b) for No. 46 Li ion and (c), (d) for No. 52 Li ion. $V_x$, $V_y$, and $V_z$ stand for the velocities along $x$, $y$, and $z$ directions. $V_t$ is the total velocity.

![](./images/812759011177791488_11.jpg)

Fig. 7 Representative structures of Li-Si alloy and statistical number of various microstructures for (a) LiSi and (b) Li₂Si. In the LiSi structure, only the number of rings was counted. In the Li₂Si structure, isolated atoms, small clusters and chains were counted.

The cutoff radius of 2.5 Å was used for structural analysis.

First, LiSi-St-1 and LiSi-St-2 were considered for structural analysis. We examined all the rings for the two configurations during the whole AIMD process. As the data is expected to be huge, we picked up the structures every 10 steps. Therefore, 1000 sets of structures were obtained. After that, the number of rings for the 1000 sets of structures was summed. There are totally 2221 and 1746 rings for LiSi-St-1 and LiSi-St-2 cases, as shown in Fig. 8. The detailed statistical results for the rings with different Si atom number were also seen in Fig. 8. Likewise, the other LiSi structures, i.e., LiSi-St-1', LiSi-St-2', LiSi-St-3, LiSi-St-4, LiSi-St-5, were then analysed. In order to emphasize the impact of the ring number, we artificially modified the number of rings in LiSi structure. Taking LiSi-St-1 as the initial configuration, we reduced the number of rings to be 1862, and named it as LiSi-St-1''. Similarly, we increased the number of rings of LiSi-St-2 to be 2131, and named it as LiSi-St-2''. The statistical results for all structures were shown in Fig. 8 and Table S2† (see Supplementary Information).

![](./images/812759011177791488_12.jpg)

Fig. 8 Number of rings with different Si atom number, total number of rings and diffusion coefficients for various LiSi structures.

The Li diffusion coefficients for all structures were shown in Fig. 8 and Table S1† (see Supplementary Information). The MSD profiles of Li ions for LiSi-St-1’’ and LiSi-St-2’’ were shown in Fig. S2† (see Supplementary Information). For each kind of Si rings (3~8 member), no distinct relationship between the Li diffusion coefficients and the number of Si rings is observed. Interestingly, combining the diffusion coefficients of Li ions with the total number of various Si rings, the approximate inverse relation is clearly found. Specifically, large total number of Si rings corresponds to small Li diffusion coefficient, and vice versa. Therefore, we could use the total number of Si rings to evaluate the diffusion rate of Li ions. It is noted that the total number of Si rings is also associated with the channel areas based on the relationship between the Li diffusion coefficients and the channel areas (see Fig. 4). This is easy to be understood. From a statistical point of view, the increase of the number of Si rings means the dispersion of Si atoms under the condition of the constant Si atom number. Therefore, large total number of Si rings corresponds to low aggregation degree of Si atoms, thus resulting in small channel areas and low diffusion coefficients. On the contrary, small total number of rings leads to large channel areas.

### Li₂Si structures
After exploring the relationship between the Li diffusion property and the Si distribution in LiSi amorphous phase, we tried to figure out whether similar conclusions can also be found in Li-rich phase, such as Li₂Si. That is, whether high aggregation degree of Si atoms will result in large diffusion coefficients. Similar to the LiSi case, we first tried to find out whether the concept of diffusion channel is valid in Li₂Si structure. We chose one configuration of Li₂Si amorphous phase to carry out AIMD simulation. During the simulation process, it is found that the Si distribution is very dispersive. Besides this, the diffusion of Si atoms is relatively fast. According to the MSD profile (see Supplementary Information, Fig. S3†), the diffusion coefficient of Si atoms in Li₂Si structure is calculated to be $D_{Si}=3.5×10^{-6} cm^2/s$, which is about three times of that in LiSi case ($1.2×10^{-6} cm^2/s$). Taking into account the detailed structures, we found that many Si atoms in LiSi are connected to each other, which results in a robust Si frame. Therefore, the positions of Si atoms in LiSi are relatively local. In contrast, dispersive distribution of Si atoms in Li₂Si produces smaller atomic group with respect to LiSi, thus resulting in larger diffusion coefficients of Si atoms. Grey *et al.*[38-40] studied the chemical structures of lithiated pure-Si anodes by means of *in situ/ex situ* ⁷Li solid-state nuclear magnetic resonance (NMR) and pair distribution function (PDF) analysis. They found that a LiₓSi phase consists of polymeric Si chains and clusters with small x, while of more isolated Si atoms with large x. These findings further confirm the dispersive distribution of Si atoms in Li₂Si with respect to LiSi. Due to the dispersive distribution and fast diffusion of Si atoms, it is meaningless to consider the diffusion channel of Li ions. Despite this, the microstructures of Si atoms could be employed for our discussion. In addition, since the ring structures can hardly be observed, we only studied the effect of Si chains and small Si clusters (including isolated atom, dumbbell, boomerang, star) on the diffusion of Li ions in Li₂Si amorphous phase. The representative microstructures (chains and small clusters) were shown in Fig. 2. We also provided one sample of Li₂Si structures and the statistical number of various Si microstructures in this structure, as shown in Fig. 7(b).

We obtained five initial configurations of Li₂Si amorphous phase, namely Li₂Si-St-1, Li₂Si-St-2, Li₂Si-St-3, Li₂Si-St-4, and Li₂Si-St-5, by means of simulated annealing method. Then, the AIMD simulations for these five structures are performed. On one hand, we calculated the Li diffusion coefficients of these Li₂Si structures, which are shown in Fig. 9 and Table S3† (see Supplementary Information). On the other hand, we analysed the number of chains and small clusters. Analogous to the case of LiSi, we picked up the structures every 10 steps. Therefore, each Li₂Si case includes 1000 intermediate structures. The corresponding statistical results are shown in Fig. 9 and Fig. S4† (see Supplementary Information). Fig. 9(a) shows the total number of Si clusters and Si chains, while Fig. 9(b) and 9(c) give the number of all Si clusters and the number of all Si chains, respectively. Fig. S4† (see Supplementary Information) shows the separated results for the microstructures. In Fig. 9(a), the perfect inverse relations between the diffusion coefficients of Li ions and the total number of Si microstructures is observed. To further confirm this conclusion, we artificially reduced the total number of Si microstructures, which is named as Li₂Si-St-1’. The results are also

included in Fig. 9(a). Obviously, the relationship between the diffusion coefficient and the total number of Si microstructures still complies with the rules mentioned above. According to Fig. 9(b) and 9(c), one can see that the number of Si clusters is much larger than that of Si chains. As a result, the small Si clusters play a dominant role in affecting the diffusion of Li ions, while the Si chain structures play a modulating role. It is noted that though the number of clusters and chains in $\text{Li}_2\text{Si-St-1}$ is lower than that in $\text{Li}_2\text{Si-St-5}$, the Li ion diffusion coefficient of $\text{Li}_2\text{Si-St-1}$ is also lower than that of $\text{Li}_2\text{Si-St-5}$, which seems to be a little deviation from the rules mentioned above. Actually, it should be kept in mind that the Li diffusion coefficient is calculated according to the results of 10000 time steps. In contrast, the statistical results of microstructures (Fig. 9) are based on the 1000 intermediate structures. Therefore, the selected statistical samples could bring such slight deviation. The results of $\text{Li}_2\text{Si}$ are extremely similar to that of LiSi. Here, small number of Si chains and Si clusters stands for high aggregation degree of Si atoms, and vice versa. Therefore, high aggregation degree of Si atoms leads to large Li diffusion coefficient, whereas low aggregation degree of Si atoms results in small diffusion coefficient. Meanwhile, the total number of Si microstructures (including chains and clusters) could be used to describe the aggregation degree of Si atoms.

![](./images/812759011177791488_13.jpg)

Fig. 9 (a) Total number of Si microstructures and diffusion coefficients of Li ions, (b) total number of clusters, and (c) total number of chains for various $\text{Li}_2\text{Si}$ structures.

## Conclusions and Perspectives
View Article Online
DOI: 10.1039/C9NR03986D

In summary, we performed AIMD to study the influence of Si microstructures on the diffusion of Li ions in Li-Si alloy for Si anode materials. LiSi and $\text{Li}_2\text{Si}$ were selected as the representative Li-Si alloys for Li-deficient and Li-rich phases. By analysing the number of Si microstructures, including rings, chains, and small clusters, we established the relationship between the distribution of Si atoms and the Li diffusion coefficients. When the number of Si microstructures is large, which suggests the dispersed distribution of Si atoms, the Li diffusion coefficients is conversely small. In contrast, small number of Si microstructures corresponds to the aggregated distribution of Si atoms, thus resulting in large Li diffusion coefficients. Overall, the aggregation degree of Si atoms significantly affects the transport property of Li ion in the Li-Si alloys regardless of the Li concentration. Experimentally, Choi *et al.*[41] observed the line structures with a few nanometres on {100} surface of Si wafer during the lithiation process by using transmission electron microscopy (TEM). Furthermore, they thought that these line structures are micro-cracks that can provide fast diffusion paths for Li. The generation of micro-cracks results from the aggregation distribution of Si atoms to some extent. Therefore, this experimental result suggests that the aggregation distribution of Si atoms facilitates the diffusion of Li ions.

According to the results mentioned above, we proposed an envisage to further improve the Li transport property in Si anode materials during the process of charging and discharging. As shown in Fig. 10, we can purposefully dope some kinds of elements into Si anode, which facilitate the aggregation of Si atoms even if the charging/discharging process is ongoing. In this situation, not only that the diffusion rate of Li ions would be enhanced, but the cycle stability of Si anode materials is improved to some extent because less structural changes of Si frames happen. Actually, Pan *et al.*[42] studied the performance of silicon monoxide (SiO) as an anode material. They found that the Li-ion diffusion in SiO are consistently faster than that in Si by means of galvanostatic intermittent titration technique (GITT) and electrochemical impedance spectroscopy (EIS). What's more, by using scanning electron microscopy (SEM) analysis, the volume expansion rate of SiO particle (~118 %) is significantly less than that of Si particle (c.a. 280 %). Basically, the reduction of volume change in SiO originates from the introduction of O, which results in the formation of Si-O composite system and the aggregation distribution of Si atoms. Clearly, this result further verifies the effect of Si aggregation on Li diffusion. Therefore, our results in this work can provide a theoretical guidance for the design of Si anode materials with high rate capability and cycle stability.

![](./images/812759011177791488_14.jpg)

Fig. 10 Schematic diagram of Li ion diffusion in (a) pure Li-Si alloy and (b) element-doped Li-Si alloy. Red curves and straight lines represent the diffusion path of Li ions. Blue, green, and brown balls stand for Si, Li, and doped element atoms, respectively.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
This work was supported by the National Natural Science Foundation of China (Grants No. 11664012, 11564016), the Excellent Youth Foundation of Jiangxi Province (Grant No. 20171BCB23035).

## ORCID
Bo Xu: 0000-0002-6896-0409
Jing Shi: 0000-0003-3288-3306
Musheng Wu: 0000-0003-1366-8328
Chuying Ouyang: 0000-0001-8891-1682
Guoqing Wang: 0000-0003-3817-6856

## Notes and references
1.  J. M. Tarascon and M. Armand, *Nature*, 2001, **414**, 359-367.
2.  Y. Wang, B. Liu, Q. Li, S. Cartmell, S. Ferrara, Z. D. Deng and J. Xiao, *J. Power Sources*, 2015, **286**, 330-345.
3.  P. G. Bruce, S. Bruno and T. Jean-Marie, *Angew. Chem.-Int. Edit.*, 2010, **47**, 2930-2946.
4.  G. Jeong, Y.-U. Kim, H. Kim, Y.-J. Kim and H.-J. Sohn, *Energ. Environ. Sci.*, 2011, **4**, 1986-2002.
5.  M. Gu, Y. Li, X. Li, S. Hu, X. Zhang, W. Xu, S. Thevuthasan, D. R. Baer, J.-G. Zhang and J. Liu, *Acs Nano*, 2012, **6**, 8439-8447.
6.  P. Limthongkul, Y.-I. Jang, N. J. Dudney and Y.-M. Chiang, *Acta Mater.*, 2003, **51**, 1103-1113.
7.  U. Kasavajjula, C. Wang and A. J. Appleby, *J. Power Sources*, 2007, **163**, 1003-1039.
8.  S.-J. Lee, J.-K. Lee, S.-H. Chung, H.-Y. Lee, S.-M. Lee and H.-K. Baik, *J. Power Sources*, 2001, **97**, 191-193.
9.  M. Winter and J. O. Besenhard, *Electrochim. Acta*, 1999, **45**, 31-50.
10. M. Ge, J. Rong, X. Fang and C. Zhou, *Nano Lett.*, 2012, **12**, 2318-2323.
11. G. C. Shivaraju, C. Sudakar and A. S. Prakash, *Electrochim. Acta*, 2019, **294**, 357-364.
12. I. Gonzalez, A. N. Sosa, A. Trejo, M. Calvino, A. Miranda and M. Cruz-Irisson, *Dalton Trans*, 2018, **47**, 7505-7514.
13. L. Hou, H. Zheng, R. Cui, Y. Jiang, Q. Li, X. Jiang, J. Gao and F. Gao, *Micropor. Mesopor. Mat.*, 2019, **275**, 42-49.
14. L. Hong, Z. Wang, L. Chen and X. Huang, *Adv Mater*, 2010, **21**, 4593-4607.
15. Y. Wan-Jing, L. Chang, H. Peng-Xiang, Z. Lili, S. Xu-Yi, L. Feng and C. Hui-Ming, *Acs Nano*, 2015, **9**, 5063-5071.
16. C. Lam, Y. F. Zhang, Y. H. Tang, C. S. Lee, I. Bello and S. T. Lee, *J. Cryst. Growth*, 2000, **220**, 466-470.
17. C. K. Chan, H. Peng, L. Gao, K. Mcllwrath, F. Z. Xiao, R. A. Huggins and Y. I. Cui, *Nat. Nanotechnol.*, 2008, **3**, 31.
18. O. Mao, R. L. Turner, I. A. Courtney, B. D. Fredericksen, M. I. Buckett, L. J. Krause and J. R. Dahn, *Cheminform.*, 2010, **30**.
19. IH. Ghassemi, M. Au and R. Shahbazian-Yassar, *Microsc Microanal.*
20. . Urbanski, A. Omar, J. Guo, A. Janke, U. Reuter, M. Malanin, F. Schmidt, D. Jehnichen, M. Holzschuh, F. Simon, K.-J. Eichhorn, L. Giebeler and P. Uhlmann, *J. Electrochem. Soc.*, 2019, **166**, A5275-A5286.
21. T. Liu, Q. Chu, C. Yan, S. Zhang, Z. Lin and J. Lu, *Adv. Energy Mater.*, 2019, **9**.
22. J. Li, G. Zhang, Y. Yang, D. Yao, Z. Lei, S. Li, Y. Deng and C. Wang, *J. Power Sources*, 2018, **406**, 102-109.
23. X. Cai, W. Liu, Z. Zhao, S. Li, S. Yang, S. Zhang, Q. Gao, X. Yu, H. Wang and Y. Fang, *ACS Appl. Mater. Inter.*, 2019, **11**, 3897-3908.
24. C. Li-Feng, H. Liangbing, C. Jang Wook and C. Yi, *Acs Nano*, 2010, **4**, 3671-3678.
25. J.-Z. Wang, C. Zhong, S.-L. Chou and H.-K. Liu, *Electrochem. Commun.*, 2010, **12**, 1467-1470.
26. A. Ostadhossein, E. D. Cubuk, G. A. Trisaris, E. Kaxiras, S. Zhang and A. C. Van Duin, *Phys. Chem. Chem. Phys.*, 2015, **17**, 3832-3840.
27. H. Kim, C.-Y. Chou, J. G. Ekerdt and G. S. Hwang, *J. Phys. Chem. C*, 2011, **115**, 2514-2521.
28. P. Johari, Y. Qi and V. B. Shenoy, *Nano Lett.*, 2011, **11**, 5494-5500.
29. J. Pan, Q. Zhang, J. Li, M. J. Beck, X. Xiao and Y.-T. Cheng, *Nano Energy*, 2015, **13**, 192-199.
30. G. Wang, J. Shi, M. Wu, C. Ouyang and B. Xu, *Solid State Commun.*, 2016, **247**, 47-52.
31. K. Zhao, W. L. Wang, J. Gregoire, M. Pharr, Z. Suo, J. J. Vlassak and E. Kaxiras, *Nano Lett.*, 2011, **11**, 2962-2967.
32. H. Wang and H. B. Chew, *Extreme Mechanics Letters*, 2016, **9**, 503-513.
33. G. Kresse and J. Hafner, *Phys. Rev. B*, 1993, **47**, 558.
34. G. Kresse and J. Furthmüller, *Phys. Rev. B*, 1996, **54**, 11169.
35. G. Kresse and D. Joubert, *Phys. Rev. B*, 1999, **59**, 1758.
36. P. E. Blöchl, *Phys. Rev. B*, 1994, **50**, 17953.
37. S. Le Roux and P. Jund, *Comp. Mater. Sci.*, 2010, **49**, 70-83.
38. K. Ogata, E. Salager, C. J. Kerr, A. E. Fraser, C. Ducati, A. J. Morris, S. Hofmann, and C. P. Grey, *Nat. Commun.*, 2014, **5**, 3217.
39. B. Key, M. Morcrette, J. M. Tarascon, and C. P. Grey, *J. Am. Chem. Soc.* 2011, **133**, 503-512.
40. B. Key, R. Bhattacharyya, M. Morcrette, V. Seznec, J. M. Tarascon, and C. P. Grey, *J. Am. Chem. Soc.*, 2009, **131**, 9239.
41. Y. S. Choi, M. Pharr, C. S. Kang, S. B. Son, S. C. Kim, K. B. Kim, H. Roh, S. H. Lee, K. H. Oh and J. J. Vlassak, *J. Power Sources*, 2014, **265**, 160-165.
42. K. Pan, F. Zou, M. Canova, Y. Zhu, and J. H. Kim, *J. Power Sources*, 2019, **413**, 20-28.

Table of Content (TOC)

![](./images/812759011177791488_15.jpg)

**Synopsis:**
The effect of Si microstructures on Li ion diffusion in Li-Si alloys was studied by using the first-principles molecular dynamics calculations. The relationship between the aggregation degree of Si atoms and the Li diffusion coefficients is established.