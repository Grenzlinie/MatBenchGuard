# DFT calculations of the synergistic effect of $\boldsymbol{\lambda}$-MnO₂/graphene composites for electrochemical adsorption of lithium ions†

Huixin Zhang, $^{a}$ Xiao Du, $^{*a}$ Shengqi Ding, $^{a}$ Qiang Wang, $^{a}$ Lutong Chang, $^{a}$ Xuli Ma, $^{a}$ Xiaogang Hao $^{*a}$ and Changjun Pen $^{b}$

Recently, the composite of spinel-type manganese oxide $(\lambda\text{-MnO}_2)$/graphene has drawn wide attention because of its good electrochemical adsorption selectivity for low concentrations of $\text{Li}^+$ ions from lake brine or seawater to cope with the fast-rising demand of lithium resources. In this composite, the synergistic effect between the good selectivity of $\lambda\text{-MnO}_2$ for $\text{Li}^+$ ions and the excellent conductivity of graphene play an important role for the electrochemical adsorption of $\text{Li}^+$ ions. In order to reveal the synergistic mechanism in the electronic conductivity, the ionic conductivity and the ion selectivity of the $\lambda\text{-MnO}_2$/graphene composite, density functional theory (DFT) calculations combined with electrochemical adsorption experiments were carried out. The calculation results show that the enhanced electronic conductivity of the composite is due to the decrease of the band gap $(E_g)$ in the $\lambda\text{-MnO}_2$/graphene composite compared with pure $\lambda\text{-MnO}_2$. Meanwhile, the graphene composited with $\lambda\text{-MnO}_2$ decreased the diffusion energy barrier of $\text{Li}^+$ ions in $\lambda\text{-MnO}_2$. In addition, the competitive adsorption of $\text{Li}^+$, $\text{Na}^+$ and $\text{Mg}^{2+}$ ions were investigated by the nudged elastic band (NEB) method and charge distribution analysis. The results show that $\text{Li}^+$ ions in $\lambda\text{-MnO}_2$ exist in their pure ion state and have the lowest diffusion energy barrier compared with $\text{Na}^+$ and $\text{Mg}^{2+}$. The results of the DFT calculations were validated by cyclic voltammetry, electrochemical impedance spectroscopy and electrochemical adsorption experiments.

## Introduction

With the rapid development of new energy vehicles, the demand for lithium resources is increasing more and more across the world. $^{1}$ Because lithium resources are mainly obtained from seawater and lake brines which have more than 60% of the lithium resources in the world, the extraction of lithium ions ($\text{Li}^+$ ions) from seawater and lake brines has broad prospects. $^{2,3}$ To date, the most common methods to extract lithium resources are adsorption, $^{4,5}$ ion exchange, $^{6}$ membrane separation $^{7}$ and electrodialysis. $^{8}$ Among them, the ion-sieve adsorption method has become the most promising method for $\text{Li}^+$ ion extraction in seawater and lake brines based on its low cost, easy operation and high ion selectivity. $^{9}$ However, the low adsorption capacity and high time consumption are stumbling blocks for the application of the adsorption method due to the low average concentration of $\text{Li}^+$ ions in seawater $(0.17\ \text{mg L}^{-1})$ and lake brines. Fortunately, the electrochemically switched ion exchange (ESIX) technique presents a new approach for the extraction of lithium resources from seawater, because it can be used for the extraction of low-concentration ions from aqueous solutions driven by electricity. $^{10,11}$ Herein, it is vital to develop an electro-active ion exchange material with high $\text{Li}^+$ ion selectivity to suppress the interference of $\text{Na}^+$ and $\text{Mg}^{2+}$ ions in seawater and lake brines. $^{12,13}$ Among the various ion sieves, spinel-type manganese oxide $(\lambda\text{-MnO}_2)$ is widely used because of its unique three-dimensional pore ion sieve structure, which exhibits high selectivity for $\text{Li}^+$ ions compared with other $\text{MnO}_2$ types. $^{4,5,14}$ However, $\lambda\text{-MnO}_2$ has poor electron/ion conductivity, $^{15}$ which needs further improvement of its electronic conduction and ion conduction performance.

Graphene has drawn more attention because of its zero-band gap and high conductivity. In addition, graphene also has two-dimensional honeycomb crystals formed by a single layer of carbon atoms. $^{16,17}$ In this case, it is often used as a conductive additive to improve the electrochemical properties of electrode materials because of its excellent character. $^{18}$ He *et al.* prepared a lithium manganese oxide $(\text{LiMn}_2\text{O}_4)$ nanorod electrode wrapped with graphene and found that the graphene and $\text{LiMn}_2\text{O}_4$

---

$^{a}$ Department of Chemical Engineering, Taiyuan University of Technology, Taiyuan 030024, P. R. China. E-mail: duxiao@tyut.edu.cn, xghao@tyut.edu.cn
$^{b}$ State Key Laboratory of Chemical Engineering and Department of Chemistry, East China University of Science and Technology, Shanghai, 200237, P. R. China
† Electronic supplementary information (ESI) available: Fig. S1–S3 and Tables S1–S5. See DOI: 10.1039/c9cp00714h

composite has higher capacity, electroactivity and cyclic performance compared with pure $LiMn_2O_4$ and graphene. $^{19}$ Peng *et al.* fabricated quasi-2D ultrathin $MnO_2$/graphene nanosheets as high-performance in-plane supercapacitors. $^{20}$ Furthermore, graphene is widely used in lithium-ion batteries. $^{21–23}$ Özcan *et al.* discovered freestanding graphene/$MnO_2$ cathodes for Li-ion batteries displayed the best cycling performance and better electrochemical reaction behaviour. $^{24}$ Chai *et al.* found that hierarchical holey graphene/$MnO_2$ composites have better electrochemical performances as potential electrode materials for supercapacitors. $^{25}$ Therefore, $MnO_2$/graphene composites can be considered as an ideal electrochemically switched ion exchange material for $Li^+$ ion separation. However, the unclear synergistic effect between the $MnO_2$ and the graphene has become a barrier for designing and developing this kind of composite material. Generally, it is still difficult to reveal the synergistic mechanism only through experimental research. Fortunately, theoretical calculations can be used to analyze the mechanism from the electronic level, which could provide an explanation for some experimental phenomena. $^{26–28}$

In recent years, much theoretical research has been devoted to the development of $Li^+$ ion exchange electrode materials. Quantum chemical calculations have already been applied to various electroactive materials, $^{29}$ especially for batteries. $^{21,22,30–33}$ Zhang *et al.* studied the migration mechanism of $Li^+$ ions in $Li_2FeSiO_4$ through first-principles calculations, $^{34}$ and found that $Li^+$ ions had the largest diffusion coefficient in $Li_2FeSiO_4$. Ning *et al.* studied the effect of Jahn-Teller (JT) distortion on the diffusion of lithium ions in $\lambda$-MnO$_2$ by the first-principles method, $^{35}$ and found that the lowest diffusion energy is between the Mn-O and Li-O bond when $Li^+$ ions pass through the co-line. Wang *et al.* studied the electronic structure of a graphene/LiFePO$_4$ composite material using first-principles$^{36}$ and found that LiFePO$_4$ composited with graphene has a higher $Li^+$ ion storage capacity. Although theoretical research of lithium storage materials has made great progress, the effect of graphene on the $Li^+$ ion storage for spinel manganese oxide is still lacking theoretical research.

In this paper, density functional theory (DFT) was used to calculate the geometric and electronic structure of $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene composites. Meanwhile, the effect of graphene on $\lambda$-MnO$_2$ electronic conduction and ionic conductivity was investigated. Finally, the selectivity of $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene for $Li^+$, $Na^+$ and $Mg^{2+}$ ions was studied. All calculation results are supported by cyclic voltammetry (CV), electrochemical impedance spectroscopy (EIS) and electrochemical adsorption experiments. In brief, the electrochemical adsorption performance of the electrode materials for lithium was studied from three aspects (electron conductivity, ion conductivity and ion selectivity) by experiments and theoretical calculations.

## Results and discussion

### Electronic conductivity

In this paper, the electronic structures of $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene were analyzed by the DFT+$U$ method. Fig. 1a and b show the density of states (DOS) and the projected density of states (PDOS) of $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene. As can be seen from the figure, the PDOS of the O atom and Mn atom overlap. This indicates that the Mn-O bond exhibits covalent bond properties, which provides a stable skeleton structure for the insertion and release of $Li^+$ ions. It can be seen from Fig. 1a that the density of states at the conduction band minimum (CBM) and the valence band maximum (VBM) of $\lambda$-MnO$_2$ is composed of O 2p states and Mn 3d states, in which the band gap is 1.079 eV. By observing the total DOS of $\lambda$-MnO$_2$, the orbitals do not span the Fermi level. Based on the above analysis, we could draw the conclusion that $\lambda$-MnO$_2$ is a semiconductor. But, graphene was composited with $\lambda$-MnO$_2$, which is shown in Fig. 1b. The orbitals of the total DOS of $\lambda$-MnO$_2$/graphene span the Fermi level, which demonstrates that $\lambda$-MnO$_2$/graphene is a conductor. Also, the band gap of the composite system was reduced to 0 eV, which demonstrates that the compositing of graphene improves the electronic conductivity of the material. From the figure, the PDOS intensity of O 2p and Mn 3d was increased in the composite system compared with $\lambda$-MnO$_2$. Meanwhile, it was revealed that the degree of hybridization between the O atoms and Mn atoms was improved, and the delocalization of electrons was promoted after $\lambda$-MnO$_2$ was composited with graphene.

![](./images/817402878523080705_1.jpg)

Fig. 1 DOS and PDOS of (a) $\lambda$-MnO$_2$; and (b) $\lambda$-MnO$_2$/graphene. The dashed lines refer to the Fermi level.

The degree of hybridization between the O and Mn atoms can also be observed visually from the electron density map. Fig. 2a and b show the electron density maps of the O atom and Mn atom in $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene respectively. From Fig. 2b, the obvious yellow part indicates the high degree of sharing of the electron density between the O atom and the Mn atom. It was proved that the electron density of the O atom and the Mn atom in the $\lambda$-MnO$_2$/graphene composite system overlaps to a greater degree than compared to $\lambda$-MnO$_2$. In the meantime, it was shown that the hybridization degree of the atomic orbitals between the O and Mn atoms was improved after $\lambda$-MnO$_2$ was composited with graphene. Due to O and Mn atoms being highly overlapped, electrons were easy to pass on

![](./images/817402878523080705_2.jpg)

Fig. 2 The electron density maps for O and Mn along the (1 0 1) crystal plane of (a) $\lambda$-MnO$_2$; and (b) $\lambda$-MnO$_2$/graphene.

the –O–Mn–O–Mn– chain, which promoted the delocalization of electrons. In conclusion, composited graphene improved the electronic conductivity of the material.

### Ionic conductivity
The diffusion rate of ions is an important indicator to estimate the performance of electrode materials. $^{37}$ In this paper, a LST/QST transition state search and the NEB method were used to study the diffusion properties of Li⁺ ions in $\lambda$-MnO₂ and $\lambda$-MnO₂/graphene. According to previous studies, Li⁺ ions diffuse in the form of a three-dimensional channel through $\lambda$-MnO₂, $^{35,38}$ which is on the surface (1 0 1). As Fig. 3a shows, the Li⁺ ion diffuses from the 8a position of a LiO₄ tetrahedron in $\lambda$-MnO₂ through the 16c position of the intermediate octahedron to the 8a position of the adjacent LiO₄ tetrahedron in the $\lambda$-MnO₂. $^{35,38}$ Meanwhile, the energy barrier of this diffusion process was 1.09 eV. Moreover, it was reported that the diffusion path of the Li⁺ ion between two graphene layers is HT–HT (H: hexagon site; T: top site) as shown in Fig. 3b. $^{39}$ By the NEB method, the energy barrier of the Li⁺ ion in the diffusion process between graphene layers was 0.058 eV, which was much lower than the Li⁺ ion in $\lambda$-MnO₂, indicating that Li⁺ ions spread faster in graphene. In order to study the effect of the composited graphene on the diffusion characteristics of Li⁺ ions in $\lambda$-MnO₂, a surface was cleaved on $\lambda$-MnO₂ along the diffusion direction of Li⁺ ions, namely, the (1 0 1) surface. Subsequently, in order to study the synergistic effect of graphene and $\lambda$-MnO₂ on Li⁺ ion diffusion, the (1 0 1) surface was composited with a graphene surface (shown in Fig. 3c). The diffusion energy barrier of Li⁺ ions was 0.76 eV in $\lambda$-MnO₂/graphene (shown in Fig. 3d), suggesting that the diffusion energy barrier of Li⁺ ions was greatly reduced after $\lambda$-MnO₂ was composited with graphene. To sum up, this result indicates that the compositing graphene improves the ionic conductivity, promotes the diffusion of Li⁺ ions in the material, and improves the adsorption rate of Li⁺ ions.

![](./images/817402878523080705_3.jpg)

Fig. 3 The diffusion path (a–c) and energy barrier (d) of Li⁺ in (a) $\lambda$-MnO₂; (b) graphene; and (c) $\lambda$-MnO₂/graphene.

In order to analyze the intrinsic mechanism of graphene promoted Li⁺ ion diffusion in materials, the structure of the LiMn₂O₄/graphene composite system was analyzed through DFT calculations. Table S3 (ESI†) lists the Mn–O average bond length ($L_{\text{Mn-O}}$) and Li–O average distance ($d_{\text{Li-O}}$) between internal LiMn₂O₄ and the LiMn₂O₄/graphene interface. Here, the $L_{\text{Mn-O}}$ at the interface of the LiMn₂O₄/graphene composite system tends to be shorter when compared with the structure of LiMn₂O₄. The shrink of the $\lambda$-MnO₂ framework at the interface leads to the enlargement of the Li–O distance $d_{\text{Li-O}}$, which increased the diffusion channel of Li⁺ ions and reduced the steric hindrance of Li⁺ ions in the diffusion process. Therefore, the diffusion coefficient of Li⁺ ions in the material was increased. Through DFT and NEB method analysis, $\lambda$-MnO₂ composited with graphene facilitates the diffusion of Li⁺ ions in the material, thereby improving the ionic conductivity of the material.

### Ionic selectivity
In this paper, DFT and NEB methods were used to investigate the adsorption selectivity of $\lambda$-MnO₂/graphene for Li⁺ ions in aqueous solution. Common ions Na⁺ and Mg²⁺ were also calculated to investigate the competitive adsorption with Li⁺. Fig. 4 shows a diffusion energy barrier figure of Li⁺, Na⁺ and Mg²⁺ in $\lambda$-MnO₂, graphene and $\lambda$-MnO₂/graphene respectively, which was calculated by the NEB method. In general, a high energy barrier indicates that lithium ion migration is more difficult in the crystal, and a low energy barrier indicates that lithium ions migrate more easily within the crystal. $^{40,41}$ As illustrated in Fig. 4a, the diffusion energy barriers of Li⁺, Na⁺ and Mg²⁺ were 1.09 eV, 1.31 eV and 1.53 eV in $\lambda$-MnO₂ respectively. Obviously, this result indicates that the pore structure of spinel-type $\lambda$-MnO₂ is more conducive to the diffusion of Li⁺ ions. So, $\lambda$-MnO₂ has good diffusion selectivity for Li⁺ ions. Observing Fig. 4c, the diffusion energy barriers of Li⁺, Na⁺, and Mg²⁺ between the $\lambda$-MnO₂ and graphene layers were 0.76 eV, 0.91 eV, and 1.15 eV respectively, indicating that the diffusion energy barrier of the above three ions is reduced after compositing with graphene. Here, one can draw the conclusion that the $\lambda$-MnO₂/graphene composite system still has high

![](./images/817402878523080705_4.jpg)

Fig. 4 The diffusion energy barriers of Li⁺, Na⁺ and Mg²⁺ by NEB calculations in (a) $\lambda$-MnO₂; (b) graphene; and (c) $\lambda$-MnO₂/graphene, respectively.

diffusion selectivity for $Li^{+}$ ions. Fig. 4b shows that the diffusion energy barriers of $Li^{+}$, $Na^{+}$ and $Mg^{2+}$ have little difference in pure graphene. Obviously, $\lambda$-$MnO_{2}$ plays a major role in ion selectivity.

In order to further analyze why $\lambda$-$MnO_{2}$ has higher diffusion selectivity for $Li^{+}$ ions, Mulliken charges and bonds were studied. As shown in Table S4 (ESI$\dagger$), the net charge of Li is $1.06e$ in $LiMn_{2}O_{4}$, which is close to the formal charge of $Li^{+}$ ions. Interestingly, it was found that there is a pure ionic bond between Li and O, so Li with a high ionization degree is easier to migrate and spread in $\lambda$-$MnO_{2}$.

On the contrary, the Mulliken charges of Na and Mg atoms are $0.84e$ and $1.79e$ in $NaMn_{2}O_{4}$ and $MgMn_{2}O_{4}$ respectively, which deviate from their formal charges. From the Mulliken charges, we can come to the conclusion that Na and Mg are not ionized completely, and there are covalent bond components between Na, Mg and O. Accordingly, Na and Mg have a high energy barrier in the diffusion process. Moreover, the strength of the covalent bond can be analyzed by bond population quantitatively. Generally, a large bond population value indicates a high covalent degree of the bond, and a bond population value close to 0 indicates a high degree of ionic bonding. $^{42}$ The bond population value of Li-O is 0 (Table S4, ESI$\dagger$), indicating that there is no covalent interaction between Li and O, and Li exists in pure ion form. So, higher ionization promotes reversible electrochemical adsorption of Li in $\lambda$-$MnO_{2}$. Whereas, the Na-O and Mg-O bond populations are 0.13 and $-1.38$ respectively, which shows that there is a covalent interaction between Na, Mg atoms and O atoms, and it can enable the higher diffusion energy barrier of $Na^{+}$ and $Mg^{2+}$ in $\lambda$-$MnO_{2}$.

Electron density difference maps can be used to analyze electron transfer and bonding visually. As shown in Fig. 5, the red and blue regions represent the increase and decrease of electron density respectively. Here, the electron density decreases on Mn and increases on O, which demonstrated that electrons are transferred from Mn atoms to O atoms. Subsequently, a strong covalent bond is formed between Mn and O, which makes the electrode material have a relatively stable structure. In the following, the electron density is changed after Li enters in $\lambda$-$MnO_{2}$ (Fig. 5a), and the electron density change of Li is close to 0. This result indicates that electron transfer does not occur on Li. Here, Li exists in the form of a pure ionic state in $LiMn_{2}O_{4}$, which is beneficial for the electrochemical adsorption of $Li^{+}$. In Fig. 5b and c, the electron density of the Na and Mg atoms increases, suggesting that there is electron transfer between Na, Mg atoms and $\lambda$-$MnO_{2}$. Due to the state of this electron transfer, Na and Mg are not in the form of their pure ionic state. As a consequence, Na and Mg have a higher diffusion energy barrier in the process of diffusing in the material.

![](./images/817402878523080705_5.jpg)

Fig. 5 Electron density difference maps along the (1 0 1) crystal plane of (a) $LiMn_{2}O_{4}$; (b) $NaMn_{2}O_{4}$; and (c) $MgMn_{2}O_{4}$.

## Experimental verification
The prepared nanorod shapes of $\lambda$-$MnO_{2}$ and the $\lambda$-$MnO_{2}$/graphene composites are in good agreement with the previous SEM images (Fig. S1a and b, ESI$\dagger$). $^{11}$ A CV curve was used to verify the effect of graphene on the electrochemical ion exchange performance of $\lambda$-$MnO_{2}$. Fig. 6 shows the CV curves of graphene, $\lambda$-$MnO_{2}$ and $\lambda$-$MnO_{2}$/graphene electrode materials. For the $\lambda$-$MnO_{2}$ electrode, a significant redox peak occurred in the CV curve, which can be attributed to the redox reaction between $Mn^{3+}$/$Mn^{4+}$ in $\lambda$-$MnO_{2}$, and the adsorption of $Li^{+}$ ions. In the process of $Mn^{3+}$ being oxidized to $Mn^{4+}$, $Li^{+}$ ions are removed from the material. In the process of $Mn^{4+}$ being reduced to $Mn^{3+}$, $Li^{+}$ ions are taken up in the material. Graphene has little adsorption and storage capacity for $Li^{+}$ ions, so the graphene electrode exhibits the smallest current density compared with $\lambda$-$MnO_{2}$ and $\lambda$-$MnO_{2}$/graphene. Besides, after $\lambda$-$MnO_{2}$ was com- posited with graphene, the redox peak current intensity was obviously enhanced, and the area enclosed by the curve was also obviously increased. Thus, the electrochemical ion exchange performance of $Li^{+}$ ions in electrode materials is improved, which is consistent with the theoretical calculation results.

EIS is a means of analyzing the electrochemical properties of materials. $^{43,44}$ EIS is made up of a semicircle in the high-frequency region and a straight line in the low-frequency region. In the EIS, $R_{ct}$ represents the charge transfer resistance, which is linked to the Faraday electrochemical reaction of the material. The slope of the linear part is defined as $Z_{w}$, which is associated with diffusion performance from the electrolyte to the electrode material. The smaller the semicircle diameter and the larger the slope of the linear part shows the better electron conductivity and ion diffusivity of the material. $^{26}$ In addition, $R_{e}$, $C_{L}$ and $C_{dl}$ respectively represent the electrolyte resistance, the limiting capacitance, and the interface double capacitance. In this work, pure $\lambda$-$MnO_{2}$ and $\lambda$-$MnO_{2}$/graphene Nyquist impedance plots and their corresponding equivalent circuit model are shown in Fig. $7.^{45}$ It can be seen that $\lambda$-$MnO_{2}$/graphene has a smaller semicircular diameter than pure $\lambda$-$MnO_{2}$ in the high frequency region, which indicates the higher electron conduction performance

![](./images/817402878523080705_6.jpg)

Fig. 6 CV curves of graphene, $\lambda$-$MnO_{2}$ and $\lambda$-$MnO_{2}$/graphene electrodes at a scan rate of $10 mV s^{-1}$ in $0.1 M Li_{2}SO_{4}$ solution with a potential range of 0.2-1.2 V.

![](./images/817402878523080705_7.jpg)

Fig. 7 Impedance Nyquist plots and the corresponding equivalent circuit models of graphene, $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene in the frequency range from 10 mHz to 100 kHz.

of $\lambda$-MnO$_2$/graphene. Since graphene has almost no adsorption capacity for Li$^+$ ions, the Li$^+$ ion does not adsorb and desorb well on graphene, so graphene has a larger semicircular diameter and a smaller slope of the linear part compared to $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene. On the basis of the EIS data (Table S5, ESI$\dagger$), with the composite of graphene, the $R_{\text{ct}}$ became smaller, suggesting that the electron conduction performance of the material is enhanced after compositing with graphene. At the same time, the result of the calculations is in agreement with the density of states of pure $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene. Besides, in the low frequency region, $\lambda$-MnO$_2$/graphene has a larger linear slope than pure $\lambda$-MnO$_2$, which indicates the higher ion diffusion performance of $\lambda$-MnO$_2$/graphene. Meanwhile, the $Z_{\text{w}}$ became bigger, indicating that the composite of graphene facilitated the diffusion of ions. The result of the calculations is in agreement with the diffusion energy barrier diagram of pure $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene.

The competitive selectivity of Li$^+$, Na$^+$ and Mg$^{2+}$ was studied in a ternary mixed solution of 5 ppm LiCl, NaCl and MgCl$_2$ respectively. The competitive adsorption curves of Li$^+$, Na$^+$ and Mg$^{2+}$ on $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene are shown in Fig. 8. $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene show high selectivity for Li$^+$ compared to Na$^+$ and Mg$^{2+}$, which is well consistent with the calculation result of ion selectivity. Besides, the adsorption capacity of $\lambda$-MnO$_2$ to Li$^+$ ions is almost unchanged compared to $\lambda$-MnO$_2$/graphene, but the adsorption rate is improved after graphene was composited. The saturation adsorption time of Li$^+$ ions is decreased from 60 to 40 minutes. On the other hand, it was found that graphene has almost no adsorption capacity for Li$^+$, Na$^+$ and Mg$^{2+}$ through experimental tests.

![](./images/817402878523080705_8.jpg)

Fig. 8 Competitive adsorption kinetics curves of Li$^+$, Na$^+$ and Mg$^{2+}$ ions on $\lambda$-MnO$_2$ (a); and $\lambda$-MnO$_2$/graphene (b).

## Conclusions

In summary, the ESIX performance of $\lambda$-MnO$_2$/graphene for Li$^+$ ions was studied by theoretical calculation methods as well as experimental investigation. All of the computational results are in good agreement with the experimental results. A DFT approach has been used in the study of electronic conductivity, ionic conductivity and ion selectivity. Conclusions indicate that the high electronic conductivity of $\lambda$-MnO$_2$/graphene is due to the narrow band gap and the high degree of hybridization of Mn and O atoms, and the good ionic conductivity of $\lambda$-MnO$_2$/graphene is attributed to the low diffusion energy barrier, a large average $d_{\text{Li-O}}$, and a small $L_{\text{Mn-O}}$. Meanwhile, compared to Na$^+$ and Mg$^{2+}$, the lower diffusion energy barriers of Li$^+$ resulted in a higher diffusion selectivity for Li$^+$ ions. Moreover, Mulliken charge population, the bond population, and difference electron density analysis show that Li$^+$ ions exist in the form of their pure ionic state in $\lambda$-MnO$_2$, which causes a lower diffusion energy barrier of Li$^+$ ions. This work systematically expounds the reasons for the synergistic effect in $\lambda$-MnO$_2$/graphene composite materials from the electronic level, and provides useful ideas for efficient electroactive material design.

## Methods

### Materials and synthesis

**Preparation of precursor $\boldsymbol{\beta}$-MnO$_2$.** 8 mmol of hydrated manganese sulfate (MnSO$_4$$\cdot$H$_2$O) and ammonium persulfate $[({\text{NH}}_4)_2{\text{S}}_2{\text{O}}_8]$ were mixed together to form a dispersed solution. Subsequently, stirring was continued until it was homogeneous, and then it was placed in a hydrothermal reaction vessel of polytetrafluoroethylene maintained at 120 °C for 12 h, to obtain a black solid $\beta$-MnO$_2$. Finally, this was filtered and washed several times with deionized water, and dried at 120 °C.$^{46}$

**Preparation of $\boldsymbol{\lambda}$-MnO$_2$.** 5 mmol of the above synthesized $\beta$-MnO$_2$ and 2.5 mmol of lithium hydroxide monohydrate (LiOH$\cdot$H$_2$O) were mixed, dispersed in 10 mL of absolute ethanol. This was followed by 20 min of ball milling to dry it at room temperature. Subsequently, this was calcined at 700 °C for 10 h to get a dark gray powder of LiMn$_2$O$_4$ and then was pretreated by ultrasonication for 1.0 h in a 0.5 M H$_2$SO$_4$ solution. Finally, the material was filtered, washed and dried to obtain a red solid $\lambda$-MnO$_2$.$^{47}$

**Preparation of $\boldsymbol{\lambda}$-MnO$_2$/graphene.** 0.3 g of PVA and 60 mL of distilled water were mixed at a constant temperature controlled by a water bath at about 80 °C until it was completely dissolved. When the temperature was dropped down to about 30 °C, 0.03 g of succinic acid was added to the above solution and stirred until completely dissolved. Subsequently, the mixed aqueous solution was sealed with plastic wrap and allowed to stand for 30 min to get solution A. Meanwhile, 6 mg of graphene was added to 40 mL distilled water, and later stirred at 80 °C until it

was completely dissolved. 60 mg of $\lambda$-MnO$_2$ was added to the graphene dispersion and treated by ultrasonication for 30 min to get solution B. After the A and B solutions were mixed and sonicated for 1 min, the bubbles at the surface were removed. Subsequently, filtering was performed with PTFE filter paper using a vacuum extraction filter device. Finally, the above mixture was dried at room temperature for 1 hour.$^{48}$

Characterization and electrochemical measurements

The electrochemical performance of the graphene, $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene electrodes was tested in a three-electrode system with EC-Lab software on the VMP3 potentiostat at room temperature. Cyclic voltammetry (CV) was performed in which a quartz wafer coated with film material was used as the working electrode, and a platinum wire was used as the counter electrode. Furthermore, CV, electrochemical impedance spectroscopy (EIS) and electrochemical adsorption experiments were tested for pure graphene, $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene. The electrolyte was a 0.1 mol L$^{-1}$ Li$_2$SO$_4$ solution for testing CV and EIS. The working electrodes were prepared by mixing graphene, $\lambda$-MnO$_2$ or $\lambda$-MnO$_2$/graphene powder, carbon black and polyvinylidine fluoride (PVDF) (mass ratio of 7:2:1) on the Pt sheet (1 cm $\times$ 1 cm), and a Pt sheet (1 cm $\times$ 1 cm) as the counter electrode. But for the electrochemical adsorption experiments, the electrode material was coated on the graphite paper (2 cm $\times$ 3 cm) as the working electrode, and a steel sheet (2 cm $\times$ 3 cm) as the counter electrode. Ag/AgCl electrodes were used as reference electrodes for the above three experiments. CV performance tests were performed for the graphene, $\lambda$-MnO$_2$ and $\lambda$-MnO$_2$/graphene film electrodes at a sweep speed of 10 mV s$^{-1}$ with a voltage window range of 0.2-1.2 V. EIS was carried out at an open circuit voltage of 0 V and a frequency range of 10 mHz to 100 kHz with an amplitude of 5 mV. Moreover, electrochemical adsorption experiments were performed in a mixed solution containing LiCl, NaCl and MgCl$_2$, in which each cation concentration was 5 ppm.

Computational details

LiMn$_2$O$_4$ and delithiated $\lambda$-MnO$_2$ belong to the cubic system, where the lattice constant is $a = b = c = 8.236$ Å, and the space group is $Fd3m$.$^{49}$ According to the literature reports, the diffusion path of Li$^+$ ions in $\lambda$-MnO$_2$ passes a tetrahedral (8a) site through the intermediate octahedral (16c) site to the adjacent tetrahedral (8a) site.$^{35}$ As shown in Fig. S2a (ESI$\dagger$), in order to study the synergistic effect of graphene and $\lambda$-MnO$_2$ on the Li$^+$ ion diffusion performance, a surface along the diffusion path of Li$^+$ ions in $\lambda$-MnO$_2$ was cleaved, namely, the (1 0 1) surface in Fig. S2b (ESI$\dagger$), and then the (1 0 1) surface and monolayer graphene were composited. The distance of the $\lambda$-MnO$_2$/graphene composites was optimized, of which the distance was 3.406 Å. The phonon dispersion calculation shows no imaginary frequency, which indicates that the structure is dynamically stable (Fig. S4, ESI$\dagger$).$^{50,51}$ After that, the binding energy at the basis of the $\lambda$-MnO$_2$/graphene composites was calculated well, finding that the interface of $\lambda$-MnO$_2$/graphene was the most stable position (Table S1, ESI$\dagger$).$^{52}$ Moreover, the binding energies at the G, T1, T2 and T3 sites were calculated and it was found that the binding energies were the lowest in the T1 site. So, Li$^+$ ions likely tend to occupy the interface sites (Fig. S3 and Table S2, ESI$\dagger$). Some literature also found that it is easy for the Li$^+$ ion to occupy the interface sites.$^{52,53}$ Then, a 15 Å vacuum layer was built to eliminate the influence of the c-axis between the top layer and each other layer.$^{52}$ Moreover, the $\lambda$-MnO$_2$/graphene model containing lithium is shown in Fig. S2c (ESI$\dagger$).

In this case, the CASTEP modules included in Materials Studio 8.0 software package were used. The DFT plane wave pseudopotential method was used to calculate the geometrical structure and electronic structure of the $\lambda$-MnO$_2$/graphene model. Here, the Perdew-Burke-Ernzerhof (PBE) of the generalized gradient approximation (GGA) was adopted.$^{42,54,55}$ The ultrasoft pseudopotential for every atom is used in the calculations,$^{56}$ the energy cut off for plane-wave expansion was 500 eV, the energy tolerance was $2 \times 10^{-5}$ eV per atom, the maximum force tolerance was 0.05 eV Å$^{-1}$, the maximum displacement tolerance was $1 \times 10^{-3}$ Å, the maximum stress was 0.1 GPa, the self-consistent field (SCF) calculation accuracy was set to $2.0 \times 10^{-6}$ eV per atom and the Brillouin zone $k$-point was set to $3 \times 3 \times 3$.$^{35}$ In general, for some systems containing d electrons (transition metals), the DFT calculation method tends to underestimate the band gap value of the material. So, to overcome the error of the DFT calculation method on the band gap, this study adopts the DFT+$U$ method of spin polarization to calculate the band gap of the material, where the $U$ value of Mn in $\lambda$-MnO$_2$ was set as 4.0 eV.$^{57,58}$ The effect of the dipole corrections on the electronic structure of MnO$_2$ can be omitted.$^{59}$

In order to study the diffusion mechanism of ions in $\lambda$-MnO$_2$/graphene, this paper uses complete linear synchronous transit (LST) and quadratic synchronous transit (QST) methods to search the transition state (TS).$^{60}$ Nudged elastic band (NEB) is applied to confirm the TS and to explore the minimum energy path of ion diffusion.$^{42,61,62}$ In order to reduce the calculation cost, the transition metal atom (Mn) was not added as $U$ when the TS search and TS confirmation were calculated. Moreover, for saving computing time, all the atomic positions in the model were fixed except for Li atoms moving during those processes according to the method in ref. 40 and 63.

Conflicts of interest

There are no conflicts to declare.

Acknowledgements

This work was supported by the National Natural Science Foundation of China (21776191, 21706181).

References

1 J. Lee, S.-H. Yu, C. Kim, Y.-E. Sung and J. Yoon, *Phys. Chem. Chem. Phys.*, 2013, **15**, 7690-7695.

2 J. Lee, A. Urban, X. Li, D. Su, G. Hautier and G. Ceder, *Science*, 2014, **343**, 519-522.

3 F. Croce, A. D'Epifanio, J. Hassoun, P. Reale and B. Scrosati, J. Power Sources, 2003, 119, 399-402.

4 H. Park, N. Singhal and E. H. Jho, Water Res., 2015, 87, 320-327.

5 Y. Han, H. Kim and J. Park, Chem. Eng. J., 2012, 210, 482-489.

6 K. Ooi, Y. Makita, A. Sonoda, R. Chitrakar, Y. Tasaki-Handa and T. Nakazato, Chem. Eng. J., 2016, 288, 137-145.

7 M. J. Park, G. M. Nisola, E. L. Vivas, L. A. Limjuco, C. P. Lawagon, J. G. Seo, H. Kim, H. K. Shon and W. J. Chung, J. Membr. Sci., 2016, 510, 141-154.

8 W. H. Chi, H. J. Min, Y. J. Kim, W. K. Son, K. S. Kang, S. L. Chang and T. S. Hwang, Sep. Purif. Technol., 2016, 166, 34-40.

9 L. Tian, M. Wei and H. Mei, Chem. Eng. J., 2010, 156, 134-140.

10 J. Xiao and X. Hao, Prog. Chem., 2010, 22, 2420-2427.

11 X. Du, G. Guan, X. Li, A. D. Jagadale, X. Ma, Z. Wang, X. Hao and A. Abudula, J. Mater. Chem. A, 2016, 4, 13989-13996.

12 M. Remko, P. T. V. Duijnen and R. Broer, RSC Adv., 2013, 3, 9843-9853.

13 P. Deepa, P. Polandaivel and K. Senthilkumar, Comput. Theor. Chem., 2011, 974, 57-65.

14 L. Li, W. Qu, F. Liu, T. Zhao, X. Zhang, R. Chen and F. Wu, Appl. Surf. Sci., 2014, 315, 59-65.

15 W. Yao, H. Zhou and Y. Lu, J. Power Sources, 2013, 241, 359-366.

16 S. Nigar, Z. Zhou, H. Wang and M. Imtiaz, RSC Adv., 2017, 7, 51546-51580.

17 J. Wang, F. Ma and M. Sun, RSC Adv., 2017, 7, 16801-16822.

18 Y. Guo, X. Sun, Y. Liu, W. Wang, H. Qiu and J. Gao, Carbon, 2012, 50, 2513-2523.

19 J. He, Y. Chen, P. Li, F. Fu, J. Liu and Z. Wang, RSC Adv., 2015, 5, 80063-80068.

20 L. Peng, X. Peng, B. Liu, C. Wu, Y. Xie and G. Yu, Nano Lett., 2013, 13, 2151-2157.

21 Y. Cui, Z. Yu, C. Hong, K. Wei and S. Shi, Appl. Surf. Sci., 2018, 433, 1083-1093.

22 J. J. Zhou, W. W. Zhou, C. M. Guan, J. Q. Shen, C. Y. Ouyang and M. S. Lei, Sci. China: Phys., Mech. Astron., 2012, 55, 1376-1382.

23 B. Mortazavi, H. Yang, F. Mohebbi, G. Cuniberti and T. Rabczuk, Appl. Energy, 2017, 202, 323-334.

24 Ş. Özcan, A. GüLer, T. Cetinkaya, M. O. Guler and H. Akbulut, Beilstein J. Nanotechnol., 2017, 8, 1932-1938.

25 Y. Chai, Z. Li, J. Wang, Z. Mo and S. Yang, J. Alloys Compd., 2019, 775, 1206-1212.

26 S. Ding, X. Du, Y. Yang, P. Wang, Z. Zhang, X. Hao, C. Peng and G. Guan, Phys. Chem. Chem. Phys., 2018, 20, 17313-17323.

27 L. Xing, J. Vatamanu, O. Borodin, G. D. Smith and D. Bedrov, J. Phys. Chem. C, 2012, 116, 23871-23881.

28 L. Ling, Y. Cao, Z. Zhao, P. Liu, B. Wang, R. Zhang and D. Li, Comput. Mater. Sci., 2018, 149, 182-190.

29 Z. Shadike, Y. Zhou, L. Chen, Q. Wu, J. Yue, N. Zhang, X. Yang, L. Gu, X. Liu and S. Shi, Nat. Commun., 2017, 8, 566.

30 S. Shi, H. Zhang, X. Ke, C. Ouyang, M. Lei and L. Chen, Phys. Lett. A, 2009, 373, 4096-4100.

31 S. Shi, J. Gao, Y. Liu, Y. Zhao, Q. Wu, W. Ju, C. Ouyang and R. Xiao, Chin. Phys. B, 2016, 25, 018212.

32 O. Rahaman, B. Mortazavi and T. Rabczuk, J. Power Sources, 2016, 307, 657-664.

33 X. Wang, P. Hu, L. Chen, Y. Yao, Q. Kong, G. Cui, S. Shi and L. Chen, J. Mater. Chem. A, 2017, 5, 3839-3847.

34 P. Zhang, Y. Zheng, S. Yu, S. Q. Wu, Y. H. Wen, Z. Z. Zhu and Y. Yang, Electrochim. Acta, 2013, 111, 172-178.

35 F. Ning, B. Xu, J. Shi, H. Su, M. Wu, G. Liu and C. Ouyang, J. Phys. Chem. A, 2017, 5, 9618-9626.

36 H. Wang, N. Zhao, C. Shi, L. Ma, F. He, C. He, J. Li and E. Liu, Electrochim. Acta, 2017, 247, 1030-1037.

37 B. G. Choi, M. Yang, S. C. Jung, K. G. Lee, J.-G. Kim, H. Park, T. J. Park, S. B. Lee, Y.-K. Han and Y. S. Huh, ACS Nano, 2013, 7, 2453-2460.

38 H.-J. Yan, Z.-Q. Wang, B. Xu and C. Ouyang, Funct. Mater. Lett., 2012, 5, 1250037.

39 X. Fan, W. T. Zheng and J. L. Kuo, ACS Appl. Mater. Interfaces, 2012, 4, 2432-2438.

40 J. Zheng, Z. Ren, G. Ping, F. Li and J. Fan, Appl. Surf. Sci., 2011, 258, 1651-1655.

41 T. R. Juran, J. Young and M. Smeu, J. Phys. Chem. C, 2018, 122, 8788-8795.

42 R. Xiao, J. Xie, T. Luo, L. Huang, Y. Zhou, D. Yu, C. Chen and Y. Liu, J. Phys. Chem. C, 2018, 122, 1513-1521.

43 H. R. Naderi, P. Norouzi and M. R. Ganjali, Appl. Surf. Sci., 2016, 366, 552-560.

44 M. Bin, Z. Wenbo, S. Shijun and W. Aiqin, Phys. Chem. Chem. Phys., 2014, 16, 7872-7880.

45 Z. Chen, J. Li, Y. Chen, Y. Zhang, G. Xu, J. Yang and Y. Feng, Particuology, 2014, 15, 27-33.

46 X. Wang and Y. Li, J. Am. Chem. Soc., 2002, 124, 2880-2881.

47 D. K. Kim, P. Muralidharan, H. W. Lee, R. Ruffo, Y. Yang, C. K. Chan, H. Peng, R. A. Huggins and Y. Cui, Nano Lett., 2008, 8, 3948-3952.

48 F. Gao, X. Du, X. Hao, S. Li, X. An, M. Liu, N. Han, T. Wang and G. Guan, Chem. Eng. J., 2017, 328, 293-303.

49 N. Leifer, F. Schipper, E. M. Erickson, C. Ghanty, M. Talianker, J. Grinblat, C. M. Julien, B. Markovsky and D. Aurbach, J. Phys. Chem. C, 2017, 121, 9120-9130.

50 A. Togo and I. Tanaka, Scr. Mater., 2015, 108, 1-5.

51 Z. Xu, X. Lv, J. Chen, L. Jiang, Y. Lai and J. Li, Phys. Chem. Chem. Phys., 2017, 19, 7807-7819.

52 R. Zhang, J. Zhao, L. Guo, H. Qin, W. Shi and Z. Lu, RSC Adv., 2017, 7, 29821-29826.

53 H. Tachikawa and H. Kawabata, Thin Solid Films, 2009, 518, 873-876.

54 M. D. Segall, P. J. D. Lindan, M. J. Probert, C. J. Pickard, P. J. Hasnip, S. J. Clark and M. C. Payne, J. Phys.: Condens. Matter, 2002, 14, 2717-2744.

55 J. P. Perdew, K. Burke and M. Ernzerhof, Phys. Rev. Lett., 1996, 77, 3865-3868.

56 D. Vanderbilt, Phys. Rev. B: Condens. Matter Mater. Phys., 1990, 41, 7892-7895.

57 S. P. Ong, V. L. Chevrier, G. Hautier, A. Jain, C. Moore,
S. Kim, X. Ma and G. Ceder, *Energy Environ. Sci.*, 2011, **4**,
3680-3688.

58 G. Li, P. Zhao, H. Zheng, L. Yang, S. Lu and P. Peng,
*J. Hazard. Mater.*, 2018, **354**, 8-16.

59 L. Li, X. Feng, N. Yao, S. Chen, S. Feng, K. Xiong,
D. Wei, X. Qi, J. Hu and Z. Wei, *ACS Catal.*, 2015, **5**,
4825-4832.

60 T. A. Halgren and W. N. Lipscomb, *Chem. Phys. Lett.*, 1977,
**49**, 225-232.

61 G. Henkelman, B. P. Uberuaga and H. Jónsson, *J. Chem.
Phys.*, 2000, **113**, 9901-9904.

62 G. Henkelman and H. Jónsson, *J. Chem. Phys.*, 2000, **113**,
9978-9985.

63 O. Leenaerts, B. Partoens and F. M. Peeters, *Appl. Phys. Lett.*,
2008, **93**, 193107.