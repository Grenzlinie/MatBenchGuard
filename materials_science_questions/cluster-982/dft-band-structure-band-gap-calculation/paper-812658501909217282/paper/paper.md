Physical Chemistry Chemical Physics

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: J. Lang and Y. H. Hu, *Phys. Chem. Chem. Phys.*, 2020, DOI: 10.1039/D0CP00637H.

![](./images/812658501909217282_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/812658501909217282_2.jpg)

rsc.cc/pccp

ARTICLE

# Phosphorus-Based Metal-Free Z-scheme 2D van der Waals Heterostructures for Visible-Light Photocatalytic Water Splitting: a First-Principles Study

Junyu Lang, $^{a}$ and Yun Hang Hu $^{*ab}$

Direct splitting of water over semiconductor under sunlight irradiation would be a promising approach for hydrogen production and solar energy utilization. In this work, a BlueP/PN with 2D van der Waals (vdW) heterostructure is proposed as a novel catalyst for the Z-scheme photocatalytic system. Its electronic structures, optical properties, and combined configuration were systematically evaluated by hybrid density functional theory (DFT) calculations. It was revealed that the 2D vdW heterostructure of BlueP/PN can play an important role in water splitting under visible light irradiation. This predicts a novel design of P-based vdW heterostructures for efficient photocatalysts.

## Introduction

Solar-to-Hydrogen (STH) is a promising approach to storing the infinite solar energy in the form of chemical energy. In particular, photocatalytic splitting of water into hydrogen implements a complete conversion from photo energy to chemical energy including light harvest, energy transfer and energy storage. $^{1-5}$ Photocatalysts are essential for the splitting and most of them are semiconductors. When a semiconductor is excited by light, the photogenerated electron-hole pairs react with the water molecule to yield hydrogen and oxygen. The catalytic efficiency is restrained by the light absorption and charges separation of the semiconductor. The band structure of the photocatalyst determines not only the redox potential of the photogenerated carriers, but also the ability of light absorption. Intensive efforts have been made to develop photocatalysts with an expanded light absorption region due to their narrow bandgaps, such as $WO_3^6$, $BiVO_4^7$, $AgNbO_3^8$, black $TiO_2^9$, $Sm_2Ti_2S_2O_5^{10}$, $g$-$C_3N_4^{11}$, Black $P^{12}$, and $TaON^{13}$. Furthermore, doping semiconductors with metal/non-metal can decrease the bandgap. $^{14-17}$

However, although narrowing the bandgap can enlarge spectral response, it weakens the redox potential to decrease the photoelectron activity. Constructing the Z-scheme photocatalytic system is an ideal way to achieve maximal light absorption without sacrifice of the activity of photoelectrons. $^{18-20}$ Moreover, the heterostructure can substantially accelerate the charge separation to improve the efficiency of photoconversion. An efficient Z-scheme photocatalytic system must meet the following three requirements: (1) its two parts can yield the photogenerated electron and the hole at the same time, (2) the band alignment of the two parts must distribute crossly, and (3) the photoelectron from one part must be ease to combine the hole from another part, enhancing the charge separation.

Recently, novel van der Waals (vdW) heterostructures that consist of different 2D materials attracted extensive attention due to its unique electronic properties. $^{21-23}$ Compared to bulk materials, 2D materials have advantages in photocatalytic water splitting such as remarkable specific surface area, carrier mobility, controllable interfaces, and so on. $^{24-25}$ For instance, transition metal dichalcogenides$^{26}$, MXenes$^{27}$, black phosphorene$^{28}$, $g$-$C_3N_4^{29}$ and others have been widely used due to their outstanding performance.

Blue phosphorene (BlueP) has been successfully synthesized through molecular beam epitaxial growth on an Au (111) substrate by black phosphorus as a precursor. $^{30}$ It has attracted intense research interest due to its superb properties such as sizable bandgap and ultra-high mobility.$^{30-31}$ It has been expected to have potential applications, such as superconductor electrode$^{32}$, thermoelectric material$^{33}$, anodes for lithium-ion batteries$^{34}$, gas sensors$^{35, 36}$, photocatalysts$^{37, 38}$ and metal-oxide-semiconductor field-effect transistors (MOSFETs)$^{39, 40}$. Furthermore, theoretical studies have explored the stability and electronic characteristics of its 2-dimensional structures.$^{31, 41}$ Particularly, blue-phosphorene-based vdW heterostructures have attracted increasing interest due to their extraordinary electronic and optical properties. Most recently, numerous BlueP-based heterostructures, such as boron phosphide/blue phosphorus,$^{42}$ BlueP/TMDCs,$^{43,44}$ BlueP/Graphene,$^{45}$ and BlueP/MXene$^{46}$ heterostructures, have been fabricated and evaluated. More interestingly, the BlueP/AlN heterostructure exhibits suitable band edge positions for the redox potentials of water, which makes it a potential photocatalyst for water splitting.$^{47}$ A BlueP/BSe interlayer heterostructure possesses an indirect gap and

$^{a}$ School of Environmental Science and Engineering, Shanghai Jiao Tong University, Shanghai 200240, P. R. China. E-mail: yunhangh@mtu.edu
$^{b}$ Department of Materials Science and Engineering, Michigan Technological University, Houghton, Michigan 49931, United States.

intrinsic type-II band alignment. In particular, this heterostructure material is considered as a potential photocatalyst for water splitting with enhanced optical properties in the visible and ultraviolet light zones.⁴⁸ This situation encouraged us to propose the 2D BlueP and PN monolayers as photocatalysts for the hydrogen evolution reaction (HER) and oxygen evolution reaction (OER), respectively, in this work. Furthermore, DFT calculations were employed to evaluate the structural and electronic properties of the 2D vdW heterojunctions BlueP/PN and its potential application in the Z-scheme photocatalytic water splitting. It was demonstrated that BlueP/PN heterojunctions would be efficient Z-scheme photocatalysts for water splitting under visible light irradiation due to their suitable band alignments.

## Methods
The model of BlueP is built according to previous report⁴⁹, which belongs to trigonal system. There are two P atoms in a unit cell with a latticed constant of 3.31 Å. The monolayer PN, which origins from r-PN, possesses the symmetry group of P3M1. The BlueP and PN monolayers were evaluated by DFT calculation with periodic boundary conditions using the Vienna Ab initio Simulation Package (VASP). Projector-augmented-wave (PAW) methods for P and N atoms were employed to examine the electro-static interactions between valence and core electrons. The geometrical optimization and electronic structure calculations were implemented using the Generalized Gradient Approximation (GGA) of Perdew, Burke, and Ernzerhof (PBE) functionals. In particular, band structures are computed based on the Heyd-Scuseria-Ernzerh of hybrid functional (HSE06) to correct the underestimated bandgaps in PBE. All of the atoms in the primitive cell were completely relaxed until none of the forces exceeded 0.01 eV Å⁻¹. The Brillouin zone was sampled by using a 21 × 21 × 1 Monkhorst-Pack k-point mesh in PBE and 7 × 7 × 1 k-point in HSE06. A large vacuum layer of 20 Å was used to prevent the artificial interlayer interaction. The long-range effect of van der Waals force was considered by applying DFT-D2 method of Grimme. The plane-wave cut off energy was set as 500 eV. A large supercell model was used to calculate the Gibbs free energy of hydrogen adsorption ($\Delta G_{H*}$). The BlueP, PN and BlueP/PN heterostructure were enlarged to 4 × 4, 5 × 5, and 2 × 2 supercell, respectively, which ensure the distance of H atoms in the adjacent cell is larger than 10 Å. The Gibbs free energy is calculated by the following equation:

$$
\Delta G_{H*} = \Delta E_{H*} + \Delta E_{ZPE} - T\Delta S, \tag{1}
$$

$\Delta E_{H*}$, $\Delta E_{ZPE}$ and $\Delta S$ are the adsorption energy of H, zero-point energy variation and entropy variation in H adsorption process, respectively. $\Delta E_{H*}$ is equal to the energy difference before and after adsorption of hydrogen as follows:

$$
\Delta E_{H*} = E_{Total} - E_{sueface} - \frac{1}{2}E_{H_2}, \tag{2}
$$

Although various H adsorption sites were pre-examined using eq (2), the most stable structure was selected as model for the HER calculation. $E_{ZPE}$ values of H* and H₂ were obtained from vibrational frequency calculations. $\Delta S$ is approximately equal to $-1/2S_{H_2}$ because the vibrational entropy can be neglected.

## Results and discussion
DFT calculations were exploited to evaluate the structure and electronic properties of BlueP and PN. The geometric structures of monolayer BlueP and PN were fully optimized and shown in Figs. 1a and 1b, respectively. The lattice constants of BlueP and PN calculated from GGA-PBE are 3.314 and 2.692 Å, which are in good agreement with the values of previous studies.⁴⁹,⁵⁰ This confirms the feasibility of the calculation approach. Monolayer BlueP, in which the bond length of P-P is 2.27 Å, belongs to P-3M1 symmetry group. In contrast, the monolayer PN, which origins from r-PN, possesses the symmetry group of P3M1. The similar shape of their cells can allow them to form the vdW 2D/2D heterostructure. Although 2D BlueP and PN have the same angle between the cell edges, they have different lattice constants, leading to 10.3% mismatch between PN and BlueP.

![](./images/812658501909217282_3.jpg)

Fig. 1 Atomic structure model of monolayer BlueP (a) and PN (b).

The BlueP/PN heterostructure possesses three different types of configuration: (I) averaging their lattice constants to form a point-to-point structure, (II) grabbing a repeated unit with similar shape and suitable size to combine with a super cell and (III) resizing the scale of the cell by multiple super cell method to create BlueP/PN heterostructure (Fig. 2). In type (I) configuration, the match level between the lattice is the primary consideration. The P atom and the N atom in PN are one-by-one corresponding to the P atom in BlueP, which needs a strong horizontal force to maintain the structural stability. However, the 2D/2D vdW hetrostructure is constructed by van der Waals interaction, which is not strong enough to squeeze the structure in the horizontal direction. The thermodynamic stability of 2D/2D vdW heterostructure was evaluated by the formation energy as follows:

$$
E_{form} = \frac{E_{BP/PN}^{Total}-n*E_{BP}^{Total}-m*E_{PN}^{Total}}{A}, \tag{3}
$$

where $E_{BP/PN}^{Total}$, $E_{BP}^{Total}$, and $E_{PN}^{Total}$ are the total energy of BlueP/PN heterostructure, monolayer BlueP, and monolayer PN, respectively; $n$ and $m$ are the numbers of BlueP and PN unit cell used to build BlueP/PN heterostructure; $A$ is the x-y cross-sectional area of the interface in BlueP/PN heterostructure. In

type (I) configuration, the BlueP unites with PN in different positions including translation and rotation to form variety BlueP/PN heterostructures (Table 1). The formation energy for type (I) configuration is in the range of 0.045 ~ 0.127 eV/Å². The positive value of formation energy indicates its poor thermodynamic stability. In type (II), a periodic repeated unit can be grabbed from the 2D plane of PN, which consists of 4 P and 4 N atoms. The size of the unit is close to the 2 × 2 super cell of BlueP, which is able to construct vdW heterostructure with less mismatch. Considering the relative position of the two layers, four possible models of BlueP/PN heterostructures were built. The most stable structure is II-1 with formation energy of -0.038 eV/Å². On the other hand, 4 × 4 super cell of BlueP and 5 × 5 super cell of PN can form BlueP/PN heterostructure with a mismatch of 0.75%. Thus, II-1 model was selected for the following further evaluations.

![](./images/812658501909217282_4.jpg)

Fig. 2 Three different types of BlueP/PN heterostructures.

<table>
<caption>Table 1. Formation energies of all possible BlueP/PN models.</caption>
<tbody>
<tr>
<td>
BlueP/PN (I-1)
<br>a=3.036 Å α=120.1°
<br>d=4.005 Å E<sub>form</sub>=0.126 eV/Å²
<br>![](./images/812658501909217282_5.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (I-2)
<br>a=3.090 Å α=120.1°
<br>d=2.168 Å E<sub>form</sub>=0.085 eV/Å²
<br>![](./images/812658501909217282_6.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (I-3)
<br>a=3.079 Å α=119.9
<br>d=3.101 Å E<sub>form</sub>=0.113 eV/Å²
<br>![](./images/812658501909217282_7.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (I-4)
<br>a=3.034 Å α=120.0°
<br>d=3.751 Å E<sub>form</sub>=0.127 eV/Å²
<br>![](./images/812658501909217282_8.jpg)
<br>Top view Side view
</td>
</tr>
<tr>
<td>
BlueP/PN (I-5)
<br>a=3.376 Å α=119.3°
<br>d=2.434 Å E<sub>form</sub>=0.047 eV/Å²
<br>![](./images/812658501909217282_9.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (I-6)
<br>a=3.372 Å α=119.3°
<br>d=2.383 Å E<sub>form</sub>=0.045 eV/Å²
<br>![](./images/812658501909217282_10.jpg)
<br>Top view Side view
</td>
<td colspan="2"></td>
</tr>
<tr>
<td>
BlueP/PN (II-1)
<br>a=5.486 Å α=120.0°
<br>d=3.907 Å E<sub>form</sub>=-0.038 eV/Å²
<br>![](./images/812658501909217282_11.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (II-2)
<br>a=5.487 Å α=120.0°
<br>d=3.811 Å E<sub>form</sub>=-0.034 eV/Å²
<br>![](./images/812658501909217282_12.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (II-3)
<br>a=5.487 Å α=120.0°
<br>d=4.103 Å E<sub>form</sub>=-0.032 eV/Å²
<br>![](./images/812658501909217282_13.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (II-4)
<br>a=5.485 Å α=120.0°
<br>d=4.123 Å E<sub>form</sub>=-0.032 eV/Å²
<br>![](./images/812658501909217282_14.jpg)
<br>Top view Side view
</td>
</tr>
<tr>
<td>
BlueP/PN (III-1)
<br>a=13.487 Å α=120.0°
<br>d=3.715 Å E<sub>form</sub>=-0.033 eV/Å²
<br>![](./images/812658501909217282_15.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (III-2)
<br>a=13.438 Å α=120.0°
<br>d=3.510 Å E<sub>form</sub>=-0.034 eV/Å²
<br>![](./images/812658501909217282_16.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (III-3)
<br>a=13.440 Å α=120.0°
<br>d=3.409 Å E<sub>form</sub>=-0.035 eV/Å²
<br>![](./images/812658501909217282_17.jpg)
<br>Top view Side view
</td>
<td>
BlueP/PN (III-4)
<br>a=13.442 Å α=120.0°
<br>d=3.493 Å E<sub>form</sub>=-0.035 eV/Å²
<br>![](./images/812658501909217282_18.jpg)
<br>Top view Side view
</td>
</tr>
</tbody>
</table>


ARTICLE

The band structures of BlueP and PN are examined and shown in Fig.3. The band gaps from PBE calculation are 1.77 and 0.80 eV for BlueP and PN, respectively, which are smaller than the previous studies.⁴²·⁵⁰ Therefore, a more accurate approach, "the hybrid functional HSE06 model", was used employed for the evaluation of band structures. The HSE06 calculations showed that both of monolayer BlueP and PN are indirect semiconductors. BlueP's bandgap value, which is the difference between the valence band maximum (VBM located between Γ and K points) and the conduction band minimum (CBM located between Γ and M points), is 2.64 eV. This is close to the value of other studies (2.7 eV).⁴²·⁴⁴ 2D PN also possesses an indirect band structure with a bandgap of 1.86 eV.

The band alignment of the two components plays an important role in a Z-scheme photocatalyst. Using the vacuum level ($E_{vac}$) as reference, the work function ($\Phi$) has the following relationship with the Fermi level ($E_f$):

$$
\Phi = E_{vac} - E_f, \tag{4}
$$

The work functions of BlueP and PN, which were calculated from a local potential along the vertical direction of the 2D plane, are 7.5 eV and 6.8eV, respectively (Fig. 4).

![](./images/812658501909217282_19.jpg)

Fig. 3 Band structures and DOS of BlueP (a) and PN (b) calculated with HSE06 (black line) and PBE (red line).

![](./images/812658501909217282_20.jpg)

Fig. 4 Calculated electrostatic potentials alone the Z direct of BlueP (a) and PN (b).

When BlueP was combined with PN, electrons would flow from PN to BlueP, which was driven by the difference between their Fermi levels after alignment, until this gap disappeared. Consequently, the BlueP layer and PN layer were charged to form a build-in electric field. After aligning the band structure, the CBM and VBM of BlueP become higher than those of PN. The relative positions of CBM and VBM are suitable for the construction of 2D/2D BlueP/PN Z-scheme photocatalyst. Furthermore, BlueP and PN can be synchronously triggered by visible light due to their narrow band gap. The final factor determining whether the BlueP and PN could make up Z-scheme system is the charge transfer behavior between BlueP and PN. The charge density difference was employed to reveal the change of charge spatial distribution after constructing the BlueP/PN heterojunction. The difference of interface charge density from two individual parts was calculated as the follows:

$$
\Delta \rho = \rho_{BP/PN} - \rho_{BP} - \rho_{PN}, \tag{5}
$$

where $\rho_{BlueP/PN}$, $\rho_{BlueP}$ and $\rho_{PN}$ represent the charge density of BlueP/PN, BlueP, and PN, respectively. Fig. 5a shows the electron accumulation and depletion, which are represented by yellow and blue parts, respectively. In the interface region, the yellow area mainly dispensed near the BlueP surface and the blue area covered the surface of PN. The xy-planar-averaged differential charge density was calculated and presented in Fig.5b. It was found that, in the interface region, the electrons were concentrated at the surface of BlueP, leading to its negatively charged feature. In contrast, the electric density of the PN surface decreased to generate holes with positive charge. The electron transfer from PN to BlueP was further demonstrated by the work function analysis. As discussed above, when the monolayer PN nanosheet interacted with the monolayer BlueP nanosheet to form BlueP/PN heterostructure, electron transfer occurred in the interface region until two Fermi energy reached the same level. Furthermore, the amount of transferred electrons could be obtained from planar-averaged electrostatic potential along the Z axis for the

BlueP/PN heterostructure (Fig. 5b). The amount of transferred charge ($\Delta$Q) was obtained by integral of the $\Delta\rho$ from -$\infty$ to Z. A total of 0.0004 e charge was transferred from the PN to the BlueP layer in a single unit of BlueP/PN. The Fermi energy of BlueP/PN heterostructure was -6.13 eV with respect to the vacuum level (Fig. 5c). A 7.99 eV potential drop ($\Delta$V$_H$) across the interface indicates that the excitonic behavior of the BlueP/PN heterostructure is very far from that of the individual BlueP sheet or PN sheet. The potential drop can drive the separation of electrons and holes by the incline of the potential between BlueP and PN.

![](./images/812658501909217282_21.jpg)

Fig. 5 (a) 3D isosurface of differential charge density for BlueP/PN heterojunction, (b) The xy-planar-averaged differential charge density (black line) along z axis, and the plane-integrated differential electron density (red line), and (c) Calculated electrostatic potentials alone the Z direct of BlueP/PN (the electron accumulation and depletion are represented by yellow and blue color, respectively)

The band structure of BlueP/PN was calculated by HSE06 hybrid functional model. As shown in Fig. 6, different from monolayer PN and the BlueP that possess indirect band gaps, the BlueP/PN heterostructure has a typical direct band gap of 1.3 eV. The VBM and CBM of BlueP/PN heterostructure, which are located at the $\Gamma$ point, mainly derive from BlueP and PN, respectively. The total density of states (TDOS) and the partial density of states (PDOS) of BlueP/PN vdW heterostructure were also calculated using the HSE06 hybrid functional method. Fig. 7 shows that the VBM of BlueP/PN vdW heterostructure is mainly composed of P 2p orbitals, whereas the CBM of the BlueP/PN vdW heterostructure is dominated by N 2p orbitals. However, it is hardly to achieve the excitation from the P 2p to N 2p, because the P atoms in BlueP and the N atoms in PN near the interface are both in saturated coordination and the vdW force is not strong enough to create a localized state in the forbidden band.

![](./images/812658501909217282_22.jpg)

Fig. 6 The electronic band structure of BlueP/PN vdW heterostructure using HSE06 method, with partitioned band structure of BlueP and PN.

The energy band levels (VBM and CBM) of BlueP and PN are interlaced with each other when they constitute the 2D BlueP/PN vdW heterostructure. BlueP possesses the VBM potential of 2.57 V and the CBM potential of 0.19 V (vs NHE). For PN, the VBM potential is 1.97 V and the CBM potential 0.79 V (vs NHE). Both of them can produce electrons and holes in their CB and VB under visible light irradiation, respectively. Then the photo-generated electrons in the CB of BlueP would move into the VB of PN to combine photo-generated holes. This recombination can promote the separation of photo-induced carriers, resulting in more photogenerated electrons at the CBM of PN and more photogenerated holes at the VBM of BlueP. Consequently, net photogenerated electrons and holes were located at PN and BlueP, respectively. Therefore, 2D BlueP/PN heterostructure would be a direct Z-Scheme photocatalytic heterostructure (Fig. 8). Compared with the traditional type II heterostructure, the direct Z type heterostructure can form a more negative potential of CBM and more positive potential of

![](./images/812658501909217282_23.jpg)

Fig. 7 The total density of states of the BlueP/PN vdW heterostructure (a), corresponding PDOS (projected density of states) of BlueP in vdW heterostructure (b) and PDOS of PN in vdW heterostructure (c).

VBM, achieving a strong reduction and oxidation ability. For direct Z-Scheme BlueP/PN heterostructure, the potential of CBM is -3.62 eV higher than the water reduction potential at pH=0 and the potential of VBM is -6.2 eV lower than the water oxidation potential. These findings indicate that the Z type BlueP/PN heterostructure has sufficient driving force for HER and OER reactions, which can achieve overall water splitting under visible light irradiation.

![](./images/812658501909217282_24.jpg)

Fig. 8 Schematic presentation of the band edge aliments of BlueP/PN vdW heterostructure.

The HER was explored to examine the performance of BlueP/PN for photocatalytic water splitting. According to the Tafel mechanism, surface H atom is formed by reducing H⁺ (H⁺+e⁻→H*), and then yield H₂ (H*+H*→H₂). The absolute value of Gibbs free energy of hydrogen adsorption, $|\Delta G_{H*}|$, is reversely proportional to the activity of HER. Fig. 9 shows the free energy diagrams of HER over BlueP, PN and BlueP/PN heterostructure and the corresponding models for the calculation. The formation of 2D vdW heterostructure decreased $|\Delta G_{H*}|$ to 1.79 eV from 2.21 eV (BlueP) and 2.03 eV (PN). This indicates that BlueP/PN heterostructure would have better activity for HER than individual BlueP and PN.

![](./images/812658501909217282_25.jpg)

Fig. 9 Free energy diagrams for HER over BlueP, PN, and BlueP/PN. The inserts are the top view and side view of the H adsorbed model.

The nonlinear optical intersubband absorption coefficient of a material is associated with its photocatalysis, photovoltaics, and optoelectronics. The coefficient can be calculated from the following equation:

$$
\alpha(v)=\sqrt{2 \omega\left(\sqrt{\varepsilon_{1}(v)^{2}+\varepsilon_{2}(v)^{2}}-\varepsilon_{1}(v)\right)}, \tag{6}
$$

where $\varepsilon_1$ and $\varepsilon_2$ are the real and imaginary parts of the dielectric function, respectively. Furthermore, $v$ is the light frequency and described as follows:

$$
v=\frac{c}{\lambda}, \tag{7}
$$

where c is velocity of light; the $\lambda$ is the wavelength. The optical absorption coefficients of BlueP, PN, and BlueP/PN were calculated. The light absorption of 2D g-C₃N₄ was calculated at the same computational accuracy as reference. As shown in Fig. 10, BlueP has a clear absorption in the visible region (400-800 nm) due to its narrow band gap, which is comparable to the 2D g-C₃N₄. Furthermore, BlueP/PN heterostructure exhibits strengthened absorption ability in the visible region, which is stronger than the superposition of individual BlueP and PN.

![](./images/812658501909217282_26.jpg)

Fig. 10 The optical absorption coefficients of BlueP, PN, and BlueP/PN calculated with HSE06 functional model.

## Conclusions
A 2D BlueP/PN heterostructure was proposed. Furthermore, its energy band structure, DOS, electron densities, and electrostatic potentials were calculated with the HSE06 hybrid density functional method. It is a direct band structure with a bandgap of 1.3 eV. The projected DOS and band structure showed that the BlueP/PN heterostructure is a staggered band alignment structure. Furthermore, the work functions and the charge densities revealed that PN interacted with BlueP to form a heterojunction, and its parts were positively and negatively charged to form a built-in electric field at the interface. As a result, the VBM of BlueP and the CBM of PN accumulated more holes and electrons, respectively. The separation of photoexcited holes and electrons can enhance the participation

of holes and electrons in the photocatalytic reaction on the surfaces. In addition, the formation of BlueP/PN heterostructure could reduce energy barrier of HER, enhancing its activity of water splitting. Therefore, the 2D BlueP/PN nano heterostructure possesses a direct Z scheme photocatalytic feature and thus would be efficient for water splitting to $H_2$ and $O_2$.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
J.L. thanks the support of China Postdoctoral Science Foundation (2019M651397).

## References
1  T. Hisatomi, J. Kubota and K. Domen, *Chem. Soc. Rev.*, 2014, **43**, 7520-7535.
2  A. Kudo and Y. Miseki, *Chem. Soc. Rev.*, 2009, **38**, 253-278.
3  S. J. A. Moniz, S. A. Shevlin, D. J. Martin, Z.-X. Guo and J. Tang, *Energy Environ. Sci.*, 2015, **8**, 731-759.
4  M. Ni, M. K. H. Leung, D. Y. C. Leung and K. Sumathy, *Renewable Sustainable Energy Rev.*, 2007, **11**, 401-425.
5  X. Zou and Y. Zhang, *Chem. Soc. Rev.*, 2015, **44**, 5148-5180.
6  H. Zheng, J. Z. Ou, M. S. Strano, R. B. Kaner, A. Mitchell and K. Kalantar-zadeh, *Adv. Funct. Mater.*, 2011, **21**, 2175-2196.
7  S. Tokunaga, H. Kato and A. Kudo, *Chem. Mater.*, 2001, **13**, 4624-4628.
8  G. Li, S. Yan, Z. Wang, X. Wang, Z. Li, J. Ye and Z. Zou, *Dalton Trans.*, 2009, DOI: 10.1039/b906799j, 8519-8524.
9  X. Chen, L. Liu, P. Y. Yu and S. S. Mao, *Science*, 2011, **331**, 746-750.
10 A. Ishikawa, T. Takata, J. N. Kondo, M. Hara, H. Kobayashi and K. Domen, *J. Am. Chem. Soc.*, 2002, **124**, 13547-13553.
11 S. Cao, J. Low, J. Yu and M. Jaroniec, *Adv. Mater.*, 2015, **27**, 2150-2176.
12 X. Zhu, T. Zhang, Z. Sun, H. Chen, J. Guan, X. Chen, H. Ji, P. Du and S. Yang, *Adv. Mater.*, 2017, **29**, 1605776.
13 G. Hitoki, T. Takata, J. N. Kondo, M. Hara, H. Kobayashi and K. Domen, *Chem. Commun.*, 2002, DOI: 10.1039/b202393h, 1698-1699.
14 R. Asahi, T. Morikawa, T. Ohwaki, K. Aoki and Y. Taga, *Science*, 2001, **293**, 269-271.
15 C. Burda, Y. B. Lou, X. B. Chen, A. C. S. Samia, J. Stout and J. L. Gole, *Nano Lett.*, 2003, **3**, 1049-1051.
16 X. Chen and C. Burda, *J. Am. Chem. Soc.*, 2008, **130**, 5018-2019.
17 T. Ohno, M. Akiyoshi, T. Umebayashi, K. Asai, T. Mitsui and M. Matsumura, *Appl. Catal.*, A, 2004, **265**, 115-121.
18 D. Huang, S. Chen, G. Zeng, X. Gong, C. Zhou, M. Cheng, W. Xue, X. Yan and J. Li, *Coord. Chem. Rev.*, 2019, **385**, 44-80.
19 H. Li, W. Tu, Y. Zhou and Z. Zou, *Adv. Sci.*, 2016, **3**, 1500389.
20 J. Low, C. Jiang, B. Cheng, S. Wageh, A. A. Al-Ghamdi and J. Yu, *Small Methods*, 2017, **1**, 1700080.
21 C. Li, P. Zhou and D. W. Zhang, *J. Semicond.*, 2017, **38**, 031005.
22 G. Li, L. Zhang, W. Xu, J. Pan, S. Song, Y. Zhang, H. Zhou, Y. Wang, L. Bao, Y.-Y. Zhang, S. Du, M. Ouyang, S. T. Pantelides and H.-J. Gao, *Adv. Mater.*, 2018, **30**, 1804650.
23 Z. Zuo, Z. Xu, R. Zheng, A. Khanaki, J.-G. Zheng and J. Liu, *Sci. Rep.*, 2015, **5**, 14760.
24 C. Tan, X. Cao, X.-J. Wu, Q. He, J. Yang, X. Zhang, J. Chen, W. Zhao, S. Han, G.-H. Nam, M. Sindoro and H. Zhang, *Chem. Rev.*, 2017, **117**, 6225-6331.
25 G. R. Bhimanapati, Z. Lin, V. Meunier, Y. Jung, J. Cha, S. Das, D. Xiao, Y. Son, M. S. Strano, V. R. Cooper, L. Liang, S. G. Louie, E. Ringe, W. Zhou, S. S. Kim, R. R. Naik, B. G. Sumpter, H. Terrones, F. Xia, Y. Wang, J. Zhu, D. Akinwande, N. Alem, J. A. Schuller, R. E. Schaak, M. Terrones and J. A. Robinson, *ACS Nano*, 2015, **9**, 11509-11539.
26 K. F. Mak and J. Shan, *Nat. Photonics*, 2016, **10**, 216-226.
27 F. Shahzad, M. Alhabeb, C. B. Hatter, B. Anasori, S. M. Hong, C. M. Koo and Y. Gogotsi, *Science*, 2016, **353**, 1137-1140.
28 J. Pang, A. Bachmatiuk, Y. Bin, B. Trzebicka, L. Zhao, L. Fu, R. G. Mendes, T. Gemming, Z. Liu and M. H. Rummeli, *Adv. Energy Mater.*, 2018, **8**, 1702093.
29 X. Lu, K. Xu, P. Chen, K. Jia, S. Liu and C. Wu, *J. Mater. Chem. A*, 2014, **2**, 18924-18928.
30 J.-P. Xu, J.-Q. Zhang, H. Tian, H. Xu, W. Ho and M. Xie, *Phys. Rev. Mater.*, 2017, **1**, 061002.
31 M. Sun, W. Tang, Q. Ren, S.-k. Wang, J. Yu and Y. Du, *Appl. Surf. Sci.*, 2015, **356**, 110-114.
32 J.-J. Zhang and S. Dong, *2D Mater.*, 2016, **3**, 035006.
33 C. Sevik and H. Sevinçli, *Nanotechnology*, 2016, **27**, 355705.
34 Q. Peng, Z. Wang, B. Sa, B. Wu and Z. Sun, *ACS Appl. Mater. Interfaces*, 2016, **8**, 13449-13457.
35 S. Sun, T. Hussain, W. Zhang and A. Karton, *Appl. Surf. Sci.*, 2019, **486**, 52-57.
36 L. Kou, T. Frauenheim and C. Chen, *J. Phys. Chem. Lett.*, 2014, **5**, 2675-2681.
37 B.-J. Wang, X.-H. Li, X.-L. Cai, W.-Y. Yu, L.-W. Zhang, R.-Q. Zhao and S.-H. Ke, *J. Phys. Chem. C*, 2018, **122**, 7075-7080.
38 L. Lu, Y. Dai, W. Wei, Y. Liang and B. Huang, *J. Mater. Chem. A*, 2018, **6**, 21087-21097.
39 L. Banerjee, A. Mukhopadhyay, A. Sengupta and H. Rahaman, *J. Comput. Electron.*, 2016, **15**, 919-930.
40 J. Wang, Q. Cai, J. Lei, G. Yang, J. Xue, D. Chen, B. Liu, H. Lu, R. Zhang and Y. Zheng, *ACS Appl. Mater. Interfaces*, 2019, **11**, 20956-20964.
41 I. Khan, J. Son and J. Hong, *Phys. Lett. A*, 2018, **382**, 205-209.
42 Y. Mogulkoc, M. Modarresi, A. Mogulkoc and B. Alkan, *Phys. Chem. Chem. Phys.*, 2018, **20**, 12053-12060.
43 Q. Peng, Z. Wang, B. Sa, B. Wu and Z. Sun, *Sci. Rep.*, 2016, **6**, 31994.
44 Z. Y. Zhang, M. S. Si, S. L. Peng, F. Zhang, Y. H. Wang and D. S. Xue, *J. Solid State Chem.*, 2015, **231**, 64-69.
45 M. Sun, J.-P. Chou, J. Yu and W. Tang, *Phys. Chem. Chem. Phys.*, 2017, **19**, 17324-17330.
46 G. Li, Y. Zhao, S. Zeng, M. Zulfiqar, L.-W. Wang and J. Ni, *Comput. Mater. Sci.*, 2018, **152**, 256-261.
47 Q. Yang, C.-J. Tan, R.-S. Meng, J.-K. Jiang, Q.-H. Liang, X. Sun, D.-G. Yang and X.-P. Chen, *IEEE Electron Device Lett.*, 2016, **38**, 145-148.
48 B.-J. Wang, X.-H. Li, R. Zhao, X.-L. Cai, W.-Y. Yu, W.-B. Li, Z.-S. Liu, L.-W. Zhang and S.-H. Ke, *J. Mater. Chem. A*, 2018, **6**, 8923-8929.
49 J. L. Zhang, S. Zhao, C. Han, Z. Wang, S. Zhong, S. Sun, R. Guo, X. Zhou, C. D. Gu, K. D. Yuan, Z. Li and W. Chen, *Nano Lett.*, 2016, **16**, 4903-4908.
50 X. Tan, Y. Ji, H. Dong, M. Liu, T. Hou and Y. Li, *RSC Adv.*, 2017, **7**, 50239-50245.

This journal is © The Royal Society of Chemistry 20xx

J. Name., 2013, **00**, 1-3 | 7

graphical abstract

![](./images/812658501909217282_27.jpg)

A BlueP/PN with 2D van der Waals (vdW) heterostructure was proposed and theoretically investigated to construct Z-scheme photocatalytic system for water splitting under visible light irradiation.