bbox marker: ![](./images/814723990261071873_1.jpg)

bbox marker: ![](./images/814723990261071873_2.jpg)

PAPER

View Article Online
View Journal | View Issue

bbox marker: ![](./images/814723990261071873_3.jpg)

Cite this: J. Mater. Chem. A, 2014, 2,
13898

# Comparative study on structure, energetic and mechanical properties of a ε-CL-20/HMX cocrystal and its composite with molecular dynamics simulation

Ting Sun, $^{a}$ Ji Jun Xiao, $^{* a}$ Qiang Liu, $^{a}$ Feng Zhao $^{b}$ and He Ming Xiao $^{* a}$

Molecular dynamics (MD) simulation was conducted for a $\varepsilon$-CL-20 (2,4,6,8,10,12-hexanitro-2,4,6,8,10,12hexazaisowurtzitane) crystal, a $\beta$-HMX (1,3,5,7-tetranitro-1,3,5,7-tetrazocane) crystal, a $\varepsilon$-CL-20/HMX cocrystal and its composite with the same molar ratio as in the cocrystal using a COMPASS force field with NPT ensemble at different temperatures. The maximum bond length $(L_{max})$ of the $N-NO_{2}$ trigger bond, cohesive energy density (CED) and binding energy $(E_{bind})$ between HMX and CL-20 molecules as well as elastic properties were calculated. $L_{max}$ increases with rising temperature and is found to be in the order of $\varepsilon$-CL-20/HMX cocrystal $<$ CL-20/HMX composite $<\varepsilon$-CL-20 crystal at the same temperature. CED and $E_{bind}$ of the cocrystal decrease with increasing temperature and are all greater than those of the composite at the same temperature. These indicate that the cocrystal is the most insensitive and its thermal stability is better than that of the composite. Furthermore, the pair correlation function $g(r)$ analysis reveals that hydrogen bonds exist. The tensile modulus $(E)$, bulk modulus $(K)$ and shear modulus $(G)$ of the $\varepsilon$-CL-20/HMX cocrystal and the composite are smaller than those of $\varepsilon$-CL-20 and $\beta$-HMX crystals and decrease with increasing temperature. However, the $K/G$ values of the cocrystal and the composite are larger than those of the other two crystals, implying that they have better ductility.

Received 7th March 2014
Accepted 12th June 2014
DOI: 10.1039/c4ta01150c
www.rsc.org/MaterialsA

## 1 Introduction
In the field of energetic materials, high performance and insensitive explosives have always attracted much attention of researchers. $^{1}$ For current single compound explosives, high performance and safety are somewhat mutually exclusive, which seriously limit their development and applications. $^{2}$ Fortunately, the recent formation of the energetic cocrystal offers opportunities to modify the properties of energetic materials, such as oxygen balance, sensitivity, detonation velocity, and safety. $^{3,4}$ A cocrystal $^{5,6}$ is a multiple component crystal that is constructed out of two or more neutral molecular components, which are solid in their pure forms under ambient conditions. These components co-exist as an intrinsic stoichiometric ratio by non-covalent interactions (such as hydrogen bonding, van der Waals, and $\pi-\pi$ stacking interactions).

1,3,5,7-Tetranitro-1,3,5,7-tetrazocane (HMX) is known as a typical octa-heterocyclic nitramine explosive with the best comprehensive performance and is widely used because of its thermal stability and high detonation velocity. Among the four reported crystalline phases, denoted as $\alpha, \beta, \delta$ and $\gamma, \beta$-HMX is the most thermodynamically stable form under ambient conditions. $^{7}$ On the other hand, 2,4,6,8,10,12-hexanitro2,4,6,8,10,12-hexaazaisowurtzitane (CL-20) is the most famous high energy density compound (HEDC) for practical applications at present. The $\varepsilon$ polymorph $^{8-10}$ of CL-20 is the densest and most thermodynamically stable form of the reported crystalline forms $(\alpha, \beta, \gamma$ and $\varepsilon)$. Molecular structures of HMX and CL-20 are respectively shown in Fig. 1(a) and (b). However, in modern ordnance, CL-20 has failed to meet the strong requirements of safety due to its high sensitivity.

Bolton et al. $^{4}$ prepared a $2:1$ (molar ratio) cocrystal of CL-20/ HMX, which exhibits higher explosive power and oxygen balance than $\beta$-HMX, and features a similar sensitivity to that of HMX. These properties make the CL-20/HMX cocrystal a very attractive candidate to replace HMX. In the cocrystal structure obtained from X-ray diffraction, HMX molecules are all in $\beta$ polymorph, but disorder was observed in CL-20 molecules [Fig. 1(c)] due to several different polymorphs for CL-20 molecules in the cocrystal powder sample. In this paper, we designed and constructed the model of the $\varepsilon$-CL-20/HMX cocrystal according to the experimental structure in ref. 4 and our designed primitive cell is shown in Fig. 1(d). For comparison, the $\varepsilon$-CL-20/HMX cocrystal, the $\varepsilon$-CL-20/HMX composite with the same molar ratio, $\varepsilon$-CL-20 and $\beta$-HMX crystals were all

$^{a}$ Molecules and Materials Computation Institute, School of Chemical Engineering,
Nanjing University of Science and Technology, Nanjing 210094, PR China. E-mail:
xiao_jijun@njust.edu.cn; xiao@njust.edu.cn; Fax: +86 25 84303919
$^{b}$ National Key Laboratory of Shock Wave and Detonation Physics, Institute of Fluid
Physics, China Academy of Engineering Physics, Mianyang 621900, PR China

13898 | J. Mater. Chem. A, 2014, 2, 13898-13904
This journal is © The Royal Society of Chemistry 2014

![](./images/814723990261071873_4.jpg)

Fig. 1 Molecular structures of HMX (a) and CL-20 (b), disorder (c) observed in CL-20 molecules (nitro positions shown as arrows), and the theoretical primitive cell of the CL-20/HMX cocrystal (d).

considered. It is well known that with increasing temperature, energetic materials become more sensitive and less stable. In view of this, MD simulations were conducted at different temperatures, and the structural data, CED data and $E_{\text{bind}}$ data as well as elastic properties were calculated from the MD trajectories. These data were analyzed to compare and explore their sensitivity, thermal stability, and mechanical properties.

More specifically, in this paper we first introduce the construction of models and computation conditions for the simulation. Then the N-NO₂ trigger bond lengths of the $\varepsilon$-CL-20 crystal, the $\varepsilon$-CL-20/HMX composite and the cocrystal at different temperatures are presented and discussed in terms of the relationship with sensitivity. The cohesive energy density (CED) and binding energy ($E_{\text{bind}}$) between HMX and CL-20 molecules for the composite and the cocrystal at different temperatures are also provided and discussed in terms of the relationship with sensitivity and thermal stability.

In addition, the analysis of the interactions between HMX and CL-20 molecules in the composite and the cocrystal is shown using pair correlation function (PCF). After PCF analysis, the mechanical properties of $\beta$-HMX, the CL-20/HMX composite, the cocrystal, and $\varepsilon$-CL-20 such as tensile modulus ($E$), Poisson's ratio ($\nu$), bulk modulus ($K$), shear modulus ($G$), and quotient $K/G$ are analyzed and discussed.

## 2 Modeling and computational methods

In this paper, all simulations were performed under a COMPASS (condensed-phase optimized molecular potentials for atomistic simulation studies) force field,¹¹ which is suitable for MD simulation of the condensed phase, especially for nitramine explosives. For instance, previous studies show that it has been successfully applied for $\varepsilon$-CL-20¹⁰,¹²,¹³ and $\beta$-HMX.¹⁴,¹⁵

Based on the crystal parameters derived from X-ray diffraction,¹⁶,¹⁷ the primary cells of $\varepsilon$-CL-20 and $\beta$-HMX crystals, corresponding to $(2 \times 2 \times 4)$ and $(5 \times 3 \times 3)$ unit cells, respectively, were built. With reference to the initial structure in ref. 4, the primitive cell of the cocrystal was obtained by taking the place of the CL-20 molecule in the cocrystal with $\varepsilon$-CL-20 molecules [Fig. 1(d)], and then the primary cell for the $\varepsilon$-CL-20/HMX cocrystal, corresponding to $(2 \times 3 \times 2)$ unit cells was built. There were 48 $\varepsilon$-CL-20 molecules, 24 $\beta$-HMX molecules, having totally 2400 atoms in the cocrystal.

According to the molar ratio of $2:1$ for CL-20 and HMX, $(2 \times 2 \times 3)$ unit cells of $\varepsilon$-CL-20 and $(3 \times 2 \times 2)$ unit cells of $\beta$-HMX were prepared, and their molecular clusters were placed in a cubic periodic box with a length of $100$ Å. Then the cubic periodic box was compressed gradually step by step, and at each step NVT ensemble MD run at 295 K was carried out until the system attained thermal equilibrium. This process continued until the composite arrived at its theoretical density. After that the modeling of the composite was completed. The composite model also contained 48 $\varepsilon$-CL-20 molecules and 24 $\beta$-HMX molecules, having totally 2400 atoms.

The above models for $\varepsilon$-CL-20 and $\beta$-HMX crystals, the $\varepsilon$-CL-20/HMX cocrystal and the $\varepsilon$-CL-20/HMX composite were allowed to evolve dynamically in isothermal-isobaric (NPT) ensemble with Andersen temperature control using the stochastic collision method¹⁸ and Parrinello-Rahman pressure control fully relaxing all parameters¹⁹ at atmospheric pressure. The temperature started from 245 K, with an increasing step of 50 K, to 445 K. In the following condensed phase simulation cases, the van der Waals interactions were truncated at $9.5$ Å with long range tail correction,²⁰ and the electrostatic interactions were calculated *via* the standard Ewald summation.²¹ The equations of motion were integrated with a step of 1 fs. After equilibration run, production runs of 1 ns were performed, during which data were collected with 10 fs sampling interval for analysis. These computations were all carried out using software program-MS (Material Studio) from Accelrys Inc. (San Diego, CA).

![](./images/814723990261071873_5.jpg)

Fig. 2 Equilibrium structures of the cocrystal (a) and the composite (b) at 295 K ($\varepsilon$-CL-20 in yellow).

For illustration, the equilibrium structures of the $\varepsilon$-CL-20/HMX cocrystal and composite at 295 K are shown in Fig. 2.

## 3 Results and discussions

### 3.1 Trigger bond length and sensitivity

A trigger bond of the energetic molecule is a weak bond, which breaks preferentially with external stimuli, causing thermal

![](./images/814723990261071873_6.jpg)

Fig. $3 \ ~N-NO_{2}$ bond length distribution of $\varepsilon$-CL-20 at $295 ~K$.

decomposition or detonation. Politzer et al. $^{22}$ have used the reciprocals of the lengths of the trigger bonds to measure the bond strength and described the impact sensitivity of nitramine and nitro compounds. Based on the production trajectory, MD simulation is able to give the statistical distribution of the bond length, as shown in Fig. 3. The average bond length $(1.397 \AA)$ of $N-NO_{2}$ for $\varepsilon$ -CL-20 is close to the experimental $(1.369 \AA)^{16}$ and the quantum optimized data $(1.371 \AA).^{23}$ Besides, the molecules with maximum bond lengths are "activated" and our group has predicted the relative impact sensitivity of energetic systems with the maximum bond lengths $L_{ max }$ of trigger bonds. $^{15}$

It is well known that CL-20 is more sensitive than HMX, $^{24}$ and both the experimental $^{25}$ and theoretical $^{26}$ studies have verified that the CL-20 component is prior to decompose in pyrolysis. So in this study, we mainly concentrate on the trigger bond lengthof CL-20 and its trigger bond is $N-NO_{2} \cdot^{27,28}$

Table 1 presents the results of the trigger bond lengths $(N-NO_{2})$ of $\varepsilon$ -CL-20 for the $\varepsilon$ -CL-20 crystal, the $\varepsilon$ -CL-20/HMX composite and the cocrystal at different temperatures based on the production trajectory. As the temperature increases, the average bond lengths $L_{ave }$ of all the three models increase, butnot obviously, whereas the maximum bond length $L_{ max }$  increases gradually and significantly. Therefore, the variation trend of $L_{ max }$ well reflects the fact that the sensitivity increases with rising temperature. Furthermore, for every temperature, $L_{max }$ is in the order of $\varepsilon$ -CL-20/HMX (cocrystal) $<\varepsilon$ -CL-20/HMX(composite) $<\varepsilon$ -CL-20 crystal. Then we may infer that the impact sensitivity for these systems is in the following sequence: $\varepsilon$ -CL20/HMX(cocrystal) $<\varepsilon$ -CL-20/HMX(composite) $<\varepsilon$ -CL-20 crystal. It was expected that adding HMX in CL-20/HMX will reduce sensitivity relatively to the $\varepsilon$ -CL-20 crystal by diluting the more sensitive component. However, $L_{ max }$ reduction in the cocrystal is more significant than in the composite, suggesting that the cocrystal is less sensitive than the composite.

### 3.2 Cohesive energy density
The cohesive energy density (CED) is the amount of energy needed to completely separate molecules from each other per mole for unit volume until there are no interactions within, i.e. the energy required to transfer from the condensed phase to the gas phase. In atomistic simulations, CED corresponds to the cohesive energy per unit volume and the cohesive energy is defined as the increase in energy per mole of a material till all intermolecular forces are eliminated.

The CEDs of the $\varepsilon$ -CL-20/HMX cocrystal and composite are listed in Table 2. As shown in Table 2, under the COMPASS force field for MD simulation, CED is the sum of vdW and electro- static energy, i.e., nonbond energy between molecules. Besides, it is obviously seen that, as the temperature increases, CED, vdW, and electrostatic energy in the cocrystal and composite all decrease monotonously. This agrees with the experimental fact that the sensitivity becomes higher with increasing tempera- ture, as lower energy needed for the material to transfer from the condensed phase to the gas phase tends to cause decom- position and explosion. $^{15}$ Therefore, CED can also be used as a theoretical criterion for the heat and impact sensitivity. At the same temperature, the CED of the cocrystal is much higher than that of the composite, indicating that the cocrystal is more stable and insensitive, which is consistent with the conclusion deduced from $L_{ max }$ .

### 3.3 Interactions between $\beta$ -HMX and $\varepsilon$ -CL-20 in the $\varepsilon$ -CL-20/ HMX cocrystal and composite
#### 3.3.1 Binding energy.
Binding energy $(E_{bind })$ is defined as the negative value of the intermolecular interaction energy $(E_{inter })$ , that is, $E_{bind }=-E_{inter }$ , which can well reflect the compatibility of the two components blended with each other. The intermolecular interaction energy can be evaluated by the total energies of the whole system and individual component energy in the system. As such, $E_{bind }$ between $\varepsilon$ -CL-20 and $\beta$ -HMXcan be expressed as follows:

$$E_{\text {bind }}=-E_{\text {inter }}=-\left(E_{\text {total }}-E_{\varepsilon \text {-CL-20 }}-E_{\beta \text {-HMX }}\right)$$

Table 1 The trigger bond $(N-NO_{2})$ lengths of $\varepsilon$ -CL-20 for the $\varepsilon$ -CL-20 crystal, $\varepsilon$ -CL-20/HMX composite and cocrystal at different temperatures. The corresponding deviations are listed in brackets
| Model     | Bond length/Å | Temperature/K |        |        |        |        |
| --------- | ------------- | ------------- | ------ | ------ | ------ | ------ |
|           |               | 245           | 295    | 345    | 395    | 445    |
| $\varepsilon$-CL-20 | $L_{ave}$     | 1.396 (0.028) | 1.397 (0.031) | 1.398 (0.033) | 1.399 (0.036) | 1.399 (0.038) |
|           | $L_{max}$     | 1.574         | 1.594  | 1.618  | 1.622  | 1.652  |
| Composite | $L_{ave}$     | 1.395 (0.028) | 1.396 (0.031) | 1.396 (0.033) | 1.397 (0.036) | 1.398 (0.038) |
|           | $L_{max}$     | 1.562         | 1.591  | 1.611  | 1.621  | 1.644  |
| Cocrystal | $L_{ave}$     | 1.392 (0.028) | 1.393 (0.030) | 1.394 (0.033) | 1.395 (0.035) | 1.396 (0.038) |
|           | $L_{max}$     | 1.547         | 1.572  | 1.603  | 1.608  | 1.640  |

<table>
<caption>Table 2 Cohesive energy density CED<sup>a</sup> and relevant energies of the $\varepsilon$-CL-20/HMX composite and cocrystal at different temperatures (kJ cm<sup>−3</sup>)</caption>
<thead>
<tr>
<th rowspan="2">Model</th>
<th rowspan="2">Energy</th>
<th colspan="5">Temperature/K</th>
</tr>
<tr>
<th>245</th>
<th>295</th>
<th>345</th>
<th>395</th>
<th>445</th>
</tr>
</thead>
<tbody>
<tr>
<td>Composite</td>
<td>CED</td>
<td>0.74(0.01)</td>
<td>0.71(0.01)</td>
<td>0.69(0.01)</td>
<td>0.68(0.01)</td>
<td>0.65(0.01)</td>
</tr>
<tr>
<td></td>
<td>vdW</td>
<td>0.33(0.00)</td>
<td>0.32(0.00)</td>
<td>0.31(0.00)</td>
<td>0.31(0.01)</td>
<td>0.30(0.01)</td>
</tr>
<tr>
<td></td>
<td>Electrostatic</td>
<td>0.41(0.01)</td>
<td>0.40(0.01)</td>
<td>0.38(0.01)</td>
<td>0.37(0.01)</td>
<td>0.35(0.01)</td>
</tr>
<tr>
<td>Cocrystal</td>
<td>CED</td>
<td>0.84(0.01)</td>
<td>0.81(0.01)</td>
<td>0.79(0.01)</td>
<td>0.77(0.01)</td>
<td>0.74(0.01)</td>
</tr>
<tr>
<td></td>
<td>vdW</td>
<td>0.38(0.00)</td>
<td>0.37(0.00)</td>
<td>0.36(0.00)</td>
<td>0.35(0.00)</td>
<td>0.34(0.01)</td>
</tr>
<tr>
<td></td>
<td>Electrostatic</td>
<td>0.46(0.01)</td>
<td>0.45(0.01)</td>
<td>0.43(0.01)</td>
<td>0.42(0.01)</td>
<td>0.40(0.01)</td>
</tr>
</tbody>
</table>

<sup>a</sup> CED = $E_{\text{vdW}} + E_{\text{Electrostatic}}$. The corresponding deviations are listed in brackets.

<table>
<caption>Table 3 Binding energies of $\varepsilon$-CL-20/HMX (composite and cocrystal) at different temperatures (kJ mol<sup>−1</sup>)<sup>a</sup></caption>
<thead>
<tr>
<th>Model</th>
<th>T/K</th>
<th>$E_{\text{total}}$</th>
<th>$E_{\text{CL-20}}$</th>
<th>$E_{\text{HMX}}$</th>
<th>$E_{\text{bind}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Composite</td>
<td>245</td>
<td>−83 942.9(25.1)</td>
<td>−58 602.7(23.2)</td>
<td>−22 141.4(19.4)</td>
<td>3198.8(14.9)</td>
</tr>
<tr>
<td></td>
<td>295</td>
<td>−82 342.7(34.5)</td>
<td>−57 463.6(22.7)</td>
<td>−21 763.9(15.4)</td>
<td>3115.2(8.7)</td>
</tr>
<tr>
<td></td>
<td>345</td>
<td>−80 873.2(37.3)</td>
<td>−56 471.8(33.2)</td>
<td>−21 406.5(24.4)</td>
<td>2994.9(14.2)</td>
</tr>
<tr>
<td></td>
<td>395</td>
<td>−79 203.9(47.0)</td>
<td>−55 323.8(35.4)</td>
<td>−20 910.0(31.3)</td>
<td>2970.1(18.1)</td>
</tr>
<tr>
<td></td>
<td>445</td>
<td>−77 420.0(50.8)</td>
<td>−54 012.1(46.4)</td>
<td>−20 547.3(26.3)</td>
<td>2860.6(26.2)</td>
</tr>
<tr>
<td>Cocrystal</td>
<td>245</td>
<td>−85 066.0(23.6)</td>
<td>−58 096.3(30.3)</td>
<td>−21 463.7(17.8)</td>
<td>5506.0(17.7)</td>
</tr>
<tr>
<td></td>
<td>295</td>
<td>−83 477.5(15.7)</td>
<td>−57 002.1(15.7)</td>
<td>−21 102.2(23.3)</td>
<td>5373.3(11.3)</td>
</tr>
<tr>
<td></td>
<td>345</td>
<td>−81 875.2(33.0)</td>
<td>−55 912.4(32.1)</td>
<td>−20 634.0(23.6)</td>
<td>5328.7(11.8)</td>
</tr>
<tr>
<td></td>
<td>395</td>
<td>−80 225.6(44.0)</td>
<td>−54 840.1(18.5)</td>
<td>−20 224.1(21.6)</td>
<td>5161.4(22.9)</td>
</tr>
<tr>
<td></td>
<td>445</td>
<td>−78 533.3(44.6)</td>
<td>−53 632.1(45.4)</td>
<td>−19 907.9(30.9)</td>
<td>4993.3(11.9)</td>
</tr>
</tbody>
</table>

<sup>a</sup> The corresponding deviations are listed in brackets.

where $E_{\text{total}}$ is the total energy of the whole system, and $E_{\varepsilon\text{-CL-20}}$ and $E_{\beta\text{-HMX}}$ are, respectively, the energies of $\varepsilon$-CL-20 and $\beta$-HMX. Higher binding energy means stronger interaction between components and thus more stable system. In this paper, it has important influence on the compatibility for the $\varepsilon$-CL-20/HMX composite, the formation of the cocrystal and the thermal

![](./images/814723990261071873_7.jpg)

Fig. 4 PCF for $\text{H}\cdots\text{O}$ and $\text{H}\cdots\text{N}$ atom pairs in the $\varepsilon$-CL-20/HMX cocrystal and composite at 295 K.

![](./images/814723990261071873_8.jpg)

Fig. 5 PCF for H(1)⋯O(2) (a) and H(2)⋯O(1) (b) in the cocrystal at different temperatures.

stability of energetic systems. The total energies ($E_{\text{total}}$) of the whole system, the energies of $\varepsilon$-CL-20 ($E_{\varepsilon\text{-CL-20}}$) and $\beta$-HMX ($E_{\beta\text{-HMX}}$), and the binding energies ($E_{\text{bind}}$) at different temperatures are tabulated in Table 3.

It is obviously observed that with increasing temperature $E_{\text{bind}}$ of the composite and the cocrystal both decreases gradually, which means that the thermodynamic stability of the two systems decreases. Besides, we can find that $E_{\text{bind}}$ of the cocrystal is much larger than the composite explosive at each temperature, which means that the cocrystal is more stable. Herein we can find a reasonable explanation from the illustrated example in Fig. 2(a) and (b), where it can be seen that layers of $\beta$-HMX alternate with bilayers of $\varepsilon$-CL-20 in the cocrystal, namely, interactions are layer-layer, while for the $\varepsilon$-CL-20/HMX composite, interactions only exist at the interfaces of different components having smaller interaction area. So it is not difficult to understand that stronger interactions exist between $\beta$-HMX and $\varepsilon$-CL-20 in the cocrystal.

### 3.3.2 Pair correlation function analysis.
The pair correlation function (PCF) is a useful physical tool because it provides insights into a material structure by a measure of local spatial ordering, which gives a measure of the probability density $g(r)$ of finding an atom at some distance from a reference atom.

In this paper, two kinds of atom pairs ($\text{H}\cdots\text{O}$ and $\text{H}\cdots\text{N}$) were considered. H, O, and N (negatively charged) atoms in $\varepsilon$-CL-20 molecules were denoted as H(1), O(1), and N(1) and those in $\beta$-HMX molecules were named as H(2), O(2) and N(2), respectively.

In order to explore the interaction between $\varepsilon$-CL-20 and $\beta$-HMX molecules, PCF for $\text{H}\cdots\text{O}$ and $\text{H}\cdots\text{N}$ atomic pairs in the $\varepsilon$-CL-20/HMX cocrystal and composite at 295 K are depicted in Fig. 4, respectively.

Generally, the interaction distance range ($r$) for the hydrogen bond is 2.0–3.1 Å and for strong vdW is 3.1–5.0 Å. When $r$ is farther than 5.0 Å, the vdW interaction is very weak.¹³ In Fig. 4(a) and (b), the first peaks of the curves all locate at about 2.4 Å. This means that hydrogen bonds exist in H(1)⋯O(2) and H(2)⋯O(1) pairs. In Fig. 4(c) and (d), the first peaks of the curves for H(1)⋯N(2) and H(2)⋯N(1) locate at about 4.5–4.9 Å, which indicates that only vdW interaction exists in these pairs. From Fig. 4(a)–(d), we can also find that the value of $g(r)$ of the cocrystal is mostly higher than that of the composite. This implies that the interaction in the two kinds of pairs between $\varepsilon$-CL-20 and $\beta$-HMX in the cocrystal is stronger than that in the composite, which is consistent with the conclusion that $E_{\text{bind}}$ of the CL-20/HMX cocrystal is much larger than that of the composite.

Fig. 5 shows $g(r)$ and its variation with temperature of two hydrogen bond interactions in the cocrystal, H(1)⋯O(2) and H(2)⋯O(1). Obviously, the peak height decreases and it slightly shifts to the right, which is mainly attributed to the enhanced atomic motion with increasing temperature, indicating that the interaction between $\varepsilon$-CL-20 and $\beta$-HMX in the cocrystal is

Table 4 Tensile modulus ($E$), Poisson's ratio ($\nu$), bulk modulus ($K$), shear modulus ($G$) and quotient $K/G$ at different temperatures. The corresponding deviations are listed in brackets. The unit for $E$, $K$ and $G$ is GPa

<table>
<thead>
<tr>
<th></th>
<th></th>
<th colspan="5">Temperature/K</th>
</tr>
<tr>
<th>System</th>
<th>Parameter</th>
<th>245 K</th>
<th>295 K</th>
<th>345 K</th>
<th>395 K</th>
<th>445 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>β-HMX</td>
<td>$E$</td>
<td>11.1 (0.08)</td>
<td>10.2 (0.06)</td>
<td>9.6 (0.10)</td>
<td>8.7 (0.07)</td>
<td>8.0 (0.12)</td>
</tr>
<tr>
<td></td>
<td>$\nu$</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.2 (0.00)</td>
</tr>
<tr>
<td></td>
<td>$K$</td>
<td>8.1 (0.09)</td>
<td>7.4 (0.06)</td>
<td>6.7 (0.09)</td>
<td>5.9 (0.05)</td>
<td>5.3 (0.04)</td>
</tr>
<tr>
<td></td>
<td>$G$</td>
<td>4.4 (0.03)</td>
<td>4.0 (0.02)</td>
<td>3.8 (0.04)</td>
<td>3.5 (0.03)</td>
<td>3.2 (0.06)</td>
</tr>
<tr>
<td></td>
<td>$K/G$</td>
<td>1.9 (0.02)</td>
<td>1.8 (0.01)</td>
<td>1.8 (0.01)</td>
<td>1.7 (0.02)</td>
<td>1.6 (0.03)</td>
</tr>
<tr>
<td>Composite</td>
<td>$E$</td>
<td>5.6 (0.16)</td>
<td>4.3 (0.09)</td>
<td>3.6 (0.08)</td>
<td>3.1 (0.11)</td>
<td>2.6 (0.21)</td>
</tr>
<tr>
<td></td>
<td>$\nu$</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.4 (0.00)</td>
<td>0.4 (0.01)</td>
</tr>
<tr>
<td></td>
<td>$K$</td>
<td>6.1 (0.07)</td>
<td>4.8 (0.07)</td>
<td>4.6 (0.15)</td>
<td>4.2 (0.14)</td>
<td>3.6 (0.12)</td>
</tr>
<tr>
<td></td>
<td>$G$</td>
<td>2.1 (0.06)</td>
<td>1.6 (0.04)</td>
<td>1.5 (0.03)</td>
<td>1.1 (0.04)</td>
<td>0.9 (0.08)</td>
</tr>
<tr>
<td></td>
<td>$K/G$</td>
<td>2.9 (0.06)</td>
<td>3.0 (0.05)</td>
<td>3.0 (0.06)</td>
<td>3.7 (0.13)</td>
<td>3.9 (0.26)</td>
</tr>
<tr>
<td>Cocrystal</td>
<td>$E$</td>
<td>9.0 (0.04)</td>
<td>8.6 (0.04)</td>
<td>8.0 (0.07)</td>
<td>7.4 (0.05)</td>
<td>6.3 (0.07)</td>
</tr>
<tr>
<td></td>
<td>$\nu$</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
</tr>
<tr>
<td></td>
<td>$K$</td>
<td>8.6 (0.07)</td>
<td>8.3 (0.05)</td>
<td>7.7 (0.04)</td>
<td>7.1 (0.09)</td>
<td>5.8 (0.06)</td>
</tr>
<tr>
<td></td>
<td>$G$</td>
<td>3.4 (0.02)</td>
<td>3.3 (0.01)</td>
<td>3.0 (0.03)</td>
<td>2.8 (0.02)</td>
<td>2.4 (0.03)</td>
</tr>
<tr>
<td></td>
<td>$K/G$</td>
<td>2.5 (0.02)</td>
<td>2.5 (0.02)</td>
<td>2.5 (0.02)</td>
<td>2.6 (0.03)</td>
<td>2.4 (0.03)</td>
</tr>
<tr>
<td>ε-CL-20</td>
<td>$E$</td>
<td>13.4 (0.12)</td>
<td>12.4 (0.06)</td>
<td>11.8 (0.03)</td>
<td>11.0 (0.09)</td>
<td>9.7 (0.13)</td>
</tr>
<tr>
<td></td>
<td>$\nu$</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
<td>0.3 (0.00)</td>
</tr>
<tr>
<td></td>
<td>$K$</td>
<td>10.7 (0.07)</td>
<td>10.0 (0.09)</td>
<td>9.4 (0.08)</td>
<td>8.7 (0.06)</td>
<td>7.8 (0.04)</td>
</tr>
<tr>
<td></td>
<td>$G$</td>
<td>5.2 (0.05)</td>
<td>4.8 (0.02)</td>
<td>4.6 (0.02)</td>
<td>4.3 (0.04)</td>
<td>3.8 (0.06)</td>
</tr>
<tr>
<td></td>
<td>$K/G$</td>
<td>2.1 (0.02)</td>
<td>2.1 (0.02)</td>
<td>2.1 (0.02)</td>
<td>2.0 (0.02)</td>
<td>2.1 (0.03)</td>
</tr>
</tbody>
</table>

decreased as the temperature increases. This conclusion is consistent with the trend that the binding energy of the co-crystal decreases with increasing temperature.

### 3.4 Mechanical properties
Mechanical properties are some of the most important properties of energetic materials due to their relationship with material preparation, storage, transportation and usage. The elastic modulus is an indicator of material stiffness and a measurement of material resistance to elastic deformation. Plastic and fracture properties can be related to the elastic modulus. The greater the shear modulus is, the larger the hardness and yield strength are, which are the resistance to plastic deformation. The greater the bulk modulus is, the larger the fracture strength is. The quotient $K/G$ empirically indicates the extent of the plastic range of a material. A high value of $K/G$ is associated with ductility and a low value with brittleness. $^{29}$

Table 4 summarizes the calculated moduli, Poisson's ratios and quotients $K/G$ of the four models (β-HMX crystal, ε-CL-20 crystal, ε-CL-20/HMX composite and cocrystal) based on fluctuation analysis of the production trajectories and Reuss average$^{30,31}$ at different temperatures. As shown in Table 4, as the temperature increases, the elastic moduli of the four systems all decrease, indicating that the stiffness, hardness, yield strength and fracture strength of the materials are diminished with increasing temperature. At the same temperature, the moduli of the ε-CL-20/HMX composite and cocrystal are smaller than those of ε-CL-20 and β-HMX crystals, but the quotients $K/G$ of the composite and the cocrystal are higher than those of ε-CL-20 and β-HMX crystals, *i.e.* the ductility of both the composite and the cocrystal is better than those of the two crystals.

## 4 Conclusions
In this study, NPT-MD simulations have been performed for ε-CL-20, β-HMX, ε-CL-20/HMX composites and the ε-CL-20/HMX cocrystal. Major findings can be summarized as follows:
(1) $L_{\text{max}}$ of the N-NO₂ trigger bond increases monotonously with increasing temperature, which has proved that $L_{\text{max}}$ can be used as a theoretical judgment of the heat and impact sensitivity for these energetic systems. At the same temperature, $L_{\text{max}}$ was compared for the three materials and as a result ε-CL-20/HMX(cocrystal) < ε-CL-20/HMX(composite) < ε-CL-20 crystal, indicating that the formation of the cocrystal can reduce sensitivity and improve safety.
(2) CEDs of the ε-CL-20/HMX cocrystal and composite both decrease with increasing temperature, suggesting that the energy needed for transferring from the condensed phase to the gas phase (CED) can also be used to correlate with the heat and impact sensitivity. CED of the cocrystal is higher than that of the composite at the same temperature, indicating that the co-crystal system is more stable and insensitive than the ordinary composite, namely, cocrystallization can reduce sensitivity.
(3) Binding energy ($E_{\text{bind}}$) between CL-20 and HMX decreases with increasing temperature. $E_{\text{bind}}$ of the CL-20/HMX cocrystal is much higher than that of the composite, because the interactions between different components in cocrystal are layer-layer having larger interaction area, while for the composite, the interactions only exist at the interfaces. The pair correlation function $g(r)$ reveals that the hydrogen bond interactions in the cocrystal and the composite mainly originate from H of CL-20 and O of HMX, H of HMX and O of CL-20, and decrease slightly as the temperature increases.
(4) Compared with the mechanical properties of pure components (ε-CL-20 and β-HMX), the stiffness of both the CL-20/HMX cocrystal and the composite is smaller, while $K/G$ is larger, indicating that the ductility of the cocrystal and the composite is better.

## Acknowledgements
This work is supported by the grant from the Joint Fund of National Natural Science Foundation of China and China Academy of Engineering Physics (NSAF) (Grant no. U1230120).

## References
1 J. P. Agrawal, Recent trends in high-energy materials, *Progr. Energ. Combust. Sci.*, 1998, **24**(1), 1-30.
2 A. K. Sikder and N. Sikder, A review of advanced high performance, insensitive and thermally stable energetic materials emerging for military and space applications, *J. Hazard. Mater.*, 2004, **112**(1), 1-15.
3 O. Bolton and A. J. Matzger, Improved Stability and Smart-Material Functionality Realized in an Energetic Cocrystal, *Angew. Chem., Int. Ed.*, 2011, **50**(38), 8960-8963.
4 O. Bolton, L. R. Simke, P. F. Pagoria and A. J. Matzger, High Power Explosive with Good Sensitivity: A 2: 1 Cocrystal of CL-20: HMX, *Cryst. Growth Des.*, 2012, **12**(9), 4311-4314.
5 F. Lara-Ochoa and G. Espinosa-Perez, Cocrystals Definitions, *Supramol. Chem.*, 2007, **19**(8), 553-557.
6 N. Shan and M. J. Zaworotko, The role of cocrystals in pharmaceutical science, *Drug Discovery Today*, 2008, **13**(9), 440-446.
7 W. H. Zhu, J. J. Xiao, G. F. Ji, F. Zhao and H. M. Xiao, First-principles study of the four polymorphs of crystalline octahydro-1, 3, 5, 7-tetranitro-1, 3, 5, 7-tetrazocine, *J. Phys. Chem. B*, 2007, **111**(44), 12715-12722.
8 J. P. Agrawal, Some new high energy materials and their formulations for specialized applications, *Propellants, Explos., Pyrotech.*, 2005, **30**(5), 316-328.
9 M. F. Foltz, C. L. Coon, F. Garcia and A. L. Nichols, The thermal stability of the polymorphs of hexanitrohexaazaisowurtzitane, Part I, *Propellants, Explos., Pyrotech.*, 1994, **19**(1), 19-25.
10 H. M. Xiao, X. J. Xu and L. Qiu, *Theoretical Design of High Energy Density Materials*, Science press, Beijing, 2008.
11 H. Sun, COMPASS: An ab initio force-field optimized for condensed-phase applications overview with details on alkane and benzene compounds, *J. Phys. Chem. B*, 1998, **102**(38), 7338-7364.

12 X. J. Xu, H. M. Xiao, J. J. Xiao, W. Zhu, H. Huang and J. S. Li, Molecular dynamics simulations for Pure $\varepsilon$-CL-20 and $\varepsilon$-CL-20-based PBXs, *J. Phys. Chem. B*, 2006, **110**(14), 7203-7207.

13 X. J. Xu, J. J. Xiao, H. Huang and J. S. Li, Molecular dynamics simulations on the structures and properties of $\varepsilon$-CL-20-based PBXs—primary theoretical studies on HEDM formulation design, *Sci. China, Ser. B: Chem.*, 2007, **50**(6), 737-745.

14 J. J. Xiao, W. R. Wang, J. Chen, G. F. Ji, W. Zhu and H. M. Xiao, Study on structure, sensitivity and mechanical properties of HMX and HMX-based PBXs with molecular dynamics simulation, *Comput. Theor. Chem.*, 2012, 21-27.

15 J. J. Xiao, W. H. Zhu, W. Zhu and H. M. Xiao, *Molecular Dynamics of Energetic Materials*, Science press, Beijing, 2013.

16 X. Q. Zhao and N. C. Shi, Crystal structure of $\varepsilon$-hexanitrohexaazaisowurtzitane, *Chin. Sci. Bull.*, 1995, **40**(23), 2158-2160.

17 C. S. Choi and H. P. Boutin, A study of the crystal structure of $\beta$-cyclotetramethylene tetranitramine by neutron diffraction, *Acta Crystallogr., Sect. B: Struct. Crystallogr. Cryst. Chem.*, 1970, **26**(9), 1235-1240.

18 H. C. Andersen, Molecular dynamics simulations at constant pressure and/or temperature, *J. Chem. Phys.*, 1980, **72**(4), 2384.

19 M. Parrinello and A. Rahman, Polymorphic transitions in single crystals: A new molecular dynamics method, *J. Appl. Phys.*, 1981, **52**, 7182.

20 M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids*, Oxford university press, 1989.

21 P. P. Ewald, Evaluation of optical and electrostatic lattice potentials, *Ann. Phys.*, 1921, **64**, 253-287.

22 P. Politzer, J. S. Murray, P. Lane, P. Sjoberg and H. G. Adolph, Shock-sensitivity relationships for nitramines and nitroaliphatics, *Chem. Phys. Lett.*, 1991, **181**(1), 78-82.

23 X. J. Xu, W. H. Zhu and H. M. Xiao, DFT studies on the four polymorphs of crystalline CL-20 and the influences of hydrostatic pressure on $\varepsilon$-CL-20 crystal, *J. Phys. Chem. B*, 2007, **111**(8), 2090-2097.

24 R. L. Simpson, P. A. Urtiew, D. L. Ornellas, G. L. Moody, K. J. Scribner and D. M. Hoffman, CL-20 performance exceeds that of HMX and its sensitivity is moderate. *Propellants, Explosives, Pyrotechnics*, 1997, **22**(5), 249-255.

25 L. Ding, F. Q. Zhao and Z. R. Liu, Thermal decomposition of CL-20/HMX mixed system, *J. Solid Rocket Technol.*, 2008, **31**(2), 164-167.

26 H. Liu, Q. K. Li and Y. H. He, Pyrolysis of CL20-TNT cocrystal from ReaxFF/lg Reactive Molecular Dynamics Simulations, *Acta Phys. Sin.*, 2013, **62**(20), 208202.

27 X. J. Xu, H. M. Xiao, X. H. Ju and X. D. Gong, Theoretical Study on Pyrolysis Mechanism for $\varepsilon$-Hexanitrohexaazaisowurtzitane, *Chin. J. Inorg. Chem.*, 2005, **25**(5), 536-539.

28 M. Geetha, U. R. Nair, D. B. Sarwade, G. M. Gore, S. N. Asthana and H. Singh, Studies on CL-20: the most powerful high energy material, *J. Therm. Anal. Calorim.*, 2003, **73**(3), 913-922.

29 S. F. Pugh, Relations between the elastic moduli and the plastic properties of polycrystalline pure metals, *Philos. Mag.*, 1954, **45**(367), 823-843.

30 M. Parrinello and A. Rahman, Strain fluctuation and elastic constants, *J. Chem. Phys.*, 1982, **76**, 2662-2666.

31 J. P. Watt, G. F. Davies and R. J. O'Connell, The Elastic properties of composite materials, *Rev. Geophys. Space Phys.*, 1976, **14**, 541-563.