Applied Catalysis B: Environmental 163 (2015) 361-369

![](./images/814702421933555712_1.jpg)

Contents lists available at ScienceDirect

Applied Catalysis B: Environmental

journal homepage: www.elsevier.com/locate/apcatb

![](./images/814702421933555712_2.jpg)

Combined experimental and computational study of CO oxidation promoted by Nb in manganese oxide octahedral molecular sieves

![](./images/814702421933555712_3.jpg)

Homer C. Genuino $^{a}$, Mohammad S. Seraji $^{a}$, Yongtao Meng $^{a}$, Diego Valencia $^{b}$, Steven L. Suib $^{a,c,*}$

$^{a}$ Department of Chemistry, University of Connecticut, 55 North Eagleville Road, Storrs, CT 06269-3060, USA
$^{b}$ Inorganic Chemistry and Catalysis Group, Debye Institute for Nanomaterials Science, Utrecht University, Universiteitweg 99, 3584 CG Utrecht, The Netherlands
$^{c}$ Institute of Materials Science, University of Connecticut, 97 North Eagleville Road, Storrs, CT 06269-3136, USA

---

### ARTICLE INFO

**Article history:**
Received 28 May 2014
Received in revised form 11 August 2014
Accepted 13 August 2014
Available online 22 August 2014

**Keywords:**
Octahedral molecular sieves
Niobium substitution
CO oxidation
DFT calculations
Fukui function$f^{\dagger}$

### ABSTRACT

Framework-substituted Mn oxide octahedral molecular sieves with different Nb concentrations (2-20 mol% Nb-K-OMS-2) were synthesized via a single-step reflux method allowing for direct incorporation of the dopant into the mixed-valent Mn structure. Their specific surface areas ranged from 75 to $199\,\text{m}^2\,\text{g}^{-1}$ with modified composition, size, morphology, porosity, thermal stability, and redox properties depending on the extent of substitution. Catalytic testing showed that the Nb-K-OMS-2 materials were active for CO oxidation and that the presence of Nb significantly enhanced the activity of pure K-OMS-2. For example, the conversions of 1% CO at $100\,^{\circ}\text{C}$ using 0%, 2%, 5%, 10%, 15%, and 20% Nb-K-OMS-2 were 4%, 10%, 25%, 62%, 59%, and 41%, respectively. When the $\text{O}_2$ concentrations increased from 1% to 10% at $120\,^{\circ}\text{C}$, the activities of 10% and 15% Nb-K-OMS-2 materials were improved by as much as 61% and 69%, respectively. These catalysts were also stable and less prone to deactivation by moisture (~3% $\text{H}_2\text{O}$) at temperatures $>100\,^{\circ}\text{C}$ than pure K-OMS-2. Theoretical calculations revealed that the substitution of Mn by Nb was a thermodynamically-favorable process and produced electrophilic centers, which can provide favorable sites for strong CO adsorption on the Nb-K-OMS-2 surface. The interaction of CO at these sites exhibited the beneficial effect of Nb substitution in the K-OMS-2 materials.

© 2014 Elsevier B.V. All rights reserved.

---

### 1. Introduction

Octahedral molecular sieves (OMS) are a family of compounds that are relatively benign and can be found in Nature as manganese nodules on the ocean floor [1]. The synthetic cryptomelane-type Mn oxide OMS (K-OMS-2) are inexpensive and have been extensively used for years in various applications including batteries, heterogeneous catalysis, ion-exchange, chemical sensing, and pollutant degradation [2-5]. K-OMS-2 materials are excellent catalysts due to the mixed valency of Mn ($\text{Mn}^{4+}$, $\text{Mn}^{3+}$, and $\text{Mn}^{2+}$). These catalysts are also both porous and semiconducting and can be regenerated with air or $\text{O}_2$.

For optimal reaction efficiency and selectivity in catalysis, K-OMS-2 can be tailored using a significant number of strategies including the manipulation of temperature, pH, time, and pressure under hydrothermal and reflux conditions, and the use of various co-solvents and reducing agents. Doping by subtle introduction of an active metal into the tunnel or framework sites of K-OMS-2 materials is another effective strategy to modify their properties and improve their catalytic performance. One of the applications of doped K-OMS-2 materials is the total and preferential oxidation of CO, wherein enhancement in activity and selectivity is achieved by introducing single-type, low-valent metal cations (M) such as $\text{Ag}^+$, $\text{Cu}^{2+}$, $\text{Zn}^{2+}$, and $\text{Co}^{2+}$ in the tunnel sites [6-8]. A special M-O-Mn bridge with suitable coordination for efficient charge transfer in the K-OMS-2 structure is suggested to be responsible for high activity of doped K-OMS-2 catalysts [6].

We reported the successful incorporation of $\text{V}^{5+}$ ions at different concentrations (1-20 mol%) into the K-OMS-2 framework as a recent example involving a high-valent cation [9]. V-K-OMS-2 materials grown by a simple reflux method produced cryptomelane with well-developed nanospherical structures, which are unusual as compared to the regular K-OMS-2 fibrous morphology. This study further provided an understanding of the effects of the

---

* Corresponding author at: Department of Chemistry, University of Connecticut, 55 North Eagleville Road, Storrs, CT 06269-3060, USA. Tel.: +1 860 486 2797; fax: +1 860 486 2981.
E-mail address: Steven.Suib@uconn.edu (S.L. Suib).

http://dx.doi.org/10.1016/j.apcatb.2014.08.021
0926-3373/© 2014 Elsevier B.V. All rights reserved.

amount of dopant and the mode of doping into the K-OMS-2 struc- ture on the enhancement of catalytic activity and selectivity for CO oxidation under diverse conditions. A considerable interest now is to generalize this synthetic approach by using other high-valent, non-noble transition metal dopants such as niobium for such reac- tions. Although no gas phase oxidation study has been reported in the literature so far on the use of Nb-K-OMS-2 materials, they were previously used for chemical sensing applications and pre- pared using $KNbO_{3}$ as a precursor synthesized via a conventional hydrothermal method [10]. Therefore, characterization and other activity testing of the materials need to be explored.

In the present study, we utilized a template/surfactant-free reflux method for the isomorphous substitution of Mn by Nb into the K-OMS-2 framework with $NbCl_{5}$ acting as the source of Nb dopant at different concentrations. Complete characterization techniques were employed in order to elucidate the dominating factors for improved activity by establishing potential relationships between the properties (e.g. structure, morphology, composition, surface area, porosity, thermal stability, and reducibility) and cat- alytic performance. Application-relevant tests were performed by exploring the effects of $O_{2}$ concentration and the presence of $H_{2}O$ vapor in the feed gas on the catalytic activity. The question of why and how the Nb substitution of Mn is directed toward increased activity of K-OMS-2 is fundamentally important. Therefore, we also demonstrate here for the first time the beneficial effect of the Nb substitution on the catalytic performance of K-OMS-2 for CO oxida- tion based on electronic properties obtained by density functional theory (DFT) calculations.

## 2. Experimental
### 2.1. Preparation of the catalysts

A solution containing 5.0g of $KMnO_{4}$ in 100 mL of distilled deionized water (DDW) was prepared to synthesize K-OMS-2. A second solution was then prepared by dissolving 7.5 g of $MnSO_{4}\cdot H_{2}O$ in 50.0 mL of DDW and adding 8.5 mL of concentrated $HNO_{3}$. This solution was subsequently added dropwise into the $KMnO_{4}$ solution with vigorous stirring forming a dark brown pre- cipitate. The resultant slurry was refluxed overnight at $100-110^{\circ}C$, washed with copious amounts of DDW, dried in an oven at $120^{\circ}C$ for 12 h, and ground into powders to obtain the K-OMS-2 material. To prepare 2%, 5%, 10%, and 20% Nb-K-OMS-2 materials, the above procedure was modified by adding appropriate amounts of aqueous $NbCl_{5}$ solution into the $KMnO_{4}$ solutions.

### 2.2. Characterization of the catalysts

Elemental analysis was conducted using a Thermo Jarrell Ash model ICAP 61E trace analyzer inductively-coupled plasma atomic emission spectrometer (ICP-AES). Powder X-ray diffraction (XRD) analysis was conducted on a Rigaku Ultima IV diffractometer (Cu Kα radiation, $\lambda=0.15406 nm$) with an operating voltage and cur rent of 40 kV and 44 mA, respectively. Raman spectroscopy was performed at room temperature on a Renishaw 2000 Raman micro- scope attached to a CCD camera, with an $Ar^{+}$ laser (514 nm) as the excitation source. The spectrometer was calibrated with a silicon wafer. The spectra were collected at 64 scans with a scan rate of $126 min^{-1}$.

Nitrogen sorption experiments were conducted on a Quanta- chrome Autosorb-1-1C automated adsorption system at liquid nitrogen temperature. Prior to measurement, the samples were degassed at $120^{\circ}C$ for 6 h. The surface areas of the synthesized materials were determined by the Brunauer-Emmett-Teller (BET) method.

The morphologies of the materials were recorded using a Zeiss DSM 982 Gemini field emission scanning electron microscopy (FESEM) with a Schottky emitter operating at an accelerating volt- age of 2.0 kV and a beam current of 1.0 mA. The samples were dispersed in ethanol with ultrasonic treatment for 30 min and drops of the suspension were placed on a copper grid. Transmis- sion electron microscopy (TEM) images and selected area electrondiffraction patterns (SAED) were obtained using a JEOL JEM 2010 FasTEM microscope operating at an accelerating voltage of 200 kV. The samples were loaded onto a carbon-coated gold grid.

X-ray photoelectron spectroscopy (XPS) studies were carried out on a PHI model 590 spectrometer with microprobes using Al Kα ($\lambda=1486.6 eV$) as radiation operated at an accelerating voltage of 12.5 kV. The powder samples were pressed onto carbon tapes mounted on double-sided adhesive copper tape stick to a sample stage, where Nb 3d, Mn 2p, and O 1s transitions were recorded. Charging effects were corrected by adjusting the binding energy of C 1s to 284.6 eV.

The thermal stability of the materials was determined using a Hi-Res TA instrument Model 2950 thermogravimetric analyzer(TGA) in an ultrahigh pure nitrogen atmosphere from $30^{\circ}C$ to $950^{\circ}C$ at a ramp rate of $20^{\circ}C min^{-1}$. Temperature programmed reduction (TPR) experiments were conducted using a gas mixture of 3% CO in He. Typically, a sample of about 0.2 g was packed into a quartz tube supported by quartz wool and loaded into a programmable tube furnace. Prior to analysis, the sample was pre- treated for 1 h by passing He gas (20 sccm) through the sample heated at $150^{\circ}C$. Desorbing gases were monitored using a Cirrus MKS residual gas analyzer equipped with a quadrupole mass selec- tive detector.

### 2.3. Catalytic evaluation for CO oxidation

The CO oxidation tests were conducted in a quartz tubular fixed- bed flow-type reactor at atmospheric pressure with 100 mg of catalysts, as described in our previous work [9,11]. The composition of feed gas was $1\% CO,1\% O_{2}$, and $5\% N_{2}$ in He. The space velocity in all experiments was $12000 mL h^{-1}g^{-1}$ and the reaction tempera ture ranged from $25^{\circ}C$ to $200^{\circ}C$. Nitrogen was used as the internal standard for gas chromatography (GC). Prior to analysis, the sample catalyst was pretreated for 2 h by passing He gas (20 sccm) through the sample heated at $150^{\circ}C$. Higher $O_{2}$ concentration (1% CO, 10% $O_{2},5\% N_{2}$ in He) and application-relevant tests (1% CO, $21\% O_{2}$, and $78\% N_{2}$ ) were analogously performed. Catalytic tests with moist feed gas $(\sim 3\% H_{2}O)$ were conducted analogously by passing the feed gas through a water bubbler at room temperature. Helium was used as the carrier gas and the composition of the effluent gas was analyzed online using an SRI model 8610C GC equipped with a 6' molecular sieve, a 6' silica gel column, and a thermal con- ductivity detector. Peak areas were collected by allowing 30 min stabilization at each reaction temperature. The peak areas of CO, $O_{2}$, and $CO_{2}$ were directly proportional to their concentrations and were used for quantitative analyses. $N_{2}$ was used as the internal standard. Stability studies of the most active catalysts were con- ducted for 24 h in a feed gas composition of $1\% CO,O_{2}$ (1% and 21%), and $5\% N_{2}$ in He under wet and dry conditions.

### 2.4. Computational details

A model was constructed based on our previous work repor- ting the crystallographic data of K-OMS-2 [12]. K-OMS-2 consists of double-wide slabs of edge-shared $MnO_{6}^{8-}$ octahedra. The tunnels are bound by four $Mn_{2}O_{6}^{4-}$ slabs, each rotated $90^{\circ}$ to its neigh bor, and joined through corner-shared O atoms. The unit cell (I4/m space) contains 16 O atoms and 8 Mn sites as shown in Fig. 1. Explic- itly shown in Fig. 1 are the two main Mn sites in the K-OMS-2 unit

![](./images/814702421933555712_4.jpg)

Fig. 1. Unit cell of the K-OMS-2 crystal structure: representation with (A) octahedral sites and (B) explicit atoms (Mn = gray, O = red, and K = purple). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

<table>
<caption>Table 1<br>Combined results of ICP-AES and N₂ physisorption experiments of undoped and Nb-K-OMS-2 materials.</caption>
<thead>
<tr>
<th>% Nb</th>
<th>Surface area (m² g⁻¹) ᵃ</th>
<th>Pore volume (cm³ g⁻¹) ᵇ</th>
<th>Mole% Nbᶜ</th>
<th>K:Mnᵈ</th>
</tr>
</thead>
<tbody>
<tr>
<td>0%</td>
<td>71</td>
<td>0.243</td>
<td>–</td>
<td>1:8.3</td>
</tr>
<tr>
<td>2%</td>
<td>75</td>
<td>0.314</td>
<td>2.1%</td>
<td>1:8.5</td>
</tr>
<tr>
<td>5%</td>
<td>81</td>
<td>0.306</td>
<td>4.5%</td>
<td>1:8.2</td>
</tr>
<tr>
<td>10%</td>
<td>158</td>
<td>0.328</td>
<td>9.4%</td>
<td>1:8.9</td>
</tr>
<tr>
<td>15%</td>
<td>169</td>
<td>0.295</td>
<td>14.6%</td>
<td>1:8.8</td>
</tr>
<tr>
<td>20%</td>
<td>199</td>
<td>0.474</td>
<td>17.1%</td>
<td>1:9.5</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">ᵃ BET specific surface area by N₂ physisorption.</td>
</tr>
<tr>
<td colspan="5">ᵇ BJH desorption cumulative pore volume N₂ physisorption.</td>
</tr>
<tr>
<td colspan="5">ᶜ Mole% Nb determined by ICP-AES.</td>
</tr>
<tr>
<td colspan="5">ᵈ K:Mn molar ratio determined by ICP-AES.</td>
</tr>
</tfoot>
</table>

cell. These apparently different Mn atoms by virtue of symmetry are important at the edge of the crystals, where the catalytic CO processes can take place. Here, we studied the isomorphic substitution of the Mn atom by Nb atom in each site of K-OMS-2. A cluster model was then built using the crystallographic coordinates. The CO adsorption on the different Mn or Nb sites was modeled and the corresponding energies for such adsorption were calculated.

The theoretical calculations were carried out using the density functional theory (DFT) within the well-known PW91 functional [13,14]. The basis set was represented by a double numerical polarized (DNP) basis in combination with effective core potentials for the treatment of the ionic cores. The systems studied were relaxed until the remaining total force was below 0.0002 Ha Å⁻¹. A thermal smearing of 0.05 Ha was used for geometry optimization and electronic property calculations. The Fukui functions were computed within the Hirshfeld population analysis. All the calculations were performed with the DMol³ code, which was included in the Materials Studio package [15,16].

## 3. Results and discussion

### 3.1. ICP-AES

The experimentally-determined concentrations of Nb in Nb-K-OMS-2 were in good agreement with the expected concentrations calculated from initial reaction mixtures, except for the 20% Nb-K-OMS-2 sample (Table 1). The exact average concentrations (mol%) of Nb in the Nb-K-OMS-2 materials with initial reaction mixtures of 2%, 5%, 10%, 15%, and 20% Nb were 2.1%, 4.5%, 9.4%, 14.6%, and 17.1%, respectively. The increasing concentration of Nb ions from 2% to 20% can be correlated with a successive reduction of the concentration of Mn ions relative to K ions in the materials, as shown in the K:Mn ratios.

![](./images/814702421933555712_5.jpg)

Fig. 2. Powder XRD patterns of K-OMS-2 materials with different Nb concentrations.

### 3.2. X-ray diffraction

The XRD patterns of undoped and Nb-K-OMS-2 materials were similar to the tetragonal structure of cryptomelane-type manganese oxide (JCPDS 29-1020) as shown in Fig. 2. The reflections obtained were characteristics of $2 \times 2$ tunnel structure of the regular OMS-2 [4]. However, the XRD patterns of samples with low levels of Nb (2% and 5%) appeared to have narrower and more intense peaks as compared to undoped K-OMS-2. This is indicative of the presence of small crystallite sizes of the latter. Nevertheless, XRD results suggest that in doped materials, Nb ions were highly dispersed into the structure of K-OMS-2 forming a solid solution. Slightly broader diffraction peaks and reduced peak intensities were obtained for 20% Nb-K-OMS-2 as compared to other Nb-K-OMS-2 materials, suggesting that the maximum allowable structural substitution limit of cryptomelane for Nb is ~15 mol%. Substitution beyond this point resulted in the disruption of the crystalline structure and consequent formation of an amorphous material. However, the absence of additional peaks attributed to Nb or Nb oxide phases and any obvious impurities in the materials suggests that a separate crystalline Nb compound did not form.

![](./images/814702421933555712_6.jpg)

Fig. 3. Raman spectra of K-OMS-2 materials with different Nb concentrations.

### 3.3. Raman spectroscopy

Fig. 3 shows the Raman spectra of Nb-K-OMS-2 materials. They reveal the absence of out-of-framework Nb oxides with structures possessing a Raman active Nb=O bond such as $NbO_4$ and $NbO_6$ structures, and crystalline $Nb_2O_5$ or amorphous $Nb_2O_5·H_2O$ [17,18]. The peaks in the range of $500-700\,\text{cm}^{-1}$ can be attributed to the $MnO_6$ octahedral double chains [19]. For example, pure K-OMS-2 exhibits a strong major peak centered at $\sim650\,\text{cm}^{-1}$ ($A_{1g}$ vibrational mode) together with a weak shoulder at $\sim570\,\text{cm}^{-1}$ ($F_{2g}$ vibrational mode), which are characteristic of Mn-O lattice vibrations [20]. These are indicative of a well-developed tetrago- nal structure with $2\times2$ tunnels. Here, an additional band centered at $\sim870\,\text{cm}^{-1}$ was observed, which becomes more prominent as the concentration of Nb in K-OMS-2 increases. This band is specific for Nb-O vibrations resulting from the elongation of Nb=O bonds typically located in the high wavenumber region between 900 and $1000\,\text{cm}^{-1}$ for free niobium pentoxide ($Nb_2O_5$) [17]. The absence of a Raman active feature between 900 and $1000\,\text{cm}^{-1}$ region in all materials suggests that no extra framework Nb from segregated Nb oxide particles was present, in line with the structural data obtained by XRD.

### 3.4. $N_2$ physisorption

The BET surface areas of K-OMS-2 increased with increasing Nb concentration (Table 1). The surface areas of undoped, 2%, and 5% Nb-K-OMS-2 materials were $71\,\text{m}^2\text{g}^{-1}$, $75\,\text{m}^2\text{g}^{-1}$, and $81\,\text{m}^2\text{g}^{-1}$, respectively, but those of 10%, 15% and 20% Nb-K-OMS-2 materials were relatively high ($158\,\text{m}^2\text{g}^{-1}$, $169\,\text{m}^2\text{g}^{-1}$, and $286\,\text{m}^2\text{g}^{-1}$, respectively). This trend can be correlated with the significant reduction of crystallinity as shown in their XRD patterns when the Nb concentration increased from 2% to 20% Nb.

The $N_2$ adsorption-desorption isotherms of the 2% and 5% Nb-K-OMS-2 materials exhibited Type II isotherms, whereas the 10%, 15%, and 20% Nb-K-OMS-2 materials exhibited Type IV isotherms (Fig. 4). At low $P/P_0$ or the region of monolayer coverage, 10%, 15%, and 20% Nb-K-OMS-2 materials had relatively higher slopes than 2% and 5% Nb-K-OMS-2 materials further indicating their relatively high surface areas and lowered degree of crystallinity. At high relative pressures, the differences in the shapes of the hysteresis loops distinct are indicative of the relative proportions of voids or pores between particles of Nb-K-OMS-2 materials as a consequence of their morphologies. For example, 2% and 5% Nb-K-OMS-2 materials showed relatively longer hysteresis loops, which indicates slit-shaped mesopores with varying sizes and shapes. The hysteresis loop for high level Nb doping materials stretched over a wide range of relative pressure ($\sim0.4-0.7$).

![](./images/814702421933555712_7.jpg)

Fig. 4. $N_2$ adsorption-desorption isotherms of K-OMS-2 materials with different Nb concentrations.

### 3.5. FESEM and TEM

The morphology of Nb-K-OMS-2 materials grown by a reflux method changed from nanorod structures to nanocrystallites depending on the Nb content, as shown in their FESEM and the TEM images (Fig. 5). The 2% Nb-K-OMS-2 had needle-like morphology, which is typical for synthetic cryptomelane materials. However, the average length of the particles was reduced from $\sim150-200\,\text{nm}$ to $\sim100\,\text{nm}$ in 5% Nb-K-OMS-2. Another notable feature is the expansion of the average width of the particles from $\sim20\,\text{nm}$ in 2% Nb-K-OMS-2 to $\sim50\,\text{nm}$ in 5% Nb-K-OMS-2. With 5% Nb, the size of the particles decreased dramatically forming grain-like structures or short nanorods of $\sim35\,\text{nm}$ in width and $\sim50\,\text{nm}$ in length. In 10% Nb-K-OMS-2, particles with crystallite size of $\sim20\,\text{nm}$ were formed. The formation of this morphology was most likely due to a slight distortion of the tetragonal crystal structure of cryptomelane to the monoclinic geometry. The ideal tetragonal unit cell can undergo small structural distortion that lowers the symmetry to the monoclinic space group $I2/m$ when large cations such as $Nb^{5+}$ substitute for octahedral $Mn^{4+}$ and $Mn^{3+}$ in K-OMS-2. This type of morphology can lead to a large number of adsorption sites in the materials. Reduced-growth, high surface area (BET), and low crystallinity (XRD) K-OMS-2 materials with 15% and 20% Nb consisted of uniform nanocrystallites throughout the material. No secondary phases in the FESEM and TEM images were observed in all the Nb doped materials, confirming the compositional homogeneity of Nb ions. This can be correlated again with the XRD results where no obvious impurity in the doped K-OMS-2 materials such as separate Nb compounds and that the dopant ions were highly dispersed into the unit cell of K-OMS-2.

![](./images/814702421933555712_8.jpg)

Fig. 5. Representative FESEM and TEM images (insets: SAED) of K-OMS-2 materials with different Nb concentrations.

The well-defined periodic lattice planes observed in the HRTEM images of K-OMS-2 confirmed the excellent crystallinity of these nanomaterials. Perfect surface structures were observed and no obvious surface defect sites were formed in the typical crystal structures of 2%, 5%, and 10% Nb-K-OMS-2 materials. The interplanar spacings observed are all in accordance with those measured with XRD for the bulk powder sample. The diminishing diffraction rings or spots in the SAED pattern of 20% Nb-K-OMS-2 revealed less crystalline phases, in line with the XRD results. No impurity phases were present in all the materials.

### 3.6. XPS

XPS results indicate that Nb species on the surface of the Nb-K-OMS-2 materials were not in a purely $5^+$ oxidation state. The oxidation state of Nb species using $NbCl_5$ as a precursor was between $4^+$ and $5^+$, as elucidated from the BEs of the Nb $3d_{5/2}$ peak centered between 205 eV and 207 eV, shifting closer to $5^+$ as the Nb content increases (Fig. 6) [19]. As expected, the intensities of the bands increased with increasing Nb loading.

The O 1s XPS spectra for Nb-K-OMS-2 materials are displayed in Fig. 7. Each spectrum was deconvoluted into three or four peaks corresponding to the types of oxygen species on the surface according to their peak positions: low BE peak (529.1-530.0 eV) ascribed to lattice O ($O_2^{2-}$); medium BE peak (530.1-532.0 eV) associated with surface adsorbed O ($O_2^-$ or $O^-$), $OH^-$ groups on the surface, and O vacancies; and high BE peak (532.1-533.4 eV) ascribed to adsorbed molecular $H_2O$ [21]. Low BE peak corresponds to O species bonded to metal cations in a coordinatively saturated environment ($O_{sat}$), whereas medium BE peak corresponds to O species bonded to metal cations in a coordinatively unsaturated environment.

![](./images/814702421933555712_9.jpg)

Fig. 6. Nb 3d XPS spectra of K-OMS-2 materials with different Nb concentrations.

![](./images/814702421933555712_10.jpg)

Fig. 7. O 1s XPS spectra of K-OMS-2 materials with different Nb concentrations.

environment ($\mathrm{O_{unsat}}$) [22]. The 20% Nb-K-OMS-2 possessed poorer lattice oxygen species on the surface than those of other Nb-K-OMS-2 materials. For instance, the % peak area ratio of $\mathrm{O_{sat}}$ to $\mathrm{O_T}$ ($\mathrm{O_T}$: $\mathrm{O_{sat}}+\mathrm{O_{unsat}}=100\%$) for 2-15% Nb-K-OMS-2 ranged from 0.59 to 0.62, whereas those for 20% Nb-K-OMS-2 was 0.47. This suggests that more Nb substituted into the framework of K-OMS-2 resulted in more surface metal cations in a low coordination environment causing possible formation of surface defects such as O vacancies. In addition, the % peak area of high BE O peak in 20% Nb-K-OMS-2 was the highest (16%). The $\mathrm{O_{sat}}$ BE values of Nb-K-OMS-2 materials were lower than those previously measured for pure manganese oxides such as K-OMS-2 (529.9 eV) and commercial $\mathrm{MnO_2}$ ($\beta$ form) (529.8 eV) under the same experimental conditions [4,23]. This means that the amount of available surface oxygen in the form of $\mathrm{OH^-/H_2O}$ on K-OMS-2 materials increases with Nb substitution.

### 3.7. TGA

The TGA profiles of Nb-K-OMS-2 materials were similar in terms of the shape of the curves and the temperature zones where three major weight losses occurred (Fig. 8). The first major weight loss between $30\ ^{\circ}\text{C}$ and $250\ ^{\circ}\text{C}$ was due to the desorption of physisorbed $\mathrm{H_2O}$ and $\mathrm{O_2}$ from the surface. This was followed by desorption of chemisorbed $\mathrm{H_2O}$ up to $580\ ^{\circ}\text{C}$. The second major weight loss between $580\ ^{\circ}\text{C}$ and $600\ ^{\circ}\text{C}$ was caused by the evolution of structural oxygen near the surface without decomposition of the material. The third major weight loss between $710\ ^{\circ}\text{C}$ and $750\ ^{\circ}\text{C}$ was due to the depletion of oxygen from the framework of the material resulting in phase transformation from $\mathrm{KMn_8O_{16}}$ to $\mathrm{Mn_2O_3}$ and then to $\mathrm{Mn_3O_4}$.

The 2% and 5% Nb-K-OMS-2 materials had fairly similar % weight losses from first to third major weight losses, whereas the 10%, 15%, and 20% Nb-K-OMS-2 materials had significantly steeper slopes of weight loss at low temperature regions. These results suggest higher overall weight losses for the 10%, 15%, and 20% Nb-K-OMS-2 materials due to the desorption of large amounts of physisorbed and chemisorbed $\mathrm{H_2O}$ and surface $\mathrm{O_2}$ than other materials, without the loss of structural oxygen, which can lead to decomposition. The similarities and differences in thermal stability can also be correlated with the observed changes in morphology and textural properties of the materials as a result of Nb substitution.

![](./images/814702421933555712_11.jpg)

Fig. 8. TGA profiles of K-OMS-2 materials with different Nb concentrations.

### 3.8. TPR

Fig. 9 presents the CO TPR profiles of the Nb-K-OMS-2 materials showing peaks corresponding to the formation of $\mathrm{CO_2}$. Three reduction peaks were observed. The first two peaks overlapped with each other—at $\sim 230\ ^{\circ}\text{C}$ (due to labile oxygen) and at $\sim 290\ ^{\circ}\text{C}$ (due to the reduction of $\mathrm{KMn_8O_{16}}$ to $\mathrm{Mn_3O_4}$. The maximum intensity of the third reduction peak was centered at $\sim 390\ ^{\circ}\text{C}$ (due to the reduction of $\mathrm{Mn_3O_4}$ to MnO). The intensity of the reduction peaks generally decreased as the concentration of Nb increased, partly due to pretreatment. Relative to 2% Nb-K-OMS-2, however, the first peaks were shifted to lower temperature regimes, whereas the second peaks were shifted to higher temperatures with increasing Nb concentration. The third peaks essentially remained in the same position. For example, relative to 2% Nb-K-OMS-2, 10% Nb-K-OMS-2 first peak shifted from $\sim 260\ ^{\circ}\text{C}$ to $\sim 200\ ^{\circ}\text{C}$, second peak shifted from $\sim 295\ ^{\circ}\text{C}$ to $\sim 310\ ^{\circ}\text{C}$, and third peak was still at $\sim 400\ ^{\circ}\text{C}$. These results strongly suggest that Nb substitution enhanced the mobility and liability of structural oxygen close to the surface of K-OMS-2, but slightly retarded Mn reduction. There were no increases in the peak intensities with Nb concentration, suggesting that a combined reduction of separate Nb and Mn oxide phases did not occur.

### 3.9. Electronic properties

The Nb incorporation in K-OMS-2 was studied by DFT methods to better understand the doping process. The $\Delta E$ for the Mn(1) substitution by Nb is $-331.5\ \text{kJ}\ \text{mol}^{-1}$, whereas the one for Mn(2) is $-281.4\ \text{kJ}\ \text{mol}^{-1}$. These values suggest that the substitution of the Mn(1) is energetically more favorable than the one for the Mn(2) site. The substitution of Mn by Nb in the framework is nevertheless an exothermic process for both sites. Experimentally, we did

<table>
<caption>Table 2<br>Condensed Fukui functions for undoped and Nb-K-OMS-2 materials by DFT calculations.</caption>
<thead>
<tr>
<th rowspan="2">Material</th>
<th colspan="4">Fukui function for nucleophilic attack, $f^-$</th>
</tr>
<tr>
<th>K</th>
<th>Mn(1)</th>
<th>Mn(2)</th>
<th>Nb</th>
</tr>
</thead>
<tbody>
<tr>
<td>K-OMS-2</td>
<td>0.024</td>
<td>0.044</td>
<td>0.026</td>
<td>–</td>
</tr>
<tr>
<td>Nb(1)-K-OMS-2</td>
<td>0.024</td>
<td>0.044</td>
<td>0.025</td>
<td>0.044</td>
</tr>
<tr>
<td>Nb(2)-K-OMS-2</td>
<td>0.010</td>
<td>0.047</td>
<td>0.032</td>
<td>0.086</td>
</tr>
</tbody>
</table>

$^\text{a}$ Fukui functions computed within the Hirshfeld population analysis.

not detect the presence of Nb isolated phases in the synthesized materials.

The substitution of Mn by Nb is thermodynamically possible. We then analyzed the electronic structure of the Nb-K-OMS-2 to get a deeper insight into the changes provided by Nb. By definition, the Fukui functions ($f$) are chemical descriptors for identifying the atom in a molecule which is most likely to react. Specifically, the information provided by the condensed Fukui functions for nucleophilic attack ($f^-$) predicts the susceptible atom toward CO attack. Therefore, the $f^-$ values provide information on the Nb substitution in the K-OMS-2 materials.

The calculated $f^-$ values for the Nb-K-OMS-2 system are summarized in Table 2. Nucleophilic attack is more favorable at the Mn(1) atom in the K-OMS-2. The Mn(1) and Mn(2) atoms, which seem identical because of the symmetry, exhibit difference in the $f^-$ values (0.044 and 0.026, respectively). This difference suggests that CO could have preferential and stronger interaction with Mn(1) than with Mn(2). The $f^-$ values were also calculated for the Nb substitution in the two sites. For the Nb(1)-K-OMS-2 system, the $f^-$ values remained almost the same in all the atoms, with a $f^-$ value for Nb(1) similar to that of Mn(1). The Nb substitution in the Mn(2) site produced changes in almost all the atoms. In general, the Mn(1) and Mn(2) sites increased their $f^-$ values from 0.044 to 0.047 and from 0.026 to 0.032, respectively. The $f^-$ values for K decreased from 0.024 to 0.010, with the one for Nb(2) being the highest (0.086). Therefore in the Nb(2)-K-OMS-2 material, the nucleophilic attack is therefore expected to be at the Nb site. The analysis of the Fukui functions strongly points out the effect of the Nb substitution to produce centers for nucleophilic attack in the K-OMS-2 materials, which is beneficial when a nucleophilic molecule such as CO is present at the surface of the catalyst.

![](./images/814702421933555712_12.jpg)

Fig. 9. CO TPR profiles (average of two measurements) of K-OMS-2 materials with different Nb concentrations.

<table>
<caption>Table 3<br>M-CO bond lengths and CO adsorption energies on two distinct sites of undoped and Nb-K-OMS-2 materials by DFT calculations.</caption>
<thead>
<tr>
<th>Material</th>
<th>M-CO bond length(Å)</th>
<th>CO adsorption energy (kJ mol$^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mn(1)-K-OMS-2</td>
<td>2.04</td>
<td>–88.5</td>
</tr>
<tr>
<td>Mn(2)-K-OMS-2</td>
<td>2.00</td>
<td>–53.5</td>
</tr>
<tr>
<td>Nb(1)-K-OMS-2</td>
<td>2.24</td>
<td>–110.1</td>
</tr>
<tr>
<td>Nb(2)-K-OMS-2</td>
<td>2.21</td>
<td>–131.4</td>
</tr>
</tbody>
</table>

The interaction of CO with Mn or Nb in the K-OMS-2 materials was also studied using DFT methods to develop deeper insights into the effect of Nb substitution. The optimized geometries for the CO adsorption on the Mn(1) and Mn(2) sites are shown in Fig. 10. The geometry of the K-OMS-2 is maintained after the geometry optimization and the adsorption of the CO is clearly observed on the Mn(1) and Mn(2) centers, respectively. Table 3 summarizes the values of the CO adsorption energy at different sites. The CO adsorption is an exothermic process for both sites. However, the adsorption energy for the CO adsorption on Mn(1) ($-88.5\ \text{kJ mol}^{-1}$) is larger as compared with Mn(2) ($-53.5\ \text{kJ mol}^{-1}$). Such differences in adsorption energies are in good agreement with the Fukui functions values for nucleophilic attack discussed above.

The optimized geometries for the CO adsorption for the Nb-K-OMS-2 on the Nb(1) and Nb(2) sites are depicted in Fig. 11. The geometry of the parent materials was conserved after the interaction with CO. We can appreciate the interaction of CO with the Nb(1) and Nb(2) centers. The bond length of M—CO with respect to Mn is larger for Nb, which can be explained in terms of the larger atomic radii of Nb than of Mn. The CO adsorption for both sites is also an exothermic process. Moreover, the energy for the CO adsorption on Nb sites is higher as compared with Mn sites indicating preferential adsorption. The CO adsorption energy on Nb(2) ($-131.4\ \text{kJ mol}^{-1}$) is higher than on Nb(1) ($-110.1\ \text{kJ mol}^{-1}$). This difference is also in good agreement with the Fukui functions for nucleophilic attack for each site. Therefore, the Nb substitution on the K-OMS-2 provides centers with stronger affinity with CO molecule as compared with pure K-OMS-2 which could be useful for its conversion.

### 3.10. Catalytic performance for CO oxidation

The catalytic performance, expressed as the average % CO conversion to $\text{CO}_2$, as a function of temperature of the synthesized materials is shown in Fig. 12. All Nb doped catalysts showed higher activities with increasing Nb concentration. The undoped and 2% Nb-K-OMS-2 catalysts, with almost similar surface areas and morphologies, gave relatively low CO conversions (<10%) below 120 °C. Remarkable enhancement in catalytic activity was observed at temperatures <120 °C. For example, ~80% increase and ~70% increase in CO conversion were observed by increasing the reaction temperature from 140 °C to 160 °C using 2% and 5% Nb-K-OMS-2 catalysts, respectively. The 10% Nb-K-OMS-2 showed the best activity and initiated catalytic CO oxidation in the low temperature regions (<100 °C). This catalyst showed excellent activities giving CO conversions of 62% at 100 °C and complete oxidation at 160 °C. The catalytic activity of the 20% Nb-K-OMS-2 was comparable to the 15% Nb-K-OMS-2 at ≤100 °C. At higher temperatures, 15% Nb-K-OMS-2 was more active than 20% Nb-K-OMS-2. These results suggest that 10% was the approximate optimum Nb loading for

![](./images/814702421933555712_13.jpg)

Fig. 10. Optimized geometries for the CO adsorption on the undoped K-OMS-2 material: Mn(1)-CO and (B) Mn(2)-CO.

![](./images/814702421933555712_14.jpg)

Fig. 11. Optimized geometries for the CO adsorption on the Nb-K-OMS-2 material: Nb(1)-CO and (B) Nb(2)-CO.

![](./images/814702421933555712_15.jpg)

Fig. 12. % CO conversions (average of three measurements) as a function of temperature over K-OMS-2 materials with different Nb concentrations using 1% CO, 1% O₂, and 5% N₂ in He under dry conditions.

efficient enhancement of CO oxidation under most experimental conditions. Commercial pure $Nb_2O_5$ powder was also tested under the same experimental conditions and found to be completely inactive for CO oxidation even up to $140\,^\circ\text{C}$. Finally, the catalytic activity of 10% Nb-K-OMS-2 was maintained high (100% conversion) during a 24-h time-on-stream at $160\,^\circ\text{C}$, indicating the stability of the catalyst (Fig. 13).

The effects of increasing $O_2$ concentration and the presence of water vapor ($\sim$3% $H_2O$) in the feed gas on the catalytic activity were also investigated (Fig. 14). At $100\,^\circ\text{C}$ using 1% CO and 10% $O_2$, the % conversions obtained using the 10% and 15% Nb-K-OMS-2 catalysts increased from 62% to 75% and 59% to 66%, respectively. At $120\,^\circ\text{C}$, when the $O_2$ concentrations increased from 1% to 10%, the activities of 10% and 15% Nb-K-OMS-2 materials were improved by as much as 61% and 69%, respectively. These results indicate the positive influence of $O_2$ concentration on the activity of Nb-K-OMS-2. Further increase in the $O_2$ concentration from 10% $O_2$ to 21% $O_2$ (realistic condition) promoted the catalytic activity of the most active catalyst, 10% Nb-K-OMS-2. For example, complete CO oxidation (100% conversion) was achieved at $100\,^\circ\text{C}$ and $120\,^\circ\text{C}$ using 21% $O_2$ under dry conditions. The activity of Nb-K-OMS-2 was maintained during stability tests at $100\,^\circ\text{C}$ and $160\,^\circ\text{C}$ due to facile reversibility of oxygen readsorption (continuously replenished by $O_2$ in the feed gas) on Nb-K-OMS-2 surface. Oxygen species desorbed from Nb-K-OMS-2 can oxidize CO molecules without destruction of the cryptomelane framework structure giving good stability. Gaseous oxygen species can oxidize the reduced Mn species and maintained the activity of Nb-K-OMS-2 material during CO oxidation reactions.

In the presence of water vapor, however, the 10% Nb-K-OMS-2 catalyst was poisoned even after using 21% $O_2$. For example, the % CO conversion dropped from 75% to 48% (stable in a 24-h trial run, Fig. 13) using the 10% Nb-K-OMS-2 catalyst at $100\,^\circ\text{C}$ and 21% $O_2$ under moist conditions. Nevertheless, the catalyst gained activity starting at $120\,^\circ\text{C}$ even reaching 100% conversion at $180\,^\circ\text{C}$ and $200\,^\circ\text{C}$ and showed better moisture tolerance as compared to undoped K-OMS-2 material. Water molecules can block the active sites of K-OMS-2 catalysts thereby deactivating the material. At moderate to high temperatures ($\geq120\,^\circ\text{C}$), the 10% Nb-K-OMS-2 showed greater tolerance to water deactivation than pure K-OMS-2 since there is enough energy for water desorption as well as for thermal activation of CO. Recall that the catalytic activity can be attributed to the involvement of oxygen and these species (surface oxygen, hydroxyl groups, and oxygen vacancies due to Nb substitution) on the active sites are more pronounced in 10% Nb-K-OMS-2 than in pure K-OMS-2 as shown in TGA and TPR results. Theoretical calculations further revealed that the interaction of CO at electrophilic centers or sites exhibited the beneficial effect of Nb substitution in the K-OMS-2 materials. Therefore, the experimentally observed enhanced catalytic activity of Nb-K-OMS-2 as compared with K-OMS-2 is strongly supported by the energetics and Fukui parameters for nucleophilic attack derived from the DFT calculations.

![](./images/814702421933555712_16.jpg)

Fig. 13. % CO conversions (one measurement) as a function of reaction time over 10% Nb-K-OMS-2 using 1% CO: stability tests under dry and wet conditions.

![](./images/814702421933555712_17.jpg)

Fig. 14. % CO conversions as a function of temperature (average of three measurements) over 10% and 15% Nb-K-OMS-2 materials using 1% CO: effects of O₂ concentration and water vapor.

## 4. Conclusions

In summary, high-valent Nb ions were successfully incorporated into the K-OMS-2 framework structure prepared by a facile simple reflux method, tailoring the morphology, particle size, and surface area of the materials. The morphological evolution from nanofibers to nanocrystallites enabled us to observe how the synthetic K-OMS-2 structure systematically responds to high-valent Nb doping. The structural crash point of doped K-OMS-2 was found beyond 15% Nb loading. The 10% and 15% Nb-K-OMS-2 catalyst showed the highest catalytic activity among all of the Nb-OMS-2 catalysts tested. Comparison between catalytic activities of doped K-OMS-2 under dry and wet conditions showed that the 10% Nb-K-OMS-2 catalyst was poisoned but was more moisture tolerant than undoped K-OMS-2. Theoretical calculations by DFT showed that the substitution of Mn by Nb was an exothermic process and produced centers for nucleophilic attack by CO. These centers can provide favorable sites for strong CO adsorption on the Nb-K-OMS-2 surface. Therefore, the interaction of CO with Nb doped K-OMS-2 presented the beneficial effect of the Nb in the K-OMS-2 materials. High valency substitution of K-OMS-2 is now considered as another novel strategy to fine-tune the properties of the material to the desired task, such as the manipulation of temperature, pressure, pH and solvents.

## Acknowledgements

We thank Drs. Heng Zhang and Lichun Zhang for their help with the XPS and TEM experiments, respectively. We also thank Dayton Horvath for his help with the synthesis of the materials and useful discussions. This work was supported by the U.S. Department of Energy, Office of Basic Energy Sciences, Division of Chemical, Geochemical, and Biological Sciences under Contract DE-FG02-86ER13622.A0000.

## References

[1] H. Genuino, H. Huang, E. Njagi, L. Stafford, S.L. Suib, in: A. Perosa, M. Selva (Eds.), A Review of Green Synthesis of Nanophase Inorganic Materials for Green Chemistry Applications, Handbook of Green Chemistry, vol. 8, John Wiley and Sons, Inc, 2012, pp. 217-244.
[2] T. Oishi, K. Yamaguchi, N. Mizuno, ACS Catal. 1 (2011) 1351-1354.
[3] H. Huang, C.-H. Chen, L. Xu, H. Genuino, J. Garcia-Martinez, H.F. Garces, L. Jin, C. King'ondu, S.L. Suib, Chem. Commun. 46 (2010) 5945-5947.
[4] H.C. Genuino, S. Dharmarathna, E.C. Njagi, M.C. Mei, S.L. Suib, J. Phys. Chem. C 116 (2012) 12066-12078.
[5] S.L. Suib, Acc. Chem. Res. 41 (2008) 479-487.
[6] G.G. Xia, Y.G. Yin, W.S. Willis, S.L. Suib, J. Catal. 185 (1999) 91-105.
[7] R. Hu, L. Xie, S. Ding, J. Hou, Y. Cheng, D. Wang, Catal. Today 131 (2008) 513-519.
[8] M. Özacar, A.S. Poyraz, H.C. Genuino, C.H. Kuo, Y. Meng, S.L. Suib, Appl. Catal. A: Gen. 462-463 (2013) 64-74.
[9] H.C. Genuino, Y. Meng, D.T. Horvath, C.H. Kuo, A.M. Morey, R. Joesten, S.L. Suib, ChemCatalChem 5 (2013) 2306-2317.
[10] M. Polverejan, J.C. Villegas, S.L. Suib, J. Am. Chem. Soc. 126 (2004) 7775-7777.
[11] E.C. Njagi, C.-H. Chen, H. Genuino, H. Huang, S.L. Suib, Appl. Catal. B: Environ. 99 (2010) 103-110.
[12] C. Calvert, R. Joesten, K. Ngala, J. Villegas, A. Morey, X. Shen, S.L. Suib, Chem. Mater. 20 (2008) 6382-6388.
[13] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Perdeson, D.J. Singh, C. Fiolhais, Phys. Rev. B 46 (1992) 6671.
[14] J.P. Perdew, Phys. B: Condens. Matter 172 (1991) 1.
[15] B. Delley, J. Chem. Phys. 92 (1990) 508.
[16] B. Delley, J. Chem. Phys. 113 (2000) 7756.
[17] J.-M. Jehng, I.E. Wachs, Chem. Mater. 3 (1991) 100-107.
[18] B.X. Huang, K. Wang, J.S. Church, Y.-S. Li, Electrochim. Acta (1999) 2571-2577.
[19] C. Julien, M. Massot, S. Rangan, M. Lemal, D.J. Guyomard, Raman Spectrosc. 33 (2002) 223.
[20] C. Julien, M. Massot, R. Baddour-Hadjean, S. Franger, S. Bach, J.P. Pereira-Ramos, Solid State Ionics 159 (2003) 345-356.
[21] J.P. Holgado, G. Munuera, J.P. Espinos, A.R. Gonzalez-Elipe, Appl. Surf. Sci. 158 (2000) 164-171.
[22] R. Larachi, A. Pierre, A. Adnot, A. Bernis, Appl. Surf. Sci. 195 (2002) 236-250.
[23] Y. Meng, H.C. Genuino, C.-H. Kuo, H. Huang, S.-Y. Chen, L. Zhang, A. Rossi, S.L. Suib, J. Am. Chem. Soc. 135 (2013) 8594-8605.