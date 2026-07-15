# Revealing the Charge Storage Mechanism of Nickel Oxide Electrochromic Supercapacitor

Zhihui Luo, Lei Liu, Xiaoyong Yang, Xuan Luo, Peng Bi, Zhenjin Fu, Aimin Pang, Wei Li, and Yong Yi

ACS Appl. Mater. Interfaces, Just Accepted Manuscript • DOI: 10.1021/acsami.0c09606 • Publication Date (Web): 03 Aug 2020
Downloaded from pubs.acs.org on August 3, 2020

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W.,
Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# Revealing the Charge Storage Mechanism of Nickel Oxide Electrochromic Supercapacitor

Zhihui Luo¹, Lei Liu²*, Xiaoyong Yang¹·³, Xuan Luo⁴, Peng Bi⁵, Zhenjin Fu¹, Aimin Pang⁶, Wei Li⁶ and Yong Yi¹*.

¹ State Key Laboratory for Environment-friendly Energy Materials, Southwest University of Science and Technology, Mianyang 621010, China.

² School of Physics, Beihang University, Beijing 100191, China.

³ Condensed Matter Theory Group, Materials Theory Division, Department of Physics and Astronomy, Uppsala University, Box 516, 75120

⁴ Research Center of Laser Fusion, China Academy of Engineering Physics, Mianyang 621900.

$^{5}$ School of Science, Southwest University of Science and Technology, Mianyang 621010, China.

$^{6}$ Science and Technology on Aerospace Chemical Power Laboratory, Hubei Institute of Aerospace Chemotechnology, Xiangyang, 441003, Hubei, China

Keywords: electrochromic supercapacitor, transition metal oxides, first-principle calculation, reaction kinetic analysis, charge storage mechanism.

Abstract: Nickel oxide (NiO) is considered one of the most promising positive anode materials for electrochromic supercapacitors. Nevertheless, a detailed mechanism of the electrochromic and energy storage process has yet to be unraveled. In this research, the charge storage mechanism of a NiO electrochromic electrode was investigated by combining the in-depth experimental and theoretical analyses. Experimentally, a kinetic analysis of the Li-ions behavior based on the cyclic

voltammetry curves reveals the major contribution of surface capacitance versus total capacity, providing fast reaction kinetics and highly reversible electrochromic performance. Theoretically, our model uncovers that Li-ions prefer to adsorb at fcc sites on the NiO (111) surface then diffuse horizontally over the plane and finally migrate in the bulk. More significantly, the calculated theoretical surface capacity (106 mAh g⁻¹) accounts for about 77.4 % of the total experimental capacity (137 mAh g⁻¹), indicating that the surface storage process dominates the whole charge storage, which is in accordance with the experimental results. This work provides a fundamental understanding of transition metal oxides for applications in electrochromic supercapacitors, and can also promote the exploration of novel electrode materials for high-performance electrochromic supercapacitors.

### 1. Introduction
Supercapacitors (SCs) have been widely applied in digital communications, portable electronics and electric vehicles thanks to their rapid charging/discharging rate, superior rate capability, high power density, long-term stability and safe operation.¹⁻³ Recently, in

order to meet the demand of intelligent electronics and extend their application range, supercapacitors with diverse functionalities and novel features have captured tremendous attention. Electrochromism refers to the reversible color change of some materials under electrochemical redox reactions induced by an applied external voltage.⁴ Electrochromic materials, capable of storing/releasing ions and electrons during charging/discharging have been previously demonstrated to show supercapacitor characteristics. Incorporating electrochromic materials into supercapacitors could provide connectivity and deliver relevant information to realize intelligent electrochromic energy storage devices, which might represent a promising trend in science and technology.⁵⁻⁶ Electrochromic supercapacitors (ESCs) that integrate electrochromic capability and energy storage performance into one platform are highly attractive, because they can function as a normal supercapacitor for energy storage and also monitors the stored energy level in a predictable and noticeable manner.⁷⁻¹⁰

To date, transition metal oxides, Prussian blue and conducting polymers have been widely investigated as individual electrodes for electrochromic supercapacitors.¹¹⁻¹² Among them, nickel oxide (NiO) is one of the most widely studied positive

electrochromic materials owing to its superior electrochromic performance and reversible energy storage capability.¹³⁻¹⁴ Previous reports about NiO electrochromic supercapacitors mainly focused on synthesizing nanostructure/nanoparticles or developing novel methods/configurations to improve its basic properties (such as optical modulation, switching time, coloration efficiency, capacity, cycling stability, *ect.*). For example, Cai *et al.* prepared uniform NiO nanoparticles by a solvothermal method, the resultant films possessed high capacitance, excellent rate capability, a large optical modulation, high coloration efficiency and good cycling stability when they were used in electrochromic supercapacitor application.¹⁵ Dong *et al.* fabricated NiO/Ag/NiO (NAN) electrodes by electron-beam deposition method, the NAN film also exhibited large optical modulation, fast response time, high specific capacitance and great long-term cycling stability, which even could compare with nanostructured NiO films.¹⁶ However, a comprehensive and systematic research on the electrochromic and energy storage mechanism of the NiO electrode is still lacking. To the best of our knowledge, the cause of the electrochromism remains unsettled despite scientific research on NiO electrochromic materials that has persisted for nearly 30 years, and not only is the

energy storage mechanism poorly understood, but even the ionic kinetic absorption-diffusion behavior involved in the electrochemical process is sometimes ambiguous.

These uncertainties are particularly noteworthy when $Li^+$-based electrolytes are used during the electrochromic process. Passerini *et al.* initiated researches about the electrochromic behaviors of NiO that cycled in Li-ion electrolytes and proposed a simple two-step electrochemical reaction.¹⁷ They presumed that an activated procedure occurred in the initial cycling of the NiO electrode, whereas there are no reports referring to the specific description of the activation process. In addition, the initial irreversible activation process requires the application of very low potentials, resulting in many reactions occurring at the electrode/electrolyte interfaces, as well as Li-based oxides and hydroxides forming at the electrode surface.¹⁸⁻¹⁹ Furthermore, once relatively excessive potential is applied to the NiO electrode during electrochemical testing, multiple coupled peaks will emerge in the cyclic voltammetry (CV) curves.

Nevertheless, the statement of this phenomenon still lacks support from any unequivocal pieces of evidence. Considering the above-mentioned problems, the electrochromic process and energy storage mechanism of NiO electrodes in $Li^+$-based

electrolytes still have many controversies. To accurately demonstrate the electrochemical process and the energy storage mechanism of electrochromic NiO cycled in Li⁺-based electrolytes, the following questions must be addressed. What is the adsorption behavior of Li-ions in the electrolyte after migration to the electrolyte/electrode interface (which crystal plane or active site will be resided by Li-ions)? Where does the redox reaction involved in the electrochromic process occur? How do the adsorbed Li-ions diffuse into the subsurface and inside of the material?

Unfortunately, thus far, barely detailed and effective work at the atomic level has been carried out to answer these questions and reveal the energy storage mechanism of NiO electrochromic electrodes. Therefore, a comprehensive and further study at the atomic level is urgently needed to elucidate the charge storage mechanism of NiO electrochromic supercapacitor electrodes.

Herein, the electrochromic behavior and charge storage mechanism of the NiO electrode when cycled in the Li⁺-based electrolyte (LiClO₄-PC) were systematically investigated by combining experimental results and first-principle calculations. Electrochemical measurements and optical transmittance spectra were performed to

study the electrochemical behavior and electrochromic properties of the NiO electrodes.

The kinetic behavior of Li-ions was analyzed to qualitatively reveal the contribution of surface capacitance and diffusion-related processes versus the total capacity. Li-ion adsorption and diffusion at the electrode interface/subsurface in various sites were investigated to reveal the charge storage mechanism at the microscale. The charge transfer and distribution of the NiO (1 1 1) surface during the electrochemical process were calculated using Bader electron valence charge analysis. Moreover, the average intercalation potential, theoretical capacity, and electronic structure analysis were calculated to evaluate the properties of the NiO electrode as a positive electrochromic material for SCs. Based on the electronic structure analysis, a surface pseudocapacitive Li-ion storage mechanism is proposed. Through detailed research on the Li-ion adsorption and diffusion processes, a discharge process model of the electrode at the micro-scale level is proposed, which can be well matched with the experimentally measured discharge curve of the NiO electrode.

## 2. Experimental

### 2.1 Preparation of NiO Electrochromic Supercapacitor

NiO thin films were deposited on indium tin oxide (ITO) coated glasses substrates by direct-current (DC) reactive magnetron sputtering. The substrates were cleaned ultrasonically in industrial alcohol and deionized water in sequence for 30 min and then dried in air. Before deposition, the base pressure of the vacuum chamber was pumped lower than $5×10^{-4}$ Pa, and the pure metallic nickel target (99.99%) was pre-sputtered for 5 minutes to clean the contaminants on the surface. During sputtering, the pure Ar (99.99%) and $O_2$ (99.99%) at a ratio of 9:1 were introduced into the chamber as sputtering gas through mass flow controller. The work pressure was fixed at 1.5 Pa and the DC power was 225 W during the deposition process. There were no substrate bias and no substrate heating (without taking into account the heating of the substrate by the plasma). The distance from the substrate to the target was fixed at 15cm, and the substrates were kept rotating at a constant speed at about $54^o$ per second to guarantee the homogeneity of the films.

### 2.2 Characterization Method

Grazing incidence X-ray diffraction (GIXRD, M189XHF-SRA, Mac Science) with Cu-Ka radiation ($\lambda$=1.5405 Å) was applied for the characterization of the crystallographic structure of the thin films at a constant glancing incidence angle of 0.5°. Scanning electron microscope (SEM, FEI-Phillips XL30 S-FEG) and TEM (JEOL-2100) were employed to investigate the morphology and structure of the as-deposited sample films.

The chemical composition for thin films was analyzed by X-ray photoelectron spectrum (XPS). Cyclic voltammetry (CV), chronoamperometry (CA) and galvanostatic charge/discharge (GCD) were carried out on an electrochemical workstation (CS2350, CorrTest, Wuhan). The electrochemical measurements for as-prepared thin films were conducted in the conventional three-electrode configurations using 1 M $LiClO_4$-PC electrolyte with a platinum (Pt) foil counter electrode and an Ag/AgCl reference electrode. The spectrum transmittance was measured by UV-VIS spectrophotometer (PUXI, TU1901). Additionally, the *in-situ* optical transmittance at 550 nm was also recorded during the electrochemical process.

### 2.3 Computational Methods

All calculations were performed by the Vienna ab initio Simulation Package (VASP) based on density functional theory (DFT).²⁰⁻²¹ The projector-augmented-wave (PAW) was used, and the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation (GGA) was chosen for the exchange correlation functional.²²⁻²⁴ A plane-wave cutoff of 450 eV was used for the kinetic energy for all calculations. The convergence of electronic iterations and final force on each atom were $10^{-6}$ eV and 0.02 eV/Å, respectively. Besides, the magnetic (spin-polarized) calculation was considered to measure the magnetic moments for each atom.²⁵

In regards to the adsorption behavior of Li atoms on a clean NiO (111) surface at different sites, a 6-layer 3×3×1 supercell of NiO (111) plane was constructed with a 15 Å vacuum. The deep four bottom layers were fixed, while the first two layers were fully relaxed. The Monkhorst-Pack²⁶ scheme was set to 2×2×1 for structural optimization and 5×5×1 for the density of states (DOS). In order to elucidate the interactions between the adsorbed Li atom and NiO surface, van der Waals corrections were included using the

DFT-D3 method.²⁷⁻²⁸ The adsorption energy is evaluated according to the following
equation:

$$
E_{a d s}=E_{N i O / L i}-E_{N i O}-E_{L i} \tag{1}
$$

where $E_{NiO/Li}$, $E_{NiO}$ and $E_{Li}$ are the total energy of the slab model covered with Li
atoms, the isolated adsorbate NiO (111) plane and the total energy per atom for the
bulk Li, respectively. The topological Bader charge²⁹ method was applied to obtain the
amount of valence electrons around the atoms. The diffusion barrier energy was
computed by the climbing-image nudged elastic band (CI-NEB) method so as to
investigate the performance of the positive materials.

## 3. Results and Discussion

The X-ray diffraction (XRD) pattern of the as-deposited NiO film on ITO substrate is
demonstrated in Figure 1a. The diffraction peaks emanating from the (1 1 1), (2 0 0), (2
2 0), (3 1 1) and (2 2 2) planes are clear evidence for NiO with a face-centered cubic
structure (JCPDS No. 47-1049). Additionally, NiO has a strong peak corresponding to
the (1 1 1) lattice plane, implying that NiO shows a preferred (1 1 1) orientation.

Moreover, the morphology of the film was characterized by scanning electron microscopy (SEM), which revealed that the NiO crystalline grain exhibits column-like triangular shapes with an average diameter of 30-40 nm (Figure 1b). The cross-section SEM image reveals column-like triangles with a height of about 656 nm that are aligned vertically and adhered strongly to the ITO glass. Furthermore, the strong adhesion not only ensures the electron transport between the electrochromic layer and the transparent conductive layer but could also prevent the film from falling off the substrate. It is speculated that these column-like porous structures may exhibit a high surface area that enables active-site accessibility and facilitates effective insertion/extraction of $Li^+$ ions, which might endow the NiO electrode with excellent electrochemical performance. In addition, Figure S1 presents the $N_2$ adsorption-desorption isotherm of the NiO electrode. The typical type-IV curve with an obvious hysteresis loop between 0.4 and 1.0 ($P/P_0$) suggests the existence of mesopores among the triangular rods, and the pore diameters are mainly distributed at 20-30 nm based on the Barrett-Joyner-Halenda (BJH) model. Figure 1c displays a typical TEM image of the NiO film scrapped from the ITO glass, which confirms that the film is

composed of a sheet structure with dense small particles. The distinct rings of the selected area electron diffraction (SAED) pattern coincide to the (1 1 1), (2 0 0), (2 2 0) and (3 1 1) surfaces, further illustrating the polycrystalline feature of the NiO film, which agrees well with the XRD pattern.

As a promising electrode for electrochromic supercapacitors, the NiO film is eager to possess excellent electrochromic properties. The optical transmittance spectra of the NiO film between the colored and bleached states were measured in the wavelength range of 300-800 nm and are shown in **Figure 1d**. Under the action of external alternating potentials, the optical modulation between colored and bleached states was about 50% at a wavelength of 500 nm. The switching time from one state to the other under alternating potentials, which is a significant factor for electrochromic electrodes, is defined as the time required for the electrode to reach 90% of its full optical modulation.

**Figure 1e** presents the chronoamperometry curve and the corresponding *in-situ* transmittance curve at 550 nm for the NiO electrode. The coloring and bleaching times of the NiO electrode were found to be 4.2 and 2.6 s, respectively. The switching time was faster than previously reported materials, including NiO nanoparticles (11.5 s and

9.5 s)$^{15}$ and porous NiO nanosheet array films (9.1 s and 3.3 s)$^{30}$. The short switching time of the NiO electrode is possibly related to the fact that the nanoporous structure expands the contact surface area between the electrode and electrolyte, thus facilitating ions transmission. To evaluate the practicality of the NiO film as an electrochromic supercapacitor electrode, the charge/discharge curves at a current density of 1 A cm$^{-3}$ and the corresponding *in-situ* transmittance at 550 nm were recorded (Figure 1f).

Clearly, when charged to 1.1 V, the NiO film reached a fully charged state and its transparency decreased from 76.2% to 26.1%. During the charging process, when the electrical charge was completely consumed at a potential of 0 V, the color of the NiO electrode faded away and became transparent. The NiO film simultaneously exhibits energy storage and electrochromic functions, which is very useful for fabricating an energy storage device whose working state can be monitored with visual changes.

![](./images/812583435875909633_1.jpg)

Figure 1. Structurer and optical transmittance spectra of the NiO electrode. a) XRD pattern. b) SEM images. c) TEM image (inset: SAED pattern). d) Transmittance spectra and the digital photos at the bleached and colored states. e) Chronoamperometry curve and the corresponding in-situ transmittance curve at 550 nm. f) Galvanostatic charge-discharge curve and corresponding in-situ transmittance curve at 550nm.

The electrochemical performance of the as-deposited NiO electrode was measured with a three-electrode system containing $1\ \text{M}\ \text{LiClO}_4$-PC electrolyte with Pt foil as the counter electrode and a saturated Ag/AgCl electrode as the reference. Cyclic voltammetry (CV) curves at various scan rates and galvanostatic charge/discharge

(GCD) profiles at different current densities are presented in Figure 2a, b, respectively.

The Li-ion diffusion coefficient was calculated according to the Randles-Sevcik equation
of $i_{p}=2.69{\times}10^{5}n^{3/2}AD_{Li}^{1/2}C_{Li}v^{1/2}$, where $D_{Li}$ is the diffusion coefficient of $\text{Li}^{+}$, $i_p$ is the peak current, $n$ is the number of electrons involved in the reactions ($n$ = 1 in this system), $A$ is the contact area between the electrode and electrolyte, $C_{Li}$ is the Li-ions concentration in the electrolyte, and $v$ is the scan rate.${}^{31-32}$ According to the CV curves measured in the potential range of 0-1.1 V, the extracted diffusion coefficient for Li-ions was calculated to be $2.12{\times}10^{-12}$ cm² s⁻¹. Notably, the achieved $\text{Li}^{+}$ diffusion coefficient of the NiO electrode compares favorably with those of other reported NiO based positive electrodes in Li-ion supercapacitors (most at magnitudes of $\sim$$10^{-12}$–$10^{-15}$ cm² s⁻¹). Based on the CV curves, the areal capacitance and the volumetric capacitance were calculated and demonstrated in Figure 2c. The NiO electrode achieved the maximum areal capacitance and volumetric capacitance of 23.4 mF cm⁻² and 173.6 F cm⁻² at 5 mV s⁻¹, which are higher than the previous report with $\text{MnO}_{2}@$PPy (6.53 mF cm⁻² at 5 mV s⁻¹).${}^{33}$ Furthermore, when the scan rate increased from 5 to 200 mV s⁻¹, the

volumetric capacitance was retained at 50%, indicating excellent rate capability. The quasi-rectangular CV profiles and linear symmetric GCD curves with a slight hump suggest that the charge storage of the NiO film includes both faradaic and capacitive behaviors.

The faradaic and capacitive controlled processes can be identified by analyzing the CV data according to the relation of $\log i_{p}=b \times \log v+\log a$, where $v$ is the sweep rate, and $a$ and b are changeable parameters (Figure 2d). Here, the value of $b$=0.5 stands for a diffusion-controlled process, while $b$=1.0 stands for a surface-prevailed process. The obtained $b$ values of NiO are 0.88, 0.89, 0.86, 0.87 and 0.84, implying that the total capacity of the NiO is controlled by both capacitor-like and diffusion-dominated behavior. The quantitative contribution from the diffusion-controlled insertion processes and surface capacitor-like processes for the charge storage can be distinguished according to Dunn's method. $^{34-35}$

![](./images/812583435875909633_2.jpg)

Figure 2. Electrochemical and optical characterizations of the NiO electrode. a) Cyclic voltammetry curves at various scan rates. b) Galvanostatic charge/discharge curves at different current densities. c) Areal and volumetric capacitance. d) $\log i_{p}$ versus $\log v$ linear relationship. e) CV curves at $5\ \text{mV·s}^{-1}$ illustrating the surface capacitance contribution (shadow area) to total current. f) Percentage of the diffusion-controlled and surface capacitive behavior at different scan rates.

Figure 2e displays the representative CV curve recorded at $5\ \text{mV s}^{-1}$ with about 76.6% of the total capacity deriving from the capacitive contribution (shaded region). Meanwhile, the surface capacitive effect becomes gradually dominant when the scan rate increases (Figure 2f). The desirable capacitive behavior contributes to the superior

rate capability and excellent cycling stability, which may be attributed to the nanoscale particles and porous structure of the NiO electrode. Although the above investigations have clarified the charge storage behavior of NiO to a certain extent, a detailed mechanism of the Li atom migration kinetics involved in the charge storage process is still unclear.

A fundamental understanding of the pseudocapacitance of transition metal oxides will promote their real-world applications in electrochromic devices and SCs. Although the NiO electrode presents excellent electrochromic performance and ultra-high pseudocapacitance, its electrochromism and charge storage mechanisms at the atomic/molecular level are largely unclear until now. Thus, the NiO electrode was further investigated via DFT to better comprehend the dominance of the surface-based pseudocapacitive behavior by the surface adsorption and diffusion behavior of the Li atoms. Before exploring the surface adsorption and diffusion behavior of NiO, we also check the structural stability. The stability of adsorption geometry has assessed by ab initio molecular dynamics (AIMD)³⁶⁻³⁷ under the NVT ensemble with a time step of 1.0 fs at 298K and a total duration of 1.2 ps. As shown in Figure S2, the plot of Potential energy vs simulation time shows nearly constant trend (red line is the linear fitting) indicating the stability of equilibrium configurations. In other words, the structure is quite intact and energy is well converged.

First, the adsorption behavior of lithium on the NiO surface was calculated to determine the preferred orientation, including on the NiO (1 1 1), NiO (1 1 0) and NiO (1 0 0) surfaces, in that the electronic properties of the NiO slab are strongly associated with the surface terminations.

Because the surface compositions of different crystal faces are different, four symmetrical positions top (T), bridge (B), fcc (H1), and hcp (H2), were examined on the (1 1 1) surface.

Figure 3 depicts the optimized structure of the NiO (1 1 1) plane with diverse views (top and

![](./images/812583435875909633_3.jpg)

Figure 3. The optimized structure of NiO (111) plane. As viewed from a) ZY plane, b) XZ plane, c) XY plane. d) Top site (T), e) Bridge site (B), f) Fcc site (H1), g) Hcp site (H2). The pink, blue and green balls indicate Ni, O and Li atoms, respectively.

side views) and the possible adsorption sites of the Li atom. As for NiO (1 1 0) and NiO (1 0 0),

the O-Ni-bridge and four-degree vacancy sites were considered, including the above

four relaxed configurations, as shown in Figure S3. The structural stability was

estimated by comparing the relative adsorption energy. The adsorption energies of each

surface at distinctive sites are listed in Table S1. Almost all the calculated adsorption

energies are negative, clearly suggesting that Li atoms are more inclined to adsorb onto the NiO surface rather than self-clustering. The adsorption energy of the H1 site of NiO (1 1 1) was found to be -7.15 eV. Notably, the adsorption energy of the (1 1 1) plane was far larger than those of the NiO (1 0 0) and (1 1 0) planes, suggesting that Li-atoms tend to prefer adsorbing on the (1 1 1) crystal plane of the NiO film.

The geometric parameters of Li atoms adsorbed on the NiO (1 1 1) surface are shown in **Table S2**. Upon Li adsorption, the Ni atoms adjacent to Li atom undergo a slight distortion. The Ni-O bond length changed slightly when the Li atom was implanted into the NiO. This is due to the interaction between the Li atom and the O atom, causing the position of the oxygen atom and the Ni-O bond angle to change. It can be seen from **Table S2** that the adsorption energy of the H1 site (-7.15 eV) is obviously higher than other sites, indicating that the Li atom prefers to adsorb on the H1 site. Moreover, after structural optimization, the adsorbed Li atoms on the B and T sites will ultimately migrate to the hollow site (H1), which confirms that the H1 site is the most stable

adsorption site. In other words, this means that the charge storage mechanism of NiO is closely related to the adsorption behavior of the (1 1 1) plane.

Table 1. The Bader charge of the NiO (111) plane in the H, B, H1, and H2 sites.

<table>
  <thead>
    <tr>
      <th rowspan="2">Species</th>
      <th colspan="4">Charge transfer(eV)</th>
    </tr>
    <tr>
      <th>T</th>
      <th>B</th>
      <th>H1</th>
      <th>H2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ni</td>
      <td>-1.0095</td>
      <td>-1.0119</td>
      <td>-1.0375</td>
      <td>-1.0246</td>
    </tr>
    <tr>
      <td>O</td>
      <td>+1.0256</td>
      <td>+1.0279</td>
      <td>+1.0539</td>
      <td>+1.0408</td>
    </tr>
    <tr>
      <td>Li</td>
      <td>-0.8689</td>
      <td>-0.8633</td>
      <td>-0.8868</td>
      <td>-0.8778</td>
    </tr>
  </tbody>
</table>

More significantly, the theoretical simulation can be used to further understand the electrochromic process of the NiO electrode. Wen *et al.* demonstrated that charge exchange in the NiO electrochromic electrode is mainly due to surface processes and involves both cations and anions from the electrolyte, rather than like the case of $WO_3$ electrochromic electrode that exhibited cation intercalation processes, which is consistent with our above theoretical simulation results. To further evaluate the

variations in the valence states for the NiO electrode, the charge transfer and distributions at the colored and bleached states were analyzed.

The charge density difference of the NiO (1 1 1) plane H1 site at different states is shown in **Figure 4** with an isovalue of 0.0023. The charge density differences of the other three adsorbed sites are displayed in **Figure S4**. When a Li atom adsorbs, the electron loss and accumulation are found in the region above the Li atom (purple part) and between the O and Li atom (green part), resulting in a strong chemical bond between the Li and O atoms, which indicates strong electron transfer from the Li atom to the O atoms (**Figure 4b**). At the same time, the electron loss region presented around the Ni atoms in order to maintain the charge balance of the NiO system.

![](./images/812583435875909633_4.jpg)

![](./images/812583435875909633_5.jpg)

Figure 4. Electrochromic mechanism of the NiO electrode. a-b) Charge density difference of (1 1 1) plane with isovalue 0.0023, where the purple and blue part stand by loss and gain in charge. The charge density difference which is obtained by subtracting from the charge density of the total adsorbed system, $\Delta \rho=\rho_{\mathrm{NiO}(111)+\mathrm{Li}}-\left(\rho_{\mathrm{NiO}(111)}+\rho_{\mathrm{Li}}\right)$. c) The slab cut along (0 0 1) direction of charge density difference in NiO (1 1 1) plane; d) The slab cut along (0 0 1) direction of charge density before the lithium atom adsorbed. The pink, blue and green balls indicate Ni, O and Li atoms, respectively. e-f) XPS spectra at the colored and bleached states.

Moreover, the charge density difference of the slab cut along the $(0\ 0\ 1)$ direction further confirms that the quantity of charge is transferred from the Li atom to the O atom (Figure 4d). Furthermore, the Bader charge method was performed to quantitatively analyze the charge transfer and chemical interaction from an overall perspective. Table 1 presents the Bader charge from the slab to the lithium atom. For the Li atom, the charge transfer amounts at the T, B, H1, and H2 positions were $-0.8689e$, $-0.8633e$, $-0.8778e$, and $-0.8868e$, respectively, which approaches approximately $-1.0e$. Meanwhile, the charge transfer amount about the Ni atoms nears $-1.0e$, resulting in an increased valence state from $Ni^{2+}$ to $Ni^{3+}$ that is accompanied with color changes of the transparent NiO electrode. To investigate the valence change of the nickel ions in NiO at various states, an *ex-situ* XPS measurement was carried out. Notably, the proportion of $Ni^{3+}$ ions contained in NiO increased from 58.4 % to 68.9 % during the coloring process, and was simultaneously accompanied by an increased $Ni_2O_3$ content (Figure 4e-f). It can be clearly seen that the XPS analysis results were well matched with the theoretical computations.

To get further insight into the influence of the adsorption behavior on the charge storage, the density of states (DOS) of the NiO systems were calculated. The partial density of states (PDOS) of bare NiO and Li$_x$NiO are depicted in Figure 5a with $x$=0.037, 0.185, and 0.222, respectively. As shown in Figure 5b, the bandgap of the bare NiO is near 3.37 eV, which is slightly smaller than the experimental value of 3.8 eV.$^{38}$ After the Li adsorbed on the NiO (111) plane, the bandgap decreased to 1.65 eV. With the increase of Li concentration, the bandgap of the system continued to decrease. Interestingly, the system became metallic when six lithium atoms were adsorbed on the H1 site, demonstrating that the material possesses an excellent conductive performance as a supercapacitor (Figure 5d). Moreover, with the decrease of the bandgap, photoelectrons absorb energy more easily and undergo transitions, which is beneficial to the adsorption behavior of lithium ions. In addition, the DOS with 2-9 Li atoms are presented in Figure S5.

![](./images/812583435875909633_6.jpg)

Figure 5. Adsorption behavior of the NiO electrode. a) The partial Density of State (PDOS) of bare NiO. b~d) The partial Density of State (PDOS) of Li$_x$NiO with $x$=0.037, 0.185, 0.222, respectively. e) Calculated different Li-ion concentration of adsorption energies. f) Intercalation voltage on fcc sites of NiO (1 1 1) plane.

To explore how many Li atoms can be adsorbed on the NiO (1 1 1) surface before the adsorption energy reaches the cohesive energy of BCC-Li, the sequential adsorption energies at various adsorption concentrations were calculated. Subsequently, the maximum theoretical capacity ($C_M$) and the intercalation potential $V$ were calculated for the Li atom in the surface process. Based on the above discussion, the fcc site on the

NiO (1 1 1) plane was considered as the initial state. The concentration of Li atoms on the fcc site of the NiO (1 1 1) plane was altered by inserting 2, 3, 4, 5, 6, 7, 8 and 9 Li atoms (i.e., $x$ = 0.074, 0.111, 0.148, 0.185, 0.222, 0.259, 0.296 and 0.333 in $\text{Li}_x\text{NiO}$, respectively). The relaxed adsorption structures for a variety lithium concentrations on NiO the (1 1 1) surface are shown in Figure S6. Consequently, the maximum theoretical capacity ($C_M$) was appraised by equation (2):

$$
C_{M}=\frac{\mathrm{xF}}{M_{NiO}} \tag{2}
$$

where the $x$ is the number of adsorbed Li atom, $F$ is the Faraday constant and $\text{M}_{NiO}$ is the molar weight of NiO.

Then, the insertion voltage was calculated by the following equation:

$$
V=-\frac{E_{Li_{x}Ni_{27}O_{27}}-E_{Ni_{27}O_{27}}-xE_{Li}}{zxe} \tag{3}
$$

where $z$, $E_{Li}$ , $E_{Li_{x}Ni_{27}O_{27}}$ and $E_{Ni_{27}O_{27}}$ are the charge of Li, the total energy per atom for the bulk Li and the total energies of $E_{Li_{x}Ni_{27}O_{27}}$ and $E_{Ni_{27}O_{27}}$, respectively. Figure 5e shows that the adsorption energy of 9 adsorbed Li atoms is higher than the cohesive energy of BCC-Li, demonstrating that the NiO (111) plane can take in at large as 8 Li atoms. That

is, Li dendrite is begins to form when the adsorption is over the cohesive energy of Li.

Thus, according to equation (3), the maximum theoretical surface capacity is 106 mAh
g⁻¹, corresponding to the Li₀.₂₉₆NiO. The computed capacity is very similar to the experimentally measured results (137 mAh g⁻¹).³⁹ As shown in **Figure 5f**, the lithiation process exhibits five plateaus with a decreasing trend. The initial to final process is Li₀.₀₇₄NiO→ Li₀.₁₁₁NiO, Li₀.₁₄₈NiO→ Li₀.₁₈₅NiO, Li₀.₁₈₅NiO→ Li₀.₂₂₂NiO and Li₀.₂₅₉NiO→ Li₀.₂₉₆NiO corresponding to 1.57, 1.26, 0.87, 0.45 and 0.26 V vs. Li/Li⁺, respectively. The average voltage value is 0.882 V.

With that, the diffusion behavior was evaluated to reveal the charge storage mechanism. The diffusion barrier energy was computed by the climbing-image nudged elastic band (CI-NEB) method. First, the influence of surface diffusion on the charge storage mechanism is discussed. Since the fcc site is energetically favorable, the two possible diffusion pathways between neighbor fcc sites are shown in **Figure 6a**, which are along the A and B directions. The calculated diffusion barriers for the Li atom are both 224 meV along the path-1 and path-2 directions, as shown in **Figure 6b**. This result confirms that the ion diffusion velocity of the two paths is comparable. Besides, the

surface diffusion barrier is lower than that of some two-dimensional materials, such as
GeP₃ (0.4 eV), graphene (0.37 eV) and MoS₂(0.25 eV).⁴⁰⁻⁴² Such a lower diffusion
barrier facilitates the transportation of electrons and ions on the surface.

![](./images/812583435875909633_7.jpg)

Figure 6. Li-atoms diffusion energy barrier of the NiO surface and bulk. a) The potential
Li-ion migration pathways on the (111) plane. b) The minimum energy path (MEP)
illustration the barriers of Li diffusion along path-1 and path-2. c) The possible diffusion
path of the surface to bulk, from a to d. d) The corresponding diffusion barriers of
surface to bulk. e) The possible bulk diffusion path, Li1 to Li2, Li2 to Li3 and Li3 to Li4
with path-1, path-2, and path-3, respectively. f) The diffusion barrier profiles of bulk to
bulk. The pink, blue and green balls indicate Ni, O and Li atoms, respectively.

Second, the effect of Li atom diffusion from the surface toward the bulk on charge storage was also investigated. As elucidated in **Figure 6c**, the possible Li atom migration paths following surface $\rightarrow$ bulk are rationally built. Along the diffusion path from the surface toward the inside of the bulk, Li atoms penetrate three layers (from point a to point d). The diffusion barrier is calculated to be 12.44 eV for Li atom penetrating the three layers (**Figure 6d**), illustrating that as Li atoms migrate from the surface toward the bulk, penetrating layers is quite burdensome. These diffusion barriers show that Li atoms are more likely to diffuse along the (1 1 1) surface, rather than penetrating the three layers due to the excessive diffusion barrier height of the surface to the bulk. Therefore, the effect of Li atom diffusion from bulk to bulk was also evaluated. The possible Li atom migration paths following bulk $\rightarrow$ bulk (path-1, path-2 and path-3) are shown in **Figure 6e**. The diffusion barrier profiles from one unoccupied tetrahedral site to another are shown in **Figure 6f**. The diffusion barriers are 0.66 eV, 0.72 eV and 0.66 eV along path-1, path-2 and path-3, respectively, which are generally higher than the diffusion barrier for the surface diffusion, but lower than the barrier of the surface toward the bulk. These results imply that most of the Li atoms are adsorbed on

the surface, yet a small part of them could migrate into the inner during the charging/discharging process. Due to the ultrahigh diffusion barrier of the surface toward the inside of bulk, the diffusion-controlled capacity contributes only slightly to charge storage. This further confirms that the dominance of surface diffusion in the charge storage process.

Taking the above discussions into consideration, the electrochemical processes and charge storage mechanism of the NiO electrochromic electrode based on Li atom electrolytes are schematically depicted in Figure 7a. First of all, Li atoms will prefer to absorb at active sites on the NiO (1 1 1) plane with low Li content. During this process, faradaic redox reactions will occur on the host NiO surface, with an accompanying in change of the Ni valance. This phenomenon is called surface redox pseudocapacitance behavior. Benefiting from this process, the electrode can undergo stable and reversible electrochromic performance. Of course, it is not excluded that the anions (such as $ClO_4^-$) in the electrolyte will also undergo desorption/adsorption on the surface due to the porous nanostructure of the NiO electrodes. In other words, there may also be double-layer energy storage behavior on the electrode surface. Then, the adsorbed ions will

diffuse horizontally over the electrode surface to open space for the next adsorbing ions. Last but not least, the Li atoms will diffuse from the surface to the subsurface and finally migrate in the bulk. In fact, the diffusion process only provides a weak contribution to the energy storage of the electrode due to the large diffusion energy barrier. Based on the above discussion, the discharging process of the NiO electrode is schematically illustrated in Figure 7b. The voltage decreases monotonically with increasing capacity in the surface storage process, while it presents a plateau in the bulk storage process. In other words, the electrochromism and pseudocapacitance of the NiO electrode originate from the adsorption of Li atom on the (1 1 1) plane. The surface capacitive charge storage dominates and is responsible for the excellent electrochemical cyclic performance of the NiO electrode.

![](./images/812583435875909633_8.jpg)

Figure7. The charge storage mechanism of the NiO electrode. a) Electrochemical processes and charge storage mechanism of the NiO. b) Schematic illustration of the Li-storage mechanism of NiO and the atomic structures of Li-adsorbed.

## 4. Conclusions

In summary, a comprehensive study of a sputter-deposited NiO electrochromic supercapacitor was performed via combining experimental and theoretical analyses. The as-prepared NiO electrochromic supercapacitor exhibited superior rate capability and highly reversible electrochromic behavior, which is comparable if not better than previously reported works. The Li atoms reaction kinetics on the NiO electrode were investigated by detailed analysis of cyclic voltammetry curves, demonstrating the energy storage is controlled by both capacitor-like and diffusion-dominated behavior, while the surface capacitance behavior is dominant. Moreover, the adsorption and diffusion mechanisms were further investigated by first-principle calculations, revealing that Li atoms prefer to occupy fcc sites on the NiO (1 1 1) plane, eventually forming $Li_{0.296}$NiO on the surface. Furthermore, the electrochromic behavior was accompanied

by a surface oxidation reaction due to the valence band of the host material being altered. In addition, the adsorbed Li atoms on the (1 1 1) plane will first diffuse horizontally over the electrode surface, then diffuse to the subsurface and finally migrate in the bulk. More significantly, the calculated theoretical surface capacity (106 mAh g⁻¹) accounts for about 77.4 % of the total experimental capacity (137 mAh g⁻¹), demonstrating that the surface storage process plays an indispensable and essential role in the charge storage mechanism. Revealing the detailed electrochromic energy storage mechanism of the NiO electrode may offer new insights into the design of novel electrochromic supercapacitor electrodes. Importantly, the combination of in-depth experimental and theoretical approaches developed in this paper is readily applicable to probing the kinetics and mechanisms of adsorption and diffusion processes in other transition metal oxide-based electrochromic supercapacitor electrodes.

Supporting Information.

Geometric parameters, adsorption energy, N₂ adsorption-desorption isotherm, PDOS of NiO (111) and optimized structure of NiO (110), (100) plane

### Corresponding Author

* E-mail: yiyong@swust.edu.cn(Yong Yi);

* E-mail: BY1719120@buaa.edu.cn(Lei Liu).

### Author Contributions

The manuscript was written through the contributions of all authors. All authors have given approval to the final version of the manuscript. Zhihui Luo and Lei Liu contributed equally to this work. Lei Liu performed the experiment. Zhihui Luo completed the theoretical simulation and drafted the manuscript. Dr. Xiaoyong Yang and Dr. Yong Yi contributed to the conception and design of this topic. Xuan Luo, Peng Bi and Zhenjin Fu helped perform the analysis with constructive discussions. Wei Li and Aimin Pang helped to comment on the revised manuscript.

### Acknowledgments

This work was financially supported by the Project of State Key Laboratory of Environment-friendly Energy Materials, Southwest University of Science and

Technology (No.18fksy0203,19fksy08), the Open research fund program of science and technology on aerospace chemical power laboratory (STACPL12018B05-1), the Academic Excellence Foundation of BUAA for Ph.D. Students (Lei LIU, BY1719120) and the National Natural Science Foundation of China (21975066, 21875061).

Conflict of Interest

The authors declare no conflict of interest.

References

(1) Augustyn, V.; Simon, P.; Dunn, B. Pseudocapacitive Oxide Materials for High-Rate Electrochemical Energy Storage. *Energy & Environmental Science* **2014**, 7, 1597-1614.

(2) Li, H.; Qi, C.; Tao, Y.; Liu, H.; Wang, D. W.; Li, F.; Yang, Q. H.; Cheng, H. M. Quantifying the Volumetric Performance Metrics of Supercapacitors. *Advanced Energy Materials* **2019**, 9, 1900079.

(3) Wang, F.; Wu, X.; Yuan, X.; Liu, Z.; Zhang, Y.; Fu, L.; Zhu, Y.; Zhou, Q.; Wu, Y.; Huang, W. Latest Advances in Supercapacitors: From New Electrode Materials to Novel Device Designs. *Chemical Society Reviews* **2017**, 46, 6816-6854.

(4) Zhen Wang, X. W., Shan Conga, Fengxia Geng, Zhigang Zhao. Fusing Electrochromic Technology with Other Advanced Technologies: A New Roadmap for Future Development. *Materials Science & Engineering R* **2019**, 140, 100524.

(5) Liu, L.; Du, K.; He, Z.; Wang, T.; Zhong, X.; Ma, T.; Yang, J.; He, Y.; Dong, G.; Wang, S.; Diao, X. High-Temperature Adaptive and Robust Ultra-Thin Inorganic All-Solid-State Smart Electrochromic Energy Storage Devices. *Nano Energy* **2019**, *62*, 46-54.

(6) Liu, L.; Zhang, Q.; Du, K.; He, Z.; Wang, T.; Yi, Y.; Wang, M.; Zhong, X.; Dong, G.; Diao, X. An Intelligent and Portable Power Storage Device Able to Visualize the Energy Status. *Journal of Materials Chemistry A* **2019**, *7*, 23028-23037.

(7) Xiangtao Huo; Huanyu Zhang; Weiguo Shen; Xiwang Miao; Mei Zhang; Guo, M. Bifunctional Aligned Hexagonal_Amorphous Tungsten Oxide Core_Shell Nanorod Arrays with Enhanced Electrochromic and Pseudocapacitive Performance. *Journal of Materials Chemistry A* **2019**, *7*, 16867-16875.

(8) Cai, G.; Darmawan, P.; Cui, M.; Wang, J.; Chen, J.; Magdassi, S.; Lee, P. S. Highly Stable Transparent Conductive Silver Grid/PEDOT: PSS Electrodes for Integrated Bifunctional Flexible Electrochromic Supercapacitors. *Advanced Energy Materials* **2016**, *6*, 1501882.

(9) Yun, T. G.; Park, M.; Kim, D. H.; Kim, D.; Cheong, J. Y.; Bae, J. G.; Han, S. M.; Kim, I. D. All-Transparent Stretchable Electrochromic Supercapacitor Wearable Patch Device. *ACS Nano* **2019**, *13*, 3141-3150.

(10) Qin, S.; Zhang, Q.; Yang, X.; Liu, M.; Sun, Q.; Wang, Z. L. Hybrid Piezo/Triboelectric-Driven Self-Charging Electrochromic Supercapacitor Power Package. *Advanced Energy Materials* **2018**, *8*, 1800069.

(11) Thakur, V. K.; Ding, G.; Ma, J.; Lee, P. S.; Lu, X. Hybrid Materials and Polymer Electrolytes for Electrochromic Device Applications. *Adv Mater* **2012**, *24*, 4071-96.

(12) Cai, G.; Wang, J.; Lee, P. S. Next-Generation Multifunctional Electrochromic Devices. *Acc Chem Res* **2016**, *49*, 1469-76.

(13) Liu, Q.; Chen, Q.; Zhang, Q.; Xiao, Y.; Zhong, X.; Dong, G.; Delplancke-Ogletree, M.-P.; Terryn, H.; Baert, K.; Reniers, F.; Diao, X. In Situ Electrochromic Efficiency of a Nickel Oxide Thin Film: Origin of Electrochemical Process and Electrochromic Degradation. *Journal of Materials Chemistry C* **2018**, *6*, 646-653.

(14) Guo, J.; Wang, M.; Dong, G.; Zhang, Z.; Zhang, Q.; Yu, H.; Xiao, Y.; Liu, Q.; Liu, J.; Diao, X. Mechanistic Insights into the Coloration, Evolution, and Degradation of NiOx Electrochromic Anodes. *Inorganic Chemistry* **2018**, *57*, 8874-8880.

(15) Cai, G.; Wang, X.; Cui, M.; Darmawan, P.; Wang, J.; Eh, A. L.-S.; Lee, P. S. Electrochromo-Supercapacitor Based on Direct Growth of NiO Nanoparticles. *Nano Energy* **2015**, *12*, 258-267.

(16) Dong, W.; Lv, Y.; Zhang, N.; Xiao, L.; Fan, Y.; Liu, X. Trifunctional NiO-Ag-NiO Electrodes for ITO-Free Electrochromic Supercapacitors. *Journal of Materials Chemistry C* **2017**, *5*, 8408-8414.

(17) Decker, F.; Passerini, S.; Pileggi, R.; Scrosati, B. The Electrochromic Process in Non-Stoichiometric Nickel Oxide Thin Film Electrodes. *Electrochimica Acta* **1992**, *37*, 1033-1038.

(18) Wen, R.-T.; Granqvist, C. G.; Niklasson, G. A. Anodic Electrochromism for Energy-Efficient Windows: Cation/Anion-Based Surface Processes and Effects of Crystal Facets in Nickel Oxide Thin Films. *Advanced Functional Materials* **2015**, *25*, 3359-3370.

(19) Dong, D.; Djaoued, H.; Vienneu, G.; Robichaud, J.; Brown, D.; Brüning, R.; Djaoued, Y. Electrochromic and Colorimetric Properties of Anodic NiO Thin Films: Uncovering Electrochromic Mechanism of NiO. *Electrochimica Acta* **2020**, *335*, 135648.

(20) G. Kresse, J. F. Efficiency of Ab-Initio Total Energy Calculations for Metals and Semiconductors Using a Plane-Wave Basis Set. *Computational Materials Science* **1996**, *6*, 0-50.

(21) Kresse G; J., F. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. *Physical Review B* **1996**, *54*, 11169-11189.

(22) Kresse G; Joubert D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. *Physical Review B* **1999**, *59*, 1758-1775.

(23) Blochl, P. E. Projector Augmented-Wave Method. *Phys Rev B Condens Matter* **1994**, *50*, 17953-17979.

(24) John P. Perdew; Kieron Burke; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Physical Review Letters* **1996**, *77*, 3865-3868.

(25) Yamada, T. K.; Bischoff, M. M.; Heijnen, G. M.; Mizoguchi, T.; Van Kempen, H. Observation of Spin-Polarized Surface States on Ultrathin Bct Mn(001) Films by Spin-Polarized Scanning Tunneling Spectroscopy. *Phys Rev Lett* **2003**, *90*, 056803.

(26) Monkhorst, H. J.; Pack, J. D. Special Points for Brillouin-Zone Integrations. *Physical Review B* **1976**, *13*, 5188-5192.

(27) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A Consistent and Accurate Ab Initio Parametrization of Density Functional Dispersion Correction (DFT-D) for the 94 Elements H-Pu. *J Chem Phys* **2010**, *132*, 154104.

(28) Grimme, S. Density Functional Theory with London Dispersion Corrections. *WIRES Computational Molecular Science* **2011**, *1*, 211-228.

(29) Tang, W.; Sanville, E.; Henkelman, G. A Grid-Based Bader Analysis Algorithm without Lattice Bias. *J Phys Condens Matter* **2009**, *21*, 084204.

(30) Cai, G. F.; Tu, J. P.; Zhang, J.; Mai, Y. J.; Lu, Y.; Gu, C. D.; Wang, X. L. An Efficient Route to a Porous NiO/Reduced Graphene Oxide Hybrid Film with Highly Improved Electrochromic Properties. *Nanoscale* **2012**, *4*, 5724-30.

(31) Yu, H.; Guo, J.; Wang, C.; Zhang, J.; Liu, J.; Zhong, X.; Dong, G.; Diao, X. High Performance in Electrochromic Amorphous WOx Film with Long-Term Stability and Tunable Switching Times Via Al/Li-ions Intercalation/Deintercalation. *Electrochimica Acta* **2019**, *318*, 644-650.

(32) Wang, F.; Zhang, N.; Zhao, X.; Wang, L.; Zhang, J.; Wang, T.; Liu, F.; Liu, Y.; Fan, L. Z. Realizing a High-Performance Na-Storage Cathode by Tailoring Ultrasmall Na₂FePO₄F Nanoparticles with Facilitated Reaction Kinetics. *Adv Sci (Weinh)* **2019**, *6*, 1900649.

(33) Yue, Y.; Yang, Z.; Liu, N.; Liu, W.; Zhang, H.; Ma, Y.; Yang, C.; Su, J.; Li, L.; Long, F.; Zou, Z.; Gao, Y. A Flexible Integrated System Containing a Microsupercapacitor, a Photodetector, and a Wireless Charging Coil. *ACS Nano* **2016**, *10*, 11249-11257.

(34) Kim, J. W.; Augustyn, V.; Dunn, B. The Effect of Crystallinity on the Rapid Pseudocapacitive Response of Nb₂O₅. *Advanced Energy Materials* **2012**, *2*, 141-148.

(35) Kim, J. W.; Augustyn, V.; Dunn, B. Pseudocapacitive Contributions to Electrochemical Energy Storage in TiO₂ (Anatase) Nanoparticles. *Journal of Physical Chemistry C* **2007**, *111*, 14925-14931.

(36) Pavone, P.; Karch, K.; Schutt, O.; Strauch, D.; Windl, W.; Giannozzi, P.; Baroni, S. Ab Initio Lattice Dynamics of Diamond. *Phys Rev B Condens Matter* **1993**, *48*, 3156-3163.

(37) Jena, N. K.; Araujo, R. B.; Shukla, V.; Ahuja, R. Borophane as a Bench-Mate of Graphene: A Potential 2D Material for Anode of Li and Na-ion Batteries. *Acs Applied Materials & Interfaces* **2017**, *9*, 16148-16158.

(38) Kumari, L.; Li, W. Z.; Vannoy, C. H.; Leblanc, R. M.; Wang, D. Z. Vertically Aligned and Interconnected Nickel Oxide Nanowalls Fabricated by Hydrothermal Route. *Crystal Research and Technology* **2009**, *44*, 495-499.

(39) Thomas, M. G. S. R.; David, W. I. F.; Goodenough, J. B. Synthesis and Structural Characterization of the Normal Spinel $Li[Ni_2]O_4$. *Materials Research Bulletin* **1985**, *20*, 1137-1146.

(40) Zhang, C.; Jiao, Y.; He, T.; Ma, F.; Kou, L.; Liao, T.; Bottle, S.; Du, A. Two-Dimensional $GeP_3$ as a High Capacity Electrode Material for Li-ion Batteries. *Physical Chemistry Chemical Physics* **2017**, *19*, 25886-25890.

(41) David, L.; Bhandavat, R.; Singh, G. $MoS_2$/Graphene Composite Paper for Sodium-ion Battery Electrodes. *ACS Nano* **2014**, *8*, 1759-1770.

(42) Mortazavi, M.; Wang, C.; Deng, J.; Shenoy, V. B.; Medhekar, N. V. Ab Initio Characterization of Layered $MoS_2$ as Anode for Sodium-ion Batteries. *Journal of Power Sources* **2014**, *268*, 279-286.

Table of Contents

![](./images/812583435875909633_9.jpg)