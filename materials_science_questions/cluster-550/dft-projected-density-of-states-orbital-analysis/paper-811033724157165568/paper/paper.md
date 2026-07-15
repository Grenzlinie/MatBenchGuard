# Computational Modeling of Novel Bulk Materials for the Intermediate-Band Solar Cells

Murugesan Rasukkannu,*,† Dhayalan Velauthapillai,† and Ponniah Vajeeston‡

†Department of Computing, Mathematics and Physics, Western Norway University of Applied Sciences, Inndalsveien 28, 5063 Bergen, Norway
‡Department of Chemistry, Center for Materials Science and Nanotechnology, University of Oslo, P.O. Box 1033, Blindern, N-0315 Oslo, Norway

**Supporting Information**

### ABSTRACT:
Research communities have been studying materials with intermediate bands (IBs) in the middle of the band gap to produce efficient solar cells. Cells based on these materials could reach theoretical efficiencies up to 63.2%. In this comprehensive study, we investigate by means of accurate first-principle calculation the electronic band structure of 2100 novel compounds (bulk materials) to discover whether the IB is present in these materials. Our calculations are based on the density functional theory, using the generalized-gradient approximation for exchange and correlation terms and focusing on the band structure, the density of states, and the electron effective masses of the structures in the database. The IB structures are obtained by adding metallic or semimetallic atoms in the bulk material. By means of these calculations, we have clearly identified a number of compounds that may having high potential to be used as photovoltaic materials. We present here the numerical results for 17 novel IB materials, which could theoretically prove to be suitable for photovoltaic applications.

![](./images/811033724157165568_1.jpg)

Research communities have been studying materials with intermediate bands in the middle of the bandgap to achieve efficient solar cells. Cells based on these materials could reach theoretical efficiencies up to 63.2%.

## INTRODUCTION
Multi-band gap materials offer the possibility of increasing the efficiency of solar cells beyond the limit of traditional single-band gap solar-cell materials. Intermediate-band (IB) materials are characterized by the splitting of the main band gaps into two or more sub-band gaps by narrow IBs and have been the focus of recent studies.¹² In IB solar cells, an IB material is sandwiched between two ordinary p-type and n-type semiconductors and deed as discriminating contacts to the valence band (VB) and the conduction band (CB), respectively. In IB materials, an electron is promoted from the VB to the CB through the IB. Upon absorption of sub-band gap-energy photons, the electrons transit from VB to CB and later from IB to CB. It will add up to the transition of electrons from VB to CB through conventional VB-to-CB photon absorption.¹² By adopting a hypothesis similar to that of Shockley and Queisser,³ it was shown in 1997⁴ that balance-limiting efficiencies of 63.2% for IB solar cells and 41% for single-band gap solar cells can be achieved at a concentration of 46 050 suns at earth and sun temperatures of 300 and 6000 K, respectively.

The IB should be partially filled to permit the comparable rates for the low sub-band gap-energy photon absorption processes and should not overlap with either the VB or the CB to avoid fast transitions through thermalizations.⁵ We can consider the IB solar cells as a combination of three cells. Cells representing VB-to-IB and IB-to-CB transitions can be regarded as two cells in series, and the VB-to-CB transition can represent a parallel cell. The cell will have a high tolerance to changes in the solar spectrum.⁶

In the mid-20th century, researchers⁷⁻¹⁰ suggested the concept of creating intermediate levels in the middle of a forbidden band gap to increase the maximum photocurrent by doping the semiconductor with a large concentration of impurities. At an early stage, it was believed that these IBs would cause nonradiative recombination. It has been later shown that the nonradiative recombination can be suppressed by using a sufficiently high concentration of dopants.¹⁰⁻¹³

Two major approaches are considered in fabricating IB solar cells, namely, quantum-dot IBs (QDIBs) and bulk IB solar cells. By using quantum dots with different shapes and sizes, the IB levels can be tuned. The first QDIB was produced in 2004 on the basis of the InAs/GaAs QD material with an efficiency of 15.3%. Energy levels of the confined states in a quantum dot can be used as IB in QDIBs. However, there are many challenges with QDIBs as quantum dots are very small and do not absorb a significant amount of light. With an increasing number of QDs, the cell structure can be damaged, and strain will cause severe damages. At room temperature, the Shockley−Read−Hall recombination is a dominant mechanism that leads to low efficiency in QDIB solar cells due to deeper impurities.

Received: December 21, 2016
Accepted: March 31, 2017
Published: April 13, 2017

![](./images/811033724157165568_2.jpg)

Figure 1. Band diagram of bulk IB solar cell; $E_{vi}$—energy gap between the top of the VB and the bottom of an IB, $E_{ci}$—energy gap between the top of the IB and the bottom of the CB, $\Delta E_{i}$—width of the IB, $E_{g}$—total band gap between the top of the VB and the bottom of the CB. The electronic transitions (V, I), (I, I), (I, C), and (V, C) are also explained.

<table><thead><tr><th>serial no.</th><th>chemical formula</th><th>Pearson symbol</th><th>space group number</th><th>band gap ($E_{vi}$)</th><th>band gap ($E_{ci}$)</th><th>width of IB ($\Delta E_{i}$)</th><th>total band gap ($E_{g}$)</th><th>band gap type</th></tr></thead><tbody><tr><td>1.</td><td>$K_{6}C_{60}$</td><td>cI132</td><td>204</td><td>0.61</td><td>0.28</td><td>0.39</td><td>1.28</td><td>ID</td></tr><tr><td>2.</td><td>$Au_{2}Cs_{2}I_{6}$</td><td>tI20</td><td>139</td><td>0.64</td><td>1.01</td><td>0.7</td><td>2.35</td><td>ID</td></tr><tr><td>3.</td><td>$Ag_{2}GeBaS_{4}$</td><td>tI16</td><td>121</td><td>0.90</td><td>0.35</td><td>1.16</td><td>2.41</td><td>ID</td></tr></tbody></table>

<table><thead><tr><th>serial no.</th><th>chemical formula</th><th>Pearson symbol</th><th>space group number</th><th>band gap ($E_{vi}$)</th><th>band gap ($E_{ci}$)</th><th>width of IB ($\Delta E_{i}$)</th><th>total band gap ($E_{g}$)</th><th>band gap type</th></tr></thead><tbody><tr><td>1.</td><td>$CuAgPO_{4}$</td><td>oP56</td><td>61</td><td>1.27</td><td>0.61</td><td>0.74</td><td>2.62</td><td>DB</td></tr><tr><td>2.</td><td>$Ag_{2}ZnSnS_{4}$</td><td>tI16</td><td>121</td><td>0.47</td><td>0.57</td><td>1.66</td><td>2.70</td><td>DB</td></tr><tr><td>3.</td><td>$Au_{2}Cs_{2}Br_{6}$</td><td>tI20</td><td>139</td><td>0.67</td><td>1.23</td><td>0.81</td><td>2.71</td><td>DB</td></tr><tr><td>4.</td><td>$Ag_{3}AsS_{4}$</td><td>oP16</td><td>31</td><td>0.73</td><td>1.04</td><td>1.00</td><td>2.77</td><td>DB</td></tr><tr><td>5.</td><td>$Ag_{2}KSbS_{4}$</td><td>tI16</td><td>121</td><td>0.81</td><td>1.08</td><td>0.94</td><td>2.93</td><td>ID</td></tr><tr><td>6.</td><td>$Na_{3}Se_{4}Sb$</td><td>cI16</td><td>217</td><td>1.02</td><td>1.24</td><td>0.71</td><td>2.97</td><td>DB</td></tr><tr><td>7.</td><td>$AgK_{2}SbS_{4}$</td><td>oP32</td><td>118</td><td>1.52</td><td>1.03</td><td>0.47</td><td>2.97</td><td>DB</td></tr><tr><td>8.</td><td>$AsRb_{3}Se_{4}$</td><td>oP32</td><td>62</td><td>1.32</td><td>0.98</td><td>0.97</td><td>3.15</td><td>DB</td></tr></tbody></table>

Several research groups have produced QDIB solar cells, $^{14-22}$ and efficiencies over 18% have been reported by Blokhin et al. $^{20}$

The second type of IB solar cells is based on bulk materials. The IB was detected through photoreflectance measurements in some bulk materials, and this formation was attributed to band anticrossing and heavily mismatched alloys. $^{23}$ The first of these bulk materials, ZnMnTeO, was developed by Walukiewicz and co-workers. $^{23}$ Later, numerous quantum-accurate calculations have been performed on VInS bulk material, characterized by an IB containing Fermi levels. Phillips and co-workers developed bulk IB solar cells using ZnTe doped with an oxygen atom and obtained higher efficiencies and short-circuit current than QDIB solar cells. $^{24,25}$ The band gap properties of bulk materials are widely studied, and the technologies are well verified by researchers. $^{5,26-33}$ However, the search for intermediate-band gap materials continues, to model high-efficiency IB solar cells. Figure 1 shows the band diagram of an IB solar cell with $E_{g}$, the total band gap between the top of the VB and the bottom of the CB. In the figure, $E_{vi}$ is the energy gap between the top of the VB to the bottom of an IB, $E_{ci}$ is the energy gap between the top of the IB to the bottom of the CB, and $\Delta E_{i}$ is the width of the IB. Furthermore, the electronic transitions of (V, I), (I, I), (I, C), and (V, C) are schematically depicted in the figure.

In the present work, we study 2100 structures with the aim of identifying ideal candidates for solar-cell materials. We employ density functional theory (DFT) calculations to verify the presence of an IB, isolated in the band gap of the semiconductor compounds of bulk material compounds with different substitutional impurities forming ternary alloys. The calculated band gap values are used to identify the most suitable compounds for solar-cell applications. We also present density of states (DOS) and effective mass calculations for the selected IB materials.

## RESULTS AND DISCUSSION

The main focus of the present work is to find the potential IB materials from the selected 2100 compounds. Because of the very high computational cost, we mainly focused on the electronic structure, the DOS and effective mass calculations. The hybrid electronic structure and optical properties of the selected IB compounds are under investigation, and the results will be published in a forthcoming work. We employ the DFT method to elucidate the band structure arrangement of 2100

bulk materials, vital for the interaction of IB and could be potent solar cells with sufficient band gap. The DFT approaches to reveal the significant and computational features of the bulk materials and these features can be used as virtual screenings of band structures of the 2100 compounds to identify the novel IB compounds. From the first screening, we observed 312 compounds having an IB with the maximum of the VB at the Fermi level. Among these, 282 compounds were selected for further analysis and 30 compounds were found as heavy elements. After carrying out a detailed analysis, we found out that only 17 compounds among the starting 282 would be acceptable semiconductor materials for photovoltaic applications. The rest were found to be perfect insulators, with band gap values larger than $3.51\ \text{eV}.^{34}$ The electronic properties of these 17 compounds are presented in Tables 1−3. It is well

<table>
  <caption>Table 3. Calculated Effective Masses of Narrow-Band Gap Compounds; Light Holes ($m^*_{lh}$), Heavy Holes ($m^*_{hh}$), and Electrons ($m^*_e$)</caption>
  <thead>
    <tr>
      <th>serial no.</th>
      <th>plane directions</th>
      <th>compound</th>
      <th>$m^*_{lh}\cdot m_e$</th>
      <th>$m^*_{hh}\cdot m_e$</th>
      <th>$m^*_e\cdot m_e$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.</td>
      <td>110</td>
      <td>$K_6C_{60}$</td>
      <td>0.092</td>
      <td>0.164</td>
      <td>0.216</td>
    </tr>
    <tr>
      <td>2.</td>
      <td>110</td>
      <td>$Au_2Cs_2I_6$</td>
      <td>0.096</td>
      <td>0.265</td>
      <td>0.095</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>110</td>
      <td>$Ag_2GeBaS_4$</td>
      <td>0.059</td>
      <td>0.114</td>
      <td>0.021</td>
    </tr>
  </tbody>
</table>

known that the band gap ($E_g$) values of solids obtained from usual DFT calculations are systematically underestimated due to discontinuity in the exchange-correlation potential. Thus, the calculated $E_g$ values are typically 30−50% smaller than those measured experimentally. $^{35}$ It is recognized that the theoretically calculated $E_g$ for semiconductors and insulators are strongly dependent on the approximations used, particularly on the exchange and correlation terms of the potential. In the present work, because of the large number compounds involved in the screening process, we have used only generalized-gradient approximation. However, the overall structure is not going to change except the band gap value irrespective of the approximation.

We have chosen to divide the 17 compounds with IBs into three groups depending on the magnitude of their band gap values. The first group of three compounds is named as narrow-band gap semiconductors, which is characterized by band gaps varying from 1.2 to 2.5 eV. The second group of eight compounds is named wide-band gap 1 semiconductors, which includes materials with band gaps varying from 2.6 to 3.15 eV. Finally, the third group is named as wide-band gap 2 semiconductors. In this case, the band gap values vary from 3.15 to 3.5 eV. The band structures of these compounds are presented in Figures 2a−c, 3a−d, 4a−d, and 5a−f, and we calculate the total band gaps, band gaps $E_{vi}$, $E_{ci}$, and the widths of the IB ($\Delta E_i$) bands for all of the compounds. The electronic structure properties of these compounds are presented in Tables 1, 2, and S1.

As presented in Table 1, narrow-band gap semiconductors $K_6C_{60}$ (alkali fullerides), $Au_2Cs_2I_6$, and $Ag_2GeBaS_4$ had total indirect band gaps of 1.28, 2.35, and 2.41 eV, respectively.

From Figure 2a, the calculated values for $K_6C_{60}$ are: The total indirect band gap is 1.28 eV, band gaps $E_{vi}$ and $E_{ci}$ are 0.61 and 0.28 eV, respectively, and the width of the IB is 0.39 eV. The band gap of 1.28 eV makes an optimal compound for the PV applications as their light responses are in the infrared region. Also, the IB will help the material to absorb additional photons with lower energy. It should be noted that $K_6C_{60}$ is already known as a semiconductor and the nature of the band structure is not well explained about the IB. However, they explained that the electronic structure of crystalline $K_6C_{60}$ is indirect band gap of $0.48\ \text{eV}.^{36}$ The DOS around the VB maximum is very similar to that of the isolated $C_{60}$ molecule, and the K atoms are almost completely ionized. $^{36}$

![](./images/811033724157165568_3.jpg)

Figure 2. Calculated electronic band structures of (a) $K_6C_{60}$, (b) $Au_2Cs_2I_6$, (c) and $Ag_2GeBaS_4$. The Fermi level is set to zero.

Similarly, from Figure 2b, the calculated values for $Au_2Cs_2I_6$ are as follows: The total indirect band gap is 2.35 eV, band gaps $E_{vi}$ and $E_{ci}$ are 0.64 and 1.01 eV, respectively, and the width of the IB, $\Delta E_i$ is 0.70 eV. The band gap of 2.35 eV for $Au_2Cs_2I_6$ shows that the material has its response to light in the visible

![](./images/811033724157165568_4.jpg)

Figure 3. Calculated electronic band structures of (a) $CuAgPO_4$ (up and down spin bands; up-black, down-red), (b) $Ag_2ZnSnS_4$, (c) $Au_2Cs_2Br_6$, and (d) $Ag_3AsS_4$. The Fermi level is set to zero.

region. For $Au_2Cs_2I_6$, the IB region has the optimal thickness to balance the absorption rate and recombination rate. $^{37}$ In Figure 2b, $Au_2Cs_2I_6$ has a broad band dispersion of IB, enough to produce an optical depth for subgap light, ensuring the compound to absorb subgap light so that it can be considered as a potential PV material. $^{37}$

From Figure 2c, the calculated values for $Ag_2GeBaS_4$ are: The total indirect band gap is 2.41 eV, band gaps $E_{vi}$ and $E_{ci}$ are 0.90 and 0.35 eV, respectively, and the width of the IB is 1.16 eV. The band gap of 2.35 eV for $Ag_2GeBaS_4$ shows that the material has its response to light in the visible region. Here, we observe that the width of the IB, $\Delta E_{i}$, in $Ag_2GeBaS_4$ is much higher than $E_{ci}$ and $E_{vi}$. Because of the broadness of the IB, photons can also be absorbed by the electrons from lower- energy states of the IB to excite to higher-energy states of IB. When the IB broadens, the absorption of photons for the transition of electrons from the VB to lower-energy states of IB as well as from the higher-energy states of IB to CB will be reduced. These effects will lead to lower efficiencies of the solar cell based on $Ag_2GeBaS_4$. It has been shown that the efficiency limit for an IB solar cell is reduced from higher to lower efficiencies if the width is infinitesimally significant. $^{38}$ It is important to note that all of these three materials, $K_6C_{60}$, $Au_2Cs_2I_6$, and $Ag_2GeBaS_4$, present indirect band gaps.

As presented in Table 2, the wide-band gap semiconductors $CuAgPO_4$, $Ag_2ZnSnS_4$, $Au_2Cs_2Br_6$, $Ag_3AsS_4$, $Ag_2KSbS_4$, $Na_3Se_4Sb$, $AgK_2SbS_4$, and $AsRb_3Se_4$ had the total band gaps of 2.62, 2.70, 2.71, 2.77, 2.93, 2.97, 2.97, and 3.15 eV, respectively. Figures 3a-d and 4a-d show the calculated band structures of $CuAgPO_4$, $Ag_2ZnSnS_4$, $Au_2Cs_2Br_6$, $Ag_3AsS_4$, $Ag_2KSbS_4$, $Na_3Se_4Sb$, $AgK_2SbS_4$, and $AsRb_3Se_4$ with IB, respectively. The calculated values of $E_{vi}$, $E_{ci}$, and $\Delta E_{i}$, and the total band gaps are presented in Table 2. The band gap type of the above eight compounds is direct band gap except for $Ag_2KSbS_4$ (indirect band gap). From Figure 2c, the calculated values for $Ag_2ZnSnS_4$ are: The total direct band gap is 2.70 eV, band gaps $E_{vi}$ and $E_{ci}$ are 0.47 and 0.57 eV, respectively, and the width of the IB is 1.66 eV. The band gap of 2.70 eV for $Ag_2ZnSnS_4$ shows that the material has its response to light in the visible region. Here, we observe that the width of the IB, $\Delta E_{i}$, in $Ag_2ZnSnS_4$ is much higher than $E_{ci}$ and $E_{vi}$. The increase in the IB width leads to a decrease in efficiency; however, it is still significantly higher than that of a single-band gap solar cell. $^{39}$ The band gaps associated with optimum efficiencies are constant for all IB solar cells when the IB width exceeds 2 eV. $^{39}$ Because of the display of the small amount of data, we added the remaining six compounds in the Supporting Information.

In general, the electrochemical potentials of the electrons in the different bands are close to the edges of the bands. The

![](./images/811033724157165568_5.jpg)

Figure 4. Calculated electronic band structures of (a) $Ag_2KSbS_4$, (b) $Na_3Se_4Sb$, (c) $AgK_2SbS_4$, and (d) $AsRb_3Se_4$. The Fermi level is set to zero.

![](./images/811033724157165568_6.jpg)

Figure 5. Total and site-projected DOS of $Au_2Cs_2I_6$. The Fermi level is set to zero and marked by a vertical dotted line.

open-circuit voltage of any solar cell is the difference between the CB minimum at the electrode in contact with the n-type side and the VB maximum at the electrode in contact with the p-type side. Thus, the maximum photovoltage of IB solar cells on the materials presented in Tables 1 and S1 is limited to 2.41 and 3.51 eV, respectively. $Ag_2GeBaS_4$ is still capable of absorbing energy photons above 0.28 eV in Table 1 and $Ag_6SiSO_8$ of 0.47 eV in Table 2. IB solar cells can deliver a maximum photovoltage by absorbing two sub-band gap

photons to produce one high-energy electron; the laws of thermodynamics would be violated if this were not the case. $^{1}$

All of the 17 semiconductor compounds presented in this work have properties that make them suitable for PV applications; we show here the DOS analysis for three compounds, namely, $Au_{2}Cs_{2}I_{6}$, $Ag_{2}GeBaS_{4}$, and $Ag_{2}ZnSnS_{4}$. The band gaps of 1.28 and 2.41 eV, respectively, make $Au_{2}Cs_{2}I_{6}$ and $Ag_{2}GeBaS_{4}$ optimal PV materials. Solar cells based on $Ag_{2}ZnSnS_{4}$ materials are interesting as a high efficiency gain for these types of cells has been recently observed. $^{40}$ There are also reports on the possibilities to integrate $Ag_{2}ZnSnS_{4}$ in the Cu based solar cells as an additional absorption layer. $^{40}$ The total DOS of $Au_{2}Cs_{2}I_{6}$ in Figure 5 shows that the IB is formed in the energy region between 0.64 and 1.34 eV. The IB composed of I 2p are described by the projected density of states (PDOS), as shown in Figure 5. Figure 6 shows that the IB is formed in the

![](./images/811033724157165568_7.jpg)

Figure 6. Total and site PDOS of $Ag_{2}GeBaS_{4}$. The Fermi level is set to zero and marked by a vertical dotted line.

energy region between 0.90 and 2.06 eV of the total DOS of $Ag_{2}GeBaS_{4}$. We have also plotted the PDOS at the IB mainly composed of the S 2p band and the Ge 4s band as well as the smaller mixing of the Ba 4d band. For $Ag_{2}ZnSnS_{4}$, the IB is formed in the energy region between 0.47 and 2.13 eV, and the electron density, as shown in Figure 7 better describes the states. The PDOS of $Ag_{2}ZnSnS_{4}$ at the IB mainly composed of the Sn 5s band and the S 2p band is shown in Figure 7. The $Ag_{2}ZnSnS_{4}$ has an energy gap of 2.62 eV. We found the excellent IB peaks between CB and VB in the three materials, namely, $Au_{2}Cs_{2}I_{6}$, $Ag_{2}GeBaS_{4}$, and $Ag_{2}ZnSnS_{4}$. We observed that the p and s states play a vital role in the band structure for the applicability of semiconductor for PV applications.

In Figures 5−7, broadening of IB indicates a highly parabolic dispersion relationship that induces lower values for the DOS. $^{41}$ From Tables 3 and 4, the electron effective masses of $Au_{2}Cs_{2}I_{6}$, $Ag_{2}GeBaS_{4}$, and $Ag_{2}ZnSnS_{4}$ are $0.095m_{e}$, $0.021m_{e}$, and $0.025m_{e}$, respectively. Lower values for the electron effective mass are as expected because the effective mass is directly related to the values of DOS. In addition, the IB region has the optimal thickness to balance the absorption rate and the recombination rate. $^{37}$ We may expect the effective IBSC to have IB thickness enough to ensure these materials to absorb sufficient subgap light. We conclude that the conversion efficiency of bulk IBSC strongly depends not only on the band gap but also on the position and thickness of IB and DOS. $^{37,41}$

![](./images/811033724157165568_8.jpg)

Figure 7. Total and site PDOS of $Ag_{2}ZnSnS_{4}$. The Fermi level is set to zero and marked by a vertical dotted line.

<table>
<thead>
<tr>
<th>serial no.</th>
<th>plane directions</th>
<th>compound</th>
<th>$m^{*}_{hh}\cdot m_{e}$</th>
<th>$m^{*}_{lh}\cdot m_{e}$</th>
<th>$m^{*}_{e}\cdot m_{e}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.</td>
<td>100</td>
<td>$CuAgPO_{4}$</td>
<td>3.875</td>
<td>4.969</td>
<td>14.229</td>
</tr>
<tr>
<td>2.</td>
<td>110</td>
<td>$Ag_{2}ZnSnS_{4}$</td>
<td>0.033</td>
<td>0.237</td>
<td>0.025</td>
</tr>
<tr>
<td>3.</td>
<td>110</td>
<td>$Au_{2}Cs_{2}Br_{6}$</td>
<td>0.870</td>
<td>1.810</td>
<td>0.806</td>
</tr>
<tr>
<td>4.</td>
<td>100</td>
<td>$Ag_{3}AsS_{4}$</td>
<td>0.200</td>
<td>0.234</td>
<td>0.012</td>
</tr>
<tr>
<td>5.</td>
<td>110</td>
<td>$Ag_{2}KSbS_{4}$</td>
<td>0.125</td>
<td>0.526</td>
<td>0.034</td>
</tr>
<tr>
<td>6.</td>
<td>110</td>
<td>$Na_{3}Se_{4}Sb$</td>
<td>0.377</td>
<td>0.381</td>
<td>0.085</td>
</tr>
<tr>
<td>7.</td>
<td>100</td>
<td>$AgK_{2}SbS_{4}$</td>
<td>1.524</td>
<td>12.025</td>
<td>1.007</td>
</tr>
<tr>
<td>8.</td>
<td>100</td>
<td>$AsRb_{3}Se_{4}$</td>
<td>6.213</td>
<td>84.330</td>
<td>2.595</td>
</tr>
<tr>
<td>9.</td>
<td>100</td>
<td>$AsCs_{3}Se_{4}$</td>
<td>8.213</td>
<td>24.794</td>
<td>3.561</td>
</tr>
<tr>
<td>10.</td>
<td>110</td>
<td>$Al_{2}HgSe_{4}$</td>
<td>0.070</td>
<td>0.255</td>
<td>0.021</td>
</tr>
<tr>
<td>11.</td>
<td>110</td>
<td>$PdPbF_{4}$</td>
<td>0.391</td>
<td>0.592</td>
<td>0.094</td>
</tr>
<tr>
<td>12.</td>
<td>100</td>
<td>$C_{2}Te_{2}F_{4}$</td>
<td>3.293</td>
<td>5.165</td>
<td>7.659</td>
</tr>
<tr>
<td>13.</td>
<td>100</td>
<td>$AlMoVO_{7}$</td>
<td>1.680</td>
<td>2.756</td>
<td>1.959</td>
</tr>
<tr>
<td>14.</td>
<td>110</td>
<td>$Ag_{6}SiSO_{8}$</td>
<td>0.145</td>
<td>2.634</td>
<td>0.053</td>
</tr>
</tbody>
</table>

## EFFECTIVE MASS CALCULATION

The calculation of the effective mass is important for a detailed study of energy levels in solar devices. The conductivity effective masses of electrons and holes affect the mobility, electrical resistivity, and free-carrier optical response of photovoltaic applications. $^{42}$ To investigate the electron/hole conduction properties of the identified IB materials, we have computed the electron/hole effective mass at the VB/CB. For an excellent IB, a low effective mass corresponds to a high mobility of the electrons/holes at the VB/CB and consequently high conductivity. For the EM calculation, we have employed the effective mass calculator (EMC). $^{43}$ EMC implements the calculation of the effective masses at the bands extreme using the finite difference method (FDM) (not the band-fitting method). The effective mass $(m^{*})$ of charge carriers is defined as $^{43}$

$$
\left( \frac{1}{m^{*}} \right)_{ij} = \frac{1}{\hbar^{2}} \frac{\partial^{2}E_{n}(\vec{k})}{\partial k_{i}k_{j}}, \ i,j=x,y,z \tag{1}
$$

where $x$, $y$, and $z$ are the directions in the reciprocal Cartesian space $(2\pi/A)$, $E_{n}(k)$ is the dispersion relation for the $n$th electronic band, and indices $i$ and $j$ denote reciprocal components. The explicit form of the symmetric tensor in the right-hand side of eq 1 is⁴³

$$
\frac{\mathrm{d}^{2} E}{\mathrm{~d} k^{2}}=\left(\begin{array}{ccc}
\frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{x}^{2}} & \frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{x} \mathrm{~d} k_{y}} & \frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{x} \mathrm{~d} k_{z}} \\
\frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{x} \mathrm{~d} k_{y}} & \frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{y}^{2}} & \frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{y} \mathrm{~d} k_{z}} \\
\frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{x} \mathrm{~d} k_{z}} & \frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{y} \mathrm{~d} k_{z}} & \frac{\mathrm{d}^{2} E}{\mathrm{~d} k_{z}^{2}}
\end{array}\right)
$$

(2)

The effective mass components are the inverse of the eigenvalues of eq 2, and the principal directions correspond to the eigenvectors.⁴³

To better understand the effective mass of semiconductors, it is not possible to fit the band to the quadratic polynomial. In this case, the results from the parabolic fitting can be reproduced with the FDM.⁴³ The FDM employed to solve the effective mass approximation equations because the spurious solutions can be included in the formalism, and the FDM can be solved by the hard equation having a high degree of polynomial.⁴⁴ This approach is quite reliable, and it was successfully applied for several classes of materials in the literature.⁴³ We present the effective masses of 14 compounds in Tables 3 and 4. The effective mass of an electron was computed from the minimum of the CB; the effective mass of the heavy hole was computed from the maximum of the first VB curvature, whereas the second VB curvature was used for the light hole. In the case of materials presented in Tables 3 and 4, the PBE functional predicts the effective masses of the light hole, heavy hole, and electron, which are parabolic-fitted values with a step size of 0.05 (1/bohr). The three narrow-band gap compounds, $K_{6}C_{60}$, $Au_{2}Cs_{2}I_{6}$, and $Ag_{2}GeBaS_{4}$, have low effective masses, as presented in Table 3.

The thirteen wide-band gap compounds in Table 4 have effective masses of electron lower than those of light holes and heavy holes except for $CuAgPO_{4}$. The effective masses of electron of photovoltaic materials silicon (Si), germanium (Ge), and gallium arsenide (GaAs) are $0.26m_{e}$, $0.067m_{e}$, and $0.12m_{e}$, respectively.⁴⁵,⁴⁶ The above three photovoltaic materials are single-band gap materials. It is well known that the band gaps of Si, Ge, and GaAs are 1.12, 0.66, and 1.424 eV, respectively. The maximum energy conversion of silicon and GaAs solar cells can reach 30% efficiency.⁴⁸ We can use germanium as the doping material in silicon solar cells because of its low band gap. We noticed that the effective masses of the electron for the silicon and GaAs are low.⁴⁵ From our results, we observed that the effective masses of electron for $K_{6}C_{60}$, $Au_{2}Cs_{2}I_{6}$, and $Ag_{2}GeBaS_{4}$ are $0.216m_{e}$, $0.095m_{e}$, and $0.021m_{e}$, respectively.

From Table 4, we noted that the effective masses of electron for $Ag_{2}ZnSnS_{4}$, $Au_{2}Cs_{2}Br_{6}$, $Ag_{3}AsS_{4}$, $Ag_{2}KSbS_{4}$, $Na_{3}Se_{4}Sb$, $Al_{2}HgSe_{4}$, $PdPbF_{4}$, $Ag_{6}SiSO_{8}$ are $0.025m_{e}$, $0.806m_{e}$, $0.012m_{e}$, $0.034m_{e}$, $0.085m_{e}$, $0.021m_{e}$, $0.094m_{e}$, and $0.053m_{e}$, respectively. Hence, the effective masses of electron of our narrow-band gap and wide-band gap materials are approximately equal to those of the photovoltaic materials. From Table 4, the effective mass of an electron is $0.025m_{e}$ for $Ag_{2}ZnSnS_{4}$ in [110] plane direction. We observed from Jing et al. that the effective mass of an electron is $0.16m_{e}$ for $Ag_{2}ZnSnS_{4}$ in [100] plane direction.⁴² Hence, we found a lower effective mass in [110] direction than in [100] direction. These effective masses are better described by the band structures of the most curved parabolic band, as shown in Figures 3−5. Because of the effective masses for the presented materials, in this article, the electron mobility from VB to CB will be higher and the recombination effect will be lower.

## CONCLUSIONS

We have carried out a comprehensive study of the electronic band structures of 2100 new bulk compounds using first- principle calculations with the DFT. Among these compounds, we have found that only 17 compounds have IBs. These compounds could be potentially used as photovoltaic materials based on the detailed studies of band structure, the DOS and effective mass calculations. Our effective mass calculations show that these compounds have high electron/hole conduction properties, which make them suitable for PV applications. Although we have studied 2100 new compounds from the ICSD database, our study clearly demonstrates the possibility of having more IB materials from the list of currently known compounds from the database. Thus, we are in the process of investigating more IB-compounds and results of the detailed analysis will be published in a forthcoming article.

## COMPUTATIONAL DETAILS

Total energies have been calculated by the projected augmented plane-wave (PAW) implementation of the Vienna ab initio simulation package.⁴⁷ Ground-state geometries were determined by minimizing stresses and the Hellman−Feynman forces using the conjugate-gradient algorithm with a force convergence threshold if $10^{-3}$ eV Å⁻¹. Brillouin-zone integration was performed using the Monkhorst−Pack k- meshes with a Gaussian broadening of 0.1 eV. A 600 eV kinetic energy cutoff was used for the plane-wave expansion. All of these calculations usually set to use approximately the same density of $k$-points in the reciprocal space for all structures. Because a large variety of structures was considered in this study, both metallic and insulating, we ensured that the $k$-points mesh was dense enough to determine the total energy with meV/atom accuracy. All structures containing transition elements are treated using the spin-polarized approach. In some cases, the starting magnetization vanished as self- consistency was reached. For all of these computations, the starting structures were directly taken from the ICSD database and input parameters, and file generation was done automati- cally by locally developed code "Tool". For the calculation of band structure, the $k$-point files were generated again with the help of locally developed code "KPATH". The information about the high symmetric points of the $k$-vector in the Brillouin zone was taken from the Bilbao Crystallographic Server.⁴⁸⁻⁵⁰ All of the calculated electronic structures of the studied systems are documented in the DFTBD database. For the transition metals, we have used exchange-correlation functional with the Hubbard parameter correction (GGA+U), following the rotationally invariant form. The full details about the computed $U$ and $J$ values are presented in the DFTBD database website.⁵¹⁻⁵⁴

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acsomega.6b00534.

Tables, list of computed compounds and figures (PDF)

## AUTHOR INFORMATION

### Corresponding Author
*E-mail: rmu@hvl.no.

#### ORCID
Murugesan Rasukkannu: 0000-0002-2167-3242

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
The authors gratefully acknowledge the Bergen University College for financially supporting M.R. P.V. and D.V. acknowledge the NOTUR computing facilities of project. numbers NN2867K and NN2875K, which have been used to conduct the calculations presented in this article, and further acknowledge Dr.Vishnu for fruitful discussions.

## REFERENCES
(1) Luque, A.; Marti, A.; Stanley, C. Understanding IntermediateBand Solar Cells. Nat. Photonics 2012, 6, 146−152.

(2) Luque, A.; Marti, A. A metallic intermediate band high efficiency solar cell. Prog. Photovoltaics 2001, 9, 73−86.

(3) Shockley, W.; Queisser, H. J. Detailed balance limit of efficiency of p-n junction solar cells. J. Appl. Phys. 1961, 32, 510−519.

(4) Luque, A.; Martí, A. Increasing the efficiency of ideal solar cells by photon induced transitions at intermediate levels. Phys. Rev. Lett. 1997, 78, 5014.

(5) Palacios, P.; Aguilera, I.; Sánchez, K.; Conesa, J.; Wahnón, P. Transition-metal-substituted indium thiospinels as novel intermediateband materials: prediction and understanding of their electronic properties. Phys. Rev. Lett. 2008, 101, No. 046403.

(6) Green, M. A. Multiple band and impurity photovoltaic solar cells: general theory and comparison to tandem cells. Prog. Photovoltaics 2001, 9, 137−144.

(7) Shockley, W.; Read, W., Jr. Statistics of the recombinations of holes and electrons. Phys. Rev. 1952, 87, 835−842.

(8) Hall, R. N. Electron-hole recombination in germanium. Phys. Rev. 1952, 87, 387.

(9) Lang, D.; Henry, C. Nonradiative recombination at deep levels in GaAs and GaP by Lattice-Relaxation Multiphonon Emission. Phys. Rev. Lett. 1975, 35, 1525.

(10) Wolf, M. Limitations and possibilities for improvement of photovoltaic solar energy converters: part I: considerations for earth’s surface operation. Proc. IRE 1960, 48, 1246−1263.

(11) Ekins-Daukes, N.; Honsberg, C.; Yamaguchi, M. In Signature of Intermediate Band Materials from Luminescence Measurements, Proceedings of the 31st IEEE Photovoltaic Specialists Conference, 2005; IEEE, 2005; pp 49−54.

(12) Strandberg, R.; Reenaas, T. W. Photofilling of intermediate bands. J. Appl. Phys. 2009, 105, No. 124512.

(13) Levy, M. Y.; Honsberg, C. Solar cell with an intermediate band of finite width. Phys. Rev. B 2008, 78, No. 165122.

(14) Hubbard, S.; Cress, C.; Bailey, C.; Raffaelle, R.; Bailey, S.; Wilt, D. Effect of strain compensation on quantum dot enhanced GaAs solar cells. Appl. Phys. Lett. 2008, 92, No. 123512.

(15) Oshima, R.; Takata, A.; Okada, Y. Strain-compensated InAs/ GaNAS quantum dots for use in high-efficiency solar cells. Appl. Phys. Lett. 2008, 93, No. 083111.

(16) Kechiantz, A.; Sun, K.; Kechiyants, H.; Kocharyan, L. Selfordered Ge/Si quantum dot intermediate band photovoltaic solar cells. ISJAEE 2005, 12, 85−87.

(17) Laghumavarapu, R.; El-Emawy, M.; Nuntawong, N.; Moscho,A.; Lester, L.; Huffaker, D. Improved device performance of InAs/ GaAs quantum dot solar cells with GaP strain compensation layers. Appl. Phys. Lett. 2007, 91, 243115.

(18) Popescu, V.; Bester, G.; Hanna, M. C.; Norman, A. G.; Zunger, A. Theoretical and experimental examination of the intermediate-band concept for strain-balanced (In, Ga) As/Ga (As, P) quantum dot solar cells. Phys. Rev. B 2008, 78, No. 205321.

(19) Bailey, C. G.; Forbes, D. V.; Raffaelle, R. P.; Hubbard, S. M. Near 1 V open circuit voltage InAs/GaAs quantum dot solar cells. Appl. Phys. Lett. 2011, 98, No. 163105.

(20) Blokhin, S.; Sakharov, A.; Nadtochy, A.; Pauysov, A.; Maximov, M.; Ledentsov, N.; Kovsh, A.; Mikhrin, S.; Lantratov, V.; Mintairov, S.; et al. AlGaAs/GaAs photovoltaic cells with an array of InGaAs QDs. Semiconductors 2009, 43, 514−518.

(21) Guimard, D.; Morihara, R.; Bordel, D.; Tanabe, K.; Wakayama, Y.; Nishioka, M.; Arakawa, Y. Fabrication of InAs/GaAs quantum dot solar cells with enhanced photocurrent and without degradation of open circuit voltage. Appl. Phys. Lett. 2010, 96, No. 203507.

(22) Zhou, D.; Sharma, G.; Thomassen, S.; Reenaas, T.; Fimland, B. Optimization towards high density quantum dots for intermediate band solar cells grown by molecular beam epitaxy. Appl. Phys. Lett. 2010, 96, No. 061913.

(23) Walukiewicz, W.; Shan, W.; Yu, K.; Ager, J., III; Haller, E.; Miotkowski, I.; Seong, M.; Alawadhi, H.; Ramdas, A. Interaction of localized electronic states with the conduction band: Band anticrossing in II−VI semiconductor ternaries. Phys. Rev. Lett. 2000, 85, 1552.

(24) Wang, W.; Lin, A. S.; Phillips, J. D. Intermediate-band photovoltaic solar cell based on ZnTe: O. Appl. Phys. Lett. 2009, 95, No. 011103.

(25) Wang, W.; Lin, A. S.; Phillips, J. D.; Metzger, W. K. Generation and recombination rates at ZnTe: O intermediate band states. Appl. Phys. Lett. 2009, 95, No. 261107.

(26) Antolín, E.; Marti, A.; Olea, J.; Pastor, D.; González-Díaz, G.; Mártil, I.; Luque, A. Lifetime recovery in ultrahighly titanium-doped silicon for the implementation of an intermediate band material. Appl. Phys. Lett. 2009, 94, No. 042115.

(27) Wahnón, P.; Tablero, C. Ab initio electronic structure calculations for metallic intermediate band formation in photovoltaic materials. Phys. Rev. B 2002, 65, No. 165115.

(28) Ling, C.; Zhou, L. Q.; Banerjee, D.; Jia, H. Band structures of ZnTe: O alloys with isolated oxygen and with clustered oxygen impurities. J. Alloys Compd. 2014, 584, 289−294.

(29) Strandberg, R. Evaluation of a selection of intermediate band materials based on their absorption coefficients. IEEE J. Photovoltaics 2013, 3, 997−1003.

(30) Aguilera, I.; Palacios, P.; Sánchez, K.; Wahnón, P. Theoretical optoelectronic analysis of $MnIn_2S_4$ and $CdIn_2S_4$ thiospinels: effect of transition-metal substitution in intermediate-band formation. Phys. Rev. B 2010, 81, No. 075206.

(31) Kong-Ping, W.; Shu-Lin, G.; Jian-Dong, Y.; Kun, T.; Shun-Ming, Z.; Meng-Ran, Z.; You-Rui, H.; Rong, Z.; You-Dou, Z. Theoretical optoelectronic analysis of intermediate-band photovoltaic material based on ZnY1 − xOx (Y = S, Se, Te) semiconductors by firstprinciples calculations. Chin. Phys. B 2013, 22, No. 107103.

(32) Palacios, P.; Wahnón, P.; Pizzinato, S.; Conesa, J. C. Energetics of formation of $TiGa_3As_4$ and $TiGa_3P_4$ intermediate band materials. J. Chem. Phys. 2006, 124, No. 014711.

(33) Sánchez, K.; Aguilera, I.; Palacios, P.; Wahnón, P. Assessment through first-principles calculations of an intermediate-band photovoltaic material based on Ti-implanted silicon: Interstitial versus substitutional origin. Phys. Rev. B 2009, 79, No. 165203.

(34) Huang, F.-W.; Sheu, J.-K.; Lee, M.-L.; Tu, S.-J.; Lai, W.-C.; Tsai, W.-C.; Chang, W.-H. Linear photon up-conversion of 450 meV in InGaN/GaN multiple quantum wells via Mn-doped GaN intermediate band photodetection. Opt. Express 2011, 19, A1211−A1218.

(35) Lundqvist, S.; March, N. H. *Theory of the Inhomogeneous Electron Gas*; Springer US, 1983; pp 309−389.

(36) Erwin, S. C.; Pederson, M. R. Electronic structure of crystalline K₆C₆₀. *Phys. Rev. Lett.* 1991, 67, 1610.

(37) Sullivan, J. T.; Simmons, C. B.; Buonassisi, T.; Krich, J. J. Targeted search for effective intermediate band solar cell materials. *IEEE J. Photovoltaics* 2015, 5, 212−218.

(38) Levy, M. Y.; Honsberg, C. Solar cell with an intermediate band of finite width. *Phys. Rev. B* 2008, 78, No. 165122.

(39) Levy, M. Y.; Honsberg, C. Intraband absorption in solar cells with an intermediate band. *J. Appl. Phys.* 2008, 104, No. 113103.

(40) Jing, T.; Dai, Y.; Ma, X.; Wei, W.; Huang, B. Electronic Structure and Photocatalytic Water-Splitting Properties of Ag₂ZnSn(S1−x Se x)₄. *J. Phys. Chem. C* 2015, 119, 27900−27908.

(41) Okada, Y.; Ekins-Daukes, N.; Kita, T.; Tamaki, R.; Yoshida, M.; Pusch, A.; Hess, O.; Phillips, C.; Farrell, D.; Yoshida, K.; et al. Intermediate band solar cells: Recent progress and future directions. *Appl. Phys. Rev.* 2015, 2, No. 021302.

(42) Riffe, D. M. Temperature dependence of silicon carrier effective masses with application to femtosecond reflectivity measurements. *J. Opt. Soc. Am. B* 2002, 19, 1092−1100.

(43) Fonari, A.; Sutton, C. Validation of the Effective Masses Calculated Using Finite Difference Method on a Five-Point Stencil for Inorganic and Organic Semiconductors. 2013, arXiv:condensed matter/1302.4996. arXiv.org e-Print archive. https://arxiv.org/abs/1302.4996.

(44) Cartoixa, X.; Ting, D.-Y.; McGill, T. Numerical spurious solutions in the effective mass approximation. *J. Appl. Phys.* 2003, 93, 3974−3981.

(45) Van Zeghbroeck, B. *Principles of Semiconductor Devices*; Colarado University, 2004.

(46) Green, M. A.; Emery, K.; Hishikawa, Y.; Warta, W.; Dunlop, E. D. Solar cell efficiency Tables (Version 45). *Prog. Photovoltaics* 2015, 23, 1−9.

(47) Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. *Phys. Rev. B* 1996, 54, 11169−11186.

(48) Aroyo, M.; Perez-Mato, J.; Orobengoa, D.; Tasci, E.; De La Flor, G.; Kirov, A. Crystallography online: Bilbao crystallographic server. *Bulg. Chem. Commun.* 2011, 43, 183−197.

(49) Aroyo, M. I.; Perez-Mato, J. M.; Capillas, C.; Kroumova, E.; Ivantchev, S.; Madariaga, G.; Kirov, A.; Wondratschek, H. Bilbao Crystallographic Server: I. Databases and crystallographic computing programs. *Z. Kristallogr. - Cryst. Mater.* 2006, 221, 15−27.

(50) Aroyo, M. I.; Kirov, A.; Capillas, C.; Perez-Mato, J.; Wondratschek, H. Bilbao Crystallographic Server. II. Representations of crystallographic point groups and space groups. *Acta Crystallogr., Sect. A: Found. Crystallogr.* 2006, 62, 115−128.

(51) Dudarev, S.; Botton, G.; Savrasov, S. Y.; Szotek, Z.; Temmerman, W.; Sutton, A. Electronic Structure and Elastic Properties of Strongly Correlated Metal Oxides from First Principles: LSDA + U, SIC-LSDA and EELS Study of UO₂ and NiO. *Phys. Status Solidi A* 1998, 166, 429−443.

(52) Kresse, G.; Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. *Comput. Mater. Sci.* 1996, 6, 15−50.

(53) Liechtenstein, A.; Anisimov, V.; Zaanen, J. Density-functional theory and strong interactions: Orbital ordering in Mott-Hubbard insulators. *Phys. Rev. B: Condens. Matter Mater. Phys.* 1995, 52, No. R5467.

(54) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* 1996, 77, 3865.