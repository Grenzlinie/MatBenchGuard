PHYSICAL REVIEW B 69, 195312 (2004)

# Simulation of Ge/Si intermixing during heteroepitaxy

Richard J. Wagner* and Erdogan Gulari
Department of Chemical Engineering, University of Michigan, Ann Arbor, Michigan 48109, USA

(Received 3 November 2003; published 25 May 2004)

During epitaxial growth of Ge on Si(001), intermixing can occur between the deposited Ge and the Si substrate. We show that although Ge prefers to wet the surface, entropy drives some fraction into the underlying layers. We present a simple model of intermixing by equilibration of the top crystal layers in the absence of bulk diffusion. The equilibration is performed with a flexible lattice Monte Carlo simulation. Ultimately, intermixing leads to a temperature-dependent graded Ge concentration. The resulting evolution of chemical potential is consistent with the onset of islanding after 3-4 monolayers of deposition.

DOI: 10.1103/PhysRevB.69.195312
PACS number(s): 68.35.Md, 02.70.Uu, 68.35.Fx

## I. INTRODUCTION

Heteroepitaxy of germanium on silicon is an important technology in microelectronic fabrication. Electronic differences between Ge and Si make their combination useful for constructing high-efficiency lasers and photodetectors from quantum wells or quantum dots. $^{1}$ Such devices are grown by depositing thin films on the order of 10 nm onto Si surfaces. The exact structure of these surfaces and thin films becomes increasingly important as the feature size in devices approaches the atomic scale.

Deposition of Ge on a clean Si wafer may be thought ideally to form an abrupt interface between the materials. However, many experimental studies have shown some degree of intermixing. Qin et al. detected mixing as Si-Ge dimers diffused across a $Si(001)$ surface. $^{2}$ Nakajima et al. measured Ge/Si(001) intermixing by high-resolution Rutherford backscattering spectroscopy, finding Ge mixed as deep as the fourth layer and measuring the change in composition with temperature and coverage. $^{3,4}$ Lin et al. tracked the distribution of Si and Ge on a growing Ge/Si(001) surface by scanning tunneling microscopy. $^{5}$ The continued presence of Si atoms on the surface after two monolayers (ML) of Ge deposition revealed intermixing. Figure 1 illustrates the contrast between an ideal abrupt interface and a more realistic one with intermixing.

During epitaxial growth, several atomic processes occur within the forming crystal: adsorption, desorption, surface diffusion, and bulk diffusion. For a given net deposition rate (adsorption minus desorption), the remaining growth processes are surface diffusion and bulk diffusion. But there is a large difference between the rates of these two types of diffusion. Atoms at the surface are much less confined and can more easily move to other lattice sites. Qin et al. measured an activation energy of 1.01 eV and an attempt frequency of $10^{14}$ Hz for Ge-Si dimers diffusing on the surface of $Si(100).^{6}$ Fahley et al. reported an activation energy of 4-5 eV for diffusion of Ge atoms in bulk Si. $^{7}$ Thus, surface diffusion is much faster than bulk diffusion and we can approximate growth by neglecting bulk diffusion and considering the surface atoms to be in a local equilibrium. As each layer is deposited, it exchanges atoms with the topmost layer of the substrate. But once a layer is completely buried by added layers, it ceases to exchange atoms. This simplification is supported by the findings of Copel et al. who presented evidence of intermixing occurring during growth at $500^{\circ}C$ but not at room temperature nor during postgrowth annealing. $^{8}$

## II. METHODS

We model the growth of Ge on Si at the atomic scale. Construction begins with the crystal substrate. Silicon atoms are initially placed on a diamond lattice, each atom within the bulk of the crystal having four bonded neighbors. At the surface, atoms are paired into dimers to form the $(2×1)$ reconstruction. The simulated system spans sixteen by sixteen unit cells along the [100] and [010] axes (where the Si unit cell length is $5.43\mathring{A}$). Periodic boundaries are imposed along these horizontal edges. The initial substrate thickness is sixteen layers of mobile atoms along the [001] axis. Two layers of atoms fixed at the ideal bulk Si positions anchor the bottom edge. For cases where a Ge epilayer is added, dimers are removed to form the $(2×8)$ reconstruction.

Once an atomic configuration is set, the total energy is calculated with the Tersoff potential. $^{9}$ The accuracy of this potential for modeling structure, elastic properties, and defect energies is reviewed elsewhere. $^{10,11}$ The atomic positions are then relaxed by conjugate gradient minimization $^{12}$ until the net force on each atom falls below $10^{-3}$ eV/Å. Thus, the minimum-energy conformation is determined for any configuration of atoms.

Intermixing is performed by a flexible lattice Monte Carlo equilibration. First, the energy of the initial configuration is noted. Then a swapping event is attempted: two atoms from within the top two layers are randomly chosen and exchanged. Another relaxation is performed to compute the en-

![](./images/812349675083399169_1.jpg)

FIG. 1. (Color online) Schematic cross section of Ge/Si interfaces. In a simple model of abrupt heteroepitaxy, the Ge atoms (dark) sit atop the Si substrate (light). With intermixing, some Ge diffuses into the substrate, displacing Si atoms into the epilayers.

![](./images/812349675083399169_2.jpg)

FIG. 2. Evolution to local equilibrium after deposition of 1 ML Ge $(2\times8)$ on Si at $600\ ^{\circ}\text{C}$. The surface concentration (circles) and total energy (squares) stabilize before the data collection window of 25–50 MCS (horizontal bar).

ergy of the new configuration. Then the Metropolis algorithm is followed to determine whether to keep the new configura- tion or revert to the initial configuration. $^{13}$ The likelihood of accepting a new configuration is dictated by the thermal en- ergy $kT$, where $k$ is the Boltzmann constant and $T$ is the temperature. If the change in energy $\Delta E$ is negative then the new configuration is accepted. If $\Delta E$ is positive then the new configuration is accepted with probability $p=e^{-\Delta E/kT}$ or re- jected otherwise.

This process of attempted atom exchanges is repeated for 25 Monte Carlo steps (MCS), where one MCS consists of as many attempted exchanges as there are atoms in the inter- mixing region. Then an additional 25 MCS are run with properties measured and averaged at 1 MCS intervals. Figure 2 demonstrates that 25 MCS is a sufficient duration for the system to reach local equilibrium before data collection. A complete run of 50 MCS took 450 h on a 1.0 GHz personal computer processor.

This method is closely related to the Ising model of lattice Monte Carlo simulation. $^{14}$ In that model, the dipoles of a magnet sit on the vertices of a square lattice. At each step, an exchange of dipoles is attempted, with the resulting energy calculated from the interactions between adjacent dipoles. The method described here likewise maintains atoms on a well-defined lattice, where the lattice describes the configu- ration of bonds between atoms. However, the lattice is al- lowed to deform as the lengths and angles of the bonds relax to a minimum-energy conformation. The practical difference is that the calculation of energy is not a simple evaluation directly from lattice occupancy but instead requires minimi- zation based on the complex interactions of bond lengths and angles. A similar technique of Monte Carlo simulation with relaxation at every step was performed by Barabási. $^{15}$ Re cently, Sonnet et al. studied Ge/Si intermixing in quantum dots with similar Ising-type exchanges in a crystal likewise modeled with the Tersoff potential. $^{16}$ Earlier investigations by Kelires et al. introduced that method to model the bulk and surface of Si-Ge alloys, although without the configura- tion lattice and global relaxation described here. $^{17,18}$ Our work differs primarily in the application of the technique to study evolution of the wetting layer during growth.

![](./images/812349675083399169_3.jpg)

FIG. 3. (Color online) Intermixing between the Si substrate and a Ge epilayer. Atoms of Si (light) and Ge (dark) are shown for the top two layers. Zigzag lines indicate dimer bonds and tapered lines indicate bonds from the topmost layer (larger circles) down to the second layer (smaller circles). (a) Initial configuration with an abrupt interface. (b) Swapping one Ge atom from the epilayer into the substrate increases the crystal energy by $+223$ meV.

### III. SURFACE INTERMIXING

Energetics drives Ge to wet a Si surface. While the atoms within the bulk of a diamond lattice each have four neigh- bors, atoms at the surface are left with only two neighbors and two dangling bonds. Formation of surface dimers re- lieves one dangling bond per atom but the other remains. In a crystal containing both Si and Ge, it is most efficient for the Ge to migrate to these surface sites—Ge bonds are weaker than Si bonds, so the cost of dangling bonds is cheaper for Ge than for Si.

A simple simulation illustrates these wetting energetics. Figure 3 shows an overhead view of a Si substrate covered by 1 ML of Ge. In Fig. 3(a), the topmost layer is composed entirely of Ge. In Fig. 3(b), one Ge atom has been swapped from its surface site down to the second layer. The energy cost of this exchange is $+223$ meV. This matches the aver- age energies for moving a Ge atom from the top to the sec- ond layer as calculated by density functional theory: $+145$ meV by Cho et al. $^{19}$ and $+226$ meV by Yoshimoto et al. $^{20}$ Thus, the entirely Ge-terminated surface is confirmed as the lowest energy configuration. However, the cost of in- termixing is accessible with the thermal energy $kT$. At $600\ ^{\circ}\text{C}$, $kT=75$ meV and the probability of exchange, $e^{-\Delta E/kT}$, is $5\%$.

A simulation of surface equilibration was performed by mixing the top two layers of a system with 1 ML Ge on a Si substrate. Initially, the surface is entirely terminated by Ge as seen in Fig. 4(a). During equilibration, the exchange of at- oms moves some Ge into the second layer and leaves Si on the surface. After 50 MCS at $600\ ^{\circ}\text{C}$, only $76\%$ of the sur- face atoms are Ge. Figure 4(b) shows the formation of pure and mixed Si dimers on the surface. The energy cost of mov- ing a Ge atom away from the surface is more easily attained at higher temperatures. Figure 5 shows that simulation over the temperature range of $400\ ^{\circ}\text{C}$–$800\ ^{\circ}\text{C}$ produces the trend

![](./images/812349675083399169_4.jpg)

FIG. 4. (Color online) Equilibration of surface concentration. (a)
Initial construction of a Si substrate covered by a 1 ML Ge (2
×8) epilayer. (b) Structure after the top two layers have equili-
brated at 600 °C. One quarter of the Ge atoms have moved into the
substrate, displacing Si into pure and mixed dimers on the surface.

of decreasing surface atomic fraction of Ge. These results
qualitatively match experimental observations of surface Ge
reduction for submonolayer Ge films.³

Our assumption of active surface diffusion and the ab-
sence of bulk diffusion should be applicable over a wide
range of temperatures. Qin *et al.* observed the exchange of
Ge from diffusing surface dimers into the Si substrate at
temperatures as low as 100 °C.⁶ In contrast, the high activa-
tion energy for bulk diffusion limits its effect until at least
800 °C, at which temperature the residence time for Ge at-
oms in Si is roughly one day.

![](./images/812349675083399169_5.jpg)

FIG. 5. Surface concentration after deposition of 1 ML Ge (2
×8). As temperature increases, more Ge mixes into the topmost Si
layer and less remains at the surface. Error bars indicate standard
deviations during data collection.

## IV. INTERMIXING DURING GROWTH

Equilibration of a single Ge layer may be extended to the
process of intermixing during growth. Atom exchange within
the top two layers is simply repeated as additional Ge layers
are deposited on the surface. We study this intermixing in
systems of up to 3000 atoms. Equilibrium distributions of Ge
have been calculated for 1 ML films by density functional
theory, but computational demands limited those studies to
tens of atoms in highly periodic structures.¹⁹,²⁰ Application
of a proven empirical potential permits much larger and
more complex systems to be studied. Modeling the evolution
of the Ge film during growth is important for characterizing
the Si-Ge interface and understanding the transition to is-
landing.

### A. Whole layers

We model this growth scenario with a multistage flexible
lattice Monte Carlo simulation. The system begins with an
eight by eight unit cell substrate of pure Si with (2×1)

![](./images/812349675083399169_6.jpg)

FIG. 6. (Color online) Growth sequence with intermixing at 600 °C. (a) A layer of Ge (2×8) is deposited on a Si(001) substrate. (b) The
top two layers are equilibrated, swapping 0.21 ML of Ge into the second layer. (c) A second layer of Ge is deposited, forming a (2×8)
reconstruction on the surface and filling in the missing dimers of the former surface layer. (d) The top two layers are again equilibrated,
moving 0.02 ML of Ge; the layer which was previously second is now buried as the third layer and no longer exchanges atoms. The atomic
percent of Ge in each layer is labeled. These percentages do not sum to 100% since the top layer is in a (2×8) reconstruction and therefore
contains only 7/8 ML of atoms.

![](./images/812349675083399169_7.jpg)

FIG. 7. (Color online) Concentration profiles for growth at various temperatures. At 1 K the concentration changes abruptly at the interface. For higher temperatures, intermixing yields a graded profile.

surface reconstruction. Then, a single epilayer of Ge with $(2\times 8)$ reconstruction is placed atop the substrate. With the new epilayer in place, we equilibrate the top two layers at the growth temperature. After 150 MCS, the composition and energy of the system are noted. Then, another epilayer is added and equilibrated. Figure 6 shows the evolution of composition during the growth sequence. Once the original surface layer becomes buried by two epilayers it ceases to participate in the surface equilibration. This process of deposition and local equilibration is repeated until seven Ge layers have been added.

The growth simulation yields a final structure with a graded composition profile. Figure 7 shows how the amount of intermixing depends on anneal temperature. At 1 K, no intermixing occurs (since the thermal energy is insufficient to overcome the energy cost of moving Ge away from the surface) and the Ge/Si interface is abrupt. At temperatures of $400\,^{\circ}\text{C}$ to $800\,^{\circ}\text{C}$ the intermixing increases, carrying 0.24 ML of Si into the epilayers at $800\,^{\circ}\text{C}$.

### B. Atomic layer epitaxy

Atomic layer epitaxy is a technique for depositing precisely controlled doses of Ge atoms onto a substrate surface. Each dosage cycle consists of two steps: (1) deposition of a hydrogenated Ge compound at low temperature to saturate the surface and (2) annealing at high temperature to remove the hydrogen and allow restructuring of the surface.$^{5}$ Since the amount of the hydrogenated Ge precursor that can adsorb to the surface is limited by surface area, the amount deposited with each cycle is a constant fraction of a monolayer.

Modeling heteroepitaxy of fractional monolayers requires more sophistication than the general case of whole monolayers. The surface must remain smooth to avoid the effect of steps as the fractional layers are added. This is accomplished by depositing the Ge dose in a patch after first shifting substrate atoms downward to open a matching indentation on the surface. This downward shift occurs in a column extending to the base of the substrate; Si atoms moving beyond the fixed layers at the bottom are simply discarded. With each deposition, the placement of the patch is relocated adjacent to the previous patch. This advancement of the deposition site approximates the behavior of a moving step edge on an extensive substrate. After each dose of Ge, the top two layers are equilibrated at the anneal temperature of 950 K. Figure 8 illustrates the prescribed sequence for the first two cycles of Ge deposition.

We perform the atomic layer epitaxy simulations with a system size of 16 by 16 unit cells and 25 MCS equilibration times. As the growth proceeds, some Si from the substrate mixes into the epilayers and remains at the surface. As shown in Fig. 9, even at 1.2 ML when there is enough Ge to completely coat the surface, 14% of the surface atoms are still Si. The compositions resulting from this growth sequence may be compared directly to the experiments of Lin $et$ $al.^{5}$ Our simulations appear to be slightly conservative—more intermixing occurs in experiment, leading to a higher surface concentration of Si at 2.0 ML coverage. This discrepancy is explained by our application of intermixing to only

![](./images/812349675083399169_8.jpg)

FIG. 8. (Color online) Growth sequence for atomic layer epitaxy with cycles of 0.4 ML Ge deposition. (a) The system begins with a Si(001)-$(2\times 1)$ substrate 16 ML thick. (b) Atoms within a 0.4 ML patch are shifted downward to form an indentation. (c) The indentation is filled with Ge $(2\times 1)$. (d) The top two layers are equilibrated at 950 K, allowing some Ge to move into the second layer. (e) Another indentation is formed adjacent to the site of the first. The downward shift relocates some Ge from the second layer to the third. (f) The indentation is filled with another 0.4 ML dose of Ge. (g) Equilibration of the top two layers relocates some Ge to help wet the surface. The atomic percent of Ge in each layer is labeled.

![](./images/812349675083399169_9.jpg)

FIG. 9. Surface concentration during atomic layer epitaxy. Intermixing at 950 K moves some Ge atoms into the substrate and maintains a presence of Si atoms on the surface even after 1.2 ML of Ge have been deposited.

the top two surface layers. Diffusion deeper into the substrate can occur but would be limited kinetically rather than thermodynamically. Thus these simulations give at least a lower bound for intermixing and the graded concentration profiles may be applied to examining the structure and energetics of heteroepitaxy.

### V. ONSET OF ISLANDING

A very interesting application of Ge heteroepitaxy on Si is the self-assembly of nanometer-scale islands, or quantum dots. $^{21}$ Experimentally, island formation is found to begin once 3-4 ML of Ge are deposited. $^{22}$ Why does islanding begin at that particular thickness? The onset of islanding is determined by chemical potential—islands form if the energy per atom in an island is less than that in a flat epilayer. By modeling the islands as pyramids with rebonded step {105} facets, we have calculated the chemical potential for ideal islands to be 31 meV/atom. $^{23}$ We now calculate the chemical potential for flat epilayers, including the effects of intermixing. Comparison of the potentials affords direct prediction for the onset of islanding.

During the growth simulations, the top two crystal layers are allowed to equilibrate after each layer of Ge is deposited. Then, the average total energy is tabulated. The chemical potential $\mu_{\text{epi}}$ for each epilayer is

$$
\mu_{\text{epi}}=\frac{E_{\text{epi}}-E_{\text{ref}}}{N}-\epsilon_{\text{Ge}},
$$

where $E_{\text{epi}}$ is the total energy with that epilayer, $E_{\text{ref}}$ is the energy before the epilayer was added, $N$ is the number of atoms added, and $\epsilon_{\text{Ge}}$ is the cohesive energy of bulk Ge ($-3.8506$ eV/atom).

The chemical potential for growth at $800^\circ\text{C}$ is compared with that of an abrupt interface in Fig. 10. The lowering of potential in the range of 1-3 ML is explained by the surface energy of exposed Si. For an abrupt interface, the potential of the first epilayer is very low since the Ge replaces costly Si dangling bonds with less costly Ge ones. With intermixing, some Si is forced into the Ge epilayer by entropy, thus reintroducing some dangling Si bonds and raising the chemical potential. But subsequent epilayers participate in covering the exposed Si and are therefore lower in chemical potential. Consequently, the chemical potential with intermixing increases gradually from the first epilayer until complete coverage by Ge.

![](./images/812349675083399169_10.jpg)

FIG. 10. Tempered chemical potential for intermixed epilayers. With an abrupt interface, the chemical potential for 2 ML of flat epilayers exceeds that of an ideal island. With intermixing, the chemical potential for flat epilayers increases gradually with increasing coverage.

Comparing this tempered chemical potential to the island potential over a range of coverages reveals the onset of islanding. Figure 11 shows that the epilayer potential is lower for the first 3 ML of deposition. Beyond that thickness the island potential becomes lower. This result agrees very well with the experimentally observed onset of islanding. We believe this is the first direct calculation of the critical thickness for islanding of Ge on Si(001) based on atomistic simulation. Earlier work $^{24}$ sought to calculate the energy for epilayer growth with an abrupt interface but failed to capture the high energy of the second epilayer. $^{25,23}$ Intermixing is a key force in delaying the onset of islanding until the observed thickness.

### VI. CONCLUSIONS

We have presented a simple model for intermixing during the heteroepitaxy of Ge on Si(001). A flexible lattice Monte

![](./images/812349675083399169_11.jpg)

FIG. 11. Energetics of island formation. For the first 3 ML of deposition, flat epilayers are energetically favored. Beyond 3 ML, islands have lower potential.


Carlo simulation was devised to equilibrate the Ge epilayers with the underlying Si substrate. For coverages of 1 ML Ge, entropy counteracts the wetting nature of Ge and mixes the top two layers. Simulation of growth showed an abrupt in- terface at 1 K and a graded Ge composition at higher tem- peratures. The chemical potential was calculated for growth with mixing and compared to the chemical potential of py- ramidal islands, explaining the critical thickness for the onset of islanding.

## ACKNOWLEDGMENTS
Partial financial support by the National Science Founda- tion (Grant No. CTS-9985449) is gratefully acknowledged.

*Electronic address: wagnerr@umich.edu
$^{1}$D. Bimberg, M. Grundmann, and N.N. Ledentsov, *Quantum Dot Heterostructures* (Wiley, New York, 1999).
$^{2}$X.R. Qin, B.S. Swartzentruber, and M.G. Lagally, Phys. Rev. Lett. **84**, 4645 (2000).
$^{3}$K. Nakajima, A. Konishi, and K. Kimura, Phys. Rev. Lett. **83**, 1802 (1999).
$^{4}$K. Nakajima, A. Konishi, and K. Kimura, Nucl. Instrum. Methods Phys. Res. B **161-163**, 452 (2000).
$^{5}$D.-S. Lin, J.-L. Wu, S.-Y. Pan, and T.-C. Chiang, Phys. Rev. Lett. **90**, 046102 (2003).
$^{6}$X.R. Qin, B.S. Swartzentruber, and M.G. Lagally, Phys. Rev. Lett. **85**, 3660 (2000).
$^{7}$P.M. Fahey, P.B. Griffin, and J.D. Plummer, Rev. Mod. Phys. **61**, 289 (1989).
$^{8}$M. Copel, M.C. Reuter, M.H. von Hoegen, and R.M. Tromp, Phys. Rev. B **42**, 11 682 (1990).
$^{9}$J. Tersoff, Phys. Rev. B **39**, 5566 (1989).
$^{10}$H. Balamane, T. Halicioglu, and W.A. Tiller, Phys. Rev. B **46**, 2250 (1992).
$^{11}$K. Moriguchi and A. Shintani, Jpn. J. Appl. Phys., Part 1 **37**, 414 (1998).
$^{12}$W.H. Press, S.A. Teukolsky, W.T. Vetterling, and B.P. Flannery, *Numerical Recipes in C* (Cambridge University Press, Cam- bridge, 1997).
$^{13}$N.A. Metropolis, A.W. Rosenbluth, A.H. Teller, and E. Teller, J. Chem. Phys. **21**, 1087 (1953).
$^{14}$M.E.J. Newman and G.T. Barkema, *Monte Carlo Methods in Sta- tistical Physics* (Clarendon, Oxford, 1999).
$^{15}$A.-L. Barabási, Appl. Phys. Lett. **70**, 2565 (1997).
$^{16}$P. Sonnet and P.C. Kelires, Phys. Rev. B **66**, 205307 (2002).
$^{17}$P.C. Kelires and J. Tersoff, Phys. Rev. Lett. **63**, 1164 (1989).
$^{18}$P.C. Kelires, Phys. Rev. Lett. **75**, 1114 (1995).
$^{19}$J.-H. Cho and M.-H. Kang, Phys. Rev. B **61**, 1688 (2000).
$^{20}$Y. Yoshimoto and M. Tsukada, Surf. Sci. **423**, 32 (1999).
$^{21}$J. Drucker, IEEE J. Quantum Electron. **38**, 975 (2002).
$^{22}$A. Vailionis, B. Cho, G. Glass, P. Desjardins, D.G. Cahill, and J.E. Greene, Phys. Rev. Lett. **85**, 3672 (2000).
$^{23}$R.J. Wagner, Ph.D. thesis, University of Michigan, 2004.
$^{24}$J. Tersoff, Phys. Rev. B **43**, 9377 (1991).
$^{25}$K. Li, D.R. Bowler, and M.J. Gillan, Surf. Sci. **526**, 356 (2003).
