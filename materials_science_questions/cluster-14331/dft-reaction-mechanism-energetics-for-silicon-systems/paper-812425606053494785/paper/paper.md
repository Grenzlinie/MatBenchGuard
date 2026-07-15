# Organocalcium Complex-Catalyzed Selective Redistribution of $ArSiH_3$ or $Ar(alkyl)SiH_2$ to $Ar_3SiH$ or $Ar_2(alkyl)SiH$
Tao Li, Karl N. McCabe, Laurent Maron,* Xuebing Leng, and Yaofeng Chen*

Cite This: ACS Catal. 2021, 11, 6348−6356

ABSTRACT: Calcium is an abundant, biocompatible, and environ- mentally friendly element. The use of organocalcium complexes as catalysts in organic synthesis has had some breakthroughs recently, but the reported reaction types remain limited. On the other hand, hydrosilanes are highly important reagents in organic and polymer syntheses, and redistribution of hydrosilanes through C−Si and Si− H bond cleavage and reformation provides a straightforward strategy to diversify the scope of such compounds. Herein, we report the synthesis and structural characterization of two calcium alkyl complexes supported by $\beta$-diketinato-based tetradentate ligands. These two calcium alkyl complexes react with $PhSiH_3$ to generate calcium hydrido complexes, and the stability of the hydrido complexes depends on the supporting ligands. One calcium alkyl complex efficiently catalyzes the selective redistribution of $ArSiH_3$ or $Ar(alkyl)SiH_2$ to $Ar_3SiH$ and $SiH_4$ or $Ar_2(alkyl)SiH$ and $alkylSiH_3$, respectively. More significantly, this calcium alkyl complex also catalyzes the cross-coupling between the electron-withdrawing substituted $Ar(R)SiH_2$ and the electron-donating substituted $Ar'(R)SiH_2$, producing $ArAr'(alkyl)SiH$ in good yields. The synthesized $ArAr'(alkyl)SiH$ can be readily transferred to other organosilicon compounds such as $ArAr'(alkyl)SiX$ (where $X = OH$, $OEt$, $NEt_2$, and $CH_2SiMe_3$). DFT investigations are carried out to shed light on the mechanistic aspects of the redistribution of $Ph(Me)SiH_2$ to $Ph_2(Me)SiH$ and reveal the low activation barriers (17−19 kcal/mol) in the catalytic reaction.

KEYWORDS: calcium, catalysis, DFT, hydrosilane, redistribution

![](./images/812425606053494785_1.jpg)

## INTRODUCTION
Calcium is an abundant, biocompatible, and environmentally friendly element. The organocalcium chemistry has attracted researchers’ attention for more than a century since, for example, Beckmann reported his attempts on the synthesis of a calcium aryl complex in 1905.¹,² However, although calcium has the advantages of low cost and environmentally benign nature, the use of organocalcium complexes as catalytic reagents in organic synthesis did not gain momentum until recently. The development of calcium catalysts has lagged far behind that of transition-metal catalysts, which is mainly associated with the following features: (1) the divalent calcium ion lacks the d-electrons, which are perceived as crucial for catalytic reactions and (2) the calcium alkyl and hydrido complexes, which are the best candidates for catalysis, are rare.³⁻⁵ The groups of Harder, Hill, Okuda, and others have made some pioneer contributions in developing organocalcium complexes as catalysts. They synthesized several calcium alkyl, hydrido, and amido complexes and demonstrated their efficiency as catalysts in organic synthesis.³⁻⁹ However, the reported reaction types catalyzed by organocalcium complexes remain limited and are mainly focused on the hydrogenation or hydroelementation of alkenes (or alkynes), dehydrocoupling of aminoboranes, and dehydrocoupling of silanes with terminal alkynes (or amines).

Hydrosilanes are highly important reagents in organic and polymer syntheses.¹⁰ The redistribution of hydrosilanes is a straightforward strategy to diversify the scope of such compounds.¹¹ However, the poor selectivity and low efficiency severely hindered the application of this synthetic protocol.¹² First, the hydrosilanes can undergo dehydrocoupling to give oligo- or polysilanes, where the redistribution is, in fact, a side reaction.¹³ Second, the redistribution reactions usually provide a mixture of primary, secondary, tertiary, and quaternary silanes.¹⁴ Examples of highly selective hydrosilane redistrib- ution are quite rare (Scheme 1). Tanaka and co-workers briefly reported that $\{RuCl_2[P(C_6H_4Me-p)_3]_3\}$ catalyzes the selective

Received: January 31, 2021
Revised: April 29, 2021
Published: May 13, 2021

![](./images/812425606053494785_2.jpg)

Scheme 1. Selective Redistribution of Arylsilanes

a) Previous works

$$
\ce{Me2Si(C6H4NR2) + B(C6F5)3 ->[ - Me2SiH2] (NR2C6H4)2SiMe2}
$$
quaternary silanes

$$
\ce{R'C6H4SiH3 + [Ru(II),Yb(II),Ln(III) or Ba(II) complex] ->[ - SiH4] (R'C6H4)2SiH2}
$$
secondary silanes

b) This work

$$
\ce{R'C6H4SiH3 + Ca(II) complex ->[ - 2 SiH4] (R'C6H4)3SiH}
$$
tertiary silanes

$$
\ce{AlkylSiH2(C6H4R') + Ca(II) complex ->[ - AlkylSiH3] (R'C6H4)2SiH(Alkyl)}
$$
tertiary silanes

redistribution of trihydrophenylsilane and trihydro(p-tolyl)-silane to dihydrodiphenylsilane and dihydrodi(p-tolyl)silane, respectively, with the elimination of $\ce{SiH4}$. $^{15}$ Hou and co-workers reported that $\ce{B(C6F5)3}$ catalyzes the redistribution of tertiary silanes containing electron-rich aromatic substituents to quaternary silanes with good selectivity. $^{16}$ Recently, we found that a divalent ytterbium alkyl complex catalyzes the redistribution of primary arylsilanes to selectively provide a series of secondary arylsilanes as well as the cross-coupling between the electron-withdrawing substituted primary arylsi- lanes and electron-donating substituted primary arylsilanes to secondary arylsilanes containing two different aryls. $^{17}$ After our report, Luo and co-workers reported that the hybrid materials $\ce{Ln(CH2C6H4-NMe2-o)3@SBA-15 (Ln = La, Y)}$ are also able to catalyze the selective redistribution of primary arylsilanes to secondary arylsilanes, although the catalytic activity is much lower than that of the divalent ytterbium alkyl complex. $^{18}$ Very recently, Cheng and co-workers reported the selective redistribution of primary arylsilanes to secondary arylsilanes catalyzed by a heteroleptic barium aminobenzyl complex. $^{19}$ However, the selective redistribution of primary arylsilanes to tertiary arylsilanes as well as aryl- and alkyl-substituted secondary silanes $\ce{Ar(R)SiH2}$ to tertiary silanes $\ce{Ar2(R)SiH}$ remain challenging. There was a report that shows that alkali- metal complexes and $\ce{Ba(OC8H17)2}$ catalyze the redistribution of trihydrophenylsilane to hydrotriphenylsilane, but the yields were not ideal. $^{20}$ The radius of calcium(II) ion is very close to that of the ytterbium(II) ion $[\ce{Ca^2+} (1.00\ \text{Å})$ and $\ce{Yb^2+} (1.02\ \text{Å})$ for the coordination number of 6], $^{21}$ and recent studies showed that the catalytic properties of organocalcium complexes are somewhat similar to those of divalent organoytterbium complexes. Therefore, after we disclosed the selective redistribution of primary arylsilanes to secondary arylsilanes catalyzed by a divalent ytterbium alkyl complex, we investigated the synthesis of the related calcium alkyl complex and its catalytic properties toward the redistribution of primary arylsilanes. Interestingly, the synthesized calcium alkyl complex catalyzes the redistribution of primary arylsilanes to provide tertiary arylsilanes in excellent yields with the elimination of $\ce{SiH4}$ (Scheme 1). More significantly, the calcium alkyl complex is also able to catalyze the redistribution of $\ce{Ar(alkyl)SiH2}$ to $\ce{Ar2(alkyl)SiH}$ as well as the cross-coupling between the electron-withdrawing substituted $\ce{Ar(alkyl)SiH2}$ and electron- donating substituted $\ce{Ar'(alkyl)SiH2}$ to $\ce{ArAr'(alkyl)SiH}$ with the elimination of $\ce{alkylSiH3}$.

■ RESULTS AND DISCUSSION

Synthesis and Structural Characterization of Calcium Complexes. Reactions of $\ce{CaI2}$ with the potassium salt L1K $\{\text{L1} = [\ce{MeC(NDipp)CHC(Me)NCH2CH2N(Me)-CH2CH2NMe2}]^-, \text{Dipp} = 2,6-(^i\text{Pr})_2\text{C}_6\text{H}_3)\}$ or L2K $\{\text{L2} = [\ce{MeC(NDipp)CHC(^t\text{Bu})NCH2CH2N(Me)CH2CH2NMe2}]^-\}$ in tetrahydrofuran (THF) at room temperature provide calcium iodides, 1 and 2, with 90 and 89% yields, respectively (Scheme 2). The desired calcium alkyl complexes, 3 and 4, are

Scheme 2. Synthesis of Calcium Alkyl Complexes 3 and 4

$$
\ce{CaI2 + L1K or L2K ->[THF, r.t.][ - KI] [(L)CaI]}
$$
$\text{R} = \text{Me}$ (1), 90% yield
$\text{R} = ^t\text{Bu}$ (2), 89% yield

$$
\ce{[(L)CaI] + KCH2SiMe3 ->[benzene, r. t.][ - KI] [(L)Ca-CH2SiMe3]}
$$
$\text{R} = \text{Me}$ (3), 49% yield
$\text{R} = ^t\text{Bu}$ (4), 79% yield

subsequently synthesized from the reaction of calcium iodides, 1 and 2, with $\ce{KCH2SiMe3}$ in benzene at room temperature with 49 and 79% yields. Complexes 1−4 are characterized by NMR spectroscopy $[^1\text{H}, \, ^{13}\text{C}(^1\text{H})]$ and elemental analysis, the structures of 3 and 4 are further confirmed by single-crystal X-ray diffraction. The molecular structure of 4 is shown in Figure 1, while that of 3 is given in the Supporting Information. The structural features of 3 and 4 are very similar, and 4 is taken as the example. In 4, the calcium adopts a distorted square pyramidal geometry according to the $\tau$ value of 0.14, with the four nitrogen atoms of L2 forming the basal plane and a carbon

![](./images/812425606053494785_3.jpg)

Figure 1. Molecular structure of complex 4 with ellipsoids set at 30% probability level. Dipp isopropyl groups and hydrogen atoms are omitted for clarity. Selected bond distances [Å]: Ca−N1 2.3643(11), Ca−N2 2.3719(12), Ca−N3 2.5371(12), Ca−N4 2.5998(12), and Ca−C28 2.5079(14).

atom of the alkyl group in the apical position. The bond lengths of Ca−N3 and Ca−N4 [2.5371(12) and 2.5998(12) Å, respectively] are significantly longer than those of Ca−N1 and Ca−N2 [2.3643(11) and 2.3719(12) Å, respectively], as the N3 and N4 atoms are the neutral donors, while the N1 and N2 atoms act as the anionic ones. The Ca−C bond length is 2.5079(14) Å, which is similar to that in a calcium terminal alkyl complex {Ca[CH(SiMe₃)₂]₂(THF)₂} [2.4930(18) Å].²² This bond length is also close to that reported for a divalent ytterbium alkyl complex (L1YbCH₂SiMe₃) [2.510(4) Å],¹⁷ which is reasonable as the Ca²⁺ and Yb²⁺ ions have very similar ion radii. In the ¹H NMR spectra of 3 and 4 recorded in C₆D₆, the Ca−CH₂ appears as two broad signals at δ = −1.18 and −1.48 ppm for 3 and δ = −1.23 and −1.39 ppm for 4, indicating that the rotation of −CH₂SiMe₃ group in the complexes is hindered. The ¹³C(¹H) NMR spectra of 3 and 4 show the appearance of Ca−CH₂ signals at δ = 6.4 ppm for 3 and 6.5 ppm for 4.

Complex 3 reacts with PhSiH₃ at room temperature to yield complex 5 (Scheme 3), which is formed from an addition of

**Scheme 3. Reactions of Calcium Alkyl Complexes 3 and 4 with PhSiH₃**

$$
\begin{align*}
\ce{2\left[\begin{matrix}
\overset{\text{Dipp}}{N} & \underset{\text{N}}{N} \
| & | \
\ce{N} & \ce{Ca} - \ce{CH2SiMe3} \
| & | \
\ce{N} & \ce{N}
\end{matrix}\right]_3 + 2 PhSiH3 &->[\text{Hexane, r. t.}][-2 PhSiH2CH2SiMe3] \left[\begin{matrix}
\overset{\text{Dipp}}{N} & \underset{\text{N}}{N} & \underset{\text{H}}{Ca} & \underset{\text{N}}{N} & \overset{\text{N}}{N} \
| & | & | & | & | \
\ce{N} & \ce{Ca} & - & \ce{Ca} & \ce{N} \
| & | & | & | & | \
\ce{N} & \ce{N} & \underset{\text{H}}{N} & \ce{N} & \ce{N}
\end{matrix}\right]_5, 65\% \text{ yield}} \
\ce{2\left[\begin{matrix}
\overset{\text{Dipp}}{N} & \underset{\text{N}}{N} \
| & | \
\ce{N} & \ce{Ca} - \ce{CH2SiMe3} \
| & | \
\ce{N} & \ce{^{t}BuN}
\end{matrix}\right]_4 + 2 PhSiH3 &->[\text{Hexane, r. t.}][-2 PhSiH2CH2SiMe3] \left[\begin{matrix}
\overset{\text{Dipp}}{N} & \underset{\text{N}}{N} & \underset{\text{H}}{Ca} & \underset{\text{N}}{N} & \overset{\text{Dipp}}{N} \
| & | & | & | & | \
\ce{N} & \ce{Ca} & - & \ce{Ca} & \ce{N} \
| & | & | & | & | \
\ce{^{t}BuN} & \ce{N} & \underset{\text{H}}{N} & \ce{N} & \ce{^{t}BuN}
\end{matrix}\right]_6, 80\% \text{ yield}}
\end{align*}
$$

the Ca−H bond of the initially formed calcium hydride to one C═N bond of ligand L1. A similar addition has been previously observed in the reaction of an yttrium dimethyl complex containing the same supporting ligand [L1YMe₂] with PhSiH₃.²³ On the other hand, the reaction of complex 4 with PhSiH₃ gives a calcium hydride 6, indicating that the presence of a bulky tert-butyl group inhibits the addition of the Ca−H bond to C═N. Single crystals of 5 and 6 are obtained and analyzed by X-ray crystallography. The molecular structure of 5 is shown in Figure S2 in the Supporting Information, and the structural parameters of 5 are in line with the addition of H⁻ to the monoanionic ligand L1, which forms a dianionic ligand. Complex 6 exists as a dimer, in which each of the calcium ions is coordinated by four nitrogen atoms of L2 and two bridging hydrides (Figure 2). The Ca−H bond lengths, 2.25(3) and 2.21(3) Å, are comparable to those in a dimeric calcium hydride supported by the bulky bidentate ketiminato ligand [(Dipp-nacnac)CaH(THF)]₂ {Dipp-nacnac = [MeC(NDipp)-CHC(NDipp)Me]⁻, Dipp = 2,6-(ᵗPr)₂C₆H₃}, 2.09(4)−2.21(3) Å.²⁴ The ¹H NMR spectrum of 6 in C₆D₆ at 25 °C shows two sets of signals, indicating that there are two isomers in the solution. Some signals are broad and overlapped, but increasing the temperature from 25 to 75 °C results in the broadening and coalescence of the resonances followed by sharpening of the resulting coalesced signals. The Ca−H signal appears at δ = 4.74 ppm at 65 °C, close to that in [(Dipp- nacnac)CaH(THF)]₂ (4.45 ppm). The ¹H DOSY NMR experiments in C₆D₆ at 25 °C reveals that these two isomers are both dimers, which have the hydrodynamic radii of 6.75 Å (see the Supporting Information for details).

![](./images/812425606053494785_4.jpg)

**Figure 2.** Molecular structure of complex 6 with ellipsoids at 30% probability level. Dipp isopropyl groups and hydrogen atoms (except CaH and CaH′) are omitted for clarity. Selected bond distances [Å]: Ca−N1 2.417(2), Ca−N2 2.402(2), Ca−N3 2.607(2), Ca−N4 2.650(2), Ca−H 2.25(3), Ca−H′ 2.21(3), and Ca···Ca′ 3.574(1).

Catalytic Activity of Calcium Complexes. Although the divalent ytterbium alkyl complex [L1YbCH₂SiMe₃] and the calcium alkyl complex 3 catalyze the redistribution of PhSiH₃ to produce diarylsilane Ph₂SiH₂ as the main product by eliminating one SiH₄ molecule, the calcium alkyl complex 4 efficiently catalyzes the redistribution of PhSiH₃ to triarylsilane Ph₃SiH by eliminating two SiH₄ molecules (Table 1, entry 3 vs entries 1 and 2). When the reaction with 1 mol % of 4 is conducted in an open system under argon at 37 °C and stirred rapidly to facilitate the dissipation of SiH₄ gas, >99% of PhSiH₃ is consumed in 40 min and Ph₃SiH and Ph₂SiH₂ are produced in 57 and 41% yields, respectively. As the redistribution is reversible, the dissipation of volatile SiH₄ promotes the conversion of PhSiH₃ into products.¹⁷ Upon increasing the reaction time to 2 h, the generated Ph₂SiH₂ mostly converts into Ph₃SiH, and the yield of Ph₃SiH increases to 92%. The calcium hydride 6 shows a similar reactivity (slightly higher reactivity at the beginning), indicating that the hydride, which is generated from the reaction of the alkyl complex with arylsilane, is the real catalytic species in the catalytic cycle. Complex 4 can also efficiently catalyze the conversion of p-Ph- C₆H₄SiH₃ into triarylsilane (p-Ph-C₆H₄)₃SiH, with the yield of (p-Ph-C₆H₄)₃SiH being 84% in 2 h. Under the same reaction conditions, the electron-withdrawing −Cl- or −F-substituted arylsilanes rapidly undergo the redistribution reaction to give the triarylsilanes (95% yield for the −Cl-substituted substrate and 91% yield for the −F-substituted one in 40 min, Table 1, entries 6 and 7). The redistribution of p-Me-C₆H₄SiH₃ or p- OMe-C₆H₄SiH₃ is slower than that of PhSiH₃, which is related to the electronic effect of −Me and −OMe. Reactivity decrease induced by the electron-donating group at the para-position had also been observed in the divalent ytterbium complex- catalyzed arylsilane redistribution.¹⁷ This reactivity can be increased by increasing the reaction temperature as the reactions at 50 °C provide (p-Me-C₆H₄)₃SiH and (p-OMe- C₆H₄)₃SiH in 96 and 93% yields, respectively, in 3 h using 2 mol % of 4 as the catalyst (Table 1, entries 8 and 9). The reactivity of these arylsilanes follows the order Cl > F > H > Ph > Me > OMe, which is in line with that of their Hammett

**Table 1. Redistribution of $ArSiH_3$ to $Ar_3SiH$ and $SiH_4$**$^{a}$

$$\ce{R-C6H4-SiH3 -> [][} \left(\ce{R-C6H4-}\right)_3\ce{SiH + 2 SiH4}$$

<table>
  <thead>
    <tr>
      <th rowspan="2">entry</th>
      <th rowspan="2">cat</th>
      <th rowspan="2">$ArSiH_3$</th>
      <th colspan="2">40 min</th>
      <th colspan="2">2 h</th>
    </tr>
    <tr>
      <th>conv. (%)$^b$</th>
      <th>yield (%)$^b$</th>
      <th>conv. (%)$^b$</th>
      <th>yield (%)$^b$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>[Yb] (1%)$^c$</td>
      <td rowspan="4"><ce>C6H5-SiH3></td>
      <td>99</td>
      <td>25(73)$^d$</td>
      <td>99</td>
      <td>42(56)$^d$</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3 (1%)</td>
      <td>99</td>
      <td>9(89)$^d$</td>
      <td>99</td>
      <td>21(77)$^d$</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4 (1%)</td>
      <td>&gt;99</td>
      <td>57(41)$^d$</td>
      <td>&gt;99</td>
      <td>92</td>
    </tr>
    <tr>
      <td>4</td>
      <td>6 (0.5%)$^e$</td>
      <td>&gt;99</td>
      <td>68(31)$^d$</td>
      <td>&gt;99</td>
      <td>95</td>
    </tr>
    <tr>
      <td>5</td>
      <td>4 (1%)</td>
      <td><ce>Ph-C6H4-SiH3></td>
      <td>-</td>
      <td>-</td>
      <td>&gt;99</td>
      <td>84(16)$^d$</td>
    </tr>
    <tr>
      <td>6</td>
      <td>4 (1%)</td>
      <td><ce>Cl-C6H4-SiH3></td>
      <td>&gt;99</td>
      <td>95</td>
      <td>&gt;99</td>
      <td>97</td>
    </tr>
    <tr>
      <td>7</td>
      <td>4 (1%)</td>
      <td><ce>F-C6H4-SiH3></td>
      <td>&gt;99</td>
      <td>91(8)$^d$</td>
      <td>&gt;99</td>
      <td>94</td>
    </tr>
    <tr>
      <td>8$^f$</td>
      <td>4 (2%)</td>
      <td><ce>CH3-C6H4-SiH3></td>
      <td>&gt;99$^g$</td>
      <td>89$^g$(11)$^d$</td>
      <td>&gt;99$^h$</td>
      <td>96$^h$</td>
    </tr>
    <tr>
      <td>9$^f$</td>
      <td>4 (2%)</td>
      <td><ce>MeO-C6H4-SiH3></td>
      <td>&gt;99$^g$</td>
      <td>83$^g$(16)$^d$</td>
      <td>&gt;99$^h$</td>
      <td>93$^h$</td>
    </tr>
    <tr>
      <td>10$^f$</td>
      <td>4 (2%)</td>
      <td><ce>Me2N-C6H4-SiH3></td>
      <td>&gt;99$^g$</td>
      <td>6$^g$(93)$^d$</td>
      <td>&gt;99$^h$</td>
      <td>10$^h$(89)$^d$</td>
    </tr>
    <tr>
      <td>11$^f$</td>
      <td>4 (2%)</td>
      <td><ce>C6H4(CH3)-SiH3></td>
      <td>&gt;99$^g$</td>
      <td>95$^g$</td>
      <td>&gt;99$^h$</td>
      <td>99$^h$</td>
    </tr>
    <tr>
      <td>12</td>
      <td>4 (1%)</td>
      <td><ce>MeO-C6H4(CH3)-SiH3></td>
      <td>99</td>
      <td>43(53)$^d$</td>
      <td>&gt;99</td>
      <td>90</td>
    </tr>
    <tr>
      <td>13</td>
      <td>4 (1%)</td>
      <td><ce>n-C6H13-SiH3></td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

$^{a}$Reactions are conducted in an open system under argon with 1 or 2 mol % of catalyst in $C_6D_6$ at 37 °C, $[ArSiH_3]$ = 1.36 mol/L. $^{b}$Determined by $^1$H NMR spectroscopy using 1,3,5-trimethylbenzene as the internal standard. $^{c}$[Yb] = [L1YbCH$_2$SiMe$_3$]. $^{d}$The value in parenthesis is the yield of diarylsilane. $^{e}$Complex 6 is a dimer; therefore, 0.5 mol % of 6 is used. $^{f}$Reaction temperature is 50 °C. $^{g}$Reaction time is 120 min. $^{h}$Reaction time is 180 min.

constants Cl (0.23) > F (0.06) > H (0) > Ph (-0.01) > Me (-0.17) > OMe (-0.27).$^{25}$ When $p$-NMe$_2$-C$_6$H$_4$SiH$_3$ is the substrate, the reaction produces diarylsilane ($p$-NMe$_2$-C$_6$H$_4$)$_2$SiH$_2$ as the main product (Table 1, entry 10). The low reactivity of $p$-NMe$_2$-C$_6$H$_4$SiH$_3$ can be ascribed to the strong electron-donating property of $-$NMe$_2$, and the $-$NMe$_2$ group may also form a coordinate bond with the metal center and reduce the reactivity of the metal catalyst. Complex 4 also efficiently catalyzes the conversion of $m$-Me-C$_6$H$_4$SiH$_3$ and $o$-OMe-C$_6$H$_4$SiH$_3$ into corresponding triarylsilanes, ($m$-Me-C$_6$H$_4$)$_3$SiH and ($o$-OMe-C$_6$H$_4$)$_3$SiH (Table 1, entries 11 and 12). Under the same reaction conditions, alkylsilanes such as $n$-C$_6$H$_{13}$SiH$_3$ do not undergo the redistribution reaction to give the dialkylsilane or trialkylsilane (Table 1, entry 13).

The selective redistribution of aryl- and alkyl-substituted secondary silanes $Ar(alkyl)SiH_2$ to tertiary silanes $Ar_2(alkyl)$-SiH by eliminating $alkylSiH_3$ has not been reported before. Interestingly, calcium alkyl complex 4 is able to catalyze this reaction, and its catalytic activity is much higher than those of [L1YbCH$_2$SiMe$_3$] and calcium alkyl complex 3 (Table 2, entry 3 vs entries 1 and 2). In the presence of 1 mol % of 4, 92% of $Ph(Me)SiH_2$ is consumed and $Ph_2(Me)SiH$ is produced in 91% yield in 2 h when the reaction is conducted in an open system under an argon atmosphere at 37 °C and stirred rapidly to facilitate the dissipation of $MeSiH_3$ gas. The elimination of

**Table 2. Redistribution of $Ar(alkyl)SiH_2$ to $Ar_2(alkyl)SiH$ and $AlkylSiH_3$**$^{a}$

$$\ce{R-C6H4-Si(alkyl)H2 -> [][} \left(\ce{R-C6H4-}\right)_2\ce{Si(alkyl)H + alkylSiH3}$$

<table>
  <thead>
    <tr>
      <th rowspan="2">Entry</th>
      <th rowspan="2">Cat</th>
      <th rowspan="2">$Ar(alkyl)SiH_2$</th>
      <th colspan="2">40 min</th>
      <th colspan="2">2 h</th>
    </tr>
    <tr>
      <th>conv. (%)$^b$</th>
      <th>yield (%)$^b$</th>
      <th>conv. (%)$^b$</th>
      <th>yield (%)$^b$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>[Yb]</td>
      <td rowspan="2"><ce>C6H5-Si(Me)H2></td>
      <td>28</td>
      <td>27</td>
      <td>37</td>
      <td>36</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>13</td>
      <td>12</td>
      <td>18</td>
      <td>17</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4</td>
      <td><ce>C6H5-Si(Me)H2></td>
      <td>59</td>
      <td>58</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <td>4</td>
      <td>4</td>
      <td><ce>F-C6H4-Si(Me)H2></td>
      <td>85</td>
      <td>84</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <td>5</td>
      <td>4</td>
      <td><ce>Cl-C6H4-Si(Me)H2></td>
      <td>78$^c$</td>
      <td>77$^c$</td>
      <td>91$^d$</td>
      <td>89$^d$</td>
    </tr>
    <tr>
      <td>6</td>
      <td>4</td>
      <td><ce>F3C-C6H4-Si(Me)H2></td>
      <td>90$^c$</td>
      <td>89$^c$</td>
      <td>94$^d$</td>
      <td>93$^d$</td>
    </tr>
    <tr>
      <td>7</td>
      <td>4</td>
      <td><ce>Cl-C6H4(CH3)-Si(Me)H2></td>
      <td>97</td>
      <td>94</td>
      <td>99</td>
      <td>96</td>
    </tr>
    <tr>
      <td>8</td>
      <td>4</td>
      <td><ce>CH3-C6H4-Si(Me)H2></td>
      <td>36</td>
      <td>35</td>
      <td>86$^e$</td>
      <td>85$^e$</td>
    </tr>
    <tr>
      <td>9</td>
      <td>4</td>
      <td><ce>MeO-C6H4-Si(Me)H2></td>
      <td>34</td>
      <td>33</td>
      <td>83$^e$</td>
      <td>82$^e$</td>
    </tr>
    <tr>
      <td>10$^f$</td>
      <td>4</td>
      <td><ce>Me2N-C6H4-Si(Me)H2></td>
      <td>60$^g$</td>
      <td>59$^g$</td>
      <td>75$^e$</td>
      <td>74$^e$</td>
    </tr>
    <tr>
      <td>11$^f$</td>
      <td>4</td>
      <td><ce>C6H4(CH3)-Si(Me)H2></td>
      <td>51$^g$</td>
      <td>50$^g$</td>
      <td>67$^e$</td>
      <td>65$^e$</td>
    </tr>
    <tr>
      <td>12</td>
      <td>4</td>
      <td><ce>C6H5-Si(Et)H2></td>
      <td>50</td>
      <td>48</td>
      <td>84</td>
      <td>82</td>
    </tr>
  </tbody>
</table>

$^{a}$Reactions are conducted in an open system under argon with 1 mol % of catalyst in $C_6D_6$ at 37 °C, $[Ar(alkyl)SiH_2]$ = 1.36 mol/L. $^{b}$Determined by $^1$H NMR spectroscopy using 1,3,5-trimethylbenzene as the internal standard. $^{c}$Reaction time is 10 min. $^{d}$Reaction time is 20 min. $^{e}$Reaction time is 180 min. $^{f}$Reaction temperature is 50 °C and 5 mol % of catalyst is used. $^{g}$Reaction time is 120 min.

$MeSiH_3$ from the reaction is confirmed by the $^1$H NMR spectral monitoring of the reaction in a sealed NMR tube ($\delta$ = 3.58 ppm, 3H, $MeSiH_3$; $\delta$ = -0.12 ppm, 3H, $MeSiH_3$). Similar to that observed in the redistribution of $ArSiH_3$ to $Ar_3SiH$, introducing electron-withdrawing substituents, such as $-$F, $-$Cl, or $-$CF$_3$, at the para-position of Ar group increases the reactivity of $Ar(Me)SiH_2$ (Table 2, entries 4−6). The reaction of ($p$-F-C$_6$H$_4$)(Me)SiH$_2$ gives ($p$-F-C$_6$H$_4$)$_2$(Me)SiH in 84% yield in 40 min and 93% yield in 2 h. For the substrates with a $-$Cl or $-$CF$_3$ substituent, the reactions are even faster [89% yield of ($p$-Cl-C$_6$H$_4$)$_2$(Me)SiH and 93% yield of ($p$-CF$_3$-C$_6$H$_4$)$_2$(Me)SiH in 20 min]. ($m$-Cl-C$_6$H$_4$)(Me)SiH$_2$ also rapidly undergoes the redistribution reaction, providing 94% yield of ($m$-Cl-C$_6$H$_4$)$_2$(Me)SiH in 40 min. On the other hand, the substrates containing electron-donating substituents display lower reactivity (Table 2, entries 8−10), even though the redistribution of the substrates with $-$Me or $-$OMe substituent in the para-position provides the corresponding $Ar_2$(Me)SiH in 85 and 82% yields, respectively, in 3 h. For ($p$-NMe$_2$-C$_6$H$_4$)(Me)SiH$_2$, using an increased amount of 4 (5 mol %) and performing the reaction at an elevated temperature (50 °C), the tertiary silane can be obtained with 74% yield. The introduction of a methyl substituent at the ortho-position of Ar decreases the reactivity [with 5 mol % of 4, the reaction of ($o$-Me-C$_6$H$_4$)(Me)SiH$_2$ at 50 °C provides ($o$-Me-C$_6$H$_4$)$_2$(Me)SiH in 65% yield in 3 h]. In the presence of 4 (1 mol %), $Ph(Et)SiH_2$ also undergoes redistribution to

Table 3. Cross-Coupling between $Ar(Me)SiH_{2}$ and $Ar'(Me)SiH_{2}^{a,b}$

$$
\begin{aligned}
\mathrm{Me-SiH_{2}}_{\mathrm{R^1}} + \mathrm{Me-SiH_{2}}_{\mathrm{R^2}} &\longrightarrow \mathrm{Me-Si-H_{R^1}^{R^1SiR^2}} + \mathrm{MeSiH_3} \\
\mathrm{R^1Si}\quad 2.0\ \mathrm{equiv}\quad \mathrm{R^2Si} & \\
&\longrightarrow \mathrm{Me-Si-H_{R^1}^{R^1SiR^1}} + \mathrm{Me-Si-H_{R^2}^{R^2SiR^2}}
\end{aligned}
$$

<table>
  <thead>
    <tr>
      <th rowspan="2">entry</th>
      <th rowspan="2">substrate</th>
      <th rowspan="2">time (min)</th>
      <th colspan="3">yield (%)</th>
    </tr>
    <tr>
      <th>$R^{1}SiR^{2}$</th>
      <th>$R^{1}SiR^{1}$</th>
      <th>$R^{2}SiR^{2}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>$R^{1}=CF_{3},R^{2}=H$</td>
      <td>30</td>
      <td>89</td>
      <td>&lt;2</td>
      <td>18</td>
    </tr>
    <tr>
      <td>2</td>
      <td>$R^{1}=CF_{3},R^{2}=F$</td>
      <td>30</td>
      <td>82</td>
      <td>17</td>
      <td>45</td>
    </tr>
    <tr>
      <td>3</td>
      <td>$R^{1}=CF_{3},R^{2}=Me$</td>
      <td>30</td>
      <td>84</td>
      <td>&lt;2</td>
      <td>9</td>
    </tr>
    <tr>
      <td>4</td>
      <td>$R^{1}=CF_{3},R^{2}=OMe$</td>
      <td>30</td>
      <td>81</td>
      <td>&lt;2</td>
      <td>7</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$R^{1}=CF_{3},R^{2}=NMe_{2}$</td>
      <td>30</td>
      <td>59</td>
      <td>35</td>
      <td>&lt;2</td>
    </tr>
    <tr>
      <td>6</td>
      <td>$R^{1}=CF_{3},R^{2}=NMe_{2}$</td>
      <td>70</td>
      <td>96</td>
      <td>&lt;2</td>
      <td>&lt;2</td>
    </tr>
    <tr>
      <td>7</td>
      <td>$R^{1}=Cl,R^{2}=H$</td>
      <td>70</td>
      <td>81</td>
      <td>16</td>
      <td>49</td>
    </tr>
    <tr>
      <td>8</td>
      <td>$R^{1}=Cl,R^{2}=F$</td>
      <td>70</td>
      <td>72</td>
      <td>28</td>
      <td>65</td>
    </tr>
    <tr>
      <td>9</td>
      <td>$R^{1}=Cl,R^{2}=Me$</td>
      <td>70</td>
      <td>78</td>
      <td>18</td>
      <td>26</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$R^{1}=Cl,R^{2}=OMe$</td>
      <td>70</td>
      <td>73</td>
      <td>19</td>
      <td>22</td>
    </tr>
    <tr>
      <td>11</td>
      <td>$R^{1}=Cl,R^{2}=NMe_{2}$</td>
      <td>70</td>
      <td>58</td>
      <td>41</td>
      <td>&lt;2</td>
    </tr>
    <tr>
      <td>12</td>
      <td>$R^{1}=Cl,R^{2}=NMe_{2}$</td>
      <td>140</td>
      <td>73</td>
      <td>15</td>
      <td>&lt;2</td>
    </tr>
    <tr>
      <td>13</td>
      <td>$R^{1}=F,R^{2}=Me$</td>
      <td>140</td>
      <td>62</td>
      <td>38</td>
      <td>36</td>
    </tr>
    <tr>
      <td>14</td>
      <td>$R^{1}=F,R^{2}=OMe$</td>
      <td>140</td>
      <td>61</td>
      <td>35</td>
      <td>34</td>
    </tr>
  </tbody>
</table>

$^{a}$Reactions are conducted in an open system under argon with 2 mol % of catalyst [related to $Ar(Me)SiH_{2}$] in $C_{6}D_{6}$ for 30, 70, or 140 min at 37 °C, $[Ar(Me)SiH_{2}]=0.5$ mol/L, $[Ar'(Me)SiH_{2}]=1.0$ mol/L. $^{b}$The yields are determined by $^{1}$H NMR spectroscopy using 1,3,5-trimethylbenzene as the internal standard; the yields of $R^{1}SiR^{2}$ and $R^{1}SiR^{1}$ are calculated based on the amount of $R^{1}Si$ used, while those of $R^{2}SiR^{2}$ are based on the amount of $R^{2}Si$ used.

produce $Ph_{2}(Et)SiH$ by eliminating $EtSiH_{3}$ in 82% yield in 2 h at 37 °C (Table 2, entry 12).

Compared to the homo-coupling of $Ar(R)SiH_{2}$, the cross-coupling between two different $Ar(R)SiH_{2}$ is more challenging due to the easy homo-coupling side reactions. Fascinatingly, complex 4 is able to catalyze the cross-coupling of the electron-withdrawing $-CF_{3}$- or $-Cl$-substituted $Ar(Me)SiH_{2}$ with $-H$-, $-F$-, $-Me$-, $-OMe$-, or $-NMe_{2}$-substituted $Ar(Me)SiH_{2}$ to give the corresponding tertiary silanes, containing one alkyl and two different aryl groups, in good yields (72−96% yields) (Table 3, one of the substrates is used in 2.0 equiv). The cross-coupling of $(p-CF_{3}-C_{6}H_{4})(Me)SiH_{2}$ with $Ar(R)SiH_{2}$ containing $-H$, $-F$, $-Me$, or $-OMe$ at the para-position of Ar is also fast (with 2 mol % of 4 as the catalyst, the reactions at 37 °C provide the cross-coupling products in 81−89% yields in 30 min). On the other hand, the reaction of $(p-CF_{3}-C_{6}H_{4})(Me)SiH_{2}$ with $(p-NMe_{2}-C_{6}H_{4})(Me)SiH_{2}$ is slower, as $(p-CF_{3}-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)H$ is obtained in only 59% yield in 30 min. The slower reaction is in line with the lower reactivity of $(p-NMe_{2}-C_{6}H_{4})(Me)SiH_{2}$, being similar to that observed in the homocoupling of $(p-NMe_{2}-C_{6}H_{4})(Me)SiH_{2}$. A high yield of $(p-CF_{3}-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)H$ can be achieved by increasing the reaction time to 70 min, which gives the product in 96% yield. The yield of the homo-coupling product $(p-CF_{3}-C_{6}H_{4})_{2}Si(Me)H$ decreases from 35% to <2%; this is reasonable as the $Si-C_{Ar}$ bond of $(p-CF_{3}-C_{6}H_{4})_{2}Si(Me)H$ can be easily cleaved that enables $(p-CF_{3}-C_{6}H_{4})_{2}Si(Me)H$ to react with excess $(p-NMe_{2}-C_{6}H_{4})(Me)SiH_{2}$ in the system to yield $(p-CF_{3}-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)H$. The cross-coupling reactions of $(p-Cl-C_{6}H_{4})(Me)SiH_{2}$ with $-H$-, $-F$-, $-Me$-, or $-OMe$-substituted $Ar(Me)SiH_{2}$ afford the cross-coupling products in 72−81% yields in 70 min, and with $-NMe_{2}$-substituted $Ar(Me)SiH_{2}$ in 73% yield in 140 min. The selectivity for the cross-coupling of the $-F$-substituted $Ar(Me)SiH_{2}$ with $-Me$- or $-OMe$-substituted $Ar(Me)SiH_{2}$ is not high, providing the cross-coupling products in 62 and 61% yields in 140 min. This is reasonable as the difference in the electronic properties between $-F$ and $-Me$ or $-OMe$ is not significant; the Hammett constants of $-F$, $-Me$, and $-OMe$ are 0.06, −0.17, and −0.27, respectively.$^{25}$ The cross-coupling products $(p-CF_{3}-C_{6}H_{4})PhSi(Me)H$, $(p-CF_{3}-C_{6}H_{4})(p-Me-C_{6}H_{4})Si(Me)H$, $(p-CF_{3}-C_{6}H_{4})(p-OMe-C_{6}H_{4})Si(Me)H$, $(p-CF_{3}-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)H$, $(p-Cl-C_{6}H_{4})PhSi(Me)H$, $(p-Cl-C_{6}H_{4})(p-Me-C_{6}H_{4})Si(Me)H$, $(p-Cl-C_{6}H_{4})(p-OMe-C_{6}H_{4})Si(Me)H$, $(p-Cl-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)H$, $(p-F-C_{6}H_{4})(p-Me-C_{6}H_{4})Si(Me)H$, and $(p-F-C_{6}H_{4})(p-OMe-C_{6}H_{4})Si(Me)H$ are isolated and characterized by NMR spectroscopy ($^{1}$H, $^{13}$C, $^{19}$F, and $^{29}$Si) and high-resolution mass spectrometry (see the Supporting Information for details).

Further Transformation of the Cross-Coupling Product. The cross-coupling product has one reactive $Si-H$ bond and therefore may react further. To demonstrate this possibility, the cross-coupling of $(p-CF_{3}-C_{6}H_{4})(Me)SiH_{2}$ with $(p-NMe_{2}-C_{6}H_{4})(Me)SiH_{2}$ is scaled up to gram scale, and $(p-CF_{3}-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)H$ is obtained and tested for further transformation. First, $(p-CF_{3}-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)H$ is treated with $H_{2}O$ in THF at room temperature using 0.3 mol % of $[RhCl(CO)_{2}]_{2}$ as a catalyst. After 30 min, $(p-CF_{3}-C_{6}H_{4})(p-NMe_{2}-C_{6}H_{4})Si(Me)OH$ is obtained in 91% yield, in which $-H$ is selectively replaced by $-OH$ (Scheme 4). Accordingly, treatment of $(p-CF_{3}-$

Scheme 4. Transformation of $(p\text{-CF}_3\text{-C}_6\text{H}_4)(p\text{-NMe}_2\text{-C}_6\text{H}_4)\text{Si(Me)H}$ into Other Organosilicon Compounds

$$
\small
\begin{matrix}
\ce{F3C-C6H4-Si(Me)(H)-C6H4-NMe2} &
\begin{cases}
\ce{->[H2O][0.3 mol\% [RhCl(CO)2]2, THF, r. t., 30 min]} & \ce{F3C-C6H4-Si(Me)(OH)-C6H4-NMe2} \
& 91\% \
\ce{->[EtOH][5 mol\% KN(SiMe3)2, toluene, r. t., 6 h]} & \ce{F3C-C6H4-Si(Me)(OEt)-C6H4-NMe2} \
& 95\% \
\ce{->[LiNEt2][toluene, 75 ^\circ C, 24 h]} & \ce{F3C-C6H4-Si(Me)(NEt2)-C6H4-NMe2} \
& 95\% \
\ce{->[LiCH2SiMe3][benzene, 75 ^\circ C, 24 h]} & \ce{F3C-C6H4-Si(Me)(CH2SiMe3)-C6H4-NMe2} \
& 90\%
\end{cases}
\end{matrix}
$$

![](./images/812425606053494785_5.jpg)

Figure 3. Computed enthalpy profile at the DFT (B3PW91) level for the redistribution reaction of $\text{Ph(Me)SiH}_2$ catalyzed by 4. Energy values are shown in kcal/mol. Gibbs free energy is given within brackets.

$\text{C}_6\text{H}_4)(p\text{-NMe}_2\text{-C}_6\text{H}_4)\text{Si(Me)H}$ with EtOH in toluene for 6 h in the presence of 5 mol % of $\text{KN(SiMe}_3\text{)}_2$ produces $(p\text{-CF}_3\text{-C}_6\text{H}_4)(p\text{-NMe}_2\text{-C}_6\text{H}_4)\text{Si(Me)OEt}$ in 95% yield. $(p\text{-CF}_3\text{-C}_6\text{H}_4)(p\text{-NMe}_2\text{-C}_6\text{H}_4)\text{Si(Me)H}$ also reacts with $\text{LiNEt}_2$ in toluene at $75\ ^\circ\text{C}$ to give $(p\text{-CF}_3\text{-C}_6\text{H}_4)(p\text{-NMe}_2\text{-C}_6\text{H}_4)\text{Si(Me)NEt}_2$ in 95% yield in 24 h. It also reacts with $\text{LiCH}_2\text{SiMe}_3$ in benzene at $75\ ^\circ\text{C}$ to provide $(p\text{-CF}_3\text{-C}_6\text{H}_4)(p\text{-NMe}_2\text{-C}_6\text{H}_4)\text{Si(Me)CH}_2\text{SiMe}_3$ in 90% yield in 24 h.

DFT Calculations. In order to get insights into the reaction mechanism, DFT calculations (B3PW91) were carried out on the redistribution reaction of a typical secondary silane $\text{Ph(Me)SiH}_2$ in the presence of complex 4 (Figure 3). The redistribution process begins by $\text{Si-H}$ activation of $\text{Ph(Me)SiH}_2$ by complex 4. The other transition states were computed, namely, $\text{Si-H}$ activation with silicon at the $\alpha$ position and $\text{Si-C}$ activation with silicon at the $\beta$ position (see Figures S167 and S168 in the Supporting Information) and are found to be higher in energy by 5.6 and 36.6 kcal/mol, respectively, so that they can be discarded. After the formation of a silane adduct (almost athermic, 1.8 kcal/mol), a $\text{Si-H}$ $\sigma$-bond metathesis transition state with silicon at the $\beta$ position is achieved. The associated activation barrier is 19.1 kcal/mol, indicating a kinetically accessible step. The geometry around the silicon is a slightly distorted trigonal bipyramid (TBP) with the exchanged hydrogen and alkyl groups occupying the equatorial and apical positions, respectively. Interestingly, the alkyl group is

reoriented with an elongated ${\rm Ca{-}C}$ bond (2.58 Å) in order to have the lone pair pointing toward the calcium atom, and the interaction between the calcium and the alkyl group is ensured by a strong $\alpha$-agostic interaction. The ${\rm Ca{-}H}$ bond is not yet formed (2.49 Å) and the activated ${\rm Si{-}H}$ one is elongated (from 1.49 to 1.59 Å) as the hydrogen interacts with Ca (Ca–H distance, 2.27 Å). Following the intrinsic reaction coordinate, it yields the calcium hydride (whose dimerization is computed to be favorable by 13.2 kcal/mol, but that is quite unlikely to occur under catalytic conditions due to the low concentration of the formed hydride and also because the dimerization barrier is computed to be 15.5 kcal/mol) with the release of the tertiary silane $({\rm Ph})({\rm Me}){\rm Si(H)(CH_2SiMe_3)}$ that is observed experimentally. This step is exothermic by 4.7 kcal/mol. The formed hydride can thus react with another molecule of ${\rm Ph(Me)SiH_2}$ (see also Figure S169). The reaction begins by the formation of a stable silane adduct (−6.2 kcal/mol). Rather than the unproductive ${\rm Si{-}H}$ activation (H/H exchange), the system undergoes a ${\rm Si{-}C}$ activation reaction. Such a reaction was also reported to be kinetically accessible and favored over ${\rm Si{-}H}$ activation with the silicon at the $\alpha$ position by Perrin et al. in their study of hydrosilylation of alkene catalyzed by ${\rm Cp_2^*SmH.^{26}}$ The associated transition state is again an $\sigma$-bond metathesis one with the silicon at the $\beta$ position. The geometry is also a slightly distorted TBP around the silicon where the hydride lies in the equatorial plane and the phenyl ring is in the apical position. The ${\rm Si{-}H}$ bond almost formed (1.67 Å), while the $\ce{Ca{\cdots}C}$ distance remains long (3.04 Å). However, the *ipso* carbon of the phenyl ring is bent in the direction of the calcium indicating that although small, an interaction exists between the two centers. The barrier is slightly lower than the first one (17.4 kcal/mol) in line with a kinetically accessible step. The system further evolves with the formation of a calcium phenyl complex and the liberation of ${\rm MeSiH_3}$ that is observed experimentally, and whose formation is exothermic by 5.4 kcal/mol from the entrance channel (almost athermic +0.8 kcal/mol from calcium hydride formation). Finally, the calcium phenyl complex reacts with a molecule of silane ${\rm Ph(Me)SiH_2}$. After weak coordination of silane (0.1 kcal/mol), the system reaches a ${\rm Si{-}H}$ activation transition state (TS) with silicon at the $\beta$ position. This TS has similar features as those of the Si–C activation one which was just described above. Indeed, the hydrogen lies in the equatorial plane, whereas the phenyl is in the apical position. The ${\rm Si{-}H}$ bond is elongated to 1.63 Å allowing a ${\rm Ca{-}H}$ interaction at 2.26 Å. The Ca–phenyl distance has also been strongly elongated to 2.93 Å (2.47 Å in the calcium phenyl complex) but remains bent toward Ca. The second phenyl ring lies in the equatorial plane, whereas the *ipso* methyl is in the apical position. The associated barrier is 19.1 kcal/mol, which is similar to the first barrier, indicating that the hydride formation, which is the actual catalyst, is the rate-determining step of the reaction. Following the intrinsic reaction coordinate, it yields the silane distribution product ${\rm SiH(Me)(Ph)_2}$ and regenerates the calcium hydride. The overall redistribution reaction is exothermic by 9.1 kcal/mol. The substituent effect has been investigated by computing the redistribution reaction for $(p{\rm -CF_3{-}C_6H_4})({\rm Me}){\rm SiH_2}$ (Table 2, entry 6). The computed reaction profile (Figure S170) is quite similar to that reported for ${\rm PhSi(Me)H_2}$ (Figure 3), but the energies are found to be lower. Following the Curtin–Hammett principle, since the rate-determining step of the reaction is the last step (redistribution TS), the difference in the activity of the two substrates only depends on the TS energies (13.6 for ${\rm R' = }$ $p$-H vs 9.5 kcal/mol for ${\rm R' = }$ $p$-${\rm CF_3}$) so that the activity for the latter is greater than that of the former.

## CONCLUSIONS
In summary, organocalcium complexes supported on a $\beta$-diketiminato-based tetradentate ligand (L1 or L2) are synthesized and structurally characterized, and their application as catalysts for the redistribution of hydrosilanes is explored. The supporting ligands L1 and L2 can both stabilize the calcium alkyl complex, while for calcium hydride, only the one with L2 which contains a bulky *tert*-butyl group is obtained. The calcium alkyl complex supported by L2 efficiently catalyzes the redistribution of ${\rm ArSiH_3}$ or Ar(alkyl)-${\rm SiH_2}$ to ${\rm Ar_3SiH}$ and ${\rm SiH_4}$ or ${\rm Ar_2(alkyl)SiH}$ and ${\rm alkylSiH_3}$, respectively, and its catalytic performance is much better than those of the calcium alkyl complex supported by L1 and a reported divalent ytterbium alkyl complex. This calcium alkyl complex also catalyzes the cross-coupling between the electron-withdrawing, substituted ${\rm Ar(R)SiH_2}$ and the electron-donating, substituted ${\rm Ar'(R)SiH_2}$ to provide ArAr'(alkyl)-SiH in good yields, and the synthesized ArAr'(alkyl)SiH can be easily transferred to other organosilicon compounds based on its ${\rm Si{-}H}$ bond transformation. Therefore, this protocol provides new opportunities to synthesize various arylsilanes. Both experimental and theoretical studies indicate that calcium hydride is the real catalytic species in the catalytic cycle. The reaction sequence is demonstrated to involve three steps (catalyst formation, Ca–Ph formation, and catalyst regeneration) which exhibit similar low activation barriers (17–19 kcal/mol) in line with a facile reaction.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acscatal.1c00463.
Experimental and computational details and X-ray crystallography structure data (PDF)
Crystallographic information on complex 3 (CCDC 2043282) (CIF)
Crystallographic information on complex 4 (CCDC 2043283) (CIF)
Crystallographic information on complex 5 (CCDC 2043284) (CIF)
Crystallographic information on complex 6 (CCDC 2043285) (CIF)

## AUTHOR INFORMATION

### Corresponding Authors
Laurent Maron – LPCNO, CNRS & INSA, Université Paul Sabatier, Toulouse 31077, France; orcid.org/0000-0003-2653-8557; Email: laurent.maron@irsamc.ups-tlse.fr
Yaofeng Chen – State Key Laboratory of Organometallic Chemistry, Shanghai Institute of Organic Chemistry, University of Chinese Academy of Sciences, Chinese Academy of Sciences, Shanghai 200032, People's Republic of China; orcid.org/0000-0003-4664-8980; Email: yaofchen@mail.sioc.ac.cn

### Authors
Tao Li – State Key Laboratory of Organometallic Chemistry, Shanghai Institute of Organic Chemistry, University of

Chinese Academy of Sciences, Chinese Academy of Sciences,
Shanghai 200032, People's Republic of China
Karl N. McCabe – LPCNO, CNRS & INSA, Université Paul
Sabatier, Toulouse 31077, France
Xuebing Leng – State Key Laboratory of Organometallic
Chemistry, Shanghai Institute of Organic Chemistry,
University of Chinese Academy of Sciences, Chinese Academy
of Sciences, Shanghai 200032, People's Republic of China;
orcid.org/0000-0003-3291-8695

Complete contact information is available at:
https://pubs.acs.org/10.1021/acscatal.1c00463

## Author Contributions
The manuscript was written through contributions of all
authors. All authors have given approval to the final version of
the manuscript.

## Notes
The authors declare no competing financial interest.
Caution: $SiH_4$ and $MeSiH_3$ are pyrophoric.
Crystallographic data can be obtained free of charge via www.
ccdc.cam.ac.uk/data_request/cif, or by emailing data_
request@ccdc.cam.ac.uk, or by contacting The Cambridge
Crystallographic Data Centre, 12 Union Road, Cambridge
CB21EZ, UK; fax: +44 1223336033.

## ACKNOWLEDGMENTS
This work was supported by the National Natural Science
Foundation of China (nos. 21732007, 21890721, and
21821002), K. C. Wong Education Foundation, the Strategic
Priority Research Program of the Chinese Academy of
Sciences (grant no. XDB20000000), Shanghai Municipal
Committee of Science and Technology, and the Program of
Shanghai Academic Research Leader. L.M. is a senior member
of the Institut Universitaire de France. L.M. acknowledges the
Chinese Academy of Sciences President's International
Fellowship Initiative. CalMip is finally acknowledged for a
generous grant of computing time.

## REFERENCES
(1) Beckmann, E. Einige Anwendungen von metallischem Calcium.
Ber. Dtsch. Chem. Ges. 1905, 38, 904−906.

(2) Westerhausen, M.; Gärtner, M.; Fischer, R.; Langer, J. Aryl
Calcium Compounds: Syntheses, Structures, Physical Properties, and
Chemical Behavior. Angew. Chem., Int. Ed. 2007, 46, 1950−1956.

(3) Harder, S. From Limestone to Catalysis: Application of Calcium
Compounds as Homogeneous Catalysts. Chem. Rev. 2010, 110,
3852−3876.

(4) Hill, M. S.; Liptrot, D. J.; Weetman, C. Alkaline Earths as Main
Group Reagents in Molecular Catalysis. Chem. Soc. Rev. 2016, 45,
972−988.

(5) Mukherjee, D.; Schuhknecht, D.; Okuda, J. Hydrido Complexes
of Calcium: A New Family of Molecular Alkaline-Earth-Metal
Compounds. Angew. Chem., Int. Ed. 2018, 57, 9590−9602.

(6) (a) Buch, F.; Brettar, J.; Harder, S. Hydrosilylation of Alkenes
with Early Main−Group Metal Catalysts. Angew. Chem., Int. Ed. 2006,
45, 2741−2745. (b) Spielmann, J.; Buch, F.; Harder, S. Early Main−
Group Metal Catalysts for the Hydrogenation of Alkenes with H2.
Angew. Chem., Int. Ed. 2008, 47, 9434−9438. (c) Bauer, H.; Alonso,
M.; Färber, C.; Elsen, H.; Pahl, J.; Causero, A.; Ballmann, G.; De
Proft, F.; Harder, S. Imine hydrogenation with simple alkaline earth
metal catalysts. Nat. Catal. 2018, 1, 40−47. (d) Bauer, H.; Alonso,
M.; Fischer, C.; Rösch, B.; Elsen, H.; Harder, S. Simple Alkaline−
Earth Metal Catalysts for Effective Alkene Hydrogenation. Angew.
Chem., Int. Ed. 2018, 57, 15177−15182. (e) Martin, J.; Knüpfer, C.;
Eyselein, J.; Färber, C.; Grams, S.; Langer, J.; Thum, K.; Wiesinger,
M.; Harder, S. Highly Active Superbulky Alkaline Earth Metal Amide
Catalysts for Hydrogenation of Challenging Alkenes and Aromatic
Rings. Angew. Chem., Int. Ed. 2020, 59, 9102−9112.
(7) (a) Crimmin, M. R.; Casely, I. J.; Hill, M. S. Calcium-Mediated
Intramolecular Hydroamination Catalysis. J. Am. Chem. Soc. 2005,
127, 2042−2043. (b) Barrett, A. G. M.; Boorman, T. C.; Crimmin, M.
R.; Hill, M. S.; Kociok-Köhn, G.; Procopiou, P. A. Heavier group 2
element-catalysed hydroamination of isocyanates. Chem. Commun.
2008, 5206−5208. (c) Crimmin, M. R.; Arrowsmith, M.; Barrett, A.
G. M.; Casely, I. J.; Hill, M. S.; Procopiou, P. A. Intramolecular
Hydroamination of Aminoalkenes by Calcium and Magnesium
Complexes: A Synthetic and Mechanistic Study. J. Am. Chem. Soc.
2009, 131, 9670−9685. (d) Barrett, A. G. M.; Brinkmann, C.;
Crimmin, M. R.; Hill, M. S.; Hunt, P.; Procopiou, P. A. Heavier
Group 2 Metals and Intermolecular Hydroamination: A Computa-
tional and Synthetic Assessment. J. Am. Chem. Soc. 2009, 131, 12906−
12907. (e) Hill, M. S.; Liptrot, D. J.; MacDougall, D. J.; Mahon, M.
F.; Robinson, T. P. Hetero-dehydrocoupling of silanes and amines by
heavier alkaline earth catalysis. Chem. Sci. 2013, 4, 4212−4222.
(f) Bellham, P.; Hill, M. S.; Kociok-Köhn, G.; Liptrot, D. J. Bespoke
synthesis of unsymmetrical diaminoboranes by alkaline earth catalysis.
Chem. Commun. 2013, 49, 1960−1962. (g) Arrowsmith, M.; Hill, M.
S.; Kociok-Köhn, G. Group 2 Catalysis for the Atom−Efficient
Synthesis of Imidazolidine and Thiazolidine Derivatives. Chem.—Eur.
J. 2015, 21, 10548−10557. (h) Liptrot, D. J.; Hill, M. S.; Mahon, M.
F.; Wilson, A. S. S. Alkaline−Earth−Catalyzed Dehydrocoupling of
Amines and Boranes. Angew. Chem., Int. Ed. 2015, 54, 13362−13365.
(i) Morris, L. J.; Hill, M. S.; Mahon, M. F.; Manners, I.; McMenamy,
F. S.; Whittell, G. R. Heavier Alkaline-Earth Catalyzed Dehydrocou-
pling of Silanes and Alcohols for the Synthesis of Metallo−
Polysilylethers. Chem.—Eur. J. 2020, 26, 2954−2966.
(8) (a) Jochmann, P.; Davin, J. P.; Spaniol, T. P.; Maron, L.; Okuda,
J. A Cationic Calcium Hydride Cluster Stabilized by Cyclen−Derived
Macrocyclic N,N,N,N-Ligands. Angew. Chem., Int. Ed. 2012, 51,
4452−4455. (b) Leich, V.; Spaniol, T. P.; Maron, L.; Okuda, J.
Hydrosilylation catalysis by an earth alkaline metal silyl: synthesis,
characterization, and reactivity of bis(triphenylsilyl)calcium. Chem.
Commun. 2014, 50, 2311−2314. (c) Schuhknecht, D.; Lhotzky, C.;
Spaniol, T. P.; Maron, L.; Okuda, J. Calcium Hydride Cation [CaH]+
Stabilized by an NNNN-type Macrocyclic Ligand: A Selective
Catalyst for Olefin Hydrogenation. Angew. Chem., Int. Ed. 2017, 56,
12367−12371. (d) Schuhknecht, D.; Spaniol, T. P.; Maron, L.;
Okuda, J. Regioselective Hydrosilylation of Olefins Catalyzed by a
Molecular Calcium Hydride Cation. Angew. Chem., Int. Ed. 2020, 59,
310−314.
(9) (a) Al-Shboul, T. M. A.; Görls, H.; Westerhausen, M. Calcium-
mediated hydrophosphination of diphenylethyne and diphenylbuta-
diyne as well as crystal structure of 1,4-diphenyl-1,4-bis-
(diphenylphosphanyl)buta-1,3-diene. Inorg. Chem. Commun. 2008,
11, 1419−1421. (b) Al-Shboul, T. M. A.; Pálfi, V. K.; Yu, L.;
Kretschmer, R.; Wimmer, K.; Fischer, R.; Görls, H.; Reiher, M.;
Westerhausen, M. Catalytic synthesis of vinylphosphanes via calcium-
mediated intermolecular hydrophosphanylation of alkynes and
butadiynes. J. Organomet. Chem. 2011, 696, 216−227. (c) Ziemann,
S.; Krieck, S.; Görls, H.; Westerhausen, M. 1,2-Bis(anilido)ethane
Complexes of Calcium and Potassium: Synthesis, Structures, and
Catalytic Activity. Organometallics 2018, 37, 924−933. (d) Neal, S. R.;
Ellern, A.; Sadow, A. D. Optically active, bulky tris(oxazolinyl)borato
magnesium and calcium compounds for asymmetric hydroamination/
cyclization. J. Organomet. Chem. 2011, 696, 228−234. (e) Liu, B.;
Roisnel, T.; Carpentier, J.-F.; Sarazin, Y. When Bigger Is Better:
Intermolecular Hydrofunctionalizations of Activated Alkenes Cata-
lyzed by Heteroleptic Alkaline Earth Complexes. Angew. Chem., Int.
Ed. 2012, 51, 4943−4946. (f) Liu, B.; Carpentier, J.-F.; Sarazin, Y.
Highly Effective Alkaline Earth Catalysts for the Sterically Governed
Hydrophosphonylation of Aldehydes and Nonactivated Ketones.
Chem.—Eur. J. 2012, 18, 13259−13264. (g) Liu, B.; Roisnel, T.;
Carpentier, J.-F.; Sarazin, Y. Cyclohydroamination of Aminoalkenes

Catalyzed by Disilazide Alkaline-Earth Metal Complexes: Reactivity Patterns and Deactivation Pathways. *Chem.—Eur. J.* **2013**, *19*, 2784–2802. (h) Sarazin, Y.; Carpentier, J.-F. Calcium, Strontium and Barium Homogeneous Catalysts for Fine Chemicals Synthesis. *Chem. Rec.* **2016**, *16*, 2482–2505. (i) Shi, X.; Hou, C.; Zhao, L.; Deng, P.; Cheng, J. Mononuclear calcium complex as effective catalyst for alkenes hydrogenation. *Chem. Commun.* **2020**, *56*, 5162–5165.

(10) (a) Brook, M. A. *Silicon in Organic, Organometallic, and Polymer Chemistry*; Wiley: New York, 2000. (b) *The Chemistry of Organic Silicon Compounds*; Patai, S., Rappoport, Z., Eds.; Wiley: Chichester, 1989; Vol. 1. (c) *The Chemistry of Organic Silicon Compounds*; Rappoport, Z., Apeloig, Y., Eds.; Wiley: Chichester, 1998; Vol. 2.

(11) Curtis, M. D.; Epstein, P. S. Redistribution Reactions on Silicon Catalyzed by Transition Metal Complexes. *Adv. Organomet. Chem.* **1981**, *19*, 213–255.

(12) (a) Radu, N. S.; Hollander, F. J.; Tilley, T. D.; Rheingold, A. L. Samarium-mediated redistribution of silanes and formation of trinuclear samarium−silicon clusters. *Chem. Commun.* **1996**, 2459–2460. (b) Castillo, I.; Tilley, T. D. Mechanistic Aspects of Samarium-Mediated $\sigma$-Bond Activations of Arene C−H and Arylsilane Si−C Bonds. *J. Am. Chem. Soc.* **2001**, *123*, 10526–10534. (c) Sadow, A. D.; Tilley, T. D. Enhanced Reactivity of Cationic vs Neutral Hafnocene Complexes in Stoichiometric and Catalytic $\sigma$-Bond Metathesis Reactions Involving Si−H and Si−C Bonds. *Organometallics* **2001**, *20*, 4457–4459. (d) Castillo, I.; Tilley, T. D. Organolutetiurn Complexes in $\sigma$-Bond Metathesis Reactions Involving Silicon. Catalysts for the Hydrogenolysis of Si−C Bonds. *Organometallics* **2001**, *20*, 5598–5605. (e) Mucha, N. T.; Waterman, R. Iridium Pincer Catalysts for Silane Dehydrocoupling: Ligand Effects on Selectivity and Activity. *Organometallics* **2015**, *34*, 3865–3872.

(13) (a) Tilley, T. D. The coordination polymerization of silanes to polysilanes by a “.sigma.-bond metathesis” mechanism. Implications for linear chain growth. *Acc. Chem. Res.* **1993**, *26*, 22–29. (b) Gauvin, F.; Harrod, J. F.; Woo, H. G. Catalytic Dehydrocoupling: A General Strategy for the Formation of Element−Element Bonds. *Adv. Organomet. Chem.* **1998**, *42*, 363–405. (c) Corey, J. Y. Dehydrocoupling of Hydrosilanes to Polysilanes and Silicon Oligomers: A 30 Year Overview. *Adv. Organomet. Chem.* **2004**, *51*, 1–52.

(14) (a) Speier, J. L.; Zimmerman, R. E. Disproportionation of Phenylsilanes with Aluminum Chloride as the Catalyst. *J. Am. Chem. Soc.* **1955**, *77*, 6395–6396. (b) Sangtrirutnugul, P.; Tilley, T. D. Silyl Derivatives of [Bis(8-quinolyl)methylsilyl]iridium(III) Complexes: Catalytic Redistribution of Arylsilanes and Dehydrogenative Arene Silylation. *Organometallics* **2007**, *26*, 5557–5568. (c) Hao, J.; Vabre, B.; Zargarian, D. Reactions of Phenylhydrosilanes with Pincer−Nickel Complexes: Evidence for New Si−O and Si−C Bond Formation Pathways. *J. Am. Chem. Soc.* **2015**, *137*, 15287–15298.

(15) Sakakura, T.; Kumberger, O.; Tan, R. P.; Arthur, M.-P.; Tanaka, M. Ruthenium Complex-catalysed Selective Redistribution Reaction of Aryltrihydrosilanes and Desilanative Polymerization of Bis(trihydrosilyl)benzenes. *J. Chem. Soc., Chem. Commun.* **1995**, 193–194.

(16) Ma, Y.; Zhang, L.; Luo, Y.; Nishiura, M.; Hou, Z. B(C₆F₅)₃-Catalyzed C−Si/Si−H Cross-Metathesis of Hydrosilanes. *J. Am. Chem. Soc.* **2017**, *139*, 12434–12437.

(17) Liu, X.; Xiang, L.; Louyriac, E.; Maron, L.; Leng, X.; Chen, Y. Divalent Ytterbium Complex-Catalyzed Homo- and Cross-Coupling of Primary Arylsilanes. *J. Am. Chem. Soc.* **2019**, *141*, 138–142.

(18) Guo, C.; Li, M.; Chen, J.; Luo, Y. Highly selective redistribution of primary arylsilanes to secondary arylsilanes catalyzed by Ln-(CH2C6H4NMe2-o)3@SBA-15. *Chem. Commun.* **2020**, *56*, 117–120.

(19) Liu, Z.; Shi, X.; Cheng, J. Selective homo- and cross-desilacoupling of aryl and benzyl primary silanes catalyzed by a barium complex. *Dalton Trans.* **2020**, *49*, 8340–8346.

(20) Itoh, M.; Inoue, K.; Ishikawa, J.-i.; Iwata, K. Disproportionation Reactions of Organohydrosilanes in The Presence of Base Catalysts. *J. Organomet. Chem.* **2001**, *629*, 1–6.

(21) Shannon, R. D. Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides. *Acta Crystallogr., Sect. A: Cryst. Phys., Diffr., Theor. Gen. Crystallogr.* **1976**, *32*, 751–767.

(22) Crimmin, M. R.; Barrett, A. G. M.; Hill, M. S.; MacDougall, D. J.; Mahon, M. F.; Procopiou, P. A. Bis(trimethylsilyl)methyl Derivatives of Calcium, Strontium and Barium: Potentially Useful Dialkyls of the Heavy Alkaline Earth Elements. *Chem.—Eur. J.* **2008**, *14*, 11292–11295.

(23) Zhou, J.; Chu, J.; Zhang, Y.; Yang, G.; Leng, X.; Chen, Y. An Yttrium Hydride−Silane Complex as a Structural Model for a $\sigma$-Bond Metathesis Transition State. *Angew. Chem., Int. Ed.* **2013**, *52*, 4243–4246.

(24) Harder, S.; Brettar, J. Rational Design of a Well-Defined Soluble Calcium Hydride Complex. *Angew. Chem., Int. Ed.* **2006**, *45*, 3474–3478.

(25) Hansch, C.; Leo, A.; Taft, R. W. A survey of Hammett substituent constants and resonance and field parameters. *Chem. Rev.* **1991**, *91*, 165–195.

(26) Perrin, L.; Maron, L.; Eisenstein, O.; Tilley, T. D. Bond Activations of PhSiH₃ by Cp₂SmH: A Mechanistic Investigation by the DFT Method. *Organometallics* **2009**, *28*, 3767–3775.