# Polarization and Valley Switching in Monolayer Group-IV Monochalcogenides

Paul Z. Hanakata, $^{1}$ Alexandra Carvalho, $^{2}$ David K. Campbell, $^{1, *}$ and Harold S. Park $^{3, \dagger}$

$^{1}$ Department of Physics, Boston University, Boston, MA 02215
$^{2}$ Centre for Advanced 2D Materials and Graphene Research Centre,
National University of Singapore, 6 Science Drive 2, 117546, Singapore
$^{3}$ Department of Mechanical Engineering, Boston University, Boston, MA 02215
(Dated: August 9, 2021)

Group-IV monochalcogenides are a family of two-dimensional puckered materials with an orthorhombic structure that is comprised of polar layers. In this article, we use first principles calculations to show the multistability of monolayer SnS and GeSe, two prototype materials where the direction of the puckering can be switched by application of tensile stress or electric field. Furthermore, the two inequivalent valleys in momentum space, which dictated by the puckering orientation, can be excited selectively using linearly polarized light, and this provides additional tool to identify the polarization direction. Our findings suggest that SnS and GeSe monolayers may have observable ferroelectricity and multistability, with potential applications in information storage.

PACS numbers: 85.50 Gk, 64.70 Nd, 71.20 Mg

The discovery of 2D materials that can be isolated into single layers through exfoliation and exhibit novel properties has established new paradigms for ultrathin devices based on atomically sharp interfaces [1, 2]. In particular, transition metal dichalcogenides (TMDs) have been studied extensively and have shown potential for many technological applications ranging from photovoltaics to valleytronic devices [3–9]. The family of monolayer 2D materials has recently grown to include other 2D semiconductors, such as phosphorene and related materials.

However, one of the features thus far lacking for applications both in 2D electronics and in valleytronics is non-volatile memory. Ferromagnetism, an essential element in spintronic memories, is believed to be achievable in graphene and other 2D materials but so far remains difficult to realize and control [10]. Ferroelectric memories, in which the information is stored in the orientation of the electric dipole rather than in the magnetization are a possible option. Single-layer graphene (SLG) ferroelectric field-effect transistors (FFET) with symmetrical bit writing have been demonstrated [11], but the prototypes rely on bulk or thin film ferroelectric substrates [11] or ferroelectric polymers [12], rather than on crystalline atomically thin ferroelectric materials. An altogether different approach to information storage relies on phase change materials, where the bit value corresponds to a distinct structural phase of the material. Researchers have recently optimized the phase switching energy by using superlattice structures where the movement of the atoms is confined to only one dimension [13].

In this article, we analyze the stability of group-IV monochalcogenide MX (M=Ge or Sn, and X=S or Se) monolayers, paying particular interest to their potential as memory functional materials. As prototypes, we use SnS and GeSe. In ambient conditions, bulk SnS and GeSe crystallize in the orthorhombic structure of the $Pnma$ space group. At 878 K, SnS goes through a second-order displacive phase transition into the $\beta$-SnS phase with $Cmcm$ symmetry [14, 15], which is also a layered phase that can be viewed as a distorted rocksalt structure. For bulk GeSe, such a phase transition has not been observed. Instead, at 924 K bulk GeSe transforms into the rocksalt phase ($Fm\overline{3}m$). This phase can also be stabilized using external pressure [16].

Similar to phosphorene [17, 18], $Pnma$ SnS and GeSe can be exfoliated [19, 20]. In monolayer form, they feature multiple valleys, large spin-orbit splitting[21] and a piezoelectric coefficient that surpasses that of the TMDs [22, 23]. Having an in-plane polar axis makes SnS and GeSe monolayers capable of a mechanical response to an applied electric field.

Here, we use density functional theory (DFT) calculations to characterize the multistability of SnS and GeSe, exploring ways in which the phase transitions and domain switch can be triggered externally. We start by demonstrating how the reversible phase transition can be induced by uniaxial stress or electric field. Then, we show how the phase and lattice orientation states can be detected using the valley properties.

## METHODS

The calculations were based on density functional theory (DFT) implemented in the QUANTUM ESPRESSO package [24]. The generalized gradient approximation (GGA) of Perdew-Burke-Ernzerhof (PBE) was used for the exchange and correlation functional, and Troullier-Martins type pseudopotentials [25]. The Kohn-Sham orbitals were expanded in a plane-wave basis with a cutoff energy of 70 Ry, and for the charge density a cutoff of 280 Ry was used. A $k$-point grid sampling grid was generated using the Monkhorst-Pack scheme with $10 \times 10 \times 1$ points [26], and a finer regular grid of $80 \times 80 \times 1$ was used

![](./images/867758934109192256_1.jpg)

FIG. 1. Schematic configuration-coordinate diagram for Cmcm-ML and Pnma-ML phases, in SnS and GeSe.

for transition probability calculations. The equilibrium structures were found by using a conjugate-gradient opti- mization algorithm, and the energy landscape is mapped by relaxing the structure under constraints for each of the in-plane lattice parameters, while all the other structural parameters are allowed to relax.

We used the modern theory of polarization [27] to cal- culate the spontaneous polarization given by

$$
\vec{\mathcal{P}}=\frac{1}{\Omega} \sum_{\tau} q_{\tau}^{\mathrm{ion}} \mathbf{R}_{\tau}-\frac{2 i e}{(2 \pi)^{3}} \sum_{n}^{\mathrm{occ}} \int_{B Z} d^{3} \mathbf{k} e^{-i \vec{k} \cdot \mathbf{R}}\left\langle u_{n \mathbf{k}}\right| \frac{\partial u_{n \mathbf{k}}}{\partial \mathbf{k}}\right\rangle,
$$

where $q_{\tau}$ is the ionic charge plus the core electrons, $\mathbf{R}_{\tau}$ is the position of ions, $\Omega$ is the unit cell volume, e is the elementary charge, $n$ is the valence band index, $\mathbf{k}$ is the wave vector, and $u_{n \mathbf{k}}$ is the electronic wave function. The first term is the contribution from ions and core electrons, and the second term is the electronic contribution defined as adiabatic flow of current which can be calculated from the Berry connection [27].The response of the material to a homogenous static external electric field is calcu- lated based on methods developed by Refs. [28, 29] im- plemented in the QUANTUM ESPRESSO package [24].

# RESULTS

## Multistability of SnS and GeSe in the monolayer phase

We start by exploring the energy landscape of mono- layer SnS and GeSe. We consider the monolayer form of the two structures that are known for bulk SnS ie., a cen- trosymmetric structure (Cmcm), and the Pnma struc- ture resembling black phosphorus, and which is the only known layered structure of bulk GeSe. We will designate the respective monolayer phases by appending 'ML' to the respective bulk space group.

The atomic positions in the Pnma-ML phase are $\pm$(M:0.25$\pm \delta$, 0.25, 0.05; X:0.25, 0.25, -0.05) in fractional coordinates, where M=(Sn, Ge) and X=(S, Se), $\delta=0.06$ and 0.08 for SnS and GeSe, respectively. The Cmcm- ML phase is obtained by taking $\delta=0$. As a result, the Cmcm-ML has two perpendicular mirror symmetry planes, as well as inversion symmetry, while Pnma-ML has no inversion symmetry. In our DFT simulations we used $\delta=0.01$ as a tolerance to distinguish the Pnma-ML phase from the Cmcm-ML phase [30].

![](./images/867758934109192256_2.jpg)

FIG. 2. Stress-strain curves of monolayer (a) SnS and (b) GeSe for tensile strain along the $\hat{x}$ (black circle) and $\hat{y}$ (red square) directions. (I) indicates the Pnma-ML structure re- configuration such that the puckering (armchair) direction $\hat{d}_{\text{puck}}$ becomes $\hat{y}$ instead of $\hat{x}$. (II) indicates the transforma- tion into an hexagonal phase. In the insets of (a) and (b), the strain in the $\hat{y}$ direction was shifted to highlight the rotation of the Pnma-ML structure by $\pi/2$, swapping the armchair and zigzag directions. (c) and (d) top and side view of SnS structure with $\hat{d}_{\text{puck}}=\hat{x}$. The larger grey atom is Sn and the smaller yellow atom is S. (e) The respective Brillouin zone and the high symmetry points.

The Pnma-ML and the Cmcm-ML phases can both be seen as distortions of a rocksalt bilayer that can be transformed into each other by a displacement of some of the atoms along $\hat{x}$ (see Fig.2 for $\hat{x}$ and $\hat{y}$ directions). For SnS, Cmcm-ML is a local minima of the energy sur- face. For GeSe, the Cmcm-ML structure is not an en- ergy minimum but a saddle point. The activation energy for reorientation of the Pnma-ML puckering direction is very small (88 meV for SnS and 43 meV for GeSe). We note that GGA has been successful in predicting the small enthalpy differences (tens of meV) between differ- ent phases of ferroelectric materials, because systematic errors cancel out when comparing systems with very sim- ilar structures [32]. The broken inversion symmetry and total energy with a typical double-well potential of SnS and GeSe are the first two indications that these materi- als may possess ferroelectricity.

![](./images/867758934109192256_3.jpg)

FIG. 3. Structural visualization of clamped SnS monolayer under uniform electric field at points of transition. Puckering and electric dipole orientation (red arrow) can switch from positive $\hat{x}$ (b) to either negative $\hat{x}$ (a) or positive $\hat{y}$ (c) depending on the directions of applied electric field.

### Application of uniaxial stress

The phase transition of SnS to $Cmcm$-ML, or equivalently the reorientation of the $Pnma$-ML structure, can be induced by in-plane uniaxial tensile stress (Fig. 2). We use an effective thickness to estimate the values of stress, as outlined in Ref. [23].

For uniaxial stress along $\hat{y}$, the SnS structure begins to resemble $Cmcm$-ML as the shorter lattice parameter $b$ is stretched. For $\epsilon_{y}>0.08$, uniaxial stress results in the rotation of the $Pnma$-ML structure by $\pi/2$. The puckering $\hat{d}_{\text{puck}}$ thus rotates from $\hat{x}$ to $\hat{y}$ [Fig. 2(a), transition I]. Similar qualitative behavior is observed in GeSe (see Fig. 2(b)). Both SnS and GeSe transit to $Cmcm$ phase, but they spontaneously revert back to $Pnma$ once the tensile stress is removed [33].

The application of uniaxial stress along $\hat{x}$ reveals another phase transition at $\epsilon_{x}=0.72$ and $0.78$ for SnS and GeSe, respectively. The structure is a hexagonal phase resembling blue phosphorene (see Ref. [34]). The hexagonal structure and its band structure are plotted in Fig. 4.

### Application of electric field

Application of an electric field is an alternative way to trigger the transition between different minima on the energy surface of SnS or GeSe. Since the $Pnma$-ML structure is piezoelectric, the application of an electric field along the polar ($\hat{x}$) direction in a mechanically free sample induces strain as well [23]. However, here we will consider, for simplicity, the application of an electric field to a mechanically clamped sample.

The spontaneous polarization in the $Pnma$-ML phase, which was measured with respect to the centrosymmetric structure by taking as the effective volume the equivalent volume occupied by a layer of the bulk unit cell, is 0.6 and $1.7\ \text{C/m}^2$ for SnS and GeSe, respectively, which is comparable to that of 3D ferroelectrics [35].

In this case, application of an electric field with polarity opposed to the bond dipole results in bonds breaking and creates new bonds with inversion of the polarization along $\hat{x}$, rather than in a rotation of the structure. As shown in Fig. 3 (a) the ionic configuration changes (i.e., $\hat{d}_{\text{puck}}$ switches from $\hat{x}$ to $-\hat{x}$), and it is apparent from Eq. 1 that the electric dipole orientation can be switched, which we have found to be the case based on our DFT calculations.

The coercive field for this puckering transformation is $0.18\times 10^{7}\ \text{V/cm}$ for SnS and $0.51\times 10^{7}\ \text{V/cm}$ for GeSe. Moreover, we found that applying an electric field in $\hat{y}$ at $0.29\times 10^{7}\ \text{V/cm}$ ($0.80\times 10^{7}\ \text{V/cm}$) could also convert the $\hat{d}_{\text{puck}}$ from $\hat{x}$ to $\hat{y}$ for SnS (GeSe). The coercive field calculated by this method corresponds to the electric field at which the unfavorable phase becomes unstable and can be seen as an upper bound for the coercive field of a real multi-domain material. This is usually smaller provided that the domain walls are mobile at that temperature and, according to a recent work [36], the domain wall energy is small for this class of materials. Thus, the electric fields necessary for ferroelectric switching are clearly achievable in current 2D experiments [37]. The structures of SnS monolayer under electric fields at which the puckering orientation switches are plotted in Fig. 3.

Since the two materials possess a spontaneous, reversible polarization and bistability, they classify as ferroelectrics. The configuration-coordinate diagram of GeSe is typical of a ferroelectric with second-order phase transition at $T=0$ (consistent with the change in symmetry). The energy curve for SnS has a minimum rather than a saddle point at $Cmcm$-ML, and therefore resembles a ferroelectric with first order phase transition, with the peculiarity that the $Cmcm$-ML structure is stable for all $T>0$. Recently, based on Car-Parrinello molecular dynamics simulations, Mehboudi et al. showed that monolayer monochalcogenides undergo an order-disorder phase transition [31]. Hence, since SnS and GeSe have four degenerate $Pnma$-ML phases, we expect that the average total polarization goes to zero as temperature approaches $T_{\text{m}}$.

### Band structure

The phase transitions are accompanied by changes of the band structure and can, therefore, be detected optically. Representative SnS and GeSe band structures under uniaxial stress are shown in Fig. 4 and Fig. 5, respectively. We note that even though the band gap is underestimated due to our usage of DFT as the calculation method [21], the dispersion of the bands is accurately reproduced. Unstrained SnS is an indirect-gap semiconductor with its valence band maximum located near the X-point (along the $\Gamma$-X line) and the conduction band minimum near the Y-point (along the $\Gamma$-Y line). There are,

![](./images/867758934109192256_4.jpg)

FIG. 4. Representative band structures of SnS monolayers (a) unstrained, (b) to (d) under tensile uniaxial stress along the $\hat{x}$ for axial strains of $\epsilon_x=0.22$ to $\epsilon_x=0.75$, and (e) to (g) under tensile uniaxial stress along $\hat{y}$ for axial strains of $\epsilon_y=0.02$ to $\epsilon_y=0.27$. The dotted lines locate the valence band maxima. The corresponding side and top view of structural visualizations are below the band structure plots. It is apparent that the band structure (b) $\epsilon_x=0.22$ (or an uniaxial stress of $\sigma_{xx}\sim1.4$GPa) is equivalent to the band structure (g) $\epsilon_y=0.27$ (or an uniaxial stress of $\sigma_{yy}\sim1.4$GPa) if the $\hat{x}$ and $\hat{y}$ are inverted (rotation around $\Gamma$ axis on figures).

![](./images/867758934109192256_5.jpg)

FIG. 5. Evolution of GeSe band structure with strains in armchair (a) to (d) and zigzag direction (e) to (h). The dotted lines locate the valence band maxima. The structure inversion is found at $\epsilon_y=0.15$. It is apparent that the band structure (b) $\epsilon_x=0.22$ (or an uniaxial stress of $\sigma_{xx}\sim1.4$GPa) is equivalent to the band structure (h) $\epsilon_y=0.30$ (or an uniaxial stress of $\sigma_{yy}\sim1.4$GPa) if the $\hat{x}$ and $\hat{y}$ are inverted (rotation around $\Gamma$ axis on figures).

therefore, two two-fold degenerate valleys, designated $V_x$ and $V_y$, respectively. At large strains along $\hat{x}$, SnS transforms to a hexagonal phase at $\epsilon_x=0.72$ resembling blue phosphorene (Fig. 4 (c)) [34] and becomes a direct gap at $\epsilon_x=0.75$. For uniaxial stress along $\hat{y}$ there is a transition from indirect gap to direct gap at $\epsilon_y=0.02$ (see Fig. 4(e)), after which the system again becomes indirect gap.

The band structure of GeSe under uniaxial stress is shown in Fig. 5 (a) to (d) for the $\hat{x}$ and (e) to (h) for the $\hat{y}$. Even though unstrained GeSe is a direct-gap semiconductor, there are also two nearly degenerate conduction band minima at the $V_x$ and $V_y$ points. The swapping between the $\hat{x}$ and $\hat{y}$ of the $Pnma$-ML structure under tensile stress along the $\hat{y}$ direction occurs at $\epsilon_y=0.15$ and is in this case accompanied by a loss of the direct bandgap, which becomes indirect as the structure reverts back into $Pnma$-ML. As shown in Fig. 5, the band structure (b) $\epsilon_x=0.22$ is equivalent to the band structure (h) $\epsilon_y=0.30$ if the $\hat{x}$ and $\hat{y}$ are inverted (rotation around $\Gamma$ axis on figures). The transition to a hexagonal phase under tensile stress along $\hat{x}$ ($\epsilon_x=0.78$) is also accompanied by an indirect- to direct-gap semiconductor transition.

In addition, we calculated the projected density of states for SnS and GeSe for various strains (Fig. 6). The trends of the evolution of PDOS of GeSe and SnS with increasing strain are similar. Specifically, the relative contributions of the $p$-orbitals for Sn and Ge atoms at energies close to the maximum valence band increases with increasing strain.

The selection of valleys $V_x$ or $V_y$ can be achieved by at least two different optical methods: (i) using the fact that the direct gap is different at the two valley pairs; or (ii) using the optical selection rules. The direct transitions at the $V_x$ and $V_y$ valleys have different energies, provided there is a means to identify the orientation of the crystal (Fig. 7). We plot the energy difference between valence and conduction band of SnS as functions of in plane wave

![](./images/867758934109192256_6.jpg)

FIG. 6. Projected density of states (PDOS) of SnS (a) to (e) and GeSe (f) to (j) for different strains. The top panels are PDOS of Sn (Ge) atom and the bottom panels are PDOS of S (Se) atom.

vectors shown in Fig. 7 (a) and (b). It can be seen that the gap surface of $\epsilon_x = 0.22$ (Fig. 7 (a)) is equivalent to $\epsilon_y = 0.27$ (Fig. 7 (b)) but rotated $90^\circ$. It is evident that under uniaxial stress in $\hat{y}$ the bands have rotated in the Brillouin Zone, i.e. the $V_y$ valley effectively becomes the $V_x$ valley after passing the transition point of $\epsilon_y$=0.08.

### Transition probabilities

Using linearly polarized light to select the valleys $V_x$ or $V_y$ provides an additional method to detect the phase transition optically. The interband transition probability at a given wave vector $\mathbf{k}$ is given by [7, 38]

$$
P_{i}(\mathbf{k}) \propto\left|\frac{m}{\hbar}\left\langle c(\mathbf{k})\left|\frac{\partial H}{\partial k_{i}}\right| v(\mathbf{k})\right\rangle\right|^{2}, \tag{2}
$$

where $i$ is the direction of the light polarization, $c(\mathbf{k})$ is the conduction band wave function, $v(\mathbf{k})$ is the valence band wave function, and $H$ is the Hamiltonian. Alternatively, one can relate the transition probability to the dipole moment between the initial and the final bands: $\langle\mathbf{c}|\hat{p}_{x/y}|\mathbf{v}\rangle$, where the momentum direction corresponds to the light polarization. For the transition to be allowed, the dipole moment must not vanish. It is possible to determine whether it is finite or not using the symmetry of the bands and the momentum. Since the dipole moment is computed by integrating the product of the initial and final wave functions, and the momentum, it is nonzero only if this product $(\propto \mathbf{c}^{\dagger}(\mathbf{r})\partial_{x/y}\mathbf{v}(\mathbf{r}))$ is not odd with respect to any of the axes. In other words, the integrand must remain unchanged under every symmetry transformation of the space group characterizing the crystal.

We used our $ab$ initio results to calculate the transition probabilities. For unstrained SnS, $\hat{y}$-polarized light populates only the $V_y$ valleys, as there is no coupling between the valence and conduction band at $V_x$ in the $\hat{y}$ direction (see Fig. 7 (e)). As shown by Ref. [38], the conduction band, valence band, and the $p_x$ have a same irreducible representation. Consequently, the direct product of these quantities results in a non-vanishing transition probability coupling. On the other hand, $\hat{y}$-polarized light cannot excite $V_x$, as it possesses differ-

![](./images/867758934109192256_7.jpg)

FIG. 7. Band gap surfaces (a) $\epsilon_x = 0.22$ and (b) $\epsilon_y = 0.27$ demonstrate the valley swapping. (c) Schematic selective valley polarization. (d) Evolution of the bandgap and (e, f) relative polarization under uniaxial stress along $\hat{y}$, highlighting the phase transition. Under small strain, the direct transition at $V_x$ is only visible under incident $x$-polarized light, while the $V_y$ transition is visible under both incident $y$ and $x$ (with a small coupling) polarized light.

ent representation. $\hat{x}$-polarized light can populate both $V_x$ and $V_y$ but it populates predominantly the $V_x$ valleys, with $P_x(V_x)/P_x(V_y) \sim 40$. Similar behavior is observed in GeSe with a smaller selective valley polarization ratio. For instance, with linearly $\hat{x}$-polarized light the selective valley polarization ratio was found to be $P_x(V_x)/P_x(V_y) \sim 15$. The schematic valley polarization is shown in Fig. 7 (c).

The evolution of local gap $V_x$ and $V_y$ of SnS under stress in the $\hat{y}$ direction is shown in Fig. 7(d). We see that there is an abrupt change in $V_y$ gap near the transition point $\epsilon_y = 0.08$. We also plot the relative polarization $P_y(V_x)/P_x(V_x)$ and $P_x(V_y)/P_y(V_y)$ as a function of axial strain $\epsilon_y$, shown in Fig. 7(e) and (f) for SnS and GeSe, respectively. As we discussed earlier, $\hat{x}$-polarized light populates predominantly the $V_x$ valleys but there is still a small transition probability at $V_y$ when $\hat{x}$-polarized light is used. The absorption threshold for $\hat{x}$-polarized light has an abrupt change near $\epsilon_y = 0.08$ ($\epsilon_y = 0.15$ for GeSe), when the phase transition takes place. However, the absorption edge for $\hat{y}$-polarized light changes smoothly.

Before the transition point, the structure has a mirror symmetry inverting $\hat{y}$, and the $V_y$ valleys can be populated using polarized light along $\hat{y}$ and $\hat{x}$ (the latter with a very small coupling). However, after the transition point, the puckering direction is rotated to be in the $\hat{y}$, and the reflection symmetry in $\hat{y}$ is broken, whereas a reflection symmetry emerges in $\hat{x}$. As a result, $V_x$ can be excited by both $\hat{x}$ and $\hat{y}$ polarized light after the transition takes place. We have therefore demonstrated how optical transitions can be used to detect the orientation of the structure which determines valley configurations.

In summary, we have used first-principles calculations to demonstrate the potential of group-IV monochalcogenide monolayers as functional materials for information storage. This strategy, demonstrated using SnS and GeSe as prototypes, relies on the metastability and the possibility of switching the polarization direction using stress or electric field, creating a binary memory device. Comparing these prototype materials, SnS differs from GeSe because it has a stable centrosymmetric phase which, at $T=0$, is close in energy to the $Pnma$-ML phase.

Due to their peculiar band structures, both SnS and GeSe could in principle be used as functional materials for memory devices that can be easily interfaced with valleytronics logic. Valleytronics is based on the concept that the valley index can potentially be used to store information for subsequent logic operations, equivalent to spin in spintronics. However, in most valleytronics materials the information can be considered non-volatile only up to the timescale defined by inter-valley scattering processes, which are ubiquitous in real materials. Structural changes, used to store information in phase change memory devices, take place on a timescale orders of magnitude longer. Materials such as SnS and GeSe can be used to convert information stored as structural phase into information stored as valley index. One possibility is for example by using near-bandgap light that excites only the pair of valleys corresponding to the lowest energy exciton. The subsequent electronic state will have electron-hole pairs with momentum $(\pm k_x, 0)$ or $(0, \pm k_y)$, depending on the structure orientation. This valley state can be transmitted onto a valley-filter [39]. Alternatively, if coupled to a polarized light detector, the polarization switching can be detected optically taking advantage of valley-dependent direction of the linear polarization of the luminescence [38].

P.Z.H. is grateful for the support of the Physics and Mechanical Engineering Departments at Boston University, the hospitality of the NUS Centre for Advanced 2D Materials and Graphene Research Centre where this work was initiated, the support of the Materials Science and Engineering Innovation Grant and the Boston University High Performance Shared Computing Cluster. A.C. acknowledges support by the National Research Foundation, Prime Minister Office, Singapore, under its Medium Sized Centre Programme and CRP award "Novel 2D materials with tailored properties: beyond graphene" (Grant No. R-144-000-295-281). D.K.C. is grateful for the hospitality of the Aspen Center for Physics which is supported by NSF Grant #PHY-1066293, and of the International Institute for Physics of the Federal Uni-

versity of Rio Grande do Norte, in Natal, Brazil, where some of this work was completed. HSP acknowledges the support of the Mechanical Engineering Department at Boston University. We thank Alex Rodin for helpful comments and discussions.

* Corresponding author: dkcampbe@bu.edu
† Corresponding author: parkhs@bu.edu

[1] P. Miro, M. Audiffred, and T. Heine, *Chem. Soc. Rev.* 43, 6537 (2014).

[2] V. Nicolosi, M. Chhowalla, M. G. Kanatzidis, M. S. Strano, and J. N. Coleman, *Science* 340 (2013).

[3] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, and M. S. Strano, *Nature Nanotechnology* 7, 699 (2012).

[4] P. Johari and V. B. Shenoy, *ACS Nano* 6, 5449 (2012).

[5] M. Chhowalla, H. S. Shin, G. Eda, L.-J. Li, K. P. Loh, and H. Zhang, *Nature Chemistry* 5, 263 (2013).

[6] H. Zeng, J. Dai, W. Yao, D. Xiao, and X. Cui, *Nature Nanotechnology* 7, 490 (2012).

[7] D. Xiao, G.-B. Liu, W. Feng, X. Xu, and W. Yao, *Phys. Rev. Lett.* 108, 196802 (2012).

[8] E. J. Sie, J. W. McIver, Y.-H. Lee, L. Fu, J. Kong, and N. Gedik, *Nature Materials* 14, 290 (2014).

[9] J. Kim, X. Hong, C. Jin, S.-F. Shi, C.-Y. S. Chang, M.-H. Chiu, L.-J. Li, and F. Wang, *Science* 346, 1205 (2014).

[10] M. Sepioni, R. R. Nair, S. Rablen, J. Narayanan, F. Tuna, R. Winpenny, A. K. Geim, and I. V. Grig- orieva, *Phys. Rev. Lett.* 105, 207205 (2010).

[11] E. B. Song, B. Lian, S. M. Kim, S. Lee, T.-K. Chung, M. Wang, C. Zeng, G. Xu, K. Wong, Y. Zhou, *et al.*, *Applied Physics Letters* 99, 042109 (2011).

[12] Y. Zheng, G.-X. Ni, C.-T. Toh, C.-Y. Tan, K. Yao, and B. Özyilmaz, *Phys. Rev. Lett.* 105, 166602 (2010).

[13] R. Simpson, P. Fons, A. Kolobov, T. Fukaya, M. Krbal, T. Yagi, and J. Tominaga, *Nature Nanotechnology* 6, 501 (2011).

[14] S. Alptekin, *Journal of Molecular Modeling* 17, 2989 (2011).

[15] T. Chattopadhyay, A. Werner, H. Von Schnering, and J. Pannetier, *Revue de Physique Appliquée* 19, 807 (1984).

[16] V. L. Deringer, R. P. Stoffel, and R. Dronskowski, *Phys. Rev. B* 89, 094303 (2014).

[17] A. S. Rodin, A. Carvalho, and A. H. Castro Neto, *Phys. Rev. Lett.* 112, 176801 (2014).

[18] H. Liu, A. T. Neal, Z. Zhu, Z. Luo, X. Xu, D. Tomnek, and P. D. Ye, *ACS Nano* 8, 4033 (2014).

[19] J. R. Brent, D. J. Lewis, T. Lorenz, E. A. Lewis, N. Sav- jani, S. J. Haigh, G. Seifert, B. Derby, and P. OBrien, *Journal of the American Chemical Society* 137, 12689 (2015).

[20] B. Mukherjee, Y. Cai, H. R. Tan, Y. P. Feng, E. S. Tok, and C. H. Sow, *ACS Applied Materials & Interfaces* 5,9594 (2013).

[21] L. C. Gomes and A. Carvalho, *Phys. Rev. B* 92, 085406 (2015).

[22] R. Fei, W. Li, J. Li, and L. Yang, *Applied Physics Letters* 107, 173104 (2015).

[23] L. C. Gomes, A. Carvalho, and A. H. Castro Neto, *Phys. Rev. B* 92, 214103 (2015).

[24] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococ- cioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcov- itch, *Journal of Physics: Condensed Matter* 21, 395502 (19pp) (2009).

[25] N. Troullier and J. L. Martins, *Phys. Rev. B* 43, 1993 (1991).

[26] H. J. Monkhorst and J. D. Pack, *Phys. Rev. B* 13, 5188 (1976).

[27] R. D. King-Smith and D. Vanderbilt, *Phys. Rev. B* 47, 1651 (1993).

[28] I. Souza, J. Íñiguez, and D. Vanderbilt, *Phys. Rev. Lett.* 89, 117602 (2002).

[29] P. Umari and A. Pasquarello, *Phys. Rev. Lett.* 89, 157602 (2002).

[30] We define puckering orientation as a unit vector of the in plane bond formed by the nearest neighbor of MX atoms in the direction of the broken mirror symmetry. For the SnS structure shown in Fig. 2(d), the puckering direction $\hat{d}_{\text{puck}} = \hat{x}$ as we define $\hat{d}_{\text{puck}} = \frac{\hat{x}_\text{S}-\hat{x}_\text{Sn}}{|\hat{x}_\text{S}-\hat{x}_\text{Sn}|}$.

[31] M. Mehboudi, A. M. Dorio, W. Zhu, A. van der Zande, H. O. H. Churchill, A. A. Pacheco-Sanjuan, E. O. Harriss, P. Kumar, and S. Barraza-Lopez, *Nano Letters* 16, 1704 (2016).

[32] S. Sanna, C. Thierfelder, S. Wippermann, T. P. Sinha, and W. G. Schmidt, *Phys. Rev. B* 83, 054112 (2011).

[33] We found that once the stretch is removed the $Cmcm$ structure spontaneously reverts back to $Pnma$ for both SnS and GeSe. However, we found that during *compres- sion*, the $Cmcm$ phase of SnS is stable.

[34] M. Mehboudi, K. Utt, H. Terrones, E. O. Harriss, A. A. Pacheco SanJuan, and S. Barraza-Lopez, *Proceedings of the National Academy of Sciences* 112, 5888 (2015).

[35] W. Zhong, R. King-Smith, and D. Vanderbilt, *Physical review letters* 72, 3618 (1994).

[36] H. Wang and X. Qian, arXiv preprint arXiv:1606.04522 (2015).

[37] B. Radisavljevic, A. Radenovic, J. Brivio, V. Giacometti, and A. Kis, *Nature nanotechnology* 6, 147 (2011).

[38] A. S. Rodin, L. C. Gomes, A. Carvalho, and A. H. Cas- tro Neto, *Phys. Rev. B* 93, 045431 (2016).

[39] D. Gunlycke and C. T. White, *Phys. Rev. Lett.* 106, 136806 (2011).