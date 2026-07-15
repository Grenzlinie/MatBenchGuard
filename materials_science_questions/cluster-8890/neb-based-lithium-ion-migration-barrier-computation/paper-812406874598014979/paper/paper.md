![](./images/812406874598014979_1.jpg)

Accepted Article

Title: Optimization of Magnesium-Doped Lithium Metal Anode for
High Performance Lithium Metal Batteries through Modeling and
Experiment

Authors: Peiyuan Gao, Haiping Wu, Xianhui Zhang, Hao Jia, Ju-Myung
Kim, Mark H Engelhard, Chaojiang Niu, Zhijie Xu, Ji-Guang
Zhang, and Wu Xu

This manuscript has been accepted after peer review and appears as an
Accepted Article online prior to editing, proofing, and formal publication
of the final Version of Record (VoR). This work is currently citable by
using the Digital Object Identifier (DOI) given below. The VoR will be
published online in Early View as soon as possible and may be different
to this Accepted Article as a result of editing. Readers should obtain
the VoR from the journal website shown below when it is published
to ensure accuracy of information. The authors are responsible for the
content of this Accepted Article.

To be cited as: Angew. Chem. Int. Ed. 10.1002/anie.202103344

Link to VoR: https://doi.org/10.1002/anie.202103344

WILEY-VCH

# RESEARCH ARTICLE

## Optimization of Magnesium-Doped Lithium Metal Anode for High Performance Lithium Metal Batteries through Modeling and Experiment

Peiyuan Gao, $^{a,\#}$ Haiping Wu, $^{b,\#}$ Xianhui Zhang, $^{b}$ Hao Jia, $^{b}$ Ju-Myung Kim, $^{b}$ Mark H. Engelhard, $^{c}$ Chaojiang Niu, $^{b}$ Zhijie Xu, $^{a}$ Ji-Guang Zhang, $^{b}$ Wu Xu $^{b,}$

| [a] | Dr. P. Y. Gao, Dr. Z. J. Xu<br>Physical and Computational Science Directorate, Pacific Northwest National Laboratory, Richland, Washington 99354, United States. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [b] | Dr. H. P. Wu, Dr. X. H. Zhang, Dr. H. Jia, Dr. J. M. Kim, Dr. C. J. Niu, Dr. J.-G. Zhang, Dr. W. Xu<br>Energy and Environment Directorate, Pacific Northwest National Laboratory, Richland, Washington 99354, United States |
| [c] | Mr. M. H. Engelhard<br>Environmental Molecular Sciences Laboratory, Pacific Northwest National Laboratory, Richland, Washington 99354, United States          |

# These authors contributed equally to this work.
* Corresponding Author. Email: wu.xu@pnnl.gov

Supporting information for this article is given via a link at the end of the document.

**Abstract:** Lithium (Li)-magnesium (Mg) alloy with limited Mg amount, which can also be called Mg-doped Li (Li-Mg), has been considered as a potential alternative anode for high energy density rechargeable Li metal batteries. However, the optimum doping-content of Mg in Li-Mg anode and the mechanism of the improved performance are not well understood. Herein, density functional theory (DFT) calculations are used to investigate the effect of Mg amount in Li-Mg anode. The Li-Mg with about 5 wt.% Mg (abbreviated as Li-Mg5) has the lowest absorption energy of Li, thus all the surface area can be "controlled" by Mg atoms, leading to the smooth and continuous deposition of Li on the surface around the Mg center. A localized high concentration electrolyte enables Li-Mg5 to exhibit the best cycling stability in Li metal batteries with high-loading cathode and lean electrolyte under 4.4 V high-voltage, which is approaching the demand of practical application. This electrolyte also helps generate an inorganic-rich solid electrolyte interphase, which leads to smooth, compact and less corrosion layer on the Li-Mg5 surface. Both theoretical simulations and experimental results prove that Li-Mg5 has optimum Mg content and gives best battery cycling performance. This work also provides an effective approach to identify optimal alloy-type Li metal anodes for improving long-term cycling stability of high-energy-density Li metal batteries.

## Introduction

State-of-the-art lithium (Li)-ion batteries have been widely deployed in applications in mobile electronic devices, electric vehicles and grid energy storage. $^{[1]}$ New electrode materials are still needed to develop high energy densities (in both gravimetric and volumetric), high power, and outstanding cycling performance Li-ion batteries. $^{[2]}$ Graphite is an excellent anode material for long-cycling Li-ion batteries. $^{[3]}$ However, the low theoretical specific capacity $(372mAhg^{-1})$ of graphite anodes has limited the further increase in energy density of Li-ion batteries. Alloy-type anodes have shown much higher theoretical specific capacities than graphite anode in Li-ion batteries. For instance, Tu et al. reported that using a Sn-Li alloy anode could enable high-capacity cycling in both symmetric cells and prototype cells with $LiNi_{0.8}Co_{0.15}Al_{0.05}O_{2}$ (NCA) cathode having a nominal specific capacity of $190mAhg^{-1}^{[4]}$ In addition to Sn, several metals and metalloids including Zn, Al, Si, Ag and Mg have also been investigated as the alloy-type anode materials and achieved largely disparate capacities. $^{[2,5]}$ For instance, many elements like Mg, Ag, Zn and Al have more than double the volumetric capacity of graphite. $^{[5b]}$ However, alloy-type anodes experience huge volume changes in alloying/de-alloying processes during the charge/discharge of Li-ion batteries, leading to short cycle life of the batteries.

To achieve high energy density Li-based batteries, metallic Li has been considered as the ultimate anode material because of its ultrahigh theoretical specific capacity $(3860mAhg^{-1})$ and extremely low redox potential (-3.040 V vs. standard hydrogen electrode). It is also well-known that a solid electrolyte interphase (SEI) layer is formed on the anode surface during the initial cycles. $^{[6]}$ However, the detailed composition, structure and mechanism of the SEI, along with the evolution upon battery cycling, vary a lot depending on many factors (like the component, composition and structure of electrolyte, current density, temperature, pressure, etc.) and still remain a matter of debate. $^{[7]}$ Especially in batteries with Li metal as anode, the high chemical reactivity of Li with electrolyte makes it challenging to form a stable SEI layer, normally resulting in low Li Coulombic efficiency. In addition, the formation and evolution of mossy and/or dendritic Li during repeated Li deposition/stripping processes generate large porous Li structure with high surface area, much electrochemical inactive or "dead" Li and thick and resistive SEI, consume active Li source and deplete electrolyte amount, thus leading to high safety concerns and short cycle life of Li metal batteries. These problems are common challenges faced by Li metal batteries, which have perplexed researchers for decades. Currently, the technology of Li metal anode is still under development. $^{[8]}$

In comparison with metallic Li anode, the alloy anodes show remarkable improvement in stability at the surface and in the bulk during cycling. $^{[9]}$ Mg has been studied extensively as a component in alloys, including the Li-Mg alloy. The enhanced surface stability of Li-Mg alloy can be ascribed to the formation of a robust passivation layer, which can protect the anode from uneven Li deposition, thus reducing the uncontrolled growth of Li

# RESEARCH ARTICLE

dendrites.[¹⁰] According to their binary phase diagram, Li-Mg alloy has large single phase solid solution regions in Li < 5.7 wt.% and > 11 wt.% at room temperature.[¹¹] Since the Li-rich solid solution phase in Li-Mg alloy and the pure Li crystal are both body-centered cubic (BCC) lattice structure, that means the capacity of this alloy can be tuned in a broad range while keeping phase change free. However, in previous studies,[¹²] low rate capability for the lithiation of Mg and low average voltage in Li-Mg alloy were reported when the amount of Mg is very high (> 60 wt.%). In 2019, Kong et al. demonstrated the Li-Mg alloy with 18.6 wt.% Mg to be a very promising anode material for Li||S battery,[¹³] and Choi *et al.* even reported that Li anode doped with a marginal amount of Mg (5.1 wt.%) is able to improve the cycling performance of Li metal battery drastically.[¹⁴] Besides, localized high-concentration electrolytes (LHCEs) enable high voltage Li metal batteries (LMBs) and minimize the Li pulverization due to the unique solvation structure.[¹⁵] Investigation of Li-Mg alloys in LHCEs is a very important topic and will be highly rewarding. Utilizing a Li-Mg alloy with the optimized content of Mg in a proper LHCE will be a very promising way to achieve an excellent performance which beyond the Li metal anode.

In this work, a systematical study of the effect of Mg content in Li-Mg alloy anode with less than 30 wt.% Mg, which is also called Mg-doped Li anode, on the performance of Li metal battery was performed by computational calculations and experimental validation in an LHCE, because computational modeling techniques based on density functional theory (DFT) have been successfully demonstrated for material design in recent years.[¹⁶] First, the surface models of Li-Mg alloy anode with different amounts of doped Mg in Li were built at atomic level. Then, several DFT calculations were performed to examine the absorption energy of Li on the anode. An optimum of Mg content was identified on the absorption energy curve of Li on Li-Mg alloy surface, where its absorption energy is the lowest. Finally, the calculated results were further validated by the cycling performance of batteries using Li or Li-Mg as anode, with high loading (4.2 mAh cm⁻²) LiNi₀.₈Mn₀.₁Co₀.₁O₂ (NMC811) as cathode and lean electrolyte amount (3 g (Ah)⁻¹) of LHCE. And this is the first successful demonstration of Li-Mg anode utilized in a battery with such a high areal capacity and a low amount of electrolyte.

## Results and Discussion

The models of anode surface were built at atomic scale, which are shown in Figure 1. The anode surface model of pure Li and Li doped with Mg were both built for comparison. The Li (100) facet was selected as it is the lowest energy surface.[¹⁴] A thick vacuum layer (>16 Å) was added to form a surface. For the Li-Mg alloys, based on the pure Li model, the center Li atom on the surface was replaced by Mg atom. In all the DFT calculations, the number of Mg atom was fixed as one, and the size of surface area was changed to model the change of Mg content. In DFT calculations it is assumed that the small content of Mg will not change the lattice of Li in plane. In Figure 1c a surface model with 4.5 wt.% Mg is presented as an example. Note that according to the interaction curves between Li atom and Mg atom in the previous work by Choi et al.[¹⁴], the longest interaction distance is about 8 Å. The unit cell length of pure Li crystal is 3.43 Å in our calculations. That means there is no interaction between the Mg atom and the Li atoms on the fourth layer, as their distances is larger than 8 Å. Consequently, the weight percentage of Mg in the DFT calculations is calculated based on three layers of Li atoms. To model the deposition of Li, another Li atom is assumed to be absorbed around the Mg atom in the deposition of Li on Li (100) facet. The absorption energy ($E_{absorption}$) in DFT calculation is defined as following:

$$
E_{absorption}=E_{total}-E_{subsurface}-E_{Li} \tag{1}
$$

where $E_{total}$ is the total energy of the system, $E_{subsurface}$ is the energy of the surface, and $E_{Li}$ is the energy of single Li atom in vacuum.

![](./images/812406874598014979_2.jpg)

**Figure 1.** (a-d) Simulation model of pure Li and Mg-doped Li surface: (a) Front view and (b) top view of pure Li system; (c) Front view and (d) top view of Li-Mg system with 4.5 wt.% Mg doping in Li. Li, purple ball; Mg, green ball. (e, f) Absorption energies of Li atom obtained in DFT calculations on (e) Li (100) facet and (f) Li-Mg alloy with different Mg doping contents.

Figures 1e and 1f show the absorption energies of Li atom on the (100) facet of pure Li and Li-Mg alloy with different Mg doping contents, respectively. The average absorption energy of Li on pure Li is -1.521 eV (Figure 1e). When adding small amount of Mg into Li, the absolute value of absorption energy of Li decreases to -1.586 eV for Mg of about 4.2 wt.% and further to -

1.620 eV for Mg of about 4.5 wt.%. The average difference is about 0.06 eV. That indicates the interaction between Li and Mg atoms is stronger than the interaction between Li and Li atoms. Therefore, the Li atom can be absorbed and grow around Mg center in the deposition process of Li. However, when more Mg is added, the absorption energy of Li on Li-Mg alloy surface goes up and reaches a value of -1.563 eV at Mg content of about 7.0 wt.%. After that, the absorption energy of Li slightly decreases to -1.564 eV at about 12.0 wt.% Mg and -1.572 eV at 24.0 wt.% Mg in the Li-Mg alloy. Therefore, there exists a lowest absorption energy of Li at the content of Mg of about 4.5 wt.% in Li-Mg alloy (or the mole ratio of Li/Mg is 99:1). When the content of Mg is about 4.5 wt.%, all the surface area can actually be "controlled" by Mg atom. So, the nucleation and growth of Li on the surface of Li-Mg alloy with 4.5 wt.% Mg will be smooth and continuous around the Mg center, and this 4.5 wt.% Mg can be considered as the optimum in Li-Mg alloy for good Li deposition.

According to the calculation results, only a small amount of Mg is needed if the distribution of Mg in Li is homogeneous at molecular/atomic level. This mechanism is different from previous studies with high amount of Mg in Li-Mg alloy.¹²,¹⁷ In those cases, as a result of the high Mg content, small Mg-rich hexagonal-close-packed (HCP) domains would be produced in Li metal upon delithiation. The hcp domains on the surface can act as host and a passivation layer when Li atoms insert into the anode. However, the Li dendrite growth cannot be suppressed on the surface area without Mg domains. This effect of two adjacent Mg atoms on the absorption energy of Li is further investigated by DFT calculations. Figure 2 shows that if two Mg atoms are present together on the surface, the absorption energy of Li on the two Mg atoms (E = -1.679 eV) is lower than that on single Mg atom (E = -1.619 eV). Moreover, the Li atom prefers the position of the diagonal center between the two Mg atoms (E = -1.690 eV, Figure 2a) to that of the center between the two side-by-side Mg atoms (E = -1.679 eV, Figure 2b). This means that if the Mg is not well distributed on the surface of Li-Mg alloy, or if the Mg content is high, they may form Mg-Mg atom pairs and such Mg-Mg pairs preferably absorb Li to deposit, then leading to uneven Li deposition on the surface of Li-Mg alloy anode, which makes the Li deposition worse.

![](./images/812406874598014979_3.jpg)

Figure 2. Different configurations of two Mg atoms in (a) diagonal positions and (b) side by side, on Li-Mg alloy surface and the absorption energies of Li.

To further investigate the evolution of the surface chemistry of Li-Mg alloy, several DFT calculations were performed to compute the migration activation energy barrier of Li in the bulk system and on the surface. Previous works have demonstrated the energy of bridge configuration for Li on the Li (100) facet is lower than the top configuration¹⁸ (see Figure S4 for configuration details). Therefore, in this work, only the bridge path, i.e., the hopping mechanism, is investigated as the practical migration pathway. Figure 3 presents the migration pathway schemes and calculated migration energy profiles along the migration pathways. Our calculated diffusion activation energy barrier for Li on the Li (100) facet is 0.074 eV, which is in agreement with previous works across step edges.¹⁸⁻¹⁹ For Li diffusion on Li-Mg alloy surface, two cases are considered. As shown in Figure 3b and 3c, when a Li atom is absorbed around Mg atoms on Li-Mg surface, the Li atom could move around the Mg atom (Figure 3b) or move away from the Mg atom (Figure 3c). Interestingly, as shown in Figure 3f and 3g, these two energy barriers are almost the same. Both are about 1.7 times larger than the energy barrier of Li diffusion on pure Li surface (Figure 3e). The diffusion coefficient of Li can be calculated using the standard diffusion formula.²⁰

$$
D = \lambda^2 v\ exp\left(\frac{E_a}{k_B T}\right) \tag{2}
$$

where $\lambda$ is the jump distance, $v$ is the vibration frequency of the atom, $E_a$ is migration activation energy, $k_B$ is the Boltzmann constant and $T$ is the temperature.

For Li diffusion on the pure Li and Li-Mg alloy surface, the prefactors $\lambda$ and $v$ are the same. By comparison of the diffusion coefficients, we can identify that the diffusion coefficient of Li atom on Li-Mg alloy surface is 5.5 times slower than pure Li surface. That means Li atoms would be trapped by Mg atom when it diffuses on Li-Mg surface, which is helpful to homogenous Li nucleation around Mg atom in early stage of Li plating. Figure 3h shows the energy barrier of Li in bulk Li. It is found that the energy barrier of Li in bulk Li is about three times larger than Li on Li surface, indicating the diffusion of Li is much slower in bulk system. For Li diffusion in Li-Mg bulk, as the interaction between Li and Mg is stronger, higher energy barrier can be expected.

Based on the simulation results, two commercially available Li-Mg alloy anodes with Mg content of 5 wt.% (noted as Li-Mg5, which is close to the theoretical optimum content of Mg 4.5 wt.%) and 10 wt.% (noted as Li-Mg10) were investigated. The long-term cyclability of Li-Mg alloy was first evaluated using Li-Mg||Li-Mg symmetric cells, compared with Li||Li symmetric cells. The cycling performance of the symmetric cells with a cycling capacity of 1 mAh cm⁻² at a current density of 0.5 mA cm⁻² for each plating/stripping process is shown in Figure S1. The Li||Li cell with a localized high-concentration electrolyte (LHCE) of 1.49 M lithium bis(trifluorosulfonyl)imide (LiFSI) in 1,2-dimethoxyethane (DME) and 1,1,2,2-tetrafluoro-2,2,3,3-tetrafluoropropyl ether (TTE) (DME/TTE = 1:3 by mol.) has the largest polarization (~24 mV). In contrast, the Li-Mg5||Li-Mg5 cell and Li-Mg10||Li-Mg10 cell show lower polarization of 19 mV and 15 mV, respectively. This is consistent with the previous result that Li-Mg alloy has a better lithiophilicity as the enthalpy of infinite solution ($\Delta_{sol}H^\circ$) of the Li metal into the Li-Mg alloy is negative.²¹ $\Delta_{sol}H^\circ$ describes the driving force for their atomic mixing. A negative $\Delta_{sol}H^\circ$

RESEARCH ARTICLE

![](./images/812406874598014979_4.jpg)

Figure 3. Schematic illustration and migration energy profiles of Li atom in bulk and on surface of pure Li and 4.5 wt.% Li-Mg alloy. (a) Migration scheme of Li on Li surface, (b) migration scheme of Li on Li-Mg alloy surface (towards Mg atom), (c) migration scheme of Li on Li-Mg alloy surface (away from Mg atom), (d) migration scheme of Li in Li bulk, (e) migration energy profile of Li on Li surface, (f) migration energy profile of Li on Li-Mg alloy surface (towards Mg atom), (g) migration energy profile of Li on Li-Mg alloy surface (away from Mg atom), and (h) migration energy profile of Li in Li bulk. Li, purple ball; Mg, green ball. The initial and final positions of Li are highlighted as 1 and 2. Note that the migration scheme in bulk system is in cross-section view.

indicates an improved electrochemical wetting and correspondingly low plating overpotential.

The electrochemical performance of the two Li-Mg alloys was further evaluated in Li-Mg||NMC811 coin cells, with the comparison to the pure Li anode in Li||NMC811 cells. Cells with a medium-high loading of 1.3 mAh cm² NMC811 cathode, a thick Li and Li-Mg anodes (500 µm) and an excess electrolyte (75 µL) of LHCE were first assembled and tested. As shown in Figure 4a, the charge/discharge voltage profiles of the cells in the first formation cycle at C/10 rate (where 1C = 1.3 mA cm⁻²) in the voltage range of 2.8-4.4 V are very similar when different anodes are used. The initial Coulombic efficiencies of pure Li, Li-Mg5 and Li-Mg10 are 86.4, 88.2 and 87.9%, respectively. After 200 cycles at 1C rate under room temperature, the capacity retention of the Li||NMC811 cell is 86.9% (Figure 4b). After that, the cell cycling efficiency decreases and varies extensively. On the contrary, the Li-Mg10||NMC811 cell shows a continuously faster capacity fading, with only 75.0% of the initial capacity after 200 cycles or 69.0% capacity retention after 220 cycles. Actually, the cell cycling efficiency drops quickly after 100 cycles. As for Li-Mg5||NMC811 cell, a great enhancement of cycling performance is achieved with 91.4% of the initial capacity after 200 cycles or 85.5% capacity retention even after 280 cycles. After 280 cycles, the cell cycling efficiency and the cell capacity drop quickly. Therefore, the anode cycling stability follows the order as: Li-Mg5 > Li > Li-Mg10. From the above DFT calculation results, it is known that about 5 wt.% Mg in Li-Mg alloy can well "control" the deposition of Li on anode. When the ratio achieved 10 wt.%, more Li atoms on the surface will be replaced by Mg atoms, then more Mg-Mg atom pairs may be formed. Furthermore, as indicated by the above calculations in Figure 2, Li is preferably absorbed by the Mg-Mg pair. That will make the deposition of Li uneven on the surface of Li-Mg10 alloy anode. Therefore, the interphase layer may be not so compact for Li-Mg10.

The relationship between the anode/electrolyte interphase and the cycling stability was further investigated with scanning electron microscopy (SEM) and X-ray photoelectron spectroscopy (XPS). The surface of the pure Li metal after 225 cycles is porous (Figure 5a). The cross-section image shows that the corrosion layer is around 49 µm with porous structures (Figure 5b). The Li-Mg5 has smooth and dense surface after 290 cycles (Figure 5c) and the corrosion layer on Li-Mg5 is only 32 µm (Figure 5d), which is much thinner than that of pure Li metal. The Li-Mg10 shows a rough surface (Figure 5e) and has a thin corrosion layer thickness (Figure 5f). The latter phenomenon can be explained as below: Due to the very fast capacity decay after 100 cycles, the utilization of Li in Li-Mg10 in each cycle is largely reduced compared to the cells with pure Li and Li-Mg5, thus the possible corrosion to Li-Mg10 during cycling test is limited and then it shows a thin corrosion layer on the anode surface.


![](./images/812406874598014979_5.jpg)

Figure 4. (a) Voltage profiles of the first charge/discharge cycle at C/10 rate and (b) cycling performance of Li||NMC811 cells and Li-Mg||NMC811 cells with 1.3 mAh cm⁻² NMC811 cathode and excess electrolyte of 75 μL at 1C rate, in the voltage window is 2.8-4.4 V at 25 °C. The batteries were tested at 1C for both charge and discharge after two formation cycles at C/10, where 1C = 1.3 mA cm⁻².

![](./images/812406874598014979_6.jpg)

Figure 5. (a-f) SEM images of (a b) Li metal, (c d) Li-Mg5, (e f) Li-Mg10 after cycling test with excess electrolyte of 75 μL. (g) Atomic ratios of different elements tested by XPS on cycled Li-Mg5 and Li-Mg10. (h) XPS of selected elements for cycled Li-Mg5 and Li-Mg10.

RESEARCH ARTICLE

The SEIs of different anodes were further characterized with XPS. The SEI of Li-Mg5 has the atomic ratio of Li 31.30%, C 12.11%, N 2.56%, O 44.65%, F 4.66% and S 4.59% (Figure 5g). The SEI of Li-Mg10 has the atomic ratio of Li 42.88%, C 12.97%, N 1.84%, O 33.83%, F 4.92% and S 3.38%. They both have high contents of Li and O and low content of C, indicating inorganic-rich SEIs formed on Li-Mg5 and Li-Mg10 anode surfaces. The atomic ratio is similar to the result of the pure Li metal in our previous study. $^{[22]}$ As indicated by Figure 5h, for C 1s spectra, the main difference is that the SEI on Li-Mg5 has more signal of $CO_{3}^{2-}$, which can be assigned to $Li_{2}CO_{3}$. F 1s spectra show that the main fluorine (F)-containing species is LiF in the SEIs on Li-Mg5 (91.3% of F-containing species) and Li-Mg10 (94.6% of F-containing species). The pure Li metal in the same electrolyte in our previous study showed similar F 1s spectra. $^{[22]}$ They all indicate the critical effect of the reduction of LiFSI salt. O 1s spectra of Li-Mg10 is similar to that of pure Li metal and they both have the signal of $Li_{2}O$, while Li-Mg5 doesn't have $Li_{2}O$. Li-Mg5 and Li-Mg10 have similar S 2p spectra and they have lower amount of $Li_{2}S$ compared with pure Li metal. $^{[22]}$ Overall, the SEI on Li-Mg5 contains more $Li_{2}CO_{3}$ and less $Li_{2}O$ than that of Li-Mg10, which probably improves the stability of the SEI and is beneficial for the cycling performance. This result suggests that the content of Mg in Li-Mg not only affects the Li deposition behavior but also influences the composition of the SEI.

On the cycled cathode surfaces, the atomic ratios of different elements tested by XPS for Li-Mg5||NMC811 and Li-Mg10||NMC811 cells are shown in Figure S2. There are less Li and more C in the NMC811 surface from the Li-Mg5 cell, when compared to those from the Li-Mg10 cell, while the other elements (N, O, F and S) have similar contents. There are apparent signals of LiF, S-F and $SO_{x}$ species (Figure S3) from salt anion decomposition, indicating the reactions of the LiFSI salt on the cathodes. A main difference between O 1s spectra of NMC811 of Li-Mg5||NMC811 and Li-Mg10||NMC811 is that NMC811 of Li-Mg10||NMC811 has a higher amount of M-O, indicating that there is more dissolution of transition metal ions on NMC811 in Li-Mg10||NMC811 cell. This result suggests that the cathode electrolyte interphase (CEI) of NMC811 of Li-Mg5||NMC811 has better protection of the cathode, which is another reason of stable cycling performance of Li-Mg5||NMC811 cell at a high cutoff voltage.

![](./images/812406874598014979_7.jpg)

Figure 6. (a) Cycling performances of Li||NMC811 cells and Li-Mg||NMC811 cells with two Mg-doped Li anodes (Li-Mg5 and Li-Mg10), 4.2 mAh cm⁻² NMC811 cathode, and lean electrolyte at 14 μL. Voltage window is 2.8~4.4 V. The batteries were tested at C/3 charge and discharge after two formation cycles at C/10. Voltage profiles as a function of cycle number of (b) Li||NMC811 cell, (c) Li-Mg5||NMC811 cell and (d) Li-Mg10||NMC811 cell.

In order to evaluate the battery cycling performance under conditions close to practical applications, the NMC811 cathode with a high areal capacity loading (4.2 mAh cm⁻²) and the electrolyte with lean amount at electrolyte/capacity ratio of 3 g (Ah)⁻¹ (or 14 μL in each coin cell where the cathode disk had a diameter of 1.27 cm) were used to assemble the coin cells. As shown in Figure 6a, the Li||NMC811 cell cycled at C/3 rate (where 1C = 4.2 mA cm⁻²) remains 80% of its initial capacity after 130

cycles and then exhibits a fast capacity decay. An increased cell overpotential during cycling can be observed (Figure 6b). The Li- Mg5||NMC811 cell shows a greatly improved cycling stability, having a 80% capacity retention after 171 cycles. There is only a small cell overpotential increase during cycling (Figure 6c). When further increasing the Mg content to 10 wt.% in the Li-Mg alloy anode, the Li-Mg10||NMC811 cell actually demonstrates the poorest cycling stability and shortest cycle life. The capacity decreases to 80% of the initial value only after 83 cycles and then quickly drops to zero. Meanwhile, there is a large increase in overpotential with cycling (Figure 6d). This is possibly attributed to the accumulation of resistive film on Li-Mg10 surface. The cycling stability follows the same trend as the cells with a lower areal capacity and an excess electrolyte which are shown in Figure 6: Li-Mg5 > Li > Li-Mg10, although it's more challenging to test LMBs with a high loading cathode and a lean electrolyte. The cycling performance results indicate that the Li-Mg5/electrolyte interphase layer is probably more compact and well maintained compared to those formed on Li-Mg10 and pure Li. Although macroscopic phase separation will not occur for Li-Mg10 alloy, the distribution of Mg in Li-Mg alloy may not be uniform at molecular level.

In order to evaluate the morphology of anodes after cycling test in practical conditions, SEM images of cycled Li metal and Li- Mg alloys were tested. There are cracks and irregular deposits on Li metal surface (Figure 7a). Li-Mg10 surface is very rough and porous with large size fiber-like structures (Figure 7e). In sharp contrast, the surface of Li-Mg5 is very flat and dense (Figure 7c).

This is consistent with the prediction from the simulation that Li growth on Li-Mg alloy with 5 wt.% Mg will be smoothly continuous. As shown in Figure 7d, the cross-sectional image of Li-Mg5 shows a corrosion layer with an average thickness of 67 µm, indicating a denser and more uniform Li deposition than pure Li metal that has a corrosion layer of about 89 µm thick. This is consistent with the DFT result as well. Therefore, Li has a denser deposition on Li-Mg5 alloy. For Li-Mg10, it has a corrosion layer of about 61 µm thick (Figure 7f). Considering the short cycle life of Li- Mg10||NMC811 cell, which only stably cycled around 80 cycles and then the capacity dropped quickly to zero, the total utilization of Li in Li-Mg10 should be very limited compared to those in pure Li and Li-Mg5. Therefore, it is reasonable that its corrosion layer is thinner than those of pure Li and Li-Mg5. However, if we assume that the corrosion layer on pure Li or Li-Mg alloy is mainly generated during the effective cycles before the capacity reaches the 80% retention, then the average thickness growth rate of the corrosion layer is 0.68 µm per cycle for pure Li, 0.39 µm per cycle for Li-Mg5, and 0.73 µm per cycle for Li-Mg10 in the tested electrolyte. It is demonstrated that about 5 wt.% Mg in Li-Mg alloy does show improved Li deposition/stripping behavior or Li protection in batteries. More or less Mg content than this value actually adversely influences the Li deposition/stripping behavior and the battery cycling stability.

![](./images/812406874598014979_8.jpg)

Figure 7. SEM images top-view (a, c, e) and cross-sectional view (b, d, f) of Li metal (a and b), Li-Mg5 (c and d), Li-Mg10 (e and f) after cycling test in Figure 6.

## Conclusion
We have utilized DFT calculations to investigate the effect of Mg doping in Li-Mg alloy on the cycling stability of batteries using Li-Mg alloy with different Mg doping amounts. The differences in Li-Mg alloy can be explained in terms of absorption energy of Li on Li-Mg or pure Li surface. An optimum content of 4.5-5 wt.% Mg can lead to the lowest absorption energy and the smoothly continuous deposition of Li on the surface around the Mg center. The battery cycling performance tests are consistent with the DFT results. Li-Mg5||NMC811 cell has demonstrated a capacity retention of 80% after 171 cycles under a stringent condition of high-voltage (4.4 V), high-loading cathode (4.2 mAh cm⁻²), lean electrolyte (E/C ratio of 3 g (Ah)⁻¹), and relatively high cycling rate (C/3 or 1.4 mA cm⁻²). The findings in this study suggest that Li metal with marginal Mg doping content (about 5 wt.%) is a promising candidate that may substitute pure Li metal in Li metal batteries to enhance their long cycling stability and higher rate capability. This work through theoretical simulations and experimental validation also sheds light in developing effective and optimal alloying-type Li metal anodes to achieve long-term cycle life of high-energy-density Li metal batteries.

## Acknowledgements
This work was supported by the Assistant Secretary for Energy Efficiency and Renewable Energy, Vehicle Technologies Office, of the U.S. Department of Energy through the Advanced Battery Materials Research (BMR) program under Contract No. DE-AC05-76RL01830. The SEM and XPS characterizations were conducted in the William R. Wiley Environmental Molecular Sciences Laboratory (EMSL), a national scientific user facility sponsored by DOE's Office of Biological and Environmental Research and located at Pacific Northwest National Laboratory (PNNL). PNNL is operated by Battelle for the Department of Energy under Contract DE-AC05-76RL01830. The 1.3 mAh cm⁻² NMC811 electrodes were kindly supplied by Dr. Bryant Polzin of Cell Analysis, Modeling and Prototyping (CAMP) Facility at Argonne National Laboratory. The LiFSI salt was provided by Dr. Kazuhiko Murata of Nippon Shokubai Co., Ltd.

Keywords: Lithium metal battery • lithium anode • magnesium-doped lithium • simulation • cycling performance

[1]
aK. Xu, Chemical Reviews 2014, 11, 11503-11618; bY. Y. Liu, Y. Y. Zhu, Y. Cui, Nature Energy 2019, 4, 540-550.
[2]
aN. Mahmood, T. Tang, Y. Hou, Advanced Energy Materials 2016, 6, 1600374; bJ. Meng, H. Guo, C. Niu, Y. Zhao, L. Xu, Q. Li, L. Mai, Joule 2017, 1, 522-547.
[3]
R. Kumar, S. Sahoo, E. Joanni, R. K. Singh, W. K. Tan, K. K. Kar, A. Matsuda, Prog. Energy Combust. Sci. 2019, 75, 56.
[4]
Z. Tu, S. Choudhury, M. J. Zachman, S. Wei, K. Zhang, L. F. Kourkoutis, L. A. Archer, Nature Energy 2018, 3, 310-316.
[5]
aC.-M. Park, J.-H. Kim, H. Kim, H.-J. Sohn, Chemical Society Reviews 2010, 39, 3115-3141; bM. N. Obrovac, V. L. Chevrier, Chemical Reviews 2014, 114, 11444-11502; cH. Liu, X.-B. Cheng, J.-Q. Huang, S. Kaskel, S. Chou, H. S. Park, Q. Zhang, ACS Materials Letters 2019, 1, 217-229; dX. Zhang, Y. Yang, Z. Zhou, Chemical Society Reviews 2020, 49, 3040-3071.
[6]
E. Peled, S. Menkin, Journal of the Electrochemical Society 2017, 164, A1703-A1719.
[7]
S. Li, M. W. Jiang, Y. Xie, H. Xu, J. Y. Jia, J. Li, Adv. Mater. 2018, 30, 29.
[8]
J. Liu, Z. N. Bao, Y. Cui, E. J. Dufek, J. B. Goodenough, P. Khalifah, Q. Y. Li, B. Y. Liaw, P. Liu, A. Manthiram, Y. S. Meng, V. R. Subramanian, M. F. Toney, V. V. Viswanathan, M. S. Whittingham, J. Xiao, W. Xu, J. H. Yang, X. Q. Yang, J. G. Zhang, Nature Energy 2019, 4, 180-186.
[9]
A. Hagopian, D. Kopač, J.-S. Filhol, A. Kopač Lautar, Electrochimica Acta 2020, 353, 136493.
[10]
W. Xu, J. L. Wang, F. Ding, X. L. Chen, E. Nasybutin, Y. H. Zhang, J. G. Zhang, Energy Environ. Sci. 2014, 7, 513-537.
[11]
R. A. Guidotti, P. J. Masset, Journal of Power Sources 2008, 183, 388-398.
[12]
aC.-M. Park, Y.-U. Kim, H. Kim, H.-J. Sohn, Journal of Power Sources 2006, 158, 1451-1455; bZ. Shi, M. Liu, D. Naik, J. L. Gole, Journal of Power Sources 2001, 92, 70-80.
[13]
L.-L. Kong, L. Wang, Z.-C. Ni, S. Liu, G.-R. Li, X.-P. Gao, Advanced Functional Materials 2019, 29, 1808756.
[14]
S. H. Choi, S. J. Lee, D.-J. Yoo, J. H. Park, J.-H. Park, Y. N. Ko, J. Park, Y.-E. Sung, S.-Y. Chung, H. Kim, J. W. Choi, Advanced Energy Materials 2019, 9, 1902278.
[15]
X. Ren, L. Zou, X. Cao, M. H. Engelhard, W. Liu, S. D. Burton, H. Lee, C. Niu, B. E. Matthews, Z. Zhu, C. Wang, B. W. Arey, J. Xiao, J. Liu, J.-G. Zhang, W. Xu, Joule 2019, 3, 1662-1676; bX. Cao, X. Ren, L. Zou, M. H. Engelhard, W. Huang, H. Wang, B. E. Matthews, H. Lee, C. Niu, B. W. Arey, Y. Cui, C. Wang, J. Xiao, J. Liu, W. Xu, J.-G. Zhang, Nat. Energy 2019, 4, 796-805.
[16]
aA. M. Nolan, Y. Z. Zhu, X. F. He, Q. Bai, Y. F. Mo, Joule 2018, 2, 2016-2046; bA. P. Wang, S. Kadam, H. Li, S. Q. Shi, Y. Qi, npj Comput. Mater. 2018, 4, 26.
[17]
aM. Jagannathan, K. S. R. Chandran, Journal of the Electrochemical Society 2013, 160, A1922-A1926; bT. J. Richardson, G. Chen, Journal of Power Sources 2007, 174, 810-812.
[18]
aD. Gaissmaier, D. Fantauzzi, T. Jacob, The Journal of Chemical Physics 2018, 150, 041723; bl. T. Røe, S. M. Selbach, S. K. Schnell, The Journal of Physical Chemistry Letters 2020, 11, 2891-2895.
[19]
M. Jäckle, A. Groß, Journal of Chemical Physics 2014, 141, 174710.
[20]
H. Xu, D. Lee, S. B. Sinnott, V. Dierolf, V. Gopalan, S. R. Phillpot, Journal of Physics: Condensed Matter 2010, 22, 135002.
[21]
W. Liu, P. Liu, D. Mitlin, Chem. Soc. Rev. 2020, 49, 7284-7300.
[22]
X. Ren, P. Gao, L. Zou, S. Jiao, X. Cao, X. Zhang, H. Jia, M. H. Engelhard, B. E. Matthews, H. Wu, H. Lee, C. Niu, C. Wang, B. W. Arey, J. Xiao, J. Liu, J.-G. Zhang, W. Xu, Proc. Natl. Acad. Sci. U. S. A. 2020, 117, 28603-28613.

RESEARCH ARTICLE
Entry for the Table of Contents

![](./images/812406874598014979_9.jpg)

Mg-doped Li with about 5 wt.% Mg (Li-Mg5) has the lowest absorption-energy of Li from density functional theory calculations. Experimental tests demonstrate that Li-Mg5 exhibits superior cycling stability to pure Li and Li-Mg10 anodes in Li metal batteries with high-loading cathode and lean electrolyte under 4.4 V high-voltage, leading to dense and less-corrosive Li deposition thus validating the simulation results.