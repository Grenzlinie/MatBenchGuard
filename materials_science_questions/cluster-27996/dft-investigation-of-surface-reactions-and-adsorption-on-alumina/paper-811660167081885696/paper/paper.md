# Methanol dehydrogenation on Rh(1 1 1): A density functional and microkinetic modeling study

Ruibin Jiang$^{\mathrm{a}}$, Wenyue Guo$^{\mathrm{a},*}$, Ming Li$^{\mathrm{a}}$, Houyu Zhu$^{\mathrm{a}}$, Lianming Zhao$^{\mathrm{a}}$, Xiaqing Lu$^{\mathrm{c}}$, Honghong Shan$^{\mathrm{b},*}$

$^{\mathrm{a}}$ College of Physics Science and Technology, China University of Petroleum, Dongying, Shandong 257061, PR China
$^{\mathrm{b}}$ College of Chemistry and Chemical Engineering, China University of Petroleum, Dongying, Shandong 257061, PR China
$^{\mathrm{c}}$ Department of Physics and Materials Science, City University of Hong Kong, Hong Kong, China

---

## ARTICLE INFO

**Article history:**
Received 9 December 2010
Received in revised form 13 May 2011
Accepted 16 May 2011
Available online 23 May 2011

**Keywords:**
Methanol
Dehydeogenation
Rh(1 1 1)
Catalysis
Density functional theory
Mocrokinetic modeling

---

## ABSTRACT

Rh(1 1 1)-catalyzed methanol dehydrogenation is systematically studied based on density functional (DF) calculations and microkinetic modelings. We find that, compared to those for the same reaction on other transition metal surfaces, e.g., Ni(1 1 1), Pd(1 1 1) and Pt(1 1 1), the adsorption configurations of some relevant intermediates on Rh(1 1 1) are relatively abundant and the adsorption potential energy surfaces (PES) are relatively flat. Transition states for all the possible elementary steps involved are searched. Based on the DF results, we model the reaction at two sets of typical reaction conditions, i.e., the low temperatures in ultrahigh vacuum conditions and the high temperature and high pressure conditions. The DF calculations and microkinetic modelings reveal that paths $\mathrm{CH_3OH \to CH_3O \to CH_2O \to CHO \to CO}$ and $\mathrm{CH_3OH \to CH_2OH \to CHOH \to CHO \to CO}$ are dominant under all the reaction conditions, whereas at the high temperatures and high pressures, paths $\mathrm{CH_3OH \to CH_2OH \to CH_2O \to CHO \to CO}$ and $\mathrm{CH_3OH \to CH_2OH \to CHOH \to COH \to CO}$ are also significant. Under all the considered reaction conditions, apparent activation energy for the methanol decomposition is found to decrease with temperature, and the reaction order of methanol is decreased when increasing its partial pressure. In addition, it is found that it is the very activated adsorption state ($\eta^1(\mathrm{C})-\eta^1(\mathrm{O})-\eta^1(\mathrm{H})$) for formaldehyde on Rh(1 1 1) that results in the fact that methanol oxidation does not take place at formaldehyde.

© 2011 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Global energy shortage and stringent emission regulations have stimulated extensive research and development in the area of fuel cells. Hydrogen fueled proton exchange membrane fuel cells (PEMFC) have been attractive candidates in the low-emission automotive applications [1,2]. Owing to the problems concerning the handling and storage of hydrogen, extensive research has been dedicated to developing technologies for on-board hydrogen production from liquid fuels. In this respect, methanol has been considered as a promising fuel due to the abundant source as well as the high hydrogen-to-carbon ratio [3]. Producing hydrogen from methanol involves several practical routes, e.g., decomposition (MD), steam re-forming (MSR), oxidative steam reforming (OSRM) and partial oxidation (POM).

Rhodium is an excellent catalyst in some industrial catalytic processes, including partial oxidation of methane and POM [4–6].

In order to gain fundamental insight into the POM mechanism, methanol decomposition on the single-crystal Rh(1 1 1) surface at low temperatures under ultrahigh vacuum (UHV) condition has been extensively studied [7,8]. The results showed that methanol adsorbed molecularly on Rh(1 1 1), and began to decompose into methoxy at 140 K in a heating process [8]. Intermediate methoxy was suggested to hydrogenate to methanol or dehydrogenate to adsorbed CO and H by Solymosi et al. [7]; whereas Houtman and Barteau believed it is exclusively decomposed to CO and H [8]. In both studies [7,8], in addition to methoxy, no other intermediates were observed; and the final products were exclusively CO and $\mathrm{H_2}$. On oxygen pre-adsorbed Rh(1 1 1), oxidation still mainly occurred at CO, with that at the formaldehyde intermediate negligible [8].

On the other hand, there are several studies for methanol decomposition and oxidation on rhodium at high temperatures and high (up to ambient) partial pressures, which correspond to the practically catalytically relevant conditions [5,6,9]. These studies demonstrated that products for methanol decomposition at these conditions are also CO and $\mathrm{H_2}$. Experiments also showed that the measurable conversion of methanol begins at a significantly lower temperature (550 K), and the conversion reaches a flux limited value at about 900 K [6]. In the presence of $\mathrm{O_2}$, methanol also

---

* Corresponding authors. Tel.: +86 546 839 6319; fax: +86 546 839 7511.
E-mail addresses: wyguo@hdpu.edu.cn (W. Guo), shanhh@hdpu.edu.cn (H. Shan).

1381-1169/$ – see front matter © 2011 Elsevier B.V. All rights reserved.
doi:10.1016/j.molcata.2011.05.007

<table><thead><tr><th>Species</th><th>Configurationª</th><th>Eadsb</th><th>dC–O</th><th>dX–Rh</th><th>Anglesf</th></tr></thead><tbody><tr><td>CH₃OH*</td><td>top−η¹(O)</td><td>14.8 (13.4)</td><td>1.43</td><td>2.28c</td><td>54</td></tr><tr><td>CH₃O*</td><td>fcc−η³(O)</td><td>57.2 (52.8)</td><td>1.41</td><td>2.18c,2.18c,2.18c</td><td>0</td></tr><tr><td></td><td>hcp−η³(O)</td><td>54.4 (50.2)</td><td>1.41</td><td>2.19c,2.19c,2.20c</td><td>3</td></tr><tr><td></td><td>bridge−η²(O)</td><td>56.0 (52.1)</td><td>1.40</td><td>2.14c,2.14c</td><td>53</td></tr><tr><td></td><td>top−η¹(O)</td><td>52.0 (49.5)</td><td>1.35</td><td>2.01c</td><td>78</td></tr><tr><td>CH₂OH*</td><td>bridge−η¹(C)−η¹(O)</td><td>52.4 (49.8)</td><td>1.46</td><td>2.26c,2.05d</td><td>86</td></tr><tr><td>CH₂O*</td><td>fcc−η¹(C)−η²(O)</td><td>24.2 (22.2)</td><td>1.37</td><td>2.18c,2.18c,2.08d</td><td>80</td></tr><tr><td></td><td>hcp−η¹(C)−η²(O)</td><td>24.6 (23.0)</td><td>1.38</td><td>2.16c,2.16c,2.07d</td><td>80</td></tr><tr><td></td><td>fcc−η¹(C)−η¹(O)−η¹(H)</td><td>21.5 (21.2)</td><td>1.31</td><td>2.06c,2.12d,1.83e</td><td>83</td></tr><tr><td></td><td>hcp−η¹(C)−η¹(O)−η¹(H)</td><td>22.0 (22.0)</td><td>1.31</td><td>2.06c,2.11d,1.79e</td><td>82</td></tr><tr><td></td><td>fcc−η²(C)−η¹(O)</td><td>20.0 (20.6)</td><td>1.30</td><td>2.08c,2.32d,2.32d</td><td>80</td></tr><tr><td>CHOH*</td><td>top−η¹(C)</td><td>80.3 (78.1)</td><td>1.31</td><td>1.87d</td><td>53</td></tr><tr><td></td><td>bridge−η²(C)</td><td>79.6 (78.0)</td><td>1.35</td><td>2.06d,2.06d</td><td>45</td></tr><tr><td>CHO*</td><td>fcc−η²(C)−η¹(O)</td><td>59.8 (57.0)</td><td>1.28</td><td>2.11c,2.09d,2.11d</td><td>75</td></tr><tr><td></td><td>hcp−η²(C)−η¹(O)</td><td>59.8 (57.1)</td><td>1.26</td><td>2.11c,2.10d,2.10d</td><td>75</td></tr><tr><td></td><td>bridge−η¹(C)−η¹(O)</td><td>64.0 (60.8)</td><td>1.25</td><td>2.19c,1.92d</td><td>82</td></tr><tr><td>COH*</td><td>fcc−η³(C)</td><td>106.7 (98.7)</td><td>1.32</td><td>1.98d,1.99d,2.05d</td><td>0</td></tr><tr><td></td><td>hcp−η³(C)</td><td>110.2 (106.8)</td><td>1.33</td><td>1.98d,2.00d,2.02d</td><td>0</td></tr><tr><td>CO*</td><td>fcc−η³(C)</td><td>42.9 (41.7)</td><td>1.18</td><td>2.10d,2.10d,2.10d</td><td>3</td></tr><tr><td></td><td>hcp−η³(C)</td><td>44.5 (43.2)</td><td>1.18</td><td>2.09d,2.09d,2.09d</td><td>0</td></tr><tr><td></td><td>bridge−η²(C)</td><td>43.2 (41.8)</td><td>1.17</td><td>2.01d,2.03d</td><td>1</td></tr><tr><td></td><td>top−η¹(C)</td><td>48.6 (46.5)</td><td>1.15</td><td>1.83d</td><td>0</td></tr><tr><td>H*</td><td>fcc</td><td>65.5 (61.5)</td><td></td><td>1.82e,1.83e,1.83e</td><td></td></tr><tr><td></td><td>hcp</td><td>64.1 (60.3)</td><td></td><td>1.82e,1.82e,1.82e</td><td></td></tr><tr><td></td><td>top</td><td>60.6 (56.2)</td><td></td><td>1.54e</td><td></td></tr><tr><td>H₂*</td><td>top</td><td>13.7 (7.7)</td><td></td><td>1.67e</td><td>87</td></tr></tbody><tfoot><tr><td colspan="6">a fcc, hcp, top and bridge are adsorption site, ηⁿ(X) denotes that X atom interacts with n surface metal atoms.</td></tr><tr><td colspan="6">b Values calculated using the equation of Eads=Eslab+Eadsorbate−Eadsorbate/slab. Parameters in parentheses are adsorption energies after zero-point energy corrections.</td></tr><tr><td colspan="6">c O–Rh bond length.</td></tr><tr><td colspan="6">d C–Rh bond length.</td></tr><tr><td colspan="6">e H–Rh bond length.</td></tr><tr><td colspan="6">f Values are angles between the surface normal and the O–C axis.</td></tr></tfoot></table>

decomposes into CO and H firstly, and CO₂ is formed via the oxidation of CO [6].

Previous experimental studies have shown that methanol decomposition into CO and H is important in the POM process on Rh(1 1 1), thus exploring the methanol decomposition mechanism is desired for accurately understanding and modeling the POM process. Although experiments have gained some information for methanol oxidation on Rh(1 1 1) [5–9], the reason why the oxidation takes place at CO rather than formaldehyde is still unclear. Furthermore, mechanism and kinetic parameters for methanol decomposition on Rh(1 1 1) have not been obtained in the experiments [5–9]. These facts motivate us to perform a theoretical investigation.

In this paper, we investigate the decomposition of methanol on Rh(1 1 1) by using the periodic self-consistent density functional theory (DFT). We determine the thermochemical and kinetic parameters for all the elementary steps involved. The calculated results are compared with those for the analogous reactions on other transition metal surfaces, e.g., Pd(1 1 1)[10], Pt(1 1 1)[11] and Ni(1 1 1)[12]. Furthermore, on the basis of the DFT-derived parameters, including binding energies, activation barriers, entropies and pre-exponential factors, we formulate a detailed microkinetic model, which extends the DFT-based results to the realistic conditions. Finally, we present the predictions of the model regarding the dominant reaction pathways, coverages, reaction rates, reaction orders and apparent activation energies for methanol decomposition on Rh(1 1 1) occurring under different conditions.

## 2. Computational details

DFT calculations were performed with program package DMol³ in Materials Studio of Accelrys Inc [13–15]. The exchange-correlation energy was calculated within the generalized gradient approximation (GGA) using the form of the functional proposed by Perdew and Wang [16,17], usually referred to as Perdew–Wang 91 (PW91). Density functional semicore pseudopotential (DSPP) [18] method was employed for the Rh atoms, and the carbon, oxygen and hydrogen atoms were treated with an all-electron basis set. The valence electron functions were expanded into a set of numerical atomic orbitals by a double-numerical basis with polarization functions (DNP). A Fermi smearing of 0.005 Hartree was used to improve the computational performance. All computations were performed with spin-polarization.

The Rh(1 1 1) surface was modeled using a $(2 \times 2)$ surface unit cell with a $10\ \mathring{\text{A}}$ vacuum region. The reciprocal space was sampled with a $(5 \times 5 \times 1)$ $k$-points grid generated automatically using the Monkhorst–Pack method [19]. A single adsorbate was allowed to adsorb on one side of the $(2 \times 2)$ unit cell, corresponding to a surface coverage of 25%. Full-geometry optimization was performed for all relevant adsorbates and the uppermost two layers without symmetry restriction, while the bottom layer Rh atoms were fixed at the bulk-truncated positions at the experimentally determined lattice constant of $3.80\ \mathring{\text{A}}$. Nonperiodical structures were fully optimized at the same theoretical level for the isolated atoms, radicals and molecules involved. A recent study has indicated that the three-layer thickness slab is adequate for the investigation of reactions on Rh(1 1 1) [20] and the present calculations also indicated that the energy changes were less than $1.2\ \text{kcal}\ \text{mol}^{-1}$ when a four-layer slab was employed.

Transition state (TS) searches were performed with the complete Linear Synchronous Transit/Quadratic Synchronous Transit (LST/QST) method implemented in DMol³ [21]. The convergence criterion for the TS searches was set to 0.01 Hartree/$\mathring{\text{A}}$ for the root mean square of atomic forces. Transition states were identified by the number of imaginary frequencies (NIMG) with NIMG=1. We applied the transition-state theory (TST) formalism [22] to predict rate constants for all the elementary steps involved.

![](./images/811660167081885696_1.jpg)

Fig. 1. Top view and side view (inserted) of the adsorption configurations of species involved in methanol dehydrogenation on Rh(111): (a) CH₃OH; (b) η³(O) adsorbed CH₃O; (c) η²(O) adsorbed CH₃O; (d) η¹(C)-η¹(O) adsorbed CH₂OH; (e) η¹(C)-η²(O) adsorbed CH₂O; (f) η¹(C)-η¹(O)-η¹(H) adsorbed CH₂O; (g) η²(C) adsorbed CHOH; (h) η¹(C) adsorbed CHOH; (i) η¹(C)-η¹(O) adsorbed CHO; (j) η³(C) adsorbed COH; (k) η¹(C) adsorbed CO; (l) atomic H.

## 3. Results

In this section, we first give adsorption geometries and energies for all species involved in the title reaction. Then we investigate the elementary steps from methanol to the final products, co-adsorbed CO and H, describing the TS geometries and energies.

For comparison, we often refer to three sets of data for methanol decomposition on Pd(111) [10], Pt(111) [11] and Ni(111) [12]. Values of adsorption energies, energy barriers and reaction energies are reported without zero-point energy (ZPE) corrections unless otherwise stated.

### 3.1. Adsorption of intermediates

In this section, we present a systematic investigation of geometries and energies for all the species involved. The most important adsorption configurations of the species are shown in Fig. 1, and information for all the possible adsorption configurations is given in Table 1.

#### 3.1.1. Methanol

Similar to the situation of Pd(111) [10], Pt(111) [11] and Ni(111)[12], methanol binds to Rh(111) at top site via the oxygen atom (see Fig. 1a). In this configuration, distance between O and the nearest surface Rh is 2.28 Å, with the O-H bond nearly parallel to the surface and the O-C axis tilted by 36° (see Table 1). This configuration has been confirmed by the high-resolution electron energy loss spectroscopy (HREELS) experiment [8]. The adsorption energy is calculated to be 14.8 kcal mol⁻¹, in good agreement with the previous theoretical value (15.3 kcal mol⁻¹)[23] but a little larger than the value determined in the thermal desorption experiment (11.5 kcal mol⁻¹) [7]. The difference between the theoretical and experimental values may arise from the different coverages considered, it has been pointed out that the adsorption energies of methanol depend on coverages [24,25]. For comparison, adsorption energies for methanol on Pd(111) [10], Pt(111) [11] and Ni(111) [12] are relatively low (9.1, 7.6 and 3.8 kcal mol⁻¹, respectively).

#### 3.1.2. Methoxy

Experiment [8] has shown that methoxy is upright adsorbed via the oxygen atom on Rh(111), but the adsorption sites were not determined. The present DFT calculation demonstrates that adsorption configurations of methoxy on Rh(111) are much abundant, i.e., staying vertically at fcc (see Fig. 1b) and hcp sites and tiltedly at bridge (see Fig. 1c) and top sites. The fcc state has the largest adsorption energy (57.2 kcal mol⁻¹), followed by the bridge and hcp states (56.0 and 54.4 kcal mol⁻¹), and the top state with the binding energy of 52.0 kcal mol⁻¹ is the least stable (see Table 1). The small difference in the adsorption energies suggests that adsorption PES for methoxy on Rh(111) is relatively flat, in contrast to the rather corrugated PESs for methoxy on both Pd(111) [10] and Ni(111) [12]. On the latter two surfaces [10,12], three-fold and bridge sites account for nearly a same stability for methoxy, whereas top adsorption is unstable. On Pt(111) [11], methoxy only adsorbs stably at top site gaining an energy of 35.5 kcal mol⁻¹, in which the O-C axis is inclined 59° from the surface normal.

#### 3.1.3. Hydroxymethyl

Previous theoretical studies have suggested that hydroxymethyl is indeed the preferred intermediate in methanol dehydrogenation on both Pd(111) [10] and Pt(111) [11]. In contrast to the top adsorption via the C atom of CH₂OH on Pd(111) [10], Pt(111) [11] and Ni(111) [12], we find that hydroxymethyl on Rh(111)

![](./images/811660167081885696_2.jpg)

Fig. 2. Top view and side view (inserted) of transition state structures involved in methanol dehydrogenation on Rh(111).

favors the $\eta^1(\mathrm{C})-\eta^1(\mathrm{O})$ configuration at bridge site (see Fig. 1d). The $\mathrm{O}-\mathrm{C}$ axis of $\mathrm{CH}_2 \mathrm{OH}$ is nearly flat located with the $\mathrm{C}-\mathrm{Rh}$ and $\mathrm{O}-\mathrm{Rh}$ bonds being 2.05 and $2.26 \AA$ long (see Table 1). The adsorption energy calculated to be $52.4 \mathrm{kcal} \mathrm{mol}^{-1}$ on $\mathrm{Rh}(111)$ is $8.6,6.7$ and $13.7 \mathrm{kcal} \mathrm{mol}^{-1}$ larger than those on $\operatorname{Pd}(111)$ [10], Pt(111) [11] and $\operatorname{Ni}(111)[12]$.

### 3.1.4. Formaldehyde
It is generally believed that formaldehyde adsorbs on the clean surfaces of group VIII metals via the $\eta^1(\mathrm{C})-\eta^1(\mathrm{O})$ mode [26], stabilizing the system by $12.5 \mathrm{kcal} \mathrm{mol}^{-1}$ on $\operatorname{Pd}(111)$ [10], $11.5 \mathrm{kcal} \mathrm{mol}^{-1}$ on $\operatorname{Pt}(111)$ [11] and $23.7 \mathrm{kcal} \mathrm{mol}^{-1}$ on $\operatorname{Ni}(111)$ [12]. However, the present calculation indicates adsorption configurations for formaldehyde on $\mathrm{Rh}(111)$ are much abundant, e.g., the $\eta^1(\mathrm{C})-\eta^2(\mathrm{O})$ and $\eta^1(\mathrm{C})-\eta^1(\mathrm{O})-\eta^1(\mathrm{H})$ configurations formed at both fcc and hcp sites (see Fig. 1e,f) and $\eta^2(\mathrm{C})-\eta^1(\mathrm{O})$ at fcc. As shown in Table 1, the $\eta^1(\mathrm{C})-\eta^2(\mathrm{O})$ configuration is the most stable with the binding energy ca. $24 \mathrm{kcal} \mathrm{mol}^{-1}$, followed by $\eta^1(\mathrm{C})-\eta^1(\mathrm{O})-\eta^1(\mathrm{H})$ (ca. $22 \mathrm{kcal} \mathrm{mol}^{-1}$ ) and then fcc- $\eta^2(\mathrm{C})-\eta^1(\mathrm{O})\left(20 \mathrm{kcal} \mathrm{mol}^{-1}\right)$. The small difference in adsorption energies (less than $4 \mathrm{kcal} \mathrm{mol}^{-1}$ ) favors conversions between various adsorption configurations. Moreover, the special configuration of $\eta^1(\mathrm{C})-\eta^1(\mathrm{O})-\eta^1(\mathrm{H})$ is expected to facilitate $\mathrm{CH}_2 \mathrm{O}$ dehydrogenation because the relevant $\mathrm{C}-\mathrm{H}$ bond is substantially weakened (mirrored by its length of $1.19 \AA$ ) as the result of the formation of the $\mathrm{H}-\mathrm{Rh}$ bond.

### 3.1.5. Hydroxymethylene
$\mathrm{CHOH}$ prefers the bridge and top sites through the carbon atom on $\mathrm{Rh}(111)$ with almost identical adsorption energies (ca. $80 \mathrm{kcal} \mathrm{mol}^{-1}$; see Table 1). In the bridge configuration (see Fig. $1 \mathrm{~g}$ ), the two $\mathrm{C}-\mathrm{Rh}$ bonds are $2.06 \AA$ long and the $\mathrm{O}-\mathrm{C}$ axis is $45^{\circ}$ tilted. In the top case (see Fig. $1 \mathrm{~h}$ ), the $\mathrm{C}-\mathrm{Rh}$ distance is $1.87 \AA$ and the $\mathrm{O}-\mathrm{C}$ axis is inclined by $53^{\circ}$. On $\operatorname{Pd}(111)$ [10], also the bridge and top adsorption configurations were located for hydroxymethylene, with the binding energies of 72.0 and $63.9 \mathrm{kcal} \mathrm{mol}^{-1}$, respectively, whereas on $\operatorname{Pt}(111)$ only the bridge adsorption with the binding energy of $74.7 \mathrm{kcal} \mathrm{mol}^{-1}$ was available [11].

### 3.1.6. Formyl
Formyl has been proposed as an intermediate in methanol dehydrogenation on $\mathrm{Rh}(111)$ by Houtman and Barteau [8]. However, no experimental structural information has been obtained for adsorbed CHO. Our calculation indicates CHO could stably bind at fcc, hcp and bridge sites. The top adsorption is indeed unstable, which would transform into the bridge site during optimization. The bridge adsorption favors the $\eta^1(\mathrm{C})-\eta^1(\mathrm{O})$ configuration (see Fig. $1 \mathrm{i}$ ), with the adsorption energy of $64.0 \mathrm{kcal} \mathrm{mol}^{-1}$. The threefold (fcc and hcp) adsorptions favoring the $\eta^2(\mathrm{C})-\eta^1(\mathrm{O})$ configuration are $4.2 \mathrm{kcal} \mathrm{mol}^{-1}$ less stable (see Table 1). On $\operatorname{Ni}(111)$ [12], top adsorption is favorable with the adsorption energy of $55.4 \mathrm{kcal} \mathrm{mol}^{-1}$; on $\operatorname{Pd}(111)$ [10], CHO could stably bind at all high symmetry sites, and the fcc adsorption affords the largest binding energy $\left(58.5 \mathrm{kcal} \mathrm{mol}^{-1}\right)$; on $\operatorname{Pt}(111)$ [11], all high symmetry sites afford almost identical adsorption energies, with the top adsorption being the largest one $\left(54.4 \mathrm{kcal} \mathrm{mol}^{-1}\right)$.

### 3.1.7. Hydroxymethylidyne
$\mathrm{COH}$ binds upright through the $\mathrm{C}$ end at three-fold hollow sites on $\mathrm{Rh}(111)$ (see Fig. $1 \mathrm{j}$ ). The adsorption energy is $106.7 \mathrm{kcal} \mathrm{mol}^{-1}$ at hcp and $103.2 \mathrm{kcal} \mathrm{mol}^{-1}$ at fcc. Similar adsorption configurations have also been determined for $\mathrm{COH}$ on both $\operatorname{Pd}(111)$ [10] and $\operatorname{Pt}(111)$ [11], with identical binding energies $\left(94.5 \mathrm{kcal} \mathrm{mol}^{-1}\right)$ on $\operatorname{Pd}(111)$ and the binding energy of $99.1 \mathrm{kcal} \mathrm{mol}^{-1}$ for the fcc adsorption on $\operatorname{Pt}(111)$. No information is available for $\mathrm{COH}$ on $\operatorname{Ni}(111)$.

<table>
<thead>
<tr><th colspan="7">Table 2<br>Comparison of energy barriers <i>E</i><sub>a</sub> and reaction energy Δ<i>H</i> (in kcal mol<sup>−1</sup>) for all elementary reactions involved in methanol dehydrogenation.</th></tr>
</thead>
<tbody>
<tr><td>Reaction</td><td colspan="2">Rh(1 1 1)<sup>a</sup></td><td colspan="2">Ni(1 1 1)<sup>b</sup></td><td colspan="2">Pd(1 1 1)<sup>c</sup></td><td colspan="2">Pt(1 1 1)<sup>d</sup></td></tr>
<tr><td></td><td><i>E</i><sub>a</sub></td><td>Δ<i>H</i></td><td><i>E</i><sub>a</sub></td><td>Δ<i>H</i></td><td><i>E</i><sub>a</sub></td><td>Δ<i>H</i></td><td><i>E</i><sub>a</sub></td><td>Δ<i>H</i></td></tr>
<tr><td>CH<sub>3</sub>OH* → CH<sub>3</sub>O* + H*</td><td>21.9(16.5)</td><td>1.3(−2.7)</td><td>9.3</td><td>−18.4</td><td>33.5</td><td>12.5</td><td>18.7</td><td>14.3</td></tr>
<tr><td>CH<sub>3</sub>O* → CH<sub>2</sub>O* + H*</td><td>12.6(9.3)</td><td>−1.0(−5.8)</td><td>22.6</td><td>4.3</td><td>17.3</td><td>−6.3</td><td>5.8</td><td>−7.4</td></tr>
<tr><td>CH<sub>2</sub>O* → CHO* + H*</td><td>0.7(0.0)</td><td>−12.6(−14.0)</td><td>11.0</td><td>−9.1</td><td>14.1</td><td>−16.9</td><td>0.0</td><td>−14.1</td></tr>
<tr><td>CHO* → CO* + H*</td><td>14.8(12.2)</td><td>−21.1(−23.5)</td><td>4.1</td><td>−37.3</td><td>13.5</td><td>−19.0</td><td>5.3</td><td>−22.4</td></tr>
<tr><td>CH<sub>3</sub>OH* → CH<sub>2</sub>OH* + H*</td><td>21.4(17.1)</td><td>−0.3(−3.8)</td><td>28.7</td><td>−5.3</td><td>28.2</td><td>2.6</td><td>15.5</td><td>−3.9</td></tr>
<tr><td>CH<sub>2</sub>OH* → CHOH* + H*</td><td>18.9(15.0)</td><td>0.4(−3.4)</td><td></td><td></td><td>26.5</td><td>0.0</td><td>14.5</td><td>0.23</td></tr>
<tr><td>CH<sub>2</sub>OH* → CH<sub>2</sub>O* + H*</td><td>25.2(20.7)</td><td>0.6(−4.7)</td><td></td><td></td><td>22.0</td><td>3.7</td><td>17.3</td><td>10.6</td></tr>
<tr><td>CHOH* → COH* + H*</td><td>13.7(9.1)</td><td>−12.6(−15.7)</td><td></td><td></td><td>17.4</td><td>−8.0</td><td>18.4</td><td>−11.1</td></tr>
<tr><td>CHOH* → CHO* + H*</td><td>11.7(6.9)</td><td>−10.5(−15.3)</td><td></td><td></td><td>15.4</td><td>−13.2</td><td>9.9<sup>e</sup></td><td>−23.3<sup>e</sup></td></tr>
<tr><td>COH* → CO* + H*</td><td>33.7(28.5)</td><td>−20.9(−23.1)</td><td></td><td></td><td>21.9</td><td>−24.3</td><td>22.4</td><td>−12.2</td></tr>
<tr><td>H* + H* → H<sub>2</sub>*</td><td>13.2(12.5)</td><td>9.4(10.6)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td colspan="9">a Values in parentheses are energies after zero-point energy corrections.</td></tr>
<tr><td colspan="9">b Values are taken from Ref. [12].</td></tr>
<tr><td colspan="9">c values are taken from Ref. [10].</td></tr>
<tr><td colspan="9">d values are taken from Ref. [11].</td></tr>
<tr><td colspan="9">e This step is a quasi-simultaneous O−H/C−H scission.</td></tr>
</tbody>
</table>

### 3.1.8. Carbon monoxide

On Rh(1 1 1), several experiments [27–29] have indicated that CO adsorbs at top site at low coverages, and at top and threefold sites at high coverages. Our calculations indicate that CO could stably bind at top, bridge and threefold sites on Rh(1 1 1). The top adsorption is indeed the most stable (see Table 1), in which CO is adsorbed via the carbon end (see Fig. 1k). The calculated distances of C−O and C−Rh are in excellent agreement with the experimental values (1.15 and 1.83 Å vs 1.15 ± 0.07 and 1.84 ± 0.07 Å) [30]. Similar adsorption configurations are also found for the other sites. For comparison, previous theoretical studies have shown that CO prefers threefold sites on Pd(1 1 1) [10], Pt(1 1 1) [11] and Ni(1 1 1) [12].

### 3.1.9. Atomic hydrogen and molecular hydrogen

Similar to the situation of the other transition metals considered, H is adsorbed at hollow sites on Rh(1 1 1) to maximize its chemical bonds. The fcc adsorption is the most stable (65.5 kcal mol<sup>−1</sup>; the hcp and top adsorptions are less stable by 1.4 and 4.9 kcal mol<sup>−1</sup>. The calculated fcc adsorption energy is in excellent agreement with the previous theoretical values (66.0 [4] and 65.5 kcal mol<sup>−1</sup> [31]). Also, the adsorption energies of H on Rh(1 1 1) are very close to those on Pd(1 1 1) (64.4 kcal mol<sup>−1</sup>) [10], Pt(1 1 1) (62.5 kcal mol<sup>−1</sup>) [11] and Ni(1 1 1) (67.9 kcal mol<sup>−1</sup>) [12]. Molecular hydrogen adsorbs at top site on Rh(1 1 1) with the H−H bond flat located. The calculated adsorption energy is 13.7 kcal mol<sup>−1</sup>, and the H−H bond is elongated to 0.88 Å from 0.73 Å in free molecule, suggesting H<sub>2</sub> is strongly activated.

## 3.2. Decomposition of adsorbed methanol

In this section, we investigate all the elementary steps involving both the initial C−H and O−H bond scission. The involved TS structures are shown in Fig. 2. The C−O path is not considered, because it was not found in experiments [24,32] and also a rather high energy barrier (33.4 kcal mol<sup>−1</sup>) for its initial step is revealed by us.

### 3.2.1. Initial O−H bond scission

Initial O−H bond scission is a classical path that has been proposed for methanol decomposition on Rh(1 1 1) [7,8,33,34]. The suggested path is methanol → methoxy → formaldehyde → formyl → carbon monoxide.

#### 3.2.1.1. CH₃OH → CH₃O + H.
The initial state (IS) is the top adsorbed methanol. We take the coadsorbed CH<sub>3</sub>O<sub>bridge</sub> + H<sub>fcc</sub> configuration as the final state (FS), because it could be transferred readily from the coadsorbed CH<sub>3</sub>O<sub>fcc</sub> + H<sub>fcc</sub> configuration, even though the isolated adsorption of CH<sub>3</sub>O at fcc site is slightly preferred. Following the approach of CH<sub>3</sub>OH toward the metal surface, the O−H bond is activated. In TS1 (see Fig. 2), the dissociated H binds at bridge site, while the CH<sub>3</sub>O moiety sits still at the off-top site. Following TS1, CH<sub>3</sub>O and H* diffuse to bridge and fcc sites, forming the thermoneutral FS (1.8 kcal mol<sup>−1</sup> endothermic).

The energy barrier of 21.9 kcal mol<sup>−1</sup> we find for this step is close to that for the same step on Pt(1 1 1) (18.7 kcal mol<sup>−1</sup>) [11], but is considerably higher than that for Ni(1 1 1) (9.3 kcal mol<sup>−1</sup>) [12] or remarkably lower than that for Pd(1 1 1) (33.5 kcal mol<sup>−1</sup>) [10]. Therefore, the activity ability of surfaces toward the O−H bond of methanol follows the order of Ni(1 1 1) > Pt(1 1 1) ≅ Rh(1 1 1) > Pd(1 1 1). For comparison, the analogous step on Pd(1 1 1) [10] and Pt(1 1 1) [11] is endothermic by 12.5 and 14.3 kcal mol<sup>−1</sup>, respectively, but on Ni(1 1 1) is exothermic by 18.4 kcal mol<sup>−1</sup> due to the rather strong adsorption of CH<sub>3</sub>O [12].

#### 3.2.1.2. CH₃O → CH₂O + H.
For methoxy dehydrogenation, both fcc and bridge adsorptions are considered as the IS's due to the similar stabilities of them. These two IS's are found to connect to a same FS, in which CH<sub>2</sub>O adsorbs in the fcc−η<sup>1</sup>(C)−η<sup>2</sup>(O) mode, and the atomic H sits at hcp site. These two paths indeed proceed via a similar reaction process, i.e., the incline of the O−C bond makes one of the C−H bonds close to surface so that it could be activated. TS2 is featured by the dissociated H at top site and CH<sub>2</sub>O at bridge site via the O atom with the O−C bond tiltedly directed (see Fig. 2). After the TS, the atomic H diffuses to hcp site, and CH<sub>2</sub>O is favored by further incline of the O−C axis for the formation of the C−Rh bond. Energy barriers for the two paths are basically equal in value (13.1 and 12.6 kcal mol<sup>−1</sup> for the fcc and bridge adsorbed CH<sub>3</sub>O). The low energy barriers demonstrate that methoxy could dehydrogenate readily into formaldehyde. Thermodynamically, this step is nearly thermoneutral (see Table 2).

#### 3.2.1.3. CH₂O → CHO + H.
For the formaldehyde dehydrogenation, both hcp−η<sup>1</sup>(C)−η<sup>2</sup>(O) and hcp−η<sup>1</sup>(C)−η<sup>1</sup>(O)−η<sup>1</sup>(H) states are considered as the IS's. However, the former process has a significantly higher energy barrier than the latter one (11.0 vs. 0.7 kcal mol<sup>−1</sup>), thus here we only elaborate the latter process. The reaction is excited by the stretching vibration of the C−H bond that has been obviously activated in the adsorption. In TS3 (see Fig. 2), the positions of nascent CHO and H change slightly with respect to those in the IS. After the TS, the atomic H diffuses to fcc site, and the C atom of CHO approaches to another Rh, forming the

$hcp-\eta^2(C)-\eta^1(O)$ configuration. Although this step is exothermic on all the surfaces considered[10-12](see Table 2), it is hindered by much different barriers on different surfaces, i.e., nearly no barriers on Rh(1 1 1) and Pt(1 1 1)[11] and considerable barriers on Ni(1 1 1) [12] and Pd(1 1 1)[10] (11.0 and $14.1\ \text{kcal}\ \text{mol}^{-1}$, respectively).

3.2.1.4. $CHO\rightarrow CO+H$. Bridge bound CHO is selected as the IS of this step. In the FS, CO and H bind at opposite threefold sites (hcp and fcc, respectively). In this step, a swag vibration of the adsorbed CHO makes the O atom depart from the surface and the C-H bond approach the metals. In TS4, CHO binds at off-top site, with the C-H bond, which is obviously elongated but still held, flat located (see Fig. 2). Following the TS, the C-H bond is broken, and CO and H diffuse to threefold sites. The calculated reaction energy is $-21.1\ \text{kcal}\ \text{mol}^{-1}$, and the relevant energy barrier is $14.8\ \text{kcal}\ \text{mol}^{-1}$.

### 3.2.2. Initial C-H bond scission
This pathway involves initial C-H bond scission followed by stepwise H abstraction to form adsorbed CO and H.

3.2.2.1. $CH_3OH\rightarrow CH_2OH+H$. Similar to the situation of the other metals considered, this step on Rh(1 1 1) starts with a rotation of the adsorbed methanol, such that the methyl group could move down and one of the C-H bonds could be activated. In TS1', the C-O axis of the $CH_2OH$ moiety is nearly flat located via C, and the dissociated H at off-top site shares the Rh atom with C (see Fig. 2). After TS1', $CH_2OH$ further approaches to the surface; while the atomic H moves to nearly fcc site because of strong repulsion of $CH_2OH$.

Energy barrier for this step is $21.4\ \text{kcal}\ \text{mol}^{-1}$, obviously lower than those on both Ni(1 1 1) ($28.7\ \text{kcal}\ \text{mol}^{-1}$) [12] and Pd(1 1 1) ($28.2\ \text{kcal}\ \text{mol}^{-1}$) [10] but $5.9\ \text{kcal}\ \text{mol}^{-1}$ higher than that on Pt(1 1 1) [11]. This step is slightly exothermic on Rh(1 1 1), similar to those on Ni(1 1 1)[12] and Pt(1 1 1)[11], but different from the situation of Pd(1 1 1)[10] (see Table 2).

3.2.2.2. $CH_2OH\rightarrow CHOH+H$. This step is initiated by the intrarotation of $CH_2OH$, thus a surface Rh atom could insert into one of the C-H bonds. In TS2'a (see Fig. 2), CHOH and H* share a Rh atom, with the C-H distance elongating to $1.38\ \text{Å}$. Following the TS, CHOH and H move respectively to bridge and fcc sites, forming the nearly thermoneutral FS. This step needs to overcome an energy barrier of $18.9\ \text{kcal}\ \text{mol}^{-1}$.

3.2.2.3. $CH_2OH\rightarrow CH_2O+H$. Alternatively, approach of the OH end of $CH_2OH$ to the surface results in the O-H activation. In TS2'b, the $CH_2O$ moiety still locates at bridge site, while the dissociated H sits at off-top site (see Fig. 2). After TS2'b, $CH_2O$ arranges to fcc site favoring the $\eta^1(C)-\eta^2(O)$ configuration and H moves to another fcc site, giving the thermoneutral FS. This step affords an energy barrier of $25.2\ \text{kcal}\ \text{mol}^{-1}$.

3.2.2.4. $CHOH\rightarrow COH+H$. This step is featured by the bridge adsorbed CHOH as the IS, and facilitated by the diffusion of CHOH to adjacent hcp site. In TS3'a (see Fig. 2), COH sits nearly at hcp site via the C end with the C-O axis approximately upright pointed, and the dissociated H sits atop one of the three Rh atoms bound to COH. Passing through TS3'a, COH rotates to the upright configuration at hcp site, and the atomic H moves to adjacent fcc site. Although this step is exothermic by $12.6\ \text{kcal}\ \text{mol}^{-1}$, the energy barrier is relatively high ($13.7\ \text{kcal}\ \text{mol}^{-1}$).

3.2.2.5. $CHOH\rightarrow CHO+H$. The IS of this process is selected as the top adsorbed CHOH. The FS is CHO (bridge-$\eta^1(C)-\eta^1(O)$)+H (fcc).

The reaction is excited with the help of the O-H stretching vibration. In TS3'b (see Fig. 2), the dissociated H locates over bridge site, and the CHO fragment still binds at top site via the C atom, changing slightly with respect to that in the IS. Passing the TS, CHO rotates to bridge site and H diffuses to fcc site. Energy barrier and reaction energy for this process are calculated to be 11.7 and $-10.5\ \text{kcal}\ \text{mol}^{-1}$, respectively.

3.2.2.6. $COH\rightarrow CO+H$. This step is strongly exothermic ($20.9\ \text{kcal}\ \text{mol}^{-1}$) but with a high activation energy of $33.7\ \text{kcal}\ \text{mol}^{-1}$. The incline of the C-O bond in COH brings the hydrogen atom close to the surface, favoring the O-H bond activation. In TS4', CO sits still at threefold site but with the C-O bond tilted; the abstracted H sits at off-top site sharing the Rh atom with CO (see Fig. 2). After TS4', CO diffuses to the top site favoring the upright configuration, and the atomic H moves to adjacent fcc site.

3.2.2.7. $H+H\rightarrow H_2$. At the IS, the two hydrogen atoms are adsorbed at adjacent fcc sites. The diffusions of both H atoms make the system reach the TS, in which the two H atoms barely bind at top site with H-H distance of $1.30\ \text{Å}$. Passing through the TS, the two H atoms approach each other forming FS. This step is hindered by $13.2\ \text{kcal}\ \text{mol}^{-1}$, and is endothermic by $9.4\ \text{kcal}\ \text{mol}^{-1}$.

## 4. Discussion

### 4.1.1. Comparison of adsorptions on different metal surfaces

For the late group VIII metal surfaces, e.g., Pt(1 1 1), Pd(1 1 1) and Ni(1 1 1), we have summarized the preferred adsorption configurations of intermediates involved in methanol dehydrogenation, in which the intermediates tend to form saturated-type structures by bonding with the surface metal atom(s)[10] and have obvious preference between different adsorptions[10-12]. Compared with these metals, Rh(1 1 1) accounts for relatively abundant adsorption configurations as well as relatively flat adsorption potential energy surface (PES) for some intermediates, e.g., $CH_3O$, $CH_2O$ and CHOH. This typical adsorption property has also been observed for the adsorptions of $CH_2$ and $CH_3$ on Rh(1 1 1) [4], in which they prefer the threefold sites, with the energy difference often lower than $2.4\ \text{kcal}\ \text{mol}^{-1}$, compared to the facts that there are only bridge adsorption for $CH_2$ and top adsorption for $CH_3$ on the other group VIII transition metals [35,36]. Moreover, adsorption is always stronger for species on Rh(1 1 1) than on Pd(1 1 1)[10] and Pt(1 1 1)[11], but no obvious tendency of adsorption strengths is found between Rh(1 1 1) and Ni(1 1 1)[12] (see Table S1 in the Supporting Information).

This typical adsorption properties of Rh(1 1 1) can be rationalized by the partial density of state (PDOS) of the metal surface. Nørskov and co-workers have shown that the adsorption energy of adsorbate on metal surface is related to the location of the surface d-band center relative to the Fermi level. As the d-band center is closer to the Fermi level, the bond between the adsorbate and the metal surface would become stronger since the antibonding states exist above the Fermi level and these states are empty. On the other hand, when the d-band center is shifted down (further from the Fermi level) and the antibonding states would become filled, and thereby the bond between the metal surface and the adsorbate is weaker [37]. The values compiled by Andersen et al. [38] showed that the d-band centers of the four metal surfaces are $-1.73\ \text{eV}$ for Rh(1 1 1), $-1.83\ \text{eV}$ for Pd(1 1 1), $-2.52\ \text{eV}$ for Pt(1 1 1) and $-1.29\ \text{eV}$ for Ni(1 1 1). Therefore, it is reasonable that Rh(1 1 1) accounts for stronger adsorption than Pt(1 1 1) and Pd(1 1 1) for the species considered. According to the d-band center values, adsorbate on Ni(1 1 1) should have the strongest adsorption

![](./images/811660167081885696_3.jpg)

Fig. 3. The d-orbital density of states of Rh(1 1 1), Ni(1 1 1), Pd(1 1 1) and Pt(1 1 1).

among all the metal surfaces considered, but the calculated results show it depends on adsorbates (see Table S1 in the Supporting Information). Furthermore, as shown in Fig. 3, the PDOS of Rh(1 1 1) is strikingly more broad than the PDOS's of all the other metals considered. The high energy end of the PDOS is relatively simi- lar for all the metal surfaces, terminated at about 2.17 eV; while the low energy end is obviously different, which still has signifi- cant electronic states between -5.42 and -6.50 eV for Rh(1 1 1), but does not for the other surfaces. The broadening of the PDOS toward the low energy range indicates that, in addition to the interaction between the higher energy orbitals, adsorption of adsorbates on Rh(1 1 1) may also involve the lower energy orbitals, giving rela- tively abundant configurations with larger binding energies. For instance, free formaldehyde has the electronic state of $\sigma(C-H)$ at -5.42 to -6.50 eV (see Fig. S1 in Supporting Information), this state could interact with d states of Rh(1 1 1) giving the special $\eta^{1}(C)-\eta^{1}(O)-\eta^{1}(H)$ configuration that is not found on the other surfaces. As mentioned above, it is this special adsorption configu- ration that strongly favors the C-H bond scission of formaldehyde on Rh(1 1 1).

### 4.2. Dehydrogenation PES

Detailed PES for methanol dehydrogenation on Rh(1 1 1) is pre- sented in Fig. 4. The energy reference used in the figure corresponds to the energy of gaseous molecule of $CH_{3}OH$, and the values are corrected by ZPE. The weak interaction of methanol with Rh(1 1 1) suggests that desorption rather than dehydrogenation would be preferable for adsorbed methanol. For the dehydrogenation, there are four different pathways depending on intermediates for O-H bond scission (see Scheme 1). It is found from the PES that initial C-H and O-H bond scission on Rh(1 1 1) are both favorable.

For the initial O-H bond scission channel, the first step is the rate-determining step with the highest energy barrier of $16.5 kcal mol^{-1}$. It can be found that methoxy prefers to dehydrogenate rather than hydrogenate, agreeing well with the experimental finding that no methanol desorption associating with methoxy hydrogenation was observed [8]. It should be mentioned that part of methoxy desorbing as methanol found by Solymosi et al. [7] may arise from the fact that the high coverage of methanol $(5.8 × 10^{14}$ molecules $cm^{-2})$ prevents methoxy dehydrogenation but promotes methoxy hydrogenation. For formaldehyde, decom- position to CHO takes place spontaneously because the C-H bond has been obviously activated in the IS, explaining the fact that no formaldehyde was detected in the experiments [7,8]. The rapid decomposition of $CH_{2}O$ would prevent it from being oxidized in the POM process, consistent with the experimental findings that on the $Rh(111)-(2 × 2)O$ surface methanol dehydrogenates to CO first, and then CO is oxidized to $CO_{2}$ [8]. As a result, we believe that the reason why oxidation does not take place at formalde- hyde is mainly originated from the rapid decomposition of $CH_{2}O$, which results from the special adsorption configuration of $CH_{2}O$ $(\eta^{1}(C)-\eta^{1}(O)-\eta^{1}(H))$. Finally, CHO overcomes a moderate energy barrier to CO.

Along the initial C-H bond scission path, $CH_{2}OH$ prefers C-H bond cleavage to produce CHOH rather than O-H bond scis- sion to $CH_{2}O$, mirrored by the corresponding energy barriers $(15.0 kcal mol^{-1}$ vs. $20.7 kcal mol^{-1})$. Once CHOH is formed, it may also dehydrogenate via C-H and/or O-H bond scission; and it can be seen from Fig. 4 that the O-H bond cleavage (forming CHO) is slightly favorable. However, CHO dehydrogenates to CO with a moderate energy barrier as mentioned above, whereas interme- diate COH from the H-COH bond scission needs to overcome a relatively high energy barrier to form CO. Therefore, path 3 (see Scheme 1) should be the main reaction path along the initial C-H path, in which also the initial step is the rate-determining step. Con-

![](./images/811660167081885696_4.jpg)

Scheme 1. Reaction pathways of methanol dehydrogenation.

![](./images/811660167081885696_5.jpg)

Fig. 4. Potential energy surface of methanol dehydrogenation on Rh(1 1 1). Energies (in kcal mol⁻¹) are relative to gas-phase methanol with zero-point energy corrections.
1, CH₃OH*; 2, CH₃O*+H*; 2', CH₂OH*+H*; 3, CH₂O*+2H*; 3', CHOH*+2H*; 4, CHO*+3H*; 4', COH*+3H*; 5, CO*+4H*; 6, CO*+H₂*+2H*; 7, CO*+2H₂*. A*+nH* represents respective adsorptions of A and nH atoms on (n+1) separated slabs.

sidering that initial C−H and O−H bond scission are both favorable, methanol dehydrogenation on Rh(1 1 1) involves two competitive reaction paths, i.e., paths **1** and **3** (see Scheme 1).

The initial step of methanol decomposition on Rh(1 1 1) is quite different from those on the other metal surfaces considered, i.e., O−H activation for Ni(1 1 1) [12] and C−H activation for Pd(1 1 1) [10] and Pt(1 1 1) [11]. The difference can be rationalized by the relative stabilities of CH₃O and CH₂OH on the surfaces with respect to free methanol (see Fig. 5). It can be found that CH₂OH is much more stable than CH₃O on both Pd(1 1 1) [10] and Pt(1 1 1) [11], accounting for the preference of initial C−H bond scission. On Ni(1 1 1) [12], however, CH₃O is strikingly more stable than CH₂OH, explaining the fact that initial O−H bond scission is preferred. Rh(1 1 1) affords nearly the same stabilities for these two species, thus favors both the initial C−H and O−H paths.

For the initial O−H path, it is found that the PES on Rh(1 1 1) is very similar to that on Pt(1 1 1) [11], in which formaldehyde decompose spontaneously, in contrast to the non-neglctable energy barrier for the same step on Ni(1 1 1) [12] and Pd(1 1 1) [10]. For the initial C−H path, C−H bond scission in CH₂OH and O−H bond scission in CHOH are favored on both Pt(1 1 1) [11] and Rh(1 1 1), while O−H bond scission on Pd(1 1 1) is favored for both CH₂OH and CHOH [10].

![](./images/811660167081885696_6.jpg)

Fig. 5. Stabilities of methoxy and hydroxymethyl on different metal surfaces with respect to gas-phase methanol.

### 4.3. Microkinetic modeling

In this subsection, we first present the microkinetic model of methanol decomposition on Rh(1 1 1). Then, the microkinetic modeling of the title reaction is carried out at two sets of typical reaction conditions: low temperatures relevant to the UHV conditions; and high temperatures and high pressures, corresponding to the practical POM conditions.

#### 4.3.1. Microkinetic model

The microkinetic model includes all the 14 elementary steps shown in **Table 3**. The adsorption and desorption steps are assumed to be in equilibrium. For the other steps, we apply the pseudo-steady-state approximation, that is, the production and consumption rates of the relevant reactant species are assumed to be identical. The reverse reactions of the elementary steps are not included in the model, because all of the elementary reactions are exothermic except the combination of H atoms to molecular hydrogen (step 12). In step 12, the product of H₂ would desorb rather readily from the surface compared to dissociation, so the possibility of the H₂ dissociation can also be neglected. It should be pointed out that, as the system pressure increases, this assumption of irreversible reaction steps will become less reliable. The detailed description of the microkinetic model is given in the Supporting Information. Similar kinetic modeling approaches have been successfully applied to various reaction systems on metal surfaces [39,40].

<table>
<caption>Table 3<br>Elementary steps included in the microkinetic model for methanol dehydrogenation on Rh(1 1 1).</caption>
<thead>
<tr>
<th>Steps</th>
<th>Surface reactions</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>CH₃OH(g)+* ↔ CH₃OH*</td>
</tr>
<tr>
<td>2</td>
<td>CH₃OH*+* → CH₃O*+H*</td>
</tr>
<tr>
<td>3</td>
<td>CH₃O*+* → CH₂O*+H*</td>
</tr>
<tr>
<td>4</td>
<td>CH₂O*+* → CHO*+H*</td>
</tr>
<tr>
<td>5</td>
<td>CHO*+* → CO*+H*</td>
</tr>
<tr>
<td>6</td>
<td>CH₃OH*+* → CH₂OH*+H*</td>
</tr>
<tr>
<td>7</td>
<td>CH₂OH*+* → CHOH*+H*</td>
</tr>
<tr>
<td>8</td>
<td>CH₂OH*+* → CH₂O*+H*</td>
</tr>
<tr>
<td>9</td>
<td>CHOH*+* → COH*+H*</td>
</tr>
<tr>
<td>10</td>
<td>CHOH*+* → CHO*+H*</td>
</tr>
<tr>
<td>11</td>
<td>COH*+* → CO*+H*</td>
</tr>
<tr>
<td>12</td>
<td>H*+H* → H₂*</td>
</tr>
<tr>
<td>13</td>
<td>CO* ↔ CO(g)+*</td>
</tr>
<tr>
<td>14</td>
<td>H₂* ↔ H₂(g)+*</td>
</tr>
</tbody>
</table>

![](./images/811660167081885696_7.jpg)

Fig. 6. Surface coverages of CO, COH and vacant sites as a function of temperature involved in the methanol dehydrogenation on Rh(1 1 1) under UHV conditions predicted by microkinetic modeling. Coverages for the other species are less than 10⁻¹⁰ ML and thus not shown.

Rigorously, to construct a self-consistent microkinetic model, the binding energies used are determined from DFT calculations carried out at the surface coverages estimated by the microkinetic modeling. One important relation that should be incorporated in the model is the coverage dependence of the CO binding energy because previous studies have indicated CO adsorption energy on transition metal surfaces is predominantly affected by coverages [41,42]. We find a linear dependence of the DFT-derived binding energies of CO on Rh(1 1 1) at various coverages ($\theta_{\text{CO}}$), the relation is $E_{\text{ads}}^{\text{CO}}=-25.5\theta_{\text{CO}}+52.0$ kcal mol⁻¹ (after ZPE correction). This relation implies that the adsorption energy of CO reduces linearly with its coverage. In addition to CO, we do not incorporate into the model the coverage effects of the other intermediates based on the facts that (i) binding energies for the other species (except methanol and H₂) are not the parameters of the microkinetic model, (ii) CO coverage has small effects on the binding energies of CH₃OH and H₂ as indicated previously [35] and (iii) the coverages of CH₃OH and H₂ are estimated to be very low under all the considered conditions by the microkinetic modeling.

### 4.3.2. Under the typical UHV conditions (100 K<T<300 K, $p=10^{-6}$ Torr)
In the UHV experiments [8,24,32], it was found that about 50% of methanol undergoes dehydrogenation to form adsorbed hydrogen and carbon monoxide during methanol desorption between 110 and 205 K. No any other intermediates and products were observed. In the following, the microkinetic modeling of methanol decomposition was carried out with the typical UHV conditions, i.e., the pressure at 10⁻⁶ Torr and the temperatures in the range of 100–300 K.

#### 4.3.2.1. Coverages.
Fig. 6 gives coverages for intermediates (including vacant sites) with non-negligible values (>10⁻³ ML) estimated based on the microkinetic model. It can be found that under the UHV conditions intermediates with non-negligible coverages are only CO and COH. The coverages of CO are very high under all UHV conditions (above 0.63 ML). As temperature rises, the coverage of CO increases at first (ca. 100–160 K), reaches the maximum value of almost 1.0 ML at 160 K and finally decreases after the maximum point. This is because temperatures for CO desorption are higher than those for its formation [24]. At the initial stage, CO is produced by methanol dehydrogenation and stays on the surface, and it begins to desorb only when temperatures are higher than a certain value. COH is presented with visible coverage only at the lower temperatures (100–150 K), which shows a remarkable descending trend. The number of vacant sites can be negligible at lower temperatures (<190 K) and at higher temperatures (>190 K) it increases with the rise of temperature (see Fig. 6).

![](./images/811660167081885696_8.jpg)

Fig. 7. Reaction rate ($r_{\text{ovl}}$) and apparent activation energies ($H^{*}$) for methanol dehydrogenation on Rh(1 1 1) under UHV conditions.

It should be pointed out that methoxy is observed in experiments [7,8], while the microkinetic modeling show the coverage of methoxy is negligibly low. To confirm the disagreement does not originate from the microkinetic model we used, we estimate the coverage of methoxy when the reverse reactions are included. The result demonstrates the coverage of methoxy is still rather low (see Section 3 in the Supporting Information). In fact, this discrepancy can be rationalized by three factors: (i) coadsorption with methanol at high coverages, which enhances the formation of methoxy [25] and inhibits the dehydrogenation of methoxy, indirectly enhancing the stability of methoxy; (ii) surface residual oxygen atoms, which could favor the formation of methoxy and enhance the stabilization of the intermediate [8]; and (iii) the impinging of CH₃OH with surface, which results in the formation of methoxy [7]. These effects facilitate the formation of methoxy.

#### 4.3.2.2. Reaction mechanism.
A comparison of the rates of various elementary steps included in the model (see Table S2 in the Supporting Information) reveals (i) rates for initial O–H and C–H activation are in the same order, (ii) the rate of C–H bond scission for CH₂OH is several orders larger than that of its O–H path, (iii) CHOH has a rate for O–H bond scission that is much larger than that of C–H bond cleavage and (iv) the total rate of paths **1** and **3** is almost the same as the net rate for the overall dehydrogenation. These results clearly suggest that methanol decomposition on Rh(1 1 1) under the UHV conditions involves predominantly paths **1** and **3**.

#### 4.3.2.3. Reaction rates and apparent activation energies.
Fig. 7a gives the total reaction rate as a function of temperature under the UHV

![](./images/811660167081885696_9.jpg)

Fig. 8. Effect of temperature and methanol partial pressure on the coverages of CO ($\theta_{\text{CO}}$), COH ($\theta_{\text{COH}}$) as well as vacant site ($\theta^*$). Coverages for the other species are less than $10^{-4}$ ML. 1, 375.03 Torr; 2, 112.51 Torr; 3, 37.50 Torr; 4, 3.75 Torr; 5, 0.38 Torr; 6, 0.025 Torr.

conditions. We can find the rate is rather low when the temperature is lower than 200 K and increases rapidly when the temperature is above 200 K. This is partly because the rate constants of the relevant elementary steps are heightened at the higher temperatures and partly because the vacant sites favoring decompositions are obviously increased at temperatures above 200 K (see Fig. 6). The apparent activation energy ($H^*$) is calculated according to $H^* = RT^2(\text{d} \ln r_{\text{ovl}}/\text{d}T)_{p,y_i}$, where $y_i$ stands for the mole fraction of species $i$ in the reaction mixture, $R$ is the gas constant, $T$ is the temperature, $p$ is the pressure and $r_{\text{ovl}}$ is the total reaction rate. As shown in Fig. 7b, it can be found that $H^*$ is remarkably decreased as temperature rises, especially at the higher temperatures.

### 4.3.3. At high temperatures and high pressures
(500 K < T < 1000 K, 0.025 Torr < p < 375.03 Torr)

At the high pressures and high temperatures, products for methanol decomposition are still CO and $\text{H}_2$ [5,6,9]. Experiment also showed that the measurable conversion of methanol begins at a significantly lower temperature (550 K), and conversion reaches a flux limited value at about 900 K [6]. In this section, we model the reaction at the temperatures of 500–1000 K and the pressures of 0.025–375.03 Torr.

#### 4.3.3.1. Coverages.
We find that CO and COH are still the most abundant surface intermediates at all the modeling conditions, and coverages for the other species are less than $10^{-4}$. Fig. 8 shows the surface coverages of the most abundant surface intermediates at different methanol partial pressures as a function of temperature.

For CO at a given partial pressure, the coverage curve is analogous to that for methanol decomposition under UHV condition as shown in Fig. 6, i.e., there is a maximum point in the curve and the coverage decreases at the lower and higher temperatures, especially for the higher temperatures. We can also find that the maximum point of curve would be shifted to the higher temperature region when the pressure is increased and thus the curves for different methanol partial pressures crosses in the lower temperature range. At higher temperatures (>650 K), clear relation between the CO coverage and the partial pressure is observed, i.e., the higher the methanol partial pressure the larger the CO coverage. On the other hand, it can be found from Fig. 8 that the surface coverage of COH decreases exponentially with temperature but increases obviously with methanol partial pressure. The number of vacant sites increases nearly linearly with temperature; while at a given temperature, it decreases with the increase of methanol partial pressure (see Fig. 8).

![](./images/811660167081885696_10.jpg)

Fig. 9. Reaction rate ($r_{\text{ovl}}$) for methanol dehydrogenation on Rh(1 1 1) at high temperatures and high pressures. The inserted figure is used to show clearly the reaction rate at lower partial pressures. The notation of the numbers is the same as in Fig. 8.

#### 4.3.3.2. Reaction mechanism.
At high temperatures and high pressures, a comparison of the relative rates of various elementary steps included in the model (see Table S3 in the Supporting Information) reveals that paths **1** and **3** are still the main reaction channels; however, the other paths (paths **2** and **4**) are also significant, reflected by the fact that rates for the O–H path in $\text{CH}_2\text{OH}$ and the C–H path in CHOH are only one order lower than the respective alternative paths.

#### 4.3.3.3. Reaction rates.
Fig. 9 shows the overall reaction rate as a function of temperature at different methanol partial pressures. The overall reaction rate is negligibly low below 550 K, and increases quickly when the temperature is above 550 K (see Fig. 9). This is in good agreement with the experimental finding that the measurable conversion of methanol begins at 550 K [6]. There is an optimum temperature with a maximum rate for the methanol conversion at a given methanol partial pressure, and the optimum temperature shifts to the high temperature range as the methanol partial pressure is increased. This is because the higher temperatures favor increases in both the elementary rate constants and vacant sites but depresses the methanol adsorption. As shown in Fig. 9, the maximum rate locates always in the range of 850–950 K when the methanol partial pressure is higher than 50 Torr. This is in consistent with the experimental result that the conversion reaches a flux limited value at about 900 K [6].

#### 4.3.3.4. Apparent activation energies and reaction orders.
To determine the kinetic expression for an overall reaction, two

![](./images/811660167081885696_11.jpg)

Fig. 10. Temperature dependent apparent activation energy at 375.03 Torr $(H^{*})$ (a) and partial pressure dependent methanol reaction order at 900 K (b) for methanol dehydrogenation on Rh(111).

parameters, apparent activation energy $H^{*}$ and reaction order $\alpha$, should be provided. In theory, $\alpha$ is calculated according to $\alpha_{i}=(\mathrm{d} \ln r_{o v l} / \mathrm{d} \ln y_{i})_{T, p}$. Fig. 10a gives $H^{*}$for methanol decomposition on Rh(111) as a function of temperature at 375.03 Torr and $\alpha$ of methanol as a function of pressure at 900 K, corresponding to the condition for the highest overall reaction rate. Similar to the situation of the UHV conditions, the $H^{*}$ at the high temperature and high pressure condition decreases with temperature. It can be seen from Fig. 10b that the $\alpha$ of methanol is positive for methanol decomposition and decreases with the increase of methanol partial pressure. At higher pressures (above 100 Torr) the $\alpha$ of methanol is distributed in the range of 0.70-0.73. The variations in $\alpha$ and $H^{*}$ may then be used to generate explicitly expression of the overall reaction rate in different regimes, without actually performing experiments under these conditions. Such an analysis is of use for utilizing results from the low pressure kinetic studies to model reaction behavior at high pressures, that is, bridging the pressure gap.

## 5. Conclusion

In the present study, methanol dehydrogenation into carbon monoxide on Rh(111) has been explored using DFT slab calculation and microkinetic modeling. We can now conclude by summarizing a number of the main points below.

Compared with the other transition metal surfaces (Ni(111), Pd(111) and Pt(111)), Rh(111) accounts for larger adsorption energies for most species, abundant adsorption configurations and rather flat adsorption PES for some species. It is found that the initial C-H and O-H activations are comparable on Rh(111), and paths $\mathrm{CH}_{3} \mathrm{OH} \rightarrow \mathrm{CH}_{3} \mathrm{O} \rightarrow \mathrm{CH}_{2} \mathrm{O} \rightarrow \mathrm{CHO} \rightarrow \mathrm{CO}$ and $\mathrm{CH}_{3} \mathrm{OH} \rightarrow \mathrm{CH}_{2} \mathrm{OH} \rightarrow \mathrm{CHOH} \rightarrow \mathrm{CHO} \rightarrow \mathrm{CO}$ are the most possible pathways. This is quite different from the situation of Pd(111), Pt(111) and Ni(111). The reason why oxidation does not take place at $\mathrm{CH}_{2} \mathrm{O}$ is that there is a very activated adsorption state $(\eta^{1}(\mathrm{C})-\eta^{1}(\mathrm{O})-\eta^{1}(\mathrm{H}))$ of formaldehyde on Rh(111), which dehydrogenates spontaneously.

Microkinetic modeling demonstrates that CO and COH are the most abundant surface species, and coverages for other intermediates are rather low. Under UHV conditions, it is really the two most possible paths that determines the dehydrogenation of methanol on Rh(111), and other paths are negligible; the reaction rate is rather low at low temperature and increases rapidly at temperatures above 200 K. At high temperatures and high pressures, the two most possible paths are still dominant, whereas the other two paths of $\mathrm{CH}_{3} \mathrm{OH} \rightarrow \mathrm{CH}_{2} \mathrm{OH} \rightarrow \mathrm{CH}_{2} \mathrm{O} \rightarrow \mathrm{CHO} \rightarrow \mathrm{CO}$ and $\mathrm{CH}_{3} \mathrm{OH} \rightarrow \mathrm{CH}_{2} \mathrm{OH} \rightarrow \mathrm{CHOH} \rightarrow \mathrm{COH} \rightarrow \mathrm{CO}$ also become significant. In addition, it is found that apparent activation energy decreases with temperature at all reaction conditions; and reaction order of methanol decreases with the increment of methanol partial pressure.

## Acknowledgements

This work was supported by IRT0759 of MOE, PRC, State Key Basic Research Program of China (2006CB202505), National Natural Science Foundation of China (Nos. 20476061 and 10979077), CNPC Science & Technology Innovation Foundation (2009D-5006-04-07), and the Fundamental Research Funds for the Central Universities (09CX05002A).

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.molcata.2011.05.007

## References

[1] M. Granovskii, I. Dincer, M.A. Rosen, Int. J. Hydrogen Energy 31 (2006) 337.
[2] J.J. Spivey, Ind. Eng. Chem. Res. 26 (1987) 2165.
[3] W.H. Cheng, Appl. Catal. A 130 (1995) 13.
[4] B.S. Bunnik, G.J. Kramer, J. Catal. 242 (2006) 309.
[5] H.Y.H. Chan, C.T. Williams, M.J. Weaver, C.G. Takoudis, J. Catal. 174 (1998) 191.
[6] M.P. Mallen, L.D. Schmidt, J. Catal. 161 (1996) 230.
[7] F. Solymosi, A. Berkó, T.I. Tarnóczi, Surf. Sci. 141 (1984) 533.
[8] C. Houtman, M.A. Barteau, Langmuir 6 (1990) 1558.
[9] C.T. Williams, C.G. Takoudis, M.J. Weaver, J. Phys. Chem. B 102 (1998) 406.
[10] R. Jiang, W. Guo, M. Li, D. Fu, H. Shan, J. Phys. Chem. C 113 (2009) 4188.
[11] J. Greeley, M. Mavrikakis, J. Am. Chem. Soc. 126 (2004) 3910.
[12] G.C. Wang, Y.H. Zhou, Y. Morikawa, J. Nakamura, Z.S. Cai, X.Z. Zhao, J. Phys. Chem. B 109 (2005) 12431.
[13] B. Delley, J. Chem. Phys. 92 (1990) 508.
[14] B. Delley, J. Chem. Phys. 100 (1996) 6107.
[15] B. Delley, J. Chem. Phys. 113 (2000) 7756.
[16] J.P. Perdew, Y. Wand, Phys. Rev. B 33 (1986) 8800.
[17] J.P. Perdew, Y. Wang, Phys. Rev. B 45 (1992) 13244.
[18] B. Delley, Phys. Rev. B 66 (2002) 155125.
[19] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[20] N. Kapur, J. Hyun, B. Shan, J.B. Nicholas, K. Cho, J. Phys. Chem. C 114 (2010) 10171.
[21] T.A. Halgren, W.N. Lipscomb, Chem. Phys. Lett. 49 (1977) 225.
[22] K.J. Laidler, Chemical Kinetics, 3rd ed., Harper and Row, New York, 1987.
[23] J. Kua, W.A.G. III, J. Am. Chem. Soc. 121 (1999) 10928.
[24] R. Schennach, G. Krenn, K.D. Rendulic, Vacuum 71 (2003) 89.
[25] H.P. Koch, G. Krenn, I. Bako, R. Schennach, J. Chem. Phys. 122 (2005) 244720.
[26] M. Mavrikakis, M.A. Barteau, J. Mol. Catal. A: Chem. 131 (1998) 135.
[27] A. Beutler, E. Lundgren, R. Nyholm, J.N. Andersen, B.J. Setlik, D. Heskett, Surf. Sci. 396 (1998) 117.
[28] R. Linke, D. Curulla, M.J.P. Hopstaken, J.W. Niemantsverdriet, J. Chem. Phys. 115 (2001) 8209.
[29] G. Krenn, I. Bako, R. Schennach, J. Chem. Phys. 124 (2006) 144703.
[30] M. Gierer, A. Barbieri, M.A.V. Hove, G.A. Somorjai, Surf. Sci. 391 (1997) 176.
[31] C. Popa, W.K. Offermans, R.A.V. Santen, A.P.J. Jansen, Phys. Rev. B 74 (2006) 155428.

[32] G. Krenn, R. Schennach, J. Chem. Phys. 120 (2004) 5729.

[33] F. Solymosi, A. Berkó, T.I. Tarnóczi, J. Chem. Phys. 87 (1987) 6745.

[34] G.K. Chuah, N. Kruse, W.A. Schmidt, J.H. Block, G. Abend, J. Catal. 119 (1989) 342.

[35] A. Michaelides, P. Hu, J. Am. Chem. Soc. 122 (2000) 9866.

[36] J.F. Paul, P. Sautet, J. Phys. Chem. B 109 (1998) 1578.

[37] B. Hammer, J.K. Nørskov, Adv. Catal. 45 (2000) 71.

[38] O.K. Andersen, O. Jepsen, D. Glötzel, Highlights of Condensed Matter Theory, vol. LXXXIX, Corso Soc. Italiana di Fisica, Bologna, 1985, p. 59.

[39] P. Liu, J.A. Rodrigues, J. Phys. Chem. B 110 (2006) 19418.

[40] Y.M. Choi, P. Liu, J. Am. Chem. Soc. 131 (2009) 13054.

[41] S. Kandoi, J. Greeley, M.A. Sanchez-Castillo, S.T. Evans, A.A. Gokhale, J.A. Dumesic, M. Mavrikakis, Top. Catal. 37 (2006) 17.

[42] A.A. Gokhale, J.A. Dumesic, M. Mavrikakis, J. Am. Chem. Soc. 130 (2008) 1402.