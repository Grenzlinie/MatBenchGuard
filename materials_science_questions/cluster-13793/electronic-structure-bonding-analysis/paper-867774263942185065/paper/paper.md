
# Fluorination-Enriched Electronic and Magnetic Properties in Graphene Nanoribbons

Duy Khanh Nguyen, \( ^{*,\dagger} \)  Yu-Tsung Lin, \( ^{\dagger} \)  Shih-Yang Lin, \( ^{\ddagger} \)  Yu-Huang Chiu, \( ^{\ddag} \)  Ngoc Thanh Thuy Tran, \( ^{\dagger} \)  and Ming Fa-Lin \( ^{*,\dagger} \) 

 \( ^{\dagger} \) Department of Physics, National Cheng Kung University, 701 Tainan, Taiwan
 \( ^{\ddagger} \) Department of Applied Physics, National Pingtung University, 900 Pingtung, Taiwan

E-mail: nguyenkhanhphysics2015@gmail.com; mflin@mail.ncku.edu.tw

Phone: +886-6-275-7575. Fax: 886-6-274-7995

## Abstract

The feature-rich electronic and magnetic properties of fluorine-doped graphene nanoribbons are investigated by the first-principles calculations. They arise from the cooperative or competitive relations among the significant chemical bonds, finite-size quantum confinement and edge structure. There exist C-C, C-F, and F-F bonds with the multi-orbital hybridizations. Fluorine adatoms can create the p-type metals or the concentration- and distribution-dependent semiconductors, depending on whether the  \( \pi \)  bonding is seriously suppressed by the top-site chemical bonding. Furthermore, five kinds of spin-dependent electronic and magnetic properties cover the non-magnetic and ferromagnetic metals, the non-magnetic semiconductors, and the anti-ferromagnetic semiconductors with/without the spin splitting. The diverse essential properties are clearly revealed in the spatial charge distribution, the spin density, and the orbital-projected density of states.

Keywords: Multi-orbital hybridizations, fluorination, top-site doping, buckled structures, strong electron affinity
 

## Introduction

A new scientific era has been opened since the discovery of graphene. \( ^{1} \)  This 2D system exhibits a lot of novel and unusual electronic properties. \( ^{2} \)  However, there exist few obstacles in the potential applications of graphene-based materials. \( ^{3} \)  To overcome the gapless feature, the direct method is to create one-dimensional (1D) strips of graphene, usually referred to as graphene nanoribbons. \( ^{4} \)  GNRs are one of the main-stream nanomaterials, mainly owing to the complex relations among honeycomb lattice, one-atom thickness, finite-size quantum confinement and edge structure. Each GNR could be regarded as a finite-width graphene strip or an unzip carbon nanotube. \( ^{5} \)  Up to now, GNRs have been successfully synthesized by the various experimental methods including both top-down and bottom-up schemes. \( ^{6} \)  From the geometric point of view, graphene cutting seems to be the simplest and intuitive method, in which the available routes cover lithographic patterning \( ^{7} \)  and etching of graphene, \( ^{8} \)  sonochemical breaking, \( ^{9} \)  metal-catalyzed cutting of graphene, \( ^{10} \)  and oxidation cutting of graphene. Another approach is to unzip carbon nanotube using metal nanoclusters as scalpels, \( ^{11} \)  and a wet chemical method based on acid reactions. \( ^{12} \)  The chemical vapor deposition is utilized to massively produce GNRs to meet the essential requirement of semiconductor industry. \( ^{13} \)  GNRs are expected to have high potential applications in nanoelectronic \( ^{14} \)  and spintronic \( ^{15} \)  devices, gas sensor, \( ^{16} \)  and nanocomposites. \( ^{17} \) 

Interestingly, electronic properties of GNRs can be easily modulated by chemical doping, \( ^{18} \)  mechanical strain, \( ^{19,20} \)  layer number, \( ^{21} \)  curved surface, \( ^{22} \)  edge-passivation, \( ^{23,24} \)  stacking configuration; \( ^{25} \)  electric \( ^{26,27} \)  and magnetic \( ^{28,29} \)  fields. Among these modulations, the chemical modification on ribbon surface is the most effective one in creating the dramatic changes between the semiconducting and metallic behaviors (the non-magnetic and magnetic configurations). The previous theoretical studies clearly show the geometry- and doping-enriched electronic and magnetic properties. Two typical achiral GNRs, armchair and zigzag ones (AGNRs and ZGNRs), present the width-dependent energy gaps, \( ^{30,31} \)  and the latter possess the anti-ferromagnetic spin configuration across the ribbon center. \( ^{32} \)  The chemical dopings
 

of transition metal Co/Ni adatoms will induce the metallic band structures with free conduction electrons, \( ^{33} \)  in which the spin-split energy bands correspond to the ferromagnetic configuration. However, alkali adatoms can create the non-magnetic metals in AGNRs and the ferromagnetic ones in ZGNRs under specific distributions. \( ^{34} \)  The ligand-protected aluminum clusters adsorbed AGNRs lead to the semiconducting or metallic band structures, depending on their kinds. \( ^{35} \)  As for molecule adsorptions,  \( (\mathrm{CO}, \mathrm{NO}, \mathrm{NO}_{2}, \mathrm{O}_{2}, \mathrm{N}_{2}, \mathrm{CO}_{2}) \)  do not change the semiconducting behavior, \( ^{36} \)  while  \( NH_{3} \)  presents the n-type doping. On the experimental side, the adsorption of hydrogen molecules on the Pd-functionalized multi-layer GNRs are successfully obtained, \( ^{37} \)  and tin oxide nanoparticles are also synthesized on GNRs to form a composite material. \( ^{38} \)  These results indicate that surface chemical adsorption may serve as a tool for controlling the electronic properties of GNRs. \( ^{39} \)  However, a systematic theoretical study on the halogen-adsorbed GNRs is absent up to now. Fluorine adatoms have very strong electron affinity; they are thus expected to present the significant chemical bondings with carbon atoms and greatly diversify the essential properties.

This work is focused on the essential geometric, electronic and magnetic properties of fluorine-doped GNRs. They are explored in detail by using the density functional theory. The bond lengths, positions of adatoms, ground state energies, energy bands, spatial charge distributions, free carrier densities, spin densities, magnetic moments, and density of states (DOS) are evaluated using the first-principles calculations. The dependence on concentration, distribution of adatoms, and edge structure is fully included in the calculations. By the detailed analyses, the critical orbital hybridizations in chemical bonds are identified from atom-dominated energy bands, the spatial charge distribution, and the orbital-projected DOSs. The current study shows that they are responsible for the diverse electronic and magnetic properties, covering the ferromagnetic and non-magnetic metals, the non-magnetic semiconductors, and the anti-ferromagnetic semiconductors with/without spin splitting. Furthermore, the feature-rich band structures are reflected in a lot of prominent peaks in DOSs. The predicted optimal geometries, energy bands and DOSs could be verified by scanning
 

tunneling microscopy (STM) \( ^{40} \) , angle-resolved photoemission spectroscopy (ARPES) \( ^{41} \)  and scanning tunneling spectroscopy (STS) \( ^{42} \) , respectively.

## Computational methods

The essential properties of F-doped GNRs are investigated by using the Vienna ab initio simulation package \( ^{43} \)  within the spin-polarized density functional theory. The exchange and correlation energies, which come from the many-particle Coulomb interactions, are evaluated from the Perdew-Burke-Ernzerhof functional \( ^{44} \)  under the generalized gradient approximation. Furthermore, the projector-augmented wave pseudopotentials can characterize the electron-ion interactions. \( ^{45} \)  Plane waves, with an maximum energy cutoff of 400 eV, are utilized to calculate wave function and state energies. The 1D periodic boundary condition is along  \( \hat{x} \) , and the vacuum spacing associated with  \( \hat{y} \)  and  \( \hat{z} \)  is larger than 15 Å to avoid the interactions between two neighboring nanoribbons. The Brillouin zone is sampled by  \( 15 \times 1 \times 1 \)  and  \( 100 \times 1 \div 1 \)  k point meshes within the Monkhorst-Pack scheme for geometric optimizations and further calculations on electronic structures, respectively. The convergence for energy is set to be  \( 10^{-5} \)  eV between two simulation steps, and the maximum Hellmann-Feynman force acting on each atom is less than 0.01 eV/ \( \AA \)  during the ionic relaxations.

## Results and discussion

The geometric, electronic and magnetic properties of fluorine-adsorbed GNRs are investigated for various distributions and concentrations of adatoms in zigzag and armchair systems. The widths of AGNR and ZGNR, as shown in Figs. 1(a) and 1(b), are characterized by the number of dimers lines and zigzag lines ( \( N_{A} \)  and  \( N_{Z} \) ) along  \( \hat{y} \) , respectively, in which the periodical lengths in a unit cell along  \( \hat{x} \)  are 3b and  \( 2\sqrt{3}b \)  (b the C-C bond length). In general, the double-side adsorptions have the lower ground state energies  \( E_{0} \) 's, compared to the single-side cases (Table 1). The optimal adatom position is situated at the top site,
 

regardless of any doping cases. Fluorination can induce the buckled GNR structure. Carbon atoms nearest to F deviate from the graphene plane, being sensitive to distributions and concentrations. For single adatom adsorption, the carbon heights are, respectively, 0.053 Å and 0.133 Å at center and edge of GNR. They obviously grow with F-concentration, e.g., 0.205 Å for 100% adsorption. F adatoms are very close to C, in which the shortest and longest F-C bond lengths (1.395 Å and 1.547 Å), respectively, correspond to the highest concentration and single adatom near ribbon center. Moreover, the nearest C-C bond lengths are lengthened in the range of 0.06 – 0.12 Å, compared with those of pristine GNRs. This indicates the  \( \sigma \) -bonding changes due to the strong fluorination. The critical F-C chemical bondings, being responsible for the featured geometric structures, are expected to dominate the other essential properties.

GNRs possess the unusual 1D band structures because of honeycomb symmetry, quantum confinement and edge structure. Pristine AGNRs present a lot of 1D energy bands, as shown in Fig. 2(a) for the  \( N_{A}=12 \)  system. The occupied valence bands are asymmetric to the unoccupied conduction bands about the Fermi level  \( E_{F} \) , in which a direct energy gap of  \( E_{g}^{d}=0.6~eV \)  at the  \( \Gamma \)  point arises from the finite-size effect. The electronic states of  \( E^{c,v}\leq2~eV \)  and the deeper ones are, respectively, dominated by the  \( \pi \)  bondings of parallel  \( 2p_{z} \)  orbitals, and the  \( \sigma \)  bondings of  \( (2p_{x},2p_{y}) \)  orbitals (indicated from the orbital-projected DOSs in Fig. 6(a)). Most of energy bands belong to parabolic dispersions, while few of them have partially flat ones within a certain range of  \( k_{x} \)  (e.g.,  \( E^{v}=-2.1~eV \)  and -4.7 eV). All the energy dispersions depend on wave vector monotonously except for the subband anti-crossings. The band-edge states, which occur at  \( k_{x}=0,1 \)  (in unit of  \( \pi/3b \) ), and others related to subband anti-crossings, will create the van Hove singularities in DOSs.

The semiconducting band structures are dramatically changed by the strong fluorination. For the single-adatom adsorption, the F-doped AGNRs exhibit the metallic energy bands, as clearly indicated from  \( (13)_{s} \)  in Figs. 2(b) and  \( (1)_{s} \)  in Fig. 2(c). The Fermi level is shifted to the  \( \pi \) -electronic valence states; that is,  \( E_{F} \)  presents a red shift. There exist free holes in the
 

unoccupied valence states between two Fermi momenta ( \( \pm k_{F} \)  related to two valence bands intersecting with  \( E_{F} \) ). Electrons are transferred from carbon atoms to fluorine adatoms. The low-lying energy bands mainly arise from the  \( \pi \)  bondings of carbon atoms, being independent of adatom positions. Moreover, the  \( (\mathrm{F},\mathrm{C}) \) -co-dominated energy bands, accompanied with the  \( \sigma \)  bands, appear at  \( E^{v} \leq -2.5 \)  eV. They have the weak energy dispersions or the narrow band widths. The rich features of energy bands further illustrate the critical F-C bondings, leading to the significant modifications of  \( \pi \)  and  \( \sigma \)  bands ( \( \pi \)  band and  \( \sigma^{2} \)  bondings).

The main features of electronic structures are very sensitive to the variations in the concentration, relative position, single- or double-side adsorptions, and edge structure. With the gradual increase of concentration, the Fermi-momentum states are drastically changed, as shown in Figs. 2(d)-2(h) for two-F adsorptions. The total free hole density, the summation of Fermi momenta in partially unoccupied  \( \pi \) -electronic valence bands, will become higher  \( [(6,21)_{s} \)  in Fig. 2(d) and  \( (6,21)_{d} \)  in Fig. 2(e); Table 1] or keep the same  \( [(1,23)_{s} \)  in Fig. 2(g) and  \( (1,23)_{d} \)  in Fig. 2(h)], compared to that of the single adatom (Figs. 2(b) and 2(c)). Moreover, the metallic band structure might be thoroughly changed into the semiconducting one for a very close adatom distance, e.g., an indirect gap of  \( E_{g}^{i}=0.64 \)  eV for the  \( (1,6)_{d} \)  adsorption in Fig. 2(f). This suggests the termination of the extended  \( \pi \)  bonding in AGNRs. Specifically, all the F-doped AGNRs belong to larger-gap semiconductors under high adatom concentrations (Figs. 2(j)-2(l)), in which the critical concentration is estimated to be about 10/24 in the  \( N_{A}=12 \)  system (Fig. 2(j)). There are more F-dependent valence bands. Such energy bands determine the magnitude of energy gap, and  \( E_{g} \)  also depends on the  \( \sigma \)  bonding of carbon atoms (DOSs in Figs. 6(c)-6(d)). A large gap of  \( E_{g}^{i}=3.2 \)  eV is revealed in the highest adatom concentration (100% adsorption in Fig. 2(l)). In addition, the single- and double-side adsorptions present the almost identical low-lying energy bands and spin configurations (e.g., Figs. 2(g) and 2(h); Figs. 4(b) and 4(c)), when the  \( (x,y) \)  projection and the adatom concentration keep the same.

The linear free hole density deserves a closer examination. It is linearly proportional to
 

the Fermi momentum by the relation  \( \lambda = 2k_{F}/\pi \)  for each partially unoccupied valence band. By the detailed calculations and analyses,  \( \lambda \)  has no simple relation with concentration except for one-adatom adsorption. A single F in a unit cell can create almost one free hole for any adsorption positions (Table 1), i.e., it attracts one electron from the bonded carbon atom because of rather strong electron affinity. The metallic 4-, 6-, and 8-adatom adsorptions can present two or one free holes in a unit cell, respectively, corresponding to the spin-degenerate and spin-split energy bands in Fig. 2 (non-magnetism and ferro-magnetism). However, only the lower carrier case is revealed in zigzag systems (Figs. 3(b) and 3(f); Table 1). In addition, when the fully unoccupied  \( \pi \) -electronic valence states are taken into account, each F adatom just contributes one hole in a unit cell. The F-doped GNRs are in sharp contrast with the alkali-doped systems. \( ^{46} \)  The latter belongs to n-type metals even for the 100% adatom concentration. Each alkali adatom generates one conduction electron from the outermost s orbital by means of the significant alkali-C bond, being independent of adatom distributions. This will lead to very high conduction electron density.

Edge structures play a critical role in the diverse essential properties. There are certain important differences between zigzag and armchair systems in band structures without or with fluorination. Pristine ZGNRs, as shown in Fig. 3(a), have a pair of partially flat valence and conduction bands nearest to  \( E_{F} \)  at small  \( k_{x} \) 's, corresponding to wave functions localized at the zigzag boundaries. \( ^{47} \)  Such bands have the double degeneracy for the spin degree of freedom even if they are closely related to the anti-ferromagnetic configuration across the ribbon center and the ferromagnetic one at the same edge (discussed in Fig. 4(d)). Their energy dispersions become strong at large  \( k_{x} \) 's. The band-edge states, which appear at  \( k_{x} = 1/2 \) , determine a direct gap of  \( E_{g}^{d} = 0.46 \)  eV for a  \( N_{Z} = 8 \)  ZGNR. This gap is due to the strong competition between quantum confinement and spin configuration. The partially flat bands near  \( k_{x} = 0 \)  and  \( E_{F} \) , with the localized charge distributions, might be changed by fluorination, such as, energy dispersions, energy gap, and state degeneracy in Figs. 3(b)-3(f). When one F adatom is very close to the zigzag edge, the number of edge-localized energy
 

bands is reduced to half in the presence of spin splitting, as shown for the  \( (3)_{s} \)  adsorption in Fig. 3(b). Furthermore, such bands intersect with the Fermi level and thus exhibit the metallic behavior (Table 1). They will disappear under two adatoms near both zigzag edges  \( [(3,30)_{s} \)  in Fig. 3(c) and  \( (3,30)_{d} \)  in Fig. 3(d)], leading to a direct-gap semiconductor (Table 1). As for the central two-F adsorption, the double of partial flat bands, with spin splitting, come to exist  \( [(11,14)_{d} \)  in Fig. 3(e)], in which half of them correspond to the edge- or center-localized electronic states. This system is an indirect narrow-gap semiconductor. Specifically, the number of low-lying flat bands keeps the same if two adatoms are, respectively, close to edge and center  \( [(3,14)_{d} \)  in Fig. 3(f)]. Their spin splitting creates a 1D metal. Also, it should be noticed that all the metallic F-absorbed ZGNRs, being related to the spin-split partially flat bands, present one free hole in a unit cell (Table 1).

The dependence of energy bands on electron spins is diversified by fluorine doping and edge. There exist five kinds of spin-dependent electronic and magnetic properties. The pristine AGNRs are confinement-induced semiconductors without spin-split energy bands and magnetism (the first kind in Fig. 2(a) and Table 1). The similar features are also revealed in the semiconducting F-doped AGNRs (Figs. 2(f) and 2(j)). However, the metallic systems might present the spin-degenerate energy bands in the absence of magnetism (the second kind in Figs. 2(d) and 2(e)), or the spin splitting with the ferromagnetic configuration (the third kind in Figs. 2(g) and 2(h)). As for ZGNRs, the pristine systems are the anti-ferromagnetic semiconductors without spin splitting (the fourth kind in Fig. 3(a)); furthermore, the F-doped ones present the first kind (Figs. 3(c) and 3(d)), the third kind (Figs. 2(b) and 2(f)), or the fifth kind (the semiconducting behavior with spin splitting under the anti-ferromagnetic configuration; Fig. 3(e)).

The spatial spin densities and magnetic moments could provide more information about the essential properties. The third, fourth and fifth kinds exhibit the different arrangements (Figs. 4(a)-4(d), Fig. 4(e) and Fig. 4(f)), in which the competition between the spin-up and spin-down configurations determines the net magnetic moment in a unit cell (Table 1).
 

The spin densities are mostly distributed near the edge structures except for the fifth kind (Fig. 4(f)). When one F is situated at the armchair (zigzag) edge, the ferromagnetic spin-up configuration occurs there (the similar one is created at another one), as shown in Fig. 4(a) (Fig. 4(d)). This leads to a net moment of 0.47 (0.42)  \( \mu_{B} \) . For two-F adsorptions near both boundaries, AGNRs exhibit the enhanced ferromagnetism across the ribbon center with 0.76  \( \mu_{B} \)  (Figs. 4(b) and 4(c)), while magnetism is absent in ZGNRs (Figs 3(c) and 3(d)). These illustrate that F adatoms close to the armchair and zigzag edges, respectively, create and destroy the same-spin arrangement there. The pristine ZGNRs, as indicated in Fig. 4(e), has an anti-ferromagnetic configuration in the absence of magnetic moment. Specifically, the coexistence of edge and center distributions is revealed in the central two-F adsorption (Fig. 4(f)), leading to an unusual anti-ferromagnetic configuration with a zero magnetic moment.

In addition to spin arrangements, the charge density  \( (\rho) \) , the charge density difference  \( (\Delta\rho) \) , and the partial charge density  \( (\rho_{P}) \)  are very useful in understanding the multi-orbital hybridizations in chemical bonds and the fluorination-enriched energy bands.  \( \Delta\rho \)  is generated by subtracting the charge density of GNR and F adatoms from that of F-absorbed system.  \( \rho \)  clearly illustrates the chemical bondings as well as the charge transfer. For a planar GNR, the parallel  \( 2p_{z} \)  orbitals and the planar  \( (2p_{x}, 2p_{y}, 2s) \)  orbitals, respectively, form the  \( \pi \)  and  \( \sigma \)  bondings, as shown in Fig. 5(a) for  \( N_{A} = 12 \)  AGNR (the solid and dashed rectangles). Fluorination can induce the high charge density between F and C, obvious change in  \( \pi \)  bonding, and observable reduction in  \( \sigma \)  bonding (Figs. 5(b) and 5(d)). The strong fluorination effects are also revealed in drastic density variations, especial for  \( (\Delta\rho) \)  near F adatoms on  \( (x, z) \)  and  \( (y, z) \)  planes (Figs. 5(c) and 5(e)). These clearly indicate the complicated  \( (2p_{x}, 2p_{y}, 2p_{z})-(2p_{x}, 2p_{y}, 2p_{z}) \)  hybridizations in F-C bonds. When the distance between two fluorine adatoms is sufficiently short, there exist the significant  \( (2p_{x}, 2p_{y}) \)  hybridizations in F-F bonds, as illustrated in Figs. 5(c) and 5(e) (red rectangles on  \( (x, z) \)  and  \( (y, z) \)  planes). As for the metallic and semiconducting behaviors, they are, respectively, characterized by the distorted and terminated  \( \pi \)  bondings in the partial charge density related to electronic
 

states very close to  \( E_{F} \)  (Figs. 5(f) & 5(h), and Figs. 5(g) & 5(i)).

The diverse electronic structures and magnetic configurations are clearly evidenced in the orbital- and spin-projected DOSs (Fig. 6). There are a plenty of special structures, in which the asymmetric and symmetric peaks, respectively, come from the parabolic and partially flat bands. When the F-concentration is below 50% (Figs. 6(a)-6(b) & 6(e)-6(g)), the low-energy DOS is dominated by the  \( \pi \)  bonding of C- \( 2p_{z} \)  orbitals (red curves). This bonding also makes contributions to the deeper-energy DOS. The peak structures, which is due to the  \( \sigma \)  bonding of  \( (2p_{x},2p_{y}) \)  orbitals, appear at E < -2.5 eV (green curves). The similar structures are revealed by the  \( (2p_{x},2p_{y}) \)  and  \( 2p_{z} \)  of the F adatoms (dashed blue and pink curves). The former present a sufficiently wide energy width of 2 eV, so that there exist the significant  \( (2p_{x},2p_{y}) \)  orbital hybridizations in F-F bonds. All the orbitals can create the merged peak structures at deeper energy, clearly illustrating the  \( (2p_{x},2p_{y},2p_{z}) \) -( \( 2p_{x},2p_{y},2p_{z} \) ) multi-orbital hybridizations in F-C bonds. Specifically, at high concentrations, the energy width of the bands might be more than 5 eV (Figs. 6(c)-6(d)); furthermore, the corresponding peaks are stronger than those of the  \( \sigma \)  bands. The occupied valence bands are closely related to the  \( (2p_{x},2p_{y}) \)  orbitals of F and C, especially for the orbital hybridization in F-F bonds.

Five kinds of essential properties are characterized by the specific peak structures near the Fermi level. A pair of anti-symmetric peaks near E = 0, which is divergent in the opposite direction, is characteristic of energy gap in the absence of spin splitting (the first kind), as shown in Figs. 6(a)-6(d). But for non-magnetic metals (the second kind), the similar pair presents a blue shift about 0.5 - 1.0 eV (Figs. 6(e) and 6(f), and DOS is finite at the Fermi level. The spin-polarized peak structures are revealed in ferromagnetic metals (the third kind in Figs. 6(g) and 6(h)). The low-energy peaks are quite different for spin-up and spin-down configurations, in which they are asymmetric about E = 0, and the former predominates the occupied states of E < 0. Specifically, the partially flat bands in a pristine ZGNR can create a pair of symmetric peaks (blue triangles in Fig. 6(i)), accompanied with an energy gap and one peak due to an extra band-edge state (Fig. 3(a)). This corresponds
 

to an anti-ferromagnetic semiconductor with spin degeneracy (the fourth kind). Three are more pairs of symmetric peaks centered about in the presence of spin splitting, as indicated in Fig. 6(j). The fifth kind of peak structure arises from narrow-gap F-absorbed ZGNRs with the spin-split anti-ferromagnetism.

On the experimental sides, STM, which can provide the spatially atomic distributions of the local nano-structures, have been successfully used to identify the unique geometric structures of the graphene-related systems, covering graphite, graphene, graphene compounds, carbon nanotubes, and GNRs. The atomic-scaled observations clearly reveal the 2D networks of local defects, \( ^{48} \)  the buckled and rippled structures of graphene islands, \( ^{49-51} \)  the adatom distributions on graphene surface, \( ^{52} \)  the nanoscale width of GNR, \( ^{53} \)  and the chiral arrangements of the hexagons on the planar edges \( ^{54} \)  and a cylindrical surface. \( ^{55} \)  As to F-absorbed GNRs, the buckled structure, the adatom height, and the bond length (Table 1) deserve further STM examinations. Such measurements are very useful in the identification of the significant orbital hybridizations related to F-C, F-F and C-C chemical bonds.

ARPES is the most powerful experimental technique to examine the wave-vector-dependent band structures. The experimental measurements on graphene-related systems have confirmed the feature-rich electronic structures under the distinct dimensions. For example, the verified energy bands include an isotropic Dirac-cone structure with linear energy dispersions in monolayer graphene, \( ^{56} \)  two pairs of parabolic bands in bilayer AB stacking, \( ^{57} \)  the bilayer- and monolayer-like energy dispersions, respectively, at  \( k_{z}=0 \)  and zone boundary in AB-stacked graphite, \( ^{58} \)  and 1D parabolic energy bands with energy gaps in AGNRs. \( ^{59} \)  In addition, an edge-localized partial flat band is deduced to be associated with the zigzag-like steps on graphite surface. \( ^{60} \)  Up to now, the ARPES measurements on the adatom-enriched unusual energy bands of GNRs are absent. The ARPES and spin-resolved ARPES \( ^{61} \)  are available in verifying the predicted five kinds of electronic structures and magnetic configurations in F-absorbed GNRs. That is to say, the complicated relations among the finite-size effects, the edge structures, the spin configurations, and the multi-orbital hybridizations.
 

could be examined by them.

The STS measurements, with the tunneling differential conductance  \( (dI/dV) \)  proportional to DOS, could serve as very efficient methods to identify the dimension-enriched special structures in DOS. They have verified the diverse electronic properties in  \( sp^{2} \) -bonding carbon-related systems. The measured DOSs show the splitting  \( \pi \)  and  \( \pi^{*} \)  peaks and a finite value near  \( E_{F} \)  characteristic of the semi-metallic behavior in graphite, \( ^{62} \)  a linear E-dependence vanishing at the Dirac point in monolayer graphene, the asymmetry-created peak structures in bilayer graphene, \( ^{63} \)  a prominent peak at  \( E_{F} \)  arising from partially flat bands in tri-layer and penta-layer ABC-stacked graphene; \( ^{64} \)  the geometry-dependent energy gaps and the asymmetric peaks of 1D parabolic bands in carbon nanotubes \( ^{65} \)  and GNRs. The STS and spin-resolved STS could be utilized to examine five kinds of low-lying DOSs in F-absorbed GNRs, covering the finite value at  \( E_{F} \) , energy gap and spin-polarized peak structures. In short, geometric structures, electronic properties and magnetic configurations are enriched by the multi-orbital hybridizations in strong chemical bondings and the spin arrangements. The interactions of atomic orbitals present  \( 2p_{x}-2p_{z} \)  and  \( (2p_{x},2p_{y})-(2p_{x},3p_{y}) \)  in C-C bonds,  \( (2p_{x},2p_{y},2p_{z})-(2p_{x},2p_{y},2p_{z}) \)  in F-C bonds, and  \( (2p_{x},2p_{y})-(2p_{x},3p_{y}) \)  in F-F bonds.

## Concluding remarks

The geometric structures, electronic and magnetic properties of F-adsorbed GNRs are investigated using the first-principles calculations. The atom-dominated band structure, the spatial charge density, the spin arrangement, and the orbital-projected DOS are useful in exploring the orbital- and spin-dependent essential properties. For example, band structure, free carrier density, magnetism and DOS are determined by which kinds of orbital hybridizations and spin configurations. The similar analyses could be further generalized to the emergent layered materials, with nanoscale thickness and unique lattice symmetries, covering silicene, germanene, tinene, phosphorene,  \( MoS_{2} \)  and so on. The fluorination-induced
 

diverse phenomena mainly arises from the complicated relations among lattice symmetry, quantum confinement, edge structure, significant chemical bonding, and spin arrangement. The metallic or semiconducting behaviors with/without magnetism indicate the highly potential applications, such as electronic, optical, and spintronic devices.

Each F-absorbed GNR presents an obvious buckling, in which the adatom height and the change of C-C bond length are mainly determined by the very strong fluorination. The multiorbital hybridizations in F-C, C-C and F-F bonds, and the edge-dependent spin distributions are responsible for five kinds of electronic and magnetic properties. The metallic behavior is revealed at certain F-distributions below 40% concentration. AGNRs could create one or two holes per unit cell, respectively, corresponding to the spin-split and spin-degenerate  \( \pi \) -electronic energy bands (non-magnetism and ferromagnetism). However, ZGNRs only exhibit the lower carrier-density case. On the other hand, the semiconducting systems could survive at various F-adsorptions except for single adatom. The  \( \pi \)  bonding predominates the essential properties, including the gap-dependent parabolic bands with spin degeneracy (non-magnetism) and partially flat bands in the absence/presence of spin splitting (antiferromagnetism). Under high adatom concentrations, non-magnetic parabolic bands, with an energy gap are determined by the  \( (2p_{x}, 2p_{y}) \)  orbitals of F and C. The 1D energy dispersions are reflected in DOS as many anti-symmetric and symmetric peaks. There exist five kinds of low-lying peak structures characteristic of the main features of essential properties. The predicted geometric structures, energy bands and DOSs, could be verified by STM, ARPES and STS, respectively, especially for the latter two tools with spin resolution.
 

## Acknowledgments

This work was supported by the Physics Division, National Center for Theoretical Sciences (South), the Nation Science Council of Taiwan. We also thank the National Center for High-performance Computing (NCHC) for computer facilities.
 

## References

(1) Novoselov, K. S; Geim, A. K; Morozov, S. V; Jiang, D; Zhang, Y; Dubonos, S. V; Firsov, A. A. Electric field effect in atomically thin carbon films. Science 2004, 306, 666-669.

(2) Zhang, Y; Tan, Y. W; Stormer, H. L; Kim, P. Experimental observation of the quantum Hall effect and Berry’s phase in graphene. Nature 2005, 438, 201-204.

(3) Duplock, E. J; Scheffler, M; Lindan, P. J. Hallmark of perfect graphene. Physical Review Letters 2004, 92, 225502.

(4) Jiao, L; Wang, X; Diankov, G; Wang, H; Dai, H. Facile synthesis of high-quality graphene nanoribbons. Nature nanotechnology 2010, 5, 321-325.

(5) Kosynkin, D. V; Higginbotham, A. L; Sinitskii, A; Lomeda, J. R; Dimiev, A; Price, B. K; Tour, J. M. Longitudinal unzipping of carbon nanotubes to form graphene nanoribbons. Nature 2009, 458, 872-876.

(6) Talirz, L; Söde, H; Cai, J; Ruffieux, P; Blankenburg, S; Jafaaar, R; Fasel, R. Termini of bottom-up fabricated graphene nanoribbons. Journal of the American Chemical Society 2013, 135, 2060-2063.

(7) Han, M. Y; Özyılmaz, B; Zhang, Y; Kim, P. Energy band-gap engineering of graphene nanoribbons. Physical review letters 2007, 98, 206805.

(8) Chen, Z; Lin, Y. M; Rooks, M. J; Avouris, P. Graphene nano-ribbon electronics. Physica E: Low-dimensional Systems and Nanostructures 2007, 40, 228-232.

(9) Li, X; Wang, X; Zhang, L; Lee, S; Dai, H. Chemically derived, ultrasmooth graphene nanoribbon semiconductors. Science 2008, 319, 1229-1232.

(10) Datta, S. S; Strachan, D. R; Khamis, S. M; Johnson, A. C. Crystallographic etching of few-layer graphene. Nano letters 2008, 8, 1912-1915.
 

(11) Elias, A. L; Botello-Mendez, A. R; Meneses-Rodriguez, D; Jehova Gonzalez, V; Ramirez-Gonzalez, D; Ci, L; Terrones, M. Longitudinal cutting of pure and doped carbon nanotubes to form graphitic nanoribbons using metal clusters as nanoscalepels. Nano letters 2009, 10, 366-372.

(12) Kosynkin, D. V; Higginbotham, A. L; Sinitskii, A; Lomeda, J. R; Dimiev, A; Price, B. K; Tour, J. M. Longitudinal unzipping of carbon nanotubes to form graphene nanoribbons. Nature 2009, 458, 872-876.

(13) Campos-Delgado, J; Romo-Herrera, J. M; Jia, X; Cullen, D. A; Muramatsu, H; Kim, Y. A; Ohba, T. Bulk production of a new form of  \( sp^{2} \)  carbon: crystalline graphene nanoribbons. Nano letters 2008, 8, 2773-2778.

(14) Barone, V; Hod, O; Scuseria, G. E. Electronic structure and stability of semiconducting graphene nanoribbons. Nano letters 2006, 6, 2748-2754.

(15) Yan, Q; Huang, B; Yu, J; Zheng, F; Zang, J; Wu, J; Duan, W. Intrinsic current-voltage characteristics of graphene nanoribbon transistors and effect of edge doping. Nano letters 2007, 7, 1469-1473.

(16) Pak, Y; Kim, S. M; Jeong, H; Kang, C. G; Park, J. S; Song, H; Kim, J. T. Palladium-decorated hydrogen-gas sensors using periodically aligned graphene nanoribbons. ACS applied materials and interfaces 2014, 6, 13293-13298.

(17) Rafiee, M. A; Lu, W; Thomas, A. V; Zandiatashbar, A; Rafiee, J; Tour, J. M; Koratkar, N. A. Graphene nanoribbon composites. ACS nano 2010, 4, 7415-7420.

(18) Li, Y; Zhou, Z; Shen, P; Chen, Z. Spin gapless semiconductor-metal-half-metal properties in nitrogen-doped zigzag graphene nanoribbons. ACS Nano 2009, 3, 1952-1958.

(19) Chang, C. P; Wu, B. R; Chen, R. B; Lin, M. F. Deformation effect on electronic
 

and optical properties of nanographite ribbons. Journal of applied physics 2007, 101, 063506.

(20) Lin, S. Y; Chang, S. L; Shyu, F. L; Lu, J. M; Lin, M. F. Feature-rich electronic properties in graphene ripples. Carbon 2015, 86, 207-216.

(21) Huang, Y. C; Chang, C. P; Lin, M. F. Magnetoabsorption spectra of bilayer graphene ribbons with Bernal stacking. Physical Review B 2008, 78, 115422.

(22) Lin, C. Y; Wu, J. Y; Ou, Y. J; Chiu, Y. H; Lin, M. F. Magneto-electronic properties of multilayer graphenes. Physical Chemistry Chemical Physics 2015, 17, 26008-26035.

(23) Chang, S. L; Lin, S. Y; Lin, S. K; Lee, C. H; Lin, M. F. Geometric and electronic properties of edge-decorated graphene nanoribbons. Scientific reports 2014, 4, 6038.

(24) Lin, Y. T; Chung, H. C; Yang, P. H; Lin, S. Y; Lin, M. F. Adatom bond-induced geometric and electronic properties of passivated armchair graphene nanoribbons. Physical Chemistry Chemical Physics 2015, 17, 16545-16552.

(25) Sadeghi, H; Ahmadi, M. T; Mousavi, S. M; Ismail, R; Ghadiry, M. H. Channel conductance of ABA stacking trilayer graphene nanoribbon field-effect transistor. Modern Physics Letters B 2012, 26, 1250047.

(26) Chang, C. P; Huang, Y. C; Lu, C. L; Ho, J. H; Li, T. S; Lin, M. F. Electronic and optical properties of a nanographite ribbon in an electric field. Carbon 2006, 44, 508-515.

(27) Kan, E. J; Li, Z; Yang, J; Hou, J. G. Will zigzag graphene nanoribbon turn to half metal under electric field? Applied physics letters 2007, 91, 243116.

(28) Lin, M. F; Shyu, F. L. Optical properties of nanographite ribbons. Journal of the Physical Society of Japan 2000, 69, 3529-3532.
 

(29) Huang, Y. C; Chang, C. P; Lin, M. F. Magnetic and quantum confinement effects on electronic and optical properties of graphene ribbons. Nanotechnology 2007, 18, 495401.

(30) Han, M. Y; Brant, J. C; Kim, P. Electron transport in disordered graphene nanoribbons. Physical review letters 2010, 104, 056801.

(31) Yang, Y; Murali, R. Impact of size effect on graphene nanoribbon transport. IEEE Electron Device Letters 2010, 31, 237-239.

(32) Son, Y. W; Cohen, M. L; Louie, S. G. Energy gaps in graphene nanoribbons. Physical review letters, 2006, 97, 216803.

(33) Wang, Z; Xiao, J; Li, M. Adsorption of transition metal atoms (Co and Ni) on zigzag graphene nanoribbon. Applied Physics A 2013, 110, 235-239.

(34) Krepel, D; Hod, O. Lithium adsorption on armchair graphene nanoribbons. Surface Science 2011, 605, 1633-1642.

(35) da Rocha, C. G; Clayborne, P. A; Koskinen, P; Häkkinen, H. Optical and electronic properties of graphene nanoribbons upon adsorption of ligand-protected aluminum clusters. Physical Chemistry Chemical Physics 2014, 16, 3558-3565.

(36) Huang, B; Li, Z; Liu, Z; Zhou, G; Hao, S; Wu, J; Duan, W. Adsorption of gas molecules on graphene nanoribbons and its implication for nanoscale molecule sensor. The Journal of Physical Chemistry C 2008, 112, 13442-13446.

(37) Johnson, J. L; Behnam, A; Pearton, S. J; Ural, A. Hydrogen Sensing Using Pd Functionalized Multi Layer Graphene Nanoribbon Networks. Advanced Materials 2010, 22, 4877-4880.

(38) Lin, J; Peng, Z; Xiang, C; Ruan, G; Yan, Z; Natelson, D; Tour, J. M. Graphene
 

nanoribbon and nanostructured  \( SnO_{2} \)  composite anodes for lithium ion batteries. ACS nano 2013, 7, 6001-6006.

(39) Yazyev, O. V. A guide to the design of electronic properties of graphene nanoribbons. Accounts of chemical research 2013, 46, 2319-2328.

(40) Binnig, G; Rohrer, H. Scanning tunneling microscopy. Surface science 1983, 126, 236-244.

(41) Gray, A. X; Papp, C; Ueda, S; Balke, B; Yamashita, Y; Plucinski, L; Pickett, W. E. Probing bulk electronic structure with hard X-ray angle-resolved photoemission. Nature Materials 2011, 10, 759-764.

(42) Söde, H; Talirz, L; Gröning, O; Pignedoli, C. A; Berger, R; Feng, X; Ruffieux, P. Electronic band dispersion of graphene nanoribbons via Fourier-transformed scanning tunneling spectroscopy. Physical Review B 2015, 91, 045429.

(43) Kresse, G; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Physical review B 1996, 54, 11169.

(44) Perdew, J. P; Burke, K; Ernzerhof, M. Generalized gradient approximation made simple. Physical review letters 1996, 77, 3865.

(45) Blöchl, P. E. Projector augmented-wave method. Physical review B 1994, 50, 17953.

(46) Lin, Y. T; Lin, S. Y; Chiu, Y. H; Lin, M. F. Alkali-induced rich properties in graphene nanoribbons: Chemical bonding. arXiv preprint arXiv:1609.05562(2016).

(47) Son, Y. W; Cohen, M. L; Louie, S. G. Energy gaps in graphene nanoribbons. Physical review letters 2006, 97, 216803.

(48) Cervenka, J; Katsnelson, M. I; Flipse, C. F. J. Room-temperature ferromagnetism in graphite driven by two-dimensional networks of point defects. Nature Physics 2009, 5, 840-844.
 

(49) Meng, L; He, W. Y; Zheng, H; Liu, M; Yan, H; Yan, W; Liu, Z. Strain-induced one-dimensional Landau level quantization in corrugated graphene. Physical Review B 2013, 87, 205405.

(50) Bai, K. K; Zhou, Y; Zheng, H; Meng, L; Peng, H; Liu, Z; He, L. Creating one-dimensional nanoscale periodic ripples in a continuous mosaic graphene monolayer. Physical review letters 2014, 113, 086102.

(51) De Parga, A. V; Calleja, F; Borca, B. M. C. G; Passeggi Jr, M. C. G.; Hinarejos, J. J; Guinea, F; Miranda, R. Periodically rippled graphene: growth and spatially resolved electronic structure. Physical review letters 2008, 100, 056807.

(52) Pandey, D; Reifenberger, R; Piner, R. Scanning probe microscopy study of exfoliated oxidized graphene sheets. Surface Science 2008, 602, 1607-1613.

(53) Ruffieux, P; Cai, J; Plumb, N. C; Patthey, L; Prezzi, D; Ferretti, A; Fasel, R. Electronic structure of atomically precise graphene nanoribbons. ACS Nano 2012, 6, 6930-6935.

(54) Tao, C; Jiao, L; Yazyev, O. V; Chen, Y. C; Feng, J; Zhang, X; Dai, H. Spatially resolving edge states of chiral graphene nanoribbons. Nature Physics 2011, 7, 616-620.

(55) Wilder, J. W; Venema, L. C; Rinzler, A. G; Smalley, R. E; Dekker, C. Electronic structure of atomically resolved carbon nanotubes. Nature 1998, 391, 59-62.

(56) Ohta, T; Bostwick, A; McChesney, J. L; Seyller, T; Horn, K; Rotenberg, E. Interlayer interaction and electronic screening in multilayer graphene investigated with angle-resolved photoemission spectroscopy. Physical Review Letters 2007, 98, 206802.

(57) Ohta, T; Bostwick, A; Seyller, T; Horn, K; Rotenberg, E. Controlling the electronic structure of bilayer graphene. Science 2006, 313, 951-954.

(58) Grüneis, A; Attaccalite, C; Pichler, T; Zabolotnyy, V; Shiozawa, H; Molodtsov, S. L;
 

Follath, R. Electron-electron correlation in graphite: a combined angle-resolved photoemission and first-principles study. Physical review letters 2008, 100, 037601.

(59) Ruffieux, P; Cai, J; Plumb, N. C; Patthey, L; Prezzi, D; Ferretti, A; Fasel, R. Electronic structure of atomically precise graphene nanoribbons. ACS Nano 2012, 6, 6930-6935.

(60) Sugawara, K; Sato, T; Souma, S; Takahashi, T; Suematsu, H. Fermi surface and edge-localized states in graphite studied by high-resolution angle-resolved photoemission spectroscopy. Physical Review B, 2006, 73, 045124.

(61) Usachov, D; Fedorov, A; Otrokov, M. M; Chikina, A; Vilkov, O; Petukhov, A; Grüneis, A. Observation of single-spin dirac fermions at the graphene/ferromagnet interface. Nano Letters 2015, 15, 2396-2401.

(62) Klusek, Z. Investigations of splitting of the  \( \pi \)  bands in graphite by scanning tunneling spectroscopy. Applied surface science 1999, 151, 251-261.

(63) Luican, A; Li, G; Reina, A; Kong, J; Nair, R. R; Novoselov, K. S; Andrei, E. Y. Single-layer behavior and its breakdown in twisted graphene layers. Physical review letters 2011, 106, 126802.

(64) Que, Y; Xiao, W; Chen, H; Wang, D; Du, S; Gao, H. J. Stacking-dependent electronic property of trilayer graphene epitaxially grown on Ru (0001). Applied Physics Letters 2015, 107, 263101.

(65) Odom, T. W; Huang, J. L; Kim, P; Lieber, C. M. Atomic structure and electronic properties of single-walled carbon nanotubes. Nature 1998, 391, 62-64.
 

Table 1: Ground state energy, magnetic moment and magnetism, energy gap, free holes in a unit cell, and geometric parameters for  \( N_{A} = 12 \)  armchair and  \( N_{Z} = 8 \)  zigzag GNRs under single- and double-side fluorinations. NM, FM and AFM, respectively, correspond to non-magnetism, ferro-magnetism and anti-ferro-magnetism.

<table><tr><td>GNRs</td><td>Adsorption configurations</td><td>E0(eV)</td><td>Magnetic moment (μB)/magnetism</td><td>Ed(i)(eV)/Metal</td><td>Number of holes</td><td>F-C(Å)</td><td>C height(Å)</td><td>Nearest C-C(Å)</td></tr><tr><td rowspan="22">AGNRNA=12</td><td>Pristine(13)s</td><td>-234.7419-237.0912</td><td>0/NM0/NM</td><td>Edg=0.60</td><td>01</td><td>0.1547</td><td>0.053</td><td>1.4281.483</td></tr><tr><td>(1)s</td><td>-237.4201</td><td>0.47/FM</td><td>M</td><td>1</td><td>1.471</td><td>0.133</td><td>1.489</td></tr><tr><td>(6,21)s</td><td>-239.4138</td><td>0/NM</td><td>M</td><td>2</td><td>1.545</td><td>0.055</td><td>1.491</td></tr><tr><td>(6,21)d</td><td>-239.4261</td><td>0/NM</td><td>M</td><td>2</td><td>1.546</td><td>0.054</td><td>1.491</td></tr><tr><td>(1,23)s</td><td>-240.4703</td><td>0.76/FM</td><td>M</td><td>1</td><td>1.468</td><td>0.132</td><td>1.488</td></tr><tr><td>(1,23)d</td><td>-240.4839</td><td>0.76/FM</td><td>M</td><td>1</td><td>1.469</td><td>0.131</td><td>1.488</td></tr><tr><td>(1,6)d</td><td>-241.0514</td><td>0/NM</td><td>Eg=0.64</td><td>0</td><td>1.443</td><td>0.161</td><td>1.493</td></tr><tr><td>(6,9,14,17)d</td><td>-245.3591</td><td>0/NM</td><td>M</td><td>2</td><td>1.503</td><td>0.097</td><td>1.497</td></tr><tr><td>(2,9,18,23)d</td><td>-245.8006</td><td>0.56/FM</td><td>M</td><td>1</td><td>1.454</td><td>0.15</td><td>1.491</td></tr><tr><td>(1,2,23,24)d</td><td>-250.2258</td><td>0/NM</td><td>Eg=0.98</td><td>0</td><td>1.43</td><td>0.17</td><td>1.496</td></tr><tr><td>(C:F=24:6)d</td><td>-250.4901</td><td>0/NM</td><td>M</td><td>2</td><td>1.532</td><td>0.068</td><td>1.497</td></tr><tr><td>(C:F=24:6)d</td><td>-251.897</td><td>0.57/FM</td><td>M</td><td>1</td><td>1.443</td><td>0.161</td><td>1.493</td></tr><tr><td>(C:F=24:6)d</td><td>-255.5256</td><td>0/NM</td><td>Eg=0.85</td><td>0</td><td>1.414</td><td>0.186</td><td>1.506</td></tr><tr><td>(C:F=24:8)d</td><td>-258.6336</td><td>0/NM</td><td>M</td><td>2</td><td>1.446</td><td>0.154</td><td>1.503</td></tr><tr><td>(C:F=24:8)d</td><td>-257.9218</td><td>0.59/FM</td><td>M</td><td>1</td><td>1.473</td><td>0.127</td><td>1.498</td></tr><tr><td>(C:F=24:8)d</td><td>-261.6414</td><td>0/NM</td><td>Eg=0.12</td><td>0</td><td>1.416</td><td>0.184</td><td>1.506</td></tr><tr><td>(C:F=24:10)d</td><td>-268.196</td><td>0/NM</td><td>Eg=0.56</td><td>0</td><td>1.416</td><td>0.184</td><td>1.507</td></tr><tr><td>(C:F=24:14)d</td><td>-283.013</td><td>0/NM</td><td>Eg=2.25</td><td>0</td><td>1.413</td><td>0.187</td><td>1.53</td></tr><tr><td>(C:F=24:20)d</td><td>-303.9926</td><td>0/NM</td><td>Eg=2.69</td><td>0</td><td>1.408</td><td>0.192</td><td>1.505</td></tr><tr><td>(C:F=24:24)d</td><td>-319.2921</td><td>0/NM</td><td>Eg=3.2</td><td>0</td><td>1.395</td><td>0.205</td><td>1.544</td></tr><tr><td rowspan="8">ZGNRNZZ=8</td><td>Pristine(3)s</td><td>-308.0119</td><td>0/AFM</td><td>Edg=0.46</td><td>0</td><td>0</td><td>1.428</td><td>1.485</td></tr><tr><td>(13)s</td><td>-311.9155</td><td>0.42/FM</td><td>M</td><td>1</td><td>1.462</td><td>0.138</td><td>1.481</td></tr><tr><td>(3,14)d</td><td>-310.4937</td><td>0.4/FM</td><td>M</td><td>1</td><td>1.55</td><td>0.05</td><td>1.481</td></tr><tr><td>(3,6)d</td><td>-314.6181</td><td>0.37/FM</td><td>M</td><td>1</td><td>1.45</td><td>0.15</td><td>1.488</td></tr><tr><td>(11,14)d</td><td>-314.8808</td><td>0.37/FM</td><td>M</td><td>1</td><td>1.432</td><td>0.168</td><td>1.492</td></tr><tr><td>(19,22)d</td><td>-313.5967</td><td>0/AFM</td><td>Eg=0.2</td><td>0</td><td>1.501</td><td>0.099</td><td>1.494</td></tr><tr><td>(3,30)s</td><td>-313.3396</td><td>0/AFM</td><td>Eg=0.2</td><td>0</td><td>1.504</td><td>0.096</td><td>1.486</td></tr><tr><td>(3,30)d</td><td>-315.9246</td><td>0/NM</td><td>Edg=0.46</td><td>0</td><td>1.454</td><td>0.146</td><td>1.487</td></tr><tr><td></td><td>(C:F=32:32)d</td><td>-420.1127</td><td>0/NM</td><td>Edg=0.46</td><td>0</td><td>1.455</td><td>0.145</td><td>1.487</td></tr></table>
 

(a)  \( N_{A}=12 \)  AGNR

![](./images/867774263942185065_1.jpg)

Figure 1: Geometric structures of F-adsorbed GNRs for (a)  \( N_{A} = 12 \)  armchair and (b)  \( N_{Z} = 8 \)  zigzag systems. The black rectangles represent unit cells. The lattice constants are, respectively, a = 3b and  \( a = 2\sqrt{3}b \)  for armchair and zigzag GNRs. Numbers on the top of carbons denote the positions of adatoms.
 
![](./images/867774263942185065_2.jpg)

 
![](./images/867774263942185065_3.jpg)

Figure 2: Band structures of  \( N_{A}=12 \)  AGNR for (a) pristine, (b) (13)s, (c) (1)s, (d) (6,21)s, (e) (6,21)d, (f) (1,6)d, (g) (1,23)s, (h) (1,23)d, (i) (8F)d, (j) (10F)d, (k) (20F)d, & (l) (24F)d; Blue circles represent the contribution of F adatoms. The red and black curves denote the spin-split energy bands.
 
![](./images/867774263942185065_4.jpg)

![](./images/867774263942185065_5.jpg)

![](./images/867774263942185065_6.jpg)

![](./images/867774263942185065_7.jpg)

![](./images/867774263942185065_8.jpg)

![](./images/867774263942185065_9.jpg)

![](./images/867774263942185065_10.jpg)

![](./images/867774263942185065_11.jpg)

![](./images/867774263942185065_12.jpg)

![](./images/867774263942185065_13.jpg)

Figure 3: Band structures of  \( N_{Z}=8 \)  ZGNR for (a) pristine ZGNR, (b)  \( (3)_{s} \) , (c)  \( (3,30)_{s} \) ,  \( (d) \)   \( (3,30)_{d} \) , (e)  \( (11,14)_{d} \) , & (f)  \( (3,14)_{d} \( ; Blue circles represent the contribution of F adatoms. The red and black curves denote the spin-split energy bands.
 
![](./images/867774263942185065_14.jpg)

Figure 4: Spin density of  \( N_{A} = 12 \)  AGNR for (a)  \( (1)_{s} \) , (b)  \( (1, 23)_{s} \) ,  \( (c) \)   \( (1, 23)_{d} \) , and  \( N_{Z} = 8 \)  ZGNR for (d)  \( (3)_{s} \) , (e) pristine, and (f)  \( (11, 14)_{d} \) .
 
![](./images/867774263942185065_15.jpg)

Figure 5: Spatial charge density of  \( N_{A} = 12 \)  AGNR for (a) Pristine, (b)  \( (13)_{s} \) , & (d)  \( (24F)_{d} \) ; charge density difference for (c)  \( (13)_{s} \) , (e)  \( (24F)_{d} \) . Partial charge density is shown for (f)  \( \mathrm{AGNR}-(6,21)_{d} \) , (g)  \( \mathrm{ZGNR}-(3,14)_{d} \) , (h)  \( \mathrm{AGNR}-(1,6)_{d} \) , and (i)  \( \mathrm{ZGNR}-(11,14)_{d} \) .
 
![](./images/867774263942185065_16.jpg)

Figure 6: Orbital-projected DOSs for (a) Pristine, (b)  \( (10\mathrm{F})_{d^{-}} \) , (c)  \( (20\mathrm{F})_{d^{- }} \) , (d)  \( (24\mathrm{F})_{d^{-}} \) , (e)  \( (13)_{s^{-}} \) , (f)  \( (6,21)_{d^{-}} \) , (g)  \( (1,23)_{d^{-}} \) adsorbed  \( N_{A}=12 \)  AGNR; (h)  \( (3,14)_{d^{-}} \) , (i) pristine; (j)  \( (11,14)_{d^{-}} \) adsorbed  \( N_{Z}=8 \)  ZGNR. Blue triangles correspond to the partially flat bands.
 
