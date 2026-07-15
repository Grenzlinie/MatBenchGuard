**Article**

# Systematic Exploration of the Interactions between Pyrite and Coal from the View of Density Functional Theory

Peng Xi $^{1,2}$, Fengling Sun $^{1}$, Xiaoyu Tang $^{1}$, Xiaoping Fan $^{1,2}$, An Lu $^{3}$, Kaifei Lu $^{4,*}$ and Qiming Zhuo $^{5,*}$

1.  School of Chemical Safety, North China Institute of Science and Technology, Beijing 101601, China; pengxi@ncist.edu.cn (P.X.); sunfengling@ncist.edu.cn (F.S.); temic0315@163.com (X.T.); fanxp6566203@163.com (X.F.)
2.  Hebei Key Laboratory of Hazardous Chemicals Safety and Control Technology, North China Institute of Science and Technology, Beijing 101601, China
3.  Key Laboratory of Power Machinery and Engineering of Ministry of Education, Shanghai Jiao Tong University, Shanghai 200240, China; anl0203@sjtu.edu.cn
4.  Department of Student Affairs, Beijing Institute of Economics and Management, Beijing 100102, China
5.  School of Chemical and Environmental Engineering, China University of Mining and Technology (Beijing), Beijing 100083, China
*Correspondence: kaifeilu@biem.edu.cn (K.L.); zhuoqiming92@126.com (Q.Z.); Tel.: +86-187-0152-6695 (K.L.)

**Abstract:** Coal is often adhered to by pyrite during slime flotation, causing an increase in the sulfur content of clean coal. In order to study the mechanism of pyrite adhesion to coal surfaces, different coal structural units were built and optimized, and the most stable adsorption model of them on pyrite surfaces was determined. The mechanism of pyrite particles adhering to the surface of coal slurries was explored with the method of DFT. The results showed that the interaction mechanism between pyrite surface and Ph-OH and Ph-O-CH₃ was the result of a weak interaction between the H atom of Ph-OH and Ph-O-CH₃ and the S atom of the pyrite surface. The interaction mechanism between the pyrite surface and Ph-COOH and Ph-CO-CH₃ was both as a result of H-S interactions and weak Fe-O interactions. On the whole, there were weak interactions between pyrite particles and the coal slurry, and the pyrite particles can spontaneously adsorb on the surface of the coal slurry.

**Keywords:** interaction; pyrite; coal; density functional theory; desulfurization

![](./images/1047364490682695686_1.jpg)

Citation: Xi, P.; Sun, F.; Tang, X.; Fan, X.; Lu, A.; Lu, K.; Zhuo, Q. Systematic Exploration of the Interactions between Pyrite and Coal from the View of Density Functional Theory. Processes 2024, 12, 2125. https://doi.org/10.3390/pr12102125

Academic Editor: Haibin Zuo

Received: 17 August 2024
Revised: 17 September 2024
Accepted: 25 September 2024
Published: 29 September 2024

![](./images/1047364490682695686_2.jpg)

Copyright: © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

Sulfur causes great harm to the ecological environment; human health; and the quality of coke, steel, and other industrial products during the utilization of coal. Therefore, it is of great practical significance to efficiently remove sulfur from coal [1]. With the widespread application of mechanized coal mining and the continuous deterioration of coal’s geological conditions, a large amount of high-sulfur coal slime, most of which is pyrite sulfur, is produced. The pyrite with a fine particle size that is embedded in high-sulfur coal slime is generally removed by economic and effective flotation methods [2].

Many coal flotation practices of high-sulfur slime have found that there is a large amount of undissolved pyrite in clean coal subjected to conventional flotation [3]. Due to inadequate dissociation, the pyrite floats up with symbiotic coal, turning into clean coal. The combined desulfurization process of grinding and flotation lead to the discovery that the surface of the fresh pyrite itself is hydrophilic, but a large amount of obviously dissociated pyrites enter the foam layer. A large number of studies believe that the coal-pyrite particles undergo electrochemical oxidation on the surface to generate hydrophobic substances during coal mining, transportation, and washing, and then directly attach to the bubbles. Through experimental methods, Zhu [4] and R.H. Yoon [5] found that the sulfide FeSₓ and sulfur-rich layer formed on the pyrite surface caused the surface to be hydrophobic. Niu [6] found that at low pH, the oxidation product of pyrite—sulfur—accounted for a large proportion, with greater hydrophobicity and floatability. Using the

Processes 2024, 12, 2125. https://doi.org/10.3390/pr12102125  https://www.mdpi.com/journal/processes

first-principles method of DFT, the previous study [7] found that a weak Fe-S-O bond was formed between the iron atom, the oxidized sulfur, and water molecules instead of the strong Fe-O bond formed on ideal surfaces. Some studies thought that the symbiotic coal or the carbon defect existing in the lattice had an important effect on the hydrophobicity of pyrite. Z. Çetinkaya [8] combined bioleaching and chemical experiments to eliminate sulfur from Sivas Kangal lignite coal, and obtained clean coal with 2.89% total sulfur content. F. H. Channa [9] obtained a desulfurization rate of about 77.01% utilizing Hardgrove grinding and taking advantage of the large differences in hardness and grindability. There was still some dissociated pyrite that entered the clean coal because of the symbiotic coal. Cao [3] found that it was difficult to observe the monomer-dissociated pyrite in the flotation concentrate; pyrites only float when they coexist with coal. Previous studies [10-13] have found that the symbiotic coal transformed coal pyrite to hydrophobic from hydrophilic, and the carbon defect enhanced its hydrophobicity according to DFT calculations. Other studies have reported that coal-pyrites were mainly entrained into the foam product by water. S. K. Kawatra found [14,15] that the fresh monomer-dissociated coal-pyrite mainly entered into the flotation concentrate due to water entrainment and mechanical entrainment, and its internal surface hydrophobicity was not the main reason. The above studies explored the mechanism of coal-pyrite entering flotation concentrate from four perspectives—the hydrophobicity of the coal-pyrite surface, symbiosis with coal, entrainment, and surface oxidation. However, it has not been reported how the completely dissociated fine-grained coal-pyrite captures hydrophobic coal particles in a manner that is as non-selective as fine-grained clay minerals; that is, the interaction mechanism between fine-grained pyrite particles and coal particles has not been reported.

With the development of modern physical technology, advanced modern analytical techniques have greatly facilitated the study of the interaction between minerals, but the microscopic mechanism of the interaction between minerals has not been explored at the molecular/atomic level. The first-principles calculation method based on density functional theory has been widely used in mineral processing, and can reveal the interaction mechanism between small molecules and minerals at the atomic and molecular level. Using DFT-D+U, Mkhonto [16,17] found that the covalent bonding was formed by the reaction between the trithiocarbonate benzothiazole/benzoxazole/benzimidazole S atoms and the Fe atoms of the pyrite surface. Liu [18,19] confirmed that $\mathrm{H_2O}$ molecules tend to adsorb on the Fe atoms more than on the Cu atoms of the chalcopyrite surface, and found that the chemical adsorption of sodium di(isobutyl) dithiophosphinate (3418A) on the chalcopyrite surface is stronger than that of dibutyl dithiophosphate (DTP), according to DFT calculations. Zhang [20] found that the newly developed parameter set achieved a good balance between computational accuracy and efficiency between typical lead minerals and flotation reagents according to self-consistent-charge density functional tight-binding (SCC-DFTB) theory. Feng [21] calculated the synergistic adsorption of ethyl xanthate and butyl xanthate on pyrite surfaces using DFT and found that the interaction between them had a stronger effect than that of a single reagent. Chen [22] calculated the adsorption of quaternary phosphorus salts on the kaolinite (001) surface and found that quaternary phosphorus salts formed C-H$\cdots$O hydrogen bonds.

Therefore, this paper intends to study the agglomeration behavior of fine-grained pyrite and coal particles from the perspective of the fine-grained pyrite cover in the slime flotation process leading to an increase in the sulfur content of the concentrate. Different coal structural units were built and optimized, and the adsorption configuration of coal structural units on pyrite surfaces was calculated, including the frontier orbital, adsorption energy, bonding analysis, charge transfer, Density of States (DOS), and band structure, using the method of DFT simulation.

## 2. Calculation Methods and Model

### 2.1. The Frontier Orbital Calculation

To determine the frontier orbital characteristics of refined models of pyrite (100) surface and coal structural units, the Dmol³ module was employed, involving energy optimization. The Brillouin zone's k-point sampling utilized the gamma point method. The calculation of exchange-correlation energy relied on the GGA-PW91 functional, while core electrons were treated with Effective Core Potentials, and a DNP basis set was employed. The calculations were performed with high precision, and the self-consistent field convergence criterion was set to $1.0 \times 10^{-6}$ eV/atom.

### 2.2. DFT Calculation

An in-depth exploration into the adsorption behavior of coal structural units onto pristine pyrite (100) surfaces was conducted employing density functional theory (DFT) methodology. This comprehensive analysis leveraged the advanced CASTEP program, integrated within Materials Studio 2018 software, to ensure precise and accurate calculations throughout the entire study.

The exchange-correlation interactions among electrons were modeled using the Generalized Gradient Approximation—Perdew Wang 91 (GGA-PW91) [23,24]. The calculation focused on valence electrons (Fe $3\text{d}^{6}4\text{s}^{2}$ and S $3\text{s}^{2}3\text{p}^{4}$) through the use of ultra-soft pseudopotentials [25]. A plane wave cut-off energy of 350 eV [26] was employed, and a Monkhorst-Pack [27,28] k-point grid of $4 \times 4 \times 4$ was utilized. Convergence for the self-consistent field (SCF) was achieved with a precision of $2.0 \times 10^{-6}$ eV per atom. Spin polarization was included in the simulation. Additionally, the structural units of coal were optimized within a cubic cell of $20 \times 20 \times 20$ Å, with Brillouin zone sampling limited to the gamma point, as depicted in Figure 1. All other parameters matched those used for the optimization of the primitive unit cell.

![](./images/1047364490682695686_3.jpg)

Figure 1. The model of coal oxygenated structural units. (a) Ph-OH; (b) Ph-COOH; (c) Ph-C=O; (d) Ph-O-.

The adsorption energy, which measures the interaction between the coal structural units (adsorbate) and the pyrite surface, can be assessed as follows:

$$\mathrm{E_{ads} = E_{X/slab} - E_X - E_{slab}} \tag{1}$$

In the given context, $\mathrm{E_{ads}}$ represents the adsorption energy, and X denotes the coal structural unit. The term $\mathrm{E_{X/slab}}$ refers to the energy of the pyrite surface with the adsorbed coal structural units. $\mathrm{E_{slab}}$ and $\mathrm{E_X}$ are the energies of the pyrite surface and the coal structural units, respectively. A negative value for $\mathrm{E_{ads}}$ indicates an exothermic process, with a larger magnitude of $|\mathrm{E_{ads}}|$ signifying the increased stability of the adsorbed structure [29–31].

## 3. Results and Discussion

### 3.1. Frontier Orbital Analysis

The local position activity was analyzed using frontier orbitals (HOMO and LUMO). The regions with the highest HOMO distribution were prone to protonation reactions, while those with the largest LUMO distribution were more likely to undergo deprotonation.

As an example, the formation of the pyrite surface was examined [10-13]. To explore the interaction between coal and pyrite, we calculated the frontier orbital energies for the structural units of both coal and pyrite, as well as their energy differences. The results are presented in Table 1.

Table 1. The frontier orbital energies of coal structural units and pyrite.

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="2">Frontier Orbital Energy/eV</th>
<th colspan="2">Frontier Orbital Energy Difference/eV</th>
</tr>
<tr>
<th>HOMO</th>
<th>LUMO</th>
<th>$\Delta E_{1}$</th>
<th>$\Delta E_{2}$</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">Coal structural units</td>
<td>Ph-OH</td>
<td>−5.692</td>
<td>−2.656</td>
<td>3.023</td>
<td>1.232</td>
</tr>
<tr>
<td>Ph-COOH</td>
<td>−5.371</td>
<td>−1.030</td>
<td>4.649</td>
<td>0.911</td>
</tr>
<tr>
<td>Ph-C=O</td>
<td>−5.390</td>
<td>−1.027</td>
<td>4.652</td>
<td>0.930</td>
</tr>
<tr>
<td>Ph-O-</td>
<td>−6.361</td>
<td>−2.388</td>
<td>3.291</td>
<td>1.901</td>
</tr>
<tr>
<td>Pyrite</td>
<td></td>
<td>−5.679</td>
<td>−4.460</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Note: $\Delta E_{1} = \left| E_{HOMO}^{surface} - E_{LUMO}^{adsorbate} \right|$, $\Delta E_{2} = \left| E_{HOMO}^{adsorbate} - E_{LUMO}^{surface} \right|$, where $E_{HOMO}^{surface}$ and $E_{LUMO}^{surface}$ are the HOMO and LUMO energies of the surface, respectively; $E_{HOMO}^{adsorbate}$ and $E_{LUMO}^{adsorbate}$ are the HOMO and LUMO energies of different oxygen structural units, respectively.

Based on the differences in the frontier orbital energies between various coal structural units and the pyrite surface listed in Table 1, it was observed that the frontier orbital energy difference $\Delta E_{2}$ for all coal structural units relative to pyrite was consistently smaller than $\Delta E1$. This suggests that the LUMO orbitals of the coal structural units are more likely to interact with the HOMO orbitals of pyrite. Additionally, the values of $\Delta E_{2}$ for different coal structural units showed an increasing trend, whereby Ph-COOH < Ph-C=O < Ph-OH < Ph-O-. This trend implies a progressive decrease in the reactivity of the HOMO orbitals of the coal structural units (Figure 2).

![](./images/1047364490682695686_4.jpg)

Figure 2. The frontier orbitals of coal structural units. (a) Ph-OH; (b) Ph-COOH; (c) Ph-C=O; (d) Ph-O-.

### 3.2. DFT Calculation

To explore how coal interacts with pyrite during the slime flotation process, density functional theory (DFT) calculations were employed to study the adsorption of various oxygen-containing structural units on pyrite surfaces. This involved determining the

equilibrium adsorption configurations, calculating adsorption energies, and analyzing charge transfer and Mulliken charge populations to better understand the interaction mechanism between pyrite and coal.

### 3.2.1. Adsorption Configurations and Adsorption Energy

The equilibrium adsorption configurations and adsorption energies of various coal structural units on different sites of the pyrite (100) surface were analyzed. Table 2 displays the adsorption energies (Eads) for these coal structural units on the pyrite surface, while Figure 3 illustrates the most stable equilibrium adsorption configurations. In the figure, the numbers indicate the distances between the bonding atoms, measured in angstroms (Å).

Table 2. The adsorption energy, $\text{E}_{\text{ads}}$, for coal structural units on the pyrite surface.

<table>
<thead>
<tr>
<th>Coal Structural Units</th>
<th>$\text{E}_{\text{ads}}$/kJ·mol⁻¹</th>
<th>Adsorption Configuration of Coal Structural Units</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">Ph-OH/FeS₂</td>
<td>24.90</td>
<td>F</td>
</tr>
<tr>
<td>24.82</td>
<td>P</td>
</tr>
<tr>
<td>2.84</td>
<td>LPS</td>
</tr>
<tr>
<td>1.85</td>
<td>HPS</td>
</tr>
<tr>
<td rowspan="4">Ph-COOH/FeS₂</td>
<td>−23.57</td>
<td>F</td>
</tr>
<tr>
<td>14.46</td>
<td>P</td>
</tr>
<tr>
<td>−62.19</td>
<td>LPS</td>
</tr>
<tr>
<td>−1.99</td>
<td>HPS</td>
</tr>
<tr>
<td rowspan="4">Ph-CO-CH₃/FeS₂</td>
<td>−25.39</td>
<td>F</td>
</tr>
<tr>
<td>7.40</td>
<td>P</td>
</tr>
<tr>
<td>−10.77</td>
<td>LPS</td>
</tr>
<tr>
<td>7.92</td>
<td>HPS</td>
</tr>
<tr>
<td rowspan="4">Ph-O-CH₃/FeS₂</td>
<td>42.49</td>
<td>F</td>
</tr>
<tr>
<td>42.55</td>
<td>P</td>
</tr>
<tr>
<td>25.82</td>
<td>LPS</td>
</tr>
<tr>
<td>1.9</td>
<td>HPS</td>
</tr>
</tbody>
</table>

Note: For ease of reference, the following symbols denote different configurations for the initial adsorption sites of coal structural units: "F" signifies a position above the Fe atom, "P" indicates that the plane of the benzene ring is perpendicular to the pyrite surface, "HPS" denotes a site above the high-position S atom, and "LPS" represents a site above the low-position S atom.

For Ph-OH, the $\text{E}_{\text{ads}}$ on the HPS sites of the pyrite surface was 1.85 kJ/mol, smaller than F, P, and LPS, which demonstrated that the former adsorption configuration was most stable. The $\text{E}_{\text{ads}}$ values of Ph-COOH on different sites of the pyrite surface were −23.57, 14.46, −62.19, and −1.99 kJ/mol. The $\text{E}_{\text{ads}}$ values on LPS sites were the smallest, and their adsorption configuration was the most stable, as shown in Figure 3b. The smallest $\text{E}_{\text{ads}}$ value of Ph-CO-CH₃ on different sites of the pyrite surface was −25.39 kJ/mol, whose adsorption configuration is shown in Figure 3c. The smallest $\text{E}_{\text{ads}}$ value of Ph-O-CH₃ on different sites of the pyrite surface was −1.90 kJ/mol, which was very close to the results of Ph-OH. It demonstrated that the adsorption of Ph-O-CH₃ was as stable as that of Ph-OH. The physical adsorption strength of different coal structural units on the pyrite surface decreased from Ph-COOH, Ph-CO-CH₃, and Ph-OH to Ph-O-CH₃, whose results were the same as the frontier orbital energies of coal structural units and pyrite. From the macroscopic view, although the pyrite surface was hydrophobic and difficult to float itself during the slime flotation, the fine pyrite particles can adhere to the surface of coal particles and float upwards.

![](./images/1047364490682695686_5.jpg)

Figure 3. Adsorption configurations of different coal structural units on the pyrite (100) surface.
((a) Ph-OH; (b) -COOH; (c) -C=O; (d) -O-).

### 3.2.2. Analysis of Bonding
Furthermore, taking the most stable adsorption configurations as the objects of study, we further calculated the Mulliken population [32] and length between different coal structural units and the pyrite (100) surface, as shown in Table 3.

<table>
<caption>Table 3. Mulliken population and length of different coal structural units.</caption>
<thead>
<tr>
<th>Adsorption Model</th>
<th>Interaction</th>
<th>Population</th>
<th>Length/Å</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ph-OH/FeS₂</td>
<td>H-S</td>
<td>0.00</td>
<td>2.990</td>
</tr>
<tr>
<td rowspan="2">Ph-COOH/FeS₂</td>
<td>H-S</td>
<td>0.05</td>
<td>2.475</td>
</tr>
<tr>
<td>Fe-O</td>
<td>0.13</td>
<td>2.797</td>
</tr>
<tr>
<td rowspan="2">Ph-CO-CH₃/FeS₂</td>
<td>Fe-O</td>
<td>0.13</td>
<td>2.820</td>
</tr>
<tr>
<td>H-S</td>
<td>0.00</td>
<td>2.895</td>
</tr>
<tr>
<td rowspan="2">Ph-O-CH₃/FeS₂</td>
<td>H-S</td>
<td>−0.01</td>
<td>2.597</td>
</tr>
<tr>
<td>H-S</td>
<td>0.00</td>
<td>2.595</td>
</tr>
</tbody>
</table>

For Ph-OH and Ph-O-CH₃, the Mulliken population between both the S atom of the pyrite (100) surface and the H atom of the hydroxyl group or ether bond on the benzene ring was 0.00, and the bond lengths were long. There was no bond and even no interaction formed between the H atom and the S atom. It illustrated that there was almost no interaction between Ph-OH, Ph-O-CH₃, and the pyrite (100) surface, and even the interaction was repulsive. The adsorption of Ph-OH and Ph-O-CH₃ on the pyrite (100) surface will not occur during the process of coal flotation desulfurization.

For Ph-COOH and Ph-CO-CH₃, the Mulliken population between both the Fe atom of the pyrite surface and the O atom of the carboxyl or carbonyl group on the benzene ring was 0.13, and a weak interaction between the Fe atom and the O atom was formed. In addition, the S of the pyrite surface also interacted with the H of the hydroxyl group or carbonyl on the benzene ring, and a weaker H-S interaction was formed. However, the population between the S atom and the H atom of Ph-COOH was 0.05, which was bigger

than that of Ph-CO-CH₃. This illustrated that there was a weak interaction between Ph-COOH, Ph-CO-CH₃, and the pyrite surface. The adsorption of Ph-COOH and Ph-CO-CH₃ on the pyrite (100) surface will occur during the process of coal flotation desulfurization, and the adsorption of Ph-COOH on the pyrite (100) surface was more stable. This may be due to a physical adsorption between the adsorbate and the adsorbent.

As such, this demonstrated that the coal units can adsorb on the pyrite surface and the coal-pyrite interactions are a physical adsorption. It was more difficult for Ph-OH and Ph-O-CH₃ than Ph-COOH and Ph-CO-CH₃ to adsorb on the pyrite (100) surface, which is consistent with the adsorption energy results. The fresh monomer-dissociated coal-pyrite will enter into the flotation concentrate during the process of coal flotation desulfurization due to the interaction between coal and pyrite.

### 3.2.3. Charge Transfer
The Mulliken charge population (MCP) [33] refers to the loss and transfer of electrons between the atoms interacting with each other. The MCP results before (B) and after (A) adsorption of different coal structural units on the pyrite (100) surface are shown in Table 4.

Table 4. MCP of the bonding atoms between different coal structural units and the pyrite (100) surface.

<table>
<thead>
  <tr>
    <th>Adsorption Model</th>
    <th>Atomic Label</th>
    <th>Adsorption Status</th>
    <th>s</th>
    <th>p</th>
    <th>d</th>
    <th>Total</th>
    <th>Charge/e</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="4">Ph-OH/FeS₂</td>
    <td rowspan="2">H</td>
    <td>B</td>
    <td>0.46</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.46</td>
    <td>0.54</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0.48</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.48</td>
    <td>0.52</td>
  </tr>
  <tr>
    <td rowspan="2">S</td>
    <td>B</td>
    <td>1.86</td>
    <td>4.26</td>
    <td>0.00</td>
    <td>6.12</td>
    <td>−0.11</td>
  </tr>
  <tr>
    <td>A</td>
    <td>1.86</td>
    <td>4.26</td>
    <td>0.00</td>
    <td>6.12</td>
    <td>−0.11</td>
  </tr>
  <tr>
    <td rowspan="8">Ph-COOH/FeS₂</td>
    <td rowspan="2">H</td>
    <td>B</td>
    <td>0.44</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.44</td>
    <td>0.55</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0.52</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.52</td>
    <td>0.48</td>
  </tr>
  <tr>
    <td rowspan="2">S</td>
    <td>B</td>
    <td>1.84</td>
    <td>4.26</td>
    <td>0.00</td>
    <td>6.12</td>
    <td>−0.12</td>
  </tr>
  <tr>
    <td>A</td>
    <td>1.82</td>
    <td>4.19</td>
    <td>0.00</td>
    <td>6.01</td>
    <td>−0.01</td>
  </tr>
  <tr>
    <td rowspan="2">Fe</td>
    <td>B</td>
    <td>0.35</td>
    <td>0.44</td>
    <td>7.14</td>
    <td>7.93</td>
    <td>0.07</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0.34</td>
    <td>0.44</td>
    <td>7.12</td>
    <td>7.90</td>
    <td>0.10</td>
  </tr>
  <tr>
    <td rowspan="2">O</td>
    <td>B</td>
    <td>1.82</td>
    <td>4.74</td>
    <td>0.00</td>
    <td>6.56</td>
    <td>−0.57</td>
  </tr>
  <tr>
    <td>A</td>
    <td>1.82</td>
    <td>4.72</td>
    <td>0.00</td>
    <td>6.54</td>
    <td>−0.54</td>
  </tr>
  <tr>
    <td rowspan="8">Ph-CO-CH₃/FeS₂</td>
    <td rowspan="2">H</td>
    <td>B</td>
    <td>0.66</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.66</td>
    <td>0.33</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0.72</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.72</td>
    <td>0.27</td>
  </tr>
  <tr>
    <td rowspan="2">S</td>
    <td>B</td>
    <td>1.86</td>
    <td>4.26</td>
    <td>0.00</td>
    <td>6.12</td>
    <td>−0.11</td>
  </tr>
  <tr>
    <td>A</td>
    <td>1.86</td>
    <td>4.24</td>
    <td>0.00</td>
    <td>6.08</td>
    <td>−0.09</td>
  </tr>
  <tr>
    <td rowspan="2">Fe</td>
    <td>B</td>
    <td>0.35</td>
    <td>0.44</td>
    <td>7.14</td>
    <td>7.93</td>
    <td>0.07</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0.34</td>
    <td>0.44</td>
    <td>7.12</td>
    <td>7.90</td>
    <td>0.10</td>
  </tr>
  <tr>
    <td rowspan="2">O</td>
    <td>B</td>
    <td>1.82</td>
    <td>4.70</td>
    <td>0.00</td>
    <td>6.52</td>
    <td>−0.52</td>
  </tr>
  <tr>
    <td>A</td>
    <td>1.82</td>
    <td>4.68</td>
    <td>0.00</td>
    <td>6.50</td>
    <td>−0.49</td>
  </tr>
  <tr>
    <td rowspan="4">Ph-O-CH₃/FeS₂</td>
    <td rowspan="2">H</td>
    <td>B</td>
    <td>0.68</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.68</td>
    <td>0.31</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0.78</td>
    <td>0.00</td>
    <td>0.00</td>
    <td>0.78</td>
    <td>0.23</td>
  </tr>
  <tr>
    <td rowspan="2">S</td>
    <td>B</td>
    <td>1.86</td>
    <td>4.26</td>
    <td>0.00</td>
    <td>6.12</td>
    <td>−0.11</td>
  </tr>
  <tr>
    <td>A</td>
    <td>1.86</td>
    <td>4.26</td>
    <td>0.00</td>
    <td>6.12</td>
    <td>−0.11</td>
  </tr>
</tbody>
</table>

For Ph-OH and Ph-O-CH₃, the H 1s orbit of the former obtained 0.02 e, and the latter obtained 0.10 e. The S 3p orbit of the pyrite surface had no change. A weak H-S bond was formed after adsorption on the pyrite surface. After Ph-COOH and Ph-CO-CH₃ adsorbed on the pyrite surface, the O 2p orbit of them lost 0.02 e and the Fe 3d of the pyrite surface lost 0.03 e, with a strong Fe-O bond being formed. Meanwhile, the H 1s orbit of Ph-COOH and Ph-CO-CH₃ obtained 0.08 e and 0.06 e, respectively. The S 3p orbit of the pyrite surface each lost 0.11 e and 0.04 e; a weak H-S bond was also formed after adsorption (Figure 4).

![](./images/1047364490682695686_6.jpg)

Figure 4. Electron density and charge density difference map after different coal structural units adsorption on the pyrite (100) surface: ((a) Ph-OH; (b) -COOH; (c) -C=O; (d) -O-).

### 3.2.4. Density of States (DOS) and Band Structure

For Ph-OH and Ph-O-CH₃, the interaction between the coal units and the pyrite surface primarily involved the H atom of the coal units and the S atom of the pyrite. Consequently, the Partial Density of States (PDOS) for the H and S atoms was plotted before and after adsorption, as shown in Figure 5a,d. In contrast, for Ph-COOH and Ph-CO-CH₃, the interaction was mainly between the O atoms of the coal units and the Fe atoms of the pyrite surface, as illustrated in Figure 5b,c. Thus, the Density of States (DOS) for the O and Fe atoms was analyzed before and after adsorption, with the Fermi level (Ef) set at 0 eV. For Ph-OH and Ph-O-CH₃, there was minimal change in the DOS of H 1s and S 2p, indicating a weak interaction between these units and the pyrite surface. However, Ph-COOH and Ph-CO-CH₃ showed slight changes in the DOS of O 2s and S 3p, with interaction energy between O and Fe ranging from 5 eV to 15 eV. These findings are consistent with the charge transfer and Mulliken population results.

From the band structure after different coal structural units adsorption on the pyrite (100) surface in Figure 6, for Ph-OH, Ph-O-CH₃, Ph-COOH, and Ph-CO-CH₃, the band gaps were very close, at around 0.670 eV, from 0.664 eV, 0.675 eV, and 0.673 eV to 0.671 eV. The band structure showed an extremely large energy range, in which all bands looked pretty flat. These findings were consistent with the DOS results (Figure 5).

![](./images/1047364490682695686_7.jpg)

![](./images/1047364490682695686_8.jpg)

![](./images/1047364490682695686_9.jpg)

![](./images/1047364490682695686_10.jpg)

Figure 5. Density of States (DOS) before and after different coal structural units adsorption on the pyrite (100) surface: ((a) Ph-OH; (b) -COOH; (c) -C=O; (d) -O-).

![](./images/1047364490682695686_11.jpg)

(a) Band gap is 0.664 eV

![](./images/1047364490682695686_12.jpg)

(b) Band gap is 0.673 eV

Figure 6. Cont.

![](./images/1047364490682695686_13.jpg)

(c) Band gap is 0.671 eV

![](./images/1047364490682695686_14.jpg)

(d) Band gap is 0.675 eV

Figure 6. Band structure after different coal structural units adsorption on the pyrite (100) surface: ((a) Ph-OH; (b) -COOH; (c) -C=O; (d) -O-.

## 4. Conclusions

The entrainment mechanism of fine pyrite into clean coal was studied from the view of quantum chemistry by simulating the adsorption process of the coal structural units on the pyrite surface.

(1) After the coal structural units were adsorbed on the pyrite surface, the $E_{\text{ads}}$ value of Ph-OH and Ph-O-CH₃ was positive and the $E_{\text{ads}}$ value of Ph-COOH and Ph-CO-CH₃ was negative, which implied an endothermic reaction and an exothermic reaction. The adsorption energy of different coal structural units on the pyrite surface decreased from Ph-COOH, Ph-CO-CH₃, and Ph-OH to Ph-O-CH₃. The physical adsorption stability of different coal structural units on the pyrite surface decreased.

(2) The interaction between the Ph-OH and Ph-O-CH₃ molecule and the pyrite surface is extremely weak and the interaction between the Ph-COOH and Ph-CO-CH₃ molecule and the pyrite surface is slightly stronger. Such a weak interaction between them cannot be a chemical bond. The coal-pyrite interactions are a physical adsorption.

(3) On the whole, the charge transferred from the pyrite surface to coal structural units. For Ph-OH and Ph-O-CH₃, the electrons were mainly gathered around the S atoms of the pyrite surface. After Ph-COOH and Ph-CO-CH₃ were adsorbed on the pyrite surface, the electrons were mainly gathered around the Fe atoms of the pyrite surface and the O atoms of coal structural units. The occurrence of electron accumulation made it possible for coal structural units to adsorb on the pyrite surface.

(4) The fresh monomer-dissociated coal-pyrite entered into the flotation concentrate partially due to the interactions between the coal particles and the fine pyrite particles. Therefore, mixing measures and the action of adding the efficient dispersants and inhibitors can be taken to avoid natural adsorption to improve the subsequent desulfurization rate and the selectivity of mineral flotation. Then, the concentrate grade can be improved and it will bring greater economic benefits.

Author Contributions: Conceptualization, P.X.; methodology, P.X.; validation, P.X.; formal analysis, P.X.; investigation, K.L.; resources, P.X.; data curation, P.X.; writing-original draft preparation, P.X.; writing-review and editing, F.S.; visualization, P.X.; project administration, P.X.; funding acquisition, K.L. and A.L.; supervision, X.F. and X.T.; software, Q.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by Science and Technology Project of Hebei Education Department (BJK2023063) and supported by the Fundamental Research Funds for the Central Universities (Grant No. 3142021001). The work is also supported by the Foundation of Key Laboratory of Power Machinery and Engineering, Ministry of Education, P.R. China (202201).

Data Availability Statement: The data presented in this study are available on request from the corresponding author on request.

Acknowledgments: We would like to thank Q. Zhuo for providing software.

Conflicts of Interest: The authors declare no conflicts of interest.

## References

1.  Chen, Q.R. Consideration of clean coal strategy in China. *J. Heilongjiang Univ. Sci. Technol.* 2004, 14, 261–264.
2.  Lu, M.X.; Liu, W.L. Sulfur Distribution of High Sulfur Coal and Feasibility Study of Coal Desulfurization Before Combustion. *Coal Sci. Technol.* 1999, 27, 42–45.
3.  Cao, S.M.; Cao, Y.J.; Ma, Z.L.; Liao, Y.F. The flotation separation of fine pyrite locked in coking coal. *J. China Univ. Min. Technol.* 2019, 48, 1366–1374.
4.  Zhu, H.; Li, H.L.; Ou, Z.S.; Wang, D.Z. Effect of Pyrite Surface Oxidation on the Desulurization in Coal Flotation. *Clean Coal Technol.* 2000, 6, 5–8.
5.  Yoon, R.H.; Lagno, M.; Luttrel, G.H.; Mirlvzarski, J.A. On the hydrophobicity of coal pyrite. In *Processing and Utilization of High-Sulfur Coals IV*; Dugan, P.R., Quiley, D.R., Attia, Y.A., Eds.; Elsevier Science Publishers B.V.: Amsterdam, The Netherlands, 1991; pp. 241–253.
6.  Niu, X.P. Correlation of Surface Oxidation of Galena, Chalcopyrite and Pyrite with Their Floatability. Ph.D. Dissertation, Chinese Academy of Sciences, Institute of Process Engineering, Beijing, China, 2019.
7.  Xi, P.; Shi, C.X.; Yan, P.K. DFT study on the influence of sulfur on the hydrophobicity of pyrite surfaces in the process of oxidation. *Appl. Surf. Sci.* 2018, 466, 964–969. [CrossRef]
8.  Çetinkaya, Z. Investigation of removal of ash and sulfur from Kangal (Sivas/Turkey) lignite with the application of combined methods. *Int. J. Coal Prep. Util.* 2024, 2391908, 1–18. [CrossRef]
9.  Channa, F.H.; Khoso, S.A.; Soomro, S.A.; Uqaili, M.A. Studies on sulfur liberation characteristics of Pakistani high sulfur low-rank coal using Hardgrove grinding. *Int. J. Coal Prep. Util.* 2024, 2341953, 1–20. [CrossRef]
10. Xi, P.; Liu, W.L.; Han, Y.H. Study on the mechanism of coal pyrite crystal lattice defects and floatability. *J. China Coal. Soc.* 2016, 41, 997–1003.
11. Xi, P.; Liu, W.L.; Yang, Z.Y. Quantum chemistry investigation on influence of carbon atom adsorption in carbon material to the coal pyrite hydrophobicity. *J. China Coal. Soc.* 2017, 42, 1290–1296.
12. Xi, P.; Ma, R.X.; Liu, W.L. Research on the Effect of Carbon Defects on the Hydrophilicity of Coal Pyrite Surface from the Insight of Quantum Chemistry. *Molecules* 2019, 24, 2285. [CrossRef] [PubMed]
13. Xi, P.; Wang, D.H.; Liu, W.L. DFT Study into the Influence of Carbon Material on the Hydrophobicity of a Coal Pyrite Surface. *Molecules* 2019, 24, 3534. [CrossRef] [PubMed]
14. Kawatra, S.K.; Eisele, T.C. Pyrite recovery mechanisms in coal flotation. *Int. J. Miner. Process.* 1997, 50, 187–201. [CrossRef]
15. Kawatra, S.K.; Eisele, T.C.; Johnson, H. Recovery of liberated pyrite in coal flotation: Entrainment or hydrophobicity. In *Processing and Utilization of High-Sulfur Coals IV*; Dugan, P.R., Quiley, D.R., Attia, Y.A., Eds.; Elsevier Science Publishers B.V.: Amsterdam, The Netherlands, 1991; pp. 255–277.
16. Mkhonto, P.P.; Zhang, X.R.; Lu, L. Adsorption mechanisms and effects of thiocarbamate collectors in the separation of chalcopyrite from pyrite minerals: DFT and experimental studies. *Miner. Eng.* 2022, 176, 107318. [CrossRef]
17. Mkhonto, P.P.; Zhang, X.R.; McFadzean, B. Incorporating pH into DFT-D+U and microflotation recovery studies on heterocyclic collector-pyrite interactions. *Sep. Purif. Technol.* 2024, 337, 126430. [CrossRef]
18. Liu, Y.C.; Chen, J.H.; Li, Y.Q. Adsorption behaviors of dibutyl dithiophosphate and sodium-diisobutyl dithiophosphinate (3418A) on chalcopyrite: A combined experimental and theoretical study. *Appl. Surf. Sci.* 2023, 636, 157810. [CrossRef]
19. Liu, Y.C.; Chen, J.H.; Li, Y.Q. First-principles study on the co-adsorption of water and oxygen molecules on chalcopyrite (112)-M surface. *Int. J. Min. Sci. Technol.* 2023, 33, 1055–1063. [CrossRef]
20. Zhang, Y.B.; Chen, J.H.; Li, Y.Q. Application of a new self-consistent-charge density-functional tight-binding(SCC-DFTB) parameter set for simulating the adsorption of flotation reagents on the surface of typical lead minerals. *Miner. Eng.* 2024, 209, 108631. [CrossRef]
21. Feng, X.L.; Jian, S.; Chen, H.M.; Chen, J.H. Synergistic adsorption of ethyl xanthate and butyl xanthate on pyrite surfaces: A DFT study. *Quantum Chem.* 2024, 124, e27448. [CrossRef]
22. Chen, P.; Sun, W.; Yue, T. Dynamics simulation of tributyltetradecylphosphonium chloride on kaolinite (001) plane. *J. China Univ. Min. Technol.* 2014, 43, 294–299.
23. Segall, M.D.; Lindan, P.J.D.; Probert, M.J.; Pickard, C.J.; Hasnip, P.J.; Clark, S.J.; Payne, M.C. First-principles simulation: Ideas, illustrated and the CASTEP code. *J. Phys. Condens. Matter* 2002, 14, 2717–2744. [CrossRef]
24. Perdew, J.P.; Chevary, J.A.; Vosko, S.H.; Jackson, K.A.; Pederson, M.R.; Singh, D.J.; Fiolhais, C. Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation. *Phys. Rev. B Condens. Matter Mater. Phys.* 1992, 46, 6671–6687. [CrossRef] [PubMed]
25. Vanderbilt, D. Soft self-consistent pseudopotentials in a generalized eigenvalue formalism. *Phys. Rev. B* 1990, 41, 7892–7895. [CrossRef] [PubMed]

26. Li, Y.; Chen, J.; Zhao, C. Influence of external electronic field on the electronic structure and optical properties of pyrite. *RSC Adv.* 2017, **7**, 56676–56681. [CrossRef]

27. Monkhorst, H.J.; Pack, J.D. Special points for Brillouin-zone integrations. *Phys. Rev. B Solid State* 1976, **13**, 5188–5192. [CrossRef]

28. Pack, J.D.; Monkhorst, H.J. "Special points for Brillouin-zone integrations"—A reply. *Phys. Rev. B Solid State* 1977, **16**, 1748–1749. [CrossRef]

29. Han, Y.; Liu, W.L.; Zhou, J. Interactions between kaolinite Al-OH surface and sodium hexametaphosphate. *Appl. Surf. Sci.* 2016, **387**, 759–765. [CrossRef]

30. Han, Y.; Liu, W.L.; Chen, J.H. DFT simulation of the adsorption of sodium silicate species on kaolinite surfaces. *Appl. Surf. Sci.* 2016, **370**, 403–409. [CrossRef]

31. Yang, Z.; Liu, W.; Zhang, H. DFT study of the adsorption of 3-chloro-2-hydroxypropyl trimethylammonium chloride on montmorillonite surfaces in solution. *Appl. Surf. Sci.* 2018, **436**, 58–65. [CrossRef]

32. Mulliken, R.S. Electronic population analysis on LCAO-MO molecular wave functions. IV. bonding and antibonding in LCAO and Valence-bond theories. *J. Chem. Phys.* 1955, **23**, 2343–2346. [CrossRef]

33. Šolc, R.; Gerzabek, M.H.; Lischka, H.; Tunega, D. Wettability of kaolinite (001) surfaces—Molecular dynamic study. *Geoderma* 2011, **169**, 47–54. [CrossRef]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.