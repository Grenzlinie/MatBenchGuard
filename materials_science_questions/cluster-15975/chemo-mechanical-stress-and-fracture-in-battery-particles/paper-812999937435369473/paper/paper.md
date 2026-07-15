# Controlling Surface Oxides in Si/C Nanocomposite Anodes for High-Performance Li-Ion Batteries

Guorui Zheng, Yuxuan Xiang, Liangfan Xu, Hao Luo, Baolin Wang, Yang Liu, Xiang Han, Weimin Zhao, Shijian Chen, Hailong Chen, Qiaobao Zhang, Ting Zhu,* and Yong Yang*

Si/C composites represent one promising class of anode materials for next-generation lithium-ion batteries. To achieve high performances of Si-based anodes, it is critical to control the surface oxide of Si particles, so as to harness the chemomechanical confinement effect of surface oxide on the large volume changes of Si particles during lithiation/delithiation. Here a systematic study of Si@SiOₓ/C nanocomposite electrodes consisting of Si nanoparticles covered by a thin layer of surface oxide with a tunable thickness in the range of 1–10 nm is reported. It is shown that the oxidation temperature and time not only control the thickness of the surface oxide, but also change the structure and valence state of Si in the surface oxide. These factors can have a strong influence on the lithiation/delithiation behavior of Si nanoparticles, leading to different electrochemical performances. By combining experimental and modeling studies, an optimal thickness of about 5 nm for the surface oxide layer of Si nanoparticles is identified, which enables a combination of high capacity and long cycle stability of the Si@SiOₓ/C nanocomposite anodes. This work provides an in-depth understanding of the effects of surface oxide on the Si/C nanocomposite electrodes. Insights gained are important for the design of high-performance Si/C composite electrodes.

## 1. Introduction

Lithium ion batteries (LIBs) have been widely used in portable electronics, medium to large-scale energy storage systems and electric vehicles.¹ The next-generation LIBs must meet a multitude of stringent requirements, including excellent cycle stability, high capacity, high energy and power densities, high safety, and low cost.²

As an alternative to the graphite anode for commercial LIBs, Si has attracted considerable attention, due to its high theoretical capacity of 3579 mA h g⁻¹, low operating potential, abundance, and low cost. However, the practical applications of Si-based anode materials are hindered by low Li⁺ diffusivity and electrical conductivity and especially by drastic volume changes (≈300%) during lithiation/delithiation. The latter problem can cause Si pulverization, loss of electrical contact, and consumption of active Li associated with the unstable evolution of solid electrolyte interphases (SEIs). As a result, Si-based anodes generally exhibit low Coulombic efficiency, poor cycle stability, and rate capability.³ To address these problems, one effective approach is to use Si nanoparticles (NPs) for the facile accommodation of large volume changes. But the high specific surface area associated with nanomaterials causes aggregation of Si NPs during cycling and provides plenty of active surface sites to form SEIs. Moreover, repeated expansion and contraction of Si NPs induce fracture and uncontrolled formation of

---

G. Zheng, Y. Xiang, L. Xu, S. Chen, Prof. Y. Yang
State Key Laboratory for Physical Chemistry of Solid Surfaces
Collaborative Innovation Center of Chemistry for Energy Materials
Department of Chemistry
College of Chemistry and Chemical Engineering
Xiamen University
Xiamen 361005, P. R. China
E-mail: yyang@xmu.edu.cn

H. Luo, B. Wang, Dr. H. Chen, Prof. T. Zhu
Woodruff School of Mechanical Engineering
Georgia Institute of Technology
Atlanta, GA 30332, USA
E-mail: ting.zhu@me.gatech.edu

Y. Liu
Department of Materials Science Engineering
North Carolina State University
Raleigh, NC 27695, USA

X. Han
Semiconductor Photonics Research Center
Department of Physics
College of Physical Science and Technology
Xiamen University
Xiamen 361005, P. R. China

W. Zhao, Prof. Y. Yang
College of Energy
Xiamen University
Xiamen 361005, P. R. China

Dr. Q. Zhang
Department of Materials Science and Engineering
College of Materials
Xiamen University
Xiamen 361005, P. R. China

---

![](./images/812999937435369473_1.jpg)
The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/aenm.201801718.

DOI: 10.1002/aenm.201801718

Adv. Energy Mater. 2018, 1801718
1801718 (1 of 12)
© 2018 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

SEIs. Consequently, a continuous consumption of active Li and electrolytes can still lead to low Coulombic efficiency, increased impedance, and fast capacity fading of the Si NPs-based anodes in LIBS.

Among Si-based anodes, Si/C composites are considered as one of the most promising class of anode materials that can achieve a large-scale industrial production for commercial use and ultimately replace the graphite anode. $^{[4]}$ The carbon coating layer has been shown to reduce side reactions with the electrolytes and increase the electrical conductivity, so as to enable an improved cycle stability and high rate capability. $^{[5]}$ However, due to the inherently weak interaction between Si and carbon, Si has a tendency to separate from the conductive carbon network and then expose more fresh surface, resulting in the formation of new SEIs during long-term electrochemical cycling. Therefore, various interfacial modifications between Si and carbon have been studied. Hassan et al. used Si-sulfur-graphene to develop a robust hierarchical nanoarchitecture, which prevented agglomeration of Si, stabilized the electrode and SEIs, leading to a superior reversible capacity of over $1000\ \text{mA h g}^{-1}$ for 2275 cycles at $2\ \text{A g}^{-1}.^{[6]}$ Han et al. prepared mesoporous Si particles encapsulated in the interfacial Si-N-C layer to enhance interactions between Si and carbon as well as to form a stable SEI layer, which resulted in a high electrochemical performance. $^{[7]}$ Sun et al. showed that by tailoring the Si-carbon interface with atomic oxygen, the cycle life of Si/C composite electrodes can be improved by $300\%$ even at high mass loadings. $^{[8]}$

The exposed fresh surface of Si can react with oxygen to form a surface layer of $\text{SiO}_{x}$. The presence of the surface $\text{SiO}_{x}$ layer has been shown to alleviate the agglomeration among Si particles and enhance the adhesion between Si and graphene. $^{[9]}$ In addition, $\text{SiO}_{x}$ can react with Li to form $\text{Si}$, $\text{Li}_{x}\text{O}$ and lithium silicate in different forms during the first lithiation process, which could constrain the volume expansion of Si in subsequent cycles. $^{[10]}$ Therefore, it is necessary to investigate the effects of surface oxide on the Si/C composite electrodes in a controllable and quantitative manner, which is essential to their applications in next-generation LIBs. In a recent paper, Cui and co-workers investigated individual Si nanowires with and without surface oxide before and after lithiation by ex situ transmission electron microscopy (TEM). $^{[10\text{a}]}$ Their results indicated that the thickness of surface oxide and the size of nanowire critically affected the lithiation-induced volume expansion and electrochemical cycling characteristics. However, the effects of surface oxide on the volume change of Si NPs in practical electrodes could be more complex than those on individual nanowires revealed by ex situ TEM. Hence, it is important to conduct a more in-depth study of the Si/C nanocomposite anodes with different extents of surface oxidation of Si NPs.

In this paper, we prepared a series of $\text{Si@SiO}_{x}/\text{C}$ nanocomposite anodes with controlled surface oxide thickness. We conducted the structural characterization, electrochemical measurement, and chemomechanical simulation for those nanocomposite systems. The optimal conditions of surface oxide were studied in order to achieve high performances of $\text{Si@SiO}_{x}/\text{C}$ nanocomposite anodes. The integrated experimental and modeling studies indicate that the $\text{Si@SiO}_{x}/\text{C}$ nanocomposites with thick surface oxides lead to low Li diffusion/reaction kinetics and self-limiting lithiation, resulting in a low capacity but long-cycle stability. By contrast, thin surface oxides give rise to a high capacity but low cycling stability. This can be attributed to the limited mechanical constraints by the thin surface oxides, leading to surface cracking and degradation of Si NPs. Our results show that an optimal thickness of about 5 nm for the surface oxide layer enables a combination of high capacity and cycle stability for the $\text{Si@SiO}_{x}/\text{C}$ nanocomposite anodes. Finally, we note that the surface oxide can also influence the formation and evolution of SEIs; their effects on the electrochemical performance are not clearly understood and warrant further study in the future. $^{[11]}$

## 2. Results and Discussion

### 2.1. Structure and Morphology

A series of $\text{Si@SiO}_{x}/\text{C}$ nanocomposite anodes were synthesized in this work, as described in detail in the Experimental Section. The $\text{Si@SiO}_{x}/\text{C}$ NPs in the nanocomposite have a core of crystalline Si, an inner shell of thermally grown amorphous $\text{SiO}_{x}$ with controlled oxidation extent, and an outer shell of carbon coating. TEM experiments were performed to characterize the oxide thickness, microstructure, and interfacial morphology of the $\text{Si@SiO}_{x}$ NPs prepared with different oxidation conditions. As shown in Figure 1a, as-received Si NPs are about 30 nm in diameter. Fast Fourier transform (FFT) analysis of the marked areas indicates that the Si NPs have a core of crystalline Si and a thin shell of amorphous $\text{SiO}_{x}$. To tune the thickness of the amorphous $\text{SiO}_{x}$ shell, the initial oxide layer of about 4 nm thick on the surface of as-received Si NPs was removed by washing with HF acid, and subsequently a native oxide layer of about 1 nm thick was formed when Si NPs were exposed in air. These NPs were further oxidized to increase the thickness of the oxide layer in the range of 1–10 nm, as controlled by the oxidation temperature and time.

Figure 2a–e shows the characterization results of microstructure and composition of the $\text{Si@SiO}_{x}$ NPs with different oxide layer thicknesses. In the X-ray diffraction (XRD) patterns, a broad hump centered at $2\theta$ of $21.8^\circ$ is seen and the peak intensity increases with the increasing oxidation temperature and time, which is characteristic of amorphous Si suboxides. $^{[10\text{c}]}$ The Bragg diffraction peaks of crystalline Si confirm the presence of crystalline Si, which is encapsulated in the amorphous $\text{SiO}_{x}$ shell, as shown by the TEM images in Figure 1. The Fourier transform infrared (FTIR) spectra of different $\text{Si@SiO}_{x}$ NPs (Figure 2b) show three characteristic peaks around 1100, 810, and $480\ \text{cm}^{-1}$, which can be assigned to the asymmetric $\text{Si-O-Si}$ bond stretching, $\text{SiO}_{4}$ tetrahedron ring, and $\text{O-Si-O}$ bond deformation, respectively. $^{[12]}$ The shapes and positions of the peaks vary for different samples. The increase of peak intensity and blue shift with the increasing oxidation temperature and time can be associated with a thicker $\text{SiO}_{x}$ layer and a higher valence state distribution of Si in $\text{SiO}_{x}$. Hence, these results indicate that both the thickness and composition (Si/O ratio and defects in $\text{SiO}_{x}$) of the oxide layers can be controlled by varying oxidation conditions. $^{[13]}$ Furthermore, all the Raman spectra of $\text{Si@SiO}_{x}$ NPs with different oxide layer thicknesses (Figure 2c) show a single Raman band corresponding

![](./images/812999937435369473_2.jpg)

Figure 1. TEM images and associated FFT images (of the red boxed area in the corresponding TEM images) for Si NPs under different oxidation treatment, showing Si NPs with a) an initial oxide layer of 4 nm thick. b) A native oxide layer of 1 nm thick. c) An oxide layer of 1 nm thick produced by oxidation at 650 °C for 20 min. d) An oxide layer of 5 nm thick produced by oxidation at 750 °C for 20 min. e) An oxide layer of 6 nm thick produced by oxidation at 750 °C for 60 min. f) An oxide layer of 8 nm thick produced by oxidation at 850 °C for 5 min. g) An oxide layer of 10 nm thick produced by oxidation at 850 °C for 20 min. h) Comparison of thickness of the thermally grown oxide layers under different oxidation conditions shown in (a) to (g).

to nanocrystalline Si, which has a large extent of red shift compared to that of the Si wafer (520 cm⁻¹); this change can be attributed to the effect of slight destruction of the lattice structure in nanocrystalline Si compared to the reference Si wafer. Furthermore, there also exists a small extent of blue shift with increasing oxidation temperature and time among samples with different oxide layers; this is likely due to the fact that a strong optical phonon mode of Si crystal confined in the SiOₓ matrix can affect the lattice vibration mode of Si. Interest- ingly, compared to the sample oxidized at 750 °C for 20 min, the Si NPs oxidized at 750 °C for 30 or 40 min show red shift in spite of their increasing oxidation extent, which implies the poor quality of the oxide layer derived from change of its micro- structure that can be correlated to their inferior electrochemical cyclic stability as discussed below. The above results indicate that the quality of oxide layers formed on the surface of Si NPs is not only dependent on oxide thickness, but also influenced by composition, which could affect the corresponding electro- chemical performance.

To further clarify the chemical environment of Si in dif- ferent Si@SiOₓ nanocomposites, we carried out quantitative $^{29}$Si magic angle spinning (MAS) nuclear magnetic resonance (NMR) analysis. As shown in Figure 2d,e, all the samples show a pronounced resonance centered around -81 ppm and a small and broad resonance centered around -109 ppm. The former is assigned as the covalently bonded Si atoms in crystalline Si and the latter is assigned to tetrahedral coordi- nated Si atoms in the amorphous SiOₓ environments, respec- tively.[¹⁴] The decrease in peak intensity of the crystalline Si and the concerted increase in peak intensity of the amorphous SiOₓ further indicate an increased ratio of SiOₓ versus Si with extended oxidation. Moreover, the peak of crystalline Si is shifted toward high field direction and the peak width is broadened, which may correspond to an increase of the com- pressive stress leading to a slight structure change in the lat- tice of bulk Si due to the thicker oxide layers under extended oxidation. On the other hand, the peak of amorphous SiOₓ is also shifted toward the high field direction, implying that the valence state of Si becomes higher with extended oxidation. Therefore, Si NPs oxidized under different condi- tions not only show the difference in the thickness of oxide layers, but also the chemical characteristics of Si in the SiOₓ layers, which can influence the stress generation and lithia- tion dynamics in Si@SiOₓ NPs.

The scanning electron microscopy (SEM) images in Figure S1a-d of the Supporting Information show the surface

![](./images/812999937435369473_3.jpg)

Figure 2. Characterization of structures and compositions of Si@SiOₓ NPs with different thicknesses of surface oxide layers. a) XRD patterns, b) FTIR spectra, c) Raman spectrums, and d,e) ²⁹Si MAS NMR spectra.

morphology of as-received Si NPs, Si NPs with native oxide layer, polyacrylonitrile (PAN)-coated Si NPs with native oxide layer, and carbon-coated Si NPs with native oxide layer, respectively. It is seen from Figure S1a of the Supporting Information that the as-received Si NPs have a uniform size of about 30 nm. After hydrofluoric acid treatment, the Si NPs with native oxide layer are well dispersed and their electrical conductivities should be enhanced as shown in Figure S1b of the Supporting Information. The PAN-coated samples in Figure S1c of the Supporting Information were annealed for preparing the carbon-coated Si NPs in Figure S1d of the Supporting Information. These carbon-coated Si NPs have a high carbon content of 18.47 wt% and their morphology is apparently different from that of Si NPs with a native oxide layer. As indicated by circles in Figure S1d of the Supporting Information, floc-like carbon is readily found. Such kind of carbon can block the agglomeration of Si NPs and also connect Si NPs through a fine conductive network. Moreover, the binder-free monolithic structure is porous for infiltration of electrolytes into the bulk electrode, so as to promote charge transfer and ion diffusion.

The chemical characteristics of Si in the SiOₓ layers of different Si@SiOₓ/C nanocomposite electrodes are determined by X-ray photoelectron spectroscopy (XPS), as shown in Figure 3. The Si 2p peak is corrected according to C 1s peak centered at 284.8 eV. Obviously, there are broad peaks within the range of 102–107 eV in all the measured samples, which are fitted with four peaks belonging to $Si^+$, $Si^{2+}$, $Si^{3+}$, and $Si^{4+}$ of the amorphous SiOₓ layer.^{[15]} Compared to the results of as-received Si NPs in Figure 3a, the averaged binding energy of Si in the SiOₓ layer in Figure 3b moves to a lower energy, indicating that HF acid can effectively remove the initial oxide to form a native oxide in air. Furthermore, with increasing oxide thickness, the averaged valence of Si in the SiOₓ layer also increases (Figure 3c,d). It is clear that the native SiOₓ layer has a tendency to turn into a SiO₂ layer during continuous oxidation of SiOₓ and, however, positively influence their mechanical confinement effect. In addition, the peaks centered at around 99.5 eV are fitted into two peaks related to Si 2p₁/₂ and Si 2p₃/₂ which are attributed to the signal from Si clusters/domains remaining in the SiOₓ layer or/and the crystalline Si under the oxide layer, as the thickness of the SiOₓ layer could be slightly less than the penetration depth of the X-ray photoelectron. With the increasing oxidation of the SiOₓ layer, the Si signal decreases gradually and eventually disappears in the sample oxidized at 850 °C for 20 min, which does not necessarily imply the disappearance of crystalline Si, but rather indicates the disappearance of XPS detectable Si with an increased thickness of the SiOₓ layer.

### 2.2. Electrochemical Properties

To understand the effect of surface oxide on the performance of Si@SiOₓ/C nanocomposites, electrochemical measurements were carried out. Figure 4a shows the reversible capacity and cyclic stability of the electrodes prepared by Si NPs under different oxidation treatment. The associated electrochemical

![](./images/812999937435369473_4.jpg)

Figure 3. XPS spectra of Si 2p of different Si@SiOₓ/C nanocomposite electrodes before cycling. a) As-received Si NPs. b) Si NPs with native oxide.
c) Si NPs surface oxide grown at 750 °C for 30 min. d) Si NPs surface oxide grown at 850 °C for 20 min.

parameters are summarized in Table 1. The gravimetric specific capacity is calculated based on the mass of the entire electrode, thus accounting for the contribution of amorphous SiOₓ and C to the total capacity. From elemental analysis, the contents of C, H, and N on electrode after annealing were 18.47, 0.87, and 4.75 wt%, respectively. During the first lithiation and delithiation, the Si NPs with the native oxide layer of ≈1 nm thick show the specific capacities of 2580 and 2129 mA h g⁻¹, respectively, which correspond to an initial Coulombic efficiency of 83%. A rapid capacity drop occurs in the early cycles, which indicates fast degradation of the native oxide layer, leading to an irreversible consumption of active Li. With an increase of degree of oxidation, the cycle performance is improved. Especially, for the sample oxidized at 750 °C for 20 min, giving an oxide layer of ≈5 nm thick, the specific capacities during the first lithiation and delithiation are respectively 2209 and 1777 mA h g⁻¹, which correspond to an initial Coulombic efficiency of 80%; the capacity decreases slowly, reaching 783 mA h g⁻¹ after 300 cycles. However, for the sample oxidized at 750 °C for 30 min, giving an oxide layer of ≈6 nm thick, the specific capacities are stable during the first 100 cycles, but decrease markedly after 100 cycles. This is similar to the fast capacity decrease of the Si NPs with the native oxide layer. As the oxidation temperature or/and time are further increased, the cycle performance is improved again, but the reversible capacity is lower, especially in the sample oxidized at 850 °C for 20 min giving an oxide layer of 10 nm thick. Hence, the above results indicate that one can adjust the oxidation conditions to achieve different electrochemical performance. For example, the sample with an oxide layer of 5 nm thick exhibits a higher capacity, while the sample with an oxide layer of 8 nm thick enable a better cycle performance at a lower capacity. According to previous work,^{[10a]} the large volume expansion of lithiated Si NPs could be suppressed by surface oxide, due to the lithiation-induce hydrostatic compressive stress that limits the extent of lithiation. However, this simple argument is at variance with our results.

To study the relationship between oxide thickness and electrochemical performance, the Si@SiOₓ/C nanocomposite electrodes with different oxide layer thicknesses are cycled by starting with a discharge process, which corresponds to lithiation of the electrodes between 5 mV and 2 V at a current density of 210 mA g⁻¹ in a half-cell at 30 °C. The measured lithiation-delithiation profiles at different cycles are shown in Figure 4b-e. During the first cycle, the voltage profiles of all samples are compared in Figure S2a of the Supporting Information. The initial voltage hysteresis of different samples shows a slight difference, indicating that there are different lithiation and delithiation dynamics of bulk Si which are influenced by surfaces oxides with different thicknesses. With an increasing degree of oxidation, the potential difference between lithiation and delithiation plateaus is increased during the first cycle, indicating the passivation of surface oxide and a better crystallization of bulk silicon with increasing oxidation extent. The corresponding differential capacity (dQ/dV) plots for all samples

![](./images/812999937435369473_5.jpg)

Figure 4. Electrochemical performance of the Si@SiOₓ/C nanocomposite anodes with different surface oxide thicknesses. a) Specific delithiation capacity versus cycle number at the discharge (lithiation)/charge (delithiation) current densities of 210 mA g⁻¹ between voltage limits of 5 mV to 2 V using a 10 vol% fluoroethylene carbonate (FEC)-added electrolyte. b–e) Galvanostatic voltage profiles at a current density of 210 mA g⁻¹. (b) Si with native oxide (1 nm thick), (c) 750 °C, 20 min (5 nm thick), (d) 750 °C, 30 min (6 nm thick), and (e) 850 °C, 20 min (10 nm thick).

during the first cycle are compared in Figure S2b of the Supporting Information. Interestingly, the sample oxidized at 750 °C for 20 min with a surface oxide layer of ≈5 nm thick exhibits a sharp peak at 0.07 V, which may correspond to a stable lithiation process due to the well-formed oxide layer and the stable SEI layer with superior mechanical properties despite large volume expansion during lithiation. The inset in Figure S2b of the Supporting Information reveals the formation of SEI layers and the onset of lithiation of SiOₓ and carbon with potentials higher than bulk Si. These results suggest that the lithiation

<table>
<thead>
<tr>
<th>Samples</th>
<th>1st Lithiation capacity [mA h g⁻¹]</th>
<th>1st Delithiation capacity [mA h g⁻¹]</th>
<th>1st Coulombic efficiency [%]</th>
<th>Delithiation capacity after 300 cycles [mA h g⁻¹]</th>
<th>Delithiation capacity retention ratio after 300 cycles [%]</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pristine Si</td>
<td>2289</td>
<td>1891</td>
<td>83</td>
<td>709</td>
<td>37</td>
</tr>
<tr>
<td>Si with native oxide layer</td>
<td>2580</td>
<td>2129</td>
<td>83</td>
<td>40</td>
<td>2</td>
</tr>
<tr>
<td>650 °C, 20 min</td>
<td>2400</td>
<td>1968</td>
<td>82</td>
<td>159</td>
<td>8</td>
</tr>
<tr>
<td>750 °C, 20 min</td>
<td>2209</td>
<td>1777</td>
<td>80</td>
<td>783</td>
<td>44</td>
</tr>
<tr>
<td>750 °C, 30 min</td>
<td>1950</td>
<td>1595</td>
<td>82</td>
<td>120</td>
<td>8</td>
</tr>
<tr>
<td>750 °C, 40 min</td>
<td>1658</td>
<td>1329</td>
<td>80</td>
<td>306</td>
<td>23</td>
</tr>
<tr>
<td>750 °C, 60 min</td>
<td>1049</td>
<td>813</td>
<td>78</td>
<td>625</td>
<td>77</td>
</tr>
<tr>
<td>850 °C, 5 min</td>
<td>1061</td>
<td>776</td>
<td>73</td>
<td>733</td>
<td>94</td>
</tr>
<tr>
<td>850 °C, 20 min</td>
<td>459</td>
<td>279</td>
<td>61</td>
<td>387</td>
<td>139</td>
</tr>
</tbody>
</table>

starts in SiOₓ and C, and then proceeds in Si, as shown clearly for the cases of as-received Si and Si with native oxide with an extra peak at around 0.4 V. This could be attributed to better lithiation of SiOₓ and C without further thermal oxidation treatment. On the other hand, the formation stage of SEI layers is much different. With increasing oxidation extent, especially for the sample oxidized at 850 °C for 20 min, giving an oxide layer of 10 nm thick, a broad peak in the range of 0.6–1.0 V is observed, which could be attributed to the formation of SEIs on the surface of the electrode by reductive decomposition reaction of electrolytes. These results indicate that different oxides formed on the surface of Si NPs play an important role in the formation of SEI layers that may affect the cyclic stability. During cycling, the sample with a native oxide layer of 1 nm thick shows more severe polarization and rapid capacity decay from the very beginning of lithiation and delithiation, while the capacity of the sample oxidized at 750 °C for 30 min (giving the oxide layer of 6 nm thick) starts to deteriorate after 50 cycles. However, the sample oxidized at 750 °C for 20 min (giving the oxide layer of 5 nm thick) exhibits a slow capacity decay without a drastic capacity drop. Moreover, for the sample oxidized at 850 °C for 20 min (giving the oxide layer of 10 nm thick), starting from the second cycle, the potential difference decreases and the delithiation capacity increases, indicating the activation of active materials due to slow and continuous lithiation of the thick SiOₓ layer, which is effective to reduce the charge-transfer resistance. Therefore, surface oxides can not only affect the kinetics of lithium insertion and extraction, but also influence the formation of SEI layers, leading to different electrochemical behaviors.

As shown in Figure 5a, all the Nyquist plots are composed of a depressed semicircle at high-medium frequency and an inclined tail at low frequency after delithiation in the second cycle. The depressed semicircle is associated with the total resistance of the SEI film, interphase contact and charge transfer, and the inclined tail represents the Li ion diffusion process.[¹⁶] To compare the reaction kinetics of Li⁺ with different Si@SiOₓ/C nanocomposite electrodes, all the semicircles are fitted through an equivalent circuit model in Figure 5b, and the resistance values of samples with different oxide layers are presented in Figure 5c. It is seen that with an increasing degree of oxidation, the resistances of different electrodes increase except for the samples oxidized at 750 °C for 30 and 40 min. Combining the above results with the cycle performance in Figure 4a, we note that the surface oxide layers on Si NPs formed at 750 °C for 30 and 40 min (giving an oxide layer of 6 nm thick) exhibit the most favorable electrochemical activity due to the enhance Li-ion and electron transfer at the electrode–electrolyte interface. However, these electrodes have relatively low cycle stability, which can be due to the poor mechanical stability induced by large volume changes during lithiation/delithiation cycling. Therefore, Si NPs with the optimal oxide thickness of 5 nm show a good combination of electrochemical activity and cycle stability.

### 2.3. Modeling of Optimal Oxide Thickness

To provide a theoretical understanding of the optimal surface oxide thickness, a chemomechanical model is developed to simulate the lithiation process of a representative Si NP covered with a SiO₂ surface layer of different thicknesses, as shown in Figure S3 of the Supporting Information. Similar to our previous modeling work of Si lithiation,[¹⁷] a nonlinear diffusion model is used to simulate the two-phase lithiation in the Si NP; and an elastic-perfectly plastic constitutive model is used to simulate the mechanical response of the lithiated Si. The elastic modulus and yield stress of lithiated Si are assumed to depend linearly on Li concentration. For the thin surface layer of the lithiated SiO₂, we assume it has a uniform Li distribution and a constant elastic modulus of 90 GPa, which is sufficiently large to represent the effect of mechanical constraint on the expansion of the lithiated Si. Previous in situ TEM experiments have revealed the self-limiting lithiation in Si nanowires and NPs,[¹⁸] which can be attributed to the high compressive stresses generated at the two-phase boundary (i.e., lithiation reaction front) as well as in lithiated Si. To account for this effect, we set a critical pressure above which the lithiation process effectively stops. The corresponding volume fraction of the unlithiated Si is determined for Si NPs with different oxide layer thicknesses.

Figure 6a shows the calculated volume fraction of unlithiated Si as a function of the oxide thickness for two representative critical pressures, e.g., 2.5 and 4.0 GPa. It is seen that an

![](./images/812999937435369473_6.jpg)

![](./images/812999937435369473_7.jpg)

![](./images/812999937435369473_8.jpg)

**Figure 5.** Electrochemical impedances of Si@SiOₓ/C nanocomposite electrodes. a) Electrochemical impedance spectroscopy (EIS) curves after delithiation in the second cycle and b) equivalent circuit model; $R_{sol}$: contact resistance; $R_{ct}$: charge transfer resistance; CPE$_{ct}$: constant phase element (space double-layer capacitance); $W_{dif}$: Warburg impedance. c) Electrode kinetic parameters obtained by fitting the depressed semicircles in (a) through the equivalent circuit model in (b).

increase of oxide thickness leads to an increased volume fraction of unlithiated Si. In addition, an increase of the critical pressure enables an increased extent of lithiation and thus reduces the volume fraction of the unlithiated Si. Figure 6a also indicates that a thinner surface oxide imposes less constraint on the self-limiting lithiation of Si NPs and thus leads to a more effective utilization of active Si. This can result in a larger expansion of the lithiated Si NP and thus a higher tensile hoop stress near the outer surface of the oxide layer, as shown in Figure 6b. The high tensile hoop stress can cause surface cracking and even fracture of the NP, $^{[19]}$ leading to fast capacity fade. It should be noted that the largest tensile hoop stress in the outer oxide layer occurs near the interface between the Si NP and SiOₓ oxide layer, as shown in Figure S4b of the Supporting Information. However, it is reasonable to assume the initiation of fracture from the outer surface of the SiOₓ oxide layer, as shown by our previous in situ TEM observation. $^{[19]}$ Hence we plot in Figure 6b the tensile hoop stress near the outer surface of the oxide layer.

The competing effects of self-limiting lithiation and oxide fracture result in an optimal regime of the oxide thickness. As depicted in Figure 6c, in the limit of a very thin oxide (i.e., the yellow region on the left), the weak mechanical constraint gives rise to a delay of self-limiting lithiation and thus a buildup of high stress in the oxide layer. This can lead to oxide fracture and fast capacity decay. By contrast, in the limit of a very thick oxide (i.e., the yellow region on the right), the strong mechanical constraint enhances the effect of self-limiting lithiation. This can reduce the utilization of active Si and thus the capacity of the electrode. In addition, since the specific capacity of SiOₓ is lower than that of Si, the thick oxide also contributes to capacity decrease. Therefore, the intermediate oxide thickness of around 5 nm (the green region in Figure 6c) allows a balanced electrochemical performance with high capacity and stability of the Si@SiOₓ/C nanocomposite electrode. Hence, our modeling study provides a rational understanding of the optimal oxide thickness from the perspectives of mechanical constraints and degradation of surface oxides, while other factors such as the lithiation/delithiation rate effects in oxides as well as the formation and evolution of SEIs have not been clearly understood and require a more in-depth study in the future.

To further investigate the effects of oxide thickness, we show in Figure 7a the ex situ Raman spectroscopy of Si@ SiOₓ/C nanocomposite electrodes with different oxide thicknesses after the second delithiation to 2 V. $^{[20]}$ In principle, the sharp peak centered at $\approx$515 cm⁻¹ due to the F₂g mode arises from scattering of the first-order optical phonon of crystalline Si, while the broad peak centered at $\approx$480 cm⁻¹ corresponds to the presence of amorphous Si. It is seen from Figure 7a that for the electrodes composed of Si NPs with a native oxide of 1 nm thick, there only exists a broad of peak of amorphous Si after the second delithiation. This indicates that the initial crystalline Si core of Si NPs has been fully lithiated, resulting in amorphous Si after the second delithiation and thus a lack

![](./images/812999937435369473_9.jpg)

Figure 6. Chemomechanical modeling results of the optimal thickness of surface oxide of Si NPs, by accounting for the competing effects of surface oxide on self-limiting lithiation and oxide fracture. a) Fraction of unlithiated Si (i.e., ratio of the volume of unlithiated Si ($V^u$) over the volume of a Si NP ($V_0$)) as a function of oxide thickness $t_0$ when self-limiting lithiation occurs for the critical pressure of 2.5 and 4.0 GPa. b) Hoop stress at the surface of the lithiated oxide layer as a function of oxide thickness $t_0$ when self-limiting lithiation occurs for the critical pressure of 2.5 and 4.0 GPa. c) Competing effects of self-limiting lithiation and oxide facture resulting in an optimal thickness regime (indicated in green) based on the results in (a) and (b) in the case of the critical pressure of 4.0 GPa.

of the peak of crystalline Si. With the increasing thickness of surface oxide, the intensity ratio between the sharp peak of crystalline Si and the broad peak of amorphous Si increases gradually. This indicates that a higher extent of surface oxida- tion of Si NPs leads to less utilization of the crystalline Si core, which can be attributed to the stronger effects of mechanical constraints and associated self-limiting lithiation as shown by our chemomechanical modeling results in Figure 6. It follows that the unlithiated Si core and the thick shell of surface oxides help improve the cycle performance, despite the reduced capacity. In addition, we note that the changes in the band in Figure 7a are likely due to the phonon confinement effect influenced by size and surface state of Si. Moreover, Figure 7b shows the same D-band and G-band of delocalized $sp^2\pi$ bonds in carbon caused by disorder-induced phonon mode and graphite band respectively in all the samples, proving the formation of the same amorphous carbon coating during annealing of PAN.

Figure 7c-h shows the SEM images of surface morphology of the nanocomposite electrodes before and after 2 cycles. The electrode of SiNPs with 1 nm thick native oxide exhibits a rough surface morphology comprising of NPs with irregular shapes and nonuniform sizes after 2 cycles (Figure 7f). This can be attributed to drastic volume changes and severe agglom- eration of Si NPs, indicating that the thin native oxide is inef- fective to mitigate the degradation of Si NPs. It is one of the main reasons of large capacity loss during initial cycling. With an increasing extent of oxidation of Si NPs, the electrodes after cycling become more uniform and denser especially in those with a surface oxide layer of 10 nm thick (Figure 7g,h). The well-reserved NPs with regular sizes are linked by carbon net- works, thus maintaining the high structural integrity and elec- tronic and ionic conductivities. Figure S5a-c and S6a-f of the Supporting Information further show the surface morphologies of $Si@SiO_x$/C nanocomposite anodes with different oxide thick- nesses after 20 and 300 cycles, respectively. Similar to Figure 7, Si NPs with 1 nm thick native oxide have fractured into smaller NPs, resulting in highly uneven surfaces that presumably lead to the formation of more SEIs. By contrast, there are less changes of surface morphologies of the electrodes containing Si NPs with a higher degree of oxidation such as those with surface oxides of 5 or 10 nm thick. This indicates the improved structural stability that can be related to the more stable electro- chemical cycle performance.

![](./images/812999937435369473_10.jpg)

Figure 7. Raman spectra and SEM characterization for the Si@SiOₓ/C nanocomposite electrodes. a,b) Raman spectra measured after the second delithiation to 2 V. SEM images of the electrodes are taken c-e) before cycling and f-h) after 2 cycles. Si NPs with surface oxide of (c,f) 1 nm thick, (d,g) 5 nm thick, and (e,h) 10 nm thick.

### 3. Conclusion
We have developed a series of Si@SiOₓ/C nanocomposite electrodes with controlled surface oxide thickness. To focus on understanding the effects of surface oxides, the electrodes are prepared via thermal decomposition of PAN which is used as carbon source, so as to avoid extra binders. We find that the oxidation temperature and time not only change the thickness of surface oxide, but also affect the composition and valence state distribution of Si, all of which can influence the electrochemical performance of the resulting electrodes. Our combined experimental and modeling results show that there exists an optimal surface oxide layer of about 5 nm thick in the Si@SiOₓ/C nanocomposite, which exhibits a combination of high capacity and cycle stability. For Si@SiOₓ/C nanocomposite electrodes with thicker surface oxides (e.g., 8 or 10 nm thick), the cycle stability can be improved as less appreciable capacity attenuation is measured up to 300 cycles, but the capacity is reduced due to a limited lithiation extent of Si NPs arising from the constraining effects of thick oxides. Overall, our work demonstrates the critical role of surface oxides of Si NPs in the rational design of Si/C composite electrodes, and insights gained are valuable for the development of other surface-engineered electrode particles for advanced LIBs.

### 4. Experimental Section
**Preparation of Si@SiOₓ Nanocomposites with Controlled Oxide Thickness:** To study the effects of surface oxide on the Si/C nanocomposite electrode, Si NPs with a uniform size of 30 nm were used. The as-received commercial Si NPs were first dipped in 5 vol% hydrofluoric acid for 30 min to remove the initial surface oxide. After acid treatment, the NPs were filtered from the solution and rinsed with large amounts of water and ethanol to remove excess hydrofluoric acid and residual

$SiF^{6-}$. Then the Si NPs were dried overnight in a vacuum oven at $80\ ^{\circ}C$. The native oxide was spontaneously grown on the surface of Si NPs when exposed in air. The oxidation temperature and time were further varied to control thickness of thermally grown oxide on the surface of Si NPs. The dried SiNPs were heated to the desired temperature at a rate of $4\ ^{\circ}C\ \text{min}^{-1}$ in the tube furnace under Ar atmosphere and then held for the desired time under $O_2$ stream. After this process was completed, the tube furnace was naturally cooled down to room temperature under Ar atmosphere. As a result, SiNPs covered by a thin layer of surface oxide with thickness in the range of 1-10 nm were obtained.

Preparation of Carbon-Coated $Si@SiO_x$ ($Si@SiO_x/C$) Electrodes: The binder-free monolithic composite electrodes were prepared by ball- milling and post-annealing. First, the $Si@SiO_x$ nanocomposite was dispersed into the liquid dimethyl formamide (DMF) and then mixed with PAN (10 wt% PAN was dissolved in liquid DMF beforehand to obtain a PAN solution) at a mass ratio of 1:1 using an agate jar. The mixture was blended using a planetary ball mill for 3 h at 300 rpm to form a viscous slurry. The slurry was spread onto a copper foil current collector with a diameter of 16 mm and then dried overnight in a vacuum oven at $80\ ^{\circ}C$ to form a monolithic PAN-coated $Si@SiO_x$ nanocomposite electrode. The dried PAN-coated $Si@SiO_x$ nanocomposite electrode was annealed in a tube furnace with flowing Ar by a series of operation of heating at a rate of $4\ ^{\circ}C\ \text{min}^{-1}$ to $700\ ^{\circ}C$, maintaining the temperature for 1 h, and natural-cooling to room temperature. The total active material loaded on an electrode was about 1 mg.

Material Characterization: The morphologies and structures were characterized by SEM (HITACHI S-4800) and TEM (Philips-FEI Tecnai $G^2$ F20). XRD patterns of the samples were obtained by a Rigaku Ultima IV with Cu $K\alpha$ radiation. A FTIR spectroscope (Thermo Nicolet 360FT- IR) was used for recording the FTIR spectra of the samples in the range of $400-4000\ \text{cm}^{-1}$. Raman spectra were collected using a 532 nm laser from Renishaw Raman system. For the preparation of Raman samples after the second delithiation to 2 V, the electrodes were removed from the cycled cells and were rinsed with anhydrous dimethyl carbonate for several times so as to minimize residual electrolytes. Then the electrodes were dried, sealed, and stored in a glove box under argon, and they were exposed to air for $\approx 30$ s when transferred into the Raman spectrometer. XPS spectra were acquired with PHI QUANTUM 2000 spectrometer with monochromatic Al $K\alpha$ 1486.6 eV radiation, operating at 23.2 W and in a vacuum of $<10^{-8}$ Torr. The universal contamination of the C-H bond at 284.8 eV was used as a reference for the final adjustment of energy scale in the spectra. The $^{29}$Si solid-state NMR experiments were performed on a Bruker Avance 400 NMR spectrometer with a $^{29}$Si Larmor frequency of 79.5 MHz using Bruker 4 mm double-resonance MAS NMR probe with a spinning frequency up to 12.5 kHz. The spectra were referenced to $Li_2SiO_3$ (-74 ppm, $^{29}$Si) and quantitatively analyzed through a known mass of sample used to fill the 4 mm rotor and a known number of scans when collecting the spectra. The $^{29}$Si NMR spectra were acquired using direct polarization with a $90^{\circ}$ pulse length of $1.5\ \mu\text{s}$, recycle delay of 90 s and with the bearing gas at room temperature. A Vario EL III (Elementar, Germany) was used to analyze the elemental content of the carbon-coated $Si@SiO_x$ nanocomposites. The mass of active material was carefully weighted by a microbalance (METTLER TOLEDO XS3DU) with an accuracy of $1\ \mu\text{g}$.

Electrochemical Measurements: The electrochemical measurements were carried out using CR2025 coin-type half-cells that were assembled in an argon-filled glove box and then aged for 48 h before testing. The prepared carbon-coated $Si@SiO_x$ nanocomposite electrodes served as the working electrode, lithium metal as the counter electrode, and Celgard 2300 as physical separators. The electrolyte for all the tests was $1\ \text{M}\ LiPF_6$ salt in ethylene carbonate-ethyl methyl carbonate-diethyl carbonate in a 1:1:1 ratio by volume with 10 vol% FEC additive. The assembled half cells were tested galvanostatically between 5 mV and 2 V (vs $Li/Li^+$) at a current density of $210\ \text{mA}\ \text{g}^{-1}$ on a Land CT2001A system at the temperature of $30\ ^{\circ}C$. EIS experiments were measured over the frequency ranges from 100 kHz to 10 mHz with an alternative current amplitude of 5 mV on a four-channel multifunctional electrochemical work station (PARSTAT MC) and the resulting EIS data were analyzed with the ZView electrochemical software package.

Chemomechanical Model: To simulate the two-phase lithiation in a Si NP with the resultant core-shell structure and self-limiting behavior, a nonlinear diffusion model was employed. $^{[17]}$ That is, the $Li^{+}$ diffusivity $D$ is taken as a nonlinear function of Li concentration and stress,
$$
D=D_{0} \exp \left[-\frac{\sigma_{\mathrm{p}} \Omega}{R T}\left(3.9 c-\frac{1}{1-c}\right)\right],
$$
where $D_0$ is the diffusivity constant, $c$ is the Li concentration normalized by the Li concentration at the fully lithiated state, $\Omega$ is the activation volume of Li diffusion, and $\sigma_{\mathrm{p}}$ is the pressure. It is assumed that the maximum value of $D$ is capped at $10^4D_0$, so as to facilitate the numerical stability near $c=1$. To simulate the lithiation-induced stress, an elastic and perfectly plastic model are used, in which the total strain rate tensor comes from three contributions, $\dot{\varepsilon}=\dot{\varepsilon}^{\mathrm{e}}+\dot{\varepsilon}^{\mathrm{p}}+\dot{\varepsilon}^{\mathrm{c}}$, where $\dot{\varepsilon}^{\mathrm{e}}$ and $\dot{\varepsilon}^{\mathrm{p}}$ are elastic strain rate and plastic strain rate, respectively; the elastic plastic behavior obey Hooke's law and classical $J_2$-flow rule respectively; $\dot{\varepsilon}^{\mathrm{c}}$ is the chemical strain rate caused by lithiation and its component is proportional to the rate of the normalized Li concentration,$\dot{\varepsilon}_{ij}^{\mathrm{c}}=\beta_{ij}\ \dot{c}$, where $\beta_{ij}$ is the coefficient of lithiation-induced expansion. The above chemomechanical model of coupled Li diffusion and elastic-plastic deformation is numerically implemented in the finite element package ABAQUS. Considering the spherical symmetry, a geometrical model of one quarter of a circle was constructed and the option of axial symmetry in ABAQUS was used, such that the model represents one half of a spherical particle. The coupled temperature-displacement procedure in ABAQUS/Standard is employed to solve the Li concentration and stress-strain field. The NLGEOM option is used to account for large geometrical changes. The temperature field is used to represent the normalized concentration field, since the governing equations of thermal and mass diffusion are identical. Consequently, the lithiation expansion coefficient $\beta_{ij}$ is equivalent to thermal expansion coefficient. The Li concentration- dependent diffusivity is updated via a user subroutine UMATHT. The volume expansion coefficient was chosen as follows: $\beta_{ij}=0.447$ (when $i=j$) and 0 (otherwise), giving a total volume increase of 280% for fully lithiated Si; and $\beta_{ij}=0.3$ (when $i=j$) and 0 (otherwise), giving a total volume increase of 146% for $SiO_x$, as observed in previous in situ TEM experiments. Young's modulus, Poisson's ratio for pristine Si and fully lithiated Si are taken as 160 GPa, 0.24 and 40 GPa, 0.22, respectively; the corresponding yield stress is 5 and 1 GPa; Young's modulus, Poisson's ratio, and the yield stress of partially lithiated Si are given by linear interpolation between the values of Si and fully lithiated Si. For surface $SiO_x$ and its lithiated product, Young's modulus is taken as 90 GPa, the yield stress is 5 GPa, and Poisson's ratio is 0.17. The Li diffusivity in $SiO_x$ is taken as a constant.

## Supporting Information
Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements
This work was financially supported by the National Key Research and Development Program of China (Grant Nos. 2016YFB0901500 and 2018YFB0905400), the National Natural Science Foundation of China (Grant Nos. 21233004, 21473148, 21621091, 21761132030, and 21703185), and Fundamental Research Funds for the Central Universities (Xiamen University, Grant No. 20720170042). This work was also supported by the US National Science Foundation (Award No. DMR-1410936).

## Conflict of Interest
The authors declare no conflict of interest.

---
Adv. Energy Mater. 2018, 1801718
**1801718 (11 of 12)**
© 2018 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

### Keywords

lithium-ion batteries, nanoparticles, silicon-based composite anodes, solid electrolyte interfaces, surface oxide

Received: June 3, 2018
Revised: July 12, 2018
Published online:

[1] a) J. M. Tarascon, M. Armand, *Nature* **2001**, 414, 359; b) Y. M. Sun, N. Liu, Y. Cui, *Nat. Energy* **2016**, 71, 1; c) W. J. Zhang, *J. Power Sources* **2011**, 196, 13.

[2] a) H. Wu, Y. Cui, *Nano Today* **2012**, 7, 414; b) X. Su, Q. Wu, J. Li, X. Xiao, A. Lott, W. Lu, B. W. Sheldon, J. Wu, *Adv. Energy Mater.* **2014**, 4, 1300882; c) M. Ashuri, Q. He, L. L. Shaw, *Nanoscale* **2016**, 8, 74.

[3] a) L. Liu, J. Lyu, T. Li, T. Zhao, *Nanoscale* **2016**, 8, 701; b) M. A. Rahman, G. Song, A. I. Bhatt, Y. C. Wong, C. Wen, *Adv. Funct. Mater.* **2016**, 26, 647; c) S. D. Beattie, M. J. Loveridge, M. J. Lain, S. Ferrari, B. J. Polzin, R. Bhagat, R. Dashwood, *J. Power Sources* **2016**, 302, 426.

[4] F. Luo, B. Liu, J. Zheng, G. Chu, K. Zhong, H. Li, X. Huang, L. Chen, *J. Electrochem. Soc.* **2015**, 162, A2509.

[5] a) I. H. Son, J. Hwan Park, S. Kwon, S. Park, M. H. Rummeli, A. Bachmatiuk, H. J. Song, J. Ku, J. W. Choi, S. G. Doo, H. Chang, *Nat. Commun.* **2015**, 6, 7393; b) Q. Xu, J. Y. Li, J. K. Sun, Y. X. Yin, L. J. Wan, Y. G. Guo, *Adv. Energy Mater.* **2017**, 7, 1601481; c) W. Ren, Y. Wang, Z. Zhang, Q. Tan, Z. Zhong, F. Su, *J. Mater. Chem. A* **2016**, 4, 552; d) Y. Li, K. Yan, H. W. Lee, Z. Lu, N. Liu, Y. Cui, *Nat. Energy* **2016**, 1, 16017; e) M. G. Jeong, M. Islam, H. L. Du, Y. S. Lee, H. H. Sun, W. Choi, J. K. Lee, K. Y. Chung, H. G. Jung, *Electrochim. Acta* **2016**, 209, 299.

[6] F. M. Hassan, R. Batmaz, J. Li, X. Wang, X. Xiao, A. Yu, Z. Chen, *Nat. Commun.* **2015**, 6, 8597.

[7] X. Han, H. Chen, X. Li, J. Wang, C. Li, S. Chen, Y. Yang, *J. Mater. Chem. A* **2016**, 4, 434.

[8] C. F. Sun, H. Zhu, M. Okada, K. Gaskell, Y. Inoue, L. Hu, Y. Wang, *Nano Lett.* **2015**, 15, 703.

[9] X. Bai, Y. Yu, H. H. Kung, B. Wang, J. Jiang, *J. Power Sources* **2016**, 306, 42.

[10] a) M. T. McDowell, S. W. Lee, I. Ryu, H. Wu, W. D. Nix, J. W. Choi, Y. Cui, *Nano Lett.* **2011**, 11, 4018; b) S. Sim, P. Oh, S. Park, J. Cho, *Adv. Mater.* **2013**, 25, 4498; c) J. Niu, S. Zhang, Y. Niu, H. Song, X. Chen, J. Zhou, B. Cao, *J. Mater. Chem. A* **2015**, 3, 19892; d) Y. Zhang, Y. Li, Z. Wang, K. Zhao, *Nano Lett.* **2014**, 14, 7161.

[11] a) K. W. Schroder, A. G. Dylla, S. J. Harris, L. J. Webb, K. J. Stevenson, *ACS Appl. Mater. Interfaces* **2014**, 6, 21510; b) A. L. Michan, G. Divitini, A. J. Pell, M. Leskes, C. Ducati, C. P. Grey, *J. Am. Chem. Soc.* **2016**, 138, 7918; c) A. L. Michan, M. Leskes, C. P. Grey, *Chem. Mater.* **2016**, 28, 385.

[12] J. Wang, M. Zhou, G. Tan, S. Chen, F. Wu, J. Lu, K. Amine, *Nanoscale* **2015**, 7, 8023.

[13] S. S. Suh, W. Y. Yoon, D. H. Kim, S. U. Kwon, J. H. Kim, Y. U. Kim, C. U. Jeong, Y. Y. Chan, S. H. Kang, J. K. Lee, *Electrochim. Acta* **2014**, 148, 111.

[14] a) F. Somodi, C. S. Kong, J. C. Santos, D. E. Morse, *New J. Chem.* **2015**, 39, 621; b) J. H. Kim, C. M. Park, H. Kim, Y. J. Kim, H. J. Sohn, *J. Electroanal. Chem.* **2011**, 661, 245; c) M. S. Park, E. Park, J. Lee, G. Jeong, K. J. Kim, J. H. Kim, Y. J. Kim, H. Kim, *ACS Appl. Mater. Interfaces* **2014**, 6, 9608.

[15] J. Bae, D. S. Kim, H. Yoo, E. Park, Y. G. Lim, M. S. Park, Y. J. Kim, H. Kim, *ACS Appl. Mater. Interfaces* **2016**, 8, 4541.

[16] a) H. C. Tao, M. Huang, L. Z. Fan, X. Qu, *Solid State Ionics* **2012**, 220, 1; b) M. Li, J. Gu, X. Feng, H. He, C. Zeng, *Electrochim. Acta* **2015**, 164, 163.

[17] a) X. H. Liu, H. Zheng, L. Zhong, S. Huang, K. Karki, L. Q. Zhang, Y. Liu, A. Kushima, W. T. Liang, J. W. Wang, J. H. Cho, E. Epstein, S. A. Dayeh, S. T. Picraux, T. Zhu, J. Li, J. P. Sullivan, J. Cumings, C. Wang, S. X. Mao, Z. Z. Ye, S. Zhang, J. Y. Huang, *Nano Lett.* **2011**, 11, 3312; b) S. Huang, F. Fan, J. Li, S. L. Zhang, T. Zhu, *Acta Mater.* **2013**, 61, 4354; c) J. W. Wang, Y. He, F. Fan, X. H. Liu, S. Xia, Y. Liu, C. T. Harris, H. Li, J. Y. Huang, S. X. Mao, T. Zhu, *Nano Lett.* **2013**, 13, 709; d) J. Wang, H. Luo, Y. Liu, Y. He, F. Fan, Z. Zhang, S. X. Mao, C. Wang, T. Zhu, *Nano Lett.* **2016**, 16, 5815; e) Q. B. Zhang, H. X. Chen, L. L. Luo, B. T. Zhao, H. Luo, X. Han, J. W. Wang, C. M. Wang, Y. Yang, T. Zhu, M. L. Liu, *Energy Environ. Sci.* **2018**, 11, 669.

[18] a) X. H. Liu, F. Fan, H. Yang, S. Zhang, J. Y. Huang, T. Zhu, *ACS Nano* **2013**, 7, 1495; b) M. T. McDowell, S. W. Lee, W. D. Nix, Y. Cui, *Adv. Mater.* **2013**, 25, 4966.

[19] X. H. Liu, L. Zhong, S. Huang, S. X. Mao, T. Zhu, J. Y. Huang, *ACS Nano* **2012**, 6, 1522.

[20] Z. Zeng, N. Liu, Q. Zeng, S. W. Lee, W. L. Mao, Y. Cui, *Nano Energy* **2016**, 22, 105.