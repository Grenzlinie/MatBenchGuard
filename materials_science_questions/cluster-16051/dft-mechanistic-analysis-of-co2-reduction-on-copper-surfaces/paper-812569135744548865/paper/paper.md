![](./images/812569135744548865_1.jpg)

# Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion

Ling-Nan Wu $^{a}$, Zhen-Yu Tian $^{a,b,*}$, Achraf El Kasmi $^{a}$, Muhammad Fahad Arshad $^{a,b}$, Wu Qin $^{c}$

$^{a}$ Institute of Engineering Thermophysics, Chinese Academy of Sciences, 11 Beisihuanxi Rd., Beijing 100190, China
$^{b}$ University of Chinese Academy of Sciences, Beijing 100049, China
$^{c}$ National Engineering Laboratory for Biomass Power Generation Equipment, North China Electric Power University, Beijing 102206, China

Received 7 November 2019; accepted 29 June 2020
Available online xxx

## Abstract

Cu-based oxides oxygen carriers and catalysts are found to exhibit attractive activity for CO oxidation, but the dispute with respect to the reaction mechanism of CO and $O_2$ on the CuO surface still remains. This work reports the kinetic study of CO oxidation on the CuO (111) surface by considering the adsorption, reaction and desorption processes based on density functional theory calculations with dispersion correction (DFT-D). The Eley-Rideal (ER) CO oxidation mechanism was found to be more feasible than the Mars-van-Krevelen (MvK) and Langmuir-Hinshelwood (LH) mechanisms, which is quite different from previous knowledge. The energy barrier of ER, LH, and MvK mechanisms are 0.557, 0.965, and 0.999 eV respectively at 0 K. The energy barrier of CO reaction with the adsorbed O species on the surface is as low as 0.106 eV, which is much more active in reacting with CO molecules than the lattice O of CuO (111) surface (0.999 eV). A comparison with the catalytic activity of the perfect $Cu_2O$ (111) surface shows that the ER mechanism dictates both the perfect $Cu_2O$ (111) and the CuO (111) surface activity for CO oxidation. The activity of the perfect $Cu_2O$ (111) surface is higher than that of the perfect CuO (111) surface at elevated temperatures. A micro-kinetic model of CO oxidation on the perfect CuO (111) surface is established by providing the rate constants of elementary reaction steps in the Arrhenius form, which could be helpful for the modeling work of CO catalytic oxidation.

© 2020 Published by Elsevier Inc. on behalf of The Combustion Institute.

**Keywords**: Density functional theory calculations; CuO (111); CO oxidation; Kinetic model; Surface mechanism

---

* Corresponding authors at: Institute of Engineering Thermophysics, Chinese Academy of Sciences, 11 Beisi-huanxi Rd., Beijing 100190, China.
E-mail addresses: tianzhenyu@iet.cn, tianzhenyu@iet.cn (Z.-Y. Tian).

https://doi.org/10.1016/j.proci.2020.06.376
1540-7489 © 2020 Published by Elsevier Inc. on behalf of The Combustion Institute.

## 1. Introduction

The attractive activity and rich abundance of transition metal oxides make them potential candidates for catalysts in numerous applications [1,2] including chemical looping combustion [1] and CO catalytic oxidation [3-8]. Among them,

![](./images/812569135744548865_2.jpg)

cupric oxide (CuO), with a narrow band gap of about 1.2 to 1.9 eV [9] has gained intensive research attention [9,10]. CuO has shown good catalytic ability for CO oxidation, and it has been recognized to be one of the promising substitutes for the expensive noble metal catalysts [3–5,11]. Unsupported CuO even shows complete CO oxidation activity at room temperature by the controlled generation of the catalyst. The Cu-based oxygen carriers have shown some favorable characteristics over other catalysts. Besides its low cost, CuO has also shown high reactivity in both the oxidation and reduction cycles. The reduction of CuO is favored thermodynamically to realize the complete conversion using gaseous hydrocarbon fuels, and both the reduction and oxidation processes are exothermic [1]. The drawback of CuO catalyst is its tendency to decompose at lower temperatures and the instability after several cycles, which greatly reduces the activity of CuO as the oxygen carrier during the chemical looping combustion process.

The development of CuO as the oxygen carrier relies on a good command of the CO oxidation mechanism on the CuO surface from the microscopic point of view, which is also of significance when Cu-based catalysts are used just as CO-removal catalysts. Besides, redox reactions can shift the valence states of Cu within 0, 1+ and 2+ depending on the reaction gas environment [12]. The surface morphology will also change, accordingly, and it will, in turn, affect the surface catalytic activity for CO oxidation. To reveal the change of surface morphology and catalytic activity, the CO oxidation mechanism on the Cu-based catalysts should be studied comprehensively on both the cuprous oxide (Cu₂O) and CuO surfaces. The study of surface chemistry is of importance for understanding the intrinsic mechanism behind the experimental observations. Theoretical calculations based on density functional theory (DFT) calculations can provide the intrinsic reaction mechanism from the microscopic point of view. Many studies have compared the activities of CuₓO (CuO, Cu₂O, CuₓO) and Cu experimentally [5] and explained the reaction observations according to the Mars-van-Krevelen (MvK) mechanism [4,5]. However, previous studies have reported that the Eley-Rideal (ER) mechanism dictates the CO oxidation process on the Cu₂O (111) surface rather than the MvK mechanism [13,14]. In addition, the Langmuir-Hinshelwood (LH) type CO oxidation mechanism is also faster than the MvK mechanism [13,14]. Meanwhile, the surface adsorbed O species were found to facilitate the CO oxidation processes [15,16], and the surface defects play an important role during the catalytic oxidation process. Therefore, the CO oxidation mechanism on the surface needs to be studied, and the effect of surface defects and adsorbates needs to be addressed. Although much attention has been paid to studying the CO oxidation mechanism on the Cu₂O (111) surface, relatively less efforts have been made to the study of the CO oxidation mechanism on the CuO surface. For CO catalytic oxidation mechanism, several studies have tried to elucidate the CO adsorption and oxidation mechanism on the CuO (111) surface [17,18]. However, to the best of our knowledge, only the reaction between CO and lattice O following the MvK mechanism has been mentioned in the literature [17]. The ER and LH CO oxidation mechanisms on the CuO (111) surface remain unknown. Besides, the DFT results usually provide the reaction energy profile only at 0 K. and a kinetic model is more practical to explain the experimental observations at the actual temperatures in the industry. Thus, it is of interest to study the thorough CO oxidation mechanism considering all the MvK, ER, and LH reaction mechanisms on the CuO (111) surface and develop a kinetic model to describe the reaction process at elevated temperatures.

This work aims to investigate the CO oxidation mechanisms on the CuO (111) surface based on DFT calculations from the microscopic point of view. The MvK, ER, and LH type CO oxidation mechanisms on the CuO (111) surface are explored. The adsorption energy, reaction energy barrier, and reaction energy are calculated. The effect of the surface oxygen defect and the adsorbed atomic oxygen species on the surface are addressed. A kinetic model of CO oxidation on the CuO (111) surface model is provided in the Arrhenius form based on the electronic energies at 0 K and calculated thermodynamic properties at elevated temperatures.

## 2. Computational details

The Grimme DFT long-range dispersion correction (DFT-D) [19] was incorporated in the DFT calculations. Correlation and exchange potential was described by the generalized gradient approximation (GGA) with the Perdew-Burke-Ernzerhof (PBE) method [20]. The inner core electrons were treated by the DFT Semi-core Pseudopots treatment. The Double numerical plus polarization (DNP) basis set was selected. CuO belongs to the monoclinic crystal structure with C2/C symmetry. A 3 × 4 × 2 k-point mesh was used for crystal geometric optimization. The obtained lattice constants are $a=4.669\mathring{A}$, $b=3.553\mathring{A}$, and $c=5.220\mathring{A}$ with the angles $\beta$=93.8° and $\alpha$=$\gamma$=90° For the surface slab, the k-point was tested and a 4 × 3 × 1 Monkhorst-Pack k-point grid was used during energy calculations. A $12\mathring{A}$ vacuum layer was built perpendicular to the surface plane to remove the interference from imaging surface planes. Transition states were first located by a combination of linear synchronous transit (LST) and quadratic synchronous transit (QST) method. The frequencies of the transition states were then calculated. For the transition states with more than one imaginary

Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.org/10.1016/j.proci.2020.06.376

frequency, the eigenvector following method was used to optimize the transition states and guarantee only one imaginary frequency. The validity of the reaction route from an initial state to a final state through the found transition state was confirmed by the nudged elastic band method to make sure no intermediates exist along the reaction pathway.

A proper surface model of CuO is required to represent the CuO surface properties for CO oxi- dation. The CuO (111) surface plane has the low- est surface energy [9], so it has also been widely used as the model surface to study various reac- tion processes on the CuO surface including $H_{2}$ [21,22], water [23], $O_{2}$ adsorption [24], propylene partial oxidation [10], and so on. The CuO (111) surface plane was also used as the model surface of CuO in the previous study of CO heteroge- neous oxidation on the CuO surface [17,18]. There- fore, the dominant CuO (111) surface plane was se- lected to study the CO oxidation processes in the present work. Our previous work has reported the CO oxidation mechanisms on the $Cu_{2} O$ (111) sur face based on standard DFT calculations. As the dispersion correction has been considered in this work, new calculations have been carried out us- ing the DFT-D method and the energy profiles of CO oxidation on the $Cu_{2} O$ (111) surface model are presented for comparison. The rate constants $(k)$ of elementary reaction steps were calculated accord- ing to harmonic transition-state theory (HTST)[14,16,25,26], which is $k=\frac{k_{B} T}{h}(\frac{-\Delta G_{a}}{R T})$ , where $k$ is reaction rate constant, $k_{B}$ is Boltzmann constant, $T$ is temperature, $h$ is Plank constant, $R$ is the uni versal gas constant, $\Delta G_{a}$ is the Gibbs free energy of activation. Detailed calculation process can be found elsewhere [16]. Structure information could be found in the Supplementary Material.

## 3. Results and discussion

### 3.1. CuO (111) surface model and surface properties

The established CuO (111) periodic surface model (shown in Fig. 1a) comprises nine atomic layers, including three copper atomic layers and six oxygen atomic layers. Each copper layer is sand- wiched by two oxygen layers. There are four kinds of top sites on the perfect CuO (111) surface includ- ing the saturated four-fold copper site $(Cu_{CSS})$ , the saturated four-fold oxygen site $(O_{CSS})$ , the unsatu rated three-fold copper site $(Cu_{CUS})$ , and the un saturated three-fold oxygen site $(O_{CUS})$ . The fron tier orbital analysis is provided in Fig. 1b. The sur-face highest occupied molecular orbital (HOMO) is mainly contributed by the surface unsaturated $Cu_{CUS}$ and $O_{CUS}$ sites, and less by the surface sat urated $Cu_{CSS}$ and $O_{CSS}$ sites, implying that the sur face unsaturated sites are more likely to be the ac- tive sites for the electron donating processes.

By comparing the adsorption energies at differ- ent surface sites including the top, bridge, and the hollow sites, the most stable adsorption geometry of CO on the CuO (111) surface model is found as illustrated in Fig. 2a. The surface $Cu_{CUS}$ top site is the most stable adsorption site for CO, and CO is $1.881 \AA$ away from the surface $Cu_{CUS}$ site after adsorption. The bond length of CO remains un- changed after adsorption $(1.142 \AA)$ . The interac tion between the adsorbed CO and the surface is further analyzed by comparing the partial density of states (PDOS) of the $Cu_{CUS}$ sites on the CuO(111) surface and the C of CO before and after ad- sorption in Fig. 2b. The upper part of Fig. 2b an- alyzes the electron states of the $Cu_{CUS}$ on the CuO

![](./images/812569135744548865_3.jpg)

Fig. 1. (a) Structure of CuO (111) surface; (b) HOMO of CuO (111) surface.

Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.org/10.1016/j.proci.2020.06.376

![](./images/812569135744548865_4.jpg)

Fig. 2. (a) Adsorption structures of CO on the perfect CuO (111) surface; (b) PDOS of the C from CO and the $Cu_{CUS}$ site on the CuO (111) surface model.

![](./images/812569135744548865_5.jpg)

Fig. 3. Energy profile of CO oxidation on the CuO (111) surface following MvK, ER, and LH mechanisms.

(111) surface and the C of CO before adsorption. The HOMO of the CO molecule is the $5\sigma$ orbital which could be projected to the hybridization of the 2s and 2p orbitals of C. Below the HOMO is the $1\pi$ orbital and the $4\sigma^{*}$ orbital, which are composed of the 2p and 2s orbitals of C, respectively. For the surface $Cu_{CUS}$ site, the 3d orbital plays the dominant role in its activity.

The bottom part of Fig. 2b shows the PDOS after CO adsorption. A covalent bond is formed with the peak at $-7.3$ eV with the hybridization of the s, p orbitals of the C from adsorbed CO and the s, p, and d orbitals from the surface $Cu_{CUS}$ site. Electron was transferred from the 2s and 2p orbitals to the surface $Cu_{CUS}$ site, and the s and p orbitals of the $Cu_{CUS}$ site are filled, which is in agreement with the Mulliken charge analysis that 0.377 $e$ is transferred to the surface after adsorption. Therefore, the adsorption of CO could proceed in this way with a favorable interaction with the surface $Cu_{CUS}$ site.

### 3.2. MvK, ER, and LH CO oxidation mechanisms

The overall reaction energy profile of CO reaction with lattice $O_{CUS}$ via the MvK, ER, and LH mechanisms is illustrated in Fig. 3. The side-view structures of the initial states (IS), transition states (TS) and final states (FS) are plotted in Fig. 4. Following the MvK mechanism, CO will react directly with the surface lattice O site forming a $CO_{2}$ molecule and an O vacancy. The energy barrier of CO oxidation on the CuO (111) surface via MvK mechanism is 0.999 eV, and the overall reaction energy is $-1.123$ eV

The exothermicity of the ER and the LH mechanisms are the same. The overall heat release of the MvK is smaller than the ER and LH mechanisms. Therefore, the MvK mechanism is less favorable than the ER and LH mechanisms from the thermodynamic point of view. The energy barriers of CO oxidation on the CuO (111) surface following the

Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.org/10.1016/j.proci.2020.06.376

![](./images/812569135744548865_6.jpg)

Fig. 4. Structures of IS, TS, and FS of CO oxidation on the CuO (111) surface model following MvK, ER, and LH mechanisms.

![](./images/812569135744548865_7.jpg)

Fig. 5. Energy profile of $O_{CUS}$-defective surface re-oxidation by $O_2$.

ER and LH mechanisms are 0.557 and 0.965 eV respectively. Therefore, the ER mechanism dominates the CO oxidation process and the ER mechanism is faster than the MvK and LH mechanisms at 0 K.

### 3.3. Reactivity of the defective surface and the role of adsorbed atomic oxygen

The surface defects could be an important factor in affecting the surface activity, so the role of CuO (111) surface defects on the CO oxidation process was discussed in this section The defective surface was created by removing one of the surface outmost $O_{CUS}$ site, and the formed surface $O_{CUS}$ vacancy could be replenished by an oxygen molecule. The energy profile of the reaction between $O_2$ and the surface $O_{CUS}$ vacancy is displayed in Fig. 5. The adsorption of the $O_2$ molecule near the vacancy site releases 1.272 eV, and the adsorbed $O_2$ can readily fix the surface vacancy by overcoming the energy barrier of 0.217 eV. The reaction process is also a strongly exothermic process releasing 0.955 eV. Thus, compared with the process of CO reaction with lattice O, the reaction of the surface re-oxidation process is much faster, and the reaction between CO and lattice O will therefore be the rate-determining step for the CO oxidation following the MvK mechanism on the CuO (111) surface with the energy barrier of 0.999 eV.

The adsorbed species are also of significance during the CO catalytic oxidation process. The effect of adsorbed O on the CO oxidation process is discussed as the adsorbed atomic O could be formed during the CO oxidation process via the MvK, LH, and ER mechanisms as mentioned above. The adsorbed O may also originate from the $O_2$ dissociation on the surface. The energy profile of $O_2$ dissociation on the perfect CuO (111) sur-

---
Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.org/10.1016/j.proci.2020.06.376

![](./images/812569135744548865_8.jpg)

Fig. 6. Energy profile of $O_2$ dissociation on the perfect CuO (111) surface model.

![](./images/812569135744548865_9.jpg)

Fig. 7. Structures of adsorbed O and its reaction energy profiles with CO on the CuO (111) surface.

face is shown in Fig. 6. The adsorption of $O_2$ on
the surface releases 0.725 eV. The energy barrier is
2.253 eV, and the reaction releases 0.756 eV for the
$O_2$ dissociation process with the formation of two
adsorbed atomic oxygen. The adsorbed atomic O
atoms formed in this way are located at the bridge
site of the surface between two neighboring $Cu_{CUS}$
sites. Considering the high energy barrier, the for-
mation of the atomic adsorbed O species by $O_2$
dissociation is less likely to proceed compared with
other possible routes.

Besides the surface bridge adsorption site, one
other possible atomic O adsorption site is also
found on the perfect CuO (111) surface as plotted
in Fig. 7 labled as $O_{ad1}$. The adsorbed O atom in
adsorption structure $O_{ad1}$ is located at the bridge
site between an $O_{CUS}$ site and a $Cu_{CUS}$ site. The
distance between the adsorbed O and the $Cu_{CUS}$
site is $1.909\mathring{A}$ and it is closer to the $O_{CUS}$ site with
$1.435\mathring{A}$. The adsorption energy of the atomic O
in structure $O_{ad1}$ is $-2.601$ eV, which is the smaller
(absolute value) and therefore less stable than the
other case. The adsorbed atomic O in structure $O_{ad2}$
is the same as the atomic O formed by the $O_2$ dis-
sociation process and it has larger adsorption en-
ergy, which corresponds to a more stable adsorp-
tion structure. The distance between the adsorbed
O and the neighboring two $Cu_{CUS}$ sites is $1.850\mathring{A}$

Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction
on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.
org/10.1016/j.proci.2020.06.376

and 1.879 Å, so the adsorbed O is almost in the middle of the two surfaces Cu₍C₎₍U₎₍S₎ sites.

The reactivity of the adsorbed O for CO oxidation is also provided in Fig. 7. For the adsorbed O in structure Oₐd₁, the adsorption energy of CO near the adsorbed O is −0.241 eV, which needs to overcome the energy barrier of 0.243 eV to form a CO₂ molecule. The removal of the CO₂ and the recovery of the surface need the additional energy of 0.397 eV, which is comparable with the adsorption energy of CO on the surface. Therefore, the existence of CO₂ could poison the surface and hinder the CO oxidation process. For Oₐd₂, the CO adsorption process releases 0.277 eV, and the reaction energy barrier between CO and Oₐd₂ is 0.106 eV, which is the lowest among the considered adsorbed O structures. This reaction is also a strongly exothermic process releasing 3.525 eV. The desorption of the adsorbed CO₂ molecule is higher than the other case with 0.451 eV desorption energy.

In retrospect of the reaction energy profiles, the adsorbed atomic O in structure Oₐd₂ is more stable in terms of adsorption energy. The adsorbed atomic O in Oₐd₂ is the most active one in reacting with CO with the energy barrier of 0.106 eV, which is quite easy to proceed, but the removal of the adsorbed CO₂ molecule needs higher energy than the other case. When comparing the activity of the adsorbed atomic O and the lattice O, the activity of the adsorbed atomic O is much more active than the lattice oxygen, so the abundance of surface adsorbed atomic O species should increase the surface activity of CuO (111) surface for CO oxidation. The lattice oxygen is therefore less important than the adsorbed oxygen during the CO oxidation process.

### 3.4. Comparison between the Cu₂O (111) and the CuO (111) surfaces for CO oxidation

The comparison between the activities of the CuO (111) and the Cu₂O (111) surface models for CO oxidation is discussed in this section as the oxidation state of Cu varies with the change of prevailing atmosphere and pressure [4]. The main difference between the Cu₂O (111) and the CuO surface (111) is that there are singly and doubly coordinated Cu sites on the Cu₂O (111) surface model while the CuO (111) surface has three-fold and four-fold Cu sites. The similarity is that both the Cu₂O (111) and CuO (111) surface models have three-fold and four-fold O sites. In terms of coordination number, the Cu₂O (111) surface should have stronger adsorption ability for CO, but the strong bonding between the adsorbed CO and the surface Cu₍C₎₍U₎₍S₎ sites, in turn, may hinder the following reactions.

A comparison between the energy barriers of CO oxidation on the CuO (111) surface model and on the Cu₂O (111) surface model is presented in ![](./images/812569135744548865_10.jpg)

Fig. 8. Comparison between the energy barriers of CO oxidation mechanisms on the CuO (111) and Cu₂O (111) surfaces.

Fig. 8. The energy profile of CO oxidation mechanisms on the Cu₂O (111) surface model including the MvK, ER, and LH mechanisms have been revisited incorporating the Grimme DFT long-range dispersion correction (DFT-D) [19]. A similar trend of the energy barriers of CO oxidation can be seen on both surface models. The ER oxidation mechanism has the lowest energy barrier among the three mechanisms, which is 0.557 eV for the CuO (111) surface and 0.642 eV for the Cu₂O (111) surface. The LH oxidation mechanism is less likely than the ER mechanism but more favorable than the MvK mechanism, and the energy barrier is 0.965 eV for the CuO (111) surface and 1.288 eV for the Cu₂O (111) surface. The MvK mechanism has the lowest possibility for CO oxidation to proceed, and the energy barrier is 0.999 eV and 1.486 eV for the CuO (111) and Cu₂O (111) surface respectively.

### 3.5. Reaction kinetics

The reaction kinetics of elementary reaction steps are analyzed in this part to assess the reaction behaviors at elevated temperatures. Rate constants are summarized in Table 1 in the Arrhenius form. The rate constants of adsorption and desorption processes are also provided. For the non-dissociative adsorption of CO and O₂ on the surface, the Hertz–Knudsen equation [27] is used for calculating the adsorption rate constant of the component i ($k_{\text{ads},i}$) according to $k_{\text{ads},i}=p_{i}(2\pi m_{i}k_{\text{B}}T)^{-1/2}A$ (in s⁻¹), where $p_{i}$ is the partial pressure of component $i$, $m_{i}$ is the mass of a particle, $k_{\text{B}}$ is the Boltzmann constant, $T$ is the temperature, and $A$ is the area of the adsorption surface, $\alpha$ is the sticking coefficient of the gas molecule onto the surface, and it is taken as unity in our study. The pressure of CO and O₂ is selected as 1.01 kPa

Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.org/10.1016/j.proci.2020.06.376

![](./images/812569135744548865_11.jpg)

Fig. 9. Rate constants of CO elementary oxidation steps on the CuO (111) surface. Units are s, mol, cm, cal).

<table>
<caption>Table 1
Reaction rate constants of elementary reaction steps in Arrhenius form. Units are s, mol, cm, cal).</caption>
<thead>
<tr>
<th>No.</th>
<th>A</th>
<th>n</th>
<th>E</th>
</tr>
</thead>
<tbody>
<tr>
<td>CO ads.</td>
<td>$5.425×10^{8}$</td>
<td>−0.502</td>
<td>0.111</td>
</tr>
<tr>
<td>O₂ ads.</td>
<td>$1.014×10^{10}$</td>
<td>−0.502</td>
<td>2.133</td>
</tr>
<tr>
<td>MvK</td>
<td>$4.404×10^{11}$</td>
<td>0.415</td>
<td>22,107</td>
</tr>
<tr>
<td>LH</td>
<td>$1.242×10^{10}$</td>
<td>1.142</td>
<td>21,502</td>
</tr>
<tr>
<td>ER</td>
<td>$3.173×10^{6}$</td>
<td>2.045</td>
<td>12,466</td>
</tr>
<tr>
<td>Oₐd1 + CO</td>
<td>$2.132×10^{5}$</td>
<td>2.984</td>
<td>5467</td>
</tr>
<tr>
<td>Oₐd2 + CO</td>
<td>$4.328×10^{7}$</td>
<td>2.050</td>
<td>2110</td>
</tr>
<tr>
<td>CO₂ des.</td>
<td>$1.086×10^{11}$</td>
<td>1.948</td>
<td>4968</td>
</tr>
</tbody>
</table>

and 20.2 kPa during the calculation. The Cu_CUS site density is calculated to be $9.38×10^{-10}$ based on the CuO (111) surface lattice constant and surface structure. The desorption rate of CO₂ is estimated based on transition state theory.

The reaction rate constants are compared in Fig. 9, which are calculated based on the Gibbs free energy of activation and the transition state theory. At room temperature, the rate constants of MvK, LH, and ER are 0.226, 0.001, 281.185 s⁻¹mol⁻¹cm³, respectively. The reactions between the adsorbed O and CO are fast. The rate constant of Oₐd₂ reacting with CO reaches as high as $1.507×10^{11}$ s⁻¹mol⁻¹cm³ at room temperature, which is quite easy to proceed. Rate constants of MvK, LH, and ER mechanisms increase dramatically with the increase of temperature. The rate constant of the ER mechanism is the fastest, reaching $8.188×10^{9}$ s⁻¹mol⁻¹cm³ at 1000 K, and the rate constant of LH and MvK is similar at 1000 K. Therefore, the ER reaction mechanism dictates the CO oxidation process on the CuO (111) surface. In addition, we have compared the simulated results based on the model proposed in this work and the experiment results of CO oxidation over CuO thin film catalyst. The current model could provide overall satisfactory predictions of the CO conversion curve, and more details could be found in the Supplementary Material.

## 4. Conclusions

The MvK, LH, and ER CO oxidation mechanisms on the perfect CuO (111) surface model were investigated using density functional theory calculations based on the DFT-D calculation scheme. CO oxidation via the ER mechanism has the lowest energy barrier (0.557 eV) at 0 K compared with the MvK and LH mechanisms, which is the most feasible CO oxidation mechanism on the perfect CuO (111) surface. The LH mechanism is faster than the MvK mechanism with the energy barrier of 0.965 eV0. The activity of the adsorbed atomic O species on the perfect CuO (111) surface is much higher than the lattice oxygen in general, so the existence of surface adsorbed O species could promote the CuO (111) surface catalytic activity for CO oxidation. A comparison of the catalytic activity of the perfect CuO (111) and Cu₂O (111) surface models for CO oxidation show that the ER mechanism dominates the CO oxidation process on both surface models, and the ER mechanism on the Cu₂O (111) surface is faster than on the CuO (111) surface at elevated temperatures above 0 K. Therefore, the theoretical results are different from the common belief that CO oxidation on the transition metal oxide surface follows the MvK mechanism. The micro-kinetics of CO oxidation on the CuO (111) surface provides the rate constants of elementary reaction steps in the Arrhenius form, which will be helpful for future modeling work.

Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.org/10.1016/j.proci.2020.06.376

### Declaration of Competing Interest

None.

### Acknowledgments

The authors are grateful for the financial support from the Ministry of Science and Technology of China (2017YFA0402800), Natural Science Foundation of China (No 51976216/51888103) and Recruitment Program of Global Youth Experts. We are thankful to Prof. Yufei Zhao from Beijing University of Chemical Technology for his support in DFT calculations.

### Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.proci.2020.06.376.

### References

[1] M.M. Hossain, H.I. de Lasa, *Chem. Eng. Sci.* 63 (2008) 4433–4451.
[2] J.B. Reitz, E.I. Solomon, *J. Am. Chem. Soc.* 120 (1998) 11467–11478.
[3] J.-L. Cao, G.-S. Shao, Y. Wang, Y. Liu, Z.-Y. Yuan, *Catal. Commun.* 9 (2008) 2555–2559.
[4] T.-J. Huang, D.-H. Tsai, *Catal. Lett.* 87 (2003) 173–178.
[5] U.R. Pillai, S. Deevi, *Appl. Catal. B: Environ.* 64 (2006) 146–151.
[6] Q. Zhang, K. Zhang, D. Xu, et al., *Prog. Mater. Sci.* 60 (2014) 208–337.
[7] H. Huang, L. Zhang, K. Wu, et al., *Nanoscale* 4 (2012) 7832–7841.

[8] K. Zhong, J. Xue, Y. Mao, et al., *RSC Adv.* 2 (2012) 11520–11528.
[9] J. Hu, D. Li, J.G. Lu, R. Wu, *J. Phys. Chem. C* 114 (2010) 17120–17126.
[10] Y.-Y. Song, G.-C. Wang, *J. Phys. Chem. C* 120 (2016) 27430–27442.
[11] B. Wei, N. Yang, F. Pang, J. Ge, *J. Phys. Chem. C* 122 (2018) 19524–19531.
[12] Y. Maimaiti, M. Nolan, S.D. Elliott, *Phys. Chem. Chem. Phys.* 16 (2014) 3036–3046.
[13] B.-Z. Sun, W.-K. Chen, Y.-J. Xu, *J. Chem. Phys.* 133 (2010) 154502.
[14] L.-N. Wu, Z.-Y. Tian, W. Qin, *Int. J. Chem. Kinet.* 50 (2018) 507–514.
[15] A. El Kasmi, Z.-Y. Tian, H. Vieker, A. Beyer, T. Chafik, *Appl. Catal. B: Environ.* 186 (2016) 10–18.
[16] L.-N. Wu, Z.-Y. Tian, W. Qin, *J. Phys. Chem. C* 122 (2018) 16733–16740.
[17] H.-F. Wang, R. Kavanagh, Y.-L. Guo, Y. Guo, G. Lu, P. Hu, *J. Catal.* 296 (2012) 110–119.
[18] B.-X. Yang, L.-P. Ye, H.-J. Gu, J.-H. Huang, H.-Y. Li, Y. Luo, *J. Mol. Model.* 21 (2015) 195.
[19] S. Grimme, *J. Comput. Chem.* 27 (2006) 1787–1799.
[20] J.P. Perdew, K. Burke, M. Ernzerhof, *Phys. Rev. Lett.* 77 (1996) 3865–3868.
[21] G. Hao, R. Zhang, J. Li, B. Wang, Q. Zhao, *Comput. Mater. Sci.* 122 (2016) 191–200.
[22] G. Hao, R. Zhang, J. Li, B. Wang, Q. Zhao, *Comput. Mater. Sci.* 122 (2016) 191–200.
[23] X. Yu, X. Zhang, H. Wang, G. Feng, *Appl. Surf. Sci.* 425 (2017) 803–810.
[24] S. Sun, C. Li, D. Zhang, Y. Wang, *Appl. Surf. Sci.* 333 (2015) 229–234.
[25] G.H. Vineyard, *J. Phys. Chem. Solids* 3 (1957) 121–127.
[26] W. Piskorz, F. Zasada, P. Stelmachowski, O. Diwald, A. Kotarba, Z. Sojka, *J. Phys. Chem. C* 115 (2011) 22451–22460.
[27] K.W. Kolasinski, *Surface Science: Foundations of Catalysis and Nanoscience*, 3rd Edition ed., Wiley, 2012.

Please cite this article as: L.-N. Wu, Z.-Y. Tian and A. El Kasmi et al., Mechanistic study of the CO oxidation reaction on the CuO (111) surface during chemical looping combustion, Proceedings of the Combustion Institute, https://doi.org/10.1016/j.proci.2020.06.376