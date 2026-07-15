# Radical Chain-Reaction of Terminal-Unsaturated Organic Molecules on Water-Saturated Si(100)-(2 × 1): The Role of Surface Hydroxyl Groups

Yingzi Tan and Yong Pei*

Department of Chemistry, Key Laboratory of Environmentally Friendly Chemistry and Applications of Ministry of Education, Xiangtan University, Hunan Province, China, 411105

Supporting Information

ABSTRACT: The radical initiated hydrosilylation of terminated unsaturated organic molecules on water saturated Si(100)-(2 × 1) is systematically studied using density functional theory (DFT) calculations in the framework of periodic surface model. Two possible radical chain-reaction mechanisms including the H-abstraction from surface Si−OH or Si−H group and the direct abstraction of a −OH group are studied. It is found that the surface −OH group acts as a medium for the radical chain-reaction. The chain-reaction can proceed through abstracting a H-atom from surface −OH group, while the direct abstraction of −OH group is prevented by high energy barriers. The O-adatom caused by the H-abstraction from surface −OH group promotes the reactivity of the newly generated surface dangling bond toward sequentially attached molecules. Nonetheless, it shows double-side effects on the following H-abstraction along the dimer row direction. It can either facilitate or hinder the following H-abstraction process depending on its insertion mode into the surface Si−Si skeleton. Based on the computed reaction rates of H-abstractions in different pathways, the possible growth behaviors of organic molecules on water-saturated Si(100)-(2 × 1) are predicted. The reaction of propylene and aldehyde without a conjugate βC substituent is predicted to lead to formation of disordered monolayer structures. In contrast, the styrene and benzaldehyde tend to grow quasi-one-dimensional molecular wires within the single Si−Si dimer row.

![](./images/813218878288035841_1.jpg)

## 1. INTRODUCTION

The functionalization of semiconductor surfaces with organic molecules has attracted long-term interest because of their potential application in molecular electronics and sensor devices. $^{1-13}$ Over the past decades, intensive efforts have been exerted to fabricate self-assembled organic monolayers on silicon surfaces via mild and fast attachment methods. In particular, great attention has been focused on the direct formation of the Si−X (X = C and O) bond on silicon surfaces. The hydrosilylation of hydrogen-terminated silicon has been demonstrated to be an efficient way to fabricate organic monolayer covered silicon surfaces with the direct formation of covalent Si−C bonds. Hydrosilylation routes including both wetting chemistry and ultrahigh vacuum (UHV) approaches such as UV or visible light irradiations, $^{14-17}$ hydrosilylation catalysts, $^{18}$ Grignard and alkyl lithium reagents, $^{19}$ and electrochemical $^{20}$ methods were developed during the past two decades.

Among various developed hydrosilylation methods, the radical initiated hydrosilylation of hydrogen passivated silicon surface first introduced by Chidsey et al. is one of the most promising ways to prepare highly ordered surface nanostructures. $^{21,22}$ Utilizing the unique surface pattern of reconstructed Si(100)-(2 × 1), Lopinski et al. reported for the first time the self-directed growth of highly ordered, one-dimensional styrene molecular nanowire on H−Si(100)-(2 × 1) via a radical initiated chain-reaction. $^{23}$ This pioneered work inspired intensive studies on the preparation of ordered molecular nanostructures on H−Si(100)-(2 × 1). A variety of terminal unsaturated molecules such as vinylferrocene, long alkyl chain alkene, aldehyde, and acetone were found to be capable of growing high-quality quasi-one-dimensional molecular nanowires on H−Si(100)-(2 × 1) along the surface dimer row through the radical initiated chain reactions. $^{24-38}$ Besides the growth of molecular wires parallel to surface dimer row, recent studies also showed that allylic mercaptan (ALM) $^{25}$ and acetophenone $^{28}$ can grow molecular lines across the surface dimer row. Based on different growth behaviors of ALM and styrene on H−Si(100)-(2 × 1), an inter-connected perpendicular nanowire was prepared successfully. $^{24}$ These unique ordered molecular nanowires offer great opportunities to fabricate novel molecular devices.

Motivated by experimental discoveries, theoretical calculations have been carried out to understand not only the fundamental mechanism of surface reactions, but also the underlying factors that controlled the growth pattern of molecular nanowire on H−Si(100)-(2 × 1). Cho et al. studied the reaction mechanisms of a number of organic molecules including styrene, acetone, phenylacetylene, and allyl mercaptan etc. on the H−Si(100)-(2 × 1). $^{39-43}$ Raghavachari et al. performed theoretical studies on

Received: March 29, 2013
Revised: May 23, 2013

Scheme 1. (a) Conventional Radical Chain-Reaction Mechanism on H-Terminated Silicon Surface. (b) Water Saturated Si(100)-$(2 \times 1)$ with Linear and Zigzag Patterns of $-\text{H}$ and $-\text{OH}$ Terminal Groups and Three Possible Radical Transfer Routes during Radical Chain-Reaction. (c) Three Kinds of Radical Propagation Ways for Radical Chain Reactions

![](./images/813218878288035841_2.jpg)

(a) Conventional radical chian-reaction mechanism on H-terminated silicon surface

![](./images/813218878288035841_3.jpg)

(b) Water saturated Si(100)-(2×1) and different directions for $-\text{H}$ or $-\text{OH}$ abstractions.

![](./images/813218878288035841_4.jpg)

(c) H-abstraction or OH-abstraction mode on water saturated Si(100)-(2×1)

the reaction pathways of ALM molecules and acetone on $\text{H-Si(100)-(2} \times 1\text{)}.^{44}$ Musgrave et al., Rodriguez et al., Selloni et al., and Pei et al. studied the chain-reactions of a series of terminal unsaturated organic molecules such as 1-alkene, 1-alkyne, and aldehydes on the $\text{H-Si(100)-(2} \times 1\text{)}.^{46-55}$ The reaction mechanism was suggested to contain two main steps as shown in Scheme 1a: In the first step, the unsaturated $\pi$-bond in a terminal unsaturated organic molecule reacts with a surface silicon dangling bond that was created by STM tip or thermal cleavage of $\text{Si-H}$ bond. A $\beta\text{C}$-centered radical intermediate with a Si-X linkage ($\text{X = C}$ or $\text{O}$) is formed in this step. Next, the $\beta\text{C}$ radical center abstracts a surface hydrogen atom from a neighboring $\text{Si-H}$ group to produce a new Si dangling bond ($\text{Si}\bullet$), which acts as a new reaction site to propagate the surface chain reaction. Through these theoretical studies, several factors such as the properties of $\beta\text{C}$ substituent and terminal unsaturated group in reactant molecules were revealed to affect the reaction process significantly.

To date, most experimental and theoretical studies focused on the radical chain reactions of organic molecules on the H-terminated silicon surfaces involving solely the abstraction of surface H atom as shown in Scheme 1a. We denote this process as the conventional H-abstraction route. An interesting question is raised regarding whether the radical chain reaction can proceed through abstraction of surface functional group ($\text{Si-X}$) or H atom from the surface functional groups? Recently, Gallet et al. performed detailed studies on the surface electronic structure and morphologies of water-saturated $\text{Si(100)-(2} \times 1\text{)}$ via scanning tunneling microscopy (STM) and X-ray photoelectron spectroscopy (XPS) measurements.$^{56}$ It was found that the water saturated silicon surface is composed of not only patterned $-\text{H}$ and $-\text{OH}$ groups, but also negatively charged dangling bonds. Bournel et al. found that the radical chain reaction of styrene molecules can be trigger by the naturally present dangling bond on water-saturated silicon surface to generate a styrene covalently modified silicon surface.$^{57}$ The radical chain-reaction mechanism

was proposed to involve a conventional H-abstraction route as described in Scheme 1a. The surface $-\text{OH}$ group on water-saturated $\text{Si}(100)$-(2 $\times$ 1) was suggested to block the radical-chain reaction because no evidence of $-\text{OH}$ group cleavage is observed in experiments. $^{57}$

In this work, we have systematically investigated a possible radical chain-reaction mechanism of propylene, styrene, aldehyde, and benzaldehyde on water-saturated $\text{Si}(100)$-(2 $\times$ 1) via the density functional theory (DFT) calculations. A key issue we would like to clarify is the role of surface hydroxyl groups in the reaction of styrene and other terminated unsaturated molecules on the water saturated silicon surface. Does it block the surface chain-reaction or act as a medium for the reactions? To this end, three kinds of H-atom or OH-group abstraction pathways along different directions are studied as shown in Scheme 1b and c. Through comparing the activation energies of different reaction pathways, we find that the radical chain-reaction on water-saturated $\text{Si}(100)$-(2 $\times$ 1) can proceed by abstracting an H-atom from both surface $-\text{OH}$ and $\text{Si}-\text{H}$ groups. However, the direct abstraction of an OH-group from silicon surface is a high-energy process, which is not feasible in realistic experimental conditions. We also find that the product O-adatom caused by the H-abstraction from surface $-\text{OH}$ groups can promote the reactivity of a newly formed $\text{Si(O)}\bullet$ radical site toward sequentially attached organic molecules. Nonetheless, the O-adatom demonstrates double-side effects on the following H-abstraction reaction. It can either accelerate or hinder the following H-abstraction along the dimer row depending on its insertion mode into the surface Si-skeleto.n

## 2. COMPUTATIONAL MODEL AND DETAILS
The reconstructed water saturated $\text{Si}(100)$-(2 $\times$ 1) is modeled by a slab model containing six layers of silicon atoms and two $\text{Si}-\text{Si}$ dimer rows, as shown in Figure 1. At present, we consider two types of water-saturated $\text{Si}(100)$-(2 $\times$ 1) surface: (a) the surface dimer row passivated by $-\text{OH}$ and $-\text{H}$ groups in a zigzag pattern; (b) the surface dimer row with a linear pattern of $-\text{OH}$ and $-\text{H}$ groups. A dangling bond is introduced on the surface as the initial reaction site. Of note, the defects on the water-saturated silicon surface are not considered in the present surface models, as our major motivation is to examine the role of the surface hydroxyl groups played in the surface radical chain-reactions.

![](./images/813218878288035841_5.jpg)

Figure 1. Periodic model of zigzag (left) and linear (right) types of water-saturated $\text{Si}(100)$-2 $\times$ 1. A surface dangling bond is presented initially.

The slab model is optimized using a double numerical basis set with polarization functions (DNP) for Si, C, H, and O elements, along with the Perdew-Burke-Ernzerhof (PBE) functional. $^{58,59}$ During all structural optimizations, the bottom two layers of Si atoms and the passivated H atoms beneath are fixed. The transition state structures for the H- and OH-abstraction are explored by using the combination of LST/QST algorithm with subsequent conjugated gradient (CG) optimizations. The convergence criteria for the geometrical optimization is set as $1.0 \times 10^{-5}$ Hartree for energy change, $2.0 \times 10^{-3}$ Hartree/Å for the gradient, and $5.0 \times 10^{-3}$ Å for the displacement. A smearing parameter with the value of 0.002 hartree is used during energy evaluations. The SCF calculation has the convergence of $1.0 \times 10^{-6}$ Hartree. The spin-unrestricted method is used for all calculations. At present, the DFT with dispersion corrections, called DFT-D method, was also used to validate the order of energy barriers computed by pure GGA functional (PBE). In the scheme of DFT-D method, the van der Waals interactions are described via a simple pairwise force field. Here the pairwise van der Waals parameters such as $C_6$ and $R_0$ of C, H, O, and Si atoms were chosen according to the original literature. $^{60}$

## 3. RESULTS AND DISCUSSION
### 3.1. Two Kinds of Radical Chain Reaction Mechanisms on Water-Saturated $\text{Si(100)-2} \times$ 1.
We propose two possible propagation mechanisms for the radical chain-reaction of terminal unsaturated molecules on water saturated $\text{Si}(100)$-2 $\times$ 1: the H-abstraction and the OH-abstraction routes as shown in Scheme 1c. In the H-abstraction route, the $\beta\text{C}$ radical center on adsorbed organic molecule can abstract an H atom from either surface $\text{Si}-\text{OH}$ group (Mode 1) or $\text{Si}-\text{H}$ group (Mode 2, conventional H-abstraction route) to propagate the chain-reaction. The OH-abstraction route involves the direct abstraction of an $-\text{OH}$ group from the silicon surface (Mode 3).

Radical Chain Reaction via H-Abstraction from Surface $-\text{OH}$ Group. Bournel et al. suggested the surface $-\text{OH}$ groups blocked propagation of the radical chain-reaction as direct OH-abstraction was not observed from XPS measurements. $^{57}$ However, the H-abstraction from surface $-\text{OH}$ groups was not considered. To validate a possible H-abstraction process from surface $-\text{OH}$ groups on water-saturated $\text{Si}(100)$-2 $\times$ 1, a surface dangling bond ($\text{Si}\bullet$) is created by cleavage of a surface $\text{Si}-\text{H}$ bond shown in Scheme 1b, which is surrounded by three $-\text{OH}$ groups in $r1$, $r2$, and $r3$ directions, respectively.

As shown in Scheme 2, the H-abstraction from a surface $-\text{OH}$ group involves four major steps. In the first step, organic molecules attach to surface via attack of terminal unsaturated groups to surface dangling bond ($\text{Si}\bullet$), which is the same as the

Scheme 2. Suggested H-Abstraction Routes from Surface $\text{Si}-\text{OH}$ Group

![](./images/813218878288035841_6.jpg)

![](./images/813218878288035841_7.jpg)

Figure 2. (a) Energy profiles of H-abstractions for propylene, aldehyde, styrene, and benzaldehyde on water-saturated Si(100)-2×1 (in unit of eV). The energy values displayed in the parentheses are computed by PBE/DNP with dispersion corrections (DFT-D). (b) Snapshots of located transition states of the H-abstraction process for four molecules. The snapshots of all reactants, intermediates, and transition states are given in Supporting Information as Figure S1.

conventional H-abstraction process described in Scheme 1a. However, a dangling O-adatom is generated after H-abstraction from a surface −OH group (IM1). Because of strong interactions between O-adatom and the silicon surface, the dangling O-adatom generated can readily insert into the backbone of the silicon surface to form an Si−O−Si moiety. A new surface dangling bond with an O-adatom (Si(O)•, Im1→ Pr)) is produced on the surface, which acts as a new reaction site to propagate the radical chain-reactions.

The computed energy profiles and snapshots of reaction intermediates and transition states of the proposed H-abstraction process for propylene, styrene, aldehyde, and benzaldehyde are displayed in Figure 2. In the first reaction step, attacks of propylene, styrene, aldehyde, and benzaldehyde to Si• is a barrierless process with energy release of 0.57, 1.00, 0.88, and 1.18 eV, respectively, in agreement with previous theoretical results.⁵¹ After the formation of a radical intermediate (Im), there are three branching H-abstraction pathways as shown in Scheme 1b: the interdimer H-abstraction along the surface dimer row direction (r2); the intradimer row H-abstraction (r1); and the cross-dimer-row H-abstraction (r3).

From the energy profiles displayed in Figure 2a, it can be found that the interdimer H-abstraction possesses the lowest energy barrier for the four molecules. However, the energy difference

Scheme 3. Direct OH-Abstraction Route from the Surface Si−OH Group

![](./images/813218878288035841_8.jpg)

among three H-abstraction pathways is fairly small. In particular, the energy barrier of interdimer H-abstraction is only slightly lower than those of intradimer and cross-dimer-row H-abstractions for propylene and aldehyde as shown in Figure 2a. As for the styrene and benzaldehyde, the interdimer H-abstraction is more favorable in energy than the other two pathways; the largest energy gap among three kinds of H-abstraction pathways increases to 0.20 and 0.31 eV, respectively. Herein, we emphasize that the DFT-D method predicts similar barrier heights and the same order of H-abstraction barriers along different reaction pathways to the pure GGA results.

It is interesting to compare energy profiles of H-abstraction from surface −OH groups with previously reported conventional H-abstraction routes on H-terminated Si(100)-2 × 1.³⁹⁻⁴⁴,⁴⁶⁻⁵⁵ In the case of the conventional H-abstraction reaction, the cross- dimer-row H-abstraction generally has much higher energy barriers (~0.5 eV) than the other two H-abstraction pathways. However, a significant drop of energy barrier is found for the cross-dimer-row H-abstraction on water-saturated Si(100)-2 × 1. This energy difference can be attributed to the notably decreased distance between H-atom (in −OH group) and βC radical site on water-saturated Si(100)-2 × 1, which facilitates the cross- dimer-row H-abstractions.

Radical Chain Reaction via Direct −OH Abstraction. After investigating the H-abstraction process from surface −OH groups, we consider an alternative reaction pathway that involves direct abstraction of an −OH group by the βC radical center, as shown in Scheme 3. In this kind of reaction route, the direct abstraction of −OH group by βC radical center happens instead of abstracting an H-atom.

The energy barriers of different OH-abstraction pathways by propylene, styrene, aldehyde, and benzaldehyde on zigzag patterned water-saturated Si(100)-(2 × 1) are evaluated in Figure 3 at PBE/DNP level calculations. It is found that the interdimer OH-abstraction is the most favorable pathway for the four molecules, consistent with the H-atom abstraction processes discussed above. Nonetheless, the energy barriers of direct OH-abstraction (in the range of 1.17 to 2.06 eV) are much higher than that of H-abstraction from −OH groups (in the range of 0.51 to 1.18 eV), as shown in Figures 2 and 3. Obviously, the radical-chain reaction will proceed more likely through H-abstraction rather than direct abstraction of an −OH group. A qualitative calculation based on the trimethylsilanol (Si(CCH₃)− OH) molecule indicates that the bond dissociation energy (BDE) of the (SiH₃)₃SiO−H bond is about 0.10 eV smaller than that of the (SiH₃)₃Si−OH bond, suggesting favorable scission of the SiO−H bond upon radical attack. Moreover, the shorter distance between the βC radical site and H-atom in the surface −OH group also favors the H-transfer process.

Feasibility of Chain-Reaction on Water-Saturated Si(100)-2 × 1. On basis of the calculated energy profiles of H-abstraction and OH-abstraction processes shown in Figures 2 and 3, we can qualitatively predict the feasibility of radical chain-reactions of four studied molecules on water saturated Si(100)-2 × 1. In earlier experimental studies, Wolkow et al. found that the relative stabilities of radical intermediate significantly affect the propagation of surface chain-reactions. For example, the propylene cannot grow molecular nanostructure on the H−Si(100)-2 × 1, while styrene molecules do show much better reactivity.²³ The underlying reason for such a difference was attributed to the formation of a more stable radical intermediate by styrene. A similar situation was also found for 1-alkene.³¹ The 1-alkene with longer alkyl tail shows strong dispersion interactions to the radical intermediate, which facilitates growth of molecular nanowires on H−Si(100)-2 × 1. In contrast, the shorter-tail 1-alkene shows poor reactivity. The relative stability of the radical intermediate was thus considered a key, important factor that dominates the feasibility of propagation of the surface chain reaction. If the adsorption energy of the organic molecule is smaller than the following H-abstraction barrier, the chain-reaction is most likely prohibited.³¹

At present, the terminal unsaturated groups (C═C or C═O) and βC substituents in four types of molecules strongly influence the relative stability of metastable radical intermediates (Im). The benzaldyhyde and aldehyde display much larger adsorption energies than those of styrene and propylene, respectively, due to the formation of stronger Si−O bonds. On the other hand, the conjugate substituent on βC also enhances the stability of radical intermediates via the electron delocalization effects. From Figure 2, we found that the adsorption energies of four molecules are generally larger than the following H-abstraction barriers, suggesting the reaction will go forward. Moreover, the calculated reaction rate ratio between forward and reverse reactions of the H-abstraction step (c.f. Table 1) also indicates the forward H-abstraction step is more favorable than the reverse desorption of molecules from the surface, suggesting the adsorbed molecules can proceed to the H-abstraction reactions.

### 3.2. Effects of O-Adatom on the Reactivity of Dangling Bond and Possible Growth Modes of Organic Molecules on Water-Saturated Si(100)-2 × 1.
In the above discussions, we show that the radical chain-reaction of four terminal unsaturated molecules on water-saturated Si(100)-2 × 1 can proceed through abstracting an H-atom from a surface −OH group. Nonetheless, the direct abstraction of an −OH group is prevented by high energy barriers. In the following, we will address two topics: (1) the effect of O-adatom on the reactivity of the surface dangling bond; and (2) the possible propagation routes of radical chain reactions of four molecules on water- saturated Si(100)-2 × 1.

Reactivity of Surface Dangling Bond in the Presence of O-Adatom. Recent experimental and theoretical studies based on H-terminated silicon surfaces showed that reactivity of a newly generated surface dangling bond (Si•) after H-abstraction is quite sensitive to the properties of preadsorbed molecules, which was either ‘active’ toward the additional organic molecules to propagate the chain-reaction or ‘inert’ to the adsorption of an

![](./images/813218878288035841_9.jpg)

Figure 3. (a) Energy profiles of direct OH-abstraction reactions for propylene, aldehyde, styrene, and benzaldehyde on water-saturated Si(100)-2 × 1 (in unit of eV). The energy values displayed in the parentheses are computed by PBE/DNP with dispersion corrections (DFT-D). (b) Snapshots of located transition state of direct OH-abstraction process for four molecules. The snapshots of all reactants, intermediates, and transition states are given in Supporting Information as Figure S1.

extra molecule so as to terminate the chain-reaction. $^{26,27}$
Raghavachari et al. computationally investigated the adsorption energy and H-abstraction barrier of styrene and aldehyde at the end of the ALM molecular wire and found that styrene has much smaller adsorption energy than aldehyde on the newly generated surface dangling bond, explaining why continuing growth of the styrene molecular line is not observed in experiments. $^{44}$

At present, a dangling O-adatom is produced after H-abstraction from an $-$OH group, which can insert into a neighboring Si$-$Si bond to form a new Si(O)• radical site, as shown in Scheme 2 and Figure S1 (Supporting Information). The presence of O-adatom on the radical site is expected to affect the reactivity of the radical site. In order to examine the O-adatom effect, the sequential adsorption of a second propylene and styrene on Si(O)• is investigated. From Figure 4a, the adsorption energy of a second propylene and styrene on Si(O)• is 0.602 and 1.121 eV, respectively, both slightly larger than those on the Si• site (0.567 and 1.002 eV as shown in Figures 2 and 3). After formation of a radical intermediate on the Si(O)• site, there are again three possible H-abstraction pathways. At present, the interdimer and intradimer H-abstractions have been examined as shown in Figure 4a. For propylene, the energy barriers of the following

**Table 1. Ratio of Reaction Rate between Forward H-Abstraction and Reverse Deadsorption of Molecule from Surface**⁰

<table>
  <thead>
    <tr>
      <th rowspan="2">rate ratio (forward/reverse)</th>
      <th colspan="4">grafting molecules</th>
    </tr>
    <tr>
      <th>propylene</th>
      <th>aldehyde</th>
      <th>styrene</th>
      <th>benzaldehyde</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>r1 direction</td>
      <td>7.58</td>
      <td>$3.24×10^{6}$</td>
      <td>$9.39×10^{-4}$</td>
      <td>4.94</td>
    </tr>
    <tr>
      <td>r2 direction</td>
      <td>9.20</td>
      <td>$3.79×10^{6}$</td>
      <td>2.27</td>
      <td>$4.14×10^{6}$</td>
    </tr>
    <tr>
      <td>r3 direction</td>
      <td>1.12</td>
      <td>$1.55×10^{6}$</td>
      <td>0.11</td>
      <td>22.54</td>
    </tr>
  </tbody>
</table>

⁰The reaction rate is calculated using Arrhenius formula based on the activation energies and adsorption energies displayed in Figure 2a computed at DFT/PBE level. The temperature used to evaluate the reaction rate is 298 K.

intradimer and interdimer H-abstractions are 0.49 and 0.33 eV, respectively, suggesting that H-abstraction proceeds more favorably along the dimer row direction. A similar tendency is found for styrene as well. Meanwhile, the difference in energy barriers between interdimer and intradimer H-abstractions increased to 0.59 eV, showing much stronger directional selectivity of the H-abstraction reaction. The greatly lowered energy barrier of H-abstraction along the surface dimer row direction at the Si(O)• site is also found on linearly patterned water-saturated Si(100)-2×1. As shown in Figure 4a and b, we assume one styrene or propylene molecule is preattached to the linear H/OH-Si(100)-2 × 1. After attaching to the Si(O)•, the following interdimer H-abstractions have energy barriers of 0.331 and 0.624 eV for propylene and styrene, respectively, both much lower than intradimer H-abstractions (0.597 and 0.807 eV, respectively).

To understand the effects of O-adatom on the reactivity of surface dangling bonds and height of H-abstraction barriers, we performed electronic structure and geometrical analysis. The spin and charge density of the surface radical site with or without the O-adatom are compared using the Hirshfeld charge and spin analysis. It is found that the presence of the O-adatom affects both spin density and charge state of the surface dangling bond. The charge state of the surface dangling bond changes from negative (Si•, −0.01|e|) to positive (Si(O)•, +0.17|e|) and the spin density of Si atom increases from 0.58 μB (on Si•) to 0.79 μB (on Si(O)•). The switch of charge state of the surface dangling bond is attributed to stronger electronegativity of the O-adatom, which withdraws some electrons from the Si atom. The positively charged dangling bond and increased local spin

![](./images/813218878288035841_10.jpg)

Figure 4. (a) Energy profiles of H-abstraction by the second attached propylene and styrene molecules on zigzag and linear patterned water-saturated Si(100)-2×1 (in unit of eV). (b) Snapshots of transition state structures of the H-abstraction process. The snapshots of all reactants, intermediates, and transition states are given in Supporting Information as Figure S1.

![](./images/813218878288035841_11.jpg)

Figure 5. (a) Effect of O-adatom insertion on the distance between two neighboring Si−Si dimers. (b) Effect of O-adatom insertion (away from the preadsorbed molecule) on the distance between two Si−Si dimers and the computed energy curve of H-abstraction by a second attached propylene molecule (in unit of eV). The snapshots of all reactants, intermediates, and transition state are given in Supporting Information as Figure S1.

density at the surface dangling bond facilitate the attack of electron-rich $\pi$-bonds such as $\mathrm{C=C}$ or $\mathrm{C=O}$ from reactant molecules, hence leading to increased adsorption energies of following attached molecules. Besides the electronic effects, the insertion of O-adatom into the silicon skeleton also induces strong perturbation on the configuration of the Si−Si dimer row. As shown in Figure 5a, the distance between two neighboring Si−Si dimers along the r2 direction decreases notably on both linear and zigzag surfaces. The decreased distance between two neighboring Si−Si dimer shortens the H-transfer pathway between the $\beta$C radical center and surface −OH group, which further reduces H-abstraction barriers. For comparison, the O-adatom slightly affects the geometry of the single Si−Si dimer. As a result, the intradimer H-abstraction barrier obtained in Figure 4 is nearly unchanged in comparison to the first step (displayed in Figure 2).

In the above discussions, we assume that O-adatom inserts into a Si−Si bond close to the preadsorbed molecule as shown in Figure 5a. However, the possibility that the insertion of a dangling O-adatom into a Si−Si bond away from the preadsorbed molecule cannot be ruled out. As shown in Figure 5b, the distance between two neighboring Si−Si dimers increases to 4.43 Å if the dangling O-adatom inserts into a Si−Si bond away from the preadsorbed molecule. The increased distance between two dimers eventually leads to a dramatically increased H-abstraction barrier, taking propylene as an example. The further energy calculations indicate two kinds of O-adatom insertion modes have very close energies, suggesting both of them can exist during the radical chain-reactions. As a result, we think the O-adatom generated by H-abstraction from a surface −OH group will exhibit two-sided effects on the following H-abstraction step: it can either promote or hinder the inter-dimer H-abstraction depending on its insertion mode into the Si skeleton. Despite this, we will show in the follow discussions that both kinds of O-adatom insertion modes do not affect the final surface nanostructure resulting from the chain-reaction.

Possible Growth Routes of Organic Molecules on Water- Saturated Si(100)-2 × 1. Utilizing the intrinsic anisotropy of H−Si(100)-2 × 1, several ordered low-dimensional molecular wires have been successfully prepared on the basis of the radical chain-reactions. $^{23-38}$ The reason for the self-directed growth of an ordered organic molecular wire on H−Si(100)-2 × 1 has been ascribed to the difference of energy barriers among various H-abstraction pathways, e.g., along r1, r2, and r3 directions shown in Scheme 1. In particular, because of the high energy barrier in across-dimer-row H-abstraction, the growth of a molecular wire

on H-terminated Si(100)-2 × 1 was generally restricted within a single surface dimer row for 1-alkenes and aldehydes.

The possible growth behaviors of propylene, styrene, aldehyde, and benzaldehyde on water-saturated Si(100)-2 × 1 are discussed on the basis of the relative reaction rates of different H-abstraction pathways. From Table 2, the propylene and aldehyde without a conjugate $\beta$C substituent exhibit a small difference in reaction rates (no more than 10-fold) among three H-abstraction pathways. However, the styrene and benzaldehyde exhibit much higher intradimer-row H-abstraction reaction rates than cross-dimer-row H-abstractions. In particular, the cross-dimer-row H-abstraction reaction rate of benzaldehyde is thousands of times lower than the other two pathways. The reaction rate difference suggests propylene and aldehyde without a $\beta$C conjugated substituent will take random growth on the surface, leading to disordered packing structures. As for styrene and benzaldehyde, they tend to grow molecular nanostructure restricted within a single dimer row similar to that on H-terminated Si(100)-2 × 1 because of the large difference of reaction rate between intradimer-row and across-dimer-row H-abstractions.

Finally, we would like to correlate our theoretical results with recent experimental observations. Bournel et al. found that styrene can react and grow nanostructures readily on water-saturated Si(100)-2 × 1.⁵⁷ The C(1s) XPS measurement excluded the possibility of direct abstraction of $-$OH groups, consistent with our theoretical results. However, there are no micropictures such as STM studies on the surface nanostructure. In particular, the surface $-$OH group was suggested to hinder radical chain-reaction. A diffusion of surface dangling bonds at the Si$-$OH site was proposed to renew the chain reaction.⁵⁷ At present, our theoretical results indicate the surface $-$OH group indeed plays a 'positive' role in the radical chain-reaction on water-saturated Si(100)-2 × 1. The energy barrier of H-abstraction from an $-$OH group is comparable to or even lower than that from surface Si$-$H groups as shown in Figures 2 and 4. Moreover, we also qualitatively predict that radical chain-reactions of propylene and aldehyde will propagate randomly on the surface. As for styrene and benzaldehyde, they tend to grow quasi-1D molecular wires restricted within the surface dimer row.

### 4. CONCLUSION
Radical chain-reactions of four terminal unsaturated molecules with or without $\beta$C conjugate substituent on the water-saturated Si(100)-2 × 1 are studied on the basis of DFT calculations. The results indicate that hydroxyl groups on water-saturated Si(100)-2 × 1 can act as a medium for the propagation of surface radical chain-reaction. H-abstraction from surface $-$OH groups has comparable or even lower energy barriers than the conventional H-abstraction from surface Si$-$H groups. Nonetheless, the direct abstraction of a surface $-$OH group is prevented by high energy barriers. Our calculations also indicate the O-adatom caused by H-abstraction from a surface Si$-$OH group affects both the charge state of the surface dangling bond and the configuration of surface dimers. It can change the charge state of surface dangling bond from negative to positive and increase its local spin density, hence promoting the reactivity toward sequentially attached molecules. The presence of an O-adatom can also shorten or increase the distance between two neighboring Si$-$Si dimers, which leads to decreased or increased H-abstraction energy barriers along the surface dimer row direction. Based on the computed reaction rate ratio of various H-abstraction pathways, we qualitatively predict that the reactions of propylene and aldehyde on water-saturated Si(100)-2 × 1 will lead to an irregular surface nanostructure. However, styrene and benzaldehyde can grow quasi-1D nanowires restricted within a single dimer row on water-saturated Si(100)-2 × 1.

### ASSOCIATED CONTENT
#### Supporting Information
Snapshots of intermediates, transition states, and products of different H-abstraction and OH-abstraction pathways. This material is available free of charge via the Internet at http://pubs.acs.org.

### AUTHOR INFORMATION
#### Corresponding Author
*E-mail: ypnku78@gmail.com.

#### Notes
The authors declare no competing financial interest.

### ACKNOWLEDGMENTS
Y.P. is supported by Natural Science Foundation of China (Grant No. 21103144) and Hunan Provincial Natural Science Foundation of China (12JJ7002, 12JJ1003).

### REFERENCES
(1) Xia, Y.; Whitesides, G. M. Soft Lithography. *Angew. Chem., Int. Ed.* 1998, 37, 550−575.
(2) Manoudian, R. Surface Processes in MEMS Technology. *Surf. Sci. Rep.* 1998, 30, 207−269.
(3) Buriak, J. M. Organometallic Chemistry on Silicon and Germanium Surfaces. *Chem. Rev.* 2002, 102, 1272−1308.
(4) Sieval, A. B.; Linke, R.; Zuilhof, H.; Sudhölter, E. J. R. High-Quality Alkyl Monolayers on Silicon Surfaces. *Adv. Mater.* 2000, 12, 1457−1460.
(5) Leftwich, T. R.; Teplyakov, A. V. Chemical Manipulation of Multifunctional Hydrocarbons on Silicon Surfaces. *Surf. Sci. Rep.* 2008, 63, 1−71.
(6) Ulman, A. Formation and Structure of Self-Assembled Monolayers. *Chem. Rev.* 1996, 96, 1533−1554.
(7) Wolkow, R. A. Controlled Molecular Ad Sorption on Silicon: Laying a Foundation for Molecular Devices. *Annu. Rev. Phys. Chem.* 1999, 50, 413−441.
(8) Shirahata, N.; Hozumi, A.; Yonezawa, T. Monolayer-Derivative Functionalization of Non-Oxidized Silicon Surfaces. *Chem. Rec.* 2005, 5, 145−159.
(9) Stingelin-Stutzmann, N. Organic Electronics: Complexity Made Simple. *Nat. Mater.* 2008, 7, 171−172.
(10) Yates, J. T. A New Opportunity in Silicon-Based Microelectronics. *Science* 1998, 279, 335−336.
(11) McNab, I. R.; Polanyi, J. C. Patterned Atomic Reaction at Surfaces. *Chem. Rev.* 2006, 106, 4321−4354.
(12) Bent, S. F. Attaching Organic Layers to Semiconductor Surfaces. *J. Phys. Chem. B* 2002, 106, 2830−2842.

<table>
 <caption>Table 2. Ratio of Reaction Rate between Different H-Abstraction Pathways at 298 K<sup>a</sup></caption>
 <thead>
  <tr>
   <th rowspan="2">rate ratio</th>
   <th colspan="4">grafting molecules</th>
  </tr>
  <tr>
   <th>propylene</th>
   <th>aldehyde</th>
   <th>styrene</th>
   <th>benzaldehyde</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>r2/r1</td>
   <td>1.21</td>
   <td>1.17</td>
   <td>20.06</td>
   <td>1837.15</td>
  </tr>
  <tr>
   <td>r2/r3</td>
   <td>8.19</td>
   <td>2.45</td>
   <td>2412.86</td>
   <td>8389.53</td>
  </tr>
 </tbody>
 <tfoot>
  <tr>
   <td colspan="5"><sup>a</sup>Reaction rate is calculated by Arrhenius formula based on the activation energies and adsorption energies (DFT/PBE) displayed in Figure 2a.</td>
  </tr>
 </tfoot>
</table>

(13) Hamers, R. J. Formation and Characterization of Organic Monolayers on Semiconductor Surfaces. Annu. Rev. Anal. Chem. 2008, 1, 707−736.

(14) Shestopalov, A. A.; Clark, R. L.; Toone, E. J. Catalytic Microcontact Printing on Chemically Functionalized H-Terminated Silicon. Langmuir 2010, 26, 1449−1451.

(15) Wang, X. Y.; Ruther, R. E.; Streifer, J. A.; Hamers, R. J. UV-Induced Grafting of Alkenes to Silicon Surfaces: Photoemission versus Excitons. J. Am. Chem. Soc. 2010, 132, 4048−4049.

(16) Cicero, R. L.; Linford, M. R.; Chidsey, C. E. D. Photoreactivity of Unsaturated Compounds with Hydrogen-Terminated Silicon(111). Langmuir 2000, 16, 5688−5695.

(17) Huck, L. A.; Buriak, J. M. Toward a Mechanistic Understanding of Exciton-Mediated Hydrosilylation on Nanocrystalline Silicon. J. Am. Chem. Soc. 2012, 134, 489−497.

(18) Scheres, L.; Arafat, A.; Zuilhof, H. Self-Assembly of High-Quality Covalently Bound Organic Monolayers onto Silicon. Langmuir 2007, 23, 8343−8346.

(19) Holland, J. M.; Stewart, M. P.; Allen, M. J.; Buriak, J. M. J. Metal Mediated Reactions on Porous Silicon Surfaces. Solid State Chem. 1999, 147, 251−258.

(20) Robins, E. G.; Stewart, M. P.; Buriak, J. M. Anodic And Cathodic Electrografting of Alkynes on Porous Silicon. Chem. Commun. 1999, 2479−2480.

(21) Linford, M. R.; Chidsey, C. E. D. Alkyl Monolayers Covalently Bonded to Silicon Surfaces. J. Am. Chem. Soc. 1993, 115, 12631−12632.

(22) Linford, M. R.; Fenter, P.; Eisenberger, P. M.; Chidsey, C. E. D. Alkyl Monolayers on Silicon Prepared from 1-Alkenes and Hydrogen-Terminated Silicon. J. Am. Chem. Soc. 1995, 117, 3145−3155.

(23) Lopinski, G. P.; Wayner, D. D. M.; Wolkow, R. A. Self-Directed Growth of Molecular Nanostructures on Silicon. Nature 2000, 406, 48−51.

(24) Hossain, M. Z.; Kato, H. S.; Kawai, M. Fabrication of Interconnected 1D Molecular Lines along and across the Dimer Rows on the Si(100)−(2 × 1)−H Surface through the Radical Chain Reaction. J. Phys. Chem. B 2005, 109, 23129−23133.

(25) Hossain, M. Z.; Kato, H. S.; Kawai, M. Controlled Fabrication of 1D Molecular Lines Across the Dimer Rows on the Si(100)−(2 × 1)−H Surface through the Radical Chain Reaction. J. Am. Chem. Soc. 2005, 127, 15030−15031.

(26) Hossain, M. Z.; Kato, H. S.; Kawai, M. Selective Chain Reaction of Acetone Leading to the Successive Growth of Mutually Perpendicular Molecular Lines on the Si(100)-(2 × 1)-H Surface. J. Am. Chem. Soc. 2007, 129, 12304−12309.

(27) Hossain, M. Z.; Kato, H. S.; Kawai, M. Competing Forward and Reversed Chain Reactions in One-Dimensional Molecular Line Growth on the Si(100)−(2 × 1)−H Surface. J. Am. Chem. Soc. 2007, 129, 3328−3332.

(28) Hossain, M. Z.; Kato, H. S.; Kawai, M. Self-Directed Chain Reaction by Small Ketones with the Dangling Bond Site on the Si(100)-(2 × 1)-H Surface: Acetophenone, A Unique Example. J. Am. Chem. Soc. 2008, 130, 11518−11523.

(29) Hossain, M. Z.; Kato, H. S.; Kawai, M. Valence States of One-Dimensional Molecular Assembly Formed by Ketone Molecules on the Si(100)-(2 × 1)-H Surface. J. Phys. Chem. C 2009, 113, 10751−10754.

(30) Pitters, J. L.; Wolkow, R. A. Protection−Deprotection Chemistry to Control Styrene Self-Directed Line Growth on Hydrogen-Terminated Si(100). J. Am. Chem. Soc. 2005, 127, 48−49.

(31) DiLabio, G. A.; Piva, P. G.; Kruse, P.; Wolkow, R. A. Dispersion Interactions Enable the Self-Directed Growth of Linear Alkane Nanostructures Covalently Bound to Silicon. J. Am. Chem. Soc. 2004, 126, 16048−16050.

(32) Tong, X.; DiLabio, G. A.; Clarkin, O. W.; Wolkow, R. A. Ring-Opening Radical Clock Reactions for Hybrid Organic−Silicon Surface Nanostructures: A New Self-Directed Growth Mechanism and Kinetic Insights. Nano Lett. 2004, 4, 357−360.

(33) Kruse, P.; Johnson, E. R.; DiLabio, G. A.; Wolkow, R. A. Patterning of Vinylferrocene on H−Si(100) via Self-Directed Growth of Molecular Lines and STM-Induced Decomposition. Nano Lett. 2002, 2, 807−810.

(34) Tong, X.; DiLabio, G. A.; Wolkow, R. A. A Self-Directed Growth Process for Creating Covalently Bonded Molecular Assemblies on the H−Si(100)-3 × 1 Surface. Nano Lett. 2004, 4, 979−983.

(35) Pitters, J. L.; Dogel, I; DiLabio, G. A.; Wolkow, R. A. Linear Nanostructure Formation of Aldehydes by Self-Directed Growth on Hydrogen-Terminated Silicon(100). J. Phys. Chem. B 2006, 110, 2159−2163.

(36) DiLabio, G. A.; Dogel, S. A.; Anagaw, A.; Pitters, J. L.; Wolkow, R. A. Theoretical and Spectroscopic Study of the Reaction of Diethylhydroxylamine on Silicon(100)-2 × 1. Phys. Chem. Chem. Phys. 2007, 9, 1629−1634.

(37) Dogel, I. A.; Dogel, S. A.; Pitters, J. L.; DiLabio, G. A.; Wolkow, R. A. Chemical Methods for the Hydrogen Termination of Silicon Dangling Bonds. Chem. Phys. Lett. 2007, 448, 237−242.

(38) Dogel, S. A.; DiLabio, G. A.; Zikovsky, J.; Pitters, J. L.; Wolkow, R. A. Experimental and Theoretical Studies of Trimethylene Sulfide-Derived Nanostructures on p- and n-Type H-Silicon(100)-2 × 1. J. Phys. Chem. C 2007, 111, 11965−11969.

(39) Lee, J. H.; Choi, J. H.; Cho, J. H. Enhanced Stability and Electronic Structure of Phenylacetylene Lines on the Si(100)-(2 × 1):H Surface. J. Phys. Chem C 2011, 115, 14942−14946.

(40) Choi, J. H.; Cho, J. H. Self-Directed Growth Approach for Acetylacetone Lines on an H-Terminated Si(001)-(2 × 1) Surface. Phys. Rev. B 2011, 84, 035326−035330.

(41) Choi, J. H.; Cho, J. H. First-Principles Calculations of the Structure and Growth Mechanism of Allyl Mercaptan Lines on the H/Si(100)-2 × 1 Surface. Phys. Rev. B 2011, 83, 033406−03309.

(42) Choi, J. H.; Cho, J. H. Growth Mechanism of a 1D Molecular Line across the Dimer Rows on H-Terminated Si(001). Phys. Rev. Lett. 2009, 102, 166102−166105.

(43) Lee, J. Y.; Cho, J. H. Self-directed Growth of Benzonitrile Line on H-Terminated Si(001) surface. J. Chem. Phys. 2004, 121, 8010−8013.

(44) Ferguson, G. A.; Than, C. T. L.; Raghavachari, K. Extending Molecular Lines on the Si(100)-2 × 1 Surface: A Theoretical Study of the Effect of Allylic Mercaptan Adsorbates on Radical Chain Reactions. J. Phys. Chem. Lett. 2010, 1, 679−685.

(45) Ferguson, G. A.; Than, C. T. L.; Raghavachari, K. Line Growth on the H/Si(100)-2 × 1 Surface: Density Functional Study of Allylic Mercaptan Reaction Mechanisms. J. Phys. Chem. C 2009, 113, 18817−18822.

(46) Gallo, M.; Martinez-Guerra, E.; Rodriguez, J. A. Growth of Acetone Molecular Lines on the Si(001)(2 × 1)−H Surface: First-Principle Calculations. J. Phys. Chem. C 2012, 116, 20292−20299.

(47) Kanai, Y.; Selloni, A. Competing Mechanisms in the Optically Activated Functionalization of the Hydrogen-Terminated Si(111) Surface. J. Am. Chem. Soc. 2006, 128, 3892−3893.

(48) Kanai, Y.; Takeuchi, N.; Car, R.; Selloni, A. Role of Molecular Conjugation in the Surface Radical Reaction of Aldehydes with H−Si(111): First Principles Study. J. Phys. Chem. C 2005, 109, 18889−18894.

(49) Takeuchi, N.; Selloni, A. Density Functional Theory Study of One-Dimensional Growth of Styrene on the Hydrogen-Terminated Si(001)−(3 × 1) Surface. J. Phys. Chem. B 2005, 109, 11967−11972.

(50) Takeuchi, N.; Kanai, Y.; Selloni, A. Surface Reaction of Alkynes and Alkenes with H-Si(111): A Density Functional Theory Study. J. Am. Chem. Soc. 2004, 126, 15890−15896.

(51) Pei, Y.; Ma, J.; Zeng, X. C. Effects of Radical Site Location and Surface Doping on the Radical Chain-reaction on H−Si(100)-(2 × 1): A Density Functional Theory Study. J. Phys. Chem. C 2008, 112, 16078−16086.

(52) Pei, Y.; Ma, J. Effects of $\beta$C Substituents and Terminal Unsaturated Groups on H-Abstraction Reactions of Unsaturated Molecules on the H-Terminated Si(100)−(2 × 1): Density Functional Theory Investigations. J. Phys. Chem. C 2007, 111, 5486−5492.

(53) Pei, Y.; Ma, J. Comparative Study on Reactions and Self-Directed Growth Mechanisms of Styrene Molecules on H−Terminated Si(111)

J

dx.doi.org/10.1021/jp403101v | J. Phys. Chem. C XXXX, XXX, XXX−XXX

and Si(100): Combining Quantum Chemistry and Molecular Mechanics Simulations. *Langmuir* **2006**, *22*, 3040−3048.

(54) Pei, Y.; Ma, J. Electric Field Induced Switching Behaviors of Monolayer-Modified Silicon Surfaces: Surface Designs and Molecular Dynamics Simulations. *J. Am. Chem. Soc.* **2003**, *127*, 6802−6813.

(55) Pei, Y.; Ma, J.; Jiang, Y. S. Formation Mechanisms and Packing Structures of Alkoxyl and Alkyl Monolayers on Si(111): Theoretical Studies with Quantum Chemistry and Molecular Simulation Models. *Langmuir* **2003**, *19*, 7652−7661.

(56) Gallet, J.-J.; Bournel, F.; Rochet, F.; Köhler, U.; Kubsky, S.; Silly, M. G.; Sirotti, F.; Pierucci, D. Isolated Silicon Dangling Bonds on a Water-Saturated n+-Doped Si(001)-2 × 1 Surface: An XPS and STM Study. *J. Phys. Chem. C* **2011**, *115*, 7686−7693.

(57) Bournel, F.; Gallet, J.-J.; Pierucci, D.; Khaliq, A.; Rochet, F.; Pietzsch, A. Hydrosilylation of Styrene on Water-Saturated Si(001)-2 × 1 at Room Temperature. *J. Phys. Chem. C* **2011**, *115*, 14827−14833.

(58) Delley, B. An All Electron Numerical Method for Solving the Local Density Functional for Polyatomic Molecules. *J. Chem. Phys.* **1990**, *92*, 508−517.

(59) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 386−389.

(60) Grimme, S. Semiempirical GGA-type density functional constructed with a long-range dispersion correction. *J. Comput. Chem.* **2006**, *27*, 1787−1799.