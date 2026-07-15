17 September 2024

# Hydrogen Absorption Promoted by Surface Melting: Guidelines for High-Pressure Superhydride Synthesis

Ryuhei Sato¹, Lewis Conway², Di Zhang³, Chris Pickard², Kazuto Akagi³, Kartik Sau³, Li Hao³, Shin-ichi Orimo³

1. The University of Tokyo
2. University of Cambridge
3. Tohoku University

## Abstract

The synthesis of new superhydrides with high superconducting Tc is challenging due to the high temperatures and pressures required. Here, we used machine-learning potential molecular dynamics simulations to investigate the initial stage of superhydride formation in calcium hydrides. Upon contact with high-pressure H2, the surface of CaH2 melts, leading to CaH4 formation. High pressure reduces the formation enthalpy for liquid superhydride as an intermediate state. Consequently, excess pressure above equilibrium shifts the balance towards superhydride formation and lowers the activation energy, promoting the hydrogenation reaction. Based on these thermodynamic insights, we propose superhydride synthesis guidelines focused on bulk properties: superhydride (product) melting temperature and pressure-dependent hydrogenation enthalpy, readily determined through supplementary calculations during structure prediction workflows.

## Keywords

Surface melting, Machine learning potential, Molecular Dynamics, Superhydride

Posted on 17 September 2024 — CC-BY 4.0 — This is a preprint and has not been peer reviewed. Data may be preliminary. — https://doi.org/10.26434/chemrxiv-2024-2v5l6-v3

# Hydrogen Absorption Promoted by Surface Melting: Guidelines for High-Pressure Superhydride Synthesis

Ryuhei Sato$^{1,2*}$, Lewis J. Conway$^{1,3}$, Di Zhang$^{1}$, Chris J. Pickard$^{1,3}$, Kazuto Akagi$^{1}$, Kartik Sau$^{1,4}$, Hao Li$^{1}$, Shin-ichi Orimo$^{1,5\dagger}$

$^{1}$Advanced Institute for Materials Research (WPI-AIMR), Tohoku University, 2-1-1 Katahira, Aoba-ku, Sendai 980-8577, Japan.
$^{2}$Department of Materials Engineering, the University of Tokyo, 7-3-1 Hongo Bunkyo-ku, Tokyo 113-8656, Japan.
$^{3}$Department of Materials Science and Metallurgy, University of Cambridge, 27 Charles Babbage Road, Cambridge CB3 0FS, United Kingdom.
$^{4}$Mathematics for Advanced Materials Open Innovation Laboratory (MathAM-OIL), National Institute of Advanced Industrial Science and Technology (AIST), c/o Advanced Institute for Materials Research (AIMR), Tohoku University, 2-1-1 Katahira, Aoba-ku, Sendai 980-8577, Japan.
$^{5}$Institute for Materials Research, Tohoku University, 2-1-1 Katahira, Aoba-ku, Sendai 980-8577, Japan.

\*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp
$^\dagger$Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

https://doi.org/10.26434/chemrxiv-2024-2v5l6-v3 ORCID: https://orcid.org/0000-0002-5503-0982 Content not peer-reviewed by ChemRxiv. License: CC BY 4.0

**ABSTRACT.** The synthesis of new superhydrides with high superconducting $T_\text{c}$ is challenging due to the high temperatures and pressures required. Here, we used machine-learning potential molecular dynamics simulations to investigate the initial stage of superhydride formation in calcium hydrides. Upon contact with high-pressure $\text{H}_2$, the surface of $\text{CaH}_2$ melts, leading to $\text{CaH}_4$ formation. High pressure reduces the formation enthalpy for liquid superhydride as an intermediate state. Consequently, excess pressure above equilibrium shifts the balance towards superhydride formation and lowers the activation energy, promoting the hydrogenation reaction. Based on these thermodynamic insights, we propose superhydride synthesis guidelines focused on bulk properties: superhydride (product) melting temperature and pressure-dependent hydrogenation enthalpy, readily determined through supplementary calculations during structure prediction workflows.

Hydride synthesis is an important technology in various fields represented by hydrogen storage [1,2] and superconductivity [3]. Among them, binary superhydrides with high hydrogen-to-metal (H/M) ratio were reported to have high $T_\text{c}$ values [4–11]. For example, $T_\text{c}$ of $\text{LaH}_{10}$ [4–6] and $\text{CaH}_6$ [7–9] were 250–260 K at 180 GPa and 210 K at 160 GPa. It may be possible for room-temperature superconductors to be realized in ternary or quaternary hydride materials [12–15]. Superhydrides are usually obtained by the close collaboration between theoretical simulations and experiments. Here, as an initial step, structure search methods such as metaheuristic methods [4,7,10-13] and random search [14,15] based on density functional theory (DFT) calculations have proposed novel structures. Subsequently, proposed superhydrides are realized by high-pressure synthesis using a diamond anvil cell (DAC). Although there might be a few exceptions, such as for $\text{LaH}_{10}$ [5], high-temperature heating by laser irradiation is usually required to promote reactions. This implies that superhydride synthesis involves kinetically slow processes or reactions with high activation energies. Therefore, physical insights into the reactions are important to obtain efficient synthesis routes. However, measurements in microregions within DAC are limited to specific techniques such as white X-ray diffraction and Raman spectroscopy. In addition, since interfacial reactions involve large numbers of atoms, it is difficult to apply DFT calculations owing to large computational costs. Therefore, to the best of our knowledge, no studies have been carried out to directly analyze hydrogenation reaction dynamics, and the guidelines underpinning superhydride synthesis remain unclear.

Molecular dynamics (MD) simulations are one of the most effective computational methods for the direct observation of dynamic phenomena. For example, MD simulations with interatomic potentials have contributed to the elucidation of phenomena such as superionic conduction mechanisms [16,17], carbon nanotube formation [18], and protein folding [19]. The recent developments of machine-learning potentials [20–24] have accelerated and facilitated the potential construction of new materials. These developments have enabled MD simulations to be applied to a wider variety of materials [14,15,25–28]. In fact, machine-learning potential (MLP) MD simulations have accurately reproduced the phase transition behavior of high-pressure $\text{H}_2$, which is strongly affected by the simulation cell size [25]. In addition, machine learning potentials are frequently used to explore the bulk properties of hydrides [26,27] and the structure of ternary systems [14,15].

In this study, to provide a physical insight into the superhydride synthesis, we directly observed $\text{CaH}_2$ hydrogenation by MLP-MD simulations. $\text{CaH}_2$ is an ionic crystal composed of $\text{Ca}^{2+}$ and $\text{H}^-$ with an hcp Ca lattice [29]. On the other hand, $\text{CaH}_4$ forms an fcc Ca lattice [29], which contains $\text{H}^-$ ions and $\text{H}_2^{\delta-}$ dimers. Therefore, the $\text{CaH}_2$ hydrogenation reaction, $\text{CaH}_2 + \text{H}_2 \leftrightarrow \text{CaH}_4$, is employed as an example of superhydride synthesis that requires (1) metal lattice reconstruction and (2) hydrogenation starting from stoichiometric ionic crystals whose anion sites are fully occupied by $\text{H}^-$.

$\text{CaH}_2$ hydrogenation occurs via surface melting at high temperatures. Figure 1 shows snapshots of a MLP-MD simulation of the $\text{CaH}_2$(100) surface in contact with high-density $\text{H}_2$ at $P = 40$ GPa and $T = 1500$ K. During MLP-MD simulation, the surface structure was disordered (ex. t = 100 ps and 116 ps) to absorb H atoms into the bulk. Since $\text{CaH}_2$ lacks $\text{H}_2$-molecule-like dimers ($\text{H}_2^{\delta-}$), whereas $\text{CaH}_4$ contains them, confirming H absorption during disordering from the purple lines in the bulk. After this H absorption, an ordered structure including $\text{H}_2^{\delta-}$ was formed, i.e. solid $\text{CaH}_4$ (t = 160 ps.). Figure 2(a) shows the time series of temperature, pressure, and H/M ratio during this MLP-MD simulation. As shown in the figure, the H/M ratio continued to increase during MLP-MD simulation, showing the H absorption during the disordering process. The H/M ratio reached four at around 120 ps, indicating that almost all $\text{CaH}_2$ reacts with $\text{H}_2$ to form $\text{CaH}_4$.

\*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp
†Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

![](./images/1250198784646840356_1.jpg)

FIG. 1. Snapshots of atomic configurations during $CaH_2$ hydrogenation via surface melting in a MLP-MD simulation of the $CaH_2(100)/H_2$ interface at 1500 K under 40 GPa.

The black line in Fig. 2(a) shows the results of MLP- MD simulation at $T = 1200$ K. During the MD simulation, the H/M ratio slightly increased due to the $H_2$ adsorption on the surface and $H_2$ absorption in the subsurface layer. However, the H/M ratio was still close to two, showing that the surface melting and subsequent hydrogenation did not occur at $T = 1200$ K. Figure 2(b) shows the adaptive common neighbor analysis, a-CNA [30], of Ca atoms during MLP-MD simulation. During the structural disordering, Ca formed neither an hcp Ca nor an fcc Ca lattices. This shows that $CaH_x$ during hydrogenation formed an amorphous or liquid-like structure rather than solid $CaH_2$ or $CaH_4$. After 120-ps, the fcc Ca ratio ($\approx CaH_4$) increased, confirming the formation of solid $CaH_4$. Note that the fcc Ca ratio was considered to be underestimated due to the large thermal oscillation at 1500 K. In fact, when this calculation cell was quenched to 300 K, the fcc Ca ratio increased to 86 %.

The local structure around H atoms during surface melting is similar to that around H atoms in $CaH_4$, providing an increased number of absorption sites compared with local environments for H atoms in $CaH_2$. Figure 3(a) shows a time-averaged persistence diagram (PD) [31-33] of the MLP-MD simulation of the $CaH_2(100)/H_2$ interface at 1500 K under 40 GPa with surface melting (rainbow color density plot) compared with that at 1200 K under 40 GPa without surface melting (grayscale contour plot). In Fig. 3(a), new ring structures appear around (birth, death) = (b, d) = (1.0, 2.1) only when $CaH_2$ hydrogenation occurs. This shows that these rings are important for the $CaH_2$ hydrogenation reaction. Figure 3(b) shows a PD of the MLP-MD simulation for the $CaH_2(100)/H_2$ interface at 1500 K under 40 GPa (rainbow color density plot) compared with that for bulk $CaH_4$ at 1500 K under 40 GPa (grayscale contour plot). As shown in Fig. 3(b), the rings in bulk $CaH_4$ are in good agreement with these new rings obtained during $CaH_2$ hydrogenation.

![](./images/1250198784646840356_2.jpg)

FIG. 2. (a) Time series of temperature ($T$), pressure ($P$) and H/M ratio during MLP-MD simulations of the $CaH_2(100)/H_2$ interface at (black) 1200 K and (red) 1500 K at 40 GPa. (b) Time series of Ca structure ratio (hcp, fcc, others) obtained by a-CNA during MLP-MD simulation of the $CaH_2(100)/H_2$ interface at 1500 K under 40 GPa. Here, not only the amorphous and disordered phases but also the surface and subsurface Ca atoms are classified as "Others" owing to the lack of neighboring Ca atoms.

*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp

$^\dagger$Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

Therefore, we conclude that liquid CaH₄, rather than liquid CaH₂, formed as an intermediate state during the CaH₂ hydrogenation. This is further confirmed by the time series of PDs during MLP-MD simulation, since these rings appear before 120 ps, the time before Ca atoms form an fcc lattice (Fig. S1[34]), showing that the local structure for H atoms in amorphous CaHₓ is similar to those in bulk CaH₄. Thus, the H content in the bulk increased during hydrogenation owing to the formation of H absorption sites in CaH₄. The rate-limiting step was not likely to be H diffusion in the bulk or H₂ dissociation on the surface, but rather the formation of absorption sites as discussed in Section SI. 2 of the Supporting Information [34].

![](./images/1250198784646840356_3.jpg)

FIG. 3. Time-averaged persistence diagrams (PDs) calculated using H atoms near the CaHₓ bulk during MLP-MD simulations. Rainbow color density plots in (a) and (b) show PDs of MLP-MD simulation for the CaH₂(100)/H₂ interface at 1500 K under 40 GPa between 25 and 160 ps. On the other hand, grayscale contours represent MLP-MD simulations for (a) the CaH₂(100)/H₂ interface at 1200 K under 40 GPa between 25 and 160 ps and (b) the CaH₄ bulk at 1500 K under 40 GPa. Here, H atoms with a minimum Ca–H distance of 3 Å or shorter were included in this persistent homology analysis to analyze H atoms in CaHₓ and near the interface.

Figure 4(a) shows the pressure-dependence of the H/M ratio after 1-ns MLP-MD simulations. Here, (100) and (010) surfaces were analyzed. From Fig. 4(a), it is confirmed that the CaH₂ hydrogenation reaction occurs at 1500 K above 30 GPa in this MLP. Conversely, hydrogenation does not occur at 1200 K at any pressure. This indicates that surface melting is a thermally activated process, whose reaction temperature is between 1200 K and 1500 K. At the CaH₂(010)/H₂ interface, hydrogenation does not occur at any pressure (blue circles). This result is associated with the surface energies of (100) and (010). The surface energy of (010) in vacuum is determined to be 0.034 eV/Å by DFT calculation, which is lower than 0.04 eV/Å of (100). Thus, although this is a qualitative discussion based on the surface energy under vacuum conditions, this hydrogenation behavior suggests that the surface melting is affected by the interfacial energy between CaH₂ and H₂. Another possible reason for hydrogenation occurring only on the (100) surface is the difference in the in-plane density of Ca atoms between the (100) and (010) surfaces. The CaH₂(010) surface forms a layer of close-packed hcp Ca atoms as shown in the inset in Fig. 4(a). In contrast, the CaH₂(100) surface exhibits a stepped structure (the inset in Fig. 4(a)), with a lower atomic density in the same plane compared to the (010) surface. Consequently, even though the thickness of the CaH₂ slab is several nm (Fig. S2[34]), once liquid CaH₄ forms, the reaction proceeds spontaneously, reducing both the volume and enthalpy due to the applied pressure perpendicular to the surface.

Hydrogenation via surface melting can be explained by the following thermodynamic argument. The conventional equation for surface melting for CaH₄ without hydrogenation is as follows,
$$\Delta G = \Delta G_{\text{fus}} + \Delta \gamma_{\text{interface}}, \, (1)$$
$$\Delta \gamma_{\text{interface}} = \gamma_{\text{CaH}_4\text{(s)-CaH}_4\text{(l)}} + \gamma_{\text{CaH}_4\text{(l)-H}_2\text{(l)}} - \gamma_{\text{CaH}_4\text{(s)-H}_2\text{(l)}} \cdot (2)$$

On the other hand, when CaH₂ hydrogenation reaction is involved,
$$\Delta G = \Delta G_{\text{fus}} + \Delta G_{\text{hyd}} + \Delta \gamma_{\text{interface}}, \, (3)$$
$$\Delta \gamma_{\text{interface}} = \gamma_{\text{CaH}_2\text{(s)-CaH}_4\text{(l)}} + \gamma_{\text{CaH}_4\text{(l)-H}_2\text{(l)}} - \gamma_{\text{CaH}_2\text{(s)-H}_2\text{(l)}} \cdot (4)$$

In these equations, $\Delta G_{\text{fus}}$ denotes the Gibbs free energy of CaH₄ fusion (CaH₄(s) ↔ CaH₄(l)), whereas $\Delta G_{\text{hyd}}$ represents that of the CaH₂ hydrogenation reaction, CaH₂(s) + H₂(l) ↔ CaH₄(s). The symbols (s) and (l) indicate the solid and liquid phases, respectively. $\gamma_{\text{A-B}}$ represents the energy of the interface between A and B. Since $\Delta G_{\text{hyd}}$ becomes negative under high pressure, where the hydrogenation reaction occurs, the surface melting is promoted, as described by Eq. (3). As a first approximation, here, we focus only on the enthalpies of the homogeneous system of CaH₂, CaH₄, and H₂, neglecting the entropy and interfacial energy

*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp
†Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

contributions. Figure 4(b) shows the pressure dependence of the enthalpies for CaH₄ fusion ($\Delta H_{\text{fus}}$) and liquid CaH₄ formation by CaH₂ hydrogenation ($\Delta H_{\text{fus}}$+$\Delta H_{\text{hyd}}$). The time-averaged enthalpies derived from the 100-ps MLP-MD simulations at various temperatures were fitted and extrapolated to determine the enthalpy at 0 K (Figs. S3 and S4 [34]), which was employed in these reaction enthalpy calculations.

As shown in Fig. 4(b), $\Delta H_{\text{fus}}$+$\Delta H_{\text{hyd}}$ is lower than $\Delta H_{\text{fus}}$ at pressures above 30 GPa. Consequently, surface melting via hydrogenation could occur at temperatures below the melting point of CaH₄ at pressures over 30 GPa. Therefore, liquid CaH₄ became solid CaH₄ phase after hydrogenation, since the driving force, hydrogenation enthalpy, was no longer applied to the system. Figure 4(c) shows the enthalpy changes at each stage of CaH₂ hydrogenation via surface melting. The enthalpy of liquid CaH₄, serving as an intermediate state, gradually decreases with increasing pressure, confirming how elevated pressures reduce the activation energy and enhance the hydrogenation reaction. This finding explains why we sometimes need to apply, in experiments, an excess pressure above equilibrium pressure predicted by DFT calculations.

In summary, superhydride formation occurs via surface melting, where the excess pressure over equilibrium pressure lowers the activation energy needed to form a liquid superhydride phase as an intermediate. Here, the hydrogenation reaction in superhydride formation is thermodynamically governed by the fusion enthalpy of the superhydride products ($\Delta H_{\text{fus}}$), the hydrogenation reaction enthalpy ($\Delta H_{\text{hyd}}$), and the interfacial energies ($\gamma_{\text{interface}}$). Therefore, by carefully controlling these thermodynamic properties with the appropriate temperature and pressure, the reaction pathway can be optimized. This understanding aligns well with the experimental observation that the use of BH₃NH₃ and a metal precursor is effective for superhydride synthesis [6,9]. In this process, the metal precursor is not hydrogenated until BH₃NH₃ releases H₂ molecules upon heating. This makes the enthalpy of the starting material (i.e., metal and H₂ from BH₃NH₃) less stable than that of a metal hydride and H₂ molecules under high pressure. This further reduces the activation energy and promotes the formation of a liquid superhydride phase as an intermediate state. As a result, surface melting is expected to occur even at lower temperatures than that for metal hydrides.

![](./images/1250198784646840356_4.jpg)

FIG. 4. Thermodynamics of CaH₂ surface melting. (a) H/M ratio of (black) CaH₂(100)/H₂ interface at 1200 K, (red) at 1500 K, and (blue) CaH₂(010)/H₂ interfaces at 1500 K as a function of $P$ (GPa) after 1-ns MLP-MD simulations. The insets show the lateral view of CaH₂ (100) and (010) slabs. (b) Reaction enthalpy per atom as a function of pressure. (c) Enthalpy change during CaH₂ hydrogenation relative to that for solid CaH₂(s) +H₂(l) under 10, 30, and 50 GPa.

The surface melting in our study is also similar to fluorite-type CaH₂ synthesis near ambient pressure in

*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp
$^\dagger$Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

the previous report [35]. In this reaction, fluorite-type
$\mathrm{CaH_2}$ is obtained by substituting $\mathrm{Ca^{2+}}$ with dopants
such as $\mathrm{La^{3+}}$ and $\mathrm{Y^{3+}}$. Therefore, it is expected that this
substitution plays a similar role with the surface
melting or disordering. The synthesis temperature
(1073 K) is close to the melting point of $\mathrm{CaH_2}$ at
ambient pressure. Comparison of the previous study
with the present study suggests that it is important for
superhydride synthesis to control experimental
conditions based on dopants and melting point.

Owing to the thermodynamics of surface melting
described above, theoretical structure search
workflows are expected to provide substantial insights
into experimental synthesis in the future. Specifically,
after predicting a new superhydride structure, one can
(i) calculate the pressure dependence of hydrogenation
reaction enthalpy and (ii) estimate the melting point of
the product to evaluate its feasibility for subsequent
experiments. Although constructing MLPs for
interfacial reactions, as in this study, is time-
consuming, workflows for bulk systems have already
been established [36]. Therefore, it is straightforward
to develop MLPs for a homogeneous bulk system and
estimate a rough melting temperature from the
temperature-dependent enthalpy calculations.
Consequently, we expect that the guiding principles
derived from hydrogenation reactions via surface
melting in our MLP-MD simulations, (i) the pressure
dependence of hydrogenation reaction enthalpies and
(ii) the melting temperature of superhydride products,
significantly accelerate the synthesis of new
superhydrides, integrating them with conventional
computational techniques.

## ACKNOWLEDGMENTS
We appreciate the fruitful discussion with Prof.
Sanliang Ling. This work was supported by GteX
Program Japan Grant Number JPMJGX23H1 and
JSPS KAKENHI Grant-in-Aid for Early-Career
Scientists, No. JP23K13542. The computation in this
work was done using the facilities of the
Supercomputer Center, the Institute for Solid State
Physics, the University of Tokyo and supercomputing
resources at Cyberscience Center, Tohoku University.

[1] S. Orimo, Y. Nakamori, J. R. Eliseo, A.
Züttel, C. M. Jensen, Complex hydrides for hydrogen
storage, Chem. Rev. **107**, 4111–4132 (2007).

[2] R. Mohtadi, S. Orimo, The renaissance of
hydrides as energy materials, Nat. Rev. Mater. **2**,
16091 (2017).

[3] L. Boeri, et. al., The 2021 room-temperature
superconductivity roadmap, J. Phys.: Condens. Matter.
**34**, 183002 (2022).

[4] H. Liu, I. I. Naumov, R. Hoffmann, N. W.
Ashcroft, R. J. Hemley, Potential high-Tc
superconducting lanthanum and yttrium hydrides at
high pressure, Proc. Natl. Acad. Sci. U. S. A. **114**,
6990–6995 (2017).

[5] A. P. Drozdov et., Superconductivity at
250 K in lanthanum hydride under high pressures,
Nature **569**, 528–531 (2019).

[6] M. Somayazulu, A. Muhtar, A. K. Mishra, Z.
M. Geballe, M. Baldini, Y. Meng, V. V. Struzhkin, R.
J. Hemley, Evidence for superconductivity above 260
K in lanthanum superhydride at megabar pressures,
Phys. Rev. Lett. **122**, 027001 (2019).

[7] H. Wang, J. S. Tse, K. Tanaka, T. Iitaka, Y.
Ma, Superconductive sodalite-like clathrate calcium
hydride at high pressures, Proc. Natl. Acad. Sci. U. S.
A. **109**, 6463–6466 (2012).

[8] Z. Li et. al., Superconductivity above 200 K
discovered in superhydrides of calcium, Nat. Commun.
**13**, 2863 (2022).

[9] L. Ma et. al., High-temperature superconducting
phase in clathrate calcium hydride $\mathrm{CaH_6}$ up to 215 K
at a pressure of 172 GPa, Phys. Rev. Lett. **128**, 167001
(2022).

[10] I. A. Troyan et. al., Anomalous high-
temperature superconductivity in $\mathrm{YH_6}$, Adv. Mater. **33**,
2006832 (2021).

[11] W. Chen et. al., Synthesis of molecular
metallic barium superhydride: pseudocubic $\mathrm{BaH_{12}}$,
Nat. Commun. **12**, 273 (2021).

[12] X. He, W. Zhao, Y. Xie, A. Hermann, R. J.
Hemley, H. Liu, Y. Ma, Predicted hot
superconductivity in $\mathrm{LaSc_2H_{24}}$ under pressure, Proc.
Natl. Acad. Sci. U. S. A. **121**, e2401840121, (2024).

[13] L. Liu et. al., Generic rules for achieving
room-temperature superconductivity in ternary
hydrides with clathrate structures, Phys. Rev. B **107**,
L020504 (2023).

[14] P. P. Ferreira, L. J. Conway, A. Cucciari, S.
Cataldo, F. Giannessi, E. Kogler, L. T. F. Eleno, C. J.
Pickard, C. Heil, L. Boeri, Search for ambient
superconductivity in the Lu-N-H system, Nat.
Commun. **14**, 5367 (2023).

[15] K. Dolui, L. J. Conway, C. Heil, T. A. Strobel,
R. P. Prasankumar, C. J. Pickard, Feasible route to
high-temperature ambient-pressure hydride
superconductivity, Phys. Rev. Lett. **132**, 166001
(2024).

[16] M. Parrinello, A. Rahman, P. Vashishta,
Structural transitions in superionic conductors, Phys.
Rev. Lett. **50**, 1073–1076 (1983).

[17] F. Shimojo, M. Kobayashi, Molecular
dynamics studies of molten AgI. I. Structure and

*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp

†Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

dynamical properties, J. Phys. Soc. Jpn. 60,
3725-3735 (1991).

[18] Y. Shibuta, S. Maruyama, Molecular
dynamics simulation of formation process of single-
walled carbon nanotubes by CCVD method, Chem.
Phys. Lett. 382, 381-386 (2003).

[19] J. A. McCammon, B. R. Gelin, M. Karplus,
Dynamics of folded proteins, Nature 267, 585-590
(1977).

[20] J. Behler, M. Parrinello, Generalized neural-
network representation of high-dimensional potential-
energy surfaces, Phys. Rev. Lett. 98, 146401 (2007).

[21] A. P. Bartók, M. C. Payne, R. Kondor, G.
Csányi, Gaussian approximation potentials: the
accuracy of quantum mechanics without the electrons,
Phys. Rev. Lett. 104, 136403 (2010).

[22] H. Wang, L. Zhang, J. Han, E. Weinan,
DeePMD-kit: a deep learning package for many-body
potential energy representation and molecular
dynamics, Comput. Phys. Comm. 228, 178-184
(2018).

[23] V. L. Deringer, A. P. Bartók, N. Bernstein, D.
M. Wilkins, M. Ceriotti, G. Csányi, Gaussian process
regression for materials and molecules, Chem. Rev.
121, 10073-10141 (2021).

[24] C. J. Pickard, Ephemeral data derived
potentials for random structure search, Phys. Rev. B
106, 014102 (2022).

[25] B. Cheng, G. Mazzola, C. J. Pickard, M.
Ceriotti, Evidence for supercritical behaviour of high-
pressure liquid hydrogen, Nature 585, 217-220 (2020).

[26] P. T. Salzbrenner, S. H. Joo, L. J. Conway, P.
I. C. Cooke, B. Zhu, M. P. Matraszek, W. C. Witt, C.
J. Pickard, Developments and further applications of
ephemeral data derived potentials, J. Chem. Phys. 159,
144801 (2023).

[27] N. Wang, S. Huang, Molecular dynamics
study on magnesium hydride nanoclusters with
machine-learning interatomic potential, Phys. Rev. B
102, 094111 (2020).

[28] B. W. Hamilton, P. Yoo, M. N. Sakano, M.
M. Islam, A. Strachan, High-pressure and temperature
neural network reactive force field for energetic
materials, J. Chem. Phys. 158, 144117 (2023).

[29] The space groups of $CaH_2$ and $CaH_4$ are
Pnma and I4/mmm. Nevertheless, considering only Ca
position, Ca atoms in Pnma $CaH_2$ and I4/mmm $CaH_4$
form hcp and fcc structures, respectively based on a-
CNA analysis.

[30] A. Stukowski, Structure identification
methods for atomistic simulations of crystalline
materials, Modelling Simul. Mater. Sci. Eng. 20,
045021 (2012).

[31] I. Obayashi, T. Nakamura, Y. Hiraoka,
Persistent homology analysis for materials research
and persistent homology software: HomCloud, J. Phys.
Soc. Jpn. 91, 091013 (2022).

[32] Y. Hiraoka, T. Nakamura, A. Hirata, E.
Escolar, K. Matsue, Y. Nishiura, Hierarchical
structures of amorphous solids characterized by
persistent homology, Proc. Natl. Acad. Sci. U. S. A.
113, 7035-7040 (2016).

[33] R. Sato, K. Akagi, S. Takagi, K. Sau, K. Kisu,
H. Li, S. Orimo, Topological data analysis of ion
migration mechanism, J. Chem. Phys. 158, 144116
(2023).

[34] See Supplemental Material [url] for
simulation methodology, discussion on the rate-
limiting step during hydrogenation, persistence
diagrams, initial configuration, time averaged
enthalpy during MLP-MD simulations, which
includes Refs. [37-50].

[35] H. Mizoguchi, S. Park, T. Honda, K. Ikeda,
T. Otomo, H. Hosono, Cubic Fluorite-Type $CaH_2$ with
a Small Bandgap, J. Am. Chem. Soc., 139, 11317-
1320 (2017).

[36] Y. Zhang, H. Wang, W. Chen, J. Zeng, L.
Zhang, H. Wang, E. Weinan, DP-GEN: A concurrent
learning platform for the generation of reliable deep
learning based potential energy models, Comput. Phys.
Commun. 253, 107026 (2020).

[37] G. Kresse and J. Furthmüller, Efficient
iterative schemes for ab initio total-energy
calculations using a plane-wave basis set, Phys. Rev.
B, 54, 11169-11186 (1996).

[38] G. Kresse, J. Hafner, Ab initio molecular
dynamics for liquid metals, Phys. Rev. B, 47, 558-561
(1993).

[39] G. Kresse, J. Furthmüller, Efficiency of ab-
initio total energy calculations for metals and
semiconductors using a plane-wave basis set, Comput.
Mat. Sci., 6, 15-50 (1996).

[40] J. P. Perdew, K. Burke, M. Ernzerhof,
Generalized gradient approximation made simple,
Phys. Rev. Lett., 77, 3865-3868 (1996).

[41] P. E. Blöchl, Projector augmented-wave
method, Phys. Rev. B, 50, 17953-17979 (1994).

[42] J. S. Tse, D. D. Klug, S. Desgreniers, J. S.
Smith, R. Flacau, Z. Liu, J. Hu, N. Chen, D. T. Jiang,
Structural phase transition in $CaH_2$ at high pressures,
Phys. Rev. B, 75, 134108 (2007).

[43] K. Shimamura, S. Fukushima, A. Koura, F.
Shimojo, M. Misawa, R. V. Kalia, A. Nakano, P.
Vashishta, T. Matsubara, S. Tanaka, Guidelines for
creating artificial neural network empirical
interatomic potential from first-principles molecular
dynamics data under specific conditions and its
application to $\alpha$-Ag2Se, J. Chem. Phys., 151, 124303
(2019).

*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp

$^\dagger$Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

[44] J. Zeng et. al., DeePMD-kit v2: A software package for deep potential models, J. Chem. Phys., 159, 054801 (2023).

[45] L. Zhang, J. Han, H. Wang, W. Saidi, R. Car, E Weinan, End-to-end symmetry preserving inter- atomic potential energy model for finite and extended systems, In Proceedings of the 32nd International Conference on Neural Information Processing Systems (NIPS'18), Curran Associates Inc., Red Hook, NY, USA, 4441–4451 (2018).

[46] D. Lu, W. Jiang, Y. Chen, L. Zhang, W. Jia, H. Wang, M. Chen, DP compress: a model compression scheme for generating efficient deep potential models, J. Chem. Theory Comput., 18, 5555–5567 (2022).

[47] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, J. Comput. Phys., 117, 1–19 (1995).

[48] S. Nosé, A unified formulation of the constant temperature molecular dynamics methods, J. Chem. Phys., 81, 511–519 (1984).

[49] W. G. Hoover, Constant-pressure equations of motion, Phys. Rev. A, 34, 2499–2500 (1986).

[50] A. Stukowski, Visualization and analysis of atomistic simulation data with OVITO, the open visualization tool, Modelling Simul. Mater. Sci. Eng., 18, 015012 (2010).

*Ryuhei Sato: rsato@material.t.u-tokyo.ac.jp

$^\dagger$Shin-ichi Orimo: shin-ichi.orimo.a6@tohoku.ac.jp

https://doi.org/10.26434/chemrxiv-2024-2v5l6-v3 ORCID: https://orcid.org/0000-0002-5503-0982 Content not peer-reviewed by ChemRxiv. License: CC BY 4.0
