OPEN
# Thermoelectric properties of XX- and XY-stacked GeS/GeSe van der Waals heterostructures from DFT and BTP calculations

Fredy Mamani Gonzalo¹⁴, Maurício Jeomar Piotrowski², Eduardo Rodriguez Delgado¹, Carlos Armando Polo Bravo¹, Jesús Alfredo Chacaltana García¹, Jorge Sabino Ayala Arenas³ & Efracio Mamani Flores¹⁴<sup>✉</sup>

This study utilizes density functional theory (DFT) and the Boltzmann transport equation (BTE) to investigate the structural, electronic, and thermoelectric properties of germanium sulfide (GeS) and germanium selenide (GeSe) monolayers, along with their van der Waals (vdW) heterostructures. We analyzed XX-stacked and XY-stacked configurations, where the XX configuration features direct atomic stacking, while the XY configuration exhibits staggered stacking. Our first-principles calculations indicate that the formation of GeS/GeSe heterostructures results in a reduction of bandgaps compared to their bulk and monolayer counterparts, yielding bandgap values of 0.91 eV for the XX configuration and 0.84 eV for the XY configuration. Stability assessments reveal that the XY configuration is more stable, demonstrating a lattice thermal conductivity of 15.21 W/mK compared to 17.95 W/mK for the XX configuration T 300 K. The thermoelectric properties were systematically evaluated across a temperature range of 300–800 K, revealing high Seebeck coefficients of 1.51 mV/K for the XX heterostructure and 1.39 mV/K for the XY heterostructure. reflecting their excellent charge transport capabilities. Notably, the figure of merit (ZT) at 800 K was calculated to be 0.90 for the XX configuration and 1.01 for the XY configuration, underscoring the superior thermoelectric performance of the XY heterostructure. These findings contribute to a comprehensive understanding of 2D GeS/GeSe heterostructures for thermoelectric applications and provide a solid foundation for future research and technological advancements in this domain.

In an era where environmental pollution represents a serious threat to life on Earth¹⁻³, research has increasingly focused on mitigating this problem through new technologies and sustainable energy conversion methods. These efforts aim to replace fossil fuels, which contribute to environmental pollution by releasing greenhouse gases that have detrimental effects on our ecosystem⁴⁻⁷. Renewable technologies such as solar cells have emerged as promising alternatives by harnessing the abundant energy resources provided by the sun⁸⁻¹⁰. Another notable approach is thermoelectric (TE) materials as an alternative to harness wasted energy such as heat emitted by electronic devices, body heat, and solar radiation, through the Seebeck effect, heat is directly converted into electrical energy. However, there are still challenges to obtain high thermoelectric efficiency so the search continues. One way to study the physical properties of a large number of materials is through theoretical predictions since they provide a cost-effective and efficient way in materials exploration and design, ultimately accelerating the discovery of new thermoelectric materials, in this way, it also helps to attack the environmental problem¹¹⁻¹⁶. Numerous studies are currently being conducted to improve the efficiency of thermoelectric materials¹⁷⁻²³.

The efficiency of thermoelectric materials at a specific temperature is determined by the dimensionless figure of merit (ZT), which is given by the following equation

---

¹Department of Physics, Jorge Basadre Grohmann National University, Tacna, Peru. ²Department of Physics, Federal University of Pelotas, Pelotas, Rio Grande do Sul, Brazil. ³Department of Physics, National University of San Agustín de Arequipa, Arequipa, Peru. ⁴These authors contributed equally to this work. ✉email: emamanif@unjbg.edu.pe

$$
ZT = \frac{S^{2}\sigma}{(\kappa_{e} + \kappa_{l})}T, \tag{1}
$$

where $S$, $\sigma$, $\kappa_e$, $\kappa_l$, and $T$ are the Seebeck coefficient, electrical conductivity, electronic thermal conductivity, lattice thermal conductivity, and the absolute temperature, respectively$^{24}$. In this equation, $S^2\sigma$ is commonly referred to as the power factor (PF) of thermoelectric materials. A high ZT value indicates a high energy conversion efficiency, which is achieved with a high Seebeck coefficient and high electrical conductivity but low thermal conductivity. However, balancing these parameters is challenging because of their interdependent nature, making it difficult to achieve the desired inverse relationship between electrical and thermal transport properties.

The primary composition of the major thermoelectric materials currently on the market and those expected to emerge in the near future are predominantly centered on tellurides$^{25-27}$. However, there are significant limitations to the use of tellurium, and a notable challenge is its high cost due to its scarcity in the Earth's crust, therefore, it is advantageous to discover new materials that reduce the dependence on Te. A great alternative lies in GeS and GeSe, in addition to their abundance on Earth, these materials feature lower toxicity, environmental compatibility, and chemical stability$^{28}$, these properties make them suitable for a wide range of applications, such as high-sensitivity photodetectors$^{29}$ or gas sensing$^{30}$. Furthermore, it has been shown that GeS and GeSe demonstrate high thermoelectric efficiency in their orthorhombic phase$^{31}$, likewise, experimental studies have shown that doping GeSe with Na helps to decrease the thermal conductivity to 1.06 W/mK at 300 K, in addition, GeS and GeSe are shown to be non-toxic$^{28}$. Likewise, a high $ZT = 2.12$ was predicted for n-doped $Pnma$ GeSe at 900 K$^{32}$, while, for GeS a maximum figure of merit of 0.73 at 700 K was calculated$^{33}$. On the other hand, the bilayer setup showed a maximum $ZT$ of 1.95 in armchair direction for electron doping in bilayer GeSe$^{34}$. Hao et al.$^{35}$ employed first-principles-based methods to predict a substantial enhancement in the $ZT$ in hole-doped GeSe crystals oriented along the crystallographic $b$-axis, with maximum $ZT$ values ranging from 0.8 at 300 K to 2.5 at 800 K. Subsequently, Rakshit et al.$^{33}$ revealed that GeS possesses a maximum $ZT$ of approximately 0.73 at 700 K. Additionally, Zhao et al.$^{36}$ reported a ZT of about 1.3 at 923 K, and Lee et al.$^{37}$ determined an enhanced performance in PbSe-based materials, achieving a thermoelectric figure of merit of approximately 1.5 at 800 K. Many other studies have demonstrated significant potential for improving ZT values$^{38-42}$, indicating promising thermoelectric properties$^{43,44}$.

As another strategy to improve physical properties, researchers have shown that constructing heterostructures can lead to improvements in their properties compared to the pristine material$^{45-47}$, furthermore, numerous findings confirmed that monochalcogenide-based heterostructures are promising for high-efficiency solar cell$^{48}$, optoelectronics$^{49}$, photocatalysis$^{50}$, thermal energy harvesting$^{51}$, and essentially, a great improvement in $ZT$ has been demonstrated for SnSe/SnS heterostructure$^{32}$.

Inspired by these intriguing features of heterostructures, especially for studies of monochalcogenide materials, we investigate the thermoelectric properties of bulk and monolayer (ML) GeS and GeSe as well as GeS/GeSe heterostructures by computational simulation employing the density functional theory (DFT) and Boltzmann transport theory (BTT) approach to systematically explore the Seebeck coefficients ($S$), electrical conductivity ($\sigma$), electronic thermal conductivity ($\kappa_e$), and the $ZT$ of GeS/GeSe XX and GeS/GeSe XY vdW heterostructures.

### Computational methodology
The structural and electronic properties of bulk materials, monolayers (GeS and GeSe), and their heterostructures were investigated using first-principles DFT calculations performed within the Quantum Espresso package$^{53}$. Stability was assessed through ab-initio molecular dynamics (AIMD) simulations conducted with the Vienna Ab initio Simulation Package (VASP)$^{54}$ and Phonopy$^{55}$. The exchange-correlation energy was modeled using the generalized gradient approximation (GGA) parameterized by Perdew, Burke, and Ernzerhof (PBE)$^{56}$. However, standard DFT functionals like PBE often underestimate the bandgaps of semiconductors and insulators. To overcome this limitation, we employed the range-separated hybrid Heyd-Scuseria-Ernzerhof (HSE06) functional$^{57,58}$ calculated using VASP. Additionally, to capture the long-range van der Waals (vdW) interactions crucial for layered monolayers and heterostructures, we incorporated the dispersion-corrected DFT-D3 scheme$^{59}$. Structural relaxations were conducted until the forces on all atoms were below $10^{-}$ Ry/Bohr, and the stress components were under 0.5 kbar. The Brillouin zone was sampled using a Monkhorst-Pack$^{60}$ $\mathbf{k}$-point mesh of $8 \times 8 \times 8$ for bulk materials and $6 \times 6 \times 1$ for monolayers, a shown in Fig. 1a and b. A kinetic energy cutoff of 70 Ry for the plane-wave basis set was utilized, with a convergence study performed (Figs. S2-S7). A vacuum region exceeding $20$ Å was included to eliminate spurious interactions between periodic images of monolayers and heterostructures.

To determine the thermal conductivity of the lattice, both second-order (harmonic) and third-order (anharmonic) interatomic force constants (IFC) were employed. The second-order harmonic IFC was calculated using the finite displacement method with Phonopy$^{61}$, incorporating rotational summations according to the Born-Huang$^{62}$ constraints implemented in HiPhive$^{63}$. $7 \times 7 \times 1$ supercells and a $2 \times 2 \times 1$ $\mathbf{k}$-point mesh were used. For the third-order anharmonic IFC, $3 \times 3 \times 1$ supercells were employed with Phono3py$^{64}$, applying the linearized Boltzmann transport equation (LBTE)$^{65}$ and a $\mathbf{Q}$-grid of $65 \times 65 \times 1$ were employed. The anharmonic IFC calculation was performed with a cutoff radius greater than 7.57 Å. Since the conductivity in the $z$ direction influences the results for a 2D material, a scaling factor was applied by multiplying by $h_z = z/h_{eff}$, where $z$ is the unit cell length in the $z$ direction and $h_{eff}$ is the effective monolayer thickness, considering van der Waals radii of 1.93 Å of Ge which is located on top and bottom of all monolayers an heterostructures, and evaluating the conductivity tensors in the $x$ and $y$ directions. Finally, a dense $\mathbf{k}$-point mesh of $150 \times 150 \times 1$ and $100 \times 100 \times 1$ was used for monolayers and heterostructures, respectively.

![](./images/1061484690508087319_1.jpg)

Fig. 1. Top view: (a–d) and side view: (e–h) of GeS monolayer, GeSe monolayer, GeS/GeSe XX, and GeS/GeSe vdW heterostructures. The lattice parameters are $a$ and $b$. The bond lengths between the atoms are $d_1$ and $d_2$ , and the bond angles are represented by $\theta_1$ and $\theta_2$. $d_{spacing}$ is the distance between the monolayers in the GeS/ GeSe XX and GeS/GeSe XY vdW heterostructures.

The heterostructures were constructed by stacking GeS and GeSe monolayers in XX and XY sequences, in the XX sequence, the Ge atoms of GeSe and GeS are vertically aligned, as depicted in Fig. 1c and g. Conversely, in the XY sequence, the Ge atoms are laterally shifted, aligning with the S atoms of the GeS monolayer, as shown in Fig. 1d and h. The lattice mismatch between GeS and GeSe monolayers is calculated using the formula $|\Delta|=(l-l_0)/l$, where $l$ represents the lattice parameter along the $a$ (or $b$) direction of the top layer, and $l_0$ corresponds to the lattice parameter of the bottom layer. Considering only the puckered phase was considered for both monolayers, the heterostructures were fully relaxed using the PBE functional, with subsequent calculations based on these relaxed structures. To explore the thermoelectric properties of the relaxed heterostructures, we computed the electron transport properties, including $S$, $\sigma$, and $\kappa_e$, using the semi-classical BTE as implemented in the BoltzTraP2 code⁶⁶ over a temperature range of 300–800 K. The BoltzTraP2 code evaluates the transport distribution function (TDF) by Fourier expanding the band energies derived from the DFT calculations. Subsequently, the electrical conductivity tensor $\sigma_{\alpha\beta}$ and the Seebeck coefficient tensor $S_{\alpha\beta}$ are computed from the TDF using semi-classical expressions derived from the Boltzmann transport equation under the relaxation time approximation (RTA). These expressions are represented by Eqs. 2 and 3:

$$
S_{\alpha\beta}(T;\mu)=\frac{1}{eT}\frac{\int\sigma_{\alpha\beta}(\epsilon)(\epsilon-\mu)\left[-\frac{\partial f(T;\mu)}{\partial\epsilon}\right]d\epsilon}{\int\sigma_{\alpha\beta}(\epsilon)\left[-\frac{\partial f(T;\mu)}{\partial\epsilon}\right]d\epsilon}, \tag{2}
$$

$$
\sigma_{\alpha\beta}(T;\mu)=\frac{1}{\Omega}\int\sigma_{\alpha\beta}(\epsilon)\left[-\frac{\partial f_{\mu}(T;\epsilon)}{\partial\epsilon}\right]d\varepsilon, \tag{3}
$$

The electronic thermal conductivity tensor $\kappa_{\alpha\beta}^{el}$ is then determined from the Wiedemann-Franz law given by the Eq. 4:

$$
\kappa_{\alpha\beta}^{el}(T;\mu)=\frac{1}{e^2T\Omega}\int_{-\infty}^{+\infty}\sigma_{\alpha\beta}(\epsilon)(\epsilon-\mu)^2\left[-\frac{\partial f(T;\mu)}{\partial\epsilon}\right]d\epsilon, \tag{4}
$$

where $e$ represents the electric charge of an electron, $\Omega$ denotes the volume of reciprocal space, $\varepsilon$ stands for the carrier energy, $f$ represents the Fermi distribution function, $\mu$ denotes the chemical potential, and $T$ is the absolute temperature. These transport tensors provide valuable insights into the thermoelectric performance of the investigated heterostructures. The figure of merit ($ZT$) plays a crucial role in discussing thermoelectric properties as it indicates the efficiency of converting heat into electricity. As per Eq. 1, achieving a high $ZT$ necessitates high values of the Seebeck coefficient and electrical conductivity, while aiming for low electrical thermal conductivity. However, attaining these desired values is challenging, as suggested by the Wiedemann-Franz law⁶⁷, which states that a high value of $\sigma$ corresponds to a high value of $\kappa_e$ ($\kappa_e=\sigma LT$).

### Results and discussion
#### Structural properties
Our investigation commenced with a thorough examination of the bulk structures of GeS and GeSe, as illustrated in Fig. S1. We conducted meticulous convergence tests to determine the optimal computational settings for both the k-point mesh density and the plane-wave energy cutoff, as depicted in Figs. S2 and S3. Following the establishment of accurate computational parameters, we proceeded with structural optimization calculations to ascertain the lattice parameters of the bulk materials. For bulk GeS, our calculations revealed an orthorhombic crystal structure with the Pnma space group and optimized lattice parameters: $a = 3.67$ Å, $b = 4.44$ Å, and $c = 10.77$ Å. Similarly, bulk GeSe exhibited an orthorhombic Pnma symmetry, consistent with both theoretical predictions⁶⁸ and experimental measurements⁶⁹. Refer to Table S1 for detailed structural parameters of the bulk materials.

The primary monolayers of GeS and GeSe were derived by extracting layers from the three-dimensional GeS and GeSe bulk structures, both of which belong to the space group $Pmn2_1$. These monolayers can exhibit two distinct geometries: buckled (B)⁷⁰ and puckered (P)⁷¹. In our analysis, we focused on the puckered geometry for both, GeS and GeSe monolayer, as depicted in Fig. 1a and b. Our investigation revealed that the lattice parameters of the GeS monolayer are $a = 3.67$ Å and $b = 4.46$ Å, while for the GeSe monolayer, they are calculated as $a = 3.79$ Å and $b = 4.66$ Å. These values closely align with previous theoretical studies⁶⁸,⁷², as shown in Table 1.

Within these monolayers, strong covalent bonds are established, with each atom bonded to three atoms of the opposite type. The puckered geometric structures display distortions in the cation-anion bond angles, particularly evident in the side view along the $b$ direction for both the GeS and GeSe monolayers (see Fig. 1e–f). Importantly, these monolayers exhibit metastability, a characteristic observed in experimental fabrication processes⁷³⁻⁷⁵.

Following the examination of individual GeS and GeSe monolayers, we constructed vdW heterostructures by stacking them in different configurations: XX and XY. This involved optimizing the interlayer distance ($d_{spacing}$) between the GeS and GeSe monolayers to form a GeS/GeSe XX and GeS/GeSe XY vdW heterostructures, which exhibit unique structural properties resulting from the combination of distinct monolayer materials. For the GeS/GeSe vdW heterostructures, the optimized lattice parameters are $a = 3.73$ Å and $b = 4.56$ Å. Detailed information on the bond lengths ($d_{Ge-S(Se)}$ and $d_{S(Se)-Ge}$), bond angles ($\theta_{Ge-Ge}$ and $\theta_{S(Se)-S(Se)}$), and $d_{spacing}$ are provided in Table 1.

Furthermore, Table 1 presents the binding energy ($E_b$) and lattice mismatch ($\Delta$) between the GeS and GeSe monolayers for both the XX and XY heterostructure configurations. $E_b$ quantifies the strength of attractive interactions between the GeS and GeSe monolayers within the heterostructure. A more negative value of $E_b$ indicates stronger interlayer adhesion and a more stable heterostructure configuration (see Fig. 2). This parameter plays a crucial role in determining the overall stability and cohesiveness of the heterostructure, thereby influencing its structural integrity and potential applications.

To assess the stability of the vdW heterostructures, we computed the $E_b$ using Eq. 5:

$$
E_{b}=\frac{E_{A B}-\left(E_{A}+E_{B}\right)}{S}, \tag{5}
$$

where $E_A$ and $E_B$ represent the energies of the isolated monolayers, $E_{AB}$ is the total energy of the GeS/GeSe XX or XY vdW heterostructure, and S is the area of the unit cell. Our calculations reveal that the XY stacking configuration of the GeS/GeSe vdW heterostructures exhibits higher stability than the XX stacking. Specifically, the XY configuration demonstrates a significantly higher $E_b$ value of $-19.35$ meV/Å², compared to $-14.08$ meV/Å² for the XX stacking. This higher binding energy indicates greater thermodynamic stability for the XY configuration. Moreover, we determined the optimal interlayer distances corresponding to these binding energy values to be 3.32 Å and 2.92 Å for the XX and XY stackings, respectively (see Fig. 2).

To demonstrate the dynamic stability of GeS and GeSe monolayers as well as GeS/GeSe vdW heterostructures in XX and XY stacking configurations, we used phonon dispersion calculations, where the absence of imaginary

<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>Lattice parameters</th>
      <th>$d_{Ge-S(Se)}$</th>
      <th>$d_{S(Se)-Ge}$</th>
      <th>$\theta_{Ge-Ge}$ (°)</th>
      <th>$\theta_{S(Se)-S(Se)}$ (°)</th>
      <th>$d_{spacing}$</th>
      <th>$E_b$</th>
      <th>$\Delta$ a/b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">GeS</td>
      <td>$a = 3.67$ (3.67⁷²)</td>
      <td rowspan="2">$d_{Ge-S}=2.42$</td>
      <td rowspan="2">$d_{S-Ge}=2.45$</td>
      <td rowspan="2">104.8</td>
      <td rowspan="2">$\theta_{S-S}=93.90$</td>
      <td rowspan="2">-</td>
      <td rowspan="2">-</td>
      <td rowspan="2">-</td>
    </tr>
    <tr>
      <td>$b = 4.46$ (4.43⁷²)</td>
    </tr>
    <tr>
      <td rowspan="2">GeSe</td>
      <td>$a = 3.79$ (3.97⁷²)</td>
      <td rowspan="2">$d_{Ge-Se}=2.59$</td>
      <td rowspan="2">$d_{Se-Ge}=2.56$</td>
      <td rowspan="2">100.12</td>
      <td rowspan="2">$\theta_{Se-Se}=97.30$</td>
      <td rowspan="2">-</td>
      <td rowspan="2">-</td>
      <td rowspan="2">-</td>
    </tr>
    <tr>
      <td>$b = 4.66$ (4.27⁷²)</td>
    </tr>
    <tr>
      <td rowspan="2">GeS/GeSe XX</td>
      <td>$a = 3.73$</td>
      <td>$d_{Ge-S}=2.42$</td>
      <td>$d_{S-Ge}=2.45$</td>
      <td>104.8</td>
      <td>$\theta_{S-S}=93.90$</td>
      <td rowspan="2">3.32</td>
      <td rowspan="2">$-14.08$</td>
      <td rowspan="2">3.17/4.29</td>
    </tr>
    <tr>
      <td>$b = 4.56$</td>
      <td>$d_{Ge-Se}=2.56$</td>
      <td>$d_{Se-Ge}=2.59$</td>
      <td>99.92</td>
      <td>$\theta_{Se-Se}=95.75$</td>
    </tr>
    <tr>
      <td rowspan="2">GeS/GeSe XY</td>
      <td>$a = 3.73$</td>
      <td>$d_{Ge-S}=2.42$</td>
      <td>$d_{S-Ge}=2.45$</td>
      <td>104.8</td>
      <td>$\theta_{S-S}=93.90$</td>
      <td rowspan="2">2.92</td>
      <td rowspan="2">$-19.35$</td>
      <td rowspan="2">3.17/4.29</td>
    </tr>
    <tr>
      <td>$b = 4.56$</td>
      <td>$d_{Ge-Se}=2.59$</td>
      <td>$d_{Se-Ge}=2.56$</td>
      <td>99.92</td>
      <td>$\theta_{Se-Se}=97.30$</td>
    </tr>
  </tbody>
</table>

**Table 1.** The lattice parameters ($a$ and $b$) in Å, bond lengths between atoms ($d_{Ge-S(Se)}$, $d_{S(Se)-Ge}$) in Å, bond angles ($\theta_{Ge-Ge}$, $\theta_{S(Se)-S(Se)}$) in degrees, interlayer distance ($d_{spacing}$) in Å, binding energy ($E_b$) in meV/Å², and lattice mismatch ($\Delta$ in % along a/b direction) are calculated using the PBE functional for GeS and GeSe monolayers, as well as for GeS/GeSe XX and GeS/GeSe XY vdW heterostructures.

![](./images/1061484690508087319_2.jpg)

Fig. 2. Variations of binding energy (meV/Å²) and bandgap (eV) calculated for (a) XX heterostructure and (b) XY heterostructure as function of the $d_{spacing}$ (Å).

![](./images/1061484690508087319_3.jpg)

Fig. 3. Calculated phonon dispersion of (a) GeS/GeSe XX vdW heterostructure and (b) GeS/GeSe XY vdW heterostructure along the high-symmetry point within the first Brillouin zone.

phonon modes in the dispersion curves of the monolayers (Fig. S8a,b) and of the GeS/GeSe vdW heterostructures (Fig. 3) confirmed their dynamic stability. These results are in good agreement with previous theoretical studies⁷⁶. Additionally, an ab-initio molecular dynamics (AIMD) calculation was carried out for GeS/GeSe XX and XY, where its stability is confirmed, Fig. S9. These results align with the binding energy calculations, collectively affirming the higher thermodynamic and structural stability of the XY stacking over the XX configuration. The convergence of these complementary theoretical techniques provides a comprehensive understanding of the relative stability and lattice properties of these vdW heterostructures.

### Electronic properties
The electronic properties of GeS and GeSe materials were investigated across their bulk, monolayer, and van der Waals (vdW) heterostructure configurations, employing DFT calculations as the primary analytical tool. We utilized two distinct exchange-correlation functionals: the generalized gradient approximation with the Perdew–Burke–Ernzerhof (GGA-PBE) functional, and the Heyd–Scuseria–Ernzerhof (HSE06) hybrid functional. The use of the HSE06 functional was motivated by the known tendency of the GGA-PBE approximation to underestimate the bandgap values in these materials. For the bulk materials, the HSE06 functional revealed bandgaps of 1.77 eV for GeS and 1.54 eV for GeSe, whereas the GGA-PBE underestimated these values, yielding 1.21 eV for GeS and 0.87 eV for GeSe (see Table S2 and Fig. S15). This underestimation by GGA-PBE is a well-known limitation arising from the self-interaction error and the absence of exact non-local Hartree-Fock exchange⁷⁷. The HSE06 functional, which incorporates a fraction of exact Hartree-Fock exchange, provides an improved description of the electronic structure and more accurate bandgap predictions for these materials.

Specifically, the conduction band minimum (CBM) is located at $\Gamma$ point and the valence band maximum (VBM) is located along the $\Gamma$-X path (0.39 0.00 0.00), resulting in an indirect bandgap of 1.76 ( close to experimental result, 1.58⁷³) eV. Similarly, the calculations with HSE06 hybrid functional also yielded indirect

bandgaps for the monolayers, albeit with a different distribution of the critical points. As depicted in Fig. S10 c), for the GeS monolayer, the VBM is situated at Y-Γ (0.00 0.38 0.00) point, whereas the CBM lies along the Γ-X (0.40 0.00 0.00), leading to an indirect bandgap of 2.49 eV. Analogous behavior is observed for the GeSe monolayer in Fig. S10b), where at PBE level, the VBM is located at the Y-Γ (0.00 0.40 0.00) point, and the CBM at *Gamma*-X (0.39 0.00 0.00), resulting in an indirect bandgap of 1.23 (1.16⁷⁸ and experimental value of 1.14⁷³) eV. Likewise, the HSE06 level showed an indirect bandgap of 1.80 eV for GeSe monolayer at the same points as PBE, as shown in Fig. S10d). In contrast, the HSE06 functional predicted significantly larger bandgaps.

Building upon our investigations of the bulk and monolayer forms, we further explored the electronic properties of XX- and XY-stacked GeS/GeSe van der Waals (vdW) heterostructures. Figure 5a, exhibits an indirect bandgap of approximately 0.91 eV for GeSe/GeSe XX heterostructure, while XY has 1.02 eV, which is very close to 0.98 eV from a theoretical study of GeS/GeSe⁷⁹, where compared to GeS or GeSe monolayer, in Fig. 5a and b, the CVM shows a slight degeneracy, this may occur due to the absence of inversion symmetry in the layer structures, which causes a splitting in the energy bands, however, to obtain the effective mass, we use the semiparabolic CBM at Γ-X. Furthermore, GeSe/GeSe XY in Γ-X of CBM shows a steeper curve than XX, these bands have similar behavior for both PBE and HSE06. Likewise, the atomic projected of electronic band structures of XX and XY vdW heterostructures are observed in Fig. 4 at PBE level, where in both heterostructures the VBM is governed by Se atoms indicating the important role of Se for *p*-type doping. On the other hand, the conduction band shows contribution of all 3 atoms, however, the Ge atom shows greater contribution, especially at the CBM points indicating a great potential in electrical conductivity in the *n*-region.

In Fig. 5c and d, a clear difference in the bandgap by HSE06 compared to PBE is shown, this increase is due to the exact exchange portion of 25 %, which provides an improved description of the electron-electron interactions and leads to more reliable bandgap predictions. In Fig. 5c, the GeSe/GeSe XX heterostructure exhibits an indirect bandgap of approximately 1.42 eV. Similarly, Fig. 5d shows the band structure of the GeSe/GeSe XY vdW heterostructure calculated with the HSE06 functional showing an indirect band gap of 1.34 eV, and VBM and CBM occur at the Γ-X and Y-Γ points in the Brillouin zone for both heterostructures, the values reported in this study are very close to a recent study⁷⁹. The creation of the heterostructures efficiently reduced the bandgap at PBE and HSE06 level compared to their monolayer forms (Table 2).

## Thermoelectric properties
The accurate prediction of thermoelectric properties, such as the Seebeck coefficient, electrical conductivity, and electronic thermal conductivity, is crucial for evaluating the potential of materials for various applications⁸⁰. In the previous section, we calculated the electronic band structures of the GeSe-GeS-based van der Waals heterostructures using two different exchange-correlation functionals, PBE and HSE06. However, in this section, we solely utilize the computationally efficient Perdew-Burke-Ernzerhof (PBE) functional within DFT to generate the band structures as input for the calculation of thermoelectric properties employing the BoltzTraP2 code⁶⁶, the reason is because PBE offered bandgap results closer to the experimental ones, both for GeS and GeSe monolayer⁷³, and while HSE06 offers more accurate results in majority of materials, it turns out to be highly computationally demanding, while BoltzTraP2 requires a dense mesh of points-**k**. Furthermore, the choice of the PBE functional is a well-established practice in the field of thermoelectric materials research, as it has been demonstrated to provide reliable qualitative trends and relative comparisons of thermoelectric performance among different material systems, despite its inherent limitations in accurately predicting bandgaps. Importantly, the use of the PBE functional in this study aligns with the established practices in the field of thermoelectric materials research, facilitating direct comparisons with previously reported results and enabling a consistent framework for evaluating the thermoelectric performance of the investigated vdW heterostructures relative to other material systems.

![](./images/1061484690508087319_4.jpg)

Fig. 4. Atomic projected band structure for the van der Waals heterostructures: (a) GeS/GeSe XX, and (b) GeS/GeSe XY using the PBE functional.

![](./images/1061484690508087319_5.jpg)

Fig. 5. Band structure and bandgap indications for the van der Waals heterostructures: (a) GeS/GeSe XX, and (b) GeS/GeSe XY using the PBE functional; and (c) GeS/GeSe XX, and (d) GeS/GeSe XY using the HSE06 functional along high-symmetry $\mathbf{k}$-points.

<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>$E_g^{PBE}$ (eV)</th>
      <th>$E_g^{HSE06}$ (eV)</th>
      <th>Bandgap (PBE)</th>
      <th>Bandgap (HSE06)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GeS ML</td>
      <td>$1.76$ ($1.69^{68}$, $1.66^{72}$)</td>
      <td>$2.49$</td>
      <td>Indirect</td>
      <td>Indirect</td>
    </tr>
    <tr>
      <td>GeSe ML</td>
      <td>$1.23$ ($1.14^{68}$, $1.10^{72}$)</td>
      <td>$1.80$</td>
      <td>Indirect</td>
      <td>Indirect</td>
    </tr>
    <tr>
      <td>GeS/GeSe XX</td>
      <td>$0.91$</td>
      <td>$1.42$</td>
      <td>Indirect</td>
      <td>Indirect</td>
    </tr>
    <tr>
      <td>GeS/GeSe XY</td>
      <td>$1.02$</td>
      <td>$1.34$</td>
      <td>Indirect</td>
      <td>Indirect</td>
    </tr>
  </tbody>
</table>

Table 2. Bandgap values and types calculated for GeS ML, GeSe ML, GeS/GeSe XX, and GeS/GeSe XY using PBE and HSE06 functionals.

![](./images/1061484690508087319_6.jpg)

Fig. 6. The thermoelectric properties of GeS monolayer: (a) Seebeck coefficient ($S$), (b) electrical conductivity ($\sigma$), (c) electronic thermal conductivity ($\kappa_e$), and (d) the figure of merit ($ZT$) as a function of chemical potential in the temperature range from 300 to 800 K.

In Figs. 6 and 7 the thermoelectric properties of GeS and GeSe monolayers are illustrated, where in a) the Seebeck coefficient ($S$) shows a decrease due to its sensitivity to temperature, and is inversely proportional to the temperature gradient$^{81}$, $p$-type materials display a positive Seebeck coefficient since the predominance of holes governs the conduction of the material. Conversely, $n$-type materials, characterized by an excess of electrons, exhibit a negative Seebeck coefficient, contributing significantly to the conduction of the materials, similarly, the electrical conductivity ($\sigma$) is related to temperature, as seen in Eq. 3, furthermore, in Fig. S11a,b it can be seen that above the Fermi level, in CBM it is dominated by both Ge and Se, this is reflected in the electrical conductivity for $n$-type GeS and GeSe ML, where in Figs. 6b and 7b a more pronounced peak is observed in the $n$-region. Likewise, in Figs. 6c and 7c it was noted that there is a predominance in values of the chemical potential greater than 0 for the electronic thermal conductivity ($\kappa_e$), where this does not present drastic changes due to temperature.

Based on DP (deformation potential), relaxation time were calculated for both, monolayers and heterostructures using Eq. 6, applying uniaxial external strain in the range of $-1$-$1\%$ (Figs. S13 and S14). Negative values indicate tensile strain, while positive values indicate compression. The relaxation time ($\tau$) was calculated using the equation:

$$
\tau = \frac{\mu_{2D}m^{*}}{e}, \tag{6}
$$

![](./images/1061484690508087319_7.jpg)

Fig. 7. The thermoelectric properties of GeSe monolayer: (a) Seebeck coefficient (S), (b) electrical conductivity ($\sigma$), (c) electronic thermal conductivity ($\kappa_{e}$), and (d) the figure of merit (ZT) as a function of chemical potential in the temperature range from 300 to 800 K.

<table><thead><tr><th rowspan="2">Material</th><th colspan="4">Electron</th><th colspan="5">Hole</th></tr><tr><th>$m_{x}^{*}/m_{0}$</th><th>$m_{y}^{*}/m_{0}$</th><th>$\mu_{2D,x}$</th><th>$\mu_{2D,y}$</th><th>$m_{x}^{*}/m_{0}$</th><th>$m_{y}^{*}/m_{0}$</th><th>$\mu_{2D,x}$</th><th>$\mu_{2D,y}$</th><th>$\tau$ (s)</th></tr></thead><tbody><tr><td>GeS ML</td><td>0.48</td><td>0.33</td><td>193.55</td><td>155.56</td><td>0.30</td><td>0.20</td><td>510.33</td><td>140.15</td><td>$2010^{-14}$</td></tr><tr><td>GeSe ML</td><td>0.51</td><td>0.34</td><td>185.90</td><td>157.85</td><td>0.22</td><td>0.15</td><td>185.96</td><td>42.85</td><td>$7310^{-14}$</td></tr><tr><td>GeS/GeSe XX</td><td>0.54</td><td>0.36</td><td>1154.01</td><td>69.75</td><td>0.17</td><td>0.12</td><td>395.07</td><td>95.37</td><td>$8810^{-13}$</td></tr><tr><td>GeS/GeSe XY</td><td>0.44</td><td>0.30</td><td>2001.00</td><td>148.50</td><td>0.19</td><td>0.13</td><td>312.43</td><td>123.62</td><td>$4610^{-13}$</td></tr></tbody></table>

Table 3. Effective mass of electrons and holes along $x$ direction ($m_{x}^{*}/m_{0}$) and $y$ direction ($m_{y}^{*}/m_{0}$), carrier mobility ($\mu_{2D}$), and relaxation time ($\tau$) at 300 K.

where $\mu_{2D}$ is the carrier mobility of two-dimensional materials, $m^{*}$ is the effective mass, and $e$ is the charge of an electron. The effective mass and the carrier mobility can be calculated with the following equations:

$$
\mu_{2 D}=\frac{e \hbar^{3} C_{2 D}}{k_{B} T m^{*} \overline{m} E_{d}^{2}},\tag{7a}
$$

$$
m^{*}=\hbar^{2}\left(\frac{d^{2} E}{d \mathbf{k}^{2}}\right)^{-1},\tag{7b}
$$

where $\mathbf{k}$ denotes the wave vector, $E$ represents the energy associated with the wave vector $\mathbf{k}$, $\hbar$ is the reduced Planck constant, $C_{2 D}$ is the elastic modulus, $E_{d}$ is the deformation potential, and $\overline{m}$ ($\sqrt{m_{x} m_{y}}$) is the average effective mass. The values of effective mass and relaxation time for monolayers and vdW heterostructures are detailed in Table 3. Where, the results obtained by applying this theory to determine $C_{2 D}$ and $E_{d}$ are represented in Figs. S13 and S14 for a vacuum level ($E_{vacuum}$) of 3.09, 3.36, 5.64, and 5.62 eV for GeS ML, GeSe ML, GeS/ GeSe XX, and GeS/GeSe XY, respectively, as shown in Fig. S12.

On the other hand, the lattice thermal conductivity is associated with the phononic modes $\lambda$, which is obtained using the linearized Boltzmann transport equation (LBTE), and is given in terms of the Cartesian components $\alpha\beta$ por

$$
\begin{aligned}
\kappa^{\alpha \beta}= & \sum_{\lambda} \frac{1}{k_{\mathrm{B}} T^{2} V} \\
& \times\left\langle f_{0}\left(\omega_{\mathbf{q}, \lambda} ; T\right)\left[1+f_{0}\left(\omega_{\mathbf{q}, \lambda} ; T\right)\right]\left(\hbar \omega_{\mathbf{q}, \lambda}\right)^{2} v_{\mathbf{q}, \lambda}^{\alpha} F_{\mathbf{q}, \lambda}^{\beta}\right\rangle_{\mathbf{q}}.
\end{aligned}\tag{8}
$$

Where $\mathbf{q}$ is the vector in reciprocal space. The equilibrium distribution function $f_{0}(\omega_{\mathbf{q},\lambda}; T)$ is evaluated for angular frequency $\omega_{\mathbf{q},\lambda}$ and temperature $T$. The vector $F_{\mathbf{q},\lambda}$, which is obtained by solving the LBTE, is directly linked to the phonon lifetime $^{e?}$. The term $\langle\cdots\rangle_{\mathbf{q}}$ indicates that an average is performed over the first Brillouin zone. Where in Fig. S18a the $\kappa_{l}$ calculated for GeS and GeSe ML are depicted and we can notice that in the case of GeSe, the $\kappa_{l}$ is lower than the experimental value 1.57 W/mK at $300\ \text{K}^{82}$.

These parameters combined, through the Eq. 1 lead to the figure of merit (ZT), where for GeS ML (GeSe ML) exhibit a high thermoelectric efficiency at 800 K of 1.83 (1.73), as illustrated in Figs. 6 and 7d, where the GeS monolayer presents a higher peak in the $p$ region, meanwhile, GeSe monolayer shows a $n$-type behavior, because the maximum peak is located at positive values of the chemical potential.

In contrast to the monolayers, the thermoelectric properties of XX and XY vdW heterostructures are shown in Figs. 8 and 9. For instance, the calculated values of the Seebeck coefficient for the XX vdW heterostructure are depicted in Fig. 8a. At 300 K, a high Seebeck coefficient of 1.58 mV/K is observed, due to the inverse proportionality with the temperature gradient, at 800 K the Seebeck coefficient presents the minimum value,

![](./images/1061484690508087319_8.jpg)

Fig. 8. (a) Seebeck coefficient, (b) electrical conductivity, (c) electronic thermal conductivity, and (d) figure of merit of GeS/GeSe XX vdW heterostructure as a function of chemical potential in the temperature range from 300 to 800 K.

![](./images/1061484690508087319_9.jpg)

Fig. 9. (a) Seebeck coefficient, (b) electrical conductivity, (c) electronic thermal conductivity, and (d) figure of merit of GeS/GeSe XY vdW heterostructure as a function of chemical potential in the temperature range from 300 to 800 K.

this could indicate a low thermoelectric efficiency at high temperatures. Similarly, the XY vdW heterostructure, in Fig. 9a, exhibits a high Seebeck coefficient of 1.55 W/mK at 300 K.

In Fig. 8b, the electrical conductivity of the XX vdW heterostructure is shown as a function of the chemical potential. The maximum calculated value for $n$-type charge carriers was $426.82 \times 10^{5}$ 1/Ωm with a chemical potential value of 2.13 eV at 300 K. At a maximum temperature of 800 K, the electrical conductivity shows a decrease to $167.13 \times 10^{5}$ 1/Ωm for $n$-type, which is due to the predominance of intrinsic phonon scattering mechanisms at high temperatures, also considering the rough shape of the heterostructure and the contribution of many bands of Ge and Se atoms a to de conduction band. Likewise, the GeS/GeSe XY vdW heterostructure presented similar properties, as shown in Fig. 9b, with values of $542.68 \times 10^{5}$ 1/Ωm for $n$-type charge carriers at a chemical potential of 2.02 eV at 300 K. The electrical conductivity shows a temperature-dependent behavior, reaching a value of $197.65 \times 10^{5}$ 1/Ωm at 800 K, this trend is closely linked to the underlying dynamics of charge carrier scattering and phonon interactions at elevated temperatures. Under these conditions, phonon-phonon interactions and electron-phonon scattering become more pronounced causing the probability of electron scattering with phonons to increase significantly limiting the mobility of charge carriers since electrons or holes are more frequently deflected by lattice vibrations, reducing their ability to move freely through the material. Furthermore, the relaxation time ($\tau$) representing the average time between scattering events plays a crucial role in this behavior. As the temperature is increased, the enhanced scattering leads to a reduction in the relaxation time, as illustrated in Fig. 10b.

The electronic thermal conductivity shows a similar behavior to the electrical conductivity since both are linearly related, we find that at room temperature, the GeS/GeSe XX vdW heterostructure demonstrates a maximum electronic thermal conductivity for $n$-type carriers of 310.21 W/mK, as depicted in Fig. 8c at room temperature, meanwhile, a minimum value of $\kappa_{e}$ of 290.11 W/mK was found at 800 K. Similar but slightly lower values were reported for $n$-type carriers in the case of the GeS/GeSe XY vdW heterostructure, which is 589.07 W/mK at room temperatures, as shown in Fig. 9c, we report 197.65 W/mK at 800 K, unlike $\sigma$, a large of variation in electronic thermal conductivity at high temperatures, this can be attributed to a combination of saturation effects, the dominance of electronic contributions, and intrinsic characteristics of GeS and GeSe that make the thermal response stable in that temperature range. Another important factor that contributes to thermal conductivity is the lattice thermal conductivity ($\kappa_{l}$), which plays a very important role in boosting thermoelectric efficiency, since unlike S, $\sigma$, and $\kappa_{e}$, the $\kappa_{l}$ does not depend on the carrier concentration, in this study, a lattice thermal conductivity of 15.21 W/mK was calculated for GeS/GeSe XX at room temperature, as depicted in Table 4, meanwhile, a higher value of 17.95 W/mK was computed for GeS/GeSe XY at room temperature, Fig. 10a. On the other hand, at high temperatures, the lattice thermal conductivity decreases to 5.61 (6.60) W/mK for the GeS/GeSe XX (GeS/GeSe XY) heterostructures, which could primarily due to Phonon-Phonon Umklapp scattering, grain boundaries and dislocation scattering. Compared with the electronic thermal

![](./images/1061484690508087319_10.jpg)

Fig. 10. (a) Lattice thermal conductivity and (b) relaxation time of GeS/GeSe XX and XY vdW heterostructures in the temperature range from 300 to 800 K.

<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>S (mV/K)</th>
      <th>$\sigma$ ($10^{5}1/\Omega$ m)</th>
      <th>$\kappa_{e}$ (W/mK)</th>
      <th>$\kappa_{l}$ (W/mK)</th>
      <th>ZT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GeS ML</td>
      <td>1.58</td>
      <td>73.03</td>
      <td>52.39</td>
      <td>1.16</td>
      <td>0.64</td>
    </tr>
    <tr>
      <td>GeSe ML</td>
      <td>1.55</td>
      <td>28.23</td>
      <td>20.27</td>
      <td>0.32</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>GeS/GeSe XX</td>
      <td>1.51</td>
      <td>426.82</td>
      <td>310.21</td>
      <td>15.21</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>GeS/GeSe XY</td>
      <td>1.39</td>
      <td>542.68</td>
      <td>589.07</td>
      <td>17.95</td>
      <td>0.16</td>
    </tr>
  </tbody>
</table>

Table 4. Seebeck coefficient (S), electrical conductivity ($\sigma$), electronic thermal conductivity ($\kappa_{e}$), lattice thermal conductivity ($\kappa_{l}$), and figure of merit (ZT) were calculated using the PBE functional for GeS and GeSe monolayers, as well as for GeS/GeSe XX and GeS/GeSe XY van der Waals heterostructures, all values are presented at 300 K.

conductivity, there is no significant contribution from the lattice thermal conductivity to the total thermal conductivity which is $\kappa_{Tot} = \kappa_{l} + \kappa_{e}$.

A high value of the Seebeck coefficient, electronic electrical and thermal conductivity but low lattice thermal conductivity led to a maximum thermoelectric efficiency at 300 K (800 K) of 0.13 (0.84) for the GeS/GeSe XX vdW heterostructure in the $n$-region. Conversely, the GeS/GeSe XY vdW heterostructure exhibits a higher peak in the $p$-region, demonstrating that the stacking arrangement of GeS and GeSe monolayers can shift the material from $p$-type to $n$-type with a $ZT = 0.83$ at 800 K, as shown in Fig. 8d. The ability to alter charge carriers is crucial for thermoelectric devices, as both $p$-type and $n$-type materials are necessary for efficient performance. This transition from $p$-type to $n$-type occurs due to changes in the distribution of electrons and holes within the heterostructure when the geometry is modified. The high ZT values, especially in the XY configuration, suggest that GeS/GeSe heterostructures are promising candidates for high-temperature thermoelectric applications, such as waste heat recovery, where materials with high thermal resistance and electrical efficiency are required. The ability of these heterostructures to maintain excellent performance across a wide temperature range (300–800 K) makes them suitable for use in power generation and cooling devices in industrial processes or in thermoelectric generators for automotive and aerospace applications.

### Conclusions
We have performed an extensive study on the structural, electronic, and thermoelectric properties of GeS and GeSe materials in various forms, including bulk, 2D monochalcogenide monolayers, and GeS/GeSe (XX and XY) vdW heterostructures. This investigation utilized a combination of first-principles calculations and BTE approach to provide a comprehensive understanding of these materials. Through material engineering, we created two heterostructures by vertically stacking monochalcogenides. Among these, the XY heterostructure demonstrated greater stability than the XX vdW heterostructure and exhibited lower lattice thermal conductivity. The formation of heterostructures resulted in a significant reduction in the bandgap of the monolayers. Specifically, the GeS/GeSe XX and GeS/GeSe XY vdW heterostructures showed remarkable stability, with bandgaps of 0.91 eV and 1.02 eV, respectively at PBE level. The analysis of the thermoelectric properties revealed high Seebeck coefficients and electrical conductivities for these heterostructures, which contributed to their excellent thermoelectric performance. The GeS/GeSe XX vdW heterostructure achieved a high thermoelectric figure of merit (ZT) of 0.84 at 800 K, while the GeS/GeSe XY vdW heterostructure exhibited an even higher ZT value of 0.83 at the same temperature. This indicates that the most stable heterostructure also exhibited the highest thermoelectric figure of merit, highlighting the potential of these materials for thermoelectric applications. The

creation and analysis of GeS/GeSe vdW heterostructures have shown that these materials possess favorable electronic and thermoelectric properties. The stability, reduced bandgap, high Seebeck coefficient, and high electrical conductivity of these heterostructures underscore their promise for future thermoelectric applications.

## Data availability
All data relevant to this study are presented in the manuscript, and its supplementary information files. Any remaining questions or requests for additional details regarding the datasets should be directed to the corre- sponding author.

Received: 29 August 2024; Accepted: 29 October 2024
Published online: 05 November 2024

## References
1. Nematollahi, O., Hoghooghi, H., Rasti, M. & Sedaghat, A. Energy demands and renewable energy resources in the middle east. Renew. Sustain. Energy Rev. 54, 1172-1181 (2016).
2. Tyralis, H., Mamassis, N. & Photis, Y. N. Spatial analysis of the electrical energy demand in Greece. Energy Policy 102, 340-352(2017).
3. Kaberger, T. Progress of renewable electricity replacing fossil fuels. Glob. Energy Interconnect. 1, 48-52 (2018).
4. Lindroos, T. J. et al. Replacing fossil fuels with bioenergy in district heating-comparison of technology options. Energy 231, 120799(2021).
5. Abas, N., Kalair, A. & Khan, N. Review of fossil fuels and future energy technologies. Futures 69, 31-49 (2015).
6. Coram, A. & Katzner, D. W. Reducing fossil-fuel emissions: Dynamic paths for alternative energy-producing technologies. Energy Econ. 70, 179-189 (2018).
7. Gomes, C. L. & Carvalho, A. Electronic and optical properties of low-dimensional group-IV monochalcogenides. J. Appl. Phys.128, 121101 (2020).
8. Zhao, P. et al. Design of new photovoltaic systems based on two-dimensional group-IV monochalcogenides for high performance solar cells. J. Mater. Chem. A 5, 24145-24152 (2017).
9. Singh, A. K. & Hennig, R. G. Computational prediction of two-dimensional group-IV mono-chalcogenides. Appl. Phys. Lett. 105042103 (2014).
10. Sarkar, A. S. & Stratakis, E. Recent advances in 2D metal monochalcogenides. Adv. Sci. 7, 2001655 (2020).
11. Zhang, J. et al. Novel Ge-Sb-Te thermoelectric materials: A demonstration for an efficient diffusion couple technique in expediently exploiting new thermoelectric materials. Ceram. Int. 45, 16039-16045 (2019).
12. Han, Z. et al. Room-temperature thermoelectric materials: Challenges and a new paradigm. Journal of Materiomics (2021).
13. Pourkiaei, S. M. et al. Thermoelectric cooler and thermoelectric generator devices: A review of present and potential applications, modeling and materials. Energy 186, 115849 (2019).
14. Freer, R. & Powell, A. V. Realising the potential of thermoelectric technology: A roadmap. J. Mater. Chem. C 8, 441-463 (2020).
15. Patel, A., Singh, D., Sonvane, Y., Thakor, P. & Ahuja, R. High thermoelectric performance in two-dimensional Janus monolayer material WS-X (X= Se and Te). ACS Appl. Mater. Interfaces 12, 46212-46219 (2020).
16. Gao, Z., Liu, G. & Ren, J. High thermoelectric performance in two-dimensional tellurium: An ab initio study. ACS Appl. Mater. Interfaces 10, 40702-40709 (2018).
17. Zhou, Y. & Zhao, L.-D. Promising thermoelectric bulk materials with 2D structures. Adv. Mater. 29, 1702676. https://doi.org/10.1002/adma.201702676 (2017)
18. Ge, Z.-H. et al. Low-cost, abundant binary sulfides as promising thermoelectric materials. Mater. Today 19, 227-239 (2016).
19. Hsu, K. F. et al. Cubic $AgPb_m$ SbTe $_{2+m}$: Bulk thermoelectric materials with high figure of merit. Science 303, 818-821 (2004).
20. Mishra, P, Singh, D., Sonvane, Y. & Ahuja, R. Two-dimensional boron monochalcogenide monolayer for thermoelectric material. Sustain. Energy Fuels 4, 2363-2369 (2020).
21. Jiang, B. et al. High figure-of-merit and power generation in high-entropy GeTe-based thermoelectrics. Science 377, 208-213(2022).
22. Haq, B. U. et al. Thermoelectric properties of the novel cubic structured silicon monochalcogenides: A first-principles study. J. Alloy Compd. 769, 413-419 (2018).
23. Tang, H. et al. Graphene network in copper sulfide leading to enhanced thermoelectric properties and thermal stability. Nano Energy 49, 267-273 (2018).
24. Snyder, G. J. & Snyder, A. H. Figure of merit ZT of a thermoelectric device defined from materials properties. Energy Environ. Sci.10, 2280-2283 (2017).
25. Gelbstein, Y. et al. Highly efficient Ge-rich $Ge_x$ $Pb_{1-x}$ Te thermoelectric alloys. J. Electron. Mater. 39, 2049-2052 (2010).
26. Huang, L., Zheng, Y., Xing, L. & Hou, B. Recent progress of thermoelectric applications for cooling/heating, power generation, heat flux sensor and potential prospect of their integrated applications. Therm. Sci. Eng. Prog. 45, 102064 (2023).
27. Jaziri, N. et al. A comprehensive review of thermoelectric generators: Technologies and common applications. Energy Rep. 6,264-287(2020).
28. Tolloczko, A. K. et al. Photoemission study of the thermoelectric group IV-VI van der Waals Crystals (GeS, SnS, and SnSe). Adv. Opt. Mater. 12, 2302049. https://doi.org/10.1002/adom.202302049 (2024).
29. Ramasamy, P., Kwak, D., Lim, D.-H., Ra, H.-S. & Lee, J.-S. Solution synthesis of GeS and GeSe nanosheets for high-sensitivity photodetectors. J. Mater. Chem. C4, 479-485. https://doi.org/10.1039/C5TC03667D (2016).
30. Gao, R. et al. Adsorption and gas-sensing performance of $SF_6$ decomposition gases on GeS monolayers with and without single vacancies and Si-doping. Appl. Surf. Sci. 568, 150961. https://doi.org/10.1016/j.apsusc.2021.150961 (2021).
31. Ding, G., Gao, G. & Yao, K. High-efficient thermoelectric materials: The case of orthorhombic IV-VI compounds. Sci. Rep. 5, 9567. https://doi.org/10.1038/srep09567 (2015).
32. Zhang, M., Flitcroft, J. M., Guillemot, S. K. & Skelton, J. M. Thermoelectric properties of Pnma and R3m GeS and GeSe. J. Mater. Chem. C 11, 14833-14847. https://doi.org/10.1039/D3TC02938G (2023).
33. Rakshit, M. et al. A study of anisotropic thermoelectric properties of bulk Germanium Sulfide in its Pnma phase: A combined first-principles and machine-learning approach. Phys. Scr. 97, 125804. https://doi.org/10.1088/1402-4896/ac9be4 (2022).
34. Fan, Q., Zhang, W., Qing, H. & Yang, J. Exceptional thermoelectric properties of bilayer GeSe: First principles calculation. Materials15, 971. https://doi.org/10.3390/ma15030971 (2022).
35. Hao, S., Shi, F., Dravid, V. P., Kanatzidis, M. G. & Wolverton, C. Computational prediction of high thermoelectric performance in hole doped layered GeSe. Chem. Mater. 28, 3218-3226 (2016).
36. Zhao, L.-D. et al. Raising the thermoelectric performance of p-type PbS with endotaxial nanostructuring and valence-band offset engineering using CdS and ZnS. J. Am. Chem. Soc. 134, 16327-16336 (2012).
37. Lee, Y. et al. Contrasting role of antimony and bismuth dopants on the thermoelectric performance of lead selenide. Nat. Commun.5, 3640 (2014).

38. Shafique, A. & Shin, Y.-H. Thermoelectric and phonon transport properties of two-dimensional IV–VI compounds. *Sci. Rep.* **7**, 506 (2017).
39. Sarkar, D. et al. Metavalent bonding in GeSe leads to high thermoelectric performance. *Angew. Chem. Int. Ed.* **60**, 10350–10358 (2021).
40. Shu, Z. et al. High-performance thermoelectric monolayer $\gamma$-GeSe and its group-IV monochalcogenide isostructural family. *Chem. Eng. J.* **454**, 140242 (2023).
41. Shu, Z. *et al.* High-performance thermoelectric $\gamma$-GeSe and its group-IV monochalcogenide isostructural family. Available at SSRN 4156468 .
42. Guo, S.-D. & Wang, Y.-H. Thermoelectric properties of orthorhombic group IV–VI monolayers from the first-principles calculations. *J. Appl. Phys.* **121**, 034302 (2017).
43. U IHaq, B., AlFaify, S. & Laref, A. Exploring novel flat-band polymorphs of single-layered germanium sulfide for high-efficiency thermoelectric applications. *J. Phys. Chem. C* **123**, 18124–18131 (2019).
44. Morales-Ferreiro, J., Diaz-Droguett, D. E., Celentano, D. & Luo, T. First-principles calculations of thermoelectric properties of IV–VI chalcogenides 2D materials. *Front. Mech. Eng.* **3**, 15 (2017).
45. Wang, C., Chen, Y.-X., Gao, G., Xu, K. & Shao, H. Theoretical investigations of Janus WSeTe monolayer and related van der Waals heterostructures with promising thermoelectric properties. *Appl. Surf. Sci.* **593**, 153402 (2022).
46. Rahim, A. et al. Electronic and thermoelectric properties of group IV–VI van der Waals heterostructures. *J. Comput. Electron.* **21**, 725–732 (2022).
47. Hu, W. & Yang, J. First-principles study of two-dimensional van der Waals heterojunctions. *Comput. Mater. Sci.* **112**, 518–526 (2016).
48. Cheng, K. et al. Lateral heterostructures of monolayer group-IV monochalcogenides: Band alignment and electronic properties. *J. Mater. Chem. C* **5**, 3788–3795. https://doi.org/10.1039/C7TC00595D (2017).
49. Yu, W. et al. Tunable electronic properties of GeSe/phosphorene heterostructure from first-principles study. *Appl. Phys. Lett.* https://doi.org/10.1063/1.4962434 (2016).
50. Ju, L., Dai, Y., Wei, W., Li, M. & Huang, B. DFT investigation on two-dimensional GeS/WS₂ van der Waals heterostructure for direct Z-scheme photocatalytic overall water splitting. *Appl. Surf. Sci.* **434**, 365–374. https://doi.org/10.1016/j.apsusc.2017.10.172 (2018).
51. Vaziri, S. et al. Ultrahigh thermal isolation across heterogeneously layered two-dimensional materials. *Sci. Adv.* **5**, eaax1325. https://doi.org/10.1126/sciadv.aax1325 (2019).
52. Zhang, R., Zhou, Z., Yao, Q., Qi, N. & Chen, Z. Significant improvement in thermoelectric performance of SnSe/SnS via nano-heterostructures. *Phys. Chem. Chem. Phys.* **23**, 3794–3801. https://doi.org/10.1039/D0CP05548D (2021).
53. Giannozzi, P. et al. QUANTUM ESPRESSO: A modular and open-source software project for quantum simulations of materials. *J. Phys.: Condens. Matter* **21**, 395502 (2009).
54. Hafner, J. Ab-initio simulations of materials using VASP: Density-functional theory and beyond. *J. Comput. Chem.* **29**, 2044–2078. https://doi.org/10.1002/jcc.21057 (2008).
55. Togo, A., Chaput, L., Tadano, T. & Tanaka, I. Implementation strategies in phonopy and phono3py. *J. Phys.: Condens. Matter* **35**, 353001. https://doi.org/10.1088/1361-648X/acd831 (2023).
56. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* **77**, 3865 (1996).
57. Heyd, J., Scuseria, G. E. & Ernzerhof, M. Hybrid functionals based on a screened coulomb potential. *J. Chem. Phys.* **118**, 8207–8215 (2003).
58. Krukau, A. V., Vydrov, O. A., Izmaylov, A. F. & Scuseria, G. E. Influence of the exchange screening parameter on the performance of screened hybrid functionals. *J. Chem. Phys.* **125**, 224106 (2006).
59. Grimme, S., Antony, J., Ehrlich, S. & Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. *J. Chem. Phys.* **132**, 154104 (2010).
60. Monkhorst, H. J. & Pack, J. D. Special points for brillouin-zone integrations. *Phys. Rev. B* **13**, 5188 (1976).
61. Togo, A. & Tanaka, I. First principles phonon calculations in materials science. *Scripta Mater.* **108**, 1–5 (2015).
62. Born, M. & Huang, K. *Dynamical Theory of Crystal Lattices* (Oxford University Press, 1996).
63. Eriksson, F., Fransson, E. & Erhart, P. The hiphive package for the extraction of high-order force constants by machine learning. *Adv. Theory Simulat.* **2**, 1800184 (2019).
64. Togo, A., Chaput, L., Tadano, T. & Tanaka, I. Implementation strategies in Phonopy and Phono3py. *J. Phys.: Condens. Matter* **35**(35), 353001 (2023).
65. Chaput, L. Direct solution to the linearized phonon Boltzmann equation. *Phys. Rev. Lett.* **110**, 265506 (2013).
66. Madsen, G. K. H., Carrete, J. & Verstraete, M. J. BoltzTraP2, a program for interpolating band structures and calculating semi-classical transport coefficients. *Comput. Phys. Commun.* **231**, 140–145. https://doi.org/10.1016/j.cpc.2018.05.010 (2018).
67. Chester, G. & Thellung, A. The law of Wiedemann and Franz. *Proc. Phys. Soc.* **77**, 1005 (1961).
68. Gomes, L. C. & Carvalho, A. Phosphorene analogues: Isoelectronic two-dimensional group-IV monochalcogenides with orthorhombic structure. *Phys. Rev. B* **92**, 085406 (2015).
69. Antunez, P. D., Buckley, J. J. & Brutchey, R. L. Tin and germanium monochalcogenide IV–VI semiconductor nanocrystals for use in solar cells. *Nanoscale* **3**, 2399–2411 (2011).
70. Poudel, S. P. & Barraza-Lopez, S. Metastable piezoelectric group-IV monochalcogenide monolayers with a buckled honeycomb structure. *Phys. Rev. B* **103**, 024107 (2021).
71. Hu, T. & Dong, J. Two new phases of monolayer group-IV monochalcogenides and their piezoelectric properties. *Phys. Chem. Chem. Phys.* **18**, 32514–32520 (2016).
72. Fei, R., Li, W., Li, J. & Yang, L. Giant piezoelectricity of monolayer group IV monochalcogenides: SnSe, SnS, GeSe, and GeS. *Appl. Phys. Lett.* **107**, 173104 (2015).
73. Vaughn, D. D., Patel, R. J., Hickner, M. A. & Schaak, R. E. Single-crystal colloidal nanosheets of GeS and GeSe. *J. Am. Chem. Soc.* **132**, 15170–15172. https://doi.org/10.1021/ja107520b (2010).
74. Aerts, M. et al. Highly efficient carrier multiplication in pbs nanosheets. *Nat. Commun.* **5**, 3789 (2014).
75. Schornbaum, J. et al. Epitaxial growth of PbSe quantum dots on MoS₂ nanosheets and their near-infrared photoresponse. *Adv. Func. Mater.* **24**, 5798–5806 (2014).
76. Qin, G. et al. Diverse anisotropy of phonon transport in two-dimensional group IV–VI compounds: A comparative study. *Nanoscale* **8**, 11306–11319 (2016).
77. Bao, J. L., Gagliardi, L. & Truhlar, D. G. Self-interaction error in density functional theory: An appraisal. *J. Phys. Chem. Lett.* **9**, 2353–2358 (2018).
78. Xu, Y. et al. First-principles study on the electronic, optical, and transport properties of monolayer $\alpha$-and $\beta$-GeSe. *Phys. Rev. B* **96**, 245421. https://doi.org/10.1103/PhysRevB.96.245421 (2017).
79. Shang, J. et al. Electronic and optical properties of the ges/gese heterostructure tuned by in-plane strain. *Can. J. Phys.* [SPACE]https://doi.org/10.1139/cjp-2023-0345 (2024).
80. Cai, B., Hu, H., Zhuang, H.-L. & Li, J.-F. Promising materials for thermoelectric applications. *J. Alloy. Compd.* **806**, 471–486 (2019).
81. Fukui, T. *et al.* Evaluation methods for properties of nanostructured body. in *Nanoparticle Technology Handbook* 317–383, https://doi.org/10.1016/B978-044453122-3.50009-X (Elsevier, 2008).

82. Shaabani, L., Aminorroaya-Yamini, S., Byrnes, J., Akbar Nezhad, A. & Blake, G. R. Thermoelectric performance of Na-doped GeSe. ACS Omega 2, 9192-9198. https://doi.org/10.1021/acsomega.7b01364 (2017).

## Acknowledgements
We express our sincere gratitude to the Universidad Nacional Jorge Basadre Grohmann for its support through the project: "Development of new thermoelectric materials for energy conversion: A theoretical and experi- mental approach", approved by rectoral resolution $N^{O}$ 11174-2023-UNJBG, and with the support PROCIEN CIA-CONCYTEC, Peru, in the framework of the call E041-2023-01 (Process number PE501082822-2023 -PRO- CIENCIA).

## Author contributions
F.M.G. and E.M.F. conceived the computational study and performed the DFT calculations. J.A.C.G. and J.S.A.A. analyzed the results and interpreted the data. M.J.P., E.R.D. and C.A.P.B. provided guidance and supervision. E.M.F. coordinated the research project. All authors contributed to writing and reviewing the manuscript.

## Declarations

### Competing interests
The authors declare no competing interests.

### Additional information
**Supplementary Information** The online version contains supplementary material available at https://doi.org/1 0.1038/s41598-024-78250-4.

Correspondence and requests for materials should be addressed to E.M.F.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2024