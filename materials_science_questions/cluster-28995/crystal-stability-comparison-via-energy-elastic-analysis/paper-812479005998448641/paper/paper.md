# Asymmetric equilibrium core structures of pyramidal-II $\langle c+a\rangle$ dislocations in ten hexagonal-close-packed metals

Claire Albrecht*
Materials Department, University of California, Santa Barbara, California 93106-5050, USA

Anil Kumar
Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA

Shuozhi Xu
Department of Mechanical Engineering, University of California, Santa Barbara, California 93106-5070, USA

Abigail Hunter
X Computational Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA

Irene J. Beyerlein
Materials Department, University of California, Santa Barbara, California 93106-5050, USA
and Department of Mechanical Engineering, University of California, Santa Barbara, California 93106-5070, USA

![](./images/812479005998448641_1.jpg)
(Received 21 August 2020; revised 15 December 2020; accepted 8 March 2021; published 6 April 2021)

The structures of pyramidal-II $\langle c+a\rangle$ dislocations, one of the most important defects in structural hexagonal-close-packed (HCP) metals, have not been fully characterized for many of the HCP metals in use today. Here, we employ *ab initio* informed phase-field dislocation dynamics to determine the minimum energy structure of pyramidal $\{\overline{1}\overline{1}22}\langle 11\overline{2}3\rangle$ dislocations in ten HCP metals, including Be, Co, Mg, Re, Ti, Zn, Cd, Hf, Y, and Zr. As input for the simulations, we calculate, using first-principles density functional theory, the $\{\overline{1}\overline{1}22\}$ generalized stacking fault energy (GSFE) curves for all ten metals. From these calculations, it is found that magnetism in Co is necessary for achieving a local minimum in the GSFE curve. We observe in simulations that edge and screw character dislocations split into two partials separated by a low-energy intrinsic stacking fault. The splitting distance is shown to scale inversely with the local minimum energy normalized by the product of its shear modulus and Burgers vector. Interestingly, some HCP metals exhibit an asymmetric structure, with either unequal partial Burgers vectors or widths, in contrast to the symmetric configuration expected from linear elastic dislocation theory. We explain these structures by properties of the local maxima in their GSFE curves. Metals with larger degrees of elastic anisotropy result in dislocations with larger splitting distances than would be expected under the commonly used assumption of elastic isotropy. These findings on the sizes and asymmetry in the structures of pyramidal-II $\langle c+a\rangle$ dislocations are fundamental to understanding how these dislocations glide and interact or react with other defects when these metals are mechanically strained.

DOI: 10.1103/PhysRevMaterials.5.043602

## I. INTRODUCTION

Hexagonal-close-packed (HCP) materials are already being widely used as structural materials in several key industries, and there is currently great interest in expanding their employment in many next-generation engineering applications. HCP Hf, Zr, and Be and their alloys are frequently used in many nuclear and defense industries [1–4]. In the biomedical industry, HCP Ti and Zr and their alloys have long been the materials of choice, but additional alloys of Mg and Zn are currently being considered [5,6]. Many HCP Co-based alloys are in development for use in newer high-temperature aerospace applications [7,8]. Employment of HCP materials in these technologies necessitates understanding and modeling their deformation response, whether in processing or in service.

With respect to the HCP lattice, HCP materials slip easiest in their compact $\langle a\rangle$ direction on their compact planes, either basal or prismatic. Deformation in their $\langle c\rangle$ axis requires pyramidal $\langle c+a\rangle$ slip, which is more difficult, and the degree of plastic anisotropy scales with the difference in activation energies between $\langle a\rangle$ slip and pyramidal $\langle c+a\rangle$ slip modes [9–15]. Another inelastic mode of deformation that occurs easily in HCP materials is deformation twinning, and it competes directly with pyramidal $\langle c+a\rangle$ slip in accommodating $\langle c\rangle$ axis deformation [6,16]. Ductility of HCP metals is thought to be limited by plastic anisotropy and/or deformation twinning [15]. Therefore, enabling a wider use of HCP metals and improving ductility is dependent on understanding pyramidal $\langle c+a\rangle$ slip [17–20].

*claire_weaver@ucsb.edu

---
2475-9953/2021/5(4)/043602(18)
043602-1
©2021 American Physical Society
---
PHYSICAL REVIEW MATERIALS 5, 043602 (2021)

Pyramidal $\langle c+a\rangle$ dislocations can be difficult to move due to the combined effect of a relatively large Burgers vectors (36–46 % longer than an $\langle a\rangle$ Burgers vectors) and some atomic shuffling, as a consequence of the atomically rumpled pyramidal plane [20,21]. Based on Frank’s rule, it is energetically preferable for a full $\{\overline{1} \overline{1} 22\}\langle c+a\rangle$ dislocation to dissociate into two equal partial dislocations rather than remain whole by the following reaction [20]:

$$
\frac{1}{3}[2 \overline{1} \overline{1} 3] \rightarrow \frac{1}{6}[2 \overline{1} \overline{1} 3]+\frac{1}{6}[2 \overline{1} \overline{1} 3]. \tag{1}
$$

The products of this reaction, the two like-signed partials, repel. In their attempt to glide away, their motion is limited by the stacking fault they create across the glide plane. Their equilibrium separation $R_{\mathrm{e}}$ can be estimated by a balance of their repulsive interaction energy and penalizing energy of their stacking fault in between them [22]:

$$
R_{\mathrm{e}}=\frac{K b^{2}}{8 \pi I}, \tag{2}
$$

where $b$ is the magnitude of the Burgers vector of the undissociated, compact dislocation, $I$ is the intrinsic stacking fault energy (SFE), and $K$ is the anisotropic energy factor from Ref. [23], which depends only on the dislocation character and the five independent elastic constants.

The extent of the stacking fault $R_{\mathrm{e}}$ plays an important role not only in the partial dislocation mobility, but also in key dislocation-based processes, such as grain boundary migration, interactions between grain boundaries and interfaces, dislocation network formation, and dislocation-dislocation reactions [14,24–27]. They may be responsible for the choice of prevalent dislocation reactions, preferred glide planes, and mechanisms for overcoming obstacles, such as cross-slip or climb [28–31]. Dislocation theory and atomistic simulations suggest that dissociation of dislocations with relatively large Burgers vectors, such as pyramidal dislocations, can play a role in twin embryo formation or twin boundary migration in HCP metals [32–35].

The dissociated core structure of the pyramidal-II $\{\overline{1} \overline{1} 22\}$ plane is, in part, a consequence of its complex fault energy landscape, the energy associated with shearing across the glide plane. The energy along the $\langle 11 \overline{2} 3\rangle$ slip direction, called the generalized stacking fault energy (GSFE) curve, has a single local minimum corresponding to $I$. The displacement, $x_{I}$, to reach this local minimum is related to the Burgers vector of the partials. Density functional theory (DFT) calculations for the GSFE curve on the pyramidal-II plane have been reported in a number of works for Mg [21,36,37], Ti [36,38,39], Zr [36,38,40], as well as Cd, Zn, and Re [36]. For Mg, *Dou et al.* [37] studied the peaks and valley in the relevant displacement path, finding that the two peaks were unequal and the local minimum $I$ does not occur at half-shift between stable points. The asymmetry suggests an asymmetric split of the perfect dislocation and overall core structure, deviating from the geometric model in Eq. (2). Recent DFT work on Mg, as well as the other metals Zr, Ti, Cd, Zn, and Re, noted similar asymmetries, but further indicated that these asperities varied with the metal [36,38,40]. *Kumar et al.* [21,41] demonstrated that allowing for additional relaxations, during the calculation of the pyramidal GSFE curve, caused changes in the peaks and local minimum and the displacements needed to achieve them. In the case of pyramidal-II in Mg, the displacement shift became closer to $0.5b$, and consistent with Eq. (2). They explained that for the pyramidal planes in Mg and Zr, additional atomic shuffles were needed to reach the lowest energy minimum state. The same was not true for the basal or prismatic planes, whose atomic structures are flat and symmetric about the glide direction. However, for other metals, curves from fully relaxed DFT calculations still show that an asymmetry persists [36,41].

A few experimental studies have identified moving or dissociated $\langle c+a\rangle$ dislocations in Mg, otherwise identification or characterization of dislocation cores is challenging and requires high-resolution microscopy. Slip trace analyses of deformed Mg and Mg alloy crystals have provided evidence of profuse pyramidal slip [9,11,13,42,43]. *In situ* microscopy in nanocrystalline Mg witnessed pyramidal slip dislocations in motion [15]. Early room-temperature experimental observations from transmission electron microscopy (TEM) by Stohr and Poirier [44] reported that pyramidal dislocations are dissociated into two equal length $(1/2)\langle c+a\rangle$ dislocations, in agreement with the analytical picture in Eq. (1). More recently, high-resolution TEM (HR-TEM) studies revealed the stabilization of a single $(1/2)\langle c+a\rangle$ partial dislocation on the pyramidal-II $\{\overline{1} \overline{1} 22\}$ plane [21].

In addition to the $\{\overline{1} \overline{1} 22\}$ plane, pyramidal $\langle c+a\rangle$ dislocations can possibly glide on the first-order $\{\overline{1} \overline{1} 01\}$ pyramidal plane. The preferred pyramidal plane for a given HCP material currently relies on experimental observation and is not yet understood. Second-order (or type II) pyramidal glide is commonly expected in most HCP metals with the exception of Ti and Zr. However, pyramidal type II has been observed in Zr [45–47] and Ti [48,49], while the other type I glide has been reported more recently in Mg [43,50,51].

Computational studies of dislocation core structures have been carried out via a number of methods. The large size of Burgers vectors most often limits application of DFT for calculating the equilibrium core structures of pyramidal dislocations. The relatively larger length scales accessible with molecular dynamics methods makes it suitable; however, the largest body of work to date focuses on the one HCP metal, Mg, for which interatomic potentials have been developed specifically for studying defects. Alternatively, a number of continuum models based on continuum mechanics, such as the phase-field microelasticity (PFM) [52], phase-field dislocation dynamics (PFDD) [53], semidiscrete variational [54], and generalized Peierls-Nabarro (GPN) models [55], have been employed to compute dislocation core structures. They are formulated to capture long-range stress fields of dislocations, while sacrificing atomic-scale physics and fidelity. This class of models is developed primarily for simulating dislocation processes, involving one or more discrete dislocations, and their application to core structures is one problem they share with *ab initio* and atomistic methods [53,56].

The PF-based methods and GPN models minimize an energy functional at every point in the system, and the order parameters are usually chosen to identify a slipped phase and an unslipped phase. Dislocation core structures are calculated by relating discrete atomic displacements with a continuous disregistry field. The input parameters for the energies associated with these displacements can be obtained from

ab initio calculations, experimental measurements, molecular dynamics, or molecular statics (MS), provided that reliable potentials exist [57]. The PFDD model was recently extended to determine the static and dynamic properties of discrete dislocations belonging to all types of slip modes in the HCP crystal, such as the basal $\langle a\rangle$, prismatic $\langle a\rangle$, and pyramidal $\langle c+a\rangle$ slip modes [38]. Previously, the PFDD methodology was predominantly applied to dislocations in materials with cubic crystal structures, namely face-centered cubic (FCC) [57–59], and body-centered cubic (BCC) [60,61] structures. The dissociation simulations using the HCP PFDD method incorporated directly DFT-calculated GSFE surfaces and curves for the different HCP slip planes, and they employed isotropic elasticity [38]. The results demonstrated good agreement with available results from MS, DFT, or experimental observations of dislocations structures in Mg.

Here, we employ an elastically anisotropic version of the PFDD approach, developed in Ref. [58], to compute the equilibrium structures of pyramidal-II $\{\overline{1}\overline{1}22\}\langle 11\overline{2}3\rangle$ dislocations in ten HCP metals: Be, Co, Mg, Re, Ti, Zn, Cd, Hf, Y, and Zr. All input parameters including the lattice parameters, elastic constants, and GSFE curves are computed from first principles to avoid any dependence on interatomic potentials. These ten metals exhibit anisotropic elasticity to varying degrees [62]. For the DFT GSFE calculations, we apply the same method with full relaxation to all ten and show that their energetic landscapes exhibit a single local minimum and two unequal maxima, featuring a wide range of intrinsic SFEs. We show that achieving a single local minimum in the GSFE for Co requires accounting for its ferromagnetic properties.

In all these metals, the $\langle c+a\rangle$ pyramidal dislocations dissociate into two partials that separate in plane, creating extended structures, with nm-sized splitting distances. For the screw dislocation, Zn has the widest splitting distance and Ti the narrowest, and for the edge dislocation, Hf has the widest and Be the narrowest. Considering all ten metals, the separation distances scale inversely with the normalized intrinsic SFE, $I/(Kb)$, where $K$ is an anisotropic energy factor dependent on elastic constants and dislocation character. In most cases, the dislocation partial core widths and Burgers vectors are not ideally equal. These asymmetries in the dislocation structures can be explained by deviations in the $\{\overline{1}\overline{1}22\}$ GSFE landscape from that expected of a metal with an ideal $c/a$ ratio and symmetric landscape. Metals with higher levels of elastic anisotropy have wider separation distances for both screw and edge character dislocations than expected with effective isotropic constants, being 20–35 % broader for Zn, which is highly anisotropic but has no effect on Re, Y, and Mg, which are all nearly isotropic. These findings on the equilibrium structure of $\langle c+a\rangle$ pyramidal-II dislocations across a broad range of HCP metals are important for understanding their motion and interactions with other dislocations or interfaces.

## II. COMPUTATIONAL METHODS

### A. DFT methodology and calculations

For all DFT calculations here, we use the Vienna ab-initio Simulation Package (VASP) [63,64] and we utilize the generalized gradient approximation for the exchange correlation functional with the Perdew-Burke-Ernzerhof parametrization [65]. The interaction between valence electrons and ionic cores is treated using projector augmented wave potentials. The number of valence electrons for each material can be found in Table I. A plane-wave energy cutoff of 400 eV is employed and the structure is optimized until the force on each atom becomes smaller than 0.01 eV/Å. We use a $19 \times 19 \times 19$ $\Gamma$-centered Monkhorst-Pack $k$-point mesh to integrate the Brillouin zone of the primitive HCP unit cells to calculate the lattice parameters and elastic constants. For the GSFE curves, we adopted a $17 \times 13 \times 1$ $k$-point mesh. The $k$-point mesh was sufficiently dense that the convergence of total energy was less than 1 meV per atom with respect to a change in mesh size [66,67]. We confirmed that higher values of energy cutoff (up to 500 eV) and finer $k$-point grids do not lead to significant differences in the constants or GSFEs. All supercells contain a thick vacuum layer of 15 Å along the $z$-direction. Among these ten metals, Co is a well-known ferromagnetic material [68]. So we also identify the effect of ferromagnetic (FM) ordering in Co on the lattice parameters, elastic constants, and GSFE through comparisons with those calculated without magnetism (NM).

TABLE I. Number of valence electrons in pseudopotential used in DFT calculations and dimensions of supercell for pyramidal-II GSFE calculations in Å. Number of atoms is 60. Number of planes along the $z$-direction is 30, which is sufficiently large according to prior work in FCC [69] and BCC metals [70].

| Material   | No. of valence electrons | Supercell dimensions $(x,y,z)$ |
|------------|---------------------------|--------------------------------|
| Be         | 2                         | $(3.923, 4.226, 38.544)$       |
| Mg         | 2                         | $(5.525, 6.089, 51.488)$       |
| Y          | 11                        | $(6.316, 6.777, 58.547)$       |
| Ti         | 4                         | $(5.063, 5.467, 51.960)$       |
| Zr         | 4                         | $(5.596, 6.100, 51.392)$       |
| Hf         | 4                         | $(5.529, 5.965, 52.832)$       |
| Re         | 7                         | $(4.800, 5.264, 47.134)$       |
| Co (NM)    | 9                         | $(4.259, 4.658, 42.835)$       |
| Co (FM)    | 9                         | $(4.316, 4.746, 43.524)$       |
| Zn         | 12                        | $(4.614, 5.594, 46.894)$       |
| Cd         | 12                        | $(5.255, 6.410, 52.345)$       |

The lattice parameters and elastic constants calculated via DFT are presented in Table II. Overall, these quantities are in good agreement with previous DFT calculations and experimental measurements (see Table VIII in Appendix B) [21,40]. For all HCP metals, we confirmed that the calculated elastic constants satisfy $2C_{66}=C_{11}-C_{12}$, indicating transversely isotropic elasticity with five independent constants.

In addition to the lattice parameters and elastic constants, PFDD also utilizes $\{\overline{1}\overline{1}22\}$ GSFE curves in order to calculate the equilibrium dislocation core structures. For this work, the GSFE is the excess potential energy incurred when one crystal half is sheared relative to the other half across the pyramidal-II $\{\overline{1}\overline{1}22\}$ plane. The relevant direction of shearing on this plane is the $\langle 11\overline{2}3\rangle$ direction, the slip direction along which the local maxima and minimum usually lie. Many details of these lattice energy curves can affect the core structure, and for this reason we employ DFT for its calculation, as opposed to MS or a hypothetical function. To do so, we use the relaxed

<table>
<caption>TABLE II. Lattice parameters (in Å) and elastic constants (in GPa) for the ten HCP metals obtained from DFT and isotropic shear modulus $\mu$ (in GPa), and Lamé parameter, $\lambda$ (in GPa).</caption>
<thead>
<tr>
<th>Material</th>
<th>$a$</th>
<th>$c/a$</th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C_{13}$</th>
<th>$C_{33}$</th>
<th>$C_{44}$</th>
<th>$C_{66}$</th>
<th>$\mu$</th>
<th>$\lambda$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Be</td>
<td>2.265</td>
<td>1.5760</td>
<td>303</td>
<td>36.7</td>
<td>12.5</td>
<td>380.1</td>
<td>165.2</td>
<td>133.2</td>
<td>154.35</td>
<td>20.38</td>
</tr>
<tr>
<td>Mg</td>
<td>3.190</td>
<td>1.6250</td>
<td>63.3</td>
<td>25.9</td>
<td>20.8</td>
<td>65.7</td>
<td>18</td>
<td>18.7</td>
<td>19.26</td>
<td>23.53</td>
</tr>
<tr>
<td>Y</td>
<td>3.648</td>
<td>1.5660</td>
<td>74</td>
<td>24.4</td>
<td>21.3</td>
<td>78.1</td>
<td>25.2</td>
<td>24.8</td>
<td>25.65</td>
<td>22.91</td>
</tr>
<tr>
<td>Ti</td>
<td>2.923</td>
<td>1.5810</td>
<td>159.4</td>
<td>108.9</td>
<td>83.9</td>
<td>191.7</td>
<td>37.6</td>
<td>25.2</td>
<td>35.67</td>
<td>94.43</td>
</tr>
<tr>
<td>Zr</td>
<td>3.231</td>
<td>1.6010</td>
<td>135.1</td>
<td>80.3</td>
<td>70.7</td>
<td>166.1</td>
<td>26.1</td>
<td>27.4</td>
<td>30.23</td>
<td>77.59</td>
</tr>
<tr>
<td>Hf</td>
<td>3.192</td>
<td>1.5790</td>
<td>183.4</td>
<td>83.1</td>
<td>72.5</td>
<td>206.1</td>
<td>52.6</td>
<td>50.1</td>
<td>54.05</td>
<td>78.31</td>
</tr>
<tr>
<td>Re</td>
<td>2.773</td>
<td>1.6130</td>
<td>617.9</td>
<td>281</td>
<td>233.4</td>
<td>678.6</td>
<td>165.4</td>
<td>168.4</td>
<td>177.61</td>
<td>260.48</td>
</tr>
<tr>
<td>Co (NM)</td>
<td>2.459</td>
<td>1.6090</td>
<td>424.2</td>
<td>161.1</td>
<td>151.6</td>
<td>457.6</td>
<td>84.8</td>
<td>131.6</td>
<td>116.35</td>
<td>170.72</td>
</tr>
<tr>
<td>Co (FM)</td>
<td>2.492</td>
<td>1.6208</td>
<td>359.2</td>
<td>164.8</td>
<td>109.3</td>
<td>406.4</td>
<td>93.1</td>
<td>97.2</td>
<td>106.11</td>
<td>139.44</td>
</tr>
<tr>
<td>Zn</td>
<td>2.664</td>
<td>1.8470</td>
<td>154.3</td>
<td>38.4</td>
<td>48.4</td>
<td>63.9</td>
<td>30.4</td>
<td>58</td>
<td>39.58</td>
<td>45.05</td>
</tr>
<tr>
<td>Cd</td>
<td>3.034</td>
<td>1.8610</td>
<td>76.8</td>
<td>42.1</td>
<td>34.1</td>
<td>45.6</td>
<td>7.8</td>
<td>17.3</td>
<td>12.51</td>
<td>38.31</td>
</tr>
</tbody>
</table>

method [21], wherein for each displacement step, minimization of the energy of the system is ensured by fixing all atomic positions along the glide direction and allowing those along the plane normal and the in-plane direction lying normal to the glide direction to relax. Fine displacement intervals were used to precisely locate the local minimum. Note that with the same DFT model design, the GSFE curves or surfaces for the basal, prismatic, and two types of pyramidal planes in Mg, Zr, and Ti have been previously calculated [21,38,71]. Here, we extend the pyramidal-II GSFE calculations for all ten HCP metals

Figure 1(a) presents the calculated GSFE curves for all ten HCP metals. We observe that all curves have two pronounced local maxima, denoted as the unstable SFEs, $U_1$ and $U_2$, and a local minimum, well known as the intrinsic SFE $I$. To ensure the local minimum indeed lies along the GSFE curve, the full pyramidal-II GSFE surface of Mg was calculated with DFT (see Fig. 10 in Appendix A). Compared to prior pyramidal-II GSFE curves, the results in Fig. 1 are similar with the exception of Cd [36]. Differences could be attributed to more atoms in the present supercell ($\approx$60) but a coarser $k$-point grid.

The relative shear displacement $x_I/b$ across the plane corresponding to $I$ leads to a metastable stacking fault. Table III summarizes the values for $I$, $U_1$, $U_2$, and $x_I/b$. In all metals, the two peak energies, $U_1$ and $U_2$, belonging to the same landscape, are unequal with $U_2 > U_1$. The local minimum $x_I/b$ displacement is shifted from the ideal $x_I/b=0.5$, a reflection of the anisotropy in bond length. In low-symmetry HCP metals, the bond lengths are generally unequal for all planes. When $c/a=\sqrt{8}/3=1.633$, all 12 nearest neighbors of an atom in the double lattice structure are equidistant. Only one of the ten HCP metals, Mg, possesses a nearly ideal $c/a$ ratio, and accordingly, its $x_I/b=0.49$. Two metals, Zn and Cd, have $c/a$ ratios greater than ideal, leading to $x_I/b>0.5$. All remaining metals have below ideal $c/a$ ratios and $x_I/b<0.5$.

Figure 1(b) examines more closely the GSFE curves for Co calculated with and without ferromagnetic ordering. The effect of magnetism on the GSFE is found to be significant. Without magnetism, the GSFE possesses no pronounced local minimum, but with magnetism, it has a single local minimum at $x_I/b=0.45$, like the other nine HCP metals. The peak energy $U_2$ also reduces with magnetism by 8%. Table II shows that magnetism increased the lattice parameter $a$ and the $c/a$ ratio and decreased the elastic constants $C_{11}$, $C_{13}$, and $C_{33}$. A similar effect of magnetism on $a$ was reported in prior studies of cubic metals, namely Cr [61], Fe [72], and Ni [69]. More importantly, the values for the elastic moduli determined with ferromagnetism achieve better agreement with the experimen-

![](./images/812479005998448641_2.jpg)

FIG. 1. Comparison of GSFE profiles (a) for the pyramidal-II plane in ten HCP metals as determined by DFT, and (b) for Co with and without magnetism considered in the DFT simulations. In (a), the GSFE curve for Co is shown with the effect of ferromagnetism considered. The unstable SFEs, $U_{1,2}$, and intrinsic SFE, $I$, are labeled in (b).

<table><thead><tr><th rowspan="2">Material</th><th colspan="2">$U_{1}$</th><th colspan="2">$I$</th><th colspan="2">$U_{2}$</th></tr><tr><td>$mJm^{-2}$</td><td>$x_{U_{1}}/b$</td><td>$mJm^{-2}$</td><td>$x_{I}/b$</td><td>$mJm^{-2}$</td><td>$x_{U_{2}}/b$</td></tr></thead><tbody><tr><td>Be</td><td>1335.7</td><td>0.23</td><td>678.2</td><td>0.47</td><td>1768.6</td><td>0.71</td></tr><tr><td>Mg</td><td>262.9</td><td>0.27</td><td>168.1</td><td>0.49</td><td>397.4</td><td>0.72</td></tr><tr><td>Y</td><td>380.1</td><td>0.27</td><td>352.3</td><td>0.42</td><td>565.6</td><td>0.71</td></tr><tr><td>Ti</td><td>617.8</td><td>0.21</td><td>332.1</td><td>0.44</td><td>764.2</td><td>0.68</td></tr><tr><td>Zr</td><td>538.5</td><td>0.21</td><td>260.2</td><td>0.44</td><td>658.2</td><td>0.69</td></tr><tr><td>Hf</td><td>730.2</td><td>0.20</td><td>411.9</td><td>0.43</td><td>919.6</td><td>0.69</td></tr><tr><td>Re</td><td>1468.1</td><td>0.27</td><td>1168.0</td><td>0.44</td><td>2088.8</td><td>0.74</td></tr><tr><td>Co (NM)</td><td>870.0</td><td>0.21</td><td>857.3</td><td>0.30</td><td>1502.5</td><td>0.69</td></tr><tr><td>Co (FM)</td><td>889.6</td><td>0.29</td><td>702.2</td><td>0.45</td><td>1381.2</td><td>0.71</td></tr><tr><td>Zn</td><td>324.3</td><td>0.35</td><td>150.3</td><td>0.52</td><td>393.4</td><td>0.78</td></tr><tr><td>Cd</td><td>174.4</td><td>0.36</td><td>78.2</td><td>0.53</td><td>202.3</td><td>0.79</td></tr></tbody></table>

tally measured values, which are presented in Table VIII in Appendix B. Hereafter, PFDD calculations in this paper will use the GSFE curve, lattice parameters, and elastic moduli calculated for Co from DFT with ferromagnetism considered.

### B. PFDD formulation

As is fundamental in phase field approaches, this method relies on the evolution of one or more order parameters through the minimization of the total system energy. For phase field approaches formulated to study the motion and interaction of dislocations, the order parameters, $\zeta$, represent the location of and area traveled by dislocations within the system [52,53,73]. The order parameters are defined by slip systems within a material, and hence the number of order parameters varies with the crystallography of the material under study. Defined in this way, the set of $\zeta$ is used to describe the plastic strain as

$$
\epsilon_{i j}^{p}=\frac{1}{2} \sum_{\alpha=1}^{N_{\mathrm{op}}} \frac{b_{\alpha}}{d_{\alpha}} \zeta_{\alpha}(\mathbf{x}, t) \delta_{\alpha}\left(s_{i}^{\alpha} m_{j}^{\alpha}+s_{j}^{\alpha} m_{i}^{\alpha}\right),\qquad(3)
$$

where the sum is taken over all slip systems $\alpha$ from 1 to $N_{\text {op }}$ included in the material, $b_{\alpha}$ is the magnitude of the Burgers vector on the slip plane of interest, $d_{\alpha}$ is the interplanar distance for the active slip plane, $\delta_{\alpha}$ is the Dirac distribution supported on the slip plane, $\mathbf{m}$ is the slip plane normal, and $\mathbf{s}$ is the normalized slip vector. In many crystals, multiple systems share the same plane; therefore, while $d_{\alpha}$ is defined with each slip system $\alpha$, slip systems on the same slip plane will share the same $d_{\alpha}$.

In the PFDD method, the order parameters evolve through the minimization of the total system energy density, $E$, dictated at each time step via the time-dependent Ginzburg-Landau (TDGL) equation

$$
\frac{\partial \zeta_{\alpha}(\mathbf{x}, t)}{\partial t}=-L \frac{\delta E(\zeta)}{\delta \zeta_{\alpha}(\mathbf{x}, t)},\qquad(4)
$$

where $L$, which is related to the convergence speed of the system, is a non-negative coefficient that is constant and set to unity here for all order parameters. For calculations involving multiple order parameters, Eq. (4) becomes a set of $N$ coupled integrodifferential equations that must be solved numerically to evolve the system. In the dislocation problems of interest for this work, the total free energy density of the system consists of two contributions [53,59]:

$$
E=E^{\text {strain }}+E^{\text {lattice }},\qquad(5)
$$

where $E^{\text {strain }}$ is the elastic strain energy density generated by the presence of dislocations in the system and interactions between these dislocations. The lattice energy density, $E^{\text {lattice }}$, describes the energy expended as a dislocation glides through the crystal lattice breaking and reforming atomic bonds. Under an external stress, a third term for the work done to the system through an applied stress would be included. However, for the problems in this work, no external stress is applied. In addition, past PFDD formulations have included a gradient energy term, representing the energy density stored in the partial dislocation cores in FCC metals [57]. It tends to increase the partial dislocation core size in better agreement with MS [57,74]. With its basic effect qualitatively understood, we refrain from adding the gradient energy term in the present application since it requires an additional material-dependent coefficient. We note that in this case, without the gradient energy term, the PFDD formulation employed is equivalent to a GPN model [55]. We emphasize that the GPN model has not yet been applied to the problem of pyramidal-II dislocation cores, to the best of our knowledge.

The elastic strain energy density, $E^{\text {strain }}$, which is commonly expressed in terms of the elastic strain, can also be expressed in terms of the plastic strain [53]:

$$
E^{\text {strain }}=\frac{1}{(2 \pi)^{3}} f \frac{1}{2} \hat{A}_{m n u v}(\mathbf{k}) \hat{\epsilon}_{m n}^{p}(\mathbf{k}) \hat{\epsilon}_{u v}^{p *}(\mathbf{k}) d^{3} k,\qquad(6)
$$

where a superposed $(^{\wedge})$ denotes the Fourier transform, $\hat{A}_{m n u v}(\mathbf{k})=C_{m n u v}-C_{k l u v} C_{i j m n} \hat{G}_{k i}(\mathbf{k}) k_{j} k_{l}, \mathbf{k}$ is the wave number vector, $\hat{G}_{k i}(\mathbf{k})$ is the Fourier transform of the Green's tensor of linear elasticity, $f$ denotes the principal value of the integral, $C_{i j k l}$ is the elastic moduli tensor, and the superscript $(*)$ denotes the complex conjugation.

To examine the effect of HCP anisotropy, we will use the elastic moduli tensor and the Green's tensor for either a transversely isotropic or ideally isotropic material in the calculations. The elastic stiffness tensor for both a transversely isotropic hexagonal system, $\mathbf{C}^{\mathrm{a}}$, and an isotropic system, $\mathbf{C}^{\mathrm{i}}$, can be given in compact matrix notation by

$$
\begin{aligned}
\mathbf{C}^{\mathrm{a}} & =\left[\begin{array}{cccccc}
C_{11} & & & & & \\
C_{12} & C_{11} & & & & \\
C_{13} & C_{13} & C_{33} & & & \\
& & & C_{44} & & \\
& & & & C_{44} & \\
& & & & & C_{66}
\end{array}\right], \\
\mathbf{C}^{\mathrm{i}} & =\left[\begin{array}{cccccc}
\lambda+2 \mu & & & & & \\
\lambda & \lambda+2 \mu & & & & \\
\lambda & \lambda & \lambda+2 \mu & & & \\
& & & \mu & & \\
& & & & \mu & \\
& & & & & \mu
\end{array}\right],
\end{aligned}
$$
(7)

<table>
<caption>TABLE IV. Interplanar spacing, $d$, normalized in terms of the Burgers vector magnitude $b$ and the calculated coefficients for the lattice energy periodic potential for the pyramidal-II [Eq. (11)] slip mode. All coefficients are shown in units of mJ m⁻².</caption>
<thead>
  <tr>
    <th>Material</th>
    <th>$d/b$</th>
    <th>$p_0$</th>
    <th>$p_1$</th>
    <th>$p_2$</th>
    <th>$p_3$</th>
    <th>$p_4$</th>
    <th>$q_1$</th>
    <th>$q_2$</th>
    <th>$q_3$</th>
    <th>$q_4$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Be</td>
    <td>0.22619</td>
    <td>989.73</td>
    <td>−295.15</td>
    <td>−572.54</td>
    <td>−45.07</td>
    <td>−41.44</td>
    <td>−178.95</td>
    <td>143.29</td>
    <td>6.682</td>
    <td>−15.83</td>
  </tr>
  <tr>
    <td>Mg</td>
    <td>0.22318</td>
    <td>217.98</td>
    <td>−75.35</td>
    <td>−116.48</td>
    <td>−6.137</td>
    <td>−9.728</td>
    <td>−55.26</td>
    <td>15.05</td>
    <td>8.900</td>
    <td>−1.228</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0.22680</td>
    <td>332.03</td>
    <td>−154.61</td>
    <td>−137.14</td>
    <td>−24.28</td>
    <td>−4.422</td>
    <td>−76.47</td>
    <td>22.48</td>
    <td>10.91</td>
    <td>−1.145</td>
  </tr>
  <tr>
    <td>Ti</td>
    <td>0.22589</td>
    <td>427.52</td>
    <td>−165.06</td>
    <td>−220.30</td>
    <td>−22.96</td>
    <td>−9.542</td>
    <td>−52.33</td>
    <td>118.72</td>
    <td>−13.57</td>
    <td>−16.63</td>
  </tr>
  <tr>
    <td>Zr</td>
    <td>0.22466</td>
    <td>366.91</td>
    <td>−127.64</td>
    <td>−196.37</td>
    <td>−21.80</td>
    <td>−8.282</td>
    <td>−48.31</td>
    <td>105.95</td>
    <td>−12.50</td>
    <td>−12.27</td>
  </tr>
  <tr>
    <td>Hf</td>
    <td>0.22601</td>
    <td>528.33</td>
    <td>−184.61</td>
    <td>−258.63</td>
    <td>−41.86</td>
    <td>−18.95</td>
    <td>−82.81</td>
    <td>131.01</td>
    <td>−11.56</td>
    <td>−15.33</td>
  </tr>
  <tr>
    <td>Re</td>
    <td>0.22392</td>
    <td>1205.08</td>
    <td>−482.64</td>
    <td>−551.80</td>
    <td>−92.09</td>
    <td>−1.064</td>
    <td>−269.59</td>
    <td>46.20</td>
    <td>42.31</td>
    <td>24.93</td>
  </tr>
  <tr>
    <td>Co (NM)</td>
    <td>0.22416</td>
    <td>875.19</td>
    <td>−404.22</td>
    <td>−306.22</td>
    <td>−74.51</td>
    <td>−38.14</td>
    <td>−239.18</td>
    <td>93.18</td>
    <td>40.97</td>
    <td>−17.05</td>
  </tr>
  <tr>
    <td>Co (FM)</td>
    <td>0.22344</td>
    <td>770.05</td>
    <td>−318.55</td>
    <td>−360.51</td>
    <td>−33.14</td>
    <td>−23.72</td>
    <td>−220.16</td>
    <td>48.84</td>
    <td>16.88</td>
    <td>4.346</td>
  </tr>
  <tr>
    <td>Zn</td>
    <td>0.20934</td>
    <td>214.57</td>
    <td>−74.43</td>
    <td>−115.09</td>
    <td>−5.264</td>
    <td>−15.33</td>
    <td>−49.90</td>
    <td>−56.68</td>
    <td>23.13</td>
    <td>8.863</td>
  </tr>
  <tr>
    <td>Cd</td>
    <td>0.20848</td>
    <td>109.91</td>
    <td>−41.06</td>
    <td>−57.01</td>
    <td>−2.154</td>
    <td>−8.134</td>
    <td>−25.06</td>
    <td>−35.13</td>
    <td>13.93</td>
    <td>4.391</td>
  </tr>
</tbody>
</table>

where $2C_{66}=C_{11}-C_{12}$, $\mu$ is the shear modulus, and $\lambda$ is Lamé's first constant. We utilize a Voigt average to determine the two isotropic constants from the five transversely isotropic constants (Table II), using [22]

$$
\mu=\frac{1}{30}[7C_{11}-5C_{12}+2C_{33}+12C_{44}-4C_{13}], \tag{8}
$$

$$
\lambda=\frac{1}{15}[C_{11}+C_{33}+5C_{12}+8C_{13}-4C_{44}], \tag{9}
$$

whose values are also included in Table II.

The lattice energy $E^\text{lattice}$ depends on the material, and in some cases, such as HCP and BCC metals, the lattice energies of more than one type of crystallographic plane are of interest [38,61]. In general, $E^\text{lattice}$ can be written as [38,53]

$$
E^\text{lattice}=\sum_{\beta=1}^{N_\text{p}}\int\frac{1}{d_\beta}\phi_\beta(\zeta_1(\mathbf{x}),\zeta_2(\mathbf{x}),\dots,\zeta_N(\mathbf{x}))d^3x, \tag{10}
$$

where $\phi_\beta(\zeta_1(x),\zeta_2(x),\dots)$ is a periodic potential for slip plane $\beta$ on up to $N_\text{p}$ planes.

### C. PFDD model for $\langle c+a\rangle$ pyramidal dislocations

Here we consider a straight dislocation belonging to a pyramidal-II $\langle c+a\rangle$ slip system. Hence, $N_\text{op}=1$, $N_\text{p}=1$, and $\alpha=\beta=1$. In what follows, we drop the subscripts $\alpha$ and $\beta$. For the periodic potential of the pyramidal-II plane, the following continuous function, proposed in Ref. [38], is adopted:

$$
\begin{aligned}
\phi(\zeta)&=p_0+p_1\cos(2\pi\zeta)+p_2\cos(4\pi\zeta)+p_3\cos(6\pi\zeta) \\
&\quad +p_4\cos(8\pi\zeta)+q_1\sin(2\pi\zeta)+q_2\sin(4\pi\zeta) \\
&\quad +q_3\sin(6\pi\zeta)+q_4\sin(8\pi\zeta), \tag{11}
\end{aligned}
$$

where the coefficients $p_0,\dots,p_4,q_1,\dots,q_4$ are calculated from the GSFE curves using the MATLAB curve-fitting tool [75]. The continuous GSFE curves are shown in Fig. 1(a) and the corresponding coefficients are presented in Table IV.

The explicit Euler method is employed for the time integration in the TDGL equation. The order parameter at time $t_i+\Delta t$ is formulated explicitly based on its value at time $t_i$ according to Eq. (4). A recent PFDD work [74] found that the explicit Euler method requires the time-step size $\Delta t$ to be small enough for numerical stability, so $\Delta t=0.01$ is used in our work.

Figure 2(a) shows the three-dimensional (3D) cuboidal periodic simulation cell. As part of the fast Fourier transform method for calculating the strain energy density, periodic boundary conditions are employed. All order parameters $\zeta=0$ (perfect direct lattice) at each grid point, except those that lie on the plane $z=N/2$ and between $x=N/4$ and $x=3N/4$ (in the darker shaded area) where $\zeta=1$ (perfect direct lattice translated by one Burgers vector) for all grid points in this region. Since dislocations are not explicitly defined in the PFDD model, but rather are inferred as a structurally necessary defect along boundaries between regions with different order parameter integer values, two perfect dislocations are

![](./images/812479005998448641_3.jpg)

FIG. 2. Schematics showing (a) the initial simulation setup for the PFDD computational cell with two infinitely long parallel dislocations forming a dipole. In (b), the HCP unit cell is oriented (shown for an initial edge dislocation) such that the pyramidal-II glide plane lies parallel to the $xy$-plane in the simulation cell in (a). The simulation setup for a screw dislocation would have the same initialization shown in (a), while the HCP unit cell in (b) would be rotated around the $z$-axis by $90^\circ$. For clarity, the $x$-, $y$-, and $z$-axis in our simulation cell correspond to the $x$-, $y$-, and $z$-axis, respectively, in our HCP unit cell when initializing for an edge dislocation, and to the $y$-, $x$-, and $z$-axis, respectively, when initializing for a screw dislocation. Thus, the slip plane lies parallel to the simulation cell surface, the dislocation line sense lies parallel to the $y$-axis, and the Burgers vector (and unit cell) orientation is reflective of the desired dislocation character.

initialized in our simulation cell, one at $x=N/4$ and the other at $x=3N/4$, forming a dipole. We chose this setup as opposed to initializing the order parameter step from $0 \to 1$ at $x=N/2$ to avoid placing an unintentional dislocation along the periodic boundary. Along each direction of the simulation cell, there are $N=640$ grid points. Several simulation cell sizes were tested, and this size was determined to be sufficiently large such that the final equilibrium state was unaffected by the image dislocations in the periodic cells.

The grid spacing in all $x$, $y$, and $z$ directions is set as the interplanar distance $d$ for the pyramidal-II plane normalized by the Burgers vector magnitude $b$. Note that $b$ is for the $\langle 11\overline{2}3 \rangle$ direction and $d$ is for the $\{\overline{1}\overline{1}22\}$ plane. In the $(hkl)$ Miller-Bravais notation, the interplanar spacing is $\frac{1}{d^2} = \frac{4}{3} \frac{h^2+hk+k^2}{a^2} + \frac{l^2}{c^2}$. Thus, the interplanar spacing accounts for the lattice spacing in both the $\langle a \rangle$ and $\langle c \rangle$ directions and changes with the material $c/a$ ratio. By using the interplanar spacing as the grid spacing, the calculations account for the differences in the $c$-axis length among the HCP materials. Table IV summarizes the normalized interplanar spacing $d/b$ for each material. In addition, the DFT calculated elastic constants and lattice parameters, shown previously in Table II, are used to inform the material parameters for each simulation.

Each simulation begins with a perfect edge or screw dislocation dipole placed on the glide plane, as shown in Fig. 2(a). The dipole consists of a pair of dislocations with equal and opposite sign, which produces a net zero Burgers circuit around the simulation cell. The lines of the pair lie at $N/4$ and $3N/4$ along the $x$-axis, and the line sense is oriented parallel to the $y$-axis, which is the $[1\overline{1}00]$ direction, as shown in Fig. 2(b). For the edge dislocation, the Burgers vector is oriented parallel to the $x$-axis ($[11\overline{2}3]$ direction), and for the screw dislocation it lies parallel to the $y$-axis. It can be demonstrated that as the system relaxes to its equilibrium state, the two dislocations in the dipole behave independently and identically. Accordingly, we focus the analysis hereafter on the positive dislocation, which is on the left in Fig. 2(a).

## III. RESULTS

### A. Disregistry across the core structure

To determine the structure of the dislocation at all times during the relaxation process, we extract in-plane values of the order parameter, $\zeta$, and compute the disregistry $b\zeta$ across the plane where the dislocation lies. Given that $b$ is a constant for each metal, the latter quantity can be simplified as the order parameter density $d\zeta/dx$. Initially the full dislocation is compact and its $d\zeta/dx$ profile corresponds to a narrow peak at the initial position $x=0$. If the dislocation dissociates during relaxation into smaller, distinct partial dislocations, the order parameter density profile would transform in time to one comprised of relatively shorter peaks where these partials are located, as illustrated in Fig. 3. The viewing plane of this illustration lies transverse to the dislocation line. The two peaks correspond to the two partial dislocations on the glide plane, and the locations of these peaks correspond to the positions of the center of the cores. To conserve the Burgers vector, the partials will have the same sign and thus repel one another, causing the left partial to displace to the left and the right one to the right from the dissociation site. If the cores of these partials were compact, then they would appear as two narrow peaks. Yet, in actuality, the cores of the partials assume a finite width $w$ in response to the energetic expense associated with creating a fault. Adopting the approach used commonly in analyses of diffraction data, we establish the widths of the partial cores, $w_{\text{l}}$ and $w_{\text{r}}$, as the full width at half-maximum (FWHM) of each peak in the $d\zeta/dx$ profile. Over the years, the size of the extended dislocation cores has been most prominently characterized by the equilibrium distance between the two partials, which has also been variously called the equilibrium stacking fault width (SFW) or splitting distance. Here, we define the equilibrium splitting distance as the distance between the centers of the two partial, denoted as $R_{\text{e}}$, as illustrated in Fig. 3.

![](./images/812479005998448641_4.jpg)

FIG. 3. A schematic of the gradient of the order parameter, $d\zeta/dx$. The labels indicate the equilibrium SFW, $R_{\text{e}}$, and their core widths, $w_{\text{l}}$ and $w_{\text{r}}$, respectively.

The Burgers vector decomposition between the two partials can also be determined from $\zeta$ and its density $d\zeta/dx$. The magnitude of the Burgers vectors for the partial dislocations can be expressed as a fraction of the magnitude of the full pyramidal-II Burgers vector. The magnitude of the Burgers vector of the left partial is related to the value of the order parameter $\zeta_0 = \zeta(x_0)$ where the position $x_0$ is the minimum value of the gradient within the stacking fault (i.e., between the two peaks). The magnitude of the Burgers vector for the right partial dislocation is the remainder $1 - \zeta_0$. Having identified $\zeta_0$, we can calculate the Burgers vector of the two partials $b_{\text{l}}$ and $b_{\text{r}}$ via
$$
b = \zeta_0 b + (1 - \zeta_0)b = b_{\text{l}} + b_{\text{r}}. \tag{12}
$$

### B. Be, Mg, and Y

We begin with the group II and III HCP metals, Be, Y, and Mg. The GSFE curve of Be stands out from the others in Fig. 1(a) with the largest unstable SFEs $U_{1,2}$, as well as a distinct local minimum at the stable energy $I$. In the GSFE curves for Y and Mg, however, the differences among $U_{1,2}$ and $I$ are relatively small, and hence their local minima lie in a relatively shallow energy well.

Figure 4 shows the order parameter $\zeta$ and its density $d\zeta/dx$ after the equilibrium structure is achieved for dislocations in these metals. These profiles focus on a smaller region of the model crystal and $\zeta$ is represented by the dotted lines and

![](./images/812479005998448641_5.jpg)

FIG. 4. The order parameter, $\zeta$ (dotted lines), and its density, $d\zeta/dx$ (solid lines), along the [11$\overline{2}$3] slip direction for initialized edge (a,b,c) and screw (d,e,f) dislocations in Be, Mg, and Y. Both isotropic (red) and anisotropic (blue) elastic considerations are compared. The vertical lines represent the location of the two partials before the dissociation, when they are one unstable perfect dislocation at zero position, and at the end of the simulation, when equilibrium is achieved.

$d\zeta/dx$ by the solid lines. The initial position of the dislocation before the dissociation process is zero (as indicated with vertical dashed line). In all three metals, the dislocation was observed to dissociate into two partials with a stacking fault in between. The partial dislocations appear as the two broad peaks in the order parameter density, and the stacking fault is the intervening, nearly flat region between them.

Table V summarizes the Burgers vectors of their partials as well as their splitting distances $R_{\text{e}}$. The Burgers vectors in each partial dislocation are nearly, but not exactly, equal in value, with the left one being slightly smaller than the right one. For Be, Mg, and Y, their final splitting distances are, respectively, 18.17, 25.81, and 21.52 Å for the edge dislocations and 18.17, 17.66, and 16.91 Å for the screw dislocations. The edge dislocations have larger $R_{\text{e}}$ than the screw dislocations. This trend only confirms the stronger edge repulsion force generated between two like-edge dislocations than two like-screw dislocations.

For validation, we turn to available DFT calculations, which only exist for Mg. DFT calculations reported 16.6 and 18.3 Å, respectively, for screw and edge dislocations [76] and 14 Å for the screw dislocation [29]. MS simulations calculated 15 and 20.72 Å, respectively, for screw and edge dislocations [77] and 22.6 Å for the edge dislocation [21]. Differences are small considering likely variations in the definition of $R_{\text{e}}$, elastic constants, and fault energies among these studies. Further, as noted earlier, without the gradient term, partial core widths tend to be narrower than those from DFT or MS [57].

The estimates for the widths of the partial cores $w$ for Be, Y, and Mg are listed in Table V. The energetic formulation

<table>
<caption>TABLE V. The equilibrium SFW, $R_{\text{e}}$, the left and right partial dislocation core widths, $w_{\text{l}}$ and $w_{\text{r}}$, and the left and right Burgers vector magnitude, $b_{\text{l}}$ and $b_{\text{r}}$, respectively, for perfect edge and screw dislocation dissociation in ten HCP materials. Due to the grid spacing, the partial dislocation core widths have error bars of $\pm 0.1b$. Values of $R_{\text{e}}$, $w_{\text{l}}$, $w_{\text{r}}$, $b_{\text{l}}$, and $b_{\text{r}}$ are normalized by $b$.</caption>
<thead>
<tr>
<th>Material</th>
<th>Dislocation</th>
<th>$b$ (Å)</th>
<th>$R_{\text{e}}$</th>
<th>$w_{\text{l}}$</th>
<th>$b_{\text{l}}$</th>
<th>$w_{\text{r}}$</th>
<th>$b_{\text{r}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Be</td>
<td>Edge</td>
<td>4.228</td>
<td>4.298</td>
<td>0.45</td>
<td>0.48</td>
<td>0.45</td>
<td>0.52</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>4.228</td>
<td>4.298</td>
<td>0.68</td>
<td>0.48</td>
<td>0.68</td>
<td>0.52</td>
</tr>
<tr>
<td>Mg</td>
<td>Edge</td>
<td>6.087</td>
<td>4.240</td>
<td>0.89</td>
<td>0.49</td>
<td>0.45</td>
<td>0.51</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>6.087</td>
<td>2.901</td>
<td>0.89</td>
<td>0.46</td>
<td>0.47</td>
<td>0.51</td>
</tr>
<tr>
<td>Y</td>
<td>Edge</td>
<td>6.778</td>
<td>3.175</td>
<td>0.68</td>
<td>0.48</td>
<td>0.45</td>
<td>0.52</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>6.778</td>
<td>2.495</td>
<td>0.91</td>
<td>0.46</td>
<td>0.45</td>
<td>0.54</td>
</tr>
<tr>
<td>Ti</td>
<td>Edge</td>
<td>5.468</td>
<td>4.065</td>
<td>0.45</td>
<td>0.44</td>
<td>0.45</td>
<td>0.56</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>5.468</td>
<td>2.259</td>
<td>0.45</td>
<td>0.44</td>
<td>0.45</td>
<td>0.56</td>
</tr>
<tr>
<td>Zr</td>
<td>Edge</td>
<td>6.099</td>
<td>4.717</td>
<td>0.45</td>
<td>0.44</td>
<td>0.45</td>
<td>0.56</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>6.099</td>
<td>2.696</td>
<td>0.45</td>
<td>0.44</td>
<td>0.45</td>
<td>0.56</td>
</tr>
<tr>
<td>Hf</td>
<td>Edge</td>
<td>5.966</td>
<td>4.971</td>
<td>0.45</td>
<td>0.44</td>
<td>0.68</td>
<td>0.56</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>5.966</td>
<td>3.389</td>
<td>0.45</td>
<td>0.44</td>
<td>0.68</td>
<td>0.56</td>
</tr>
<tr>
<td>Re</td>
<td>Edge</td>
<td>5.262</td>
<td>5.599</td>
<td>1.79</td>
<td>0.46</td>
<td>0.67</td>
<td>0.54</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>5.262</td>
<td>3.807</td>
<td>1.34</td>
<td>0.46</td>
<td>0.67</td>
<td>0.54</td>
</tr>
<tr>
<td>Co (FM)</td>
<td>Edge</td>
<td>4.746</td>
<td>4.916</td>
<td>1.79</td>
<td>0.47</td>
<td>0.89</td>
<td>0.53</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>4.746</td>
<td>3.576</td>
<td>1.34</td>
<td>0.47</td>
<td>0.67</td>
<td>0.53</td>
</tr>
<tr>
<td>Zn</td>
<td>Edge</td>
<td>5.595</td>
<td>4.815</td>
<td>0.42</td>
<td>0.52</td>
<td>0.42</td>
<td>0.48</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>5.595</td>
<td>4.397</td>
<td>0.42</td>
<td>0.52</td>
<td>0.42</td>
<td>0.48</td>
</tr>
<tr>
<td>Cd</td>
<td>Edge</td>
<td>6.410</td>
<td>4.168</td>
<td>0.42</td>
<td>0.53</td>
<td>0.42</td>
<td>0.47</td>
</tr>
<tr>
<td></td>
<td>Screw</td>
<td>6.410</td>
<td>2.710</td>
<td>0.42</td>
<td>0.53</td>
<td>0.42</td>
<td>0.47</td>
</tr>
</tbody>
</table>

**TABLE VI.** The ratio between the left and right partial dislocation cores, $w_{\mathrm{l}}/w_{\mathrm{r}}$, for both edge and screw dislocations, and the ratio between the unstable SFEs, $U_{2}/U_{1}$, and the ratio, $D_{2}/D_{1}$. Values of $w_{\mathrm{l}}$ and $w_{\mathrm{r}}$ are from Table V.

| Material   | $w_{\mathrm{l}}/w_{\mathrm{r}}$ (edge) | $w_{\mathrm{l}}/w_{\mathrm{r}}$ (screw) | $U_{2}/U_{1}$ | $D_{2}/D_{1}$ |
|------------|-----------------------------------------|------------------------------------------|---------------|---------------|
| Be         | 1.0                                     | 1.0                                      | 1.324         | 1.252         |
| Mg         | 1.98                                    | 1.89                                     | 1.512         | 1.600         |
| Y          | 1.5                                     | 2.02                                     | 1.488         | 5.156         |
| Ti         | 1.0                                     | 1.0                                      | 1.237         | 1.223         |
| Zr         | 1.0                                     | 1.0                                      | 1.222         | 1.170         |
| Hf         | 0.66                                    | 0.66                                     | 1.259         | 1.267         |
| Re         | 2.67                                    | 2.0                                      | 1.423         | 2.157         |
| Co (FM)    | 2.0                                     | 2.0                                      | 1.553         | 2.390         |
| Zn         | 1.0                                     | 1.0                                      | 1.213         | 1.151         |
| Cd         | 1.0                                     | 1.0                                      | 1.160         | 1.112         |

in the model expects that the larger $U_{1,2}$ would lead to the narrower $w$. As expected, we observe that the cores of the partials are generally wider in dislocations of Mg and Y, with the smaller peak energies than those of Be, which has the highest $U_{1}$ and $U_{2}$ of this group.

We see that, in Mg and Y, the dislocation structures are asymmetric with the width $w_{\mathrm{l}}$ of the left partial generally larger than $w_{\mathrm{r}}$ for the right one. The asymmetry can be quantified by the ratio of $w_{\mathrm{l}}/w_{\mathrm{r}}$, which is also given in Table VI. In the case of the edge dislocation, in Mg, the asymmetry is noticeable with $w_{\mathrm{l}}/w_{\mathrm{r}}$ slightly less than 2.0, and less so in Y with $w_{\mathrm{l}}/w_{\mathrm{r}}=1.5$. These differences result primarily from the different energetic pathways on the GSFE curve corresponding to their displacement. The energetic path for the left partial as it displaces in the negative $\langle 11\overline{2}3\rangle$ direction follows the right-hand portion of the GSFE and is affected by the second peak $U_{2}$. This path is different from that taken by the right partial, which displaces in the positive $\langle 11\overline{2}3\rangle$ direction and is, hence, dictated by $U_{1}$.

We performed a second set of calculations considering isotropic elasticity in place of the more realistic anisotropic elasticity. The split distances $R_{\mathrm{e}}$ and asymmetries between the two partials are not noticeably affected by elastic anisotropy. Exceptions are a slight decrease in $R_{\mathrm{e}}$ for the edge dislocation in Be from 18.17 to $16.26\ \mathring{\mathrm{A}}$ and a slight increase for the screw dislocation in Mg from 17.66 to $19.02\ \mathring{\mathrm{A}}$ when isotropy is assumed.

### C. Ti, Zr, and Hf

In this section, the equilibrium structures of dislocations for group IV HCP metals (Ti, Zr, and Hf) are examined. The GSFE curves for this group have similar shapes with a distinct local minimum located at $x_{l}/b=0.43$–0.44, which deviates significantly from the ideal 0.5. In each case, the two local maxima, $U_{1}$ and $U_{2}$, are not significantly different in value.

Figure 5 presents $\zeta$ and $d\zeta/dx$ for screw and edge dislocations in these metals after equilibrium is achieved. Like the previous metals, the dislocations in this group do not maintain a compact core. They dissociate into two distinct partials, which for all three metals are unequal in value, with the left one being noticeably smaller, by 18%, than the right one. This uneven split is an outcome of the relatively short critical shear displacement of $0.43b$–$0.44b$ needed to achieve the local minimum fault in all their GSFE curves. The

![](./images/812479005998448641_6.jpg)

**FIG. 5.** The order parameter, $\zeta$ (dotted lines), and its density, $/dx$ (solid lines), along the $[11\overline{2}3]$ slip direction for an initialized edge and screw dislocation in Ti, Zr, and Hf. The coloring follows Fig. 4.

![](./images/812479005998448641_7.jpg)

FIG. 6. The order parameter, $\zeta$ (dotted lines), and its density, $d\zeta/dx$ (solid lines), along the [11$\overline{2}$3] slip direction for an initialized edge and screw dislocation in Re and Co (FM). The coloring follows Fig. 4.

separation distances $R_{\mathrm{e}}$ of these partials belonging to the edge dislocations are 28.77, 22.23, and 29.66 Å for Zr, Ti, and Hf, respectively. Compared to the edge dislocations, in all metals in this group, $R_{\mathrm{e}}$ for screw dislocations are smaller, 16.44, 12.35, and 20.22 Å for Zr, Ti, and Hf, respectively.

Table V lists the partial widths, $w$, as defined by the FWHM method in the two peaks in $\zeta$. Two of the metals, Zr and Ti, feature a symmetric core structure with $w_{\mathrm{l}}/w_{\mathrm{r}}=1.0$. Hf, on the other hand, exhibits an asymmetric core, unlike Zr and Ti, with $w_{\mathrm{l}}/w_{\mathrm{r}}=0.66$.

The same calculations under the assumption of elastic isotropy are also shown in the same plots for comparison. Elastic anisotropy of Ti and Zr leads to wider $R_{\mathrm{e}}$ than when the anisotropy is removed. The edge dislocation in Ti exhibits the greatest increase in $R_{\mathrm{e}}$ from 17.29 Å (isotropic) to 22.23 Ar- ing; (anisotropic). For Hf, on the other hand, elastic anisotropy does not lead to significant changes in $R_{\mathrm{e}}$ or its asymmetric structure.

## D. Re and Co

Next, we study the equilibrium core structures of dislocations in the group VII and IX HCP metals: Re and Co. Their GSFE curves were compared to others previously in Fig. 1(a). An important distinguishing feature of their energetic landscapes compared to the other eight metals is their significant differences between their two peak energies $U_{1}$ and $U_{2}$. $U_{2}$ is 30% higher than $U_{1}$ in Re and 36% higher than $U_{1}$ in Co.

Figure 6 presents their equilibrium dislocation structures. These two metals share many common features, with the most prominent one being their asymmetric structure, compared to the dislocation structures of other metals. They both dissociate into two partials that are unequal in Burgers vector value and core width. The Burgers vector left partial is approximately 15% smaller in length than that of the right one and its width is twice as large. The widths of the partial cores are some of the largest compared to the other metals, even though their lattice parameters are not. Re has the larger $R_{e}$ of 29.46 and 20.03 Å for the edge and screw dislocations, respectively. Co has a smaller $R_{e}$ of 23.33 and 16.97 Å for the two dislocations, respectively.

For comparison, the calculated structures using their isotropic equivalent elastic properties are also included in these profiles. Elastic anisotropy has a negligible effect on the splitting distance of both the edge and screw dislocations. Only a very slight increase is seen in the $R_{\mathrm{e}}$ for the screw dislocation in Co due to elastic anisotropy; $R_{\mathrm{e}}=15.91$ Å for isotropy compared to 16.97 Å for anisotropy.

## E. Zn and Cd

The last two metals studied are Zn and Cd, which are group XII metals. The GSFE curves for these materials were presented previously in Fig. 1(a). Compared to the other metals, they have the lowest unstable SFEs $U_{1}$ and $U_{2}$. Also, unique to this group, their $c/a$ ratios are larger than the ideal value, and

![](./images/812479005998448641_8.jpg)

FIG. 7. The order parameter, $\zeta$ (dotted lines), and its density, $d\zeta/dx$ (solid lines), along the $[11\bar{2}3]$ slip direction for initial edge and screw dislocations in Zn and Cd. The coloring follows Fig. 4.

the displacement $x_{I}/b$ at which the local minimum is achieved is greater than 0.5 (located at 0.52–0.53). The displacements corresponding to the unstable SFEs are also larger than those of the other metals.

Figure 7 shows the calculated $\zeta$ and $d\zeta/dx$ profiles for the equilibrium cores for the edge and screw dislocations in Zn and Cd. Their splitting distances, $R_{\rm e}$, are 26.94 and 24.60 Å for the edge and screw dislocations for Zn, and 26.73 and 17.37 Å for Cd.

The dislocation structures of these two metals are nearly symmetric. The widths of their two partials are nearly equal. Although, like the other metals, the Burgers vectors of the two partials are not precisely equal in length, the difference is not significant (within $\pm 0.02$ Å). Due to the larger displacement offset of the local minimum in their GSFE curves, the value of the Burgers vector of the left partial is slightly larger than the right one.

Figures 7(a)–7(d) show that anisotropy has a significant effect on the equilibrium splitting distances for both Zn and Cd. These group XII elements are the only materials here to exhibit a much narrower $d\zeta/dx$ peak separation distance when anisotropy is taken into consideration. In Zn, for the edge dislocation, $R_{\rm e}$ reduces to 26.94 Å under elastically anisotropic conditions from an isotropic one of 42.17 Å; for the screw dislocation, $R_{\rm e}$ reduces to 24.60 Å under elastically anisotropic properties from $R_{e}$ of 30.45 Å under isotropic ones. Cd shows a similar trend, with $R_{\rm e}$ values of 26.73 and 37.42 Å for the edge dislocation with elastic anisotropy and isotropic isotropy, respectively. Finally, in the screw case in Cd, we see $R_{e}$ equal to 17.37 and 22.72 Å for the elastic anisotropic and isotropic cases, respectively.

## IV. DISCUSSION

From the DFT calculations, we find that these metals bear different levels of elastic anisotropy and different maxima and minima in their GSFE curves. In PFDD calculations, these properties are directly taken into account, and as the results have shown, the dissociation process leads to dislocation cores that deviate from the ideal picture, particularly showing partial dislocations with noncompact cores that are unequal in their widths and Burgers vectors. With all ten HCP metals in hand, we identify in the next few sections the material properties that govern their core structure.

### A. Scaling of core size with the intrinsic stacking fault energy

The analytical model in Eq. (2) expects that the intrinsic SFE, $I$, has the most pronounced effect on the $R_{\rm e}/b$. Figure 8 presents the variation in the PFDD calculated distances when considering anisotropy, $R_{\rm e}/b$, with $I/(Kb)$, as expected from the analytical model in Eq. (2). $R_{\rm e}/b$ shows a strong inverse scaling with $I/(Kb)$. Metals Ti and Y have the largest $I/(Kb)$ and also the narrowest $R_{\rm e}/b \approx 2$–3, while Zn and Be with the smallest $I/(Kb)$ have the widest $R_{\rm e}/b \approx 5$–6. The inverse scaling reflects the same basic principle used in the analytical

![](./images/812479005998448641_9.jpg)

FIG. 8. The equilibrium partial separation distance $R_{\mathrm{e}}$, calculated using PFDD plotted against (a) the intrinsic SFE $I$ normalized by $Kb$, and (b) the unstable SFE $U_{2}$, also normalized by $Kb$. Expressions for $K$ are given in Ref. [23].

model, namely that an SFW at low $I$ comprises a large fraction of the entire core structure, and $I$ has a dominant effect on the equilibrium split distance.

Figure 8(b) examines the relationship between $R_{\mathrm{e}}$ and the higher maxima $U_{2}$ in the GSFE curve. A remarkably strong inverse scaling in $U_{2}/(Kb)$ emerges. A similar analysis with $U_{1}/(Kb)$ does not show a strong trend, and it can be found in Fig. 11 in Appendix C. In the dissociation process, the partial dislocations move apart, and evidently it is the higher maximum $U_{2}$ that affects the resistance.

To date, the analytical model in Eq. (2) was the only application used to predict $R_{\mathrm{e}}/b$ for the pyramidal-II dislocations for just some of the HCP metals studied here. This work quantifies the equilibrium stacking fault width as well as other inherent features of the dislocation structure on the pyramidal-II plane for all ten HCP materials. Results indicate that as expected from theory, $R_{\mathrm{e}}/b$ scales inversely with $I/(Kb)$ and is minimally impacted by $U_{1}/(Kb)$ and $U_{2}/(Kb)$. The key difference is that the scaling is not as strong as the analytical model predicts and is not profoundly affected by the anisotropy in its elasticity properties inherent to HCP metals.

### B. Origin of the asymmetric cores
The analysis so far has indicated that the asymmetry in the dislocation structures is not a consequence of elastic anisotropy. The dislocation cores from the anisotropic and isotropic equivalent calculations exhibit very similar, if not the same, asymmetries. The properties of the GSFE curves of the individual metals, on the other hand, are highly influential. In particular, the core widths of the partials are affected by the depth of the local minimum in the GSFE. Shallow energy wells, for instance, would suggest that a broad partial core, in which the partial Burgers vector is distributed in plane, is more energetically favorable than the formation of the compact partial core bordering a minimum energy intrinsic stacking fault.

Here we observe that the GSFE curves of all ten HCP metals exhibit some degree of asymmetry about the local minimum state. The two local maxima, $U_{1}$ and $U_{2}$, are unequal, and hence the local minimum lies at different depths with respect to $U_{1}$ and $U_{2}$. The left partial, as it displaces left in the negative slip direction, is affected by $D_{2}$, and the right one, as it displaces in the positive slip direction, by $D_{1}$. With depth quantified by $D=(U-I)/U$, their differences can be measured by comparing $D_{1}=(U_{1}-I)/U_{1}$ and $D_{2}=(U_{2}-I)/U_{2}$ in each GSFE curve. Table VI summarizes the ratios $U_{2}/U_{1}$ and $D_{2}/D_{1}$ for each metal. A correlation can be identified by comparing $D_{2}/D_{1}$ with $w_{1}/w_{\mathrm{r}}$. The more symmetric core widths have nearly equal depths within $20\%$. Those metals with GSFE curves with greater differences, where $D_{2}/D_{1}$ is large, such as Mg, Y, and Re, have highly asymmetric cores.

### C. Effect of elastic anisotropy
The equilibrium core structures calculated assuming effective isotropic or actual anisotropic elastic properties are similar in many features. For instance, many of the asymmetric properties of the core are retained even when the anisotropy is removed by using the effective isotropic constants. The primary effect of anisotropy is, in some cases, either to narrow or widen the equilibrium split distance, $R_{\mathrm{e}}$. Qualitatively, these effects only confirm that the dominant contribution of elasticity is to control the elastic repulsive interactions between the two partials.

In theory, the ratio of the anisotropic to isotropic $R_{\mathrm{e}}^{\mathrm{ani}}/R_{\mathrm{e}}^{\mathrm{iso}}$ should scale with the ratio of the preenergy factors, $K/\mu$ from Eq. (2), the analytical calculation for the stacking fault widths. Figure 9(a) shows the variation in the ratio of $R_{\mathrm{e}}^{\mathrm{ani}}/R_{\mathrm{e}}^{\mathrm{iso}}$, determined using PFDD, with the calculated preenergy factor $K/\mu$ for both edge and screw dislocations. The calculations follow the expected scaling, although we see that cases in which the anisotropic and isotropic separations were nearly equivalent correspond to a range of $K/\mu=1.05$-$1.2$. Yet we still find that in most cases, the anisotropic $R_{\mathrm{e}}$ is wider than the isotropic one when $K/\mu$ is much greater than unity and vice versa when it is much less than unity.

Over the years, many factors have been proposed to quantify the level of elastic anisotropy in HCP metals, some of which we have included in Appendix D for completeness. Knowing which anisotropic indexes best capture certain material behavior could be important to larger length scale models,

![](./images/812479005998448641_10.jpg)

FIG. 9. The ratio of the anisotropic to the isotropic equilibrium SFW $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}$ plotted against (a) the anisotropic energy factor, $K$, normalized by the shear modulus, $\mu$, and (b) the logarithmic Euclidean anisotropy index, $A^{L}$, for both edge and screw dislocation dissociation.

which cannot model discrete deformation behaviors. There have been many different anisotropic indexes (see Table IX for the calculations of $\alpha$, $\beta$, and $\gamma$, as well as Fig. 12 depicting their relationship, if any, to the ratio $R^{\mathrm{ani}} / R^{\mathrm{iso}}$ for edge and screw dislocations) that do not consistently describe the impact elastic anisotropy can have on the equilibrium stacking fault width.

Recently, however, a measure of the distance between the upper and lower bounds of the fourth-ranked elasticity tensor was used to develop an index $A^{L}$, applicable to all classes of elastic anisotropy [78]. Here we apply $A^{L}$ to quantify the level of anisotropy among the ten HCP materials. $A^{L}$ is defined as

$$
A^{L}=\sqrt{\left[\ln \left(\frac{\kappa^{\mathrm{V}}}{\kappa^{\mathrm{R}}}\right)\right]^{2}+5\left[\ln \left(\frac{\mu^{\mathrm{V}}}{\mu^{\mathrm{R}}}\right)\right]^{2}}, \tag{13}
$$

where the bulk $(\kappa^{\mathrm{V}}, \kappa^{\mathrm{R}})$ and shear moduli $(\mu^{\mathrm{V}}, \mu^{\mathrm{R}})$ are calculated following the Voigt and Reuss averages, respectively. By definition, for an ideally isotropic material, $A^{L}=0$.

Table VII shows the $A^{L}$ factors, as well as all the other indicators, for all metals here. According to $A^{L}$, Y is the most isotopic HCP metal and Zn the most anisotropic. Figure 9 plots the ratio of the anisotropic to isotropic $R_{\mathrm{e}}$ against $A^{L}$. The effect of anisotropy on the deviations is greater in the edge case than the screw case. It can be anticipated that the edge dislocations would be more sensitive to the level of anisotropy due to the more complex elastic stress state generated by edge dislocations than screw dislocations.

Significantly, Fig. 9(b) shows that the closer $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}$ is to unity, the smaller is the value of $A^{L}$, and vice versa. For instance, metals like Y, Re, and Mg, with the relatively lower values of $A^{L}$, have $R_{\mathrm{e}}$ values that are unchanged when isotropy is assumed in place of their actual anisotropy. It captures the fact that, while Mg may be nearly isotropic, it is not exactly isotropic, explaining the slight deviation of $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}$ of the screw dislocation from unity. As $A^{L}$ for the metal increases up to 0.2, $R_{\mathrm{e}}^{\mathrm{ani}}$ becomes increasingly greater than $R_{\mathrm{e}}^{\mathrm{iso}}$. Likewise, the $R_{\mathrm{e}}^{\mathrm{ani}}$ of Cd and Zn, which have the highest $A^{L}$ (>0.3), deviate the most from their isotropic $R_{\mathrm{e}}^{\mathrm{iso}}$ counterpart, although the effect is to shrink $R_{\mathrm{e}}^{\mathrm{ani}}$ with respect to $R_{\mathrm{e}}^{\mathrm{iso}}$.

The value for the preenergy factor $K/\mu$ in Fig. 9(a) does not adequately reflect the variation of $R^{\mathrm{ani}} / R^{\mathrm{iso}}$. We find in Fig. 9(b) that the closer $A^{L}$ is to zero, the closer the ratio $R^{\mathrm{ani}} / R^{\mathrm{iso}}$ is to unity, and vice versa, the higher the value of $A^{L}$, the greater the ratio $R^{\mathrm{ani}} / R^{\mathrm{iso}}$ diverges from unity. In this regard, the $K/\mu$ prefactor does not work as well as $A^{L}$.

The correlation is a significant result in light of the fact that three common indices are poor indicators of the degree of anisotropy. In Fig. 12(a), shown in Appendix D, we plot the $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}$ versus the other anisotropic indicator $\alpha$ [Eq. (D1)]. This factor is defined by only four of the five constants. Similar to $A^{L}$, for both the edge and screw character dislocations, larger $\alpha$ corresponds to higher deviations from ideally isotropic. Mg, Y, and Re present the lowest degree of anisotropy with the $\alpha$ indicator, and Zn and Cd show the highest deviation from isotropy. However, Be has a negative value for this indicator and is an outlier. We also test, in Appendix D, the performances of the other anisotropic indicators $\beta$ [Eq. (D2)] and $\gamma$ [Eq. (D3)], as shown in Figs. 12(b) and 12(c). As shown, the differences in the anisotropic and isotropic $R_{\mathrm{e}}$ exhibit no correlation with these other HCP anisotropy indicators for either the edge or screw-character dislocations. At least for dislocations, these anisotropy indicators do not gauge well the anisotropic effects on $R_{\mathrm{e}}$.

<table>
<caption>TABLE VII. Log-Euclidean anisotropy index, $A^{L}$, calculated using Eq. (13), and the bulk $(\kappa^{\mathrm{V}}, \kappa^{\mathrm{R}})$ and shear moduli $(\mu^{\mathrm{V}}, \mu^{\mathrm{R}})$ as defined by Voigt and Reuss, are calculated for the ten HCP materials. All values are determined using DFT calculated elastic constants shown in Table II.</caption>
<thead>
<tr>
<th>Material</th>
<th>$A^{L}$</th>
<th>$\kappa^{\mathrm{V}}$</th>
<th>$\kappa^{\mathrm{R}}$</th>
<th>$\mu^{\mathrm{V}}$</th>
<th>$\mu^{\mathrm{R}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Be</td>
<td>0.033</td>
<td>123.28</td>
<td>122.69</td>
<td>154.35</td>
<td>152.13</td>
</tr>
<tr>
<td>Mg</td>
<td>0.018</td>
<td>36.37</td>
<td>36.35</td>
<td>19.26</td>
<td>19.10</td>
</tr>
<tr>
<td>Y</td>
<td>0.005</td>
<td>40.01</td>
<td>40.01</td>
<td>25.65</td>
<td>25.58</td>
</tr>
<tr>
<td>Ti</td>
<td>0.173</td>
<td>118.21</td>
<td>118.17</td>
<td>35.67</td>
<td>33.01</td>
</tr>
<tr>
<td>Zr</td>
<td>0.092</td>
<td>97.74</td>
<td>97.36</td>
<td>30.23</td>
<td>29.01</td>
</tr>
<tr>
<td>Hf</td>
<td>0.021</td>
<td>114.34</td>
<td>114.26</td>
<td>54.05</td>
<td>53.55</td>
</tr>
<tr>
<td>Re</td>
<td>0.028</td>
<td>378.89</td>
<td>378.86</td>
<td>177.61</td>
<td>175.42</td>
</tr>
<tr>
<td>Co (FM)</td>
<td>0.075</td>
<td>210.18</td>
<td>210.16</td>
<td>106.11</td>
<td>102.61</td>
</tr>
<tr>
<td>Zn</td>
<td>0.509</td>
<td>71.43</td>
<td>60.11</td>
<td>39.58</td>
<td>31.95</td>
</tr>
<tr>
<td>Cd</td>
<td>0.341</td>
<td>46.64</td>
<td>42.01</td>
<td>12.51</td>
<td>10.82</td>
</tr>
</tbody>
</table>

![](./images/812479005998448641_11.jpg)

FIG. 10. The standard (a) and relaxed (b) GSFE surfaces for the pyramidal-II plane in Mg. The x- and y-axis values are normalized by the magnitude of a direct lattice translation vector along the $\langle 11\overline{2}3\rangle$ and $\langle \overline{1}100\rangle$ directions, respectively.

## V. CONCLUSIONS

In this work, we use phase-field dislocation dynamics (PFDD) to calculate the size and structural properties of pyramidal-II $\langle c+a\rangle$ dislocations in ten HCP metals: Be, Cd, Co, Hf, Mg, Re, Ti, Y, Zn, and Zr. These metals vary widely in their $c/a$ ratio and degree of elastic anisotropy. As part of the formulation, the calculation incorporates generalized stacking fault energy (GSFE) curves for the pyramidal-II plane calculated from density functional theory (DFT). Among these metals, the GSFE curves are similar in shape but vary significantly in the location and value of their two local maxima and local minimum $I$. In addition, for Co, magnetism is shown to play a vital role in achieving a local minimum energy in its GSFE. With DFT informed PFDD simulations of the dissociation process of both perfect screw and edge dislocations to their low energy, equilibrium structures are obtained. For all metals, the equilibrium dislocation structures of both edge and screw character are not compact, but they extend bounded by two partial dislocations. Their splitting distances, $R_\text{e}$, are found to range from 1.2 to 3 nm. We show that $R_\text{e}/b$ scales inversely with the local minimum $I/(\mu b)$. For some metals, the structures are asymmetric, wherein the core widths of the two partial dislocations are not exactly equal, deviating from the classic picture from dislocation theory. The asymmetries in these cases can be explained by significantly unequal maxima in the GSFE curves. The elastic anisotropy is shown to not affect asymmetry between the partial Burgers vectors or core widths. We show that the stronger the degree of elastic anisotropy, as measured by the $A^L$ factor, the stronger the effect on $R_\text{e}$. The influence, whether widening or narrowing the core relative to isotropy, depends on the degree of anisotropy and the screw/edge character of the dislocation.

## ACKNOWLEDGMENTS

C.A. was supported by the Department of Defense (DoD) through the National Defense Science & Engineering Graduate Fellowship (NDSEG) Program. A.H. gratefully acknowledges support from the Materials project within the Physics and Engineering Models (PEM) Subprogram element of the Advanced Simulation and Computing (ASC) Program at Los Alamos National Laboratory (LANL), USA. I.J.B. acknowledges financial support from the National Science Foundation (NSF CMMI-1728224). Use was made of computational facilities purchased with funds from the National Science Foundation (CNS-1725797) and administered by the Center for Scientific Computing (CSC). The CSC is supported by the California NanoSystems Institute and the Materials Research Science and Engineering Center (MRSEC; NSF DMR 1720256) at UC Santa Barbara.

## APPENDIX A: GSFE SURFACE

Figure 10 shows 2D GSFE surfaces for the pyramidal-II plane in Mg calculated with standard and $x$-relaxed methods for determining GSFEs [21,41] using DFT. In the standard method, we shift the upper half of the crystal with respect to the lower half of the crystal on the pyramidal-II plane in small displacements and only allow atomic positions along the $z$-direction to relax. In the $x$-relaxed method, we also allow for an additional relaxation along the $\langle \overline{1}100\rangle$ direction. Additional relaxation normal to $\langle 11\overline{2}3\rangle$ allows for local rearrangement of

![](./images/812479005998448641_12.jpg)

FIG. 11. The equilibrium SFW $R_\text{e}$ plotted against the unstable SFE, $U_1$, normalized by the anisotropic energy factor, $K$, and the Burgers vector, $b$.

![](./images/812479005998448641_13.jpg)

FIG. 12. The ratio of the anisotropic to the isotropic equilibrium SFW $R_{\mathrm{e}}^{\mathrm{ani}}/R_{\mathrm{e}}^{\mathrm{iso}}$ plotted against the anisotropy indices (a) $\alpha$, (b) $\beta$, and (c) $\gamma$ for both edge and screw dislocation dissociation.

the atoms near the glide plane, which leads to a well-defined local minimum compared to a shallow minimum for the standard (unrelaxed) GSFE surface [41].

The lowest energetic path on the pyramidal-II GSFE surfaces, obtained using both the standard [Fig. 10(a)] and $x$-relaxed [Fig. 10(b)] methods, lies along the $\langle c+a\rangle$ edge, collinear to the $\langle 11\overline{2}3\rangle$ direction, energetically indicating that the partials will have only parallel components. This allows us to simplify the input for the periodic potential $\phi$, used in the $E^{\text{lattice}}$ calculation, Eq. (10), of the PFDD model, from the GSFE surface to the GSFE curve, that describes the governing energetics for the pyramidal-II plane. For this reason, we justify calculating only the GSFE curves for the remaining HCP materials, which would otherwise be too computationally time-consuming when using DFT to calculate the full GSFE surface. The full GSFE surface could be calculated with MS, however this method is dependent on interatomic potentials and could impact the position of the minima, and thus impact the PFDD results.

## APPENDIX B: EXPERIMENTAL ELASTIC CONSTANTS

The experimentally determined elastic constants are presented in Table VIII. The elastic constants calculated using DFT in Table II are in good agreement with these experimentally determined elastic constants.

TABLE VIII. Experimentally determined elastic constants (in GPa) for the ten HCP metals [62] for comparison with the DFT derived values in Table II.

<table>
<thead>
<tr>
<th>Material</th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C_{13}$</th>
<th>$C_{33}$</th>
<th>$C_{44}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Be</td>
<td>299.40</td>
<td>27.60</td>
<td>11.00</td>
<td>342.20</td>
<td>166.20</td>
</tr>
<tr>
<td>Mg</td>
<td>63.48</td>
<td>25.94</td>
<td>21.70</td>
<td>66.45</td>
<td>18.47</td>
</tr>
<tr>
<td>Y</td>
<td>83.40</td>
<td>29.10</td>
<td>19.00</td>
<td>80.10</td>
<td>26.90</td>
</tr>
<tr>
<td>Ti</td>
<td>176.10</td>
<td>86.90</td>
<td>68.30</td>
<td>190.50</td>
<td>50.80</td>
</tr>
<tr>
<td>Zr</td>
<td>155.40</td>
<td>67.20</td>
<td>64.60</td>
<td>172.50</td>
<td>36.30</td>
</tr>
<tr>
<td>Hf</td>
<td>190.10</td>
<td>74.50</td>
<td>65.50</td>
<td>204.40</td>
<td>60.00</td>
</tr>
<tr>
<td>Re</td>
<td>634.40</td>
<td>266.00</td>
<td>202.00</td>
<td>701.60</td>
<td>169.10</td>
</tr>
<tr>
<td>Co (FM)</td>
<td>319.50</td>
<td>166.10</td>
<td>102.00</td>
<td>373.60</td>
<td>82.40</td>
</tr>
<tr>
<td>Zn</td>
<td>179.09</td>
<td>37.50</td>
<td>55.40</td>
<td>68.80</td>
<td>45.95</td>
</tr>
<tr>
<td>Cd</td>
<td>129.23</td>
<td>39.99</td>
<td>40.95</td>
<td>56.68</td>
<td>24.20</td>
</tr>
</tbody>
</table>

## APPENDIX C: VARIATION OF $R_{\mathrm{e}}$ WITH THE LOWER UNSTABLE STACKING FAULT ENERGY

We compared the equilibrium SFW $R_{\mathrm{e}}$ against the three critical energetic values on the GSFE curve ($U_{1}$, $I$, and $U_{2}$). Previously shown in Fig. 8(a), $R_{\mathrm{e}}$ inversely scales with the local energetic minimum, the intrinsic stacking fault energy $I$, in accordance with the predictions from the analytical model [Eq. (2)], which doesn't take into consideration either of the unstable stacking fault energies. Interestingly, we found the strongest inverse scaling trend with the global energetic maximum $U_{2}$, shown in Fig. 8(b). For completeness, Fig. 11 shows the equilibrium SFW $R_{\mathrm{e}}$ plotted against $U_{1}$, the lesser of the two unstable stacking fault energies on the GSFE curve ($U_{1}<U_{2}$). This analysis with $U_{1}$ does not show as strong a trend as can be found in the comparison with $I$ and $U_{2}$.

## APPENDIX D: ADDITIONAL MEASURES OF ELASTIC ANISOTROPY

Figure 11 shows the equilibrium SFW $R_{\mathrm{e}}$ plotted against the unstable SFE, and Table IX presents the traditionally used anisotropic indices $\alpha$, $\beta$, and $\gamma$, calculated in Eqs. (D1)-(D3).

TABLE IX. Traditionally used anisotropic indices $\alpha$, $\beta$, and $\gamma$, calculated in Eqs. (D1)-(D3). All values are determined using DFT calculated elastic constants shown in Table II.

<table>
<thead>
<tr>
<th>Material</th>
<th>$\alpha$</th>
<th>$\beta$</th>
<th>$\gamma$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Be</td>
<td>$-3.232$</td>
<td>$0.806$</td>
<td>$1.008$</td>
</tr>
<tr>
<td>Mg</td>
<td>$1.130$</td>
<td>$1.039$</td>
<td>$1.272$</td>
</tr>
<tr>
<td>Y</td>
<td>$0.953$</td>
<td>$0.984$</td>
<td>$1.120$</td>
</tr>
<tr>
<td>Ti</td>
<td>$0.913$</td>
<td>$0.670$</td>
<td>$1.401$</td>
</tr>
<tr>
<td>Zr</td>
<td>$0.697$</td>
<td>$1.050$</td>
<td>$1.681$</td>
</tr>
<tr>
<td>Hf</td>
<td>$0.833$</td>
<td>$0.952$</td>
<td>$1.230$</td>
</tr>
<tr>
<td>Re</td>
<td>$0.944$</td>
<td>$1.018$</td>
<td>$1.332$</td>
</tr>
<tr>
<td>Co (FM)</td>
<td>$1.076$</td>
<td>$1.044$</td>
<td>$1.610$</td>
</tr>
<tr>
<td>Zn</td>
<td>$2.661$</td>
<td>$1.908$</td>
<td>$0.564$</td>
</tr>
<tr>
<td>Cd</td>
<td>$2.150$</td>
<td>$2.218$</td>
<td>$1.390$</td>
</tr>
</tbody>
</table>

CLAIRE ALBRECHT *et al.*

PHYSICAL REVIEW MATERIALS **5**, 043602 (2021)

Here we present results for the measures of elastic anisotropy in HCP materials conventionally referred to as $\alpha$, $\beta$, and $\gamma$, and they are related to the elastic constants by [79]

$$
\alpha=\frac{C_{11}+C_{12}-C_{33}}{C_{13}}, \tag{D1}
$$

$$
\beta=\frac{C_{66}}{C_{44}}, \tag{D2}
$$

$$
\gamma=\frac{1}{2 C_{44}}\left[\frac{C_{33}+C_{11}+C_{12}}{2}-\frac{C_{13} \sqrt{\alpha^{2}+8}}{2}\right]. \tag{D3}
$$

We note that only the last anisotropy factor, $\gamma$, contains all five independent elastic constants of an HCP metal.

Figure 12 presents the ratio of the anisotropic to isotropic equilibrium SFW $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}$ compared to these anisotropic indices: $\alpha$ (a), $\beta$ (b), and $\gamma$ (c). The points where $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}=1$ are spread out across various index values, demonstrating the inefficiency of these indices at predicting the scaling effect of elastic anisotropy on the equilibrium SFW between materials. When compared to the Log-Euclidean anisotropy index $A_{L}$ in Fig. 9(b), we can see that points where $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}=1$ are densely packed and that the greater the value of $A_{L}$, the more likely $R_{\mathrm{e}}^{\mathrm{ani}} / R_{\mathrm{e}}^{\mathrm{iso}}$ will diverge from 1, making it a more suitable index for predicting the effect of elastic anisotropy on the equilibrium SFW for each material.

[1] M. Knezevic, I. J. Beyerlein, T. A. Sisneros, and C. N. Tomé, A polycrystal plasticity model for predicting mechanical response and texture evolution during strain-path changes: Application to beryllium, *Int. J. Plast.* **49**, 185 (2013).

[2] E. Cerreta, C. A. Yablinsky, G. T. Gray, III, S. V. Vogel, and D. W. Brown, The influence of grain size and texture on the mechanical response of high purity hafnium, *Mater. Sci. Eng. A* **456**, 243 (2007).

[3] L. B. Addessio, E. K. Cerreta, and G. T. Gray, III, Mechanical behavior of zirconium and hafnium in tension and compression, *Metall. Mater. Trans. A* **36A**, 2893 (2005).

[4] S. I. Choi and J. H. Kim, Radiation-induced dislocation and growth behavior of zirconium and zirconium alloys - A review, *Nucl. Eng. Tech.* **45**, 385 (2013).

[5] Y. Q. Guo, S. H. Zhang, I. J. Beyerlein, D. Legut, S. L. Shang, Z. K. Liu, and R. F. Zhang, Synergetic effects of solute and strain in biocompatible Zn-based and Mg-based alloys, *Acta Mater.* **181**, 423 (2019).

[6] I. J. Beyerlein, X. Zhang, and A. Misra, Growth twins and deformation twins in metals, *Annu. Rev. Mater. Res.* **44**, 329 (2014).

[7] D. Coutsouradis, A. Davin, and M. Lamberigts, Cobalt-based superalloys for applications in gas turbines, *Mater. Sci. Eng.* **88**, 11 (1987).

[8] J. K. Tien, T. E. Howson, G. L. Chen, and X. S. Xie, Cobalt availability and superalloys, *JOM* **32**, 12 (1980).

[9] T. Obara, H. Yoshinga, and S. Morozumi, $11 \overline{2} 2\langle 1123\rangle$ Slip system in magnesium, *Acta Metall.* **21**, 845 (1973).

[10] M. Zecevic, I. J. Beyerlein, and M. Knezevic, Activity of pyramidal I and II $\langle c+a\rangle$ slip in Mg alloys as revealed by texture development, *J. Mech. Phys. Solids* **111**, 290 (2018).

[11] H. Tonda and S. Ando, Effect of temperature and shear direction on yield stress by $11 \overline{2} 2\langle\overline{1} \overline{1} 23\rangle$ slip in HCP metals, *Metall. Mat. Trans. A* **33**, 831 (2002).

[12] C. M. Byer, B. Li, B. Cao, and K. T. Ramesh, Microcompression of single-crystal magnesium, *Scr. Mater.* **62**, 536 (2010).

[13] S. Ando and H. Tonda, Non-basal slip in magnesium-lithium alloy single crystals, *Mater. Trans.* **41**, 1188 (2000).

[14] Z. Ding, W. Liu, H. Sun, S. Li, D. Zhang, Y. Zhao, E. J. Lavernia, and Y. Zhu, Origins and dissociation of pyramidal $\langle c+a\rangle$ dislocations in magnesium and its alloys, *Acta Mater.* **146**, 265 (2018).

[15] Q. Yu, L. Qi, R. K. Mishra, J. Li, and A. M. Minor, Reducing deformation anisotropy to achieve ultrahigh strength and ductility in Mg at the nanoscale, *Proc. Natl. Acad. Sci. USA* **110**, 13289 (2013).

[16] M. A. Kumar and I. J. Beyerlein, Local microstructure and micromechanical stress evolution during deformation twinning in hexagonal polycrystals, *J. Mater. Res.* **35**, 217 (2020).

[17] M. Yoo, Slip, twinning, and fracture in hexagonal close-packed metals, *Metall. Trans. A* **12A**, 409 (1981).

[18] N. J. Kim, Critical Assessment 6: Magnesium sheet alloys: viable alternatives to steels? *Mater. Sci. Technol.* **30**, 1925 (2014).

[19] B.-C. Shuh, M. S. Shim, K. S. Shin, and N. J. Kim, Current issues in magnesium sheet alloys: Where do we go from here? *Scr. Mater.* **84-85**, 1 (2014).

[20] P. G. Partridge, The crystallography and deformation modes of hexagonal close-packed metals, *Metall. Rev.* **12**, 169 (1967).

[21] A. Kumar, B. Morrow, R. J. McCabe, and I. J. Beyerlein, An atomic-scale modeling and experimental study of $\langle c+a\rangle$ dislocations in Mg, *Mater. Sci. Eng. A* **695**, 270 (2017).

[22] J. P. Hirth and J. Lothe, *Theory of Dislocations*, 2nd ed. (Krieger, Florida, 1982).

[23] M. M. Savin, V. M. Chernov, and A. M. Strokova, Energy factor of dislocations in hexagonal crystals, *Phys. Status Solidi A* **35**, 747 (1976).

[24] J. Han, S. L. Thomas, and D. J. Srolovitz, Grain-boundary kinetics: A unified approach, *Prog. Mater. Sci.* **98**, 386 (2018).

[25] M. A. Meyers, A. Mishra, and D. J. Benson, Mechanical properties of nanocrystalline materials, *Prog. Mater. Sci.* **51**, 427 (2006).

[26] M. H. Yoo, S. R. Agnew, J. R. Morris, and K. M. Ho, Non-basal slip systems in HCP metals and alloys: source mechanisms, *Mater. Sci. Eng. A* **319-321**, 87 (2001).

[27] Y. Tang and J. A. El-Awady, Formation and slip of pyramidal dislocations in hexagonal close-packed magnesium single crystals, *Acta Mater.* **71**, 319 (2014).

[28] S. Sandlöbes, M. Friák, S. Zaefferer, A. Dick, S. Yi, D. Letzig, Z. Pei, L. F. Zhu, J. Neugebauer, and D. Raabe, The relation between ductility and stacking fault energies in Mg and Mg-Y alloys, *Acta Mater.* **60**, 3011 (2012).

[29] M. Itakura, H. Kaburaki, M. Yamaguchi, and T. Tsuru, Novel Cross-Slip Mechanism of Pyramidal Screw Dislocations in Magnesium, *Phys. Rev. Lett.* **116**, 225501 (2016).

[30] D. Buey, L. G. Hector, Jr., and M. Ghazisaeidi, Core structure and solute strengthening of second-order pyramidal $\langle c+a\rangle$ dislocations in Mg-Y alloys, *Acta Mater.* **147**, 1 (2018).

043602-16

[31] D. H. Kim, F. Ebrahimi, M. V. Manuel, J. S. Tulenko, and S. R. Phillpot, Grain-boundary activated pyramidal dislocations in nano-textured Mg by molecular dynamics simulation, Mater. Sci. Eng. A 528, 5411 (2011).

[32] R. L. Bell and R. W. Cahn, The dynamics of twinning and the interrelation of slip and twinning in zinc crystals, Proc. R. Soc. A 239, 494 (1957).

[33] M. Yoo, Interaction of slip dislocations with twins in HCP metals, Trans. Metall. Soc. AIME 245, 2051 (1969).

[34] S. Mendelson, Dislocation dissociations in hcp metals, J. Appl. Phys. 41, 1893 (1970).

[35] K. Yaddanapudi, B. Leu, M. A. Kumar, X. Wang, J. M. Schoenung, E. J. Lavernia, T. Rupert, I. J. Beyerlein, and S. Mahajan, Accommodation and formation of $\{\overline{1}012\}$ twin tips in an Mg-Y alloys, Acta Mater. 204, 116514 (2021).

[36] B. Yin, Z. Wu, and W. A. Curtin, Comprehensive first-principles study of stable stacking faults in hcp metals, Acta Mater. 123, 223 (2017).

[37] Y. Dou and J. Zhang, Effects of structural relaxation on the generalized stacking fault energies of hexagonal-close-packed system from first-principles calculations, Comput. Mater. Sci. 98, 405 (2015).

[38] C. Albrecht, A. Hunter, A. Kumar, and I. J. Beyerlein, A phase field model for dislocations in hexagonal close packed crystals, J. Mech. Phys. Solids 137, 103823 (2020).

[39] P. Kwaśniak, P. Špiewak, H. Garbacz, and K. J. Kurzydłowski, Plasticity of hexagonal systems: Split slip modes and inverse Peierls relation in $\alpha$-Ti, Phys. Rev. B 89, 144105 (2014).

[40] M. Ardeljan, D. J. Savage, A. Kumar, I. J. Beyerlein, and M. Knezevic, The plasticity of highly oriented nano-layered Zr/Nb composites, Acta Mater. 115, 189 (2016).

[41] A. Kumar, M. A. Kumar, and I. J. Beyerlein, First-principles study of crystallographic slip modes in $\omega$-Zr, Sci. Rep. 7, 8932 (2017).

[42] B. Syed, J. Geng, R. K. Mishra, and K. S. Kumar, [0001]Compression response at room temperature of single-crystal magnesium, Scr. Mater. 67, 700 (2012).

[43] K. Y. Xie, Z. Alam, A. Caffee, and K. J. Hemker, Pyramidal I slip in c-axis compressed Mg single crystals, Scr. Mater. 112, 75 (2016).

[44] J. F. Stohr and J. P. Poirier, Etude en microscopie electronique du glissement pyramidal {1122}⟨1123⟩ dans le magnesium, Philos. Mag. 25, 1313 (1972).

[45] F. Long, M. R. Daymond, Z. Yao, and M. A. Kirk, Deformation mechanism study of hot rolled Zr-2.5Nb alloy by transmission electron microscopy. II. In situ transmission electron microscopy study of deformation mechanism change of a Zr-2.5Nb alloy upon heavy ion irradiation, J. Appl. Phys. 117, 104302 (2015).

[46] F. Long, L. Balogh, and M. R. Daymond, Evolution of dislocation density in a hot rolled Zr-2.5Nb alloy with plastic deformation studied by neutron diffraction and transmission electron microscopy, Philos. Mag. 97, 2888 (2017).

[47] F. Long, J. Kacher, Z. Yao, and M. R. Daymond, A tomographic TEM study of tension-compression asymmetry response of pyramidal dislocations in a deformed Zr-2.5Nb alloy, Scr. Mater. 153, 94 (2018).

[48] Y. Minonishi, S. Morozumi, and H. Yoshinaga, {1122}⟨1123⟩ slip in titanium, Scr. Metall. 16, 427 (1982).

[49] K. Kishida, J. G. Kim, T. Nagae, and H. Inui, Experimental evaluation of critical resolved shear stress for the first-order pyramidal c+a slip in commercially pure Ti by micropillar compression method, Acta Mater. 196, 168 (2020).

[50] H. Fan and J. A. El-Awady, Towards resolving the anonymity of pyramidal slip in magnesium, Mater. Sci. Eng. A 644, 318 (2015).

[51] J. Geng, M. F. Chisholm, R. K. Mishra, and K. S. Kumar, An electron microscopy study of dislocation structures in Mg single crystals compressed along [0001] at room temperature, Philos. Mag. 95, 3910 (2015).

[52] Y. U. Wang, Y. M. Jin, A. M. Cuitiño, and A. G. Khachaturyan, Nanoscale phase field microelasticity theory of dislocations: model and 3D simulations, Acta Mater. 49, 1847 (2001).

[53] M. Koslowski, A. Cuitiño, and M. Ortiz, A phase-field theory of dislocations dynamics, strain hardening and hysteresis in ductile single crystals, J. Mech. Phys. Solids 50, 2597 (2002).

[54] V. V. Bulatov and E. Kaxiras, Semidiscrete Variational Peierls Framework for Dislocation Core Properties, Phys. Rev. Lett. 78, 4221 (1997).

[55] G. Schoeck, The generalized Peierls-Nabarro model, Philos. Mag. A 69, 1085 (1994).

[56] Y. Wang and J. Li, Phase field modeling of defects and deformation, Acta Mater. 58, 1212 (2010).

[57] S. Xu, J. R. Mianroodi, A. Hunter, I. J. Beyerlein, and B. Svendsen, Phase-field-based calculations of the disregistry fields of static extended dislocations in FCC metals, Philos. Mag. 99, 1400 (2019).

[58] S. Xu, Y. Su, and I. J. Beyerlein, Modeling dislocations with arbitrary character angle in face-centered cubic transition metals using the phase-field dislocation dynamics method with full anisotropic elasticity, Mech. Mater. 139, 103200 (2019).

[59] I. J. Beyerlein and A. Hunter, Understanding dislocation mechanics at the mesoscale using phase field dislocation dynamics, Philos. Trans. R. Soc. A 374, 20150166 (2016).

[60] X. Peng, N. Mathew, I. J. Beyerlein, K. Dayal, and A. Hunter, A 3D phase field dislocation dynamics model for body-centered cubic crystals, Comput. Mater. Sci. 171, 109217 (2020).

[61] S. Xu, Y. Su, L. T. W. Smith, and I. J. Beyerlein, Frank-Read source operation in six body-centered cubic refractory metals, J. Mech. Phys. Solids 141, 104017 (2020).

[62] G. Simmons and H. Wang, Single Crystal Elastic Constants and Calculated Aggregate Properties: A Handbook (MIT Press, Cambridge, MA, 1971).

[63] G. Kresse and J. Furthmüller, Efficiency of ab initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6, 15 (1996).

[64] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[65] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996).

[66] Y. Su, M. Ardeljan, M. Knezevic, M. Jain, S. Pathak, and I. J. Beyerlein, Elastic constants of pure body-centered cubic Mg in nanolaminates, Comput. Mater. Sci. 174, 109501 (2020).

[67] S. Xu, E. Hwang, W.-R. Jian, Y. Su, and I. J. Beyerlein, Atomistic calculations of the generalized stacking fault energies in two refractory multi-principal element alloys, Intermetallics 124, 106844 (2020).

[68] D. Chiba, S. Fukami, K. Shimamura, N. Ishiwata, K. Kobayashi, and T. Ono, Electrical control of the ferromagnetic phase transition in cobalt at room temperature, *Nat. Mater.* **10**, 853 (2011).

[69] Y. Su, S. Xu, and I. J. Beyerlein, Density functional theory calculations of generalized stacking fault energy surfaces for eight face-centered cubic transition metals, *J. Appl. Phys.* **126**, 105112 (2019).

[70] X. Wang, S. Xu, W.-R. Jian, X.-G. Li, Y. Su, and I. J. Beyerlein, Generalized stacking fault energies and Peierls stresses in refractory body-centered cubic metals from machine learning-based interatomic potentials, *Comput. Mater. Sci.* **192**, 110364 (2021).

[71] M. Ardeljan, M. Knezevic, M. Jain, S. Pathak, A. Kumar, N. Li, N. A. Mara, J. K. Baldwin, and I. J. Beyerlein, Room temperature deformation mechanism of Mg/Nb nanolayered composites, *J. Mater. Res.* **33**, 1311 (2018).

[72] J.-A. Yan, C.-Y. Wang, and S.-Y. Wang, Generalized-stacking-fault energy and dislocation properties in bcc Fe: A first-principles study, *Phys. Rev. B* **70**, 174105 (2004).

[73] J. R. Mianroodi, A. Hunter, I. J. Beyerlein, and B. Svendsen, Theoretical and computational comparison of models for dislocation dissociation and stacking fault/core formation in fcc systems, *J. Mech. Phys. Solids* **95**, 719 (2016).

[74] S. Xu, J. R. Mianroodi, A. Hunter, B. Svendsen, and I. J. Beyerlein, Comparative atomistic and continuum modeling of the disregistry and Peierls stress for dissociated edge and screw dislocations in Al, *Int. J. Plast.* **129**, 102689 (2020).

[75] *MATLAB and Curve Fitting Toolbox Release* (MathWorks, Natick, MA, 2016).

[76] M. Ghazisaeidi, L. G. Hector, and W. A. Curtin, First-principles core structures of $\langle c+a\rangle$ edge and screw dislocations in Mg, *Scr. Mater.* **75**, 42 (2014).

[77] Z. Wu, B. Yin, and W. A. Curtin, Energetics of dislocation transformations in hcp metals, *Acta Mater.* **119**, 203 (2016).

[78] C. M. Kube, Elastic anisotropy of crystals, *AIP Adv.* **6**, 095209 (2016).

[79] U. F. Kocks, C. N. Tomé, and H.-R. Wenk, *Texture and Anisotropy: Preferred Orientations in Polycrystals and their Effect on Materials Properties* (Cambridge University Press, Cambridge, 2008).