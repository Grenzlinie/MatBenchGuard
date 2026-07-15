# A Solid-State Electrolyte Based on $Li_{0.95}Na_{0.05}FePO_4$ for Lithium Metal Batteries

Bohao Peng, Zaichun Liu, Qi Zhou, Xiaosong Xiong, Shuang Xia, Xuelong Yuan, Faxing Wang, Kenneth I. Ozoemena, Lili Liu, Lijun Fu, and Yuping Wu*

Solid-state electrolytes (SSEs) play a crucial role in developing lithium metal batteries (LMBs) with high safety and energy density. Exploring SSEs with excellent comprehensive performance is the key to achieving the practical application of LMBs. In this work, the great potential of $Li_{0.95}Na_{0.05}FePO_4$ (LNFP) as an ideal SSE due to its enhanced ionic conductivity and reliable stability in contact with lithium metal anode is demonstrated. Moreover, LNFP-based composite solid electrolytes (CSEs) are prepared to further improve electronic insulation and interface stability. The CSE containing 50 wt% of LNFP (LNFP50) shows high ionic conductivity (3.58 × 10⁻⁴ S cm⁻¹ at 25 °C) and good compatibility with Li metal anode and cathodes. Surprisingly, the LMB of Li|LNFP50|LiFePO₄ cell at 0.5 C current density shows good cycling stability (151.5 mAh g⁻¹ for 500 cycles, 96.5% capacity retention, and 99.3% Coulombic efficiency), and high-energy LMB of Li|LNFP50|Li[Ni₀.₈Co₀.₁Mn₀.₁]O₂ cell maintains 80% capacity retention after 170 cycles, which are better than that with traditional liquid electrolytes (LEs). This investigation offers a new approach to commercializing SSEs with excellent comprehensive performance for high-performance LMBs.

## 1. Introduction

The development and efficient utilization of renewable energy is one of the important ways to solve the current energy crisis and environmental problems, which calls for high-performance energy storage technology. $^{[1]}$ The widely used lithium-ion battery (LIBs) is considered as an effective energy storage technology, but its energy density has been approaching its limit and needs to be further improved. $^{[2,3]}$ Lithium metal batteries (LMBs) are considered as the most promising next generation of high energy density energy storage devices due to the low potential (-3.04 V) and high theoretical specific capacity (3860 mAh g⁻¹) of lithium (Li) metal anode. $^{[4]}$ However, the safety issues caused by the ultra-high chemical reactivity and the uneven deposition of Li metal anodes limit the commercialization of LMBs. $^{[5,6]}$ Solid-state lithium metal batteries (SSLMBs) paired with high-capacity cathodes (like Ni-rich layered oxides) and high-performance solid-state electrolytes (SSEs) may meet the requirements of both outstanding safety and high energy density. $^{[7]}$

High ionic conductivity is one of the most important characteristic indicators of high-performance SSEs. Typically, NASICON-Type SSEs (such as $Li_{1.3}Al_{0.3}Ti_{1.7}(PO_4)_3^{[8]}$) and sulfide SSEs (such as $Li_{10}GeP_2S_{12}^{[9]}$) have achieved ionic conductivity that matches or even surpasses that of organic liquid electrolytes (LEs). However, their practical application in SSLMBs is limited by the interface issues in contact with Li anode or cathodes. $^{[10]}$ For example, the incompatibility of NASICON-Type SSEs with Li metal arises due to the reduction of $Ti^{4+}$ by Li metal. $^{[11]}$ The low electrochemical window of most sulfide SSEs makes them thermodynamically unstable to match with Li metal anode. $^{[12]}$ Moreover, direct contact between sulfide SSEs and the oxide cathodes creates a space charge layer at the interface, causing a lack of compatibility between them. $^{[13]}$ Generally, high-performance SSEs should have not only high ionic conductivity characteristics but also excellent interface stability with Li anode and cathodes. Toward this end, composite solid electrolytes (CSEs) that combine polymer and inorganic SSEs are an effective solution for addressing interface issues between SSEs and electrodes. $^{[14]}$

$LiFePO_4$ (LFP) is generally used as the cathode for LIBs after conductive carbon coating due to its stable structure and low price. $^{[15]}$ Pure LFP is basically an insulator because of its low intrinsic electronic conductivity ($10^{-9}$ S cm⁻¹) (Figure S1a, Supporting Information), $^{[16]}$ which makes it possible for LFP to be used as SSE. Since the lithium-ion chemical diffusion coefficient of LFP is very low ($10^{-10}$-$10^{-15}$ cm² s⁻¹),$^{[17,18]}$ it is necessary to

---

B. Peng, Q. Zhou, S. Xia, X. Yuan, L. Liu, L. Fu, Y. Wu
School of Energy Science and Engineering
Nanjing Tech University
Nanjing, Jiangsu Province 211816, P. R. China
E-mail: wuyp@seu.edu.cn

Z. Liu, X. Xiong, F. Wang, Y. Wu
Confucius Energy Storage Lab
School of Energy and Environment
Southeast University
Nanjing 210096, P. R. China

K. I. Ozoemena
Molecular Sciences Institute
School of Chemistry
University of the Witwatersrand
Private Bag 3, Wits, Johannesburg 2050, South Africa

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adma.202307142

DOI: 10.1002/adma.202307142

![](./images/913614756068196459_1.jpg)

Figure 1. Theoretical calculations of LNFP. a) Optimized structure of LNFP. b) Li-ions transport channels in LNFP. c) Li-ions transport energy barriers in LFP and LNFP.

improve the ionic conductivity of LFP as a solid electrolyte. Research efforts have proved that as a cathode for LIBs, the ionic conductivity of LFP can be improved through strategies such as introducing elements of Na, Mg, or Zr and Co.[¹⁶] However, LFP has not yet been developed as an SSE or filler.

In this work, we found that doping Na⁺ in LFP can promote its Li⁺ diffusion confirmed by experiments and theoretical calculations, and for the first time, Li₀.₉₅Na₀.₀₅FePO₄ (LNFP) was discovered as SSE, which demonstrates good stability in contact with Li metal anode. We further prepared a flexible LNFP-based CSE with excellent interface compatibility by a simple preparation method. The LNFP on the surface of the CSE acts as a mixed ionic/electronic conductive layer and thus greatly improves the interface compatibility between the cathode and SSEs. The addition of poly(vinylidene fluoride) (PVDF) increased flexibility, improved interface physical contact, and further reduced electronic conductance. A high-energy all-solid-state lithium metal battery was assembled using the LNFP-based CSE and LFP or nickel-rich Li[Ni₀.₈Co₀.₁Mn₀.₁]O₂ (NCM811) cathodes, exhibiting excellent electrochemical properties comparable to those in LEs. The results demonstrate that the CSEs with optimal ratio possess high ionic conductivity and good interfacial compatibility with both anode and cathodes in either chemistry or physics, and SSLMBs with CSEs exhibit excellent long-term cycling stability.

## 2. Results and Discussion

### 2.1. Nature of $\boldsymbol{\mathrm{Li_{1-x}Na_{x}FePO_{4}}}$ ($\boldsymbol{x=0, 0.025, 0.05, 0.1}$)

First-principal calculations were performed to evaluate the ionic conductivity enhancement of Na-doped LFP. The calculated results indicate that Na occupies the 4a site of the original Li after doping (Figure 1a). The introduction of a small amount of Na will not block the ion transport channels in LFP due to the three-dimensional transport characteristics of Li-ions within it (Figure 1b). Most importantly, the nudged elastic band (NEB) calculations were carried out to investigate the changes in the migration behavior of Li-ions in LFP after Na doping as illustrated in Figure 1c. And it was found that the migration energy barrier of Li-ions near Na-occupied sites significantly decreases (0.38 eV) compared to that in the original LFP (0.68 eV). This proves that the introduction of Na can greatly increase the migration rate of Li-ions in LFP, making the LNFP potentially suitable as a high-performance SSE.

To prove the enhancements of the ionic conductivity, $\mathrm{Li_{1-x}Na_{x}FePO_{4}}$ was prepared by the solid-phase method.[¹⁹] The X-ray diffraction (XRD) pattern (Figure 2a) and the refined XRD image (Figure S2, Supporting Information) indicate that the main characteristic diffraction peaks of $\mathrm{Li_{1-x}Na_{x}FePO_{4}}$ match the characteristic peaks of the standard spectrum (JCPDS card PDF#81-1173), which is consistent with the typical olivine structure of LFP with no other impurities detected.[²⁰] This suggests that the doping of a small amount of Na⁺ into LFP does not alter the olivine structure. Additionally, the XRD local magnification (Figure 2b) shows a slight shift in the diffraction peak towards a smaller angle. Since the larger radius (1.02 Å) of Na⁺ compared to the Li⁺ (0.76 Å), the lattice constant of $\mathrm{Li_{1-x}Na_{x}FePO_{4}}$ increases gradually with an increase of Na⁺ content (Table S1, Supporting Information).[¹⁹] Moreover, the prepared materials were further analyzed using infrared spectroscopy. The attenuated total reflection-fourier transform infrared (ATR-FTIR) spectroscopy absorption of $\mathrm{Li_{1-x}Na_{x}FePO_{4}}$ is mainly distributed in two bands (1139–971 cm⁻¹ and 635–468 cm⁻¹) (Figure 2c). Table S2 (Supporting Information) summarizes the vibration modes corresponding to each infrared absorption peak.[²¹] The positions of the peaks in the infrared spectra are completely consistent, and no other miscellaneous peaks are found, indicating that the ideal products were synthesized and Na⁺ doping does not affect the structure of the infrared spectra. Moreover, the scanning electron microscope (SEM) and energy dispersive spectrometer (EDS) results confirmed the successful introduction of Na element as shown in Figure 2d. It can be seen that the particle sizes of LNFP are in the micron scale, and the Na and other elements are highly evenly distributed.

To explore the effect of Na⁺ doping on ionic conductivity, the electrochemical impedance spectroscopy (EIS) test of

![](./images/913614756068196459_2.jpg)

Figure 2. Physical and Electrochemical characterization of $Li_{1-x}Na_xFePO_4$. a) XRD patterns. b) Locally enlarged image of XRD. c) ATR-FTIR spectra. d) SEM image and EDX mapping of elements: oxygen (O), iron (Fe), sodium (Na), phosphorus (P). e) Nyquist impedance plot at room temperature. f) Galvanostatic cycling performance of symmetric cell.

$Li_{1-x}Na_xFePO_4$ pellets was performed at room temperature (Figure 2e). The results indicate the ionic conductivity of $Li_{1-x}Na_xFePO_4$ increases first and then decreases as the $Na^+$ doping amount increases (Table S1, Supporting Information). This is because when a small amount of $Na^+$ is doped in the 4a site, Li-ions transport channels near the Na-occupied sites in the $Li_{1-x}Na_xFePO_4$ have been expanded, which is consistent with the theoretical calculation results (Figure 1) and will be beneficial for the transport of $Li^+$. However, when the doping amount increases, excessive $Na^+$ occupying 4a sites will block the three-dimensional Li-ions transport channels in LFP, hindering the transport of Li-ions and resulting in a decrease in ionic conductivity. Therefore, appropriate Na doping is the key to improving the ionic conductivity of LFP, and our results indicate LNFP exhibits the highest ionic conductivity at room temperature $(8.78 × 10^{-4}\ S\ cm^{-1})$ and the lowest activation energy $(E_a = 0.119\ eV)$ (Figure S3, Supporting Information), so it is used for subsequent tests. Furthermore, Li||Li symmetric battery with LNFP exhibits good cycling stability as illustrated in Figure 2f, proving that LNFP has good compatibility with Li metal anode and shows great potential as SSE for LMBs.

### 2.2. Characterization of the CSEs
Although the synthesized LNFP shows good compatibility with Li metal anode and small electronic conductivity $(10^{-8}\ S\ cm^{-1})$ (Figure S1a, Supporting Information), when in direct contact with the cathodes, the conductive additive (such as: Super P) in the cathodes increases its electronic conductivity and causes an oxidation reaction in the LNFP at a certain voltage, resulting in the loss of lithium ions and the generation of $Na_{0.05}FePO_4$ (NFP). This will lead to overcharging of the battery and ultimate failure. Therefore, CSEs were prepared by combining LNFP with typical polymer electrolyte PVDF to further reduce electronic conductivity and interface impedance. Due to thermal and chemical stability, mechanical properties, good toughness, and good dielectric constant $(\approx8.4)$, PVDF is considered an ideal polymer

![](./images/913614756068196459_3.jpg)

Figure 3. Physical and Electrochemical characterization of LNFP-based CSEs. a) Preparation process of CSEs. b) SEM images of CSEs at the surface. c) XRD patterns of CSEs. d) Arrhenius plots of ionic conductivity. e) Linear sweep voltammetry plots. f) Chronoamperometry curves of Li|LNFPPx|Li at 10 mV s⁻¹.

matrix for the preparation of CSEs which has been widely used.[22-24]

The CSEs can be denoted as LNFPx ($x$ wt% represents the mass ratio of LNFP to the total CSEs). LNFP x were prepared by the typical casting method as illustrated in Figure 3a. First, the addition of PVDF decreases the overall electronic conductivity of CSEs ($<10^{-9}$ S cm⁻¹) (Figure S1b, Supporting Information). The SEM images of different CSEs are shown in Figure 3b. It can be observed that when inorganic particles are less filled, CSEs are essentially a polymer. LNFP particles are uniformly dispersed in the PVDF matrix without obvious agglomeration (LNFP30). However, excessive inorganic particles will agglomerate and cause the formation of a large number of holes, which makes the transport path of Li-ions discontinuous, hindering the migration of Li-ions (LNFP70). In addition, cross-sectional SEM and element mapping analysis show that LNFP particles are evenly dispersed in the CSE, and the element distribution is uniform, which proves that the whole electrolyte is uniform (Figure S4, Supporting Information). Moreover, with the increase in the proportion of LNFP fillers, the XRD peaks of PVDF decreased gradually (Figure 3c). The lower intensity of the characteristic peaks of PVDF indicates that LNFP significantly reduces the crystallinity of the PVDF matrix.

EIS test of different CSEs (Figure S5, Supporting Information) and Arrhenius plots of ionic conductivity (Figure 3d) were used to assess Li-ions transport ability in CSEs. With the increase of LNFP fillers in CSEs, the ionic conductivity first increases and then decreases. When m(LNFP): m(PVDF) = 1: 1, the CSE of LNFP50 exhibits the highest ionic conductivity ($3.58 \times 10^{-4}$ S cm⁻¹ at $25\ ^{\circ}\text{C}$) and the lowest activation energy ($E_{\text{a}} = 0.207$ eV). The initial increase of ionic conductivity proves the key role of LNFP in promoting Li⁺ conduction of CSEs. The latter decrease is due to that excess LNFP ($\geq$60 wt%) starts to aggregate, causing ceramic/polymer phase separation and ultimately leading to the formation of pores as clearly shown in Figure 3b, which is detrimental to Li-ions conduction.[25]

To better demonstrate the role of LNFP in improving ionic conductivity, other materials such as LFP, TiO₂, and MgO were used as fillers for comparison (Figure S6, Supporting Information). Compared with other fillers, LNFP exhibits the most significant effect on ionic conductivity of CSEs (Table S3, Supporting Information). We attribute it to the significant improvement in the

<table><thead><tr><th>Sample</th><th>σ at 25 °C [S cm⁻¹]</th><td>Ea [eV]</td><td>tLi+</td><td>Oxidation potential (V)</td></tr></thead><tbody><tr><td>LNFP30</td><td>1.54 × 10⁻⁴</td><td>0.303</td><td>0.26</td><td>5.1</td></tr><tr><td>LNFP40</td><td>1.94 × 10⁻⁴</td><td>0.212</td><td>0.37</td><td>5.1</td></tr><tr><td>LNFP50</td><td>3.58 × 10⁻⁴</td><td>0.207</td><td>0.41</td><td>5.1</td></tr><tr><td>LNFP60</td><td>1.49 × 10⁻⁴</td><td>0.271</td><td>0.67</td><td>4.1</td></tr><tr><td>LNFP70</td><td>8.71 × 10⁻⁵</td><td>0.276</td><td>0.84</td><td>4.0</td></tr></tbody></table>

intrinsic ionic conductivity of Li-ions in LNFP after the introduction of Na element (8.78 × 10⁻⁴ S cm⁻¹). Therefore, filling with LNFP has a more significant conductivity enhancement effect compared to other inorganic fillers (LFP, TiO₂, and MgO). LNFP provides additional Li⁺ and allows for rapid Li⁺ transport through the construction of fast Li-ions transport channels after Na doping, which increases the pathways for Li⁺ conduction in CSEs.[26,27] Besides, the addition of LNFP resulted in low crystallinity of PVDF in CSEs, which is conducive to ionic transport in the CSEs with reduced interface impedance.[28,29]

Linear sweep voltammetry (LSV) was used to further evaluate the electrochemical stability window of CSEs. As illustrated in Figure 3e, LNFP60 and LNFP70 show an obvious current at 4.0 and 4.1 V, which were caused by the oxidation reaction of excessive LNFP fillers under high voltage. When m(LNFP): m(PVDF) = 1: 1, the decomposition potential is ≈5.1 V. The results present that the electrochemical window of LNFP50 is sufficient to meet the requirements of active cathodes even with high voltage in LMBs. The Li⁺ transfer number (tLi+) was measured by the chronoamperometry method (Figure 2d), and impedance plots before and after the Li⁺ transfer number test are shown in Figure S7 (Supporting Information). Results demonstrate that tLi+ of CSEs increases with the amount of LNFP. This is because CSE tends to be a single ionic conductor with the increase of LNFP,[30] Notably, the highest tLi+ of 0.84 is achieved for LNFP70, which depends on the LNFP content. The thermal stability of CSEs was further evaluated by thermogravimetry analysis (TGA) testing (Figure S8, Supporting Information). The CSEs begin to lose weight at 450 °C, and the thermal decomposition temperature becomes higher with the increase of LNFP. LNFP can improve the thermal stability of CSEs due to its high preparation temperature of 700 °C.

As summarized in Table 1, LNFP50 exhibited great potential as a high-performance CSE due to its excellent comprehensive performance, such as the highest ionic conductivity (3.58 × 10⁻⁴ S cm⁻¹), the lowest Eₐ (0.207 eV), an appropriate Li⁺ transfer number (0.41), and a high enough oxidative decomposition potential (5.1 V). Therefore, LNFP50 was assembled into various solid-state batteries for further evaluation of its related properties.

### 2.3. Stability of LNFP50 in Contact Li Metal Anode

The Li||Li symmetric cells were assembled to further evaluate the stability of LNFP50 for Li metal anode. As the current density increased (Figure 4a), the voltage hysteresis of the symmetrical cells also increased in a regular manner. Moreover, LNFP50 showed an ordered profile until the specific current density reached 5.2 mA cm⁻². In contrast, the voltage profile of Li||Li symmetric cells paired with commercial polypropylene (PP) film and LEs exhibited sudden drops under a lower critical current of 4.1 mA cm⁻². Higher critical current density suggests that LNFP50 effectively inhibits the generation of Li dendrites during rapid deposition/stripping.[31]

The Li||Li symmetric cell with LNFP50 exhibits excellent cycling stability and successfully stabilizes cycling for over 900 hours (h) (Figure 4b) with a low overpotential of ≈40 mV (Figure S9, Supporting Information). On the contrary, Li||Li symmetric cell with PP film can only cycle stably for <400 h, followed by severe voltage fluctuations and large polarization voltage. This indicates that the uneven lithium deposition/stripping makes the dendrites easily grow and pierce the PP separator or fall down leading to dead lithium in the LEs system. In contrast, the lithium deposition/stripping can proceed stably and reversibly using LNFP50 CSE. The excellent Li metal protection performance demonstrated by LNFP50 CSE is mainly due to the enhanced ionic conductivity and mechanical strength of CSE after filled with LNFP, which helps to suppress Li dendrites. Moreover, the excellent flexibility of PVDF allows CSE to adapt to volume changes and ensures its close contact with Li metal anode during the lithium deposition/stripping progress.[32]

To further evaluate the compatibility of LNFP50 to lithium metal anode, the Li|LNFP50|Cu asymmetric cells were assembled to investigate the electrochemical performance and physical morphology of lithium deposition/stripping. As illustrated in Figure S10 (Supporting Information), Li|LNFP50|Cu asymmetric cell shows a lithium deposition overpotentials close to LEs system of ≈40 mV. Furthermore, the Li|LNFP50|Cu asymmetric cells can maintain long-term cycling stability for up to 1400 cycles with high stable Coulombic efficiency (CE) of ≈99.2%, which is almost seven times than the cycling stability of Li|PP|Cu asymmetric cells (Figure 4c). This indicates that combining with LNFP50 CES can achieve more stable lithium deposition/stripping performance. Li||Cu cell at 1 mA cm⁻² and 1 mAh cm⁻² can still operate stably with a high coulomb efficiency (99.0%), and its performance does not suffer significant attenuation, which indicates that LNFP50 allows lithium ions to migrate rapidly at high current densities (Figure S11, Supporting Information). In addition, we found a uniform and compact lithium is formed on the copper surface after lithium deposition in Li|LNFP50|Cu asymmetric cells as detected in Figure 4d, e. In contrast, there is a distinct porous lithium on the copper surface in Li|PP|Cu cells, which can usually lead to the formation of lithium dendrites and ultimately leads to battery failure (Figure S12, Supporting Information).[33] Therefore, compared to PP or previous reports (Table S4, Supporting Information), our LNFP50 SSE exhibits enormous potential for application in LMBs due to its advantages of remarkable cycling stability and excellent lithium deposition/stripping performance in contact with Li metal anode.

### 2.4. SLMBs Performances

To demonstrate the feasibility of LNFP50 in practical applications, SLMBs were assembled with Li as anode, LNFP50 as

![](./images/913614756068196459_4.jpg)

Figure 4. Electrochemical characterizations on Li||LNFP50 interface. a) Critical current density test of LNFP50 or PP. b) Galvanostatic cycling performance of Li|| Li cells with LNFP50 or PP at 0.5 mA cm⁻² and 0.5 mAh cm⁻². c) Long-term cycling stability Li deposition/stripping in Li|| Cu cells with LNFP50 or PP at 0.5 mA cm⁻² with a fixed Li deposition of 0.5 mAh cm⁻². d) Top view and e) Section view of deposited Li of Li||Cu cells with LNFP50 at 0.5 mA cm⁻² and 2.0 mAh cm⁻².

electrolyte, and LFP as cathode. As illustrated in Figure 5a, Li|LNFP50|LFP cell exhibits long cycling stability with stable CE of ≈99.3%. After 500 cycles, the capacity of Li|LNFP50|LFP cell was maintained at 151.5 mAh g⁻¹ with a capacity retention rate of 96.5%. While the Li|PP|LFP cell experienced unstable CE and significant capacity degradation with only 68% capacity retention after 300 cycles, which is mainly due to the consumption of LEs and the generation of dead lithium, ultimately leading to the growth of dendrites.[³⁴] The excellent long cycling of Li|LNFP50|LFP cell further proved the good interface compatibility of LNFP50 CSE with Li anode and LFP cathode, promoting uniform Li deposition/stripping and inhibiting Li dendrites growth. The voltage profiles of the Li|LNFP50|LFP cell suggest stable charge and discharge with flat voltage plateaus and low overpotential as presented in Figure 5b, indicating the favorable electrochemical performance and interface compatibility of LNFP50 CSE. In contrast, a larger overpotential was detected by using the PP film (Figure S13, Supporting Information). Additionally, the high ionic conductivity of LNFP50 CSE enables the SSLMBs to exhibit good rate performance. As shown in Figure 5c, the specific discharge capacities of Li|LNFP50|LFP are 161.1, 160.9, 148.7, 132.9, and 158.4 mAh g⁻¹ at 0.5, 1, 3, 5, and 1 C, respectively. And the overpotential increases slowly with the increase of current (Figure 5d). This makes it possible for LNFP50 CSE to meet fast charging requirements in the future.

Moreover, SSLMBs with high voltage nickel-rich NCM811 cathode were further evaluated. Considering the wide electrochemical window of the LNFP50, Li|LNFP50|NCM811 cells were

![](./images/913614756068196459_5.jpg)

Figure 5. Electrochemical performance of SSLMBs at $35\ ^{\circ}\text{C}$. a) cycling performance of Li||LFP at 0.5 C. b) potential profiles at specific cycles of Li||LFP. c) rate capabilities of Li||LFP. d) potential profiles at different rates of Li||LFP. e) cycling performance of Li||NCM811 at 1 C. f) potential profiles at specific cycles of Li||NCM811. g) rate capabilities of Li||NCM811. h) potential profiles at different rates of Li||NCM811.

able to be tested from 2.8 to 4.3 V at $35\ ^{\circ}\text{C}$. The initial discharge capacity of Li|LNFP50| NCM811 is $195.6\ \text{mAh g}^{-1}$ at 0.2 C. The SSLMB using LNFP50 exhibits better cycling stability with capacity retention of 80% after 170 cycles compared to that with PP (Figure 5e), which is due to the wide electrochemical window of LNFP50 and interface compatibility with electrodes. As demonstrated in Figure 5f, like general SSEs, LNFP50 also shows an increase in interface impedance after cycling. This is because the volume of the electrode changes during cycling, $^{[35,36]}$ leading to an increase of interface impedance. The Li|LNFP50|NCM811 cell also shows good rate capability due to the high ionic conductivity of LNFP50 (Figure 5g). The overpotential increases slightly with the increase of current densities (Figure 5h). Therefore, LNFP50 can work normally and stably in high-voltage nickel-rich system because of its wide electrochemical window, interface compatibility, and flexibility of LNFP50, indicating its great potential for more applications in LMBs.

It is widely acknowledged that an interlayer with mixed ionic/electronic conductivity can significantly enhance the interface and lead to uniform deposition of lithium. $^{[37-40]}$ LNFP

![](./images/913614756068196459_6.jpg)
![](./images/913614756068196459_7.jpg)

**Figure 6.** Working principle of LNFP50 CSE. a) Ideal model of LNFP50 CSE and schematics to illustrate ionic/electronic conductive layer. b) XRD and c) ATR-FTIR spectra comparison of primary LNFP50 and LNFP50 after charging.

on the CSE surface in contact with cathodes may act as an ionic/electronic conductive layer, as shown in **Figure 6a**. In the ionic/electronic conductive layer, LNFP can become NFP by losing electron and $Li^{+}$ (from $Fe^{2+}$ to $Fe^{3+}$) at a certain voltage (theoretical value $\approx 3.5$ V). In the ionic conductive layer, this phenomenon does not happen, which is because LNFP is enclosed by PVDF to isolate electrons, and LNFP is only involved in the transport of $Li^{+}$. To further verify the rationality of the hypothesis, XRD and ATR-FTIR for LNFP50 disassembled from Li||LNFP50|NCM811 cells (charged from open circuit potential to 4.3 V) were tested to verify the LNFP state at the surface in contact with the cathode and the inner. Since a small amount of $Na^{+}$ doping does not affect the XRD and IR spectrum, the different characteristic peaks of LFP and FP can also be used to discriminate between LNFP and NFP. $^{[21]}$ The typical P-O asymmetric stretching vibration $(1051\ \text{cm}^{-1})$ and P-O symmetric stretching vibration $(971\ \text{cm}^{-1})$ of LNFP disappear after charging, and the stretching mode of $PO_{4}^{3-}$ of NFP appears $(995\ \text{cm}^{-1})$. XRD and ATR-FTIR tests show that LNFP on the surface and only the surface can lose both electrons and lithium ions to generate NFP, and the internal LNFP is not oxidized due to the inaccessibility of electrons. And the change of LNFP in the ionic/electronic conductive layer is highly reversible because NFP was not found after the complete charge-discharge cycle from ATR-FTIR spectra (Figure S14, Supporting Information). The above experiments demonstrate that the surface LNFP of LNFP50 CSE has electronic conductivity after contact with the conductive additive of the cathode. The surface LNFP on the cathode side can conduct electrons and ions at the same time, so it acts as a mixed ionic/electronic conductive layer that makes the cathode interface stable and results in good rate performance and stability of the battery. $^{[43]}$ The Tafel plot was utilized to verify the electrode interface kinetics (Figure S15, Supporting Information). $^{[38,39]}$ Compared with PP, LNFP50 has a slightly higher current density $(i_{0}\approx12\ \mu\text{A}\ \text{cm}^{-2})$, which indicates that $Li^{+}$ can transfer faster from the electrolyte/electrode interface, reflecting the enhancement of Li deposition/stripping kinetics. There are three ionic transport paths in the CSE: the segmented movement of ions along the polymer electrolyte, ionic hopping within inorganic particles, and ionic transfer across the interfaces between the inorganic particle and polymer. $^{[44]}$ With the increase in the content of the ionic conductor, the ion transport path would gradually transit from the polymer phase to the inorganic phase. $^{[45]}$ In LNFP50, the ion transport of LNFP is faster, so the ion transport mainly occurs in LNFP particles, and the ion transport for the isolated LNFP particles is through the interfaces between the filler and polymer electrolyte as illustrated in Figure 6a. $^{[46]}$

Overall, the excellent cycling performance of Li||LFP and Li||NCM811 LMBs can be attributed to excellent interface compatibility and flexibility, and the good rate performance due to the high ionic conductivity of CSEs. LNFP50 exhibits sufficiently high ionic conductivity and good electrochemical stability for the anode as well as good physical contact stability. Moreover, the mixed ionic/electronic conductive layer on the surface of LNFP50 in contact with cathodes achieves good electrochemical stability for cathodes, enabling its long-term stable application in LMBs.

### 3. Conclusion
In summary, we investigated the effect of $Na^{+}$ doping on LFP to prepare a high-performance SSE combined with first-principal calculations and experiments. The ionic conductivity $(8.78\times10^{-4}$

$S$ cm⁻¹ at 25 °C) is found to be the highest as the Na doping content is increased to 0.05, which shows good compatibility with Li metal anode. Then we investigated the electrochemical behavior of LNFP-based CSEs incorporating with PVDF, and achieved the optimal proportion of 50 wt% with stable performance. LNFP50 exhibits the highest ionic conductivity $(3.58 × 10^{-4}$ S cm⁻¹ at 25 °C), the lowest $E_{a}$ (0.207 eV), and wide electrochemical window ($\approx$5.1 V) as well as flexibility. LNFP50 CSE achieves excellent interfacial stability with lithium metal and cathodes, which exhibits the good and long cycling performance in Li||Li, Li||Li, Li||Cu, Li|LNFP50|LFP, and high voltage Li|LNFP50|NCM811 batteries. Undoubtedly, this work expands the options of solid electrolytes and opens a new way to develop high-performance CSE in SSLMBs.

## 4. Experimental Section
Preparation of LNFP particle: LNFP was synthesized by solid-state synthesis. $FeC_{2}O_{4}\cdot 2H_{2}O$ (99% purity, Sinopharm), $NH_{4}H_{2}PO_{4}$ (99% purity, Macklin), $Na_{2}CO_{3}$ (AR, Sinopharm), and $Li_{2}CO_{3}$ (AR, Sinopharm) were placed in an agate bowl according to their stoichiometric ratio. The mixture was ball milled at 400 rpm for 10 h (Bench-Top Planetary Automatic Ball Mills, MSK-SFM-1). The mixture was subsequently subjected to heating at 350 °C for 5 h, followed by a temperature increase to 700 °C for an additional 10 h, and all carried out under an argon atmosphere. Finally, LNFP powders were obtained by ball-milling the heated product.

Preparation of CSEs: First, LNFP and PVDF (Arkema Fluorochemical Co. Ltd., Kynar HSV900, $Mw \approx 100000$) were added to Dimethylacetamide (DMAc, AR, Sinopharm) in different proportions. The mixed solution was mechanically stirred for 6 h, and then the casting solution was applied to a clean glass plate and dried to obtain CSEs. The thickness of the CSEs is $\approx$30 $\mu$m.

Preparation of LFP/NCM811 Electrode: LFP/NCM811 (80 wt%), PVDF (10 wt%), and Super P (10 wt%) were mixed in N-methyl-2-pyrrolidone (NMP), and the slurry was evenly applied to the aluminum foil. The electrode was cut into slices after drying in an 80 °C vacuum oven. The mass loading of the cathode active material in the full cell is $\approx$1.5 mg cm⁻².

Material Characterization: Structure and morphology were performed by X-ray diffraction (Rigaku, Cu $K\alpha$ radiation, 2 Theta range = 10–90°) and Philips XL-70 scanning electron microscope. ATR-FTIR spectra were recorded on a UV-vis spectrophotometer (UV-2600, Bruker). Thermal stability analysis was performed using a synchronous thermal analyzer (NET-ZSCH, STA 449 F1, Heating rate = 10 °C min⁻¹, range = 25–700 °C).

Electrochemical Measurement: The ionic conductivity of SSEs was measured by Solartron Analytical 1287A electrochemical workstation (temperature range = 25–105 °C, frequency range = 0.1–10⁵ Hz). Stainless steel (SS)|SSEs|SS batteries were assembled for testing. Pure LNFP powder was formed into a pellet with a diameter of 15 mm and a density of 2.3 g cm⁻³. A drop of conventional nonaqueous carbonate electrolyte (LB315, 10 $\mu$L) was added to offset the poor solid-solid contact. The $\sigma$ and $E_{a}$ were obtained from the following equation:

$$
\sigma=\frac{L}{R S}=Aexp\frac{-E_{a}}{K_{B}T} \tag{1}
$$

Here $L$ is the electrolyte thickness, $R$ is the bulk resistance, $S$ is the contact area of the SSE and electrode, $K_{B}$ is the Boltzmann constant, $A$ is the pre-exponential factor, and $T$ is the temperature.

The SS|SSEs|SS symmetrical batteries were prepared, and the electronic conductivity of SSEs was obtained by applying 0.5 V polarization voltage by the chronoamperometry. Electrochemical stability was tested by LSV on Li|SSEs|SS cell (range = 2–6 V, scan rate = 1 mV s⁻¹). The 10 mV step potential was applied to Li|SSEs|Li for 1000 s to obtain the initial current and steady current, and then $t_{Li+}$ was obtained through calculation. Li||Li symmetric cells and Li||Cu asymmetric cells were utilized in a LAND test system to explore lithium deposition/stripping behavior.

The electrochemical performance of CSEs was evaluated through galvanostatic charging-discharging with the structure of Li||LFP (or NCM811). The charge-discharge cycling of Li||LFP (or NCM811) cells was conducted at 35 °C from 2.5 V to 4.2 V (or 2.8 V to 4.3 V). The pressure applied to the cells was 50 kg cm⁻². A drop of LB315 (10 $\mu$L, Zhangjiagang Guotai Huarong New Chemical Materials Co., Ltd.) was added to wet the interface in all kinds of tests. The CSEs had a total mass of $\approx$13.1 mg cm⁻² and only contained trace amounts of LEs, which measured less than 3.5 $\mu$L cm⁻² (2.63 mg cm⁻²). This amount was significantly lower than the typical LEs (total = 34.0 mg cm⁻², LE = 25 $\mu$L cm⁻², and 32.6 mg cm⁻²).$^{[7]}$

Theoretical calculations. First-principal calculations were carried out with the standard density functional theory using CASTEP program within the generalized gradient approximation as formulated by the Perdew-Burke-Ernzerhof functional. A simulation cell of $Li_{16}Fe_{16}P_{16}O_{64}$ was established for LFP using a supercell with 16 units. A simulation cell of $Li_{15}NaFe_{16}P_{16}O_{64}$ replacing one of Li at 4a sites with one Na was established for LNFP. The final set of energies for all calculations was computed with an energy cut-off of 570 eV. The convergence criteria for energy were set to be $10^{-5}$ eV, and the residual forces on each atom became smaller than 0.02 eVÅ⁻¹. The Brillouin zone integration was performed with 2 × 3 × 3 $\Gamma$-centred Monkhorst-Pack k-point meshes in geometry optimization calculations. The minimum energy paths of Li jumps between neighboring 4a sites were obtained by means of the NEB method.

## Supporting Information
Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements
B.P. and Z.L. contributed equally to this work. The authors gratefully acknowledge the financial support from National Key R & D Program of China (2021YFB2400400), the National Natural Science Foundation Committee of China (52073143, Key Project of 52131306, and Distinguished Youth Scholar Project of 52122209), Project on Carbon Emission Peak and Neutrality of Jiangsu Province (BE2022031-4), the Natural Science Foundation of Jiangsu Province (No. BK20200696), the China Postdoctoral Science Foundation (2023M730562) and the Jiangsu Funding Program for Excellent Postdoctoral Talent (2023ZB187). The authors also acknowledge the support of the DSI-NRF-WITS SARChI Chair in Materials Electrochemistry and Energy Technologies (MEET) (UID No. 132739).

## Conflict of Interest
The authors declare no conflict of interest.

## Data Availability Statement
The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Keywords
composite solid electrolytes, ionic/electronic conductive layer, $Li_{0.95}Na_{0.05}FePO_{4}$, PVDF, solid-state lithium metal batteries

Received: July 19, 2023
Revised: September 4, 2023
Published online: November 23, 2023

[1] Q. Cheng, X. Zhao, G. Yang, L. Mao, F. Liao, L. Chen, P. He, D. Pan, S. Chen, *Energy Storage Mater.* 2021, 41, 842.

[2] C. F. J. Francis, I. L. Kyratzis, A. S. Best, *Adv. Mater.* 2020, 32, 1904205.

[3] Y. Jin, H. Yu, X. Liang, *Appl. Phys. Rev.* 2021, 8, 031301.

[4] S. Chen, J. Zhang, L. Nie, X. Hu, Y. Huang, Y. Yu, W. Liu, *Adv. Mater.* 2021, 33, 2002325.

[5] Y. Liu, R. Hu, D. Zhang, J. Liu, F. Liu, J. Cui, Z. Lin, J. Wu, M. Zhu, *Adv. Mater.* 2021, 33, 2004711.

[6] M. Yao, Q. Ruan, Y. Wang, L. Du, Q. Li, L. Xu, R. Wang, H. Zhang, *Adv. Funct. Mater.* 2023, 33, 2213702.

[7] Z. Chang, H. Yang, X. Zhu, P. He, H. Zhou, *Nat. Commun.* 2022, 13, 1510.

[8] S. He, Y. Xu, B. Zhang, X. Sun, Y. Chen, Y. Jin, *Chem. Eng. J.* 2018, 345, 483.

[9] Y. Kato, S. Hori, R. Kanno, *Adv. Energy Mater.* 2020, 10, 2002153.

[10] Z. Gao, H. Sun, L. Fu, F. Ye, Y. Zhang, W. Luo, Y. Huang, *Adv. Mater.* 2018, 30, 1705702.

[11] Y. Gu, J. Hu, C. Lai, C. Li, *Adv. Energy Mater.* 2023, 13, 2203679.

[12] S. Deng, X. Li, Z. Ren, W. Li, J. Luo, J. Liang, J. Liang, M. N. Banis, M. Li, Y. Zhao, X. Li, C. Wang, Y. Sun, Q. Sun, R. Li, Y. Hu, H. Huang, L. Zhang, S. Lu, J. Luo, X. Sun, *Energy Storage Mater.* 2020, 27, 117.

[13] W. He, L. Zhou, M. K. Tufail, P. Zhai, P. Yu, R. Chen, W. Yang, *Trans. Tianjin Univ.* 2021, 27, 423.

[14] T. Yang, C. Wang, W. Zhang, Y. Xia, H. Huang, Y. Gan, X. He, X. Xia, X. Tao, J. Zhang, *J Energy Chem* 2023, 84, 189.

[15] A. K. Padhi, K. S. Nanjundaswamy, J. B. Goodenough, *J. Electrochem. Soc.* 1997, 144, 1188.

[16] S.-P. Chen, D. Lv, J. Chen, Y.-H. Zhang, F.-N. Shi, *Energy Fuels* 2022, 36, 1232.

[17] S.-Y. Chung, Y.-M. Chiang, *Electrochem. Solid-State Lett.* 2003, 6, A278.

[18] S.-Y. Chung, J. T. Bloking, Y.-M. Chiang, *Nat. Mater.* 2002, 1, 123.

[19] Y. R. Zhu, R. Zhang, L. Deng, T. F. Yi, M. F. Ye, J. H. Yao, C. S. Dai, *Metall. Mater. Trans. E.* 2015, 2, 33.

[20] N. Nitta, F. Wu, J. T. Lee, G. Yushin, *Mater. Today* 2015, 18, 252.

[21] C. M. Burba, R. Frech, *J. Electrochem. Soc.* 2004, 151, A1032.

[22] Y. Jin, C. Liu, Z. Jia, X. Zong, D. Li, M. Fu, J. Wei, Y. Xiong, *J. Alloys Compd.* 2021, 874, 159890.

[23] X. Shi, N. Ma, Y. Wu, Y. Lu, Q. Xiao, Z. Li, G. Lei, *Solid State Ionics* 2018, 325, 112.

[24] X. Zhang, T. Liu, S. Zhang, X. Huang, B. Xu, Y. Lin, B. Xu, L. Li, C.-W. Nan, Y. Shen, *J. Am. Chem. Soc.* 2017, 139, 13779.

[25] M. Dirican, C. Yan, P. Zhu, X. Zhang, *Mater. Sci. Eng., C* 2019, 136, 27.

[26] H. Huo, N. Zhao, J. Sun, F. Du, Y. Li, X. Guo, *J Power Sources* 2017, 372, 1.

[27] J. Bae, Y. Li, J. Zhang, X. Zhou, F. Zhao, Y. Shi, J. B. Goodenough, G. Yu, *Angew. Chem., Int. Ed.* 2018, 57, 2096.

[28] F. Croce, L. Persi, B. Scrosati, F. Serraino-Fiory, E. Plichta, M. A. Hendrickson, *Electrochim. Acta* 2001, 46, 2457.

[29] J. Zheng, Y.-Y. Hu, *ACS Appl Mater Interfaces* 2018, 10, 4113.

[30] B. K. Zhang, R. Tan, L. Y. Yang, J. X. Zheng, K. C. Zhang, S. J. Mo, Z. Lin, F. Pan, *Energy Storage Mater.* 2018, 10, 139.

[31] W. Guo, W. Zhang, Y. Si, D. Wang, Y. Fu, A. Manthiram, *Nat. Commun.* 2021, 12, 3031.

[32] Y. Wu, Y. Li, Y. Wang, Q. Qiu, Q. Chen, M. Chen, *J Energy Chem* 2022, 64, 62.

[33] J. Sun, J. Peng, T. Ring, L. Whittaker-Brooks, J. Zhu, D. Fraggedakis, J. Niu, T. Gao, F. Wang, *Energy Environ. Sci.* 2022, 15, 5284.

[34] H. Huo, X. Li, Y. Chen, J. Liang, S. Deng, X. Gao, K. Doyle-Davis, R. Li, X. Guo, Y. Shen, C.-W. Nan, X. Sun, *Energy Storage Mater.* 2020, 29, 361.

[35] C. K. Christensen, M. A. H. Mamakhel, A. R. Balakrishna, B. B. Iversen, Y.-M. Chiang, D. B. Ravnsbæk, *Nanoscale* 2019, 11, 12347.

[36] F. Strauss, L. De Biasi, A.-Y. Kim, J. Hertle, S. Schweidler, J. Janek, P. Hartmann, T. Brezesinski, *ACS Mater. Lett.* 2020, 2, 84.

[37] Y. Chen, Z. Wang, X. Li, X. Yao, C. Wang, Y. Li, W. Xue, D. Yu, S. Y. Kim, F. Yang, A. Kushima, G. Zhang, H. Huang, N. Wu, Y.-W. Mai, J. B. Goodenough, J. Li, *Nature* 2020, 578, 251.

[38] X. Xiong, W. Yan, Y. Zhu, L. Liu, L. Fu, Y. Chen, N. Yu, Y. Wu, B. Wang, R. Xiao, *Adv. Energy Mater.* 2022, 12, 2103112.

[39] Q. Zhou, X. Yang, X. Xiong, Q. Zhang, B. Peng, Y. Chen, Z. Wang, L. Fu, Y. Wu, *Adv. Energy Mater.* 2022, 12, 2201991.

[40] L. Luo, Z. Sun, H. Gao, C. Lan, X. Huang, X. Han, P. Su, Z. Zhang, C. Li, W. Huang, Q. Wei, Q. Zhang, M.-S. Wang, S. Chen, *Adv. Energy Mater.* 2023, 13, 2203517.

[41] X. He, J. M. Larson, H. A. Bechtel, R. Kostecki, *Nat. Commun.* 2022, 13, 1398.

[42] C. Jiang, Z. Chen, B. Lu, Z. Li, S. Zhang, Y. Liu, G. Luo, *Chem. Eng. J.* 2022, 450, 138163.

[43] S. Deng, B. Wang, Y. Yuan, X. Li, Q. Sun, K. Doyle-Davis, M. N. Banis, J. Liang, Y. Zhao, J. Li, R. Li, T.-K. Sham, R. Shahbazian-Yassar, H. Wang, M. Cai, J. Lu, X. Sun, *Nano Energy* 2019, 65, 103988.

[44] X. Fan, C. Zhong, J. Liu, J. Ding, Y. Deng, X. Han, L. Zhang, W. Hu, D. P. Wilkinson, J. Zhang, *Chem. Rev.* 2022, 122, 17155.

[45] X. Yang, J. Liu, N. Pei, Z. Chen, R. Li, L. Fu, P. Zhang, J. Zhao, *Nanomicro Lett* 2023, 15, 74.

[46] K. S. Oh, J. E. Lee, Y. H. Lee, Y. S. Jeong, I. Kristanto, H. S. Min, S. M. Kim, Y. J. Hong, S. K. Kwak, S. Y. Lee, *Nanomicro Lett* 2023, 15, 179.