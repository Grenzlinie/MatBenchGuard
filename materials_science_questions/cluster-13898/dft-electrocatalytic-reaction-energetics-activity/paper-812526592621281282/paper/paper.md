# An In-Depth Theoretical Exploration of Influences of Non-Metal-Elements Doping on the ORR Performance of Co–gN₄

Cehuang Fu, $^{[a]}$ Liuxuan Luo, $^{[a]}$ Lijun Yang, $^{[b]}$ Shuiyun Shen, $^{*[a]}$ Xiaohui Yan, $^{[a]}$ Jiewei Yin, $^{[a]}$ Guanghua Wei, $^{[c]}$ and Junliang Zhang $^{*[a]}$

Single atom catalysts (SACs) show a great attraction towards the oxygen reduction reaction (ORR) owing to its advantage in overcoming the cost issue of fuel cell because of its high utilization, low cost and great CO tolerance. However, theoretical investigation on the influences of different doping on the ORR catalytic activity of Co SACs has not been systematically performed. In this regard, the influences of non-metal-elements doping (B, N, Si, P, S) on the ORR catalytic activity of Co–gN₄ is well explored based on density functional theory (DFT). The rate-limiting step for the ORR on Co–gN₄ is the formation of OOH. When the doping content of B increases, the adsorption on Co site becomes weaker which limits the occurrence of 4e⁻ ORR process. N doping shows a weak promotion on the ORR process on Co site. The Si site next to N can be poisoned by OH. The P site next to N will be poisoned by O at high potential and OH at low potential. The S site next to N would be poisoned by O. It is revealed that the ORR process on Co site can be promoted when the carbon next to N is replaced by Si/P/S by promoting the rate-limiting step.

## 1. Introduction

Hydrogen is considered as one of the most promising renewable energies to help solve the exhaustion and pollution problems of fossil energy. $^{[1]}$ And proton exchange membrane fuel cells (PEMFCs) are burgeoning as the optimal technique of hydrogen utilization and have taken too much attention, especially in the automotive field. The sluggish kinetics of oxygen reduction reaction (ORR) in the cathode greatly limits the fuel cell performance, and at present, only platinum satisfies the requirement in both the activity and stability for the commercialization of PEMFCs. $^{[2]}$ However, it is very frustrating that Pt is rare and costly, thus the fuel cell cost remains high for their large-scale industrial application so far. $^{[3]}$ Different strategies have been developed to enhance the ORR performance on Pt, including (1) alloying Pt with different transition metals, such as Pt₃Co and Pt₃Ni, (2) forming Pt monolayer loaded by other metals, (3) pyrolyzing non-noble metal catalyst, such as pyrolyzed Fe–N–C composites. $^{[4-7]}$

More recently, single atom catalysts (SACs) are highly profiled in the ORR catalyst design owing to their advantages of high utilization, low cost and great CO tolerance. $^{[8]}$ Among various SACs, the series of iron-based catalysts, of which Fe atom is coordinated with 4 N atom (marked as Fe–gN₄) is considered as the better one for its high activity in ORR. $^{[9,10]}$ However, there remains a big issue in the stability of Fe-based catalysts caused by Fenton reaction, during which Fe²⁺ is highly active to react with H₂O₂ and its product would degrade the ionomer membrane. $^{[11-13]}$ Although providing lower ORR activities relative to Fe-based catalysts, cobalt-based catalysts usually possess more preferred stability than iron-based catalysts and are more promising to catalyze the ORR. $^{[10,12,14,15]}$ The structure of Co–gN₄ is thought as the main active site in cobalt-based catalysts and more and more researches on Co SACs are being performed to strengthen the ORR activity. $^{[16-19]}$ Yin et al. obtained stable Co single atoms on nitrogen-doped porous carbon through pyrolyzing pre-designed bimetallic Zn/Co metal-organic frameworks and a great ORR performance with a half-wave potential of 0.881 V was achieved. $^{[16]}$ Zhang et al decorated isolated Co sites with pre-designed configuration of polystyrene, polyacrylonitrile and as-synthesized cobalt porphyrins into interconnected multichannel carbon matrix and the as-decorated Co–gN₄ performed greater O₂ adsorption and reduction efficiency. $^{[17]}$ Cobalt single-atoms with a Co–gN₄ moiety were anchored on a porous porphyrinic triazine-based framework and led to a half-wave potential of 0.808 V in Yi's work. $^{[18]}$ It is reported by Yang et al. that a single-atom Co electrocatalyst with CoN₄ moieties dispersed on nitrogen-doped graphitic nanosheet has been prepared by a surfactant-assisted approach and shows a high ORR activity with a half-wave potential of 0.87 V. $^{[19]}$ Although amazing ORR activities are achieved and some corresponding speculations are made,

---

[a] C. Fu, L. Luo, S. Shen, X. Yan, J. Yin, Prof. J. Zhang
Institute of Fuel Cells, MOE Key Laboratory of Power & Machinery Engineering
School of Mechanical Engineering
Shanghai Jiao Tong University
Shanghai 200240 (P. R. China)
E-mail: shuiyun_shen@sjtu.edu.cn
junliang.zhang@sjtu.edu.cn

[b] Prof. L. Yang
MOE Key Laboratory of Mesoscopic Chemistry, Jiangsu Provincial Lab for Nanotechnology
School of Chemistry and Chemical Engineering
Nanjing University
Nanjing 210240 (P. R. China)

[c] Prof. G. Wei
SJTU-Paris Tech Elite Institute of Technology
Shanghai Jiao Tong University
Shanghai 200240 (P. R. China)

![](./images/812526592621281282_1.jpg)
Supporting information for this article is available on the WWW under
https://doi.org/10.1002/cctc.202001713

theoretical investigation on the influences of different doping on the ORR catalytic activity of Co–gN₄ has not been systemati- cally performed.

In this work, the influences of non-metal-elements doping on the ORR catalytic activity of Co–gN₄ have been well explored based density function theory (DFT). It is recognized that the rate-limiting elementary reaction on Co–gN₄ is the formation of OOH because of weak O₂ adsorption. Accompanied with the increase in the doping of a second-period element, the adsorptions of intermediates on Co site becomes weaker and the ORR mechanism proceeds as those on non-doped Co–gN₄, which does not benefit the ORR on Co–gN₄. When being coordinated with a third-period element, for example, when the carbon next to nitrogen is replaced by P or Si, the ORR process will be promoted greatly because of different mechanisms. It is found that Si site may be poisoned by OH during the ORR process and the formation of OOH is promoted. P site may be poisoned by O and OH during the ORR process, and when it is poisoned by OH at low potential, OH on P would be excellent proton donors and when it is poisoned by O at high potential, the formation of OOH is promoted greatly. S site may be poisoned by O and the formation of OOH is promoted. The difference between the second-period-element doping and third-period-element doping may come from the hydrogen bond between OH and O on doped sites (Si/P/S) which could stabilize adsorbates (O₂/OOH/O/OH). What's more, the O adsorbed on P or S site leads to the different effect on O₂/O adsorptions and OOH/OH adsorptions, which is the key to break the scaling relationship that limits the ORR process on catalysts.

## Computational Details

All the calculations with density functional theory are carried on the DMol3 on Material Studio 8.0. The generalized gradient-corrected Perdew-Burke-Ernzerhof functional (GGA-PBE) is used to described the electronic exchange and correlation. $^{[20-21]}$ Tkatchenko-Scheffler (TS) method is used in Dispersion-corrected DFT scheme to calculated the van der Waals interactions. $^{[22]}$ DFT semi-core pseudopotentials are applied in core treatment. $^{[20]}$ The atomic orbital is described by double numerical plus polarization (DNP) 4.4 basis set. $^{[23]}$ The Muliken population analysis is used in calculation of the charge density difference.

The single Co atom catalyst model (marked as Co–gN₄) in Figure 1a is built with the monolayer graphite, which consists of 94 C atoms. All models are sampled by $5×4×1$ Monkhorst-Pack grid. The lattice parameters are $\alpha=14.760$ Å, $\beta=17.0434$ Å, $c=20.0$ Å. The con- vergence tolerances of energy, max force and max displacement are 0.00001 Ha, 0.002 Ha/Å, 0.005 Å.

![](./images/812526592621281282_2.jpg)

Figure 1. The top view of (a) Co–gN₄ (b) doped Co–gN₄. Grey, carbon. Blue, nitrogen. Green, cobalt. Black, doping elements.

The as-doped single Co atom catalyst models (doped Co–gN₄) are built by replacing carbon with non-metal elements, and one of possible structures are shown in Figure 1b. The doped models are marked as BNC, NNC, SiNC, PNC, SNC according to doping elements.

In Figure 2a, all possible doping sites are marked according to doping elements and structural symmetry, for example, BNC-1 represents the situation that the C atom at site 1 is taken the place of by B. $\Delta E_{formation}$ is calculated by:

$$
\Delta E_{\text{formation}}=\text{E}_{\text{structure}}-\text{E}_{\text{BNC1/NNC1/SiNC1/PNC1/SNC1}} \tag{1}
$$

Where $E_{structure}$ is structure energy and $E_{BNC1}$ is BNC1's energy. In Figure 3b–3f that B, Si, P, S tends to be coordinated with N, and as the distance between the doping site and Co site increases, this coordinated structure becomes less preferred thermodynamically. It is worth mentioned that the special site4 is closest to Co site and is more unstable than site1, which may be led to by special graphite structure. The most stable coordinated structures are marked as BNC-1, SiNC-1, PNC-1 and SNC-1. However, when C atom is replaced by N atom, the bonding between two N atoms is not preferred based on Figure 3c, the most unstable coordinated structures is marked as NNC-1. It is noted from Figure 2b that the catalyst surface is not symmetric on two side when being doped by the third-period elements, the ORR process is thus not calculated on the doped structures which are doped by more than one Si/P/S atom.

![](./images/812526592621281282_3.jpg)

Figure 2. (a) Possible doping sites on Co–gN₄ used in calculation. $\Delta E_{formation}$ of all possible (b) single-B-atom-doped, (c) single-N-atom-doped, (d) single- Si-atom-doped, (e) single-P-atom-doped and (f) single-S-atom-doped struc- tures.

![](./images/812526592621281282_4.jpg)

Figure 3. The energy profile of the ORR process on Co–gN₄.

The adsorption energies of O₂/OOH/O/OH which are used to evaluate the ORR process on different catalysts are given as follow:

$$E_{O2}=G_{ad}-G_{O2}-G_{structure} \tag{2}$$

$$E_{OOH}=G_{ad}-G_{O2}-G_{H+}-G_{e-}-G_{structure} \tag{3}$$

$$E_{O}=G_{ad}-G_{O2}-2G_{H+}-2G_{e-}+G_{H2O}-G_{structure} \tag{4}$$

$$E_{OH}=G_{ad}-G_{O2}-3G_{H+}-3G_{e-}+G_{H2O}-G_{structure} \tag{5}$$

where $G_{ad}$ is the total energy of catalyst for the adsorption of O₂/ OOH/O/OH, $G_{O2}$ is the free energy of O₂ and $G_{structure}$ is that of clean catalyst surface. The energy of $(H^{+}+e^{-})$ is defined as two times of that of H₂ on the standard condition (U=0 and pH=0).^{[24-25]} And the free energy was calculated as:

$$G=E+ZPE-TS-neU \tag{6}$$

where E is the energy of the model calculated with DFT, ZPE is the zero-point energy which is calculated by $\sum (h\nu_{i}/2)$ (h is the Planck constant and $\nu_{i}$ is the vibrational frequency), T is the temperature (298.15 K), S is the entropy of the structure which is given by vibrational frequency, n is the number of electrons transferred in elementary reaction, e is the charge constant and U is the potential.^{[24-26]} $G_{H2O(l)}=G_{H2O(g)}+RT×ln(P/P0)$ is used to calculate the energy of H₂O, where $G_{H2O(g)}$ is given by DFT calculation, R is gas constant with $P_{0}=1$ bar and P=0.035 bar. The free energy of O₂ is calculated according to the thermodynamic energy (4.92 eV) released by the reaction of $2H_{2}+O_{2}\to2H_{2}O$. The energy profile of ORR process is given by the difference value of total energy between elementary steps.^{[24,25]}

The charge density difference, which is used to evaluate the valance state, is calculated by Muliken analysis as followed:

$$\Delta\rho=\rho_{AB}-\rho_{A}-\rho_{B} \tag{7}$$

where $\rho_{AB}$, $\rho_{A}$ and $\rho_{B}$ are density after and before coordination.

## Results and Discussion
### ORR process on non-doped Co-gN₄

The ORR process on most carbon-based SACs could be described by the following reaction steps:^{[19]}

$$O_{2}\to O_{2}^{*} \tag{1}$$

$$O_{2}^{*}+H^{+}+e^{-}\to OOH^{*} \tag{2}$$

$$OOH^{*}+H^{+}+e^{-}\to O^{*}+H_{2}O \tag{3}$$

$$O^{*}+H^{+}+e^{-}\to OH^{*} \tag{4}$$

$$OH^{*}+H^{+}+e^{-}\to H_{2}O \tag{5}$$

The breaking of O=O bond and the desorption of OH are main rate-determining steps in the ORR process.^{[24]} The stronger the adsorption is, the more strenuous the interaction between oxygen and catalyst is, for which the O=O bond is easier to break up or OOH is easier to form.^{[24]} On the other hand, it is hard for OH to desorb and H₂O is finally formed. According to the calculation in Figure 3, the energy for every state is 0, −0.31316, −0.80658, −2.15894, −3.90224 eV at 1.23 V and the low activity of Co−gN₄ mostly comes from the weak OOH adsorption. The overpotential is about 0.73 V, which is limited by the small $\Delta G$ of step (2). What's more, the weak OOH adsorption may even lead to formation of H₂O₂.^{[27,28]} The calculation result matches well the result in previous studies.^{[27,28]}

### ORR process on B-doped Co-gN₄

The Mulliken charge of Co is calculated and is presented in Figure 4a. Co lost more electrons when the distance between the doping site and Co decreases (every model contains only one B atom and is marked as BNC in Figure 2). Figure 4b shows the Mulliken charge of structures (such as Figure 4c), which are doped by different contents of B at equivalent sites. It is observed that Co loses more electrons and performs a higher valance state as the B content increases or the distance between Co and the doping site reduces. The tendency may be attributed to the fact that the electronegativity of B is weaker than that of C. When B is doped on graphite, a positive-charge region forms near Co−N₄, for which Co site would lose more electrons for balance.

When Co−gN₄ is doped by a B atom, the energy profile of the ORR process on a series of doped structures are listed in Table 1. Compared with that of non-doped Co−gN₄ in Figure 3, the adsorption of O₂/OOH/O/OH on BNC-1 which is preferred thermodynamically and contains a higher-valance-state Co is

![](./images/812526592621281282_5.jpg)

Figure 4. The relationship between the Mulliken charge of Co (a) and doping site (b) the number of B atoms are doping on BNC-1. $D_{Co-B}$ is the distance between Co and B.

<table>
<caption>Table 1. The energy profile of ORR on some B-doped Co−gN₄ at 0 V.</caption>
<thead>
<tr>
<th>Model</th>
<th>State 2 [eV]</th>
<th>State 3 [eV]</th>
<th>State 4 [eV]</th>
<th>State 5 [eV]</th>
</tr>
</thead>
<tbody>
<tr>
<td>BNC-1</td>
<td>−0.33707</td>
<td>−0.85481</td>
<td>−2.4221</td>
<td>−3.98165</td>
</tr>
<tr>
<td>BNC-2</td>
<td>−0.31382</td>
<td>−0.83647</td>
<td>−2.28665</td>
<td>−3.92126</td>
</tr>
<tr>
<td>BNC-3</td>
<td>−0.31471</td>
<td>−0.83005</td>
<td>−2.27151</td>
<td>−3.91844</td>
</tr>
<tr>
<td>BNC-4</td>
<td>−0.28958</td>
<td>−0.76838</td>
<td>−2.30483</td>
<td>−3.85527</td>
</tr>
<tr>
<td>BNC-5</td>
<td>−0.3263</td>
<td>−0.8385</td>
<td>−2.3417</td>
<td>−3.93633</td>
</tr>
<tr>
<td>BNC-6</td>
<td>−0.29286</td>
<td>−0.80129</td>
<td>−2.28084</td>
<td>−3.88762</td>
</tr>
<tr>
<td>BNC-7</td>
<td>−0.31168</td>
<td>−0.82578</td>
<td>−2.27281</td>
<td>−3.90834</td>
</tr>
<tr>
<td>BNC-8</td>
<td>−0.30426</td>
<td>−0.81637</td>
<td>−2.28085</td>
<td>−3.90597</td>
</tr>
<tr>
<td>BNC-9</td>
<td>−0.31605</td>
<td>−0.83282</td>
<td>−2.26819</td>
<td>−3.91597</td>
</tr>
</tbody>
</table>

intensified. When B atom is coordinated with N as BNC-4, adsorptions of intermediates are weaker than those on non-doped Co–gN₄. According to other data in Table 1, it could be deduced that when B atom is not coordinated with N, adsorptions of intermediates are similar with those on non-doped Co–gN₄ except O adsorption.

To further study the relationship between adsorptions of ORR intermediates and B doping, the ORR process is calculated on doped models which contain different B content (structures are showed in Figure S1) at BNC-1, which is preferred thermodynamically according to Figure 2. It is found in Figure 5 that accompanied with the increase in B content, the adsorption on Co site is weakened. The potential-limiting step is step (2) and overpotentials of most doped structures are about 0.7 V. The result could be understood by scaling relationships.¹²⁹⁾ O₂/OOH/O/OH adsorptions are weakened together and the energy released in potential-limiting step varies insignificantly.

In summary, the valance state of Co can be used to describe the influence of B doping, potential-limiting step is not promoted by B doping and the higher B content will lead to the weaker OOH adsorption, thus promoting the formation of H₂O₂.

## ORR process on N-doped Co–gN₄

The doping sites in N-doped Co–gN₄ models are same as those in B-doped Co–gN₄. When Co–gN₄ is doped by N elements, of which the electronegativity is greater than that of C, Co loses less electrons according to the Mulliken charge showed in Figure 6. The valance state of Co is mostly related to N content as N is not coordinated with Co-N₄ site. The ORR process is also considered on N-doped Co–gN₄ and performed in Table 2. Compared with that on non-doped Co–gN₄, adsorptions of intermediates on N-doped Co–gN₄ are always weakened. It is suggested by Figure 7 that when N content increases (structures are shown in Figure S2), adsorptions of intermediates are influenced little. N doping fails to promote the potential-limiting step and the overpotential on doped catalysts are about 0.7 V.

![](./images/812526592621281282_6.jpg)

Figure 5. Energies of state 2–5 on BNC-1 when B content increases.

![](./images/812526592621281282_7.jpg)

Figure 6. The relationship between Co's Mulliken charge (a) and doping site (b) doping content. D_{Co–N} is the distance between Co and N.

<table>
<caption>Table 2. The energy profile of ORR on some N-doped Co–gN₄ at 0 V.</caption>
<thead>
<tr>
<th>Model</th>
<th>State 2 [eV]</th>
<th>State 3 [eV]</th>
<th>State 4 [eV]</th>
<th>State 5 [eV]</th>
</tr>
</thead>
<tbody>
<tr>
<td>NNC-1</td>
<td>−0.17825</td>
<td>−0.67191</td>
<td>−2.01562</td>
<td>−3.76025</td>
</tr>
<tr>
<td>NNC-2</td>
<td>−0.25645</td>
<td>−0.73521</td>
<td>−2.03754</td>
<td>−3.82536</td>
</tr>
<tr>
<td>NNC-3</td>
<td>−0.25568</td>
<td>−0.73373</td>
<td>−2.05406</td>
<td>−3.82879</td>
</tr>
<tr>
<td>NNC-4</td>
<td>−0.09668</td>
<td>−0.57368</td>
<td>−1.79403</td>
<td>−3.66551</td>
</tr>
<tr>
<td>NNC-5</td>
<td>−0.25867</td>
<td>−0.74979</td>
<td>−2.03243</td>
<td>−3.82582</td>
</tr>
<tr>
<td>NNC-6</td>
<td>−0.21315</td>
<td>−0.69655</td>
<td>−1.99676</td>
<td>−3.8022</td>
</tr>
<tr>
<td>NNC-7</td>
<td>−0.25186</td>
<td>−0.72816</td>
<td>−2.02744</td>
<td>−3.8211</td>
</tr>
<tr>
<td>NNC-8</td>
<td>−0.23232</td>
<td>−0.69542</td>
<td>−1.98453</td>
<td>−3.79807</td>
</tr>
<tr>
<td>NNC-9</td>
<td>−0.24838</td>
<td>−0.73302</td>
<td>−2.02422</td>
<td>−3.80319</td>
</tr>
</tbody>
</table>

![](./images/812526592621281282_8.jpg)

Figure 7. Energies of state 2–5 on NNC-3 when doping content increases.

In sum, when doped with N, Co–gN₄, which contains lower Co's valance state, would shows weaker adsorption and N doping always leads to less ΔG of step (2) than non-doped Co–gN₄ does. Thus, ORR (4e⁻ reaction) on Co–gN₄ is limited by N doping.

## ORR process on Si-doped Co–gN₄

When doped with third-period element (Si, P, S and marked as SiNC, PNC, SNC), there is a protuberance at doping site as Figure S3. What's more, the special surface structure influences the O₂ adsorption and ORR process greatly. There are interesting adsorption structures on SiNC and PNC in Figure 8. It is more stable for oxygen to be adsorbed on Co and Si site as bridge style. What's more, when adsorbed on Co and P sites,

![](./images/812526592621281282_9.jpg)

Figure 8. Possible $O_2$ adsorption structures after optimization on (a) SiNC, (b) PNC, and (c) SNC. Red, oxygen. Orange, silicon. Purpose, phosphorus.

the oxygen molecule preferred to be broken into 2 O atoms on Co and P sites. The bridge adsorption does not appear on SNC, which may be result of weaker interaction between sulfur and oxygen.

When $O_2$ is adsorbed as bridge style and reduced at elementary reaction [2], O=O bond is broken and OH is adsorbed on Co site and O is located at Si sites. The ORR process is calculated in Figure 9a. It is worth mentioning that OH desorption is greatly endothermal on Si site and hard to be reduced, which indicates that the Si is very likely poisoned by OH.

When $O_2$ is adsorbed on Co as top site and the ORR process is described by reaction steps (1)..(5), O is found to be adsorbed as Co-O-Si bridge style as shown in Figure 10a and OH would be adsorbed on Si when O is reduced as shown in Figure 10b. Because OH desorption on Si site is a greatly endothermal process, steps (1)-(5) are not suitable to describe the ORR process on Si-doped Co-gN$_4$. Thus, the final ORR process on SiNC could be described by steps (6)-(10), in agreement with Figure 9b:

$$\mathrm{O}_{2}+\mathrm{OH}^{*}(\mathrm{Si}) \rightarrow \mathrm{O}_{2}{ }^{*}+\mathrm{OH}^{*}(\mathrm{Si}) \tag{6}$$

$$\mathrm{O}_{2}{ }^{*}+\mathrm{OH}^{*}(\mathrm{Si})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OOH}^{*}+\mathrm{OH}^{*}(\mathrm{Si}) \tag{7}$$

$$\mathrm{OOH}^{*}+\mathrm{OH}^{*}(\mathrm{Si})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{O}^{*}+\mathrm{OH}^{*}(\mathrm{Si}) \tag{8}$$

$$\mathrm{O}^{*}+\mathrm{OH}^{*}(\mathrm{Si})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OH}^{*}+\mathrm{OH}^{*}(\mathrm{Si}) \tag{9}$$

$$\mathrm{OH}^{*}+\mathrm{OH}^{*}(\mathrm{Si})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{H}_{2} \mathrm{O}+\mathrm{OH}^{*}(\mathrm{Si}) \tag{10}$$

![](./images/812526592621281282_10.jpg)

Figure 9. The energy profile of ORR process on SiNC (a) when Si site is not poisoned and (b) when Si site is poisoned by hydroxyl. *(Si) is used to mark the adsorption on Si site.

Compared with that on non-doped Co-gN$_4$, during ORR process on Si-doped Co-gN$_4$, the interactions between Co and oxygen species (OOH, O and OH) is intensified, which may accelerate the process of breaking O=O bond. Desorption of OH becomes the potential-limiting elementary reaction. The over-potential does not decrease greatly.

Other Si-doping sites are shown in Figure 2. When Si atom is doped at SINC-4, O migration is also observed and OH desorption is great endothermic process, which suggests Si site is poisoned by OH as what is found on SINC-1. ORR process on SiNC-4 works as indicated in steps (6)-(10) and is limited because of less $\Delta$G of OOH formation as Figure S4. When Si atom is doped at other sites, adsorptions of intermediates are similar with that on non-doped Co-gN$_4$ according to Table S1.

According to Table S1, it is worth mentioned that when Co is not poisoned by OH, energy diagrams of elementary reactions are similar to those on B-doped CoP. Thus, the valance state may not be the key to promote potential-limiting step. It is speculated that OH on Si site may be the key point. Hydrogen bond could form between OH and intermediates ($O_2$/OOH/O/ OH) as Figure S7 (H atom always points to O atom on Co site) and in Table S4. The stability of intermediates is intensified according to large adsorption energies on SiNC-1 and SiNC-4. The energy released in step (7) increases and the potential-limiting step is promoted. However, the ORR process is still limited by scaling relationships because $O_2$/OOH/O/OH adsorptions are influenced similarly. Comparing the adsorptions on SiNC-1 and SiNC-4 after OH poisoning, adsorptions on SiNC-4 are weaker. The reason may be that though hydrogen bond help stabilize adsorbates, when the distance between Si and Co is too closed, OH on S site may take up the space near Co site. The narrow space leads to a repulsive interaction between adsorbates, which finally leads to a weaker adsorption on SiNC-4.

![](./images/812526592621281282_11.jpg)

Figure 10. (a) O is adsorbed as Co-O-Si bridge site after optimization (b) OH moves to Si site during further reducing process. White, H.

## ORR process on P-doped Co-gN$_4$

$O_2$ adsorption on Co site is stronger than that on P site and ORR process, which performs on Co site, could be described by

reaction steps (1)-(5) in Figure 11a. Another $O_2$ adsorption structure on P-doped Co-$gN_4$ as Figure 8b indicates that the breaking of $O_2$'s double bond, which is considered as the key step of ORR, is intensified greatly on P-doped Co-$gN_4$. The energy profile when $O_2$ is broken could be described as Figure 11b. And the fact that O and OH are more stable on P site than Co site (about 2.88 and 1.45 eV) verifies the strong interaction between oxygen and phosphorus the P site is likely to be poisoned by O atom or hydroxyl during ORR process and loses its influence in breaking O=O bond. From the calculation of ORR elementary reactions (11)—(15) with OH taking up P site in Figure 11c, the migration of H atom is found in elementary reactions (11) and (13). After optimization as Figure 12, the $O_2$ and O on Co site is reduced by the OH on P site, which indicates that the OH on P site may be great medium for proton transfer and promote ORR process on Co site. However, little $\Delta G$ of elementary reaction (15) is only -0.22 eV which indicates that O is not preferred to be reduced in high potential condition. When P site is poisoned by O atom, the ORR energy profile is shown in Figure 11d and the formation of OOH is promoted greatly, which is very different to the energy profile without poisoning in Figure 11b. In sum, the ORR reaction mechanism on PNC could be concluded as elementary reactions (1)-(5) (P site is not poisoned), [11]-[15] (P site is poisoned by OH and marked as OH*(P)) and steps (16)-(20) (P site is poisoned by O atom and marked as O*(P)):

$$\mathrm{O}_{2}+\mathrm{OH}^{*}(\mathrm{P}) \rightarrow \mathrm{OOH}^{*}+\mathrm{O}^{*}(\mathrm{P}) \tag{11}$$

$$\mathrm{OOH}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{O}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}_{2} \mathrm{O} \tag{12}$$

$$\mathrm{O}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OH}^{*}+\mathrm{O}^{*}(\mathrm{P}) \tag{13}$$

$$\mathrm{OH}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{O}^{*}(\mathrm{P}) \tag{14}$$

$$\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OH}^{*}(\mathrm{P})+\mathrm{H}_{2} \mathrm{O} \tag{15}$$

$$\mathrm{O}_{2}+\mathrm{O}^{*}(\mathrm{P}) \rightarrow \mathrm{O}_{2}{ }^{*}+\mathrm{O}^{*}(\mathrm{P}) \tag{16}$$

$$\mathrm{O}_{2}{ }^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OOH}^{*}+\mathrm{O}^{*}(\mathrm{P}) \tag{17}$$

$$\mathrm{OOH}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{O}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}_{2} \mathrm{O} \tag{18}$$

$$\mathrm{O}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OH}^{*}+\mathrm{O}^{*}(\mathrm{P}) \tag{19}$$

$$\mathrm{OH}^{*}+\mathrm{O}^{*}(\mathrm{P})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{O}^{*}(\mathrm{P})+\mathrm{H}_{2} \mathrm{O} \tag{20}$$

![](./images/812526592621281282_12.jpg)

Figure 11. ORR elementary reactions when (a) $O_2$ is adsorbed on Co site, (b) $O_2$ is adsorbed on Co and P sites as bridge type and P is not poisoned, (c) when P site is poisoned by OH, and (d) when P site is poisoned by O.
Potential is 0 V. *(P) is used to marked the adsorption on P site.

![](./images/812526592621281282_13.jpg)

Figure 12. The migration of H from P site to Co site (a) before optimization in step 1, (b) after optimization in step 1, (c) before optimization in step 3, and (d) after optimization in step 3.

Compared with that on non-doped Co-$gN_4$, the ORR process on PNC-1 is promoted by intensifying the formation of OOH greatly. What's more, when P site is poisoned, formation of $H_2O_2$ is limited thermodynamically. The overpotential is 0.48 V.

Other P-doping sites are shown in Figure 2. When P atom is doped as PNC-4, bond breaking of $O_2$ is also observed and OH is hard to be formed on P site, which suggests P site is poisoned by O as what is found on PNC-1. ORR process on PNC-4 works as in steps (16)-(20) and is promoted because of greater $\Delta G$ of OOH formation as Figure S5. When P atom is doped at other sites, adsorptions of intermediates are similar with that on non-doped Co-$gN_4$ according to Table S2.

According to Table S2, ORR is influenced insignificantly if P is not doped next to N site. When P site is poisoned by OH, adsorptions on Co are intensified as those on SiNC-1 and SiNC-4. In Figure S7 and Table S4, when P site is poisoned by O on PNC-1, the adsorptions of $O_2$/O are weakened and adsorptions of OOH/OH are intensified, which could be also explained by

hydrogen bond. Hydrogen bond between O(P*) and OOH/OH stabilizes the adsorbates. O(P*) and $O_2$/O, which accept electrons from catalysts together (O's electronegativity is the highest in models), leads to weaker $O_2$/O adsorptions because of repulsive interaction. Thus, the potential-limiting step is promoted because energy released in OOH formation increases a lot. What's more, different effects on $O_2$/O adsorptions and OOH/OH adsorptions break the scaling relationship which limits the ORR process on catalysts. Similar with those on SiNC-1 and SiNC-4, adsorptions on PNC-4 are weaker because of space taken up by O*(P).

## ORR process on S-doped Co–gN₄
The bridge adsorption does not appear on SNC and OH adsorption on S site is weaker than that on Co site, which may come from the weak adsorption on S site. Thus, the Co is still the main active site in ORR process. O is adsorbed as two types in Figure 13 according to calculation and their ORR energy profiles are shown in Figure 14. It is indicated by the energy profile in Figure 14b that though OH desorption on S site is very easy, S site is more likely to be poisoned by O atom, because the reduction of O is a great endothermic process. Beside elementary reactions (1)–(5) as in Figure 14a, ORR elementary reactions could happen as shown in (11)–(15), of which S site is poisoned by O atom as Figure 15. Compared with non-doped Co–gN₄, the formation of OOH is intensified. The overpotential is 0.56 V.

$$\mathrm{O}_{2}+\mathrm{O}^{*}(\mathrm{S}) \rightarrow \mathrm{O} 2^{*}+\mathrm{O}^{*}(\mathrm{S}) \tag{21}$$

$$\mathrm{O}_{2}{ }^{*}+\mathrm{O}^{*}(\mathrm{S})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OOH}^{*}+\mathrm{O}^{*}(\mathrm{S}) \tag{22}$$

$$\mathrm{OOH}^{*}+\mathrm{O}^{*}(\mathrm{S})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{O}^{*}+\mathrm{O}^{*}(\mathrm{S})+\mathrm{H}_{2} \mathrm{O} \tag{23}$$

$$\mathrm{O}^{*}+\mathrm{O}^{*}(\mathrm{S})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{OH}^{*}+\mathrm{O}^{*}(\mathrm{S}) \tag{24}$$

$$\mathrm{OH}^{*}+\mathrm{O}^{*}(\mathrm{S})+\mathrm{H}^{+}+\mathrm{e}^{-} \rightarrow \mathrm{O}^{*}(\mathrm{S})+\mathrm{H}_{2} \mathrm{O} \tag{25}$$

![](./images/812526592621281282_14.jpg)

Figure 13. O atom is adsorbed (a) between Co and S sites (b) on S site. Yellow, S.

![](./images/812526592621281282_15.jpg)

Figure 14. ORR elementary reactions when (a) O is adsorbed between Co and P site (b) S site is not poisoned and O is adsorbed on S site. *(S) is used to marked the adsorption on S site.

![](./images/812526592621281282_16.jpg)

Figure 15. ORR elementary reactions when S site is poisoned by O. *(S) is used to marked the adsorption on S site.

Other S-doping sites are shown in Figure 2. When S atom is doped at SNC-4, O migration is also observed and the formation of OH on S site is a great endothermic process, which suggests S site may be poisoned by O as what is found on SNC-1. If S site is not poisoned, ORR works as described in (1)–(5) and adsorption is weaker than that of on non-doped Co–gN₄. If S site is poisoned by O, ORR works following elementary reactions (21)–(25) and adsorption is weaker than that of on non-doped Co–gN₄ as Figure S6. When S atom is doped at other sites, adsorptions of intermediates are similar with that on non-doped Co–gN₄ according to Table S3.

According to Table S3, ORR is influenced little by valance state. The effect of O on S site of SNC-1 and SNC-4 could be also understood by hydrogen bond as what is found in P-doped CoP in Figure S7 and Table S4.

## Conclusion
In summary, the influence of non-metal elements doping on Co–gN₄ is studied in our work. The formation of OOH is main limiting step on non-doped Co–gN₄. It is revealed that:
(1) The B doping leads to more electrons lost by Co site. Compared with that on non-doping Co–gN₄, adsorption of ORR intermediates on Co site is intensified under low B doping content. With B content increases, adsorption on Co site is weakened. Elementary reaction on B-doped Co–gN₄ could be described as in elementary reactions (1)–(5).
(2) The N doping leads to less electrons lost by Co site and weaker adsorption. With the N content increases, adsorptions of ORR intermediates change little. Compared with

that on non-doped Co−gN₄, 4e⁻ ORR process on N-doped Co−gN₄, which is described as in elementary reactions (1)–(5), is limited.

(3) When Si is coordinated with N, Si site is preferred to be poisoned by OH because of stronger interaction between O and Si. The ORR process on Si-doped Co−gN₄ could be describe as [6]–[10] and is promoted because of larger ΔG of OOH formation.

(4) When P site is coordinated with N, P site is preferred to be poisoned by OH at low potential and O at high potential. The OH on P site is a great proton donor for ORR process on Co site. ORR process on P-doped Co−gN₄ could be described by elementary reactions (1)–(5), (11)–(15) and (16)–(20). OOH formation is promoted by P doping.

(5) When S is coordinated with N, ORR process on S-doped Co−gN₄ is described by elementary reactions (1)–(5) or (21)–(25). The doping of sulfur intensifies formation of OOH on Co site.

(6) The difference between second-period-element doping and third-period-element doping may come from the hydrogen bond between OH and O on doped sites (Si/P/S) which could stabilize adsorbates (O₂/OOH/O/OH). What's more, the different effect on O₂/O adsorptions and OOH/OH adsorptions, which comes from O atom on P/S site, breaks the scaling relationship which limits the ORR process on catalysts.

This study not only reveals ORR mechanism on non-metal-element doping Co−gN₄, but also provides a theorical doping strategy to prepare modified carbon-based Co SACs with improved ORR activity.

## Acknowledgements

We acknowledge financial support by *The National Key Research and Development Program of China* (Grant Number 2018YFB1502700) and the computing resource of the High Performance Computing Center (HPCC) of Nanjing University.

## Conflict of Interest

The authors declare no conflict of interest.

**Keywords:** Oxygen Reduction Reaction · Density Functional Theory · Cobalt · Single Atom Catalyst · Doping

[1] J. D. Holladay, J. Hu, D. L. King, Y. Wang, *Catal. Today* **2009**, 139, 244–260.
[2] W. Lubitz, W. Tumas, *Chem. Rev.* **2007**, 107, 3900–3903.
[3] C. Wang, N. M. Markovic, V. R. Stamenkovic, *ACS Catal.* **2012**, 2, 891–898.
[4] H. A. Gasteiger, S. S. Kocha, B. Sompalli, F. T. Wagner, *Appl. Catal. B* **2005**, 56, 9–35.
[5] R. Tian, S. Shen, F. Zhu, L. Luo, X. Yan, G. Wei, J. Zhang, *ChemSusChem* **2018**, 11, 1015–1019.
[6] L. Luo, F. Zhu, R. Tian, L. Li, S. Shen, X. Yan, J. Zhang, *ACS Catal.* **2017**, 7, 5420–5430.
[7] L. Li, S. Shen, G. Wei, X. Li, K. Yang, Q. Feng, J. Zhang, *ACS Appl. Mater. Interfaces* **2019**, 11, 15, 14126–14135.
[8] C. Zhu, S. Fu, Q. Shi, D. Du, Y. Lin, *Angew. Chem. Int. Ed.* **2017**, 56, 13944–13960; *Angew. Chem.* **2017**, 129, 14132–14148.
[9] H. R. Byon, J. Suntivich, Y. Shao-Horn, *Chem. Mater.* **2011**, 23, 3421–3428.
[10] C. W. B. Bezerra, L. Zhang, K. Lee, H. Liu, A. L. B. Marques, E. P. Marques, H. Wang, J. Zhang, *Electrochim. Acta* **2008**, 53, 4937–4951.
[11] J. Chen, X. Yan, C. Fu, Y. Feng, C. Lin, X. Li, S. Shen, C. Ke, J. Zhang, *ACS Appl. Mater. Interfaces* **2019**, 11, 37779–37786.
[12] L. Li, S. Shen, X. Li, L. Luo, G. Wei, J. Zhang, *Int. J. Hydrogen Energy* **2020**, 45, 6563–6572.
[13] J. Li, M. Chen, D. A. Cullen, S. Hwang, M. Wang, B. Li, K. Liu, S. Karakalos, M. Lucero, H. Zhang, C. Lei, H. Xu, G. E. Sterbinsky, Z. Feng, D. Su, K. L. More, G. Wang, Z. Wang, G. Wu, *Nat. Can.* **2018**, 1, 935–945.
[14] D. Banhama, S. Ye, K. Pei, J. Ozaki, T. Kishimoto, Y. Imashiroc, *J. Power Sources* **2015**, 285, 334–348.
[15] X. X. Wang, D. A. Cullen, Y. T. Pan, S. Hwang, M. Wang, Z. Feng, J. Wang, M. H. Engelhard, H. Zhang, Y. He, Y. Shao, D. Su, K. L. More, J. S. Spendelow, G. Wu, *Adv. Mater.* **2018**, 30, 1706758.
[16] P. Yin, T. Yao, Y. Wu, L. Zheng, Y. Lin, W. Liu, H. Ju J Zhu, X. Hong, Z. Deng, G. Zhou, S. Wei, Y. Li, *Angew. Chem. Int. Ed.* **2016**, 55, 10800–10805; *Angew. Chem.* **2016**, 128, 10958–10963.
[17] H. Zhang, W. Zhou, T. Chen, B. Y. Guan, Z. Li, X. W. Lou, *Energy Environ. Sci.* **2018**, 11, 1980–1984.
[18] J. D. Yi, R. Xu, G. L. Chai, T. Zhang, K. Zang, B. Nan, H. Lin, Y. L. Liang, J. Lv, J. Luo, R. Si, Y. B. Huang, R. Cao, *J. Mater. Chem. A* **2019**, 7, 1252–1259.
[19] L. Yang, L. Shi, D. Wang, Y. Lv, D. Cao, *Nano Energy* **2018**, 50, 691–698.
[20] B. Delley, *J. Chem. Phys.* **2000**, 113, 7756–7764.
[21] J. P. Perdew, K. Burke, M. Ernzerhof, *Phys. Rev. Lett.* **1996**, 77, 3865–3868.
[22] S. Grimme, *J. Comb. Chem.* **2006**, 27, 1787.
[23] D. R. Hamann, M. Schluter, C. Chiang, *Phys. Rev. Lett.* **1979**, 43, 1494–1497.
[24] B. Hammer, J. K. Nørskov, *Nature* **1995**, 376, 238.
[25] J. K. Nørskov, T. Bligaard, A. Logadottir, J. R. Kitchin, J. G. Chen, S. Pandelov, U. Stimming, *J. Electrochem. Soc.* **2005**, 152, J23–J26.
[26] C. J. Cramer, *Essentials of computational chemistry: theories and models*, Wiley, New Jersey **2013**.
[27] X. Zhang, Z. Lu, Z. Yang, *Int. J. Hydrogen Energy* **2016**, 41, 21212–21220.
[28] X. Zhang, Z. Yang, Z. Lu, W. Wang, *Carbon* **2018**, 130, 112–119.
[29] E. M. Fernández, P. G. Moses, A. Toftelund, H. A. Hansen, J. I. Martínez, F. A. Pedersen, J. Kleis, B. Hinnemann, J. Rossmeisl, T. Bligaard, J. K. Nørskov, *Angew. Chem. Int. Ed.* **2008**, 47, 4683–4686; *Angew. Chem.* **2008**, 120, 4761–4764.

Manuscript received: October 20, 2020
Revised manuscript received: December 17, 2020
Accepted manuscript online: December 21, 2020
Version of record online: April 16, 2021