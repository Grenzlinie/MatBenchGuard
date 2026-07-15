# Why $[(\eta^5\text{-}C_5Me_nH_{5-n})_2Ti]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ Can Not Add a $H_2$ Molecule to the Side-On-Coordinated $N_2$ while Its Zr and Hf Analogues Can? Insights from Computational Studies

Djamaladdin G. Musaev,* Petia Bobadova-Parvanova, and Keiji Morokuma

Cherry L. Emerson Center for Scientific Computation and Department of Chemistry,
Emory University, Atlanta, Georgia 30322

Received December 15, 2006

The potential energy surface of the reaction $[(\eta^5\text{-}C_5Me_nH_{5-n})_2M]_2(\mu_2,\eta^2,\eta^2\text{-}N_2) + H_2 \to [(\eta^5\text{-}C_5Me_nH_{5-n})_2M][(\eta^5\text{-}C_5Me_nH_{5-n})_2MH](\mu_2,\eta^2,\eta^2\text{-}NNH)$ at low-lying singlet and triplet electronic states of the reactants was investigated using density functional methods, for $n = 0$ and 4, and $M =$ Ti, Zr, and Hf. Ground electronic states of the Ti complexes are found to be triplet states, while that for the corresponding Zr and Hf complexes are singlet states. In their singlet state, all these complexes satisfy known necessary conditions (they have a side-on-coordinated $N_2$ molecule and appropriate frontier orbitals) for successful addition of an $H_2$ molecule to the coordinated $N_2$, and consequently, add of an $H_2$ molecule with a reasonable energy barrier. Hf complexes show slightly higher reactivity than corresponding Zr complexes, and in turn, both are more reactive than their singlet-state Ti counterparts. The calculated trend in reactivity of Zr and Hf complexes is consistent with the latest experimental data (see refs 13 and 16). However, Ti complexes have the *ground* triplet state that lacks in appropriate frontier orbitals. As a result, $H_2$ addition to the Ti complexes at their triplet ground states requires a larger activation barrier than the singlet state and is endothermic (lacks of driven force for reaction). On the basis of these results, we predict that the $[(\eta^5\text{-}C_5Me_4H)_2M]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ and $[(\eta^5\text{-}C_5H_5)_2M]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ complexes cannot react with an $H_2$ molecule for $M =$ Ti, while those for $M =$ Zr and Hf can. It was shown that the difference in the B3LYP (hybrid) and PBE (nonhybrid) calculated energy gaps between the lowest closed-shell singlet and triplet states of the present complexes reduces via first- > second- > third-row transition metals; both hybrid and nonhybrid density functionals can be safely used to describe reactivity of the low-lying low-spin and high-spin states of second- and third-row transition metal complexes.

## 1. Introduction

The design of novel catalysts capable of hydrogenation of nitrogen molecule under mild conditions occupies the minds of many scientists. Nevertheless, it still remains one of the challenges of modern chemical sciences.¹ Extensive experimental¹⁻³ and theoretical⁴⁻⁷ studies during the past several decades have provided deeper understanding of the fundamental principles of dinitrogen hydrogenation and have elucidated several factors that are necessary for the success of direct reaction of $H_2$ and $N_2$. The first of them is the side-on coordination of an $N_2$ molecule to two transition metal centers to form a $[L_nM]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ complex. However,

* To whom correspondence should be addressed. E-mail: dmusaev@emory.edu. Phone: 404-727-2382.
(1) (a) Fryzuk, M. D.; Johnson, S. A. *Coord. Chem. Rev.* **2000**, *200*−202, 379. (b) *Catalytic Ammonia Synthesis*; Jennings, J. R., Ed.; Plenum: New York, 1991. (c) Fryzuk, M. D. *Nature* **2004**, *427*, 498. (d) Schlögl, R. *Angew. Chem., Int. Ed.* **2003**, *42*, 2004. (e) Mori, M. *J. Organomet. Chem.* **2004**, *689*, 4210. (g)Yandulov, D. V.; Schrock, R. R. *Science* **2003**, *76*, 301. (h) Schrock, R. R. *Acc. Chem. Res.* **2005**, *38*, 955. (i) MacKay, B. A.; Fryzuk, M. D. *Chem. Rev.* **2004**, *104*, 385. (j) Gambarotta, S.; Scott, J. *Angew. Chem., Int. Ed.* **2004**, *43*, 5298. (h) Himmel, H. J.; Reither M. *Angew. Chem., Int. Ed.* **2006**, *45*, 6264.
(2) MacLachlan, E. A.; Fryzuk, M. D. *Organometallics* **2006**, *25*, 1530, and references therein.
(3) Bernskoetter, W. H.; Lobkovsky, E.; and Chirik, P. J. *J. Am. Chem. Soc.* **2005**, *127*, 14051.
(4) Bobadova-Parvanova, P.; Wang, Q.; Quinonero-Santiago, D.; Morokuma, K.; Musaev, D. G. *J. Am. Chem. Soc.* **2006**, *128*, 11391.
(5) Musaev, D. G. *J. Phys. Chem. B* **2004**, *108*, 10012.
(6) Basch, H.; Musaev, D. G.; Morokuma, K. *Organometallics* **2000**, *19*, 3393.
(7) Musaev, D. G.; Basch, H.; Morokuma, K. *Computational Modeling of Homogeneous Catalysis*; Kluwer Academic Publishers: Norwell, MA, 2002.

10.1021/ic062405b CCC: $37.00
© 2007 American Chemical Society
Published on Web 03/07/2007

Inorganic Chemistry, Vol. 46, No. 7, 2007 **2709**

numerous studies $^{1,2,8}$ of the reactivity of dinuclear transition metal complexes with side-on-coordinated $N_2$ molecules show that not every reported $[L_nM]_2(\mu_2,\eta^2,\eta^2-N_2)$ complex adds a hydrogen molecule to $N_2$ via a hydrogenation mechanism. Among the reported dinuclear transition metal complexes of type $[L_nM]_2(\mu_2,\eta^2,\eta^2-N_2)$, those containing group IV metals (Zr and Hf) are more promising. $^{1,3}$ The second necessary condition $^{3-5,7}$ for the successful $N_2$ hydrogenation is availability of the appropriate frontier orbitals of $[L_nM]_2(\mu_2,\eta^2,\eta^2-N_2)$ complexes for activation of a dihydrogen molecule: the HOMO of $[L_nM]_2(\mu_2,\eta^2,\eta^2-N_2)$, which is expected to donate electrons to the $\sigma_u^*$ orbital of the coming $H_2$ molecule, should be a $\pi$-bonding orbital of the $M-N_2-M$ fragment. Meanwhile, the LUMO of $[L_nM]_2$-$(\mu_2,\eta^2,\eta^2-N_2)$, which accepts electrons from the $\sigma_g$-bonding MO of the reacting $H_2$ molecule should mainly have metal character. This qualitative orbital picture is consistent with the "metathesis" transition state (involving one of the M and N atoms of the complex and two H atoms from the $H_2$ molecule) reported for $H_2$ addition to dizirconium-$N_2$, $[L_n$-Zr$]_2(\mu_2,\eta^2,\eta^2-N_2)$ complexes. $^{4-6,9-12}$ Geometrical rigidity $^4$ of the $L_n$ ligands of the M centers is another important factor for successful addition of several (consequently) $H_2$ molecules to the side-on-coordinated $N_2$. The rigid (nonflexible) ligand environment of the M centers prevents the formation of H-bridged [with a $M(\mu_2-H)(\mu_2,\eta^2,\eta^2-NNH)M$ moiety] intermediate after the first $H_2$ addition, which requires a larger energy barrier for the next $H_2$ addition than the intermediate without H-bridged structure [with a HM-$(\mu_2,\eta^2,\eta^2-NNH)M$ moiety].

However, available experiments $^2$ indicate that the above-presented three factors are not the only necessary conditions for successful hydrogenation of the coordinated $N_2$ molecule, and some other factors could also be vital for the success of this reaction. Below, we demonstrate this for the reaction of $[(\eta^5-C_5Me_nH_{5-n})_2M]_2(\mu_2,\eta^2,\eta^2-N_2)$ for $n=0$ and 4 and M = Ti, Zr, and Hf with the dihydrogen molecule.

Reaction of the dizirconium complex $[(\eta^5-C_5Me_4H)_2Zr]_2$-$(\mu_2,\eta^2,\eta^2-N_2)$ (and its numerous derivatives) with a hydrogen molecule was the subject of several recent experimental $^{13}$ and theoretical $^{4,11,14,15}$ studies. In 2004, Chirik and coworkers $^{13}$ reported that a di-Zr complex, $[(\eta^5-C_5Me_4H)_2Zr]_2$-$(\mu_2,\eta^2,\eta^2-N_2)$, reacts with an $H_2$ molecule at $22\ ^{\circ}C$ and 1 atm of $H_2$ and leads to the formation of $N-H$ bonds. Subsequent warming of the complex to $85\ ^{\circ}C$ results in formation of a small amount of ammonia. Computational studies from our $^{4,14,15}$ and other $^{11}$ groups have demonstrated that the reaction
$$
\begin{aligned}
&[(\eta^5\text{-}C_5\text{Me}_4\text{H})_2\text{Zr}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)\ +\ \text{H}_2\rightarrow\\
&\quad [(\eta^5\text{-}C_5\text{Me}_4\text{H})_2\text{Zr}][(\eta^5\text{-}C_5\text{Me}_4\text{H})_2\text{ZrH}](\mu_2,\eta^2,\eta^2\text{-NNH})\ (1)
\end{aligned}
$$
occurs with a 17.9 (19.6) kcal/mol energy barrier at the "metathesis-like" transition state (similar to that reported $^{5,9,10,12}$ for the reaction of another dizirconium-$N_2$ complex with $H_2$), and is exothermic by 11.5 (6.2) kcal/mol (here and below, numbers given in parentheses include the zero-point-energy corrections).

Reaction of the dihafnium complex $[(\eta^5-C_5Me_4H)_2Hf]_2$-$(\mu_2,\eta^2,\eta^2-N_2)$ with an $H_2$ molecule also was recently reported $^{16}$ at $23\ ^{\circ}C$ and 1 atm of $H_2$. Interestingly, the Hf complex hydrogenates dinitrogen faster than the corresponding Zr complex. Furthermore, thermolysis of $[(\eta^5-C_5Me_4H)_2$-HfH$]_2(\mu_2,\eta^2,\eta^2-N_2H_2)$ results in cyclometalation of a cyclopentadienyl methyl group rather than ammonia formation, as was the case with corresponding Zr complex. $^{13}$

Reaction of the dititanum analogue of these complexes, $[(\eta^5-C_5Me_4H)_2Ti]_2(\mu_2,\eta^2,\eta^2-N_2)$, with an $H_2$ molecule has not been reported. In the literature, several dinitrogen complex of Ti were reported, $^{17}$ but none of them hydrogenates $N_2$. It is noteworthy that recently a matrix isolation technique was used to show that "naked" $Ti_2$ dimer cleaves the $N-N$ triple bond of $N_2$ and forms (TiN)$_2$ species without a significant energy barrier. $^{18}$ Furthermore, Andrews and co-workers, $^{19}$ on the basis of the density functional and matrix-isolation studies, have shown that the degree of dinitrogen activation by "naked" Ti, Zr, and Hf atoms increases in the order Ti < Zr < Hf. This trend has been rationalized by the increasing size of the valence $nd$ orbitals. Similar conclusions were made by Blomberg and Siegbahn $^{20}$ in the study of $M_2N_2$ systems by ab initio methods for M = Ti, Zr, and Hf.

In order to clarify similarites and differences and elucidate the reasons for hydrogenation of $[(\eta^5-C_5Me_nH_{5-n})_2M]_2$-$(\mu_2,\eta^2,\eta^2-N_2)$ for M = Ti, Zr, and Hf, in the present paper we study and compare the mechanism of the reaction
$$
\begin{aligned}
&[(\eta^5\text{-}C_5\text{Me}_n\text{H}_{5-n})_2\text{M}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)\ +\ \text{H}_2\rightarrow\\
&\quad [(\eta^5\text{-}C_5\text{Me}_n\text{H}_{5-n})_2\text{M}][(\eta^5\text{-}C_5\text{Me}_n\text{H}_{5-n})_2\text{MH}]\\
&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad(\mu_2,\eta^2,\eta^2\text{-NNH})\ (2)
\end{aligned}
$$
for M = Ti, Zr, and Hf in the lowest singlet and triplet electronic states of the reactants. In our studies we use unsubstituted ($n=0$) and tetramethyl (Me)-substituted ($n=4$) derivatives of these complexes. The mechanism of reaction 2 for M = Zr in its singlet electronic state was

(8) Chirik, P.; Henling, L. M.; Bercaw, J. E. *Organometallics* **2001**, 20, 534.

(9) Basch, H.; Musaev, D. G.; Morokuma, K.; Fryzuk, M. D.; Love, J. B.; Seidel, W. W.; Albinati, A.; Koetzle, F.; Klooster, W. T.; Mason, S. A.; Eckert, J. *J. Am. Chem. Soc.* **1999**, 121, 523.

(10) Basch, H.; Musaev, D. G.; Morokuma, K. *J. Am. Chem. Soc.* **1999**, 121, 5754.

(11) Miyachi, H.; Shigeta, Y.; Hirao, K. *J. Phys. Chem. A* **2005**, 109, 8800.

(12) Yates, B. F.; Basch, H.; Musaev, D. G.; Morokuma, K. *J. Chem. Theor. Comp.* **2006**, 2, 1298.

(13) Pool, J. A.; Lobkovsky, E.; Chirik, P. J. *Nature* **2004**, 427, 527.

(14) Bobadova-Parvanova, P.; Wang, Q.; Morokuma, K.; Musaev, D. G., *Angew. Chem., Int. Ed.* **2005**, 44, 7101.

(15) Bobadova-Parvanova, P.; Quinonero-Santiago, D.; Morokuma, K.; Musaev, D. G. *Chem. Theor. Comp.* **2006**, 2, 336.

(16) Bernskoetter, W. H.; Olmos, A. V.; Lobkovsky, E.; Chirik, P. J. *Organometallics* **2006**, 25, 1021.

(17) (a) Hanna, T. E.; Lobkovsky, E.; Chirik, P. J. *J. Am. Chem. Soc.* **2006**, 128, 6018. (b) Hanna, T. E.; Lobkovsky, E.; Chirik, P. J. *J. Am. Chem. Soc.* **2004**, 126, 14688, and references therein.

(18) Himmel, H.-J.; Hubner, O.; Klopper, W.; Manceron, L. *Angew. Chem., Int. Ed.* **2006**, 45, 2799.

(19) Kushto, G. P.; Souter, P. F.; Certihin, G. V.; Andrews, L. *J. Chem. Phys.* **1999**, 110, 9020.

(20) Blomberg, M. R. A.; Siegbahn, P. E. M. *J. Am. Chem. Soc.* **1993**, 115, 6908.

![](./images/812010322427641859_1.jpg)

Figure 1. Schematic representation of structures of reactants, transition states, and products of reaction 2.

reported previously. $^{4,11,14}$ Here, for completeness of the data presented, we will visit our previous results when required.

## 2. Computational Procedure
The geometries of all reactants, transition states, and products of reaction 2 were optimized using the hybrid density functional B3LYP method $^{21}$ and the Stevens-Basch-Krauss (SBK) $^{22}$ relativistic effective core potentials (for Ti, Zr, Hf, C, and N). In these calculations we used standard CEP-31G basis sets for H, C, N, Ti, Zr, and Hf atoms with additional d-type polarization function for all $N$ atoms $(\alpha=0.80)$. Below we denote this approach as B3LYP/CEP-31G(d$_\text{N}$). This is the same approach that was used previously in our studies. Therefore, the use of this approach in the present paper will enable us to compare new findings with those from our previous studies. All reported structures were optimized without any symmetry constraints. The nature of all intermediates and transition states were confirmed by performing normal-mode analysis. In addition, we performed intrinsic-reaction-coordinate (IRC) calculations from all located transition states to confirm the nature of reactants and products connected by these transition states. All reported data were calculated by using Gaussian 03 program package. $^{23}$

In general, it is known that hybrid density functionals such as B3LYP overstabilize, while nonhybrid functionals (like BLYP, PBE, etc.) understabilize, high-spin states relative to low-spin states. $^{24}$ The best approaches to calculate the energy difference between the lowest electronic states would be highly correlated methods such as CCSD(T) and MRSD-CI with a very large basis set. However, the application of such sophisticated methods to the transition metal complexes like $[(\eta^5\text{-}C_5\text{Me}_n\text{H}_{5-n})_2\text{M}]_2(\mu_2,\eta^2,\eta^2\text{-N}_2)$ is computationally too costly. Therefore, in this paper, in order to determine "sandwich" relative energies of lowest triplet and closed-shell singlet states of the reactant $[(\eta^5\text{-}C_5\text{Me}_n\text{H}_{5-n})_2\text{M}]_2(\mu_2,\eta^2,\eta^2\text{-N}_2)$ for $n=0$ and $\text{M}=$ Ti, Zr, and Hf, we performed calculations (geometry optimization and energy calculation) utilizing both hybrid (B3LYP) and nonhybrid (PBE) $^{25}$ density functionals, which previously shown to describe the geometries of transition metal complexes with reasonable accuracy. $^{26}$ We expected that the comparison of the B3LYP- and PBE-calculated energy differences between the closed-shell singlet and triplet states will enable us to qualitatively determine the ground and excited states of these species, as well as to roughly estimate the error introduced by the use of B3LYP and/or PBE methods in determining energetics of low-lying electronic states of the systems studied here.

One should note that in our previous paper $^4$ we have shown that the use of larger basis sets like Stuttgart-Dresden effective core potential and associated large (SDD) $^{27}$ basis set for $\text{M}$ ($\text{M}=$ Zr)

---

(21) (a) Becke, A. D. *Phys. Rev. A* **1988**, *38*, 3098. (b) Lee, C.; Yang, W.; Parr, R. G. *Phys. Rev. B* **1988**, *37*, 785. (c) Becke, A. D. *J. Chem. Phys.* **1993**, *98*, 5648.

(22) (a) Stevens, W. J.; Basch, H.; Krauss, M. *J. Chem. Phys.* **1984**, *81*, 6026. (b) Stevens, W. J.; Krauss, M.; Basch, H.; Jasien, P. G. *Can. J. Chem.* **1992**, *70*, 612. (c) Cundari, T. R.; Stevens, W. J. *J. Chem. Phys.* **1994**, *98*, 5555.

(23) Frisch, M. J.; et al. *Gaussian 03*, Revision C.02; Gaussian, Inc.: Wallingford, CT, 2004.

(24) (a) Khavrutskii, I. V.; Musaev, D. G.; Morokuma, K. *Inorg. Chem.* **2003**, *42*, 2606, and references therein. (b) Reiher, M.; Salomon, O.; Hess, B. A. *Theor. Chem. Acc.* **2001**, *107*, 48. (c) Harvey, J. N. *Struct. Bonding* **2004**, *112*, 152.

(25) Perdew, J. P.; Burke, K.; Ernzerhof, M. *Phys. Rev. Lett.* **1996**, *77*, 3865.

(26) (a) Cui, Q.; Musaev, D. G.; Svensson, M.; Sieber, S.; Morokuma, K. *J. Am. Chem. Soc.* **1995**, *117*, 12366-12367. (b) Musaev, D. G.; Morokuma, K. *J. Phys. Chem.* **1996**, *100*, 6509-6517. (c) Erikson, L. A.; Pettersson, L. G. M.; Siegbahn, P. E. M.; Wahlgren, U. *J. Chem. Phys.* **1995**, *102*, 872-878. (d) Ricca, A.; Bauschlicher, C. W., Jr. *J. Phys. Chem.* **1994**, *98*, 12899-12903. (e) Heinemann, C.; Hertwig, R. H.; Wesendrup, R.; Koch, W.; Schwarz, H. *J. Am. Chem. Soc.* **1995**, *117*, 495-500. (f) Hertwig, R. H.; Hrusak, J.; Schroder, D.; Koch, W.; Schwarz, H. *Chem. Phys. Lett.* **1995**, *236*, 194-200. (g) Schroder, D.; Hrusak, J.; Hertwig, R. H.; Koch, W.; Schwerdtfeger, P.; Schwarz, H. *Organometallics* **1995**, *14*, 312-316. (h) Fiedler, A.; Schroder, D.; Shaik, S.; Schwarz, H. *J. Am. Chem. Soc.* **1994**, *116*, 10734-10741. (i) Fan, L.; Ziegler, T. *J. Chem. Phys.* **1991**, *95*, 7401-7408. (j) Berces, A.; Ziegler, T.; Fan, L. *J. Phys. Chem.* **1994**, *98*, 1584-1595. (k) Lyne, P. D.; Mingos, D. M. P.; Ziegler, T.; Downs, A. *J. Inorg. Chem.* **1993**, *32*, 4785-4796. (l) Li, J.; Schreckenbach, G.; Ziegler, T. *J. Am. Chem. Soc.* **1995**, *117*, 486-494.

(27) (a) Fuentealba, P.; Preuss, H.; Stoll, H.; Szentpaly, L. V. *Chem. Phys. Lett.* **1989**, *89*, 418. (b) Wedig, U.; Dolg, M.; Stoll, H.; Preuss, H. *Quantum Chemistry: The Challenge of Transition Metals and Coordination Chemistry*; Veillard: Reidel, Dordrecht, 1986; p 79. (c) Leininger, T.; Nicklass, A.; Stoll, H.; Dolg, M.; Schwerdtfeger, P., *J. Chem. Phys.* **1996**, *105*, 1052. (d) Cao, X. Y.; Dolg, M. *J. Mol. Struct. (THEOCHEM)* **2002**, *581*, 139.


![](./images/812010322427641859_2.jpg)

Figure 2. Potential energy profiles (with zero-point-energy corrections) of reaction 2 for $[(\eta^{5}-C_{5}Me_{n}H_{5-n})_{2}M]_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$ with M = Ti, Zr and Hf and $n = 0$ and 4 in their closed-shell singlet (S) and triplet (T) electronic states calculated at the B3LYP/CEP-31G(d$_N$) level of theory.

<table>
<caption>Table 1. Calculated Relative Energies (in kcal/mol) of the Reactants, Transition States, and Products of Reaction 2 for M = Ti, Zr, and Hf at Their Closed-Shell Singlet (S) and Triplet (T) Electronic States<sup>a</sup></caption>
<thead>
<tr>
<th rowspan="2">complex</th>
<th rowspan="2">state</th>
<th rowspan="2">method</th>
<th colspan="3">n = 0</th>
<th colspan="3">n = 4</th>
</tr>
<tr>
<th>Ti</th>
<th>Zr</th>
<th>Hf</th>
<th>Ti</th>
<th>Zr</th>
<th>Hf</th>
</tr>
</thead>
<tbody>
<tr>
<td>reactants</td>
<td>S</td>
<td>B3LYP</td>
<td>0.0 (0.0)</td>
<td>0.0 (0.0)</td>
<td>0.0 (0.0)</td>
<td>0.0 (0.0)</td>
<td>0.0 (0.0)</td>
<td>0.0 (0.0)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>PBE</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>T</td>
<td>B3LYP</td>
<td>$-24.1\left(-23.5\right)$</td>
<td>$0.5\left(0.8\right)$</td>
<td>$10.3\left(10.5\right)$</td>
<td>$-20.9\left(-20.8\right)$</td>
<td>$-0.3\left(-0.7\right)$</td>
<td>$7.7\left(7.8\right)$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>PBE</td>
<td>$-3.1$</td>
<td>$6.1$</td>
<td>$11.6$</td>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>TS</td>
<td>S</td>
<td>B3LYP</td>
<td>$23.6\left(26.7\right)$</td>
<td>$18.8\left(21.4\right)$</td>
<td>$17.7\left(20.3\right)$</td>
<td>$16.0\left(18.7\right)$</td>
<td>$18.0\left(19.6\right)$</td>
<td>$17.1\left(19.0\right)$</td>
</tr>
<tr>
<td></td>
<td>T</td>
<td>B3LYP</td>
<td>$13.2\left(15.8\right)$</td>
<td>$18.7\left(21.2\right)$</td>
<td>$23.4\left(26.2\right)$</td>
<td>$-0.4\left(2.0\right)$</td>
<td>$22.2\left(23.9\right)$</td>
<td>$26.4\left(29.0\right)$</td>
</tr>
<tr>
<td>product</td>
<td>S</td>
<td>B3LYP</td>
<td>$-12.6\left(-6.4\right)$</td>
<td>$-13.1\left(-6.9\right)$</td>
<td>$-14.2\left(-7.8\right)$</td>
<td>$-17.5\left(-11.5\right)$</td>
<td>$-11.4\left(-6.2\right)$</td>
<td>$-15.3\left(-9.3\right)$</td>
</tr>
<tr>
<td></td>
<td>T</td>
<td>B3LYP</td>
<td>$-15.4\left(-10.1\right)$</td>
<td>$3.6\left(9.0\right)$</td>
<td>$-2.8\left(2.5\right)$</td>
<td>$-22.0\left(-17.3\right)$</td>
<td>$0.1\left(4.5\right)$</td>
<td>$1.9\left(8.1\right)$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9"><sup>a</sup> ZPE-corrected energies are given in parentheses.</td>
</tr>
</tfoot>
</table>

and the standard 6-31G(d) basis set for the remaining atoms (H, C, and N) has no significant effect on the calculated geometries and energetics of the reactants, transition states, and products of reaction 2. Therefore, in our present studies we use only B3LYP/ CEP-31G(d$_N$) and/or PBE/CEP-31G(d$_N$) approaches.

## 3. Results and Discussion

### A. Relative Stability of the Lowest Singlet (S) and Triplet (T) Electronic States of Complexes $[(\eta^{5}-C_{5}Me_{n}-$$H_{5-n})_{2}M]_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$ for $n = 0$ and 4, and M = Ti, Zr, and Hf.
In Figure 1 we schematically present the structures of the reactants, transition states, and products of reaction 2 for M = Ti, Zr, and Hf at their closed-shell singlet and triplet electronic states. In Table 1 we present the calculated relative energies of the reactants, transition states, and products of reaction 2 for M = Ti, Zr and Hf at their closed-shell singlet and triplet electronic states. Numbers presented with and without parentheses correspond to the zero-point-energy corrected and noncorrected values. Comparison of these numbers shows that inclusion of zero-point energy correction does not change the trends in the energetics. Therefore, below we discuss only the zero-point-corrected energies, when available (which also schematically presented in Figure 2), while both values are presented in Table 1 and throughout the paper. The important geometry parameters of all struc-tures calculated at the B3LYP/CEP-31G(d$_N$) level of theory are given in Table 2. Figure 3 shows crucial frontier orbitals of $[(\eta^{5}-C_{5}H_{5})_{2}M]_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$ for M = Ti, Zr and Hf at their singlet and triplet states.

As seen from Table 1 and Figure 2, the ground electronic state of the reactant, $[(\eta^{5}-C_{5}Me_{n}H_{5-n})_{2}Ti]_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$ is a triplet (for both $n = 0$ and 4) with one unpaired electron on each Ti center. At the B3LYP level, the singlet states are 24.1 (23.5) and 20.9 (20.8) kcal/mol higher in energy for $n = 0$ and 4, respectively. At the PBE level, the singlet−triplet energy splitting for the complex with $n = 0$ is found to be only 3.1 kcal/mol. By taking into account the fact that B3LYP method overstabilizes and PBE understabilizes high-spin states, one can confidently conclude that the ground electronic state of the Ti complexes $[(\eta^{5}-C_{5}Me_{n}H_{5-n})_{2}Ti]_{2}-$$(\mu_{2},\eta^{2},\eta^{2}-N_{2})$ is a triplet both for $n = 0$ and 4, with the singlet state $\sim$10 kcal/mol higher in energy.

This picture is different for analogous Zr and Hf com-plexes. Indeed, for Zr and Hf complexes the singlet and triplet states are extremely close to each other at both B3LYP

Computational Studies on $[(\eta^{5}-C_{5}Me_{n}H_{5-n})_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$

![](./images/812010322427641859_3.jpg)

Figure 3. Schematic presentation of frontier orbitals of $[(\eta^{5}-C_{5}H_{5})_{2}M]_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$ for M = Ti, Zr, and Hf in their closed-shell singlet (S) and triplet (T) electronic states calculated at the B3LYP/CEP-31G(d$_{N}$) level of theory.

Table 2. Bond Lengths (in Å) of the Reactants, Transition States, and Products of Reaction 2 for M = Ti, Zr, and Hf in their Closed-Shell Singlet and Triplet Electronic States Calculated at the B3LYP/CEP-31G(d$_{N}$) Level of Theory

<table><tbody><tr><td rowspan="2">complex state</td><td rowspan="2"></td><td colspan="9">n = 0</td><td colspan="9">n = 4</td></tr><tr><td>N¹−N²</td><td>M¹−N¹</td><td>M¹−N²</td><td>M²−N¹</td><td>M²−N²</td><td>M¹−H²</td><td>N¹−H¹</td><td>H¹−H²</td><td></td><td>N¹−N²</td><td>M¹−N¹</td><td>M¹−N²</td><td>M²−N¹</td><td>M²−N²</td><td>M¹−H²</td><td>N¹−H¹</td><td>H¹−H²</td></tr><tr><td colspan="20">M = Ti</td></tr><tr><td rowspan="2">reactant</td><td>S</td><td>1.326</td><td>1.984</td><td>1.984</td><td>1.984</td><td>1.984</td><td></td><td></td><td></td><td></td><td>1.327</td><td>2.003</td><td>2.005</td><td>2.003</td><td>2.005</td><td></td><td></td><td></td></tr><tr><td>T</td><td>1.238</td><td>2.139</td><td>2.139</td><td>2.139</td><td>2.139</td><td></td><td></td><td></td><td></td><td>1.243</td><td>2.168</td><td>2.155</td><td>2.168</td><td>2.155</td><td></td><td></td><td></td></tr><tr><td rowspan="2">TS</td><td>S</td><td>1.304</td><td>2.206</td><td>2.100</td><td>2.026</td><td>2.101</td><td>1.765</td><td>1.335</td><td>1.110</td><td></td><td>1.267</td><td>2.233</td><td>2.236</td><td>3.020</td><td>2.076</td><td>1.726</td><td>1.246</td><td>1.179</td></tr><tr><td>T</td><td>1.332</td><td>2.146</td><td>2.032</td><td>2.142</td><td>2.125</td><td>1.790</td><td>1.342</td><td>1.037</td><td></td><td>1.249</td><td>3.007</td><td>2.413</td><td>2.100</td><td>2.183</td><td>1.940</td><td>1.352</td><td>0.982</td></tr><tr><td rowspan="2">product</td><td>S</td><td>1.399</td><td>3.107</td><td>1.932</td><td>1.985</td><td>1.969</td><td>1.695</td><td>1.031</td><td></td><td></td><td>1.424</td><td>3.081</td><td>1.963</td><td>1.972</td><td>2.005</td><td>1.693</td><td>1.027</td><td></td></tr><tr><td>T</td><td>1.293</td><td>3.101</td><td>2.017</td><td>2.067</td><td>2.167</td><td>1.698</td><td>1.034</td><td></td><td></td><td>1.297</td><td>2.074</td><td>3.201</td><td>3.172</td><td>1.910</td><td>1.701</td><td>1.035</td><td></td></tr><tr><td colspan="20">M = Zr</td></tr><tr><td rowspan="2">reactant</td><td>S</td><td>1.416</td><td>2.087</td><td>2.087</td><td>2.087</td><td>2.087</td><td></td><td></td><td></td><td></td><td>1.404</td><td>2.114</td><td>2.101</td><td>2.114</td><td>2.101</td><td></td><td></td><td></td></tr><tr><td>T</td><td>1.260</td><td>2.248</td><td>2.248</td><td>2.248</td><td>2.248</td><td></td><td></td><td></td><td></td><td>1.274</td><td>2.239</td><td>2.249</td><td>2.239</td><td>2.249</td><td></td><td></td><td></td></tr><tr><td rowspan="2">TS</td><td>S</td><td>1.422</td><td>2.237</td><td>2.146</td><td>2.093</td><td>2.095</td><td>1.987</td><td>1.383</td><td>1.030</td><td></td><td>1.416</td><td>2.264</td><td>2.145</td><td>2.129</td><td>2.093</td><td>2.026</td><td>1.415</td><td>0.988</td></tr><tr><td>T</td><td>1.362</td><td>2.253</td><td>2.142</td><td>2.244</td><td>2.246</td><td>1.976</td><td>1.376</td><td>1.038</td><td></td><td>1.356</td><td>2.301</td><td>2.175</td><td>2.242</td><td>2.239</td><td>1.982</td><td>1.396</td><td>1.039</td></tr><tr><td rowspan="2">product</td><td>S</td><td>1.493</td><td>2.303</td><td>2.198</td><td>2.158</td><td>1.994</td><td>1.851</td><td>1.034</td><td></td><td></td><td>1.477</td><td>3.195</td><td>2.101</td><td>2.087</td><td>2.111</td><td>1.864</td><td>1.029</td><td></td></tr><tr><td>T</td><td>1.382</td><td>2.466</td><td>2.172</td><td>2.248</td><td>2.244</td><td>1.855</td><td>1.038</td><td></td><td></td><td>1.329</td><td>2.134</td><td>2.432</td><td>3.191</td><td>2.183</td><td>1.838</td><td>1.027</td><td></td></tr><tr><td colspan="20">M = Hf</td></tr><tr><td rowspan="2">reactant</td><td>S</td><td>1.481</td><td>2.042</td><td>2.042</td><td>2.042</td><td>2.042</td><td></td><td></td><td></td><td></td><td>1.462</td><td>2.056</td><td>2.063</td><td>2.056</td><td>2.063</td><td></td><td></td><td></td></tr><tr><td>T</td><td>1.298</td><td>2.169</td><td>2.169</td><td>2.169</td><td>2.169</td><td></td><td></td><td></td><td></td><td>1.301</td><td>2.181</td><td>2.189</td><td>2.181</td><td>2.189</td><td></td><td></td><td></td></tr><tr><td rowspan="2">TS</td><td>S</td><td>1.478</td><td>2.188</td><td>2.096</td><td>2.044</td><td>2.038</td><td>1.974</td><td>1.395</td><td>1.005</td><td></td><td>1.474</td><td>2.225</td><td>2.085</td><td>2.064</td><td>2.046</td><td>2.017</td><td>1.455</td><td>0.958</td></tr><tr><td>T</td><td>1.376</td><td>2.220</td><td>2.107</td><td>2.200</td><td>2.206</td><td>1.950</td><td>1.396</td><td>1.021</td><td></td><td>1.376</td><td>2.254</td><td>2.130</td><td>2.176</td><td>2.315</td><td>1.955</td><td>1.418</td><td>1.019</td></tr><tr><td rowspan="2">product</td><td>S</td><td>1.520</td><td>2.284</td><td>2.155</td><td>2.117</td><td>1.973</td><td>1.831</td><td>1.034</td><td></td><td></td><td>1.520</td><td>3.170</td><td>2.075</td><td>2.045</td><td>2.071</td><td>1.837</td><td>1.027</td><td></td></tr><tr><td>T</td><td>1.336</td><td>3.199</td><td>2.086</td><td>2.151</td><td>2.252</td><td>1.834</td><td>1.030</td><td></td><td></td><td>1.342</td><td>2.099</td><td>2.427</td><td>3.147</td><td>2.142</td><td>1.820</td><td>1.025</td><td></td></tr></tbody></table>

and PBE levels of theory. However, the calculated energy gap between triplet (T) and singlet (S) states, $\Delta E(\text{S}-\text{T})$ increases upon going to the Hf complex. Thus, these results clearly show that complex $[(\eta^{5}-C_{5}Me_{n}H_{5-n})_{2}M]_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$ (for both $n = 0$ and 4) has a triplet (e.g., ferromagnetic) ground electronic state for M = Ti, while for its Zr and Hf analogous the singlet ground states are going to be available for reaction.

The B3LYP and PBE levels give significantly different $\Delta E(\text{S-T})$ values from each other, 24.1 (23.5) and 3.1 kcal/mol, respectively, for the first-row transition metal M = Ti in the complex $[(\eta^{5}-C_{5}H_{5})_{2}M]_{2}(\mu_{2},\eta^{2},\eta^{2}-N_{2})$. The difference in the $\Delta E(\text{S}-\text{T})$ values calculated at the B3LYP and PBE levels smoothly reduces upon going from M = Ti (21 kcal/mol) to M = Zr (5.6 kcal/mol) and M = Hf (1.3 kcal/mol). In other words, the difference in $\Delta E(\text{S}-\text{T})$ introduced by using hybrid and nonhybrid density functionals to describe low-lying electronic states of transition metal complexes reduces via first-row > second-row > third-row transition metals. Thus, both the hybrid and nonhybrid density functionals can be used to describe low-lying electronic states of the second- and third-row transition metal complexes. However, if the energy gap between the low- and high-spin states of the first-row transition metal complexes is a few kilocalories per mole, one should use both functionals with a caution.

Inorganic Chemistry, Vol. 46, No. 7, 2007 2713

Analysis of the HOMO and LUMO orbitals (see Figure 3) of these species clearly show that in their closed-shell singlet states HOMO is a bonding $\pi$-orbital of the $\mathrm{M-N_{2}-M}$ fragment, which is suitable for interaction with the $\sigma_{\mathrm{u}}{ }^{*}$ orbital of the coming $\mathrm{H}_{2}$ molecule. Their LUMO is a $\sigma$-orbital with mainly metal d character, which is appropriate for interaction with the $\sigma_{\mathrm{g}}$-bonding orbital of the $\mathrm{H}_{2}$ molecule. Thus, the frontier orbitals of all these complexes at their singlet electronic states are suitable for addition of $\mathrm{H}_{2}$ molecule via the "metathesis" transition states discussed in the introduction.

Furthermore, as seen in Figure 3, the energy of the HOMO lowers via $\mathrm{M}=\mathrm{Ti}(-0.143)>\mathrm{Zr}(-0.146)>\mathrm{Hf}(-0.150$ hartree), while that for the LUMO increases via the same trend, i.e., $\mathrm{Ti}(-0.082)<\mathrm{Zr}(-0.071)<\mathrm{Hf}(-0.060$ hartree). This trend in HOMO energy indicates that $\mathrm{M}-\mathrm{N}_{2}-\mathrm{M}$ interaction in $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{Me}_{n} \mathrm{H}_{5-n}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ increases via $\mathrm{M}=\mathrm{Ti}<\mathrm{Zr}<\mathrm{Hf}$. This conclusion is consistent with the calculated $\mathrm{N}-\mathrm{N}$ bond distances in these compounds, which increases via $\mathrm{Ti}(1.326 \AA)<\mathrm{Zr}(1.416 \AA)<\mathrm{Hf}(1.481 \AA)$. Thus, the $\mathrm{N}_{2}$ molecule is more activated in the Hf complex than in the $\mathrm{Zr}$ and Ti complexes.

The $\mathrm{S} \rightarrow \mathrm{T}$ excitation corresponds to the promotion of an electron from the $\mathrm{M}-\mathrm{N}_{2}-\mathrm{M}$ bonding HOMO to the nonbonding LUMO. As a result, the HOMO and LUMO of the singlet state become the SOMO-2 and SOMO-1 of triple state, respectively. As seen in Figure 3, the SOMO-2 and SOMO-1 orbitals of triplet-state Ti complexes are the antisymmetric and symmetric combination of Ti d orbitals. On the other hand, for $\mathrm{Zr}$ and Hf complexes, while SOMO-2 and SOMO-1 are similar to the singlet-state HOMO and LUMO, respectively, SOMO-2 significantly lost its $\mathrm{M}-\mathrm{N}_{2}-\mathrm{M}$ bonding character. This effect is much more pronounced for $\mathrm{Zr}$ than Hf complexes. The above-presented picture is consistent with the calculated energy difference between the SOMO-1 and SOMO-2, as well as with the calculated $\mathrm{N}-\mathrm{N}$ bond distance in these species: the calculated $\Delta E(\mathrm{SOMO}-1$ - SOMO-2) is 0.005, 0.010, and 0.029 hartree and the $\mathrm{N}-\mathrm{N}$ bond distance is $1.238,1.260$, and $1.298 \AA$, for $\mathrm{M}=\mathrm{Ti}, \mathrm{Zr}$, and $\mathrm{Hf}$, respectively. Thus, the orbital analysis clearly indicates that $\mathrm{S} \rightarrow \mathrm{T}$ excitation in $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{Me}_{n} \mathrm{H}_{5-n}\right)_{2} \mathrm{M}\right]_{2-}$ $\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ should reduce $\mathrm{M}-\mathrm{N}_{2}$ interaction but increase the $\mathrm{N}-\mathrm{N}$ bonding. Indeed, as seen in Table 2, the calculated $\mathrm{M}-\mathrm{N}_{2}$ bond distances are longer for triplet states than the corresponding singlet states by $0.12-0.16 \AA$, while the calculated $\mathrm{N}-\mathrm{N}$ bond distances in singlet complexes are about $0.08-0.19 \AA$ longer than in the corresponding triplet complexes. The calculated $\mathrm{N}-\mathrm{N}$ bond distance is shorter for $\mathrm{M}=\mathrm{Ti}$ than for $\mathrm{M}=\mathrm{Zr}$ and Hf in both the singlet and triplet states.

### B. Potential Energy Surfaces (PESs) of Reaction 2 in the Closed-Shell Singlet (S) and Triplet (T) States of Reactants, Transition States, and Products.
From the above-presented discussion it is clear that the geometrical structure (all the complexes studied here have a side-oncoordinated $\mathrm{N}_{2}$ molecule) and the character of the HOMO and LUMO (the HOMO is a bonding $\pi$-orbital of the $\mathrm{M}-\mathrm{N}_{2}-\mathrm{M}$ fragment, and the LUMO is a $\sigma$-orbital with mainly metal d character) of the singlet-state $\left[\left(\eta^{5}-\mathrm{C}_{5^{-}}\right.\right.$ $\left.\left.\mathrm{Me}_{n} \mathrm{H}_{5-n}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ complexes are consistent with the first two necessary conditions for successful hydrogenation of a coordinated $\mathrm{N}_{2}$ molecule, as discussed in the Introduction. Therefore, one may expect that these complexes at their singlet electronic states will add an $\mathrm{H}_{2}$ molecule to coordinated $\mathrm{N}_{2}$ molecule under mild conditions (with a reasonable energy barrier). In fact, our calculations of PES of reaction 2 are consistent with above-presented expectations (see Figure 2); at the singlet electronic states, complexes $\left[\left(\eta^{5}-\right.\right.$ $\left.\left.\mathrm{C}_{5} \mathrm{Me}_{4} \mathrm{H}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ and $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{H}_{5}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$, for $\mathrm{M}=\mathrm{Ti}, \mathrm{Zr}$, and Hf, should add an $\mathrm{H}_{2}$ molecule to the coordinated $\mathrm{N}_{2}$ to give the $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{Me}_{n} \mathrm{H}_{5-n}\right)_{2} \mathrm{M}\right]\left[\left(\eta^{5}-\mathrm{C}_{5^{-}}\right.\right.$ $\left.\left.\mathrm{Me}_{n} \mathrm{H}_{5-n}\right)_{2} \mathrm{MH}\right]\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{NNH}\right)$ product. The calculated energy barriers (relative to the singlet-state reactants), as shown in Table 1 and Figure 2, are 23.6 (26.7), 18.8 (21.4), and 17.7 (20.3) $\mathrm{kcal} / \mathrm{mol}$ for $n=0$, and $16.0(18.7), 18.0(19.6)$, and 17.1 (19.0) $\mathrm{kcal} / \mathrm{mol}$ for $n=4$, for $\mathrm{M}=\mathrm{Ti}, \mathrm{Zr}$, and $\mathrm{Hf}$, respectively. Thus, the reactivity of the complex $\left[\left(\eta^{5}-\mathrm{C}_{5^{-}}\right.\right.$ $\left.\left.\mathrm{Me}_{n} \mathrm{H}_{5-n}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ with an $\mathrm{H}_{2}$ molecule, in their singlet electronic states, increases via $\mathrm{M}=\mathrm{Ti}<\mathrm{Zr} \leq \mathrm{Hf}$. This trend can qualitatively be explained by the calculated exothermicity of reaction 2 , which increases via $\mathrm{M}=\mathrm{Ti}$ $[-12.6(-6.4)$ and $-17.5(-11.5) \mathrm{kcal} / \mathrm{mol}$, for $n=0$ and 4] $<\mathrm{Zr}[-13.1(-6.9)$ and $-11.4(-6.2) \mathrm{kcal} / \mathrm{mol}$, for $n=$ 0 and 4] $<$ Hf $[-14.2(-7.8)$ and $-15.3(-9.3) \mathrm{kcal} / \mathrm{mol}$ for $n=0$ and 4], as well as with the degree of activation of the $\mathrm{N}-\mathrm{N}$ bond in the reactant complexes $(\mathrm{N}-\mathrm{N}$ bond distance becomes longer via $\mathrm{M}=\mathrm{Ti}[1.326$ and $1.327 \AA$, for $n=0$ and 4] $<\mathrm{Zr}[1.416$ and $1.404 \AA$, for $n=0$ and 4] $<$ Hf [1.481 and $1.462 \AA$, for $n=0$ and 4]. The above mentioned trend in reactivity of the $\mathrm{Zr}$ and Hf complexes with an $\mathrm{H}_{2}$ molecule correlates well with the available experimental results. ${ }^{13,16}$

However, as discussed above, the singlet electronic state is not the ground state for the Ti complexes; it lies significantly higher in energy than the corresponding ground triple state. Although the singlet state is the ground state for $\mathrm{Zr}$ and Hf complexes, their triplet states are only few kilocalories per mole higher in energy. Therefore, we also have to examine the PES of reaction 2 in the lowest triplet states of the complexes $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{Me}_{4} \mathrm{H}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ and $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{H}_{5}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ for $\mathrm{M}=\mathrm{Ti}, \mathrm{Zr}$, and Hf.

For $\mathrm{M}=\mathrm{Ti}$, the ground electronic state of both $\left[\left(\eta^{5}-\mathrm{C}_{5^{-}}\right.\right.$ $\left.\left.\mathrm{Me}_{4} \mathrm{H}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ and $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{H}_{5}\right)_{2} \mathrm{M}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ are triplet states, the conclusion, as discussed in a preceding section, obtained at the both B3LYP and BPE levels of theory. As seen in Figure 2, the calculated energy barriers (relative to the triplet state reactants) are very large, 37.3 (39.3) and 20.5 (22.8) $\mathrm{kcal} / \mathrm{mol}$ for $n=0$ and 4 , respectively. These values are larger than those for the singlet states of these complexes, especially for $n=0$ complexes. Furthermore, the reactions (eq 2) for the triplet Ti complexes are endothermic by $8.7(13.4) \mathrm{kcal} / \mathrm{mol}$ for $n=0$ and nearly thermally neutral (with the energy of reaction of $-1.1(3.5)$ $\mathrm{kcal} / \mathrm{mol})$ for $n=4$. These values of the calculated barriers and reaction energies for the triplet ground states of $\mathrm{Ti}$ complexes $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{Me}_{4} \mathrm{H}\right)_{2} \mathrm{Ti}\right]_{2}\left(\mu_{2}, \eta^{2}, \eta^{2}-\mathrm{N}_{2}\right)$ and $\left[\left(\eta^{5}-\mathrm{C}_{5} \mathrm{H}_{5}\right)_{2-}\right.$

### Computational Studies on $[(\eta^5\text{-}C_5Me_nH_{5-n})_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$

$\text{Ti}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ allow us to conclude that at the ground triplet electronic state these complexes cannot react with an $\text{H}_2$ molecule under mild conditions. In other words, Ti complexes $[(\eta^5\text{-}C_5Me_4H)_2\text{Ti}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ and $[(\eta^5\text{-}C_5H_5)_2\text{Ti}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ are not expected to react with an $\text{H}_2$ molecule because they have triplet ground states and, consequently, a weak $\text{Ti}-\text{N}_2$ interaction and a strong $\text{N}-\text{N}$ bond.

For the triplet-state Zr complexes the relative energy of the reactants, as well as the barrier for $\text{H}_2$ addition, is almost the same (or a few kilocalories per mole larger) as those for the singlet state reactants. However, the triplet-state reaction is endothermic (by 3.1(8.2) and 0.2 (5.2) kcal/mol for $n =$ 0 and 4, respectively), while the singlet-state reaction is exothermic. Therefore, we expect that reaction 2 for the Zr complexes takes place in the singlet state.

For the triplet-state Hf complexes, reaction 2 is found to be exothermic (by 13.1 (8.0) and 5.8 (0.3) kcal/mol for $n =$ 0 and 4, respectively) and has a 13.1(15.7) and 18.7 (21.2) kcal/mol barrier calculated relative to the triplet-state reactants for $n =$ 0 and 4, respectively. Since the ground states of the Hf complexes are clearly the singlet states and the singlet transition state is energetically lower than the triplet state, reaction 2 for the Hf complexes is expected take place entirely in the singlet state.

### 4. Conclusions

In summary, we can draw the following conclusions from the above-presented discussion:

1. The ground electronic state of both $[(\eta^5\text{-}C_5Me_4H)_2\text{M}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ and $[(\eta^5\text{-}C_5H_5)_2\text{M}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ is the triplet state for $\text{M} =$ Ti, but it is the closed-shell singlet state for $\text{M} =$ Zr and Hf. The HOMO and LUMO of these complexes in the singlet states are the $\text{M}-\text{N}_2-\text{M}$ $\pi$-bonding and metal $\sigma$-nonbonding orbitals, respectively. For the triplet state of the Hf complexes, SOMO-2 and SOMO-1 are similar to the singlet HOMO and LUMO, respectively. On the other hand, for Zr and Ti complexes, while SOMO-1 is very similar to singlet state LUMO, SOMO-2 corresponds to antisymmetric combination of metal d orbitals and has lost most of the $\text{M}-\text{N}_2-\text{M}$ bonding character (especially for $\text{M} =$ Ti).

2. In the closed-shell singlet electronic state, all the complexes studied satisfy known necessary conditions (they have a side-on-coordinated $\text{N}_2$ molecule and appropriate frontier orbitals) for successful addition of an $\text{H}_2$ molecule to the coordinated $\text{N}_2$. As a result, reaction 2 for all these complexes in the singlet state occurs with a reasonable energy barrier and is exothermic. The Hf complexes exhibit slightly larger reactivity than their Zr analogues, which in turn are more reactive than the singlet-state Ti analogues.

3. However, the Ti complexes studied here are unlikely to react with an $\text{H}_2$ molecule because they have triplet ground electronic state with no appropriate frontier orbitals (its frontier orbitals are the singly occupied nonbonding metal d orbitals) for interaction with a coming $\text{H}_2$ molecule. These triplet-state Ti complexes have a weak $\text{M}-\text{N}_2$ interaction and a strong $\text{N}-\text{N}$ bonding. As a result, reaction 2 for triplet Ti complexes has a large energy barrier and is endothermic (lacks a driving force). Thus, $[(\eta^5\text{-}C_5Me_4H)_2\text{Ti}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ and $[(\eta^5\text{-}C_5H_5)_2\text{Ti}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2)$ complexes cannot react with an $\text{H}_2$ molecule because they have a triplet ground electronic state, while their Zr and Hf analogues react with an $\text{H}_2$ molecule because they have singlet ground electronic state.

4. The error introduced by using hybrid and nonhybrid density functionals to describe low-lying spin states of transition metal complexes reduces via first-row > second-row > third-row transition metals. Both hybrid and nonhybrid density functionals can be used to describe low-lying states of the second and third-row transition metal complexes. However, if the energy gap between the low- and high-spin states of the first-row transition metal complexes is only a few kilocalories per mole, one should use both hybrid and nonhybrid density functionals with a caution.

### Acknowledgment.
The use of the facilities of the Cherry Emerson Center for Scientific Computation of Emory University is highly appreciated.

### Supporting Information Available:
Complete ref 23; (Table 1S) The B3LYP/CEP-31G(d$_N$)-calculated energies (in Hartree) and $<\text{S}^2>$ values; and (Table 2S) Cartesian coordinates (in Å) of the reactants, transition states, and products of the reaction $[(\eta^5\text{-}C_5Me_nH_{5-n})_2\text{M}]_2(\mu_2,\eta^2,\eta^2\text{-}N_2) + \text{H}_2 \rightarrow [(\eta^5\text{-}C_5Me_nH_{5-n})_2\text{M}][(\eta^5\text{-}C_5Me_nH_{5-n})_2\text{MH}](\mu_2,\eta^2,\eta^2\text{-}NNH)$ in their closed-shell singlet and triplet states. This material is available free of charge via the Internet at http://pubs.acs.org.

IC062405B

---

_Inorganic Chemistry, Vol. 46, No. 7, 2007 2715_