# Catalytic activity of PtCu intermetallic compound for CO oxidation: A theoretical insight

Javier Amaya Suárez, José J. Plata, Antonio M. Márquez, Javier Fdez. Sanz *

Departamento de Química Física, Facultad de Química, Universidad de Sevilla, 41012, Sevilla, Spain

---

## ARTICLE INFO

**Keywords:**
Platinum
Copper
CO oxidation
Intermetallic
DFT

---

## ABSTRACT

To understand the microscopic mechanism of the CO oxidation reaction at PtCu nanoparticles, which have unique geometric and electronic structures compared to their component metals, we present here a theoretical study, based on density functional theory calculations, of the main reaction steps of this reaction. We examine the $O_2$ dissociation, the CO adsorption and the CO + $O_2$ reaction at an atomic level and use the computed geometries, Bader charges, and vibrational frequencies to rationalize the role of the intermetallic nanoparticles surface structure on the experimentally observed much higher activity of these nanoparticles as catalysts of the preferential oxidation of CO. By comparing with clean Pt (111) surface and with different Cu-doped models of this same surface, our results show that, at the surface, the presence of Cu induces the segregation of CO molecules at Pt sites and of $O_2$ molecules at Cu sites. Contrarily to Pt surfaces, the unassisted $O_2$ dissociation has a high barrier at the intermetallic nanoparticle surface and proceeds through a CO-assisted mechanism in which the new CO bond is formed while the O—O bond is broken with a kinetic barrier much lower than on either Pt (111) or in Pt-doped surfaces. The particular structure of the intermetallic surface is shown to have a significant role in the low kinetic barrier for the reaction, allowing for an easy approach of the CO to the adsorbed $O_2$ molecule that permits an early transition state with a low energetic barrier.

---

## 1. Introduction

The heterogeneously catalysed reaction of CO with $O_2$ is a key step in catalysis. A critical application is its implication in the use of Pt-based catalysts in a variety of industrial processes [1,2]. The production of hydrogen, the control of exhaust emissions, and the electrochemical cell reactions are well-known reactions that employ Pt as a catalyst [3–6]. All these processes have a serious deficiency related to the strong adsorption of CO on Pt surfaces that blocks the active sites at the catalyst surface, hampering the reaction instead of improving it [7–9]. Pt catalysts, thus, becomes efficient when the CO coverage is reduced and adsorption and dissociation of $O_2$ can take place. This limits the application of Pt-based catalysts to temperatures exceeding 400 K. Due to its technological relevance, the CO oxidation reaction continues to be studied [10–16], especially to achieve CO oxidation at lower temperatures [17,18]. As both CO and $O_2$ should be adsorbed at the surface of the catalyst, the structure of the surface plays an important role in controlling the catalyst reactivity. In this direction, Pt-catalysts can be modified by contact with active oxides, like $CeO_2$ [19], or by alloying with other metals [20–23].

The use of intermetallic compounds (IMCs) has revealed a promising pathway to improve the catalytic properties of their constituents [24]. IMC are compounds with two or more distinct metal atoms that may have a crystal structure different from that of the isolated metal elements. For instance, some IMCs have been found more selective for partial hydrogenation reactions [25–27] and the addition of a secondary element to Pt has produced bimetallic catalysts that showed higher activity toward CO oxidation at lower temperatures than those of supported Pt nanoparticles [28–33]. In this regard, several studies [32,-34] have shown that supported PtCu IMC nanoparticles were more active than $Pt/SiO_2$ or $Pt/Al_2O_3$ for the preferential oxidation of CO (PROX) in the highest CO conversion: around 80 % at temperatures above 413 K while $Pt/SiO_2$ resulted in aprox. 20 % conversion at 453 K and much smaller at lower temperatures. Regarding selectivity, in presence of excess $H_2$, $CO_2$ selectivity of the $PtCu/SiO_2$ catalyst was found to be similar to that of $Pt/SiO_2$. Based on their results, Komatsu et al. [32,34]

---

* Corresponding author.
E-mail address: sanz@us.es (J. Fdez. Sanz).

https://doi.org/10.1016/j.cattod.2020.12.007
Received 31 July 2020; Received in revised form 3 November 2020; Accepted 14 December 2020
0920-5861/© 2020 Elsevier B.V. All rights reserved.

Please cite this article as: Javier Amaya Suárez, *Catalysis Today*, https://doi.org/10.1016/j.cattod.2020.12.007

suggested that the addition of Cu facilitates the adsorption of $O_2$ and weakens the CO-surface bond. They also propose that the CO oxidation occurs at the nanoparticle/support interface at the experimental conditions, with CO preferentially adsorbing at Pt atoms and $O_2$ molecules at Cu atoms. However, the role of the IMC surface structure, and its influence at the atomic scale, on the CO oxidation reaction mechanism have not been addressed.

Recently, Gómez et al. [35] reported the purification of hydrogen through CO preferential oxidation using $PtCu/Al_2O_3$ structured catalysts. The catalysts consisted of cordierite monoliths and alumina foams covered by aggregates of 2-5 $\mu$m of $PtCu/Al_2O_3$ that filled the substrate cavities. The role of both Pt and Cu metals in the intermetallic $Pt_xCu_y/\gamma$-$Al_2O_3$ catalysts in the PROX reaction has also been examined in detail by Castillo et al. [36] using a variety of structural characterization techniques.

In this work we present a comprehensive theoretical study, by employing density functional theory (DFT) methods, of the microscopic mechanism of the $CO + O_2$ reaction at the PtCu IMC (012) surface. For the sake of completeness, we examine the characteristics of the same reaction mechanism at the clean Pt (111) surface and in two models of Cu-doped Pt (111) surface. After presenting the necessary computational and model details, we start by considering the $O_2$ dissociation barrier on all surfaces and found that the introduction of Cu increases the barrier for $O_2$ dissociation relative to that on Pt (111). Next, we check out the CO adsorption. While the interaction with Pt sites at the IMC surface is even stronger than in the clean Pt (111) surface, Cu sites show a much lower bonding energy with CO. Finally, we obtain the energetic barrier for the reaction of CO with an adsorbed $O_2$ molecule and analyse the differences in the geometric and electronic structure induced by the structure of the IMC surface that result in a much lower energetic barrier in this surface. On the other hand, although we exclusively focus on the CO oxidation catalyzed by the Pt-Cu IMC surfaces, we assume that our conclusions can be extrapolated to the CO-PROX process as the effects of hydrogen on the optimized structures and computed activation barriers are expected to be small.

## 2. Computational details and models

DFT spin-polarized calculations were performed within the VASP code [37-39] using the projector augmented wave (PAW) method. The electronic states were expanded in a plane-wave basis set with a cut-off energy of 400 eV [40,41] which ensures adequate convergence of energetic and structural parameters with respect to basis set size. Exchange-correlation energies were computed using the approximation proposed by Perdew, Burke and Ernzerhof (PBE) [42] based on the generalized gradient approximation (GGA) and considering three-dimensional periodic boundary conditions (PBC). Bulk cell parameters where optimized for Pt ($a = 2.792$ Å) and PtCu ($a = b = 2.728$ Å, $c = 12.534$ Å). All atoms were fully relaxed during the geometry optimizations until forces were below $0.02$ eV/Å. The Brillouin zone was sampled using a Monkhorst-Pack scheme with a gamma-centered $4 \times 4 \times 1$ k-points grid [43]. Further increase in the density of the k-points grid showed no improvement on the computed energies below $10^{-3}$ eV. Transition states were computed using the climbing-image nudged elastic band method with 5 intermediate images [44]. Bader charges were computed using the algorithm of Henkelman et al [45-47].

The surfaces were modelled using a $4 \times 4$ slab with 4 atomic layers of thickness and a vacuum of 11 Å (Fig. 1). Four different slabs were modelled in order to analyse the influence of the presence of copper on the CO oxidation. The first model contains 64 Pt atoms and represents a clean Pt (111) surface (Fig. 1a,b). The PtCu-1 model contains 63 Pt and 1 Cu atom on the surface which represents a copper concentration of $1.5$ % in total and $6.3$ % on surface (Fig. 1c,d). PtCu-4 model contains 60 Pt and 4 Cu surface atoms, this ratio accounts for a Cu concentration of $6.3$ % in total and a $25$ % on the surface (Fig. 1e,f).

The PtCu IMC crystal structure belongs to the $R \overline{3}m$ space group with its unit cell containing 3 atoms of both Cu and Pt [48]. Experimental X-ray diffraction (XRD) data [34] shows that PtCu nanoparticles are truly intermetallic rather than alloy. They have a Kurnarov-type structure and their XRD diagrams present two peaks associated to the (012) and (104) planes, being the former the most intense. Thus, we represent the IMC as a stack of Cu and Pt planes that result in a structure of alternating rows of Cu and Pt atoms at the (012) surface. Our slab model contains, thus, 32 Pt and 32 Cu atoms with a $50$ % of Cu on the surface (Fig. 1g,h) representing the most stable (012) surface.

## 3. Results and discussion

This section is focused on the study of the adsorption and reactivity of both $O_2$ and CO molecules on the selected slab models. We discuss the $O_2$ adsorption and dissociation along with the CO adsorption and oxidation analysing the energetics, geometries and charge transfer between the key atoms. Influence of the copper atoms in these properties is carefully evaluated.

### 3.1. $O_2$ dissociation

Molecular oxygen adsorbs preferentially nearly parallel to the surface on a top-hollow-bridge configuration at a fcc-hollow site with hcp-hollow sites being higher in energy by about 0.26 eV and other configurations like top/bridge about 1.6-2.0 eV higher than the fcc-hollow and unstable towards either hcp or fcc sites. For the isolated oxygen atom, the preferred adsorption site is the fcc-hollow, with the hcp-hollow being calculated with our setup about 0.4 eV higher in energy. The $O_2$ dissociation is exothermic on the Pt (111) surface by $-1.6$ eV and by about -2.1 eV on the surfaces containing Cu, including the (012) surface

![](./images/812519797974630401_1.jpg)

Fig. 1. Top and side view of the slab models: (a,b) Pt (111), (c,d) PtCu-1 (111), (e,f) PtCu-4 (111) and (g,h) PtCu IMC (012) surfaces. Colors: Pt, gray and Cu, ochre.

of the IMC system. Results for the Pt (111) surface are in agreement with previous studies of the interaction of molecular and atomic oxygen with the clean Pt surface [49,50]. Here we will focus our study on the effect of the presence of surface Cu atoms on the $O_2$ dissociation barrier when the $O_2$ molecule is adsorbed at a fcc-hollow site that includes, at least, one Cu atom. Energy barriers (in eV) for the $O_2$ dissociation, Bader charge analysis for relevant atoms, and O-O distance (in Å) on the transition state (TS), are presented in Table 1 for the models examined in this work. In all cases, the dissociation to oxygen atoms on fcc and hcp sites has been examined, following the ideas presented in a recent paper that shows that this is the path with the lowest barrier [51].

The barrier for $O_2$ dissociation on the Pt (111) surface is computed as 0.23 eV, similar to previous results [49,50,52]. However, when at least one Cu atom is present at the $O_2$ adsorption site, the barrier significantly increases to about 0.9-1.0 eV, increasing with surface Cu content. At Pt-only surface sites of the PtCu-1 and PtCu-4 models the computed energy barrier is comparable to the value obtained on the clean Pt (111) surface. These results show that the presence of Cu basically blocks the $O_2$ dissociation explaining the experimental results of Komatsu et al. [34] that found the $^{16}O_2$-$^{18}O_2$ exchange reaction did not proceed at temperatures below 473 K on PtCu IMC nanoparticles. This is explained by the high kinetic barrier imposed by the presence of Cu atoms that, in the case of the IMC (012) surface, should always be involved in the reaction. The reason for this higher energy barrier can be understood by looking at structural details of the TS, also presented in Table 1. The configuration of the TS corresponds to one O atom at the initial fcc site while the second O atom moves to a position atop one surface Pt (see Fig. 2) or Cu atom.

If we examine the computed Bader charges of the atoms involved in the TS we can see that we have a highly ionic system. There is a charge transfer from the surface to the $O_2$ molecule, about 0.7-0.8 $e^-$ in the initial state, that reaches 1.1 $e^-$ on the TS at the Pt (111) surface and further increases to 1.2-1.3 $e^-$ on the Cu containing surfaces. The O-O distance is high, 2.0 Å on the Pt (111) surface, as consequence of the electrostatic repulsion of the two negatively charged O atoms. This repulsion increases on the Cu-containing surfaces, as the electron transfer increases. Consequently, the O-O distance increases and, thus, the TS is less stable on these Cu-containing surfaces. The fact that both the electron transfer and the O-O distance is about the same on the Cu- surfaces indicates that the effect is local, and that a single Cu atom is enough to block the $O_2$ dissociation at a given surface hollow site.

### 3.2. CO adsorption

The strength and mechanism of the CO interaction with transition metal surfaces is well known after many years of both experimental and theoretical work. On the Pt (111) surface, experimental data clearly indicate a preference for on top adsorption with an interaction energy of about 1.4-1.5 eV [9,53]. In striking contrast, DFT based theoretical calculations predict a stronger adsorption at the fcc hollow site and, in general, show a tendency to overbind [54]. Although this is the case for the PBE functional used in this work, we want to focus our study on the comparative effects that the addition of Cu to Pt and, eventually, the formation of the IMC structure has on the adsorption and reactivity of CO towards oxygen. Experimental data by different authors [55,56] show that surface diffusion of CO on Pt (111) is very slow with a kinetic barrier of about 0.54 eV, essentially coverage and temperature independent. Thus, we can safely ignore the influence of surface CO diffusion on the present study.

![](./images/812519797974630401_2.jpg)

Fig. 2. TS geometry for the $O_2$ dissociation on the PtCu-4 (111) surface. Colors: Pt, gray; Cu, ochre; and O, red.

As shown by the interaction energies displayed in Table 2, surfa- ce-CO bond is stronger at Pt sites and increases in Cu-containing sur- faces. This increase is CO-surface bond energy can be related to the surface-to-CO charge transfer that takes place. The Bader charge computed for the surface Pt atom decreases (is less positive) with increasing surface Cu content while, at the same time, the electron density transferred to the CO $\pi^*$ bond increases (the CO is more negatively charged). As a consequence, the C-O bond weakens as can be confirmed by the decreasing CO vibrational frequency. The red shift of the CO vibrational frequency on the IMC surface, compared to the CO vibrational frequency on the Pt (111) surface ($\sim24\ \text{cm}^{-1}$) agrees reasonably well with the experimentally observed red shift ($\sim37\ \text{cm}^{-1}$) although it is lower in magnitude. The Cu-CO interaction energies are much weaker and increase with Cu content on the Pt (111) surface to decrease to its lower value at the IMC (012) surface. The charge transferred from the surface to the CO molecule is lower in all Cu sites than in Pt sites, resulting in the observed lower Cu-CO bond energies and in a lower red shift of the CO vibrational frequency. A Redhead analysis [57] using a preexponential factor of $10^{13}\text{s}^{-1}$, that corresponds to the computed vibrational frequency of $\sim400-500\ \text{cm}^{-1}$ for the metal C-O bond, allow us to estimate a desorption temperature of about 650 K on Pt sites of the IMC (012) surface while at the Cu sites it is only about 200 K. Although the desorption temperature on Pt sites is clearly overestimated compared to experimental data that indicate nearly total CO desorption at $\sim623$ K [34], the difference with Cu sites is high enough to warrant that at usual operation temperatures CO molecules will occupy only Pt sites and that Cu sites will be empty and available for the adsorption of the $O_2$ molecule.

### 3.3. CO reaction with $O_2$

Two different mechanisms can be responsible for the CO oxidation at metal surfaces: direct reaction with O adatoms or reaction with an adsorbed $O_2$ molecule that dissociates at the same time. Regarding the

<table>
<caption>Table 1<br>Activation barrier ($\Delta E^{\ddagger}$), Bader charges for surface atoms at the hollow site and O-O distance on the transition state structure for $O_2$ dissociation over the different surface models.</caption>
<thead>
<tr>
<th>Model</th>
<th>$\Delta E^{\ddagger}$ (eV)</th>
<th>$q_{Pt}$</th>
<th>$q_{Cu}$</th>
<th>$q_{O_2}$</th>
<th>$d_{O-O}$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pt (111)</td>
<td>0.23</td>
<td>0.43, 0.28</td>
<td>--</td>
<td>--1.13</td>
<td>2.04</td>
</tr>
<tr>
<td>PtCu-1 (111)</td>
<td>0.88</td>
<td>0.29</td>
<td>0.65</td>
<td>--1.22</td>
<td>2.21</td>
</tr>
<tr>
<td>PtCu-4 (111)</td>
<td>0.92</td>
<td>0.36</td>
<td>0.60, 0.57</td>
<td>--1.30</td>
<td>2.26</td>
</tr>
<tr>
<td>IMC (012)</td>
<td>0.98</td>
<td>0.13</td>
<td>0.56, 0.54</td>
<td>--1.26</td>
<td>2.14</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2<br>CO adsorption energies ($\Delta E$), Bader charges for CO and surface metal atom and CO vibrational frequency.</caption>
<thead>
<tr>
<th>Model</th>
<th colspan="4">on top-Pt</th>
</tr>
<tr>
<th></th>
<th>$\Delta E$ (eV)</th>
<th>$q_{Pt}$</th>
<th>$q_{CO}$</th>
<th>$\nu_{CO}$ ($\text{cm}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pt (111)</td>
<td>1.78</td>
<td>0.227</td>
<td>--0.123</td>
<td>2054</td>
</tr>
<tr>
<td>PtCu-1 (111)</td>
<td>1.84</td>
<td>0.180</td>
<td>--0.126</td>
<td>2049</td>
</tr>
<tr>
<td>PtCu-4 (111)</td>
<td>1.90</td>
<td>0.119</td>
<td>--0.143</td>
<td>2040</td>
</tr>
<tr>
<td>IMC (012)</td>
<td>1.85</td>
<td>--0.058</td>
<td>--0.173</td>
<td>2030</td>
</tr>
<tr>
<th></th>
<th colspan="4">on top-Cu</th>
</tr>
<tr>
<th></th>
<th>$\Delta E$ (eV)</th>
<th>$q_{Pt}$</th>
<th>$q_{CO}$</th>
<th>$\nu_{CO}$ ($\text{cm}^{-1}$)</th>
</tr>
<tr>
<td>PtCu-1 (111)</td>
<td>0.68</td>
<td>0.530</td>
<td>--0.083</td>
<td>2066</td>
</tr>
<tr>
<td>PtCu-4 (111)</td>
<td>0.83</td>
<td>0.505</td>
<td>--0.125</td>
<td>2061</td>
</tr>
<tr>
<td>IMC (012)</td>
<td>0.62</td>
<td>0.471</td>
<td>--0.120</td>
<td>2051</td>
</tr>
</tbody>
</table>

possibility of direct reaction with O adatoms we have already discussed that $O_2$ dissociation has a high kinetic barrier in Cu containing surfaces, thus, we don't expect to find O adatoms near Cu sites on these surfaces. Moreover, the barrier for direct reaction between the CO molecule and one isolated O adatom is quite high: 1.58 eV on the Pt (111) surface and 1.24-1.59 eV on Cu containing surfaces. Thus, we can discard this path for the CO oxidation on all surfaces. The alternative path is the attack of the CO molecule to a surface $O_2$ molecule forming a new C—O bond and, at the same time, activating the dissociation of the $O_2$ molecule. Results on **Table 3** for the kinetic barrier for this path show that, while this barrier is still high for the Pt, PtCu-1, and PtCu-4 (111) surfaces (1.68 eV, 1.78 eV, and 1.49 eV, respectively) it is significantly reduced on the IMC (012) surface to a value of 0.50 eV. **Fig. 3** presents as a summary the energy profile for the two reaction mechanisms on the Pt (111) and IMC (012) surfaces.

The reasons behind this much lower kinetic barrier on this surface can be understood looking at the geometric parameters of the transition state structure also displayed on **Table 3**.

At all surfaces the O—O distance is quite large, 1.912.12 Å, except at the IMC (012) surface where it is much shorter, 1.81 Å. At the same time, the new C—O bond length is much longer at the Pt, PtCu-1, and PtCu-4 surfaces (1.931.99 Å) than at the IMC (012) surface (1.75 Å). These data indicate that at the IMC (012) surface the transition state structure has a more formed C—O bond while simultaneously there is some more O-O bond remaining than in the Pt (111) derived surfaces, even when some Cu is present. These geometric changes can be related to the presence of the second row of Cu atoms at the IMC (012) surface interacting with the CO molecule (see **Fig. 4**). The bond distance with this Cu atom is 2.75 Å while it is much shorter when this atom is Pt (2.37-2.50 Å) despite the bigger atomic radius of the Pt atom. This indicates that there is some repulsive interaction between the Cu atom of the IMC (012) surface, that bears a Bader charge of +0.35 and the C atom that also shows a positive Bader charge of +2.06. This effect pushes the C atom towards the $O_2$ molecule, facilitating the formation of the new C—O bond. At all the other surfaces, when this is a Pt atom, its Bader charge is only slightly positive (+0.02 to +0.05) and the CO molecule stays closer to this surface atom.

### 4. Conclusions
In this work, we examined and analysed, from a theoretical point of view, the role of Cu on PtCu intermetallic surfaces in the activity of these surfaces towards the CO oxidation reaction. Two possible reaction paths have been investigated (see **Fig. 5**): *a)* a two-step mechanism where first the $O_2$ molecule dissociates at the surface and in a second step the surface O adatoms react with the adsorbed CO molecule and *b)* a single step mechanism where the $O_2$ dissociation is assisted by the simultaneous reaction with the CO molecule. On the clean Pt (111) surface (**Fig. 4**, top) the dissociation of the $O_2$ molecule is easy, with an energetic barrier of only 0.23 eV. However, the reactions of CO with either O adatoms or adsorbed $O_2$ molecules both have high kinetic barriers (1.58 eV and 1.68 eV, respectively). On the Cu containing surfaces (**Fig. 4**, bottom) the barrier for $O_2$ dissociation is, on the contrary, high at Cu sites (0.88-0.98 eV) while it still low at Pt-only sites (0.23-0.26 eV). However, as these sites are not available at the IMC (012) surface, the $O_2$ dissociation will be hampered at this surface. Reaction between the CO and $O_2$ molecules still present a high barrier at the PtCu-1 and PtCu-4 surfaces (1.78 eV and 1.49 eV) but it is strongly reduced at the IMC (012) surface down to 0.50 eV. This reduced reaction barrier has been related to the particular structure of the IMC (012) surface. While the CO molecule adsorbs at Pt sites, the Cu atoms remain free and are preferential adsorption sites for the $O_2$ molecule. The positive charge of the Cu surface atoms, compared to the nearly neutral Pt, pushes the CO molecule toward the adsorbed $O_2$ molecule, favouring the formation of an early C—O bond without requiring the full dissociation of the O—O bond at the transition state.

<table>
<caption>Table 3
CO + $O_2$ reaction energetic barrier, O—O distance, new CO— bond distance, C-surface metal atoms bond distances, and Bader charge for surface M atom (see Fig. 3) at the transition state geometry.</caption>
<thead>
<tr>
<th>Model</th>
<th>$\Delta E^{\ddagger}$ (eV)</th>
<th>$d_{O-O}$ (Å)</th>
<th>$d_{C-O}$ (Å)</th>
<th>$d_{C-M}$ (Å)</th>
<th>$q_M$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pt (111)</td>
<td>1.68</td>
<td>2.12</td>
<td>1.93</td>
<td>2.37</td>
<td>+0.02</td>
</tr>
<tr>
<td>PtCu-1 (111)</td>
<td>1.78</td>
<td>1.91</td>
<td>1.92</td>
<td>2.49</td>
<td>+0.05</td>
</tr>
<tr>
<td>PtCu-4 (111)</td>
<td>1.48</td>
<td>1.92</td>
<td>1.99</td>
<td>2.50</td>
<td>+0.05</td>
</tr>
<tr>
<td>IMC (012)</td>
<td>0.50</td>
<td>1.81</td>
<td>1.75</td>
<td>2.75</td>
<td>+0.35</td>
</tr>
</tbody>
</table>

![](./images/812519797974630401_3.jpg)

Fig. 3. Energy profiles for the CO oxidation reaction on Pt (111) surface (top) and on IMC surface (bottom). On each profile the dotted line separates the two mechanisms: reaction with O adatoms (right) and reaction with adsorbed $O_2$ molecule (left). Energies for transition states and products of each step are presented relative to the reactant.

![](./images/812519797974630401_4.jpg)

Fig. 4. Transition state geometry for the CO + $O_2$ oxidation on PtCu IMC (012) surface. Colors: Pt, gray; Cu, ochre; C, black; O, red.

### CRediT authorship contribution statement
**Javier Amaya Suárez**: Investigation, Data curation. **José J. Plata**: Methodology, Validation. **Antonio M. Márquez**: Formal analysis, Writing - original draft. **Javier Fdez. Sanz**: Writing - review & editing.

![](./images/812519797974630401_5.jpg)

Fig. 5. Schematic representation of the proposed mechanisms for CO oxidation reaction on Pt, PtCu-X and Pt-Cu IMC. Energy barrier values expressed in eV. Values in parentheses indicate the energy barrier when Cu atoms are involved.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This work was funded by the Ministerio de Ciencia e Innovación, grant PID2019-106871GB-I00, and the Junta de Andalucía, grant US-1381410, co-financed by FEDER funds from the European Union. The authors thankfully acknowledge the computer resources allocated by the Red Española de Supercomputación at the Lusitania node, and the technical support provided by Cenits.

## References

[1] G. Ertl, H. Knözinger, F. Schüth, J. Weitkamp, Handbook of Heterogeneous Catalysis, 2nd ed., 2008. New York.

[2] G.A. Somorjai, Y. Li, Introduction to Surface Chemistry and Catalysis, Wiley, 2010.

[3] H. Igarashi, H. Uchida, M. Suzuki, Y. Sasaki, M. Watanabe, Removal of carbon monoxide from hydrogen-rich fuels by selective oxidation over platinum catalyst supported on zeolite, Appl. Catal. A Gen. 159 (1997) 159-169, https://doi.org/10.1016/S0926-860X(97)00075-6.

[4] R.M. Heck, R.J. Farrauto, Automobile exhaust catalysts, Appl. Catal. A Gen. 221 (2001) 443-457, https://doi.org/10.1016/S0926-860X(01)00818-3.

[5] S.K. Das, A. Reis, K.J. Berry, Experimental evaluation of CO poisoning on the performance of a high temperature proton exchange membrane fuel cell, J. Power Sources 193 (2009) 691-698, https://doi.org/10.1016/j.jpowsour.2009.04.021.

[6] J. Wu, H. Yang, Platinum-based oxygen reduction electrocatalysts, Acc. Chem. Res. 46 (2013) 1848-1857, https://doi.org/10.1021/ar300359w.

[7] H. Hopster, H. Ibach, Adsorption of CO on Pt(111) and Pt 6(111) × (111) studied by high resolution electron energy loss spectroscopy and thermal desorption spectroscopy, Surf. Sci. 77 (1978) 109-117.

[8] D.F. Ogletree, M.A. Van Hove, G.A. Somorjai, LEED intensity analysis of the structures of clean Pt(111) and of CO adsorbed on Pt(111) in the (c4 × 2) arrangement, Surf. Sci. 173 (1986) 351-365, https://doi.org/10.1016/0039-6028(86)90195-0.

[9] G. Ertl, M. Neumann, K.M. Streit, Chemisorption of CO on the Pt(111) surface, Surf. Sci. 64 (1977) 393-410, https://doi.org/10.1016/0039-6028(77)90052-8.

[10] J. Wintterlin, S. Völkening, T.V.W. Janssens, T. Zambelli, G. Ertl, Atomic and macroscopic reaction rates of a surface-catalyzed reaction, Science 278 (1997) 1931-1934, https://doi.org/10.1126/science.278.5345.1931.

[11] A. Alavi, P. Hu, T. Deutsch, P.L. Silvestrelli, J. Hutter, CO oxidation on Pt(111): an Ab initio density functional theory study, Phys. Rev. Lett. 80 (1998) 3650-3653, https://doi.org/10.1103/PhysRevLett.80.3650.

[12] A.D. Allian, K. Takanabe, K.L. Fujdala, X. Hao, T.J. Truex, J. Cai, C. Buda, M. Neurock, E. Iglesia, Chemisorption of CO and mechanism of CO oxidation on supported platinum nanoclusters, J. Am. Chem. Soc. 133 (2011) 4498-4517, https://doi.org/10.1021/ja110073u.

[13] R.M. Arán-Ais, F.J. Vidal-Iglesias, M.J.S. Farias, J. Solla-Gullón, V. Montiel, E. Herrero, J.M. Feliu, Understanding CO oxidation reaction on platinum nanoparticles, J. Electroanal. Chem. 793 (2017) 126-136, https://doi.org/10.1016/j.jelechem.2016.09.031.

[14] B.V. L'Vov, A.K. Galwey, Catalytic oxidation of CO on platinum: thermochemical approach, J. Therm. Anal. Calorim. 111 (2013) 145-154, https://doi.org/10.1007/s10973-012-2241-6.

[15] J. Kim, M.C. Noh, W.H. Doh, J.Y. Park, In situ observation of competitive CO and O₂ adsorption on the Pt(111) surface using near-ambient pressure scanning tunneling microscopy, J. Phys. Chem. C. 122 (2018) 6246-6254, https://doi.org/10.1021/acs.jpcc.8b01672.

[16] D. Vogel, C. Spiel, Y. Suchorski, A. Trinchero, R. Schlögl, H. Grönbeck, G. Rupprechter, Local catalytic ignition during CO oxidation on low-index Pt and Pd surfaces: a combined PEEM, MS, and DFT study, Angew. Chemie Int. Ed. 51 (2012) 10041-10044, https://doi.org/10.1002/anie.201204031.

[17] M.A. Newton, D. Ferri, G. Smolentsev, V. Marchionni, M. Nachtegaal, Room-temperature carbon monoxide oxidation by oxygen over Pt/Al₂O₃ mediated by reactive platinum carbonates, Nat. Commun. 6 (2015) 8675, https://doi.org/10.1038/ncomms9675.

[18] N. An, X. Yuan, B. Pan, Q. Li, S. Li, W. Zhang, Design of a highly active Pt/Al₂O₃ catalyst for low-temperature CO oxidation, RSC Adv. 4 (2014) 38250-38257, https://doi.org/10.1039/c4ra05646a.

[19] A. Trovarelli, Catalysis by Ceria and Related Materials, Imperial College Press, London, 2002, https://doi.org/10.1142/p249.

[20] M. Watanabe, Y. Zhu, H. Uchida, Oxidation of CO on a Pt-Fe alloy electrode studied by surface enhanced infrared reflection-absorption spectroscopy, J. Phys. Chem. B 104 (2000) 1762-1768, https://doi.org/10.1021/jp993001q.

[21] B.E. Hayden, M.E. Rendall, O. South, Electro-oxidation of carbon monoxide on well-ordered Pt(111)/Sn surface alloys, J. Am. Chem. Soc. 125 (2003) 7738-7742, https://doi.org/10.1021/ja0214781.

[22] J.J. Li, B.L. Zhu, G.C. Wang, Z.F. Liu, W.P. Huang, S.M. Zhang, Enhanced CO catalytic oxidation over an Au-Pt alloy supported on TiO₂ nanotubes: investigation of the hydroxyl and Au/Pt ratio influences, Catal. Sci. Technol. 8 (2018) 6109-6122, https://doi.org/10.1039/c8cy01642a.

[23] M. Kobayashi, S. Hidai, H. Niwa, Y. Harada, M. Oshima, Y. Horikawa, T. Tokushima, S. Shin, Y. Nakamori, T. Aoki, Co oxidation accompanied by degradation of Pt-Co alloy cathode catalysts in polymer electrolyte fuel cells, Phys. Chem. Chem. Phys. 11 (2009) 8226-8230, https://doi.org/10.1039/b903818c.

[24] S. Furukawa, T. Komatsu, Intermetallic compounds: promising inorganic materials for well-structured and electronically modified reaction environments for efficient catalysis, ACS Catal. 7 (2017) 735-765, https://doi.org/10.1021/acscatal.6b02603.


[25] T. Komatsu, M. Fukui, T. Yashima, Cobalt intermetallic compounds for selective hydrogenation of acetylene, Stud. Surf. Sci. Catal. 101 B (1996) 1095-1104, https://doi.org/10.1016/s0167-2991(96)80321-1.

[26] T. Komatsu, S. Hyodo, T. Yashima, Catalytic properties of Pt-Ge intermetallic compounds in the hydrogenation of 1,3-butadiene, J. Phys. Chem. B 101 (1997) 5565-5572, https://doi.org/10.1021/jp971117l.

[27] T. Komatsu, D. Satoh, A. Onda, Ti-Pt intermetallic compound catalysts more active than Pt for hydrogen dissociation and ethylene hydrogenation, Chem. Commun. (2001) 1080-1081, https://doi.org/10.1039/b102415a.

[28] K. Liu, A. Wang, T. Zhang, Recent advances in preferential oxidation of CO reaction over platinum group metal catalysts, ACS Catal. 2 (2012) 1165-1178, https://doi.org/10.1021/cs200418w.

[29] M.M. Schubert, M.J. Kahlich, G. Feldmeyer, M. Hüttner, S. Hackenberg, H. A. Gasteiger, R.J. Behm, Bimetallic PtSn catalyst for selective CO oxidation in $H_2$- rich gases at low temperatures, Phys. Chem. Chem. Phys. 3 (2001) 1123-1131, https://doi.org/10.1039/b008062o.

[30] B.S. Caglayan, İ.I. Soykal, A.E. Aksoylu, Preferential oxidation of CO over Pt-Sn/ AC catalyst: adsorption, performance and DRIFTS studies, Appl. Catal. B Environ. 106 (2011) 540-549, https://doi.org/10.1016/j.apcatb.2011.06.014.

[31] P.V. Snytnikov, K.V. Yusenko, S.V. Korenev, Y.V. Shubin, V.A. Sobyanin, Co-Pt bimetallic catalysts for the selective oxidation of carbon monoxide in hydrogen-containing mixtures, Kinet. Catal. 48 (2007) 276-281, https://doi.org/10.1134/S0023158407020127.

[32] T. Komatsu, A. Tamura, Pt₃Co and PtCu intermetallic compounds: promising catalysts for preferential oxidation of CO in excess hydrogen, J. Catal. 258 (2008) 306-314, https://doi.org/10.1016/j.jcat.2008.06.030.

[33] G. Saravanan, R. Khobragade, L. Chand Nagar, N. Labhsetwar, Ordered intermetallic Pt-Cu nanoparticles for the catalytic CO oxidation reaction, RSC Adv. 6 (2016) 85634-85642, https://doi.org/10.1039/c6ra19602k.

[34] T. Komatsu, M. Takasaki, K. Ozawa, S. Furukawa, A. Muramatsu, PtCu intermetallic compound supported on alumina active for preferential oxidation of CO in hydrogen, J. Phys. Chem. C. 117 (2013) 10483-10491, https://doi.org/10.1021/jp4007729.

[35] L.E. Gómez, B.M. Sollier, A.M. Lacoste, E.E. Miró, A.V. Boix, Hydrogen purification for fuel cells through CO preferential oxidation using PtCu/Al2O3 structured catalysts, J. Environ. Chem. Eng. 7 (2019) 103376, https://doi.org/10.1016/j.jece.2019.103376.

[36] R. Castillo, E. Dominguez Garcia, J.L. Santos, M.A. Centeno, F. Romero Sarria, M. Daturib, J.A. Odriozola, Upgrading the PtCu intermetallic compounds: the role of Pt and Cu in the alloy, Catal. Today 356 (2020) 390-398, https://doi.org/10.1016/j.cattod.2019.11.026.

[37] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169-11186, https://doi.org/10.1103/PhysRevB.54.11169.

[38] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6 (1996) 15-50, https://doi.org/10.1016/0927-0256(96)00008-0.

[39] G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47 (1993) 558-561, https://doi.org/10.1103/PhysRevB.47.558.

[40] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758-1775, https://doi.org/10.1103/PhysRevB.59.1758.

[41] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953-17979, https://doi.org/10.1103/PhysRevB.50.17953.

[42] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865-3868, https://doi.org/10.1103/PhysRevLett.77.3865.

[43] H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13 (1976) 5188-5192, https://doi.org/10.1103/PhysRevB.13.5188.

[44] G. Henkelman, B.P. Uberuaga, H. Jónsson, A climbing image nudged elastic band method for finding saddle points and minimum energy paths, J. Chem. Phys. 113 (2000) 9901-9904, https://doi.org/10.1063/1.1329672.

[45] R.F.W. Bader, Atoms in Molecules: A Quantum Theory, Oxford University Press, Clarendon Press, 1990.

[46] G. Henkelman, A. Arnaldsson, H. Jónsson, A fast and robust algorithm for Bader decomposition of charge density, Comput. Mater. Sci. 36 (2006) 354-360, https://doi.org/10.1016/j.commatsci.2005.04.010.

[47] E. Sanville, S.D. Kenny, R. Smith, G. Henkelman, Improved grid-based algorithm for Bader charge allocation, J. Comput. Chem. 28 (2007) 899-908, https://doi.org/10.1002/jcc.20575.

[48] Kristin Persson, Materials Data on CuPt (SG:166) by Materials Project, 2016, https://doi.org/10.17188/1280433.

[49] D.J. Miller, H. Öberg, L.Å. Näslund, T. Anniyev, H. Ogasawara, L.G.M. Pettersson, A. Nilsson, Low $O_2$ dissociation barrier on Pt(111) due to adsorbate-adsorbate interactions, J. Chem. Phys. 133 (2010) 224701, https://doi.org/10.1063/1.3512618.

[50] P.D. Nolan, B.R. Lutz, P.L. Tanaka, J.E. Davis, C.B. Mullins, Molecularly chemisorbed intermediates to oxygen adsorption on Pt(111): a molecular beam and electron energy-loss spectroscopy study, J. Chem. Phys. 111 (1999) 3696-3704, https://doi.org/10.1063/1.479649.

[51] Q. Fu, J. Yang, Y. Luo, A first principles study on the dissociation and rotation processes of a single $O_2$ molecule on the Pt(111) surface, J. Phys. Chem. C. 115 (2011) 6864-6869, https://doi.org/10.1021/jp200687t.

[52] B. Shan, N. Kapur, J. Hyun, L. Wang, J.B. Nicholas, K. Cho, CO-coverage-dependent oxygen dissociation on Pt(111) surface, J. Phys. Chem. C. 113 (2009) 710-715, https://doi.org/10.1021/jp808763h.

[53] K. Golibrzuch, P.R. Shirhatti, J. Geweke, J. Rn Werdecker, A. Kandratsenka, D. J. Auerbach, A.M. Wodtke, C. Bartels, CO desorption from a catalytic surface: elucidation of the role of steps by velocity-selected residence time measurements, J. Am. Chem. Soc. 137 (2015) 1465-1475, https://doi.org/10.1021/ja509530k.

[54] P. Janthon, F. Viñes, J. Sirijaaraensre, J. Limtrakul, F. Illas, Adding pieces to the CO/ Pt(111) puzzle: the role of dispersion, J. Phys. Chem. C. 121 (2017) 3970, https://doi.org/10.1021/acs.jpcc.7b00365.

[55] V.J. Kwasniewski, L.D. Schmidt, Surface diffusion of CO on Pt (111), Surf. Sci. 274 (1992) 329-340, https://doi.org/10.1016/0039-6028(92)90838-W.

[56] H. Froitzheim, M. Schulze, Surface diffusion of CO on Pt(111): a HREELS study at high temperatures, Surf. Sci. 320 (1994) 85-92, https://doi.org/10.1016/0039-6028(94)00498-6.

[57] P.A. Redhead, Thermal desorption of gases, Vacuum 12 (1962) 203-211, https://doi.org/10.1016/0042-207X(62)90978-8.