# Conversion mechanisms of peroxy linkage defect in silica optical fiber

Zhixing Peng$^{\text{a}}$, Pengfei Lu$^{\text{a},*}$, Baonan Jia$^{\text{a}}$, Jie Zhang$^{\text{a}}$, Binbin Yan$^{\text{a}}$, You Wang$^{\text{b}}$, Bin Yang$^{\text{c},*}$, Gang-Ding Peng$^{\text{d}}$

$^{\text{a}}$ State Key Laboratory of Information Photonics and Optical Communications, Beijing University of Posts and Telecommunications, POB 72, Beijing 100876, China
$^{\text{b}}$ Southwest Institute of Technical Physics, POB 432, Chengdu 610041, Sichuan, China
$^{\text{c}}$ High-Tech Research and Development Center, Ministry of Science and Technology, Beijing 100044, China
$^{\text{d}}$ School of Electrical Engineering & Telecommunications, University of New South Wales, NSW 2052, Sydney, Australia

---

## ARTICLE INFO

**Keywords:**
First principles
Silica fiber
POL defect
Conversion mechanism

## ABSTRACT

We present first principles calculations on conversion of a peroxy linkage (POL, $\equiv\mathrm{Si}-\mathrm{O}-\mathrm{O}-\mathrm{Si}\equiv$) defect. GW and Bethe-Salpeter equation methods are introduced. POL defect has different reaction paths when interacts with $\mathrm{H}_{2}$. It will convert into silanol ($\mathrm{Si}-\mathrm{OH}+\mathrm{Si}-\mathrm{OH}$) at the ground state ($\mathrm{S}_{0}$) and likely to transfer into $\mathrm{Si}-\mathrm{OOH}+\mathrm{Si}-\mathrm{H}$ at the triplet state ($\mathrm{T}_{1}$). Optical absorption strength of hydrogen-induced defects is higher than the POL defect between 6 and 8 eV and would be more easily lead to a laser-induced damage phenomenon. Our results not only display a better understanding of how $\mathrm{H}_{2}$ molecular interacts with the POL defect, but also provide a guidance to figure out these defects in silica fiber.

---

### 1. Introduction

With the rapid continuous development of the modern tele-communications industry, silica-based optical fiber and fiber-based optical devices have attracted numerous interest among experimental studies as well as theoretical studies [1,2]. Some intrinsic defects, such as the POL, peroxy radical (POR) and $\mathrm{E}'$ center *etc.* would be easily introduced into the silica-based fiber during the manufacturing process or by a high temperature treatment in oxygen-enriched environments [3]. Especially in laser irradiation or radiative environment, kinds of defects will damage the performance of optical fiber as well as its related devices and decrease the transmission efficiency of optical fiber [4-6]. These defects play a crucial role in affecting the optical property and cause an attenuation of the optical signal and a decrease of bandwidth.

One of the earliest experimental detection of the POL defect in silica was found by Nishikawa et al. [7]. And the formation of POL defect could through absorbing an interstitial oxygen by network. Many researchers devoted to studying the optical and electronic properties of POL defect [8-17]. POL defect remains a stable configuration in the $\mathrm{S}_{0}$ state, whereas it is unstable in the $\mathrm{T}_{1}$ state and it would break down into a POR defect and an $\mathrm{E}'$ center [18]. Raghavachari et al. calculated the transition energies which excited from the ground state to triplet state of several defect configurations in silica and provides a theoretical basis for our calculation [19,20]. Hydrogen is often used as a defect passivator during the manufacturing process of optical fiber or relevant optical devices [21]. The loading of hydrogen could reduce attenuation at visible to near-ultraviolet wavelengths and improve the depth of the deep ultraviolet region (DUV) effectively [22-27], it is also known to take place in plenty of reaction processes among amorphous $\mathrm{SiO}_{2}$ and $\mathrm{Si/SiO}_{2}$ interface [28-32]. In amorphous $\mathrm{SiO}_{2}$, El-Sayed et al. found that hydrogen atoms can interact with strained $\mathrm{Si-O}$ bond, forming with two distinct defect structures, which are referred to a $[\mathrm{SiO}_{4}/\mathrm{H}]^{0}$ center and a hydroxyl $\mathrm{E}'$ center [33,34]. Li et al. found $\mathrm{H}_{2}$ molecule can dissociates at an $\mathrm{E}'$ center to form a $\mathrm{Si-H}$ bond and an interstitial $\mathrm{H}$ atom [35].

As a result of radiation-induced process, $\mathrm{H}_{2}$ molecules may diffuse into the $\alpha-\mathrm{SiO}_{2}$ core of optical fiber and interact with intrinsic defects, forming with hydrogen-related passivated defects. The reaction between POL defects and $\mathrm{H}_{2}$ has different reaction paths. Generally, $\mathrm{H}_{2}$ could interact with $\mathrm{O-O}$ bond and thus the POL defects may be transformed into silanol ($\mathrm{Si-OH}$) groups [13,16,17]. On the other hand, $\mathrm{H}_{2}$ could break strained $\mathrm{Si-O}$ bond, resulting with a new defect consisting of a $\mathrm{Si-OOH}$ group and a hydrogen bridge defect ($\mathrm{Si-H}$) [33,36].

In this paper, we address the possible conversion paths between POL with $\mathrm{H}_{2}$ and analyze the geometry structure and formation energy of corresponding derivative defects. Hydrogen's reaction with POL defect may lead to two distinct hydrogen-related defects. We calculate the electronic structures and optical properties about all these defect configurations. Our paper is organized as follows. In *Section 2*, the computational methods and models are presented. Our results and discussion are given in *Section 3*. Finally, we give a brief summary in *Section 4*.

---

* Corresponding authors.
E-mail addresses: photon.bupt@gmail.com (P. Lu), yangb@htrdc.com (B. Yang).

https://doi.org/10.1016/j.jnoncrysol.2018.06.017
Received 5 April 2018; Received in revised form 5 June 2018; Accepted 8 June 2018
0022-3093/ Crown Copyright © 2018 Published by Elsevier B.V. All rights reserved.

![](./images/813028644074029057_1.jpg)

Fig. 1. (a) Typical POL defect configurations, (b) local structure of POL defect in ground (singlet) sate, (c) local structure of POL defect in triplet state, the Si atoms are yellow balls, the O atoms are red balls, the black dashed line in (c) refers to the broken bond of Si-O bond. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

## 2. Computational methods

The first-principles calculations presented in this framework are based on density functional theory (DFT) by using plane wave-pseudopotential code VASP (Vienna ab initio simulation package) [37, 38]. The projected augmented wave (PAW) method was employed to treat the interactions between core electrons and valence electrons [39, 40]. We used a 96-atoms silica fiber model, consisting of 32 Si atoms and 64 O atoms. This model was obtained by classical molecular dynamics (MD) simulations of quenching from a $2 \times 2 \times 2$ crystal silica supercell and its' density is in good agreement with experimental value of 2.20 g/$\text{cm}^3$ [27]. Defected structures, such as POL and its' hydrogen-induced defects, were built with this non-defective model as a precursor. The Tersoff potential is performed and the Langevin thermostat is expected to dominate the system temperature. Wave functions are expanded by using a plane wave basis with a cutoff energy of 450 eV. We set the value of Gaussian broadening as 0.1 eV and employ a $2 \times 2 \times 2$ k-point mesh for Brillouin zone integration. The optimization is accomplished by a relatively high accuracy that the ground state electronic convergence limit is at $10^{-5}$ eV. All the atomic positions and lattice structure were fully relaxed with the threshold of a maximum force of 0.01 eV/Å.

The climbing image nudged elastic band (CI-NEB) is an efficient method to determine the minimum energy path between a given initial and final position [41-43]. To study the reaction pathways, energy barriers were calculated by using the CI-NEB method [44]. We fully optimized the initial and final structures as well as intermediate images which linearly interpolated between them. The potential lowest energy configuration was searched along the reaction path and a convergence criterion of 0.01 eV/Å was applied. Many-body perturbation theory techniques are employed to calculate the quasi-particle energies and optical absorption spectra [45]. The GW (where G stands for one-particle Green function and W refers to screened Coulomb potential) approximation with a GW0 scheme are adopted to calculate electronic structure properties, a Bathe-Salpeter-equation (BSE) method based upon the quasi-particle scGW0 calculations are expected to obtain the optical properties [46, 47]. We take into consider the attraction between quasi-electron and quasi-hole solving by BSE method. The precision of GW-BSE calculation is within 0.1 eV.

## 3. Results and discussion

### 3.1. Geometry structures

During the manufacturing process of the silica optical fiber in an oxygen-enriched environment, the network would probably absorbs interstitial oxygen atoms and lead to the formation of POL (Si-O-O-Si) [48-50]. We analyzed the typical POL defect configuration (Fig. 1(a)), and then the configuration of the POL defect was optimized in the $S_0$ state and the $T_1$ state in Fig. 1(b) and Fig. 1(c), respectively. After optimized with the $S_0$ state, the calculation shows that the POL defect is stable, and local atomic structure is similar with peroxide molecule ($\text{H}_2\text{O}_2$) [13, 14, 51]; the mean distance of O-O bond is about $1.50$ Å which is close to the O-O bond length in the gaseous hydrogen peroxide molecule ($1.46$ Å) [52]; the length of the Si-O bond is around $1.68$ Å which is a little bit higher than the corresponding bond length in a non-defective configuration. The angle of Si-O-O is approximately $102.15^\circ$. While after having a geometry optimization with the $T_1$ state, the POL defect would be in a unstable state and break down into a peroxy radical (POR) defect and a generic $E'$ center. The distance of O-O bond is reduced to $1.38$ Å, it means that the breakage of the Si-O bond lead to the enhancement of O-O bond in the $T_1$ state.

The injection of hydrogen can effectively improve the depth of the deep ultraviolet region (DUV) [22-26]. Meanwhile, the strained Si-O bonds, O-O bonds are thought to be cleaved more easily in radiation/laser-induced processes and would be more chemically active when interact with hydrogen molecules. The POL defects may be transformed into -OH or -OOH groups during hydrogen annealing following the reactions:

$$\equiv \mathrm{Si-O-O-Si} \equiv+\mathrm{H}_{2} \rightarrow \equiv \mathrm{Si-OH}+\equiv \mathrm{Si-OH} \tag{1}$$

$$\equiv \mathrm{Si-O-O-Si} \equiv+\mathrm{H}_{2} \rightarrow \equiv \mathrm{Si-OOH}+\equiv \mathrm{Si-H} \tag{2}$$

Fig. 2 shows the two hydrogen-induced defect configurations of POL, which refers to two reactions' products of Reaction (1)-(2).The first defect configuration ($\text{Si-OH} + \equiv\text{Si-OH}$) in Fig. 2(a) is typically formed when hydrogen molecule interacts with elongated O - O bonds, for the O - O bonds are likely to be broken by laser irradiation. It is formed with a three-coordinated Si linked with a hydroxyl and the mean distance of Si-O bonds and O-O bonds are $1.64$ Å and $0.97$ Å, respectively. The decline of Si-O bond length is probably caused by the elongated O-O bond. Meanwhile, $\text{H}_2$ molecule would also interact with a strained Si-O bond, forming a peroxy ($\equiv\text{Si-OOH}$) and a hydrogen-bridge defect ($\equiv\text{Si-H}$) as well. Especially for the $T_1$ state, the POL defect would present another conversion path and the defect would likely to convert into a peroxy $\equiv\text{Si-OOH}$ and a $\equiv\text{Si-H}$ defect. After optimization, the Si-H bond averages at $1.47$ Å which perfectly matches with Ref [33], where the Si-O bond, O-O bond and O-H bond average at $1.69$ Å, $1.46$ Å and $0.98$ Å, respectively.

### 3.2. Formation energy and conversion path

In order to investigate interconversion process of defects, we set 32 POL configurations and calculate reaction pathways, average formation energy and conversion intermediate structures to determine energy barriers. The average formation energy $(E_f)$ is defined as

![](./images/813028644074029057_2.jpg)

Fig. 2. Local structure of H-induced defects of POL configuration, (a) local structure of silanol configuration (Si-OH + Si-OH), (b) the local structure of Si-OOH + Si-H configuration, the Si atoms are yellow balls, the O atoms are red balls, H atoms are white balls.

<table>
<caption>Table 1 Average Formation energy of the two hydrogen-induced defects.</caption>
<thead>
<tr>
<th>Initial state → final state</th>
<th>Transition state I</th>
<th>Transition state II</th>
<th>Formation Energy(eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>POL + H₂ → ≡ Si - OH + ≡ Si - OH</td>
<td>Si - O··O - Si + H₂</td>
<td>Si - O··O - Si + H··H</td>
<td>0.51(eV)</td>
</tr>
<tr>
<td>POL + H₂ → ≡ Si - OOH + ≡ Si - H</td>
<td>Si··O - O - Si + H₂</td>
<td>Si··O - O - Si + H··H</td>
<td>4.20(eV)</td>
</tr>
</tbody>
</table>

$E_{\mathrm{f}}=E_{\mathrm{POL}}+E_{\mathrm{H}_{2}}-E_{\text{defect}}$. Where $E_{POL}$ is the total energy of POL configuration, $E_{defect}$ indicate the energy of hydrogen-induced defect of POL which mentioned in Reaction (1)-(2), and $E_{H_{2}}$ is the energy of an isolated hydrogen molecule.

For the POL defect, the rupture of Si-O bond and O-O bond need different input energy, thus the formation energy of two hydrogen-induced defects are different. Table 1 lists two reaction paths and corresponding transition state configurations and relative energy as well as formation energy of hydrogen-induced defects.

In order to further reveal the conversion paths and average energy barriers from POL to corresponding hydrogen-induced defect, we calculate the energy of transition states to define the energy paths of the POL configuration to the hydrogen-induced defect configurations by means of the CI-NEB method. The CI-NEB calculation from initial state to transition state and then to final defect structure are performed by using separated images. Fig. 3 illustrates the total energy, local structure of initial state/final state as well as the transition state configurations.

The conversion path, which start from initial state (POL+ H₂) to transition state I, transition state II and then to the final state (Fig. 3), could illustrate state transition and average barrier of reactions. Fig. 3(a) shows interconversion process as well as its' energy barrier of Reaction (1) and we set four intermediate state configuration to simulate the reaction process. In this path, the first structure conversion is the departure of two O atoms with the breaking of O - O bond, namely indicates initial state converts to transition state I, the average energy barrier of this conversion is approximately at 1.31 eV, along with O-O distance increases from $1.50\mathring{A}$ to $1.83\mathring{A}$. And the second structure conversion is the breaking of H-H bond which refers to the interconversion from transition state I (Si - O··O - Si + H₂) to transition state II (Si - O··O - Si + H··H). Average energy barrier between transition state I and transition state II is 0.66 eV, accompany with interstitial H₂ molecule splitting into two hydrogen atoms. In the final conversion, the free hydrogen atoms would interact with dangling oxygen bonds to form the silanol configuration. The reaction from transition state II to the final state (Si-OH + Si-OH) is exothermic.

Another conversion path is showed in Fig. 3(b). Similarly, we also set four intermediate state configurations which marked with black dots. The first conversion the breaking of Si - O bond and average energy barrier from the initial state to the transition state I (Si··O - O - Si + H₂) is 3.72 eV, accompanied with the elongating of Si-O bond from $1.68\mathring{A}$ to $2.50\mathring{A}$. The next process is from the transition state I to the transition state II (Si··O - O - Si + H··H) and its' transition energy barrier is 0.67 eV [33, 56], the H₂ molecule would

![](./images/813028644074029057_3.jpg)

Fig. 3. (a) Conversion path from initial state (POL + H₂) to final state silanol (Si-OH + Si-OH) configuration, (b) Conversion path from initial state (POL + H₂) to final state Si-OOH + Si-H configuration; Black dot: image energies in the transition. Black solid line: spline interpolated. Intersected images: atom structures (only local structures are shown).

split into free hydrogen atoms. In the final process, the hydrogen atoms interact with the dangling bonds and form the final configuration (Si−OOH + Si−H).

Finally, the average formation energy of Si−OOH + Si−H configuration (4.20 eV) is higher than the silanol configuration (0.51 eV) and the silanol configuration is more likely to be formed. Whereas, under the irradiation of ArF or F₂ laser (7.9 eV), all above conversions might take place.

### 3.3. Electronic structure and optical property

For a non-defective structure, the calculated band gap by GW + BSE method is 9.66 eV which is in a good agreement with the measured threshold in silica [27], Vella et al. have evidenced that amorphous SiO₂ features an indirect gap near 9 eV [57]. The calculated total density of states (DOS) and optical absorption spectra (OA) of the POL defect configuration and its' hydrogen-induced defects, including silanol configuration as well as the Si−OOH + Si−H configuration, are shown in Fig. 4 and Fig. 5. For the POL defect model, there is one unoccupied defect state at 8.67 eV and two occupied defect states at −0.48 eV, −0.24 eV near the Fermi energy level, which is approximately matched with the results in Ref [17], the lower occupied defect state is at 0.21 eV above top of valence band (TVB) while the higher occupied defect state is at 0.45 eV. As is showed in the black dashed line in Fig. 4 or Fig. 5, we analyzed the optical properties of the POL configuration and found that defect states cause a weak absorption band with peaks at 6.47 eV and 7.66 eV; their oscillator strengths (f) are 0.0002, and 0.019, respectively. Experimentally, Imai et al. analyzed absorption property of oxygen-related defects in silica and attributed a low-intensity absorption band between 6.5 and 7.8 eV to the POL defect which is almost matched with our calculations [53]. And our calculations is in accordance with Pacchioni's et al. results [13]. While Nishikawa et al. [7] and Sakurai et al. [54] observed optical absorption band at 3.8 eV and their opinions about the POL defect is the cause of 3.8 eV band is not support by the calculation results.

To better comprehend the properties of two hydrogen-induced defect configurations, we compared the DOS and OA with the POL defect configuration. In Fig. 4, we illustrate the DOS and OA properties of the silanol configuration in red line. We observed that there was only one occupied defect states located at −0.21 eV near the Fermi level and two unoccupied levels appear at 10.23 eV and 10.38 eV, indicated with a', c', d', respectively. The bottom of the conduction band (BCB) is labeled with b' which located at 8.85 eV. On the top of Fig. 4, we depicted the optical properties of two configurations. We also found that transition between the defects states cause three weak absorption peak at 7.07 eV, 7.44 eV and 8.03 eV, indicated with A', B', C', respectively.

![](./images/813028644074029057_4.jpg)

Fig. 4. Calculated DOS (bottom) and optical absorption spectra (top) of POL defect in black dashed line and the silanol configuration in red line. Insert shows a magnified view of the spectrum between 5 and 8 eV.

![](./images/813028644074029057_5.jpg)

Fig. 5. Calculated DOS (bottom) and optical absorption spectra (top) of POL defect in black dashed line and the Si−OOH + Si−H configuration in red line. Insert shows a magnified view of the spectrum between 5 and 8 eV.

In Fig. 5, we also illustrate the DOS and OA properties of the Si−OOH + Si−H configuration in red line. Similar to the silanol configuration, there is also only one occupied defect state, which located at −0.24 eV (a'') and the defect state is at 0.66 eV above the TVB. The BCB and two unoccupied defect states is located at 8.49 eV, 9.69 eV and 10.11 eV, which labeled with b'', c'', d''. As showed in Fig. 5, there are three absorption peaks A'', B'', C'' at around 6.37 eV, 7.17 eV and 7.51 eV. These absorptions are produced by quasi-degenerate excitations with exciton binding energy of about 1.86 eV. The transitions in the range of 6–8 eV, might originating from the transition between the occupied defect level (a'') and the BCB (b'') as well as the unoccupied defect levels (c'', d''). Between the range of 6–8 eV, the optical absorption intensity of the silanol configuration or Si−OOH + Si−H configuration is higher than the POL defect configuration, which means it would more easily to lead to a laser-induced damage of the optical material.

First of all, there have been some studies suggesting that the POL defects are likely to be the precursors of silanol configurations [17,55]. Nishikawa et al. found the POL defect could transformed into a POR and E' center defect pair [7], and Wang et al. also proved that the POL defects could be the precursors of POR-E' defect center in a specific state [51]. Furthermore, we present one of the conversion path that POL can transformed into the Si−OOH + Si−H configuration with H₂ molecule. In Table 1, we give the formation energies of two distinct conversion paths, as the formation energy of silanol configuration is only 0.51 eV, which is much larger than the Si−OOH + Si−H configuration (4.20 eV). As suggested by the Fig. 3 that the energy barrier of breaking a strain Si−O bond is 3.72 eV, while breaking a strained O−O bond is only 1.31 eV. So the concentration of Si−OOH + Si−H

configuration should be much less than the silanol configurations. Meanwhile, in Fig. 4 and Fig. 5, we calculated the electronic density of states and optical properties of the three configuration. From the calculation we found the occupied defect state of two hydrogen-induced configuration is reduced. During the range of 6-8 eV, there still have been some low-intensity optical absorption bands and, interestingly, presenting a red shift phenomenon in optical absorption spectral compared with the POL defect.

## 4. Conclusion
In summary, classical MD and GW/BSE methodologies are used to figure out the geometry, electronic properties and optical properties of the POL defect as well as its' hydrogen-induced defects. We analyzing the different reaction pathways and interconversion mechanism between the POL defect and hydrogen-induced defects by CI-NEB method. After the treatment with H₂, the POL defect configuration would more likely to convert into the silanol configuration (Si-OH + Si-OH) at the ground state. Meanwhile, it would convert into the Si-OOH + Si-H configuration at the triplet state. Our results show that the electronic and optical properties of the POL defect are roughly similar with its' H-induced defects, the defect levels of all configurations are located close to the TVB. But the optical absorption strength between 6 and 8 eV of hydrogen-induced defects is higher than the POL defect. Our calculations provide precise analysis and useful instructions to interaction in silica fiber, which is of remarkable significance to improve laser-induced damage performance.

## Acknowledgements
This work was supported by the National Key Research and Development Program of China (No.2017YFB0405100).

We acknowledge the computational support from the Beijing Computational Science Research Center (CSRC) and the National Natural Science Foundation of China (61675032).

## References
[1] R.P. Gupta, Electronic structure of crystalline and amorphous silicon dioxide, Phys. Rev. B 32 (1985) 8278.
[2] J. Samthein, A. Pasquarello, R. Car, Structural and electronic properties of liquid and amorphous SiO₂: an ab initio molecular dynamics study, Phys. Rev. Lett. 74 (1995) 4682.
[3] R.A.B. Devine, The Physics and Technology of Amorphous SiO₂, Springer, US, 1988.
[4] A. Salleo, S.T. Taylor, M.C. Martin, W.R. Panero, R. Jeanloz, T. Sands, F.Y. Génin, Laser-driven formation of a high-pressure phase in amorphous silica, Nat. Mater. 2 (2003) 796.
[5] A. Salleo, T. Sands, F.Y. Génin, Machining of transparent materials using an IR and UV nanosecond pulsed laser, Appl. Phys.A 71 (2000) 601-608.
[6] F.R. Wang, Laser induced rear-surface-crack damage properties of fused silica etched with HF solution, Acta Phys. Sin. 59 (2010) 5122-5127.
[7] H. Nishikawa, R. Tohmon, Y. Ohki, K. Nagasawa, Y. Hama, Defects and optical absorption bands induced by surplus oxygen in high-purity synthetic silica, J. Appl. Phys. 65 (1989) 4672-4678.
[8] L. Skuja, M. Hirano, H. Hosono, K. Kajihara, Defects in oxide glasses, physica status solidi (c), vol. 2, (2005), pp. 15-24.
[9] K. Kajihara, L. Skuja, H. Hosono, Diffusion and reactions of photoinduced interstitial oxygen atoms in amorphous SiO₂ impregnated with 18O-labeled interstitial oxygen molecules, J. Phys. Chem. C 118 (2014) 4282-4286.
[10] D. Di Francesca, S. Agnello, S. Girard, C. Marcandella, P. Paillet, A. Boukenter, Y. Ouerdane, F. Gelardi, Influence of O-loading pretreatment on the radiation response of pure and fluorine-doped silica-based optical fibers, IEEE Trans. Nucl. Sci. 61 (2014) 3302-3308.
[11] A. Mehonic, M. Buckwell, L. Montesi, L. Garnett, S. Hudziak, S. Fearn, R. Chater, D. Mcphail, A.J. Kenyon, Structural changes and conductance thresholds in metal-free intrinsic SiOx resistive random access memory, J. Appl. Phys. 117 (2015) 124505.
[12] E.P. O'Reilly, J. Robertson, Theory of defects in vitreous silicon dioxide, Phys. Rev. B 27 (1983) 3780.
[13] G. Pacchioni, G. Ieraño, Ab initio theory of optical transitions of point defects in SiO 2, Phys. Rev. B 57 (1998) 818.
[14] Y. Chabal, M. Weldon, Y. Caudano, B. Stefanov, K. Raghavachari, Spectroscopic studies of H-decorated interstitials and vacancies in thin-film silicon exfoliation, Phys. B Condens. Matter 273 (1999) 152-163.

[15] M.A. Szymanski, A.L. Shluger, A.M. Stoneham, Role of disorder in incorporation energies of oxygen atoms in amorphous silica, Phys. Rev. B 63 (2001) 224207.
[16] D. Ricci, G. Pacchioni, M.A. Szymanski, A.L. Shluger, A.M. Stoneham, Modeling disorder in amorphous silica with embedded clusters: the peroxy bridge defect center, Phys. Rev. B 64 (2001) 224104.
[17] B. Winkler, L. Martin-Samos, N. Richard, L. Giacomazzi, A. Alessi, S. Girard, A. Boukenter, Y. Ouerdane, M. Valant, Correlations between structural and optical properties of peroxy bridges from first principles, J. Phys. Chem. C 121 (2017) 4002-4010.
[18] R. Su, H. Zhang, S.L. Jiang, J. Chen, W. Han, Quasi-particle calculations on electronic and optical properties of the peroxy linkage and neutral oxygen vacancy defects in amorphous silica, Acta Phys. Sin. 65 (2016) 027801.
[19] B.B. Stefanov, K. Raghavachari, Photoabsorption of the peroxide linkage defect in silicate glasses, J. Chem. Phys. 111 (1999) 8039-8042.
[20] K. Raghavachari, G. Pacchioni, Photoabsorption of dioxasilanylene and silanone groups at the surface of silica, J. Chem. Phys. 114 (2001) 4657-4662.
[21] D.M. Fleetwood, R.D. Schrimpf, Defects in Microelectronic Materials and Devices, CRC Press, 2008.
[22] D. Sempolinski, T. Seward, C. Smith, N. Borrelli, C. Rosplock, Effects of glass forming conditions on the KrF-excimer-laser-induced optical damage in synthetic fused silica, J. Non-Cryst. Solids 203 (1996) 69-77.
[23] M. Shimbo, T. Nakajima, N. Tsuji, T. Kakuno, T. Obara, Estimation of the life of synthetic silica glass under long time irradiation by ArF excimer laser, Jpn. J. Appl. Phys. 38 (1999) L848.
[24] M. Oto, S. Kikugawa, T. Miura, M. Hirano, H. Hosono, Fluorine doped silica glass fiber for deep ultraviolet light, J. Non-Cryst. Solids 349 (2004) 133-138.
[25] H. Hosono, Y. Abe, H. Imagawa, H. Imai, K. Arai, Experimental evidence for the Si-Si bond model of the 7.6-eV band in SiO 2 glass, Phys. Rev. B 44 (1991) 12043.
[26] H. Imai, K. Arai, H. Hosono, Y. Abe, T. Arai, H. Imagawa, Dependence of defects induced by excimer laser on intrinsic structural defects in synthetic silica glasses, Phys. Rev. B 44 (1991) 4812.
[27] Z. Weinberg, G. Rubloff, E. Bassous, Transmission, photoconductivity, and the experimental band gap of thermally grown SiO₂ films, Phys. Rev. B 19 (1979) 3107.
[28] E. Cartier, J. Stathis, D. Buchanan, Passivation and depassivation of silicon dangling bonds at the Si/SiO₂ interface by atomic hydrogen, Appl. Phys. Lett. 63 (1993) 1510-1512.
[29] J. Stathis, E. Cartier, Atomic hydrogen reactions with P b centers at the (100) Si/ SiO₂ interface, Phys. Rev. Lett. 72 (1994) 2745.
[30] H. Henschel, O. Kohn, U. Weinand, Radiation hardening of pure silica optical fibers by high-pressure hydrogen treatment, IEEE Trans. Nucl. Sci. 49 (2002) 1401-1409.
[31] J. Suñé, E. Wu, Quantitative two-step hydrogen model of SiO2 gate oxide breakdown, Solid State Electron. 46 (2002) 1825-1837.
[32] G. Pobegen, M. Nelhiebel, T. Grasser, Detrimental impact of hydrogen passivation on NBTI and HC degradation, Reliability Physics Symposium (IRPS), IEEE International, IEEE, 2013, pp. XT. 10.11-XT. 10.16 2013.
[33] A.-M. El-Sayed, Y. Wimmer, W. Goes, T. Grasser, V.V. Afanas, A.L. Shluger, Theoretical models of hydrogen-induced defects in amorphous silicon dioxide, Phys. Rev.B 92 (2015) 014107.
[34] A.-M. El-Sayed, M.B. Watkins, T. Grasser, V.V. Afanas'Ev, A.L. Shluger, Hydrogen-induced rupture of strained Si- O bonds in amorphous silicon dioxide, Phys. Rev. Lett. 114 (2015) 115503.
[35] Z. Li, S. Fonash, E. Poindexter, M. Harmatz, F. Rong, W. Buchwald, Hydrogen annealing of E' centers in thermal SiO2 on Si, J. Non-Cryst. Solids 126 (1990) 173-176.
[36] T. Bakos, S. Rashkeev, S. Pantelides, H₂O and O₂ molecules in amorphous SiO₂: defect formation and annihilation mechanisms, Phys. Rev. B 69 (2004) 195206.
[37] G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47 (1993) 558.
[38] G. Kresse, J. Hafner, Ab initio molecular-dynamics simulation of the liquid-metal-amorphous-semiconductor transition in germanium, Phys. Rev. B 49 (1994) 14251.
[39] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953.
[40] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758.
[41] K. Tibbetts, C.R. Miranda, Y.S. Meng, G. Ceder, An ab initio study of lithium diffusion in titanium disulfide nanotubes, Chem. Mater. 19 (2007) 5302-5308.
[42] S.-h. Wen, Z. Hou, K.-L. Han, Mo - S - I nanowires: a promising anode material for Lithium-ion batteries. A first-principles study, J. Phys. Chem. C 113 (2009) 18436-18440.
[43] B. Peng, F. Cheng, Z. Tao, J. Chen, Lithium transport at silicon thin film: barrier for high-rate capability anode, J. Chem. Phys. 133 (2010) 034701.
[44] G. Henkelman, B.P. Uberuaga, H. Jónsson, A climbing image nudged elastic band method for finding saddle points and minimum energy paths, J. Chem. Phys. 113 (2000) 9901-9904.
[45] L. Martin-Samos, G. Bussi, SaX: an open source package for electronic-structure and optical-properties calculations in the GW approximation, Comput. Phys. Commun. 180 (2009) 1416-1425.
[46] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865.
[47] G. Onida, L. Reining, A. Rubio, Electronic excitations: density-functional versus many-body Green's-function approaches, Rev. Mod. Phys. 74 (2002) 601.
[48] D. Hamann, Diffusion of atomic oxygen in SiO 2, Phys. Rev. Lett. 81 (1998) 3447.
[49] G. Pacchioni, G. Ieranò, Ab initio formation energies of point defects in pure and Ge-doped SiO 2, Phys. Rev. B 56 (1997) 7304.
[50] H. Nishikawa, T. Shiroyama, R. Nakamura, Y. Ohki, K. Nagasawa, Y. Hama, Photoluminescence from defect centers in high-purity silica glasses observed under 7.9-eV excitation, Phys. Rev.B 45 (1992) 586.

[51] W. Wang, P. Lu, L. Han, C. Zhang, L. Wu, P. Guan, R. Su, J. Chen, Structural and electronic properties of peroxy linkage defect and its interconversion in fused silica, J. Non-Cryst. Solids 434 (2016) 96-101.

[52] K.L. Bak, J. Gauss, P. Jørgensen, J. Olsen, T. Helgaker, J.F. Stanton, The accurate determination of molecular equilibrium structures, J. Chem. Phys. 114 (2001) 6548-6556.

[53] H. Imai, K. Arai, T. Saito, S. Ichimura, H. Nonaka, J. Vigouroux, H. Imagawa, H. Hosono, Y. Abe, UV and VUV optical absorption due to intrinsic and laser in- duced defects in synthetic silica glasses, The Physics and Technology of Amorphous SiO₂, Springer, 1988, pp. 153-159.

[54] Y. Sakurai, K. Nagasawa, Correlation between 1.5 eV photoluminescence-band and 3.8 eV absorption band in silica glass, J. Non-Cryst. Solids 261 (2000) 21-27.

[55] R. Salh, Defect related luminescence in silicon dioxide network: a review, in: crystalline silicon-properties and uses, INTECH 43 (2011) 205-210.

[56] F. Messina, M. Cannas, Character of the reaction between molecular hydrogen and a silicon dangling bond in amorphous SiO2, J. Phys. Chem. C 111 (2007) 6663-6667.

[57] E. Vella, F. Messina, M. Cannas, R. Boscaino, Unraveling exciton dynamics in amorphous silicon dioxide: interpretation of the optical features from 8 to 11 Ev, Phys. Rev. B 83 (2011) 174201.