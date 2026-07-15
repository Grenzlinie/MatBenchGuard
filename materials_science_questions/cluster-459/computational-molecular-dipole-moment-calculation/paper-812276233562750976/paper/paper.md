# On the Multiple-Minima Problem in the Conformational Analysis of Polypeptides.
## I. Backbone Degrees of Freedom for a Perturbed $\alpha$-Helix $^{\boldsymbol{1}}$

LUCJAN PIELA* and HAROLD A. SCHERAGA, $^\dagger$
Baker Laboratory of Chemistry, Cornell University, Ithaca, New York, 14853-1301

### Synopsis

The multiple-minima problem is the most formidable in the conformational analysis of polypeptides. Several approaches have been developed to surmount this problem, and we present an additional one here that may possibly be extendable to very large polypeptides. In this new approach, designated the Self-Consistent Electric Field (SCEF) method, we calculate the electric field, due to the whole molecule, at each CO and NH group of the peptide units, and also in the middle of the C'N peptide bonds, for an arbitrary starting conformation. It is assumed that the native conformation has approximately optimal orientations of its group dipoles in the electric field. The direction of the electric field with respect to the CO and NH bond dipole moments provides information as to which peptide units are the worst oriented. We then compute the changes in the backbone dihedral angles $\phi$ and $\psi$ required to align the most unfavorably oriented peptide-unit dipole moments along the electric field. After carrying out such alignment of dipoles, a complete potential energy function is used in a minimization procedure to locate the nearest local minimum. The SCEF and energy-minimization procedures are then applied iteratively to try to locate the global minimum. The effectiveness of this method is illustrated by computations on very different starting conformations of terminally blocked 19-residue chains of poly(L-alanine), for which the global minimum is judged to be the right-handed $\alpha$-helix.

### INTRODUCTION

It is well-known that the main obstacle hampering the attainment of the global minimum in conformational energy calculations on polypeptides and proteins is the presence of an inordinately large number of minima in the multidimensional conformational energy hypersurface.$^{1}$ For a small polypeptide of 100 amino acids, the number is of the order of $10^{100}$; for comparison, the number of atoms in the universe is of the order of $10^{80}$. Several approaches have been used to try to overcome this problem,$^{2-8}$ but so far they have been limited to chains that are shorter than six residues for methods exploring the whole conformational space,$^{2-5,7,8}$ and 20-30 residues for the so-called "build-up" procedure.$^{6}$ For longer chains, these methods become very inefficient, and we explore here a new method that may possibly be extendable to longer chains.

$^{1}$This article is dedicated to Ephraim Katchalski-Katzir on the occasion of his 70th birthday.
*On leave from the University of Warsaw, Faculty of Chemistry, Pasteura 1, 02-093 Warsaw, Poland, 1984-1986.
$^\dagger$To whom requests for reprints should be addressed.

Biopolymers, Vol. 26, S33-S58 (1987)
© 1987 John Wiley & Sons, Inc.
CCC 0006-3525/87/02S0033-S26$04.00

This new approach is based on the hypothesis that low-energy conforma- tions must also be of favorable electrostatic interactions. While other interac- tions, such as hydrophobic interactions, $^{9}$ undoubtedly play an important role in initiating protein folding, all except the electrostatic interactions are of short range. Therefore, in order that distant parts of the chain may recognize and approach each other, the total electrostatic interactions in the system must play the dominant role, presumably even in water. Then, as remote parts of the chain come together, the other types of interaction come into play.

The dominance of electrostatic interactions has been discussed frequently in the literature (see, e.g., Refs. 10-23). Heretofore, however, this work was limited mainly to showing that
1. the orientations of the CO and NH dipoles in an $\alpha$-helix are very favorable electrostatically $^{12}$ and, therefore, an $\alpha$-helix has a large dipolemoment $^{12,13}$;
2. the electric field produced by an $\alpha$-helix in a protein is a very importantfactor stabilizing the native conformation $^{14}$;
3. the formation of a regular backbone structure may be influenced by electrostatic interactions $^{10,16,22,23}$; and
4. the relative orientations of $\alpha$-helices and $\beta$-sheets in proteins are favorable electrostatically. $^{11,17,20}$

Of course, other interactions also must be taken into account, e.g., repulsive contributions are certainly comparable in magnitude; without them, the molecule would collapse and the electrostatic energy would approach $-\infty$. However, they come into play only when the interacting atoms (or groups of atoms) are near one another. It is assumed, therefore, that the native confor- mation arises when the electrostatic interactions are optimal (and is only modulated by other interactions).

In the present paper, we use this assumption to search for the global or native minimum of the energy of a polypeptide when its starting conforma- tion differs more and more from the native one. Since the electrostatic interactions are directional, we are able to compute the direction in which to move in conformational space to achieve this goal.

# SELF-CONSISTENT ELECTROSTATIC FIELD METHOD

In this initial paper, we are interested only in the backbone conformations of polypeptides and will not attempt to study side-chain conformations from the point of view of their optimal orientation in the electric field (although the side chains participate in creating the electric field in the molecule); this additional problem is under study in our laboratory. To simplify the system studied, we consider a poly(L-alanine) chain. We assume that the electrostatic energy of the peptide units in the electric field produced by all charges (including those on the methyl groups of the alanines) within the molecule should be approximately optimal; i.e., all rotatable peptide units must adopt approximately the electrostatically best positions. The charges that create the electric field are the atomic charges used in the standard Empirical Conforma- tional Energy Program for Peptides (ECEPP/2), $^{24}$ and the dielectric constant $\epsilon$ for the medium in which the electrostatic forces act has been assumed $^{24}$ to

be 2.0; if required, there will be no difficulty in introducing other charge distributions that produce an electric field or a dielectric constant that depends on the nature of the interacting particles, the distance between them, and the intervening medium.

The procedure for the SCEF method is as follows:

(a) The direction of the electric field with respect to the CO and NH bond dipole moments in each peptide unit will provide information as to which peptide unit is the worst oriented.

(b) Then knowledge of the directions of the electric field, calculated in the middle of the peptide unit, and of the dipole moment of this unit, will enable us to carry out a necessary rotation subject to bond-length and bond-angle restrictions in order to align the electric field parallel to the dipole moment (lower electrostatic energy).

(c) The procedure will be repeated until self-consistency is achieved.

## Electric Field at a Peptide Unit

The electric field $\mathscr{E}$ at any point $\mathbf{r}$ of a given peptide unit $i$ is calculated as

$$
\mathscr{E}(\mathbf{r})=(1 / \epsilon) \sum_{j}^{\prime} q_{j}\left(\mathbf{r}_{j}-\mathbf{r}\right) /\left|\mathbf{r}_{j}-\mathbf{r}\right|^{3} \tag{1}
$$

where $q_{j}$ stands for the charge on atom $j$ with position vector $\mathbf{r}_{j}$, and the prime on the summation sign indicates that atoms $\mathrm{C}_{i}^{\prime}, \mathrm{O}, \mathrm{N}_{i+1}, \mathrm{H}, \mathrm{C}_{i}^{\alpha}$, and $\mathrm{C}_{i+1}^{\alpha}$ within peptide unit $i$ (Fig. 1) do not contribute to the field (H is the atom bound to the nitrogen of the peptide unit). The exclusion of these atoms is equivalent to the assumption that the peptide unit is rigid and rigidly bound to the $\mathrm{C}^{\alpha}$'s. We have allowed the dihedral angles $\omega$ to vary but, since deviations from rigidity (e.g., if the angle $\omega \neq 180^{\circ}$ ) are usually very small, the final results are not significantly affected.

The electric field is calculated at the three points of the $i$ th peptide unit: $\mathbf{r}_{i, \mathrm{CO}}, \mathbf{r}_{i, \mathrm{NH}}$, and $\mathbf{r}_{i}$, which will be defined below. The electric field vectors $\mathscr{E}\left(\mathbf{r}_{i, \mathrm{CO}}\right)$ and $\mathscr{E}\left(\mathbf{r}_{i, \mathrm{NH}}\right)$ at these points in the $\mathrm{CO}$ and $\mathrm{NH}$ bonds, respectively, are used to determine which peptide unit is the worst oriented with respect to the electric field, while the electric field vector calculated in the middle of the $\mathrm{C}^{\prime}-\mathrm{N}$ bond of peptide unit $i$ [see Eq. (4)], $\mathscr{E}\left(\mathbf{r}_{i}\right)$, will enable us to determine what to do in order to improve the orientation of this peptide unit. The points represented by the position vectors $\mathbf{r}_{i, \mathrm{CO}}$ and $\mathbf{r}_{i, \mathrm{NH}}$ are defined so that the bond quadrupole moments vanish, i.e., so as to satisfy the following two equations:

$$
Q_{\mathrm{CO}}=q_{\mathrm{C}}\left|\mathbf{r}_{i, \mathrm{C}}-\mathbf{r}_{i, \mathrm{CO}}\right|^{2}+q_{\mathrm{O}}\left|\mathbf{r}_{i, \mathrm{O}}-\mathbf{r}_{i, \mathrm{CO}}\right|^{2}=0 \tag{2}
$$

$$
Q_{\mathrm{NH}}=q_{\mathrm{N}}\left|\mathbf{r}_{i, \mathrm{~N}}-\mathbf{r}_{i, \mathrm{NH}}\right|^{2}+q_{\mathrm{H}}\left|\mathbf{r}_{i, \mathrm{H}}-\mathbf{r}_{i, \mathrm{NH}}\right|^{2}=0 \tag{3}
$$

and $\mathbf{r}_{i}$ is defined as

$$
\mathbf{r}_{i}=\left(\mathbf{r}_{i, \mathrm{C}}+\mathbf{r}_{i, \mathrm{~N}}\right) / 2 \tag{4}
$$

where $Q_{\mathrm{CO}}$ and $Q_{\mathrm{NH}}$ are the quadrupole moments of the $\mathrm{CO}$ and $\mathrm{NH}$ bonds,

![](./images/812276233562750976_1.jpg)

Fig. 1. Peptide unit $i$ with the atomic charges (in electronic charge units) as in Ref. 24. The whole unit may rotate about the $C_{i}^{a}-C_{i}'$ axis (variation of $\psi_{i}$), about the $N_{i+1}-C_{i+1}^{a}$ axis (variation of $\phi_{i+1}$), and about the $C_{i}'-N_{i+1}$ axis (variation of $\omega_{i}$). The angle between the $C_{i}^{a}-C_{i}'$ and $N_{i+1}-C_{i+1}^{a}$ axes is equal to $6^{\circ}$ (for a planar trans peptide unit). The arrows show the positions of the center of the peptide unit ($\mathbf{r}_{i}$, the middle of the $C'-N$ bond), a point along the CO bond ($\mathbf{r}_{i, \text{CO}}$), and a point along the NH bond ($\mathbf{r}_{i, \text{NH}}$). The position vectors $\mathbf{r}_{i, \text{CO}}$ and $\mathbf{r}_{i, \text{NH}}$ divide the CO and NH bonds in the ratios $1.082:1$ and $0.703:1$, respectively (see the text). For the terminal peptide units the charges (and the position vectors) are determined by the same procedure, and their values are slightly different. $^{24}$

respectively. We have adopted the notation that $\mathbf{r}_{i, \text{X}}$ stands for the position vector of atom $\text{X}$ in peptide unit $i$ (here, $\text{C}$ and $\text{N}$ designate $C_{i}'$ and $N_{i+1}$, respectively, of Fig. 1). Equations (2) and (3) determine points $\mathbf{r}_{i, \text{CO}}$ and $\mathbf{r}_{i, \text{NH}}$, which divide the CO and NH bonds in the ratio $1.082:1$ and $0.703:1$ from $\text{C}$ to $\text{O}$ and from $\text{N}$ to $\text{H}$, respectively (from the ECEPP parameterization $^{24}$ for a standard peptide unit).

The points $\mathbf{r}_{i, \text{CO}}$, $\mathbf{r}_{i, \text{NH}}$ and $\mathbf{r}_{i}$ are also the reference points with respect to which the dipole moments $\boldsymbol{\mu}_{i}^{\text{CO}}$ and $\boldsymbol{\mu}_{i}^{\text{NH}}$ of the CO and NH bonds, and $\boldsymbol{\mu}_{i}$ of the whole peptide unit CONH, respectively, are calculated:

$$
\boldsymbol{\mu}_{i}^{\text{CO}}=q_{\mathrm{C}}\left(\mathbf{r}_{i, \mathrm{C}}-\mathbf{r}_{i, \mathrm{CO}}\right)+q_{\mathrm{O}}\left(\mathbf{r}_{i, \mathrm{O}}-\mathbf{r}_{i, \mathrm{CO}}\right) \tag{5}
$$

$$
\boldsymbol{\mu}_{i}^{\text{NH}}=q_{\mathrm{N}}\left(\mathbf{r}_{i, \mathrm{N}}-\mathbf{r}_{i, \mathrm{NH}}\right)+q_{\mathrm{H}}\left(\mathbf{r}_{i, \mathrm{H}}-\mathbf{r}_{i, \mathrm{NH}}\right) \tag{6}
$$

$$
\begin{aligned}
\boldsymbol{\mu}_{i}= & q_{\mathrm{C}}\left(\mathbf{r}_{i, \mathrm{C}}-\mathbf{r}_{i}\right)+q_{\mathrm{O}}\left(\mathbf{r}_{i, \mathrm{O}}-\mathbf{r}_{i}\right) \\
& +q_{\mathrm{N}}\left(\mathbf{r}_{i, \mathrm{N}}-\mathbf{r}_{i}\right)+q_{\mathrm{H}}\left(\mathbf{r}_{i, \mathrm{H}}-\mathbf{r}_{i}\right)
\end{aligned} \tag{7}
$$

It should be noted that, in definitions (5) and (6), we do not split $q_{\mathrm{C}}$ (or $q_{\mathrm{N}}$)

into a part belonging to the $\mathrm{C}_{i}^{\alpha}-\mathrm{C}_{i}^{\prime}$ (or $\mathrm{N}_{i+1}-\mathrm{C}_{i+1}^{\alpha}$) and $\mathrm{C}_{i}^{\prime}-\mathrm{N}_{i+1}$ bonds. Therefore, we need not consider the dipole moment of the $\mathrm{C}_{i}^{\prime}-\mathrm{N}_{i+1}$ bond. This dipole moment is automatically taken into account through $\boldsymbol{\mu}_{i}^{\mathrm{CO}}$ and $\boldsymbol{\mu}_{i}^{\mathrm{NH}}$. If the total charge distribution in a peptide unit (represented approxi- mately as atomic point charges) is preserved, as it is here, the above choice of bond dipoles is as good as other possible (and arbitrary) ones. It should also be noted that, if the CO, NH, and CONH groups were neutral, the dipole moments $\boldsymbol{\mu}_{i}^{\mathrm{CO}}, \boldsymbol{\mu}_{i}^{\mathrm{NH}}$, and $\boldsymbol{\mu}_{i}$ would not depend on a particular choice of (arbitrary) points $\mathbf{r}_{i, \mathrm{CO}}, \mathbf{r}_{i, \mathrm{NH}}$, and $\mathbf{r}_{i}$. This arbitrariness has been used in Eqs. (2) and (3) to eliminate the quadrupole moments of the CO and NH bonds, thereby fixing the values of the corresponding dipole moments. Since the quadrupole moments of the CO and NH bonds have been eliminated by this special choice of the reference points [Eqs. (2) and (3)], the first neglected higher electrostatic interactions involve the octupole moments of these bonds (this does not mean that the quadrupole moment of a peptide unit or of larger segments of the molecule has been eliminated). Presumably, these interactions are much smaller than those involving the dipole moments of the CO and NH bonds because they decrease faster with distance (by a factor of $1 / r^{2}$).

# Measure of Deviation of Bond Dipole Moments from Alignment with Electric Field

When a rotation about the $\mathrm{C}_{i}^{\alpha}-\mathrm{C}_{i}^{\prime}$ (or $\mathrm{N}_{i+1}-\mathrm{C}_{i+1}^{\alpha}$) axis is considered for the $i$th peptide unit, only the electric field components perpendicular to the rotation axis will change:

$$
\mathscr{E}_{\perp k}\left(\mathbf{r}_{i, \mathrm{CO}}\right)=\mathscr{E}\left(\mathbf{r}_{i, \mathrm{CO}}\right)-\left[\mathscr{E}\left(\mathbf{r}_{i, \mathrm{CO}}\right) \cdot \mathbf{e}_{i, k}\right] \mathbf{e}_{i, k}
\tag{8}
$$

$$
\mathscr{E}_{\perp k}\left(\mathbf{r}_{i, \mathrm{NH}}\right)=\mathscr{E}\left(\mathbf{r}_{i, \mathrm{NH}}\right)-\left[\mathscr{E}\left(\mathbf{r}_{i, \mathrm{NH}}\right) \cdot \mathbf{e}_{i, k}\right] \mathbf{e}_{i, k}
\tag{9}
$$

where $\mathbf{e}_{i, k}$ for $k=1,2$ denotes the unit vectors along the rotation axes $\mathrm{C}_{i}^{\alpha}-\mathrm{C}_{i}^{\prime}$ and $\mathrm{N}_{i+1}-\mathrm{C}_{i+1}^{\alpha}$, respectively (Fig. 1), and $\mathbf{a} \cdot \mathbf{b}$ stands for the scalar product of vectors $\mathbf{a}$ and $\mathbf{b}$. We assume here that the points given by the vectors $\mathbf{r}_{i, \mathrm{CO}}$ and $\mathbf{r}_{i, \mathrm{NH}}$ are sufficiently close to the rotation axis. Such a rotation may lead to a better alignment of the dipole moments $\boldsymbol{\mu}_{i}^{\mathrm{CO}}$ and $\boldsymbol{\mu}_{i}^{\mathrm{NH}}$ with respect to the electric field acting on them.

Since the energy of a dipole in an electric field is equal to the negative of the scalar product of both vectors (therefore, in the case of parallel vectors, the negative product of the lengths of both vectors), Eq. (10) represents the lower bound for the energy gain due to the rotation (i.e., the energy gain if the dipole moments were optimally aligned in the electric field; we assume here that the electric field in the neighborhood of the CO and NH groups is uniform)

$$
\Delta E_{i}=\Delta E_{i}^{\mathrm{CO}}+\Delta E_{i}^{\mathrm{NH}}
\tag{10}
$$

where the individual energy gains, $\Delta E_{i}^{\mathrm{CO}}(<0)$ and $\Delta E_{i}^{\mathrm{NH}}(<0)$, to align the dipole and field vectors, are

$$
\Delta E_{i}^{\mathrm{X}}=-\left|\boldsymbol{\mu}_{i, \perp k}^{\mathrm{X}}\right|\left|\mathscr{E}_{\perp k}\left(\mathbf{r}_{i, \mathrm{X}}\right)\right|+\left[\boldsymbol{\mu}_{i, \perp k}^{\mathrm{X}} \cdot \mathscr{E}_{\perp k}\left(\mathbf{r}_{i, \mathrm{X}}\right)\right]
\tag{11}
$$

with

$$
\boldsymbol{\mu}_{i, \perp k}^{\mathrm{X}}=\boldsymbol{\mu}_{i}^{\mathrm{X}}-\left(\boldsymbol{\mu}_{i}^{\mathrm{X}} \cdot \mathbf{e}_{i, k}\right) \mathbf{e}_{i, k}
\tag{12}
$$

for X = CO, and NH, respectively. Since $\Delta E_{i}=0$ for perfect orientation of the $i$th peptide unit in the electric field, $\Delta E_{i}$ may be used as a measure of the deviation of the orientation of the $i$th peptide unit from perfect alignment. In this paper, the $\Delta E_{i}$s are calculated from Eqs. (10)-(12), with $k=1$, by calculating the components of the dipole moment and electric field perpendicular to the $\mathbf{e}_{i, 1}$ axis. Although analogous quantities can be calculated for the axis $\mathbf{e}_{i, 2}$, they are expected to be similar in magnitude since both axes $\mathbf{e}_{i, 1}$ and $\mathbf{e}_{i, 2}$ are nearly parallel (they form an angle of about $6^{\circ}$ for a planar trans peptide unit; Fig. 1).

# Aligning the Electric Field and Dipole Moment of the Peptide Unit

The $\Delta E_{i}$s calculated for each $i$ by means of Eq. (10) enable us to detect which peptide unit is the most unfavorably oriented in the electric field produced by the whole polypeptide molecule. In this section, we determine the rotation that must be performed in order to improve the orientation of this peptide unit with respect to the electric field (in fact, the rotation may be determined for any peptide unit but, in the SCEF method, only the rotation associated with the most poorly oriented peptide units will be executed). To this end, we make use of $\boldsymbol{\mu}_{i}$ and $\mathscr{E}(\mathbf{r}_{i})$ of Eqs. (7) and (1), respectively. The reason why we used the two dipole-field pairs (corresponding to the CO and NH bonds) in the previous section while, in the present section, we use only one pair (corresponding to the whole peptide unit) is as follows: To reduce the effects of the considerable inhomogeneity of the electric field as much as possible, it is reasonable to use the smallest polar systems possible, i.e., the CO and NH bonds, to estimate the energy gains precisely. In this section, however, we determine the rotation that has to be performed in order to align these two dipoles and the electric field. Primarily because of the inhomogeneity of the electric field, this would lead to two different dihedral angles of rotation: one optimal for CO and one optimal for NH, respectively. To avoid this ambiguity, we use here only one dipole field pair: $\boldsymbol{\mu}_{i}$ and $\mathscr{E}(\mathbf{r}_{i})$.

The electric field $\mathscr{E}(\mathbf{r}_{i})$ calculated at peptide unit $i$ can be viewed as the sum of two electric fields: one produced by the left-hand (N-terminal) portion, $\mathscr{E}_{\mathrm{L}}(\mathbf{r}_{i})$, and the other by the right-hand (C-terminal) portion, $\mathscr{E}_{\mathrm{R}}(\mathbf{r}_{i})$, of the whole polypeptide chain:

$$
\mathscr{E}(\mathbf{r}_{i})=\mathscr{E}_{\mathrm{L}}(\mathbf{r}_{i})+\mathscr{E}_{\mathrm{R}}(\mathbf{r}_{i})
\tag{13}
$$

This partition will enable us to examine how the electric field $\mathscr{E}(\mathbf{r}_{i})$ changes when a rotation of the left (or the right) portion of the molecule about the $\mathbf{e}_{i, 1}$ (or $\mathbf{e}_{i, 2}$) axis is executed. Since the components of $\boldsymbol{\mu}_{i}$, $\mathscr{E}_{\mathrm{L}}(\mathbf{r}_{i})$, and $\mathscr{E}_{\mathrm{R}}(\mathbf{r}_{i})$ that are parallel to an axis of rotation do not change if the rotation is executed (and, therefore, do not influence the choice of the optimal orientation—we assume here that the center of the peptide unit given by position vector $\mathbf{r}_{i}$ is sufficiently close to the rotation axes), we are interested only in the perpendic-

MULTIPLE-MINIMA PROBLEM. I
S39

ular components of $\boldsymbol{\mu}_{i}, \mathscr{E}_{\mathrm{L}}(\mathbf{r}_{i})$, and $\mathscr{E}_{\mathrm{R}}(\mathbf{r}_{i})$ with respect to the $\mathbf{e}_{i, k}$ axis

$$
\boldsymbol{\mu}_{i, \perp k}=\boldsymbol{\mu}_{i}-\mathbf{e}_{i, k}\left(\boldsymbol{\mu}_{i} \cdot \mathbf{e}_{i, k}\right)
$$

$$
\mathscr{E}_{\mathrm{L}, \perp k}(\mathbf{r}_{i})=\mathscr{E}_{\mathrm{L}}(\mathbf{r}_{i})-\mathbf{e}_{i, k}\left[\mathscr{E}_{\mathrm{L}}(\mathbf{r}_{i}) \cdot \mathbf{e}_{i, k}\right]
$$

$$
\mathscr{E}_{\mathrm{R}, \perp k}(\mathbf{r}_{i})=\mathscr{E}_{\mathrm{R}}(\mathbf{r}_{i})-\mathbf{e}_{i, k}\left[\mathscr{E}_{\mathrm{R}}(\mathbf{r}_{i}) \cdot \mathbf{e}_{i, k}\right]
$$

If $\boldsymbol{\mu}_{i, \perp k}$ does not lie along $\mathscr{E}_{\perp k}=\mathscr{E}_{\mathrm{L}, \perp k}+\mathscr{E}_{\mathrm{R}, \perp k}$ in the actual three-dimensional structure of the protein under investigation, we try to achieve perfect alignment of these two vectors (according to the underlying assumption of the SCEF method) by carrying out one rotation about $\mathbf{e}_{i, k}$ (either $k=1$ or $k=2$). For $k=1$, this means a rotation $\mathscr{E}_{\mathrm{L}, \perp 1} \rightarrow \mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}$, while for $k=2$ it is a rotation $\mathscr{E}_{\mathrm{R}, \perp 2} \rightarrow \mathscr{E}_{\mathrm{R}, \perp 2}^{\prime}$, i.e., rotations about the $\mathrm{C}_{i}^{\alpha}-\mathrm{C}_{i}^{\prime}$ axis (or $\psi_{i}$ ) and about the $\mathrm{N}_{i+1}-\mathrm{C}_{i+1}^{\alpha}$ axis (or $\phi_{i+1}$ ), respectively. It is sufficient to carry out only one of these two rotations at a time to bring about the alignment that therefore is achieved if either one of the following two (alignment) equations is satisfied: for $k=1$,

$$
\boldsymbol{\mu}_{i, \perp 1} \cdot\left(\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}+\mathscr{E}_{\mathrm{R}, \perp 1}\right)=\left|\boldsymbol{\mu}_{i, \perp 1}\right|\left|\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}+\mathscr{E}_{\mathrm{R}, \perp 1}\right|
$$

for $k=2$

$$
\boldsymbol{\mu}_{i, \perp 2} \cdot\left(\mathscr{E}_{\mathrm{L}, \perp 2}+\mathscr{E}_{\mathrm{R}, \perp 2}^{\prime}\right)=\left|\boldsymbol{\mu}_{i, \perp 2}\right|\left|\mathscr{E}_{\mathrm{L}, \perp 2}+\mathscr{E}_{\mathrm{R}, \perp 2}^{\prime}\right|
$$

Figure 2 shows how Eq. (17) can be solved. Since the solution of Eq. (18) is analogous to that of Eq. (17) (see the caption to Fig. 2), here we present the solution of Eq. (17) only. From straightforward geometrical considerations (see Fig. 2), the angle $\alpha$ between $\boldsymbol{\mu}_{i, \perp 1}$ and the rotated left-hand electric field, $\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}$, satisfies the relation.

$$
|\alpha|=\operatorname{arc} \cos (c / b)
$$

where $b=\left|\mathscr{E}_{\mathrm{L}, \perp 1}\right|, c=d^{1 / 2}$ with $d=b^{2}-a^{2} \sin ^{2} \theta_{\mathrm{R}}, a=\left|\mathscr{E}_{\mathrm{R}, \perp 1}\right|$, and $\theta_{\mathrm{R}}$ is the angle between $\mathscr{E}_{\mathrm{R}, \perp 1}$ and $\boldsymbol{\mu}_{i, \perp 1}$. Equation (19) has various numbers of solutions: four, $\alpha_{1}$ and $\alpha_{2}=180^{\circ}-\alpha_{1},-\alpha_{1},-\alpha_{2}$ (when $d>0$ ); two, $90^{\circ}$ and $-90^{\circ}$ (when $d=0$ ); or none (when $d<0$ ). These solutions, if they exist, correspond to different energies of the dipole moment $\boldsymbol{\mu}_{i, \perp 1}$ in the electric field $\mathscr{E}_{\perp 1}$ (e.g., $\alpha_{1}$ and $\alpha_{2}$ of Fig. 2 correspond to the parallel and antiparallel orientations of both vectors), and therefore only one of them (the angle that gives the lowest energy of the dipole moment in the electric field, $+\alpha_{1}$ in Fig. 2) represents the solution of alignment Eq. (17). For this unique solution, if it exists, one may calculate the expected energy gain when the rotation by $\Delta \psi_{i}=\beta_{\mathrm{L}}+\alpha_{1}$ (see Fig. 2 for definitions of angles) is executed about the $\mathbf{e}_{i, 1}$ axis (i.e., rotation of the left-hand side of the molecule about the $\mathrm{C}_{i}^{\alpha}-\mathrm{C}_{i}^{\prime}$ axis, see Fig. 2)

$$
\Delta E_{i, \mathrm{~L}}=-\boldsymbol{\mu}_{i, \perp 1} \cdot\left(\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}-\mathscr{E}_{\mathrm{L}, \perp 1}\right)
$$

It should be noted that the solution of Eq. (17) leads to only an approximate

![](./images/812276233562750976_2.jpg)

Fig. 2. Solution of alignment equation (17). The rotation axis $k=1$ corresponds to the $C_{i}^{\alpha}-C_{i}^{\prime}$ bond (variation of $\psi_{i}$, Fig. 1) and is perpendicular to the plane of the figure at point $O$. The dipole moment $\boldsymbol{\mu}_{i, \perp 1}$ and the left- and right-hand electric fields $\mathscr{E}_{\mathrm{L}, \perp 1}$ and $\mathscr{E}_{\mathrm{R}, \perp 1}$ are the perpendicular components of the corresponding vectors for the $i$ th peptide unit [see Eqs. (14)-(16)]. The circle has its center at the end of the immobile vector $\mathscr{E}_{\mathrm{R}, \perp 1}$ and a radius of $|\mathscr{E}_{\mathrm{L}, \perp 1}|$. The sum of the two electric fields, the fixed $\mathscr{E}_{\mathrm{R}, \perp 1}$ and the rotatable $\mathscr{E}_{\mathrm{L}, \perp 1}$ [the latter field being calculated from eq. (17), i.e., before any rotation] is a vector starting at the origin $O$ and ending somewhere on the circle. In other words, the right-hand side of the molecule is held fixed together with the $i$ th peptide unit, while the left-hand side of the molecule is allowed to rotate about the $C_{i}^{\alpha}-C_{i}^{\prime}$ axis. There are two vectors (defined by the intersections of the circle with the direction of the dipole moment, as shown in the figure), $\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}$ and $\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime \prime}$, which ensure that the vectors $\mathscr{E}_{\mathrm{R}, \perp 1}+\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}$ and $\mathscr{E}_{\mathrm{R}, \perp 1}+\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime \prime}$ (pointing in opposite directions) are colinear with $\boldsymbol{\mu}_{i, \perp 1}$. Only the first of these vectors has the direction of $\boldsymbol{\mu}_{i, \perp 1}$, and therefore only $\mathscr{E}_{\mathrm{L}, \perp 1}^{\prime}$ is the solution of Eq. (17). The solution of the analogous Eq. 18 requires interchanging the subscripts $\mathrm{R} \leftrightarrow \mathrm{L}$ and $1 \leftrightarrow 2$ of the electric field vectors and the dipole moment as well as $\beta \leftrightarrow \theta$.

alignment of $\boldsymbol{\mu}_{i, \perp 1}$ and the corresponding electric field component after the rotation $\Delta \psi_{i}$ is performed. The reason is that the center of the peptide unit $(\mathbf{r}_{i}$, Fig. 1, where the electric field vector is calculated) deviates slightly from the $\psi_{i}$ axis, and the electric field is inhomogeneous. As a result, after rotation $\Delta \psi_{i}$, the center of the peptide unit has a different position (and, therefore, the electric field produced by the left-hand side of the molecule is different at this point) with respect to the left-hand side of the molecule than before the rotation, whereas Eq. (17) assumes that there is no such change. To obtain an accurate variation of $\psi_{i}$, Eq. (17) can be solved iteratively by calculating $\mathscr{E}_{\mathrm{L}, \perp 1}$ (Fig. 2) in the $m$ th iteration for the conformation of the molecule obtained by rotation $\Delta \psi_{i}$, the value computed in the $(m-1)$ th iteration. In the present paper, however, we found it sufficient to limit the computation to $m=1$, i.e., to solve Eq. (17) only once.

Similar calculations can be carried out for the rotation of the right-hand side field (i.e., $\Delta \phi_{i+1}=\beta_{\mathrm{R}}+\alpha_{1}$, rotation of the right-hand side of the molecule about the $\mathrm{N}_{i+1}-\mathrm{C}_{i+1}^{\alpha}$ axis, Fig. 1) and the unique solution, if it exists, of alignment Eq. (18) corresponds to the expected energy gain given by

$$
\Delta E_{i, \mathrm{R}}=-\boldsymbol{\mu}_{i, \perp 2} \cdot\left(\mathscr{E}_{\mathrm{R}, \perp 2}^{\prime}-\mathscr{E}_{\mathrm{R}, \perp 2}\right) \tag{21}
$$

Then, one decides which rotation will be performed, $\psi_{i}$ or $\phi_{i+1}$, by comparing $\Delta E_{i, \mathrm{~L}}$ and $\Delta E_{i, \mathrm{R}}$ of Eqs. (20) and (21), and choosing the more negative of the two together with the associated dihedral angle of rotation. Hence, if $\Delta E_{i, \mathrm{~L}} \leq$ $\Delta E_{i \mathrm{R}}$ then one varies $\psi_{i}$, otherwise $\phi_{i+1}$, the dihedral angle of rotation being $\Delta \psi_{i}=\beta_{\mathrm{L}}+\alpha_{1}$ or $\Delta \phi_{i+1}=\beta_{\mathrm{R}}+\alpha_{1}$, respectively, where $\alpha_{1}$ implies the solution of Eq. (17) or (18), respectively (Fig. 2). If both Eqs. (17) and (18) accidentally have no solution, then another unfavorably oriented peptide unit would have to be chosen.

### Iterative Structure of the SCEF Procedure

The strategy of the SCEF procedure may be summarized as follows:

1. For a given starting conformation of the polypeptide, minimize its complete (e.g., ECEPP/2) conformational energy with respect to all backbone dihedral angles-$\phi, \psi, \omega$-to reach the nearest local minimum. This allows the molecule to relax to some extent while all interactions in the assumed conformational energy function are taken into account.

2. Calculate the electric field vectors at each CO and NH group of the peptide units of the whole polypeptide molecule.

3. Calculate the energy gains $\Delta E_{i}$ of Eq. (10) for every $i$, and select the most negative value of $\Delta E_{i}$; i.e., select the peptide unit $j$ that is the worst oriented in the electric field of the polypeptide chain.

4. Calculate the electric field vectors $\mathscr{E}_{\mathrm{L}, \perp 1}, \mathscr{E}_{\mathrm{R}, \perp 1}, \mathscr{E}_{\mathrm{L}, \perp 2}$, and $\mathscr{E}_{\mathrm{R}, \perp 2}$ for peptide unit $j$. Choose the more negative term from $\Delta E_{j, \mathrm{~L}}$ and $\Delta E_{j, \mathrm{R}}$ of Eqs. (20) and (21), as well as the associated dihedral angle of rotation: $\beta_{\mathrm{L}}+\alpha_{1}$ if $\Delta E_{j, \mathrm{~L}} \leq \Delta E_{j, \mathrm{R}}$ or $\beta_{\mathrm{R}}+\alpha_{1}$ if $\Delta E_{j, \mathrm{~L}}>\Delta E_{j, \mathrm{R}}$, as the change of the dihedral angle, $\psi_{j}$ or $\phi_{j+1}$ respectively (see the section on the aligning of the electric field and dipole moment of the peptide units; see also Fig. 2). Thus, in this step one decides which variation-$\psi_{j}$ or $\phi_{j+1}$-will be carried out, and the size of the dihedral angle for this rotation. This rotation will hereafter be called the "diagnostic rotation."

5. Carry out the diagnostic rotation.

6. Use the new conformation of the molecule as the starting point in step 1:
    (a) if a new local minimum is reached (i.e., one that differs from the result of step 1), then repeat the procedure from step 2 for this new minimum;
    (b) if the same local minimum is found as in the previous application of step 1, then step 3 must be repeated, but with the choice of a new $j$ that corresponds to the next lowest of the $\Delta E_{i}$ s.

7. The above procedure (steps 1-6) is repeated until self-consistency is achieved, i.e., until further application of the procedure does not change the conformation of the polypeptide chain.

If there are several peptide units $i=j_{1}, j_{2} \ldots$ with low values of $\Delta E_{i}$ and they are widely separated in space, the procedure can be modified to speed the computation by carrying out the diagnostic rotations at the same time for each of these peptide units. After steps 1 and 2 have been completed for the initial conformation, steps 3 and 4 are carried out for each peptide unit independently. In step 5, several independent rotations are carried out, one for each of the peptide units, then step 6 is performed as before. In an example given below, this procedure was applied successfully for the interresidue separation $j_{1}-j_{2}=2$ residues.

The following are some of the characteristic features of the SCEF method:

1. At any stage of the procedure, the method detects where the largest defect of the three-dimensional structure of the polypeptide exists (in terms of poor electrostatic interactions), and calculates how to avoid it.

2. The procedure has a local character; i.e., the spatial orientation of a particular peptide unit is changed because this is energetically favorable for this unit alone.

3. Each step of the SCEF procedure improves the conformation of the worst-oriented peptide unit.

4. In the procedure, the electrostatic forces (calculated from dipole-electric field interactions) dictate the direction and the overall size of the conformational changes of the molecule in order to reach another conformation. Then, the electrostatic interactions involving the partial atomic charges together with all other interactions included in the assumed conformational energy function modify the structure of the molecule, allowing it to relax.

## NUMERICAL EXAMPLES

The calculations reported here were carried out for the ${\mathrm{CH}}_{3}{\mathrm{CO-(\text{Ala})}}_{19}{\mathrm{NHCH}}_{3}$ molecule, using the ECEPP/2 conformational energy function. $^{24}$ Our aim here was to study systematically how the SCEF procedure behaves when the starting conformation is taken further and further from the global-minimum position. Since our procedure is designed to detect where the largest electrostatic defect exists in the molecule, we stress that, after we had introduced defects, we proceeded on the assumption that we did not know whether and where they had been introduced. The actual position of the largest electrostatic defect was always detected by using step 3 of the SCEF method (see section on the iterative structure of the SCEF procedure), i.e., by selecting the peptide unit with the lowest value of $\Delta E_{i}$ of Eq. (10). The global-minimum conformation for the polypeptide under study is believed to be an $\alpha$-helix. Therefore, our first goal was to determine whether the SCEF procedure, after reaching the global minimum, will remain there, thereby demonstrating its convergence. In the following discussion, the term "optimization" stands for step 1 of the SCEF procedure.

### "Perfect" Finite $\alpha$-Helix

After optimizing all dihedral angles of the $\alpha$-helix (by step 1), the maximum energy gains $\Delta E_{i}^{\mathrm{CO}}$ and $\Delta E_{i}^{\mathrm{NH}}$ were computed with Eq. (11) (Table I, columns $M = 0$). As can be seen, all of the CO and NH bond dipoles are close to their best positions (the expected electrostatic energy gains not exceeding $-0.02$ and $-0.12$ kcal/mole for the CO and NH bonds, respectively), except for a few peptide units at both ends of the helix, where the worst orientation is indicated for the first (N-terminal) peptide unit with electrostatic energy gains of $-2.24$ and $-0.49$ kcal/mole for the CO and NH bonds, respectively. There are also smaller deviations from the electrostatically best positions at the C-terminus where the gain for the CO bond of residue 20 is equal to $-0.75$ kcal/mole. It should be noted that the influence of the ends of the helix does not extend very far. Indeed, only two units at each end are perturbed significantly ($|\Delta E_{i}|$ exceeds $\sim 0.6$ kcal/mole). This is a promising result

<table>
<caption>TABLE I: Energies⁸, $-\Delta E_i^{\text{CO}}$ and $-\Delta E_i^{\text{NH}}$ for the "Perfect" Finite Poly(L-Alanine) $\alpha$-Helix ($M = 0$) and for Molecules with a Single Defect</caption>
<thead>
<tr>
<th>$M^\text{b}$</th>
<th>$n^\text{c}$</th>
<th>$i^\text{d}$</th>
<th></th>
<th colspan="20">Residue $i$</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>10</th>
<th>11</th>
<th>12</th>
<th>13</th>
<th>14</th>
<th>15</th>
<th>16</th>
<th>17</th>
<th>18</th>
<th>19</th>
<th>20</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>any</td>
<td>iteration</td>
<td>CO</td>
<td>2.24</td>
<td>0.20</td>
<td>0.03</td>
<td>0.09</td>
<td>0.04</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
<td>0.01</td>
<td>0.02</td>
<td>0.01</td>
<td>0.00</td>
<td>0.00</td>
<td>0.11</td>
<td>0.61</td>
<td>0.75</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>NH</td>
<td>0.49</td>
<td>0.59</td>
<td>0.01</td>
<td>0.19</td>
<td>0.16</td>
<td>0.12</td>
<td>0.11</td>
<td>0.12</td>
<td>0.11</td>
<td>0.11</td>
<td>0.11</td>
<td>0.11</td>
<td>0.10</td>
<td>0.11</td>
<td>0.12</td>
<td>0.11</td>
<td>0.06</td>
<td>0.05</td>
<td></td>
</tr>
<tr>
<td>0</td>
<td></td>
<td>1(C)</td>
<td>CO</td>
<td>2.31</td>
<td>0.18</td>
<td>0.01</td>
<td>0.10</td>
<td>0.05</td>
<td>0.00</td>
<td>0.00</td>
<td>0.09</td>
<td>0.31</td>
<td>0.28</td>
<td>2.69</td>
<td>0.03</td>
<td>0.06</td>
<td>0.04</td>
<td>0.01</td>
<td>0.00</td>
<td>0.12</td>
<td>0.60</td>
<td>0.76</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>NH</td>
<td>0.51</td>
<td>0.59</td>
<td>0.02</td>
<td>0.20</td>
<td>0.16</td>
<td>0.10</td>
<td>0.11</td>
<td>0.14</td>
<td>0.06</td>
<td>0.01</td>
<td>1.23</td>
<td>0.67</td>
<td>0.21</td>
<td>0.09</td>
<td>0.16</td>
<td>0.12</td>
<td>0.10</td>
<td>0.11</td>
<td>0.07</td>
<td>0.05</td>
</tr>
<tr>
<td>0</td>
<td></td>
<td>1(G)</td>
<td>CO</td>
<td>2.22</td>
<td>0.23</td>
<td>0.02</td>
<td>0.07</td>
<td>0.06</td>
<td>0.03</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.57</td>
<td>0.19</td>
<td>0.00</td>
<td>0.07</td>
<td>0.08</td>
<td>0.01</td>
<td>0.00</td>
<td>0.00</td>
<td>0.11</td>
<td>0.64</td>
<td>0.74</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>NH</td>
<td>0.49</td>
<td>0.60</td>
<td>0.01</td>
<td>0.18</td>
<td>0.17</td>
<td>0.14</td>
<td>0.07</td>
<td>0.08</td>
<td>0.24</td>
<td>0.11</td>
<td>0.24</td>
<td>0.02</td>
<td>0.09</td>
<td>0.17</td>
<td>0.12</td>
<td>0.10</td>
<td>0.13</td>
<td>0.12</td>
<td>0.06</td>
<td>0.05</td>
</tr>
<tr>
<td>0</td>
<td></td>
<td>1(E)</td>
<td>CO</td>
<td>2.22</td>
<td>0.17</td>
<td>0.03</td>
<td>0.07</td>
<td>0.06</td>
<td>0.01</td>
<td>0.03</td>
<td>0.06</td>
<td>0.45</td>
<td>1.10</td>
<td>3.35</td>
<td>0.03</td>
<td>0.00</td>
<td>0.03</td>
<td>0.02</td>
<td>0.01</td>
<td>0.00</td>
<td>0.19</td>
<td>0.60</td>
<td>0.74</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>NH</td>
<td>0.48</td>
<td>0.56</td>
<td>0.00</td>
<td>0.19</td>
<td>0.16</td>
<td>0.12</td>
<td>0.09</td>
<td>0.11</td>
<td>0.09</td>
<td>0.01</td>
<td>1.46</td>
<td>0.57</td>
<td>0.11</td>
<td>0.10</td>
<td>0.11</td>
<td>0.13</td>
<td>0.13</td>
<td>0.09</td>
<td>0.07</td>
<td>0.05</td>
</tr>
<tr>
<td>0</td>
<td></td>
<td>1(F)</td>
<td>CO</td>
<td>2.34</td>
<td>0.20</td>
<td>0.01</td>
<td>0.09</td>
<td>0.07</td>
<td>0.00</td>
<td>0.01</td>
<td>0.10</td>
<td>0.55</td>
<td>0.75</td>
<td>4.16</td>
<td>0.04</td>
<td>0.13</td>
<td>0.15</td>
<td>0.05</td>
<td>0.00</td>
<td>0.00</td>
<td>0.08</td>
<td>0.59</td>
<td>0.77</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>NH</td>
<td>0.51</td>
<td>0.61</td>
<td>0.03</td>
<td>0.20</td>
<td>0.18</td>
<td>0.11</td>
<td>0.09</td>
<td>0.19</td>
<td>0.09</td>
<td>0.04</td>
<td>1.75</td>
<td>0.79</td>
<td>0.32</td>
<td>0.41</td>
<td>0.16</td>
<td>0.10</td>
<td>0.09</td>
<td>0.13</td>
<td>0.07</td>
<td>0.06</td>
</tr>
</tbody>
</table>

$^\text{a}$In kcal/mole. It should be noted that these are the energies calculated by Eq. (11). They are used to obtain $\Delta E_i$ of Eq. (10) to detect the location of the defect. It is the values of $\Delta E_{j,L}$ and $\Delta E_{j,R}$ of Eqs. (20) and (21), however, that determine the dihedral angle to be altered (see step 4 in the section on iterative structure of the SCEF procedure).
$^\text{b}M$ is the number (and type) of defects in the starting conformation.
$^\text{c}n$ is the number of SCEF iterations, after which the $\Delta E_i$s were calculated.
$^\text{d}i$ is the peptide unit number.

because it suggests that the perturbation of the electric field due to defects is quite local and will not have a great influence on other regions of this molecule.

The end effects mentioned above, intrinsic to any finite $\alpha$-helix, are associ- ated in the SCEF procedure with a set of diagnostic dihedral angles for the residues involved, as described in the section on aligning the electric field and dipole moment of the peptide unit. In the following, we describe what happens when one follows the diagnosis in the particular case of the "perfect" finite $\alpha$-helix.

The worst-oriented peptide unit is number 1 (which lies between the end group, numbered 1, and the first full residue, which is numbered 2). The solution of the alignment equation that is the most energetically favorable (corresponding to the lower of $\Delta E_{1, \mathrm{~L}}$ and $\Delta E_{1, \mathrm{R}}$ ) indicates an energy gain of $\Delta E_{1, \mathrm{R}}=-1.56 \mathrm{kcal} / \mathrm{mole}$ if we add $76.2^{\circ}$ to $\phi_{2}$. If, however, we follow this diagnosis and add $76.2^{\circ}$, then, after step 1 (of the next iteration) of the SCEF procedure (energy minimization after having added $76.2^{\circ}$ to $\phi_{2}$ in step 5), the molecule returns to the "perfect" helix conformation shown in the $M=0$ columns of Table I. The same result is obtained if we follow the other diagnoses (associated with the other end effects), i.e., add $31.6^{\circ}$ to $\phi_{3}$, or $43.8^{\circ}$ to $\psi_{20}$, or $16.9^{\circ}$ to $\psi_{19}$; energy minimization always returns the conformation to the finite "perfect" $\alpha$-helix.

This study of the "perfect" finite helix is also instructive in that it reveals that the CO and NH bonds of peptide units far from the helix ends are not oriented perfectly along either the left-hand field $\mathscr{E}_{\mathrm{L}, \perp 1}$ or the right-hand field $\mathscr{E}_{\mathrm{R}, \perp 2}$, each taken by itself; the angles between the corresponding dipolemoment components and the fields are $43^{\circ}$ and $-94^{\circ}$, respectively, for the CO bonds, and $26^{\circ}$ and $-61^{\circ}$, respectively, for the NH bonds. It is only the total electric field (calculated far from the helix ends) that is well-oriented along the dipole moments of the CO and NH bonds (for example, the deviation of the dipole moment component and the electric field component orthogonal to the $k=1$ axis is $9^{\circ}$ for the CO and $24^{\circ}$ for the NH bond). Furthermore, if we follow the diagnosis for any peptide unit inside the helix (which is: add $26.5^{\circ}$ to $\phi_{i}$ ), then step 1 of the SCEF procedure returns the "perfect" $\alpha$-helix.

Thus, we have shown that the "perfect" (i.e., energy-minimized) finite $\alpha$-helix is invariant with respect to the SCEF procedure.

# Single Defects

In the next test of the SCEF procedure, we introduced a variety of single defects into the interior of the $\alpha$-helix and used the distorted conformation as a starting point in the procedure. The single defects were chosen from each of the five lowest-energy backbone conformations of the terminally blocked single alanine residue $^{25}$ and located in the middle of the helix. In the notation of Zimmerman et al., $^{26}$ these conformations are $\mathrm{C}(\phi=-80^{\circ}, \psi=76^{\circ}), \mathrm{E}(\phi$ $=-155^{\circ}, \psi=157^{\circ}), \mathrm{D}(\phi=-151^{\circ}, \psi=46^{\circ}), \mathrm{F}(\phi=-75^{\circ}, \psi=139^{\circ})$ and $\mathrm{G}(\phi=-158^{\circ}, \psi=-58^{\circ})$. The $\alpha$-helical conformation of alanine (A; $\phi=$ $-74^{\circ}, \psi=-35^{\circ}$ ) was, of course, excluded from this list of possible defects. For the $\mathrm{CH}_{3} \mathrm{CO}-\mathrm{Ala}-\mathrm{NHCH}_{3}$ molecule, the calculated relative energies (in $\mathrm{kcal} / \mathrm{mole}$ ) of the above conformations $^{25}$ are $\mathrm{C}(0.00), \mathrm{E}(0.69), \mathrm{A}(0.79), \mathrm{D}(1.09)$,

F(1.11), and G(1.72). Since any of the interior single defects breaks three hydrogen bonds, and there are 17 hydrogen bonds in the perfect finite helix considered here, a single defect corresponds to the rupture of 17.6% of the hydrogen bonds. The following is a description as to how the SCEF procedure treated each of these single defects.

## Defect C
Figure 3(a) shows the molecule with defect C, after optimization of its conformation (step 1); the structure is trapped in a non-$\alpha$-helical local minimum after this optimization. From the $\Delta E_i$s of Table I [columns $M = 1(\text{C})$], it follows that the worst-oriented peptide unit is number 11 [the criterion is always $\Delta E_i$ of Eq. (10)]. The calculated diagnosis dihedral angle for this unit is $\psi_{11}^{\text{new}} = \psi_{11}^{\text{old}} - 120^\circ$. This gives $\psi_{11}^{\text{new}} = +65^\circ - 120^\circ = -55^\circ$, which brings residue 11 from region C of the $(\phi, \psi)$ map to region A ($\alpha$-helical). Then step 1 of the SCEF procedure produced the "perfect" $\alpha$-helix. This shows that the global minimum was attained and that the resulting conformation is invariant to further application of the SCEF method (see previous subsection).

## Defect G
After defect G was introduced, and the energy subsequently optimized (step 1), the molecule looked like a distorted $\alpha$-helix [Fig. 3(b)]. In fact, as can be seen from Fig. 3(b), the molecule differs from the "perfect" helix mainly by the presence of one 1-5 hydrogen bond (the CO of peptide unit 8 with the NH of peptide unit 12) instead of the 1-4 hydrogen bond that is characteristic of the "perfect" $\alpha$-helix. As indicated by the $\Delta E_i$s, the SCEF procedure detects some defects at both ends of the molecule (unchangeable by the SCEF procedure; see first subsection) and a defect at peptide unit 10 [Table I, columns $M = 1(\text{G})$]. This time the diagnosis is $\phi_{11}^{\text{new}} = \phi_{11}^{\text{old}} + 57^\circ$. Application of step 1 of the SCEF method to this new starting conformation led to the perfect finite $\alpha$-helix.

It should be noted that here the SCEF procedure has been successful for a starting point [Fig. 3(b)] where it was necessary to *break* one (non-$\alpha$-helical, 1-5) hydrogen bond to reach the global minimum.

## Defect E
Figure 3(c) shows the molecule with defect E after optimization of its conformation (step 1). From the $\Delta E_i$s of Table I [columns $M = 1(\text{E})$], it follows that a defect is detected at peptide unit 11. The computed diagnosis for this peptide unit is $\psi_{11}^{\text{new}} = \psi_{11}^{\text{old}} - 173^\circ$, and we obtain $\psi_{11}^{\text{new}} = 114^\circ - 173^\circ = -59^\circ$. This means that the molecule now contains a single G defect and, indeed, after optimization it is identical to that shown in Fig. 3(b); for further treatment, see Defect G.

## Defect D
After introduction of defect D, the optimized conformation that resulted in step 1 was single defect C, which was then treated as in the subsection on Defect C.

![](./images/812276233562750976_3.jpg)

Fig. 3. Conformations of the molecule when a single defect has been introduced and the conformation optimized within a given local minimum. The single defect corresponds to the C (a), G (b), E (c) or F (d) conformation of a single alanine.²⁶ Part (b) also shows how conformation (c) appears after the first iteration and the subsequent optimization (step 1) of the SCEF method. In all cases, the method converges to the "perfect" finite helix. In the figure, only the C, N, O, and H bound to N (smaller circle) atoms are displayed. The hydrogen bonds are indicated by dashed lines.

![](./images/812276233562750976_4.jpg)

Fig. 3. (Continued from the previous page.)

### Defect F

After optimization, the conformation of the molecule is that shown in Fig. 3(d), and the corresponding $\Delta E_i$s are displayed in the last two columns of Table I. From this table, it can be seen that the defect is localized at Ala-11, and the computed diagnosis is $\psi_{11}^{\text{new}} = \psi_{11}^{\text{old}} - 150^\circ$. This changes the conformation of Ala-11 to conformation A, and step 1 results in the global minimum.

### Double Defects

As in the previous section, we distort the perfect finite $\alpha$-helix, but this time we introduce two defects of the C-type. We have chosen the C-type defect because the C-conformation is the most stable one for the terminally blocked alanine residue.²⁵ Therefore, it seemed that a C-defect might be the most difficult one to remove by the SCEF method. Four starting points have been chosen; they differ by the distances between the defects. The calculated $\Delta E_i$s are given in Table II.

<table><caption>TABLE II Energies⁸, $-\Delta E_{i}^{\text{CO}}$ and $-\Delta E_{i}^{\text{NH}}$ for the Molecule with Double Defects</caption>
<thead>
  <tr>
    <th>$\Delta l^{\text{b}}$<br>$M^{\text{c}}$<br>$n^{\text{d}}$</th>
    <td colspan="2">4<br>2<br>0</td>
    <td colspan="2">3<br>2<br>0</td>
    <td colspan="2">2<br>2<br>0</td>
    <td colspan="2">1<br>2<br>0</td>
  </tr>
  <tr>
    <th>$i^{\text{e}}$</th>
    <td>CO</td>
    <td>NH</td>
    <td>CO</td>
    <td>NH</td>
    <td>CO</td>
    <td>NH</td>
    <td>CO</td>
    <td>NH</td>
  </tr>
</thead>
<tbody>
  <tr>
    <th>1</th>
    <td>2.10</td>
    <td>0.45</td>
    <td>2.03</td>
    <td>0.51</td>
    <td>2.25</td>
    <td>0.49</td>
    <td>2.25</td>
    <td>0.49</td>
  </tr>
  <tr>
    <th>2</th>
    <td>0.30</td>
    <td>0.68</td>
    <td>0.65</td>
    <td>0.86</td>
    <td>0.20</td>
    <td>0.62</td>
    <td>0.20</td>
    <td>0.61</td>
  </tr>
  <tr>
    <th>3</th>
    <td>0.00</td>
    <td>0.04</td>
    <td>0.00</td>
    <td>0.07</td>
    <td>0.02</td>
    <td>0.02</td>
    <td>0.02</td>
    <td>0.02</td>
  </tr>
  <tr>
    <th>4</th>
    <td>0.01</td>
    <td>0.15</td>
    <td>0.02</td>
    <td>0.13</td>
    <td>0.06</td>
    <td>0.18</td>
    <td>0.08</td>
    <td>0.19</td>
  </tr>
  <tr>
    <th>5</th>
    <td>0.51</td>
    <td>0.09</td>
    <td>0.01</td>
    <td>0.16</td>
    <td>0.01</td>
    <td>0.14</td>
    <td>0.03</td>
    <td>0.15</td>
  </tr>
  <tr>
    <th>6</th>
    <td>0.44</td>
    <td>0.09</td>
    <td>0.01</td>
    <td>0.14</td>
    <td>0.00</td>
    <td>0.11</td>
    <td>0.01</td>
    <td>0.11</td>
  </tr>
  <tr>
    <th>7</th>
    <td>0.19</td>
    <td>0.00</td>
    <td>0.51</td>
    <td>0.06</td>
    <td>0.22</td>
    <td>0.13</td>
    <td>0.00</td>
    <td>0.12</td>
  </tr>
  <tr>
    <th>8</th>
    <td>3.07</td>
    <td>1.24</td>
    <td>0.12</td>
    <td>0.00</td>
    <td>0.45</td>
    <td>0.04</td>
    <td>0.18</td>
    <td>0.12</td>
  </tr>
  <tr>
    <th>9</th>
    <td>0.12</td>
    <td>0.80</td>
    <td>2.60</td>
    <td>1.29</td>
    <td>0.13</td>
    <td>0.00</td>
    <td>0.33</td>
    <td>0.06</td>
  </tr>
  <tr>
    <th>10</th>
    <td>0.91</td>
    <td>0.30</td>
    <td>1.48</td>
    <td>1.20</td>
    <td>2.49</td>
    <td>1.18</td>
    <td>0.17</td>
    <td>0.00</td>
  </tr>
  <tr>
    <th>11</th>
    <td>0.43</td>
    <td>0.07</td>
    <td>1.11</td>
    <td>0.61</td>
    <td>0.48</td>
    <td>0.24</td>
    <td>2.03</td>
    <td>0.62</td>
  </tr>
  <tr>
    <th>12</th>
    <td>3.12</td>
    <td>1.62</td>
    <td>2.78</td>
    <td>1.22</td>
    <td>1.26</td>
    <td>1.06</td>
    <td>1.48</td>
    <td>0.71</td>
  </tr>
  <tr>
    <th>13</th>
    <td>0.25</td>
    <td>0.69</td>
    <td>0.19</td>
    <td>0.84</td>
    <td>0.23</td>
    <td>0.71</td>
    <td>0.14</td>
    <td>0.49</td>
  </tr>
  <tr>
    <th>14</th>
    <td>0.01</td>
    <td>0.09</td>
    <td>0.05</td>
    <td>0.22</td>
    <td>0.02</td>
    <td>0.15</td>
    <td>0.00</td>
    <td>0.06</td>
  </tr>
  <tr>
    <th>15</th>
    <td>0.05</td>
    <td>0.19</td>
    <td>0.11</td>
    <td>0.19</td>
    <td>0.05</td>
    <td>0.10</td>
    <td>0.08</td>
    <td>0.15</td>
  </tr>
  <tr>
    <th>16</th>
    <td>0.07</td>
    <td>0.19</td>
    <td>0.06</td>
    <td>0.22</td>
    <td>0.02</td>
    <td>0.15</td>
    <td>0.01</td>
    <td>0.13</td>
  </tr>
  <tr>
    <th>17</th>
    <td>0.00</td>
    <td>0.15</td>
    <td>0.00</td>
    <td>0.14</td>
    <td>0.00</td>
    <td>0.14</td>
    <td>0.00</td>
    <td>0.13</td>
  </tr>
  <tr>
    <th>18</th>
    <td>0.23</td>
    <td>0.07</td>
    <td>0.13</td>
    <td>0.10</td>
    <td>0.14</td>
    <td>0.11</td>
    <td>0.13</td>
    <td>0.11</td>
  </tr>
  <tr>
    <th>19</th>
    <td>0.59</td>
    <td>0.07</td>
    <td>0.71</td>
    <td>0.06</td>
    <td>0.65</td>
    <td>0.07</td>
    <td>0.63</td>
    <td>0.07</td>
  </tr>
  <tr>
    <th>20</th>
    <td>0.72</td>
    <td>0.04</td>
    <td>0.51</td>
    <td>0.03</td>
    <td>0.78</td>
    <td>0.05</td>
    <td>0.78</td>
    <td>0.06</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="9">⁸In kcal/mole.<br>ᵇ$\Delta l$ is the interdefect separation (number of residues).<br>ᶜSee footnote b of Table I.<br>ᵈSee footnote c of Table I.<br>ᵉSee footnote d of Table I.</td>
  </tr>
</tfoot>
</table>

### Interdefect Distance 4

The optimized geometry of the molecule with two defects separated by four peptide units [i.e., at the $i$th and $(i + 4)$th residues] is shown in Fig. 4(a). In this molecule, 35.3% of the hydrogen bonds are broken. The $\Delta E_i$s detect two large defects, at peptide units 8 and 12 (columns $\Delta l = 4$ of Table II). Since the defects are quite well-separated (see Table II), we corrected both defects at the same time (see the section on iterative structure of the SCEF procedure). The diagnosis is as follows: $\psi_{8}^{\text{new}} = \psi_{8}^{\text{old}} - 130^{\circ}$ and $\psi_{12}^{\text{new}} = \psi_{12}^{\text{old}} - 156^{\circ}$, leading to $\psi_{8}^{\text{new}} = -60^{\circ}$ and $\psi_{12}^{\text{new}} = -72^{\circ}$. Optimization from this new starting conformation gave an imperfect $\alpha$-helix with one 1-5 hydrogen bond [similar to that in Fig. 3(b)], which was transformed to the "perfect" $\alpha$-helix in the second iteration of the SCEF procedure.

### Interdefect Distance 3

The optimized starting conformation of the molecule (with 35.3% of the hydrogen bonds broken) is shown in Fig. 4(b). The $\Delta E_i$s detected the two largest defects at peptide units 9 and 12 $[\Delta E_9 = 3.89,\ \Delta E_{12} = 4.00$ kcal/mole

![](./images/812276233562750976_5.jpg)

Fig. 4. Conformations of the molecule when two defects (of the C-type) have been introduced and the conformation is optimized within the local minimum. For a description of the atoms, see the caption to Fig. 3. The interdefect separation is equal to four (a), three (b), two (d), and one (f) residues. Parts (c) and (e) show the molecules (b) and (d), respectively, immediately after the diagnosis in the first iteration of the SCEF method (the two defects are removed simultaneously). The SCEF procedure converges to the "perfect" finite $\alpha$-helix.

in Table II (columns $\Delta l=3$)], and the diagnosis for treating both at the same time is $\psi_{9}^{\text{new}}=\psi_{9}^{\text{old}}-113^{\circ}$ and $\psi_{12}^{\text{new}}=\psi_{\text{old}}^{12}-130^{\circ}$, leading to $\psi_{9}^{\text{new}}=-54^{\circ}$ and $\psi_{12}^{\text{new}}=-52^{\circ}$. To demonstrate the effectiveness of the SCEF method, the molecule in the new starting point (after the first iteration) is shown in Fig. 4(c). The subsequent optimization gave the global minimum.

![](./images/812276233562750976_6.jpg)

Fig. 4. (Continued from the previous page.)

## Interdefect Distance 2

The optimized starting conformation of the molecule (with 29.4% of the hydrogen bonds broken) is shown in Fig. 4(d). The first iteration detects two defects (Table II, columns $\Delta l=2$) at peptide units 10 and 12. The diagnosis

for both defects (treated independently and simultaneously) is $\psi_{10}^{\text{new}} = \psi_{10}^{\text{old}} - 104^\circ$ and $\psi_{12}^{\text{new}} = \psi_{12}^{\text{old}} - 96^\circ$, leading to $\psi_{10}^{\text{new}} = -41^\circ$ and $\psi_{12}^{\text{new}} = -26^\circ$. Figure 4(e) shows the molecule immediately after the prediction; it is an imperfect helix. Optimization of this starting conformation led to the global minimum.

### Interdefect Distance 1

The optimized starting conformation of the molecule (with 23.5% of the hydrogen bonds broken) is shown in Fig. 4(f). The $\Delta E_i$s detect the largest defect at Ala-11 (Table II, columns $\Delta l = 1$, peptide unit 11). The diagnosis is $\psi_{11}^{\text{new}} = \psi_{11}^{\text{old}} - 89^\circ$, leading to $\psi_{11}^{\text{new}} = -22^\circ$. This "starting" point was used in the optimization procedure (second iteration, step 1), and attained a confor- mation identical to that containing a single C-defect, which was treated previously. Hence, again, the global minimum is attained.

### Triple Defects

Figure 5(a-d) show the optimized conformations of the molecule after introduction of triple C-type defects. The three defects were always equidis- tant, with different interdefect distances (4, 3, 2, and 1 residues for Fig. 5a, b, c, and d, respectively). The molecules displayed have 52.9, 52.9, 41.2, and 29.4%, respectively, of the original hydrogen bonds broken, and the $\Delta E_i$s (before and after the first iteration), are reported in Table III. Figure 5(a) shows how one of the conformations appears before the first iteration of the

![](./images/812276233562750976_7.jpg)

Fig. 5. Conformations of the molecules when three defects (of the C-type) have been intro- duced and the conformation is optimized within a local minimum. For a description of the atoms, see the caption to Fig. 3. The interdefect separation is equal to four (a), three (b), two (c), and one (d) residues. From all of these starting points, the SCEF procedure converges to the "perfect" finite $\alpha$-helix.

![](./images/812276233562750976_8.jpg)

Fig. 5. (Continued from the previous page.)

SCEF procedure. After the first iteration (diagnosis of three defects at a time) and subsequent optimization (step 1), the conformation resembles that shown in Fig. 3(b); thus, in this case, a hydrogen bond of the 1-5 type also appears. In each case, the SCEF method reached the global minimum, the "perfect" finite α-helix, in at most three iterations.

### Quadruple Defect

Figure 6(a) represents the $CH_3CO-Ala_{19}-NHCH_3$ molecule (with the optimized conformation) in which only 5 of the original 17 hydrogen bonds are present; 70.6% of the α-helical hydrogen bonds are broken. This conformation resulted from the introduction of four C-type defects (each separated by three residues). The calculated $\Delta E_i$s are reported in Table IV, $n = 0$.

Figures 6(b-e) illustrate how the conformation changed during the iterations of the SCEF method; to show the intermediate conformations, we removed only one defect in each iteration. In the first iteration, the procedure detected the largest defect at peptide unit 6, and the diagnosis is: $\psi_6^{new} = \psi_6^{old} - 136^\circ$, leading to $\psi_6^{new} = -60^\circ$. The conformation, after this diagnosis but before optimization, is shown in Fig. 6(b). Then, after optimization, the analysis of the $\Delta E_i$s (Table IV, $n = 1$), shows a defect at peptide unit 9, with the diagnosis $\psi_9^{new} = \psi_9^{old} - 109^\circ$, leading to $\psi_9^{new} = -50^\circ$. The conformation immediately after the diagnosis is displayed in Fig. 6(c). After optimization of this structure, the $\Delta E_i$s (Table IV, $n = 2$) exhibit a defect at peptide unit 15, and the diagnosis is $\psi_{15}^{new} = \psi_{15}^{old} - 146^\circ$, leading to $\psi_{15}^{new} = -57^\circ$. The result-

# MULTIPLE-MINIMA PROBLEM. I

S53

TABLE III
Energies$^{\mathrm{a}}$, $-\Delta E_{i}^{\mathrm{CO}}$ and $-\Delta E_{i}^{\mathrm{NH}}$ for the Molecule with Triple Defects

<table>
<thead>
<tr>
<th>$\Delta l^{\mathrm{b}}$</th>
<td colspan="2">4</td>
<td colspan="2">4</td>
<td colspan="2">3</td>
<td colspan="2">3</td>
<td colspan="2">2</td>
<td colspan="2">2</td>
<td colspan="2">1</td>
<td colspan="2">1</td>
</tr>
<tr>
<th>$M^{\mathrm{c}}$</th>
<td colspan="2">3</td>
<td colspan="2">3</td>
<td colspan="2">3</td>
<td colspan="2">3</td>
<td colspan="2">3</td>
<td colspan="2">3</td>
<td colspan="2">3</td>
<td colspan="2">3</td>
</tr>
<tr>
<th>$n^{\mathrm{d}}$</th>
<td colspan="2">0</td>
<td colspan="2">1</td>
<td colspan="2">0</td>
<td colspan="2">1</td>
<td colspan="2">0</td>
<td colspan="2">1</td>
<td colspan="2">0</td>
<td colspan="2">1</td>
</tr>
<tr>
<th>$i^{\mathrm{e}}$</th>
<td>CO</td>
<td>NH</td>
<td>CO</td>
<td>NH</td>
<td>CO</td>
<td>NH</td>
<td>CO</td>
<td>NH</td>
<td>CO</td>
<td>NH</td>
<td>CO</td>
<td>NH</td>
<td>CO</td>
<td>NH</td>
<td>CO</td>
<td>NH</td>
</tr>
</thead>
<tbody>
<tr>
<th>1</th>
<td>2.46</td>
<td>0.52</td>
<td>2.22</td>
<td>0.49</td>
<td>2.82</td>
<td>0.53</td>
<td>2.78</td>
<td>0.77</td>
<td>2.26</td>
<td>0.49</td>
<td>2.27</td>
<td>0.49</td>
<td>2.26</td>
<td>0.49</td>
<td>2.25</td>
<td>0.49</td>
</tr>
<tr>
<th>2</th>
<td>0.28</td>
<td>0.65</td>
<td>0.23</td>
<td>0.60</td>
<td>0.01</td>
<td>0.45</td>
<td>0.10</td>
<td>0.61</td>
<td>0.22</td>
<td>0.64</td>
<td>0.18</td>
<td>0.60</td>
<td>0.17</td>
<td>0.60</td>
<td>0.20</td>
<td>0.61</td>
</tr>
<tr>
<th>3</th>
<td>0.00</td>
<td>0.06</td>
<td>0.02</td>
<td>0.01</td>
<td>0.00</td>
<td>0.03</td>
<td>0.01</td>
<td>0.07</td>
<td>0.00</td>
<td>0.04</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
<td>0.02</td>
</tr>
<tr>
<th>4</th>
<td>0.44</td>
<td>0.24</td>
<td>0.07</td>
<td>0.18</td>
<td>1.04</td>
<td>0.57</td>
<td>0.03</td>
<td>0.17</td>
<td>0.02</td>
<td>0.16</td>
<td>0.09</td>
<td>0.19</td>
<td>0.07</td>
<td>0.19</td>
<td>0.08</td>
<td>0.19</td>
</tr>
<tr>
<th>5</th>
<td>0.26</td>
<td>0.20</td>
<td>0.06</td>
<td>0.16</td>
<td>0.17</td>
<td>0.11</td>
<td>0.03</td>
<td>0.18</td>
<td>0.00</td>
<td>0.14</td>
<td>0.03</td>
<td>0.15</td>
<td>0.01</td>
<td>0.14</td>
<td>0.03</td>
<td>0.15</td>
</tr>
<tr>
<th>6</th>
<td>0.32</td>
<td>0.00</td>
<td>0.03</td>
<td>0.12</td>
<td>0.20</td>
<td>0.03</td>
<td>0.18</td>
<td>0.07</td>
<td>0.43</td>
<td>0.12</td>
<td>0.00</td>
<td>0.10</td>
<td>0.00</td>
<td>0.10</td>
<td>0.01</td>
<td>0.11</td>
</tr>
<tr>
<th>7</th>
<td>3.09</td>
<td>1.14</td>
<td>0.00</td>
<td>0.07</td>
<td>0.17</td>
<td>0.01</td>
<td>0.34</td>
<td>0.00</td>
<td>0.60</td>
<td>0.03</td>
<td>0.00</td>
<td>0.12</td>
<td>0.22</td>
<td>0.13</td>
<td>0.00</td>
<td>0.12</td>
</tr>
<tr>
<th>8</th>
<td>0.23</td>
<td>0.92</td>
<td>0.00</td>
<td>0.07</td>
<td>2.02</td>
<td>1.31</td>
<td>1.68</td>
<td>1.18</td>
<td>0.14</td>
<td>0.00</td>
<td>0.15</td>
<td>0.15</td>
<td>0.46</td>
<td>0.05</td>
<td>0.19</td>
<td>0.12</td>
</tr>
<tr>
<th>9</th>
<td>1.16</td>
<td>0.41</td>
<td>0.00</td>
<td>0.04</td>
<td>0.06</td>
<td>0.66</td>
<td>0.39</td>
<td>0.74</td>
<td>2.25</td>
<td>1.15</td>
<td>0.42</td>
<td>0.04</td>
<td>0.23</td>
<td>0.00</td>
<td>0.34</td>
<td>0.06</td>
</tr>
<tr>
<th>10</th>
<td>0.58</td>
<td>0.04</td>
<td>0.57</td>
<td>0.11</td>
<td>0.27</td>
<td>0.21</td>
<td>0.87</td>
<td>0.51</td>
<td>0.32</td>
<td>0.12</td>
<td>0.14</td>
<td>0.00</td>
<td>2.12</td>
<td>0.65</td>
<td>0.17</td>
<td>0.00</td>
</tr>
<tr>
<th>11</th>
<td>2.65</td>
<td>1.48</td>
<td>0.19</td>
<td>0.24</td>
<td>2.43</td>
<td>1.18</td>
<td>3.17</td>
<td>1.45</td>
<td>0.83</td>
<td>0.82</td>
<td>2.42</td>
<td>1.19</td>
<td>0.64</td>
<td>0.26</td>
<td>2.04</td>
<td>0.62</td>
</tr>
<tr>
<th>12</th>
<td>1.23</td>
<td>1.08</td>
<td>0.00</td>
<td>0.02</td>
<td>0.81</td>
<td>0.88</td>
<td>0.01</td>
<td>0.73</td>
<td>0.25</td>
<td>0.18</td>
<td>0.53</td>
<td>0.25</td>
<td>1.59</td>
<td>0.70</td>
<td>1.48</td>
<td>0.72</td>
</tr>
<tr>
<th>13</th>
<td>1.32</td>
<td>0.52</td>
<td>0.07</td>
<td>0.10</td>
<td>0.88</td>
<td>0.51</td>
<td>0.15</td>
<td>0.27</td>
<td>1.14</td>
<td>0.92</td>
<td>1.26</td>
<td>1.09</td>
<td>0.22</td>
<td>0.64</td>
<td>0.14</td>
<td>0.49</td>
</tr>
<tr>
<th>14</th>
<td>0.09</td>
<td>0.02</td>
<td>0.08</td>
<td>0.17</td>
<td>2.58</td>
<td>1.22</td>
<td>0.11</td>
<td>0.28</td>
<td>0.29</td>
<td>0.75</td>
<td>0.24</td>
<td>0.75</td>
<td>0.01</td>
<td>0.10</td>
<td>0.00</td>
<td>0.06</td>
</tr>
<tr>
<th>15</th>
<td>2.83</td>
<td>1.09</td>
<td>0.01</td>
<td>0.12</td>
<td>0.00</td>
<td>0.82</td>
<td>0.07</td>
<td>0.18</td>
<td>0.01</td>
<td>0.15</td>
<td>0.02</td>
<td>0.17</td>
<td>0.06</td>
<td>0.13</td>
<td>0.08</td>
<td>0.15</td>
</tr>
<tr>
<th>16</th>
<td>0.01</td>
<td>0.65</td>
<td>0.00</td>
<td>0.09</td>
<td>0.06</td>
<td>0.29</td>
<td>0.01</td>
<td>0.10</td>
<td>0.00</td>
<td>0.08</td>
<td>0.00</td>
<td>0.08</td>
<td>0.02</td>
<td>0.14</td>
<td>0.01</td>
<td>0.13</td>
</tr>
<tr>
<th>17</th>
<td>0.10</td>
<td>0.19</td>
<td>0.00</td>
<td>0.13</td>
<td>0.00</td>
<td>0.02</td>
<td>0.00</td>
<td>0.12</td>
<td>0.00</td>
<td>0.15</td>
<td>0.01</td>
<td>0.15</td>
<td>0.00</td>
<td>0.14</td>
<td>0.00</td>
<td>0.13</td>
</tr>
<tr>
<th>18</th>
<td>0.07</td>
<td>0.13</td>
<td>0.11</td>
<td>0.12</td>
<td>0.05</td>
<td>0.25</td>
<td>0.06</td>
<td>0.12</td>
<td>0.14</td>
<td>0.13</td>
<td>0.13</td>
<td>0.13</td>
<td>0.15</td>
<td>0.11</td>
<td>0.13</td>
<td>0.11</td>
</tr>
<tr>
<th>19</th>
<td>0.56</td>
<td>0.11</td>
<td>0.64</td>
<td>0.06</td>
<td>0.45</td>
<td>0.05</td>
<td>0.44</td>
<td>0.08</td>
<td>0.73</td>
<td>0.06</td>
<td>0.69</td>
<td>0.06</td>
<td>0.65</td>
<td>0.07</td>
<td>0.63</td>
<td>0.07</td>
</tr>
<tr>
<th>20</th>
<td>0.82</td>
<td>0.06</td>
<td>0.74</td>
<td>0.05</td>
<td>0.58</td>
<td>0.03</td>
<td>0.68</td>
<td>0.03</td>
<td>0.78</td>
<td>0.06</td>
<td>0.77</td>
<td>0.05</td>
<td>0.77</td>
<td>0.05</td>
<td>0.78</td>
<td>0.06</td>
</tr>
</tbody>
</table>

$^{\mathrm{a-e}}$Same footnotes as in Table II.

ing structure, before optimization by step 1, is shown in Fig. 6(d). After optimization of the structure, the new diagnosis (see Table IV, $n=3$) is $\psi_{12}^{\text{new}}=\psi_{12}^{\text{old}}-121^{\circ}$, leading to $\psi_{12}^{\text{new}}=-67^{\circ}$, a conformation shown in Fig. 6(e). This is already quite close to the "perfect" $\alpha$-helix, and two more iterations (see Table IV, $n=4$ and $n=5$) led to the global minimum.

## CONCLUSIONS

The numerical examples cited show that the SCEF method can start from many essentially different conformations of $\mathrm{CH}_{3} \mathrm{CO}-(\mathrm{Ala})_{19}-\mathrm{NHCH}_{3}$ and reach the $\alpha$-helical conformation in a few steps. Iteration is continued until the dipoles of the peptide units are optimally aligned with the local electrostatic field. In all the examples reported here, the minimum reached at the end of the procedure was always the "perfect" $\alpha$-helix, even when the initial conformation was far from the final one. The SCEF procedure can make *large* changes in $\phi$ and $\psi$, something that conventional direct energy minimization (which becomes trapped in local minima) cannot do. This, however, may lead to some complications; for example, for globular proteins, a large change in a dihedral angle may destroy the conformation of some parts of the molecule that are far from the defect. This problem is under investigation in our laboratory. Preliminary results for bovine pancreatic trypsin inhibitor (BPTI) show that the method detects electrostatic defects in the so-called native

![](./images/812276233562750976_9.jpg)

Fig. 6. (a) Conformations of the molecules (with four defects of the C type) after optimization (step 1). For a description of the atoms, see the caption to Fig. 3. Of the hydrogen bonds, 70.6% are broken, and the five remaining hydrogen bonds are present at the termini, i.e., about 1.5 turns of the $\alpha$-helix are present at each end of the molecule. Parts (b)-(e) show the evolution of conformation (a) during subsequent iterations of the SCEF procedure. The conformation displayed, (b)-(e), is always that obtained immediately after the diagnosis and before optimization (to show the effectiveness of the diagnosis of the SCEF method). (b) First iteration. Two turns of the $\alpha$-helix are completed at the N-terminus, with the C-terminus unchanged. (c) Second iteration. Three turns of the $\alpha$-helix are completed at the N-terminus, while the C-terminus remains unchanged. (d) Third iteration. Two turns of the $\alpha$-helix are now completed at the C-terminus, but the N-terminus does not change in this iteration. (e) Fourth iteration. The whole $\alpha$-helix has been completed, except for a minor defect at peptide unit 9. After the next two iterations, the SCEF procedure converges to the perfect finite $\alpha$-helix.

![](./images/812276233562750976_10.jpg)

Fig. 6. (Continued from the previous page.)

<table><thead><tr><th colspan="15">TABLE IV</th></tr><tr><th colspan="15">Energiesa, $-\Delta E_{i}^{CO}$ and $-\Delta E_{i}^{NH}$ for the Molecule with a Quadruple Defect</th></tr><tr><th>$\Delta l^{b}$</th><td colspan="2">3</td><td colspan="2">3</td><td colspan="2">3</td><td colspan="2">3</td><td colspan="2">3</td><td colspan="2">3</td></tr><tr><th>$M^{c}$</th><td colspan="2">4</td><td colspan="2">4</td><td colspan="2">4</td><td colspan="2">4</td><td colspan="2">4</td><td colspan="2">4</td></tr><tr><th>$n^{d}$</th><td colspan="2">0</td><td colspan="2">1</td><td colspan="2">2</td><td colspan="2">3</td><td colspan="2">4</td><td colspan="2">5</td></tr><tr><th>$i^{e}$</th><td>CO</td><td>NH</td><td>CO</td><td>NH</td><td>CO</td><td>NH</td><td>CO</td><td>NH</td><td>CO</td><td>NH</td><td>CO</td><td>NH</td></tr></thead><tbody><tr><td>1</td><td>2.11</td><td>0.45</td><td>2.52</td><td>0.70</td><td>2.55</td><td>0.55</td><td>2.40</td><td>0.53</td><td>2.27</td><td>0.50</td><td>2.28</td><td>0.50</td></tr><tr><td>2</td><td>0.31</td><td>0.84</td><td>2.26</td><td>1.04</td><td>0.08</td><td>0.56</td><td>0.11</td><td>0.53</td><td>0.19</td><td>0.59</td><td>0.19</td><td>0.59</td></tr><tr><td>3</td><td>1.91</td><td>0.48</td><td>0.08</td><td>0.28</td><td>0.00</td><td>0.04</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>4</td><td>0.71</td><td>0.08</td><td>0.00</td><td>0.06</td><td>0.15</td><td>0.27</td><td>0.10</td><td>0.25</td><td>0.10</td><td>0.20</td><td>0.11</td><td>0.20</td></tr><tr><td>5</td><td>0.27</td><td>0.00</td><td>0.38</td><td>1.02</td><td>0.08</td><td>0.20</td><td>0.01</td><td>0.19</td><td>0.04</td><td>0.16</td><td>0.06</td><td>0.16</td></tr><tr><td>6</td><td>3.75</td><td>1.31</td><td>0.32</td><td>0.17</td><td>0.53</td><td>0.22</td><td>0.36</td><td>0.18</td><td>0.00</td><td>0.11</td><td>0.00</td><td>0.08</td></tr><tr><td>7</td><td>0.02</td><td>0.57</td><td>0.86</td><td>0.03</td><td>0.10</td><td>0.00</td><td>0.06</td><td>0.01</td><td>0.01</td><td>0.06</td><td>0.00</td><td>0.06</td></tr><tr><td>8</td><td>0.07</td><td>0.04</td><td>0.31</td><td>0.20</td><td>0.14</td><td>0.00</td><td>0.63</td><td>0.08</td><td>0.00</td><td>0.13</td><td>0.00</td><td>0.25</td></tr><tr><td>9</td><td>2.64</td><td>0.89</td><td>2.84</td><td>1.68</td><td>1.03</td><td>1.50</td><td>0.83</td><td>1.47</td><td>0.08</td><td>0.03</td><td>0.58</td><td>0.10</td></tr><tr><td>10</td><td>0.02</td><td>0.58</td><td>0.12</td><td>0.67</td><td>2.66</td><td>0.96</td><td>2.49</td><td>0.88</td><td>0.13</td><td>0.10</td><td>0.18</td><td>0.25</td></tr><tr><td>11</td><td>0.26</td><td>0.16</td><td>0.21</td><td>0.07</td><td>0.18</td><td>0.03</td><td>0.20</td><td>0.04</td><td>0.23</td><td>0.27</td><td>0.00</td><td>0.02</td></tr><tr><td>12</td><td>1.56</td><td>1.09</td><td>1.77</td><td>0.99</td><td>3.77</td><td>1.43</td><td>3.10</td><td>1.31</td><td>0.04</td><td>0.05</td><td>0.08</td><td>0.10</td></tr><tr><td>13</td><td>0.13</td><td>0.58</td><td>0.35</td><td>0.87</td><td>1.09</td><td>0.99</td><td>0.10</td><td>0.48</td><td>0.03</td><td>0.09</td><td>0.08</td><td>0.17</td></tr><tr><td>14</td><td>0.24</td><td>0.32</td><td>0.58</td><td>0.32</td><td>0.90</td><td>0.65</td><td>0.08</td><td>0.18</td><td>0.04</td><td>0.14</td><td>0.01</td><td>0.11</td></tr><tr><td>15</td><td>2.56</td><td>1.17</td><td>2.66</td><td>1.56</td><td>4.22</td><td>1.58</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.10</td><td>0.01</td><td>0.09</td></tr><tr><td>16</td><td>0.10</td><td>0.56</td><td>0.10</td><td>0.82</td><td>0.02</td><td>0.90</td><td>0.07</td><td>0.22</td><td>0.00</td><td>0.11</td><td>0.01</td><td>0.12</td></tr><tr><td>17</td><td>0.02</td><td>0.26</td><td>0.09</td><td>0.36</td><td>0.18</td><td>0.36</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.09</td><td>0.00</td><td>0.12</td></tr><tr><td>18</td><td>0.07</td><td>0.20</td><td>0.01</td><td>0.28</td><td>0.00</td><td>0.45</td><td>0.17</td><td>0.06</td><td>0.08</td><td>0.12</td><td>0.12</td><td>0.10</td></tr><tr><td>19</td><td>0.69</td><td>0.08</td><td>0.48</td><td>0.16</td><td>0.50</td><td>0.11</td><td>0.69</td><td>0.04</td><td>0.60</td><td>0.07</td><td>0.60</td><td>0.06</td></tr><tr><td>20</td><td>0.88</td><td>0.08</td><td>0.65</td><td>0.07</td><td>0.83</td><td>0.08</td><td>0.70</td><td>0.04</td><td>0.76</td><td>0.06</td><td>0.74</td><td>0.05</td></tr><tr><td colspan="15">a-eSame footnotes as in Table II.</td></tr></tbody></table>

conformation of BPTI (as determined by x-ray crystallography) and, by removing them, shifts the conformation close to the "native" one, but with much lower energy (L. Piela, G. Némethy, and H. A. Scheraga, to be pub- lished).

It is as yet an open question as to how many solutions there are in the SCEF procedure. It is almost certain that some starting points will lead to no physically interesting solution. For example, one need only realize that, if the starting conformation were multiple knotted, it would be necessary to break one or more bonds in order to unravel it. Our impression is that some starting conformations could lead to other electrostatically favorable structures, differ- ent from an $\alpha$-helix, e.g., the $\beta$-sheet. If this were true, then the SCEF procedure would find several local minima (but a drastically reduced number) and not necessarily the global or native conformation. This question is presently under investigation in our laboratory.

The present paper may be summarized as follows:

1. Unlike other methods, the SCEF procedure does not make use of the thermodynamic hypothesis, which states that the native conformation corre- sponds to the free energy minimum. Instead, it provides a local picture, in which a peptide unit, being a very polar group of atoms, "detects" whether it is in a favorable or unfavorable conformation by comparing the orientation of its dipole moment with that of the electric field at this particular unit. Thus, the situation of the peptide unit is independent of whether the free energy of the whole polypeptide can (equilibrium thermodynamics) or cannot (nonequi- librium thermodynamics) be calculated, and it is independent of the total free energy of the molecule, except insofar as the latter is reflected in the electric field at this particular peptide unit. This is a reasonable feature of our method and implies that, in principle, the SCEF procedure may lead to a final structure that is different from the global minimum (this is formally similar to the situation in which a real molecule may be kinetically trapped in a local minimum).

2. The basic advantage of the SCEF method is that, in a particular step, it does not explore the whole conformational space as other methods do. This is because it detects where the largest defect in the structure exists and calcu- lates the direction in which to alleviate the defect. Thus, the SCEF method eliminates the principal difficulty in other methods (except the "build-up" procedure $^{6}$) of having to explore the whole conformational space.

3. The SCEF procedure changes the conformation of a polypeptide by steps, improving the orientation of the peptide unit in each step in response to the electrostatic field.

4. The SCEF procedure automatically predicts a motion in conformational space that, in fact, is cooperative (i.e., the predicted angle $\psi_{j}$ or $\phi_{j+1}$ strongly depends on the positions of other residues) and therefore formally exhibits this important feature of the real folding process. Indeed, very probably, the larger the number of peptide units that are oriented in an organized way, the stronger is the electric field that they produce on a poorly oriented peptide unit, and therefore, the more probable is its rotation towards the favorable orientation.

5. In the SCEF method, the electrostatic forces dictate the direction of the search for the most stable structure of a polypeptide molecule. At any stage of

the procedure, however, *all the other forces* included in the conformational potential energy modify the resulting structure. These corrections, however, are limited to changes within a local minimum.

6. The SCEF method does not need the long computation times that are generally required by other methods. The computation time for the diagnoses is negligible. The most time-consuming step is the minimization of the energy (step 1 of the SCEF procedure).

7. In the present formulation, the SCEF method does not treat the side- chain degrees of freedom (although the side chains participate in formation of the electric field) and does not take into account the microscopic structure of the solvent, the latter being treated in a primitive manner by use of a dielectric constant. Research on these problems is in progress in our labora- tory.

Note Added in Proof:

Since it is of interest to examine the relative energies of the conformations listed in Tables I-IV, we present them here in Table V.

<table>
<caption>TABLE V<br>Relative Energies</caption>
<thead>
<tr>
<th>Table No.</th>
<th>Conformation No.ᵃ</th>
<th>ECEPP Energyᵇ<br>(kcal/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>I</td>
<td>1ᶜ</td>
<td>– 47</td>
</tr>
<tr>
<td></td>
<td>2(C)</td>
<td>– 36</td>
</tr>
<tr>
<td></td>
<td>3(G)</td>
<td>– 38</td>
</tr>
<tr>
<td></td>
<td>4(E)</td>
<td>– 35</td>
</tr>
<tr>
<td></td>
<td>5(F)</td>
<td>– 35</td>
</tr>
<tr>
<td>II</td>
<td>1</td>
<td>– 32</td>
</tr>
<tr>
<td></td>
<td>2</td>
<td>– 31</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>– 26</td>
</tr>
<tr>
<td></td>
<td>4</td>
<td>– 29</td>
</tr>
<tr>
<td>III</td>
<td>1</td>
<td>– 21</td>
</tr>
<tr>
<td></td>
<td>2</td>
<td>– 38</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>– 22</td>
</tr>
<tr>
<td></td>
<td>4</td>
<td>– 31</td>
</tr>
<tr>
<td></td>
<td>5</td>
<td>– 16</td>
</tr>
<tr>
<td></td>
<td>6</td>
<td>– 25</td>
</tr>
<tr>
<td></td>
<td>7</td>
<td>– 24</td>
</tr>
<tr>
<td></td>
<td>8</td>
<td>– 29</td>
</tr>
<tr>
<td>IV</td>
<td>1</td>
<td>– 8</td>
</tr>
<tr>
<td></td>
<td>2</td>
<td>14</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>131</td>
</tr>
<tr>
<td></td>
<td>4</td>
<td>128</td>
</tr>
<tr>
<td></td>
<td>5</td>
<td>– 35</td>
</tr>
<tr>
<td></td>
<td>6</td>
<td>– 38</td>
</tr>
</tbody>
</table>

ᵃThe conformations are listed in the order in which they appear in the Tables. For conforma- tions with a single defect (Table I), the capital letters indicate the type of defect.
ᵇOnly the relative energies have physical significance²⁵,²⁶.
ᶜEnergy-minimized α-helix with no defect. In all four Tables, the conformation converged to the α-helix, with an energy of – 47 kcal/mol.

We are indebted to Drs. G. Némethy, R. Hoffmann, K. D. Gibson, and L. Glasser for helpful discussions, and to S. Rumsey for producing the figures. This work was supported by research grants from the National Institute of General Medical Sciences, of the National Institutes of Health (GM-14312), and from the National Science Foundation (DMB84-01811). Support was also received from the National Foundation for Cancer Research.

## References

1.  Némethy, G. & Scheraga, H. A. (1977) *Q. Rev. Biophys.* **10**, 239-352.
2.  Scheraga, H. A. (1981) *Biopolymers* **20**, 1877-1899.
3.  Meirovitch, H. & Scheraga, H. A. (1981) *Proc. Natl. Acad. Sci. USA*, **78**, 6584-6587.
4.  Wako, H. & Scheraga, H. A. (1982) *J. Protein Chem.* **1**, 85-117.
5.  Paine, G. H. & Scheraga, H. A. (1985) *Biopolymers* **24**, 1391-1436.
6.  Vásquez, M. & Scheraga, H. A. (1985) *Biopolymers* **24**, 1437-1447.
7.  Gibson, K. D., Chin, S., Pincus, M. R., Clementi, E. & Scheraga, H. A. (1986) in *Supercomputer Simulation in Chemistry*, Symposium in Montreal, August 25-27, 1985.
8.  Purisima, E. O. & Scheraga, H. A. (1986) *Proc. Natl. Acad. Sci. USA*, **83**, 2782-2786
9.  Matheson, R. R., Jr. & Scheraga, H. A. (1978) *Macromolecules* **11**, 819-829.
10. Blagdon, D. E. & Goodman, M. (1975) *Biopolymers* **14**, 241-245.
11. Levitt, M. & Chothia, C. (1976) *Nature* **261**, 552-558.
12. Wada, A. (1976) *Adv. Biophys.* **9**, 1-63.
13. Hol, W. G. J., Van Duijnen, P. Th. & Berendsen, H. J. C. (1978) *Nature*, **273**, 443-446.
14. Van Duijnen, P. Th., Thole, B. Th. & Hol, W. G. J. (1979) *Biophys. Chem.* **9**, 273-280.
15. Perutz, M. F. (1978) *Science* **201**, 1187-1191.
16. Jernigan, R. L., Miyazawa, S. & Szu, S. C. (1980) *Macromolecules* **13**, 518-525.
17. Hol, W. G. J., Halie, L. M. & Sander, C. (1981) *Nature* **294**, 532-536.
18. Wada, A. & Nakamura, H. (1981) *Nature* **293**, 757-758.
19. Sheridan, R. P., Levy, R. M. & Salemme, F. R. (1982) *Proc. Natl. Acad. Sci., USA* **79**, 4545-4549.
20. Chou, K. C., Némethy, G. & Scheraga, H. A. (1983) *J. Phys. Chem.* **87**, 2869-2881.
21. Hol, W. G. J. & DeMaeyer, M. C. H. (1984) *Biopolymers* **23**, 809-817.
22. Shoemaker, K. R., Kim, P. S., Brems, D. N., Marqusee, S., York, E. J., Chaiken, I. M., Stewart, J. M. & Baldwin, R. L. (1985) *Proc. Natl. Acad. Sci. USA* **82**, 2349-2353.
23. Scheraga, H. A. (1985) *Proc. Natl. Acad. Sci. USA* **82**, 5585-5587.
24. Némethy, G., Pottle, M. S. & Scheraga, H. A. (1983) *J. Phys. Chem.* **87**, 1883-1887.
25. Vásquez, M., Némethy, G. & Scheraga, H. A. (1983) *Macromolecules* **16**, 1043-1049.
26. Zimmerman, S. S., Pottle, M. S., Némethy, G. & Scheraga, H. A. (1977) *Macromolecules* **10**, 1-9.

Received February 28, 1986

Accepted June 18, 1986