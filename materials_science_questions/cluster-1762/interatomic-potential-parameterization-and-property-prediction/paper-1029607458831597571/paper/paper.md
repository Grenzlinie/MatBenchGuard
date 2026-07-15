Article

# Atomistic Simulation Studies of $\mathbf{Na_4SiO_4}$

Mallikage Shalani Shanika $^{1}$, Poobalasingam Abiman $^{1}$, Poobalasuntharam Iyngaran $^{1}$
and Navaratnarajah Kuganathan $^{2,*}$

1 Department of Chemistry, University of Jaffna, Thirunelvely, Jaffna 40000, Sri Lanka;
shalanishanika@univ.jfn.ac.lk (M.S.S.); abiman@univ.jfn.ac.lk (P.A.); piyngaran@univ.jfn.ac.lk (P.I.)
2 Department of Materials, Faculty of Engineering, Imperial College London, London SW7 2AZ, UK
* Correspondence: n.kuganathan@imperial.ac.uk

**Abstract:** Tetrasodium silicate ($\text{Na}_4\text{SiO}_4$) has emerged as a promising candidate for battery applications due to its favorable ionic transport properties. Atomic-scale simulations employing classical pair potentials have elucidated the defect mechanisms and ion migration dynamics in $\text{Na}_4\text{SiO}_4$. The Na Frenkel defect, characterized by the creation of a Na vacancy and an interstitial $\text{Na}^{+}$ ion, is identified as the most energetically favorable defect process, facilitating efficient vacancy-assisted $\text{Na}^{+}$ ion migration. This process results in three-dimensional ion diffusion with a low activation energy of 0.55 eV, indicating rapid ion movement within the material. Among monovalent dopants ($\text{Li}^{+}$, $\text{K}^{+}$, and $\text{Rb}^{+}$), $\text{K}^{+}$ was found to be the most advantageous for substitution on the Na site. For trivalent doping, Al is the most favorable on the Si site, generating additional $\text{Na}^{+}$ ions and potentially enhancing ionic conductivity. Ge was identified as a promising isovalent dopant for the Si site. These theoretical findings suggest that $\text{Na}_4\text{SiO}_4$ could offer high ionic conductivity and stability when optimized through appropriate doping. Experimental validation of these predictions could lead to the development of advanced battery materials with improved performance and durability.

**Keywords:** tetra sodium silicate; defects; diffusion; atomistic simulation; battery material

![](./images/1029607458831597571_1.jpg)

Citation: Shanika, M.S.; Abiman, P.;
Iyngaran, P.; Kuganathan, N.
Atomistic Simulation Studies of
$\text{Na}_4\text{SiO}_4$. *Crystals* **2024**, 14, 718.
https://doi.org/10.3390/
cryst14080718

Academic Editor: Ram S. Katiyar

Received: 24 July 2024
Revised: 5 August 2024
Accepted: 7 August 2024
Published: 10 August 2024

![](./images/1029607458831597571_2.jpg)

Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

## 1. Introduction

Creating clean, renewable energy is one of the major challenges of the 21st century, and overcoming this challenge necessitates the advancement of innovative material systems. Advances in materials science are crucial for enhancing the efficiency, cost-effectiveness, and sustainability of various energy technologies.

Batteries have transformed into a fundamental aspect of modern technology, seamlessly integrating into nearly every electronic device [1–4]. Acting as vital energy reservoirs, they have diverse applications across various industries [5–7]. Presently, lithium-ion batteries dominate the market, especially in electric vehicles and electronic gadgets [8–10]. However, the diminishing availability of lithium minerals poses a challenge to meeting demand. The world is currently grappling with a shortfall in lithium supply. In response, sodium-ion batteries have emerged as a focal point of extensive research, offering promise as a sustainable alternative to lithium-ion batteries [11–15]. Multiple molecules are currently under consideration as potential materials for anodes and cathodes in sodium-ion batteries [16–18].

The selection of electrode or electrolyte materials for Na-ion batteries is critical to achieving high performance, safety, and cost-effectiveness. Each material class has its advantages and challenges, and ongoing research focuses on optimizing these materials through structural engineering, composite formation, and surface modifications. Polyanionic-type materials are gaining significant attention in the development of Na-ion batteries due to their high working potential, excellent structural stability, and safety. These materials include compounds where the active cathode species are coordinated by anionic groups

---
*Crystals* **2024**, 14, 718. https://doi.org/10.3390/cryst14080718  
https://www.mdpi.com/journal/crystals

such as phosphates (e.g., $NaMPO_4$ ($M$ = Fe, Mn, Ni)), sulfates (e.g., $Na_2MSiO_4$ ($M$ = Fe, Mn, Co, Ni)) and borates (e.g., $Na_3MB_5O_{10}$ ($M$ = V, Fe, Mn, Co, etc.)) [19–22].

$Na_4SiO_4$ holds particular significance in this pursuit [23]. As a mineral, it presents potential as a key component in the development of sodium-ion batteries. Research is actively investigating its potential and effectiveness in meeting the increasing demand for energy storage solutions [24–26]. $Na_4SiO_4$ can be produced through a wet mixing method using $NaOH$ and $Na_2SiO_3\bullet9H_2O$ as raw materials [27]. A key benefit of $Na_4SiO_4$ is its stability and eco-friendly characteristics. It can be easily prepared using simple, abundant raw materials at low cost. Furthermore, like orthophosphates, the orthosilicate ($SiO_4^{4-}$) matrix benefits from strong Si–O bonds. These bonds contribute to the structural stability of the material, which is crucial for maintaining integrity during lithium insertion and extraction cycles. The study of $CO_2$ chemisorption on $Na_4SiO_4$ doped with oxysalt surfaces using density functional theory (DFT) calculations highlights the potential of doping $Na_4SiO_4$ with oxysalts to create more effective materials for $CO_2$ capture, contributing to efforts in mitigating climate change by reducing atmospheric $CO_2$ levels [24]. The addition of alkali carbonates to $Na_4SiO_4$ enhances $CO_2$ capture performance, especially at low temperatures, through the formation of $C_2O_5^{2-}$ species. This has been confirmed by in situ Raman spectroscopy and supported by DFT calculations, providing a strong basis for developing improved $CO_2$ capture technologies [28].

The study of defect processes in materials is a crucial aspect of materials science and engineering, as defects can significantly impact the physical, electrical, thermal, and mechanical properties of materials. Doping is a versatile and essential process in materials science, enabling the fine-tuning of material properties for a wide range of applications. Advances in doping techniques continue to drive innovation in electronics, optoelectronics, photovoltaics, and many other fields. Understanding and controlling doping processes is key to developing next-generation materials and devices. Na-ion diffusion is a complex but critical process in the development of Na-ion batteries and other sodium-based technologies. A deep understanding of the mechanisms, pathways, and influencing factors is essential for designing materials with optimal performance. Continued research, combining experimental studies with computational modeling, will be key to overcoming current challenges and advancing the field of Na-ion diffusion in materials.

To delve deeper into assessing the viability of $Na_4SiO_4$ as a battery material, it is crucial to thoroughly investigate additional properties such as defect energy, dopant energy, and ion migration. Conducting theoretical calculations can be challenging due to several factors including the complexity of the system and experimental validation. To overcome this obstacle, atomistic simulation studies have been previously utilized on {Kumar Prajapati, 2023 #6}to comprehensively ascertain and comprehend these properties [29–34].

In this study, we use atomistic simulation studies based on the classical pairwise potential to elucidate the defect, diffusion, and dopant properties of $Na_4SiO_4$.

## 2. Computational Methods

All calculations were performed using the classical pairwise potential simulation code GULP (General Utility Lattice Program) [35]. GULP is a computational tool used for modeling and simulating the properties of materials, particularly those with crystalline structures. It enables the calculation of various properties of materials, such as lattice dynamics, defect properties, and thermodynamic properties, using different interaction models and optimization algorithms. Interactions between ions in the crystal structure are modeled using long-range (Coulombic) and short-range (Pauli repulsion and van der Waals attraction) forces. Buckingham potentials (see Table 1) describe short-range repulsive forces. The BFGS algorithm (Broyden–Fletcher–Goldfarb–Shanno) is an iterative method for solving unconstrained nonlinear optimization problems. It is particularly well suited for problems where the function to be minimized (or maximized) is smooth. In the context of GULP, the BFGS algorithm is used to optimize the structure of a material by minimizing its potential energy [36]. In all relaxed configurations, the forces on all atoms

are smaller than 0.001 eV/Å. The Mott-Littleton method [37] is used to model point defects and migrating ions. The Mott-Littleton method is a well-established technique used in the modeling of point defects and ion migration in crystalline materials. The Mott-Littleton method divides the crystal into two regions to model defects effectively. Region I (Inner Region) is the immediate vicinity around the defect where atomic positions are significantly displaced due to the presence of the defect. In this region, the interactions between atoms and the defect are calculated explicitly. Typically, this region is spherical, and the defect is located at its center. Region II (Outer Region) extends beyond Region I and is where the defect's influence diminishes. The atoms in Region II are treated using continuum or semi-continuum approaches, where displacements are assumed to be small and can be described using linear elasticity theory or other approximations. Sodium-ion migration is calculated by considering seven interstitial points with equal intervals between neighboring Sodium sites. Defect energies of migrating ions at seven points along the diffusion path will be determined. The midpoint between two adjacent Na vacancy sites is the defect calculation center to reduce systematic errors. The energy difference between the maximum local energy associated with the saddle point along this diffusion path and the lowest Na vacancy formation energy will be calculated and reported as activation energy. Ions are modeled using this method as spherical objects with a full charge at the diluted limit. Defective energies are therefore likely to be overstated. However, relative energies will continue to trend in the same direction. The core-shell technique was used to model the polarization of ions. In earlier research [38,39], we described the formula for determining migratory paths and detailed activation energies of migration.

Table 1. Buckingham potential parameters used in the atomistic simulations of Na₄SiO₄ [40-42]. Two-body ($\Phi_{ij} (r_{ij}) = A_{ij} \exp (-r_{ij} / \rho_{ij}) - C_{ij}/r_{ij}^{6}$) where $A$, $\rho$, and $C$ are parameters reproducing the experimental data. The values of Y and K are shell charges and spring constants, respectively.

<table>
<thead>
<tr>
<th>Interaction</th>
<th>A/eV</th>
<th>ρ/Å</th>
<th>C/eV·Å⁶</th>
<th>Y/e</th>
<th>K/eV·Å⁻²</th>
</tr>
</thead>
<tbody>
<tr>
<td>Na⁺-O²⁻</td>
<td>1497.830598</td>
<td>0.287483</td>
<td>0.00</td>
<td>1.00</td>
<td>99,999</td>
</tr>
<tr>
<td>Si⁴⁺-O²⁻</td>
<td>1283.91</td>
<td>0.32052</td>
<td>10.66</td>
<td>4.00</td>
<td>99,999</td>
</tr>
<tr>
<td>O²⁻-O²⁻</td>
<td>22,764.30</td>
<td>0.1490</td>
<td>27.88</td>
<td>−2.86</td>
<td>61.50</td>
</tr>
</tbody>
</table>

## 3. Results and Discussion

### 3.1. Modelling of Na₄SiO₄ Crystal Structure

Na₄SiO₄ shows a triclinic structure with the P-1 space group according to the X-ray diffraction pattern derived by Baur et al. [23] (CIF file name: ICSD_CollCode62594). This study further explains that it consists of 24 atoms (8 Na, 2 Si, and 14 O) in a unit cell (2 formula units) with the lattice parameter found in the x, y, and z directions as $\mathrm{a}=5.58\ \mathring{\mathrm{A}}, \mathrm{b}=5.58\ \mathring{\mathrm{A}},$ and $\mathrm{c}=8.39\ \mathring{\mathrm{A}}$ and $\alpha=80.92^{\circ}, \beta=71.84^{\circ},$ and $\gamma=67.44^{\circ}$. Si atoms are coordinated with four oxygen atoms, forming a tetrahedral structure (see Figure 1). This tetrahedral coordination is a fundamental building block of many silicate structures, including quartz, feldspar, and various other minerals. To ensure the reliability of the classical potentials used in the study, a critical step is to validate these potentials against experimental data. This involves performing full geometry optimization of the crystal structure and comparing the calculated equilibrium lattice constants with experimentally determined values. The calculated lattice constants closely match the experimental values reported (see Table 2).

![](./images/1029607458831597571_3.jpg)

Figure 1. Crystal structure of $Na_4SiO_4$.

<table>
<caption>Table 2. Calculated and experimental lattice parameters of $Na_4SiO_4$.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Calculated</th>
<th>Experiment [23]</th>
<th>|Δ| %</th>
</tr>
</thead>
<tbody>
<tr>
<td>a (Å)</td>
<td>5.56</td>
<td>5.58</td>
<td>0.33</td>
</tr>
<tr>
<td>b (Å)</td>
<td>5.62</td>
<td>5.58</td>
<td>0.77</td>
</tr>
<tr>
<td>c (Å)</td>
<td>8.39</td>
<td>8.39</td>
<td>0.07</td>
</tr>
<tr>
<td>α (°)</td>
<td>81.34</td>
<td>80.92</td>
<td>0.52</td>
</tr>
<tr>
<td>β (°)</td>
<td>71.87</td>
<td>71.84</td>
<td>0.04</td>
</tr>
<tr>
<td>γ (°)</td>
<td>67.02</td>
<td>67.44</td>
<td>0.62</td>
</tr>
</tbody>
</table>

### 3.2. Defect Energetics

In this section, we examine the energetics of important defect processes in $Na_4SiO_4$. To investigate the defect characteristics in $Na_4SiO_4$, we initially analyzed point defects, including vacancies and interstitials, separately. These calculations form the basis for understanding more complex defect structures such as Schottky and Frenkel defects, as well as anti-site defects where Na and Si swap their atomic positions. The Schottky defect energy in $Na_4SiO_4$ was calculated by determining the individual vacancy formation energies for four $Na^+$, one $Si^{4+}$, and four $O^{2-}$ ions and summing them. This approach ensures that the defect maintains the stoichiometry and charge neutrality of the crystal. A Frenkel defect involves the displacement of an ion from its lattice site to an interstitial site, creating a vacancy-interstitial pair. The energy required to form a Na Frenkel defect is the sum of the vacancy formation energy and the interstitial formation energy for $Na^+$. In $Na_4SiO_4$, anti-site defects involve Na and Si atoms swapping positions. For isolated anti-site defects, a single Na atom occupies a Si site, and a single Si atom occupies a Na site. For clustered anti-site defects, multiple pairs of Na and Si atoms swap positions. The following equations in Kröger-Vink notation [43] describe the Schottky, Frenkel, and anti-site defect processes.

$$\text{Na Frenkel} : \text{Na}_{\text{Na}}^{\text{X}} \rightarrow V_{\text{Na}}^{\prime} + \text{Na}_{\text{i}}^{\bullet} \tag{1}$$

$$\text{Si Frenkel} : \text{Si}_{\text{Si}}^{\text{X}} \rightarrow V_{\text{Si}}^{\prime\prime\prime\prime} + \text{Si}_{\text{i}}^{\bullet\bullet\bullet\bullet} \tag{2}$$

$$\text{O Frenkel} : \text{O}_{\text{O}}^{\text{X}} \rightarrow V_{\text{O}}^{\bullet\bullet} + \text{O}_{\text{i}}^{\prime\prime} \tag{3}$$

$$\text{Schottky} : 4\ \text{Na}_{\text{Na}}^{\text{X}} + \text{Si}_{\text{Si}}^{\text{X}} + 4\ \text{O}_{\text{O}}^{\text{X}} \rightarrow 4\ V_{\text{Na}}^{\prime} + V_{\text{Si}}^{\prime\prime\prime\prime} + 4\ V_{\text{O}}^{\bullet\bullet} + \text{Na}_4\text{SiO}_4 \tag{4}$$

$$\text{Na}_2\text{O Schottky} : 2\ \text{Na}_{\text{Na}}^{\text{X}} + \text{O}_{\text{O}}^{\text{X}} \rightarrow 2\ V_{\text{Na}}^{\prime} + V_{\text{O}}^{\bullet\bullet} + \text{Na}_2\text{O} \tag{5}$$

$$\text{SiO}_2\text{ Schottky} : \text{Si}_{\text{Si}}^{\text{X}} + 2\ \text{O}_{\text{O}}^{\text{X}} \rightarrow V_{\text{Si}}^{\prime\prime\prime\prime} + 2\ V_{\text{O}}^{\bullet\bullet} + \text{SiO}_2 \tag{6}$$

$$\mathrm{Na/Si\ anti-site(isolated)}: \mathrm{Na_{Na}^X + Si_{Si}^X \rightarrow Na_{Si}''' + Si_{Na}^{\bullet\bullet\bullet}} \tag{7}$$

$$\mathrm{Na/Si\ anti-site(cluster)}: \mathrm{Na_{Na}^X + Si_{Si}^X \rightarrow \left\{ Na_{Si}''' + Si_{Na}^{\bullet\bullet\bullet} \right\}^X} \tag{8}$$

Figure 2 demonstrates the individual defect reaction energies. The Na Frenkel defect has the lowest energy among the considered defect processes, with an energy of 1.34 eV per defect. This indicates that the Na ions in $\mathrm{Na_4SiO_4}$ have a relatively low barrier for forming Frenkel defects, facilitating Na-ion migration via vacancy-assisted mechanisms. The next most energetically favorable defect process after the Na Frenkel defect is the $\mathrm{Na_2O}$ Schottky defect (2.79 eV/defect). This defect involves the simultaneous creation of vacancies for two Na atoms and one O atom, effectively removing a $\mathrm{Na_2O}$ unit from the crystal lattice. This higher energy implies that the formation of such defects, and consequently the loss of $\mathrm{Na_2O}$, is only feasible at high temperatures. Isolated anti-site defects have a high energy cost, making them unstable. Due to the exoergic nature of the clustering process (clustering energy: $4.91 - 8.77 = -3.86$ eV), isolated anti-site defects tend to aggregate into clusters to achieve a lower energy state. This aggregation into clusters reflects a significant tendency for the system to favor clustered anti-site defects, which are more stable and energetically favorable compared to their isolated counterparts. Other Frenkel and Schottky defects have even higher formation energies, making them practically non-existent under typical conditions. The results indicate that Na Frenkel defects are the most energetically favorable and significant in $\mathrm{Na_4SiO_4}$. Due to their lower formation energy, they dominate the defect landscape and influence the material's behavior, particularly its ionic conductivity.

![](./images/1029607458831597571_4.jpg)

Figure 2. Defect energies of different defect processes in $\mathrm{Na_4SiO_4}$.

### 3.3. Na-Ion Migration
Examining sodium-ion diffusion pathways and activation energies is crucial for understanding the ionic conductivity of $\mathrm{Na_4SiO_4}$, especially in applications such as solid-state batteries. The direct experimental characterization of these pathways is challenging due to the complexity of the material's structure and the small scale of ion movements. Therefore, computational methods are often employed to simulate and analyze these diffusion pathways and activation energies. The lithium-ion migration path calculated in $\mathrm{LiFePO_4}$ using classical pair potentials was later exactly observed in high-temperature powder neutron diffraction and the maximum entropy method. The experiment visualized a curved one-dimensional chain for lithium motion with a Li-Li separation of $3.01$ Å along the [010] direction [44]. This finding emphasizes the accuracy of our simulation methods in predicting ion migration pathways.

Using current simulation techniques, we constructed the Na-ion diffusion channels with atomic-level activation energies. Seven local Na hops were identified (A, B, C, D, E,

F, and G) (see Figure 3). Hop A has a lower activation energy of 0.23 eV, indicating that it is a favorable and energetically accessible pathway for $Na^{+}$ ion migration. Hop B has a moderate activation energy, suggesting it is less favorable compared to Hop A but still relatively accessible (see Table 3). Hop C, with the lowest activation energy among the hops listed, makes it the most energetically favorable for $Na^{+}$ ion movement. Hop D has a moderate activation energy, making it less favorable than Hop A and C but more favorable than Hops D and F. This hop has a moderate activation energy, making it less favorable than Hop A and C but more favorable than Hops D and F. The Hop E pathway has the highest activation energy among the listed hops, indicating that it is the least favorable for $Na^{+}$ ion migration. Hop G has a moderate activation energy, suggesting that it is less favorable than Hop A and C but more favorable than Hop D and F. The energy profile diagrams (see Figure 4) are essential for understanding the activation energies associated with different sodium-ion $(Na^{+})$ diffusion pathways in $Na_{4}SiO_{4}$. These diagrams illustrate the energy barriers that $Na^{+}$ ions must overcome to move through the material, providing insights into the ease or difficulty of diffusion.

![](./images/1029607458831597571_5.jpg)

Figure 3. Seven different Na local hops considered for the long-range migration pathways.

Table 3. Local Na hops and their activation energies.

<table>
<thead>
<tr>
<th>Na-Na Hop</th>
<th>Distance (Å)</th>
<th>Activation Energy (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>3.14 Å</td>
<td>0.23</td>
</tr>
<tr>
<td>B</td>
<td>3.62Å</td>
<td>0.65</td>
</tr>
<tr>
<td>C</td>
<td>3.39 Å</td>
<td>0.03</td>
</tr>
<tr>
<td>D</td>
<td>3.89Å</td>
<td>0.73</td>
</tr>
<tr>
<td>E</td>
<td>3.29 Å</td>
<td>0.55</td>
</tr>
<tr>
<td>F</td>
<td>4.07Å</td>
<td>1.02</td>
</tr>
<tr>
<td>G</td>
<td>2.91 Å</td>
<td>0.62</td>
</tr>
</tbody>
</table>

We constructed and evaluated five promising long-range pathways by examining local $Na^{+}$ hops and their associated activation energies (see Figure 4 and Table 4). The most favorable long-range path with the lowest overall activation energy (0.55 eV) is $A\leftrightarrow C\leftrightarrow E\leftrightarrow A$. In this long-range migration, $Na^{+}$ ions migrate in the $ac$ plane. An overall activation energy of 0.73 eV for three long-range pathways suggests the presence of mechanisms or reactions in materials or processes where the energy barrier for these pathways is also relatively low, facilitating easier transition or movement over longer distances. A long-range diffusion pathway with an overall migration energy of 1.02 eV indicates a significant energy barrier that must be overcome for atoms or ions to move through a material over extended distances. This high barrier can impact the material's performance in various applications.

![](./images/1029607458831597571_6.jpg)

Figure 4. Energy profile diagrams calculated for different local Na hops.

<table>
<thead>
  <tr>
    <th>Long-Range Pathway</th>
    <th>Hop Activation Energies (eV)</th>
    <th>Overall Activation Energy (eV)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>A↔C↔E↔A</td>
    <td>0.23 ↔0.03↔0.55↔0.23</td>
    <td>0.55</td>
  </tr>
  <tr>
    <td>D↔E↔G↔D↔G</td>
    <td>0.73 ↔0.55↔0.62↔0.73↔0.62</td>
    <td>0.73</td>
  </tr>
  <tr>
    <td>A↔C↔E↔D↔G</td>
    <td>0.23 ↔0.03↔0.55↔0.73↔0.62</td>
    <td>0.73</td>
  </tr>
  <tr>
    <td>A↔B↔E↔G↔D↔G</td>
    <td>0.23 ↔0.65↔0.55↔0.62↔0.73↔0.62</td>
    <td>0.73</td>
  </tr>
  <tr>
    <td>A↔C↔E↔F↔A</td>
    <td>0.23 ↔0.03↔0.55↔1.02↔0.23</td>
    <td>1.02</td>
  </tr>
</tbody>
</table>

### 3.4. Solution of Dopants

Doping in battery materials is a strategic method to enhance various properties of the materials used in batteries, including their electrical conductivity, thermal stability, capacity, and cycle life. This process involves the intentional introduction of impurities (dopants) into the host material to improve its performance. When considering isovalent and aliovalent dopants in $Na_4SiO_4$, it is important to understand the impact these dopants have on the material's structure and properties. Isovalent dopants have the same valence as the ions they replace, whereas aliovalent dopants have a different valence, which can lead to charge imbalances that must be compensated for within the crystal structure. Buckingham potentials used for dopants are provided in the electronic Supplementary Materials (ESM).

#### 3.4.1. Monovalent Dopants

Monovalent dopants (M = Li, K, and Rb) in $Na_4SiO_4$ can alter its properties, including ionic conductivity and structural stability. Monovalent dopants have a single positive charge and can substitute for $Na^+$ in the crystal lattice. The doping process is described by the following equation:

$$
\mathrm{M}_{2} \mathrm{O}+2 \mathrm{Na}_{\mathrm{Na}}^{\mathrm{X}} \rightarrow 2 \mathrm{M}_{\mathrm{Na}}^{\mathrm{X}}+\mathrm{Na}_{2} \mathrm{O} \tag{9}
$$

Endoergic (or endothermic) solution enthalpies calculated for all dopants mean that the process absorbs energy from the surroundings. This implies that adding dopants to $Na_4SiO_4$ requires thermal energy, and the process is more thermodynamically favorable at higher temperatures. Among the dopants considered, $K^+$ has the lowest solution enthalpy, meaning it requires the least amount of energy to be incorporated into $Na_4SiO_4$ (see Figure 5). This makes $K^+$ the most thermodynamically favorable dopant. A dopant with a size closer to that of the host ion will cause less distortion in the lattice. $K^+$, despite being larger, may fit into the $Na_4SiO_4$ lattice with less strain compared to other dopants, leading

to a more stable structure. This can be advantageous for practical doping processes as it suggests easier incorporation and potentially better stability.

![](./images/1029607458831597571_7.jpg)

Figure 5. Solution energies calculated for M₂O (M = Li, K, Rb).

### 3.4.2. Trivalent Dopants
Incorporating trivalent dopants on the silicon site in Na₄SiO₄ can introduce various structural and electronic modifications that may enhance the material's properties, such as ionic conductivity and stability. Substituting a $Si^{4+}$ ion with a trivalent ion ($M^{3+}$) introduces a negative charge in the lattice. This can be compensated for by creating oxygen vacancies or by incorporating additional sodium ions ($Na^{+}$) to maintain charge neutrality. The creation of oxygen vacancies can enhance ionic conductivity by providing pathways for ion migration. Additionally, extra sodium ions introduced for charge compensation can increase the number of mobile ions according to the following equation. In this study, a diverse array of trivalent dopants (M = Al, Ga, Gd, In, Sc, and Y) were examined for incorporation at the Si site.

$$
\mathrm{M}_{2} \mathrm{O}_{3}+2 \mathrm{Si}_{\mathrm{Si}}^{\mathrm{X}}+\mathrm{Na}_{2} \mathrm{O} \rightarrow 2 \mathrm{M}_{\mathrm{Si}}^{\prime}+2 \mathrm{Na}_{\mathrm{i}}^{\bullet}+2 \mathrm{SiO}_{2} \tag{10}
$$

Aluminum is the most promising trivalent dopant for improving Na₄SiO₄ due to its low solution energy and relatively small ionic radius (see Figure 6). The ionic radius of $Al^{3+}$ is relatively close to that of $Si^{4+}$. This similarity minimizes lattice distortions and strain when Al substitutes for Si. Minimal strain means the crystal structure remains stable and intact, making Al a favorable dopant. In previous simulation studies [45,46], Al has been reported to be the most promising dopant on the Si site in a variety of silicate materials. Gallium is also a promising dopant with the second lowest solution energy, indicating that it can also be incorporated into the Na₄SiO₄ lattice. Indium, despite having a larger ionic radius, has a solution energy slightly lower than Sc, but higher than Al and Ga, making it a moderately feasible dopant. Scandium, Yttrium, and Gadolinium, with higher solution energies and larger ionic radii, are less favorable for doping Na₄SiO₄. They introduce more significant lattice distortions and require more energy to incorporate, which may result in less effective enhancement of ionic conductivity.

![](./images/1029607458831597571_8.jpg)

Figure 6. Solution energies calculated for $M_2O_3$ (M = Al, Ga, In, Sc, Y, and Gd).

### 3.4.3. Tetravalent Dopants

Tetravalent dopants (M = Ge, Sn, Ti, and Ce) on the Si site in $Na_4SiO_4$ can be used to modify and enhance the material's properties while maintaining the charge balance, as they have the same +4 valence as silicon. The following reaction equation describes the following process:

$$\mathrm{MO}_{2}+\mathrm{Si}_{\mathrm{Si}}^{\mathrm{X}} \rightarrow \mathrm{M}_{\mathrm{Si}}^{\mathrm{X}}+\mathrm{SiO}_{2} \tag{11}$$

Germanium has the lowest solution energy, indicating that it is the easiest dopant to incorporate into the $Na_4SiO_4$ lattice (see Figure 7). The ionic radius of $Ge^{4+}$ (0.53 Å) is close to that of $Si^{4+}$ (0.40 Å), ensuring minimal lattice distortion. This makes $Ge^{4+}$ an excellent choice for doping, enhancing ionic conductivity, and maintaining structural integrity. Tin has a moderate solution energy, suggesting that it is relatively easy to incorporate but not as easy as $Ge^{4+}$. $Sn^{4+}$ can be beneficial for certain applications, but its larger ionic radius (0.69 Å) compared to $Si^{4+}$ could introduce some lattice distortions. Titanium has a higher solution energy, making it more difficult to incorporate into the lattice. $Ti^{4+}$ has an ionic radius of 0.61 Å, which is larger than $Si^{4+}$, potentially causing lattice distortions. However, $Ti^{4+}$ can enhance mechanical properties. Cerium has the highest solution energy, indicating the greatest difficulty in incorporating it into the lattice. $Ce^{4+}$ has a larger ionic radius, which can lead to significant lattice distortions. It may provide unique properties but is less favorable due to its high solution energy.

![](./images/1029607458831597571_9.jpg)

Figure 7. Solution energies calculated for $MO_2$ (M = Ge, Sn, Ti, and Ce).

### 4. Conclusions

In this study, we used atomistic simulation techniques to examine the defect, diffusion, and doping properties of a promising battery material, $Na_4SiO_4$. The Na Frenkel defect was found to be the most energetically favorable defect process facilitating vacancy-assisted Na-ion migration. Three-dimensional $Na^+$ ion diffusion is characterized by an activation energy of 0.55 eV. K and Ge are favorable dopants for the Na and Si sites in $Na_4SiO_4$ respectively. The doping of the Si site in $Na_4SiO_4$ with trivalent $Al^{3+}$ ions is favorable, generating additional $Na^+$ ions in the material. Experimental validation of these findings will be crucial in confirming their practical implications and optimizing $Na_4SiO_4$ for high-performance battery applications.

Supplementary Materials: The following supporting information can be downloaded at: https://www.mdpi.com/article/10.3390/cryst14080718/s1. Table S1: Buckingham potential parameters used for dopants in the atomistic simulations of $Na_4SiO_4$.

Author Contributions: Conceptualization, M.S.S.; methodology, M.S.S.; validation, P.A., P.I. and N.K.; formal analysis, M.S.S.; investigation, M.S.S.; writing—original draft preparation, N.K.; writing—review and editing, P.A.; supervision, P.A.; project administration. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: All data are provided either in the main article or in the electronic Supplementary Materials.

Acknowledgments: We acknowledge computational facilities provided by the Department of Chemistry, University of Jaffna, Sri Lanka, and Imperial College London, UK.

Conflicts of Interest: The authors declare no conflicts of interest.

### References

1.  Kim, T.; Song, W.; Son, D.-Y.; Ono, L.K.; Qi, Y. Lithium-ion batteries: Outlook on present, future, and hybridized technologies. *J. Mater. Chem. A* **2019**, 7, 2942–2964. [CrossRef]
2.  Panda, N.; Cueva-Sola, A.B.; Dzulqornain, A.M.; Thenepalli, T.; Lee, J.-Y.; Yoon, H.-S.; Jyothi, R.K. Review on lithium-ion battery recycling: Challenges and possibilities. *Geosystem Eng.* **2023**, 26, 101–118. [CrossRef]
3.  Goodenough, J.B.; Park, K.-S. The Li-Ion Rechargeable Battery: A Perspective. *J. Am. Chem. Soc.* **2013**, 135, 1167–1176. [CrossRef] [PubMed]
4.  Feng, X.; Ren, D.; Ouyang, M. Safety of lithium battery materials chemistry. *J. Mater. Chem. A* **2023**, 11, 25236–25246. [CrossRef]
5.  Grey, C.P.; Hall, D.S. Prospects for lithium-ion batteries and beyond—A 2030 vision. *Nat. Commun.* **2020**, 11, 6279. [CrossRef] [PubMed]
6.  Halder, P.; Bhattacharya, S. Battery Applications. In *Lithium Ion Glassy Electrolytes: Properties, Fundamentals, and Applications*; Bhattacharya, S., Bhattacharya, K., Eds.; Springer Nature: Singapore, 2022; pp. 159–173.
7.  Frith, J.T.; Lacey, M.J.; Ulissi, U. A non-academic perspective on the future of lithium-based batteries. *Nat. Commun.* **2023**, 14, 420. [CrossRef] [PubMed]
8.  Ralls, A.M.; Leong, K.; Clayton, J.; Fuelling, P.; Mercer, C.; Navarro, V.; Menezes, P.L. The Role of Lithium-Ion Batteries in the Growing Trend of Electric Vehicles. *Materials* **2023**, 16, 6063. [CrossRef] [PubMed]
9.  Kennedy, B.; Patterson, D.; Camilleri, S. Use of lithium-ion batteries in electric vehicles. *J. Power Sources* **2000**, 90, 156–162. [CrossRef]
10. Chen, W.; Liang, J.; Yang, Z.; Li, G. A Review of Lithium-Ion Battery for Electric Vehicle Applications and Beyond. *Energy Procedia* **2019**, 158, 4363–4368. [CrossRef]
11. Wu, H.; Hao, J.; Jiang, Y.; Jiao, Y.; Liu, J.; Xu, X.; Davey, K.; Wang, C.; Qiao, S.-Z. Alkaline-based aqueous sodium-ion batteries for large-scale energy storage. *Nat. Commun.* **2024**, 15, 575. [CrossRef]
12. Gupta, P.; Pushpakanth, S.; Haider, M.A.; Basu, S. Understanding the Design of Cathode Materials for Na-Ion Batteries. *ACS Omega* **2022**, 7, 5605–5614. [CrossRef] [PubMed]
13. Skundin, A.M.; Kulova, T.L.; Yaroslavtsev, A.B. Sodium-Ion Batteries (a Review). *Russ. J. Electrochem.* **2018**, 54, 113–152. [CrossRef]
14. Ferraro, M.; Tumminia, G. Techno-economics Analysis on Sodium-Ion Batteries: Overview and Prospective. In *Emerging Battery Technologies to Boost the Clean Energy Transition: Cost, Sustainability, and Performance Analysis*; Passerini, S., Barelli, L., Baumann, M., Peters, J., Weil, M., Eds.; Springer International Publishing: Berlin/Heidelberg, Germany, 2024; pp. 259–266.
15. Que, L.; Yu, F.; Wu, J.; Lan, Z.; Feng, Y.; Zhao, R.; Sun, Z.; Yang, Z.; Luo, H.; Chao, D. Unveil the origin of voltage oscillation for sodium-ion batteries operating at −40 °C. *Proc. Natl. Acad. Sci. USA* **2024**, 121, e2311075121. [CrossRef] [PubMed]

16. Mamoor, M.; Li, Y.; Wang, L.; Jing, Z.; Wang, B.; Qu, G.; Kong, L.; Li, Y.; Guo, Z.; Xu, L. Recent progress on advanced high energy electrode materials for sodium ion batteries. *Green Energy Resour.* **2023**, *1*, 100033. [CrossRef]

17. Singh, B.; Wang, Z.; Park, S.; Gautam, G.S.; Chotard, J.-N.; Croguennec, L.; Carlier, D.; Cheetham, A.K.; Masquelier, C.; Canepa, P. A chemical map of NaSICON electrode materials for sodium-ion batteries. *J. Mater. Chem. A* **2021**, *9*, 281–292. [CrossRef]

18. Jayamkondan, Y.; Penki, T.R.; Nayak, P.K. Recent advances and challenges in the development of advanced positive electrode materials for sustainable Na-ion batteries. *Mater. Today Energy* **2023**, *36*, 101360. [CrossRef]

19. Bianchini, F.; Fjellvåg, H.; Vajeeston, P. First-principles study of the structural stability and electrochemical properties of Na₂MSiO₄ (M = Mn, Fe, Co and Ni) polymorphs. *Phys. Chem. Chem. Phys.* **2017**, *19*, 14462–14470. [CrossRef] [PubMed]

20. Zhu, L.; Li, L.; Wen, J.; Zeng, Y.-R. Structural stability and ionic transport property of NaMPO₄ (M = V, Cr, Mn, Fe, Co, Ni) as cathode material for Na-ion batteries. *J. Power Sources* **2019**, *438*, 227016. [CrossRef]

21. Strauss, F.; Rousse, G.; Sougrati, M.T.; Dalla Corte, D.A.; Courty, M.; Dominko, R.; Tarascon, J.-M. Synthesis, Structure, and Electrochemical Properties of Na₃MB₅O₁₀ (M = Fe, Co) Containing M²⁺ in Tetrahedral Coordination. *Inorg. Chem.* **2016**, *55*, 12775–12782. [CrossRef]

22. Sivakumaran, A.; Samson, A.J.; Bristi, A.A.; Surendran, V.; Butler, S.; Reid, S.; Thangadurai, V. High ionic conducting rare-earth silicate electrolytes for sodium metal batteries. *J. Mater. Chem. A* **2023**, *11*, 15792–15801. [CrossRef]

23. Baur, W.H.; Halwax, E.; Völlenkle, H. Comparison of the crystal structures of sodium orthosilicate, Na₄SiO₄, and sodium orthogermanate, Na₄GeO₄. *Monatshefte Chem./Chem. Mon.* **1986**, *117*, 793–797. [CrossRef]

24. Ling, C.; Luo, X.; Wang, Z.; Tang, Z. Experimental and DFT study of Na₄SiO₄ doped with oxysalts for high-temperature CO₂ capture. *Chem. Eng. J.* **2024**, *495*, 153331. [CrossRef]

25. Ling, C.; Wang, Z.; Tang, Z. Performance improvement of Na₄SiO₄ doped with Li₂CO₃-K₂CO₃ for high-temperature CO₂ capture and thermochemical energy storage. *Chem. Eng. J.* **2023**, *476*, 146921. [CrossRef]

26. Plascencia-Hernández, F.; Araiza, D.G.; Pfeiffer, H. Effect of Sodium Ortho and Pyrosilicates (Na₄SiO₄-Na6Si₂O₇) Mixture during the CO2 Chemical Capture Performance. *Ind. Eng. Chem. Res.* **2022**, *61*, 11012–11024. [CrossRef]

27. Wang, Z.; Sun, C.; Xu, Q.; Zou, X.; Cheng, H.; Lu, X. In Situ XRD, Raman Characterization, and Kinetic Study of CO₂ Capture by Alkali Carbonate-Doped Na₄SiO₄. *Separations* **2022**, *9*, 428. [CrossRef]

28. Liu, J.; Wang, Z.; Wang, Z.; Song, J.; Li, G.; Xu, Q.; You, J.; Cheng, H.; Lu, X. Alkali carbonates promote CO₂ capture by sodium orthosilicate. *Phys. Chem. Chem. Phys.* **2019**, *21*, 13135–13143. [CrossRef] [PubMed]

29. Aparicio, P.A.; Dawson, J.A.; Islam, M.S.; de Leeuw, N.H. Computational Study of NaVOPO₄ Polymorphs as Cathode Materials for Na-Ion Batteries: Diffusion, Electronic Properties, and Cation-Doping Behavior. *J. Phys. Chem. C* **2018**, *122*, 25829–25836. [CrossRef]

30. Kuganathan, N.; Kordatos, A.; Anurakavan, S.; Iyngaran, P.; Chroneos, A. Li₃SbO₄ lithium-ion battery material: Defects, lithium ion diffusion and tetravalent dopants. *Mater. Chem. Phys.* **2019**, *225*, 34–41. [CrossRef]

31. Kumar Prajapati, A.; Bhatnagar, A. A review on anode materials for lithium/sodium-ion batteries. *J. Energy Chem.* **2023**, *83*, 509–540. [CrossRef]

32. Goldmann, B.A.; Clarke, M.J.; Dawson, J.A.; Islam, M.S. Atomic-scale investigation of cation doping and defect clustering in the anti-perovskite Na₃OCl sodium-ion conductor. *J. Mater. Chem. A* **2022**, *10*, 2249–2255. [CrossRef]

33. Ahiavi, E.; Dawson, J.A.; Kudu, U.; Courty, M.; Islam, M.S.; Clemens, O.; Masquelier, C.; Famprikis, T. Mechanochemical synthesis and ion transport properties of Na₃OX (X = Cl, Br, I and BH₄) antiperovskite solid electrolytes. *J. Power Sources* **2020**, *471*, 228489. [CrossRef]

34. Islam, M.S.; Fisher, C.A.J. Lithium and sodium battery cathode materials: Computational insights into voltage, diffusion and nanostructural properties. *Chem. Soc. Rev.* **2014**, *43*, 185–204. [CrossRef]

35. Gale, J.D. GULP: A computer program for the symmetry-adapted simulation of solids. *J. Chem. Soc. Faraday Trans.* **1997**, *93*, 629–637. [CrossRef]

36. Gale, J.D.; Rohl, A.L. The General Utility Lattice Program (GULP). *Mol. Simul.* **2003**, *29*, 291–341. [CrossRef]

37. Mott, N.F.; Littleton, M.J. Conduction in polar crystals. I. Electrolytic conduction in solid salts. *Trans. Faraday Soc.* **1938**, *34*, 485–499. [CrossRef]

38. Kuganathan, N.; Rushton, M.J.D.; Grimes, R.W.; Kilner, J.A.; Gkanas, E.I.; Chroneos, A. Self-diffusion in garnet-type Li₇La₃Zr₂O₁₂ solid electrolytes. *Sci. Rep.* **2021**, *11*, 451. [CrossRef] [PubMed]

39. Kuganathan, N.; Ganeshalingam, S.; Chroneos, A. Defects, Diffusion, and Dopants in Li₂Ti₆O₁₃: Atomistic Simulation Study. *Materials* **2019**, *12*, 2851. [CrossRef]

40. Kuganathan, N.; Solovjov, A.L.; Vovk, R.V.; Chroneos, A. Defects, diffusion and dopants in Li₈SnO₆. *Heliyon* **2021**, *7*, e07460. [CrossRef]

41. Heath, J.; Chen, H.; Islam, M.S. MgFeSiO₄ as a potential cathode material for magnesium batteries: Ion diffusion rates and voltage trends. *J. Mater. Chem. A* **2017**, *5*, 13161–13167. [CrossRef]

42. Pedone, A.; Gambuzzi, E.; Malavasi, G.; Menziani, M.C. First-principles simulations of the ²⁷Al and ¹⁷O solid-state NMR spectra of the CaAl₂Si₃O₁₀ glass. *Theor. Chem. Acc.* **2012**, *131*, 1147. [CrossRef]

43. Kröger, F.A.; Vink, H.J. Relations between the Concentrations of Imperfections in Crystalline Solids. In *Solid State Physics*; Seitz, F., Turnbull, D., Eds.; Academic Press: Cambridge, MA, USA, 1956; Volume 3, pp. 307–435.

44. Fisher, C.A.J.; Hart Prieto, V.M.; Islam, M.S. Lithium Battery Materials $\text{LiMPO}_4$ (M = Mn, Fe, Co, and Ni): Insights into Defect Association, Transport Mechanisms, and Doping Behavior. *Chem. Mater.* **2008**, *20*, 5907–5915. [CrossRef]

45. Islam, M.S.; Dominko, R.; Masquelier, C.; Sirisopanaporn, C.; Armstrong, A.R.; Bruce, P.G. Silicate cathodes for lithium batteries: Alternatives to phosphates? *J. Mater. Chem.* **2011**, *21*, 9811–9818. [CrossRef]

46. Jones, A.; Slater, P.R.; Islam, M.S. Local Defect Structures and Ion Transport Mechanisms in the Oxygen-Excess Apatite $\text{La}_{9.67}(\text{SiO}_4)_6\text{O}_{2.5}$. *Chem. Mater.* **2008**, *20*, 5055–5060. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.