# Role of multi-ion interactions in the stacking-fault energies of transition metals

R. E. Beissner
Southwest Research Institute, San Antonio, Texas 78284
(Received 2 March 1976)

The theory of multi-ion interactions is applied to calculations of the stacking-fault energies of transition metals. It is found that observed trends in the stabilities of close-packed transition metals can be explained on the basis of a simple model in which resonant scattering, three-ion interactions dominate.

## I. INTRODUCTION

The results of recent calculations of stacking-fault energies and comparisons with experimental data indicate that a pseudopotential expansion carried to second order in the energy is adequate for the treatment of nontransition metals. $^{1,2}$ As Heine and Weaire $^{3}$ had noted earlier, it was to be expected that a second-order theory would be successful in this particular application because the pseudopotential matrix elements involved in the perturbation expansion are small.

For transition metals, on the other hand, it is unlikely that such a simple theory will suffice because the resonant scattering of $d$ electrons by transition-metal ions leads to large matrix elements and, hence, to slower convergence of the perturbation expansion. Indeed, even for the noble metals, where one might hope that the effects of resonant scattering are not too pronounced, calculated stacking-fault energies based on a second-order approximation are in poor agreement with experimental results. $^{1,2}$ It seems clear, therefore, that a successful theory of stacking-fault energies in transition metals, and perhaps the noble metals as well, must include the effects of higher-order terms in the perturbation expansion. $^{4}$ The purpose of the work reported here was to see if an extension to third order will adequately account for observed trends in the stacking-fault energies and relative stabilities of close-packed transition metals.

In analogy with Harrison's formulation of the second-order theory $^{5}$ of stacking-fault energies, one might attempt a third-order calculation by making use of the formal expression $^{6}$ for the third-order energy in terms of the plane-wave matrix elements of the pseudopotential and the structure factors for the perfect and faulted crystal. It is well known, however, that calculations of third-order energies by this method are extremely complex, even for perfect nontransition-metal crystals. $^{7,8}$ Since the prospect of extending such a calculation to stacking faults with the additional complication of resonant scattering is indeed formidable, for the investigation reported here we choose an alternative, approximate approach based on the theory of multi-ion interactions. $^{9,10}$

In short, our approach is based on Harrison's observation that the third-order term in the perturbation expansion of the total energy can be written as a sum of three-ion interaction energies. $^{9}$ The third-order term in the expression for the stacking-fault energy is therefore the difference between the three-ion sum for the faulted crystal and the corresponding sum for the perfect crystal. By truncating these sums, i. e., by keeping only those three-ion interactions judged to be dominant in the determination of the stacking-fault energy, we obtain an approximation to the third-order energy.

In the text of this paper we will first describe in more detail the method for calculating the third-order energy. An approximate method for estimating the second-order energy will then be derived, followed by a discussion of the electron-ion scattering model used in numerical computations. The results of our study, which are presented in the concluding section, show that for most transition metals it is the three-ion terms, not pairwise interactions, that comprise the dominant contribution to the stacking-fault energy. Although quantitative agreement with experimental data on stacking-fault energies is only fair, the calculations do adequately explain observed trends in the relative stabilities of close-packed structures for the first three transition-metal series.

## II. CALCULATION OF THE THREE ION ENERGY

Our starting point is the following general expression for the three-ion contribution to the stacking-fault energy:
$$
\begin{aligned}
\gamma_{3}= & \frac{1}{2 A} \sum_{i} \sum_{\substack{j \neq i \\
k \neq j \\
k \neq i}} \sum\left[v_{3}\left(\overrightarrow{\mathrm{R}}_{i}^{F}, \overrightarrow{\mathrm{R}}_{j}^{F}, \overrightarrow{\mathrm{R}}_{k}^{F}\right)\right. \\
& \left.-v_{3}\left(\overrightarrow{\mathrm{R}}_{i}^{P}, \overrightarrow{\mathrm{R}}_{j}^{P}, \overrightarrow{\mathrm{R}}_{k}^{P}\right)\right],
\end{aligned}
$$
where $\overrightarrow{\mathrm{R}}_{i}^{F}$ and $\overrightarrow{\mathrm{R}}_{i}^{P}$ are ion positions in the faulted $(F)$ and perfect $(P)$ crystals, $A$ is the fault area, and $v_{3}$ is the three-ion interaction energy defined in Ref. 10. Since $v_{3}$ already includes a sum over
---
13
5131
---

cyclic permutations of ion positions (i. e., a sum of identical three-ion diagrams) only distinct diagrams are to be included in the sums on $i$, $j$, and $k$. Also, terms in which all three ion positions lie on the same side of the fault plane do not contribute be- cause in such cases the three-ion energies are the same in the faulted and perfect crystals. Thus the only diagrams that need be considered are those distinct diagrams where two of the position vectors terminate on opposite sides of the fault plane. We therefore choose $\vec{R}_{i}$ to be the position of an ion on one side of the fault plane and $\vec{R}_{k}$ a position on the opposite side, with $\vec{R}_{j}$ on either side.

Figure 1 is an example of a pair of three ion con- figurations that give a nonvanishing contribution in the calculation of the intrinsic fault energy in an fcc crystal. Here $\vec{R}_{i}$ and $\vec{R}_{j}$ are the same in the per fect and faulted structures while $\vec{R}_{k}$ terminates at the positions indicated by $\vec{R}_{k}^{P}$ and $\vec{R}_{k}^{F}$ in the perfect and faulted crystals, respectively.

For this particular geometrical arrangement, it is easily seen that for each ion position $\vec{R}_{j}$ below the fault plane there are three equivalent diagrams corresponding to the three nearest-neighbor posi- tions of $\vec{R}_{i}$. Also, there are three more equivalent diagrams in the mirror-image configuration in which $\vec{R}_{k}$ and $\vec{R}_{j}$ terminate above the plane while $\vec{R}_{i}$ lies below. Thus, assuming that the energy dif- ference in Eq. (1) is the same for all $\vec{R}_{j}$ below the fault plane, we obtain, for that part of the stacking fault energy due to the interactions illustrated in Fig. 1,
$$\Delta \gamma_{3}=(1 / 2 \omega)\left(6 v_{3}^{A B A}-6 v_{3}^{A B C}\right),$$
where $\omega$ is the area per ion and $v^{A B A}$ and $v^{A B C}$ are the energies corresponding to the particular dia- grams considered here. Similar arguments can, of course, be applied to other three-ion configura- tions thus leading to the formula

$$\gamma_{3}=\frac{1}{2 \omega}\left(\sum_{i} N_{i}^{F} v_{3}^{F}(i)-\sum_{i} N_{i}^{P} v_{3}^{P}(i)\right),\qquad(2)$$

where $N_{i}^{F}$ is the number of equivalent diagrams of the $i$ th geometry in the faulted crystal. $v_{3}^{F}(i)$ is the corresponding energy, the $N_{i}^{P}$ and $v_{3}^{P}(i)$ are the diagram weights and energies for the perfect fcc structure, and the sum is over all nonequivalent three-ion diagrams.

![](./images/812741393272274945_1.jpg)

FIG. 1. Typical pair of three-ion interactions that con- tribute to the intrinsic stacking-fault energy for face- centered-cubic crystals. Here $\vec{R}_{k}^{P}$ and $\vec{R}_{k}^{F}$ are ion posi tions in the perfect $(P)$ and faulted $(F)$ crystals, while $\vec{R}_{i}$ and R, are the same in both cases.

![](./images/812741393272274945_2.jpg)

FIG. 2. Schematic illustration of three-ion interac- tions. Terms included in the truncated stacking-fault energy sum were those for which either $\alpha \leqslant 30^{\circ}$ or $R$ ≤20 a.u.

In the applications discussed in Sec. V, the only diagrams considered were those for which at least two of the three ions were nearest neighbors and for which the third ion was in either the adjacent or next-nearest plane, as illustrated in Fig. 2. In addition, the sums over diagrams were limited to terms for which either $\alpha \leqslant 30^{\circ}$ or $R \leqslant 20$ a.u.(see Fig. 2). While the truncation of the sums at these particular values of $\alpha$ and $R$ is somewhat arbitrary, it can be seen from the expression for $v_{3}$ given in Ref. 10 that the three-ion energy is in- versely proportional to the product of the three in- terior path lengths times the roundtrip distance, thus causing $v_{3}$ to fall off rather rapidly with in creasing $R$. Also, because the resonant scattering terms in $v_{3}$ contain products of the Legendre poly nomials $P_{2}(\cos \Theta_{i})$, where $\Theta_{i}$ is the scattering an gle at the $i$ th ion site, the energy tends to be larg er for diagrams with $\alpha \approx 0$ than for diagrams with larger $\alpha$. Actual computations of $v_{3}$ confirmed these expected trends, in that they showed that en- ergies corresponding to the larger values of $\alpha$ and $R$ are small, usually about $10 \%$ of the dominant terms. Still, it should be noted that in some cases the larger terms tend to cancel and, when this hap- pens, the truncation error can be significant. We will return to this point when discussing the results of our computations in Sec. V.

### III. CALCULATION OF THE PAIRWISE INTERACTION ENERGY

To calculate that part of the stacking fault en- ergy due to pairwise interactions we used the for-

malism of Blandin et al. $^{11}$ They showed that the pairwise contribution to $\gamma$ can be written

$$
\gamma_{2}=\sum_{n=2}^{\infty} N(n) \Delta \phi(n h),
$$

where $h$ is the distance between close-packed planes, $N(n)$ is an integral weight corresponding to a particular fault configuration, and $\Delta \phi(n h)$ is an interplanar potential difference. $^{1,3}$ Blandin et al., also showed that the potential difference is related to the energy-wave number character- istic $\Phi(q)$ as follows:

$$
\Delta \phi(n h) \approx \frac{9 h}{\pi \omega} \int_{-\infty}^{\infty} \Phi\left[\left(q_{z}^{2}+g^{2}\right)^{1 / 2}\right] e^{i q_{z} n h} d q_{z}, \quad (3)
$$

where $g$ is the magnitude of the smallest nonvan ishing reciprocal-lattice vector.

From the Fourier transform relationship $^{3}$ between $\Phi(q)$ and the pairwise interaction energy $v_{2}$,we find, using the asymptotic approximation, $^{10}$

$$
v_{2}(R) \sim-\frac{2}{\pi} \int_{0}^{E_{F}} \operatorname{Im} e^{2 i \kappa R} \frac{f^{2}(E, \pi)}{R^{2}} d E
$$

that for $q>2 \kappa_{F}$, where $\kappa_{F}$ is the Fermi wave number,

$$
\begin{aligned}
\Phi(q) \approx-\frac{4}{q \Omega_{0}} \int_{0}^{E_{F}}|f(E, \pi)|^{2} & \left(\frac{1}{2} \cos 2 \eta \ln \left|\frac{q+2 \kappa}{q-2 \kappa}\right|\right. \\
& \left.+\frac{\pi}{2} \sin 2 \eta\right) d E \quad(4)
\end{aligned}
$$

where $\Omega_{0}$ is the volume per ion, $f(E, \pi)$ is the scattering amplitude at energy $E$ and scattering angle $\pi$, and $\kappa=\sqrt{E}$. The angle $\eta$ is defined in terms of the scattering phase shifts $\delta_{l}$ by $\tan \eta=\alpha / \beta$, where

$$
\alpha=\sum_{l}(-1)^{l}(2 l+1) \cos \delta_{l} \sin \delta_{l},
$$

$$
\beta=\sum_{l}(-1)^{l}(2 l+1) \sin ^{2} \delta_{l}.
$$

The condition $q>2 \kappa_{F}$ is satisfied here because, from Eq. (3), $q \geqslant g$ and $g>2 \kappa_{F}$ for all transition metals. Substitution of Eq. (4) in Eq. (3) gives, to first order in $1 / n h$ and neglecting terms of order $\exp (-g n h)$

$$
\Delta \phi(n h) \approx \frac{18}{n h \omega^{2}} \int_{0}^{E_{F}}|f(E, \pi)|^{2} \cos 2 \eta \frac{e^{-2 \lambda_{z} n h}}{\sqrt{E}} d E,
$$

where

$$
\lambda_{z}=\left[\left(\frac{1}{2} g\right)^{2}-E\right]^{1 / 2}.
$$

In applying this result in the computations described below the final integration was numerically evaluated, and only the term corresponding to next-nearest-neighbor plane interactions $(n=2)$ was retained in the stacking fault energy sum.

## IV. CALCULATION OF PHASE SHIFTS

Our choice of a model for the calculation of scattering phase shifts for transition metal ions is based largely on the work of Pettifor. $^{12}$ He showed that one can reproduce, with reasonable accuracy, the results of more detailed calculations of the densities of states of transition metals, by basing a simpler calculation on the assumption that the $d$-electron resonance energy $E_{r}$ and width $\Delta$ are constants for the first three transition-metal series. In the calculation reported here we made the additional approximations that the nonresonant scattering phase shifts can be derived from a pseudopotential which, again, is the same for all elements, and that the nearest-neighbor distance is the same (5.0 a.u.) for all elements. This leaves us with a rather simple calculational model in which the only parameter that distinguishes one element from the next is the Fermi energy. However, except for the approximation concerning phase shifts for nonresonant scattering, this is the same model used by Pettifor in his calculations of the relative energies of the hcp, fcc, and bcc structures. The fact that Pettifor's results are in accord with the observed structures of transition metals suggests that the model, through obviously an idealization, forms a reasonable basis for the study of stacking fault energies as well.

For the resonance parameters we used Moriarty's values for copper $^{13}(E_{r}=0.33$ Ry and $\Delta=0.014$ Ry). Fermi energies as a function of valence $Z$ were determined by adding an average of Pettifor's calculated values of $E_{F}-E_{r}$ for the fcc and hcp structures to the value chosen for $E_{r}$. The value of the resonant part of the $d$ electron phase shift was determined from the formula

$$
\tan \left(\delta_{2}-\delta_{b}\right)=\Delta /\left(E_{r}-E\right),
$$

where $\delta_{2}$ and $\delta_{b}$ are the resonant and nonresonant parts of the $l=2$ phase shift.

To calculate the nonresonant scattering phase shifts we used the empty core potential, the core radius being that given by Ashcroft and Langreth $^{14}$ for copper. The phase shifts were calculated in the first Born approximation and were based on the uniform screening charge assumption. $^{15}$ Because there is considerable uncertainty as to the validity of such a simple model, we performed two sets of calculations using effective valences $\left(Z_{s}\right)$ of one and two in the nonresonant scattering pseudopotential.

## V. RESULTS AND DISCUSSION

The results of our calculations are shown in Fig.3. These plots show the stacking fault energy for intrinsic faults in fcc crystals as a function of $Z$,

![](./images/812741393272274945_3.jpg)

FIG. 3. Calculated intrinsic stacking-fault energies for face-centered-cubic crystals. The parameter $Z_s$ is the valence assumed in the calculation of nonresonant scattering phase shifts. The dashed parts of the curves correspond to values of the total valence (including $d$ electrons) where neither close-packed structure is stable. Experimental data, shown here by the symbol $\times$, are taken from Ref. 16 for copper ($Z$=11) and nickel-cobalt alloys ($9< Z<10$), and from Ref. 17 for cobalt ($Z$=9).

the total valence, for both values of $Z_s$. The dashed part of the curve corresponds to those values of $Z$ where neither close-packed structure is stable and where, therefore, no comparisons with observed stable structures or stacking fault energies are possible. Also shown are experimental data for cobalt ($Z$=9), nickel ($Z$=10), copper ($Z$=11), and cobalt-nickel alloys. The stacking fault energy for hcp cobalt is shown as a negative number because the theoretical expression for the energy of an intrinsic fault in an hcp crystal is approximately equal to minus the expression for the intrinsic fcc energy. As can be seen from the stacking sequences for the perfect and faulted crystals, this relationship is exact if one ignores all interactions involving third and more distant neighbors planes.

The first point to be noted here is that the two calculated curves are in reasonably good agreement for most values of $Z$. Since these two curves are based on nonresonant scattering phase shifts that differ by about a factor of 2, this must mean that the details of nonresonant scattering are relatively unimportant, and that the general trend of stacking fault energy versus valence is determined largely by resonant scattering properties. It should be noted, however, that the resonance width $\Delta$, which we have taken from Moriarty's calculation, is related to nonresonant scattering properties through hybridization. One would therefore expect that a first-principles calculation would show a stronger dependence on nonresonant scattering properties than is indicated here.

Another point to be noted regarding Fig. 3 is that the stability of the fcc phase against faulting is correctly predicted for most values of $Z$. Thus, for $Z>9$ we obtain positive values, which indicates stability against faulting in fcc crystals, while for $6< Z<9$ and $Z<4$, where the stable close-packed structure is hcp, we obtain negative fault energies. The only notable exception is the $Z_s$=2 curve at $Z$=4 (titanium, zirconium, and hafnium), where the calculation indicates that the fcc structure is stable. This failure may well be due to the approximate treatment of nonresonant scattering, since the energy for $Z_s$=1 has the correct sign. On the other hand, the fact that the absolute value stacking fault energy is much smaller at $Z$=4 than at other values of $Z$ indicates that there is considerable cancellation in the sum of two- and three-ion interaction energies, and that the truncation error mentioned above may therefore be significant. It should also be noted that a similar situation exists at $Z$=9 (cobalt, rhodium, and iridium). Here, however, one of the elements (cobalt) is in fact stable in the hcp phase, while the other two form stable fcc crystals.

It is of interest to compare these results with Pettifor's calculations of the relative energies of close-packed phases. $^{12}$ As was noted previously, our assumptions of constant resonance parameters and nearest-neighbor distance are consistent with Pettifor's model although he used different numerical values for the resonance parameters. However, the principal difference between his model and ours lies in the treatment of nonresonant scattering. In spite of these differences our results for the relative stabilities of the fcc and hcp structures as a function of $Z$ are in reasonably good agreement with Pettifor's. Thus he finds that there is a region of hcp stability near $Z$=4 followed by an fcc stable region near $Z$=5, an fcc to hcp transition near $Z$=7 and finally, an hcp to fcc transition near $Z$=9. We take this, and the fact that the results agree with observed trends in crystal structure, as indications that our simple scattering model is adequate as a first approximation, and that we have included the most significant terms in our approximate summation of the multi-ion expansion.

Regarding the calculated values of the stacking-fault energies, as can be seen in Fig. 3, agreement with experimental data is satisfactory for copper and cobalt, but poor for nickel and cobalt-nickel alloys. In view of the very simple model that was used in calculating electron-ion scattering

![](./images/812741393272274945_4.jpg)

FIG. 4. Pairwise $(\gamma_{2})$ and three-ion $(\gamma_{3})$ contributions to the stacking fault energy for $Z_{s}=1$. At almost all values of the valence the three-ion energy is much greater than the pairwise contribution, which is multiplied by 10 in this plot.

phase shifts, we do not consider these comparisons particularly significant, except, perhaps, as an indication that a more careful treatment is needed for quantitative comparisons with experiment.

Finally, in Fig. 4 we show the two- and three-ion contributions to the stacking fault energy for $Z_{s}=1$ (the results for $Z_{s}=2$ are similar). The important point to be noted here is that three-ion interactions dominate at almost all values of $Z$. Although one might expect, on the basis of our earlier calculation for the noble metals, $^{1}$ that a more accurate nonasymptotic calculation would yield larger values for the pairwise contribution, we still believe that the dominance of three-ion terms exhibited here is at least qualitatively correct.
One reason for this is that the pairwise energies are so small compared to three-ion energies that the errors introduced through the asymptotic approximation, being roughly of the same order of magnitude as the pairwise predictions themselves, $^{1}$ are expected to be insignificant compared to the three-ion energies.

Another reason is that from Pettifor's calculation, and from the observed stability of close-packed phases as a function of $Z$, one would expect three hcp-fcc transitions in a transition metal series. The three-ion energy does, in fact, show three such transitions while the pairwise energy has only two. Thus assuming only that the shapes of the two- and three-ion curves shown in Fig. 4 are correct, one would expect three-ion contributions to dominate.

In conclusion, therefore, we have demonstrated that observed trends in the stabilities of close-packed transition metals can be explained on the basis of a third-order calculation involving a simple resonant scattering model of electron-ion interactions. The calculations indicate that such trends are governed largely by three-ion interactions at most values of the valence. Comparisons with experimentally measured stacking-fault energies show, as expected, that a more careful treatment is needed for quantitative predictions of stacking-fault energies. Still, the degree of success realized in the prediction of structural trends and, at least, the correct sign and order of magnitude of stacking-fault energies, supports our principal conclusions regarding the dominant roles of resonant scattering and three-ion interactions.

## ACKNOWLEDGMENT

This work was supported in part by the U. S. Army Research Office.

$^{1}$ R. E. Beissner, Phys. Rev. B $\underline{8}$, 5432 (1973).
$^{2}$ J. F. Devlin, J. Phys. F $\underline{4}$, 1865 (1974).
$^{3}$ V. Heine and D. Weaire, Solid State Phys. $\underline{24}$, 249 (1970).
$^{4}$ An alternative approach based on the tight-binding approximation but ignoring $s-d$ hybridization is suggested by F. Ducastelle and F. Cyrot-Lackmann, J. Phys. Chem. Solids $\underline{32}$, 285 (1971). See also, T. C. Tisone, Acta Met. $\underline{21}$, 229 (1973).
$^{5}$ W. A. Harrison, Pseudopotentials in the Theory of Metals (Benjamin, New York, 1966).
$^{6}$ P. Lloyd and A. Sholl, J. Phys. C $\underline{1}$, 1620 (1968).
$^{7}$ E. G. Brovman, Yu. Kagan, and A. Holas, Zh. Eksp. Teor. Fiz $\underline{61}$, 737 (1971) [Sov. Phys.-JETP $\underline{34}$, 394 (1972)].
$^{8}$ C. M. Bertoni, V. Bortolani, C. Calandra, and F. Nizzoli, J. Phys. F $\underline{3}$, L244 (1973).
$^{9}$ W. A. Harris, Phys. Rev. B $\underline{7}$, 2408 (1973).
$^{10}$ R. E. Beissner, Phys. Rev. B $\underline{9}$, 5108 (1974).
$^{11}$ A. Blandin, J. Friedel, and G. Saada, J. Phys. C Suppl. $\underline{3}$, 128 (1966).
$^{12}$ D. G. Pettifor, J. Phys. C $\underline{3}$, 367 (1970).
$^{13}$ J. A. Moriarty, Phys. Rev. B $\underline{6}$, 1239 (1972).
$^{14}$ N. W. Ashcroft and D. C. Langreth, Phys. Rev. $\underline{159}$, 500 (1967).
$^{15}$ R. W. Shaw, Jr., Phys. Rev. B $\underline{5}$, 4742 (1972).
$^{16}$ P. C. J. Gallagher, Met. Trans. $\underline{1}$, 2429 (1970).
$^{17}$ T. Ericsson, Acta Metallogr. $\underline{14}$, 853 (1966).