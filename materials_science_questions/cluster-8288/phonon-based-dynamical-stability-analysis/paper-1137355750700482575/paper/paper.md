# Propylenidene: A Novel Metallic Carbon Monolayer with Unconventional Ring Topology

José A. S. Laranjeira$^{a, *}$, K. A. L. Lima$^{b,c}$, Nicolas F. Martins$^{a}$, Luis A. Cabral$^{d}$, L.A. Ribeiro Junior$^{b,c}$ and Julio R. Sambrano$^{a}$

$^{a}$Modeling and Molecular Simulation Group, São Paulo State University (UNESP), School of Sciences, Bauru, 17033-360, SP, Brazil
$^{b}$Institute of Physics, University of Brasília, Brasília , 70910-900, DF, Brazil
$^{c}$Computational Materials Laboratory, LCCMat, Institute of Physics, University of Brasília, Brasília, 70910-900, DF, Brazil
$^{a}$Department of Physics and Meteorology, São Paulo State University (UNESP), School of Sciences, Bauru, 17033-360, SP, Brazil

---

## ARTICLE INFO

**Keywords:**
Two-dimensional
Propylenidene
Density functional theory
Carbon allotrope
Porous structure

## ABSTRACT

Two-dimensional (2D) carbon allotropes have drawn significant interest owing to their impressive physical and chemical characteristics. Following graphene's isolation, a wide range of 2D carbon materials has been suggested, each with distinct electronic, mechanical, and optical traits. Rational design and synthesis of new 2D carbon structures hinge on experimentally reported precursors. Here, we present a 2D carbon allotrope, propylenidene (PPD), originating from bicyclopropylidene. PPD forms a rectangular lattice with 3, 8, and 10-membered carbon rings. Density functional theory (DFT) simulations investigate its structural, electronic, mechanical, and optical properties. Our study shows PPD to be metallic. PPD exhibits absorption in the infrared and visible range, showing directional dependence in its response. Mechanically, PPD exhibits marked anisotropy; Young's modulus ($Y$) varies between 205.83 N/m and 164.46 N/m. These findings underscore the potential of this novel monolayer in applications such as energy storage, gas sensing, and optoelectronics.

---

## 1. Introduction

Two-dimensional (2D) carbon allotropes have garnered considerable attention due to their remarkable physical and chemical properties [1-6]. Since the isolation of graphene [7], a wide variety of 2D carbon-based structures have been proposed, each exhibiting distinct electronic, mechanical, and optical behaviors [8-16]. Many of these allotropes feature porous architectures and have been predicted to perform well in applications such as gas sensing [17, 18], metal-ion batteries [19, 20], and hydrogen storage [21, 22].

Metallic 2D carbon allotropes are particularly attractive for energy-related applications due to their high electrical conductivity and rich $\pi$-electron systems. These materials can act as effective $\pi$-acceptors when decorated with alkali, transition, or post-transition metals, enabling strong charge transfer from the adsorbed species to the carbon framework. This interaction induces partial positive charges on the adsorbed atoms, stabilizing them on the surface and enhancing their reactivity.

Recent studies have demonstrated that metallic and conductive carbon allotropes, when decorated with metal atoms, can serve as efficient platforms for hydrogen storage, catalysis, and battery technologies. Darvishnejad *et al.* [23] investigated the decoration of a sp$^2$-hybridized 2D carbon framework known as PBCF-graphene with several transition metals (Sc, Ti, V, Cr, Mn), revealing that Cr-decorated structures could reversibly adsorb up to 17 H$_2$ molecules, achieving a capacity of 9.10 wt% with adsorption energies in the optimal physisorption range. Similarly, Dewangan *et al.* [24] studied Li-decorated $\Psi$-graphene, a carbon allotrope containing pentagons, hexagons, and heptagons. Their results showed that a single Li atom could adsorb seven hydrogen molecules via polarization mechanisms, with an average adsorption energy of -0.31 eV/H$_2$, leading to a gravimetric capacity of 15.15 wt%.

Mahamiya et al. [25] extended this approach to PAI-graphene, composed of polymerized as-indacene units. They demonstrated that Li atoms could be stably anchored and each atom could bind up to four hydrogen molecules, resulting in a hydrogen capacity of 15.7 wt%, surpassing the DOE targets. Bi et al. [26] focused on penta-octa-graphene (POG) and showed that decoration with Li or Ti yields stable systems capable of storing up to 9.9 wt% of hydrogen, with adsorption energies between 0.14 and 0.95 eV. Cheng et al. [27] explored M-graphene decorated with Li, Ca, and Sc, and found that single metal atoms could reversibly adsorb up to six H$_2$ molecules, with favorable binding energies and high gravimetric densities. They also showed that external electric fields could modulate the adsorption behavior.

In another work, Cheng et al. [28] investigated HOT-graphene, a Dirac semimetal with hexagonal, octagonal, and tetragonal rings. The authors showed that decoration with alkali and alkaline earth metals (Li, Na, K, Ca) led to ultrahigh hydrogen uptake capacities (up to 14.59 wt%), and AIMD simulations confirmed the thermal stability of the metallized systems. Umadevi et al. [29] examined TPH-graphene nanoribbons and showed that Li and Na decoration significantly enhanced H$_2$ adsorption, yielding gravimetric capacities of 7.75 wt% and 6.90 wt%, respectively, along with stable charge transfer and polarization mechanisms.

In addition to hydrogen storage, conductive 2D carbon frameworks have proven valuable for battery applications. Martins et al. [30] employed OCD-graphene, a distorted

---
*Corresponding author
ORCID(s):

---
Laranjeira et al.: *Preprint submitted to Elsevier*
Page 1 of 10

Propylenidene

carbon lattice with octagonal rings, as an anode material for sodium-ion batteries. Their simulations showed a high theoretical capacity (1339 mAh/g), low diffusion barrier (0.12 eV), and thermal stability confirmed by AIMD. Cai et al. [31] studied Net-C18, a graphene-like metallic carbon sheet containing 5-, 6-, and 8-membered rings, and demon- strated that it could serve as a high-performance anode for lithium-ion batteries with a specific capacity of 403 mAh/g. Finally, Lima et al. [32] introduced Petal-Graphyne, a metal- lic allotrope composed of 4-, 8-, 10-, and 16-membered rings, which showed excellent performance for both Li and Na-ion storage, with low migration barriers and theoretical capacities exceeding 1000 mAh/g.

On the other hand, a promising approach for designing new 2D carbon materials involves starting from experimen- tally known molecular precursors [3, 33, 34]. By assembling these building blocks into extended networks, it becomes possible to tune hybridization, bonding geometry, and elec- tronic structure rationally. This strategy enables the design of low-symmetry carbon lattices with tailored band gaps, mechanical anisotropy, and surface reactivity [35-37], facil- itating their integration into nanoelectronics, energy storage, and catalysis platforms [38-40].

Among such precursors, bicyclopropylidene stands out as a highly strained hydrocarbon consisting of two fused cyclopropyl rings connected by a central double bond [41]. Its unique geometry introduces significant ring strain and perturbs the conventional $\pi$-electron delocalization typically found in planar $sp^2$-hybridized systems [42, 43]. This reac- tivity has been explored in various transformations includ- ing rearrangements, cycloadditions, and polymerization [44,45], making it a compelling unit for constructing novel carbon frameworks.

In this work, we propose a new two-dimensional car- bon allotrope named *Propylenidene* (PPD), formed by or- ganizing bicyclopropylidene units into a rectangular lat- tice comprising 3-, 8-, and 10-membered rings. Using den- sity functional theory (DFT), we systematically investigate its structural, electronic, optical, and mechanical proper- ties. The dynamical and thermal stability of PPD is con- firmed through phonon dispersion, cohesive energy analysis, Born-Huang mechanical criteria, and *ab initio* molecular dynamics (AIMD). The results suggest that PPD is a ther- mally robust and conductive 2D material with potential relevance for applications in hydrogen storage, alkali-ion batteries, and heterogeneous catalysis. While the present work focuses on the pristine monolayer, future studies will explore its performance as a tunable platform for energy conversion and storage applications.

## 2. Methodology

To investigate the structural, electronic, mechanical, and optical properties of the proposed Propylenidene (PPD) monolayer, we employed first-principles calculations based on density functional theory (DFT) [46], as implemented in the Vienna Ab Initio Simulation Package (VASP) [47,48]. The exchange-correlation energy was treated using the generalized gradient approximation (GGA) with the Perdew-Burke-Ernzerhof (PBE) functional [49], and the core-valence electron interactions were described by the projector-augmented wave (PAW) method [48? ].

A plane-wave kinetic energy cutoff of 520 eV was employed to ensure accurate total energy convergence. Structural optimization was performed using the conjugate- gradient algorithm until the Hellmann-Feynman forces on each atom were below 0.01 eV/Å, and the total energy variation between consecutive ionic steps was less than $10^{-5}$ eV. A vacuum region of 15 Å was included along the out-of-plane direction to prevent interactions between periodic images. Brillouin zone sampling was performed using a $\Gamma$-centered Monkhorst-Pack grid of $12 \times 18 \times 1$ for static and electronic calculations, and a coarser $6 \times 9 \times 1$ mesh during structural relaxations.

To account for long-range van der Waals interactions, especially relevant in porous or open frameworks, Grimme's DFT-D4 correction scheme [50] was applied.

The thermodynamic stability of the PPD monolayer was assessed by computing the cohesive energy ($E_{\text{coh}}$), defined as:
$$
E_{\text{coh}} = \frac{E_{\text{tot}} - \sum_{i} n_{i} E_{i}}{\sum_{i} n_{i}}, \tag{1}
$$
where $E_{\text{tot}}$ is the total energy of the relaxed structure, $E_{i}$ is the total energy of an isolated atom of type $i$ (in this case, carbon), and $n_{i}$ is the number of atoms of that type in the unit cell.

The dynamical stability was confirmed through phonon dispersion calculations using density functional perturbation theory (DFPT), as implemented in the Phonopy code [51]. Thermal stability was further examined via *ab initio* molec- ular dynamics (AIMD) simulations in the canonical (NVT) ensemble, using the Nosé-Hoover thermostat [52, 53], per- formed at multiple temperatures (300 K, 600 K, 900 K, and1200 K) for a total simulation time of 5 ps and a time step of 1 fs. The scanning tunneling microscopy (STM) images were obtained using self-consistent calculations within the Quantum ESPRESSO package [54], considering a bias volt- age of 1.0 V.

## 3. Results and Discussion

PPD is represented by a rectangular unit cell that belongs to the *Pmmm* (No. 47) space group, with lattice parameters $a = 6.70$ Å and $b = 3.80$ Å (see Fig.1(a)). This rectan- gular cell contains three distinct carbon atoms, namely C1 (0.89746, 0.00000, 0.00000), C2 (0.28464, 0.81572, 0.00000), and C3 (0.60855, 0.50000, 0.00000). This atomic arrange- ment forms a 2D carbon framework comprising 3-, 8-, and10-membered rings. The 10- and 8-membered pores have diameters of 5.24 Å and 4.07 Å, respectively.

The bond lengths in PPD are not uniform, reflecting the coexistence of different ring sizes and the angular strain of

Propylenidene

bicyclopropylidene motifs. Bonds within the cyclopropene-like rings range from 1.40 Å to 1.41 Å. Connections between the 3-membered rings and the larger 8-membered rings also exhibit lengths near 1.41 Å, indicating partial double-bond character. In contrast, the bonds bridging the 10-membered rings extend up to 1.46 Å. Bond angles in the 3-membered rings are near 60.0°; in 8-membered rings, they range from 120.6° to 149.65°; and in ten-membered rings, from 118.5° to 151.2°. The novel structure exhibits a cohesive energy ($E_{\text{coh}}$) of (-7.23 eV/atom), indicating the energy necessary to break down the solid into individual atoms. This value is comparable to that obtained for other carbon allotropes such as graphene (-7.68 eV/atom), T-graphene (-7.45 eV/atom), Graphenylene (-7.33 eV/atom), Graphenyl-diene (-6.92 eV/atom), and Graphyne (-7.20 eV/atom), all calculated at the same theory level of this study.

The dynamical stability of PPD was evaluated by calculating the phonon band dispersion along the high-symmetry paths of the Brillouin zone, as shown in Fig. 1(b). The absence of imaginary frequencies in the phonon spectrum confirms its stability. At the $\Gamma$-point, three acoustic phonon modes are observed. Most phonon branches are within the 0-23 THz range, displaying multiple crossings, indicative of various thermal conductivity pathways. In the 27-44 THz range, the dispersion is reduced. As expected for two-dimensional materials, the phonon dispersion of PPD exhibits three acoustic branches: the longitudinal acoustic (LA), transverse acoustic (TA), and out-of-plane flexural acoustic (ZA) modes. The LA and TA modes show a linear dispersion near the $\Gamma$ point, reflecting in-plane vibrational motions typical of 2D systems. The third acoustic mode, the ZA mode, exhibits a parabolic dispersion near $\Gamma$, which is a well-known feature in 2D materials due to the restoring force being weaker for out-of-plane atomic displacements [55].

The highest vibrational frequency of PPD is approximately 57 THz ($\sim$1900 cm⁻¹), which is slightly higher than the LO/TO mode of graphene at the $\Gamma$-point ($\sim$48 THz, $\sim$1580 cm⁻¹) [56]. This increase is attributed to the presence of highly strained three-membered rings, which shift the optical modes to higher frequencies. The low-frequency acoustic modes (ZA, TA, LA) follow a similar trend to graphene but exhibit greater dispersion due to the lower lattice symmetry of PPD. In contrast to graphene, PPD displays a phonon gap between 44 and 50 THz, which originates from its unique 3-8-10 ring topology. The phonon dispersion was computed along the $\Gamma$-Y-S-X-$\Gamma$-S path in the rectangular Brillouin zone, shown in the inset, which differs from the hexagonal Brillouin zone characteristic of graphene.

The thermal stability of PPD was evaluated through *ab initio* molecular dynamics (AIMD) simulations in the canonical (NVT) ensemble for 5 ps with a 1 fs time step at four different temperatures: 300, 600, 900, and 1200 K. Fig. 2(a) shows the temporal evolution of the total energy, which exhibits only minor fluctuations at all temperatures, indicating the absence of structural collapse during the simulations. The corresponding final snapshots of the atomic configurations are displayed in Fig. 2(b-e). At 300 K [Fig. 2(b)], the monolayer retains its pristine geometry without noticeable distortions, with bond lengths fluctuating in the 1.35-1.50 Å range. Increasing the temperature to 600 K [Fig. 2(c)] results in slight out-of-plane oscillations, with bond lengths varying between 1.36-1.53 Å, but the overall topology and pore arrangement remain intact. At 900 K [Fig. 2(d)], moderate bond-angle deviations and enhanced rippling are observed, with bond lengths spanning 1.32-1.56 Å, yet the framework preserves its connectivity. Even at 1200 K [Fig. 2(e)], despite more pronounced thermal distortions and increased undulation amplitudes, the bond length range (1.32-1.51 Å) remains within values typical of stable $sp^2$-hybridized carbon networks. These results confirm that PPD maintains robust thermal stability up to at least 1200 K.

Fig. 3(a) shows the electronic band structure of propylenidene calculated using the PBE (red curves) and HSE06 (blue curves) functionals. In both cases, the valence and conduction bands overlap at the Fermi level ($E_F$), confirming the metallic nature of the material with no discernible band gap. Several bands cross $E_F$ along different high-symmetry directions, indicating the presence of multiple conduction channels. Closer to the $\Gamma$ point, bands near $E_F$ exhibit steeper slopes, indicating lighter effective masses and potentially higher carrier velocities. While the general dispersion features are preserved across both methods, the HSE06 functional introduces a shift. It modifies the curvature of certain bands due to the improved treatment of exchange interactions.

The projected density of states (PDOS), shown in Fig. 3(b), further elucidates the orbital contributions to the electronic structure. States in the vicinity of $E_F$ are dominated by $p_z$ orbitals, consistent with $\pi$-type delocalization across the planar carbon network, which facilitates metallic conduction. Contributions from $p_x$ and $p_y$ orbitals are smaller near $E_F$, while s-orbitals are mostly located at deeper energies, below -4 eV, indicating their minimal role in conduction processes. The dominance of $p_z$ character near the Fermi level suggests that the metallicity arises primarily from $\pi$-electron overlap, a feature common in conjugated carbon frameworks [32, 57-59].

To better understand the charge distribution and bonding characteristics of PPD, we examined its electron localization function (ELF), depicted in Fig. 4(a). The ELF effectively evaluates electron localization. A value of 1 indicates highly localized electrons, typical in covalent bonds or lone pairs. Conversely, a 0.5 reflects delocalized electrons akin to a homogeneous electron gas, and a value of 0 represents areas with minimal electron density.

In PPD, the bicyclopropylidene motifs exhibit areas of high electron localization, as revealed by the electron localization function (ELF) map in Fig.4(a). This localization is primarily due to the angular strain imposed by the highly constrained 3-membered rings. In the bonds linking adjacent bicyclopropylidene units within the 8-membered rings, the ELF shows a noticeable reduction, suggesting a lower angular strain for these bonds. A similar trend is observed in the 10-membered rings, where the $\pi$ bonds of

Propylenidenide

![](./images/1137355750700482575_1.jpg)
![](./images/1137355750700482575_2.jpg)

Figure 1: (a) Top view of atomic structure of propylenidenide (PPD) monolayer. (b) Phonon dispersion of PPD along high-symmetry paths of the Brillouin zone.

the bicyclopropylidene motifs display weaker localization compared to the cyclopropane-like rings themselves.

Scanning tunneling microscopy (STM) simulations, shown in Fig. 4(b), provide further insight into the spatial distribution of the electronic states near the Fermi level. Bright spots in the simulated STM image correspond to regions with a high local density of states (LDOS), which are mainly associated with the cyclopropene-like rings within the PPD framework. These features could serve as experimental fingerprints for identifying the material.

To investigate the optical properties of PPD, we calculated its absorption coefficient, as shown in Fig. 5. In the absorption spectra [Fig. 5(top)], the first notable feature appears in the $xx$ polarization as a moderate peak of approximately 1.5% located at ~0.8 eV, within the infrared region. This low-energy response is likely associated with $\pi-\pi^{*}$ electronic transitions, consistent with the delocalized $p_{z}$ states near the Fermi level observed in the band structure and PDOS. The next pronounced peak emerges in the $yy$ polarization, reaching ~4.0% at ~2.3 eV, within the visible range, indicating stronger light-matter coupling for this polarization and suggesting enhanced interband transitions along the $y$ crystallographic direction. At higher photon energies, both polarizations exhibit relatively strong absorption in the ultraviolet region, with maxima exceeding 4%.

The reflectivity spectra [Fig. 5(middle)] remain low ($R < 0.07$) throughout the visible and near-UV regions, with peaks coinciding with the main absorption resonances, confirming that these features stem from direct interband transitions. The transmittance [Fig. 5(down)] remains high ($T > 92\%$) across most of the studied range, with minima aligned with the absorption peaks. The clear difference in optical profile between the $xx$ and $yy$ components underscores the pronounced optical anisotropy of propylenidenide, which could be exploited for polarization-sensitive optoelectronic applications.

The elastic constants of PPD were recalculated to refine the assessment of its mechanical properties, which are crucial for understanding structural stability and elastic response. The updated independent elastic constants are $C_{11} = 235.06$ N/m, $C_{22} = 225.76$ N/m, $C_{12} = C_{21} = 81.25$ N/m, and $C_{66} = 55.89$ N/m. According to the Born-Huang stability criteria for a rectangular lattice [60] — namely, $C_{11} > 0$, $C_{66} > 0$, and $C_{11}C_{22} > C_{12}^{2}$ — the PPD monolayer is mechanically stable.

The polar plots of the in-plane mechanical properties of propylenidenide (PPD) [Fig. 6(a–c)] reveal a distinct four-fold symmetry, consistent with the orthorhombic $Pmmm$ space group of the crystal lattice. This symmetry underscores the direct influence of the atomic-scale bonding topology on the macroscopic mechanical response, and reflects the intrinsic anisotropy of PPD. Young's modulus ($Y$), which quantifies the resistance to uniaxial deformation, shows moderate anisotropy, varying between 164.46 N/m and 205.83 N/m (an anisotropy ratio of 1.25). The highest stiffness occurs along the $a$-axis and $b$-axis directions ($\theta = 0^{\circ}$ and $\theta = 90^{\circ}$), which are oriented parallel and perpendicular, respectively, to the bicyclopropylidene motifs. In contrast, the minimum stiffness ($Y_{\text{min}} = 164.46$ N/m) is observed along the diagonal directions ($\theta = 45^{\circ}$, $135^{\circ}$, etc.), where applied stress

Propylenidene

![](./images/1137355750700482575_3.jpg)

Figure 2: Ab initio molecular dynamics (AIMD) simulations of PPD in the NVT ensemble over 5 ps with a 1 fs time step at four different temperatures. (a) Time evolution of the total energy at 300 K, 600 K, 900 K, and 1200 K, showing only small fluctuations and no signs of structural collapse. Final snapshots of the atomic configurations after the simulations at (b) 300 K, (c) 600 K, (d) 900 K, and (e) 1200 K.

induces torsional deformation of the C–C bonds that bridge two bicyclopropylidene units to form the octagonal rings. These bonds, measuring $1.46\ \mathring{A}$ as previously highlighted, correspond to single bonds and thus possess greater rotational freedom, leading to a softer elastic response in these orientations.

The shear modulus $G(\theta)$ [Fig. 6(b)] and Poisson's ratio $v(\theta)$ [Fig. 6(c)] display the same four-fold rotational pattern, reflecting the fact that the orthorhombic symmetry imposes identical elastic responses under $90^\circ$ rotations. $G$ ranges from 55.89 N/m to 74.55 N/m, with an anisotropy ratio of 1.33. $v$ spans from 0.346 to 0.472, yielding an anisotropy ratio of 1.37.

The mechanical properties summarized in Table 1 highlight the balanced stiffness and anisotropy of the newly proposed propylenidene. Its Young's modulus spans from 164.46 N/m to 205.83 N/m, exceeding that of $\alpha$-anthraphenylene while remaining below $\beta$- and $\gamma$-anthraphenylene, as well as more rigid allotropes such as graphene and penta-graphene. Compared to graphenylene, a porous carbon allotrope with experimentally reported synthesis [61] and a Young's modulus of 209.02 N/m (isotropic), propylenidene presents slightly lower stiffness but introduces mechanical anisotropy, which can be advantageous for direction-dependent applications. The maximum Poisson's ratio ($v_{\text{max}} = 0.47$) is among the highest in the dataset, suggesting greater lateral strain accommodation under uniaxial loading compared to materials with low $v$, such as graphene ($v = 0.17$) or graphenylene ($v = 0.27$). In terms of shear modulus, propylenidene ($G_{\text{max}} = 74.55\ \text{N/m}, G_{\text{min}} = 55.89\ \text{N/m}$) surpasses $\alpha$-anthraphenylene and is comparable to $\beta$-anthraphenylene, indicating robust resistance to shear deformations with moderate anisotropy. Overall, the combination of relatively high stiffness, significant but controlled anisotropy, and elevated Poisson's ratio positions propylenidene as a mechanically resilient and flexible 2D carbon allotrope, bridging the gap between highly rigid materials like graphene and more compliant, experimentally verified porous networks such as graphenylene.

Propylenidene

![](./images/1137355750700482575_4.jpg)

Figure 3: (a) Electronic band structure of propylenidene calculated using PBE (red curves) and HSE06 (blue curves) along the high-symmetry path $\Gamma$-$X$-$S$-$Y$-$\Gamma$-$S$. Both methods confirm metallic behavior, with several bands crossing the Fermi level ($E_F$) and an absence of a band gap. (b) Projected density of states (PDOS) showing the orbital contributions: $p_z$ orbitals dominate near $E_F$, consistent with $\pi$-electron delocalization responsible for the metallic conduction.

Table 1
Maximum and minimum values of Young's modulus ($Y_{\text{max}}, Y_{\text{min}}$) (N/m), Poisson's ratio ($v_{\text{max}}, v_{\text{min}}$), and shear modulus ($G_{\text{max}}, G_{\text{min}}$) (N/m) for several carbon monolayers, including the newly proposed propylenidene. The values were calculated employing the same theoretical framework employed to study the propylenidene.

<table>
  <thead>
    <tr>
      <th></th>
      <th>$Y_{\text{max}}/Y_{\text{min}}$</th>
      <th>$v_{\text{max}}/v_{\text{min}}$</th>
      <th>$G_{\text{max}}/G_{\text{min}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Propylenidene (this work)</td>
      <td>205.83/164.46</td>
      <td>0.472/0.346</td>
      <td>74.55/55.89</td>
    </tr>
    <tr>
      <td>Graphene [7]</td>
      <td>345.42/345.42</td>
      <td>0.17/0.17</td>
      <td>147.60/147.60</td>
    </tr>
    <tr>
      <td>Penta-graphene [62]</td>
      <td>271.81/266.67</td>
      <td>-0.08/-0.10</td>
      <td>151.21/144.98</td>
    </tr>
    <tr>
      <td>T-graphene [63]</td>
      <td>293.90/148.02</td>
      <td>0.58/0.16</td>
      <td>148.02/126.57</td>
    </tr>
    <tr>
      <td>$\gamma$-anthraphenylene [57]</td>
      <td>281.00/158.27</td>
      <td>0.47/0.25</td>
      <td>79.67/57.35</td>
    </tr>
    <tr>
      <td>$\beta$-anthraphenylene [57]</td>
      <td>215.50/167.53</td>
      <td>0.34/0.23</td>
      <td>76.26/64.35</td>
    </tr>
    <tr>
      <td>$\alpha$-anthraphenylene [57]</td>
      <td>169.94/127.89</td>
      <td>0.40/0.26</td>
      <td>65.29/52.87</td>
    </tr>
    <tr>
      <td>PHE-graphene[64]</td>
      <td>262.29/262.29</td>
      <td>0.26/0.26</td>
      <td>103.91/103.91</td>
    </tr>
    <tr>
      <td>Graphenylene [61, 65]</td>
      <td>209.02/209.02</td>
      <td>0.27/0.27</td>
      <td>82.11/82.11</td>
    </tr>
    <tr>
      <td>Graphenyldiene [11]</td>
      <td>122.47/122.47</td>
      <td>0.35/0.35</td>
      <td>45.29/45.29</td>
    </tr>
  </tbody>
</table>

## 4. Conclusion

This study presents a comprehensive analysis of the structural, electronic, mechanical, and optical properties of the newly proposed porous 2D carbon allotrope, propylenidene (PPD). Our first-principles calculations confirm its stability, supported by phonon dispersion and molecular dynamics simulations. The 2D structure, composed of 10-8-3 carbon-membered rings, introduces distinctive pores with diameters of 5.24 Å and 4.07 Å, respectively.

PPD demonstrates metallic behavior, with a large contribution of $\pi$ p$_z$ states closer to the Fermi level. Optically, PPD exhibits absorption in the infrared and visible range, showing directional dependence in its response. Mechanically, the material presents high anisotropy for Young's modulus, shear modulus, and Poisson's ratio, with significant variation across different crystallographic directions. Overall, PPD emerges as a promising material with a combination of stability, metallicity, and tailored mechanical and optical properties, making it an exciting candidate for future research

Propylenidene

![](./images/1137355750700482575_5.jpg)

Figure 4: (a) Electron localization function (ELF) of PPD. (b) Simulated scanning tunneling microscopy (STM) for PPD.

and practical applications in advanced nanotechnology and materials science.

## Data access statement
Data supporting the results can be accessed by contacting the corresponding author.

## Conflicts of interest
The authors declare no conflict of interest.

## Acknowledgements
This work was supported by the Brazilian funding agencies Fundação de Amparo à Pesquisa do Estado de São Paulo - FAPESP (grant no. 2022/03959-6, 2022/14576-0, 2020/01144-0,2024/05087-1,2024/19996-3 and 2022/16509-9), and National Council for Scientific, Technological Development - CNPq (grant no. 307213/2021-8). L.A.R.J. acknowledges the financial support from FAP-DF grants 00193.00001808/2022-71 and 00193-00001857/2023-95, FAPDF-PRONEM grant 00193.00001247/2021-20, PDPG- FAPDF-CAPES Centro-Oeste 00193-00000867/2024-94, and CNPq grants 350176/2022 - 1 and 167745/2023 - 9. The computational facilities were supported by resources supplied by the "Centro Nacional de Processamento de Alto Desempenho em São Paulo (CENAPAD-SP)" and CENAPAD-RJ (SDumont).

## Declaration of generative AI and AI-assisted technologies in the writing process
During the preparation of this work the authors used Writefull in order to improve the readability and language of the manuscript. After using this tool/service, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.

![](./images/1137355750700482575_6.jpg)

Figure 5: Optical properties of propylenidene for light polarized along the x (black curves) and y (red curves) crystallographic directions: (top) absorption coefficient $\alpha$, (middle) reflectivity $R$, and (bottom) transmittance $T$ as functions of photon energy.

## CRediT authorship contribution statement
José A. S. Laranjeira: Conceptualization of this study, Methodology, Review and editing, Investigation, Formal analysis, Writing - review & editing, Writing - original draft.
K. A. L. Lima: Conceptualization of this study, Methodology, Review and editing, Investigation, Formal analysis, Writing - review & editing, Writing - original draft.
Nicolas F. Martins: Conceptualization of this study, Methodology, Review and editing, Investigation, Formal analysis, Writing - review & editing, Writing - original draft.
Luis A. Cabral: Investigation, Formal analysis, Resources, Writing - review & editing.
L.A. Ribeiro Junior: Conceptualization of this study, Methodology, Review and editing, Investigation, Formal analysis, Writing - review & editing, Writing - original draft.
Julio R. Sambrano: Conceptualization of this study, Methodology, Review and

Propylenidene

[25] Vikram Mahamiya, Alok Shukla, and Brahmananda Chakraborty. Potential reversible hydrogen storage in li-decorated carbon allotrope pai-graphene: A first-principles study. *International Journal of Hy- drogen Energy*, 48(96):37898–37907, 2023. Materials and methods for hydrogen energy.

[26] Lan Bi, Zhicheng Miao, Yan Ge, Ziyi Liu, Yi Xu, Jie Yin, Xin Huang, Yunhui Wang, and Zhihong Yang. Density functional theory study on hydrogen storage capacity of metal-embedded penta-octa- graphene. *International Journal of Hydrogen Energy*, 47(76):32552–32564, 2022.

[27] Kunyang Cheng, Mingyang Shi, Xiujuan Cheng, Xuying Zhou, Chuanyu Zhang, Gang Jiang, and Jiguang Du. Metal-decorated m- graphene for high hydrogen storage capability and reversible hydro- gen release. *Fuel*, 374:132405, 2024.

[28] Meijuan Cheng, Dongliang Chen, Rundong Chen, Weilong Liu, Qiubao Lin, and Zizhong Zhu. Metallized hot-graphene: A novel reversible hydrogen storage medium with ultrahigh capacity. *Inter- national Journal of Hydrogen Energy*, 48(87):34164–34179, 2023.

[29] Palanivel Umadevi, Elayappan Vijayakumar, and Senthilkumar Lak- shmipathi. Exploring the potential of alkali metal-decorated tph- graphene nanoribbons for high-efficiency hydrogen storage: A first- principles study. *International Journal of Hydrogen Energy*, 56:1092–1100, 2024.

[30] Nicolas F. Martins, José A. Laranjeira, and Julio R. Sambrano. Ocd- graphene: a 2d carbon allotrope with high theoretical capacity for sodium-ion batteries. *FlatChem*, 53:100910, 2025.

[31] Xing Hong Cai, Qiang Yang, Shaohui Zheng, and Min Wang. Net- c18: A predicted two-dimensional planar carbon allotrope and poten- tial for an anode in lithium-ion battery. *ENERGY & ENVIRONMEN- TAL MATERIALS*, 4(3):458–464, 2021.

[32] Kleuton A.L. Lima, José A.S. Laranjeira, Nicolas F. Martins, Alexan- dre C. Dias, Julio R. Sambrano, Douglas S. Galvão, and Luiz A. Ribeiro Junior. Petal-graphyne: A novel 2d carbon allotrope for high-performance li and na ion storage. *Journal of Energy Storage*, 130:117235, 2025.

[33] Elena Pérez-Elvira, Ana Barragán, Aurelio Gallardo, José Santos, Cristina Martín-Fuentes, K. Lauwaet, J. Gallego, R. Miranda, Hide- hiro Sakurai, José I. Urgel, Jonas Björk, Nazario Martín, and D. Écija. Coronene-based 2d networks by on-surface skeletal rearrangement of sumanene precursors. *Angewandte Chemie (International Ed. in English)*, 64, 2024.

[34] Chunxiang Zhao, Yiqi Yang, C. Niu, Jia-Qi Wang, and Yu Jia. C-57 carbon: A two-dimensional metallic carbon allotrope with pentagonal and heptagonal rings. *Computational Materials Science*, 2019.

[35] Teng Wan, Qingyang Fan, Mingfei Wei, Jie Wu, Dangli Gao, Yanxing Song, and Sining Yun. Design and physical property study of seven novel carbon allotropes by random methods combined group and graph theories. *Computational Materials Science*, 2024.

[36] Shunhong Zhang, Jian Zhou, Qian Wang, Xiaoshuang Chen, Y. Kawa- zoe, and P. Jena. Penta-graphene: A new carbon allotrope. *Proceed- ings of the National Academy of Sciences*, 112:2372 – 2377, 2015.

[37] Q. Wei, Quan Zhang, Haiyan Yan, and Meiguang Zhang. A new superhard carbon allotrope: tetragonal c64. *Journal of Materials Science*, 52:2385–2391, 2017.

[38] Yi Peng, Bingzhang Lu, and Shaowei Chen. Carbon-supported single atom catalysts for electrochemical energy conversion and storage. *Advanced Materials*, 30, 2018.

[39] Chao Hu, Mingyu Li, J. Qiu, and Ya-Ping Sun. Design and fabrication of carbon dots for energy conversion and storage. *Chemical Society reviews*, 48 8:2315–2337, 2019.

[40] Hengjia Shao, Li Zhong, Xingqiao Wu, Yun-Xiao Wang, Sean C. Smith, and Xin Tan. Recent progress of density functional theory studies on carbon-supported single-atom catalysts for energy storage and conversion. *Chemical communications*, 2025.

[41] Armin De Meijere, Sergei I Kozhushkov, Thomas Späth, Malte Von Seebach, Sandra Löhr, Hanno Nüske, Tim Pohlmann, Mazen Es-Sayed, and Stefan Bräse. Bicyclopropylidene. a unique tetrasub- stituted alkene and versatile c. *Pure Appl. Chem*, 72(9):1745–1756, 2000.

[42] Jan Foerstner, Sergej Kozhushkov, Paul Binger, Petra Wedemann, Mathias Noltemeyer, Armin de Meijere, and Holger Butenschön. The first metal complexes of bicyclopropylidene, a unique tetrasubstituted alkene ligand. *Chemical Communications*, (2):239–240, 1998.

[43] A De Meijere, Ihsan Erden, Walter Weber, and Dieter Kaufmann. Bicyclopropylidene: cycloadditions onto a unique olefin. *The Journal of Organic Chemistry*, 53(1):152–161, 1988.

[44] Armin de Meijere, Malte von Seebach, Stefan Zöllner, Sergei I Kozhushkov, Vladimir N Belov, Roland Boese, Thomas Haumann, Jordi Benet-Buchholz, Dmitrii S Yufit, and Judith AK Howard. Spiro- cyclopropanated bicyclopropylidenes: Straightforward preparation, physical properties, and chemical transformations. *Chemistry--A European Journal*, 7(18):4021–4034, 2001.

[45] Wei Wang, Wen-Jie Zhang, Lei Wang, Ching Kheng Quah, Hoong- Kun Fun, Jian-Hua Xu, and Yan Zhang. Photoinduced reactions of para-quinones with bicyclopropylidene leading to diverse polycyclic compounds with spirocyclopropanes. *The Journal of Organic Chem- istry*, 78(12):6211–6222, 2013.

[46] Pierre Hohenberg and Walter Kohn. Inhomogeneous electron gas. *Physical review*, 136(3B):B864, 1964.

[47] Georg Kresse and Jürgen Furthmüller. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. *Physical review B*, 54(16):11169, 1996.

[48] Georg Kresse and Daniel Joubert. From ultrasoft pseudopoten- tials to the projector augmented-wave method. *Physical review b*, 59(3):1758, 1999.

[49] John P Perdew, Kieron Burke, and Matthias Ernzerhof. General- ized gradient approximation made simple. *Physical review letters*, 77(18):3865, 1996.

[50] Eike Caldeweyher, Christoph Bannwarth, and Stefan Grimme. Exten- sion of the d3 dispersion coefficient model. *The Journal of Chemical Physics*, 147(3):034112, 07 2017.

[51] Atsushi Togo and Isao Tanaka. First principles phonon calculations in materials science. *Scripta Materialia*, 108:1–5, 2015.

[52] Shuichi Nosé. A unified formulation of the constant temperature molecular dynamics methods. *The Journal of chemical physics*, 81(1):511–519, 1984.

[53] William G Hoover. Canonical dynamics: Equilibrium phase-space distributions. *Physical review A*, 31(3):1695, 1985.

[54] Paolo Giannozzi, Stefano Baroni, Nicola Bonini, Matteo Calandra, Roberto Car, Carlo Cavazzoni, Davide Ceresoli, Guido L Chiarotti, Matteo Cococcioni, Ismaila Dabo, Andrea Dal Corso, Stefano de Gironcoli, Stefano Fabris, Guido Fratesi, Ralph Gebauer, Uwe Gerstmann, Christos Gougoussis, Anton Kokalj, Michele Lazzeri, Layla Martin-Samos, Nicola Marzari, Francesco Mauri, Riccardo Mazzarello, Stefano Paolini, Alfredo Pasquarello, Lorenzo Paulatto, Carlo Sbraccia, Sandro Scandolo, Gabriele Sclauzero, Ari P Seitso- nen, Alexander Smogunov, Paolo Umari, and Renata M Wentzcov- itch. Quantum espresso: a modular and open-source software project for quantum simulations of materials. *Journal of Physics: Condensed Matter*, 21(39):395502, sep 2009.

[55] Xuefei Yan, Xiangyue Cui, Bowen Wang, Hejin Yan, Yongqing Cai, and Qingqing Ke. Surface asymmetry induced turn-overed lifetime of acoustic phonons in monolayer mosse. *iScience*, 26(5):106731, 2023.

[56] L. A. Falkovsky. Phonon dispersion in graphene. *Journal of Experimental and Theoretical Physics*, 105(2):397–403, Aug 2007.

[57] K.A.L. Lima, José A.S. Laranjeira, Nicolas F. Martins, Sérgio A. Azevedo, Julio R. Sambrano, and L.A. Ribeiro. Anthraphenylenes: Porous 2d carbon monolayers with biphenyl-anthracene frameworks. *Physica B: Condensed Matter*, 713:417299, 2025.

[58] Jose A. S. Laranjeira, Kleuton A. Lima, Nicolas F. Martins, Luiz A. Ribeiro Junior, Douglas S. Galvão, and Julio R. Sambrano. A novel graphyne-like carbon allotrope: 2d dewar-anthracyne. *Journal of Inorganic and Organometallic Polymers and Materials*, Jul 2025.

[59] José A. S. Laranjeira, Nicolas F. Martins, Kleuton Antunes Lopes Lima, Luis A. Cabral, Luiz A. Ribeiro Júnior, Douglas S. Galvão, and Julio R. Sambrano. Tphe-graphene: A first-principles

Propylenidene

study of a new 2d carbon allotrope for hydrogen storage. *ACS Omega*, 0(0):null, 0.

[60] Max Born. On the stability of crystal lattices. i. In *Mathematical Proceedings of the Cambridge Philosophical Society*, volume 36, pages 160–172. Cambridge University Press, 1940.

[61] Qi-Shi Du, Pei-Duo Tang, Hua-Lin Huang, Fang-Li Du, Kai Huang, Neng-Zhong Xie, Si-Yu Long, Yan-Ming Li, Jie-Shan Qiu, and Ri-Bo Huang. A new type of two-dimensional carbon crystal prepared from 1, 3, 5-trihydroxybenzene. *Scientific reports*, 7(1):40796, 2017.

[62] Shunhong Zhang, Jian Zhou, Qian Wang, Xiaoshuang Chen, Yoshiyuki Kawazoe, and Puru Jena. Penta-graphene: A new carbon allotrope. *Proceedings of the National Academy of Sciences*, 112(8):2372–2377, 2015.

[63] Xian-Lei Sheng, Qing-Bo Yan, Fei Ye, Qing-Rong Zheng, and Gang Su. T-carbon: a novel carbon allotrope. *Physical review letters*, 106(15):155703, 2011.

[64] Li Zeng, Yingxiang Cai, Zhihao Xiang, Yu Zhang, and Xuechun Xu. A new metallic $\pi$-conjugated carbon sheet used for the cathode of li–s batteries. *RSC advances*, 9(1):92–98, 2019.

[65] Qi Song, Bing Wang, Ke Deng, Xinliang Feng, Manfred Wagner, Julian D Gale, Klaus Müllen, and Linjie Zhi. Graphenylene, a unique two-dimensional carbon network with nondelocalized cyclo-hexatriene units. *Journal of Materials Chemistry C*, 1(1):38–41, 2013.