
# Electronic Structure and Fermiology of Superconducting LaNiGa \( _{2} \) 

David J. Singh

Materials Science and Technology Division, Oak Ridge National Laboratory, Oak Ridge, Tennessee 37831-6056 (Dated: August 19, 2021)

We report electronic structure calculations for the layered centrosymmetric superconductor  \( LaNiGa_{2} \) , which has been identified as having a possible triplet state based on evidence for time reversal symmetry breaking. The Fermi surface has several large sheets and is only moderately anisotropic, so that the material is best described as a three dimensional metal. These include sections that are open in the in-plane direction as well as a section that approaches the zone center. The density of states is high and primarily derived from Ga p states, which hybridize with Ni d states. Comparing with experimental specific heat data, we infer a superconducting  \( \lambda \leq 0.55 \) , which implies that this is a weak to intermediate coupling material. However, the Ni occurs in a nominal  \( d^{10} \)  configuration in this material, which places the compound far from magnetism. Implications of these results for superconductivity are discussed.

PACS numbers: 74.20.Rp, 74.20.Pq, 74.70.Dd

## I. INTRODUCTION

Hillier and co-workers recently discovered the appearance of spontaneous magnetic fields with onset at the superconducting critical temperature in samples of the centrosymmetric intermetallic compound  \( LaNiGa_{2} \)  using muon spin rotation ( \( \mu SR \) ). \( ^{1} \)  Symmetry analysis implies that  \( LaNiGa_{2} \) , which is a  \( \sim2 \)  K superconductor, \( ^{2,3} \)  is a triplet superconductor with a non-unitary state. \( ^{1} \)  One mechanism for obtaining triplet superconductivity is nearness to ferromagnetism as in the likely triplet superconductor  \( Sr_{2}RuO_{4} \) . \( ^{4-6} \)  Interestingly, Ni is a ferromagnet and intermetallic  \( Ni_{3}Ga \)  is a highly renormalized itinerant paramagnet near ferromagnetism. \( ^{7,8} \) 

There is, however, little other data available about the superconducting properties of  \( LaNiGa_{2} \) . So far, three reports are all based on polycrystalline samples prepared by arc melting using different source material. Aoki and coworkers reported bulk superconductivity with  \( T_{c}=2.01 \)  K (onset at 2.1 K) on a sample with a residual resistivity ratio of 34 and residual resistivity of  \( \sim1.5\ \mu\Omega \)  cm, while Zeng and co-workers obtained  \( T_{c}=1.97 \)  K, on a sample with a residual resistivity ratio of 5.2 and residual resistivity of  \( 14.1\ \mu\Omega \)  cm.

The purpose of this paper is to report the electronic structure and related properties in relation to the superconductivity of this material. Our density functional calculations were based on the generalized gradient approximation of Perdew, Burke and Ernzerhof, \( ^{9} \)  and used the general potential linearized augmented planewave (LAPW) method, \( ^{10} \)  as implemented in the WIEN2k code. \( ^{11} \)  The LAPW sphere radii employed were 2.5 bohr, 2.2 bohr and 2.0 bohr for La, Ni and Ga, respectively. Relativity was included at the scalar relativistic level for the valence states (the core states were treated fully relativistically). We used highly converged basis sets corresponding to  \( R_{min}k_{max}=9.0 \) , where  \( k_{max} \)  is the interstitial planewave cut-off and  \( R_{min}=2.0 \)  bohr is the smallest sphere radius, as well as dense Brillouin zone samples, i.e. a 32x32x32 mesh for the calculations of the Fermiology.

![](./images/867772349355655651_1.jpg)

FIG. 1. (color online) Crystal structure of  \( LaNiGa_{2} \)  showing the coordinate system used here. The structure depicted is based on the experimental lattice parameters with relaxed internal coordinates.

and a 16x16x16 mesh for the fixed spin moment calculations. The semi-core states (La 5s, 5p, Ni 3p and Ga 3d) were included with the valence electrons using local orbitals. We used the standard LAPW basis, as opposed to the so-called APW+lo basis. \( ^{12} \) 

LaNiGa \( _{2} \)  occurs in an orthorhombic structure, with space group, #65, Cmmm, and two formula units per primitive cell. \( ^{13} \)  The calculations were done using the experimental lattice parameters,  \( a=4.29\ \AA \) ,  \( b=17.83\ \AA \)  and  \( c=4.273\ \AA \) , \( ^{13} \)  with internal atomic coordinates determined by total energy minimization. The structure is depicted in Fig. 1 and the calculated atomic coordinates are given in Table I. As may be seen, the structure is layered along the b-axis. This might suggest an effectively two dimensional electronic structure, but this is not what we find (see below).

We start with the large energy scale features of the band structure and density of states (DOS), which are shown in Figs. 2 and 3, respectively. The band structure shows four bands in the energy range from -9 eV to -4 eV (all energies are given with respect to the Fermi energy  \( E_{F} \) ). These are derived primarily from the Ga s orbitals.
 

TABLE I. Internal atomic coordinates of Cmmm LaNiGa \( _{2} \)  as determined by total energy minimization. The coordinates are with respect to the experimental lattice parameters,  \( a=4.29 \AA \) ,  \( b=17.83 \AA \)  and  \( c=4.273 \AA \) 

<table><tr><td></td><td>x</td><td>y</td><td>z</td></tr><tr><td>La (4j)</td><td>0.0</td><td>0.3591</td><td>0.5</td></tr><tr><td>Ni (4i)</td><td>0.0</td><td>0.0719</td><td>0.0</td></tr><tr><td>Ga1 (4i)</td><td>0.0</td><td>0.2092</td><td>0.0</td></tr><tr><td>Ga2 (2d)</td><td>0.0</td><td>0.0</td><td>5.5</td></tr><tr><td>Ga3 (2b)</td><td>0.0</td><td>0.0</td><td>5.0</td></tr></table>

(note that there are two formula units per primitive unit cell, i.e. 4 Ga atoms). The unoccupied flat bands starting at  \( \sim2 \)  eV are the La 4f states.

Between the Ga s bands and the La f resonance there are dispersive bands of primarily Ga p character and additional flatter bands centered at  \( \sim \) 2 eV. These occupied flat bands are the Ni d bands, which mix with the Ga p bands in the energy range around -2 eV. This is clearly seen in the DOS, which has a prominent peak of Ni d character centered near -2 eV, with a width of  \( \sim \)  2 eV. While one may observe that there is some Ni d character at and above  \( E_{F} \) , this is a minor component that arises because of hybridization in the Ga p derived bands. This means that the Ni d bands are nominally occupied in this compound, and correspondingly that Ni occurs in a  \( d^{10} \)  configuration.

The implication is that electronic structure near the Fermi energy in  \( LaNiGa_{2} \)  is derived from sp bands of primarily Ga p character, hybridized with Ni d states. This is surprising for an unconventional superconductor, where one might naturally suppose that triplet pairing is a consequence of magnetism associated with the transition element or perhaps other correlation effects due to an open d or f shell.

Turning to the low energy properties, there are several bands crossing the  \( E_{F} \)  as shown in Fig. 2. We obtain  \( N(E_{F})=3.19\ \mathrm{eV}^{-1} \)  on per formula unit both spins basis, which corresponds to a bare specific heat coefficient,  \( \gamma_{bare}=7.52 \) . Zeng and co-workers \( ^{2} \)  reported a specific heat coefficient,  \( \gamma=11.64\ \mathrm{mJ/mol\ K^{2}} \) , which implies an enhancement,  \( \gamma=\gamma_{bare}(1+\lambda) \) , with  \( \lambda=0.55 \) . This is consistent with the conclusion of Zeng and co-workers that  \( LaNiGa_{2} \)  is a weakly coupled superconductor.

The substantial value of  \( N(E_{F}) \)  would imply that the material is either an itinerant ferromagnet or close to it if the bands near the Fermi energy were primarily Ni derived. However, this is not the case and the Ni d component of the density of state is not large, having a value of  \( 0.59\,eV^{-1} \)  per formula unit both spins. Taking a typical Ni Stoner I of  \( 1\,eV \) , \( ^{14} \)  this yields  \( NI \sim 0.3 \)  (note that the  \( N(E_{F}) \)  in the Stoner formula is per spin). This is far less than unity, indicating that this material is not near magnetism. We did fixed spin moment calculations to confirm this. The energy as a function of constrained moment is shown in Fig. 4. As may be seen there is no indication of metamagnetism or nearness to a ferromag-

![](./images/867772349355655651_2.jpg)

FIG. 2. (color online) Density functional band structure of LaNiGa \( _{2} \)  as obtained for the relaxed crystal structure. The dotted horizontal lines at 0 eV denote the Fermi energy,  \( E_{F} \) . The lower panel is a blow-up around  \( E_{F} \) . The path through the zone and labels are shown in the inset.

![](./images/867772349355655651_3.jpg)

FIG. 3. (color online) Electronic density of states and d projection onto the Ni LAPW sphere on a per formula unit basis.
 
![](./images/867772349355655651_4.jpg)

FIG. 4. (color online) Energy as a function of constrained spin magnetization from fixed spin moment calculations. The energy and magnetization are on a per formula unit basis, and the energy is relative to the non-spin-polarized case. The symbols are calculated points, while the curve is an interpolation.

![](./images/867772349355655651_5.jpg)

FIG. 5. (color online) Two views of the calculated Fermi surface of  \( LaNiGa_{2} \) .  \( \Gamma \)  is at the center of each plot. The zone and labels are given in the inset of Fig. 2. The coloring is arbitrary and is used to distinguish the different sections.

netic state.

The calculated Drude plasma energies are  \( \hbar\Omega_{p,xx}=4.40 \)  eV,  \( \hbar\Omega_{p,yy}=2.11 \)  eV, and  \( \hbar\Omega_{p,zz}=4.71 \)  eV. Within Boltzmann transport theory, the conductivity is related to the plasma frequency,  \( \sigma_{xx} \propto N(E_{F}) < v_{x}^{2} > \tau \propto \Omega_{p,xx}^{2}\tau \) , and similarly for the other directions, where  \( \tau \)  is an inverse scattering rate. Therefore the transport is predicted to be three dimensional, and only moderately anisotropic, with the b-axis conductivity lower than the in-plane conductivity by a factor of  \( \sim5 \) . This three dimensionality is perhaps not surprising in light of the fact that the electronic structure near  \( E_{F} \)  is derived from bands that have primary Ga p character, hybridized with Ni d states, rather than being mainly derived from the more compact Ni d orbitals.

As mentioned, there are several bands that cross  \( E_{F} \) . The Fermi surface is shown in Fig. 5. There are several large sheets, including sheets near the zone center as well as the zone corners. Additionally, besides open sheets along  \( k_{y} \) , which is the direction perpendicular to the layers, there are open sheets along both of the in-plane  \( (k_{x}, k_{z}) \)  directions as well. Specific heat measurements show an exponential dependence below  \( T_{c} \)  (Ref. 2), which indicates a fully gapped superconducting state. In a triplet superconductor the order parameter must change sign under inversion through the  \( \Gamma \)  point. In this context the combination of a fully gapped state and the complex open Fermi surfaces in all crystallographic directions and sheets very close to the zone center is unexpected since simple triplet states would not be fully gapped on such a Fermi surface.

The thermopower of a metal is sensitive to the details of the band structure at the Fermi energy. We calculated the thermopower within the constant scattering time approximation based on the first principles band structure. We used the Boltzmann equation to derive the results. We obtain negative values of  \( S_{xx}(300\;\mathrm{K})=-8.3\;\mu\mathrm{V/K} \) ,  \( S_{yy}(300\;\mathrm{K})=-9.6\;\mu\mathrm{V/K} \) , and  \( S_{zz}(300\;\mathrm{K})=-0.3\;\mu\mathrm{V/K} \) . Averaging these values with the conductivity, we obtain  \( S_{av}=(S_{xx}\sigma_{xx}+S_{yy}\sigma_{yy}+S_{zz}\sigma_{zz})/(\sigma_{xx}+\sigma_{yy}+\sigma_{zz})=-4.6\;\mu\mathrm{V/K} \)  at 300 K, which is very close to the value of  \( \sim-5\;\mu\mathrm{V/K} \)  from Fig. 8 of Ref. 3. This provides support for the calculated Fermi surface.

To summarize the results of the calculations, we find Ni to be in a nominal  \( d^{10} \)  state. LaNiGa \( _{2} \)  has a complex three dimensional Fermi surface, derived mainly from sp states, that hybridize with Ni d states. This Fermi surface includes open sections in all three crystallographic directions and additionally has a section near the zone center. We do not find proximity to ferromagnetism but we do find a moderately high  \( N(E_{F}) \) , which in conjunction with experimental specific heat data suggests a modest  \( \lambda \)  consistent with weak coupling.

The data raise some other questions about the superconductivity of  \( LaNiGa_{2} \) . First of all, we do not find heavy bands. However, the weak dependence of  \( T_{c} \)  on residual resistivity \( ^{2,3} \)  is most readily explained in a triplet scenario if the bands are very heavy (as in a heavy Fermion) so that the coherence length becomes very short. Actually, besides the dispersive bands, we note that the coherence length  \( \zeta=28 \)  nm determined from the  \( \muSR \)  measurements is not so short although it is shorter than the 66 nm coherence length of  \( Sr_{2}RuO_{4} \) . \( ^{4} \)  Secondly, there is a difficulty in identifying a plausible pairing interaction. While a purely attractive interaction, such as the electron phonon interaction can be pairing for a triplet state provided that it has strong momentum dependence, as is easily seen from the gap equation it will be more pairing for a conventional singlet s-wave state. Therefore even in this case an additional repulsive in-
 

interaction will be needed. Two possible interactions are the Coulomb repulsion, and spin-fluctuations. However, the dispersive sp bands argue against these in  \( LaNiGa_{2} \) . Also the modest value of the  \( \lambda \)  inferred from the specific heat does not leave much room for competing interactions (note that in a case where one has repulsive and attractive interactions they will partially cancel for the superconducting  \( \lambda \)  but will be additive for the specific heat  \( \lambda \) ).

Nonetheless, it is a fact that time reversal symmetry breaking has been observed by  \( \mu \) SR at the bulk  \( T_{c} \)  in samples of this material. \( ^{1} \)  Further characterization

 \( ^{1} \)  A. D. Hillier, J. Quintanilla, E. Mazidian, J. F. Annett, and R. Cywinski, Phys. Rev. Lett., 109, 097001 (2012).

 \( ^{2} \)  N. L. Zeng and W. H. Lee, Phys. Rev. B, 66, 092503 (2002).

 \( ^{3} \)  Y. Aoki, K. Terayama, and H. Sato, J. Phys. Soc. Jpn., 64, 3986 (1995).

 \( ^{4} \)  A. P. Mackenzie and Y. Maeno, Rev. Mod. Phys., 75, 657 (2003).

 \( ^{5} \)  T. M. Rice and M. Sigrist, J. Phys.: Condens. Matter, 7, L643 (1995).

 \( ^{6} \)  I. I. Mazin and D. J. Singh, Phys. Rev. Lett., 79, 733 (1997).

 \( ^{7} \)  S. M. Hayden, G. G. Lonzarich, and H. L. Skriver, Phys. Rev. B, 33, 4977 (1986).

 \( ^{8} \)  A. Aguayo, I. I. Mazin, and D. J. Singh, Phys. Rev. Lett., 92, 147201 (2004).

of  \( LaNiGa_{2} \)  and its superconducting properties would be highly desirable, particularly using pure phase single crystals if these can be made.

## ACKNOWLEDGMENTS

I am thankful for helpful discussions with J. Quintanilla, J.F. Annett and A.D. Hillier. This work was supported by the Department of Energy, Basic Energy Sciences, Materials Sciences and Engineering Division.

 \( ^{9} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett., 77, 3865 (1996).

 \( ^{10} \)  D. J. Singh and L. Nordstrom, Planewaves Pseudopotentials and the LAPW Method, 2nd Edition (Springer, Berlin, 2006).

 \( ^{11} \)  P. Blaha, K. Schwarz, G. Madsen, D. Kvasnicka, and J. Luitz, WIEN2k, An Augmented Plane Wave + Local Orbitals Program for Calculating Crystal Properties (K. Schwarz, Tech. Univ. Wien, Austria) (2001).

 \( ^{12} \)  E. Sjostedt, L. Nordstrom, and D. J. Singh, Solid State Commun., 114, 15 (2000).

 \( ^{13} \)  V. A. Romaka, Y. N. Grin, Y. P. Yarmolyuk, R. V. Skolozdra, and A. A. Yartys, Ukrainskii Fizicheskii Zhurnal, 28, 227 (1983).

 \( ^{14} \)  J. F. Janak, Phys. Rev. B, 16, 255 (1977).

 \( ^{15} \)  G. K. H. Madsen and D. J. Singh, Comput. Phys. Commun., 175, 67 (2006).
 
