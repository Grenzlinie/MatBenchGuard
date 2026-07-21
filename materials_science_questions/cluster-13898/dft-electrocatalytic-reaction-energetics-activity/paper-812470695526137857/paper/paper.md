# The modulating effect of N coordination on single-atom catalysts researched by Pt-N<sub>χ</sub>-C model through both experimental study and DFT simulation

Mengmeng Fan $^{a,b,1,*}$, Jiewu Cui $^{b,c,1}$, Junjie Zhang $^{b}$, Jingjie Wu $^{d}$, Shuangming Chen $^{e}$, Li Song $^{e}$, Zixing Wang $^{b}$, Ao Wang $^{g}$, Robert Vajtai $^{b}$, Yucheng Wu $^{c,*}$, Pulickel M. Ajayan $^{b}$, Jianchun Jiang $^{g,*}$, Dongping Sun $^{f,*}$

$^{a}$ Nanjing Forestry University, Jiangsu Co-Innovation Center for Efficient Processing and Utilization of Forest Resources, College of Chemical Engineering, Nanjing 210037, China
$^{b}$ Rice University, Department of Materials Science and NanoEngineering, Houston, TX 77005, USA
$^{c}$ Hefei University of Technology, School of Materials Science and Engineering, Hefei 230009, China
$^{d}$ University of Cincinnati, Department of Chemical and Environmental Engineering, Cincinnati, OH 45221, USA
$^{e}$ University of Science and Technology of China, National Synchrotron Radiation Laboratory, CAS Center for Excellence in Nanoscience, Hefei 230026, China
$^{f}$ Nanjing University of Science and Technology, Chemicobiology and Functional Materials Institute, Nanjing 210094, China
$^{g}$ Key Lab of Biomass Energy and Material, Jiangsu Province, Jiangsu Co-Innovation Center of Efficient Processing and Utilization of Forest Resources, Institute of Chemical Industry of Forest Products, Chinese Academy of Forestry, Nanjing 210042, China

---

## ARTICLE INFO

**Article history:**
Received 30 September 2020
Revised 24 January 2021
Accepted 26 January 2021
Available online 24 April 2021

**Keywords:**
Modulating effect
N coordination
Single-atom catalysts
Pt-N<sub>χ</sub>-C model
DFT simulation

---

## ABSTRACT

N-doped carbon-based single-atom catalysts (NC-SACs) are widely researched in various electrochemical reactions due to high metal atom utilization and catalytic activity. The catalytic activity of NC-SACs originates from the coordinating structure between single metal site (M) and the doped nitrogen (N) in carbon matrix by forming M-N<sub>x</sub>-C structure ($1 \leq x \leq 4$). The M-N<sub>4</sub>-C structure is widely considered to be the most stable and effective catalytic site. However, there is no in-depth research for the "x" modulation in Pt-N<sub>x</sub>-C structure and the corresponding catalytic properties. Herein, atomically dispersed Pt on N-doped carbon (Pt-NC) with Pt-N<sub>x</sub>-C structure ($1 \leq x \leq 4$), as a research model, is fabricated by a ZIF-8 template and applied to catalytic oxygen reduction. Different carbonization temperatures are used to control N loss, and then modulate the N coordination of Pt-N<sub>x</sub>-C structure. The Pt-NC has the predictable low half-wave potential ($E_{1/2}$) of 0.72 V vs RHE compared to the Pt/C 20% of 0.81V due to low Pt content. Remarkably, the Pt-NC shows a high onset potential (1.10 V vs RHE, determined for $j = -0.1$ mA cm<sup>2</sup>) and a high current density of 5.2 mA cm<sup>-2</sup>, more positive and higher than that of Pt/C 20% (0.96 V) and 4.9 mA cm<sup>-2</sup>, respectively. As the structural characterization and DFT simulation confirmed, the reducing Pt-N coordination number induces low valence of Pt atoms and low free energy of oxygen reduction, which is responsible for the improved catalytic activity. Furthermore, the Pt-NC shows high mass activity (172 times higher than that of Pt/C 20%), better stability and methanol crossover resistance.

© 2021 Published by Elsevier Ltd on behalf of Chinese Society for Metals.

---

## 1. Introduction

Single-atom catalysts (SACs) are widely researched in various metal catalysts because of high atomic utilization and catalytic activity [1,2]. Carbon-supported SACs or metal nanoparticles are the most researched class and applied into various chemical transformations [3,4], especially, atomically dispersed metal atoms on N-doped carbon (NC-SACs) [5,6]. N-doped carbon is considered to be the most promising support material. N atoms doped into carbon matrix act as not only the excellent immobilizing sites for metal atoms [7-9] but also the catalytic sites in many electrochemical reactions [10-14]. As demonstrated in many researches, the catalytic activity of NC-SACs originates from the metal atoms surrounded by four N atoms (M-N<sub>4</sub>-C) which is known to be thermodynamically stable [15,16]. For example, Fe NC-SACs (single Fe atom catalysts supported on N-doped graphene) with Fe-N<sub>4</sub>-C structure have a low reducing overpotential with high Faradic efficiency (80%) in

---

* Corresponding authors.
E-mail addresses: fanmengmeng370@163.com (M. Fan), ycwu@hfut.edu.cn (Y. Wu), jiangjc@icifp.cn (J. Jiang), sundpe301@163.com (D. Sun).
1 The authors have contributed equally to this paper.

https://doi.org/10.1016/j.jmst.2021.01.093
1005-0302/© 2021 Published by Elsevier Ltd on behalf of Chinese Society for Metals.

![](./images/812470695526137857_1.jpg)
![](./images/812470695526137857_2.jpg)
![](./images/812470695526137857_3.jpg)

electrochemically reducing $CO_2$ [17], high benzene oxidation reaction activity [18]. The other NC-SACs include Zn NC-SACs showing high activity for reducing oxygen by $Zn$-$N_4$-C sites [19], Cr NC-SACs showing high activity for reducing oxygen by $Cr$-$N_4$-C [20], Pd NC-SACs showing high selectivity for photothermal hydrogenation of acetylene to ethylene by $Pd$-$N_4$-C [21]. Remarkably, the stable M-$N_4$-C structure does not represent the highest catalytic activity or most appropriate selectivity in a specific reaction, for instance, the $Ni$-$N_2$-C structure shows the highest catalytic activity of $CO_2$ reduction [22] and the $Zn$-$N_2$-C has the highest activity for oxygen reduction [23]. Modulating M-$N_x$-C structure by changing "x" is an effective approach to design and prepare NC-SACs with controllable catalytic activity [22,24].

Pt-based electrocatalysts are considered to be one of the best electrocatalysts for several important electrochemical reactions in energy storage and conversion, such as oxygen reduction reaction (ORR) [25], hydrogen evolution reaction (HER) [26], and methanol electrooxidation [27]. Due to the expensive price and limited reserve [28,29], the cost of traditional Pt-based catalysts limits the practical application. Therefore, the exploration of Pt NC-SACs is extremely significant for reducing the cost of Pt-based catalysts. However, there are few reports to explore the modulating effect of N coordination on the catalytic activity of Pt-based NC-SACs.

In this research, atomically dispersed $Pt^{2+}$ precursor was dispersed and restricted into the frameworks of ZIF-8. Then, the $Pt^{2+}$ was reduced, coordinated with local nearby N, C atoms and formed Pt-$N_x$-C structure after carbonization progress. The Pt-NC with different N coordination is prepared by modulating carbonization temperature [18,30]. The changing of the N-coordinating environment directly affects the electronic structures of single $Pt^{\delta +}$ ($0 \leq \delta < 2$) atom, resulting in distinctly different catalytic activities [31-33]. The results show that high carbonization temperature results in high N loss, and the resultant low Pt-N coordination corresponds to the low chemical state of $Pt^{\delta +}$ ($0 \leq \delta < 2$), which is beneficial to reducing the energy barrier in oxygen reduction. The modulated Pt-NC catalysts show high catalytic performances which are comparable with commercial Pt/C catalyst.

## 2. Experimental sections

### 2.1. Preparation of Pt-NC

Solution A: tetraammineplatinum chloride monohydrate (Sigma-Aldrich, purity ~98%) of 4.5 mg, 9 mg, 13.5 mg was dissolved into 7 ml methanol and 1 ml deionized water (for preparing $Pt^{2+}$/ZIF-8-0.5%, -1.0% -1.5%) or 18 mg dissolved into 7 ml methanol and 2 ml deionized water (for preparing $Pt^{2+}$/ZIF-8-2.0%). After completely dissolving, 0.83 g zinc nitrate hexahydrate (Sigma-Aldrich, purity ~98%) was added to the above solution. Solution B: 0.92 g 2-methylimidazole (Sigma-Aldrich, purity ≥99%) was dissolved into 28 ml methanol.

Then solutions A, B were mixed and stirred for half an hour at room temperature. Then, the above solution was rested for another 23.5 h. The white precipitates were collected by centrifuge (4000 rpm, 5 min) and washed 3 times with ethanol. Finally, the precipitates were dried for 5 h at 80°C in an oven. The obtained white powders were placed in a porcelain boat and annealed at (800, 900, 1000, 1100°C for 1 h under Ar of 100 sccm). Subsequently, as-prepared black powders were immersed in 0.1 M HCl overnight to remove residual Zn species, and washed several times with DI water until neutral pH value and dried under 60°C in a vacuum oven. The blank sample was prepared by the same method but without the addition of tetraammineplatinum chloride monohydrate.

### 2.2. Characterization of Pt-NC

The X-ray diffraction spectrum (XRD) was measured by X-ray diffractometer (Rigaku D/Max Ultima II, Cu $K\alpha$ radiation). The Raman spectra were measured by Raman spectroscopy (Renishaw, 532 nm laser excitation). The X-ray photoelectron spectroscopy (XPS) was completed by X-ray photoelectron spectrometer (PHI Quantera). The field emission scanning electron microscope (FE-SEM) images were obtained by a scanning electron microscope (FEI Quanta 400). The transmission electron microscope (TEM) images were obtained by a transmission electron microscope (JEOL HC). The $N_2$ adsorption-desorption isotherms and the pore size distribution were obtained by an automated gas sorption analyzer (Quantachrome instrument, iQ3). The high-resolution transmission electron microscope (HR-TEM) images were measured by a field emission gun transmission electron microscope (JEOL 2100F). The aberration-corrected high-angle annular dark-field scanning transmission electron microscope (HAADF-STEM) images were obtained by FEI Titan Themis³ S/TEM at 300 kV with probe spherical aberration correctors, and Super-X quad energy dispersive spectrometer (EDS) detector. The inductively coupled plasma mass spectrometry (ICP-MS) was obtained by Perkin Elmer Optima 4300DV.

### 2.3. Rotating disk electrode (RDE) measurement in alkaline solution

The RDE test was completed in a three-electrode system by electrochemical workstation (CHI 608D). The Hg/HgO electrode and Pt wire were used as reference electrode and counter electrode, respectively. The catalyst of 4 mg was dispersed into the solution of 2 ml (DI water: isopropanol: 5 wt% Nafion solution = 80%: 10%: 10%, v/v). The above ink was sonicated for 4 h. 20 $\mu$L of Pt-NC catalyst ink or 16 $\mu$L Pt/C (20 wt%) was dropped on an RDE (5 mm in diameter) and dried under ambient condition. The $O_2$ or $N_2$ flow was constant 100 sccm during the RDE or CV test in 0.1 M KOH. The CV curves were measured at 100 mV s⁻¹ with the potential from 0 V to 1.1 V (vs RHE). The LSV was performed with potential from 0 V to 1.1 V at a scan rate of 10 mV s⁻¹ with different rotating speeds. The catalytic stability was measured at 0.56 V for 8000 s in 0.1 M KOH. The resistant methanol was measured in 0.1 M KOH at 10 mV s⁻¹. The RHE was calculated based on the following equation: $V_{RHE} = V_{(Hg/HgO)} + 0.0592 \times pH + 0.095$.

K-L equations [34]:

$$
\frac{1}{J} = \frac{1}{B\omega^{1/2}} + \frac{1}{J_K} \tag{1}
$$

$$
B = 0.62nFC_0(D_0)^{2/3}\gamma^{-1/6} \tag{2}
$$

$J$ current density, $\omega$ electrode rotation rate, $n$ electron transfer number, $F$ Faraday constant ($F = 96485$ C mol⁻¹), $C_0$ bulk concentration of $O_2$ ($C_0 = 1.2 \times 10^{-3}$ mol L⁻¹), $D_0$ the diffusion coefficient of $O_2$ ($D_0 = 1.9 \times 10^{-5}$ cm s⁻¹), and $\gamma$ the kinematic viscosity of the electrolyte ($\gamma = 0.1$ m² s⁻¹) [35-37].

### 2.4. Rotating ring-disk electrode (RRDE) measurement in alkaline solution

The RRDE measurement was carried out to determine the yield of $H_2O_2$ (%) and the electron transfer number ($n$), which was calculated by Eqs. (3) and (4):

$$
H_2O_2(\%) = \frac{200I_r/N}{I_d + I_r/N} \tag{3}
$$

$$
n = \frac{4I_d}{I_d + I_r/N} \tag{4}
$$

$I_d$ the disk currents, $I_r$ the ring currents, $N$ the ring current collection efficiency (37% the RRDE electrode: PINE E7R9)

### 2.5. Theoretical calculations

The DFT calculations were completed by the Vienna ab initio simulation package (VASP) [38,39]. The projector-augmented wave (PAW) potentials with the generalized gradient approximation of the Perdew-Burke-Ernzerhof (GGA-PBE) formulation were used with a cutoff energy of 600 eV. The 8 × 8 graphene supercell and 3 × 3 k-point mesh were adopted in our calculations. A vacuum region with 20 Å thickness was introduced to eliminate interaction between slabs. The force for relaxation was converged to < 0.01 eV/Å. The equation of $G = E_{\text{total}} + E_{\text{ZPE}} - TS$ was used for obtaining the free energies of the reaction intermediates, where $E_{\text{total}}$ is the total energy of species, $E_{\text{ZPE}}$ is the zero-point energy and $S$ is the entropy. The configurational entropy is neglected. During the calculating progress of the free energy of the reaction intermediates, the effect of water was considered by adding a correction on the formation energy of reaction intermediates [40].

### 3. Results and discussion

$[\text{Pt}(\text{NH}_3)_4]^{2+}$ is an ideal platinum precursor due to the existence of $\text{NH}_3$ ligands which can guarantee $\text{Pt}^{2+}$ single atomic dispersion and avoid Pt accumulation during calcination [41]. In Fig. 1(a), the precursors of ZIF-8 and $[\text{Pt}(\text{NH}_3)_4]\text{Cl}_2$ were mixed after short-time sonication and the $[\text{Pt}(\text{NH}_3)_4]^{2+}$ was uniformly dispersed into the framework of ZIF-8 polyhedrons instead of replacing $\text{Zn}^{2+}$ note as demonstrated by the unchanged crystal structure of ZIF-8 (Fig. S1 in Supplementary Information) [42]. The dried $\text{Pt}^{2+}$/ZIF-8 was calcined under Ar gas at 1100°C to carbonize organic ligands, remove Zn residue and reduce $\text{Pt}^{2+}$ to $\text{Pt}^{\delta+}$ ($0 \leq \delta < 2$). At the same time, the $\text{Pt}^{\delta+}$ was embedded into N-doped carbon (NC) by forming N, C coordination. To optimize the Pt content, we mixed 1.5 wt.%, 2.0 wt.% $[\text{Pt}(\text{NH}_3)_4]\text{Cl}_2$ (compared to the weight of 2-methylimidazole) into ZIF-8 and named the as-prepared Pt-NC samples as Pt-NC-1.5% and Pt-NC-2.0%, respectively.

As shown in the SEM images, the polyhedrons of $\text{Pt}^{2+}$/ZIF-8-1.5% have uniform size distribution of ~300 nm (Figs. 1(b) and S2). The Pt-NC-1.5% also keeps an excellent polyhedral structure with abundant cracks on the surface (Fig. 1(c)) induced by releasing of internal gas molecules during carbonization. The as-prepared Pt-NC samples show high specific surface area of ~700 $\text{m}^2\text{g}^{-1}$ (Fig. 1(d)) with a mesopore size of 2–8 nm (Fig. 1(d), inset), which is beneficial to dispersing more single Pt atom [43,44]. In the HR-TEM images, the Pt-NC-1.5% not only shows abundant mesoporous structure but also there is no appearance of Pt nanoparticles (Fig. S3). In the HAADF-STEM images, the Pt-NC-1.5% (Pt content, 0.03 wt.%) shows significantly stronger metallic luster compared to the amorphous carbon of TEM grid, indicating the Pt doping (Fig. 1(e)). No obvious Pt clusters are observed in the HAADF-STEM images but only very few nanoparticles. To demonstrate the Pt atomically doping in blank areas, a series of EDS spectra were measured in the HAADF-STEM images (Fig. 1(e, f)). The EDS (Fig. 1(g1)) on Pt nanoparticles shows distinct Pt peaks of Pt-M, Pt-L$\alpha$ and Pt-L$\beta$ at 2.1 KeV, 9.6 KeV and 11.2 keV, respectively. The other three EDS spectra at blank areas (Fig. 1(g2-g4)) show similar Pt peaks, indicating the successful Pt doping in atomic size. In contrast, there is no Pt signal in the carbon network of the TEM grid in Fig. 1(g5). The high-resolution HADDDF-STEM images were measured and the images (Fig. 1(h) and (i)) show abundant bright dots, which strongly confirms the atomic isolation of Pt atoms. The Pt mapping also indicates the uniform Pt atomically doping (Fig. S4). Furthermore, the Pt-NC-1.5% shows amorphous carbon structure as demonstrated by the irregular fringe array at the edge of the polyhedron (Fig. S5) [45,46] and the broad (002), (100) peaks of amorphous carbon in XRD patterns (Fig. S6) [47]. However, when adding excessive Pt precursor, the obvious Pt nanoparticles appear in the Pt-NC-2.0% (Pt content, 0.036 wt.%) as shown in Fig. S7.

<table>
<caption>Table 1 The content of N species (at.%) in the Pt-NC-1.5% samples at various calcination temperatures</caption>
<thead>
<tr>
<th>Temperatue</th>
<th>Pyridinic N</th>
<th>Pt-N</th>
<th>Pyrrolic/graphitic N</th>
<th>Zn-N</th>
</tr>
</thead>
<tbody>
<tr>
<td>800°C</td>
<td>2.90</td>
<td>3.20</td>
<td>11.90</td>
<td>1.92</td>
</tr>
<tr>
<td>900°C</td>
<td>3.00</td>
<td>3.30</td>
<td>9.60</td>
<td>0.59</td>
</tr>
<tr>
<td>1000°C</td>
<td>0.71</td>
<td>0.84</td>
<td>4.65</td>
<td>/</td>
</tr>
<tr>
<td>1100°C</td>
<td>0.40</td>
<td>0.57</td>
<td>3.13</td>
<td>/</td>
</tr>
</tbody>
</table>

As shown in XPS survey spectra (Fig. 2(a)), the Pt-NC-1.5%, Pt-NC-2.0% and blank NC show N peaks corresponding to 4.1 at.%, 2.9 at.% and 4.4 at.%, respectively. In the N 1s spectrum of blank NC, two peaks at 398.2 eV and 400.8 eV are corresponding to pyridinic N and pyrollic N/graphitic N, respectively (Fig. 2(b)) [37,48]. A new peak of Pt-N at 398.7 eV appears in the Pt-NC-1.5%, indicating the existence of interaction between N atoms and $\text{Pt}^{\delta+}$ (Fig. 2(b)) [49]. With increasing calcination temperature, the N contents, Pt-N contents gradually decrease (Fig. 2(c) and (d)). The decrease of Pt-N indicates the decrease of the number of Pt-N coordination (Fig. 2(d)) when $\text{Pt}^{2+}$ is reduced to $\text{Pt}^{\delta+}$. Furthermore, with increasing calcinations temperature, the pyrollic-N/graphitic-N shifts from 399.8 eV to 400.9 eV, suggesting the conversion trend to graphitic-N. The binding energy of Pt-N shifts from 398.3 eV to 398.7 eV (Fig. 2(c)) due to the increase of reducing degree of $\text{Pt}^{\delta+}$. ZIF-8 has been widely researched as the NC support for SACs [50]. The relatively low annealing temperature (lower than 1000 °C) can realize the formation of M-N₄ structures such as Ir-N₄ [51], Cr-N₄ [14], Co-N₄ [52]. Under low calcination temperatures (800 and 900°C), abundant N sites (above 16 at.%) ensure high Pt-N coordination and form stably atomic dispersion like Ru-N₄, Fe-N₄ and Co-N₄ [37,53-55]. According to the Pt-N contents in the Pt-NC-1.5% at 800°C (3.2 at.%), at 900°C (3.3 at.%), we can theoretically calculate the content of $\text{Pt}^{\delta+}$ (~0.8 at.%), which is one quarter of Pt-N content, because the structure of four N atoms coordinating one metal atom is the most stable (Table 1) [37,56]. Under high temperature (1100°C), the Pt-N content of 0.57 at.% is lower than 0.8 at.%, indicating the number of Pt-N lower than that of $\text{Pt}^{\delta+}$. High temperature (1100°C) damages the Pt-N coordination, leading to the partial aggregation of Pt atoms which can explain the appearance of Pt nanoparticles (Fig. 1(f)) [24]. In the high-resolution of Pt 4f obtained by long-time scanning in XPS characterization, Pt-NC-1.5% contains two peaks located at 70.8 eV and 75.5 eV attributed to the Pt $4\text{f}_{7/2}$ and Pt $4\text{f}_{5/2}$ peaks, respectively, which are close to those of $\text{Pt}^0$ (Fig. 2(e)). The Pt $4\text{f}_{7/2}$ in the Pt-NC-1.5% at 900 and 1000°C shows relatively higher binding energy, 71.1 eV and 71.2 eV, respectively, indicating a more positive valence of $\text{Pt}^{\delta+}$ and higher N coordination (Fig. S8) [25,31]. The Pt $4\text{f}_{7/2}$ and Pt $4\text{f}_{5/2}$ peaks of the Pt-NC-2.0% shift to higher binding energy at 71.3 eV and 76.2 eV due to the formation of PtO on the surface of Pt nanoparticles (Fig. 2(e)) [49]. The X-ray absorption near-edge structure (XANES) was completed to further characterize Pt state, compared to the reported Pt $\text{L}_3$ edge intensity of $\text{PtO}_2$ (~2.32) and Pt foil (~1.24) [25,57-59], the white line intensity of Pt-NC-1.5% is 1.44 (Fig. S9), higher than that of $\text{PtO}_2$ and lower than that of Pt foil. The XANES measurement demonstrates the single Pt atom in Pt-NC-1.5% possesses a partially positive charge. In addition, the increasing temperature can effectively remove Zn impurity further demonstrated by ICP-MS and increase the graphitization degree of NC support as shown that the ratios of $I_D/I_G$ reduce from 1.22 to 0.92 in Raman spectra (Figs. 2(f) and S10) [60].

Compared to the CV curves in $\text{N}_2$-saturated 0.1 M KOH solution, there is an obvious reducing peak at 6.4 V vs RHE (All potential is relative to RHE, unless otherwise specified) in $\text{O}_2$-saturated solu-

![](./images/812470695526137857_4.jpg)

Fig. 1. (a) Schematic illustration for fabricating Pt-NC. SEM images of Pt²⁺/ZIF-8-1.5% without calcination (b) and Pt-NC-1.5% calcined at 1100°C for 1 h (c), bar 200 nm. (d) N₂ adsorption desorption isotherms of NC, Pt-NC calcined at 1100°C for 1 h (Inset is the pore diameter distribution curves). (e, f) Aberration-corrected HAADF-STEM images of Pt-NC-1.5% calcined at 1100°C for 1 h, bar 100 nm and 10 nm. (g) EDS spectra selecting different sites at HAADF-STEM images. (h, i) High-resolution HADDF-STEM image and corresponding enlarged view of Pt-NC-1.5% (calcined at 1100°C for 1 h) with abundant bright dots, bar 100 nm and 2 nm.

tion, indicating the catalytic performance of the Pt-NC-1.5% and Pt-NC-2.0% (Fig. 3(a)) for reducing oxygen [61]. It has been reported that N atoms doping can improve the catalytic performance of carbon materials [10,62] but the catalytic activity of N dopant can be negligible compared to the Pt sites in our research (Fig. S11). Due to the change of local electronic structure of single Ptᵟ⁺ effect by the changed N coordination through various calcination conditions, the Pt-NC-1.5% samples show different catalytic activities. As shown in Fig. 3(b), the Pt-NC-1.5% at 1100 °Cis considered to be the optimal annealed temperature according to the highest onset potential (1.10 V, determined for $j = -0.1$ mA cm⁻²), current density (5.2 mA cm⁻² at 0 V) and $E_{1/2}$ (half-wave potential, 0.72 V) [61,63]. We optimized the Pt loading as shown in Fig. S12. The high annealed temperature (1100°C) also can effectively remove the Zn impurity to eliminate the interference of Zn-N on overall catalytic activity (Table S1) and therefore all the following Pt-NC samples were annealed at 1100°C. Furthermore, the textural properties, important factors for catalytic performance [64,65], were compared by BET characterization in Fig. S13. With increasing carbonization temperature, the BET SSAs increase first and then decrease due to the increase and then decrease of micropores. The pore distribution shows a changing trend from micropores to mesopores because of the continuous collapse of micropore structure [64]. The increase of mesopores is beneficial to improving the catalytic activity by increasing the diffusion of electrolyte and oxygen.

Although the $E_{1/2}$ of Pt/C (20%) is 0.81 V vs RHE higher than that of the Pt-NC-1.5% (0.72 V), the Pt-NC-1.5% shows a higher onset potential of 1.10 V, much more positive than the Pt/C 20% (0.96 V), and a higher limited current density of 5.2 mA cm⁻² (4.9 mA cm⁻² for Pt/C 20%) (Fig. 3(c)). To further test the catalytic perfor-

![](./images/812470695526137857_5.jpg)

Fig. 2. (a) XPS survey scans for the NC, Pt-NC-1.5% and Pt-NC-2.0%. (b) The high-resolution N 1s spectra of NC, Pt-NC-1.5%. (c) The high-resolution N 1s of Pt-NC-1.5% samples under different calcination temperatures at 800-1100°C. (d) The contents of N configurations in the Pt-NC-1.5% samples at various temperatures. (e) The high-resolution Pt 4f of the Pt-NC-1.5%, -2.0%. (f) The Raman spectra of the Pt-NC-1.5% samples at different calcination temperatures.

mance of ORR, $2e^{-}$ or $4e^{-}$ transfer number corresponding to the products of $H_{2}O_{2}$ and $H_{2}O$, the polarization curves of the Pt-NC-1.5% at different rotation rates were measured (Fig. 3(d)) and the curves show that the current density gradually increases with increasing rotation speed due to the enhanced electrolyte diffusion rate [10]. According to the liner K-L equation and the corresponding fitting slope between $J^{-1}$ and $\omega^{-1/2}$ (Fig. 3(d) inset), the electron transfer number was computed to be 4.1, indicating a $4e^{-}$ pathway for oxygen reduction. The RRDE measurements were also completed to detect $H_{2}O_{2}$ generated during oxygen reduction and the low $H_{2}O_{2}$ yield indicates high $4e^{-}$ selectivity (Fig. 3(e)) [27]. The average electron transfer number of the Pt-NC-1.5% is ~3.88 close to ~3.95 of Pt/C (20%), higher than ~3.74 of the Pt-NC-2.0%, and the $H_{2}O_{2}$ yield is < 6.4% close to ~3.5% of Pt/C (20%) at 0.3-0.8 V. Pt-NC-1.5% samples calcined at different temperatures have the same changing trend of catalytic activity in alkaline or acidic environment, but they show lower catalytic performances in acidic environment (Fig. S14).

(1 M methanol was added into solution at 400 s).

The Tafel slope of the Pt-NC-1.5% is determined to be 84.3 mV decade⁻¹, lower than that of Pt/C (20%) (108.1 mV decade⁻¹) in Fig. 4(a). In the normalization of Pt loading, the mass activity of the Pt-NC-1.5% is 172 times higher than that of Pt/C (20%) in Fig. 4(b). The catalytic stability was measured by long-time (8000 s) chronoamperometry at 0.7 V and the Pt-NC-1.5% shows a slight reduction (down 6.5%) much lower than Pt/C 20% (down 42.2%) in Fig. 4(c). Furthermore, Pt-NC-1.5% also shows excellent methanol crossover resistance (Fig. 4(d)).

Compared to the catalyst of Pt (20%), it is a predictable result for the lower $E_{1/2}$, slightly lower electron transfer number of the Pt-NC-1.5% due to the low Pt content, while the higher onset potential of the Pt-NC-1.5% is unpredictable and needs further discussion. In this research, we have excluded the effect of the N species and Pt contents on the higher onset potential by the NC and Pt-NC-2.0% catalysts, respectively. According to the series of structural comparisons of Pt-NC-1.5% samples at increasing cal-

![](./images/812470695526137857_6.jpg)

Fig. 3. (a) CV curves of NC, Pt-NC-1.5%, -2.0% and Pt/C (20%) in $N_2$- or $O_2$-saturated 0.1 M KOH with a sweep rate of 100 mV s⁻¹. (b) RDE polarization curves of Pt-NC-1.5% samples under different calcination temperatures in $O_2$-saturated 0.1 M KOH with a sweep rate of 10 mV s⁻¹ and rotation rate of 1600 rpm. (c) LSV curves in $O_2$-saturated 0.1 M KOH aqueous solution with a sweep rate of 10 mV s⁻¹ and rotation rate of 1600 rpm. (d) LSV curves of Pt-NC-1.5% in $O_2$ saturated 0.1 M KOH at various rotation rates (Inset is K-L plots from 0.1 to 0.4 V vs RHE). (e) $H_2O_2\%$ yield of the samples during the LSV test (solid line) and the corresponding calculated electron transfer number (dashed line) with 10 mV s⁻¹ at 1600 rpm in 0.1 M KOH.

cination temperatures, great changes of coordinating structure of Pt-NC-1.5% samples have taken place including low Pt-N contents and weakly positive valence of Pt. Therefore, we speculate that the higher onset potential mainly originates from the changed coordinating structure, which is well demonstrated by the following DFT simulation.

We made a series of theory simulation based on the associative mechanism by DFT calculations to further demonstrate the modulating effect of variable N coordination on Pt-$N_x$-C in reducing oxygen. According to the change of Pt-N contents and Pt valence states, we speculated four potential Pt configurations which contain one, two, three and four Pt-N coordinating bonds, respectively (Fig. 5). Due to the same changing trend of experimentally catalytic activity of Pt-NC-1.5% samples, the following simulation is applicable for both acidic and alkaline environments.

With the decrease of the number of Pt-N coordination, the free energy of Pt-$N_x$-C gradually decreases and Pt-$N_1$-C shows the lowest $\Delta G$ indicating the lower energy barrier in ORR in Fig. 6 inset. The free energy diagrams (Fig. 6 inset) can well explain the origin of positive onset potential and low Tafel slope of Pt-NC-1.5% resulted from the highly active Pt sites for catalytically reducing oxygen, a kinetically controlled process at high potential. Based on the efficient reduction catalytic energy barrier in Pt-$N_1$-C, we proposed the reaction pathway for oxygen reduction in Fig. 6. At the first step, the double bonds of $O_2$ molecule were absorbed on single Pt⁸⁺ atom and then formed *OOH [66]. Compared to the adsorption of two O atoms on nearby Pt atoms in Pt nanoparticles, the adsorption of double bonds is easier to break the O-O bond in single atomic Pt catalyst [49]. Due to the only one Pt-N coordination in Pt-$N_1$-C, the Pt atom shows a weaker association with *OOH so the -OH was easy to be desorbed to form $H_2O$ in second step. According to the free energy diagrams, the second step is the rate-limiting step and therefore we can obtain the catalytic order Pt-$N_1$-C > Pt-$N_2$-C > Pt-$N_3$-C > Pt-$N_4$-C, which is consistent with

![](./images/812470695526137857_7.jpg)

Fig. 4. (a) Tafel plots from LSV curves of Pt-NC-1.5%, Pt/C (20%). (b) Current density and mass activity at 0.70 V vs RHE of Pt-NC-1.5%, Pt-NC-2.0% and Pt/C (20%) for ORR. (c) Chronoamperometric curves for stability test with the Pt-NC-1.5% and Pt/C (20%) at 0.56 V for 8000 s in 0.1M KOH. (d) Methanol toxicity test with Pt-NC-1.5% and Pt/C (20%) at 0.56 V in 0.1M KOH

![](./images/812470695526137857_8.jpg)

Fig. 5. The simulated structures of (a) Pt-N₁-C, (b) Pt-N₂-C, (c) Pt-N₃-C, (d) Pt-N₄-C with different Pt-N coordination.

![](./images/812470695526137857_9.jpg)

Fig. 6. The proposed reaction pathways for reducing O₂ to H₂O on Pt-N₁-C catalyst in acidic environment and the free energy diagrams on different Pt-Nₓ-C catalysts (Inset).

the catalytic order Pt-NC-1.5% at 1100°C > Pt-NC-1.5% at 1000°C > Pt-NC-1.5% at 900°C > Pt-NC-1.5% at 800°C. The above order mainly depends on the strength of absorption between Pt atom and *OOH (or desorption of *O-OH) which can be modulated by the quantity of nearby N. In the third and fourth steps, the radical *O regenerates *OH and then produces another H₂O with adding H⁺ and e⁻. After above four steps, the single Ptᵟ⁺ atom begins a new catalytic cycle.

## 4. Conclusion

Temperature can effectively modulate the N coordination of metal atoms by controlling N loss, and high temperature induces high N loss which results in low N coordination. The model of Pt-Nₓ-C well demonstrates the efficient regulation of N coordination on the catalytic activity of oxygen reduction by controlling calcination temperature in this research. With the decrease of N coordination of Pt-Nₓ-C, the catalytic activity gradually increases, and the activity is better than the Pt/C (20%) catalyst, especially the

positive onset potential. Pt-N₁-C structure with the lowest N co-ordination shows the lowest energy barrier in oxygen reduction as demonstrated by DFT simulation. To sum up, the accurate "x" mod-ulation of M-Nₓ-C structure is a promising way for preparing catalysts with controllable catalytic properties but a potential question of metal atom aggregation should be considered when we design and modulate M-Nₓ-C structure of NC-SACs.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work was financially supported by the National Natural Science Foundation of China (Nos. 51572124 and 51702162), the Natural Science Foundation of Jiangsu Province (No. BK20180154 and BK20180490), the Fundamental Research Funds for the Central Universities (No. 30920130111003) and A Project Funded by the Priority Academic Program Development of Jiangsu Higher Education Institutions (PAPD, China).

## Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.jmst.2021.01.093.

## References

[1] C. Zhu, S. Fu, Q. Shi, D. Du, Y. Lin, Angew. Chem. Int. Ed. 56 (2017) 13944-13960.
[2] A. Wang, J. Li, T. Zhang, Nat. Rev. Chem. 2 (2018) 65-81.
[3] Y. Huang, X. Huang, M. Ma, C. Hu, F. Seidi, S. Yin, H. Xiao, J. Mater. Chem. C 9 (2021) 818-828.
[4] Y. Huang, A. Buffa, H. Deng, S. Sarkar, Y. Ouyang, X. Jiao, Q. Hao, D. Mandler, J. Power Sources 439 (2019) 227046.
[5] M. Fan, J. Cui, J. Wu, R. Vajtai, D. Sun, P.M. Ajayan, Small 16 (2020) 1906782.
[6] B. Bayatsarmadi, Y. Zheng, A. Vasileff, S.Z. Qiao, Small 13 (2017) 1700191.
[7] H. Han, Y. Noh, Y. Kim, S. Park, W. Yoon, D. Jang, S.M. Choi, Green Chem. 22 (2020) 71-84.
[8] H. Wu, Y. Cheng, B. Wang, Y. Wang, M. Wu, W. Li, B. Liu, S. Lu, J. Energy Chem. 57 (2021) 198-205.
[9] W. Li, Y. Zhao, Y. Liu, M. Sun, G.I.N. Waterhouse, B. Huang, K. Zhang, T. Zhang, S. Lu, Angew. Chem. Int. Ed. 60 (2020) 3290-3298.
[10] Z. Lin, G.H. Waller, Y. Liu, M. Liu, C.P. Wong, Nano Energy 2 (2013) 241-248.
[11] H. Han, S. Park, D. Jang, S. Lee, W.B. Kim, Chem. Sus. Chem. 13 (2020) 539-547.
[12] H. Han, Y. Noh, Y. Kim, W.S. Jung, S. Park, W.B. Kim, Nanoscale 11 (2019) 2423-2433.
[13] H. Song, Y. Li, L. Shang, Z. Tang, T. Zhang, S. Lu, Nano Energy 72 (2020) 104730.
[14] Y. Liu, X. Li, Q. Zhang, W. Li, Y. Xie, H. Liu, L. Shang, Z. Liu, Z. Chen, L. Gu, Z. Tang, T. Zhang, S. Lu, Angew. Chem. Int. Ed. 59 (2020) 1718-1726.
[15] X. Li, W. Bi, M. Chen, Y. Sun, H. Ju, W. Yan, J. Zhu, X. Wu, W. Chu, C. Wu, Y. Xie, J. Am. Chem. Soc. 139 (2017) 14889-14892.
[16] S. Wei, A. Li, J.C. Liu, Z. Li, W. Chen, Y. Gong, Q. Zhang, W.C. Cheong, Y. Wang, L. Zheng, H. Xiao, C. Chen, D. Wang, Q. Peng, L. Gu, X. Han, J. Li, Y. Li, Nat. Nanotechnol. 13 (2018) 856-861.
[17] C. Zhang, S. Yang, J. Wu, M. Liu, S. Yazdi, M. Ren, J. Sha, J. Zhong, K. Nie, A.S. Jalilov, Z. Li, H. Li, B.I. Yakobson, Q. Wu, E. Ringe, H. Xu, P.M. Ajayan, J.M. Tour, Adv. Energy Mater. 8 (2018) 1703487.
[18] Y. Pan, Y. Chen, K. Wu, Z. Chen, S. Liu, X. Cao, W.C. Cheong, T. Meng, J. Luo, L. Zheng, C. Liu, D. Wang, Q. Peng, J. Li, Chen C, Nat. Commun. 10 (2019) 4290.
[19] J. Li, S. Chen, N. Yang, M. Deng, S. Ibraheem, J. Deng, J. Li, L. Li, Z. Wei, Angew. Chem. Int. Ed. 58 (2019) 7035-7039.
[20] E. Luo, H. Zhang, X. Wang, L. Gao, L. Gong, T. Zhao, Z. Jin, J. Ge, Z. Jiang, C. Liu, W. Xing, Angew. Chem. Int. Ed. 58 (2019) 12469-12475.
[21] S. Zhou, L. Shang, Y. Zhao, R. Shi, G.I.N. Waterhouse, Y.C. Huang, L. Zheng, T. Zhang, Adv. Mater. 31 (2019) 1900509.
[22] Y.N. Gong, L. Jiao, Y. Qian, C.Y. Pan, L. Zheng, X. Cai, B. Liu, S.H. Yu, H.L. Jiang, Angew. Chem. Int. Ed. 59 (2020) 2705-2709.
[23] F. Li, Y. Bu, G.F. Han, H.J. Noh, S.J. Kim, I. Ahmad, Y. Lu, P. Zhang, H.Y. Jeong, Z. Fu, Q. Zhong, J.B. Bae, Nat. Commun. 10 (2019) 2623.
[24] J. Li, H. Zhang, W. Samarakoon, W. Shan, D.A. Cullen, S. Karakalos, M. Chen, D. Gu, K.L. More, G. Wang, Z. Feng, Z. Wang, G. Wu, Angew. Chem. Int. Ed. 58 (2019) 18971-18980.
[25] T. Li, J. Liu, Y. Song, F. Wang, ACS Catal. 8 (2018) 8450-8458.

[26] D. Liu, X. Li, S. Chen, H. Yan, C. Wang, C. Wu, Y.A. Haleem, S. Duan, J. Lu, B. Ge, P.M. Ajayan, Y. Luo, J. Jiang, L. Song, Nat. Energy 4 (2019) 512-518.
[27] X. Zhao, M. Yin, L. Ma, L. Liang, C. Liu, J. Liao, T. Lu, W. Xing, Energ Environ. Sci. 4 (2011) 2736-2753.
[28] X. Cui, S. Yang, X. Yan, J. Leng, S. Shuang, P.M. Ajayanl, Z. Zhang, Adv. Funct. Mater. 26 (2016) 5708-5717.
[29] S. Wang, S.P. Jiang, T.J. White, J. Guo, X. Wang, J. Phys. Chem. C 113 (2009) 18935-18945.
[30] X. Hai, X. Zhao, N. Guo, C. Yao, C. Chen, W. Liu, Y. Du, H. Yan, J. Li, Z. Chen, X. Li, Z. Li, H. Xu, P. Lyu, J. Zhang, M. Lin, C. Su, S.J. Pennycook, C. Zhang, S. Xi, J. Lu, ACS Catal. 10 (2020) 5862-5870.
[31] X. Wang, Z. Chen, X. Zhao, T. Yao, W. Chen, R. You, C. Zhao, G. Wu, J. Wang, W. Huang, J. Yang, X. Hong, S. Wei, Y. Wu, Y. Li, Angew. Chem. Int. Ed. 57 (2017) 1944-1948.
[32] J. Jones, H. Xiong, A.T. DeLaRiva, E.J. Peterson, H. Pham, S.R. Challa, G. Qi, S. Oh, M.H. Wiebenga, X.I. Pereira Hernández, Y. Wang, A.K. Datye, Science 353 (2016) 150.
[33] H. Zhang, S. Hwang, M. Wang, Z. Feng, S. Karakalos, L. Luo, Z. Qiao, X. Xie, C. Wang, D. Su, Y. Shao, G. Wu, J. Am. Chem. Soc. 139 (2017) 14143-14149.
[34] S.M. Unni, V.M. Dhavale, V.K. Pillai, S. Kurungot, J. Phys. Chem. C 114 (2010) 14654-14661.
[35] R. Liu, D. Wu, X. Feng, K. Müllen, Angew. Chem. Int. Ed. 49 (2010) 2565-2569.
[36] S. Yang, X. Feng, X. Wang, K. Müllen, Angew. Chem. Int. Ed. 50 (2011) 5339-5343.
[37] C. Zhang, J. Sha, H. Fei, M. Liu, S. Yazdi, J. Zhang, Q. Zhong, X. Zou, N. Zhao, H. Yu, Z. Jiang, E. Ringe, B.I. Yakobson, J. Dong, D. Chen, J.M. Tour, ACS Nano 11 (2017) 6930-6941.
[38] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169-11186.
[39] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758-1775.
[40] D. Deng, L. Yu, X. Pan, S. Wang, X. Chen, P. Hu, L. Sun, X. Bao, Chem. Commun. 47 (2011) 10016-10018.
[41] Y. Chen, S. Ji, W. Sun, W. Chen, J. Dong, J. Wen, J. Zhang, Z. Li, L. Zheng, C. Chen, Q. Peng, D. Wang, Y. Li, J. Am. Chem. Soc. 140 (2018) 7407-7410.
[42] Z. Liang, C. Qu, D. Xia, R. Zou, Q. Xu, Angew. Chem. Int. Ed. 57 (2018) 9604-9633.
[43] I. Kone, A. Xie, Y. Tang, Y. Chen, J. Liu, Y. Chen, Y. Sun, X. Yang, P. Wan, ACS Appl. Mater. Inter. 9 (2017) 20963-20973.
[44] L. Yang, X. Zeng, W. Wang, D. Cao, Adv. Funct. Mater. 28 (2017) 1704537.
[45] H. Zhang, H. Osgood, X. Xie, Y. Shao, G. Wu, Nano Energy 31 (2017) 331-350.
[46] X. Wang, H. Zhang, H. Lin, S. Gupta, C. Wang, Z. Tao, H. Fu, T. Wang, J. Zheng, G. Wu, X. Li, Nano Energy 25 (2016) 110-119.
[47] R. Ning, C. Ge, Q. Liu, J. Tian, A.M. Asiri, K.A. Alamry, C.M. Li, X. Sun, Carbon 78 (2014) 60-69.
[48] H. Fei, J. Dong, M.J. Arellano-Jiménez, G. Ye, N. Dong Kim, E.L.G. Samuel, Z. Peng, Z. Zhu, F. Qin, J. Bao, M.J. Yacaman, P.M. Ajayan, D. Chen, J.M. Tour, Nat. Commun. 6 (2015) 8668.
[49] J. Liu, M. Jiao, L. Lu, H.M. Barkholtz, Y. Li, Y. Wang, L. Jiang, Z. Wu, D.J. Liu, L. Zhuang, C. Ma, J. Zeng, B. Zhang, D. Su, P. Song, W. Xing, W. Xu, Y. Wang, Z. Jiang, G. Sun, Nat. Commun. 8 (2017) 15938.
[50] T. Sun, L. Xu, D. Wang, Y. Li, Nano Res. 12 (2019) 2067-2080.
[51] M. Xiao, J. Zhu, G. Li, N. Li, S. Li, Z.P. Cano, L. Ma, P. Cui, P. Xu, G. Jiang, H. Jin, S. Wang, T. Wu, J. Lu, A. Yu, D. Su, Z. Chen, Angew. Chem. Int. Ed. 58 (2019) 9640-9645.
[52] F. Cao, L. Zhang, Y. You, L. Zheng, J. Ren, X. Qu, Angew. Chem. Int. Ed. 59 (2020) 5108-5115.
[53] Y. Chen, S. Ji, Y. Wang, J. Dong, W. Chen, Z. Li, R. Shen, L. Zheng, Z. Zhuang, D. Wang, Y. Li, Angew. Chem. Int. Ed. 56 (2017) 6937-6941.
[54] Y. Han, Z. Wang, R. Xu, W. Zhang, W. Chen, L. Zheng, J. Zhang, J. Luo, K. Wu, Y. Zhu, C. Chen, Q. Peng, Q. Liu, P. Hu, D. Wang, Y. Li, Angew. Chem. Int. Ed. 57 (2018) 11262-11266.
[55] D. Zhang, W. Chen, Z. Li, Y. Chen, L. Zheng, Y. Gong, Q. Li, R. Shen, Y. Han, W.C. Cheong, L. Gu, Y. Li, Chem. Commun. 54 (2018) 4274-4277.
[56] Z. Zhang, J. Xiao, X.J. Chen, S. Yu, L. Yu, R. Si, Y. Wang, S. Wang, X. Meng, Y. Wang, Z.Q. Tian, D. Deng, Angew. Chem. Int. Ed. 57 (2018) 16339-16342.
[57] Y. Chen, S. Ji, W. Sun, Y. Lei, Q. Wang, A. Li, W. Chen, G. Zhou, Z. Zhang, Y. Wang, L. Zheng, Q. Zhang, L. Gu, X. Han, D. Wang, Y. Li, Angew. Chem. Int. Ed. 59 (2020) 1295-1301.
[58] Y. Qu, B. Chen, Z. Li, X. Duan, L. Wang, Y. Lin, T. Yuan, F. Zhou, Y. Hu, Z. Yang, C. Zhao, J. Wang, C. Zhao, Y. Hu, G. Wu, Q. Zhang, Q. Xu, B. Liu, P. Gao, R. You, W. Huang, L. Zheng, L. Gu, Y. Wu, Y. Li, J. Am. Chem. Soc. 141 (2019) 4505-4509.
[59] K. Jiang, B. Liu, M. Luo, S. Ning, M. Peng, Y. Zhao, Y.R. Lu, T.S. Chan, F.M.F. de Groot, Y. Tan, Nat. Commun. 10 (2019) 1743.
[60] M. Fan, Y. Huang, F. Yuan, Q. Hao, J. Yang, D. Sun, J. Power Sources 366 (2017) 143-150.
[61] L. Hao, S. Zhang, R. Liu, J. Ning, G. Zhang, L. Zhi, Adv. Mater. 27 (2015) 3190-3195.
[62] Y. Huang, K. Tang, F. Yuan, W. Zhang, B. Li, F. Seidi, H. Xiao, D. Sun, Carbon 168 (2020) 12-21.
[63] H. Yu, L. Shang, T. Bian, R. Shi, G.I.N. Waterhouse, Y. Zhao, C. Zhou, L.Z. Wu, C.H. Tung, T. Zhang, Adv. Mater. 28 (2016) 5080-5086.
[64] F. Pan, B. Li, W. Deng, Z. Du, Y. Gang, G. Wang, Y. Li, Appl. Catal. B 252 (2019) 240-249.
[65] F. Pan, B. Li, X. Xiang, G. Wang, Y. Li, ACS Catal 9 (2019) 2124-2133.
[66] S. Liu, M.G. White, P. Liu, J. Phys. Chem. C 120 (2016) 15288-15298.
