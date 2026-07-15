
# Spin-state transition and spin-polaron physics in cobalt oxide perovskites: ab initio approach based on quantum chemical methods

L. Hozoi, \( ^{1} \)  U. Birkenheuer, \( ^{1,2} \)  H. Stoll, \( ^{3} \)  and P. Fulde \( ^{1} \) 

 \( ^{1} \) Max-Planck-Institut für Physik komplexer Systeme, Nöthnitzer Str. 38, 01187 Dresden, Germany  
 \( ^{2} \) Forschungszentrum Dresden-Rossendorf, Bautzner Landstr. 128, 01328 Dresden, Germany  
 \( ^{3} \) Universität Stuttgart, Pfaffenwaldring 55, 70550 Stuttgart, Germany  
(Dated: October 26, 2018)

A fully ab initio scheme based on quantum chemical wavefunction methods is used to investigate the correlated multiorbital electronic structure of a 3d-metal compound,  \( LaCoO_{3} \) . The strong short-range electron correlations, involving both Co and O orbitals, are treated by multiferrence techniques. The use of effective parameters like the Hubbard  \( U \)  and interorbital  \( U' \) , J terms and the problems associated with their explicit calculation are avoided with this approach. We provide new insight into the spin-state transition at about 90 K and the nature of charge carriers in the doped material. Our results indicate the formation of a  \( t_{2g}^{4}e_{g}^{2} \)  high-spin state in  \( LaCoO_{3} \)  for  \( T \gtrsim 90 K \) . Additionally, we explain the paramagnetic phase in the low-temperature lightly doped compound through the formation of Zhang-Rice-like O hole states and ferromagnetic clusters.

An accurate description of correlated electrons is one of the central problems of condensed-matter theory. The commonly used approach for the computation of electronic structures is based on density-functional theory and various approximations to it, the most applied being the local density approximation (LDA). This approach has led to unprecedented progress in computational condensed-matter physics and surprisingly good results for numerous compounds. However, it is also known and well documented that the LDA has problems with describing strongly correlated systems which usually involve d and f electrons. For that reason extensions like the LDA+U \( ^{[1]} \)  and LDA plus dynamical mean-field theory (LDA+DMFT) \( ^{[2]} \)  were developed. In the latter approaches, the strong local correlations are described by effective interactions such as the Hubbard U, an interorbital Coulomb repulsion  \( U' \) , and an on-site exchange coupling J. Even so, the correlation treatment is limited to on-site effects, despite of the fact that intersite correlations are known to be sizeable. To deal with the latter, the LDA+DMFT scheme has been generalized to a cluster LDA+DMFT \( ^{[2,3]} \) . But a self-consistent computation of the Coulomb repulsion parameters U,  \( U' \)  (and intersite V) is in this context particularly difficult \( ^{[4]} \) . It is fair to state that the main virtue of LDA, namely its simplicity, has got more and more lost.

This suggests the use of a different approach, based on the computation of many-body wavefunctions  \( [5] \)  by means of quantum chemical techniques  \( [6] \) . It has the advantage that all approximations are well controlled and that it is not necessary to introduce effective interactions like  \( U, U' \)  or J. Here, we demonstrate this for the case of a 3d oxide compound,  \( LaCoO_{3} \) . Our analysis is based on a local Hamiltonian approach  \( [7, 8, 9, 10] \)  and performed on large fragments including several  \( CoO_{6} \)  octahedra. Localized Wannier functions and embedding potentials are obtained for these fragments from prior periodic Hartree-Fock (HF) calculations for the infinite crystal  \( [10, 11] \) . Since our scheme is parameter-free, variational, and multiconfigurational (or multiferrence, see below), it has great predictive power. It can, for example, predict the basic ingredients required in effective impurity models like DMFT. For late transition-metal (TM) oxides, in particular, it is important to anticipate whether (and which of) the TM d orbitals are sufficient for constructing a minimal effective orbital space or whether both TM d and oxygen p functions must be considered as active. That such questions can be reliably addressed with quantum chemical methods was shown before for the layered copper oxides  \( [12] \)  and ladder vanadates  \( [13] \) . However, simple point-charge embeddings were used in previous work for representing the surroundings of the region where the correlation treatment is carried out. A newly developed, rigorous embedding technique  \( [10, 11] \)  is applied here for the first time to a 3d-metal compound.

LaCoO \( _{3} \)  has attracted considerable attention due to a number of puzzling phase transitions induced by changes in temperature [14, 15], doping [15, 16], and/or strain [17, 18]. Up to now, most of the experimental work was aimed at understanding the nature of the phase transitions in the undoped compound, from a nonmagnetic insulator at low T to a paramagnetic semiconductor above 90 K and to a metal for T > 500 K. The low-T ground-state was assigned to a closed-shell  \( t_{2g}^{6}e_{g}^{0} \)  configuration [low-spin (LS), S = 0] of the Co ions [14]. For  \( T \gtrsim 90 \)  K, however, the available experimental results are rather contradictory. While recent x-ray absorption spectroscopy (XAS) [19] and inelastic neutron scattering (INS) [20] measurements indicate with increasing T a gradual transition into a  \( S = 2 \)  ( \( t_{2g}^{4}e_{g}^{2} \) ) high-spin (HS) configuration of the Co 3d electrons, electron energy-loss spectroscopy data [21] and the observation of Co-O bond-length alternation [22] suggest the formation of a S = 1 ( \( t_{2g}^{5}e_{g}^{1} \) ) intermediate-spin (IS) state for T > 90 K, susceptible to Jahn-Teller distortions. On the theoretical side, the transition to a HS state around 90 K is favored by
 

many-body model Hamiltonian calculations [19]. The IS electron configuration is supported by LDA+U calculations [21, 23]. A wavefunction-based quantum chemical analysis is not available yet for this system.

The first step in our investigation is an ab initio closed-shell restricted HF (RHF) calculation for the periodic solid. The crystal code  \( [24] \)  is employed for this purpose. We use all-electron Gaussian-type basis sets of triple-zeta quality  \( [25] \)  and a cubic perovskite crystal structure. The Co-O distance is taken to be d = 1.92 Å, as reported for low T in ref.  \( [28] \) . It is well-known that the HF approximation strongly overestimates the fundamental band gap in insulators. For  \( LaCoO_{3} \) , the RHF gap is 13.3 eV, where the upper valence bands have O 2p character and the lowest conduction bands are related to the Co 3d- \( e_{g} \)  levels. On-site and intersite correlation effects are here investigated in direct space by multiconfiguration complete-active-space self-consistent-field (CASSCF) and multiferrence configuration-interaction (MRCI) calculations  \( [6] \) . The orbital basis entering the correlation treatment is provided by the localization module of the crystal program. These functions are the Wannier orbitals (WO's) associated with the RHF bands  \( [29] \) . The CASSCF and MRCI calculations are carried out with the MOLPRO quantum chemical package  \( [30] \) .

Several sites are included in the correlation treatment. These sites are partitioned into two groups: an "active" region  \( C_{A} \) , which here consists of one  \( CoO_{6} \)  octahedron, and a "buffer" zone  \( C_{B} \) , including the Co and all other O ions of the six nearest-neighbor (NN) octahedra (i.e., 6 Co and 30 O ions) plus the La NN's of the "active" octahedron (8 La sites) [31]. The role of the buffer zone  \( C_{B} \)  is to ensure an accurate representation of the tails of the WO's centered in the active region  \( C_{A} \) . While the occupied orbitals in the buffer zone are frozen, orbitals centered at sites in the  \( C_{A} \)  region (and their tails in  \( C_{B} \) ) are allowed to relax and polarize in the quantum chemical calculation. We denote  \( C_{A} + C_{B} \)  as C. The sur-

![](./images/867748218761380627_1.jpg)

FIG. 1: Diagram for the lowest N (left) and  \( (N-1) \)  (right) particle states. The MRCI treatment is based on a cas-7 reference, see text. Only the Co 3d and O  \( 2p-e_{g} \)  electrons are correlated in the MRCI-7 calculations. For MRCI-11, the Co 3s, 3p electrons are also included. The reference is in each graph the energy of the MRCI-11 LS state.

roundings of this group of ions (i.e., the crystalline environment) are modelled as an effective one-electron potential. This is obtained from the periodic RHF calculation and incorporated in the one-electron Hamiltonian in the CASSCF/MRCI treatment via the CRYSTAL-MOLPRO interface program  \( [10, 11] \) . A ground-state closed-shell self-consistent-field calculation for C leads to changes of only few meV ( \( \approx 3 \)  meV) in the total energy, which shows that our embedding potential was properly constructed and the projection of the original crystal WO's centered at sites of the  \( C_{A} \)  region onto the set of basis functions associated with  \( C = C_{A} + C_{B} \)  [32] leads to insignificant changes of the longer-range "tails".

The low-temperature  \( (T\ll90\;\mathrm{K}) \)  ground-state configuration and the nature of the lowest N-particle excited states are first studied at the CASSCF level. In CASSCF, a number of active electrons is allowed to be distributed in all possible ways over a given number of active orbitals. Both the orbitals and the coefficients in the multiconfiguration expansion are optimized [6]. In the case of a single  \( Co^{3+} \)  ion, a minimal active space is constructed with six electrons and five 3d orbitals, which we denote as cas-5. Intriguingly, for such a minimal active space, CASSCF predicts a  \( HS t_{2g}^{4} e_{g}^{2} \)  ( \( ^{5}T_{2g} \) ) ground-state configuration. The LS state,  \( t_{2g}^{6} e_{g}^{0} \)  ( \( ^{1}A_{g} \) ), is 1.26 eV higher in energy. The IS state,  \( t_{2g}^{5} e_{g}^{1} \)  ( \( ^{3}T_{1g} \) ), is 0.21 eV above the LS state, see Fig. 1. Clearly, the minimal orbital space description is insufficient for this system.

A first guess is that the active space must be enlarged with O 2p orbitals. Indeed, the RHF band structure, with the O 2p bands located above the Co  \( t_{2g} \)  levels, see above, suggests that O 2p to Co 3d charge-transfer (CT) effects are important. The two  \( \sigma \) -like  \( e_{g} \)  combinations of 2p orbitals at the NN O sites have the largest overlap with the Co 3d functions. When these two combinations of  \( e_{g} \)  symmetry are added to the active space, which we denote as the cas-7 orbital space, the CASSCF HS-LS splitting is reduced by 0.39 eV, to 0.87 eV. This is related to the strong interaction between the “non-CT”  \( t_{2g}^{6}e_{g}^{0} \)  and the O  \( 2p-e_{g} \)  to Co 3d- \( e_{g} \)  CT configurations in the LS CASSCF wavefunction. However, the HS state is still the lowest, see Fig. 1. Other types of charge fluctuations are taken into account by MRCI calculations. In a first step, we account for all single and double excitations from the Co 3d and O  \( 2p-e_{g} \)  orbitals. The reference is the cas-7 wavefunction. The HS-LS splitting is now reduced by an additional 0.69 eV, with the HS state remaining the ground-state. A switch in the energy order of these two states is only obtained when accounting for correlation effects (single and double excitations in the MRCI treatment) which involve the semi-core Co 3s, 3p electrons. These correlations are mainly related to the coupling between the O  \( 2p-e_{g} \)  to Co 3d- \( e_{g} \)  CT, on-site Co 3s, 3p → 3d, 4s, 4p, and Co 3d → 4s,  \( 4p \)  excitations. For such MRCI wavefunctions [34], the LS state is found indeed to be the lowest and the first N-particle excited
 

state is the HS state, with an excitation energy of 6 meV ( \( \approx 70 \)  K, not visible in Fig. 1).

We thus find that the HS state is lower in energy than the IS arrangement. For an undistorted lattice, this energy difference is 0.60 eV. Additionaly, the quantum chemical calculations provide unique, detailed information about the importance of different types of correlation effects. The good agreement between the LS-HS splitting and the temperature where the magnetic phase transition occurs (70 vs. 90-100 K) is remarkable. One should, however, realize that inclusion of other excitation processes and larger basis sets would modify quantitatively this splitting, although we expect that the order of the two states would not change [35].

We now proceed with the analysis of the lowest electron-removal and electron-addition states. It was argued that the largest interaction with the  \( 2p \rightarrow 3d \)  CT configurations and the strongest stabilization effects occur for the  \( t_{2g}^{4}e_{g}^{1} \)  IS hole state [36]. Therefore, the lowest  \( (N-1) \)  states are often associated with an  \( IS, t_{2g}^{4}e_{g}^{1}(^{4}T_{1g}) \) , configuration of the Co ions. Our calculations show that the lowest-energy hole states are related to the  \( LS, t_{2g}^{5}e_{g}^{0}(^{2}T_{2g}) \) , configuration. Even by CASSCF, with a cas-7 active space, the  \( LS t_{2g}^{5}e_{g}^{0} \)  hole state is about half eV lower than the IS  \( (N-1) \)  state. MRCI calculations which include the Co 3s, 3p electrons yield an even a larger splitting of 0.85 eV, see Fig. 1. The implication is that the strongest CT effects occur for reference configurations with completely empty 3d- \( e_{g} \)  levels, as also found in the N-electron system.

The lowest hole states in  \( LaCoO_{3} \)  have strong O 2p character and resemble the lowest  \( (N-1) \)  state in cuprates [37]. In cuprates, the dominant contribution to the ionized state is a superposition of two configurations,  \( \left|t_{2g}^{5}d_{z^{2}}^{2}b^{2}a^{0}\right\rangle \)  and  \( \left|t_{2g}^{6}d_{z^{2}}^{2}b^{0}a^{2}\right\rangle \) , where b and a are bonding and antibonding combinations of the O  \( 2p_{\sigma} \)  and Cu 3d orbitals of  \( (x^{2}-y^{2}) \)  symmetry on one  \( CuO_{4} \)  plaquette. In the CASSCF wavefunction [12], the Cu 3d and O  \( 2p_{\sigma} \)   \( (x^{2}-y^{2}) \)  orbitals contribute with nearly equal weight to b and a. The added hole has therefore predominant O 2p character [12]. For cubic perovskites, the two 3d- \( e_{g} \)  components are degenerate. The dominant contributions to the first ionized state in  \( LaCoO_{3} \)  imply then three configurations:  \( \left|t_{2g}^{5}b_{x^{2}-y^{2}}^{2}b_{z^{2}a^{0}}^{2}x_{z^{2}-y^{2}}^{0}a_{z^{2}}^{0}\right\rangle \) ,  \( \left|t_{2g}^{5}b_{x^{2}-y^{2}}^{0}b_{z^{2}a^{0}}^{2}x_{z^{2}-y^{2}}^{2}a_{z^{2}}^{0}\right\rangle \) , and  \( \left|t_{2g}^{5}b_{x^{2}-y^{2}}^{2}b_{z^{2}a^{0}}^{0}x_{z^{2}-y^{2}}^{0}a_{z^{2}}^{0}\right\rangle \) . The bonding and antibonding  \( e_{g} \)  orbital combinations are again strong mixtures of TM 3d and O 2p functions (see Fig. 2), such that the added hole has large weight at the O sites. However, in contrast to the hole state in cuprates, all six ligands are involved, although in the presence of lattice distortions [22] the  \( e_{g} \)  levels split and the hole does not have the same weight at each of the NN ligands. A study of the coupling between the charge and lattice degrees of freedom in  \( LaCoO_{3} \)  is left, however, for future work.

The strong O 2p hole character of the ionized state is expected to induce ferromagnetic (FM) correlations between the Co  \( t^{5} \) -like ion and its six Co NN's, like for the 2p hole in cuprates [38] or for the O  \( 2p_{g}^{1} \)  configuration in  \( NaV_{2}O_{5} \)  [13]. The formation of FM spin-polaron clusters was indeed inferred from measurements of the magnetization in lightly doped samples, see, e.g., ref. [15]. For no or small distortions, the configuration of each of the six Co NN's is  \( HS t_{2g}^{4}e_{g}^{2} \)  and the total spin of the spin cluster is  \( S = 1/2 + 6 \times 2 = 25/2 \) . If the coupling to the lattice is strong, an IS configuration  \( t_{2g}^{5}e_{g}^{1} \)  at the NN Co sites [22] can be energetically more favorable and the total spin is  \( S = 1/2 + 6 \times 1 = 13/2 \) . Obviously, the motion of the added hole is strongly renormalized by the NN FM correlations. In cuprates, for example, the NN "bare" hopping is reduced by a factor of 4 by short-range spin interactions [12]. The study of such correlations requires very involved calculations for  \( LaCoO_{3} \)  because a number of five d orbitals is needed at each TM site. A computational approach like that used in copper oxides, where all TM neighbors of the two octahedra directly involved in the hopping process are included in CASSCF [12], is at present not feasible for  \( LaCoO_{3} \) . The possibility of using an incremental scheme like that proposed in ref. [7] will be investigated in future work.

The lowest  \( (N+1) \)  states are related to the HS  \( t_{2g}^{5}e_{g}^{2} \)   \( (^{4}T_{1g}) \)  configuration. MRCI calculations which include in addition to the orbitals used in the cas-7 reference the Co 3s, 3p predict a splitting of 1.00 eV between the  \( t_{2g}^{5}e_{g}^{2} \)   \( (^{4}T_{1g}) \)  and  \( t_{2g}^{6}e_{g}^{1} \)   \( (^{2}E_{g}) \)  states.

The matrix elements (ME's) associated with local electron-removal and electron-addition configurations like those described above can be used to construct “correlated” band structures within a quasiparticle picture [32]. The  \( N \rightarrow (N \mp 1) \)  excitation energies correspond to the diagonal (“on-site”) ME's in the K-dependent secular problem while overlap and Hamiltonian integrals in-

a)

![](./images/867748218761380627_2.jpg)

FIG. 2: Bonding and antibonding p-d orbitals for the LS hole state of (a)  \( (x^{2}-y^{2}) \)  and (b)  \( z^{2} \)  symmetry. The  \( (x^{2}-y^{2}) \)  hybrids [see (a)] resemble the ZR p-d orbitals in cuprates.
 

volving holes or added electrons at different lattice positions  \( \mathbf{R} \)  (i.e.,  \( \langle\Psi_{0n\sigma}^{N+1}|\Psi_{\mathbf{R}n^{\prime}\sigma}^{N+1}\rangle \)  and  \( \langle\Psi_{0n\sigma}^{N+1}|H|\Psi_{\mathbf{R}n^{\prime}\sigma}^{N+1}\rangle \)  ME's, where n is a band index and  \( \sigma \)  denotes the spin) enter as off-diagonal (intersite) terms. As discussed above, accurate results for the intersite ME's cannot be obtained at this moment in  \( LaCoO_{3} \) . Nevertheless, we can extract from our data estimates for the ionization potential [lowest  \( N\rightarrow(N-1) \)  excitation energy] and electron affinity [lowest  \( (N+1) \)  state]. In our MRCI calculations, these values are  \( \mathrm{IP}_{0}=4.47 \)  and  \( \mathrm{EA}_{0}=-4.24 \)  eV and incorporate the most important short-range correlations. Corrections due to long-range polarization effects can be estimated by applying the approximation of a dielectric continuum [32]. This gives  \( \mathrm{IP}=\mathrm{IP}_{0}-C/R \)  and  \( \mathrm{EA}=\mathrm{EA}_{0}+C/R \) , where  \( C=e^{2}\frac{\epsilon_{0}-1}{\epsilon_{0}} \) ,  \( \epsilon_{0}\approx23 \)  [39] is the static dielectric constant, and R defines a sphere around the extra hole or electron beyond which the dielectric response reaches its asymptotic value  \( \epsilon_{0} \) . R is taken here as the average between the NN Co-O and Co-La distances, R=2.62 Å, which leads to IP=1.84 and EA=-1.61. Given the fact that we neglect the finite widths of the two bands, the energy difference  \( \mathrm{IP}-\mathrm{EA}=3.45 \)  eV represents an overestimate of the actual band gap.

To summarize, a recently developed ab initio scheme is applied here to the study of many-body effects in  \( LaCoO_{3} \) . The nonmagnetic low-T ground-state involves a subtle interplay between ligand-field and exchange interactions plus on-site and CT fluctuations. The lowest N-particle excited state is predicted to be the  \( HS t_{2g}^{4}e_{g}^{2} \)  state. In agreement with XAS [19] and INS [20] experiments, the IS  \( t_{2g}^{5}e_{g}^{1} \)  state is 0.60 eV higher. Whether this HS-IS splitting is sufficiently low to be compensated by the energy gain associated with a Jahn-Teller ordered configuration of the  \( e_{g} \)  orbitals, as suggested in ref. [22], will be the subject of future work. We also study the nature of the low-energy electron-removal and electron-addition states. The lowest  \( (N-1) \)  excitation is related to a local  \( t_{2g}^{5} \) , S=1/2 configuration. The added hole has large weight at the O sites, due to a strong mixing of the Co and O  \( e_{g} \)  orbitals. A large hole density at the O sites causes FM correlations among the adjacent Co 3d electrons, which agrees with the observation of “giant” FM polarons (S=10-16) and paramagnetic behavior at small doping and low T [15]. Our analysis offers new insight into the correlated electronic structure of  \( LaCoO_{3} \) . Additionally, the ab initio results provide valuable information for models aiming at a realistic description of the finite-temperature properties of this system.

We thank A. D. Rata, M. S. Laad, A. Shukla, G. Maris, and A. Stoyanova for stimulating discussions.

[1] V. I. Anisimov, J. Zaanen, and O. K. Andersen, Phys. Rev. B 44, 943 (1991).

[2] G. Kotliar et al., Rev. Mod. Phys. 78, 865 (2006).

[3] T. Maier, M. Jarrell, T. Pruschke, and M. H. Hettler, ibid. 77, 1027 (2005).

[4] F. Aryasetiawan et al., Phys. Rev. B 70, 195104 (2004); I. V. Solovyev and M. Imada, ibid. 71, 045103 (2005).

[5] P. Fulde, Adv. Phys. 51, 909 (2002).

[6] See, e.g., T. Helgaker, P. Jørgensen, and J. Olsen, Molecular Electronic-Structure Theory (Wiley, Chichester, 2000).

[7] H. Stoll, Phys. Rev. B 46, 6700 (1992).

[8] J. Gräfenstein, H. Stoll, and P. Fulde, ibid. 55, 13588 (1997).

[9] A. Shukla, M. Dolg, P. Fulde, and H. Stoll, ibid. 57, 1471 (1998).

[10] U. Birkenheuer, P. Fulde, and H. Stoll, Theor. Chem. Acc. 116, 398 (2006).

[11] U. Birkenheuer, C. Willnauer, M. von Arnim, W. Al-sheimer, and D. Izotov, Contribution II.1.8 in Scientific Report 2000-2002, MPI-PKS Dresden (2003), p. 71.

[12] L. Hozoi and M. S. Laad, Phys. Rev. Lett. 99, 256404 (2007); L. Hozoi, M. S. Laad, and P. Fulde, arXiv:0801.3607 (unpublished).

[13] L. Hozoi, C. Presura, C. de Graaf, and R. Broer, Phys. Rev. B 67, 035117 (2003).

[14] J. B. Goodenough, in Progress in Solid State Chemistry, Ed. H. Reiss (Pergamon, London, 1971), Vol. 5, p. 145.

[15] M. Imada, A. Fujimori, and Y. Tokura, Rev. Mod. Phys. 70, 1039 (1998), Sec. IV.G.4.

[16] M. Itoh, I. Natori, S. Kubota, and K. Motoya, J. Phys. Soc. Jpn. 63, 1486 (1994).

[17] D. Fuchs et al., Phys. Rev. B 77, 014434 (2008).

[18] A. D. Rata, A. Herklotz, K. Nenkov, L. Schultz, and K. Dörr, Phys. Rev. Lett. 100, 076401 (2008).

[19] M. W. Haverkort et al., ibid. 97, 176405 (2006).

[20] A. Podlesnyak et al., ibid. 97, 247208 (2006).

[21] R. F. Klie et al., ibid. 99, 047203 (2007).

[22] G. Maris et al., Phys. Rev. B 67, 224423 (2003).

[23] M. A. Korotin et al., ibid. 54, 5309 (1996).

[24] CRYSTAL 2000, University of Torino, Italy.

[25] For O, we used the basis set (BS) of Corà [26], without d functions. For La, Towler's BS was applied, see http://www.tcm.phy.cam.ac.uk/~mdt26/crystal.html. For Co, we used Towler's s and p functions (see above) and the d functions of Seijo et al. [27].

[26] F. Corà, Mol. Phys. 103, 2483 (2005).

[27] L. Seijo, Z. Barandiaran, and S. Huzinaga, J. Chem. Phys. 91, 7011 (1989).

[28] P. G. Radaelli and S.-W. Cheong, Phys. Rev. B 66, 094408 (2002).

[29] C. M. Zicovich-Wilson, R. Dovesi, and V. R. Saunders, J. Chem. Phys. 115, 9708 (2001).

[30] MOLPRO 2006, Cardiff University, United Kingdom.

[31] The “active” octahedron is centered at  \( (0,0,0) \) , the six NN octahedra at  \( (\pm a,0,0) \) ,  \( (0,\pm a,0) \) , \( (0,0,\pm a) \) , and the La NN's are at  \( (\pm a/2,\pm a/2,\mp a/2) \) .

[32] See [10, 33] and references therein for details.

[33] L. Hozoi, U. Birkenheuer, P. Fulde, A. Mitrushchenkov, and H. Stoll, Phys. Rev. B 76, 085109 (2007).

[34] In the present version of MOLPRO [30], for an open-shell reference wavefunction, the virtual orbital space cannot be restricted only to the  \( C_{A} \)  region. It includes thus functions in both  \( C_{A} \)  and  \( C_{B} \) , which leads to very large expansions of the wavefunction,  \( \approx10^{9} \)  Slater determinants.

[35] For example,  \( 2p_{\pi}(t_{2g})-3d(t_{2g}) \)  excitations would slightly
 

favor the HS state, while the use of larger basis sets should stabilize the LS state.

[36] R. H. Potze, G. A. Sawatzky, and M. Abbate, Phys. Rev. B 51, 11501 (1995).

[37] F. C. Zhang and T. M. Rice, ibid. 37, 3759 (1988).

[38] In contrast to the original picture of Zhang and Rice,

from the magnetic point of view, the two-hole p-d state is not decoupled from other TM sites, see [12].

[39] M. S. Islam, M. Cherry, and C. R. A. Catlow, J. Solid State Chem. 124, 230 (1996).
 
