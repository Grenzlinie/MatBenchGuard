SPECIAL ISSUE ARTICLE

# Dynamic structure change of Cu nanoparticles on carbon supports for $CO_2$ electro-reduction toward multicarbon products

Qiang Li | Yehui Zhang | Li Shi | Mingliang Wu | Yixin Ouyang | Jinlan Wang ![](./images/812047282798067712_1.jpg)

School of Physics, Southeast University,
Nanjing, China

## Correspondence
Jinlan Wang, School of Physics, Southeast
University, Nanjing 211189, China.
Email: jlwang@seu.edu.cn

## Funding information
National Natural Science Foundation of
China, Grant/Award Numbers: 22033002,
21525311, 21703032; Fundamental
Research Funds for the Central
Universities of China

## Abstract
Cu nanoparticles with different sizes, morphology, and surface structures exhibit distinct activity and selectivity toward $CO_2$ reduction reaction, while the reactive sites and reaction mechanisms are very controversial in experiments. In this study, we demonstrate the dynamic structure change of Cu clusters on graphite-like carbon supports plays an important role in the multicarbon production by combining static calculations and ab-initio molecular dynamic simulations. The mobility of Cu clusters on graphite is attributed to the near-degenerate energies of various adsorption configurations, as the interaction between Cu atoms and surface C atoms is weaker than that of Cu-Cu bonds in the tight cluster form. Such structure change of Cu clusters leads to step-like irregular surface structures and appropriate interparticle distances, increasing the selectivity of multicarbon products by reducing the energy barriers of C-C coupling effectively. In contrast, the large ratio of edge and corner sites on Cu clusters is responsible for the increased catalytic activity and selectivity for CO and $H_2$ compared with Cu(100) surface, instead of hydrocarbon products like methane and ethylene. The detailed study reveals that the dynamic structure change of the catalysts results in roughened surface morphologies during catalytic reactions and plays an essential role in the selectivity of $CO_2$ electro-reduction, which should be paid more attention for studies on the reaction mechanisms.

## KEYWORDS
ab-initio calculations, $CO_2$ electro-reduction reaction, Cu clusters, dynamic structure change, multicarbon products

---

## 1 | INTRODUCTION

The continuous consumption of limited fossil fuels, which plays a dominant role in the structure of energy production and consumption, leads to serious climate and environmental problems, thus the development of reactive and selective technology for the utilization of $CO_2$ by clean energy is highly demanded.¹ In recent

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.
© 2021 The Authors. InfoMat published by UESTC and John Wiley & Sons Australia, Ltd.


years, electrochemical $CO_2$ reduction reaction ($CO_2RR$) have attracted tremendous attention as it presents a promising route to convert $CO_2$ directly into valuable hydrocarbon fuels and chemicals to realize sustainable carbon cycles. $^{2,3}$ For this purpose, products with two or more carbons ($C_{2+}$ products, such as $C_2H_4$, $C_2H_5OH$, $CH_3COO^-$, and $n$-$C_3H_7OH$) is more desirable compared with $C_1$ products (such as $CO$, $HCOOH$, and $CH_4$), due to the high volumetric energy densities and the potential usage as building units for long-chain hydrocarbon fuels and oxygenates. $^{4-6}$

To date, extensive efforts have been devoted to the search and development of catalytic active materials for effective electro-catalytic reduction of $CO_2$, including bulk metals, alloys, metal oxides, and single-atom catalysts. $^{7-10}$ Among all the explored systems, Cu-based catalysts show the unique ability of $CO_2RR$ toward multicarbon products in comparison to other metals. $^{2,11}$ However, Cu-based materials generally suffer from two basic issues, the high over-potential required in the range of $-0.7$ to $-1.2$ V and very poor selectivity that consists of up to 16 different kinds of $C_1$–$C_3$ hydrocarbon and oxygenate products. $^{12}$ Previous results revealed that the activity and selectivity of $CO_2RR$ on Cu-based materials are highly sensitive to the surface structures. $^{13}$ Therefore, various strategies have been applied to modify the physical and chemical properties of Cu-based catalysts and get insight into the factors that affect the $CO_2RR$ reactivity and selectivity, including size, shape, components, defects, and oxidation states. $^{14-17}$ In particular, the preparation of metal nanoparticles (NPs) by screening with different sizes, morphology, and surface area is a common procedure used in experiments to tune the catalytic activity and product selectivity. $^{18}$ For example, Reske et al prepared Cu NP catalysts in the 2–15 nm mean size range, and found that the catalytic activity and selectivity for $H_2$ and $CO$ increased dramatically for small Cu NPs, especially for NPs below 5 nm. $^{19}$ This means that the Cu NPs with a large population of low-coordinated surface sites have no improvement for multicarbon products compared with Cu bulk electrode. In contrast, Baturina et al revealed the carbon-supported Cu NPs tended to be more active toward $C_2H_4$ generation than electrodeposited smooth copper films, and the corners, edges, and defects sites were assumed to be the reactive centers for the C–C coupling. $^{20}$ More recently, the Cu catalysts loaded on carbon frameworks and gas-diffusion layers exposed much improved $C_2$ product selectivity with faradaic efficiency (FE) up to $80\%.^{21,22}$ In addition, Kim et al demonstrated that an ensemble of Cu NPs enabled the formation of $C_2$–$C_3$ products at relative low over-potentials with FE up to $50\%$ ($-0.75$ V), which was attributed to the structural transformation of the Cu NP ensemble to cube-like particles intermixed with smaller NPs. $^{23}$ Apparently, the Cu particle size effect on the activity and selectivity of $CO_2RR$ based on experimental findings is controversial, the understanding of the principles underlining the relations of structure-activity-selectivity on Cu NPs is still lacking. Therefore, it is necessary to identify the reactive centers and corresponding thermodynamic and kinetic paths for different kinds of products, especially for experimentally observed multicarbon products, providing insightful information for C–C coupling process and guiding the design of active and selective $CO_2$ electroreduction catalysts toward multicarbon products.

In this study, the $CO_2RR$ activity of several selected Cu clusters, the carbon support effect, and the dynamic structure change of Cu clusters were systematically investigated by combining static density functional theory (DFT) calculations and ab-initio molecular dynamics (AIMD) simulations. The reaction profiles of $CO_2RR$ on the corner and edge sites of the selected Cu clusters are compared with Cu(100) surface. We demonstrate that the corner and edge sites of small Cu clusters improve the $CO_2RR$ activity toward CO production by low coordinated Cu sites, but the following reduction processes including protonation of CO and C–C coupling still require high energies, suggesting no improvement for multi-step proton-coupled electron transfer (PCET) products comparing with Cu(100) surface. The interface effect between Cu clusters and carbon support is further studied and the key intermediate of *CO does not tend to adsorb on the interface Cu sites. Moreover, the Cu clusters can be located on the graphene by one or a few adsorption sites and various adsorption configurations can exist with similar adsorption energies, thus the dynamic structure change of the clusters on the substrate is identified by AIMD simulations. The structure transformation with surface reconstruction and variation of interparticle interaction can reduce the energy barrier of C–C coupling effectively, and thus is considered as the main cause for improved multicarbon products based on Cu NPs observed from experiments.

## 2 | RESULTS AND DISCUSSION

### 2.1 | Isolated Cu clusters

It is well-known that the "catalytic particle size effect" plays an important role in the reactivity and product selectivity of catalytic reactions. For Cu NPs that are commonly used in electro-reduction experiments, the particle sizes can be in a wide range from 2 to 50 nm, which present large variations of selectivity and activity. $^{19,20,22-24}$ It seems that the size of ~2 nm (~500 atoms)

can be acceptable for DFT-based methods, but the accurate description of reaction intermediates and mechanisms with complicated potential surfaces is severely limited by expensive computational cost. A typical character of NPs, which is different from modeled surfaces, is the presence of large numbers of uncoordinated sites around the corners and edges. Therefore, we focus on these specific reactive sites for the catalytic reaction of $CO_2$ reduction with several small $Cu_n$ clusters, where $n=8,20,38$ (even numbers) and $n=13,55$ (odd numbers). The series of small clusters can reflect the reactivity of Cu NPs by the highly-dense corner and edge sites, and they also represent the facets-like sites as shown in Figure S1. For large clusters, the majority of the surface sites correspond to Cu facets-like sites. The initial structures of the randomly selected clusters are referred to previous reported theoretical studies and further optimized (details see Supporting Information).$^{25,26}$ A reference Cu(100) surface, which shows higher $C_{2+}$ product selectivity comparing with Cu(111), is studied as well.$^{27,28}$

The CHE model is adopted for the reaction free energy calculations along with $CO_2$ reduction processes on Cu clusters and Cu(100) surface with the Eley-Rideal (ER) mechanism, where the protons are from the electrolyte and coupled with the intermediates directly.$^{29}$ The reaction pathway for $CO_2$ reduction toward CO is well established by previous studies and it is commonly accepted that the reduction process proceeds through the intermediate of *COOH, that is, $^*CO_2\rightarrow ^*COOH\rightarrow ^*CO$.$^{30-32}$ However, the following reduction steps are still in debate, the C—C coupling processes can either start from *CO—*CO or proceed with *CO—*CHO, where the *CHO is first generated by $^*CO$.$^{27,28}$ Here, we consider the relative energy barriers of *CO—*CHO coupling since the *CO—*CO is calculated to be a thermodynamically unfavorable process in uncharged conditions.$^{33}$ Besides, we expect that the energy barriers of *CO—*CHO can also reflect the trend for *CO—*CO. Moreover, we intend to obtain relative energies, where the energy barrier of *CO—*CHO for Cu(100) surface is set as a reference value and compares with the energy barriers for Cu clusters.

A full reaction pathway toward $C_2H_4$ production and adsorption structures of the intermediates on model Cu(100) surface and Cu clusters of 38 and 55 can be found in Figures S2-S4. The comparison of the first three PCET process $(H^++e^-)$ and the energy barrier of C—C coupling between Cu(100) and five Cu clusters are displayed in Figure 1. Clearly, the corner Cu atoms from Cu clusters with low coordination numbers show strong binding and activation of $CO_2$, and the increase of free energy from $^*CO_2$ to $^*COOH$ for Cu clusters is much lower than that of pure Cu(100) surface, which agrees with previous studies.$^{34}$ Meanwhile, the binding of CO on Cu clusters is also enhanced by these corner or edge sites, especially for Cu clusters with odd numbers, which have an unpaired electron that makes them chemically more reactive than the even-numbered copper clusters.$^{25}$ In accordance with previous results, the adsorption energies of CO decrease with the increase of Cu cluster size (Figure S5).$^{25}$ The size dependence of adsorption properties of CO is in line with other metals such as Pt and Pd, which can be well understood by the concomitant shift of the metal d-levels.$^{35,36}$ Nevertheless, a strong binding with CO is not equal to a high selectivity of hydrocarbon products. The optimal CO binding strength is estimated to be around −0.6 eV according to the volcano plots based on the Sabatier principle,$^{32,37}$ which makes Cu a promising catalyst for $CO_2RR$ involving multiple (larger than 2) PCET processes. Here, the selected Cu clusters show no obvious improvement for the following processes including $^*CO\rightarrow ^*CHO$ and C—C coupling based on the calculated free energies. It can be seen that several clusters, $Cu_{55}$ for example, can slightly reduce the free energy change from *CO to *COH, but the average value of 0.70 eV for the selected Cu clusters is on the same level as Cu(100) surface of 0.76 eV. Similarly, the energy barriers for *CO—*CHO coupling for Cu clusters remain as high as 0.73 eV on average. Therefore, the isolated Cu NPs with abundant corner and edge sites do not promote the product selectivity for $C_{2+}$ products comparing with Cu surfaces, neither C1 products of $CH_3OH$ and $CH_4$. Similar with the adsorption of *COOH and *CO, the

![](./images/812047282798067712_2.jpg)

**FIGURE 1** Free energy profiles ($\Delta G$) of reaction pathway of $CO_2RR$ to $C_2H_4$ with the first four PCET steps and C—C coupling process (gray shadow) on five selected clusters and extended Cu(100) surface, which is marked as red. An illustrative example of $Cu_{55}$ of intermediate structures is shown on the top and others can be seen in the Supporting Information. PCET, proton-coupled electron transfer

adsorption of *H by the corner and edge sites is enhanced as well (Figure S6), the negative free energy values indicate that the reactive sites can be covered with *H species for HER reaction under high potentials applied in CO₂RR. Therein, the efficiency for the competition reaction of HER is increased by a high ratio of low coordinated sites, as observed experimentally by Reske et al that the reaction products are dominated with H₂ and CO for Cu NPs below 2 nm.¹⁹

## 2.2 | Carbon-supported Cu clusters

It is observed from experiments that carbon-supported Cu NPs are more active toward C₂H₄ generation than Cu films and Cu nano-cubes,²⁰ˢ²³ suggesting that the carbon supports may play an important role in the product selectivity of CO₂RR. To simulate the support effect, only the graphitic crystallite part of the commonly used carbon supports, for example, carbon black and carbon paper, is considered, while the amorphous-like part is neglected.³⁸ Figure S8 illustrates that the layers of graphite have a negligible effect on the adsorption energy of the Cu cluster, thus the simulation model is approximated as Cu clusters supported on a single layer of graphite, that is, graphene (GR).

To illustrate the support effect, we first investigate the interaction between Cu clusters and the substrate. It is expected that the interaction between Cu clusters and GR can be maximized by increasing the contact sites as many as possible, based on which the adsorption models were constructed. Considering Cu₄-graphene as an example, the initial structures of Cu₄ are placed on the graphene support in a flat configuration and a tetrahedron configuration with four and three Cu atoms connecting with GR. However, both initial structures end with a geometry configuration that only one Cu site interacts with C sites from GR after geometry optimization. The results suggest that the Cu—C bonds between the Cu cluster and GR is weaker than the Cu—Cu bonds in tight clusters. Meanwhile, the bonding between GR and Cu cluster can be maximized when the $s$ and $d_{z^2}$ orbitals of the corner sites of Cu cluster are facing with the big conjugating $\pi$ bond of GR (Figure S10), thus the interaction between Cu₄ cluster and GR is limited to one adsorption site. For large clusters of Cu₃₈ and Cu₅₅, the adsorption structures with different numbers of adsorption sites can be obtained and the energy difference between the tested clusters is within ~0.3 eV. Even with one adsorption site, the calculated adsorption energies and electron localization function (ELF) analysis indicate that the binding between Cu and C from the substrate is strong enough to keep the Cu cluster anchoring on the GR surface (Figure 2(B),(C)).

![](./images/812047282798067712_3.jpg)

FIGURE 2 (A) Initial and optimized structures of Cu₄ cluster supported on GR substrate. (B) Calculated adsorption energies of Cu₃₈ (red) and Cu₅₅ (blue) supported on GR with different number of adsorption Cu sites. (C) Left: electron localization function (ELF) map of GR-Cu₃₈, the maximum ELF value between Cu and C is about 0.5, indicating a weak covalent-like nature of the Cu—C bond. Right: charge density difference between Cu₃₈ and GR, the isosurface value is set as 0.005 eV/Å.³ (D) Calculated adsorption energies of CO on several Cu clusters supported on GR at top (red) and interface (blue) sites, respectively. GR, graphene

Therefore, the potential energy surfaces of the hybrid systems contain numerous local minimums with comparable energies. In that case, the adsorption structure of Cu clusters can easily evolve to other configurations as long as one or a few Cu atoms interact with the GR support, which will be shown in the following AIMD simulations.

Figure 2(C) illustrates the charge transfer process that occurs between the Cu cluster and GR support, suggesting that the Cu atoms at the interface and top sites can have different charges and thus influence the adsorption properties of the intermediates during $CO_2RR$. The adsorption energies of CO on the interface and top sites are then calculated and compared, the results clearly show that the top sites are much preferred for the selected clusters. Therefore, the top sites for the following reduction process after CO production are considered as reactive centers. Moreover, a defective GR with a typical 5-8-5 type is also taken into account for the interface effect. It should be noticed that the defective sites tend to be filled by Cu atoms from Cu clusters due to the stronger binding between defective C sites and Cu atoms than Cu-Cu bonds in the cluster form (Figure S11). Still, the adsorption energy of the CO molecule on the top site is higher than the interface site (Figure S12), which is consistent with non-defective GR. $^{26}$ Since the Cu top sites are far away from carbon support, especially for Cu NPs that larger than 15 nm, thus the interface effect between the GR substrate and Cu NPs on the *CO-*COH and C-C coupling processes that proceed on the top sites is expected to be trivial.

### 2.3 | Dynamic structure change

As mentioned above, the GR support can hold Cu clusters with very few adsorption sites, thus the Cu cluster can be mobile on the surface of GR as long as one or a few Cu atoms interacting with the GR substrate. In the following, AIMD simulations are performed to simulate the dynamic structure change of Cu clusters on GR under room temperature of 300 K in aqueous solution. The start geometry is based on optimized structures of GR-Cu clusters, a time-step of 0.5 fs is then simulated to record the trajectories of structure evolutions till we observe several similar or repeat structure movements (~20 ps). Figure 3(A) records the temperature and energy changes with the time evolution in the first 5 ps, which should be long enough as it contains the typical adsorption configurations shown in Figure 2(B). It can be found that the temperature is well-maintained around room temperature and the energies oscillate with various adsorption configurations after a short time variation. The AIMD simulations agree with the results from energy calculations, indicating that the hybrid system contains numerous local minimums with comparable energies. As shown in Figure 3(B) and Videos S1 & S2, the interacting sites of Cu atoms and C sites are varying along with time evolution. Meanwhile, the soft GR substrate undergoes structure deformation along with Cu cluster movement. It should be noted that the AIMD simulations assume that Cu clusters maintain their metallic character along with time change. However, the metallic state of Cu NPs can be only preserved under electro-reduction conditions, otherwise the clusters can be easily oxidized in water solution and the dynamic behavior of the clusters can be restricted. $^{39}$ Therefore, the supported Cu NPs (in metallic state, $Cu^0$) on carbon materials are expected to be changeable constantly during the $CO_2RR$ process with applied potentials. In fact, the structural transformation of Cu NPs during electro-catalytic reactions captured by AIMD simulations here has also been observed by previous experimental studies. Kim et al found that the densely packed Cu NPs change to cube-like particles mixed together with smaller NPs on the carbon support after electro-catalysis. The agreement between theoretical simulations and experiments indicates that the dynamic structural change during electro-reduction reactions plays an important role in the activity and selectivity of $CO_2RR$, which can be largely affected by the surface structures of Cu NPs.

Next, we investigate how the surface structure change of Cu NPs on carbon support has influence on the selectivity of $CO_2RR$. A common feature of all the structures that recorded from AIMD simulation is that the facet-like Cu atoms on cluster surfaces move up and down along with time evolution, showing irregular surfaces as illustrated by several examples in Figure 3(B). A surface roughness factor is then defined (Figure 3(C)) to illustrate the dynamic fluctuation of the facet-like surface Cu atoms. Obviously, the Cu atoms keep fluctuating and can reach a lift up to 0.6 Å from the initially assigned plane surface, which is defined by three corner Cu atoms. With high and low positions of surface Cu atoms, the flat facet leads to step-like sites, which can promote the C-C coupling process effectively than close-packed surfaces. $^{40}$ Figure 3(D) shows the scanned potential energy curves for CO adsorbed on a pristine Cu atom and shifted Cu atom on Cu(100) surface as a function of the angle of rotation referring to the surface plane of Cu(100). For a shifted Cu atom or an irregular surface, the energy barrier for the CO rotation on the surface is much smaller compared with the pristine Cu(100) surface, thus the possibility of C-C coupling is increased especially under low

![](./images/812047282798067712_4.jpg)

FIGURE 3 (A) Variations of temperatures and energies along with Time steps for AIMD simulations of GR-Cu₅₅, the simulation is performed at 300 K for 5 ps with a Time step of 0.5 fs. (B) Snapshots from AIMD simulations of GR-Cu₅₅ structure, three interface Cu sites are marked as cyan to reveal the dynamic structure change. (C) Surface roughness factor changes of GR-Cu₅₅ along with time evolution, insert illustrates the definition of the factor, see also Figure S13. (D) Scanned potential energy curves for CO adsorbed on pristine Cu(100) surface and shifted surface as a function of the angle of rotation. (E) & (F) Test examples of C—C coupling process based on the structures, which present large Surface roughness, obtained from AIMD simulations. AIMD, ab-initio molecular dynamics; GR, graphene

![](./images/812047282798067712_5.jpg)

FIGURE 4 (A)-(C) Snapshots from AIMD simulations of two Cu₈ clusters adsorbed on GR, the initial distance between two clusters is set to 6.0 Å and a Cu₁₆ cluster is formed after 5 ps. (D)-(F) Test examples of C—C coupling processes based on structures obtained from AIMD simulations with reference to the Cu—Cu distance. AIMD, ab-initio molecular dynamics; GR, graphene

CO coverage condition. Besides, the C—C distance can be shortened due to the nearly free CO rotation, and the energy barrier for C—C coupling is then expected to be smaller than that of flat Cu surfaces. To verify the surface structure-dependent behavior, the energy barriers of *CO and *CHO coupling are determined based on the structures randomly extracted from AIMD trajectories. From several examples (Figure 3(E),(F) and Figure S17), the energy barriers of C—C coupling ranging from 0.25 to 0.55 eV are reduced considerably compared with the reference Cu(100) surface (0.77 eV), suggesting the selectivity of $C_{2+}$ products can be much improved with irregular surfaces by dynamic structure change of Cu NPs.

Since the supported Cu clusters on GR are mobile, the cluster aggregation process is also captured by AIMD simulations. As shown in Figure 4(A)-(C), two isolated Cu clusters with a distance of 6 Å aggregated into one cluster after 5 ps on GR support. For comparison, the two isolated Cu clusters without GR support placed in a periodic box are simulated under the same conditions, and the two clusters keep separated along with time evolution (Figure S18). Therefore, the carbon support plays a key role in the dynamic structure change of Cu clusters. During the aggregation process, the Cu—Cu distance from the two clusters is decreasing, thus the distance between the adsorbed intermediates of *CO and *CHO is varying as well. Therefore, the energy barriers of C—C coupling can be effectively reduced with an appropriate C—C distance as proved by example calculations showed in Figure 4(D)-(F), and the structures are taken from the trajectories of AIMD simulation based on the Cu—Cu distance.

### 2.4 | Discussion

Low coordination sites of NPs, such as corners and edges, are often considered to be the reactive centers for increased activity and selectivity compared with their bulk counterparts. Reske et al assigned the dramatic increase in catalytic activity for small Cu NPs around 2 nm to the high ratio of low-coordinated surface atoms, and the high selectivity of $H_{2}$ and CO is obtained. $^{19}$ As the size grows to 15 nm, the population of Cu facet-like surface atoms increases, forming hydrocarbon products of $CH_{4}$ and $C_{2}H_{4}$. Our calculations and other theoretical studies support the conclusions by free energy calculations of $CO_{2}RR$ on the low-coordinated sites of Cu clusters, the isolated Cu clusters show an improved $H_{2}$ and CO activity while the selectivity for further products is limited, due to large energy consumption for $^{*}CO \to ^{*}COH$ and C—C coupling. Therefore, the reactive sites for deep reduction products are ascribed to surface sites of Cu NPs with high coordination numbers as proposed by Reske et al with the ball models. $^{19}$ Furthermore, we demonstrate that the dynamic structure change of Cu NPs on carbon supports can contribute to the enhanced $C_{2+}$ product selectivity observed experimentally by Cu NPs, $^{20,23}$ as captured and proved by AIMD simulations and C—C energy barrier calculations. Accordingly, the carbon supports play a crucial role in the structural features of the supported Cu NPs, depending on the binding strength between carbon supports and Cu NPs. We have shown that the interaction between graphite and Cu cluster is weaker than the Cu—Cu bonds in the tight cluster form, and the Cu clusters undergo dynamic structure changes on the substrate. Defective sites like 5-8-5 type on graphite are also considered and the reactive C sites have strong interaction with Cu atoms from Cu NPs, thus the defective sites can be filled with Cu atoms and the Cu cluster keeps moving on the GR surface (Figures S11 and S21). Therefore, carbon supports that are mainly composed of graphite or other forms of six-ring carbon structures, carbon black for example, are expected to achieve structure changes of Cu NPs. The results agree with the experiments done by Baturina et al, the carbon-supported Cu NPs were found to be more active toward $C_{2}H_{4}$ generation comparing with electrodeposited smooth copper films and carbon black, single-wall carbon nanotubes, and Ketjen Black were applied. $^{20}$ In contrast, Reske et $al^{19}$ found that the selectivity of methane and ethylene was increasingly suppressed for unsupported Cu NPs. In addition, the interaction between Cu NPs and supports also depends on the experimental procedures, for example, the $O_{2}$ plasma etching may form large or massive defective sites to fix the Cu NPs. Subsequently, the resulting activity and selectivity can be reflected by isolated cluster calculations as shown in Figure 1.

Apart from structure transformation and cluster aggregations as illustrated by AIMD simulations, it was also suggested by experiments that the Cu NPs can also undergo cluster separation processes. $^{23,41}$ However, the realistic systems and experimental environment are extremely complicated, thus approximations have to be adopted to simplify the simulation models and reduce the computational costs. Consequently, the AIMD simulations neglect the abundant adsorbed intermediates and solvent molecules, which may drive the Cu—Cu bond breakage and lead to cluster separation. Therein, only the dynamic surface change and cluster aggregation are determined by AIMD simulations. Alternatively, the cluster separation can be considered as an inverse process of cluster aggregation, both processes can result in appropriate Cu—Cu distance and orientation for C—C coupling, which was proved to be efficient for C—C coupling as shown in Figure 4. Moreover, it was also proposed that

interface contact (either Mott-Schottky or Ohmic), interparticle distance, and local pH have an influence on the product selectivity during $CO_2$ electro-reduction$^{23,42,43}$; further in-depth study of the mechanisms of these factors are needed in future studies.

## 3 | CONCLUSION
In summary, the influence factors including the size effect of Cu clusters, the interface effect between Cu clusters and carbon supports, and the dynamic structure change of the catalysts, on the activity and selectivity of $CO_2$RR have been explored by static energy calculations and dynamic simulations. Our results show that the large ratio of the under-coordinated corner and edge sites on Cu clusters increase the activity for both HER and $CO_2$RR toward CO production, while the selectivity of methane and $C_{2+}$ products is limited. We attribute the increased $C_{2+}$ selectivity to the dynamic structure change of Cu clusters on the carbon supports during $CO_2$RR processes. With the help of AIMD simulations, we are able to provide insight information on the structural transformation of Cu clusters on carbon support, including the surface reconstruction and the cluster aggregation. Such dynamic change of the Cu clusters leads to roughened surface morphology, or step-like surface sites, and proper interparticle distance, which reduce the energy barriers of C-C coupling effectively comparing with Cu(100) surface. Although approximations have to be adopted to simplify the simulation models in this study, the calculated results show a number of consistencies with available experimental data. Therefore, we highlight that the dynamic structure change of the catalysts during catalytic reactions, and the study can provide new perspectives of $CO_2$ conversion to multicarbon products.

## 4 | COMPUTATIONAL DETAILS
All static DFT calculations were carried out by the Vienna ab-initio Simulation Package (VASP),$^{44-46}$ the generalized gradient approximation (GGA) was applied with the functional of Perdew-Burke-Ernzerhof (PBE) functional.$^{47}$ The projector-augmented wave (PAW) method was used to describe the wavefunctions in the core regions,$^{48}$ while the valence wavefunctions were expanded as a linear combination of plane-waves with a cutoff energy of 400 eV. For geometry optimization procedures, the convergence of total energy was set to $10^{-5}$ eV and the Hellmann-Feynman force on each relaxed atom was $<0.02$ eV $\AA^{-1}$. The weak van der Waals interaction was considered by dispersion correction PBE + D3.$^{49,50}$ The Gibbs reaction free energy change of PCET process ($\text{H}^+ + \text{e}^-$) for all the $CO_2$RR elementary steps was calculated based on a simple computational hydrogen electrode (CHE) model proposed by Nørskov et al.,$^{30,51}$ and details with model corrections are listed in the Supporting Information. The solvation effect was incorporated with an implicit model implemented in VASPsol.$^{52,53}$ The climbing image nudged elastic band (NEB) method was employed for the determination of the transition states and the C-C coupling barriers.$^{54,55}$

All the AIMD simulations were performed by the CP2K code with PBE functional, which is consistent with VASP calculations.$^{56,57}$ The valence electrons were described by double-$\zeta$ basis sets of the MOLOPT type and the core parts are represented by Goedecker-Teter-Hutter pseudopotentials, respectively.$^{58,59}$ The dispersion interactions were also taken into account with D3 method by Grimme.$^{49}$ The self-consistent continuum solvation (SCCS) model was adopted to account for the solvation effect.$^{60-62}$ The time step was fixed at 0.5 fs and the temperature maintained at 300 K using a Nosé-Hoover thermostat chain.$^{63}$

## ACKNOWLEDGMENTS
This work is supported by National Natural Science Foundation of China (Grant No. 22033002, 21525311, and 21703032) and the Fundamental Research Funds for the Central Universities of China. The authors thank the computational resources from the Big Data Computing Center of Southeast University and National Supercomputing Center of Tianjin.

## CONFLICT OF INTEREST
The authors declare no conflict of interest.

## ORCID
Jinlan Wang https://orcid.org/0000-0002-4529-874X

## REFERENCES
1. Chu S, Majumdar A. Opportunities and challenges for a sustainable energy future. *Nature*. 2012;488:294-303.
2. Birdja YY, Perez-Gallent E, Figueiredo MC, et al. Advances and challenges in understanding the electrocatalytic conversion of carbon dioxide to fuels. *Nat Energy*. 2019;4:732-745.
3. Ross MB, De Luna P, Li Y, et al. Designing materials for electrochemical carbon dioxide recycling. *Nat Catal*. 2019;2:648-658.
4. Nielsen DU, Hu X-M, Daasbjerg K, Skrydstrup T. Chemically and electrochemically catalysed conversion of $CO_2$ to CO with follow-up utilization to value-added chemicals. *Nat Catal*. 2018;1:244-254.
5. Zheng Y, Vasileff A, Zhou X, et al. Understanding the roadmap for electrochemical reduction of $CO_2$ to multi-carbon

oxygenates and hydrocarbons on copper-based catalysts. *J Am Chem Soc.* 2019;141:7646-7659.

6. Ouyang YX, Shi SL, Bai XW, Li Q, Wang JL. Breaking scaling relations for efficient $CO_2$ electrochemical reduction through dual-atom catalysts. *Chem Sci.* 2020;11:1807-1813.

7. Vasileff A, Xu C, Jiao Y, Zheng Y, Qiao S. Surface and interface engineering in copper-based bimetallic materials for selective $CO_2$ electroreduction. *Chem.* 2018;4:1809-1831.

8. Yuan H, Li Z, Zeng XC, Yang J. Descriptor-based design principle for two-dimensional single-atom catalysts: carbon dioxide electroreduction. *J Phys Chem Lett.* 2020;11:3481-3487.

9. Zhi X, Jiao Y, Zheng Y, Vasileff A, Qiao S-Z. Selectivity roadmap for electrochemical $CO_2$ reduction on copper-based alloy catalysts. *Nano Energy.* 2020;71:104601.

10. Zhao J, Zhao J, Li F, Chen Z. Copper dimer supported on a $C_2N$ layer as an efficient electrocatalyst for $CO_2$ reduction reaction: a computational study. *J Phys Chem C.* 2018;122:19712-19721.

11. Nitopi S, Bertheussen E, Scott SB, et al. Progress and perspectives of electrochemical $CO_2$ reduction on copper in aqueous electrolyte. *Chem Rev.* 2019;119:7610-7672.

12. Kuhl KP, Cave ER, Abram DN, Jaramillo TF. New insights into the electrochemical reduction of carbon dioxide on metallic copper surfaces. *Energ Environ Sci.* 2012;5:7050-7059.

13. Pérez-Gallent E, Marcandalli G, Figueiredo MC, Calle- Vallejo F, Koper MTM. Structure- and potential-dependent cation effects on CO reduction at copper single-crystal electrodes. *J Am Chem Soc.* 2017;139:16412-16419.

14. Gao D, Arán-Ais RM, Jeon HS, Roldan CB. Rational catalyst and electrolyte design for $CO_2$ electroreduction towards multi- carbon products. *Nat Catal.* 2019;2:198-210.

15. Feng X, Jiang K, Fan S, Kanan MW. Grain-boundary-dependent $CO_2$ electroreduction activity. *J Am Chem Soc.* 2015;137:4606-4609.

16. He T, Reuter K, Du A. Atomically dispersed asymmetric Cu-B pair on 2d carbon nitride synergistically boosts the conversion of CO into $C_2$ products. *J Mater Chem A.* 2020;8:599-606.

17. Bai X, Li Q, Shi L, et al. Hybrid $Cu^0$ and $Cu^{x+}$ as atomic interfaces promote high-selectivity conversion of $CO_2$ to $C_2H_5OH$ at low potential. *Small.* 2020;16:e1901981.

18. Li Z, Ji S, Liu Y, et al. Well-defined materials for heterogeneous catalysis: from nanoparticles to isolated single-atom sites. *Chem Rev.* 2020;120:623-682.

19. Reske R, Mistry H, Behafarid F, Roldan Cuenya B, Strasser P. Particle size effects in the catalytic electroreduction of $CO_2$ on Cu nanoparticles. *J Am Chem Soc.* 2014;136:6978-6986.

20. Baturina OA, Lu Q, Padilla MA, et al. $CO_2$ electroreduction to hydrocarbons on carbon-supported cu nanoparticles. *ACS Catal.* 2014;4:3682-3695.

21. Huo Y, Peng X, Liu X, Li H, Luo J. High selectivity toward $C_2H_4$ production over Cu particles supported by butterfly- wing-derived carbon frameworks. *ACS Appl Mater Interfaces.* 2018;10:12618-12625.

22. Dinh C-T, Burdyny T, Kibria MG, et al. $CO_2$ electroreduction to ethylene via hydroxide-mediated copper catalysis at an abrupt interface. *Science.* 2018;360:783-787.

23. Kim D, Kley CS, Li Y, Yang P. Copper nanoparticle ensembles for selective electroreduction of $CO_2$ to $C_2$-$C_3$ products. *Proc Natl Acad Sci U S A.* 2017;114:10560-10565.

24. Li Q, Zhu W, Fu J, et al. Controlled assembly of Cu nanoparticles on pyridinic-N rich graphene for electrochemical reduction of $CO_2$ to ethylene. *Nano Energy.* 2016;24:1-9.

25. Zhang X, Liu J-X, Zijlstra B, et al. Optimum Cu nanoparticle catalysts for $CO_2$ hydrogenation towards methanol. *Nano Energy.* 2018;43:200-209.

26. Lim DH, Jo JH, Shin DY, et al. Carbon dioxide conversion into hydrocarbon fuels on defective graphene-supported Cu nanoparticles from first principles. *Nanoscale.* 2014;6:5087-5092.

27. Garza AJ, Bell AT, Head-Gordon M. Mechanism of $CO_2$ reduction at copper surfaces: pathways to $C_2$ products. *ACS Catal.* 2018;8:1490-1499.

28. Calle-Vallejo F, Koper MT. Theoretical considerations on the electroreduction of CO to $C_2$ species on Cu(100) electrodes. *Angew Chem Int Ed.* 2013;52:7282-7285.

29. Lin W, Stocker KM, Schatz GC. Mechanisms of hydrogen-assisted $CO_2$ reduction on nickel. *J Am Chem Soc.* 2017;139:4663-4666.

30. Peterson AA, Abild-Pedersen F, Studt F, Rossmeisl J, Nørskov JK. How copper catalyzes the electroreduction of carbon dioxide into hydrocarbon fuels. *Energ Environ Sci.* 2010;3:1311-1315.

31. Kortlever R, Shen J, Schouten KJ, Calle-Vallejo F, Koper MT. Catalysts and reaction pathways for the electrochemical reduction of carbon dioxide. *J Phys Chem Lett.* 2015;6:4073-4082.

32. Peterson AA, Nørskov JK. Activity descriptors for $CO_2$ electroreduction to methane on transition-metal catalysts. *J Phys Chem Lett.* 2012;3:251-258.

33. Montoya JH, Shi C, Chan K, Norskov JK. Theoretical insights into a CO dimerization mechanism in $CO_2$ electroreduction. *J Phys Chem Lett.* 2015;6:2032-2037.

34. Dong H, Li Y, Jiang D-E. First-principles insight into electrocatalytic reduction of $CO_2$ to $CH_4$ on a copper nanoparticle. *J Phys Chem C.* 2018;122:11392-11398.

35. Laletina SS, Mamatkulov M, Shor EA, et al. Size-dependence of the adsorption energy of CO on Pt nanoparticles: tracing two intersecting trends by dft calculations. *J Phys Chem C.* 2017;121:17371-17377.

36. Yudanov IV, Genest A, Schauermann S, Freund H-J, Rösch N. Size dependence of the adsorption energy of CO on metal nanoparticles: a DFT search for the minimum value. *Nano Lett.* 2012;12:2134-2139.

37. Kuhl KP, Hatsukade T, Cave ER, et al. Electrocatalytic conversion of carbon dioxide to methane and methanol on transition metal surfaces. *J Am Chem Soc.* 2014;136:14107-14113.

38. Pawlyta M, Rouzaud J-N, Duber S. Raman microspectroscopy characterization of carbon blacks: spectral analysis and structural information. *Carbon.* 2015;84:479-490.

39. Lum Y, Ager JW. Stability of residual oxides in oxide-derived copper catalysts for electrochemical $CO_2$ reduction investigated with $^{18}$O labeling. *Angew Chem Int Ed.* 2018;57:551-554.

40. Liu X, Xiao J, Peng H, et al. Understanding trends in electrochemical carbon dioxide reduction rates. *Nat Commun.* 2017;8:15438.

41. Jung H, Lee SY, Lee CW, et al. Electrochemical fragmentation of $Cu_2O$ nanoparticles enhancing selective C-C coupling from $CO_2$ reduction reaction. *J Am Chem Soc.* 2019;141:4624-4633.

42. Mistry H, Behafarid F, Reske R, et al. Tuning catalytic selectiv- ity at the mesoscale via interparticle interactions. ACS Catal. 2016;6:1075-1080.

43. He T, Kour G, Mao X, Du A. $Cu^{\delta +}$ active sites stabilization through Mott-schottky effect for promoting highly efficient conversion of carbon monoxide into n-propanol. J Catal. 2020;382:49-56.

44. Kresse G, Hafner J. Ab initio molecular dynamics for open-shell transition metals. Phys Rev B. 1993;48:13115-13118.

45. Kresse G, Furthmüller J. Efficiency of ab-initio total energy cal- culations for metals and semiconductors using a plane-wave basis set. Comput Mater Sci. 1996;6:15-50.

46. Kresse G, Furthmüller J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys Rev B. 1996;54:11169-11186.

47. Perdew JP, Burke K, Ernzerhof M. Generalized gradient approximation made simple. Phys Rev Lett. 1996;77:3865-3868.

48. Kresse G, Joubert D. From ultrasoft pseudopotentials to the pro- jector augmented-wave method. Phys Rev B. 1999;59:1758-1775.

49. Grimme S, Antony J, Ehrlich S, Krieg H. A consistent and accurate ab initio parametrization of density functional disper- sion correction (DFT-D) for the 94 elements H-Pu. J Chem Phys. 2010;132:154104.

50. Grimme S, Ehrlich S, Goerigk L. Effect of the damping func- tion in dispersion corrected density functional theory. J Comput Chem. 2011;32:1456-1465.

51. Hammer B, Nørskov JK. Electronic factors determining the reactivity of metal surfaces. Surf Sci. 1995;343:211-220.

52. Mathew K, Sundararaman R, Letchworth-Weaver K, Arias TA, Hennig RG. Implicit solvation model for density-functional study of nanocrystal surfaces and reaction pathways. J Chem Phys. 2014;140:084106.

53. Mathew K, Kolluru VSC, Mula S, Steinmann SN, Hennig RG. Implicit self-consistent electrolyte model in plane-wave density-functional theory. J Chem Phys. 2019;151:234101.

54. Henkelman G, Jónsson H. Improved tangent estimate in the nudged elastic band method for finding minimum energy paths and saddle points. J Chem Phys. 2000;113:9978-9985.

55. Henkelman G, Uberuaga BP, Jónsson H. A climbing image nudged elastic band method for finding saddle points and mini- mum energy paths. J Chem Phys. 2000;113:9901-9904.

56. CP2K developers group under the terms of the GNU General Public Licence; 2015. www.cp2k.org.

57. VandeVondele J, Krack M, Mohamed F, et al. Quickstep: fast and accurate density functional calculations using a mixed gaussian and plane waves approach. Comput Phys Commun. 2005;167:103-128.

58. VandeVondele J, Hutter J. Gaussian basis sets for accurate cal- culations on molecular systems in gas and condensed phases. J Chem Phys. 2007;127:114105.

59. Goedecker S, Teter M, Hutter J. Separable dual-space gaussian pseudopotentials. Phys Rev B. 1996;54:1703-1710.

60. Andreussi O, Dabo I, Marzari N. Revised self-consistent contin- uum solvation in electronic-structure calculations. J Chem Phys. 2012;136:064102.

61. Fattebert J-L, Gygi F. Density functional theory for efficient ab initio molecular dynamics simulations in solution. J Comput Chem. 2002;23:662-666.

62. Yin W-J, Krack M, Li X, Chen L-Z, Liu L-M. Periodic con- tinuum solvation model integrated with first-principles calculations for solid surfaces. Prog Nat Sci. 2017;27:283-288.

63. Li Q, Zhao Y, Guo J, et al. On-surface synthesis: a promising strategy toward the encapsulation of air unstable ultra-thin 2D materials. Nanoscale. 2018;10:3799-3804.

# SUPPORTING INFORMATION
Additional supporting information may be found online in the Supporting Information section at the end of this article.

How to cite this article: Li Q, Zhang Y, Shi L, Wu M, Ouyang Y, Wang J. Dynamic structure change of Cu nanoparticles on carbon supports for $CO_2$ electro-reduction toward multicarbon products. InfoMat. 2021;1-10. https://doi.org/10.1002/inf2.12229