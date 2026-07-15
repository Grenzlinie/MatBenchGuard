RESEARCH ARTICLE

# Band gap engineered ternary semiconductor $\boldsymbol{Pb_xCd_{1-x}S}$: Nanoparticle-sensitized solar cells with an efficiency of 8.5% under 1% sun—A combined theoretical and experimental study

Patsorn Boon-on¹ | Shang-Wei Lien² | Tay-Rong Chang²,³,⁴ | Jen-Bin Shi⁵ | Ming-Way Lee¹

¹Institute of Nanoscience and Department of of Physics, National Chung Hsing University, Taichung, 402, Taiwan
²Department of Physics, National Cheng Kung University, Tainan, 701, Taiwan
³Center for Quantum Frontiers of Research & Technology (QFort), National Cheng Kung University Tainan, 701, Taiwan
⁴Physics Division, National Center for Theoretical Sciences, Hsinchu, 30013, Taiwan
⁵Department of Electronic Engineering, Feng Chia University, Taichung, 40724, Taiwan

Correspondence
Ming-Way Lee, Department of Physics, National Cheng Kung University, Tainan 701, Taiwan.
Email: mwl@phys.nchu.edu.tw

Funding information
Ministry of Science and Technology (MOST), Grant/Award Numbers: MOST107-2627-E-006-001, MOST108-2112-M-005-002; Young Scholar Fellowship Program from the Ministry of Science and Technology (MOST), Grant/Award Number: MOST108-2636-M-006-002

## Abstract
We report the synthesis and photovoltaic properties of a ternary metal sulfide alloyed semiconductor $Pb_xCd_{1-x}S$ prepared by the two-stage sequential ionic layer adsorption reaction. The synthesized $Pb_xCd_{1-x}S$ nanoparticles (NPs) retain the hexagonal structure of the CdS host with Pb substituting a fraction of the Cd atom (x = 0-0.17). Band structures of $Pb_xCd_{1-x}S$ with various Pb contents x were calculated using the complementary density functional theory (DFT) method. Optical, quantum efficiency, cyclic voltammetry measurements, and band structure calculation revealed that the band gap of $Pb_xCd_{1-x}S$ decreased with increasing x, resulting in an increased optical absorption band from 500 to 720 nm (1.73-2.44 eV) for x = 0 to 0.17. Solid-state $Pb_xCd_{1-x}S$ semiconductor nanoparticle-sensitized solar cells (NSSCs) were fabricated from the synthesized NPs using spiro-OMeTAD as the hole-transporting material. The best $Pb_{0.05}Cd_{0.95}S$ cell yielded a power conversion efficiency (PCE) of 3.67%, a $V_{oc}$ of 0.70 V, and a fill factor (FF) of 62.8% under 1 sun. The PCE increased to 5.93% under a reduced light intensity of 0.1 sun and further increased to 8.48% under 0.01 sun. The external quantum efficiency (EQE) spectrum covers the spectral range of 300 to 730 nm with a maximal EQE of 82% at $\lambda$ = 580 nm. The PCE over 8% can be categorized into a high-efficiency NSSCs. In addition, the $V_{oc}$ of 0.70 V is a relatively high $V_{oc}$ among all NSSCs. The high PCE and $V_{oc}$ suggest that $Pb_xCd_{1-x}S$ has potential to be an efficient solar absorber.

## KEYWORDS
cadmium sulfide, lead cadmium sulfide, nanoparticle, quantum dot, sensitizer, SILAR, solar cell

---

## 1 | INTRODUCTION

Semiconductor nanoparticle-sensitized solar cells (NSSCs) are a potential low-cost alternative to Si-based photovoltaic devices. A NSSC adopts the basic architecture of a dye-sensitized solar cell in which a layer of semiconductor nanoparticles (NPs) is coated over a mesoporous $TiO_2$ electrode. The employment of semiconductor NP sensitizers has the advantages of tunable band gap due to the quantum size effect, large optical absorption coefficient, and multiple electron-hole pair generation by a single photon.¹⁻³ To achieve the Shockley-Queisser efficiency limit, the solar absorber material should have an ideal band gap of $E_g$ approximately 1.1 to 1.4 eV.⁴ To date, the most widely investigated semiconductor sensitizers have been the binary metal chalcogenides such as CdS, CdSe, PbS, PbSe, and $Ag_2S$.⁵⁻⁹ The power conversion efficiencies (PCEs) of NSSCs based on single-layered binary NPs are low (typically approximately 2%-3%) due to their relatively large $E_g$s and, hence, small light-harvesting ranges.¹⁰,¹¹ A strategy to increase the

optical absorption range is to combine two binary semiconductors with different band gaps. Cosensitized NSSCs such as CdS/CdSesignificantly improved their PCE to approximately $5\%$ to $6\%.^{10,11}$ The photovoltaic performance of various single-layered and double-layered NSSCs have been presented and compared in several review papers. $^{10-13}$ In general, a NSSC achieving a PCE of approximately $6\%$ to $8\%$ can be categorized into a high-efficiency NSSC. PCEs higher than $8\%$ usually require special techniques such asdouble passivation coatings of $ZnS/TiO_{2}$ or amorphous $TiO_{2}/ZnS/$  $TiO_{2}$ to reduce carrier recombination. $^{14,15}$

In addition to the double-layered cosensitizer approach, an alternative strategy to increase the adsorption range is to tune the band gap $E_{g}$ of a semiconductor. The $E_{g}$ of a ternary or quaternary semiconductor can be tuned by several approaches such as varying the NP size, changing material composition, and doping impurities. Among these approaches, varying material composition has been shown to be a highly successful method. The material composition of a ternary alloyed semiconductor, such as a metal sulfide $A_{x}M_{1-x}S$, can be controlled by varying (a) the cation composition,(b) the anionic composition, and (c) the cationic-anionic composi- tion. As an example, the optical absorption range of the cation- alloyed semiconductor $Zn_{x}Cd_{1-x}S$ could be increased from 391 to474 nm by controlling the ratio of the two cationic elements Zn and $Cd^{16}$ The $E_{g}$ of $Sn_{x}Sb_{2-y}S_{3}$ is tunable from 1.5 to 2.0 eV byvarying the $Sn/Sb$ contents. $^{17}$ In the case of anionic alloys, the $E_{g}$  of $CdS_{x}Se_{1-x}$ is tunable from 500 to 650 nm by varying the compositions of two anionic elements S and Se. $^{18}$ The large absorption ranges in anionic alloys $CdSe_{x}Te_{1-x}$ resulted in high PCEs ofapproximately $8\%$ to $9\%.^{15,19,20}$

CdS is one of the most extensively studied binary semiconduc- tor material in NSSCs because the material is easy to grow. It has a relatively large $E_{g}$ of 2.5 eV and a small absorption range of300 to $500 nm^{21}$ The PCE of CdS NSSCs is low (typically approximately $2\%$ ) due to the small absorption range. $^{10,11}$ However, thelarge $E_{g}$ produces an open-circuit voltage $V_{oc}$ of approximately 0.5 to 0.6 eV, which is a relatively large $V_{oc}$ among all NP materials. $^{10,11}$ Motivated by the high $V_{oc}$ , this work aims to develop a CdS-based ternary alloyed semiconductor that would produce a broader optical absorption range and retain the high $V_{oc}$ value. Here, the ternary alloyed semiconductor $Pb_{x}Cd_{1-x}S$ is prepared by substituting part of the cationic element Cd in CdS with Pb atoms. From a theoretical point of view, the $E_{g}$ of a semiconductor is inversely proportional to the lattice constant. The substitution of $Cd^{2+}$ ion $(0.95 \AA)$ by the larger $Pb^{2+}$ ion $(1.19 \AA)$ is predicted to produce a ternary $Pb_{x}Cd_{1-x}S$ semiconductor with a reduced $E_{g}$ . Vacuum coevaporation of PbS and CdS powder produced thin films of a mixture of two binary PbS/CdS phases. $^{22}$ Chemical solution growth produced films of PbS-CdS composite with weak evidence of formation of the ternary $Pb_{x}Cd_{1-x}S$ phase. $^{23}$ The results in Nasir and Naji $^{22}$ and Mohammed et $al^{23}$ indicate that the synthesis of the ternary $Pb_{x}Cd_{1-x}S$ phase by addition of PbS into CdS is a difficult experiment due to the thermodynamic instability of (Pb,Cd)S solution. Recently, liquid-junction $Pb_{x}Cd_{1-x}S$ NSSCs have been reported to yield a high PCE of $5.3\%.^{24}$ A second work on $Pb_{x}Cd_{1-x}S$ NSSCs reported a PCE of $3.2\%$ (X-ray diffraction [XRD]of $Pb_{x}Cd_{1-x}S$ not presented). $^{25}$ A different-structured but relevant NSSC based on binary core-shell PbS/CdS NP cosensitizer yieldeda high PCE of $7.19\%.^{26}$

In this work, $Pb_{x}Cd_{1-x}S$ NPs were synthesized using the two stage sequential ionic layer adsorption reaction (SILAR). The band gapwas tuned by controlling the Pb content x. Solid-state $Pb_{x}Cd_{1-x}S$  NSSCs were fabricated from the synthesized NPs. The dependences of photovoltaic performance on SILAR cycles and sun intensity are investigated. The changes of band gap with Pb content x are studied using optical spectra, external quantum efficiency (EQE) spectra and cyclic voltammetry. The incorporation of Pb into CdS significantly increased the light-harvesting range. The $Pb_{x}Cd_{1-x}S$ NSSC achieves a PCE comparable with that of other high-performance NSSCs reported to date.

## 2 | EXPERIMENTAL

Figure 1A shows a schematic diagram of a solid-state $Pb_{x}Cd_{1-x}S$  NSSC consisting of a $TiO_{2}$ blocking layer, a mesoporous $TiO_{2}$ elec trode layer, a $Pb_{x}Cd_{1-x}S$ light absorber layer, a solid electrolyte layer, and a gold electrode. The preparation process for each component is described below.

### 2.1 | TiO₂ blocking layer

An fluorine-doped tin oxide (FTO) glass substrate (Pilkington, $7 \Omega$ square $^{-1}$ ) was first patterned into a solid-state solar cell configu ration by etching with Zn powder in a 2M HCl solution, followed by cleaning in acetone, methanol, and deionized (DI) water, respectively. A $TiO_{2}$ blocking layer was prepared by hot spraying a 0.2M titanium diisoproxide bis(acetylacetonate) $(C_{16}H_{28}O_{6}Ti)$ ethanol solution(vol. ratio: 1:9) onto the prepatterned FTO substrate placed on a500°C hot plate for 10 minutes. A total number of 15 hot spray cycles typically produced a blocking layer of thickness approximately 120 nm(Figure 1B).

### 2.2 | Mesoporous TiO₂ electrode

The mesoporous $TiO_{2}$ electrode $(mp-TiO_{2})$ layer was prepared by the spin coating method. Anatase $TiO_{2}$ paste (Dyesol 30NR-T, particle size $\approx 30 nm$ ) was dissolved into a $95\%$ ethanol solution with a mass ratio of $1: 1.5 ; 75 \mu L$ of the diluted $TiO_{2}$ paste solution was dripped onto FTO glass then spun at 2500 rpm for30 seconds. The process was repeated twice. Finally, the $TiO_{2}$  paste-coated FTO was heated $500^{\circ}C$ for 30 minutes. The finalthickness of the $mp-TiO_{2}$ layer is typically approximately $1 \mu m$ (Figure 1B).

![](./images/812687189749006338_1.jpg)

FIGURE 1 (A) Schematic diagram of a solid-state $Pb_xCd_{1-x}S$ nanoparticle-sensitized solar cell (NSSC) and (B) scanning electron microscopy (SEM) cross-sectional image of a fabricated $Pb_xCd_{1-x}S$ NSSC with thickness of each layer labelled [Colour figure can be viewed at wileyonlinelibrary.com]

## 2.3 | Synthesis of $Pb_xCd_{1-x}S$ NPs

$Pb_xCd_{1-x}S$ NPs were synthesized using a two-stage SILAR process. First, a layer of PbS binary NPs was grown on a prepared $TiO_2$ electrode. Second, a layer of CdS was grown on top of the PbS NPs. Post annealing transformed the PbS/CdS double-layered structure into the ternary alloyed $Pb_xCd_{1-x}S$ phase. A PbS SILAR cycle consisted of subsequent immersion of a mp-$TiO_2$ electrode into a 0.1M, $25^\circ$C $PbNO_3$ aqueous solution for 30 seconds, rinsed in DI water, then immersed into a 0.1M, $25^\circ$C $Na_2S.9H_2O$ methanol solution for 30 seconds, followed by rinsing in methanol and drying at $60^\circ$C in air. This SILAR process produced PbS NPs coated on $TiO_2$ particles. The number of PbS SILAR cycles was repeated $n$ times to obtain the desired amount of PbS material (referred to as PbS($n$)). A CdS SILAR cycle consisted of immersing the PbS-coated $TiO_2$ electrode into a 0.1M, $25^\circ$C Cd $(NO_3)_2$ ethanol solution for 2 minutes, rinsing in ethanol, then immersed into a 0.1M, $25^\circ$C $Na_2S.9H_2O$ methanol solution for 2.5 minutes, finished by rinsing in methanol and drying as above. The number of CdS SILAR cycles was repeated for seven times (referred to as CdS(7)). The PbS($n$)/CdS(7) doubled-layered electrode was transformed into the ternary $Pb_xCd_{1-x}S$ semiconductor by annealing in a $N_2$ gas-flowing tube furnace at $250^\circ$C for 20 minutes.

## 2.4 | Solar cell fabrication

2,2',7,7'-Tetrakis(N,N-di-pmethoxyphenyl-amine)-9,9'-spirobifluorene (Spiro-OMeTAD, Merck) was used as the hole transport material (HTM) for solid-state $Pb_xCd_{1-x}S$ NSSCs. The HTM solution consisted of 0.315M Spiro-OMeTAD, 0.167M of 4-tertbutyl pyridine, and 28.2mM of lithium-bis(trifluoromethane sulfonyl)imide salt. The HTM solution was filled into the porous spaces of a mp-$TiO_2$ electrode by dropping the solution (70 $\mu$L) on the $Pb_xCd_{1-x}S$-coated $TiO_2$ electrode, let to sit still for 60 seconds, then spun at 2000 rpm for 30 seconds to allow full penetration of the electrolyte. The process not only filled the HTM into the $TiO_2$ electrode but also coated a layer of Spiro-OMeTAD HTM material (thickness of approximately 100-200 nm) on top of the mp-$TiO_2$ electrode. The assembly was finished by sputtering an Au film of thickness approximately 100 nm on top of the HTM layer. Figure 1B shows a cross-sectional scanning electron microscopy (SEM) image of a completed solar cell with thickness for each layer: 120 nm ($TiO_2$ blocking layer), 922 nm (mp-$TiO_2$/Pb$_x$Cd$_{1-x}$S NP layer), and 178 nm (spiro-OMeTAD layer).

## 2.5 | Material, optical, and photovoltaic characterization

The quality and morphology of the synthesized material were characterized by X-ray energy dispersive spectroscopy (EDS), XRD, transmission electron microscopy (TEM), X-ray photoelectron spectroscopy (XPS), optical absorption spectra, and cyclic voltammetry (CV). EDS was measured using a JEOL JSM-7800F Prime Schottky field emission scanning electron microscope operating at 15 kV. XRD patterns were measured using a PANalytical X'Pert Pro MRD diffractometer. TEM images were recorded using a JEOL JEM-2010 Scanning Image Observation microscope operating at 200 kV. XPS was measured using a ULVAC-PHI 5000 Versa Probe electron spectroscope for chemical analysis with Ar-heated treatment. Optical absorption spectra were recorded using a Hitachi 2800A spectrophotometer. CV curves were measured using a Bio-Logic SAS SP-150 with a maximum power of 65 W and a scan rate of 100 mV/s. The supporting electrolyte was 0.1M KCl in DI water. Photovoltaic current-voltage (I-V) curves were recorded using a Keithley 2400 source meter illuminated with a 150-W Oriel Xe lamp under $100-mW/cm^2$ light intensity. An Oriel filter was used to simulate the AM 1.5 solar spectrum. The incident sun intensity was tunable from 1 to 0.1 sun by inserting metal meshes in the light path. EQE spectra were measured using an Acton monochromator with a 250-W tungsten-halogen lamp (without white light biasing). A metal mask placed above the solar cell defined the active area to be 3 mm × 3 mm.

## 2.6 | Theoretical calculation method

The electronic structures were computed using the projector augmented wave method$^{27,28}$ as implemented in the VASP package$^{29}$ within the generalized gradient approximation (GGA) scheme.$^{30}$ The

spin-orbit coupling (SOC) was included self-consistently in the calculations of electronic structures with k-point mesh $7 \times 7 \times 5$. We performed calculations with the Heyd-Scuseria-Ernzerhof (HSE) hybrid function $^{31,32}$ for an accurate estimate of the energy band gap. The experimental structural parameters were employed (Table S2). In order to systematically calculate the band structure with finite Pb doping, we constructed a tight-binding Hamiltonian for both CdS and PbS, where the tight-binding model matrix elements were calculated by projecting onto the Wannier orbitals, $^{33,34}$ which used the VASP2WANNIER90 interface. $^{35}$ We used Cd (Pb) $s$ and $p$ orbitals and $S$ $p$ orbitals to construct Wannier functions without using the maximizing localization procedure. The electronic structure of the samples with finite dopings was calculated by a linear interpolation of tight-binding model matrix elements of CdS and PbS. Since tight-binding parameters contained all important information such as lattice constants and atomic bonding strength, an interpolation presumably covered all systematic changes of the electronic structure between the two end points. This approach has been implemented in the semiconductor-like topological materials. $^{36,37}$

## 3 | RESULTS AND DISCUSSION

### 3.1 | Theoretical results

To understand the nature of the evolution of the band structure as a function of Pb doping, we performed first-principle calculations on the bulk band structure of $\text{Pb}_x\text{Cd}_{1-x}\text{S}$ based on GGA method with HSE correction, as shown in Figure 2. In Figure 2A, we show the bulk band structure of the pristine CdS along important high symmetry directions. The bulk Brillouin zone (BZ) is shown in Figure 2D, where high symmetry points are noted. Our GGA + HSE reveals an insulating ground state with 2.3-eV direct energy band gap $(E_{\text{g}})$ at $\Gamma$ point, consistent quite well with our experimental measurements. We also calculated the band structure of PbS by assuming that it is in the same crystal structure. As shown in Figure 2C, the general trend is that the bands are pushed closer and shift below the Fermi level $E_{\text{F}}$. For example, in PdS, the labelled b1 and b2 bands (correspond to the topmost of valence band and the bottom of conduction band in CdS, respectively) touch together and shift about $-3$ eV below $E_{\text{F}}$. Figure 2E shows the evolution of the band structure around $E_{\text{F}}$ as a function of

![](./images/812687189749006338_2.jpg)

FIGURE 2 (A) Bulk band structure of the pristine CdS with the inclusion of spin-orbit coupling plus Heyd-Scuseria-Ernzerhof (HSE) correction. (B) The same as (A) but zoom-in around $E_{\text{F}}$. (C) Bulk band structure of PbS by assuming that it has the same crystal structure as CdS. (D) The bulk Brillouin zone (BZ) of CdS. (E) The evolution of the band structure around $E_{\text{F}}$ as a function of Pb doping. (F) The doping dependence of the band gap $E_{\text{g}}$ at $\Gamma$ point. The blue diamond and blue star symbols correspond to the theoretical results and our experimental measurements, respectively. The red dots indicate the band gap value as function of lattice constants of pristine CdS [Colour figure can be viewed at wileyonlinelibrary.com]

Pb doping. Our calculation shows that the energy band gap decreases rapidly and the binding energy increases simultaneously with increas- ing Pb doping concentration. Figure 2F shows the doping dependence of the band gap value at the $\Gamma$ point. The blue diamond and blue star symbols correspond to the first-principle calculated results and our experimental measurements, respectively. It can be seen that the cal- culated and measured results show a consistent trend for Pb doping concentration below 10%. The deviation of an energy offset between the theory and experiment in 17% Pb doping may resulted from the theoretical limitations. This is because we employed simple linear interpolation method for simulating complicated doping effect. There- fore, it would not be surprising that the scope of application of this method is in low doping region. It is also noteworthy that the lattice effect is not the major effect that modifies the energy band gap. The band gap decreases slightly as extending the lattice constants of pris- tine CdS (red dots in Figure 2F). The significant band structure evolu- tion of $Pb_{x} Cd_{1-x} S$ might result from the different types of orbital bonding between Cd-S and Pb-S. For pristine CdS, two electrons transfer from the Cd 5s orbital to S 3p orbital forming the Cd-S ionic bond, consequently pushing the Cd s bands and pulling the S p bands above and below $E_{F}$ , respectively. Contrary to Cd(5s)-S(3p), PdS exhibits different bonding behavior. The Pb 6p orbital hybridizes strongly with S 3p orbital and dominates around $E_{F}$ , while Pb 6 s bands lies around -8 eV below $E_{F}$ . Since the bandwidth of PdS is signifi cantly larger than CdS, the Pb doping in CdS will tend to pull down the conduction bands to increase the bandwidth of the whole system, resulting in the energy band gap decrease.

## 3.2 | Energy dispersive spectroscopy

The elemental compositions of the alloyed $Pb_{x} Cd_{1-x} S$ NPs are expected to vary with the number of SILAR cycles. Therefore, it is important first to determine the elemental compositions of each $Pb_{x} Cd_{1-x} S$ sample. Figure S1 displays the EDS spectra of five $Pb_{x} Cd_{1-x} S$ samples prepared with various numbers of PbS SILAR cycles n = 0 to 4 (the number of CdS SILAR cycles was all fixed at7, Supporting Information). Table 1 lists the Pb, Cd, and S atomic percentages of the five samples. As the number of PbS SILAR cycles increased from 0 to 4, the Pb atomic percentage increased from 0% to8.5%, while the Cd atomic percentage decreased from 51.7% to45.1%. Meanwhile, the S atomic percentage remained approximately the same. The continued increase in the Pb composition x with increasing PbS SILAR cycles n indicates that Pb atoms have been added to the synthesized material. Based on the EDS data in Table 1, the chemical formula of the five samples can be expressed as CdS, $Pb_{0.02} Cd_{0.98} S, Pb_{0.05} Cd_{0.95} S, Pb_{0.10} Cd_{0.90} S$ , and $Pb_{0.17} Cd_{0.83} S$ , respec tively (determination of the accurate chemical formula is beyond the scope of this paper focusing on photovoltaics).

TABLE 1 EDS data of $Pb_{x} Cd_{1-x} S$ NPs prepared with different number of PbS(n) SILAR cycles

<table>
<thead>
<tr>
<th rowspan="2">SILAR Cycles</th>
<th colspan="3">Atomic, %</th>
<th rowspan="2">Pb:Cd Ratio</th>
<th rowspan="2">Pb Content x</th>
</tr>
<tr>
<th>Pb</th>
<th>Cd</th>
<th>S</th>
</tr>
</thead>
<tbody>
<tr>
<td>PbS(0)/CdS(7)</td>
<td>0</td>
<td>55.7</td>
<td>44.3</td>
<td>-</td>
<td>0</td>
</tr>
<tr>
<td>PbS(1)/CdS(7)</td>
<td>1.2</td>
<td>51.7</td>
<td>47.2</td>
<td>1:43</td>
<td>0.02</td>
</tr>
<tr>
<td>PbS(2)/CdS(7)</td>
<td>2.7</td>
<td>51.1</td>
<td>46.2</td>
<td>1:19</td>
<td>0.05</td>
</tr>
<tr>
<td>PbS(3)/CdS(7)</td>
<td>5.2</td>
<td>46.0</td>
<td>48.9</td>
<td>1:9</td>
<td>0.10</td>
</tr>
<tr>
<td>PbS(4)/CdS(7)</td>
<td>8.5</td>
<td>45.1</td>
<td>46.4</td>
<td>1:5</td>
<td>0.17</td>
</tr>
</tbody>
</table>

Note. The number of CdS SILAR cycles was fixed at 7. Each atomic percentage data represents the average of data from three different sample positions.
Abbreviation: EDS, energy dispersive spectroscopy; NP, nanoparticle; SILAR, sequential ionic layer adsorption reaction.

## 3.3 | X-ray diffraction

Figure 3A displays the XRD patterns of the host CdS (top spectrum) along with four Pb-incorporated $Pb_{x} Cd_{1-x} S$ samples with various x. The CdS host shows the hexagonal structure ((hkl) indices labelled in the figure), in agreement with the literature (JCPDS 00-041-1049). The four $Pb_{x} Cd_{1-x} S$ samples exhibit the same XRD peaks with that of the CdS host. However, the angles are shifted slightly to lower angles relative to CdS. The results indicate that the $Pb_{x} Cd_{1-x} S$ samples retain the hexagonal structure of the CdS host. For comparison, the XRD peaks of pure PbS are displayed in the bottom panel (JCPDS 01-078-1055). As seen, the $Pb_{x} Cd_{1-x} S$ samples do not contain the peaks asso ciated with PbS, indicating that the synthesized $Pb_{x} Cd_{1-x} S$ does not contain the PbS phase (within the limit of XRD sensitivity). Figure 3B shows the enlarged $2 \theta$ angles of the (110) peak for five samples. The angle decreases from 44.04 (x = 0) to 43.88 (x = 0.02), 43.69(x = 0.05), 43.54 (x = 0.10), and 43.33° (x = 0.17). A similar downshift in angle with increasing x is also observed in the (002) peak (see Table S1). A downshift in the XRD angle indicates a lattice expansion. This result is explained in terms of the size effect of cationic ion. The ionic radius of $Pb^{2+}(1.19 \AA)$ is significantly larger than that $(0.95 \AA)$ of $Cd^{2+}$ ion. The substitution of Cd by Pb results in an expansion in lat tice. The lattice constants of the five samples were calculated from the XRD spectra. Figure 3C,D shows the dependence of the lattice constants a and c on Pb content x. Table S2 lists the calculated lattice constants of the five samples. As seen in the figures, the lattice con- stants a and c both increase linearly with x. The dependence can be expressed by the following equations:

$$a=0.2232x+4.1408,$$

$$c=0.8097x+6.71346.$$

## 3.4 | Transmission electron microscopy

Figure 4A shows a TEM image of a bare $TiO_{2}$ film. The $TiO_{2}$ particles are mostly long and rectangular in shape with sizes of approximately30 nm. Figure 4B shows an image of the host CdS particles, marked as

![](./images/812687189749006338_3.jpg)

FIGURE 3 (A) X-ray diffraction (XRD) patterns of $Pb_xCd_{1-x}S$ nanoparticles (NPs) with various Pb content $x$, (B) enlarged XRD (110) peak of $Pb_xCd_{1-x}S$ NPs with various Pb content $x$, (C) lattice parameter $a$ as a function of $x$, and (D) lattice parameter $c$ as a function of $x$ [Colour figure can be viewed at wileyonlinelibrary.com]

red arrows, coated on a $TiO_2$ film. The CdS NPs have an average size of 12 nm. The inset shows lattice fringes of the CdS NP. The interplane spacing $d$ of 0.312 nm can be assigned to the (101) plane of CdS. Figure 4C shows a TEM image of $Pb_xCd_{1-x}S$ NPs ($x = 0.05$) coated on a $TiO_2$ film. The $Pb_xCd_{1-x}S$ NPs can be seen to be randomly distributed on $TiO_2$ particles without observable aggregation. The NPs have sizes in the range of 15 to 20 nm and an average diameter of 16 nm. The interplane spacing $d$ (inset) of 0.326 nm is slightly larger than that of the CdS host. An increased $d$ indicates an expansion in the lattice, in agreement with the XRD data. Figure 4D show a simulation and analysis of selected area electron diffraction (SAED) pattern of $Pb_{0.05}Cd_{0.95}S$ NPs. The pattern (with (hkl) indices labelled) matches well with the hexagonal structure of the CdS host, providing an additional support of the XRD data shown in Figure 3.

## 3.5 | X-ray photoelectron spectroscopy

The elemental composition and oxidation state of the $Pb_xCd_{1-x}S$ nanocrystal (NC) sample with the best photovoltaic performance ($x = 0.05$) were investigated by XPS. Figure 5A shows a typical XPS survey spectra and presence of Pb, Cd, S, Ti, and O elements. The high-resolution spectrum of lead, shown in Figure 5B, shows two strong peaks at binding energy of 137.8 eV for Pb $4f_{7/2}$ and 142.7 eV for Pb $4f_{5/2}$, respectively, $^{38}$ confirming presence of the divalent lead $Pb^{2+}$ state in the $Pb_xCd_{1-x}S$ phase. Figure 5C shows the binding energy of 404.7 eV for Cd $3d_{5/2}$ and 411.4 eV for Cd $3d_{3/2}$ with an energy difference of 6.7 eV, indicating that cadmium is in +2 oxidation state in the $Pb_{0.05}Cd_{0.95}S$ sample. $^{39}$ Figure 5D shows a large peak at 162.2 eV and a small peak at 161 eV corresponding to S $2p_{3/2}$ and S $2p_{1/2}$ respectively, which is indicative that sulfur exists as a divalent $S^{2-}$ anion in the $Pb_{0.05}Cd_{0.95}S$ sample. $^{40}$

## 3.6 | Optical spectra

Figure 6 shows the optical spectra of five $Pb_xCd_{1-x}S$ samples with various numbers of PbS SILAR cycles $n$ (CdS SILAR cycles fixed at 7). Note that the Pb content $x$ changes with PbS SILAR cycles $n$, as shown in Table 1. The transmission $T(\lambda)$ (Figure 6A) were measured by taking the ratio of $I_{Pb_xCd_{1-x}S}/I_{TiO_2}$, where $I_{Pb_xCd_{1-x}S}$ is the light intensity transmitted through the $Pb_xCd_{1-x}S$ NPs and $I_{TiO_2}$ is the light intensity transmitted through the $TiO_2$ background. The $T(\lambda)$ value at a given wavelength decreases with increasing PbS SILAR cycles $n$ and PbS content $x$, indicating increasing light absorption. Figure 6B shows the absorbance $A(\lambda) = -\log_{10}T(\lambda)$ of the five samples. The absorbance A also increases with increasing PbS SILAR cycles $n$, which again indicates higher absorption. The increase in light absorption in samples with high PbS SILAR cycles $n$ can be attributed to (a) an increase in

![](./images/812687189749006338_4.jpg)

the amount of semiconductor material as more SILAR cycles were performed and (b) a lowering in band gap $E_{\text{g}}$, which results in a larger optical absorption coefficient. Figure 6C displays the Tauc plots $(h\nu)^2$ vs $h\nu$ where $h$ is the Plank's constant and $\nu$ is photon energy. The intercept to x-axis can be used to estimate the energy gap $E_{\text{g}}$. Figure 6D shows the dependence of $E_{\text{g}}$ on x. Table 2 lists the data. As seen in the figure and table, the band gap decreases monotonically with increasing SILAR cycles $n$: $E_{\text{g}}$ = 2.40 ($n$ = 0), 2.17 ($n$ = 1), 2.04 ($n$ = 2), 1.88 ($n$ = 3), and 1.78 ($n$ = 4). The incorporation of Pb into CdS leads to a reduction in $E_{\text{g}}$ from 2.40 to 1.78 eV. A second possible cause of $E_{\text{g}}$ reduction is the quantum size effect. The size of $\text{Pb}_{x}\text{Cd}_{1-x}\text{S}$ particles increases with increasing SILAR cycles $n$. A larger NP would exhibit a lower $E_{\text{g}}$, if the quantum size effect is important. The exciton Bohr radius of CdS is approximately 3 nm.⁴¹ According to the TEM results, the average diameter of $\text{Pb}_{x}\text{Cd}_{1-x}\text{S}$ NPs is approximately 16 nm, which is significantly larger than the Bohr radius of CdS. The much larger $\text{Pb}_{x}\text{Cd}_{1-x}\text{S}$ particle size suggests that the quantum size effect in $\text{Pb}_{x}\text{Cd}_{1-x}\text{S}$ is weak and unimportant. We will address further on the issue of $E_{\text{g}}$ lowering in the section of CV below. The top panel in Figure 6 shows pictures of the five $\text{Pb}_{x}\text{Cd}_{1-x}\text{S}$ samples with various number of PbS SILAR cycles $n$. The color changes continuously from yellow to light brown with increasing PbS SILAR cycles, indicating a gradual decrease in $E_{\text{g}}$ as the Pb content x increases. The pictures provide an additional support to the optical $E_{\text{g}}$ data shown in Figure 6D.

### 3.7 | CV measurements

The dependence of $E_{\text{g}}$ on Pb content x was further investigated by CV measurements. The conduction band minimum $E_{\text{CB}}$ and valence band maximum $E_{\text{VB}}$ are also important parameters for a solar material because they can affect the charge transport in a solar cell. Here, the relative positions of $E_{\text{CB}}$ and $E_{\text{VB}}$ were also studied by CV measurements. Figure 7A shows CV curves of five $\text{Pb}_{x}\text{Cd}_{1-x}\text{S}$ samples. The peak at 1.02 eV is attributed to the oxidation process of PbS. The energy levels of $E_{\text{CB}}$ and $E_{\text{VB}}$ were calculated using the equations below⁴²:

$$
E_{\text{CB}} = -E_{a} = -e\left(E_{\text{onset}}^{\text{red}} + 4.71\right)\text{ eV},
$$

$$
E_{\text{VB}} = -E_{c} = -e\left(E_{\text{onset}}^{\text{ox}} + 4.71\right)\text{ eV},
$$

where $E_{\text{onset}}^{\text{red}}$ and $E_{\text{onset}}^{\text{ox}}$ is the energy of reduction reaction and oxidation reaction with step onset, respectively. The calculated values of

![](./images/812687189749006338_5.jpg)

FIGURE 5 X-ray photoelectron spectroscopy (XPS) analysis of $Pb_{0.05}Cd_{0.95}S$ nanoparticles (NPs) (A) survey spectrum and deconvoluted spectra of (B) Pb 4f, (C) Cd 3d, and (D) S 2p, respectively [Colour figure can be viewed at wileyonlinelibrary.com]

$E_g$, $E_{CB}$, and $E_{VB}$ of the five samples are listed in Table 2. The associated energy level diagrams are plotted in Figure 7B. The CV-measured $E_g$ decreased with increasing Pb content $x$, in agreement with the optimal results. In addition, the $E_{CB}$ energy level moves down, whereas $E_{VB}$ moves up with increasing $x$. In order to have efficient electron injection, the $E_{CB}$ of $Pb_xCd_{1-x}S$ should be higher than that of $TiO_2$ ($-4.2$ eV). According to Table 2, the $E_{CB}$ of the $Pb_xCd_{1-x}S$ samples with high $x$ are close to the $E_{CB}$ of $TiO_2$ ($E_{CB} = -4.20$ ($x = 0.10$) and $-4.25$ eV ($x = 0.17$)). This implies that the electron injection in these two $Pb_xCd_{1-x}S$ samples would be less efficient, leading to lower performance, which is exactly what the photovoltaic data revealed in the discussion below.

### 3.8 | Photovoltaic performance

The photovoltaic performance of a NSSC prepared by the SILAR method is highly sensitive to the number of SILAR cycles. A SILAR number too high or too low both result in poor performance. Figure 8A displays the $I$-$V$ curves of five $Pb_xCd_{1-x}S$ NSSCs with various numbers of PbS SILAR cycles $n = 0, 1, 2, 3$, and 4 (CdS SILAR cycles number fixed at 7). Table 3 lists their associated photovoltaic parameters: short-circuit current density $J_{sc}$, open-circuit voltage $V_{oc}$, fill factor (FF) and PCE. The PCE of the CdS host was 1.36% ($n = 0$, sample no. 1), consistent with the data in the literature. As the number of PbS SILAR cycles increased, the PCE increased to 2.59% ($n = 1$, sample no. 2) and reached a maximal value of 3.67% at $n = 2$ (sample no. 3). After that, a further increase in $n$ decreased the PCE to 2.87% ($n = 3$, sample no. 4) and 2.09% ($n = 4$, sample no. 5), respectively. The rest photovoltaic parameters of the optimal cell are $J_{sc} = 8.34$ mA/cm², $V_{oc} = 0.70$ V, and FF = 62.8%. The PCE (3.67%) of the maximal sample is near three times of that (1.36%) of the host CdS sample (ie, without Pb incorporation). The $J_{sc}$, $V_{oc}$, and FF of the best cell are all significantly improved over that of the CdS host. A major part of the PCE improvement arises from $J_{sc}$, which increased from 5.10 (the CdS host) to 8.34 mA/cm² (the best cell), an increase of 62%. The improved $J_{sc}$ indicates increased light absorption in the Pb-incorporated $Pb_xCd_{1-x}S$ solar cells, which results from the reduced band gap through Pb substitution. This result is consistent with the optical Tauc plots shown in Figure 6. The improved $J_{sc}$ could also be partly

![](./images/812687189749006338_6.jpg)

![](./images/812687189749006338_7.jpg)

![](./images/812687189749006338_8.jpg)

![](./images/812687189749006338_9.jpg)

![](./images/812687189749006338_10.jpg)

FIGURE 6 Optical spectra (A) transmission, (B) absorbance, and (C) Tauc plots $(Ahv)^2$ vs $h\nu$ of $Pb_xCd_{1-x}S$ nanoparticles (NPs) with various Pb content $x$ and (D) $E_g$ vs Pb content $x$ [Colour figure can be viewed at wileyonlinelibrary.com]

<table>
<thead>
<tr>
<th>$Pb_xCd_{1-x}S$</th>
<th>$E_{CB}$, eV</th>
<th>$E_{VB}$, eV</th>
<th>$E_g$ (CV), eV</th>
<th>$E_g$ (Optical), eV</th>
<th>$E_g$ (EQE²), (eV)²</th>
</tr>
</thead>
<tbody>
<tr>
<td>$x=0$</td>
<td>−3.68</td>
<td>−6.24</td>
<td>2.56</td>
<td>2.40</td>
<td>2.52</td>
</tr>
<tr>
<td>$x=0.02$</td>
<td>−3.90</td>
<td>−6.18</td>
<td>2.28</td>
<td>2.17</td>
<td>2.23</td>
</tr>
<tr>
<td>$x=0.05$</td>
<td>−4.08</td>
<td>−6.02</td>
<td>1.94</td>
<td>2.04</td>
<td>2.04</td>
</tr>
<tr>
<td>$x=0.10$</td>
<td>−4.20</td>
<td>−5.97</td>
<td>1.77</td>
<td>1.88</td>
<td>1.92</td>
</tr>
<tr>
<td>$x=0.17$</td>
<td>−4.25</td>
<td>−5.94</td>
<td>1.69</td>
<td>1.78</td>
<td>1.89</td>
</tr>
</tbody>
</table>

Note. For comparison, $E_g$s determined from optical and EQE measurements are also shown.
Abbreviations: CV, cyclic voltammetry; EQE, external quantum efficiency.

attributed to the increased amount of semiconductor material depos-
ited on the photoelectrode as the number of SILAR cycle was
increased, which led to increased light absorption. However, when
the SILAR cycle number exceeded the optimal cycle ($n=2$), a further
increase in the SILAR cycles would overload the TiO₂ electrode, which
reduced the porous spaces within the TiO₂ electrode and hampered
proper filling of the solid HTM electrolyte, leading to reduced perfor-
mance, as observed in sample nos. 4 and 5.

![](./images/812687189749006338_11.jpg)

FIGURE 7 (A) Cyclic voltammetry curves of $Pb_xCd_{1-x}S$ nanoparticles (NPs) with various Pb content $x$. Insets: Magnified curves of [a] anodic potential and [b] cathodic potential. Supporting electrolyte: 0.1M KCl in deionized water and (B) conduction band levels, valence band levels, and band gaps determined from cyclic voltammetry (CV) curves [Colour figure can be viewed at wileyonlinelibrary.com]

A second notable result in Table 3 is the $V_{oc}$, achieving a maximal value of 0.70 V. The high $V_{oc}$ achieved among all NSSCs is approximately 0.60 to 0.70 V, obtained in various materials such as CdS/ CdSe and CdSeTe. $^{10,12}$ The $V_{oc}$ of $Pb_xCd_{1-x}S$ is comparable with that of other high $V_{oc}$ NSSCs reported to date.

The photovoltaic performance of a SILAR-prepared NSSC improves by measuring the $I$-$V$ curves under reduced light intensities. Figure 8B displays the $I$-$V$ curves of the best $Pb_{0.05}Cd_{0.95}S$ cell under various reduced light intensities $I_0$. Table 4 lists their photovoltaic parameters. As the light intensity $I_0$ was reduced, the photovoltaic parameters PCE, FF, and $J_{sc}$ all increased or improved whereas $V_{oc}$ decreased. The PCE increased from 3.67% (1 sun) to 5.93% (10% sun) and further to 8.48% (1% sun). The PCE under 1% sun is 2.3 times of that under 1 sun. At 0.5 sun, the FF is the major improvement: from 62.8% to 70.8%, an increase of 13%. The current efficiency increased more than 100% between 1 sun and 1% sun. For low light intensities, the current improvement becomes greater. The remarkable improvement in PCE and FF is attributed to the reduction in carrier recombination at low light intensities. The reduced carrier recombination improves the charge transport, resulting in improved photocurrent $J_{sc}$. This can be understood by examining the changes of $J_{sc}$ with light intensity in Table 4. The $J_{sc}$ is 8.34 mA/cm² under 1 sun. For most solar cell materials without carrier recombination (such as Si), $J_{sc}$ depends linearly on light intensity $I_0$. Namely, the number of photoexcited electrons is proportional to the number of incident photons. Assuming linear response in $Pb_xCd_{1-x}S$, $J_{sc}$ should decrease from 8.34 mA/cm² (1 sun) to $8.34 \times 1\% = 0.0834$ mA/cm² (1% sun). However, Table 4 shows $J_{sc} = 0.19$ mA/cm² (1% sun), which is more than two times of that expected from the linear response. The improvement indicates that $Pb_xCd_{1-x}S$ became a much more efficient solar material under low light. The result can be interpreted using the multiple trapping model for carrier recombination in which charges repeat trapping and detrapping from trap sites. $^{43,44}$ The theory predicts a sublinear $J_{sc}$ vs $I_0$ power law: $J_{sc} \propto I_0^\alpha$ ($\alpha < 1$) for a multiple trapping process. A sublinear power law implies that as the light intensity $I_0$ is reduced, $J_{sc}$ will

![](./images/812687189749006338_12.jpg)

FIGURE 8 (A) $I$-$V$ curves of $Pb_xCd_{1-x}S$ nanoparticle-sensitized solar cells (NSSCs) with various Pb content $x$ under 1 sun and (B) $I$-$V$ curves of the best $Pb_{0.05}Cd_{0.95}S$ NSSC under various reduced light intensities [Colour figure can be viewed at wileyonlinelibrary.com]

TABLE 3 Photovoltaic parameters of $\text{Pb}_x\text{Cd}_{1-x}\text{S}$ solar cells with different numbers of SILAR cycles and Pb content $x$

<table>
<thead>
<tr>
<th>Sample No.</th>
<th>SILAR Cycles</th>
<th>$\text{Pb}_x\text{Cd}_{1-x}\text{S}$</th>
<th>$J_{\text{sc}}$, mA/cm²</th>
<th>$V_{\text{oc}}$, V</th>
<th>FF, %</th>
<th>PCE, %</th>
<th>$J_{\text{ph}}$, EQE-Integrated, mA/cm²</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>CdS(7)</td>
<td>CdS</td>
<td>5.10</td>
<td>0.56</td>
<td>47.7</td>
<td>1.36</td>
<td>2.31</td>
</tr>
<tr>
<td>2</td>
<td>PbS(1)/CdS(7)</td>
<td>$\text{Pb}_{0.02}\text{Cd}_{0.98}\text{S}$</td>
<td>6.10</td>
<td>0.68</td>
<td>62.4</td>
<td>2.59</td>
<td>5.28</td>
</tr>
<tr>
<td>3</td>
<td>PbS(2)/CdS(7)</td>
<td>$\text{Pb}_{0.05}\text{Cd}_{0.95}\text{S}$</td>
<td>8.34</td>
<td>0.70</td>
<td>62.8</td>
<td>3.67</td>
<td>12.07</td>
</tr>
<tr>
<td>4</td>
<td>PbS(3)/CdS(7)</td>
<td>$\text{Pb}_{0.10}\text{Cd}_{0.90}\text{S}$</td>
<td>6.83</td>
<td>0.66</td>
<td>63.8</td>
<td>2.87</td>
<td>10.70</td>
</tr>
<tr>
<td>5</td>
<td>PbS(4)/CdS(7)</td>
<td>$\text{Pb}_{0.17}\text{Cd}_{0.83}\text{S}$</td>
<td>5.46</td>
<td>0.63</td>
<td>60.8</td>
<td>2.09</td>
<td>8.46</td>
</tr>
</tbody>
</table>

Abbreviations: EQE, external quantum efficiency; FF, fill factor; PCE, power conversion efficiency; SILAR, sequential ionic layer adsorption reaction.

TABLE 4 Photovoltaic parameters of the best $\text{Pb}_{0.05}\text{Cd}_{0.95}\text{S}$ NSSC under various reduced light intensities

<table>
<thead>
<tr>
<th>Sun Intensity</th>
<th>$J_{\text{sc}}$, mA/cm²</th>
<th>$V_{\text{oc}}$, V</th>
<th>FF, %</th>
<th>PCE, %</th>
</tr>
</thead>
<tbody>
<tr>
<td>100% sun</td>
<td>8.34</td>
<td>0.70</td>
<td>62.8</td>
<td>3.67</td>
</tr>
<tr>
<td>50% sun</td>
<td>4.44</td>
<td>0.70</td>
<td>70.8</td>
<td>4.40</td>
</tr>
<tr>
<td>10% sun</td>
<td>1.21</td>
<td>0.68</td>
<td>72.3</td>
<td>5.93</td>
</tr>
<tr>
<td>5% sun</td>
<td>0.73</td>
<td>0.65</td>
<td>73.4</td>
<td>6.93</td>
</tr>
<tr>
<td>1% sun</td>
<td>0.19</td>
<td>0.60</td>
<td>73.5</td>
<td>8.48</td>
</tr>
</tbody>
</table>

Abbreviations: FF, fill factor; NSSC, nanoparticle-sensitized solar cell; PCE, power conversion efficiency.

decrease at a lower rate than that $I_0$ does. This will lead to a higher PCE at low light intensities. Analysis of the photocurrent $J_{\text{sc}}$ and light intensity $I_0$ data in Table 4 yielded a sublinear power law: $J_{\text{sc}} \propto I_0^{0.86}$, in agreement with the multiple trapping theory. Similar sublinear relation: $J_{\text{sc}} \propto I_0^{0.60}$ and $J_{\text{sc}} \propto I_0^{0.45}$ have also been observed in dye-sensitized solar cells by and Schlichthorl et al$^{45}$ and Franco et al.$^{46}$ The material quality of semiconductor NPs grown by the SILAR method is generally lower than that grown by other chemical methods such as hot injection. The low material quality is probably due to the low reaction temperature so that there is insufficient kinetic energy for atoms to rearrange. Moreover, the atoms of a metal chalcogenide crystal grown by SILAR usually have the cation/anion (C-A) atoms arranged like CCCC-AAAA, quite different from the ideal arrangement of C-A-C-A. Rinsing can reduce but not eliminate the problem. Hence, NPs grown by SILAR contain a large number of surface defects acting as trapping centers. Electron-hole recombination could occur via multiple trapping processes. The electron-hole recombination process is significantly suppressed under reduced light, resulting in improved $J_{\text{sc}}$ and, hence, higher efficiency. The efficiency of 8.48% represents the maximal PCE achieved in the present work. This PCE is comparable with that of other high-efficiency NSSCs based on binary and ternary metal chalcogenides reported so far.

### 3.9 | External quantum efficiency

Quantum efficiency is an important parameter that can reveal the conversion ability of photon to electron of a solar material. Figure 9 shows the EQE spectra of five $\text{Pb}_x\text{Cd}_{1-x}\text{S}$ NSSCs with different $x$. The spectra exhibit two notable features: (a) the EQE performance improves with increasing Pb content $x$. The best performance is the $\text{Pb}_{0.05}\text{Cd}_{0.95}\text{S}$ cell, yielding the maximum EQE of 82% at $\lambda$ = 580 nm. The performance decreases for samples with $x$ > 0.1. The dependence of EQE performance on Pb content $x$ is consistent with the photovoltaic $I$-$V$ curves shown in Figure 8; (b) the EQE spectra become broader with increasing $x$. The spectral range increases from 300 to 500 nm of the CdS host ($x$ = 0) to 300 to 730 nm for $\text{Pb}_{0.17}\text{Cd}_{0.83}\text{S}$ NPs. The enhanced spectral range can be better understood by analyzing the band gap from the EQE spectra. The onset of an EQE spectrum represents the energy where the valence band to conduction band transition occurs, ie, the band gap $E_{\text{g}}$. Figure 9B shows the enlarged EQE spectra near the $E_{\text{g}}$ onsets. The EQE-deduced $E_{\text{g}}$ values for the five samples are listed in Table 2. The result shows that $E_{\text{g}}$ decreases with increasing $x$, in agreement with the results from optical Tauc plots. Note that the best EQE value of 82% for the $\text{Pb}_{0.05}\text{Cd}_{0.95}\text{S}$ cell is close to the theoretical maximal achievable EQE value of approximately 85% (there being an approximately 15% loss due to optical absorption and reflection by the FTO substrate). The near ideal EQE indicates the good quality of the $\text{Pb}_x\text{Cd}_{1-x}\text{S}$ material and fabrication of the solar cells.

The total photocurrent $J_{\text{ph}}$ generated by a solar cell can be calculated from the EQE spectrum using the equation:

$$
J_{ph}=e\int EQE(\lambda)\Phi(\lambda)d\lambda,
$$

where $\Phi(\lambda)$ is the incident photon flux and $e$ is the elementary charge. The calculation $J_{ph}$ for the five samples is shown in Figure 9C and listed in Table 3. The largest EQE-integrated photocurrent is $J_{\text{ph}}$ = 12.07 mA/cm² observed in the $\text{Pb}_{0.05}\text{Cd}_{0.95}\text{S}$ cell ($E_{\text{g}}$ = 1.8 eV).

We summarized the notable results of this work. (a) The band gap of $\text{Pb}_x\text{Cd}_{1-x}\text{S}$ can be tuned from 2.44 to 1.73 eV by controlling the Pb content $x$, resulting in an increased light-harvesting range from 500 to 720 nm. (b) The best cell yielded a PCE of 8.48% (0.01 sun), a respectable high efficiency for a NSSC. The PCE is higher than that (5.3%) reported previously in liquid-junction $\text{Pb}_x\text{Cd}_{1-x}\text{S}$ NSSCs.$^{24}$ (c) The $V_{\text{oc}}$ (0.70 V) is comparable with the high $V_{\text{oc}}$ of other NSSCs reported so far. The main weakness of this work is the large number of surface defects formed on the

![](./images/812687189749006338_13.jpg)

FIGURE 9 (A) External quantum efficiency (EQE) spectra of $Pb_xCd_{1-x}S$ nanoparticle-sensitized solar cells (NSSCs) with various Pb content x and (B) EQE onset of $Pb_xCd_{1-x}S$ NSSCs with various Pb content x and (C) EQE-integrated photocurrent for various samples [Colour figure can be viewed at wileyonlinelibrary.com]

surface synthesized $Pb_xCd_{1-x}S$ NPs, leading to large carrier recombination and low PCE under 1 sun. This problem could be improved by using other material growth methods such as hot injection that produce less surface defects. It would be interesting to apply the ternary $Pb_xCd_{1-x}S$ material to thin-film p-n or p-i-n junction solar cells—the most practical solar cell devices.

## 4 | CONCLUSION
We demonstrated the growth of ternary $Pb_xCd_{1-x}S$ NPs using the SILAR process and function of solid-state $Pb_xCd_{1-x}S$ NSSCs prepared on a mesoporous $TiO_2$ electrode. The incorporation of Pb into CdS increased the light-harvesting range from 500 to 720 nm. The best performance cell with Pb content $x = 0.05$ achieved an efficiency exceeding 8% and a high $V_{oc}$ of 0.70 V. Higher performance is expected with improved NP growth and passivation treatments to reduce carrier recombination.

## ACKNOWLEDGEMENTS
The authors are grateful for the financial support from the Ministry of Science and Technology (MOST) in Taiwan under grant no. MOST108-2112-M-005-002. T.-R.C. was supported by the Young Scholar Fellowship Program from the Ministry of Science and Technology (MOST) in Taiwan, under a MOST grant for the Columbus Program MOST108-2636-M-006-002 and in part by MOST107-2627-E-006-001.

## ORCID
Ming-Way Lee https://orcid.org/0000-0002-8343-9179

## REFERENCES
1. Gore S, Hodes G. Quantum size effects in the study of chemical solution deposition mechanisms of semiconductor films. J Phys Chem. 1994;98(20):5338-5346. https://doi.org/10.1021/j100071a026
2. Moreels I, Lambert K, DeMuynck D, et al. Composition and size-dependent extinction coefficient of colloidal PbSe quantum dots.

Chem Mater. 2007;19(25):6101-6106. https://doi.org/10.1021/ cm071410q

3. Schaller RD, Klimov VI. High efficiency carrier multiplication in PbSe nanoparticles: implications for solar energy conversion. Phys Rev Lett. 2004;92(18):186601-186604. https://doi.org/10.1103/PhysRevLett. 92.186601

4. Shockley W, Queisser HJ. Detailed balance limit of efficiency of p-n junction solar cells. J Appl Phys. 1961;32(3):510-519. https://doi.org/ 10.1063/1.1736034

5. Larramona G, Chone C, Jacob A, et al. Nanostructured photovoltaic cell of the type titanium dioxide, cadmium sulfide thin coating, and copper thiocyanate showing high quantum efficiency. Chem Mater. 2006;18(6):1688-1696. https://doi.org/10.1021/cm052819n

6. Guijarro N, Lana-Villarreal T, Mora-Seró I, Bisquert J, Gómez J. CdSe quantum dot-sensitized TiO₂ electrodes: effect of quantum dot cov- erage and mode of attachment. J Phys Chem C. 2009;113(10):4208- 4214. https://doi.org/10.1021/jp808091d

7. Itzhaik Y, Niitsoo O, Page M, Hodes G. Sb₂S₃-sensitized nanoporous TiO₂ solar cells. J Phys Chem C. 2009;113(11):4254-4256. https://doi. org/10.1021/jp900302b

8. González-Pedro V, Sima C, Marzari G, et al. High performance PbS quantum dot sensitized solar cells exceeding 4% efficiency: the role of metal precursors in the electron injection and charge separation. Phys Chem Chem Phys. 2013;15(33):13835-13843. http://doi.org/10. 1039/C3CP51651B

9. Tumbimtiae A, Wu KL, Tung HY, Lee MW, Wang GJ. Ag₂S quantum dot-sensitized solar cells. Electrochem Commun. 2010;12(9):1158- 1160. https://doi.org/10.1016/j.elecom.2010.06.006

10. Sharma D, Jha R, Kumar S. Quantum dot sensitized solar cell: recent advances and future perspectives in photoanode. Sol Energ Mat Sol C. 2016;155:294-322. https://doi.org/10.1016/j.solmat. 2016.05.062

11. Mustakim NSM, Ubani CA, Sepeai S, Ludin NA, Teridi MAM, Ibrahim MA. Quantum dots processed by SILAR for solar cell applica- tions. Sol Energy. 2018;163:256-270. https://doi.org/10.1016/j. solener.2018.02.003

12. Ye M, Gao X, Hong X, et al. Recent advances in quantum dot-sensi- tized solar cells: insights into photoanodes, sensitizers, electrolytes and counter electrodes. Sustainable Energy Fuels. 2017;1:1217-1231. http://doi.org/10.1039/C7SE00137A

13. Chebrolu VT, Kim HJ. Recent progress in quantum dot sensitized solar cells: an inclusive review of photoanode, sensitizer, electrolyte, and the counter electrode. J Mater Chem C. 2019;7:4911-4933. http://doi.org/10.1039/C8TC06476H

14. Zhao K, Pan Z, Mora-Seró I, et al. Boosting power conversion efficien- cies of quantum-dot sensitized solar cells beyond 8% by recombina- tion control. J Am Chem Soc. 2015;137(16):5602-5609. https://doi. org/10.1021/jacs.5b01946

15. Ren ZW, Wang J, Pan Z, et al. Amorphous TiO₂ buffer layer boosts efficiency of quantum dot sensitized solar cells to over 9%. Chem Mater. 2015;27(24):8398-8405. https://doi.org/10.1021/acs. chemmater.5b03864

16. Zhong X, Feng Y, Knoll W, Han M. Alloyed ZnₓCd₁₋ₓS nanocrystals with highly narrow luminescence spectral width. J Am Chem Soc. 2003;125(44):13559-13563. https://doi.org/10.1021/ja036683a

17. Samosir H, Boon-on P, Lin YE, et al. Tunable optical properties in SnₓSb₂₋ᵧS₃: a new solar absorber material with an efficiency of near 5%. J Phys Chem C. 2019;123(9):5209-5215. https://doi.org/10. 1021/acs.jpcc.8b10596

18. Santra PK, Kamat PV. Tandem-layered quantum dot solar cells: tuning the photovoltaic response with luminescent ternary cadmium chalco- genides. J Am Chem Soc. 2013;135(2):877-885. https://doi.org/10. 1021/ja310737m

19. Wang G, Wei H, Luo Y, et al. A strategy to boost the cell performance of CdSeₓTe₁₋ₓ quantum dot sensitized solar cells over 8% by introducing Mn modified CdSe coating layer. J Power Sources. 2016; 302:266-273. http://doi.org/10.1016/j.jpowsour.2015.10.070

20. Wang J, Li Y, Shen Q, et al. Mn doped quantum dot sensitized solar cells with power conversion efficiency exceeding 9%. J Mater Chem A. 2016;4:877-886. http://doi.org/10.1039/C5TA09306F

21. Madelung O. Semiconductor Data Handbook. Berlin: Springer; 2004.

22. Nasir EM, Naji IS. Structural and optical properties of PbₓCd₁₋ₓS thin films prepared by vacuum evaporation technique. Aust J Basic & Appl Sci. 2015;9(20):364-371.

23. Mohammed MA, Mousa AM, Ponpon JP. Optical and optoelectric properties of PbCdS ternary thin films deposited by CBD. J Semicond Tech Sci. 2009;9(2):117-123. http://doi.org/10.5573/JSTS.2009.9. 2.117

24. Yuan D, Xiao L, Luo J, et al. High-throughput screening and optimiza- tion of binary quantum dots cosensitized solar cell. ACS Appl Mater Interfaces. 2016;8:18150-18156. http://doi.org/10.1021/acsami. 6b06029

25. Yuan C, Li L, Huang J, Ning Z, Sun L, Ågren H. Improving the photo- current in quantum-dot-sensitized solar cells by employing alloy PbₓCd₁₋ₓS quantum dots as photosensitizers. Nanomaterials. 2016; 6(6):97-109. https://doi.org/10.3390/nano6060097

26. Jiao S, Wang J, Shen Q, Li Y, Zhong X. Surface engineering of PbS quantum dot sensitized solar cells with a conversion efficiency exceeding 7%. J Mater Chem A. 2016;4:7214-7221. https://doi.org/ 10.1039/C6TA02465C

27. Blöchl PE. Projector augmented-wave method. Phys Rev B. 1994; 50(24):17953-17979. https://doi.org/10.1103/PhysRevB.50.17953

28. Kresse G, Joubert D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys Rev B. 1999;59(3):1758-1775. https://doi.org/10.1103/PhysRevB.59.1758

29. Kresse G, Furthmüller J. Efficiency of ab-initio total energy calcula- tions for metals and semiconductors using a plane-wave basis set. Comput Mater Sci. 1996;6(1):15-50. http://doi.org/10.1016/0927- 0256(96)00008-0

30. Perdew JP, Burke K, Ernzerhof M. Generalized gradient approxima- tion made simple. Phys Rev Lett. 1996;77(18):3865-3868. https://doi. org/10.1103/PhysRevLett.77.3865

31. Heyd J, Scuseria GE, Ernzerhof M. Hybrid functionals based on a screened coulomb potential. J Chem Phys. 2003;118(18):8207-8215. https://doi.org/10.1063/1.1564060

32. Heyd J, Scuseria GE, Ernzerhof M. Erratum: hybrid functionals based on a screened coulomb potential. J Chem Phys. 2006;124(21): 219906-219906-1. http://doi.org/10.1063/1.2204597

33. Marzari N, Vanderbilt D. Maximally localized generalized Wannier functions for composite energy bands. Phys Rev B. 1997;56(20): 12847-12865. https://doi.org/10.1103/PhysRevB.56.12847

34. Souza I, Marzari N, Vanderbilt D. Maximally localized Wannier func- tions for entangled energy bands. Phys Rev B. 2001;65(3): 035109-035121. https://doi.org/10.1103/PhysRevB.65.035109

35. Mostofi AA, Yates JR, Lee YS, Souza I, Vanderbilt D, Marzari N. wannier90: a tool for obtaining maximally-localised Wannier func- tions. Comput Phys Commun. 2008;178(9):685-699. https://doi.org/ 10.1016/j.cpc.2007.11.016

36. Franchini C, Kováčik R, Marsman M, et al. Maximally localized Wannier functions in LaMnO₃ within PBE + U, hybrid functionals and partially self-consistent GW: an efficient route to construct ab initio tight-binding parameters for e₉ perovskites. J Phys Condens Matter. 2012;24(23):235602-235618. http://doi.org/10.1088/0953-8984/ 24/23/235602

37. Xu SY, Xia Y, Wray LA, et al. Topological phase transition and texture inversion in a tunable topological insulator. Science. 2011;332(6029): 560-564. http://doi.org/10.1126/science.1201607

38. Kim J, Hwang S, Lee C, Kim H. Etching behavior of Pb ion from PbO- B₂O₃-SiO₂ glasses in HNO₃ solution. Met Mater Int. 2009;15(5):857- 862. http://doi.org/10.1007/s12540-009-0857-7

39. Nikam PR, Baviskar PK, Sali JV, Gurav KV, Kim JH, Sankapal BR. CdS surface encapsulated ZnO nanorods: synthesis to solar cell applica- tion. *J Alloys Compd.* 2016;689:394-400. https://doi.org/10.1016/j. jallcom.2016.07.295

40. Wang R, Chen S, Ng YH, et al. ZnO/CdS/PbS nanotube arrays with multi-heterojunctions for efficient visible-light-driven photo- electrochemical hydrogen evolution. *Chem Eng J.* 2019;362:658-666. https://doi.org/10.1016/j.cej.2019.01.073

41. Ekimov AI, Efros AL, Onushchenko AA. Quantum size effect in semi- conductor microcrystals. *Solid State Commun.* 1985;56(11):921-924. https://doi.org/10.1016/S0038-1098(85)80025-9

42. Manjceevan A, Bandara J. Systematic stacking of PbS/CdS/CdSe multi-layered quantum dots for the enhancement of solar cell effi- ciency by harvesting wide solar spectrum. *Electrochim Acta.* 2018;271:567-575. https://doi.org/10.1016/j.electacta.2018.03.193

43. Tachiya M, Seki K. Theory of bulk electron-hole recombination in a medium with energetic disorder. *Phys Rev B.* 2010;82(2):085201-085208. http://doi.org/10.1103/PhysRevB.82.085201

44. Nelson J, Haque SA, Klug DR, Durrant JR. Trap-limited recombination in dye-sensitized nanocrystalline metal oxide electrodes. *Phys Rev B.* 2001;63(20):205321-205329. http://doi.org/10.1103/PhysRevB.63.205321

45. Schlichthorl G, Park NG, Frank AJ. Evaluation of the charge-collection efficiency of dye-sensitized nanocrystalline $TiO_2$ solar cells. *J Phys Chem B.* 1999;103(5):782-791. https://doi.org/10.1021/jp9831177

46. Franco G, Gehring J, Peter LM, Ponomarev EA, Uhlendorf I. Fre- quency-resolved optical detection of photoinjected electrons in dye- sensitized nanocrystalline photovoltaic cells. *J Phys Chem B.* 1999;103(4):692-698. https://doi.org/10.1021/jp984060r

## SUPPORTING INFORMATION
Additional supporting information may be found online in the Supporting Information section at the end of this article.

How to cite this article: Boon-on P, Lien S-W, Chang T-R, Shi J-B, Lee M-W. Band gap engineered ternary semiconductor $Pb_xCd_{1-x}$S: Nanoparticle-sensitized solar cells with an efficiency of 8.5% under 1% sun-A combined theoretical and experimental study. *Prog Photovolt Res Appl.* 2020;1-14. https://doi.org/10.1002/pip.3245