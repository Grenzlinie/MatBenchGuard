OPEN
# Molecular modeling analyses of functionalized cellulose

Hend A. Ezzat¹, Nayera M. El-Sayed², Dina Shehata³, Hanan Elhaes³, Asmaa Ibrahim³, Haitham Kalil⁴, Medhat A. Ibrahim⁵,⁶, Moataz M. Yousef⁷, Ibrahim S. Yahia⁸, Heba Y. Zahran⁸ & Islam Gomaa⁷

Functionalization of cellulose with nanomaterials and functional groups is essential for enhancing its properties for specific applications, such as flexible sensors and printed electronics. This study employs Hartree Fock (HF) and Density Functional Theory (DFT) calculations to investigate the vibrational spectra of cellulose, identifying DFT: B3LYP/3-21 g** as the optimal model aligning with experimental spectra. Using this model, we examined the impact of functionalizing cellulose with various groups (OH, NH₂, COOH, CH₃, CHO, CN, SH) and graphene oxide (GO) on its electronic properties. The results indicate that cellulose functionalized with GO (Cellulose-GO) has the lowest bandgap energy (0.1687 eV), and improvements in reactivity, stability, and electronic properties were confirmed through Molecular Electrostatic Potential (MESP) and Total Dipole Moment (TDM) analyses. The spectrum of Density of States (DOS) for the cellulose functionalized with different groups shows several peaks, indicating various energy levels where electronic states are concentrated. The Projected Density of States (PDOS) analysis reveals how different functional groups affect the electronic structure of cellulose. Moreover, the (Cellulose-GO) composite was characterized using an Attenuated Total Reflection Fourier Transform Infrared (ATR-FTIR) spectrometer, revealing interaction through the OH group of CH₂OH, as indicated by a new band at 1710 cm⁻¹, consistent with theoretical predictions. Overall, this study demonstrates that functionalization with GO enhances cellulose's responsiveness, degradation, and electrical properties, making it suitable for applications in flexible electronic devices and protective barriers against corrosion.

**Keywords** Cellulose, Nanocomposite, GO, DFT: B3LYP/3-21 g**, ATR-FTIR

Surface functionalization is an effective way to alter the properties of a material's surface¹. Recently, polymer surface functionalization has gained importance for managing the electronic characteristics and activity of polymer surfaces². This is achieved by modifying the polymer with active functional groups and/or nanomaterials³ˡ⁴. Advancing natural polymers through functionalization represents an important step in green technology⁵. Among natural polymers, conjugated polymers that can be processed with the appropriate solution are always among the sought-after candidates for inexpensive electronics and optoelectronics technology⁶. Additionally, organic molecule-based materials have become highly significant in materials science, particularly for applications in optoelectronic and mechanochromic luminescent devices⁷. These materials, with their conjugated electron systems, offer enhanced efficiency, stability, and flexibility, making them promising candidates for advanced research. In this context, functionalizing polysaccharides with various organic groups presents an opportunity to leverage these properties.

Polysaccharides, as the most important type of natural polymer, have efficient and active functional groups that perform a wide range of crucial functions⁸. Cellulose, the most well-known polysaccharide, is composed of D-anhydro glucopyranose units linked by -(1,4)-glycosidic bonds⁹. It is a widely available renewable resource, sourced from plants such as trees, cotton, and hemp, making it inexpensive to produce due to established and

¹Nano Unite, Space Lab, Solar and Space Research Department, National Research Institute of Astronomy and Geophysics (NRIAG), Helwan, Cairo 11421, Egypt. ²Physics Department, Faculty of Science, Mansoura University, Mansoura 35516, Egypt. ³Physics Department, Faculty of Women for Arts, Science and Education, Ain Shams University, Cairo 11757, Egypt. ⁴Chemistry Department, Faculty of Science, Suez Canal University, Ismailia 41522, Egypt. ⁵Spectroscopy Department, National Research Centre, 33 El-Bohouth St., Dokki, Giza 12622, Egypt. ⁶Molecular Modeling and Spectroscopy Laboratory, Centre of Excellence for Advanced Science, National Research Centre, 33 El-Bohouth St., Dokki, Giza 12622, Egypt. ⁷Nanotechnology Research Centre (NTRC), The British University in Egypt (BUE), Suez Desert Road, El-Sherouk City, Cairo 11837, Egypt. ⁸Nanoscience Laboratory for Environmental and Bio-Medical Applications (NLEBA), Semiconductor Lab., Metallurgical Lab.1., Physics Department, Faculty of Education, Ain Shams University, Roxy, Cairo 11757, Egypt. ✉️email: ma.khalek@nrc.sci.eg

cost-effective extraction and processing methods¹⁰. Cellulose's natural porosity makes it ideal for filtration and absorbent products like air filters, as well as for certain battery components¹¹. Its ability to form thin films and sheets is essential for industrial uses, such as packaging materials, biodegradable plastics, photographic film bases, coatings, and membranes¹². With high permittivity, cellulose can store and release electrical energy, making it suitable for electronic applications like capacitors¹³. Additionally, its chemical stability ensures durability and performance in diverse environments¹⁴. Thus, cellulose is utilized in a wide range of applications¹⁵⁻¹⁸.

Natural fibrous materials have emerged as a practical alternative to synthetic fibers¹⁹. However, regenerated cellulose's weak mechanical properties limit its use as a membrane material. To enhance its properties, other materials are often added to cellulose, resulting in composites with improved chemical and physical capabilities²⁰,²¹. Functionalizing cellulose and its derivatives with graphene oxide (GO) enhances their thermal stability and ion transport²²,²³, making them suitable for applications like UV shielding and water purification²⁴,²⁵. Functional groups containing oxygen atoms can bind metal ions or polymers like cellulose to form metal complexes. Dispersion of nanoparticles in a polymer matrix improves mechanical, thermal, and electrochemical properties²⁶. Each nanoparticle, such as GO, enhances different aspects of the polymer. Graphene, a two-dimensional sheet of sp2 bonded carbon, has unique visual, electrochemical, mechanical, and thermal properties²⁷. Graphene oxide (GO), a chemically synthesized precursor of graphene, contains various oxygenated functional groups. These groups disrupt graphene's conjugated structure, making GO an insulating material, but also improve interfacial interaction with substrates, significantly enhancing the physical properties of composite materials²⁸.

Molecular modeling is a computational technique that simulates chemical structures and reactions numerically. Its primary role is to provide insights into molecules and reactions that are difficult to observe directly, such as transition states and unstable intermediates²⁹. This method assesses the energy of molecular structures, optimizes their geometry, and calculates their vibrational frequencies³⁰. It is widely used to generate reliable spectroscopic and structural data across various fields³¹. Semi-empirical methods, which use parameters from experimental results, simplify computations, offering cost-effective and reasonably accurate predictions of energy and structures when good parameters are available³². These methods are largely based on quantum mechanics and produce high-quality quantitative estimates for many systems³³. Density Functional Theory (DFT) is similar to ab initio methods, requiring comparable computational effort as Hartree-Fock theory, the least expensive ab initio method. DFT calculations have been extensively used to investigate the electronic and photovoltaic properties of materials³⁴. It is preferred for its inclusion of electron correlation effects, providing more accurate results than some ab initio methods³⁵. Although DFT has limitations, such as issues with exchange interaction treatment and long-range noncovalent interactions, it is highly effective for small molecular systems³⁶.

The primary goal of this research is to conduct vibrational computations for cellulose to identify the optimal basis set that aligns with experimental results. Theoretical calculations were performed using HF and DFT: B3LYP with various basis sets, including 3-21 g, 6-31 g, 6-311 g, LANL2DZ, and LANL2MB. The best basis set will then be used to determine the most suitable site for cellulose chain functionalization (center or terminal). Additionally, to study the impact of functionalization on cellulose's electrical properties and bandgap variation, key properties such as total dipole moment, HOMO-LUMO energy gap, molecular electrostatic potential, and density of states (DOS) were calculated for these model molecules. Several functional groups, including (OH, NH₂, COOH, CH₃, CHO, CN, SH) and GO, were proposed for cellulose functionalization at the ideal interaction site.

## Materials and methods
### Materials
Pure microcrystalline cellulose powder (20 µm) was sourced from Sigma-Aldrich Company, Inc., USA, and dimethyl sulfoxide (DMSO) was obtained from Labscan Ltd., for film preparation. Graphene oxide (GO) was synthesized using graphite powder from Fluke, Germany, and solvents including H₂SO₄ (98%), H₂O₂ (30%), and HCl (33%), all purchased from El-Nasr Pharmaceutical Company in Egypt. Additionally, KMnO₄ was acquired from Alfa Aesar (98%, Germany).

### Synthesis of GO
The Hummers method was used to synthesize GO³⁷. In this process, 1 g of graphite was stirred with 35 ml of H₂SO₄ and 3 g of KMnO₄ for about an hour in an ice-water bath, keeping the temperature below 20 °C. After an hour, approximately 105 ml of H₂O₂ was gradually added to the solution and heated to around 100 °C. The mixture was then diluted with 280 ml of distilled water. The resulting GO precipitate was washed with 2 M HCl, followed by water, and then dried.

### Preparation of cellulose and cellulose-GO
The casting method was employed to prepare cellulose films and cellulose films containing a significant amount of GO. For the cellulose film, 0.25 g of cellulose was dissolved in 100 mL of DMSO using a magnetic stirrer at 800 rpm for 2 h at 70 °C until fully dissolved, and then cast into a glass petri dish. For the Cellulose-GO film, 0.25 g of cellulose was dissolved in 100 mL of DMSO as before, and then 0.025 g (10% wt.) of GO was added. The mixture was stirred at the same temperature for 2 h or until the solution became homogeneous, and then dried in glass petri dishes.

### Fourier transform infrared spectroscopy
The Fourier Transform Infrared (FTIR) spectra were obtained using a Vertex 70 FTIR spectrometer manufactured by Bruker Optik GmbH, Germany. The instrument was equipped with a diamond ATR crystal system and operated in the spectral range of 4000–400 cm⁻¹with a spectral resolution of 4 cm⁻¹.

### Calculation details
Optimization and vibrational calculations were conducted for Cellulose using HF³⁸and DFT: B3LYP methods³⁹⁻⁴¹, employing various basis sets such as 3-21 g, 6-31 g, 6-311 g, LANL2DZ, and LANL2MB. The DFT/B3LYP functional with various basis sets was chosen based on its established reliability and accuracy for organic compounds. This level of theory has been widely accepted in the literature for studying the electronic properties of polymers and functionalized materials. The combination of DFT and B3LYP has been shown to yield satisfactory results for predicting binding energies, electronic structures, and other critical properties relevant to our study. The Gaussian 09 software package from Gaussian, Inc., Wallingford, CT, USA, was utilized for structure optimization and molecular characteristic calculations at the Molecular Spectroscopy and Modeling Unit, National Research Centre, Cairo, Egypt⁴². Total Dipole Moment (TDM), bandgap energy, and Molecular Electrostatic Potential (MESP) were also determined for functionalized cellulose with different groups (OH, NH2, COOH, CH₃, CHO, CN, SH) and graphene oxide (GO) using the DFT: B3LYP/3-21 g** model⁴³,⁴⁴. Moreover, various parameters indicative of inhibition efficiency was determined through DFT calculations to evaluate the inhibition enhancement resulting from functionalization with GO. The quantum parameters included electron affinity (EA = −ELUMO), ionization potential (IP = −EHOMO), global hardness (η = (IP−EA)/2), chemical softness (σ=1/η), electronegativity (χ = (IP+EA)/2), fraction of transferred electrons (ΔN = (χFe−χinh)/2(ηFe−ηinh), where χFe represents the electronegativity of iron (which is zero) and ηFe (which is 7 eV)), and electrophilicity index (ω)⁴⁵,⁴⁶. Chemical hardness and softness were also calculated. These parameters simulate the chemical reactivity and stability of structures.

### Results and discussion
#### Molecular modeling study
A model of cellulose was constructed using three cellulose units. Initially, optimization and vibrational spectra calculations were performed using the HF and DFT: B3LYP methods with various basis sets (3-21G, 6-31G, 6-311G, LANL2DZ, and LANL2MB) to compare with experimental data. The cellulose model was then considered for functionalization with the OH group in two ways: at the center and terminal units, as depicted in Fig. 1. The functionalization was envisioned to occur through the CH₂OH group, assuming a complex interaction between the OH group and the active site of the cellulose CH₂OH group (both the center and terminal). To determine the optimal contact site, the binding energy of these two positions was calculated. Various functional groups, including OH, NH₂, COOH, CH₃, CHO, CN, SH, and graphene oxide (GO) were proposed for cellulose functionalization at the optimal interaction site. Consequently, these functional groups were suggested for cellulose functionalization at the terminal position, as depicted in Fig. 2.

#### Binding energy
DFT: B3LYP/3-21G** was employed to explore the optimal functionalization position along the cellulose chain (center or terminal). The binding energies for cellulose functionalized with the OH group were calculated for both the center and terminal units. Table 1 presents the total energy and binding energies computed. Binding energy values are presented in a.u. and eV. Based on the current data, Cellulose-OH-Terminal has a more negative BE (-0.594 a.u. or -16.163 eV) compared to Cellulose-OH-Center (-0.564 a.u. or -15.347 eV), indicating that functionalization at the terminal unit is more energetically favorable. This trend suggests that terminal OH groups interact more strongly with cellulose, supporting greater stability. In other words, cellulose-OH- Terminal demonstrated the lowest negative binding energy, indicating it as the most favorable site for cellulose functionalization⁴⁷.

#### Energies and MESP of functionalized cellulose with different functional groups
To assess the impact of functionalization on cellulose activity, the Total Dipole Moment (TDM), bandgap energy, and Molecular Electrostatic Potential (MESP) were examined. Table 2 presents the calculated variations in TDM and bandgap energy (ΔE) for the investigated interactions. The TDM of functionalized cellulose ranged from 4.353 Debye to 63.976 Debye for OH, NH₂, COOH, CH₃, CHO, CN, SH, and GO, respectively. Similarly, the bandgap energy (ΔE) of functionalized cellulose ranged from 7.944 eV to 0.168 eV for OH, NH₂, COOH,

![](./images/1063669143951114247_1.jpg)

Figure 1. Optimized structure of a cellulose model consisting of three units, functionalized with an OH group at the active site of the CH 2 OH group in two different positions: (a) Center, and (b) Terminal.

![](./images/1063669143951114247_2.jpg)

Figure 2. DFT: B3LYP/3-21 g** optimized structure of cellulose functionalized with various functional groups interacting through the CH 2 OH active site at the terminal position: (a) Cellulose, (b) Cellulose-OH, (c) Cellulose-NH 2 , (d) Cellulose-COOH, (e) Cellulose-CH 3 , (f) Cellulose-CHO, (g) Cellulose-CN, (h) Cellulose-SH, and (i) Cellulose-GO.

<table><thead><tr><th>Structures</th><th>TE, (a.u)</th><th>Binding Energy (a.u)</th><th>Binding Energy (eV)</th></tr></thead><tbody><tr><td>OH</td><td>-75.311</td><td></td><td></td></tr><tr><td>Cellulose</td><td>-1898.381</td><td></td><td></td></tr><tr><td>Cellulose-OH-Center</td><td>-1973.132</td><td>-0.564</td><td>-15.347</td></tr><tr><td>Cellulose-OH-Terminal</td><td>-1973.103</td><td>-0.594</td><td>-16.163</td></tr></tbody></table>

Table 1. The calculated total energy (TE) and binding energy as (a.u and eV) for cellulose and functionalized cellulose with OH group through active side CH₂OH in the two different positions center and terminal units.

$CH_3$, $CHO$, $CN$, $SH$, and GO, respectively. The notable reduction in $\Delta E$ for Cellulose-GO, which has the lowest bandgap energy (0.1687 eV), suggests enhanced reactivity and improved electronic conductivity. This supports previous findings by Sagadevan et al., who observed that GO-functionalized composites displayed similar improvements in conductivity and reactivity due to reduced bandgap values⁴⁸. The concurrent increase in TDM and reduction in bandgap energy ($\Delta E$) underscores the enhancement in both the electrical properties and structural stability of cellulose⁴⁹. Furthermore, the substantial TDM increase in Cellulose-GO (63.975 Debye) aligns with research by Brakat et al., which demonstrated that GO functionalization significantly increased polarizability, thereby making the material more suitable for applications like flexible electronics and sensors⁵⁰. The observed correlation between elevated TDM and lowered $\Delta E$ reflects improved electrical characteristics and stability in cellulose, in agreement with findings from other studies on functionalized polysaccharides and nanocomposites⁵¹. This combination of properties indicates that Cellulose-GO is highly compatible with applications requiring both high electrical responsiveness and stability, such as electronic devices and protective coatings.

MESP serves as another crucial descriptor for assessing the reactivity of chemical interactions, as it delineates the impact of alterations in charge distribution on structural reactivity⁵². Figure 3 illustrates the MESP of both cellulose and functionalized cellulose with diverse functional groups and GO. Consequently, the MESP surface maps of functionalized cellulose were depicted in Fig. 3 using a spectrum of colors ranging from red (representing the highest charge area) to blue (representing the lowest charge region). The active site of cellulose was identified as the OH group of the $CH_2OH$ group. Upon functionalization of cellulose with various functional groups, the intensity of the red color in the regions along the polymer chain increased. The physical characteristics and reactivity of all functional groups, particularly Cellulose-GO, exhibited significant enhancement, rendering it suitable for a broad spectrum of applications. TDM, bandgap energy, and MESP were examined for cellulose models with different functional groups to scrutinize the impact of functionalization on cellulose activity.

### Inhibition parameters for cellulose-GO
As shown in Table 3, the functionalization of cellulose with graphene oxide (GO) significantly alters its electronic properties. Notably, the cellulose/GO composite exhibits a marked increase in chemical softness ($\sigma$), while its chemical hardness ($\eta$) is considerably lower than that of cellulose alone. This indicates that cellulose/GO has a greater tendency to adapt to an external electronic environment, enhancing its reactivity. Such increased softness, along with the decreased hardness, supports the composite's ability to inhibit chemical reactions by adsorbing effectively onto metal surfaces. These properties are critical for corrosion inhibition applications, where a material's reactivity and adsorption capacity are paramount.

Furthermore, the calculated $\Delta N$ values, which represent the electron-donating ability of the inhibitors, indicate that cellulose/GO exhibits a significantly enhanced ability to donate electrons compared to pristine cellulose. This can be observed in the relative changes in the ionization potentials (I) and electronic affinities (A) across the different structures. For instance, the ionization potential of cellulose/GO is notably lower than that of cellulose, which implies a greater capacity for electron donation. In contrast, the electronic affinity remains relatively stable, suggesting that while cellulose/GO is more willing to lose electrons, it maintains its ability to stabilize additional charge. These attributes highlight the superior reactivity of cellulose/GO as an effective inhibitor, reinforcing its potential for applications requiring electron transfer and corrosion protection.

Additionally, the electrophilicity index ($\omega$), calculated as $\omega = \mu 2/2\eta$, confirms the unique inhibitory properties of cellulose/GO⁵³. With a significantly elevated $\omega$ value, cellulose/GO demonstrates a strong ability to stabilize additional electronic charge through interactions with the metal surface. This stability, combined with its high electrophilicity, indicates that cellulose/GO not only acts as an effective inhibitor but also demonstrates enhanced stability and reactivity compared to unmodified cellulose. These attributes make cellulose/GO particularly well-suited for applications in corrosion prevention, where a balance of high softness, reactivity, and electron-donating capability is advantageous.

<table>
  <thead>
    <tr>
      <th>Structures</th>
      <th>TDM (Debye)</th>
      <th>ΔE (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cellulose</td>
      <td>4.353</td>
      <td>7.944</td>
    </tr>
    <tr>
      <td>Cellulose -OH</td>
      <td>4.051</td>
      <td>6.654</td>
    </tr>
    <tr>
      <td>Cellulose -NH₂</td>
      <td>4.212</td>
      <td>8.017</td>
    </tr>
    <tr>
      <td>Cellulose -COOH</td>
      <td>2.123</td>
      <td>7.507</td>
    </tr>
    <tr>
      <td>Cellulose -CH₃</td>
      <td>2.997</td>
      <td>8.074</td>
    </tr>
    <tr>
      <td>Cellulose -CHO</td>
      <td>3.391</td>
      <td>6.665</td>
    </tr>
    <tr>
      <td>Cellulose -CN</td>
      <td>6.957</td>
      <td>6.571</td>
    </tr>
    <tr>
      <td>Cellulose -SH</td>
      <td>3.188</td>
      <td>5.968</td>
    </tr>
    <tr>
      <td>Cellulose -GO</td>
      <td>63.975</td>
      <td>0.168</td>
    </tr>
  </tbody>
</table>

Table 2. TDM (Debye) and HOMO-LUMO bandgap energy $\Delta E$ (eV) for cellulose and functionalized cellulose with different functional groups and GO interacted through the active side of cellulose $CH_2OH$ group in terminal position.

![](./images/1063669143951114247_3.jpg)

Figure 3. MESP of cellulose functionalized with various functional groups interacting through the terminal position using DFT: B3LYP/3-21 g**: (a) Cellulose, (b) Cellulose-OH, (c) Cellulose-NH 2 , (d) Cellulose-COOH, (e) Cellulose-CH 3 , (f) Cellulose-CHO, (g) Cellulose-CN, (h) Cellulose-SH, and (i) Cellulose-GO.

## Calculated DOS and PDOS
Figure 4 presents the Density of States (DOS) spectrum for unmodified cellulose and cellulose functionalized with various functional groups and GO. The DOS spectrum provides crucial information on the distribution of electronic states within the material, offering insights into its electronic properties. In the DOS plots, the blue line represents the density of electronic states across various energy levels. Peaks in this spectrum indicate energy levels where many electronic states are concentrated. The green lines correspond to energy levels occupied by electrons in the molecule's ground state, which are located below the Fermi level (set to 0 eV). The red lines, on the other hand, indicate unoccupied energy levels, or virtual states, above the Fermi level. The energy region

<table>
<thead>
<tr><th>Structure</th><th>LUMO</th><th>HOMO</th><th>Ionization Potential (I)</th><th>Electronic Affinity (A)</th><th>Electronic chemical potential (μ)</th><th>Chemical hardness (η)</th><th>Absolute softness (σ)</th><th>Electrophilicity index (ω)</th></tr>
</thead>
<tbody>
<tr><td>Cellulose</td><td>1.442</td><td>-6.502</td><td>6.502</td><td>-1.442</td><td>-2.530</td><td>3.972</td><td>0.252</td><td>0.806</td></tr>
<tr><td>Cellulose -OH</td><td>0.179</td><td>-6.475</td><td>6.475</td><td>-0.179</td><td>-3.148</td><td>3.327</td><td>0.300</td><td>1.489</td></tr>
<tr><td>Cellulose -NH₂</td><td>1.597</td><td>-6.419</td><td>6.419</td><td>-1.597</td><td>-2.410</td><td>4.008</td><td>0.249</td><td>0.725</td></tr>
<tr><td>Cellulose -COOH</td><td>0.973</td><td>-6.533</td><td>6.533</td><td>-0.973</td><td>-2.779</td><td>3.754</td><td>0.266</td><td>1.029</td></tr>
<tr><td>Cellulose -CH₃</td><td>1.638</td><td>-6.435</td><td>6.435</td><td>-1.638</td><td>-2.398</td><td>4.037</td><td>0.248</td><td>0.712</td></tr>
<tr><td>Cellulose -CHO</td><td>0.055</td><td>-6.61</td><td>6.61</td><td>-0.055</td><td>-3.277</td><td>3.333</td><td>0.300</td><td>1.611</td></tr>
<tr><td>Cellulose -CN</td><td>0.819</td><td>-6.642</td><td>6.642</td><td>-0.819</td><td>-2.911</td><td>3.731</td><td>0.268</td><td>1.136</td></tr>
<tr><td>Cellulose -SH</td><td>-0.524</td><td>-6.492</td><td>6.492</td><td>0.524</td><td>-3.508</td><td>2.984</td><td>0.335</td><td>2.063</td></tr>
<tr><td>Cellulose -GO</td><td>-4.076</td><td>-4.244</td><td>4.244</td><td>4.076</td><td>-4.156</td><td>0.084</td><td>11.855</td><td>102.575</td></tr>
</tbody>
</table>

Table 3. The global reactivity descriptors for functionalized cellulose and cellulose/GO.

![](./images/1063669143951114247_4.jpg)

Figure 4. The density of states (DOS): (a) Cellulose, (b) Cellulose-OH, (c) Cellulose-NH 2 , (d) Cellulose-COOH, (e) Cellulose-CH 3 , (f) Cellulose-CHO, (g) Cellulose-CN, (h) Cellulose-SH, and (i) Cellulose-GO.

between the highest occupied molecular orbital (HOMO) and the lowest unoccupied molecular orbital (LUMO) is commonly referred to as the band gap. In the DOS spectrum, this corresponds to the energy range where no electronic states are present between the highest peak of the green lines and the lowest peak of the red lines. The size of this gap is significant for determining electrical conductivity and other electronic properties, as it defines the ease with which electrons can be excited from the HOMO to the LUMO.

Upon functionalizing cellulose with various groups and GO, the DOS spectrum reveals additional peaks, indicating new energy levels that arise from these modifications. In particular, Fig. 4h and i show states that appear close to the Fermi level. These states correspond to virtual, unoccupied states introduced by the functionalization process. Their proximity to the Fermi level suggests a reduction in the effective band gap, which can enhance the material's electrical conductivity by allowing electrons to be more readily excited. This alteration of electronic properties due to functionalization is a key aspect for the potential use of functionalized cellulose in electronic applications. The DOS spectrum also reveals a clear band gap in most cases, indicating a semiconducting behavior. However, the additional virtual states created by the functional groups and GO suggest increased electronic interactions, which may enhance the material's conductivity and reactivity. This information is valuable for designing cellulose-based materials with tailored electronic properties for various technological applications.

Figure 5 illustrates the Projected Density of States (PDOS) for cellulose and its various functionalized forms. The PDOS analysis helps in understanding the contribution of different atoms or functional groups to the electronic states of the material. Each subfigure (a to i) represents a different functionalization of cellulose, where the blue Line represents the PDOS contributed by oxygen atoms, the green line represents the PDOS contributed by carbon atoms, red line represents the PDOS contributed by hydrogen atoms, cyan sticks indicate the occupied orbitals and the magenta sticks indicate the virtual (unoccupied) orbitals. The PDOS for pure cellulose shows the distribution of electronic states contributed by its constituent atoms. Peaks in the DOS spectrum represent energy levels where a significant number of electronic states are available. The band gap can be observed as the energy range between the highest occupied and the lowest unoccupied states. Functionalization with hydroxyl groups (OH) shifts the electronic states. The presence of OH groups influences the distribution of states, particularly near the Fermi level, which might affect the band gap and reactivity. Amino groups ($\text{NH}_2$) also modify the PDOS. These changes can be seen in the new peaks or shifts in existing peaks, indicating the alteration of electronic states due to $\text{NH}_2$ groups. Carboxyl groups (COOH) introduce new states or modify existing ones. The PDOS indicates how COOH groups impact the overall electronic structure, potentially affecting properties like solubility and reactivity. Methyl groups ($\text{CH}_3$) show their influence on the PDOS by altering the distribution of states. These changes can provide insight into how $\text{CH}_3$ functionalization affects the electronic properties of cellulose. Aldehyde groups (CHO) shift the electronic states significantly. The PDOS for Cellulose-CHO can reveal how these groups impact the material's reactivity and band gap. The influence of CN and thiol groups can also be crucial for understanding changes in electronic properties and potential applications. Graphene oxide (GO) significantly alters the PDOS of cellulose. The integration of GO introduces new states and shifts existing ones, which can drastically change the electronic properties, making Cellulose-GO composites suitable for various advanced applications.

### IR spectrum of cellulose and its various functionalized forms
The infrared (IR) frequencies, which provide distinctive fingerprint information, have played a significant role in various chemistry fields. Consequently, the IR frequencies of cellulose were computed using HF and DFT: B3LYP methods with basis sets including 3-21 g, 6-31 g, 6-311 g, LANL2DZ, and LANL2MB, and then compared to experimental IR data. Tables 4 and 5 compare the theoretical IR frequencies of cellulose obtained from HF and DFT: B3LYP calculations with the experimental data using the mentioned basis sets. The theoretical IR data from Table 4 were utilized after each basis set was adjusted. Table 4 highlights the main characteristics of pure cellulose FTIR bands, such as the broad O-H stretching bands at $3345\ \text{cm}^{-1}$ and C-H stretching bands around $2900\ \text{cm}^{-1}$. Additionally, C-H and C-O vibrations were assigned to bands at 1430 and $1640\ \text{cm}^{-1}$, respectively. The region around $1370-1340\ \text{cm}^{-1}$ was associated with the $\text{CH}_3$ umbrella mode, while the absorption bands for C-CH and C-CO of the cellulose polymer appeared at 1280 and $1320\ \text{cm}^{-1}$. The C-O-C vibration was allocated to the band at $1160-1030\ \text{cm}^{-1}$, and the bands for C-H and $\text{CH}_2$ appeared at 895 and $615\ \text{cm}^{-1}$, respectively$^{54}$. A comparison of the data in Tables 4 and 5 revealed that DFT: B3LYP/3-21 g yielded the closest values to the experimental data. Consequently, IR frequencies obtained using the 3-21 g** basis set were compared with those obtained using the 3-21 g basis set for improved accuracy. However, several vibrational modes obtained using DFT: B3LYP/3-21 g** were found to be in line with the experimental data, suggesting the suitability of using DFT: B3LYP/3-21 g**$^{55}$ to examine cellulose functionalized by various functional groups and GO in close proximity to experimental results.

Experimental FTIR spectroscopy of cellulose-GO film is depicted in Fig. 6 and outlined in Table 6. The characteristic bands of cellulose encompass a broadband predicted at $3325\ \text{cm}^{-1}$, attributed to the OH groups of both cellulose and GO. Upon the synthesis of cellulose/GO composite via the OH group of $\text{CH}_2\text{OH}$, a new band representing the GO (COOH) group emerged at $1710\ \text{cm}^{-1}$. The interaction between cellulose and GO through the $\text{CH}_2\text{OH}$ group caused a shift of the entire cellulose band to a lower wavenumber. It has been previously established that IR absorption occurs due to the interaction between the IR electric field vector and the molecular dipole transition moments, which are associated with molecular vibrations. Absorption is maximized when the electric field vector and the dipole transition moment are parallel$^{56}$. Applying this principle to the experimental FTIR spectra, variations in the IR-absorbance intensity, particularly in C-O at $1620\ \text{cm}^{-1}$as Bronsted acid as previously discussed, are evident$^{57}$. These variations are expected to be more pronounced in cellulose without graphene, in correlation with the dipole moment values obtained from modeling, as shown in Table 2.

### Conclusions
In conclusion, this study examined the functionalization of cellulose with various functional groups and graphene oxide (GO) to enhance its properties for diverse applications. Through computational modeling and experimental analyses, we investigated the vibrational spectra, electronic properties, and reactivity of cellulose

![](./images/1063669143951114247_5.jpg)

Figure 5. The projected density of states (PDOS): (a) Cellulose, (b) Cellulose-OH, (c) Cellulose-NH2, (d) Cellulose-COOH, (e) Cellulose-CH3, (f) Cellulose-CHO, (g) Cellulose-CN, (h) Cellulose-SH, and (i) Cellulose-GO.

<table>
 <thead>
  <tr>
   <th>Exp.</th>
   <th>3–21 g</th>
   <th>6–31 g</th>
   <th>6–311 g</th>
   <th>LANL2DZ</th>
   <th>LANL2MB</th>
   <th>Assignment</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>615</td>
   <td>633</td>
   <td>633</td>
   <td>630</td>
   <td>631</td>
   <td>607</td>
   <td>CH₂</td>
  </tr>
  <tr>
   <td>895</td>
   <td>872</td>
   <td>874</td>
   <td>877</td>
   <td>867</td>
   <td>931</td>
   <td>C-H</td>
  </tr>
  <tr>
   <td>1160 ~ 1030</td>
   <td>1167-1031</td>
   <td>1175-1042</td>
   <td>1178-1046</td>
   <td>1168-1035</td>
   <td>1263-1138</td>
   <td>C-O-C</td>
  </tr>
  <tr>
   <td>1280</td>
   <td>1276</td>
   <td>1279</td>
   <td>1282</td>
   <td>1269</td>
   <td>1373</td>
   <td>C-CO</td>
  </tr>
  <tr>
   <td>1320</td>
   <td>1324</td>
   <td>1328</td>
   <td>1334</td>
   <td>1318</td>
   <td>1438</td>
   <td>C-CH</td>
  </tr>
  <tr>
   <td>1370 ~ 1340</td>
   <td>1377-1345</td>
   <td>1381-1346</td>
   <td>1383-1350</td>
   <td>1373-1335</td>
   <td>1494-1456</td>
   <td>Split CH₃ umbrella mode</td>
  </tr>
  <tr>
   <td>1430</td>
   <td>1430</td>
   <td>1436</td>
   <td>1432</td>
   <td>1428</td>
   <td>1586</td>
   <td>C-H</td>
  </tr>
  <tr>
   <td>1640</td>
   <td>-</td>
   <td>-</td>
   <td>-</td>
   <td>-</td>
   <td>-</td>
   <td>C-O</td>
  </tr>
  <tr>
   <td>2900</td>
   <td>2990</td>
   <td>2941</td>
   <td>2945</td>
   <td>2960</td>
   <td>3166</td>
   <td>CH Sym. Str.</td>
  </tr>
  <tr>
   <td>3345</td>
   <td>3342</td>
   <td>3512</td>
   <td>3563</td>
   <td>3537</td>
   <td>3800</td>
   <td>O-H Stretching</td>
  </tr>
 </tbody>
</table>

Table 4. HF calculated IR of cellulose (scaled) calculated using different basis sets including 3–21 g, 6–31 g, 6–311 g, LANL2DZ, and LANL2MB compared with cellulose IR experimental result.

<table>
 <thead>
  <tr>
   <th>Exp.</th>
   <th>3–21 g</th>
   <th>6–31 g</th>
   <th>6–311 g</th>
   <th>LANL2DZ</th>
   <th>LANL2MB</th>
   <th>3–21 g**</th>
   <th>Assignments</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>615</td>
   <td>637</td>
   <td>629</td>
   <td>629</td>
   <td>611</td>
   <td>611</td>
   <td>635</td>
   <td>CH₂</td>
  </tr>
  <tr>
   <td>895</td>
   <td>890</td>
   <td>716</td>
   <td>723</td>
   <td>850</td>
   <td>851</td>
   <td>849</td>
   <td>C-H</td>
  </tr>
  <tr>
   <td>1160 ~ 1030</td>
   <td>1122-1029</td>
   <td>1132-1029</td>
   <td>1131-1028</td>
   <td>1167-1092</td>
   <td>1167-1092</td>
   <td>1117-1022</td>
   <td>C-O-C</td>
  </tr>
  <tr>
   <td>1280</td>
   <td>1278</td>
   <td>1273</td>
   <td>1274</td>
   <td>1311</td>
   <td>1311</td>
   <td>1281</td>
   <td>C-CO</td>
  </tr>
  <tr>
   <td>1320</td>
   <td>1324</td>
   <td>1308</td>
   <td>1312</td>
   <td>1375</td>
   <td>1375</td>
   <td>1320</td>
   <td>C-CH</td>
  </tr>
  <tr>
   <td>1370 ~ 1340</td>
   <td>1374-1343</td>
   <td>1370-1339</td>
   <td>1371-1339</td>
   <td>1422-1396</td>
   <td>1422-1396</td>
   <td>1371-1339</td>
   <td>Split CH₃ umbrella mode</td>
  </tr>
  <tr>
   <td>1430</td>
   <td>1418</td>
   <td>1417</td>
   <td>1393</td>
   <td>1562</td>
   <td>1595</td>
   <td>1417</td>
   <td>C-H</td>
  </tr>
  <tr>
   <td>1640</td>
   <td>-</td>
   <td>-</td>
   <td>-</td>
   <td>-</td>
   <td>-</td>
   <td>-</td>
   <td>C-O</td>
  </tr>
  <tr>
   <td>2900</td>
   <td>2943</td>
   <td>2956</td>
   <td>2934</td>
   <td>3105</td>
   <td>3105</td>
   <td>3021</td>
   <td>CH Sym-stretching</td>
  </tr>
  <tr>
   <td>3345</td>
   <td>3388</td>
   <td>3503</td>
   <td>3551</td>
   <td>3537</td>
   <td>3537</td>
   <td>3619</td>
   <td>O-H Stretch</td>
  </tr>
 </tbody>
</table>

Table 5. DFT: B3LYP calculated IR of cellulose (scaled) calculated using different basis sets including 3–21 g, 6–31 g, 6–311 g, LANL2DZ, LANL2MB, and 3–21 g** compared with cellulose IR experimental result.

![](./images/1063669143951114247_6.jpg)

Figure 6. FTIR Transmittance spectra of cellulose and cellulose-GO.

and its functionalized derivatives. Our findings indicate that DFT: B3LYP/3–21 g** emerged as the optimal method for predicting the vibrational frequencies of cellulose, while functionalization with GO at the terminal position exhibited the most favorable binding energy and stability. The DOS and PDOS analysis provides detailed insights into how different functional groups affect the electronic structure of cellulose. By comparing the DOS and PDOS of pure and functionalized cellulose, one can understand the influence of each functional

<table><thead><tr><th>Cellulose-GO</th><th>Assignments</th></tr></thead><tbody><tr><td>605</td><td>CH₂</td></tr><tr><td>875</td><td>C-H</td></tr><tr><td>1140~1010</td><td>C-O-C</td></tr><tr><td>1280</td><td>C-CO</td></tr><tr><td>1306</td><td>C-CH</td></tr><tr><td>1350~1320</td><td>Split CH₃ umbrella mode</td></tr><tr><td>1410</td><td>C-H</td></tr><tr><td>1620</td><td>C-O</td></tr><tr><td>1710</td><td>COOH of GO</td></tr><tr><td>2880</td><td>CH Sym. Str.</td></tr><tr><td>3325</td><td>O-H Stretching</td></tr></tbody></table>

Table 6. Band assignment of FTIR result of cellulose and Cellulose-GO.

group on the material's electronic properties. Furthermore, the study examined the interaction between cellulose and GO via the $CH_{2}OH$ group, revealing a notable shift in the cellulose band to a lower wavenumber. This observation aligns with theoretical principles regarding IR absorption and molecular dipole moments, as elucidated in our discussion. The experimental FTIR spectra further highlighted variations in IR-absorbance intensity, particularly in the C-O region at $1620\ cm^{-1}$, confirming the impact of functionalization on cellulose's structural characteristics. In fact, this study provides a comprehensive investigation into the electronic properties and stability of cellulose and its functionalized derivatives, particularly in the context of their applications in advanced materials and nanocomposites. Understanding the electronic characteristics, such as binding energy, chemical reactivity, and density of states, is crucial for the development of cellulose-based materials in fields like flexible electronics, sensors, and bioengineering. By elucidating these properties, our work aims to contribute valuable insights into the design and optimization of cellulose derivatives for enhanced performance in various technological applications.

## Data availability
The data that support the findings of this study are available from the corresponding author upon reasonable request.

Received: 2 July 2024; Accepted: 23 October 2024
Published online: 12 November 2024

## References
1. Williams, M. & Teplyakov, A. *Chemical functionalization of surfaces: preparation for secondary chemical modification*. (2018).
2. Varanasi V, Velten M, Odatsu T, Ilyas A, Iqbal S, Aswath P. in *Materials for Bone Disorders*. 405-452 (Elsevier, 2017).
3. Vesel, A. & Mozetic, M. New developments in surface functionalization of polymers using controlled plasma treatments. *J. Phys. D: Appl. Phys.* 50, 293001 (2017).
4. Li, X., Wang, X., Zhang, L., Lee, S. & Dai, H. Chemically derived, ultrasmooth graphene nanoribbon semiconductors. *Science*. 319, 1229-1232. https://doi.org/10.1126/science.1150878 (2008).
5. Susilorini, R. M. R. et al. The advantage of natural polymer modified mortar with seaweed: green construction material innovation for sustainable concrete. *Procedia Eng.* 95, 419-425 (2014).
6. Tanış, E. New optoelectronic material based on biguanide for orange and yellow organic light emitting diode: a combined experimental and theoretical study. *J. Mol. Liq.* 358, 119161 (2022).
7. Tanış, E. Optical and photonic properties dependence on HNMB solvents: An emitter molecule for OLEDs. *Optik*. 252, 168576 (2022).
8. Yadav, H. & Karthikeyan, C. *In Polysaccharide Carriers for drug Delivery 1-17* (Elsevier, 2019). Woodhead Publishing, Sawston, Cambridge UK
9. Abdullah, N. A. et al. Nanocellulose from agricultural waste as an emerging nanotechnology material for nanotechnology applications-an overview. *Polimery*. 66 (3), 155-214 (2021).
10. Akatwijuka, O., Gepreel, M.AH., Abdel-Mawgood, A. et al. Overview of banana cellulosic fibers: agro-biomass potential, fiber extraction, properties, and sustainable applications. *Biomass Conv. Bioref.* 14, 7449-7465 (2024).
11. Mathew, A., Poulose, A., Gopakumar, D. A., Pasquini, D., Grohens, Y., & George, J. J. Nanocellulose-Based Ultralight Porous Material for Various Environmental Applications. *Nanomaterials for Airand Water Purification*. 1, 373-397 (2024).
12. Nadeem, H., Athar, M., Dehghani, M., Garnier, G. & Batchelor, W. Recent advancements, trends, fundamental challenges and opportunities in spray deposited cellulose nanofibril films for packaging applications. *Sci. Total Environ.* 836, 155654. https://doi. org/10.1016/j.scitotenv.2022.155654 (2022).
13. Luo, Q., Shen, H., Zhou, G. & Xu, X. A mini-review on the dielectric properties of cellulose and nanocellulose-based materials as electronic components. *Carbohydr. Polym.* 303, 120449 (2023).
14. Mawardi, I. et al. Eco-friendly production and performance evaluation of water-resistant cellulose nanofiber bioaerogels. *Polym. Eng. Sci.* 64, 733-748 (2024).
15. Pourmadadi, Mehrab, et al. Novel carboxymethyl cellulosebased nanocomposite: A promising biomaterial for biomedical applications. *ProcessBiochem.* 130, 211-226 (2023).
16. Dufresne, A. Preparation and applications of cellulose nanomaterials. *Chem. Afr.* 6, 2219-2236 (2023).
17. Khan, A., Alamry, K. A., Oves, M. & Althomali, R. H. A facile and green approach for the fabrication of nano-biocomposites by reducing silver salt solution into silver nanoparticles using modified carboxymethyl cellulose for antimicrobial potential. *J. Polym. Res.* 28, 1-13 (2021).

18. Yusuf, M. Cellulose-based nanomaterials for water pollutantremediation. *Handbook of nanomaterials and nanocomposites for energyand environmental applications*. 213-228, (2021).

19. Singha, A. Kumar Thakur, V. Saccharum cilliare fiber reinforced polymer composites. *J. Chem. 5*, 782-791 (2008).

20. Yaqoob, A. A. et al. Cellulose Derived Graphene/Polyaniline Nanocomposite Anode for Energy Generation and Bioremediation of toxic metals via Benthic Microbial fuel cells. *Polym. (Basel). 13*, 135. https://doi.org/10.3390/polym13010135 (2020).

21. Zhang, L., Yu, Y., Zheng, S., Zhong, L. & Xue, J. Preparation and properties of conductive bacterial cellulose-based graphene oxide-silver nanoparticles antibacterial dressing. *Carbohydr. Polym. 257*, 117671. https://doi.org/10.1016/j.carbpol.2021.117671 (2021).

22. Pinto, S. C. et al. Bacterial cellulose/graphene oxide aerogels with enhanced dimensional and thermal stability. *Carbohydr. Polym. 230*, 115598. https://doi.org/10.1016/j.carbpol.2019.115598 (2020).

23. Wu, Y. et al. Enhanced ion transport by graphene oxide/cellulose nanofibers assembled membranes for high-performance osmotic energy harvesting. *Mater. Horiz. 7*, 2702-2709 (2020).

24. Ahmed, A., Adak, B., Bansala, T. & Mukhopadhyay, S. Green Solvent Processed Cellulose/Graphene Oxide Nanocomposite Films with Superior Mechanical, Thermal, and Ultraviolet Shielding properties. *ACS Appl. Mater. Interfaces. 12*, 1687-1697. https://doi.org/10.1021/acsami.9b19686 (2020).

25. Yu, H., Hong, H. J., Kim, S. M., Ko, H. C. & Jeong, H. S. Mechanically enhanced graphene oxide/carboxymethyl cellulose nanofibril composite fiber as a scalable adsorbent for heavy metal removal. *Carbohydr. Polym. 240*, 116348 (2020).

26. Maaza, L., Djafri, F., Belmokhtar, A. & Benyoucef, A. Evaluation of the influence of Al2O3 nanoparticles on the thermal stability and optical and electrochemical properties of PANI-derived matrix reinforced conducting polymer composites. *J. Phys. Chem. Solids. 152*, 109970 (2021).

27. Hammadi, F., Belardja, M., Lafjah, M. & Benyoucef, A. Studies of influence of ZrO2 nanoparticles on reinforced conducting polymer and their optical, thermal and electrochemical properties. *J. Inorg. Organomet. Polym. Mater. 31*, 1176-1184 (2021).

28. Nair, R. R. et al. Fine structure constant defines visual transparency of graphene. *Science. 320*, 1308. https://doi.org/10.1126/science.1156965 (2008).

29. Hawick, K., Grove, D., Coddington, P. & Buntine, M. Commodity cluster computing for computational chemistry. *Internet J. Chem. 3*, 1099-8292 (2000).

30. Omar, A. et al. Investigation of morphological, structural and electronic transformation of PVDF and ZnO/rGO/PVDF hybrid membranes. *Opt. Quantum Electron. 55*, 381 (2023).

31. El-Mansy, M. A., Bayoumy, A. M., Elhaes, H. & Ibrahim, M. A. Exploring the electronic, optical, and bioactive properties for new modified fullerenes via molecular modeling. *Opt. Quantum Electron. 55*, 100 (2023).

32. Scuseria, G. E. Comparison of coupled-cluster results with a hybrid of hartree-Fock and density functional theory. *J. Chem. Phys. 97*, 7528-7530 (1992).

33. Brandenburg, J. G., Grimme, S. Dispersion correctedHartree-Fock and density functional theory for organic crystal structureprediction. *Prediction and Calculation of Crystal Structures: Top Curr Chem. 345*, 1-23 (2014).

34. Tanış, E. A study of silicon and germanium-based molecules in terms of solar cell devices performance. *Turk. J. Chem. 46*, 1607-1619 (2022).

35. Issaoui, N., Ghalla, H., Muthu, S., Flakus, H. & Oujia, B. Molecular structure, vibrational spectra, AIM, HOMO-LUMO, NBO, UV, first order hyperpolarizability, analysis of 3-thiophenecarboxylic acid monomer and dimer by Hartree-Fock and density functional theory. *Spectrochim Acta Mol. Biomol. Spectrosc. 136*, 1227-1242 (2015).

36. Zunger, A., Bridging the gap between density functionaltheory and quantum materials. *Nat. Comput. Sci. 2*, 529-532 (2022).

37. Hummers Jr, W. S., & Offeman, R. E. Preparation ofgraphitic oxide. *JACS. 80*, 1339-1339 (1958).

38. Lieb, E. H., Simon, B. The Hartree-Fock theoryfor coulomb systems. *Commun. Math. Phys. 53*, 185-194 (1977).

39. Raghavachari, K. Perspective on Density functional thermochemistry. III. The role of exact exchange Becke AD (1993) J Chem Phys 98: 5648-52. *Theor. Chem. Acc. 103*, 361-363 (2000).

40. Lee, C., Yang, W. & Parr, R. G. Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density. *Phys. Rev. B Condens. Matter. 37*, 785 (1988).

41. Vosko, S. H., Wilk, L., & Nusair, M. Accuratespin-dependent electron liquid correlation energies for local spin densitycalculations: a critical analysis. *Can. J. Phys. 58*, 1200-1211 (1980).

42. Frisch, M. J. I. & Wallingford, C. T. *gaussian 09, Revision d. 01, Gaussian. 201* (2009).

43. Anisimov, Y. A., Evitts, R. W., Cree, D. E. & Wilson, L. D. Polyaniline/Biopolymer Composite Systems for Humidity Sensor Applications: a review. *Polym. (Basel). 13*, 2722. https://doi.org/10.3390/polym13162722 (2021).

44. Elhaes, H., Morsy, M., Yahia, I. S., Ibrahim, M. Molecularmodeling analyses for electronic properties of CNT/TiO 2 nanocomposites. *Opt.Quantum Electron. 53*, 1-13 (2021).

45. Kubba, R. M., Mohammed, M. A. & Ahamed, L. D. F. T. Calculations and experimental study to Inhibit Carbon Steel Corrosion in saline solution by Quinoline-2-One Derivative. *Carbon Steel Corros. 18*, 0113-0113 (2021).

46. Abdelsalam, M.M., Bedair, M.A., Hassan, A.M., Heakal, B.H., Younis, A., Elbialy, Z.I., Badawy, M.A., Fawzy, H.E.D. and Fareed, S.A., Greensynthesis, electrochemical, and DFT studies on the corrosion inhibition ofsteel by some novel triazole Schiff base derivatives in hydrochloric acidsolution. *Arab. J. Chem. 15*, 103491 (2022).

47. Tavakol, H. Study of binding energies using DFT methods, vibrational frequencies and solvent effects in the interaction of silver ions with uracil tautomers. *Arab. J. Chem. 10*, S786-S799 (2017).

48. Sagadevan, S. et al. Functionalized graphene-based nanocomposites for smart optoelectronic applications. *Nanotechnol Rev. 10*, 605-635 (2021).

49. Al-Fifi, Z., Eid, M., Saleh, N. A. & Ibrahim, M. Molecular modelling analyses of the substituted 3'-Azido-2', 3' dideoxythymidine. *J. Comput. Theor. Nanosci. 11*, 409-412 (2014).

50. Brakat, A. & Zhu, H. Nanocellulose-graphene hybrids: Advanced functional materials as multifunctional sensing platform. *Nanomicro Lett. 113*, 1-37 (2022).

51. Ezzat, H. A., Hegazy, M. A., Nada, N. A., Osman, O. & Ibrahim, M. A. Development of natural polymer/metal oxide nanocomposite reinforced with graphene oxide for optoelectronic applications. *NRIAG J. Astron. Geophys. 10*, 10-22 (2021).

52. Politzer, P., Laurence, P. R. & Jayasuriya, K. Molecular electrostatic potentials: an effective tool for the elucidation of biochemical phenomena. *Environ. Health Perspect. 61*, 191-202. https://doi.org/10.1289/ehp.8561191 (1985).

53. Al-Amiery, A. et al. Quantum chemical elucidation on corrosion inhibition efficiency of Schiff base: DFT investigations supported by weight loss and SEM techniques. *Int. J. Low-Carbon Technol. 15*, 202-209 (2020).

54. Zhang, L. et al. Micro-FTIR combined with curve fitting method to study cellulose crystallinity of developing cotton fibers. *Anal. Bioanal Chem. 413*, 1313-1320. https://doi.org/10.1007/s00216-020-03094-6 (2021).

55. Alghunaim, N. S. Effect of hydration on the electronicproperties of Si/PANI/3ZnO nanocomposite. *J. Inorg. Organomet. Polym. Mater. 30*, 451-456 (2020).

56. Narasimhan, B. Spectroscopy of Polymers-edited by Jack L. Koenig, Elsevier, New York, NY, 491 pages. *J. Control. Release. 3*, 389 (2002). (1999).

57. He, C. et al. Understanding the promotional effect of Mn2O3 on micro-/mesoporous hybrid silica nanocubic-supported pt catalysts for the low-temperature destruction of methyl ethyl ketone: an experimental and theoretical study. *ACS Catal. 8*, 4213-4229 (2018).


### Acknowledgements
This work is conducted during the sixth spectroscopy winter school SWS-06 at National Research Centre, Dokki, Egypt (03 February to 27 March 2024).

### Author contributions
All authors have equally participated in work, writing and discussion of this manuscript.

### Funding
Open access funding provided by The Science, Technology & Innovation Funding Authority (STDF) in cooperation with The Egyptian Knowledge Bank (EKB).

### Declarations

#### Competing interests
The authors declare no competing interests.

#### Additional information
Correspondence and requests for materials should be addressed to M.A.I.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024