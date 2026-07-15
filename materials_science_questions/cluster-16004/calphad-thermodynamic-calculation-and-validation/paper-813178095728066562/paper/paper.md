P. Waldner, H. Ipser: Thermodynamic modeling of the $Ni-In$ system

Peter Waldner $^{1,3}$, Herbert Ipser $^{2}$

$^{1}$ Institut für Physikalische Chemie, Montanuniversität Leoben, Leoben, Austria
$^{2}$ Institut für Anorganische Chemie, Universität Wien, Wien, Austria
$^{3}$ Currently at Center for Research on Computational Thermochemistry, Ècole Polytechnique de Montréal, Montréal, Canada

# Thermodynamic modeling of the $Ni-In$ system

The complete nickel-indium system was thermodynamically assessed at a total pressure of 1 bar from room temperature up to liquidus temperatures. The Gibbs energies of five condensed solution phases and five stoichiometric compounds were modeled using all available $T-x$ phase diagram and thermodynamic data. For the Ni-rich solid solution with face-centered cubic structure as well as the liquid phase a substitutional approach was chosen to describe the Gibbs energies. Sublattice models were applied to account for the description of the thermodynamics of three nonstoichiometric intermetallic compounds. Three sublattices were chosen according to the crystallographic structures of the $\zeta-Ni_{2} In$ and $\zeta'-Ni_{13} In_{9}$ phases, whereas two sublattices were selected for the $\delta$-NiIn phase. The gas phase was treated as thermodynamically ideal. All computations were carried out with the Gibbs energy minimization program ChemSage and its routine for parameter optimization.

**Keywords:** Nickel; Indium; $Ni-In$ system; Phase diagram: $Ni-In$; Thermodynamic modeling: $Ni-In$

## Thermodynamische Modellierung des Systems $Ni-In$

Das gesamte System Nickel-Indium wurde für einen Gesamtdruck von 1 bar im Temperaturbereich von Raumtemperatur bis zu Liquidustemperaturen thermodynamisch ausgewertet. Die Gibbsschen Energien von fünf kondensierten Mischphasen und fünf stöchiometrischen Verbindungen wurden unter Berücksichtigung sämtlicher vorhandener Temperaturdaten bezüglich des $T-x$-Phasendiagrammes und der thermodynamischen Eigenschaften modelliert. Für die Beschreibung der Gibbsschen Energie des kubisch-flächenzentrierten Ni-reichen Mischkristalles und der flüssigen Phase wurde ein Substitutionsansatz gewählt. Für die Beschreibung der Thermodynamik von drei nichtstöchiometrischen intermetallischen Phasen kamen Untergittermodelle zur Anwendung. Entsprechend den kristallographischen Strukturen wurden für die Phasen $\zeta-Ni_{2} In$ und $\zeta'-Ni_{13} In_{9}$ drei Untergitter ausgewählt und zwei Untergitter für die $\delta$-NiIn-Phase. Die Gasphase wurde als thermodynamisch ideal behandelt. Alle Berechnungen wurden mit dem Gibbsenergie-Minimierungsprogramm ChemSage und dem entsprechenden Unterprogramm zur Parameteroptimierung durchgeführt.

## 1 Introduction

A thermodynamic description of the binary system $Ni-In$ represents an essential contribution to multicomponent databases in the field of electronics. Ni alloys are used as contact materials for III-V semiconductors containing In (like InAs or InSb, e. g.) and also as metallization for soldering contacts which may interact with novel lead-free, In-containing solders. The design and development of such materials can be supported by a better understanding of their phase transformations and microstructures which is itself strongly dependent on a quantitative knowledge of the phase equilibria and of the thermodynamics of all subsystems, like e. g. $Ni-In$. As a consequence, analytical and consistent expressions are needed for the Gibbs energies of all phases in the system.

According to the literature, the system $Ni-In$ contains five condensed solution phases and five stoichiometric intermetallic compounds [88Sin, 90Mas, 97Dur, 99Oka]. The Ni-rich solid solution, $\zeta-Ni_{2} In$, $\zeta'-Ni_{13} In_{9}$, the $\delta$-NiIn phase with a large homogeneity range near the equiatomic composition, and the liquid phase belong to the mixture phases. The line compounds $Ni_{2} In$ and $Ni_{3} In$ on the Ni-rich side, NiIn in the center, and finally $Ni_{2} In_{3}$ and $Ni_{3} In_{7}$ on the In-rich side of the binary system are involved in several invariant equilibria between the melting points of pure Ni and In, i. e., 1455 and $157^{\circ}C$, respectively. Like the $\delta$-NiIn phase, $\zeta-Ni_{2} In$ shows a wide homogeneity range and congruent melting behavior. It is stable between about $470^{\circ}C$ and its congruent melting point of about $950^{\circ}C$, its stability field extends mainly to the In-rich side. In contrast to $\zeta-Ni_{2} In$, the $\delta$-NiIn phase exists only in a rather narrow temperature range of about $150^{\circ}C$, i. e., between about $780^{\circ}C$ and the congruent melting point around $930^{\circ}C$. The deviation from the equiatomic stoichiometry is strongly asymmetric, again to the In-rich side. $\zeta'-Ni_{13} In_{9}$, on the other hand, shows a rather narrow homogeneity range compared to its adjacent intermetallic solution phases.

In a very recent experimental investigation of the Ni-rich part of the $Ni-In$ phase diagram by Norén at al. [00Nor] various ordered superstructures related to the $B8_{2}$ structure of $\zeta-Ni_{2} In$ were observed at lower temperatures, in addition to the two compounds $Ni_{3} In$ and $Ni_{13} In_{9}$. However, the authors were not able to draw clear and unequivocal conclusions from their X-ray and electron diffraction patterns concerning the corresponding phase relationships. Although such ordering phenomena may play a role in $B8_{2}$ phases as the experience from the closely related $B8_{1}$ (NiAs) phases shows [64Kje], we have to rely here on the phase diagram data by [97Dur] until the existence of additional phase transformations is confirmed by further evidence.

A first thermodynamic modeling of the binary system $Ni-In$ was carried out recently by Waldner and Ipser [02Wal] which focused on the thermodynamics of the $B8_{2}$ phase $\zeta-Ni_{2} In$ in the Ni-rich part of the system.

Z. Metallkd. 93 (2002) 8 © Carl Hanser Verlag, München

P. Waldner, H. Ipser: Thermodynamic modeling of the ${\rm Ni-In}$ system

The aim of the present study is to provide the first thermodynamic optimization of the system ${\rm Ni-In}$ over the entire composition range, using the Gibbs energy modeling of the Ni-rich part by [02Wal] as a starting point. All phase equilibria in the system as well as all available thermodynamic properties like activity data, enthalpies of formation, and enthalpies of melting should be reproduced simultaneously in a consistent way.

## 2 Experimental data

The experimental information applied for modeling calculations in this work can be classified into two major groups. One group contains $T-x$ phase diagram data including two sets of data on phase equilibria covering certain temperature ranges and various kinds of information on invariant reactions. The other one includes experimental thermodynamic information, e.g. enthalpies of formation or In activities, both for individual phases and for two-phase regions.

### 2.1 $T-x$ phase diagram data

The modeling calculations in the present study were based on the recent and comprehensive phase diagram study by Durussel et al. [97Dur] and on the earlier review by Singleton and Nash [88Sin]. In addition, the results by Richter [98Ric] concerning the region around the $\delta$-NiIn phase were also included.

Various discrepancies exist among the results of the cited references with respect to specific regions in the phase diagram, e.g. the maximum solubility of In in the Ni solid solution or the equilibrium temperatures of invariant reactions involving the $\delta$-NiIn phase. It will be discussed below which of the literature data lead to a more consistent description of the phase diagram and to a better agreement with the available thermodynamic information.

### 2.2 Thermodynamic data

Bhattacharya and Masson [75Bha,76Bha,77Bha] determined the vapor pressure of In over solid ${\rm Ni-In}$ alloys up to 60 at.% In by an atomic absorption method at 1000 and 1050 K. An effusion method was used by Berezutskii et al. [81Ber] to measure In activities over liquid ${\rm Ni-In}$ alloys at 1248 K. Bienzle and Sommer [91Bie] studied In activities in the composition range of the Ni-rich solid solution between 1080 and 1280 K by an electromotive force (emf) method, and Katayama et al. [01Kat] as well as Schmid et al. [95Sch] used the same method to obtain In activities for liquid and solid alloys at temperatures between about 1000 and 1350 K up to 65 at.% In.

In addition to the activity data, results of calorimetric measurements were also available. Enthalpies of formation of solid ${\rm Ni-In}$ alloys at 298 K were reported by Schmid et al. [95Sch], together with the enthalpies of fusion of the congruently melting phases $\zeta$-Ni₂In and $\delta$-NiIn. Predel and Vogelbein [79Pre] determined enthalpies of formation of solid ${\rm Ni-In}$ alloys at 1060 K by solution calorimetry. Enthalpies of mixing for liquid ${\rm Ni-In}$ alloys were obtained by direct reaction calorimetry at 1750 K by Hayer et al. [93Hay].

## 3 Thermodynamic modeling

The thermodynamic modeling of the Gibbs energies of specific phases in a system consists first of a critical evaluation of the available literature information and leads to an optimization of the corresponding data. In this respect it is obvious that thermodynamic data, such as activities, can aid in the evaluation of the phase diagram, whereas, on the other hand, information on phase equilibria can be used to deduce thermodynamic properties. Thus it is frequently possible to resolve discrepancies in the available data, and all interpolations and extrapolations can be made in a thermodynamically correct manner.

Several semi-empirical models exist which provide analytical expressions of Gibbs energies. In a thermodynamic ‘optimization’ adjustable model parameters are calculated using simultaneously all available thermodynamic and phase equilibrium data in order to obtain one set of model equations describing the Gibbs energy as a function of temperature, pressure, and composition. At the end one has a small set of model parameters which is ideal for storage in a data bank. They can be used to re-calculate all thermodynamic properties as well as an optimized version of the corresponding phase diagram. Furthermore, the model equations for the various phases of interest in binary systems can then be used to predict the properties of multi-component systems containing the respective binaries as subsystems.

In the present work the pressure dependence is of limited importance from a practical and thermodynamic point of view. Consequently, the subsequent discussions of Gibbs energy expressions refer to their temperature and/or composition dependency only.

### 3.1 Gas phase

For the thermodynamic description of the gas phase monoatomic and diatomic In and monoatomic Ni were taken into account: (In, In₂, Ni). Since at a total pressure of 1 bar the gas phase becomes stable only at temperatures above $2000\,^\circ{\rm C}$ an ideal solution model was accepted:
$$
\begin{aligned}
G =& x_{\rm In} G_{\rm In}^0 + x_{\rm In_2} G_{\rm In_2}^0 + x_{\rm Ni} G_{\rm Ni}^0 \\
&+ RT(x_{\rm In} \ln x_{\rm In} + x_{\rm In_2} \ln x_{\rm In_2} + x_{\rm Ni} \ln x_{\rm Ni})
\tag{1}
\end{aligned}
$$
The $G^0$ terms represent the standard Gibbs energies of the corresponding pure gaseous constituents, the ideal entropy of mixing is given by the logarithmic terms; $x_{\rm In}$, $x_{\rm In_2}$, and $x_{\rm Ni}$ are the mole fractions of the species, $R$ is the gas constant, and $T$ is the absolute temperature.

### 3.2 Nickel solid solution and liquid phase

The face-centered cubic (fcc) solid solution of In in Ni forms a substitutional mixture phase. In the same way as for the liquid phase, monoatomic Ni and In are considered as constituents. As a result, the following Gibbs energy expression is applicable for both solution phases:
$$
G = x_{\rm Ni} G_{\rm Ni}^0 + x_{\rm In} G_{\rm In}^0 + RT(x_{\rm Ni} \ln x_{\rm Ni} + x_{\rm In} \ln x_{\rm In}) + G_{\rm m}^{\rm ex}
\tag{2}
$$
where $G_{\rm Ni}^0$ and $G_{\rm In}^0$ are the standard Gibbs energies of the corresponding pure solid or liquid metals, and the logarith-

826
Z. Metallkd. 93 (2002) 8

mic terms represent the entropy of ideal mixing of Ni and In constituents in the solid or liquid mixture phase; $G_{\mathrm{m}}^{\mathrm{ex}}$ is the excess Gibbs energy. The excess Gibbs energy describes first-order interaction energies between Ni and In atoms as a function of temperature and composition. A Redlich-Kister-type expression gives the corresponding composition dependence:

$$
G^{\mathrm{ex}}=x_{\mathrm{Ni}}\left(1-x_{\mathrm{Ni}}\right) \sum_{i=1,2..} L_{i}(T)\left(1-2 x_{\mathrm{Ni}}\right)^{i-1} \tag{3}
$$

where the $L_{i}$ terms are temperature dependent parameters of the series expansion.

### 3.3 The $\zeta$-Ni₂In and the $\zeta'$-Ni₁₃In₉ phase

The crystal structure of the $\zeta$-Ni₂In phase is of the B8₂ type (Pearson symbol $h P 6$, space group $P 6_{3} / m m c$) as reported in [91Vil] and confirmed by [00Nor]. The In atoms form a hexagonal close-packed (hcp) arrangement where the octahedral and the so-called trigonal-bipyramidal (double-tetrahedral) positions are occupied by Ni atoms. As a result three sublattices, two for the Ni atoms and one for the In atoms, can be distinguished in the crystal lattice: $(\mathrm{Ni}, \mathrm{Va})_{1}(\mathrm{Ni})_{1}(\mathrm{In}$, $\mathrm{Ni})_{1}$. The first sublattice (I), the trigonal-bipyramidal positions, contains Ni atoms and vacancies (Va) to take into account the deviation from the exact Ni₂In stoichiometry to the In-rich side. The second sublattice (II) represents the octahedral positions and is assumed to be completely filled with Ni atoms forming a hexagonal primitive arrangement. The third sublattice (III) models the close packed hexagonal array of the In atoms; it is assumed that they can be substituted by Ni atoms to some degree in order to account for the deviation to the Ni-rich side. For more details about the thermodynamic model for the $\zeta$-Ni₂In Phase the reader is referred to the study by Waldner and Ipser [02Wal].

Very recently Norén et al. reported the occurrence of ordering effects in the B8₂ lattice of the $\zeta$ phase which lead to new low-temperature superstructure phases [00Nor]. However, the authors were not able to establish reliable phase relationships nor did they relate their findings to the experimental phase diagram data by Durussel et al. [97Dur]. Although such ordering phenomena cannot be completely excluded as the experience with the various superstructures in B8₁ phases shows [64Kje] it appears that the experimental evidence by [00Nor] is not strong enough to completely change the well-established phase diagram in this composition range. Therefore, no attempts will be made to involve these ordering phases but we will rely on the basic features of the Ni-In phase diagram by [97Dur].

For the analytical description of the discussed sublattice approach for $\zeta$-Ni₂In the compound energy formalism derived by Hillert and Staffansson [70Hil] and generalized by Sundman and Ågren [81Sun] was chosen; it yields the following expression for the Gibbs energy of the B8₂ phase:

$$
\begin{aligned}
G= & y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{In}_{(\mathrm{III})}} G_{\mathrm{NiNiIn}}^{0}+y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{Ni}_{(\mathrm{III})}} G_{\mathrm{NiNiNi}}^{0} \\
& +y_{\mathrm{Va}_{(\mathrm{I})}} y_{\mathrm{In}_{(\mathrm{III})}} G_{\mathrm{VaNiIn}}^{0}+y_{\mathrm{Va}_{(\mathrm{I})}} y_{\mathrm{Ni}_{(\mathrm{III})}} G_{\mathrm{VaNiNi}}^{0} \\
& +R T\left(y_{\mathrm{Ni}_{(\mathrm{I})}} \ln y_{\mathrm{Ni}_{(\mathrm{I})}}+y_{\mathrm{Va}_{(\mathrm{I})}} \ln y_{\mathrm{Va}_{(\mathrm{I})}}\right) \\
& +R T\left(y_{\mathrm{In}_{(\mathrm{III})}} \ln y_{\mathrm{In}_{(\mathrm{III})}}+y_{\mathrm{Ni}_{(\mathrm{III})}} \ln y_{\mathrm{Ni}_{(\mathrm{III})}}\right)+G^{\mathrm{ex}}
\end{aligned} \tag{4}
$$

The first four terms contain the standard Gibbs energies of all possible compounds formed by the sublattice constituents; they are followed by two entropy expressions according to the mixing on each of the two sublattices, I and III. The excess Gibbs energy expression is written separately in terms of all binary excess parameters $L_{\left(j_{1}, j_{2}: i: k\right)}$ and $L_{\left(j: i: k_{1}, k_{2}\right)}$.

$$
\begin{aligned}
G^{\mathrm{ex}}= & y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{Va}_{(\mathrm{I})}} L_{(\mathrm{Ni}, \mathrm{Va}: \mathrm{Ni}: \mathrm{In})}+y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{Va}_{(\mathrm{I})}} L_{(\mathrm{Ni}, \mathrm{Va}: \mathrm{Ni}: \mathrm{Ni})} \\
& +y_{\mathrm{In}_{(\mathrm{III})}} y_{\mathrm{Ni}_{(\mathrm{III})}} L_{(\mathrm{Ni}: \mathrm{Ni}: \mathrm{In}, \mathrm{Ni})}+y_{\mathrm{In}_{(\mathrm{III})}} y_{\mathrm{Ni}_{(\mathrm{III})}} L_{(\mathrm{Va}: \mathrm{Ni}: \mathrm{In}, \mathrm{Ni})}
\end{aligned} \tag{5}
$$

Each of the $L$ parameters can be temperature and composition dependent. For an analytical description of their composition dependence a Redlich-Kister expression is applied, for example:

$$
L_{\left(j_{1}, j_{2}: i: k\right)}(T)=\sum_{n=0} n L_{\left(j_{1}, j_{2}: i: k\right)}(T)\left(y_{j_{1}}-y_{j_{2}}\right)^{n} \tag{6}
$$

Ellner et al. [69Ell] reported the $\zeta'$-Ni₁₃In₉ phase with a small deviation from stoichiometry around the composition Ni₁₃In₉ to be a filled variant of the hexagonal B8₁-(NiAs-) structure. Since the B8₂ structure can be derived from the B8₁ structure by gradually filling the vacancies in the trigonal-bipyramidal interstices by Ni atoms, the following sublattice approach, similar to the one for B8₂-type $\zeta$-Ni₂In, was accepted: $(\mathrm{Ni}, \mathrm{Va})_{1}(\mathrm{Ni})_{1}(\mathrm{In})_{1}$. Consequently, the Gibbs energy of $\zeta'$-Ni₁₃In₉ can be expressed in an analogous manner to Eqs. (4)-(6), reduced to the corresponding contributions of sublattice (I).

### 3.4 The $\delta$-NiIn phase

The $\delta$-NiIn phase with a considerable homogeneity range in the $T-x$ phase diagram [88Sin, 90Mas, 97Dur, 98Ric, 99Oka] is characterized by a B2-type structure. This structure can be considered to consist of two interpenetrating primitive cubic sublattices, in the case of $\delta$-NiIn one for the Ni atoms, sublattice I, and the other one, sublattice II, for the In atoms. Phases of the B2 type can show two kinds of defect mechanisms [82Cha], i. e., the substitutional mechanism (where nonstoichiometry is caused by substitutional defects on either sublattice) and the so-called triple-defect mechanism. In the latter case which usually occurs in intermetallic compounds consisting of a transition metal and a metal of group 13 of the periodic table, deviation to the transition metal-rich side of stoichiometry is mainly caused by substitution whereas deviation to the other side is due to vacancies on the transition metal sublattice. Although no specific information is available on the predominant defects in $\delta$-NiIn, it was assumed that it is of the triple-defect type like NiAl and NiGa [82Cha]. Consequently, the following two-sublattice approach was accepted: $(\mathrm{Ni}, \mathrm{Va})_{1}(\mathrm{In}, \mathrm{Ni})_{1}$. Sublattice I allows vacancies on regular Ni positions whereas sublattice II provides the possibility of anti-structural Ni atoms on regular In sites. It should be pointed out that this approach is compatible with the descriptions of the B2 phase in the system Ni-Al by Ansara et al. [97Ans] and Huang and Chang [98Hua].

Applying again the compound energy formalism [70Hil, 81Sun], the following analytical description of the Gibbs

energy of the $\delta$-NiIn phase is obtained:

$$
\begin{aligned}
G= & y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{In}_{(\mathrm{II})}} G_{\mathrm{NiIn}}^{0}+y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{Ni}_{(\mathrm{II})}} G_{\mathrm{NiNi}}^{0}+y_{\mathrm{Va}_{(\mathrm{I})}} y_{\mathrm{In}_{(\mathrm{II})}} G_{\mathrm{Valn}}^{0} \\
& +y_{\mathrm{Va}_{(\mathrm{I})}} y_{\mathrm{Ni}_{(\mathrm{II})}} G_{\mathrm{VaNi}}^{0}+R T\left(y_{\mathrm{Ni}_{(\mathrm{I})}} \ln y_{\mathrm{Ni}_{(\mathrm{I})}}+y_{\mathrm{Va}_{(\mathrm{I})}} \ln y_{\mathrm{Va}_{(\mathrm{I})}}\right) \\
& +R T\left(y_{\mathrm{In}_{(\mathrm{II})}} \ln y_{\mathrm{In}_{(\mathrm{II})}}+y_{\mathrm{Ni}_{(\mathrm{II})}} \ln y_{\mathrm{Ni}_{(\mathrm{II})}}\right)+G^{\mathrm{ex}}
\end{aligned}
\tag{7}
$$

According to the chosen sublattice approach four terms containing the standard Gibbs energies of the four model compounds and two entropy expressions have to be distin- guished. The excess Gibbs energy may contain temperature and composition dependent interaction parameters between regular and defect species describing second-order interac- tions between regular nickel and vacancies (defect constitu- ent) on the first sublattice (I) and regular In and substitu-tional Ni (defect constituent) on the second sublattice (II):

$$
\begin{aligned}
G^{\mathrm{ex}}= & y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{Va}_{(\mathrm{I})}} L_{(\mathrm{Ni}, \mathrm{Va}: \mathrm{In})}+y_{\mathrm{Ni}_{(\mathrm{I})}} y_{\mathrm{Va}_{(\mathrm{I})}} L_{(\mathrm{Ni}, \mathrm{Va}: \mathrm{Ni})} \\
& +y_{\mathrm{In}_{(\mathrm{II})}} y_{\mathrm{Ni}_{(\mathrm{II})}} L_{(\mathrm{Ni}: \mathrm{In}, \mathrm{Ni})}+y_{\mathrm{In}_{(\mathrm{II})}} y_{\mathrm{Ni}_{(\mathrm{II})}} L_{(\mathrm{Va}: \mathrm{In}, \mathrm{Ni})}
\end{aligned}
\tag{8}
$$

A Redlich-Kister type expression is applied to describethe composition dependence of the interaction parameters;it is given for $L_{(j_{1} j_{2}: k)}$ as an example by Eq. (9):

$$
L_{\left(j_{1} j_{2}: k\right)}(T)=\sum_{n=0}{ }^{n} L_{\left(j_{1} j_{2}: k\right)}(T)\left(y_{j_{1}}-y_{j_{2}}\right)^{n}
\tag{9}
$$

### 3.5 Stoichiometric compounds
According to the phase diagram information by [88Sin,90Mas, 97Dur, 99Oka] five solid phases of the title system are treated as line compounds in this study: $Ni_{3} In, Ni_{2} In$ , $NiIn, Ni_{2} In_{3}$ and $Ni_{3} In_{7}$ . Consequently, the Gibbs energy function of these stoichiometric compounds is temperaturedependent only:

$$
G=\Delta_{\mathrm{f}} H_{298}+\int_{298}^{T} c_{p} \mathrm{~d} T-T\left[S_{298}+\int_{298}^{T}\left(c_{p} / T\right) \mathrm{d} T\right] \quad(10)
$$

where $\Delta_{f} H_{298}$ and $S_{298}$ are the enthalpy of formation and the entropy at 298 K, and $c_{p}$ is the heat capacity at constant pressure.

## 4 Results and discussion
### 4.1 Optimized model quantities
The optimization computations were carried out with the Gibbs energy minimization software ChemSage (Eriksson and Hack [90Eri]) and its routine for parameter optimiza- tion (Königsberger and Eriksson [95Kön]). Standard Gibbs energy values for pure Ni and In in the corresponding gas- eous, liquid and solid states were taken from the SGTE(Scientific Group Thermodata Europe) unary database for pure elements, compiled by Dinsdale [91Din] for the con- densed states. All optimized model quantities are presented in Tables 1-5. As they originate from computations, at least two digits are given after the decimal point for enthalpy numbers and four digits for entropy numbers in order to en- able the reader to precisely reproduce all the data presented in the tables and figures of this paper.

Table 1 gives the calculated excess Gibbs energy para- meters in Eq. (3) for the fcc Ni solid solution and the liquid phase. The fcc Ni solid solution is described by a regular model whereas the liquid phase shows a more complicated deviation from thermodynamically ideal behavior de- scribed by four interaction parameters, three of them tem- perature dependent.

The sublattice model for the description of the $\zeta-Ni_{2} In$  phase by Eq. (4) defines four compounds which are $Ni_{2} In(\zeta), Ni_{3}(\zeta), NiIn(\zeta)$ and $Ni_{2}(\zeta)$ . The heat capacity func tion of $Ni_{2} In(\zeta)$ was estimated from the heat capacity func tion of pure solid In in its standard state and pure nonmag- netic fcc Ni [91Din] by applying Neumann-Kopp's rule. Those of $Ni_{3}(\zeta)$ and $Ni_{2}(\zeta)$ were determined calculating three and two times the quantities of pure nonmagnetic fcc Ni [91Din]. For the heat capacity function of $NiIn(\zeta)$ it was assumed to be an advantageous alternative to Neu- mann-Kopp's rule to use the heat capacity function of the real stoichiometric compound NiIn experimentally deter- mined by Perring et al. [99Per]. To simplify the optimiza- tion procedure, the quantities $\Delta_{f} H_{298}$ and $S_{298}$ of the two hy pothetical compounds $Ni_{3}(\zeta)$ and $Ni_{2}(\zeta)$ were linked by the constraints

$$
\begin{aligned}
& \Delta_{\mathrm{f}} H_{298}\left(\mathrm{Ni}_{3}(\zeta)\right)=1.5 \Delta_{\mathrm{f}} H_{298}\left(\mathrm{Ni}_{2}(\zeta)\right) \quad \text { and } \\
& S_{298}\left(\mathrm{Ni}_{3}(\zeta)\right)=1.5 S_{298}\left(\mathrm{Ni}_{2}(\zeta)\right).
\end{aligned}
$$

Since all four compounds are hypothetical their enthalpies of formation at $298 ~K, \Delta_{f} H_{298}$ , and the corresponding entro pies, $S_{298}$ , were used together with the interaction param eters of Eq. (5) for the optimization computations. It was found that two interaction parameters of Eq. (5), i.e., $L_{(Ni, Va: Ni: In)}$ and $L_{(Ni: Ni: In, Ni)}$ , were sufficient to model the corresponding experimental data related to the $\zeta-Ni_{2} In$  phase [02Wal].

According to the selected sublattice approach for the $\zeta'$  $Ni_{13} In_{9}$ phase the number of the model compounds reduces to two which are $Ni_{2} In(\zeta^{\prime})$ and $NiIn(\zeta^{\prime})$ . The heat capacities of both compounds (which are also hypothetical) were fixed in the same way as discussed for the corresponding compounds of the $\zeta-Ni_{2}$ In phase. It was possible to describe the Gibbs energy of the $\zeta'$ -phase as ideal in terms of the ap plied thermodynamic model as no $L_{(j_{1} j_{2}: i: k)}$ parameters were needed. Tables 2 and 3 contain all optimized model parameters for the phases $\zeta-Ni_{2} In$ and $\zeta'-Ni_{13} In_{9}$ , respec tively.

Using Eq. (7) in order to model the thermodynamics of the $\delta$ -NiIn phase, four model 'compounds' with B2 struc ture have to be distinguished: $NiIn(\delta), Ni_{2}(\delta), In(\delta)$ and $Ni(\delta)$ . The first one represents ideally ordered NiIn withB2 structure. According to the crystallography of the B2

<table>
<caption>Table 1. Optimized excess Gibbs energy quantities of the fcc nickel solid solution and of the liquid phase (in $J mol^{-1}$).</caption>
<tbody>
<tr>
<td>fcc solid solution</td>
<td>$L_{1}=-26062.75+15.25921T$</td>
</tr>
<tr>
<td rowspan="4">liquid phase</td>
<td>$L_{1}=-43340.31+17.42413T$</td>
</tr>
<tr>
<td>$L_{2}=+19273.70-8.30913T$</td>
</tr>
<tr>
<td>$L_{3}=+3079.330-17.52576T$</td>
</tr>
<tr>
<td>$L_{4}=-15351.06$</td>
</tr>
</tbody>
</table>

Table 2. Optimized thermodynamic model quantities of the $\zeta$-
Ni₂In phase according to the applied sublattice model.

<table>
 <thead>
  <tr>
   <th>Model compound</th>
   <th>$\Delta_{f}H_{298}$/J mol⁻¹</th>
   <th>$S_{298}$/J (K mol)⁻¹</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Ni₂In($\zeta$)</td>
   <td>$- 48941.100$</td>
   <td>102.66890</td>
  </tr>
  <tr>
   <td>Ni₃($\zeta$)</td>
   <td>$+ 52691.985$</td>
   <td>97.453755</td>
  </tr>
  <tr>
   <td>NiIn($\zeta$)</td>
   <td>$- 26602.840$</td>
   <td>89.735680</td>
  </tr>
  <tr>
   <td>Ni₂($\zeta$)</td>
   <td>$+ 35127.990$</td>
   <td>64.969170</td>
  </tr>
  <tr>
   <td colspan="3">Excess Gibbs energy quantities/J mol⁻¹:
<br>
$^{0}L_{(\text{Ni,Va:Ni:In})} = - 22151.50 + 30.32828\ T$
<br>
$^{0}L_{(\text{Ni:Ni:In,Ni})} = - 34625.91$</td>
  </tr>
 </tbody>
</table>

Table 3. Optimized thermodynamic model quantities of the $\zeta'$-
Ni₁₃In₉ phase according to the applied sublattice model.

<table>
 <thead>
  <tr>
   <th>Model compound</th>
   <th>$\Delta_{f}H_{298}$/J mol⁻¹</th>
   <th>$S_{298}/$ J (K mol)⁻¹</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Ni₂In($\zeta'$)</td>
   <td>$- 49101.60$</td>
   <td>97.89880</td>
  </tr>
  <tr>
   <td>NiIn($\zeta'$)</td>
   <td>$- 45011.73$</td>
   <td>72.46804</td>
  </tr>
 </tbody>
</table>

structure the second one can be interpreted as pure Ni hy-
pothetically crystallizing in a body-centered cubic (bcc)
structure whereas the third and fourth ones are pure In and
Ni, both occurring hypothetically in a cubic primitive struc-
ture. Consequently, $\Delta_{f}H_{298}$, $S_{298}$ and the heat capacity func-
tion of Ni₂($\delta$) were fixed calculating twice the quantities of
pure bcc Ni [91Din]. The thermodynamic data for Ni($\delta$) to-
gether with the interaction parameter $L_{(\text{Ni,Va:Ni})}$ in Eq. (8)
were taken from Ansara et al. [97Ans] for reasons of com-
patibility with his modeling of the B2 phase in the system
Ni–Al. As the present work deals for the first time with
pure hypothetical In solved in a phase with B2 structure it
was necessary to model the Gibbs energy of In($\delta$). The heat
capacity function of In($\delta$) was estimated from the heat capa-
city function of pure solid In in its standard state [91Din]. In
analogy to the case of NiIn($\zeta$) discussed above the heat ca-
pacity function of NiIn($\delta$) was fixed on the basis of the heat
capacity function of the real stoichiometric compound NiIn
determined experimentally by Perring et al. [99Per]. The
quantities $\Delta_{f}H_{298}$ and $S_{298}$ of In($\delta$) and NiIn($\delta$) were ad-
justed during the optimization process simulta-
neously with one interaction parameter of Eq. (8),
i. e. $L_{(\text{Ni,Va:In})}$. This parameter describing the interac-
tion between Ni and vacancies on the first sublattice
(I), when the second sublattice (II) is occupied by
In, turned out to be highly effective. Table 4 shows
all quantities for $\delta$-NiIn that were modeled in the
present work.

It was necessary to include the Gibbs energies of
the five stoichiometric compounds Ni₃In, Ni₂In,
NiIn, Ni₂In₃ and Ni₃In₇ into the optimization proce-
dure since experimental enthalpies of formation at
298 K show considerable scatter and, additionally,
thermodynamic data for the entropies at 298 K and
heat capacities (except for the NiIn compound) are
missing completely. The heat capacity function of
NiIn was taken from the paper of Perring et al.
[99Per] whereas the heat capacity functions for the
remaining four compounds were estimated in the
same way as discussed for the compounds of the
$\zeta$-Ni₂In phase, i. e. by applying Neumann-Kopp’s rule. Ta-
ble 5 gives all modeled values of the five phases that were
treated as stoichiometric compounds in this work.

Table 4. Optimized thermodynamic model quantities of the
$\delta$-NiIn phase according to the applied sublattice model.

<table>
 <thead>
  <tr>
   <th>model compound</th>
   <th>$\Delta_{f}H_{298}$/J mol⁻¹</th>
   <th>$S_{298}$/J (K mol)⁻¹</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>NiIn($\delta$)</td>
   <td>$- 33476.49$</td>
   <td>85.13860</td>
  </tr>
  <tr>
   <td>In($\delta$)</td>
   <td>$+ 43036.36$</td>
   <td>80.69493</td>
  </tr>
  <tr>
   <td colspan="3">Excess Gibbs energy quantities/J mol⁻¹:
<br>
$^{0}L_{(\text{Ni,Va:In})} = - 73393.66 + 37.13719\ T$
<br>
$^{1}L_{(\text{Ni,Va:In})} = - 45496.26 + 59.16134\ T$</td>
  </tr>
 </tbody>
</table>

Table 5. Optimized thermodynamic model quantities of the stoi-
chiometric compounds in the system nickel-indium.

<table>
 <thead>
  <tr>
   <th>compound</th>
   <th>$\Delta_{f}H_{298}$/J mol⁻¹</th>
   <th>$S_{298}$/J (K mol)⁻¹</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Ni₃In</td>
   <td>$- 52465.65$</td>
   <td>133.96930</td>
  </tr>
  <tr>
   <td>Ni₂In</td>
   <td>$- 49142.61$</td>
   <td>104.61740</td>
  </tr>
  <tr>
   <td>NiIn</td>
   <td>$- 45061.60$</td>
   <td>76.105440</td>
  </tr>
  <tr>
   <td>Ni₂In₃</td>
   <td>$- 128013.40$</td>
   <td>176.00760</td>
  </tr>
  <tr>
   <td>Ni₃In₇</td>
   <td>$- 197514.60$</td>
   <td>407.88330</td>
  </tr>
 </tbody>
</table>

### 4.2 Comparison between calculation and experimental
data

Figure 1 shows the $T$-$x$ phase diagram of the Ni–In system
at a total pressure of 1 bar calculated on the basis of the op-
timized Gibbs energies of all phases in the system. It can be
seen that the agreement with the experimental results of the
most recent phase diagram investigations by Durussel et al.
[97Dur] and Richter [98Ric] is very satisfactory. Table 6
contains the temperatures of all invariant equilibria as well
as the compositions of the involved phases, as calculated
in the present work, in comparison with experimental data
by [97Dur] and [98Ric] and assessed values from [88Sin].
For the majority of the data it is observed that the agreement
with at least one of the quoted experimental sources is very
good.

![](./images/813178095728066562_1.jpg)

Fig. 1. Calculated Ni–In phase diagram at a total pressure of 1 bar together
with experimental data by [97Dur] and [98Ric].

P. Waldner, H. Ipser: Thermodynamic modeling of the Ni−In system

Table 6. Comparison of the calculated invariant equilibria with experimental (Durussel et al. [97Dur], Richter [98Ric]) and assessed values (Singleton and Nash [88Sin]); s = solid.

<table><tbody><tr><td>Invariant equilibrium</td><td>Temperature, °C</td><td colspan="3">Composition, at% In</td><td>Ref.</td></tr><tr><td>Ni(s)/ liquid</td><td>1455
1455
1455.1</td><td>0.0
0.0
0.0</td><td>0.0
0.0
0.0</td><td></td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>fcc-(Ni)/ liquid/ζ</td><td>910
908 ± 2
909.7</td><td>14.5
9.5 ± 0.5
7.9</td><td>26.5
25 ± 0.7
25.0</td><td>31.0
31.2 ± 0.5
31.4</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>fcc-(Ni)/ Ni₃In/ζ</td><td>848
845 ± 2
845.0</td><td>10.0
7.0 ± 0.5
6.9</td><td>24.5
25 ± 0.5
25.0</td><td>31.0
31.2 ± 0.5
31.6</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>Ni₃In/ Ni₂In/ζ</td><td>665
665 ± 2
665.0</td><td>25.5
25 ± 0.7
25.0</td><td>33.3
32.5 ± 0.5
33.3</td><td>33.5
33.5 ± 0.5
33.4</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>Ni₂In/ ζ/ζ'</td><td>482
470 ± 2
472.6</td><td>33.5
32.5 ± 0.5
33.3</td><td>37.0
34 ± 0.5
35.3</td><td>38.5
39.0
40.9</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>ζ/liquid/ δ</td><td>918
908 ± 2
923.8</td><td>41.5
42 ± 0.5
41.7</td><td>46.6
48.5 ± 0.5
48.7</td><td>51.5
49.5 ± 0.5
51.2</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>ζ/ζ'/δ</td><td>876
853 ± 3
870
868.7</td><td>41.0
41 ± 0.5
41
41.0</td><td>42.2
42.0 ± 0.5
42.0
42.4</td><td>52.0
52.7 ± 0.5
51.0
51.6</td><td>[88Sin]
[97Dur]
[98Ric]
calc.</td></tr><tr><td>ζ'/NiIn/ δ</td><td>860
845 ± 3
862.8</td><td>42.0
42.0
42.4</td><td>49.5
50.5 ± 0.5
50.0</td><td>53.0
53.3 ± 0.5
51.8</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>ζ/liquid</td><td>950 ± 2
946.6</td><td>36.0 ± 0.5
35.6</td><td>36.0 ± 0.5
35.6</td><td></td><td>[97Dur]
calc.</td></tr><tr><td>δ/liquid</td><td>930 ± 2
925 ± 5
926.2</td><td>55.0 ± 0.5
54.5
55.0</td><td>55.0 ± 0.5
54.5
55.0</td><td></td><td>[97Dur]
[98Ric]
calc.</td></tr><tr><td>NiIn/δ/ Ni₂In₃</td><td>770
779 ± 2
785
776.4</td><td>50.5
50 ± 0.5
50
50.0</td><td>56.0
55.4 ± 0.5
55.5
55.8</td><td>59.0
60.5 ± 0.5
60.0
60.0</td><td>[88Sin]
[97Dur]
[98Ric]
calc.</td></tr><tr><td>δ/Ni₂In₃/ liquid</td><td>870
865 ± 2
868.9</td><td>58.9
58.8 ± 0.5
59.4</td><td>60.0
60.0 ± 0.5
60.0</td><td>69.8
70.0 ± 2
76.1</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>Ni₂In₃/ Ni₃In₇/ liquid</td><td>409
404 ± 2
404.2</td><td>60.0
60.0 ± 0.5
60.0</td><td>70.0
70.0 ± 0.5
70.0</td><td>96.5
95.0
96.3</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>Ni₃In₇/ liquid/ In(s)</td><td>156.5
156 ± 1
156.3</td><td>70.5
70.0 ± 0.5
70.0</td><td>100.0
100.0
99.9</td><td>100.0
100.0
100.0</td><td>[88Sin]
[97Dur]
calc.</td></tr><tr><td>In(s)/ liquid</td><td>156.6
156.63
156.6</td><td>100.0
100.0
100.0</td><td>100.0
100.0
100.0</td><td></td><td>[88Sin]
[97Dur]
calc.</td></tr></tbody></table>

It should be mentioned that this modeling results in a maximum solubility of 7.9 at.% In in the solid Ni solution which is closer to the data by [97Dur] than to [88Sin] (compare the eutectic equilibrium [fcc (Ni)/liquid/ζ]). Furthermore, it should be pointed out that the calculated In content of the liquid phase involved in the peritectic reaction [δ/Ni₂In₃/liquid] is shifted to a considerably higher value compared to the experimental results. However, this is accepted in view of the consistency with the experimental thermodynamic data for the liquid phase discussed below. Any attempt to shift the composition of the the liquid phase to lower indium contents results in a loss of the good agreement with adjacent phase equilibria and thermodynamic data.

Figs. 2−4 demonstrate that the modeled Gibbs energy functions of the Ni solid solution, the liquid phase and the ζ-Ni₂In phase are also able to reproduce very well the experimental In partial pressure data. For the fcc (Ni) phase, the calculated line in Fig. 2 is closer to the results of Bhattacharya and Masson [75Bha] than to those of Bienzle and Sommer [91Bie]. Fig. 3 demonstrates very good agreement between calculated In partial pressures and experimental values by Schmid et al. [95Sch] and Berezutskii et al. [81Ber] for the liquid phase, and Fig. 4 gives a similar comparison for the ζ-Ni₂In phase with experimental data by Bhattacharya and Masson [76Bha], Schmid et al. [95Sch], and Katayama [01Kat]. In addition, Table 7 provides a comparison for various two-phase regions between calculated and experimental In partial pressures at 1000 K determined by Bhattacharya and Masson [77Bha] and Schmid et al. [95Sch]; again the agreement is very satisfactory.

![](./images/813178095728066562_2.jpg)

Fig. 2. Experimental and calculated partial pressures of In in the fcc Ni solid solution.

![](./images/813178095728066562_3.jpg)

Fig. 3. Experimental and calculated partial pressures of In in the liquid phase.

Z. Metallkd. 93 (2002) 8

![](./images/813178095728066562_4.jpg)

Fig. 4. Experimental and calculated partial pressures of In in the $\zeta$-Ni₂In phase at 1000 K.

<table>
<caption>Table 7. Experimental and calculated values of In partial pressures in different two-phase regions at 1000 K.</caption>
<thead>
<tr>
<th>Two-phase region</th>
<th>$\log(p_{\text{In}}/\text{bar})$</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\zeta/\zeta'$</td>
<td>$-7.787$<br>$-7.941$</td>
<td>[95Sch]<br>calc.</td>
</tr>
<tr>
<td>$\zeta'/\text{NiIn}$</td>
<td>$-7.759$<br>$-7.801$</td>
<td>[95Sch]<br>calc.</td>
</tr>
<tr>
<td>$\text{NiIn/Ni}_2\text{In}_3$</td>
<td>$-7.484$<br>$-7.295$<br>$-7.415$</td>
<td>[95Sch]<br>[77Bha]<br>calc.</td>
</tr>
<tr>
<td>$\text{Ni}_2\text{In}_3/\text{liquid}$</td>
<td>$-7.082$<br>$-7.053$</td>
<td>[95Sch]<br>calc.</td>
</tr>
</tbody>
</table>

Finally, a comparison between model computations and experimental calorimetric data is shown in Figs. 5–7. Satisfactory reproduction of experimental enthalpies of mixing in the liquid state [93Hay] by the corresponding modeled Gibbs energy is demonstrated in Fig. 5. Fig. 6 gives a summary of experimental data for the enthalpy of formation at several temperatures. Together with the calorimetric data of Predel and Vogelbein [79Pre] and Schmid et al. [95Sch], enthalpies of formation that were derived from emf measurements by Vinokurova et al. [70Vin, 73Vin] and from atomic absorption experiments by Bhattacharya and Masson [75Bha] are also included. The solid line refers to the calculated enthalpy of formation at 1060 K, and the kinks in this line correspond to phase boundaries between the corresponding phase fields in Fig. 1. In view of the scatter of the experimental data, the agreement is quite satisfactory except for the data points by Bhattacharya and Masson [75Bha] in the nickel solid solution phase. Since these were obtained by Gibbs-Duhem integration from the temperature dependence of the partial Gibbs energies, they were given a weak statistical weight during the optimization calculations. Similarly, the scattered values for the phases Ni₃In, Ni₂In₃, and Ni₃In₇ at In mole fractions of 0.25, 0.6 and 0.7 were used with a low statistical weight. Finally, Fig. 7 shows the enthalpy of formation at 298 K as a function of composition. Here it can be seen that the correspondence between calculation and experiment is much better for the Ni₃In₇ phase.

![](./images/813178095728066562_5.jpg)

Fig. 5. Experimental and calculated enthalpies of mixing in the liquid phase; standard states: Ni(l), In(l).

![](./images/813178095728066562_6.jpg)

Fig. 6. Experimental and calculated enthalpies of formation of solid Ni–In alloys; standard states: fcc Ni(s), In(l).

![](./images/813178095728066562_7.jpg)

Fig. 7. Experimental and calculated enthalpies of formation of solid Ni–In alloys at 298 K; standard states: fcc Ni(s), In(s).

The enthalpies of melting of the two intermetallic phases $\zeta$-Ni₂In and $\delta$-NiIn were also calculated on the basis of the modeled Gibbs energies of the two compounds and of the liquid phase. Table 8 demonstrates very good agreement with the experimental values by [95Sch].

P. Waldner, H. Ipser: Thermodynamic modeling of the $Ni-In$ system

Table 8. Experimental and calculated values of the enthalpy of melting of the congruently melting phases $\zeta-Ni_{2}In$ and $\delta-NiIn$.

<table>
  <thead>
    <tr>
      <th>Phase</th>
      <th>$T/^\circ$C</th>
      <th>$x_{In}$</th>
      <th>$\Delta_{m}H/J\ mol^{-1}$</th>
      <th>Ref.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">$\zeta-Ni_{2}In$</td>
      <td>943</td>
      <td>0.37</td>
      <td>16150</td>
      <td>[95Sch]</td>
    </tr>
    <tr>
      <td>946.6</td>
      <td>0.356</td>
      <td>15914</td>
      <td>calc.</td>
    </tr>
    <tr>
      <td rowspan="2">$\delta-NiIn$</td>
      <td>921</td>
      <td>0.55</td>
      <td>20440</td>
      <td>[95Sch]</td>
    </tr>
    <tr>
      <td>926.2</td>
      <td>0.549</td>
      <td>19628</td>
      <td>calc.</td>
    </tr>
  </tbody>
</table>

## 5 Conclusion

For the first time, a complete thermodynamic description of the $Ni-In$ system is presented. With the modeled Gibbs energies of eleven phases in the system it is possible to calculate all phase equilibria of the $T-x$ phase diagram at a total pressure of 1 bar over the entire composition range. Available experimental thermodynamic data can be reproduced in a satisfactory manner. Therefore, this work can serve as a basic contribution to establishing data bases for multi-component Ni and/or In alloys.

The authors want to thank Profs. W. Sitte and H. Gamsjäger for their interest in this research. Financial support by the Austrian Science Foundation under Project No. P12962-CHE is gratefully acknowledged.

## References

64Kje Kjekshus, A.; Pearson W.B., in H. Reiss (ed.), Progr. Mater. Sci. 1 (1964) 83.
69Ell Ellner, M.; Bhan, S.; Schubert, K.: J. Less-Common Met. 19 (1969) 245.
70Hil Hillert, M.; Staffanson, L.I.: Acta Chem. Scand. 24 (1970) 3618.
70Vin Vinokurova, G.A.; Geiderikh, V.A.: Russ. J. Phys. Chem. 44 (1970) 1190.
73Vin Vinokurova, G.A.; Geiderikh, V.A.; Gerasimov Ya.I.: Dokl. Akad. Nauk. SSSR 211 (1973) 620.
75Bha Bhattacharya, D.; Masson, D.B.: Metall. Trans. A 6 (1975) 2273.
76Bha Bhattacharya, D.; Masson, D.B.: Mater. Sci. Eng. 22 (1976) 133.
77Bha Bhattacharya, D.; Masson, D.B.: Mater. Sci. Eng. 28 (1977) 285.
79Pre Predel, B.; Vogelbein, W.: Thermochim. Acta 30 (1979) 187.
81Ber Berezutskii, V.V.; Ivanov, M.I.; Lukashenko, G.M.: Ukr. Khim. Zh. 47 (1981) 543.
82Cha Chang, Y.A.; Neumann, J.P.: Prog. Solid State Chem. 14 (1982) 221.
81Sun Sundman, B.; Ågren, J.: J. Phys. Chem. Solids 42 (1981) 297.
88Sin Singleton, M.F.; Nash, P.: Bull. Alloy Phase Diagr. 9 (1988) 592.
90Eri Eriksson, G.; Hack, K.: Metall Trans B 21 (1990) 1013.
90Mas Massalski, T.B.; Okamoto, H.; Subramanian, P.R.; Kacprzak, L. (eds.): Binary Alloy Phase Diagrams, 2nd edition, ASM, Materials Park, OH (1990) 2267.
91Bie Bienzle, M.; Sommer F.: Z. Metallkd. 82 (1991) 609.
91Din Dinsdale, A.T.: CALPHAD 15 (1991) 317.
91Vil Villars, P.; Calvert, L.D. (eds.): Pearson's Handbook of Crystallographic Data for Intermetallic Phases, 2nd edition, ASM, Materials Park, OH (1991) 4025.
93Hay Hayer, E.; Komarek, K.L.; Gaune-Escard, M.; Bros, J.P.: J. Non-Cryst. Solids 156-158 (1993) 379.
95Kön Königsberger, E.; Eriksson, G.: CALPHAD 19 (1995) 207.
95Sch Schmid, J.; Bienzle, M.; Sommer, F.; Predel, B.: Z. Metallkd. 86 (1995) 877.
97Ans Ansara, I.; Dupin, N.; Lukas, H.L.; Sundman, B.: J. Alloys Comp. 247 (1997) 20.
97Dur Durussel, Ph.; Burri, G.; Feschotte, P.: J. Alloys Comp. 257 (1997) 253.
98Hua Huang, W.; Chang, Y.A.: Intermetallics 6 (1998) 487.
98Ric Richter, K.W.: J. Phase Equil. 19 (1998) 455.
99Oka Okamoto, H.: J. Phase Equil. 20 (1999) 540.
99Per Perring, L.; Kuntz, J.J.; Bussy, F.; Gachon, J.C.: Intermetallics 7 (1999) 1235.
00Nor Norén, L.; Withers, R.L.; Tabira, Y.: J. Alloys Comp. 309 (2000) 179.
01Kat Katayama, I.: Private communication, Osaka University (2001).
02Wal Waldner, P.; Ipser H.: Intermetallics 10 (2002) 485.

(Received March 8, 2002)

### Correspondence address

Prof. Dr. Herbert Ipser
Institut für Anorganische Chemie
Universität Wien
Währingerstr. 42, A-1090 Wien, Austria
Tel.: + 43 1 4277 52606
Fax: + 43 1 4277 9526
E-mail: herbert.ipser@univie.ac.at