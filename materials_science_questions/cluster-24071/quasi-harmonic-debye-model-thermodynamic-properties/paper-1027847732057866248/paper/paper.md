**Article**

# Ab Initio Studies of Mechanical, Dynamical, and Thermodynamic Properties of Fe-Pt Alloys

Ndanduleni Lesley Lethole * and Patrick Mukumba

Department of Physics, University of Fort Hare, Private Bag X1314, Alice 5700, South Africa;
pmukumba@ufh.ac.za

* Correspondence: nlethole@ufh.ac.za

**Abstract:** The density functional theory (DFT) framework in the generalized gradient approximation (GGA) was employed to study the mechanical, dynamical, and thermodynamic properties of the ordered bimetallic Fe-Pt alloys with stoichiometric structures Fe₃Pt, FePt, and FePt₃. These alloys exhibit remarkable magnetic properties, high coercivity, excellent chemical stability, high magnetization, and corrosion resistance, making them potential candidates for application in high-density magnetic storage devices, magnetic recording media, and spintronic devices. The calculations of elastic constants showed that all the considered Fe-Pt alloys satisfy the Born necessary conditions for mechanical stability. Calculations on macroscopic elastic moduli showed that Fe-Pt alloys are ductile and characterized by greater resistance to deformation and volume change under external shearing forces. Furthermore, Fe-Pt alloys exhibit significant anisotropy due to variations in elastic constants and deviation of the universal anisotropy index value from zero. The equiatomic FePt showed dynamical stability, while the others showed softening of soft modes along high symmetry lines in the Brillouin zone. Moreover, from the phonon densities of states, we observed that Fe atomic vibrations are dominant at higher frequencies in Fe-rich compositions, while Pt vibrations are prevalent in Pt-rich rich.

**Keywords:** Fe-Pt alloys; elastic constants; Debye temperature; phonon dispersion curves; stability; mechanical stability; thermodynamic properties

---

## 1. Introduction

Ferromagnetic Fe-Pt intermetallic alloys are a significant group of solid-state materials, exhibiting intriguing physical and chemical properties that are inherently dependent on their specific chemical compositions. These materials find applications across various industries, including catalysis for chemical reactions, ultrahigh-density magnetic data storage such as hard disk drives and magnetic sensors, spintronic devices, and high-temperature mechanics due to their large uniaxial magnetocrystalline anisotropies (MCA) and high coercivity, amongst other desirable magnetic properties [1–4]. The large MCA presents the potential of decreasing the magnetic particle dimensions to a few nanometers of grain sizes without degrading the thermal stability of the magnetization axis direction. Crystallographically, they stabilize in two Strukturbericht symbols and three space groups: L1₀ (body-centered tetragonal $P4/mmm$-FePt) and L1₂ (face-centered cubic $Pm\overline{3}m$-Fe₃Pt, $Pm\overline{3}m$-FePt₃ and body-centered tetragonal $I4/mmm$-Fe₃Pt). The L1₀ phase features an alternating arrangement of Fe and Pt atoms which can undergo a disorder–order phase transition from face-centered cubic (fcc) to tetragonal at temperatures of approximately above 650 °C [5]. Müller et al. employed both analytic bond-order potential and lattice-based Monte Carlo simulations and reported that the observed disorder–order transition temperature decreases with particle grain size [6,7]. Furthermore, Yu et al. reported that the ferromagnetic orientation and dynamical stability break down above the threshold pressure of 96.7 GPa as a result of undergoing spontaneous magnetization [8]. The transformation

![](./images/1027847732057866248_1.jpg)

Citation: Lethole, N.L.; Mukumba, P.
Ab Initio Studies of Mechanical,
Dynamical, and Thermodynamic
Properties of Fe-Pt Alloys. *Materials*
2024, 17, 3879. https://doi.org/
10.3390/ma17153879

Academic Editor: Grega
Klančnik

Received: 2 July 2024
Revised: 29 July 2024
Accepted: 1 August 2024
Published: 5 August 2024

![](./images/1027847732057866248_2.jpg)

Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

---

Materials 2024, 17, 3879. https://doi.org/10.3390/ma17153879
https://www.mdpi.com/journal/materials

has significant implications for understanding the dynamical properties of Fe-Pt alloys, as it influences the material's magnetic behavior band mechanical response. Furthermore, in L1₀ bimetallic compounds, the difference in atomic size between the two constituent atoms is less than 15%. Thus, the orientation of magnetization and magnitude of the local magnetic moment and stability are significantly influenced by the concentrations and atomic sizes of Fe and Pt [9]. These dissimilarities in crystal lattice arrangement and chemical compositions significantly impact the lattice dynamics of these alloys. The face-centered Fe-rich $Pm\overline{3}m$-Fe₃Pt has a similar intermetallic arrangement as the Cu₃Ag-ordered crystal structure. Temperature-based X-ray diffraction and transmission electron microscopy studies demonstrated that the $Pm\overline{3}m$-Fe₃Pt alloy fully crystallizes at annealing temperatures above 800 °C [10,11]. The grain size and lattice parameter increase until this temperature and remain constant thereafter, signifying that crystallization is fully converged and lattice has reached stability. Moreover, the Mössbauer spectrometry and magnetic characterization results showed that the structure conforms to a ferromagnetic state at temperatures below 120 K and paramagnetic state at 300 K and above. The L1₂ cubic Pt-rich $Pm\overline{3}m$-FePt₃ is an intermediate alloy that occurs below 300 °C during the formation of the L1₀ FePt [4]. Further structural arrangements were discussed in detail in our previous communication [3]. Moreover, recently revised phase diagram studies have revealed the existence of other novel ordered FePt₂ and Fe₂Pt alloys [12]. Yu et al. have since performed computational simulations on these alloys to investigate their various thermodynamic, mechanical, and dynamical stabilities [13,14]. For the FePt₂ composition, they reported on five different space groups, namely: $I4/mmm$, $P4/nmm$, $Immm$, $Cmcm$, and $P63/mmc$, which were predicted to be thermodynamically and mechanically stable, with the $I4/mmm$ being the most thermodynamically stable [13]. Furthermore, four space groups of Fe₂Pt, namely: $Cmcm$, $Immm$, $I4/mmm$, and $P\overline{3}m1$ were also reported to be low-energy ferromagnetic stable structures [14].

Phonon dispersion spectra measurements of Fe-Pt alloys to determine their dynamical properties have previously been reported using both experimental and density functional theory (DFT)-based first-principles studies. Pierron-Bohnes et al. measured the vibrational modes of the conventional unit cell of the ordered L1₀ $P4/mmm$-FePt structure at 300 K using the inelastic neutron scattering method [15]. They observed that this alloy is thermodynamically stable since the dispersion relations curves displayed only positive modes of vibrations. Earlier, Noda et al. also investigated and compared the dispersion spectra between the ferromagnetic $Pm\overline{3}m$-Fe₃Pt and paramagnetic $Pm\overline{3}m$-FePt₃ cubic L1₂ alloys using the inelastic neutron scattering technique at room temperature [16]. They observed that the acoustic modes for both alloys are similar, particularly in the lower-energy region, mainly because their lattice constants differ by only 3%. It has been also determined that the dispersion curves in Fe₃Pt and FePt₃ are influenced by the force constants associated with their respective nearest neighbors, namely Fe-Fe and Pt-Pt; thus, the nearest neighbor pairs have dominant roles in lattice dynamics. Sternik et al. corroborated the experimental measurements by conducting first-principles computations on the phonon dispersion curves of the $2 \times 2 \times 2$ primitive supercells of $P4/mmm$-FePt, $Pm\overline{3}m$-Fe₃Pt, and $Pm\overline{3}m$-FePt₃ alloys using the direct method as embedded in the PHONON code [17]. They reported that the $P4/mmm$-FePt and $Pm\overline{3}m$-FePt₃ alloys show no imaginary modes along high symmetry directions of the Brillouin zone, while there are imaginary frequencies for the transversal acoustic mode on the $Pm\overline{3}m$-Fe₃Pt alloy. Furthermore, their investigation into the impact of magnetic ordering on the dispersion relations of $Pm\overline{3}m$-FePt₃ revealed that the frequencies of the antiferromagnetic orientation slightly surpass those of the ferromagnetic orientation. Nevertheless, the dispersion curves exhibit a remarkable similarity.

Investigation of mechanical properties such as elasticity, hardness, shear resistance, ductility, and anisotropy is a crucial prerequisite in solid-state materials before their design and development. DFT calculations of elastic constants have been performed for various binary and ternary alloys and were reported to reveal valuable insights at both ambient and elevated conditions. Phasha et al. investigated the structural and mechanical properties

of the ordered Mg-Li binary alloys to predict their phase stability [18]. Their findings revealed that there is a correlation between the heats of formation and elastic constants in terms of predicting stability. Phases with negative heats of formation tend to satisfy the Born necessary stability conditions and have a positive tetragonal shear modulus $C'$. Recent DFT studies on various alloys and other compounds have also corroborated these pioneering conclusions. Botha et al. investigated the relationship between the mechanical, dynamical, and thermodynamic properties of Pt-Pd alloys by calculating their elastic con- stants, phonon dispersion spectra, and heats of formation, respectively [19]. Their results indicated that energetically favorable, i.e., with negative heats of formation, compositions satisfy Born stability conditions (mechanical stability) and depict only positive modes of vibrations in the phonon dispersion spectra (dynamical stability). Similar studies were performed on Co-alloyed MnPt alloys, revealing that energetically favorable compositions are mechanically stable [20,21]. It was further revealed that the Debye temperature of $CsGaSb_{2}$ calculated from the single-crystal elastic constants yields approximately a sim- ilar value to the one calculated from the phonon density of states, confirming a robust link between mechanical and dynamical properties. Moreover, the polycrystalline bulk modulus calculated from the elastic constants exhibited exceptional alignment with values derived from alternative equations of state [21]. DFT calculations on the elastic constants of Fe-Pt alloys $(P 4 / mmm-FePt, Pm \overline{3} m-Fe_{3} Pt$ , and $Pm \overline{3} m-FePt_{3})$ have also been previously performed [11]. It was reported that $Pm \overline{3} m-Fe_{3} Pt$ is mechanically unstable due to negative $C'$ and $C_{44}$ values, while others satisfied the Born stability conditions. On the contrary, earlier results revealed mechanical stability [7,22].

Despite the significant experimental and computational advances made in these al- loys, there remains a notable gap regarding the origins of lattice dynamics and elastic behavior for optimizing their functionality and ensuring their long-term stability. More- over, little work has been completed on the $I 4 / mmm-Fe_{3} Pt$ alloy, prompting the need to understand and compare the mechanical, dynamical, and thermodynamical proper- ties across the entire spectrum of existing Fe-Pt alloys. Thus, the current communication will put special emphasis on this alloy. These properties are critical in designing and developing new composition-dependent magnetic materials. Additionally, understanding these properties provides valuable insights in predicting the stability of these materialswhen subjected to industrial conditions. Building from our previous communication [3] where the structural, magnetic, and electronic properties of $P 4 / mmm-FePt, I 4 / mmm-Fe_{3} Pt$ , $Pm \overline{3} m-Fe_{3} Pt$ , and $Pm \overline{3} m-FePt_{3}$ were reported, the current study presents density functional theory (DFT)-based first-principles computations to establish a corroboration between the mechanical, dynamical, and thermodynamic properties of the same alloys at ambient conditions. Elemental contributions of Fe and Pt atoms on the phonon dispersion spectra are also determined by the partial phonon density of states. Moreover, this work is an extrapolation of the existing theoretical and inelastic neutron scattering measurements of magnetic, mechanical and lattice dynamical properties of Fe-Pt alloys which have re- ported TA-mode softening on $Pm \overline{3} m-Fe_{3} Pt$ [11,17,23,24]. We found that the equiatomic P4/mmm-FePt alloy exhibits dynamical stability, as evidenced by only positive vibrations in the phonon dispersion spectrum. Moreover, the less-studied $I 4 / mmm-Fe_{3} Pt$ alloy shows comparable mechanical stability, ductility, anisotropy, and Debye temperature with the other alloys. Our findings contribute to the growing body of knowledge in the field of alloy research and provide a solid foundation for future investigations. By unravelling the complexities of these ordered alloys, we can unlock their full potential and harness their properties for technological advancements.

## 2. Computational Procedure
All calculations were performed using the Cambridge Serial Total Energy Package(CASTEP) [25] simulation code which is incorporated in with the Materials Studio 2020 version suite. CASTEP is a widely used code in the field of computational chemistry and materials science due to its ability to accurately predict the properties and behaviors of

materials at the atomic level. Its key strength lies in its ability to perform first-principles calculations based on density functional theory, which accurately describes the electronic structure of materials without the need for empirical parameters, thus allowing the study of properties such as elastic constants, phonon spectra, and thermodynamic properties. However, some calculations are time-consuming and computationally expensive, limiting the size of systems that can be studied and the timescales that can be simulated. We carried out collinear spin polarization density functional theory (DFT) computations within the generalized gradient approximation (GGA) utilizing the Perdew, Burke, and Ernzerhof (PBE) functional [26]. All structures were initially relaxed by performing a full geometry optimization while maintaining a fixed basis quality and allowing cell volume to change. The Coulomb interactions between the valence electrons of iron (Fe: $3d^6 4s^2$) and platinum (Pt: $4f^{14} 5d^9 6s^1$) atoms, and their respective pseudo-ionic cores, were accurately modelled using on-the-fly generated (OTFG) ultrasoft pseudopotentials. This approach enables calculations to be conducted with reduced energy cut-offs and ensures that the generated potentials are steady across solid-state and pseudo-atom calculations. Furthermore, it enhances the accurateness and dependability of the results by utilizing the same exchange-correlation functional throughout. A customized energy cut-off of 350 eV was adequate to minimize the total energy of the bulk structure until the difference between two successive low-memory Broyden–Fletcher–Goldfarb–Shanno (BFGS) iterations was within 0.001 eV. The low-memory Broyden–Fletcher–Goldfarb–Shanno (LBFGS) [27] algorithm was preferred due to its ability to accelerate geometry optimization and accuracy for large systems [28]. To sample the wave functions, we employed the Monkhorst-Pack grid parameters of $9 \times 9 \times 7, 4 \times 4 \times 4, 6 \times 6 \times 6$, and $8 \times 8 \times 8$ for $P4/mmm$-FePt, $I4/mmm$-Fe₃Pt, $Pm\overline{3}m$-FePt₃, and $Pm\overline{3}m$-Fe₃Pt, respectively. The calculations for all structures were conducted assuming the ferromagnetic (FM) arrangement of the local magnetic moments. Moreover, for the tetragonal $P4/mmm$-FePt and $I4/mmm$-Fe₃Pt, we computed the primitive tetragonal cell as opposed to the conventional cell due to minimal computational resources. As a result, $I4/mmm$-Fe₃Pt with lattice parameters $a \neq c$ was computed as $I4/mmm$-Fe₃Pt with $a = c$. The phonon dispersion spectra along high symmetry lines and the accompanying phonon density of states were calculated via the finite displacement method which was proven to be highly effective for metallic systems [29,30]. The finite displacement technique relies on numerically differentiating forces acting on atoms, which are calculated for multiple unit cells with atomic displacements. Phonon density of states also serves as a requirement for the computation of thermodynamic properties, which permits assignment of temperature factors during analysis. Lastly, the monocrystalline elastic constants were calculated using the stress–strain approach with a maximum strain amplitude of 0.003. The additional calculation criteria for elastic constants involved sustaining total energy of convergence below $2.0 \times 10^{-6}\ \text{eV/atom}$, making sure that the Hellman-Feynman force is maintained under $0.006\ \text{eV/\AA}$, and keeping the ionic displacement within $2.0 \times 10^{-4}$.

## 3. Results and Discussion
### 3.1. Mechanical Properties

Before determining the mechanical and dynamical properties of Fe-Pt alloys, structural relaxation was performed to obtain ground-state lattice parameters. To validate the approach utilized, the calculated structural lattice parameters were compared with the existing experimental data. The purpose of this analysis is to ensure the accuracy and reliability of our results. The current GGA-calculated lattice parameters exhibit an impressive agreement of over 98% with the previously reported data, thereby demonstrating the robustness of the approach employed.

Table 1 presents the calculated lattice constants, elastic constants, moduli, Pugh ratio, anisotropy factor, Poisson ratio, Vickers hardness, and Debye temperature for the Fe-Pt alloys. Calculation of elastic constants is crucial in characterizing the mechanical behavior of materials and response to externally induced stress. The Taylor expansion of the total

energy of a strained system [31,32] (see Equation (1)) was used to calculate the elastic constants (Cᵢⱼ).

$$
U(V, \varepsilon)=U(V_{0}, 0)+V_{0}\left[\sum_{i} \tau_{i} \varepsilon_{i} \tilde{\zeta}_{i}+\frac{1}{2} \sum_{i j} C_{i j} \varepsilon_{i} \tilde{\zeta}_{i} \varepsilon_{j} \tilde{\zeta}_{j}\right],
\tag{1}
$$

where $U(V_{0},0)$ is the energy of the unstrained system with equilibrium volume $V_{0}$; $\tau_{i}$ and $\tilde{\zeta}_{i}$ are elements in the stress tensor and a factor taking care of the Voigt index, respectively. Cubic and tetragonal crystal systems contain three ($c_{11}, c_{12}, c_{44}$) and six ($c_{11}, c_{33}, c_{44}, c_{66}, c_{12,}c_{13}$) independent elastic constants, respectively. Except for $C_{12}$ in $P4/mmm$-FePt, the obtained monocrystalline elastic constants are in agreement with the previous semi-empirical Monte Carlo results obtained using the modified embedded atom method (MEAM) and angular dependent analytic bond-order potential (ABOP) formalism [6,22], further affirming the accuracy of the approach employed. Moreover, our $C_{12}$ value is in better agreement with the DFT value of 94 GPa reported by Zotov and Ludwig [11]. For cubic crystals ($Pm\overline{3}m$-Fe₃Pt and $Pm\overline{3}m$-FePt₃) to be deemed mechanically stable, the mandatory Born stability criterion in Equation (2) must be fulfilled [33,34].

$$
C_{11}+2 C_{12}>0, \quad C_{11}>\left|C_{12}\right| \text { and } C_{44}>0
\tag{2}
$$

Table 1. Calculated lattice constants, elastic constants, and moduli for the four ordered bimetallic Fe-Pt alloys. Available experimental data are provided in parentheses.

<table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>$Pm\overline{3}m$-Fe₃Pt</th>
    <th>$I4/mmm$-Fe₃Pt</th>
    <th>$P4/mmm$-FePt</th>
    <th>$Pm\overline{3}m$-FePt₃</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="5">Lattice Parameters (Å)</td>
  </tr>
  <tr>
    <td>a (Å)</td>
    <td>3.735 (3.72) [10]</td>
    <td>5.276</td>
    <td>2.725 (2.728)</td>
    <td>3.914 (3.87) [22]</td>
  </tr>
  <tr>
    <td>c (Å)</td>
    <td>-</td>
    <td>-</td>
    <td>3.784 (3.85) [22]</td>
    <td>-</td>
  </tr>
  <tr>
    <td colspan="5">Bond Length (Å) [4]</td>
  </tr>
  <tr>
    <td>Fe-Pt</td>
    <td>2.641</td>
    <td>2.638</td>
    <td>2.700 (2.667)</td>
    <td>2.768</td>
  </tr>
  <tr>
    <td>Fe-Fe</td>
    <td>2.641</td>
    <td>2.638</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Pt-Pt</td>
    <td>-</td>
    <td></td>
    <td>-</td>
    <td>2.768</td>
  </tr>
  <tr>
    <td colspan="5">Elastic Constants (GPa) [22]</td>
  </tr>
  <tr>
    <td>$C_{11}$</td>
    <td>206.344 (238.8)</td>
    <td>259.280</td>
    <td>346.778 (304.2)</td>
    <td>301.055 (325.8)</td>
  </tr>
  <tr>
    <td>$C_{33}$</td>
    <td></td>
    <td>209.513</td>
    <td>292.106 (242.0)</td>
    <td></td>
  </tr>
  <tr>
    <td>$C_{44}$</td>
    <td>85.957 (90.46)</td>
    <td>68.757</td>
    <td>113.855 (106.5)</td>
    <td>105.108 (90.4)</td>
  </tr>
  <tr>
    <td>$C_{66}$</td>
    <td></td>
    <td>35.522</td>
    <td>48.38190 (40.8)</td>
    <td></td>
  </tr>
  <tr>
    <td>$C_{12}$</td>
    <td>170.625 (184.1)</td>
    <td>90.790</td>
    <td>73.457 (222.6)</td>
    <td>183.094 (230.1)</td>
  </tr>
  <tr>
    <td>$C_{13}$</td>
    <td></td>
    <td>152.871</td>
    <td>161.090 (197.3)</td>
    <td></td>
  </tr>
  <tr>
    <td>$C'$</td>
    <td>17.859</td>
    <td>84.245</td>
    <td>136.66</td>
    <td>58.981</td>
  </tr>
  <tr>
    <td>$B$</td>
    <td>182.531</td>
    <td>168.908</td>
    <td>197.102</td>
    <td>222.415</td>
  </tr>
  <tr>
    <td>$G$</td>
    <td>46.379</td>
    <td>51.670</td>
    <td>87.423</td>
    <td>83.360</td>
  </tr>
  <tr>
    <td>$\lambda$</td>
    <td>151.612</td>
    <td>134.461</td>
    <td>138.820</td>
    <td>166.842</td>
  </tr>
  <tr>
    <td>$E$</td>
    <td>128.274</td>
    <td>140.667</td>
    <td>228.488</td>
    <td>222.306</td>
  </tr>
  <tr>
    <td>$\sigma$</td>
    <td>0.383</td>
    <td>0.361</td>
    <td>0.307</td>
    <td>0.333</td>
  </tr>
  <tr>
    <td>$A^{U}$</td>
    <td>1.624</td>
    <td>1.082</td>
    <td>0.891</td>
    <td>0.412</td>
  </tr>
  <tr>
    <td>$\theta_{T}$</td>
    <td>276.697</td>
    <td>298.023</td>
    <td>330.790</td>
    <td>291.904</td>
  </tr>
  <tr>
    <td>$H$</td>
    <td>2.931</td>
    <td>3.907</td>
    <td>8.650</td>
    <td>6.906</td>
  </tr>
  <tr>
    <td>$G/B$</td>
    <td>0.254</td>
    <td>0.306</td>
    <td>0.444</td>
    <td>0.375</td>
  </tr>
</tbody>
</table>

The mechanical stability conditions for tetragonal systems ($P4/mmm$-FePt and $I4/mmm$-Fe₃Pt) are delineated based on Equation (3) [35]. We note that the elastic constants for both the cubic and tetragonal systems are satisfied, demonstrating mechanical stability, which

corroborates the thermodynamic stability reported previously [3]. Additionally, we have noted a positive $C'$ value, which further confirms the mechanical stability of the systems.

$$
\begin{aligned}
& C_{11}-C_{12}>0 ; \quad C_{11}+C_{33}-2 C_{13}>0 ; \\
& C_{i i}>0(i=1,3,4) ; \quad 2 C_{11}+C_{33}+2 C_{12}+4 C_{13}>0
\end{aligned}
\tag{3}
$$

The elastic constants of the tetragonal systems can further be analyzed by examining their similarities and discrepancies. Significant differences are observed between the calculated $C_{i j}$ values, suggesting that the tetragonal alloys are highly anisotropic. Particularly, $C_{11}$ and $C_{33}$ are significantly higher than $C_{44}$ and $C_{66}$, indicating greater resistance to unidirectional compression compared to shear. Furthermore, there exists a substantial difference between the following pairs of $C_{i j}$ s, $C_{11}$ and $C_{33} ; C_{44}$ and $C_{66} ; C_{12}$ and $C_{13}$, which has an impact on the behavior of the material. $C_{11}$ represents the stiffness of the material in the direction perpendicular to the crystallographic planes, while $C_{33}$ represents the stiffness parallel to the crystallographic planes, namely [100]; [010]; and [001]. $C_{11}$ values are significantly higher than those of $C_{33}$, indicating greater resistance to compression in the $a$-axis in comparison to the $c$-axis or greater linear compressibility along the $c$-axis compared to the $a$-axis when the material is subjected to external forces. Thus, the interatomic chemical bonds within the (001) plane are more robust compared to the bonding along the crystal direction [001]. The relationship $C_{44}>C_{66}$, indicates that shear deformation is more prominent when a net stress is imposed along the [100] crystallographic direction of the (010) crystallographic plane, as opposed to when the same stresses are exerted in the [100] direction within the plane (001). This indicates that the alloys exhibit anisotropic behavior with greater resistance to shear deformation in one direction compared to another. Moreover, the significant difference between $C_{12}$ and $C_{13}$ demonstrates that when stress is imposed along the $a$-axis, the subsequent strain will be more pronounced along the $a$-axis than the $c$-axis. This further highlights the anisotropic response of these alloys under stress, as evidenced by the high $A^{U}$ values. When assessing the level of anisotropy, we have chosen to utilize the universal anisotropy index $A^{U}$ in Equation (4) as postulated by Ranganathan and Stoja-Starzewski [36]. This index is particularly suitable as it considers both shear and bulk contributions, acknowledging the inherent anisotropy present in all single crystals. The magnitude of the deviation of $A^{U}$ from zero is the measure of the degree of anisotropy exhibited by a single crystal, with a value of zero indicating a locally isotropic crystal.

$$
A^{U}=5 \frac{G^{V}}{G^{R}}+\frac{B^{V}}{B^{R}}-6
\tag{4}
$$

where $G^{V}, G^{R}, B^{V}$, and $B^{R}$ are the shear and bulk moduli Voigt and Reuss estimates, respectively. We observe that $A^{U}$ decreases with Fe content, thus $P m \overline{3} m-\mathrm{Fe}_{3} \mathrm{Pt}$ and $I 4 / \mathrm{mmm}$ $\mathrm{Fe}_{3} \mathrm{Pt}$ are highly anisotropic over $P 4 / m m m-\mathrm{FePt}$ and $P m \overline{3} m-\mathrm{FeP}_{3}$, respectively.

The calculation of independent elastic constants allowed us to estimate the macroscopic elastic bulk (B), shear (G), and Young's (E) moduli utilizing the Voigt [37] and Reuss [38] estimates. These estimates establish simple and linear relationships between the isotropic bulk and shear moduli of the polycrystalline material. Additionally, Hill demonstrated that the Voigt and Reuss expressions serve as upper and lower bounds, respectively, and proposed an arithmetic average modulus value [39]. The bulk modulus signifies the material's ability to withstand compression under applied hydrostatic pressure, while the shear modulus indicates its resistance to deformation from external forces at a constant volume. Young's modulus, on the other hand, measures the material's stiffness by determining the ratio of vertical linear stress to linear strain.

$$
G_{V}=\left(\frac{C_{11}-C_{12}+3 C_{44}}{5}\right) ; G_{R}=\left(\frac{C_{44}\left(C_{11}-C_{12}\right)}{4 C_{44}+3\left(C_{11}-C_{12}\right)}\right) ; G_{H}=\left(\frac{G_{V}+G_{R}}{2}\right)
\tag{5}
$$

$$
\begin{aligned}
B_{V} & =\frac{1}{9}\left[2\left(C_{11}+C_{12}\right)+C_{33}+4 C_{13}\right] ; B_{R}=\frac{C^{2}}{M} ; C^{2}=\left(C_{11}+C_{12}\right) C_{33}-2 C_{13}^{1} ; \\
B_{H} & =\left(\frac{B_{V}+B_{R}}{2}\right)
\end{aligned}
\tag{6}
$$

$$
C^{\prime}=\left(\frac{C_{11}-C_{12}}{2}\right)
\tag{7}
$$

The current DFT calculations revealed that Fe-Pt alloys have intrinsic mechanical hardness, stiffness, and shear resistance, i.e., are highly resistant to changes from external mechanical stress due to relatively large magnitudes of $B$, $G$, and $E$. The shear modulus is less than the bulk in all the alloys, suggesting they exhibit greater resistance to volumetric change than shear deformation, and that the shear modulus is the parameter limiting stability. $P m \overline{3} m-\mathrm{FePt}_{3}$ possesses the highest bulk modulus value, suggesting the greatest mechanical hardness and compression resistance over $P 4 / m m m$-FePt, $P m \overline{3} m-\mathrm{Fe}_{3} \mathrm{Pt}$, and $I 4 / m m m-\mathrm{Fe}_{3} \mathrm{Pt}$, respectively. This is consistent with a previous DFT study on Pt/Pd alloys, which showed that the bulk modulus is higher in Pt-rich compositions [19]. The $P m \overline{3} m$ $\mathrm{Fe}_{3} \mathrm{Pt}$ system possesses the lowest shear modulus value of $46.379 \mathrm{GPa}$, indicating the greatest susceptibility to shear deformation compared to $I 4 / m m m-\mathrm{Fe}_{3} \mathrm{Pt}, P m \overline{3} m-\mathrm{FePt}_{3}$, and $P 4 / m m m$-FePt, respectively. The Young's modulus suggests that $P 4 / m m m$-FePt adopts highest stiffness over, $P m \overline{3} m-\mathrm{FePt}_{3}, P m \overline{3} m-\mathrm{Fe}_{3} \mathrm{Pt}$, and $I 4 / m m m-\mathrm{Fe}_{3} \mathrm{Pt}$, respectively.

To assess ductility and brittles, we computed the Pugh shear to the bulk modulus $(K)$ [40] and Poisson $(v)$ [41] ration of solid-state materials. Pugh postulated that a material is considered ductile if $K$ is less than the critical value 0.5 and brittle when greater than 0.5 . We noticed that $K$ values are less than 0.5 for all Fe-Pt alloys, demonstrating ductility. Ductile materials exhibit greater resistance to thermal shock and are easier to machine. Moreover, we noted that the Fe-rich $P m \overline{3} m-\mathrm{Fe}_{3} \mathrm{Pt}$ and $I 4 / m m m-\mathrm{Fe}_{3} \mathrm{Pt}$ systems possess lower $K$ values, due to their low shear modulus. The Poisson's ratio associated with volume changes in directions perpendicular to the applied tension during deformation typically ranges from -1 to 0.5 . An indication of ductility is present when the value exceeds 0.26 , otherwise the material is considered brittle. The Poisson ratio for these alloys is greater than 0.26 , further confirming ductility. Interestingly, the less-studied $I 4 / m m m-\mathrm{Fe}_{3} \mathrm{Pt}$ shows excellent ductility over $P m \overline{3} m-\mathrm{FePt}_{3}$ and $P 4 / m m m$-FePt, respectively. Furthermore, the Poisson ratio was used to analyze bonding type in Fe-Pt alloys. Crystals are considered covalent if $v$ is approximately 0.1 , ionic if $v=0.25$, and metallic if $v>0.33$ [42,43]. We note that $v$ values are greater than 0.33 for $P m \overline{3} m-\mathrm{Fe}_{3} \mathrm{Pt}, I 4 / m m m-\mathrm{Fe}_{3} \mathrm{Pt}$, and $P m \overline{3} m-\mathrm{FePt}_{3}$, implying metallic bonding. On the other hand, $P 4 / m m m$-FePt shows a ratio less than 0.33 but greater than 0.25 , indicating half-metallic behavior. This is in good agreement with the density of states predictions reported in our previous communication [3]. To gain insight into the thermal properties of Fe-Pt alloys, we determined the Debye temperature $\left(\theta_{D}\right)$. This property represents the point at which the atoms within a solid material cease to vibrate independently, but instead begin to move in a synchronized manner. It signifies the highest normal mode of vibration and serves to establish a correlation between elastic constants and phonon dispersions, specific heat, thermal expansion, and thermal conductivity. Equation (8) was utilized in the computation of the Debye temperature [44].

$$
\theta_{D}=\frac{\hbar v}{k_{B}}\left(6 \pi^{2} n\right)^{1 / 3},
\tag{8}
$$

where $n, v$, and $k_{B}$ are the atom concentration, phase velocity, and Boltzmann constant, respectively. Our DFT calculations show relatively huge magnitudes of Debye temperature (~300 K), indicating high vibrational modes in the phonon dispersion spectra (see Figure 1) and consequently high thermal conductivity. Laureti et al. employed the Correlated Debye Model (CDMT) to measure the Debye temperature of $P 4 / m m m$-FePt and reported $\theta_{D}=340 \mathrm{~K}$ [4], which is consistent with our results (330.79 K). Materials with higher Debye temperatures also have stiffer and more rigid lattices, while those with lower Debye temperatures exhibit softer and more flexible structures [45,46]. To estimate the Vickers

hardness of Fe-Pt alloys, we employed the microscopic bond resistance model proposed by Tian et al. [47] as shown in Equation (9).

$$
H_{V}=0.92 k^{1.137} G^{0.708},
\tag{9}
$$

where $k$ is the $G/B$ ratio and $G$ is the shear modulus. Our findings show that the metallic Fe-Pt alloys relatively show low hardness. In principle, this is expected for ductile materials with low (<0.5) $G/B$ values, as proposed by Chen et al. [48].

![](./images/1027847732057866248_3.jpg)

Figure 1. Phonon dispersion curves for (a) $Fm\overline{3}m$-Fe₃Pt, (b) $4mmm$-Fe₃Pt, (c) $P4/mmm$-FePt, and (d) $Pm\overline{3}m$-FePt₃ alloys.

### 3.2. Phonon Dispersion Curves

The phonon dispersion relations along high symmetry lines in the Brillouin zone were calculated to determine the lattice dynamic stability of Fe-Pt alloys and are presented in Figure 1. Phonon dispersion frequencies are calculated as the analysis of forces associated with a systematic set of atomic displacements from equilibrium positions in a crystal system. Materials are considered stable if there are no negative frequencies (soft modes) along high symmetry lines. We observe that the ordered L1₀ $P4/mmm$-FePt displays only positive phonon vibrational modes along the high symmetry directions, indicating that all the eigenvalues are real and the alloy is dynamically stable. This finding aligns well with previous theoretical and experimental research [15,17,49]. The other compositions, in particular $Pm\overline{3}m$-FePt₃, show imaginary frequencies of vibration along high symmetry lines in the spectrum, reflecting deviation dynamical instability and possible structural deformation which results in lowering of the symmetry [50]. The anomalous behavior shows that the frequencies of vibration decrease with the increasing wave vector as opposed to increasing. This may be attributed to the presence of complex interactions between the Fe and Pt atoms in the lattice, leading to the formation of localized vibrations that propagate through the material in a non-traditional manner. Dynamical instability is not pronounced for $Pm\overline{3}m$-Fe₃Pt and $I4/mmm$-Fe₃Pt since the negative vibrations are not along the center of the Brillouin zone G.

The modes of vibration for $Pm\overline{3}m$-Fe₃Pt and $I4/mmm$-Fe₃Pt as depicted in Figure 1a,b share a related frequency range and similarities along G, which can be attributed to their identical chemical composition and stoichiometry. Moreover, we note that the separation

between the acoustic and optical modes is not enough to create a gap in the dispersion relations of all the alloys, suggesting seamless continuous energy transfer between the phonon modes. The disparities in mass among the alloys are evident through the observation that the frequencies of vibrations (optical modes) are higher in Fe-rich (with smaller mass) alloys and lower in Pt-rich (with larger mass) alloys.

### 3.3. Phonon Density of States

To analyze the distinctive elemental vibrational contributions, we conducted calculations of the phonon density of states (DOS) as illustrated in Figure 2. The spectra can be categorized into two frequency regions: one where Fe vibrations predominate and another where Pt vibrations are more prominent. In Fe-rich compositions, Fe vibrations are prevalent at higher frequencies, whereas Pt-rich compositions exhibit dominance of Pt vibrations. Additionally, a significant level of anisotropy in lattice dynamics is apparent in all structures, particularly in $P4/mmm$-FePt (Figure 2c). The lowest frequency band (1.9–3.6 THz) comprises vibrations of the heavier platinum atoms, while frequencies above 4 THz are attributed to Fe vibrations. These findings align well with similar DFT calculations reported in previous studies [17,50]. In the Fe-rich $Pm\overline{3}m$-Fe₃Pt and $I4/mm$-Fe₃Pt compositions, Pt movement prevails up to 4 THz with minimal contribution from Fe, indicating that heavier Pt movement is responsible for the presence of imaginary soft modes leading to dynamical instability. Conversely, in the $Pm\overline{3}m$-FePt₃ composition, Fe vibrations dominate in the −5 to 2 THz range, while Pt is more prominent in the 4 to 6 THz region. Therefore, the negative frequencies observed in the phonon dispersion curves of this alloy stem from the movement of multiple Fe atoms. Moreover, it should be noted that the elemental partial DOSs of Fe and Pt were sampled for only one atom each. Hence, there are significant differences between the sum (red) and atomic plots (blue and green) in the non-equiatomic compositions since other atoms are not included.

![](./images/1027847732057866248_4.jpg)

Figure 2. Calculated phonon density of states (a) $Pm\overline{3}m$-Fe₃Pt, (b) $I4/mmm$-Fe₃Pt, (c) $P4/mmm$-FePt, and (d) $Pm\overline{3}m$-FePt₃ alloys.

### 3.4. Thermodynamic Properties

Thermodynamic (temperature-dependent) quantities have been evaluated from the phonon density of states (DOS) in the temperature range of 0 to 1000 K based on the relations developed by Baroni et al. as listed in Table 2 [51]. All quantities were calculated at ground state, that is, geometry optimization was fully converged and all the phonon eigenfrequencies were real and non-negative.

<table>
<caption>Table 2. Formulae for thermodynamic quantities.</caption>
<tr>
<td>$$E(T) = E_{tot} + E_{zp} + \int \frac{\hbar\omega}{e^{\left(\frac{\hbar\omega}{kT}\right)}-1}F(\omega)d\omega,$$</td>
<td>Enthalpy</td>
</tr>
<tr>
<td>$$F(T) = E_{tot} + E_{zp} + kT \int F(\omega)\left[1 - e^{\left(-\frac{\hbar\omega}{kT}\right)}\right]d\omega$$</td>
<td>Free energy</td>
</tr>
<tr>
<td>$$S(T) = k\left\{\int \frac{\frac{\hbar\omega}{kT}}{e^{\left(\frac{\hbar\omega}{kT}\right)}-1}F(\omega)d\omega - \int F(\omega)\ln\left[1 - e^{\left(\frac{\hbar\omega}{kT}\right)}b\right]d\omega\right\}$$</td>
<td>Entropy</td>
</tr>
<tr>
<td>$$C_{v}(T) = k \int \frac{\left(\frac{\hbar\omega}{kT}\right)^2 e^{\left(\frac{\hbar\omega}{kT}\right)}}{\left[e^{\left(\frac{\hbar\omega}{kT}\right)}-1\right]^2}F(\omega)d\omega$$</td>
<td>Heat capacity</td>
</tr>
<tr>
<td>$$C_{v}^{D} = 9Nk\left(\frac{T}{\theta_{D}}\right)^3 \int_{0}^{\theta_{D}/T} \frac{x^4 e^x}{(e^x-1)^2}dx$$</td>
<td>Debye temperature</td>
</tr>
</table>

where $E_{zp}, k, \hbar, F(\omega), \theta_{D}$, and $N$ are zero-point vibrational energy, Boltzmann constant, Planck constant, phonon density of states, Debye temperature, and number of atoms per cell, respectively.

Enthalpy, free energy, and entropy are fundamental thermodynamic properties that govern the behavior of solid-state materials. In the context of solid-state materials, enthalpy plays a crucial role in understanding phase transitions, such as melting and crystallization. For example, the enthalpy change associated with the melting of a solid reflects the energy required to overcome intermolecular forces and disrupt the crystalline structure, leading to a transition from a solid to a liquid state. Free energy is a key parameter in predicting the stability and equilibrium of different crystal structures. By comparing the free energy of different crystal phases, we can determine the phase that is thermodynamically favored under specific conditions. Entropy is closely related to the organization of atoms and molecules in a crystal lattice. Higher entropy is associated with increased disorder and greater freedom of movement for particles, whereas lower entropy corresponds to a more ordered and structured arrangement which is associated with favorable thermal conductivity and resistance to thermal expansion and deformation.

These three thermodynamic potentials as a function of temperature are plotted in Figure 3. From our graphical representations, we observed that entropy and enthalpy rise with temperature, while the free energy decreases. The $I4/mmm$-$Fe_3Pt$ alloy shows the largest entropy values, alluding to the high mobility of atoms within the lattice structure, while the $P4/mmm$-FePt has the lowest, suggesting a more compact structural arrangement and thermal stability and conductivity. This is consistent with the phonon dispersion spectra predictions where $P4/mmm$-FePt showed dynamical stability. The free energies are negative and continue to decrease with temperature, implying thermodynamic stability [49], which corroborates the heats of formation in the previous communication [3]. Figure 4a shows the variation in isobaric heat capacity ($C_v$) as a function of temperature (0–1000 K). Heat capacities are critical in determining the thermal behavior of solid-state materials and are strongly dependent on intermolecular bonds. Materials with strong intermolecular bonds tend to have higher heat capacities as more energy is required to disrupt these bonds and increase the temperature. As the temperature increases, the heat capacities of Fe-Pt alloys show uneven characteristics. At temperatures below 200 K, $C_v$ increases exponentially and gradually scales off toward the Dulong–Petit boundary at higher temperatures. This behavior is common in most solid-state materials [19,21,52]. In the temperature range, $I4/mmm$-$Fe_3Pt$ (~46 cal/cell·K) shows the highest $C_v$ value, followed by $Fm\overline{3}m$-$Fe_3Pt$ (~23 cal/cell·K), $Fm\overline{3}m$-$FePt_3$ (~17 cal/cell·K), and $P4/mmm$-FePt (~12 cal/cell·K), respectively. Interestingly, in temperatures below 80 K, the heat capacities are consistent with the

bond length (see Table 1). An alloy with the shortest bond length ($I4/mmm$-Fe₃Pt) exhibits the highest $C_v$ value, while an alloy with the longest bond length ($P4/mmm$-FePt) has the lowest value, further confirming a compact lattice structure on the latter.

![](./images/1027847732057866248_5.jpg)

Figure 3. Thermodynamic properties of Fe-Pt alloys. (a) $Pm\overline{3}m$-Fe₃Pt (b) $I4/mmm$-Fe₃Pt (c) $P4/mmm$-FePt (d) $Pm\overline{3}m$-FePt₃.

![](./images/1027847732057866248_6.jpg)

Figure 4. (a) Isochoric heat capacities and (b) Debye temperature vs. temperature for Fe-Pt alloys.

The variation in the Debye temperature ($\theta_D$) as a function of temperature is shown in Figure 4b. Our results show a very strong linear increment relation between $\theta_D$ and $T$ for $Pm\overline{3}m$-FePt₃ and a moderate linear increase for $I4/mmm$-Fe₃Pt and $Pm\overline{3}m$-Fe₃Pt. Interestingly, $P4/mmm$-FePt shows a nearly constant $\theta_D$ vs. $T$ relationship with a small standard deviation within 14, suggesting that the modes of vibration are compact and thermal stability is achieved for $P4/mmm$-FePt, which is in good agreement with the phonon dispersion spectra and entropy predictions. The Debye temperature decreases with Pt content, which is in good agreement with related DFT studies [19,53]. Moreover, $\theta_D$ of $Pm\overline{3}m$-FePt₃ is highly affected by temperature, indicating the increase in atomic mobility and vibrations, which is consistent with the negative phonon modes of vibration.

### 4. Conclusions
The current study has successfully conducted ab initio simulations on the bimetallic Fe-Pt alloys to gain insights into the intrinsic factors underlying their mechanical, dynami- cal, and thermodynamic behavior, as well as to derive their stability trends. Moreover, we have established a link between the lattice dynamic and thermodynamic properties. All Fe-Pt alloys were predicted to be mechanically stable since they satisfied the Born stability conditions for cubic and tetragonal crystal lattices. Moreover, Fe-Pt alloys are characterized by the presence of sizeable anisotropy rising from the discrepancies in elastic constants and deviation of the universal anisotropy index from zero, which may give rise to a type of anisotropy called magnetocrystalline anisotropy. The prediction of mechanical stability and anisotropy is in good agreement with the thermodynamic stability and sizeable mag- netocrystalline anisotropy energies reported in our previous communication. Computation of phonon dispersion spectra showed that the equiatomic $L1_{0}$ $P4/mmm$-FePt is dynami cally stable at ambient conditions, while the other compositions show soft modes along high-symmetry directions of the Brillouin zone. This study revealed that the negative vi- brational modes predominantly emanate from Fe atoms in the highly dynamically unstable $Pm\overline{3}m$-FePt₃ alloy, while dynamical instability is not pronounced in $I4/mmm$-Fe₃Pt since the negative vibrations are not along the center of the Brillouin zone. Moreover, $I4/mmm$- Fe₃Pt shows excellent mechanical stability, ductility, and thermal properties. Furthermore, the temperature versus entropy plots indicated that dynamically unstable alloys exhibit high atomic mobility as entropy exponentially increases with temperature, leading to the disordering of the lattice structure. This was corroborated by the heat capacity and Debye temperature plots. The free energies were predicted to be negative and to continue to decrease with temperature, implying thermodynamic stability in all the alloys. In addition to the current conclusions, it is of interest to perform ternary alloying of FePt with other transition metals such as Mn, Co, and Ni to determine any potential enhancement of the desired properties.

**Author Contributions:** Conceptualization, N.L.L. and P.M.; methodology, N.L.L.; software, N.L.L. and P.M.; validation, N.L.L. and P.M.; formal analysis, N.L.L.; investigation, N.L.L.; resources, N.L.L. and P.M.; data curation, N.L.L.; writing-original draft preparation, N.L.L.; writing-review and editing, N.L.L. and P.M.; visualization, N.L.L.; supervision, N.L.L. and P.M.; project administration, N.L.L.; funding acquisition, N.L.L. and P.M. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research received no external funding.

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** The generated data can be obtained from nlethole@ufh.ac.za or ndandulethole@gmail.com.

**Acknowledgments:** This work was performed at the University of Fort using the computing resources provided by the National Integrated Cyberinfrastructure System (NICIS). The financial support was provided by the Renewable Energy-Wind Research Niche Area of the Govern Mbeki Research and Development Centre (GMRDC), University of Fort Hare.

**Conflicts of Interest:** The authors declare no conflicts of interest.

### References
1.  Wang, J.P. FePt Magnetic Nanoparticles and Their Assembly for Future Magnetic Media. *Proc. IEEE* **2008**, 96, 1847. [CrossRef]
2.  Alsaad, A.; Ahmad, A.A.; Obeidat, T.S. Structural, electronic and magnetic properties of the ordered binary FePt, MnPt, and CrPt3 alloys. *Heliyon* **2020**, 6, e03545. [CrossRef] [PubMed]
3.  Lethole, N.; Ngoepe, P.; Chauke, H. Compositional Dependence of Magnetocrystalline Anisotropy, Magnetic Moments, and Energetic and Electronic Properties on Fe-Pt Alloys. *Materials* **2022**, 15, 5679. [CrossRef] [PubMed]

4. Laureti, S.; D'Acapito, F.; Imperatori, P.; Patrizi, E.; Varvaro, G.; Puri, A.; Cannas, C.; Capobianchi, A. Synthesis of highly ordered L10 MPt alloys (M = Fe, Co, Ni) from crystalline salts: An in situ study of the pre-ordered precursor reduction strategy. *J. Mater. Chem. C* **2023**, *11*, 16661. [CrossRef]

5. Crisan, A.D.; Bednarcik, J.; Michalik, Š.; Crisan, O. In situ monitoring of disorder-order A1-L10 FePt phase transformation in nanocomposite FePt-based alloys. *J. Alloys Compd.* **2014**, *615*, S188. [CrossRef]

6. Müller, M.; Erhart, P.; Albe, K. Thermodynamics of L10 ordering in FePt nanoparticles studied by Monte Carlo simulations based on an analytic bond-order potential. *Phys. Rev. B* **2007**, *76*, 155412. [CrossRef]

7. Müller, M.; Albe, K. Lattice Monte Carlo simulations of FePt nanoparticles: Influence of size, composition, and surface segregation on order-disorder phenomena. *Phys. Rev. B* **2005**, *72*, 094203. [CrossRef]

8. Yu, G.L.; Cheng, T.; Zhang, X. Effect of pressure on the magnetic, mechanical, and dynamical properties of L10-FePt alloy. *J. Appl. Phys.* **2023**, *134*, 085902. [CrossRef]

9. Whang, S.H.; Feng, Q.; Gao, Y.Q. Ordering, deformation and microstructure in L10 type FePt. *Acta Mater.* **1998**, *46*, 6485. [CrossRef]

10. Crisan, O.; Crisan, A.D.; Randrianantoandro, N. Temperature-Dependent Phase Evolution in FePt-Based Nanocomposite Multiple-Phased Magnetic Alloys. *Nanomaterials* **2022**, *12*, 4122. [CrossRef]

11. Zotov, N.; Ludwig, A. First-principles calculations of the elastic constants of FeePt alloys. *Intermetallics* **2008**, *16*, 113. [CrossRef]

12. Cabri, L.J.; Oberthür, T.; Schumann, D. The Mineralogy of Pt-Fe alloys and phase relations in the Pt-Fe binary system. *Can. Miner.* **2022**, *60*, 331. [CrossRef]

13. Yu, G.; Cheng, T.; Zhang, X. Exploring the structural stability and related physical properties of FePt₂ alloys. *Phys. B Condens. Matter.* **2024**, *680*, 415833. [CrossRef]

14. Yu, G.; Cheng, T.; Zhang, X. Exploration of novel structures and related physical properties of Fe₂Pt ordered alloys. *Solid. State Sci.* **2023**, *146*, 107380. [CrossRef]

15. Pierron-Bohnes, V.; Montsouka, R.V.P.; Goyhenex, C.; Mehaddene, T.; Messad, L.; Bouzar, H.; Numakura, H.; Tanaka, K.; Hennion, B. Atomic migration in bulk and thin film L10 alloys: Experiments and molecular dynamics simulations. *Defect Diffus. Forum* **2007**, *1*, 263.

16. Noda, Y.; Endoh, Y.; Katano, S.; Iizumi, M. Lattice dynamics of FePt alloys of AB3 type ordered structure. *Phys. B* **1983**, *120*, 317. [CrossRef]

17. Sternik, M.; Couet, S.; Lazewski, J.; Jochym, P.T.; Parlinski, K.; Vantomme, A.; Temst, K.; Piekarz, P. Dynamical properties of ordered FeePt alloys. *J. Alloys Compd.* **2015**, *651*, 528. [CrossRef]

18. Phasha, M.J.; Ngoepe, P.E.; Chauke, H.R.; Pettifor, D.G.; Nguyen-Mann, D. Link between structural and mechanical stability of fcc- and bcc-based ordered MgeLi alloys. *Intermetallics* **2010**, *18*, 2083. [CrossRef]

19. Botha, L.M.; Ouma, C.N.M.; Obodo, K.O.; Bessarabov, D.G.; Sharypin, D.L.; Varyushin, P.S.; Plastinina, E.I. Ab Initio Study of Structural, Electronic, and Thermal Properties of Pt/Pd-Based Alloys. *Condens. Matter.* **2023**, *8*, 76. [CrossRef]

20. Diale, R.G.; Ngoepe, P.E.; Moema, J.S.; Phasha, M.J.; Moller, H.; Chauke, H.R. A computational study of the thermodynamic and magnetic properties of Co alloyed MnPt. *MRS Adv.* **2023**, *8*, 651. [CrossRef]

21. Al-Essa, S.; Essaoud, S.S.; Bouhemadou, A.; Ketfi, M.E.; Omran, S.B.; Chik, A.; Radjai, M.; Allali, D.; Khenata, R.; Al-Douri, Y. A Comprehensive Ab Initio Study of the Recently Synthesized Zintl Phase CsGaSb₂ Structural, Dynamical Stability, Elastic and Thermodynamic Properties. *J. Inorg. Organomet. Polym. Mater.* **2024**. [CrossRef]

22. Kim, J.; Koo, Y.; Lee, B.J. Modified embedded-atom method interatomic potential for the Fe-Pt alloy system. *J. Mater. Res.* **2006**, *21*, 199. [CrossRef]

23. Tajima, K.; Endoh, Y.; Ishikawa, Y.; Stirling, W.G. Acoustic-Phonon Softening in the Invar Alloy Fe₃Pt. *Phys. Rev. Lett.* **1976**, *37*, 519. [CrossRef]

24. Kastner, J.; Neuhaus, J.; Wassermann, E.; Petry, W.; Hennion, B.; Bach, H. TA1 [110] phonon dispersion and martensitic phase transition in ordered alloys Fe₃Pt. *Eur. Phys. J. B* **1999**, *11*, 75. [CrossRef]

25. Clark, S.J.; Segall, M.D.; Pickard, C.J.; Hasnip, P.J.; Probert, M.J.; Refson, K.; Payne, M.C. First principles methods using CASTEP. *Z. Krist. Cryst. Mater.* **2005**, *220*, 567. [CrossRef]

26. Perdew, J.P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* **1996**, *77*, 3865. [CrossRef] [PubMed]

27. Hao, D.; He, X.; Roitberg, A.E.; Zhang, S.; Wang, J. Development and Evaluation of Geometry Optimization Algorithms in Conjunction with ANI Potentials. *J. Chem. Theory Comput.* **2022**, *18*, 978. [CrossRef] [PubMed]

28. Packwood, D.; Kermode, J.; Mones, L.; Bernstein, N.; Wooley, J.; Gould, N.; Ortner, C.; Csanyi, G. A universal preconditioner for simulating condensed phase materials. *J. Chem. Phys.* **2016**, *144*, 164109. [CrossRef] [PubMed]

29. Togo, A. First-principles Phonon Calculations with Phonopy and Phono3py. *J. Phys. Soc. Jpn.* **2023**, *92*, 012001. [CrossRef]

30. Togo, A.; Tanaka, I. First principles phonon calculations in materials science. *Scr. Mater.* **2015**, *108*, 1. [CrossRef]

31. Chen, H.S. *Elastic Anisotropy of Metal*; Metallurgy Industry Press: Beijing, China, 1996.

32. Fast, L.; Wills, J.M.; Johansson, B.; Eriksson, O. Elastic constants of hexagonal transition metals: Theory. *Phys. Rev. B* **1995**, *51*, 17431. [CrossRef] [PubMed]

33. Karki, B.B.; Ackland, G.J.; Crain, J. Elastic instabilities in crystals from ab initio stress—Strain relations. *J. Phys. Condens. Matter.* **1997**, *9*, 8579. [CrossRef]

34. Kittel, C. *Introduction to Solid State Physics*, 8th ed.; John Wiley & Sons Inc.: Hoboken, NJ, USA, 2005.

35. Born, M.; Huang, K. *Dynamical Theory of Crystal Lattices*; Clarendon: Oxford, UK, 1956.

36. Ranganathan, S.I.; Ostoja-Starzewski, M. Universal Elastic Anisotropy Index. *Phys. Rev. Lett.* 2008, 101, 055504. [CrossRef] [PubMed]

37. Voigt, W. *Lehrbuch der Kristallphysik*; Taubner: Leipzig, Germany, 1928.

38. Reuss, A. Calculation of the flow limits of mixed crystals on the basis of the plasticity of monocrystals. *Z. Angew. Math. Mech.* 1929, 9, 55.

39. Hill, R. The Elastic Behaviour of a Crystalline Aggregate. *Proc. Phys. Soc. A* 1952, 65, 349. [CrossRef]

40. Pugh, S.F. XCII. Relations between the elastic moduli and the plastic properties of polycrystalline pure metals. The London, Edinburgh, and Dublin Philosophical Mag. *J. Sci.* 1954, 45, 823.

41. Frantsevich, I.N.; Voronov, F.F.; Bokuta, S.A. *Elastic Constants and Elastic Moduli of Metals and Insulators*; Frantsevich, I.N., Ed.; Naukova Dumka: Kiev, Ukraine, 1983; p. 60.

42. Murtaza, G.; Gupta, S.K.; Seddik, T.; Khenata, R.; Alahmed, Z.A.; Ahmed, R.; Khachai, H.; Jha, P.K.; Omran, S.B. Structural, electronic, optical and thermodynamic properties of cubic REGa3 (RE = Sc or Lu) compounds: Ab initio study. *J. Alloys Compd.* 2014, 597, 36. [CrossRef]

43. Haines, J.; Léger, J.M.; Bocquillon, G. Synthesis and Design of Superhard Materials. *Annu. Rev. Mater.* 2001, 31, 1. [CrossRef]

44. Kiejna, A.; Wojciechowski, K.F. The surface of real metals. In *Metal Surface Electron Physic*; Alden Press: Oxford, UK, 1996; p. 19.

45. Jiang, D.; Xiao, W.; Liu, D.; Liu, S. Structural stability, electronic structures, mechanical properties and debye temperature of W-Re alloys: A first-principles study. *Fusion Eng. Des.* 2021, 162, 112081. [CrossRef]

46. Tohei, T.; Kuwabara, A.; Oba, F.; Tanaka, I. Debye temperature and stiffness of carbon and boron nitride polymorphs from first principles calculations. *Phys. Rev. B* 2006, 73, 064304. [CrossRef]

47. Tian, Y.; Xu, B.; Zhao, Z. Microscopic theory of hardness and design of novel superhard crystals. *Int. J. Refract. Hard. Met.* 2012, 33, 93. [CrossRef]

48. Chen, X.Q.; Niu, H.; Li, D.; Li, Y. Modeling hardness of polycrystalline materials and bulk metallic glasses. *Intermetallics* 2011, 19, 1275. [CrossRef]

49. Zerrougui, Z.; Bouferrache, K.; Ghebouli, M.A.; Slimani, Y.; Chihi, T.; Ghebouli, B.; Fatmi, M.; Benlakhdar, F.; Mouhammad, S.A.; Algethami, N.; et al. Study of structural, elastic, mechanical, electronic and magnetic properties of FeX (X=Pt, Pd) austenitic and martensitic phases. *Solid State Sci.* 2023, 141, 107211. [CrossRef]

50. Piekarz, P.; Lazewski, J.; Jochym, P.T.; Sternik, M.L.; Parlinski, K. Vibrational properties and stability of FePt nanoalloys. *Phys. Rev. B* 2017, 95, 134303. [CrossRef]

51. Baroni, S.; de Gironcoli, S.; Corso, A.D.; Giannozzi, P. Phonons and related crystal properties from density-functional perturbation theory. *Rev. Mod. Phys.* 2001, 73, 515. [CrossRef]

52. Dima, R.S.; Maleka, P.M.; Maluta, N.E.; Maphanga, R.R. Structural, Electronic, Mechanical, and Thermodynamic Properties of Na Deintercalation from Olivine NaMnPO4: First-Principles Study. *Materials* 2022, 15, 5280. [CrossRef] [PubMed]

53. Tang, K.; Wang, T.; Qi, W.; Li, Y. Debye temperature for binary alloys and its relationship with cohesive energy. *Phys. B Condens. Matter.* 2018, 531, 95. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.