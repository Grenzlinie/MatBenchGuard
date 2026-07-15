Accepted Manuscript

Nitridation of the metallic $Mo_2C(001)$ surface from $NH_3$ dissociative adsorption – A DFT Study

Fan Wang, Teng Li, Haijun Jiao

<table>
  <tr>
    <td>PII:</td>
    <td>S0039-6028(19)30392-9</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.susc.2019.121466</td>
  </tr>
  <tr>
    <td>Article Number:</td>
    <td>121466</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>SUSC 121466</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Surface Science</td>
  </tr>
  <tr>
    <td>Received date:</td>
    <td>27 May 2019</td>
  </tr>
  <tr>
    <td>Revised date:</td>
    <td>16 July 2019</td>
  </tr>
  <tr>
    <td>Accepted date:</td>
    <td>16 July 2019</td>
  </tr>
</table>

Please cite this article as: Fan Wang, Teng Li, Haijun Jiao, Nitridation of the metallic $Mo_2C(001)$ surface from $NH_3$ dissociative adsorption – A DFT Study, Surface Science (2019), doi: https://doi.org/10.1016/j.susc.2019.121466

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

![](./images/812753807439036417_1.jpg)

### Highlights

- Coverage dependent NH₃ dissociative adsorption on metallic Mo₂C(001) was computed
- NH₃ dissociative adsorption is exothermic and thermodynamically favorable
- NH₃ adsorption prefers top site; and the adsorption of NH and N prefers hollow site
- NH₂ adsorbs at bridge and hollow sites at low coverage; but bridge site at high coverage
- Saturation coverage of NH₃, NH₂, NH and N using NH₃ is 0.75, 1.0, 1.0 and 0.5 ML

# Nitridation of the metallic $\text{Mo}_2\text{C}(001)$ surface from $\text{NH}_3$ dissociative adsorption – A DFT Study

Fan Wang, $^{a}$ Teng Li$^{b,c}$ and Haijun Jiao$^{a,b}$

a) Leibniz-Institut für Katalyse e.V. an der Universität Rostock, Albert-Einstein Strasse 29a, 18059 Rostock, Germany. b) State Key Laboratory of Coal Conversion, Institute of Coal Chemistry, Chinese Academy of Sciences, Taiyuan, 030001, China; c) University of Chinese Academy of Sciences, No. 19A Yuquan Road, Beijing, 100049, China; E-Mail: haiju.jiao@catalysis.de

Dedicated to Prof. Dr. Jean-François Halet on the occasion of his 60th birthday

## Abstract
Adsorption and sequential decomposition of ammonia on the metallic $\text{Mo}_2\text{C}(001)$ surface have been systematically computed using periodic density functional theory under the consideration of van der Waals dispersion correction (PBE-D3). It is found that $\text{NH}_3$ adsorption prefers the top sites from low to saturation coverage. For the adsorption of surface $\text{NH}_2$, bridge and hollow sites are possible at low coverage and only bridge sites are preferred at high coverage up to saturation. The adsorption of surface NH and N prefers the hollow sites. Sequential decomposition of $\text{NH}_3$ into surface $\text{NH}_2$, NH and N has low barrier and is highly exothermic. On the basis of surface Mo atoms, the saturation coverage of surface $\text{NH}_3$, $\text{NH}_2$, NH and N by using $\text{NH}_3$ as nitridation agent is 0.75, 1.0, 1.0 and 0.5 monolayer, respectively. These results provide the basis for the study of surface properties and catalytic reaction of nitrided $\text{Mo}_2\text{C}$ surfaces. The dissociative adsorption of ammonia among others metals and molybdenum nitrides has been categorized and compared.

Keywords: Molybdenum carbide; ammonia dissociative adsorption; nitridation; coverage-dependence; DFT

## INTRODUCTION

Transition metal carbides have found wide industrial applications due to their extraordinary physical and chemical properties and attracted broad interests in academia and applied research.[1-5] One of the promising applications is transition metal carbides based heterogeneous catalysis and the prominent examples are molybdenum ($Mo_2C$) and tungsten ($W_2C$) carbides as potential substitutes of noble metals catalysts following the pioneering work of Levy and Boudart in 1973.[6] It has been demonstrated that $Mo_2C$ based catalysts are effective in reactions typically catalyzed by noble metals, such as water-gas shift reaction,[7, 8] CO hydrogenation to alcohols,[9, 10] hydrodesulfurization,[11] hydrodenitrogenation in petroleum refining,[12] hydro-treating,[13, 14] hydrogen production[15] and electro-catalysis and electro-chemistry.[16-21]

Catalytic synthesis and decomposition of ammonia are important reactions in science and technology, for example, in producing $CO_x$-free hydrogen,[22-24] and in purifying fuel from the air-blown gasification of coal.[25] During these reactions, the nature of metal-nitrogen interaction plays a decisive role in determining the catalytic activity.[26, 27] Experimentally, $Mo_2C$ catalyzed ammonia synthesis and decomposition had been reported. For instance, Oyama found the performance of $Mo_2C$ and other interstitial alloys to be similar to that of group VIII noble metals in ammonia synthesis.[28] Choi found that $Mo_2C$ is active in ammonia decomposition and can be used as substitutes for precious metal catalysts in petrochemical processes.[29] Recent study by Schlögl et al.,[30] showed the excellent catalytic activity of $Mo_2C$ in ammonia decomposition and computed molybdenum nitride formation under $NH_3$ atmosphere. They found that $Mo_2C(0001)$ (space group $P6_3/mmc$) having more adsorption sites is more active than $MoN(0001)$ (space group $P\bar{6}m2$) having less adsorption sites in $NH_3$ decomposition, although the binding energy of N is stronger over MoN than over $Mo_2C$.

In addition to the experimental work, computational studies of the adsorption and decomposition of ammonia on various metals such as Fe, Co and Ni are reported.[31-33] Very recent DFT study focused on the stepwise decomposition of ammonia on the $Mo_2N(100)$ and $Mo_2N(111)$ surfaces and illustrated the contributions of individual step to overall process.[34] As one of the most important transition metal carbides, there are no reports about ammonia decomposition on $Mo_2C$ surfaces. Previously studies mainly focused on surface structures and properties of various $Mo_2C$ surfaces;[35, 36] the adsorption and activation of small molecules,[37-41] and the catalytic mechanisms of the dehydrogenation of formic acid,[42] and hydrogenation of furfural [43] and hydrodeoxygenation of carboxylic acid.[44] In this work, we discussed the coverage-dependent dissociative adsorption of ammonia on the $Mo_2C(001)$ surface and the subsequent nitridation by using $NH_3$.

## METHOD AND MODEL

Method: All calculations were done by using the plane-wave based density functional theory (DFT) method implemented in the Vienna ab initio simulation package (VASP).[45, 46] The effect of the core electrons was taken into account by the projector augmented wave method (PAW).[47, 48] The electron exchange and correlation energy is treated within the generalized gradient approximation (GGA) in the Perdew-Burke-Ernzerhof functional (PBE).[49] In this study, we included van der Waals dispersion correction by employing the latest D3 method with Becker-Jonson damping.[50, 51] To have accurate energy with errors less than 1 meV per atom, a cutoff energy of 400 eV and the Gaussian electron smearing method with $\sigma$ = 0.10 eV were used. Geometry optimization was converged until forces acting on atoms were smaller than 0.02 eV/Å, whereas the energy threshold-defining self-consistency of electron density was set to $10^{-4}$ eV. All transition state structures were optimized by using the climbing image nudged elastic band (CI-NEB) method,[52] and the frequency analysis was also processed to verify an authentic transition state having only one imaginary frequency and provides zero-point energy (ZPE). For the bulk structure, the lattice parameters of the hexagonal phase were determined by minimizing the total energy of the unit cell by using a conjugated-gradient algorithm to relax the ions and a 5×5×5 Monkhorst-Pack k-point grid[39] was used for sampling the Brillouin zone.

Model: $Mo_2C$ can have orthorhombic [53, 54] or hexagonal [55-57] crystalline phase depending on the carburization conditions. In our work, we used the hexagonal $Mo_2C$ phase with an eclipsed configuration as the unit cell.[58] The calculated lattice

~ 3 ~

parameters of the cell are $2a = 6.277$ Å, $2b = 6.070$ Å and $c = 4.722$ Å, in good agreement with the experimental values ($a = b = 3.011$ Å, $c = 4.771$ Å).[59] We used a periodic p(2×2) slab with a surface area of 12.2×12.1 Å and a six-layer model with the top three layers relaxed and the bottom three layers fixed in the bulk positions. This has been tested in previous studies.[37, 39]

The adsorption energy ($E_{\text{ads}}$) is defined according to $E_{\text{ads}} = E(\text{X/slab}) - [E(\text{X}) + E(\text{slab})]$, where $E(\text{X/slab})$ is the total energy of the slab with one X molecule, $E(\text{slab})$ is the total energy of the bare slab and $E(\text{X})$ is the total energy of a free X molecule in gas phase, and therefore the more negative the $E_{\text{ads}}$ the stronger the adsorption. To get the saturation coverage ($\text{X} = \text{NH}_3$), we used the stepwise adsorption energy, $\Delta E_{\text{ads}} = E(\text{X})n+1/\text{slab} - [E(\text{X})n/\text{slab} + E(\text{X})]$, where a positive $\Delta E_{\text{ads}}$ for n+1 adsorbed X molecules indicates the saturation adsorption with n adsorbed X molecules. The barrier ($E_{\text{a}}$) and reaction energy ($\Delta E_{\text{r}}$) are calculated according to $E_{\text{a}} = E_{\text{TS}} - E_{\text{IS}}$ and $\Delta E_{\text{r}} = E_{\text{FS}} - E_{\text{IS}}$, where $E_{\text{IS}}$, $E_{\text{FS}}$ and $E_{\text{TS}}$ are the energies of the corresponding initial state (IS), final state (FS), and transition state (TS), respectively. The reaction energies and barriers include the ZPE obtained from frequency analysis.[60]

## RESULTS AND DISCUSSION

Figure 1 shows the schematic side and top views of the metallic $\text{Mo}_2\text{C}(001)$ surface, which has sixteen surface Mo atoms and ten possible adsorption sites (**t1, t2, b1-b4** and **h1-h4**). On **t1** site the $\text{Mo}_1$ atom binds two C atoms in the second layer and has one dangling bond (saturated bulk Mo binds three C atoms, saturated bulk C atom binds six Mo atoms); and on **t2** site the $\text{Mo}_2$ atom binds with only one C atom in the second layer and has two dangling bonds. The **b1** site links two $\text{Mo}_1$ atoms; the **b2** site links one $\text{Mo}_1$ and one $\text{Mo}_2$; the **b3** site links two $\text{Mo}_2$ atoms; the **b4** site links one $\text{Mo}_1$ and one $\text{Mo}_2$ sharing one second layer C atom. For the 3-fold hollow sites (**h1-h4**), they differ in not only surface Mo atoms but also sublayer atoms. The **h1** site has one $\text{Mo}_1$ and two $\text{Mo}_2$ as well as one vacancy in the second layer. The **h2** site has two $\text{Mo}_1$, one $\text{Mo}_2$ and one third layer Mo atom. The **h3** site has two $\text{Mo}_1$, one $\text{Mo}_2$ and one second-layer C atom. The **h4** site has one $\text{Mo}_1$, two $\text{Mo}_2$ and one third layer Mo atom.

![](./images/812753807439036417_2.jpg)

Figure 1. Top (a) and side (b) views of the metallic $\text{Mo}_2\text{C}(001)$ surface with possible adsorption sites (green balls for Mo atoms, gray balls for first layer C atoms and black balls for C atoms in other layers, $\text{t}$ for top, $\text{b}$ for bridge and $\text{h}$ for 3-fold hollow sites)

### (a) $\text{NH}_3$ adsorption:
The adsorption of one $\text{NH}_3$ on the ten possible adsorption sites was computed, and five stable adsorption configurations are located (Figure S1). The **t1** site has the strongest adsorption energy (−1.30 eV) and the second most stable adsorption configuration is at the **t2** site (−1.10 eV); while the adsorption configurations at the bridge (**b1**; −0.91 and **b3**; −0.66 eV) and hollow (**h2**; −0.71 eV) sites are higher in energy and less stable. That the **t1** site is more preferred over the **t2** site is due to their local difference in electronic property, i.e.; the **t1** site with two second layer carbons atoms is more positively charged than the **t2** site with only one second layer carbons atom (0.625 vs. 0.419 e) according to Bader charge analysis.[61-64] That $\text{NH}_3$ prefers the top site is due to its electron lone pair at the N center, which represents the highest occupied molecular orbital. Following this energetic order (**t1 > t2 > b1 > h2 > b3**), we computed $\text{NH}_3$ adsorption at high coverage.

~ 4 ~

For studying $\text{NH}_3$ adsorption at high coverage we further increased the number of $\text{NH}_3$ molecules one by one at remote sites to minimize the lateral repulsive intermolecular interaction, where we considered the most stable adsorption configuration at individual coverage by considering different possibilities on the basis of the above discussed energetic order, while adsorption configurations with adjacently adsorbed $\text{NH}_3$ molecules are computed for comparison. It is found that the stable adsorption configuration does not exactly follow this energetic order. The more stable adsorption configurations are shown in Figure 2 and the less stable adsorption configurations are given in Supporting Information (Figure S2), which shows clearly that the remote adsorption configurations are more stable than the adjacent ones, particularly at low coverage ($n$ = 2-6). For example, the adsorption configuration of three $\text{NH}_3$ molecules at three adjacent $\boldsymbol{\text{t1}}$ sites in a line is less stable than that at three remote $\boldsymbol{\text{t1}}$ sites by 0.18 eV.

![](./images/812753807439036417_3.jpg)

Figure 2. Stepwise adsorption configurations and energies ($\Delta E_{\text{ads}}$) of $\text{NH}_3$ molecules on the metallic $\text{Mo}_2\text{C}(001)$ surface (blue balls for N atoms and white balls for H atoms, using gaseous $\text{NH}_3$ as reference)

For $n$ = 1-8, the adsorbed $\text{NH}_3$ molecules are located at $\boldsymbol{\text{t1}}$ sites and the stepwise adsorption energy decreases gradually, and at the same time, the distance between N-Mo increases gradually (Table S1). For $n$ = 8, all eight $\boldsymbol{\text{t1}}$ sites are occupied. On the basis of $n$ = 8, further $\text{NH}_3$ molecules are adsorbed one by one. That the $\boldsymbol{\text{t1}}$ site is more preferred than the $\boldsymbol{\text{t2}}$ site can also be found at high coverage, for example, for $n$ = 7 with one $\text{NH}_3$ at the $\boldsymbol{\text{t2}}$ site is less stable than that with all $\text{NH}_3$ at the $\boldsymbol{\text{t1}}$ sites by 0.12 eV; and for $n$ = 8 with two $\text{NH}_3$ molecules at the $\boldsymbol{\text{t2}}$ site is less stable than that with all $\text{NH}_3$ molecules at the $\boldsymbol{\text{t1}}$ site by 0.19 eV, despite the adjacent $\text{NH}_3$ in two parallel lines (Figure S2).

For $n$ = 9-12, all $\text{NH}_3$ molecules are located at $\boldsymbol{\text{t2}}$ site and the stepwise adsorption energy decreases. For $n$ = 10, however, the stepwise adsorption energy is slightly higher than that of $n$ = 9; and this disorder remains despite various variations of the adsorption configurations; and one feature is the head-to-head H-H distance for $n$ = 10 and no such feature can be found in other adsorption configurations. Analysis of charge density does not give any reasonable explanations (Figure S3). The saturation coverage has twelve adsorbed $\text{NH}_3$ molecules, since a positive adsorption energy is found for $n$ = 13, where the added $\text{NH}_3$ molecule desorb from the surface. For $n$ = 12, all eight $\boldsymbol{\text{t1}}$ and four $\boldsymbol{\text{t2}}$ sites are occupied.

(b) $\text{NH}_2$ adsorption: Different from $\text{NH}_3$, $\text{NH}_2$ has two electronic configurations,[65] the more stable one ($^2\text{B}_1$) has the single electron perpendicular to the molecular plane and the lone pair electron in the molecular plane and the less stable one ($^2\text{A}_1$) has the single electron in the molecular plane and the lone pair electron perpendicular to the molecular plane. For one $\text{NH}_2$ adsorp-

~ 5 ~

tion on the ten possible adsorption sites, five stable adsorption configurations were found (Figure S4). In contrast to NH₃, the adsorption configurations at **b2**, **h1** and **h2** sites are very close in energy (-5.06, -5.04 and -5.05 eV, respectively) and that at **t2** (-4.22 eV) and **b4** (-4.86 eV) sites are higher in energy and less stable. In these stable adsorption configurations, the NH₂ plane is nearly perpendicular to the surface. It is also noted that no stable adsorption configuration at **t1** site can be located.

Following this stability order (Figure S4), we computed NH₂ adsorption at high coverage, but such negligible energy differences among **b2**, **h1** and **h2** sites make the search for the more or most stable adsorption configurations difficult. Since **h1** and **h2** sites share one **b2** site, small displacement will shift **b2** adsorption either to **h1** or **h2**. For comparison we tentatively computed the adsorption configurations for $n=4$ remotely at **h1** and **h2** sites. After structure optimization, the adsorption configuration at **h1** becomes that of **b2**, and that of **h2** is more stable than **b2** by 0.19 eV (Figure S5). Detailed comparison shows that the adsorption configuration at **h2** site can be considered as tilted **b2** site on the basis of the Ni-Mo distances (2.184, 2.244 and 2.500Å). For further comparison we computed the adsorption configurations for $n=12$ at **h1** and **b4**, **h2** and **b4** as well as **b2** and **b4** sites; and they are very close in energy within 0.03 eV (Figure S6). This indicates their structure flexibilities. To obtain the most stable configuration at individual coverage, we further calculated and compared different NH₂ coverage on Mo₂C(001) surface on both **b2** and **h2** sites by considering different possibilities (Figure S7 and S8). The most stable adsorption configurations at individual coverage with stepwise adsorption energies are summarized in Figure 3. For $n=1$-$8$, **h2** sites are preferably adsorbed close to **b2** site, and the stepwise adsorption energies are in close range of $n=2$-$4$, and that for $n=5$, $7$ and $8$ decreases. Apart from $n=1$ and $8$, where the adsorbed NH₂ are located at **b2** sites, other adsorption configurations have NH₂ at **h2** or tilted **b2** sites. On the basis of the adsorption configuration of $n=8$, stepwise NH₂ adsorption at **b4** sites is computed and the stepwise adsorption decreases from $n=9$-$12$. At $n=16$, all **b2** and **b4** sites are occupied.

![](./images/812753807439036417_4.jpg)

Figure 3. Structures and energies ($\Delta E_{ads}$/eV) of the most stable adsorption sites for stepwise NH₂ adsorption on Mo₂C(001) surface blue balls for N atoms and white balls for H atoms; using gaseous NH₂ radical as reference

(c) NH adsorption: NH radical can have several electronic configurations,[66] and the ground state has a triplet state and the singlet state is much high in energy and less stable. For one NH adsorption (Figure S9), five stable adsorption configurations were found. The adsorption configuration at **h1** site is most stable (-8.08 eV), followed by that at **h2**, **h3** and **h4** sites (-7.91,-7.46 and -7.78 eV, respectively); and that at **t1** site is much high in energy and less stable (-6.57 eV). In these adsorption configurations, NH is perpendicular to the surface. It is noted that no stable adsorption configurations at the bridge sites can be found.

Having the most stable adsorption configuration at the **h1** site, high coverage NH adsorption in remote sites has been computed (Figure 4). From *n* = 1-4, the stepwise adsorption energies are close and those of *n* = 5-8 are also close, but somewhat lower than that for *n* = 1-4. For *n* = 8 (Figure S10), we computed the adsorption configurations at **h2**, **h3** and **h4** sites; and they are higher in energy and less stable than that at **h1** site by 0.33, 2.68 and 5.90 eV, respectively.

![](./images/812753807439036417_5.jpg)

Figure 4. Structures and energies ($\Delta E_{ads}$/eV) of the most stable adsorption sites for stepwise NH adsorption on $Mo_2C(001)$ surface (blue balls for N atoms and white balls for H atoms; using gaseous NH radical as reference)

(d) Adsorption of N. For the adsorption of an N atom, only hollow sites adsorption configurations are found (Figure 5). The most stable one is at **h1** site (-2.67 eV), followed tightly by those at **h2** and **h4** sites (-2.14 and -2.08 eV) and that at **h3** site is least stable (-1.52 eV). Following this energetic order, we computed N adsorption at high coverage. The stepwise adsorption energy for *n* = 1-4 are close; and that for *n* = 5-8 decreases with coverage increase. Significant low stepwise adsorption energies are found for *n* = 9-12, while those for *n* = 13-16 are positive, indicating that thermodynamically it is not possible to occupy all hollow site by using molecular $N_2$ gas as nitridation agent.

![](./images/812753807439036417_6.jpg)

Figure 5. Structures and energies ($\Delta E_{ads}$/eV) of the most stable adsorption sites for stepwise N adsorption on Mo₂C(001) surface (blue balls for N atoms; using gaseous N₂ as reference)

(e) NH₃ Dissociative Adsorption. In addition to molecular adsorption, NH₃ dissociative adsorption on the Mo₂C(001) surface is computed for understanding the nitridation process, where we used the most stable adsorption sites of NH₃, NH₂, NH and N discussed above, and the most stable adsorption sites of hydrogen were taken from previous report (Figure S11).[37, 39] The structures of the IS, TS and FS of each step are shown in Figure S12. The potential energy surface of NH₃ successive dissociation is shown in Scheme 1.

![](./images/812753807439036417_7.jpg)

Scheme 1. Potential energy surface of NH₃ dissociative adsorption on Mo₂C(001) surface

Starting from NH₃ at the **t1** site, the first step is NH₃ dissociation into NH₂ and H (NH₃ = NH₂+H); and this step has barrier of 0.63 eV and is exothermic by 1.13 eV. That the dissociation barrier is lower than the adsorption energy reveals that NH₃ prefers dissociation. In the transition state (**TS1**, Figure S12), the breaking N-H distance is 1.543 Å and the forming NH₂ group is at the **b1** site with N-Mo distances of 2.916 and 2.111 Å; and the H atom is at the **b2** site with N-Mo distance of 2.621 and 1.645 Å. In the final state (FS1, Figure S12), the NH₂ group is at the **b1** site and the H atom is at the **h1** site. After the dissociation, both NH₂ and H migrate to the more stable remote sites, i.e.; the **b2** site for NH₂ and another **h1** site for the H atom (IS2, Figure S12), and the migration of the NH₂ and H species is exothermic by 0.64 eV, and the overall first decomposition step of NH₃ dissociative adsorption at the **t1** site is therefore exothermic by 1.77 eV.

Starting from NH₂ at the **b2** site, the second dissociation step (NH₂+H = NH+2H) is also favorable thermodynamically (−1.17 eV) and has much low barrier of 0.33 eV. The breaking N-H distance in the transition state (**TS2**, Figure S12) is 1.432 Å, and the NH group is at the **h1** site with N-Mo distances of 2.180, 2.180 and 2.097 Å; and the H atom is tilted at **b2** site. After the dissociation, the formed H atom at the **h1** site migrates to another **h1** site; and this is exothermic by 0.04 eV (FS2, Figure S12). Totally, the second dissociation step is exothermic by 1.21 eV.

The last step of NH dissociation into N and H (NH+2H = N+3H) has barrier of 0.77 eV and is exothermic by 1.01 eV. The higher barrier of this step is due to the perpendicular adsorption configuration of NH on the surface. The breaking N-H distance in the transition state (**TS3**, Figure S12) is 1.314 Å and the N-Mo distances are 2.048, 2.058 and 2.013 Å at **h1** site. The dissociated H atom migrates by exothermic 0.13 eV, and the total reaction is exothermic by 1.14 eV for the last step.

On the basis of the stepwise decomposition, we evaluated the stepwise H₂ evolution (Scheme 1). The desorption energies of 0.5 H₂, 1.0 H₂ and 1.5 H₂ is 1.15, 2.27 and 3.41 eV, respectively; and this corresponds to the computed adsorption energy of one H atom on the clean surface (−1.15 eV).[37, 39] This indicates that all these hydrogen atoms are adsorbed on the surface because of the rather low coverage. Therefore, we computed the coverage-dependent H₂ evolution on the basis of the high coverage adsorbed NH₂, NH and N reported above; and such coverage-dependent H₂ evolution can also provide useful information about the nitridation process by using NH₃; and this is particularly interesting since transition-metal nitrides can be used widely as catalysts in hydro-treating reactions.[67, 68]

![](./images/812753807439036417_8.jpg)

Figure 6. Stepwise adsorption energies of NH₃ (a); NH₂ (b); NH (c) and N (d) at high coverage by using NH₃ as nitridation agent. The calculated equation: $\Delta E(\text{NH}_x) = E[(\text{NH}_x)_n/\text{slab}] - E[(\text{NH}_x)_{n-1}/\text{slab}] - (E[\text{NH}_3] - (3 - X)/2E[\text{H}_2])$, for x = 3, 2, 1, 0

Different from above discussed NHₓ (x = 0, 1, 2, 3) coverages on Mo₂C(001) by using the corresponding gaseous radical as reference, we calculated the saturation of coverage for each NHₓ intermediate by using gaseous NH₃ as nitridation agent (Figure

~ 9 ~

6). The saturation coverage of NH₃, NH₂, NH and N can have 12, 16, 16 and 8 surface species, respectively or 0.75, 1.0, 1.0 and 0.5 monolayer coverage on the basis of the exposed surface Mo atoms. The saturation coverage of NH₂ and NH by using gaseous NH₃ is the same as that by using the NH₂ and NH radical, respectively. The saturation coverage using gaseous N₂ can have 12 N atoms (0.75 ML) on the surface; while can have 8 N atoms (0.5 ML) using gaseous NH₃.

On the basis of these results and the available literature data (Table 1), one can compare the metal and surface dependent NH₃ decomposition. As listed in Table 1, four types of reactions can be categorized. The first type is the full decomposition, in which all three elementary steps ($\ce{NH3 = NH2 + H}$; $\ce{NH2 = NH + H}$; $\ce{NH = N + H}$) are exothermic, and this can be found on the Mo₂C(001), Fe(110) and Fe(100) surfaces. The second type has partial decomposition, in which the first two elementary steps are exothermic and the last step is endothermic or close to thermal neutral, such as on the Co(111) and Ni(111) surfaces. The third type has also partial decomposition, but the first step is exothermic and the second and third steps are endothermic, such as on the Ni(110) and Ir(100). The clear surface dependence is shown between Ni(111) and Ni(110) surfaces. The last type shows that all three elementary steps are endothermic, such as on the Pd(111) and Cu(111) surfaces. On the CoO(100) surface, NH₃ does not decompose and all three elementary steps are endothermic and have extremely high barriers. In addition, surface dependent activity is also found on the γ-Mo₂N(100) and γ-Mo₂N(111) surfaces, i.e.; NH₃ decomposes hardly on the γ-Mo₂N(100) surface, but very easily and fully on the γ-Mo₂N(111) surface, like on the Mo₂C(001), Fe(110) and Fe(100) surfaces.

<table>
<caption>Table 1. Comparison of the calculated barriers ($E_a$, eV) and reaction energy ($\Delta E_r$, eV) for each decomposition step of NH₃</caption>
<thead>
<tr>
<th rowspan="2">Surface</th>
<th rowspan="2">$E_{ads}$(eV)</th>
<th colspan="2">$\ce{NH3 = NH2 + H}$</th>
<th colspan="2">$\ce{NH2 + H = NH + 2H}$</th>
<th colspan="2">$\ce{NH + 2H = N + 3H}$</th>
</tr>
<tr>
<th>$E_a$(eV)</th>
<th>$\Delta E_r$(eV)</th>
<th>$E_a$(eV)</th>
<th>$\Delta E_r$(eV)</th>
<th>$E_a$(eV)</th>
<th>$\Delta E_r$(eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mo₂C(001)</td>
<td>−1.30</td>
<td>0.63</td>
<td>−1.13</td>
<td>0.33</td>
<td>−1.17</td>
<td>0.77</td>
<td>−1.01</td>
</tr>
<tr>
<td>Fe(110)[32]</td>
<td>−0.83</td>
<td>0.72</td>
<td>−0.62</td>
<td>0.24</td>
<td>−1.11</td>
<td>1.16</td>
<td>−0.43</td>
</tr>
<tr>
<td>Fe(100)[69]</td>
<td>−0.92</td>
<td>0.95</td>
<td>−0.29</td>
<td>1.14</td>
<td>−0.32</td>
<td>0.78</td>
<td>−0.52</td>
</tr>
<tr>
<td>Co(111)[32]</td>
<td>−0.68</td>
<td>1.01</td>
<td>−0.14</td>
<td>0.21</td>
<td>−0.44</td>
<td>1.06</td>
<td>0.10</td>
</tr>
<tr>
<td>Ni(111)[32]</td>
<td>−0.75</td>
<td>1.11</td>
<td>−0.28</td>
<td>0.59</td>
<td>−0.57</td>
<td>1.11</td>
<td>0.06</td>
</tr>
<tr>
<td>Ni(110)[70]</td>
<td>−0.80</td>
<td>0.80</td>
<td>−0.25</td>
<td>1.41</td>
<td>0.54</td>
<td>0.70</td>
<td>0.29</td>
</tr>
<tr>
<td>Ir(100)[71]</td>
<td>−0.96</td>
<td>0.86</td>
<td>−0.55</td>
<td>1.02</td>
<td>−0.04</td>
<td>0.96</td>
<td>0.33</td>
</tr>
<tr>
<td>Pd(111)[72]</td>
<td>−0.84</td>
<td>1.71</td>
<td>0.49</td>
<td>1.54</td>
<td>0.15</td>
<td>1.70</td>
<td>0.71</td>
</tr>
<tr>
<td>Cu(111)[73]</td>
<td>−0.46</td>
<td>1.67</td>
<td>0.65</td>
<td>1.35</td>
<td>0.76</td>
<td>1.98</td>
<td>1.55</td>
</tr>
<tr>
<td>CoO(100)[74]</td>
<td>−0.61</td>
<td>3.13</td>
<td>0.89</td>
<td>3.40</td>
<td>1.62</td>
<td>3.03</td>
<td>1.10</td>
</tr>
<tr>
<td rowspan="3">γ-Mo₂N(100)[34]</td>
<td rowspan="3">−0.97</td>
<td>1.20</td>
<td>0.02</td>
<td>1.18</td>
<td>−0.12</td>
<td>1.04</td>
<td>0.40</td>
</tr>
<tr>
<td>1.28</td>
<td>0.30</td>
<td>1.18</td>
<td>0.29</td>
<td>2.05</td>
<td>0.69</td>
</tr>
<tr>
<td>1.31</td>
<td>0.80</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td rowspan="2">γ-Mo₂N(111)[34]</td>
<td rowspan="2">−1.18</td>
<td>0.64</td>
<td>−0.89</td>
<td>0.22</td>
<td>−1.09</td>
<td>1.12</td>
<td>−0.11</td>
</tr>
<tr>
<td>0.78</td>
<td>−0.58</td>
<td>0.46</td>
<td>−0.97</td>
<td>1.14</td>
<td>−0.04</td>
</tr>
</tbody>
</table>

## CONCLUSION

Density functional theory computations were carried out to study the adsorption and sequential decomposition of ammonia on the hexagonal metallic Mo₂C(001) surface. The ultimative goal of this study is the nitridation degree of the Mo₂C(001) surface by using NH₃ as environment agent. The metallic Mo₂C(001) surface has two types of Mo atoms differentiated by the local carbon environment, the Mo atom with two carbon atoms has higher NH₃ adsorption energy than that with one carbon atom; and each type has eight expose Mo atoms.

The adsorption of NH₃ prefers the top site via the nitrogen lone pair electrons in the entire coverage range, and the saturation coverage is 0.75 monolayer on the basis of exposed surface Mo atoms. There is no hydrogen bonding among the adsorbed NH₃ moleucles. It is found that NH₃ prefers decomposition instead of desorption, and all three elementary decomposition steps have low barries and are exothermic; and this shows that full decomposition into surface N and H atoms are favored kinetically and thermodynamically.

The adsorption of $NH_2$ is coverage-dependent; i.e.; at low coverage $NH_3$ adsorption at both bridge and hollow sites have close energies, and bridge sites are preferred at high coverage up to saturation; and the saturation coverage is 1.0 monolayer. In contrast, the adsorption of NH and N is coverage independent, and only hollow sites are preferred in the entire coverage range. The saturation coverage for NH and N is 1.0 and 0.5 monolayer, respectively.

The dissociative adsorption of ammonia among others metals and molybdenum nitrides has been categorized and compared. Our results provide the basis for studying the surface properties and catalytic reaction of nitrided $Mo_2C$ surfaces.

## Supporting Information
Adsorption structures and energies of $NH_3$ at different sites (Figures S1-S3), $NH_2$ at different sites (Figures S4-S8), NH at different sites (Figure S9 and S10) and H at different sites (Figure S11); transition state structures of $NH_3$ sequential decomposition (Figure S12); Mo-N distances of $NH_3$ remote (Table S1) and adjacent adsorption (Table S2).

## Acknowledgements
F. Wang thanks the support of the China Scholarship Council (CSC); and the general financial support from the BMBF and the state of Mecklenburg-Vorpommern, Germany, is acknowledged.

## REFERENCE
[1] L.E. Toth, Transition Metal Carbides and Nitrides, Academic Press, New York and London, 1971.
[2] A.L.I. V. A. Gubanov, V. P. Zhukov, Electronic Structure of Refractory Carbides and Nitrides, Cambridge University Press, 1994.
[3] S.T. Oyama, The Chemistry of Transition Metal Carbides and Nitrides, Blackie Academic & Professional, an important of Chapman & Hall, Wester Cleddens Road, Bishopbriggs, Glasgow G64 2NZ, 1996.
[4] J.G. Chen, J. Eng, S.P. Kelty, Catal. Today 43 (1998) 147-158.
[5] H.H. Hwu, J.G. Chen, Chem. Rev. 105 (2005) 185-212.
[6] R.B. Levy, M. Boudart, Science 181 (1973) 547.
[7] M. Nagai, K. Matsuda, Journal of Catalysis 238 (2006) 489-496.
[8] J.A. Schaidle, A.C. Lausche, L.T. Thompson, Journal of Catalysis 272 (2010) 235-245.
[9] M. Xiang, D. Li, W. Li, B. Zhong, Y. Sun, Fuel 85 (2006) 2662-2665.
[10] S. Zaman, K.J. Smith, Catalysis Reviews 54 (2012) 41-132.
[11] V. Sundaramurthy, A.K. Dalai, J. Adjaye, Applied Catalysis B: Environmental 68 (2006) 38-48.
[12] H.A. Al-Megren, S.L. González-Cortés, T. Xiao, M.L.H. Green, Appl. Catal., A 329 (2007) 36-45.
[13] M.K. Neylon, S. Choi, H. Kwon, K.E. Curry, L.T. Thompson, Appl. Catal., A 183 (1999) 253-263.
[14] S.J. Ardakani, X. Liu, K.J. Smith, Appl. Catal., A 324 (2007) 9-19.
[15] R. Barthos, F. Solymosi, Journal of Catalysis 249 (2007) 289-299.
[16] R. Jiang, J. Fan, L. Hu, Y. Dou, X. Mao, D. Wang, Electrochim. Acta 261 (2018) 578-587.
[17] C. Wan, B.M. Leonard, Chem. Mater. 27 (2015) 4281-4288.
[18] K. Zhang, Y. Zhao, D. Fu, Y. Chen, Journal of Materials Chemistry A 3 (2015) 5783-5788.
[19] W.F. Chen, C.H. Wang, K. Sasaki, N. Marinkovic, W. Xu, J.T. Muckerman, Y. Zhu, R.R. Adzic, Energy & Environmental Science 6 (2013) 943-951.
[20] L. Liao, S. Wang, J. Xiao, X. Bian, Y. Zhang, M.D. Scanlon, X. Hu, Y. Tang, B. Liu, H.H. Girault, Energy & Environmental Science 7 (2014) 387-392.
[21] S.K. Kim, Y.-J. Zhang, H. Bergstrom, R. Michalsky, A. Peterson, ACS Catal. 6 (2016) 2003-2013.
[22] G. Papapolymerou, V. Bontozoglou, J. Mol. Catal. A: Chem. 120 (1997) 165-171.
[23] T.V. Choudhary, C. Sivadinarayana, D.W. Goodman, Catalysis Letters 72 (2001) 197-201.
[24] R. Lan, J.T.S. Irvine, S. Tao, Int. J. Hydrogen Energy 37 (2012) 1482-1494.
[25] Y. Ozawa, Y. Tochihara, Catal. Today 164 (2011) 528-532.

[26] R. Schlögl, Angew. Chem. Int. Ed. 42 (2003) 2004-2008.

[27] H.K. G. Ertl, F. Schüth, J. Weitkamp, Handbook of heterogeneous catalysis, Wiley-VCH, Weinheim, Germany, 2008.

[28] S.T. Oyama, Catal. Today 15 (1992) 179-200.

[29] J.G. Choi, J. Ind. Eng. Chem. 10 (2004) 967-971.

[30] W. Zheng, T.P. Cotter, P. Kaghazchi, T. Jacob, B. Frank, K. Schlichte, W. Zhang, D.S. Su, F. Schüth, R. Schlögl, J. Am. Chem. Soc. 135 (2013) 3458-3464.

[31] X. Zhang, Z. Lu, D. Ma, Z. Yang, Int. J. Hydrogen Energy 40 (2015) 346-352.

[32] X. Duan, J. Ji, G. Qian, C. Fan, Y. Zhu, X. Zhou, D. Chen, W. Yuan, J. Mol. Catal. A: Chem. 357 (2012) 81-86.

[33] G. Lanzani, K. Laasonen, Int. J. Hydrogen Energy 35 (2010) 6571-6577.

[34] J. Zhao, C. Cui, H. Wang, J. Han, X. Zhu, Q. Ge, J. Phys. Chem. C 123 (2019) 554-564.

[35] T. Wang, X. Liu, S. Wang, C. Huo, Y.-W. Li, J. Wang, H. Jiao, J. Phys. Chem. C 115 (2011) 22360-22368.

[36] T. Wang, S. Wang, Y.-W. Li, J. Wang, H. Jiao, J. Phys. Chem. C 116 (2012) 6340-6348.

[37] Y. Shi, Y. Yang, Y.-W. Li, H. Jiao, Appl. Catal., A 524 (2016) 223-236.

[38] T. Wang, Y.-W. Li, J. Wang, M. Beller, H. Jiao, J. Phys. Chem. C 118 (2014) 3162-3171.

[39] T. Wang, Y.-W. Li, J. Wang, M. Beller, H. Jiao, J. Phys. Chem. C 118 (2014) 8079-8089.

[40] T. Wang, Q. Luo, Y.-W. Li, J. Wang, M. Beller, H. Jiao, Appl. Catal., A 478 (2014) 146-156.

[41] T. Wang, X. Tian, Y. Yang, Y.-W. Li, J. Wang, M. Beller, H. Jiao, Phys. Chem. Chem. Phys. 17 (2015) 1907-1917.

[42] Q. Luo, T. Wang, G. Walther, M. Beller, H. Jiao, J. Power Sources 246 (2014) 548-555.

[43] Y. Shi, Y. Yang, Y.-W. Li, H. Jiao, ACS Catal. 6 (2016) 6790-6803.

[44] Y. Shi, Y. Yang, Y.-W. Li, H. Jiao, Catal. Sci. Technol. 6 (2016) 4923-4936.

[45] G. Kresse, J. Furthmüller, Computational Materials Science 6 (1996) 15-50.

[46] G. Kresse, J. Furthmüller, Phys Rev B 54 (1996) 11169-11186.

[47] P.E. Blöchl, Phys Rev B 50 (1994) 17953-17979.

[48] G. Kresse, D. Joubert, Phys Rev B 59 (1999) 1758-1775.

[49] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865-3868.

[50] S. Grimme, J. Antony, S. Ehrlich, H. Krieg, J. Chem. Phys. 132 (2010) 154104.

[51] S. Grimme, S. Ehrlich, L. Goerigk, J. Comput. Chem. 32 (2011) 1456-1465.

[52] G. Henkelman, B.P. Uberuaga, H. Jónsson, J. Chem. Phys. 113 (2000) 9901-9904.

[53] T.P. St. Clair, S.T. Oyama, D.F. Cox, S. Otani, Y. Ishizawa, R.-L. Lo, K.-i. Fukui, Y. Iwasawa, Surf. Sci. 426 (1999) 187-198.

[54] A.N. Christensen, Acta Chem. Scand., A 31 (1977) 509-511.

[55] E. Parthé, V. Sadogopan, Acta Crystallogr. 16 (1963) 202-205.

[56] J. Dubois, T. Epicier, C. Esnouf, G. Fantozzi, P. Convert, Acta Metall. 36 (1988) 1891-1901.

[57] T. Epicier, J. Dubois, C. Esnouf, G. Fantozzi, P. Convert, Acta Metall. 36 (1988) 1903-1921.

[58] J. Haines, J. Leger, C. Chateau, J. Lowther, J. Phys.: Condens. Matter 13 (2001) 2447.

[59] R.J. Fries, C.P. Kempter, Anal. Chem. 32 (1960) 1898-1898.

[60] C.J. Cramer, Essentials of Computational Chemistry: Theories and Models, 2nd Edition, Wiley, England, 2004.

[61] W. Tang, E. Sanville, G. Henkelman, J. Phys.: Condens. Matter 21 (2009) 084204.

[62] E. Sanville, S.D. Kenny, R. Smith, G. Henkelman, J. Comput. Chem. 28 (2007) 899-908.

[63] G. Henkelman, A. Arnaldsson, H. Jónsson, Computational Materials Science 36 (2006) 354-360.

[64] M. Yu, D.R. Trinkle, J. Chem. Phys. 134 (2011) 064111.

[65] T. Koenig, J.A. Hoobler, C.E. Klopfenstein, G. Hedden, F. Sunderman, B.R. Russell, J. Am. Chem. Soc. 96 (1974) 4573-4577.

[66] T. Fueno, V. Bonacic-Koutecky, J. Koutecky, J. Am. Chem. Soc. 105 (1983) 5547-5557.

[67] R.C.V. McGee, S.K. Bej, L.T. Thompson, Appl. Catal., A 284 (2005) 139-146.

[68] W.-F. Chen, K. Sasaki, C. Ma, A.I. Frenkel, N. Marinkovic, J.T. Muckerman, Y. Zhu, R.R. Adzic, Angew. Chem. Int. Ed. 51 (2012) 6131-6135.

[69] S.C. Yeo, S.S. Han, H.M. Lee, J. Phys. Chem. C 118 (2014) 5309-5316.

[70] X. Duan, G. Qian, C. Fan, Y. Zhu, X. Zhou, D. Chen, W. Yuan, Surf. Sci. 606 (2012) 549-553.

[71] C.-z. He, H. Wang, L.-y. Huai, J.-y. Liu, J. Phys. Chem. C 116 (2012) 24035-24045.

~ 12 ~

[72] Z. Jiang, Q. Pan, M. Li, T. Yan, T. Fang, Appl. Surf. Sci. 292 (2014) 494-499.

[73] Z. Jiang, P. Qin, T. Fang, Chem. Phys. 445 (2014) 59-67.

[74] K. Shojaee, B.S. Haynes, A. Montoya, Mater. Chem. Phys. 156 (2015) 141-149.

Graphical Abstract

TOC

![](./images/812753807439036417_9.jpg)