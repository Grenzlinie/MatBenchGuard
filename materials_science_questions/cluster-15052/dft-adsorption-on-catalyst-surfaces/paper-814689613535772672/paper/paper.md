# A cluster DFT study of $NH_3$ and NO adsorption on the $(MoO_2)^{2+}$/HZSM-5 surface: Lewis versus Brønsted acid sites

Zhifeng Yan $^{a,b}$, Zhijun Zuo $^{c}$, Zhe Li $^{a,*}$, Jinshan Zhang $^{b}$

$^{a}$ College of Chemistry and Chemical Engineering, Taiyuan University of Technology, Taiyuan 030024, Shanxi, China
$^{b}$ College of Material Science and Engineering, Taiyuan University of Technology, Taiyuan 030024, Shanxi, China
$^{c}$ Key Laboratory of Coal Science and Technology of Ministry of Education and Shanxi Province, Taiyuan University of Technology, Taiyuan 030024, Shanxi, China

---

## ARTICLE INFO

**Article history:**
Received 15 September 2014
Received in revised form 10 October 2014
Accepted 10 October 2014
Available online 18 October 2014

**Keywords:**
DFT
$(MoO_2)^{2+}$/HZSM-5
Lewis acid site
Brønsted acid site
$NH_3$ adsorption
NO adsorption.

## ABSTRACT

A systematic DFT study was carried out to investigate $NH_3$ and NO adsorption on both Lewis and Brønsted acid sites of $(MoO_2)^{2+}$/HZSM-5 catalyst by using cluster models. The adsorption energy results indicate that $NH_3$ could strongly adsorb on both Lewis and Bronsted acid sites in the form of coordinated $NH_3$ and $NH_4^{+}$, respectively, whereas NO represents poorer adsorption ability. It is also found that Lewis and Brønsted acid sites are competitive energetically for $NH_3$ adsorption. According to the difference in the proposed mechanisms for $NH_3$ adsorption on different acid sites, particular attention has been focused on the first dissociation of coordinated $NH_3$ for Lewis acid site and the effect of Mo site on the introduction of NO for Brønsted acid site. For the coordinated $NH_3$ on Lewis acid site, the more electron donation from $NH_3$ is, the greater its adsorption stability is and the higher active its H atoms are. In addition, DOS results show that stability of the H atoms is enhanced by interacting with framework oxygen and especially the H atoms chemical-bonded with framework oxygen. For the $NH_4^{+}$ on Brønsted acid site, reduced-state $Mo^{5+}$ holds stronger reducibility and oxidizability than terminal oxygen, which is suggested to play a key role in adsorption and activation of $NO_x$ together with the adsorbed $NH_4^{+}$.

Crown Copyright © 2014 Published by Elsevier B.V. All rights reserved.

---

## 1. Introduction

Nitrogen oxides ($NO_x$) from automobile exhaust emissions and industrial processes are the major source of air pollution and several methods have been proposed to meet the current $NO_x$ legislation emission limits. It is widely accepted that selective catalytic reduction (SCR) of $NO_x$ by $NH_3$ to produce $N_2$ and $H_2O$ is the most effective technique being able to reduce $NO_x$ emission at ppm levels [1]. The commercial catalysts used today for this SCR reaction are $V_2O_5$-$MoO_3$ ($WO_3$)/$TiO_2$, where $MoO_3$ behave as "chemical" promoter for SCR reaction besides playing "structural" promoter for the catalyst [2,3]. Nevertheless, the high oxidation ability of $SO_2$ to $SO_3$ and the toxicity of $V_2O_5$ to the environment and human health prohibit the employment of $V_2O_5$ as active center [4–6]. Furthermore, the use of $TiO_2$ as support is limited by its low resistance to sintering, low surface area and high cost [1]. Therefore, great efforts have been made to develop new catalysts to avoid the above defects.

Most research about SCR catalysts deal with $MoO_x$ species as promoter. Focusing growing attention on its high promotional effect, in recent years, catalysts loaded with only $MoO_x$ species acting as active component not promoter, such as Mo/HZSM-5 [7–11], $MoO_3$/$TiO_2$ [3,12,13] and $MoO_3$/$CeO_2$ [6,14] have been applied to study the catalytic performances for SCR reaction of $NO_x$. Wang et al. [7] investigated the $C_2H_2$-SCR reaction of NO over Mo/HZSM-5 and the results demonstrated that appropriate amount of Mo incorporation to HZSM-5 considerably enhance the title reaction, both by accelerating the intermediate formation and by strengthening the adsorption of $NO_x$ on the catalyst surface. Salgado et al. [8] found that Mo/HZSM-5 catalyst for $C_2H_5OH$-SCR of NO is less active but has a high selectivity to $N_2$, which is consistent with $NH_3$-SCR experiments results from Li et al. [9,10]. Furthermore, Li et al. also pointed out that the catalytic performances of Mo/HZSM-5 for SCR of NO is strongly influenced by different synthesis methods, Si/Al ratio and the Mo content loaded on ZSM-5, which may be related with the surface structure of $MoO_x$ species.

However, the structure of $MoO_x$ active center of Mo/HZSM-5 catalyst is still a matter of debate in the literature. The difficulties in distinguishing the $MoO_x$ active center lie in the low loading of Mo as well as the coexistence of the external surface and the

---

* Corresponding author. Tel.: +86 351 6018975; fax: +86 351 6018975.
E-mail address: lizhe@tyut.edu.cn (Z. Li).

http://dx.doi.org/10.1016/j.apsusc.2014.10.048
0169-4332/Crown Copyright © 2014 Published by Elsevier B.V. All rights reserved.

inner-channel $MoO_x$ species [15]. By using Raman and X-ray absorption spectroscopy (XAS), Iglesia and co-workers [16–19] proposed a structure of $(Mo_2O_5)^{2+}$ dimer as active center associating with two neighboring Brønsted acid sites, which is consistent with some other studies [20–23]. However, other groups rather suggested a monomer, either $(MoO_2)^{2+}$ or $(MoO_2)^{2+}$ anchored, respectively, on one or two Brønsted acid sites [24–31]. By using H/D isotope exchange and $^{27}$Al MAS NMR and $NH_3$-TPD, Tessonnier et al. [32,33] claimed that the anchoring mode of $MoO_x$ active center is strongly linked with the Si/Al ratio of the starting ZSM-5 zeolite: the $(MoO_2)^{2+}$ monomer at low Si/Al ratio and the $(Mo_2O_5)^{2+}$ dimer at high Si/Al ratio. The results of density functional theory (DFT) calculations showed that the $(MoO_2)^{2+}$ monomer and $(Mo_2O_5)^{2+}$ dimer may coexist in the actual samples and $(MoO_2)^{2+}$ monomer is more tightly connected with the frameworks than the $(Mo_2O_5)^{2+}$ dimer [34]. Therefore, $(MoO_2)^{2+}$ monomer was chosen as the anchoring mode and $(MoO_2)^{2+}/$HZSM-5 was built to represent the Mo/HZSM-5 in this paper.

Adsorption performances of $NH_3$ and NO play an important role in the SCR reaction and their adsorption properties are related to the type of active sites on the catalyst surface. Peng et al. [6] suggested that $MoO_x$ species provides $MoO_3$–$CeO_2$ catalysts with Brønsted acid site. Based on the FT-IR data for $V_2O_5$–$MoO_3$/TiO$_2$, Busca and co-workers [35] deduced that $MoO_x$ species of Mo/TiO$_2$ act as Lewis sites in adsorbing and activating $NH_3$ and the coordinated $NH_3$ will be oxidized to $NH_2$ which later reacts with NO giving adsorbed nitrosamide. Furthermore, $NH_3$-TPD and FT-IR results from Lietti et al. indicated that $NH_3$ could be coordinatively held over Lewis acid sites (associated with Ti, V and Mo surface cation species) and be protonated as $NH_4^+$ ions over Mo–OH or V–OH Brønsted sites of $V_2O_5$–$MoO_3$/TiO$_2$ catalysts [3]. Unfortunately, a detailed adsorption investigation of $NH_3$ and NO on Mo/HZSM-5 catalyst surfaces with the DFT is absent by far.

In this paper, $(MoO_2)^{2+}/$HZSM-5 was built to represent the Mo/HZSM-5. Aiming to understand the initial step of the $NH_3$-SCR reaction of NO on Mo/HZSM-5 catalyst, DFT approach was performed to investigate how $NH_3$ and NO adsorb on both Lewis and Brønsted acid sites of $(MoO_2)^{2+}/$HZSM-5 catalyst models. And then the electronic properties of adsorption structures were analyzed to predict the next step of the proposed reaction mechanism. We hope that the results may be extended to understand the initial step of the SCR mechanism on other catalysts loaded with only $MoO_x$ species acting as active component.

## 2. Computational models and details

In the unit cell of ZSM-5, there are 12 distinct tetrahedral Si sites for Al cation substitution, denoted as T sites (T1–T12) [36]. The substitution of $Si^{4+}$ by $Al^{3+}$ introduces a negative charge, which is compensated by one $H^+$ and an acidic bridging hydroxyl group (Brønsted acid site) is formed. For ZSM-5 zeolite, there is no experimental information about the preferential site for Si/Al substitution. Several theoretical investigations tried to address this issue but the results did not show significant differences between the relative energies of ZSM-5 structures with Al in different T sites [37,38]. For double Si/Al substitutions of ZSM-5, Lowenstein's rule [39] indicated that one Al cannot be connected directly to another Al through an oxygen atom (Al–O–Al linkage), the nearest-neighbor tetrahedral sites are all Si. Therefore, the closest Al's are at next-nearest neighbor (NNN) sites [30]. Zhou et al. [34] confirmed that two NNN B-acid sites can build a stable $(MoO_2)^{2+}$ monomer but two next-next-nearest-neighbor (NNNN) B-acid sites are too far to associate $(MoO_2)^{2+}$. Consequently, the double Si/Al substitutions at T3T12 sites as suggested by Zhou et al. [34] were chosen for location of $(MoO_2)^{2+}$ monomer. A 20T cluster, which includes the full 12-membered ring, was cut from ZSM-5 framework for investigation (Fig. 1). The dangling bond on the second shell framework O or Si atoms was saturated with H atom and with O–H and Si–H distances fixed at 1.00 and $1.46\mathring{A}$, respectively, oriented along the bond direction to what would otherwise have been the next framework atoms. During the calculations, the atomic coordinates in the external two layers of the zeolite clusters (O–H and Si–H) were fixed in their original crystallographic positions to retain the zeolite structure, while other atoms were relaxed. The structures of the $MoO_2(OH)_2$ molecule and HZSM-5 cluster were constructed and optimized first. Then the $(MoO_2)^{2+}$ part was cut and grafted onto HZSM-5 cluster model to build $(MoO_2)^{2+}/$HZSM-5 and $MoSi_{18}Al_2O_{53}H_{30}$ was formed, which was optimized to study the adsorption performances of $NH_3$ and NO on both Lewis and Brønsted acid sites.

All calculations were performed with the DFT method by running the program package Dmol³ in Materials Studio [40,41]. The exchange-correlation potential was treated within the local density approximation (LDA) with the Perdew Wang (PWC) functional [42] and the generalized gradient approximation (GGA) of Perdew–Wang (PW91) exchange correlation interactions [43]. The atomic core representation of ECP (relativistic effective core potentials) was selected [44,45], in which all-electron calculations were done for H, O, Si and Al atoms. The Mo atom was presented by valence basis set with the $[Ar]3d^{10}$ core described by a model core potential, so we could treat the outer shell electrons (4s, 4p, 4d, 5s) only. Double-numeric quality basis set with polarization function (DNP) were performed to describe the valence orbital of all the atoms in our calculations. A self-consistent field procedure is carried out with a convergence criterion of $10^{-5}$ a.u. for both the energy and electron density. Geometry optimizations are performed under no symmetry constraints, with a convergence criterion of $10^{-3}$ a.u. for the gradient, and $10^{-3}$ a.u. for the displacement.

The adsorption energy $E_{\text{ads}}$ was expressed as the following equation: $E_{\text{ads}} = E_{\text{molecule/cluster}} - E_{\text{cluster}} - E_{\text{molecule}}$, where $E_{\text{molecule/cluster}}$ is the total energy of the cluster with the adsorbed $NH_3$ or NO molecule, $E_{\text{cluster}}$ is the total energy of the cluster itself and $E_{\text{molecule}}$ is that of free $NH_3$ or NO molecule. a more negative $E_{\text{ads}}$ corresponds to a stronger binding of the adsorbed molecule on the cluster. The bonding characteristics and electronic properties were examined by the Mulliken population analysis [46–49], Mayer bond order indices [50,51], Fukui function and density of states (DOS) analysis. With the present computational method, the determined bond lengths for free $NH_3$ and NO molecules in gas phase are, respectively, 1.023 and $1.154\mathring{A}$, in agreement with the experimental values of $1.012\mathring{A}$ for $NH_3$ [52] and $1.151\mathring{A}$ for NO [53], respectively.

## 3. Results

### 3.1. Structure and properties of the $(MoO_2)^{2+}/$HZSM-5 substrate model

The optimized $(MoO_2)^{2+}/$HZSM-5 cluster model is shown in Fig. 2 (denoted as L-model) and corresponding structural parameters are listed in Table 1. The terminal hydrogens in all models are veiled for simplicity. The Mo atom bears tetrahedral symmetry and bridges nearly symmetrically on Si3–O20′–Al12–O24–Si12–O20–Al3. By using LDA/PWC method, the bond lengths between Mo and framework oxygen ($O_F$) atoms in bridge Si3–O20′–Al12, Al12–O24–Si12 and Si12–O20–Al3 are 2.224, 2.036 and $2.122\mathring{A}$, respectively. Bond lengths of 1.695 and $1.698\mathring{A}$ and bond order indices of 2.158 and 2.110 describe Mo=O double bond for terminal Mo–O$_I$ and Mo–O$_{II}$ bonds, respectively. These bond lengths of Mo=O double bond are in good agreement

![](./images/814689613535772672_1.jpg)

Fig. 1. Structure of ZSM-5 zeolite with labeled T3 and T12 sites; (a) in view of (100); (b) in view of (010).

![](./images/814689613535772672_2.jpg)

Fig. 2. Optimized structure of $(MoO_{2})^{2+}$/HZSM-5. The labels of ZSM-5 framework atoms correspond to the ZSM-5 crystallographic structure.

<table>
<caption>Table 1
Bond length (Å) and bond order in parentheses of the $(MoO_{2})^{2+}$/HZSM-5.</caption>
<thead>
<tr>
<th>Bond</th>
<th>This work</th>
<th colspan="2">B3LYP/6-31G** [34]</th>
</tr>
<tr>
<th></th>
<th>PWC</th>
<th>PW91</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Mo–O<sub>I</sub></td>
<td>1.695 (2.158)</td>
<td>1.704 (2.093)</td>
<td>1.693</td>
</tr>
<tr>
<td>Mo–O<sub>II</sub></td>
<td>1.698 (2.110)</td>
<td>1.708 (2.107)</td>
<td></td>
</tr>
<tr>
<td>Mo–O20'</td>
<td>2.224</td>
<td>2.256</td>
<td>2.372</td>
</tr>
<tr>
<td>Mo–O24</td>
<td>2.036</td>
<td>2.048</td>
<td>2.005</td>
</tr>
<tr>
<td>Mo–O20</td>
<td>2.122</td>
<td>2.134</td>
<td>2.117</td>
</tr>
<tr>
<td>Mo–Al12</td>
<td>2.937</td>
<td>2.962</td>
<td>3.036</td>
</tr>
<tr>
<td>Mo–Al3</td>
<td>3.784</td>
<td>3.799</td>
<td>3.733</td>
</tr>
</tbody>
</table>

with the experimental data $1.69 \pm 0.008$ Å for the length of the Mo=O double bond of Mo/HZSM-5 catalysts [19]. The Mo atom is closer to Al12 with a Mo-Al12 distance of 2.937 Å, while more distant to Al3 with 3.784 Å in Mo-Al3. The structural parameters are in good agreement with the calculation results from Zhou et al. [34]. Compared with the LDA/PWC method, the GGA/PW91 method overestimates the bond lengths. In contrast, the LDA/PWC method gives more reasonable geometries with respect to the reported experimental [19] and calculational [34] results. Therefore, LDA with PWC method is employed this paper.

The Fukui function has been widely used as a single-reactant chemical reactivity descriptor [54]. In general, for a system with $n$ electrons, the two Fukui functions proposed by Yang [55] are:

$$
f_{k}^{-}=q_{k}(n)-q_{k}(n-1)
$$

$$
f_{k}^{+}=q_{k}(n+1)-q_{k}(n)
$$

where $q_{k}(n)$, $q_{k}(n+1)$ and $q_{k}(n-1)$ represent the electronic population of atom $k$ in the system with $n$, $n+1$ and $n-1$ electrons, respectively. The two Fukui function indices provide a successful way of measuring the reactivity of regions of clusters [56-58]. The local site with high $f_{k}^{-}$ value will easily react with electron acceptors, whereas the local site where $f_{k}^{+}$ is large will well react with electron donors. As seen in Table 2, both Mo and terminal oxygen atoms of L-model have high $f^{+}$ values and very low $f^{-}$ values, showing that $(MoO_{2})^{2+}$ of $(MoO_{2})^{2+}$/HZSM-5 prefers to accept electron but has little ability to donate electron. Furthermore, higher $f^{+}$ value for Mo atom than that for terminal oxygen atoms means Mo suffers from electrophilic attack easily. The features of the HOMO and LUMO of $(MoO_{2})^{2+}$/HZSM-5 can be seen in Fig. 3. In the HOMO, the electron density is mainly accumulated the $O_{F}$ atoms around Al3 atom. This is attributed to the fact that only one Mo-O20 bond is not enough to saturate the electrons caused by $Si_{3}/Al_{3}$ substitution. In the case of LUMO, electron density is mainly localized on the $(MoO_{2})^{2+}$ part and little is localized on the $O_{F}$ atoms connected with $(MoO_{2})^{2+}$. The frontier orbital theory analysis denotes that $(MoO_{2})^{2+}$ of $(MoO_{2})^{2+}$/HZSM-5 tend to undergo nucleophilic molecule adsorption, which is well consistent with the calculations of Fukui function.

### 3.2. $NH_{3}$ adsorption on Lewis acid site of $(MoO_{2})^{2+}$/HZSM-5

As displayed in Fig. 4, $NH_{3}$ molecule can adsorb on L-model in two ways: N-down (N atom of $NH_{3}$ bonds to $(MoO_{2})^{2+}$) and H-down (H atoms of $NH_{3}$ bonds to $(MoO_{2})^{2+}$). For the three adsorption structures of N-down in Fig. 4a-c (denoted as N1-NH₃, N2-NH₃

<table>
<caption>Table 2
Calculated Fukui function indices for Mo, O<sub>I</sub> and O<sub>II</sub> atoms and Mayer total valence (MTV) for Mo atom in different structures.</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>L-model</th>
<th>N1-NH₃</th>
<th>N2-NH₃</th>
<th>N3-NH₃</th>
<th>B-model</th>
<th>B-NH₃</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mo</td>
<td>$f_{k}^{-}$</td>
<td>0.007</td>
<td>0.019</td>
<td>0.013</td>
<td>–0.001</td>
<td>0.199</td>
<td>0.253</td>
</tr>
<tr>
<td></td>
<td>$f_{k}^{+}$</td>
<td>0.192</td>
<td>0.144</td>
<td>0.179</td>
<td>0.149</td>
<td>0.215</td>
<td>0.266</td>
</tr>
<tr>
<td>O<sub>I</sub></td>
<td>$f_{k}^{-}$</td>
<td>0.007</td>
<td>–0.011</td>
<td>–0.021</td>
<td>0</td>
<td>0.101</td>
<td>0.138</td>
</tr>
<tr>
<td></td>
<td>$f_{k}^{+}$</td>
<td>0.162</td>
<td>0.144</td>
<td>0.172</td>
<td>0.157</td>
<td>0.103</td>
<td>0.138</td>
</tr>
<tr>
<td>O<sub>II</sub></td>
<td>$f_{k}^{-}$</td>
<td>0.018</td>
<td>0.007</td>
<td>0.038</td>
<td>0.024</td>
<td>0.134</td>
<td>0.137</td>
</tr>
<tr>
<td></td>
<td>$f_{k}^{+}$</td>
<td>0.156</td>
<td>0.142</td>
<td>0.142</td>
<td>0.144</td>
<td>0.140</td>
<td>0.137</td>
</tr>
<tr>
<td>Mo(MTV)</td>
<td></td>
<td>6.3</td>
<td>6.5</td>
<td>6.5</td>
<td>6.6</td>
<td>5.3</td>
<td>5.3</td>
</tr>
</tbody>
</table>

![](./images/814689613535772672_3.jpg)

Fig. 3. HOMO and LUMO plots of $(MoO_{2})^{2+}$/HZSM-5: (a) HOMO; (b) LUMO.

![](./images/814689613535772672_4.jpg)

Fig. 4. Optimized structures of $NH_{3}$ adsorption on Lewis acid site of $(MoO_{2})^{2+}$/HZSM-5: (a) N1-$NH_{3}$; (b) N2-$NH_{3}$; (c) N3-$NH_{3}$; (d) H-down.

![](./images/814689613535772672_5.jpg)

Fig. 5. Optimized structures of Brønsted acid site model and $NH_{3}$ adsorption on Brønsted acid site model: (a) B-model; (b) B-$NH_{3}$.

![](./images/814689613535772672_6.jpg)

Fig. 6. Optimized structures of NO adsorption as N-down on Lewis and Brønsted acid sites of (MoO₂)²⁺/HZSM-5: (a) Mo-NO; (b) O-NO; (c) H-NO.

and N3-NH₃, respectively), the corresponding adsorption energies are −2.02, −2.44 and −2.77 eV, respectively. However, the adsorption energy of NH₃ adsorption as H-down is only −0.23 eV (see in Fig. 4d), together with the long distances between (MoO₂)²⁺ and H atoms of NH₃ (2.110, 2.146 and 2.171 Å), indicating much poorer adsorption ability compared with the adsorption structures as N-down. Therefore, we focus our attention on NH₃ adsorption as N-down on Lewis acid site in this paper. The bond lengths of formed Mo-N bond in N1-NH₃, N2-NH₃ and N3-NH₃ are 2.198, 2.103 and 2.140 Å, respectively. The length of Hᵢ-O2′ (2.298 Å) and bond angle of N-Hᵢ. . .O2′ for N1-NH₃ (130.9°) imply hydrogen bonding interaction, which is also the same with Hᵢᵢ-O3 (2.319 Å) and N-Hᵢᵢ. . .O3 (121.3°) for N3-NH₃. On the other hand, the Hᵢ-O20′ length for N2-NH₃ is 1.633 Å and the Hᵢ-O2 length for N3-NH₃ is 1.696 Å, which suggest strong hydrogen bonding or a new chemical bond. Owing to the formation of Mo-N bond and the interaction between H atoms and Oբ atoms, the length of Mo-Oբ, Mo-Oᵢ and Mo-Oᵢᵢ bonds are elongated slightly. Especially in the case of N2-NH₃, Mo-O20′ is elongated to break and the broken O20′ bonds to Hᵢ of NH₃ instead.

### 3.3. NH₃ adsorption on Brønsted acid site of (MoO₂)²⁺/HZSM-5

For NH₃ adsorption on Brønsted acid site, at first Brønsted acid site is modeled by adding one H atom to Oᵢ generating hydroxyl group as mentioned from other research [59-62]. After geometry optimization, these two atoms bond tightly with a Oᵢ-Hᵢ bond and the bond length is 0.993 Å. The optimized structures and that of NH₃ adsorption on Brønsted acid site are shown in Fig. 5 (denoted as B-model and B-NH₃, respectively). N atom of NH₃ bonds to Hᵢ atom of Brønsted acid site and simultaneously Oᵢ-Hᵢ bond breaks, leading to the generation of NH₄⁺. The newly formed NH₄⁺ locates upon (MoO₂)²⁺ and the length of Oᵢ-Hᵢ and Oᵢᵢ-Hᵢᵢ are 1.831 and 1.860 Å, respectively. Together with the bond angle of N-Hᵢ. . .Oᵢ (143.1°) and N-Hᵢᵢ. . .Oᵢᵢ (150.8°), it suggests the hydrogen bonding interaction. The formation of NH₄⁺ results in an obvious change of (MoO₂)²⁺/HZSM-5 structure that Mo atom turns to bridge nearly symmetrically on Al12-O24-Si12-O20-Al3 with Mo-O24 length of 2.067 Å and Mo-O20 length of 2.045 Å. The high adsorption energy of −2.25 eV indicates a strong exothermic adsorption process. Compared with the adsorption energy results of NH₃ adsorption on Lewis acid site, it is found that Lewis and Brønsted acid sites are competitive energetically for NH₃ adsorption. A similar conclusion has been reached by NH₃ adsorption onto H-BEA and H-MFI zeolites [63].

### 3.4. NO adsorption on (MoO₂)²⁺/HZSM-5

Two orientations of the NO molecule with respect to (MoO₂)²⁺/HZSM-5 are considered: one is N-down and the other is O-down on Mo atom or terminal oxygen (Oᵢ) of Lewis acid site and H atom of Brønsted acid site, respectively. These six initial structures are optimized and the optimized structures are shown is Fig. 6 (denoted as Mo-NO, O-NO and H-NO, respectively). The results reveal that N-down structures are stable but O-down structures are unstable. For the three adsorption structures as N-down, adsorption energies are −0.84, −0.68 and −0.70 eV with generated N-Mo bond length of 2.351 Å, N-O bond length of 1.905 Å and N-H bond length of 1.417 Å, respectively. Compared with the bond length of 1.154 Å for NO free molecule, it is slightly shorten to 1.136, 1.126 and 1.144 Å after NO adsorption on Mo, Oᵢ and H atoms, respectively, suggesting that NO is less active after adsorption. It is also obvious from Table 5 that the electron donations from NO to (MoO₂)²⁺/HZSM-5 are 0.272, 0.313 and 0.129e, respectively.

<table><caption>Table 3 Calculated bond length ($d$, Å), bond order ($p$, in parentheses), bond angle ($\angle$N–H–O, deg), Mulliken charge ($q$, e) and adsorption energies ($E_{\text{ads}}$, eV) of NH₃ adsorption as N-down on Lewis acid site.</caption>
<tbody><tr><th></th><td>N1–NH₃</td><td>N2–NH₃</td><td>N3–NH₃</td></tr>
<tr><th>$d_{\text{Mo-N}}$ ($p$)</th><td>2.198 (0.663)</td><td>2.103 (0.833)</td><td>2.140 (0.780)</td></tr>
<tr><th>$d_{\text{Mo-OI}}$ ($p$)</th><td>1.702 (2.124)</td><td>1.704 (2.137)</td><td>1.702 (2.133)</td></tr>
<tr><th>$d_{\text{Mo-OII}}$ ($p$)</th><td>1.703 (2.107)</td><td>1.697 (2.102)</td><td>1.705 (2.082)</td></tr>
<tr><th>$d_{\text{Mo-O20}'}$</th><td>2.354</td><td>3.308</td><td>2.598</td></tr>
<tr><th>$d_{\text{Mo-O24}}$</th><td>2.047</td><td>2.202</td><td>2.047</td></tr>
<tr><th>$d_{\text{Mo-O20}}$</th><td>2.367</td><td>2.001</td><td>2.199</td></tr>
<tr><th>$d_{\text{HIII-O}}$ a ($p$)</th><td>2.298</td><td>1.633 (0.155)</td><td>1.696 (0.142)</td></tr>
<tr><th>$d_{\text{HIII-O}}$ a</th><td>–</td><td>–</td><td>2.319</td></tr>
<tr><th>$\angle$N–Hᵢ–Oᵃ</th><td>130.9</td><td>152.4</td><td>152.3</td></tr>
<tr><th>$\angle$N–Hᵢᵢ–Oᵃ</th><td>–</td><td>–</td><td>121.3</td></tr>
<tr><th>$d_{\text{N-HII}}$</th><td>1.033</td><td>1.061</td><td>1.054</td></tr>
<tr><th>$d_{\text{N-HIII}}$</th><td>1.032</td><td>1.047</td><td>1.035</td></tr>
<tr><th>$d_{\text{N-HIIII}}$</th><td>1.032</td><td>1.031</td><td>1.030</td></tr>
<tr><th>$q_{\text{NH3}}$</th><td>0.421</td><td>0.456</td><td>0.466</td></tr>
<tr><th>$q_{\text{Mo}}$</th><td>1.106</td><td>1.131</td><td>1.103</td></tr>
<tr><th>$q_{\text{N}}$</th><td>–0.508</td><td>–0.582</td><td>–0.518</td></tr>
<tr><th>$E_{\text{ads}}$</th><td>–2.02</td><td>–2.44</td><td>–2.77</td></tr>
<tr><td colspan="4">a O atom corresponds to the oxygen atom interacting with the indicated Hᵢ or Hᵢᵢ atom in different adsorption structures.</td></tr>
</tbody></table>

In fact, the electron donation from NO molecule to substrate will reduce the occupation of pπ* antibonding orbital of NO, so the N–O bonding will be enhanced and as a result the N–O bond length will be shorten [64].

### 4. Discussion

The adsorption energy results clearly reveal that NH₃ adsorption is much more favorable energetically than NO adsorption on both Lewis and Brønsted acid sites. This means that the first step of the SCR reaction on (MoO₂)²⁺/HZSM-5 catalyst is adsorption of NH₃ on acid site rather than NO, which is consistent with the researches on other catalysts such as V₂O₅ [3,35,61,65–67], Fe/HZSM-5 [68], CuO/γ-Al₂O₃ [59] and MnOₓ [69] catalysts. Consequently, it is not further discussed about NO adsorption here.

With respect to the proposed reaction mechanism, the adsorption site of NH₃ is still a matter of debate. Most authors suggest that NH₃ adsorbs on Lewis acid site in the form of coordinated NH₃ first [35,66,67]. The coordinated NH₃ may be activated by H abstraction to form NH₂ (amide), and then NH₂ (or the coordinated NH₃ suggested by few investigators) reacts with gas phase or adsorbed NO. The others suggest that the SCR reaction begins with the NH₃ adsorption on Brønsted acid site as NH₄⁺, which later reacts with gas phase or adsorbed NO [66,67]. The former mechanism is proposed for V₂O₅-based catalysts [3,35,65–67] and transition metal-based catalysts such as Fe-, Cu-, Cr- and Mn-based catalysts [35,66,67,70] while the latter is proposed for V₂O₅-based [3,61,65], Fe-based [68] and protonic zeolites [35]. Considering the debate on adsorption sites of the proposed mechanisms and the competitive ability between Lewis and Brønsted acid sites derived from our adsorption energies calculations for NH₃ adsorption, NH₃ adsorption models of these two adsorption sites are discussed toward the next step following the proposed mechanisms. Specifically, the coordinated NH₃ adsorbed on Lewis acid site is analyzed towards its first dissociation, i.e., the activity difference between H atoms of the coordinated NH₃. For the NH₃ adsorption model of Brønsted acid site, particular attention is paid to the effect of Mo site on the introduction of NO to this adsorption model, of which NH₄⁺ interacts with gas phase or adsorbed NO.

<table><caption>Table 4 Calculated bond length ($d$, Å), bond order ($p$, in parentheses), bond angle ($\angle$N–H–O, deg), Mulliken charge ($q$, e) and adsorption energies ($E_{\text{ads}}$, eV) of the NH₃ adsorption on Brønsted acid site.</caption>
<tbody><tr><th></th><td>B-model</td><td>B-NH₃</td></tr>
<tr><th>$d_{\text{Mo-OI}}$ ($p$)</th><td>1.862 (1.189)</td><td>1.727 (1.932)</td></tr>
<tr><th>$d_{\text{Mo-OII}}$ ($p$)</th><td>1.686 (2.128)</td><td>1.736 (1.854)</td></tr>
<tr><th>$d_{\text{Mo-O20}'}$</th><td>2.344</td><td>2.910</td></tr>
<tr><th>$d_{\text{Mo-O24}}$</th><td>2.002</td><td>2.067</td></tr>
<tr><th>$d_{\text{Mo-O20}}$</th><td>2.101</td><td>2.045</td></tr>
<tr><th>$d_{\text{OI-HI}}$</th><td>0.993</td><td>1.831</td></tr>
<tr><th>$d_{\text{OII-HIII}}$</th><td>–</td><td>1.860</td></tr>
<tr><th>$\angle$N–Hᵢ–Oᵢ</th><td>–</td><td>143.1</td></tr>
<tr><th>$\angle$N–Hᵢᵢ–Oᵢᵢ</th><td>–</td><td>150.8</td></tr>
<tr><th>$d_{\text{N-H}}$ a</th><td></td><td>1.043–1.054</td></tr>
<tr><th>$q_{\text{NH4+}}$</th><td>–</td><td>0.813</td></tr>
<tr><th>$q_{\text{Mo}}$</th><td>1.218</td><td>1.126</td></tr>
<tr><th>$E_{\text{ads}}$</th><td>–</td><td>–2.25</td></tr>
</tbody></table>

![](./images/814689613535772672_7.jpg)

Fig. 7. PDOS of N and Mo atoms before and after NH₃ adsorption on Lewis acid site in N1–NH₃, N2–NH₃ and N3–NH₃.

### 4.1. NH₃ adsorption on Lewis acid site of (MoO₂)²⁺/HZSM-5

To elucidate the bonding characteristics quantitatively, Mulliken population analysis was performed and the results were listed in Table 3. The stability of adsorbed NH₃ seems to be related to its electron donation to (MoO₂)²⁺/HZSM-5. The more electron donation from NH₃ is, the greater its adsorption stability is, suggesting strong covalent contribution to the adsorption interactions. For the three N-down adsorption models, the Mo–N bond in N2–NH₃ holds the shortest bond length (2.103 Å), the largest bond order (0.833) and the most Mulliken charge density for Mo atom (1.131|e|) and N atom (0.582e), indicating the strongest Mo–N interaction. The calculated bond order indices of Hᵢ–O20′ in N2–NH₃ and Hᵢ–O2 in N3–NH₃ are 0.155 and 0.142, respectively, which denote indeed the formation of new chemical bonds there. Compared with the bond length and bond order (0.984) of N–H for free NH₃ molecule, all N–H bonds are slightly activated after NH₃ adsorption as N-down, in which the N–Hᵢ in both N2–NH₃ and N3–NH₃ are activated higher than others for its new chemical bond with Of.

To obtain further insights into the bonding mechanism, the partial densities of states (PDOS) of Mo, N, Hᵢ, Hᵢᵢ and Hᵢᵢᵢ in N1–NH₃, N2–NH₃ and N3–NH₃ were shown in Figs. 7 and 8. For the purpose of comparison, the PDOS of Mo, N and H before NH₃ adsorption were also plotted. In all PDOS plots, the Fermi level was set to zero as a reference and represented with a dotted line. Upon NH₃ adsorption, the PDOS of N shifts to the left that with lower energies accompanying with the decrease and the broadness of peaks in all

![](./images/814689613535772672_8.jpg)

Fig. 8. PDOS of H atoms before and after NH₃ adsorption on Lewis acid site in N1-NH₃, N2-NH₃ and N3-NH₃.

![](./images/814689613535772672_9.jpg)

Fig. 9. The energy levels of frontier molecular orbital for NH₃ molecule and (MoO₂)²⁺/HZSM-5.

the three N-down adsorption models, as shown in Fig. 7. The obvi- ous hybridizations between Mo-d and N-s, p orbitals suggest the strong covalent interaction between Mo and N atoms. The peaks of N-s orbital around 7 eV and N-p orbital around 9 eV shift are depleted within the range of Fermi level to 7 eV. This depletion of electron density reveals the donation of electron density from NH₃ to Mo. The N-p peaks seem to show a mixture of states within the energy range of −10 eV to Fermi level. Two sharp features (three for N₂-NH₃) are seen overlaid on a more diffuse background sug- gesting that a combination of localized and delocalized bonding maybe present. Further, the N-p and Mo-d peaks show two corre- lating features within this energy range: they both, to some extent, have broad features, and these broad features overlap in energy. In addition, the splitting N-p orbital around 4 eV in N2-NH₃ is related to the electron charge redistribution, which is caused by the break of Mo-O20' bond.

The donation of electron density from NH₃ to (MoO₂)²⁺/HZSM-5 can also be understood from Fig. 9. Fig. 9 shows the energy levels of frontier molecular orbital for NH₃ molecule and (MoO₂)²⁺/HZSM-5.

<table>
<caption>Table 5
Calculated bond length ($d$, Å), Mulliken charge ($q$, e) and adsorption energies ($E_{\text{ads}}$, eV) of the NO adsorption on (MoO₂)²⁺/HZSM-5.</caption>
<thead>
<tr>
<th></th>
<th>Mo-NO</th>
<th>O-NO</th>
<th>H-NO</th>
</tr>
</thead>
<tbody>
<tr>
<td>N-(MoO₂)²⁺/HZSM-5</td>
<td>2.351</td>
<td>1.905</td>
<td>1.417</td>
</tr>
<tr>
<td>N-O</td>
<td>1.136</td>
<td>1.126</td>
<td>1.144</td>
</tr>
<tr>
<td>$q_{\text{NO}}$</td>
<td>0.272</td>
<td>0.313</td>
<td>0.129</td>
</tr>
<tr>
<td>$E_{\text{ads}}$</td>
<td>−0.84</td>
<td>−0.68</td>
<td>−0.70</td>
</tr>
</tbody>
</table>

![](./images/814689613535772672_10.jpg)

Fig. 10. PDOS of NH₄⁺, Mo and terminal oxygen (Oᵢ and Oᵢᵢ) atoms after NH₃ adsorp- tion on Brønsted acid site.

It can be seen that the energy gap between HOMO of NH₃ and LUMO of (MoO₂)²⁺/HZSM-5 is lower than that between HOMO of (MoO₂)²⁺/HZSM-5 and LUMO of NH₃. Therefore, when NH₃ and (MoO₂)²⁺/HZSM-5 contact and react, electron density is donated from HOMO of NH₃ to LUMO of (MoO₂)²⁺/HZSM-5.

The differences of PDOS of H atoms, which is caused by different adsorption models and their different interactional types with O_F, can be observed in Fig. 8. It is noted that the energy positions of PDOS of H atoms in different adsorption models are correspond- ing to the order of adsorption stability of NH₃. The enhancement of adsorption stability of NH₃ gives rise to the energy positions of its H atoms shift to the right with higher energies. In other words, the greater adsorption stability of NH₃ is, the higher active its H atoms are. In addition, the H-s orbital around −17 eV of the H atom interacting with O_F is delocalized and broaden to the left by more 3 eV than the H atom not interacting with O_F. Notably, in this broaden range the H-s orbital of the H atom chemical-bonded with O_F exhibits much better delocalization than the H atom hydrogen- bonded with O_F. The broadness and delocalization predict that stability of the H atoms is enhanced by interacting with O_F and especially the H atoms chemical-bonded with O_F.

### 4.2. NH₃ adsorption on Brønsted acid site of (MoO₂)²⁺/HZSM-5

As displayed in Table 4, the newly formed NH₄⁺ species car- ries 0.813|e|, meaning the charge transfers from NH₄⁺ to the (MoO₂)²⁺/HZSM-5 in which Mo atom obtains some electrons and is reduced. Mulliken charge analysis show that (MoO₂)²⁺/HZSM-5 acts as an electron acceptor for both NH₃ adsorption and NO adsorption, which is consistent with the frontier orbital theory and the Fukui function analyses for (MoO₂)²⁺/HZSM-5. The Mayer total valence indicates how many single bonds are associated with the atom [71]. The calculated Mayer total valence of Mo atom in NH₃ adsorption model of Brønsted acid site is 5.3 which reveal reduced

state $Mo^{5+}$. This is supported by other experimental researches: Li et al. suggested that $Mo^{4+}$ or $Mo^{5+}$ should be related to active site on Mo/HZSM-5 catalyst for the $NH_3$-SCR reaction of NO [10]. In Fount- zoula et al.'s research, the XPS results also confirmed the presence of reduced $MoO_x$ species on $MoO_3/TiO_2$ catalyst for this reaction [13].

Fig. 10 presents the PDOS of $NH_4^+$, Mo and terminal oxygen ($O_I$ and $O_{II}$) atoms after $NH_3$ adsorption. The PDOS at the Fermi level is essentially contributed by the Mo-d with small contributions from the Mo-s and O-p but not contributed by $NH_4^+$. Furthermore, the PDOS intensity of Mo atom at Fermi level is clearly stronger than that of terminal oxygen atoms, which denotes that Mo atom was more active. Further insights into the activity of Mo and terminal oxygen atoms can be obtained from the Fukui function indices in Table 2. The $f_k^-$ and $f_k^+$ of Mo atom are greater than that of terminal oxygen atoms, respectively, which means that Mo atom is more active than terminal oxygen with respect to whether electrophilic attack or nucleophilic attack. According to the proposed reaction mechanism beginning with $NH_3$ adsorption on Brønsted acid site, the next step should be the reaction between adsorbed $NH_4^+$ and gas phase or adsorbed $NO_x$. Owing to the reducibility and oxidiz- ability of $Mo^{5+}$, it is suggested to play a key role in adsorption and activation of $NO_x$ together with the adsorbed $NH_4^+$.

## 5. Conclusions

$NH_3$ and NO adsorption on Lewis and Brønsted acid sites of $(MoO_2)^{2+}/HZSM-5$ have been investigated based on DFT method by using cluster models. $NH_3$ adsorption is found to be more favorable energetically than NO adsorption on both Lewis and Brønsted acid sites. Our results confirm that the SCR reaction on $(MoO_2)^{2+}/HZSM-5$ catalyst begins with $NH_3$ adsorption on acid site, which is consistent with the researches on other cata- lysts. Furthermore, the adsorption energy results also reveal that Lewis and Brønsted acid sites are competitive energetically for $NH_3$ adsorption, which reveals the fact that in the actual samples $NH_3$ adsorption may take place on both Lewis and Brønsted acid sites.

$NH_3$ adsorbs on Lewis acid site in the form of coordinated $NH_3$ with N atom bonds to Mo atom. $NH_3$ donates electron density to the surface and all the N-H bonds are slightly activated after $NH_3$ adsorption. According to the proposed mechanism beginning with $NH_3$ adsorption on Lewis acid site, the activity difference between H atoms of the coordinated $NH_3$ is analyzed towards its first disso- ciation. The results reveal that there is certain relationship among electron donation from $NH_3$, adsorption stability of $NH_3$ and activ- ity of H atoms. The more electron donation from $NH_3$ is, the greater its adsorption stability is and the higher active its H atoms are. In addition, DOS results show that stability of the H atoms is enhanced by interacting with $O_F$ and especially the H atoms chemical-bonded with $O_F$.

When $(MoO_2)^{2+}/HZSM-5$ is hydrogenated and generated Brønsted acid site, $NH_3$ can adsorb on this Brønsted acid site in the form of $NH_4^+$. According to the proposed mechanism for $NH_3$ adsorption on Brønsted acid site, particular attention is paid to the effect of Mo site on the introduction of NO to this adsorption model, of which $NH_4^+$ interacts with gas phase or adsorbed NO. Mayer total valence results show the presence of reduced state $Mo^{5+}$, which is consistent with other experimental researches. Furthermore, the Fukui function indices indicate that Mo atom is more active than terminal oxygen with respect to whether electrophilic attack or nucleophilic attack. Therefore, Mo site is suggested to play a key role in adsorption and activation of $NO_x$ together with the adsorbed $NH_4^+$.

## Acknowledgements

The authors gratefully acknowledge the financial support from the key program of National Natural Science Foundation of China (No. 21336006) and National Natural Science Foundation of China (No. 21073131).

## References

[1] M. Mhamdi, A. Ghorbel, G. Delahay, Catal. Today 142 (2009) 239-244.
[2] L. Casagrande, L. Lietti, I. Nova, P. Forzatti, A. Baiker, Appl. Catal. B: Environ. 22 (1999) 63-77.
[3] L. Lietti, I. Nova, G. Ramis, L. Dall'Acqua, G. Busca, E. Giamello, P. Forzatti, F. Breganti, J. Catal. 187 (1999) 419-435.
[4] J.P. Dunn, P.R. Koppula, H.G. Stenger, I.E. Wachs, Appl. Catal. B: Environ. 19 (1998) 103-117.
[5] P. Balle, B. Geiger, S. Kureti, Appl. Catal. B: Environ. 85 (2009) 109-119.
[6] Y. Peng, R. Qu, X. Zhang, J. Li, Chem. Commun. 49 (2013) 6215-6217.
[7] X.P. Wang, S.S. Yu, H.L. Yang, S.X. Zhang, Appl. Catal. B: Environ. 71 (2007) 246-253.
[8] A.L.S.M. Salgado, F.B. Passos, M. Schmal, Catal. Today 85 (2003) 23-29.
[9] Z. Li, W. Huang, K.C. Xie, J. Environ. Sci. 17 (2005) 103-105.
[10] Z. Li, K.C. Xie, W. Huang, W. Reschetilowski, Molybdenum loaded on HZSM-5: a catalyst for selective catalytic reduction of nitrogen oxides, in: N.ŽJ. Čejka, P. Nachtigall (Eds.), Studies in Surface Science Catalysis, Elsevier, Prague, 2005, pp. 1741-1748.
[11] Z. Li, W. Huang, K.C. Xie, Chin. J. Catal. 23 (2002) 535-538.
[12] K. Bourikas, C. Fountzoula, C. Kordulis, Appl. Catal. B: Environ. 52 (2004) 145-153.
[13] C. Fountzoula, N. Spanos, H.K. Matralis, C. Kordulis, Appl. Catal. B: Environ. 35 (2002) 295-304.
[14] W. Yu, J. Zhu, L. Qi, C. Sun, F. Gao, L. Dong, Y. Chen, J. Colloid Interf. Sci. 364 (2011) 435-442.
[15] D. Zhou, S. Zuo, S. Xing, J. Phys. Chem. C 116 (2012) 4060-4070.
[16] W. Ding, S. Li, G.D. Meitzner, E. Iglesia, J. Phys. Chem. B 105 (2000) 506-513.
[17] R.W. Borry, Y.H. Kim, A. Huffsmith, J.A. Reimer, E. Iglesia, J. Phys. Chem. B 103 (1999) 5787-5796.
[18] W. Ding, G.D. Meitzner, E. Iglesia, J. Catal. 206 (2002) 14-22.
[19] W. Li, G.D. Meitzner, R.W. Borry lii, E. Iglesia, J. Catal. 191 (2000) 373-383.
[20] R.O. Savinelli, S.L. Scott, Phys. Chem. Chem. Phys. 12 (2010) 5660-5667.
[21] Y.-H. Kim, R.W. Borry iii, E. Iglesia, Micropor. Mesopor. Mater. 35-36 (2000) 495-509.
[22] B. Li, S. Li, N. Li, H. Chen, W. Zhang, X. Bao, B. Lin, Micropor. Mesopor. Mater. 88 (2006) 244-253.
[23] Z.R. Ismagilov, E.V. Matus, L.T. Tsikoza, Energy Environ. Sci. 1 (2008) 526-541.
[24] D. Ma, Q. Zhu, Z. Wu, D. Zhou, Y. Shu, Q. Xin, Y. Xu, X. Bao, Phys. Chem. Chem. Phys. 7 (2005) 3102-3109.
[25] D. Ma, X. Han, D. Zhou, Z. Yan, R. Fu, Y. Xu, X. Bao, H. Hu, S.C.F. Au-Yeung, Chem. Eur. J. 8 (2002) 4557-4561.
[26] H. Minming, R.F. Howe, J. Catal. 108 (1987) 283-293.
[27] D. Zhou, D. Ma, X. Liu, X. Bao, J. Chem. Phys. 114 (2001) 9125-9129.
[28] D. Ma, Y. Shu, X. Bao, Y. Xu, J. Catal. 189 (2000) 314-325.
[29] Y. Xu, S. Liu, X. Guo, L. Wang, M. Xie, Catal. Lett. 30 (1994) 135-149.
[30] L.A. Pine, P.J. Maher, W.A. Wachter, J. Catal. 85 (1984) 466-476.
[31] D. Zhou, D. Ma, Y. Wang, X. Liu, X. Bao, Chem. Phys. Lett. 373 (2003) 46-51.
[32] J.-P. Tessonnier, B. Louis, S. Walspurger, J. Sommer, M.-J. Ledoux, C. Pham-Huu, J. Phys. Chem. B 110 (2006) 10390-10395.
[33] J.-P. Tessonnier, B. Louis, S. Rigolet, M.J. Ledoux, C. Pham-Huu, Appl. Catal. A: Gen. 336 (2008) 79-88.
[34] D. Zhou, Y. Zhang, H. Zhu, D. Ma, X. Bao, J. Phys. Chem. C 111 (2007) 2081-2091.
[35] G. Busca, M.A. Larrubia, L. Arrighi, G. Ramis, Catal. Today 107-108 (2005) 139-148.
[36] H. van Koningsveld, J.C. Jansen, H. van Bekkum, Zeolites 10 (1990) 235-242.
[37] D. Nachtigallova, P. Nachtigall, M. Sierka, J. Sauer, Phys. Chem. Chem. Phys. 1 (1999) 2019-2026.
[38] M. Sierka, J. Sauer, Faraday Discuss. 106 (1997) 41-62.
[39] W. Lowenstein, Am. Mineral. 39 (1954) 92-96.
[40] B. Delley, J. Chem. Phys. 92 (1990) 508-517.
[41] B. Delley, J. Phys. Chem. 100 (1996) 6107-6110.
[42] J.P. Perdew, Y. Wang, Phys. Rev. B 45 (1992) 13244-13249.
[43] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Phys. Rev. B 46 (1992) 6671-6687.
[44] M. Dolg, U. Wedig, H. Stoll, H. Preuss, J. Chem. Phys. 86 (1987) 866-872.
[45] A. Bergner, M. Dolg, W. Küchle, H. Stoll, H. Preuß, Mol. Phys. 80 (1993) 1431-1441.
[46] R.S. Mulliken, J. Chem. Phys. 23 (1955) 1833-1840.
[47] R.S. Mulliken, J. Chem. Phys. 23 (1955) 1841-1846.
[48] R.S. Mulliken, J. Chem. Phys. 23 (1955) 2338-2342.
[49] R.S. Mulliken, J. Chem. Phys. 23 (1955) 2343-2346.
[50] I. Mayer, Chem. Phys. Lett. 97 (1983) 270-274.
[51] I. Mayer, J. Mol. Struct. Theochem. 149 (1983) 81-89.
[52] T.Tsumuraya, T.Shishidou, T.Oguchi, J.Alloy.Compd.446-447(2007)323-327.

[53] D.R. Lide, CRC Handbook of Chemistry and Physics, CRC Press, Boca Raton, 2000, pp. 9-22.

[54] P. Geerlings, F. De Proft, W. Langenaeker, Chem. Rev. 103 (2003) 1793-1874.

[55] W. Yang, W.J. Mortier, J. Am. Chem. Soc. 108 (1986) 5708-5711.

[56] E. Florez, W. Tiznado, F. Mondragón, P. Fuentealba, J. Phys. Chem. A 109 (2005) 7815-7821.

[57] A. Poater, M. Duran, P. Jaque, A. Toro-Labbé, M. Solà, J. Phys. Chem. B 110 (2006) 6526-6536.

[58] H. Sekhar De, S. Krishnamurty, S. Pal, J. Phys. Chem. C 114 (2010) 6690-6703.

[59] F. Cao, S. Su, J. Xiang, L. Sun, S. Hu, Q. Zhao, P. Wang, S. Lei, Appl. Surf. Sci. 261 (2012) 659-664.

[60] X. Yin, H. Han, I. Gunji, A. Endou, S.S. Cheettu Ammal, M. Kubo, A. Miyamoto, J. Phys. Chem. B 103 (1999) 4701-4706.

[61] S. Soyer, A. Uzun, S. Senkan, I. Onal, Catal. Today 118 (2006) 268-278.

[62] H. Yao, Y. Chen, Y. Wei, Z. Zhao, Z. Liu, C. Xu, Surf. Sci. 606 (2012) 1739-1748.

[63] C. Busco, A. Barbaglia, M. Broyer, V. Bolis, G.M. Foddanu, P. Ugliengo, Ther- mochim. Acta 418 (2004) 3-9.

[64] X. Ding, Z. Li, J. Yang, J.G. Hou, Q. Zhu, J. Chem. Phys. 121 (2004) 2558-2562.

[65] H. Yao, Y. Chen, Z. Zhao, Y. Wei, Z. Liu, D. Zhai, B. Liu, C. Xu, J. Catal. 305 (2013) 67-75.

[66] G. Busca, L. Lietti, G. Ramis, F. Berti, Appl. Catal. B: Environ. 18 (1998) 1-36.

[67] M. Calatayud, B. Mguig, C. Minot, Surf. Sci. Rep. 55 (2004) 169-236.

[68] R.Q. Long, R.T. Yang, J. Catal. 207 (2002) 224-231.

[69] D. Fang, F. He, D. Li, J. Xie, Appl. Surf. Sci. B 285 (2013) 215-219.

[70] J. Li, H. Chang, L. Ma, J. Hao, R.T. Yang, Catal. Today 175 (2011) 147-156.

[71] I. Mayer, Int. J. Quantum. Chem. 29 (1986) 477-483.