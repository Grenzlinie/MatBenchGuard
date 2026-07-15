# Transition from Icosahedral to Decahedral Structure in a Coexisting Solid-Liquid Nickel Cluster

D. Schebarchov$^{1}$ and S. C. Hendy$^{1,2}$

$^{1}$MacDiarmid Institute for Advanced Materials and Nanotechnology,
School of Chemical and Physical Sciences,
Victoria University of Wellington, New Zealand

$^{2}$Industrial Research Ltd, Lower Hutt, New Zealand

(Dated: November 7, 2018)

## Abstract
We have used molecular dynamics simulations to construct a microcanonical caloric curve for a 1415-atom Ni icosahedron. Prior to melting the Ni cluster exhibits static solid-liquid phase coexistence. Initially a partial icosahedral structure coexists with a partially wetting melt. However at energies very close to the melting point the icosahedral structure is replaced by a truncated decahedral structure which is almost fully wet by the melt. This structure remains until the cluster fully melts. The transition appears to be driven by a preference for the melt to wet the decahedral structure.


It is well known that in small fcc clusters, noncrystalline structures such as icosahedra and decahedra can become stable as the total surface energy becomes comparable to the energy of the interior [1]. Similarly, in small coexisting solid-liquid clusters [2, 3] the energy of the solid-liquid interface makes a substantial contribution to the total energy of the cluster, and can strongly influence cluster properties [4, 5, 6]. For example, to avoid the cost of forming the interface, small clusters tend to avoid static coexistence. This leads to an S-bend in the microcanonical caloric curve [7], and the corresponding negative heat capacities observed in small sodium clusters [8]. In fact, in sufficiently small clusters static solid-liquid coexistence may not occur at all [9] allowing only a dynamic coexistence between the solid and liquid phase [6]. However, in larger clusters, just above this threshold, where the cost of forming the interface is significant but not prohibitive, it may be that the solid component assumes new structures in order to form a more favorable interface with the liquid component. This would have interesting consequences for the interpretation of premelting features in cluster caloric curves [10], and may also offer new ways of controlling cluster structures.

Indeed, the delicate balance of internal and surface energies that produce icosahedra and decahedra is further upset in a coexisting cluster by the fact that the solid region is reduced in size. While the fully solid cluster may be in the size range where one structure is stable, the smaller solid cluster coexisting with the liquid may be in a size range where another structure is stable. It is possible that a rich variety of structures may be observed in coexisting solid-liquid clusters as new energetic balances are established, and it is not difficult to imagine a sequence of structural transitions as the liquid fraction of the solid-liquid cluster increases. There may be some experimental evidence for such a scenario: Koga et al [19] have recently reported the observation of an icosahedral to decahedral transition in free gold particles as they were annealed close to their melting temperatures. It was suggested that this was a thermally activated transition driven by cluster thermodynamics. However, it is quite possible that the gold particles were in a coexisting solid-liquid state at temperatures just below the melting point, and in this case the solid-liquid interface may well have played a key role in the structural transition.

In this letter we report the transition of the solid region in a coexisting solid-liquid nickel cluster from a partial icosahedron to a decahedron. We have applied molecular dynamics simulations to construct a caloric curve for a 1415-atom cluster using an embedded atom method (EAM) potential [11]. Initially we attempted to identify the stable structure at

zero temperature by comparing the potential energies of closed-shell truncated octahedra (including variants such as the (TO)⁻ and (TO)⁺ structures [12]), cuboctahedra, icosahedra, and Marks [13] and Ino decahedra [1]. In figure 1 we show the relaxed energies for the icosahedra sequence and the Marks decahedra sequence relative to a fit to energies of the truncated octahedra sequence. In Ni we find that below 2869 atoms the icosahedral structures are lowest in energy, between 2869 and 12298 atoms the decahedral sequence is more stable and above 12298 atoms the fcc truncated octahedra become favorable. This is similar to the structural sequence predicted in Ref [14] using the same potential, although there it was estimated that fcc structures would become stable at sizes of 17000 atoms. From figure 1, we note that the icosahedron should be stable at a cluster size of 1415-atoms but that the 1389-atom Marks decahedron and the 1289-atom truncated octahedron are only slightly less favorable energetically. Thus a 1415-atom nickel cluster would seem to be a good candidate for observing structural transitions during solid-liquid coexistence.

A previous molecular dynamics study of solid-liquid coexistence in a 1289-atom nickel truncated octahedron [15] found partial wetting of the solid by the melt (with the solid exposing a solid lens consisting of (111)-facets) and then full wetting at temperatures closer to the melting point (with the solid completely covered by the melt). This study also used the same EAM potential as our simulations. Other molecular dynamics simulations of coexistence in metal clusters have studied copper [16], gold [12] and lead [9].

The caloric curves were constructed in the constant energy (microcanonical) ensemble using the following procedure: at each fixed total energy the cluster was equilibrated for 150000 time steps (where $\Delta t = 2$ fs) and then the kinetic energy was averaged over a further 150000 steps to obtain a temperature. An energy increment of 0.6 meV/atom was used to adjust the total energy between simulations by a uniform scaling of the kinetic energy. This corresponds to a heating rate of 1 meV/atom/nanosecond. To identify and characterize solid-liquid coexistence, we follow Cleveland et al [15], using the bimodality of the distribution of diffusion coefficients to distinguish solid and liquid atoms. We have previously used this method in Ref [9] to characterize the coexisting solid-liquid states in Pb clusters.

Figure 2 shows the resulting caloric curve for the 1415-atom icosahedron. At total energies below $E = -3.82$ eV/atom the cluster is fully solid. The onset of coexistence occurs at energies above just this. For energies between $E = -3.82$ eV/atom and $E = -3.77$ eV/atom the structure of the cluster is that of an incomplete icosahedron partially wetted by a region

of melt: figure 3 compares the icosahedron structure prior to heating with snapshots of the coexisting cluster at $E=-3.78$ eV/atom with the liquid atoms shaded in dark (center), and then removed (right). In the coexisting structure it is possible to distinguish 6 nearly complete tetrahedra of the 20 that make up a full icosahedron. This structure is very similar to the icosahedral solid-liquid structures seen in molecular dynamics simulations of lead clusters [9]. We note that the region of exposed (111)-facets of the icosahedron do not resemble a lens in the sense of Ref [15], where it used to refer to a patch of exposed solid surrounded by liquid in a nearly wetted cluster.

At approximately $E=-3.77$ eV/atom a transition occurs. This is visible in the caloric curve by the sudden increase in temperature at this energy indicating that the cluster has lowered its potential energy. Note that the snapshot in figure 3 is taken just prior to this transition at $E=-3.78$ eV/atom. In figure 4 we show snapshots from immediately after the transition. The top left snapshot shows exposed (111)-facets of the solid; the top right snapshot, looking at the opposite side of the cluster, shows no exposed solid. The region of exposed crystal facets is much more lens-like than in the case of the icosahedron with the melt appear to wet the solid more completely, although analysis of the distribution of diffusion coefficients suggests the liquid fraction has dropped slightly. In the bottom pictures, a common neighbor analysis [17] (CNA) has been performed using the index classification from Ref [18] to identify the structure of the solid region. The liquid atoms have been removed to show only atoms with fcc or hcp symmetries. Two angles are shown: looking down the fivefold axis of the solid (bottom left) and looking side on to this axis down one of the twin planes (bottom right). The structure closely resembles that of a five-shell Marks decahedron [13]. We conclude the that transition seen at $E=-3.77$ eV/atom in the caloric curve (figure 2) is a transition of the solid from an incomplete icosahedron to a complete decahedron.

Figure 5 shows a second caloric curve constructed by first heating from $E=-3.83$ eV/atom to $E=-3.76$ eV/atom and then cooling back to $E=-3.83$ eV/atom at the same rate. The transition from icosahedron to decahedron occurs at $E=-3.766$ eV/atom, which is close to the transition in the first caloric curve (figure 1) suggesting that this is a good estimate of the transition energy. However we note in figure 5 that upon cooling there is no transition back to the icosahedron. Presumably, the decahedron is kinetically trapped, a common occurrence in both simulations and real clusters [19]. The the decahedron is fully

solid at approximately $E = -3.79$ eV/atom. Note that the temperature of the decahedron falls below that of the icosahedron at $E = -3.80$ eV/atom; at this energy both clusters are solid indicating that the solid icosahedral structure has a lower potential energy than the decahedron consistent with the zero temperature calculations (figure 1).

Also shown in figure 5 are the number of atoms in bulk fcc positions (obtained via CNA analysis of the cluster structure) as the cluster is heated and cooled. During the heating phase the number of bulk fcc atoms steadily declines (as the solid fraction of the icosahedron decreases) until the transition at $E = -3.766$ eV/atom. At this point the number of bulk fcc atoms ($N_{fcc}$) jumps sharply as the transition to the decahedral structure occurs. Upon cooling $N_{fcc}$ increases (as the solid fraction increases) until coexistence ceases at about $E = -3.79$ eV/atom where it can be seen that $N_{fcc}$ becomes relatively static. In a perfect 1389-atom Marks decahedron (that is a relaxed structure at zero temperature) CNA analysis counts $N_{fcc} = 650$ and in a perfect 1415-atom icosahedron CNA analysis counts $N_{fcc}=400$. Both the decahedral and icosahedral structure approach these values by $E = -3.83$ eV/atom.

To test whether the location of the transition depends on cooling rate we conducted longer 4 ns (2 million steps) constant energy simulations of the icosahedron at several energies near the transition point in the caloric curve. In figure 6 we show the time evolution of the temperature and the number of fcc atoms in the $E = -3.77$ eV/atom simulation. Here the transition is seen to occur at $t = 3.65$ ns where an increase in $N_{fcc}$ and a jump in the temperature is visible. We see no such transition in 4 ns simulations at $E = -3.78$ eV/atom and $E = -3.775$ eV/atom. This again suggests that we have a good estimate of the transition energy.

There are several known instances where solid clusters undergo structural transitions prior to melting. Small gold clusters have been seen in simulations to undergo transitions from truncated-octahedral structures, which are globally stable at zero temperature, to icosahedral structures at energies just below the melting point [20]. Similarly a study of icosahedral Morse clusters found complex surface reconstructions prior to melting [21]. In these cases, the transitions are driven by the thermodynamics of the solid phase rather than contact with a melt. However it is unlikely that similar thermodynamics are driving the transition seen here as the transition is accompanied by an decrease in potential energy of about 10 meV/atom (corresponding to the rise in temperature that can be seen in figure 2).

This decrease in potential energy of the overall cluster comes from the contribution of surface atoms which drop on average by 40 meV/atom after the transition; it seems likely that this comes from an improvement in the solid-liquid interfacial energy associated with the wetting of the decahedral structure. We note that the interior atoms actually experience a net increase in potential energy of approximately 10 meV/atom. As remarked earlier, a previous study of phase coexistence in Ni clusters found a preference for fcc cuboctahedral cluster to expose (111)-facets (lenses) to the vacuum or vapour [15], suggesting a preference for the melt to wet the (100)-facets. Molten lead is known to have a preference to wet crystalline lead (100)-facets over the (111)-facets [22] and the structure of the coexisting icosahedron in figure 3 strongly resembles the coexisting icosahedron structure seen in simulations of lead [9]. It is possible that the higher-energy (100)-facets on the decahedron offer an improved solid-liquid interfacial energy over the (111)-facets; this is hard to verify directly due to the dificulty in defining the solid-liquid interface in such a small system.

At cluster sizes near 1400 atoms, the EAM potential [11] predicts that several structures possess very similar energies, including the icosahedron and the decahedron (with a size of 1389 atoms). Indeed the transition occurs between an incomplete icosahedron and a decahedron. In simulations of Ni clusters at other sizes [23], we have observed static solid-liquid coexistence in a 923-atom icosahedron (but not in cluster sizes below this) and we did not observe this transition to a decahedral structure.

We conclude that we have found a structural transition that occurs in the solid part of a coexisting solid-liquid nickel cluster modelled using an EAM potential. We believe this is the first suggestion that structural changes can occur in solid clusters to accommodate a coexisting melt. This effect may explain the recent observation of a icosahedral to decahedral transition seen in free gold particles [19] as they were annealed close to the melting point and it could provide an important kinetic mechanism for controlling the structure of nanoscale metal nanoparticles.

The authors would like to acknowledge financial support from the MacDiarmid Institute for Nanotechnology and Advanced Materials.

[1] S. Ino, J. Phys. Soc. Jpn 27, 941 (1967).

[2] S. Pochon, K. F. MacDonald, R. J. Knize and N. I. Zheludev, Phys. Rev. Lett. 92, 145702

(2004).

[3] J.-G. Lee and H. Mori, Phys. Rev. B. 70, 144105 (2004).

[4] H. Reiss P. Mirabel, and R. L. Whetten, J. Phys. Chem. 92, 7241-7246 (1988).

[5] D. J. Wales and R. S. Berry, Phys. Rev. Lett. 73, 2875 (1994).

[6] J. D. Honeycutt and H. C. Andersen, J. Phys. Chem. 91, 4950 (1987).

[7] R. M. Lynden-Bell and D. J. Wales, J. Chem. Phys. 101, 1460 (1994).

[8] M. Schmidt, R. Kusche, T. Hippler, J. Donges, W. Kronmuller, B. von Issendorff, and H. Haberland, Phys. Rev. Lett. 86, 1191-1194 (2001).

[9] S. C. Hendy, Phys. Rev. B 71, 115404 (2005).

[10] G. A. Breaux, C. M. Neal, B. Cao and M. F. Jarrold, Phys. Rev. Lett. 94, 173401 (2005).

[11] S. M. Foiles, M. I. Baskes and M. S. Daw, Phys. Rev. B 33, 7983-7991 (1986).

[12] C. L. Cleveland, W. D. Luedtke and U. Landman, Phys. Rev. B 60, 5065-5077 (1999).

[13] L. D. Marks, Rep. Prog. Phys. 57, 603 (1994).

[14] C. L. Cleveland and U. Landman, J. Chem. Phys. 94, 7376-7396 (1991).

[15] C. L. Cleveland, U. Landman and W. D. Luedtke, J. Phys. Chem. 98, 6272-6279 (1994).

[16] O. H. Nielsen, J. P. Sethna, P. Stoltze, K. W. Jacobsen, and J. K. Norskov, Europhys. Lett. 26, 51-56 (1994).

[17] A. S. Clarke and H. Jonsson, Phys. Rev. E 47, 3975 (1993).

[18] S. C. Hendy and J. P. K. Doye , Phys. Rev. B 66, 235402 (2002).

[19] K. Koga, T. Ikeshoji and K. I. Sugawara , Phys. Rev. Lett. 92, 115507 (2004).

[20] C. L. Cleveland, W. D. Luedtke, and U. Landman, Phys. Rev. Lett. 81, 2036-2039 (1998).

[21] J. P. K. Doye and D. J. Wales, Zeit. Phys. D 40, 466 (1997).

[22] B. Pluis, A. W. Denier van der Gon, J. W. M. Frenken and J. F. van der Veen, Phys. Rev. Lett. 59, 2678-2681 (1987).

[23] D. Schebarchov and S. C. Hendy, to appear in J. Chem. Phys. (2005).

![](./images/867745181783294165_1.jpg)

FIG. 1: Comparison of the relaxed zero temperature energies of icosahedra, Marks decahedra and truncated octahedra for nickel. Energies are given relative to a fit to the energies of the truncated octahedra sequence.

![](./images/867745181783294165_2.jpg)

FIG. 2: Caloric curve for the 1415-atom icosahedron. The onset of coexistence occurs at an energy of approximately $E=-3.81$ eV/atom. There is a second transition at $E=-3.77$ eV/atom, followed finally by melting at $E=-3.755$ eV/atom.

![](./images/867745181783294165_3.jpg)

FIG. 3: The figures show icosahedron prior to heating (left) and the coexisting solid-liquid icosahedron at $E = -3.78$ eV/atom just prior to the transition (center and right). In the center the liquid atoms are shown in a darker shade. Note that the liquid only partially wets the solid, exposing (111)-facets, whereas if the liquid completely wet the solid then there would be no solid exposed. On the right, the liquid atoms have been removed to show only the solid.

![](./images/867745181783294165_4.jpg)

FIG. 4: The plots show the coexisting solid-liquid decahedron at $E=-3.77$ eV/atom just after the transition. In the top two snapshots, taken from opposite viewpoints, the liquid atoms are shown in a darker shade. In the bottom snapshots, the liquid atoms have been removed and CNA analysis has been used to highlight the twin planes of the decahedron. On the bottom left the viewpoint is down the fivefold axis of the decahedron. On the right the picture is looking side on to one of the twin planes.

![](./images/867745181783294165_5.jpg)

FIG. 5: The plot shows a second caloric curve where the cluster is heated (solid lines) until the icosahedral to decahedral transition and then cooled (dashed lines). Also shown is the corresponding the number of fcc atoms (as calculated by CNA analysis) in the cluster.

![](./images/867745181783294165_6.jpg)

FIG. 6: The plot shows the time evolution of the temperature and number of fcc atoms in the cluster as it goes through the transition from icosahedron to decahedron at $E=-3.77$ (eV/atom).