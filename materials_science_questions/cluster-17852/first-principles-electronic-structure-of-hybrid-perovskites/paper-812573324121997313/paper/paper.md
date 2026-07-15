### PAPER
View Article Online
View Journal | View Issue

![](./images/812573324121997313_1.jpg)

Cite this: *RSC Adv.*, 2020, **10**, 32364

Received 10th July 2020
Accepted 27th August 2020

DOI: 10.1039/d0ra06028c
rsc.li/rsc-advances

# Structural, electronic, and optical properties of cubic formamidinium lead iodide perovskite: a first-principles investigation†

Sanjun Wang, $^{a}$ Wen-bo Xiao $\mathbb{D}^{b}$ and Fei Wang $\mathbb{D}^{*c}$

Hybrid organic-inorganic perovskites have been one of the most active areas of research into photovoltaic materials. Despite the extremely fast progress in this field, the electronic properties of formamidinium lead iodide perovskite (FAPbl₃) that are key to its photovoltaic performance are relatively poorly understood when compared to those of methylammonium lead iodide (MAPbl₃). In this study, first-principles total energy calculations based on density functional theory were used to investigate the favored orientation of FA. Different theoretical methods, with or without incorporation of spin-orbit coupling (SOC) effects, were used to study the structure, electronic properties, and charge-carrier effective mass. Also the SOC-induced Rashba $k$-dependent band splitting, density of states and optical properties are presented and discussed. These results are useful for understanding organic-inorganic lead trihalide perovskites and can inform the search for new materials and design rules.

## 1. Introduction

Hybrid organic-inorganic perovskites have found prominence as a material for the active photovoltaic layer in optoelectronic devices due to their high and balanced charge-carrier mobilities, suitable band gaps, and high absorption cross sections. $^{1-3}$ The most studied organic-inorganic lead trihalide perovskites have the general composition $APbX_{3}$, where $A=$ methylammonium (MA), formamidinium (FA), or Cs, and $X=$ I, Br, or Cl. Rapid progress in perovskite photovoltaic devices has seen certified efficiencies rise to above $25.2\%{}^{4}$ Although MAPbI₃ is the most studied hybrid metal-organic perovskite for photovoltaic applications, better performance in terms of photovoltaic efficiency is found in FAPbI₃ or mixed FA and MA hybrid perovskites. $^{5-7}$ This is because the increase in the effective cation radius caused by switching from the MA to the FA cation decreases the optical band gap, extending absorption into the near-infrared. Also FAPbI₃ gives better stability than MAPbI₃ at high temperatures. $^{8-10}$ However, its major flaw is that the black cubic $\alpha$ phase, which is responsible for the high photovoltaic efficiency, is metastable toward heat and moisture at normal operating conditions. $^{11-13}$ The stable phase, which is produced when FAPbI₃ is obtained by standard chemical methods, is the yellow hexagonal $\delta$ phase. Recently, however, Cordero *et al.* found that $\alpha$-FAPbI₃ can be perfectly stable for at least 100 days unless extrinsic factors induce its degradation. $^{8}$

There have been extensive theoretical works studying the structure and electronic, optical, and defect properties of MAPbI₃, and these have greatly deepened the understanding of MAPbI₃ and accelerated research into its application to devices. $^{14-19}$ Although there have been some of theoretical works studying FAPbI₃, $^{20-24}$ a systematic and comprehensive study is still absent. Pan *et al.* investigate the geometric and electronic structures of hybrid organic-inorganic perovskites FAPbX₃ ($X=$ Cl, Br, I). $^{20}$ Quarti *et al.* studied the flexibility structural and dynamics electronic properties of MAPbI₃ and FAPbI₃ using *ab initio* molecular dynamics simulations. $^{21}$ Kanno *et al.* theoretically studied the rotational potential energy surface of FAPbI₃. $^{22}$ Liu and Yam studied its intrinsic defects. $^{23}$ Guo *et al.* studied the effects of Rb incorporation and water degradation of the FAPbI₃ surface. $^{24}$

In this work, by using the first-principles total energy calculation method, we systematically investigated the structure, electronic properties, charge effective mass, $k$-dependent band splitting and optical properties of cubic $\alpha$-FAPbI₃. Different calculation methods were evaluated, specifically, standard density functional theory (DFT), screened hybrid DFT, and the *GW* approach, both with and without incorporation of spin-orbit coupling (SOC) effects. The ideal method would be a *GW* approach incorporating SOC, but this is highly computationally expensive. Among the other approaches, the DFT method using the Perdew-Burke-Ernzerhof functional (DFT-PBE) gives a more accurate band-gap energy, using the PBE

---

$^{a}$College of Artificial Intelligence, Henan Finance University, Zhengzhou 450046, China  
$^{b}$Key Laboratory of Nondestructive Testing Ministry of Education, Nanchang Hangkong University, Nanchang 330063, China  
$^{c}$International Laboratory for Quantum Functional Materials of Henan, School of Physics and Microelectronics, Zhengzhou University, Zhengzhou 450001, China.  
E-mail: wfei@zzu.edu.cn  
† Electronic supplementary information (ESI) available: The POSCAR file for FAPbI₃ PBE [111]. See DOI: 10.1039/d0ra06028c

---

32364 | *RSC Adv.*, 2020, **10**, 32364-32369
This journal is © The Royal Society of Chemistry 2020

functional including van der Waals interactions (PBE-vdW) gives a more accurate lattice constant, and the screened hybrid functional of Heyd, Scuseria, and Ernzerhof (HSE06) gives more reliable contributions from SOC effects. The transport properties of the charge effective mass and the optical properties are also given and discussed.

## 2. Computational details

The first-principles total energy calculation was performed using the Vienna *Ab initio* Simulation Package (VASP)²⁵,²⁶ with the standard frozen-core projector augmented-wave method and the exchange-correlation functional of generalized gradient approximation in the PBE format.²⁷ A cut-off energy of 400 eV was chosen to achieve the desired accuracy. During the optimization of the geometric structure, the total energy convergence criterion was chosen as $10^{-5}$ eV, and the force on each atom was converged to an accuracy of 0.01 eV Å⁻¹. The zero-damping DFT-D3 method of Grimme²⁸ was amended to correct for the vdW interaction in the DFT-vdW calculations. Since relativistic effects has large effect on the Pb atom, this effect was considered using SOC calculations. The HSE06 functional²⁹ with 25% of the Hartree-Fock exchange was used in the HSE06 calculations. A reciprocal-space sampling with $\Gamma$ centers in an $8 \times 8 \times 8$ Monkhorst-Pack $k$-point mesh³⁰ was set in the Brillouin zone for the standard DFT calculations. For the HSE06 calculations, a shifted $3 \times 3 \times 3$ $k$-point mesh was set in the Brillouin zone. The VASPKIT toolkit was used to obtain the lattice constant, the bulk modulus in the Birch-Murnaghan equation of state, and the charge effective mass.³¹

## 3. Results and discussion

### 3.1 Structural properties

At 300 K, FAPbI₃ has a cubic perovskite ABX₃ structure with space group $Pm\overline{3}m$. Although FA molecules are less polar than MA molecules, the polarization of FA still has great impact on the structure and the optoelectronic properties of FAPbI₃, such as the total energy, the crystal lattice, phase transitions, and the band gap of the system. To clarify the favored orientation of the FA cation in FAPbI₃, we performed first-principles total-energy calculations on various FA orientations. Three possible local minima were set, with the FA molecule aligned along the ⟨100⟩, ⟨110⟩, and ⟨111⟩ directions. In contrast to the single C-N bond in MA, the direction of polarization in MA is unique, there are two C-N bonds in the FA molecule and the N-C-N group forms a $126^\circ$ angle. We therefore used the connection directions of the two nitrogen atoms to align the FA molecule inside the unit cell. Aside from those forming the fixed cell shape, all atoms within the cell included the volume were fully relaxed to obtain the energy minimum. Here, the ⟨100⟩ orientation structure was obtained from the well-accepted structure of Weller *et al.*¹² The ⟨110⟩ and ⟨111⟩ structures were obtained by rotating the FA molecule into each respective orientation. The fully optimized structures are shown in Fig. 1, and the total energy of the unit cell and its lattice constant are shown below each structure. It can be seen from Fig. 1(b) that in the ⟨110⟩ structure, the FA molecule relaxed to the ⟨111⟩ orientation with slight divergence. The total energy of the optimized systems was found to be lower than in the ⟨100⟩ structure, by 0.0897 eV and 0.1205 eV. Furthermore, the band gaps, at 1.6316 and 1.6842 eV, were larger than the 1.5434 eV found in the ⟨100⟩ structure. So there are two local minimum total energy structure configuration in FAPbI₃, that are FA aligned with the ⟨100⟩ orientation or ⟨111⟩ orientation, as shown in Fig. 1.

The ground state of FAPbI₃ with a ⟨111⟩ orientation was the most stable, which is consistent with the results of calculations with the MA cation in the ground state of MAPbI₃, due to the organic molecule being oriented in the ⟨111⟩ direction, where it has maximum freedom.³²,³³ The most stable ⟨111⟩ orientation structure was different from the ⟨100⟩ orientation structure obtained by Weller *et al.*¹² This can be explained by Weller *et al.*'s structure being obtained at 298 K, whereas our DFT-calculated ⟨111⟩ orientation was the ground state at 0 K. This divergence in the ⟨111⟩ orientation at low temperature may induce a locally disordered low-temperature $\gamma$ phase,¹³ while the regular ⟨100⟩ orientation of the FA molecule results in a locally ordered high-temperature $\alpha$ phase. This rotational dynamics of FA molecular have revealed by the first-principles molecular dynamics simulation by Carignano *et al.*,³⁴ which show that at room temperature, the orientation of the sum vector is essen- tially (100) and should form a rotational glass at lower temperatures. These thermal effects of FA molecular are similar with MA molecular in MAPbI₃.³⁵,³⁶ Since only the cubic $\alpha$ phase

![](./images/812573324121997313_2.jpg)

Fig. 1 The optimized structures of FA aligned with the origin in the (a) ⟨100⟩, (b) ⟨110⟩, and (c) ⟨111⟩ directions in FAPbI₃. The labels below each panel indicate the optimized total energy and the lattice constant of the unit cell.

<table><caption>Table 1 Calculated lattice constant $a$, bulk modulus $B_0$, and band gap $E_g$ with and without SOC, of cubic FAPbI$_3$. Corresponding results from the theoretical and experimental literature are also presented for comparison</caption>
<thead>
<tr>
<th></th>
<th>Lattice constant $a$ (Å)</th>
<th>Bulk modulus $B_0$ (GPa)</th>
<th>Band gap $E_g$ (eV)</th>
<th>$E_g$ with SOC (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>DFT-PBE</td>
<td>6.5219</td>
<td>11.5287</td>
<td>1.5434</td>
<td>0.5157</td>
</tr>
<tr>
<td>DFT-vdW</td>
<td>6.4064</td>
<td>16.1087</td>
<td>1.3952</td>
<td>0.4169</td>
</tr>
<tr>
<td>HSE06</td>
<td>6.5193</td>
<td>11.3210</td>
<td>1.9937</td>
<td>1.1732</td>
</tr>
<tr>
<td>Theoretical</td>
<td>$6.3992,^{20} 6.42,^{24}$</td>
<td>—</td>
<td>$1.368,^{19} 1.40,^{20} 1.75,^{21} 1.45,^{24}$<br>$1.43,^{37} 1.43,^{38}$</td>
<td>$0.224,^{19} 0.66,^{21} 0.82,^{24} 1.47,^{38}$</td>
</tr>
<tr>
<td>Experimental</td>
<td>$6.3503,^{11} 6.3620,^{37} 6.3558,^{39}$</td>
<td>—</td>
<td>$1.53,^{11} 1.489,^{9} 1.45,^{39}$</td>
<td>—</td>
</tr>
</tbody>
</table>

at room temperature is of interest for use in solar cells, we examine only the $\langle 100 \rangle$ orientation cubic $\alpha$ phase in experiment by Weller et al. $^{12}$ in the remainder of this paper.

### 3.2 Electronic properties

Geometric optimization of the atomic positions (and cell parameters) was performed using three different methods, that is, DFT-PBE, DFT-vdW, and HSE06. The lattice parameters, bulk modulus, and band gap, with and without SOC, of the cubic FAPbI$_3$ structure obtained from our calculations are listed in Table 1. Comparing the calculations from the three different models, DFT-PBE provides the most accurate band gap, 1.5434 eV compared with the experimental results of 1.53 eV to 1.45 eV. However, this accuracy is mainly due to the strong relativistic effects of the Pb atom offsetting the underestimation error in the band gap obtained using typical DFT calculations. It can be seen from Table 1 that after including SOC, the DFT-PBE method gives a band gap of only 0.5157 eV, and the DFT-vdW method gives a similarly low band gap of 0.4169 eV. The HSE06-SOC method produces a value of 1.1732 eV, which is still significantly lower than the experimental value.

To obtain a more accurate value for the band gap, we used the $GW$ approach. Due to the high computational demands of the technique, we did not include SOC in these $GW$ calculations.

Using the DFT-vdW lattice constant, we obtained a band gap of 2.6041 eV from the $GW$ approach. If the decrease of $\sim$1.0 eV resulting from the SOC effect in the DFT calculations were repeated with the $GW$ calculations, that is, the reduction from 1.5434 to 0.5157 eV in DFT-PBE and from 1.3952 to 0.4169 eV in DFT-vdW, the $GW$ method including SOC would give a band gap of 1.6041 eV, which is close to the experimental value of 1.45 to 1.53 eV. If computing resources did not need to be considered, the $GW$ approach incorporating SOC would give the best results when compared to the experimental value. Otherwise, the DFT-PBE method results in the most accurate band-gap energy, the PBE-vdW method provides the most accurate lattice constant, and the HSE06 method gives reliable calculations of the contributions from SOC effects.

Cubic $\alpha$-FAPbI$_3$ perovskite is a direct-band-gap semiconductor with its conduction band minimum (CBM) and its valence band maximum (VBM) at the same R point (0.5, 0.5, 0.5). Fig. 2 shows the three different calculated band structures with and without the inclusion of SOC effects. It can be seen that the inclusion of SOC effects greatly decreases the band gap of FAPbI$_3$. The band gaps calculated from DFT-PBE and DFT-vdW are decreased by about 1.0 eV after inclusion of the SOC effects. The HSE06 calculation including SOC effects has a band gap that is about 0.82 eV lower, decreasing from 1.9937 eV to

![](./images/812573324121997313_3.jpg)

Fig. 2 The electronic band structures of perovskite cubic FAPbI$_3$ calculated from DFT-PBE, DFT-vdW, and HSE06, without SOC (a–c) and with SOC (d–f).

![](./images/812573324121997313_4.jpg)

Fig. 3 (a) The total and projected DOS of FAPbI₃ for Pb, I, and FA from DFT-PBE calculations, and enlarged views of the band dispersion around the R point for (b) DFT-PBE with SOC and (c) HSE06 with SOC.

1.1732 eV. The good consistency of the band-gap energy with experiments in the DFT calculations is caused by the strong relativistic effect of the Pb atoms offsetting the underestimation of the band gap by typical DFT calculations. This accurate calculation of band-gap energy is also seen in the typical Pb-containing perovskite, MAPbI₃.¹⁵,³² Considering that the three sets of calculations with and without the inclusion of SOC effects result in nearly the same band-edge orbital characters and band-gap positions in k-space, as well as the same trend in band-gap change, it can be concluded that DFT-PBE is able to provide an accurate qualitative picture of the evolution of the electronic structure in FAPbI₃ in common cases.

Fig. 3(a) shows the total and projected density of states (DOS) of cubic FAPbI₃ calculated using the DFT-PBE method. Based on these calculations, in FAPbI₃, FA and Pb donate one and two electrons, respectively, to the three I ions, forming a band gap between the unoccupied Pb 6p orbital in the conduction band (CB) and the occupied Pb 6s and I 5p orbitals in the valence band (VB), which is consistent with the MAPbI₃ results.¹⁴,³² There are, however, differences in orbital character that result from the differences between the FA and MA molecules. The FA shows DOS peaks near −2.9 and 3.0 eV by the 2p orbitals of the C and N atoms, while the MA shows orbitals near and below −5 eV, under the Fermi level, and no orbitals in the CB.¹,¹⁴

Because SOC has a large effect on the band-gap energy, it is an interesting property that produces k-dependent band splitting in Pb-containing perovskites. Enlarged views of the band dispersion around the R point as calculated by DFT-PBE and HSE06 with SOC are shown in Fig. 3(b) and (c), respectively. It can be seen that the VB and CB both exhibit band splitting, and this seems to be the same in the CB and the VB. This is in contrast to previous results obtained for MAPbI₃ because previous studies used the lower-symmetry tetragonal or pseudocubic phases.¹⁶ Here, we used the cubic $Pm\overline{3}m$ phase. Our results show that Pb SOC effects induce a large decease in the band gap and cause band splitting in the band edge of FAPbI₃. These large SOC effects and Rashba band splitting may induce a long carrier life in FAPbI₃.⁴⁰

### 3.3 Transport properties

The remarkable properties of FAPbI₃ perovskite in relation to solar cells are partially the result of its excellent charge-transport properties. Using the parabolic approximation, we calculated the effective mass ($m^{*}$) of carriers around the CBM and the VBM by fitting the dispersion relation, $m^{*} = \mathrm{h}^{2}/[\partial^{2}E(k)/\partial k^{2}]$, where $E(k)$ is the band-edge eigenvalue and $k$ is the wavevector. The effective hole and electron masses ($m_{\mathrm{h}}^{*}$ and $m_{\mathrm{e}}^{*}$) along three high-symmetry directions in cubic FAPbI₃, calculated using the DFT-PBE and HSE06 methods with and without the inclusion of SOC effects, are shown in Table 2. If the spin-orbit coupling effects are included, the effective mass decreases markedly. The lowest effective mass reaches 0.15 $m_{0}$ for both holes and electrons. We get an average effective hole and electron masses 0.213 $m_{0}$ and 0.184 $m_{0}$ close to Muhammad *et al.*³⁸ $G_{0}W_{0} +$ SOC results 0.273 $m_{0}$ and 0.218 $m_{0}$. These results show that the SOC effects have a great impact on not only the band-gap energy but also band-edge dispersion and transport properties. This is consistent with the results for MAPbI₃.¹⁶,³² Furthermore, the smaller effective mass in FAPbI₃ as compared to MAPbI₃ will result in better optoelectronic properties. This improvement in charge-transport

Table 2 The effective hole and electron masses ($m_{\mathrm{h}}^{*}$ and $m_{\mathrm{e}}^{*}$) along three high-symmetry directions in cubic FAPbI₃ as calculated by DFT-PBE and HSE06 with and without the inclusion of SOC effects. The unit is $m_{0}$

<table>
<thead>
<tr>
<th></th>
<th colspan="2">DFT-PBE</th>
<th colspan="2">DFT-PBE + SOC</th>
<th colspan="2">HSE06</th>
<th colspan="2">HSE06 + SOC</th>
<th colspan="2">$G_{0}W_{0}+SOC^{38}$</th>
</tr>
<tr>
<th></th>
<th>$m_{\mathrm{h}}$</th>
<th>$m_{\mathrm{e}}$</th>
<th>$m_{\mathrm{h}}$</th>
<th>$m_{\mathrm{e}}$</th>
<th>$m_{\mathrm{h}}$</th>
<th>$m_{\mathrm{e}}$</th>
<th>$m_{\mathrm{h}}$</th>
<th>$m_{\mathrm{e}}$</th>
<th>$m_{\mathrm{h}}$</th>
<th>$m_{\mathrm{e}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>R-Γ</td>
<td>0.200</td>
<td>0.255</td>
<td>0.147</td>
<td>0.109</td>
<td>0.214</td>
<td>0.265</td>
<td>0.241</td>
<td>0.144</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>R-X</td>
<td>0.239</td>
<td>0.188</td>
<td>0.186</td>
<td>0.115</td>
<td>0.270</td>
<td>0.195</td>
<td>0.190</td>
<td>0.149</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>R-M</td>
<td>0.192</td>
<td>0.843</td>
<td>0.143</td>
<td>0.116</td>
<td>0.251</td>
<td>0.848</td>
<td>0.209</td>
<td>0.260</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>Average</td>
<td>0.210</td>
<td>0.428</td>
<td>0.159</td>
<td>0.113</td>
<td>0.245</td>
<td>0.436</td>
<td>0.213</td>
<td>0.184</td>
<td>0.273</td>
<td>0.218</td>
</tr>
</tbody>
</table>

![](./images/812573324121997313_5.jpg)

Fig. 4 Absorption spectra for FAPbI₃ and MAPbI₃. Inset shows an enlarged plot of the absorption near the band gap.

properties and the smaller band gap in FAPbI₃ than MAPbI₃ results in better optoelectronic properties in cubic FAPbI₃.

### 3.4 Optical properties
As FAPbI₃ is an important optoelectronic material for solar cells, it is useful to study its absorption spectrum. For comparison, Fig. 4 shows absorption spectra for both FAPbI₃ and MAPbI₃ as calculated by DFT-PBE, which can reflect the absorption ratio already. It can be seen that FAPbI₃ has almost the same high absorption spectrum as MAPbI₃. From the inset, it can also be seen that FAPbI₃ has a lower band gap than MAPbI₃. The high level of absorption seen in these spectra is what leads to the high efficiency seen in mixed FA and MA solar cells.

## 4. Conclusions
This study systematically examined the structure, electronic properties, charge effective mass, and optical properties of cubic $\alpha$-FAPbI₃. The calculations of total energy showed that the most stable FA structure is aligned in the $\langle 111 \rangle$ direction at 0 K, though this reorients to a $\langle 100 \rangle$ ordered-symmetry structure at high temperatures. Different theoretical methods, specifically standard DFT-PBE and PBE-vdW, HSE06, and $GW$, with and without the incorporation of SOC effects, were evaluated in this work. The ideal method would be a $GW$ approach incorporating SOC. Among the other methods, DFT-PBE results in a more accurate band-gap energy, DFT-vdW gives a more accurate lattice constant, and HSE06 gives more reliable calculations of the contributions from SOC effects. The SOC effects have a great impact on the band-gap energy and Rashba band splitting, which may induce a long carrier life in FAPbI₃. The excellent and balanced charge-carrier motilities and optical-absorption properties explain the high photovoltaic efficiency in cubic $\alpha$-FAPbI₃. These results are useful for understanding organic-inorganic lead trihalide perovskites and can inform the search for new materials and design rules.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
Open Fund of the Key Laboratory of Nondestructive Testing of Ministry of Education of Nanchang HangKong University (Grant No. EW201908442 and EW201980090).

## References
1 Z. Xiao and Y. Yan, Progress in Theoretical Study of Metal Halide Perovskite Solar Cell Materials, *Adv. Energy Mater.*, 2017, **7**, 1701136.

2 C.-X. Zhang, T. Shen, D. Guo, L.-M. Tang, K. Yang and H.-X. Deng, Reviewing and understanding the stability mechanism of halide perovskite solar cells, *Infomatics*, 2020, 1-23.

3 S. Gonzalez-Carrero, R. E. Galian and J. Pérez-Prieto, Organic-inorganic and all-inorganic lead halide nanoparticles, *Opt. Express*, 2016, **24**, A285.

4 National Renewable Energy Laboratory, Best Research-Cell Efficiency Chart.

5 N. J. Jeon, J. H. Noh, W. S. Yang, Y. C. Kim, S. Ryu, J. Seo and S. Il Seok, Compositional engineering of perovskite materials for high-performance solar cells, *Nature*, 2015, **517**, 476-480.

6 Q. Han, S. H. Bae, P. Sun, Y. T. Hsieh, Y. Yang, Y. S. Rim, H. Zhao, Q. Chen, W. Shi, G. Li and Y. Yeng, Single Crystal Formamidinium Lead Iodide (FAPbI₃): Insight into the Structural, Optical, and Electrical Properties, *Adv. Mater.*, 2016, **28**, 2253-2258.

7 A. Zhumekenov, M. I. Saidaminov, M. A. Haque, E. Alarousu, S. P. Sarmah, B. Murali, I. Dursun, X. H. Miao, A. L. Abdelhady, T. Wu, O. F. Mohammed and O. M. Bakr, Formamidinium Lead Halide Perovskite Crystals with Unprecedented Long Carrier Dynamics and Diffusion Length, *ACS Energy Lett.*, 2016, **1**, 32-37.

8 F. Cordero, F. Craciun, F. Trequattrini, A. Generosi, B. Paci, A. M. Paoletti and G. Pennesi, Stability of Cubic FAPbI₃ from X-ray Diffraction, Anelastic, and Dielectric Measurements, *J. Phys. Chem. Lett.*, 2019, **10**, 2463-2469.

9 G. Liu, L. Kong, J. Gong, W. Yang, H. Mao, Q. Hu, Z. Liu, R. D. Schaller, D. Zhang and T. Xu, Pressure-Induced Bandgap Optimization in Lead-Based Perovskites with Prolonged Carrier Lifetime and Ambient Retainability, *Adv. Funct. Mater.*, 2017, **27**, 1604208.

10 A. Francisco-López, B. Charles, M. I. Alonso, M. Garriga, M. Campoy-Quiles, M. T. Weller and A. R. Goñi, Phase Diagram of Methylammonium/Formamidinium Lead Iodide Perovskite Solid Solutions from Temperature-Dependent Photoluminescence and Raman Spectroscopies, *J. Phys. Chem. C*, 2020, **124**, 3448-3458.

11 A. G. Kontos, G. K. Manolis, A. Kaltzoglou, D. Palles, E. I. Kamitsos, M. G. Kanatzidis and P. Falaras, Halogen-$NH^{2+}$ Interaction, Temperature-Induced Phase Transition, and Ordering in $(NH_2CHNH_2)PbX$ 3 (X = Cl, Br, I) Hybrid Perovskites, *J. Phys. Chem. C*, 2020, **124**, 8479-8487.

12 M. T. Weller, O. J. Weber, J. M. Frost and A. Walsh, Cubic Perovskite Structure of Black Formamidinium Lead Iodide,

$\alpha$-[HC(NH₂)₂]PbI₃, at 298 K, J. Phys. Chem. Lett., 2015, 6, 3209-3212.

13 O. J. Weber, D. Ghosh, S. Gaines, P. F. Henry, A. B. Walker, M. S. Islam and M. T. Weller, Phase Behavior and Polymorphism of Formamidinium Lead Iodide, Chem. Mater., 2018, 30, 3768-3778.

14 W.-J. Yin, T. Shi and Y. Yan, Unusual defect physics in CH₃NH₃PbI₃ perovskite solar cell absorber, Appl. Phys. Lett., 2014, 104, 063903.

15 A. Amat, E. Mosconi, E. Ronca, C. Quarti, P. Umari, M. K. Nazeeruddin, M. Grätzel and F. De Angelis, Cation-induced band-gap tuning in organohalide perovskites: Interplay of spin-orbit coupling and octahedra tilting, Nano Lett., 2014, 14, 3608-3616.

16 G. Giorgi, J. I. Fujisawa, H. Segawa and K. Yamashita, Small photocarrier effective masses featuring ambipolar transport in methylammonium lead iodide perovskite: A density functional analysis, J. Phys. Chem. Lett., 2013, 4, 4213-4216.

17 Y. Huang, L. Wang, Z. Ma and F. Wang, Pressure-Induced Band Structure Evolution of Halide Perovskites: A First-Principles Atomic and Electronic Structure Study, J. Phys. Chem. C, 2019, 123, 739-745.

18 P. Umari, E. Mosconi and F. De Angelis, Relativistic GW calculations on CH₃NH₃PbI₃ and CH₃NH₃SnI₃ Perovskites for Solar Cell Applications, Sci. Rep., 2015, 4, 4467.

19 N. Hernández-Haro, J. Ortega-Castro, Y. B. Martynov, R. G. Nazmitdinov and A. Frontera, DFT prediction of band gap in organic-inorganic metal halide perovskites: An exchange-correlation functional benchmark study, Chem. Phys., 2019, 516, 225-231.

20 Y. Y. Pan, Y. H. Su, C. H. Hsu, L. W. Huang, K. P. Dou and C. C. Kaun, First-Principles Study on Electronic Structures of FAPbX₃ (X = Cl, Br, I) Hybrid Perovskites, J. Adv. Nanomater., 2016, 1, 33-38.

21 C. Quarti, E. Mosconi and F. De Angelis, Structural and electronic properties of organo-halide hybrid perovskites from ab initio molecular dynamics, Phys. Chem. Chem. Phys., 2015, 17, 9394-9409.

22 S. Kanno, Y. Imamura and M. Hada, Theoretical Study on Rotational Controllability of Organic Cations in Organic-Inorganic Hybrid Perovskites: Hydrogen Bonds and Halogen Substitution, J. Phys. Chem. C, 2017, 121, 26188-26195.

23 N. Liu and C. Y. Yam, First-principles study of intrinsic defects in formamidinium lead triiodide perovskite solar cell absorbers, Phys. Chem. Chem. Phys., 2018, 20, 6800-6804.

24 Y. Guo, C. Li, X. Li, Y. Niu, S. Hou and F. Wang, Effects of Rb Incorporation and Water Degradation on the Stability of the Cubic Formamidinium Lead Iodide Perovskite Surface: A First-Principles Study, J. Phys. Chem. C, 2017, 121, 12711-12717.

25 G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B, 1996, 54, 11169-11186.

26 G. Kresse and J. Furthmüller, Efficiency of ab initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci., 1996, 6, 15-50.

27 J. P. Perdew, K. Burke and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett., 1996, 77, 3865-3868.

28 S. Grimme, J. Antony, S. Ehrlich and H. Krieg, A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu, J. Chem. Phys., 2010, 132, 154104.

29 A. V. Krukau, O. A. Vydrov, A. F. Izmaylov and G. E. Scuseria, Influence of the exchange screening parameter on the performance of screened hybrid functionals, J. Chem. Phys., 2006, 125, 224106.

30 H. J. Monkhorst and J. D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B, 1976, 13, 5188-5192.

31 V. Wang, N. Xu, J. C. Liu, G. Tang and W.-T. Geng, VASPKIT: A User-friendly Interface Facilitating High-throughput Computing and Analysis Using VASP Code, 2019, arXiv:1908.08269.

32 F. Wang, M. Tan, C. Li, C. Niu and X. Zhao, Unusual pressure-induced electronic structure evolution in organometal halide perovskite predicted from first-principles, Org. Electron., 2019, 67, 89-94.

33 M. Tan, S. Wang, F. Rao, S. Yang and F. Wang, Pressures Tuning the Band Gap of Organic-Inorganic Trihalide Perovskites (MAPbBr₃): A First-Principles Study, J. Electron. Mater., 2018, 47, 7204-7211.

34 M. A. Carignano, Y. Saeed, S. A. Aravindh, I. S. Roqan, J. Even and C. Katan, A close examination of the structure and dynamics of HC(NH₂)₂PbI₃ by MD simulations and group theory, Phys. Chem. Chem. Phys., 2016, 18, 27109-27118.

35 M. A. Carignano, S. A. Aravindh, I. S. Roqan, J. Even and C. Katan, Critical Fluctuations and Anharmonicity in Lead Iodide Perovskites from Molecular Dynamics Supercell Simulations, J. Phys. Chem. C, 2017, 121, 20729-20738.

36 M. A. Carignano, A. Kachmar and J. Hutter, Thermal effects on CH₃NH₃PbI₃ perovskite from Ab initio molecular dynamics simulations, J. Phys. Chem. C, 2015, 119, 8991-8997.

37 F. F. Targhi, Y. S. Jalili and F. Kanjouri, MAPbI₃ and FAPbI₃ perovskites as solar cells: Case study on structural, electrical and optical properties, Results Phys., 2018, 10, 616-627.

38 Z. Muhammad, P. Liu, R. Ahmad, S. Jalali Asadabadi, C. Franchini and I. Ahmad, Tunable relativistic quasiparticle electronic and excitonic behavior of the FAPb(I₁₋ₓBrₓ)₃ alloy, Phys. Chem. Chem. Phys., 2020, 22, 11943-11955.

39 P. Wang, J. Guan, D. T. K. Galeschuk, Y. Yao, C. F. He, S. Jiang, S. Zhang, Y. Liu, M. Jin, C. Jin and Y. Song, Pressure-Induced Polymorphic, Optical, and Electronic Transitions of Formamidinium Lead Iodide Perovskite, J. Phys. Chem. Lett., 2017, 8, 2119-2125.

40 V. C. A. Taylor, D. Tiwari, M. Duchi, P. M. Donaldson, I. P. Clark, D. J. Fermin and T. A. A. Oliver, Investigating the Role of the Organic Cation in Formamidinium Lead Iodide Perovskite Using Ultrafast Spectroscopy, J. Phys. Chem. Lett., 2018, 9, 895-901.