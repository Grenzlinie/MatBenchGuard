# Migration of a Carbon Adatom on a Charged Single-Walled Carbon Nanotube

Longtao Han¹, Predrag Krstic¹⁎, Igor Kaganovich², Roberto Car³

¹Institute for Advanced Computational Science and Department of Material Science and Engineering, State University of New York at Stony Brook, Stony Brook, NY 11794-5250

²Princeton Plasma Physics Laboratory, Princeton, NJ 08543

³Department of Chemistry, Princeton University, Princeton, NJ 08544

ABSTRACT: We find that negative charges on an armchair single-walled carbon nanotube (SWCNT) can significantly enhance the migration of a carbon adatom on the external surfaces of SWCNTs, along the direction of the tube axis. Nanotube charging results in stronger binding of adatoms to SWCNTs and consequent longer lifetimes of adatoms before desorption, which in turn increases their migration distance several orders of magnitude. These results support the hypothesis of diffusion enhanced SWCNT growth in the volume of arc plasma. This process could enhance effective carbon flux to the metal catalyst.

## 1. Introduction

⁎Corresponding author. Tel: +1(865) 603-2970, Email: predrag.krstic@stonybrook.edu

Within the plasma volume, the growth of SWCNTs from transition metal catalysts can be enhanced by the flux of carbon atoms from the plasma to the external surfaces of SWCNTs. This enhanced growth results from the combined processes of adatom adsorption on the surfaces of SWCNTs and the subsequent migration of those carbon adatoms towards the metal catalyst particles [1,2]. In plasmas, nanotubes become charged through the process of being bombarded by plasma particles, specifically electrons. Here we report the effect of surface charging on the adsorption and migration of carbon adatoms, determined by performing highly accurate, all-electron Density Functional Theory (DFT) calculations, followed by Kinetic Monte Carlo (KMC) simulations. We found that while this charging only slightly affects the barriers to adatom diffusion along nanotubes, it significantly increases their adsorption energies. This seemingly counterintuitive observation is the result of increased electron density in the region between the carbon adatoms and the carbon atoms of the SWCNT. The consequence of this added density is an improvement in the covalent coupling between adatoms and SWCNTs. In concert with relatively lower diffusion energy barriers, this enhanced coupling increases the lifetime of adatoms on the surfaces of SWCNTs, allowing for longer migration distances before desorption.

Carbon nanotubes (CNT) [3, 4] have attracted significant attention from academia and industry, due to their superior thermal, mechanical, and electrical properties [5]. For example, SWCNTs have been shown to be promising materials for use in electronic [6],energy conversion [7, 8], and energy storage [9, 10] applications, because changes in tube chirality yield changes in their bandgap, and therefore allows for control over their electrical properties. The great demand for such materials calls for the development of methods for the large-scale production of minimally-defected, structurally-controlled SWCNTs.

Unfortunately the high level of control over SWCNT synthesis required for such applications has not yet been fully realized, and cannot be realized without acquiring a better understanding of the underlying growth mechanism for SWCNTs. Various models for growth mechanisms have been developed, such as the vapor-liquid-solid (VLS) [11, 12], scooter-growth [13], root-growth [14] and vapor-solid-solid models [15]. Most of the aforementioned models for the CNT nucleation and growth have been developed having in mind the chemical vapor deposition (CVD) method. In the VLS model, a carbon precursor from the gas phase adsorbs onto the surface of a transition metal catalyst particle and then dissociates. The resulting carbon atoms then diffuse into the liquid catalyst nanoparticle, possibly forming metal carbides. This process eventually results in saturation of the nanoparticles with carbon, excess of which then crystallizes at the catalyst surface. These excess carbon atoms assemble into a graphene cap whose edges are strongly chemisorbed to the metal catalyst. A crucial feature of this mechanism is its avoidance, at all stages of growth, of any open graphene edges, the existence of which would mean exposing energetically expensive dangling bonds. The energy minimized, curved surface of the cap has $\text{sp}^2$ covalently bonded carbons, forming hexagons and pentagons, with minimal dangling bonds at the edges. Once the cap is formed, insertion of new carbons occurs between the tube edge and the catalytic particle resulting in the growth of a SWCNT. Once overcoating of the catalyst by carbon is reached, the process is suppressed and deactivated [11, 12]. A proposed surface-mediated growth model can also explain the lower activation energy associated with plasma-enhanced CVD growth [16]. In this model, carbon transport toward the root of SWCNTs occurs not by bulk diffusion through a liquid particle, but rather by surface diffusion over a potentially solid catalyst particle.

High-pressure, arc-discharge plasma, utilizing carbon electrodes can be used for producing high quality, defect-free SWCNT [17]. However, despite the successful development of this method,

detailed understanding of all physical and chemical processes taking place during the SWCNT synthesis in the arc is challenging. In contrast to the CVD method which has carbon precursor molecules as its only reactive species, many reactive species exist in the plasma volume, including neutral and excited atoms, ions, electrons, radicals, and molecules. Furthermore, unlike the CVD method, the temperature of an arc-discharge plasma varies from 10,000 K in the arc column to below 1000K at the discharge periphery, offering a very broad range of gas temperatures as well as a significantly higher flux of feedstock particles. Therefore, the mechanisms of nucleation and growth of the SWCNT in the arc plasma could be significantly different from those proposed for CVD synthesis. For instance, in contrast to CVD where carbon precursors must first adsorb to catalyst particles and then dissociate into reactive carbon, for arc-discharge plasma synthesis, reactive carbon atoms could be adsorbed on the SWCNT surface directly from plasma. The high temperature plasma may enable an accelerated surface migration of adsorbed atoms toward the junction between catalyst and root of the growing SWCNT, enhancing the total carbon flux available for SWCNT growth. In addition, in the arc-discharge method, the nanotube surface is subject to the flux of plasma ions and electrons, which are capable of charging the SWCNT. These distinctions from CVD may be of importance in arc-discharge plasma synthesis, achieving accelerated, controlled growth of SWCNT, and thus are the main motivations for the present study.

The adsorption behavior of atoms and molecules on SWCNT has been studied extensively, mainly for the purpose of hydrogen storage [18], gas sensing [19], catalysis [20] etc., but few of these studies have focused on the adsorption of carbon atoms on SWCNT. Durgun et al. [21] utilized a pseudopotential plane-wave DFT (PWDFT) method to calculate the stable adsorption geometries and adsorption energies ($E_a$) for a number of adatoms on SWCNT, ranging from alkali to transition metals and group IV elements. They found adsorption energies, $E_a$= 3.7 and 4.2 eV at

the two stable positions of a C adatom on (8,0) SWCNT [20]. Lehtinen et al. [22] examined adsorption of carbon adatoms on graphene using spin-polarized PWDFT, finding the equilibrium position to be a bridge-like structure with $E_a$=1.40 eV. Krasheninnikov et al.[23, 24] calculated $E_a$ making use of the tight-binding DFT approximation (DFTB) and PWDFT to study adsorption and migration of carbon adatoms on SWCNT's of various chiralities. Their calculations for the adsorption energies of carbon atoms at their most stable sites on SWCNTs ranges from 2.7-4 eV for tubes with diameters from 0.6-1.4 nm. The migration barriers of carbon adatoms are found to be in the range of 0.6–1 eV for SWCNT with typical diameters of 1-1.4 nm, and are governed by the orientation of the C-C bond with respect to tube axis [23, 24].

Studies of the effects of charging on the properties of SWCNTs have been conducted both experimentally and theoretically, to determine the charge density profiles and relevant electronic structures. Keblinski et al.[25] conducted DFT calculations of charge distributions on negatively and positively charged nanotubes of finite length. They found that the charge distributed in U-like profile along the nanotube for both positive and negative charges, with charge density located primarily at the tube ends.Follow-up studies showed that the charge enhancement at the tube ends decreases as the tube length increases [26], which was later experimentally confirmed by showing that over a micron long nanotube the charge was almost uniformly distributed [27]. In addition, recent research performed by Wang et al. showed that CNTs can be negatively charged during thermal CVD growth, and that charging can be utilized to control their resulting chirality [28].

### 2. Computational details

We studied the charging effects for metallic (5,5) SWCNT in the armchair configuration, which exhibits surface migration paths with the lowest energy barriers along the CNT axis. The

calculations were carried for a (5,5) SWCNT of finite length (2 nm), containing 180 carbon atoms. In order to pacify dangling bonds at the CNT ends, we terminated each end with "crown" of 10 hydrogen atoms. Hydrogen-termination ensures chemical passivation of the dangling carbon bonds at the edges, which provides faster convergence of the DFT calculations [29]. This is a common approach in the studies of CNT bulk properties [30]. Varying the negative charge on the CNTs from 0 to -12e in steps of -2e, (where e is the elementary charge), we identified the stable sites, and then calculated adsorption energies, diffusion energy barriers, and vibrational frequencies. In addition to the metallic (5,5) SWCNT, we studied the migration parameters of two semiconducting SWCNTs (adsoprtion energies, and diffusion barriers) (10,5) and zig-zag (10,0), of finite lengths in the absence of charging.. These computations were performed using all-electron molecular DFT [31, 32] with 6-31G* valence double-zeta polarized Gaussian basis set and PBE0 hybrid functional [33], implemented by NWChem computational chemistry package [34]. The results are shown in the Supporting Information (SI), Fig. S1 and S2. We find that only (5,5) SWCNT has a continuous migration path with low diffusion barriers for adatom migration, in the direction of the tube axis. This is the reason to study in detail the effects of charging on adatom migration on the external surface of the metalic, armchair (5,5) SWCNT.

### 2.1 Adsorption sites and energies

Three equilibrium adsorption sites for carbon adatom were identified for a (5,5) SWCNT, close to the middle of the CNT length. In agreement with previous studies [20, 22], they are located above the bridges connecting neighboring carbon atoms, as shown in Fig. 1(a). Note that sites 1 and 3 in Fig. 1(a) are equivalent. The location of the equilibrium adsorption sites in the middle of the bridging sites is not unique to (5,5) SWCNTs; two examples showing adatom adsorption sites

at corresponding bridge sites of SWCNT of other chiralities are shown in Fig. S1. The geometry of SWCNT was optimized for each charge, with and without an adatom present. The adsorption energy is calculated from

$$
E_{a}{ }^{q}=E(C N T+C)^{q}-E(C N T)^{q}-E(C) \tag{1}
$$

where superscript "q" is the charge of the system, and E(CNT+C), E(CNT) and E(C) are the geometry optimized configuration energies of CNTs with an adatom present, a pristine CNT, and spin-polarized (triplet) single carbon atom, respectively. We assume that the CNT is charged before adsorbing the adatom, as expressed by $(CNT)^q$ in Eq. 1. Previous studies [20,21] indicated that adsorption energies are dependent on the local curvature of SWCNT, showing that adsorption energy is lowest when carbon-carbon bond orientation is along the tube axis, and is highest when the orientation is perpendicular to the tube axis, (in agreement with our findings, Table 1).

![](./images/867761314062139711_1.jpg)

Fig. 1. (a) Equilibrium adsorption sites marked by yellow stars, (b) possible migration paths and (c) energy profiles of migration barriers between the equilibrium sites for an adatom on a (5,5) SWCNT. The green arrows in (b) represent the paths with the lowest energy barriers, which are between sites 1 and 3. The red arrows represent paths through sites 2 with barriers higher than 1.5 eV, and these paths are less probable routes for migration than those indicated by the green arrows. Relative energies of adatoms adsorbed at

three sites are illustrated by dashed horizontal lines in (c), and the energies of an adatom along the migration paths between sites 1-2, 1-3 and 2-3 are represented by hollow rhombs on a black line, a red line, and hollow circles on a blue line, respectively.

Using Eq. 1 we also calculated adsorption energies as a function of the number of negative charges present on a (5,5) SWCNT, as shown in Fig. 2 and Table S1. For all three adsorption sites, we found adsorption energies increased with increasing charge. This increase in energy is particularly large when |q|> 4e, for reasons that will be discussed in detail in the following section.

Table 1

Adsorption energies at the three types of adsorption sites for SWCNTs of each of the three chirality types. Data in Refs. [22,23] are calculated by the PWDFT, with PAW potential and GGA hybrid functional. Our calculations are performed on the finite-length SWCNTs, using molecular DFT in NWChem package, with polarized Gaussian basis 6-31G* and PBE0 hybrid functional.

<table>
  <thead>
    <tr>
      <th>Chirality type</th>
      <th colspan="3">Adsorption energy at three adatom sites (eV)</th>
    </tr>
    <tr>
      <th></th>
      <th>Site 1</th>
      <th>Site 2</th>
      <th>Site 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(5,5)</td>
      <td>2.01</td>
      <td>2.87</td>
      <td>2.01</td>
    </tr>
    <tr>
      <td>(5,5) by PWDFT ref. 22,23</td>
      <td>2.35</td>
      <td>3.30</td>
      <td>2.35</td>
    </tr>
    <tr>
      <td>(10,5)</td>
      <td>1.64</td>
      <td>1.99</td>
      <td>1.35</td>
    </tr>
    <tr>
      <td>(10,0)</td>
      <td>1.63</td>
      <td>2.29</td>
      <td>2.29</td>
    </tr>
    <tr>
      <td>(10,0) by PWDFT ref. 22,23</td>
      <td>2.10</td>
      <td>2.60</td>
      <td>2.60</td>
    </tr>
  </tbody>
</table>

### 2.2 Migration barriers

Identification of the minimum energy path (MEP) for migration from one stable equilibrium configuration to another was done by the nudged elastic band method, and implemented by DFT in NWChem. Each energy barrier height (Eᵦ) is listed as the difference between the transition state energy and the equilibrium energy (Fig. 2 and Table S2). Surface migration paths for an adatom between the equilibrium sites for the armchair (5,5) SWCNT are shown in Fig. 1(b). Migration

paths with high-energy barriers between the stable sites are shown in red. Possible fast migration paths, corresponding to the low-energy barriers are shown in light green, which occur in the direction of the CNT axis. The corresponding MEPs are shown in Fig. 1(c). Even though the most stable adsorption states are those with the highest binding energy, which are regularly connected with large barriers, it is worth noting that bombardment of the CNT by plasma particles may bring adatoms to vibrationally excited states and thus may accelerate the migration. As mentioned above, there is no continuous low-barrier path for the SWCNTs of the other two considered chirality types. The path with lowest barriers for (10, 0) and (10, 5) SWCNT still contains a barrier of 1.1 eV and 0.7 eV, respectively, as shown in Fig. S2.

![](./images/867761314062139711_2.jpg)

Fig. 2. Migration barrier heights (Eᵦ) and adsorption energies (Eₐ) of a (5,5) SWCNT as a function of charge on the SWCNT.

Unlike adsorption energies, which monotonically increase by almost 90 % in the considered range of charges, the migration barriers, shown in Fig. 2 and Table S2, non-monotonically vary up to 30%. In the next section we will show simulation results for the migration of an adatom over a charged (5,5) SWCNT using the KMC method.

### 2.3 Kinetic Monte Carlo

Simulations of carbon adatom migration were conducted using the KMC method [35]. KMC simulations account for desorption from, and hopping between, the three types of adatom sites. The corresponding transition rates were calculated using the obtained energy barriers, adsorption energies, and vibrational frequencies obtained using Arrhenius-type formulas:

$$
k_{s \rightarrow f}=v_{s} \exp \left(-\frac{E_{s \rightarrow f}}{k_{B} T}\right) \tag{2}
$$

$$
k_{d}^{s}=v_{s} \exp \left(-\frac{E_{a}^{s}}{k_{B} T}\right) \tag{3}
$$

where $v_{s}$ is the vibrational frequency of the corresponding state in the direction of reaction, $E_{s \rightarrow f}$ is the energy barrier for the transition from a state "s" to a state "f," $E_{a}^{s}$ is the adsorption energy of a state "s," and temperature $T$ was chosen to be 1700 K.

The vibrational frequencies, $v_{s}$ , drivers for both hopping and desorption, were calculated by numerical Hessian in NWChem, and the results are presented in the SI. Table S3 shows the normal mode frequencies for an adatom located at the different sites on a SWCNT with varying charges. These frequencies correspond to three modes illustrated in Figure S3. All normal mode frequencies are close to $10^{13}$ Hz, in agreement with previous studies [23]. The vibrational frequency of an adatom is a projection of the normal mode frequencies to the direction of the reaction coordinate.

Transition rates for the KMC simulation, hopping rates as determined by Eq. 2 and desorption rates as determined by Eq. 3, are tabulated in Table S4. All trajectories were started in an adsorbed state. Lifetime is defined as the total time an adatom stayed on the surface of a CNT before desorbing into the vacuum. Migration distance is defined as the distance that an adatom migrated along the tube axis direction, during its lifetime. Each migration trajectory contains up to $10^{10}$ steps. We calculated the average values from 400,000 trajectories at each charge to get the convergence. In this calculation the length of CNT was assumed infinite, with the properties as calculated in the middle of our finite tube. The charge density with the total added charge q at the tube is used as q/L (e/nm), where L=1.98 nm.

## 3 Results and discussion

Both migration distance and lifetime of the migration process are shown in Fig. 3 for a CNT with varying numbers of charges q. While we identified three possible initial sites for an adatom, in this paper we show only the case where site 2 is initially populated. Because the other cases, where sites 1 and 3 are initially populated, almost fully overlap with the case where site 2 is initially populated. This is valid, because $E_{b}$ (1,3->2) < $E_{a}$ as shown in Fig.2 and adatom transfers to the site 2 well before it can move far along CNT before desorption. The migration distance increases as q increases – from 25 nm at q=0, to about 100 nm at q=-4e, and then further increases to approximately 13 microns at q=-12e. On the other hand, the lifetime slowly increases – from 10 $\mu$s at q=0, to 27 $\mu$s at q=-4e, and finally a significant increase to about 160 ms at q=-12e. The abrupt increase of migration distance at q=-2e results from the lower migration energy barriers between sites 1 and 3 at q=-2e than at q=0 or -4e. While a slight increase in the migration energy barrier partially offsets the effect of the increased adsorption energy, the migration distance and

lifetime increase significantly only for $|q| > 4e$, where there is a corresponding noticeable increase in the adsorption energy as well.

![](./images/867761314062139711_3.jpg)

Fig. 3. Migration distance, (the black line with squares), and lifetime, (the blue dashed line with triangles), of a carbon adatom as a function of the charge on a (5,5) SWCNT of 2 nm long. Charge density in the middle of the tube for each case is shown on the upper axis.

As others have previously reported, for finite tubes which are not terminated by hydrogen atoms, the charge density on a charged SWCNT is primarily located at the tube ends, (a U-like profile) [25, 26]. In our case, we found that termination of SWCNTs with hydrogen atoms results in polar carbon-hydrogen bonds. These observed dipoles show a positive charge to be on the hydrogen atoms and a negative charge to be on the carbon atoms (see Fig. 4). Away from the SWCNT ends, the charge density is nearly homogeneous. These distributions of charges were determined using

Mullikan population analysis. While the absolute value of charges determined based on Mullikan analysis is not reliable, the trends in charge differences between sites for varying total SWCNT charge should be reliable. As is evident in Fig. 4 and Table S5, when an adatom is added to a SWCNT with varying charges, it changes from having a positive charge of approximately 0.26e (for q=0) to having a negative charge of approximately -0.3e (for q=-12e). For a centrally located carbon atom in a SWCNT, the negative charge localized on it does not exceed 0.05e. The corresponding repulsive electrostatic energy between an adatom and a CNT is expected to increase with increased CNT charging.

![](./images/867761314062139711_4.jpg)

Fig. 4. The distribution of Mulliken charges along the axis of a (5,5) SWCNT for an adatom adsorbed at (a) site 1, (b) site 2. Filled symbols represent the charges localized on the carbon atoms of a SWCNT. Each data point represents the charge per atom averaged over 10 atoms that share the same normalized position along nanotube. Hollow symbols represent the charges localized on an adatom.

As shown in Fig. 2 and Table S1, the adsorption energies increase significantly when the negative charges on a CNT exceed 4e. This increase is associated with an increase in covalent bonding between an adatom and the two carbon atoms closest to it on the surface of a SWCNT. This is illustrated in Fig. 5, showing the differences of electron densities in the vicinity of adatom of the charged CNT (q=-4e, -8e, and -12e) + adatom, and charge-neutral cases. Although the

Mulliken negative charge of the adatom increases with q, this increase is not localized on the adatom, but rather occupies the space between the adatom and two carbon atoms closest to it on CNT. This increased density strengthens the covalent bonding and thus contributes to the increased adsorption energy. This result is consistent with the decrease of the HOMO-LUMO gap of the

![](./images/867761314062139711_5.jpg)

Fig. 5. Isosurface of the difference in electron density with additional charge: -4e (green), -8e (purple), -12e (dim blue), compared to the q=0 case. The isovalue of 0.02 is used in all three cases.

CNT + adatom with increasing q, as shown in Table 2. While Fig. 5 illustrates the electron density changes for the stable site 2, the adsorption energy for sites 1 and 3 increases even more for |q| > 4e. This occurs because the equilibrium adsorption configuration changes. As shown in Fig. 6, three carbon atoms of the SWCNT bond to the adatom instead of only two as discussed previously. Interestingly, the migration barriers do not change significantly with increasing q, (Fig. 2 and Table S2). The barrier along the fast migration path, (the green path in Fig. 1(b)), is less than 0.5 eV,

even for q=-12e. Because the desorption rates are exponentially dependent on $E_a^s$ (Eq. 3), and adsorption energies increase in absolute value with q, increasing q greatly increases the lifetime of adatoms, yielding increases in the migration distances, (as obtained by KMC and shown in Fig. 3).

**Table 2**
HOMO-LUMO gap of a (5,5) SWCNT (with an adatom present) for different charges

<table>
  <thead>
    <tr>
      <th>Molecule</th>
      <th colspan="7">HOMO-LUMO Gap (eV)</th>
    </tr>
    <tr>
      <th>type</th>
      <th>q=0</th>
      <th>q=-2e</th>
      <th>q=-4e</th>
      <th>q=-6e</th>
      <th>q=-8e</th>
      <th>q=-10e</th>
      <th>q=-12e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CNT</td>
      <td>1.4170</td>
      <td>0.8367</td>
      <td>1.2217</td>
      <td>0.8620</td>
      <td>0.7700</td>
      <td>0.5628</td>
      <td>1.0759</td>
    </tr>
    <tr>
      <td>CNT+C(1)</td>
      <td>1.3780</td>
      <td>0.9406</td>
      <td>0.9049</td>
      <td>0.9527</td>
      <td>0.8001</td>
      <td>0.7253</td>
      <td>0.9130</td>
    </tr>
    <tr>
      <td>CNT+C(2)</td>
      <td>1.4869</td>
      <td>0.7152</td>
      <td>1.0255</td>
      <td>0.8767</td>
      <td>0.7455</td>
      <td>0.5675</td>
      <td>0.8176</td>
    </tr>
    <tr>
      <td>CNT+C(3)</td>
      <td>1.3769</td>
      <td>0.9392</td>
      <td>0.9057</td>
      <td>0.9522</td>
      <td>0.8002</td>
      <td>0.7259</td>
      <td>0.9130</td>
    </tr>
  </tbody>
</table>

![](./images/867761314062139711_6.jpg)

Fig. 6. Equilibrium adsorption configuration of an adatom at site 1 for (a) |q| ≤ 4e; (b) |q| >6e.

Based on the above results, we can estimate the contribution from surface migration to the carbon flux toward the root of a SWCNT. If homogeneous flux density of carbon particles onto a SWCNT is $F$, and $r$ is the radius of the catalyst particle, the total number of particles impinging on the hemisphere of the catalyst particle in a unit time is $2\pi r^2 F$. Assuming the radius of SWCNT is correlated to the radius of catalyst, the number of particles in unit time impinging on the SWCNT surface of length $L$ is $2\pi rLF$. The ratio of these fluxes is $L/r$. Since $L$ can be on the order of 10 microns, while $r$ is typically on order of nanometers, this ratio can reach several orders of

magnitude. A significant proportion of these adsorbed carbon atoms on the SWCNT surface could diffuse toward the catalyst-CNT root. Possible reduction of this fluence at the junction of a SWCNT and catalyst particle [36, 37, 38] is beyond the scope of the present study. Healing of defects during the CNT growth can also be aided by enhanced carbon adatom surface migration. As such, it is possible that enhanced migration is responsible for the production of the characteristically low-defect SWCNT synthesized in the arc plasma volume [39].

## 4 Conclusions

In summary, we explored the adsorption and migration behavior of a carbon adatom on negatively charged, armchair SWCNT of finite length, finding significant increase in the migration distance when $|q| > 4$e. The transition rates were determined using first-principles DFT calculations. The increased adsorption energies for negatively charged SWCNTs result from increased covalent bonding between the adsorbed carbon adatom and the carbon atoms of CNTs. This stronger bonding leads to significantly increased lifetime for the adatom, allowing for longer migration distance before desorption back into the plasma. These findings indicate an enhanced carbon adatoms flux on the external surface of SWCNTs toward the metal catalyst, which could lead to a profound increase in the growth rate of SWCNTs in the arc plasma volume.

## Acknowledgments

This work was supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, Material Sciences and Engineering Division Grant No. DE-AC02-09CH11466. Presented results were in part calculated using XSEDE computing facilities, (Stampede and

Comet), LIRed computing facilities of IACS of SBU, and DOE NCCS computing facilities at ORNL. We are grateful to Prof. Robert J. Harrison for inspiring discussions.

## Appendix A. Supplementary data
Supplementary data related to this article can be found at *URL*.

## References
[1] D.-H. Kim, H.-S. Jang, C.-D. Kim, D.-S. Cho, H.-S. Yang, H.-D. Kang, et al., Dynamic growth rate behavior of a carbon nanotube forest characterized by in situ optical growth monitoring, Nano Lett. 3(6) (2003) 863-865.
[2] R.E. Morjan, V. Maltsev, O. Nerushev, Y. Yao, L.K. Falk, E.E. Campbell, High growth rates and wall decoration of carbon nanotubes grown by plasma-enhanced chemical vapour deposition, Chem. Phys. Lett. 383(3) (2004) 385-390.
[3] S. Iijima, T. Ichihashi, Single-shell carbon nanotubes of 1-nm diameter, Nature 363(6430) (1993) 603-605.
[4] D. Bethune, C. Klang, M. De Vries, G. Gorman, R. Savoy, J. Vazquez, R. Beyers, Cobalt- catalysed growth of carbon nanotubes with single-atomic-layer walls, Nature 363(6430) (1993) 605-607.
[5] R.H. Baughman, A.A. Zakhidov, W.A. de Heer, Carbon nanotubes--the route toward applications, Science 297(5582) (2002) 787-792.
[6] M.L. Moser, G. Li, M. Chen, E. Bekyarova, M.E. Itkis, R.C. Haddon, Fast Electrochromic Device Based on Single-Walled Carbon Nanotube Thin Films, Nano Lett. 16(9) (2016) 5386-5393.
[7] I. Jeon, T. Chiba, C. Delacou, Y. Guo, A. Kaskela, O. Reynaud, et al., Single-Walled Carbon Nanotube Film as Electrode in Indium-Free Planar Heterojunction Perovskite Solar Cells: Investigation of Electron-Blocking Layers and Dopants, Nano Lett. 15(10) (2015) 6665-6671.
[8] A. Kongkanand, R. Martínez Domínguez, P.V. Kamat, Single wall carbon nanotube scaffolds for photoelectrochemical solar cells. Capture and transport of photogenerated electrons, Nano Lett. 7(3) (2007) 676-680.
[9] Y. Zhu, Y. Wen, X. Fan, T. Gao, F. Han, C. Luo, et al., Red phosphorus-single-walled carbon nanotube composite as a superior anode for sodium ion batteries, ACS Nano 9(3) (2015) 3254-3264.
[10] H.X. Zhang, C. Feng, Y.C. Zhai, K.L. Jiang, Q.Q. Li, S.S. Fan, Cross-Stacked Carbon Nanotube Sheets Uniformly Loaded with $SnO_{2}$ Nanoparticles: A Novel Binder-Free and High-Capacity Anode Material for Lithium-Ion Batteries, Adv. Mater. 21(22) (2009) 2299-2304.
[11] R. Baker, M. Barber, P. Harris, F. Feates, R. Waite, Nucleation and growth of carbon deposits from the nickel catalyzed decomposition of acetylene, J. Catal. 26(1) (1972) 51-62.

[12]F. Ding, P. Larsson, J.A. Larsson, R. Ahuja, H. Duan, A. Rosén, et al., The importance of strong carbon-metal adhesion for catalytic nucleation of single-walled carbon nanotubes, Nano Lett. 8(2) (2008) 463-468.

[13]A. Thess, R. Lee, P. Nikolaev, H. Dai, Crystalline ropes of metallic carbon nanotubes, Science 273(5274) (1996) 483.

[14]J. Gavillet, A. Loiseau, C. Journet, F. Willaime, F. Ducastelle, J.-C. Charlier, Root-growth mechanism for single-wall carbon nanotubes, Phys. Rev. Lett. 87(27) (2001) 275504.

[15]A.J. Page, K. Chandrakumar, S. Irle, K. Morokuma, SWNT nucleation from carbon-coated SiO2 nanoparticles via a vapor- solid- solid mechanism, J. Am. Chem. Soc. 133(3) (2010) 621-628.

[16]S. Hofmann, G. Csanyi, A. Ferrari, M. Payne, J. Robertson, Surface diffusion: the low activation energy path for nanotube growth, Phys. Rev. Lett. 95(3) (2005) 036101.

[17]C. Journet, W. Maser, P. Bernier, A. Loiseau, M.L. De La Chapelle, d.l.S. Lefrant, et al., Large-scale production of single-walled carbon nanotubes by the electric-arc technique, Nature 388(6644) (1997) 756-758.

[18]N. Faginas-Lago, D. Yeni, F. Huarte, Y. Wang, M. Alcamí, F. Martin, Adsorption of Hydrogen Molecules on Carbon Nanotubes Using Quantum Chemistry and Molecular Dynamics, J. Phys. Chem. A 120(32) (2016) 6451-6458.

[19]P. Bondavalli, P. Legagneux, D. Pribat, Carbon nanotubes based transistors as gas sensors: state of the art and critical review, Sens. Actuators B Chem. 140(1) (2009) 304-318.

[20]J. Moreno, S. Aspera, M. David, H. Kasai, A computational study on the effect of local curvature on the adsorption of oxygen on single-walled carbon nanotubes, Carbon 94 (2015) 936-941.

[21]E. Durgun, S. Dag, S. Ciraci, O. Gülseren, Energetics and electronic structures of individual atoms adsorbed on carbon nanotubes, J. Phys. Chem. B 108(2) (2004) 575-582.

[22]P. Lehtinen, A.S. Foster, A. Ayuela, A. Krasheninnikov, K. Nordlund, R.M. Nieminen, Magnetic properties and diffusion of adatoms on a graphene sheet, Phys. Rev. Lett. 91(1) (2003) 017202.

[23]A. Krasheninnikov, K. Nordlund, P. Lehtinen, A.S. Foster, A. Ayuela, R.M. Nieminen, Adsorption and migration of carbon adatoms on carbon nanotubes: Density-functional ab initio and tight-binding studies, Phys. Rev. B 69(7) (2004) 073402.

[24]A. Krasheninnikov, K. Nordlund, P. Lehtinen, A. Foster, A. Ayuela, R. Nieminen, Adsorption and migration of carbon adatoms on zigzag carbon nanotubes, Carbon 42(5) (2004) 1021-1025.

[25]P. Keblinski, S. Nayak, P. Zapol, P. Ajayan, Charge distribution and stability of charged carbon nanotubes, Phys. Rev. Lett. 89(25) (2002) 255503.

[26]C. Li, T.-W. Chou, Electrostatic charge distribution on single-walled carbon nanotubes, Appl. Phys. Lett. 89(6) (2006) 063103.

[27]Z. Wang, M. Zdrojek, T. Mélin, M. Devel, Electric charge enhancements in carbon nanotubes: theory and experiments, Phys. Rev. B 78(8) (2008) 085425.

[28]J. Wang, P. Liu, B. Xia, H. Wei, Y. Wei, Y. Wu, et al., Observation of Charge Generation and Transfer during CVD Growth of Carbon Nanotubes, Nano Lett. 16(7) (2016) 4102-4109.

[29]D. Henwood, J.D. Carey, Ab initio investigation of molecular hydrogen physisorption on graphene and carbon nanotubes, Phys. Rev. B 75(24) (2007) 245413.

[30] C. Kim, K. Seo, B. Kim, N. Park, Y.S. Choi, K.A. Park, Y.H. Lee, Tip-functionalized carbon nanotubes under electric fields, Phys. Rev. B 68(11) (2003) 115403.

[31] P. Hohenberg, W. Kohn, Inhomogeneous electron gas, Phys. Rev. 136(3B) (1964) B864.

[32] W. Kohn, L.J. Sham, Self-consistent equations including exchange and correlation effects, Phys. Rev. 140(4A) (1965) A1133.

[33] C. Adamo, V. Barone, Toward reliable density functional methods without adjustable parameters: The PBE0 model, J. Chem. Phys. 110(13) (1999) 6158-6170.

[34] M. Valiev, E.J. Bylaska, N. Govind, K. Kowalski, T.P. Straatsma, H.J. Van Dam, et al., NWChem: a comprehensive and scalable open-source solution for large scale molecular simulations, Comput. Phys. Commun. 181(9) (2010) 1477-1489.

[35] A.B. Bortz, M.H. Kalos, J.L. Lebowitz, A new algorithm for Monte Carlo simulation of Ising spin systems, J. Comput. Phys. 17(1) (1975) 10-18.

[36] O.A. Louchev, Y. Sato, H. Kanda, Morphological stabilization, destabilization, and open-end closure during carbon nanotube growth mediated by surface diffusion, Physical Review E 66(1) (2002) 011601.

[37] O.A. Louchev, T. Laude, Y. Sato, H. Kanda, Diffusion-controlled kinetics of carbon nanotube forest growth by chemical vapor deposition, J. Chem. Phys. 118(16) (2003) 7622-7634.

[38] O.A. Louchev, H. Kanda, A. Rosén, K. Bolton, Thermal physics in carbon nanotube growth kinetics, J. Chem. Phys. 121(1) (2004) 446-456.

[39] M. Meyyappan, Plasma nanotechnology: past, present and future, J. Phys. D: Appl. Phys. 44(17) (2011) 174002.

# Supporting Information

## Migration of Carbon Adatom on a Charged Single Walled Carbon Nanotube

Longtao Han¹, Predrag Krstic¹⁎, Igor Kaganovich², Roberto Car³

¹Institute for Advanced Computational Science and Department of Material Science and Engineering, State University of New York at Stony Brook, Stony Brook, NY 11794-5250

²Princeton Plasma Physics Laboratory, Princeton, NJ 08543

³Department of Chemistry, Princeton University, Princeton, NJ 08544

---
⁎Corresponding author. Tel: +1(865) 603-2970, Email: predrag.krstic@stonybrook.edu

S1: Migration parameters in absence of charging of two semiconducting SWCNT of (10,5) and zig-zag (10,0) chiralities with finite lengths

![](./images/867761314062139711_7.jpg)

Figure S1 Equilibrium adsorption sites for SWCNT of two chirality types: (a) (10,0); (b) (10,5)

![](./images/867761314062139711_8.jpg)

Figure S2 Possible migration path and energy profile along path of (a) (10,0) and (b) (10,5) SWCNT

S2: Migration parameters of charged SWCNT of (5,5) chirality with finite lengths

Table S1 Adsorption energy of adatom on (5,5) SWCNT at different charges

<table>
  <thead>
    <tr>
      <th>Adsorption<br>site</th>
      <th colspan="7">Adsorption energy (eV)</th>
    </tr>
    <tr>
      <th></th>
      <th>q=0</th>
      <th>q=-2e</th>
      <th>q=-4e</th>
      <th>q=-6e</th>
      <th>q=-8e</th>
      <th>q=-10e</th>
      <th>q=-12e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2.0106</td>
      <td>2.1876</td>
      <td>2.1603</td>
      <td>2.9171</td>
      <td>3.3800</td>
      <td>3.7796</td>
      <td>3.7860</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.8715</td>
      <td>2.8969</td>
      <td>3.0040</td>
      <td>3.4177</td>
      <td>3.6873</td>
      <td>3.9357</td>
      <td>4.0773</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0104</td>
      <td>2.1880</td>
      <td>2.1607</td>
      <td>2.9172</td>
      <td>3.3801</td>
      <td>3.7797</td>
      <td>3.7860</td>
    </tr>
  </tbody>
</table>

Table S2 Migration energy barriers of adatom on (5,5) SWCNT at different charges

<table>
  <thead>
    <tr>
      <th>Direction</th>
      <th colspan="7">Migration energy barrier (eV)</th>
    </tr>
    <tr>
      <th></th>
      <th>q=-0</th>
      <th>q=-2e</th>
      <th>q=-4e</th>
      <th>q=-6e</th>
      <th>q=-8e</th>
      <th>q=-10e</th>
      <th>q=-12e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1,3->2</th>
      <td>1.5476</td>
      <td>1.5314</td>
      <td>1.3400</td>
      <td>1.9277</td>
      <td>1.9462</td>
      <td>1.9418</td>
      <td>1.9703</td>
    </tr>
    <tr>
      <th>2->1,3</th>
      <td>2.3928</td>
      <td>2.2408</td>
      <td>2.1837</td>
      <td>2.4283</td>
      <td>2.2535</td>
      <td>2.0980</td>
      <td>2.2616</td>
    </tr>
    <tr>
      <th>1->3</th>
      <td rowspan="2">0.3935</td>
      <td rowspan="2">0.1025</td>
      <td rowspan="2">0.1328</td>
      <td rowspan="2">0.4429</td>
      <td rowspan="2">0.4793</td>
      <td rowspan="2">0.5647</td>
      <td rowspan="2">0.4896</td>
    </tr>
    <tr>
      <th>3->1</th>
    </tr>
  </tbody>
</table>

S3: Vibrational frequencies of adatom on (5,5) SWCNT

Table S3 Normal mode frequencies of adatom at different charges

<table>
  <thead>
    <tr>
      <th rowspan="2">Charge</th>
      <th colspan="3">Normal mode frequency ($10^{13}$ Hz)</th>
    </tr>
    <tr>
      <th>Site 1</th>
      <th>Site 2</th>
      <th>Site 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">q=0</td>
      <td>0.912</td>
      <td>0.457</td>
      <td>0.913</td>
    </tr>
    <tr>
      <td>1.415</td>
      <td>2.218</td>
      <td>1.415</td>
    </tr>
    <tr>
      <td>2.387</td>
      <td>2.514</td>
      <td>2.386</td>
    </tr>
    <tr>
      <td rowspan="3">q=-2e</td>
      <td>0.959</td>
      <td>1.092</td>
      <td>0.957</td>
    </tr>
    <tr>
      <td>1.376</td>
      <td>2.252</td>
      <td>1.377</td>
    </tr>
    <tr>
      <td>2.368</td>
      <td>2.556</td>
      <td>2.369</td>
    </tr>
    <tr>
      <td rowspan="3">q=-4e</td>
      <td>0.869</td>
      <td>1.669</td>
      <td>0.866</td>
    </tr>
    <tr>
      <td>1.395</td>
      <td>2.260</td>
      <td>1.393</td>
    </tr>
    <tr>
      <td>2.370</td>
      <td>2.402</td>
      <td>2.370</td>
    </tr>
    <tr>
      <td rowspan="3">q=-6e</td>
      <td>0.847</td>
      <td>0.894</td>
      <td>0.839</td>
    </tr>
    <tr>
      <td>1.357</td>
      <td>2.214</td>
      <td>1.356</td>
    </tr>
    <tr>
      <td>2.348</td>
      <td>2.466</td>
      <td>2.347</td>
    </tr>
    <tr>
      <td rowspan="3">q=-8e</td>
      <td>0.878</td>
      <td>1.367</td>
      <td>0.872</td>
    </tr>
    <tr>
      <td>1.387</td>
      <td>2.293</td>
      <td>1.385</td>
    </tr>
    <tr>
      <td>2.392</td>
      <td>2.497</td>
      <td>2.391</td>
    </tr>
    <tr>
      <td rowspan="3">q=-10e</td>
      <td>0.828</td>
      <td>1.074</td>
      <td>0.827</td>
    </tr>
    <tr>
      <td>1.366</td>
      <td>2.205</td>
      <td>1.366</td>
    </tr>
    <tr>
      <td>2.327</td>
      <td>2.598</td>
      <td>2.327</td>
    </tr>
    <tr>
      <td rowspan="3">q=-12e</td>
      <td>0.835</td>
      <td>1.173</td>
      <td>0.833</td>
    </tr>
    <tr>
      <td>1.324</td>
      <td>2.242</td>
      <td>1.321</td>
    </tr>
    <tr>
      <td>2.383</td>
      <td>2.503</td>
      <td>2.380</td>
    </tr>
  </tbody>
</table>

![](./images/867761314062139711_9.jpg)

Figure S3 Illustration of three vibrational normal modes of adatom at (5,5) SWCNT

S4: Transition rates for KMC simulation

Table S4 Transition rates of adatoms on (5,5) SWCNT at different charges

<table>
  <thead>
    <tr>
      <th>Transition type</th>
      <th colspan="7">Transition rates (ns⁻¹)</th>
    </tr>
    <tr>
      <th></th>
      <th>q=0</th>
      <th>q=-2e</th>
      <th>q=-4e</th>
      <th>q=-6e</th>
      <th>q=-8e</th>
      <th>q=-10e</th>
      <th>q=-12e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1,3-&gt;2</td>
      <td>2.582E-01</td>
      <td>2.881E-01</td>
      <td>1.065E+00</td>
      <td>1.928E-02</td>
      <td>1.698E-02</td>
      <td>1.750E-02</td>
      <td>1.441E-02</td>
    </tr>
    <tr>
      <td>2-&gt;1,3</td>
      <td>8.053E-04</td>
      <td>2.274E-03</td>
      <td>3.358E-03</td>
      <td>6.323E-04</td>
      <td>2.085E-03</td>
      <td>6.028E-03</td>
      <td>1.973E-03</td>
    </tr>
    <tr>
      <td>1-&gt;3,3-&gt;1</td>
      <td>6.805E+02</td>
      <td>4.967E+03</td>
      <td>4.038E+03</td>
      <td>4.864E+02</td>
      <td>3.793E+02</td>
      <td>2.118E+02</td>
      <td>3.536E+02</td>
    </tr>
    <tr>
      <td>1-&gt;d</td>
      <td>1.094E-02</td>
      <td>3.270E-03</td>
      <td>3.938E-03</td>
      <td>2.247E-05</td>
      <td>9.532E-07</td>
      <td>6.234E-08</td>
      <td>5.965E-08</td>
    </tr>
    <tr>
      <td>2-&gt;d</td>
      <td>3.067E-05</td>
      <td>2.581E-05</td>
      <td>1.242E-05</td>
      <td>7.371E-07</td>
      <td>1.170E-07</td>
      <td>2.147E-08</td>
      <td>8.168E-09</td>
    </tr>
    <tr>
      <td>3-&gt;d</td>
      <td>1.096E-02</td>
      <td>3.261E-03</td>
      <td>3.929E-03</td>
      <td>2.245E-05</td>
      <td>9.528E-07</td>
      <td>6.226E-08</td>
      <td>5.965E-08</td>
    </tr>
  </tbody>
</table>

S5: Mulliken charge on adatom with different charges on (5,5) SWCNT

<table>
  <thead>
    <tr>
      <th rowspan="2">Adsorption<br>site</th>
      <th colspan="7">Mulliken charge on adatom (e)</th>
    </tr>
    <tr>
      <th>q=0</th>
      <th>q=-2e</th>
      <th>q=-4e</th>
      <th>q=-6e</th>
      <th>q=-8e</th>
      <th>q=-10e</th>
      <th>q=-12e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0.2567</td>
      <td>0.1200</td>
      <td>0.0789</td>
      <td>-0.1942</td>
      <td>-0.2391</td>
      <td>-0.2831</td>
      <td>-0.3165</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.2602</td>
      <td>0.2296</td>
      <td>0.0456</td>
      <td>-0.0572</td>
      <td>-0.1214</td>
      <td>-0.2113</td>
      <td>-0.2340</td>
    </tr>
  </tbody>
</table>