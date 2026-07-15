# Z methodology for phase diagram studies: platinum and tantalum as examples

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2014 J. Phys.: Conf. Ser. 500 162001

(http://iopscience.iop.org/1742-6596/500/16/162001)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 138.5.159.110
This content was downloaded on 16/04/2015 at 09:06

Please note that terms and conditions apply.

# Z methodology for phase diagram studies:
platinum and tantalum as examples

L Burakovsky¹, S P Chen¹, D L Preston² and D G Sheppard¹

¹ Theoretical and ² Computational Physics Divisions, Los Alamos National Laboratory, Los Alamos, New Mexico 87545

E-mail: burakov@lanl.gov

**Abstract.** The Z methodology is a novel technique for phase diagram studies. It combines the direct Z method for the computation of melting curves and the inverse Z method for the calculation of solid-solid phase boundaries. In the direct Z method, the solid phases along the melting curve are determined by comparing the solid-liquid equilibrium boundaries of candidate crystal structures. The inverse Z method involves quenching the liquid into the most stable solid phase at various temperatures and pressures to locate a solid-solid boundary. The direct and inverse Z methods in conjunction with the VASP *ab initio* molecular dynamics package are used to investigate the phase diagrams of tantalum and platinum. We compare our results to the most recent experimental data.

## 1. Introduction
The Z method was developed to calculate melting curves using first-principles based software, specifically VASP (Vienna Ab initio Simulation Package). The Z method was introduced for the first time in our paper on the *ab initio* melting curve of Mo [1]. The method has since been applied to the study of a large number of melting curves of different materials [2, 3, 4], and comparisons with experimental data on Pb [5], Ta [6], Fe [7], and Pt at ESRF [8] show good agreement. If a material has more than one thermodynamically stable crystal structure, the Z method yields the solid-liquid equilibrium boundaries of those structures. The phase having the highest solid-liquid equilibrium temperature over some pressure range is the most stable, thus the physical melting curve, including triple points, is the envelope of the solid-liquid equilibrium boundaries. We note that until recently, VASP could only be run for $NVE$ or $NVT$ ensembles, but with the release of the latest version, VASP5.3, we now have the option of running $NPT$, hence the so-called 2-phase simulations are now an alternative to the Z method.

For a number of materials, including Be, Fe, and Pt, the solid-liquid equilibrium boundaries of different solid phases are indistinguishable within mutual error bars because they have very close free energies. Consequently, the most stable structure cannot be determined using the Z method, and an alternative approach is needed.

## 2. Inverse Z methodology
To cope with this difficulty, and to locate solid-solid phase boundaries, we introduce a method complementary to the Z method, which we call the "inverse Z method." It consists of quenching the liquid into the most stable solid structure at a number of $(P,T)$ points to bracket a solid-solid

![](./images/814753403811921921_1.jpg)
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

Published under licence by IOP Publishing Ltd

![](./images/814753403811921921_2.jpg)

Figure 1. Typical isochore used in the Z methodology. Different segments of the isochore correspond to solid (AB), superheated solid (BC), liquid (DE), and supercooled liquid (DF) states. Melting corresponds to segment CD. Isochoric and isothermal solidification processes correspond to segments FB and GH, respectively.

phase boundary. The phase boundary determined in this way can be checked for consistency with the corresponding triple point found by the direct Z method. The inverse Z method for the calculation of solid-solid phase boundaries, along with the direct Z method for the calculation of melting curves, constitute the Z methodology for the complete study of phase diagrams, which we now discuss in detail.

Figure 1 shows a typical Z isochore ABCDE (3 green segments). It can be approximately mapped out by performing a sequence of ab initio molecular dynamics (AIMD) runs at progressively higher temperatures and pressures, typically 6-8 points, starting in the solid (segment AB), progressing to the superheated solid (segment BC), and finally to the liquid (segment DE). If the total energy in an AIMD run in the superheated solid is such that the equilibrium temperature $T < T_C$, the final state is on segment AC, but if $T > T_C$ the system melts and the final state is a point $(P_l,T_l)$ on segment DE above the melting curve; a further increase in the initial system energy moves the final state up segment DE. Ideally, the AIMD runs in the superheated solid would differ by only small temperature increments so that the upper vertex C would be precisely determined, and then a run starting from C would take the system to the point D on the melting curve, but generally this cannot be achieved in practice. The vertex D can only be bracketed from below by the highest calculated state $(P_s,T_s)$ on solid segment AB, and from above by the lowest state $(P_l,T_l)$ on liquid segment DE. We approximate the melting point as $(P_m,T_m)=((P_s+P_l)/2,(T_s+T_l)/2)$. The true melting point must be close to $(P_m,T_m)$ because the actual melting curve crosses the box formed by $P_m\pm(P_l-P_s)/2$ and $T_m\pm(T_l-T_s)/2$.

The inverse Z method is essentially this procedure carried out in reverse, but with an important variation discussed below. If one starts with liquid (segment DE) and could repeat this procedure in the opposite direction, the "mirror" image of the isochore ABCDE would be formed, namely, EDFBA. The vertices C and F are not necessarily symmetric with respect to the melting curve. It can be shown [9] that $T_C = T_m\left(1+\Delta S_m/C_V^S\right)$ and $T_F = T_m\left(1-\Delta S_m/C_V^L\right)$, where $\Delta S_m$ is the entropy of melting, and $C_V^S$ and $C_V^L$ are the solid and liquid heat capacities at constant volume. With the "canonical" values $\Delta S_m=R\ln 2$ and $C_V^S=3R$ [9], one gets $T_C=(1+\ln 2/3)=1.231T_m$. Since the value of $C_V^L$ lies between $3R$ for solid and $3R/2$ for ideal monatomic gas, one gets $T_m(1-2\ln 2/3)\leq T_F\leq T_m(1-\ln 2/3)$, or $0.538T_m\leq T_F\leq 0.769T_m$.

In the inverse Z method, one starts in the liquid (a point on DE) and then decreases the total energy so that the system becomes a supercooled liquid (segment DF). For system energies

such that the equilibrium temperature $T > T_F$, the final state will be on segment EF, but if $T < T_F$, the nature of the final state depends on whether $T_F$ is above or below the vitrification temperature $T_g$. If $T_F > T_g$ then the final state will lie on solid segment AB, but if $T_F \leq T_g$, the final state may either be a glass or remain a supercooled liquid. To ensure that the final state is always a solid, we employ a procedure which differs from simply reversing the direct Z method: we first supercool the liquid to point G (figure 1) and then continue running at fixed $T$ in an $NVT$ ensemble until the final solid state (point H) is reached. The passage from G to H proceeds with a reduction in total energy and pressure, which is the driving force for this process in the actual AIMD run.

Since the solidification kinetics is approximately governed by the factor $\exp\{\Delta F/T_{GH}\}$, where $\Delta F \equiv F_l - F_s$ is the liquid-solid free energy difference at the solidification temperature $T_{GH}$, in the case of several energetically competitive solid phases the most stable solid phase has the largest $\Delta F$ and is therefore the fastest to solidify. Hence, the inverse Z method yields the most stable solid phase at a given $(P,T)$.

In order to implement the inverse Z procedure correctly, one must ensure that (i) the solidification process is initiated, which requires an adequate degree of supercooling, and (ii) it is not hindered by geometric constraints on the computational cell. We have carried out extensive suites of inverse Z computations on the low-Z materials Be and C, for which AIMD simulations of systems of order 1000 atoms can be performed relatively fast, and found that requirements (i) and (ii) were always satisfied by imposing two simple criteria. As regards (i) we must choose $T_{GH}$ in the range $(0.55 - 0.85)T_m$, i.e. at least 15% supercooling to initiate solidification but less than 45% supercooling to remain above $T_g \sim 0.5T_m$. Regarding (ii), the computational cell must be sufficiently large, of order 500 atoms; the most stable solid phase may not fit into a smaller cell because of geometric constraints, and may in principle be replaced by a less stable structure during solidification.

The subsequent identification of the crystal structure of the final state can be done by means of a number of techniques: (i) comparison of radial distribution functions (RDFs); (ii) comparison of X-Ray diffraction patterns in reciprocal momentum space; (iii) geometric structure analysis (coordination number, angles between interatomic bonds, etc.). Two different final-state crystal structures at $(P_1,T_1)$ and $(P_2,T_2)$ then bracket the corresponding solid-solid phase boundary.

Let us now consider the practical implementation of the inverse Z method in two cases, namely, the phase diagrams of Pt and Ta, which we now discuss in detail.

### 3. Inverse Z methodology applied to the phase diagram of Pt
The phase diagram of Pt is of great importance because Pt is used as a pressure calibration standard in high-pressure studies. The melting curve of Pt was measured in a laser-heated diamond anvil cell (DAC) by Kavner and Jeanloz [10] (shown in figure 2), and turned out to be inconsistent with calculations [4]. This circumstance prompted Belonoshko and Rosengren to carry out AIMD simulations of the Pt melting curve using the direct Z method with VASP [4]. Their $fcc$ melting curve is much higher than that found by Kavner and Jeanloz, and has been confirmed in recent experiments by Errandonea [8].

If the true melting curve of Pt is that presented in [4] and [8], the question arises as to what was measured by Kavner and Jeanloz. To address this question, we carried out our own suite of AIMD simulations. We first recalculated the melting curve of $fcc$-Pt using the Z method, this time with a total of 18 valence electrons per atom (5s, 5p, 5d, and 6s orbitals), in contrast to 10 valence electrons per atom (5d and 6s alone) as in [4]. We used a 256-atom cell with a single $\Gamma$-point; full energy convergence (to $\lesssim 1$ meV/atom) was verified by performing short runs with $2 \times 2 \times 2$ and $3 \times 3 \times 3$ $k$-point meshes and comparing their output with that of the run with a single $\Gamma$-point. Our melting curve of $fcc$-Pt essentially coincides with that of [4], and is given by the formula ($T$ in K, $P$ in GPa) $T_m(P)=2042(1+P/44.3)^{0.85}$.

![](./images/814753403811921921_3.jpg)

Figure 2. Phase diagram of Pt obtained from combining the Z methodology with the $fcc$-$rhcp$ solid-solid phase boundary calculated using the approach of ref. [16]. The Pt melting curve obtained by Kavner and Jeanloz is also shown as dashed blue line.

![](./images/814753403811921921_4.jpg)

Figure 3. Phase diagram of Pt obtained from the Z methodology: $fcc$-Pt melting curve (green line), liquid Pt solidified into solid $fcc$ (green bullets), $9R$-Pt melting curve (blue line), liquid Pt solidified into solid $9R$ (blue bullets), and the (tentative) $fcc$-$9R$ solid-solid phase boundary (violet).

We then applied the inverse Z method to locate solid-solid boundaries. We used a computational cell of order 500 atoms (prepared by melting of both a $5 \times 5 \times 5$ solid $fcc$ cell and different solid hexagonal cells of similar size) with 18 electrons per atom in the valence, hence our systems had $\sim 9000$ electrons; to the best of our knowledge, AIMD simulations of this magnitude have never been previously undertaken. We carried out $NVT$ calculations using the Nosé-Hoover thermostat with a timestep of 1 fs. Complete solidification typically required 15-20 ps, or 15000-20000 timesteps; for comparison, equilibrium for a direct-Z $NVE$ run is typically achieved within 5000-10000 timesteps. We found that Pt solidifies into $fcc$ below the violet line in figure 3, while above this line it solidifies into a hexagonal structure. Extrapolation of this line to higher $P$ indicates that it crosses the melting curve at $\sim 300$ GPa. The RDFs did not allow us to discriminate between different hexagonal structures: $hcp$, $dhcp$ (double-$hcp$), $thcp$ (triple-$hcp$), $9R$ ($\alpha$-Sm). Upon fast quenching of the hexagonal structures to low $T$, where RDFs are more discriminating, we observed all four hexagonal structures. Hence, the inverse Z method indicates that there may be a number of energetically competitive hexagonal structures of Pt at high $PT$.

To clarify this issue, we calculated the solid-liquid equilibrium boundaries of all four hexagonal structures using the direct Z method with VASP. We ran cells of 250-300 atoms with 18 valence electrons per atom. All four solid-liquid boundaries turn out to be very close to each other (and to that of $fcc$-Pt). The solid-liquid boundary of $9R$-Pt is nominally the highest of all (yet the remaining boundaries are in agreement with the $9R$-Pt one within the error bars of the method, $\sim 100-200$ K), and is given by the formula $T_{m}(P)=1500(1+P/20.0)^{0.79}$, which is shown in figure 3 along with the $fcc$-liquid boundary: the two curves cross each other at $\sim 35$ GPa.

Our results indicate that structures with different stacking sequences ($AB...$ for $hcp$, $ABC...$ for $fcc$, $ABAC...$ for $dhcp$, $ABCACB...$ for $thcp$, and $ABCBCACAB...$ for $9R$) are energetically very close. Hence, the energy cost of forming a stacking fault between two such structures is virtually zero. Consequently, the actual layer stacking could be non-periodic and, in principle, random. A randomly disordered hexagonal close-packed ($rhcp$) structure was first introduced for hard-sphere colloids [11], and has since been the subject of literature discussions [12, 13]. In general, when different stacking sequences become energetically degenerate, that is,

![](./images/814753403811921921_5.jpg)

Figure 4. Phase digram of Ta obtained from the Z methodology: bcc-Ta melting curve (green), Pnma-Ta melting curve (blue), and the bcc-Pnma solid-solid phase boundary (red). The Ta shock Hugoniot and the RAMP compression (quasi-isentrope) curve are also shown as thin dashed blue and solid black lines, respectively.

the energy difference between any two such structures is $\sim 1-10$ meV per atom, or $\sim 10-100$ K, then in the resulting structure any two adjacent layers can occur with equal probability.

We are not aware of any references to elements with a rhcp structure. We note, however, that a rhcp phase may have been discovered experimentally in Au above 250 GPa by Dubrovinsky et al. [14]. Although their x-ray diffraction data indicate hcp, their first-principles calculations reveal small energy differences of $\sim 1$ meV/atom between hexagonal structures with different stacking sequences, though dhcp is favored. The most stable solid structure may be a mixture of hcp and dhcp, or of all of the hexagonal phases; in other words, it may be rhcp. We also note that a structure similar to rhcp was conjectured to be the most stable solid phase of Fe at Earth core PT conditions [15].

One can model the rhcp phase boundary of Pt by using the approach suggested by Boehler et al. [16]. Using their formula $T_d = T_m \{1 - x(1 - x)\}$ , where $T_m$ is the melting temperature of the disorder-free state, $T_d$ is the rhcp "melting" temperature, and $x = (P - P_L)/(P_U - P_L)$, with the Pt "lower crossing point" (L) and "upper crossing point" (U) values $P_L = 35$ GPa and $P_U = 300$ GPa gives the "melting" curve, $T_d(P)$, shown in figure 2. This "melting" curve is in good agreement with that found by Kavner and Jeanloz, also shown in figure 2.

## 4. Inverse Z methodology applied to the phase diagram of Ta
The phase diagram of Ta remains highly controversial. The discrepancy between the $\sim 300$ GPa melting temperatures observed in DAC $(\sim 4000$ K) and shock compression experiments $(\sim 10000$ K) has not been fully resolved. Previously we attempted to explain this discrepancy by associating the DAC melting curve with a solid-solid boundary, or with the onset of plastic flow driven by internal shear stresses associated with a solid-solid transformation and/or laser heating [2]. We identified another solid structure of Ta, namely, hexagonal omega (hex-$\omega$), as a candidate for its high-PT solid phase. This conclusion was disputed in [18] where it was argued that the hex-$\omega$ phase only stabilizes in a relatively small cell (in [2] we dealt with systems of order 100 atoms) and will destabilize in a larger cell and eventually become less stable than bcc.

To gain insight into these issues we have carried out a comprehensive study of Ta using the Z methodology. We first solidified Ta over a wide pressure range using the inverse Z technique. Liquid Ta was prepared by melting a 500-atom $(5 \times 5 \times 5)$ fcc-Ta cell. We found that above the red line shown in figure 4, Ta solidifies into an orthorhombic structure. Although the RDFs of this

structure and $bcc$ are similar at high $T$, they are clearly distinguishable when they are quenched to low $T$. A more detailed comparison of this orthorhombic structure with the $Pnma$-Ta that was very recently suggested by Yao and Klug [19] confirms that they are basically identical. We then carried out a suite of AIMD simulations of the solid-liquid boundaries of the $bcc$-Ta, hex-$\omega$-Ta, and $Pnma$-Ta phases using the direct Z method with computational cells of order 500 atoms. We discovered that: (i) at this cell size hex-$\omega$ melts below $bcc$, and is therefore less stable than $bcc$; (ii) the melting curve of $Pnma$-Ta crosses that of $bcc$-Ta at $\sim200$ GPa, which defines the location of the $bcc$-$Pnma$-liquid triple point; and (iii) extrapolation of the $bcc$-$Pnma$ transition line to lower $P$ is consistent with the location of the $bcc$-$Pnma$-liquid triple point from (ii). In figure 4 we also show the shock Hugoniot and the RAMP compression (quasi-isentrope) curve from recent LLNL experiments [20]. It is seen that the $bcc$-$Pnma$ transition is predicted to take place at $\sim220$ GPa on the Hugoniot, and at $\sim320$ GPa on the quasi-isentrope. We note that Kalitkin and Kuzmina predict a solid-solid transition on the Ta Hugoniot at 220 GPa (see page 109 in [21], and [22]), and LLNL experiments indicate a solid-solid transition on the quasi-isentrope at $300-350$ GPa [20].

## 5. Conclusions

To conclude, we have introduced a new approach, the Z methodology, for the computation of both melting curves and solid-solid phase boundaries. We have applied the Z methodology to the study of the phase diagrams of Pt and Ta, and our results compare favorably with the existing experimental data in both cases. These examples demonstrate that the Z methodology is a powerful utility for the calculation of phase diagrams. The limitation of this utility is that, as noted above, the inverse Z method detects a solid-solid phase boundary in the range $(0.55-0.85)T_m$ only. However, with the knowledge of the $T=0$ solid-solid transition points from the cold free-energy calculations, and of the solid-solid-liquid triple points from the direct Z method, complete solid-solid phase boundaries can be constructed.

## References

[1] Belonoshko A B *et al.* 2008 *Phys. Rev. Lett.* **100** 135701
[2] Burakovsky L *et al.* 2010 *Phys. Rev. Lett.* **104** 255702 and references therein
[3] Belonoshko A B *et al.* 2009 *Phys. Rev. B* **79** 220102(R)
[4] Belonoshko A B and Rosengren A 2012 *Phys. Rev. B* **85** 174104 and references therein
[5] Dewaele A, Mezouar M, Guignot N and Loubeyre P 2007 *Phys. Rev. B* **76** 144106
[6] Dewaele A, Mezouar M, Guignot N and Loubeyre P 2010 *Phys. Rev. Lett.* **104** 255701
[7] Anzellini S *et al.* 2013 *Science* **340** 464
[8] Errandonea D 2013 *Phys. Rev. B* **87** 054108
[9] Belonoshko A B, Skorodumova N V, Rosengren A and Johansson B 2006 *Phys. Rev. B* **73** 012201
[10] Kavner A and Jeanloz R 1998 *J. Appl. Phys.* **83** 7553
[11] Auer S and Frenkel D 2001 *Nature* **409** 1020
[12] Dolbnya I P *et al.* 2005 *Europhys. Lett.* **72** 962
[13] Byelov D V *et al.* 2010 *Phase Transitions* **83** 107
[14] Dubrovinsky L *et al.* 2007 *Phys. Rev. Lett.* **98** 045503
[15] Ishikawa T, Tsuchiya T and Tsuchiya J 2011 *Phys. Rev. B* **83** 212101
[16] Boehler R, Ross M, Söderlind P and Boercker D B 2001 *Phys. Rev. Lett.* **86** 5731
[17] Morgan J A 1974 *High Temp. - High Pres.* **6** 195
[18] Haskins J B, Moriarty J A and Hood R Q 2012 *Phys. Rev. B* **86** 224104
[19] Yao Y and Klug D D 2013 *Phys. Rev. B* **88** 054102
[20] Lazicki A, Eggert J and Rygg R 2013 FY12 LLNL OMEGA Experimental Programs *Livermore National Laboratory Tech. Rep.* LLNL-TR-607997
[21] Kalitkin N N and Kuzmina L V 2004 *High Pressure Shock Compression of Solids VII* Springer-Verlag, New York
[22] Ivanchenko E S, Kalitkin N N and Kuz'mina L V 2009 *Mathematical Models and Computer Simulations* **1** 383