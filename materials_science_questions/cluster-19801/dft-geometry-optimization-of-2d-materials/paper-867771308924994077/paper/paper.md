
# (Meta-)stable reconstructions of the diamond (111) surface: interplay between diamond- and graphite-like bonding

A.V. Petukhov \( ^{*} \) 

RIM and NSR Research Centers, Theoretical Physics, University of Nijmegen, NL-6525 ED Nijmegen, The Netherlands

D. Passerone \( ^{\dagger} \) , F. Ercolessi, E. Tosatti

Istituto Nazionale di Fisica della Materia (INFM) and Scuola Internazionale Superiore di Studi Avanzati (SISSA), Via Beirut 2/4, 34014 Trieste, Italy

A. Fasolino

RIM Research Center, Theoretical Physics, University of Nijmegen, NL-6525 ED Nijmegen, The Netherlands

Off-lattice Grand Canonical Monte Carlo simulations of the clean diamond (111) surface, based on the effective many-body Brenner potential, yield the  \( (2 \times 1) \)  Pandey reconstruction in agreement with ab-initio calculations and predict the existence of new meta-stable states, very near in energy, with all surface atoms in three-fold graphite-like bonding. We believe that the long-standing debate on the structural and electronic properties of this surface could be solved by considering this type of carbon-specific configurations.

The discovery of fullerene has awakened an increasing interest in carbon based nanostructures as well as in processes, such as diamond graphitization \( ^{1} \)  or the graphite-to-diamond transformation \( ^{2} \)  leading to structures, which promise to have desirable properties of both graphite and diamond. It is important to develop predictive schemes to treat diamond, graphite and mixed bonding with approaches able to deal with large structures, often beyond the possibility of ab-initio calculations. The effective many-body empirical potentials due to Tersoff \( ^{3} \)  for group IV elements are very accurate for Si and Ge, but less reliable for C. In particular, for C the Tersoff potential yields the unreconstructed (111)  \( (1 \times 1) \)  surface as the most stable against the experimental evidence \( ^{4-7} \)  of a  \( (2 \times 1) \)  Pandey reconstruction. \( ^{8,9} \)  For the (001) face it predicts dimerization with a strong asymmetric displacement of the third-layer atoms. \( ^{10} \)  Here, we use the potential proposed by Brenner \( ^{11} \)  (parametrization I) and show that it is reliable also at the surface. \( ^{12} \) 

We perform off-lattice Grand Canonical Monte Carlo (GCMC) simulations \( ^{13} \)  of the (111) surface of diamond. We find the unbuckled undimerized  \( (2\times1) \)  Pandey chain reconstruction as the minimum energy structure and three new meta-stable states, close in energy, with all surface atoms in a three-fold graphite-like bonding. Two of them are obtained by a strong dimerization of the lower (4-fold coordinated) chain, inducing a small dimerization of the upper ( \( \pi \) -bonded) chain as well. The third meta-stable  \( (\sqrt{3}\times\sqrt{3})R30^{\circ} \)  reconstruction is formed by a regular array of vacancies.

Surprisingly, the reconstruction of clean diamond(111) is not yet established in detail, although there is a consensus that the  \( \pi \) -bonded Pandey  \( (2\times1) \)  reconstruction \( ^{8,9} \)  is the most stable. One important issue is whether this surface is metallic or semiconducting. In most calculations \( ^{14-17} \)  the band of surface states is metallic whereas experimentally the highest occupied state is at least 0.5 eV below the Fermi level. \( ^{18,19} \)  Dimerization along the  \( \pi \) -bonded chain could open the surface gap \( ^{20,21} \)  but only one total-energy calculation obtains slightly dimerized chains yielding a 0.3 eV gap \( ^{20} \)  in the surface band. Experimentally, recent X-ray data \( ^{6} \)  and medium-energy ion scattering \( ^{7} \)  do not show any dimerization but favor the  \( (2\times1) \)  reconstruction accompanied by a strong tilt of the  \( \pi \) -bonded chains, similar to the  \( (2\times1) \)  reconstruction of Si(111) and Ge(111). The tilt is however not confirmed by theoretical studies. \( ^{14-17,20} \)  Also, relaxations in deeper layers are debated. The bonds between first and second bilayers are found to be elongated by an amount which varies between 1% \( ^{6,7} \)  and 8%. \( ^{4,14,20} \)  Bonds between the second and third bilayers are slightly shifted ( \( \lesssim1\% \) ) in theoretical studies while X-ray data suggest a 5-6% relaxation. \( ^{6,7} \) 

Experimentally, uncertainties can be caused by variations of surface preparation. A partial graphitization \( ^{1,19,22} \)  and other structural phases \( ^{23,24} \)  can coexist at the real surface. It is noteworthy that most structural models were first suggested for Si and Ge \( ^{8,25,26} \)  and then extended to diamond. \( ^{9,14} \)  However, the former always favor tetrahedral four-fold coordination whereas C favors also the graphite-like three-fold bonding, the latter being in fact energetically stable in the bulk at normal conditions. One can therefore expect diamond to have additional low-energy surface structures, such as the meta-stable reconstructions presented here.

Empirical potentials, although less accurate than ab-initio calculations, allow to explore larger portions of phase space and can lead to unexpected structures, which can then be tested in more accurate calculations and taken into account in the experimental data analysis. We exploit the MC simulated annealing scheme to overcome potential energy barriers and identify low-energy surface structures. Atoms in the bottom layers are kept fixed at their ideal bulk positions while the others (usually, four bilayers of 128 atoms each) are mobile. We consider either a VNT, PNT or  \( P\mu T \)  ensembles for differ-
 

ent tasks. The canonical VNT ensemble is used to minimize ordered structures. During the simulated annealing we allow for volume fluctuations  \( (PNT) \) . We consider also a grand canonical  \( P\mu T \)  ensemble \( ^{13} \)  to access structures with different number of atoms than in the bulk terminated structure. Each atom creation/destruction is enabled only in the near-surface region (2-3 top bilayers) and followed by 1000 MC equilibration moves. We have optimized the implementation of the potential by use of neighbor lists which allow to calculate energy variations on a finite portion of the sample. The one-dimensional functions defining the potential are stored in tables with a fine grid and calculated by linear interpolation. The attractive  \( V_{A} \) , repulsive  \( V_{R} \)  and the cut-off  \( f_{c} \)  terms are stored as a function of the square of interatomic distances to avoid square root operations. The three-dimensional F function is stored on a finer grid and the tricubic interpolation \( ^{11} \)  is replaced by a linear one, reducing the terms to be evaluated from 64 to 8. We note that, in a strongly covalent system like diamond, creation and destruction are very improbable events, also because immediately after creation or destruction the neighboring atoms have not yet adjusted to the new local environment; after a destruction the system can gain up to 2 eV by relaxation. This energy has been added as an umbrella \( ^{27} \)  in the acceptance rule for creation/destruction.

![](./images/867771308924994077_1.jpg)

FIG. 1. Left: relaxed  \( 1 \times 1 \) , right: Pandey  \( \pi \) -bonded chain. The top (111) and side (110) views are presented in the top and bottom images, respectively. The relative changes of the bond lengths and the atom labeling schemes used in Table I are indicated.

Throughout, we give energy gains  \( \Delta E \)  per  \( 1 \times 1 \)  unit cell, relative to the bulk-terminated surface. We find the relaxed  \( (1 \times 1) \)  and Pandey  \( (2 \times 1) \(  structures shown in Fig. 1 to have  \) \Delta E = 0.244 \(  and 1.102 eV, respectively. Apart from a 4% elongation of the bond between first and second bilayer against 8% \) ^{4,14,20} $  for the Pandey structure, our results agree remarkably well with ab-initio calculations. \( ^{14,17,20,28} \) 

To the best of our knowledge, no one has succeeded before in simulating a spontaneous transition from the ideal  \( (1 \times 1) \)  to the  \( (2 \times 1) \(  reconstructed diamond (111) surface. The  \) (2 \times 1) \(  reconstruction of both diamond (111) and Si (111) is associated with a large coherent displacement of the first bilayer by more than 0.5 Å, accompanied by rebonding in which one atom in the  \) 2 \times 1 $  surface unit cell changes coordination from four to three while another does the opposite. Ab-initio molecular dynamics simulation \( ^{29} \)  of the spontaneous  \( (2 \times 1) \)  reconstruction of Si (111) shows that breaking and formation of a new bond occurs at the same time. We find that for diamond, instead, the bond breaking leading to an increase of threefold (graphite-like) atoms precedes the bond formation. \( ^{30} \)  In such a situation, competition between the  \( (2 \times 1) \)  reconstruction and (partial) surface graphitization becomes very important, \( ^{22} \)  especially if the annealing is performed at high temperatures. Conversely, a low annealing temperature makes it very difficult to overcome the potential barrier between the two ordered structures. In Fig. 2 we show the top view of a diamond (111) sample, obtained from the ideal relaxed  \( (1 \times 1) \)  structure after an annealing cycle (about  \( 0.5 \cdot 10^{6} \)  MC steps) at  \( T = 750 \)  K. The efficiency of phase space exploring is improved by increasing the step size \( ^{27} \)  as to reduce the acceptance rate from the usual 50% down to 20-25%. In Fig. 2 we emphasize pieces of the lower, four-fold coordinated Pandey chains which represent the final stage of the  \( (1 \times 1) \rightarrow (2 \times 1) \)  transition. Only one rotational domain is present and the relative position of the formed chains is somewhat disordered.

![](./images/867771308924994077_2.jpg)

FIG. 2. Top view of a reconstructed diamond(111) sample after a spontaneous transition from the bulk-terminated  \( (1 \times 1) \)  structure. The four-fold coordinated atoms in the first bilayer (atoms 13 and 14 in Fig. 1) are shown as dark balls and connected by dark solid lines. Periodic boundary conditions within the surface plane are used.
 
![](./images/867771308924994077_3.jpg)

FIG. 3. Meta-stable structures of the diamond(111) surface arranged as in Fig. 1. Left and central structures are the  \( (2 \times 1) \)  and  \( (4 \times 1) \(  dimerized reconstructions. Short and long distances in the dimerized chain are indicated by solid and broken lines, respectively. The structure on the right displays the vacancy  \) (\sqrt{3} \times \sqrt{3}) R30^{o} $  reconstruction.

TABLE I. Coordinates of atoms (in Å) within top three bilayers for the Pandey model,  \( (2 \times 1) \)  and  \( (4 \times 1) \(  dimerized reconstructions. \) ^{30} $  The Brenner potential gives the diamond bulk bond length of 1.541 Å and the  \( 2 \times 1 \)  unit cell has in-plane dimensions  \( 4.357 \times 2.517 \)  Å \( ^{2} \) . The numbers in brackets for the  \( (4 \times 1) \)  dimerized reconstruction are coordinates of atoms in the second half of the unit cell (denoted with primes in Fig. 3).

<table><tr><td rowspan="2">atom</td><td colspan="4">Pandey</td><td colspan="4">{dimer 2 × 1</td><td colspan="4}>{dimer 4 × 1</td></tr><tr><td>x</td><td>y</td><td>z</td><td>x</td><td>y</td><td>x</td><td>z</td><td>y</td><td>z</td><td></td><td></td></tr><tr><td>11</td><td>3.064</td><td>-0.943</td><td>5.525</td><td>3.071</td><td>-0.942</td><td>5.638</td><td>3.072 (7.435)</td><td>-0.532 (-1.355)</td><td>5.648 (5.645)</td><td></td><td></td></tr><tr><td>12</td><td>2.370</td><td>0.315</td><td>5.519</td><td>2.353</td><td>0.332</td><td>5.625</td><td>2.379 (6.742)</td><td>0.728 (-0.095)</td><td>5.646 (5.641)</td><td></td><td></td></tr><tr><td>13</td><td>1.007</td><td>0.313</td><td>4.792</td><td>1.177</td><td>0.594</td><td>4.804</td><td>1.210 (5.591)</td><td>0.714 (-0.081)</td><td>4.802 (4.793)</td><td></td><td></td></tr><tr><td>14</td><td>0.076</td><td>-0.941</td><td>4.804</td><td>-0.112</td><td>-1.188</td><td>4.820</td><td>-0.151 (4.228)</td><td>-1.325 (-0.561)</td><td>4.813 (4.806)</td><td></td><td></td></tr><tr><td>21</td><td>3.816</td><td>-0.942</td><td>3.325</td><td>3.835</td><td>-0.965</td><td>3.331</td><td>3.838 (8.202)</td><td>-0.911 (-0.989)</td><td>3.330 (3.325)</td><td></td><td></td></tr><tr><td>22</td><td>3.041</td><td>0.316</td><td>2.880</td><td>3.065</td><td>0.299</td><td>2.872</td><td>3.072 (7.436)</td><td>0.350 (0.275)</td><td>2.866 (2.862)</td><td></td><td></td></tr><tr><td>23</td><td>1.557</td><td>0.314</td><td>3.290</td><td>1.573</td><td>0.341</td><td>3.297</td><td>1.589 (5.967)</td><td>0.378 (0.250)</td><td>3.313 (3.302)</td><td></td><td></td></tr><tr><td>24</td><td>0.895</td><td>-0.943</td><td>2.737</td><td>0.896</td><td>-0.910</td><td>2.759</td><td>0.898 (5.272)</td><td>-0.878 (-1.015)</td><td>2.774 (2.767)</td><td></td><td></td></tr><tr><td>31</td><td>3.065</td><td>0.316</td><td>1.300</td><td>3.075</td><td>0.318</td><td>1.295</td><td>3.084 (7.449)</td><td>0.322 (0.306)</td><td>1.299 (1.291)</td><td></td><td></td></tr><tr><td>32</td><td>2.346</td><td>-0.942</td><td>0.760</td><td>2.251</td><td>-0.946</td><td>0.770</td><td>2.361 (6.727)</td><td>-0.938 (-0.955)</td><td>0.769 (0.765)</td><td></td><td></td></tr><tr><td>33</td><td>0.883</td><td>-0.944</td><td>1.227</td><td>0.889</td><td>-0.930</td><td>1.240</td><td>0.895 (5.265)</td><td>-0.918 (-0.974)</td><td>1.252 (1.246)</td><td></td><td></td></tr><tr><td>34</td><td>0.152</td><td>0.315</td><td>0.739</td><td>0.156</td><td>0.328</td><td>0.752</td><td>0.162 (4.533)</td><td>0.342 (0.293)</td><td>0.756 (0.756)</td><td></td><td></td></tr></table>

At higher temperatures, apart from a tendency towards graphite-like structures, we observe also other ordered phases, similar to the Pandey reconstruction but accompanied by a strong dimerization of the lower atomic chain. \( ^{30} \)  This dimerization can be performed in two ways, leading to the  \( (2 \times 1) \)  and  \( (4 \times 1) $  structures shown in Fig. 3. The atom coordinates are given \( ^{30} \)  in Table I along with those for the Pandey reconstruction. The energy gain  \( \Delta E \)  is 0.883 and 1.023 eV, for the metastable  \( (2 \times 1) \)  and  \( (4 \times 1) $  respectively. In the dimerized chains the short/long distances between atoms 13 and 14 are 1.459/2.215 and 1.444/2.455 Å for the  \( (2 \times 1) \)  and  \( (4 \times 1) $  instead of 1.562 Å in the Pandey reconstruction. This dimerization induces dimerization of the  \( \pi \) -bonded chain as well, albeit small ( \( < 1\% \) ), which might be of importance for surface electronic properties. The  \( (4 \times 1) \)  dimerized structure is only 160 meV ( \( \approx 2000 \)  K) per broken bond higher than the Pandey structure, i.e. these phases can coexist at the surface at high temperatures. Indeed, by heating the ordered Pandey structure to 2350 K we observe a partial transformation to the dimerized state as shown in Fig. 4. Note also a precursor of surface graphitization.

Lastly, in GCMC runs we find the  \( (\sqrt{3} \times \sqrt{3})R30^{\circ} \)  reconstruction formed by an ordered array of vacancies as shown on the right hand side in Fig. 3. The bond lengths between the atoms in the first bilayer is reduced to 1.390 Å, slightly less than the equilibrium bond length in graphite (1.42 Å). The bonds between the first and second layer are elongated by  \( \sim 1\% \)  while the other bond lengths are close to the bulk value. Taking the bulk binding energy 7.346 eV as the chemical potential, the energy gain is estimated to be  \( \Delta E = 0.6145 \)  eV. Once formed, this structure is found to be very stable and remains unaltered after long GCMC annealing cycles at  \( T = 2350 \)  K. \( ^{30} \)  Similar structures have been discussed for Si. \( ^{31,32} \)  For diamond(111) a  \( (2 \times 2) \)  vacancy structure was shown to be energetically unfavorable compared to the relaxed  \( (1 \times 1) \)  structure. \( ^{33} \)  However, contrary to the  \( (2 \times 2) \)  vacancy structure, \( ^{33} \)  our  \( (\sqrt{3} \times \sqrt{3}) \)  structure has only three-fold coordinated surface atoms and might thus be more favorable.
 
![](./images/867771308924994077_4.jpg)

FIG. 4. Top and side views of the sample at 2350 K showing coexistence of the original Pandey chain (lower chains connected by solid lines) and the dimerized (alternating solid-dashed lines) reconstructions. The four atoms in the first bilayer connected by a dotted line in the top view and given as dark balls in the side view are lifted off (a precursor of surface graphitization). The dark atoms underneath in the second bilayer have changed their coordination from four to three to form a new  \( \pi \) -bonded chain.

In conclusion, we have performed off-lattice GCMC simulations of the clean diamond (111) surface structure based on the Brenner potential. A spontaneous transition from the ideal  \( (1 \times 1) \)  to the stable Pandey  \( (2 \times 1) \)  reconstruction is obtained. We also find metastable reconstructions very close in energy with strong dimerization of the lower atomic chain, which are shown to coexist with the Pandey chain reconstruction at temperatures  \( \sim 2000 \)  K. Besides, we find a deep local minimum for the vacancy stabilized  \( (\sqrt{3} \times \sqrt{3}) \)  structure. These meta-stable structures have a larger number of three-fold coordinated atoms at the surface. The absence of consensus on the structural details and electronic structure of the clean (111) surface might be related to these surface structures, which are peculiar of carbon and have never been considered so far.

A.V.P. and A.F. would like to thank E. Vlieg, F. van Bouwelen, J.J. ter Meulen, W. van Enckevort, J. Schermer and B.I. Dunlap for useful discussions. D.P., F.E. and E.T. acknowledge support by MURST.
 \( ^{*} \)  on leave from the Institute of Crystallography, 117333 Moscow, Russia; e-mail petukhov@sci.kun.nl

 \( ^{\dagger} \)  present address: Max Planck Institut für Festkörperforschung, D-70569, Stuttgart, Germany.

 \( ^{1} \)  Y.G. Gogotsi, A. Kailer, K.G. Nickel, Nature, 401, 663 (1999); A. De Vita et al., Nature 379, 523 (1996).

 \( ^{2} \)  F. Banhart, P.M. Ajayan, Nature, 382, 433 (1996).

 \( ^{3} \)  J. Tersoff, Phys. Rev. Lett. 61, 2879 (1988).

 \( ^{4} \)  E.C. Sowa, G.D. Kubiak, R.H. Stulen, J. Vac. Sci. Technol. A 6, 832 (1988).

 \( ^{5} \)  T.E. Derry, L. Smit and J.F. van der Veen, Surf. Sci. 167, 502 (1986).

 \( ^{6} \)  W.J. Huisman et al., Surface Sci., 396, 241 (1998).

 \( ^{7} \)  W.J. Huisman, J.F. Peters, J.F. van der Veen, Surface Sci., 396, 253 (1998).

 \( ^{8} \)  K.C. Pandey, Phys. Rev. Lett. 47, 1913 (1981).

 \( ^{9} \)  K.C. Pandey, Phys. Rev. B 25, 4338 (1982).

 \( ^{10} \)  A.V. Petukhov, A. Fasolino, D. Passerone, F. Ercolessi, Phys. Stat. Sol. (a) 174, 19 (1999).

 \( ^{11} \)  D.W. Brenner, Phys. Rev. B 42,9458 (1990).

 \( ^{12} \)  For the (001) surface see A.V. Petukhov, A. Fasolino, Phys. Stat. Sol. (a), to be published.

 \( ^{13} \)  F. Celestini, D. Passerone, F. Ercolessi and E. Tosatti, Surf. Sci. 402-404, 886 (1998).

 \( ^{14} \)  D. Vanderbilt, S.G. Louie, Phys. Rev. B 30, 6118 (1984).

 \( ^{15} \)  D.R. Alfonso, D.A. Drabold, S.E. Ulloa, Phys. Rev. B 51, 14669 (1995).

 \( ^{16} \)  G. Kern, J. Hafner, J. Furthmüller, G. Kresse, Surface Sci., 352-354, 745 (1996).

 \( ^{17} \)  A. Scholze, W.G. Schidt, F. Bechstedt, Phys. Rev. B 53, 13725 (1996).

 \( ^{18} \)  R. Graupner et al., Phys. Rev. B 55, 10841 (1997).

 \( ^{19} \)  J.B. Cui, J. Ristein, L. Ley, Phys. Rev. B 59, 5847 (1999).

 \( ^{20} \)  S. Iarlori et al., Phys. Rev. Lett. 69, 2947 (1992).

 \( ^{21} \)  C. Kress, M. Fiedler, F. Bechstedt, Europhys. Lett. 28, 433 (1994).

 \( ^{22} \)  G. Jungnickel et al., Mat. Res. Soc. Symp. Proc., 383, 349 (1995); Phys. Stat. Sol. (a) 154, 109 (1996).

 \( ^{23} \)  Th. Frauenheim et al., Phys. Rev. B 48, 18189 (1993).

 \( ^{24} \)  R. Graupner et al., Phys. Rev. B 57, 12397 (1998).

 \( ^{25} \)  D.J. Chadi, Phys. Rev. Lett. 26, 4762 (1982).

 \( ^{26} \)  R. Seiwatz, Surface Sci., 2, 473 (1964).

 \( ^{27} \)  M.P. Allen, D.J. Tildesley, Computer Simulation of Liquids (Clarendon Press, Oxford, 1987).

 \( ^{28} \)  R. Stumpf, P.M. Markus, Phys. Rev. B 47, R16016 (1993).

 \( ^{29} \)  F. Ancilotto et al., Phys. Rev. Lett. 65, 3148 (1990).

 \( ^{30} \)  Animations, xyz files and many other details can be found at http://www.sci.kun.nl/tvs/carbon/.

 \( ^{31} \)  W.C. Fan et al., Phys. Rev. Lett., 62, 1516 (1989).

 \( ^{32} \)  F. Ancilotto, A. Selloni, E. Tosatti, Phys. Rev. B, 43, R14726 (1991).

 \( ^{33} \)  F. Bechstedt, W.G. Schmidt, A. Scholze, Europhys. Lett. 35, 585 (1996).
 
