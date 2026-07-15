Applied Surface Science 536 (2021) 147973

![](./images/812563893304950784_1.jpg)
Contents lists available at ScienceDirect
Applied Surface Science
journal homepage: www.elsevier.com/locate/apsusc
![](./images/812563893304950784_2.jpg)

# Ab initio study of molybdenum sulfo-selenides alloy as a flexible anode for sodium-ion batteries

![](./images/812563893304950784_3.jpg)

Archana Sharma$^{\rm a}$, Mohd. Shahid Khan$^{\rm a,*}$, Md. Shahzad Khan$^{\rm b}$, Mushahid Husain$^{\rm a}$

$^{\rm a}$ Department of Physics, Jamia Millia Islamia, New Delhi 110025, India
$^{\rm b}$ School of Basic and Applied Science, Galgotias University, Greater Noida, UP 201310, India

---

## ARTICLE INFO

**Keywords:**
MoS₂
DFT
2D materials
Storage
Energy

## ABSTRACT

In the recent times, sodium-ion batteries (SIBs) are exceptionally popular as a cost-effective replacement for lithium-ion batteries (LIBs), particularly for load levelling of renewable energy sources. Using state-of-the-art density functional theory (DFT) calculations, we investigate the alloy of MoS₂ and MoSe₂ to be used as anode for rechargeable SIBs. We provide atomic level studies of important electrochemical properties of the electrode material in terms of electronic conductivity, voltage profile, specific capacity, sodium ion mobility, and mechanical strength. Our results show that the electrode possess high specific charge capacity of 1036 mA h g⁻¹ and a low anode potential window of 1.52-0.14 V, leading to high rate capability performance. In addition to high capacity, introduction of selenium also boosts the conductivity of the pristine MoS₂ material while not affecting the mechanical strength as well as maintaining the structural stability. We calculate low ion-hopping barrier of 0.035 eV and 0.052 eV for diffusion on the outside surface of Se and S atoms, suggesting fast mobility of Na and hence fast charging/discharging rate. Moreover, MoSSe alloy can withstand strains as high as 25%, depicting ultrahigh flexibility without any structural distortion even at high concentration of Na atoms.

---

## 1. Introduction

Energy crisis is the world-wide problem faced by human mankind today and sufficing the ever-growing energy demands is one of the biggest challenges. Limited reserves of fossil fuels and their adverse effects on environment have led to the emergence of renewable energy sources. For integrating these sources into the electric grid, energy storage technologies are needed to store the electricity at large scale. Electrochemical batteries are flexible and need simple maintenance, thus being the promising choice for such large-scale electricity storage application [1,2]. Lithium-ion batteries (LIBs) are the source of high energy and have been extensively utilized for portable electronics and hybrid electric vehicles due to their light weight and high energy density of lithium, ever since their first commercialization by Sony in 1990s [3]. However, lithium being limited in existence, such a large level demand is surely going to skyrocket the price. Sodium-ion batteries (SIBs) are the next-generation alternative to LIBs for meeting concerns of load levelling and sustainability. Sodium, having high ion conductivity and fast diffusion, is highly abundant and inexpensive and is well suited for large scale applications such as in electric vehicles and grid level electricity storage applications [4-7]. SIBs came into light when Stevans and Dahn reported reversible capacity of 300 mA h g⁻¹ close to that for lithium insertion in graphitic carbon in the year 2000 [8]. However, cycling efficiency was not enough for battery operation at that time. Interestingly, rechargeable batteries using sodium which is available at much lower cost than lithium, exhibit similar chemistry as lithium. Hence SIBs may benefit from the developments of LIBs.

The next immediate task is to select suitable negative electrode (anode) material with improved reaction kinetics for fast sodium ion storage, which is a primary step towards realization of high energy density and improved electrode performance as production of energy and its conversion and storage has been greatly facilitated by nano-materials [9,10]. Here comes the role of first principles computations, which plays a prominent role in designing new materials for energy production and storage and predicting relevant physico-chemical properties as it has precise control on structures. The obtained results can be helpful in both validating laboratory experiments and providing information which is either unaccessbile or difficult to achieve by experiments. A good anode material should possess high thermal and chemical stability during charging/discharging, high ion mobility and electron transport, high surface area, low voltage and large gravimetric capacity, and low cost [11,12]. With the advent of nanotechnology, 2D materials are emerging as promising anode materials. Some of the key attractions of 2D materials include: high surface area, leading to

---

* Corresponding author.
E-mail address: mskhan@jmi.ac.in (M.S. Khan).

https://doi.org/10.1016/j.apsusc.2020.147973
Received 29 April 2020; Received in revised form 1 September 2020; Accepted 22 September 2020
Available online 28 September 2020
0169-4332/ © 2020 Elsevier B.V. All rights reserved.

![](./images/812563893304950784_4.jpg)

Fig. 1. Structural and electronic properties of MoSSe alloy: (a) Optimized geometries (top, bottom and side views), along with description of possible sites for sodium adsorption (Tm: top of Mo atom; H: top of hexagon atom (b) band structures of pristine MoS₂ (left) and MoSSe alloy (right) along the high symmetry points M(0, 0.5, 0.0) → K(-0.3, 0.6, 0.0) → Γ(0.0, 0.0, 0.0) → M(0, 0.5, 0.0) with energy band gaps indicated. The Fermi level is represented by black dashed line.

availability of more active sites and hence improved ion adsorption, high contact area with electrolyte; good ion diffusivity due to reduction of path length; high electron transportation; high stability [12–15]. MoS₂, a graphene like material, has been extensively explored as potential material for numerous applications [16–18], including as potential anode material for metal-ion batteries [19–21]. Unlike the planar structure of graphene, MoS₂ supports better anchoring ability of metal atoms and hence possess higher capacity. Bare MoS₂ nanosheets have been utilized as an anode material in SIBs with a high reversible specific capacity [21,22]. However, their inherent low conductivity and large volume expansion have resulted in fast capacity fading and poor cycling stability.

Alloy of MoS₂ and MoSe₂ can be formed by replacing top S layer with Se layer. The resulting structure is also known as Janus structure of MoS₂. Recently, such structure has been synthesized by replacing S layer with Se layer at an appropriate temperature using modified chemical vapor deposition (CVD) technique [23,24]. It is one of the synthetic strategies to break the off plane symmetry of MoS₂, giving rise to many unique properties such as Rasba spin splitting, a second harmonic generation (SHG) response and large piezoelectric effect [25]. These properties can be effectively utilized in designing sensors, actuators, spintronic, energy and electromechanical devices [25]. In the present work, we study the electrochemical performance of MoSSe alloy to be used as an anode material in Na-ion batteries, with an aim to design better anode materials using DFT-based methods. Our work predicts electrode properties of the alloy which has shown interesting results in terms of high capacity, low voltage, high charging/discharging rate, high flexibility which are necessary for the development of high-performance anode materials for SIBs.

## 2. Computational details

The DFT calculations are conducted using Vienna ab initio Simulation Package (VASP) [26] within generalized gradient approximation (GGA) of Perdew-Burke-Ernzerhof (PBE) functional [27] as implemented in the medeA materials design software [28]. This package involves plane waves basis sets for the expansion of electronic wavefunctions where electron-ion interactions are described by a pseudopotential. The pseudopotential is generated by projector-augmented wave (PAW) method [29] which combines well the efficiency of pseudopotentials with the accuracy of full potential. The number of plane waves to be used is determined by energy cut off value which is chosen to be 400 eV, enough to ensure total energy convergence. Periodic images are separated using the vacuum of more than 30 Å and 5 × 5 × 1 Γ-centered k points are used for Brillouin zone integration [30]. Van der Waal (vdW) interactions are also considered using Grimme's DFT-D2 scheme [31]. The structural relaxations are achieved by conjugate-gradient method with total energy convergence of 10⁻⁵ eV between two consecutive steps and until the maximum force on each atom is 0.02 eV/Å. Migration of Na from one site to neighboring site on MoSSe surface via intermediate states is described by climbing image nudged elastic band (CI-NEB) method [32] which accurately estimates activation barrier along the minimum energy path [33,34]. In this method, each image along the pathway, is optimized to obtain its minimum energy configuration and the ones with highest energy are considered the saddle points. Diffusion barrier gives the energy difference between a saddle point and the nearest minimum point to that saddle point. Ab initio molecular dynamics (AIMD) simulations are carried out to study thermal stability of the anode material in NVT (canonical) ensemble with a time step of 2 fs at a high temperature (500 K).

## 3. Results and discussion

### 3.1. MoSSe alloy: Structural, electronic, and mechanical properties and stability

Structure of MoSSe alloy comprises of an Mo layer sandwiched between an S and an Se layer, Mo being six-fold coordinated while S and Se being three-fold coordinated. The optimized lattice constant is obtained to be 3.25 Å, which is in well agreement with literatures [24,35] and lies between the lattice constant values of MoS₂ (3.18 Å) and MoSe₂ (3.30 Å). S-Mo and Se-Mo is calculated to be 2.42 Å and 2.54 Å respectively. A fully relaxed 3 × 3 × 1 supercell of MoSSe monolayer is modeled for using as electrode material, as shown in Fig. 1 (a). Obtaining information on energy gap is the starting point for the investigation of electronic properties of the desired electrode material. We can infer about the electronic conductivity from band energy diagram of both MoS₂ and MoSSe sheets, depicted in Fig. 1 (b). In both the cases, Fermi level is positioned at the center of the valence band maximum and conduction band minimum by shifting the energy band structures. In both cases, semiconducting trait with direct band gap are obtained but with values 1.650 eV and 1.547 eV, respectively, in accordance with a previous report [23]. So, introduction of Se layer leads to reduction in band gap, suggesting it to be more conductive than pristine MoS₂ and hence improved diffusion kinetics is anticipated.

Sodium insertion/extraction may cause destruction and re-construction of structures, exhibiting large volume expansion which can further cause large stress and deformation of the electrode material, in turn, affecting the charge capacity, morphology and cycle capacity [36]. Hence, it becomes very important to investigate the mechanical stability of the electrode during sodiation process. To ensure the stability of the alloy during charging/discharging, stress induced in the material on applying strain needs to be examined which determines Young's modulus and ultimate strain of the material corresponding to the breaking strength. Variation of strain energy for both monolayer

![](./images/812563893304950784_5.jpg)

Fig. 2. (a) Strain energy as a function of applied tensile strain, (b) Stress as a function of applied tensile strain along uniaxial (x and y) direction and biaxial (xy) direction for both monolayers MoS₂ (represented by black, red and olive curves) and MoSSe (represented by blue, pink and green curves).

MoS₂ and MoSSe with respect to applied uniaxial strains along x and y directions as well as biaxial directions are shown in Fig. 2(a), where strain energy is calculated as a difference of total energy at a given strain value and total energy at zero strain. For lower values of strain, strain energy increases slowly and depicts similar behavior for both MoS₂ and MoSSe monolayers in all directions. When strained further, significant differences appear as the strain energy increases rapidly in x-direction for both the materials while it slows down in y-direction, suggesting anisotropic properties of both monolayer MoS₂ and MoSSe. Further, stress (σ) can be calculated from the slope of strain energy curves per unit volume of the material in equilibrium state.

Stress-strain curves of MoS₂ and MoSSe are calculated along uniaxial (x and y) directions and biaxial directions show that both have similar strength bearable capacity. As shown in Fig. 2 (b), stress increases linearly for all directions for lower values of strain. In this region, Young's moduli of MoS₂ and MoSSe are calculated from the slope of the stress-strain curve which are 214 GPa and 204 GPa along x-direction, 217 GPa and 210 GPa along y-direction, and 268 GPa and 259 GPa along biaxial directions, respectively. For large strains, stress-strain response remains no longer linear and the hexagonal symmetry is broken owing to the difference in the stress response along x- and y-direction. Monolayers MoS₂ and MoSSe can withstand 26% and 25% strain along x-direction, 20% and 19% along y-direction while 25% and 24% along biaxial direction. The average breaking strength of MoS₂ and MoSSe corresponding to these ultimate strains are calculated to be 23.61 GPa and 21.85 GPa along x-direction, 15.77 GPa and 14.35 GPa along y-direction, and 26.98 GPa and 25.20 GPa along biaxial direction. The calculated values of Young's modulus (E), breaking strength (σ_max), and ultimate strain (ε*) corresponding to the uniaxial tensions along x- and y-directions and biaxial tension along xy for MoS₂ and MoSSe monolayers are displayed in Table 1. The calculated biaxial Young's modulus of MoS₂ monolayer and its breaking strength are in close agreement with the measurements done by Bertolazzi et al. [37] and the calculated values along uniaxial (x and y) directions are similar to ones obtained by Zhao et al. [38]. The results indicate that the alloy can withstand large strains without breaking attributed to the high Young's modulus and ultimate strain under uniaxial and biaxial tensions, which is very important factor to be considered for SIBs application.

The stability of alloy is also evaluated at high temperature of 500 K using AIMD simulations sampled at 3000 fs. The snapshots taken at intermediate time scales are shown in Fig. 3. During the process, structure remains quite intact with only minor variations in bond lengths. Hence it can be concluded that the structure is stable at high temperatures and room temperature stability also follows.

<table><caption>Table 1 Calculated Young's modulus (E), breaking strength (σ_max), and ultimate strain (ε*) corresponding to the uniaxial tensions along x and y directions and biaxial tension along xy for MoS₂ and MoSSe monolayers.</caption>
<thead>
<tr>
<th>System</th>
<th>Direction</th>
<th>E (GPa)</th>
<th>σ_max (GPa)</th>
<th>ε*</th>
</tr>
</thead>
<tbody>
<tr>
<td>MoS₂</td>
<td>x</td>
<td>214</td>
<td>23.61</td>
<td>0.26</td>
</tr>
<tr>
<td></td>
<td>y</td>
<td>217</td>
<td>15.77</td>
<td>0.20</td>
</tr>
<tr>
<td></td>
<td>xy</td>
<td>268</td>
<td>26.98</td>
<td>0.25</td>
</tr>
<tr>
<td>MoSSe</td>
<td>x</td>
<td>204</td>
<td>21.85</td>
<td>0.25</td>
</tr>
<tr>
<td></td>
<td>y</td>
<td>210</td>
<td>14.35</td>
<td>0.19</td>
</tr>
<tr>
<td></td>
<td>xy</td>
<td>259</td>
<td>25.20</td>
<td>0.24</td>
</tr>
</tbody>
</table>

### 3.2. Sodium adsorption on MoSSe alloy and diffusion kinetics: Power and rate capability

First and foremost, for assessing storage capability of Na ion on MoSSe alloy is to have knowledge about its favorable adsorption site. Adsorption of Na atom on the surface of MoSSe alloy is considered and concentration of Na in MoSSe unit cell is denoted by x in NaₓMoSSe. Three possible adsorption sites on each side of the layer are considered, namely top of Mo atom (Tₘ), top of hexagon (H) and top of Se/S atom, as illustrated in Fig. 1 (a). The adsorption energy (E_ads) of single Na on MoSSe alloy is calculated by

$$\mathrm{E_{ads} = E_{Naalloy} - E_{alloy} - E_{Na}}$$

where E_Naalloy is the total energy of the Na adsorbed on MoSSe alloy, E_alloy and E_Na are the total energy of MoSSe alloy sheet and single Na atom, respectively. After optimization, Na atom placed on top Se/S sites migrated to respective H sites and on comparing adsorption energies, Tₘ and H sites on bottom layer (−1.66 eV, −1.63 eV) are found to be more favorable than on top layer (−1.21 eV, −1.20 eV). The calculated negative value of E_ads of Na atom on these sites show that Na is effectively adsorbed on MoSSe alloy. It is to be noted that for each side of the structure, Tₘ site is more negative than H-site but the difference is not too large. Na atoms on both the sites are triply coordinated with S/Se atoms and adsorb at the height of 1.99 Å and 2.27 Å. Na adsorption slightly stretches one of the S-Mo and Se-Mo bond lengths to 2.43 Å and 2.55 Å. It also leads to the redistribution of charges on the surface which is quantified by Bader charge analysis [39]. It is seen that Na atom donates 0.755 e and 0.748 e charges to the system when adsorbed

![](./images/812563893304950784_6.jpg)

Fig. 3. Stability of MoSSe alloy: Snapshots of MoSSe alloy sheet (top and side views) at T = 500 K after running for 0 ps, 1 ps, 2 ps and 3 ps of the ab-initio molecular dynamics at a time step of 2 fs.

<table>
<thead>
<tr>
<th colspan="4">Table 2</th>
</tr>
<tr>
<th colspan="4">Adsorption energy (E<sub>ads</sub>) of Na on MoSSe alloy, distance between Na and surface of alloy (h) and charge transfer (CT) from Na adatom to MoSSe alloy for Se and S side of the layer at top of Mo (T<sub>m</sub>) and top of hexagon (H) sites.</th>
</tr>
<tr>
<th>Site</th>
<th>E<sub>ads</sub> (eV)</th>
<th>h (Å)</th>
<th>CT (e)</th>
</tr>
</thead>
<tbody>
<tr>
<td>T<sub>m</sub> at Se side</td>
<td>−1.25</td>
<td>2.27</td>
<td>0.669</td>
</tr>
<tr>
<td>H at Se side</td>
<td>−1.20</td>
<td>2.31</td>
<td>0.660</td>
</tr>
<tr>
<td>T<sub>m</sub> at S side</td>
<td>−1.66</td>
<td>1.99</td>
<td>0.755</td>
</tr>
<tr>
<td>H at S side</td>
<td>−1.63</td>
<td>2.07</td>
<td>0.748</td>
</tr>
</tbody>
</table>

at Tm and H sites on bottom layer while on top layer charges gained by the system are 0.669 e and 0.660 e, respectively. The calculated charges depict strong bonding between Na and MoSSe alloy. The values of adsorption energy, height of Na from the MoSSe surface and charge transfer are summarized in Table 2. The origin of strong adsorption strength of Na atom on S side than on Se side is evident from relatively strong interactions between Na and S, as reflected from density of states (DOS) plot, shown in Fig. 4. As can be seen, adsorption of Na atoms does not significantly change the DOS of MoSSe. After adsorption of Na on either side results in shift of Fermi level toward conduction band which confirms charge acceptance by the system. From the magnified portions of the DOS near Fermi level, it can be seen that for Na bonded with S atoms, there are relatively more electron states near Fermi level due to more charge transfer and hence could be the reason for its strong bonding character.

Diffusion of Na ion is an important index to determine the rate capability of anode material to deliver power. Faster mobility of Na ion indicates fast charging/discharging rate of rechargeable batteries which is assessed by calculating energy barrier. Since T<sub>m</sub> is the most favorable site on both the sides of the layer, migration pathways on each side of the layer are considered between two neighboring T<sub>m</sub> sites. As per the arrangement of atoms in MoSSe structure, two migration pathways are possible, as elucidated in Fig. 5. Path I depicts the diffusion pathway to

![](./images/812563893304950784_7.jpg)

Fig. 4. Density of states (DOS) for MoSSe alloy (bottom panel), Na adsorption on Se layer (middle panel) and S layer (top panel). The black dashed line represents the Fermi level. Magnified images of the DOS near Fermi level for Na adsorption on Se layer and S layer are shown on the right.

![](./images/812563893304950784_8.jpg)

Fig. 5. Schematic illustration of Na migration pathways on the surface of Se layer (top) and S layer (bottom) with corresponding energy profiles.

the immediate neighbor through hexagonal site while Path II depicts migration to the next immediate neighbor through S/Se and hexagonal sites both. In both the pathways, intermediate structures are generated between two neighboring sites using linear interpolation method and each structure is optimized in every direction for both sides of the layer. On outside surface of Se layer: While Path I shows only one saddle point, Path II shows three saddle points, the calculated energy barrier do not differ much. The energy barrier along Path I and Path II are calculated to be 0.035 eV and 0.044 eV, respectively. On outside surface of S layer: Path I and Path II have notable differences in terms of calculated barriers. The energy barriers are calculated to be 0.052 eV and 0.589 eV for Path I and Path II, respectively. Due to high energy barrier along Path II in both cases, diffusion of Na ion will be along Path I, which is the minimum energy path. It is to note that diffusion barrier on outside surface of S is relatively larger than that of Se due to strong adsorption strength of Na on S side than on Se side, which is ascribed to lesser strong bonding between Na and Se atom. The obtained diffusion barrier of 0.035 eV (on Se side) and 0.052 eV (on S side) is smaller than those for monolayer MoS₂ [40] and layered MoS₂ [41] systems, which is attributed to improved conductivity as evident from reduced band gap.

### 3.3. Working potential, theoretical specific capacity and volume expansion of MoSSe alloy

High energy density of the battery is also an essential requirement along with high conductivity and high charging/discharging for excellent electrochemical properties. It is determined from the two important parameters for rechargeable batteries: working voltage and specific capacity. Both the parameters are directly or indirectly related to total energy calculations and therefore can be easily predicted with DFT. The following common half-cell reaction is considered for describing charge/discharge process:

$$Na_{x_1}Anode + (x_2 - x_1)Na^{n+} + (x_2 - x_1)ne^- \leftrightarrow Na_{x_2}Anode$$

where Anode denotes MoSSe alloy, $x_1$ and $x_2$ are number of $Na^+$ ions transferred during charging/discharging into anode material and n is the valency of fully ionized $Na^+$ ion (n = 1). Layer by layer adsorption of Na atoms on MoSSe alloy is considered where first layer (1L) of Na atoms is formed by placing Na atoms on most favorable adsorption site i.e., all $T_m$ sites of bottom layer. After full geometry optimization, the configuration is shown in Fig. 6. The average adsorption energy of Na atoms on MoSSe alloy is calculated by

$$E_{avg} = \frac{E_{cNaAnode} - E_{Anode} - cE_{Na}}{c}$$

where c is the total number of Na atoms adsorbed at a particular instant, $E_{cNaAnode}$ is the total energy of Na atoms adsorbed MoSSe system, $E_{Anode}$ is the total energy of MoSSe alloy and $E_{Na}$ is the energy of a single Na atom. For the first layer (1L), average adsorption energy is calculated to be $-1.520$ eV. For second adsorption layer (2L), three possible sites are investigated, H site of bottom layer, top site of S layer and $T_m$ site of Se layer. Out of which, last one turns out to be the most favorable configuration with $E_{avg}$ of $-1.493$ eV. The corresponding adsorption energy of the layer is calculated by

$$E_{layer} = \frac{(E_{Na_{x_2}Anode}) - ((x_2 - x_1)E_{Na} + E_{Na_{x_1}Anode})}{x_2 - x_1}$$

This is basically the difference between total energies before and after $Na^+$ adsorption per Na atom inserted. For first adsorption layer (1L), it has to be the same as the average adsorption energy and for second adsorption layer (2L), it is calculated to be $-1.466$ eV, ensuring strong and stable adsorption strength. The most favorable site for third adsorption layer (3L) is found to be at the top of the S, with average adsorption energy of $-1.445$ eV and adsorption energy of layer is calculated to be $-1.348$ eV. For fourth adsorption layer (4L), the most favorable site is found to be at the top of Se layer and after this, the trend is repeated through eight adsorption layers when no substantial change in the voltage profile is observed. Variation of $E_{layer}$ with respect

![](./images/812563893304950784_9.jpg)

Fig. 6. Variation of adsorption energy of layer with Na concentration (x) in NaₓMoSSe. Each concentration corresponds to number of layers denoted by L.

to the number of adsorbed layers for different Na concentrations (x = 1 to 8) is shown in Fig. 6 along with the respective configurations. Electrode potential is calculated by measuring voltage over Na covered anode, expressed by [42-44]

$$
\mathrm{V}=-\frac{\Delta \mathrm{G}}{\mathrm{nce}}
$$

where $\Delta$G is Gibbs free energy, given by the change in electronic energy before and after Na adsorption with pressure (P$\Delta$V) and entropy (T$\Delta$S) being neglected due to very small values at room temperature [44]

$$
\Delta \mathrm{G}=\left(\mathrm{E}_{\mathrm{Na}_{\mathrm{x}_{2}} \text { Anode }}\right)-\left(\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right) \mathrm{E}_{\mathrm{Na}}+\mathrm{E}_{\mathrm{Na}_{\mathrm{x}_{1}} \text { Anode }}\right)
$$

For the fully sodiated MoSSe alloy, the specific capacity is theoretically calculated by [45]

$$
\mathrm{C}=\frac{\mathrm{x}_{\max } \mathrm{nF}}{\mathrm{M}_{\text {anode }}}
$$

where $\mathrm{x}_{\max }$ is the maximum number of $\mathrm{Na}^{+}$adsorbed, F is the Faraday's constant (F = 26,801 mA h mol⁻¹) and $\mathrm{M}_{\text {anode }}$ represents the weight of anode material in g mol⁻¹. The electrode voltage of NaₓMoSSe with respect to specific capacity (corresponding to Na concentration) is shown in Fig. 7. The variation of corresponding average adsorption energy ($\mathrm{E}_{\text {ads }}$) with specific capacity is shown in the inset. During sodiation, discharge profile shows a plateau at 0.14 V while maintaining a low voltage window of 1.52-0.14 V for all specific capacities which indicates its suitability for using as anode material [22,46]. Combining low voltage anode with high voltage cathode may result in high cell voltage. It is to note that less positive anode potentials close to 0 V are not desired either, as it would lead to the formation of dendrites and blockage of solid electrolyte interphase [47]. The maximum capacity for eight-layer Na adsorbed anode material is calculated to be 1036 mA h g⁻¹ with chemical composition, Na₈MoSSe. The components serving as electrodes are the primary determinants of storage capacity and hence weight of the mobile ions has no effect on capacity calculation [48]. It is well known that performance of monolayer MoS₂ as anode for SIBs is seriously restricted due to its large volume expansion [21,22]. Hence, volume expansion resulting from the Na insertion needs to be evaluated by studying the structural variation. It is found that variation in the thickness of the material as well as lattice expansion along x and y direction for the initial two layers is more prominent as compared to next subsequent layers. For the first layer, lattice expansion of about 0.89% along x and y direction each and thickness expansion of about 0.56% take place while for second layer, these are about 2.06% and 0.31%, respectively. Addition of subsequent layers does not result in much variation in the lattice expansion while no expansion of the thickness of the material takes place further, rather it contracts, as depicted in Fig. 8 (a). Hence it can be asserted that the layered adsorption of Na atoms can be adsorbed without much change in the volume of the material. For maximum capacity of anode, there is volume expansion of about 6.08% which can be easily borne by the MoSSe alloy as evident from the its stress response. S-Mo bond length increases to 2.36 Å and Se-Mo bond length slightly increases to 2.55 Å after the adsorption of first Na layer over S-surface while S-Mo bond length slightly decreases to 2.44 Å and Se-Mo bond length increases to 2.59 Å after the adsorption of second Na layer over Se-surface. As the adsorption of Na concentration increases further, no significant change in the bond lengths of S-Mo and Se-Mo is observed. Also, there is significant reduction in the height of the Na layer from the S/Se surface with addition of Na layers from 2.25 Å (1L) to 2.15 Å (8L) for S-side and from 2.42 Å (2L) to 2.36 Å (8L) for Se-side, as shown in Fig. 8 (b). Hence, it can be concluded that structural variations for different Na concentrations are prominent for lower concentrations (x≤2). Besides, no structural distortion has been observed for MoSSe structure even at high concentration of Na atoms.

Further, bond lengths of Na with Se and S are analyzed to understand the formation of Na₂S and Na₂Se which may occur during sodiation. In this process, Na atom is adsorbed one by one, which can be considered as the intermediate structures, beginning from the S-Side upto two layers as it is most likely that Na₂S and Na₂Se may form

![](./images/812563893304950784_10.jpg)

Fig. 7. Voltage profile for different specific charge capacities of Na adsorbed MoSSe alloy. Variation of average adsorption energy with specific charge capacity is provided in the inset.

![](./images/812563893304950784_11.jpg)

Fig. 8. (a) Variation of lattice expansion (Δa or Δb and Δc) and volume expansion (ΔV), (b) S/Se-Mo bond length (d) and height (H) of Na layer from S/Se surface for different Na concentration (x) in NaₓMoSSe.

### Table 3
Calculated value of average adsorption energy (Eₐᵥ₉), adsorption energy of layer per Na atom (Eₗₐᵧₑᵣ), anode voltage and volume expansion for different Na concentration or specific capacity.

<table>
<thead>
<tr>
<th>Na conc. (x)</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
</tr>
</thead>
<tbody>
<tr>
<td>Capacity (mA h g⁻¹)</td>
<td>129.5</td>
<td>258.9</td>
<td>388.5</td>
<td>517.9</td>
<td>647.5</td>
<td>776.9</td>
<td>906.5</td>
<td>1035.9</td>
</tr>
<tr>
<td>Eₐᵥ₉ (eV)</td>
<td>−1.520</td>
<td>−1.493</td>
<td>−1.445</td>
<td>−1.422</td>
<td>−1.406</td>
<td>−1.375</td>
<td>−1.366</td>
<td>−1.329</td>
</tr>
<tr>
<td>Eₗₐᵧₑᵣ (eV)</td>
<td>−1.520</td>
<td>−1.466</td>
<td>−1.348</td>
<td>−1.354</td>
<td>−1.341</td>
<td>−1.308</td>
<td>−1.305</td>
<td>−1.299</td>
</tr>
<tr>
<td>Voltage (V)</td>
<td>1.520</td>
<td>0.733</td>
<td>0.449</td>
<td>0.338</td>
<td>0.268</td>
<td>0.218</td>
<td>0.186</td>
<td>0.143</td>
</tr>
<tr>
<td>Volume expansion (%)</td>
<td>1.43</td>
<td>3.53</td>
<td>3.87</td>
<td>4.51</td>
<td>4.72</td>
<td>5.12</td>
<td>5.62</td>
<td>6.08</td>
</tr>
</tbody>
</table>

during very low concentration of Na, given that the structural variations are more prominent for lower concentrations only. It is found that the S-Na bond lengths for 2Na are found to be about 2.82 Å each which is similar to that of S-Na bond in the crystalline Na₂S [49]. Subsequent adsorption of Na atoms over Se surface leads to Se-Na bond lengths of about 2.94 Å each for 2Na adsorption which is close to Se-Na bond length in the crystalline Na₂Se [50]. In both the cases, bond length stretches on further adsorption and hence crossing the critical value of S-Na and Se-Na bond lengths in Na₂S and Na₂Se crystals, respectively. Although, higher concentration of Na has attracted reduction in the height of the first two layers from the S/Se surface which also indicates reduction in S/Se-Na bond lengths but these stay beyond the critical value of S/Se-Na bond lengths. S-Na bond length reduces from 2.94 Å to 2.89 Å as moving from 1L to 8L while Se-Na reduces from 3.09 Å to 3.05 Å as adsorption of 2L through 8L take place.

The values of average adsorption energy, adsorption energy of layer, electrode voltage and volume expansion are tabulated in Table 3 for different Na concentration and respective specific capacity. It is observed that with increase in Na concentration, average adsorption energy of Na atom and layer adsorption energy decreases gradually from $-1.520$ eV to $-1.329$ eV and to $-1.299$ eV, respectively. This is attributed to weak electrostatic interaction between Na atoms and the alloy as well as enhanced Na-Na repulsion at high concentrations. This indicates that structure is quite stable even at high Na concentrations with adsorption energy of Na greater than cohesive energy of bulk Na ($-1.113$ eV), preventing the formation of cluster [51]. In experimental setup, these theoretically predicted capacities could be smaller due to several reasons like defects, reaction of electrode with electrolyte, which are not considered in DFT calculations. Also, it is worth noting that there are no structural changes or phase transformations during sodiation process and hence long-term stability is anticipated.

### Table 4
Comparison of electrochemical properties predicted by DFT calculations for various other similar materials.

<table>
<thead>
<tr>
<th>System</th>
<th>Max. capacity (mA h g⁻¹)</th>
<th>Anode voltage (V)</th>
<th>Diffusion barrier (eV)</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>MoSSe alloy</td>
<td>1036</td>
<td>1.5–0.14</td>
<td>0.035, 0.052</td>
<td>This work</td>
</tr>
<tr>
<td>Bulk MoS₂</td>
<td>190</td>
<td>1.7–2.0</td>
<td>0.70</td>
<td>[40]</td>
</tr>
<tr>
<td>Layered MoS₂</td>
<td>146</td>
<td>0.75</td>
<td>0.68</td>
<td>[41]</td>
</tr>
<tr>
<td>Monolayer MoS₂</td>
<td>335</td>
<td>1.00</td>
<td>0.11</td>
<td>[40]</td>
</tr>
<tr>
<td>VS₂</td>
<td>232.91</td>
<td>1.30</td>
<td>0.085</td>
<td>[52]</td>
</tr>
<tr>
<td>TiS₂, ZrS₂, NbS₂</td>
<td>260–339</td>
<td>0.74–0.95</td>
<td>0.07, 0.22</td>
<td>[53]</td>
</tr>
<tr>
<td>Defected-Stanene</td>
<td>362.8</td>
<td>1.99–1.29</td>
<td>0.15</td>
<td>[54]</td>
</tr>
<tr>
<td>Graphene</td>
<td>762</td>
<td>0.44</td>
<td>0.16, 0.22</td>
<td>[55]</td>
</tr>
<tr>
<td>Borophene</td>
<td>1640</td>
<td>1.5–0.2</td>
<td>0.34</td>
<td>[56]</td>
</tr>
<tr>
<td>MoS₂/Borophene</td>
<td>539</td>
<td>1.6–0.03</td>
<td>0.010, 0.30, 0.35</td>
<td>[58]</td>
</tr>
<tr>
<td>MoS₂/VS₂</td>
<td>584</td>
<td>1.4–0.4</td>
<td>0.44, 0.10, 0.13</td>
<td>[59]</td>
</tr>
<tr>
<td>Borophane</td>
<td>504</td>
<td>0.03</td>
<td>0.09, 0.37</td>
<td>[57]</td>
</tr>
<tr>
<td>MoS₂/Ti₂CO₂</td>
<td>447</td>
<td>0.52</td>
<td>0.36</td>
<td>[60]</td>
</tr>
<tr>
<td>MoS₂/Ti₂CF₂</td>
<td>438</td>
<td>0.20</td>
<td>0.37</td>
<td>[60]</td>
</tr>
</tbody>
</table>

### 3.4. Comparison with other anode materials

While MoSSe alloy exhibits excellent electrochemical characteristics as anode for SIBs, bulk MoS₂ [40] and layered MoS₂ [41] possess maximum capacity of 190 mA h g⁻¹ and 146 mA h g⁻¹ with high diffusion barriers of 0.70 eV and 0.68 eV, and high anode voltage range. Compared with monolayer MoS₂ [40], this alloy shows better performance in every respect, as summarized in Table 4. Many similar 2D materials such as VS₂ [52] TiS₂, ZrS₂, NbS₂ [53], stanene [54], graphene [55], borophene [56], borophane [57], as well as heterostructures of MoS₂ based heterostructures such as MoS₂/borophene [58], MoS₂/VS₂ [59], MoS₂/Ti₂CO₂ and MoS₂/Ti₂CF₂ [60], have been explored as sodium anode material. 2D materials such as, VS₂, TiS₂,

$ZrS_2$, $NbS_2$ and defected-stanene exhibit low diffusion barrier but not much improvement in charge capacity and anode voltage are observed. Light-weighted materials like graphene, borophene, $MoS_2$/Borophene, and $MoS_2$/VS$_2$ have been reported to possess improved specific capacity, low anode voltage and low diffusion barrier but there is no mention about volume expansion of the material. There have been reports on borophane, $MoS_2$/Ti$_2$CO$_2$ and $MoS_2$/Ti$_2$CF$_2$ exhibiting high mechanical strength for bearing volume expansion but possess insufficient charge capacity and moderate diffusion barrier, which are necessary for large-scale application of SIBs.

## 4. Conclusions

In summary, DFT calculations are employed to explore MoSSe alloy to be used as an anode material in SIBs for large scale application. Our results suggest that introduction of selenium content has enhanced conductivity of pristine $MoS_2$. AIMD simulations suggest that there is no structural damage of the alloy even at high temperature. The improved conductivity is responsible for smooth electron transport and diffusion of Na ion, ensuring improved diffusion kinetics of MoSSe alloy as compared to monolayer $MoS_2$ and layered $MoS_2$. The low energy barriers for Na ion diffusion over the surface of alloy is calculated to be 0.035 eV for the Se side and 0.052 eV for the S side, indicating fast mobility. This is due to strong Coulomb interactions of Na with S as compared to Se. With stable adsorption of eight layers of Na atoms on MoSSe monolayer, high theoretical capacity of 1036 mA h g$^{-1}$ and low electrode (anode) voltage range of 1.52–0.14 V are achieved. Very importantly, the alloy can withstand large volume expansion without breaking attributed to the high Young's modulus and ultimate strain of MoSSe alloy. Despite the practical challenges, such as cell design and electrode balancing remain, we expect that the results may provide new prospects to enhance the electrochemical performance of existing anode materials.

### CRediT authorship contribution statement

**Archana Sharma:** Methodology, Software, Visualization, Investigation, Validation, Writing - original draft. **Mohd. Shahid Khan:** Supervision, Writing - review & editing. **Md. Shahzad Khan:** Visualization, Investigation. **Mushahid Husain:** Conceptualization, Resources.

### Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Acknowledgements

All authors thank Jamia Millia Islamia, New Delhi, India, for providing computational support. Archana Sharma acknowledges University Grants Commission (UGC), India for Basic Scientific Research (BSR) Fellowship.

### References

[1] B. Dunn, H. Kamath, J.-M. Tarascon, Electrical energy storage for the grid: a battery of choices, Science 334 (2011) 928–935.
[2] H. Pan, Y.-S. Hu, L. Chen, Room-temperature stationary sodium-ion batteries for large-scale electric energy storage, Energy Environ. Sci. 6 (2013) 2338–2360.
[3] Y. Nishi, Lithium ion secondary batteries; past 10 years and the future, J. Power Sources. 100 (2001) 101–106.
[4] E. de la Llave, V. Borgel, K.J. Park, J.-Y. Hwang, Y.-K. Sun, P. Hartmann, F.F. Chesneau, D. Aurbach, Comparison between Na-ion and Li-ion cells: Understanding the critical role of the cathodes stability and the anodes pretreatment on the cells behavior, ACS Appl. Mater. Interfaces 8 (2016) 1867–1875.
[5] N. Yabuuchi, K. Kubota, M. Dahbi, S. Komaba, Research development on sodium-ion batteries, Chem. Rev. 114 (2014) 11636–11682.
[6] M.D. Slater, D. Kim, E. Lee, C.S. Johnson, Sodium-ion batteries, Adv. Funct. Mater. 23 (2013) 947–958.
[7] T.B. Reddy, D. Linden, Linden's Handbook of Batteries, fourth ed., McGraw-Hill, 2010.
[8] D.A. Stevens, J.R. Dahn, High capacity anode materials for rechargeable sodium-ion batteries, J. Electrochem. Soc. 147 (2000) 1271.
[9] J. Hafner, C. Wolverton, G. Ceder, Guest editors, toward computational materials design: the impact of density functional theory on materials research, MRS Bull. 31 (2006) 659–665.
[10] Y.S. Meng, M.E.A. Dompablo, First principles computational materials design for energy storage materials in lithium ion batteries, Energy Environ. Sci. 2 (2009) 589–609.
[11] X. Shao, K. Wang, R. Pang, X. Shi, Lithium intercalation in graphene/MoS$_2$ composites: first-principles insights, J. Phys. Chem. C. 119 (2015) 25860–28567.
[12] S. Goriparti, E. Miele, F. Angelis, E. Fabrizio, R.P. Zaccaria, C. Capiglia, Review on recent progress of nanostructured anode materials for Li-ion batteries, J. Power Sources. 257 (2014) 421–443.
[13] S. Mukherjee, G. Singh, Two-dimensional anode materials for non-lithium metal-ion batteries, ACS Appl. Energy Mater. 2 (2019) 932–955.
[14] A. Jain, B.J. Paul, S. Kim, V.K. Jain, J. Kim, A.K. Rai, Two dimensional porous nanodisks of NiCo$_2$O$_4$ as anode material for high performance rechargeable lithium-ion battery, J. Alloys Compd. 772 (2019) 72–79.
[15] L. Peng, Y. Zhu, D. Chen, R.S. Ruoff, G. Yu, Two-dimensional materials for beyond-lithium-ion batteries, Adv. Energy Mater. 6 (2016) 1600025.
[16] A. Sharma, M.S. Anu, M.K.M.S. Husain, A.S. Khan, Sensing of CO and NO on Cu-doped $MoS_2$ monolayer based single electron transistor, IEEE Sens. J. 18 (7) (2018) 2853–2860.
[17] A. Sharma, A. Srivastava, M. Husain, M.S. Khan, Computational investigations of Cu-embedded $MoS_2$ sheet for CO oxidation catalysis, J. Mater. Sci. 53 (2018) 9578–9588.
[18] A. Sharma, M.S. Khan, M. Husain, Adsorption of phosgene on Si-embedded $MoS_2$ sheet and electric field-assisted desorption: insights from DFT calculations, J. Mater. Sci. 54 (2019) 11497–11508.
[19] J. Xiao, D. Choi, D.L. Cosimbescu, P. Koech, J. Liu, J.P. Lemmon, Exfoliated $MoS_2$ nanocomposite as an anode material for lithium ion batteries, Chem. Mater. 22 (2010) 4522 – 4524.
[20] H. Hwang, H. Kim, J. Cho, $MoS_2$ nanoplates consisting of disordered graphene-like layers for high rate lithium battery anode materials, Nano Lett. 11 (2011) 4826–4830.
[21] D. Su, S. Dou, G. Wang, Ultrathin $MoS_2$ nanosheets as anode materials for sodium-ion batteries with superior performance, Adv. Energy Mater. 5 (2014) 1401205-1–6.
[22] X. Xie, Z. Ao, D. Su, J. Zhang, G. Wang, $MoS_2$/graphene composite anodes with enhanced performance for sodium-ion batteries: the role of the two-dimensional heterointerface, Adv. Funct. Mater. 25 (2015) 1393–1403.
[23] A.Y. Lu, H. Zhu, J. Xiao, C.P. Chuu, Y. Han, M.H. Chiu, C.C. Cheng, C.W. Yang, K.H. Wei, Y. Yang, Y. Wang, D. Sokaras, D. Nordlund, P. Yang, D.A. Muller, M.Y. Chou, X. Zhang, L.J. Li, Janus monolayers of transition metal dichalcogenides, Nat. Nanotechnol. 12 (2017) 744–749.
[24] J. Zhang, S. Jia, I. Kholmanov, L. Dong, D. Er, W. Chen, H. Guo, Z. Jin, V.B. Shenoy, L. Shi, J. Lou, Janus monolayer transition-metal dichalcogenides, ACS Nano 11 (2017) 8192–8198.
[25] R. Li, Y. Cheng, W. Haung, Recent progress of janus 2D transition metal chalcogenides: from theory to experiments, Small 14 (2018) 1802091.
[26] G. Kresse, J. Furthmuller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B. 54 (1996) 11169.
[27] J. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865–3868.
[28] MedeA, Materials Design, http://www.materialsdesign.com.
[29] P. Blochl, Projector augmented-wave method, Phys. Rev. B. 50 (1994) 17953.
[30] H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integration, Phys. Rev. B. 13 (1976) 5188–5192.
[31] S. Grimme, Semiempirical GGA-type density functional constructed with a long-range dispersion correction, J. Comput. Chem. 27 (2006) 1787–1799.
[32] G. Henkelman, B.P. Uberuaga, H. Jonsson, A climbing image nudged elastic band method for finding saddle points and minimum energy paths, J. Chem. Phys. 113 (2000) 9901–9904.
[33] B. Peng, F. Cheng, Z. Tao, J. Chen, Lithium transport at silicon thin film: Barrier for high-rate capability anode, J. Chem. Phys. 133 (2010) 034701.
[34] K. Tibbetts, C.R. Miranda, Y.S. Meng, G. Ceder, An ab initio study of lithium diffusion in titanium disulfide nanotubes, Chem. Mater. 19 (2007) 5302–5308.
[35] L. Dong, J. Lou, V.B. Shenoy, Large in-plane and vertical piezoelectricity in janus transition metal dichalcogenides, ACS Nano 11 (2017) 8242–8248.
[36] L. Li, Y. Zheng, S.L. Zhang, J.P. Yang, Z.P. Shao, Z.P. Guo, Recent progress on sodium ion batteries: potential high-performance anodes, Energy Environ. Sci. 11 (2018) 2310–2340.
[37] S. Bertolazzi, J. Brivio, A. Kis, A. Stretching and Breaking of Ultrathin MoS2. ACS Nano. 5 (2011) 9703 – 9709.
[38] Y. Gan, H. Zhao, Chirality effect of mechanical and electronic properties of monolayer $MoS_2$ with vacancies, Phys. Lett. A. 78 (2014) 2910–2914.
[39] G. Henkelman, A. Arnaldsson, H. Jonsson, Comput. Mater. Sci. 3 (2006) 354.
[40] J. Su, Y. Pei, Z. Yang, X. Wang, Ab initio study of graphene-like monolayer molybdenum disulfide as a promising anode material for rechargeable sodium ion batteries, RSC Adv. 4 (2014) 43183–43188.
[41] M. Mortazavi, C. Wang, J. Deng, V.B. Shenoy, N.V. Medhekar, Ab initio

characterization of layered $MoS_2$ as anode for sodium-ion batteries, J. Power Sources. 268 (2014) 279-286.

[42] M. Aydinol, A. Kohan, G. Cedar, K. Cho, J. Joannopoulos, *Ab initio* study of lithium intercalation in metal oxides and metal dichalcogenides, Phys. Rev. B. 56 (1997) 1354-1365.

[43] M. Aydinol, A. Kohan, G. Cedar, *Ab initio* calculation of the intercalation voltage of lithium-transition-metal oxide electrodes for rechargeable batteries, J. Power Sources. 68 (1997) 664-668.

[44] I.-H. Chu, M. Zhang, S.P. Ong, Y.S. Meng, Battery Electrodes, Electrolytes, and Their Interfaces, in: W. Andreoni, S. Yip (Eds.), In Handbook of Materials Modeling, Springer Nature, Switzerland AG, 2018, pp. 1-24.

[45] D. Er, J. Li, M. Naguib, Y. Gogotsi, V.B. Shenoy, $Ti_3C_2$ MXene as a high capacity electrode material for metal (Li, Na, K, Ca) ion batteries, ACS Appl. Mater. Interfaces 6 (2014) 11173-11179.

[46] D. Wang, Y. Liu, X. Meng, Y. Wei, Y. Zhao, Q. Pang, G. Chen, Two-dimensional $VS_2$ monolayers as potential anode materials for lithium-ion batteries and beyond: first-principles calculations, J. Mater. Chem. A. 5 (2017) 21370-21377.

[47] A. Eftekharia, Energy Storage Mater. 7 (2017) 157-180.

[48] M.D. Slater, D. Kim, E. Lee, C.S. Johnson, Adv. Funct. Mater. 23 (2013) 947-958.

[49] L. Wang, X. Zhang, L. Deng, J. Tang, H. Deng, W. Hu, Z. Liu, Revealing the reaction mechanism of sodium selenide confined within a single-walled carbon nanotube: implications for Na-Se batteries, ACS Appl. Mater. Interfaces 11 (2019) 4995-5002.

[50] P.J. Mohan, A. Datta, S.K. Pati, Structure and bonding in M-X-M systems (M = Li, Na and K; X = O, S): Effects of charge-transfer, J. Comput. Methods Sci. Eng. 7 (2007) 489-494.

[51] Charles Kittel, Introduction to Solid State Physics, eighth ed., John Wiley & Sons Inc, Hoboken, NJ, 2005, p. 50.

[52] D.B. Putungan, S.-H. Lin, J.-L. Kuo, Metallic $VS_2$ monolayer polytypes as potential sodium-ion battery anode via *ab initio* random structure searching, ACS Appl. Mater. Interfaces 8 (2016) 18754-18762.

[53] E. Yang, H. Ji, Y. Jung, Two-dimensional transition metal dichalcogenide monolayers as promising sodium ion battery anodes, J. Phys. Chem. C. 119 (2015) 26374-26380.

[54] L. Wu, P. Lu, R. Quhe, Q. Wang, C. Yang, P. Guan, K. Yang, Stanene nanomeshes as anode materials for Na-ion batteries, J. Mater. Chem. A. 6 (2018) 7933-7941.

[55] C. Ling, F. Mizuno, Boron-doped graphene as promising anode for Na-ion batteries, Phys. Chem. Chem. Phys. 16 (2014) 10419-10424.

[56] B. Mortazavi, O. Rahamana, S. Ahzi, T. Rabczuk, Flat borophene films as anode materials for Mg, Na or Li-ion batteries with ultra high capacities: A first-principles study, Appl. Mater. Today 8 (2017) 60-67.

[57] N.K. Jena, R.B. Araujo, V. Shukla, R. Ahuja, Borophane as a benchmate of graphene: A potential 2D material for anode of Li and Na-ion batteries, ACS Appl. Mater. Interfaces 9 (2017) 16148-16158.

[58] P. Xiang, X. Chen, J. Liu, B. Xiao, L. Yang, Borophene as conductive additive to boost the performance of $MoS_2$-based anode materials, J. Phys. Chem. C. 122 (2018) 302-9311.

[59] A. Samad, Y.-H. Shin, $MoS_2@VS_2$ nanocomposite as a superior hybrid anode material, ACS Appl. Mater. Interfaces. 9 (2017) 29942-29949.

[60] J. Li, Q. Peng, J. Zhou, Z. Sun, $MoS_2/Ti_2CT_2$ (T = F, O) heterostructures as promising flexible anodes for lithium/sodium ion batteries, J. Phys. Chem. C. 123 (2019) 11493-11499.