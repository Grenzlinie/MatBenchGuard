# Stability of Calcium Ion Battery Electrolytes: Predictions from Ab Initio Molecular Dynamics Simulations

Sharma S. R. K. C. Yamijala, Hyuna Kwon, Juchen Guo,* and Bryan M. Wong*

Cite This: ACS Appl. Mater. Interfaces 2021, 13, 13114−13122

Read Online

ABSTRACT: Multivalent batteries, such as magnesium-ion, calcium-ion, and zinc-ion batteries, have attracted significant attention as next-generation electrochemical energy storage devices to complement conventional lithium-ion batteries (LIBs). Among them, calcium-ion batteries (CIBs) are the least explored due to difficult reversible Ca deposition−dissolution. In this work, we examined the stability of four different Ca salts with weakly coordinating anions and three different solvents commonly employed in existing battery technologies to identify suitable candidates for CIBs. By employing Born−Oppenheimer molecular dynamics (BOMD) simulations on salt-Ca and solvent-Ca interfaces, we find that the tetraglyme solvent and carborane salt are promising candidates for CIBs. Due to the strong reducing nature of the calcium surface, the other salts and solvents readily decompose. We explain the microscopic mechanisms of salt/solvent decomposition on the Ca surface using time-dependent projected density of states, time-dependent charge-transfer plots, and climbing-image nudged elastic band calculations. Collectively, this work presents the first mechanistic assessment of the dynamical stability of candidate salts and solvents on a Ca surface using BOMD simulations, and provides a predictive path toward designing stable electrolytes for CIBs.

![](./images/812487599032631296_1.jpg)

KEYWORDS: ab initio molecular dynamics, calcium ion batteries, Born−Oppenheimer molecular dynamics, electrolyte stability, time-dependent PDOS

## INTRODUCTION

Modern technological advancements critically depend on efficient energy storage devices (batteries). Among the various candidate battery technologies, lithium-ion batteries (LIBs) are at the forefront of research and consumer use;¹⁻⁴ however, the raw materials used in LIBs (namely, lithium and cobalt) are neither earth-abundant nor evenly distributed globally (creating geopolitical tensions, particularly in the case of Co).⁵⁻⁸ The anticipated depletion in raw materials, along with the rising demand for energy storage devices, has prompted significant interest in beyond-lithium ion batteries.⁹ Among the viable alternatives to LIBs, calcium ion batteries (CIBs) have garnered significant attention due to their high gravimetric and volumetric energy densities, nontoxicity, and earth abundance.²,³,⁶,¹⁰⁻¹⁴

Calcium is the fifth most abundant element in the earth’s crust with a standard reduction potential of just 0.17 V above lithium. Accordingly, it can generate a large cell potential compared to other multivalent cation elements such as Mg or Al. Similarly, due to its lower polarization, a $Ca^{2+}$ ion should be more mobile in cathode materials compared to $Mg^{2+}$ and $Al^{3+}$ ions.²,³,¹⁰⁻¹⁴ Despite these advantages, most research on multivalent cation batteries has focused on magnesium. This shift in interest toward magnesium ion batteries (MIBs) is primarily due to the lack of stable and efficient electrolytes for CIBs that can show reversible plating and stripping of calcium.¹²,¹³ It is also important to note that while the decomposition of electrolytes at the anode, which leads to the formation of the so-called solid-electrolyte interphase (SEI), is an advantage for LIB technology, it is detrimental for CIBs.²,¹⁰,¹¹,¹⁵ This difference occurs because Li ions can readily migrate through the SEI, whereas Ca ions cannot.¹⁵ As such, identifying appropriate electrolytes that can either form a Ca-ion-permeable SEI or does not form an SEI altogether, is one of the key thrusts in developing CIBs.¹⁶

Early studies, such as the seminal work by Aurbach et al.,¹⁵ concluded that it is impossible to deposit calcium on either noble-metal or calcium−metal electrodes with typical battery electrolytes. However, studies in the past five years have shown significant progress in reversible plating and stripping of calcium.¹⁰⁻¹³ For example, Ponrouch et al. used a calcium tetrafluoroborate ($Ca[BF_4]_2$) salt in a mixture of ethylene carbonate (EC) and propylene carbonate (PC) solvents to

Received: December 7, 2020
Accepted: March 2, 2021
Published: March 10, 2021

![](./images/812487599032631296_2.jpg)

© 2021 American Chemical Society
13114
https://dx.doi.org/10.1021/acsami.0c21716
ACS Appl. Mater. Interfaces 2021, 13, 13114−13122

reversibly deposit Ca at moderate temperatures (75−100 °C).¹¹ It is important to note that the authors could not deposit Ca from the calcium bis(trifluoromethanesulfonyl)-imide (Ca[TFSI]₂) salt using the same solvent mixture and elevated temperatures. Later, Wang et al. demonstrated the reversible plating and stripping of calcium at room temperature using calcium borohydride (Ca[BH₄]₂) in tetrahydrofuran (THF).¹⁰ While these works successfully established the feasibility of reversible Ca deposition, the $BH_4^-$ and $BF_4^-$ anion used in these works is known to suffer from intrinsic instability toward oxidation.¹²,¹³

Earlier work on MIBs showed that bulkier anions, such as closo-carboranes (for example, $[CB_{11}H_{12}]^-)^{17}$ and alkoxyborates,¹⁸ possess superior oxidative stability. The bulkiness of these anions also enables charge delocalization over a large spatial extent, further enhancing the cation mobility due to decreased anion−cation interactions. Inspired by these previous findings on MIBs, both Li et al.¹² and Shyamsunder et al.¹³ considered the calcium tetrakis-(hexafluoroisopropyloxy)borate salt, $Ca[B(hfip)_4]_2$, in dimethoxyethane and showed facile calcium deposition with high ionic conductivity (>8 ms cm⁻¹) and high anionic oxidation stability (up to 4.5 V versus Ca). However, even with these bulky anions, side products such as CaF₂ were observed during reduction.¹³ While earlier work on magnesium carborane salts did not show any side products,¹⁷ to the best of our knowledge, the successful synthesis of calcium carborane salts has not yet been reported. As such, despite considerable breakthroughs in the development of CIBs, there is significant room to improve the stability of electrolytes. Moreover, the decomposition mechanisms of the salt/solvent at the calcium anode are still not fully understood, and a deep understanding of this effect is essential for probing the composition of the SEI, which further affects the plating/stripping of Ca. Furthermore, the decomposed products would provide fundamental insight into the physical and chemical properties of the electrolytes to further enhance their efficiency.

To bridge this knowledge gap, we have carried out density functional theory (DFT) and ab initio molecular dynamics (AIMD) calculations to understand the reductive stability of four salts: (1) calcium hexafluorophosphate (Ca[PF₆]₂), (2) calcium closo-monocarborane (Ca[CB₁₁H₁₂]₂), (3) Ca[TFSI]₂, and (4) $Ca[B(hfip)_4]_2$, at both 300 and 500 K. Although the $Ca[CB_{11}H_{12}]_2$ salt has not been synthesized, we provide predictions of its stability as a promising candidate salt, based on the success of its magnesium analogue. Apart from these salts, we also investigated the three most commonly used organic solvents in battery systems, including EC, PC, and tetraethylene glycol dimethyl ether (G4). Together, these ab initio calculations provide a comprehensive understanding of the various decomposition pathways of electrolytes on the calcium surface. Most importantly, our calculations provide essential design principles to enable a rational path toward rechargeable Ca-ion batteries.

## COMPUTATIONAL DETAILS

Our electronic structure and Born−Oppenheimer molecular dynamics (BOMD) simulations were performed with Kohn−Sham density functional theory using the Perdew−Burke−Ernzerhof exchange-correlation functional¹⁹ and molecularly optimized double-ζ quality (DZVP) basis set²⁰ as implemented in the CP2K software package.²¹ For the auxiliary plane-wave (PW) basis, we used 300 Ry for the PW energy cutoff and 60 Ry for the reference grid cutoff. Goedecker- Teter-Hutter pseudopotentials,²²,²³ which are compatible with the employed basis sets, were used for all the elements. Dispersion interactions were included using Grimme’s D3- dispersion correction.²⁴ Due to the large supercell sizes considered in our simulations (see the *Supporting Information*, SI), the Brillouin zone integration was performed only at the Γ-point. All optimization calculations were converged until the forces on all atoms were less than 0.02 eV/Å. Optimized geometries of the salt-surface/solvent-surface interfaces were subsequently used as the initial configurations for the NVT simulations. For predicting reaction barriers, we carried out climbing image nudged elastic band (CI-NEB) calculations with a minimum of four images between the reactants and products.

BOMD simulations were performed in a canonical ensemble (NVT) at both 300 and 500 K, and these temperatures were maintained using the Nosé−Hoover thermostat of chain length three. The equations of motion were integrated with a 1 fs time step (using a tritium mass for the hydrogen atoms). Time- dependent charge-transfer analyses were conducted using Mulliken charges, which were printed at each time step. Similarly, time-dependent projected density of states (TD- PDOS) analyses were conducted at specific time steps. Geometries at these time steps were read from the trajectory files, and wave function (SCF) optimization was performed. Additional computational setup parameters and details are given in the SI.

## RESULTS AND DISCUSSION

Figure 1 depicts all the salts and solvents studied in this work. Most of these solvent and salt-anion combinations continue to

![](./images/812487599032631296_3.jpg)

Figure 1. Various salts and solvents examined in this work. Salts: (a) calcium hexafluorophosphate (Ca[PF₆]₂), (b) calcium closo-monocarborane $(Ca[CB_{11}H_{12}]_2)$, (c) calcium bis-(trifluoromethanesulfonyl)imide (Ca[TFSI]₂), and (d) calcium tetrakis(hexafluoroisopropyloxy)borate ($Ca[B(hfip)_4]_2$). Solvents: (e) ethylene carbonate (EC), (f) tetraethylene glycol dimethyl ether (G4), and (g) propylene carbonate (PC).

![](./images/812487599032631296_4.jpg)

Figure 2. Geometries of different salt molecules on a Ca surface at the beginning (a, c, e, and g) and end (b, d, f, and h) of an NVT simulation performed at 300 K. Simulation snapshots with Ca[TFSI]₂, Ca[PF₆]₂, Ca[B(hfip)₄]₂, and Ca[CB₁₁H₁₂]₂ salts were taken at (b) 5, (d) 5, (f) 10, and (h) 15 ps, respectively. While Ca[TFSI]₂ and Ca[PF₆]₂ completely decomposed at 300 K (panels b and d), Ca[B(hfip)₄]₂ and Ca[CB₁₁H₁₂]₂ remained mostly intact (panels f and h) throughout the simulation. In panel f, the red circle shows the fragmentation of one of the carbon−fluorine bonds in the Ca[B(hfip)₄]₂ salt, which occurred at ∼2 ps (see Figure 3 and the main text for details). After that fragmentation event, the structure remained intact for more than 8 ps.

be used in existing battery technologies.²⁵⁻³¹ For example, EC, PC, and glyme solvents, along with PF₆ and TFSI anions, have previously been used in both LIB and MIB technologies.²⁵⁻³¹ Similarly, recent studies showed that both Mg[B(hfip)₄]₂ and Mg[CB₁₁H₁₂]₂ are more suitable than Mg[TFSI]₂ for reversible plating and stripping of Mg in MIBs.¹⁷,¹⁸ However, except for a few experiments,¹¹⁻¹³ most of these electrolytes have not been entirely explored in the context of CIBs. Considering their importance in battery technologies, we examined their reductive stability on the Ca surface. We first present our results on salt-Ca interfaces and then proceed to a discussion of our solvent-Ca interface calculations.

Stability of Salts on the Calcium Electrode Surface.
To investigate the stability of electrolytes on Ca electrode surfaces, we carried out AIMD simulations on the optimized electrode−surface−electrolyte models. Figure 2 depicts the geometries of each salt at the initial and final steps of an NVT simulation conducted at 300 K on a Ca surface. As shown in Figure 2, parts b and d, both Ca[TFSI]₂ and Ca[PF₆]₂ completely decomposed, suggesting their instability on a Ca surface even at room temperature. The decomposed salt species penetrated the second layer of the Ca surface and formed various products such as CaF₂, CaO, CaS, etc. Our results are in good agreement with several earlier experiments, which showed the formation of CaF₂ with fluorine-containing salts.²,¹¹,¹³,³² Moreover, the complete decomposition of TFSI anions in our simulations explains earlier experimental results²,¹¹ showing that reversible plating and stripping of Ca was impossible with the Ca[TFSI]₂ salt. Interestingly, we find that the initial stages of the decomposition mechanism of TFSI anions on the Ca surface are similar to those observed on the Li surface.³³,³⁴ Specifically, on both surfaces, the S−CF₃ bond dissociated first, followed by the dissociation of the C−F bonds in the detached CF₃ group. As such, our results indicate that the S−C bond is prone to reductive fragmentation, which further initiates the complete decomposition of the TFSI anion on a Ca surface.

Although there have been experimental studies on the synthesis of Ca[PF₆]₂,³⁵,³⁶ to the best of our knowledge, there has been no successful demonstration of reversible Ca deposition using Ca[PF₆]₂ on a calcium electrode. On the basis of our BOMD simulations, we predict that Ca[PF₆]₂ is ill-suited for rechargeable CIBs since it completely decomposes on a Ca surface. A few studies showing reversible Ca deposition using Ca[PF₆]₂ on noncalcium electrodes also observed the formation of CaF₂, confirming its poor stability.¹⁴,³²

Unlike Ca[TFSI]₂ and Ca[PF₆]₂, both Ca[B(hfip)₄]₂ and Ca[CB₁₁H₁₂]₂ remained mostly intact throughout the simulation (see Figure 2, parts f and h). With Ca[B(hfip)₄]₂, we observed the fragmentation of a C−F bond during the first 2 ps of the simulation, with no further bond cleavage during the remaining simulation period (10 ps). This observation supports recent experiments in two aspects:¹²,¹³ (1) our simulations validate that Ca[B(hfip)₄]₂ is not entirely stable on a Ca surface; in other words, a few of the C−F bonds are cleaved to form CaF₂,¹³ and (2) our predictions confirm that only minor quantities of CaF₂ will be formed when Ca[B(hfip)₄]₂ is used, unlike other fluorine-containing salts.¹² Specifically, earlier experiments showed that only a 7% molar ratio of CaF₂ was formed with Ca[B(hfip)₄]₂,¹² but more than 30% was observed with Ca(BF₄)₂.¹¹ Although an exact percentage was not reported for Ca[TFSI]₂ and Ca[PF₆]₂, we can accurately project that much higher portions (>50%) of CaF₂ would be formed (since these salts do not exhibit a reversible Ca deposition). Our simulations also predict a lower decomposition rate for Ca[B(hfip)₄]₂ than other fluorine-containing salts in our study; i.e., we observed a complete decomposition of Ca[TFSI]₂ and Ca[PF₆]₂ in 5 ps, but Ca[B(hfip)₄]₂ remained almost intact during 10 ps (except for a single C−F bond dissociation, which occurred at around 2 ps).

Contrary to the fluorine-containing salts, we did not observe any bond cleavage in Ca[CB₁₁H₁₂]₂ even up to 15 ps. As such, Ca[CB₁₁H₁₂]₂ has a superior stability among all the salts studied in this work. The exceptional stability of CB₁₁H₁₂ anion on a Ca surface is identical to earlier experiments with this anion on an Mg surface, where no side products were observed.¹⁷ We also carried out additional BOMD simulations at a higher temperature of 500 K, which further confirmed that the CB₁₁H₁₂ anion has remarkable stability compared to the other anions (see Figure S1).

After confirming the stability of the Ca[B(hfip)₄]₂ and Ca[CB₁₁H₁₂]₂ salts on a Ca surface at both 300 and 500 K, we turned our attention to understanding the stability differences among the four salts. Earlier theoretical studies on the interfaces of various electrolytes with Li or Mg surfaces suggested that the instability of an electrolyte was often associated with a substantial charge transfer (CT) across the interface.³³,³⁷⁻³⁹ As such, we first analyzed the time-dependent charge transfer (TD-CT) trends between each salt and the Ca

![](./images/812487599032631296_5.jpg)

Figure 3. Time-dependent charge-transfer (TD-CT) from the calcium surface to (a) $Ca[TFSI]_2$, (b) $Ca[PF_6]_2$, (c) $Ca[B(hfip)_4]_2$, and (d) $Ca[CB_{11}H_{12}]_2$ salts at 300 K. In all panels, the amount of charge donated by a fragment is shown as a positive value, and the charge gained by a fragment is shown as a negative value on the vertical axis. In panels (a), (b), and (c), charge transfer from the surface to the salt is observed. Both the $Ca[TFSI]_2$ and $Ca[PF_6]_2$ salts gained ~8 electrons from the Ca surface in the first 3 ps of the simulation (panels b and d). Beyond 3 ps, only minor charge fluctuations are observed. Similarly, $Ca[B(hfip)_4]_2$ gained only two electrons (at around 2 ps), and $Ca[CB_{11}H_{12}]_2$ did not accept any electrons (it has the highest reductive stability) from the Ca surface. In all cases, most of the electrons were transferred from the top layer (Ca L1) of the Ca surface to the salt.

surface to understand their redox stability at 300 K. Following the usual convention, an anion is said to be reduced (oxidized) when it accepts (donates) electrons from the Ca surface, and its reductive (oxidative) stability is considered to be lower when it decomposes by accepting (donating) electrons. An anion that neither accepts nor donates an electron will have superior redox stability.

Figure 3 depicts the charge donated/gained by a fragment (a surface or a salt or their components). Except for the $CB_{11}H_{12}$ anion, there is an apparent charge transfer from the Ca surface (red line) to the anions (orange and green lines). In other words, three out of the four salts were reduced by the Ca surface. Also, both $Ca[TFSI]_2$ and $Ca[PF_6]_2$ acquired more charge (eight electrons) from the Ca surface than $Ca[B(hfip)_4]_2$ (two electrons) or $Ca[CB_{11}H_{12}]_2$ (zero electrons), suggesting the lower reductive stability of the former salts. As such, among the anions that we studied, $CB_{11}H_{12}$ showed exceptional reductive stability followed by $B(hfip)_4$.

It is important to note that when an anion was reduced, the electrons were primarily transferred from the top layer of the Ca surface, which is in direct contact with the salt. Also, we did not observe a considerable change in CT beyond 3 ps for any of our simulations. Similar TD-CT results were obtained for all salts at 500 K (see Figure S2), which showed a quicker CT from the Ca surface to the salt compared to 300 K.

While the TD-CT analysis confirms that $Ca[TFSI]_2$ and $Ca[PF_6]_2$ decompose via reduction, and $Ca[B(hfip)_4]_2$ and $Ca[CB_{11}H_{12}]_2$ have superior reductive stability, it does not provide a microscopic rationale for the differences in stability among the salts. To obtain a more in-depth understanding, we studied the time-dependent projected density of states (TD-PDOS) of $Ca(TFSI)_2$ and $Ca[CB_{11}H_{12}]_2$ salts adsorbed onto the Ca surface at 300 K. Specifically, we examined changes in the lowest unoccupied molecular orbital (LUMO) of the salt as a function of time. When the Fermi level of the anode (i.e., the Ca surface) lies above the LUMO of a salt, an electron can transfer from the Ca surface to the salt, resulting in the reduction of the salt.⁴⁰ As such, a salt is stable toward anode reduction only when its LUMO is above the Fermi level of the anode. Figure 4 presents the TD-PDOS plots of $Ca[TFSI]_2$, and the Fermi level of the composite (salt + surface) system is shown in dashed lines. The absolute position of the Fermi level in the composite system is very close to its position in the pure Ca surface (not shown); in other words, the adsorption of the salt did not affect the position of the Fermi level of Ca. The orange and green lines correspond to the PDOS of the TFSI

![](./images/812487599032631296_6.jpg)

Figure 4. Time-dependent projected density of states (TD-PDOS) of the $Ca[TFSI]_2$ salt adsorbed on a Ca surface at 300 K. Each panel shows the time step, PDOS, and the corresponding nuclear geometry. The Fermi level of the composite (salt+surface) system is shown in dashed lines. The orange and green lines correspond to the PDOS of the TFSI anions that are located on the right ($1^{st}$ TFSI) and left ($2^{nd}$ TFSI) sides of each geometry (in the insets), respectively. During the simulation, the anion on the left decomposed first (at around 1.38 ps), followed by the anion on the right (at around 1.7 ps).

anions that are located on the right ($1^{st}$ TFSI) and left ($2^{nd}$ TFSI) sides of each inset geometry, respectively.

Since the LUMOs of the salt are primarily located above the Fermi level at 0 ps, electrons cannot transfer from the Ca surface to the anions. As such, the geometry of the salt is completely intact at 0 ps. As the simulation progresses, due to the changes in surface−salt interactions, the LUMO levels of the salt become energetically closer to the Fermi level. At 1.3 ps, the LUMO of the salt (primarily composed of the second TFSI anion, depicted on the left side in each inset geometry) overlaps with the Fermi level, creating the possibility for a CT. At 1.38 ps, the second TFSI anion acquires electrons from the Ca surface and decomposes (the C−S bond is cleaved). From the PDOS plots at 1.3 and 1.38 ps, a clear crossing in the PDOS of the second TFSI anion (green line) across the Fermi level can be observed, indicating the transfer of an electron to this anion. The electron-transfer process continues until 1.4 ps. At 1.5 ps, the PDOS of the first TFSI (orange-line) become energetically closer to the Fermi level, and by 1.7 ps, the electron transfer occurs, leading to the cleavage of the C−S bond in the first TFSI (anion on the right side in each inset geometry). Overall, we find a one-to-one correspondence between the TD-PDOS and the salt decomposition process.

Although Figure 4 only shows the cleavage of the $S-CF_3$ bond, all other bonds (such as N−S, S−O, and C−F) were also cleaved during the NVT runs (both at 300 and 500 K). Indeed, from our CI-NEB calculations, we find that the transition state barriers for most of these bonds are in the range of 30−330 meV, often involving the elongation/cleavage of the N−S bond in the transition state (see Figures S3−S5). It is important to note that all these bond cleavage reactions are highly exothermic on a Ca surface, releasing up to 1−4 eV of energy (see Figures S3−S5). As a consequence, a bond-breaking event catalyzes the further dissociation of other bonds, as observed in our NVT simulations. A similar TD-PDOS analysis for the $Ca[CB_{11}H_{12}]_2$ salt is presented in Figure S7, where we observed only minor changes in the PDOS with time, resulting in the absence of a CT between the Ca surface and the salt. Also, from our CI-NEB calculations, we find that the transition state barrier for B−B bond cleavage in

![](./images/812487599032631296_7.jpg)

Figure 5. Geometries of different solvent−surface interfaces at the beginning (a−c) and end (d−f) of an NVT simulation performed at 300 K. All simulations were carried out for at least 10 ps. While EC (d) and PC (e) solvents decomposed at 300 K to form an interphase with the Ca-surface, the G4 solvent (f) remained intact throughout the simulation, indicating its superior stability over the carbonate solvents.

$Ca[CB_{11}H_{12}]_2$ is $\sim$1.1 eV (see Figure S6). Finally, it is important to mention that unlike the TD-PDOS calculations, the ground-state PDOS calculations did not provide any rationale for the observed stability differences among salts (see Figure S8). As such, our results strongly suggest that the inclusion of dynamics is essential for understanding the stability of salt−Ca interactions in these systems.

Stability of Solvents on a Calcium Electrode Surface.
For reversible Ca deposition, apart from the availability of salts with good thermal and electrochemical stability, it is equally important to select solvents that would not decompose on the highly reductive Ca surface. To this end, we examined the stability of EC, PC, and G4 solvents on a Ca surface. Figure 5 presents geometries of the solvent−Ca interfaces at the initial and final steps of an NVT simulation conducted at 300 K. Following previous works on solvent−surface interfaces,27,33,41 a vacuum space was not incorporated along the c-direction of the simulation cell, which allows the solvent molecules to interact with both sides of the six-layer Ca surface. Among the three solvents that we studied, G4 exhibited superior stability over the carbonate (EC and PC) solvents at both 300 and 500 K (see Figure S9). We note that 500 K is within the liquidus range of EC, PC, and G4 solvents.11 Also, 500 K (=226.85 °C) is well below the boiling point of all of these solvents, which are 238, 242, and 275 °C for EC, PC, and G4, respectively.

From our TD-CT analysis (Figure 6), we find that the remarkable stability of G4 stems from its higher reductive stability compared to EC and PC. Indeed, while both the EC and PC solvents acquired around 6−25 electrons from the Ca surface, there was no appreciable charge transfer (<0.2 electrons) between G4 and the Ca surface even at 500 K. From our CI-NEB calculations, we find that the reaction barriers for the cleavage of various bonds in the EC and PC molecules on a Ca surface are comparable to energy fluctuations at room temperature (20−70 meV, see Figures

![](./images/812487599032631296_8.jpg)

Figure 6. Time-dependent charge-transfer (TD-CT) from the calcium surface to (a, b) EC, (c, d) PC solvents at 300 and 500 K, and (f) G4 solvent at 500 K. Panel (e) shows the geometry of the G4 solvent on top of the Ca surface after 10 ps of an NVT simulation at 500 K. The six layers of the calcium surface (L1−L6) are depicted with the same colors as in panels a−d and f. Both the EC and PC solvents gained electrons from the Ca surface and decomposed at both 300 and 500 K. G4 did not accept any electrons (it has the highest reductive stability) from the Ca surface at either of the temperatures (see Figure S10 for the TD-CT plot of the G4−Ca interface at 300 K). In all cases, most of the electrons were transferred from the Ca layers that are in direct contact with the solvent (Ca L1 and Ca L6).

![](./images/812487599032631296_9.jpg)

Figure 7. Various steps depicting the decomposition mechanisms of EC (a−e) and PC (f−l), solvents as observed in our BOMD simulations. For both EC and PC at 500 K, we observed the formation of either CO or $CO_3^{2-}$ fragments, depending on whether the electrons transfer to EC in a sequential or concerted manner, respectively. For EC at 500 K, apart from the products at 300 K, we also observed either the decomposition of the CO molecule into carbon and oxygen atoms or the formation of a CO dimer. For PC at 500 K, apart from the products at 300 K, we observed the formation of $CO_2$ and oxygen atoms.

S11−S18), explaining the facile decomposition of these molecules on a Ca surface. However, the cleavage barriers for the bonds in the G4 molecule are roughly an order of magnitude (165−265 meV) higher than energy fluctuations at room temperature, reflecting their higher reductive stability.

Since our simulations at 300 and 500 K do not show any decomposition of G4 on a Ca surface (during the time scales of our simulation), we predict the absence of a passivation layer at the Ca−G4 interface. Earlier AIMD simulations by Balbuena and co-workers on 1,2-dimethoxyethane (G1) (which has a similar chemical structure to G4) on a Li surface also showed the absence of passivation at the Li−G1 interface,³⁴ in agreement with our results. In the absence of passivation, there would be a facile and reversible calcium deposition on a Ca surface. However, it is also worth noting that the solvation of the G4 molecules to the $Ca^{2+}$ cation can potentially impact the electrochemical deposition. Hahn et al. demonstrated that the coordination strength between the glyme solvent molecules and the $Ca^{2+}$ cation in $Ca(TFSI)_2$ electrolytes is critical to the electrochemical deposition of Ca.⁴² The importance of the solvation of $Ca^{2+}$ was also highlighted by previous studies on the cathodic stability of $Mg^{2+}$−glyme solvation during Mg deposition. Lautar et al. also suggested that the solvated $[Mg(G1)_3]^{2+}$ cation could cathodically decompose on the Mg surface.⁴³ Seguin et al. showed that solvated glyme molecules (G1, diglyme, and triglyme in their study) can be decomposed via cleavage of a nonterminal C−O bond by the partially reduced $Mg^+$ during Mg deposition.⁴⁴ Yu et al. also suggested that Mg electrode surface impurities such as under-coordinated Mg can catalyze the decomposition of solvated diglyme molecules.⁴⁵ Overall, our work confirms the chemical stability of G4 in Ca-ion electrolytes and calls for additional studies to probe the stability at the Ca/electrolyte interface under a cathodic potential.

Figure 7 shows the degradation mechanisms of EC and PC solvents observed in our BOMD simulations at 300 and 500 K. For both EC and PC at 500 K, we observed the generation of either CO or $CO_3^{2-}$ fragments, depending on whether the electrons transfer to EC in a sequential (Figure 7, parts a−d or f−i) or concerted manner (Figure 7, parts a/e, and f/j), respectively. At 300 K, however, we only observed the generation of CO but not the generation of $CO_3^{2-}$ fragment during our simulation time scales. Similar decomposition mechanisms for the EC solvent were earlier observed on the Li and Ca surfaces.²⁷,³³ For example, Balbuena and co-workers showed that the dissociation of CO and $CO_3^{2-}$ fragments from EC molecules was triggered by an electron transfer from the Li surface. For EC at 500 K, we also observed the decomposition of the CO molecule into carbon and oxygen atoms, and the formation of a CO dimer (Figure 7 inset). For PC, we observed the formation of $CO_2$ and oxygen atoms at 500 K (Figure 7, parts k and l). Since an elevated temperature is often used as a simulation parameter to explore the phase space within a short simulation duration, we expect that the products obtained in our 500 K simulations would also be observed in the experiments at room temperature.

It is interesting to note that there is a one-to-one correspondence between the number of electrons transferred from the Ca surface and the number of bonds broken in the solvent layer. For example, at 300 K, the PC solvent layer gained roughly six electrons in 12 ps. Accordingly, we find that the carbonyl groups of three PC molecules dissociated (each

carbonyl carbon forms two bonds with oxygen atoms in the PC molecule. As such, a total of six bonds were dissociated, which is equal to the number of electrons transferred). Also, we find that the individual electron-transfer events can be distinctly observed from the TD-CT plots. As shown in Figure 6c, the first electron transferred at ~1.1 ps. This transfer resulted in the bending of the carbonyl group (Figure 7g) followed by the dissociation of one of the C1−O2/C1−O3 bonds of the PC molecule (Figure 7h). Next, at ~2 ps, another electron transfer occurs, resulting in the complete dissociation of the CO group from the PC (Figure 7i). Similarly, electron-transfer events at 5 and 6 ps and at 6.5 and 8.5 ps resulted in the dissociation of the CO groups in two other PC molecules. Together, these analyses provide a clear mechanistic understanding of the decomposition behavior of various salts and solvents on a Ca surface.

## CONCLUSIONS
In summary, we carried out BOMD simulations to examine the stability of various technologically relevant salts and solvents for CIBs. Our simulations suggest that the G4 solvent and $Ca[CB_{11}H_{12}]_2$ salt have the highest reductive stability at the Ca surface over a wide range of temperatures (they exhibit superior reductive stability at both 300 and 500 K). Among the other salts, the $Ca[B(hfip)_4]_2$ salt showed reasonable stability during the 10 ps simulation propagation time. We strongly anticipate that Ca can be reversibly deposited in glyme solvents using either $Ca[B(hfip)_4]_2$ or $Ca[CB_{11}H_{12}]_2$ salt.

Both salts ($Ca[TFSI]_2$ and $Ca[PF_6]_2$) and solvents (EC and PC) exhibited poor reductive stability and decomposed at both 300 and 500 K. As such, we find them to be less suitable for CIBs. Detailed mechanisms of their decomposition were made possible using time-dependent structural analysis techniques, including TD-PDOS, TD-CT, and CI-NEB analyses. Most importantly, we find that static electronic structure calculations alone cannot provide a rationale for the superior stability of $Ca[CB_{11}H_{12}]_2$ over the $Ca[TFSI]_2$ and $Ca[PF_6]_2$ salts, and the inclusion of dynamical effects is essential. Since the BOMD simulations used in this work inherently capture these dynamical effects, we recommend the use of these techniques (as opposed to only static DFT calculations) for predicting salt/solvent stability and obtaining a more holistic understanding of these systems. Taken together, our work provides a rational path for designing next-generation multivalent electrolytes for energy storage applications (particularly calcium batteries), which require exceptional electrolyte reductive stability to achieve their maximum potential.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at
https://pubs.acs.org/doi/10.1021/acsami.0c21716.

Additional computational details, stability, and TD-CT plots of salts at 500 K, minimum energy paths for the various bond dissociations of salt and solvent molecules on a Ca surface, TD-PDOS plots of the $Ca[CB_{11}H_{12}]_2$ salt, ground-state PDOS plots of isolated salts and salts adsorbed on the Ca surface, variation in the solvent/salt distance from the Ca surface, supporting figures, and NVT input file (PDF)

## AUTHOR INFORMATION

### Corresponding Authors
Juchen Guo − Department of Chemical & Environmental Engineering, Materials Science & Engineering Program, and Department of Chemistry, University of California—Riverside, Riverside, California 92521, United States;
orcid.org/0000-0001-9829-1202; Email: jguo@engr.ucr.edu

Bryan M. Wong − Department of Chemical & Environmental Engineering, Materials Science & Engineering Program, and Department of Chemistry, University of California—Riverside, Riverside, California 92521, United States;
orcid.org/0000-0002-3477-8043; Email: bryan.wong@ucr.edu

### Authors
Sharma S. R. K. C. Yamijala − Department of Chemical & Environmental Engineering, Materials Science & Engineering Program, and Department of Chemistry, University of California—Riverside, Riverside, California 92521, United States; orcid.org/0000-0003-1773-9226

Hyuna Kwon − Department of Chemical & Environmental Engineering, University of California—Riverside, Riverside, California 92521, United States

Complete contact information is available at:
https://pubs.acs.org/10.1021/acsami.0c21716

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
S.S.R.K.C.Y., H.K., and B.M.W. acknowledge support by the U.S. Department of Energy, Office of Science, Early Career Research Program under Award No. DE-SC0016269. J.G. acknowledges support by the National Science Foundation under grant No. DMR-2004497.

## REFERENCES
(1) Manthiram, A. A Reflection on Lithium-Ion Battery Cathode Chemistry. Nat. Commun. 2020, 11 (1), 1550.

(2) Arroyo-De Dompablo, M. E.; Ponrouch, A.; Johansson, P.; Palacín, M. R. Achievements, Challenges, and Prospects of Calcium Batteries. Chem. Rev. 2020, 120 (14), 6331−6357.

(3) Canepa, P.; Sai Gautam, G.; Hannah, D. C.; Malik, R.; Liu, M.; Gallagher, K. G.; Persson, K. A.; Ceder, G. Odyssey of Multivalent Cathode Materials: Open Questions and Future Challenges. Chem. Rev. 2017, 117 (5), 4287−4341.

(4) Baba, T.; Sodeyama, K.; Kawamura, Y.; Tateyama, Y. Li-Ion Transport at the Interface between a Graphite Anode and LiCO Solid Electrolyte Interphase: Ab Initio Molecular Dynamics Study. Phys. Chem. Chem. Phys. 2020, 22 (19), 10764−10774.

(5) Olivetti, E. A.; Ceder, G.; Gaustad, G. G.; Fu, X. Lithium-Ion Battery Supply Chain Considerations: Analysis of Potential Bottlenecks in Critical Metals. Joule 2017, 1 (2), 229−243.

(6) Grey, C. P.; Tarascon, J. M. Sustainability and in Situ Monitoring in Battery Development. Nat. Mater. 2017, 16 (1), 45−56.

(7) Vaalma, C.; Buchholz, D.; Weil, M.; Passerini, S. A Cost and Resource Analysis of Sodium-Ion Batteries. Nat. Rev. Mater. 2018, 3 (4), 18013.

(8) Li, M.; Lu, J. Cobalt in Lithium-Ion Batteries. Science 2020, 367 (6481), 979−980.

(9) Okoshi, M.; Chou, C.-P.; Nakai, H. Theoretical Analysis of Carrier Ion Diffusion in Superconcentrated Electrolyte Solutions for Sodium-Ion Batteries. J. Phys. Chem. B 2018, 122 (9), 2600−2609.

(10) Wang, D.; Gao, X.; Chen, Y.; Jin, L.; Kuss, C.; Bruce, P. G. Plating and Stripping Calcium in an Organic Electrolyte. *Nat. Mater.* 2018, **17** (1), 16−20.

(11) Ponrouch, A.; Frontera, C.; Bardé, F.; Palacín, M. R. Towards a Calcium-Based Rechargeable Battery. *Nat. Mater.* 2016, **15** (2), 169−172.

(12) Li, Z.; Fuhr, O.; Fichtner, M.; Zhao-Karger, Z. Towards Stable and Efficient Electrolytes for Room-Temperature Rechargeable Calcium Batteries. *Energy Environ. Sci.* 2019, **12** (12), 3496−3501.

(13) Shyamsunder, A.; Blanc, L. E.; Assoud, A.; Nazar, L. F. Reversible Calcium Plating and Stripping at Room Temperature Using a Borate Salt. *ACS Energy Letters* 2019, **4** (9), 2271−2276.

(14) Lipson, A. L.; Pan, B.; Lapidus, S. H.; Liao, C.; Vaughey, J. T.; Ingram, B. J. Rechargeable Ca-Ion Batteries: A New Energy Storage System. *Chem. Mater.* 2015, **27** (24), 8442−8447.

(15) Aurbach, D.; Skaletsky, R.; Gofer, Y. The Electrochemical Behavior of Calcium Electrodes in a Few Organic Electrolytes. *J. Electrochem. Soc.* 1991, **138** (12), 3536−3545.

(16) Gao, X.; Liu, X.; Mariani, A.; Elia, G. A.; Lechner, M.; Streb, C.; Passerini, S. Alkoxy-Functionalized Ionic Liquid Electrolytes: Under-standing Ionic Coordination of Calcium Ion Speciation for the Rational Design of Calcium Electrolytes. *Energy Environ. Sci.* 2020, **13** (8), 2559−2569.

(17) Jay, R.; Tomich, A. W.; Zhang, J.; Zhao, Y.; De Gorostiza, A.; Lavallo, V.; Guo, J. Comparative Study of ${\text{Mg}(\text{CB}_{11}\text{H}_{12})}_{2}$ and ${\text{Mg}(\text{TFSI})}_{2}$ at the Magnesium/Electrolyte Interface. *ACS Appl. Mater. Interfaces* 2019, **11** (12), 11414−11420.

(18) Zhao-Karger, Z.; Liu, R.; Dai, W.; Li, Z.; Diemant, T.; Vinayan, B. P.; Bonatto Minella, C.; Yu, X.; Manthiram, A.; Behm, R. J.; Ruben, M.; Fichtner, M. Toward Highly Reversible Magnesium-Sulfur Batteries with Efficient and Practical ${\text{Mg}[\text{B}(\text{hfp})_{4}]}_{2}$ Electrolyte. *ACS Energy Letters* 2018, **3** (8), 2005−2013.

(19) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* 1996, **77**, 3865−3868.

(20) VandeVondele, J.; Hutter, J. Gaussian Basis Sets for Accurate Calculations on Molecular Systems in Gas and Condensed Phases. *J. Chem. Phys.* 2007, **127** (11), 114105.

(21) VandeVondele, J.; Krack, M.; Mohamed, F.; Parrinello, M.; Chassaing, T.; Hutter, J. Quickstep: Fast and Accurate Density Functional Calculations Using a Mixed Gaussian and Plane Waves Approach. *Comput. Phys. Commun.* 2005, **167**, 103−128.

(22) Goedecker, S.; Teter, M.; Hutter, J. Separable Dual-Space Gaussian Pseudopotentials. *Phys. Rev. B: Condens. Matter Mater. Phys.* 1996, **54** (3), 1703−1710.

(23) Krack, M. Pseudopotentials for H to Kr Optimized for Gradient-Corrected Exchange-Correlation Functionals. *Theor. Chem. Acc.* 2005, **114**, 145−152.

(24) Grimme, S.; Ehrlich, S.; Goerigk, L. Effect of the Damping Function in Dispersion Corrected Density Functional Theory. *J. Comput. Chem.* 2011, **32** (7), 1456−1465.

(25) Ha, S.-Y.; Lee, Y.-W.; Woo, S. W.; Koo, B.; Kim, J.-S.; Cho, J.; Lee, K. T.; Choi, N.-S. Magnesium(II) Bis(trifluoromethane Sulfonyl) Imide-Based Electrolytes with Wide Electrochemical Windows for Rechargeable Magnesium Batteries. *ACS Appl. Mater. Interfaces* 2014, **6** (6), 4063−4073.

(26) Ma, Z.; Kar, M.; Xiao, C.; Forsyth, M.; MacFarlane, D. R. Electrochemical Cycling of Mg in ${\text{Mg}[\text{TFSI}]}_{2}$/tetraglyme Electrolytes. *Electrochem. Commun.* 2017, **78**, 29−32.

(27) Young, J.; Kulick, P. M.; Juran, T. R.; Smeu, M. Comparative Study of Ethylene Carbonate-Based Electrolyte Decomposition at Li, Ca, and Al Anode Interfaces. *ACS Applied Energy Materials.* 2019, **2**, 1676−1684.

(28) Aurbach, D.; Markovsky, B.; Shechter, A.; Ein-Eli, Y.; Cohen, H. A Comparative Study of Synthetic Graphite and Li Electrodes in Electrolyte Solutions Based on Ethylene Carbonate-Dimethyl Carbonate Mixtures. *J. Electrochem. Soc.* 1996, **143**, 3809−3820.

(29) Dahbi, M.; Ghamouss, F.; Tran-Van, F.; Lemordant, D.; Anouti, M. Comparative Study of EC/DMC LiTFSI and $\text{LiPF}_{6}$ Electrolytes for Electrochemical Storage. *J. Power Sources* 2011, **196**, 9743−9750.

(30) Pappenfus, T. M.; Henderson, W. A.; Owens, B. B.; Mann, K. R.; Smyrl, W. H. Complexes of Lithium Imide Salts with Tetraglyme and Their Polyelectrolyte Composite Materials. *J. Electrochem. Soc.* 2004, **151**, A209−A215.

(31) Doi, T.; Masuhara, R.; Hashinokuchi, M.; Shimizu, Y.; Inaba, M. Concentrated $\text{LiPF}_{6}$/PC Electrolyte Solutions for 5-V Li-$\text{Ni}_{0.5}\text{Mn}_{1.5}\text{O}_{4}$ Positive Electrode in Lithium-Ion Batteries. *Electrochim. Acta* 2016, **209**, 219−224.

(32) Wang, M.; Jiang, C.; Zhang, S.; Song, X.; Tang, Y.; Cheng, H.-M. Reversible Calcium Alloying Enables a Practical Room-Temperature Rechargeable Calcium-Ion Battery with a High Discharge Voltage. *Nat. Chem.* 2018, **10** (6), 667−672.

(33) Camacho-Forero, L. E.; Smith, T. W.; Bertolini, S.; Balbuena, P. B. Reactivity at the Lithium-Metal Anode Surface of Lithium-Sulfur Batteries. *J. Phys. Chem. C* 2015, **119** (48), 26828−26839.

(34) Camacho-Forero, L. E.; Balbuena, P. B. Effects of Charged Interfaces on Electrolyte Decomposition at the Lithium Metal Anode. *J. Power Sources* 2020, **472**, 228449.

(35) Keyzer, E. N.; Matthews, P. D.; Liu, Z.; Bond, A. D.; Grey, C. P.; Wright, D. S. Synthesis of $\text{Ca(PF}_{6}\text{)}_{2}$ Formed via Nitrosonium Oxidation of Calcium. *Chem. Commun.* 2017, **53**, 4573−4576.

(36) Keyzer, E. N.; Matthews, P. D.; Liu, Z.; Bond, A. D.; Grey, C. P.; Wright, D. S. Correction: Synthesis of $\text{Ca(PF}_{6}\text{)}_{2}$ Formed via Nitrosonium Oxidation of Calcium. *Chem. Commun.* 2018, **54**, 12271−12271.

(37) Ando, Y.; Kawamura, Y.; Ikeshoji, T.; Otani, M. Electro-chemical Reduction of an Anion for Ionic-Liquid Molecules on a Lithium Electrode Studied by First-Principles Calculations. *Chem. Phys. Lett.* 2014, **612**, 240−244.

(38) Baskin, A.; Prendergast, D. Exploration of the Detailed Conditions for Reductive Stability of ${\text{Mg}(\text{TFSI})}_{2}$ in Diglyme: Implications for Multivalent Electrolytes. *J. Phys. Chem. C* 2016, **120**, 3583−3594.

(39) Zheng, Y.; Soto, F. A.; Ponce, V.; Seminario, J. M.; Cao, X.; Zhang, J.-G.; Balbuena, P. B. Localized High Concentration Electrolyte Behavior near a Lithium-metal Anode Surface. *J. Mater. Chem. A* 2019, **7**, 25047−25055.

(40) Kumar, N.; Siegel, D. J. Interface-Induced Renormalization of Electrolyte Energy Levels in Magnesium Batteries. *J. Phys. Chem. Lett.* 2016, **7** (5), 874−881.

(41) Li, Y.; Leung, K.; Qi, Y. Computational Exploration of the Li-Electrode/Electrolyte Interface in the Presence of a Nanometer Thick Solid-Electrolyte Interphase Layer. *Acc. Chem. Res.* 2016, **49** (10), 2363−2370.

(42) Hahn, N. T.; Driscoll, D. M.; Yu, Z.; Sterbinsky, G. E.; Cheng, L.; Balasubramanian, M.; Zavadil, K. R. Influence of Ether Solvent and Anion Coordination on Electrochemical Behavior in Calcium Battery Electrolytes. *ACS Appl. Energy Mater.* 2020, **3** (9), 8437−8447.

(43) KopačLautar, A.; Bitenc, J.; Rejec, T.; Dominiko, R.; Filhol, J.-S.; Doublet, M.-L. Electrolyte Reactivity in the Double Layer in Mg Batteries: An Interface Potential-Dependent DFT Study. *J. Am. Chem. Soc.* 2020, **142** (11), 5146−5153.

(44) Seguin, T. J.; Hahn, N. T.; Zavadil, K. R.; Persson, K. A. Elucidating Non-Aqueous Solvent Stability and Associated Decomposition Mechanisms for Mg Energy Storage Applications From First-Principles. *Front. Chem.* 2019, **7**, 175.

(45) Yu, Y.; Baskin, A.; Valero-Vidal, C.; Hahn, N. T.; Liu, Q.; Zavadil, K. R.; Eichhorn, B. W.; Prendergast, D.; Crumlin, E. J. Instability at the Electrode/Electrolyte Interface Induced by Hard Cation Chelation and Nucleophilic Attack. *Chem. Mater.* 2017, **29** (19), 8504−8512.