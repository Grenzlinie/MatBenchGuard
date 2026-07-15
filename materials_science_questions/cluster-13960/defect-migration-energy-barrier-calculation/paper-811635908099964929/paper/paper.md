PHYSICAL REVIEW B 84, 054105 (2011)

![](./images/811635908099964929_1.jpg)

# U and Xe transport in $UO_{2\pm x}$: Density functional theory calculations

D. A. Andersson, B. P. Uberuaga, and P. V. Neriakar
Materials Science and Technology Division, Los Alamos National Laboratory, Los Alamos, NM 87545, USA

C. Unal
Decision Applications Division, Los Alamos National Laboratory, Los Alamos, NM 87545, USA

C. R. Stanek
Materials Science and Technology Division, Los Alamos National Laboratory, Los Alamos, NM 87545, USA

(Received 7 January 2011; revised manuscript received 30 May 2011; published 9 August 2011)

The detrimental effects of the fission gas Xe on the performance of oxide nuclear fuels are well known. However, less well known are the mechanisms that govern fission gas evolution. Here, to better understand bulk Xe behavior (diffusion mechanisms) in $UO_{2\pm x}$ we calculate the relevant activation energies using density functional theory techniques. By analyzing a combination of Xe solution thermodynamics, migration barriers, and the interaction of dissolved Xe atoms with U, we demonstrate that Xe diffusion predominantly occurs via a vacancy-mediated mechanism. Since Xe transport is closely related to the diffusion of U vacancies, we have also studied the activation energy for this process. To best reproduce experimental data for the Xe and U activation energies, it is critical to consider the active charge-compensation mechanism for intrinsic defects in $UO_{2\pm x}$. Due to the high thermodynamic cost of reducing $U^{4+}$ ions, any defect formation occurring at a fixed composition, i.e., no change in $UO_{2\pm x}$ stoichiometry, always avoids such reactions, which, for example, implies that the ground-state configuration of an O Frenkel pair in $UO_2$ does not involve any explicit local reduction (oxidation) of U ions at the O vacancy (interstitial).

DOI: 10.1103/PhysRevB.84.054105
PACS number(s): 61.72.—y, 66.30.Lw, 66.30.Ny, 66.10.C—

## I. INTRODUCTION

The evolution of fission gases in nuclear fuels is closely coupled to their performance. For example, the formation and retention of fission gas bubbles induces fuel swelling, which in turn leads to mechanical interaction with the clad, thereby increasing the probability for clad breach. $^{1}$ Retained fission gas bubbles also decrease the thermal conductivity of the fuel and consequently contribute to limiting the operating temperature and the degree of burn-up. Alternatively, fission gas can be released from the fuel to the plenum, which increases the pressure on the clad walls. Most fission gases have low solubility in the fuel matrix $^{2-5}$ and as a result there is a significant driving force for segregation of gas atoms to extended defects such as grain boundaries or dislocations and subsequently for nucleation of gas bubbles at these sinks. Fission gas insolubility is most pronounced for large fission gas atoms, notably Xe. $^{2}$ Segregation to grain boundaries is often assumed to be followed by a more rapid release to the fuel plenum, either via fast diffusion of individual gas atoms along grain boundaries or via cooperative transport mechanisms involving interlinking nucleated gas bubbles and leading to intergranular separation. $^{1,5}$ Independent of the mechanism, the first rate-determining step for fission gas release is diffusion of individual gas atoms through the fuel matrix to existing bubbles, dislocations, or grain boundaries (sinks), which is a process governed by 1) bulk diffusion of gas atoms, 2) the driving force for segregation to existing sinks, and 3) the saturation limit of the sinks.

In this paper we focus on the bulk diffusion mechanisms of Xe by calculating the activation energies for Xe and U transport as a function of $UO_{2\pm x}$ stoichiometry using density functional theory (DFT) methods. In an attempt to improve the theoretical predictions we explicitly consider different possibilities for the charge-compensation mechanism of defects in $UO_{2\pm x}$, which arise due to the variable valency of U. After assessing the accuracy and identifying systematic errors in our theoretical calculations we classify the most probable Xe and U diffusion mechanisms.

This paper is organized as follows: Section II provides a brief overview of existing models for Xe incorporation in $UO_{2\pm x}$ and the corresponding diffusion models. The theoretical methodology to be used is then outlined in Sec. III. After this we discuss and analyze results from our DFT calculations in Sec. IV, and finally we present our conclusions in Sec. V.

## II. EXISTING MODELS FOR THE SOLUBILITY AND DIFFUSION OF XE IN $UO_{2\pm x}$

### A. Thermodynamics

Due to its high impact on nuclear fuel performance the properties of Xe in $UO_{2\pm x}$ have been extensively studied using a variety of theoretical $^{2,6-24}$ and experimental techniques. $^{3-5,25-31}$ Matzke $^{3-5}$ published several reviews on this topic and concluded that Xe diffusion can be represented by an Arrhenius model, $D = D_0 e^{-E_a/k_b T}$, with activation energies $(E_a)$ that depend on $UO_{2\pm x}$ stoichiometry. This model is summarized in Table V in Sec. IV, which also specifies the corresponding Arrhenius models for vacancy-assisted diffusion of U ions (as well as the activation energies calculated in this paper). These models are valid under thermal equilibrium conditions and do not account for excess concentration of, e.g., U vacancies produced from irradiation, even though such defects are created

1098-0121/2011/84(5)/054105(12)
054105-1
©2011 American Physical Society

during burn-up or Xe diffusion via transient nonequilibrium sites. $^{14}$

To gain additional insight into the atomistic mechanisms that underly Xe transport, several theoretical studies have been undertaken. Catlow $^{6}$ and Ball and Grimes $^{7,18}$ used empirical pair potentials to determine the most stable trap sites for Xe as functions of $UO_{2\pm x}$ stoichiometry. According to Ball and Grimes $^{7}$ Xe atoms either reside in a neutral trivacancy cluster (two O vacancies, $V_O$, and one U vacancy, $V_U$, abbreviated as $V_{UO_2}$) for $UO_{2-x}$ and $UO_2$, a divacancy (one $V_O$ and one $V_U$, abbreviated as $V_{UO}$) for $UO_2$, or in a U vacancy ( abbreviated as $V_U$) for $UO_{2+x}$. Note that Ball and Grimes found divacancies and trivacancies to be competing trap sites for stoichiometric $UO_2.^{7}$ In this paper trap sites are denoted as, e.g., $V_{UO_2}$ and Xe occupying one of these sites as, e.g., $Xe_{UO_2}$. Recent theoretical studies based on different DFT implementations $^{9-11}$ provide similar conclusions. Most of these studies apply the thermodynamic point defect model summarized in Table I for estimating the stability of Xe in different trap sites, which was originally presented by Catlow. $^{12}$ The key quantities in this model are the Schottky (S) defect formation energy ($E_S$, a neutral unbound defect consisting of one $V_U$ and two $V_O$) and the O Frenkel (F) pair formation energy ($E_F$, a neutral unbound defect consisting of one $V_O$ and one O interstitial, $O_i$), as well as the binding energies of trivacancies ($B_{nt}$) and divacancies ($B_{dv}$). Apparent finite-temperature trap site formation energies that emerge from considering multiple-defect equilibria were derived by Crocombette $^{32}$ and also applied by Nerikar $et$ $al.^{11}$ A related model was introduced by Geng $et$ $al.$ in the $UO_{2+x}$ regime. $^{24}$ In principle, our study could be expanded to include such effects, but this exercise has been left as future work, and our discussion refers to the thermodynamic model in Table I. The stability of a Xe trap site is calculated as the sum of the trap formation energy and the energy associated with inserting a Xe atom into the already existing trap site, which is referred to as the solution energy of Xe atoms. $^{13}$ The preference of Xe to occupy different trap sites depending on the $UO_{2\pm x}$ stoichiometry is a consequence of the change in trap site formation energy as a function of the O content. Due to their large size, Xe atoms always favor vacancy trap site positions over interstitial sites. $^{9,11}$

### B. Kinetics
The Xe solution thermodynamics establishes the foundation for species transport, and Ball and Grimes $^{7,18}$ further investigated how the Xe atoms may move from one lattice site to another by binding a second $V_U$ to the respective Xe trap sites. They proposed that Xe transport occurs by the Xe atom jumping from its original trap site to the second bound $V_U$, which constitutes the center of a new Xe trap site after this migration step. The migration barrier for Xe atoms occupying $V_{UO_2}$ trap sites ($Xe_{UO_2}$) was predicted to be as low as 0.11 eV, while the corresponding barrier was 1.58 eV for Xe atoms in $V_U$ trap sites $^{7}$ ($Xe_U$). The latter mechanism involves displacement of two nearby oxygen ions into interstitial positions. Ball and Grimes $^{7}$ found that the barrier for $Xe_U$ can be reduced by placing the interstitial O ions created when forming two nearest-neighbor O vacancies ($V_O$) farther away from the trap site, which is effectively equivalent to forming two bound Frenkel defects. This results in a geometry that locally resembles the saddle point for $Xe_{UO_2}$, and the corresponding barriers were also predicted to be similar.

As we will show, this Xe migration barrier does not contribute to the total Xe activation energy, which instead consists of three components: the $V_U$ formation energy, the binding energy of this vacancy to the Xe trap site, and the intracluster migration barrier for the individual $V_U$ bound to this cluster. That is, the rate-limiting step is not Xe motion within the cluster, but the migration of the second $V_U$ within the cluster; without the motion of the second bound $V_U$ Xe does not diffuse. This mechanism is schematically illustrated in Fig. 1. A related mechanism was treated by Ball, and Grimes, $^{7}$ but they did not consider intracluster migration of the second bound $V_U$. Alternatively, Catlow $^{6}$ suggested that in certain concentration regimes, transport of Xe may be controlled by the formation of more mobile Xe defects such as Xe occupying anion vacancies or interstitials. $^{14}$ However, due to the high thermodynamic cost of forming such defects $^{9,11}$ we have not considered this possibility in the present paper as we expect their contribution to be small at equilibrium. Similarly, the possibility of pure kinetic control where the activation energy for Xe diffusion is identical to or higher than the activation energy for U diffusion is discarded. The latter conclusion is based on the observation that, according to experiments (summarized in Sec. IV in Table V), the U and Xe activation energies are distinct in all O composition regimes and the Xe activation energy is always the lowest.

Recently, Yun $et$ $al.$ studied Xe diffusion using DFT methods. $^{9,10}$ They applied the generalized gradient approximation (GGA) for the exchange-correlation potential and performed calculations with and without spin polarization as well as with and without spin-orbit coupling. Specifically, they considered the mobility of Xe atoms within certain defect clusters and reported new mechanisms for the correlated motion of Xe atoms, $V_O$ and $V_U$. From these calculations they suggested that Xe atoms may diffuse via a barrierless strain-driven mechanism that emerges from the redistribution of $V_O$ and $V_U$. This Xe migration mechanism is somewhat different from that proposed by Ball and Grimes, $^{7,18}$ though both predict that Xe atoms may migrate along low-barrier pathways. Yun $et$ $al.^{9,10}$ did not attempt to calculate the total Xe activation energies under thermal equilibrium, but identified the diffusion of U vacancies as the rate-limiting step.

TABLE I. The stoichiometry-dependent $V_U$, $V_{UO}$ and $V_{UO_2}$ trap site formation energies, as defined according to Catlow. $^{6}$ $E_S$ is the Schottky defect formation energy, $E_F$ is the Frenkel formation energy, $B_{dv}$ is the binding energy of the $V_{UO}$ divacancy, and $B_{nt}$ is the binding energy of the neutral $V_{UO_2}$ trivacancy.

<table>
<thead>
  <tr>
    <th></th>
    <th>$UO_{2-x}$</th>
    <th>$UO_2$</th>
    <th>$UO_{2+x}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$V_U$</td>
    <td>$E_S$</td>
    <td>$E_S$-$E_F$</td>
    <td>$E_S$-$2E_F$</td>
  </tr>
  <tr>
    <td>$V_{UO}$</td>
    <td>$E_S$-$B_{dv}$</td>
    <td>$E_S$-$\frac{1}{2}E_F$-$B_{dv}$</td>
    <td>$E_S$-$E_F$-$B_{dv}$</td>
  </tr>
  <tr>
    <td>$V_{UO_2}$</td>
    <td>$E_S$-$B_{nt}$</td>
    <td>$E_S$-$B_{nt}$</td>
    <td>$E_S$-$B_{nt}$</td>
  </tr>
</tbody>
</table>


![](./images/811635908099964929_2.jpg)

FIG. 1. (Color online) Schematic illustration of Xe diffusion via a vacancy mediated mechanism. For simplicity the cubic O sublattice is omitted and only the fcc U sublattice is shown. The proposed mechanism is valid for all Xe trap sites ($V_{UO_2}$, $V_{UO}$, and $V_U$). Xe atoms are shown in yellow, U in blue, and vacancies are represented by squares. (a) (100) projection of the U sublattice with Xe occupying a $V_U$ site and a second $V_U$ located several lattice distances away from the Xe trap site (unbound). Note that the vacancy occupied by the Xe atom is not indicated by a square. $UO_{2\pm x}$ with Xe occupying a trap site is defined as a reference and, consequently, the energy in (a) is set to the $V_U$ formation energy ($E_F^{V_U}$). (b) The $V_U$ is moved to the Xe trap site and the Xe atom occupies the central position of the void created by the original trap site, and the second bound $V_U$. The total energy changes by $-E_B$ (binding energy) between (a) and (b); consequently the energy of this configuration is $E = E_F^{V_U} - E_B$. (c) Three-dimensional view of the fcc U sublattice with a Xe atom occupying a $V_U$ and a second $V_U$ bound to this trap site. The highlighted U atom can migrate into one of the cluster vacancies, thus giving rise to net Xe diffusion. (d) Equivalent to the defect cluster in (c) but with the highlighted U atom translated from its original position in (c) into the nearest neighbor vacancy site along the $[1/2\ 0\ 1/2]$ lattice vector. The transformation from (c) to (d) is an activated process associated with a barrier $E_m$, as indicated in the figure.

## III. METHODOLOGY

### A. Density functional theory calculations

#### 1. Approach

The DFT calculations were performed with the Vienna ab initio simulation package (VASP) $^{33-35}$ using the projector-augmented-wave (PAW) method. $^{36,37}$ The rotationally invariant LDA $+U$ (where LDA is the local-density approximation) functional due to Lichtenstein $et\ al.^{38}$ was employed to describe the exchange and correlation effects and in particular to capture the intraband Coulomb repulsion among the $5f$ electrons. All calculations include spin polarization and $\mathbf{1K}$ antiferromagnetic ordering of the localized U spins is assumed, which is slightly different from the $\mathbf{3K}$ ordering observed in experiments $^{39-41}$ and from DFT allowing for spin-orbital coupling and noncollinear magnetic ordering. $^{42}$ To simplify the calculation of defect properties the latter two contributions are ignored in this paper. Recent reports have shown that the LDA/GGA $+U$ methodology correctly describes many of the relevant properties of $UO_2$ and $UO_{2+x}.^{42-56}$ In accordance with earlier LDA $+U$ studies the $U$ and $J$ values were set to $U = 4.5$ eV and $J = 0.51$ eV. $^{46}$

Defect properties were calculated within a $2 \times 2 \times 3$ (144 atoms for stoichiometric $UO_2$) supercell expansion of the cubic fluorite unit cell. This larger cell was used in order to better treat the more extended Xe clusters and keep interactions among their periodic images controlled. The supercell volumes were kept fixed at the corresponding calculated volume of $UO_2$, for which we predict $a = 5.45$ Å within the current DFT scheme $^{52}$ compared with 5.47 Å observed in experiments. $^{57}$ A $2 \times 2 \times 1$ Monkhorst-Pack k-point mesh $^{58}$ with a Gaussian smearing of 0.05 eV was used for all defect calculations within the $2 \times 2 \times 3$ supercell. We used a plane-wave cutoff energy of 400 eV. All internal structural parameters were relaxed until the total energy was converged or the Hellmann-Feynman forces on each ion were $<0.02$ eV/Å. The forces acting on Xe atoms are difficult to converge to the required $<0.02$ eV/Å limit, but since these structures nevertheless fulfill the total energy convergence criteria they are here considered to be fully relaxed. The migration barriers were calculated assuming harmonic transition-state theory (TST) by using the climbing-image nudged elastic band methodology, as implemented in the VASP. $^{59}$ Unless otherwise noted, the saddle point calculations were performed within a $2 \times 2 \times 2$ supercell, and for each barrier we applied three or four nudged elastic band images. Atomic Xe was used as the reference state for the Xe solution energies.

### 2. Issues related to orbital ordering and metastable electronic solutions

Dorado $et\ al.$ have shown that LDA/GGA $+U$ calculations applied to $UO_{2\pm x}$ may converge to metastable solutions that correspond to different U $5f$ orbital occupations. $^{44,53}$ Similar conclusions were obtained by Meredig $et\ al.^{60}$ and for Pu oxides by Jomard $et\ al.^{61}$ Due to this ambiguity, any defect parameters derived from such calculations have some uncertainty, and Dorado $et\ al.$ concluded that the spread in, for example, Frenkel and Schottky defect energies found in the literature could be traced back to this issue. $^{44,53}$ To ensure that the ground-state electronic structure is reached for each compound one should monitor the $f$ orbital occupation matrices. Dorado $et\ al.$ established the ground-state electronic structure of bulk $UO_2$ by applying different initial occupation matrices and by performing an extensive search over the space of allowed U $5f$ occupations matrices. $^{44,53}$ Due to the numerous possible distributions of charge-compensating $U^{5+}$ ions for nonstoichiometric compounds, this approach becomes quite cumbersome for the cluster defects of present interest. For this reason we have not been able to apply a complete systematic occupation matrix search to the $UO_{2\pm x}$ compounds studied in this paper. Instead we have addressed this issue by performing multiple simulations with reduced

structural symmetry (C1) for each $UO_{2\pm x}$ compound, and, by monitoring the occupation matrices, we ascertain that all structures reach similar U $5f$ orbital occupancies, presumably corresponding to the ground-state solution. Note that, even though the structural symmetry is reduced to C1, symmetry operations are kept on in the VASP code for these simulations. Both the standard diagonal occupation matrices and the occupation matrices obtained for the ground-state fluorite $UO_{2}$ solution $^{44,53}$ were used for initializing the electronic self-consistency cycles. For each $UO_{2\pm x}$ structure we always report the lowest-energy solution that we are able to obtain. Assuming that a careful search is performed with respect to structural distortions, the final solution for the $UO_{2\pm x}$ compounds is typically not very sensitive to this choice of initial occupation matrix. Nevertheless, we cannot absolutely guarantee that we have reached the electronic configuration that corresponds to the lowest-energy solution. By introducing small distortions to the perfect fluorite $UO_{2}$ structure we obtained a solution with 0.003 eV lower energy per $UO_{2}$ formula unit than for the solution obtained for perfect $UO_{2}$ by using occupation matrix control. This energy reduction is different from the much larger Jahn-Teller (JT) derived reductions described below. $^{44}$ In the present analysis we have used the somewhat higher energy obtained for perfect $UO_{2}$ by using occupation matrix control. The calculation scheme outlined above is here labeled as A (no JT).

A second approach labeled B (JT) was also attempted, for which we explicitly turn all symmetries off in the VASP code and then proceed according to the same scheme as for A (no JT). This yields a $UO_{2}$ ground state that is slightly distorted from the ideal fluorite lattice assumed in the first calculation scheme, which has been described as a JT distortion in previous reports. $^{44}$ While the corresponding structural distortions are harder to distinguish in the defect-containing lattices, the occupation matrices reveal that they reach a similar electronic structure state. Even though the absolute energies differ between the first and second approaches, for the relative quantities studied in this paper, both frameworks capture the same physical trends. As illustrated in Table II (the details of this table are discussed in Sec. III B), A (no JT) predicts elementary defect parameters that are up to 1-2 eV lower than for B (JT). Approach A (no JT) agrees somewhat better with available experiments. This may result from the fact that the distorted $UO_{2}$ structure obtained within approach B (JT) is mainly relevant for low temperatures where deviations from the cubic fluorite structure have been observed experimentally, $^{41,62-65}$ while experiments and technological applications pertinent to nuclear fuels are primarily concerned with high-temperature properties for which $UO_{2\pm x}$ is stabilized in the fluorite structure. However, this paper does not aim at determining which approach is most accurate, and for this reason all defect parameters are reported within both frameworks A (no JT) and B (JT).

### B. Modeling the oxidation and charge states of defects in $UO_{2\pm x}$
#### 1. Charge-transfer models
An O Frenkel defect in $UO_{2}$ is formed by the simultaneous creation of an O vacancy $(V_{O})$ and an O interstitial $(O_{i})$, which are then separated from each other in order to avoid recombination. This implies that the overall composition is kept fixed and there is no net oxidation or reduction. Ideally $E_{F}$ should be calculated by forming the two individual point defect constituents within a sufficiently large supercell.

TABLE II. The Frenkel energy $(E_{F})$, the Schottky energy $(E_{S})$, the binding energy of the $V_{UO}$ divacancy $(B_{dv})$, and the binding energy of the $V_{UO_{2}}$ trivacancy $(B_{nt})$ calculated from DFT and compared with selected experimental and theoretical data. "Neutral" refers to standard DFT calculations for the individual defect components, "Charged" refers to charged defect calculations for the individual components, and "O-S" short for one-supercell, implies that all defects were treated within one single supercell as described in the text. The row labeled, "Charged uncorrected" does not include the corrections for image charges or for the shift of the Kohn-Sham eigenvalues (see text for details). Positive binding energies mean attraction between the defect constituents. For each defect parameter we report the values obtained within simulation approaches A (no JT) and B (JT). As indicated within parentheses Refs. 43 and 44 report values corresponding to both approaches A (no JT) and B (JT).

<table>
<thead>
<tr>
<th>
</th>
<th>
$E_{F}$ (eV)
</th>
<th>
$E_{S}$ (eV)
</th>
<th>
$B_{dv}$ (eV)
</th>
<th>
$B_{nt}$ (eV)
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
A (no JT)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Neutral
</td>
<td>
5.26
</td>
<td>
10.15
</td>
<td>
2.93
</td>
<td>
5.58
</td>
</tr>
<tr>
<td>
Charged corrected
</td>
<td>
3.32
</td>
<td>
6.00
</td>
<td>
1.22
</td>
<td>
1.43
</td>
</tr>
<tr>
<td>
Charged uncorrected
</td>
<td>
3.10
</td>
<td>
4.98
</td>
<td>
0.39
</td>
<td>
0.41
</td>
</tr>
<tr>
<td>
O-S
</td>
<td>
3.39
</td>
<td>
6.39
</td>
<td>
1.20
</td>
<td>
1.82
</td>
</tr>
<tr>
<td>
B (JT)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</td>
</tr>
<tr>
<td>
Neutral
</td>
<td>
6.40
</td>
<td>
11.96
</td>
<td>
3.35
</td>
<td>
6.46
</td>
</tr>
<tr>
<td>
Charged corrected
</td>
<td>
4.26
</td>
<td>
7.65
</td>
<td>
1.52
</td>
<td>
2.15
</td>
</tr>
<tr>
<td>
Charged uncorrected
</td>
<td>
4.07
</td>
<td>
6.83
</td>
<td>
0.86
</td>
<td>
1.32
</td>
</tr>
<tr>
<td>
O-S
</td>
<td>
4.10
</td>
<td>
7.12
</td>
<td>
1.33
</td>
<td>
1.62
</td>
</tr>
<tr>
<td>
Reference data
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</td>
</tr>
<tr>
<td>
Jackson $et$ $al.^{69}$ (theory)
</td>
<td>
4.76
</td>
<td>
7.3
</td>
<td>
–
</td>
<td>
–
</td>
</tr>
<tr>
<td>
Dorado $et$ $al.^{43,44}$ (theory)
</td>
<td>
5.25 (A), 6.48 (B)
</td>
<td>
–
</td>
<td>
–
</td>
<td>
–
</td>
</tr>
<tr>
<td>
Nerikar $et$ $al.^{51}$ (theory)
</td>
<td>
3.95
</td>
<td>
7.6
</td>
<td>
3.67
</td>
<td>
5.1
</td>
</tr>
<tr>
<td>
Matzke$^{3-5}$ (exp.)
</td>
<td>
3.0–4.0
</td>
<td>
6–7
</td>
<td>
–
</td>
<td>
–
</td>
</tr>
</tbody>
</table>

Unfortunately, this is often difficult to achieve due to the computational limitations of current DFT implementations. Consequently, $E_F$ is usually calculated from the individual defect energies, i.e., the energy needed to create $O_i$ and $V_O$ within separate supercells. It is important to understand that this approach assumes that local oxidation and reduction occurs for the Frenkel constituents, such that $O_i$ is associated with two explicit $U^{5+}$ ions and $V_O$ with two $U^{3+}$ ions (in reality these ions do not formally reach $U^{5+}$ or $U^{3+}$ integer charge states, but they are nevertheless distinctly different from the $U^{4+}$ ions and exhibit partial charge transfer). This is a consequence of the fact that calculations for the individual defect components assume oxidization ($UO_{2+x}$ for interstitials) and reduction ($UO_{2-x}$ for vacancies) in order to maintain charge neutrality within the supercells. As a note, the charge compensation for $UO_{2-x}$ in fact involves four $U^{(3+\delta)+}$ rather than two $U^{3+}$ ions, which is expected due to the thermodynamic resistance to $U^{4+}$ reduction.

One way of studying Frenkel defect formation without assuming local oxidation or reduction is to perform so-called charged supercell calculations, where electrons are added or removed in order to suppress local oxidation or reduction of $U^{4+}$ ions. Charge neutrality is maintained by applying a homogeneous background charge according to the standard procedure for studying charged defects in semiconductors and insulators. $^{67,68}$ As an example, for $O_i$ we add two extra electrons in order to avoid formation of $U^{5+}$ ions, and for $V_O$ we correspondingly remove two electrons in order to avoid formation of $U^{3+}$ ions. Note that the extra charge does not end up as localized states on the interstitial ion or the vacant site, but rather occupies localized states ascribed to the U ions that would otherwise have mixed valance character ($U^{3+}$ or $U^{5+}$). The extra electrons that are added or removed ultimately cancel out in the calculation of $E_F$. Henceforth, the charged and neutral labels will be used to designate the charged and neutral supercell approaches to calculate defect energies, respectively. According to our calculations, the Frenkel defects formed assuming no local charge compensation (no $U^{3+}$ or $U^{5+}$ ions) are more stable than the corresponding Frenkel defects that include local charge compensation ($U^{3+}$ and $U^{5+}$ ions). The higher stability of Frenkel defects within the charged calculation scheme is a consequence of the high cost of reducing the $U^{4+}$ to $U^{3+}$ ions. In fact, if the Frenkel defect is created within an already oxidized sample ($UO_{2+x}$) the neutral solution is preferred, since there is no need to create any $U^{3+}$ ions. From a thermodynamic perspective, it is less costly to reduce the preexisting $U^{5+}$ ions back to $U^{4+}$. The Frenkel energies obtained for $UO_2$ within the charged approach and for $UO_{2+x}$ within the neutral approach are identical (assuming the charged calculations are corrected according to the procedure outlined below). Nerikar et al. $^{11}$ and Crocombette et al. $^{66}$ have studied the stability of charged point defects in $UO_2$, and their results support the high stability of Frenkel defects with charged individual components, thus confirming our present reasoning. The charged approach was also employed for studying other defects or defect configurations where no net oxidation or reduction takes place, e.g., the neutral Schottky defect. The latter defect is also more stable within the charged scheme for stoichiometric $UO_2$.

## 2. Corrections for charged supercells

Due to the image charges introduced by the periodic boundary conditions, charged supercell calculations converge slowly with respect to the cell size and there is also a shift of the electrostatic potential which is reflected in the calculated total energies for the charged systems. We have attempted to quantify these errors using the techniques described in, for example, Refs. 67 and 68 The potential alignment was achieved by monitoring the localized U s states, and image charge corrections were applied according to the modified multipole correction scheme presented by Lany and Zunger. $^{67}$ The accuracy of this scheme is expected to decrease for the high-charge states encountered in some of our calculations. The potential alignment procedure is complicated by the mixed-valence character of U ions, and specifically supercells with high charge states give rise to uncertainties. As described below, we have also derived one data set by modeling all defects within one single supercell, which circumvents the need for applying corrections to charged supercells but at the same time introduces possible errors due to (regular) defect interactions within supercells, i.e., system-size effects. This approach presents some issues for the Schottky defect, which was instead treated in oxidized supercells according to the procedure exemplified for Frenkel defects in Sec. III B 1. The main reason for using this second one-supercell (O-S) approach to calculate defect energies is to provide uncertainty quantification, in particular for the image charge and potential alignment corrections applied to the high-charge states that occur in some of our calculations.

The charged and neutral approaches to calculate $E_F$ and $E_S$ represent two limits. Table II highlights that the calculated $E_F$ and $E_S$ values, and thus any quantities derived from them, are different between the two approaches. In principle, the lowest defect energy predicted among the neutral and charged approaches represents the active defect type, which according to our calculations always corresponds to the charged scheme for stoichiometric $UO_2$. To verify this conclusion, we have calculated the Frenkel defect formation energy within one single supercell. The vacancy and interstitial were separated from each other in the $2 \times 2 \times 3$ supercell, which corresponds to a separation of $1.64a_0$ or $8.93$ Å. This calculation predicts that no local charge compensation takes place, implying that there are no explicit $U^{3+}$ or $U^{5+}$ ions present in the neighborhood of the individual point defects. This agrees with the fact that for $UO_2$ the charged scheme predicts lower $E_F$ than the neutral scheme.

Comparing the A (no JT) O-S value for $E_F$ of 3.39 eV with the uncorrected charged value of 3.10 eV, we conclude that $E_F$ derived from the charged scheme is underestimated by 0.28 eV. The correction obtained from finite-size effects and potential alignment is similar; 0.32 eV, giving $E_F = 3.43$ eV. There is some ambiguity in the potential alignment procedure due to the mixed-valence character of $UO_{2\pm x}$ and the dispersed character of charge-compensating defects. However, this contribution is rather small for $E_F$ (-0.05 eV) and the agreement between the O-S value for $E_F$ and the charged value that includes only image charge corrections (3.48 eV) is already quite good.

Some Coulomb interaction between $V_O$ and $O_i$ may still exist for the $E_F$ calculation within the single $2 \times 2 \times 3$

supercell. However, from the calculated energy vs. separation distance relation, we estimate this error to be rather small. Due to more limited separation of the individual defect components for $E_S$, we calculated the O-S $E_S$ value by forming the oxygen defects in already oxidized samples ($\text{UO}_{2+x}$). For this composition range the neutral solution is preferred since there is no need to form $\text{U}^{3+}$ ions. Moreover, it should be identical to the charged solution for stoichiometric $\text{UO}_2$ according to the results for $E_F$ presented in Sec. III B 1. This yields 6.39 eV for O-S A (no JT) to be compared with 6.22 eV for the charged A (no JT) data set (6.10 eV without the potential alignment correction). For comparison, the value derived from creating a Schottky defect within the $2 \times 2 \times 3$ supercell is 0.5 eV higher (6.91 eV). The O-S and charged data sets for approach B (JT) (see Table II) yield similar conclusions as for approach A (no JT), even though both $E_F$ and $E_S$ are predicted to be somewhat higher.

### 3. Defect formation energies
$E_F$ and $E_S$ calculated according to the procedures specified above are collected in Table II, which also contains experimental reference values $^{3-5}$ as well as selected theoretical estimates. $^{44,51,70}$ Except for Ref. 70, the theoretical references rely on DFT methods. They all apply the GGA for the exchange-correlation potential and include Hubbard $U$ correction terms for treating the correlated U $5f$ electrons. These DFT studies used techniques that correspond to our neutral approach; however, Ref. 51 also investigated the effects of introducing charged defects. For the neutral data set, our predictions are higher than most existing data, which, according to studies by Dorado $et$ $al.^{44,53}$ are likely related to the existence of metastable electronic solutions for the reference $\text{UO}_2$ structure. Recall that this issue was addressed here by following the procedure proposed by Dorado $et$ $al.^{53}$ As expected, the neutral $E_F$ values predicted in this paper and by Dorado $et$ $al.^{43,44}$ are in good agreement, especially considering the fact that different exchange-correlation potentials and supercells were used. The 3–4 eV experimental range for $E_F$ was derived from analysis of O diffusivity in stoichiometric $\text{UO}_2$. Known uncertainties related to the migration barriers of O interstitials and vacancies give rise to the stated 3–4 eV span for $E_F$. The charged and O-S $E_F$ values obtained from approach A (no JT) are within the experimental 3–4 eV range, while the values obtained from approach B (JT) are in the 4–5 eV range. The $E_F$ values from the neutral data sets are all significantly higher (>5 eV). $E_S$ can then be calculated by using the value for $E_F$ obtained from O diffusivity measurements in $\text{UO}_2$, the measured U vacancy migration barrier, and the measured total activation energy for U diffusion in the equation relating these parameters and $E_S$ to each other [Eq. (1)], which gives the experimental estimate of 6–7 eV (6.2–7.2 eV to be exact) assuming that U vacancies are the active species. The charged and O-S data exhibit a spread over almost 2 eV from 6.00 eV (charged, approach A) to 7.65 eV (charged, approach B), which is within or just outside the experimental range, respectively. As for $E_F$, the neutral $E_S$ data are always significantly higher than in the experiments. Note that the experimental derivation relies on values for the migration of U vacancies, a quantity which is not well known, as described in Sec. IV B. Consequently, reanalysis of the experimental defect parameters would be worthwhile, but it is not addressed here.

To summarize, the $E_F$ and $E_S$ values calculated within the neutral approach are always higher than the experimental estimates. $^{3-5}$ which is expected since the assumption of local neutrality does not correspond to the ground-state electronic configuration of these defects. Rather, the lowest-energy state is one in which the defects charge compensate themselves. The charged and O-S data sets are in much better agreement with experiments. These results demonstrate that, in order to achieve accurate predictions of intrinsic defect processes, we need to explicitly account for the active $\text{UO}_{2\pm x}$ charge-compensation mechanism. From the data for $E_F$ and $E_S$ we cannot conclusively say which approach, A (no JT) or B (JT), agrees better with experiments. The corrected charged data are slightly higher than the O-S data for approach B (JT), while the opposite relation emerges for A (no JT).

## IV. RESULTS AND DISCUSSION
The results section is divided into three parts; first, we calculate the thermodynamic stability of Xe trap sites and the Xe solution energy for these sites; second, we study diffusion of U via vacancy mechanisms; and third, we use the U vacancy diffusion data and the trap site stability as the basis for predicting the Xe transport properties.

### A. Stability of Xe trap sites
The formation energy of Xe trap sites as a function of $\text{UO}_{2\pm x}$ stoichiometry is listed in Table III, and the Xe solution energy is summarized in Table IV. Both the data obtained within simulation approach A (no JT) and B (JT) are listed. Even though the absolute numbers differ somewhat for these two cases (numbers found via approach B are always higher), the predicted physical trends are similar. In agreement with earlier studies we predict $V_{\text{UO}_2}$ to be the most stable Xe trap site for $\text{UO}_{2-x}.^{7,11}$ We find that the most stable $V_{\text{UO}_2}$ cluster configuration corresponds to a linear orientation of the O-U-O vacancies along [111] directions; however, Xe prefers to sit in $V_{\text{UO}_2}$ clusters where the two $V_O$ are aligned as nearest neighbors in [100] directions. The $V_{\text{UO}_2}$ data in Tables III and IV all refer to the latter case. The formation energy of the [111] $V_{\text{UO}_2}$ cluster is 0.38 eV (approach A) and 0.42 eV (approach B) lower than for the [100] configuration. For stoichiometric $\text{UO}_2$ we calculate $V_{\text{UO}}$ to be the preferred site for the charged and O-S data sets, even though $V_{\text{UO}_2}$ is only a few tenths of an electron volt higher. The neutrality scheme predicts $V_{\text{UO}_2}$ to be the most stable Xe trap site. The literature data for the trap site stability at the stoichiometric $\text{UO}_2$ composition find $X_{\text{eUO}}$ and $X_{\text{eUO}_2}$ to be rather close, which is in qualitative agreement with our results even though the detailed balance may exhibit some discrepancies. $^{7,9-11}$ Experimental studies claimed the $V_{\text{UO}_2}$ site to be the preferred one. $^{5}$ However, the experimental conclusions rely on complex defect considerations that may be associated with uncertainties and consequently we would not discard our present findings of competition between $X_{\text{eUO}}$ and $X_{\text{eUO}_2}$ from the charged and O-S defect calculations as incorrect.

<table>
<caption>TABLE III. The calculated formation energy of $V_{\text{U}}$ ($E_{F}^{V_{\text{U}}}$), $V_{\text{UO}}$ ($E_{F}^{V_{\text{UO}}}$), and $V_{\text{UO}_{2}}$ ($E_{F}^{V_{\text{UO}_{2}}}$) Xe trap sites. See the caption of Table II for explanation of the charged, neutral, and O-S labels. The charged data include all corrections applicable to charged supercells, as described in the text. Data are provided for both simulation approach A (no JT) and B (JT).</caption>
<tr><td></td><td>$UO_{2-x}$ (eV)</td><td>$UO_{2}$ (eV)</td><td>$UO_{2+x}$ (eV)</td></tr>
<tr><td>Charged: A (no JT)</td><td></td><td></td><td></td></tr>
<tr><td>$V_{\text{U}}$ ($E_{F}^{V_{\text{U}}}$)</td><td>6.00</td><td>2.69</td><td>$-0.63$</td></tr>
<tr><td>$V_{\text{UO}}$ ($E_{F}^{V_{\text{UO}}}$)</td><td>4.79</td><td>3.13</td><td>1.47</td></tr>
<tr><td>$V_{\text{UO}_{2}}$ ($E_{F}^{V_{\text{UO}_{2}}}$)</td><td>4.57</td><td>4.57</td><td>4.57</td></tr>
<tr><td>Charged: B (JT)</td><td></td><td></td><td></td></tr>
<tr><td>$V_{\text{U}}$ ($E_{F}^{V_{\text{U}}}$)</td><td>7.65</td><td>3.39</td><td>$-0.87$</td></tr>
<tr><td>$V_{\text{UO}}$ ($E_{F}^{V_{\text{UO}}}$)</td><td>6.13</td><td>4.00</td><td>1.87</td></tr>
<tr><td>$V_{\text{UO}_{2}}$ ($E_{F}^{V_{\text{UO}_{2}}}$)</td><td>5.50</td><td>5.50</td><td>5.50</td></tr>
<tr><td>Neutral: A (no JT)</td><td></td><td></td><td></td></tr>
<tr><td>$V_{\text{U}}$ ($E_{F}^{V_{\text{U}}}$)</td><td>10.15</td><td>4.88</td><td>$-0.38$</td></tr>
<tr><td>$V_{\text{UO}}$ ($E_{F}^{V_{\text{UO}}}$)</td><td>7.22</td><td>4.59</td><td>1.95</td></tr>
<tr><td>$V_{\text{UO}_{2}}$ ($E_{F}^{V_{\text{UO}_{2}}}$)</td><td>4.57</td><td>4.57</td><td>4.57</td></tr>
<tr><td>Neutral: B (JT)</td><td></td><td></td><td></td></tr>
<tr><td>$V_{\text{U}}$ ($E_{F}^{V_{\text{U}}}$)</td><td>11.96</td><td>5.56</td><td>$-0.83$</td></tr>
<tr><td>$V_{\text{UO}}$ ($E_{F}^{V_{\text{UO}}}$)</td><td>8.61</td><td>5.42</td><td>2.22</td></tr>
<tr><td>$V_{\text{UO}_{2}}$ ($E_{F}^{V_{\text{UO}_{2}}}$)</td><td>5.50</td><td>5.50</td><td>5.50</td></tr>
<tr><td>O-S: A (no JT)</td><td></td><td></td><td></td></tr>
<tr><td>$V_{\text{U}}$ ($E_{F}^{V_{\text{U}}}$)</td><td>6.39</td><td>3.01</td><td>$-0.38$</td></tr>
<tr><td>$V_{\text{UO}}$ ($E_{F}^{V_{\text{UO}}}$)</td><td>5.19</td><td>3.50</td><td>1.81</td></tr>
<tr><td>$V_{\text{UO}_{2}}$ ($E_{F}^{V_{\text{UO}_{2}}}$)</td><td>4.57</td><td>4.57</td><td>4.57</td></tr>
<tr><td>O-S: B (JT)</td><td></td><td></td><td></td></tr>
<tr><td>$V_{\text{U}}$ ($E_{F}^{V_{\text{U}}}$)</td><td>7.12</td><td>3.03</td><td>$-1.07$</td></tr>
<tr><td>$V_{\text{UO}}$ ($E_{F}^{V_{\text{UO}}}$)</td><td>5.79</td><td>3.74</td><td>1.69</td></tr>
<tr><td>$V_{\text{UO}_{2}}$ ($E_{F}^{V_{\text{UO}_{2}}}$)</td><td>5.50</td><td>5.50</td><td>5.50</td></tr>
</table>

For $UO_{2+x}$ the O-S, charged, and neutral data sets all suggest that $V_{\text{U}}$ is the most stable location for Xe, which follows earlier theoretical estimates. $^{7,11}$

### B. Activation energies for U diffusion

The activation energy for U diffusion via a vacancy mechanism is equal to the sum of the U vacancy formation energy ($E_{F}^{V_{\text{UO}_{z}}}$, where $z=0,1,2$ for $V_{\text{U}}$, $V_{\text{UO}}$ and $V_{\text{UO}_{2}}$ clusters, respectively) and the migration barrier for the U vacancies ($E_{m}^{V_{\text{UO}_{z}}}$);

$$
E_{a}^{\text{U}} = E_{F}^{V_{\text{UO}_{z}}} + E_{m}^{V_{\text{UO}_{z}}}. \tag{1}
$$

Table III lists $E_{F}^{V_{\text{UO}_{z}}}$ as a function of the $UO_{2\pm x}$ stoichiometry. For $UO_{2-x}$ the most stable form of U vacancies is, in fact, as part of the $V_{\text{UO}_{2}}$ trivacancy, and, consequently, the U vacancy formation energy for the hypostoichiometric range should be set equal to the formation energy of the trivacancy instead of the single U vacancy. Also recall that the most stable $V_{\text{UO}_{2}}$ cluster ($V_{\text{O}}$ along [111] directions) is in fact 0.38 eV (approach A) and 0.42 eV (approach B) more stable than the values listed in Table III. According to the neutral data set, the $V_{\text{UO}_{2}}$ (A) or the $V_{\text{UO}}$ (B) clusters are the preferred form of U vacancies at the $UO_{2}$ composition (all defects are in fact rather close in energy), while $V_{\text{U}}$ is predicted to be dominant by the charged and the O-S data sets. $V_{\text{U}}$ is the most stable form of U vacancies in the hyperstoichiometric range.

<table>
<caption>TABLE IV. The solution energy of Xe in $V_{\text{U}}$ (Xe$_{\text{U}}$), $V_{\text{UO}}$ (Xe$_{\text{UO}}$), and $V_{\text{UO}_{2}}$ (Xe$_{\text{UO}_{2}}$) trap sites. See the caption of Table II for explanation of the charged, neutral, and O-S labels. The charged data include the corrections applicable to charged supercells, as described in the text. Data are provided for both simulation approach A (no JT) and B (JT).</caption>
<tr><td></td><td>$UO_{2-x}$ (eV)</td><td>$UO_{2}$ (eV)</td><td>$UO_{2+x}$ (eV)</td></tr>
<tr><td>Charged: A (no JT)</td><td></td><td></td><td></td></tr>
<tr><td>Xe$_{\text{U}}$</td><td>9.26</td><td>5.95</td><td>2.63</td></tr>
<tr><td>Xe$_{\text{UO}}$</td><td>6.01</td><td>4.35</td><td>2.69</td></tr>
<tr><td>Xe$_{\text{UO}_{2}}$</td><td>4.75</td><td>4.75</td><td>4.75</td></tr>
<tr><td>Charged: B (JT)</td><td></td><td></td><td></td></tr>
<tr><td>Xe$_{\text{U}}$</td><td>11.19</td><td>6.93</td><td>2.67</td></tr>
<tr><td>Xe$_{\text{UO}}$</td><td>7.37</td><td>5.24</td><td>3.11</td></tr>
<tr><td>Xe$_{\text{UO}_{2}}$</td><td>5.78</td><td>5.78</td><td>5.78</td></tr>
<tr><td>Neutral: A (no JT)</td><td></td><td></td><td></td></tr>
<tr><td>Xe$_{\text{U}}$</td><td>12.44</td><td>7.17</td><td>1.91</td></tr>
<tr><td>Xe$_{\text{UO}}$</td><td>8.41</td><td>5.78</td><td>3.14</td></tr>
<tr><td>Xe$_{\text{UO}_{2}}$</td><td>4.75</td><td>4.75</td><td>4.75</td></tr>
<tr><td>Neutral: B (JT)</td><td></td><td></td><td></td></tr>
<tr><td>Xe$_{\text{U}}$</td><td>14.80</td><td>8.40</td><td>2.01</td></tr>
<tr><td>Xe$_{\text{UO}}$</td><td>9.76</td><td>6.57</td><td>3.37</td></tr>
<tr><td>Xe$_{\text{UO}_{2}}$</td><td>5.78</td><td>5.78</td><td>5.78</td></tr>
<tr><td>O-S: A (no JT)</td><td></td><td></td><td></td></tr>
<tr><td>Xe$_{\text{U}}$</td><td>8.68</td><td>5.29</td><td>1.91</td></tr>
<tr><td>Xe$_{\text{UO}}$</td><td>6.38</td><td>4.69</td><td>3.00</td></tr>
<tr><td>Xe$_{\text{UO}_{2}}$</td><td>4.75</td><td>4.75</td><td>4.75</td></tr>
<tr><td>O-S: B (JT)</td><td></td><td></td><td></td></tr>
<tr><td>Xe$_{\text{U}}$</td><td>9.47</td><td>5.87</td><td>1.77</td></tr>
<tr><td>Xe$_{\text{UO}}$</td><td>6.94</td><td>4.89</td><td>2.85</td></tr>
<tr><td>Xe$_{\text{UO}_{2}}$</td><td>5.78</td><td>5.78</td><td>5.78</td></tr>
</table>

To complete Eq. (1), $E_{m}^{V_{\text{UO}_{z}}}$ must be calculated for each defect type. Our DFT calculations predict a barrier of approximately 4.81 eV for a U ion migrating along the direct path connecting it with a nearest-neighbor $V_{\text{U}}$ [Fig. 2(a)]. The saddle point is located halfway between the initial and final positions. At the saddle point, the two nearest-neighbor O ions are significantly displaced in order to make way for the large U ion and at the same time maintain a favorable local coordination. Displacements are also discernible among other O ions, and their motion is also driven by retaining the U-O coordination along the migration pathway. The migration barrier increases by about 1 eV without the O sublattice distortions. The details of this migration mechanism will be further discussed in a separate study.

The experimental value for the U migration barrier is as low as 2.4 eV. $^{4}$ Yun $et$ $al.^{9,10}$ pointed out that the accuracy of the DFT methodology applied here is usually much better than the level of discrepancy that emerges with respect to the experimental migration data. One way of checking for uncertainties contained in the DFT data is to perform calculations for different exchange-correlation potentials. Consequently, we

![](./images/811635908099964929_3.jpg)

FIG. 2. (Color online) Idealized schematics of U vacancy diffusion mechanisms. (a) The starting position for diffusion of a single $V_U$, (b) $V_{UO}$ clusters, (c) $V_{UO_2}$ clusters and (d) $V_{U_2O}$ clusters. For all figures the arrows indicate the migration pathway and the highlighted (partially colored) ions are displaced significantly from their lattice positions at the saddle point in order to maintain a favorable U-O coordination throughout the migration process. U ions are shown in blue, the migrating ion in turquoise, O ions in grey and vacancies (both $V_U$ and $V_O$) are represented by squares.

also calculated the migration barrier using the Perdew-Burke- Ernzerhof (PBE) parametrization of the GGA potential. $^{70}$ The $U$ and $J$ parameters were set equal to the values for LDA $+U$. The details of these calculations will be presented elsewhere, but in summary, the GGA $+U$ barrier is about 1-1.3 eV lower than for LDA $+U$, which, even though it decreases the gap, cannot be considered to be in good agreement with experiments.

In order to resolve the discrepancies between theory and experiments, Yun *et al.* investigated the effect of binding a $V_O$ to the already existing $V_U$ ($V_{UO}$). $^9$ According to their calculations, the barrier for U diffusion decreases by 0.8-0.9 eV for this cluster compared with an isolated vacancy, which brings the migration barriers closer to the experimental numbers. Our LDA $+U$ calculations predict a similar decrease of 0.75 eV to 4.07 eV for $V_{UO}$. This barrier is still off from the experimental value of 2.4 eV, even though the GGA $+U$ $V_{UO}$ barrier just over 3.4 eV exhibits smaller discrepancy. The $V_{UO}$ migration mechanism involves significant displacement of four of the O ions, i.e., the nearest neighbors at the saddle point [see Fig. 2(b)]. Two of these ions follow in the path of and essentially stay bound to the migrating U ion. The additional $V_O$ allows these ions to largely keep the U-O coordination while the U ion moves toward the saddle point position. This O displacement pattern could not occur for $V_U$, since for this case their motion is blocked by the additional O ion. After passing the saddle point the two O ions following in the path of the migrating U ion first retain their U-O coordination and reach either an interstitial site or the vacant O site before releasing from the U ion and moving back to their original positions. Alternatively, one of the O ions may stay in what was originally the vacant O site, thus resulting in a combined U and O vacancy diffusion mechanism. Since O migration is a low-barrier process the effective U migration barrier should be very similar between these two mechanisms.

In the same way we have calculated the barrier for U migration within $V_{UO_2}$ clusters [see Fig. 2(c)]. The [111] $V_{UO_2}$ cluster exhibits a barrier that is approximately 0.30 eV lower than for $E_m^{V_U}$ (4.51 eV). The barrier for the cluster where the two O vacancies are aligned in [100] directions (measured as the total migration barrier from the gound-state [111] $V_{UO_2}$ configuration) is higher than for the [111] configuration. All the $V_{UO_2}$ barriers refer to a mechanism that includes simultaneous migration of one of the accompanying $V_O$. To recover the original [111] configuration after the initial U migration step, the $V_O$ that is left behind must undergo multiple translations. However, since $V_O$ diffusion is known to be fast and the corresponding barriers are significantly lower than the U barriers, this part of the mechanism will not contribute to the total $V_{UO_2}$ migration barrier.

In conclusion, the experimental U vacancy migration barrier cannot be reproduced by a mechanism involving $V_U$ alone and, moreover, neither $V_{UO}$ nor $V_{UO_2}$ clusters can fully resolve this discrepancy. The experimental barrier of 2.4 eV was derived from recovery analysis of heavily damaged materials. $^5$ Since there is no cost of forming the individual point defects in damaged materials, the measured activation energy would be equal to the migration barrier for the rate limiting step. However, since $V_U$ and $V_O$ are known to form clusters, it is likely that the barrier obtained from damage analysis does not correspond to the true migration barrier of a single $V_U$. We have already concluded that $V_{UO_2}$, $V_{UO}$, and $V_U$ cannot explain the experimental data, even though the $V_{UO}$ barrier from GGA $+U$ is within about 1 eV. To explore this further, we have expanded our study to include $V_{U_2O}$ clusters, consisting of two nearest neighbor $V_U$ and one $V_O$. The corresponding migration pathway involves moving the U ion into the interstitial site situated in between the original vacant cation sites and then advancing this ion farther along to either one of the two $V_U$ [see Fig. 2(d)]. The barrier for this process is predicted to be approximately 2.92 eV, which is in better agreement with experiments. The second $V_U$ enables this mechanism by decreasing the penalty for the migrating U ion to occupy or traverse through the interstitial site. The $V_{U_2O}$ cluster is predicted to be stable with respect to its isolated components [the corresponding binding energies are A (no JT) neutral 3.65 eV, charged 1.87 eV, O-S 1.87 eV; and B (JT), neutral 4.53 eV, charged 2.84 eV, O-S 1.97 eV], which supports the hypothesis that $V_{U_2O}$, or similar clusters, could be responsible for the effective migration barrier measured in damaged $UO_2$ samples. $^5$ Clusters with additional $V_O$ would be expected to exhibit similar migration characteristics. We have also calculated the migration barrier for $V_{U_2}$ clusters (two nearest-neighbor $V_U$) and for this case a barrier of 2.61 eV is obtained, which is very close to the experimental value. From these findings we propose that diffusion in damaged $UO_2$ samples involves clusters of at least two $V_U$, possibly coordinated with additional $V_O$. This mechanism has not

been previously identified. Moreover, we conclude that the commonly accepted barrier for migration of single $V_U$ is not viable and it is probably underestimated by 1.4–2.4 eV.

The A (JT) neutral, charged, and O-S approaches all predict $V_{UO_2}$ to be the active diffusion species for $UO_{2-x}$, $V_{UO}$ for $UO_2$, and $V_U$ for $UO_{2+x}$, even though for $UO_2$ the $V_U$ and $V_{UO}$ activation energies are rather close for the charged and O-S data sets while $V_{UO}$ and $V_{UO_2}$ are close for the neutral data set. For $UO_{2-x}$, $V_{UO}$ is similarly not very far away from the $V_{UO_2}$ activation energy for the O-S and charged data sets. A (no JT) and B (JT) predict different activation energies, but they capture the same physical trends. The competition between $V_U$ and $V_{UO}$ for $UO_2$ is even closer for B (JT) than for A (no JT).

Table V shows that our calculations predict U activation energies that reproduce the same trend as experiments for the full composition range, but at the same time overestimate activation energies by roughly 1 eV for the charged and O-S data sets (the situation is even worse for the neutral data set). We have seen that GGA $+U$ tends to predict migration barriers that are about 1 eV lower than for LDA $+U$ and it is interesting to note that applying the lower GGA $+U$ barrier would improve the agreement with experimental activation energies (the GGA $+U$ and LDA $+U$ defect energies are close, implying that the main difference in estimates of activation energies should come from the barriers). We believe that the decreased barrier for GGA $+U$ could be connected to the difference in equilibrium lattice constant between LDA $+U$ ($\approx$5.45 Å) and GGA $+U$ ($\approx$5.53 Å). This topic will be further discussed in a separate publication. The closest match between modeling and experiments is obtained for the A (no JT) charged and O-S data sets. In principle $V_{U_2}$ clusters could also contribute to diffusion for $UO_{2+x}$. However, applying the most relevant definition of the $V_{U_2}$ binding energy in the $UO_{2+x}$ range we predict slight repulsion (0.1-0.2 eV for the O-S data set) between the defect constituents. We recall that $V_{U_2O}$ is still bound, but the high cost of forming $V_O$ in the $UO_{2+x}$ range rules out any contributions from this cluster. For the same reason the high cost of forming $V_U$ in the $UO_{2-x}$ and $UO_2$ regions precludes $V_{U_2}$ and $V_{U_2O}$ as active diffusion species for these cases. Based on thermodynamic arguments, any contributions from $V_{U_2}$ or $V_{U_2O}$ clusters are thus neglected in this work.

The calculation of migration barriers for $V_{UO}$ and $V_{UO_2}$ involves difficulties due to the existence of local potential energy minima along or close to the migration pathway and the flexible nature of the oxygen sublattice, which complicated reaching sufficient convergence and in some cases gave predictions of very low but inaccurate migration barriers. The barriers reported above refer to calculations that reached (reasonable) convergence and should thus be reliable. Even though some uncertainty may exist for the barriers, we estimate this range to be small enough not to influence our present conclusions. By analyzing results from multiple calculations we estimate that the uncertainty limits are about 0.2–0.3 eV.

### C. Activation energies for Xe diffusion

Xe diffusion is proposed to occur via binding of an additional $V_U$ to the equilibrium Xe trap site, as illustrated in Fig. 1. Our first task is to calculate the saddle point for Xe atoms moving from their original trap site location into the second bound $V_U$. However, any intracluster Xe barrier would contribute to the total Xe activation energy only if it exceeds the barrier associated with $V_U$ migration from one part of the trap site cluster to another. Using nudged elastic band calculations and *ab initio* molecular dynamics simulations we found that the Xe atoms always prefer to occupy the central position of the clusters formed by the original trap site and the second $V_U$. Depending on the local O coordination, slight shifts from this position may occur. The barrier to move from the original vacancy site to the central void location is very small or even nonexistent ($\approx$0 eV), which implies that the intracluster Xe motion is nearly barrierless and, once the second $V_U$ is attached to the trap site, Xe will occupy the central void. The clusters formed by the original Xe trap site and the second bound $V_U$ are associated with rather significant distortions of the surrounding lattice. For $Xe_{U_2}$ (Xe in $V_U$ trap site plus the second bound $V_U$) there are especially large displacements, which effectively push two regular fluorite O ions enclosing the cluster into octahedral interstitial positions. The formation of these defects may be associated with a small barrier; however, other cluster geometries seem to form by barrierless displacements once the second $V_U$ is bound to the original trap site. From the U vacancy migration barriers calculated in Sec. IV B we conclude that the internal Xe migration barriers are always much smaller in magnitude than the $V_U$ barriers and, consequently, the former does not contribute to the Xe activation energy.

For net diffusion to occur, the Xe atom must first move from its original position to the second bound $V_U$, or rather to the central equilibrium site as discussed above, after which the original $V_U$ must either detach from the trap site cluster or jump to a new position within the trap site cluster. In the latter case the $V_U$ becomes available for another migration step by the Xe atom and in the former case a new $V_U$ may bind to the trap site and thus restart the migration process. Intracluster migration of the bound $V_U$ corresponds to co-operative migration of the cluster while separation of the bound $V_U$ from the trap site corresponds to diffusion limited by the kinetics of individual $V_U$. However, this mechanism can be discarded based on the difference in experimental U and Xe activation energies observed in Table V. Below, we come to the same conclusion based on attractive binding energies for the second $V_U$ and the ability of the fluorite lattice to maintain nearest neighbor coordination for the intracluster migration.

The Xe activation energy, $E_a^{Xe}$, is then given by
$$
E_a^{\mathrm{Xe}}=E_F^{V_{\mathrm{U}}}-E_B+E_m^{C, V_{\mathrm{U}}}. \tag{2}
$$

Here, $E_F^{V_U}$ is U vacancy formation energy, $E_B$ is the binding energy of a second $V_U$ to the Xe trap site, and $E_m^{C,V_U}$ is the effective barrier for the intracluster migration of $V_U$. $E_m^{C,V_U}$ is difficult to calculate with DFT methods due to the extended nature of the defects, in particular since the starting, saddle, and finishing positions must all be captured in the same supercell. Nevertheless, the $Xe_{U_2}$ cluster is tractable within the $2 \times 2 \times 3$ supercell and the barrier is estimated to be approximately 3.73 eV from nudged elastic band calculations, which is just over 1 eV lower than the corresponding barrier for $V_U$ diffusion in bulk $UO_2$. The reason for the decreased barrier is similar to that discussed in the context of the diffusion mechanism

<table>
<caption>TABLE V. The total activation energy for U vacancy diffusion ($E_a^{V_U}$) and the total activation energy for Xe diffusion ($E_a^{\text{Xe}}$) as functions of stoichiometry. Note that $E_a^{V_U}$ may correspond to clusters of $V_U$ and other defects as defined in the text. See the caption of Table III for the charged, neutral, and O-S labels. The listed activation energies always refer to the most stable form of U vacancies and Xe trap sites; however, at the $\text{UO}_2$ stoichiometry both the $\text{Xe}_{\text{UO}_2}$ and $\text{Xe}_{\text{UO}}$ activation energies are listed ($\text{Xe}_{\text{UO}}/\text{Xe}_{\text{UO}_2}$) since the Xe solution energy is similar for these two sites (the activation energy for the most stable site according to Table IV is highlighted). The experimental data from Refs. 3–5 are also reproduced.</caption>
<tbody>
<tr>
<td>
</td>
<td>
$E_a^{V_U}$ ($\text{U}_{2-x}$)
</td>
<td>
$E_a^{V_U}$ ($\text{UO}_2$)
</td>
<td>
$E_a^{V_U}$ ($\text{U}_{2+x}$)
</td>
<td>
$E_a^{\text{Xe}}$ ($\text{UO}_{2-x}$)
</td>
<td>
$E_a^{\text{Xe}}$ ($\text{UO}_2$)
</td>
<td>
$E_a^{\text{Xe}}$ ($\text{UO}_{2+x}$)
</td>
</tr>
<tr>
<td>
A (no JT)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Charged
</td>
<td>
8.69
</td>
<td>
7.20
</td>
<td>
4.18
</td>
<td>
7.12
</td>
<td>
6.04/3.80
</td>
<td>
2.97
</td>
</tr>
<tr>
<td>
Charged uncorrected $E_B$
</td>
<td>
</td>
<td>
</td>
</td>
<td>
7.04
</td>
<td>
4.99/3.73
</td>
<td>
2.07
</td>
</tr>
<tr>
<td>
Neutral
</td>
<td>
8.69
</td>
<td>
8.66
</td>
<td>
4.43
</td>
<td>
11.83
</td>
<td>
7.58/6.56
</td>
<td>
4.07
</td>
</tr>
<tr>
<td>
O-S
</td>
<td>
8.69
</td>
<td>
7.57
</td>
<td>
4.43
</td>
<td>
7.80
</td>
<td>
5.43/4.42
</td>
<td>
2.99
</td>
</tr>
<tr>
<td>
B (JT)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Charged
</td>
<td>
9.60
</td>
<td>
8.07
</td>
<td>
3.94
</td>
<td>
7.93
</td>
<td>
6.31/3.67
</td>
<td>
2.81
</td>
</tr>
<tr>
<td>
Charged uncorrected $E_B$
</td>
<td>
</td>
<td>
</td>
</td>
<td>
7.89
</td>
<td>
5.17/3.64
</td>
<td>
1.38
</td>
</tr>
<tr>
<td>
Neutral
</td>
<td>
9.60
</td>
<td>
9.49
</td>
<td>
3.98
</td>
<td>
12.92
</td>
<td>
7.88/6.52
</td>
<td>
2.91
</td>
</tr>
<tr>
<td>
O-S
</td>
<td>
9.60
</td>
<td>
7.81
</td>
<td>
3.74
</td>
<td>
8.25
</td>
<td>
5.18/4.15
</td>
<td>
1.89
</td>
</tr>
<tr>
<td>
Experiments Matzke$^{3-5}$
</td>
<td>
7.8 ($x \leqslant 0.02$),
</td>
<td>
5.6
</td>
<td>
2.6
</td>
<td>
6.0
</td>
<td>
3.9
</td>
<td>
1.7
</td>
</tr>
<tr>
<td>
</td>
<td>
5 ($x \geqslant 0.02$)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

identified for $V_{\text{U}_2}$ and $V_{\text{U}_2\text{O}}$ clusters in Sec. IV B. For $\text{Xe}_{\text{U}_2}$, migration occurs by moving the migrating U ion toward one of the neighboring vacancies by partially traversing via an empty interstitial site at the same time as the Xe atom moves toward the other vacant site in order to create room for the migrating U ion, which gives rise to a slightly curved path compared with bulk $V_{\text{U}}$ migration. This mechanism is enabled by the lower Coulomb repulsion between the migrating U ion and the Xe ion compared with the repulsion between isovalent U ions, which decreases the barrier height when the U ion traverses via the interstitial site. If the Xe ion is replaced by a U ion (as in regular $V_{\text{U}}$ diffusion) the (partial) interstitial path becomes unfavorable due to the short distance and high repulsion between U ions. In this paper we assume that the $\text{Xe}_{\text{U}_2\text{O}}$ and $\text{Xe}_{\text{U}_2\text{O}_2}$ barriers are similar to $\text{Xe}_{\text{U}_2}$, since we were unable to obtain reliable barriers for the two former cases (as mentioned, because of the relatively small cells for these extended defects). We recognize that somewhat lower barriers are possible for trap sites coordinated with $V_{\text{O}}$, but explicit calculation of these is left as future work.

$E_F^{V_U}$ was calculated in Sec. IV A (see Table V) and the calculated $V_{\text{U}}$ binding energies ($E_B$) are listed in Table VI, where the superscripts $\text{Xe}_{\text{U}_2\text{O}_2}$, $\text{Xe}_{\text{U}_2\text{O}}$, and $\text{Xe}_{\text{U}_2}$ denote the type of cluster. The high charge states of the bound complexes, in particular for $\text{Xe}_{\text{U}_2\text{O}}$ and $\text{Xe}_{\text{U}_2}$, imply decreased accuracy for the simplified multipole correction applied here. Additionally, substantial uncertainties arise from the difficulty of finding atoms that are sufficently separated from the localized charges to be used in the potential alignment procedure. For these two reasons we have listed both corrected and uncorrected data for the charged data set. The binding energies for the O-S data were obtained by separating the second $V_{\text{U}}$ from the Xe cluster within the same supercell. $E_B$ increases in the order of $\text{Xe}_{\text{U}_2}$, $\text{Xe}_{\text{U}_2\text{O}}$ and $\text{Xe}_{\text{U}_2\text{O}_2}$. The charged and O-S data predict attractive interactions for all clusters, while the neutral model within approach A (no JT) predicts attractive interactions only for the largest clusters. The neutral model within approach B (JT) predicts attractive binding energies for the full nonstoichiometry range. The present Xe transport model assumes that binding between trap site clusters and the second $V_{\text{U}}$ is attractive, a requirement which is not fulfilled by the neutral data set within approach A (no JT), but confirmed by all other simulation approaches. For the $\text{Xe}_{\text{U}_2\text{O}}$ cluster, the O-S data set agrees better with the uncorrected charged data set than with the corrected one. For $\text{Xe}_{\text{U}_2}$ the O-S data set is approximately in the middle between the uncorrected and corrected data. Due to these uncertainties we believe that corrected charged $E_B^{\text{Xe}_{\text{U}_2\text{O}}}$ and $E_B^{\text{Xe}_{\text{U}_2}}$ values are underestimated. For this reason both the corrected and the uncorrected binding energies will be used in the following analysis. The issue of high charge states is not as severe for $E_B^{\text{Xe}_{\text{U}_2\text{O}_2}}$, as for $E_B^{\text{Xe}_{\text{U}_2\text{O}}}$, and $E_B^{\text{Xe}_{\text{U}_2}}$. For this case the agreement between the corrected, uncorrected, and even O-S data sets is quite good. For both A (no JT) and B (JT) the highest binding energies are predicted by the uncorrected charged data sets.

<table>
<caption>TABLE VI. The binding energy of an additional $V_{\text{U}}$ to Xe atoms that occupy a trivacancy ($E_B^{\text{Xe}_{\text{U}_2\text{O}_2}}$), a divacancy ($E_B^{\text{Xe}_{\text{U}_2\text{O}}}$) or a U vacancy ($E_B^{\text{Xe}_{\text{U}_2}}$). See the caption of Table III and the text for explanation of the charged, neutral, and O-S labels. The charged data set includes both corrected and uncorrected data.</caption>
<tbody>
<tr>
<td>
</td>
<td>
$E_B^{\text{Xe}_{\text{U}_2\text{O}_2}}$
</td>
<td>
$E_B^{\text{Xe}_{\text{U}_2\text{O}}}$
</td>
<td>
$E_B^{\text{Xe}_{\text{U}_2}}$
</td>
</tr>
<tr>
<td>
A (no JT)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Charged
</td>
<td>
2.62
</td>
<td>
0.37
</td>
<td>
0.13
</td>
</tr>
<tr>
<td>
Charged uncorrected
</td>
<td>
2.69
</td>
<td>
1.43
</td>
<td>
1.02
</td>
</tr>
<tr>
<td>
Neutral
</td>
<td>
2.05
</td>
<td>
1.04
</td>
<td>
$-$0.72
</td>
</tr>
<tr>
<td>
O-S
</td>
<td>
2.32
</td>
<td>
1.30
</td>
<td>
0.36
</td>
</tr>
<tr>
<td>
B (JT)
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
Charged
</td>
<td>
3.45
</td>
<td>
0.81
</td>
<td>
0.05
</td>
</tr>
<tr>
<td>
Charged uncorrected
</td>
<td>
3.49
</td>
<td>
1.95
</td>
<td>
1.48
</td>
</tr>
<tr>
<td>
Neutral
</td>
<td>
2.77
</td>
<td>
1.42
</td>
<td>
0.32
</td>
</tr>
<tr>
<td>
O-S
</td>
<td>
2.60
</td>
<td>
1.58
</td>
<td>
0.77
</td>
</tr>
</tbody>
</table>

The total Xe activation energies calculated according to Eq. (2) are summarized in Table V. For each composition range we have assumed that Xe occupies the most stable trap site, though at the $\mathrm{UO}_{2}$ stoichiometry we list activation energies for both $V_{\mathrm{UO}}$ and $V_{\mathrm{UO}_{2}}$ since they are rather close. The most stable case is highlighted in bold. All data sets reproduce the experimental trend for the activation energy as a function of the oxygen nonstoichiometry. The activation energies predicted for the neutral approach are in most cases substantially higher than the experimental activation energies. The charged and O-S activation energies provide better agreement with experiments and among these, approach A (no JT) is closest to the experimental data. However, both data sets still tend to overestimate the activation energy. One explanation for this could be uncertainties for the migration barriers highlighted earlier for $V_{\mathrm{U}}$ by different predictions for LDA $+U$ and GGA $+U$. Similarly, the intracluster barrier $(E_{m}^{C,V_{\mathrm{U}}})$ decreases to about 3.13 eV for GGA $+U$. We speculate that the improved agreement with experiments for the data sets that apply the lower GGA $+U$ migration barriers may be related to thermal expansion occurring at reactor operating conditions, since one distinction between LDA $+U$ and GGA $+U$ is the higher equilibrium lattice parameter for the latter. Clearly, it is also possible that the DFT calculations underestimate binding energies or fail to accurately capture $E_{S}$ or the balance between $E_{S}$ and $E_{F}$. The difference between approach A (no JT) and B (JT) is typically < 1 eV. Further improvement with respect to experiments may be achieved if uncertainties regarding $E_{m}^{C,V_{\mathrm{U}}}$ for $\mathrm{Xe}_{\mathrm{U}_{2}\mathrm{O}}$ and $\mathrm{Xe}_{\mathrm{U}_{2}\mathrm{O}_{2}}$ were accounted for, i.e, the presence of $V_{\mathrm{O}}$ for Xe trap sites at the $\mathrm{UO}_{2-x}$ and $\mathrm{UO}_{2}$ stoichiometries could decrease the barrier and thus also the gap to experimental activation energies.

## V. CONCLUSIONS

Using DFT we have calculated the activation energies for Xe diffusion in $\mathrm{UO}_{2\pm x}$ as well as the closely related activation energies for U diffusion. To reach accurate predictions it is essential to treat the charge compensation for defects in $\mathrm{UO}_{2\pm x}$ in a consistent way. We illustrate how this can be achieved by applying so-called charged supercell calculations. At fixed $\mathrm{UO}_{2}$ stoichiometry the lattice always avoids reduction of $\mathrm{U}^{4+}$ into $\mathrm{U}^{3+}$ ions due to the high thermodynamic cost associated with this reaction, which, for example, implies that there is no explicit $\mathrm{U}^{3+}$-$\mathrm{U}^{5+}$ charge transfer associated with O Frenkel pair formation in $\mathrm{UO}_{2}$. This conclusion was confirmed by calculating the Frenkel defect properties within a single $2\times 2\times 3$ fluorite supercell. Stoichiometry changes and the occurrence of other charge compensating mechanisms that are more energetically costly result in worse agreement with experimental estimates.

Our calculations demonstrate that Xe transport occurs by binding a second $V_{\mathrm{U}}$ to the stable Xe trap sites and these clusters then migrate according to a vacancy mediated mechanism, which occurs due to the fact that the $V_{\mathrm{U}}$ is bound to the Xe trap sites. This implies that Xe diffusion is governed by 1) the U vacancy formation energy 2) the binding energy of vacancies to the Xe trap site, and 3) the barrier for the bound U vacancy to move from one part of the trap site cluster to another. We confirm earlier findings that the stoichiometry-dependent activation energies follow from changes in the Xe trap site solution energy and the U vacancy formation energy as function of the O content. Our predictions slightly overestimate the Xe activation energies in relation to the measured values for the full $\mathrm{UO}_{2\pm x}$ composition range, but the agreement is still rather good. Calculating the U activation energies requires us to consider formation of $V_{\mathrm{UO}_{2}}$ vacancy clusters for $\mathrm{UO}_{2-x}$. The predicted activation energies for U diffusion under thermal equilibrium conditions likewise exhibit some overestimation, while generally being in rather good agreement with available experiments. To explain the low value of 2.4 eV found for U migration from independent damage experiments (not thermal equilibrium) the presence of $V_{\mathrm{U}_{2}}$ or $V_{\mathrm{U}_{2}\mathrm{O}}$ vacancy clusters must be included in the analysis.

## ACKNOWLEDGMENTS

Work at Los Alamos National Laboratory was funded by DOE Nuclear Energy Fuel Cycle Research and Development (FCRD) Campaign, Nuclear Energy Advanced Modeling and Simulation (NEAMS) Program, Fuels Integrated Performance and Safety Code (IPSC) project under the AFCI Modeling and Simulation work package No. LA0915090108. Los Alamos National Laboratory is operated by Los Alamos National Security, LLC, for the National Nuclear Security Administration of the US DOE under Contract No. DE-AC52-06NA25396.

$^{1}$D. R. Olander, Fundamental Aspects of Nuclear Reactor Elements, NTIS, ERDA, 1975.
$^{2}$R. W. Grimes and C. R. A. Catlow, *Philos. Trans. R. Soc. London Ser. A* **335**, 609 (1991).
$^{3}$H. J. Matzke, in *Diffusion Processes in Nuclear Materials*, edited by R. P. Agarwala (North-Holland, Amsterdam, 1992).
$^{4}$H. J. Matzke, *J. Chem. Soc. Faraday Trans. 2* **83**, 1121 (1987).
$^{5}$H. J. Matzke, *Radiat. Eff. Defects Solids* **53**, 219 (1980).
$^{6}$C. R. A. Catlow, *Radiat. Eff. Defects Solids* **53**, 127 (1980).
$^{7}$R. G. J. Ball and R. W. Grimes, *Chem. Soc. Faraday Trans.* **86**, 1257 (1990).

$^{8}$T. Petit, C. Lemaignan, F. Jollet, B. Bigot, A. Pasturel, *Philos. Mag. B* **77**, 779 (1998).
$^{9}$Y. Yun, H. Kim, and K. Park, *J. Nucl. Mater.* **378**, 40 (2007).
$^{10}$Y. Yun, O. Eriksson, P. M. Oppeneer, K. Hanchul, and P. Kwangheon, *J. Nucl. Mater.* **385**, 364 (2009).
$^{11}$P. V. Neri kar, X.-Y. Liu, B. P. Uberuaga, C. R. Stanek, S. R. Phillpot, and S. B. Sinnott, *J. Phys. Condens. Matter* **21**, 435602 (2009).
$^{12}$C. R. A. Catlow, *Proc. R. Soc. London ser. A* **364**, 473 (1978).
$^{13}$C. R. Stanek and R. W. Grimes, *J. Nucl. Mater.* **282**, 265 (2000).

14X.-Y. Liu, B. P. Uberuaga, D. A. Andersson, C. R. Stanek, and K. E. Sickafus, Appl. Phys. Lett. 98, 151902 (2011).

15S. Nicoll, H. J. Matzke, and C. R. A. Catlow, J. Nucl. Mater. 226, 51 (1995).

16C. R. A. Catlow and R. W. Grimes, J. Nucl. Mater. 165, 313 (1989).

17C. R. A. Catlow, J. Chem. Soc. Faraday Trans. 2 83, 1065 (1987).

18R. G. J. Ball and R. W. Grimes, J. Nucl. Mater. 188, 216 (1992).

19M. Freyss, N. Vergnet, and T. Petit, J. Nucl. Mater. 352, 144 (2006).

20H. Y. Geng, Y. Chen, Y. Kaneta, and M. Kinoshita, J. Alloys Compd. 457, 465 (2008).

21D. Schwen, M. Huang, P. Bellon, and R. S. Averback, J. Nucl. Mater. 392, 35 (2009).

22J. Yu, R. Devanathan, and W. J. Weber, J. Phys. Condens. Matter 21, 435401 (2009).

23E. Yakub, C. Ronchi, and D. Staicu, J. Chem. Phys. 127, 094508 (2007).

24H. Y. Geng, Y. Chen, Y. Kaneta, M. Kinoshita, and Q. Wu, Phys. Rev. B 82, 094106 (2010).

25H. J. Matzke, J. Phys. (Paris) 34, 317 (1973).

26H. J. Matzke, Adv. Ceram. 17, 1 (1986).

27H. J. Matzke, Solid State Ionics 12, 25 (1984).

28H. J. Matzke, Nucl. Appl. 2, 131 (1966).

29W. Miekeley and F. W. Felix, J. Nucl. Mater. 42, 297 (1972).

30R. Lindner and H. J. Matzke, Z. Naturforsch. A 14, 582 (1959).

31W. B. Lewis, J. R. Macewan, W. H. Stevens, and R. G. Hert, AECL Report No. AECL-2019 (1964).

32J.-P. Crocombette, J. Nucl. Mater. 305, 29 (2002).

33G. Kresse and J. Hafner, Phys. Rev. B 48, 13115 (1993).

34G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).

35G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

36G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

37P. E. Blöchl, Phys. Rev. B 50, 17953 (1994).

38A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Phys. Rev. B 52, R5467 (1995).

39P. Santini, R. Lmanski, and P. Erdodblacs, Adv. Phys. 48, 537 (1999).

40G. Amoretti, A. Blaise, R. Caciuffo, J. M. Fournier, M. T. Hutchings, R. Osborn, and A. D. Taylor, Phys. Rev. B 40, 1856 (1989).

41S. B. Wilkins, R. Caciuffo, C. Detlefs, J. Rebizant, E. Colineau, F. Wastin, and G. H. Lander, Phys. Rev. B 73, 060406 (2006).

42R. Laskowski, G. K. H. Madsen, P. Blaha, and K. Schwarz, Phys. Rev. B 69, 140408(R) (2004).

43B. Dorado, P. Garcia, G. Carlot, C. Davoisne, M. Fraczkiewicz, B. Pasquet, M. Freyss, C. Valot, G. Baldinozzi, D. Simeone, and M. Bertolus, Phys. Rev. B 83, 035126 (2011).

44B. Dorado, G. Jomard, M. Freyss, and M. Bertolus, Phys. Rev. B 82, 035114 (2010).

45M. Iwasawa, Y. Chen, Y. Kaneta, T. Ohnuma, H.-Y. Geng, and M. Kinoshita., Mater. Trans. 47, 2651 (2006).

46S. L. Dudarev, D. N. Manh, and A. P. Sutton, Philos. Mag. B 75, 613 (1997).

47F. Gupta, G. Brillant, and A. Pasturel, Philos. Mag. 87, 2561 (2007).

48H. Y. Geng, Y. Chen, Y. Kaneta, and M. Kinoshita, Phys. Rev. B 75, 054111 (2007).

49H. Y. Geng, Y. Chen, Y. Kaneta, M. Iwasawa, T. Ohnuma, and M. Kinoshita, Phys. Rev. B 77, 104120 (2008).

50H. Y. Geng, Y. Chen, Y. Kaneta, and M. Kinoshita, Phys. Rev. B 77, 180101 (2008).

51P. Nerikar, T. Watanabe, J. S. Tulenko, S. R. Phillpot, and S. B. Sinnott, J. Nucl. Mater. 348, 61 (2009).

52D. A. Andersson, J. Lezama, B. P. Uberuaga, C. Deo, and S. D. Conradson, Phys. Rev. B 79, 024110 (2009).

53B. Dorado, B. Amadon, M. Freyss, and M. Bertolus, Phys. Rev. B 79, 235125 (2009).

54D. A. Andersson, T. Watanabe, C. Deo, and B. P. Uberuaga, Phys. Rev. B 80, 060101(R) (2009).

55G. Brillant and A. Pasturel, Phys. Rev. B 77, 184110 (2008).

56S. L. Dudarev, M. R. Castell, G. A. Botton, S. Y. Savrasov, C. Muggelberg, G. A. D. Briggs, A. P. Sutton, and D. T. Goddard, Micron 31, 363 (2000).

57T. Yamashita, N. Nitani, T. Tsuji, and H. Inagaki, J. Nucl. Mater. 247, 90 (1997).

58H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188 (1976).

59G. Henkelman, B. P. Uberuaga, and H. Jonsson, J. Chem. Phys. 113, 9901 (2000).

60B. Meredig, A. Thompson, H. A. Hansen, C. Wolverton, and A. van de Walle, Phys. Rev. B 82, 195128 (2010).

61G. Jomard, B. Amadon, F. Bottin, and M. Torrent, Phys. Rev. B 78, 075125 (2008).

62R. Caciuffo, G. Amoretti, P. Santini, G. H. Lander, J. Kulda, and P. deV. DuPlessis, Phys. Rev. B 59, 13892 (1999).

63D. Ippolito, L. Martinelli, and G. Bevilacqua, Phys. Rev. B 71, 064419 (2005).

64E. Blackburn, R. Caciuffo, N. Magnani, P. Santini, P. J. Brown, M. Enderle, and G. H. Lander, Phys. Rev. B 72, 184411 (2005).

65P. Santini, S. Carretta, G. Amoretti, R. Caciuffo, N. Magnani, and G. H. Lander, Rev. Mod. Phys. 81, 807 (2009).

66J.-P. Crocombette, D. Torumba, and A. Chartier, Phys. Rev. B 83, 184107 (2011).

67S. Lany and A. Zunger, Phys. Rev. B 78, 235104 (2008).

68C. Persson, Y.-J. Zhao, S. Lany, and A. Zunger, Phys. Rev. B 72, 035211 (2005).

69R. A. Jackson, A. D. Murray, J. H. Harding, and C. R. A. Catlow, Philos. Mag. 53, 27 (1986).

70J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).