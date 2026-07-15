INTERFACE SCIENCE, 2, 7-16 (1994).
© Kluwer Academic Publishers, Boston. Manufactured in The Netherlands.

# A New Type of Periodic Boundary Condition Useful for High-Temperature Atomistic Simulations of Grain Boundaries: Applications in Semiconductors

O.B.M. HARDOUIN DUPARC AND M. TORRENT

Laboratoire des solides irradiés, CEA-CEREM, CNRS-URA 1380, Ecole Polytechnique, F-91128 Palaiseau Cedex, France

**Keywords:** Boundary conditions, grain boundaries, atomic simulations, silicon, structural transition

**Abstract:** A new type of boundary condition, named Möbius or antiperiodic boundary conditions, is proposed and tested, both analytically and within the context of numerical simulations. It is shown that these boundary conditions are very useful for twist grain boundary atomistic simulations. By contrast to the use of the ordinary Born von Kármán periodic boundary conditions, they allow only one grain boundary per box instead of two. The risk of migration and overinteraction of two grain boundaries at high temperature is thus avoided while more complex grain boundaries can also be tackled at the same computer price. Such examples are presented and discussed.

## 1. Introduction

Owing to the continuing increase of computer power, it is now possible to tackle the study of both realistic and complex grain boundaries and even to monitor their behavior at high temperature via numerical simulations: Monte Carlo Metropolis and molecular dynamics. This is of special interest when there are reasons to believe that entropy effects may play a major role. For instance, it has recently been suggested by experimentalists that some grain boundaries in silicon and germanium may undergo significant solid structural changes at high temperature. Such candidates are the tilt $\Sigma=11(2\overline{3}3)$ [001]($\theta=50.48^\circ$)[1], $\Sigma=13$ (510) [001] ($\theta=22.62^\circ$) and $\Sigma=25$ (710) [001] ($\theta=16.26^\circ$) [2, 3]. The $\Sigma=11$ would double its coincidence site lattice period while the $\Sigma=13$ and the $\Sigma=25$ would oscillate between equivalent variants. As these hypotheses are based on high-resolution electron microscopy (HREM) observations performed on low-temperature samples, it seems natural to check them further with high-temperature numerical simulations.

Unfortunately, the possibility for a grain boundary to migrate randomly at high temperature constitutes a special problem in numerical simulations because of the use of the Born von Kármán (BVK) periodic boundary conditions (PBCs). These latter conditions force the simulators to put two equivalent grain boundaries, of opposite directions, per simulated box. For obvious economical reasons, the box is taken as small as possible. In the direction perpendicular to the grain boundary plane, the minimum requirement is that the box be large enough so that the two grain boundaries only negligibly influence each other. For instance, for low-angle grain boundaries the use of de Saint-Venant's principle [4] allows one to show that their mutual interaction will be small provided the distance between the grain boundaries is larger than or equal to the in-plane periodicity of the grain boundary [5]. At high temperature, however, if one of the two grain boundaries starts migrating, it may approach the other boundary and start interacting strongly with it. This may limit the reliability of long-time atomistic simulations at high temperatures. Also, even if migration is unlikely, as

for semiconductors, having two equivalent grain boundaries in a box multiplies the number of atoms by two in a nonessential way. It increases the CPU time by at least a factor of two, and it also doubles the amount of work for the subsequent graphic analyses.

In this article, we present an economical way to simulate only one twist grain boundary per box. We shall first describe our solution, which makes use of a new type of periodic boundary condition. We then proceed to test the qualification of these new boundary conditions with respect to BVK conditions and we finally apply them to the high-temperature study of the $\Sigma 11$ ($2\overline{3}3$) [011] symmetric tilt grain boundary.

## 2. A New Type of Periodic Boundary Condition
One way to simulate only one grain boundary is to forget about PBCs in the direction perpendicular to the grain boundary plane and to extend the grains far enough up to a point where they can be coupled to static perfect crystals. Because the direct coupling to static lattices is undesirable for high-temperature simulations, this scheme introduces artificial interfaces between static and dynamic regions. Its implementation is far from being trivial and computationally cheap [6].

Staring at the very special relation two twist grain boundaries have with respect to each other in a BVK box, it occurred to us that it would be possible to apply a new type of periodic boundary condition on a box half the size containing only one grain boundary. This relation between the two grain boundaries simply corresponds to a rotation around the normal axis to the grain boundary plane followed by a translation along that normal axis. As the translation is the periodic operation performed to implement the BVK PBCs, it should thus suffice to couple this translation with a rotation in order to achieve the requested new type of boundary condition. In the case of a symmetric tilt grain boundary, the angle of the rotation is $180^\circ$. As the BVK PBCs are frequently visualized in two dimensions as a torus, one can similarly oversimplify these new PBCs in the case of a symmetric tilt grain boundary with the image of a Möbius strip. We shall consequently name them **Möbius periodic boundary conditions**.

## 3. Validation of the Möbius PBCs
In the same way that the BVK PBCs had to be validated in their time, it is equally important to validate these new PBCs. We probed them both analytically on a simple harmonic system and numerically via Monte Carlo and molecular dynamic simulations.

### 3.1. Analytic Check
Analytically, it appears that the sampling of normal modes of lattice vibrations for a finite system is discrete and depends on the choice of boundary conditions: fixed ends, free ends, BVK periodicity, or Möbius periodicity. Each gives different samplings of wave vectors but Ledermann's theorem [7] ensures that the frequency spectra are essentially equivalent provided the number of bulk atoms versus the number of boundary atoms along the propagation direction be large. To give an illustration with a very simple case, let us consider the spectrum of transverse vibrational modes associated with a harmonic linear chain composed of $N$ beads. The beads all have the same mass and are coupled between first nearest neighbors via equivalent springs with an equilibrium distance $a$. In the case of periodic boundary conditions, one looks for progressive solutions $u_n = u_0 e^{i(\omega t - k n a)}$, with the conditions $u_{n+N} = \pm u_n$. The $+$ sign corresponds to BVK PBC and the $-$ sign to Möbius PBC. This immediately gives the quantization conditions on the $k$ modes, modulo $2\pi$: either $k N a = 0$ or $k N a = \pi$. Thus, solving Newton's first law, one gets $\omega(k_j) = \omega_c \cdot |\sin(k_j a/2)|$ where $\omega_c$ depends simply on the spring constant and the mass of the beads, and $k_j = 2 j \pi/N a$ (BVK PBC) or $(2j+1)\pi/N a$ (Möbius PBC). The two sets of solutions are represented in the $[0, 2\pi/a]$ interval in figure 1 for the $N = 8$ case. Although the selected modes are not the same, the $\omega_j$ all lie on the same curve and their densities are essentially equivalent and will be all the more so as $N$ is large. One can easily check that this conclusion also holds with fixed ends or free ends, as is guaranteed by Ledermann's theorem. We do not do it here as we are only interested in periodic boundary conditions.

![](./images/812339051796365313_1.jpg)

Figure 1. The selected transverse vibrational modes of an 8-atom linear harmonic chain, for two types of periodic boundary conditions: the BVK modes $k_j=2j\pi/8a$, $j=0,7$(-----) and the Möbius modes $k_j=(2j+1)\pi/8a$, $j=0,7$ (----).

### 3.2. Numerical Check

For the numerical check, we consider a three-dimensional box to which we apply the Möbius conditions in the $y$-direction as follows: the coordinates of the Möbius image of an atom of coordinates $(x,y,z)$ will be
$$
\begin{align*}
x' &= -x + \Delta x \\
y' &= y + L_y \\
z' &= -z + \Delta z
\end{align*}
$$

$L_y$ is the length of the (Möbius) box in the $y$-direction; and $\Delta x$ and $\Delta z$ are two constants which can always be fixed to zero via a proper centering of the box.

Given our subsequent interest in silicon, we chose to simulate a perfect diamond silicon lattice with the Stillinger-Weber potential (see below), using the same box with either the usual PBCs or the new ones. The cubic box contains 512 atoms. We performed several successive 10,000 step molecular dynamics runs both in the Newtonian (NVE) and the Nosé (NVT) ensemble [8,9] at an averaged temperature of about 1,000 K. The integration time step is 1.5 femtoseconds in real time. The equilibrium properties (energy, temperature, pressure, and their fluctuations) proved to be independent of the type of periodic boundary conditions. We also probed the root-mean-square atomic displacements along the three crystallographic $\langle 100 \rangle$ axes, either averaged on the whole box or averaged over $5$ Å thick slices perpendicular to the $y$-direction. The values obtained on both PBC cases remain the same up to $1\%$, with the same isotropy and homogeneity. The latter point is specially valuable as it means that there is no boundary effect, which is exactly what one expects from periodic boundary conditions.

The next step is to consider inhomogeneous systems such as grain boundaries. The results of these calculations are mainly given in the next paragraph. Here we comment only on the comparison of the Möbius PBCs against the usual BVK ones. Möbius boxes containing grain boundaries have first been checked for the minimized static energies. We used both simulated annealing Monte Carlo [10] and the quasi-molecular dynamics algorithms [11]. These techniques are specially useful when many local minima exist that may impair standard gradient minimization techniques. It is useful to be able to check that both minimization algorithms lead to the same results when the analytic

derivation and the programming of the atomic forces become involved, as with angle dependant potentials for instance. The two types of PBCs fortunately lead to exactly the same minimized energies provided the BVK boxes are twice as large as the Möbius boxes, as one would expect. For high-temperature simulations of various grain boundaries performed on Möbius boxes, we oc- casionally checked that they showed similar evo- lutions when redone on BVK boxes.

We also implemented and numerically checked the Möbius conditions on another kind of an- gular dependent potential, namely, the Tersoff potential (see below).

### 3.3. Historical Note
As expected, we later found that the idea had actually already been proposed in the past, at least once, in 1974 [12]. It had then been named "symmetry modified periodic borders." Unfortu- nately, its authors did not try to implement it and even rejected it, alleging that for grain bound- aries it could lead to wrong extensive variables in static calculations. We do not understand this assertion since it is perfectly obvious that the first of the extensive variables, namely, the static energy, can only be the same for a Möbius box and a BVK box once correctly minimized: as we have demonstrated, the BVK box contains two equivalent grain boundaries, which are sim- ply the Möbius images of one another. We have confirmed this point in detail.

## 4. Applications to the Study of Grain Boundaries in Silicon

### 4.1. Considerations about the Potentials
The directionality of the bonds in tetrahedral semiconductors is pronounced with a character- istic $\cos^{-1}(-1/3)$ angle for the diamond struc- ture. Pair additive potentials, which are purely radial, thus fail to reproduce such a noncompact structure as the most stable one. One needs po- tentials with angle dependent terms which can be provided for by simple three-body terms. Over 40 such potentials have been proposed by now to model silicon. One of the first, the Keating potential [13, 14], was closely adjusted to the diamond structure in the sense that it is a first-order measure of any departure from that tetrahedral structure. It is therefore limited to basic equilibrium properties such as elastic wave constants. Some other potentials more adapted to high-temperature atomic simulations have been devised since. One of the most pop- ular is the Stillinger-Weber (SW) potential [15]. It is a purely empirical potential, shaped to favor the diamond structure, but not as a first-order paradigm, and is endowed with seven parame- ters which have been fitted on both the diamond structure and liquid properties. Among the more recent classical potentials proposed, the Tersoff potential looks more sophisticated in the sense that it tries to both capture some quantum me- chanical considerations considering the strength of a bonding within a given environment and respect the "polymorphous perversity of silicon" [16-18]. It only has pairwise looking interactions which are nonsymmetric, noncentral, and conse- quently not purely two-bodied [13]. In its latest version, labeled here Tersoff C, it has 13 parame- ters fitted to include acceptable elastic properties. It seems to cope better with the liquid structure than the previous versions.

It is clear that none of these classical potentials is perfect, but, although many-bodied, they are still relatively easy to use. The quantum mechan- ical ab initio total energy calculations would be preferable as a state of the art, but they are very expensive from a computer point of view and can certainly not be used to perform long simu- lation runs on systems containing a few hundred atoms. The tight-binding molecular dynamics could become a third way but is still computer time demanding. We thus believe that for large systems and long simulation runs, relatively reli- able classical potentials are still worth using.

### 4.2. Tests on the Perfect Silicon Lattice
We have written both Monte Carlo and molec- ular dynamics codes with BVK and/or Möbius PBCs for the two types of aforementioned angu- lar many-body potentials, namely, SW and Ter- soff C. We checked them vis à vis their thermal

![](./images/812339051796365313_2.jpg)

Figure 2. Thermal expansion of the silicon lattice parameter: black triangles (▲▲▲): experimental values [20]; plus signs (+ + +): our results, SW potential; simples ×s (× × ×): our results, Tersoff C potential.

expansion coefficients and the root-mean-square atomic displacements (RMSADs).

The thermal expansion of the cubic diamond lattice parameter is plotted in figure 2. Our results for the SW potential perfectly coincide with [19]. The Tersoff C potential gives values slightly too large. The thermal expansion coefficient is $2.8\ 10^{-6}\text{K}^{-1}$ for SW and $5.6\ 10^{-6}\text{K}^{-1}$ for Tersoff C. The experimental value turns out to be in between, namely slightly over $4\ 10^{-6}\text{K}^{-1}$ for temperatures above 700 K [20]. At low temperatures in the 20-120 K range, silicon shrinks very slightly [20]. Our potentials do not reproduce this low-temperature peculiarity. Let us also just mention that the Keating potential dramatically contracts at all temperatures on heating.

The root-mean-square atomic displacements values are plotted in figure 3. The only two experimental values we have been able to find in the literature come from an X-ray diffraction analysis using high-order reflections [21]. The two curves which best fit these experimental points come from theoretical calculations of the phonon frequencies and their eigenvectors over the whole Brillouin zone using for instance a shell model for silicon [22] or the local Heine-Abarenkov pseudopotential model for silicon [23]. The lower curve is based on an expansion of the dynamical matrix, mainly valid at low temperature, and uses the Keating potential [24]. Our numerical values have been obtained from cubic boxes containing 1,728 atoms. The Tersoff and the SW potentials give almost identical results. They thus lead to the same value for the Lindemann-Gilvarry criterion [25, 26], namely $d = \sqrt{\langle u_i^2 \rangle}/d_{nn} = 0.075$ at the experimental melting temperature (1,684 K). $d_{nn}$ is the nearest neighbor distance at 0 K. It is worth mentioning that the SW potential has its thermodynamical melting temperature around 1,700 K [19, 27, 28]. It mechanically melts [29] at 2,400-2,500 K, whereas the Tersoff potential only does so at 2,900-3,000 K. The RMSADs $\sqrt{\langle u_i^2 \rangle}$

![](./images/812339051796365313_3.jpg)

Figure 3. Root-mean-square atomic displacements of silicon atoms versus temperature: black triangles (▲▲): Aldred and Hart (experimental) [21]; open circles (○○○): Reid and Pirie [22]; open squares (□□□): Soma and Matsuo [23]; simple ×s (×××): our work (SW); open triangles (△△△): Theeten and Dobrzynski [24].

have been probed along all the ⟨100⟩, ⟨110⟩, and ⟨111⟩ directions. Conversely looking at the low-temperature results, the simulated values look acceptable down to 300 K, which is about half the Debye temperature. However good these results seem to be, it is important to recognize that the atomic mean square displacements correspond to an averaging over all the vibrational modes accessible to the system. As such, they may overlook significant differences and weaknesses among the various potentials. A selective study of several vibrational modes and their Grüneisen parameters constitutes a more severe test [30].

### 4.3. Application to Grain Boundaries

We then used these codes to get the zero Kelvin atomic configurations for several different grain boundary structures. We used both quasi-molecular dynamics and simulated annealing Monte Carlo. One obtains the minimized interfacial energy $\gamma$ and the rigid body displacement (RBD) for each structure. Here we only give the results related to the two experimentally observed structures of the tilt $\Sigma=11(2\overline{3}3)$ [011] ($\theta=50.48^\circ$), respectively labeled $\Sigma11$A and $\Sigma11$B. A double period of $\Sigma11$A, named $\Sigma11$AD, is shown in figure 4 as a ball and stick representation projected along the [011] direction. Each vertex corresponds to a column of silicon atoms. It has a zig-zag structure made of oriented $5+7$ atom ring motifs, or structural units (SUs), which can be named $M^-$ and $M^+$, separated by neutral 6 atom rings named T. It is important to realize that this SU description is limited in two ways. First it is only a local description which does not tell you the value of the RBD between the two grains. The value of the RBD must be measured directly from the atomic positions of the bulk atoms of each grain. Second, although for instance all T-looking SUs

![](./images/812339051796365313_4.jpg)

Figure 4. $\Sigma11$AD structure. Möbius box. The vertical line is a guide to the eye to locate grain boundary plane.

will be labeled T, it is clear that they are not exactly the same from one grain boundary to an- other one, and even within one grain boundary, they will depend on their immediate neighbor- hood: the T in $M^{+}TM^{-}$ is not the same as the T in $M^{-}TM^{+}$. Thus, going downward on figure 4, $\Sigma11$AD reads $M^{+}TM^{-}TM^{+}TM^{-}T$. It is clearly made of two periods. Figure 4 cor- responds to a single period of $\Sigma11$B, which is consequently twice as large as the $\Sigma11$A period. A new oriented type of structural unit appears corresponding to the horizontal 7 + 5 atom ring motifs which one can name $P^{-}$ and $P^{+}$. They replace a T unit and inverse one of the con- tiguous $M^{\pm}$ units. The $\Sigma11$B shown in figure 5 thus reads $M^{+}P^{-}M^{+}TM^{-}P^{+}M^{-}T$. It is this $\Sigma11$B structure which was first observed on grown from the melt samples [31, 32]. The two structures have later been observed [4] on samples obtained by rather strongly deforming $\Sigma=9$ grain bound aries at different temperatures [33]. The $\Sigma11$A could thus be observed on samples deformed at a medium temperature of 1,220 K while the $\Sigma11$B was observed on samples deformed at a higher temperature (1,470 K). The minimized interfa- cial energies are given for various potentials in table 1. Although the absolute values largely differ, they all agree to give the lower minimized energy to the $\Sigma11$A model. But as the $\Sigma11$A has only a slightly lower minimized interfacial energy than $\Sigma11$B (e.g., the SW potential only gives a 2.7% difference), it was tempting to suggest that the latter structure becomes the more stable at high temperature because of a higher entropy due to its three structural units (T, M, P).

The rigid body displacements are essentially the same for SW and Tersoff C. There is no $z$ (in depth, with respect to figures 3 and 4) translation.

![](./images/812339051796365313_5.jpg)

Figure 5. $\Sigma11$B structure. Möbius box. The vertical line is a guide to the eye to locate the grain boundary plane.

<table>
<caption>Table 1. Static minimized interfacial energies $\gamma$ (mJ/m²) for various potentials: Keating(K) [13], Keating(B) [14], SW [15], Tersoff (C) [17], and Tersoff (B) [16].</caption>
<thead>
<tr>
<th>Type</th>
<th>Keating (K)</th>
<th>Keating (B)</th>
<th>SW</th>
<th>Tersoff (C)</th>
<th>Tersoff (B)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Sigma11$A</td>
<td>804</td>
<td>328</td>
<td>618</td>
<td>635</td>
<td>171.5</td>
</tr>
<tr>
<td>$\Sigma11$B</td>
<td>845</td>
<td>328</td>
<td>635</td>
<td>645</td>
<td>175</td>
</tr>
</tbody>
</table>

With respect to conservation of perfect crystal density, there is a slight $y$-dilation, 0.07 Å and 0.15 Å for $\Sigma11$A and $\Sigma11$B, respectively (SW), indicating that the atomic density is only very slightly lowered at the grain boundary. The most striking difference between the two structures resides in the vertical $x$-displacement: $\Sigma11$B has none whereas the two grains of $\Sigma11$A have a 0.82 Å vertical difference which can clearly be seen in figure 4. It might be worth noting that this value equals half the interplanar distance for the (311) planes which are perpendicular to the $x$-direction.

By slowly raising the temperature in molecular dynamics runs with both models, we started to observe simultaneous jumps of two atomic columns, shown in figure 6, for temperatures around 1,700 K. It can be seen that these jumps correspond to a change of structural units: they can for instance transform one TM⁻ SU into a P⁻M⁺ SU. In order for the whole $\Sigma11$AD SU series to be transformed into the $\Sigma11$B SU series, this kind of collective jump must occur twice: once in the upper half of the series and once in the lower half. If one artificially fixes these atomic moves on a relaxed $\Sigma11$AD structure, a further quasi-molecular dynamics relaxation will lead to the true $\Sigma11$B structure with

![](./images/812339051796365313_6.jpg)

Figure 6. A correlated jump of two atomic columns (at 1,700 K (SW)). The starting positions of the columns are indicated by the two arrows.

its correct $\Sigma 11$B vertical $x$-displacement between the two grains. At high temperature, however, these jumps simply keep on occurring every now and then, back and forth, as far as we could extend our runs, and do not drive any rigid body displacement of the grains. We extended our runs up a few hundred thousand steps. We thus cannot talk of a temperature driven phase tran- sition. What we simply observe is that these collective local atomic jumps are randomly and thermally activated. The Tersoff potential be- haves quite similarly, the temperature at which the jumps start being observable on a simulation scale being simply somewhat larger than with the SW potential.

An intermediate structure between $\Sigma 11$AD and $\Sigma 11$B can be thought of with the following SU series: $M^+P^-M^+TM^-TM^+T$. Minimized with the SW potential, it exhibits an interfacial energy just a little larger than the $\Sigma 11$Bs, $646\ \text{mJ/m}^2$, while its RBD is exactly intermediate: $0.41\ \text{\AA}$ in $x$. Heated to 1,700 K, it tends to evolve to the $\Sigma 11$AD structure.

We also simulated other $\Sigma 11$ structures with higher, and less favorable, periodicity such as $M^+TM^-TM^-TM^+TM^-TM^+TM^+TM^-T$. This structure was heated to 1,700 K. Several P units first appeared and the structure almost evolved to the B type except for a locally disordered re- gion. A P unit subsequently disappeared and the disordered region reordered into the A style, leading to a $\Sigma 11$B$\Sigma 11$AD sequence, which did not evolve any more as far as we could extend the simulation. However, freezing this $\Sigma 11$B$\Sigma 11$AD sequence and reheating it had it eventually evolve to an entire A type structure.

## 5. Conclusion

We have presented and validated a new type of periodic boundary condition which is specially suited to the simulation of twist grain boundaries in any centrosymmetric material. These conditions lead to only one grain boundary per simulation box and this could open new perspectives to study grain boundary migration.

We used these conditions to perform long-time simulations of large boxes with over 1,000 atoms interacting via classical two- and three-body potentials fitted to model silicon. Specifically studying the $\Sigma=11$ (2$\overline{3}$3) [011] models, we observed spontaneous jumps of atomic columns. These jumps correspond to changes of the local structure of the grain boundaries in terms of structural units. These changes remain local and reversible. They never drive any global move of the grains so as to modify their original rigid body translation relationship. We thus only interpret them as thermodynamically activated jumps. The same conclusions are reached with two different types of potentials: Stillinger Weber or Tersoff C. In situ observations would thus be helpful in order to decide whether more reliable potentials than Stillinger Weber or Tersoff should be used or whether extrinsic dislocations and/or impurities should be invoked to explain the observations of [1].

## Acknowledgments

This work has been started at the Laboratoire de Physique des Matériaux, Bellevue-Meudon. It was partially supported by the EEC contract SC1-CT91-0703 (TSTS). We wish to thank Prof. A. Sutton and A. Hairie for carefully rereading this paper and suggesting improvements in its presentation. Remaining imperfections are entirely ours.

## References

1. J.L. Putaux and J. Thibault-Desseaux, J. Physique 51, C1-323 (1990).
2. A. Bourret and J.L. Rouvière, in *Polycristalline Semiconductors*, Springer Proceedings in Physics, vol. 35, edited by J.H. Werner, H.J. Möller and H.P. Strunk (Springer Verlag, Berlin, 1989), p. 8.
3. J.L. Rouvière and A. Bourret, in *Polycristalline Semiconductors*, Springer Proceedings in Physics, vol. 35, edited by J.H. Werner, H.J. Möller and H.P. Strunk (Springer Verlag, Berlin, 1989), p. 19.
4. de Saint-Venant, A.J.C. Barré, in *Mémoire sur la torsion des prismes.*, Mém. des Savants étrangers (Paris 1855).
5. A.H. Cottrell, in *The Mechanical Properties of Matter* (John Wiley and Sons, New York, 1964), p. 93.
6. J.F. Lutsko, D. Wolf, S. Yip, S.R. Phillpot, and T. Nguyen, Physical Review B 38 11572 (1988).
7. W. Ledermann, Proc. Roy. Soc. Ser. A 182, 362 (1944).
8. S. Nosé, Mol. Phys. 52, 255 (1984).
9. S. Nosé, J. Chem. Phys. 81, 511 (1984).
10. S. Kirkpatrick, C.D. Gelatt, and M.P. Vecchi, Science 220, 671 (1983).
11. J.R. Beeler Jr. and G.L. Kulcinski, in *Interatomic Potentials and Simulations of Lattice Defects*, edited by P.C. Gehlen, J.R. Beeler Jr., and R.I. Jaffe (Plenum Press, New York, 1972), p. 735.
12. G.H. Bishop, G.A. Bruggeman, Ralph J. Harrison, J.A. Cox, and S.Yip, in *Nuclear Metallurgy Vol. 20*, edited by R.J. Arsenault, J.R. Beeler Jr., and J.A. Simmons (National Bureau of Standards, Gaitherburg, MD, 1976), p. 522.
13. P.N. Keating, Phys. Rev. 145, 637 (1966).
14. G.A. Baraff, E.O. Kane, and M. Schlüter, Phys. Rev. B 21, 5662 (1980).
15. F.H. Stillinger and T.A. Weber, Phys. Rev. B 31, 5262 (1985).
16. J. Tersoff, Phys. Rev. Lett. 56, 632 (1986).
17. J. Tersoff, Phys. Rev. B 37, 6991 (1988).
18. J. Tersoff, Phys. Rev. B 38, 9902 (1988).
19. J.Q. Broughton and X.Q. Li, Phys. Rev. B 35, 9120 (1987).
20. M. Schulz and R. Blachnik, in *Landolt-Börstein III/17a*, edited by O. Madelung (Springer Verlag, Heidelberg, 1982), p. 61.
21. P.J.E. Aldred and M. Hart, Proc. Roy. Soc. Lond. A 332, 239 (1973).
22. J.S. Reid and J. Pirie, Acta Cryst. A 36, 957 (1980).
23. K. Soma and H. Matsuo, Phys. Stat. Sol. (b) 111, K93 (1982).
24. J.B. Theeten and L. Dobrzynski, Phys. Rev. B 5, 1529 (1972).
25. F.A. Lindemann, Phys. Zeits. 11, 609 (1910).
26. J.J. Gilvarry, Phys. Rev. 102, 308 (1956).
27. M.K. Kluge, J.R. Ray, and A. Rahman, Phys. Rev. B 36, 4234 (1987).
28. S.R. Phillpot, J.F. Lutsko, D. Wolf, and S. Yip, Phys. Rev. B 40, 2831 (1989).
29. M. Born, J. Chem. Phys. 7, 591 (1939).
30. C.Z. Wang, C.T. Chan, and K.M. Ho, Phys. Rev. B 42, 11276 (1990).
31. A.M. Papon, M. Petit, and J.J. Bacmann, Phil. Mag. A 49, 573 (1984).
32. A Bourret and J.J. Bacmann, Revue Phys. Appl. 22, 563 (1987).
33. A. Georges, A Jacques, X. Baillin, J. Thibault-Desseaux, and J.L. Putaux, Inst. Phys. Conf. Ser. 104, 349 (1989).