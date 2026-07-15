# Understanding the Self-Healing Electrostatic Shield Mechanism at the Lithium-Metal Anode Surface
Samuel Bertolini,* Arnaud Delcorte, and Pedro Venezuela

Cite This: *Chem. Mater.* 2024, 36, 8477-8487

Read Online

## ABSTRACT:
Lithium−metal anodes, with their impressive high specific capacity of approximately 3860 mAh/g, emerge as a promising alternative to Li-ion anodes. However, when subjected to higher recharge currents for accelerated battery charging, dendrites tend to form on the Li-metal surface. These dendrites can puncture the separator, leading to short circuits upon contact with the positive electrode. Such short circuits in a nonaqueous solvent can trigger runaway reactions, which raises safety concerns. In an effort to limit dendrite formation on the lithium−metal anode, the “self-healing” electrostatic shield mechanism (SHES) incorporates a small fraction of cesium salts in the electrolyte. These cesium ions remain charged on the surface, migrating toward the dendrites. The migration of Cs-ions to the dendrite surface creates a charged shield that compels lithium ions to deposit outside the dendrites, preventing the dendrite’s undesirable growth. To delve deeper into the working of the SHES mechanism, this study specifically utilizes Li and Cs atoms in both solvated and non-solvated configurations. These atoms are employed to be adsorbed onto various sites of the Li slab surface. Density functional theory (DFT) calculations are employed to explore the adsorption energy of Cs ions on Li-metal and their relationship with dendrite formation. In the presence of the solid electrolyte interphase (SEI), Cs ions migrate to damaged areas, depositing over the exposed bare metal surface and grain boundaries. When the SEI breaks, Cs ions cover the exposed Li surface, creating a positively charged shield in the exposed area, thereby reducing the pathway for Li plating and subsequent dendrite growth.

![](./images/1055798861840252942_1.jpg)

## INTRODUCTION
Lithium-ion batteries (LIBs) are commonly employed for energy storage in devices like laptops and cell phones. Nevertheless, as the demand for higher capacity in electric mobility rises and LIBs are approaching their capacity limits, a potential alternative to replace LIBs is the use of lithium−metal batteries (LMBs), which boast a superior specific capacity compared to the graphite found in LIBs (3860 mAh/g vs 370 mAh/g). $^{1−6}$ Despite this advantage, the safety of LMBs needs enhancement by mitigating or eliminating hazardous reactions resulting from dendrite growth. $^{7−10}$

In LMBs, the electrolyte undergoes reactions with the exposed metal surface due to the narrow stability window of both the electrodes and electrolyte, coupled with the negative redox potential of lithium metal. Consequently, this leads to the degradation of the electrolyte and consumption of the anode, as the chemical potential of the anode exceeds the lowest unoccupied molecular orbital (LUMO) of the electrolyte. Similarly, the cathode interacts with the electrolyte when the chemical potential of the cathode falls below the highest occupied molecular orbital (HOMO). $^{11}$ Within the lithium−metal anode, these reactions result in the decomposition of electrolyte molecules, giving rise to the formation of a solid film comprising various species known as the solid-electrolyte interphase (SEI). The SEI spontaneously forms upon contact with the electrolyte and during the charge and discharge cycles. A robust SEI can passivate the surface, permitting the transportation of lithium ions through this protective film. The structure of the SEI is influenced by operational factors such as electrolyte composition, temperature, type of anode, voltage profile, and more. The SEI is composed of inorganic and organic components from the decomposition of the solvent, the SEI commonly features the formation of $Li_2O$, LiF, $Li_2CO_3$, and $Li_2S$ in the inorganic structure, alongside elastomers in the organic structure. $^{12−23}$ One effective strategy to prevent dendrite formation involves modifying the electrolyte composition to engineer the SEI.

Aurbach $^{24}$ suggested that the inorganic layer is the initial component to form in the solid-electrolyte interphase (SEI). As a consequence of continuous reduction, lower oxidized species may emerge near the lithium−metal surface, including insoluble salts. The dissolution of lithium accelerates reactions

Received: June 7, 2024
Revised: August 19, 2024
Accepted: August 20, 2024
Published: August 29, 2024

![](./images/1055798861840252942_2.jpg)

© 2024 American Chemical Society
8477
https://doi.org/10.1021/acs.chemmater.4c01601
*Chem. Mater.* 2024, 36, 8477−8487

between lithium and electrolyte species. In the presence of an electric field, this results in the dissolution or deposition of ions on the anode, inducing morphological changes. If the SEI fails to accommodate these changes during the charge or discharge process, it may fracture, revealing the exposed metallic phase. Preferential deposition of lithium ions occurs in these exposed areas, leading to the growth of dendrites. In the model proposed by Lu et al.,²⁵ lithium diffuses through the electrolyte, forming a phase adhered to the anode. This phase contains not only the products of reactions between the electrolyte and the anode but also intact electrolyte molecules, resulting in a porous structure. This porous SEI exhibits an uneven distribution of lithium, creating hot spots due to an uneven electric field.²⁶ Consequently, it facilitates the preferential deposition of lithium ions at points with higher electric field intensity. The metallic lithium phase in this model undergoes consumption by the electrolyte, causing the porous phase to expand and eventually leading to the clustering of lithium atoms.

Various strategies exist to mitigate dendrite formation. The self-healing approach involves expediting the formation of the solid-electrolyte interphase (SEI) by increasing the salt concentration in the electrolyte or incorporating salts that are highly reactive with the anode. In the event of SEI breakage, the self-healing mechanism enables a rapid electrolyte reaction with the exposed lithium phase, leading to the formation of a new SEI.²⁷,²⁸ Furthermore, engineering the SEI electrolyte can diminish polysulfide reactivity, enhance Li-ion conductivity, and better accommodate morphological changes.²⁹ This can be achieved not only through self-healing but also by creating an artificial SEI or developing an SEI with improved characteristics, such as higher ionic conductivity.³⁰,³¹ In lithium-sulfur (Li−S) batteries, for instance, the SEI can be tailored to react with LiNO₃, producing Li₂SO₄, which safeguards the anode against polysulfide decomposition and dendrite formation.³² Alternatively, the shuttle of polysulfides to the lithium-anode can be minimized by implementing an active cathode material that can capture the polysulfides from the solvent, such as sulfurized polyacrylonitrile (SPAN).³³⁻³⁷ Additionally, modifying the solvent for the SEI can promote elastomer formation, enabling better accommodation of morphological changes on the anode.³⁸⁻⁴⁰ The solvent nature has an important effect on the dendrite formation, Vlad et al. observed a reduction in dendrite formation by using dimethyl 2,5-dioxahexanedioate (DMDOHD) as solvent,⁴¹ while the same effect was observed by increasing the salt concentration.⁴²,⁴³ The main mechanism to engineer the SEI against dendrite growth can be summarized as modifying the electrolyte, using an artificial SEI, or controlling the initial charge/discharge process.⁴⁴ Dendrite prevention can also be achieved through pulse charging of the electric field,⁴⁵ adoption of solid-state electrolytes, or the use of polymers covering the anode that mechanically hinder dendrite growth. While polymers as electrolytes facilitate Li-ion diffusion and reduce dendrite formation, their lithium diffusion is slower compared to liquid electrolytes.⁴⁶⁻⁵⁰

The self-healing electrostatic shield mechanism (SHES), a significant technique pioneered by Ding et al.,⁵¹,⁵² involves manipulating the reduction potential of a cation (e.g., cesium) to be lower than that of lithium, as dictated by the Nernst equation. This shift is achieved by altering the ion's activity in the electrolyte when it is at low concentration. These cations, unable to deposit as a metal or form thin layers with lithium alloys, act as a protective measure when an electric field is applied to the battery during recharging. As voltage is applied to the circuit, these cations cover the dendrites, maintaining a positive charge on the surface. This positive shield repels lithium ions, preventing their deposition on the dendrites. Consequently, lithium ions deposit in alternative regions, facilitating the healing of existing dendrite surfaces and preventing the formation of new dendrites.

To facilitate the expansion of the bulk lithium (Li) anode, solvated Li-ions in the electrolyte must adhere to a surface, shed their solvents, and capture an electron originating from the bulk electrode. This sequence enables the accumulation and reduction of Li ions. The electric field generated during the charging process aids in concentrating the ions within a specific region, preventing dispersion and solvation. Since the charging mechanism involves the accumulation and reduction of ions on the anode surface, diffusion becomes a crucial factor in metal electrode materials.⁵³⁻⁵⁷ As a result, the migration of Li-metal and Li-ion atoms on the surface governs the deposition process in the Li-metal anode. Dendrite growth occurs when there is a favored direction for atoms to deposit, which may be a specific site or surface.⁵⁸ The direction of dendrite growth in metals tends to align with the lattice symmetry and growth planes, with lower atomic planar density and larger interplanar distances favoring dendrite growth.⁵⁹⁻⁶² Surface energy plays a pivotal role in determining the direction of dendrite growth, and the kinetics are linked to the dissipation of energy between the solid and liquid phases.⁶³⁻⁶⁹

Density functional theory (DFT) calculations are able to simulate the phenomenon of dendrite growth due to the intricate processes involving the electrolyte's decomposition on the exposed lithium surface, leading to the formation of a solid-electrolyte interphase (SEI), as well as the diffusion of Li ions on the SEI.¹⁶,⁷⁰⁻⁷² To shed light on why dendrites tend to grow more readily in lithium anodes compared to magnesium anodes and to explore the impact of the electric field, Groß et al.⁷³,⁷⁴ employed DFT calculations focusing on the bare phase. In our current study, we aim to unravel the mechanism of the Self-Healing Electrostatic Shield (SHES) through first-principles calculations, with the goal of elucidate the potential occurrence of the SHES mechanism. In our model, we are focus on the adsorption energy of Cs and Li atoms, as the driving force for surface structure formation, considering the explicit presence of solvents to induce charge in the Cs and Li atoms, as in a double layer. Consequently, we investigating whether cesium (Cs) atoms can cover dendrites, establishing a positive electrostatic shield on the surface to repel lithium-ion deposition and assessing whether Cs can diminish irregularities on the SEI. Additionally, we include the explicit calculations of Li/Cs ions solvated by the electrolyte in our analysis.

### COMPUTATIONAL METHODS
In this study, we aim to understand the self-healing electrostatic shield (SHES) mechanism by examining the specific sites where cesium deposition occurs over the anode under various conditions and analyzing the electron distribution within the system. The calculations of these structures were conducted through first-principles calculations, employing Density Functional Theory (DFT)⁷⁵,⁷⁶ and utilizing the Vienna Ab-initio Simulation Package (VASP)⁷⁷,⁷⁸ within the plane-wave basis set approach.⁷⁹,⁸⁰ A Monkhorst−Pack k-point mesh⁸¹ with a 2 × 2 × 1 grid was employed for Brillouin zone (BZ) sampling in every configuration, and the cutoff energy was set at 400 eV. Electron−ion interactions were modeled using PAW pseudopotentials⁸²,⁸³ from the VASP databases. Ionic relaxation was achieved

through a conjugate-gradient algorithm to attain their ground state configuration, and Gaussian smearing with a width of 0.05 eV was applied. Convergence criteria for self-consistent electronic iteration and ionic force were set to $10^{-4}$ eV and $10^{-3}$ eV/Å, respectively. The lithium lattice parameter calculated was 3.442 Å, aligning with experimental observations,⁸⁴,⁸⁵ and the bottom and top surfaces were separated by a vacuum of 15 Å. Additionally, charge analysis was performed using Bader calculations.⁸⁶⁻⁸⁸

Table 1 presents the cell parameters for various sites of adsorption. Each layer is defined as the atoms belonging to a plane parallel to the

<table>
<caption>Table 1. Slab Parameters of Different Absorption Sites Over the Lithium−Metal Anode, Including Various Configurations Such as the Bare Surface, Solid Electrolyte Interphase (SEI), and Grain Boundary of the SEI</caption>
<thead>
  <tr>
    <th>site or structure location</th>
    <th>cleavage surface and defect</th>
    <th>cell size (Å)</th>
    <th>#frozen Li layers</th>
    <th>#total Li layers</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="5">first atom adsorption</td>
    <td>100</td>
    <td>10.3 × 10.3</td>
    <td>3</td>
    <td>7</td>
  </tr>
  <tr>
    <td>110</td>
    <td>10.3 × 9.7</td>
    <td>3</td>
    <td>7</td>
  </tr>
  <tr>
    <td>320 (ledge)</td>
    <td>10.3 × 12.4</td>
    <td>9</td>
    <td>32</td>
  </tr>
  <tr>
    <td>320 (step)</td>
    <td>13.7 × 24.8</td>
    <td>5</td>
    <td>26</td>
  </tr>
  <tr>
    <td>531</td>
    <td>16.9 × 16.9</td>
    <td>7</td>
    <td>28</td>
  </tr>
  <tr>
    <td rowspan="3">Cs adatom</td>
    <td>substitute</td>
    <td>17.2</td>
    <td>---</td>
    <td>---</td>
  </tr>
  <tr>
    <td>100</td>
    <td>20.6 × 20.6</td>
    <td>3</td>
    <td>7</td>
  </tr>
  <tr>
    <td>110</td>
    <td>20.6 × 19.5</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>second atom adsorption</td>
    <td>100</td>
    <td>20.6 × 20.6</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>third atom adsorption</td>
    <td>110</td>
    <td>20.6 × 19.5</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Cs monolayer</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SEI</td>
    <td>100</td>
    <td>20.6 × 20.6</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>broken SEI</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>grain boundary</td>
    <td></td>
    <td>28.6 × 10.2</td>
    <td></td>
    <td>6</td>
  </tr>
</tbody>
</table>

cleavage surface. To assess the energy barrier for the diffusion of cesium across a lithium metal surface and the diffusion of Li ions over a monolayer of cesium deposited on the lithium−metal anode, the climb-image Nudged Elastic Band (cNEB) method⁸⁹ was employed to investigate diffusion path, and the structures of the images were optimized with a force convergence threshold set at 30 meV/Å.

### RESULTS AND DISCUSSION

To comprehend the deposition of Cs on the Li-metal surface, the adsorption energy of Li and Cs on the anode surface was determined using eq 1, where E_ads represents the adsorption energy, $E_{sys}$ is the system’s energy, $E_{slab}$ is the slab’s energy, and $E_{MI}$ is the energy of the metal atom. The references for calculating $E_{MI}$ include: 1) a metal atom in the gas phase; 2) a metal atom in bulk metal; and 3) the metal atom solvated by two DOL molecules (adsorption of Li-ion). The corresponding $E_{ads}$ values are detailed in Tables 2−4. Bulk energies were computed per atom from supercells containing 16 atoms each, with Body-Centered Cubic (BCC) lattice parameters set at 6.88 and 12.35 Å for Li and Cs, respectively. The configurations of the slabs are provided in Table 1. When the adsorption calculations are performed on neutral systems, and therefore adding a metallic atom, it is referred to as “reduced”, irrespective of whether it comes from a gas or bulk phase reference (e.g., Cs-reduced in reference 1 and 2).

<table>
<caption>Table 2. Adsorption Energy of the First Atom on the Anode Surface and Energy of Cs Substitution in Li-Bulk Phase<sup>a</sup></caption>
<thead>
  <tr>
    <th>Atoms adsorbed</th>
    <th>cleavage surface</th>
    <th>System</th>
    <th>Eads gas ion (eV)</th>
    <th>Eads bulk (eV)</th>
    <th>Eads ion (eV)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Li</td>
    <td>100</td>
    <td>adatom</td>
    <td>-1.609</td>
    <td>0.259</td>
    <td>-1.704</td>
  </tr>
  <tr>
    <td>Li</td>
    <td>110</td>
    <td>adatom</td>
    <td>-1.710</td>
    <td>0.158</td>
    <td>-1.959</td>
  </tr>
  <tr>
    <td>Li</td>
    <td>320</td>
    <td>ledge</td>
    <td>-1.791</td>
    <td>0.077</td>
    <td>-1.819</td>
  </tr>
  <tr>
    <td>Li</td>
    <td>531</td>
    <td>kink</td>
    <td>-1.831</td>
    <td>0.037</td>
    <td>-1.691</td>
  </tr>
  <tr>
    <td>Li</td>
    <td>320</td>
    <td>step</td>
    <td>-1.977</td>
    <td>-0.109</td>
    <td>-1.896</td>
  </tr>
  <tr>
    <td>Li</td>
    <td>110</td>
    <td>terrace</td>
    <td>-1.941</td>
    <td>-0.074</td>
    <td>-1.809</td>
  </tr>
  <tr>
    <td>Li</td>
    <td>100</td>
    <td>terrace</td>
    <td>-2.142</td>
    <td>-0.275</td>
    <td>-1.814</td>
  </tr>
  <tr>
    <td colspan="6" style="background:#8dd3c7;">1st Li adsorption sites on the anode</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>---</td>
    <td>substitute</td>
    <td>-0.264</td>
    <td>0.545</td>
    <td>---</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>100</td>
    <td>adatom</td>
    <td>-1.194</td>
    <td>-0.385</td>
    <td>-1.284</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>110</td>
    <td>adatom</td>
    <td>-1.229</td>
    <td>-0.412</td>
    <td>-1.552</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>320</td>
    <td>ledge</td>
    <td>-1.361</td>
    <td>-0.552</td>
    <td>-1.516</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>531</td>
    <td>kink</td>
    <td>-1.346</td>
    <td>-0.537</td>
    <td>-1.512</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>320</td>
    <td>step</td>
    <td>-1.429</td>
    <td>-0.620</td>
    <td>-1.599</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>110</td>
    <td>terrace</td>
    <td>-1.370</td>
    <td>-0.562</td>
    <td>-1.534</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>100</td>
    <td>terrace</td>
    <td>-1.502</td>
    <td>-0.693</td>
    <td>-1.627</td>
  </tr>
  <tr>
    <td colspan="6" style="background:#8dd3c7;">1st Cs adsorption sites on the anode</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>100</td>
    <td>hole</td>
    <td>-1.194</td>
    <td>-0.385</td>
    <td>-1.284</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>100</td>
    <td>bridge</td>
    <td>-1.190</td>
    <td>-0.382</td>
    <td>-1.280</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>100</td>
    <td>top</td>
    <td>-1.187</td>
    <td>-0.379</td>
    <td>-1.260</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>110</td>
    <td>bridge1</td>
    <td>-1.222</td>
    <td>-0.414</td>
    <td>-1.547</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>110</td>
    <td>bridge2</td>
    <td>-1.217</td>
    <td>-0.409</td>
    <td>-1.524</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>110</td>
    <td>hole</td>
    <td>-1.220</td>
    <td>-0.412</td>
    <td>-1.537</td>
  </tr>
  <tr>
    <td>Cs</td>
    <td>110</td>
    <td>top</td>
    <td>-1.229</td>
    <td>-0.420</td>
    <td>-1.552</td>
  </tr>
  <tr>
    <td colspan="6" style="background:#8dd3c7;">Cs adatom sites on the anode</td>
  </tr>
</tbody>
</table>

<sup>a</sup>The first column represents the adsorbed element (Li or Cs), the second column represents the cleavage on the bulk Li to generate the slab surface, and the third column represents the surface defect type. The fourth, fifth, and sixth columns represent the adsorption energy of the respective calculation in different references, as gas phase, as bulk phase, and as solvated ions.

However, when the metal atom is solvated by one or two DOL molecules, it is termed as “ion” (e.g., Li-ion in reference 3). The optimized configuration of the adsorbed reduced atom systems is used as the initial state configuration for ion-atom adsorption, achieved by adding the solvent. The systems containing the ion are optimized to ensure that the DOL molecules solvate only one atom, as depicted in the schematic Figure S1.

$$
E_{\text{ads}} = E_{\text{sys}} - E_{\text{slab}} - E_{\text{MI}} \tag{1}
$$

To discern the preferable deposition sites for Cs and Li, the initial adsorption was conducted at adatom, ledge, kink, step, and terrace sites. For each site, the lithium−metal anode was cleaved in various orientations, as detailed in Table 1, and the adsorbed atom was placed in the corresponding site subsequently, the system underwent optimization. The adsorption of a second atom was computed to elucidate how a Cs or Li layer would expand over the Li-metal surface. To explore this, we altered the distance between the two adsorbed atoms on the <100> and <110> surfaces. To assess the stability of a Cs layer over the anode, the adsorption of three atoms (two Cs and one Li) was analyzed to determine whether Li prefers to intercalate between Cs atoms or deposit at the edge of a Cs layer on the <110> surface. Beyond the bare surface, the impact of the SEI was investigated by calculating Cs adsorption on an intact SEI, a damaged SEI, and a grain boundary.

The initial adsorption of Li-reduced suggests a preference for Li to occupy higher coordinated sites, such as terraces and

Table 3. Adsorption Energy of a Second Atom Over the Anode and in the Presence of Cesium

<table>
  <tbody>
    <tr>
      <td>Atoms adsorbed</td>
      <td>cleavage surface</td>
      <td>System</td>
      <td>Eads gas (eV)</td>
      <td>Eads bulk Cs:M (eV)</td>
      <td>Eads ion (eV)</td>
      <td>distance gas (Å)</td>
      <td>distance Cs:M ion (Å)</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>100</td>
      <td>A</td>
      <td>-1.139</td>
      <td>-0.330</td>
      <td>-1.120</td>
      <td>6.358</td>
      <td>6.034</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>100</td>
      <td>B</td>
      <td>-1.136</td>
      <td>-0.327</td>
      <td>-1.279</td>
      <td>6.520</td>
      <td>5.920</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>100</td>
      <td>C</td>
      <td>-1.147</td>
      <td>-0.338</td>
      <td>-1.311</td>
      <td>7.313</td>
      <td>6.908</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>100</td>
      <td>D</td>
      <td>-1.170</td>
      <td>-0.361</td>
      <td>-1.322</td>
      <td>9.953</td>
      <td>10.038</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>110</td>
      <td>A</td>
      <td>-1.294</td>
      <td>-0.486</td>
      <td>-1.458</td>
      <td>9.728</td>
      <td>9.674</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>110</td>
      <td>B</td>
      <td>-1.271</td>
      <td>-0.462</td>
      <td>-1.187</td>
      <td>6.282</td>
      <td>5.727</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>110</td>
      <td>C</td>
      <td>-1.301</td>
      <td>-0.492</td>
      <td>-1.367</td>
      <td>6.463</td>
      <td>5.941</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>110</td>
      <td>D</td>
      <td>-1.297</td>
      <td>-0.488</td>
      <td>-1.451</td>
      <td>7.018</td>
      <td>6.881</td>
    </tr>
    <tr>
      <td>Cs-Cs</td>
      <td>110</td>
      <td>E</td>
      <td>-1.301</td>
      <td>-0.492</td>
      <td>-1.487</td>
      <td>10.223</td>
      <td>10.307</td>
    </tr>
    <tr>
      <td colspan="8">2nd adsorption of Cs sites on the anode</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>100</td>
      <td>A</td>
      <td>-1.639</td>
      <td>0.229</td>
      <td>-1.813</td>
      <td>4.428</td>
      <td>5.122</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>100</td>
      <td>B</td>
      <td>-1.619</td>
      <td>0.248</td>
      <td>-1.610</td>
      <td>4.904</td>
      <td>6.076</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>100</td>
      <td>C</td>
      <td>-1.584</td>
      <td>0.283</td>
      <td>-1.614</td>
      <td>6.975</td>
      <td>7.115</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>100</td>
      <td>D</td>
      <td>-1.585</td>
      <td>0.282</td>
      <td>-1.662</td>
      <td>9.859</td>
      <td>9.977</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>110</td>
      <td>A</td>
      <td>-2.019</td>
      <td>-0.152</td>
      <td>-1.648</td>
      <td>4.811</td>
      <td>4.717</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>110</td>
      <td>B</td>
      <td>-1.995</td>
      <td>-0.128</td>
      <td>-1.771</td>
      <td>4.903</td>
      <td>5.493</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>110</td>
      <td>C</td>
      <td>-1.910</td>
      <td>-0.042</td>
      <td>-1.966</td>
      <td>4.904</td>
      <td>6.245</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>110</td>
      <td>D</td>
      <td>-1.909</td>
      <td>-0.041</td>
      <td>-1.764</td>
      <td>8.244</td>
      <td>7.406</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>110</td>
      <td>E</td>
      <td>-1.910</td>
      <td>-0.043</td>
      <td>-1.822</td>
      <td>8.624</td>
      <td>8.738</td>
    </tr>
    <tr>
      <td>Cs-Li</td>
      <td>110</td>
      <td>F</td>
      <td>-1.892</td>
      <td>-0.024</td>
      <td>-1.810</td>
      <td>9.957</td>
      <td>9.818</td>
    </tr>
    <tr>
      <td colspan="8">Adsorption of Li sites on the anode in the presence of Cs</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>100</td>
      <td>A</td>
      <td>-1.667</td>
      <td>0.201</td>
      <td>-1.722</td>
      <td>3.231</td>
      <td>4.148</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>100</td>
      <td>B</td>
      <td>-1.601</td>
      <td>0.267</td>
      <td>-1.758</td>
      <td>3.899</td>
      <td>5.369</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>100</td>
      <td>C</td>
      <td>-1.583</td>
      <td>0.285</td>
      <td>-1.763</td>
      <td>6.918</td>
      <td>7.038</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>100</td>
      <td>D</td>
      <td>-1.587</td>
      <td>0.281</td>
      <td>-1.761</td>
      <td>10.003</td>
      <td>9.859</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>110</td>
      <td>A</td>
      <td>-1.607</td>
      <td>0.260</td>
      <td>-1.741</td>
      <td>3.478</td>
      <td>4.608</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>110</td>
      <td>B</td>
      <td>-1.619</td>
      <td>0.248</td>
      <td>-1.757</td>
      <td>3.443</td>
      <td>5.901</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>110</td>
      <td>C</td>
      <td>-1.631</td>
      <td>0.237</td>
      <td>-1.758</td>
      <td>6.903</td>
      <td>6.765</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>110</td>
      <td>D</td>
      <td>-1.614</td>
      <td>0.254</td>
      <td>-1.770</td>
      <td>9.797</td>
      <td>9.803</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>110</td>
      <td>E</td>
      <td>-1.576</td>
      <td>0.292</td>
      <td>-1.772</td>
      <td>10.243</td>
      <td>10.332</td>
    </tr>
    <tr>
      <td>Li-Li</td>
      <td>110</td>
      <td>F</td>
      <td>-1.523</td>
      <td>0.345</td>
      <td>-1.777</td>
      <td>11.112</td>
      <td>11.187</td>
    </tr>
    <tr>
      <td colspan="8">Adsorption of Li sites on the anode in the presence of Li</td>
    </tr>
  </tbody>
</table>

Table 4. Adsorption Energy of Intercalated Atoms, where the Intercalations are between Two Cs Atoms and One Li Atom

<table>
  <tbody>
    <tr>
      <td>Atoms adsorbed</td>
      <td>cleavage surface</td>
      <td>System</td>
      <td>Eads gas (eV)</td>
      <td>Eads bulk (eV)</td>
      <td>Eads ion (eV)</td>
    </tr>
    <tr>
      <td>Cs-Li-Cs</td>
      <td>110</td>
      <td>site 1</td>
      <td>-2.955</td>
      <td>-0.279</td>
      <td>-3.187</td>
    </tr>
    <tr>
      <td>Cs-Cs-Li</td>
      <td>110</td>
      <td>site 2</td>
      <td>-2.927</td>
      <td>-0.251</td>
      <td>-3.201</td>
    </tr>
    <tr>
      <td colspan="6">Adsorption of intercalated atoms</td>
    </tr>
  </tbody>
</table>

steps, within the slabs, forming a bulk phase. The adsorption energies of the first atom on different sites are detailed in Table 2, and the corresponding cell parameters are presented in Table 1. The configuration of the site is illustrated in Figure S3. Both Li-reduced and Li-ion adsorption (Table 2 and Figure S9) predominantly occur as adatoms on the <110> surface (bridge site) rather than the <100> surface (hollow site). The preferential sites for Li-ion tend to differ from those observed for Li-reduced, except the adatom locations, where Li-ions also preferentially deposits. The calculations indicate that a Li-ion preferably deposits as an adatom on the <110> surface, followed by other sites such as step and ledge, in that order. This disparity in preferential sites suggests a distinct diffusion orientation between Li-ion and Li-reduced on the bare surface. Due to the interaction between the bare phase and the electrolyte, Li-ions are more likely to be present on the surface, as ionic double layer. These higher presence of ions imply that Li has a higher likelihood of depositing on low coordination sites rather than high coordination sites, indicating a tendency to preferentially form dendrites over the <110> surface. The schematic mechanism of Li-ions moving to form a dendrite, where the Li-ion leaves a site, such as a ledge, to adsorb as an adatom, facilitating dendrite growth. This mechanism is particularly relevant after the SEI breaks and the bare phase is exposed.

The initial adhesion of Cs-reduced and Cs-ion atoms to the anode is detailed in Table 2, with the visualization of the sites provided in Figure S2. It is observed that as the adsorption energy of Cs-reduced increases, the adsorption energy of Cs-ion also increases (Figure S9). Consequently, Cs-reduced and Cs-ions exhibit a tendency to occupy the same sites. The substitutional energy was calculated by replacing four Li atoms in a Li supercell with one Cs atom, to preserve similar volume, and the lattice parameters can be found in Table 1. The positive formation energy of Cs as a substitutional atom is an indication that Cs and Li are immiscible and do not form alloys, aligning with experimental findings indicating the lack of miscibility in the Cs−Li phase diagram under normal pressure conditions.⁹⁰ Therefore, Cs does not migrate to the bulk anode; instead, it remains on the anode surface, accumulating until it forms a layer or is trapped by a solid-electrolyte interphase (SEI), forming a shield or reducing defects on the SEI. Cs tends to deposit preferentially on the <110> surface rather than the <100> surface as an adatom, following a similar trend to Li atoms. This implies a competition between Cs and Li for deposition on the <110> surface, although the adsorption of Li is preferential.

![](./images/1055798861840252942_3.jpg)
![](./images/1055798861840252942_4.jpg)

Figure 1. Relationship between the adsorption energy for the same site, comparing lithium and cesium deposition, in a reference for the gas phase and as an ion, is plotted on the left. The correlation between the adsorption energy of Cs and probability density is plotted on the right.

![](./images/1055798861840252942_5.jpg)

Figure 2. Images of adsorption of a second atom on the surface, where cesium is deposited on the same site and lithium changes the site position distance related to cesium. The atoms are colored in such a way that lithium from the slab is represented by light purple color, deposited lithium as atom as pink and cesium as dark purple.

The preferred site for Cs adatom deposition on the <100> and <110> surfaces was calculated (see Table 2), with the most stable site used as a reference for comparison with other sites (e.g., ledge, step, kink). On the <100> surface, tests were conducted for deposition on the hollow, bridge, and top sites (see Figure S3), and the hollow site was determined to be the preferred one. For the cleavage surface <110>, the bridge1, bridge2, hollow, and top sites were tested (see Figure S3), with adsorption occurring preferentially on the top site.

The most favorable site energy for Li adatom was used as the reference for the first Cs deposition and as the initial site reference for the adsorption of a second Cs. For the first atom deposition of both Cs and Li, the adsorption energy of the atom as an ion is larger than as a reduced atom. Additionally, the adsorption energy of Li-ions is stronger than that of Cs-ions, suggesting that dendrites may first form, followed by a Cs accumulation on the <110> surface, thus formation of a Cs shield on the dendrite. Eventually, a Cs layer can cover the dendrite, as indicated by our calculations. Considering the small concentration of Cs in the electrolyte and its lack of amalgamation with Li-metal, we assume that Cs remains on the surface and does not form a bulk Cs-metal.

The relationship between the adsorption energy of Cs and Li for the same sites (Figure 1) reveals a linear correlation between the adsorption of Cs-reduced and Li-reduced. Consequently, the same sites preferred for Cs-reduced adsorption are also favored for Li-reduced. Because there is competition between reduced Li and Cs atoms to be adsorbed at the most stable sites, Li will preferentially occupy these sites, repelling Cs to less stable sites. However, this correlation is not evident when comparing ions, as the preferred sites for Li-ions differ from those for Li-reduced, Cs-reduced, or Cs-ions. To assess whether Cs tends to deposit on dendrites, the radial pair distribution function (RPDF) was integrated (from 0 to 10 Å) to obtain the probability density of finding atoms in that region. Since a dendrite can be represented by a protuberance, the probability density in dendrites is smaller than in other regions of the anode. Moreover, dendrites contain more low coordination sites. As depicted in Figure 1, reduced Cs exhibits a preference for depositing in regions where the probability density is smaller. Consequently, the simulations suggest that Cs-reduced or Cs-ion will preferentially migrate to dendrites, as Cs atoms prefer to stay in low coordination sites such as dendrites.

To elucidate the growth of a Cs layer around the dendrite, the second adsorption of cesium was computed. Based on the calculations for the initial atom deposition, considering that the dendrite predominantly grows from the <110> cleavage surface, and Cs also exhibits a preference for depositing as an adatom on the <110> surface. Given that the favored deposition sites for Cs are hollow sites on the <100> surface and top sites on the <110> surface, the second Cs adsorption was applied to the same sites (hollow and top) for each surface, with variations in the distance between Cs atoms (e.g., Cs deposited on a top site for the <110> surface and a second Cs deposited on another top site on the same surface, as illustrated in Figure S4). The adsorption energy calculated for the second deposition of Cs is detailed in Table 3. When the two adsorbed atoms are initially too close, they tend to move away from the original site, due to the large ionic shell of the Cs atoms. This effect is more pronounced when adsorption occurs in the presence of ions, attributed to the electrostatic effect (Figure S4). The calculations suggest that, on both cleavage surfaces, < 100> and <110>, the second adsorption of Cs becomes more stable as the distance between Cs-Cs increases (Figure S9). However, the difference in energy between two farther sites diminishes. This implies that initially, Cs tends to uniformly spread over the dendrite. To form a Cs layer, it is crucial to accumulate a sufficient amount of Cs on the dendrites to establish an electrostatic shield. Consequently, the quantity of Cs available in the electrolyte should influence the dendrite healing process. Considering that Cs adsorption on the <100> surface is weaker than on the <110> surface, Cs may migrate from the <100> surface and homogeneously accumulate on the <110> surface, where dendrites preferentially form, as indicated by our calculations.

The second adsorption of Li in the presence of Cs on the surface was examined using the same methodology employed for the second Cs adsorption. The adsorption energies of the second Li following the deposition of the first atom (Cs) at various sites are detailed in Table 3, and the corresponding sites are depicted in Figures 2 and S4. The simulations suggest that the closer the distance between Cs and Li adsorbed on the surface (Figure S9), the stronger the adsorption energy. This trend holds true for both surfaces, <100> and <110>, and is

applicable to both Li-reduced and Li-ions. Although Li and Cs exhibit a preference for depositing near each other, there exists a cutoff distance beyond which the adsorption becomes less stable. Additionally, this cutoff distance increases when both atoms are ions, indicating the influence of the electrostatic field produced by the charge of the ions, as observed for Cs atoms. Consequently, while Cs tends to disperse over the surface, Li prefers to deposit closer to Cs atoms. The simulations suggest that initially, when Cs is still dispersed around the dendrite, it may aid in nucleating more adatom sites. Hence, it can be speculated that an increase in the number of adatom sites may enhance the nucleation rate of new dendrites and reduce the rate of dendrite growth, while also dispersing the adatom Li-ions on the <110> surface.

When Li is adsorbed in proximity to another Li atom, it tends to favor adsorption near an already reduced Li atom (Table 3). However, when Li is deposited as an ion, the preference shifts toward sites that are farther away (Figure S9). While Li-ions typically deposit in low coordination sites, predominantly as adatoms on the <110> surface, they tend to disperse across the surface and accumulate on the <110> surface. As Li-ions undergo reduction, they exhibit a tendency to agglomerate. Consequently, Li-reduced and Li-ion display distinct site preferences, leading to different diffusion fluxes between them. The manner in which Li-ions deposit as adatoms and accumulate becomes crucial for dendrite formation. As more Li-ions adsorb in the same region, the reduction rate of Li-ions increases. Agglomerated Li-reduced atoms create new sites for the deposition of additional Li-ions. The intensity of the current in the battery plays a significant role, and if lithium ions lack sufficient time to disperse, Li will undergo local reduction, initiating dendrite nucleation. As Li-ions tend to disperse across the surface and migrate to low-coordinate sites, the pathway that a Li-ion takes to deposit becomes crucial. Consequently, heterogeneities such as grain boundaries, uneven distribution of the electric field, and other factors contribute to the dendrite formation process. In a general sense, Li-ions migrate to the <110> surface, disperse across this surface, but with the accumulation and reduction of Li-ions, Li agglomerates, and new Li-ions deposit as adatoms on the newly formed sites resulting from this agglomeration. It is important to note that, as mentioned earlier, the surfaces tend to be altered to create more adatom sites, favoring dendrite formation.

To comprehend how the Cs layer may envelop dendrites and its impact on dendritic growth, an interchange related to the positions of three adsorbed atoms on the surface was conducted. Li was introduced between two Cs atoms on site 1, while Cs was introduced between a Cs and one Li atom on site 2. These configurations are illustrated in Figure 4, and the corresponding adsorption energies are outlined in Table 4. In ion-based adsorption, Cs demonstrates a preference for intercalation between another Cs-ion and Li-ion. On the other hand, when the adsorption involves reduced atoms, Li predominantly intercalates between two Cs atoms. Considering the surface's contact with the electrolyte, the influence of ions is more pronounced than that of reduced atoms. Consequently, it is anticipated that the Cs layer will expand, causing Li-ions to migrate toward the layer's edge. As the ions accumulate and undergo reduction, the edge layer diminishes, dispersing Cs atoms to accumulate in other regions. Thus, the simulation results align with the expectation that a Cs shield would form, enveloping the dendrites. Hence, further investigation is essential to determine whether the layer creates a positively charged shield around the dendrites, as suggested by the SHES.

A monolayer of Cs was deposited and optimized onto the Li anode to mimic the Cs layer shield on the dendrites. The charge density was computed following eq 3, where $\gamma$ represents the charge density, $\beta_{\text{sys}}$ denotes the electron density in the system, and $\beta_{i}$ signifies the electron density of element i (e.g., Cs, Li) within the system. The cell configuration and charge density are depicted in Figure S6; the small cutoff in the isosurface was selected to facilitate the observation of boundaries between regions with high and low electron densities. Notably, even in a neutral system, negative charges accumulate (electron accumulation) as a layer between Li atoms closest to the surface, and they also concentrate on the top of Cs atoms in a cone-like structure. Meanwhile, positive charges (electron density depletion) are confined between the negative charges on the surface and the vacuum region of the cell. Consequently, two layers of negative charge emerge—one between Cs and Li, and the other between Cs atoms and the vacuum. These findings substantiate the creation of a positive shield around the dendrites through Cs deposition, aligning with the SHES model.

$$
\gamma=\beta_{\text{sys}}-\sum \beta_{i} \tag{3}
$$

Another postulate of the SHES model suggests that Li-ions are prevented from depositing on dendrites due to repulsion promoted by the positive electrostatic shield generated when Cs covers the anode. To assess whether Li is expelled by the Cs layer, Li-reduced was introduced atop the Cs layer, and DOL molecules were subsequently added one by one, as illustrated schematically in Figure 3. It is observed that more solvated Li-ions on the surface tend to possess higher ionic charges and exhibit more stable adsorption. As a result, the Cs layer tends to adsorb the ions rather than expel them. However, as the ion's charge increases, so does the distance between the Li-ion and the Cs layer. Hence, simulations indicate that Li-ions can be adsorbed on the surface but may migrate through it until they reach the layer's edge. The increase in ion distance, attributed to a higher charge, may facilitate ion diffusion within the Cs layer. This is shown in Figure S7, where the climb-nudged elastic barrier method yields a barrier of 0.09 eV for a Li-ion to diffuse over the Cs layer. The low barrier suggests that Li-ions can readily navigate

![](./images/1055798861840252942_6.jpg)

Figure 3. Deposition of Li solvated by DOL over the anode after geometric optimization, where the anode is covered by a Cs monolayer (left). The correlation between the Li-ion charge by the number of DOL molecules solvating the ion (from 1 to 3), the distance between the Li-ion and the Cs layer, and the adsorption energy of the ion on the Cs layer (right).

around the Cs layer, supporting the assumption that Li-ions will diffuse above the Cs layer and deposit on surfaces not localized on the dendrites.

Over the Li metal bare phase, despite Cs preferring to deposit on the dendrite to establish a positive electrostatic shield, it is also crucial that the energy barrier for Cs diffusion over the surface is small. The diffusion energy barriers for both surfaces are small, at 0.025 and 0.029 eV for the <100> and <110> surfaces, respectively (Figure S7). Cs on the <110> surface moves between top sites at a distance of 2.98 Å, while on the <100> surface, it moves between hole sites at a distance of 4.87 Å. Consequently, Cs can easily migrate across the bare anode surface to deposit over the dendrite, serving as an electrostatic shield against Li-ion deposition.

The charge isosurface (at level 5e-4|e|) of the anode covered by a Cs layer was computed under three distinct scenarios, as depicted in Figure 4. When Li-reduced is deposited on the
![](./images/1055798861840252942_7.jpg)

Figure 4. Configuration of the anode covered by a Cs layer. Over this surface, three different configurations were calculated (A) a reduced Li is deposited; (B) a Li-ion solvated by two DOL molecules are deposited; and (C) the electrolyte covers the surface. The atoms are colored in such a way that Li has a green color and Cs a blue color. The charge isosurface has the intensity of 5e-4|e|, where the positive charge isosurface has a blue color, and the negative charge isosurface has a yellow color.

surface, Li occupies a bridge site between two Cs atoms, resulting in the formation of a negative charge toroid around the Li atom. The isosurface exhibits a toroid shape connected to the negative charge concentrated on top of the Cs atoms (Figure 4). The change in the positive charge volume, as defined by the isosurface, without the Li atom's adsorption, is considered negligible and remains localized in the same region (between the Cs atoms), completely overlaying a negative charge volume situated between the Li anode and the Cs layer. Upon solvation by two DOL molecules, transforming into an ion, the toroid contracts, yet a negative charge volume persists, covering the Li-ion and linking this volume to the negative charge volume positioned on top of the two Cs atoms. In the DOL molecule, the negative charge volume of the electrolyte envelops the atomic nuclei, while a positive charge volume encompasses this negative volume (except around the oxygen atoms). When the anode is shielded by a Cs layer and this layer is covered by another layer consisting solely of DOL molecules, the oxygen from DOL molecules is deposited on the Cs atoms' tops. In the presence of the electrolyte, the positive charge volume almost entirely envelops the anode, with some negative charge volumes sporadically located where the oxygen atoms of the electrolyte are positioned.

Consequently, the electrolyte enhances the Cs layer's effect, augmenting the thickness of the positive charge volume formed by the Cs layer.

While the adsorption energy calculations on the lithium metal bare surface align with the SHES model, the bare lithium metal surface interacts with the electrolyte, giving rise to the formation of a solid electrolyte interface (SEI). Thus, it becomes imperative to elucidate the role of Cs in the SEI and its potential impact on SEI defects. The cell configuration, absorption and adsorption energies of Cs and Li in the presence of the SEI for various sites, along with the visualization of the tested sites, are detailed in Table 1 (unit cell), in Table 5 (adsorption energy), and Figure 5 (visual-

<table>
<caption>Table 5. Adsorption Energy of the Cs Atom on SEI Surface, on Damaged Regions of the SEI, and in the Grain Boundary</caption>
<thead>
<tr>
<th>Atoms adsorbed</th>
<th>cleavage surface</th>
<th>System</th>
<th>Eads gas ion (eV)</th>
<th>Eads bulk (eV)</th>
<th>Eads ion (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI 1</td>
<td>-0.084</td>
<td>0.725</td>
<td>1.438</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI 2</td>
<td>-0.065</td>
<td>0.744</td>
<td>1.428</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI 3</td>
<td>-0.104</td>
<td>0.705</td>
<td>1.388</td>
</tr>
<tr>
<td colspan="6">Cs adatom sites on the SEI</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI broke 1</td>
<td>-0.747</td>
<td>0.062</td>
<td>-1.201</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI broke 2</td>
<td>-0.580</td>
<td>0.228</td>
<td>-1.004</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI broke 3</td>
<td>-1.194</td>
<td>-0.386</td>
<td>-1.566</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI broke 4</td>
<td>-0.149</td>
<td>0.659</td>
<td>-0.502</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI broke 5</td>
<td>-0.545</td>
<td>0.264</td>
<td>-0.993</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>SEI broke 6</td>
<td>-0.119</td>
<td>0.690</td>
<td>-0.231</td>
</tr>
<tr>
<td colspan="6">Cs adatom sites on a damaged SEI</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>Grain Boundary 1</td>
<td>-1.746</td>
<td>-0.938</td>
<td>---</td>
</tr>
<tr>
<td>Cs</td>
<td>100</td>
<td>Grain Boundary 2</td>
<td>-0.857</td>
<td>-0.049</td>
<td>---</td>
</tr>
<tr>
<td colspan="6">Cs absorption on the Grain Boundary</td>
</tr>
<tr>
<td>Li</td>
<td>100</td>
<td>Grain Boundary 1</td>
<td>-2.084</td>
<td>-0.216</td>
<td>---</td>
</tr>
<tr>
<td>Li</td>
<td>100</td>
<td>Grain Boundary 2</td>
<td>-2.215</td>
<td>-0.348</td>
<td>---</td>
</tr>
<tr>
<td colspan="6">Li absorption on the Grain Boundary</td>
</tr>
</tbody>
</table>

ization of the system), respectively. The positive adsorption energy of reduced Cs in a bulk reference, as well as for Cs ions, on intact SEI sites suggests that Cs is unlikely to deposit on the SEI surface. Instead, it tends to form a bulk Cs or migrate to damaged regions within the SEI. Introducing a V-shaped notch of $45^{\circ}$ on the intact SEI to simulate a fracture, which exposes the bare Li phase, results in Cs atoms preferentially depositing on the damaged SEI. During the optimization of the damaged SEI, the bare Li surface tends to be restored by the SEI, thereby reducing the exposed area. Cs atoms deposit preferentially on the damaged SEI, with the most stable sites located at the interphase between the metal surface and the SEI. Additionally, the adsorption energy on the bare phase is stronger than on the SEI surface. Therefore, in instances where the SEI is damaged during cycling, Cs is inclined to deposit on the damaged area or nanofractures that may emerge on the SEI. As a result and considering the shield effect, Cs mitigates the deposition of Li-ions on the damaged areas, leading to a more uniform deposition of Li-ions across the anode. Also, heterogeneities within the SEI can create preferential paths for Li deposition, contributing to dendrite growth, especially at grain boundaries. $^{91}$ A simulated grain boundary interphase, denoted as "$\sum\_5$," constructed by cleaving the <310> surface of LiF, indicates that Cs exhibits greater stability at the grain boundary compared to deposition on the bare Li metal surface.

![](./images/1055798861840252942_8.jpg)

Figure 5. Adsorption sites for Cs deposition over the SEI and in the grain boundaries. (A) The sites for Cs deposition on an intact SEI. (B) The sites for Cs deposition on a damaged SEI. (C) Sites for Cs deposition in the grain boundary. (D) Change in the structure of grain in the presence of the grain boundary. The atoms are colored in such a way that Li has a light purple color, Cs a dark purple color and F has cyan color.

Consequently, Cs has the potential to close grain boundaries, impeding the diffusion of Li along the grain boundary. Moreover, Cs plays a role in reducing heterogeneities within the SEI and the anode, thereby diminishing preferential pathways for lithium diffusion.

The calculation of the average charge density (ACD) in the presence of a grain boundary involved assessing the z- and x- directions was averaged based on the eq 3. Here, the z- direction is perpendicular to the surface, and the x-direction runs parallel to the cleavage surface. In the z-direction, the ACD remains constant in the metal phase and vacuum region but exhibits oscillations within the SEI layer, primarily influenced by fluorine atoms. The oscillations intensify along the x-direction, particularly in regions where grain boundaries are located, suggesting that SEI defects such as grain boundaries can locally impact the ACD. To comprehend the influence of Cs on the ACD when absorbed on grain boundaries, we calculated the ACD without Cs, denoted as "Δ", the ACD with Cs on the grain boundary denoted as "Δ(Cs)", and the ACD of Cs in the grain boundary denoted as "Cs" (refer to Figure S8). The ACD between the metal phase and the anode remains unchanged with the presence of Cs on the grain boundary. However, the introduction of Cs on the grain boundary amplifies the intensity of ACD oscillations, particularly from the location of Cs on the grain boundary extending to the surface. The electron density of Cs is concentrated near the Cs atom, thereby altering the intensity of oscillations due to the redistribution of electron density involving Li and F. Since Li may migrate through the SEI as an ion, the alteration in ACD caused by Cs absorption on the grain boundary could impact the energy barrier for Li migration through regions close to the grain boundary. This suggests that the diffusion of Li in the bulk SEI, near the grain boundaries, is influenced by the presence of Cs and the associated atomic stress. Moreover, the configuration of grains near the grain boundary (Σ_5) undergoes changes; the system readapts to minimize the grain boundary surface. As depicted in Figure 5, the SEI is expected to adopt a four-sided geometry, with each side having similar lengths and sizes, and angles close to 90°, contingent upon the local stress experienced by each region. However, after optimization, local structures shift, indicating that the structure of the SEI undergoes alterations near grain boundaries with specific angle contacts.

In the process of lithium ions deposition into the anode, after the formation of the SEI, we can consider two different scenarios: The migration of the Li-ions through the SEI, and the flux of Li-ions into the lithium bare phase when the SEI breaks and exposes the metallic structure. In the first situation, Cs-ions will decrease heterogeneous deposition by occupying defects and grain boundaries in the SEI (Figure 5). In the second state, the electric field will concentrate the migration of Li and Cs ions from the electrolyte onto the lithium bare phase, and the migration of Li and Cs atoms on the surface. Considering that Cs-ions will accumulate on the surface, preferentially in low coordination sites as in dendrites, together with the solvent, a positively charged layer tends to be formed (Figure 4), which may repel the deposition of further Li-ions in the dendrite.

## CONCLUSION

According to the SHES model, the introduction of cesium salts into the electrolyte at a low concentration prevents the reduction of Cs ions during the anode charging process, allowing only the reduction of Li-ions. This model proposes that Cs ions will form a protective layer over the anode's dendrites, establishing a positive electrostatic shield that hinders the deposition of Li ions on the dendritic surface. Consequently, this mechanism aims to inhibit dendrite growth and facilitate the healing of existing dendrites in the battery. To assess the validity of the SHES model, it is imperative to examine the following hypotheses: (H1) Cs will remain on the surface as a layer; (H2) This layer will effectively cover the dendrites; (H3) The layer exhibits a positive charge; (H4) The layer repels Li-ions; (H5) The Cs layer is stable. Additionally, delving into the implications of Cs on SEI growth is essential for expanding our understanding beyond the proposed SHES model.

The initial adsorption calculations for cesium and lithium, whether in reduced or ionized forms, were examined across various sites. It was observed that Cs-reduced, Cs-ion, and Li- reduced exhibit a tendency to deposit on the same sites, suggesting a competitive interaction among these atoms during deposition. Cs demonstrates an absorption that is not favored in the bulk anode, favoring adsorption on the Li-metal anode rather than forming a bulk material. Additionally, Cs exhibits a preference for deposition in low-coordination Cs−Li sites. Consequently, it can be inferred that Cs remains on the surface of the anode and selectively migrates toward dendrites. This aligns with hypotheses H1 and H2. The favored adsorption sites for Li-ions are adatom sites on the <110> surface, followed by step sites, indicating a tendency for Li-ions to deposit in low-coordination locations. This implies that

dendrites will predominantly grow perpendicular to the <110> surface, with Li-ions preferentially depositing on the dendrites. Cs tends to deposit favorably on the <110> surface, suggesting the formation of a Cs layer primarily on this surface, where dendrites preferentially grow. This underscores the competition between Cs and Li.

The calculations for the adsorption energies of the second atom were conducted for both Cs and Li. In the case of a second Cs adsorption, the results suggest that Cs will predominantly disperse over the adsorbed surfaces. Hence, Cs needs to initially accumulate on the dendrites to establish a uniform layer. When Cs is the first adsorbed atom and Li is the second, Li tends to deposit in close proximity to Cs. This implies that initially, Cs may contribute to the dispersion of adatom Li-ions. Li-reduced exhibits a tendency to accumulate, while Li-ions tend to disperse over the surface, with an accumulation on the <110> surface. This introduces a competition between Li-reduced and Li-ions. Sites where Li preferentially deposits will experience a faster reduction of Li-ions, allowing new Li-ions to cover the surface and gradually build the dendrite. Factors such as damaged SEI, grain boundaries, uneven electric field distribution, and current density contribute significantly to the formation of dendrites. In the case of three atoms adsorbing on the surface (two Cs and one Li), the calculations indicate that Cs-ions preferentially adsorb closer to other Cs-ions rather than Li-ions. This assumption suggests that as Cs accumulates, it will form a stable layer, and Li will tend to deposit favorably on the layer's edge, supporting hypothesis H5.

The study involved two systems to examine the charge distribution when the anode is completely covered by Cs and when the electrolyte is additionally adsorbed over this Cs layer. Cs exhibits a charge of +0.35|e| and +0.70|e| in the presence and absence of the electrolyte, respectively. The isosurface reveals that the negative charge volume is located between the Li anode and the Cs layer, as well as on top of the Cs atoms. The positive charge volume is confined between Cs atoms and the vacuum, encompassing both negative charge volumes. The presence of the electrolyte enhances the positive charge volume, expanding its size, aligning with hypothesis H3. However, when a Li-ion is adsorbed over the Cs layer, the absorption energy of Cs strengthens with an increasing number of DOL molecules solvating the Li-ion. As the charge increases, the adsorption stability in the Cs layer also increases. This contradicts hypothesis H4; nevertheless, it can be considered that as the Li-ion becomes more solvated, the distance between the Cs layer and the Li-ion increases, potentially allowing Li-ions to move above the Cs layer and deposit outside the dendrites onto other regions, contributing to the healing of the anode.

When the SEI is present, the computations suggest that Cs will relocate to areas with damaged SEI, particularly to regions where the bare Li metal surface is exposed or to grain boundary sites. Consequently, Cs will mitigate the heterogeneities in the SEI, diminishing preferential pathways for Li-ion deposition.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at
https://pubs.acs.org/doi/10.1021/acs.chemmater.4c01601.

All the complementary images and tables mentioned in the text and the images describe the sites of Li and Cs adsorption and charge distribution (PDF)

## AUTHOR INFORMATION

### Corresponding Author
Samuel Bertolini – Institute of Physics, Univesidade Federal Fluminense, Nitéroi 24210-346, Brazil; Institute of Condensed Matter and Nanoscience, Université catholique de Louvain, Louvain-la-Neuve 1348, Belgium; orcid.org/0000-0003-0969-7142; Email: samuel.bertolini@uclouvain.be

### Authors
Arnaud Delcorte – Institute of Condensed Matter and Nanoscience, Université catholique de Louvain, Louvain-la-Neuve 1348, Belgium; orcid.org/0000-0003-4127-8650
Pedro Venezuela – Institute of Physics, Univesidade Federal Fluminense, Nitéroi 24210-346, Brazil

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.chemmater.4c01601

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
The authors thank the support from Fundação Carlos Chagas Filho de Amparo à Pesquisa do Estado do Rio de Janeiro (FAPERJ) through Project ID E-26/200.602 and 210.366/2022 is gratefully acknowledged. The authors also acknowledge the computer time supported by the Institut de Calcul Intensif et de Stockage de Masse (CISM) at Université Catholique de Louvain.

## REFERENCES
(1) Yang, Z.; Gu, L.; Hu, Y.-S.; Li, H. Atomic-Scale Structure-Property Relationships in Lithium Ion Battery Electrode Materials. Annu. Rev. Mater. Res. 2017, 47 (1), 175−198.
(2) Etacheri, V.; Marom, R.; Elazari, R.; Salitra, G.; Aurbach, D. Challenges in the Development of Advanced Li-Ion Batteries: A Review. Energy Environ. Sci. 2011, 4 (9), 3243−3262.
(3) Aurbach, D.; McCloskey, B. D.; Nazar, L. F.; Bruce, P. G. Advances in Understanding Mechanisms Underpinning Lithium−Air Batteries. Nat. Energy 2016, 1 (9), 16128.
(4) Zhang, K.; Lee, G.; Park, M.; Li, W.; Kang, Y. Recent Developments of the Lithium Metal Anode for Rechargeable Non-aqueous Batteries. Adv. Energy Mater. 2016, 6 (20), 1600811.
(5) Armstrong, A. R.; Bruce, P. G. Synthesis of Layered LiMnO2 as an Electrode for Rechargeable Lithium Batteries. Nature 1996, 381 (6582), 499−500.
(6) Park, M. S.; Ma, S. B.; Lee, D. J.; Im, D.; Doo, S.-G.; Yamamoto, O. A Highly Reversible Lithium Metal Anode. Sci. Rep. 2014, 4 (1), 3815.
(7) Gilaki, M.; Francis, A.; Bautista, D.; Avdeev, I. Progress Toward Understanding Catastrophic Failure of Electric Vehicle Li-Ion Batteries: Multi-Physics Modeling. In ASME International Mechanical Engineering Congress and Exposition; American Society of Mechanical Engineers, 2016; p 5.
(8) Lisbona, D.; Snee, T. A Review of Hazards Associated with Primary Lithium and Lithium-Ion Batteries. Process Saf. Environ. Prot. 2011, 89 (6), 434−442.
(9) Tobishima, S.; Yamaki, J. A Consideration of Lithium Cell Safety. J. Power Sources 1999, 81−82, 882−886.

(10) Ritchie, A.; Howard, W. Recent Developments and Likely Advances in Lithium-Ion Batteries. *J. Power Sources* **2006**, *162* (2), 809–812.

(11) Goodenough, J. B.; Kim, Y. Challenges for Rechargeable Li Batteries. *Chem. Mater.* **2010**, *22* (3), 587–603.

(12) Aurbach, D.; Zinigrad, E.; Cohen, Y.; Teller, H. A Short Review of Failure Mechanisms of Lithium Metal and Lithiated Graphite Anodes in Liquid Electrolyte Solutions. *Solid State Ion.* **2002**, *148* (3–4), 405–416.

(13) Gireauld, L.; Grugeon, S.; Laruelle, S.; Yrieix, B.; Tarascon, J.-M. Lithium Metal Stripping/Plating Mechanisms Studies: A Metallurgical Approach. *Electrochem. Commun.* **2006**, *8* (10), 1639–1649.

(14) Ota, H.; Shima, K.; Ue, M.; Yamaki, J. Effect of Vinylene Carbonate as Additive to Electrolyte for Lithium Metal Anode. *Electrochim. Acta* **2004**, *49* (4), 565–572.

(15) Lee, Y. M.; Seo, J. E.; Lee, Y.-G.; Lee, S. H.; Cho, K. Y.; Park, J.-K. Effects of Triacetoxyvinylsilane as SEI Layer Additive on Electrochemical Performance of Lithium Metal Secondary Battery. *Electrochem. Solid-State Lett.* **2007**, *10* (9), A216.

(16) Camacho-Forero, L. E.; Smith, T. W.; Bertolini, S.; Balbuena, P. B. Reactivity at the Lithium–Metal Anode Surface of Lithium–Sulfur Batteries. *J. Phys. Chem. C* **2015**, *119* (48), 26828–26839.

(17) Camacho-Forero, L. E.; Balbuena, P. B. Elucidating Electrolyte Decomposition under Electron-Rich Environments at the Lithium- Metal Anode. *Phys. Chem. Chem. Phys.* **2017**, *19* (45), 30861–30873.

(18) Togasaki, N.; Momma, T.; Osaka, T. Enhanced Cycling Performance of a Li Metal Anode in a Dimethylsulfoxide-Based Electrolyte Using Highly Concentrated Lithium Salt for a Lithium– oxygen Battery. *J. Power Sources* **2016**, *307*, 98–104.

(19) Li, W.; Yao, H.; Yan, K.; Zheng, G.; Liang, Z.; Chiang, Y.-M.; Cui, Y. The Synergetic Effect of Lithium Polysulfide and LithiumNitrate to Prevent Lithium Dendrite Growth. *Nat. Commun.* **2015**, *6* (1), 7436.

(20) Hirai, T.; Yoshimatsu, I.; Yamaki, J. Effect of Additives on Lithium Cycling Efficiency. *J. Electrochem. Soc.* **1994**, *141* (9), 2300.

(21) Shiraishi, S.; Kanamura, K.; Takehara, Z. Surface Condition Changes in Lithium Metal Deposited in Nonaqueous Electrolyte Containing HF by Dissolution-Deposition Cycles. *J. Electrochem. Soc.* **1999**, *146* (5), 1633.

(22) Xiong, S.; Xie, K.; Diao, Y.; Hong, X. Properties of Surface Film on Lithium Anode with LiNO3 as Lithium Salt in Electrolyte Solution for Lithium–Sulfur Batteries. *Electrochim. Acta* **2012**, *83*, 78–86.

(23) Liu, Z.; Bertolini, S.; Balbuena, P. B.; Mukherjee, P. Li. Li2S Film Formation on Lithium Anode Surface of Li–S Batteries. *ACS Appl. Mater. Interfaces* **2016**, *8* (7), 4700–4708.

(24) Aurbach, D. Review of Selected Electrode–Solution Interactions Which Determine the Performance of Li and Li Ion Batteries. *J. Power Sources* **2000**, *89* (2), 206–218.

(25) Lu, D.; Shao, Y.; Lozano, T.; Bennett, W. D.; Graff, G. L.; Polzin, B.; Zhang, J.; Engelhard, M. H.; Saenz, N. T.; Henderson, P. A.; et al. Failure Mechanism for Fast-Charged Lithium Metal Batteries with Liquid Electrolytes. *Adv. Energy Mater.* **2015**, *5* (3), 1400993.

(26) López, C. M.; Vaughey, J. T.; Dees, D. W. Morphological Transitions on Lithium Metal Anodes. *J. Electrochem. Soc.* **2009**, *156* (9), A726.

(27) Xiong, S.; Xie, K.; Blomberg, E.; Jacobsson, P.; Matic, A. Analysis of the Solid Electrolyte Interphase Formed with an Ionic Liquid Electrolyte for Lithium-Sulfur Batteries. *J. Power Sources* **2014**, *252*, 150–155.

(28) Suo, L.; Hu, Y.-S.; Li, H.; Armand, M.; Chen, L. A New Class of Solvent-in-Salt Electrolyte for High-Energy Rechargeable Metallic Lithium Batteries. *Nat. Commun.* **2013**, *4* (1), 1481.

(29) Bertolini, S.; Balbuena, P. B. Effect of Solid Electrolyte Interphase on the Reactivity of Polysulfide over Lithium-Metal Anode. *Electrochim. Acta* **2017**, *258*, 1320–1328.

(30) Ma, G.; Wen, Z.; Wu, M.; Shen, C.; Wang, Q.; Jin, J.; Wu, X. A Lithium Anode Protection Guided Highly-Stable Lithium–Sulfur Battery. *Chem. Commun.* **2014**, *50* (91), 14209–14212.

(31) Menkin, S.; Golodnitsky, D.; Peled, E. Artificial Solid- Electrolyte Interphase (SEI) for Improved Cycleability and Safety of Lithium–Ion Cells for EV Applications. *Electrochem. Commun.* **2009**, *11* (9), 1789–1791.

(32) Xiong, S.; Xie, K.; Diao, Y.; Hong, X. Characterization of the Solid Electrolyte Interphase on Lithium Anode for Preventing the Shuttle Mechanism in Lithium–Sulfur Batteries. *J. Power Sources* **2014**, *246*, 840–845.

(33) Bertolini, S.; Jacob, T. Atomistic Discharge Studies of Sulfurized-Polyacrylonitrile through Ab Initio Molecular Dynamics. *Electrochim. Acta* **2022**, *403*, 139538.

(34) Bertolini, S.; Jacob, T. Capturing Polysulfides by Sulfurized- Polyacrylonitrile in Lithium-Sulfur Batteries and the Sulfur-Chain Effects through Density Functional Theory. *Electrochem. Sci. Adv.* **2022**, *2* (4), No. e2100129.

(35) Bertolini, S.; Jacob, T. Sulfurized-Polyacrylonitrile in Lithium- Sulfur Batteries: Interactions between Undercoordinated Carbons and Sulfur Structure under Low Lithiation. *J. Energy Chem.* **2022**, *66*, 587–596.

(36) Bertolini, S.; Jacob, T. Density Functional Theory Studies on Sulfur–Polyacrylonitrile as a Cathode Host Material for Lithium– Sulfur Batteries. *ACS Omega* **2021**, *6* (14), 9700–9708.

(37) Bertolini, S.; Venezuela, P.; Delcorte, A. The Effect of Lithium Battery Overpotential on Sulfurized-Polyacrylonitrile (SPAN): A Theoretical Approach. *J. Energy Storage* **2024**, *78*, 110049.

(38) Aurbach, D.; Youngman, O.; Gofer, Y.; Meitav, A. The Electrochemical Behaviour of 1,3-Dioxolane—LiClO4 Solutions—I. Uncontaminated Solutions. *Electrochim. Acta* **1990**, *35* (3), 625–638.

(39) Gofer, Y.; Ben-Zion, M.; Aurbach, D. Solutions of LiAsF6 in 1,3-Dioxolane for Secondary Lithium Batteries. *J. Power Sources* **1992**, *39* (2), 163–178.

(40) Miao, R.; Yang, J.; Xu, Z.; Wang, J.; Nuli, Y.; Sun, L. A New Ether-Based Electrolyte for Dendrite-Free Lithium-Metal Based Rechargeable Batteries. *Sci. Rep.* **2016**, *6* (1), 21771.

(41) Zhang, X.; Xu, P.; Duan, J.; Lin, X.; Sun, J.; Shi, W.; Xu, H.; Dou, W.; Zheng, Q.; Yuan, R.; et al. A Dicarbonate Solvent Electrolyte for High Performance 5 V-Class Lithium-Based Batteries. *Nat. Commun.* **2024**, *15* (1), 536.

(42) Yamada, Y.; Yamada, A. Review—Superconcentrated Electro- lytes for Lithium Batteries. *J. Electrochem. Soc.* **2015**, *162* (14), A2406.

(43) Yamada, Y.; Furukawa, K.; Sodeyama, K.; Kikuchi, K.; Yaegashi, M.; Tateyama, Y.; Yamada, A. Unusual Stability of Acetonitrile-Based Superconcentrated Electrolytes for Fast-Charging Lithium-Ion Bat- teries. *J. Am. Chem. Soc.* **2014**, *136* (13), 5039–5046.

(44) Shadike, Z.; Tan, S.; Lin, R.; Cao, X.; Hu, E.; Yang, X.-Q. Engineering and Characterization of Interphases for Lithium Metal Anodes. *Chem. Sci.* **2022**, *13* (6), 1547–1568.

(45) Mayers, M. Z.; Kaminski, J. W.; Miller, T. F., III Suppression of Dendrite Formation via Pulse Charging in Rechargeable Lithium Metal Batteries. *J. Phys. Chem. C* **2012**, *116* (50), 26214–26221.

(46) Chopade, S. A.; Au, J. G.; Li, Z.; Schmidt, P. W.; Hillmyer, M. A.; Lodge, T. P. Robust Polymer Electrolyte Membranes with High Ambient-Temperature Lithium-Ion Conductivity via Polymerization- Induced Microphase Separation. *ACS Appl. Mater. Interfaces* **2017**, *9* (17), 14561–14565.

(47) Zhou, W.; Wang, S.; Li, Y.; Xin, S.; Manthiram, A.; Goodenough, J. B. Plating a Dendrite-Free Lithium Anode with a Polymer/Ceramic/Polymer Sandwich Architecture. *J. Am. Chem. Soc.* **2016**, *138* (30), 9385–9388.

(48) Liu, Y.; Lin, D.; Liang, Z.; Zhao, J.; Yan, K.; Cui, Y. Lithium- Coated Polymeric Matrix as a Minimum Volume-Change and Dendrite-Free Lithium Metal Anode. *Nat. Commun.* **2016**, *7* (1), 10992.

(49) Fu, K.; Gong, Y.; Dai, J.; Gong, A.; Han, X.; Yao, Y.; Wang, C.; Wang, Y.; Chen, Y.; Yan, C.; Li, Y.; Wachsman, E. D.; Hu, L. F. Flexible, solid-state, ion-conducting membrane with 3D garnet nanofiber networks for lithium batteries. *Proc. Natl. Acad. Sci. U. S. A.* **2016**, *113* (26), 7094–7099.

(50) Harry, K. J.; Hallinan, D. T.; Parkinson, D. Y.; MacDowell, A. A.; Balsara, N. P. Detection of Subsurface Structures underneath Dendrites Formed on Cycled Lithium Metal Electrodes. *Nat. Mater.* 2014, **13** (1), 69−73.

(51) Ding, F.; Xu, W.; Graff, G. L.; Zhang, J.; Sushko, M. L.; Chen, X.; Shao, Y.; Engelhard, M. H.; Nie, Z.; Xiao, J.; et al. Dendrite-Free Lithium Deposition via Self-Healing Electrostatic Shield Mechanism. *J. Am. Chem. Soc.* 2013, **135** (11), 4450−4456.

(52) Ding, F.; Xu, W.; Chen, X.; Zhang, J.; Shao, Y.; Engelhard, M. H.; Zhang, Y.; Blake, T. A.; Graff, G. L.; Liu, X.; et al. Effects of Cesium Cations in Lithium Deposition via Self-Healing Electrostatic Shield Mechanism. *J. Phys. Chem. C* 2014, **118** (8), 4043−4049.

(53) Michely, T.; Hohage, M.; Bott, M.; Comsa, G. Inversion of Growth Speed Anisotropy in Two Dimensions. *Phys. Rev. Lett.* 1993, **70** (25), 3943−3946.

(54) Ruggerone, P.; Kley, A.; Scheffler, M. MICROSCOPIC ASPECTS OF HOMOEPITAXIAL GROWTH. *Prog. Surf. Sci.* 1997, **54** (3), 331−340.

(55) Brune, H. Microscopic View of Epitaxial Metal Growth: Nucleation and Aggregation. *Surf. Sci. Rep.* 1998, **31** (4), 125−229.

(56) Quayum, M. E.; Ye, S.; Uosaki, K. Mechanism for Nucleation and Growth of Electrochemical Palladium Deposition on an Au(111) Electrode. *J. Electroanal. Chem.* 2002, **520** (1), 126−132.

(57) Lin, X.; Dasgupta, A.; Xie, F.; Schimmel, T.; Evers, F.; Groß, A. Exchange Processes in the Contact Formation of Pb Electrodes. *Electrochim. Acta* 2014, **140**, 505−510.

(58) Vitos, L.; Ruban, A. V.; Skriver, H. L.; Kollár, J. The Surface Energy of Metals. *Surf. Sci.* 1998, **411** (1), 186−202.

(59) Chadwick, G. A. A Hard-Sphere Model of Crystal Growth. *Metal Sci.* 1967, **1A** (1), 132−139.

(60) Van der Planken, J.; Deruyttere, A. A Scanning Electron Microscope Study of Vapour Grown Magnesium. *J. Cryst. Growth* 1971, **11** (3), 273−279.

(61) Janner, A.; Janssen, T. From Crystal Morphology to Molecular and Scale Crystallography. *Phys. Scr.* 2015, **90** (8), 088007.

(62) Donnay, J. D. H.; Harker, D. A New Law of Crystal Morphology Extending the Law of Bravais. *Am. Mineral* 1937, **22** (5), 446−467.

(63) Du, J.; Guo, Z.; Yang, M.; Xiong, S. Growth Pattern and Orientation Selection of Magnesium Alloy Dendrite: From 3-D Experimental Characterization to Theoretical Atomistic Simulation. *Mater. Today Commun.* 2017, **13**, 155−162.

(64) Miller, W. A.; Chadwick, G. A.; Frank, F. C. The Equilibrium Shapes of Small Liquid Droplets in Solid−Liquid Phase Mixtures: Metallic h.c.p. and Metalloid Systems. *Proc. R. Soc. London, Ser. A* 1997, **312** (1509), 257−276.

(65) Sandlöbes, S.; Pei, Z.; Friák, M.; Zhu, L.-F.; Wang, F.; Zaefferer, S.; Raabe, D.; Neugebauer, J. Ductility Improvement of Mg Alloys by Solid Solution: Ab Initio Modeling, Synthesis and Mechanical Properties. *Acta Mater.* 2014, **70**, 92−104.

(66) Zhou, X.; Xie, Z.-X.; Jiang, Z.-Y.; Kuang, Q.; Zhang, S.-H.; Xu, T.; Huang, R.-B.; Zheng, L.-S. Formation of ZnO Hexagonal Micro-Pyramids: A Successful Control of the Exposed Polar Surfaces with the Assistance of an Ionic Liquid. *Chem. Commun.* 2005, **No. 44**, 5572−5574.

(67) Zhu, W.; Jin, H. M.; Wu, P.; Liu, H. L. Periodic Density Functional Theory Study of the Crystal Morphology of ${\mathrm{\{FeZn\}}}_{13}$. *Phys. Rev. B* 2004, **70** (16), 165419.

(68) Liu, P.-L.; Siao, Y.-J. Ab Initio Study on Preferred Growth of ZnO. *Scr. Mater.* 2011, **64** (6), 483−485.

(69) Rohl, A. L.; Gay, D. H. Calculating the Effects of Surface Relaxation on Morphology. *J. Cryst. Growth* 1996, **166** (1), 84−90.

(70) Bertolini, S.; Balbuena, P. B. Buildup of the Solid Electrolyte Interphase on Lithium-Metal Anodes: Reactive Molecular Dynamics Study. *J. Phys. Chem. C* 2018, **122** (20), 10783−10791.

(71) Soto, F. A.; Marzouk, A.; El-Mellouhi, F.; Balbuena, P. B. Understanding Ionic Diffusion through SEI Components for Lithium-Ion and Sodium-Ion Batteries: Insights from First-Principles Calculations. *Chem. Mater.* 2018, **30** (10), 3315−3322.

(72) Zheng, Y.; Soto, F. A.; Ponce, V.; Seminario, J. M.; Cao, X.; Zhang, J.-G.; Balbuena, P. B. Localized High Concentration Electrolyte Behavior near a Lithium−Metal Anode Surface. *J. Mater. Chem. A Mater.* 2019, **7** (43), 25047−25055.

(73) Jäckle, M.; Groß, A. Microscopic Properties of Lithium, Sodium, and Magnesium Battery Anode Materials Related to Possible Dendrite Growth. *J. Chem. Phys.* 2014, **141** (17), 174710.

(74) Jäckle, M.; Helmbrecht, K.; Smits, M.; Stottmeister, D.; Groß, A. Self-Diffusion Barriers: Possible Descriptors for Dendrite Growth in Batteries? *Energy Environ. Sci.* 2018, **11** (12), 3400−3407.

(75) Kohn, W.; Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. *Phys. Rev.* 1965, **140** (4A), A1133−A1138.

(76) Jones, R. O.; Gunnarsson, O. The Density Functional Formalism, Its Applications and Prospects. *Rev. Mod. Phys.* 1989, **61** (3), 689−746.

(77) Kresse, G.; Hafner, J. Ab Initio Molecular Dynamics for Open-Shell Transition Metals. *Phys. Rev. B* 1993, **48** (17), 13115.

(78) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. *Phys. Rev. B* 1996, **54** (16), 11169−11186.

(79) Car, R.; Parrinello, M. Unified Approach for Molecular Dynamics and Density-Functional Theory. *Phys. Rev. Lett.* 1985, **55** (22), 2471−2474.

(80) Payne, M. C.; Teter, M. P.; Allan, D. C.; Arias, T. A.; Joannopoulos, A. J. D. Iterative Minimization Techniques for Ab Initio Total-Energy Calculations: Molecular Dynamics and Conjugate Gradients. *Rev. Mod. Phys.* 1992, **64** (4), 1045.

(81) Monkhorst, H. J.; Pack, J. D. Special Points for Brillouin-Zone Integrations. *Phys. Rev. B* 1976, **13** (12), 5188.

(82) Blöchl, P. E. Projector Augmented-Wave Method. *Phys. Rev. B* 1994, **50** (24), 17953.

(83) Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. *Phys. Rev. B* 1999, **59** (3), 1758.

(84) Doll, K.; Harrison, N. M.; Saunders, V. R. A Density Functional Study of Lithium Bulk and Surfaces. *J. Phys.: Condens. Matter* 1999, **11** (26), 5007.

(85) Anderson, M. S.; Swenson, C. A. Experimental Equations of State for Cesium and Lithium Metals to 20 Kbar and the High-Pressure Behavior of the Alkali Metals. *Phys. Rev. B* 1985, **31** (2), 668−680.

(86) Henkelman, G.; Arnaldsson, A.; Jónsson, H. A Fast and Robust Algorithm for Bader Decomposition of Charge Density. *Comput. Mater. Sci.* 2006, **36** (3), 354−360.

(87) Sanville, E.; Kenny, S. D.; Smith, R.; Henkelman, G. Improved Grid-Based Algorithm for Bader Charge Allocation. *J. Comput. Chem.* 2007, **28** (5), 899−908.

(88) Tang, W.; Sanville, E.; Henkelman, G. A Grid-Based Bader Analysis Algorithm without Lattice Bias. *J. Phys.: Condens. Matter* 2009, **21** (8), 084204.

(89) Henkelman, G.; Uberuaga, B. P.; Jónsson, H. A Climbing Image Nudged Elastic Band Method for Finding Saddle Points and Minimum Energy Paths. *J. Chem. Phys.* 2000, **113** (22), 9901−9904.

(90) Desgreniers, S.; Tse, J. S.; Matsuoka, T.; Ohishi, Y.; Tse, J. J. Mixing Unmixables: Unexpected Formation of Li-Cs Alloys at Low Pressure. *Sci. Adv.* 2024, **1** (9), No. e1500669.

(91) Leung, K.; Jungjohann, K. L. Spatial Heterogeneities and Onset of Passivation Breakdown at Lithium Anode Interfaces. *J. Phys. Chem. C* 2017, **121** (37), 20188−20196.
