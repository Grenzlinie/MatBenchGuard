![](./images/811999922042699776_1.jpg)

# Prediction of composition for stable half-Heusler phases from electronic-band-structure analyses

L. Offernes *, P. Ravindran, C.W. Seim, A. Kjekshus

Department of Chemistry, University of Oslo, P.O. Box 1033, Blindern, N-0315 Oslo, Norway

Received 14 March 2007; accepted 3 April 2007
Available online 12 April 2007

## Abstract
This report describes a procedure to predict the frequently occurring non-stoichiometry of the half-Heusler XYZ alloys (viz. deviations from the equiatomic 1:1:1 composition and the usually accompanied narrow homogeneity regions) from ab initio calculated electronic-band-structure characteristics. The essential feature of this approach is to utilize the valence electron content (VEC) and the calculated electronic band structure to expose factors that according to rigid-band considerations should determine the possible deviations from 1:1:1 stoichiometry and direction of the stable solid-solution regions. These means have been used to predict the direction of equilibrium solid-solution regions for a number of ternary phase diagrams that comprise half-Heusler phases and the predictions have been tested with experimental data from literature and presently synthesized and microprobe analysed samples of NiTiSn, PtTiSn, CoTiSb, PtMnSb, NiMnSb, and CoMnSb. The predictions are made based on maximum band filling of bonding states identified through the crystal-orbital-Hamilton population (COHP) analysis and density-of-states (DOS) integration.

© 2007 Elsevier B.V. All rights reserved.

**Keywords**: Stoichiometry; Intermetallics; Half-Heusler phases; COHP; VEC

---

## 1. Introduction

Our previous detailed examinations of the half-Heusler alloys AuMnSn and AuMnSb [1–3] revealed that they do not take the exact 1:1:1 composition at $400\ ^{\circ}\text{C}$. These phases rather show narrow composition ranges, indeed in the vicinity of the ideal equiatomic composition, as displayed in the phase diagrams for the Au–Mn–Sn and Au–Mn–Sb systems [2,3] in Fig. 1. The formation of phases with compositions deviating from the equiatomic composition commonly associated with the half-Heusler phases has intrigued and challenged us for some time and the aim of this report is to expose factors that can be responsible for the deviation from the simple 1:1:1 stoichiometry and establish whether such deviations are likely to be common for half-Heusler phases in general.

Another aspect of interest is the unusual complexity of such phase diagrams and the impact the individual inherent features impose on the preparation procedure and sample quality. In the isothermal sections of the Au–Mn–Sn and Au–Mn–Sb phase diagrams in Fig. 1, single-phase regions are marked by black areas, two-phase fields are represented by tie-lines or shown as areas connecting two phases existing in equilibrium at the given temperature, and three-phase fields are depicted by triangles connecting the phases concerned. The relative amounts of each phase in two- or three-phase fields follow from the lever rule (see, e.g., Ref. [4]). If temperature is also considered as variable, the phase diagrams become three-dimensional and aspects such as phase formation and stability become important. The AuMnSn and AuMnSb phases are, e.g., peritectically formed at $\sim$470 and $\sim$575 $^{\circ}\text{C}$, respectively, thus defining the upper stability limits for these phases. The different appearances (and complexity) of these phase diagrams emphasize the importance of careful choice of nominal composition of samples for exploration of location and composition region for a genuine ternary phase. For interpretation of phase-analytical data it may also be of vital importance to have a qualified opinion on the main features of the phase diagram concerned.

The family of half-Heusler phases includes well over 100 phases and have been studied extensively in recent years (see, e.g., Refs. [5–12]). Half-Heusler phases are known to form from

---

* Corresponding author. Tel.: +47 22857397; fax: +47 22855565.
E-mail address: Laila.offernes@kjemi.uio.no (L. Offernes).

0925-8388/$ – see front matter © 2007 Elsevier B.V. All rights reserved.
doi:10.1016/j.jallcom.2007.04.038

![](./images/811999922042699776_2.jpg)
![](./images/811999922042699776_3.jpg)

Fig. 1. Phase diagrams for (a) AuMnSn and (b) AuMnSb at 400 °C [2,3]. Single-phase fields are shown as black areas, tie-lines are represented by solid and dashed lines, and three-phase fields by triangles connecting coexisting phases.

a wide variety of different elements and in a typical phase with general formula XYZ, X is a heavy transition metal, Y is a light transition metal or a rare-earth metal, and Z is a late main-group element (most frequently Sb or Sn). These phases exhibit a great variety of electronic states and physical properties. The properties of the half-Heusler phases vary somewhat systematically with the valence-electron content (VEC; note, valences prescribed by the periodic table) as manifested, e.g., by changes in electronic conductivity and magnetic characteristics with VEC [7,13]. Semiconducting features are associated with VEC=8 and 18, which represent highly preferred electron configurations fulfilling the octet or expanded octet rule. So-called half-metallic ferromagnetic (HMF) materials are found among phases with VEC=22 (see, e.g., Refs. [14–16]). These phases have large magnetic moments and in the electronic structure of these phases the majority-spin channel exhibits metallic characteristics, while the minority-spin channel exposes a semiconductor-like gap at the Fermi level ($E_{\text{F}}$). This situation theoretically results in 100% spin-polarized materials which are technologically important in the field of spintronics. HMF materials are, e.g., incorporated in magnetic multilayers which, due to the spin-dependent scattering of electrons, exhibit giant magnetoresistance (GMR). Some of the HMF half-Heusler phases also exhibit interesting magneto-optical properties, e.g., the large magneto-optical Kerr effect (MOKE) found for PtMnSb [17]. Materials with high MOKE are used in the erasable data-storage technology [18] for read/write applications.

Both theoretical and experimental investigations of half-Heusler phases have been extensive, but most studies of the half-Heusler phases seem to simply postulate an equiatomic composition. The focus of these studies has not been on the stoichiometry of the phases, but rather concentrated on specific properties [12,19–21] or trends in properties throughout the family [6,7,22,23]. Only a few of the ternary systems which contain half-Heusler phases have been systematically mapped in the form of phase diagrams [2,3,17], making it difficult to evince a qualified opinion on composition issues. There have, e.g., been published over 300 articles about the (anticipated, see Refs. [16,24,25]) HMF phases PtMnSb and NiMnSb, but while some reports [26,27] account for phase purity of the samples used, only few have documented accurate data on composition. In the theoretical treatment of these and other half-Heusler phases the equiatomic composition has almost invariably been postulated, but also experimental founded papers appear to take the equiatomic composition for granted. The authors have questioned this assumption and wondered whether this is only false for a few Mn-based phases with large VEC or whether solid-solution regions and deviations from the equiatomic composition are the rule, rather than the exceptions for a larger portion of half-Heusler phases.

To understand non-stoichiometry and its origin it is important to consider the crystal structure and possible mechanisms for disorder and composition alterations. The cubic crystal structure of the half-Heusler phases is of the AlLiSi type (Fig. 2(a); space group $F\overline{4}3m$; see Ref. [1]). The AlLiSi-type structure can be regarded as an ordered version of the $\text{CaF}_2$ type. Another way to look at the structure is to start with the $\text{Cu}_2\text{MnAl}$-type structure of the $\text{X}_2\text{YZ}$ full-Heusler phases (Fig. 2(b)). The latter structure consists of four interpenetrating fcc-lattices, two of which consist of X atoms, one of Y atoms, and one of Z atoms. If one of the X atoms is removed from the $\text{Cu}_2\text{MnAl}$-type structure according to an ordered pattern, the resulting structure (viz. the $\text{Cu}_2\text{MnAl}$ type with one empty site) has become of the AlLiSi type exhibited by the half-Heusler phases. Referring to the general formula XYZ, X takes a coordination number of 8 (four X–Y bonds in tetrahedral configuration and another four X–Z bonds in identical configuration). The Y and Z sites are crystallographically identical, both have coordination numbers of 10 with capped (by four X) octahedral geometry, amounting to four Y–X and six Y–Z bonds and four Z–X and six Z–Y bonds, respectively. The structure has no variable positional parameters, leaving the fully ordered, stoichiometric XYZ phases with the cubic lattice parameter ($a$) as the only structural variable.

As established for AuMnSn and AuMnSb, half-Heusler phases are not doomed to be stoichiometric and ordered [1–3]. At first glance it is natural to assume that the solid-solubility regions of AuMnSn and AuMnSb are brought about by (i) addition of Au, Mn, and/or Sn/Sb atoms to the just mentioned empty

![](./images/811999922042699776_4.jpg)

Fig. 2. Crystal structures of (a) half-Heusler (AlLiSi type, general formula XYZ) and (b) full-Heusler (Cu₂MnAl type, general formula X₂YZ) phases.

crystallographic site, (ii) partial removal (subtraction) of one constituent or (iii) substitution of one of the constituent by another. Other more complex non-stoichiometry variants arise on combination of the pure-cultivated mechanisms (i)-(iii), e.g., in the form of imbalanced distribution between and subsequent disorder on the mutually equivalent Mn and Sn sites as suggested for PtMnSn [28,29]. The solid-solution fields of AuMnSn and AuMnSb lie on opposite sides of the equiatomic composition (see Fig. 1) and this show that also in these cases no single of the mechanisms (i)-(iii) can satisfactory explain the deviations from 1:1:1 stoichiometry.

The rest of this paper is organized as follows. Section 2 gives a brief account of the computational and experimental methods used to collect the data foundation for the deliberations. The findings are presented and discussed in Section 3 which concludes with an overview of stoichiometry predictions according to rigid-band considerations [30,31] based on the calculated electronic-band-structure data. The predictions are then confronted with experimental findings in Section 4 and overall conclusions are finally summarized in Section 5.

## 2. Data collection

Comparatively detailed descriptions of the computational and experimental methods used in this work can be found elsewhere [32-34], but a brief account is also included here for the convenience of the readers. A considerable part of the theoretical background is in fact already published in an earlier communication [32], but all computational findings considered in this paper will nevertheless be presented as if they represented fresh results.

### 2.1. Computational methods

All calculations are performed within the framework of the generalized-gradient approximation (GGA), with exchange-correlation according to Perdew et al. [35], and density-functional theory (DFT) in the local-density approximation (LDA).

First-principles, self-consistent, tight-binding linear-muffin-tin-orbital calculations within the atomic-sphere approximation (TB-LMTO-ASA) [36] were performed to obtain the density-of-states (DOS) characteristics for all phases considered in this paper. The calculations are semi-relativistic (i.e., without spin-orbit coupling, but with all other relativistic effects included) taking also into account combined correction terms. The basis sets consisted of appropriate s, p, and d orbitals for the elements. The integration over the Brillouin zone (BZ) was made by the tetrahedron method, sampling a grid of 245 k points in the irreducible part of BZ (4096 in the full BZ). The crystal structure was divided into space filling, slightly overlapping, spheres centred on each of the atomic sites. An empty sphere is included at the empty crystallographic 4d site of the AlLiSi-type structure. The Wigner-Seitz-sphere radii used were scaled so that the total volume of all the spheres equalled the volume of the unit cell. Experimental lattice parameters were used in the calculations (listed in Table 1) for all the phases considered here.

Full potential linear muffin-tin orbital (FLMTO) calculations [37] have also been used to obtain the DOS for some of the phases (see Refs. [33,34] for details).

Crystal-orbital-Hamiltonian population (COHP) plots were calculated according to the TB-LMTO code as implemented in the TBLMTO-47 package [38]. The COHP, which is the Hamiltonian-population-weighted DOS, is a partitioning scheme for the band-structure energy in terms of orbital-pair contributions [39,40]. A negative value for the COHP indicates bonding states, whereas positive COHP values indicate antibonding states, which provides an energy-resolved visualization of the chemical bonding.

### 2.2. Experimental methods

Samples were made by melting (heating at 1100–1300 °C for about 1 min under vigorous shaking) weighed amounts of the elements in sealed, evacuated, silica-glass tubes. High purity elements were used as starting materials for the syntheses (Ti: Mackay 99.99%; Mn: Aldrich 99.98%; Co: Koch-Light

<table><caption>Table 1 Experimental lattice parameters from the present study or literature data quoted from Refs. [1,3,7,13,21,28], the condition of optimum bonding (relative to $E_{\text{F}}$) according to COHP, and the composition or dominant composition ranges for the experimentally investigated phases</caption>
<thead>
<tr>
<th>VEC<sub>eq</sub></th>
<th>vec<sub>eq</sub></th>
<th>Phase XYZ<br>(X₂YZ)</th>
<th>$a$ (Å)<sup>a</sup></th>
<th>“Optimum”<br>COHP (eV)</th>
<th>DOS estimate<br>(no. of e⁻)</th>
<th>VEC<sub>st</sub></th>
<th>vec<sub>st</sub></th>
<th>Composition ($x$,$y$,$z$)</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Composition range ($x$,$y$,$z$)–($x$,$y$,$z$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>16</td>
<td>5.33</td>
<td>FeTiSn</td>
<td>6.056</td>
<td>+0.38</td>
<td>+0.2</td>
<td>~16.2</td>
<td>5.4</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>5.67</td>
<td>FeTiSb</td>
<td>5.997</td>
<td>+0.03</td>
<td>+0.2</td>
<td>~17.2</td>
<td>5.73</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CoTiSn</td>
<td>5.957</td>
<td>+0.17</td>
<td>+1</td>
<td>~18</td>
<td>6.0</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>6.0</td>
<td>NiTiSn</td>
<td>5.941, 5.926</td>
<td>0</td>
<td>0</td>
<td>18</td>
<td>6.0</td>
<td>(0.33,0.33,0.33)</td>
</tr>
<tr>
<td>–</td>
<td>–</td>
<td>(Ni₂TiSn)</td>
<td>6.06</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>PtTiSn</td>
<td>6.168, 6.163</td>
<td>0</td>
<td>0</td>
<td>18</td>
<td>6.0</td>
<td>(0.33,0.33,0.33)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>CoVSn</td>
<td>5.98</td>
<td>0</td>
<td>0</td>
<td>18</td>
<td>6.0</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CoTiSb</td>
<td>5.832, 5.875</td>
<td>0</td>
<td>0</td>
<td>18</td>
<td>6.0</td>
<td>(0.33,0.33,0.33)</td>
</tr>
<tr>
<td>19</td>
<td>6.33</td>
<td>NiTiSb</td>
<td>5.872</td>
<td>–0.80</td>
<td>–1</td>
<td>~18</td>
<td>6.0</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CoVSb</td>
<td>5.766</td>
<td>–0.25</td>
<td>–1</td>
<td>~18</td>
<td>6.0</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>6.67</td>
<td>IrMnSn</td>
<td>6.182</td>
<td>+0.45</td>
<td>+1</td>
<td>~21</td>
<td>7.0</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>RhMnSn</td>
<td>5.947<sup>b</sup></td>
<td>+0.30</td>
<td>+0.8</td>
<td>~20.8</td>
<td>6.93</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>7.0</td>
<td>IrMnSb</td>
<td>6.164</td>
<td>+0.15</td>
<td>+0.2</td>
<td>~21.2</td>
<td>7.07</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>RhMnSb</td>
<td>6.145</td>
<td>+0.32</td>
<td>+0.5</td>
<td>~21.5</td>
<td>7.17</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CoMnSb</td>
<td>5.875, 5.865–5.878</td>
<td>0</td>
<td>0</td>
<td>21</td>
<td>7.0</td>
<td>(0.27,0.40,0.33)–(0.37,0.32,0.31)</td>
</tr>
<tr>
<td>–</td>
<td>–</td>
<td>(Co₂MnSb)</td>
<td>5.923, 5.919</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>PtMnSn</td>
<td>6.264</td>
<td>+0.45</td>
<td>+0.5</td>
<td>~21.5</td>
<td>7.17</td>
<td></td>
</tr>
<tr>
<td>22</td>
<td>7.33</td>
<td>NiMnSb</td>
<td>5.909, 5.914–5.981</td>
<td>0</td>
<td>0</td>
<td>22</td>
<td>7.33</td>
<td>(0.30,0.34,0.36)–(0.41, 0.29, 0.30)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>PtMnSb</td>
<td>6.201, 6.194–6.225</td>
<td>0</td>
<td>0</td>
<td>22</td>
<td>7.33</td>
<td>(0.30, 0.37, 0.33)–(0.33, 0.32, 0.35)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>AuMnSn</td>
<td>6.323</td>
<td>+0.01</td>
<td>+0.2</td>
<td>~22.2</td>
<td>7.4</td>
<td></td>
</tr>
<tr>
<td>23</td>
<td>7.67</td>
<td>AuMnSb</td>
<td>6.379</td>
<td>–0.47</td>
<td>–0.5</td>
<td>~22.5</td>
<td>7.5</td>
<td></td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9"><sup>a</sup> Values given in roman and italics are from literature and present study, respectively.</td>
</tr>
<tr>
<td colspan="9"><sup>b</sup> From volume optimized TB-LMTO calculations.</td>
</tr>
</tfoot>
</table>

99.998%; Ni: Goodfellow 99.98%; Sn: Merck 99.95%; Sb: Goodfellow 99.99%; Pt: Rasmussen 99.99%; Au: Rasmussen 99.95%). The initial heat treatment was concluded by quenching the samples from the molten state into water. The samples were then annealed for 30 days at $400\,^{\circ}\text{C}$ and finally quenched into water.

Powder X-ray diffraction (PXD) was used to confirm the presence of the desired half-Heusler phase with the characteristic AlLiSi-type structure. The data was also utilized to derive the lattice parameter ($a$) for the half-Heusler phases (and when relevant also for the full-Heusler phases) and to establish the possible presence of other phases.

Composition analysis was performed using an automatic wavelength-dispersive CAMECA SX 100 electron microprobe fitted with an energy-dispersive system. Acceleration voltage of 20 keV, sample current of 15–20 nA, and counting time of 10–20 s were used. Pure metals or oxides were used as standards and a thin layer of carbon was evaporated on the metallographic specimens used for electron microprobe analyses. Matrix corrections were performed by the CAMECA software and the achieved analytical precision ($2\sigma$; evaluated on the basis of repeated analyses of individual grains) is better than $\pm 1\%$. Unless otherwise stated, the composition for a given half-Heusler phase represents a mean value of at least three independent measurements. Back-scattered-electron (BSE) scans were used for imaging the samples. In BSE images the contrast is given by the average atomic weight of the different phases, e.g., a phase mainly containing heavy atoms will appear as light colored. Optical microscopy and BSE were used to check the homogeneity of the half-Heusler phases considered and to establish whether a sample had reached equilibrium or not.

A well-chosen selection of a limited number of samples with nominal composition meant to establish the solid-solution region of a phase really requires prior information about the phase diagram. As can be seen from the diagrams in Fig. 1, the ideal locations for such surveying samples would be at points within the three-phase fields surrounding the phase in question. Provided equilibrium is reached, such samples would then contain the ternary phase with different terminal compositions, outlining the solid-solution region at the temperature concerned. Since the location of such phase fields usually is as unknown as the phase diagrams themselves, our selection of nominal compositions was made according to a common pattern around (not too close or too far from) the equiatomic composition. In addition, one sample with nominal composition corresponding to the equiatomic composition was prepared for each system. The nominal composition of a sample is given with the general formula $\text{X}_{x}\text{Y}_{y}\text{Z}_{z}$, where

$$
x+y+z=1 \tag{1}
$$

e.g., using fractions rather than percentages. For the systems subjected to experimental examination the following nominal compositions ($x$,$y$,$z$) was used: (0.33, 0.33, 0.33), (0.20, 0.50,

0.30), (0.25, 0.35, 0.40), (0.40, 0.35, 0.25), and (0.45, 0.20,
0.35) for the Ni–Ti–Sn, Pt–Ti–Sn, Co–Ti–Sb, Ni–Mn–Sb, and
Co–Mn–Sb systems and (0.33, 0.33, 0.33), (0.20, 0.50, 0.30),
(0.20, 0.35, 0.45), (0.25, 0.20, 0.55), (0.30, 0.50, 0.20), (0.38,
0.20, 0.42), (0.40, 0.30, 0.30), and (0.40, 0.40, 0.20) for the
Pt–Mn–Sb system.

In the analyses of the annealed samples, we have recognized
a number of factors which have influenced the interpretation
of the findings. (i) Several of the samples turned out to be in
local equilibrium, but were hampered by macro segregation
(e.g., low-density crystals floating on the top of a higher-density
melt or vice versa). This phenomenon (which is easily observed
in vertically mounted metallographic cross sections) causes
changes in composition throughout the sample (and possibly
phase exclusion in bulk XRD analyses). (ii) Characteristic lamel-
lar microstructures are formed in eutectic solidification of a
melt. In such solidified melts the crystals of some of the phases
involved can be too small for proper microprobe analyses. (iii)
Two of the systems investigated experimentally (Ni–Ti–Sn and
Co–Mn–Sb) contained both full- and half-Heusler phases. The
similarity in structure and lattice parameter made it difficult
to distinguish these by XRD alone. (iv) Some of the inves-
tigated phases (notably NiMnSb and CoMnSb) showed clear
signs of distinct variation in homogeneity region with temper-
ature. When a sample which comprises a phase with a large
solid-solubility region at high temperatures and a narrower com-
position region at lower temperatures is cooled, parts of the phase
field become unstable and the associated excess of one or two
of the components will either be trapped (thus causing tension
and/or composition inhomogeneities) or precipitate crystals of
another phase inside the crystal domain of the reformed phase.
(v) Peritectic phases are formed on crystals of another phase
in a reaction between these crystals and a melt. As the new
phase forms, the reaction rate gradually slows down consequent
on increased solid-diffusion paths. The result is often seen as a
core of the original phase inside the peritectically formed phase.
Note that cases (iv) and (v) refer to samples that have not reached
local equilibrium (for general background on non-equilibrium
situations see Ref. [4]).

Specific cases in relation to half-Heusler phases are consid-
ered in Section 4.

### 3. Theoretical considerations on non-stoichiometry of half-Heusler phases

The hitherto performed examinations of the bonding prop-
erties of half-Heusler phases are based on calculations for a
postulated “ideal” 1:1:1 composition [32]. However, according
to information from COHP, neither of our introductory examples
AuMnSn and AuMnSb obtains an optimized bonding situation
for the equiatomic composition. The condition for “optimized”
bonding according to COHP occurs when all bonding states
are filled and all antibonding states are left empty, viz. a phase
which experiences optimized bonding should have all nega-
tive COHP values within the energy region of the occupied
states, and all positive values are associated with the unoccu-
pied states, i.e., above $E_{\text{F}}$ [41]. For phases where bonding is not
optimized, COHP is used to establish the difference in energy
(in eV) between the actually filled states and states with bond-
ing character (corresponding stability evaluations have earlier
been derived from DOS [42]). Under the supposition that the
electronic band structure remains virtually unchanged upon rel-
atively minor subtraction, addition or substitution of atoms, one
can achieve this by removing or adding electrons (so-called
rigid-band filling). This rigid-band approach usually works very
well for substitutional half-Heusler phases [32]. The forma-
tion of non-stoichiometric half-Heusler phases is probably quite
common considering the fact that theoretic calculations give
non-optimized bonding for most of the phases in the equiatomic
configuration. Our predictions presuppose that the composition
of the phase under consideration remains reasonably close to
the equiatomic composition, but will be shifted toward the VEC
which maximize the bonding interactions. The direction of the
composition shift is toward the line in the phase diagram corre-
sponding to this VEC (see below) and a possible solid-solution
region is predicted to lie along the same line. To predict the
composition shift and solid-solution region for a given phase,
the COHP plots and integrated DOS profiles originate from
calculations for the ideal equiatomic 1:1:1 phase were consulted.

Non-stoichiometric ternary half-Heusler phases are conve-
niently represented by the formula $\text{X}_{x}\text{Y}_{y}\text{Z}_{z}$. When the phase
under consideration is entered into the phase diagram, $x$, $y$, and
$z$ becomes variable between 0 and 1, viz. fractional variables are
in this case more convenient than the commonly used percent-
ages. An equiatomic stoichiometric ternary half-Heusler phase
will then have the composition $\text{X}_{1/3}\text{Y}_{1/3}\text{Z}_{1/3}$. Trivially, the com-
position variables will be connected by Eq. (1) and the VEC
variable will thus be modified to:

$$
\text{vec} = \frac{\text{VEC}}{3} \tag{2}
$$

where vec represent the valence-electron content per formula
atom (viz. vec refers to $\text{X}_{1/3}\text{Y}_{1/3}\text{Z}_{1/3}$). The valence-electron con-
tribution from each constituent of a given half-Heusler phase is
specified as $u$ electrons from X, $v$ electrons from Y, and $w$ elec-
trons from Z (where $u$, $v$, and $w$ are fixed when X, Y, and Z are
defined). This in turn specifies vec as:

$$
\text{vec} = ux + vy + wz \tag{3}
$$

or combined with Eq. (1) as

$$
\text{vec}(x, y) = (u - w)x + (v - w)y + w, \tag{4}
$$

or correspondingly with the equivalent relation expressed with
the other variables. Eq. (4) represents a straight line trough the
isothermal X–Y–Z phase diagram. For VEC values correspond-
ing to the case when the stoichiometric equiatomic composition
is satisfied, the vec($x$,$y$) line will go through the equiatomic
composition and these particular VEC and $\text{vec}(x,y)$ values are
therefore denoted $\text{VEC}_{\text{eq}}$ and $\text{vec}_{\text{eq}}(x,y)$. In cases where the
electronic-structure characteristics indicate that the phase would
rather prefer a modified composition for stability reasons, VEC
and $\text{vec}(x,y)$ will be denoted $\text{VEC}_{\text{st}}$ and $\text{vec}_{\text{st}}(x,y)$. It should be
emphasized that Eq. (2) does not deal with defect situations that

![](./images/811999922042699776_5.jpg)

Fig. 3. (a) Schematic illustration of the relationship between $\text{vec}_{\text{eq}}(x,y)$ (solid line) and $\text{vec}_{\text{st}}(x,y)$ (dashed line) for a hypothetic half-Heusler phase $X_xY_yZ_z$ (see text). The equiatomic 1:1:1 composition is indicated by a small black dot in this and corresponding diagrams. (b) The field of interest for most of the investigated systems is well within the 50%X–50%Y–50%Z cut. The location of the equiatomic 1:1:1 composition is marked by a open circle in this and corresponding diagrams. The grey portion in part a corresponds to the section reproduced in part b.

comprise added or subtracted atoms from the half-Heusler structural unit cell. However, it may still be justified to choose Eq. (2) for simplicity, when the deviations from stoichiometry are small and the predictions are intended to be of a more qualitative rather than quantitative nature. VEC is then averaged over three atoms regardless of the true number of atoms in the unit cell.When $u$, $v$, and $w$ are specified one can represent the linear relationships for $\text{vec}_{\text{eq}}(x,y)$ and $\text{vec}_{\text{st}}(x,y)$ in an isothermal cross-section of the X–Y–Z phase diagram (see Fig. 3). Since the actual phase-composition problem in this case is related to the concentration region around the centre of gravity of the diagram (1/3, 1/3, 1/3) only the portion of the diagram around this point is reproduced in most of the following representations (see Fig. 3(b)).

Specific values of $\text{vec}_{\text{eq}}(x,y)$ and $\text{vec}_{\text{st}}(x,y)$ for all phases considered in some detail in this report are given in Table 1.

### 3.1. Preliminary testing with AuMnSn and AuMnSb

According to analyses of the band filling of bonding states, a system will gain extra stability when all bonding states are filled and all antibonding states are empty [31,43,44]. Gener-

![](./images/811999922042699776_6.jpg)

Fig. 4. DOS for (a) AuMnSn and (c) AuMnSb and COHP for (b) AuMnSn and (d) AuMnSb. $E_{\text{F}}$ is marked by vertical dashed lines, and in parts b and d the interactions among X–Z, Y–Z, and X–Y, atomic pairs are distinguished by solid, dashed, and dotted profiles, respectively.

ally, the bonding and antibonding states are separated by a gap in semiconductors, a gap in the minority-spin channel in half-metals, and a so-called pseudogap (a deep valley in the DOS curve in the vicinity of $E_{\text{F}}$) in intermetallic compounds. The bonding and antibonding states in solids can easily be located using COHP. The COHP for AuMnSn (Fig. 4(b)) shows that maximum filling of the bonding states occurs at 0.01 eV above $E_{\text{F}}$ and on conferring this finding with the corresponding DOS profile (Fig. 4(a)) this amounts to addition of electrons up to the gap in the minority-spin channel, which in turn would convert AuMnSn into a HMF phase. Integration of DOS indicates that ~0.2 added electrons can be accommodated in bonding states. Hence, the predicted $\text{VEC}_{\text{st}}$ of AuMnSn is not 22 electrons, but rather ~22.2 electrons.

AuMnSb with the equiatomic composition has $\text{VEC}_{\text{eq}} = 23$. The COHP for this phase (Fig. 4(d)) shows that optimum bonding (viz. maximum filling of bonding states) occurs at 0.47 eV below $E_{\text{F}}$, which according to integration of DOS (Fig. 4(c)) corresponds to removal of about 0.5 electrons. Again one ends up at a gap in the minority-spin channel and the creation of a HMF state. The predicted value for $\text{VEC}_{\text{st}}$ of AuMnSb is accordingly 22.5 electrons.

Fig. 5(a, b) gives the lines for $\text{vec}_{\text{eq}}(x,y)$ and $\text{vec}_{\text{st}}(x,y)$ for AuMnSn and AuMnSb together with the predicted homogeneity regions [2] for the two phases. The actually observed composition regions of these phases are found in the vicinity of the equiatomic composition and between or on the lines. It is especially gratifying to note that the composition of the $\text{Au}_{x}\text{Mn}_{y}\text{Sn}_{z}$

![](./images/811999922042699776_7.jpg)

Fig. 5. Predicted equilibrium compositions or homogeneity regions for the (stable) (a) AuMnSn, (b) AuMnSb, (c) NiTiSn, (d) CoTiSb, (e) PtMnSb, and (f) NiMnSb phases, are marked by a grey disk in each diagram. The $\text{vec}_{\text{eq}}(x,y)$ and $\text{vec}_{\text{st}}(x,y)$ relations are given by solid and dashed lines, respectively, and the equiatomic composition by a black dot.

phase is predicted to lie below the $vec_{eq}(x,y)$ line, while the composition of the $Au_xMn_ySb_z$ phase is predicted to lie above the $vec_{eq}(x,y)$ line, as established experimentally (see also Fig. 1).

### 3.2. The semiconducting and HMF phases
Phases with $\text{VEC} = 18$ are predicted to be semiconductors. Semiconductors have filled bonding states and empty antibonding states separated by a gap, and accordingly optimized bonding. This trait of character must also be reflected in COHP. The HMF phases mimic the semiconducting case in the sense that they have a gap at $E_F$ in the minority-spin channel and thus a filled-band/empty-band configuration for this channel. A closer look at COHP shows that this configuration also optimizes bonding. As a result, both semiconducting and HMF phases satisfy the condition that $vec_{eq}(x,y)$ equals $vec_{st}(x,y)$. These phases are expected to take the exact equiatomic 1:1:1 composition or exist over a composition range along the $vec_{eq}(x,y)$ line.

DOS and COHP profiles for the $\text{VEC} = 18$ phase NiTiSn are given in Fig. 6, which manifest the "semiconductor gap" and the "optimized" COHP. The predicted location for the $\text{VEC} = 18$ phases NiTiSn and CoTiSb are given in Fig. 5(c, d) and the corresponding phase-diagrams for the $\text{VEC} = 22$ phases PtMnSb and NiMnSb are given in Fig. 5(e, f).

### 3.3. Predictions
For a phase which is neither semiconductor nor HMF, COHP plots should be able to demonstrate that optimum bonding can still be achieved by addition or subtraction of electrons (provided, of course, that the rigid-band assumption holds [30,32], which is often the case for alloys and intermetallic compounds). As for the gold phases (considered in Section 3.1), the predicted location of such half-Heusler phases tend toward the $vec_{st}(x,y)$ line. Fig. 7 shows a selection of ternary phase diagrams visualizing the predicted location of its half-Heusler inhabitant (numerical data are given in Table 1). The composition and possible homogeneity region are for all these phases predicted to be found in the vicinity of the equiatomic composition, located along and between the $vec_{eq}(x,y)$ and $vec_{st}(x,y)$ lines.

![](./images/811999922042699776_8.jpg)

Fig. 6. (a) DOS and (b) COHP for NiTiSn. $E_F$ is shown by vertical dashed lines. In part b the interactions among Ni-Sn, Ti-Sn, and Ni-Ti atomic pairs are distinguished by solid, dashed, and dotted profiles, respectively.

For the phases with $\text{VEC}_{eq} < 18$ we find that a certain amount of added electrons will lead to maximum filling of bonding states, thus increasing the stability of the phase which by this means come closer to the semiconducting $\text{VEC} = 18$ situation. For FeTiSn (16), FeTiSb (17), and CoTiSn (17) the predicted composition or composition region lie on the electron-rich side of the equiatomic composition (Fig. 7(a-c)). For phases with $\text{VEC} = 19$ loss of electrons will have the same effect, and the predicted homogeneity region and/or composition for NiTiSb and CoVSb is located above the $vec_{eq}(x,y)$ line in Fig. 7(d, e). RhMnSn (20) is reported to exist [45], but experimental data on composition, unit cell dimension, and magnetic moment are not available. This phase is nevertheless included in these considerations since it provide an example of a phase with VEC equally distant from the semiconducting and HMF situations. As can be seen from Fig. 7(f) the predicted stabilization occurs with an addition of electrons, viz. a preference for the HMF situation, in which magnetically non-bonding electrons on Mn are utilized for splitting of states and lowering of energy.

For several of the above considered phases the predicted deviation from $\text{VEC}_{eq}$ is large (addition or removal of some 0.5-1 electrons per formula unit) which implies that the postulated applicability of the rigid-band approximation strictly speaking no longer should be valid since for any real phase such large changes in VEC are likely to lead to significant alterations in electronic structure. In these cases more moderate composition changes are anticipated, may be associated with structural changes (as, e.g., reported for CoMnSb [26,28,46]).

### 3.4. Phase-analytical data from literature
As a first test of the validity of the way of thinking developed from the ternary gold-containing half-Heusler phases, we compare our predictions with composition information from literature. Data for IrMnSn (20), IrMnSb (21), RhMnSb (21), and PtMnSn (21) are presented in Fig. 8 and data for PtMnSb and NiMnSb are presented and discussed in Section 4 since fresh experimental data have been collected for these phases.

Masumoto et al. [47] has reported deviation from the equiatomic composition for IrMnSn (20) and as seen in Fig. 8(a), the actually observed composition is shifted in the direction predicted by the $vec_{st}(x,y)$ line, but the amount of added electrons are not as extensive as anticipated according to the rigid-band approach. Masumoto et al. reported only one composition value and conclusions on the homogeneity region can accordingly not be drawn. Turning to the corresponding Sb phase IrMnSb (21) where the anticipated deviation in composition is not as large as first expected owing to the fact that this phase is close to the HMF situation with $\text{VEC} = 22$ (Fig. 8(b)). A report [21] on deviation from the equiatomic composition is found, but this source only shifts the composition along the $vec_{eq}(x,y)$ line, not in the direction predicted for added electrons. For the isoelectric phase RhMnSb we also predict that addition of electrons is needed to stabilize the phase (Fig. 8(c)). Both van Engelen et al. [48] and Masumoto and Watanabe [47] report compositions other than

![](./images/811999922042699776_9.jpg)

Fig. 7. Predicted compositions or homogeneity regions for the (stable) (a) FeTiSn, (b) FeTiSb, (c) CoTiSn, (d) NiTiSb, (e) CoVSb, and (f) RhMnSn phases, are marked by a grey disk in each diagram. The $vec_{eq}(x,y)$ and $vec_{st}(x,y)$ relations are given by solid and dashed lines, respectively, and the equiatomic composition by a black dot.

1:1:1, but while the former authors confirm a rather large amount of added electrons the latter authors reports a composition along the $vec_{eq}(x,y)$ line. Without further experimental investigations of the Rh–Mn–Sb system it is difficult to judge whether these compositions coexist as parts of a larger homogeneity region.
Compared to other half-Heusler phases treated in the literature PtMnSn (21) is rather well surveyed with regard to composi- tion and the findings are appropriately documented in literature [29,49]. Our predictions again assume stabilization by addition of electrons, but the experimental compositions instead lie beau- tifully along the $vec_{eq}(x,y)$ line. Structural disorder is reported [29] for the PtMnSn phase and the present authors speculate that such encroachment itself may cause stabilization of an atomic arrangement which makes electronically induced adjustments unnecessary.

### 4. Experimental findings

To substantiate the predictions, we prepared 31 samples from 6 different systems which contain half-Heusler phases. Quali- tative investigation of the samples made by optical microscopy and BSE showed that quite a few of the samples had not reached proper equilibrium and some were hampered by macro seg- regation. Taken the low number of samples for each of the investigated phases and the indicative nature of our investigation, none of the samples where disregarded so that all information

![](./images/811999922042699776_10.jpg)

Fig. 8. Predicted location of composition compared with data from literature for the (stable) (a) IrMnSn [47], (b) IrMnSb [21], (c) RhMnSb [47,48], and (d) PtMnSn [29,49] phases. The equiatomic composition is marked by open circle, and composition data from literature are shown by filled symbols. The $vec_{eq}(x,y)$ and $vec_{st}(x,y)$ relations are given by solid and dashed lines, respectively.

gathered were used in some manner to shed light on the phase and system in question. The compositional findings for these phases are presented in Fig. 9.

To investigate whether a semiconducting half-Heusler phase more or less by definition is likely to take the exact equiatomic composition and relinquish the possibility for homogeneity regions, samples were made for the ternary systems Co–Ti–Sb, Ni–Ti–Sn, and Pt–Ti–Sn. The HMF phases PtMnSb and NiMnSb are well known, and although there exist a phase diagram for the Pt–Mn–Sb system [50] we took special interest in these phases. The CoMnSb (21) phase was chosen to represent a deviation from the HMF situation. The latter phase has been reported [26,28] to take both the AlLiSi- and $BiF_3$-type structure and although these structures are very similar the distinctions are likely to be important for stability reasons. However, we have taken the liberty to disregard such small deviations from the AlLiSi-type structure in the consideration of our samples.

### 4.1. NiTiSn

The NiTiSn (18) phase is predicted to be a semiconductor and experimentally measured NiTiSn crystals were found to be close to the 1:1:1 composition in all our samples. This should make comparison between data from computational calculations and experimental findings rather straightforward. The experimental samples from the Ni–Ti–Sn system are, however, “hampered” with the presence of the full-Heusler phase, $Ni_2TiSn$, from which the half-Heusler phase NiTiSn forms peritectically. In a couple of samples, the half-Heusler phase has formed on crystals of the full-Heusler phase leaving the samples in a far-from-equilibrium state after 4 weeks of annealing (see Fig. 10(a) and the accompanying figure caption). The full- and half-Heusler phases have similar atomic arrangements (see Fig. 2) and nearly equal lattice parameters which result in almost indistinguishable XRD patterns. In fact, from the inspection of XRD diagrams alone we concluded that a sample with the nominal composition $Ni_{45}Ti_{20}Sn_{30}$ contain large amounts of the half-Heusler phase. However, microprobe analyses showed that this was not the case at all. The sample contains large amounts of the full-Heusler phase and little of the half-Heusler phase. Two out of four samples were clearly not at equilibrium. The composition of the half-Heusler phase in these samples matched that of the samples that had reached equilibrium, viz. exhibit the equiatomic composition (Fig. 9(a)).

### 4.2. PtTiSn

Microprobe analysis of PtTiSn (18) also indicates that this phase takes the 1:1:1 composition (Fig. 9(b)). The present samples showed some internal macro segregation, but had reached local equilibrium, making the analysis quite uncomplicated. Too

![](./images/811999922042699776_11.jpg)

Fig. 9. Predicted location of composition compared with experimental data for the (stable) (a) NiTiSn, (b) PtTiSn, (c) CoTiSb, (d) PtMnSb, (e) NiMnSb, and (f) CoMnSb phases. The equiatomic composition is marked by open circle, present experimental data by filled circles (and open triangles for more uncertain data), and literature data by filled squares [27,47]. The $vec_{eq}(x,y)$ and $vec_{st}(x,y)$ relations are given by solid and dashed lines, respectively. About the scatter in the experimental data points in parts e and f see text for more details.

few samples were measured to justify a qualified opinion on the possible existence of a homogeneity region for the PtTiSn phase. There is, however, nothing from our investigation that indicates such a region.

### 4.3. CoTiSb

Microprobe analyses of the CoTiSb phase yielded a composition close to the stoichiometric formula and showed that the phase has little or no homogeneity region at $400\,^{\circ}\text{C}$ (Fig. 9(c); the spread in the analytical data turned out to be below the uncertainty of the microprobe technique). Also these samples showed some degree of macro segregation. We have confidence in the equiatomic composition estimate for this phase since our five samples are from at least three different phase fields. In a sample with the nominal composition $\text{Co}_{0.33}\text{Ti}_{0.33}\text{Sb}_{0.33}$ with some internal macro segregation, the CoTiSb phase seems to be in local equilibrium with small amounts of two Sb-rich Ti–Sb phases. Another sample (nominal composition $\text{Co}_{0.40}\text{Ti}_{0.35}\text{Sb}_{0.25}$) showed CoTiSb in equilibrium with a Ti-rich Ti–Sb phase and a Co-rich Co–Ti phase. A third three-phase field was found to exist between CoTiSb and two Co-rich Co–Sb phases in a sample with nominal composition $\text{Co}_{0.45}\text{Ti}_{0.20}\text{Sb}_{0.35}$. From these findings one can even produce a tentative phase-diagram sketch, that can be used for further investigations of the Co–Ti–Sb system.

![](./images/811999922042699776_12.jpg)

Fig. 10. BSE scan of sample with nominal composition (a) $Ni_{0.45}Ti_{0.20}Sn_{0.30}$ and (b) $Ni_{0.25}Ti_{0.35}Sn_{0.40}$. The sample in part a have not reached equilibrium, the core of the grey crystals consists of the full-Heusler phase while the porous rim contains the half-Heusler phase. The lighter colored matrix consists of two Ni-Sn phases (visible by optical microscopy, but not seen in the BSE images due to poor contrast). The grey crystals in part b have the exact 1:1:1 composition and have established equilibrium with the light colored crystals of a Ti-Sn phase and a Sn-rich melt (which has solidified into an eutectic of (Sn) and a Ti-Sn phase).

### 4.4. PtMnSb

The homogeneity region indicated for PtMnSb in Fig. 9(d) closely matches the region previously reported by Masumoto and Watanabe [50]. The present measurements generally yielded less Pt than the earlier study, but the deviation (approximately 0-1 at.%) can not properly be regarded as significant since the discrepancy lies within the uncertainty for the microprobe analyses. There were few problems in the analyses of these samples which proved to be homogenous and to have reached equilibrium. It is, however, important to emphasize that the PtMnSb phase exhibits a definite solid-solution region and that the implied non-stoichiometry has consequences for both sample preparation and the comparisons with the results derived according to the idealized computational model.

### 4.5. NiMnSb

The accurate microprobe analyses by Hanssen et al. [27] concluded with a composition close to the equiatomic formula for the NiMnSb phase. Our findings show a more scattered pattern (see Fig. 9(e)), but the findings enclose the equiatomic composition. The homogeneity region for NiMnSb appears to be relatively large, at least at high temperatures. In most of the present samples NiMnSb turned out to be inhomogeneous, the composition variation being clearly visible in BSE images. Such inhomogeneities are also reported by Otto et al. [26]. The NiMnSb crystals have been formed at higher temperatures and during the cooling to $400\,^{\circ}\text{C}$ or the subsequent annealing at this temperature, the phase has apparently become unstable with regard to composition leading to either composition variation or precipitation of another phase (see Fig. 11(a)). It is not obvious that such inhomogeneities or precipitates will be discovered by XRD analyses alone. First, because small changes in the lattice parameter of the half-Heusler phase cause broadening of the diffraction peaks rather than a set of new reflections. Second, small amounts of the involved phases and large grain boundary to bulk ratios will result in a low signal-to-noise ratio in the probing of such samples by any analytical technique. Such complications may certainly have large impact on interpretation of experimental results since such inhomogeneities and/or precipitates are likely to have a large effect on the properties. Only one of our five samples turned out to be homogenous. This sample had the nominal composition $Ni_{25}Mn_{35}Sb_{40}$ and contained

![](./images/811999922042699776_13.jpg)

Fig. 11. BSE scans of sample with nominal composition (a) $Ni_{0.45}Mn_{0.20}Sb_{0.35}$ and (b) $Co_{0.33}Mn_{0.33}Sb_{0.33}$. In part a, heterogeneous dendritic crystals of NiMnSb are seen dispersed in a solidified eutectic melt. According to microprobe analysis the ternary phase has the composition $Ni_{0.410}Mn_{0.285}Sb_{0.305}$. In addition to the desired ternary phase, XRD showed reflections from two other phases, which according to microprobe analysis are a Ni-Sb phase and a Mn-rich phase, appearing as light and dark colored in the BSE scans, respectively. (b) Heterogeneous dendritic crystals of the CoMnSb phase surround small regions of solidified eutectic melt. According to microprobe analysis the ternary phase has a varying composition from $Co_{0.33}Mn_{0.33}Sb_{0.34}$ to $Co_{0.38}Mn_{0.30}Sb_{0.32}$. In addition to the ternary phase, XRD showed reflections from two other phases, which according to microprobe analysis are of a Co-Sb and a Mn-Sb phase, appearing light and dark colored in the BSE scans, respectively.

the half-Heusler phase with a relatively low Ni content, but this finding shows that, with care, the phase can satisfactory be made from simple melting of the elements.

### 4.6. CoMnSb

The composition results for CoMnSb (Fig. 9(f)) are as scattered as those for the NiMnSb case and the measured compositions again lie on both sides of the $vec_{eq}(x,y)$ line. The samples of the CoMnSb phase are also hampered by another problem also experienced for NiMnSb, namely precipitation of another phase inside the domain of the half-Heusler phase (Fig. 11(b)). This is not seen in all samples, but the findings indicate a more extended homogeneity region at high temperatures. It is difficult to estimate the solid-solution region at $400\,^{\circ}\text{C}$ without a more detailed investigation of the system. The Co–Mn–Sb system also contains both a full-Heusler and a half-Heusler phase, but unlike the findings for the Ni–Ti–Sn system, preparation of the half-Heusler phase of the Co–Mn–Sb system does not invoke problems. First, the lattice parameters of the two phases are different enough to be distinguished by simple XRD analyses (Table 1) and, second, the half-Heusler phase does not appear to have formed peritectically. The indication of a relatively large homogeneity range at elevated temperatures raises the question of a partly overlapping solid-solubility field between the full- and half-Heusler phases. The direction of the homogeneity region of CoMnSb does not follow the direction of the $vec(x,y)$ lines, but rather extends toward the composition of the full-Heusler phase (see open triangles in Fig. 9(f)). To confirm whether such a range exists the temperature dependence and stability limit of the involved phases must be investigated further.

## 5. Discussion and conclusions

We have shown that the valence-electron content (VEC) is an important parameter for composition considerations on half-Heusler phases. The optimum electronic-band-structure-stabilized $\text{VEC}_{\text{st}}$ found by combining information from DOS- and COHP-calculated profiles for the equiatomic half-Heusler phase is used to predict the composition or possible homogeneity region for a stable half-Heusler phase. Generally, for phases with $\text{VEC}_{\text{eq}}$ close to the electron content in semiconducting phases, adding or removing electrons so that VEC gets closer to 18 lead to increased stability of the phase. When $\text{VEC}_{\text{eq}}$ becomes higher than 19 the desired alteration in VEC will be toward the half-metallic ferromagnetic (HMF) situation characterized by $\text{VEC}=22$. This means that, without experimentally knowing anything else about a half-Heusler phase than its constituents, one can predict whether the composition of the stable phase is likely to be shifted away from the equiatomic 1:1:1 stoichiometry or not and also the position and direction of a possible homogeneity region. The electron content is not the only counting factor for stability, so in some cases, half-Heusler phases rather undergo a systematic structural change (as indicated for, e.g., PtMnSn [29] and CoMnSb [26,46]). We believe that the involved structural perturbation implies maximizing of bonding not only by band filling but also by hybridization and other interactions and that the consequent modification of the electronic band structure acts as a substitute for a change in VEC.

The simple probing of a few ternary systems which contain a half-Heusler phase revealed several aspects which are useful to remember. First, even simple surveying of a ternary phase may require an appreciable number of samples if the homogeneity region is to be mapped with reasonable accuracy. Second, simple melting of appropriate amounts of the constituents may not yield single-phase samples. This problem may be difficult to detect by common bulk analytical methods, especially when there are only small amounts of other phases present. Third, even when single-phase samples are obtained, the question of correct composition still remains. The present work indicates that although some of the semiconducting half-Heusler phases take the equiatomic composition and also phases with other VEC values exhibit well-defined composition regions, more experimental data are needed before these inferences can be generalized. Our experimental investigation was originally intended only as a test for theoretically founded predictions, but the findings also serve as a remainder of the various processes that can hamper preparation of a single-phase half-Heusler sample. However, most of these challenges can be handled by careful sample preparation based on knowledge of the ternary phase diagram and its temperature dependence.

From our experimental data we found that the theoretical predictions based on band filling of bonding states seem valid for half-Heusler phases. Both literature data and the presently collected experimental test data seem to be consistent with the prenotion that electron content to some extent governs the composition of a phase. The phases calculated to be stable semiconductors all take the equiatomic composition, while the other phases show deviation from this composition and they are stable over homogeneity regions more or less in accordance with the predicted change in VEC. However, the amount of conclusive experimental data is fare too small for a definite general conclusion. We leave it to interested readers to verify whether the predictions holds for, e.g., the phases presented in Fig. 7 or any other half-Heusler phase. However, such verifications require detailed mapping of phase diagrams. It would be interesting to extend this kind of predictions to other systems known to exhibit non-stoichiometry. Especially families of phases with simple crystal structures and mixed bonding situations should be interesting candidates for exploring.

## Acknowledgements

The authors are grateful to Dr. Muriel Erambert (at the Department of Geosciences, University of Oslo) for assistance with the microprobe analysis. L.O. and P.R. appreciates the financial and supercomputing support from the Research Council of Norway.

## References

[1] A. Neumann, L. Offernes, A. Kjekshus, B. Klewe, J. Alloys Compd. 274 (1998) 136-141.

[2] L. Offernes, A.N. Torgersen, A. Kjekshus, J. Alloys Compd. 307 (2000) 174-178.

[3] C. Walle, L. Offernes, A. Kjekshus, J. Alloys Compd. 349 (2003) 105-110.

[4] P. Gordon, Principles of Phase Diagrams in Materials Systems, R.E. Krieger, Malabar, Florida, 1983.

[5] I. Galanakis, P.H. Dederichs, Half-Metallic Alloys, Springer, Berlin Hei- delberg, 2005.

[6] J. Pierre, R.V. Skolozdra, J. Tobola, S. Kaprzyk, C. Hordequin, M.A. Koua-cou, I. Karla, R. Currat, E. Lelièvre-Berna, J. Alloys Compd. 262/263 (1997) 101-107.

[7] J. Tobola, J. Pierre, J. Alloys Compd. 296 (2000) 243-252.

[8] I. Galanakis, Phys. Rev. B 71 (2005) 12413.1-12413.4.

[9] T. Block, M.J. Carey, B.A. Gurney, O. Jepsen, Phys. Rev. B 70 (2004) 205114.1-205114.5.

[10] F.B. Mancoff, J.F. Bobo, O.E. Richter, K. Bessho, P.R. Johnson, R. Sinclair, W.D. Nix, R.L. White, B.M. Clemens, J. Mater. Res. 14 (1999) 1560-1569.

[11] R.A. de Groot, F.M. Mueller, P.G. van Engen, K.H.J. Buschow, J. Appl. Phys. 55 (1984) 2151-2154.

[12] Y. Xia, S. Bhattacharya, V. Ponnambalam, A.L. Pope, S.J. Poon, T.M. Tritt, J. Appl. Phys. 88 (2000) 1952-1955.

[13] J. Tobola, J. Pierre, S. Kaprzyk, R.V. Skolozdra, M.A. Kouacou, J. Phys.: Condens. Matter 10 (1998) 1013-1032.

[14] R.A. de Groot, K.H.J. Buschow, J. Magn. Magn. Mater. 54-57 (1986) 1377-1380.

[15] E.T. Kulatov, Y.A. Uspenskii, S.V. Halilov, Phys. Lett. A 195 (1994) 267-270.

[16] P.A. Dowben, R. Skomski, J. Appl. Phys. 95 (2004) 7453-7458.

[17] P.G. van Engen, K.H.J. Buschow, R. Jongebreur, M. Erman, Appl. Phys. Lett. 42 (1983) 202-204.

[18] S.A. Wolf, D.D. Awschalom, R.A. Buhrman, J.M. Daughton, S. von Mol-nar, M.L. Roukes, A.Y. Chtchelkanova, D.M. Treger, Science 294 (2001) 1488-1495.

[19] F.G. Aliev, R. Villar, S. Vieira, A.P. Levanyuk, R.V. Scolozdra, Phys. Rev. B 50 (1994) 17881-17885.

[20] P.A.M. van der Heide, W. Baelde, R.A. de Groot, A.R. de Vroomen, P.G. van Engen, K.H.J. Buschow, J. Phys. F: Met. Phys. 15 (1985) L75-L80.

[21] H. Masumoto, K. Watanabe, S. Ohnuma, J. Phys. Soc. Jpn. 32 (1972) 570.

[22] H.C. Kandpal, C. Felser, R. Seshadri, J. Phys. D: Appl. Phys. 39 (2006) 776-785.

[23] J.L. Moran-Lopez, R. Rodriguez-Alba, F. Aguilera-Granja, J. Magn. Magn. Mater. 131 (1994) 417-426.

[24] R.A. de Groot, F.M. Mueller, P.G. van Engen, K.H.J. Buschow, Phys. Rev. Lett. 50 (1983) 2024-2027.

[25] P. Mavropoulos, K. Sato, R. Zeller, P.H. Dederichs, V. Popescu, H. Ebert, Phys. Rev. B 69 (2004) 054424.

[26] M.J. Otto, R.A.M. van Woerden, C.F. van der Valk, J. Wijngaard, C.F. van Bruggen, C. Haas, K.H.J. Buschow, J. Phys.: Condens. Matter 1 (1989) 2341-2350.

[27] K.E.H.M. Hanssen, P.E. Mijnarends, L.P.L.M. Rabou, K.H.J. Buschow, Phys. Rev. B 42 (1990) 1533-1540.

[28] P. Villars, L.D. Calvert, Pearson's Handbook of Crystallographic Data for Intermetallic Phases, American Society of Metals, Metals Park, OH, 1985.

[29] K. Watanabe, J. Phys. Soc. Jpn. 28 (1970) 302-307.

[30] E.A. Stern, Phys. Rev. 157 (1967) 544-551.

[31] P. Ravindran, R. Asokamani, Bull. Mater. Sci. 20 (1997) 613-622.

[32] L. Offernes, P. Ravindran, A. Kjekshus, J. Alloys Compd., in press, cor-rected proof, available online 23 October 2006.

[33] L. Offernes, P. Ravindran, A. Kjekshus, Appl. Phys. Lett. 82 (2003) 2862-2864.

[34] P. Ravindran, A. Delin, P. James, B. Johansson, J.M. Wills, R. Ahuja, O. Eriksson, Phys. Rev. B 59 (1999) 15680-15693.

[35] J.P. Perdew, P.E. Burke, O. Jepsen, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.

[36] O.K. Andersen, O. Jepsen, Phys. Rev. Lett. 53 (1984) 2571-2574.

[37] J.M. Wills, O. Eriksson, M. Alouani, D.L. Price, Electronic Structure and Physical Properties of Solids, Springer, Berlin, 2000.

[38] G. Krier, O. Jepsen, A. Burkhardt, O.K. Andersen, TB-LMTO-ASA 4.7, Stuttgart, Germany, 2000.

[39] R. Dronskowski, P.E. Blochl, J. Phys. Chem. 97 (1993) 8617-8624.

[40] G.A. Landrum, R. Dronskowski, Angew. Chem. Int. 39 (2000) 1560-1585.

[41] R. Dronskowski, Int. J. Quantum Chem. 96 (2004) 89-94.

[42] J. Xu, A.J. Freeman, Phys. Rev. B 40 (1989) 11927-11930.

[43] P. Ravindran, R. Asokamani, Phys. Rev. B 50 (1994) 668-678.

[44] J. Xu, A.J. Freeman, Phys. Rev. B 41 (1990) 12553-12561.

[45] L.D. Dudkin, Z.M. Dashevskii, R.V. Skolozdra, Inorg. Mater. 29 (1993) 254-256.

[46] M.G. Natera, M.R.L.N. Murthy, R.J. Begum, N.S. Satya Murthy, Phys. Status Solidi A 3 (1970) 959.

[47] H. Masumoto, K. Watanabe, J. Phys. Soc. Jpn. 32 (1972) 281.

[48] P.P.J. van Engelen, D.B. de Mooij, J.H. Wijngaard, K.H.J. Buschow, J. Magn. Magn. Mater. 130 (1994) 247-254.

[49] H. Masumoto, K. Watanabe, Trans. Jpn. Inst. Met. 14 (1973) 408-414.

[50] H. Masumoto, K. Watanabe, Trans. Jpn. Inst. Met. 11 (1970) 385-390.