# A DFT-D guided surface engineering of 2-D functionalized graphyne analogue covalent triazine frameworks as a high-capacity anode material of Mg-ion battery

Saeed Borhani, Morteza Moradi $^{*}$, Mehdi PooriRaj, Behnam Chameh

Department of Semiconductors, Materials and Energy Research Center (MERC), P.O. Box 31787-316, Tehran, Iran

---

## ARTICLE INFO

**Keywords:**
Mg-ion battery
Graphyne
DFT
CTF
Diffusion

---

## ABSTRACT

In the present study, we have explored the potential application of pure and functionalized 2-D graphyne-like covalent triazine framework (GYCTF) as an anode material for Mg-ion batteries, using dispersion-corrected DFT. The accurate interaction energies are crucial for energy storage and battery applications as they are directly related to the key properties in electrochemistry, such as storage capacities, in general, and open-circuit voltages (OCVs), in particular. We have found that Mg preferably adsorbs above the center of all carbon six-membered rings of GYCTF with adsorption energy of about 83.4 kcal mol⁻¹. After functionalization, -SH increases the maximum coverage of Mg on surface from 4 to 9 Mg. Also, -CH₃ strongly reduces the specific capacity of GYCTF in MIB application. After functionalization, -SH increases the maximum coverage of Mg on the surface from 4 to 9 Mg. Also, -CH3 strongly reduces the specific capacity of GYCTF in MIB application. The single-layer GYCTF-SH can be magnesiated on both sides yielding Mg₉C₁₃N₃S₄H₄ with a storage capacity as high as 1462.4 mAh g⁻¹ with an average OCV of 0.68 V. Our findings show better results in terms of storage capacity, negligible volume expansion, low OCV, and low diffusion energies comparing with commonly studied 2-D materials, making thiol-functionalized GYCTF a promising candidate as an anode material for Mg- ion batteries.

---

## 1. Introduction

All over the world, the need for fossil fuel sources is rapidly increasing year by year [1-3]. Overcoming these challenges is an important goal that can be achieved through developing different energy sources and energy storage systems. Currently, most of the energy storage industry has been dominated by lithium-ion batteries (LIBs) because of the intrinsic nature of lithium-ion, leading to reversible electrochemical processes, high energy density, cyclic stability, capacity, and wide voltage range [4]. However, the shortage of lithium resources, expensive cost, safety, and environmental issues originated from the organic electrolytes hinder the continuous large-scale applications of LIBs [5]. This situation has motivated researchers to look for alternative approaches in rechargeable battery systems based on non-lithium metal-ion batteries like sodium-ion batteries, zinc-ion batteries, magnesium-ion batteries, and so on [6,7].

Recently, rechargeable magnesium-ion batteries (MIBs) have been obtaining more and more attention thanks to a set of attractive advantages associated with multivalent Mg metal, including elemental abundance, a low relatively redox potential (-2.37 V vs. SHE), the high energy density per unit volume, high theoretical specific capacity (2205 Ah g⁻¹) [8], low cost, high safety, and low environmental impact [9]. Despite the mentioned benefits, narrow operating voltage window, poor reversible capacity, low Mg-ion conductivity, and the lack of suitable electrode materials hamper the development of MIBs [10]. Up to now, a wide verity of materials such as transition metal oxides [11], transition metal sulfides [12], carbon structures (e.g., graphene, graphite, and carbon nanotubes) [13], transition metal carbides (MXenes) [14], and transition metal dichalcogenides (TMDs) [15], have been investigated as electrode materials in MIBs.

Inspired by graphene, new organic and inorganic graphene-like 2-D materials like TMDs, MXenes, and germanene have been studied as cathode materials both experimentally and theoretically by researchers. As an example of another carbon allotrope, graphyne proposed by Baughman and coworkers [16], contain sp- and sp²-hybridized carbon atoms. Hexagons, formed by the sp²-hybridized C atoms, are connected through acetylenic linkages ($-\mathrm{C}\equiv\mathrm{C}-$). Recently, 2-D structures have been used extensively in MIBs due to their high electrical conductivity,

---

$^{*}$ Corresponding author.
E-mail address: m.moradialborzi@merc.ac.ir (M. Moradi).

https://doi.org/10.1016/j.surfin.2021.101313
Received 17 March 2021; Received in revised form 13 June 2021; Accepted 24 June 2021
Available online 2 July 2021
2468-0230/© 2021 Elsevier B.V. All rights reserved.

large redox active sites, and high volumetric capacity [17]. For example, Fan's group did fabricate $Ti_3C_2Tx@C$ (MXenes sandwiched by carbon nanospheres) as a cathode for MIBs through a self-assembly method forthe first time, providing remarkable specific capacity (198.7 mAh g $^{-1}$) and good rate capability (123.3 mAh g $^{-1}$) [18]. Therefore, electrode materials based on organic 2-D materials are promising candidates for MIBs.

Covalent organic frameworks (COFs) are primary 2-D or 3-D porous crystalline materials which are developed for the first time in 2005 [19,20]. COFs are synthesized through reacting organic units with strong covalent bonds and have attracted substantial attention since they benefit from unique properties such as high surface area, low mass density, and structural tenability [21,22]. In contrast to metal-organic frameworks (MOFs), COFs benefit from high chemical stability that makes them promising candidate materials for practical applications in gas storage [23], separation [24], catalysis, and energy storage and conversion [25]. Covalent triazine frameworks (CTFs) are a subclass of COFs that have a triazine covalent linkage (aromatic $C=N$ ring) between organic units in the extended network [26]. Generally, CTFs are syn- thesized in the presence of $ZnCl_2$ as the catalyst by polymerizing aro matic dinitriles at $400^{\circ}C$ [27]. CTFs can be utilized as desirable potential electrode materials in energy storage systems because they provide a designable network with open channels for the appropriate transport of electrons/ions [28]. Furthermore, alkali metal cations (e.g., $Li^{+},Na^{+},K^{+}$) and alkaline earth metal cations (e.g., $Mg^{+2},Ca^{+2}$) can form strong interactions with $\pi$-conjugated 2-D CTFs as well as graphene and other 2D carbon materials [29]. Therefore, it is worth considering the potential capability of 2-D CTF-based electrodes for robust metal-ion batteries. Recently, various researches have been conducted towards the use of CTFs in battery applications [30]. For example, Buyukcakir and co-workers have synthesized a novel redox-active CTF anode material for Li-ion batteries. The results have shown that polymeric framework with large specific surface area participate in redox reactions throughtriazine linkages and exhibit a high capacity (1190 mAh g $^{-1}$ at 0.5 C) and a superior rate capability, delivering the specific capacity of 520 and420 mAh g $^{-1}$ at 10 C and 20 C rates, respectively [31]. To the best of our knowledge, a few articles have focused on the DFT design of CFT as anode/cathode materials of metal-ion batteries. For instance, Ball et al. have theoretically investigated 2-D-CTF as the anode of Li-ion battery(LIB) with a high theoretical specific capacity of 925.99 mAh g $^{-1}$ and a moderately low diffusion barrier of 0.65 eV, and average OCVs lie in the range of 1.58-0.51 V [32]. In another work, Wu and coworkers have introduced a highly stable 3-D $\pi$-conjugation covalent triazine-cored framework (Azo-CTF) with triazine as the electron-rich center bridged by azo redox-active linkers is proposed and prepared as cathode mate- rials for improving both rate performance and cycle stability of LIBs, two critical issues addressed in organic electrodes [33]. Here, for the first time, inspired by the previous works, we introduce a DTF study on the possible application of pure and different functionalized graphyne-analogue CTFs as the anode material for MIBs in terms of cell voltage, ion mobility, energetics, charge transfer, and specific capacity. This study paves the way for us to understand the Mg-ion storage capability of CTFs for subsequent experimental research.

## 2. Computational methods
We selected a new and stable porous 2-D graphyne analogue CTFs nanostructure (GYCTF), which was recently synthesized by Chen et al. To avoid the boundary effects in CYCTFs, the end of atoms in these structures were saturated by hydrogen atoms [34]. Three parameter hybrid generalized gradient approximation with the B3LYP functional and the 6-13 G basis set consist of the D-polarization function (named6-31G(d)) as implemented in the GAMESS suit of the program [35] were utilized to the full geometry optimizations and calculation on the pure and four functionalized GYTCTFs (-CH3, -F, and -SH) in the presence and absence of Mg atoms. We used DFT-D to enhance the explanation of the long-range interaction [36]. The total energy is measured in the Grimme method as a function of diffusion factor for every pair of the atom, a global scaling factor, depending on the functional use of the exchange-correlation, and a damping function to prevent close singu- larities for short distances. GaussSum program [37] has been employed to get the density of states (DOS) results. Previously, regenerating experimental properties and the study of nanostructures have been done based on the B3LYP density functional [38-42]. The adsorption energy(Ead) of Mg atoms on both bare and modified surfaces obtained throughthe following equation:

$$
E_{\text {ad }}=[\mathrm{E}(\mathrm{GYCTF})+\mathrm{nE}(\mathrm{Mg})-(\mathrm{E}(\mathrm{nMg} / \mathrm{GYCTF})] / \mathrm{n} \tag{1}
$$

where $E$ (Mg/GYCTF) is the total energy of bare and functionalized GYCTF after 'n' Mg atom adsorption and E(GYCTF) is referred to as the energy of GYCTFs. The exothermic character of the adsorption is indi- cated by the position value of $E_{ad}$. The same level of theory has been used for performing the density of states (DOS), frontier molecular orbital(FMO), and all of the energy calculations. By natural bond orbitals(NBO) analysis, the net charge-transfer $(Q_{T})$ among Mg and GYCTFs is calculated to determine the variations in electronic charge through the carbon structures, defined as the difference in charge between the Mg adsorbed on the surface and an individual atom.

## 3. Results and discussion
### 3.1. Adsorption of Mg atoms on the bare GYCTF
In 2019, Chen et al have developed a bottom-up strategy to syn- thesize a new 2-D graphyne analogue Covalent Triazine Framework(GYCTF) through aromatic nucleophilic substitution reactions of cya- nuric chloride with 1,4- diethynyllithium benzene [34]. As indicated in Fig. 1a, the optimized unite cell of GYCTF is constructed by six all-carbon hexagonal rings $(C_{6})$ and six triazine hexagonal rings $(T_{6})$ so that $C_{6}$ and $T_{6}$ were connected by $-C \equiv C-$ linkage to each other. Obvi ously, GYVTF has two nonequivalent carbon atoms. As shown in Fig. 1, one is $sp^{2}$-hybridized (named as $C_{1}$ ) building hexagons, and another is sp-hybridized (named as $C_{2}$ ) connects the hexagons. In the optimized configuration, the bond length between two $sp^{2}$-hybridized carbon atoms is $1.40 \AA$ in $C_{6}$ , implying that the $\pi$-conjugate nature of graphene is kept in the hexagons and the bond length of C-N in $T_{6}$ rings is $1.37 \AA$ . The $-C \equiv C-$ triple bond is formed between the sp-hybridized carbon atoms of the chain because there is a short distance $(1.21 \AA)$ between them. It is worthy of note, the bond length of connected $C_{1}$ and $C_{2}$ atoms $(1.41 \AA)$ is much shorter than that of the normal single bond $(\sim 1.53 \AA)$ , indicating the $\pi$ binding between $C_{1}$ and $C_{2}$ atoms. In comparison with graphene, the existence of two-fold coordinated (sp-hybridized) carbon atoms in graphyne are more unfavorable energetically [43].

Effective adsorption of Mg on the host substrate is necessary for GYCTF to be a very appropriate anode material for the MIB. Our com- putations reveal that when an Mg atom is located above different carbon atoms, above $C_{6}$ and $T_{6}$ rings, or on top of the $C \equiv C$ bond, it moves throughout structural optimization to the center of the $C_{6}$ hexagonal ring, as shown in Fig. 2(a). This result agrees with the Mg adsorption on various aromatic carbonaceous nanomaterials, such as CNT [13]. It isestimated that the adsorption energy on the bare GYCTF for Mg is 83.4 kcal mol $^{-1}$ . Table 1 contains more detailed information obtained from the simulation of the various Mg-GYCTFs systems, including $E_{ad}$ values and the charge transfer $(Q_{T})$ for these configurations. The optimized configuration stands for a weak van der Waals interaction between Mg atom and bare sheet. The $E_{ad}$ results of Mg on the sheet in this structure and the transferred charge between them determine the physical nature of the interaction. A charge of approximately 0.111e is transferred from the sheet to the Mg, based on the NBO analysis. The second optimized configuration with $E_{ad}$ of near-zero $(0.45 kcal mol^{-1})$ and charge transfer of 0.002 e have shown in Fig. S1 (Supporting information). The

![](./images/812079174322749440_1.jpg)

Fig. 1. (a,b) Top and side view of bare GYCTF. (c) A slice of unit cell of GYCTF and (d) TDOS of GYCTF. Distances are in Å.

![](./images/812079174322749440_2.jpg)

Fig. 2. Optimized structure of nMg/GYCTF ($n=1$–4) and related TDOS.Distances are in Å.

adsorbing energies of the nMg/GYCTF ($n=2$, 3, and 4) structures are calculated and also indicated by the blue column in Fig. 3. The nMg/GYCTF structures possess Mg adsorbing energies in the range of 83.4 to 69.4 kcal mol⁻¹ which shows a slight reduction in $E_{\text{ad}}$ with increasing coverage. The stable configurations of nMg/GYCTF have shown in Fig. 2(b-d). We can assume that the adsorbed configurations of four Mg in bare GYCTF are stable, but the fifth Mg cannot adsorb exothermically on the studied sheet.

In order to get a deeper insight into the interactions between Mg and GYCTF, multiple Mg adsorbed sheets were further studied in terms of electronic properties. The high electronic conductivity of anode materials as a desirable factor has a major effect on the performance of MIB, especially its rate capability. The results of DOS and the $E_{\text{g}}$ between the highest occupied molecular orbitals (HOMOs) and the lowest unoccupied molecular orbitals (LUMOs) indicate that the pristine surface is a semiconductor (Fig. 1b). The bond length distribution of carbon-carbon bonds in GYCTF indicates that conjugate $\pi$ orbitals on the GYCTF basal plane formed by the coupling between C(2pz) orbitals. It is quite interesting that how the electronic structure of the sheet is controlled by the $\pi$-conjugated orbitals. Unlike the zero bandgap in graphene, GYCTF

<table><thead><tr><th>Configuration</th><th>$E_{ad}$</th><th>$^{a}Q_{T}$(|e|)</th><th>$E_{HOMO}$</th><th>$E_{LUMO}$</th><th>$E_{g}$</th><th>$^{b}\Delta E_{g}$(%)</th></tr></thead><tbody><tr><td>GYCTF</td><td>–</td><td>–</td><td>–6.24</td><td>–2.61</td><td>3.63</td><td>–</td></tr><tr><td>Mg/GYCTF</td><td>83.4</td><td>–0.111</td><td>–4.31</td><td>–2.80</td><td>1.51</td><td>–58.4</td></tr><tr><td>2Mg/GYCTF</td><td>76.3</td><td>–0.093</td><td>–4.25</td><td>–2.98</td><td>1.27</td><td>–65.0</td></tr><tr><td>3Mg/GYCTF</td><td>73.1</td><td>–0.091</td><td>–4.29</td><td>–3.04</td><td>1.25</td><td>–65.5</td></tr><tr><td>4Mg/GYCTF</td><td>69.4</td><td>–0.076</td><td>–4.29</td><td>–3.09</td><td>1.20</td><td>–67.0</td></tr><tr><td>GYCTF-CH₃</td><td>–</td><td>–</td><td>–5.91</td><td>–2.45</td><td>3.46</td><td>–</td></tr><tr><td>Mg-GYCTF-CH₃</td><td>75.1</td><td>–0.012</td><td>–4.32</td><td>–2.64</td><td>1.68</td><td>–51.4</td></tr><tr><td>2Mg-GYCTF-CH₃</td><td>67.5</td><td>–0.023</td><td>–4.23</td><td>–2.74</td><td>1.49</td><td>–57.0</td></tr><tr><td>3Mg-GYCTF-CH₃</td><td>58.2</td><td>–0.034</td><td>–4.14</td><td>–2.93</td><td>1.21</td><td>–65.0</td></tr><tr><td>4Mg-GYCTF-CH₃</td><td>47.5</td><td>–0.38</td><td>–4.16</td><td>–3.05</td><td>1.11</td><td>–68.0</td></tr><tr><td>GYCTF-F</td><td>–</td><td>–</td><td>–6.85</td><td>–3.24</td><td>3.61</td><td>–</td></tr><tr><td>Mg/GYCTF-F</td><td>45.7</td><td>–0.066</td><td>–4.01</td><td>–3.50</td><td>0.58</td><td>–83.9</td></tr><tr><td>2Mg/GYCTF-F</td><td>32.6</td><td>–0.063</td><td>–4.22</td><td>–3.70</td><td>0.58</td><td>–83.9</td></tr><tr><td>3Mg/GYCTF-F</td><td>28.7</td><td>–0.057</td><td>–4.33</td><td>–3.75</td><td>0.52</td><td>–85.6</td></tr><tr><td>4Mg/GYCTF-F</td><td>25.4</td><td>–0.051</td><td>–4.43</td><td>–3.92</td><td>0.51</td><td>–85.8</td></tr><tr><td>5Mg/GYCTF-F</td><td>23.1</td><td>–0.048</td><td>–4.46</td><td>–3.95</td><td>0.51</td><td>–85.8</td></tr><tr><td>6Mg/GYCTF-F</td><td>21.5</td><td>–0.047</td><td>–4.50</td><td>–3.98</td><td>0.51</td><td>–85.8</td></tr><tr><td>GYCTF-SH</td><td>–</td><td>–</td><td>–5.75</td><td>–3.30</td><td>2.45</td><td>–</td></tr><tr><td>Mg/GYCTF-SH</td><td>62.3</td><td>+0.134</td><td>–4.15</td><td>–3.56</td><td>0.59</td><td>–75.9</td></tr><tr><td>2Mg/GYCTF-SH</td><td>52.4</td><td>+0.122</td><td>–4.37</td><td>–3.78</td><td>0.59</td><td>–75.9</td></tr><tr><td>3Mg/GYCTF-SH</td><td>49.4</td><td>+0.117</td><td>–4.49</td><td>–3.81</td><td>0.55</td><td>–77.5</td></tr><tr><td>4Mg/GYCTF-SH</td><td>32.1</td><td>+0.103</td><td>–4.22</td><td>–3.75</td><td>0.47</td><td>–80.8</td></tr><tr><td>5Mg/GYCTF-SH</td><td>26.5</td><td>+0.098</td><td>–4.17</td><td>–3.69</td><td>0.47</td><td>–80.8</td></tr><tr><td>6Mg/GYCTF-SH</td><td>19.9</td><td>+0.082</td><td>–4.22</td><td>–3.77</td><td>0.45</td><td>–81.6</td></tr><tr><td>7Mg/GYCTF-SH</td><td>14.2</td><td>+0.075</td><td>–4.27</td><td>–3.82</td><td>0.45</td><td>–81.6</td></tr><tr><td>8Mg/GYCTF-SH</td><td>14.1</td><td>+0.072</td><td>–4.28</td><td>–3.87</td><td>0.41</td><td>–83.2</td></tr><tr><td>9Mg/GYCTF-SH</td><td>14.0</td><td>+0.068</td><td>–4.30</td><td>–3.85</td><td>0.41</td><td>–83.2</td></tr></tbody></table>

Table 1
Adsorption energy ($E_{ad}$ in kcal mol⁻¹), HOMO energies ($E_{HOMO}$), LUMO energies ($E_{LUMO}$) and HOMO-LUMO energy gap ($E_{g}$) of defected systems in eV. $QT$ is defined as the average NBO charge on the Mg atoms.

owns a wide bandgap of 3.63 eV. Calculated DOS plots for four com- plexes are shown in Fig. 2(e–h), demonstrating that (i) upon the adsorption of the Mg atom(s), LUMO of the GYCTF slightly moves to- ward lower energies, leading to a negligible impact in $E_{g}$ of the sheet, (ii) HOMO of the sheet dramatically shifts to higher energies, leading to a significant reduction in $E_{g}$ of the sheet, and (iii) adsorption of multiple Mg atoms slightly reduce the $E_{g}$ of Mg/GYCTF from 1.51 to 1.27, 1.25 and 1.20 eV for the second, third and fourth Mg adsorption, respectively.

### 3.2. Adsorption of Mg atoms on functionalized GYCTF

Although the $E_{ad}$ of Mg in GYCTF is sufficient for applying as anode material of MIB, to overcome the low maximum coverage of the Mg on studied CTF, the $H$ atoms of GYCTF (which were connected to $C_{6}$) were replaced by three different functional groups (-CH₃, -F, and -SH). As shown in Fig. 4(a–c), the geometric structure of the GYCTF sheet re- mains unchanged by the replacement of $H$ atoms by the functional groups. The calculated bond lengths of C-C (1.78 Å) for the neighboring C-X bond in the functionalized CTF are slightly longer than the same C-C bonds in the pure sheet. Nonetheless, the functionalization of GYCTF does not affect the 2-D structure of the surface. Calculated DOS of GYCTF-CH₃, GYCTF-F, and GYCTF-SH are shown in Fig. 4(d–f). As shown in frontier molecular orbital (FMO) analysis in Fig. 5(a–d), except for the GYCTF-SH structure, HOMO mainly focused on aromatic $C_{6}$ ring and acetylene connection. Instead of bare and methyl functionalized sheets, HOMO of GYCTF-F is slightly located in fluoride groups. The largest change of HOMO and LUMO corresponds to GYCTF-SH where the $E_{g}$ decreases from 3.63 to 2.45 eV. Interestingly the HOMO of GYCTF-SH mainly located on $C_{6}$ and LUMO move to acetylene groups, so that the conduction and valence bands move to a positive and negative value, respectively. Also, the semiconductor behavior of GYCTF still remains in all sheets. In perspective, the structural and dynamic stability of the 2-D planar structure of GYCTF-X should be investigated. The structural and thermodynamic stability of the surface per unit cell is determined by:

$$E_{\mathrm{f}}=\left[\mathrm{E}\left(\mathrm{C}_{\mathrm{p}} \mathrm{H}_{\mathrm{q}} \mathrm{N}_{\mathrm{r}} \mathrm{F}_{\mathrm{t}} \mathrm{S}_{\mathrm{u}}\right)-\mathrm{pE}_{\mathrm{C}}-\mathrm{qE}_{\mathrm{H}}-\mathrm{rE}_{\mathrm{N}}-\mathrm{tE}_{\mathrm{F}}-\mathrm{uE}_{\mathrm{S}}\right]/\mathrm{n} \tag{2}$$

where $n$ is the number of atoms in a single cell, and $p, q, r, t$ and $i$ indicate the number of $C, H, N, F,$ and $S$ atoms in the GYCTF-X. The energy of the isolated subscripted atoms is $E_{\mathrm{C}}, E_{\mathrm{H}}, E_{\mathrm{N}}, E_{\mathrm{F}},$ or $E_{\mathrm{S}}$. The expected values are sorted to GYCTF-F (-5.24 eV per unit cell) > GYCTF (-5.10 eV per unit cell) > GYCTF-CH₃ (-4.55 eV per unit cell) > GYCTF-SH (-4.13 eV per unit cell). Compared to the electron donor functional groups, this suggests that electron acceptor fluoride functionalization is energeti- cally more desirable since the N atoms appear to gain $\pi$-electrons of aromatic $C_{6}$ rings.

Effective adsorption of Mg atom with the host substrate is necessary for CTF to be a very appropriate anode material for the Mg-ion battery. Firstly, the length between Mg and surface was adjusted several times from 1.0 to 3.0 Å to confirm the most robust adsorption configuration. With each original length, full structure full-relaxed was performed. Our calculations show that when an Mg atom is positioned above various position, for each surface a unique configuration obtained so that unlike

![](./images/812079174322749440_3.jpg)

Fig. 3. Variation of the adsorption energy with increasing the number of nMg on the surface of GYCTF-X (For interpretation of the references to color in this figure, the reader is referred to the web version of this article).

![](./images/812079174322749440_4.jpg)

Fig. 4. (a-c) A slice of unit cell of GYCTF-X and (d-f) related TDOS.

to bare sheet in GYCTF-CH₃, the Mg atom located atop of one of the single C-C bond connected to acetylenic carbon with $E_{ad}$ of 75.1 kcal
mol⁻¹ which is slightly lower than bare CTF with a bond length of 2.56
Å. In the case of GYCTF-F, the Mg atom tends to bond to two F atoms
simultaneously with $E_{ad}$ of 45.7 kcal mol⁻¹ with a bond length of 2.01 Å
to each Fluorine atom. Interestingly in GYCTF-SH, the first Mg atom
connected to one of the $T_{6}$ nitrogen with $E_{ad}$ of 62.3 kcal mol⁻¹ and bond
length of 2.02 Å. Optimization of multiple Mg atoms insertion in GYCTF-
X is further investigated so that Mg atoms are initially set at different
sites. From the standpoint of comparison, after functionalization of
GYCTF with -CH3, -F, and -SH, the maximum inserted Mg are 4, 6, and 9
atoms, respectively. As shown in Fig. 3, the functionalization process
cannot improve the $E_{ad}$ of first Mg, but functionalization of fluoride and
thiol dramatically improved the possible coverage of GYCTF toward Mg
atoms. The $E_{ad}$of nMg ($n = 2$, ..., 9) adsorption on GYCTF-SH with the
highest possible coverage are in the range of 52.4 to 14.0 kcal mol⁻¹. In
Table 1, the $E_{ad}$, $E_{g}$, and average charge transfer between Mg atoms and
GYCTF-X are reported. The maximum charge transfer in the first Mg
insertion is related to GYCTF-SH, and the maximum average charge
transfer for full coverage Mg is related to GYCTF-H about 0.076 e. Unlike
the bare, methyl-, and fluoride-functionalized sheets, NBO population
analysis shows that Mg atoms acquire positive charge after thiol func-
tionalization so that when the number of adsorbed Mg increased, the
average of charge transfer decreased from 0.134 e to 0.068 e per Mg
atom.

In practical application, the two-dimensional nanostructures may
restack due to their higher surface energy. Thus, we also investigated the
Mg adsorption in different configurations of bilayer GYCTF-SH as the
most favorable system such as between two benzene rings (B₂), between
two triazine nitrogen atoms (N₂), between two -C≡C- links (A₂), and
between two triazine rings (T₂). After optimization, just two stable
configurations were obtained and the adsorption energies values are
sorted to T₂ ($E_{ad} = 76.9$ kcal mol⁻¹) > B₂ ($E_{ad} = 41.2$ kcal mol⁻¹) which
is shown in Fig. S2. The $E_{ad}$ of single Mg on bilayers is larger than those
on a single layer surface. These results are in agreement with previous
findings [44,45].

### 3.3. Diffusion of Mg atom on GYCTF-X

The charge and discharge process essentially depends on the
mobility of Mg is another primary factor for determining the potential
usage of GYCTF-X monolayer as anode materials in Mg ion battery.
Therefore, we employed the NEB method, the nudged elastic band, to
specify diffusion paths and measure the corresponding diffusion barriers
for understanding the migration characteristics of the Mg atom on the
surface of the sheet in the GYCTF-X monolayer. In this context, the
diffusion pathways of single Mg on the surface of GYCTF-X are studied
and demonstrated in Fig. 6. Except for GYCTF-CH3, the pathway mainly
including the migration of Mg between $C_{6}$ and $T_{6}$ for all optimized sheets
(labeled as $C_{6}$-$T_{6}$). For GYCTF-F the stable configuration was assumed as
a start point in which Mg diffused from one side to another side labeled
as $F$-$C_{6}$-$F$. In the case of GYCTF-SH, stable configuration is also the start
point, and after migration between the $T_{6}$-$C_{6}$ line, the Mg atom is finally
positioned at the middle of two -SH groups. Thus, two pathways of $N$-$T_{6}$-
$N$ and $S$-$C_{6}$-$S$ were investigated. As shown in Fig. 6, four barrier energies
were obtained for bare and GYCTF-CH3 surfaces with $E_{br}$ ranges of
0.802-0.821 eV and 0.789-0.943 eV, respectively. As mentioned above,
two different pathways for migration of Mg are possible in GYCTF-SH so
that $E_{br}$ of N-$T_{6}$-N pathway is 0.354 eV smaller than S-$C_{6}$-S pathway with
$E_{br}$ of 0.439 eV. From the standpoint of comparison, the order of $E_{br}$ for
Mg diffusion in the studied anode is GYCTF-CH3 > GYCTF > GYCTF-F >
GYCTF-SH. According to our results, the rapid charge-discharge rate
capability for Mg-ion could be available for the thiol functionalized CTF.
Also, the diffusion of Mg atoms through the bilayer of GYCTF-SH from
B2 to T2 was investigated. As shown in Fig. S3, two barrier energies were
obtained for two stacked GYCTF-SH with $E_{br}$ ranges of 0.53-0.61 eV.

### 3.4. Application of GYCTF-X in MIB

Assessing the potential possibility of the GYCTF-X as the anode
material for MIBs is the main target of the current study. The efficiency
of batteries depends strongly on the Mg storage capacity of the anode
and also on its open-circuit voltage. Theoretically, the average OCV as
one of the key parameters in battery performance is measured through
the following equation (Nernst equation):

![](./images/812079174322749440_5.jpg)

Fig. 5. FMO analysis of the optimized structures of GYCTF, GYCTF-CH₃, GYCTF-F and GYCTF-SH.

$$\text{OCV} = -\Delta\text{G/qF} \tag{3}$$

where $F$ is the Faraday constant with the value of 96,500 C mol⁻¹ and $q$ is the charge of the working ion in the electrolyte. $\Delta\text{G}$ term is the difference of the Gibbs free energy for overall reaction, which can be obtained from the internal energy $(E)$ by ignoring the changes in volume and entropy:

$$\Delta\text{G} = \Delta\text{E} + \text{P}\Delta\text{V} - \text{T}\Delta\text{S} \sim \Delta\text{E}_\text{ad} \tag{4}$$

Therefore, $V_{\text{OC}}$ is written as follows

$$\text{OCV} = \left[ - \text{E}_{(\text{Mg}2@\text{GYCTF-X})}+ E_{(\text{Mg}1@\text{GYCTF-X})} + (\text{n}_2\text{-n}_1)\text{E}_{(\text{Mg})} \right] / 2(\text{n}_2\text{-n}_1) \tag{5}$$

![](./images/812079174322749440_6.jpg)

Fig. 6. Corresponding energy barriers for different pathways of Mg on GYCTF-X surfaces.

![](./images/812079174322749440_7.jpg)

Fig. 7. Predicted OCV (V) as a function of capacity for nMg/GYCTF-X.

In theory, the metal atom's OCV covers between $\mathrm{n}_1 \leq n \leq \mathrm{n}_2$. Where $\mathrm{n}_1$ and $\mathrm{n}_2$ are the numbers of Mg adsorbed on the surface of the GYCTF-X unit cell. E(Mg1@GYCTF-X) and E(Mg2@GYCTF-X) are the total energy of Mg1@GYCTF-X and Mg2@GYCTF-X, respectively. Before calculating the OCV, the maximum adsorption quantity of the Mg atom on the studied sheets was investigated. Our calculation indicates that after Mg adsorption, the unit cell of GYCTF, GYCTF-CH₃, GYCTF-F, and GYCTF-SH are $\mathrm{Mg}_4\mathrm{C}_{13}\mathrm{N}_3\mathrm{H}_4$, $\mathrm{Mg}_4\mathrm{C}_{17}\mathrm{N}_3\mathrm{H}_{12}$, $\mathrm{Mg}_6\mathrm{C}_{13}\mathrm{N}_3\mathrm{F}_4$, and $\mathrm{Mg}_9\mathrm{C}_{13}\mathrm{N}_3\mathrm{S}_4\mathrm{H}_4$, respectively. The following formula is considered to calculate the corresponding adsorption capacities:

$$
C=2x\mathrm{F}/\mathrm{MW}_{(\text{GYCTF-X})} \tag{6}
$$

here, $x$ indicates the number of adsorbed Mg, and $\mathrm{MW}_{(\text{GYCTF-X})}$ is the molecular weight of GYCTF-X. From Eq. (5), the OCV is related to the $E_{\text{ad}}$ and required to be a positive result. A low OCV of the anode materials means a high energy density, whereas an ultralow OCV for the anode materials causes the metal plating and the dendrite formation of the adsorbed metal [46]. Fig. 7 shows the OCVs for the studied CTFs as functions of the specific capacities. For the bare GYCTF, the OCVs are 1.81, 1.65, 1.58, and 1.50 V with the theoretical capacity of 1061 mAh $\mathrm{g}^{-1}$. Theoretical capacity of functionalized sheets are GYCTF-SH (1462.4 mAh $\mathrm{g}^{-1}$) $>$ GYCTF-F (1174.2 mAh $\mathrm{g}^{-1}$) $>$ GYCTF-CH₃ (831.3 mAh $\mathrm{g}^{-1}$). Obviously, the high storage capacity of GYCTF-SH is making it a remarkable anodic candidate for use in MIBs. This value is much larger than the reported values of 319.2 mAh $\mathrm{g}^{-1}$ for $\mathrm{g}$-$\mathrm{C}_3\mathrm{N}_4$ [47], 516 mAh $\mathrm{g}^{-1}$ for $\mathrm{C}_{24}\mathrm{N}_{24}$ [48], and 1002 mAh $\mathrm{g}^{-1}$ for the SiC nanosheet [49] in former research in the field of MgIBs. On the other hand, after the final concentration, the amount of the OCV becomes negative, indicating Mg adsorption on the sheets has become thermodynamically unfavorable. These results can be explained by the formation of the clusters in concentrations higher than the final concentration, which is not pleasing for batteries. The average voltage for -CH₃ (1.34 V), -F (0.64 V), and -SH (0.68 V) were obtained by averaging the whole voltage profiles.

### 3.5. Volume change of anode

Electrode materials in conventional batteries react with $\mathrm{Mg}^{2+}$ ions within intercalation reactions. This reaction mechanism can be explained by the insertion and extraction of guest $\mathrm{Mg}^{2+}$ions within the relatively stable crystal structure of a host material with only negligible volumetric changes [50]. These small volume changes trigger hundreds of reversible cycles and thus long cyclic life. The volume change can give rise to the formation of unstable Solid Electrolyte Interphase (SEI), which will cause continuous Mg and electrolyte consumption, lower Coulombic efficiency, acceleration of degradation reactions, and finally, shorter cycle life. Here, we analyzed the in-plane expansion of the GYCTF-SH (Fig. 8) to determine the Mg intercalation effects on the volumetric change in the GYCTF-SH monolayer. Usually, by increasing the Mg adsorption, the lattice parameter is increasing. The in-plane lattice enlargements for the maximum Mg adsorption are about 0.70%, which is more favorable for Mg adsorption on FeSe monolayer with a volume change of 4.25% [51]. Top and side views of GYCTF-SH before and after maximum Mg insertion clearly show that the selected sheet slightly increased from 45.77 to 46.09 Å. Note that not only the significant deformation but also the bond breakage doesn't occur in the GYCTF-SH monolayer during Mg intercalation, and the adsorbed sites only slightly diverge from their original positions. These results make GYCTF-SH a high capacity and safe anode material for MIB applications.

### 4. Conclusion

Two-dimensional (2-D) materials have been considered promising anode materials for metal-ion batteries due to their unique physicochemical properties. Through First-principles DFT calculations, we have investigated the MIB performance of pure and three different functionalized graphyne-like CTFs as the anode active materials by studying their transition states, the adsorption ability, geometry, storage capacity, OCV, and electronic structures. As the anode materials of the MIB, Thiol-functionalized GYCTF benefits from high electrical conductivity

![](./images/812079174322749440_8.jpg)

Fig. 8. Volume change of GYCTF-SH after full coverage of Mg.

(before and after the adsorption process), appropriate average OCVs of
0.68 V, a specific capacity of 1462.4 mAh $g^{-1}$, and small structural
changes. Besides, the Mg atom owns a low diffusion barrier with a height
of 0.354 eV on the GYCTF-SH surface and the maximum intensity of
$Mg_9C_{13}N_3S_4H_4$. The obtained results in this work might open the door to
the design of promising CTF-based anode materials for MIBs.

## Author statement

We explored the potential application of pure and functionalized 2-D
graphyne-like covalent triazine framework (GYCTF) as anode materials
for Mg-ion batteries (MIBs) using dispersion-corrected DFT. We found
that Mg preferably adsorbs above the center of all carbon six-membered
rings of GYCTF with adsorption energy about 83.4 kcal/mol. After
functionalization, -SH increases the maximum coverage of Mg on sur-
face from 4 to 9 Mg. Also, $-CH_3$ strongly reduces the specific capacity of
GYCTF in MIB application. The single-layer GYCTF-SH, can be magne-
siated on both sides yielding $Mg_9C_{13}N_3S_4H_4$ with a storage capacity as
high as 1462.4 mAh $g^{-1}$ with average OCV of 0.68 V.

## Declaration of Competing Interest

The authors declare that there is no conflict of interest regarding the
publication of this article.

## References

[1] R. Kumar, M. Singh, A. Soam, Study on electrochemical properties of silicon micro
particles as electrode for supercapacitor application, Surf. Interfaces 19 (2020),
100524.

[2] N. Feizi, Y. Yamini, M. Moradi, M. Karimi, Q. Salamat, H. Amanzadeh, A new
generation of nano-structured supramolecular solvents based on propanol/gemini
surfactant for liquid phase microextraction, Anal. Chim. Acta 953 (2017) 1–9.

[3] M. Moradi, Y. Yamini, A. Vatanara, A. Saleh, M. Hojati, S. Seidi, Monitoring of
trace amounts of some anti-fungal drugs in biological fluids by hollow fiber based
liquid phase microextraction followed by high performance liquid
chromatography, Anal. Methods 2 (2010) 387–392.

[4] R. Yang, F. Zhang, X. Lei, Y. Zheng, G. Zhao, Y. Tang, C.S. Lee, Pseudocapacitive Ti-
Doped Niobium Pentoxide Nanoflake Structure Design for a Fast Kinetics Anode
toward a High-Performance Mg-Ion-Based Dual-Ion Battery, ACS Appl. Mater.
Interfaces 12 (2020) 47539–47547.

[5] D. Prakash, S. Manivannan, N, B co-doped and Crumpled Graphene Oxide
Pseudocapacitive Electrode for High Energy Supercapacitor, Surf. Interfaces 23
(2021), 101025.

[6] H. Bigdeli, M. Moradi, S. Hajati, M.A. Kiani, J. Toth, Cobalt terephthalate MOF-
templated synthesis of porous nano-crystalline $Co_3O_4$ by the new indirect solid
state thermolysis as cathode material of asymmetric supercapacitor, Phys. E 94
(2017) 158–166.

[7] D. Wu, B. Yang, H. Chen, E. Ruckenstein, Mechanical deformation induced charge
redistribution to promote the high performance of stretchable magnesium-ion
batteries based on two-dimensional C2N anodes, Nanoscale 11 (2019)
15472–15478.

[8] L. Ma, X. Li, G. Zhang, Z. Huang, C. Han, H. Li, Z. Tang, C. Zhi, Initiating a wearable
solid-state Mg hybrid ion full battery with high voltage, high capacity and ultra-
long lifespan in air, Energy Storage Mater. 31 (2020) 451–458.

[9] L. Chen, J.L. Bao, X. Dong, D.G. Truhlar, Y. Wang, C. Wang, Y. Xia, Aqueous Mg-ion
battery based on polyimide anode and prussian blue cathode, ACS Energy Lett. 2
(2017) 1115–1121.

[10] Q.D. Truong, M.K. Devaraju, I. Honma, Nanocrystalline MgMnSiO4 and MgCoSiO4
particles for rechargeable Mg-ion batteries, J. Power Sources 361 (2017) 195–202.

[11] X. Zhao, L. Mao, Q. Cheng, F. Liao, G. Yang, X. Lu, L. Chen, Interlayer Engineering
of Preintercalated Layered Oxides as Cathode for Emerging Multivalent Metal-ion
Batteries: Zinc and Beyond, Energy Storage Mater. (2021).

[12] Z. Wang, Y. Zhu, H. Peng, C. Du, X. Ma, C. Cao, Microwave-induced phase
engineering of copper sulfide nanosheets for rechargeable magnesium batteries,
Electrochim. Acta 374 (2021), 137965.

[13] D. Er, E. Detsi, H. Kumar, V.B. Shenoy, Defective graphene and graphene allotropes
as high-capacity anode materials for Mg ion batteries, ACS Energy Lett. 1 (2016)
638–645.

[14] A. Djire, A. Bos, J. Liu, H. Zhang, E.M. Miller, N.R. Neale, Pseudocapacitive Storage
in Nanolayered Ti2NTx MXene Using Mg-Ion Electrolyte, ACS Appl. Nano Mater. 2
(2019) 2785–2795.

[15] S. Mukherjee, G. Singh, Two-Dimensional Anode Materials for Non-lithium Metal-
Ion Batteries, ACS Appl. Energy Mater. 2 (2019) 932–955.

[16] Y. Yang, Q. Cao, Y. Gao, S. Lei, S. Liu, Q. Peng, High impact resistance in graphyne,
RSC Adv., 10 (2020) 1697–1703.

[17] Y. An, Y. Tian, C. Wei, Y. Tao, B. Xi, S. Xiong, J. Feng, Y. Qian, Dealloying: An
effective method for scalable fabrication of 0D, 1D, 2D, 3D materials and its
application in energy storage, Nano Today 37 (2021), 101094.

[18] F. Liu, Y. Liu, X. Zhao, X. Liu, L.Z. Fan, Pursuit of a high-capacity and long-life Mg-
storage cathode by tailoring sandwich-structured MXene@carbonnanosphere
composites, J. Mater. Chem. A 7 (2019) 16712–16719.

[19] X. Li, Q. Gao, J. Wang, Y. Chen, Z.H. Chen, H.S. Xu, W. Tang, K. Leng, G.H. Ning,
J. Wu, Q.H. Xu, S.Y. Quek, Y. Lu, K.P. Loh, Tuneable near white-emissive two-
dimensional covalent organic frameworks, Nat. Commun. 9 (2018) 2335.

[20] A.R. Bagheri, N. Aramesh, Towards the room-temperature synthesis of covalent
organic frameworks: a mini-review, J. Mater. Sci. 56 (2021) 1116–1132.

[21] J. Li, X. Zhou, J. Wang, X. Li, Two-Dimensional Covalent Organic Frameworks
(COFs) for Membrane Separation: a Mini Review, Ind. Eng. Chem. Res. 58 (2019)
15394–15406.

[22] S. Dalapati, M. Addicoat, S. Jin, T. Sakurai, J. Gao, H. Xu, S. Irle, S. Seki, D. Jiang,
Rational design of crystalline supermicroporous covalent organic frameworks with
triangular topologies, Nat. Commun. 6 (2015) 7786.

[23] M.X. Wu, Y.W. Yang, Applications of covalent organic frameworks (COFs): From
gas storage and separation to drug delivery, Chin. Chem. Lett. 28 (2017)
1135–1143.

[24] A. Sharma, R. Babarao, N.V. Medhekar, A. Malani, Methane Adsorption and
Separation in Slipped and Functionalized Covalent Organic Frameworks, Ind. Eng.
Chem. Res. 57 (2018) 4767–4778.

[25] W. Zheng, C.S. Tsang, L.Y.S. Lee, K.Y. Wong, Two-dimensional metal-organic
framework and covalent-organic framework: synthesis and their energy-related
applications, Mater. Today Chem. 12 (2019) 34–60.

[26] B. Wang, L.S. Lee, C. Wei, H. Fu, S. Zheng, Z. Xu, D. Zhu, Covalent triazine-based
framework: A promising adsorbent for removal of perfluoroalkyl acids from
aqueous solution, Environ. Pollut. 216 (2016) 884–892.

[27] S. Dey, A. Bhunia, D. Esquivel, C. Janiak, Covalent triazine-based frameworks
(CTFs) from triptycene and fluorene motifs for CO 2 adsorption, J. Mater. Chem. A
4 (2016) 6259–6263.

[28] R. Guan, L. Zhong, S. Wang, D. Han, M. Xiao, L. Sun, Y. Meng, Synergetic Covalent
and Spatial Confinement of Sulfur Species by Phthalazinone-Containing Covalent
Triazine Frameworks for Ultrahigh Performance of Li-S Batteries, ACS Appl. Mater.
Interfaces 12 (2020) 8296–8305.

[29] R. Shi, L. Liu, Y. Lu, C. Wang, Y. Li, L. Li, Z. Yan, J. Chen, Nitrogen-rich covalent
organic frameworks with multiple carbonyls for high-performance sodium
batteries, Nat. Commun. 11 (2020) 178.

[30] Y. Hu, L.J. Wayment, C. Haslam, X. Yang, S.H. Lee, Y. Jin, W. Zhang, Covalent
organic framework based lithium-ion battery: Fundamental, design and
characterization, Energy Chem. 3 (2021), 100048.

[31] O. Buyukcakir, J. Ryu, S.H. Joo, J. Kang, R. Yuksel, J. Lee, Y. Jiang, S. Choi, S.
H. Lee, S.K. Kwak, S. Park, R.S. Ruoff, Lithium Accommodation in a Redox-Active
Covalent Triazine Framework for High Areal Capacity and Fast-Charging Lithium-
Ion Batteries, Adv. Funct. Mater. 30 (2020), 2003761.

[32] B. Ball, C. Chakravarty, P. Sarkar, Two-dimensional covalent triazine framework as
a promising anode material for Li-ion batteries, J. Phys. Chem. C 123 (2019)
30155–30164.

[33] C. Wu, M. Hu, X. Yan, G. Shan, J. Liu, J. Yang, Azo-linked covalent triazine-based
framework as organic cathodes for ultrafast capacitor-type lithium-ion batteries,
Energy Storage Mater. 36 (2021) 347–354.

[34] T. Chen, W.Q. Li, X.J. Chen, Y.Z. Guo, W.B. Hu, W.J. Hu, Y.A. Liu, H. Yang, K. Wen,
A Triazine-Based Analogue of Graphyne: Scalable Synthesis and Applications in
Photocatalytic Dye Degradation and Bacterial Inactivation, Chem.– Eur. J., 26
(2020) 2269–2275.

[35] J. Tirado-Rives, W.L. Jorgensen, Performance of B3LYP density functional methods
for a large set of organic molecules, J. Chem. Theory Comput. 4 (2008) 297–306.

[36] N.N. Andrichenko, A.Y. Ermilov, Using the DFT-D method to describe dispersion
interactions in systems of weakly-bonded Xe-aromatic molecules, Russ. J.Phys.
Chem. A 87 (2013) 1342–1348.

[37] N.M. O'Boyle, A.L. Tenderholt, K.M. Langner, ccib: A library for package-
independent computational chemistry algorithms, J. Comput. Chem. 29 (2008)
839–845.

[38] M.T. Baei, A.S. Ghasemi, E. Tazikeh-Lemeski, A. Soltani, F. Ashrafi, S. Sedighi,
Effect of adsorption sensitivity of armchair single-walled BN nanotube toward
thiocyanate anion: A systematic evaluation of length and diameter effects, Surf.
Interfaces 21 (2020), 100693.

[39] L.H.S. Lacerda, S. Ricardo de Lazaro, 1. Surface and morphology investigation of
FeCrO3 material in ilmenite-, corundum- and lithium niobate- polymorphs, Surf.
Interfaces 22 (2021), 100837.

[40] B. Chettri, P.K. Patra, N.H. Hieu, D.P. Rai, Hexagonal boron nitride (h-BN)
nanosheet as a potential hydrogen adsorption material: A density functional theory
(DFT) study, Surf. Interfaces 24 (2021), 102043.

[41] M. Eslami, M. Moradi, R. Moradi, DFT investigation of hydrogen adsorption on the
C3N nanotube, Vacuum 133 (2016) 7–12.

[42] A.A. Peyghan, M. Moradi, J. Iran, First-principle study of methanol adsorption on
Ni (Pd)-decorated graphene, Chem. Soc. 12 (2015) 751–756.

[43] X. Li, B.H. Li, Y.B. He, F.Y. Kang, A review of graphynes: Properties, applications
and synthesis, New Carbon Mater. 35 (2020) 619–629.

[44] I. Muhammad, S. Wang, J. Liu, H. Xie, Q. Sun, Boron-graphdiyne as an anode
material for Li, Na, and K ion batteries with high capacities and low diffusion
barriers, J. Renew. Sustain. Energy 11 (2019), 014106.

[45] H.J. Hwang, J. Koo, M. Park, N. Park, Y. Kwon, H. Lee, Multilayer graphynes for
lithium ion battery anode, J. Phys. Chem. C 117 (14) (2013) 6919–6923.

[46] M. Boroun, S. Abdolhosseini, M. Pourfath, Separated and intermixed phases of borophene as anode material for lithium-Ion batteries, J. Phys. D Appl. Phys. 52 (2019), 245501.

[47] J. Zhang, G. Liu, H. Hu, L. Wu, Q. Wang, X. Xin, S. Li, P. Lu, Graphene-like carbon- nitrogen materials as anode materials for Li-ion and mg-ion batteries, Appl. Surf. Sci. 487 (2019) 1026–1032.

[48] E. Shakerzadeh, L. Azizinia, Can C24N24 cavernous nitride fullerene be a potential anode material for Li-, Na-, K-, Mg-, Ca-ion batteries? Chem. Phys. Lett. 764 (2021), 138241.

[49] A. Ali Khan, R. Ahmad, I. Ahmad, Silicon carbide and III-Nitrides nanosheets: Promising anodes for Mg-ion batteries, Mater. Chem. Phys. 257 (2021), 123785.

[50] D. Wu, J. Zeng, H. Hua, J. Wu, Y. Yang, J. Zhao, NaV6O15: a promising cathode material for insertion/extraction of Mg2+ with excellent cycling performance, Nano Res. 13 (2020) 335–343.

[51] X. Lv, F. Li, J. Gong, J. Gu, S. Lin, Z. Chen, Metallic FeSe monolayer as an anode material for Li and non-Li ion batteries: a DFT study, Phys. Chem. Chem. Phys. 22 (2020) 8902–8912.