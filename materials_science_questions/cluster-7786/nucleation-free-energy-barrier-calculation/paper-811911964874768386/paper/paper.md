# Hydrogen storage by spillover on graphene as a phase nucleation process

Yu Lin, Feng Ding, and Boris I. Yakobson*

Department of Mechanical Engineering and Materials Science and Department of Chemistry, Rice University, Houston, Texas 77005, USA

(Received 18 May 2008; published 14 July 2008)

Hydrogen chemisorption on graphene receptor-substrate is of great interest for energy storage. However, it is difficult to reconcile with a single H atom binding to carbon being weaker than it is within initial molecular $\text{H}_2$. This paradox is resolved by presenting the process as phase nucleation in the reaction $\text{Rec}^{\text{solid}}+\text{H}_2^{\text{gus}}\leftrightarrow(\text{H}\cdot\text{Rec})^{\text{solid}}$, with the nucleus' energy separable into the Gibbs formation potential and the interface part. Atomistic calculations bridge remarkably with the macroscopic-continuum description and show a feasible path to 7.7 wt % H content at nearly ambient conditions.

DOI: 10.1103/PhysRevB.78.041402
PACS number(s): 82.20.Wt, 64.60.Q−, 81.10.Aj

In the quest for clean energy carriers, hydrogen attracts special attention. Early reports of its adsorption on nanotubes¹ pointed to carbon as a promising storage medium and stimulated numerous studies. To store hydrogen efficiently, various carbon-based materials have been proposed—metal organic frameworks,² metal-decorated or boron-doped nanotubes, and fullerenes.³ Recent observations demonstrate that atomic H can bind reversibly (i.e., can be stored) to nanostructured carbon.⁴⁻⁶ The depth and reversibility of hydrogenation have been shown in cold hydrogen plasma experiments;⁵ in this case, H is in free atomic form and the $\varepsilon_b$=0.8 eV of its binding to nanotube⁷ does make chemisorption energetically favorable. In contrast, when in practice the initial gas is molecular, this 0.8 eV affinity to carbon cannot overweigh the strength of $\text{H}_2$ ($\frac{1}{2}E_{\text{H}_2}$=2.3 eV). Surprisingly, the rapidly growing bulk of evidence suggests exactly this: catalyst-assisted hydrogen chemisorption does occur on carbon,⁴ seemingly defying intuition and thus presenting a challenge to theory.

The term *hydrogen spillover* was coined decades ago⁸ to describe the transport of an active species (e.g., H) generated on one substance (activator, Act) to another (receptor, Rec) that would not normally adsorb it. Common in heterogeneous catalysis, the activator is metal and the receptor can be a metal or a metal oxide, $\text{H}_2\longrightarrow\text{Act}\rightarrow2\text{H}$, $\text{H}+\text{Rec}\rightarrow\text{H@Rec}$.⁸ The number of adsorbed H atoms can exceed that of the activator by orders of magnitude and approach the number of receptor atoms. This feature makes the spillover attractive for H storage: if a receptor is made from light elements, notably C, then the gravimetric fraction of the “spilled” H may be large and approach the Department of Energy’s goals in its use as an onboard energy source. While the catalyst does reduce the activation barrier, it cannot change the requirement for the overall process $\text{H}_2+\text{Rec}\rightarrow2\text{H@Rec}$ to go thermodynamically downhill: the binding $\varepsilon_b$ to carbon receptor must be stronger than $\frac{1}{2}E_{\text{H}_2}$ within $\text{H}_2$. This poses a compelling question about what configurations of chemisorbed H can be energetically favorable and how they can be reached starting from an initially pristine receptor. In other words, is it possible to suggest a physical picture of transition into these “storage” states?

To this end, we consider small groups of H on graphene, from 1, 2, 3, etc., atoms and to larger clusters, using *ab initio* methods. Although single H binding to graphene is weak, it strengthens dramatically as clusters begin to form, with the major factors being proper pairing in alternant hydrocarbons and the compensation of pyramidalization⁹ if the adjacent C atoms get hydrogenated from the opposite sides of graphene. The best binding is achieved for compact islands comprised of fully hydrogenated hexagons. Remarkably, the islands’ energy can be separated in two distinct contributions: the wetting energy, proportional to the island area $\sim l^2$, and the boundary energy, $\sim l$. This invokes an interpretation of spillover as nucleation of a new phase,¹⁰,¹¹ with the free energy $\sim-(-l^2+l)$, and accordingly defined critical size $l^*$ and the nucleation barrier $\Delta G^*$.

Relative to $\text{H}_2$, the formation energy for spillover is $\varepsilon_{\text{so}}$=$=-\varepsilon_b+\frac{1}{2}E_{\text{H}_2}$. Positive $\varepsilon_{\text{so}}$ means that chemisorption is energetically unfavorable; media with very small negative $\varepsilon_{\text{so}}$ still cannot retain H efficiently. On the other hand, a too negative $\varepsilon_{\text{so}}$ (e.g., $<-0.3$ eV) makes adsorption irreversible, unless at high temperature. Therefore, for good storage, $\varepsilon_{\text{so}}$ must lie within $-0.6$ eV$<2\varepsilon_{\text{so}}<-0.2$ eV. Since this range is rather narrow, the accuracy of calculations affects the conclusion whether H can be feasibly stored or not. After careful consideration of the methods and basis-set options (up to $6\text{-}311+G^{**}$ for some key results), we chose to conduct all the computations with the gradient-corrected correlation functional of Perdew, Burke, and Ernzerhof (PBEPBE), and the basis sets of $6\text{-}31G^{**}$ (Ref. 12) within GAUSSIAN03.¹³ Graphene was represented as either a polycyclic aromatic hydrocarbon cluster $\text{C}_{54}\text{H}_{18}$ [circumcoronene, Fig. 1(a)] or an infinite layer, treated with periodic boundary conditions (PBC).

For a cluster of $n$ chemisorbed H atoms, the average binding energy $\varepsilon_b(n)$ is
$$
\varepsilon_b(n)=(E_g+n\varepsilon_{\text{H}}-E_{n\text{H}@g})/n, \tag{1}
$$
where $E_g$ is the energy of either graphene or its fragment (e.g., $\text{C}_{54}\text{H}_{18}$), $\varepsilon_{\text{H}}$ is the energy of single H atom, and $E_{n\text{H}@g}$ is the total energy of hydrogenated graphene [e.g., $\varepsilon_b$=$\varepsilon_b(1)$]. We compute these quantities to observe some trends and regularities.

Similar to benzene, $\text{C}_6\text{H}_6$, $\text{C}_{54}\text{H}_{18}$ has an alternant conjugated system of the $sp^2$ carbon layer.¹⁴ According to the per-

![](./images/811911964874768386_1.jpg)

FIG. 1. (Color online) Structure and energy of one [(a) and (d)] or two [(b) and (c)] H atoms chemisorbed on $C_{54}H_{18}$. Six patterns with corresponding binding energies are shown (b), with two lowest-energy ortho configurations in (c) illustrating the lattice strain. Atoms adsorbed above/below the graphene are marked as solid/empty circles in (b). Bond angle and length changes induced by the H binding are shown in (d).

turbation molecular-orbital theory, $^{14}$ its atoms can be divided into two subgroups, one starred and another unstarred [Fig. 1(a)]. For an aromatic system, the $\pi$ electron of each starred/unstarred atom is paired with another $\pi$ electron of an unstarred/starred C according to the pairing theorem. $^{14}$ Adsorption of an H atom eliminates one $\pi$ electron; thus such a system has an odd number of $\pi$ electrons, one of them unpaired, i.e., a radical. This raises the total energy. Thus the binding energy 0.79 eV of the single H is small, 1.5 eV less than $\frac{1}{2}E_{H_{2}}$, too weak to drive the spillover.

Adding another H to the C of opposite subgroup removes the radical state and thus lowers the energy. In Fig. 1(b), two H atoms are added in six different ways: ortho, meta, and para, with the H's either on the same side or on the countersides of graphene [Fig. 1(c)]. In meta configuration, both H's are bound to C atoms from the same subgroup, which creates two radicals and results to weaker binding than in ortho and para.

Generally, reducing the number of unpaired $\pi$ electrons increases the binding energy. Since each $\pi$ pair consists of one $\pi$ electron from a starred and another from an unstarred C, for a given number of chemisorbed H, the binding is best if equal portions of H atoms are bound to the two subgroups. An odd number of H atoms yield at least one unpaired $\pi$ electron, destroying graphene's aromaticity. Consequently, the energy increments $\Delta E_{n}\equiv n\varepsilon_{b}(n)-(n-1)\varepsilon_{b}(n-1)$ for the odd$^{\text{th}}$ adsorbed H must be less than those for the even$^{\text{th}}$; Fig. 2(a) indeed shows such oscillations.

Further, the chemisorption of H alters the hybridization of the host C atom from $sp^{2}$ to $sp^{3}$. The C-C bonds between the $sp^{3}$ atom and its three nearest $sp^{2}$ neighbors are elongated to $\sim$0.15 nm and the angles between them are reduced from $120^{\circ}$ to $115^{\circ}$ [Fig. 1(d)], while the hydrogenated C atom buckles off the plane, in the course of pyramidalization. $^{9}$ If two adjacent C atoms are hydrogenated from the opposite sides, the induced strains compensate each other, reducing the energy. $^{15,16}$ Such configuration is more stable than the one with both H's attached on the same side. For example, the binding energy for the H's in ortho configuration increases to 1.70 eV if they are on countersides and from 1.47 eV if they are placed at the same side [Figs. 1(b) and 1(c)].

Although the binding energy for an H pair is greater than that of a single H, it still is $\sim$0.6 eV weaker than $\frac{1}{2}E_{H_{2}}$. Since the lattice strain around the two adsorbed H atoms is not fully relaxed, one expects that proper addition of more H atoms can further lower the total energy and strengthen the binding. This is plotted in Fig. 2(b) for a series of formations (some shown in Figs. 1 and 2) to display the steady increase from 0.79 eV for a single H, to 1.70 eV/H for a pair, to 2.16 eV/H for a sextet, and further to 2.35 eV/H for 24 adsorbed

![](./images/811911964874768386_2.jpg)

FIG. 2. (Color online) The aromaticity effect and closed six-ring preference for H chemisorbed on graphene. The energy increment $\Delta E_{n}$ due to $n$th atom sorption versus its number (a). In (b), binding energy per H for all clusters considered as a function of their size $n$. Illustrating some energy points, the insets show 3, 4, and 5 adsorbed H atoms, followed by the larger closed-ring structures with 6, 10, 16, and 24 atoms, and the infinite fully hydrogenated graphene. In (b), the thin line connects the most stable configurations to guide the eye.

![](./images/811911964874768386_3.jpg)

FIG. 3. (Color online) The computed energies of hydrogen bind- ing into compact aromatic clusters (with bound H atoms alternating at both sides of the graphene) depend linearly on the portion $n_{23}/n$ of $sp^{2}$-$sp^{3}$ bonds. The inset schematics show an activator-catalyst (black) next to the island of hydrogenated graphene (dark gray) on the receptor. Energies of H atom and the diffusion barriers several steps near the interface are shown on the right side.

atoms, which already is 0.05 eV/H more than $\frac{1}{2}E_{H_{2}}$. Ultimately, for a fully both-side hydrogenated graphene of composition CH, the binding energy reaches $\varepsilon_{b}(\infty)$=2.54 eV/H, exceeding $\frac{1}{2}E_{H_{2}}$ by 0.23 eV/H (as additionally confirmed in calculations with PBEPBE/6-311+G** method). This asymptotic value is close to the recent result by Sofo *et al.*, $^{17}$ ~0.15 eV/atom. In this structure, all C's have $sp^{3}$ hybridization, and the direct band gap of the fully hydrogenated graphene, 4.9 eV, is close to that of diamond, 5.5 eV. (The band gap from our full-electron calculation is noticeably larger than that calculated with pseudopotential, 3.5 eV. $^{17}$)

How such energetically favorable “monolayer diamond slab” can be reached in the course of chemisorption can be learned by inspecting Fig. 2. The formations with complete hydrogenated six-rings are more stable than others. In Fig. 2(a), the 3.5 eV affinity of the ring-closing sixth H atom is greater than that of the second or fourth one (~2.7 eV). Figure 2(b) further shows that configurations composed of six-rings (e.g., of 6H, 10H, 16H, and 24H@$C_{54}H_{18}$) have stronger binding than any others with incomplete six-rings, e.g., 12H. (This “closed-ring rule” distinctly differs from the belt formation on a thin nanotube, $^{16}$ where large wall curvature apparently controls the morphology of hydrogenation.)

The tendency of the chemisorbed H to crowd together brings about an important question as to whether a condensed two-dimensional (2D) island of H on graphene can be viewed as a new phase nucleus, as previously speculated. $^{16,18}$ Can its energy be separable into the “bulk” and boundary-interface contributions? To address this question explicitly, we distinguish three types of C-C bonds: those within pristine C sheet (connecting $sp^{2}$ atoms), those within fully hydrogenated graphene (between the $sp^{3}$ atoms), and the bonds tagged “23” (connecting $sp^{2}$ and $sp^{3}$ carbons) as the interface. With this in mind, we show in Fig. 3 the energies $\varepsilon_{b}(n)$ versus the fraction of border-type bonds, $n_{23}/n$, for several aromatic formations, with H adsorbed on both sides. The data points follow the line $\varepsilon_{b}(n)=\varepsilon_{b}(\infty)-\gamma\cdot(n_{23}/n)$ strikingly closely, with $\varepsilon_{b}(\infty)$=2.54 eV and $\gamma$=0.41 eV (deviation of <0.03 eV). It shows that the total formation energy of a spillover island can be decomposed $^{19}$ into its bulk contribution proportional to the number of H atoms, $n$, i.e., island area, and the “interface” term proportional to the number of border bonds $n_{23}\sim\sqrt{n}$, i.e., island perimeter,

$$
\begin{aligned}
\varepsilon_{\mathrm{so}}(n) n & \equiv\left[\frac{1}{2} E_{\mathrm{H}_{2}}-\varepsilon_{b}(n)\right] n=-\left[\varepsilon_{b}(\infty)-\frac{1}{2} E_{\mathrm{H}_{2}}\right] n+\gamma n_{23} \\
& =-0.23 n+1.01 \sqrt{n}, \text { in } \mathrm{eV}.
\end{aligned}
\tag{2}
$$

In the latter, we assume a nearly circular island to relate the size of perimeter with the number $n$ of chemisorbed H, $n_{23}$ $\approx\sqrt{6}n\sim l$. Integer $n$ is formally treated as continuum variable proportional to island's area or radius squared, $n\sim l^{2}$. We also compute the energies and the barriers for a diffusing H atom several sites away from the interface to quantify its kinetic affinity to the island (Fig. 3, right).

![](./images/811911964874768386_4.jpg)

FIG. 4. (Color online) Gibbs free energy of formation of a CH island in the graphene as a function of number of H, computed for different $P$ and $T$. The typical nucleation-type shapes are characterized by the critical nucleus size (number of atoms, $n^{*}$, or dimension $l^{*}$) and the nucleation barrier. The nearly vertical thin downward line corresponds to the atomic plasma, where the chemical potential is high and the nucleation barrier vanishes. The horizontal gray arrow indicates a possible role of the catalyst particle as a nucleation seed. The inset shows thermodynamic equilibrium line between the $H_{2}$ gas and the storage phase (CH).

It is then easy to recognize in Eq. (2) the signature energy dependence $\sim(-l^{2}+l)$ of a new phase nucleus. $^{10,11}$ Furthermore, an important generalization follows if a fixed value of $-\frac{1}{2}E_{\mathrm{H}_{2}}$ is replaced by a chemical potential $\mu_{\mathrm{H}}(P,T)$ of $H_{2}$ gas, $^{10}$ at pressure $P$ and temperature $T$. (Calculated vibrational frequencies of chemisorbed H are high, with corresponding factors $e^{-\hbar\omega/kT}\ll1$, and contribute negligibly to $\Delta G$ at practical temperatures.) Figure 4 shows the Gibbs free energy $\Delta G(n)=-[\varepsilon_{b}(\infty)+\mu_{\mathrm{H}}]n+\gamma\sqrt{n}$ of the spillover nucleus formation as a function of its size $n$, computed for different $T$ and $P$; it appears rather instructive. First, the inset equilibrium diagram shows when either free molecular gas [at $\Delta G(\infty)>0$] or a fully chemisorbed state [at $\Delta G(\infty)<0$] is

more favorable. It agrees reasonably with experiments⁵ of nanotube dehydrogenation upon raising $T$ to a few hundred degrees. It also shows that chemisorbed H is favored at ambient conditions, so that $sp^{2}$ carbon can in principle serve as good spillover receptor. At the same time, more detailed $\Delta G(n)$ curves display the nucleation barriers (distinct from the $H_{2}$ dissociation barrier, reduced by the metal catalyst), reflecting the fact that chemisorption of a single H is too weak to overweigh the strength of molecular $H_{2}$. In contrast, when the H source is plasma,⁵ $\mu_{\mathrm{H}}$ is very high and the nucleation barrier vanishes.

The barrier for homogeneous nucleation can be reduced by a seed,¹⁰,¹¹ which essentially shifts the initial size beyond the critical $l^{*}$ (or $n^{*}$), as indicated by the arrow in Fig. 4. Possible nucleation centers can be lattice defects or the metal particle itself, in which case it plays dual role: to lower the reaction ($H_{2}$ dissociation) transition state as a catalyst and to reduce the nucleation barrier. One can conjecture in this context that the observed role of bridges,⁴ although not yet microscopically studied, can be in improving the contact of the catalyst and effectively shifting the initial size to the larger (Fig. 4).

We discuss the molecular $H_{2}$ gas spillover/chemisorption on graphene, where H atoms tend to group into compact clusters, influenced by aromaticity rules and the pyramidalization strain, so that the "magic" (lowest-energy) clusters consist of closed six-hydrogen rings. The energy of chemisorbed clusters fits surprisingly well a continuum model of an island and can be decomposed into its bulk and "surface" (island boundary) contributions. Computed Gibbs formation energy $\Delta G^{P,T}(n)$ plots show typical phase nucleation dependencies, with the nucleation barrier $\Delta G^{*}$ and the critical size $n^{*}$ (or $l^{*}$) identified for arbitrary $P$ and $T$. An important corollary of this analysis is that the balance between the fluidic gas phase and the immobilized "7.7 wt % storage" phase can be changed in either direction by changing $P$ and $T$ not too far from the ambient conditions, thus permitting in principle reasonable refueling cycles. (The calculated energy gain by the hydrogenation of graphite under conservation of the graphene framework is not very large, which ultimately allows the reversibility.) Needless to say, the kinetic aspects, the processes' rates, and associated thermal effects-all not considered above-require further studies.

This work was supported by the DOE Hydrogen Sorption Center of Excellence, Contract No. DE-FC36-05GO15080, and partially by the Office of Naval Research (program manager Peter Schmidt). We thank Ralph Yang and Vincent Crespi for stimulating discussions.

*Corresponding author. biy@rice.edu

¹A. C. Dillon, K. M. Jones, T. A. Bekkedahl, C. H. Kiang, D. S. Bethune, and M. Heben, Nature (London) 386, 377 (1997); C. Liu, Y. Y. Fan, M. Liu, H. T. Cong, H. M. Cheng, and M. S. Dresselhaus, Science 286, 1127 (1999).

²N. L. Rosi, J. Eckert, M. Eddaoudi, D. T. Vodak, J. Kim, M. O'Keeffe, and O. M. Yaghi, Science 300, 1127 (2003).

³Y. Zhao, Y.-H. Kim, A. C. Dillon, M. J. Heben, and S. B. Zhang, Phys. Rev. Lett. 94, 155504 (2005); T. Yildirim and S. Ciraci, ibid. 94, 175501 (2005); Y. Kim, Y. Zhao, A. Williamson, M. Heben, and S. Zhang, ibid. 96, 016102 (2006); O. V. Pupysheva, A. A. Farajian, and B. I. Yakobson, Nano Lett. 8, 767 (2008).

⁴Y. Li and R. T. Yang, J. Am. Chem. Soc. 128, 726 (2006); Y. Li and R. T. Yang, ibid. 128, 8136 (2006); A. J. Lachawiec, G. S. Qi, and R. T. Yang, Langmuir 21, 11418 (2005).

⁵A. Nikitin, H. Ogasawara, D. Mann, R. Denecke, Z. Zhang, H. Dai, K. Cho, and A. Nilsson, Phys. Rev. Lett. 95, 225507 (2005).

⁶G. Zhang, P. Qi, X. Wang, Y. Lu, D. Mann, X. Li, and H. Dai, J. Am. Chem. Soc. 128, 6026 (2006).

⁷L. Hornekær, Z. Sljivancanin, W. Xu, R. Otero, E. Rauls, I. Stensgaard, E. Lægsgaard, B. Hammer, and F. Besenbacher, Phys. Rev. Lett. 96, 156104 (2006); L. Hornekær, E. Rauls, W. Xu, Z. Sljivancanin, R. Otero, I. Stensgaard, E. Lægsgaard, B. Hammer, and F. Besenbacher, ibid. 97, 186102 (2006).

⁸W. C. Conner and J. J. L. Falconer, Chem. Rev. (Washington, D.C.) 95, 759 (1995); M. Boudart and G. D.-.Mariadassou, Kinetics of Heterogeneous Catalytic Reactions (Princeton University Press, Princeton, NJ, 1984).

⁹R. C. Haddon, J. Phys. Chem. 91, 3719 (1987); R. C. Haddon, Science 261, 1545 (1993).

¹⁰L. D. Landau and E. M. Lifshitz, Statistical Physics (Butterworth, Oxford, 1995).

¹¹J. W. Christian, The Theory of Transformations in Metals and Alloys (Pergamon, New York, 2002).

¹²J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

¹³M. J. Frisch et al., GAUSSIAN 03, Revision C.02 (Gaussian, Inc., Wallingford, 2004).

¹⁴M. J. S. Dewar and R. C. Dougherty, The PMO Theory of Organic Chemistry (Plenum, New York, 1975).

¹⁵S. M. Lee, K. H. An, Y. H. Lee, G. Seifert, and T. Frauenheim, J. Am. Chem. Soc. 123, 5059 (2001).

¹⁶D. Stojkovic, P. Zhang, P. E. Lammert, and V. H. Crespi, Phys. Rev. B 68, 195406 (2003).

¹⁷J. O. Sofo, A. S. Chaudhari, and G. D. Barber, Phys. Rev. B 75, 153401 (2007).

¹⁸M. H. F. Sluiter and Y. Kawazoe, Phys. Rev. B 68, 085410 (2003).

¹⁹N. Gonzalez Szwacki and B. I. Yakobson, Phys. Rev. B 75, 035406 (2007).