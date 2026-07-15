![](./images/812605511458357249_1.jpg)
![](./images/812605511458357249_2.jpg)

Article

# Towards an Understanding of Crystallization by Attachment

Haihua Pan $^{1}$ and Ruikang Tang $^{2,*}$

1 Qiushi Academy for Advanced Studies, Zhejiang University, Hangzhou 310027, China; panhh@zju.edu.cn
2 Department of Chemistry and Center for Biomaterials and Biopathways, Zhejiang University, Hangzhou 310027, China

* Correspondence: rtang@zju.edu.cn; Tel.: +86-571-8795-3736

Received: 3 May 2020; Accepted: 27 May 2020; Published: 01 June 2020

![](./images/812605511458357249_3.jpg)

**Abstract:** Crystallization via particle attachment was used in a unified model for both classical and non-classical crystallization pathways, which have been widely observed in biomimetic mineralization and geological fields. However, much remains unknown about the detailed processes and driving mechanisms for the attachment. Here, we take calcite crystal as a model mineral to investigate the detailed attachment process using in situ Atomic Force Microscopy (AFM) force measurements and molecular dynamics simulations. The results show that hydration layers hinder the attachment; however, in supersaturated solutions, ionic bridges are formed between crystal gaps as a result of capillary condensation, which might enhance the aggregation of calcite crystals. These findings provide a more detailed understanding of the crystal attachment, which is of vital importance for a better understanding of mineral formation under biological and geological environments with a wide range of chemical and physical conditions.

**Keywords:** crystallization; calcite; interface; aggregation; molecular dynamics simulation; atomic force microscopy

## 1. Introduction

Crystallization is a pathway of condensation or organization of materials by their components from a dispersed state or a different form, which is an important process in biological, geological, industrial, and ecological systems. A monomer-by-monomer addition is envisioned in the classical understanding of crystallization [1]. However, in recent years, a diverse set of "non-classical" crystallization pathways has been revealed, enriching our understanding of material formation [2]. Crystallization by particle attachment (CPA) has been suggested to unify the "classical" and "non-classical" crystallization pathways, in which "particles" include ions, dimers and oligomers, complex and ionic clusters, droplets and amorphous precursors, poorly crystalline nanoparticles, and nanocrystals, among others [3]. Crystals can be formed from these particles via the polymerization, re-organization, phase transformation, and (oriented) aggregation processes.

The classical crystallization (CC) pathway primarily contains the stages of nucleation and crystal growth (and ripening) [4]. This crystallization pathway usually produces hundreds of seeds in a small vial in the supersaturated solution during the nucleation process. As a result, small crystalline powders instead of bulk brick are usually formed in a supersaturated solution. It is still a challenge to fabricate a large single crystal via the CC pathway. The rich CPA pathways have opened the door to challenge the limitations of the CC pathway. For example, one biomineralization system demonstrated a pathway for fabricating a single calcite crystal via amorphous precursor phase-mediated crystallization, which was revealed in sea urchin embryonic spicules [5]. An ionic oligomer polymerization-based CPA pathway has shown its advantages in the fabrication of continuous bulk crystals [6], epitaxial repair

Crystals 2020, 10, 463; doi:10.3390/cryst10060463
www.mdpi.com/journal/crystals

of single crystals and tooth enamel [7], and nanodispersed and ordered organic–inorganic hybrid materials [8]. A polymer-induced liquid precursor (PILP) process has been shown to be successful in many biomimetic and bio-inspired materials fabrications [9]. CPA-based crystallization pathways not only have profound effects and advantages in building materials, but also have great impacts on the structures and properties of materials. For example, materials with elevated dopant ratios [10]; occlusions of organic polymers, which induce defects and enhance mechanical properties [11,12]; and complex and hierarchical morphologies with rich interfaces and textured patterns [13,14] have been widely observed by "non-classical" CPA pathways; however, these features are difficult to understand in terms of the CC pathway because materials with these structures are in a high energy state, and thus are thermodynamically unfavorable. Clearly, these rich and distinct structures will endorse materials with distinct properties, such as stability, surface activities, and mechanical and optical properties, which have advanced functions and will play important roles in energy harvesting and storage, environment treatment, sustained development, and healthcare.

Increasing evidence is available and advances have been made to complement the mapping of CPA-mediated crystallization pathways; however, much still remains unknown about the detailed processes and their mechanism, which are of vital importance for material fabrication. In order to better understand particle aggregation and attachment, the theory of Derjaguin, Landau, Verwey, and Overbeek (DLVO) is widely applied in colloidal systems [15,16]. DLVO theory is successful for microsized colloids and at micro-range distances. However, assumptions of continuous colloidal materials and media in DLVO theory have limited its successful applications in the understanding of the nano-range interactions of nanosized particles, which are of special interest in CPA processes. In this respect, there are two primary concerns regarding the CPA process. First, samples of the same kind of material usually have the same type of surface potential, meaning they will repel each other. Second, highly structured (ice-like) water layers have been widely observed on mineral surfaces [17–20], which will retard the direct lattice contact during aggregation. These two facts do not support the successful (lattice) attachment of particles.

In this work, we will take the calcite crystal (an extensively studied crystal for geology and biomineralization) as a model crystal to give a detailed understanding of the CPA process by using molecular dynamics simulations, as well as Atomic Force Microscopy (AFM) force measurement and solution chemistry experiments. We found that the capillary gap formed during attachment can facilitate ionic bridge formation, enriching the understanding of the CPA process of mineral formation in geological environments, as well as in biomineralization.

## 2. Materials and Methods

### 2.1. Preparation and Characterization of Calcite

Calcite was synthesized following the work of Addadi et al. [21]. Briefly, calcite was grown by slow diffusion (about 2 days) of $(NH_{4})_{2}CO_{3}$ vapor into beakers containing 20 mL of 7.5 mM $CaCl_{2}$ in desiccators (25 cm in diameter). Then, $(NH_{4})_{2}CO_{3}$ powder was placed at the bottom of the desiccators. $CO_{2}$ and $NH_{3}$ gases were diffused into a beaker through three needle holes on its aluminum foil cover. The room temperature was set to $25 \pm 2\ {^\circ}C$. Following the same method but using 2.0 mM $CaCl_{2}$, larger calcite (>50 mm) crystals could be obtained. After crystallization, the calcite crystals were obtained after decantation and then washed with a calcite saturation solution (prepared by calcite suspension one week earlier) and water–ethanol mixture (1:2 in volume) three times. The solids were dried in air. Well-shaped 5–10 μm rhombohedral crystals were selected to prepare a calcite probe for AFM force measurements and 50–100 mm rhombohedral crystals were selected as the substrate (see below). All calcite crystallites were freshly prepared before use. The morphology of the large crystallites was observed using an optical microscope (Eclipse 80i, Nikon, Japan). Calcite probes were characterized by a scanning electron microscope (SEM, S-4800, Hitachi, Japan).

### 2.2. AFM Force Measurement

Crystal probes were fabricated by mounting a {104} facet-exposed rhombohedral calcite crystal on a tipless cantilever (NSG11 tipless, with resonant frequency and force constant of 150 kHz and 5.5 N/m, respectively; NT-MDT, Moscow, Russia) by using urethane glue (Hardman, Inc.). The edge of the rhombohedral calcite was oriented parallel to the cantilever. Another {104} facet-exposed rhombohedral calcite crystal was glued on a silicon wafer as the calcite substrate. Calcite crystals of the probe and the substrate were aligned in the same orientation, which was confirmed by using optical microscopy. The force curve was measured from the deflection of the cantilever during the approaching and retracting processes. All force measurements were performed in aqueous solutions with a commercial atomic force microscope (Nanoscope Multimode IVa with PicoForce controller, Veeco and DI, USA). The fluid flow was stopped for sensitive force measurements. Supersaturated solutions were freshly prepared for each force measurement by using $CaCl_2$ and $NaHCO_3$ solutions with equal concentrations of calcium and bicarbonate. The supersaturations were calculated by using VMINTEQ [22]. The approach and retraction forces were measured at different contacting times and in different solutions. The rates of approach and separation were less than 400 nm/s to reduce the hydrodynamic force. The same calcite probe and substrate were applied for different solution conditions and contacting times to rule out the possible effects of the crystal topology, orientation, and contacting gap on force measurement. The room temperature was controlled at $25 \pm 2\ ^{\circ}\text{C}$. More than 100 force curves for each crystal–crystal interaction were captured.

### 2.3. Molecular Dynamics Simulations

For all molecular dynamics (MD) simulations, the GROMACS program was used [23]. The X-ray crystal structures of calcite were applied as the initial configuration [24]. A water slab (520 molecules) with or without randomly inserted ions was placed between the calcite crystals, which contained 8 $\times 8 \times 4\ CaCO_3$ units. The size of the whole system was $2.514 \times 2.459 \times 4.957\ \text{nm}^3$. The force field parameters of calcite were taken from [25], reproducing the crystal and interfacial structure well. The single-point charge (SPC) water model was applied following [25]. Periodic boundary conditions were applied in all directions. Particle mesh Ewald (PME) summation was applied for the treatment of long-range Coulombic interactions [26]. The cut-off distance was chosen to be 1.1 nm. The NpT ensemble with anisotropic Berendsen method [27] and V-rescale method [28] was applied for pressure control and temperature control, respectively. Model building and MD trajectory snapshots were performed with VMD [29]. The interfacial structures could be described by using local density profiles, which were obtained by dividing the space into slices parallel to the crystal–solution interface and counting the density of each slice. The hydration numbers of ions were calculated by the integration of the radial distribution function for the first peak.

The free energy profiles (potential of mean force, PMF) of the attachment of ions were obtained by umbrella sampling with the umbrella integration method [30]. About 120 umbrella windows were set along the reaction coordination to ensure the accuracy of the integration of free energy. Replica exchange of neighboring windows was applied to enhance the quality of the sampling [31]. The error (standard deviation) was estimated from variances of mean forces [32]. The total simulation time was more than 24 ns for each free energy profile of ionic attachment. The adsorption free energy was obtained by measuring the difference of the free energy for the bulk solution and the adsorbed state in the free energy minimum. The PMF of the nanocalcite attachment was obtained by umbrella sampling with the weighted histogram analysis method (WHAM) [33], with a larger bin size of windows ($n = 50$) and longer simulation time (2 ns) for each window (compared with the simulation of the single-ion system as given above), because a slower relaxation of the hydration structure was found for a nanocrystal than that for a single ion. The free energy errors were estimated by using 20 Bayesian bootstrap analyses [34]. The simulation time was more than 100 ns for the free energy profile of the attachment of nanocalcite.

## 3. Results and Discussion

### 3.1. Retardant Effects of Hydration Layers on Attachment

#### 3.1.1. Mineral Hydration Layers

During biomimetic mineralization, crystals are formed in a water solution. Therefore, the surfaces of inorganic crystals are surrounded by water molecules. Unlike molecules in the bulk crystal phase, molecules at the surface contain many unbalanced bonds, which can interact with water molecules by ionic, coordinate, or hydrogen bonds [35,36]. These interactions will change the orientation, freedom, and organization of water molecules near a crystal surface, and as a result one to several hydration layers will be formed, which can be detected by X-ray reflectivity (XRR) [37,38], grazing incidence X-ray diffraction (GIXRD) [39], solid-state NMR (ssNMR) [40], and frequency/force modulation atomic force microscopy (FM-AFM) [41-43]. These water layers cover crystal surfaces and will affect the particle attachments during crystallization [44].

Taking the most stable mineral facets of calcite (104), hydroxyapatite (010), and brushite (010) as examples, MD simulation results revealed that there were 2 or 3 water layers on their surfaces [45-48]. For calcite (104), its hydration structures are well-established [38,41-43,45], in which the first hydration layer was coordinated with surface calcium ions by oxygen (Ow). The second water layer formed a hydrogen bond with the carbonate ions [38]. In comparison with the geometry of the calcite structure, Ow in the first hydration layer occupied the lattice site of carbonate oxygen (Oc), and Ow in the second hydration layer occupied the lattice sites of calcium ions (Figure 1) [45,46]. We take this phenomenon as the transformation of the structure information from crystals to water layers. Because the surface lattice sites were occupied by hydration water molecules, a dehydration process was needed to replace water by inorganic ions during crystallization. These processes will be analyzed in detail in the next section.

![](./images/812605511458357249_4.jpg)

Figure 1. Water density distribution for the hydration layers of the calcite (104) face. Miller indices correspond to the hexagonal cell ($a = 5$ Å, $c = 17$ Å). (a) Atomic point-cloud images of side views of the calcite (104) interface along [0 1 0] (left), and [4 2 −1] axes, respectively. The atomic number density is proportional to the brightness of the point cloud. Red: O; white: H; cyan: Ca or C. Dashed lines are drawn to guide the view for the adsorption sites (cyan for calcium lattice sites; green for oxygen lattice sites); (b) The density profile at the calcite (104) interface (red: carbonate; black: calcium; blue: water). For comparison, the density profile is replicated but is shifted to a distance of one calcium carbonate layer in calcite (see the lower one). The structures of the hydration layers parallel to the crystal surface match the periodicity of the crystal.

### 3.1.2. Dehydration during Particle Attachment

A classical crystallization process can be understood as the balance of the dynamic attachment-detachment of water molecules and ions on crystal faces. Therefore, the differences and barriers of the free energy for water molecules and ions are the keys to understanding the detailed crystallization process. The adsorption free energies of ions are larger than that of water (Figure 2a), which indicates that thermodynamically, water molecules will be replaced by ions and lead to crystal growth. However, in kinetics, the adsorption and desorption barriers of ions are much larger than that of water. These local barriers are correlated to the dehydration of ions during attachment (Figure 2b). In this regard, hydration water molecules play vital roles in the kinetics of crystal growth via ionic attachments, which has been corroborated by the analysis of the step-growth rate of supersaturated solutions with different ratios of $Ca^{2+}/CO_3^{2-}$ [49-51] and background electrolytes [52], and the spatial distribution of adsorbed mineral ions in hydration layers [53]. As a more complicated result, the anomalies in the crystal growth kinetics can be affected by the adsorption layer [54,55], which contains adsorbed mineral ions and hydration layers.

![](./images/812605511458357249_5.jpg)

Figure 2. (a) Potential of mean force (PMF) of the adsorption of water, calcium ion, and carboxylate ion. The standard deviations of PMF are marked by transparent filled bands. (b) Dehydration of ions is accompanied by the attachment of ions on calcite surface lattice sites.

In the CPA model, in addition to ions, nanocrystallites can also act as the building block. Therefore, the attachment of nanocalcites on calcite (104) is also evaluated. The PMF of the attachment of nanocalcites ($4 \times 4 \times 4$ unit cells, area = $3.2\ \text{nm}^2$) on a bulk calcite (104) face is investigated using umbrella sampling. Figure 3 reveals that a free energy barrier of $100\ \text{kJ/mol}$ ($\sim 40\ k_BT$) is needed to dehydrate and make lattice contact between two calcite faces. The hydration layers are attached so strongly that only under strong external surface pressure can they be broken through, and thereby be detected (either by using sharp AFM tips measuring just a few nm in diameter or just a few atoms on the tip, with strong cantilever (spring constant > 20 N/m) [56,57] or force measurement between two cross-stacked curved mica crystals with a surface force apparatus equipped with strong springs (>1000 N/m) [58]). Considering the much larger calcite particles in the suspension and the weak external driving force of Brownian motion ($\sim 1\ k_BT$), the hydration water layers will prevent the direct lattice attachment of microcrystallites in solution.

### 3.2. Promotion Effect of Ionic Bridge on Attachment under Supersaturated Condition

#### 3.2.1. Formation of Ionic Bridges during Attachment

Crystallite aggregates are widely observed in crystallization systems, which seems to conflict with the above conclusion that hydration layers will prevent the attachment of crystals. However, care should be taken, as the aggregated crystallites could also result from the heterogeneous nucleation on

mother crystals. A direct force measurement of calcite–calcite interaction was performed by using AFM (Figure 4a). Considering that the electrical double-layer repulsion force might prevent the attachment of calcite, 50 mM NaCl was introduced into solutions to screen this effect. It turned out that the attraction force was very small (<1 nN) between the two calcite crystallites in the saturated solutions (Figure 4b), which is consistent with other reports [59].

![](./images/812605511458357249_6.jpg)

Figure 3. Potential of mean force for the attachment of a nanocalcite (4 × 4 × 4 unit cells) on a calcite (104) substrate. The standard deviations of PMF are marked by the transparent filled band.

![](./images/812605511458357249_7.jpg)

Figure 4. Calcite–calcite force measurement: (a) scheme of the force curve measurement of calcite interactions; (b) a representative force curve of calcite in 50 mM NaCl saturated solutions; (c) a representative force curve of calcites in supersaturated solutions (supersaturation index, SI = 3.0); (d) the histogram analysis of the rupture forces.

To test if there is adhesion force in supersaturated solutions, the interaction force between the two calcite crystals was measured by AFM. In contrast to those in saturated solutions, the adhesion forces between calcite were much larger (>10 nN) in supersaturated solutions (Figure 4c). In addition to the adhesion force, during the detachment, an unexpected zig-zag force curve pattern (step-like feature) was frequently observed (inset in Figure 4c), which was understood as multiple rupture events. The rupture force was then defined as the abrupt change of the force at the rupture event, which was in the range of hundreds of pN to 1 nN (see the force histogram in Figure 4d). The magnitude of the rupture force was similar to a rupture of an ionic bond [60]. We suggest that the rupture force might be correlated with the formation of ionic bonds between two crystals.

MD simulations were performed to test if ionic bonds could be formed between two calcite crystals. Here, parts of randomly selected water molecules between two calcite crystals were replaced by calcium and carbonate ions (40 ion-pair). It turned out that as the calcium and carbonate ions were added, which formed a nanosized ionic bridge between the two crystals and remained stable for longer than 60 ns (Figure 5a). When an external force was applied to pull the ionic bridge apart, multiple rupture events were reproduced (Figure 5b). We found that the last rupture event was the breaking of a calcium-carbonate ionic bond between two clusters of calcium carbonate ions (Figure 5b). The rupture force measured in the MD simulation was about 1 nN, which was quite close to those values found in our AFM measurement (about 0.5 nN) (Figure 5c) and previous reporting [60]. Thereby, the breaking of ionic bonds can be applied to explain the rupture events in AFM force measurements.

![](./images/812605511458357249_8.jpg)
![](./images/812605511458357249_9.jpg)
![](./images/812605511458357249_10.jpg)

Figure 5. Molecular dynamics (MD) simulation results revealing the formation of ionic bridges in the gap between two calcite crystallites: (a) MD simulation snapshots; (b) the force curve calculated by pulling ionic clusters apart in the MD simulation; (c) representative force curves showing rupture events during the separation of two calcite crystallites in AFM measurements.

Therefore, in supersaturated solutions, ionic species can penetrate through the hydration layers, aggregate at the gap of two calcite crystallites, and connect them. This scenario is unexpected in the electrical double layer model but is important for the understanding of the adhesion force and the detailed CPA process.

### 3.2.2. Mechanism of Ionic Bridge Formation

In classical crystallization, the association of ions into ionic clusters in a solution does not occur readily (the probability of its formation decreases exponentially with molecular number in an ionic cluster). Even if ionic clusters could be formed in a metastable [61] or stable state [62], the hydration layers near a crystal surface may prevent the direct attachments of these ionic clusters, as explained in Section 3.1.2. Crystallization by the attachment of ionic clusters in calcite crystal growth has not been observed in AFM experiments. Instead, crystallization by classical ionic attachment has been widely reported (the step growth). This situation might be changed when two calcite crystals move closer and form a capillary gap that contains the hydration layers. Ionic clusters may keep bouncing between two walls until they penetrates through water layers. Once ionic clusters enter the hydration layers or an ionic bridge is formed throughout the hydration layers, this will lead to the release of the structured water (hydration water), which will gain in entropy (water has more freedom in bulk than in a hydration layer) [63]. These factors may be the reason for the formation of ionic bridges in the gaps between two calcite crystallites.

Heterogeneous nucleation in a capillary gap can also be applied to understand the formation of ionic bridges. The free energy of the formation of an ionic bridge ($\Delta G$) is given by:

$$
\Delta G=-\mathrm{n} \Delta \mu+\Delta(S \gamma)=-\frac{\Delta \mu}{\Omega} V_{b}+\left[S_{b s} \gamma_{b s}+2 S_{b c}\left(\gamma_{b c}-\gamma_{c s}\right)\right] \tag{1}
$$

where $\gamma_{ij}$ is the surface free energy between $i$ and $j$ phases ($b$ for the ionic bridge, $s$ for the solution, $c$ for crystal); $S_{ij}$ is the surface area between $i$ and $j$ phases; $V_{b}$ is the volume of the bridge phase; $\Omega$ is

the volume per unit of the ionic bridge phase. The chemical potential change for the formation of the ionic bridge phase, $\Delta\mu$, is given by:

$$
\Delta\mu = k_B T ln\left(\frac{K_{IAP}}{K_{sp}}\right) \tag{2}
$$

where $K_{IAP}$ and $K_{SP}$ represent the ionic activity product and the solubility product, respectively; $k_B$ is the Boltzmann constant; and $T$ is the absolute temperature.

In line with the previous work on heterogeneous nucleation on a substrate [64], the interfacial tension terms can be expressed as an effective interfacial tension ($\gamma_{eff}$). Here, we first introduce a factor, $m$, as:

$$
m = \frac{\left(\gamma_{cs} - \gamma_{bc}\right)}{\gamma_{bs}} = \cos(\theta) \tag{3}
$$

Here, $\theta$ is the contact angle (if we consider that the initial new phase has a liquid-like behavior). Now, $\gamma_{eff}$ can be expressed as:

$$
\gamma_{eff} = \left(1 - \frac{2mS_{bc}}{S_{bs}}\right)\gamma_{bs} \tag{4}
$$

For simplicity, we take an ionic bridge as a cylinder between two flat surfaces, as shown in Scheme 1. In such a case, $\theta = \pi/2$ and $m = 0$. Equation (1) can be simplified as:

$$
\Delta G = -\frac{\Delta\mu}{\Omega} V_b + S_{bs}\gamma_{bs}
$$

![](./images/812605511458357249_11.jpg)

Scheme 1. A scheme of the formation of an ionic bridge in the gap between two calcite crystallites.

The volumes of the bridge and surface areas can be determined by their radii $r$ and the gap space $H$. Here, we define a specific height as $h \equiv H/r$, giving:

$$
V_b = \pi r^3 h,\ S_{bs} = 2\pi r^2 h \tag{5}
$$

To obtain the free energy barrier of the formation of the ionic bridge ($\Delta G^{*}_{bridge}$), we get:

$$
\frac{\partial\Delta G}{\partial r} = 0 \tag{6}
$$

By using Equations (1), (4), and (5), we get:

$$
r^{*}_{bridge} = w r^{*} \tag{7}
$$

$$
\Delta G^{*}_{bridge} = f \Delta G^{*} \tag{8}
$$

$$
w = \frac{2}{3},\ f = \frac{2h}{9} \tag{9}
$$

where $r_{bridge}{}^{*}$ is the critical size for bridge formation. Here, $r^{*}$ and $\Delta G^{*}$ are the critical homogeneous nucleation radius and free energy barrier, respectively, which are given by:

$$
r^{*}=\frac{2 \gamma_{b s} \Omega}{\Delta \mu}, \Delta G^{*}=\frac{16 \pi \gamma_{b s}^{3} \Omega^{2}}{3(\Delta \mu)^{2}}
\tag{10}
$$

In comparison, for heterogeneous nucleation of a crystal phase, we have:

$$
\Delta G_{\text {hetero }}^{*}=f \Delta G^{*}, f=\frac{(1-m)^{2}(2+m)}{4}
\tag{11}
$$

Considering the same interfacial relationship as the bridge formation, we get $m=0$ and $f=0.5$. Comparing this with Equation (9), when the specific gap space $h<9 / 4$, a bridge formation in a capillary gap is more likely than that of homogeneous nucleation in solution or heterogeneous nucleation on a crystal surface. This phenomenon can be understood as capillary condensation [65].

In this work, there are about 10-20 rapture events during the separation of two calcites with a contact area of $20 \mu \mathrm{m}^{2}$. Considering that one salt bridge can produce multiple rupture events $(n=2-6$, Figure $5 b)$, the number density of ionic bridges is in the range of $0.2-1 \mu \mathrm{m}^{-2} \mathrm{~min}^{-1}$ (the contacting time is $0.5 \mathrm{~min}$ ), which is comparable to the heterogeneous nucleation rate of calcite on templated substrates $\left(0.2-1.4 \mu \mathrm{m}^{-2} \mathrm{~min}^{-1}\right)$ [66]. This result corroborates the model, showing that salt bridge nucleation is the result of the heterogeneous nucleation in a capillary gap.

Therefore, the rupture events in AFM force measurement can be understood as follows. Ions in a solution can be either enriched at the crystal surface or stochastically aggregated into ionic clusters [61,62]. However, the hydration layer may kinetically hinder the penetration of ion aggregates with the crystal lattice. Ion aggregates may be diffused away from the surface or be dissociated during this period. As the tip and substrate crystallites move closer, ion aggregates can bounce between walls and be confined by the capillary gap. A capillary condensation effect may facilitate the heterogeneous nucleation of mineral clusters, where the initial ionic bridge is formed. Multiple ionic bridges will be formed during the "contacting" period. As the separation of crystallites increases, ionic bridges are elongated and broken, leading to multiple rupture events during force measurements.

### 3.2.3. Capillary Bridges Promoted CPA Process

Several factors were observed to affect the formation of ionic bridges between crystallites. We found that increasing the "contacting" time and the supersaturation leads to the increase of the magnitude of rupture events, which can be understood by the heterogeneous nucleation in a capillary gap. These ionic bridges can facilitate the aggregation of crystallites during crystal growth.

During force measurements, there is an external force that facilitates the contacting of crystallites. However, for suspended colloidal crystallites, there is no such external force. The electrical double layer and the hydration layers may prevent colloidal crystallites moving closer. We found two strategies that can be applied to promote the CPA process. One is to use nanosized crystallites and the other is to use ultrasonic agitation. For the first case, the Brownian motion of a colloidal will be enhanced by reducing the size. Nanosized crystallites increase the collision velocity, which may make them reach a critical gap space where heterogeneous nucleation would happen. We directly observed the formation of bridges between nanogold particles before they had lattice contact with each other [67]. The aggregation-based crystallization of nanovaterite was also observed [68,69]. For the second case, calcite crystallites ay have collided with each other under ultrasonic agitation, resulting in the aggregation of micron-sized calcite crystallites or the attachment of smaller calcite crystallites on a larger calcite surface (Figure 6). The ultrasonic agitation is usually applied to suspend aggregates, but in supersaturated solutions it promotes aggregation. This abnormal phenomenon can be understood as the ionic bridge being facilitated the CPA process.

![](./images/812605511458357249_12.jpg)

Figure 6. Optical images of aggregated calcite crystallites obtained by ultrasonic agitation of calcite suspensions in a supersaturated solution (SI = 1.0): (left) relatively uniform calcite suspension (5–10 µm), captured in suspension; (right) a large calcite (40–100 µm) in a smaller calcite suspension (1–5 µm).

## 4. Conclusions

Experiments involving crystallization via particle attachment have enriched our understanding of crystallization processes, providing new pathways to break through the limitations of classical crystallization. However, the mechanism of attachment is not straight forward. The classical DLVO model is limited at the nanoscale. The hydration layers, the ionic aggregation behaviors near the crystal interface, and the capillary condensation effect have to been taken into account for a better understanding of the mechanism of attachment. As revealed in this work, even for a simple calcite crystallization system, the attachment is not only dependent upon the natural surface properties (electrical double layers and hydration layers), but is also dependent upon the solution condition, particle size, contacting time, and the capillary gap space. Detailed understanding of the mechanism of calcite attachment would allow a better understanding of geological mineral formation, biomineralization, and biomimetic fabrication of materials with hierarchically ordered structures and unlimited patterns by CPA processes.

Author Contributions: Conceptualization and analysis, H.P. and R.T.; methodology and experiments, H.P.; MD simulation, H.P.; writing—original draft preparation, H.P.; writing—review and editing, R.T., supervision, R.T. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Nation Key R&D program of China (2018YFC1105100), the National Natural Science Foundation of China (21771160, 21625105), and the Fundamental Research Funds for the Central Universities (2016QN81020).

Acknowledgments: We thank Jinhui Tao, James J. De Yoreo, and Xiang-Yang Liu for helpful discussions. The computational work was performed in the computing platform provided by the Beijing PARATERA Tech.

Conflicts of Interest: The authors declare no conflict of interest.

## References

1.  Burton, W.K.; Frank, F.C.; Cabrera, N. The growth of crystals and the equilibrium structure of their surfaces. Philos. Trans. R. Soc. Lond. Ser. A 1951, 243, 299–358. [CrossRef]

2.  Hwang, N.-M. Non-classical Crystallization. Ellipsom. Funct. Org. Surf. Film. 2016, 60, 1–20.

3.  De Yoreo, J.J.; Gilbert, P.U.P.A.; Sommerdijk, N.A.J.M.; Penn, R.L.; Whitelam, S.; Joester, D.; Zhang, H.; Rimer, J.D.; Navrotsky, A.; Banfield, J.F.; et al. Crystallization by particle attachment in synthetic, biogenic, and geologic environments. Science 2015, 349, aaa6760. [CrossRef] [PubMed]

4.  DeYoreo, J.J.; Vekilov, P.G. Principles of Crystal Nucleation and Growth. Rev. Mineral. Geochemistry 2003, 54, 57–93. [CrossRef]

5.  Politi, Y.; Metzler, R.A.; Abrecht, M.; Gilbert, B.; Wilt, F.H.; Sagi, I.; Addadi, L.; Weiner, S.; Gilbert, P.U.P.A. Transformation mechanism of amorphous calcium carbonate into calcite in the sea urchin larval spicule. Proc. Natl. Acad. Sci. USA 2008, 105, 17362–17366. [CrossRef] [PubMed]

6.  Liu, Z.; Shao, C.; Jin, B.; Zhang, Z.; Zhao, Y.; Xu, X.; Tang, R. Crosslinking ionic oligomers as conformable precursors to calcium carbonate. Nature 2019, 574, 394–398. [CrossRef]

7.  Shao, C.; Jin, B.; Mu, Z.; Lu, H.; Zhao, Y.; Wu, Z.; Yan, L.; Zhang, Z.; Zhou, Y.; Pan, H.; et al. Repair of tooth enamel by a biomimetic mineralization frontier ensuring epitaxial growth. *Sci. Adv.* 2019, **5**, eaaw9569. [CrossRef]

8.  Yu, Y.; Mu, Z.; Jin, B.; Liu, Z.; Tang, R. Organic–Inorganic Copolymerization for a Homogenous Composite without an Interphase Boundary. *Angew. Chem. Int. Ed.* 2020, **59**, 2071–2075. [CrossRef]

9.  Gower, L.B. Biomimetic Model Systems for Investigating the Amorphous Precursor Pathway and Its Role in Biomineralization. *Chem. Rev.* 2008, **108**, 4551–4627. [CrossRef]

10. Cheng, X.; Varona, P.L.; Olszta, M.J.; Gower, L.B. Biomimetic synthesis of calcite films by a polymer-induced liquid-precursor (PILP) process. *J. Cryst. Growth* 2007, **307**, 395–404. [CrossRef]

11. Cho, K.R.; Kim, Y.-Y.; Yang, P.; Cai, W.; Pan, H.; Kulak, A.N.; Lau, J.L.; Kulshreshtha, P.; Armes, S.P.; Meldrum, F.C.; et al. Direct observation of mineral-organic composite formation reveals occlusion mechanism. *Nat. Commun.* 2016, **7**, 10187. [CrossRef]

12. Kim, Y.-Y.; Ganesan, K.; Yang, P.; Kulak, A.N.; Borukhin, S.; Pechook, S.; Ribeiro, L.; Kröger, R.; Eichhorn, S.J.; Armes, S.P.; et al. An artificial biomineral formed by incorporation of copolymer micelles in calcite crystals. *Nat. Mater.* 2011, **10**, 890–896. [CrossRef] [PubMed]

13. Mao, L.-B.; Gao, H.-L.; Yao, H.-B.; Liu, L.; Cölfen, H.; Liu, G.; Chen, S.-M.; Li, S.-K.; Yan, Y.-X.; Liu, Y.; et al. Synthetic nacre by predesigned matrix-directed mineralization. *Science* 2016, **354**, 107–110. [CrossRef] [PubMed]

14. Cölfen, H.; Antonietti, M. *Mesocrystals and Nonclassical Crystallization*; John Wiley & Sons, Ltd.: Hoboken, NJ, USA, 2008; ISBN 9780470994603.

15. Derjaguin, B.; Landau, L. Theory of stability of highly charged liophobic sols and adhesion of highly charged particles in solutions of electrolytes. *Zhurnal Ekspe. I Teor. Fiz.* 1945, **15**, 663–682.

16. Verwey, E.J.W.; Overbeek, J.T.G.; van Nes, K. *Theory of the Stability of Lyophobic Colloids: The Interaction of Sol Particles Having an Electric Double Layer*; Elsevier: Amsterdam, The Netherlands, 1948.

17. Fenter, P.; Lee, S.S. Hydration layer structure at solid–water interfaces. *MRS Bull.* 2014, **39**, 1056–1061. [CrossRef]

18. Putnis, C.V.; Ruiz-Agudo, E. The Mineral-Water Interface: Where Minerals React with the Environment. *Elements* 2013, **9**, 177–182. [CrossRef]

19. Striolo, A. From Interfacial Water to Macroscopic Observables: A Review. *Adsorpt. Sci. Technol.* 2011, **29**, 211–258. [CrossRef]

20. Wang, J.; Kalinichev, A.G.; Kirkpatrick, R.J. Effects of substrate structure and composition on the structure, dynamics, and energetics of water at mineral surfaces: A molecular dynamics modeling study. *Geochim. Cosmochim. Acta* 2006, **70**, 562–582. [CrossRef]

21. Skinner, H.C.W. Biominerals. *Min. Mag.* 2005, **69**, 621–641. [CrossRef]

22. Gustafsson, J.P. Visual MINTEQ, Stockholm. Available online: https://vminteq.lwr.kth.se/ (accessed on 20 September 2019).

23. Abraham, M.J.; van der Spoel, D.; Lindahl, E.; Hess, B. The GROMACS Development Team, GROMACS User Manual Version 2016.4. Available online: www.gromacs.org (accessed on 5 March 2019).

24. Graf, D.L. Crystallographic tables for the rhombohedral carbonates. *Am. Mineral.* 1961, **46**, 1283–1316.

25. Perry, T.D.; Cygan, R.T.; Mitchell, R. Molecular models of a hydrated calcite mineral surface. *Geochim. Cosmochim. Acta* 2007, **71**, 5876–5887. [CrossRef]

26. Darden, T.; York, D.; Pedersen, L. Particle mesh Ewald: AnN log (N) method for Ewald sums in large systems. *J. Chem. Phys.* 1993, **98**, 10089–10092. [CrossRef]

27. Berendsen, H.J.C.; Postma, J.P.M.; DiNola, A.; Haak, J.R.; Van Gunsteren, W.F. Molecular dynamics with coupling to an external bath. *J. Chem. Phys.* 1984, **81**, 3684. [CrossRef]

28. Bussi, G.; Donadio, D.; Parrinello, M. Canonical sampling through velocity rescaling. *J. Chem. Phys.* 2007, **126**, 14101. [CrossRef] [PubMed]

29. Humphrey, W.; Dalke, A.; Schulten, K. VMD: Visual molecular dynamics. *J. Mol. Graph.* 1996, **14**, 33–38. [CrossRef]

30. Kästner, J.; Thiel, W. Bridging the gap between thermodynamic integration and umbrella sampling provides a novel analysis method: “Umbrella integration”. *J. Chem. Phys.* 2005, **123**, 144104. [CrossRef]

31. Murata, K.; Sugita, Y.; Okamoto, Y. Free energy calculations for DNA base stacking by replica-exchange umbrella sampling. *Chem. Phys. Lett.* 2004, **385**, 1–7. [CrossRef]

32. Kästner, J.; Thiel, W. Analysis of the statistical error in umbrella sampling simulations by umbrella integration. J. Chem. Phys. 2006, 124, 234106. [CrossRef]

33. Kumar, S.; Rosenberg, J.M.; Bouzida, D.; Swendsen, R.H.; Kollman, P.A. THE weighted histogram analysis method for free-energy calculations on biomolecules. I. The method. J. Comput. Chem. 1992, 13, 1011-1021. [CrossRef]

34. Hub, J.S.; De Groot, B.L.; Van Der Spoel, D. g_wham-A Free Weighted Histogram Analysis Implementation Including Robust Error and Autocorrelation Estimates. J. Chem. Theory Comput. 2010, 6, 3713-3720. [CrossRef]

35. Stipp, S.; Eggleston, C.; Nielsen, B. Calcite surface structure observed at microtopographic and molecular scales with atomic force microscopy (AFM). Geochim. Cosmochim. Acta 1994, 58, 3023-3033. [CrossRef]

36. Stipp, S. Toward a conceptual model of the calcite surface: Hydration, hydrolysis, and surface potential. Geochim. Cosmochim. Acta 1999, 63, 3121-3131. [CrossRef]

37. Park, C.; Fenter, P.; Zhang, Z.; Cheng, L.; Sturchio, N.C. Structure of the fluorapatite (100)-water interface by high-resolution X-ray reflectivity. Am. Min. 2004, 89, 1647-1654. [CrossRef]

38. Heberling, F.; Trainor, T.P.; Lützenkirchen, J.; Eng, P.; Denecke, M.; Bosbach, D. Structure and reactivity of the calcite-water interface. J. Colloid Interface Sci. 2011, 354, 843-857. [CrossRef]

39. Pareek, A.; Torrelles, X.; Angermund, K.; Rius, J.; Magdans, U.; Gies, H. Structure of Interfacial Water on Fluorapatite (100) Surface. Langmuir 2008, 24, 2459-2464. [CrossRef] [PubMed]

40. E Wilson, E.; Awonusi, A.; Morris, M.D.; Kohn, D.H.; Tecklenburg, M.M.; Beck, L.W. Highly Ordered Interstitial Water Observed in Bone by Nuclear Magnetic Resonance. J. Bone Min. Res. 2004, 20, 625-634. [CrossRef] [PubMed]

41. Imada, H.; Kimura, K.; Onishi, H. Water and 2-Propanol Structured on Calcite (104) Probed by Frequency-Modulation Atomic Force Microscopy. Langmuir 2013, 29, 10744-10751. [CrossRef]

42. Rode, S.; Oyabu, N.; Kobayashi, K.; Yamada, H.; Kühnle, A. True Atomic-Resolution Imaging of (10$\overline{1}$4) Calcite in Aqueous Solution by Frequency Modulation Atomic Force Microscopy. Langmuir 2009, 25, 2850-2853. [CrossRef]

43. Marutschke, C.; Walters, D.; Cleveland, J.; Hermes, I.; Bechstein, R.; Kuhnle, A. Three-dimensional hydration layer mapping on the (10.4) surface of calcite using amplitude modulation atomic force microscopy. Nanotechnology 2014, 25, 335703. [CrossRef]

44. Dorvee, J.R.; Veis, A. Water in the Formation of Biogenic Minerals: Peeling Away the Hydration Layers. J. Struct. Boil. 2013, 183, 278-303. [CrossRef]

45. Fenter, P.; Kerisit, S.; Raiteri, P.; Gale, J.D. Is the Calcite-Water Interface Understood? Direct Comparisons of Molecular Dynamics Simulations with Specular X-ray Reflectivity Data. J. Phys. Chem. C 2013, 117, 5028-5042. [CrossRef]

46. Zhu, B.; Xu, X.; Tang, R. Hydration layer structures on calcite facets and their roles in selective adsorptions of biomolecules: A molecular dynamics study. J. Chem. Phys. 2013, 139, 234705. [CrossRef] [PubMed]

47. Pan, H.; Tao, J.; Wu, T.; Tang, R. Molecular simulation of water behaviors on crystal faces of hydroxyapatite. Front. Chem. China 2007, 2, 156-163. [CrossRef]

48. Garcia, N.; Raiteri, P.; Vlieg, E.; Gale, J.D. Water Structure, Dynamics and Ion Adsorption at the Aqueous {010} Brushite Surface. Minerals 2018, 8, 334. [CrossRef]

49. Perdikouri, C.; Putnis, C.V.; Kasioptas, A.; Putnis, A. An Atomic Force Microscopy Study of the Growth of a Calcite Surface as a Function of Calcium/Total Carbonate Concentration Ratio in Solution at Constant Supersaturation. Cryst. Growth Des. 2009, 9, 4344-4350. [CrossRef]

50. Stack, A.G.; Grantham, M.C. Growth Rate of Calcite Steps As a Function of Aqueous Calcium-to-Carbonate Ratio: Independent Attachment and Detachment of Calcium and Carbonate Ions. Cryst. Growth Des. 2010, 10, 1409-1413. [CrossRef]

51. Sand, K.K.; Tobler, D.J.; Dobberschütz, S.; Larsen, K.; Makovicky, E.; Andersson, M.P.; Wolthers, M.; Stipp, S. Calcite Growth Kinetics: Dependence on Saturation Index, Ca2+:CO32-Activity Ratio, and Surface Atomic Structure. Cryst. Growth Des. 2016, 16, 3602-3612. [CrossRef]

52. Ruiz-Agudo, E.; Putnis, C.V.; Wang, L.; Putnis, A. Specific effects of background electrolytes on the kinetics of step propagation during calcite growth. Geochim. Cosmochim. Acta 2011, 75, 3803-3814. [CrossRef]

53. Ricci, M.; Spijker, P.; Stellacci, F.; Molinari, J.-F.; Voïtchovsky, K. Direct Visualization of Single Ions in the Stern Layer of Calcite. Langmuir 2013, 29, 2207-2216. [CrossRef]

54. Chernov, A.A.; Parvov, V.F.; Eskin, S.M.; Sipyagin, V.V. Fluctuations and Anomalous Temperature Dependence in the Growth Rates of KA1 (SO4)2• 12H2O and KNO3. In Pocт Кристаллов/Rost Kristallov/Growth of Crystals; Springer: Berlin/Heidelberg, Germany, 1984; pp. 103–107.

55. Bocharov, S.N.; Glikin, A.É. Kinetic anomalies of crystal growth: Development of methodical approaches and interpretations. Cryst. Rep. 2008, 53, 147–153. [CrossRef]

56. Martin-Jimenez, D.; Chacón, E.; Tarazona, P.; Garcia, R. Atomically resolved three-dimensional structures of electrolyte aqueous solutions near a solid surface. Nat. Commun. 2016, 7, 12164. [CrossRef] [PubMed]

57. Labuda, A.; Kobayashi, K.; Suzuki, K.; Yamada, H.; Grütter, P. Monotonic Damping in Nanoscopic Hydration Experiments. Phys. Rev. Lett. 2013, 110, 066102. [CrossRef] [PubMed]

58. Israelachvili, J.N.; Pashley, R.M. Molecular layering of water at surfaces and origin of repulsive hydration forces. Nature 1983, 306, 249–250. [CrossRef]

59. Røyne, A.; Dalby, K.; Hassenkam, T. Repulsive hydration forces between calcite surfaces and their effect on the brittle strength of calcite-bearing rocks. Geophys. Res. Lett. 2015, 42, 4786–4794. [CrossRef]

60. Israelachvili, J.N. Intermolecular & Surface Forces; Academic Press: Cambridge, MA, USA, 1992.

61. Smeets, P.J.M.; Finney, A.R.; Habraken, W.J.E.M.; Nudelman, F.; Friedrich, H.; Laven, J.; De Yoreo, J.J.; Rodger, P.M.; Sommerdijk, N.A.J.M. A classical view on nonclassical nucleation. Proc. Natl. Acad. Sci. USA 2017, 114, E7882–E7890. [CrossRef]

62. Gebauer, D.; Kellermeier, M.; Gale, J.D.; Bergström, L.; Cölfen, H. Pre-nucleation clusters as solute precursors in crystallisation. Chem. Soc. Rev. 2014, 43, 2348–2371. [CrossRef]

63. Budi, A.; Stipp, S.; Andersson, M.P. Calculation of Entropy of Adsorption for Small Molecules on Mineral Surfaces. J. Phys. Chem. C 2018, 122, 8236–8243. [CrossRef]

64. Liu, X.Y. Heterogeneous nucleation or homogeneous nucleation? J. Chem. Phys. 2000, 112, 9949–9955. [CrossRef]

65. Christenson, H.K. Two-step crystal nucleation via capillary condensation. CrystEngComm 2013, 15, 2030. [CrossRef]

66. Hamm, L.M.; Giuffre, A.J.; Han, N.; Tao, J.; Wang, D.; De Yoreo, J.J.; Dove, P.M. Reconciling disparate views of template-directed nucleation through measurement of calcite nucleation kinetics and binding energies. Proc. Natl. Acad. Sci. USA 2014, 111, 1304–1309. [CrossRef]

67. Jin, B.; Sushko, M.L.; Liu, Z.; Jin, C.; Tang, R. In Situ Liquid Cell TEM Reveals Bridge-Induced Contact and Fusion of Au Nanocrystals in Aqueous Solution. Nano Lett. 2018, 18, 6551–6556. [CrossRef] [PubMed]

68. Gehrke, N.; Cölfen, H.; Pinna, N.; Antonietti, M.; Nassif, N. Superstructures of Calcium Carbonate Crystals by Oriented Attachment. Cryst. Growth Des. 2005, 5, 1317–1319. [CrossRef]

69. Liu, Z.; Pan, H.; Zhu, G.; Li, Y.; Tao, J.; Jin, B.; Tang, R. Realignment of Nanocrystal Aggregates into Single Crystals as a Result of Inherent Surface Stress. Angew. Chem. Int. Ed. 2016, 55, 12836–12840. [CrossRef] [PubMed]

![](./images/812605511458357249_13.jpg)

© 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).