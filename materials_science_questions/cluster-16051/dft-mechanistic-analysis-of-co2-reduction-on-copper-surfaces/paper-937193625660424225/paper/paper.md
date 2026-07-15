# Three-dimension porous Zn-Cu alloy: An inexpensive electrocatalyst for highly selective $CO_2$ reduction to CO in non-aqueous electrolyte

Zekun Zhang $^{a}$, Shiji Li $^{a}$, Yongfang Rao $^{a, *}$, Liu Yang $^{a}$, Wei Yan $^{a,b}$, Hao Xu $^{a,b, *}$

$^{a}$ Department of Environmental Science and Engineering, Xi'an Jiaotong University, Xi'an 710049, Shaanxi, China
$^{b}$ Research Institute of Xi'an Jiaotong University, Zhejiang, Hangzhou 311200, China

---

## ARTICLE INFO

**Keywords:**
CO₂ electroreduction
Zn-Cu alloy
Morphology control
CO generation
Non-aqueous electrolyte

---

## ABSTRACT

Designing cheap and highly active electrochemical $CO_2$ reduction (ECO₂R) systems are crucial for their commercial applications. Herein, we report a 3D porous Zn-Cu alloy electrode for ECO₂R to CO. A small amount of Cu has a dramatic effect on the micro-morphology of the electrode. Furthermore, DFT calculations confirm that Zn-Cu alloying significantly reduces the formation energy barrier of *CO intermediates. The synergy between the unique 3D porous structure and the alloying effect enables the $Cu_{0.3}Zn_{9.7}$ electrode to achieve up to 90.69 % Faraday efficiency (FE) for CO at $-1.2$ V (vs. reversible hydrogen electrode (RHE)). Furthermore, we prepare a novel non-aqueous cathode electrolyte consisting of deep eutectic solvent (DES) and propylene carbonate (PC) for ECO₂R. The $FE_{CO}$ of $Cu_{0.3}Zn_{9.7}$ increased to 94.89 % and the reduction potential decreased to $-1$ V (vs. RHE). The low cost of preparing 3D porous electrodes and the ease of synthesizing the novel non-aqueous electrolyte render this ECO₂R system for CO promising for large-scale application.

---

## 1. Introduction

Since the Industrial Revolution, mankind's reliance on fossil fuels has led to increasingly serious emissions of carbon dioxide ($CO_2$) into the atmosphere, and the resulting ecological problems, such as global warming and ocean acidification, have significantly impacted the natural environment and human development [1–3]. Utilizing photo energy [4,5] or electricity [6,7] to convert $CO_2$ into high-energy chemicals not only alleviates the energy and environmental crises caused by excessive carbon emissions, but also creates a carbon economy with high added value, making it an attractive carbon–neutral strategy. Compared with photocatalysis, electrochemical $CO_2$ reduction (ECO₂R) has many advantages such as controllable reaction rate and scalable electrolyzer, and thus has received extensive attention from scholars [8,9]. Among the numerous $CO_2$ reduction products, carbon monoxide (CO) is one of the most desirable target products and has more economically viable net gross margin than other hydrocarbons and alcohols. As a primary reduction product, CO also has a wider range of applications and is more exploitable [10,11]. To achieve an impressive CO generation from ECO₂R, low-cost and earth-abundant catalysts with high selectivity are demanded [12].

According to the volcano plot using the *CO binding energy as a descriptor, precious metal gold (Au)- and silver (Ag)-based catalysts are currently the most active catalysts for ECO₂R to CO [13]. However, the low cost of the catalyst design and the high selectivity of the product are equally important for the industrial application of ECO₂R. Hence, it is urgent to develop electrocatalysts which are cheap and highly selective for CO. Recent studies have shown that zinc (Zn), which has an equally low binding energy for *CO intermediates, is considered to be an effective alternative to the aforementioned precious metal catalysts. However, the lower binding energy of Zn for the key intermediates (*COOH and *CO) in ECO₂R process compared to Au and Ag resulted in its lower intrinsic activity and selectivity for CO [14–16]. Mixed bimetals at the atomic level through alloying, solid solutions, etc., can be used to modify and tune the electronic structure of the mixed system, and the role of this synergistic bimetallic effect in promoting the conversion of ECO₂R to CO has been demonstrated [17–20]. Since copper (Cu) has a higher binding energy for *COOH and *CO than Zn, combining Cu with Zn is expected to utilize the synergistic effect to optimize the adsorption of the key intermediates on the bimetallic surface, thus improving the ECO₂R performance.

Another important factor controlling the product selectivity is the retention time for the reaction intermediates, which not only depends on the intrinsic properties of catalysts but is also closely related to their

---

* Corresponding authors at: Department of Environmental Science and Engineering, Xi'an Jiaotong University, Xi'an 710049, Shaanxi, China (Hao Xu).
E-mail addresses: yfrao@xjtu.edu.cn (Y. Rao), xuhao@xjtu.edu.cn (H. Xu).

https://doi.org/10.1016/j.cej.2023.147376
Received 26 July 2023; Received in revised form 19 October 2023; Accepted 13 November 2023
Available online 24 November 2023
1385-8947/© 2023 Elsevier B.V. All rights reserved.

morphology. The large specific surface area of porous materials can increase the number of active sites on the surface of catalysts and the interaction between intermediates and catalysts, which in turn significantly promotes the generation of reduction products [21,22]. Moreover, porous structures can also control the product distribution and generation rate by controlling the local pH and mass transfer of reactants/intermediates/products within the pores [23,24].

Aqueous electrolytes are currently the most widely investigated, environmentally benign and low-cost cathode electrolytes. However, the solubility of $CO_2$ in aqueous electrolytes is quite limited [25], and the theoretical electrode potential range in aqueous solution is wide, overlapping with the potential window of water decomposition, resulting in part of the electrical energy being wasted [26]. Meanwhile, since the aqueous electrolyte can provide abundant native $H^+$, the catalyst surface is highly susceptible to competitive hydrogen evolution reaction (HER), which is unfavorable for ECO₂R, and is also inefficient in terms of energy [27]. In recent years, ionic liquids (ILs) [28,29], a typical non-aqueous electrolyte, have been widely used in the field of ECO₂R. This electrolyte, in addition to its high $CO_2$ solubility, directly inhibits HER because of the lack of available protons in the system itself. However, the high cost and viscosity of ILs have hindered their direct application in ECO₂R. Deep eutectic solvents (DESs) are two- or three-component mixtures of hydrogen-bond acceptors (e.g., quaternary ammonium salts) and hydrogen-bond donors (e.g., compounds such as amides, carboxylic acids, and polyols) in certain stoichiometric ratios. Their physicochemical properties are very similar to ILs, and they are considered to be reasonable alternatives to ILs based on cheap raw materials and simple synthesis steps [30,31]. By mixing with low-viscosity $CO_2$ absorbers, such as propylene carbonate (PC), the viscosity of the solution can be significantly reduced, which is expected to promote ECO₂R.

Motivated by above consideration, we synthesized a 3D porous Zn-Cu alloy electrode in one step using a simple hydrogen bubble template method and used it for ECO₂R to CO. It was found that a small amount of Cu doping would have a great impact on the porosity, hydrophilicity and surface morphology of the catalysts. Hence, Cu not only acts as a dopant for the whole catalyst, but also has a strong structural role, which in turn directly affects the performance of the catalyst. Furthermore, the alloying effect of Zn and Cu produces a stabilizing effect on the *COOH intermediates, resulting in a high ECO₂R activity. In addition, the reaction kinetics of ECO₂R in aqueous electrolytes are limited and the high reduction potential leads to the generation of multiple competing reaction pathways. Hence, we prepared a novel non-aqueous combined electrolyte (DES/PC) and applied the $Cu_{0.3}Zn_{9.7}$ electrode to it. The reduction potential of ECO₂R to CO was substantially reduced, which led to an increase of $FE_{CO}$ as well. The electrode preparation method and non-aqueous electrolyte design ideas proposed in this paper are expected to provide a certain guidance for the future development of electrocatalytic systems for ECO₂R to CO.

## 2. Supporting experiment section

### 2.1. Materials and reagents

Cupric acetate $(Cu(CH_3COO)_2,\ 98.31\ \%)$ was purchased from Shanghai Haohong Scientific Co., Ltd. Zinc sulfate heptahydrate $(ZnSO_4\cdot7H_2O,\ AR)$, Potassium hydrogen carbonate $(KHCO_3,\ AR)$, Ethylene glycol $((CH_2OH)_2,\ AR)$ and Sulfuric acid $(H_2SO_4,\ 98\ \%)$ were purchased from Sinopharm Chemical Reagent Xi'an Co., Ltd. Propylene carbonate $(C_4H_6O_3,\ 99.7\ \%)$ and Choline chloride $(C_5H_{14}ClNO,\ AR,\ 98\ \%)$ were purchased from Shanghai Macklin Biochemical Co., Ltd. Cu foam (120 ppi, 99.9 %) and Zn foil (99.99 %) were purchased from Kunshan Xingzhenghong Electronic Materials Co., Ltd. Nafion-117 perfluorinated membrane was purchased from DuPont Company. All reagents are commercially available and used directly without further treatment. Deionized water $(18.2\ M\Omega\cdot cm^{-2})$ was prepared using EPED S2-D water purification system.

### 2.2. Syntheses of $Cu_xZn_{10-x}$ working electrodes

Cu foam substrates were cleaned with 37 % hydrochloric acid for 1 min to remove its primary oxide layer, and then successively sonicated in acetone, ethanol, and deionized water for 5 min, respectively, and finally cleaned with deionized water and blown dry under nitrogen $(N_2)$ atmosphere. An effective area of $1\ cm\times0.5\ cm\times2$ was glued out with silicone sealant and set aside. $x\ M\ Cu(CH_3COO)_2$ and $(0.2\ -\ x)\ M$ $ZnSO_4\cdot7H_2O$ were added to a $1.5\ M\ H_2SO_4$ and stirred until all of the metal salts were dissolved. $Cu_xZn_{10-x}$ working electrodes were prepared using a typical hydrogen bubble template method [32]. Specifically, a three-electrode system consisting of a foam Cu as the cathode, a platinum sheet electrode as the anode, and a saturated calomel electrode as the reference electrode was subjected to constant current electrodeposition. The current value was set at -2 A and the deposition time was 30 s. Fig. S1 shows the simultaneous generation of hydrogen bubbles at the sample-electrolyte interface during metal deposition. After electrodeposition, the electrodes were quickly rinsed with deionized water and dried with $N_2$ gas for spare use.

### 2.3. Synthesis of DES in PC electrolyte

Before preparing DES, choline chloride (ChCl) was dried in an oven for 24 h in advance. DES was prepared by mixing a certain amount of ChCl and ethylene glycol (EG) in a molar ratio of 1:2, and stirring in an oil bath at $80\ ^\circ C$ for 2 h. ChCl was poorly soluble in PC, whereas a combination of ChCl and EG (1:2) readily provided 1 M solutions. The combined DES/PC electrolyte was prepared by mixing 12 mL of DES with 38 mL of PC and stirring well.

### 2.4. Catalyst characterizations

The surface morphologies of the electrodes were characterized using field emission scanning electron microscopy (FE-SEM, TESCAN) equipped with Energy Dispersive Spectrometer (EDS). The contact angle measurement of the electrodes were done using angle measuring instrument (KRUSS). Crystal structure of electrodes were characterized by X-Ray Diffractometer (XRD, Shimadzu). The chemical composition and chemical state information of the electrodes were characterized using X-ray photoelectron spectroscopy (XPS, ESCALAB $Xi^+$) testing. C 1 s (284.8 eV) was used to calibrate the peak positions of various elements. The bulk chemical compositions of samples were determined by a PerkinElmer 8300 inductively coupled plasma optical emission spectrometry (ICP-OES).

### 2.5. Electrochemical reduction of $CO_2$

ECO₂R experiments were performed using a customized two-compartment H-type cell separated by a Nafion-117 perfluorinated membrane. A potentiostat (CHI-1140c) provided power for reactions. Electrochemical testing was performed using a three-electrode system consisting of a working electrode, an Ag/AgCl reference electrode (with saturated KCl aqueous solution as the filling solution) and a platinum sheet counter electrode $(1.5\times1.5\ cm)$. A $0.1\ M\ KHCO_3$ solution was used as the cathode and anode electrolyte solutions. When DES in PC was used as the cathode electrolyte, the anode electrolyte was $0.1\ M$ $H_2SO_4$ for providing hydrogen sources for reactions. Prior to ECO₂R, the cathode electrolyte was continuously bubbled with $N_2$ (99.99 %) for 30 min to evacuate the dissolved oxygen. Subsequently, $CO_2$ (99.999 %) was continuously bubbled for 30 min to saturate the electrolyte with $CO_2$. At this time, the pH of the $0.1\ M\ KHCO_3$ electrolyte was 6.8 and the pH of the DES/PC electrolyte was 5.1. At the beginning of ECO₂R, electrodes were activated by continuous electrolysis for 20 min at -1.2 V (vs. RHE). During ECO₂R, the $CO_2$ flow rate was always kept constant

![](./images/937193625660424225_1.jpg)

Scheme 1. Representation of $Cu_0Zn_{10}$ and $Cu_xZn_{10-x}$ ($x \neq 0$) prepared by hydrogen bubble template method.

at 20 sccm. To determine the FEs of the $ECO_2R$ products, the i-t curve was measured for 1800 s at different potentials. The applied potentials during the $ECO_2R$ process were converted to the RHE scale by using Eq. (1).

$$
E(\mathrm{V} \text{ vs. RHE}) = E(\mathrm{V} \text{ vs.Ag/AgCl}) + 0.199\ \mathrm{V} + 0.059 \times pH \tag{1}
$$

All gas products were detected online by gas chromatography (GC 7920, Beijing China Education Au-light Co., Ltd.). Samples were injected every 30 min for three sets of parallel experiments.

The electrochemcial active surface area (ECSA) was estimated by measuring the double-layer capacitance with cyclic voltammetry (CV) in a non-Faradaic potential range at scan rates of 40, 60, 80, 100 and 120 $\mathrm{mV \cdot s^{-1}}$ in a $\mathrm{CO_2}$-saturated $0.1\ \mathrm{M}\ \mathrm{KHCO_3}$ solution. The Linear Sweep Voltammetry (LSV) was carried out from -0.6 to -1.8 V vs. RHE in $\mathrm{CO_2}$-saturated $0.1\ \mathrm{M}\ \mathrm{KHCO_3}$ or $\mathrm{N_2}$-saturated $0.1\ \mathrm{M}\ \mathrm{KHCO_3}$ to evaluate the activity of $ECO_2R$.

### 2.6. DFT calculations
The density functional theory (DFT) calculations were performed using the Vienna ab initio Simulation Package (VASP) with the projector augmented-wave potentials [33,34]. The generalized gradient approximation (GGA) with the Perdew-Burke-Ernzerhof (PBE) functional was employed to describe the exchange-correlation [35,36]. A cutoff energy for the plane-wave basis was set to 520 eV for all calculations. The energy convergence criteria for self-consistent-field iteration was $10^{-5}\ \mathrm{eV}$, and the atomic positions were fully optimized until all the residual forces are smaller than $0.01\ \mathrm{eV\ \mathring{A}^{-1}}$. Firstly, the structure optimization of bulk Zn was performed with a Monkhorst-Pack mesh for Brillouin zone integration. Then, the slab model of Zn ($2 \times 2$ supercell, 20 atoms in total) was constructed along the Zn (100) surface, and a $15\ \mathring{A}$ vacuum space along the z-direction was included to avoid inter-layer interactions. After the optimization of the Zn (100) slab, a single Zn atom was replaced by one Cu atom on the surface were created and optimized. Finally, the free energy differences of the $\mathrm{CO_2}$ decomposition into CO

![](./images/937193625660424225_2.jpg)

Fig. 1. Morphological characterizations and their local high magnification FE-SEM images of different electrodes: (a) Cu foam, (b) $Cu_0Zn_{10}$, (c) $Cu_{0.1}Zn_{9.9}$, (d) $Cu_{0.3}Zn_{9.7}$, (e) $Cu_{0.5}Zn_{9.5}$, (f) $Cu_{0.7}Zn_{9.3}$, (g) $Cu_{0.9}Zn_{9.1}$ and (h) $Cu_1Zn_9$. High-resolution images of the $Cu_{0.3}Zn_{9.7}$ electrode: (i) intra-pore structure, (j) localized magnification of the intra-pore structure (in the red circle), (k) edge structure of the pore and (l) localized magnification of the edge structure of the pore (in the red circle). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/937193625660424225_3.jpg)

Fig. 2. Structural characterizations of electrodes. (a) Wide-angle XRD, Zoom-in XRD patterns in the range of (b) $35^{\circ}-43^{\circ}$. (c) XPS survey spectrum, (d) Zn 2p and Cu 2p XPS spectra. Quasi-in situ (e) Zn 2p and (f) Cu 2p XPS spectra of $Cu_{0.3}Zn_{9.7}$ electrode.

were calculated on both the Zn (1 0 0) slab and the Cu-doped Zn (1 0 0) slab. For all the simulations, the DFT-D3 Grimme strategy for dispersion correction of total energy was used to include the vdW interactions [37].

## 3. Results and discussion

### 3.1. Morphology and microstructure characterizations

A typical procedure for the preparation of porous coatings by the hydrogen bubble template method is shown in Scheme 1. The cathode region was in $1.5\ \text{M}\ \text{H}_{2}\text{SO}_{4}$ and electrodeposited at a high current density $(-2\ \text{A·cm}^{-2})$. In this process, hydrogen evolution occurred simultaneously with the growth of the metal plating, and hydrogen $(\text{H}_{2})$ continuously bubbled on the Cu foam-loaded plating (yellow dashed box in Fig. S1), which acted as a dynamic pore-forming template. Fig. S2 shows the color of the electrodeposition solution with different $\text{Cu}^{2+}$ contents and the macroscopic morphologies of $\text{Cu}_{x}\text{Zn}_{10-x}$ electrodes, respectively. The color of the electrodeposition solution gradually turned blue with the increase of $\text{Cu}^{2+}$ content. $\text{Cu}_{0}\text{Zn}_{10}$ electrode showed a silver-white metallic luster, and all electrodes' coatings turned black when a small amount of Cu was added.

We characterized the microscopic morphology of the electrodes. As shown in Fig. 1a, the Cu foam had an interwoven pore structure, which apparently had a much larger specific surface area than Zn foil (Fig. S3), and further deposition of plating on the Cu foam was expected to provide more active sites for $\text{ECO}_{2}\text{R}$. Interestingly, the $\text{Cu}_{0}\text{Zn}_{10}$ electrode was pore-free when there was no $\text{Cu}^{2+}$ in the deposition solution, and local high magnification image showed the electrode as a sheet-like structure (Fig. 1b). After the addition of $0.002\ \text{M}\ \text{Cu}^{2+}$, the electrode exhibited a sharp cone-like structure (Fig. 1c). Further increase of $\text{Cu}^{2+}$ content led to the formation of regular pore structures on the surface of electrodes (Fig. 1d-h), but microscopic morphologies were still drastically different. Electrodes with a $\text{Cu}^{2+}$ content of 0.01-0.014 M showed typical "fern-like" structures (Fig. 1e,f). When the $\text{Cu}^{2+}$ content ranged from 0.018 to 0.02 M, electrodes showed an irregular "cluster-like" structure. Obviously, a small change in $\text{Cu}^{2+}$ caused a dramatic change in the microscopic morphology of catalyst coatings, indicating that an important role of $\text{Cu}^{2+}$ is constructing the morphologic skeleton of the alloy coatings. Hence, the structural role of $\text{Cu}^{2+}$ was further explored.

During the electrodeposition preparation of electrodes, $\text{H}_{2}$ acts as a template for pore creation and evolves at the liquid-solid interface. Hence, the hydrophilicity of the electrode surface affects the formation of hydrogen bubbles and further influences the formation of pores in alloy coatings. Zn foil (Fig. S4a) is more hydrophilic than Cu foam (Fig. S4b), and the surface of the $\text{Cu}_{0}\text{Zn}_{10}$ electrode is highly hydrophilic (Fig. S4c). According to Pavel et al [38], such a strong hydrophilicity is attributed to the special hexagonal sheet-like structure of Zn(0001) [39]. The addition of a small amount of $\text{Cu}^{2+}$ turned the hydrophilicity of the electrode surface to hydrophobicity (Fig. S4d-i); the higher the $\text{Cu}^{2+}$ content was, the more hydrophobic the electrode surface was. When the electrode surface is highly hydrophilic, the contact angle ($\theta$) at the gas-liquid-solid interface (Scheme 1) is small. As a consequence, the residence time of $\text{H}_{2}$ bubbles on the liquid-solid surface is short and the bubble break-off diameter are relatively small. In contrast, the $\text{Cu}_{x}\text{Zn}_{10-x}$ surfaces with $\text{Cu}^{2+}$ doping show good hydrophobicity (Scheme 1), leading to longer residence time of $\text{H}_{2}$ bubbles and larger bubble break-off diameter, which is favorable for the formation of pore structures. In addition, according to the volcano plot of exchange current density $(i_{0})$ versus metal-hydrogen bond strength $(\text{E}_{\text{M-H}})$ of electrolytic hydrogen evolution summarized by Trasatti [40], $i_{0}$ is $\sim10^{-5}\ \text{A·cm}^{-2}$ for Cu and $\sim10^{-7.5}\ \text{A·cm}^{-2}$ for Zn, and the HER kinetics for Zn is much slower than that for Cu. Meanwhile, $\text{E}_{\text{Cu-H}}$ ($\sim45\ \text{kcal·mol}^{-1}$) is significantly higher than $\text{E}_{\text{Zn-H}}$ ($\sim35\ \text{kcal·mol}^{-1}$). For $\text{Cu}_{0}\text{Zn}_{10}$, a thin Zn layer rapidly deposited on the surface of Cu foam at the beginning of the electrodeposition process, and the subsequent electrodeposition process and HER process actually occurred on the "Zn foam". As a consequence, the formation of the electrode pore structure was completely dominated by $i_{0}$ (Zn) and $\text{E}_{\text{Zn-H}}$ soon after electrodeposition. The synergistic effect of hydrophilicity and kinetics together inhibited the formation of pore structures on $\text{Cu}_{0}\text{Zn}_{10}$. As shown in Fig. S5, the average coating thickness of the $\text{Cu}_{0.3}\text{Zn}_{9.7}$ electrode $(46.6\ \mu\text{m})$ was 1.66 times higher than that of the $\text{Cu}_{0}\text{Zn}_{10}$ electrode $(26.9\ \mu\text{m})$ due to the inability of $\text{Cu}_{0}\text{Zn}_{10}$ electrode to generate the pore structure by $\text{H}_{2}$ bubbling.

As shown in Fig. 1d, $\text{Cu}_{0.3}\text{Zn}_{9.7}$ still exhibited homogeneous pore structure in the local high magnification image. In contrast to other porous electrodes, $\text{Cu}_{0.3}\text{Zn}_{9.7}$ had a dense distribution of pores in the

![](./images/937193625660424225_4.jpg)

Fig. 3. $ECO_{2}R$ performance in a H-type cell reactor (In $CO_{2}$-saturated 0.1 M $KHCO_{3}$ electrolyte). (a) Current densities obtained on electrodes at different applied potentials. (b) $FE_{CO}$ on electrodes at different applied potentials. (c) CO partial current densities obtained on electrodes at different applied potentials (The result corresponds to the average of three individual measurements). (d) FEs for formation of various products and partial current density for the formation of CO on electrodes at -1.2 V (vs. RHE).

"branches" of Cu foam. The intra- and extra-pore structures were further characterized using high-resolution scanning electron microscopy. As shown in Fig. 1i, the pore structure was regular and the size was uniform (~10 µm). It was noteworthy that the macroporous coatings of the $Cu_{0.3}Zn_{9.7}$ electrode did not cover up the ~100 µm pore structure of the Cu foam. Hence, the electrode formed an inspiring 3D layered porous structure. As shown in Fig. 1j and l, the intra- and extra-pore microstructures were different. The inside of the pore showed lamellar "accordion" structures (Fig. 1j). The edge of the pore was composed of "leaf-like" structures with a size of ~200 nm (Fig. 1l). Energy Dispersive Spectrometer (EDS) (Fig. S6) shows that Zn and Cu elements were uniformly distributed on the surface of $Cu_{0.3}Zn_{9.7}$. The atomic ratio of Cu:Zn was nearly 6.5 times higher than the molar ratio of Cu:Zn in the deposition solution due to the presence of Cu foam substrates.

### 3.2. Elemental composition and surface chemistry

Elemental compositions, crystal structures and mixing patterns critical to the selectivity of $Cu_{x}Zn_{10-x}$ electrodes were analyzed using XRD and XPS. In Fig. 2a, the diffraction patterns of the seven different electrodes were matched to the metals of Zn and Cu. The Zn coating on $Cu_{0}Zn_{10}$ was thin (Fig. S5) and the XRD penetration depth was micrometer scale. As a consequence, the diffraction peaks of the Cu foam substrate were still observed, even though it was not doped with Cu. Diffraction peaks of $Cu_{0.2}Zn_{0.8}$ were all observed on other $Cu_{x}Zn_{10-x}$ (x = 0.3, 0.5, 0.7, 0.9, 1) electrodes, indicating the formation of the alloy phase in the bulk of electrodes. Details of the changes in the diffraction peaks were further analyzed by locally enlarging the diffraction pattern in the red box in Fig. 2a (Fig. 2b). The peak intensity of the $Cu_{0.2}Zn_{0.8}$ alloy gradually increased and that of the metal Zn gradually decreased with the increase of $Cu^{2+}$, indicating that the addition of more $Cu^{2+}$ caused the formation of an alloy phase rather than a phase-separated metal phase during the electroreduction of $Cu^{2+}$ and $Zn^{2+}$. In addition, since the radius Cu atoms (1.28 Å) were slightly smaller than that of Zn atoms (1.39 Å), the incorporation of Cu into Zn resulted in the lattice contraction of Zn, and the diffraction peaks of Zn were shifted to a high degree, which confirmed the formation of a solid solution between Cu and Zn [41].

High-resolution XPS was used to compare the surface electronic states of the $Cu_{x}Zn_{10-x}$ electrodes and to further understand the charge interactions between Cu and Zn (Fig. 2c-f). Peaks identified in Fig. 2c were associated with the elements Zn, Cu, O, and C. The molar ratios of $Cu^{2+}$ to $Zn^{2+}$ in the electrodeposition solution and elemental ratio of the bulk phase of the electrodes and on its surface are listed in Table S1. The atomic ratios of Cu:Zn on the electrode surface were slightly lower than those in the deposition solution and all of these ratios were smaller than the Cu:Zn ratios in the bulk of the electrodes. We attributed this to the preferential reduction of $Cu^{2+}$ within the bulk phase [42]. Since the reduction potential of $Cu^{2+}$ ($E_{Cu2+/Cu}=0.34$ V (vs. RHE)) was higher than that of $Zn^{2+}$ ($E_{Zn2+/Zn}=-0.76$ V (vs. RHE)) [24], which provided seeding sites for the further deposition of Zn and the formation of pore structures, which in turn led to the lager Cu:Zn ratios within the bulk of the electrodes than those on the surface layers. In addition, the prioritized reduction of $Cu^{2+}$ also promoted its contribution in the formation of porous plating layers.

As shown in Fig. 2d, the Zn 2p peak and the Cu 2p peak shifted to

![](./images/937193625660424225_5.jpg)

Fig. 4. (a) Plots of charging current density differences ($\Delta j$) vs. scan rates of different electrodes. (b) LSV curves obtained on different electrodes in $N_2$-purged (dashed line) and $CO_2$-purged (solid line). (c) Current ratio of $CO_2$ reduction to HER at different potentials (The result corresponds to the average of three individual measurements). (d) Tafel slops of different electrodes.

lower and higher binding energies with increasing Cu:Zn ratios, respectively (specific binding energy positions were given in Table S2), which was attributed to the electronic interactions between Zn and Cu. Since the work function of Cu (4.7) is larger than that of Zn (4.3) [24], this leads to a transfer of electrons from metallic Zn to Cu on the surface of the $Cu_xZn_{10-x}$ electrodes, indicating a well-alloyed electrode surface. XRD and XPS tests demonstrated that the $Cu_xZn_{10-x}$ electrodes showed alloying in both bulk and surface. Further quasi-in-situ XPS analysis of the Zn 2p and Cu 2p regions of the $Cu_{0.3}Zn_{9.7}$ electrode was analyzed. The deconvoluted Zn 2p core-level spectra of $Cu_{0.3}Zn_{9.7}$ in Fig. 2e shows the presence of metallic $Zn^0$ and $Zn^{2+}$ species [43]. Within the Cu 2p region (Fig. 2f), satellite peaks of Cu appeared near 942 eV, indicating the presence of $Cu^{2+}$ on the surface of $Cu_{0.3}Zn_{9.7}$ [44]. It should be noted that since no metal oxide was present in the bulk of the electrode, it indicated that small amounts of $Zn^{2+}$ and $Cu^{2+}$ were only present on the surface of $Cu_{0.3}Zn_{9.7}$. It was due to the unavoidable exposure of the electrode to the environment after preparation, resulting in partial oxidation of $Zn^0$ and $Cu^0$.

### 3.3. Electrochemistry and $ECO_2R$ performances

The linear scanning voltammetry (LSV) curves of $Cu_xZn_{10-x}$ were compared in $CO_2$-saturated 0.1 M $KHCO_3$ electrolyte. The current density was normalized to the geometrical surface area of the electrode, ca. $1\ \text{cm}^2$. As shown in Fig. S7, $Cu_xZn_{10-x}$ electrodes exhibited a gradually increasing current density with increasing Cu doping. The $Cu_{0.3}Zn_{9.7}$ electrode showed the fastest current density growth rate in the high-potential region, which may be attributed to its special 3D layered porous structure. $Cu_{0.3}Zn_{9.7}$ still had a high current density in the $ECO_2R$ potential range of $-0.8$ to $-1.6\ \text{V (vs. RHE)}$ (Fig. 3a). The $ECO_2R$ performances of $Cu_xZn_{10-x}$ electrodes were further tested, and the reduction products were $CO$, $H_2$ and a small amount of methane ($CH_4$) (Fig. 3b and Fig. S8). The $FE_{CO}$ of all electrodes, except $Cu_1Zn_9$, first increased and then decreased with increasing reduction potential. Among them, the optimal reduction potentials of Zn foil, $Cu_0Zn_{10}$ and $Cu_{0.1}Zn_{9.9}$ for CO were $-1.4\ \text{V (vs. RHE)}$, while other electrodes were $-1.2\ \text{V (vs. RHE)}$. Obviously, a certain amount of Cu doping decreased the optimal reduction potential for CO. $Cu_{0.3}Zn_{9.7}$ exhibited the highest $FE_{CO}$ (90.69 %) at $-1.2\ \text{V (vs. RHE)}$. In addition, as shown in Fig. 3c, its partial current density for CO ($j_{CO}$) at $-1.2\ \text{V (vs. RHE)}$ was $-14.88\ \text{mA·cm}^{-2}$, only lower than that of $Cu_{0.9}Zn_{9.1}$ ($-15.82\ \text{mA·cm}^{-2}$). The detailed test results of gas products in GC at $-1.2\ \text{V (vs. RHE)}$ were shown in Figs. S8 and S9. Fig. 3d compares the product distribution and the $j_{CO}$ of all electrodes at $-1.2\ \text{V (vs. RHE)}$. The $Cu_{0.3}Zn_{9.7}$ electrode exhibited the optimal $FE_{CO}$ and higher $j_{CO}$, indicating its high intrinsic activity for CO generation. Hence, $Cu_{0.3}Zn_{9.7}$ was subsequently used as a representative electrode for further investigation.

Zn foil and $Cu_0Zn_{10}$ with sheet-like nonporous structure were used as comparison electrodes. Cyclic voltammetry (CV) scans (Fig. S11) were carried out at different scan rates, and the ECSA of the electrodes was estimated using the double layer capacitance ($C_{dl}$) (Fig. 4a). The $C_{dl}$ values of Zn foil, $Cu_0Zn_{10}$ and $Cu_{0.3}Zn_{9.7}$ were 1.22, 2.48 and 2.57 $\text{mF·cm}^{-2}$, respectively, suggesting that $Cu_{0.3}Zn_{9.7}$ had the most active sites, which was favorable for improving the $ECO_2R$ performance. The LSV curves of electrodes were measured in an aqueous solution of 0.1 M $KHCO_3$ saturated with $N_2$ and $CO_2$ (Fig. 4b). The current density of Zn foil was slightly higher under $CO_2$ than under $N_2$ over the entire potential range. Whereas, the current densities of $Cu_0Zn_{10}$ and $Cu_{0.3}Zn_{9.7}$

![](./images/937193625660424225_6.jpg)

Fig. 5. (a-f) FE-SEM images and (g) XRD patterns of the $Cu_{0.3}Zn_{9.7}$ electrode before (a-c) and after 8 h (d-f) of continuous $ECO_2R$. (h) Stability test and the corresponding $FE_{CO}$ and $FE_{H2}$ of $Cu_{0.3}Zn_{9.7}$ electrode towards $ECO_2R$ performed at $-1.2$ V (vs. RHE). (i) The $FE_{CO}$ of $ECO_2R$ on $Cu_{0.3}Zn_{9.7}$, Au and Ag foils were compared (in 0.1 M $KHCO_3$ electrolyte) [11].

were significantly higher under $CO_2$ than under $N_2$. This indicates that the reduction of $CO_2$ is superior to that of $H_2O$ at these two electrodes. $Cu_{0.3}Zn_{9.7}$ exhibited a much larger current density under $CO_2$ compared to the others, suggesting that it had the highest activity towards $ECO_2R$. The order of current density magnitude of the three electrodes under $CO_2$ was consistent with that of ECSA (Zn foil $< Cu_0Zn_{10} < Cu_{0.3}Zn_{9.7}$), suggesting that the magnitude of the active area may be positively correlated with the activity of $ECO_2R$.

The current density ratios of $CO:H_2$ ($i_{CO}:i_{H2}$) were shown in Fig. 4c. The similar $i_{CO}:i_{H2}$ of Zn foil and $Cu_0Zn_{10}$ indicates that they had similar HER inhibition, which was consistent with the results observed in Fig. 3d. However, the ECSA of $Cu_0Zn_{10}$ and the LSV under $CO_2$ were greater than those of Zn foil. Such seemingly contradictory results sug- gest that active area could not play a significant role in the inhibition of HER at Zn electrodes in $ECO_2R$. Interestingly, we observed a significant increase in the $i_{CO}:i_{H2}$ of $Cu_{0.3}Zn_{9.7}$ and a significant decrease in HER activity, suggesting that the presence of Cu in the $Cu_{0.3}Zn_{9.7}$ electrode played a crucial role in improving the $ECO_2R$ current by inhibiting HER. Previous results on Zn/Cu porous electrodes [38] suggested that Cu only contributed to controlling the morphology of catalysts and the reduction of $CO_2$ occurred mainly on Zn, which could not be entirely true. The enhanced electrode activity of $Cu_{0.3}Zn_{9.7}$ could be attributed to the dual effect of the presence of Cu and the 3D porous structure. Tafel plots of the logarithmic value of $j_{CO}$ ($\log j_{CO}$) versus overpotential show that the Tafel slope of $Cu_{0.3}Zn_{9.7}$ (169.09 mV·dec⁻¹) was smaller than that of both $Cu_0Zn_{10}$ (255.15 mV·dec⁻¹) and Zn foil (331.48 mV·dec⁻¹) (Fig. 4d), indicating that $Cu_{0.3}Zn_{9.7}$ had the lowest activation energy barrier and the fastest reaction kinetics during the $ECO_2R$ process.

Stability is an important indicator of the performance of $ECO_2R$. Fig. 5a-f show the comparative morphology of $Cu_{0.3}Zn_{9.7}$ before $ECO_2R$ (Fig. 5a-c) and after 8 h of reaction (Fig. 5d-f) at $-1.2$ V (vs. RHE). The morphology of the electrode was similar before and after $ECO_2R$ reaction, and the pore structure remained after the reaction. The slightly rough edges of the "branches" of Cu foam in Fig. 5d were due to the slight dissolution and re-reduction of Zn on the surface in $ECO_2R$. The XRD comparison of $Cu_{0.3}Zn_{9.7}$ before and after electrolysis (Fig. 5g) shows that the diffraction peak intensity as well as the location of the peaks did not change, indicating that the crystal structure of $Cu_{0.3}Zn_{9.7}$ did not change during the reaction. Fig. 5h shows that during the continuous $ECO_2R$ process at $-1.2$ V (vs. RHE) for up to 8 h, the total current density remained almost constant, with $FE_{CO}$ above 80 % and $FE_{H2}$ below 20 %. These findings confirm the stability of $Cu_{0.3}Zn_{9.7}$ during $ECO_2R$.

As mentioned above, the catalysts which has currently been opti- mized for the generation of CO by $ECO_2R$ are mainly the precious metals of Au and Ag. They are often used as monometallic catalysts or as the

![](./images/937193625660424225_7.jpg)

Fig. 6. (a) Optimized atomistic configuration model. (b) Side and top views of the charge density difference at the Zn-Cu alloy interface. The red and green colors represent the charge accumulation and depletion areas, respectively. (c) Calculated free-energy diagrams of ECO₂R to CO. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

main components for the modification of bimetallic catalysts. However, it is well known that the high price of Au and Ag limits their practical application. The raw materials used in this study for the preparation of Cu₀.₃Zn₉.₇ are Cu and Zn that are relatively abundantly stored in the earth. As shown in Fig. 5i, the selectivity of Cu₀.₃Zn₉.₇ toward CO was comparable to that of Ag and Au. In addition, Cu₀.₃Zn₉.₇ had a wider reduction potential range than Ag and Au, with the limit of FE_CO higher than 80 %. However, its reduction potential was also higher. These results indicate that Cu₀.₃Zn₉.₇ is expected to be a reasonable alternative to the precious metal catalysts for ECO₂R to CO.

### 3.4. Mechanism of enhanced selectivity of the Cu₀.₃Zn₉.₇ electrode
ECO₂R to CO requires three processes shown in Eq. (2)-(4), i.e., adsorption of CO₂ at the active sites, *COOH intermediate produces *CO by protonation reaction, and desorption of the *CO intermediates [45]. Reducing the energy barrier of *CO and facilitating the desorption of *CO are the keys to improve FE_CO.

$$^{*}+CO_{2}+H^{+}+e^{-}\to^{*}COOH \tag{2}$$

$$^{*}COOH + H^{+} + e^{-}\to^{*}CO + H_{2}O \tag{3}$$

$$^{*}CO\to^{*} + CO \tag{4}$$

We performed DFT calculations to further illustrate the relationship between intermediates and selectivity. An optimization model for Cu₀.₃Zn₉.₇ was built based on the atomic ratio of Zn and Cu in ICP-OES (Fig. 6a). The differential charge density of the Zn-Cu alloy structure was shown in Fig. 6b. The Cu atom as a whole was in an electron-gaining state (0.21 electrons were gained by Cu substituting for Zn), suggesting that there was an interaction between Cu and Zn, which can affect the adsorption of key reaction intermediates on the catalyst surface [12]. Consequently, we also calculated the energy barrier for the entire ECO₂R pathway. As shown in Fig. 6c, the adsorption energy of *COOH on the Zn surface was -0.83 eV, and on the Zn-Cu alloy surface was -0.61 eV. Since the adsorption energy of *COOH on the Zn surface was too negative, resulting in its further protonation to generate *CO needed to overcome an energy barrier of 0.8 eV. Hence, it was very difficult to realize the Eq. (2) reaction on the Zn catalyst surface, which directly inhibited the CO generation. In contrast, on the surface of Zn-Cu alloy, the energy barrier for the protonation of *COOH to generate the key intermediate *CO was greatly reduced (0.57 eV). Hence, the reduction of the energy barrier of the Zn-Cu alloy for the generation of *COOH to *CO is the key to improve the CO generation activity and selectivity of the Cu₀.₃Zn₉.₇ electrode.

According to Wang et al [18], since Cu has a higher binding energy for *CO, it inhibits the desorption of *CO on the catalyst surface when more Cu is introduced, allowing the HER to dominate. This also explains the higher HER observed on the Cu₁Zn₉ electrode. In fact, introducing Cu into Zn would contribute to HER since Cu has a lower hydrogen binding energy than Zn ($\Delta\text{E}_{\text{Cu-*H}} = 0$ eV vs. $\Delta\text{E}_{\text{Zn-*H}} = +0.5$ eV) [46]. However, the experimental results show that Cu₀.₃Zn₉.₇ was able to inhibit HER (Fig. 4c). There are two main reasons for this. First, small amounts of Cu have a much greater effect on *CO production than the effect of small amounts of hydrogen binding energy reduction, suggesting that the influence of Zn-Cu on HER is much smaller than that on ECO₂R. Second, as the lowering of the *CO energy barrier allows for large amounts of *CO to be generated (Fig. 6c), CO toxicity exerts a significant effect on *H binding and the resulting HER activity [47]. At a high CO covering, HER is substantially weakened, and this effect is greater at Zn-Cu alloy electrodes than that at pure Zn electrodes.

The 3D porous structure of Cu₀.₃Zn₉.₇ also plays a crucial role in the ECO₂R to CO. The structure is able to increase the specific surface area of the electrode, provide more active sites for ECO₂R, and promote the formation of a large number of key intermediates, which is crucial for kinetically limited ECO₂R. Meanwhile, the special 3D layered porous structure can increase the retention time of *COOH in the Cu₀.₃Zn₉.₇ electrode and promote the conversion of *COOH to *CO to further improve the FE_CO. In summary, we conclude that the excellent ECO₂R performance of the Cu₀.₃Zn₉.₇ electrode is attributed to the coupling effect of its unique 3D porous structure and alloying effect of Zn and Cu.

### 3.5. Application of the Cu₀.₃Zn₉.₇ electrode in a novel electrolyte system
In this study, the FE_CO of Cu₀.₃Zn₉.₇ in 0.1 M KHCO₃ electrolyte reached 90.69 % at $-1.2$ V (vs. RHE). Although this result is close to that of the precious metals of Au and Ag, the current reduction potential is still high due to the low intrinsic activity of Zn. Low-cost DES was mixed with PC to form a novel non-aqueous cathode electrolyte; the catalytic effect of chloride in DES and the low viscosity and high CO₂ solubility of PC can further improve the selectivity of Cu₀.₃Zn₉.₇ toward CO and reduce the reduction potential. The LSV of Cu₀.₃Zn₉.₇ in two CO₂-saturated electrolytes was shown in Fig. 7a. Unlike the conventional aqueous electrolyte, the curve in DES/PC was essentially linear. The range of $-0.6$ to $-1.8$ V (vs. RHE) did not show the typical onset, linear and saturation regions indicating that Cu₀.₃Zn₉.₇ started ECO₂R at a very low reduction. Fig. 7b compares the ECO₂R performance in the two electrolytes. Fig. S12 and Fig. S13 show the detailed test results of gas products in the GC at $-0.9$ to $-1.5$ V (vs. RHE) in DES/PC electrolyte. The optimal reduction potential of Cu₀.₃Zn₉.₇ for CO was reduced to $-1$ V (vs. RHE), which corresponded to an increased FE_CO of 94.89 %. In addition, the FE_CO of Cu₀.₃Zn₉.₇ reached more than 90 % over a wide reduction potential range of $-1$ to $-1.5$ V (vs. RHE). Obviously, the DES/PC electrolyte was able to reduce the reduction potential and improve the FE_CO. The decrease in current density at the same reduction potential compared to the aqueous electrolyte is assigned to the lack of proton reduction activity exhibited by this electrolyte [48]. Fig. 7c


![](./images/937193625660424225_8.jpg)

Fig. 7. Comparison of the performance of $Cu_{0.3}Zn_{9.7}$ electrode in $0.1\ M\ KHCO_{3}$ and DES/PC cathode electrolytes. (a) LSV curves obtained in $CO_{2}$-purged. (b) $FE_{CO}$ and $FE_{H2}$ at different applied potentials. (c) Current ratio of $CO_{2}$ reduction to HER at different potentials (The result corresponds to the average of three individual measurements). (d) Radargram-based comparison of optimal $FE_{CO}$, CO partial current densities and reduction potentials. (e) Comparison of this work with published works in recent years.

confirmed this, as even at highly cathodic potentials the $H_{2}$ evolution activity in the DES/PC electrolyte is vastly lowered. As illustrated in Fig. 7d, $Cu_{0.3}Zn_{9.7}$ had a more appreciable $FE_{CO}$ and lower reduction potential in the DES/PC electrolyte. In addition, the halogen ions adsorbed on the catalyst surface during $ECO_{2}R$ process can reduce the reaction overpotential and stabilize the *COOH intermediates [49,50]. Considering the simple synthesis process and the cheap price of raw materials, we believe that the cathode electrolyte of DES/PC has a broader application prospect for $ECO_{2}R$ to CO. Finally, we compared the performance of the present work with the reported electrocatalysts in recent years (Fig. 7e and Table S3) [51-60]. The performance of the $ECO_{2}R$ to CO system reported in this work exceeded most of the reported catalysts, which was competitive and promising for application.

## 4. Conclusions

In summary, a 3D porous Zn-Cu alloy electrode was synthesized in one step using a simple hydrogen bubble template method and for $ECO_{2}R$ to CO. The characterization results show that a small amount of Cu can modulate the morphology of Zn-Cu alloy coatings. The electrode shows a non-porous Zn sheet-like structure without Cu. With the increase of Cu content, the pores on electrodes gradually became larger, and the microscopic morphology changed from "sharp cone-like" to "leaf-like", "fern-like" and irregular "cluster-like" structure. These particular morphological differences were related to the hydrophilicity of the electrode surface and differences in the hydrogen evolution kinetics of the metal. The $ECO_{2}R$ performance test results show that the $FE_{CO}$ of the $Cu_{0.3}Zn_{9.7}$ electrode at $-1.2\ V$ (vs. RHE) was $90.69\ \%$ (in $0.1\ M\ KHCO_{3}$), which was comparable to the Au and Ag foils. The regular pore structure of $Cu_{0.3}Zn_{9.7}$ provided a large ECSA, while the alloying effect of Zn and Cu played a positive role in promoting the generation of *CO, resulting in a high $ECO_{2}R$ activity. Meanwhile, $Cu_{0.3}Zn_{9.7}$ was still able to keep more than $80\ \%\ FE_{CO}$ during $8\ h$ of continuous $ECO_{2}R$. In addition, we adopted the cathodic electrolyte system of DES/PC instead of the conventional aqueous electrolyte and used it for $ECO_{2}R$. The optimal reduction potential of $Cu_{0.3}Zn_{9.7}$ for CO was reduced to $-1\ V$ (vs. RHE), corresponding to an increase in $FE_{CO}$ to $94.89\ \%$. Moreover, the electrode achieved more than $90\ \%\ FE_{CO}$ over a wide reduction potential range of -1 to $-1.5\ V$ (vs. RHE). The excellent $ECO_{2}R$ results from the direct inhibition of HER by this electrolyte, as well as the reduction of reaction overpotential and stabilization of key intermediates by halogen ions adsorbed on the electrode surface during $ECO_{2}R$. Our work proves the important regulatory roles of multi-phase metals and non-aqueous electrolytes in the $ECO_{2}R$ system and provides new ideas for designing rational $ECO_{2}R$ to CO systems.

### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Data availability

Data will be made available on request.

### Acknowledgment

The authors gratefully acknowledge the financial supports from the National Natural Science Foundation of China (52270078), the Welfare Technology Research Plan of Zhejiang Province (LZY21E080003), and the Fundamental Research Funds for the Central Universities (xzy022023039), as well as the instrumental support from Instrumental Analysis Center of Xi'an Jiaotong University.

### Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.cej.2023.147376.

---

### References

[1] J.W. Zhao, B.Q. Liu, L.S. Meng, S. He, R.S. Yuan, Y.D. Hou, Z.X. Ding, H.X. Lin, Z. Z. Zhang, X.X. Wang, J.L. Long, Plasmonic control of solar-driven CO₂ conversion at the metal/ZnO interfaces, Appl. Catal. B-Environ. 256 (2019), 117823, https://doi.org/10.1016/j.apcatb.2019.117823.

[2] J.W. Zhao, L. Xue, Z.J. Niu, L. Huang, Y.D. Hou, Z.Z. Zhang, R.S. Yuan, Z.X. Ding, X.Z. Fu, X. Lu, J.L. Long, Conversion of CO₂ to formic acid by integrated all-solar-driven artificial photosynthetic system, J. Power Sources 512 (2021), 230532, https://doi.org/10.1016/j.jpowsour.2020.230532.

[3] J.W. Zhao, L. Huang, L. Xue, Z.J. Niu, Z.Z. Zhang, Z.X. Ding, R.S. Yuan, X. Lu, J. L. Long, Selectively converting CO₂ to HCOOH on Cu-alloys integrated in hematite-driven artificial photosynthetic cells, J. Energy Chem. 79 (2023) 601-610, https://doi.org/10.1016/j.jechem.2022.12.062.

[4] J.W. Zhao, Q.Y. Huang, Z.D. Xie, Y. Liu, F.K. Liu, F. Wei, S.B. Wang, Z.Z. Zhang, R. S. Yuan, K.F. Wu, Z.X. Ding, J.L. Long, Hierarchical Hollow-TiO₂/CdS/ZnS hybrid for solar-driven CO₂-selective conversion, ACS Appl. Mater. Interfaces 15 (2023) 24494-24503, https://doi.org/10.1021/acsami.3c03255.

[5] J.W. Zhao, F.K. Liu, W.J. Wang, Y. Wang, N. Wen, Z.Z. Zhang, W.X. Dai, R.S. Yuan, Z.X. Ding, J.L. Long, S-Scheme-Heterojunction LaNiO₃/CdLa₂S₄ photocatalyst for solar-driven CO₂-to-CO conversion, ACS Appl. Nano Mater. 6 (2023) 8927-8936, https://doi.org/10.1021/acsanm.3c01443.

[6] B.Q. Miao, W.S. Fang, B. Sun, F.M. Li, X.C. Wang, B.Y. Yu, Y. Chen, Defect-rich bismuth metallene for efficient CO₂ electroconversion, Chin. J. Struct. Chem. 42 (2023), 100095, https://doi.org/10.1016/j.cjsc.2023.100095.

[7] W.F. You, X. Xu, A.H. Cao, Z.J. Tao, L.T. Kang, Synthesis of Axially coordinated cobalt porphyrin/graphene oxide nanocomposite for enhanced electrocatalytic CO₂ reduction to CO, Chin. J. Struct. Chem. 41 (2022) 2203001-2203011, https://doi.org/10.14102/j.cnki.0254-5861.2021-3247.

[8] Z.-K. Zhang, X.-S. Jing, H. Xu, Z.-C. Li, W. Yan, Advances in Design and reaction mechanism of copper-based catalysts for electrocatalytic carbon dioxide reduction, chinese, J. Anal. Chem. 51 (2023) 316-330, https://doi.org/10.19756/j.issn.0253-3820.221456.

[9] Z.W. Seh, J. Kibsgaard, C.F. Dickens, I.B. Chorkendorff, J.K. Norskov, T. F. Jaramillo, Combining theory and experiment in electrocatalysis: insights into materials design, Science 355 (2017) ead4998, https://doi.org/10.1126/science.aad4998.

[10] M. Jouny, W. Luc, F. Jiao, General techno-economic analysis of CO₂ electrolysis systems, Ind. Eng. Chem. Res. 59 (2020) 8121-8123, https://doi.org/10.1021/acs.iecr.0c01513.

[11] M. Li, Y. Hu, G. Dong, T. Wu, D. Geng, Achieving tunable selectivity and activity of CO₂ electroreduction to CO via bimetallic silver-copper electronic engineering, Small 19 (2023) 2207242, https://doi.org/10.1002/smll.202207242.

[12] L. Wan, X. Zhang, J. Cheng, R. Chen, L. Wu, J. Shi, J. Luo, Bimetallic Cu-Zn catalysts for electrochemical CO₂ reduction: phase-separated versus core-shelldistribution, ACS Catal. 12 (2022) 2741-2748, https://doi.org/10.1021/acscatal.1c05272.

[13] S. Nitopi, E. Bertheussen, S.B. Scott, X. Liu, A.K. Engstfeld, S. Horch, B. Seger, I.E. L. Stephens, K. Chan, C. Hahn, J.K. Norskov, T.F. Jaramillo, I. Chorkendorff, Progress and perspectives of electrochemical CO₂ reduction on copper in aqueous electrolyte, Chem. Rev. 119 (2019) 7610-7672, https://doi.org/10.1021/acs.chemrev.8b00705.

[14] H. Noda, S. Ikeda, Y. Oda, K. Imai, M. Maeda, K. Ito, Electrochemical reduction of carbon dioxide at various metal electrodes in aqueous potassium hydrogencarbonate solution, B. Chem. Soc. Jpn. 63 (1990) 2459-2462, https://doi.org/10.1246/bcsj.63.2459.

[15] K.P. Kuhl, T. Hatsukade, E.R. Cave, D.N. Abram, J. Kibsgaard, T.F. Jaramillo, Electrocatalytic conversion of carbon dioxide to methane and methanol on transition metal surfaces, J. Am. Chem. Soc. 136 (2014) 14107-14113, https://doi.org/10.1021/ja505791r.

[16] F. Calle-Vallejo, M.T.M. Koper, Theoretical considerations on the electroreduction of CO to C₂ species on Cu(100) electrodes, Angew. Chem. Int. Ed. 52 (2013) 7282-7285, https://doi.org/10.1002/anie.201301470.

[17] D. Kim, C. Xie, N. Becknell, Y. Yu, M. Karamad, K. Chan, E.J. Crumlin, J. K. Norskov, P. Yang, Electrochemical activation of CO₂ through atomic ordering transformations of AuCu nanoparticles, J. Am. Chem. Soc. 139 (2017) 8329-8336, https://doi.org/10.1021/jacs.7b03516.

[18] L. Wang, H. Peng, S. Lamaison, Z. Qi, D.M. Koshy, M.B. Stevens, D. Wakerley, J.A. Z. Zeledon, L.A. King, L. Zhou, Y. Lai, M. Fontecave, J. Gregoire, F. Abild-Pedersen, T.F. Jaramillo, C. Hahn, Bimetallic effects on Zn-Cu electrocatalysts enhance activity and selectivity for the conversion of CO₂ to CO, Chem. Catalysis 1 (2021) 663-680, https://doi.org/10.1016/j.checat.2021.05.006.

[19] W. Zhang, C. Xu, Y. Hu, S. Yang, L. Ma, L. Wang, P. Zhao, C. Wang, J. Ma, Z. Jin, Electronic and geometric structure engineering of bicontinuous porous Ag-Cu nanoarchitectures for realizing selectivity-tunable electrochemical CO₂ reduction, Nano Energy 73 (2020), 104796, https://doi.org/10.1016/j.nanoen.2020.104796.

[20] W. Ren, X. Tan, J. Qu, S. Li, J. Liu, X. Su, R.P. Singer, J.M. Cairney, K. Wang, S. C. Smith, C. Zhao, Isolated copper-tin atomic interfaces tuning electrocatalytic CO₂ conversion, 1449, Nat. Commun. 12 (2021), https://doi.org/10.1038/s41467-021-21750-y.

[21] K.D. Yang, W.R. Ko, J.H. Lee, S.J. Kim, H. Lee, M.H. Lee, N. Ki Tae, Morphology-directed selective production of ethylene or ethane from CO₂ on a Cu mesopore electrode, Angew. Chem. Int. Ed. 56 (2017) 796-800, https://doi.org/10.1002/anie.201610432.

[22] H. Song, M. Im, J.T. Song, J.-A. Lim, B.-S. Kim, Y. Kwon, S. Ryu, J. Oh, Effect of mass transfer and kinetics in ordered Cu-mesostructures for electrochemical CO₂ reduction, Appl. Catal. B-Environ. 232 (2018) 391-396, https://doi.org/10.1016/j.apcatb.2018.03.071.

[23] J.J. Lv, M. Jouny, W. Luc, W.L. Zhu, J.J. Zhu, F. Jiao, A Highly porous copper electrocatalyst for carbon dioxide reduction, Adv. Mater. 30 (2018) 1803111, https://doi.org/10.1002/adma.201803111.

[24] X. Su, Y. Sun, L. Jin, L. Zhang, Y. Yang, P. Kerns, B. Liu, S. Li, J. He, Hierarchically porous Cu/Zn bimetallic catalysts for highly selective CO₂ electroreduction toliquid C₂ products, Appl. Catal. B-Environ. 269 (2020), 118800, https://doi.org/10.1016/j.apcatb.2020.118800.

[25] M. Ramdin, A.R.T. Morrison, M. de Groen, R. van Haperen, R. de Kler, L.J.P. van den Broeke, J.P.M. Trusler, W. de Jong, T.J.H. Vlugt, High pressure electrochemical reduction of CO₂ to formic acid/formate: a comparison between bipolar membranes and cation exchange membranes, Ind. Eng. Chem. Res. 58 (2019) 1834-1847, https://doi.org/10.1021/acs.iecr.8b04944.

[26] L. Zhang, Z.J. Zhao, J.L. Gong, Nanostructured materials for heterogeneous electrocatalytic CO₂ reduction and their related reaction mechanisms, Angew. Chem. Int. Ed. 56 (2017) 11326-11353, https://doi.org/10.1002/anie.201612214.

[27] X. Tan, X. Sun and B. Han, Ionic liquid-based electrolytes for CO₂ electroreduction and CO₂ electroorganic transformation, Natl. Sci. Rev. 9 (2022) nwab022. 10.1093/nsr/nwab022.

[28] L.L. Snuffin, L.W. Whaley, L. Yu, Catalytic electrochemical reduction of CO₂ in ionic liquid EMIMBF₄Cl, J. Electrochem. Soc. 158 (2011) F155-F158, https://doi.org/10.1149/1.3606487.

[29] Q.G. Zhu, J. Ma, X.C. Kang, X.F. Sun, H.Z. Liu, J.Y. Hu, Z.M. Liu, B.X. Han, Efficient reduction of CO₂ into formic acid on a lead electrode using an ionic liquid catholyte mixture, Angew. Chem. Int. Ed. 55 (2016) 9012-9016, https://doi.org/10.1002/anie.201601974.

[30] T. El Achkar, H. Greige-Gerges, S. Fourmentin, Basics and properties of deep eutectic solvents: a review, Environ. Chem. Lett. 19 (2021) 3397-3408, https://doi.org/10.1007/s10311-021-01225-8.

[31] B.B. Hansen, S. Spittle, B. Chen, D. Poe, Y. Zhang, J.M. Klein, A. Horton, L. Adhikari, T. Zelovich, B.W. Doherty, B. Gurkan, E.J. Maginn, A. Ragauskas, M. Dadmun, T.A. Zawodzinski, G.A. Baker, M.E. Tuckerman, R.F. Savinell, J. R. Sangoro, Deep eutectic solvents: a review of fundamentals and applications, Chem. Rev. 121 (2021) 1232-1285, https://doi.org/10.1021/acs.chemrev.0c00385.

[32] H.-C. Shin, M.L. Liu, Copper foam structures with highly porous nanostructured walls, Chem. Mater. 16 (2004) 5460-5464, https://doi.org/10.1021/cm040887b.

[33] G. Kresse, J. Furthmüller, Efficiency of Ab-Initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6 (1) (1996) 15-50, https://doi.org/10.1016/0927-0256(96)00008-0.

[34] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (24) (1994) 17953-17979, https://doi.org/10.1103/PhysRevB.50.17953.

[35] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Atoms, molecules, solids, and surfaces: applications of the generalized gradient approximation for exchange and correlation, Phys. Rev. B 46 (11) (1992) 6671-6687, https://doi.org/10.1103/PhysRevB.46.6671.

[36] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (18) (1996) 3865-3868, https://doi.org/10.1103/PhysRevLett.77.3865.

[37] S. Grimme, J. Antony, S. Ehrlich, H. Krieg, A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu, J. Chem. Phys. 132 (15) (2010), 154104, https://doi.org/10.1063/1.3382344.

[38] P. Moreno-Garcia, N. Schlegel, A. Zanetti, A. C. Lopez, M. d. J. Galvez-Vazquez, A. Dutta, M. Rahaman and P. Broekmann, Selective Electrochemical Reduction of CO₂ to CO on Zn-Based Foams Produced by Cu²⁺ and Template-Assisted Electrodeposition, ACS Appl. Mater. Interfaces 10 (2018) 31355-31365. 10.1021/acsami.8b09894.

[39] B.N. Afanas'ev, Y.P. Akulova, A correlation between the hydrophilicity of a metal and its surface tension. Calculation of the bond energy of water molecules adsorbed on an uncharged metal surface, Prot. Met. Chem.+ 36 (2000) 25-30, https://doi.org/10.1007/BF02766735.

[40] S. Trasatti, Work function, electronegativity, and electrochemical behaviour of metals: III. Electrolytic hydrogen evolution in acid solutions, J. Electroanal. Chem. 39 (1972) 163-184, https://doi.org/10.1016/S0022-0728(72)80485-6.

[41] G. Yin, H. Abe, R. Kodiyath, S. Ueda, N. Srinivasan, A. Yamaguchi, M. Miyauchi, Selective electro- or photo-reduction of carbon dioxide to formic acid using a Cu-Zn alloy catalyst, J. Mater. Chem. A 5 (2017) 12113-12119, https://doi.org/10.1039/C7TA00353F.

[42] S. Lamaison, D. Wakerley, D. Montero, G. Rousse, D. Taverna, D. Giaume, D. Mercier, J. Blanchard, H.N. Tran, M. Fontecave, V. Mougel, Zn-Cu Alloy nanofoams as efficient catalysts for the reduction of CO₂ to syngas mixtures with a potential-independent H₂/CO ratio, Chem. Sus. Chem. 12 (2019) 511-517, https://doi.org/10.1002/cssc.201802287.

[43] Y. Xue, H. Li, X. Ye, S. Yang, Z. Zheng, X. Han, X. Zhang, L. Chen, Z. Xie, Q. Kuang, L. Zheng, N-doped carbon shell encapsulated PtZn intermetallic nanoparticles as

highly efficient catalysts for fuel cells, Nano Res. 12 (2019) 2490-2497, https://doi.org/10.1007/s12274-019-2473-x.

[44] X. Hu, C. Zhao, X. Hu, Q. Guan, Y. Wang, W. Li, Nitrogen-doped carbon cages encapsulating CuZn alloy for enhanced CO₂ Reduction, ACS Appl. Mater. Interfaces 11 (2019) 25100-25107, https://doi.org/10.1021/acsami.9b03488.

[45] W.C. Ma, X.Y. He, W. Wang, S.J. Xie, Q.H. Zhang, Y. Wang, Electrocatalytic reduction of CO₂ and CO to multi-carbon compounds over Cu-based catalysts, Chem. Soc. Rev. 50 (2021) 12897-12914, https://doi.org/10.1039/D1CS00535A.

[46] A. Bagger, W. Ju, A.S. Varela, P. Strasser, J. Rossmeisl, Electrochemical CO₂ Reduction: A Classification Problem, ChemPhysChem 18 (2017) 3266-3273, https://doi.org/10.1002/cphc.201700736.

[47] E.R. Cave, C. Shi, K.P. Kuhl, T. Hatsukade, D.N. Abram, C. Hahn, K. Chan, T. F. Jaramillo, Trends in the Catalytic Activity of Hydrogen Evolution during CO₂ Electroreduction on Transition Metals, ACS Catal. 8 (2018) 3035-3040, https://doi.org/10.1021/acscatal.7b03807.

[48] D. Wakerley, S. Lamaison, F. Ozanam, N. Menguy, D. Mercier, P. Marcus, M. Fontecave, V. Mougel, Bio-inspired hydrophobicity promotes CO₂ reduction on a Cu surface, Nat. Mater. 18 (2019) 1222-1227, https://doi.org/10.1038/s41563-019-0445-x.

[49] H. Yang, S. Li, Q. Xu, Efficient strategies for promoting the electrochemical reduction of CO2 to C2+ products over Cu-based catalysts, Chinese, J. Catal. 48 (2023) 32-65, https://doi.org/10.1016/S1872-2067(23)64429-8.

[50] S. Garg, M.R. Li, T.E. Rufford, L. Ge, V. Rudolph, R. Knibbe, M. Konarova, G.G. X. Wang, Catalyst-electrolyte interactions in aqueous reline solutions for highly selective electrochemical CO₂ reduction, Chem. Sus. Chem. 13 (2020) 304-311, https://doi.org/10.1002/cssc.201902433.

[51] S. Gong, X. Xiao, W. Wang, D.K. Sam, R. Lu, Y. Xu, J. Liu, C. Wu, X. Lv, Silk fibroin-derived carbon aerogels embedded with copper nanoparticles for efficient electrocatalytic CO₂-to-CO conversion, J. Colloid Interf. Sci. 600 (2021) 412-420, https://doi.org/10.1016/j.jcis.2021.05.054.

[52] W. Ju, F. Jiang, H. Ma, Z. Pan, Y.-B. Zhao, F. Pagani, D. Rentsch, J. Wang, C. Battaglia, Electrocatalytic reduction of gaseous CO₂ to CO on Sn/Cu-nanofiber-based gas diffusion electrodes, Adv. Energy Mater. 9 (2019) 1901514, https://doi.org/10.1002/aenm.201901514.

[53] W. Zhang, P. He, C. Wang, T. Ding, T. Chen, X. Liu, L. Cao, T. Huang, X. Shen, O. A. Usoltsev, A.L. Bugaev, Y. Lin, T. Yao, Operando evidence of Cu+ stabilization via a single-atom modifier for CO2 electroreduction, J. Mater. Chem. A 8 (2020) 25970-25977, https://doi.org/10.1039/D0TA08369K.

[54] H. Rabiee, L. Ge, X. Zhang, S. Hu, M. Li, S. Smart, Z. Zhu, H. Wang, Z. Yuan, Stand-alone asymmetric hollow fiber gas-diffusion electrodes with distinguished bronze phases for high-efficiency CO₂ electrochemical reduction, Appl. Catal. B-Environ. 298 (2021), 120538, https://doi.org/10.1016/j.apcatb.2021.120538.

[55] Y. Wu, K. Iwase, T. Harada, S. Nakanishi, K. Kamiya, Sn Atoms on Cu Nanoparticles for Suppressing Competitive H₂ Evolution in CO₂ Electrolysis, ACS Appl. Nano Mater. 4 (2021) 4994-5003, https://doi.org/10.1021/acsanm.1c00514.

[56] M. Abdinejad, Z. Mirza, X.A. Zhang, H.-B. Kraatz, Enhanced Electrocatalytic Activity of Primary Amines for CO₂ Reduction Using Copper Electrodes in Aqueous Solution, ACS Sustain. Chem. Eng. 8 (2020) 1715-1720, https://doi.org/10.1021/acssuschemeng.9b06837.

[57] M. Abdinejad, C. Ferrag, M.N. Hossain, M. Noroozifar, K. Kerman, H.B. Kraatz, Capture and electroreduction of CO₂ using highly efficient bimetallic Pd-Ag aerogels paired with carbon nanotubes, J. Mater. Chem. A 9 (2021) 12870-12877, https://doi.org/10.1039/D1TA01834E.

[58] J. Hao, H. Zhu, Y. Li, P. Liu, S. Lu, F. Duan, W. Dong, Y. Lu, T. Liu, M. Du, Tuning the electronic structure of AuNi homogeneous solid-solution alloy with positively charged Ni center for highly selective electrochemical CO₂ reduction, Chem. Eng. J. 404 (2021), 126523, https://doi.org/10.1016/j.cej.2020.126523.

[59] Z. Yin, D. Gao, S. Yao, B. Zhao, F. Cai, L. Lin, P. Tang, P. Zhai, G. Wang, D. Ma, X. Bao, Highly selective palladium-copper bimetallic electrocatalysts for the electrochemical reduction of CO₂ to CO, Nano Energy 27 (2016) 35-43, https://doi.org/10.1016/j.nanoen.2016.06.035.

[60] D. Wei, Y. Wang, C.-L. Dong, Z. Zhang, X. Wang, Y.-C. Huang, Y. Shi, X. Zhao, J. Wang, R. Long, Y. Xiong, F. Dong, M. Li, S. Shen, Decrypting the Controlled Product Selectivity over Ag-Cu Bimetallic Surface Alloys for Electrochemical CO₂ Reduction, Angew. Chem. Int. Ed. 62 (2023) e202217369.