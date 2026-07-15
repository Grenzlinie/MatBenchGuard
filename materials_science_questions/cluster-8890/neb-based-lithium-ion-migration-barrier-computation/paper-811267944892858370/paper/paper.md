Density functional theory study of Li, Na, and Mg intercalation and diffusion in $\text{MoS}_2$ with controlled interlayer spacing

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 Mater. Res. Express 3 064001

(http://iopscience.iop.org/2053-1591/3/6/064001)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.93.16.3
This content was downloaded on 09/06/2016 at 04:29

Please note that terms and conditions apply.

# Materials Research Express

**PAPER**

## Density functional theory study of Li, Na, and Mg intercalation and diffusion in MoS₂ with controlled interlayer spacing

Jing Shuai¹, Hyun Deog Yoo², Yanliang Liang², Yifei Li², Yan Yao³,³ and Lars C Grabow⁴

¹ Department of Physics, University of Houston, Houston, TX 77204, USA
² Department of Electrical and Computer Engineering and Materials Science & Engineering Program, University of Houston, Houston, TX 77204, USA
³ Texas Center for Superconductivity at University of Houston, Houston, TX 77204, USA
⁴ Department of Chemical & Biomolecular Engineering, University of Houston, Houston, TX 77204, USA

E-mail: yyao4@uh.edu and grabow@uh.edu

Keywords: MoS₂, intercalation kinetics, rechargeable batteries, magnesium, sodium, lithium, density functional theory

Supplementary material for this article is available online

### Abstract
Layered materials, such as the transition metal dichalcogenide molybdenum disulfide (MoS₂), are promising materials for ion storage in electrodes of rechargeable batteries. To extend the application range of these materials to ions beyond lithium-ions, we used van der Waals corrected density functional theory simulations to study the intercalation and diffusion of lithium (Li), sodium (Na), and magnesium (Mg) in the 2H structure of MoS₂ as a function of interlayer spacing. All three species exhibit an optimal intercalation energy, which is reached at about 11% expansion for Li and Mg, and 23% expansion for Na. Similarly, the slow diffusion kinetics of large Na and divalent Mg-ions can be improved by layer expansion. When the interlayer spacing is increased by about 35% from its equilibrium value, the diffusion of Na and Mg-ions becomes more facile than the diffusion of small, monovalent Li-ions, with diffusion barriers similar to those of Li in graphene. Our results indicate that interlayer expansion is a promising technique to improve intercalation kinetics and thermodynamics for large and/or multivalent ions in MoS₂, which can be a major limitation to battery performance. The rationalization of our results in terms of bonding geometries forms the basis of a battery electrode design framework with applications for a wide range of layered materials.

## 1. Introduction

Lithium-ion (Li-ion) batteries are in massive commercial adoption and manufacturing that is powering the growth of energy storage in both mobile and stationary applications. However, Li-ion technology has safety and resource limitations that call for alternative directions beyond Li-ion batteries [1]. Recently, both sodium (Na) and magnesium (Mg) ion batteries have attracted significant attention as future energy storage materials due to their natural abundance, negative redox potential, and high specific capacity [2, 3]. The atomic and ionic radii of Na ($r_{\text{atom,Na}} = 1.54$ Å; $r_{\text{ion,Na}} = 1.16$ Å) are larger than those of Li ($r_{\text{atom,Li}} = 1.34$ Å; $r_{\text{ion,Li}} = 0.90$ Å), thus limiting the choice of cathode materials for Na-ion batteries to those with larger spaces [4–6]. Mg metal can be reversibly deposited and stripped in a dendrite-free manner, but the strongly polarizing nature of divalent $\text{Mg}^{2+}$ ions hinders their diffusion in negatively charged host lattices despite being slightly smaller than Li ($r_{\text{atom,Mg}} = 1.30$ Å; $r_{\text{ion,Mg}} = 0.86$ Å) [7, 8]. Evidently, the key limitation for batteries using Mg- ion is the lack of suitable cathode host materials that allow for efficient intercalation with high ion mobility, which results in high capacity with fast charge and discharge behavior [9–11]. The additional challenge for Mg-ion batteries is the limited selection of a suitable electrolyte solution that can reversibly plate and strip Mg and is compatible with cathode materials [12–14].

Transition metal dichalcogenides display a characteristic layered structure, and have been studied as materials with excellent catalytic, photoelectrical, electronic, and optical properties [15–18]. In particular,

© 2016 IOP Publishing Ltd

molybdenum disulfide (MoS₂), a representative compound of layered dichalcogenides, is increasingly important in a variety of applications [19–22]. Each layer of 2H–MoS₂ is constructed by atomic tri-layers with hexagonal symmetry, in which two sulfide layers form slabs that can be stacked to form trigonal prismatic holes for molybdenum atoms. These tri-layers are weakly bound by van der Waals (vdW) forces so they can accommodate various guest ions in the interlayer gap [23]. Using highly exfoliated, graphene-like MoS₂ as a cathode material, which can reduce the intercalation issues to some extent, initial successes for Li, Mg, and Na-ion batteries with competitive battery performance have been reported [2, 24]. Concomitantly, these encouraging results have attracted interest for computational studies based on density functional theory (DFT) to investigate the effects of MoS₂ structure on its intercalation properties. For instance, Li et al [25] investigated the adsorption and diffusion of Li in MoS₂ bulk, bilayer, monolayer, and zigzag MoS₂ nanoribbons and Enyashin et al [26] studied the stability of Li intercalated in 2H- and 1T-MoS₂ as a function of the Li content and the intercalation site.

In a combined experimental and computational approach we have previously demonstrated that controlled expansion of MoS₂ interlayer spacing can drastically improve Mg-ion mobility by two orders of magnitude and enable the otherwise barely active MoS₂ to approach its theoretical capacity for Mg-ion storage [21]. Experimentally, the expansion was realized by inserting a controlled amount of poly(ethylene oxide) (PEO) into the lattice of MoS₂ to expand the interlayer distance from 6.2 to 14.5 Å (equivalent to a lattice constant expansion from $c = 12.4$ Å to $c = 29.0$ Å). Moreover, the bilayer PEO-intercalated MoS₂ nanocomposite exhibits twice the Na⁺ storage capacity as that of commercial MoS₂ [27]. Here, we extend our previous work and present the first systematic assessment of Li, Na, and Mg-ion intercalation in the 2H–MoS₂ structure with controlled interlayer spacing using DFT. The range of interlayer spacing reaches from the bulk structure to near monolayer configurations. We discuss the effect of size and charge of intercalating cations on their diffusion behavior in 2H–MoS₂, and provide valuable insights for electrode materials design beyond Li-ions.

## 2. Computational details

Spin-paired total energy calculations were performed within the framework of DFT [28] as implemented in the Vienna ab initio simulation package (VASP) [29–32]. The vdW-DF functional was adopted to treat exchange and correlation including a self-consistent van der Waals (vdW) correction to account for dispersion interaction [33, 34]. The wave function was expanded in a plane wave basis set with periodic boundary conditions using an energy cut-off of 540 eV. The projector augmented wave method was employed to treat the wave function near ionic cores [35, 36]. The hexagonal, trigonal prismatic 2H–MoS₂ structure was represented by a $3 \times 3 \times 1$ supercell, which included 18 Mo atoms and 36 S atoms. For this structure we obtained the lattice parameters $a = 3.15$ Å and $c = 12.60$ Å at the equilibrium volume, which are in good agreement with experimental data ($a = 3.160$ Å, $c = 12.294$ Å, $\alpha = 90^\circ$, $\gamma = 120^\circ$) and those from theoretical results reported before [37, 38]. This 2H–MoS₂ structure has two high symmetry adsorption sites available: the octahedral (Oₕ) site above the center of a hexagon, where a total of six $M$–S bonds can form (figure 1(a)); and the tetrahedral (Tₕ) site above a Mo atom, where only one additional $M$–S bond can be formed with a S atom from the upper layer, resulting in a total of four $M$–S bonds (figure 1(b)). We note that a 1T-MoS₂ structure with only top sites on Mo atoms exists, but a previous report concluded that intercalation into 1T-MoS₂ is unfavorable due to the formation of disordered structures after relaxation [26]. Because we only study the 2H–MoS₂ structure in our work, we will refer to it simply as MoS₂, unless otherwise noted.

We studied the effect of layer spacing on $M$ ($M = \text{Li}, \text{Na}, \text{Mg}$) intercalation by varying the lattice constant $c$ in the $z$-direction and fixed one Mo atom in each of the two layers contained in the unit cell to constrain the layer spacing to the intended value. Note that the interlayer spacing is half of the lattice constant $c$ as illustrated in figure 1. All other Mo and S atoms as well as the intercalated $M$ atoms were fully relaxed. Integrations over the Brillouin zone used a Monkhorst-Pack $4 \times 4 \times 1$ $k$ point mesh [39]. Intercalation geometries were considered converged when the force was lower than $0.05$ eV Å⁻¹. To locate transition states and calculate activation barriers we used the climbing image nudged elastic band method as implemented in the VASP transition state tools with a minimum of five intermediate images along the reaction path [40, 41]. The initially linearly interpolated images were fully relaxed within the nudged elastic band algorithm with a force convergence criterion of $0.1$ eV Å⁻¹.

Similar to previous studies we define the binding energy of $M$ with $M = \text{Li}, \text{Na}, \text{Mg}$ as
$$E_{\text{b}} = E_{\text{tot}}\left(M/\text{MoS}_{2}\right) - E_{\text{tot}}\left(\text{MoS}_{2}\right) - E_{\text{tot}}(M),$$
where $E_{\text{tot}}\left(M/\text{MoS}_{2}\right)$, $E_{\text{tot}}\left(\text{MoS}_{2}\right)$, and $E_{\text{tot}}(M)$ are the total energies of the atom $M$-intercalated MoS₂, the corresponding MoS₂ bulk structure with the same lattice constant, and the free atom $M$, respectively [25, 42]. According to this definition, a more negative binding energy indicates more favorable exothermic intercalation of $M$ in MoS₂. All binding energy and diffusion barrier values are tabulated in tables S1 and S2 in the supporting information.

![](./images/811267944892858370_1.jpg)

Figure 1. Top and front view of $M$ ($M=$ Mg, Na, Li) intercalation geometries in 2H-MoS$_2$ at (a) the octahedral $O_h$ site above the center of a hexagon, and (b) the tetrahedral $T_h$ site above a Mo atom. The teal, olive, and violet spheres denote Mo, S and $M$ atoms. The spacing between any two layers is equivalent to half the lattice constant $c$ as indicated.

## 3. Results and discussion

### 3.1. Effect of layer spacing on Mg/Na/Li intercalation in 2H-MoS$_2$

For the equilibrated MoS$_2$ structure in the absence of any intercalated atoms we obtained a value of 12.60 Å for the lattice constant in the $c$ direction, which corresponds to a nominal layer spacing of 6.3 Å for the interlayer distance. We refer to this value as the equilibrium layer spacing. We then varied the $c$ lattice constant over a range from 12 to 24 Å to determine the effect of layer spacing on the intercalation energy of Li, Na, and Mg atoms. This range is sufficiently large to cover small layer compression ($-$5%) to large expansion ($+$90%), and is essentially approaching the single layer limit. For intercalation energy calculations we considered only a single atom $M$ ($M=$ Li, Na, Mg) in the unit cell, which causes asymmetric interactions between the two layers and results in an unrealistic asymmetric layer spacing upon intercalation. In reality, multiple ions are intercalated and restore the force balance acting on the individual layers. In addition, when we use PEO to increase the layer spacing, the polymer thickness rather than the intercalated ions dictate the layer spacing [21]. We correct this artifact in our simulation by fixing the $z$ coordinate of one Mo atom in each MoS$_2$ layer, while keeping all other degrees of freedom accessible. We consider this model a good compromise between capturing the realistic material structure and computational efficiency.

For the equilibrium layer spacing Li, Na, and Mg preferentially intercalate at the $O_h$ site, where they form six equivalent $M-S$ bonds as depicted in figure 1(a). The intercalation energies are $-2.42$, $-0.44$, and $-0.87$ eV for Li, Na, and Mg, respectively. Figure 2 shows the binding energy and binding preference for all three species as a function of the lattice parameter $c$. They all exhibit similar trends near the equilibrium layer spacing and reach an optimal intercalation energy when the layer spacing is increased to ca. 14 Å (11% expansion) for the smaller Li and Mg-ions, and ca. 15.5 Å (23% expansion) for the larger Na-ions. The corresponding optimal intercalation energies are $-2.57$, $-1.50$, and $-1.30$ eV for Li, Na, and Mg, respectively. The weak intercalation energy of Na at the equilibrium layer spacing and the large expansion necessary to stabilize Na are consistent with its large

![](./images/811267944892858370_2.jpg)

diameter preventing it from favorably intercalating in the relatively small space between equilibrated $MoS_2$ layers.

As the $MoS_2$ structure is further expanded in the $c$ direction, the intercalation energy profiles for all three species in figure 2 become flat, indicating that the binding properties asymptotically approach those of a single $MoS_2$ sheet. In the single layer limit, there is no preferred binding site between $O_h$ and $T_h$ for Na and Mg, but a binding site preference reversal is calculated for Li. This change occurs at about $c = 14.7$ Å, just after the optimal binding energy is reached. Above this value Li preferentially intercalates at the $T_h$ site. At $c = 24$ Å we calculate a binding energy for Li of $-1.94$ eV on the $T_h$ site and $-1.83$ eV at the $O_h$ site, i.e., binding at the $T_h$ site is $-0.11$ eV more stable. This agrees well with the binding energy at the $T_h$ site of about $-2$ eV and a site preference over the $O_h$ site of $-0.13$ eV obtained in periodic DFT calculations by Chen *et al* [42] for an interlayer spacing of $18$ Å ($c = 36$ Å). Similarly, Li *et al* [25] used a non-periodic, all-electron DFT method and reported a binding energy of $-2.12$ eV at the $T_h$ site and $-2.01$ eV at the $O_h$ site, which corresponds to the same binding site preference we obtained. This close agreement with both prior studies approximating $MoS_2$ monolayer configurations suggest that no further changes are to be expected at lattice constants larger than what we have considered in this work.

The different binding behavior of Li in comparison to Na and Mg can be explained in terms of bond lengths. Before reaching the optimal intercalation energy with increasing lattice constant $c$, all species prefer the $O_h$ site where they form six $M-S$ bonds, three with each layer, all having equivalent bond lengths. As $c$ increases, the intercalated ions start to break off from one of the two layers and only three $M-S$ bonds remain intact. In the monolayer limit the only difference between the $O_h$ and $T_h$ site is the presence of a Mo atom in the center of the three S atoms binding to the intercalated ion. Because Na and Mg form relatively long $M-S$ bonds (2.8 Å), there is negligible interaction with any nearby Mo atoms, rendering the $O_h$ and $T_h$ sites isoenergetic. In contrast, Li stays closer to the $MoS_2$ layer with a $M-S$ bond length of only 2.4 Å, allowing it to interact with the nearby Mo atom in the $T_h$ site, which stabilizes Li intercalation and ultimately causes the binding site preference change.

### 3.2. Effect of layer spacing on Mg/Na/Li diffusion in 2H–MoS₂
The intrinsic mobility of cations in the cathode material is directly related to battery performance in terms of the rate of charging and discharging. We have previously demonstrated that by tuning the $MoS_2$ interlayer spacing with PEO to $14.5$ Å ($c = 29$ Å), the diffusivity of Mg in $MoS_2$ increased two orders of magnitude [21]. Our calculations suggested that the lower diffusion barrier is a result of breaking three out of six Mg–S bonds in the $O_h$ position once the layer spacing exceeds ca. $9$ Å ($c = 18$ Å). Above this spacing, Mg binds to only one $MoS_2$ layer without preference for $O_h$ or $T_h$, allowing it to diffuse more freely. Any further increase in lattice spacing does not significantly affect Mg mobility, congruent with approaching the monolayer limit. In the following, we extend our investigation of Mg mobility and systematically study the effect of layer spacing on the mobility of Mg, Na, and Li in $MoS_2$ host structures.

The diffusion path for Mg is independent of the layer spacing and is shown in figure 3(a). Its migration starts from the most stable $O_h$ position and proceeds via the metastable $T_h$ site before moving on to the next $O_h$ site

![](./images/811267944892858370_3.jpg)

[21]. Energy profiles for Mg diffusion in $MoS_2$ for lattice constants in the range $13\ Å < c < 18\ Å$ are provided in figure 3(b), showing that Mg diffusion from $O_h$ to $T_h$ is always endothermic until $c$ increases to $18\ Å$. This is the value above which $O_h$ and $T_h$ sites become equally stable. As the lattice constant $c$ increases from 13 to $18\ Å$, the diffusion barrier decreases from 1.12 to 0.22 eV. For $c = 18\ Å$ the diffusion profile is practically flat and no well-defined transition state exists.

A comparison of the diffusion energy profiles for Mg and Na into $MoS_2$ layers in figures 3(b) and (d) shows strong qualitative similarities. The completely flat energy profile without a discernible transition state and equally strong adsorption on the $O_h$ and $T_h$ site also exist for Na at large values of $c$. For smaller lattice constants the transition state lies near the final state for both, Mg and Na. Notably, the diffusion barriers for Na in the bulk ($c = 13\ Å$) and monolayer ($c = 18\ Å$) limit are 1.14 and 0.20 eV, and nearly identical to the corresponding values for Mg with $E_a(c = 13\ Å) = 1.12$ eV and $E_a(c = 18\ Å) = 0.22$ eV. The overlaid diffusion barriers for Mg and Na as a function of the lattice constant $c$ in figure 4 visualize these quantitative similarities most clearly. Overall, these results suggest that the stronger polarization strength of divalent $Mg^{2+}$ ions counteracts its size advantage in comparison to larger, monovalent $Na^+$ ions.

Before we continue, we briefly clarify how the switch in binding site preference for Li affects the following discussion of Li diffusion. With the exception of Li and $c > 15\ Å$, intercalation at the $O_h$ site is most stable and diffusion from $O_h$ to $T_h$ is endothermic. Thus, we have uniformly chosen the $O_h$ site as the starting site for the ion migration path along alternating $O_h$ and $T_h$ sites ($O_h \rightarrow T_h \rightarrow O_h \rightarrow T_h \rightarrow \dots$) and use it as reference in figure 3. The diffusion barrier is always defined as the maximum span between the highest and lowest energy value along the diffusion path.

Li diffusion on $MoS_2$ monolayers was previously studied by Chen et al [42] and Li et al [25], who both reported a diffusion barrier of 0.21 eV from the more stable $T_h$ site to the less favorable $O_h$ site. In the near monolayer limit with $c = 18\ Å$ we found the same endothermic diffusion path from $T_h$ to $O_h$, but with a slightly higher barrier of 0.31 eV. For the bulk-like lattice constant of $c = 13\ Å$ Li migrates from the more favorable $O_h$ site to the metastable $T_h$ site with a diffusion barrier of $E_a = 0.54$ eV, again in excellent agreement with the previously reported value of $E_a = 0.49$ eV at the equilibrium lattice constant [25]. Although Li diffusion in bulk-

![](./images/811267944892858370_4.jpg)

like MoS₂ structures is slower than on separated layers, it is still at least 0.6 eV more facile compared to Mg or Na. This result is expected because Li is relatively small and monovalent, both of which are properties that benefit ion migration.

When comparing Li's diffusion behavior between MoS₂ layers with varied spacing to Mg and Na, however, Li displays a different and somewhat unexpected behavior. As already discussed, the intercalation site preference changes only for Li from Oₕ below 14.7 Å to Tₕ as the lattice is further expanded (figure 2(a)). The lattice constant at which the Oₕ and Tₕ sites are equally favorable coincides with a minimum diffusion barrier of 0.26 eV at about $c=15$ Å (figure 3(c)). On the other hand, neither Mg nor Na exhibits a local minimum in their diffusion barriers as $c$ is increased. As a result, for large lattice constants we unexpectedly find that Li diffusion becomes even more difficult than Mg or Na diffusion as shown in figure 4.

We rationalize the different diffusion barrier behavior of Li and Na/Mg again in terms of binding configurations. At $c=15$ Å, where the minimum barrier for Li occurs, Li binds to both MoS₂ tri-layers with an equal M–S bond distance of 2.8 Å. The equal attraction to both layers causes Li to 'float' perfectly centered between the layers, such that it cannot experience the atomic scale corrugation of either layer. For larger layer spacing Li can bind to only one layer, causing the M–S bond distance to reduce gradually to 2.4 Å, at which point Li starts to interact with Mo atoms at the center of MoS₂ tri-layers and therefore diffuses on a much rougher surface as reflected by the increased diffusion barrier. Na and Mg, on the other hand, maintain a minimum M–S bond length of 2.8 Å and are hardly affected by the presence of Mo atoms.

Figure 4 depicts that at a lattice constant of ca. 17 Å the diffusion barriers for Li, Na, and Mg are nearly identical with a value of 0.28–0.30 eV. It is interesting to note that Li diffusion in graphene has a similar barrier of 0.277 eV, suggesting that 2H–MoS₂ with expanded layer spacing is a promising candidate for next generation cathode materials [43]. If one considers the intercalation energy trends in figure 2, however, it becomes evident that the lower diffusion barrier at larger expansion comes at the cost of weaker intercalation energies and a thermodynamic penalty. For optimal battery performance one must find the ideal compromise between intercalation energy (voltage) and mobility (electrical current). Here it turns out that Li remains the clear winner with an intercalation energy minimum in close proximity to its diffusion barrier minimum, both of which are near the bulk lattice constant of MoS₂. Overall, Li has the strongest intercalation energy of all three investigated species combined with a low diffusion barrier, which explains its predominant use for rechargeable batteries. Yet, our simulations indicate that it is possible to improve Na and Mg mobility and their intercalation kinetics in these layered materials by increasing the layer spacing at the cost of decreasing the operating voltage.

The main objective of this modeling work is to capture the key difference of $Li^+$, $Na^+$ and $Mg^{2+}$ diffusion in expanded MoS₂ to a first order of approximation. Comparing with experimental results we reported earlier [21, 27], we recognize the insertion of polyethylene oxide molecules, which is not considered in the simulation, certainly affects the thermodynamic and kinetic properties of ion diffusion in between the layers (such as the binding energy, intercalation voltage, and the migration barrier), but the major conclusions should still hold true.

## 4. Conclusions

We have performed periodic, vdW corrected DFT calculations to study systematically the effect of varying the spacing between 2H–MoS₂ layers on the thermodynamic and kinetic intercalation behavior for Li, Na, and Mg. The layer spacing was altered by changing the lattice constant $c$ normal to the MoS₂ layers. At the equilibrium value of the lattice constant $c$ Li, Na, and Mg ions preferentially bind to the octahedral $O_h$ site of 2H–MoS₂ and their intercalation energy weakens in the order Li < Mg < Na. When the lattice constant $c$ is increased beyond 14.7 Å, only Li changes its binding site preference to the tetrahedral $T_h$ site. We identified optimal lattice constants of ~14 and ~15.5 Å, corresponding to the strongest intercalation energy for Li and Mg, and Na, respectively. At the optimal layer spacing for each ion, the binding energy decreases in the order Li < Na < Mg, indicating that MoS₂ can be tuned to intercalate large Na ions more strongly than the smaller, but divalent, Mg ions.

The diffusion energy barrier for Li, Na, and Mg generally decreases as the lattice constant $c$ increases, indicating that layer expanded MoS₂ has higher ion mobility and can achieve faster charge and discharge kinetics. We identified a shallow diffusion barrier minimum for Li, whereas the barriers for Na and Mg monotonically decrease until they reach the value of Li diffusion in graphene in the single layer limit. The diffusion barrier minimum, as well as the site preference change for Li, can be rationalized in terms of bonding geometry and bond lengths. Li bonds strongly to S and can form short Li–S bonds, such that it can still interact with the Mo atoms at the center of a MoS₂ tri-layer. In the absence of a second layer, i.e. the single layer limit, Li is attracted to Mo atoms, thus favoring the $T_h$ site above a Mo atom and decreasing its mobility. In a narrow enough gap between two layers, the interactions of Li with the exposed S atoms from both layers are dominant, diminishing the role of Mo. This argument is congruent with the longer bonds formed by Na and Mg, preventing these ions from any significant interactions with the more distant Mo atoms independent of layer spacing. Thus, we conclude that the similar behavior of Li, Na and Mg for bulk-like MoS₂ structures is governed by their dominant interactions with S atoms, and that the different behavior of Li at large lattice spacing results from added interactions with Mo atoms.

In summary, our results demonstrate that the storage capacity and diffusion kinetics of MoS₂ can be improved by tuning its layer spacing. MoS₂ was chosen as a prototype dichalcogenide and we expect these results to be directly translatable to other layered cathode materials. To this end, our study proposes guiding principles for the design of improved battery electrode materials that allow the replacement of scarce Li with abundant Na or Mg, while simultaneously improving device safety.

## Acknowledgments

YY acknowledges financial support from the Office of Naval Research (No. N00014-13-1-0543) and National Science Foundation (CMMI-1400261). LCG acknowledges financial support from the US Department of Energy, Office of Science, Office of Basic Energy Sciences under Award No. DE-SC0011983. This work used computational resources provided by the National Energy Research Scientific Computing (NERSC) Center, a DOE Office of Science User Facility supported by the Office of Science of the US Department of Energy (under Contract No. DE-AC02-05CH11231). Parts of this work used the Extreme Science and Engineering Discovery Environment (XSEDE), which is supported by the NSF (Grant No. ACI-1053575), and HPC resources provided by the Texas Advanced Computing Center (TACC) at The University of Texas at Austin. Finally, we thank the Center of Advanced Computing and Data Systems (CACDS) at the University of Houston for access to the Maxwell/Opuntia Clusters and advanced HPC support facilitated under NSF-MRI Grant No. ACI-1531814 to carry out the research presented here.

## References

[1] Oleg S, Vikram P, Abhishek K, Chayanit C and Venkatasubramanian V 2015 Quantifying the promise of 'beyond' Li-ion batteries *Transl. Mater. Res.* 2 045002

[2] Liang Y, Feng R, Yang S, Ma H, Liang J and Chen J 2011 Rechargeable Mg batteries with graphene-like MoS₂ cathode and ultrasmall Mg nanoparticle anode *Adv. Mater.* 23 640–3

[3] Guo Y-S, Zhang F, Yang J, Wang F-F, NuLi Y and Hirano S-I 2012 Boron-based electrolyte solutions with wide electrochemical windows for rechargeable magnesium batteries *Energy Environ. Sci.* 5 9100

[4] Kim S-W, Seo D-H, Ma X, Ceder G and Kang K 2012 Electrode materials for rechargeable sodium-ion batteries: potential alternatives to current lithium-ion batteries *Adv. Energy Mater.* 2 710–21

[5] Jian Z *et al* 2014 Atomic structure and kinetics of NASICON NaₓV₂(PO₄)₃ cathode for sodium-ion batteries *Adv. Funct. Mater.* 24 4265–72

[6] Kubota K and Komaba S 2015 Review—practical issues and future perspective for Na-ion batteries *J. Electrochem. Soc.* 162 A2538–50

[7] Amatucci G G, Badway F, Singhal A, Beaudoin B, Skandan G, Bowmer T, Plitza I, Pereira N, Chapman T and Jaworski R 2001 Investigation of yttrium and polyvalent ion intercalation into nanocrystalline vanadium oxide *J. Electrochem. Soc.* 148 A940–50

[8] Mohtadi R and Mizuno F 2014 Magnesium batteries: current state of the art, issues and future perspectives *Beilstein J. Nanotechnol.* 5 1291–311

[9] Yoo H D, Shtenenberg I, Gofer Y, Gershinsky G, Pour N and Aurbach D 2013 Mg rechargeable batteries: an on-going challenge *Energy Environ. Sci.* 6 2265–79

[10] Muldoon J, Bucur C B and Gregory T 2014 Quest for nonaqueous multivalent secondary batteries: magnesium and beyond *Chem. Rev.* 114 11683–720

[11] Huie M M, Bock D C, Takeuchi E S, Marschilok A C and Takeuchi K J 2015 Cathode materials for magnesium and magnesium-ion based batteries *Coord. Chem. Rev.* 287 15–27

[12] Wan L F and Prendergast D 2014 The solvation structure of Mg Ions in Dichloro complex solutions from first-principles molecular dynamics and simulated x-ray absorption spectra *J. Am. Chem. Soc.* 136 14456–64

[13] Canepa P, Jayaraman S, Cheng L, Rajput N N, Richards W D, Gautam G S, Curtiss L A, Persson K A and Ceder G 2015 Elucidating the structure of the magnesium aluminum chloride complex electrolyte for magnesium-ion batteries *Energy Environ. Sci.* 8 3718–30

[14] Shtenenberg I, Salama M, Yoo H D, Gofer Y, Park J-B, Sun Y-K and Aurbach D 2015 Evaluation of $(CF_3SO_2)_2N^-$ (TFSI) based electrolyte solutions for Mg batteries *J. Electrochem. Soc.* 162 A7118–28

[15] Chianelli R R, Siadati M H, De la Rosa M P, Berhault G, Wilcoxon J P, Bearden R and Abrams B L 2006 Catalytic properties of single layers of transition metal sulfide catalytic materials *Catalysis Rev.* 48 1–41

[16] Wang Q H, Kalantar-Zadeh K, Kis A, Coleman J N and Strano M S 2012 Electronics and optoelectronics of two-dimensional transition metal dichalcogenides *Nat. Nanotechnol.* 7 699–712

[17] Chhowalla M, Shin H S, Eda G, Li L J, Loh K P and Zhang H 2013 The chemistry of two-dimensional layered transition metal dichalcogenide nanosheets *Nat. Chem.* 5 263–75

[18] Bao W *et al* 2014 Approaching the limits of transparency and conductivity in graphitic materials through lithium intercalation *Nat. Commun.* 5 4224

[19] Cheng F Y, Chen J and Gou X L 2006 $MoS_2$-Ni nanocomposites as catalysts for hydrodesulfurization of thiophene and thiophene derivatives *Adv. Mater.* 18 2561–4

[20] Wang H, Yu L, Lee Y H, Shi Y, Hsu A, Chin M L, Li L J, Dubey M, Kong J and Palacios T 2012 Integrated circuits based on bilayer $MoS_2$ transistors *Nano Lett.* 12 4674–80

[21] Liang Y, Yoo H D, Li Y, Shuai J, Calderon H A, Robles Hernandez F C, Grabow L C and Yao Y 2015 Interlayer-expanded molybdenum disulfide nanocomposites for electrochemical magnesium storage *Nano Lett.* 15 2194–202

[22] Wan J *et al* 2015 *In situ* investigations of Li-$MoS_2$ with planar batteries *Adv. Energy Mater.* 5 1401742

[23] Whittingham S and Gamble F R 1975 The lithium intercalates of the transition metal dichalcogenides *Mater. Res. Bull.* 10 363–71

[24] David L, Bhandavat R and Singh G 2014 $MoS_2$/graphene composite paper for sodium-ion battery electrodes *ACS Nano* 8 1759–70

[25] Li Y, Wu D, Zhou Z, Cabrera C R and Chen Z 2012 Enhanced Li adsorption and diffusion on $MoS_2$ zigzag nanoribbons by edge effects: a computational study *J. Phys. Chem. Lett.* 3 2221–7

[26] Enyashin A N and Seifert G 2012 Density-functional study of $Li_xMoS_2$ intercalates ($0 \leqslant x \leqslant 1$) *Comput. Theor. Chem.* 999 13–20

[27] Li Y, Liang Y, Robles Hernandez F C, Yoo H D, An Q and Yao Y 2015 Enhancing sodium-ion battery performance with interlayer-expanded $MoS_2$-PEO nanocomposites *Nano Energy* 15 453–61

[28] Hohenberg P 1964 Inhomogeneous electron gas *Phys. Rev.* 136 B864–71

[29] Kresse G and Hafner J 1993 Ab initio molecular dynamics for liquid metals *Phys. Rev. B* 47 558–61

[30] Kresse G and Hafner J 1994 Ab initio molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium *Phys. Rev. B* 49 14251–69

[31] Kresse G and Furthmüller J 1996 Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set *Comput. Mater. Sci.* 6 15–50

[32] Kresse G and Furthmüller J 1996 Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set *Phys. Rev. B* 54 11169–86

[33] Klimeš J, Bowler D R and Michaelides A 2010 Chemical accuracy for the van der Waals density functional *J. Phys.: Condens. Matter* 22 022201

[34] Klimeš J, Bowler D R and Michaelides A 2011 Van der Waals functionals applied to solids *Phys. Rev. B* 83 195131

[35] Blöchl P E 1994 Projector augmented-wave method *Phys. Rev. B* 50 17953–79

[36] Kresse G and Joubert D 1999 From ultrasoft pseudopotentials to the projector augmented-wave method *Phys. Rev. B* 59 1758–75

[37] Böker T, Severin R, Müller A, Janowitz C, Manzke R, Voß D, Krüger P, Mazur A and Pollmann J 2001 Band structure of $MoS_2$, $MoSe_2$, and $\alpha$-$MoTe_2$: angle-resolved photoelectron spectroscopy and ab initio calculations *Phys. Rev. B* 64 235305

[38] Min S K, Cho Y, Mason D R, Lee J Y and Kim K S 2011 Theoretical design of nanomaterials and nanodevices: nanolensing, supermagnetoresistance, and ultrafast DNA sequencing *J. Phys. Chem. C* 115 16247–57

[39] Monkhorst H J and Pack J D 1976 Special points for Brillouin-zone integrations *Phys. Rev. B* 13 5188–92

[40] Henkelman G, Uberuaga B P and Jónsson H 2000 A climbing image nudged elastic band method for finding saddle points and minimum energy paths *J. Chem. Phys.* 113 9901

[41] Henkelman G and Jónsson H 2000 Improved tangent estimate in the nudged elastic band method for finding minimum energy paths and saddle points *J. Chem. Phys.* 113 9978–85

[42] Chen H J, Huang J, Lei X L, Wu M S, Liu G, Ouyang C Y and Xu B 2013 Adsorption and diffusion of lithium on $MoS_2$ monolayer: the role of strain and concentration *Int. J. Electrochem. Sci.* 8 2196–203

[43] Zhou L-J, Hou Z F and Wu L-M 2012 First-principles study of lithium adsorption and diffusion on graphene with point defects *J. Phys. Chem. C* 116 21780–7