# Performance Analysis of Perovskite Solar Cells Using DFT-Extracted Parameters of Metal-Doped TiO₂ Electron Transport Layer

Sadiq Shahriyar Nishat,∥ Md. Jayed Hossain,∥ Faiyaz Elahi Mullick, Alamgir Kabir, Shaestagir Chowdhury, Sharnali Islam, and Mainul Hossain*

Cite This: J. Phys. Chem. C 2021, 125, 13158−13166

---

## ACCESS | Metrics & More | Article Recommendations | Supporting Information

### ABSTRACT:
The performance of perovskite solar cells (PSCs) depends heavily on the electronic and optical properties of the electron transport layer (ETL). Density functional theory (DFT) uses a quantum-mechanical approach to accurately predict the properties of different layers in PSCs, including the ETL. Titanium dioxide (TiO₂) is a widely used material for the ETL in PSCs. In this work, we use first-principles calculations based on DFT to obtain the electronic and optical properties of pristine rutile TiO₂ and TiO₂ doped with tin (Sn) and zinc (Zn). DFT-extracted carrier mobility, band gap, and the absorption spectrum of TiO₂ are used in the SCAPS-1D device simulator to evaluate the performance of the solar cell device, with respect to dopant concentration and thickness of TiO₂. PSCs with 3.125 mol % Sn-doped TiO₂ achieve a maximum power conversion efficiency (PCE) of 17.14 versus 13.70% with undoped TiO₂. We have also compared the performance of PSCs with Sn-doped and Zn-doped TiO₂. For the same dopant concentration, Sn-doped TiO₂ offers 0.63% higher PCE than the Zn-doped counterpart. The results are in good agreement with reported experimental findings and provide a reliable means of evaluating PSC performance by combining first-principles (DFT) calculations with conventional device simulations.

![](./images/812300606965284865_1.jpg)

## 1. INTRODUCTION
Organic−inorganic lead halide perovskite solar cells (PSCs) have attracted a great deal of attention in recent years as a potential candidate to replace commercial silicon solar cells. Perovskites offer a direct band gap, a high optical absorption coefficient, broadband absorption, a long carrier lifetime, high carrier mobility, and easy fabrication through well-established, low-cost, solution-processing techniques. Developments in the perovskite technology have led to significant improvement in the power conversion efficiency (PCE) of PSCs, with the certified PCE increasing from 3.8% in 2009 to 25.2% in 2020,¹⁻⁴ exceeding the efficiency of existing copper−indium−gallium− selenide and cadmium−telluride (CdTe) solar cells. Electron and hole pairs are generated in the perovskite as it absorbs incident light photons with energy larger than the band gap of the perovskite. In a typical PSC, the light-absorbing perovskite is sandwiched between an electron transport layer (ETL) and a hole transport layer (HTL). MAPbX₃ is the most commonly used metal-halide perovskite, where MA represents methyl- ammonium and X is I, Cl or Br. The ETL consists of metal oxide thin films, typically made of titanium dioxide (TiO₂)⁵ or tin oxide (SnO₂),⁶ while Spiro-OMeTAD (2,2′,7,7′-tetrakis-(N,N- p-di-methoxy-phenylamino)-9,9′-spirobifluorene)⁷ is most commonly used as the HTL. Depending on the PSC device architecture, the built-in, internal electric field from the n-i-p or p-i-n heterojunction injects electrons into the ETL and holes into the HTL from the perovskite layer, thereby avoiding direct recombination. The charge transport layers, therefore, plays a major role in extracting and transporting the photogenerated charge carriers from the perovskite absorber layer to the respective anode and cathode electrodes. Several factors, such as the presence of interfacial defects, thickness, doping, carrier injection rate, absorption spectrum, and chemical stability of the transport layers, determine the performance of the PSC device.⁸,⁹ In addition to numerous experimental efforts, researchers have also used electrical and optical simulations to optimize the ETL and HTL layers for improving device performance.¹⁰,¹¹ Solar cell capacitance simulator one dimen- sion (SCAPS-1D) software has been extensively applied to extract basic electrical characteristics and determine the PCE of PSCs.¹²⁻¹⁴ Despite the considerable success of SCAPS-1D in predicting PSC performance, the accuracy, with which different transport layers are modeled, can be compromised by using built-in absorption spectrums in SCAPS-1D. Device simulators, like SCAPS-1D, employ a simplified combination of power laws

---

Received: March 15, 2021
Revised: June 1, 2021
Published: June 11, 2021

![](./images/812300606965284865_2.jpg)

---

© 2021 American Chemical Society
13158
https://doi.org/10.1021/acs.jpcc.1c02302
J. Phys. Chem. C 2021, 125, 13158−13166

![](./images/812300606965284865_3.jpg)

Figure 1. (a) Schematic of the simulated device structure; (b) energy band diagram of the simulated device.

to derive the absorption spectrum as a function of photon energy. This may often lead to unrealistic outputs, creating discrepancies between simulation and experimental results, as discussed in the recent work by Laali et al.¹⁵

Light absorption and charge carrier diffusion are governed by fundamental properties like the material band gap, dielectric constant, and effective mass of the carriers, which can be computed, within the quantum-mechanical approach, under various conditions (e.g., doping, temperature, and so forth) by using density functional theory (DFT) calculations.¹⁶ Recently, several studies have used DFT as an independent tool to study the material properties of solar cells. Giorgi et al. used DFT analysis to investigate the role played by the MA cation in determining the band structure of MAPbI₃.¹⁷ Ma et al., on the other hand, developed a set of algorithms based on DFT and time-dependent DFT calculations to accurately predict the PCE of dye-sensitized solar cells.¹⁸ Akbari et al. employed first-principles calculations to investigate the stability and electronic structure of perovskite/TiO₂ and perovskite/Al₂O₃ interfaces.¹⁹ A comprehensive DFT study was performed by Rahman et al. to extract the optical constant, energy band gap, and effective mass of charge carriers in MAPbCl₃, MAPbBr₃ and MAPbI₃ perovskites under different concentrations of halogen dopants.²⁰ Besides, defects in perovskites were thoroughly examined by Yin et al. using first-principles DFT methods.²¹ Kumar et al. employed SCAPS 1-D software to study the performance of lead-free double PSCs, where the band gap analysis was done using DFT.²² Till date, most of the DFT studies have focused on exploring the fundamental properties of the perovskite layer. There have only been a few attempts to theoretically investigate the structural, electronic, and optical properties of the transport layers in PSCs through first-principles calculations.²³⁻²⁶

For the ETL in PSCs, TiO₂ has been the primary material of choice owing to its non-toxic nature, high chemical stability, transparency to solar radiation, and easy fabrication. In addition, TiO₂ offers a fast injection of photogenerated electrons from the perovskite layer. A recent study by Zhang et al. demonstrated PSCs with dopamine-capped TiO₂ nanoparticles as the ETL, providing long-term stability and enhanced charge-extraction efficiency at the TiO₂ and perovskite interface.²⁷ Additionally, pristine TiO₂ can be doped with a variety of dopants to enhance electron mobility and reduce electronic trap states. The dopants for TiO₂ can be alkali metals,⁵ non-metals,²⁸ transition metals,²⁹ post-transition metals,³⁰ metalloids,³¹ and lanthanides.³²

Among a myriad of potential dopants, tin (Sn) and zinc (Zn) have been demonstrated as excellent candidates for doping TiO₂. Doping with Sn significantly improves charge carrier mobility and electrical conductivity of the pristine TiO₂.³³ Zn-doped TiO₂, on the other hand, is of low cost and offers excellent transport properties along with a reduced trap-state density.²⁹,³⁴

In this work, we use first-principles DFT calculations to extract the electronic and optical properties of pristine, Sn-doped, and Zn-doped TiO₂ films. First, the DFT-extracted optical absorption spectrum, band gap, and carrier mobilities of pristine TiO₂ and TiO₂ doped with different concentrations of Sn are used in the SCAPS-1D simulator to derive the electrical characteristics and PCE of the PSCs. In addition, the influence of ETL thickness, on device performance, has also been studied. The simulation results match closely with the experiments, reported by Cai et al.³³ Thus, combining DFT calculations with the SCAPS-1D device simulator provides the well-sought theoretical platform to predict PSC performance with high accuracy. Finally, for a fixed dopant concentration, we compare the performance of PSCs with Sn- and Zn-doped TiO₂ using the DFT-extracted parameters.

### 2. MODELING AND METHODS

#### 2.1. Device Architecture.
The schematic of the PSC device, simulated in this work, is shown in Figure 1a. The planar, one-dimensional heterostructure device has an n–i–p configuration, where the ETL (pristine TiO₂, 80 nm), perovskite (CH₃NH₃PbI₃, 310 nm), and HTL (Spiro-OMeTAD, 160 nm) serve as the n-type (n), intrinsic (i), and p-type (p) regions, respectively. To account for the interface recombination, the perovskite/TiO₂ interface layer (IL1) and the perovskite/Spiro-OMeTAD interface layer (IL2) have been considered during device simulations.³⁵,³⁶ The structure is illuminated from the top at normal incidence using the standard AM 1.5G spectrum (1 kW/m²) at 300 K. When irradiated with sunlight, excitons are generated in the perovskite layer. The electric field between the ETL (n-layer) and the HTL (p-layer) causes the electrons to migrate to the n-layer, while the holes are transported to the p-layer. Figure 1b illustrates the energy band diagram of the simulated device, clearly showing the separation and transportation of the photogenerated charge carriers.

#### 2.2. DFT Calculations.
The electronic structure and optical properties of many-body systems can be investigated, within the quantum-mechanical approach, using well-established DFT

**Table 1. Input Device Parameters Used in the SCAPS Simulation**$^{a}$

<table>
  <thead>
    <tr>
      <th>parameter</th>
      <th>ETL pristine rutile TiO₂</th>
      <th>IL1</th>
      <th>perovskite CH₃NH₃PbI₃</th>
      <th>IL2</th>
      <th>HTL Spiro-OMeTAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>thickness (nm)</td>
      <td>ᵞ80</td>
      <td>10</td>
      <td>ᵞ310</td>
      <td>10</td>
      <td>ᵞ160</td>
    </tr>
    <tr>
      <td>$N_{\text{a}}$ (cm⁻³)</td>
      <td>†1.00</td>
      <td>$5.21 × 10^{9}$</td>
      <td>†$5.21 × 10^{9}$</td>
      <td>$5.21 × 10^{9}$</td>
      <td>†$2.00 × 10^{18}$</td>
    </tr>
    <tr>
      <td>$N_{\text{d}}$ (cm⁻³)</td>
      <td>†$1.00 × 10^{19}$</td>
      <td>$5.21 × 10^{9}$</td>
      <td>†$5.21 × 10^{9}$</td>
      <td>$5.21 × 10^{9}$</td>
      <td></td>
    </tr>
    <tr>
      <td>$\varepsilon_{\text{s}}$</td>
      <td>†9.00</td>
      <td>6.50</td>
      <td>†6.50</td>
      <td>6.50</td>
      <td>†3.00</td>
    </tr>
    <tr>
      <td>$\chi$ (eV)</td>
      <td>†3.90</td>
      <td>3.90</td>
      <td>†3.90</td>
      <td>3.90</td>
      <td>†2.45</td>
    </tr>
    <tr>
      <td>$E_{\text{g}}$ (eV)</td>
      <td>*3.001</td>
      <td>1.55</td>
      <td>†1.55</td>
      <td>1.55</td>
      <td>†3.00</td>
    </tr>
    <tr>
      <td>$N_{\text{C}}$ (cm⁻³)</td>
      <td>†$1.00 × 10^{21}$</td>
      <td>$2.20 × 10^{18}$</td>
      <td>†$2.20 × 10^{18}$</td>
      <td>$2.20 × 10^{18}$</td>
      <td>†$1.00 × 10^{19}$</td>
    </tr>
    <tr>
      <td>$N_{\text{V}}$ (cm⁻³)</td>
      <td>†$2.00 × 10^{20}$</td>
      <td>$1.80 × 10^{19}$</td>
      <td>†$1.80 × 10^{19}$</td>
      <td>$1.80 × 10^{19}$</td>
      <td>†$1.00 × 10^{19}$</td>
    </tr>
    <tr>
      <td>$\mu_{\text{n}}$ (cm²/V s)</td>
      <td>*$11.54 × 10^{-4}$</td>
      <td>2.00</td>
      <td>†2.00</td>
      <td>2.00</td>
      <td>†$2.00 × 10^{-4}$</td>
    </tr>
    <tr>
      <td>$\mu_{\text{p}}$ (cm²/V s)</td>
      <td>*$8.90 × 10^{-4}$</td>
      <td>2.00</td>
      <td>†2.00</td>
      <td>2.00</td>
      <td>†$2.00 × 10^{-4}$</td>
    </tr>
    <tr>
      <td>$N_{\text{def}}$</td>
      <td>†$1.00 × 10^{15}$</td>
      <td>±$3.75 × 10^{16}$</td>
      <td>§$1.00 × 10^{13}$</td>
      <td>±$1.00 × 10^{13}$</td>
      <td>†$1.00 × 10^{15}$</td>
    </tr>
    <tr>
      <td>capture cross-section for electrons and holes</td>
      <td>†$1.00 × 10^{-15}$</td>
      <td>$2.00 × 10^{-14}$</td>
      <td>§$2.00 × 10^{-14}$</td>
      <td>$2.00 × 10^{-14}$</td>
      <td>†$1.00 × 10^{-15}$</td>
    </tr>
  </tbody>
</table>

$^{a}$*DFT-extracted; $^{\dagger}$Azri et al.;$^{10}$ $^{\text{Y}}$Cai et al.;$^{33}$ $^{\S}$Tan et al.;$^{13}$ $^{\pm}$Chouhan et al.$^{35}$

calculations. In this work, we used DFT, with Hubbard-based $U$ correction, namely, the DFT + $U$ method, to derive the absorption spectrum, electronic band gap, carrier effective mass, and mobility of the rutile polymorph of the pristine and doped TiO₂ films, which is the ETL of PSCs. The Hubbard $U$ model$^{37}$ was implemented to improve the accuracy in band gap calculations. The $U$ term affects the lattice parameters, expanding the cell as the $U$ value increases. In the DFT + $U$ scheme, the on-site coulombic ($U$) and exchange ($J$) terms were combined into a single effective $U$ parameter ($U_{\text{eff}}$) to account for errors in the exchange−correlation of Ti 3d and O 2p orbitals. The on-site Coulomb potential of $U_{\text{eff}} = 8.0$ eV on the d-orbital of Ti and $U_{\text{eff}} = 6.5$ eV on the p-orbital of oxygen (O) have been used in this calculation. The band gap of TiO₂, computed using these $U$ values, is in good agreement with the experimentally determined band gap found in the literature. For the Sn-doped case, $U_{\text{eff}} = 6.0$ eV has been used for the d-orbital of Sn. The choice of $U = 6.0$ eV for Sn is validated by computing the band gap of pure SnO₂. The results show that the DFT + $U$ calculated band gap of 3.52 eV is in good agreement with the experimentally determined band gap of 3.60 eV.$^{38}$ All DFT calculations were carried out using the Vienna $ab$ initio simulation package.$^{39,40}$ Projector augmented wave (PAW) pseudopotential$^{41}$ was used to account for the electron-ion core interaction, with the Perdew−Burke−Ernzerhof function as generalized gradient approximation$^{42}$ for the exchange−correlation term. A cutoff energy of 500 eV was used to expand the Kohn−Sham orbitals into plane-wave basis sets. The employed pseudopotentials correspond to the configurations $3\text{s}^{2}3\text{p}^{6}3\text{d}^{2}4\text{s}^{2}$ for Ti and $2\text{s}^{2}2\text{p}^{4}$ for O atoms. Reciprocal space projection was used for the PAW operators, with the projection operators optimized to an accuracy of $1.0 × 10^{-7}$ eV/Å. All calculations were spin-polarized and were geometrically optimized without symmetry or spin constraints. The structures converged when the forces on all atoms were less than 0.005 eV/Å. For the relaxation of the rutile TiO₂ unit cell, the $7 × 7 × 11$ Monkhorst−Pack scheme$^{43}$ and the Gaussian smearing model, with $\sigma = 0.05$, were used to integrate the Brillouin zone. High accuracy in energy and density of state (DOS) calculations originate from a denser mesh with a $11 × 11 × 17$ $k$-point grid. For modeling rutile TiO₂ doped with Sn, $4 × 2 × 2$, $3 × 2 × 2$, and $2 × 2 × 2$ TiO₂ supercells are created, which correspond to 3.125, 4.17, and 6.25 mol % Sn-doped TiO₂, respectively.

The carrier mobilities in pristine and doped TiO₂ are calculated using the BoltzTraP2 code$^{44}$ with the constant relaxation time approximation (CRTA) method. The DFT-extracted band structure is combined with the BoltzTraP2 code to calculate the carrier effective mass and mobility, with a relaxation time of $10^{-10}$ s.$^{45,46}$ The mobility calculations are discussed in detail in the Supporting Information. Table S1 of the Supporting Information presents the computed electron and hole mobilities of undoped and doped TiO₂ layers. An alternative technique, which combines the deformation potential (DP) method$^{47}$ with DFT-based effective mass approximation, can be used to compute carrier mobilities. However, mobility values, obtained from the DP method, do not agree well with the experimental findings.

The optical properties of pristine and doped TiO₂ are obtained using independent particle approximation which combines occupied and unoccupied bands to calculate the imaginary part of the dielectric function. The real part of the dielectric function is derived from the imaginary part using the Kramers−Kronig transform. The dielectric functions are then used to obtain the optical absorption spectrum as described in the Supporting Information. Different $k$-point mesh densities have been used to test the convergence of the absorption spectrum. The results show that the $7 × 7 × 11$, $4 × 4 × 3$, $4 × 4 × 4$, and $4 × 4 × 5$ $k$-point densities give well-converged optical spectra for pure TiO₂ and 3.125, 4.17, and 6.25 mol % Sn-doped TiO₂, respectively. For instance, Figure S2 of the Supporting Information shows excellent $k$-point convergence in the absorption spectrum for 4.17 mol % Sn-doped TiO₂. The optical absorption spectrum of each layer depends on its band gap, which can be tuned by using different dopants or by simply changing the concentration of a specific dopant. SCAPS-1D offers multiple models and sub-models$^{15}$ to generate the optical absorption spectrum of each layer. In this work, the absorption spectra of undoped and doped TiO₂ (ETL) are extracted from the DFT calculations. For CH₃NH₃PbI₃ (perovskite) and Spiro-OMeTAD (HTL), the absorption spectra, used in the device simulations, are obtained from those reported by Phillips et al.$^{48}$ and Filipič et al.,$^{49}$ respectively.

### 2.3. Device Modeling.
The current−voltage characteristics of the PSC are obtained using SCAPS-1D software by solving the following semiconductor equations under steady-state conditions as a function of the position coordinate $x^{10}$

![](./images/812300606965284865_4.jpg)

Figure 2. Supercell (top), band structure (middle), and PDOS (bottom) for (a) pristine rutile TiO₂ and (b) 3.125, (c) 4.17, and (d) 6.25 mol % Sn-doped TiO₂.

$$
\begin{aligned}
\frac{\partial^{2} \psi}{\partial^{2} x} & =-\frac{\partial E}{\partial x}=-\frac{\rho}{\varepsilon_{\mathrm{s}}}=-\frac{q}{\varepsilon_{\mathrm{s}}}\left[\mathrm{p}-\mathrm{n}+N_{\mathrm{d}}{ }^{+}(x)-N_{\mathrm{a}}{ }^{-}(x)\right. \\
& \left. \pm N_{\text {def }}(x)\right]
\end{aligned}
\tag{1}
$$

where, $\psi$, $q$, $\varepsilon_{\text{s}}$, and $E$ denote the electrostatic potential, electronic charge, relative permittivity of the medium, and the electric field across the p−n junction, respectively. The carrier density is given by p (holes) and n (electrons), while $N_{\mathrm{d}}{ }^{+}$and $N_{\mathrm{a}}{ }^{-}$are the ionized donor and acceptor densities, respectively. The defect density is given by $N_{\text{def}}$. The defect type is assumed to be neutral, having a Gaussian energetic distribution with a characteristic energy of 0.1 eV. The thermal velocity, for electrons and holes, is taken $10^{7}$ cm/s. The current densities are related to the carrier generation and recombination rates as follows:

$$
\frac{\partial j_{\mathrm{n}}}{\partial x}+G-R_{\mathrm{n}}(\mathrm{n}, \mathrm{p})=0 ;-\frac{\partial j_{\mathrm{p}}}{\partial x}+G-R_{\mathrm{p}}(\mathrm{n}, \mathrm{p})=0
\tag{2}
$$

where $j_{\mathrm{p}}$, and $j_{\mathrm{n}}$ are the electron and hole current densities, respectively, $G$ is the generation rate for the electron and hole pairs, and $R_{\mathrm{n}, \mathrm{p}}$ is the net recombination rate. Here, $j_{\mathrm{p}}$ and $j_{\mathrm{n}}$ depend on the respective carrier mobilities

$$
j_{\mathrm{n}}=q n \mu_{\mathrm{n}} E+q D_{\mathrm{n}} \frac{\partial \mathrm{n}}{\partial x} ; j_{\mathrm{p}}=q n \mu_{\mathrm{p}} E-q D_{\mathrm{p}} \frac{\partial \mathrm{p}}{\partial x}
\tag{3}
$$

with $D_{\mathrm{n}}$ and $D_{\mathrm{p}}$ being the electron and hole diffusion coefficients, respectively. $\mu_{\mathrm{n}}$ is the electron mobility, and $\mu_{\mathrm{p}}$ denotes the hole mobility. For the pristine and doped TiO₂ layers, $\mu_{\mathrm{n}}$ and $\mu_{\mathrm{p}}$ are derived from the DFT calculations. Table 1 summarizes the different input parameters used in the SCAPS-1D simulations, where $\chi$ is the electron affinity and $N_{\mathrm{c}}$ and $N_{\mathrm{v}}$ are the effective DOSs for the conduction and valence bands, respectively.

## 3. RESULTS AND DISCUSSION

### 3.1. Electronic Properties of TiO₂.
Figure 2 shows the supercells, with the DFT-derived energy band gap and the partial DOSs (PDOS) for pristine rutile TiO₂ as well as TiO₂ doped with 3.125, 4.17, and 6.25 mol % of Sn. Rutile TiO₂ has a tetragonal structure (space group $P4_{2}/mmm$ with Patterson symmetry $P4/mmm$) containing two Ti (cation) and four O (anion) atoms. For doped TiO₂, supercells (cubic) of TiO₂ are created by replacing the Ti atom with Sn. From the DOS, it is

observed that the valence band region is constructed by Ti 3d, O 2p, and Sn 4d orbitals, occupying the energy bands between 2.2 and 6 eV. The conduction band, on the other hand, consists of contributions from Ti 3d, O 2p, and Sn 5s orbitals occupying the energy bands between 0 and 5.8 eV. Therefore, depending on the concentration, the 4d and 5s orbitals of Sn modulate the conduction band minima (CBM) and the valence band maxima (VBM), resulting in changes in band gap. For pristine rutile TiO₂, the DFT-calculated band gap is 3.00 eV. When doped with Sn, the Sn 5s defect orbitals push the conduction band toward a higher energy, slightly changing the energy band gap from 2.98 eV (3.125 mol % Sn) to 2.99 eV (4.17 mol % Sn). The results are in good agreement with previously reported studies.³³ˢ⁰ˢ¹ At higher Sn concentrations (6.25 mol % Sn), the band gap decreases to 2.83 eV because of the larger number of valence electrons of Sn compared to Ti.

3.2. Optical Properties of TiO₂. The performance of the solar cell heavily depends on the absorption coefficient of the TiO₂ layer. Figure 3 shows a significant difference between the

![](./images/812300606965284865_5.jpg)

Figure 3. Absorption spectrum of pristine rutile TiO₂ obtained from DFT and SCAPS.

DFT-calculated absorption spectrum of pristine rutile TiO₂ and the default, analytical optical absorption spectrum, obtained from SCAPS. In the traditional SCAPS model, the optical absorption, $\alpha(\lambda)$, as a function of wavelength $(\lambda)$ is given by

$$
\alpha(\lambda)=\left(A+\frac{B}{h \nu}\right) \sqrt{h \nu-E_{\mathrm{g}}} \tag{4}
$$

where $h\nu$ is the incident photon energy, $E_{\text{g}}$ is the material band gap, and A (in $\mathrm{cm}^{-1} \mathrm{eV}^{-1 / 2}$) and B (in $\mathrm{cm}^{-1} \mathrm{eV}^{1 / 2}$) are the model parameters.⁵² From Figure 3, it is clear that in comparison with SCAPS, the DFT calculations yield a more realistic absorption profile for pristine rutile TiO₂, with significantly stronger absorption in the shorter, ultraviolet (UV) wavelength regions.³³ The default SCAPS spectrum, on the other hand, shows a considerably lower absorption profile throughout the entire wavelength range, which leads to an overestimation of the number of photons reaching the perovskite layer. Hence, the DFT-derived optical spectra more accurately predict the device performance, as discussed in the subsequent sections.

Figure 4a,b compares the absorption spectrum and transmittance between undoped and Sn-doped TiO₂ layers. Doping with Sn increases the optical band gap of TiO₂, causing the absorption edge to be blue-shifted, as shown in Figure 4a. Maximum absorption occurs in the UV region, below 400 nm, for both doped and undoped TiO₂. Doped TiO₂ samples exhibit enhanced transmittance, compared to the undoped counterpart. Figure 4b confirms that in the visible range, 3.125 mol % Sn-doped TiO₂ provides the highest transmittance, allowing a larger number of incident photons to pass through the ETL and reach the perovskite layer.

The indirect band gap, $E_{\text{g}}$, of pristine and doped TiO₂ can be derived from the absorption spectrum using the Kubelka−Munk formula³³ˢ³

$$
\alpha h \nu=C\left(h \nu-E_{\mathrm{g}}\right)^{2} \tag{5}
$$

where C is the proportionality constant. Figure 4c shows the optical band gaps derived from the Tauc plots, where Sn-doped TiO₂ films exhibit higher optical band gaps than the pristine TiO₂. As the Sn doping concentration is increased above 3.125 mol %, the optical band gap decreases from 3.196 eV (3.125 mol % Sn) and 3.146 eV (4.17 mol % Sn) to 3.088 eV (6.25 mol % Sn). This is consistent with the experimental findings by Cai et al.,³³ where the decrease in the optical band gap at high doping concentrations is attributed to the structural defects caused by the overdose of Sn dopants. The optical absorption spectrum and the corresponding band gaps obtained from the Tauc plots have been used as input parameters in the subsequent SCAPS-1D simulations to obtain the electrical characteristics of the PSC device.

3.3. Solar Cell Device Characteristics. The current−density versus voltage ($J-V$) graphs of pristine and Sn-doped rutile TiO₂ are shown in Figure 5a. For the undoped TiO₂, the simulated results are obtained using the DFT-extracted absorption spectrum as well as the default, built-in spectrum used in the SCAPS simulator. For the same input parameters, the $J-V$ curve, corresponding to the DFT-extracted absorption spectrum, matches more closely with the experimental results, reported by Cai et al.³³ Also, PSC with Sn-doped TiO₂ yields a higher PCE than the one with undoped TiO₂. Doping with Sn causes a positive shift in Fermi energy of pristine TiO₂, which

![](./images/812300606965284865_6.jpg)

Figure 4. DFT-extracted (a) absorption and (b) transmittance spectra of pristine and Sn-doped TiO₂; (c) Tauc plots, showing optical band gaps.

![](./images/812300606965284865_7.jpg)

Figure 5. (a) $J-V$ characteristics of PSC with pristine and Sn-doped TiO₂ layers and (b) corresponding IPCE curves.

![](./images/812300606965284865_8.jpg)

Figure 6. Effect of pristine and Sn-doped TiO₂ thickness on (a) $J_{sc}$, (b) $V_{oc}$, (c) FF, and (d) PCE of the solar cell.

improves the efficiency of electron injection. $^{33,54}$ Moreover, Sn-doped TiO₂ has a higher conductivity than the undoped counterpart, leading to more efficient electron extraction at the TiO₂/perovskite interface. Both these factors contribute to higher values of short-circuit current density ($J_{sc}$) and fill factor (FF) in PSCs with Sn-doped TiO₂. Also, reduced carrier recombination and improved charge collection and separation enhance the open-circuit voltage ($V_{oc}$) in Sn-doped TiO₂ PSCs. Table S2 of the Supporting Information summarizes the output photovoltaic parameters of PSCs with undoped and doped TiO₂. The PCE of the proposed device, with pristine rutile TiO₂ is 13.70%, whereas the PCEs for the Sn-doped TiO₂ devices are 17.14% (3.125 mol % Sn), 17.07% (4.17 mol % Sn), and 15.42% (6.25 mol % Sn), respectively. At a higher dose of Sn, electron trapping sites are introduced, which deteriorate the charge transport properties and increase absorption by the TiO₂ layer. The physical origin of decreased electron mobility at a high Sn content can also be justified based on the electronic structural changes obtained from the DFT calculations. Since the relaxation time is fixed, the mobility depends on the effective mass of the charge carriers which, in turn, relies on the VBM and CBM of the $E-k$ diagram. From the DOS, shown in Figure 2, it is clear that the contribution of the 5s orbital of Sn near CBM is flat compared to the contributions made by the 3d orbital of Ti and the 2p orbital of O. As the Sn concentration increases, it flattens the CBM even more, thereby increasing the effective mass of the electrons and decreasing the mobility. Consequently, the PCE decreases when the Sn content exceeds 3.125 mol %. $^{33}$ The corresponding incident-photon-to-electron conversion efficiency (IPCE) spectra are shown in Figure 5b, where the Sn-doped TiO₂ devices exhibit a higher IPCE for the wavelengths between 300 and 900 nm. Toward the short wavelength region, a majority of the incoming photons are absorbed by TiO₂ and the thick glass/FTO (fluorine-doped tin oxide), which forms the front contact, without reaching the perovskite layer. At wavelengths above 800 nm, the energy of the incident photons is less than the band gap of the perovskite and therefore cannot generate excitons. Although in practice, TiO₂ with less than 3.125 mol % Sn doping can yield a higher PCE, as demonstrated by Cai et al. $^{33}$ and Liao et al., $^{55}$ the DFT calculations at low doping concentrations are currently limited by our available computational resources. For example, 2 mol % Sn doping in TiO₂ results in a supercell with 150 atoms by replacing 1 Ti atom, out of 50 Ti atoms, with a single Sn atom. The computational resources used in this work can however handle a maximum of only 100 atoms.

The performance of PSCs also depends on the thickness of the TiO₂ layer, as displayed in Figure 6a−d. A thinner ETL facilitates electron extraction from the perovskite/TiO₂ interface and enhances the PCE by yielding higher $J_{sc}$. The open-circuit

![](./images/812300606965284865_9.jpg)

Figure 7. Top left: supercell $(3 \times 2 \times 2)$; bottom left: energy band diagram; right: PDOS of $TiO_{2}$ doped with 4.17 mol % Zn.

voltage $(V_{oc})$ remains nearly constant, indicating that there is no leakage of the charge carriers as the thickness of $TiO_{2}$ is increased. $^{56}$ Moreover, the thinner $TiO_{2}$ layer is more transparent to incoming solar radiation and offers lower series resistance and defect densities, contributing to the enhanced performance of the PSC device.

3.4. Doping $TiO_{2}$ with Zn. Zinc (Zn), when used as a dopant, modifies the electronic structure of $TiO_{2}$, enhancing its electrical conductivity. This leads to higher $J_{sc}$ and PCE in PSCs with Zn-doped $TiO_{2}$ when compared to PSCs with pristine $TiO_{2} \cdot^{34}$ The widespread use of Zn as a dopant material for $TiO_{2}$ is attributed to the low cost of Zn precursors. Moreover, Zn-doped $TiO_{2}$ is found to have a lower number of trap states when compared to undoped $TiO_{2}$ films. $^{29}$ Here, for a given doping concentration, we have compared the performance of PSCs with Sn-doped and Zn-doped $TiO_{2}$ using DFT-extracted energy band gaps, carrier mobilities, and absorption spectra. Figure 7 shows the supercell $(3 \times 2 \times 2)$, energy band diagram, and PDOS of $TiO_{2}$, doped with 4.17 mol % Zn, where $U_{eff}=10.8$ eV has been used for the d-orbital of Zn. Choosing the $U$ value as 10.8 eV yielded a band gap of 3.24 eV for pure ZnO, which matched very closely with the experimentally determined band gap of 3.25 eV, as demonstrated in our previous study. $^{57}$ The PDOS of Zn-doped $TiO_{2}$ shows the contribution of the 3d orbital of Zn, hybridized with the 2p-orbital of O, to form the VBM. This pushes the VBM toward the higher energy, reducing the band gap to 2.89 eV for 4.17 mol % Zn-doped $TiO_{2}$. The carrier mobilities are calculated using the CRTA method, with a relaxation time of $10^{-10}$ s, and are listed in Table S1 of the Supporting Information. From Figure 8a,b, it is clear that for any given wavelength, the 4.17 mol % Sn-doped $TiO_{2}$ is less absorbing, with higher transmittance than the Zn-doped counterpart. The $J_{sc}, V_{oc}, FF$, and PCE of the PSC with Zn-doped $TiO_{2}$ are $20.15$ mA/cm$^{2}$, 1.12 V, 0.73, and 16.44%, respectively. Figure 8c and Table S2 of the Supporting Information compare the current−voltage characteristics of PSCs with 4.17 mol % Sn- and Zn-doped $TiO_{2}$ films, having pristine $TiO_{2}$ as the reference. The results confirm that the PCE obtained from a PSC with 4.17 mol % Sn-doped $TiO_{2}$ is 0.63% higher than that obtained from a PSC with 4.17 mol % Zn-doped $TiO_{2}$. The corresponding IPCE plots are shown in Figure 8d.

![](./images/812300606965284865_10.jpg)

Figure 8. DFT-extracted (a) absorption and (b) transmittance spectrum; (c) $J-V$ characteristics and (d) IPCE curves of the solar cell device with pristine $TiO_{2}$ and 4.17 mol % Sn- and Zn-doped $TiO_{2}$ ETLs.

4. CONCLUSIONS

In summary, we have accurately derived the device characteristics of PSCs with pristine, Sn-doped, and Zn-doped $TiO_{2}$ as the ETL using the DFT-extracted absorption spectrum, band gap, and carrier mobility of $TiO_{2}$. The DFT calculations take into consideration the quantum-mechanical properties of the ETL and provide a more realistic absorption spectrum than the built-in spectrum in the SCAPS simulator. The current−voltage characteristics of the PSC with pristine $TiO_{2}$ showed that the absorption spectrum of $TiO_{2}$, obtained from SCAPS, clearly overestimates the solar cell performance. The DFT extracted spectrum, on the other hand, yields electrical characteristics that are in very good agreement with experimental results reported in

the literature. The excellent matching between the simulation and experimental results can be attributed to the appropriate choice of $U$ values and relaxation time for the DFT-computed absorption spectrum and carrier mobilities. A maximum PCE of $17.14\%$ is achieved for $3.125$ mol % Sn-doped TiO₂, which is $3.44\%$ higher than that of the PCE obtained with pristine TiO₂ films. A higher concentration of Sn degrades the device performance due to increased defect levels. The performance of the solar cell, with varying thicknesses of pristine and Sn-doped TiO₂, has also been investigated, with thinner TiO₂ layers ($\sim$20 nm) yielding the highest $J_{sc}$ and PCE. Comparing the PCE between $4.17$ mol % Sn- and Zn-doped TiO₂ layers, it is clear that PSCs with the Sn-doped ETL are slightly more efficient than those with the Zn-doped ones. The combination of DFT calculations and device simulations, as demonstrated in this study, can be further extended to include other layers, organic molecular additives, and metal dopants, paving the way for predicting the performance of PSCs with quantum-mechanical accuracy.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jpcc.1c02302.

Macroscopic charge carrier mobility calculations in TiO₂ using DFT; carrier mobilities of undoped and doped TiO₂ calculated with the CRTA method; calculation of optical properties of TiO₂ using DFT; PSC output characteristics obtained from SCAPS-1D using DFT-extracted parameters of undoped and doped TiO₂ (PDF)

## AUTHOR INFORMATION

### Corresponding Author
Mainul Hossain – Department of Electrical and Electronic Engineering, University of Dhaka, Dhaka 1000, Bangladesh;
orcid.org/0000-0001-9011-9029; Email: mainul.eee@du.ac.bd

### Authors
Sadiq Shahriyar Nishat – Department of Physics, University of Dhaka, Dhaka 1000, Bangladesh; orcid.org/0000-0003-4236-346X

Md. Jayed Hossain – Department of Electrical and Electronic Engineering, University of Dhaka, Dhaka 1000, Bangladesh; orcid.org/0000-0002-6685-7627

Faiyaz Elahi Mullick – Department of Electrical and Electronic Engineering, University of Dhaka, Dhaka 1000, Bangladesh

Alamgir Kabir – Department of Physics, University of Dhaka, Dhaka 1000, Bangladesh

Shaestagir Chowdhury – Department of Mechanical and Materials Engineering, Portland State University, Portland, Oregon 97201, United States

Sharnali Islam – Department of Electrical and Electronic Engineering, University of Dhaka, Dhaka 1000, Bangladesh; orcid.org/0000-0002-0218-7337

Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpcc.1c02302

### Author Contributions
∥S.S.N and M.J.H contributed equally to this work.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
No funding was received for this work. The authors thankfully acknowledge the technical support from Fab Lab DU at the University of Dhaka and the Bangladesh Research and Education Network (BdREN) for providing the necessary computational resources for this simulation study.

## REFERENCES
(1) Kim, J. Y.; Lee, J.-W.; Jung, H. S.; Shin, H.; Park, N.-G. High-Efficiency Perovskite Solar Cells. Chem. Rev. 2020, 120, 7867−7918.

(2) Nayak, P. K.; Mahesh, S.; Snaith, H. J.; Cahen, D. Photovoltaic Solar Cell Technologies: Analysing the State of the Art. Nat. Rev. Mater. 2019, 4, 269−285.

(3) Roy, P.; Kumar Sinha, N.; Tiwari, S.; Khare, A. A Review on Perovskite Solar Cells: Evolution of Architecture, Fabrication Techniques, Commercialization Issues and Status. Sol. Energy 2020, 198, 665−688.

(4) Li, N.; Niu, X.; Chen, Q.; Zhou, H. Towards Commercialization: The Operational Stability of Perovskite Solar Cells. Chem. Soc. Rev. 2020, 49, 8235−8286.

(5) Peter Amalathas, A.; Landová, L.; Conrad, B.; Holovský, J. Concentration-Dependent Impact of Alkali Li Metal Doped Mesoporous TiO₂ Electron Transport Layer on the Performance of CH₃NH₃PbI₃ Perovskite Solar Cells. J. Phys. Chem. C 2019, 123, 19376−19384.

(6) Ke, W.; Fang, G.; Liu, Q.; Xiong, L.; Qin, P.; Tao, H.; Wang, J.; Lei, H.; Li, B.; Wan, J.; Yang, G.; Yan, Y. Low-Temperature Solution-Processed Tin Oxide as an Alternative Electron Transporting Layer for Efficient Perovskite Solar Cells. J. Am. Chem. Soc. 2015, 137, 6730−6733.

(7) Shariatinia, Z. Recent Progress in Development of Diverse Kinds of Hole Transport Materials for the Perovskite Solar Cells: A Review. Renew. Sustain. Energy Rev. 2020, 119, 109608.

(8) Le Corre, V. M.; Stolterfoht, M.; Perdigón Toro, L.; Feuerstein, M.; Wolff, C.; Gil-Escrig, L.; Bolink, H. J.; Neher, D.; Koster, L. J. A. Charge Transport Layers Limiting the Efficiency of Perovskite Solar Cells: How to Optimize Conductivity, Doping, and Thickness. ACS Appl. Energy Mater. 2019, 2, 6280−6287.

(9) Cho, A.-N.; Park, N.-G. Impact of Interfacial Layers in Perovskite Solar Cells. ChemSusChem 2017, 10, 3687−3704.

(10) Azri, F.; Meftah, A.; Sengouga, N.; Meftah, A. Electron and Hole Transport Layers Optimization by Numerical Simulation of a Perovskite Solar Cell. Sol. Energy 2019, 181, 372−378.

(11) Hima, A.; Lakhdar, N.; Benhaoua, B.; Saadoune, A.; Kemerchou, I.; Rogti, F. An Optimized Perovskite Solar Cell Designs for High Conversion Efficiency. Superlattices Microstruct. 2019, 129, 240−246.

(12) Haidari, G. Comparative 1D Optoelectrical Simulation of the Perovskite Solar Cell. AIP Adv. 2019, 9, 085028.

(13) Tan, K.; Lin, P.; Wang, G.; Liu, Y.; Xu, Z.; Lin, Y. Controllable Design of Solid-State Perovskite Solar Cells by SCAPS Device Simulation. Solid State Electron. 2016, 126, 75−80.

(14) Chakraborty, K.; Choudhury, M. G.; Paul, S. Numerical Study of Cs₂TiX₆ (X = Br⁻, I⁻, F⁻ and Cl⁻) Based Perovskite Solar Cell Using SCAPS-1D Device Simulation. Sol. Energy 2019, 194, 886−892.

(15) Laali, J.; Hamedani, A.; Alahyarizadeh, G.; Minuchehr, A. Performance Analysis of the Perovskite Solar Cells by a Realistic, DFT-Accurate Optical Absorption Spectrum. Superlattices Microstruct. 2020, 143, 106551.

(16) Le Bahers, T.; Rérat, M.; Sautet, P. Semiconductors Used in Photovoltaic and Photocatalytic Devices: Assessing Fundamental Properties from DFT. J. Phys. Chem. C 2014, 118, 5997−6008.

(17) Giorgi, G.; Fujisawa, J.-I.; Segawa, H.; Yamashita, K. Cation Role in Structural and Electronic Properties of 3D Organic−Inorganic Halide Perovskites: A DFT Analysis. J. Phys. Chem. C 2014, 118, 12176−12183.

(18) Ma, W.; Jiao, Y.; Meng, S. Predicting Energy Conversion Efficiency of Dye Solar Cells from First Principles. J. Phys. Chem. C 2014, 118, 16447−16457.

(19) Akbari, A.; Hashemi, J.; Mosconi, E.; De Angelis, F.; Hakala, M. First Principles Modelling of Perovskite Solar Cells Based on $TiO_2$ and $Al_2O_3$: Stability and Interfacial Electronic Structure. J. Mater. Chem. A 2017, 5, 2339−2345.

(20) Rahman, N. M.; Adnaan, M.; Adhikary, D.; Islam, M.; Alam, M. K. First-Principles Calculation of the Optoelectronic Properties of Doped Methylammonium Lead Halide Perovskites: A DFT-Based Study. Comput. Mater. Sci. 2018, 150, 439−447.

(21) Yin, W.-J.; Shi, T.; Yan, Y.; Yin, W.; Shi, T.; Yan, Y. Unusual Defect Physics in $CH_3NH_3$ $PbI_3$ Perovskite Solar Cell Absorber. Appl. Phys. Lett. 2014, 104, 063903.

(22) Kumar, M.; Raj, A.; Kumar, A.; Anshul, A. Theoretical Evidence of High Power Conversion Efficiency in Double Perovskite Solar Cell Device. Opt. Mater. 2020, 111, 110565.

(23) Arroyo-De Dompablo, M. E.; Morales-García, A.; Taravillo, M. DFT+U Calculations of Crystal Lattice, Electronic Structure, and Phase Stability under Pressure of $TiO_2$ Polymorphs. J. Chem. Phys. 2011, 135, 054503.

(24) Kamisaka, H.; Suenaga, T.; Nakamura, H.; Yamashita, K. DFT-Based Theoretical Calculations of Nb- and W-Doped Anatase $TiO_2$: Complex Formation between W Dopants and Oxygen Vacancies. J. Phys. Chem. C 2010, 114, 12777−12783.

(25) Xie, K.; Jia, Q.; Wang, Y.; Zhang, W.; Xu, J. The Electronic Structure and Optical Properties of Anatase $TiO_2$ with Rare Earth Metal Dopants from First-Principles Calculations. Materials 2018, 11, 179.

(26) Ghuman, K. K.; Singh, C. V. A DFT + U Study of (Rh, Nb)-Codoped Rutile $TiO_2$. J. Phys.: Condens. Matter 2013, 25, 085501.

(27) Zhang, Y.; Liu, X.; Li, P.; Duan, Y.; Hu, X.; Li, F.; Song, Y. Dopamine-Crosslinked $TiO_2$/Perovskite Layer for Efficient and Photostable Perovskite Solar Cells under Full Spectral Continuous Illumination. Nano Energy 2019, 56, 733−740.

(28) Xiang, P.; Lv, F.; Xiao, T.; Jiang, L.; Tan, X.; Shu, T. Improved Performance of Quasi-Solid-State Dye-Sensitized Solar Cells Based on Iodine-Doped $TiO_2$ Spheres Photoanodes. J. Alloys Compd. 2018, 741, 1142−1147.

(29) Liu, X.; Wu, Z.; Zhang, Y.; Tsamis, C. Low Temperature Zn-Doped $TiO_2$ as Electron Transport Layer for 19% Efficient Planar Perovskite Solar Cells. Appl. Surf. Sci. 2019, 471, 28−35.

(30) Kim, J. Y.; Rhee, S.; Lee, H.; An, K.; Biswas, S.; Lee, Y.; Shim, J. W.; Lee, C.; Kim, H. Universal Elaboration of Al-Doped $TiO_2$ as an Electron Extraction Layer in Inorganic−Organic Hybrid Perovskite and Organic Solar Cells. Adv. Mater. Interfaces 2020, 7, 1902003.

(31) Shi, X.; Ding, Y.; Zhou, S.; Zhang, B.; Cai, M.; Yao, J.; Hu, L.; Wu, J.; Dai, S.; Nazeruddin, M. K. Enhanced Interfacial Binding and Electron Extraction Using Boron-Doped $TiO_2$ for Highly Efficient Hysteresis-Free Perovskite Solar Cells. Adv. Sci. 2019, 6, 1901213.

(32) Zhang, B.; Song, Z.; Jin, J.; Bi, W.; Li, H.; Chen, C.; Dai, Q.; Xu, L.; Song, H. Efficient Rare Earth Co-Doped $TiO_2$ Electron Transport Layer for High-Performance Perovskite Solar Cells. J. Colloid Interface Sci. 2019, 553, 14−21.

(33) Cai, Q.; Zhang, Y.; Liang, C.; Li, P.; Gu, H.; Liu, X.; Wang, J.; Shentu, Z.; Fan, J.; Shao, G. Enhancing Efficiency of Planar Structure Perovskite Solar Cells Using Sn-Doped $TiO_2$ as Electron Transport Layer at Low Temperature. Electrochim. Acta 2018, 261, 227−235.

(34) Wu, M.-C.; Chan, S.-H.; Jao, M.-H.; Su, W.-F. Enhanced Short-Circuit Current Density of Perovskite Solar Cells Using Zn-Doped $TiO_2$ as Electron Transport Layer. Sol. Energy Mater. Sol. Cells 2016, 157, 447−453.

(35) Chouhan, A. S.; Jasti, N. P.; Avasthi, S. Effect of Interface Defect Density on Performance of Perovskite Solar Cell: Correlation of Simulation and Experiment. Mater. Lett. 2018, 221, 150−153.

(36) Baktash, A.; Amiri, O.; Sasani, A. Improve Efficiency of Perovskite Solar Cells by Using Magnesium Doped ZnO and $TiO_2$ Compact Layers. Superlattices Microstruct. 2016, 93, 128−137.

(37) Anisimov, V. I.; Zaanen, J.; Andersen, O. K. Band Theory and Mott Insulators: Hubbard U Instead of Stoner I. Phys. Rev. B: Condens. Matter Mater. Phys. 1991, 44, 943−954.

(38) Ahmed, A. S.; Shafeeq, M.; Singla, M. L.; Tabassum, S.; Naqvi, A. H.; Azam, A. Band Gap Narrowing and Fluorescence Properties of Nickel Doped $SnO_2$ Nanoparticles. J. Lumin. 2011, 131, 1−6.

(39) Kresse, G.; Hafner, J. Ab Initio Molecular Dynamics for Liquid Metals. Phys. Rev. B: Condens. Matter Mater. Phys. 1993, 47, 558−561.

(40) Paier, J.; Hirschl, R.; Marsman, M.; Kresse, G. The Perdew-Burke-Ernzerhof Exchange-Correlation Functional Applied to the G2-1 Test Set Using a Plane-Wave Basis Set. J. Chem. Phys. 2005, 122, 234102.

(41) Blöchl, P. E. Projector Augmented-Wave Method. Phys. Rev. B: Condens. Matter Mater. Phys. 1994, 50, 17953.

(42) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996, 77, 3865−3868.

(43) Monkhort, H. J.; Pack, J. D. Special Points for Brilloin-Zone Integrations. Phys. Rev. B: Solid State 1976, 13, 5188−5192.

(44) Madsen, G. K. H.; Carrete, J.; Verstraete, M. J. BoltzTraP2, a Program for Interpolating Band Structures and Calculating Semi-Classical Transport Coefficients. Comput. Phys. Commun. 2018, 231, 140−145.

(45) Ozawa, K.; Emori, M.; Yamamoto, S.; Yukawa, R.; Yamamoto, S.; Hobara, R.; Fujikawa, K.; Sakama, H.; Matsuda, I. Electron-Hole Recombination Time at $TiO_2$ Single-Crystal Surfaces: Influence of Surface Band Bending. J. Phys. Chem. Lett. 2014, 5, 1953−1957.

(46) Yamada, Y.; Kanemitsu, Y. Determination of Electron and Hole Lifetimes of Rutile and Anatase $TiO_2$ Single Crystals. Appl. Phys. Lett. 2012, 101, 133907.

(47) Bardeen, J.; Shockley, W. Deformation Potentials and Mobilities in Non-Polar Crystals. Phys. Rev. 1950, 80, 72−80.

(48) Phillips, L. J.; Rashed, A. M.; Treharne, R. E.; Kay, J.; Yates, P.; Mitrovic, I. Z.; Weerakkody, A.; Hall, S.; Durose, K. Dispersion Relation Data for Methylammonium Lead Triiodide Perovskite Deposited on a (100) Silicon Wafer Using a Two-Step Vapour-Phase Reaction Process. Data Br. 2015, 5, 926−928.

(49) Filipič, M.; Löper, P.; Niesen, B.; De Wolf, S.; Krč, J.; Ballif, C.; Topič, M. $CH_3NH_3PbI_3$ Perovskite/Silicon Tandem Solar Cells: Characterization Based Optical Simulations. Opt. Express 2015, 23, A263−A278.

(50) Long, R.; Dai, Y.; Meng, G.; Huang, B. Energetic and Electronic Properties of X- (Si, Ge, Sn, Pb) Doped $TiO_2$ from First-Principles. Phys. Chem. Chem. Phys. 2009, 11, 8165−8172.

(51) Long, R.; Dai, Y.; Huang, B. Geometric and Electronic Properties of Sn-Doped $TiO_2$ from First-Principles Calculations. J. Phys. Chem. C 2009, 113, 650−653.

(52) Burgelman, M.; Decock, K.; Niemegeers, A.; Verschraegen, J.; Degrave, S. SCAPS Manual, Ferbruary, 2019.

(53) Xu, R.; Li, Y.; Feng, S.; Wang, J.; Zhang, J.; Zhang, X.; Bian, C.; Fu, W.; Li, Z.; Yang, H. Enhanced Performance of Planar Perovskite Solar Cells Using Ce-Doped $TiO_2$ as Electron Transport Layer. J. Mater. Sci. 2020, 55, 5681−5689.

(54) Gao, X.-X.; Ge, Q.-Q.; Xue, D.-J.; Ding, J.; Ma, J.-Y.; Chen, Y.-X.; Zhang, B.; Feng, Y.; Wan, L.-J.; Hu, J.-S. Tuning the Fermi-Level of $TiO_2$ Mesoporous Layer by Lanthanum Doping towards Efficient Perovskite Solar Cells. Nanoscale 2016, 8, 16881−16885.

(55) Liao, Y.-H.; Chang, Y.-H.; Lin, T.-H.; Chan, S.-H.; Lee, K.-M.; Hsu, K.-H.; Hsu, J.-F.; Wu, M.-C. Boosting the Power Conversion Efficiency of Perovskite Solar Cells Based on Sn Doped $TiO_2$ Electron Extraction Layer via Modification of the $TiO_2$ Phase Junction. Sol. Energy 2020, 205, 390−398.

(56) Shalan, A. E.; Narra, S.; Oshikiri, T.; Ueno, K.; Shi, X.; Wu, H.-P.; Elshanawany, M. M.; Wei-Guang Diau, E.; Misawa, H. Optimization of a Compact Layer of $TiO_2$ via Atomic-Layer Deposition for High-Performance Perovskite Solar Cells. Sustain. Energy Fuels 2017, 1, 1533−1540.

(57) Ayon, S. A.; Billah, M. M.; Nishat, S. S.; Kabir, A. Enhanced Photocatalytic Activity of $Ho^{3+}$ Doped ZnO NPs Synthesized by Modified Sol-Gel Method: An Experimental and Theoretical Investigation. J. Alloys Compd. 2021, 856, 158217.