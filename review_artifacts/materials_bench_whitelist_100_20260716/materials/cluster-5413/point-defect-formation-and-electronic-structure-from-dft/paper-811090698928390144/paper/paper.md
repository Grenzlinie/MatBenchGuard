PHYSICAL REVIEW B 95, 035301 (2017)

# Effect of intrinsic point defects on ferroelectric polarization behavior of $SrTiO_3$

Konstantin Klyukin
Department of Chemical and Biomolecular Engineering, University of Nebraska-Lincoln, Lincoln, Nebraska 68588, USA

Vitaly Alexandrov*
Department of Chemical and Biomolecular Engineering, University of Nebraska-Lincoln, Lincoln, Nebraska 68588, USA
and Nebraska Center for Materials and Nanoscience, University of Nebraska-Lincoln, Lincoln, Nebraska 68588, USA

(Received 9 August 2016; revised manuscript received 23 November 2016; published 4 January 2017)

The effect of a variety of intrinsic defects and defect clusters in bulk and thin films of $SrTiO_3$ on ferroelectric polarization and switching mechanisms is investigated by means of density-functional-theory based calculations and the Berry phase approach. Our results show that both the titanium $Ti_{Sr}^{\bullet\bullet}$ and strontium $Sr_{Ti}''$ antisite defects induce ferroelectric polarization in $SrTiO_3$, with the $Ti_{Sr}^{\bullet\bullet}$ defect causing a more pronounced spontaneous polarization and higher activation barriers of polarization reversal than $Sr_{Ti}''$. The presence of oxygen vacancies bound to the antisite defects can either enhance or diminish polarization depending on the configuration of the defect pair, but it always leads to larger activation barriers of polarization switching as compared to the antisite defects with no oxygen vacancies. We also show that the magnitude of spontaneous polarization in $SrTiO_3$ can be tuned by controlling the degree of Sr/Ti nonstroichiometry. Other intrinsic point defects such as Frenkel defect pairs and electron small polarons also contribute to the emergence of ferroelectric polarization in $SrTiO_3$.

DOI: 10.1103/PhysRevB.95.035301

## I. INTRODUCTION

Switchable polarization in ferroelectric materials due to the orientation of dipoles by an external electric field is central to various energy and information storage technologies in- cluding sensors and actuators [1], electro-optic devices [2-4], and ferroelectric field-effect transistors for nonvolatile mem- ories [5,6]. In past years it has been revealed that ferro- electric polarization is not exclusive to polar materials and can be induced throughout the nonferroelectric layer of the heterostructure by combining a nonferroelectric oxide such as $SrTiO_3$ with a ferroelectric oxide, e.g., $BaTiO_3$ [7], or even with another nonferroelectric oxide, e.g., $LaCrO_3$ [8]. Moreover, the emergence of net ferroelectric polarization was recently demonstrated for nanometer-thick films of $SrTiO_3$ [9] where this effect was attributed to electrically induced alignment of polar nanoregions that can naturally form because of the presence of intrinsic defects in $SrTiO_3$ crystals. It was previously demonstrated that intrinsic defects such as the antisite Ti defects can form in the bulk phase of Ti-rich $SrTiO_3$, generate local polarization around the antisite Ti center due to an off-center displacement of the defect, and might contribute to the appearance of polar nanoregions [9,10] in a manner similar to extrinsic defects [11].

Native point defects in perovskite-structured $SrTiO_3$ were studied extensively in the past both experimentally and theoretically with the largest emphasis being placed on the oxygen vacancy as the most prominent point defect in $SrTiO_3$ that affects a wide range of material properties including electronic and optical behavior [12-18]. $SrTiO_3$ point defect chemistry, thermodynamics, and kinetics of defect formation and diffusion were also investigated in great detail [19-23]. For example, oxygen vacancies serve as a source of $n$-type conductivity that can vary with oxygen partial pressure and are responsible for insulator-to-metal transition [18]. Oxygen vacancies are also known to play a key role in the resistive switching process under applied electric field due to their low activation energies of diffusion [12,24-26]. Also, it is well established that point defects including oxygen vacancies play a critical role in mediating polarization switching in ferro- electrics by controlling the local polarization stability, acting as pinning sites for domain-wall motion and ultimately defining the mechanism and kinetics of polarization switching [27,28].

The impact of intrinsic point defects including oxygen va- cancies on the polarization switching phenomenon in $SrTiO_3$ is much less understood. In this study we carry out a systematic investigation of the effect of native defects in bulk and thin-film $SrTiO_3$ on ferroelectric polarization and polarization reversal at a single defect level by means of first-principles electronic structure calculations.

## II. COMPUTATIONAL METHOD

First-principles calculations are performed within the den- sity functional theory (DFT) formalism using the projector augmented wave (PAW) potentials [29] as implemented in the Vienna $Ab$ initio Simulation Package (VASP) [30]. The PAW potentials for Sr, Ti, O, and Ru contain 10, 12, 6, and 14 valence electrons, respectively, that is, Sr: $4s^24p^65s^2$, Ti: $3s^23p^64s^23d^2$, O: $2s^22p^4$, and Ru: $4p^65s^14d^7$. The generalized gradient approximation Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional [31] is employed in the modified form for solids PBEsol [32] along with a plane wave cutoff energy of 400 eV. The rotationally invariant PBEsol $+U$ approach is adopted with $U_{\text{eff}}=4.36$ eV on the Ti $3d$ orbitals that was shown to provide a good description of the electronic structure properties of $SrTiO_3$ with and without defects [10,23,33]. The ions are relaxed by applying a conjugate-gradient algorithm until the Hellmann-Feynman forces are less than $20$ meV/Å with an optimized lattice

*Corresponding author: valexandrov2@unl.edu

2469-9950/2017/95(3)/035301(8)
035301-1
©2017 American Physical Society

![](./images/811090698928390144_1.jpg)

FIG. 1. The atomic structure of $SrTiO_3/SrRuO_3$ thin films with the antisite $Ti_{Sr}^{\bullet\bullet}$ defect in the middle of the supercell which induces polarization along the [100] direction.

constant of 3.903 Å. The $3\times3\times3$ Monkhorst-Pack $k$ mesh is used for the Brillouin zone integration for a $3\times3\times3$ supercell, while the mesh was adjusted for other supercells to provide a similar $k$-point density in each direction.

To investigate the influence of intrinsic defects and defect clusters on the polarization properties of $SrTiO_3$, we construct a $3\times3\times3$ supercell consisting of 135 atoms for the bulk calculations and a $3\times3\times7$ multilayered structure comprised of four $SrTiO_3$ and three $SrRuO_3$ layers for the thin-film calculations (see Fig. 1). To optimize the geometry, we first constrained the in-plane structure of each bulk material component of the $SrRuO_3/SrTiO_3$ heterostructure to the optimized lattice constant of $SrTiO_3$ and performed full relaxation of internal coordinates and $c/a$ ratio. For $SrRuO_3$ we find $c/a=1.017$, while $SrTiO_3$ remains cubic with $c/a=1$. The structure of the $SrRuO_3/SrTiO_3$ supercell was constructed by stacking $SrRuO_3/SrTiO_3$ cells along the [100] direction and performing full atom relaxation. In all bulk calculations the lattice constant was fixed and only atom relaxation was allowed.

The Berry-phase approach [34] within the modern theory of polarization is employed to calculate polarization properties. According to this approach the spontaneous polarization is defined as the difference in polarization between the polar and nonpolar (centrosymmetric) reference states [35]. To estimate polarization switching barriers we calculate the migration energy profile $E_m$ along the minimum energy path between two polarization states ($P_-$ and $P_+$) using the climbing image nudged elastic band method [36]. To denote the $SrTiO_3$ point defects we adopt the Kröger-Vink nomenclature [20,37].

## III. RESULTS AND DISCUSSION

### A. $Ti_{Sr}^{\bullet\bullet}$ antisite defect

We start by considering the titanium-strontium $Ti_{Sr}^{\bullet\bullet}$ antisite defect where the $Ti^{4+}$ ion occupies a site on the $Sr^{2+}$ sublattice. This defect was predicted to be the dominant defect in $SrTiO_3$ along with the oxygen vacancy $V_O$ under Ti-rich conditions [10,23]. To find the most stable atomic configuration for $Ti_{Sr}^{\bullet\bullet}$ we examine the atomic structures with the Ti atom shifted along the [100], [110], and [111] crystallographic directions. A large $Ti_{Sr}^{\bullet\bullet}$ off-centering of 0.78 Å along the [100] direction is found to be the most energetically favorable with an energy gain of 0.48 eV with respect to the nonshifted configuration, in agreement with previous estimates [9,10]. The displaced Ti atom forms four Ti-O bonds of length 2.20 Å that are much closer to the Ti-O bond distances in pristine $SrTiO_3$ (1.95 Å). We attribute this displacement primarily to the covalency effect due to an effective hybridization between $3d$ states of the antisite and $2p$ states of the neighboring O ions as seen from the analysis of the partial density of states. The atomic configuration with the shifted $Ti_{Sr}^{\bullet\bullet}$ can thus be considered as an electric dipole comprised of a negatively charged Sr vacancy and a positively charged Ti interstitial which induces the electric polarization.

TABLE I. Quantities calculated for a $3\times3\times3$ $SrTiO_3$ supercell with different defects: defect off-centering $d$ along the corresponding directions, Born charge associated with the off-centered cation, average spontaneous polarization $P$, and activation barrier for polarization switching $E_m$. Calculated Born charges for pristine $SrTiO_3$ are 2.56, 6.57, $-5.23$, and $-1.93$ for $Sr$, Ti, $O_{\parallel}$, and $O_{\perp}$, correspondingly.

| Defect | $d$ (Å) | Born charge | $P$ ($\mu$C/cm²) | $E_m$ (eV) |
|--------|---------|-------------|-------------------|------------|
| $Ti_{Sr}^{\bullet\bullet}$ | 0.78 [100] | 1.72 | 16.8 | 0.13 |
| $Ti_{Sr}^{\bullet\bullet}$-$V_O^{\times}$ | 0.82 [011] | | | |
| $Ti_{Sr}^{\bullet\bullet}$-$V_O^{\bullet\bullet}$ | 0.79 [011] | 2.48 | 22.6 | 0.23 |
| $Sr_{Ti}^{\prime\prime}$ | 0.26 [011] | 3.11 | 7.6 | 0.05 |
| $Sr_{Ti}^{\prime\prime}$-$V_O^{\times}$ | 0.81 [100] | 3.59 | 15.7 | 0.76 |
| $Sr_{Ti}^{\prime\prime}$-$V_O^{\bullet\bullet}$ | 0.81 [100] | | | |
| $V_{Ti}^{\prime\prime\prime\prime}$-$O_i^{\times}$ | 0.61 [110] | 2.2 | 20.3 | 0.54 |
| $V_{Sr}^{\prime\prime}$-$O_i^{\times}$ | 1.24 [100] | 0.15 | 7.2 | 0.61 |
| $Ti_{Ti}^{\bullet}$-$V_O^{\times}$ | 0.08 [100] | 5.1 | 5.0 | |

Using the Berry phase method we estimate the average polarization of the supercell $P^{100}(Ti_{Sr}^{\bullet\bullet})$ to be $16.8\ \mu$C/cm². In full agreement with previous calculations [9], we find that despite the large off-centering of $Ti_{Sr}^{\bullet\bullet}$, its local dipole moment is relatively small due to a small Born effective charge of 1.72 (see Table I). Consequently, the overall dipole moment is dominated by the induced dipole moments in the surrounding cells rather than by the dipole moment of the antisite Ti atom which accounts for about 8.1% of the total dipole moment of the supercell. Thus, the electric dipole moment induced by a large off-centering of the defect atom is accompanied by geometrical distortions polarizing the region surrounding the defect.

We also estimate the migration energy barriers for [100] $\rightarrow$ [$\overline{1}$00] polarization switching and find that the barrier for the direct switching between these two polarization states is rather large (0.48 eV), while the two-step migration via the intermediate state [110] is characterized by the barrier of only 0.13 eV (see Fig. 2). For this metastable state the average supercell polarization $P^{110}(Ti_{Sr}^{\bullet\bullet})=15.1\ \mu$C/cm².

The influence of oxygen vacancies on $SrTiO_3$ polarization properties is not well understood at the $ab$ initio level despite the predominant role of this defect in $SrTiO_3$ defect

![](./images/811090698928390144_2.jpg)

![](./images/811090698928390144_3.jpg)

FIG. 2. (a) Atomic structures of $SrTiO_3$ with the antisite $Ti_{Sr}^{\bullet\bullet}$ defect for two polarization states with $Ti_{Sr}^{\bullet\bullet}$ shifted along the [100] and [110] directions. (b) Migration energy profile between polarization states caused by the $Ti_{Sr}^{\bullet\bullet}$ defect. Polarization reversal from [100] to $[\overline{1}00]$ is achieved via the metastable polarization states with the [110] and $[\overline{1}01]$ directions.

chemistry. Previous theoretical studies suggested that $Ti_{Sr}^{\bullet\bullet}$ and $V_O$ together with $V_{Sr}^{\prime\prime}$ should be the most thermodynamically stable defects in $SrTiO_3$ under Ti-rich conditions [10,17,23], while the Ti-rich environment is predicted to be energetically more favorable than excess $SrO$ in $SrTiO_3$ [23]. Calculated formation energies as a function of Fermi level indicate that the doubly charged $V_O^{\bullet\bullet}$ should be more stable than the singly charged $V_O^{\bullet}$ and neutral $V_O^{\times}$ even in $n$-type $SrTiO_3$ in which the Fermi level is close to the bottom of the conduction band [10,17]. It is expected that the presence of the positively charged oxygen vacancies in the vicinity of the $Ti_{Sr}^{\bullet\bullet}$ defect may change the dipole moment induced by $Ti_{Sr}^{\bullet\bullet}$.

First, our calculations reveal a negative binding energy of about $-0.4$ eV between $V_O^{\bullet\bullet}$ and $Ti_{Sr}^{\bullet\bullet}$ indicating that the formation of the defect complex is energetically favored over the isolated defects. To examine different atomic arrangements between these defects, we displace $Ti_{Sr}^{\bullet\bullet}$ with respect to $V_O^{\bullet\bullet}$ as shown in Fig. 3. We find that the most stable configuration is nonmagnetic and characterized by a $Ti_{Sr}^{\bullet\bullet}$ off-centering of $0.79$ Å along the [110] direction towards the vacancy exhibiting polarization $P^{110}(Ti_{Sr}^{\bullet\bullet}\text{-}V_O^{\bullet\bullet})=22.6\ \mu\text{C/cm}^2$ which is enhanced with respect to the $Ti_{Sr}^{\bullet\bullet}$ case with no oxygen vacancy. We also find that a slightly less favorable (by 0.02 eV) spin-polarized configuration with a magnetic moment of $2\mu_B$ has a much lower polarization $P^{110}(Ti_{Sr}^{\bullet\bullet}\text{-}V_O^{\bullet\bullet})=5.61\ \mu\text{C/cm}^2$ caused by a much less pronounced off-centering of $0.43$ Å.

![](./images/811090698928390144_4.jpg)

FIG. 3. (a) Atomic structures of $SrTiO_3$ with $Ti_{Sr}^{\bullet\bullet}$ and $V_O^{\bullet\bullet}$ for polarization states with $Ti_{Sr}^{\bullet\bullet}$ shifted along the [110], $[1\overline{1}0]$, and $[\overline{1}\overline{1}0]$ directions. (b) Migration energy profiles between polarization states caused by the $Ti_{Sr}^{\bullet\bullet}$ and $V_O^{\bullet\bullet}$ defects. Polarization switching from [110] to $[1\overline{1}0]$ can be achieved via the metastable polarization state with the [100] direction.

The nonsymmetrical state $P\_$ is characterized by a reduced polarization $P^{1\overline{1}0}(Ti_{Sr}^{\bullet\bullet}\text{-}V_O^{\bullet\bullet})=14.4\ \mu\text{C/cm}^2$ caused by a $0.81$ Å off-centering. Such a decrease relative to the most stable $P^{110}$ state could be explained by the opposite directions of dipoles formed by $V_{Sr}^{\prime\prime}\text{-}Ti_{Sr}^{\bullet\bullet}$ and $V_{Sr}^{\prime\prime}\text{-}V_O^{\bullet\bullet}$. The switching barrier between these two polarization states is computed to be 0.24 eV, which is twice higher than for $Ti_{Sr}^{\bullet\bullet}$ with no oxygen vacancy. A displacement along the $[\overline{1}\overline{1}0]$ direction leads to a substantially diminished polarization $P^{\overline{1}\overline{1}0}(Ti_{Sr}^{\bullet\bullet}\text{-}V_O^{\bullet\bullet})=2.2\ \mu\text{C/cm}^2$ and a greater switching barrier.

We next analyze the $Ti_{Sr}^{\bullet\bullet}\text{-}V_O^{\times}$ defect complex since neutral $V_O^{\times}$ may have the formation energy only slightly higher than those of the positive charge states in the $n$-type region [17]. We find that the complex is stable with an estimated binding energy of about $-0.35$ eV, but is characterized by the metallic behavior and no polarization can be given. In this case one electron of the antisite defect moves to the conduction band forming a metallic state near the Fermi level while the second electron forms a localized in-gap state (Fig. 4). In relation to polarization properties this suggests that the formation of the $Ti_{Sr}^{\bullet\bullet}\text{-}V_O^{\times}$ defect complexes may also contribute to the resistive switching in Ti-rich $SrTiO_3$; however, the interplay between polarization and metallic conductivity being in the focus of many recent studies of perovskite oxides [38,39] deserves a separate detailed investigation.

We should note here that antiferroelectricity in perovskite oxides is a well recognized phenomena that leads to the competition between ferroelectric and antiferroelectric phases depending on the interplay between different factors such as

![](./images/811090698928390144_5.jpg)

FIG. 4. Density of electronic states calculated for the $Ti_{Sr}^{\bullet\bullet}$-$V_{O}^{\times}$
defect complex. The Fermi level corresponds to zero.

chemical composition, strain, size effects, and reconstruction
at surfaces [40–42]. Although we have not investigated in
detail how various intrinsic defects producing ferroelectric
polarization in $SrTiO_{3}$ interact with each other, to obtain some
insight into the possibility of antiferroelectric ordering, we
compared the energetics of both ferroelectric and antiferro-
electric configurations of two $Ti_{Sr}^{\bullet\bullet}$ antisite defects placed in a
model $3\times3\times3$ supercell. We found that the antiferroelectric
configuration is less favorable than the ferroelectric configu-
ration by 0.13 eV.

### B. $Sr_{Ti}''$ antisite defect
Similarly to $Ti_{Sr}^{\bullet\bullet}$, the formation of the antisite $Sr_{Ti}''$ defect
in which a Sr ion substitutes one Ti ion is expected in Sr-rich
$SrTiO_{3}$ (Fig. 5) [23]. This configuration can be regarded as
an electric dipole composed of a strontium interstitial and a
titanium vacancy. In this structure the Sr ion is coordinated by
six O atoms with the Sr-O distances being considerably shorter
(2.22–2.26 Å) than those in pristine $SrTiO_{3}$ (2.76 Å) where Sr
is coordinated by 12 oxygens. Our calculations reveal that
the most energetically favorable configuration of $Sr_{Ti}''$ has an
off-centering of 0.26 Å along the [110] direction (Fig. 5). We
do not observe any significant overlap between the Sr and O
states in partial density of states and attribute this displacement
mainly to the electrostatic effect. Also, since the ionic size of
$Sr^{2+}$ is much larger than that of $Ti^{4+}$, there is little space for the
$Sr_{Ti}''$ antisite to displace and the off-centering is much smaller
than we observe for the $Ti_{Sr}^{\bullet\bullet}$ antisite defect.

The calculated electric polarization $P^{110}(Sr_{Ti}'')$ equals to
$7.6\ \mu C/cm^{2}$ which is about twice smaller than in the $Ti_{Sr}^{\bullet\bullet}$
case. The energy barrier calculated for polarization switching
is only 0.05 eV rendering a low coercive voltage (Fig. 5). The
contribution of the antisite Sr atom to the total dipole moment
of the supercell is found to be about 10.6%, being comparable
with the $Ti_{Sr}^{\bullet\bullet}$ case. This spin-polarized structure of $Sr_{Ti}''$ induces
magnetic moments on the nearest to $Sr_{Ti}''$ oxygen atoms and is
more energetically favorable than the nonmagnetic structure
by about 0.17 eV exhibiting a much higher polarization
switching barrier of $\sim0.3$ eV. We also estimate polarization
$P^{100}(Sr_{Ti}'')$ induced by the $Sr_{Ti}''$ displacement along the [100]
direction, which is the direction of film growth to be as low as
$2.5\ \mu C/cm^{2}$.

![](./images/811090698928390144_6.jpg)

FIG. 5. (a) Atomic structures of $SrTiO_{3}$ with the antisite $Sr_{Ti}''$
defect corresponding to two different polarization states with the
defect shifted along the [110] and [100] directions. (b) Migration
energy profile between polarization states caused by the $Sr_{Ti}''$ defect.
Polarization switching from the [110] to the $[\overline{1}\overline{1}0]$ direction can
be achieved via the polarization states with the [100] and [0$\overline{1}$0]
directions.

The addition of oxygen vacancies is also found to have
a significant impact on ferroelectric polarization induced
by the $Sr_{Ti}''$ defect. Recently, the formation of $Sr_{Ti}''$-$V_{O}^{\bullet\bullet}$
defect complexes was observed experimentally during the
electroforming and resistive switching of $SrTiO_{3}$ [43]. These
complexes were previously calculated to have low formation
enthalpies under Sr-rich conditions [23] and we estimate that
the $Sr_{Ti}''$ defect has very large binding energies of $-1.76$ and
$-1.85$ eV with doubly charged $V_{O}^{\bullet\bullet}$ and neutral $V_{O}^{\times}$ vacancies,
correspondingly.

Our calculations show that the positively charged oxygen
vacancy causes a metallic state near the Fermi level and there-
fore no polarization can be provided for the $Sr_{Ti}''$-$V_{O}^{\bullet\bullet}$ defect
pair. On the other hand, neutral $V_{O}^{\times}$ leads to semiconducting
behavior and the most stable structure is characterized by a
large off-centering (0.81 Å) of the antisite defect along the
[100] direction as shown in Fig. 6. In this case the antisite $Sr_{Ti}''$
forms four short bonds of 2.23 Å and one much longer bond
of 2.72 Å with the neighboring oxygen atoms. The average
polarization of the supercell is estimated as $15.7\ \mu C/cm^{2}$. The
energy profile of $Sr_{Ti}''$ diffusion associated with polarization
switching in the presence of $V_{O}^{\times}$ becomes nonsymmetrical with
a very high switching barrier of 0.76 eV and a flat minimum for
the $P_{-}$ state (Fig. 6). This state induces a small polarization of

![](./images/811090698928390144_7.jpg)

FIG. 6. (a) Atomic structures of $SrTiO_3$ with the $Sr_{Ti}''$ defect and neutral $V_O^\times$ corresponding to two different polarization states with the antisite defect shifted along the [100] and [$\bar{1}$10] directions. (b) Energy profile between two polarization states caused by $Sr_{Ti}''$ and $V_O^\times$. The polarization state for the [$\bar{1}$10] direction has a very flat minimum suggesting that the state with $Sr_{Ti}''$ shifted along the [100] direction acts as a trap.

$2.1\ \mu\text{C/cm}^2$ and should be unstable with respect to polarization switching. The switching via diffusion of oxygen vacancies, however, is expected to have large barriers ($\sim$0.6–1.0 eV) [44].

In general, the results obtained for spontaneous polarization induced by the antisite $Ti_{Sr}^{\bullet\bullet}$ and $Sr_{Ti}''$ defects are in qualitative agreement with experimental findings showing that although the excess of Sr can lead to ferroelectricity in polycrystalline $SrTiO_3$ at low temperatures, the observed polarization is considerably lower than for Ti-rich samples [45].

### C. Frenkel defects and small polarons
The deficiency of cation atoms and excess of oxygen atoms leads to the formation of Frenkel defect pairs. In the case of the titanium vacancy $V_{Ti}'''$ and oxygen interstitial $O_i^\times$ pair we find that the most stable position for $O_i^\times$ is to be shifted from the $V_{Ti}'''$ site along the [110] direction by $0.61\ \mathring{A}$ as depicted in Fig. 7. The distance between $O_i^\times$ and two adjacent lattice oxygen atoms is $1.35\ \mathring{A}$, while the corresponding angle between three oxygen atoms is about $110^\circ$. The electric dipole formed by this Frenkel pair causes a large average polarization $P^{110}(V_{Ti}'''-O_i^\times)$ of about $20.3\ \mu\text{C/cm}^2$, but with a high switching barrier of 0.54 eV.

Calculations of the other Frenkel defect pair composed of a Sr vacancy and an oxygen interstitial reveal that it is energetically preferable for $O_i^\times$ to be shifted along the [100] direction with the $1.24\ \mathring{A}$ off-centering from the initial Sr position (Fig. 8). However, such a significant off-centering does not induce a large local dipole moment because of the very small Born charge of 0.15 on the O interstitial (see Table I). The overall polarization of the supercell in this case is computed

![](./images/811090698928390144_8.jpg)

![](./images/811090698928390144_9.jpg)

035301-5

to be around $7.2\ \mu\text{C/cm}^2$ with the high diffusion barrier for polarization switching of 0.61 eV.

It was previously shown that excess electrons in the bulk ${\text{SrTiO}}_3$ do not become localized in the form of small polarons on Ti atoms, but can be stabilized in the presence of oxygen vacancies [46]. It turned out that in $n$-type ${\text{SrTiO}}_3$ the most stable configuration corresponds to the case when each oxygen vacancy traps one small polaron remaining in a +1 charge state and providing one electron to the conduction band. We find that the dipole moment produced by such a defect pair causes a moderately large polarization of $5.0\ \mu\text{C/cm}^2$.

### D. The impact of defect concentration and the ${\text{SrTiO}}_3/{\text{SrRuO}}_3$ interface

In this section we aim to examine how the defect concentration and the presence of the interface with ${\text{SrRuO}}_3$ can impact polarization properties of ${\text{SrTiO}}_3$. To simulate different concentrations of the antisite ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ and ${\text{Sr}}_{\text{Ti}}^{\prime\prime}$ defects we consider one defect in $2\times2\times2$, $3\times3\times3$, and $4\times4\times4$ supercells corresponding to a Sr/Ti ratio of 0.78, 0.93, 0.97, 1.03, 1.07, and 1.28, respectively. In addition, we examine two ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ (or ${\text{Sr}}_{\text{Ti}}^{\prime\prime}$) defects in a $3\times3\times3$ supercell with the largest defect separation attainable in this cell which corresponds to the Sr/Ti ratio of 0.86 and 1.16. As seen from Fig. 9, an increase of the ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ defect concentration causes noticeably enhanced polarization, but as the defect concentration increases polarization gets diminished partly due to a much smaller displacement of ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ being $0.45\ \text{\AA}$ for Sr/Ti = 0.78 as compared to $0.78\ \text{\AA}$ for Sr/Ti = 0.93. A similar trend is observed for the ${\text{Sr}}_{\text{Ti}}^{\prime\prime}$ defect and we also find that the high concentration of antisite ${\text{Sr}}_{\text{Ti}}$ (Sr/Ti = 1.29) leads to a metallic electronic structure. This is consistent with experimental observations showing the absence of ferroelectricity in Sr-rich ${\text{SrTiO}}_3$ (001) thin films [47] as well as the presence of ferroelectricity in polycrystalline ${\text{SrTiO}}_3$ at low stoichiometry of Sr/Ti = 1.04–1.10 [45].

![](./images/811090698928390144_10.jpg)

FIG. 9. Average spontaneous polarization as a function of defect concentration. Sr-rich condition Sr/Ti > 1 corresponds to the larger concentration of ${\text{Sr}}_{\text{Ti}}^{\prime\prime}$ and Sr/Ti < 1 corresponds to the larger concentration of ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$. The inset is a comparison between the results obtained using PBEsol+$U$ and the hybrid HSE06 functional for three different concentrations of the ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ defect computed only at the $\Gamma$ point.

Importantly, for a Sr/Ti ratio of 1.16 the system with two neighboring ${\text{Sr}}_{\text{Ti}}^{\prime\prime}$ defects becomes more stable if the defects are displaced along the different directions ([110] and $[\overline{1}\overline{1}0]$) giving rise to a decrease of the total polarization, an effect that is not observed for ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$. Overall, we predict the same trend for spontaneous polarization as a function of Sr/Ti nonstoichiometry as previously measured for Ti- and Sr-rich ${\text{SrTiO}}_3$ samples [45], with the antisite ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ defect causing a more pronounced polarization than ${\text{Sr}}_{\text{Ti}}^{\prime\prime}$ for the same defect concentration.

To obtain some insights into the impact of a thin-film interface on polarization properties, we focus on the antisite ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ defect that exhibits the most pronounced and easily switchable polarization in the bulk phase. It was previously demonstrated that the creation of this defect in the ${\text{SrTiO}}_3/{\text{SrRuO}}_3$ thin films is more probable than in the bulk ${\text{SrTiO}}_3$ due to its lower formation energy [9]. Since no polarization was experimentally detected in the ${\text{SrRuO}}_3$ region of the heterostructure [9], we assume that all the dipole moments are induced by the four ${\text{SrTiO}}_3$ layers.

In order to directly compare spontaneous polarization of the ${\text{SrTiO}}_3/{\text{SrRuO}}_3$ interfacial structure with the case of bulk ${\text{SrTiO}}_3$, we also estimate polarization for a $3\times3\times4$ supercell of the bulk ${\text{SrTiO}}_3$ that corresponds to the same number of ${\text{SrTiO}}_3$ layers as in the heterostructure. Our calculations predict that the presence of the interface with metallic ${\text{SrRuO}}_3$ has very little influence on the average atomic displacements that are a little decreased at the interface, and therefore should not have a considerable impact on the total polarization. Based on the obtained results and the fact that the formation energy of ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ becomes significantly reduced in thin films [9], we conclude that the enhancement of polarization in thin films is not due to the influence of the ${\text{SrTiO}}_3/{\text{SrRuO}}_3$ interface.

### E. The effect of the functional and $k$-point sampling

We should note here that it is known that ${\text{SrTiO}}_3$ exhibits both antiferrodistortive and ferroelectric instabilities in the cubic phase [48]. However, it was found that polar instability in ${\text{SrTiO}}_3$ is very weak leading to an energy gain of only 0.8 meV per formula unit (at 0 antiferrodistortive angle) reaching around 0.1 meV at the theoretical equilibrium antiferrodistortive angle of 5.7 when using the PBEsol functional, which is consistent with our estimates. We observe that the Ti-O displacement in ${\text{SrTiO}}_3$ becomes even smaller when using PBEsol+$U$ as compared to the plain PBEsol functional. In any case, these instabilities should be captured in our models as we consider intrinsic defects in large supercells imposing no symmetry constraints.

To assess the effect of $U$ on polarization properties of ${\text{SrTiO}}_3$, we perform additional calculations for the $U$ values in the 4–4.5 eV range previously used in the literature for ${\text{SrTiO}}_3$. As expected, we find that increasing the $U$ value leads to a stronger electron localization on Ti atoms, while the total polarization is decreased. Similarly, decreasing the $U$ value results in a more pronounced electron delocalization that increases the total polarization. However, the results obtained for the antisite ${\text{Ti}}_{\text{Sr}}^{\bullet\bullet}$ defect show that variation of the $U$ value

035301-6

in the 4–4.5 eV range affects ferroelectric polarization only within 10%.

In order to evaluate the effect of the functional on the polarization properties of SrTiO₃, we also employ the HSE06 functional [49] to compute polarization on the example of the antisite $Ti_{Sr}^{\bullet\bullet}$ defect as a function of the defect concentration to be compared with the PBEsol+$U$ approach ($U_{\text{eff}} = 4.36$ eV). Since hybrid calculations for supercell sizes used in our study in combination with dense $k$-point meshes are very time consuming, we only carry out $\Gamma$-point calculations. We find that both the $k$-point sampling and the functional have an influence on the calculated polarization (see Fig. 9). For example, polarization for the Sr/Ti = 0.93 nonstoichiometry level estimated using PBE+$U$ at the $\Gamma$ point is found to be $23\ \mu\text{C}/\text{cm}^2$, whereas it is $16.8\ \mu\text{C}/\text{cm}^2$ for a $3\times3\times3$ $k$-point mesh. The same effect of $k$-point sampling is expected for the HSE06 functional and thus polarization values in the hybrid approach should be lower than we find in calculations using only the $\Gamma$ point. Overall, however, both hybrid and PBE+$U$ approaches show the same trend in polarization as a function of the antisite concentration with the hybrid method showing more pronounced polarization.

## IV. CONCLUSIONS
In summary, we have explored the impact of a range of native point defects on ferroelectric polarization and the mechanisms of polarization reversal in bulk and thin films of SrTiO₃ by employing DFT calculations in combination with the Berry phase approach. We have shown that the antisite $Ti_{Sr}^{\bullet\bullet}$ defect should result in the pronounced spontaneous polarization; however, the presence of oxygen vacancies may substantially reduce the polarization, make polarization switching barriers much higher, and even cause noninsulating behavior. The presence of antisite $Sr_{Ti}''$ induces smaller polarization with lower barriers of polarization switching than those for $Ti_{Sr}^{\bullet\bullet}$, in quantitative agreement with previously measured polarization for Sr- and Ti-rich SrTiO₃ samples. We have also found that the increase in spontaneous polarization in SrTiO₃/SrRuO₃ thin films can be achieved by tailoring the degree of Sr/Ti nonstoichiometry and is not due to the presence of SrTiO₃/SrRuO₃ interfaces. Some other intrinsic point defects such as Frenkel defect pairs and electron small polarons have been also found to give sizable contributions to spontaneous polarization of SrTiO₃.

## ACKNOWLEDGMENTS
We would like to thank Alexei Gruverman for fruitful discussions and comments on this study. The Holland Computing Center at the University of Nebraska-Lincoln is acknowledged for computational support. This work was supported by the National Science Foundation (NSF) through the Nebraska Materials Research Science and Engineering Center (MRSEC) (Grant No. DMR-1420645). V.A. gratefully acknowledges support from the startup package.

[1] C.-B. Eom and S. Trolier-McKinstry, *MRS Bull.* **37**, 1007 (2012).

[2] B. W. Wessels, *Annu. Rev. Mater. Res.* **37**, 659 (2007).

[3] C. Xiong, W. H. Pernice, J. H. Ngai, J. W. Reiner, D. Kumah, F. J. Walker, C. H. Ahn, and H. X. Tang, *Nano Lett.* **14**, 1419 (2014).

[4] J. P. George, P. F. Smet, J. Botterman, V. Bliznuk, W. Woestenborghs, D. V. Thourhout, K. Neyts, and J. Beeckman, *ACS Appl. Mater. Interfaces* **7**, 13350 (2015).

[5] J. Scott, *Science* **315**, 954 (2007).

[6] V. Garcia and M. Bibes, *Nat. Commun.* **5**, 4289 (2014).

[7] J. Neaton and K. Rabe, *Appl. Phys. Lett.* **82**, 1586 (2003).

[8] R. B. Comes, S. R. Spurgeon, S. M. Heald, D. M. Kepaptsoglou, L. Jones, P. V. Ong, M. E. Bowden, Q. M. Ramasse, P. V. Sushko, and S. A. Chambers, *Adv. Mater. Interfaces* **3**, 1500779 (2016).

[9] D. Lee, H. Lu, Y. Gu, S.-Y. Choi, S.-D. Li, S. Ryu, T. Paudel, K. Song, E. Mikheev, S. Lee *et al.*, *Science* **349**, 1314 (2015).

[10] M. Choi, F. Oba, and I. Tanaka, *Phys. Rev. Lett.* **103**, 185502 (2009).

[11] U. Bianchi, J. Dec, W. Kleemann, and J. G. Bednorz, *Phys. Rev. B* **51**, 8737 (1995).

[12] A. Kalabukhov, R. Gunnarsson, J. Börjesson, E. Olsson, T. Claeson, and D. Winkler, *Phys. Rev. B* **75**, 121404 (2007).

[13] V. E. Alexandrov, E. A. Kotomin, J. Maier, and R. A. Evarestov, *Eur. Phys. J. B* **72**, 53 (2009).

[14] Y. Yamada, H. Yasuda, T. Tayagaki, and Y. Kanemitsu, *Phys. Rev. Lett.* **102**, 247401 (2009).

[15] C. Mitra, C. Lin, J. Robertson, and A. A. Demkov, *Phys. Rev. B* **86**, 155105 (2012).

[16] M. Choi, F. Oba, Y. Kumagai, and I. Tanaka, *Adv. Mater.* **25**, 86 (2013).

[17] A. Janotti, J. B. Varley, M. Choi, and C. G. Van de Walle, *Phys. Rev. B* **90**, 085202 (2014).

[18] P. Calvani, M. Capizzi, F. Donato, S. Lupi, P. Maselli, and D. Peschiaroli, *Phys. Rev. B* **47**, 8917 (1993).

[19] D. A. Muller, N. Nakagawa, A. Ohtomo, J. L. Grazul, and H. Y. Hwang, *Nature (London)* **430**, 657 (2004).

[20] R. Merkle and J. Maier, *Angew. Chem., Int. Ed.* **47**, 3874 (2008).

[21] E. A. Kotomin, V. Alexandrov, D. Gryaznov, R. Evarestov, and J. Maier, *Phys. Chem. Chem. Phys.* **13**, 923 (2011).

[22] D. J. Keeble, S. Wicklein, R. Dittmann, L. Ravelli, R. A. Mackie, and W. Egger, *Phys. Rev. Lett.* **105**, 226102 (2010).

[23] B. Liu, V. R. Cooper, H. Xu, H. Xiao, Y. Zhang, and W. J. Weber, *Phys. Chem. Chem. Phys.* **16**, 15590 (2014).

[24] M. Janousch, G. Meijer, U. Staub, B. Delley, S. Karg, and B. Andreasson, *Adv. Mater.* **19**, 2232 (2007).

[25] J. Park, D.-H. Kwon, H. Park, C. Jung, and M. Kim, *Appl. Phys. Lett.* **105**, 183103 (2014).

[26] M. Zhao, Y. Zhu, Q. Wang, M. Wei, X. Liu, F. Zhang, C. Hu, T. Zhang, D. Qiu, M. Li, and R. Xiong, *Appl. Phys. Lett.* **109**, 013504 (2016).

[27] M.-W. Chu, I. Szafraniak, D. Hesse, M. Alexe, and U. Gösele, *Phys. Rev. B* **72**, 174112 (2005).

[28] S. V. Kalinin, B. J. Rodriguez, A. Y. Borisevich, A. P. Baddorf,

N. Balke, H. J. Chang, L.-Q. Chen, S. Choudhury, S. Jesse, P. Maksymovych *et al.*, Adv. Mater. **22**, 314 (2010).

[29] G. Kresse and D. Joubert, Phys. Rev. B **59**, 1758 (1999).

[30] G. Kresse and J. Furthmüller, Phys. Rev. B **54**, 11169 (1996).

[31] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

[32] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. **100**, 136406 (2008).

[33] S. Okamoto, A. J. Millis, and N. A. Spaldin, Phys. Rev. Lett. **97**, 056802 (2006).

[34] R. D. King-Smith and D. Vanderbilt, Phys. Rev. B **47**, 1651 (1993).

[35] N. A. Spaldin, J. Solid State Chem. **195**, 2 (2012).

[36] G. Henkelman, B. P. Uberuaga, and H. Jónsson, J. Chem. Phys. **113**, 9901 (2000).

[37] F. A. Kröger and N. H. Nachtrieb, Phys. Today **17**(10), 66 (1964).

[38] T. H. Kim, D. Puggioni, Y. Yuan, L. Xie, H. Zhou, N. Campbell, P. J. Ryan, Y. Choi, J.-W. Kim, J. R. Patzner *et al.*, Nature (London) **533**, 68 (2016).

[39] N. A. Benedek and T. Birol, J. Mater. Chem. C **4**, 4000 (2016).

[40] G. Shirane, Phys. Rev. **86**, 219 (1952).

[41] X. Tan, C. Ma, J. Frederick, S. Beckman, and K. G. Webber, J. Am. Ceram. Soc. **94**, 4091 (2011).

[42] K. M. Rabe, Antiferroelectricity in Oxides: A Reexamination, in *Functional Metal Oxides* (Wiley-VCH Verlag GmbH and Co. KGaA, Weinheim, 2013), pp. 221–244.

[43] C. Lenser, A. Koehl, I. Slipukhina, H. Du, M. Patt, V. Feyer, C. M. Schneider, M. Lezaic, R. Waser, and R. Dittmann, Adv. Funct. Mater. **25**, 6360 (2015).

[44] D. D. Cuong, B. Lee, K. M. Choi, H.-S. Ahn, S. Han, and J. Lee, Phys. Rev. Lett. **98**, 115503 (2007).

[45] Y. Y. Guo, H. M. Liu, D. P. Yu, and J.-M. Liu, Phys. Rev. B **85**, 104108 (2012).

[46] X. Hao, Z. Wang, M. Schmid, U. Diebold, and C. Franchini, Phys. Rev. B **91**, 085204 (2015).

[47] F. Yang, Q. Zhang, Z. Yang, J. Gu, Y. Liang, W. Li, W. Wang, K. Jin, L. Gu, and J. Guo, Appl. Phys. Lett. **107**, 082904 (2015).

[48] U. Aschauer and N. A. Spaldin, J. Phys.: Condens. Matter **26**, 122203 (2014).

[49] A. V. Krukau, O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, J. Chem. Phys. **125**, 224106 (2006).