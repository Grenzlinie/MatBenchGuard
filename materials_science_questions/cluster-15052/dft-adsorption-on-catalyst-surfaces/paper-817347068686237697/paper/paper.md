# Robust route to $\boldsymbol{H_2O_2}$ and $\boldsymbol{H_2}$ via intermediate water splitting enabled by capitalizing on minimum vanadium-doped piezocatalysts

Yuekun Li$^{1,\S}$, Li Li$^{2,\S}$, Fangyan Liu$^{1}$, Biao Wang$^{1}$, Feng Gao$^{1}$, Chuan Liu$^{5}$, Jingyun Fang$^{4}$, Feng Huang$^{1}$, Zhang Lin$^{2,3}$, and Mengye Wang$^{1}$ ($\bowtie$)

$^{1}$ School of Materials, Sun Yat-Sen University, Shenzhen 518107. State Key Laboratory of Optoelectronic Materials and Technologies, Sun Yat-Sen University, Guangzhou 510275, China
$^{2}$ School of Environment and Energy, Guangdong Provincial Key Laboratory of Solid Wastes Pollution Control and Recycling, South China University of Technology, Guangzhou 510006, China
$^{3}$ School of Metallurgy and Environment, Central South University, Changsha 410083, China
$^{4}$ Guangdong Provincial Key Laboratory of Environmental Pollution Control and Remediation Technology, School of Environmental Science and Engineering, Sun Yat-Sen University, Guangzhou 510275, China
$^{5}$ The Guangdong Province Key Laboratory of Display Material and Technology, School of Electronics and Information Technology, Sun Yat-Sen University, Guangzhou 510275, China
$^{\S}$ Yuekun Li and Li Li contributed equally to this work.

© Tsinghua University Press 2022
Received: 19 April 2022 / Revised: 4 May 2022 / Accepted: 5 May 2022

## ABSTRACT
$H_2O_2$ is an environmentally friendly chemical for a wide range of water treatments. The industrial production of $H_2O_2$ is an anthraquinone oxidation process, which, however, consumes extensive energy and produces pollution. Here we report a green and sustainable piezocatalytic intermediate water splitting process to simultaneously obtain $H_2O_2$ and $H_2$ using single crystal vanadium (V)-doped $NaNbO_3$ ($V$-$NaNbO_3$) nanocubes as catalysts. The introduction of V improves the specific surface area and active sites of $NaNbO_3$. Notably, $V$-$NaNbO_3$ piezocatalysts of 10 mg exhibit 3.1-fold higher piezocatalytic efficiency than the same catalysts of 50 mg, as more piezocatalysts lead to higher probability of aggregation. The aggregation causes reducing active sites and decreased built-in electric field due to the neutralization between different nano-catalysts. Remarkably, piezocatalytic $H_2O_2$ and $H_2$ production rates of $V$-$NaNbO_3$ (10 mol%) nanocubes (102.6 and 346.2 $\mu$mol$\cdot$g$^{-1}\cdot$h$^{-1}$, respectively) are increased by 2.2 and 4.6 times compared to the as-prepared pristine $NaNbO_3$ counterparts, respectively. This improved catalytic efficiency is attributed to the promoted piezo-response and more active sites of $NaNbO_3$ catalysts after V doping, as uncovered by piezo-response force microscopy (PFM) and density functional theory (DFT) simulation. More importantly, our DFT results illustrate that inducing V could reduce the dynamic barrier of water dissociation over $NaNbO_3$, thus enhancing the yield of $H_2O_2$ and $H_2$. This facile yet robust piezocatalytic route using minimal amounts of catalysts to obtain $H_2O_2$ and $H_2$ may stand out as a promising candidate for environmental applications and water splitting.

## KEYWORDS
water splitting, $H_2$ evolution, $H_2O_2$ production, piezocatalysis, vanadium-doped $NaNbO_3$

## 1 Introduction
As a green and efficient oxidant, $H_2O_2$ is widely used in mining, electronics, pulp, packaging, and textile bleaching industries [1,2]. Especially since 2019, due to the raging COVID-19, the demand for $H_2O_2$ as the disinfectant has been significantly increased. As the predominant industrial process of $H_2O_2$ production, the anthraquinone method, however, causes a high energy consumption and induces serious pollutants, such as 2-ethylanthraquinone, trioctyl phosphate, tert-butyl urea, and $K_2CO_3$ lye [3,4]. Thus, it is highly desirable to develop a green and sustainable technique to produce $H_2O_2$.

Among the various environmentally friendly routes, the intermediate water splitting (IWS) has gained wide interest, as it could convert $H_2O$ into high-value $H_2O_2$ by exploiting green energy. Compared with the traditional overall water splitting (OWS) (i.e., a 4e⁻ reaction path), IWS is a 2e⁻ reaction and is thus more kinetically favorable [5-10]. Moreover, IWS possesses the advantage of the automatic separation of products (i.e., liquid $H_2O_2$ and gas $H_2$), preventing the reverse reaction. Clearly, developing breakthrough strategies of efficient IWS becomes urgent. Capable of being initiated by the mechanical force such as wind, tide, and wave, piezoelectric catalysis has attracted wide interest [11]. Quite intriguingly, piezoelectric catalysis is a facile yet robust technique, which could construct a built-in electric field in a single material to achieve the catalytic reactions. Ever since the first report, piezocatalysis has been widely employed in the

---
Address correspondence to wangmengye@mail.sysu.edu.cn

![](./images/817347068686237697_1.jpg)

hydrogen evolution, degradation of organic dyes, and synthesis of organic chemicals [12-17]. In contrast, the studies on piezocatalytic IWS are relatively few and limited in scope.

Herein, we report a piezocatalytic strategy to accomplish IWS, simultaneously generating high-value $H_{2}O_{2}$ and $H_{2}$ from pure water. We choose single-crystal $NaNbO_{3}$ nanocubes to investigate piezocatalytic IWS, as $NaNbO_{3}$ is one of the typical piezoelectric materials and possesses advantages, including excellent chemical stability, high charge mobility, and nontoxic elements [18]. In addition, it is easy to craft $NaNbO_{3}$ single crystals. Driven by the piezo-potential, piezocatalytic reduction reactions and oxidation reactions take place at the opposite facets of $NaNbO_{3}$ single crystals. Compared with polycrystalline compounds, single crystals could effectively inhibit the inverse catalytic redox reactions, consequently improving the catalytic efficiency. In order to further improve the piezoelectric response of $NaNbO_{3}$, V is doped into the lattice of $NaNbO_{3}$ nanocubes [19]. Through V doping, the structure asymmetry of $NaNbO_{3}$ materials is increased and the crystal size is reduced, thus remarkably improving its piezocatalytic $H_{2}$ and $H_{2}O_{2}$ production performance. Particularly, $NaNbO_{3}$ nanocubes doped by an optimal amount of V demonstrates 4.6- and 2.2-fold enhancement of $H_{2}$ and $H_{2}O_{2}$ production over pure $NaNbO_{3}$ piezocatalysts, respectively. Quite intriguingly, it is shown that minimum V-doped $NaNbO_{3}$ (V-$NaNbO_{3}$) nanocubes could achieve the highest piezocatalytic efficiency. The first-principle calculations based on density functional theory (DFT) are employed to further uncover the piezocatalytic mechanism of V-$NaNbO_{3}$.

## 2 Materials and methods

### 2.1 Chemicals

Niobium oxide $(Nb_{2}O_{5})$ and vanadium oxide $(V_{2}O_{5})$ were purchased from Macklin (Shanghai, China). Sodium hydroxide (NaOH) was purchased from Guangzhou Chemical Reagent Factory. Deionized (DI) water was used in the experiment. All chemicals were of analytical grade and without further purification.

### 2.2 Preparation of piezocatalysts

According to previous reports, $NaNbO_{3}$ nanoparticles were synthesized by a hydrothermal method [20]. $Nb_{2}O_{5}$ (1.06 g) was well dispersed in 40 mL NaOH aqueous solution (8 M) under vigorously stirring for 1 h. Then the obtained solution was transferred to a Teflon-lined autoclave (100 mL) and heated at $180\ ^{\circ}C$ for 8 h. After the autoclave was cooled naturally down to room temperature, the powders were washed three times with DI water, and then dried at $70\ ^{\circ}C$ for 24 h. Finally, the products were annealed at $400\ ^{\circ}C$ for 6 h to obtain $NaNbO_{3}$ piezocatalysts.

V-$NaNbO_{3}$ nanocubes were synthesized by the same synthesis procedure as $NaNbO_{3}$. Mixtures of 1.06 g $Nb_{2}O_{5}$ and different amounts of $V_{2}O_{5}$ were grounded in an agate mortar. Then these mixtures were added to 40 mL NaOH aqueous solution (8 M) and stirred for 1 h. The following procedures were similar to those of $NaNbO_{3}$ nanocubes. 0.0363, 0.0725, and 0.109 g of $V_{2}O_{5}$ were utilized and the corresponding as-prepared samples were denoted V-$NaNbO_{3}$ 5 mol%, 10 mol%, and 15 mol%, respectively.

### 2.3 Characterizations of $NaNbO_{3}$ and $V-NaNbO_{3}$

Powder X-ray diffraction (PXRD) patterns were measured using a Bruker D8-Advance X-ray diffractometer with $Cu\ K\alpha$ radiation ($\lambda = 0.154$ nm) at 40 kV and 40 mA. Transmission electron microscopy (TEM) and high-resolution transmission electron microscopy (HRTEM) images of the nanostructures were recorded on an electron microscope (FEI-TALOS-F200X) operating at an accelerating voltage of 200 kV. Piezo-response force microscopy (PFM) measurements were performed on an atomic force microscope instrument (Bruker, Dimension Icon) using Pt/Ir coated silicon probes. The composition and chemical states were analyzed using X-ray photoelectron spectroscopy (XPS, Thermo Fisher Scientific K-Alpha), equipped with Al $K\alpha$ (1,486.8 eV) X-ray source. In order to deal with the potential charging issue, a electron flood gun operated at 15 kV and 10 mA was used by the instrument. The binding energy corrections were made using the carbon peak (284.6 eV) as a reference.

### 2.4 Piezocatalytic measurements

Piezocatalytic $H_{2}$ and $H_{2}O_{2}$ evolution of $NaNbO_{3}$ and V-$NaNbO_{3}$ was conducted in a home-made glass reactor. 10 mg $NaNbO_{3}$ or V-$NaNbO_{3}$ nanoparticles were dispersed in 45 mL pure DI water. Then Ar was fed into the bottle to remove the air. The piezocatalytic process was under the continuous ultrasonic excitation (power ~ 192 W and frequency ~ 68 kHz). The generated gas (0.4 mL) was intermittently extracted and measured by a gas chromatograph (GC, Shimadzu GC-2014). The concentration of as-produced $H_{2}O_{2}$ was measured by a modified N,N-diethyl-p-phenylene-diamine (DPD)-horseradish peroxidase (POD) method at every 30 min [21]. 1 mL catalytic solution was pipetted into a 10 mL volumetric flask, and then 3 mL phosphate buffer (0.5 M and pH = 6) was added. Subsequently, $50\ \mu L$ of the DPD solution $(10\ \text{mg·mL}^{-1})$ and $50\ \mu L$ of the POD solution $(1\ \text{mg·mL}^{-1})$ were added. The solution was diluted with deionized water to 10 mL. $H_{2}O_{2}$ concentration was obtained by measuring the absorbance at 551 nm using a ultraviolet-visible spectrophotometer (UV-vis, Shimadzu, Cary 500). The analysis of $OH\cdot$ during the piezocatalytic process was conducted by a photoluminescence (PL) instrument using terephthalic acid (THA) as a dosimeter [22]. Before the measurement, the pH value of 10 mM THA solution (45 mL) was adjusted to 7. The catalytic solution (2 mL) was dropped on a sapphire substrate, and then analyzed by the photoluminescence spectra (Flexone, with a He-Cd laser $(\lambda_{\text{ex}} = 325$ nm)). The changes of peak intensity were monitored by measuring the maximal emission at $\lambda = 425$ nm, which represented the concentration of $OH\cdot$.

### 2.5 Simulation

All theoretical calculations were carried out using the first-principles simulations based on DFT by implementing Vienna *ab-initio* simulation package (VASP) [23,24] with exchange correlation energy function that was modeled by Perdew-Burke-Ernzerhof (PBE) function [25,26]. A cutoff energy of 500 eV was used for the plane-wave basis set in all calculations. The optimized lattice parameters of the bulk and the V-doped $NaNbO_{3}$ were $a = 5.563\ \mathring{A}$, $c = 5.637\ \mathring{A}$, $c = 15.581\ \mathring{A}$ and $a = 5.531\ \mathring{A}$, $b = 5.600\ \mathring{A}$, $c = 15.614\ \mathring{A}$, respectively. To model the stressed situation, the lattice parameter along c-axis was reduced to $15.427\ \mathring{A}$, which corresponded to a stress of 1 GPa. Then, the surface of $NbO_{2}$-terminated $NaNbO_{3}$ (001) was simulated by a $(1\times1)$ unit cell of 5-layer slab, where the bottom two layers of the slabs were fixed to their bulk positions, while the other three layers were allowed to relax. A thickness of $20\ \mathring{A}$ vacuum was added in the direction perpendicular to the slabs, so that the interactions among any adjusting molecules could be ignored. One of the surficial Nb atoms was substituted by V atom to model the V-doped surface. And the V-doped surface with O-vacancy was created by the removal of one O atom advecting to V atom. The Brillouin-zone integrations were performed using a $(2\times3\times1)$ k-mesh of the Monkhorst-Pack sampling scheme [27]. All atoms in the model were relaxed until the force on each atom

was below $0.01\ \text{eV-Å}^{-1}$. After obtaining the relaxed surfaces, the absorbates of $\text{H}$, $\text{OH}$, and $\text{H}_2\text{O}$ were placed on the surface and relaxed. The adsorption energies of $\text{H}$, $\text{OH}$, and $\text{H}_2\text{O}$ on the slabs were calculated as

$$\Delta E_{\text{M}} = E(\text{M}/\text{slab}) - E(\text{slab}) - E(\text{M})\ (\text{M} = \text{H},\text{OH},\text{and}\ \text{H}_2\text{O})$$

where $E(\text{slab})$, $E(\text{M})$, and $E(\text{M}/\text{slab})$ are the total energies of clean slab, absorbates, and slab with absorbates, respectively. The Gibbs free energy change of the absorbates was calculated as

$$\Delta G_{\text{M}*} = \Delta E_{\text{M}} + \Delta E_{\text{ZPE}} - T\Delta S\ (\text{M} = \text{H},\text{OH},\text{and}\ \text{H}_2\text{O})$$

where $\Delta E_{\text{ZPE}}$, $T$, and $\Delta S$ are the zero-point energy change, temperature, and entropy change, respectively. Gibbs free energy change was calculated at $T=298.15\ \text{K}$.

## 3 Results and discussion
The scanning electron microscopy (SEM) was employed to reveal the morphology and structure of $\text{NaNbO}_3$ and $\text{V-NaNbO}_3$ nanoparticles. Pure $\text{NaNbO}_3$ nanoparticles exhibit cubic features with side lengths of about $0.55\ \mu\text{m}$ (Fig. 1(a)). When the doping concentration of $\text{V}$ rises from $5\ \text{mol}\%$, $10\ \text{mol}\%$ to $15\ \text{mol}\%$, the length of $\text{V-NaNbO}_3$ cube piezocatalysts is reduced from $0.5$, $0.45$ to $0.4\ \mu\text{m}$, respectively (Figs. 1(b)-1(d)). In order to confirm the crystal structure of as-prepared samples, XRD patterns of pure $\text{NaNbO}_3$ and $\text{NaNbO}_3$ doped by different concentrations of $\text{V}$ were measured. The diffraction peaks at $22.8^\circ$, $32.6^\circ$, $39.9^\circ$, $40.2^\circ$, $46.4^\circ$, $52.6^\circ$, and $57.9^\circ$ correspond to (101), (121), (031), (022), (202), (141), and (123) crystal planes of orthogonal $\text{NaNbO}_3$ crystals, respectively (JCPDS No. 82-0606, Fig. 1(e)). After $\text{V}$ doping, no new peaks are displayed, and the orthogonal structure of $\text{NaNbO}_3$ remains unchanged (Fig. 1(e)). It is worth noting that with the rising amount of $\text{V}$ doping, the increase in full width half maximum (FWHM) of $\text{V-NaNbO}_3$ is found, indicating that $\text{V}$ doping decreases the size of $\text{NaNbO}_3$ nanoparticles (Table S1 in the Electronic Supplementary Material (ESM)). This is consistent with the SEM results (Figs. 1(a)-1(d)). The above observation suggests that $\text{V}$ doping might improve the piezocatalytic efficiency of $\text{NaNbO}_3$ nanocubes by raising their specific surface area (Table S1 in the ESM).

Raman spectroscopy was exploited to probe the local structures of $\text{NaNbO}_3$ and $\text{V-NaNbO}_3$ (Fig. S1 in the ESM). The region from $100$ to $150\ \text{cm}^{-1}$ is related to the Na-site displacement and $\text{NbO}_6$ octahedral tilting [28]. All the bands in the region of $150$-$800\ \text{cm}^{-1}$ could be ascribed as the internal modes of $\text{NbO}_6$. Two peaks from $150$ to $300\ \text{cm}^{-1}$ are located in the $\text{v}_5(\text{F}_{2\text{g}})$ and $\text{v}_6(\text{F}_{2\text{u}})$ bands, which represent the triply degenerate $\text{O-Nb-O}$ bending vibrations [29]. The weak band $\text{v}_4(\text{F}_{1\text{u}})$ around $400\ \text{cm}^{-1}$ is stemmed from asymmetric $\text{Nb-O}$ stretching. Two strong peaks at $557.8$ and $607.7\ \text{cm}^{-1}$ are ascribed to $\text{v}_2(\text{E}_{\text{g}})$ and $\text{v}_1(\text{A}_{1\text{g}})$ breathing vibration modes, respectively, which are associated with high-frequency $\text{Nb-O}$ stretching bands [30]. As the amount of doped $\text{V}$ is too little, its signal cannot be detected by Raman. In addition, it further confirms that $\text{V}$ doping does not alter the crystal structure of $\text{NaNbO}_3$.

To uncover the growth process of $\text{V-NaNbO}_3$ piezocatalysts, as-crafted materials after different hydrothermal time were collected (Fig. 1(f)). At the first stage, the $\text{Nb}_2\text{O}_5$ and $\text{V}_2\text{O}_5$ powders are wrapped by $\text{NaOH}$ (Fig. 1(f)(i)). After $30\ \text{min}$, $\text{Nb}_2\text{O}_5$ and $\text{V}_2\text{O}_5$ powders react with each other and form sunflower-seed-likes structures (Fig. 1(f)(ii)), which indicates the formation of entangled networks of $\text{Na}_8\text{Nb}_6\text{O}_{19}\cdot n\text{H}_2\text{O}$ chains (Eq. (1)) [31]. Then the reaction between $\text{Na}_8\text{Nb}_6\text{O}_{19}\cdot n\text{H}_2\text{O}$ and $\text{Nb}_2\text{O}_5$ occurs (Eq. (2)), in the meanwhile, grey sunflower-seed-like construction is transformed to yellow rod-like architectures which are $\text{NaNbO}_3$ nanocrystals (Fig. 1(f)(iii)). During the growth via an Ostward ripening, $\text{NaNbO}_3$ nanocrystals exhibit rough surface, composing of rod-like crystals (Fig. 1(f)(iv)) [32]. Eventually, the surfaces of $\text{NaNbO}_3$ become smooth after the progress of dissolution and regeneration (Fig. 1(f)(v))

$$8\text{NaOH} + 3\text{Nb}_2\text{O}_5 + (n-4)\text{H}_2\text{O} = \text{Na}_8\text{Nb}_6\text{O}_{19}\cdot n\text{H}_2\text{O} \quad (1)$$

$$\text{Na}_8\text{Nb}_6\text{O}_{19}\cdot n\text{H}_2\text{O} + \text{Nb}_2\text{O}_5 = 8\text{NaNbO}_3 + n\text{H}_2\text{O} \quad (2)$$

Figure 2 depicts the morphology and crystal structure of pure $\text{NaNbO}_3$ and $\text{V-NaNbO}_3$ ($10\ \text{mol}\%$) nanoparticles. By comparing TEM images of pure $\text{NaNbO}_3$ and $\text{V-NaNbO}_3$, the reduction of crystal size is obviously observed after $\text{V}$ doping (Figs. 2(a) and 2(c)). As shown in Fig. 2(b), the lattice fringe of $0.392\ \text{nm}$ is ascribed to the (001) plane of orthogonal $\text{NaNbO}_3$ [33], and the selected area electron diffraction (SEAD) pattern reveals that the as-prepared $\text{NaNbO}_3$ nanoparticles are single crystalline.

Similar with pure $\text{NaNbO}_3$, $\text{V-NaNbO}_3$ piezocatalysts demonstrate the same single crystal structure (Fig. 2(d)). The

![](./images/817347068686237697_2.jpg)

Figure 1 (a)-(d) SEM images of (a) $\text{NaNbO}_3$, (b) $\text{V-NaNbO}_3$ ($5\ \text{mol}\%$), (c) $\text{V-NaNbO}_3$ ($10\ \text{mol}\%$), and (d) $\text{V-NaNbO}_3$ ($15\ \text{mol}\%$). (e) XRD patterns of $\text{NaNbO}_3$ and $\text{V-NaNbO}_3$ with various $\text{V}$ doping concentrations. (f) Schematic illustration of the growth process of $\text{V-NaNbO}_3$.

![](./images/817347068686237697_3.jpg)

Figure 2 (a) TEM image, (b) HRTEM image, and SAED pattern (inset) of pure $NaNbO_3$ piezocatalysts. (c) TEM image, (d) HRTEM image, SAED pattern (inset), and (e) TEM image and EDS mapping (in STEM mode) corresponding to the Nb, Na, O, and V of V-$NaNbO_3$ piezocatalysts. (f) XPS survey spectra of V-$NaNbO_3$ (10 mol%) and pure $NaNbO_3$. (g) High-resolution XPS spectra of V $2p_{3/2}$ for V-$NaNbO_3$ (10 mol%). High-resolution XPS spectra (h) Nb 3d and (i) O 1s for pure $NaNbO_3$ and V-$NaNbO_3$ (10 mol%).

above observation indicates that V doping makes the size of $NaNbO_3$ shrink, but does not alter the lattice of $NaNbO_3$. The elements, including Nb, Na, O, and V, are well distributed in V-$NaNbO_3$, suggesting the uniform V doping (Fig. 2(e)).

XPS measurement was employed to characterize the chemical states of $NaNbO_3$ and V-$NaNbO_3$ (10 mol%). Na, Nb, and O elements are observed in $NaNbO_3$, and Na, Nb, O, and V elements are detected in V-$NaNbO_3$ (10 mol%) (Fig. 2(f)). The C 1s peak is due to contaminated hydrocarbons in the XPS spectra. Figure 2(g) demonstrates the V $2p_{3/2}$ spectra. Two peaks at 516.9 and 515.4 eV are in good agreement with the reported values of $V^{5+}$ and $V^{4+}$, respectively (Fig. 2(g)) [34]. The peak of Na 1s is located at 1,071.0 eV, which is well in agreement with $Na^+$ (Fig. S2 in the ESM) [35]. The Nb 3d of both samples shows two peaks at 209.53 and 206.83 eV, which are attributed to Nb $3d_{5/2}$ and Nb $3d_{3/2}$ of $Nb^{5+}$, respectively (Fig. 2(h)) [36]. In the high-resolution O 1s spectra, three peaks at 529.62, 531.42, and 531.71 eV are fitted, which correspond to lattice $O^{2-}$ ions, surface $O^{2-}$ vacancy (Vo), and surface adsorbed oxygen, respectively (Fig. 2(i)) [37]. It is worth noting that V doping promotes the proportion of Vo from 13.7% to 16.6%. The increasing number of Vo could provide more active sites for the reactants, which might be conducive to the catalytic reactions.

Quite intriguingly, it is found that V-$NaNbO_3$ (10 mol%) piezocatalysts of minimal amounts show the most excellent catalytic performance (Fig. 3(a)). The V-$NaNbO_3$ (10 mol%) piezocatalysts increasing from 10, 20, 30 to 50 mg exhibit reducing piezocatalytic efficiency (i.e., 333.0, 229.5, 184.5, and 110.7 $\mu$mol$\cdot$g$^{-1}\cdot$h$^{-1}$) of V-$NaNbO_3$, respectively (Fig. 3(a)). It has been widely accepted that the dispersion of the piezocatalysts significantly affects the performance of piezoelectric hydrogen production, as aggregation of catalysts causes the less exposure of active sites. Especially in the piezocatalytic process, V-$NaNbO_3$ nanocubes aggregate due to the electrostatic interaction between the piezoelectric surfaces possessing positive and negative charges from different catalysts. The aggregation not only reduces the number of active sites, but also weakens the built-in electric field due to the neutralization between different nanocubes. Therefore, less amounts of V-$NaNbO_3$ (10 mol% and 10 mg) possess higher piezocatalytic efficiency. Thus, catalysts of 10 mg are used in piezocatalysis.

To shed light on the advantage of V-$NaNbO_3$, the piezocatalytic $H_2O_2$ and $H_2$ evolution of pure $NaNbO_3$ and $NaNbO_3$ doped by various amount of V was evaluated in DI water under ultrasonic

![](./images/817347068686237697_4.jpg)

Figure 3 (a) Time-dependent piezocatalytic $H_2$ evolution of V-NaNbO$_3$ (10 mol%) of different weights. (b) Time-dependent piezocatalytic $H_2$ evolution of as-prepared NaNbO$_3$ and V-NaNbO$_3$ with various V doping concentrations. (c) Piezocatalytic hydrogen yield by employing as-crafted NaNbO$_3$ and V-NaNbO$_3$ containing different V doping. (d) Piezocatalytic H$_2$O$_2$ yield by employing as-crafted NaNbO$_3$ and V-NaNbO$_3$ containing different V doping.

vibrations. The $H_2$ production without catalysts is slight (i.e., 6.4 $\mu$mol$\cdot$g$^{-1}$h$^{-1}$, Fig. 3(c)). The piezocatalytic $H_2$ generation rates of NaNbO$_3$, V-NaNbO$_3$ (5 mol%), V-NaNbO$_3$ (10 mol%), and V-NaNbO$_3$ (15 mol%) are 75.0, 200.4, 346.2, and 225.2 $\mu$mol$\cdot$g$^{-1}$h$^{-1}$, respectively (Fig. 3(c)). An obvious increase of $H_2$ generation rate is exhibited over piezocatalysts with the increasing amount of V doping from 0 mol% to 10 mol%. Clearly, V-NaNbO$_3$ (10 mol%) possesses the optimal piezocatalytic efficiency and shows a 4.6-fold improvement compared to pristine NaNbO$_3$. However, the $H_2$ yield decreases sharply when NaNbO$_3$ is doped by V of 15 mol%. This reduction of the piezocatalytic performance indicates that too much V might serve as the charge recombination centers. In other words, doping appropriate amount of V into the lattice of NaNbO$_3$ could enhance its catalytic activity. More reasons will be discussed in the latter parts.

At the same time, H$_2$O$_2$ yields of NaNbO$_3$ and V-NaNbO$_3$ were measured (Fig. 3(d)), which shows a similar trend as $H_2$ generation rates. After V doping, NaNbO$_3$ piezocatalysts display higher catalytic activity (Fig. 3(d)). The H$_2$O$_2$ yields of NaNbO$_3$, V-NaNbO$_3$ (5 mol%), V-NaNbO$_3$ (10 mol%), and V-NaNbO$_3$ (15 mol%) nanocubes are 46.4, 54.7, 102.6, and 88.0 $\mu$mol$\cdot$g$^{-1}$h$^{-1}$, respectively. V-NaNbO$_3$ (10 mol%) achieves the highest H$_2$O$_2$ generation efficiency, which is 2.21 times higher than pristine NaNbO$_3$. During the piezocatalytic water oxidation, H$_2$O$_2$, OH$\cdot$, and solvated hydroxyl are produced. OH$\cdot$ radicals could react with each other to form H$_2$O$_2$. Therefore, the generation of solvated hydroxyl is the main reason that leads to the yield proportion of H$_2$O$_2$ to $H_2$ lower than 1:1.

In order to better understand the piezocatalytic activity, piezoelectric properties of pure NaNbO$_3$ and V-NaNbO$_3$ (10 mol%) were explored via a PFM. The piezo-responses of NaNbO$_3$ and V-NaNbO$_3$ (10 mol%) were measured by the PFM tip scanning across a $2.0\ \mu$m $\times 2.0\ \mu$m surface area. Figures 4(a) and 4(b) show a three-dimensional (3D) view of NaNbO$_3$ and V-NaNbO$_3$ surface topography, revealing the quantitative height signals and the detailed surfaces. Concurrently, applying a probe bias in the polarization direction of the same region, the change of amplitude and phase can be observed (Figs. 4(c)-4(f)). Compared with pure NaNbO$_3$, V-NaNbO$_3$ (10 mol%) achieves higher piezoelectric response (Figs. 4(c)-4(f)). This suggests that V doping might increase the structure asymmetry of NaNbO$_3$, further increasing the polarization and thus causing the improved piezocatalytic efficiency.

The piezocatalytic mechanism is illustrated in Fig. 5(a). Under the application of the mechanical force, the lattice displacement of V-NaNbO$_3$ (10 mol%) creates dipole moments, thus forming an internal polarized electric field. Driven by this polarization-induced potential, free electrons and holes move toward the opposite direction and participate in the catalytic $H_2$ generation and H$_2$O$_2$ evolution reactions, respectively.

To further investigate the piezocatalytic mechanism of overall water splitting, the first-principle calculations based on DFT provide a possible understanding of V-NaNbO$_3$ surface reactions at the atomic scale. From the structural simulation of V-NaNbO$_3$, the bond length of V-O (3.288 Å) is similar as Nb-O (3.332 Å), which remains the structure integrity of NaNbO$_3$ after doped by vanadium. Simultaneously, slightly shortened V-O bond enlarges the asymmetry of NaNbO$_3$ crystal structure. This suggests the enhanced piezo-response, agreeing well with the PFM results (Fig. 4) [38].

As shown in Fig. 5(b), the dissociation barrier of H$_2$O on stressed (001) V-NaNbO$_3$ surface (i.e., 0.360 eV) is lower than on the NaNbO$_3$ counterpart (i.e., 0.508 eV), indicating that V doping facilitates the water dissociation. In addition, compared with NaNbO$_3$ (0.924 eV), V-NaNbO$_3$ possesses a more optimized $\Delta G_{H^\cdot}$, resulting in that $H_2$ generation is prone to occur on the V-NaNbO$_3$ surface (Fig. 5(c)). Free energy of the first water oxidation step is another vital parameter to determine catalytic activity and selectivity in water dissociation. On the basis of previous thermodynamic studies [39,40], free energy of the formation of adsorbed OH over V-NaNbO$_3$ is closer to OH$\cdot$ in comparison with NaNbO$_3$ [41], suggesting that it is more favorable for OH$\cdot$ to be produced on V-NaNbO$_3$ surface than the NaNbO$_3$ counterpart (Fig. 5(d)). This is confirmed by the

![](./images/817347068686237697_5.jpg)

![](./images/817347068686237697_6.jpg)

Figure 4 (a) and (b) Surface topographies, (c) and (d) PFM amplitudes, and (e) and (f) PFM phase images of pure $NaNbO_3$ and $V$-$NaNbO_3$ (10 mol%) measured in air.

![](./images/817347068686237697_7.jpg)

Figure 5 (a) Schematic illustration of $NaNbO_3$ piezocatalytic mechanism under ultrasonic vibrations. Free energy diagrams of (b) water dissociation, (c) hydrogen generation, and (d) $H_2O_2$ generation on stressed $NaNbO_3$ and $V$-$NaNbO_3$ (001) surface. (e) Schematic illustration of calculated hydrogen evolution process on stressed $V$-$NaNbO_3$ surface and atomic structure of $V$-$NaNbO_3$ (001) surface with oxygen vacancy.

experimental data of OH. generation using $NaNbO_{3}$ and V- $NaNbO_{3}$ (10 mol%) as the piezocatalysts (Fig. S3 in the ESM). Figure 5(e) shows a water dissociation process on the (001) plane of stressed $V-NaNbO_{3}$. During the piezocatalytic process, $H_{2}O$ tends to be adsorbed on the V atom of $NaNbO_{3}$ (Fig. 5(e)(i)). Then one H atom of adsorbed $H_{2}O$ molecule moves to the nearest O site to form O-H species and generates $OH^{*}$ in the initial position, where $OH^{*}$ swiftly converts to OH. (Figs. 5(e)(ii) and 5(e)(iii)) [42]. After the as-obtained OH. radicals combine to form $H_{2}O_{2}$ molecules, $H_{2}O_{2}$ detaches from the $V-NaNbO_{3}$ surface (Figs. 5(e)(iv)-5(e)(vi)). In the meanwhile, H atoms of nearby O-H species approach each other to generate $H_{2}$ molecules (Figs. 5(e)(iv)-5(e)(vi)) [43-46].

## 4 Conclusions
In summary, we develop a green and efficient piezocatalytic process initiated by the mechanical force to achieve IWS, concurrently obtaining value-added $H_{2}O_{2}$ and $H_{2}$ from pure water. In this study, ternary oxides (i.e., $NaNbO_{3}$ single crystal nanocubes) are chosen as the model piezocatalysts. In order to enhance the piezoelectric properties, V is doped into the lattice of $NaNbO_{3}$. V doping reduces the crystal size of $NaNbO_{3}$, obviously increasing the specific surface area of catalysts. The PFM measurements suggest that, after modified by V, the piezo- response of $NaNbO_{3}$ is promoted. In addition, surface oxygen vacancies of $NaNbO_{3}$ are induced during the V doping, as revealed by XPS spectra. As a result, the optimal piezocatalytic $H_{2}$ and $H_{2}O_{2}$ evolution of $V-NaNbO_{3}$ is markedly improved by 4.6 and 2.2-fold, respectively, compared with pristine $NaNbO_{3}$. The lower production rate of $H_{2}O_{2}$ than $H_{2}$ is due to the produced solvated hydroxyls during the piezocatalysis. It is worth noting that the piezocatalytic activity of $V-NaNbO_{3}$ is inversely proportional to its used weight. Catalysts of 10 mg exhibit the best catalytic performance, which 3.1 times better than those of 50 mg. According to DFT calculations, V doping expands the asymmetryof $NaNbO_{3}$ crystal structure by replacing $Nb-O$ bond $(3.332 \AA)$  with shortened $V-O$ bond $(3.288 \AA)$ . More importantly, V doping reduces the reaction dynamic barrier of water dissociation over $NaNbO_{3}$ , consequently facilitating the production of $H_{2}O_{2}$ and $H_{2}$ . V acts as the active sites for piezocatalysis, which improves the piezocatalytic efficiency. As such, this strategy supplies a general way to design piezocatalytic system using green energy (such as tide, wind, and wave) for potential applications in water splitting and environmental treatments.

## Acknowledgements
M. Y. W. gratefully acknowledges the financial support from the National Natural Science Foundation of China (No. 21905317), the Young Elite Scientists Sponsorship Program by CAST (No.2019QNRC001), and Open Fund of Guangdong Provincial Key Laboratory of Solid Wastes Pollution Control and Recycling (No.2020B121201003).

Electronic Supplementary Material: Supplementary material(typical Raman spectra of $NaNbO_{3}$ and $V-NaNbO_{3}$ with various doping concentrations (Fig. S1). XPS spectra of Na 1s (Fig. S2). PL spectra of solution obtained from the piezocatalytic system using $NaNbO_{3}$ and $V-NaNbO_{3}$ (10 mol\%) as the catalysts after $1 ~h$ (Fig. S3). The length of $NaNbO_{3}$ and $V-NaNbO_{3}$ nanocubes calculated from XRD data of their (101) planes (Table S1)) is available in the online version of this article at https://doi.org/10.1007/s12274-022-4506-0.

![](./images/817347068686237697_8.jpg)
![](./images/817347068686237697_9.jpg)

## References
[1] Lei, J. Y.; Chen, B.; Lv, W. J.; Zhou, L.; Wang, L. Z.; Liu, Y. D.; Zhang, J. L. Robust photocatalytic $H_{2}O_{2}$ production over inverse opal g- $C_{3}N_{4}$ with carbon vacancy under visible light. ACS Sustain. Chem. Eng. 2019, 7, 16467-16473.

[2] Wang, Z. Z.; Zhao, Y. J.; Zhou, Y. J.; Wang, X.; Huang, H.; Liu, Y.; Shao, M. W.; Kang, Z. H. All-in-one photocatalysis device for one- step high concentration $H_{2}O_{2}$ photoproduction. Chem. Eng. J. 2022,427,131972.

[3] Hou, H. L.; Zeng, X. K.; Zhang, X. W. Production of hydrogen peroxide by photocatalytic processes. Angew. Chem., Int. Ed. 2020,59,17356-17376.

[4] Yang, S.; Verdaguer-Casadevall, A.; Arnarson, L.; Silvio, L.; Čolić, V.; Frydendal, R.; Rossmeisl, J.; Chorkendorff, I.; Stephens, I. E. L. Toward the decentralized electrochemical production of $H_{2}O_{2}$ : A focus on the catalysis. ACS Catal. 2018, 8, 4064-4081.

[5] Zhang, J. N.; Hu, W. P.; Cao, S.; Piao, L. Y. Recent progress for hydrogen production by photocatalytic natural or simulated seawater splitting. Nano Res. 2020, 13, 2313-2322.

[6] Iwashina, K.; Iwase, A.; Ng, Y. H.; Amal, R.; Kudo, A. Z-schematic water splitting into $H_{2}$ and $O_{2}$ using metal sulfide as a hydrogen evolving photocatalyst and reduced graphene oxide as a solid-state electron mediator. J. Am. Chem. Soc. 2015, 137, 604-607.

[7] Cui, X.; Zhao, Q.; Huang, Z. M.; Xiao, Y. F.; Wan, Y. P.; Li, S. L.;Lee, C. S. Water-splitting based and related therapeutic effects: Evolving concepts, progress, and perspectives. Small 2020, 16,2004551.

[8] Zhao, J.; He, X. Y. Preparation and electrocatalytic properties of oxygen precipitation of amorphous NiCo oxide. J. Synth. Cryst.2020,49,896-897.

[9] Huang, J.; Wang, Y.; Liu, X. Q.; Li, Y. C.; Hu, X. Q.; He, B.; Shu, Z.; Li, Z.; Zhao, Y. L. Synergistically enhanced charge separation in $BiFeO_{3}/Sn:TiO_{2}$ nanorod photoanode via bulk and surface dual modifications. Nano Energy, 2019, 59, 30-40.

[10] He, B.; Jia, S. R.; Zhao, M. Y.; Wang, Y.; Chen, T.; Zhao, S. Q.; Li, Z.; Lin, Z. Q.; Zhao, Y. L.; Liu, X. Q. General and robust photothermal-heating-enabled high-efficiency photoelectrochemical water splitting. Adv. Mater. 2021, 33, 2004406.

[11] Lin, Z. Q.; Zhi, C. Y.; Qu, L. T. Nano Research Energy: An interdisciplinary journal centered on nanomaterials and nanotechnology for energy. Nano Res. Energy 2022, I, e9120005.

[12] Wu, J.; Qin, N.; Bao, D. H. Effective enhancement of piezocatalytic activity of $BaTiO_{3}$ nanowires under ultrasonic vibration. Nano Energy 2018,45,44-51.

[13] Su, Y.; Zhang, L.; Wang, W. Z.; Li, X. M.; Zhang, Y. L.; Shao, D. K. Enhanced $H_{2}$ evolution based on ultrasound-assisted piezo catalysis of modified $MoS_{2}$ . J. Mater. Chem. A 2018, 6,11909-11915.

[14] Wu, J. M.; Chang, W. E.; Chang, Y. T.; Chang, C. K. Piezo-catalytic effect on the enhancement of the ultra-high degradation activity in the dark by single- and few-layers $MoS_{2}$ nanoflowers. Adv. Mater.2016, 28, 3718-3725.

[15] Zhao, X. N.; Lei, Y. C.; Fang, P. F.; Li, H. J.; Han, Q.; Hu, W. G.; He, C. Q. Piezotronic effect of single/few-layers $MoS_{2}$ nanosheets composite with $TiO_{2}$ nanorod heterojunction. Nano Energy 2019, 66,104168.

[16] Kubota, K.; Pang, Y. D.; Miura, A.; Ito, H. Redox reactions of small organic molecules using ball milling and piezoelectric materials. Science 2019, 366, 1500-1504.

[17] Zhao, L. L.; Zhang, Y.; Wang, F. L.; Hu, S. C.; Wang, X. N.; Ma, B. J.; Liu, H.; Wang, Z. L.; Sang, Y. H. $BaTiO_{3}$ nanocrystal-mediated micro pseudo-electrochemical cells with ultrasound-driven piezotronic enhancement for polymerization. Nano Energy 2017, 39,461-469.

[18] Payandeh, S.; Strauss, F.; Mazilkin, A.; Kondrakov, A.; Brezesinski, T. Tailoring the $LiNbO_{3}$ coating of Ni-rich cathode materials for stable and high-performance all-solid-state batteries. Nano Res. Energy 2022, 1: e9120016.

[19] Liu, D. Y.; Zeng, Q.; Hu, C. Q.; Chen, D.; Liu, H.; Han, Y. S.; Xu,

L.; Zhang, Q. B.; Yang J. Light doping of tungsten into copper-platinum nanoalloys for boosting their electrocatalytic performance in methanol oxidation. *Nano Res. Energy* **2022**, 1: e9120017.

[20] Veldurthi, N. K.; Jitta, R. R.; Ravi, G.; Guje, R.; Velchuri, R.; Venkataswamy, P.; Vithal, M. Fabrication and visible-light induced photocatalytic activity of $\mathrm{NaNbO_3}$ oriented composite photocatalyst coupled with $\mathrm{N-NaNbO_3}$ and $\mathrm{V-NaNbO_3}$. *ChemistrySelect* **2016**, 1, 2783–2791.

[21] Wei, Y.; Zhang, J. Z.; Zheng, Q.; Miao, J.; Alvarez, P. J. J.; Long, M. C. Quantification of photocatalytically-generated hydrogen peroxide in the presence of organic electron donors: Interference and reliability considerations. *Chemosphere* **2021**, 279, 130556.

[22] Wang, B.; Zhang, Q.; He, J. Q.; Huang, F.; Li, C. F.; Wang, M. Y. Co-catalyst-free large ZnO single crystal for high-efficiency piezocatalytic hydrogen evolution from pure water. *J. Energy Chem.* **2022**, 65, 304–311.

[23] Kresse, G.; Furthmüller, J. Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set. *Phys. Rev. B* **1996**, 54, 11169–11186.

[24] Kresse, G.; Furthmüller, J. Efficiency of *ab-initio* total energy calculations for metals and semiconductors using a plane-wave basis set. *Comput. Mater. Sci.* **1996**, 6, 15–50.

[25] Kresse, G.; Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. *Phys. Rev. B* **1999**, 59, 1758–1775.

[26] Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* **1996**, 77, 3865–3868.

[27] Monkhorst, H. J.; Pack, J. D. Special points for Brillouin-zone integrations. *Phys. Rev. B* **1976**, 13, 5188–5192.

[28] Li, F.; Zhai, J. W.; Shen, B.; Liu, X.; Yang, K.; Zhang, Y.; Li, P.; Liu, B. H.; Zeng, H. R. Influence of structural evolution on energy storage properties in $\mathrm{Bi_{0.5}Na_{0.5}TiO_3}$-$\mathrm{SrTiO_3}$-$\mathrm{NaNbO_3}$ lead-free ferroelectric ceramics. *J. Appl. Phys.* **2017**, 121, 054103.

[29] Ye, J. M.; Wang, G. S.; Chen, X. F.; Cao, F.; Dong, X. L. Enhanced antiferroelectricity and double hysteresis loop observed in lead-free $\mathrm{(1\mathrm{-}x)NaNbO_3\mathrm{-}xCaSnO_3}$ ceramics. *Appl. Phys. Lett.* **2019**, 114, 122901.

[30] Li, W.; Xia, X.; Zeng, J. T.; Zheng, L. Y.; Man, Z. Y.; Li, G. R. 1/6 type diffraction patterns and double P–E hysteresis loops in $\mathrm{Bi(Mg_{2/3}Nb_{1/3})O_3}$ modified $\mathrm{NaNbO_3}$ ceramics. *J. Phys. D.: Appl. Phys.* **2020**, 53, 305302.

[31] Zhu, H. Y.; Zheng, Z. F.; Gao, X. P.; Huang, Y. N.; Yan, Z. M.; Zou, J.; Yin, H. M.; Zou, Q. D.; Kable, S. H.; Zhao, J. C. et al. Structural evolution in a hydrothermal reaction between $\mathrm{Nb_2O_5}$ and $\mathrm{NaOH}$ solution: From $\mathrm{Nb_2O_5}$ grains to microporous $\mathrm{Na_2Nb_2O_6{\cdot}2/3H_2O}$ fibers and $\mathrm{NaNbO_3}$ cubes. *J. Am. Chem. Soc.* **2006**, 128, 2373–2384.

[32] Wu, S. Y.; Zhang, W.; Chen, X. M. Formation mechanism of $\mathrm{NaNbO_3}$ powders during hydrothermal synthesis. *J. Mater. Sci.:Mater. Electron.* **2010**, 21, 450–455.

[33] Shi, H. F.; Chen, G. Q.; Zhang, C. L.; Zou, Z. G. Polymeric $\mathrm{g\text{-}C_3N_4}$ coupled with $\mathrm{NaNbO_3}$ nanowires toward enhanced photocatalytic reduction of $\mathrm{CO_2}$ into renewable fuel. *ACS Catal.* **2014**, 4, 3637–3643.

[34] Liu, J. W.; Han, R.; Zhao, Y.; Wang, H. T.; Lu, W. J.; Yu, T. F.; Zhang, Y. X. Enhanced photoactivity of V-N codoped $\mathrm{TiO_2}$ derived from a two-step hydrothermal procedure for the degradation of PCP-Na under visible light irradiation. *J. Phys. Chem. C* **2011**, 115, 4507–4515.

[35] Molak, A.; Pawelczyk, M.; Kubacki, J.; Szot, K. Nano-scale chemical and structural segregation induced in surface layer of $\mathrm{NaNbO_3}$ crystals with thermal treatment at oxidising conditions studied by XPS, AFM, XRD, and electric properties tests. *Phase Transit.* **2009**, 82, 662–682.

[36] Kubacki, J.; Molak, A.; Talik, E. Electronic structure of $\mathrm{NaNbO_3}$-Mn single crystals. *J. Alloys Compd.* **2001**, 328, 156–161.

[37] Kim, J. H.; Jang, Y. J.; Kim, J. H.; Jang, J. W.; Choi, S. H.; Lee, J. S. Defective $\mathrm{ZnFe_2O_4}$ nanorods with oxygen vacancy for photoelectrochemical water splitting. *Nanoscale* **2015**, 7, 19144–19151.

[38] Huang, H. W.; Tu, S. C.; Zeng, C.; Zhang, T. R.; Reshak, A. H.; Zhang, Y. H. Macroscopic polarization enhancement promoting photo-and piezoelectric-induced charge separation and molecular oxygen activation. *Angew. Chem., Int. Ed.* **2017**, 56, 11860–11864.

[39] Baek, J. H.; Gill, T. M.; Abroshan, H.; Park, S.; Shi, X. J.; Nørskov, J.; Jung, H. S.; Siahrostami, S.; Zheng, X. L. Selective and efficient Gd-doped $\mathrm{BiVO_4}$ photoanode for two-electron water oxidation to $\mathrm{H_2O_2}$. *ACS Energy Lett.* **2019**, 4, 720–728.

[40] Li, L. J.; Hu, Z. F.; Yu, J. C. On-demand synthesis of $\mathrm{H_2O_2}$ by water oxidation for sustainable resource production and organic pollutant degradation. *Angew. Chem., Int. Ed.* **2020**, 59, 20538–20544.

[41] You, H. L.; Wu, Z.; Zhang, L. H.; Ying, Y. R.; Liu, Y.; Fei, L. F.; Chen, X. X.; Jia, Y. M.; Wang, Y. J.; Wang, F. F. et al. Harvesting the vibration energy of $\mathrm{BiFeO_3}$ nanosheets for hydrogen evolution. *Angew. Chem., Int. Ed.* **2019**, 58, 11779–11784.

[42] Siahrostami, S.; Li, G. L.; Viswanathan, V.; Nørskov, J. K. One-or two-electron water oxidation, hydroxyl radical, or $\mathrm{H_2O_2}$ evolution. *J. Phys. Chem. Lett.* **2017**, 8, 1157–1160.

[43] Liu, Y. P.; Li, Y. H.; Li, X. Y.; Zhang, Q.; Yu, H.; Peng, X. W.; Peng, F. Regulating electron-hole separation to promote photocatalytic $\mathrm{H_2}$ evolution activity of nanoconfined $\mathrm{Ru/MXene/TiO_2}$ catalysts. *ACS Nano* **2020**, 14, 14181–14189.

[44] Liao, Y. W.; Yang, J.; Wang, G. H.; Wang, J.; Wang, K.; Yan, S. D. Hierarchical porous NiO as a noble-metal-free cocatalyst for enhanced photocatalytic $\mathrm{H_2}$ production of nitrogen-deficient $\mathrm{g\text{-}C_3N_4}$. *Rare Metals* **2022**, 41, 396–405.

[45] Wang, C. Y.; Yang, C. H.; Zhang, Z. C. Unraveling molecular-level mechanisms of reactive facet of carbon nitride single crystals photocatalyzing overall water splitting. *Rare Metals* **2020**, 39, 1353–1355.

[46] Yang, T. L.; Ni, S. F.; Qin, P.; Dang, L. A. mechanism study on the hydrogen evolution reaction catalyzed by molybdenum disulfide complexes. *Chem. Commun.* **2018**, 54, 1113–1116.