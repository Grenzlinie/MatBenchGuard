# Strain stiffening, high load-invariant hardness, and electronic anomalies of boron phosphide under pressure

Rui Gui, $^{1}$ Zhe Xue, $^{2}$ Xuefeng Zhou, $^{1}$ Chao Gu, $^{1}$ Xiangting Ren, $^{1}$ Hu Cheng, $^{1}$ Dejiang Ma, $^{1}$ Jiaqian Qin $^{\circledR},^{1,3}$ Yongcheng Liang, $^{1,4}$ Xiaozhi Yan, $^{1}$ Jianzhong Zhang $^{\circledR},^{5}$ Xinyu Zhang, $^{2, *}$ Xiaohui Yu, $^{6}$ Liping Wang, $^{1}$ Yusheng Zhao, $^{1, \dagger}$ and Shanmin Wang $^{1, \ddagger}$

$^{1}$ Department of Physics & SUSTech Academy for Advanced Interdisciplinary Studies, Southern University of Science & Technology, Shenzhen, Guangdong, 518055, China
$^{2}$ State Key Lab of Metastable Materials Science & Technology, Yanshan University, Qinhuangdao, 066004, China
$^{3}$ Metallurgy and Materials Science Research Institute, Chulalongkorn University, Bangkok 10330, Thailand
$^{4}$ College of Science, Donghua University, Shanghai 201620, China
$^{5}$ Materials Science & Technology Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA
$^{6}$ Institute of Physics, Chinese Academy of Sciences, Beijing, 100190, China

![](./images/812690882233892865_1.jpg)
(Received 5 September 2019; revised manuscript received 15 December 2019; published 15 January 2020)

New refractory hard materials with a favorable band gap are in high demand for the next-generation semiconductors capable of withstanding high temperature and other hostile environments. Boron phosphide (BP) is such an attractive candidate with exceptional properties; however, it has mainly been studied theoretically because of the difficulty in sample preparation. In this work, we report successful synthesis of large millimeter-sized single-crystal BP. The final product has a zinc-blende structure with a unique electronic structure and is optically transparent with a moderate band gap of $\sim$2.1 eV. Our experiments, in conjunction with *ab initio* simulations, reveal that the compound exhibits extraordinary strain stiffening and unusually high load-invariant hardness of $\sim$38 (3) GPa, which is close to the 40-GPa threshold for superhard materials, making BP the hardest among all known semiconductors. Based on the first-principles calculations, the fracture mechanisms in BP under tensile and shear deformations can be attributed to the formation of a metastable hexagonal phase. Further spectroscopic measurements indicate that an unusual electronic transition occurs at high pressures of $\sim$13 GPa, resulting in an asymptotically enhanced covalent bonding state. The pressure dependence of multiphonon processes is also determined by Raman measurement. In addition, our studies suggest a phonon-assisted photoluminescence process and evidence for the photon-pumped étalon effect at 707 nm.

DOI: 10.1103/PhysRevB.101.035302

## I. INTRODUCTION

Wide band gap crystalline solids made of light elements (e.g., SiC) are a class of new-generation semiconductors for many technological applications. Owing to their exceptional properties, mainly including superior thermal conductivity, high breakdown voltage, and low effective mass [1], they hold great promise for revolutionizing almost every aspect of industry [1,2]. Of particular interest is developing superhard semiconductors for extreme environments, such as high temperature, high stress, and high radiation [3]. Capabilities of withstanding these harsh conditions are arguably attributed to the materials' unique electronic structure and strong covalent bonds [1]. Accordingly, a rational design of superhard semiconducting solids can be achieved by incorporating light elements (e.g., B and N) into the lattice of heavier base elements (e.g., Al and Si). Similar electronegativities for the constituent atoms would favor the formation of a strong covalent network and hence strengthen the materials' mechanical properties.

Among these solids, the IV-IV and III-V compounds such as SiC, GaN, and AlN are by far the most widely explored chemistry for the next-generation semiconductors [1]. Remarkably, all these compounds are isovalent with an identical valence electron concentration (VEC) of eight electrons per formula, resembling that in diamond. Therefore, most of them preferably crystallize in a diamondlike or similar structure with a strong covalent bonding network [1]. As a result, the hardness of these materials is inherently high (e.g., $\sim$26--30 GPa for SiC) [4,5], although still far below the 40-GPa threshold commonly defined for superhard materials [6,7]. This is primarily due to the presence of an appreciable amount of ionic bonds in these materials, which would result in sizable strain softening under indentation and significantly lower their hardness [8,9]. Also noted is that the N- or Si-based valence characters and phonon bands often bring about relatively low charge mobility and degraded thermal conductivity. Besides, the band gaps in many of these materials are greater than 3 eV, which will severely impede the development of new devices that require energy gaps in the optically visible range.

Alternative to nitrides and carbides, conventional superhard materials such as diamond and cubic boron nitride (c-BN) have also been the focus of the development of new-generation semiconductors for high-performance devices [3].

*xyzhang@ysu.edu.cn
†zhaoys@sustech.edu.cn
‡wangsm@sustech.edu.cn

However, synthesizing these materials often involves stringent high-pressure and high-temperature conditions, leading to high production cost and low yield. These constraints, along with difficulties in integration and extralarge band gaps (i.e., above 5 eV), have posed an insurmountable barrier to their widespread use. As a result, despite decades of intensive efforts, the search for superhard semiconductors is still limited to only a few material systems, calling for entirely new materials with desired properties to mitigate the above-mentioned issues.

As a sister semiconductor in the III-V material system, zinc-blende boron phosphide (BP) is structurally isotypic with c-BN, making it a highly promising superhard solid with a finite band gap. Although the first study on BP can be traced back to as early as the 1950s [10-12], only a handful of reports have since been published [1,13-17]. This compound remains relatively unknown including its mechanical, electronic, and optical properties, mainly because synthesizing a high-quality BP sample is still challenging. Consequently, BP is lagging far behind other III-V materials in terms of both fundamental studies and industrial applications. Recently, there has been a resurgence of interest in BP, and a record-high thermal conductivity of $460-540\ \mathrm{W\ m^{-1}\ K^{-1}}$ was reported for a single-crystal sample at room temperature [18,19], indicative of a great potential for advanced heat sink applications. Additional computational studies indicate that BP is one of the most promising $p$-type candidates with optical transparency, ultralow effective mass, and high charge mobility, in striking contrast to the known oxides and nitrides [20]. Besides, $n$-type BP has also been used as a metal-free and visible-light-active photocatalyst for hydrogen evolution [21]. At high pressure, several structural transitions in BP have theoretically been predicted, accompanied by interesting electronic transitions including superconductivity [22,23]. Anomalous behaviors in the effective charges and phonon modes of BP have been investigated in Refs. [14,15,24]. Very recently, Solozhenko and Bushlya have reported high Vickers hardness of $\sim 30$ GPa and fracture toughness of $\sim 2\ \mathrm{MPa\ m^{1/2}}$ for BP [17], implying excellent mechanical properties. However, such mechanical properties are mainly determined based on a polycrystalline sample; the grain size and defects would have a profound influence for obtaining its intrinsic properties. Inspired by these findings, we have in this work synthesized high-quality single-crystal BP and systematically investigated its structural, electronic, optical, and mechanical properties, leading to the discovery of BP as a transparent quasisuperhard semiconductor with evidence for the photoluminescence-induced étalon effect. In combination with the first-principles calculations, the origin of its superior hardness and the fracture mechanism under tensile and shear deformations have also been elucidated.

## II. EXPERIMENTAL SECTION

**Synthesis.** BP powders were synthesized from stoichiometric reaction between high-purity B and P powders at $850\ ^{\circ}\mathrm{C}$-$1100\ ^{\circ}\mathrm{C}$ in vacuum. The flux method was exploited for growing large single crystals from starting materials of B and P powders with nickel metal as a solvent, in a molar ratio of $\mathrm{B:P:Ni}=2.5:2.5:1$. A similar reaction route has previously been reported in Ref. [25] and an overview of the synthesis of BP can also been found therein. To avoid possible contamination, the admixed sample powders were sealed in quartz tubes in a vacuum environment and then heated in a muffle furnace. In each experimental run, the sample was first heated at $1150\ ^{\circ}\mathrm{C}$-$1200\ ^{\circ}\mathrm{C}$ for 16 h, followed by cooling to $1100\ ^{\circ}\mathrm{C}$ at a rate of $3\ ^{\circ}\mathrm{C/h}$ and then quenching to ambient temperature at a rate of $300\ ^{\circ}\mathrm{C/h}$. Attempts to use nickel phosphide (i.e., $\mathrm{Ni_{2}P}$) as a solvent for growing BP single crystals were unsuccessful, though using $\mathrm{Ni_{12}P_{5}}$ and $\mathrm{Cu_{3}P}$ as solvents under pressure has previously been reported [25]. The recovered sample was washed with mixed acids of HCl and $\mathrm{HNO_{3}}$ (i.e., aqua regia) to remove the byproducts of white phosphorus and $\mathrm{Ni_{x}P}$, and the final product was phase-pure and surface-clean single crystals.

**Characterization.** The as-prepared samples were examined by x-ray diffraction (XRD) with $\mathrm{Cu\ K}\alpha$ radiation and the crystal structure was determined from the Rietveld analysis of XRD data using the GSAS program [26]. Microstructures of the sample were characterized by a field emission scanning electron microscope (FE-SEM) and a Leica M205C microscope. X-ray photoelectron spectroscopy (XPS) measurements were performed to determine the electronic structure. The band gap, optical absorption and emission, and phonon properties were characterized using ultraviolet-visible (UV-Vis), infrared (IR), Raman, and photoluminescence (PL) spectrometers. Thermal stabilities were evaluated using a simultaneous thermogravimetric analysis (TGA) and differential scanning calorimeter (DSC) measurements in an Ar atmosphere. Several TGA-DSC measurements have been performed in air, but they were all unsuccessful, due to the failure of the Pt-Ru alloy sensor, probably damaged by the decomposed phosphorus and oxygen.

Vickers hardness was measured for single-crystal BP under different loads of 98, 245, and 490 mN using an FM-810 hardness tester. Because of the limited crystallite size of single crystals, attempts to increase the load for determination of hardness led to complete cracking of the single crystals. Under each applied load, the measurement was taken with a dwelling time of 15 s and repeated five to ten times to obtain statistically improved averages. Single crystals of BP were mounted on a $\mathrm{SiO_{2}}$ substrate using epoxy resin, and surfaces of random crystallographic orientation were prepared with mirror quality for the measurement. Nanoindentation hardness measurements were also performed at a series of fixed target maximum displacements of 10, 20, 40, 60, 80, 100, and 120 nm, using a Berkovich indenter and a displacement control mode with a strain rate of $0.05\ \mathrm{s^{-1}}$. The loading time and holding time were 46 and 20 s, respectively. The reduced or combined effective elastic modulus was derived using the well-known Oliver-Pharr method [27].

High-pressure ($P$) angle-dispersive synchrotron XRD experiments using a diamond-anvil cell (DAC) were performed up to $\sim 27$ GPa at the beamline of 4W2/BSRF. High-$P$ Raman and PL spectra were obtained using a 532-nm excitation laser at room temperature. In each high-$P$ experiment, the single-crystal or powdered BP sample was loaded into the sample hole in a rhenium gasket preindented to $\sim 30\ \mu\mathrm{m}$ thickness with neon as the pressure-transmitting medium. A few ruby balls were also loaded in the same sample hole to serve as

![](./images/812690882233892865_2.jpg)

FIG. 1. Structure and morphology of as-prepared samples. (a) Refined XRD pattern for sample powders synthesized at 1000 °C for 2 h. Black circles and red lines denote the observed and calculated profiles, respectively. The difference curve between the observed and calculated profiles is shown in cyan color. The blue tick marks correspond to the peak positions. Inset is the crystal structure of BP with the zinc-blende symmetry. (b) Optical images of typical BP single crystals grown at 1200 °C (upper panel, in orange) and 1150 °C (bottom panel, in golden yellow). The scale bar for both optical images is 200 $\mu$m.

![](./images/812690882233892865_3.jpg)

FIG. 2. Thermal stability analysis for BP. Thermogravimetry-differential thermal analysis, TG-DTG, performed in an Ar atmosphere. The decomposition of BP starts at $T_d = 1135(5)\,^\circ\text{C}$ with a rate of $\sim$7.6 mg/min at around 1200 °C. At a relatively low temperature of $\sim$670 °C, a clear fluctuation in weight that would be attributed to the disassociation of surface adsorbed gases. Attempts to determine the thermal stability of BP in air is unsuccessful, because the Pt-Rh thermocouple of the instrument was damaged by an unknown process, likely an associated reaction between Pt-Rh and decomposed P.

the internal pressure standard [28]. More experimental details for in situ high-P DAC measurements can be found elsewhere [29]. The optical quality of the diamond anvils was checked by the relative intensity of the second-order phonon bands located at $2160-2680\,\text{cm}^{-1}$ (or 2.06-2.0 eV) [30], based on the Raman measurement. In this work, the intensity of the second-order multiphonons Raman transition is about 1.5 times the intensity of the background fluorescence of our diamond, indicating a quite good signal-to-noise ratio for optical measurement [31].

Calculations. Ab initio simulations were performed using the density functional theory (DFT) with the generalized gradient approximation (GGA) and the Perdew-Burke- Ernzerhof (PBE) functionals implemented in the Vienna Ab initio Simulation Package (VASP) code [32,33]. The ion-electron interaction was described by the projector augmented wave (PAW) method [34], both the B $2s^22p^1$ and P $3s^23p^3$ states were treated explicitly as valence electrons. A kinetic energy cutoff of 600 eV was used for all calculations and a $15\times15\times15$ Gamma centered Monkhorst-Pack $k$-point mesh was employed for structural relaxations [35]. The convergence criteria for the Hellmann-Feynman force and total energy were set at $0.01\,\text{eV}/\mathring{\text{A}}$ and $10^{-6}\,\text{eV}$ per atom, respectively. To accurately calculate the electronic structure, the $k$-point meshes were increased up to $25\times25\times25$ with the PEB method corrected by the hybrid functional (HSE06). To calculate the phonon dispersions, a $3\times3\times3$ supercell (i.e., $\text{B}_{27}\text{P}_{27}$) and high convergence criteria of $10^{-8}\,\text{eV}/\text{atom}$ and $10^{-3}\,\text{eV}/\mathring{\text{A}}$ were used for optimization of energies and atomic forces to achieve high accuracies, respectively.

### III. RESULTS AND DISCUSSION

Figure 1(a) shows a typical XRD pattern for BP powders synthesized at 1000 °C with a duration of 2 h. Apparently, the final product is phase pure and adopts a cubic, zinc- blende structure with space group $F\overline{4}3m$ (No. 216), which is structurally isotypic with most III-V and IV-IV compounds (i.e., diamondlike materials) such as AlN and SiC [1,36]. As mentioned above, all these compounds have an identical VEC of 8, a unique electronic attribute that favors the formation of zinc-blende or wurtzite crystal structure. The refined lattice parameters for BP are sensitive to the synthesis temperature ($T$). At 1100 °C, the maximum value $a = 4.5400(3)\,\mathring{\text{A}}$ is reached; however, below or above this temperature, the produced sample is either nanocrystalline or phosphorus defi- cient, resulting in slightly reduced lattice parameters (see Fig. S1 in the Supplemental Material [37]; also see [15,24,38,39]). As presented in Fig. 1(b), the recovered crystals display a plateletlike shape and have clean and well-defined crystalline facets with grain size up to a few millimeters. Strikingly, the crystals are transparent and show a yellow color for the sample synthesized at 1150 °C. In fact, the determined band gap, $E_g$, for BP is $\sim$2.1 eV (see Fig. S2 in the Supplemental Material [37]), corresponding to the energy of the yellow color within the optically visible region. From this point of view, the color of BP crystals originates from its band gap. At a

![](./images/812690882233892865_4.jpg)

FIG. 3. XPS measurements and valence states of BP. (a) XPS spectra of B1s, P2s, and P2p. (b) XPS spectra of P $2p_{3/2,1/2}$. In (a,b), the solid dots and red solid lines in the top panels denote the observed and fitted XPS spectra, respectively. The solid red lines in the bottom panels are fitted XPS spectra for P2s, P2p, and B1s. On the high-energy shoulder of the main peak in (a,b), a few weak peaks occur and may correspond to some unidentified oxides such as $PO_4^{3-}$ and $B_2O_3$, likely associated with possible surface contamination of the sample. (c) Binding energy of B1s of the known compounds as a function of valence states of boron. The linear relationship has a slope of $\sim$1.46 eV/valence state. (b,c) Binding energy of P2p and P2s of the known compounds as a function of valence states of phosphorus. Because the split of P2p is very small, the average value of P2p is used to evaluate the valence state of P.

higher temperature of 1200 °C, the obtained crystals possess a dark yellow color, an indication of slightly reduced band gap [Fig. 1(b)], owing to thermally induced substoichiometry in the sample (i.e., $x<1$ in $BP_x$). Indeed, our thermal analysis in Fig. 2 shows that the decomposition temperature is determined to be $\sim$1135 °C in an Ar atmosphere. Clearly, for the sample synthesized at 1200 °C, more crystalline defects should exist than that of the sample synthesized at 1150 °C. These findings indicate that the tuning of the synthesis temperatures provides an effective approach to alter the band gap and color of BP by changing phosphorus concentration $x$ in $BP_x$.

As a rarely studied member of diamondlike compounds, BP also has a three-dimensional bonding network with both covalent and ionic bond characters as determined by our XPS experiment (see Fig. 3). Analyses of XPS spectra of P and B in Figs. 3(a) and 3(b) give the binding energies of 187.74, 129.98, 130.92, and 188.61 eV for P2s, P$2p_{3/2}$, P$2p_{1/2}$, and B1s states. To evaluate the valence states of BP, the relations between the valence states and binding energies for B and P in Figs. 3(c)-3(e) are established by a series of known compounds as listed in Table I. The thus-measured valence states for both B and P are close to $+0.5$ and $-0.5$, respectively. This indicates a peculiar electronic configuration of $B^{0.5+}P^{0.5-}$, which significantly deviates from the value of 3 in the pure ionic sample (i.e., $B^{3+}P^{3-}$). On the other hand, it is much closer to that of the pure covalent end member

<table><caption>TABLE I. Summary of binding energies of B1s and P2p for BP and a number of typical B- and P-bearing compounds (all in units of eV).</caption>
<tbody><tr><th rowspan="2">Material</th><th rowspan="2">Valence state</th><th colspan="2">P2p</th><th rowspan="2">P2s</th><th rowspan="2">B1s</th><th rowspan="2">Reference</th></tr><tr><th>P 2p<sub>3/2</sub></th><th>P 2p<sub>1/2</sub></th></tr><tr><td>BP</td><td>B<sup>0.5+</sup>, P<sup>0.5−</sup></td><td>129.98</td><td>130.92</td><td>187.74</td><td>188.61</td><td>This work</td></tr><tr><td>P</td><td>P<sup>0</sup></td><td></td><td>129.7</td><td>187</td><td>–</td><td>Ref. [48]</td></tr><tr><td>Zn<sub>3</sub>P<sub>2</sub></td><td>P<sup>3−</sup></td><td></td><td>128.3</td><td>185.9</td><td>–</td><td>Ref. [49]</td></tr><tr><td>FePO<sub>4</sub></td><td>P<sup>5+</sup></td><td></td><td>135</td><td>192.52</td><td>–</td><td>Ref. [50]</td></tr><tr><td>MgB<sub>2</sub></td><td>B<sup>−</sup></td><td colspan="2">—</td><td>–</td><td>186.6</td><td>Ref. [51]</td></tr><tr><td>β-B</td><td>B<sup>0</sup></td><td colspan="2">—</td><td>–</td><td>187.9</td><td>Ref. [52]</td></tr><tr><td>B<sub>2</sub>O<sub>3</sub></td><td>B<sup>3+</sup></td><td colspan="2">—</td><td>–</td><td>192.4</td><td>Ref. [52]</td></tr></tbody></table>

(i.e., B<sup>1−</sup>P<sup>1+</sup>), which has a strong covalent bond formed from the hybridization of $sp$ bands. Clearly, the covalent bonding state in BP prevails and will sufficiently strengthen the crystal lattice, which would lead to excellent mechanical properties.

To assess the hardness of BP, we performed nano- and microindentation measurements for BP based on the single-crystal samples, as shown in Fig. 4. Plots in Fig. 4(a) are the load-displacement data for nanoindentation, and the separation between loading and unloading starts to occur above the critical displacement of 40 nm or the critical load of 1.6 mN, below which the elastic deformation overwhelms under indentation (also see Figs S3 and S4 in the Supplementary Material [37]). Compared with the loading process that involves both elastic and plastic deformations, only elastic deformation takes place under indentation upon unloading [27,40]. For the measurements above the critical load, the elastic unloading processes can well be described by a similar power law, $\alpha(h-h_{f})^{\gamma}$. The thus-derived exponential value $\gamma \approx 1.383$ is identical to the theoretical value of 1.38 based on the effective shape concept for nanoindentors [40]. In

![](./images/812690882233892865_5.jpg)

FIG. 4. Hardness and elastic properties of BP determined using nano- and microindentation methods. (a) Load-displacement data taken during different loading and unloading cycles at a series of target maximum displacements or loads. Red dashed line denotes a fit of the load versus displacement to a power low, $\alpha(h-h_{f})^{\gamma}$, for the elastic unloading process under an 8-mN load. The blue dashed line defines the slope for the upper portion of the unloading curve (i.e., contact stiffness). The derived parameters are included in (a). (b) Hardness and reduced effective elastic modulus as a function of indenter displacement based on the data in (a). (c) Vickers hardness ($H_{V}$) and fracture toughness ($K_{\text{IC}}$) versus the applied load for single-crystal BP. Inset is a typical SEM image to show the indentation pyramid with cracks at a load of 490 mN. (d) $H_{V}$ as a function of the product $k^{2}G$($k = G/B$) for a number of semiconductors. Inset is hardness versus band gap for typical refractory semiconductors.

addition, the elastic unloading stiffness $S$, defined by the slope of the upper portion of the unloading curve, is also calculated with a value of 0.116 mN/nm.

The determined hardness and effective elastic modulus for BP are plotted in Fig. 4(b) as a function of maximum displacement. At small loads or displacements, because of the indentation size effect both hardness and modulus are small but increase rapidly as the displacement increases. Above the 40-nm critical displacement, the plateau values of 37 (3) and 275 (10) GPa are reached, respectively. Apparently, the load-invariant hardness is unexpectedly high and nearly in the superhard regime with a threshold value of 40 GPa. To further confirm the hardness measurement, a microindentation experiment was also performed, and the measured Vickers hardness $H_V$ is plotted in Fig. 4(c) as a function of load. At a small load of 98 mN, the measured hardness is $H_V \approx 50$ GPa. Using asymptotic leveling as a criterion, the load-independent hardness value of 38 (3) GPa is achieved under loads of 245 and 490 mN, which is in excellent agreement with the results of nanoindentation. It has come to our attention that a relatively low hardness value of $\sim$30 GPa was reported in Ref. [17], probably because their experiment is primarily based on sintered polycrystalline samples and the hardness is often extrinsically affected by the sintering quality, grain boundary and size, and defects. Compared with SiC [5], the $H_V$ value of BP is leveled off at a much smaller critical load of 245 mN, close to that of most hard transition-metal carbides and nitrides with outstanding toughness [41,42]. Besides, as will be discussed later, BP exhibits extraordinary ductility, which may also be responsible for its low critical load, in striking contrast to conventional brittle ceramics with high critical loads for achieving load-invariant hardness [43]. Thus, the fracture toughness $K_{\text{IC}}$ of BP can also be evaluated from the radial cracks produced in the measurement of Vickers hardness (Refs. [17,44,45]) and the determined value is $\sim 3.0$ MPa$\,$m$^{1/2}$, close to that of diamond and cubic boron nitride (c-BN) and much larger than that of SiC($\sim$ 1.8 MPa$\,$m$^{1/2}$) [5]. The mechanisms underlying the high toughness will be discussed later based on theoretical calculations.

It is worth mentioning that the calculated bulk modulus ($B$) and shear modulus ($G$) of BP are $\sim$162 and $\sim$165 GPa, respectively, close to that reported in Ref. [23]. By a compression experiment [15], Solozhenko *et al.* have measured its bulk modulus of $B \approx 174$ GPa, which is slightly larger than the calculated values, probably due to the influence of non-hydrostatic pressure conditions as frequently occurs in high-$P$ experiments. To keep the discussion consistent in this work, the theoretical values of $B = 162$ GPa and $G = 165$ GPa are hereafter selected for the following discussion and calculations. Remarkably, such elastic moduli of BP are dramatically lower than those of most refractory materials [46,47]. From this viewpoint, BP is mechanically unfavorable to form superhard material. To establish the correlation between elastic moduli and hardness in BP, we plot in Fig. 4(d) the $H_V$ against $k^2 G$($k = G/B$) for a number of semiconductors. Clearly, the $H_V$ obeys the power-law relation as proposed by Chen *et al.* [18], which is given by

$$
H_V = 2(k^2 G)^{0.585} - 3. \tag{1}
$$

Interestingly, the calculated hardness is $H_V = 37.5$ GPa, in excellent agreement with experimental observations. Considering the relatively low shear modulus, the hardness in BP is intimately related to the ratio $k$, which has a large value of 1.02 and is the third highest after only those of c-BN (i.e., 1.04) and diamond (i.e., 1.20) [46]. As is commonly accepted, elastic properties often do not give an accurate account of a material's hardness. In contrast, the parameter $k$ is in this regard a more reliable indicator and can be used for prediction of new superhard material. A comparison between BP and other known refectory semiconductors in Fig. 4(d) indicates that BP is the hardest semiconductor with a moderate band gap of $\sim$2.1 eV within the visible spectrum range. A suitable band gap would facilitate the tailoring of the electronic properties of BP, which is one of the major advantages over most of its competitors with large band gaps exceeding 3 eV. In conjunction with its high thermal and chemical stability, this compound is readily available for a wide variety of applications under extreme working conditions, especially in devices of high power, high voltage, and high frequency.

The stress-strain relations from *ab initio* simulations are important for accurately elucidating the deformation and ideal strength of superhard materials under different loading conditions [53–55]. We thus performed the first-principles calculations on BP to explore the deformation mechanisms along various inequivalent high-symmetry directions [Fig. 5(a)] under tensile and shear strains ($\varepsilon$) as shown in Figs. 5(b) and 5(c). Because BP adopts a diamondlike structure, it is expected that the mechanically strongest and weakest directions would be intimately linked to the (100) and (111) crystallographic planes. Indeed, the tensile strength along the [111] direction is the weakest with an ultimate strength of $\sigma_{\text{min}} = \sigma_{[111]} = 35.4$ GPa at a small strain $\varepsilon = 0.17$. At higher strain levels, a considerable softening occurs and eventually leads to fracture at $\varepsilon = 0.27$. In contrast, the highest ultimate tensile strength of $\sigma_{[100]} = 68.5$ GPa is achieved along the [100] direction, nearly twice that of $\sigma_{[111]}$. An intermediate strength value of 42.4 GPa is obtained for the mode along the [110] direction, which is mainly attributed to the B-P bonds that participate in the tensile deformation as will be discussed later.

For the $\sigma_{[110]}$ tensile and $\tau_{(110)[001]}$ shear deformations, sudden fractures happen at the corresponding critical strains of 0.37 and 0.32 [Figs. 5(b) and 5(c)], indicating the occurrence of tensile and shear instabilities. To gain insight into the details of the fracture mechanism, several typical snapshots of the $\tau_{(110)[001]}$ shear mode deformations are captured and plotted in Fig. 5(d). With the increase of strain, the B-P bonds in the (110) plane are progressively prolonged along the [001] direction, which is accompanied by a profound charge redistribution. At the critical strain of 0.32 [see snapshot S3 in Fig. 5(d)], the reordering of atoms proceeds as a result of bond breaking, leading to the formation of a unique hexagonal BP, which is structurally isotopic with h-BN and graphite [snapshot S4 in Fig. 5(d)]. Similar behaviors and phase transition also occur under the $\sigma_{[110]}$ tensile deformation (see Fig. S5 in the Supplemental Material [37]). Such strain-driven structural instability gives an accurate account of the tensile and shear fractures in BP. However, the asymmetrically distributed charge density suggests that the hexagonal phase is thermodynamically unstable and cannot be preserved to

![](./images/812690882233892865_6.jpg)

FIG. 5. Calculations of the dual tensile and shear strengths for BP. (a) Crystal structure at equilibrium. Arrow lines denote the high-symmetry directions, along which the tensile and shear deformations are calculated. (b) Stress responses under tensile strains along various high-symmetry directions. (c) Stress responses under pure shear strains in the selected high-index planes (110), (100), and (111) along a few typical shear directions. (d) Snapshots of crystal and electronic structures under four typical shear strains as denoted with S1, S2, S3, and S4 in (c).

ambient conditions, which differs from diamond and c-BN. Nevertheless, this provides a plausible approach for the syn- thesis of hexagonal BP under shear or tensile deformation. Such a proposed hexagonal new phase, for example, would be produced under the indentation as the large shear stress will be involved at the interface between the diamond tip and the sample, and further experimental effort is needed to verify this speculation. The calculated elastic properties and strengths for BP are summarized in Table II. Also listed in Table II are the mechanical properties of the known superhard materials of $B_6O$, c-BN, and diamond for comparison.

As shown in Fig. 6, the crystallographic dependence of the tensile strength is primarily attributed to the number of B-P bonds involved in the tensional deformation. For zinc-blende BP, each P atom is surrounded by four neighboring B atoms to form $[PB_4]$ tetrahedral coordination [Figs. 6(a) and 6(b)]. All four bonds in Fig. 6(c) are tensioned in the $\sigma_{[100]}$ mode to resist tensile stress and to achieve the highest ultimate

TABLE II. Calculated Voigt bulk modulus $B_V$, shear modulus $G_V$, Vickers hardness $H_V$, and ideal strength (i.e., the minimum tensile strength $\sigma_{min}$ and shear strength $\tau_{min}$) for zinc-blende BP. $\beta$-SiC, h-$B_6$O, c-BN, and diamond are also included for comparison.

<table>
<thead>
<tr>
<th>Material</th>
<th>Reference</th>
<th>$G_V$ (GPa)</th>
<th>$B_V$ (GPa)</th>
<th>$k = G_V/B_V$</th>
<th>$H_V$ (GPa)</th>
<th>$\sigma_{min}$ (GPa)</th>
<th>$\tau_{min}$ (GPa)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cubic BP</td>
<td>This study</td>
<td>165</td>
<td>162</td>
<td>1.02</td>
<td>37.5</td>
<td>$\sigma_{[111]} = 35.1$</td>
<td>$\tau_{(111)[11\bar{2}]} = 28.0$</td>
</tr>
<tr>
<td>$\beta$-SiC</td>
<td>Ref. [46]</td>
<td>191</td>
<td>224</td>
<td>0.85</td>
<td>32.8</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>h-$B_6$O</td>
<td>Refs. [46,56]</td>
<td>204</td>
<td>228</td>
<td>0.90</td>
<td>36.4</td>
<td>$\sigma_{[10\bar{1}0]} = 53.3$</td>
<td>$\tau_{(0001)[10\bar{1}0]} = 38.0$</td>
</tr>
<tr>
<td>c-BN</td>
<td>Refs. [46,56]</td>
<td>390</td>
<td>376</td>
<td>1.04</td>
<td>65.5</td>
<td>$\sigma_{[111]} = 55.3$</td>
<td>$\tau_{(111)[11\bar{2}]} = 58.3$</td>
</tr>
<tr>
<td>Diamond</td>
<td>Refs. [46,56]</td>
<td>528</td>
<td>442</td>
<td>1.20</td>
<td>93.4</td>
<td>$\sigma_{[111]} = 82.3$</td>
<td>$\tau_{(111)[11\bar{2}]} = 86.8$</td>
</tr>
</tbody>
</table>

![](./images/812690882233892865_7.jpg)

FIG. 6. Calculated tensile deformation along high-symmetry [100], [110], and [111] directions. (a) Crystal structure of BP at equilibrium with three marked high-symmetry tensile directions. (b) Polyhedral view of the $[PB_4]$ tetrahedral coordination formed by P atoms and its four neighboring B atoms. At equilibrium, the bond length and bond angle are $1.945\ \mathring{A}$ and $109.47^\circ$, respectively. (c) Stress responses under tensile strain along the selected high-symmetry directions. (d) Tensile deformation along the [100] direction. All four bonds are equivalent and have an identical bond length. (e) Tensile deformation along the [110] direction with two stretched bonds and two compressed bonds. (f) Tensile deformation along the [111] direction with one stretched bond and three compressed bonds.

tensile strength [Fig. 6(b)], which is different from the weaker modes of $\sigma_{[110]}$ and $\sigma_{[111]}$ with a differently reduced number of tensioned B-P bonds and hence the increased number of compressed B-P bonds, as illustrated in Figs. 6(e) and 6(f). The weakest mode of $\sigma_{[111]}$, for example, has only one tensioned B-P bonds with three compressed B-P bonds. Evidently, the bond angles will also be substantially modified and should contribute partially to the softening of the modes of $\sigma_{[110]}$ and $\sigma_{[111]}$. Similarly, for the shear deformation, the (111)[11$\overline{2}$] slip system is responsible for the minimum shear strength $\tau_{\text{min}} = \tau_{(111)[11\overline{2}]} = 24.6\mathrm{GPa}$ and the highest shear strength $\tau_{(100)[010]} = 44.3\mathrm{GPa}$ is attained by the (100)[010] shearing mode.

In view of the relatively low elastic properties of BP (see Table II), this material does not seem to be in favor of its superhardness. To gain insight into the underlying mechanism, a comparative study of the shear deformation is performed between BP and superhard material c-BN. Along the high-symmetry directions as seen in Fig. 7, both materials show a similar crystallographic dependence of anisotropic tensile deformation; the weakest direction [111] holds for both materials, suggesting that the (111) plane is the most easily cleavable. Accordingly, three different shear stress-strain curves associated with the (111) plane are calculated in Figs. 7(a) and 7(b). Although the ultimate tensile and shear strengths of BP along all selected directions are more than twofold smaller than those of c-BN, the calculated fracture strains in BP are nearly twice that of c-BN. This is an indication of excellent ductility and toughness in BP, which provides a reasonable interpretation for its high toughness as determined in our experiment (Fig. 4). In fact, superhard materials with superior ductility and toughness are highly desired to greatly extend the damage threshold for ease of machining and for achieving a long working life when used in tools or devices. More importantly, the shear stresses steadily increase along all selected directions as the strain increases

![](./images/812690882233892865_8.jpg)

FIG. 7. Calculated stress-strain relationships for both zinc- blende BP (a) and cubic BN (b). Curves with open symbols represent tensile deformation, and curves with solid symbols denote shear deformation. Inset is an enlargement of the (111)[11$\overline{2}$] shearing slip system for cubic BP and c-BN; for simplicity, the yield point of the shear mode is defined using the proportional limit of the elastic region, as denoted by the black arrow.

![](./images/812690882233892865_9.jpg)

FIG. 8. High-$P$ Raman spectra for BP. (a) First-order Raman lines $\Gamma_{\text{TO}}$ and $\Gamma_{\text{LO}}$ taken at selected pressures. The letter "D" denotes the data taken on decompression. (b) Phonon frequencies of TO and LO modes as a function of pressure. Black lines represent the best fits to the pressure dependence of phonon frequencies for three different pressure regions of 0–13 GPa, 13–36 GPa, and 36–56 GPa (see Fig. S9 in the Supplemental Material [37]; also see [15,24,39]). A few phonon modes appear on the edges of the $\Gamma_{\text{TO}}$ and $\Gamma_{\text{LO}}$ lines at high pressure. The inset shows the pressure dependence of the peak intensity ratio between $\Gamma_{\text{TO}}$ and $\Gamma_{\text{LO}}$, $I_{\text{TO}}/I_{\text{LO}}$. The black line denotes the best fit of experimental data to a square-power law. (c) The Born transverse effective charge, $e_{T}^{*}$, and $\omega_{\text{LO}}^{2} - \omega_{\text{TO}}^{2}$ as a function of pressure. Inset is the calculated valence charge using the Bader method.

to higher levels (Fig. 7), inferring substantial strain stiffening or hardening. In particular, the strain-stiffening ratio, which is a measure of the degree of strain stiffening defined by the ultimate strength relative to the yield strength, of the weakest (110)[001] shearing mode is as large as that in c-BN (i.e., $\sim$3.4). Such strain stiffening is expected to occur under indentation to strongly resist the shear deformation and is presumably responsible for the superhardness in BP. A similar strain-stiffening mechanism has recently been used for the prediction of two nontraditional superhard solids in the W-N material system [54].

To investigate the optical properties of this phosphide, we performed high-$P$ Raman spectroscopy measurements on single-crystal samples (see Fig. 8 and Figs. S6–S13 in the Supplemental Material [37]; also see [15,24,39]). As shown in Fig. 8(a), the high-$P$ Raman spectra feature a first-order Raman doublet, corresponding to the transverse and longitudinal optical phonons (i.e., TO and LO). Infrared activity of both TO and LO modes in BP is also identified (Fig. S14 in the Supplemental Material [37]). At ambient conditions, the frequencies of the TO and LO modes, $\omega_{\text{TO}}$ and $\omega_{\text{LO}}$, are 799.8 (2) and 827.5(2)$\text{cm}^{-1}$, respectively, which are consistent with previous reports [15,24]. Interestingly, with increasing pressure, the peak separation between TO and LO is marginally reduced at the early stage of compression (i.e., below 13 GPa) with slopes of 6.39 and $5.38\text{cm}^{-1}/\text{GPa}$, respectively, followed by a nearly parallel increase up to 36 GPa as summarized in Fig. 8(b). Although the slope variation is small, it is significant enough to be measured based on our careful analysis (see Figs. S7 and S8 in the Supplemental Material [37]), leading to the discovery of an exotic electronic transition as will be discussed below. Another slope change in the 36–60 GPa range is ambiguous, and future experimental work is needed to address it. Probably because of multiphonons, several phonon modes and pressure dependence of frequencies are also investigated including acoustic and optical phonons [Fig. 8(b)].

Concurrent with the variation of peak separation, the intensity of the TO peak is noticeably increased relative to that of the LO peak, and they are nearly identical around 17 GPa [Fig. 8(a)]. With further increase in pressure, the TO peak becomes even stronger than the LO peak and overwhelms above 50 GPa. In principle, the pressure dependence of peak intensity ratio, $I_{\text{TO}}/I_{\text{LO}}$, between the $\Gamma_{\text{TO}}$ and $\Gamma_{\text{LO}}$ can be deduced from the effective electro-optical constant, $\alpha(P)$, given by

$$
\frac{I_{\text{TO}}}{I_{\text{LO}}} \sim \alpha(P)^{-2} \sim \frac{\omega_{\text{LO}}^{2} - \omega_{\text{TO}}^{2}}{V\varepsilon_{\infty}(E_{c15} - E_{c1})^{2}}, \tag{2}
$$

where $V$, $\varepsilon_{\infty}$, and $E_{c15} - E_{c1}$ correspond to the unit-cell volume, optical dielectric constant, and energy difference between the conduction band states of $\Gamma_{15c}$ and $\Gamma_{1c}$. The pressure dependences of these variables can be evaluated using previously reported data [15,24]. The thus-calculated intensity ratios as a function of pressure are in excellent agreement with these present experimental observations, which can well be described by a square power law (i.e., $\propto P^{2}$) (see Fig. S9 in the Supplemental Material [37]; also see [15,24,39]). Obviously, the intriguing variations of optical phonon intensity under pressures are due to the electro-optical effect, which contributes to the scattering probability amplitude of the LO phonon at the center of the Brillouin zone.

For a binary compound formed from two different elements, the ionicity is an inherent character of the chemical bond with an asymmetric distribution of electron density, which produces oppositely charged ions. As a result, the longitudinal vibrations will dynamically induce additional separation between the oppositely charged ions, which exerts extra restoring force to the LO mode, leading to a large frequency increase in the LO mode relative to the TO mode (i.e., the splitting of the LO and TO modes) (see Supplemental Material [37]). Thus, the bonding state of material at high pressures can be determined by analysis of the effective charge and the LO-TO splitting. In fact, the Born effective charge $\text{e}_{T}^{*}$ is a fundamental quantity and has extensively been used for the study of crystalline lattice dynamics, given by

$$
e_{T}^{*2} = \frac{\varepsilon_{\infty}V\mu}{16\pi}(\omega_{\text{LO}}^{2} - \omega_{\text{TO}}^{2}), \tag{3}
$$

where $\mu$ is the reduced mass of the two-component atoms, and the rest of the variables have been defined in Eq. (2). A detailed description for the deduction of $\text{e}_{T}^{*}$ can be found in Ref. [24].

![](./images/812690882233892865_10.jpg)

FIG. 9. High-$P$ second-order Raman spectra for BP. (a) Raman patterns taken upon compression with intensity plotted in a logarithmic scale to show the weak multiphonon processes. Each second-order phonon mode in the frequency range of $500-1800\,\text{cm}^{-1}$ is identified as a combination of the first-order phonon modes of acoustic and optical branches (Ref. [15]). The inset is the calculated phonon dispersion for BP at ambient pressure (Ref. [14]). The longitudinal (L) and transverse (T) modes of optical (O) and acoustic (A) bands are denoted with LO, TO, LA, and TA, respectively. (b) Phonon frequencies of the second-order Raman modes versus pressure. Phonon modes of $\Gamma_{\text{TO}}$ and $\Gamma_{\text{LO}}$ are also plotted for comparison.

Figure 8(c) displays the pressure dependences of the derived $e_{T}^{*}$, and the frequency splitting between LO and TO (i.e., $\omega_{\text{LO}}^{2}-\omega_{\text{TO}}^{2}$) (see Figs. S9-S11 in the Supplemental Material [37]; also see [15,24,39]). Both $e_{T}^{*}$ and frequency splitting decrease linearly at the initial stage of compression up to $\sim13$ GPa, especially for $e_{T}^{*}$ with a $\sim40\%$ reduction, indicating that a substantial amount of charges is transferred from P to B atoms as the bond is shortened at higher pressures. This would in turn substantially increase the fraction of covalent bonds, in favor of the stain stiffening as aforementioned. However, above 13 GPa, the variation trend of LO-TO splitting is radically altered and the $\omega_{\text{LO}}^{2}-\omega_{\text{TO}}^{2}$ value increases as the pressure rises, whereas the $e_{T}^{*}$ retains at a small leveled-off value of $\sim0.75$. This indicates an electronic transition at the critical pressure of 13 GPa without involving the symmetry breaking as determined by high-$P$ XRD measurement (see Fig. S15 in the Supplemental Material [37]; also see [15]). To confirm this transition, we employed the $ab$ initio theory to calculate the Bader charge at high pressures [inset of Fig. 8(c)]. To our delight, a mild decrease of the Bader charge is found in the 0-7 GPa pressure range, consistent with the experimental observations. Around the transition pressure (i.e., 7 GPa), an abrupt increase of the Bader charge is observed, indicative of an electronic transition. It is noted that the obtained Bader charge is close to the XPS result (Fig. 3) but drastically smaller than the $e_{T}^{*}$ value at ambient conditions, probably because the Born effective charge is a measure of dynamic charge, whereas the former quantifies the static charge. In fact, the effective charge is closely related to the antisymmetric part of the crystal potential composed by long- and short-range components as pointed out by Sengstag *et al.* [9]. Pressure can profoundly alter the relative fraction of two antisymmetric components, which causes an appreciable variation of effective charge [9]. In the case of BP, because the long-range ionic term may dominate at low pressure with respect to the short-range core potential, the effective charge decreases in magnitude with pressure. However, the fraction of the short-range term is increased at higher pressures and becomes comparable to that of the long-range potential above $\sim13$ GPa, which could be responsible for the anomalous transitions in both the Born and Bader charges.

A careful investigation of the variations of multiphonon processes is shown in Fig. 9. High-$P$ Raman spectra plotted in Fig. 9(a) display the logarithm scale of intensity to show the weak multiphonon modes (i.e., second-order phonon modes). Combined with previous calculations in Ref. [14], each peak can well be assigned to second-order phonon modes; these multiphonons are produced by combination of acoustic and optical modes located at the high-symmetry points of $L$, $\Gamma$, and $X$, near the center of the Brillouin zone [see Fig. 9(a)]. With increasing pressure, the intensity of such phonons is progressively lowered and most peaks vanish above 20 GPa. Figure 9(b) presents the derived phonon frequencies versus pressure. Below the frequency of $750\,\text{cm}^{-1}$, the observed multiphonon processes are the acoustic multiphonon modes, while only optical modes appear above $1350\,\text{cm}^{-1}$. In the intermediate frequency range of $900-1200\,\text{cm}^{-1}$, a number of hybrid modes formed between a pair of acoustic and optical modes are active. As expected, in contrary to the acoustic branch, the optical mode is sensitive to pressure, because the external pressure acts as additional restoring force to the out-of-phase vibrations (i.e., optical modes), giving rise to the enhanced phonon frequencies in the optical branch at higher pressures.

![](./images/812690882233892865_11.jpg)

![](./images/812690882233892865_12.jpg)

![](./images/812690882233892865_13.jpg)

![](./images/812690882233892865_14.jpg)

FIG. 10. High-$P$ PL measurement for BP. (a) Selected high-$P$ spectra taken on compression and decompression (marked with the “D” letter) at room temperature. Vertical sticks denote four components A–D of the spectrum. Gray-black squares and dots denote the PL and second-order Raman peaks of the diamond anvil, respectively. The indirect band gap $E_g$ is estimated using the high-energy edge of the PL spectrum. (b) Energies of the four PL components and the band gap as a function of pressure. Red dots and blue solid squares represent the $E_g$ value measured from the ultraviolet spectrum and calculated from $ab$ $initio$ theory, respectively. (c) Excitation-power dependence of the 706.8-nm emission spectrum band composed of several sharp fringes, based on the photon-driven emission using a 4.5-$\mu$m thin-plate single crystal [see Fig. 1(b)]. The wavelength of the excitation laser is 532 nm and the spectra are taken at ambient conditions. (d) Fringe mode spacing, $\Delta\lambda$, as a function of wavelength of the fringe center, $\lambda$.

In order to investigate the emission spectrum of this material, the photoluminescence (PL) spectroscopy measurements were carried out as shown in Fig. 10. At low pressures the spectra consist of four emission bands spaced approximately 0.4 eV apart [Fig. 10(a)], corresponding to the phonon sideband of BP. This is because BP is an indirect semiconductor and because a phonon-assisted emission process is involved during the electron-hole recombination [57]. The obtained energies for these peaks are 1.943, 1.858, 1.780, and 1.690 eV, respectively, in good agreement with previous reports at 300 K (Table IV) [12,13,25]. With increasing pressure, the four bands are gradually shifted to the high-energy side of the spectrum, while the peak intensities are promptly reduced. At the critical pressure of $\sim$13.9 GPa, all PL peaks are almost completely submerged in the background signals of the diamond anvils (see Refs. [58,59] for PL of diamond). Apparently, the critical pressure corresponds to that of the electronic transition as measured in the Raman spectroscopy measurement [Fig. 8(b)], inferring that the underlying transition mechanism in PL is also linked to the variation of crystal potential under pressures. As an indirect semiconductor, the band gap of BP can conveniently be estimated using the high-energy edge of the PL spectrum. As shown in Fig. 10(b), the first three emission bands have a similar pressure dependence of peak position with a slope of $-10$ meV/GPa, close to that of the band gap (also see Fig. S16 in the Supplemental Material [37]). This is because the position of the sideband is predominantly determined by the band gap. In contrast, the $D$ band has a relatively flat slope (i.e., $-5$ meV/GPa), which may arise from microscopic aggregates or inclusions of phosphorus as previously proposed in Ref. [13].

TABLE III. Assignments for the second-order Raman and infrared spectrum of BP.

| Assignment          | Raman (cm⁻¹) at 0.4 GPa, this work | Calculated Ref. [14] | Infrared (cm⁻¹), this work |
|---------------------|------------------------------------|----------------------|----------------------------|
| $L_{\text{TA}} + X_{\text{TA}}$ | 548.0                              | 554.9                | –                          |
| $2X_{\text{TA}}$    | 621.0                              | 616.6                | –                          |
| $L_{\text{TA}} + L_{\text{LA}}$ | 697.7                              | 732.6                | –                          |
| $L_{\text{TA}} + X_{\text{LA}}$ | 705.5                              | 732.3                | –                          |
| $\Gamma_{\text{TO}}$ | 799.8                              | 809.3                | 798.5                      |
| $\Gamma_{\text{LO}}$ | 827.5                              | 834.6                | 825.5                      |
| $L_{\text{TA}} + X_{\text{LO}}$ | 1000.7                             | 1007.6               | –                          |
| $X_{\text{TA}} + L_{\text{TO}}$ | 1030.8                             | 1035.2               | –                          |
| $X_{\text{TA}} + \Gamma_{\text{LO}}$ | 1127.7                             | 1142.9               | –                          |
| $X_{\text{TO}} + L_{\text{LA}}$ | 1160.4                             | 1161.6               | –                          |
| $2L_{\text{TO}}{}^{\text{a}}$ | 1435.7                             | 1451.2               | –                          |
| $L_{\text{LO}} + L_{\text{TO}}$ | 1452.5                             | 1475.5               | –                          |
| $L_{\text{LO}} + \Gamma_{\text{LO}}$ | 1570.0                             | 1583.2               | –                          |
| $2\Gamma_{\text{TO}}$ | 1594.9                             | 1618.5               | –                          |
| $\Gamma_{\text{TO}} + \Gamma_{\text{LO}}$ | 1612.0                             | 1643.8               | –                          |

${}^{\text{a}}$Based on the phonon dispersion calculations in Ref. [14]; at the $L$ point the phonon frequencies of TO and LO do not degenerate and have different values of $L_{\text{TO}} = 726.9\,\text{cm}^{-1}$ and $L_{\text{LO}} = 748.6\,\text{cm}^{-1}$.

Figure 10(c) shows the room-temperature PL spectra obtained from a 4.5-$\mu\text{m}$ thin plate of a single-crystal sample at different excitation laser powers. At a low excitation power of 2.5 mW, instead of a broadened emission band, a few weak fringes appear in the same energy region of the spectrum. This is seemingly caused by the étalon effect, because only the emitted light with certain wavelengths can be selected and strongly amplified by the thin crystal with two parallel reflecting surfaces that form a resonant cavity. Interestingly, as the excitation power is elevated, these longitudinal modes of the étalon are remarkably increased. The sharp fringe modes are symmetrically distributed around the strongest line located at a wavelength of 707 nm (Fig. S17 in the Supplemental Material [37]), corresponding to the red color. It is noted that the fringe width is gently increased (Fig. S18 in the Supplemental Material [37]), and a similar phenomenon has also been observed in h-BN and ZnO [60,61]. Furthermore, the fringe mode spacing $\Delta\lambda$, as a function of wavelength in Fig. 10(d), can well be described by the equation as follows [60–62],

$$
\Delta\lambda = \frac{\lambda^{2}}{2L[n - \lambda(dn/d\lambda)]}, \tag{4}
$$

where $n$ and $dn/d\lambda$ are the refractive index and its dispersion. The thus-derived refractive index value is $n \approx 2.65$ (8), close to that of SiC ($n = 2.55$–$2.60$) [36]. The discovery of photoluminescence-induced étalon effect in BP would provide many opportunities for the design of entirely new optical productions for diverse applications.

## IV. CONCLUSIONS

In summary, we have synthesized millimeter-sized high-quality zinc-blende BP single crystals. The nearly stoichiometric sample is optically transparent with a moderate band gap of $E_{g} \approx 2.1\,\text{eV}$ manifested by its intrinsic yellowish crystalline color. We also provide a feasible strategy to tailor the band gap and crystalline color by tuning the concentration of incorporated phosphorus. Despite its low elastic moduli, this material exhibits an unexpectedly high load-invariant hardness of 38 (3) GPa, near the 40 GPa threshold commonly accepted for superhard materials. By means of theoretical simulations, the deformation behaviors of BP under tensile and shear strains are thoroughly investigated, leading to the discovery of extraordinary strain stiffening and strengthening, as well as exceptional mechanical performance. In addition, both shear and tensile instabilities are closely related to the formation of hexagonal BP, which ultimately causes the fracture of the material. The study of high-$P$ behaviors of optical phonon splitting at the zone center has revealed an unusual electronic transition at $\sim$13 GPa with a strongly enhanced covalent bonding network. The phonon-assisted photoluminescence is also identified in BP with an indirect band structure, and the electronic-transition-induced suppression of the phonon sideband is uncovered at high pressure. Last, there is evidence for the photon-driven étalon effect in a 4.5-$\mu\text{m}$ thin-plate BP with the strongest radiation wavelength of 707 nm, corresponding to the red color. BP is a very hard and tough transparent semiconductor with a finite band gap in the visible spectrum range, making it a very promising candidate of the

TABLE IV. Energies of photo- (P)- and electro- (E) luminescence (L) band peaks (all in units of eV).

| Band designation | PL at 77 K, Ref. [13] | EL at 300 K, Ref. [12] | PL at 300 K, this work |
|------------------|------------------------|------------------------|------------------------|
| A                | 1.782                  | 1.972                  | 1.943                  |
| B                | 1.744                  | 1.886                  | 1.858                  |
| C                | 1.695                  | 1.769                  | 1.780                  |
| D                | 1.658                  | 1.648                  | 1.690                  |

new-generation semiconductors for a wide variety of practical applications.

## ACKNOWLEDGMENTS
This work was supported by the Key Research Plat- forms and Research Projects of Universities in Guangdong Province (Grant No. 2018KZDXM062), the Guangdong In- novative & Entrepreneurial Research Team Program (Grant No. 2016ZT06C279), the Shenzhen Peacock Plan (Grant No. KQTD2016053019134356), the Shenzhen Development & Reform Commission Foundation for Novel Nano-MaterialSciences, and the Research Platform for Crystal Growth & Thin-Film Preparation at SUSTech. The work was also par- tially supported by the Shenzhen Development and Reform Commission Foundation for Shenzhen Engineering Research Center of Frontier Materials Synthesis at High Pressure. Por- tions of this work were performed at the 4W2 station, Beijing Synchrotron Radiation Facility (BSRF).

R.G., Z.X., and X.Z. contributed equally to this work.

The authors declare that they have no competing financial interests.

[1] H. Morkoç, S. Strite, G. B. Gao, M. E. Lin, B. Sverdlov, and M. Burns, J. Appl. Phys. 76, 1363 (1994).
[2] S. Kasap and P. Capper, *Springer Handbook of Electronic and Photonic Materials* (Springer International Publishing, Berlin,2017).
[3] *National Research Council, Status and Applications of Diamond and Diamond-Like Materials: An Emerging Technology* (The National Academies Press, Washington, DC, 1990).
[4] A. Datye, U. D. Schwarz, and H.-T. Lin, Ceramics 1, 198(2018).
[5] J. Qian, L. L. Daemen, and Y. Zhao, Diamond Relat. Mater. 14,1669 (2005).
[6] V. V. Brazhkin, A. G. Lyapin, and R. J. Hemley, Philos. Mag. A82, 231 (2002).
[7] V. Brazhkin, N. Dubrovinskaia, M. Nicol, N. Novikov, R. Riedel, V. Solozhenko, and Y. Zhao, Nat. Mater. 3, 576 (2004).
[8] A. R. Goñi, H. Siegle, K. Syassen, C. Thomsen, and J. M. Wagner, Phys. Rev. B 64, 035205 (2001).
[9] T. Sengstag, N. Binggeli, and A. Baldereschi, Phys. Rev. B 52, R8613 (1995).
[10] P. Popper and T. A. Ingles, Nature 179, 1075 (1957).
[11] B. Stone and D. Hill, Phys. Rev. Lett. 4, 282 (1960).
[12] R. J. Archer, R. Y. Koyama, E. E. Loebner, and R. C. Lucas, Phys. Rev. Lett. 12, 538 (1964).
[13] F. M. Ryan and R. C. Miller, Phys. Rev. 148, 858 (1966).
[14] H. W. L. Alves and K. Kunc, J. Phys.: Condens. Matter 4, 6603(1992).
[15] V. L. Solozhenko, O. O. Kurakevych, Y. Le Godec, A. V.Kurnosov, and A. R. Oganov, J. Appl. Phys. 116, 033501(2014).
[16] W. Katherine, L. Kathleen, and K. Kirill, Mater. Res. Express3, 074003 (2016).
[17] V. L. Solozhenko and V. Bushlya, J. Superhard Mater. 41, 84(2019).
[18] J. S. Kang, H. Wu, and Y. Hu, Nano Lett. 17, 7507 (2017).
[19] Q. Zheng, S. Li, C. Li, Y. Lv, X. Liu, P. Y. Huang, D. A. Broido, B. Lv, and D. G. Cahill, Adv. Funct. Mater. 28, 1805116 (2018).
[20] J. B. Varley, A. Miglio, V.-A. Ha, M. J. van Setten, G.-M. Rignanese, and G. Hautier, Chem. Mater. 29, 2568 (2017).
[21] L. Shi, P. Li, W. Zhou, T. Wang, K. Chang, H. Zhang, T. Kako, G. Liu, and J. Ye, Nano Energy 28, 158 (2016).
[22] R. M. Wentzcovitch, M. L. Cohen, and P. K. Lam, Phys. Rev. B36, 6058 (1987).
[23] X. Zhang, J. Qin, H. Liu, S. Zhang, M. Ma, W. Luo, R. Liu, and R. Ahuja, Sci. Rep. 5, 8761 (2015).
[24] J. A. Sanjurjo, E. López-Cruz, P. Vogl, and M. Cardona, Phys. Rev. B 28, 4579 (1983).
[25] Y. Kumashiro, T. Yao, and S. Gonda, J. Cryst. Growth 70, 515(1984).
[26] B. H. Toby, J. Appl. Cryst. 34, 210 (2001).
[27] W. C. Oliver and G. M. Pharr, J. Mater. Res. 7, 1564 (1992).
[28] H. K. Mao, J. Xu, and P. M. Bell, J. Geophys. Res. 91, 4673(1986).
[29] S. Wang, X. Yu, Z. Lin, R. Zhang, D. He, J. Qin, J. Zhu, J. Han, L. Wang, H.-k. Mao et al., Chem. Mater. 24, 3023 (2012).
[30] S. A. Solin and A. K. Ramdas, Phys. Rev. B 1, 1687 (1970).
[31] https://www.almax-easylab.com/DiamondSelectionPage.aspx.
[32] G. Kresse and J. Furthmuller, Phys. Rev. B 54, 11169 (1996).
[33] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77,3865 (1996).
[34] P. E. Blochl, Phys. Rev. B 50, 17953 (1994).
[35] H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188(1976).
[36] http://www.ioffe.ru/SVA/NSM/Semicond/index.html.
[37] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.101.035302 for computational information about the calculated tensile deformation along different direc- tions and additional experimental information, such as X-ray diffraction patterns, Raman, photoluminescence, Ultraviolet- visible absorption, and X-ray photo-electron spectroscopy, about the structural, electronic, and optical properties of BP.
[38] J. Tauc, Mater. Res. Bull. 3, 37 (1968).
[39] C. Trallero-Giner, K. Kunc, and K. Syassen, Phys. Rev. B 73,205202 (2006).
[40] W. C. Oliver and G. M. Pharr, J. Mater. Res. 19, 3 (2004).
[41] S. Wang, X. Yu, J. Zhang, L. Wang, K. Leinenweber, D. He, and Y. Zhao, Cryst. Growth Des. 16, 351 (2016).
[42] X.-J. Chen et al., Proc. Natl. Acad. Sci. USA 102, 3198(2005).
[43] V. V. Brazhkin and V. L. Solozhenko, J. Appl. Phys. 125,130901 (2019).
[44] P. Chantikul, G. R. Anstis, B. R. Lawn, and D. B. Marshall, J. Am. Ceram. Soc. 64, 539 (1981).
[45] G. R. Anstis, P. Chantikul, B. R. Lawn, and D. B. Marshall, J. Am. Ceram. Soc. 64, 533 (1981).
[46] X.-Q. Chen, H. Niu, D. Li, and Y. Li, Intermetallics 19, 1275(2011).
[47] H. Niu, J. Wang, X.-Q. Chen, D. Li, Y. Li, P. Lazar, R.Podloucky, and A. N. Kolmogorov, Phys. Rev. B 85, 144116(2012).

[48] N. B. Goodman, L. Ley, and D. W. Bullett, *Phys. Rev. B* **27**, 7440 (1983).

[49] U. Elrod, M. C. Lux-Steiner, M. Obergfell, E. Bucher, and L. Schlapbach, *Appl. Phys. B* **43**, 197 (1987).

[50] Y. Wang and P. M. A. Sherwood, *Surf. Sci. Spectra* **9**, 99 (2002).

[51] R. P. Vasquez, C. U. Jung, M.-S. Park, H.-J. Kim, J. Y. Kim, and S.-I. Lee, *Phys. Rev. B* **64**, 052510 (2001).

[52] C. W. Ong, H. Huang, B. Zheng, R. W. M. Kwok, Y. Y. Hui, and W. M. Lau, *J. Appl. Phys.* **95**, 3527 (2004).

[53] Y. Zhang, H. Sun, and C. Chen, *Phys. Rev. Lett.* **93**, 195504 (2004).

[54] C. Lu, Q. Li, Y. Ma, and C. Chen, *Phys. Rev. Lett.* **119**, 115503 (2017).

[55] R. F. Zhang, D. Legut, Z. J. Lin, Y. S. Zhao, H. K. Mao, and S. Veprek, *Phys. Rev. Lett.* **108**, 255502 (2012).

[56] R. F. Zhang, Z. J. Lin, Y. S. Zhao, and S. Veprek, *Phys. Rev. B* **83**, 092101 (2011).

[57] R. H. Lyddane, R. G. Sachs, and E. Teller, *Phys. Rev.* **59**, 673 (1941).

[58] https://ned.ipac.caltech.edu/level5/Sept03/Li/Li4.html.

[59] J. Jeske *et al.*, *Nat. Commun.* **8**, 14000 (2017).

[60] D. C. Reynolds, D. C. Look, and B. Jogai, *Solid State Commun.* **99**, 873 (1996).

[61] K. Watanabe, T. Taniguchi, and H. Kanda, *Nat. Mater.* **3**, 404 (2004).

[62] M. I. Nathan, A. B. Fowler, and G. Burns, *Phys. Rev. Lett.* **11**, 152 (1963).