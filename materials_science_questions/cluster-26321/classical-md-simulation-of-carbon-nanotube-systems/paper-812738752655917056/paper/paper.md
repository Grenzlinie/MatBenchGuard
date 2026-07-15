# Electronic Transport through Carbon Nanotubes: Effects of Structural Deformation and Tube Chirality

Amitesh Maiti,¹,* Alexei Svizhenko,²,† and M. P. Anantram²

¹Accelrys Inc., 9685 Scranton Road, San Diego, California 92121
²NASA Ames Research Center, Mail Stop: T27A-1, Moffett Field, California 94035-1000
(Received 24 September 2001; published 11 March 2002)

Atomistic simulations using a combination of classical force field and density-functional theory (DFT) show that carbon atoms remain essentially $sp^2$ coordinated in either bent tubes or tubes pushed by an atomically sharp atomic-force microscope (AFM) tip. Subsequent Green’s-function-based transport calculations reveal that for armchair tubes there is no significant drop in conductance, while for zigzag tubes the conductance can drop by several orders of magnitude in AFM-pushed tubes. The effect can be attributed to simple stretching of the tube under tip deformation, which opens up an energy gap at the Fermi surface.

DOI: 10.1103/PhysRevLett.88.126805
PACS numbers: 73.63.Fg, 61.46.+w, 62.25.+g, 85.35.Kt

Tremendous potential for technological applications has thrust carbon nanotubes into one of the hottest areas of research activity. This has been fueled by recent experimental breakthroughs in diverse application areas [1], ranging from flat panel displays, to novel microelectronic devices, to hydrogen storage devices, to structural reinforcing agents, to chemical and electromechanical sensors. A pioneering experiment in the last application area involved a metallic nanotube suspended over a 600 nm long trench [2]. When the middle part of such a suspended nanotube was pushed with the tip of an atomic force microscope (AFM), the conductivity was found to decrease by nearly 2 orders of magnitude for a deformation angle of $15^\circ$. The effect was found to be completely reversible, i.e., through repeated cycles of AFM deformation and tip removal, the electrical conductance displayed a cyclical variation with constant amplitude.

The drop in conductance in the AFM-deformed tube was much higher than the computationally predicted values for tubes bent under mechanical duress. Such calculations, using both tight-binding [3] and semi-empirical Extended-Hückel type approaches [4] concluded that even under large bending angles the reduction in electrical conductance was less than an order of magnitude. For AFM-deformed nanotubes, in contrast, O(N) tight-binding calculations [5] show that beyond a critical deformation several C atoms close to the AFM tip become $sp^3$ coordinated. The $sp^3$ coordination ties up delocalized $\pi$ electrons into localized $\sigma$ states. This would naturally explain the large drop in electrical conductivity, as verified by explicit transport calculations.

Under either bending or pushing by an atomically sharp AFM tip, bond reconstruction, if any, is likely to occur only in the highly deformed, nonstraight part of the tube in the middle. This prompted us to use a DFT-based quantum mechanical description of the middle part of the tube (~100 atoms), while the long and essentially straight part away from the middle was described accurately using the universal force field (UFF) [6,7]. Structures and energetics obtained this way for bent tubes were in good agreement with previous work using an interatomic potential [8]. For the AFM tip-deformed tubes, on the other hand, the situation depended on how the tip was represented. Thus, if the presence of the tip was simulated by constraining a single C atom on the bottom side of the middle part of the tube, simulations on a (5,5) armchair led to the development of $sp^3$ coordination between the constrained atom and an atom on the top side at a critical deformation angle of $\sim7^\circ$, which destabilized into a complex broken-bond defect at higher deformation angles [9]. On the other hand, a more realistic representation of the AFM tip by means of an atomically sharp 15-atom Li needle yielded an $sp^2$-coordinated all-hexagonal tube for deformation angles as high as $25^\circ$ for the same (5,5) tube [10]. A large drop in conductance is expected under $sp^3$ coordination and broken bond defects [5,9]. However, given the uncertainty of $sp^3$ coordination, can one still expect a significant conductance drop in a tip-deformed, yet $sp^2$-coordinated tube?

In this Letter, we address the above question by extending the combined DFT-UFF calculations to a (12,0) metallic zigzag tube. For comparison, we have also considered a (6,6) armchair tube, which is slightly smaller in diameter, but has the same number of atoms (12) along the tube circumference as the (12,0) zigzag. The main result of structural relaxation using DFT-UFF is that $sp^3$ coordination does not happen under either bending or tip deformation (using an atomically sharp 15-atom Li tip as in Ref. [10]) up to very large angles. Following structural relaxation at each bending and deformation angle, we compute the electronic density of states (DOS), transmission, and conductance using the recursive Green’s function method [11]. For the armchair tube, the resulting conductance is lowered only by a factor of 1.01 for the tube bent by $40^\circ$ and a factor of 1.05 for a tube tip deformed by $25^\circ$. Under the same deformations, drop in conductance, for the zigzag tube, is much higher, being a factor of 1.9 under bending, and a remarkable $1.7\times10^4$ under tip deformation.

The simulations were carried out on tubes of 2400 atoms, both for the (6,6) and (12,0) tubes. Initially the straight

tube was relaxed with the UFF. For bending simulations,
two halves of the tube were then rotated by equal and
opposite angles about an axis perpendicular to the tube and
passing through the center of mass of the initial straight
tube. At each end of the tube, a contact region defined by
a unit cell [12] plus one atomic ring (a total of 36 and 60
atoms for the armchair and the zigzag tube, respectively)
was then fixed and the whole tube relaxed with the UFF. To
simulate AFM tip deformation, the 15-atom Li needle was
initially aimed at the center of a hexagon on the bottom
side of the middle part of tube. The Li needle was then
displaced by an amount $\delta$ toward the tube along the needle-
axis, resulting in a deformation angle $\theta = \tan^{-1}(2\delta/L)$,
$L$ being the unstretched length of the tube. The whole
tube was then relaxed by UFF keeping the needle atoms
and the end contact regions of the tube fixed. Fixing the
relative positions of contact region atoms at the same value
as in an unstretched tube guarantees that contacts may be
approximated by ideal undeformed semi-infinite carbon
nanotube leads and that all possible contact modes are
coupled to the deformed part of the tube.

Following the UFF relaxation, a cluster of 132 C atoms
for the (6,6) and a cluster of 144 C atoms for the (12,0)
were cut out from the middle of the tubes. These clusters,
referred to below as the QM clusters (plus the 15 Li-tip
atoms in tip-deformation simulations) were further relaxed
with Accelrys' DFT-code DMol$^3$ [13], with the end atoms
of the cluster plus the Li-tip atoms fixed at their respec-
tive classical positions. The electronic wave functions in
DMol$^3$ were expanded in a double-numeric polarized
(DNP) basis set with a real-space cutoff of $4.0$ Å. The
Hamiltonian was approximated with the Harris functional
[14] using a local exchange-correlation potential [15], and
the "medium" grid was chosen for numerical integration.

Figure 1 displays the tip-deformed QM cluster for the
(6,6) and the (12,0) tubes at the highest deformation angle
of $25^\circ$ considered in these simulations. Even under such
large deformations, there is no indication of $sp^3$ bonding
[16], similar to what was observed for the (5,5) tube in
Ref. [10]. Although not explicitly shown here, results for
bending also yield $sp^2$-coordinated all-hexagonal tubes.
The absence of $sp^3$ coordination is inferred based on an
analysis of nearest neighbor distances of the atoms with
the highest displacements, i.e., the ones on the top of the
kink in a bent tube, and the ones closest to the Li tip in a
tip-deformed tube. Although for each of these atoms the
three nearest neighbor C-C bonds are stretched to between
$1.45$-$1.75$ Å, the distance of the fourth neighbor, required
to induce $sp^3$ coordination is greater than $2.2$ Å for all
tubes in our simulations. The main difference between
a tip-deformed tube versus a bent tube is that there is an
overall stretching in the former [17], whereas in the latter
case there is no net stretching, and the extra compressive
strain on the bottom side is relieved through the formation
of a kink beyond a critical bending angle.

Following atomic relaxation of the structures, we per-
formed conductance calculations in order to make further
![](./images/812738752655917056_1.jpg)

FIG. 1. DMol$^3$-relaxed Li-tip-deformed QM clusters for (a) the
(6,6) armchair (132 C atoms); and (b) the (12,0) zigzag (144 C
atoms), in side views. The deformation angle is $25^\circ$ for both
tubes. (c) and (d) are respective views along the tube length,
with the Li-tip hidden for clarity.

predictions on the electromechanical behavior of nano-
tubes. A coherent conductance was studied within a
nearest-neighbor $sp^3$ tight-binding Hamiltonian in a non-
orthogonal basis. The parametrization scheme explicitly
accounts for effects of strain in the system through a bond-
length-dependence of the Hamiltonian and the overlap
matrices $H_{ij}$ and $S_{ij}$, as in Ref. [18]. We have also
checked to confirm that other tight-binding parametriza-
tions give qualitatively the same results [19,20]. First, the
retarded Green's function $G^R$ of the whole nanotube was
determined by solving the following equation:

$$(E \cdot S_{ij} - H_{ij} - \Sigma_{L,ij}^R - \Sigma_{R,ij}^R)G^{R,jk} = \delta_i^k, \quad (1)$$

where $\Sigma_{L,R}^R$ are the retarded self-energies of the left and
the right semi-infinite contacts. The transmission and the
electronic density of states (DOS) at each energy were then
found [21,22] from the equations

$$T(E) = G^{R,ij}\Gamma_{L,jk}G^{A,kl}\Gamma_{R,li}, \tag{2}$$

$$N_\alpha(E) = -\frac{1}{\pi}\text{Im}\{S_{\alpha j}G^{R,j\alpha}\}, \tag{3}$$

where $\Gamma_{L,R} = i(\Sigma_{L,R}^R - \Sigma_{L,R}^A)$ are the couplings to the left
and right leads. Finally, the total conductance of the tube
was computed using the Landauer-Büttiker formula:

$$G = \frac{2e^2}{h}\int_{-\infty}^{\infty} T(E)\left(-\frac{\partial f_0}{\partial E}\right)dE, \tag{4}$$

where $f_0(E)$ is the Fermi-Dirac function.

Figure 2 displays the computed conductance (at $T =$
300 K) for the (6,6) and the (12,0) tubes as a function

![](./images/812738752655917056_2.jpg)

FIG. 2. Computed conductance (at $T=300$ K) for the (6,6) and (12,0) nanotubes as a function of (top) bending; and (bot- tom) tip deformation. Under $40^{\circ}$ bending conductance of the zigzag tube drops by a factor of 1.9, while for the armchair tube it drops by only 1.01. Under $25^{\circ}$ tip-deformation, conductance of the zigzag tube drops by 4 orders of magnitude, while for the armchair tube it drops only by a factor of 1.05.

of bending and tip-deformation angles. The conductance remains essentially constant for the (6,6) tube in either bending or tip-deformation simulations. However, for the (12,0) tube the conductance drops by a factor of 1.9 under bending at $\theta=40^{\circ}$ , and much more significantly under tip deformation: by $\sim 0.3$ at $15^{\circ}, 2$ orders of magnitude at $20^{\circ}$ , and 4 orders of magnitude at $\theta=25^{\circ}$ [23].

To analyze which part of the zigzag tube is responsible for the conductance drop, we computed the DOS in the vicinity of the Fermi surface. Figure 3 displays the DOS averaged over 2 unit cells [11] (96 atoms) in three differentregions of the AFM-deformed (12,0) tube for $\theta=25^{\circ}$ :(1) undeformed contact, (2) highly deformed tip region, and (3) the uniformly stretched straight regions on either side of the tip-deformed region. DOS in both tip region and the straight part show a band-gap opening, which proves that the conductance drop occurs everywhere in the tube, rather than in the tip-deformed region alone. This has im- portant implications for the application of nanotubes as electromechanical sensors: given a metallic zigzag nano- tube, one could induce a significant conductance drop sim- ply upon uniform stretching. To check this, we computed the conductance of a uniformly stretched (12,0) tube as a function of strain, shown in Fig. 4, and compared it to that of AFM-deformed tube from Fig. 2. Both cases show quan- titatively the same drastic decay of conductance. The inset of Fig. 4 also shows a band gap opening in transmission in the two cases [24], compared to that of a nondeformed tube.

In order to explain the differences in conductance of the(6,6) and the (12,0) tubes as a function of strain, we have analyzed the band structures of a metallic zigzag and an armchair nanotube. Starting from the band structure of the2D graphene [25] under deformation [26], one can derive the following dispersion relations for the crossing sub- bands within the $\pi$ -electron approximation ( $a'$ below is thestrained periodic repeat length along the nanotube axis):

$$
E(k)= \pm t_{2}\left\{1+\alpha^{2}-2 \alpha \cos \left(\frac{\sqrt{3} k a^{\prime}}{2}\right)\right\}^{1 / 2} \quad(5 \mathrm{a})
$$

for a metallic zigzag tube, and

$$
E(k)= \pm t_{2}\left|1-2 \alpha \cos \left(\frac{k a^{\prime}}{2}\right)\right| \quad(5 \mathrm{~b})
$$

for an armchair tube. Here, $\alpha=t_{1} / t_{2}$ is the ratio of nonequivalent hopping parameters. For a zigzag tube, $\alpha>1$ . Consequently, there is no value of $k a'$ for which E(k) =0 [for dispersion (5a)], and a band gap opens up. However, for an armchair tube, $\alpha<1$ and one can always find a value of k a', such that E(k)=0 [for dispersion(5b)], as long as $\alpha>1 / 2$ . The magnitude of the strain induced bandgap decreases monotonically with increase inchiral angle [26], being maximum for a chiral angle of $0^{\circ}$ (zigzag) and gradually reducing to zero at a chiral angle of30° (armchair). An experiment as in Ref. [2] is, thus, ex- pected to show a decrease in conductance as the nanotube is deformed with an AFM tip, for all nanotubes except the armchair tube. The decrease in conductance should be the largest for the metallic zigzag nanotubes, and smaller for nanotubes with a chiral angle closer to armchair.

In summary, we find that both under bending and un- der deformation with an atomically sharp AFM tip, car-bon nanotubes essentially remain all hexagonal and $sp^{2}$  coordinated. In the absence of $s p^{3}$ coordination, arm chair tubes remain significantly conducting even at large deformations. However, metallic zigzag tubes display a dramatic drop in conductance, particularly under tip de- formation. A density of states analysis indicates that the

![](./images/812738752655917056_3.jpg)

FIG. 3. Density of states, averaged over two unit cells (96 at- oms) in three different regions of AFM-deformed (12,0) tube at $\theta=25^{\circ}$ . The Fermi surface is at E=0. Nearly equal band gaps open up in the straight part of the tube and in the tip region. Lower DOS in the tip region is due to a larger local straining of C-C bonds close to the AFM tip.

![](./images/812738752655917056_4.jpg)

FIG. 4. Conductance of the uniformly stretched (12,0) tube compared to that of the tip-deformation case in Fig. 2. Actual angles of tip deformation are indicated. The % strain for the AFM-deformed tube is computed from the average C-C bond- stretch in the middle of the straight portion of the tube [17]. The inset shows transmission in the vicinity of the Fermi surface ($E = 0$) for a uniform strain of 10% and a tip-deformation angle of $25^\circ$, as compared to the undeformed tube.

conductance drop is distributed over the whole tube, rather than focused in the tip region. This suggests the possibil- ity of designing nanoelectromechanical sensors in which nanotubes are subjected to a uniform tensile strain.

A.M. would like to acknowledge Accelrys Inc. for its support. A.S. and M.P.A. would like to acknowledge NASA for funding the development of the 2D Quantum Device Simulator used for the conductance calculations in this paper. M.P.A. acknowledges useful discussions with Michael J. Mehl [18].

*Corresponding author.
Email address: amaiti@accelrys.com
†Corresponding author.
Email address: svizhenk@nas.nasa.gov

[1] Articles on nanotubes in Phys. World 13, 29-53 (2000).
[2] T.W. Tombler et al., Nature (London) 405, 769 (2000).
[3] M. Nardelli and J. Bernholc, Phys. Rev. B 60, R16 338 (1999).
[4] A. Rochefort, P. Avouris, F. Lesage, and D. Salahub, Phys. Rev. B 60, 13 824 (1999).
[5] L. Liu et al., Phys. Rev. Lett. 84, 4950 (2000).
[6] A.K. Rappe et al., J. Am. Chem. Soc. 114, 10 024 (1992).
[7] N. Yao and V. Lordi, J. Appl. Phys. 84, 1939 (1998).
[8] S. Iijima, C. Brabec, A. Maiti, and J. Bernholc, J. Chem. Phys. 104, 2089 (1996).
[9] A. Maiti, Chem. Phys. Lett. 331, 21 (2000).
[10] A. Maiti, Phys. Status Solidi B 226, 87 (2001).
[11] A. Svizhenko, M.P. Anantram, T.R. Govindan, B. Biegel, and R. Venugopal, J. Appl. Phys. 91, 2343 (2002).
[12] For computation of self-energies of semi-infinite carbon nanotube contacts in Eq. (1), it was convenient to partition the whole tube in adjacent repeating segments, or "unit cells." For an armchair and a zigzag tube, respectively, the unit cell consists of two and four rings of atoms around the circumference. This implies 24 atoms for the (6,6) tube and 48 atoms for the (12,0) tube per unit cell.
[13] B. Delley, J. Chem. Phys. 92, 508 (1990); J. Phys. Chem. 100, 6107 (1996); http://www.accelrys.com/ mstudio/dmol3.html
[14] J. Harris, Phys. Rev. B 31, 1770 (1985).
[15] S.H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys. 58, 1200 (1980).
[16] For a 110-atom QM cluster out of a 1000-atom (5,5) tube, we have also performed calculations in which the AFM tip was modeled with a capped (5,5) nanotube as in Ref. [5]. The resulting structures were slightly more $sp^2$ relaxed than that obtained with the atomically sharper Li tip. In addition, the $sp^2$-coordinated QM cluster deformed either with a Li-tip or a capped (5,5) tube was lower in $DMol^3$ energy than the $sp^3$-coordinated, highly strained cluster in the constrained-atom case.
[17] For a tube with a very large length-to-diameter ratio, the length $L$ stretches to $\sim L\sec\theta$, $\theta$ being the tip-deformation angle. However, for moderately long tubes used in our simulations, the average tensile strain in the straight part of the tube is slightly lower than $(\sec\theta - 1)$.
[18] D.A. Papaconstantopoulos, M.J. Mehl, S.C. Erwin, and M.R. Pederson, in Proceedings of the Symposium on Tight- Binding Approach to Computational Materials Science, edited by P.E.A. Turchi, A. Gonis, and L. Colombo (Ma- terials Research Society, Warrendale, PA, 1998), Vol. 491.
[19] J.-C. Charlier, Ph. Lambin, and T.W. Ebbesen, Phys. Rev. B 54, R8377 (1996).
[20] W.A. Harrison, Electronic Structure and the Properties of Solids (Dover, New York, 1989).
[21] In the Eqs. (1)-(3), summation is performed over the re- peating roman indices. The lower and upper indices denote covariant and contravariant components of a tensor.
[22] D. Lohez and M. Lanoo, Phys. Rev. B 27, 5007 (1983).
[23] For the (12,0) tube, we also studied the dependence of conductance drop as a function of tube length. Thus at a tip-deformation angle of $15^\circ$, tubes of 2400, 3600, and 4800 atoms have conductance drops of 0.29, 0.13, and 0.10, respectively, which extrapolates to $\sim$0.08 for very long tubes.
[24] A. Heyd, A. Charlier, and E. McRae, Phys. Rev. B 55, 6820 (1997).
[25] J.W. Mintmire and C. White, Carbon (Elsevier Science Ltd., New York, 1995), Vol. 33, No. 7, pp. 893-902; M.S. Dresselhaus, G. Dresselhaus, and P.C. Eklund, Science of Fullerenes and Carbon Nanotubes (Academic Press, New York, 1996).
[26] For electromechanical properties of tubes of any chirality and definition of $t_1,t_2,t_3$, see L. Yang, M.P. Anantram, J. Han, and J.P. Lu, Phys. Rev. B 60, 13 874 (1999).