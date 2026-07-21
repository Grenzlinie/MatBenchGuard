phys. stat. sol. (a) 174, 19 (1999)

Subject classification: 68.35.Bs; 61.50.Ah; S5

# Reconstruction of Diamond (001) Surface:
## A Monte Carlo Study with the Tersoff Potential

A. V. PETUKHOV (a), A. FASOLINO (a), D. PASSERONE (b), and F. ERCOLESSI (b)

(a) RIM and NSR Research Centres, Institute of Theoretical Physics, University of Nijmegen,
6525 ED Nijmegen, The Netherlands

(b) SISSA, Via Beirut 4, 34100 Trieste, Italy

(Received March 25, 1999)

We have performed an off-lattice Monte Carlo simulation of the (001) surface structure of diamond, based on the empirical many-body Tersoff potential. We find a dimerized $(2 \times 1)$ reconstruction with an asymmetric rearrangement of atoms in deeper layers nevertheless leaving the dimers unbuckled. Some atoms in second and third layers are then found in graphite-like three-fold coordination. Although this result is probably an artifact of the phenomenological potential which is used to describe interatomic interactions, it may correctly suggest a possible way of surface graphitization.

## 1. Introduction

Many unique properties of diamond and diamond-like coatings raised significant attention to their synthesis [1 to 7]. Nevertheless, a microscopic description of the growth and nucleation at diamond surfaces is still lacking. A theoretical study of these phenomena requires to deal with large unit cells to allow the formation of facets and defects as well as to describe ther interplay between diamond- and graphite-like bonding at surfaces [6]. Empirical many-body potentials [8] have been developed for silicon, germanium and carbon in order to be able to perform large scale simulations of disordered phases, while keeping a detailed description of the strongly directional covalent bonding. The Tersoff potential has been proved to work fairly accurately for Si and Ge, where diamond-like four-fold coordination to nearest neighbors is always favored [8]. Carbon forms instead both four-fold and graphite-like three-fold arrangements of nearest neighbors; even though the Tersoff potential was fit to reproduce the most important features of both structures, it may fail when both are present at the same time [9].

On the way towards the study of diamond growth, we have performed a test simulation of predictions of the Tersoff potential for the diamond (001) surface structure. This surface is known to present a $(2 \times 1)$ reconstruction due to the formation of unbuckled dimers [1 to 5, 10]. The Monte Carlo (MC) technique has been proved to be very effective for structural investigations. Here we exploit the MC simulated annealing scheme to overcome potential energy barriers and find the minimum energy surface structures. A new $(2 \times 1)$ reconstruction with significantly lower energy is found in which the dimers stay unbuckled while the atoms in deeper layers form an asymmetric structure. We argue that although this prediction is probably an artifact of the potential inaccuracy, it may correctly suggest a possible pathway of graphitization of the diamond (001) surface.

![](./images/812465249868316673_1.jpg)

Fig. 1. Top view of the diamond (001) surface structure after an annealing cycle. The atom positions are labelled with balls of variable size, the largest being at the surface. The bonds are drawn between atoms separated by less than 1.8 Å

## 2. Simulated Annealing

In this work the samples consist of 20 atomic layers with $6 \times 6 = 36$ atoms in each of them. Four bottom layers are kept fixed at bulk-terminated positions while in the other 16 layers the atoms ($16 \times 36 = 576$ atoms in total) can be moved according the MC Metropolis scheme (acceptance of a more is based on constructing the Boltzmann factor using evaluation of the energy change). The simulated annealing cycles have been always started from bulk-terminated samples with lattice constant $a = 3.567$ Å, and no constraints based on an expected reconstruction are used. The sample temperature has been raised to $T = (2500$ to $3000)$ K and then slowly reduced in 10 to 20 steps to $T \approx 10$ K. For each $T$ several thousands MC steps have been computed (one MC step corresponds to one movement try per atom in average). The temperature-dependent maximally allowed displacement of an atom has been chosen in a way that about 50% of moves are accepted for most efficient computing.

The diamond surface structure after such a simulated annealing cycle is shown in Fig. 1. First of all, one can see that many atoms in the topmost layer have formed dimers, which are arranged in parallel rows. We note that the dimerization of diamond (001) surface was not observed in a molecular dynamic simulation using the same Tersoff empirical potential by Haliciouglu [11]. Later, Dyson and Smith [10] have found that the Tersoff potential does predict dimerization, in agreement with our result. However, in addition to dimerization, one can observe additional structural changes which are most evident in the third layer of atoms. Many third-layer atoms underneath the dimer row have moved away from symmetric positions and have cut one of their bonds towards the second-layer atoms.

## 3. Energy Minimization

To remove the randomness from the structure, energy minimization has then been performed for three reconstructions at low temperatures ($T \approx 10$ to $30$ K, reduced down to

zero at the end of the run). Keeping $T$ low has been found to be important to avoid formation of domains with another reconstruction.

If we perform such a low-$T$ energy minimization for a bulk-terminated sample, the structure keeps the ideal $(1\times1)$ in-plane structure and displays relaxations along the normal, which rapidly decay in the bulk (see Table 1). These relaxations result in an energy gain of 0.36 eV per surface atom (relative to the bulk-terminated sample).

Next we have considered a sample where the topmost surface atoms have been pre- moved closer together in pairs to obtain the $(2\times1)$ reconstruction. The minimized structure is diplayed in Fig. 2b. This structure gives an energy gain of 0.26 eV per dimer (i.e., 0.13 eV per surface atom) relative to the relaxed $(1\times1)$ structure (Fig. 2a), which is quite close to the energy gain 0.2 eV/dimer as calculated for the same empirical po- tential by Dyson and Smith [10], but is far too small compared to results of first-prin- ciple calculations [3 to 5].

The third structure studied is an asymmetric $(2\times1)$ reconstruction, in which the third-layer atom below the dimer rows has been pre-moved from its symmetric posi- tion before the energy minimization run. In the following we use the $(2\times1)$a nota- tion for this reconstruction, where 'a' stands for asymmetric. The $(2\times1)$a reconstruc- tion gives an energy gain of 1.55 eV per dimer relative to the relaxed $(1\times1)$ structure, i.e. very much more favorable than the symmetric $(2\times1)$ reconstruction. Note that despite the asymmetry of the structure in deeper layers, the dimers are not buckled. Table 1 summarizes the atom displacements for the three studied structures. The $(2\times1)$a structure implies rearrangements of atomic positions of more layers than the other two structures. However, even when fixing the fourth- and deeper-layer atoms to bulk-terminated positions, the $(2\times1)$a reconstruction remains by far the most stable.

Table 1
Atom displacements of the first six atomic layers relative to their bulk-terminated posi- tions for the three structures studied. The atom labelling scheme is explained in Fig. 2. The accuracy of displacements is of order 0.001 to 0.002 Å (last digit shown). For com- parison: the bulk interlayer distance along the [001] direction $a/4=0.892$ Å, the bulk nearest neighbor distance $\sqrt{3}a/4=1.5445$ Å

<table>
<thead>
<tr>
<th colspan="2">$(1\times1)$</th>
<th rowspan="2">atom</th>
<th colspan="2">$(2\times1)$</th>
<th colspan="2">$(2\times1)$a</th>
</tr>
<tr>
<th>layer</th>
<th>$\delta z$ (Å)</th>
<th>$\delta y$ (Å)</th>
<th>$\delta z$ (Å)</th>
<th>$\delta y$ (Å)</th>
<th>$\delta z$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>$-0.127$</td>
<td>11</td>
<td>0.491</td>
<td>$-0.183$</td>
<td>0.582</td>
<td>$-0.236$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>12</td>
<td>$-0.490$</td>
<td>$-0.183$</td>
<td>$-0.453$</td>
<td>$-0.238$</td>
</tr>
<tr>
<td>2</td>
<td>0.013</td>
<td>21</td>
<td>0.023</td>
<td>0.114</td>
<td>0.112</td>
<td>0.003</td>
</tr>
<tr>
<td></td>
<td></td>
<td>22</td>
<td>$-0.023$</td>
<td>0.114</td>
<td>0.198</td>
<td>0.290</td>
</tr>
<tr>
<td>3</td>
<td>$-0.004$</td>
<td>31</td>
<td>0.000</td>
<td>0.082</td>
<td>0.028</td>
<td>0.144</td>
</tr>
<tr>
<td></td>
<td></td>
<td>32</td>
<td>0.000</td>
<td>$-0.078$</td>
<td>$-0.155$</td>
<td>$-0.214$</td>
</tr>
<tr>
<td>4</td>
<td>$-0.001$</td>
<td>41</td>
<td>0.000</td>
<td>0.037</td>
<td>$-0.007$</td>
<td>0.082</td>
</tr>
<tr>
<td></td>
<td></td>
<td>42</td>
<td>0.000</td>
<td>$-0.037$</td>
<td>0.009</td>
<td>$-0.073$</td>
</tr>
<tr>
<td>5</td>
<td>$-0.001$</td>
<td>51</td>
<td>$-0.006$</td>
<td>$-0.001$</td>
<td>0.017</td>
<td>0.020</td>
</tr>
<tr>
<td></td>
<td></td>
<td>52</td>
<td>0.007</td>
<td>$-0.001$</td>
<td>0.016</td>
<td>0.012</td>
</tr>
<tr>
<td>6</td>
<td>$-0.001$</td>
<td>51</td>
<td>$-0.007$</td>
<td>$-0.001$</td>
<td>$-0.016$</td>
<td>$-0.001$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>62</td>
<td>0.007</td>
<td>$-0.001$</td>
<td>0.016</td>
<td>0.001</td>
</tr>
</tbody>
</table>

![](./images/812465249868316673_2.jpg)

Fig. 2. Double unit cell of $(1\times1)$ (a) and unit cells of $(2\times1)$ (b) and $(2\times1)$a (c) structures. The top panels show the top $xy$ views along with the labelling scheme used in Table 1. The lower panels show the side $yz$ views together with arrows indicating directions of most evident displacements. Length of arrows is approximately proportional to the displacement. The positive $x\parallel[1\overline{1}0]$, $y\parallel[110]$ and $z\parallel[001]$ directions are indicated

## 4. Discussion

To our knowledge, such an asymmetric reconstruction was never predicted theoretically nor observed experimentally. Theoretically, it is difficult to find the global energy minimum in many-dimensional conformation space. In this respect our MC method in conjunction with a simulated annealing scheme seems to be quite powerful. In most experimental studies it is hard to characterize the atomic structure in deeper layers. The asymmetric $(2\times1)$a reconstruction can turn out to be consistent with the known structural information on clean diamond (100) surfaces. Our result thus suggests for a more attentive analysis of the structural data for a possible asymmetric structure in deeper layers.

However, we are not in a position to clain that the $(2\times1)$a structure should give the global energy minimum in reality. Quite probably, it is an artifact of the inaccuracy of the empirical Tersoff potential which is used in our simulations. In our results one can observe some other features, which disagree with known facts. The dimer bond length is found $1.54\,\mathring{A}$ for $(2\times1)$ and $1.49\,\mathring{A}$ for $(2\times1)$a to be longer than $\approx1.4\,\mathring{A}$ calculated in more accurate ab-initio calculations [4, 5]. In addition, in our simulated annealing computations of the diamond (111) surface no reconstruction has been observed in contrast to the usual believe in its $(2\times1)$ reconstruction [12].

Despite its low reliability, we believe that our results can still be of interest. More accurate calculations might prove that the asymmetric structure shown in Fig. 2c does not correspond to the global energy minimum of the surface, but one could still expect that its energy is rather low. Thus, at thermodynamic equilibrium for a real diamond (001) surface at finite temperatures, one could expect to find some of the third-layer atoms moved from their symmetric positions. The atoms '32' and '22' then appear in a graphite-like three-fold coordination with a nearly planar arrangement of the nearest neighbors, thus forming two nearly-parallel graphitic 'mini-planes'. Such a structure could serve as an initial step towards graphitization of the diamond (001) surface. We

note that the pathway of graphitization of diamond (111) surface has been extensively studied in the past [13]. To our knowledge, no suggestions have been made for possible pathway for graphitization of the (001) surface.

## 5. Summary
To summarize, we have performed an off-lattice MC simulation of the structure of a clean diamond (001) surface based on the Tersoff potential. The obtained data for the $(1\times 1)$ and symmetric $(2\times 1)$ reconstructions agree with reported results [10, 11]. In addition, our simulated annealing strategy allowed us to find a new $(2\times 1)$a reconstruc- tion with a significantly lower energy, which suggests that this possibility has to be taken into account in the analysis of the structural data. Although the prediction of the $(2\times 1)$a reconstruction has a low reliability due to the possible inaccuracy of the used empirical potential, it is argued that it may correctly suggest a possible way of graphiti- zation of the diamond (001) surface. Low reliability of the Tersoff potential for predict- ing diamond surface structure makes questionable its use for diamond growth studies.

One of the reasons of the Tersoff potential inaccuracy could be the fact that it does not properly distinguish bonds of different type (single vs. conjugated). This problem is overcome in the empirical potential of Brenner [9], which we are currently implement- ing to check the predictions of the present work. Another advantage of the Brenner potential is that it can also describe carbon–hydrogen interactions; that will allow us to investigate diamond growth in the presence of hydrogen on the surface which has been shown to play an important role.

**Acknowledgement** We would like to acknowledge Hans ter Meulen, Frank von Bou- welen, Willem van Enckevort, and John Schermer for stimulating discussions.

## References
[1] Th. Frauenheim, U. Stephan, P. Blaudeck, D. Porezag, H.-G. Busmann, W. Zimmermann- Edling, and S. Lauer, Phys. Rev. B **48**, 18189 (1993).
[2] S. Skokov, C. S. Carmer, B. Weiner, and M. Frenklach, Phys. Rev. B **49**, 5662 (1994).
[3] Z. Jing and J. L. Whitten, Phys. Rev. B **50**, 2598 (1994).
[4] J. Furthmüller, J. Hafner, and G. Kresse, Phys. Rev. B **53**, 7334 (1996).
[5] P. Krüger and J. Pollmann, Phys. Rev. Lett. **74**, 1155 (1995).
[6] S. Scandolo, M. Bernasconi, G. L. Chiarotti, P. Focher, and E. Tosatti, Phys. Rev. Lett. **74**, 4015 (1995).
M. Zaser and F. Banhart, Phys. Rev. Lett. **79**, 3680 (1997).
A. Reznik, V. Richter, and R. Kalish, Phys. Rev. B **56**, 7930 (1997).
[7] See also other papers in this issue.
[8] J. Tersoff, Phys. Rev. Lett. **56**, 632 (1986); Phys. Rev. B **37**, 6991 (1988).
[9] D. W. Brenner, Phys. Rev. B **42**, 9458 (1990).
[10] A. J. Dyson and P. V. Smith, Surface Sci. **316**, 309 (1994).
[11] T. Halicioglu, Surface Sci. **259**, L714 (1991).
[12] S. Iarlori, G. Galli, F. Gygi, M. Parinello, and E. Tosatti, Phys. Rev. Lett. **69**, 2947 (1992).
[13] R. Graupner, F. Maier, J. Ristein, L. Ley, and Ch. Jung, Phys. Rev. B **57**, 12397 (1998).
G. Kern and J. Hafner, Phys. Rev. B **58**, 13167 (1998).

<br>