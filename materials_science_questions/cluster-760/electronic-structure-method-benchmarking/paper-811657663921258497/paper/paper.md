REGULAR ARTICLE

# Assessment of theoretical procedures for hydrogen-atom abstraction by chlorine, and related reactions

Bun Chan · Leo Radom

Received: 28 March 2011 / Accepted: 17 May 2011 / Published online: 4 June 2011
© Springer-Verlag 2011

**Abstract** We have examined a number of hydrogen-abstraction reactions and assessed various theoretical procedures with regard to their performance for geometry optimization and for calculating barriers and reaction energies. We find that the BH&H-LYP and M05-2X procedures with the 6-31+G(d,p) basis set provide reasonable predictions for the geometries of the transition structures and also yield reasonable imaginary frequencies when compared with our benchmark QCISD/6-31+G(d,p) and CCSD(T)/6-311+G(3df,2p) values. For the calculation of barriers and reaction energies, M05-2X appears to be the most accurate of the hybrid functionals. The double-hybrid functionals, B2K-PLYP, UB2-PLYP-09, ROB2-PLYP, and DSD-B-LYP-D3, when used in combination with an augmented triple-zeta basis set, give very good agreement with the benchmark URCCSD(T)/aug-cc-pVQZ energies. We find that for wavefunction procedures, use of CCSD(T) in combination with an augmented triple-zeta quality basis set is required for the accurate prediction of barriers and reaction energies for these reactions.

**Keywords** Hydrogen abstraction · Ab initio · Density functional theory

---

Dedicated to Professor Shigeru Nagase on the occasion of his 65th birthday and published as part of the Nagase Festschrift Issue.

Electronic supplementary material The online version of this article (doi:10.1007/s00214-011-0967-z) contains supplementary material, which is available to authorized users.

B. Chan · L. Radom (⊗)
School of Chemistry and ARC Centre of Excellence for Free Radical Chemistry and Biotechnology, University of Sydney, Sydney, NSW 2006, Australia
e-mail: radom@chem.usyd.edu.au

B. Chan
e-mail: chan_b@chem.usyd.edu.au

---

## 1 Introduction

Free radical chlorination is an important reaction in organic synthesis [1], industrial processes [2], and stratospheric chemistry [3–6]. The reaction is used for the industrial synthesis of chloroform, dichloromethane, and hexachlorobutadiene [2]. It also represents a significant loss channel for stratospheric methane, which impacts greenhouse-gas models [4]. Furthermore, radical chlorination reactions of methane and ethane are widely used as reference reactions in relative rate studies [7–12]. Finally, hydrogen-atom abstraction by chlorine is an important step for the propagation of free radical chlorination [1]. Thus, determination of accurate kinetic parameters for these types of reactions is desirable.

Computational quantum chemistry [13–15] is a powerful tool for obtaining such quantities. For instance, Yamataka and Nagase investigated hydrogen-abstraction reactions using the MP2 procedure [16]. The higher-level CCSD(T) procedure with the Dunning quadruple-zeta aug-cc-pVQZ basis set [17–19] has been applied to the $Cl\bullet + CH_4 \rightarrow ClH + \bullet CH_3$ reaction [20], while the related $F\bullet + CH_4 \rightarrow FH + \bullet CH_3$ reaction has been studied at the CCSD(T) level with the larger aug-cc-pCV5Z basis set [21]. Although the high-level CCSD(T) method allows the evaluation of thermodynamic and kinetic parameters with sub-$kJ\ mol^{-1}$ accuracy, it is applicable today only to relatively small systems. As a result, finding a compromise between accuracy and computational cost is important for further advancing the theoretical study of these reactions.

Taylor et al. [22] have recently examined hydrogen abstraction by chlorine atom from a set of small molecules

![](./images/811657663921258497_1.jpg)

related to the building blocks of amino acids. It was found that for geometry optimization, some popular density functional theory (DFT) methods such as B3-LYP [23–25] and BMK [26] do not give reliable transition structures (TSs) compared with benchmark CCSD(T) or QCISD geometries. For the evaluation of energies, the theoretical procedures performed in the order W1′ [27–29] > G3X (MP2)-RAD [30] > ROMP2/G3XLarge [31] ~ UB2-PLYP [32]/G3XLarge > UBMK/G3XLarge > UB3-LYP/ G3XLarge.

While these results provide helpful insights into the appropriate theoretical procedures for studying hydrogen abstraction by chlorine, it would be useful to extend this study. Specifically, identifying a reliable DFT procedure for optimizing transition structures would be beneficial, because the use of CCSD(T) and QCISD geometries can rapidly become prohibitively expensive. Furthermore, it would also be attractive to evaluate the performance of a wider range of DFT procedures for the calculation of reaction energies and barriers, in the hope of further reducing the cost of computations. In the present study, we address these issues with an extended investigation into hydrogen abstraction by chlorine, and related reactions.

## 2 Computational details

Standard ab initio molecular orbital theory and DFT cal- culations were carried out with GAUSSIAN 09 [33] and MOLPRO 2006 [34]. The frozen-core approximation was used in all wavefunction correlation calculations. Geome- tries of stationary points were optimized using UQCISD and various DFT procedures with the 6-31+G(d,p) basis set. The DFT procedures that have been examined for their performance for geometry optimization are hybrid func- tionals, namely B3-LYP [23], B3-P86 [35], B3-PW91 [36], B97-2 [37], B98 [38], BH&H-LYP [39], BMK [26], M05 [40], M05-2X [41], M06 [42], M06-2X [42], MPW1PW91 [43], and PBE1-PBE [44]. Following each geometry opti- mization, harmonic frequency analysis at the same level of theory was carried out to confirm the nature of the sta- tionary point as a minimum (equilibrium structure) or first- order saddle point (transition structure).

Benchmark energies were calculated at the UR- CCSD(T)/aug-cc-pVQZ level. We employed the aug-cc- pwCVQZ basis set [45] for bromine, in place of aug-cc- pVQZ, in order to appropriately account for the correlation effects of the 3d orbitals. In the present study, we have assessed the performance of the wavefunction methods HF, MP2, MP3, MP4, CCSD and CCSD(T), as well as various DFT procedures. The DFT procedures examined include pure functionals B-LYP [23] and M06-L [42], hybrid functionals B3-LYP, LC-B-LYP [46], CAM-B3-LYP [47], ωB97X-D [48], BH&H-LYP, BMK, M05, M05-2X, M06 and M06-2X, and double-hybrid functionals UB2-PLYP [32], UB2K-PLYP [49], and their R variants (RB2-PLYP and RB2K-PLYP) in which the proportion of HF exchange and MP2 correlation are assumed to be the same as for the U methods. In addition, we have examined UB2-PLYP-09 [50] and ROB2-PLYP [50], in which the proportion of HF exchange and MP2 correlation have been optimized using the same test set, specifically the 148 heats of formation from the G2/97 set [51, 52], as well as DSD-B-LYP-D3 [53]. Single-point energies at the above levels were cal- culated in combination with a variety of basis sets, including the Pople-type basis sets [13] 6-31G(d), 6-31+G(d,p), 6-311+G(2df,p), 6-311+G(3df,2p) and G3LargeXP [54], and the Dunning sets [17] cc-pVnZ and aug-cc-pVnZ ($n = \text{D, T and Q}$). Bond lengths reported in the paper are in Å, while relative energies are vibrationless values in $\text{kJ mol}^{-1}$.

## 3 Results and discussion

### 3.1 Choice of geometry

In order to identify the appropriate DFT procedure for geometry optimization, we have considered the transition structures for the set of five hydrogen-abstraction reactionsthat have also been used for this purpose in reference [22]:

$$\text{Cl}\bullet + \text{CH}_4 \rightarrow \text{ClH} + \bullet\text{CH}_3 \tag{1}$$

$$\text{Cl}\bullet + \text{CH}_3\text{NH}_3^+ \rightarrow \text{ClH} + \bullet\text{CH}_2\text{NH}_3^+ \tag{2}$$

$$\text{Cl}\bullet + \text{CH}_3\text{CHO} \rightarrow \text{ClH} + \bullet\text{CH}_2\text{CHO} \tag{3}$$

$$\text{Cl}\bullet + \text{CH}_3\text{CO}_2\text{H} \rightarrow \text{ClH} + \bullet\text{CH}_2\text{CO}_2\text{H} \tag{4}$$

$$\text{Cl}\bullet + \text{CH}_3\text{CO}_2^- \rightarrow \text{ClH} + \bullet\text{CH}_2\text{CO}_2^- \tag{5}$$

We first examine the geometries obtained with the com- plete set of 13 hybrid DFT procedures for reaction 1, with a focus on the key bond lengths, namely the Cl–H bond that is being formed, the H–C bond that is being broken, and the distance between the Cl and C atoms. We then further assess several of the more promising procedures for reactions 2–5. We also compare the calculated imag- inary frequencies with the benchmark values to assess the ability of the DFT procedures to obtain reliable estimates of the curvature on the potential energy surface in the vicinity of the transition structure. The results are shown in Table 1.

For the transition structure for the reaction of Cl• with CH₄, there is a range of 0.089 Å for the predicted Cl$\cdots$H distance, with the shortest distance being the one obtained with B3-P86 (1.370 Å) and the longest being that for M05 (1.459 Å). We find that the BH&H-LYP functional

![](./images/811657663921258497_2.jpg)

<table>
<caption>Table 1 Imaginary frequencies ($\omega_{\mathrm{i}}$, $\mathrm{cm}^{-1}$) for the transition structures, and selected interatomic distances (Å), and their mean absolute deviations (MAD) and largest deviations (LD) from CCSD(T) or QCISD values</caption>
<thead>
<tr>
<th></th>
<th>Substrate</th>
<th>Methodª</th>
<th>$\omega_{\mathrm{i}}$</th>
<th>Cl$\cdots$H</th>
<th>H$\cdots$C</th>
<th>Cl$\cdots$C</th>
<th>MAD</th>
<th>LD</th>
</tr>
</thead>
<tbody>
<tr>
<td>(1)</td>
<td>CH₄</td>
<td>B3-LYP</td>
<td>338.7</td>
<td>1.391</td>
<td>1.584</td>
<td>2.975</td>
<td>0.113</td>
<td>0.170</td>
</tr>
<tr>
<td></td>
<td></td>
<td>B3-P86</td>
<td>196.7</td>
<td>1.370</td>
<td>1.626</td>
<td>2.996</td>
<td>0.141</td>
<td>0.212</td>
</tr>
<tr>
<td></td>
<td></td>
<td>B3-PW91</td>
<td>283.7</td>
<td>1.383</td>
<td>1.584</td>
<td>2.968</td>
<td>0.113</td>
<td>0.170</td>
</tr>
<tr>
<td></td>
<td></td>
<td>B97-2</td>
<td>312.9</td>
<td>1.381</td>
<td>1.577</td>
<td>2.957</td>
<td>0.108</td>
<td>0.163</td>
</tr>
<tr>
<td></td>
<td></td>
<td>B98</td>
<td>194.9</td>
<td>1.373</td>
<td>1.646</td>
<td>3.020</td>
<td>0.155</td>
<td>0.232</td>
</tr>
<tr>
<td></td>
<td></td>
<td>BH&amp;H-LYP</td>
<td>972.7</td>
<td>1.426</td>
<td>1.450</td>
<td>2.876</td>
<td>0.024</td>
<td>0.036</td>
</tr>
<tr>
<td></td>
<td></td>
<td>BMK</td>
<td>328.3</td>
<td>1.394</td>
<td>1.591</td>
<td>2.985</td>
<td>0.118</td>
<td>0.177</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05</td>
<td>761.0</td>
<td>1.459</td>
<td>1.403</td>
<td>2.862</td>
<td>0.013</td>
<td>0.020</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05-2X</td>
<td>807.8</td>
<td>1.426</td>
<td>1.470</td>
<td>2.896</td>
<td>0.037</td>
<td>0.056</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06</td>
<td>508.6</td>
<td>1.421</td>
<td>1.499</td>
<td>2.920</td>
<td>0.056</td>
<td>0.085</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06-2X</td>
<td>745.9</td>
<td>1.409</td>
<td>1.508</td>
<td>2.917</td>
<td>0.062</td>
<td>0.094</td>
</tr>
<tr>
<td></td>
<td></td>
<td>MPW1-PW91</td>
<td>356.9</td>
<td>1.391</td>
<td>1.546</td>
<td>2.937</td>
<td>0.088</td>
<td>0.132</td>
</tr>
<tr>
<td></td>
<td></td>
<td>PBE1-PBE</td>
<td>311.5</td>
<td>1.386</td>
<td>1.561</td>
<td>2.946</td>
<td>0.097</td>
<td>0.147</td>
</tr>
<tr>
<td></td>
<td></td>
<td>QCISD</td>
<td>1,254.6</td>
<td>1.435</td>
<td>1.415</td>
<td>2.850</td>
<td>0.003</td>
<td>–0.004</td>
</tr>
<tr>
<td></td>
<td></td>
<td>QCISDb</td>
<td>1,220.6</td>
<td>1.448</td>
<td>1.396</td>
<td>2.844</td>
<td>0.012</td>
<td>–0.018</td>
</tr>
<tr>
<td></td>
<td></td>
<td>CCSD(T)b</td>
<td>1,245.8</td>
<td>1.439</td>
<td>1.414</td>
<td>2.854</td>
<td></td>
</tr>
<tr>
<td>(2)</td>
<td>CH₃NH₃⁺</td>
<td>B3-LYP</td>
<td>847.0</td>
<td>1.391</td>
<td>1.550</td>
<td>2.868</td>
<td>0.051</td>
<td>0.087</td>
</tr>
<tr>
<td></td>
<td></td>
<td>BH&amp;H-LYP</td>
<td>1,350.6</td>
<td>1.402</td>
<td>1.473</td>
<td>2.819</td>
<td>0.005</td>
<td>0.010</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05</td>
<td>913.4</td>
<td>1.416</td>
<td>1.457</td>
<td>2.814</td>
<td>0.007</td>
<td>0.014</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05-2X</td>
<td>1,277.5</td>
<td>1.409</td>
<td>1.478</td>
<td>2.805</td>
<td>0.010</td>
<td>0.015</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06</td>
<td>1,030.1</td>
<td>1.406</td>
<td>1.515</td>
<td>2.823</td>
<td>0.022</td>
<td>0.052</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06-2X</td>
<td>1,206.7</td>
<td>1.393</td>
<td>1.520</td>
<td>2.823</td>
<td>0.025</td>
<td>0.057</td>
</tr>
<tr>
<td></td>
<td></td>
<td>QCISD</td>
<td>1,536.4</td>
<td>1.402</td>
<td>1.463</td>
<td>2.814</td>
<td></td>
</tr>
<tr>
<td>(3)</td>
<td>CH₃CHO</td>
<td>B3-LYP</td>
<td>1,068.5</td>
<td>1.480</td>
<td>1.393</td>
<td>2.868</td>
<td>0.029</td>
<td>0.047</td>
</tr>
<tr>
<td></td>
<td></td>
<td>BH&amp;H-LYP</td>
<td>1,442.1</td>
<td>1.495</td>
<td>1.341</td>
<td>2.834</td>
<td>0.009</td>
<td>0.015</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05</td>
<td>1,216.1</td>
<td>1.180</td>
<td>1.295</td>
<td>2.831</td>
<td>0.119</td>
<td>–0.300</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05-2X</td>
<td>1,139.6</td>
<td>1.509</td>
<td>1.340</td>
<td>2.842</td>
<td>0.017</td>
<td>0.029</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06</td>
<td>1,075.2</td>
<td>1.508</td>
<td>1.342</td>
<td>2.847</td>
<td>0.018</td>
<td>0.028</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06-2X</td>
<td>1,096.5</td>
<td>1.485</td>
<td>1.358</td>
<td>2.842</td>
<td>0.011</td>
<td>0.016</td>
</tr>
<tr>
<td></td>
<td></td>
<td>QCISD</td>
<td>1,612.0</td>
<td>1.480</td>
<td>1.346</td>
<td>2.826</td>
<td></td>
</tr>
<tr>
<td>(4)</td>
<td>CH₃CO₂H</td>
<td>B3LYP</td>
<td>998.4</td>
<td>1.453</td>
<td>1.429</td>
<td>2.880</td>
<td>0.041</td>
<td>0.062</td>
</tr>
<tr>
<td></td>
<td></td>
<td>BH&amp;H-LYP</td>
<td>1,425.1</td>
<td>1.468</td>
<td>1.372</td>
<td>2.838</td>
<td>0.007</td>
<td>0.010</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05</td>
<td>1,257.8</td>
<td>1.516</td>
<td>1.314</td>
<td>2.829</td>
<td>0.036</td>
<td>0.055</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05-2X</td>
<td>1,227.6</td>
<td>1.474</td>
<td>1.374</td>
<td>2.847</td>
<td>0.013</td>
<td>0.019</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06</td>
<td>931.9</td>
<td>1.477</td>
<td>1.377</td>
<td>2.854</td>
<td>0.017</td>
<td>0.026</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06-2X</td>
<td>1,085.3</td>
<td>1.451</td>
<td>1.403</td>
<td>2.854</td>
<td>0.024</td>
<td>0.036</td>
</tr>
<tr>
<td></td>
<td></td>
<td>QCISD</td>
<td>1,581.6</td>
<td>1.461</td>
<td>1.367</td>
<td>2.828</td>
<td></td>
</tr>
<tr>
<td>(5)</td>
<td>CH₃CO₂⁻</td>
<td>B3-LYP</td>
<td>294.7</td>
<td>1.340</td>
<td>2.041</td>
<td>3.308</td>
<td>0.312</td>
<td>0.498</td>
</tr>
<tr>
<td></td>
<td></td>
<td>BH&amp;H-LYP</td>
<td>203.0</td>
<td>1.379</td>
<td>1.658</td>
<td>3.020</td>
<td>0.075</td>
<td>0.115</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05</td>
<td>172.4</td>
<td>1.330</td>
<td>1.985</td>
<td>3.264</td>
<td>0.282</td>
<td>0.442</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M05-2X</td>
<td>108.8</td>
<td>1.337</td>
<td>1.895</td>
<td>3.184</td>
<td>0.223</td>
<td>0.352</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06</td>
<td>186.9</td>
<td>1.347</td>
<td>1.910</td>
<td>3.210</td>
<td>0.233</td>
<td>0.367</td>
</tr>
<tr>
<td></td>
<td></td>
<td>M06-2X</td>
<td>226.4</td>
<td>1.360</td>
<td>1.773</td>
<td>3.106</td>
<td>0.149</td>
<td>0.230</td>
</tr>
<tr>
<td></td>
<td></td>
<td>QCISD</td>
<td>422.5</td>
<td>1.415</td>
<td>1.543</td>
<td>2.945</td>
<td></td>
</tr>
</tbody>
</table>

Benchmark CCSD(T) and QCISD values obtained from Ref. [22]

ª The 6-31+G(d,p) basis set was employed unless otherwise noted
b 6-311+G(3df,2p)

![](./images/811657663921258497_3.jpg)

$(1.426\ \text{Å})$ yields the best agreement with the benchmark CCSD(T) value $(1.439\ \text{Å})$. The range for the calculated $\text{H}\cdots\text{C}$ distance is much wider $(0.243\ \text{Å})$, from $1.403\ \text{Å}$ for M05 to $1.646\ \text{Å}$ for B98. In this case, the M05 procedure gives the best agreement with the CCSD(T) value of $1.414\ \text{Å}$. The range for the $\text{Cl}\cdots\text{C}$ distance $(0.176\ \text{Å})$ is somewhat smaller than that for the $\text{H}\cdots\text{C}$ distance $(0.243\ \text{Å})$, indicating some compensation between $\text{Cl}\cdots\text{H}$ and $\text{H}\cdots\text{C}$ bonds. Overall, we find that the BH&H-LYP, M05-2X, and M05 procedures provide the best estimates for the key bond lengths in the $\text{Cl}\bullet+\text{CH}_4$ transition structure, with mean absolute deviations (MADs) of 0.024, 0.037, and $0.013\ \text{Å}$, respectively.

For the calculated imaginary frequencies for the TSs for the reaction of $\text{Cl}\bullet$ with $\text{CH}_4$, we find that when compared with the CCSD(T) value of $1,245.8\ \text{cm}^{-1}$, all DFT procedures underestimate the frequency of this vibration, with a lowest value of $194.9\ \text{cm}^{-1}$ predicted by B98. We find that BH&H-LYP, M05-2X, and M05 yield frequencies that are in closest agreement with CCSD(T), with values of 971.8, 807.8, and $761.0\ \text{cm}^{-1}$, respectively. The closer agreement of these three DFT procedures with CCSD(T) results, both in terms of the key bond distances, as well as the predicted imaginary frequencies, has led us to further investigate their performance for reactions 2–5. We have also included in our analysis the widely used B3-LYP method and two procedures closely related to M05 and M05-2X, namely M06 and M06-2X.

We find that these functionals generally give MADs for the transition structures for reactions 2–5 that are smaller than $0.05\ \text{Å}$, with the exception of those for reaction 5, for which all the DFT procedures appear to significantly overestimate the $\text{Cl}\cdots\text{C}$ separation. For example, the MAD for BH&H-LYP is $0.075\ \text{Å}$, while much larger deviations are seen for B3-LYP $(0.312\ \text{Å})$, M05 $(0.282\ \text{Å})$, M05-2X $(0.223\ \text{Å})$, M06 $(0.233\ \text{Å})$, and M06-2X $(0.149\ \text{Å})$. For reactions 2–5, BH&H-LYP has the smallest overall MAD $(0.024\ \text{Å})$ as well as the smallest LD (largest deviation, $0.115\ \text{Å}$), while B3-LYP yields the largest MAD $(0.109\ \text{Å})$ and LD $(0.498\ \text{Å})$ values. It is also apparent that BH&H-LYP gives the closest agreement with QCISD for the calculated imaginary frequencies for reactions 2–5. Based on these observations, we have chosen BH&H-LYP/6-31+G(d,p) for geometry optimization for the rest of our investigation.

### 3.2 Choice of single-point energy

Turning our attention to the performance of the various procedures for calculating relative energies, we have investigated the prototypical hydrogen-atom abstractions from $\text{CH}_4$ by the $\text{Cl}\bullet$, $\text{F}\bullet$, $\text{Br}\bullet$, $\text{HO}\bullet$, and $\text{HOO}\bullet$ radicals, and abstraction from $\text{CH}_3\text{CHO}$ by $\text{Cl}\bullet$:

$$\text{Cl}\bullet+\text{CH}_4\rightarrow\text{ClH}+\bullet\text{CH}_3\tag{1}$$

$$\text{F}\bullet+\text{CH}_4\rightarrow\text{FH}+\bullet\text{CH}_3\tag{6}$$

$$\text{Br}\bullet+\text{CH}_4\rightarrow\text{BrH}+\bullet\text{CH}_3\tag{7}$$

$$\text{HO}\bullet+\text{CH}_4\rightarrow\text{H}_2\text{O}+\bullet\text{CH}_3\tag{8}$$

$$\text{HOO}\bullet+\text{CH}_4\rightarrow\text{H}_2\text{O}_2+\bullet\text{CH}_3\tag{9}$$

$$\text{Cl}\bullet+\text{CH}_3\text{CHO}\rightarrow\text{ClH}+\bullet\text{CH}_2\text{CHO}\tag{10}$$

Reaction 10 was included in the present study because it represents the most challenging case examined in reference 22, largely associated with spin contamination in the TS for abstraction, and in the product $\bullet\text{CH}_2\text{CHO}$ radical.

We have probed the performance of the high-level CCSD(T) procedure by comparing several calculated bond dissociation energies (BDEs) relevant to reactions 1 and 6–9, and the corresponding reaction energies, with experimental values (Table 2). It can be seen that UCCSD(T) and URCCSD(T) give BDEs and reaction energies ($\Delta E_{\text{r}}$) that are very close to one another. In general, the use of the aug-cc-pVQZ basis set yields BDEs that are in good accord with experimental values, with an MAD of $1.7\ \text{kJ mol}^{-1}$. The agreement is somewhat less good when the smaller aug-cc-pVTZ basis set is used, with an MAD for the BDEs of $7.1\ \text{kJ mol}^{-1}$. For the energies of reactions 1 and 6–9, better results are obtained with both basis sets, with MADs of 3.2 and $1.0\ \text{kJ mol}^{-1}$, respectively, for the TZ and QZ basis sets. On the basis of these results, we have chosen URCCSD(T)/aug-cc-pVQZ as the benchmark method. While the aim of the present study was assessment of theoretical procedures, we provide relevant URCCSD(T)/aug-cc-pVQZ barriers and reaction energies in Table 3.

We have surveyed a variety of DFT- and wavefunction-based methods and compared the calculated vibrationless barriers and reaction energies with the benchmark UR-CCSD(T)/aug-cc-pVQZ values. The MADs for the barriers and reaction energies are presented in Tables 4 and 5, respectively. First, we examine the performance of the various methods in predicting barriers. It is apparent that with the exception of B-LYP, all DFT procedures examined have MADs that are less than $10\ \text{kJ mol}^{-1}$ for at least some of the basis sets. Among these, M06-2X is the only one that achieves such accuracy in combination with *all* the basis sets examined. We also note that LC-B-LYP and BMK give MADs that are less than $10\ \text{kJ mol}^{-1}$ for all basis sets other than 6-31G(d), while CAM-B3-LYP and M05-2X have MADs that are less than $10\ \text{kJ mol}^{-1}$ except with the aug-cc-pVDZ basis set. When we further examine the basis set effect among the DFT methods, we do not find consistent improvement as the basis set size increases. In particular, for M06-L, B3-LYP, $\omega$B97X-D, M05, and M06, the best results are actually obtained with the smallest 6-31G(d) basis set.

![](./images/811657663921258497_4.jpg)

**Table 2** Comparison of calculated and experimental bond dissociation energies (BDEs), and the energies ($\Delta E_{\text{r}}$) of related hydrogen-atom-transfer reactions 1 and 6–9, as well as the corresponding mean absolute deviations (MADs) (vibrationless, kJ mol$^{-1}$)

|            | UCCSD(T) AVTZ$^{\text{a}}$ | URCCSD(T) AVTZ$^{\text{a}}$ | UCCSD(T) AVQZ$^{\text{a}}$ | URCCSD(T) AVQZ$^{\text{a}}$ | Expt$^{\text{b}}$ |
|------------|-----------------------------|------------------------------|-----------------------------|------------------------------|-------------------|
| $\text{CH}_3$–H | 465.9                       | 465.9                        | 468.5                       | 468.5                        | 470.4             |
| Cl–H       | 439.0                       | 439.0                        | 444.9                       | 445.0                        | 445.3             |
| F–H        | 582.6                       | 582.7                        | 589.5                       | 589.6                        | 591.2             |
| Br–H       | 384.1                       | 384.3                        | 392.1$^{\text{c}}$          | 392.1$^{\text{c}}$           | 392.8             |
| HO–H       | 516.5                       | 516.6                        | 522.5                       | 522.6                        | 525.4             |
| HOO–H      | 387.0                       | 387.0                        | 390.2                       | 390.2                        | 393.1             |
| MAD        | 7.2                         | 7.1                          | 1.7                         | 1.7                          |                   |
| $\Delta E_{\text{r}}$ 1 | 26.9                   | 26.9                        | 23.6                         | 23.5                        | 25.0              |
| $\Delta E_{\text{r}}$ 6 | $-$116.7               | $-$116.8                    | $-$121.0                    | $-$121.1                     | $-$120.8          |
| $\Delta E_{\text{r}}$ 7 | 81.8                   | 81.6                        | 76.4$^{\text{c}}$           | 76.5$^{\text{c}}$            | 77.6              |
| $\Delta E_{\text{r}}$ 8 | $-$50.6               | $-$50.7                    | $-$54.0                    | $-$54.1                     | $-$55.1           |
| $\Delta E_{\text{r}}$ 9 | 78.9                   | 78.9                        | 78.3                         | 78.3                        | 77.3              |
| MAD        | 3.3                         | 3.2                          | 1.0                         | 1.0                          |                   |

$^{\text{a}}$ $\text{AV}n\text{Z} = \text{aug-cc-pV}n\text{Z}$ ($n = \text{T, Q}$)
$^{\text{b}}$ Obtained from NIST Chemistry Webbook [58] and back-corrected to vibrationless values using zero-point vibrational energies and thermal corrections to enthalpies obtained from scaled [59] BH&H-LYP/6-31+G(d,p) frequencies
$^{\text{c}}$ The aug-cc-pwCVQZ basis set was used for Br

**Table 3** URCCSD(T)/aug-cc-pVQZ//BH&H-LYP/6-31+G(d,p) vibrationless and 0 K barriers ($E^{\ddagger}$) and reaction energies ($\Delta E_{\text{r}}$) for reactions 1 and 6–10 (kJ mol$^{-1}$)

<table>
  <thead>
    <tr>
      <th colspan="2">Reactants</th>
      <th colspan="2">Vibrationless</th>
      <th colspan="2">0 K</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>$E^{\ddagger}$</th>
      <th>$\Delta E_{\text{r}}$</th>
      <th>$E^{\ddagger}$</th>
      <th>$\Delta E_{\text{r}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\text{F}\bullet$</td>
      <td>$\text{CH}_4$</td>
      <td>0.3</td>
      <td>$-$121.1</td>
      <td>$-$4.8</td>
      <td>$-$135.4</td>
    </tr>
    <tr>
      <td>$\text{Cl}\bullet$</td>
      <td>$\text{CH}_4$</td>
      <td>29.7</td>
      <td>23.5</td>
      <td>12.9</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td>$\text{Br}\bullet^{\text{a}}$</td>
      <td>$\text{CH}_4$</td>
      <td>70.2</td>
      <td>76.5</td>
      <td>53.0</td>
      <td>53.5</td>
    </tr>
    <tr>
      <td>$\text{HO}\bullet$</td>
      <td>$\text{CH}_4$</td>
      <td>24.9</td>
      <td>$-$54.1</td>
      <td>18.4</td>
      <td>$-$59.3</td>
    </tr>
    <tr>
      <td>$\text{HOO}\bullet$</td>
      <td>$\text{CH}_4$</td>
      <td>112.3</td>
      <td>78.3</td>
      <td>103.4</td>
      <td>72.0</td>
    </tr>
    <tr>
      <td>$\text{Cl}\bullet$</td>
      <td>$\text{CH}_3\text{CHO}$</td>
      <td>21.7</td>
      <td>$-$18.1</td>
      <td>5.0</td>
      <td>$-$34.3</td>
    </tr>
  </tbody>
</table>

$^{\text{a}}$ The aug-cc-pwCVQZ basis set was used for Br

We now turn our attention to the two double-hybrid functionals B2-PLYP and B2K-PLYP, with both U and R formulations. They represent two “extremes” among the double hybrids that are based on B-LYP. Thus, B2-PLYP includes the least amount of ab initio components (53% HF and 27% MP2), while B2K-PLYP includes 72% HF and 42% MP2, which is the most among the B2x-PLYP family of double-hybrid procedures. We find that the performance of B2K-PLYP is rather sensitive to the size of the basis set, where small basis sets lead to fairly poor results. On the other hand, the performance of B2-PLYP appears to be somewhat less sensitive to basis set size.

This is consistent with the proportion of DFT and wavefunction contributions in these two double hybrids, such that B2K-PLYP behaves more like a wavefunction method, in which the use of an adequately sized basis set is critical, while the performance of B2-PLYP deteriorates less with decreasing basis set size, as is often the case with DFT procedures. As a result of these basis set considerations, we find that when used in combination with small basis sets, B2-PLYP provides somewhat more reliable barriers. However, as the size of the basis set increases, B2K-PLYP eventually outperforms B2-PLYP.

The UB2-PLYP-09 method contains 62% HF and 35% MP2, while ROB2-PLYP contains 59% HF and 28% MP2. Thus, they lie between B2-PLYP and B2K-PLYP in terms of wavefunction contribution to energies. We find that for the most part, their performance also lies between the two extremes. We also note that, in general, the U and R formulations yield comparable results for these double-hybrid procedures. The DSD-B-LYP-D3 procedure is a new type of double-hybrid functional that makes use of SCS-MP2 [55]

![](./images/811657663921258497_5.jpg)

<table><caption>Table 4 Mean absolute deviations from URCCSD(T)/AVQZᵃ benchmark values for vibrationless barriers (kJ mol⁻¹) for reactions 1 and 6–10ᵇ</caption>
<thead>
<tr>
<th></th>
<th>B1</th>
<th>B2</th>
<th>B3</th>
<th>B4</th>
<th>LXP</th>
<th>VDZ</th>
<th>VTZ</th>
<th>VQZ</th>
<th>AVDZ</th>
<th>AVTZ</th>
<th>AVQZ</th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="12">Pure DFT methods</th>
</tr>
<tr>
<th>B-LYP</th>
<td>20.4</td>
<td>30.0</td>
<td>29.5</td>
<td>31.0</td>
<td>30.4</td>
<td>31.5</td>
<td>28.6</td>
<td>29.5</td>
<td>35.2</td>
<td>30.1</td>
<td>29.9</td>
</tr>
<tr>
<th>M06-L</th>
<td>9.5</td>
<td>16.7</td>
<td>16.4</td>
<td>17.4</td>
<td>16.5</td>
<td>16.9</td>
<td>15.9</td>
<td>14.5</td>
<td>21.3</td>
<td>16.8</td>
<td>15.8</td>
</tr>
<tr>
<th colspan="12">Hybrid DFT methods</th>
</tr>
<tr>
<th>B3-LYP</th>
<td>7.2</td>
<td>13.1</td>
<td>13.3</td>
<td>14.8</td>
<td>14.1</td>
<td>14.4</td>
<td>12.5</td>
<td>13.2</td>
<td>18.4</td>
<td>13.8</td>
<td>13.6</td>
</tr>
<tr>
<th>LC-B-LYP</th>
<td>12.9</td>
<td>9.5</td>
<td>8.4</td>
<td>8.0</td>
<td>8.2</td>
<td>8.2</td>
<td>8.4</td>
<td>8.4</td>
<td>9.0</td>
<td>8.3</td>
<td>8.3</td>
</tr>
<tr>
<th>CAM-B3-LYP</th>
<td>8.8</td>
<td>7.8</td>
<td>8.0</td>
<td>9.3</td>
<td>8.5</td>
<td>8.5</td>
<td>7.5</td>
<td>8.0</td>
<td>12.1</td>
<td>8.3</td>
<td>8.1</td>
</tr>
<tr>
<th>ωB97X-D</th>
<td>5.7</td>
<td>8.8</td>
<td>9.5</td>
<td>11.1</td>
<td>10.4</td>
<td>9.1</td>
<td>8.2</td>
<td>8.6</td>
<td>14.3</td>
<td>9.6</td>
<td>9.0</td>
</tr>
<tr>
<th>BH&amp;H-LYP</th>
<td>21.3</td>
<td>11.8</td>
<td>11.3</td>
<td>9.8</td>
<td>10.7</td>
<td>10.5</td>
<td>11.8</td>
<td>11.3</td>
<td>6.9</td>
<td>10.9</td>
<td>11.1</td>
</tr>
<tr>
<th>BMK</th>
<td>10.1</td>
<td>4.6</td>
<td>7.7</td>
<td>8.7</td>
<td>8.0</td>
<td>6.9</td>
<td>7.1</td>
<td>7.1</td>
<td>8.4</td>
<td>7.8</td>
<td>7.5</td>
</tr>
<tr>
<th>M05</th>
<td>8.7</td>
<td>10.0</td>
<td>13.0</td>
<td>13.6</td>
<td>13.3</td>
<td>11.3</td>
<td>10.0</td>
<td>11.0</td>
<td>14.9</td>
<td>11.0</td>
<td>11.3</td>
</tr>
<tr>
<th>M05-2X</th>
<td>6.0</td>
<td>5.1</td>
<td>4.6</td>
<td>6.6</td>
<td>6.2</td>
<td>4.8</td>
<td>5.3</td>
<td>5.5</td>
<td>10.1</td>
<td>6.9</td>
<td>6.0</td>
</tr>
<tr>
<th>M06</th>
<td>7.3</td>
<td>9.0</td>
<td>10.8</td>
<td>12.2</td>
<td>11.5</td>
<td>11.7</td>
<td>9.3</td>
<td>8.6</td>
<td>14.5</td>
<td>10.3</td>
<td>9.3</td>
</tr>
<tr>
<th>M06-2X</th>
<td>9.0</td>
<td>3.1</td>
<td>5.0</td>
<td>6.3</td>
<td>5.5</td>
<td>4.8</td>
<td>5.0</td>
<td>4.8</td>
<td>7.1</td>
<td>5.8</td>
<td>5.1</td>
</tr>
<tr>
<th colspan="12">Double-hybrid DFT methods</th>
</tr>
<tr>
<th>UB2-PLYP</th>
<td>13.4</td>
<td>6.0</td>
<td>4.5</td>
<td>6.0</td>
<td>5.3</td>
<td>3.0</td>
<td>3.9</td>
<td>4.9</td>
<td>7.9</td>
<td>5.8</td>
<td>5.7</td>
</tr>
<tr>
<th>UB2K-PLYP</th>
<td>23.6</td>
<td>11.1</td>
<td>5.6</td>
<td>3.4</td>
<td>4.1</td>
<td>10.7</td>
<td>6.1</td>
<td>3.9</td>
<td>1.4</td>
<td>2.1</td>
<td>2.2</td>
</tr>
<tr>
<th>RB2-PLYP</th>
<td>15.2</td>
<td>6.3</td>
<td>3.7</td>
<td>5.4</td>
<td>4.6</td>
<td>3.5</td>
<td>3.3</td>
<td>4.3</td>
<td>6.3</td>
<td>5.3</td>
<td>6.0</td>
</tr>
<tr>
<th>RB2K-PLYP</th>
<td>25.7</td>
<td>12.8</td>
<td>6.7</td>
<td>4.1</td>
<td>5.2</td>
<td>12.7</td>
<td>7.0</td>
<td>4.6</td>
<td>3.3</td>
<td>3.3</td>
<td>2.5</td>
</tr>
<tr>
<th>UB2-PLYP-09</th>
<td>17.7</td>
<td>6.4</td>
<td>2.6</td>
<td>3.3</td>
<td>2.8</td>
<td>5.0</td>
<td>2.5</td>
<td>2.3</td>
<td>4.5</td>
<td>3.2</td>
<td>3.3</td>
</tr>
<tr>
<th>ROB2-PLYP</th>
<td>20.6</td>
<td>8.3</td>
<td>3.5</td>
<td>2.0</td>
<td>2.8</td>
<td>8.1</td>
<td>4.0</td>
<td>2.2</td>
<td>1.6</td>
<td>1.6</td>
<td>3.4</td>
</tr>
<tr>
<th>DSD-B-LYP-D3</th>
<td>20.3</td>
<td>7.6</td>
<td>2.2</td>
<td>2.0</td>
<td>1.7</td>
<td>7.4</td>
<td>3.0</td>
<td>1.6</td>
<td>3.2</td>
<td>2.5</td>
<td>2.4</td>
</tr>
<tr>
<th colspan="12">Unrestricted wavefunction methods</th>
</tr>
<tr>
<th>UHF</th>
<td>71.7</td>
<td>62.1</td>
<td>61.9</td>
<td>60.6</td>
<td>61.8</td>
<td>61.5</td>
<td>62.3</td>
<td>62.4</td>
<td>57.9</td>
<td>61.9</td>
<td>62.3</td>
</tr>
<tr>
<th>UMP2</th>
<td>36.7</td>
<td>23.2</td>
<td>14.0</td>
<td>11.8</td>
<td>12.4</td>
<td>21.5</td>
<td>13.7</td>
<td>10.6</td>
<td>10.6</td>
<td>10.0</td>
<td>9.5</td>
</tr>
<tr>
<th>UMP3</th>
<td>41.6</td>
<td>28.7</td>
<td>20.5</td>
<td>18.3</td>
<td>19.1</td>
<td>27.6</td>
<td>19.7</td>
<td>16.0</td>
<td>13.6</td>
<td>14.4</td>
<td>13.6</td>
</tr>
<tr>
<th>UMP4</th>
<td>38.0</td>
<td>23.0</td>
<td>13.3</td>
<td>10.5</td>
<td>11.3</td>
<td>22.8</td>
<td>12.5</td>
<td>8.6</td>
<td>8.9</td>
<td>8.1</td>
<td>6.1</td>
</tr>
<tr>
<th>UCCSD</th>
<td>36.8</td>
<td>23.1</td>
<td>16.6</td>
<td>14.3</td>
<td>15.3</td>
<td>22.9</td>
<td>16.2</td>
<td>12.7</td>
<td>8.6</td>
<td>10.8</td>
<td>10.0</td>
</tr>
<tr>
<th>UCCSD(T)</th>
<td>32.8</td>
<td>17.7</td>
<td>9.1</td>
<td>6.0</td>
<td>6.9</td>
<td>17.9</td>
<td>8.3</td>
<td>3.7</td>
<td>2.5</td>
<td>2.2</td>
<td>0.5</td>
</tr>
<tr>
<th colspan="12">Restricted-open-shell wavefunction methods</th>
</tr>
<tr>
<th>RHF</th>
<td>86.9</td>
<td>76.6</td>
<td>74.6</td>
<td>73.2</td>
<td>74.1</td>
<td>76.1</td>
<td>75.0</td>
<td>74.7</td>
<td>71.6</td>
<td>74.2</td>
<td>74.6</td>
</tr>
<tr>
<th>RMP2</th>
<td>28.8</td>
<td>19.1</td>
<td>9.6</td>
<td>9.0</td>
<td>8.9</td>
<td>15.6</td>
<td>9.3</td>
<td>9.0</td>
<td>9.2</td>
<td>9.7</td>
<td>9.7</td>
</tr>
<tr>
<th>RMP3</th>
<td>39.8</td>
<td>27.4</td>
<td>19.2</td>
<td>17.0</td>
<td>17.9</td>
<td>26.2</td>
<td>18.5</td>
<td>14.6</td>
<td>12.2</td>
<td>13.2</td>
<td>12.3</td>
</tr>
<tr>
<th>RMP4</th>
<td>34.7</td>
<td>19.4</td>
<td>10.2</td>
<td>7.7</td>
<td>8.5</td>
<td>19.7</td>
<td>9.6</td>
<td>5.6</td>
<td>6.2</td>
<td>5.4</td>
<td>4.0</td>
</tr>
<tr>
<th>URCCSD</th>
<td>37.3</td>
<td>23.7</td>
<td>17.1</td>
<td>14.8</td>
<td>15.8</td>
<td>23.4</td>
<td>16.7</td>
<td>13.1</td>
<td>9.1</td>
<td>11.3</td>
<td>10.5</td>
</tr>
<tr>
<th>URCCSD(T)</th>
<td>32.5</td>
<td>17.4</td>
<td>8.6</td>
<td>5.5</td>
<td>6.4</td>
<td>17.6</td>
<td>7.8</td>
<td>3.3</td>
<td>2.3</td>
<td>1.8</td>
<td>0.0</td>
</tr>
</tbody>
</table>

ⁱ The aug-cc-pwCVQZ basis set was employed for bromine
ⁱ B1 = 6-31G(d), B2 = 6-31+G(d,p), B3 = 6-311+G(2df,p), B4 = 6-311+G(3df,2p), LXP = G3LargeXP, VnZ = cc-pVnZ, AVnZ = aug-cc-pVnZ (n = D, T, Q)

and includes the D3 [56] empirical dispersion correction. It has been shown to perform well for a wide range of systems [53]. In the present study, we also find it to perform well for the barriers for hydrogen-atom-abstraction reactions.

For the wavefunction methods, we find a surprisingly good performance by MP2, which somewhat fortuitously produces MADs similar to those for the much more costly MP4 or CCSD. At the intermediate MP3 level, the MADs are larger than for MP2, MP4, and CCSD. We also note that CCSD yields somewhat larger MADs than MP4 and MP2. For all wavefunction methods examined, there is a consistent basis set effect, in which a larger basis set generally leads to a lower MAD. We find that R performs slightly better than U. We also note that for URCCSD(T), there is a difference of 1.8 kJ mol⁻¹ between the MAD for aug-cc-pVTZ and that for aug-cc-pVQZ.

![](./images/811657663921258497_6.jpg)

<table>
 <thead>
  <tr>
   <th>
    Table 5 Mean absolute deviations from URCCSD(T)/AVQZa benchmark values for vibrationless reaction energies (kJ mol-1) for reactions 1 and 6–10b
   </th>
   <th>
    B1
   </th>
   <th>
    B2
   </th>
   <th>
    B3
   </th>
   <th>
    B4
   </th>
   <th>
    LXP
   </th>
   <th>
    VDZ
   </th>
   <th>
    VTZ
   </th>
   <th>
    VQZ
   </th>
   <th>
    AVDZ
   </th>
   <th>
    AVTZ
   </th>
   <th>
    AVQZ
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    Pure DFT methods
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    B-LYP
   </th>
   <td>
    31.2
   </td>
   <td>
    7.4
   </td>
   <td>
    7.0
   </td>
   <td>
    7.4
   </td>
   <td>
    7.0
   </td>
   <td>
    18.4
   </td>
   <td>
    8.7
   </td>
   <td>
    7.1
   </td>
   <td>
    6.8
   </td>
   <td>
    6.5
   </td>
   <td>
    6.8
   </td>
  </tr>
  <tr>
   <th>
    M06-L
   </th>
   <td>
    31.5
   </td>
   <td>
    14.3
   </td>
   <td>
    15.1
   </td>
   <td>
    15.0
   </td>
   <td>
    14.2
   </td>
   <td>
    23.5
   </td>
   <td>
    17.2
   </td>
   <td>
    17.6
   </td>
   <td>
    13.7
   </td>
   <td>
    15.0
   </td>
   <td>
    17.0
   </td>
  </tr>
  <tr>
   <th>
    Hybrid DFT methods
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    B3-LYP
   </th>
   <td>
    34.6
   </td>
   <td>
    9.9
   </td>
   <td>
    7.4
   </td>
   <td>
    5.7
   </td>
   <td>
    5.6
   </td>
   <td>
    19.7
   </td>
   <td>
    9.8
   </td>
   <td>
    7.1
   </td>
   <td>
    4.7
   </td>
   <td>
    5.7
   </td>
   <td>
    5.5
   </td>
  </tr>
  <tr>
   <th>
    LC-B-LYP
   </th>
   <td>
    33.9
   </td>
   <td>
    10.3
   </td>
   <td>
    7.8
   </td>
   <td>
    7.2
   </td>
   <td>
    7.6
   </td>
   <td>
    18.0
   </td>
   <td>
    7.0
   </td>
   <td>
    7.6
   </td>
   <td>
    8.0
   </td>
   <td>
    7.8
   </td>
   <td>
    8.0
   </td>
  </tr>
  <tr>
   <th>
    CAM-B3-LYP
   </th>
   <td>
    35.7
   </td>
   <td>
    10.7
   </td>
   <td>
    6.4
   </td>
   <td>
    4.7
   </td>
   <td>
    4.6
   </td>
   <td>
    20.3
   </td>
   <td>
    8.8
   </td>
   <td>
    6.0
   </td>
   <td>
    3.6
   </td>
   <td>
    4.7
   </td>
   <td>
    4.5
   </td>
  </tr>
  <tr>
   <th>
    $\omega$B97X-D
   </th>
   <td>
    34.8
   </td>
   <td>
    0.1
   </td>
   <td>
    8.4
   </td>
   <td>
    7.2
   </td>
   <td>
    6.8
   </td>
   <td>
    20.5
   </td>
   <td>
    11.1
   </td>
   <td>
    8.8
   </td>
   <td>
    6.1
   </td>
   <td>
    7.7
   </td>
   <td>
    7.5
   </td>
  </tr>
  <tr>
   <th>
    BH&amp;H-LYP
   </th>
   <td>
    42.1
   </td>
   <td>
    17.9
   </td>
   <td>
    14.1
   </td>
   <td>
    11.6
   </td>
   <td>
    11.5
   </td>
   <td>
    26.3
   </td>
   <td>
    15.9
   </td>
   <td>
    13.1
   </td>
   <td>
    11.6
   </td>
   <td>
    12.2
   </td>
   <td>
    11.7
   </td>
  </tr>
  <tr>
   <th>
    BMK
   </th>
   <td>
    38.8
   </td>
   <td>
    15.3
   </td>
   <td>
    10.9
   </td>
   <td>
    8.8
   </td>
   <td>
    8.7
   </td>
   <td>
    23.9
   </td>
   <td>
    12.7
   </td>
   <td>
    11.8
   </td>
   <td>
    8.4
   </td>
   <td>
    9.6
   </td>
   <td>
    10.6
   </td>
  </tr>
  <tr>
   <th>
    M05
   </th>
   <td>
    30.5
   </td>
   <td>
    7.8
   </td>
   <td>
    8.9
   </td>
   <td>
    10.7
   </td>
   <td>
    10.6
   </td>
   <td>
    21.5
   </td>
   <td>
    11.7
   </td>
   <td>
    10.2
   </td>
   <td>
    8.7
   </td>
   <td>
    8.6
   </td>
   <td>
    9.3
   </td>
  </tr>
  <tr>
   <th>
    M05-2X
   </th>
   <td>
    33.1
   </td>
   <td>
    8.5
   </td>
   <td>
    6.5
   </td>
   <td>
    4.3
   </td>
   <td>
    4.2
   </td>
   <td>
    18.8
   </td>
   <td>
    6.2
   </td>
   <td>
    5.1
   </td>
   <td>
    3.4
   </td>
   <td>
    3.3
   </td>
   <td>
    4.0
   </td>
  </tr>
  <tr>
   <th>
    M06
   </th>
   <td>
    29.0
   </td>
   <td>
    6.8
   </td>
   <td>
    5.5
   </td>
   <td>
    6.0
   </td>
   <td>
    5.7
   </td>
   <td>
    15.5
   </td>
   <td>
    8.6
   </td>
   <td>
    7.1
   </td>
   <td>
    4.3
   </td>
   <td>
    5.1
   </td>
   <td>
    5.7
   </td>
  </tr>
  <tr>
   <th>
    M06-2X
   </th>
   <td>
    35.6
   </td>
   <td>
    11.7
   </td>
   <td>
    7.5
   </td>
   <td>
    5.8
   </td>
   <td>
    5.8
   </td>
   <td>
    19.9
   </td>
   <td>
    8.5
   </td>
   <td>
    7.1
   </td>
   <td>
    4.4
   </td>
   <td>
    5.1
   </td>
   <td>
    5.8
   </td>
  </tr>
  <tr>
   <th>
    Double-hybrid DFT methods
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    UB2-PLYP
   </th>
   <td>
    37.1
   </td>
   <td>
    11.8
   </td>
   <td>
    6.7
   </td>
   <td>
    3.3
   </td>
   <td>
    3.5
   </td>
   <td>
    21.9
   </td>
   <td>
    8.7
   </td>
   <td>
    4.5
   </td>
   <td>
    3.7
   </td>
   <td>
    3.4
   </td>
   <td>
    2.6
   </td>
  </tr>
  <tr>
   <th>
    UB2K-PLYP
   </th>
   <td>
    38.4
   </td>
   <td>
    13.5
   </td>
   <td>
    7.8
   </td>
   <td>
    4.3
   </td>
   <td>
    4.6
   </td>
   <td>
    23.1
   </td>
   <td>
    9.3
   </td>
   <td>
    5.0
   </td>
   <td>
    5.1
   </td>
   <td>
    3.5
   </td>
   <td>
    2.4
   </td>
  </tr>
  <tr>
   <th>
    RB2-PLYP
   </th>
   <td>
    37.5
   </td>
   <td>
    11.6
   </td>
   <td>
    5.6
   </td>
   <td>
    2.0
   </td>
   <td>
    2.3
   </td>
   <td>
    21.9
   </td>
   <td>
    7.7
   </td>
   <td>
    3.3
   </td>
   <td>
    3.3
   </td>
   <td>
    2.3
   </td>
   <td>
    1.8
   </td>
  </tr>
  <tr>
   <th>
    RB2K-PLYP
   </th>
   <td>
    38.0
   </td>
   <td>
    12.4
   </td>
   <td>
    6.3
   </td>
   <td>
    3.3
   </td>
   <td>
    3.6
   </td>
   <td>
    22.3
   </td>
   <td>
    7.4
   </td>
   <td>
    3.9
   </td>
   <td>
    5.6
   </td>
   <td>
    3.5
   </td>
   <td>
    2.0
   </td>
  </tr>
  <tr>
   <th>
    UB2-PLYP-09
   </th>
   <td>
    37.5
   </td>
   <td>
    12.3
   </td>
   <td>
    6.9
   </td>
   <td>
    3.3
   </td>
   <td>
    3.5
   </td>
   <td>
    22.2
   </td>
   <td>
    8.6
   </td>
   <td>
    4.3
   </td>
   <td>
    4.0
   </td>
   <td>
    2.9
   </td>
   <td>
    2.0
   </td>
  </tr>
  <tr>
   <th>
    ROB2-PLYP
   </th>
   <td>
    38.9
   </td>
   <td>
    13.1
   </td>
   <td>
    6.9
   </td>
   <td>
    3.3
   </td>
   <td>
    3.6
   </td>
   <td>
    23.1
   </td>
   <td>
    8.7
   </td>
   <td>
    4.4
   </td>
   <td>
    4.8
   </td>
   <td>
    3.2
   </td>
   <td>
    3.1
   </td>
  </tr>
  <tr>
   <th>
    DSD-B-LYP-D3
   </th>
   <td>
    37.9
   </td>
   <td>
    12.8
   </td>
   <td>
    7.1
   </td>
   <td>
    3.6
   </td>
   <td>
    3.9
   </td>
   <td>
    22.7
   </td>
   <td>
    8.7
   </td>
   <td>
    4.2
   </td>
   <td>
    4.5
   </td>
   <td>
    2.6
   </td>
   <td>
    2.3
   </td>
  </tr>
  <tr>
   <th>
    Unrestricted wavefunction methods
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    UHF
   </th>
   <td>
    52.0
   </td>
   <td>
    29.1
   </td>
   <td>
    27.4
   </td>
   <td>
    25.1
   </td>
   <td>
    25.6
   </td>
   <td>
    35.9
   </td>
   <td>
    28.3
   </td>
   <td>
    26.5
   </td>
   <td>
    25.1
   </td>
   <td>
    26.3
   </td>
   <td>
    25.8
   </td>
  </tr>
  <tr>
   <th>
    UMP2
   </th>
   <td>
    35.0
   </td>
   <td>
    18.6
   </td>
   <td>
    15.7
   </td>
   <td>
    16.4
   </td>
   <td>
    16.7
   </td>
   <td>
    20.3
   </td>
   <td>
    13.5
   </td>
   <td>
    15.9
   </td>
   <td>
    15.7
   </td>
   <td>
    16.2
   </td>
   <td>
    17.1
   </td>
  </tr>
  <tr>
   <th>
    UMP3
   </th>
   <td>
    37.9
   </td>
   <td>
    19.5
   </td>
   <td>
    13.6
   </td>
   <td>
    10.7
   </td>
   <td>
    11.1
   </td>
   <td>
    24.8
   </td>
   <td>
    13.3
   </td>
   <td>
    9.0
   </td>
   <td>
    11.9
   </td>
   <td>
    10.1
   </td>
   <td>
    7.8
   </td>
  </tr>
  <tr>
   <th>
    UMP4
   </th>
   <td>
    41.5
   </td>
   <td>
    18.2
   </td>
   <td>
    12.2
   </td>
   <td>
    8.7
   </td>
   <td>
    9.1
   </td>
   <td>
    26.8
   </td>
   <td>
    11.7
   </td>
   <td>
    6.9
   </td>
   <td>
    10.0
   </td>
   <td>
    7.7
   </td>
   <td>
    6.6
   </td>
  </tr>
  <tr>
   <th>
    UCCSD
   </th>
   <td>
    36.9
   </td>
   <td>
    14.7
   </td>
   <td>
    10.6
   </td>
   <td>
    7.2
   </td>
   <td>
    7.7
   </td>
   <td>
    23.0
   </td>
   <td>
    10.0
   </td>
   <td>
    4.9
   </td>
   <td>
    6.8
   </td>
   <td>
    5.7
   </td>
   <td>
    2.7
   </td>
  </tr>
  <tr>
   <th>
    UCCSD(T)
   </th>
   <td>
    37.6
   </td>
   <td>
    14.7
   </td>
   <td>
    9.7
   </td>
   <td>
    5.6
   </td>
   <td>
    6.1
   </td>
   <td>
    23.3
   </td>
   <td>
    8.7
   </td>
   <td>
    3.1
   </td>
   <td>
    5.6
   </td>
   <td>
    3.7
   </td>
   <td>
    0.3
   </td>
  </tr>
  <tr>
   <th>
    Restricted-open-shell wavefunction methods
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    RHF
   </th>
   <td>
    57.8
   </td>
   <td>
    33.6
   </td>
   <td>
    29.6
   </td>
   <td>
    27.0
   </td>
   <td>
    27.3
   </td>
   <td>
    41.3
   </td>
   <td>
    30.8
   </td>
   <td>
    28.5
   </td>
   <td>
    28.7
   </td>
   <td>
    28.1
   </td>
   <td>
    27.6
   </td>
  </tr>
  <tr>
   <th>
    RMP2
   </th>
   <td>
    30.6
   </td>
   <td>
    13.6
   </td>
   <td>
    10.8
   </td>
   <td>
    11.4
   </td>
   <td>
    11.8
   </td>
   <td>
    15.8
   </td>
   <td>
    8.5
   </td>
   <td>
    10.3
   </td>
   <td>
    11.0
   </td>
   <td>
    10.7
   </td>
   <td>
    11.1
   </td>
  </tr>
  <tr>
   <th>
    RMP3
   </th>
   <td>
    35.8
   </td>
   <td>
    18.1
   </td>
   <td>
    12.4
   </td>
   <td>
    9.5
   </td>
   <td>
    9.9
   </td>
   <td>
    22.7
   </td>
   <td>
    12.1
   </td>
   <td>
    7.7
   </td>
   <td>
    10.5
   </td>
   <td>
    8.8
   </td>
   <td>
    6.3
   </td>
  </tr>
  <tr>
   <th>
    RMP4
   </th>
   <td>
    37.7
   </td>
   <td>
    14.6
   </td>
   <td>
    8.6
   </td>
   <td>
    5.1
   </td>
   <td>
    5.6
   </td>
   <td>
    23.1
   </td>
   <td>
    8.0
   </td>
   <td>
    3.1
   </td>
   <td>
    6.4
   </td>
   <td>
    4.1
   </td>
   <td>
    3.3
   </td>
  </tr>
  <tr>
   <th>
    URCCSD
   </th>
   <td>
    37.1
   </td>
   <td>
    15.0
   </td>
   <td>
    10.7
   </td>
   <td>
    7.3
   </td>
   <td>
    7.8
   </td>
   <td>
    23.2
   </td>
   <td>
    10.1
   </td>
   <td>
    5.0
   </td>
   <td>
    7.1
   </td>
   <td>
    5.9
   </td>
   <td>
    3.0
   </td>
  </tr>
  <tr>
   <th>
    URCCSD(T)
   </th>
   <td>
    37.5
   </td>
   <td>
    14.6
   </td>
   <td>
    9.4
   </td>
   <td>
    5.4
   </td>
   <td>
    5.9
   </td>
   <td>
    23.1
   </td>
   <td>
    8.4
   </td>
   <td>
    2.8
   </td>
   <td>
    5.4
   </td>
   <td>
    3.5
   </td>
   <td>
    0.0
   </td>
  </tr>
 </tbody>
</table>

aThe aug-cc-pwCVQZ basis set was employed for bromine
bB1 = 6-31G(d), B2 = 6-31+G(d,p), B3 = 6-311+G(2df,p), B4 = 6-311+G(3df,2p), LXP = G3LargeXP, VnZ = cc-pVnZ, AVnZ = aug-cc-pVnZ ($n$ = D, T, Q)

Turning our attention to the performance of the various methods in calculating reaction energies (Table 5), we find that the use of the 6-31G(d) basis set leads to substantial deviations from the URCCSD(T)/aug-cc-pVQZ values, with MADs in excess of 30 kJ mol-1 for all methods. In addition, the use of the cc-pVDZ basis set gives double-digit deviations for all methods, while calculations using 6-31+G(d,p) also give substantial MADs. When an appropriate basis set is used, most DFT procedures give MADs that are smaller than 10 kJ mol-1. Two notable exceptions are the M06-L and the BH&H-LYP functionals, which substantially overestimate the reaction energies. Thus, while BH&H-LYP provides fair estimations of the geometries of the transition structures, it does not give a good account for the reaction energies. On the basis of the performance for reaction energies as well as that for barriers, we find M05-2X to be an adequately reliable

![](./images/811657663921258497_7.jpg)

hybrid functional for the study of hydrogen-abstraction reactions.

The UB2-PLYP, RB2-PLYP, UB2K-PLYP, RB2K-PLYP, UB2-PLYP-09, ROB2-PLYP, and DSD-B-LYP-D3 double-hybrid functionals all perform comparably for reaction energies. In this case, a systematic improvement with increasing basis set size is observed for all methods. As is the case for the calculated barriers, we find only minor differences when comparing the performance of U and R formalisms. Taking the observations for both the barriers and reaction energies into account, we deem the use of UB2K-PLYP, RB2K-PLYP, UB2-PLYP-09, ROB2-PLYP, and DSD-B-LYP-D3 in combination with an augmented triple-zeta-quality basis set an appropriate methodology for studying the energies of these types of hydrogen-abstraction reactions.

For the wavefunction methods, MP2 is found to be less good for reaction energies than for barriers. It also displays a non-monotonic basis set effect. For the MP series, when used in combination with reasonably sized basis sets, there is generally a consistent improvement in the performance with increasing electron correlation, with the MADs decreasing in the order MP2 > MP3 > MP4. We find that URCCSD outperforms UMP4 but URCCSD gives somewhat larger MADs than RMP4.

It is noteworthy that, in general, a consistent basis set effect is found in calculating reaction energies for the correlation methods beyond MP2. We note that aug-cc-pVDZ outperforms cc-pVTZ and that aug-cc-pVTZ yields MADs comparable to cc-pVQZ. Thus, it appears that the inclusion of diffuse functions is required to obtain reliable energies for these reactions. We also note that there is a $5.4\ \text{kJ mol}^{-1}$ difference between the calculated reaction energies for URCCSD(T) with the aug-cc-pVDZ and the aug-cc-pVQZ basis sets, and a $3.5\ \text{kJ mol}^{-1}$ difference between the aug-cc-pVTZ and aug-cc-pVQZ values. This further highlights the importance of employing an adequately sized basis set for studying these reactions. Finally we note that as is the case for the barriers, there is only a minor difference between reaction energies obtained with U and R formalisms for highly correlated procedures.

### 3.3 The reaction of $\text{CH}_3\text{CHO}$

The reaction of $\text{Cl}\bullet$ with $\text{CH}_3\text{CHO}$ to give $\text{ClH}$ and $\bullet\text{CH}_2\text{CHO}$ (reaction 10) has been previously identified to be a challenging case for theoretical methods due to high spin contamination in the transition structure and in the product radical [22]. Indeed, the transition structure and the $\bullet\text{CH}_2\text{CHO}$ radical have the largest $\langle S^2\rangle$ values among all species examined, specifically 0.90 and 0.92, respectively, at the UHF/aug-cc-pVQZ level, which are substantially larger than the value of 0.75 for a pure doublet state. We have therefore examined in greater detail the barrier and reaction energy for this reaction obtained with unrestricted and restricted-open-shell procedures (Table 6).

<table>
<caption>Table 6 Differences in barriers and reaction energies calculated with unrestricted and restricted-open-shell methods for $\text{Cl}\bullet+\text{CH}_3\text{CHO}\rightarrow\text{ClH}+\bullet\text{CH}_2\text{CHO}$ (U–R, kJ mol⁻¹)</caption>
<thead>
<tr>
<th></th>
<th>B1</th>
<th>B2</th>
<th>B3</th>
<th>B4</th>
<th>LXP</th>
<th>VDZ</th>
<th>VTZ</th>
<th>VQZ</th>
<th>AVDZ</th>
<th>AVTZ</th>
<th>AVQZ</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="12"><em>Barrier</em></td>
</tr>
<tr>
<td>B2-PLYP</td>
<td>−3.1</td>
<td>−3.0</td>
<td>−2.8</td>
<td>−2.5</td>
<td>−2.7</td>
<td>−2.9</td>
<td>−2.0</td>
<td>−1.8</td>
<td>−2.7</td>
<td>−1.9</td>
<td>−1.9</td>
</tr>
<tr>
<td>B2K-PLYP</td>
<td>−2.7</td>
<td>−2.7</td>
<td>−3.3</td>
<td>−3.3</td>
<td>−3.8</td>
<td>−2.5</td>
<td>−1.6</td>
<td>−1.4</td>
<td>−3.7</td>
<td>−1.8</td>
<td>−1.7</td>
</tr>
<tr>
<td>HF</td>
<td>−27.8</td>
<td>−26.4</td>
<td>−23.0</td>
<td>−22.7</td>
<td>−22.2</td>
<td>−26.2</td>
<td>−23.0</td>
<td>−22.5</td>
<td>−24.4</td>
<td>−22.4</td>
<td>−22.4</td>
</tr>
<tr>
<td>MP2</td>
<td>32.4</td>
<td>31.0</td>
<td>31.5</td>
<td>31.4</td>
<td>31.4</td>
<td>31.4</td>
<td>31.8</td>
<td>32.5</td>
<td>30.2</td>
<td>31.8</td>
<td>32.6</td>
</tr>
<tr>
<td>MP3</td>
<td>14.9</td>
<td>13.4</td>
<td>12.4</td>
<td>12.2</td>
<td>12.2</td>
<td>13.9</td>
<td>12.5</td>
<td>12.8</td>
<td>12.7</td>
<td>12.4</td>
<td>12.9</td>
</tr>
<tr>
<td>MP4</td>
<td>18.9</td>
<td>17.9</td>
<td>17.8</td>
<td>18.2</td>
<td>18.2</td>
<td>18.2</td>
<td>18.1</td>
<td>19.2</td>
<td>17.6</td>
<td>18.8</td>
<td>19.2</td>
</tr>
<tr>
<td>CCSD</td>
<td>−0.8</td>
<td>−0.9</td>
<td>−0.8</td>
<td>−0.8</td>
<td>−0.7</td>
<td>−0.8</td>
<td>−0.8</td>
<td>−0.7</td>
<td>−0.9</td>
<td>−0.8</td>
<td>−0.7</td>
</tr>
<tr>
<td>CCSD(T)</td>
<td>1.0</td>
<td>1.0</td>
<td>1.4</td>
<td>1.4</td>
<td>1.5</td>
<td>1.1</td>
<td>1.4</td>
<td>1.5</td>
<td>1.1</td>
<td>1.5</td>
<td>2.1</td>
</tr>
<tr>
<td colspan="12"><em>Reaction energy</em></td>
</tr>
<tr>
<td>B2-PLYP</td>
<td>−1.6</td>
<td>−1.3</td>
<td>−0.6</td>
<td>−0.5</td>
<td>−0.5</td>
<td>−1.5</td>
<td>−0.3</td>
<td>−0.1</td>
<td>−1.3</td>
<td>0.7</td>
<td>0.9</td>
</tr>
<tr>
<td>B2K-PLYP</td>
<td>0.5</td>
<td>1.0</td>
<td>0.9</td>
<td>1.0</td>
<td>1.1</td>
<td>0.4</td>
<td>1.6</td>
<td>2.0</td>
<td>0.7</td>
<td>−1.3</td>
<td>−1.2</td>
</tr>
<tr>
<td>HF</td>
<td>−31.3</td>
<td>−29.0</td>
<td>−25.0</td>
<td>−24.8</td>
<td>−24.1</td>
<td>−31.3</td>
<td>−26.0</td>
<td>−24.9</td>
<td>−27.2</td>
<td>−24.6</td>
<td>−24.5</td>
</tr>
<tr>
<td>MP2</td>
<td>32.5</td>
<td>32.5</td>
<td>32.3</td>
<td>32.4</td>
<td>32.3</td>
<td>31.1</td>
<td>32.4</td>
<td>33.3</td>
<td>31.4</td>
<td>32.9</td>
<td>33.7</td>
</tr>
<tr>
<td>MP3</td>
<td>11.7</td>
<td>10.9</td>
<td>9.1</td>
<td>9.2</td>
<td>9.1</td>
<td>9.9</td>
<td>9.2</td>
<td>9.7</td>
<td>10.0</td>
<td>9.4</td>
<td>9.9</td>
</tr>
<tr>
<td>MP4</td>
<td>21.2</td>
<td>20.9</td>
<td>20.3</td>
<td>20.5</td>
<td>20.6</td>
<td>20.4</td>
<td>21.2</td>
<td>22.2</td>
<td>19.8</td>
<td>20.9</td>
<td>21.3</td>
</tr>
<tr>
<td>CCSD</td>
<td>−1.8</td>
<td>−1.7</td>
<td>−1.7</td>
<td>−1.7</td>
<td>−1.6</td>
<td>−2.0</td>
<td>−1.8</td>
<td>−1.7</td>
<td>−1.7</td>
<td>−1.7</td>
<td>−1.6</td>
</tr>
<tr>
<td>CCSD(T)</td>
<td>0.6</td>
<td>0.6</td>
<td>1.1</td>
<td>1.2</td>
<td>1.3</td>
<td>0.8</td>
<td>1.2</td>
<td>1.3</td>
<td>0.9</td>
<td>1.2</td>
<td>1.3</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="12">B1 = 6-31G(d), B2 = 6-31+G(d,p), B3 = 6-311+G(2df,p), B4 = 6-311+G(3df,2p), LXP = G3LargeXP, $VnZ = \text{cc-p}VnZ$, $AVnZ = \text{aug-cc-p}VnZ$ ($n$ = D, T, Q)</td>
</tr>
</tfoot>
</table>

![](./images/811657663921258497_8.jpg)

We can see that for the B2-PLYP and B2K-PLYP double-hybrid DFT procedures, there are only small dif- ferences in the barriers and reaction energies calculated with U and R formalisms. This is consistent with previous findings from Menon et al. for C–H BDEs, where there are only very minor U–R differences [57]. In contrast, the U–R values for wavefunction methods are substantial, until one reaches the CCSD or CCSD(T) levels. It is apparent that UHF gives lower barriers and reaction energies than RHF, as indicated by the negative U–R values. This is consistent with the larger variational freedom for UHF than for RHF. However, UMP2, UMP3, and UMP4 all yield barriers and reaction energies that are higher than those for the corre- sponding R counterparts, with MP2 giving the largest U–R values while MP3 yields the smallest. For the MP series, we find that R procedures give closer agreement with the benchmark URCCSD(T)/aug-cc-pVQZ values (supple- mentary material, Tables S2 and S3). When reaction 10 is excluded from our analysis, we find that U and R formal- isms perform very similarly to one another (supplementary material, Tables S4 and S5).

## 4 Concluding remarks

In this study, we have examined a number of hydrogen- abstraction reactions and assessed a number of DFT pro- cedures for their performance for geometry optimization and the performance of various DFT and wavefunction methods for calculating relative energies. The following major findings emerge from the present study:

- The BH&H-LYP and M05-2X procedures with the 6-31+G(d,p) basis set provide reasonable predictions for the geometries of the transition structures for hydrogen-atom abstraction by chlorine atom. They also yield reasonable imaginary frequencies when compared with the benchmark values, which is indicative of good descriptions of the potential energy surfaces near the saddle points.
- Despite being reasonably accurate in predicting geo- metries, the BH&H-LYP functional does not give rise to good barriers or reaction energies for the prototypical abstraction reactions examined. On the other hand, we find that the M05-2X functional, when combined with adequate basis sets, provides a reasonably accurate and cost-effective estimate of barriers and reaction energies.
- We find that double-hybrid functionals, when used with suitable basis sets, yield close agreement with the benchmark URCCSD(T) energies. The basis set effect for these functionals depends on the proportion of wavefunction methods in the procedures. At the extremes, B2K-PLYP, with a large proportion of HF exchange and MP2 correlation, displays a performance that is rather sensitive to basis set size, while the behavior of B2-PLYP is less dependent on the size of the basis set. We recommend the use of B2K-PLYP, UB2-PLYP-09, ROB2-PLYP, and DSD-B-LYP-D3 with an augmented triple-zeta quality basis set for studying these reactions.
- For wavefunction methods, we find that it is important to use the high-level CCSD(T) procedure in combina- tion with a diffuse-function-augmented basis set that is preferably of triple-zeta quality for an accurate account of both the barriers and the reaction energies for the hydrogen-abstraction reactions. We find that the use of either U or R reference wavefunctions yields very similar results, except in the case of abstraction from CH₃CHO, where high spin contamination in the transition structure and the radical product leads to substantially different UHF and UMP$n$ values com- pared with the R counterparts. In this case, the R formalism yields results that are in better agreement with the benchmark.

Acknowledgments We gratefully acknowledge the award of an Australian Professorial Fellowship and funding from the ARC Centre of Excellence for Free Radical Chemistry and Biotechnology (to L.R.) and generous allocations of computer time from the National Computational Infrastructure (NCI) National Facility and Intersect Australia Ltd.

## References

1. Smith MB, March J (2007) March’s advanced organic chemistry: reactions, mechanisms, and structure, 6th edn. Wiley, Hoboken
2. Rossberg M, Lendle W, Pfleiderer G, Tögel A, Dreher EL, Langer E, Rassaerts H, Kleinschmidt P, Strack H, Cook R, Beck U, Lipper KA, Torkelson TR, Löser E, Beutel KK, Mann T (2006) In: Ullmann’s encyclopedia of industrial chemistry. Wiley-VCH, Weinheim
3. Solomon S (1999) Rev Geophys 37:275
4. Wayne RP (2000) Chemistry of atmospheres, 3rd edn. Oxford University Press, Oxford
5. Bianco R, Hynes JT (2006) Acc Chem Res 39:159
6. Ravishankara AR (2009) Proc Natl Acad Sci USA 106:13639
7. Wallington TJ, Andino JM, Lorkovic IM, Kaiser EW, Marston G (1990) J Phys Chem 94:3644
8. Atkinson R, Baulch DL, Cox RA, Hampson RF Jr, Kerr JA, Troe J (1992) J Phys Chem Ref Data 21:1125
9. Kaiser EW, Wallington TJ (1996) J Phys Chem 100:4111
10. Sarzynski D, Sztuba B (2002) Int J Chem Kinet 34:651
11. Kaiser EW, Wallington TJ (2010) Int J Chem Kinet 42:113
12. Gola AA, Sarzynski D, Drys A, Jodkowski JT (2010) Chem Phys Lett 486:7
13. Hehre WJ, Radom L, Schleyer PvP, Pople JA (1986) Ab initio molecular orbital theory. Wiley, New York
14. Koch W, Holthausen MC (2001) A chemist’s guide to density functional theory, 2nd edn. Wiley, New York

![](./images/811657663921258497_9.jpg)

15. Jensen F (2007) Introduction to computational chemistry, 2nd edn. Wiley, Chichester

16. Yamataka H, Nagase S (1988) J Org Chem 53:3232

17. Dunning TH Jr (1989) J Chem Phys 90:1007

18. Kendall RA, Dunning TH Jr, Harrison RJ (1992) J Chem Phys 96:6796

19. Woon DE, Dunning TH Jr (1993) J Chem Phys 98:1358

20. Troya D, Weiss PJE (2006) J Chem Phys 124:074313

21. Czakó G, Shepler BC, Braams BJ, Bowman JM (2009) J Chem Phys 130:084301

22. Taylor MS, Ivanic SA, Wood GPF, Easton CJ, Bacskay GB, Radom L (2009) J Phys Chem A 113:11817

23. Lee C, Yang W, Parr RG (1988) Phys Rev B 37:785

24. Becke AD (1993) J Chem Phys 98:5648

25. Stephens PJ, Devlin FJ, Chabalowski CF, Frisch MJ (1994) J Phys Chem 98:11623

26. Boese AD, Martin JML (2004) J Chem Phys 121:3405

27. Martin JML, de Oliveira G (1999) J Chem Phys 111:1843

28. Martin JML (1999) Chem Phys Lett 310:271

29. Parthiban S, Martin JML (2001) J Chem Phys 114:6014

30. Henry DJ, Sullivan MB, Radom L (2003) J Chem Phys 118:4849

31. Curtiss LA, Redfern PC, Raghavachari K, Pople JA (2001) J Chem Phys 114:108

32. Grimme S (2006) J Chem Phys 124:034108

33. Frisch MJ, Trucks GW, Schlegel HB, Scuseria GE, Robb MA, Cheeseman JR, Scalmani G, Barone V, Mennucci B, Petersson GA, Nakatsuji H, Caricato M, Li X, Hratchian HP, Izmaylov AF, Bloino J, Zheng G, Sonnenberg JL, Hada M, Ehara M, Toyota K, Fukuda R, Hasegawa J, Ishida M, Nakajima T, Honda Y, Kitao O, Nakai H, Vreven T, Montgomery JA Jr, Peralta JE, Ogliaro F, Bearpark M, Heyd JJ, Brothers E, Kudin KN, Staroverov VN, Kobayashi R, Normand J, Raghavachari K, Rendell A, Burant JC, Iyengar SS, Tomasi J, Cossi M, Rega Millam NJ, Klene M, Knox JE, Cross JB, Bakken V, Adamo C, Jaramillo J, Gomperts RE, Stratmann O, Yazyev AJ, Austin R, Cammi C, Pomelli JW, Ochterski R, Martin RL, Morokuma K, Zakrzewski VG, Voth GA, Salvador P, Dannenberg JJ, Dapprich S, Daniels AD, Farkas O, Foresman JB, Ortiz JV, Cioslowski J, Fox DJ (2009) Gaussian 09, revision A02. Gaussian, Inc., Wallingford

34. Werner HJ, Knowles PJ, Lindh R, Manby FR, Schütz M, Celani P, Korona T, Mitrushenkov A, Rauhut G, Adler TB, Amos RD, Bernhardsson A, Berning A, Cooper DL, Deegan MJO, Dobbyn AJ, Eckert F, Goll E, Hampel C, Hetzer G, Hrenar T, Knizia G, Köppl C, Liu Y, Lloyd AW, Mata RA, May AJ, McNicholas SJ, Meyer W, Mura ME, Nicklaß A, Palmieri P, Pflüger K, Pitzer R, Reiher M, Schumann U, Stoll H, Stone AJ, Tarroni R, Thor-steinsson T, Wang M, Wolf A (2006) MOLPRO 2006.1. Uni-versity of Birmingham, Birmingham

35. Perdew JP (1986) Phys Rev B 33:8822

36. Perdew JP (1991) In: Ziesche P, Eschrig P (eds) Electronic structure of solids'91. Akademie Verlag, Berlin

37. Wilson PJ, Bradley TJ, Tozer DJ (2001) J Chem Phys 115:9233

38. Schmider HL, Becke AD (1998) J Chem Phys 108:9624

39. Becke AD (1993) J Chem Phys 98:1372

40. Zhao Y, Schultz NE, Truhlar DG (2005) J Chem Phys 123:194101

41. Zhao Y, Schultz NE, Truhlar DG (2006) J Chem Theory Comput 2:364

42. Zhao Y, Truhlar DG (2008) Theor Chem Acc 120:215

43. Adamo C, Barone V (1998) J Chem Phys 108:664

44. Adamo C, Barone V (1999) J Chem Phys 110:6158

45. Wilson AK, Woon DE, Peterson KA, Dunning TH Jr (1999) J Chem Phys 110:7667

46. Iikura H, Tsuneda T, Yanai T, Hirao K (2001) J Chem Phys 115:3540

47. Yanai T, Tew D, Handy N (2004) Chem Phys Lett 393:51

48. Chai JD, Head-Gordon M (2008) Phys Chem Chem Phys 10:6615

49. Tarnopolsky A, Karton A, Sertchook R, Vuzman D, Martin JML (2008) J Phys Chem A 112:3

50. Graham DC, Menon AS, Goerigk L, Grimme S, Radom L (2009) J Phys Chem A 113:9861

51. Curtiss LA, Redfern PC, Raghavachari K, Pople JA (1997) J Chem Phys 106:1063

52. Curtiss LA, Redfern PC, Raghavachari K, Pople JA (1998) J Chem Phys 109:42

53. Goerigk L, Grimme S (2011) J Chem Theory Comput 7:291

54. Curtiss LA, Redfern PC, Raghavachari K (2007) J Chem Phys 126:084108

55. Grimme S (2003) J Chem Phys 118:9095

56. Grimme S, Antony J, Ehrlich S, Krieg H (2010) J Chem Phys 132:154104. See also: http://toc.uni-muenster.de/DFTD3/index.html

57. Menon AS, Radom L (2008) J Phys Chem A 112:13225

58. Linstrom PJ, Mallard WG (eds) (2010) NIST chemistry webbook, NIST standard reference database number 69. National Institute of Standards and Technology, Gaithersburg

59. Merrick JP, Moran D, Radom L (2007) J Phys Chem A 111:11683

![](./images/811657663921258497_10.jpg)