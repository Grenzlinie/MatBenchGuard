PHYSICAL REVIEW B 92, 134112 (2015)

# Soft modes and anharmonicity in $H_3[Co(CN)_6]$: Raman spectroscopy and first-principles calculations

K. K. Mishra, $^{1, *}$ Sharat Chandra, $^{1}$ Nilesh P. Salke, $^{2}$ S. N. Achary, $^{3}$ A. K. Tyagi, $^{3}$ and Rekha Rao $^{2, *}$

$^{1}$Materials Science Group, Indira Gandhi Centre for Atomic Research, Kalpakkam 603 102, India
$^{2}$Solid State Physics Division, Bhabha Atomic Research Centre, Mumbai 400 085, India
$^{3}$Chemistry Division, Bhabha Atomic Research Centre, Mumbai 400 085, India

(Received 1 July 2015; revised manuscript received 1 October 2015; published 26 October 2015)

In situ high-pressure Raman spectroscopy and ab initio calculations are carried out to investigate the phase stability and the thermal expansion behavior of $H_3[Co(CN)_6]$. Raman studies at high pressures in a diamond anvil cell identify soft phonons and phase instability at 2.3 GPa. Evidence of pressure-induced amorphization is found at 11 GPa. The phonon frequencies and eigenvectors obtained from ab initio calculation are used to complement the observed phonon spectra and for assignment of Raman modes. The computed eigenvector displacement patterns indicate that the soft modes correspond to the CN-librational vibrations ($E_g$ mode) of the Co-CN-H-NC-Co linkages and their Grüneisen parameters are found to be negative, in agreement with our measured values. The thermal expansion coefficient $(15.6\times10^{-6}\ \text{K}^{-1})$ calculated using our computed mode Grüneisen parameters is found to be in good agreement with the reported value $(20\times10^{-6}\ \text{K}^{-1})$. Temperature-dependent phonon spectra down to 77 K are used to obtain the anharmonicities of different modes.

DOI: 10.1103/PhysRevB.92.134112
PACS number(s): 78.30.-j, 62.50.-p, 63.20.Ry, 65.40.De

## I. INTRODUCTION

Study of the thermal expansion behavior of flexible framework structure materials has attracted considerable interest following the report of a large negative thermal expansion (NTE) in cubic $Zr(WO_4)_2$ [1] over a large temperature range and a colossal anisotropic thermal expansion in $Ag_3[Co(CN)_6](AgCCN)$ [2]. To understand the unusual NTE behavior, extensive investigations have been carried out on such systems employing various techniques, such as Raman spectroscopy [3-10], far-infrared (IR) transmission spectroscopy [10], inelastic neutron scattering [11-14], x-ray [2] and neutron diffraction [15], reverse Monte Carlo modeling [16,17], and lattice dynamics simulation [2,10,18,19]. It is widely accepted that the central feature of NTE behavior in these systems often lies in their unique flexible crystal structure and unusual phonon dynamics. Understanding of fundamental physics behind NTE behavior is important in designing and developing composite material to have controlled thermal expansion as needed.

The AgCCN is trigonal [2] at ambient conditions with space group $P\bar{3}1m$, consisting of alternate layers of $Ag^+$ and $[Co(CN)_6]^{3-}$ ions stacked parallel to the crystallographic $c$ axis. These layers are connected with the almost flexible Co-CN-Ag-NC-Co linear linkages along the $\langle101\rangle$ direction and form a set of three identical interpenetrating, distorted cubic networks [2]. To preserve the structural integrity of this flexible linkage, it is geometrically necessary that any expansion in the trigonal basal plane [$a(b)$ axes] be accompanied by a decrease in an orthogonal $c$ axis of comparable magnitude. Such changes with temperature result in positive thermal expansion (PTE) in one direction $(\alpha_a=132\times10^{-6}\ \text{K}^{-1})$ coupled with NTE in the perpendicular direction $(\alpha_c=-130\times10^{-6}\ \text{K}^{-1})$ in the temperature range 16 to 500 K, its decomposition temperature; however, the net volume thermal expansion is positive $(\alpha_V=45\times10^{-6}\ \text{K}^{-1})$. Such a colossal coefficient of thermal expansion (CTE), which is an order of magnitude greater than that observed in other crystalline materials, is argued to be due to weak $Ag^+\dots Ag^+$ metallic interaction [2]. Calculations using density functional theory (DFT) suggest that the flexing of this structure requires a small energy contribution by the Ag-related phonon modes. In addition, the extremely shallow energy surface suggests that the observed colossal thermal expansion is achieved only by its small value of the bulk modulus, along with a normal value of the thermal Grüneisen constant [2,20]. Besides a large CTE, it possesses large anisotropic negative linear compression (NLC) with pressure that manifests as an $a$-axis contraction coupled with NLC along the $c$ axis [15]. Neutron diffraction results show that the ambient trigonal phase is stable until a phase transition to a monoclinic phase $(C2/m)$ at 0.19 GPa, and it is observed that the second phase exhibits less NTE and NLC compared to its ambient phase [15]. No phase transition is observed until 500 K, which is the decomposition temperature. Earlier Raman scattering investigations on AgCCN, as a function of pressure at constant temperature and as a function of temperature at constant pressure, have been used to identify the optical phonons responsible for NTE, and it has been shown that the Co-CN bending mode occurring at $335\ \text{cm}^{-1}$ contributes significantly to the NTE [8]. Mode Grüneisen parameters of all modes in both phases are reported for possible correlation with thermodynamical properties [8]. High-pressure (HP) Raman spectroscopic investigation on trigonal $KMn[Ag(CN)_2]_3$ has revealed the contribution of different phonons to its thermal expansion and examined its phase stability [18]. Unlike AgCCN, K-ion inclusion at the interstitial site is found to stiffen the lattice and change the lattice dynamics, resulting in a lower NTE coefficient [18]. Softening of low-energy optic modes related to Ag translation and transverse acoustic modes are concluded to be responsible for the pressure-induced phase transition at 2.8 GPa [18]. In this class of materials, because of their structural flexibility, pressure-induced

*Corresponding authors: kkm@igcar.gov.in and rekhar@barc.gov.in

1098-0121/2015/92(13)/134112(9)
134112-1
©2015 American Physical Society

![](./images/814586770560647169_1.jpg)

FIG. 1. (Color online) Trigonal crystal structure of ${\rm H_3[Co(CN)_6]}$, space group $P\bar{3}1m$, (a) showing the unit cell and (b) as looking down along the [001] crystallographic axis. The atoms are labeled.

amorphization (PIA) and lattice mode softening are often observed [3–10].

${\rm H_3[Co(CN)_6]}$ crystallizes in the trigonal phase, isostructural to AgCCN, with the flexible linear linkages consisting of ${\rm H^+}$ in place of the ${\rm Ag^+}$ cation (Fig. 1). However, it has an unusual symmetric arrangement of the hydrogen atom in the Co-C-N-H-N-C-Co linkages and very short N...H...N separation [16]. It exhibits anisotropic thermal expansion, with $\alpha_{\rm c}=-2.4\times10^{-6}\ {\rm K^{-1}}$ and $\alpha_{\rm a}=14.8\times10^{-6}\ {\rm K^{-1}}$ and an overall PTE coefficient in the temperature range 4 to 300 K and the magnitude of $\alpha_{\rm v}=20\times10^{-6}\ {\rm K^{-1}}$ at 300 K, which is moderate compared to that observed in AgCCN [16]. In addition, thermal evolution of the x-ray diffraction (XRD) analysis shows no evidence for any phase transition in the previously mentioned temperature range. However, there is no experimental report on the role of different phonons in its thermal expansion. Since phonon modes and their Grüneisen parameters are directly responsible for thermal expansion in a material, it becomes straightforward to find their relation. Contrary to the general observation that one finds an increase in NTE with an increase volume in isostructural compounds [21], deuteration of ${\rm H_3[Co(CN)_6]}$, which leads to a higher volume, resulted in a lower NTE [16] (unit cell volume for ${\rm H_3[Co(CN)_6]}$ of $\sim204.2\ \mathring{\rm A}^3$, deuterated ${\rm H_3[Co(CN)_6]}$ of $\sim205.2\ \mathring{\rm A}^3$ [16], and AgCCN of $\sim304.7\ \mathring{\rm A}^3$ [2]). Thus, it would be of interest to investigate the compound under pressure in relation to its thermal expansion behavior. Furthermore, an investigation on the HP stability of the trigonal phase and its comparison with that of AgCCN exhibiting a colossal CTE could give insight about their differences in the CTE.

Thermal expansion in a solid is known to arise due to its inherent anharmonicity involved in lattice vibration. Because of this anharmonicity, phonon frequencies change under variable temperature [22]. The changes in the phonon mode frequencies with temperature involve contribution from both the pure volume (implicit) and the pure temperature (explicit) effects. Therefore, by investigating the Raman spectra as a function of temperature and pressure separately, the change of phonon mode frequencies with temperature on a material can be decoupled: a quasiharmonic (implicit) contribution solely due to change in lattice volume and a true anharmonic (explicit) contribution due to phonon-phonon interactions [23]. Furthermore, for NTE materials, soft modes are often found to have a larger magnitude of true anharmonicity than of its total anharmonicity. In general, calculation of thermal expansion is carried out under quasiharmonic approximation (QHA), which is valid and expected to give good results only when phonon-phonon interactions are negligible. In ${\rm ZrW_2O_8}$ [6], the quasiharmonic contribution is dominant; hence, thermal expansion calculated under QHA reported good matching with the experimental value [4]. Therefore, it is imperative to investigate the anharmonic behavior of phonon modes to gain an idea about the role of different phonons in determining NTE.

In the present paper, *in situ* HP Raman spectroscopic studies are carried out on ${\rm H_3[Co(CN)_6]}$ to investigate its structural stability at HP and to obtain the contribution of the various phonon modes to the thermal expansion using experiments. From HP Raman spectra measurements, soft phonons are identified. Behaviors of phonons at low temperatures down to 77 K are also investigated to estimate the anharmonicity of phonons. To complement the experimental results, phonon dispersion curve, eigenvectors, and Grüneisen parameters are computed by employing *ab initio* DFT calculations using the Vienna *Ab initio* Simulation Package (VASP) and Phonopy. The phonon eigenvectors are used for the assignment of the phonon modes. The thermal expansion of the titular compound is calculated using Grüneisen parameters of all phonons and compared with the reported value.

## II. EXPERIMENTAL DETAILS

The ${\rm H_3[Co(CN)_6]}$ sample was prepared from ${\rm K_3[Co(CN)_6]}$ by a cation exchange process similar to a procedure described earlier [24]. The ion exchange column of about 25 cm was prepared by using acidic resin and was fully protonated by using excess HCl. The column was repeatedly washed with deionized water to remove any unbounded ${\rm H^+}$ or ${\rm Cl^-}$ in the column. Aqueous solution of ${\rm K_3[Co(CN)_6]}$(1.5 mMol) was passed through this column, and the eluted liquid was collected from the midregion of the column. The eluted solution was allowed to slowly evaporate at ambient temperature. In a period of three weeks, colorless needle-shaped crystals were obtained. The phase purity of the crystals was confirmed by powder XRD analysis. The diffraction pattern could be indexed to the trigonal crystal system with space group $P\bar{3}1m$, lattice parameters $a=6.4306\ \mathring{\rm A}$ and $c=5.7006\ \mathring{\rm A}$, and a volume of the unit cell equal to $204.15\ \mathring{\rm A}^3$, which are consistent with the earlier report [25]. Raman measurements were carried out on unoriented single crystal pieces loaded into a $150$-$\mu$m hole of a stainless-steel gasket (preindented

<table><caption>TABLE I. Irreducible representations of different sites in the $P\overline{3}1m$ unit cell of trigonal $\text{H}_3[\text{Co(CN)}_6]$.</caption>
<tbody><tr><th>Atom</th><th>Site</th><th>Irreducible representation</th></tr>
<tr><td>Co</td><td>$1\text{a}(D_{3\text{d}})$</td><td>$A_{2\text{u}} + E_{\text{u}}$</td></tr>
<tr><td>H</td><td>$3\text{g}(C_{2\text{h}})$</td><td>$A_{1\text{u}} + E_{\text{u}} + 2A_{2\text{u}} + 2E_{\text{u}}$</td></tr>
<tr><td>C</td><td>$6\text{k}(C_{\text{s}})$</td><td>$2A_{1\text{g}} + 2E_{\text{g}} + 2A_{2\text{u}} + 2E_{\text{u}} + A_{2\text{g}} + 2E_{\text{g}} + 2A_{1\text{u}} + 2E_{\text{u}}$</td></tr>
<tr><td>N</td><td>$6\text{k}(C_{\text{s}})$</td><td>$2A_{1\text{g}} + 2E_{\text{g}} + 2A_{2\text{u}} + 2E_{\text{u}} + A_{2\text{g}} + 2E_{\text{g}} + 2A_{1\text{u}} + 2E_{\text{u}}$</td></tr>
</tbody></table>

to a 70-$\mu$m thickness) of a diamond anvil cell (DAC; model B-05, Diacell Products, Leicester, U.K.). The Raman spectra were recorded in the backscattering geometry using both a transmitting and a nontransmitting medium. A mixture of 4:1 methanol-ethanol was used as the pressure transmitting medium. Ruby fluorescence was used for the estimation of pressure. About 25 mW of power at the 532-nm line from a diode-pumped solid-state laser was used to excite the sample. Scattered light from the sample was analyzed using a homebuilt 0.9-m single monochromator, coupled with an edge filter and detected with a cooled charge-coupled device (Andor Technology). Low-temperature Raman measurements from 293 down to 77 K were carried out using the Linkam (THMS 600) stage. The spectra were fitted to Lorentzian line shapes with a suitable background using the Jandel PeakFit program to yield a good fit, and the central mode frequency, full width at half maximum, and integrated intensity were obtained.

Ab initio first-principles calculations were carried out using VASP [26–28], the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation for exchange and correlation [29], and the projector- augmented wave (PAW) pseudopotentials. A plane-wave basis set with a cutoff energy of 450 eV was used. The calculations were performed using a $7 \times 7 \times 7$ Monkhorst-Pack grid, along with a shift of the k grid to include the $\Gamma$ point. The lattice parameters and the positions of all 16 atoms of the trigonal primitive unit cell of $\text{H}_3[\text{Co(CN)}_6]$ [23] were relaxed one after the other in three cycles for determining the ground state atomic configuration. In each cycle, first the lattice parameters were relaxed, followed by the atom positions, which were relaxed simultaneously. A $2 \times 2 \times 2$ supercell was constructed from the relaxed configuration, and the atom positions were again relaxed before carrying out the phonon calculations. The final total energy and force convergences were better than $10^{-9}$ eV and $10^{-4}$ eV/Å, respectively. The zone-center phonon frequencies were calculated using the VASP implementation of density functional perturbation theory. The phonon spectrum over the entire Brillouin zone, the mode Grüneisen parameters, thermal expansion, and heat capacity were computed within the QHA using the Phonopy program [30]. Visual representations of different phonon modes were obtained using the V_Sim Visualization package [31]. The elastic constant and compliance matrices were also calculated using density functional perturbation theory for the equilibrium structure, using the relaxed unit cell and a $9 \times 9 \times 9$ Monkhorst-Pack grid with no shift.

### III. RESULTS AND DISCUSSION

The compound $\text{H}_3[\text{Co(CN)}_6]$ stabilizes in a trigonal structure with space group $P\overline{3}1m$ (point group $D_{3d}$), with only one formula unit per primitive cell. This results in 16 atoms in the primitive cell and consequently a total of 48 degrees of freedom, with three acoustic phonons. The irreducible representations corresponding to each site can be obtained using the Halford-Hornig site-group analysis [32] and are given in Table I. The irreducible representation for optical phonons is $\Gamma_{\text{opt}} = 4A_{1\text{g}} + 6E_{\text{g}} + 2A_{2\text{g}} + 9E_{\text{u}} + 6A_{2\text{u}} + 3A_{1\text{u}}$ and for acoustic phonons is $\Gamma_{\text{acoustic}} = A_{2\text{u}} + E_{\text{u}}$. Thus, there are 10 Raman active modes ($4A_{1\text{g}}$ and $6E_{\text{g}}$), 15 IR active modes ($6A_{2\text{u}}$ and $9E_{\text{u}}$, excluding the acoustic phonons) and 5 optically inactive or silent modes ($2A_{2\text{g}} + 3A_{1\text{u}}$) expected. Because of the centrosymmetric nature of the crystal, the Raman and IR active phonons for the trigonal phase are mutually exclusive. Figure 2 shows the normalized Raman spectrum of $\text{H}_3[\text{Co(CN)}_6]$ at several hydrostatic pressures, including ambient pressure. The spectral intensity is normalized with

![](./images/814586770560647169_2.jpg)

FIG. 2. (Color online) Normalized Raman spectra of $\text{H}_3[\text{Co(CN)}_6]$ at various pressures: (a) $100$–$650\ \text{cm}^{-1}$ and (b) $2000$–$2400\ \text{cm}^{-1}$. The spectral intensity is normalized with respect to the intensity of the $A_{1\text{g}}$ mode at $210\ \text{cm}^{-1}$. The arrow indicates soft modes at 140 and $348\ \text{cm}^{-1}$, which have negative pressure dependence. New modes appearing at 2.3 GPa are labeled using asterisks. Solid curves are the Lorentzian least-square fits to ambient data.

134112-3

![](./images/814586770560647169_3.jpg)

FIG. 3. (Color online) Phonon dispersion curves and phonon DOS obtained from first-principles density functional simulations using VASP for the trigonal primitive unit cell with 16 atoms. The zone-center phonon frequencies exhibit good matching with experimental Raman modes.

respect to the intensity of the $A_{1g}$ mode at $210\mathrm{cm}^{-1}$. At ambient conditions, a total number of eight Raman modes are observed, similar to the number reported earlier [24]. There are no Raman active phonon modes in the spectral range between 800 and $2000\mathrm{cm}^{-1}$. The observed modes are less than those predicted, which may be due to either accidental degeneracy of phonon frequencies or insufficient intensities arising from the small polarizability of a few modes. The most intense modes in the spectrum are seen at 175, 2185, and $2208\mathrm{cm}^{-1}$. In the absence of the polarized Raman measurements on an oriented single crystal, the observed modes are assigned based on the calculated eigenvectors obtained from computation. The computed phonon dispersion over the entire Brillouin zone, and the total and atom decomposed phonon density of states (DOS) are shown in Fig. 3. The partial phonon DOS of each atom is calculated after accounting for all degrees of freedom for each atom type. One can see that in the low-frequency range $(<600\mathrm{cm}^{-1})$, the contribution comes from predominantly CN-librational modes, while the $\mathrm{C\equiv N}$ internal modes contribute to the DOS corresponding to the phonon frequencies greater than $2000\mathrm{cm}^{-1}$. Hydrogen-related phonon DOS contributions can be seen $\sim1200\mathrm{cm}^{-1}$ and in the broad dispersion band between 500 and $1500\mathrm{cm}^{-1}$. Since the H atom in $\mathrm{H_3[Co(CN)_6]}$ is relatively smaller in size as compared to Ag in a similar system, like AgCCN, its vibrational movements can be quite complex and the contributions from many such modes can result in the broad dispersion observed in the phonon band. As can be seen from phonon DOS for each atom, cobalt has the least contribution to the phonon DOS. Cobalt, being a heavy atom, contributes in the lower frequency range of the phonon spectrum. Mixing of the optical and acoustic modes is apparent in the whole Brillouin zone in the low-frequency region. This is similar to the mixing observed in AgCCN [10] but contrary to that in $\mathrm{Zn(CN)_2}$ [7]. The calculated elastic constants and the compliance matrix elements of $\mathrm{H_3[Co(CN)_6]}$ are listed in Table II. For the trigonal crystal system, we obtained five unique elastic constants: $C_{11}(=C_{22})$, $C_{33}$, $C_{44}(=C_{55}$ and $C_{66})$, $C_{12}$, and $C_{13}(=C_{23})$. All other elements of the elastic constant

<table>
<caption>TABLE II. Elastic constants and compliances of $\mathrm{H_3[Co(CN)_6]}$ calculated using density functional perturbation theory for the equilibrium volume.</caption>
<tbody>
<tr>
<td>Matrix element</td>
<td>11</td>
<td>33</td>
<td>44</td>
<td>12</td>
<td>13</td>
</tr>
<tr>
<td>Elastic constant, $\text{C}$ (GPa)</td>
<td>79.961</td>
<td>143.756</td>
<td>66.879</td>
<td>28.902</td>
<td>71.733</td>
</tr>
<tr>
<td>Compliance, $\text{S}$ ($\text{GPa}^{-1}$)</td>
<td>0.023</td>
<td>0.020</td>
<td>0.015</td>
<td>0.004</td>
<td>0.013</td>
</tr>
</tbody>
</table>

matrix are zero. The compliance matrix $\mathbf{S}$ is calculated as the inverse of the elastic constant matrix $(\mathbf{C}^{-1})$. Linear compressibilities of $\mathrm{H_3[Co(CN)_6]}$ in the ambient trigonal phase have been computed using the elastic constants in Table II. The compressibilities in the basal plane and along its trigonal direction are given by the simple transformations [10]: $\chi_{\perp}=(C_{33}-C_{13})/(C_{11}C_{33}-2C_{13}^2+C_{12}C_{33})$ and $\chi_{\parallel}=(C_{11}+C_{12}-2C_{13})/(C_{11}C_{33}-2C_{13}^2+C_{12}C_{33})$. The calculated values are $\chi_{\perp}=13.4\times10^{-3}\,\text{GPa}^{-1}$ and $\chi_{\parallel}=-6.46\times10^{-3}\,\text{GPa}^{-1}$.

Observed Raman mode frequencies, which are close to the calculated zone-center phonon frequencies, are assigned to the corresponding symmetry species. Table III lists the observed mode frequencies, along with the calculated values and their assignments. Close matching of $\sim4\%$ between the experimental and the computed values is found for all modes. However, the mismatch between the experimental and the calculated Grüneisen parameters could be partly related to the difference [10] between the experimental volume and the relaxed volume obtained by DFT. Although DFT accurately predicts bulk physical quantities like the thermal expansion coefficient and specific heat, microscopic parameters like Grüneisen parameters obtained from an experiment are often not reproduced accurately using DFT [7,10,18]. Figure 4 shows the displacement vectors for the different Raman modes. The $E_{\text{g}}$ mode at $137\mathrm{cm}^{-1}$ [Fig. 4(a)] and $335\mathrm{cm}^{-1}$ [Fig. 4(b)] involves librational (or local transverse) vibration of CN ions about the Co-C-N-H-N-C-Co linear linkages joining Co$\dots$Co ions, consistent with the prediction of Keen *et al.* [16] but contrary to the assignments by Haser *et al.* [24]. The Grüneisen parameters of these modes are negative (Table III). This will be discussed later. However, the internal modes $E_{\text{g}}$ at $2245\mathrm{cm}^{-1}$ [Fig. 4(c)] and $A_{1\text{g}}$ at $2280\mathrm{cm}^{-1}$ [Fig. 4(d)] exhibit symmetric stretching vibration of $\mathrm{C\equiv N}$ along the rigid linkage, consistent with the assignment by Haser *et al.* [24]. Similar kinds of stretching vibrations are observed in other flexible systems, like AgCCN [10], $\mathrm{KMn[Ag(CN)_2]_3}$ [18], and $\mathrm{Zn(CN)_2}$ [7].

Upon increase in pressure, intensities of the modes characteristic of the trigonal phase reduce, while Raman bands at 137, 155, 557, 578, 2148, 2187, and $2206\mathrm{cm}^{-1}$ probably corresponds to a new phase whose intensities grow with a subsequent pressure run. At 2.3 GPa, the pairs of bands, viz., one pair at 137 and $155\mathrm{cm}^{-1}$ and another at 557 and $578\mathrm{cm}^{-1}$, are considered to be arising from the splitting of the librational modes at 140 and $507\mathrm{cm}^{-1}$, respectively. In addition, at 2.3 GPa, a triplet at 2148, 2187, and $2206\mathrm{cm}^{-1}$ is found to be arising from the splitting of the mode at $2185\mathrm{cm}^{-1}$ of the trigonal phase. The $E_{\text{g}}$ mode at 140 and $348\mathrm{cm}^{-1}$ (Fig. 2, arrow) is seen to soften, whereas others

<table>
<caption>TABLE III. Observed Raman modes frequencies (labeled R) and Grüneisen parameters ($\gamma_i$) of H₃[Co(CN)₆]. Simulated mode frequencies and their assignments were obtained from the VASP computed eigenvectors using the Phonopy program.</caption>
<thead>
<tr>
<th colspan="2">Experimental valuesª</th>
<th colspan="4">DFT</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\omega$(cm⁻¹)</td>
<td>$\gamma_j$</td>
<td>$\omega$(cm⁻¹)</td>
<td>$\gamma_j$</td>
<td>Symmetry</td>
<td>Mode description</td>
</tr>
<tr>
<td>110 (IR)</td>
<td></td>
<td>119</td>
<td>−4.1</td>
<td>$A_{2u}$</td>
<td>Co-C-N-H-N-C-Co translation</td>
</tr>
<tr>
<td>140 (R)</td>
<td>−1.31</td>
<td>137</td>
<td>−3.9</td>
<td>$E_g$</td>
<td>CN libration</td>
</tr>
<tr>
<td>175 (R)</td>
<td>2.01</td>
<td>173</td>
<td>−0.25</td>
<td>$E_g$</td>
<td>CN libration</td>
</tr>
<tr>
<td>210 (R)</td>
<td>1.48</td>
<td>216</td>
<td>−0.41</td>
<td>$A_{1g}$</td>
<td>CN libration</td>
</tr>
<tr>
<td>348 (R)</td>
<td>−1.85</td>
<td>335</td>
<td>−1.08</td>
<td>$E_g$</td>
<td>CN libration</td>
</tr>
<tr>
<td>400 (IR)</td>
<td></td>
<td>422</td>
<td>4.2</td>
<td>$A_{2u}$</td>
<td>CN libration</td>
</tr>
<tr>
<td>482 (R)</td>
<td>0.11</td>
<td>476</td>
<td>1.15</td>
<td>$E_g$</td>
<td>CN libration</td>
</tr>
<tr>
<td>507 (R)</td>
<td>8.02</td>
<td>482</td>
<td>10.11</td>
<td>$A_{1g}$</td>
<td>CN libration</td>
</tr>
<tr>
<td>560 (IR)</td>
<td></td>
<td>616</td>
<td>2.6</td>
<td>$E_u$</td>
<td>CN libration</td>
</tr>
<tr>
<td>1100 (IR)</td>
<td></td>
<td>1159</td>
<td>−0.7</td>
<td>$E_u$</td>
<td>N-H bending</td>
</tr>
<tr>
<td>1160 (IR)</td>
<td></td>
<td>1181</td>
<td>−0.5</td>
<td>$A_{2u}$</td>
<td>N-H stretching</td>
</tr>
<tr>
<td>2145 (IR)</td>
<td></td>
<td>2206</td>
<td>0.2</td>
<td>$A_{2u}$</td>
<td>Asymmetric stretching of C-N+N-H</td>
</tr>
<tr>
<td>2180 (IR)</td>
<td></td>
<td>2209</td>
<td>0.2</td>
<td>$E_u$</td>
<td>Asymmetric stretching of C-N+N-H</td>
</tr>
<tr>
<td>2185 (R)</td>
<td>0.53</td>
<td>2243</td>
<td>0.23</td>
<td>$E_g$</td>
<td>Symmetric stretching of CN</td>
</tr>
<tr>
<td>2208 (R)</td>
<td>0.52</td>
<td>2280</td>
<td>0.24</td>
<td>$A_{1g}$</td>
<td>Symmetric stretching of CN</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="6">ªObserved IR frequencies from Ref. [25].</td>
</tr>
</tfoot>
</table>

exhibit normal hardening up to 11 GPa, the highest pressure in the present paper. Beyond 2.3 GPa, softening of these modes is relatively less. Experiments were also carried out with no pressure-transmitting medium. Raman features similar to those observed in the hydrostatic case are noticed in the nonhydrostatic case, which indicates that the HP behavior of the sample is the same under hydrostatic and nonhydrostatic conditions. Softening of the mode is known to cause lattice instabilities [22] and consequently drive phase transitions [33,34]. The preceding findings clearly suggest a structural transformation at 2.3 GPa from a trigonal (PI) to a (PII) phase. Since splitting of modes causes an increase in the number of modes in PII, this phase is expected to be of lower lattice symmetry than is PI. It can be noticed (Fig. 2) that the relative intensity of the Raman band at $175\ \text{cm}^{-1}$ is almost constant in the ambient phase and shows marked decrease with pressure in PII. However, the relative intensity of the Raman band at $348\ \text{cm}^{-1}$ shows subtle increase in the ambient phase and gradually decreases in the PII phase. At 11 GPa, these Raman bands vanish. This reduction of intensities in the HP phase points toward development of positional disorder at HP [5]. An increase or decrease in the intensity of any mode is determined by the corresponding changes in the derivative of the polarizability ($\chi$) with respect to the normal coordinate ($\partial\chi/\partial\text{q}$). Further discussion on mode intensity in PII is presented later. The pressure dependence of the mode frequencies is shown in Fig. 5. A clear change in the slope of a few modes is noticed at 2.3 GPa, which further corroborates the phase transition. Two modes, at 140 and $348\ \text{cm}^{-1}$ in PI, show negative slope in the $\omega$ vs $P$ curve and are called the soft mode, while other modes exhibit normal hardening behavior. Mode softening implies a negative Grüneisen parameter $\gamma_i$ and is a key factor for contributing to NTE, while hard modes contribute to PTE. These Grüneisen parameters are key inputs for determining thermal properties such as specific heat and lattice thermal expansion. Table III lists the experimental mode frequencies $\omega_i$ and the corresponding Grüneisen parameters of PI, using the formula $\gamma_i=\frac{B_o}{\omega_i}\frac{d\omega_i}{dP}$ [22], where $B_o$ is the bulk modulus obtained using simulation, which is discussed later. The Grüneisen parameter, being a dimensionless quantity, can only be compared for different modes. The Grüneisen parameter of several librational modes is nearly three times that of the stretching modes, suggesting that the CN-librational modes become easily compressed and deformed under the application of pressure, while a low value of this parameter for the 2185 and $2208\ \text{cm}^{-1}$ stretching modes implies that stretching vibrations are less sensitive to pressure. As

![](./images/814586770560647169_4.jpg)

FIG. 4. (Color online) Atomic displacements of (a) $137\ \text{cm}^{-1}$ and (b) $335\ \text{cm}^{-1}$ modes showing transverse vibration of CN. The modes at (c) $2243\ \text{cm}^{-1}$ and (d) $2280\ \text{cm}^{-1}$ correspond to C≡N symmetric stretching vibrations. Arrows are proportional to the amplitude of the atomic motion. Balls in magenta are Co, those in black are C, those in blue are N, and those in pink indicate H atoms.

![](./images/814586770560647169_5.jpg)

FIG. 5. (Color online) Pressure dependencies of Raman modes. Straight lines through the data are linear square fits to the filled data. The vertical line indicates the identified possible transition pressure. Filled and open symbols are from experimental runs with and without transmitting medium, respectively.

mentioned earlier, CN-librational modes at 140 and $348\,\text{cm}^{-1}$ are contributing negatively to thermal expansion, reminiscent of a flexible system like $\text{Zn(CN)}_2$ [7], while all other modes are significantly contributing to PTE. Pressure dependence of mode frequencies (open symbols in Fig. 5) corresponding to the no-pressure medium have mode behaviors similar to those observed in the hydrostatic case (filled symbols in Fig. 5). In PII, the soft modes of PI continue to exhibit softening, suggesting instability of this structure as well. As pointed out earlier, isostructural AgCCN is reported to undergo a similar phase transition from a trigonal to a lower symmetry monoclinic phase ($C2/m$) at comparatively lower pressure, i.e., 0.19 GPa [15]. It is known that $C2/m$ is the subgroup of the $P\bar{3}1m$ space group and the phase transition from the $P\bar{3}1m$ trigonal phase to the $C2/m$ monoclinic phase is related by condensation of the $E_\text{g}$ mode [10]. In our present experimental result, the condensation of the $E_\text{g}$ mode (soft mode) in PI indicates the possibility of its transition to the HP $C2/m$ monoclinic phase. The other possibility for PII could be $P\bar{3}1m$ (the other subgroup of $P\bar{3}1m$), which is related to the condensation of IR active $A_{2\text{u}}$ and $E_{\text{u}}$ modes of the parent $P\bar{3}1m$ phase. In the absence of IR experimental results under HP, we cannot comment on this phase. Thus, the present paper will motivate detailed HP diffraction and IR spectroscopic studies to resolve the issue.

One can see from the spectra (Fig. 2) that several low- frequency modes and the internal modes corresponding to $\text{C}\equiv\text{N}$ stretching vibration broaden above 5 GPa. Growth of the positional disorder with pressure often causes broadening of modes and is expected due to inhomogeneous broadening [5] caused by a distribution of bond lengths and bond angles about a mean value, in contrast to them being unique, as in a perfect crystalline phase. In addition, intensities of all modes gradually decrease and subsequently disappear at 11 GPa, probably due to a lack of long-range order or periodicity. These results indicate a possible PIA at 11 GPa. Using Raman spectroscopic investigation, PIA in several flexible NTE materials [6,8,18] is reported on or below 13 GPa. Raman spectra were also recorded from a few spots after completely releasing the pressure (Fig. 6). Unlike in the isostructural AgCCN [8], the broad Raman band at $406\,\text{cm}^{-1}$ and the other at $618\,\text{cm}^{-1}$, corresponding to poorly crystallized oxides of cobalt [35], along with a few low-frequency bands at 175 and $210\,\text{cm}^{-1}$, corresponding to partially recovered phases (PI and PII) of the titular compound, are noticed, while the bands of amorphous carbon nitride are not seen in the high-frequency region. This suggests that probably $\text{H}_3[\text{Co(CN)}_6]$ is partially decomposed and is irreversible in the pressure reducing cycle.

![](./images/814586770560647169_6.jpg)

FIG. 6. Raman spectra of $\text{H}_3[\text{Co(CN)}_6]$ (a) at ambient conditions and (b) and (c) at different regions of the sample recovered from 11 GPa. The position (in reciprocal centimeters) marked in (b) is identified in comparison to the parent PI phase.

Figure 7(a) shows the temperature dependence of Raman spectra of $\text{H}_3\text{Co(CN)}_6$ over the entire range of phonon frequencies. Frequencies of all modes except the $E_\text{g}$ mode at $348\,\text{cm}^{-1}$ monotonically soften as a function of temperature. Neither disappearance of existing modes nor emergence of any extra modes is noticed in the Raman spectrum down to 77 K, the lowest temperature reached in the present paper. Furthermore, monotonous changes in mode frequencies indicating the absence of any phase transition agree well

![](./images/814586770560647169_7.jpg)

FIG. 7. (Color online) (a) Raman spectra of ${\rm H_3[Co(CN)_6]}$ at different temperatures $100$–$650\ {\rm cm}^{-1}$ and $2000$–$2400\ {\rm cm}^{-1}$, and (b) the temperature dependence of Raman modes. Only the $E_{\rm g}$ mode at $348\ {\rm cm}^{-1}$ exhibits hardening. Straight lines through the data are linear square fits to the data.

with temperature-dependent XRD results [16]. Temperature dependence of the mode frequencies is shown in Fig. 7(b). The $d\omega_i/dT$ of the various phonon modes is obtained by linear fits to $\omega_i$ vs $T$; these slopes essentially represent the total anharmonicities of the modes. We can separate the true anharmonic and the quasiharmonic parts using the well-known formula [22]

$$
\left. \frac{1}{\omega_i} \frac{d\omega_i}{dT} \right|_P = \left. \frac{1}{\omega_i} \frac{d\omega_i}{dT} \right|_V - \gamma_i \alpha
$$

where the first term on the right-hand side is the true anharmonic (explicit) contribution and the second is the quasiharmonic (implicit) term. Thus, using the thermal expansion coefficient $\alpha = 20 \times 10^{-6}\ {\rm K}^{-1}$ and our present mode Grüneisen parameters $\gamma_i$, we have separated the quasiharmonic and the true anharmonic contribution to the total anharmonicity of eight observed modes (Table IV). We notice from this table that the magnitude of total anharmonicity is large for some CN librational modes, indicating a large contribution to the thermal expansion. In particular, the low-energy modes, viz., 140, 210, and $507\ {\rm cm}^{-1}$, have large anharmonicities. The modes at 140 and $348\ {\rm cm}^{-1}$ have a negative Grüneisen parameter, suggesting their role in NTE. The high-frequency ${\rm C\equiv N}$ stretching modes are not strongly anharmonic. Quasiharmonicity and true anharmonicity for ${\rm C\equiv N}$ stretching modes contribute almost equally to the total anharmonicity. A comparatively higher magnitude of true anharmonicity of the CN-librational mode, compared to that of the ${\rm C\equiv N}$ stretching vibration, agrees well with the high-frequency ${\rm C\equiv N}$ stretching internal modes being stiffer compared to the low-frequency librational modes. We have also calculated the quasiharmonic and the true anharmonic contribution for AgCCN using the previously reported HP and temperature-dependent Raman spectroscopic data [8], given in Table V. The magnitude of total anharmonicity of most modes of ${\rm H_3Co(CN)_6}$ is comparable to those of AgCCN [8] and is almost an order of magnitude less than that of zirconium tungstate [6]. However, a fair comparison of their magnitude indicates that the anharmonicity of these soft modes is found to be larger than that observed in AgCCN [8]. In the case of ${\rm H_3Co(CN)_6}$, the true anharmonicity of ${\rm C\equiv N}$ stretching vibrations is found to be $\sim 2.5$ times less than that obtained for stretching modes in AgCCN. Table IV also shows that the modes at 175, 348, and $507\ {\rm cm}^{-1}$ have a predominant quasiharmonic contribution. However, the modes at 140, 210, and $482\ {\rm cm}^{-1}$ have a large true anharmonic contribution. As mentioned earlier, other phonon vibrations, possibly of a highly anharmonic nature, can be explored with other spectroscopic techniques like IR, since those are not identified by the Raman spectroscopy because of the centrosymmetric nature of the crystal.

Using first-principles calculations, the phonon spectrum was computed at equilibrium volume ($a = 6.3169\ \mathring{\rm A}$ and $c = 5.7025\ \mathring{\rm A}$, with unit cell volume $V_0 = 197.0647\ \mathring{\rm A}^3$) obtained after lattice relaxation. The equilibrium volume was varied $\pm 10\%$ under hydrostatic compression and expansion, and the

TABLE IV. Total anharmonicity, quasiharmonic (implicit) contribution, and true anharmonic (explicit) contribution of different phonons in ${\rm H_3[Co(CN)_6]}$. The numbers in parentheses are standard errors to the least significant digit.

<table>
<thead>
<tr>
<th colspan="4">${\rm H_3[Co(CN)_6]}$</th>
</tr>
<tr>
<th>Mode frequencies
(${\rm cm}^{-1}$)</th>
<th>Total anharmonic
($10^{-5}\ {\rm K}^{-1}$)</th>
<th>Quasiharmonic $\alpha\gamma_i$ ($10^{-5}\ {\rm K}^{-1}$)</th>
<th>True anharmonic
($10^{-5}\ {\rm K}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>140</td>
<td>$-7.4(8)$</td>
<td>$-2.6(1)$</td>
<td>$-10.0(9)$</td>
</tr>
<tr>
<td>175</td>
<td>$-2.1(9)$</td>
<td>$4.0(4)$</td>
<td>$2(1)$</td>
</tr>
<tr>
<td>210</td>
<td>$-6.6(9)$</td>
<td>$2.9(1)$</td>
<td>$-4(1)$</td>
</tr>
<tr>
<td>348</td>
<td>$1.2(6)$</td>
<td>$-3.7(1)$</td>
<td>$-2.5(7)$</td>
</tr>
<tr>
<td>482</td>
<td>$-2.0(4)$</td>
<td>$0.2(0)$</td>
<td>$-1.8(4)$</td>
</tr>
<tr>
<td>507</td>
<td>$-23.3(0)$</td>
<td>$16.0(1)$</td>
<td>$-7.3(1)$</td>
</tr>
<tr>
<td>2185</td>
<td>$-1.8(0)$</td>
<td>$1.0(3)$</td>
<td>$-0.8(3)$</td>
</tr>
<tr>
<td>2208</td>
<td>$-2.1(8)$</td>
<td>$1.0(1)$</td>
<td>$-1.1(9)$</td>
</tr>
</tbody>
</table>

TABLE V. Total anharmonicity, quasiharmonic (implicit) contribution, and true anharmonic (explicit) contribution of different phonons in AgCCN.

<table>
<thead>
<tr>
<th colspan="4">AgCCN$^{\rm a}$</th>
</tr>
<tr>
<th>Mode frequencies
(${\rm cm}^{-1}$)</th>
<th>$\gamma$i</th>
<th>Total anharmonic
($10^{-5}\ {\rm K}^{-1}$)</th>
<th>Quasiharmonic $\alpha\gamma_i$ ($10^{-5}\ {\rm K}^{-1}$)</th>
<th>True anharmonic
($10^{-5}\ {\rm K}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>87</td>
<td>$0.75$</td>
<td>$-11.5$</td>
<td>$+3.38$</td>
<td>$-8.12$</td>
</tr>
<tr>
<td>139</td>
<td>$0.94$</td>
<td>$-6.47$</td>
<td>$+4.23$</td>
<td>$-2.24$</td>
</tr>
<tr>
<td>165</td>
<td>$0.43$</td>
<td>$-5.45$</td>
<td>$+1.94$</td>
<td>$-3.51$</td>
</tr>
<tr>
<td>335</td>
<td>$-0.09$</td>
<td>$-0.09$</td>
<td>$-0.41$</td>
<td>$-0.5$</td>
</tr>
<tr>
<td>474</td>
<td>$0.05$</td>
<td>$-0.42$</td>
<td>$+0.23$</td>
<td>$-0.19$</td>
</tr>
<tr>
<td>521</td>
<td>$0.31$</td>
<td>$-6.53$</td>
<td>$+1.4$</td>
<td>$-5.13$</td>
</tr>
<tr>
<td>2184</td>
<td>$0.02$</td>
<td>$-2.34$</td>
<td>$+0.09$</td>
<td>$-2.25$</td>
</tr>
<tr>
<td>2204</td>
<td>$0.03$</td>
<td>$-2.59$</td>
<td>$+0.14$</td>
<td>$-2.45$</td>
</tr>
</tbody>
</table>

$^{\rm a}$Data from Ref. [8].

total energies of these configurations was used to calculate the bulk modulus $B_{\mathrm{o}}$ and its derivative $B_{\mathrm{o}}^{\prime}$ by fitting the volume vs total energy data to the third-order Birch-Murnaghan equation of state. We find $B_{\mathrm{o}}=138$ GPa and $B_{\mathrm{o}}^{\prime}=3.78$. From the volume dependence of the various zone-center optical phonons, the mode Grüneisen parameters $\gamma_{i}$ for all 30 optical modes were obtained using the expression $\gamma_{i}=-\frac{V_{\mathrm{o}}}{\omega_{i}} \frac{\Delta \omega_{i}}{\Delta V}$. The calculated $\gamma_{i}$'s for most of the modes are found to match quite well with the experimental values. Table III shows a comparison of the calculated and experimental $\gamma_{i}$ for eight observed Raman modes. To calculate the thermal expansion coefficient $\alpha$, one needs to evaluate the total specific heat $C_{\mathrm{V}}$ and average Grüneisen parameter $\gamma_{\mathrm{av}}$. Using Einstein's specific heat relation, $C_{i}=R\left[x_{i}^{2} \exp \left(x_{i}\right)\right] /\left[\exp \left(x_{i}-1\right)\right]^{2}$, where $R$ is the gas constant and $x_{i}=\hbar \omega_{i} / k_{\mathrm{B}} T$ is the dimensionless phonon energy (with $k_{\mathrm{B}}$ as the Boltzmann constant and $T$ as the temperature), the total specific heat $C_{\mathrm{V}}$ was obtained by summing over the $C_{i}$ for various modes ($i=1$ to 30). The thermal expansion coefficient is obtained using the expression, $\alpha=\left(\gamma_{\mathrm{av}} C_{\mathrm{V}}\right) /\left(3 V_{\mathrm{m}} B_{\mathrm{o}}\right)$, where $\gamma_{\mathrm{av}}=\left(\Sigma p_{i} C_{i} \gamma_{i}\right) / C_{\mathrm{V}}$, with $p_{i}$ as the number of phonons or branches of frequency $\omega_{i}$ at the Brillouin zone center, $V_{\mathrm{m}}$ as the molar volume, and $B_{\mathrm{o}}$ as the bulk modulus. The molar volume is determined to be $1.2 \times 10^{-4} \mathrm{~m}^{3} /$ mole, and the calculated value (DFT) of $\alpha=15.6 \times 10^{-6} \mathrm{~K}^{-1}$ is in good agreement with the reported value. The contribution to the total $\alpha$ only from the Raman active phonons (our experiment) is obtained as $\alpha_{\text {Raman }}=1.2 \times 10^{-6} \mathrm{~K}^{-1}$, which is about $6 \%$ of the total experimentally reported $\alpha$ at $300 \mathrm{~K}$ [16]. Thus, significant contribution to total $\alpha$ by other modes (IR and silent) is evident. Using DFT, we have also obtained the volume thermal expansion coefficient vs temperature behavior, as shown in Fig. 8. The PTE behavior is similar to the recently reported trend using XRD experimental results [16]. Appreciably, it turns out that the calculated $\alpha\left(15.6 \times 10^{-6} \mathrm{~K}^{-1}\right)$ using Grüneisen parameters $\gamma_{i}$ for all modes is in good agreement $(\sim 80 \%)$ with $\alpha_{\mathrm{V}}$ (experimental) [16] at $300 \mathrm{~K}$, suggesting thermal expansion properties like $\mathrm{Zn}(\mathrm{CN})[2,7]$ and AgCCN [10] are well described by generalized gradient approximation calculations within the QHA. However, our DFT predicts a negative volume expansion at low temperature $(<120 \mathrm{~K})$, while the experimentally observed volumetric thermal expansion coefficient $\alpha_{\mathrm{V}}$ is reported to be positive in the $4-300 \mathrm{~K}$ range [16]. This difference between the reported experimental data and our calculations could be because the experiments have been carried out on powder samples, whereas our computation is on an ideal crystal. Furthermore, in the reported experimental results [16], the atomistic configurations have been extracted from the diffraction data using the reverse Monte Carlo method; subsequently, these configurations were used to calculate various thermal expansion coefficients. We believe the methodologies adopted in the reported experiment and our computation can explain the differences observed in the two cases. The small discrepancy between experimental and calculated values in AgCCN is partly attributed to QHA [10]. We can see from the phonon dispersion plots and the partial phonon DOS plotted for different volumes used in the QHA (not shown in the paper) that under HPs (volume contraction), the phonon modes corresponding to the CN librations are the major contributors to phase instability and can lead to the observed structural phase transition. However, under volume expansion (which can correspond to the change in temperature), the phonon modes corresponding to $\mathrm{H}$ and its bonding atoms tend to become unstable. Thus, vibrations involving the $\mathrm{H}$ atom are primarily responsible for the observed nonlinearity in the thermal expansion coefficient.

![](./images/814586770560647169_8.jpg)

FIG. 8. Thermal expansion behavior of $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$ calculated at the relaxed lattice parameters.

As discussed, the flexible Co-C-N-H-N-C-Co linkages do not exhibit any thermal expansion along the $\langle 101\rangle$ direction due to the resultant effect of orientation of the bonds along the linkages [20] and the negative thermal contribution of local transverse CN vibration (CN librational), neutralizing any expansion. This implies that any thermal expansion in basal plane lattice parameter $a(b)$ results into a concomitant reduction in the $c$ axis. Therefore, from this picture of geometric flexibility, the effect of the coupling between lattice parameters $a$ and $c$ on thermal expansion is understandable. In the context of a colossal thermal expansion, the compressibility (reciprocal of the bulk modulus $B_{0}$ ) of the flexible crystals often gives rise to the existence of either a moderate or a colossal thermal expansion because the Grüneisen parameter of the phonon modes, representing their respective mode anharmonicity, appeared to have a normal value [2,20], as found in our present $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$ system. Since Grüneisen parameters are found to be normal, their thermal expansion is solely related to their compressibility, viz., the smaller the compressibility, the larger the CTE, and vice versa. A recent DFT calculation [20] indicates a relatively shallow energy surface vs lattice parameter in AgCCN than what is observed in $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$, suggesting a smaller value of compressibility of $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$. In our present calculation, we obtain $B_{0}=138$ GPa, which is larger than $\sim 7-10$ GPa as found in AgCCN [15,20]. The lower value of $B_{0}$ in AgCCN is argued to be associated with the weak $\mathrm{Ag}^{+} \ldots \mathrm{Ag}^{+}$metallophilic interaction [2,19] and hence the colossal thermal expansion. However, in the absence of any metallophilic interaction, unlike AgCCN, $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$ possesses less compressibility, leading to exhibition of a moderate thermal expansion. The present Raman investigation at HP and lattice dynamics calculations provide insight into the relative role of different phonon modes in contributing to thermal expansion in $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$.


## IV. CONCLUSION

To conclude, we have identified the optical phonon modes responsible for NTE phenomena in $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$ using Raman spectroscopy as a function of pressure and first-principles calculations. Grüneisen parameters $\gamma_{i}$ for all phonon modes are obtained from our calculations. Mode assignments have been carried out using the computed frequencies and eigenvectors. A few phonon modes in $\mathrm{H}_{3}[\mathrm{Co}(\mathrm{CN})_{6}]$ are soft, and their contributions to NTE arises from CN-librational modes of the Co-C-N-H-N-C-Co linkages. The calculated values of the thermal expansion coefficient $\alpha$ using Grüneisen parameters are in good agreement with the reported experimental value. Upon increase in pressure, instability in the ambient trigonal phase is found at 2.3 GPa. The HP phase exhibits PIA at 11 GPa. Anharmonicity of several phonon modes and their contribution to the thermal expansion has been illustrated.

## ACKNOWLEDGMENTS

K.K.M. thanks M. P. Janawadkar and B. V. R. Tata for encouragement and the director of the Indira Gandhi Centre for Atomic Research for support. K.K.M. also thanks T. R. Ravindran for fruitful discussion. K.K.M. acknowledges the Bhabha Atomic Research Centre for a visiting scientist position.

---

[1] T. A. Mary, J. S. O. Evans, T. Vogt, and A. W. Sleight, *Science* **272**, 90 (1996).

[2] A. L. Goodwin, M. Calleja, M. J. Conterio, M. T. Dove, J. S. O. Evans, D. A. Keen, L. Peters, and M. G. Tucker, *Science* **319**, 794 (2008).

[3] T. R. Ravindran, A. K. Arora, and T. A. Mary, *Phys. Rev. Lett.* **84**, 3879 (2000).

[4] T. R. Ravindran and A. K. Arora, *Phys. Rev. Lett.* **86**, 4977 (2001).

[5] T. R. Ravindran, A. K. Arora, and T. A. Mary, *J. Phys. Condens. Matter* **13**, 11573 (2001).

[6] T. R. Ravindran, A. K. Arora, and T. A. Mary, *Phys. Rev. B* **67**, 064301 (2003).

[7] T. R. Ravindran, A. K. Arora, S. Chandra, M. C. Valsakumar, and N. V. Chandra Shekar, *Phys. Rev. B* **76**, 054302 (2007).

[8] R. Rao, S. N. Achary, A. K. Tyagi, and T. Sakuntala, *Phys. Rev. B* **84**, 054107 (2011).

[9] K. Kamali, T. R. Ravindran, C. Ravi, Y. Sorb, N. Subramanian, and A. K. Arora, *Phys. Rev. B* **86**, 144301 (2012).

[10] P. Hermet, J. Catafesta, J.-L. Bantignies, C. Levelut, D. Maurin, A. B. Cairns, A. L. Goodwin, and J. Haines, *J. Phys. Chem. C* **117**, 12848 (2013).

[11] A. L. Goodwin, J.-L. Chaplot, H. Schober, and T. A. Mary, *Phys. Rev. Lett.* **86**, 4692 (2001).

[12] R. Mittal, S. L. Chaplot, H. Schober, A. I. Kolesnikov, C.-K. Loong, C. Lind, and A. P. Wilkinson, *Phys. Rev. B* **70**, 214303 (2004).

[13] R. Mittal, S. L. Chaplot, and H. Schober, *Appl. Phys. Lett.* **95**, 201901 (2009).

[14] G. Ernst, C. Broholm, G. R. Kowach, and A. P. Ramirez, *Nature* **396**, 147 (1998).

[15] A. L. Goodwin, D. A. Keen, and M. G. Tucker, *Proc. Natl. Acad. Sci. USA* **105**, 18708 (2008).

[16] D. A. Keen, M. T. Dove, J. S. O. Evans, A. L. Goodwin, L. Peters, and M. G. Tucker, *J. Phys. Condens. Matter* **22**, 404202 (2010).

[17] M. J. Conterio, A. L. Goodwin, M. G. Tucker, D. A. Keen, M. T. Dove, L. Peters, and J. S. O. Evans, *J. Phys. Condens. Matter* **20**, 255225 (2008).

[18] K. Kamali, C. Ravi, T. R. Ravindran, R. M. Sarguna, T. N. Sairam, and G. Kaur, *J. Phys. Chem. C* **117**, 25704 (2013).

[19] H. Fang, M. T. Dove, and K. Refson, *Phys. Rev. B* **90**, 054302 (2014).

[20] M. Calleja, A. L. Goodwin, and M. T. Dove, *J. Phys. Condens. Matter* **20**, 255226 (2008).

[21] J. S. O. Evans, T. A. Mary, and A. W. Sleight, *J. Solid State Chem.* **133**, 580 (1997).

[22] A. Perakis, E. Sarantopoulou, Y. S. Raptis, and C. Raptis, *Phys. Rev. B* **59**, 775 (1999).

[23] B. A. Weinstein and R. Zallen, in *Light Scattering in Solids IV*, edited by M. Cardona and G. Guntherodt (Springer-Verlag, Berlin, 1984), pp. 463.

[24] R. Haser, B. Bonnet, and J. Rozere, *J. Mol. Struct.* **40**, 177 (1977).

[25] J. Roziere and J. Tomkinson, *Chem. Phys.* **45**, 447 (1980).

[26] G. Kresse and J. Furthmuller, *Phys. Rev. B* **54**, 11169 (1996).

[27] G. Kresse and J. Hafner, *Phys. Rev. B* **49**, 14251 (1994).

[28] G. Kresse and J. Furthmuller, *Phys. Rev. B* **54**, 11169 (1996).

[29] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[30] A. Togo, F. Oba, and I. Tanaka, *Phys. Rev. B* **78**, 134106 (2008).

[31] V_Sim atomic visualization package. Available online from http://inac.cea.fr/L_Sim/V_Sim/index.en.html.

[32] W. G. Fateley and F. R. Dollish, *Infrared and Raman Selection Rules for Molecular and Lattice Vibrations* (Wiley-Interscience, New York, 1972).

[33] B. Batlogg, A. Jayaraman, J. E. Van Cleve, and R. G. Maines, *Phys. Rev. B* **27**, 3920(R) (1983).

[34] A. K. Arora, T. Sato, T. Okada, and T. Yagi, *Phys. Rev. B* **85**, 094113 (2012).

[35] H. C. Choi, Y. M. Jung, I. Noda, and S. B. Kim, *J. Phys. Chem. B* **107**, 5806 (2003).