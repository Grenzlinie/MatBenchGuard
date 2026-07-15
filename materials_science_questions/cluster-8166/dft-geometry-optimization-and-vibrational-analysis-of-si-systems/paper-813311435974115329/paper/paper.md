PHYSICAL REVIEW B 85, 195315 (2012)

# Electronic properties of Si(111)-7 x 7 and related reconstructions:
## Density functional theory calculations

Manuel Smeu* and Hong Guo
Centre for the Physics of Materials and Department of Physics, McGill University, Montreal, Quebec, Canada

Wei Ji
Department of Physics, Renmin University of China, Beijing 100872, China

Robert A. Wolkow†
National Institute for Nanotechnology, National Research Council of Canada, Edmonton, Alberta, Canada

(Received 28 February 2012; published 14 May 2012)

The $7 \times 7$ reconstruction of Si(111) has the interesting property of being metallic despite bulk Si being a semiconductor. This surface has a complex reconstruction that takes on a dimer-adatom stacking fault (DAS) structure composed of adatoms, rest atoms, and several other key features. It is believed that the dangling bonds of the adatoms play a crucial role in the high conductivity and that this is predominantly a surface-state band effect. To elucidate the details of this mechanism, we investigate a set of related Si(111) reconstructions of increasing complexity in order to resolve the effect of the different DAS features on the electronic and transport properties of the Si(111)-$7 \times 7$ surface. Density functional theory calculations are carried out on the $\sqrt{3} \times \sqrt{3}$-$R30^{\circ}$, $2 \times 2$, $5 \times 5$, and $7 \times 7$ reconstructions of Si(111). Since these surfaces are modeled as two-dimensional slabs, a careful investigation is carried out to determine the slab thickness needed to capture the structural and electronic properties of these systems. The densities of states (DOSs) projected on different atoms in these surfaces are then compared, revealing that the $\sqrt{3} \times \sqrt{3}$, $5 \times 5$, and $7 \times 7$ surfaces are metallic, while the $2 \times 2$ surface is semiconducting. Finally, the DOSs for Si(111)-$7 \times 7$ are related to scanning tunneling microscope data to offer an explanation for different adatom prominence trends depending on Si sample doping.

DOI: 10.1103/PhysRevB.85.195315
PACS number(s): 73.20.—r, 68.35.bg, 31.15.E—

## I. INTRODUCTION

With the ongoing diminishing size of electronic devices, surface effects are becoming more and more important. $^{1-5}$ Of particular interest is the Si(111)-$7 \times 7$ reconstructed surface, which has metallic conducting properties despite bulk Si being a semiconductor. $^{6}$ This phenomenon must be well understood in order to reliably control and exploit this property in future electronic devices.

The Si(111)-$7 \times 7$ surface has received much attention due to its conductive properties and the longstanding mystery over its atomic structure. The dimer-adatom stacking fault (DAS) model was proposed by Takayanagi $et$ $al.;^{7}$ it consists of a $7 \times 7$ supercell as outlined by the dashed line in Fig. 1. The supercell is divided into a faulted ($F$) and an unfaulted ($U$) half. Each half contains six adatoms, represented by the orange spheres forming a triangle. This yields two distinct types of adatoms in each half of the supercell: those at the corners of the triangle and those at the center of each side. Inside this adatom triangle, there are three rest atoms, represented by the red spheres. Around the perimeter of the supercell and separating the two halves are dimers. Corner holes can also be seen at each corner of the supercell in Fig. 1. This is now the accepted structure of the Si(111)-$7 \times 7$ reconstruction.

Although this surface is known to conduct as a metal, there remains disagreement about its actual conductivity, with experimental results spanning over four orders of magnitude. $^{2}$ This uncertainty is attributed to the sensitivity to the sample quality and limitations of experimental techniques. Computational studies on the $7 \times 7$ reconstruction are also challenging due to its complex nature and sheer size. Parallel algorithms have made its study possible, $^{8}$ but it has been limited to models and approaches that may not fully capture the properties of this system. For example, Brommer $et$ $al.^{8}$ used density functional theory (DFT) with the local density approximation on a supercell geometry. Only the $\Gamma$ point of the Brillouin zone was used and only the top three Si layers were relaxed. Previously, Northrup used pseudopotential total energy calculations to obtain the electronic structure of a simpler model for Si-$7 \times 7$, namely, the Si(111)-$\sqrt{3} \times \sqrt{3}$ reconstruction. $^{9}$ Later on, Ihara $et$ $al.$ performed an ambitious DFT calculation on the $7 \times 7$ surface to obtain its electronic structure. $^{10}$ However, they used experimental data to set up the atomic coordinates in their system since structure relaxations on a system of that size (396 atoms) were not feasible at the time. With further technological improvements and increased availability of computational resources, it is now possible to carry out more accurate calculations on more realistic systems.

At this point, a thorough understanding of the features that give the Si(111)-$7 \times 7$ surface its interesting properties is needed. Namely, we need to study the effect of the adatoms, rest atoms, and other DAS features that make this surface conductive. To this end, electronic structure calculations were performed on several related reconstructions of Si(111) of increasing complexity, as shown in Fig. 2. The simplest is the $\sqrt{3} \times \sqrt{3}$-$R30^{\circ}$ reconstruction (simply referred to as $\sqrt{3} \times \sqrt{3}$ from here on), which only has adatoms out of the DAS features listed above. Next is the $2 \times 2$ reconstruction, which also has rest atoms. Yet more complex, the $5 \times 5$ reconstruction also includes dimers and corner holes. Finally, we have the $7 \times 7$ reconstruction, which has all of these features, including four kinds of adatoms: those at the corners of the supercell and those at the edges, which can be on the $F$ or $U$ half.

1098-0121/2012/85(19)/195315(9)
195315-1
©2012 American Physical Society

![](./images/813311435974115329_1.jpg)

FIG. 1. (Color online) Top (a) and side (b) views of the DAS structure for Si(111)-7 × 7. Adatoms are shown in orange, and rest atoms in red.

The idea is that by comparing these reconstructions of increasing complexity, we may resolve the effects of the different DAS features on the conductivity of Si(111)-7 × 7. Density functional theory (DFT) calculations were employed for atomic relaxations of these surfaces and in order to obtain the electronic structure. The calculated densities of states (DOSs) are then compared to scanning tunneling microscope data for the Si(111)-7 × 7 surface.

## II. COMPUTATIONAL DETAILS

All calculations have been carried out with the Vienna *Ab Initio* Simulation Package (VASP),¹¹,¹² using the Perdew-Burke-Ernzerhof generalized gradient approximation (PBE-GGA) for the exchange correlation energy.¹³ A projector-augmented-wave method was used for the ionic potentials,¹⁴,¹⁵ with a kinetic energy cutoff for the plane-wave basis of 400 eV. The structure relaxations proceeded until the net force on each atom (except those that were frozen) was less than 0.02 eV/Å. Since VASP calculations are for periodic systems, the surfaces were represented as slabs of finite thickness. A minimum of 14 Å of vacuum space separated atoms of one supercell from atoms of its image (next repeat unit) in the direction normal to the surface. In the plane of the surface, the Brillouin zone was sampled with sufficient $k$ points so that the energy was converged to less than 1 meV/atom. For the Si-$\sqrt{3} \times \sqrt{3}$ and Si-2 × 2 systems, 5 × 5 $k$ points were required in the plane of the surface, while the Si-5 × 5 and Si-7 × 7 systems required 3 × 3 $k$ points. For density of states (DOS) calculations, the $k$ sampling was more than doubled in each direction (21 × 21 for Si-$\sqrt{3} \times \sqrt{3}$ and Si-2 × 2, 11 × 11 for Si-5 × 5, and 7 × 7 for Si-7 × 7) and Gaussian broadening was used with a value of 0.05 eV.

![](./images/813311435974115329_2.jpg)

FIG. 2. (Color online) The four reconstructions of Si(111) studied in this work. The yellow parallelogram outlines one unit cell for each system.

## III. RESULTS

### A. Slab thickness testing

The slabs used to model the reconstructed surfaces are two-dimensional (2D) periodic structures of finite thickness (number of atomic layers). One side of each slab is reconstructed, while the atoms on the opposite side are held fixed in their bulk positions and their dangling bonds (DBs) are passivated with H atoms. Since the slab has a finite thickness, it is necessary to determine how many atomic layers are needed to properly treat these systems. The objective was to achieve convergence in terms of geometry and electronic structure with respect to the slab thickness.

To determine the minimum thickness required, the two smallest and simplest systems were considered: Si(111)-$\sqrt{3} \times \sqrt{3}$ and Si(111)-2 × 2. Structure relaxations were performed on 2, 4, 6, 8, and 10 layers of Si atoms (including the reconstructed bilayer). For example, Fig. 3 shows a cross-sectional view of 10 layers of Si(111)-$\sqrt{3} \times \sqrt{3}$ and Si(111)-2 × 2. To build each system with fewer layers, atoms were removed from the bottom (with H atoms used to cap the DBs at the bottom of the slab in each case). Note that at the start of the relaxations, all Si atoms other than those in the reconstructed bilayer were initially in bulk Si positions. The bottom bilayer was held frozen to bulk positions for the entire relaxation (for systems with two or four layers, only the bottom atomic layer

![](./images/813311435974115329_3.jpg)

FIG. 3. (Color online) Side view of 10-layer slabs of $\sqrt{3} \times \sqrt{3}$ (left) and 2 × 2 (right).

<table><caption>TABLE I. Bond distances (Å) for Si(111)-$\sqrt{3} \times \sqrt{3}$</caption>
<thead>
  <tr>
    <th>No. of layers</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
    <th>d</th>
    <th>e</th>
    <th>f</th>
    <th>g</th>
    <th>h</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2</td>
    <td>2.65</td>
    <td>2.41</td>
    <td>2.34</td>
    <td>2.43</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>2.50</td>
    <td>2.65</td>
    <td>2.36</td>
    <td>2.41</td>
    <td>2.30</td>
    <td>2.42</td>
    <td>2.40</td>
    <td>2.27</td>
  </tr>
  <tr>
    <td>6</td>
    <td>2.51</td>
    <td>2.64</td>
    <td>2.36</td>
    <td>2.41</td>
    <td>2.29</td>
    <td>2.43</td>
    <td>2.38</td>
    <td>2.34</td>
  </tr>
  <tr>
    <td>8</td>
    <td>2.51</td>
    <td>2.64</td>
    <td>2.36</td>
    <td>2.41</td>
    <td>2.29</td>
    <td>2.43</td>
    <td>2.38</td>
    <td>2.34</td>
  </tr>
  <tr>
    <td>10</td>
    <td>2.51</td>
    <td>2.65</td>
    <td>2.36</td>
    <td>2.41</td>
    <td>2.30</td>
    <td>2.43</td>
    <td>2.38</td>
    <td>2.34</td>
  </tr>
</tbody>
</table>

was frozen). All other atoms, including the capping H atoms, were then relaxed.

For the structure comparison, several Si–Si bond lengths near the surface (a–h in Fig. 3) were compared for slabs of different thicknesses. The values are summarized in Table I for Si(111)-$\sqrt{3} \times \sqrt{3}$ and in Table II for Si(111)-$2 \times 2$. With two layers, the bond lengths are quite different from those in the thicker systems. This is reasonable since the atoms in the bottom layer are frozen to bulk positions, and the system is too thin to adequately accommodate the reconstruction. With four layers, all the bond lengths are converged with the exception of the one labeled h in each system (Fig. 3). Again, this makes sense since, with four layers, this bond includes frozen atoms. For six and more atomic layers, the listed bond lengths are fully converged, with variations smaller than $0.01$ Å. Note that bond distances between atoms in lower layers were also verified and they agree to within $0.01$ Å for 6–10 layers.

As a further check of the quality of the geometries, the relative heights of the four inequivalent adatoms were compared in the relaxed Si(111)-$7 \times 7$ system with six atomic layers. We obtained the following trend in atomic heights: $CoF > CeF > CoU > CeU$, where $Co$ and $Ce$ signify corner and center adatoms, respectively. Our trend agrees with previous careful calculations, $^{16}$ as well as LEED, $^{17}$ STM, $^{18–20}$ and AFM experiments. $^{21,22}$ Additionally, bond lengths for all adatoms and rest atoms in the Si-$7 \times 7$ system were compared to those obtained by Brommer et al. in their earlier calculations. $^{8}$ The largest difference was for the bonds on the rest atoms, with values reported in Ref. 8 being shorter than those in this work by $0.04$ Å. Overall, there was good agreement for the Si-$7 \times 7$ structures.

To test convergence for the electronic structure, total DOS plots are compared for different numbers of layers, as shown in Fig. 4 for Si(111)-$\sqrt{3} \times \sqrt{3}$ and Si(111)-$2 \times 2$. The energy of interest is close to the Fermi level, $E_{\text{F}}$, since these are the states more relevant to the metallic properties of the surface. For each system, two layers clearly result in a very different DOS spectrum from those with more layers. With additional layers, the DOSs appear to systematically converge toward the plot for 10 layers. Note that the plots for 8 and 10 layers are almost identical near $E_{\text{F}}$, and the one for 6 layers is also quite reasonable.

Overall, the atomic structure converges faster than the electronic structure with respect to the thickness of the slab. In the interest of consistency, and because the $5 \times 5$ and $7 \times 7$ systems are so large and computationally intensive, we opted to treat all four reconstructions with six atomic layers. This provides us with a good balance of converged electronic structure near $E_{\text{F}}$, for systems of reasonable size. The relaxed atomic coordinates for the four reconstructions studied in this work are provided in the Appendix.

### B. Comparison of reconstructions

To gain a better understanding of the role that each DAS feature has on the surface conductivity of Si(111)-$7 \times 7$, the DOSs for several related Si(111) reconstructions of increasing complexity are compared. These are plotted in Fig. 5(a), with scaled units of the DOS intensity, for ease of comparison. The region of interest is around $E_{\text{F}}$, since those are the states that are responsible for the metallic properties of Si(111)-$7 \times 7$. The $\sqrt{3} \times \sqrt{3}$ reconstruction has some DOSs at $E_{\text{F}}$, suggesting that this surface might also have metallic properties. A little more complex is the $2 \times 2$ reconstruction, which has a DOS peak right beneath $E_{\text{F}}$, but it drops off at $E_{\text{F}}$, meaning that this system would have semiconducting properties. The $5 \times 5$ and $7 \times 7$ systems both have DOSs at and around $E_{\text{F}}$, as expected from the known metallic properties of Si(111)-$7 \times 7$. Note that these two systems actually have very similar spectra in terms of both their peak positions and their qualitative shapes, such as the prominent peak at $-0.5$ eV with a small shoulder at $-0.4$ eV, the overall shape of the DOS in the range $[-0.2,0.2]$ eV, and the prominent peak at $0.3$ eV.

Although the analysis of the total DOS for different reconstructions is informative, a more instructive comparison can be made by looking at the local DOS projected on specific atoms in each system (PDOS); in other words, the DOS associated with the orbitals of certain atoms. Figure 5(b) shows

<table><caption>TABLE II. Bond distances (Å) for Si(111)-$2 \times 2$.</caption>
<thead>
  <tr>
    <th>No. of layers</th>
    <th>a</th>
    <th>b</th>
    <th>c</th>
    <th>d</th>
    <th>e</th>
    <th>f</th>
    <th>g</th>
    <th>h</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2</td>
    <td>2.59</td>
    <td>2.38</td>
    <td>2.44</td>
    <td>2.45</td>
    <td>2.37</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>4</td>
    <td>2.49</td>
    <td>2.40</td>
    <td>2.40</td>
    <td>2.42</td>
    <td>2.38</td>
    <td>2.27</td>
    <td>2.41</td>
    <td>2.27</td>
  </tr>
  <tr>
    <td>6</td>
    <td>2.49</td>
    <td>2.42</td>
    <td>2.40</td>
    <td>2.42</td>
    <td>2.37</td>
    <td>2.28</td>
    <td>2.42</td>
    <td>2.35</td>
  </tr>
  <tr>
    <td>8</td>
    <td>2.49</td>
    <td>2.43</td>
    <td>2.40</td>
    <td>2.42</td>
    <td>2.37</td>
    <td>2.28</td>
    <td>2.42</td>
    <td>2.35</td>
  </tr>
  <tr>
    <td>10</td>
    <td>2.49</td>
    <td>2.43</td>
    <td>2.40</td>
    <td>2.42</td>
    <td>2.37</td>
    <td>2.29</td>
    <td>2.42</td>
    <td>2.35</td>
  </tr>
</tbody>
</table>

![](./images/813311435974115329_4.jpg)

FIG. 4. (Color online) DOS (arbitrary units) for (a) Si(111)-$\sqrt{3} \times \sqrt{3}$ and (b) Si(111)-$2 \times 2$ with different numbers of layers.

the DOS projected on the adatoms for each reconstruction. Interestingly, the $2 \times 2$ adatom peak is relatively far from $E_\text{F}$, at 0.7 eV. The other three systems have tall broad adatom peaks right at $E_\text{F}$, confirming that the DOSs at $E_\text{F}$ for these three systems are due to their adatoms. For reasons discussed below, the $2 \times 2$ system is quite different.

Continuing with this analysis, Fig. 5(c) shows the DOSs projected onto the rest atoms for the $2 \times 2$, $5 \times 5$, and $7 \times 7$ reconstructions (the $\sqrt{3} \times \sqrt{3}$ system is omitted because it does not have rest atoms). Both the $5 \times 5$ and the $7 \times 7$ systems have their rest atom peaks at $-0.5$ eV. The $2 \times 2$ system has its rest atom peak right below $E_\text{F}$, near $-0.1$ eV. This analysis shows that it is actually the rest atoms that contribute the DOS near $E_\text{F}$ for the $2 \times 2$ system shown in Fig. 5(a). Finally, the $5 \times 5$ and $7 \times 7$ systems also have dimer atoms and corner holes, whose projected DOSs are shown in Fig. 5(d). Again, there is remarkable agreement between these two systems. Note that the dimer atoms also have a small contribution to DOS at $E_\text{F}$. The corner hole peaks for these two systems agree almost perfectly, as shown by the dashed curves.

To better explore the reason why the $\sqrt{3} \times \sqrt{3}$, $5 \times 5$, and $7 \times 7$ systems are metallic while the $2 \times 2$ system is semiconducting, the population of their DBs can be considered. Each adatom DB and rest atom DB contributes an electron to the electronic structure. Looking at Fig. 2, we can see that the $\sqrt{3} \times \sqrt{3}$ surface has one adatom per supercell, so that its DB is partially occupied, leading to the state lying at $E_\text{F}$. However, in the $2 \times 2$ system, there is one adatom DB and one rest atom DB, each contributing one electron per supercell. Upon electronic relaxation, the electron from the adatom DB drops to the (lower energy) rest atom DB so that the latter becomes doubly occupied while the former becomes empty. A similar sort of charge transfer mechanism has also been suggested to occur within the buckled dimers on the Si(100)-$2 \times 1$ surface, to a smaller extent. $^{23-26}$ This is the reason why the rest atom peak of $2 \times 2$ lies below the $E_\text{F}$, while the adatom peak is above it. To reiterate, it is because of the 1:1 ratio of adatoms to rest atoms in the $2 \times 2$ supercell that this system ends up with a semiconducting electronic structure. Finally, for $5 \times 5$ and $7 \times 7$, there is also electron transfer from the adatom DB to the rest atom DB since the rest atom peaks are below $E_\text{F}$, thus doubly occupied. However, since there are more adatoms per unit cell than rest atoms (3:1 and 2:1 for $5 \times 5$ and $7 \times 7$, respectively), the adatom DBs remain partially occupied, and therefore their states lie at the $E_\text{F}$, thus producing conduction.

![](./images/813311435974115329_5.jpg)

FIG. 5. (Color online) DOS and PDOS (arbitrary units) for the various Si(111) reconstructions. (a) Total DOS; (b) adatom PDOS; (c) rest atom PDOS; (d) dimer and corner hole atom PDOS.

### C. Tuning electronic structure

Even though the $2 \times 2$ system has a band gap, like all semiconductors, its electronic structure can be tuned with a gate or doping so that it becomes metallic. As an extreme

![](./images/813311435974115329_6.jpg)

FIG. 6. (Color online) Adatom PDOS (arbitrary units) for Si(111)-2 $\times$ 2 with different total charges.

example of doping in this system, calculations were carried out on the Si(111)-2 $\times$ 2 slab with an excess or deficit of one electron per unit cell. The adatom PDOSs are shown in Fig. 6 for these cases. In the neutral system, shown by the black curve, the adatom peak is near 0.7 eV. Removing an electron shifts it even higher, to about 1.1 eV (red curve). Conversely, adding an electron shifts the adatom peak to $E_{\text{F}}$. This is because the adatom DB becomes partially occupied by the extra electron, and the system becomes metallic in that scenario. Again, this is an example of extreme doping, but it serves the purpose of illustrating how the electronic structure of the systems can be tuned to obtain the desired properties.

It should be pointed out that such a drastic effect is not expected with metallic surfaces such as Si-7 $\times$ 7. In cases where there are many states at the $E_{\text{F}}$, an excess or deficit of one electron will only have a minimal shift on the DOS spectrum. Therefore, the effect described above is most pronounced with systems that have a band gap (i.e., semiconductors).

### D. Inequivalent Si(111)-7 $\times$ 7 and Si(111)-5 $\times$ 5 adatoms
As mentioned above, the Si(111)-7 $\times$ 7 reconstruction has a faulted and an unfaulted half. The adatoms in each of these are either at the corner ($Co$) or in the center of a side ($Ce$), which results in four types of adatoms, designated $CoU$, $CeU$, $CoF$, and $CeF$. By projecting the DOS onto each of these types, the electronic structures of these atoms may be compared, as shown in Fig. 7(a). The adatoms in the faulted half have a higher DOS at $E_{\text{F}}$ than the adatoms on the unfaulted half. In each half, the center adatoms have a higher DOS at $E_{\text{F}}$ than the corner adatoms. Therefore, the DOS height at $E_{\text{F}}$ follows $CeF > CoF > CeU > CoU$.

Experimentally, STM work by Wang $et$ $al.^{27}$ on n-doped Si found the following trend in adatom brightness for a bias voltage of $-0.57$ V: $CoF > CeF > CoU > CeU$, where the brightness is proportional to the DOS in the energy range spanned by the voltage. The same trend was also found by other groups studying occupied-state images on n-doped Si-7 $\times$ 7. $^{20}$ However, a study by Chaika $et$ $al$. on p-doped Si shows that the ordering of $CeF$ and $CoU$ is reversed, giving $CoF > CoU > CeF > CeU$. $^{28}$ Therefore, it seems that the adatom brightness trend is dependent on the sample doping.

<table>
<caption>TABLE III. Integrated PDOSs from Fig. 7(a).</caption>
<thead>
<tr>
<th>Adatom</th>
<th>p type<br>([$-0.6, -0.1$] eV)</th>
<th>Intrinsic<br>([$-0.5,0.0$] eV)</th>
<th>n type<br>([$-0.4,0.1$] eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$CoF$</td>
<td>8.3</td>
<td>15.6</td>
<td>25.1</td>
</tr>
<tr>
<td>$CeF$</td>
<td>2.6</td>
<td>8.0</td>
<td>20.3</td>
</tr>
<tr>
<td>$CoU$</td>
<td>6.1</td>
<td>11.1</td>
<td>17.3</td>
</tr>
<tr>
<td>$CeU$</td>
<td>1.8</td>
<td>5.6</td>
<td>14.8</td>
</tr>
</tbody>
</table>

![](./images/813311435974115329_7.jpg)

FIG. 7. (Color online) PDOS (arbitrary units) for inequivalent adatoms. (a) Si(111)-7 $\times$ 7; (b) Si(111)-5 $\times$ 5.

In order to compare the calculated results to those from STM experiments, the DOSs need to be integrated in the appropriate energy range. Table III reports such integrated DOSs for various ranges, representing different types of doping scenarios. For p-type doping, the $E_{\text{F}}$ is effectively shifted (relative to the DOS features; see Sec. III C) to a lower value than in an intrinsic sample, so the integration would be up to $-0.1$ eV in this example. The reverse happens with n-type doping, where the $E_{\text{F}}$ and, therefore, the integration maximum are shifted to a higher value. With these values for the integration limits, the calculated results are in agreement with the trends from experiments. The important point is that a reversal of the adatom prominence order is possible by changing the doping of the sample. The calculated DOSs offer a clear explanation for this phenomenon. Table IV lists integrated DOSs for narrower energy windows than those in Table III. For an intrinsic sample, the integrated DOSs for $CeF$ and $CoU$ are 8.0 and 11.1 (arbitrary units), respectively. Now considering an n-type sample, the window [$ -0.5, -0.4$] eV is excluded, while [0.0,0.1] eV is included. It is the latter which makes the big difference since there is such a large difference, 7.0 (arbitrary units), in the integrated DOSs near $E_{\text{F}}$ for $CeF$ and $CoU$ (values in boldface in Table IV). Indeed, the contribution from this small window is sufficient to change the prominence order for the adatoms in an n-doped sample.

Note that the analysis above is for occupied-state images of the surface. For unoccupied-state images, STM experiments show very little difference in brightness between the different adatom types. $^{19,20}$ To compare the calculations in this case, the positive energies need to be considered for the DOS integration. Although there are some differences between the different adatoms, the large peak near 0.3 eV would dominate

<table><caption>TABLE IV. Integrated PDOSs from Fig. 7(a) for narrow energy windows.â</caption>
<thead>
  <tr>
    <th>Adatom</th>
    <th>$\lbrack - 0.6, - 0.5\rbrack$</th>
    <th>$\lbrack - 0.5, - 0.4\rbrack$</th>
    <th>$\lbrack - 0.4, - 0.1\rbrack$</th>
    <th>$\lbrack - 0.1,0.0\rbrack$</th>
    <th>[0.0,0.1]</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$CoF$</td>
    <td>0.9</td>
    <td>0.6</td>
    <td>6.9</td>
    <td>8.8</td>
    <td>11.2</td>
  </tr>
  <tr>
    <td>$CeF$</td>
    <td>1.3</td>
    <td>0.3</td>
    <td>1.0</td>
    <td>6.8</td>
    <td>14.0</td>
  </tr>
  <tr>
    <td>$CoU$</td>
    <td>0.4</td>
    <td>1.0</td>
    <td>6.8</td>
    <td>5.8</td>
    <td>7.0</td>
  </tr>
  <tr>
    <td>$CeU$</td>
    <td>0.9</td>
    <td>0.2</td>
    <td>0.7</td>
    <td>4.7</td>
    <td>10.3</td>
  </tr>
</tbody>
</table>
âEnergy ranges are in electron volts.

the integrated DOS, and this peak is similar for the four types of adatoms. Therefore the calculations also agree with the STM experiments for unoccupied states.

The PDOSs in Fig. 7(a) can also be used to interpret photoemission studies on Si-7 $\times$ 7, such as the work by Uhrberg $et~al.^{29}$ In that study, they found a previously undetected Si surface state between the energies of the $S_{1}$ state due to adatoms and the $S_{2}$ state corresponding to rest atoms and corner hole atoms. The new state, denoted $S_{1}^{\prime}$, was attributed to $CoF$ and $CoU$ adatoms, which is consistent with the PDOSs calculated in this work. In Fig. 5, the rest atoms and corner hole states are near $- 0.55$ and $- 0.4$ eV, respectively, while the adatom peaks are around $E_{\text{F}}$. However, the $CoU$ and $CoF$ adatoms also have a peak near $- 0.15$ eV, as shown in Fig. 7(a), corresponding to $S_{1}^{\prime}$ in the work by Uhrberg $et~al.^{29}$ Therefore, the calculated PDOSs are also in agreement with photoemission studies of Si-7 $\times$ 7.³⁰

In the $5 \times 5$ system, there are only two types of adatoms: $CoF$ and $CoU$ (see Fig. 2). The PDOSs associated with these are plotted in Fig. 7(b). Note that they have the same trend at $E_{\text{F}}$, with the PDOS for $CoF$ being higher than that for $CoU$. However for the peak near $- 0.15$ eV, the trend is opposite to that in the $7 \times 7$ system. Overall, the shapes of the PDOSs for corner adatoms of $5 \times 5$ and $7 \times 7$ show excellent qualitative agreement.

## IV. SUMMARY
To summarize, DFT calculations were carried out on the $\sqrt{3} \times \sqrt{3}$-$R30^\circ$, $2 \times 2$, $5 \times 5$, and $7 \times 7$ reconstructions of Si(111). We found that six layers of Si are sufficient to properly capture the structural and electronic properties of Si surfaces when they are modeled as 2D slabs. For all systems except $2 \times 2$, there are DOSs at $E_{\text{F}}$, and these are primarily due to the adatom states in these systems. In the $2 \times 2$ surface, there is a 1:1 ratio of adatoms to rest atoms, resulting in fully occupied rest atom DBs and empty adatom DBs, which gives this surface semiconducting characteristics. In the $\sqrt{3} \times \sqrt{3}$, $5 \times 5$, and $7 \times 7$ systems, the adatom DB remains partially occupied, setting the $E_{\text{F}}$ right in the adatom PDOSs of these systems, resulting in their metallic character. However, the $2 \times 2$ system could also become metallic provided that appropriate doping or gating is arranged. The DOSs for the four inequivalent adatoms of Si-7 $\times$ 7 were compared to STM experimental data. The difference in experiments on n-doped versus p-doped Si samples can be explained from our calculated DOSs by an appropriate shift of the $E_{\text{F}}$. Finally, we found that the electronic structure of the $5 \times 5$ and $7 \times 7$ systems are very similar in terms of DOS peak positions and their qualitative shapes. This may be useful for expensive simulations where the $7 \times 7$ system can be modeled using the less computationally intensive $5 \times 5$ system, which has half the atoms per supercell.

## ACKNOWLEDGMENTS
We gratefully acknowledge financial support from the Canadian Institute for Advanced Research (CIFAR) and the Natural Sciences and Engineering Research Council of Canada (NSERC). W.J. was supported by the Program for New Century Excellent Talents in University, Ministry of Science and Technology (MOST) Grant No. 2012CB932704, National Natural Science Foundation of China (NSFC) Grant No. 11004244, and Beijing Natural Science Foundation (BNSF) Grant No. 2112019. The calculations were performed at the computation facilities of the Réseau Québécois de Calcul de Haute Performance (RQCHP) and Consortium Laval, Université du Québec, McGill and Eastern Québec (CLUMEQ).

<table><caption>TABLE V. Atomic coordinates for Si(111)-$\sqrt{3} \times \sqrt{3}$ (Å).</caption>
<thead>
  <tr>
    <th>Atom</th>
    <th>$X$</th>
    <th>$Y$</th>
    <th>$Z$</th>
    <th>Atom</th>
    <th>$X$</th>
    <th>$Y$</th>
    <th>$Z$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>H</td>
    <td>3.90</td>
    <td>0.50</td>
    <td>1.02</td>
    <td>Si</td>
    <td>6.14</td>
    <td>5.15</td>
    <td>0.92</td>
  </tr>
  <tr>
    <td>H</td>
    <td>3.90</td>
    <td>0.50</td>
    <td>4.79</td>
    <td>Si</td>
    <td>1.64</td>
    <td>6.06</td>
    <td>0.97</td>
  </tr>
  <tr>
    <td>H</td>
    <td>7.16</td>
    <td>0.50</td>
    <td>2.91</td>
    <td>Si</td>
    <td>4.99</td>
    <td>5.62</td>
    <td>2.91</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>3.87</td>
    <td>2.00</td>
    <td>0.98</td>
    <td>Si</td>
    <td>8.34</td>
    <td>6.06</td>
    <td>4.84</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>3.87</td>
    <td>2.00</td>
    <td>4.84</td>
    <td>Si</td>
    <td>1.64</td>
    <td>8.49</td>
    <td>0.97</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>7.22</td>
    <td>2.00</td>
    <td>2.91</td>
    <td>Si</td>
    <td>4.99</td>
    <td>7.91</td>
    <td>2.91</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>2.75</td>
    <td>2.79</td>
    <td>2.91</td>
    <td>Si</td>
    <td>8.34</td>
    <td>8.49</td>
    <td>4.84</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>6.10</td>
    <td>2.79</td>
    <td>4.84</td>
    <td>Si</td>
    <td>3.97</td>
    <td>9.09</td>
    <td>1.14</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>6.10</td>
    <td>2.79</td>
    <td>0.98</td>
    <td>Si</td>
    <td>3.97</td>
    <td>9.09</td>
    <td>4.68</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>2.69</td>
    <td>5.15</td>
    <td>2.91</td>
    <td>Si</td>
    <td>7.03</td>
    <td>9.09</td>
    <td>2.91</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>6.13</td>
    <td>5.15</td>
    <td>4.90</td>
    <td>Si</td>
    <td>4.99</td>
    <td>10.55</td>
    <td>2.91</td>
  </tr>
</tbody>
</table>

<table><caption>TABLE VI. Atomic coordinates for Si(111)-2 $\times$ 2 (Å).</caption>
<thead>
  <tr>
    <th>Atom</th>
    <th>$X$</th>
    <th>$Y$</th>
    <th>$Z$</th>
    <th>Atom</th>
    <th>$X$</th>
    <th>$Y$</th>
    <th>$Z$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>H</td>
    <td>0.56</td>
    <td>0.49</td>
    <td>0.97</td>
    <td>Si</td>
    <td>6.17</td>
    <td>5.15</td>
    <td>10.70</td>
  </tr>
  <tr>
    <td>H</td>
    <td>0.54</td>
    <td>0.50</td>
    <td>4.84</td>
    <td>Si</td>
    <td>1.68</td>
    <td>6.04</td>
    <td>2.92</td>
  </tr>
  <tr>
    <td>H</td>
    <td>3.91</td>
    <td>0.50</td>
    <td>2.89</td>
    <td>Si</td>
    <td>1.68</td>
    <td>6.04</td>
    <td>6.76</td>
  </tr>
  <tr>
    <td>H</td>
    <td>3.91</td>
    <td>0.50</td>
    <td>6.79</td>
    <td>Si</td>
    <td>5.00</td>
    <td>6.04</td>
    <td>4.84</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>0.56</td>
    <td>2.00</td>
    <td>0.97</td>
    <td>Si</td>
    <td>5.01</td>
    <td>5.57</td>
    <td>8.71</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>0.56</td>
    <td>2.00</td>
    <td>4.83</td>
    <td>Si</td>
    <td>5.03</td>
    <td>7.85</td>
    <td>8.71</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>3.91</td>
    <td>2.00</td>
    <td>2.90</td>
    <td>Si</td>
    <td>1.60</td>
    <td>8.46</td>
    <td>6.91</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>3.91</td>
    <td>2.00</td>
    <td>6.77</td>
    <td>Si</td>
    <td>1.60</td>
    <td>8.46</td>
    <td>2.78</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>2.79</td>
    <td>2.79</td>
    <td>4.83</td>
    <td>Si</td>
    <td>5.18</td>
    <td>8.46</td>
    <td>4.85</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>2.79</td>
    <td>2.79</td>
    <td>8.70</td>
    <td>Si</td>
    <td>0.45</td>
    <td>8.97</td>
    <td>4.85</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>6.14</td>
    <td>2.79</td>
    <td>6.77</td>
    <td>Si</td>
    <td>3.97</td>
    <td>8.97</td>
    <td>6.88</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>6.14</td>
    <td>2.79</td>
    <td>10.63</td>
    <td>Si</td>
    <td>3.97</td>
    <td>8.97</td>
    <td>2.82</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>2.79</td>
    <td>5.19</td>
    <td>4.84</td>
    <td>Si</td>
    <td>0.56</td>
    <td>9.59</td>
    <td>0.98</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>2.71</td>
    <td>5.15</td>
    <td>8.71</td>
    <td>Si</td>
    <td>5.02</td>
    <td>10.28</td>
    <td>8.71</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>6.17</td>
    <td>5.15</td>
    <td>6.71</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

## APPENDIX: ATOMIC COORDINATES

This Appendix contains the Cartesian coordinates for the slabs modeling the four Si(111) reconstructions considered in this work. The atomic coordinates for the Si(111)-$\sqrt{3} \times \sqrt{3}$ system are listed in Table V and the supercell using these coordinates had the lattice vectors $\vec{a} = (6.70,0.00,0.00)$, $\vec{b} = (0.00,25.00,0.00)$, and $\vec{c} = (3.35,0.00,5.80)$ (values in Å). Note that the capping H atoms at the bottom of the slab are listed along with the six layers of Si. Table VI lists the atomic coordinates of the Si(111)-$2 \times 2$ system, which had the lattice vectors $\vec{a} = (6.70,0.00,3.87)$, $\vec{b} = (0.00,25.00,0.00)$, and $\vec{c} = (0.00,0.00,7.73)$. For all four reconstructions, the

TABLE VII. Atomic coordinates for the top four layers of Si(111)-$5 \times 5$ (Å).

<table>
  <thead>
    <tr>
      <th>Atom No.</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>Atom No.</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>9.53</td>
      <td>5.10</td>
      <td>8.66</td>
      <td>51</td>
      <td>8.37</td>
      <td>7.90</td>
      <td>10.65</td>
    </tr>
    <tr>
      <td>2</td>
      <td>9.53</td>
      <td>5.10</td>
      <td>12.61</td>
      <td>52</td>
      <td>1.69</td>
      <td>7.90</td>
      <td>6.78</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2.81</td>
      <td>5.10</td>
      <td>4.79</td>
      <td>53</td>
      <td>1.69</td>
      <td>7.90</td>
      <td>14.50</td>
    </tr>
    <tr>
      <td>4</td>
      <td>16.13</td>
      <td>5.10</td>
      <td>16.43</td>
      <td>54</td>
      <td>11.72</td>
      <td>7.95</td>
      <td>16.47</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2.81</td>
      <td>5.10</td>
      <td>16.49</td>
      <td>55</td>
      <td>11.72</td>
      <td>7.95</td>
      <td>24.15</td>
    </tr>
    <tr>
      <td>6</td>
      <td>16.13</td>
      <td>5.10</td>
      <td>24.18</td>
      <td>56</td>
      <td>5.06</td>
      <td>7.95</td>
      <td>20.31</td>
    </tr>
    <tr>
      <td>7</td>
      <td>12.87</td>
      <td>5.14</td>
      <td>14.46</td>
      <td>57</td>
      <td>15.06</td>
      <td>8.29</td>
      <td>15.15</td>
    </tr>
    <tr>
      <td>8</td>
      <td>12.87</td>
      <td>5.14</td>
      <td>26.15</td>
      <td>58</td>
      <td>11.18</td>
      <td>8.29</td>
      <td>12.91</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12.86</td>
      <td>5.14</td>
      <td>18.42</td>
      <td>59</td>
      <td>15.06</td>
      <td>8.29</td>
      <td>25.47</td>
    </tr>
    <tr>
      <td>10</td>
      <td>9.44</td>
      <td>5.14</td>
      <td>16.45</td>
      <td>60</td>
      <td>11.18</td>
      <td>8.29</td>
      <td>8.38</td>
    </tr>
    <tr>
      <td>11</td>
      <td>12.86</td>
      <td>5.14</td>
      <td>22.18</td>
      <td>61</td>
      <td>2.25</td>
      <td>8.29</td>
      <td>18.07</td>
    </tr>
    <tr>
      <td>12</td>
      <td>2.74</td>
      <td>5.14</td>
      <td>20.31</td>
      <td>62</td>
      <td>2.25</td>
      <td>8.29</td>
      <td>3.22</td>
    </tr>
    <tr>
      <td>13</td>
      <td>6.18</td>
      <td>5.14</td>
      <td>18.33</td>
      <td>63</td>
      <td>15.06</td>
      <td>8.32</td>
      <td>17.61</td>
    </tr>
    <tr>
      <td>14</td>
      <td>9.44</td>
      <td>5.14</td>
      <td>24.16</td>
      <td>64</td>
      <td>9.05</td>
      <td>8.32</td>
      <td>14.14</td>
    </tr>
    <tr>
      <td>15</td>
      <td>6.18</td>
      <td>5.14</td>
      <td>22.28</td>
      <td>65</td>
      <td>15.06</td>
      <td>8.32</td>
      <td>23.00</td>
    </tr>
    <tr>
      <td>16</td>
      <td>6.07</td>
      <td>5.16</td>
      <td>10.64</td>
      <td>66</td>
      <td>4.38</td>
      <td>8.32</td>
      <td>16.84</td>
    </tr>
    <tr>
      <td>17</td>
      <td>2.83</td>
      <td>5.16</td>
      <td>8.77</td>
      <td>67</td>
      <td>9.05</td>
      <td>8.32</td>
      <td>7.14</td>
    </tr>
    <tr>
      <td>18</td>
      <td>2.83</td>
      <td>5.16</td>
      <td>12.51</td>
      <td>68</td>
      <td>4.38</td>
      <td>8.32</td>
      <td>4.45</td>
    </tr>
    <tr>
      <td>19</td>
      <td>12.96</td>
      <td>5.22</td>
      <td>10.64</td>
      <td>69</td>
      <td>5.00</td>
      <td>8.47</td>
      <td>8.76</td>
    </tr>
    <tr>
      <td>20</td>
      <td>9.49</td>
      <td>5.21</td>
      <td>20.31</td>
      <td>70</td>
      <td>5.00</td>
      <td>8.47</td>
      <td>12.53</td>
    </tr>
    <tr>
      <td>21</td>
      <td>16.13</td>
      <td>5.22</td>
      <td>12.47</td>
      <td>71</td>
      <td>1.74</td>
      <td>8.47</td>
      <td>10.64</td>
    </tr>
    <tr>
      <td>22</td>
      <td>6.15</td>
      <td>5.23</td>
      <td>6.76</td>
      <td>72</td>
      <td>11.69</td>
      <td>8.50</td>
      <td>20.31</td>
    </tr>
    <tr>
      <td>23</td>
      <td>16.13</td>
      <td>5.22</td>
      <td>28.14</td>
      <td>73</td>
      <td>8.40</td>
      <td>8.50</td>
      <td>18.41</td>
    </tr>
    <tr>
      <td>24</td>
      <td>6.15</td>
      <td>5.23</td>
      <td>14.52</td>
      <td>74</td>
      <td>8.40</td>
      <td>8.50</td>
      <td>22.21</td>
    </tr>
    <tr>
      <td>25</td>
      <td>16.18</td>
      <td>5.23</td>
      <td>20.30</td>
      <td>75</td>
      <td>7.40</td>
      <td>9.04</td>
      <td>8.79</td>
    </tr>
    <tr>
      <td>26</td>
      <td>8.38</td>
      <td>5.60</td>
      <td>10.64</td>
      <td>76</td>
      <td>3.78</td>
      <td>9.04</td>
      <td>6.70</td>
    </tr>
    <tr>
      <td>27</td>
      <td>1.68</td>
      <td>5.60</td>
      <td>6.77</td>
      <td>77</td>
      <td>7.40</td>
      <td>9.04</td>
      <td>12.50</td>
    </tr>
    <tr>
      <td>28</td>
      <td>1.68</td>
      <td>5.60</td>
      <td>14.51</td>
      <td>78</td>
      <td>0.57</td>
      <td>9.04</td>
      <td>8.55</td>
    </tr>
    <tr>
      <td>29</td>
      <td>11.72</td>
      <td>5.63</td>
      <td>16.44</td>
      <td>79</td>
      <td>3.78</td>
      <td>9.04</td>
      <td>14.59</td>
    </tr>
    <tr>
      <td>30</td>
      <td>11.72</td>
      <td>5.63</td>
      <td>24.17</td>
      <td>80</td>
      <td>0.57</td>
      <td>9.04</td>
      <td>12.73</td>
    </tr>
    <tr>
      <td>31</td>
      <td>5.03</td>
      <td>5.63</td>
      <td>20.31</td>
      <td>81</td>
      <td>10.47</td>
      <td>9.06</td>
      <td>10.64</td>
    </tr>
    <tr>
      <td>32</td>
      <td>15.09</td>
      <td>5.98</td>
      <td>14.50</td>
      <td>82</td>
      <td>0.64</td>
      <td>9.06</td>
      <td>4.97</td>
    </tr>
    <tr>
      <td>33</td>
      <td>11.72</td>
      <td>5.98</td>
      <td>12.55</td>
      <td>83</td>
      <td>0.64</td>
      <td>9.06</td>
      <td>16.32</td>
    </tr>
    <tr>
      <td>34</td>
      <td>15.09</td>
      <td>5.97</td>
      <td>26.11</td>
      <td>84</td>
      <td>12.84</td>
      <td>9.11</td>
      <td>18.23</td>
    </tr>
    <tr>
      <td>35</td>
      <td>11.72</td>
      <td>5.97</td>
      <td>8.73</td>
      <td>85</td>
      <td>9.63</td>
      <td>9.11</td>
      <td>16.37</td>
    </tr>
    <tr>
      <td>36</td>
      <td>1.66</td>
      <td>5.98</td>
      <td>18.36</td>
      <td>86</td>
      <td>12.84</td>
      <td>9.11</td>
      <td>22.39</td>
    </tr>
    <tr>
      <td>37</td>
      <td>1.66</td>
      <td>5.98</td>
      <td>2.92</td>
      <td>87</td>
      <td>12.77</td>
      <td>9.12</td>
      <td>14.65</td>
    </tr>
    <tr>
      <td>38</td>
      <td>15.07</td>
      <td>6.01</td>
      <td>18.32</td>
      <td>88</td>
      <td>6.02</td>
      <td>9.11</td>
      <td>18.46</td>
    </tr>
    <tr>
      <td>39</td>
      <td>15.07</td>
      <td>6.01</td>
      <td>22.29</td>
      <td>89</td>
      <td>9.63</td>
      <td>9.11</td>
      <td>24.25</td>
    </tr>
    <tr>
      <td>40</td>
      <td>8.42</td>
      <td>6.01</td>
      <td>14.48</td>
      <td>90</td>
      <td>6.02</td>
      <td>9.11</td>
      <td>22.16</td>
    </tr>
    <tr>
      <td>41</td>
      <td>4.99</td>
      <td>6.01</td>
      <td>16.47</td>
      <td>91</td>
      <td>12.77</td>
      <td>9.12</td>
      <td>25.97</td>
    </tr>
    <tr>
      <td>42</td>
      <td>8.42</td>
      <td>6.01</td>
      <td>6.79</td>
      <td>92</td>
      <td>2.96</td>
      <td>9.12</td>
      <td>20.31</td>
    </tr>
    <tr>
      <td>43</td>
      <td>4.99</td>
      <td>6.01</td>
      <td>4.81</td>
      <td>93</td>
      <td>9.50</td>
      <td>9.55</td>
      <td>20.31</td>
    </tr>
    <tr>
      <td>44</td>
      <td>5.04</td>
      <td>6.06</td>
      <td>8.68</td>
      <td>94</td>
      <td>3.92</td>
      <td>9.58</td>
      <td>10.64</td>
    </tr>
    <tr>
      <td>45</td>
      <td>11.73</td>
      <td>6.06</td>
      <td>20.31</td>
      <td>95</td>
      <td>8.37</td>
      <td>10.36</td>
      <td>10.64</td>
    </tr>
    <tr>
      <td>46</td>
      <td>5.04</td>
      <td>6.06</td>
      <td>12.60</td>
      <td>96</td>
      <td>1.69</td>
      <td>10.36</td>
      <td>6.79</td>
    </tr>
    <tr>
      <td>47</td>
      <td>8.38</td>
      <td>6.06</td>
      <td>18.37</td>
      <td>97</td>
      <td>1.69</td>
      <td>10.36</td>
      <td>14.50</td>
    </tr>
    <tr>
      <td>48</td>
      <td>1.65</td>
      <td>6.06</td>
      <td>10.64</td>
      <td>98</td>
      <td>11.72</td>
      <td>10.43</td>
      <td>16.46</td>
    </tr>
    <tr>
      <td>49</td>
      <td>8.38</td>
      <td>6.06</td>
      <td>22.24</td>
      <td>99</td>
      <td>11.72</td>
      <td>10.43</td>
      <td>24.16</td>
    </tr>
    <tr>
      <td>50</td>
      <td>15.07</td>
      <td>6.35</td>
      <td>10.64</td>
      <td>100</td>
      <td>5.05</td>
      <td>10.43</td>
      <td>20.31</td>
    </tr>
  </tbody>
</table>


TABLE VIII. Atomic coordinates for the top four layers of Si(111)-7 $\times$ 7 (Å).

<table>
  <thead>
    <tr>
      <th>Atom No.</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>Atom No.</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>Atom No.</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>Atom No.</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>19.56</td>
      <td>5.14</td>
      <td>37.75</td>
      <td>51</td>
      <td>18.41</td>
      <td>5.61</td>
      <td>28.03</td>
      <td>101</td>
      <td>11.73</td>
      <td>7.92</td>
      <td>31.88</td>
      <td>151</td>
      <td>16.31</td>
      <td>9.11</td>
      <td>35.85</td>
    </tr>
    <tr>
      <td>2</td>
      <td>19.56</td>
      <td>5.14</td>
      <td>33.78</td>
      <td>52</td>
      <td>11.73</td>
      <td>5.61</td>
      <td>31.89</td>
      <td>102</td>
      <td>11.73</td>
      <td>7.92</td>
      <td>24.19</td>
      <td>152</td>
      <td>19.50</td>
      <td>9.09</td>
      <td>29.81</td>
    </tr>
    <tr>
      <td>3</td>
      <td>16.13</td>
      <td>5.14</td>
      <td>35.76</td>
      <td>53</td>
      <td>11.73</td>
      <td>5.61</td>
      <td>24.18</td>
      <td>103</td>
      <td>18.40</td>
      <td>7.95</td>
      <td>20.32</td>
      <td>153</td>
      <td>12.71</td>
      <td>9.09</td>
      <td>33.73</td>
    </tr>
    <tr>
      <td>4</td>
      <td>19.55</td>
      <td>5.14</td>
      <td>30.02</td>
      <td>54</td>
      <td>18.42</td>
      <td>5.64</td>
      <td>20.30</td>
      <td>104</td>
      <td>8.36</td>
      <td>7.89</td>
      <td>18.36</td>
      <td>154</td>
      <td>12.78</td>
      <td>9.04</td>
      <td>26.02</td>
    </tr>
    <tr>
      <td>5</td>
      <td>12.87</td>
      <td>5.14</td>
      <td>33.87</td>
      <td>55</td>
      <td>5.03</td>
      <td>5.64</td>
      <td>28.03</td>
      <td>105</td>
      <td>5.04</td>
      <td>7.95</td>
      <td>28.04</td>
      <td>155</td>
      <td>19.50</td>
      <td>9.09</td>
      <td>26.26</td>
    </tr>
    <tr>
      <td>6</td>
      <td>19.55</td>
      <td>5.14</td>
      <td>26.05</td>
      <td>56</td>
      <td>8.37</td>
      <td>5.60</td>
      <td>18.36</td>
      <td>106</td>
      <td>15.06</td>
      <td>7.90</td>
      <td>14.50</td>
      <td>156</td>
      <td>9.63</td>
      <td>9.09</td>
      <td>31.96</td>
    </tr>
    <tr>
      <td>7</td>
      <td>9.43</td>
      <td>5.14</td>
      <td>31.89</td>
      <td>57</td>
      <td>15.07</td>
      <td>5.61</td>
      <td>14.50</td>
      <td>107</td>
      <td>1.67</td>
      <td>7.90</td>
      <td>22.23</td>
      <td>157</td>
      <td>7.30</td>
      <td>8.99</td>
      <td>16.52</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16.11</td>
      <td>5.15</td>
      <td>28.03</td>
      <td>58</td>
      <td>1.67</td>
      <td>5.61</td>
      <td>22.24</td>
      <td>108</td>
      <td>8.36</td>
      <td>7.89</td>
      <td>10.64</td>
      <td>158</td>
      <td>19.54</td>
      <td>9.11</td>
      <td>22.07</td>
    </tr>
    <tr>
      <td>9</td>
      <td>12.87</td>
      <td>5.15</td>
      <td>29.90</td>
      <td>59</td>
      <td>8.37</td>
      <td>5.60</td>
      <td>10.64</td>
      <td>109</td>
      <td>1.68</td>
      <td>7.89</td>
      <td>14.50</td>
      <td>159</td>
      <td>10.46</td>
      <td>9.04</td>
      <td>18.44</td>
    </tr>
    <tr>
      <td>10</td>
      <td>19.56</td>
      <td>5.14</td>
      <td>22.28</td>
      <td>60</td>
      <td>1.69</td>
      <td>5.60</td>
      <td>14.50</td>
      <td>110</td>
      <td>1.67</td>
      <td>7.90</td>
      <td>6.77</td>
      <td>160</td>
      <td>7.38</td>
      <td>9.04</td>
      <td>20.21</td>
    </tr>
    <tr>
      <td>11</td>
      <td>16.19</td>
      <td>5.20</td>
      <td>31.91</td>
      <td>61</td>
      <td>1.67</td>
      <td>5.61</td>
      <td>6.76</td>
      <td>111</td>
      <td>17.88</td>
      <td>8.29</td>
      <td>12.24</td>
      <td>161</td>
      <td>14.10</td>
      <td>9.04</td>
      <td>16.36</td>
    </tr>
    <tr>
      <td>12</td>
      <td>6.17</td>
      <td>5.14</td>
      <td>30.01</td>
      <td>62</td>
      <td>18.42</td>
      <td>5.98</td>
      <td>12.59</td>
      <td>112</td>
      <td>15.75</td>
      <td>8.32</td>
      <td>11.01</td>
      <td>162</td>
      <td>7.30</td>
      <td>8.99</td>
      <td>12.48</td>
    </tr>
    <tr>
      <td>13</td>
      <td>12.87</td>
      <td>5.15</td>
      <td>26.17</td>
      <td>63</td>
      <td>15.12</td>
      <td>6.01</td>
      <td>10.66</td>
      <td>113</td>
      <td>11.11</td>
      <td>8.32</td>
      <td>8.33</td>
      <td>163</td>
      <td>5.99</td>
      <td>9.11</td>
      <td>29.90</td>
    </tr>
    <tr>
      <td>14</td>
      <td>16.23</td>
      <td>5.10</td>
      <td>16.47</td>
      <td>64</td>
      <td>11.69</td>
      <td>6.00</td>
      <td>8.68</td>
      <td>114</td>
      <td>9.00</td>
      <td>8.32</td>
      <td>7.11</td>
      <td>164</td>
      <td>3.77</td>
      <td>9.04</td>
      <td>22.33</td>
    </tr>
    <tr>
      <td>15</td>
      <td>9.51</td>
      <td>5.10</td>
      <td>20.34</td>
      <td>65</td>
      <td>8.40</td>
      <td>6.00</td>
      <td>6.78</td>
      <td>115</td>
      <td>2.23</td>
      <td>8.29</td>
      <td>3.20</td>
      <td>165</td>
      <td>12.71</td>
      <td>9.09</td>
      <td>22.34</td>
    </tr>
    <tr>
      <td>16</td>
      <td>19.56</td>
      <td>5.14</td>
      <td>18.32</td>
      <td>66</td>
      <td>18.42</td>
      <td>6.05</td>
      <td>31.90</td>
      <td>116</td>
      <td>4.35</td>
      <td>8.32</td>
      <td>4.43</td>
      <td>166</td>
      <td>3.80</td>
      <td>8.99</td>
      <td>14.50</td>
    </tr>
    <tr>
      <td>17</td>
      <td>2.80</td>
      <td>5.10</td>
      <td>24.22</td>
      <td>67</td>
      <td>15.07</td>
      <td>6.05</td>
      <td>33.84</td>
      <td>117</td>
      <td>17.88</td>
      <td>8.29</td>
      <td>16.76</td>
      <td>167</td>
      <td>9.63</td>
      <td>9.09</td>
      <td>24.11</td>
    </tr>
    <tr>
      <td>18</td>
      <td>16.13</td>
      <td>5.14</td>
      <td>20.31</td>
      <td>68</td>
      <td>1.66</td>
      <td>5.98</td>
      <td>2.91</td>
      <td>118</td>
      <td>2.23</td>
      <td>8.29</td>
      <td>25.80</td>
      <td>168</td>
      <td>17.15</td>
      <td>9.06</td>
      <td>14.50</td>
    </tr>
    <tr>
      <td>19</td>
      <td>12.87</td>
      <td>5.14</td>
      <td>22.19</td>
      <td>69</td>
      <td>4.97</td>
      <td>6.01</td>
      <td>4.80</td>
      <td>119</td>
      <td>11.11</td>
      <td>8.32</td>
      <td>20.68</td>
      <td>169</td>
      <td>14.10</td>
      <td>9.04</td>
      <td>12.64</td>
    </tr>
    <tr>
      <td>20</td>
      <td>2.74</td>
      <td>5.14</td>
      <td>28.03</td>
      <td>70</td>
      <td>15.08</td>
      <td>6.05</td>
      <td>29.98</td>
      <td>120</td>
      <td>15.75</td>
      <td>8.32</td>
      <td>17.99</td>
      <td>170</td>
      <td>16.31</td>
      <td>9.11</td>
      <td>20.21</td>
    </tr>
    <tr>
      <td>21</td>
      <td>9.43</td>
      <td>5.14</td>
      <td>24.18</td>
      <td>71</td>
      <td>18.42</td>
      <td>5.98</td>
      <td>16.41</td>
      <td>121</td>
      <td>9.00</td>
      <td>8.32</td>
      <td>21.89</td>
      <td>171</td>
      <td>0.63</td>
      <td>9.06</td>
      <td>24.05</td>
    </tr>
    <tr>
      <td>22</td>
      <td>6.17</td>
      <td>5.14</td>
      <td>26.06</td>
      <td>72</td>
      <td>1.66</td>
      <td>5.97</td>
      <td>26.09</td>
      <td>122</td>
      <td>4.35</td>
      <td>8.32</td>
      <td>24.57</td>
      <td>172</td>
      <td>19.45</td>
      <td>9.12</td>
      <td>18.50</td>
    </tr>
    <tr>
      <td>23</td>
      <td>16.23</td>
      <td>5.10</td>
      <td>12.53</td>
      <td>73</td>
      <td>18.42</td>
      <td>6.06</td>
      <td>24.16</td>
      <td>123</td>
      <td>21.75</td>
      <td>8.29</td>
      <td>37.07</td>
      <td>173</td>
      <td>5.99</td>
      <td>9.11</td>
      <td>26.17</td>
    </tr>
    <tr>
      <td>24</td>
      <td>22.83</td>
      <td>5.10</td>
      <td>35.78</td>
      <td>74</td>
      <td>15.08</td>
      <td>6.05</td>
      <td>26.08</td>
      <td>124</td>
      <td>18.39</td>
      <td>8.49</td>
      <td>31.92</td>
      <td>174</td>
      <td>0.54</td>
      <td>9.04</td>
      <td>20.47</td>
    </tr>
    <tr>
      <td>25</td>
      <td>16.19</td>
      <td>5.20</td>
      <td>24.16</td>
      <td>75</td>
      <td>11.70</td>
      <td>6.05</td>
      <td>28.03</td>
      <td>125</td>
      <td>15.09</td>
      <td>8.49</td>
      <td>33.83</td>
      <td>175</td>
      <td>2.94</td>
      <td>9.12</td>
      <td>28.03</td>
    </tr>
    <tr>
      <td>26</td>
      <td>9.48</td>
      <td>5.20</td>
      <td>28.03</td>
      <td>76</td>
      <td>8.37</td>
      <td>6.06</td>
      <td>29.97</td>
      <td>126</td>
      <td>21.75</td>
      <td>8.32</td>
      <td>34.61</td>
      <td>176</td>
      <td>10.46</td>
      <td>9.04</td>
      <td>10.57</td>
    </tr>
    <tr>
      <td>27</td>
      <td>9.53</td>
      <td>5.15</td>
      <td>16.37</td>
      <td>77</td>
      <td>11.69</td>
      <td>6.00</td>
      <td>20.32</td>
      <td>127</td>
      <td>15.14</td>
      <td>8.49</td>
      <td>30.10</td>
      <td>177</td>
      <td>0.57</td>
      <td>9.04</td>
      <td>16.28</td>
    </tr>
    <tr>
      <td>28</td>
      <td>12.77</td>
      <td>5.16</td>
      <td>14.50</td>
      <td>78</td>
      <td>8.40</td>
      <td>6.00</td>
      <td>22.22</td>
      <td>128</td>
      <td>21.74</td>
      <td>8.32</td>
      <td>29.25</td>
      <td>178</td>
      <td>7.38</td>
      <td>9.04</td>
      <td>8.79</td>
    </tr>
    <tr>
      <td>29</td>
      <td>6.06</td>
      <td>5.16</td>
      <td>18.37</td>
      <td>79</td>
      <td>15.12</td>
      <td>6.01</td>
      <td>18.34</td>
      <td>129</td>
      <td>18.39</td>
      <td>8.49</td>
      <td>24.15</td>
      <td>179</td>
      <td>0.57</td>
      <td>9.04</td>
      <td>12.72</td>
    </tr>
    <tr>
      <td>30</td>
      <td>9.51</td>
      <td>5.10</td>
      <td>8.66</td>
      <td>80</td>
      <td>21.78</td>
      <td>5.97</td>
      <td>37.71</td>
      <td>130</td>
      <td>21.74</td>
      <td>8.32</td>
      <td>26.82</td>
      <td>180</td>
      <td>3.77</td>
      <td>9.04</td>
      <td>6.67</td>
    </tr>
    <tr>
      <td>31</td>
      <td>2.82</td>
      <td>5.16</td>
      <td>20.24</td>
      <td>81</td>
      <td>4.97</td>
      <td>6.01</td>
      <td>24.20</td>
      <td>131</td>
      <td>8.36</td>
      <td>8.49</td>
      <td>29.94</td>
      <td>181</td>
      <td>0.54</td>
      <td>9.04</td>
      <td>8.53</td>
    </tr>
    <tr>
      <td>32</td>
      <td>22.84</td>
      <td>5.10</td>
      <td>28.03</td>
      <td>82</td>
      <td>15.07</td>
      <td>6.06</td>
      <td>22.23</td>
      <td>132</td>
      <td>15.14</td>
      <td>8.49</td>
      <td>25.97</td>
      <td>182</td>
      <td>0.62</td>
      <td>9.06</td>
      <td>4.96</td>
    </tr>
    <tr>
      <td>33</td>
      <td>9.53</td>
      <td>5.15</td>
      <td>12.63</td>
      <td>83</td>
      <td>8.37</td>
      <td>6.06</td>
      <td>26.10</td>
      <td>133</td>
      <td>11.56</td>
      <td>8.50</td>
      <td>28.03</td>
      <td>183</td>
      <td>16.22</td>
      <td>9.55</td>
      <td>31.97</td>
    </tr>
    <tr>
      <td>34</td>
      <td>19.65</td>
      <td>5.22</td>
      <td>14.50</td>
      <td>84</td>
      <td>21.76</td>
      <td>6.01</td>
      <td>33.89</td>
      <td>134</td>
      <td>15.09</td>
      <td>8.49</td>
      <td>22.24</td>
      <td>184</td>
      <td>16.22</td>
      <td>9.56</td>
      <td>24.10</td>
    </tr>
    <tr>
      <td>35</td>
      <td>2.82</td>
      <td>5.16</td>
      <td>16.50</td>
      <td>85</td>
      <td>11.74</td>
      <td>6.06</td>
      <td>16.46</td>
      <td>135</td>
      <td>8.36</td>
      <td>8.49</td>
      <td>26.13</td>
      <td>185</td>
      <td>9.41</td>
      <td>9.56</td>
      <td>28.03</td>
    </tr>
    <tr>
      <td>36</td>
      <td>12.85</td>
      <td>5.23</td>
      <td>18.37</td>
      <td>86</td>
      <td>5.03</td>
      <td>6.06</td>
      <td>20.33</td>
      <td>136</td>
      <td>21.75</td>
      <td>8.29</td>
      <td>19.00</td>
      <td>186</td>
      <td>10.67</td>
      <td>9.58</td>
      <td>14.50</td>
    </tr>
    <tr>
      <td>37</td>
      <td>22.82</td>
      <td>5.22</td>
      <td>39.74</td>
      <td>87</td>
      <td>21.76</td>
      <td>6.00</td>
      <td>29.93</td>
      <td>137</td>
      <td>21.75</td>
      <td>8.32</td>
      <td>21.46</td>
      <td>187</td>
      <td>3.87</td>
      <td>9.58</td>
      <td>18.43</td>
    </tr>
    <tr>
      <td>38</td>
      <td>6.14</td>
      <td>5.23</td>
      <td>22.25</td>
      <td>88</td>
      <td>8.36</td>
      <td>6.05</td>
      <td>14.50</td>
      <td>138</td>
      <td>11.72</td>
      <td>8.48</td>
      <td>16.39</td>
      <td>188</td>
      <td>3.87</td>
      <td>9.58</td>
      <td>10.57</td>
    </tr>
    <tr>
      <td>39</td>
      <td>6.06</td>
      <td>5.16</td>
      <td>10.63</td>
      <td>89</td>
      <td>5.03</td>
      <td>6.05</td>
      <td>16.42</td>
      <td>139</td>
      <td>4.98</td>
      <td>8.48</td>
      <td>20.28</td>
      <td>189</td>
      <td>18.41</td>
      <td>10.44</td>
      <td>35.76</td>
    </tr>
    <tr>
      <td>40</td>
      <td>2.82</td>
      <td>5.16</td>
      <td>12.50</td>
      <td>90</td>
      <td>11.74</td>
      <td>6.06</td>
      <td>12.54</td>
      <td>140</td>
      <td>8.54</td>
      <td>8.47</td>
      <td>14.50</td>
      <td>190</td>
      <td>18.38</td>
      <td>10.39</td>
      <td>28.03</td>
    </tr>
    <tr>
      <td>41</td>
      <td>2.80</td>
      <td>5.10</td>
      <td>4.78</td>
      <td>91</td>
      <td>21.76</td>
      <td>6.00</td>
      <td>26.14</td>
      <td>141</td>
      <td>4.93</td>
      <td>8.47</td>
      <td>16.58</td>
      <td>191</td>
      <td>11.74</td>
      <td>10.39</td>
      <td>31.87</td>
    </tr>
    <tr>
      <td>42</td>
      <td>22.83</td>
      <td>5.10</td>
      <td>20.28</td>
      <td>92</td>
      <td>1.64</td>
      <td>6.06</td>
      <td>18.37</td>
      <td>142</td>
      <td>11.71</td>
      <td>8.47</td>
      <td>12.61</td>
      <td>192</td>
      <td>11.74</td>
      <td>10.39</td>
      <td>24.20</td>
    </tr>
    <tr>
      <td>43</td>
      <td>6.14</td>
      <td>5.20</td>
      <td>14.50</td>
      <td>93</td>
      <td>5.03</td>
      <td>6.05</td>
      <td>12.57</td>
      <td>143</td>
      <td>1.71</td>
      <td>8.48</td>
      <td>18.39</td>
      <td>193</td>
      <td>8.36</td>
      <td>10.34</td>
      <td>18.35</td>
    </tr>
    <tr>
      <td>44</td>
      <td>2.82</td>
      <td>5.16</td>
      <td>8.76</td>
      <td>94</td>
      <td>21.78</td>
      <td>5.97</td>
      <td>18.36</td>
      <td>144</td>
      <td>4.93</td>
      <td>8.47</td>
      <td>12.42</td>
      <td>194</td>
      <td>15.06</td>
      <td>10.37</td>
      <td>14.50</td>
    </tr>
    <tr>
      <td>45</td>
      <td>12.85</td>
      <td>5.23</td>
      <td>10.63</td>
      <td>95</td>
      <td>21.76</td>
      <td>6.01</td>
      <td>22.17</td>
      <td>145</td>
      <td>4.98</td>
      <td>8.48</td>
      <td>8.72</td>
      <td>195</td>
      <td>18.41</td>
      <td>10.44</td>
      <td>20.31</td>
    </tr>
    <tr>
      <td>46</td>
      <td>22.87</td>
      <td>5.23</td>
      <td>31.91</td>
      <td>96</td>
      <td>5.03</td>
      <td>6.06</td>
      <td>8.67</td>
      <td>146</td>
      <td>1.71</td>
      <td>8.48</td>
      <td>10.61</td>
      <td>196</td>
      <td>1.67</td>
      <td>10.37</td>
      <td>22.23</td>
    </tr>
    <tr>
      <td>47</td>
      <td>6.14</td>
      <td>5.23</td>
      <td>6.75</td>
      <td>97</td>
      <td>1.64</td>
      <td>6.06</td>
      <td>10.63</td>
      <td>147</td>
      <td>19.45</td>
      <td>9.12</td>
      <td>37.57</td>
      <td>197</td>
      <td>5.03</td>
      <td>10.44</td>
      <td>28.03</td>
    </tr>
    <tr>
      <td>48</td>
      <td>22.87</td>
      <td>5.23</td>
      <td>24.15</td>
      <td>98</td>
      <td>21.77</td>
      <td>6.35</td>
      <td>14.50</td>
      <td>148</td>
      <td>16.28</td>
      <td>9.04</td>
      <td>28.03</td>
      <td>198</td>
      <td>8.36</td>
      <td>10.34</td>
      <td>10.66</td>
    </tr>
    <tr>
      <td>49</td>
      <td>22.82</td>
      <td>5.22</td>
      <td>16.33</td>
      <td>99</td>
      <td>18.40</td>
      <td>7.95</td>
      <td>35.75</td>
      <td>149</td>
      <td>12.78</td>
      <td>9.04</td>
      <td>30.05</td>
      <td>199</td>
      <td>1.70</td>
      <td>10.34</td>
      <td>14.50</td>
    </tr>
    <tr>
      <td>50</td>
      <td>18.42</td>
      <td>5.63</td>
      <td>35.77</td>
      <td>100</td>
      <td>18.39</td>
      <td>7.92</td>
      <td>28.03</td>
      <td>150</td>
      <td>19.54</td>
      <td>9.11</td>
      <td>33.99</td>
      <td>200</td>
      <td>1.67</td>
      <td>10.37</td>
      <td>6.77</td>
    </tr>
  </tbody>
</table>

two lowest Si layers were frozen to their bulk positions, while the remaining Si and H atoms were allowed to fully relax.

The coordinates of the relaxed Si atoms (top four layers) of the Si(111)-5 $\times$ 5 system are listed in Table VII and those of the Si(111)-7 $\times$ 7 system are listed in Table VIII. For these two big systems, the bottom two Si layers can be obtained by extending the coordinates of the Si(111)-2 $\times$ 2 system since they are frozen to bulk values. Similarly, the $\vec{a}$ and $\vec{c}$ lattice vectors of the 5 $\times$ 5 and 7 $\times$ 7 systems can also be obtained by appropriately scaling those of the 2 $\times$ 2 system ($\vec{b}$ is the same for all slabs).

*Present address: Department of Chemistry, Northwestern University, Evanston, IL 60208, USA; manuel.smeu@northwestern.edu.
†Department of Physics, University of Alberta, Edmonton, Alberta, Canada.

¹A. Pecchia and A. D. Carlo, *Rep. Prog. Phys.* **67**, 1497 (2004).

²M. D'angelo, K. Takase, N. Miyata, T. Hirahara, S. Hasegawa, A. Nishide, M. Ogawa, and I. Matsuda, *Phys. Rev. B* **79**, 035318 (2009).

³G. Y. Jing, H. L. Duan, X. M. Sun, Z. S. Zhang, J. Xu, Y. D. Li, J. X. Wang, and D. P. Yu, *Phys. Rev. B* **73**, 235409 (2006).

⁴V. Timoshevskii, Y. Ke, H. Guo, and D. Gall, *J. Appl. Phys.* **103**, 113705 (2008).

⁵M. Smeu, R. A. Wolkow, and H. Guo, *J. Am. Chem. Soc.* **131**, 11019 (2009).

⁶K. Yoo and H. H. Weitering, *Phys. Rev. B* **65**, 115424 (2002).

⁷K. Takayanagi, Y. Tanishiro, M. Takahashi, and S. Takahashi, *J. Vac. Sci. Technol. A* **3**, 1502 (1985).

⁸K. D. Brommer, M. Needels, B. E. Larson, and J. D. Joannopoulos, *Phys. Rev. Lett.* **68**, 1355 (1992).

⁹J. E. Northrup, *Phys. Rev. Lett.* **57**, 154 (1986).

¹⁰S. Ihara, T. Uda, and M. Hirao, *Appl. Surf. Sci.* **60–61**, 22 (1992).

¹¹G. Kresse and J. Hafner, *Phys. Rev. B* **47**, 558 (1993).

¹²G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

¹³J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

¹⁴P. E. Blöchl, *Phys. Rev. B* **50**, 17953 (1994).

¹⁵G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

¹⁶S. H. Ke, T. Uda, and K. Terakura, *Phys. Rev. B* **62**, 15319 (2000).

¹⁷S. Y. Tong, H. Huang, C. M. Wei, W. E. Packard, F. K. Men, G. Glander, and M. B. Webb, *J. Vac. Sci. Technol. A* **6**, 615 (1988).

¹⁸R. J. Hamers, R. M. Tromp, and J. E. Demuth, *Phys. Rev. Lett.* **56**, 1972 (1986).

¹⁹R. Wolkow and P. Avouris, *Phys. Rev. Lett.* **60**, 1049 (1988).

²⁰P. Avouris and R. Wolkow, *Phys. Rev. B* **39**, 5091 (1989).

²¹T. Uchihashi, Y. Sugawara, T. Tsukamoto, M. Ohta, S. Morita, and M. Suzuki, *Phys. Rev. B* **56**, 9834 (1997).

²²N. Nakagiri, M. Suzuki, K. Okiguchi, and H. Sugimura, *Surf. Sci.* **373**, L329 (1997).

²³D. H. Rich, T. Miller, and T.-C. Chiang, *Phys. Rev. B* **37**, 3124 (1988).

²⁴E. Landemark, C. J. Karlsson, Y.-C. Chao, and R. I. G. Uhrberg, *Phys. Rev. Lett.* **69**, 1588 (1992).

²⁵E. Artacho and F. Ynduráin, *Phys. Rev. Lett.* **62**, 2491 (1989).

²⁶J. P. LaFemina, *Surf. Sci. Rep.* **16**, 137 (1992).

²⁷Y. L. Wang, H.-J. Gao, H. M. Guo, H. W. Liu, I. G. Batyrev, W. E. McMahon, and S. B. Zhang, *Phys. Rev. B* **70**, 073312 (2004).

²⁸A. Chaika and A. Myagkov, *Chem. Phys. Lett.* **453**, 217 (2008).

²⁹R. I. G. Uhrberg, T. Kaurila, and Y.-C. Chao, *Phys. Rev. B* **58**, R1730 (1998).

³⁰Note that the energies reported by Uhrberg *et al.*²⁹ are lower than those calculated here by about 0.35 eV. This is attributed to their use of an n-type Si sample, while the model used in this work represents intrinsic Si.