### FULL PAPER

# Identification of decomposition reactions for HMDSO organosilicon using quantum chemical calculations

Yaosong Huang | Yugong Chen | Mingfei Zhou

College of Energy, Soochow University,
Suzhou, China

Correspondence
Yaosong Huang, College of Energy, Soochow
University, Suzhou 215006, China.
Email: yshuang@suda.edu.cn

## Abstract
Hexamethyldisiloxane [HMDSO, $(CH_{3})_{3}$-SiOSi-$(CH_{3})_{3}$] is an important precursor for $SiO_{2}$ formation during flame-based silica material synthesis. As a result, HMDSO reactions in flame have been widely investigated experimentally, and many results have indicated that HMDSO decomposition reactions occur very early in this process. In this paper, quantum chemical calculations are performed to identify the initial decomposition of HMDSO and its subsequent reactions using the density functional theory at the level of B3LYP/6-311+G (d, p). Four reaction pathways-(a) Si-O bond dissociation of HMDSO, (b) Si-C bond disso- ciation of HMDSO, (c) dissociation and recombination of Si-O and Si-C bonds, and (d) elimination of a methane molecule from HMDSO-have been examined and identified. From the results, it is found that the barrier of 84.38 kcal/mol and Si-O bond dissociation energy of 21.55 kcal/mol are required for the initial decomposition reaction of HMDSO in the first pathway, but the highest free energy barrier (100.69 kcal/mol) is found in the third reaction pathway. By comparing the free energy barriers and reaction rate constants, it is concluded that the most possible initial decomposition reaction of HMDSO is to eliminate the $CH_{3}$ radical by Si-C bond dissociation.

## KEYWORDS
decomposition reaction, density functional theory, quantum chemical calculation, rate constant

---

## 1 | INTRODUCTION

As one of the organosilicons, hexamethyldisiloxane (HMDSO, $C_{6}H_{18}Si_{2}O$) has been widely used to fabricate flame-based silica materials, such as silica nanoparticles, film and glass, etc. $^{[1-3]}$ Compared to the traditional precursor $SiCl_{4}$, no acidic products (such as $HCl$ and $Cl_{2}$) are generated for HMDSO combustion in the flame. Thus, HMDSO has been taken as an ideal precursor for $SiO_{2}$ generation without acid pollution. The reaction kinetics of HMDSO significantly affects the flame temperature and some key species formation (eg, $SiO_{2}$ and $CH_{3}$ radicals) and ultimately influences the structure and composition of synthetic silica materials. $^{[4,5]}$ This means that HMDSO chemical reactions are crucial in the synthesis of silica materials. As the initial reaction steps of HMDSO combustion, HMDSO decomposition reactions are of considerable importance as they have a great influence on the subsequent chemical reactions and accuracy of combustion simulations. $^{[4,6,7]}$

Experimental studies on HMDSO decomposition reactions have been conducted by Chernyshev et al. $^{[8]}$ at $675^{\circ}C$ in a flow reactor. Based on the initial products, two possible reaction schemes were proposed. The first scheme described the dissociation of the Si-O bond to produce the radicals of trimethylsilyl and trimethylsilyloxyl, and the second scheme was considered to yield the species of tetramethylsilane (TMS) and dimethylsilanone by chemical bond dissociation and rearrangement. Alexander et al. $^{[9]}$ reported another initial reaction step for HMDSO decomposition, which eliminated a methyl radical to produce the pentamethyldisiloxane. This scheme is also considered to be the result of Si-C bond dissociation. Besides these, considering the possibility of C-H bond cleavage, the elimination of a hydrogen atom from the HMDSO molecule to form a methane molecule through the rearrangement of hydrogen

atom and methyl radical is possible. However, this reaction scheme had not been studied in the past. In addition, the initial reaction products of HMDSO in the above-mentioned schemes can further decompose into small intermediate species through subsequent reaction pathways, but this is rarely reported.

Currently, few studies have been reported to identify the reaction pathways of HMDSO decomposition and calculate the reaction rate constants. Due to difficulty in the measurements of products and elementary reactions, theoretical investigations are conducted using the quantum chemical calculation method in this paper based on density functional theory (DFT). As an outline, the computational details are shown in Section 2. Identification of HMDSO decomposition pathways and calculation of the reaction rate constants are performed in Section 3. Conclusions are presented in Section 4.

## 2 | COMPUTATIONAL DETAILS

The calculations are performed in Gaussian 09 quantum chemistry software $^{[10]}$ using the DFT with Becke's three-parameter hybrid density functional and Lee-Yang-Parr correlation functional approximation (B3LYP). $^{[11]}$ The coupled-cluster singles and doubles (CCSD) $^{[12]}$ model is also used to obtain additional data to benchmark the calculated results from DFT. Ground-state geometries of the reactants, products, and transition states are optimized using the basis set of 6-311+G (d, p). To determine the transition states, relaxed scanning along the reaction coordinate is first conducted to obtain an initial guess structure of the transition state. Then, the initial guess structure with the maximum energy is further optimized to find the closest saddle point using the Berny algorithm. $^{[13]}$ If only one imaginary frequency is found in the frequency analysis, the transition states will be identified. After that, intrinsic reaction coordinate (IRC) calculations are also conducted to verify whether the identified transition states indeed connect the reactants to products. The maximum points of each IRC calculation are set to 120, with a step size equal to 5.

Thermochemistry data of elementary reactions is calculated. As the aim of this work is to identify the decomposition reactions, only the reaction enthalpy $\Delta H_{r}$, reaction Gibbs free energy $\Delta G_{r}$, and activation barriers (ie, $\Delta H_{f}^{\ddagger}$ and $\Delta G_{f}^{\ddagger}$) are calculated and analyzed. $\Delta H_{r}$ and $\Delta G_{r}$ are defined as the differences of enthalpy and Gibbs free energy between the products and reactants, respectively. $\Delta H_{f}^{\ddagger}$ and $\Delta G_{f}^{\ddagger}$ are defined as the differences of enthalpy and Gibbs free energy between the transition states and reactants, respectively. In the above thermochemistry calculations, zero-point energy correction has been performed. The temperature-dependent rate constants $k(T)$ are computed at temperatures of 298.15, 1000, 1500, 2000, and 2500 K using the conventional transition state theory (TST), that is,

$$
k(T)=\kappa \sigma \frac{k_{\mathrm{B}} T}{h} \exp \left(-\frac{\Delta G_{f}^{+^{\ddagger}}}{R T}\right)
$$

where $\kappa$ is the transmission coefficient of the tunneling effect, which is calculated using the Wigner method. $^{[14]} \sigma$ is the reaction path symmetry number, $\sigma=\sigma_{\mathrm{rot}, \mathrm{R}} / \sigma_{\mathrm{rot}, \mathrm{TST}}$, where $\sigma_{\mathrm{rot}, \mathrm{R}}$ and $\sigma_{\mathrm{rot}, \mathrm{TST}}$ are the rotational symmetry numbers of the reactant and transition state, respectively. $k_{\mathrm{B}}, h$, and $R$ are Boltzmann's constant, Planck's constant, and universal gas constant, respectively. $\Delta G_{f}^{\ddagger}$ is the Gibbs free energy of activation for the forward reaction. The parameters $\kappa, \sigma$, and $\Delta G_{f}^{\ddagger}$ can be calculated using the Gaussian output files.

## 3 | RESULTS AND DISCUSSION

To investigate the reaction pathways of HMDSO decomposition, molecular structures for all reactants and productions are first optimized. The initial guess geometry for HMDSO molecule is shown in Figure 1A with the bond angle of Si-O-Si equal to $150^{\circ} \mathrm{C}$ and bond lengths of $\mathrm{Si}-\mathrm{O}$ and

![](./images/812575376206200834_1.jpg)

FIGURE 1 Geometries of HMDSO with the A, initial structure and B, optimized structure

Si—C equal to 1.43 and 1.51 Å, respectively. After optimization to energy minimum at 298.15 K, the lengths of Si—O bond and Si—C bond become 1.65 and 1.88 Å, respectively, and the bond angle of Si—O—Si becomes 179°C, as shown in Figure 1B. Frequency calculation is also performed to obtain the thermochemistry data. According to the bond dissociation of HMDSO, four reaction pathways of the thermal decomposition of HMDSO are studied in the present work, including the pathways named P1 due to Si—O bond breaking, P2 due to Si—C bond breaking, P3 due to dissociation and recombination of Si—O and Si—C bonds, and P4 due to CH₄ elimination.

## 3.1 | Reaction pathway P1: Si—O bond dissociation

HMDSO first decomposes into trimethylsilyloxyl (CH₃)₃SiO and trimethylsilyl Si(CH₃)₃ via Si—O bond dissociation, as shown in reaction (1). The enthalpy and Gibbs free energy of HMDSO, (CH₃)₃SiO, and Si(CH₃)₃ calculated by DFT and CCSD are presented in Table 1. The relative errors between DFT and CCSD are less than 0.3%. This indicates that the DFT has comparable computational accuracy with the gold-standard theory. Therefore, DFT is used in the later calculations.

The numbers above the arrow in reaction (1) are the Gibbs free energy of activation and Gibbs free energy of reaction (in parenthesis), respectively, that is, $\Delta G^{\ddagger}_{f}$ (in kcal/mol) and $\Delta G_{r}$ (in kcal/mol). The numbers below the arrow are the activation enthalpy $\Delta H^{\ddagger}_{f}$ (in kcal/mol) and reaction enthalpy $\Delta H_{r}$ (in kcal/mol) (in parenthesis). To find the transition state of the reaction, relaxed scanning is first performed to obtain an initial guess structure of the transition state. Then, the guess molecular structure is further optimized to find the closest saddle point that has only one imaginary frequency. For reaction (1), the barrier is found to be 84.38 kcal/mol, and dissociation energy of the Si—O bond is 21.55 kcal/mol. The subsequent decomposition reactions of Si(CH₃)₃ and Si(CH₃)₂ have been reported in reference.¹⁵

Reactions (2) to (6) occur due to further decomposition of the intermediate species (CH₃)₃SiO, (CH₃)₂SiO, CH₃SiO, CH₂SiO etc. For instance, (CH₃)₃SiO decomposes into (CH₃)₂SiO and CH₃ radical with the free energy barrier of 55.93 kcal/mol, as shown in reaction (2). After that, two reaction pathways are possible for the subsequent decomposition of (CH₃)₂SiO. The first one is to eliminate a CH₄ molecule through the dissociation of Si—C bond and C—H bond, followed by recombination (see reaction 3). This reaction takes place with a barrier of 82.95 kcal/mol. The second is to eliminate a methyl radical by Si—C bond dissociation with the barrier of 73.4 kcal/mol, as shown in reaction 4. Finally, both the products CH₂SiO and CH₃SiO decompose into SiO, as shown in reactions (5) and (6). The barriers for these two reactions are 82.62 kcal/mol and 34.74 kcal/mol, respectively.

<table>
<caption>TABLE 1 The calculated enthalpy and Gibbs free energy (Hartree) for the reactants and products in reaction (1)</caption>
<thead>
<tr>
<th>Reactant/product</th>
<th>Enthalpy (DFT)</th>
<th>Enthalpy (CCSD)</th>
<th>Free energy (DFT)</th>
<th>Free energy (CCSD)</th>
</tr>
</thead>
<tbody>
<tr>
<td>HMDSO</td>
<td>−893.615452</td>
<td>−890.981444</td>
<td>−893.676720</td>
<td>−891.046126</td>
</tr>
<tr>
<td>(CH₃)₃SiO</td>
<td>−484.421150</td>
<td>−482.984478</td>
<td>−484.463326</td>
<td>−483.026556</td>
</tr>
<tr>
<td>Si(CH₃)₃</td>
<td>−409.159962</td>
<td>−407.989359</td>
<td>−409.199306</td>
<td>−408.028748</td>
</tr>
</tbody>
</table>

![](./images/812575376206200834_2.jpg)

FIGURE 2 Gibbs free energy profile for reaction pathway P1. TS1 to TS6 are the transition states for reactions 1 to 6

![](./images/812575376206200834_3.jpg)

Figure 2 shows the Gibbs free energy profile for HMDSO decomposition pathway P1. The vertical y-axis and horizontal x-axis represent the Gibbs free energy and reaction coordinate, respectively. The number above the peak of the curve is Gibbs free energy of activation, and

the number below the local minima of the curve is the Gibbs free energy of reaction, with the presentation of the corresponding reactants or products. As shown, it is found that the free energy barrier of $CH_4$ molecule elimination from reaction (3) is 82.95 kcal/mol, while the $CH_3$ radical elimination from reaction (4) is only 73.40 kcal/mol. This indicates that it is more likely to directly eliminate $CH_3$ radical using reaction (4). To further validate this conclusion, the rate constant $k_3$ of reaction (3) and rate constant $k_4$ of reaction (4) are calculated at a high temperature (ie, 1000, 2000, and 2500 K) using TST theory. The ratios of $k_4$/$k_3$ at 1000, 2000, and 2500 K are 105, 10.6, and 6.7, respectively. Hence, it is more likely that the $CH_3$ radical is eliminated at a temperature below 2500 K. However, it is found that, with the temperature increasing, the ratio of $k_4$/$k_3$ decreases. This indicates that reaction (3) can compete with reaction (4) if the reactive temperature is over 2500 K.

## 3.2 | Reaction pathway P2: Si—C bond dissociation

The HMDSO molecule has a relatively weak Si—C bond, which can be broken down to remove a methyl radical, as shown in reaction (7). This reaction occurs with the barrier of 37.92 kcal/mol and is exothermic by 12.97 kcal/mol. After that, the trimethylsilyloxyl $(CH_3)_3SiO$ and dimethylsiloxane $(CH_3)_2SiO$ are formed due to the thermal decomposition of the product $(CH_3)_3SiOSi(CH_3)_2$ according to different breaking locations of Si—O bond. It is found that the dissociation energy of Si—O bond for $(CH_3)_3SiO$ formation is 92.5 kcal/mol, as shown in reaction (8), while the dissociation energy of Si—O bond for $(CH_3)_2SiO$ formation is only 58.27 kcal/mol (see reaction 9). This indicates that more heat is needed to form $(CH_3)_3SiO$. The subsequent reaction pathways for $(CH_3)_3SiO$ or $(CH_3)_2SiO$ decomposition will follow reactions (2) to (6) or (3) to (6).

Figure 3 shows the Gibbs free energy profile for reactions (7) to (9) in the HMDSO decomposition pathway P2. As shown, the high free energy barrier is required for $(CH_3)_2SiO$ formation, which is nearly twice as large as the one of $(CH_3)_3SiO$ formation. This means that it is much easier to break down the Si—O bond that has a lower number of $CH_3$ radicals connected to Si atom during $(CH_3)_3SiOSi(CH_3)_2$ decomposition.

![](./images/812575376206200834_4.jpg)

### 3.3 | Reaction pathway P3: dissociation and recombination of Si—O and Si—C bonds

According to the experimental results, $^{[6]}$ dimethylsiloxane $((CH_3)_2SiO)$ and etramethylsilane $((CH_3)_4Si)$ are found during HMDSO decomposition. This can be attributed to the dissociation of chemical bond Si—O and dissociation and recombination of Si—C bond, as shown in reaction (10). A total barrier of 100.69 kcal/mol is required for Si—O bond dissociation and Si—C bond dissociation and recombination. Heat absorption is 61.71 kcal/mol for this reaction, and the free energy of this reaction is 55.23 kcal/mol. The decomposition pathway of the intermediate product $(CH_3)_2SiO$ can be described using the reactions (3) to (6).

![](./images/812575376206200834_5.jpg)

### 3.4 | Reaction pathway P4: elimination of a methane molecule

Direct elimination of a methane molecule from HMDSO occurs during the initial thermal decomposition reactions of HMDSO, as shown in reaction (11). This is attributed to the dissociation of H atom and its recombination with a methyl radical. Thus, a barrier of 45.41 kcal/mol is required for this reaction, and the corresponding heat release is 53.71 kcal/mol. After that, the product $(CH_3)_3SiOSiCH_3CH_2$ further decomposes into the molecules of $(CH_3)_2SiO$ and $SiCH_3CH_2$ by absorbing the heat of 117.05 kcal/mol, as shown in reaction (12). The free energy barrier is 93.18 kcal/mol for this reaction. Decomposition of $(CH_3)_2SiO$ can be described via reactions (3) to (6).

![](./images/812575376206200834_6.jpg)

![](./images/812575376206200834_7.jpg)

### 3.5 | Comparison of HMDSO decomposition reaction pathways

Based on the above discussion, four reaction pathways are identified during the initial thermal decomposition of HMDSO. The Gibbs free energy profiles for the pathways are shown in Figure 4. Barriers for the four reactions are 84.38, 37.79, 100.69, and 45.41 kcal/mol, respectively. This indicates that the most possible pathway for HMDSO initial decomposition is to remove a $CH_3$ radical by Si—C dissociation (ie, pathway P2), followed by pathways P4, P1, and P3. This can be validated by the reaction rate constants that are shown in Table 2. As shown, five temperature

FIGURE 3 Gibbs free energy profile for decomposition pathway P2. TS7 to TS9 are transition states for reactions 7 to 9

![](./images/812575376206200834_8.jpg)

FIGURE 4 Gibbs free energy profiles for HMDSO initial decomposition pathways

![](./images/812575376206200834_9.jpg)

TABLE 2 Rate constants for HMDSO initial thermal decomposition reactions

<table>
  <thead>
    <tr>
      <th>Temperature (K)</th>
      <th>$k_1$ ($s^{-1}$)</th>
      <th>$k_7$ ($s^{-1}$)</th>
      <th>$k_{10}$ ($s^{-1}$)</th>
      <th>$k_{11}$ ($s^{-1}$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>298.15</td>
      <td>$8.30 \times 10^{-50}$</td>
      <td>$9.70 \times 10^{-16}$</td>
      <td>$9.10 \times 10^{-62}$</td>
      <td>$3.12 \times 10^{-21}$</td>
    </tr>
    <tr>
      <td>1000</td>
      <td>$4.43 \times 10^{-6}$</td>
      <td>$1.07 \times 10^{5}$</td>
      <td>$2.02 \times 10^{-9}$</td>
      <td>$2.46 \times 10^{3}$</td>
    </tr>
    <tr>
      <td>1500</td>
      <td>$1.57 \times 10^{1}$</td>
      <td>$9.29 \times 10^{7}$</td>
      <td>$6.59 \times 10^{-2}$</td>
      <td>$7.52 \times 10^{6}$</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>$2.49 \times 10^{4}$</td>
      <td>$2.98 \times 10^{9}$</td>
      <td>$4.10 \times 10^{2}$</td>
      <td>$4.53 \times 10^{8}$</td>
    </tr>
    <tr>
      <td>2500</td>
      <td>$2.18 \times 10^{6}$</td>
      <td>$2.52 \times 10^{10}$</td>
      <td>$8.15 \times 10^{4}$</td>
      <td>$5.57 \times 10^{9}$</td>
    </tr>
  </tbody>
</table>

points are calculated, that is, 298.15, 1000, 1500, 2000, and 2500 K. At the same temperature, the rate constant is $k_7 > k_{11} > k_1 > k_{10}$, which corresponds to the HMDSO decomposition pathway: P2 → P4 → P1 → P3. It was also found that the rate constant at 298.15 K is close to zero, indicating that HMDSO thermal decomposition cannot occur at low temperatures, while with the temperature increasing, the rate constant rises rapidly, especially at high temperatures above 1500 K.

## 4 | CONCLUSIONS

Quantum chemical calculations are performed to investigate HMDSO thermal decomposition reactions. Four reaction pathways that include the initial decomposition of HMDSO and subsequent reactions of intermediates are identified. For the first pathway P1, that is, Si—O bond dissociation of HMDSO, the initial dissociation step of HMDSO has a barrier of 84.38 kcal/mol and an Si—O bond dissociation energy of 21.55 kcal/mol. In the subsequent decomposition of (CH₃)₂SiO, it is more likely for a CH₃ radical to be eliminated at temperatures below 2500 K, while at higher temperatures, such as above 2500 K, the CH₄ elimination reaction can compete with the reaction of CH₃ elimination. For the second pathway P2, that is, Si—C bond dissociation of HMDSO, a barrier of 37.92 kcal/mol is needed for Si—C bond dissociation to eliminate a CH₃ radical, and this reaction is exothermic by 12.97 kcal/mol. The free energy barrier for (CH₃)₂SiO formation is nearly twice as large as the one of (CH₃)₃SiO formation, indicating that it is much easier to break down the Si—O bond that has a lower number of CH₃ radicals connected to an Si atom during (CH₃)₃SiOSi(CH₃)₃ decomposition. For the third pathway P3, that is, dissociation and recombination of Si—O and Si—C bonds, the high free energy barrier is found, which reaches 100.69 kcal/mol. For the fourth pathway P4, that is, elimination of a methane molecule from HMDSO, the dissociation of H atom and its recombination with CH₃ to form a CH₄ molecule need to overcome the free energy barrier of 45.41 kcal/mol. Through the comparison of the four decomposition reaction pathways, it was found that the most possible pathway is to eliminate a CH₃ radical by Si—C dissociation (ie, pathway P2), followed by the pathways of P4, P1, and P3. This can also be validated through the reaction rate constant calculation using the TST.

## AUTHOR CONTRIBUTIONS

Yaosong Huang: Formal analysis; investigation; methodology; software; writing-original draft; writing-review and editing. Yugong Chen: Methodology; software. Mingfei Zhou: Formal analysis; methodology; resources.

## ORCID

Yaosong Huang https://orcid.org/0000-0001-7402-8741

## REFERENCES

[1] O. M. Feroughi, L. Deng, S. Kluge, T. Dreier, H. Wiggers, I. Wlokas, C. Schulz, *Proc. Combust. Inst.* 2017, 36, 1045.
[2] Y. Jia, R. Yue, G. Liu, J. Yang, Y. Ni, X. Wu, Y. Chen, *Appl. Surf. Sci.* 2013, 265, 405.
[3] F. Seishi, K. Norio, J. Hiroki, *European Patent EP0908418 A1*, 1999.
[4] A. Rittler, L. Deng, I. Wlokas, A. M. Kempf, *Proc. Combust. Inst.* 2017, 36, 1077.
[5] S. M. C. Robin, J. Hossein, D. Thomas, W. Hartmut, W. Irenäus, S. Christof, *Proc. Combust. Inst.* 2019, 37, 1221.
[6] C. L. Yeh, E. Zhao, H. K. Ma, *J. Therm. Sci.* 2001, 10, 92.
[7] H. K. Chagger, D. Hainsworth, P. M. Patterson, M. Pourkashanian, A. Williams, *Symp. Combust.* 1996, 26, 1859.
[8] E. A. Chernyshev, T. L. Krasnova, A. P. Sergeev, E. S. Abramova, *Russ. Chem. B+* 1997, 46, 1586.
[9] M. R. Alexander, F. R. Jones, R. D. Short, *J. Phys. Chem. B* 1997, 101, 3614.
[10] M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheese-man, G. Scalmani, V. Barone, B. Mennucci, G. A. Petersson, H. Nakatsuji, M. Car-icato, X. Li, H. P. Hratchian, A. F. Izmaylov, J. Bloino, G. Zheng, J. L. Sonnenberg, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, J. A. Montgomery, J. E. Peralta, F. Ogliaro, M. Bearpark, J. J. Heyd, E. Brothers, K. N. Kudin, V. N. Staroverov, R. Kobayashi, J. Normand, K. Raghavachari, A. Rendell, J. C. Burant, S. S. Iyengar, J. Tomasi, M. Cossi, N. Rega, J. M. Millam, M. Klene, J. E. Knox, J. B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R. E. Stratmann, O. Yazyev, A. J. Austin, R. Cammi, C. Pomelli, J. W. Ochterski, R. L. Martin, K. Morokuma, V. G. Za-krzewski, G. A. Voth, P. Salvador, J. J. Dannenberg, S. Dapprich, A. D. Daniels, J. B. F. Farkas, J. V. Ortiz, J. Cioslowski, D. J. Fox, *Gaussian 09, Revision D. 01*, Gaussian Inc., Wallingford, CT 2009.
[11] P. J. Stephens, F. J. Devlin, C. F. Chabalowski, M. J. Frisch, *J. Phys. Chem.* 1994, 98, 11623.
[12] G. D. Purvis, R. J. Bartlett, *J. Chem. Phys.* 1982, 76, 1910.
[13] H. B. Schlegel, *J. Comput. Chem.* 1982, 3, 214.
[14] E. Georganta, R. K. Rahman, A. Raj, S. Sinha, *Combust. Flame* 2017, 185, 129.
[15] X. Liu, J. Zhang, A. Vazquez, D. Wang, S. Li, *Phys. Chem. Chem. Phys.* 2018, 20, 18782.

How to cite this article: Huang Y, Chen Y, Zhou M. Identification of decomposition reactions for HMDSO organosilicon using quantum chemical calculations. *Int J Quantum Chem.* 2020;e26415. https://doi.org/10.1002/qua.26415