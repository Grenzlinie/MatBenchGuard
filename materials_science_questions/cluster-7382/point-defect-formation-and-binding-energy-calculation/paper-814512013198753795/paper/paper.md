# Vacancy-Vacancy Interaction in Copper

V. G. WEIZER AND L. A. GIRIFALCO
Lewis Research Center, National Aeronautics and Space Administration, Cleveland, Ohio

(Received June 16, 1960)

The binding energy of two vacancies in a static lattice as a function of their separation and the positions of their displaced neighboring atoms has been calculated using a Morse potential function model for copper. It was found that two vacancies attract one another at separation less than about 7 A. At separations greater than 7 A the vacancies do not interact appreciably. The most stable separation was found to be the first-nearest-neighbor separation or the divacancy configuration, for which the binding energy was found to be 0.64 ev. Based on these calculations, it is shown that third-stage annealing in irradiated copper may be accounted for by divacancy migration. The role of the divacancy in copper self-diffusion is also explained.

## INTRODUCTION

A NUMBER of solid-state phenomena, such as void formation and radiation damage annealing, are concerned with the interactions of lattice defects with one another. The vacancy-vacancy interaction in a static lattice, because of its simplicity, is the object of study in this paper. Both the energy of interaction of two vacancies as a function of their separation and the positions of their displaced neighboring atoms have been calculated using a Morse potential function model for copper.

The Morse crystal employed consists of a 20×20×20-atom face-centered cubic lattice, which is equivalent to an infinite lattice for calculations performed on defects located near the center.

The energy of interaction, $\Phi_{ij}$, between two isolated atoms, $i$ and $j$, as a function of their separation, $r_{ij}$, is given by the Morse potential function as
$$\phi_{ij}=D\left[e^{-2\alpha\left(r_{ij}-r_{0}\right)}-2e^{-\alpha\left(r_{ij}-r_{0}\right)}\right], \tag{1}$$
where $D$ is the dissociation energy of the pair, $r_{0}$ is the equilibrium separation, and $\alpha$ is a constant.

The energy of interaction of one atom $i$ with every other atom $j$ in the lattice is
$$\phi_{i}{ }^{\prime}=D\left[\sum_{j} e^{-2\alpha\left(r_{j}-r_{0}\right)}-2 \sum_{j} e^{-\alpha\left(r_{j}-r_{0}\right)}\right]. \tag{2}$$

To facilitate the calculation of interaction energies between two atoms neither of which is at the origin of the coordinate system, the origin is translated through a vector $\delta_{1}, \delta_{2}, \delta_{3}$. If the following substitutions are made in Eqs. (1) and (2):
$$\beta=e^{\alpha r_{0}},$$
$$r_{ij}=\left[\left(m_{ij}-\delta_{1}\right)^{2}+\left(n_{ij}-\delta_{2}\right)^{2}+\left(l_{ij}-\delta_{3}\right)^{2}\right]^{\frac{1}{2}} a,$$
then
$$\begin{aligned}
\phi_{ij}=D\{ & \beta^{2} \exp \left[-2 \alpha a\left(\left(m_{ij}-\delta_{1}\right)^{2}+\left(n_{ij}-\delta_{2}\right)^{2}\right.\right. \\
& \left.\left.+\left(l_{ij}-\delta_{3}\right)^{2}\right)^{\frac{1}{2}}\right]-2 \beta \exp \left[-\alpha a\left(\left(m_{ij}-\delta_{1}\right)^{2}\right.\right. \\
& \left.\left.\left.+\left(n_{ij}-\delta_{2}\right)^{2}+\left(l_{ij}-\delta_{3}\right)^{2}\right)^{\frac{1}{2}}\right]\right\}, \tag{3}
\end{aligned}$$
and
$$\begin{aligned}
\phi_{i}{ }^{\prime}=D\{ & \beta^{2} \sum_{j} \exp \left[-2 \alpha a\left(\left(m_{j}-\delta_{1}\right)^{2}+\left(n_{j}-\delta_{2}\right)^{2}\right.\right. \\
& \left.\left.+\left(l_{j}-\delta_{3}\right)^{2}\right)^{\frac{1}{2}}\right]-2 \beta \sum_{j} \exp \left[-\alpha a\left(\left(m_{j}-\delta_{1}\right)^{2}\right.\right. \\
& \left.\left.\left.+\left(n_{j}-\delta_{2}\right)^{2}+\left(l_{j}-\delta_{3}\right)^{2}\right)^{\frac{1}{2}}\right]\right\}, \tag{4}
\end{aligned}$$
where $l_{ij}$, $m_{ij}$, and $n_{ij}$ are the position coordinates of atom $j$ with respect to atom $i$, and $a$ is the half-cell lattice spacing.

The energy of cohesion, $\Phi$, is
$$\Phi=\frac{N}{2} \varphi_{i}{ }^{\prime},$$
where $N$ is the number of atoms in the crystal.

The values of the Morse function constants used in this work are
$$\alpha=1.3588 \mathrm{~A}^{-1},$$
$$\beta=49.11,$$
$$D=0.3429 \mathrm{ev}.$$

These values were deduced from the macroscopic properties of copper. $^{1,2}$

## CALCULATIONS

The interaction energy, $E_{B}$, of two vacancies both of which are on normal lattice sites is given by
$$E_{B}=E_{N N}+E_{D R}-2 E_{V R}, \tag{5}$$
where $E_{NN}$ is the energy of interaction between two atoms at the same separation as the two vacancies, $E_{DR}$ is the relaxation energy of the atoms neighboring the pair, and $E_{VR}$ is the energy of relaxation of an isolated vacancy. $^{3}$

For convenience in performing the calculations, the interaction energy, $E_{B}$, was calculated for only four separations: first-, second-, fourth-, and eighth-nearest-neighbor separations. It was found that at the eighth-nearest-neighbor separation the vacancies exerted no appreciable effect upon each other, and thus calculations for larger separations were not performed.

The term $E_{NN}$ is calculated by means of Eq. (1). The energy of vacancy relaxation, $E_{VR}$, has been calculated by the authors in a previous publication and shown to

$^{1}$ L. A. Girifalco and V. G. Weizer, Phys. Rev. 114, 687-690 (1959).
$^{2}$ L. A. Girifalco and V. G. Weizer, National Aeronautics and Space Administration Report NASA TR R-5, 1959.
$^{3}$ L. A. Girifalco and V. G. Weizer, J. Phys. Chem. Solids 112, 260-264 (1960).

![](./images/814512013198753795_1.jpg)

FIG. 1. Vacancy-vacancy interaction energy versus separation.

be $0.56 \mathrm{ev} .^{3}$ Equation (4) is used to calculate $E_{D R}$, the lattice summations being performed on a high-speed digital computer.

The method used in calculating $E_{D R}$ is essentially the same as that used to calculate $E_{V R}{ }^{3}$ First, the atoms neighboring the pair of vacancies are grouped into symmetrical sets. In the vacancy relaxation these sets are the sets of nearest neighbors. Here, however, where the symmetry is much lower, the situation is not that simple. The criteria for placing an atom in a set are that it should be a certain distance A away from vacancy number one and a certain distance B away from vacancy number two. The first- and second-nearest neighbors to each vacancy were shown to be the only atoms contributing appreciably to the relaxation about the pair, resulting in eleven sets for the first-nearest-neighbor separation, nine sets for the second-nearest-neighbor separation, thirteen sets for the fourth-nearest-neighbor separation, and ten sets for the eighth-nearest-neighbor separation.

These sets are then displaced, one at a time, along their relaxation trajectories, and the energy of the crystal is calculated as a function of these displacements. While the first set is being displaced, the remaining sets are held in their original positions. The point of minimum crystal energy is taken to be the equilibrium position of the first set to the first approximation. These new positions of the first set are then substituted for the original positions, and the second set is displaced in a similar manner. This process is continued until all the sets have been displaced. Then, because of the displacement of the second and succeeding sets, the equilibrium position of the first set has been disturbed, and therefore the entire sequance must be repeated until further calculations yield no new results.

The order in which the sets are displaced is based upon the estimated amount of relaxation, the set relaxing the most being displaced first. It should also be noted that the original positions of the atoms neighboring the vacancies are the positions of relaxed neighbors about an isolated vacancy. $^{3}$

The relaxation trajectories can be described as follows: The atoms are first allowed to relax radially toward or away from vacancy number one. Then, using the newly calculated positions as original positions, the atoms are allowed to relax radially toward or away from vacancy number two. This process is repeated, switching from vacancy number one to vacancy number two and back again until equilibrium is reached. This, then, is the final equilibrium configuration about a pair of vacancies.

The energy of the crystal after relaxation is then subtracted from the energy of the crystal before relaxation to give the relaxation energy of the vacancy pair. The relaxation energy is then combined with $E_{N N}$ and $E_{V R}$ in Eq. (5) to obtain the interaction energy $E_{B}$.

## RESULTS

The interaction energy of two vacancies as a function of their separation is shown in Fig. 1. The points on the solid curve are the values calculated in this paper. The dotted curve is a Morse potential function which represents the interaction of two vacancies when no relaxation occurs, that is, when $E_{V R}=E_{D R}=0$.

It should be noted, however, that the only points that are meaningful on these curves are the points at the different lattice neighbor separations. Between each of these points there is an energy barrier, over which the vacancy can travel only if it has the required activation energy.

The most stable separation for the two vacancies is the first-nearest-neighbor separation called the divacancy configuration with a binding energy of $0.64 \mathrm{ev}$. This is slightly above the range of values obtained by Bartlett and Dienes. $^{4}$ Using a bond-counting technique they arrived at the limiting values of $0.23 \mathrm{ev}$ and $0.59 \mathrm{ev}$.

Table I gives the positions of the atoms around the vacancies before and after relaxation. The first set of coordinates in each group is the set of coordinates of a typical atom of the group in its normal lattice position. The second set of coordinates in each group is the position of the atom in its final relaxed position. The origin of the coordinate system is placed midway between the two vacancies in all four cases. The coordinates of the vacancies are given in the table.

For purposes of computation the atoms neighboring the vacancies were divided into sets as described previously. However, inspection of the final configuration shows that because of the mirror symmetry existing between the two vacancies, many of these sets are equivalent, thus reducing the total number of sets by

$^{4}$ S. H. Bartlett and G. J. Dienes, Phys. Rev. 89, 848-852 (1953).

VACANCY-VACANCY INTERACTION IN Cu

almost a factor of two. The grouping in Table I reflects the fact that many of the sets previously used are equivalent.

By comparison of the results of the eighth-nearest-neighbor separation calculations with the calculations performed for a single vacancy, it can be seen that the configuration about two vacancies of eighth-nearest-neighbor separation is very nearly the same as the configuration about two isolated vacancies.

The constants in the Morse function used in this paper were calculated to reflect the electron distribution of a perfect crystal. When this function is applied to an imperfect crystal, some error will probably be introduced because of the electronic redistribution. However, in these calculations, where a subtractive process is used to calculate the binding energy, the errors will at least partially cancel themselves out. Thus, these calculations should give a fairly accurate value of the binding energy of a divacancy and a reliable picture of the interaction of two vacancies.

DISCUSSION

It has been suggested by Li and Nowick⁵ that the divacancy mechanism might be responsible for third-stage annealing⁶ in deuteron-irradiated copper which shows an activation energy of 0.69 ev at about 220°K.⁷⁻¹⁰ Following this suggestion and noting Overhauser's⁷ observation that the third-stage annealing mechanism is bimolecular, it might be assumed that the process involves the migration of divacancies to the less mobile vacancies, which in this case act as sinks for the divacancies. The combination of a divacancy with a vacancy would form a trivacancy, which has been shown to be quite immobile in copper.¹¹

If one then uses the value of 0.69 ev for the energy of migration of a divacancy in copper, $E_{m}{}^{D}$, 1.0 ev for the energy of formation of a vacancy,¹² $E_{f}{}^{V}$, and 0.64 ev for the binding energy of a divacancy, $E_{B}$, then the activation energy for divacancy diffusion, $E_{D}{}^{D}$, given by

$$E_{D}{}^{D}=2E_{f}{}^{V}-E_{B}+E_{m}{}^{D}$$

is calculated to be 2.05 ev.

<table>
<caption>Table I. Positions of atoms around a pair of vacancies before and after relaxation at different separations. See text.</caption>
<tbody>
<tr>
<td colspan="4">
First-nearest-neighbor
separation, vacancies
located at $-\frac{1}{2}, -\frac{1}{2},$
0, and $\frac{1}{2}, \frac{1}{2}, 0$
</td>
<td colspan="4">
Second-nearest-neighbor separation, va-
cancies located at
1, 0, 0, and $-1, 0, 0$
</td>
</tr>
<tr>
<td>Group</td>
<td colspan="3">Coordinates</td>
<td>Group</td>
<td colspan="3">Coordinates</td>
</tr>
<tr>
<td>1</td>
<td>0.50</td>
<td>−0.50</td>
<td>1.00</td>
<td>1</td>
<td>0.0</td>
<td>1.00</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>0.46</td>
<td>−0.46</td>
<td>0.92</td>
<td></td>
<td>0.0</td>
<td>0.96</td>
<td>0.0</td>
</tr>
<tr>
<td>2</td>
<td>−1.50</td>
<td>0.50</td>
<td>0.0</td>
<td>2</td>
<td>1.00</td>
<td>1.00</td>
<td>1.00</td>
</tr>
<tr>
<td></td>
<td>−1.49</td>
<td>0.49</td>
<td>0.0</td>
<td></td>
<td>0.99</td>
<td>0.98</td>
<td>0.98</td>
</tr>
<tr>
<td>3</td>
<td>−1.50</td>
<td>−0.50</td>
<td>1.00</td>
<td>3</td>
<td>2.00</td>
<td>1.00</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>−1.48</td>
<td>−0.50</td>
<td>0.98</td>
<td></td>
<td>1.98</td>
<td>0.97</td>
<td>0.0</td>
</tr>
<tr>
<td>4</td>
<td>−1.50</td>
<td>−1.50</td>
<td>0.0</td>
<td>4</td>
<td>1.00</td>
<td>2.00</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>−1.48</td>
<td>−1.48</td>
<td>0.0</td>
<td></td>
<td>1.02</td>
<td>2.02</td>
<td>0.0</td>
</tr>
<tr>
<td>5</td>
<td>−0.50</td>
<td>−0.50</td>
<td>2.00</td>
<td>5</td>
<td>3.00</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>−0.50</td>
<td>−0.50</td>
<td>2.00</td>
<td></td>
<td>3.01</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td>6</td>
<td>−2.50</td>
<td>−0.50</td>
<td>0.0</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>−2.51</td>
<td>−0.50</td>
<td>0.0</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="4">
Fourth-nearest-neighbor
separation, vacancies
located at 1, 0, 1,
and $-1, 0, -1$
</td>
<td colspan="4">
Eighth-nearest-neighbor separation, va-
cancies located at
−2, 0, 0, and 2, 0, 0
</td>
</tr>
<tr>
<td>Group</td>
<td colspan="3">Coordinates</td>
<td>Group</td>
<td colspan="3">Coordinates</td>
</tr>
<tr>
<td>1</td>
<td>1.00</td>
<td>0.0</td>
<td>−1.00</td>
<td>1</td>
<td>1.00</td>
<td>1.00</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>1.01</td>
<td>0.0</td>
<td>−1.01</td>
<td></td>
<td>1.02</td>
<td>0.98</td>
<td>0.0</td>
</tr>
<tr>
<td>2</td>
<td>0.0</td>
<td>1.00</td>
<td>1.00</td>
<td>2</td>
<td>2.00</td>
<td>1.00</td>
<td>1.00</td>
</tr>
<tr>
<td></td>
<td>0.03</td>
<td>0.98</td>
<td>1.01</td>
<td></td>
<td>2.00</td>
<td>0.98</td>
<td>0.98</td>
</tr>
<tr>
<td>3</td>
<td>0.0</td>
<td>0.0</td>
<td>2.00</td>
<td>3</td>
<td>2.00</td>
<td>2.00</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>0.03</td>
<td>0.0</td>
<td>1.99</td>
<td></td>
<td>2.00</td>
<td>2.01</td>
<td>0.0</td>
</tr>
<tr>
<td>4</td>
<td>1.00</td>
<td>2.00</td>
<td>1.00</td>
<td>4</td>
<td>3.00</td>
<td>1.00</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>1.00</td>
<td>2.01</td>
<td>1.00</td>
<td></td>
<td>2.98</td>
<td>0.98</td>
<td>0.0</td>
</tr>
<tr>
<td>5</td>
<td>1.00</td>
<td>1.00</td>
<td>2.00</td>
<td>5</td>
<td>4.00</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td></td>
<td>1.00</td>
<td>0.99</td>
<td>1.99</td>
<td></td>
<td>4.01</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td>6</td>
<td>2.00</td>
<td>0.0</td>
<td>2.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>1.97</td>
<td>0.0</td>
<td>1.97</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>3.00</td>
<td>0.0</td>
<td>1.00</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>3.01</td>
<td>0.0</td>
<td>1.01</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

The activation energies for diffusion for both vacancies and divacancies are thus seen to be equal. This would explain why, if divacancies contribute to diffusion, no deviation from linearity is seen in experimental $\ln D$ against $1/T$ curves.

From these calculations, then, one is led to believe that the divacancy is probably responsible for third-stage annealing in copper and is also active in the mechanism of self-diffusion in copper.

⁵ C. Y. Li and A. S. Nowick, Phys. Rev. 103, 294 (1956).

⁶ G. J. Dienes and G. H. Vineyard, *Radiation Effects in Solids* (Interscience Publishers, Inc., New York, 1957), p. 163.

⁷ A. W. Overhauser, Phys. Rev. 91, 448 (1953); Phys. Rev. 94, 1551 (1954).

⁸ H. G. Cooper, J. S. Koehler, and J. W. Marx, Phys. Rev. 97, 599 (1955).

⁹ R. R. Eggleston, Acta Met. 1, 683 (1953).

¹⁰ M. J. Druyvesteyn and J. A. Manintveld, Nature 168, 868 (1951); J. A. Manintveld, Nature 169, 623 (1952).

¹¹ A. C. Damask, G. J. Dienes, and V. G. Weizer, Phys. Rev. 113, 781 (1959).

¹² G. Airoldi, G. L. Bacchella, and E. Germagnoli, Phys. Rev. Letters 2, 145 (1959).