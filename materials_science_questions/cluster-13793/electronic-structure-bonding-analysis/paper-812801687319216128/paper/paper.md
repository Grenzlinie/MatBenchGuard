OPEN
# Rapid and reversible lithiation of doped biogenous iron oxide nanoparticles

Masaaki Misawa¹²³, Hideki Hashimoto⁴, Rajiv K. Kalia³, Syuji Matsumoto⁵⁶, Aiichiro NakanoID³, Fuyuki Shimojo², Jun Takada⁵⁶, Subodh Tiwari³, Kenji Tsuruta⁶ & Priya Vashishta³

Received: 8 February 2018
Accepted: 28 November 2018
Published online: 12 February 2019

Certain bacteria produce iron oxide material assembled with nanoparticles (NPs) that are doped with silicon (Fe:Si ~ 3:1) in ambient environment. Such biogenous iron oxides (BIOX) proved to be an excellent electrode material for lithium-ion batteries, but underlying atomistic mechanisms remain elusive. Here, quantum molecular dynamics simulations, combined with biomimetic synthesis and characterization, show rapid charging and discharging of NP within 100fs, with associated surface lithiation and delithiation, respectively. The rapid electric response of NP is due to the large fraction of surface atoms. Furthermore, this study reveals an essential role of Si-doping, which reduces the strength of Li-O bonds, thereby achieving more gentle and reversible lithiation culminating in enhanced cyclability of batteries. Combined with recent developments in bio-doping technologies, such fundamental understanding may lead to energy-efficient and environment-friendly synthesis of a wide variety of doped BIOX materials with customized properties.

Biologically produced materials exhibit amazing properties that often surpass those of the best man-made materials¹. For example, microbes such as bacteria have remarkable abilities to synthesize materials with intricate nanostructures with outstanding properties²⁻⁵. Such biomineralization played crucial roles in the geological history of the Earth³. Since it usually occurs under ambient conditions, biomineralization is also utilized in environment-friendly renewable energy technologies such as the production of acetate from carbon oxide and sunlight⁴. An archetypal example of biomineralization is provided by iron (Fe)-oxidizing bacteria, which use divalent iron (Fe²⁺) in aqueous environment as an energy source²⁶⁻⁹. These bacteria are ubiquitous since Fe is the fourth most abundant element in the Earth's crust¹⁰. Their metabolism oxidizes Fe²⁺ into Fe³⁺ to gain energy, while depositing the product of the chemical reaction as iron oxide (Fe₂O₃) solid. Despite a hundred years of recognition of their importance¹¹, however, detailed knowledge about their physiology, chemistry and mechanics is severely limited. Aquatic iron-oxidizing bacteria, *Leptothrix ochracea*, produce Fe³⁺-based amorphous oxide microtubular sheaths consisting of nanoparticles (NPs) of diameter ~2 nm⁵¹². This biogenous iron oxide (BIOX) was found to be amorphous and doped with silicon (Si), with cation composition of Fe:Si ~ 3:1¹³¹⁴. Owing to its unique nanostructure, this material has been studied as a next-generation functional material¹⁵¹⁶. As a practical matter, nanostructured transition metal-containing mixed oxides, hydroxide, salts and even metal-organic frameworks are widely studied for energy-storage applications¹⁷⁻³². Among them, iron-oxide based NPs or nanosheets are promising electrode materials due to its high theoretical capacity, abundance and safety¹⁷⁻²⁴. Recently, BIOX was found to exhibit remarkable cyclability when used as an anode in lithium-ion batteries¹³¹⁴. Namely, their Li-storage capacity does not degrade after many lithiation/delithiation cycles, which is an essential property for commercially viable batteries. Since *Leptothrix ochracea* lives worldwide and readily produces BIOX at ambient conditions (e.g., the BIOX is widely seen in natural aquatic environment such as swamp or channel as

¹Faculty of Science and Engineering, Kyushu Sangyo University, Fukuoka, 813-8503, Japan. ²Department of Physics, Kumamoto University, Kumamoto, 860-8555, Japan. ³Collaboratory for Advanced Computing and Simulations, Department of Physics & Astronomy, Department of Computer Science, Department of Chemical Engineering & Materials Science, and Department of Biological Sciences, University of Southern California, Los Angeles, CA, 90089-0242, USA. ⁴Department of Applied Chemistry, School of Advanced Engineering, Kogakuin University, Tokyo, 192-0015, Japan. ⁵Core Research for Evolutionary Science and Technology (CREST), Japan Science and Technology Agency (JST), Okayama University, Okayama, 700-8530, Japan. ⁶Graduate School of Natural Science and Technology, Okayama University, Okayama, 700-8530, Japan. Correspondence and requests for materials should be addressed to A.N. (email: anakano@usc.edu)

![](./images/812801687319216128_1.jpg)

Figure 1. Simulated and synthesized NPs. (a,b) The initial configurations of the simulation cells with (a) $Fe_2O_3$ NP and (b) $Fe_2O_3$-$SiO_2$ NP in $LiPF_6$ electrolyte. White, red, yellow, green, pink, and brown spheres represent Fe, O, Si, Li, P and F, respectively. Blue lines show the cell edges. (c,d) TEM images of as-synthesized (c) 2Fh and (d) 20% Si-doped 2Fh, where the insets show ED patterns.

reddish-brown precipitate), it could provide sustainable supply of low-cost, high-performance Li-battery elec- trode materials in an environment-friendly manner. While the excellent performance of BIOX has been hypoth- esized to arise from its nanostructure based on 2 nm NP¹², the microscopic mechanisms underlying the superior cyclability remains elusive. Also not known is the role of the significant amount (~25%) of Si-doping. Thus, the fundamental scientific questions are: (1) how does the BIOX's nanostructure enhance the cyclability of lithiation, and (2) what is the role of-Si doping?

We performed joint simulation and biomimetic-experiment study in order to answer these questions. First principles quantum molecular dynamics (QMD) simulations were performed to study lithiation and delithiation properties of an amorphous Si-free and Si-doped $Fe_2O_3$ NPs, which is immersed in $Li^+(PF_6)^-$ electrolyte. QMD simulations follow the trajectories of all atoms while computing interatomic forces quantum mechanically from first principles (simulation details are described in methods). We simulated a Si-free NP ($Fe_{24}O_{36}$, Fig. 1a) and a Si-doped NP ($Fe_{18}O_{27-}Si_6O_{12}$, Fig. 1b), each immersed in 19 $LiPF_6$ at a temperature of 500 K. First, the simulation cells were thermalized for 1.33 picoseconds (ps) to confirm the structural stability. Next, 18 electrons were intro- duced in the simulation cells, and the systems were thermalized for 4.84 ps to study the lithiated state. Subsequently, delithiation dynamics were studied by removing 18 electrons and thermalizing the systems for 1.82 ps.

In order to mirror these QMD simulations, we chemically synthesized biomimetic iron oxide NPs (2-line ferrihydrite, 2Fh) with and without Si-doping (synthesis details are described in methods)³³. The microstructures of Si-free (Fig. 1c) and Si-doped (Fig. 1d) systems were observed using transmission electron microscopy (TEM). TEM images of Si-doped samples before and after discharging are found in ref.³³. Both samples consist of primary particles of a diameter of about 5 nm. The electron diffraction (ED) pattern for Si-free sample (inset in Fig. 1c) shows clear spots indicating monophasic crystalline structure of 2Fh, whereas degradation of the spots for the Si-doped sample (inset in Fig. 1d) can be attributed to amorphization of the structure by Si doping. The X-ray diffraction analysis also reveals the inhomogenization dependent on the Si molar ratio (Fig. S1 in supplementary information).

![](./images/812801687319216128_2.jpg)

Figure 2. Lithiated NP structure. (a,b) Snapshots of lithiated (a) Si-free and (b) Si-doped iron oxide NPs due to charging. White, red, yellow and green spheres represent Fe, O, Si and Li atoms, respectively. (c,d) Distribution of (c) O-Li-O and (d) Li-O-Li bond angles in the charged state. The black curve with circles and red curve with squares show the BADFs in the Si-free and Si-doped systems, respectively.

## Surface lithiation
First, we studied lithiated structures due to charging. Figure 2a,b, illustrates the Si-free and Si-doped iron oxide NPs, respectively, with Li atoms adsorbed on the surfaces. In this stage, the numbers of adsorbed Li atoms are the same between the two types of NPs. Poizot *et al.* demonstrated that the lithiation of transition-metal oxide NPs is accompanied by the nucleation of crystalline $\text{Li}_2\text{O}$,

$$
\text{M}_x\text{O}_y + 2y\text{e}^- + 2y\text{Li}^+ \rightarrow y\text{Li}_2\text{O} + x\text{M}(\text{M} = \text{Fe, Co, Ni, Cu}), \tag{1}
$$

which is distinct from the conventional lithiation mechanism based on Li insertion in bulk materials³⁴. On the other hand, it is considered that amorphous Li and Si-based amorphous oxide matrix is formed during the lith-iation/delithiation process of BIOX anodes¹³. Figure 2c,d, shows the bond angle distribution functions (BADFs) for O-Li-O and Li-O-Li bonds, respectively. Figure 2c shows a sharp peak in the O-Li-O angle distribution for the Si-free system. This peak corresponds to two-membered $(\text{Li-O})_2$ or $(\text{Li-O})(\text{Fe-O})$ rings as seen in Fig. 2a. On the other hand, in the Si-doped system, tetrahedral $\text{SiO}_4$ units likely hinder the formation of such two-membered rings. This explains the broader O-Li-O angle distribution for the Si-doped system in Fig. 2c. The existence of two-membered rings (as in crystalline $\text{Li}_2\text{O}$) in the Si-free system indicates the formation of crystalline $\text{Li}_2\text{O}$-like fragments in $\text{Fe}_2\text{O}_3$-NP anodes, which is consistent with previous studies in transition-metal oxide NPs³⁴, whereas amorphous Li and Si-based amorphous oxide matrix is formed in BIOX anodes, which again is consistent with previous studies¹³.

## Rapid delithiation
Starting from the lithiated states in Fig. 2, we investigated the delithiation dynamics upon discharging. Figure 3 shows time evolution of the number of Li ions classified by adsorption stages. To investigate the degree of lith-iation, we introduce the number of adsorbed Li ions, $N_{\text{ad}}$: (a) delithiated state, in which Li is not bonded to NP ($N_{\text{ad}}=0$, Fig. 3a); (b) intermediate state, in which Li is bonded to both NP and electrolyte anion ($N_{\text{ad}}=0.5$, Fig. 3b); and (c) lithiated state, in which Li is bonded only to NP but not to electrolyte anion ($N_{\text{ad}}=1.0$, Fig. 3c). Figure 3d shows the total value of $N_{\text{ad}}$ summed over all Li atoms as a function of time during 0.8 ps after the removal of electrons. The initial and final values of $N_{\text{ad}}$ were almost the same between Si-free and Si-doped sys-tems. The delithiation is accompanied by the change of the ionic valency (Fig. S2) as expected from Eq. (1), though the numbers of injected and ejected electrons, as well as the time duration of the simulations, are insufficient to

![](./images/812801687319216128_3.jpg)

Figure 3. Rapid delithiation of NPs. (a–c) Three types of the lithiation state: (a) delithiated, (b) intermediate and (c) lithiated states. (d) Time evolution of the number of adsorbed Li atoms on the surfaces, after 18 electrons were removed at $t=0$ ps. The black solid and red dashed curves correspond to the Si-free and Si-doped systems, respectively.

observe the complete conversion from $Fe^0$ to $Fe^{3+}$, as is inferred from previous X-ray photoelectron spectroscopy (XPS) data³⁵. Dissociation of Li ions on the Si-free NP started and the total $N_{\text{ad}}$ dropped very rapidly immediately after discharge (S1.mov in supplementary information). The dissociation reaction progressed around 80% during 0.05 ps, and almost completed by 0.3 ps. On the other hand, in the Si-doped system, the delithiation reaction proceeds more gently than in the Si-free system (S2.mov in supplementary information). It is conceivable that such a gentle dissociation behavior reduces the mechanical load and damage on electrodes, thereby resulting in improved cyclability.

### Structural stabilization by Si-doping
To quantify the structural stability of NPs during the delithiation process, Fig. 4a shows the average kinetic energies of the Li atoms that were dissociated from the NPs at the end of the simulation. Rapid increase of the kinetic energy is observed immediately after the removal of electrons in the Si-free system but not in the Si-doped system. The former may impose large stress on a NP and lead to structural deformations that are detrimental for the structural integrity of electrodes. To quantify geometric deformations of NPs, translationally and rotationally minimized root mean square displacements $D$ were calculated by

$$
D = \min_{b,A} \sqrt{\frac{1}{N} \sum_{i=1}^{N} (\mathbf{r}_{i}^{0} - \mathbf{b} - \mathbf{A}\mathbf{r}_{i}^{t})^{2}},
\tag{2}
$$

where $N$, $\mathbf{r}_{i}^{t}$, $\mathbf{b}$ and $\mathbf{A}$ are the number of atoms in a NP, atomic position of the $i$-th atom at time $t$, translational vector and rotation matrix, respectively³⁶. Figure 4b shows reduced $D$ for the Si-doped system compared to that of the Si-free system, indicating that the structural stability of NP during delithiation is increased by Si-doping. In order to characterize topological stability, the Hamming distances $D_{\text{H}}$ of the NPs (Fig. 4c) were calculated to quantify the number of chemical bond-breakage and bond-formation events:

$$
D_{H} = \frac{1}{2} \sum_{i,j}^{N} |\delta_{i,j}^{0} - \delta_{i,j}^{t}|,
\tag{3}
$$

where $\delta_{i,j}^{t}=1$ if bond exists between $i$-th and $j$-th atoms at time $t$, and 0 otherwise. Figure 4c shows that the topological change of the Si-doped NP is about 30% lower than that of the Si-free NP. These results show that Si-doping enhances the structural stability of BIOX NP, thereby increasing the cyclability of BIOX-based lithium-ion battery electrodes.

To test the hypothesis that the enhanced structural stability during delithiation of BIOX NPs due to Si-doping leads to improved cyclability of BIOX NP-based batteries, we experimentally measured the rate capability of BIOX-based lithium-ion battery. 2032 coin-type cells using 2-line ferrihydrite (2Fh, also called iron(III) oxide-hydroxides) and 20% Si-doped 2Fh for electrodes were prepared³³. Here, we used the Si-doped 2Fh as a basis of the primary NPs in the BIOX. The cell performance was evaluated using an electrochemical analyzer

![](./images/812801687319216128_4.jpg)

Figure 4. Structural stabilization and improvement of battery rate capability by Si-doping. (a–c) Time evolution of the average kinetic energy of dissociated Li atoms (a) geometrical deformation of NPs (b) and the Hamming distances (c) of the Si-free (black solid lines) and S-doped (red dashed lines) NPs during the delithiation simulations. (d) Experimental measurements of battery rate capabilities for the 2Fh (black), 20% Si-doped 2Fh (red) and their difference (blue with second y axis). In (a) cyan and yellow colors indicate the areas where the average kinetic energy for the Si-free system is greater and less than that for the Si-doped system, respectively.

(Toscat2000; Toyo System, Japan) under galvanostatic conditions in the voltage range of 0.3–3.0 V at 100–12,000 mA/g. The rate capability of the 2Fh samples were measured at current rates of 100, 300, 600, 1,500, 3,000, 6,000, 9,000, 12,000 mA/g. It was confirmed that the rate capabilities of the Si-20% system are higher than that of the 2Fh system above 600 mA/g and keeps lower fading as the current rate increases (Fig. 4d). This result is consistent with the kinetic, geometrical and topological behaviors in the lithiation/delithiation processes at high charging rate shown above. These values in the electrochemical property are comparable not only to those obtained for anodes with bacteriogenic samples (BIOX) but also to those in previous reports¹⁷⁻²¹ for other nanostructured iron oxides, e.g., Table 1 in ref.²¹. Thus, the essential feature of capacity enhancement solely by Si doping is clearly seen in this measurement.

Furthermore, to investigate the medium-range structural change and porosity of the NPs, distribution of cation (Fe and Si)-anion (O) rings in the NPs at delithiated states are analyzed using King's shortest-path criterion (Fig. S3)³⁷,³⁸. In the Si-free NP, the numbers of small four-membered rings and large ten-membered rings were reduced and the average ring size decreased upon lithiation and delithiation cycle, while the Si-doped NP showed opposite trends. It has been shown that the increased ring size is associated with tetrahedrally-coordinated atoms, which is inversely proportional to the number density³⁹,⁴⁰. Therefore, this result indicates that the four-coordinated Si atoms doped in NP reduces structural changes and increases porosity, resulting in enhanced capability and cyclability.

### Chemical origin of Si-dope-induced structural stability
In order to understand the fundamental mechanisms underlying the Si-doping-induced structural stabilization shown above, we estimated the bond strengths by performing bond overlap populations (BOP) analysis⁴¹. The BOP measures the covalency of chemical bonding. The BOP distributions for Li-O bonds before and immediately after removing electrons are shown in Fig. 5. The sharp peaks (pointed by blue arrows) at large positive bond orders in Fig. 5a indicate that strong bonds exist in the Si-free system. In contrast, the sharp peak (pointed by blue arrow) at a negative bond order in Fig. 5b represents anti-bonding in the Si-free system after removing electrons. Thus, Si-doping reduces the strength of covalent bonds. We also found that not only covalency but also ionicity of Li-O bonds in the Si-doped system is reduced compared to that in the Si-free system (Figs S4 and S5). The weaker chemical bonding in the Si-doped system explains less violent dissociation behaviors observed in the Si-doped system (S2.mov) compared to the Si-free system (S1.mov). Namely, the key structural stabilization mechanism is the weakening of Li-O bond, i.e., gentler lithiation and delithiation involving small binding energy with Si doping. Remarkable plastic deformation exhibited by Si at the nanoscale has also been utilized in lithium battery electrodes⁴². Recent reports have shown that nanostructured SiO₂-based anodes can exhibit high cyclability comparable to the present study, with higher capacity (> 1000 mAh/g) than other oxide-base anodes⁴³⁻⁵.

![](./images/812801687319216128_5.jpg)

Figure 5. Change of chemical bonding by Si-doping. Distribution of the bond overlap population between Li and O before (a) and immediately after (b) removing electrons. Black solid and red dashed lines are for the Si-free and Si-doped cases, respectively.

The BIOX-based anode, on the other hand, has its cost effectiveness due to its self-assembled/biogenous manner in its fabrication process.

In summary, our QMD simulations revealed the key role of Si-doping for the structural stability of BIOX NPs during lithiation and delithiation, which leads to the enhanced cyclability of Li-ion batteries as demonstrated by our biomimetic synthesis and characterization. Recent developments in bio-doping technologies have enabled intricate control of the chemical composition of biogenous NPs by simply changing the solutions in which the bacteria are cultivated⁴⁶⁴⁷. The fundamental understanding of chemical bonding in BIOX NPs in this work may lead to sustainable synthesis of a wide variety of doped BIOX materials with desired properties.

### Methods
#### Simulation methods.
In our QMD simulations, the electronic states were calculated using projector augmented-wave method within a framework of spin-polarized density functional theory, in which the generalized gradient approximation was used for the exchange-correlation energy⁴⁸⁴⁹. To consider the on-site Coulomb repulsion among the localized electrons, the DFT + $U$ method was employed with $U_{\text{eff}} = 4.00$ eV for Fe $3d$ electrons⁵⁰. The plane-wave cutoff energies were 25 and 250 Ry for the electronic pseudo-wave functions and pseudo-charge density, respectively. Projector functions were generated for the $3d$, $4s$, and $4p$ states of Fe, $2s$ and $2p$ states of O, Li and F, and $3s$, $3p$ and $3d$ states of P. The local magnetic moments were taken into account for Fe in the antiferro-magnetic alignment. The equations of motion were numerically integrated with a time step of 1.2 fs in a canonical ensemble. A total of 212 and 215 atoms ($12\text{Fe}_{2}\text{O}_{3}$ and $9\text{Fe}_{2}\text{O}_{3}$-$6\text{SiO}_{2}$, respectively, immersed in $19\text{LiPF}_{6}$) in a cubic supercell with a side length of $L = 18.26$ Å was thermalized at 500 K to enhance the mobility of Li ions. The periodic boundary conditions were applied in all directions. The $\Gamma$ point was used for Brillouin zone sampling for electronic structure calculation. The total simulation time was 7.986 ps. We reproduced the lithiation and delithiation processes by injecting and eliminating electrons for the supercell, respectively. We used a uniform background charge, with a total charge number of $Q = 0$ from simulation time $t = 0$ ps to 1.331 ps, $Q = 18$ from $t = 1.331$ ps to 6.655 ps, and $Q = 0$ again from $t = 6.655$ ps to 7.986 ps. The interatomic distances of F to F in $\text{PF}_{6}{}^{-}$ unit structures are constrained from $t = 1.331$ ps to avoid disintegration of $\text{PF}_{6}{}^{-}$.

#### Experimental methods.
The 2Fh sample was prepared by the method of Smith *et al.*⁵¹, and the Si-doped 2Fh samples were prepared by modifying the Smith's method in the following manner: First, 20 g of $\text{Fe(NO}_{3}\text{)}_{3}\bullet9\text{H}_{2}\text{O}$ (Nacalai Tesque, 99.0%) was crushed to a fine powder by an alumina mortar and pestle and dissolved in 10 mL of 2-propanol (Nacalai Tesque, 99.0%). Subsequently, an appropriate amount of tetraethyl orthosilicate (Nacalai Tesque 95.0%) was added to the solution. The Si concentration, $x = \text{Si}/(\text{Si} + \text{Fe})$, was adjusted to $x = 0$–0.5 in increments of 0.1. Then, about 48 g of $\text{NH}_{4}\text{HCO}_{3}$ (Nacalai Tesque 96.0%) was added to the solution and mixed using an alumina pestle until the rate of $\text{CO}_{2}$ generation became slow enough and a thick, red ocher paste formed. The obtained paste was moved to a polytetrafluoroethylene beaker and left for 6–12 h at room temperature to complete the reaction. Finally, the paste was washed with ~2 L of distilled water and ~200 mL of ethanol and dried under vacuum for 2 days at room temperature.

### References
1. Keten, S., Xu, Z. P., Ihle, B. & Buehler, M. J. Nanoconfinement controls stiffness, strength and mechanical toughness of beta-sheet crystals in silk. *Nat. Mater.* **9**, 359–367, https://doi.org/10.1038/Nmat2704 (2010).
2. Emerson, D., Fleming, E. J. & McBeth, J. M. Iron-Oxidizing Bacteria: An Environmental and Genomic Perspective. *Annu. Rev. Microbiol.* **64**, 561–583, https://doi.org/10.1146/annurev.micro.112408.134208 (2010).
3. Banfield, J. F., Welch, S. A., Zhang, H. Z., Ebert, T. T. & Penn, R. L. Aggregation-based crystal growth and microstructure development in natural iron oxyhydroxide biomineralization products. *Science* **289**, 751–754, https://doi.org/10.1126/science.289.5480.751 (2000).
4. Sakimoto, K. K., Wong, A. B. & Yang, P. D. Self-photosensitization of nonphotosynthetic bacteria for solar-to-chemical production. *Science* **351**, 74–77, https://doi.org/10.1126/science.aad3317 (2016).
5. Takeda, M. *et al.* Solubilization and structural determination of a glycoconjugate which is assembled into the sheath of Leptothrix cholodnii. *Int. J. Biol. Macromol.* **46**, 206–211, https://doi.org/10.1016/j.ijbiomac.2009.12.006 (2010).

6. Emerson, D. *et al.* Comparative genomics of freshwater Fe-oxidizing bacteria: implications for physiology, ecology, and systematics. *Front. Microbiol.* **4**, 1–17, https://doi.org/10.3389/fmicb.2013.00254 (2013).

7. Dong, H. L., Jaisi, D. P., Kim, J. & Zhang, G. X. Microbe-clay mineral interactions. *Am. Mineral.* **94**, 1505–1519, https://doi.org/10.2138/am.2009.3246 (2009).

8. Marsili, E. *et al.* Shewanella secretes flavins that mediate extracellular electron transfer. *Proc. Natl. Acad. Sci. USA* **105**, 3968–3973, https://doi.org/10.1073/pnas.0710525105 (2008).

9. Hedrich, S., Schlomann, M. & Johnson, D. B. The iron-oxidizing proteobacteria. *Microbiology* **157**, 1551–1564, https://doi.org/10.1099/mic.0.045344-0 (2011).

10. Wedepohl, K. H. The composition of the continental-crust. *Geochim. Cosmochim. Acta* **59**, 1217–1232, https://doi.org/10.1016/0016-7037(95)00038-2 (1995).

11. Harder, E. C. *Iron-depositing Bacteria and Their Geologic Relations.* Vol. 113 (US Geological Survey, 1919).

12. Hashimoto, H. *et al.* Amorphous structure of iron oxide of bacterial origin. *Mater. Chem. Phys.* **137**, 571–575, https://doi.org/10.1016/j.matchemphys.2012.10.002 (2012).

13. Hashimoto, H. *et al.* Bacterial nanometric amorphous fe-based oxide: a potential lithium-ion battery anode material. *ACS Appl. Mater. Interfaces* **6**, 5374–5378, https://doi.org/10.1021/am50905y (2014).

14. Sakuma, R. *et al.* High-rate performance of a bacterial iron-oxide electrode material for lithium-ion battery. *Mater. Lett.* **139**, 414–417, https://doi.org/10.1016/j.matlet.2014.10.126 (2015).

15. Kunoh, T., Kunoh, H. & Takada, J. Perspectives on the Biogenesis of Iron Oxide Complexes Produced by Leptothrix, an Iron-oxidizing Bacterium and Promising Industrial Applications for their Functions. *J. Microbial Biochem. Technol.* **7**, 419–426, https://doi.org/10.4172/1948-5948.1000249 (2015).

16. Schrofel, A. *et al.* Applications of biosynthesized metallic nanoparticles - A review. *Acta Biomater.* **10**, 4023–4042, https://doi.org/10.1016/j.actbio.2014.05.022 (2014).

17. Cao, K. *et al.* 3D hierarchical porous α-Fe2O3 nanosheets for high-performance lithium-ion batteries. *Adv. Energy Mater.* **5**, 1401421, https://doi.org/10.1002/aenm.201401421 (2015).

18. Goriparti, S. *et al.* Review on recent progress of nanostructured anode materials for Li-ion batteries. *J. Power Sources* **257**, 421–443, https://doi.org/10.1016/j.jpowsour.2013.11.103 (2014).

19. Koo, B. *et al.* Hollow iron oxide nanoparticles for application in lithium ion batteries. *Nano Lett.* **12**, 2429–2435, https://doi.org/10.1021/nl3004286 (2012).

20. Owusu, K. A. *et al.* Low-crystalline iron oxide hydroxide nanoparticle anode for high-performance supercapacitors. *Nat. Commun.* **8**, 14264, https://doi.org/10.1038/ncomms14264 (2017).

21. Zhang, L., Wu, H. B. & Lou, X. W. Iron-oxide-based advanced anode materials for lithium-ion batteries. *Adv. Energy Mater.* **4**, 1300958, https://doi.org/10.1002/aenm.201300958 (2014).

22. Luo, J. *et al.* Three-dimensional graphene foam supported Fe3O4 lithium battery anodes with long cycle life and high rate capability. *Nano Lett.* **13**, 6136–6143, https://doi.org/10.1021/nl403461n (2013).

23. Wei, W. *et al.* 3D graphene foams cross-linked with pre-encapsulated Fe3O4 nanospheres for enhanced lithium storage. *Adv. Mater.* **25**, 2909–2914, https://doi.org/10.1002/adma.201300445 (2013).

24. Zheng, S. *et al.* Transition-Metal (Fe, Co, Ni) Based Metal-Organic Frameworks for Electrochemical Energy Storage. *Adv. Energy Mater.* **7**, 1602733, https://doi.org/10.1002/aenm.201602733 (2017).

25. Kou, T., Yao, B., Liu, T. & Li, Y. Recent advances in chemical methods for activating carbon and metal oxide based electrodes for supercapacitors. *J. Mater. Chem. A* **5**, 17151–17173, https://doi.org/10.1039/c7ta05003h (2017).

26. Li, B. *et al.* Ultrathin Nickel–Cobalt Phosphate 2D Nanosheets for Electrochemical Energy Storage under Aqueous/Solid-State Electrolyte. *Adv. Funct. Mater.* **27**, 1605784, https://doi.org/10.1002/adfm.201605784 (2017).

27. Li, X. *et al.* Nitrogen-Doped Cobalt Oxide Nanostructures Derived from Cobalt–Alanine Complexes for High-Performance Oxygen Evolution Reactions. *Adv. Funct. Mater.* **28**, 1800886, https://doi.org/10.1002/adfm.201800886 (2018).

28. Xiao, X. *et al.* Facile synthesis of ultrathin Ni-MOF nanobelts for high-efficiency determination of glucose in human serum. *J. Mater. Chem. B* **5**, 5234–5239, https://doi.org/10.1039/c7tb00180k (2017).

29. Zhu, J. *et al.* Porous and Low-Crystalline Manganese Silicate Hollow Spheres Wired by Graphene Oxide for High-Performance Lithium and Sodium Storage. *ACS Appl. Mater. Interfaces* **9**, 24584–24590, https://doi.org/10.1021/acsami.7b06088 (2017).

30. Guo, X., Zhang, G., Li, Q., Xue, H. & Pang, H. Non-noble metal-transition metal oxide materials for electrochemical energy storage. *Energy Storage Mater.* **15**, 171–201, https://doi.org/10.1016/j.ensm.2018.04.002 (2018).

31. Xu, Y. *et al.* Prussian blue and its derivatives as electrode materials for electrochemical energy storage. *Energy Storage Mater.* **9**, 11–30, https://doi.org/10.1016/j.ensm.2017.06.002 (2017).

32. Zhao, D., Xie, D., Liu, H., Hu, F. & Wu, X. Flexible α-Fe₂O₃ nanorod electrode materials for sodium-ion batteries with excellent cycle performance. *Funct. Mater. Lett.* Online Ready, https://doi.org/10.1142/S1793604718400027 (2018).

33. Hashimoto, H. *et al.* Bio-inspired 2-line ferrihydrite as a high-capacity and high-rate-capability anode material for lithium-ion batteries. *J. Power Sources* **328**, 503–509, https://doi.org/10.1016/j.jpowsour.2016.08.037 (2016).

34. Poizot, P., Laruelle, S., Grugeon, S., Dupont, L. & Tarascon, J. M. Nano-sized transition-metaloxides as negative-electrode materials for lithium-ion batteries. *Nature* **407**, 496–499, https://doi.org/10.1038/35035045 (2000).

35. Furusawa, H. *et al.* Biogenous iron oxide (L-BIOX) as a high capacity anode material for lithium ion batteries. *Electrochim. Acta* **281**, 227–236, https://doi.org/10.1016/j.electacta.2018.05.171 (2018).

36. Mou, W. W., Hattori, S., Rajak, P., Shimojo, F. & Nakano, A. Nanoscopic mechanisms of singlet fission in amorphous molecular solid. *Appl. Phys. Lett.* **102**, 173301, https://doi.org/10.1063/1.4795138 (2013).

37. King, S. V. Ring Configurations in a Random Network Model of Vitreous Silica. *Nature* **213**, 1112–1113, https://doi.org/10.1038/2131112a0 (1967).

38. Franzblau, D. S. Computation of ring statistics for network models of solids. *Phys. Rev. B* **44**, 4925, https://doi.org/10.1103/PhysRevB.44.4925 (1991).

39. Stixrude, L. & Bukowinski, M. S. T. Rings, topology, and the density of tectosilicates. *Am. Mineral.* **75**, 1159–1169 (1990).

40. Ryuo, E., Wakabayashi, D., Koura, A. & Shimojo, F. Ab initio simulation of permanent densification in silica glass. *Phys. Rev. B* **96**, 054206, https://doi.org/10.1103/PhysRevB.96.054206 (2017).

41. Mulliken, R. S. Electronic Population Analysis on Lcao-Mo Molecular Wave Functions. 2. Overlap Populations, Bond Orders, and Covalent Bond Energies. *J. Chem. Phys.* **23**, 1841–1846, https://doi.org/10.1063/1.1740589 (1955).

42. Zhao, K. J. *et al.* Lithium-assisted plastic deformation of silicon electrodes in lithium-ion batteries: a first-principles theoretical study. *Nano Lett.* **11**, 2962–2967, https://doi.org/10.1021/nl201501s (2011).

43. Yan, N. *et al.* Hollow Porous SiO₂ nanocubes towards high-performance anodes for lithium-ion batteries. *Sci. Rep.* **3**, 1568, https://doi.org/10.1038/srep01568 (2013).

44. Favors, Z. *et al.* Stable cycling of SiO2 nanotubes as high-performance anodes for lithium-ion batteries. *Sci. Rep.* **4**, 4605, https://doi.org/10.1038/srep04605 (2014).

45. Tu, J. *et al.* Straightforward approach toward SiO₂ nanospheres and their superior lithium storage performance. *J. Phys. Chem. C* **118**, 7357–7362, https://doi.org/10.1021/jp5011023 (2014).

46. Ishihara, H. *et al.* Silicon-rich, iron oxide microtubular sheath produced by an iron-oxidizing bacterium, *leptothrix* sp. strain OUMS1, in culture. *Minerals* **4**, 565–577, https://doi.org/10.3390/min4030565 (2014).

47. Kunoh, T. *et al.* Biosorption of metal elements by exopolymer nanofibrils excreted from Leptothrix cells. *Water Res.* **122**, 139–147, https://doi.org/10.1016/j.watres.2017.05.003 (2017).

48. Blochl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B* **50**, 17953–17979, https://doi.org/10.1103/PhysRevB.50.17953 (1994).

49. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* **77**, 3865–3868, https://doi.org/10.1103/PhysRevLett.77.3865 (1996).

50. Cava, C. E., Roman, L. S. & Persson, C. Effects of native defects on the structural and magnetic properties of hematite alpha-Fe₂O₃. *Phys. Rev. B* **88**, 045136, https://doi.org/10.1103/PhysRevB.88.045136 (2013).

51. Smith, S. J. *et al.* Novel Synthesis and Structural Analysis of Ferrihydrite. *Inorg. Chem.* **51**, 6421–6424, https://doi.org/10.1021/ic300937f (2012).

### Acknowledgements
The authors are grateful to Profs Y. Takeda and N. Imanishi for pertinent discussions on their XPS analyses. This research was supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, Materials Science and Engineering Division, Grant # DE-SC0018195. The work in Japan was supported by KAKENHI (23104512 and 18H01708) and grant-in-aid for Japan Society for the Promotion of Science research fellows (16J05234). The simulations were performed at the Center for High Performance Computing of the University of Southern California.

### Author Contributions
R.K.K., A.N., F.S., J.T., K.T. and P.V. designed the research. M.M. and S.T. performed simulations. H.H. and S.M. performed experiments. All participated in data analysis and writing the paper.

### Additional Information
Supplementary information accompanies this paper at https://doi.org/10.1038/s41598-019-38540-8.

Competing Interests: The authors declare no competing interests.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812801687319216128_6.jpg)
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2019