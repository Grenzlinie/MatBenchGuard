# On the binary Sb-Sn system: ab initio calculation and thermodynamic remodeling

Wojciech Gierlotka¹,* ![](./images/812744125639032833_1.jpg)

¹ National Dong Hwa University, Hualien, Taiwan, ROC

Received: 6 April 2019
Accepted: 13 August 2019

© Springer Science+Business Media, LLC, part of Springer Nature 2019

## ABSTRACT
The thermodynamic descriptions of phase diagrams play an important role in modern materials engineering, especially as a part of materials genome used for development of new alloys. Therefore, it is crucial to have a thermodynamic database that is in agreement with recent experimental findings. The binary Sb-Sn system is an important part of step soldering and a promising Li-ion battery electrode; therefore, a knowledge of its phase equilibria is essential for modern engineering. The newest experimental results enhanced the knowledge about phase equilibria and crystal structures in this system, and hence it is possible to propose a new, more accurate thermodynamic model of this important binary system. In this work, the CALPHAD method was used for determination of Gibbs energies of all phases; moreover, the new knowledge about a crystal structure of intermetallic compound $Sb_3Sn_4$ enabled the application of the first-principles calculations, which made CALPHAD description more precise. The proposed thermodynamic description shows a good agreement with available experimental data and can be used for future development of higher-ordered alloys.

## Introduction
The binary Sb-Sn system is an important part of the step soldering technology [1-3]. Some of the electronic instruments require more than one soldering step during production process; therefore, to avoid melting of joints done earlier, solders with different melting temperatures are used. The melting temperature of Sb-Sn solder is higher than a classical Sn-Pb; thus, antimony-tin solders found application as so-called high-temperature solder. Furthermore, addition of alloying elements to the binary Sb-Sn alloy allows for development of lead-free high-temperature solders with various melting temperatures. It is obvious that knowledge of phase equilibria and phase transformations of solder material is crucial for its applications. On the other hand, Sb and Sn are active elements toward Li; thus, the intermetallic phase Sb-Sn is a potential candidate for electrode material [4]. Moreover, thermodynamic databases are necessary parts of materials genome used for a novel approach to materials design, so-called "materials by design" [5] technique. In this approach, it is crucial to have an accurate thermodynamic description that

Address correspondence to E-mail: wojtek@gms.ndhu.edu.tw

https://doi.org/10.1007/s10853-019-03934-6

Published online: 21 August 2019

![](./images/812744125639032833_2.jpg)

follows recent findings and is in agreement with information that is considered as state of the art. Due to the new experimental data describing phase equilibria in the binary Sb-Sn system, it seems to be reasonable to propose a new thermodynamic model that also can be considered as a state of the art.

## Literature review

The literature reveals several versions of phase diagram. The most popular depiction of phase equilibria of Sb-Sn system includes five phases: liquid, BCT_A5 (Sn), Rhombohedral_A7 (Sb), SbSn, and $Sb_2Sn_3$. The very detailed literature review was done by Schmetterer et al. [6]; therefore, in this paper only the most significant information will be listed. For the first time, the phase equilibria were described by Reinders [7] who proposed a Sb-Sn phase diagram with two intermetallic compounds: SbSn and $Sb_4Sn_3$ or $Sb_5Sn_4$. After that, Gallagher [8] suggested different equilibria, where only one intermediate phase SbSn with a high- and low-temperature variations. Williams [9] described the Sb-Sn system with aid of thermal analysis (TA) and concluded the existence of one intermetallic compound SbSn. Loebe [10] analyzed ternary Pb-Sb-Sn system, and by the way he determined homogeneity range of SbSn phase as 50-53 at.% Sb. Using electroconductivity measurement as a function of composition, Konstantinow and Smirnov [11] were able to determine two intermetallic compounds: SbSn and $Sb_2Sn_3$. The eutectic reaction at 518 K in the Sb-Sn system was reported by Stead and Spencer [12]. The first X-ray diffraction (XRD) analysis was done by Jones and Bowen [13] who determined a crystal structure of SbSn phase as NaCl-type. The same authors in their next work [14] determined solubility of Sn in (Sb) phase and Sb in (Sn) as 10 at.% and 9 at.%, respectively. Broniewski and Sliwowski [15] investigated a homogeneity range of SbSn phase by aid of electromotive force measurement (EMF) and TA and reported a range 40-60 at.% of Sb. Solidus temperatures were determined by Iwase et al. [16] based on differential thermal analysis (DTA). In the same work, Iwase et al. [16] reported a thermal effect at 598 K and interpreted it as a phase transformation in SbSn. The phase transformation at 598 K was confirmed by Blondel and Laffitte [17], but in contrast to Iwase et al. [16] they reported phase transformation in $Sb_2Sn_3$. The SbSn phase was also investigated by Hagg and Hybinette [18] who focused on crystal structure determination.

The phase equilibria were described by Hansen and Onderko [19] who proposed a phase diagram with only one intermediate phase SbSn that exhibits a wide homogeneity range. A solubility of Sb in (Sn) phase was determined by Eyre [20] based on equilibration experiment at different temperatures from 323 to 496 K. Allen and Perepezko [21] examined the SbSn phase by XRD method. Moreover, they [21] completed DTA and differential scanning calorimetry (DSC) experiments for Sn-rich side ($x_{Sb} < 0.25$) of the Sb-Sn system. In that work [21], the polymorphic transformation of SbSn phase was not confirmed, but instead, the NaCl-type of crystal lattice of this SbSn phase was affirmed. Predel and Schwermann [22] improved the phase diagram and added a $Sn_3Sb_2$ compound that was formed at 515 K from (Sn) and SbSn phase. The $Sn_3Sb_2$ phase was decomposed by a peritectic reaction at 598 K. The phase diagram proposed by Predel and Schwermann [22] was redrawn by Okamoto et al. [23] in their well-known phase diagram handbook. After that, Vasilliev et al. [24] suggested that the SbSn phase is in fact a set of four phases $\beta$, $\beta'$, $\beta''$, and $\beta'''$ and proposed a modified phase diagram of the Sb-Sn system.

The Predel and Schwermann's [22] phase diagram of Sb-Sn with five phases: liquid, BCT_A5 (Sn), Rhombohedral_A7 (Sb), SbSn, and $Sb_2Sn_3$, was the main representation of phase equilibria for many years, even the eutectoid reaction at 515 K was not well examined and documented [25, 26]. This mystery was partially resolved by Chen et al. [27] who were not able to find the reaction at 515 K using differential thermal analysis (DTA). Consequently, they [27] proposed a new phase diagram, where the $Sb_2Sn_3$ was stable at the room temperature. However, Chen et al. [27] were not able to distinguish SbSn and $Sb_2Sn_3$ phases based on XRD experiment; therefore, they followed Predel and Schwermann's [22] stoichiometry of $Sb_2Sn_3$. Recently, Schmetterer et al. [6, 28] performed a deep literature research as well as own experimental investigation on Sb-Sn phase diagram. According to their results, the phase $Sb_2Sn_3$ does not exist in the antimony-tin system. Instead, a binary phase $Sb_3Sn_4$ is presented. This particular phase is believed to be stable at room temperature and decomposed at peritectic reaction liquid + SbSn = $Sb_3Sn_4$ at 599 K. Moreover, using X-ray

![](./images/812744125639032833_3.jpg)

diffraction (XRD) method, Schmetterer et al. [28] described a crystal structure of SbSn phase as $\text{Sb}_3\text{Sn}_4$ blocks with additional Sb layers.

To the best knowledge of author, thermodynamic properties of the solid phases were not investigated. The liquid phase was examined by calorimetric and electromotive force measurement (EMF) methods. The calorimetric measurement was used by Kawakami [29] who determined enthalpy of mixing at 1073 K. The same method was utilized by Kleppa [30] at 723 K, Witting and Gehring [31] at 973 K, Sommer et al. [32] at temperature range from 788 K to 1108 K, and Azzaoui et al. [33] at 892 K and 913 K. The enthalpy of mixing does not exhibit temperature dependency, and differences between respective measurements can be explained by an experimental error. The EMF method was utilized by Frantic and McDonald [34] and Yanko et al. [35] who used molten salt electrolyte for Sn-rich alloys. Their results approach ideal solution and almost do not show deviation from Raoult's law. The same method was used by Vassiliev et al. [36] who measured chemical potential of Sn for whole concentration range. In contrast, Hao et al. [26], Itoh et al. [37], and Jendrzejczyk and Fitzner [38] used solid state electrolyte in their EMF determination. Results of works [26, 37, 38] agree one another and show negative deviation from Raoult's Law for whole concentration range.

The Sb–Sn system was thermodynamically modeled by Jonsson and Agren [39], Oh et al. [40], Ohtani et al. [25], and by Chen et al. [27]. In general, the thermodynamic descriptions agree one another except the description of intermetallic phase $\text{Sb}_2\text{Sn}_3$. Earlier descriptions [25, 39, 40] proposed this intermetallic stable at the temperature range 515–598 K, whereas Chen et al. [27] assumed that this IMC is stable from 0 to 598 K. Recently, Lysenko [41] added a phase $\text{Sb}_3\text{Sn}_4$ to the description by Oh et al. [40] proposing a system with two IMCs: $\text{Sb}_2\text{Sn}_3$ and $\text{Sb}_3\text{Sn}_4$. However, taking into account experimental information this proposition does not seem to be correct.

The experimental information available in the literature was gathered and organized by Okamoto et al. [42] who published a review of binary Sb–Sn system in Journal of Phase Equilibria and Diffusion.

## Thermodynamic models

Thermodynamic descriptions of five phases: liquid, BCT_A5, Rhombohedral_A7, SbSn, and $\text{Sb}_3\text{Sn}_4$, are presented in this work.

The Gibbs free energies of pure elements with respect to temperature $^0G_i(T)=G_i(T)-H_i^\text{SER}$ are represented by Eq. 1:

$$
\begin{aligned}
^0G_i(T) &= a + bT + cT\ln(T) + dT^2 + eT^{-1} + fT^3 + iT^4 \\
&\quad + jT^7 + kT^{-9}
\end{aligned}
\tag{1}
$$

The $^0G_i(T)$ data are referred to the constant enthalpy value of the standard element reference $H_i^\text{SER}$ at 298.15 K and 1 bar as recommended by Scientific Group Thermodata Europe (SGTE) [43]. The reference states are Rhombohedral_A7 (Sb) and BCT_A5 (Sn). The expression may be given for several temperature ranges, where the coefficients $a, b, c, d, e, f, i, j$, and $k$ have different values. The $^0G_i(T)$ functions are taken from SGTE Unary (pure elements) TDB v.5 [43].

The BCT_A5, Rhomboheral_A7 and liquid phases are described by a substitutional solution model where the Gibbs energy of one mole of phase is given as follows:

$$
\begin{aligned}
^mG^\alpha &= x_\text{Sb}\,^0G_\text{Sb}^\alpha + x_\text{Sn}\,^0G_\text{Sn}^\alpha + RT(x_\text{Sb}\ln x_\text{Sb} + x_\text{Sn}\ln x_\text{Sn}) \\
&\quad + x_\text{Sb}x_\text{Sn}\sum_i(^iA + ^iBT)(x_\text{Sb} - x_\text{Sn})^i
\end{aligned}
\tag{2}
$$

where $\alpha$ is a given phase (liquid, BCT_A5, and Rhombohedral_A7), $R$ is a gas constant, $T$ is an absolute temperature, $^iA$ and $^iB$ are adjustable parameters and $i$ is an integer ($i=0,1,2...$).

The $^iA + ^iBT$ term in Eq. 2 is identified as an interaction parameter. The $^iA$ is interpreted as excess enthalpy and $^iB$ as excess entropy. It is well-known fact that this kind of approach sometimes leads to inverted miscibility gap in liquid phase at high temperatures or allows excess Gibbs energy for approaching $+\infty$ when $T$ also approaches $+\infty$. To avoid this non-physical behavior of excess Gibbs energy, Kaptay [44] proposed so-called exponential function for describing interaction parameters:

$$
^jL^\text{Liquid}_\text{Al,Ti} = ^jh^\text{Liquid}_\text{Al,Ti} \cdot \exp\left(-\frac{T}{^j\tau^\text{Liquid}_\text{Al,Ti}}\right)
\tag{3}
$$

![](./images/812744125639032833_4.jpg)

where $^{j}L_{\text{Al,Ti}}^{\text{Liquid}}$ is an interaction parameter of J-th degree, $^{j}h_{\text{Al,Ti}}^{\text{Liquid}}$ is the enthalpy part of the interaction energy, $^{j}\tau_{\text{Al,Ti}}^{\text{Liquid}}$ is a special temperature, at which the interaction energy would cross zero if it was described by the linear model and $T$ is the absolute temperature.

The exponential interaction parameters were used in this work for describing excess Gibbs energy of liquid phase.

The intermediate phase $\text{Sb}_3\text{Sn}_4$ was treated as a line compound; therefore, its Gibbs energy is described by the following equation:
$$
{ }^{0} G_{\mathrm{Sb}: \mathrm{Sn}}^{\mathrm{Sb}_{3} \mathrm{Sn}_{4}}=a+b T+3 * \mathrm{GHSERSB}+4 * \mathrm{GHSERSN}
\tag{4}
$$
where $a$ and $b$ are adjustable parameters, $T$ is an absolute temperature and GHSERSB and GHSERSN are Gibbs energies of Sb and Sn in their SER reference state, respectively.

According to Schmetterer et al. [28], the SbSn phase is a mix of Sb3Sn4 blocks and Sb layers; therefore, a two-sublattice model (Sb,Sn)4:(Sb)3 is proposed in this work. The Gibbs energy is therefore given by the following equation:
$$
\begin{aligned}
{ }^{\mathrm{m}} G^{\mathrm{SbSn}}= & y_{\mathrm{Sb}}^{\mathrm{I}} y_{\mathrm{Sb}}^{\mathrm{II}}{ }^{0} G_{\mathrm{Sb}, \mathrm{Sb}}^{\mathrm{SbSn}}+y_{\mathrm{Sn}}^{\mathrm{I}} y_{S b}^{\mathrm{II}}{ }^{0} G_{\mathrm{Sn}, \mathrm{Sb}}^{\mathrm{SbSn}}+{ }^{\mathrm{id}, \mathrm{mix}} G_{\mathrm{m}}^{\mathrm{SbSn}} \\
& +{ }^{\mathrm{xs}} G_{\mathrm{m}}^{\mathrm{SbSn}}
\tag{5}
\end{aligned}
$$
where $^{\text{id,mix}}G_{\text{m}}^{\text{SbSn}}$ is the Gibbs free energy of ideal mixing, $^{\text{xs}}G_{\text{m}}^{\text{SbSn}}$ is the excess Gibbs free energy, $y_{i}^{m}$ is a m ($m$ = I or II) site fraction occupied by an element I (I = Sb, Sn) and $^{0}G_{i,j}^{\text{SbSn}}$ is the Gibbs energy of end member when a sublattice I is occupied by element I and sublattice II is occupied by element $j$.

The ideal mixing term is given by Eq. 6:
$$
{ }^{\mathrm{id}, \mathrm{mix}} G_{\mathrm{m}}^{\mathrm{SbSn}}=4 \mathrm{RT}\left(y_{\mathrm{Sb}}^{\mathrm{I}} \ln y_{\mathrm{Sb}}^{\mathrm{I}}+y_{\mathrm{Sn}}^{\mathrm{I}} \ln y_{\mathrm{Sn}}^{\mathrm{I}}\right)
\tag{6}
$$

And the excess Gibbs energy is given by Eq. 7:
$$
{ }^{\mathrm{xs}} G_{\mathrm{m}}^{\mathrm{SbSn}}=y_{\mathrm{Sb}}^{\mathrm{I}} y_{\mathrm{Sn}}^{\mathrm{I}} y_{\mathrm{Sb}}^{\mathrm{II}} \sum_{k}{ }^{k} L^{\mathrm{SbSn}}\left(y_{\mathrm{Sb}}^{\mathrm{I}}-y_{\mathrm{Sn}}^{\mathrm{I}}\right)^{k}
\tag{7}
$$
where $y_{i}^{m}$ is a $m$ ($m$ = I or II) site fraction occupied by an element $i$ ($i$ = Sb, Sn) and $^{k}L_{i,j}^{\text{SbSn}}$ is the adjustable parameter in a form $^{k}A+^{k}BT$.

![](./images/812744125639032833_5.jpg)

## Ab initio calculation
According to Shmetterer et al. [28], the $\text{Sb}_3\text{Sn}_4$ crystalizes in a rhombohedral structure that belongs to $R\overline{3}m$ space group and is analogous to homologous structures of $\text{As}_3\text{Sn}_4$ and $\text{P}_3\text{Sn}_4$. The parameters of a unit cell were determined as $a=4.33111\text{A}$ A and $c=37.302\text{A}$ A [28]. This information was used for modeling a crystal structure of $\text{Sb}_3\text{Sn}_4$ in VESTA software [45], what is shown in Fig. 1 and exported as a CIF file. The CIF2Cell [46] code was used for generating input structure of Wigner-Seitz cells for further calculations. The ab initio calculation was performed within density functional theory (DFT) that was implemented in the Siesta [47] software. The calculation was spin-non-polarized and used generalized gradient approximation (GGA) pseudopotentials. The pseudopotentials for Sb and Sn were taken from the Siesta web page [47]. Before calculation, a convergence test in respect to the number of k points in Monkhorst-Pack mesh grid was done. The values used in this work were $10\times10\times10$. The mesh cut-off was also converged and determined as 400 Ry. During the calculation, the phases geometry was optimized and minimal value of energies was obtained parameters for Weiner-Seitz cells equal: $a=4.308, 5.9123$, and $4.350$ Å for Sb, Sn, and $\text{Sb}_3\text{Sn}_4$, respectively, and the formation enthalpy of $\text{Sb}_3\text{Sn}_4$ was determined as $-29600$ J/mol. It should be written here that a standard procedure in a case of determination of formation enthalpy by ab initio

![](./images/812744125639032833_6.jpg)

Figure 1 A unit cell of a phase $\text{Sb}_3\text{Sn}_4$ modeled in VESTA software for further ab initio calculation.

method and discussion about phase stability is cal-
culating the convex hull. Unfortunately, it is impos-
sible to calculate the convex hull and discuss the
stabilities of $Sb_3Sn_4$ and $Sb_2Sn_3$ phases due to the
unreported crystal structure of $Sb_2Sn_3$ phase. In the
latest version of Sb–Sn phase diagram with $Sb_2Sn_3$
phase proposed by Okamoto [48], the crystal struc-
ture of $Sb_2Sn_3$ remained unknown. Schmetterer et al.
[6] discussed crystallization of $Sb_2Sn_3$ in NaCl-type
crystal structure, as proposed by Chen et al. [27], but
the discussion concludes that this crystal structure
cannot be considered due to diverging stoichiometry.
Consequently, it was impossible to calculate forma-
tion enthalpy of $Sb_2Sn_3$, prepare the convex hull, and
discuss phases stability.

## Optimization procedure

The thermodynamic optimization was carried out in
agreement with the guideline by Schmid-Fetzer et al.
[49]. The thermodynamic information about liquid
phase, phase equilibria information, and ab initio
calculation result were used in this modeling. Each
piece of the selected information was given a certain
weight based on personal judgment and experimen-
tal uncertainty. The formation energy of $Sb_3Sn_4$
obtained from first principle approach was assumed
as a function independent of temperature and kept
unchanged during the optimization procedure. First,
the liquid phase was optimized using thermody-
namic data such as activities of elements and
enthalpy of mixing. After that, parameters of liquid
phase were kept unchanged and solid phases were
assessed based on invariant reactions, phase equi-
libria data, and formation energy of $Sb_3Sn_4$ taken
from ab initio calculation. Finally, all the
adjustable parameters were optimized together in
order to obtain the best fitting of experimental data.

## Results and discussion

The ab initio calculations performed in this work
provide also a unit cell size for relaxed structure. As
it was mentioned in paragraph 4, during this proce-
dure following values for a size of Weigner-Seitz cell:
4.308, 5.9123, and 4.350 Å for Sb, Sn, and $Sb_3Sn_4$,
respectively. Converting obtained information back
to the size of a unit cell of $Sb_3Sn_4$, the parameters are
equal $a = 4.3079$ Å and $c = 37.1029$ Å. The agreement
with experimental results seems to be good because
difference along $x$ and $c$ axis is equal to $-0.54\%$.
Similarly, the calculated size of Sb unit cell is only
0.23% bigger than given in the literature [50]. The
bigger difference between information provided by
experiment [51] and calculation was observed in a
case of Sn. The calculated unit cell is 1.37% bigger
than revealed by experiment. The difference between
calculated and experimentally determined sizes of
unit cells is not surprise, and this phenomenon can be
found quite often in the literature [47].

The thermodynamic parameters for all phases in
the binary Sb–Sn system obtained in this work are
given in Table 1. For the optimization, the Thermo-
Calc [52] software was used and results were addi-
tionally checked in the Pandat [53] software. This
procedure allows for a double check of obtained
results due to different algorithms for phase diagram
calculation applied in both softwares [52, 53].

Figure 2 displays calculated phase diagram com-
pared to experimental data provided by Schmetterer
et al. [28], Chen et al. [27], Iwase et al. [16], Ohtani
et al. [25], and Predel and Schwermann [22]. It can be
seen that a phase diagram agrees with most of the
experimental data. The invariant reactions are
reproduced well within experimental information
range. Detailed information is given in Table 2. The
liquidus line of binary region liquid + SbSn follows
data given by Schmetterer et al. [28] and Chen et al.
[27] rather than given by Predel and Schwermann
[22]. Both calculated intermediate phases reproduce
experimentally determined phase equilibrium well.
The Gibbs energy of the intermetallic compound
$Sb_3Sn_4$ was calculated as follows: First, the energy of
formation of the compound was determined by
ab initio calculation at 0 K; next it was assumed that
enthalpy of formation is independent of temperature;
therefore, it is equal energy of formation at 0 K. This
information was subsequently applied to optimiza-
tion procedure where the entropy of formation was
assessed. After optimization of $Sb_3Sn_4$, the Gibbs
energy of SbSn was calculated. Modeled in this work
invariant reactions, together with respective compo-
sition of phases, are given in Table 2. It can be noticed
that composition of SbSn phase in the reaction:
$L + Rhombohedral\_A7 = SbSn$, is shifted toward Sb
comparing with previous works. This behavior was
suggested by Schmetterer et al. [28], and this work
consequently follows this suggestion. As it was

![](./images/812744125639032833_7.jpg)

<table>
<caption>Table 1 Thermodynamic parameters of phases in the binary Sb–Sn system</caption>
<thead>
<tr>
<th>Phase</th>
<th>Parameter</th>
<th>References</th>
</tr>
</thead>
<tbody>
<tr>
<td>Liquid</td>
<td>$^{0}L_{\text{Sb,Sn}}^{\text{Liquid}} = -5384.54 * \text{EXP}(-1.00004781\text{E} - 05 * T)$</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>$^{1}L_{\text{Sb,Sn}}^{\text{Liquid}} = 8620.04 * \text{EXP}(-5.39237166\text{E} - 03 * T)$</td>
<td>This work</td>
</tr>
<tr>
<td>BCT_A5</td>
<td>$^{0}L_{\text{Sb,Sn}}^{\text{BCT_A5}} = -13767.02 + 10.7383 * T$</td>
<td>This work</td>
</tr>
<tr>
<td>Rhombohedral_A7</td>
<td>$^{0}L_{\text{Sb,Sn}}^{\text{Rhombohedral_A7}} = 5289.04 - 2.4569 * T$</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>$^{1}L_{\text{Sb,Sn}}^{\text{Rhombohedral_A7}} = -2595.98$</td>
<td>This work</td>
</tr>
<tr>
<td>Sb₃Sn₄</td>
<td>$^{0}G_{\text{Sb:Sn}}^{\text{Sb₃Sn₄}} = -29600 + 7.9409 * T + 3 * \text{GHSERSB} + 4 * \text{GHSERSN}$</td>
<td>This work</td>
</tr>
<tr>
<td>SbSn</td>
<td>$^{0}G_{\text{Sb:Sn}}^{\text{SbSn}} = -90.74 + 1.9943 * T + ^{0}G_{\text{Sb:Sn}}^{\text{Sb₃Sn₄}}$</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>$^{0}G_{\text{Sb:Sb}}^{\text{SbSn}} = 63033.55 - 46.9427 * T + 7\text{GHSERSB}$</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>$^{0}L_{\text{Sb:Sb,Sn}}^{\text{SbSn}} = -39339.33 + 12.6125 * T$</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td>$^{1}L_{\text{Sb:Sb,Sn}}^{\text{SbSn}} = 19516.64 - 70.0693 * T$</td>
<td>This work</td>
</tr>
</tbody>
</table>

Figure 2 Calculated phase
diagram of Sb–Sn system
superimposed with
experimental data.

![](./images/812744125639032833_8.jpg)

written in a previous paragraph, the liquid phase was
described by exponential model proposed by Kaptay
[44]. This model leads in rare occasions to stabiliza-
tion of liquid phase at low temperature [44]. In this
work, the low-temperature stabilization of liquid
does not occur; however, due to a common practice
of showing calculated phase diagrams from 300 K up
to higher temperature, it was decided to show cal-
culated phase diagram for a temperature range
300–1500 K.

Figure 3 shows calculated activity of tin at 1173 K
superimposed with experimental data obtained by
Itoh et al. [37], Jendrzejczyk and Fitzner [38], and
Frantic and McDonalds [34]. The calculation follows

![](./images/812744125639032833_9.jpg)

**Table 2** Calculated invariant reactions in the binary Sb–Sn system

<table>
  <thead>
    <tr>
      <th>Reaction</th>
      <th>T (K)</th>
      <th colspan="3">Composition, $x_{\text{Sb}}$</th>
      <th>Refs.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">L + $\text{Sb}_3\text{Sn}_4$ = BCT_A5</td>
      <td>517.2</td>
      <td>0.071</td>
      <td>0.428</td>
      <td>0.098</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>516</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>519</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[16]</td>
    </tr>
    <tr>
      <td>523</td>
      <td>0.06</td>
      <td>–</td>
      <td>0.1</td>
      <td>[22]</td>
    </tr>
    <tr>
      <td>518</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[36]</td>
    </tr>
    <tr>
      <td>517</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[10]</td>
    </tr>
    <tr>
      <td>517</td>
      <td>–</td>
      <td>0.428</td>
      <td>–</td>
      <td>[28]</td>
    </tr>
    <tr>
      <td rowspan="7">L + SbSn = $\text{Sb}_3\text{Sn}_4$</td>
      <td>595.6</td>
      <td>0.194</td>
      <td>0.462</td>
      <td>0.428</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>583</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>598</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[16]</td>
    </tr>
    <tr>
      <td>597</td>
      <td>0.21</td>
      <td>–</td>
      <td>0.43</td>
      <td>[22]</td>
    </tr>
    <tr>
      <td>598</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[36]</td>
    </tr>
    <tr>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[10]</td>
    </tr>
    <tr>
      <td>599</td>
      <td>–</td>
      <td>–</td>
      <td>0.428</td>
      <td>[28]</td>
    </tr>
    <tr>
      <td rowspan="7">L + Rhombohedral_A7 = SbSn</td>
      <td>697.5</td>
      <td>0.489</td>
      <td>0.869</td>
      <td>0.674</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>703</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[7]</td>
    </tr>
    <tr>
      <td>698</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[16]</td>
    </tr>
    <tr>
      <td>698</td>
      <td>0.50</td>
      <td>–</td>
      <td>0.652</td>
      <td>[22]</td>
    </tr>
    <tr>
      <td>698</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[36]</td>
    </tr>
    <tr>
      <td>695</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[10]</td>
    </tr>
    <tr>
      <td>698</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>[28]</td>
    </tr>
  </tbody>
</table>

**Figure 3** Calculated activity of Sn in liquid Sb–Sn at 1173 K together with experimental data. The reference states are: Sb—liquid, Sn—liquid.

![](./images/812744125639032833_10.jpg)

![](./images/812744125639032833_11.jpg)

Itoh et al. [37] data rather than the data given by Jendrzejczyk and Fitzner [38] and Frantic and McDonalds [34]. It can be easily seen that even the experiment temperature varies marginally the discrepancy between obtained activities is quite big. For example, for concentration $x_{\text{Sn}} = 0.6$ activity determined by Jendrzejczyjk-Handzlik and Fitzner [38] is equal to 0.44, whereas Itoh et al. [37] reported value of 0.51; therefore, one can say that calculation agrees with experiment pretty fair.

Figure 4 exhibits calculated chemical potential of Sn in liquid Sb-Sn at 900 K and 770 K. In the same figure, the experimental data given by Vassilev et al. [36] are placed. It can be seen that for a temperature 900 K calculation reproduces experimental data pretty well except on point for higher concentration of Sn; however, it can be noticed that the mentioned experimental data do not fit a trend represented by other points. For temperature 770 K, the calculation agrees with all experimental data.

Figure 5 shows calculated enthalpy of mixing of liquid phase superimposed with experimental data given by Azzaoui et al. [33], Witting and Gehring [31], and Sommer et al. [32]. This figure shows a very good agreement between calculation and experiment. It also demonstrates that enthalpy of mixing in a case of binary Sb-Sn system can be treated as a function independent of temperature. A small difference between various datasets can be explained by experimental error, which in a case of calorimetric measurement can be assumed as 250 J/mol. The calorimetric data obtained at 1073 K by Kawakami [29] were not included into this optimization because it was impossible to obtain the original work. Similarly, the data given by Sommer et al. [32] were not placed in the graph due to a big temperature range of measurement what makes comparison with calculation impossible.

A proposed new thermodynamic model of the binary Sb-Sn system was developed on combination of recent determination of phase equilibria, well-known thermodynamic properties of liquid phase, and ab initio calculation. It provides a consistent set of thermodynamic parameters that can reproduce all experimental data quite well. The set of parameters can be used in future work for development of high-ordered lead-free alloys or determination of interaction of the Sb-Sn solder with various substrates.

![](./images/812744125639032833_12.jpg)

![](./images/812744125639032833_13.jpg)

![](./images/812744125639032833_14.jpg)

## Summary
A new thermodynamic model of the binary Sb-Sn system is proposed in this paper. Due to unavailable thermodynamic data about solid phases, the ab initio calculation was applied for determination of $Sb_3Sn_4$ formation energy, what made whole description more accurate. The proposed phase diagram is in agreement with the newest finding and includes $Sb_3Sn_4$ intermetallic compound instead $Sb_2Sn_3$ phase. The proposed description can be used for further development of lead-free solders or electrode materials for Li batteries.

## Acknowledgements
The work was supported by Taiwan Ministry of Science and Technology under Grant 107-2221-E-259-011.

## Compliance with ethical standards
Conflict of interest The author declares that he has no conflict of interest.

## References
[1] Ohnuma I, Liu XJ, Ohtani H, Ishida K (1999) Thermody- namioc database for micro-soldering alloys. J Electron Mater 28:1164-1171

[2] Jang JW, Kim PG, Tu KM, Lee M (1999) High-temperature lead-free SnSb solders: wetting reactions on Cu foils and phased-in Cu-Cr thin films. J Mater Res 14:3895-3900

[3] Corbin SF (2005) High-temperature variable melting point Sn-Sb solder paste using transient liquid-phase powder processing. J Electron Mater 34:1016-1025

[4] Kamali AR, Fray DJ (2011) Tin-based materials as advanced anode materials for lithium ion batteries: a review. Rev Adv Mater Sci 27:14-24

[5] Olson GB (2000) Materials by design. Science 288:995-1001

[6] Schmetterer C, Polt J, Flandorfer H (2017) The phase equilibria in the Sb-Sn system-part I: literature review. J Alloys Compd 728:497-505

[7] Reinders W (1900) Alloys of antimony and tin. Z Anorg Chem 25:113-125

[8] Gallagher FE (1906) The alloys of antimony and tin. J Phys Chem US 10:93-98

[9] Williams RS (1907) On the alloys of antimony with mag- nese, chromium, silicon and tin, of bismuth with chromium

![](./images/812744125639032833_15.jpg)

and silicon and of magnese with tin and lead. Z Anorg Chem 55:1–33

[10] Loebe R (1911) Uber die Konstitution der ternaren Lagierungen von Blei, Zinn und Antimon. Metallurgie 8:7–15

[11] Konstantinow N, Smirnow W (1912) Uber die Legierungen von Zinn und Antimon. In: Internationale Zeitschrift fur Metallographie, Berlin, pp 152–171

[12] Stead JE, Spencer LJ (1919) On the Sb–Sn system. J Inst Met 22:127–130

[13] Jones WM, Bowen EG (1930) The compound SnSb. Nature 126:846–847

[14] Bowen EG, Jones WM (1931) An X-rey investigation of the tin-antimony alloys. Philos Mag 106:441–462

[15] Broniewski W, Sliwowski L (1928) Antimony-tin alloys. Rev Met 25:312–321

[16] Iwase K, Aoki N, Osawa A (1931) DTA measurements in Sb–Sn alloys. Sci Rep Tohoku Imp Univ 20:353

[17] Blondel R, Laffitte P (1935) Phase transformations in Sb–Sn alloys. Comptes Rendus 200:1472–1474

[18] Hagg G, Hybinette AG (1935) X-ray studies on the system tin-antimony and tin-arsenic. Philos Mag 20:913–929

[19] Hansen M, Onderko K (1958) Constitution of binary alloys. McGraw-Hill, New York

[20] Eyro BL (1960) The solid solubility of antimony in tin. J Inst Met 88:223–224

[21] Allen WP, Perepezko JH (1990) Constitution of the tin-an- timony system. Scr Metall Mater 24:2215–2220

[22] Predel B, Schwermann W (1971) Constitution and thermo- dynamics of antimony-tin system. J Inst Met 99:169–172

[23] Okamoto H, Subramanian PR, Massalski TB (1990) Binary alloy phase diagrams. ASM International, Materials Park

[24] Vassilev V, Lelaurain M, Hertz J (1997) A new proposal for the binary (Sn, Sb) phase diagram and its thermodynamic properties based on a new emf study. J Alloys Compd 247:223–233

[25] Ohtani H, Okuda K, Ishida K (1995) Thermodynamic study of phase equilibria in the Pb–Sn–Sb system. J Phase Equilb 16:416–429

[26] Hao IS, Kang T, Park PC (1977) On the Sb–Sn system: electrochemical measurement of thermodynamic properties in liquid phase. Korean Metall Trans 15:361–365

[27] Chen SW, Chen CC, Gierlotka W, Zi AR, Chen PY, Wu HJ (2008) Phase equilibria of the Sn–Sb system. J Electron Mater 37:992–1002

[28] Schmetterer C, Polt J, Flandorfer H (2018) The phase equilibria in the Sb–Sn system—part II: experimental results. J Alloys Compd 743:523–536

[29] Kawakami M (1930) A further investigation of the heat of mixture in molten metals. Sci Rep Res Inst Tohoku Univ 19:521–549

[30] Kleppa OJ (1956) A calorimetric investigation of some binary and ternary liquid alloys rich in tin. J Phys Chem 60:842–846

[31] Witting FE, Gehring E (1971) Die Mischungswarmen des Antimonos mit B-Metallen. Ber Bunsenges Phys Chem 71:372–376

[32] Sommer F, Lück R, Rupf-Bolz N, Predel B (1983) Chemical short-range order in liquid Sb–Sn alloys proved with the aid of the dependence of the mixing enthalpies o temperature. Mater Res Bull 18:621–629

[33] Azzoui M, Notin M, Hertz J (1993) Ternary experimental excess functions by means of high-order polynomials. Enthalpy of mixing of liquid Pb–Sn–Sb alloys. Z Metallkd 84:545–551

[34] Frantic RO, McDonalds HJ (1946) A thermodynamic study of the tin-antimony system. Trans Electrochem Soc 88:243–251

[35] Yanko JA, Drake AE, Hovorka F (1946) Thermodynamioc studies of dilute solutions in molten binary alloys. Trans Electrochem Soc 89:357–372

[36] Vassiliev V, Feutelais Y, Sghaier M, Legendre B (2001) Thermodynamic investigation in In-Sb, Sb–Sn and In-Sb–Sn liquid systems. J Alloys Compd 314:198–205

[37] Itoh K, Koiko K, Narita Y (1980) Activity measurement of Pb–Sn and Sn–Sb based molten alloys. Nippon Kogo Kaishi 96:97–101

[38] Jendrzejczyk-Handzlik D, Fitzner K (2015) Thermodynamic properties of liquid (antimony + tin) and (gold + anti- mony + tin) alloys determined from e.m.n.f. measurement. J Chem Thermodyn 85:86–93

[39] Jonsson B, Agren J (1986) Thermodynamic assessment of Sb–Sn system. Mater Sci Technol 2:913–916

[40] Oh CS, Shim JH, Lee B-J, Lee DN (1996) A thermodynamic study on the Ag-Sb-Sn system. J Alloys Compd 238:155–166

[41] Lysenko VA (2019) Thermodynamic reassessment of the Sb–Sn and In–Sb–Sn system. J Alloys Compd 776:850–856

[42] Okamoto H (1998) Sb–Sn (antimony-tin). J Phase Equilib 19:292

[43] Scientific Group Thermodata Europe (2015) Unary Database v. 5.0, France

[44] Kaptay G (2017) The exponential excess Gibbs energy model revisited. Calphad 56:169–184

[45] Momma K, Izumi F (2011) VESTA 3 for three-dimensional visualization of crystal, volumetric, and morphology data. J Appl Crystallogr 44:1272–1276

![](./images/812744125639032833_16.jpg)

[46] Bjorkman T (2011) CIF2Cell: generating geometries for electronic structure programs. Comput Phys Commun 182:1183-1186

[47] https://departments.icmab.es/leem/siesta/. Accessed 26 Sept 2017

[48] Okamoto H (2012) Sb-Sn (antimony-tin). J Phase Equilib Differ 34:347

[49] Schmid-Fetzer R, Andersson D, Chevalier PY, Eleno L, Fabrichnaya O, Kattner UR, Sundman B, Wang C, Watson A, Zabdyr L, Zinkevich M (2007) Assessment techniques, database design and software facilities for thermodynamics and diffusion. Calphad 31:38-52

[50] Schiferl D, Barrett CS (1969) The crystal structure of arsenic at 4.2, 78 and 299 K. J Appl Cryst 2:30-36

[51] Allison MC, Avdeev M, Schmid S, Liu S, Söhnel T, Ling CD (2016) Synthesis, structure and geometrically frustrated magnetism of the layered oxide-stannide compounds Fe(Fe₃-xMnx)Si₂Sn₇O₁₆. Dalton Trans 45:9689-9694

[52] Andersson JO, Helander T, Höglund L, Shi PF, Sundman B (2002) Thermo-Calc and DICTRA, computational tools for materials science. Calphad 26:273-312

[53] Chen SL, Daniel S, Zhang F, Chang YA, Yan XY, Xie FY, Schmid-Fetzer R, Oates WA (2002) The PANDAT software package and its application. Calphad 26:175-188

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812744125639032833_17.jpg)