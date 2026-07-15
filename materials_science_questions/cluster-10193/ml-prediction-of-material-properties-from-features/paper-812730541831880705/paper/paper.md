![](./images/812730541831880705_1.jpg)

Subscriber access provided by TRINITY COLL

Article

# Simultaneously Achieving High Activity and Selectivity towards Two-Electron O2 Electroreduction: the Power of Single-Atom Catalysts

Xiangyu Guo, Shiru Lin, Jinxing Gu, Shengli Zhang, Zhongfang Chen, and Shiping Huang

ACS Catal., Just Accepted Manuscript • DOI: 10.1021/acscatal.9b02778 • Publication Date (Web): 23 Sep 2019

Downloaded from pubs.acs.org on September 24, 2019

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

---

is published by the American Chemical Society. 1155 Sixteenth Street N.W.,
Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the
course of their duties.

# Simultaneously Achieving High Activity and Selectivity towards Two-Electron
$O_2$ Electroreduction: the Power of Single-Atom Catalysts

Xiangyu Guo†, Shiru Lin§, Jinxing Gu§, Shengli Zhang‡,*, Zhongfang Chen§,*,
Shiping Huang†,*

† State Key Laboratory of Organic-Inorganic Composites, Beijing University of
Chemical Technology, Beijing 100029, China

‡ MIIT Key Laboratory of Advanced Display Materials and Devices, Ministry of
Industry and Information Technology, Institute of Optoelectronics & Nanomaterials,
Nanjing University of Science and Technology, Nanjing, 210094

§ Department of Chemistry, University of Puerto Rico, San Juan, PR 00931, USA

**ABSTRACT**

On-site production of hydrogen peroxide ($\text{H}_2\text{O}_2$) using electrochemical methods could be more efficient than the current industrial process. However, due to the existence of scaling relations for the adsorption of reaction intermediates, there is long established trade-off between the activity and selectivity of catalysts, as the enhancement of catalytic activity is typically accompanied by four-electron $\text{O}_2$ reduction reaction (ORR), leading to the reduced selectivity for the $\text{H}_2\text{O}_2$ production.

Herein, by means of density functional theory (DFT) computations, we reported the feasibility of several classes of important and representative experimentally achievable single-atom catalysts (SACs) towards two-electron ORR, paying attention to their stability, selectivity, and activity at the acidic medium. Starting from 210 two-dimensional (2D) SACs, we demonstrated that SACs have the potential to break the metal-based scaling relations and simultaneously achieve high activity and selectivity towards $\text{H}_2\text{O}_2$ production, and screened out 7 SACs with higher activity than the $\text{PtHg}_4$ in acid media. Especially, a noble metal-free SAC, namely single Zn atom centered phthalocyanine ($\text{Zn@Pc-N}_4$), has a remarkable activity improvement with a small overpotential of 0.15 V. Moreover, using multi-variable analysis and machine-learning techniques, we provided a comprehensive understanding of the underlying origin of the selectivity and activity of SACs, and unveiled the intrinsic correlation between structure and catalytic performance. This work may pave a way to the design and discovery of more promising materials for $\text{H}_2\text{O}_2$ production.

**KEYWORDS:** single-atom catalysts, two-dimensional materials, oxygen reduction reaction, $\ce{H_{2}O_{2}}$ production, density functional theory calculations, machine learning

## 1. INTRODUCTION

$\ce{H_{2}O_{2}}$ is not only a versatile and environmentally benign chemical oxidant widely used for water treatment,¹⁻² pulp bleaching,³ and chemical synthesis,⁴ but also a potential candidate for energy storage.⁵ Nowadays, the substantial demand for $\ce{H_{2}O_{2}}$ places this chemical as one of the important products in the world. However, the industrial production of $\ce{H_{2}O_{2}}$ is primarily based on the Riedl–Pfleiderer process developed nearly 70 years ago,⁶ which involves the sequential hydrogenation and oxidation of anthraquinone. The inherent complexity and high energy consumption of this process promote researchers to explore alternative processes for $\ce{H_{2}O_{2}}$ production.⁷⁻¹¹ In this context, the development of an electrochemical process to partially reduce $\ce{O_{2}}$ to $\ce{H_{2}O_{2}}$ ($\ce{O_{2} + 2H^{+}/e^{-} -> H_{2}O_{2}}$) at the acidic medium would be an attractive strategy, since it can be performed at ambient conditions utilizing renewable solar and wind energies. However, we are still in lack of practical and cost-effective electrocatalysts that exhibit high activity and selectivity for $\ce{H_{2}O_{2}}$ production

Scheme 1 summarizes the pathway for four-electron and two-electron $\ce{O_{2}}$ reductions. To achieve the high catalytic activity, the adsorption of HOO* should be enhanced, while to obtain high selectivity, the adsorption of O* (the product of HOO* dissociation) should be reduced.

![](./images/812730541831880705_2.jpg)

Scheme 1. Reaction pathways along with $O_2$ electroreduction.

To date, numerous materials, such as noble metals,¹²⁻¹⁴ metal alloys¹⁵⁻²¹, and carbon-based materials,²²⁻²⁸ have been proposed to improve the catalytic performance for two-electron $O_2$ electroreduction. Unfortunately, due to the general existence of scaling relations for the adsorption of reaction intermediates (O*, OOH* and OH*),²⁹⁻³⁰ it is a grand challenge to simultaneously achieve high activity and selectivity of the electrocatalysts for $H_2O_2$ production: tuning the binding strength of O* to improve the selectivity towards $H_2O_2$ production is commonly accompanied by changes of OOH* adsorption energy, leading to reduced selectivity.

To simultaneously enhance the activity and selectivity, we need to increase the OOH* binding strength and meanwhile decrease O* adsorption energy, thus the scaling relations have to be broken in some way. Along this line, Siahrostami *et al.* theoretically identified and experimentally demonstrated that Pt-Hg nanoparticles as a promising catalyst for $H_2O_2$ production.³¹ Note that the preferred adsorption sites of O* and OOH* on metal surface are different (hollow site and atop site, respectively), the isolated Pt atoms surrounded by inert Hg atoms can effectively bind OOH* as well as suppress the

adsorption of O*, as reflected by the adsorption energies of OOH* and O* falling below the scaling line of the elemental metal surfaces, and thus achieving the record-high performance: a selectivity of up to 96% and a mass activity of $26 \pm 4$ A $g_{noble metal}^{-1}$ at 50 mV overpotential. Inspired by the great success of this strategy, several bimetallic alloys, such as Pd-Hg and Pd-Au, have been developed, $^{32-33}$ however, the scarcity of noble metals and toxicity of Hg significantly hinder their large-scale applications.

Single-atom catalysts (SACs), e.g., with metal atoms atomically dispersed on two-dimensional (2D) materials, may help provide us a solution to achieve cost-effective, stable, and highly active and selective electrocatalysts for direct $H_2O_2$ production. SACs could offer 100% utilization of metal atoms as active sites. More importantly, the underlying substrate could dramatically modify the electronic structure of supported single atoms, thus altering the activity and selectivity of the active site, $^{34-41}$ and making it possible to break the scaling relations. Though extensive investigations have been devoted into SACs, $^{42-44}$ to our best knowledge, the possible structure-property correlation regarding activity and selectivity of SACs for $H_2O_2$ production has not been examined.

Herein, by means of large-scale density functional theory (DFT) computations, we systematically examined the stability, selectivity, and activity of several experimentally feasible 2D SACs for $H_2O_2$ production at the acidic medium. We screened over 210 SACs and found that 31 SACs can co-balance the selectivity and activity, which could boost the high-performance for two-electron $O_2$ reduction. Remarkably, Zn@Pc-N₄

exhibits the highest activity with an ultralow overpotential of 0.15 V, comparable with previously reported noble metal-based catalysts. Furthermore, combining multi-variable analysis with the machine-learning method, we presented a deep insight into interaction nature of adsorbates on SACs., and demonstrated the intrinsic structure-property correlation of SACs. This work not only identified promising SACs, but also provided a new strategy for discovering and designing high-performance SACs toward direct $\ce{H_{2}O_{2}}$ production.

## 2. COMPUTATIONAL METHODS

Our spin-polarized DFT computations were performed using the Vienna ab initio simulation package (VASP).$^{45}$ The Projector-augmented-wave (PAW) potentials$^{46}$ were employed to represent the electron-ion interactions, and the electron exchange-correlation interactions were treated by PBE functional within the generalized gradient approximation (GGA).$^{47}$ A plane-wave cutoff energy of 400 eV was adopted for all the computations, and the Brillouin zone was sampled using the 3×3×1 and 9×9×1 Monkhorst-Pack $k$-points grids for structure relaxations and electronic structure computations, respectively. To prevent artificial interactions between periodic images, a vacuum space of at least 15 Å was applied in the perpendicular direction of the 2D layer. The convergence threshold for the self-consistent field (SCF) was set at $10^{-5}$ eV for the total energy change and 0.02 eV/Å for the maximum forces on atoms. To describe the van-der-Waals (vdW) interactions between the reactants and the catalyst, we carried out a dispersion correction using DFT-D3 method with the standard parameters

by Grimme and co-workers.⁴⁸ To include the solvation effect, we added a solvation correction to the reaction intermediates, which was estimated to be ~0.3 eV⁴⁹ (for detailed explanations, see Supporting information (SI)).

The changes of Gibbs free energy ($\Delta G$) for each elementary step along the two-electron O₂ partial reduction was evaluated using the computational hydrogen electrode (CHE) model developed by Nørskov and co-workers.⁵⁰ In this model, the chemical potential of the H⁺/e⁻ pair is equal to half of the gas-phase H₂ at standard hydrogen electrode (SHE) conditions, and the electrode potential, $U$ (versus SHE), is taken into account by shifting the electron by $-eU$ when an electron is transferred. The computed electronic energy was converted into Gibbs free energy by adding zero-point energy and entropy contributions, which are estimated by harmonic approximations. For free molecules, the translational, rotational, and vibrational entropy terms were considered, whereas for adsorbates only vibrational entropy was taken into account due to the negligible contributions of the translational and rotational entropies. Since the high-spin ground state of the O₂ molecule is poorly described in DFT computations,⁵¹⁻⁵² all free energies were computed relative to H₂O($l$) and H₂($g$). Moreover, to account for the gas-phase errors encountered with PBE exchange-correlation functionals, the corrections of -0.08, -0.06, and -0.09 eV were added to the electronic energy of H₂, H₂O, and H₂O₂, respectively.⁵³ The excellent agreement between the computed thermodynamic quantities for free H₂, H₂O, and H₂O₂ molecules with the experimental values (Table S1) demonstrates the reliability of our DFT calculations.

## 3. RESULTS AND DISCUSSION

### 3.1. Screening process and catalyst models

To screen SACs suitable for electrochemical synthesis of H₂O₂, we set up three criteria (Scheme 2): a) SACs should have superior thermodynamic and electrochemical stabilities, so that they have good feasibility for experimental realization and are stable in electrochemical environment; b) SACs can selectively stabilize the OOH* and c) destabilize O* intermediates to guarantee the improvement of catalytic activity and selectivity, respectively.

Screening single-atom catalysts

![](./images/812730541831880705_3.jpg)

Scheme 2. Schematic illustration of the discovery and design of SACs for the electrochemical synthesis of H₂O₂.

In this work, we constructed totally 210 SACs models by rationally anchoring a series of single metal atoms on several essential and representative experimentally available substrates (Figure 1): i), the widely studied graphene materials, including defective graphene⁵⁴ and N-doped graphene⁵⁵⁻⁵⁷ (M@C₃, M@C₄, and M@N₄); ii), boron nitride (BN) monolayer (M@N₃),⁵⁸⁻⁶² iii), macrocyclic structures, a kind of two-

dimensional covalent organic frameworks, which have been studied as substrates to anchor single atoms for various reactions, including phthalocyanine-N₄ (M@Pc-N₄),⁶³⁻⁶⁶ pyrphyrin-N₄ (M@Py-N₄),⁶⁷⁻⁶⁸ and porphyrin-N₄ (M@Pr-N₄).⁶⁹⁻⁷² In the next sections, we will examine the stabilities of these SACs and their activities and selectivity towards partial O₂ reduction following our screening strategy.

![](./images/812730541831880705_4.jpg)

Figure 1. (a) Screened metal atoms with their most stable bulk structures. (b) Schematic illustration of all the considered SACs.

### 3.2. Stability of SACs.

To evaluate the thermodynamic and electrochemical stabilities of SACs, we systematically investigated the formation energy ($E_f$) and dissolution potential ($U_{diss}$, versus SHE), which are defined as $E_f = E_{M@SUB} - E_{SUB} - E_M$ and $U_{diss} = U_{diss}^\circ$

$(metal, bulk)-^{E_f}/_{ne}$, respectively, where $E_M$ is the total energy of metal atoms in the most stable bulk structure. $E_{M@SUB}$ and $E_{SUB}$ are the total energies of SAC and substrate, respectively; $U_{diss}^\circ(metal, bulk)$ and $n$ are the standard dissolution potential of bulk metal and the number of electrons involved in the dissolution, respectively. According to the above definitions, a negative $E_f$ (< 0 eV) indicates that it is thermodynamically favorable to form the monoatomic moieties, and the diffusion and aggregation of metal atoms could be suppressed, whereas a more positive $U_{diss}$ relative to the equilibrium potential (> 0.7 V vs. SHE) indicates that the metal atoms on the SAC under examination bind with the substrate strongly enough and the dissolution of metal atoms can be avoided under the electrochemical conditions, thus the SAC is stable in electrochemical environment.⁷³ However, considering that SACs and bulk materials may transfer a different number of electrons in the dissolution process, we used a wider range in $U_{diss}$ (> 0 V) to account for such uncertainties, as most of the experimentally synthesized SACs are within this limit (Figure S1).

Figure 2 shows the $U_{diss}$ of supported metal atoms versus $E_f$ of all the 210 SACs examined in this study (detailed values of $E_f$ and $U_{diss}$ are given in Table S2-3). Following these two stability criteria, the whole figure (coordinate plane) can be divided into four quadrants, which are depicted by blue, yellow, green and purple respectively. Note that a SAC with a negative $E_f$ and a positive $U_{diss}$ is considered as thermodynamically and electrochemically stable. Only SACs fall into the blue region will be considered in the following investigations.

![](./images/812730541831880705_5.jpg)

Figure 2. Dissolution potentials ($U_{diss}$) of metal atoms versus formation energies ($E_f$)
of 210 SACs under investigation.

Generally, compared with the early transition metal atoms (e.g. Sc, Ti, V, Y, Zr, Nb and Hf), those in group 8 to 12 are more likely to be stabilized on the defective site of the substrates under the reaction conditions, as indicated by the more positive $U_{diss}$ values of metal atoms. Particularly, atoms including Fe, Co, Ni, Ru, Rh, Pd, Ir, and Pt display superior thermodynamic and electrochemical stabilities on all the studied substrates, rendering these SACs experimentally feasible. Encouragingly, a series of M@C₃ and M@N₄ moieties, as identified as experimentally feasible targets by our computations, have recently been synthesized.⁷⁴⁻⁷⁵ Thus, the SACs with high thermodynamic and electrochemical stabilities predicted here hold outstanding promise for synthesis.

Moreover, substrates such as BN, Pc-N₄, Py-N₄, Pr-N₄ are demonstrated as good supports to anchor most considered metal atoms. The favorable $E_f$ and $U_{diss}$ values could effectively suppress the dissolution of a metal atom during the O₂ electroreduction process, offering these substrates as the potential hosts for metal atoms.

Our above screening process led to a total of 149 SACs which are expected to be stable under the reaction conditions: 15 SACs for M@C₃, 28 SACs for M@N₃, 14 SACs for M@C₄, 15 SACs for M@g-N₄, 26 SACs for M@Pc-N₄, 23 SACs for M@Py-N₄, and 28 SACs for M@Pr-N₄. In the following investigations, we will only consider the catalytic selectivity and activity of these 149 SACs.

### 3.3. Selectivity of $O_2$ electroreduction on SACs.

The electroreduction of $O_2$ can either produce the desired $H_2O_2$ via the two-electron pathway or $H_2O$ through the four-electron pathway. Since no contiguous active sites are available on SACs surfaces, the O-O bond cleavage is not possible, which excludes the possible dissociative mechanism.⁷⁶ Thus, only associative pathway needs to be considered (Figure 3a).

Apparently, once the $O_2$ molecular is hydrogenated by $H^+/e^-$ pair, the further protonation of $OOH^*$ (or transfer of $H^+/e^-$) can proceed via two reaction pathways: a) $OOH^* + H^+/e^- \rightarrow O^* + H_2O$ ($R1$) or b) $OOH^* + H^+/e^- \rightarrow H_2O_2$ ($R2$). To ensure that a SAC thermodynamically favors $H_2O_2$ formation relative to $H_2O$, the potential barrier for $H_2O_2$ formation ($R2$) should be smaller than that for the hydrogenation of $OOH^*$ to $O^*$ adsorbate and $H_2O$ ($R1$). Consequently, the Gibbs free energy of $O^*$ ($\Delta$G($O^*$)) for a SAC with a high selectivity towards $H_2O_2$ production should be more positive than 3.52 eV ($\Delta$G($H_2O_2$) - $\Delta$G($H_2O$)).

Thus, we computed the $\Delta$G($O^*$) values for all the 149 thermodynamically and electrochemically stable SACs. Figure 3b-h presents the $\Delta$G($O^*$) values versus the group number of metal atoms for these SACs (for detailed values, see Table S4). Note that only the SACs with $\Delta$G($O^*$) lying above the 3.52 eV threshold value prefer the $H_2O_2$ formation ($R2$) rather than the desorption of $H_2O$ ($R1$), thus are selective towards $H_2O_2$ production.

Our computations showed that the Gibbs free energies of $O^*$ intermediate ($\Delta$G($O^*$)) for most of the SACs under investigation are less than 3.52 eV, indicating

their poor selectivity for producing $\text{H}_2\text{O}_2$. Among 149 thermodynamically and electrochemically stable SACs, only 31 SACs meet the selectivity criterion ($\Delta\text{G(O*)} >$ 3.52 eV).

![](./images/812730541831880705_6.jpg)

Figure 3. (a) Schematic illustration of the reactions and the equilibrium potentials during the $\text{O}_2$ electroreduction. (b)-(h) Computed $\Delta\text{G(O*)}$ as a function of the group number of metal atoms. The horizontal dashed line denoted $\Delta\text{G(O*)} = \Delta\text{G(H}_2\text{O}_2\text{)} - \Delta\text{G(H}_2\text{O)} = 3.52$ eV.

Interestingly, two factors were identified that play an essential role in catalytic selectivity of SACs. One important factor affecting the O* binding strength is the number of $d$-electrons of the metal centers. For the SACs with metal atoms in groups 3 to 10, increasing the number of $d$-electrons of metal atoms tends to weaken the interaction between metal atom active site and O*. The increased valence electrons in $d$-orbitals of these metal sites lead to the partially occupied antibonding states of M-O bond below the Fermi level, and thus resulting in the destabilization of O* intermediate.

Another key factor affecting the binding strength of O* intermediate is the coordination environment of metal atoms. Among these 149 SACs, the 3d transition metals (TMs) of Ni, Cu and Zn, 4d TMs of Pd and Ag, and 5d TMs of Pt and Au dispersed on g-N₄, Pc-N₄, Py-N₄, Pr-N₄ present distinguished performance for suppressing the O adsorption, offering a high selectivity towards H₂O₂ production. However, in the M@C₃, M@N₃ and M@C₄ systems, only Bi@C₃, Bi@N₃, Ga@N₃, Cu@C₄, and Bi@C₄ are expected to be selective for two-electron pathway, while the rest of SACs prefer O₂ reduction via a four-electron pathway to H₂O.

Our above procedure finally screened out 31 SACs that meet the selectivity criterion, and their activity for H₂O₂ production will be examined in the subsequent analyses.

### 3.4. Activity of SACs towards H₂O₂ production

In addition to high stability and selectivity, a promising catalyst for electroreduction of O₂ to H₂O₂ should have a small overpotential, or a sizable limiting

potential $(U_L)$ close to the equilibrium potential (0.70 V vs. SHE). The ideal situation is that the Gibbs free energy changes in each elementary step are the same at zero potential so that all reaction free energies can be zero when the electrode potential reaches equilibrium potential. Consequently, the optimal $\Delta$G(OOH*) value is estimated to be 4.22 eV, which can be used as an index to evaluate activity (for detailed understandings, see Figure S2).

To screen out highly active electrocatalyst for $H_2O_2$ production from the 31 SACs which survived our stability and selectivity evaluations, we computed the free energy diagram for $O_2$ reduction to $H_2O_2$ on these SACs (Figure S3). Elementary step with maximum free energy change is defined as the potential-limiting step (PDS) of reaction, and the theoretical limiting potential is determined by $U_L = \Delta G_{PDS}/e$, where $\Delta G_{PDS}$ is the free energy change of PDS. The maximum $U_L$ of 0.70 V corresponds to zero overpotential. Here, the activity and selectivity of $PtHg_4(110)$ were selected as a benchmark for comparison because of its high-performance for two-electron $O_2$ electroreduction ($U_L$=0.46 V, details see Figure S4).$^{31}$

Figure 4a presents the computed $U_L$ of 31 SACs, and the volcano relation between $U_L$ and $\Delta$G(OOH*) is plotted in Figure 4b. Clearly, SACs with $\Delta$G(OOH*) value below 4.22 eV hinders the formation of $H_2O_2$, while weak binding of OOH* ($\Delta$G(OOH*) > 4.22 eV)) leads to the $O_2$ protonation step as the PDS. Remarkably, seven out of the 31 SACs examined here, namely Ag@Pc-$N_4$, Ni@g-$N_4$, Au@Pr-$N_4$, Ni@Py-$N_4$, Au@Py-$N_4$, Zn@Py-$N_4$ and Zn@Pc-$N_4$, display higher activity than the noble metal-based $PtHg_4$ in acid media ($U_L$=0.46 V).$^{31}$ In particular, a noble metal-free

SAC, Zn@Pc-N₄, has the highest activity for H₂O₂ production with $U_L$ of 0.55 V (corresponding to the overpotential of 0.15 V). Note that the Ni@Py-N₄ proposed here was also predicted to have retentively low overpotential for four-electron ORR,⁷⁷ but the selectivity of Ni@Py-N₄ was not fully considered. Moreover, six out of the seven most promising catalysts are macrocyclic structures, demonstrating that macrocyclic structures are of higher-performance than graphene- and BN-based materials examined in this work.

![](./images/812730541831880705_7.jpg)

Figure 4. (a) Computed $U_L$ values of 31 SACs in comparison with the PtHg₄ benchmark ($U_L$=0.46 V). (b) Volcano relation between $U_L$ and ΔG(OOH*) for SACs. (c) Variations of activity versus selectivity for SACs. The PtHg₄(110) was selected as a benchmark for comparison.

Since the thermodynamically predicted activity volcanoes on TMs have been shown to be in close agreement with the kinetic activity volcanoes,⁷⁸ assuming that the kinetic activation barrier is equal to the thermodynamic free energy change of PDS

($\Delta G_{\text{PDS}}$), we can readily compute the rate constant $k$ using the Arrhenius equation using the following equations

$$
\mathrm{k}=A\mathrm{exp}\left(-\Delta G_{PDS}/k_B T\right) \tag{1}
$$

$$
\ln\left(k_{SAC}/k_{PtHg_4}\right)=\left[\Delta G_{PDS}(PtHg_4)-\Delta G_{PDS}(SAC)\right]/k_B T \tag{2}
$$

and the catalytic selectivity can be estimated by the ratio of rate constant $k_{R2}$ and $k_{R1}$, via the equation of (3).

$$
\ln\left(k_{R2}/k_{R1}\right)=\left[\Delta G(O^*)-\Delta G(H_2O_2)\right]/k_B T \tag{3}
$$

Here, $A$ is the pre-exponential factor, $k_B$ is the Boltzmann constant, T is the temperature of 298.15K.

Figure 4c plots the variations of activity versus selectivity for 31 SACs and the PtHg₄(110) benchmark. Promisingly, the values of $\ln(k_{R2}/k_{R1})$ are always positive, indicating that the two-electron reduction of $O_2$ is preferred on these SACs, in other words, these SACs have a good selectivity towards $H_2O_2$ production. Notably, the computed values of $\ln(k_{SAC}/k_{PtHg_4})$ for Ag@Pc-N₄, Ni@g-N₄, Au@Pr-N₄, Ni@Py-N₄, Au@Py-N₄, Zn@Py-N₄, and Zn@Pc-N₄ are 0.88, 1.41, 1.93, 1.95, 2.68, 3.11 and 3.65, respectively. We can estimate that the reaction rate on the Zn@Pc-N₄ surface could be 38 times ($\mathrm{e}^{3.65}$) faster than that of the PtHg₄(110).

To gain a deep insight into the kinetic aspects, we also investigated the energy barrier for the potential-determining step, namely the hydrogenation of $O_2$ species, on Zn-Pc-N₄, Zn-Py-N₄, and Au-Py-N₄ surfaces, since these SACs display the high activity for $H_2O_2$ production. The solvated proton was modelled by a $H_5O_2^+$ near the intermediates, following the recent experimental⁷⁹ and theoretical studies.⁸⁰,⁸¹ A

linearized Poisson-Boltzmann implicit solvation model was used to neutralize the nonzero charge in the simulation, as implemented in VASPsol.⁸² We employed a dielectric constant of 78.5 for water and a Debye length of 3.0 Å to simulate one mole electrolyte solution of monovalent cations. Our computations showed that the solvated proton can spontaneously transfer to the O₂* after full structural optimization (Figure S5), suggesting that the electron-proton transfers to oxygen are very facile. This phenomenon was also observed in the recently studied Fe-N-C system,⁸¹ in which the energy barrier of the OOH* formation on the Fe-N₄ surface is estimated to be only 0.03 eV when using the H₉O₄⁺ as the proton source. It is expected that such kinetic barrier of proton transfer on the selected catalysts may not affect the general tendency based on thermodynamic analysis.

In addition, we also examined the H₂O₂ adsorption on the selected SACs. Our computations showed that the H₂O₂ on the selected catalysts only display weak binding, as indicated by the computed adsorption energies (Eₐds) of -0.13 to -0.41 eV (Figure S6); when taking account of zero-point energy and entropy contributions, the adsorption free energies become positive, indicating the desorption of H₂O₂ on the selected catalysts can easily occur under the room temperature, and further dissociation of the as-formed H₂O₂ to HO* species on the metal active sites could be suppressed.

### 3.5. Origin of activity and selectivity for H₂O₂ production

The origin of activity and selectivity on SACs can be understood by an interplay between ensemble (or geometrical) effects and ligand (or electronic) effects. Essentially, there exists a great difference between SACs and metal surfaces. On a metal surface,

OOH* and O* intermediates normally adsorb on atop sites and hollow sites, respectively. Whereas for a SAC, only atop sites are available for adsorption due to the unique atomic ensemble at the active site. Thereby, the lack of hollow sites on the SAC surface can specifically destabilize O*, while OOH* adsorption can be mostly retained.

Figure 5a illustrates the computed $\Delta\text{G(OOH*)}$ vs. $\Delta\text{G(O*)}$ on the 31 studied SACs as well as a series of different metal surfaces.⁸³ On metal surfaces, $\Delta\text{G(OOH*)}$ and $\Delta\text{G(O*)}$ present a nearly linear scaling relation: increasing catalytic selectivity towards two-electron ORR significantly weakens the adsorption of OOH*, leading to the reduced activity. In contrast, on the SAC surfaces, the adsorption of OOH* can be enhanced in the high selective region ($\Delta\text{G(O*)}$>3.52 eV). The computed $\Delta\text{G(OOH*)}$ of SACs falls below the scaling line of the metal surfaces due to the strong ensemble and ligand effects. This broken scaling relation enables SACs as active and selective catalysts towards $\text{H}_2\text{O}_2$ production.

![](./images/812730541831880705_8.jpg)

Figure 5. (a) Variations of $\Delta\text{G(O}^*)$ and $\Delta\text{G(OOH}^*)$ on the 31 studied SACs. The corrections of -0.02 and 0.17 eV were added to convert the electronic potential into Gibbs free energy for $\text{O}^*$ and $\text{OOH}^*$, respectively (see Figure S7). The weight of four variables in $\text{O}^*$ (b) and $\text{OOH}^*$ (c) adsorption. (d) Scaling relationships between the $\Delta\text{G(O}^*)$ and $B_{M-O}$. (e) Scaling relationships between the $\Delta\text{G(OOH}^*)$ and $C_{OOH^*}$.

Normally, it is difficult to clearly separate the ensemble effects and the ligand effects for $\text{O}^*/\text{OOH}^*$ adsorption, since the interactions between the reaction intermediates and SACs involve some different stochastic distributions of multi-variable. Here, we proposed a general strategy to identify the key properties for adsorption using multiple linear regression method as described in equation (4),

$$
\begin{bmatrix}
\Delta G_{i}^{1} \\
\vdots \\
\Delta G_{i}^{n}
\end{bmatrix}
=
\begin{bmatrix}
\varepsilon_{d/p}^{1} & C_{M}^{1} & C_{i}^{1} & B_{M-i}^{1} \\
\vdots & \vdots & \vdots & \vdots \\
\varepsilon_{d/p}^{n} & C_{M}^{n} & C_{i}^{n} & B_{M-i}^{n}
\end{bmatrix}
\begin{bmatrix}
A \\
B \\
C \\
D
\end{bmatrix} + E
\tag{4}
$$

where $\Delta G_{i}^{n}$ is Gibbs free energy of O*/OOH* intermediate, $\varepsilon_{d/p}$ is the band center of metal atom: *the p*-band center was used for Al, Ga, Sn, and Bi because of the existence of partially filled *p*-orbital for these atoms, while the *d*-band center was used for the other metal atoms. $C_{M}$ and $C_{i}$ are the net charge of metal atom and O*/OOH*, respectively. $B_{M-i}$ is the bond population between the metal site and O*/OOH*. A, B, C, and D are coefficients, and E is the constant due to the ensemble effects of SACs (Further computational details are given in SI and Table S5-9). Simply, $\varepsilon_{d/p}$ and $C_{M}$ represent the intrinsic electronic properties of the active site, while $C_{i}$ and $B_{M-i}$ denote the bonding characteristics between the metal atom and adsorbate. In principle, the different adsorption behaviors of adsorbates can be divided into (1) interactions due to the band hybridization, which can be characterized by $\varepsilon_{d/p}$ and $B_{M-i}$, and (2) interactions mostly related to the charge transfer, which can quantified by $C_{M}$ and $C_{i}$.

Using eq. (4), we can readily define the weight of these four variables in O*/OOH* adsorption (Figure 5b-c). Interestingly, the adsorption of O* and OOH* intermediates on SACs surfaces, which we refer as adsorption-induced surface interactions, exhibits different interaction patterns.

For O* adsorption, the energy levels of partially filled metal orbital (*d* or *p* orbital) and *O-2p* orbital are well matched, leading to the partial occupation of the bonding orbitals. The strong band hybridization increases the bond population ($B_{M-O}$) between

the metal atom and O*, which enhances the M-O interaction. Accordingly, the contribution of the above properties towards increasing the $\Delta$G(O*) follows the order of $B_{M-O}>C_{O^*}>C_{M}>\varepsilon_{d/p}$. Note that the $\varepsilon_{d/p}$ presents a poor correlation with the $\Delta$G(O*) (Figure S8), implying that the band center model is ineffective in describing the adsorption energies for SACs. This derivation could be ascribed to the strong spin effects (Figure S9 and Table S10). After O* adsorption, the $B_{M-O}$ shows a clear spin splitting between the $\alpha$ and $\beta$ orbitals. The strong spin polarization provides large exchange stabilization energy for the $\alpha$ spin orbitals, shifting the $\alpha$ spin orbitals to lower energy levels, and thus less interaction of $\alpha$ spin orbitals is observed.

For OOH* adsorption (Figure 5c), the contribution of the above properties for enhancing the binding strength of OOH* has the following order: $C_{OOH^*}>C_{M}>B_{M-OOH}\approx\varepsilon_{d/p}$. In this case, the charge transfer between the OOH* and SACs plays an essential role in OOH* adsorption, while the band hybridization has a small contribution. Moreover, different from the O* adsorption, there exist some correlations between the $C_{M}$ and the $C_{OOH^*}$, which indicates that the metal site can be considered as an electron donor, and the electrons can transfer from the metal atom to the adsorbed OOH*. The different weights between $C_{M}$ and $C_{OOH^*}$ in OOH* adsorption can be attributed to the contributions of the substrate.

During the $O_2$ reduction process, the substrate can serve as an electron reservoir. Once the $O_2$ molecule is protonated by $H^+/e^-$ pair, the underlying substrate acts as an electron donor and provides electrons to the OOH*, favoring the OOH* adsorption. Thus, even for SACs with the same M@$N_4$ moiety, their catalytic activities may vary

to a significant degree. For example, with the same $Au@N_4$ moiety, the $U_L$ values for $Au@Pc-N_4$, $Au@Py-N_4$, and $Au@Pr-N_4$ are 0.42, 0.53 and 0.51 V, respectively.

Overall, using multiple linear regression method and multiple-variable analysis, we presented a deep insight into interaction nature of adsorbates on SACs. Interestingly, since the bond population $B_{M-O}$ and the net charge of $OOH^*$ $C_{OOH^*}$ exert an enormous function on $O^*$ and $OOH^*$ adsorptions, respectively, approximately a linear correction exists between $B_{M-O}$ and $\Delta$G(O*), and between $C_{OOH^*}$ and $\Delta$G (OOH*) (Figure 5d-e). In detail, the SACs under examination can be divided into two categories depending on occupation of these $p$-orbitals. For TMs (in group 3 to 12) with fully filled $p$-orbitals, the Gibbs free energy shows a clear correlation with $B_{M-O}$ and $C_{OOH^*}$, with adjusted $R^2$ of 0.87 and 0.82, respectively, implying the important role of band hybridization and charge transfer in $O^*/OOH^*$ adsorption. However, for Al, Ga, and Bi atoms with partially filled $p$-orbitals, the Gibbs free energy deviates from the linear relation, which would be associated primarily with the $p$-states of metal atoms. As shown in Figure S10, the computed partial density of states (PDOS) suggest that the states of Al, Ga, and Bi near the Fermi level are mainly contributed by the $p$-orbitals, while the $d$-states have small contributions. The interaction of the $2p$-O states with a broad distribution of $p$-states will give rise to the formation bonding states below the Fermi level (Figure S11), leading to the partially occupied bonding states of adsorbates. Accordingly, the binding strength can vary continuously as the surface electronic structure changes, and the Al, Ga, Bi atoms display the different adsorption behaviors compared to the TMs. Especially, since the $Zn-Pc-N_4$ can provide the moderate charge

transfer and band hybridization for the adsorption of the OOH* and O* relative to the PtHg₄ (110), respectively (Figure 6), the possible activity and selectivity of two-electron ORR can be significantly improved.

![](./images/812730541831880705_9.jpg)

Figure 6. (a) Charge density difference, (b) PDOS, and (c) COHP plots for O*/OOH* adsorbed on the Zn-Pc-N₄ and PtHg₄(110) surfaces.

### 3.6. Identifying the intrinsic structure-selectivity correlation

As shown in our screening procedure, screening out the ORR catalysts with high selectivity towards two-electron partial reduction is the key step. Since the catalytic selectivity is significantly affected by the binding strength of O*, it is essential to identify the intrinsic correlation between structure and $\Delta$G(O*). So far, several theoretical models have been proposed to correlate the adsorption energy of reaction intermediates (i.e., OOH* and OH*) with different properties of catalysts.³⁰,⁷⁷,⁸⁴ However, most of them are valid for a specific type of substrate doped with transitional

metals, while general correlations between $\Delta\mathrm{G(O^*)}$ and the intrinsic properties of the catalysts for all these three typical materials with both transitional metals and main group elements are still elusive.

Thus, we utilized the machine-learning models to explore the correction between $\Delta\mathrm{G(O^*)}$ and intrinsic descriptors of the 149 experimentally feasible SAC catalysts (obtained in Section 3.2). A feature set with eight intrinsic descriptors are selected (Table S11), which includes the adjusted electron numbers of $d/p$ orbital ($\mathrm{e}_{dp}$), the oxide formation enthalpy $(H_{f.ox}),^{85}$ electronegativity $(N_m)$, electron affinity $(A_m)$ and first ionization energy $(I_m)$ of central atoms, number of coordinated $\mathrm{N}$ atom $(N_n)$, the sum of the electronegativity of neighboring $\mathrm{C}$ and $\mathrm{N}$ atoms $(SN_m)$, the distance ratio ($R_d$, which is calculated by $R_d = D_d/2D_e$, where $D_d$ is the distance between the central atom and the hole center of materials, $D_e$ is the distance between the central atom and the hole edges).

Note that in our ML model, adjusted $d/p$ electron numbers are used. For early transitional metals (Sc, Ti, Y, and Hf) and main group elements (Al, Ga, Sn and Bi), all the electrons from the valence orbitals to the second outer $d/p$ orbitals are counted ($\mathrm{e}_{dp}$), while for the other elements, $\mathrm{e}_{dp}$ is the number of valence electrons of $d$ orbitals. The distance ratio is used to describe the void coverage of base materials. The first five descriptors ($\mathrm{e}_{dp}$, $H_{f.ox}$, $N_m$, $A_m$, and $I_m$) are the chemical properties of central atoms, while the others $(N_n,\ \ SN_m,\ \ R_d)$ are descriptors for the chemical environment. Through these eight descriptors, we can depict the underlying patent of the intrinsic descriptors and the catalysis performance of single-atom electrocatalysts.

The random forest algorithm⁸⁶⁻⁸⁷ as implanted in scikit-learn⁸⁸ were employed for the optimal model. Random forests provide accurate predictions in many applications through averaging more than hundreds of decision trees trained by randomly selected samples. Cross validations were carried out for each training process with test sample sizes around 20%. The max depth was set as 5 and the number of trees modeled was 200. The random forest model exhibits excellent performance, with a train score of 0.95 and a test score of 0.92. The predicted $\Delta$G(O*) agrees well with our DFT results with adjusted R² of 0.95 (Figure 7a), which suggests the applicability of the machine- learning method to external data points.

Furthermore, we compared the importance of eight intrinsic descriptors, which encode the insight into chemical properties in adsorption ability (Figure 7b). We found that the interfacial binding is primarily associated with the readily available physical properties of metal atoms, namely $H_{f.ox}$ and $e_{dp}$, with feature importance of 0.59 and 0.20, respectively, while the other six descriptors have relatively low feature importance. Especially, since the $H_{f.ox}$ reflects the oxophilicity of metal atoms, metals with a weaker affinity for oxygen, such as Ag, Au, and Pd, can significantly reduce band hybridization between the metal and oxygen, and thus result in the improved selectivity toward the production of H₂O₂. This helps to explain why these metals are commonly used in two-electron ORR electrocatalysts, which consistent with our electronic structure analysis (Section 3.5). We conclude that the machine-learning method is very helpful for establishing the intrinsic structure-property correlation, and

thus accelerating the discovery of more efficient SACs toward two-electron $\ce{O_{2}}$ electroreduction.

![](./images/812730541831880705_10.jpg)

Figure 7. (a) Comparison between DFT and predicted $\Delta$G(O*) values, where both training and testing data points are presented. (b) Feature importance of random forest model for $\Delta$G(O*).

## CONCLUSIONS

In summary, we presented a comprehensive understanding of the application of experimentally available single-atom electrocatalysts for $\ce{H_{2}O_{2}}$ production, on the basis of spin-polarized DFT computation and thermodynamic analysis. We demonstrated that a total of 31 SACs could not only enhance the adsorption of OOH* but also suppress the adsorption of O* relative to metal surfaces, which result in the high selectivity for $\ce{H_{2}O_{2}}$ production. Promisingly, the single Zn atom centered phthalocyanine (Zn@Pc-$\ce{N_{4}}$) displayed an outstanding activity with an ultralow overpotential of 0.15 V, comparable with reported $\ce{PtHg_{4}}$ catalysts. Meanwhile, the high thermodynamic and electrochemical stabilities of metal atoms can effectively avoid aggregation and dissolution, rendering the Zn@Pc-$\ce{N_{4}}$ as a distinguished electrocatalyst for two-electron

O₂ reduction. Furthermore, by applying multiple-variable analysis with the machine- learning method, we shed light on the underlying origin of the selectivity and activity of SACs for adsorption-induced surface interactions, which includes the M-O band hybridization, and charge transfer between SAC and OOH* intermediate, and presented a general strategy to identify the intrinsic correlation between the readily available physical properties of metal atoms (e.g. oxide formation energy) and catalytic selectivity of SACs (both transitional and main group metals) in three types of representative substrates. We believe this work will be helpful in guiding the design and discovery for stable and efficient SACs towards direct H₂O₂ production.

## ASSOCIATED CONTENT

### Supporting Information
Explanation of solvation correction and bond population; PBE-corrections, zero-point energies, entropies used in the construction of reaction free energies throughout the paper; detailed values related in the figures; formation energy versus dissolution potential of experimentally reported SACs; free energy diagram for two-electron ORR on ideal electrocatalyst, SACs, and Pt₁Hg₄(110) surface; initial and final configurations of solvated proton transfer to O₂*; H₂O₂ adsorption on the selected SACs; Scaling relations of E(O*) vs. G(O*), and E(OOH*) vs. G(OOH*); band center of metal atom versus Gibbs free energy of O* on SACs. bond populations of α and β orbitals for O* adsorption; PDOS of SACs; COHP of O* adsorption.

## AUTHOR INFORMATION

### Corresponding Author
* <zhongfangchen@gmail.com> (ZC)

* zhangslvip@njust.edu.cn (SZ)

* huangsp@mail.buct.edu.cn (SH)

ORCID

Zhongfang Chen: 0000-0002-1445-9184

Shengli Zhang: 0000-0003-4981-231X

Xiangyu Guo: 0000-0001-5102-2910

Shiru Lin: 0000-0002-0159-2269

Jinxing Gu: 0000-0003-4805-7017

Notes

The authors declare no competing financial interest.

ACKNOWLEDGMENTS

This work is supported in China by the National Natural Science Foundation of China (Grant No. 21776004), the Fundamental Research Funds for the Central Universities (No. 30916015106) and in USA by the National Science Foundation-Centers of Research Excellence in Science and Technology (NSF-CREST Center) for Innovation, Research and Education in Environmental Nanotechnology (CIRE2N) (Grant No. HRD-1736093). A portion of the calculations used the resources of the Compute and Data Environment for Science (CADES) at ORNL and of the National Energy Research Scientific Computing Center, which are supported by the Office of Science of the U.S. DOE under Contract No. DE-AC05-00OR22750 and DE-AC02-05CH11231, respectively.

## REFERENCES

1.  Martínez-Huitle, C. A.; Ferro, S. Electrochemical Oxidation of Organic Pollutants for the Wastewater Treatment: Direct and Indirect Processes. *Chem. Soc. Rev.* **2006**, 35, 1324-1340.

2.  Brillas, E.; Sirés, I.; Oturan, M. A. Electro-Fenton Process and Related Electrochemical Technologies Based on Fenton's Reaction Chemistry. *Chem. Rev.* **2009**, 109, 6570-6631.

3.  Hage, R.; Lienke, A., Applications of Transition-Metal Catalysts to Textile and Wood-Pulp Bleaching. *Angew. Chem. Int. Ed.* **2006**, 45, 206-222.

4.  Enache, D. I.; Edwards, J. K.; Landon, P.; Solsona-Espriu, B.; Carley, A. F.; Herzing, A. A.; Watanabe, M.; Kiely, C. J.; Knight, D. W.; Hutchings, G. J. Solvent-Free Oxidation of Primary Alcohols to Aldehydes Using Au-Pd/TiO₂ Catalysts. *Science* **2006**, 311, 362-365.

5.  Fukuzumi, S.; Yamada, Y.; Karlin, K. D. Hydrogen Peroxide as a Sustainable Energy Carrier: Electrocatalytic Production of Hydrogen Peroxide and the Fuel Cell. *Electrochim. Acta* **2012**, 82, 493-511.

6.  Hans-Joachim, R.; Georg, P. Production of Hydrogen Peroxide. U.S. Patent 2, 215, 883, Sep 24, 1940.

7.  Campos-Martin, J. M.; Blanco-Brieva, G.; Fierro, J. L. G. Hydrogen Peroxide Synthesis: An Outlook beyond the Anthraquinone Process. *Angew. Chem. Int. Ed.* **2006**, 45, 6962-6984.

8. Jiang, Y.; Ni, P.; Chen, C.; Lu, Y.; Yang, P.; Kong, B.; Fisher, A.; Wang, X. Selective Electrochemical $\text{H}_2\text{O}_2$ Production through Two-Electron Oxygen Electrochemistry. *Adv. Energy Mater.* **2018**, *8*, 1801909-1801933.

9. Yang, S.; Verdaguer-Casadevall, A.; Arnarson, L.; Silvioli, L.; Čolić, V.; Frydendal, R.; Rossmeisl, J.; Chorkendorff, I.; Stephens, I. E. L. Toward the Decentralized Electrochemical Production of $\text{H}_2\text{O}_2$: A Focus on the Catalysis. *ACS Catal.* **2018**, *8*, 4064-4081.

10. Perry, S. C.; Pangotra, D.; Vieira, L.; Csepei, L. I.; Sieber, V.; Wang, L.; Ponce de León, C.; Walsh, F. C. Electrochemical Synthesis of Hydrogen Peroxide from Water and Oxygen. *Nat. Rev. Chem.* **2019**, *3*, 442-458.

11. Shi, X.; Siahrostami, S.; Li, G.-L.; Zhang, Y.; Chakthranont, P.; Studt, F.; Jaramillo, T. F.; Zheng, X.; Nørskov, J. K. Understanding Activity Trends in Electrochemical Water Oxidation to form Hydrogen Peroxide. *Nat. Commun.* **2017**, *8*, 701-706.

12. Gervasini, A.; Carniti, P.; Desmedt, F.; Miquel, P. Liquid Phase Direct Synthesis of $\text{H}_2\text{O}_2$: Activity and Selectivity of Pd-Dispersed Phase on Acidic Niobia-Silica Supports. *ACS Catal.* **2017**, *7*, 4741-4752.

13. Arrigo, R.; Schuster, M. E.; Abate, S.; Giorgianni, G.; Centi, G.; Perathoner, S.; Wrabetz, S.; Pfeifer, V.; Antonietti, M.; Schlögl, R. Pd Supported on Carbon Nitride Boosts the Direct Hydrogen Peroxide Synthesis. *ACS Catal.* **2016**, *6*, 6959-6966.

14. Hu, B.; Deng, W.; Li, R.; Zhang, Q.; Wang, Y.; Delplanque-Janssens, F.; Paul, D.; Desmedt, F.; Miquel, P. Carbon-Supported Palladium Catalysts for the Direct

Synthesis of Hydrogen Peroxide from Hydrogen and Oxygen. *J. Catal.* **2014**, *319*, 15-26.

15. Edwards, J. K.; Solsona, B.; N, E. N.; Carley, A. F.; Herzing, A. A.; Kiely, C. J.; Hutchings, G. J. Switching Off Hydrogen Peroxide Hydrogenation in the Direct Synthesis Process. *Science* **2009**, *323*, 1037-1041.

16. Edwards, J. K.; Ntainjua N, E.; Carley, A. F.; Herzing, A. A.; Kiely, C. J.; Hutchings, G. J. Direct Synthesis of $\ce{H_{2}O_{2}}$ from $\ce{H_{2}}$ and $\ce{O_{2}}$ over Gold, Palladium, and Gold-Palladium Catalysts Supported on Acid-Pretreated $\ce{TiO_{2}}$. *Angew. Chem. Int. Ed.* **2009**, *48*, 8512-8515.

17. Li, F.; Shao, Q.; Hu, M.; Chen, Y.; Huang, X. Hollow Pd-Sn Nanocrystals for Efficient Direct $\ce{H_{2}O_{2}}$ Synthesis: The Critical Role of Sn on Structure Evolution and Catalytic Performance. *ACS Catal.* **2018**, *8*, 3418-3423.

18. Xu, J.; Ouyang, L.; Da, G. J.; Song, Q. Q.; Yang, X. J.; Han, Y. F. Pt Promotional Effects on Pd-Pt Alloy Catalysts for Hydrogen Peroxide Synthesis Directly from Hydrogen and Oxygen. *J. Catal.* **2012**, *285*, 74-82.

19. Zheng, Z.; Ng, Y. H.; Wang, D. W.; Amal, R. Epitaxial Growth of Au-Pt-Ni Nanorods for Direct High Selectivity $\ce{H_{2}O_{2}}$ Production. *Adv. Mater.* **2016**, *28*, 9949-9955.

20. Freakley, S. J.; He, Q.; Harrhy, J. H.; Lu, L.; Crole, D. A.; Morgan, D. J.; Ntainjua, E. N.; Edwards, J. K.; Carley, A. F.; Borisevich, A. Y.; Kiely, C. J.; Hutchings, G. J. Palladium-Tin Catalysts for the Direct Synthesis of $\ce{H_{2}O_{2}}$ with High Selectivity. *Science* **2016**, *351*, 965-968.

21. Jirkovský, J. S.; Panas, I.; Ahlberg, E.; Halasa, M.; Romani, S.; Schiffrin, D. J. Single Atom Hot-Spots at Au-Pd Nanoalloys for Electrocatalytic $\ce{H_{2}O_{2}}$ Production. *J. Am. Chem. Soc.* **2011**, *133*, 19432-19441.

22. Kim, H. W.; Ross, M. B.; Kornienko, N.; Zhang, L.; Guo, J.; Yang, P.; McCloskey, B. D. Efficient Hydrogen Peroxide Generation using Reduced Graphene Oxide-based Oxygen Reduction Electrocatalysts. *Nat. Catal.* **2018**, *1*, 282-290.

23. Lu, Z.; Chen, G.; Siahrostami, S.; Chen, Z.; Liu, K.; Xie, J.; Liao, L.; Wu, T.; Lin, D.; Liu, Y.; Jaramillo, T. F.; Nørskov, J. K.; Cui, Y. High-efficiency Oxygen Reduction to Hydrogen Peroxide Catalysed by Oxidized Carbon Materials. *Nat. Catal.* **2018**, *1*, 156-162.

24. Chai, G. L.; Hou, Z.; Shu, D. J.; Ikeda, T.; Terakura, K. Active Sites and Mechanisms for Oxygen Reduction Reaction on Nitrogen-Doped Carbon Alloy Catalysts: Stone-Wales Defect and Curvature Effect. *J. Am. Chem. Soc.* **2014**, *136*, 13629-13640.

25. Bukas, V. J.; Kim, H. W.; Sengpiel, R.; Knudsen, K.; Voss, J.; McCloskey, B. D.; Luntz, A. C. Combining Experiment and Theory to Unravel the Mechanism of Two-Electron Oxygen Reduction at a Selective and Active Co-catalyst. *ACS Catal.* **2018**, 11940-11951.

26. Li, M.; Zhang, L.; Xu, Q.; Niu, J.; Xia, Z. N-Doped Graphene as Catalysts for Oxygen Reduction and Oxygen Evolution Reactions: Theoretical Considerations. *J. Catal.* **2014**, *314*, 66-72.

27. Chen, S.; Chen, Z.; Siahrostami, S.; Higgins, D.; Nordlund, D.; Sokaras, D.; Kim, T. R.; Liu, Y.; Yan, X.; Nilsson, E.; Sinclair, R.; Nørskov, J. K.; Jaramillo, T. F.; Bao, Z. Designing Boron Nitride Islands in Carbon Materials for Efficient Electrochemical Synthesis of Hydrogen Peroxide. *J. Am. Chem. Soc.* **2018**, *140*, 7851-7859.

28. Lin, C. Y.; Zhang, L.; Zhao, Z.; Xia, Z. Design Principles for Covalent Organic Frameworks as Efficient Electrocatalysts in Clean Energy Conversion and Green Oxidizer Production. *Adv. Mater.* **2017**, *29*, 1606635-1606641.

29. Man, I. C.; Su, H. Y.; Calle-Vallejo, F.; Hansen, H. A.; Martínez, J. I.; Inoglu, N. G.; Kitchin, J.; Jaramillo, T. F.; Nørskov, J. K.; Rossmeisl, J. Universality in Oxygen Evolution Electrocatalysis on Oxide Surfaces. *ChemCatChem* **2011**, *3*, 1159-1165.

30. Viswanathan, V.; Hansen, H. A.; Rossmeisl, J.; Nørskov, J. K. Universality in Oxygen Reduction Electrocatalysis on Metal Surfaces. *ACS Catal.* **2012**, *2*, 1654-1660.

31. Siahrostami, S.; Verdaguer-Casadevall, A.; Karamad, M.; Deiana, D.; Malacrida, P.; Wickman, B.; Escudero-Escribano, M.; Paoli, E. A.; Frydendal, R.; Hansen, T. W.; Chorkendorff, I.; Stephens, I. E. L.; Rossmeisl, J. Enabling Direct H₂O₂ Production through Rational Electrocatalyst Design. *Nat. Mater.* **2013**, *12*, 1137-1143.

32. Verdaguer-Casadevall, A.; Deiana, D.; Karamad, M.; Siahrostami, S.; Malacrida, P.; Hansen, T. W.; Rossmeisl, J.; Chorkendorff, I.; Stephens, I. E. L. Trends in the

Electrochemical Synthesis of $\mathrm{H_2O_2}$: Enhancing Activity and Selectivity by Electrocatalytic Site Engineering. *Nano Lett.* **2014**, *14*, 1603-1608.

33. Wilson, N. M.; Priyadarshini, P.; Kunz, S.; Flaherty, D. W. Direct Synthesis of $\mathrm{H_2O_2}$ on Pd and $\mathrm{Au_xPd_1}$ Clusters: Understanding the Effects of Alloying Pd with Au. *J. Catal.* **2018**, *357*, 163-175.

34. Choi, C. H.; Kim, M.; Kwon, H. C.; Cho, S. J.; Yun, S.; Kim, H. T.; Mayrhofer, K. J. J.; Kim, H.; Choi, M. Tuning Selectivity of Electrochemical Reactions by Atomically Dispersed Platinum Catalyst. *Nat. Commun.* **2016**, *7*, 10922-10930.

35. Sahoo, S. K.; Ye, Y.; Lee, S.; Park, J.; Lee, H.; Lee, J.; Han, J. W. Rational Design of TiC-Supported Single Atom Electrocatalysts for Hydrogen Evolution and Selective Oxygen Reduction Reactions. *ACS Energy Lett.* **2019**, *4*, 126-132.

36. Yang, S.; Kim, J.; Tak, Y. J.; Soon, A.; Lee, H. Single-Atom Catalyst of Platinum Supported on Titanium Nitride for Selective Electrochemical Reactions. *Angew. Chem. Int. Ed.* **2015**, *55*, 2058-2062.

37. Sun, Y.; Silvioli, L.; Sahraie, N. R.; Ju, W.; Li, J.; Zitolo, A.; Li, S.; Bagger, A.; Arnarson, L.; Wang, X.; Moeller, T.; Bernsmeier, D.; Rossmeisl, J.; Jaouen, F.; Strasser, P. Activity-Selectivity Trends in the Electrochemical Production of Hydrogen Peroxide over Single-Site Metal-Nitrogen-Carbon Catalysts. *J. Am. Chem. Soc.* **2019**, *141*, 12372-12381.

38. Yang, S.; Tak, Y. J.; Kim, J.; Soon, A.; Lee, H. Support Effects in Single-Atom Platinum Catalysts for Electrochemical Oxygen Reduction. *ACS Catal.* **2017**, *7*, 1301-1307.

39. Li, B. Q.; Zhao, C. X.; Liu, J. N.; Zhang, Q. Electrosynthesis of Hydrogen Peroxide Synergistically Catalyzed by Atomic Co-$N_x$-C Sites and Oxygen Functional Groups in Noble-Metal-Free Electrocatalysts. *Adv. Mater.* **2019**, 1808173-1808180.

40. Jiang, K.; Back, S.; Akey, A. J.; Xia, C.; Hu, Y.; Liang, W.; Schaak, D.; Stavitski, E.; Nørskov, J. K.; Siahrostami, S.; Wang, H. Highly Selective Oxygen Reduction to Hydrogen Peroxide on Transition Metal Single Atom Coordination. *Nat. Commun.* 2019, 10, 3997-4007.

41. Shen, R.; Chen, W.; Peng, Q.; Lu, S.; Zheng, L.; Cao, X.; Wang, Y.; Zhu, W.; Zhang, J.; Zhuang, Z.; Chen, C.; Wang, D.; Li, Y. High-Concentration Single Atomic Pt Sites on Hollow $CuS_x$ for Selective $O_2$ Reduction to $H_2O_2$ in Acid Solution. *Chem* **2019**, 5, 1-12.

42. Chen, Y.; Ji, S.; Chen, C.; Peng, Q.; Wang, D.; Li, Y. Single-Atom Catalysts: Synthetic Strategies and Electrochemical Applications. *Joule* **2018**, 2, 1242-1264.

43. Zhang, H.; Liu, G.; Shi, L.; Ye, J. Single-Atom Catalysts: Emerging Multifunctional Materials in Heterogeneous Catalysis. *Adv. Energy Mater.* **2017**, 8, 1701343-1701366.

44. Wang, A.; Li, J.; Zhang, T. Heterogeneous Single-Atom Catalysis. *Nat. Rev. Chem.* **2018**, 2, 65-81.

45. Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations using a Plane-Wave Basis Set. *Phys. Rev. B* **1996**, 54, 11169-11186.

46. Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. *Phys. Rev. B* **1999**, *59*, 1758-1775.

47. Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 3865-3868.

48. Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A Consistent and Accurate Ab Initio Parametrization of Density Functional Dispersion Correction (DFT-D) for the 94 Elements H-Pu. *J. Chem. Phys.* **2010**, *132*, 154104.

49. Calle-Vallejo, F.; Martínez, J. I.; Rossmeisl, J. Density Functional Studies of Functionalized Graphitic Materials with Late Transition Metals for Oxygen Reduction Reactions. *Phys. Chem. Chem. Phys.* **2011**, *13*, 15639-15643.

50. Nørskov, J. K.; Rossmeisl, J.; Logadottir, A.; Lindqvist, L.; Kitchin, J. R.; Bligaard, T.; Jónsson, H. Origin of the Overpotential for Oxygen Reduction at a Fuel-Cell Cathode. *J. Phys. Chem. B* **2004**, *108*, 17886-17892.

51. Jones, R. O.; Gunnarsson, O. The Density Functional Formalism, Its Applications and Prospects. *Rev. Mod. Phys.* **1989**, *61*, 689-746.

52. Kurth, S.; Perdew, J. P.; Blaha, P. Molecular and Solid-State Tests of Density Functional Approximations: LSD, GGAs, and Meta-GGAs. *Int. J. Quantum Chem.* **1999**, *75*, 889-909.

53. Peterson, A. A.; Abild-Pedersen, F.; Studt, F.; Rossmeisl, J.; Nørskov, J. K. How Copper Catalyzes the Electroreduction of Carbon Dioxide into Hydrocarbon Fuels. *Energy Environ. Sci.* **2010**, *3*, 1311-1315.

54. Wang, H.; Wang, Q.; Cheng, Y.; Li, K.; Yao, Y.; Zhang, Q.; Dong, C.; Wang, P.; Schwingenschlögl, U.; Yang, W.; Zhang, X. X. Doping Monolayer Graphene with Single Atom Substitutions. *Nano Lett.* **2012**, *12*, 141-144.

55. Wang, J.; Li, Z.; Wu, Y.; Li, Y. Fabrication of Single-Atom Catalysts with Precise Structure and High Metal Loading. *Adv. Mater.* **2018**, *30*, 1801649-1801653.

56. Peng, Y.; Lu, B.; Chen, S. Carbon-Supported Single Atom Catalysts for Electrochemical Energy Conversion and Storage. *Adv. Mater.* **2018**, *30*, 1801995-1802019.

57. Park, J.; Nabae, Y.; Hayakawa, T.; Kakimoto, M. A. Highly Selective Two-Electron Oxygen Reduction Catalyzed by Mesoporous Nitrogen-Doped Carbon. *ACS Catal.* **2014**, *4*, 3749-3754.

58. Zhao, J.; Chen, Z. Single Mo Atom Supported on Defective Boron Nitride Monolayer as an Efficient Electrocatalyst for Nitrogen Fixation: A Computational Study. *J. Am. Chem. Soc.* **2017**, *139*, 12480-12487.

59. Sun, W.; Meng, Y.; Fu, Q.; Wang, F.; Wang, G.; Gao, W.; Huang, X.; Lu, F. High-Yield Production of Boron Nitride Nanosheets and Its Uses as a Catalyst Support for Hydrogenation of Nitroaromatics. *ACS Appl. Mater. Inter.* **2016**, *8*, 9881-9888.

60. Tan, X.; Tahini, H. A.; Arandiyan, H.; Smith, S. C. Electrocatalytic Reduction of Carbon Dioxide to Methane on Single Transition Metal Atoms Supported on a Defective Boron Nitride Monolayer: First Principle Study. *Adv. Theory Simul.* **2019**, *2*, 1800094.

61. Grant, J. T.; Carrero, C. A.; Goeltl, F.; Venegas, J.; Mueller, P.; Burt, S. P.; Specht, S. E.; McDermott, W. P.; Chieregato, A.; Hermans, I. Selective Oxidative Dehydrogenation of Propane to Propene using Boron Nitride Catalysts. *Science* **2016**, 354, 1570.

62. Tian, J.; Tan, J.; Xu, M.; Zhang, Z.; Wan, S.; Wang, S.; Lin, J.; Wang, Y. Propane Oxidative Dehydrogenation over Highly Selective Hexagonal Boron Nitride Catalysts: The Role of Oxidative Coupling of Methyl. *Sci. Adv.* **2019**, 5, 8063-8068.

63. Zhang, Z.; Xiao, J.; Chen, X.-J.; Yu, S.; Yu, L.; Si, R.; Wang, Y.; Wang, S.; Meng, X.; Wang, Y.; Tian, Z. Q.; Deng, D. Reaction Mechanisms of Well-Defined Metal-N₄ Sites in Electrocatalytic CO₂ Reduction. *Angew. Chem. Int. Ed.* **2018**, 57, 16339-16342.

64. Liu, Y.; McCrory, C. C. L. Modulating the Mechanism of Electrocatalytic CO₂ Reduction by Cobalt Phthalocyanine through Polymer Coordination and Encapsulation. *Nat. Commun.* **2019**, 10, 1683-1692.

65. Han, N.; Wang, Y.; Ma, L.; Wen, J.; Li, J.; Zheng, H.; Nie, K.; Wang, X.; Zhao, F.; Li, Y.; Fan, J.; Zhong, J.; Wu, T.; Miller, D. J.; Lu, J.; Lee, S. T.; Li, Y. Supported Cobalt Polyphthalocyanine for High-Performance Electrocatalytic CO₂ Reduction. *Chem* **2017**, 3, 652-664.

66. Silva, F. L.; Reis, R. M.; Barros, W. R. P.; Rocha, R. S.; Lanza, M. R. V. Electrogeneration of Hydrogen Peroxide in Gas Diffusion Electrodes: Application of Iron (II) Phthalocyanine as a Modifier of Carbon Black. *J. Electroanal. Chem.* **2014**, 722, 32-37.

67. Mette, G.; Sutter, D.; Gurdal, Y.; Schnidrig, S.; Probst, B.; Iannuzzi, M.; Hutter, J.; Alberto, R.; Osterwalder, J. From Porphyrins to Pyrphyrins: Adsorption Study and Metalation of a Molecular Catalyst on Au(111). *Nanoscale* **2016**, 8, 7958-7968.

68. Gurdal, Y.; Hutter, J.; Iannuzzi, M. Insight into (Co)Pyrphyrin Adsorption on Au(111): Effects of Herringbone Reconstruction and Dynamics of Metalation. *J. Phys. Chem. C* **2017**, 121, 11416-11427.

69. Micheroni, D.; Lan, G.; Lin, W. Efficient Electrocatalytic Proton Reduction with Carbon Nanotube-Supported Metal-Organic Frameworks. *J. Am. Chem. Soc.* **2018**, 140, 15591-15595.

70. Guo, J.; Li, Y.; Cheng, Y.; Dai, L.; Xiang, Z. Highly Efficient Oxygen Reduction Reaction Electrocatalysts Synthesized under Nanospace Confinement of Metal-Organic Framework. *ACS Nano* **2017**, 11, 8379-8386.

71. Zuo, Q.; Liu, T.; Chen, C.; Ji, Y.; Gong, X.; Mai, Y.; Zhou, Y. Ultrathin Metal-Organic Framework Nanosheets with Ultrahigh Loading of Single Pt Atoms for Efficient Visible-Light-Driven Photocatalytic $\mathrm{H_2}$ Evolution. *Angew. Chem. Int. Ed.* **2019**, 131, 10304-10309.

72. Yamanaka, I.; Ichihashi, R.; Iwasaki, T.; Nishimura, N.; Murayama, T.; Ueda, W.; Takenaka, S. Electrocatalysis of Heat-Treated Cobalt-Porphyrin/Carbon for Hydrogen Peroxide Formation. *Electrochim. Acta* **2013**, 108, 321-329.

73. Greeley, J.; Nørskov, J. K. Electrochemical Dissolution of Surface Alloys in Acids: Thermodynamic Trends from First-Principles Calculations. *Electrochim. Acta* **2007**, 52, 5829-5836.

74. Fei, H.; Dong, J.; Feng, Y.; Allen, C. S.; Wan, C.; Volosskiy, B.; Li, M.; Zhao, Z.; Wang, Y.; Sun, H.; An, P.; Chen, W.; Guo, Z.; Lee, C.; Chen, D.; Shakir, I.; Liu, M.; Hu, T.; Li, Y.; Kirkland, A. I.; Duan, X.; Huang, Y. General Synthesis and Definitive Structural Identification of $MN_4C_4$ Single-Atom Catalysts with Tunable Electrocatalytic Activities. *Nat. Catal.* **2018**, *1*, 63-72.

75. Fei, H.; Dong, J.; Wan, C.; Zhao, Z.; Xu, X.; Lin, Z.; Wang, Y.; Liu, H.; Zang, K.; Luo, J.; Zhao, S.; Hu, W.; Yan, W.; Shakir, I.; Huang, Y.; Duan, X. Microwave-Assisted Rapid Synthesis of Graphene-Supported Single Atomic Metals. *Adv. Mater.* **2018**, *30*, 1802146-1802153.

76. Kulkarni, A.; Siahrostami, S.; Patel, A.; Nørskov, J. K. Understanding Catalytic Activity Trends in the Oxygen Reduction Reaction. *Chem. Rev.* **2018**, *118*, 2302-2312.

77. Xu, H.; Cheng, D.; Cao, D.; Zeng, X. C., A Universal Principle for a Rational Design of Single-Atom Electrocatalysts. *Nat. Catal.* **2018**, 1, 339-348.

78. Seh, Z. W.; Kibsgaard, J.; Dickens, C. F.; Chorkendorff, I.; Nørskov, J. K.; Jaramillo, T. F. Combining Theory and Experiment in Electrocatalysis: Insights into Materials Design. *Science* **2017**, *355*, 4998-5009.

79. Stoyanov, E. S.; Stoyanova, I. V.; Reed, C. A. The Structure of the Hydrogen Ion ($\text{H}_{\text{aq}}^{+}$) in Water. *J. Am. Chem. Soc.* **2010**, *132*, 1484-1485.

80. Chang, K.; Zhang, H.; Chen, J. G.; Lu, Q.; Cheng, M. J. Constant Electrode Potential Quantum Mechanical Study of $\text{CO}_2$ Electrochemical Reduction Catalyzed by N-Doped Graphene. *ACS Catal.* **2019**, *9*, 8197-8207.

81. Wang, Y.; Tang, Y. J.; Zhou, K. Self-Adjusting Activity Induced by Intrinsic Reaction Intermediate in Fe-N-C Single-Atom Catalysts. *J. Am. Chem. Soc.* **2019**, 141, 14115-14119.

82. Fishman, M.; Zhuang, H. L.; Mathew, K.; Dirschka, W.; Hennig, R. G. Accuracy of Exchange-Correlation Functionals and Effect of Solvation on the Surface Energy of Copper. *Phys. Rev. B* **2013**, 87, 245402.

83. Rossmeisl, J.; Logadottir, A.; Nørskov, J. K. Electrolysis of Water on (Oxidized) Metal Surfaces. *Chem. Phys.* **2005**, 319, 178-184.

84. Dickens, C. F.; Montoya, J. H.; Kulkarni, A. R.; Bajdich, M.; Nørskov, J. K. An Electronic Structure Descriptor for Oxygen Reactivity at Metal and Metal-Oxide Surfaces. *Surf. Sci.* **2019**, 681, 122-129.

85. O'Connor, N. J.; Jonayat, A. S. M.; Janik, M. J.; Senftle, T. P. Interaction Trends between Single Metal Atoms and Oxide Supports Identified with Density Functional Theory and Statistical Learning. *Nat. Catal.* **2018**, 1, 531-539.

86. Liaw A, Wiener M. Classification and Regression by RandomForest, *J. R news* **2002**, 2, 18-22.

87. Díaz-Uriarte, R.; De Andres, S. A. Gene Selection and Classification of Microarray Data using Random Forest. *BMC Bioinformatics* **2006**, 7, 3-15.

88. Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V. Scikit-learn: Machine Learning in Python. *J. Mach. Learn. Res.* **2011**, 12, 2825-2830.

Table of contents (TOC)

![](./images/812730541831880705_11.jpg)