# Localized Defects in Semiconductors: The Divacancy in Silicon‡

JOSPH CALLAWAY*
Department of Physics, University of California, Riverside, California
AND
A. JAMES HUGHES†
Applied Research Laboratory, Aeronutronic Division of Philco-Ford Corporation, Newport Beach, California
(Received 13 July 1967)

The energies of localized states associated with the neutral divacancy in silicon are computed using a procedure in which wave functions and potentials are expanded in terms of Wannier functions for the perfect crystal. The divacancy is represented by a pseudopotential. The lowest eight bands and the thirteen nearest unit cells (including the central cell where the atoms are missing) are considered. Lattice relaxation is neglected. Matrix elements of the Green's function and of the defect potential on the Wannier-function basis are obtained by numerical integration, using a pseudopotential band calculation. Two localized states of different symmetry are found to be possible.

## I. INTRODUCTION
TN a previous calculation, $^{1}$ we have developed a method for calculating the energies and wave func- tions of bound states associated with localized defects in semiconductors. In this approach, the wave function of the defect state is expanded in terms of Wannier functions for the perfect crystal. Matrix elements of the defect potential and of the Green's function on the Wannier function basis are formed by numerical inte- gration. Solution of a determinantal equation yields the energy of the bound state. In I, this procedure was applied to the isolated vacancy in silicon. Ten lattice sites and eight bands were included.

The results of that calculation showed that a bound state associated with the isolated vacancy could be ob- tained. This was sufficiently encouraging to suggest that it would be desirable to study another defect by these procedures, and we decided to investigate the di- vacancy. This has been done. The results, which are in many respects similar to those we obtained for the single vacancy, are reported here. Two bound states, of dif- ferent symmetry, can be obtained.

The experimental situation concerning the divacancy is quite complex. Information concerning the electronic states associated with this defect is derived from elec- tron-paramagnetic-resonance $^{2}$ (EPR) and infrared absorption measurements $^{3,4}$ in irradiated silicon. The experiments show that certain characteristic EPR spectra and infrared absorption bands are associated with the divacancy, and appear when the Fermi level is in some specific range. Since an EPR signal is observed only when there is an unpaired spin, it is necessary to assume that the defect can exhibit different charge states. Apparently there are four of these, involving a single positive, neutral, single negative, and double negative states.

Interpretation of the experimental data in terms of an energy-level scheme for the different charge states of the divacancy is subject to many uncertainties. We will discuss some of the possibilities in Sec. V in relation to the results of our calculation. Some orientation with re- spect to experiment is desirable, however, at this point.

The G6 EPR spectrum, which is associated with the single-positive-charge state, is observed in irradiated $p$-type silicon when the Fermi level is below about 0.25 eV above the valence band. Absorption of light of wave- length 0.25 eV bleaches the observed EPR signal. This is associated with a photoconductivity threshold and the beginning of an infrared absorption band centered at $3.9\ \mu$ (0.32 eV). It is natural to conclude from this that the lowest-energy state of the neutral divacancy is located at 0.25 eV above the valence band.

The G7 EPR spectrum is associated with the state in which the divacancy has a single negative charge. It is observed in irradiated $n$-type silicon but not until the Fermi level has dropped about 0.4 eV below the con- duction band. We may conclude from this that the double-negative-charge state of the divacancy is located at about this energy. There does not seem to be any conclusive evidence concerning the energy of the state with a single negative charge, except that it should be between 0.25 eV above the valence band and 0.4 eV below the conduction band-a range of about 0.45 eV.

Two other infrared absorption bands associated with the divacancy are found at $1.8\ \mu$ (0.69 eV) in both $n$- and $p$-type silicon and at $3.3\ \mu$ (0.38 eV) in $n$-type sili- con. It appears that these bands are not associated with a photoconductivity threshold; they may there- fore correspond to transitions involving excited states of the divacancy. We will return to this problem in Sec. V

*Present address: Department of Physics, Louisiana State University, Baton Rouge, Louisiana
†Present address: Theoretical Physics Department, Research and Engineering Division, Autonetics, Anaheim, California.
‡ Supported by the Philco-Ford Corporation.
1 J. Callaway and A. J. Hughes, Phys. Rev. 156, 860 (1967). This paper is referred to as I.
2 G. D. Watkins and J. W. Corbett, Phys. Rev. 138, A543 (1965).
3 H. Y. Fan and A. K. Ramdas, J. Appl. Phys. 30, 1127 (1959).
4 L. J. Cheng, J. C. Corelli, J. W. Corbett, and G. D. Watkins, Phys. Rev. 152, 761 (1966).

---
164 1043

The plan of this paper is as follows: In Sec. II, we review the general procedures of the calculation, which were presented at greater length in I. Section III con- tains a discussion of the symmetry properties of the wave functions we consider. Our results are presented in Sec. IV. The results are compared with experiment in Sec. V, which also contains our conclusions.

## II. SUMMARY OF THE METHOD
The computation of the properties of localized defect states in semiconductors can be based on the methods of solid-state scattering theory. $^{1,5}$ In this section we shall briefly summarize the method as applied to the silicon divacancy. Reference 1 is followed closely and should be consulted for a more detailed description of our procedure.

Let the Hamiltonian of the perfect crystal including the periodic potential be denoted by $H_{0}$, and the change in crystal potential produced by the introduction of the defect be denoted by $V$. We define a Green's function $G$ by
$$G=\left(E-H_{0}\right)^{-1}. \quad(2.1)$$

Since we are concerned here with bound states, the quantity $E$ which appears may be taken to be a real energy.

Consider the determinantal function $D(E)$ defined by
$$D(E)=\operatorname{det}[I-G V],\qquad(2.2)$$
where $I$ is a unit operator. For every real $E$, say $E_{0}$, for which Eq. (2.2) vanishes, the operator $I-G V$ is singu lar. Hence there must exist some vector $|\phi\rangle$ which is annihilated by the operator $I-G(E_{0}) V$ . This implies that $|\phi\rangle$ is a solution of the Schrödinger equation for energy $E_{0}$ 
$$\left(H_{0}+V\right)|\phi\rangle=E_{0}|\phi\rangle.\qquad(2.3)$$

Thus the problem of solving the Schrödinger equa- tion for the energy of a defect state may be approached by looking for the roots of $D(E)$ . We do not require the full (infinite) matrix $G$ in order to evaluate $D(E)$ in the case of a potential of finite range. It is sufficient to ob- tain that portion which has the same extension in the sites and in the bands as $V$ does. From here on, we will use the symbol $G$ to refer to this sub matrix. It is also convenient to invert the sub matrix $G$ and solve instead
$$\operatorname{det}\left[G^{-1}-V\right]=0.\qquad(2.4)$$

A suitable basis for the representations of operators must be selected. For localized defect problems the Wannier functions are appropriate and appear to have considerable advantage.

The formal definitions of the Wannier functions and the Bloch function for band $n$ and wave vector $k$ , and is an eigenfunction of $H_{0}$ with an energy band function $E_{n}(k)$ .
$$H_{0} \Psi_{n}(\mathbf{k}, \mathbf{r})=E_{n}(\mathbf{k}) \Psi_{n}(\mathbf{k}, \mathbf{r}).\qquad(2.5)$$

The Wannier function is defined by
$$a_{n}\left(\mathbf{r}-\mathbf{R}_{\mu}\right)=\frac{\Omega^{1 / 2}}{(2 \pi)^{3 / 2}} \int_{\text {B.Z. }} d^{3} k \exp \left[-i \mathbf{k} \cdot \mathbf{R}_{\mu}\right] \Psi_{n}(\mathbf{k}, \mathbf{r}) \text { (2.6) }$$
in which $R_{\mu}$ is a lattice vector, $\Omega$ is the volume of the unit cell, and the integral is over the Brillouin zone. As is well known, the Wannier functions are orthogonal in both the band and site indices. The elements of the Green's function on the Wannier basis are given by
$$\begin{aligned}
(n \mu|G| l \nu) & =\int a_{n}{ }^{*}\left(\mathbf{r}-\mathbf{R}_{\mu}\right) \frac{1}{E-H_{0}} a_{l}\left(\mathbf{r}-\mathbf{R}_{\nu}\right) d^{3} r \\
& =\frac{\delta_{n l} \Omega}{(2 \pi)^{3}} \int \frac{d^{3} k \exp -i \mathbf{k} \cdot\left(\mathbf{R}_{\mu}-\mathbf{R}_{\nu}\right)}{E-E_{n}(\mathbf{k})}.
\end{aligned}\qquad(2.7)$$

Finally, the defect potential on this basis is given by
$$(n \mu|V| l \nu)=\int a_{n}^{*}\left(\mathbf{r}-\mathbf{R}_{\mu}\right) V(\mathbf{r}) \alpha_{l}\left(\mathbf{r}-\mathbf{R}_{\nu}\right) d^{3} r. \quad(2.8)$$

In treating the divacancy in silicon, we have em- ployed Bloch functions, energy band functions, and Green's functions which were obtained in our earliercalculation of the energy levels of the single vacancy. $^{1}$  The potential matrix elements of the divacancy were then calculated and the zeros of the determinantal func- tion (2.2) located.

Let us briefly summarize the procedure employed in Ref. 1. In order to determine energy levels of bound states associated with a vacancy or divacancy, it is necessary to have an expression for the change in po- tential produced by the removal of silicon atoms. The total crystal potential can be represented as the sum of potentials due to the individual atoms. If relaxation of atoms near the divacancy is ignored, the defect per- turbation will be the negative of the potentials of the missing silicon atoms. The true wave functions for valence states, including those associated with a defect, must be orthogonal to the wave function of core elec- trons. In order to circumvent difficulties associated with the strength of the true potential and with the orthogonality requirement, the pseudopotential method(see Harrison $^{6}$ for a review of the procedure) may be employed. In order to simplify our calculations, the pseudopotential method was employed to obtain wave functions and energy band functions in the perfect crystal and, in addition, was used to represent the di- vacancy defect potential. The Wannier functions of our calculation were then constructed from the pseudo- potential wave functions.

5 J. Callaway, J. Math. Phys. 5, 783 (1964).
6 W. A. Harrison, Pseudopotentials in the Theory of Metals(W. A. Benjamin, Inc., New York, 1966), p. 19.

To construct Wannier functions, Bloch functions for the entire Brillouin zone are required. It is convenient to divide the Brillouin zone into equivalent 1/48 sub-zones. Wave functions and energy band functions are obtained directly in 1/48 of the Brillouin zone and then transformed to obtain states elsewhere in the Brillouin zone. Since Wannier functions may be altered by a change in phase of the Bloch functions from which they are constructed, it is necessary to specify phase factors brought in by transformations completely. This question was investigated in Ref. 1. It was shown that for isolated energy bands, that is, energy bands which do not touch (interact with) or cross other bands, the following relation is obeyed by the Bloch function at points $\alpha \mathbf{k}$ in the star of $\mathbf{k}$.

$$
\left(\alpha\left|\mathbf{t}_{\alpha}\right) \Psi_{n}(\mathbf{k}, \mathbf{r})=\chi_{n}{ }^{(j)}(\alpha) \exp \left[-i \alpha \mathbf{k} \cdot \mathbf{t}_{\alpha}\right] \Psi_{n}(\alpha \mathbf{k}, \mathbf{r}) ; \quad(2.9)\right.
$$

$\chi_{n}^{(j)}(\alpha)$ is the character for the operation $\alpha$ in the $j$ th one-dimensional representation of the point group. The effect of Eq. (2.9) is to ensure, as far as possible, smooth behavior of the wave function as its argument $\mathbf{k}$ goes around the Brillouin zone. From Eqs. (2.9) and (2.6), it follows that the Wannier functions associated with isolated energy bands transform according to the onedimensional representations of the diamond point group.

Wave functions and energy band functions were obtained numerically for silicon from a pseudopotential band calculation. Brust's⁷ parameters were employed, and only the lowest 15 plane waves were included. As an illustration, we show the band structure obtained along one line (of no symmetry) in the Brillouin zone in Fig. 1.

An investigation of the conduction bands showed that these bands were not isolated, but were interacting and exhibited quasidegeneracies. As a result, if one constructs energy bands according to the usual "energy ordering" scheme, the resulting wave functions are not smooth functions of $k$ throughout the Brillouin zone. Problems arise at points of quasidegeneracy where two bands approach closely. Although the energy bands—as defined above—do not cross, the wave functions vary rapidly with $k$ in the small region in which the bands interact strongly. Away from the region of close approach, the wave functions are such that the bands appear to have crossed and thus switched their symmetries. Thus, at points of quasidegeneracy, energy bands could be defined either by "energy ranking" or by symmetry of the associated wave functions. We note that if "energy ranking" is employed to define the bands involving quasidegeneracies, they will be of "mixed" symmetries. We have consistently defined our energy bands such that they are always of the single symmetry type, so that the "simple" band analysis is applicable. This "single" symmetry prescription is of considerable convenience in that group-theoretic analysis and simplifications may be applied to the Wannier functions and to the determination of the bound states of the defect. This group-theoretic analysis is carried out in the next section for the divacancy. The symmetries of the Wannier functions for the lowest eight bands are listed in Table I.

![](./images/813231707443429379_1.jpg)

FIG. 1. Energy bands in silicon as calculated with Brust's pseudopotential parameters and 15 plane waves along the line $\Gamma-Q\left[\left(\frac{1}{3}, 2,1\right)\right.$ axis $]$ in the Brillouin zone. The bands are numbered in order of increasing energy. The separation between $\Gamma_{2}^{\prime}$ and $\Gamma_{25}^{\prime}$ has been slightly increased for clarity.

TABLE I. Symmetry assignments for the calculated energy bands. All Wannier functions formed from a given band are thus either real (R) or pure imaginary (I) as indicated in the third column above.

| Band | $O_{h}$ |   |
|------|---------|---|
| 1    | $\Gamma_{1}$ | R |
| 2    | $\Gamma_{2}^{\prime}$ | I |
| 3    | $\Gamma_{1}$ | R |
| 4    | $\Gamma_{1}^{\prime}$ | I |
| 5    | $\Gamma_{1}$ | R |
| 6    | $\Gamma_{2}^{\prime}$ | I |
| 7    | $\Gamma_{2}^{\prime}$ | I |
| 8    | $\Gamma_{2}$ | R |

⁷ D. Brust, Phys. Rev. 134, A1337 (1964).

### III. SYMMETRY ANALYSIS OF THE DIVACANCY ON THE WANNIER FUNCTION BASIS

The origin for the Bloch functions and hence for the defect problem is located midway between the two atoms in a silicon unit cell. The two atoms are thus located at $\pm d=\pm \frac{1}{8} a(1,1,1)$. To create a divacancy we remove the two atoms in the unit cell at the origin.

Before discussing the group theory for the defect, a comment on notation should be made. We have three

TABLE II. Coordinates of the two vacancy sites $c$ and $c^{\prime}$ and their first neighbors. $\gamma$ is the Jahn-Teller distortion parameter and is a small positive number. The vectors are in units of $\frac{1}{4} a$ and our choice of coordinate axes differs from that of Watkins and Corbett (Ref. 2).

$$
\begin{aligned}
a & =\left(\frac{1}{4},-\frac{3}{4},-\frac{3}{4}\right)+\gamma(-1,1,0) \\
b & =\left(-\frac{3}{4},-\frac{3}{4}, \frac{1}{4}\right) \\
c & =\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right) \\
d & =\left(-\frac{3}{4}, \frac{1}{4},-\frac{3}{4}\right)-\gamma(-1,1,0) \\
a^{\prime} & =\left(-\frac{1}{4}, \frac{3}{4}, \frac{3}{4}\right)-\gamma(-1,1,0) \\
b^{\prime} & =\left(\frac{3}{4}, \frac{3}{4},-\frac{1}{4}\right) \\
c^{\prime} & =\left(-\frac{1}{4},-\frac{1}{4},-\frac{1}{4}\right) \\
d^{\prime} & =\left(\frac{3}{4},-\frac{1}{4}, \frac{3}{4}\right)+\gamma(-1,1,0)
\end{aligned}
$$

different point groups to consider, $O_{h}$ for the silicon perfect crystal, $D_{3 d}$ for the divacancy without distortion or relaxation, and $C_{2 h}$ for the divacancy with a JahnTeller distortion. For consistency, we have employed the same $O_{h}$ labeling $^{8,9}$ of irreducible representations for all three groups. Thus our notation for $D_{3 d}$ will differ from that of Koster. $^{10}$ The character tables for $D_{3 d}$ and $C_{2 h}$ may be obtained from the $O_{h}$ character table with the proper deletions.

Table II contains the coordinates of the two vacan- cies $c$ and $c^{\prime}$ and the nearest-neighbor atoms to the va cancies. $\gamma(\overline{1} 10)$ represents the change in coordinate position due to a Jahn-Teller distortion and $\gamma$ is a small positive number. Thus atoms $a$ and $d$ move toward each other, as do atoms $a^{\prime}$ and $d^{\prime}$.

To simulate the divacancy potential without distor- tion, we subtract atomic pseudopotentials at the atom sites labeled $c$ and $c^{\prime}$. It is seen that there are 12 sym metry operations for this defect potential and that the group is $D_{3 d}$. To simulate the defect potential with dis tortion, the atoms $a, d, a^{\prime}, d^{\prime}$ (and associated pseudo potentials) would be removed (subtracted) at distor tion-free positions and placed (added) at the locations shown in Table II. Thus the symmetry group $(C_{2 h})$ with distortion is seen to consist of the four operations given in Table III.

The calculations reported herein all pertain to a di vacancy without Jahn-Teller distortion. To include dis tortion and consider the same number of lattice sites as was done for $D_{3 d}$ in order to obtain convergent results would increase the numerical labor involved beyond the bounds of feasibility. It is therefore of interest to see what statements can be made about similarities or dif ferences in the problems as treated with and without Jahn-Teller distortion. It is rather difficult to assess the changes in bound-state energy levels to be expected in going from $D_{3 d}$ to $C_{2 h}$. It may be shown for the one dimensional representations and for the central-cell $[(0,0,0)$ lattice site] matrix elements that the bands which contribute are the same in both $D_{3 d}$ and $C_{2 h}$. For the remaining site groups, the transformation to $C_{2 h}$ brings additional bands and interband couplings into the problem.

A total of eight bands (four valence and four conduc tion) and thirteen lattice sites have been considered. These sites and the associated site group index for sym metrized combinations of Wannier functions are listed in Table IV.

In calculations of this nature, the most labor is in volved in the calculation of the matrix elements of the defect potential on the Wannier basis. We shall see that group theory can be employed to substantially reduce the labor involved. As the problem is now phrased, eight bands and thirteen lattice vectors yield a defect potential matrix of order $104 \times 104$; hermiticity reduces this to a consideration of 5460 elements. By an applica tion of group theory, many of the matrix elements can be shown to be either zero or simply related to other matrix elements.

Consider the matrix element
$$
(n \mu|V| l \nu)=\int a_{n} *\left(\mathbf{r}-\mathbf{R}_{\mu}\right) V(\mathbf{r}) a_{l}\left(\mathbf{r}-\mathbf{R}_{\nu}\right) d^{3} r. \quad(3.1)
$$

It was shown $^{1}$ that for an operation $\{\beta \mid 0\}$ in the sym metry group of the defect potential the following relation between matrix elements holds:
$$
(n \mu|V| l \nu)=\chi_{n}^{(j)}(\beta) \chi_{l}^{(k)}(\beta)(n \rho|V| l \tau), \quad(3.2)
$$
where $\mathbf{R}_{\mu}=\beta \mathbf{R}_{\rho}, \mathbf{R}_{\nu}=\beta \mathbf{R}_{\tau}$, and $\chi_{n}^{(j)}$ and $\chi_{l}^{(k)}$ are the appropriate characters for operation $\beta$ for bands $n$ and $l$. Thus $(n \mu|V| l \nu)$ and $(n \rho|V| l \tau)$ are simply related. Applying Eq. (3.2) to determine the number of independent matrix elements for the thirteen-site problem, we find that there are fourteen different site vector pairs which must be considered. These are listed in Table V. For eight bands Table V represents 644 matrix elements. Using Eq. (3.2), several of the matrix elements can be shown to vanish by symmetry. The number of matrix elements which must be calculated

<table><thead><tr><td><b>Class</b></td><td><b>$D_{3d}$ Operations in</b></td><td><b>Operations in $C_{2h}$</b></td></tr></thead><tbody><tr><td><b>E</b></td><td><b>x y z</b></td><td><b>x y z</b></td></tr><tr><td><b>$JC_{2}$</b></td><td><b>y x z</b></td><td><b>y x z</b></td></tr><tr><td></td><td><b>z y x</b></td><td></td></tr><tr><td></td><td><b>x z y</b></td><td></td></tr><tr><td><b>$C_{3}$</b></td><td><b>z x y</b></td><td></td></tr><tr><td></td><td><b>y z x</b></td><td></td></tr><tr><td><b>J</b></td><td><b>$\overline {x}\overline {y}\overline {z}$</b></td><td><b>$\overline {x}\overline {y}\overline {z}$</b></td></tr><tr><td><b>$C_{2}$</b></td><td><b>$\overline {y}\overline {x}\overline {z}$</b></td><td><b>$\overline {y}\overline {x}\overline {z}$</b></td></tr><tr><td></td><td><b>$\overline {z}\overline {y}\overline {x}$</b></td><td></td></tr><tr><td></td><td><b>$\overline {x}\overline {z}\overline {y}$</b></td><td></td></tr><tr><td><b>$JC_{3}$</b></td><td><b>$\overline {z}\overline {x}\overline {y}$</b></td><td></td></tr><tr><td></td><td><b>$\overline {y}\overline {z}\overline {x}$</b></td><td></td></tr></tbody></table>

TABLE III. Symmetry operations in the group of the defect potential for $D_{3 d}$ and $C_{2 h}$.

8 J. Callaway, Energy Band Theory (Academic Press Inc., New York, 1964), p. 23.
9 L. Marriot, Group Theory and Solid State Physics (Prentice- Hall, Inc., Englewood Cliffs, New Jersey, 1962), p. 80.
10 G. F. Koster, in Solid State Physics, edited by F. Seitz and D. Turnbull (Academic Press Inc., New York, 1957), Vol. 5, p. 173.

is shown in the fourth column of Table V giving a total of 510 elements.

No further simplifications can be achieved using single Wannier functions as basis functions. On this basis the solution of a 104×104 determinantal equation would be required. We now wish to consider the factorization of the determinant $D(E)$ into small subdeterminants. This is done by the application of standard techniques to construct symmetrized linear combinations of Wannier functions which transform according to irreducible representations of the symmetry group of the defect potential. In particular, if we want a linear combination of Wannier functions which belong to the $\sigma$th row of the $s$th irreducible representation of the group of the potential (we denote operations in this group by $\beta$), we form the combination

$$
\begin{aligned}
A_{n}^{(\sigma, s)}\left(\mathbf{r} ; R_{\mu}\right) & \sim \sum_{\beta} D_{\sigma, \sigma}{ }^{(s)}(\beta)\{\beta \mid 0\} a_{n}\left(\mathbf{r}-\mathbf{R}_{\mu}\right) \\
& =\sum_{\beta} D_{\sigma, \sigma}{ }^{(s)}(\beta) \chi_{n}{ }^{(j)}(\beta) a_{n}\left(\mathbf{r}-\beta \mathbf{R}_{\mu}\right). \quad(3.3)
\end{aligned}
$$

The symmetrized Wannier function $A_{n}^{(\sigma, s)}(\mathbf{r} ; R_{\mu})$ is thus characterized by row $\sigma$, representation $s$, band $n$, and site group $R_{\mu}$. For the thirteen lattice vectors in Table IV we have three site groups. For one-dimensional representations we would thus obtain a secular determinant no larger than 24×24. However, for particular site groups, (nonzero) symmetrized Wannier functions cannot be formed from all eight bands. These results are contained in Table VI for the 4 one-dimensional groups of the defect potential. We see that the determinants for $\Gamma_{1}$ and $\Gamma_{2}{ }^{\prime}$ would be 13×13 and the determinants for $\Gamma_{2}$ and $\Gamma_{1}{ }^{\prime}$ would be 7×7.

An examination of Table VI and our numerical matrix elements indicated that, among the one-dimensional representations, solutions of $\Gamma_{1}$ and $\Gamma_{2}{ }^{\prime}$ symmetry were most likely to contain bound states. We have, therefore, limited our attention to these two representations. The numerical results are presented in the next section.

TABLE IV. Column 1 contains the site group index for $D_{3 d}$. Column 2 lists the vectors in the site groups in units of $\frac{1}{2} a$. Columns 3 and 4 are the distance squared from the lattice site $\mathbf{R}_{n}$ to the vacancies at $+\mathbf{d}$ and $-\mathbf{d}$.

<table>
<thead>
<tr>
<th>Site Group</th>
<th>$\{ \mathbf {R}_{n}\} $</th>
<th>$|\mathbf {R}_{n}-\mathbf {d}|^{2}$</th>
<th>$|\mathbf {R}_{n}+\mathbf {d}|^{2}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>$(0,0,0)$</td>
<td>$\frac {3}{16}$</td>
<td>$\frac {3}{16}$</td>
</tr>
<tr>
<td>2</td>
<td>$(1,1,0)$</td>
<td>$1\frac {3}{16}$</td>
<td>$3\frac {3}{16}$</td>
</tr>
<tr>
<td></td>
<td>$(0,1,1)$</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$(1,0,1)$</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$(1,\overline {1},0)$</td>
<td>$3\frac {3}{16}$</td>
<td>$1\frac {3}{16}$</td>
</tr>
<tr>
<td></td>
<td>$(0,\overline {1},1)$</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$(1,0,\overline {1})$</td>
<td></td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>$(1,\overline {1},0)$</td>
<td>$2\frac {3}{16}$</td>
<td>$2\frac {3}{16}$</td>
</tr>
<tr>
<td></td>
<td>$(0,1,\overline {1})$</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$(1,0,1)$</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$(1,1,0)$</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$(0,\overline {1},1)$</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>$(1,0,\overline {1})$</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

TABLE V. The fourteen types of potential matrix elements which must be considered for the three site group problem involving thirteen lattice site vectors.

<table>
<thead>
<tr>
<th>Pair index</th>
<th>Matrix element</th>
<th>Band indices</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>$(s,000|V|t,000)$</td>
<td>$t\geq s$</td>
<td>14</td>
</tr>
<tr>
<td>2</td>
<td>$(s,000|V|t,110)$</td>
<td>$s,t$</td>
<td>40</td>
</tr>
<tr>
<td>3</td>
<td>$(s,000|V|t,1\overline {1}0)$</td>
<td>$s,t$</td>
<td>32</td>
</tr>
<tr>
<td>4</td>
<td>$(s,110|V|t,110)$</td>
<td>$t\geq s$</td>
<td>24</td>
</tr>
<tr>
<td>5</td>
<td>$(s,110|V|t,011)$</td>
<td>$t\geq s$</td>
<td>36</td>
</tr>
<tr>
<td>6</td>
<td>$(s,110|V|t,\overline {1}\overline {1}0)$</td>
<td>$t\geq s$</td>
<td>24</td>
</tr>
<tr>
<td>7</td>
<td>$(s,110|V|t,0\overline {1}\overline {1})$</td>
<td>$t\geq s$</td>
<td>36</td>
</tr>
<tr>
<td>8</td>
<td>$(s,110|V|t,01\overline {1})$</td>
<td>$s,t$</td>
<td>64</td>
</tr>
<tr>
<td>9</td>
<td>$(s,110|V|t,\overline {1}01)$</td>
<td>$s,t$</td>
<td>64</td>
</tr>
<tr>
<td>10</td>
<td>$(s,110|V|t,10\overline {1})$</td>
<td></td>
<td>64</td>
</tr>
<tr>
<td>11</td>
<td>$(s,1\overline {1}0|V|t,1\overline {1}0)$</td>
<td>$t\geq s$</td>
<td>20</td>
</tr>
<tr>
<td>12</td>
<td>$(s,1\overline {1}0|V|t,01\overline {1})$</td>
<td>$t\geq s$</td>
<td>36</td>
</tr>
<tr>
<td>13</td>
<td>$(s,1\overline {1}0|V|t,\overline {1}10)$</td>
<td>$t\geq s$</td>
<td>20</td>
</tr>
<tr>
<td>14</td>
<td>$(s,110|V|t,0\overline {1}1)$</td>
<td>$t\geq s$</td>
<td>36</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>$\overline {510}$</td>
</tr>
</tbody>
</table>

## IV. RESULTS

As was done in I, we have inserted a continuous parameter $\lambda$ into the determinantal equation for the energies of bound states
$$
\operatorname{det}\left[G^{-1}-\lambda V\right]=0. \quad(4.1)
$$

We may suppose that symmetrized basis functions have been employed in constructing the matrices $G$ and $V$ so that Eq. (4.1) pertains to a single irreducible representation. The energies of bound states determined from Eq. (4.1) are functions of $\lambda$; since $\lambda$ effectively controls the strength of the potential, we can determine the dependence of the bound-state energies on the strength of the potential. Additional information can be obtained by changing the size of the matrices: that is, we can delete various bands or lattice site groups.

The energies of the bound states belonging to the $\Gamma_{1}$ and $\Gamma_{2}{ }^{\prime}$ representations are shown as functions of $\lambda$ in Fig. 2. In this case all the relevant bands have been included with three site groups (the central cell plus nearest twelve neighboring cells) being considered. The results are particularly interesting in that they indicate that bound states are possible in both representations for values of $\lambda$ between 1 and 2. There is, in fact, a small region of values of $\lambda$, between 1.29 and 1.38 in which bound states occur in both representations, with that belonging to $\Gamma_{2}{ }^{\prime}$ having an energy about 0.7 eV larger than that belonging to $\Gamma_{1}$. In this range of $\lambda$, we therefore find that both a ground state and an excited state of the divacancy are possible. The symmetries of these states are such that an optical transition between them would be allowed. It is possible to interpret the experimental infrared absorption measurements of Cheng et al. $^{4}$ in such a way that one of the observed absorption bands corresponds to this transition.

Some information concerning the nature of the wave functions for these states may be obtained by examining the eigenvectors. These are listed in Table VII for an

![](./images/813231707443429379_2.jpg)

FIG. 2. Energies of divacancy states of symmetry $\Gamma_{1}$ and $\Gamma_{2}^{\prime}$ as functions of $\lambda$. The scale of energy employed places the valenceband maximum at 0.0 eV and the conduction-band minimum at 0.92 eV. This is not in exact agreement with experiment since the experimental band gap is not precisely obtained with Brust's pseudopotential parameters and 15 plane waves.

energy 0.06 eV above the valence band. The eigenvectors are, of course, functions of $E$ and thus of $\lambda$ corresponding to the curves of Fig. 2; the qualitative characteristics of the two given in Table VII are retained. It will be noticed that the eigenvector for $\Gamma_{2}^{\prime}$ is dominated by the contribution of band 2 while for $\Gamma_{1}$, no single contribution appears to be as important.

The relative importance of individual bands to the $E(\lambda)$ curves was investigated deleting them singly or in combination. Generally, one can say that removing a conduction band shifts the $E(\lambda)$ curve to the left, that is, to smaller values of $\lambda$, while removing a valence band shifts the curve to larger values of $\lambda$. We have found only one situation which is inconsistent with this simple statement: Removal of the contribution from band 4 in the $\Gamma_{1}$ representation has an effect opposite to that expected.

Some of the information obtained by deleting bands is shown in Figs. 3 and 4. We see in these figures that removal of all conduction bands does shift the curves somewhat to the left; however, these shifts are small compared to those obtained by deleting valence bands 1 and 2. The shift of the $E(\lambda)$ curves in those cases; from a region near $\lambda=1$ to one near $\lambda=8$, indicates the vital importance of the lowest bands in these states.

TABLE VI. List of the symmetrized linear combinations of Wannier functions which can be formed for the three site groups and eight bands. "0" indicates that a (nonzero) symmetrized Wannier function cannot be formed for the band and site in question.

<table>
<thead>
<tr>
<th>Representation<br>Site group<br>Band</th>
<th>$\Gamma_{1}$<br>1 2 3</th>
<th>$\Gamma_{2}$<br>1 2 3</th>
<th>$\Gamma_{1}'$<br>1 2 3</th>
<th>$\Gamma_{2}'$<br>1 2 3</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 $\Gamma_{1}$</td>
<td>$x x x$</td>
<td>$0 0 0$</td>
<td>$0 0 x$</td>
<td>$0 x 0$</td>
</tr>
<tr>
<td>2 $\Gamma_{2}'$</td>
<td>$0 x 0$</td>
<td>$0 0 x$</td>
<td>$0 0 0$</td>
<td>$x x x$</td>
</tr>
<tr>
<td>3 $\Gamma_{1}$</td>
<td>$x x x$</td>
<td>$0 0 0$</td>
<td>$0 0 x$</td>
<td>$0 x 0$</td>
</tr>
<tr>
<td>4 $\Gamma_{1}'$</td>
<td>$0 0 x$</td>
<td>$0 x 0$</td>
<td>$x x x$</td>
<td>$0 0 0$</td>
</tr>
<tr>
<td>5 $\Gamma_{1}$</td>
<td>$x x x$</td>
<td>$0 0 0$</td>
<td>$0 0 x$</td>
<td>$0 x 0$</td>
</tr>
<tr>
<td>6 $\Gamma_{2}'$</td>
<td>$0 x 0$</td>
<td>$0 0 x$</td>
<td>$0 0 0$</td>
<td>$x x x$</td>
</tr>
<tr>
<td>7 $\Gamma_{2}'$</td>
<td>$0 x 0$</td>
<td>$0 0 x$</td>
<td>$0 0 0$</td>
<td>$x x x$</td>
</tr>
<tr>
<td>8 $\Gamma_{2}$</td>
<td>$0 0 0$</td>
<td>$x x x$</td>
<td>$0 x 0$</td>
<td>$0 0 x$</td>
</tr>
</tbody>
</table>

TABLE VII. Eigenvectors for the $\Gamma_{1}$ and $\Gamma_{2}^{\prime}$ representations are listed for $E=0.06$ eV (above the valence band). $\lambda=1.32$ for $\Gamma_{1}$ and 1.08 for $\Gamma_{2}'$.

<table>
<thead>
<tr>
<th>Site<br>group</th>
<th>$\Gamma_{1}$<br>Band</th>
<th>Component</th>
<th>Site<br>group</th>
<th>$\Gamma_{2}'$<br>Band</th>
<th>Component</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 0 0</td>
<td>1</td>
<td>$-0.4938$</td>
<td>0 0 0</td>
<td>1</td>
<td>$-0.7902$</td>
</tr>
<tr>
<td>0 0 0</td>
<td>3</td>
<td>$0.3317$</td>
<td>0 0 0</td>
<td>6</td>
<td>$0.1095$</td>
</tr>
<tr>
<td>0 0 0</td>
<td>5</td>
<td>$-0.3982$</td>
<td>0 0 0</td>
<td>7</td>
<td>$0.2578$</td>
</tr>
<tr>
<td>1 1 0</td>
<td>1</td>
<td>$-0.1069$</td>
<td>1 1 0</td>
<td>1</td>
<td>$0.2635$</td>
</tr>
<tr>
<td>1 1 0</td>
<td>2</td>
<td>$-0.3159$</td>
<td>1 1 0</td>
<td>2</td>
<td>$-0.3794$</td>
</tr>
<tr>
<td>1 1 0</td>
<td>3</td>
<td>$-0.0212$</td>
<td>1 1 0</td>
<td>3</td>
<td>$-0.1650$</td>
</tr>
<tr>
<td>1 1 0</td>
<td>5</td>
<td>$0.0998$</td>
<td>1 1 0</td>
<td>5</td>
<td>$0.1192$</td>
</tr>
<tr>
<td>1 1 0</td>
<td>6</td>
<td>$0.1044$</td>
<td>1 1 0</td>
<td>6</td>
<td>$0.0223$</td>
</tr>
<tr>
<td>1 1 0</td>
<td>7</td>
<td>$0.1623$</td>
<td>1 1 0</td>
<td>7</td>
<td>$-0.0182$</td>
</tr>
<tr>
<td>$\overline{1} 1 0$</td>
<td>1</td>
<td>$0.0577$</td>
<td>$\overline{1} 1 0$</td>
<td>2</td>
<td>$-0.1932$</td>
</tr>
<tr>
<td>$\overline{1} 1 0$</td>
<td>3</td>
<td>$0.4068$</td>
<td>$\overline{1} 1 0$</td>
<td>6</td>
<td>$0.0071$</td>
</tr>
<tr>
<td>$\overline{1} 1 0$</td>
<td>4</td>
<td>$0.3975$</td>
<td>$\overline{1} 1 0$</td>
<td>7</td>
<td>$0.0288$</td>
</tr>
<tr>
<td>$\overline{1} 1 0$</td>
<td>5</td>
<td>$-0.0430$</td>
<td>$\overline{1} 1 0$</td>
<td>8</td>
<td>$0.0575$</td>
</tr>
</tbody>
</table>

Figures 3 and 4 also show the effect of considering a smaller number of lattice sites. If only the central cell is considered, that is, if we include only the Wannier functions associated with the two missing atoms, we obtain the $E(\lambda)$ curves labeled "central cell only." The bound state appears near $\lambda=1.35$ for $\Gamma_{2}'$ and 1.6 for $\Gamma_{1}$. When the second site group of six cells is included, the curves labeled "two site groups" are obtained. These have bound states which are already present in the case $\lambda=1.0$ and are, in this respect, probably in better agreement with experiment than are our final results. It is also quite interesting that, in this approximation, the energy separation between $\Gamma_{1}$ and $\Gamma_{2}'$ states is reasonable small (less than 0.15 eV) and actually changes sign. When the third site group is included both curves shift to larger $\lambda$, but $\Gamma_{1}$ is affected rather more than is $\Gamma_{2}'$. The difference appears to result mainly from the somewhat anomalous contribution from band 4.

![](./images/813231707443429379_3.jpg)

FIG. 3. Energy of the localized state of symmetry $\Gamma_{1}$ in various approximations: (A) All contributing bands, two site groups only;(B) three site groups, all conduction bands removed: (C) three site groups, all bands (same as in Fig. 2); (D) central cell only with all contributing bands; (E) band 1 removed (use upper scale for $\lambda$.

![](./images/813231707443429379_4.jpg)

FIG. 4. Energy of the localized state of symmetry $\Gamma_{2}'$ in various approximations: (A) three site groups, all conduction bands removed; (B) two site groups, all contributing bands; (C) three site groups, all bands (same as in Fig. 2); (D) central cell only, all contributing bands; (E) band 2 removed (use upper scale for $\lambda$).

It is rather difficult to assess the general convergence of our expansion in a reliable way since, at present, we are unable to include either more bands or more lattice sites. However, it would appear both from the form of the eigenvector and from the behavior of $E(\lambda)$ that $\Gamma_{2}'$ is reasonably stable. The convergence of $\Gamma_{1}$ appears to be rather poorer as far as lattice sites are concerned. The wave function appears to spread out more in the Wannier representation. In both cases, it appears unlikely that addition of higher conduction bands will have a significant effect. As the wave functions spread out more in $k$ space, which is the tendency observed for the higher bands, the matrix elements of the pseudopotential tend to become small since the pseudopotential is largest near $k=0$. With the pseudopotential method, there are no other valence bands to include.

## V. DISCUSSION AND CONCLUSIONS

The experimental information on the properties of the divacancy which was cited in the Introduction seems to require that it is possible for the divacancy to exist in four different charge states. Our calculations pertain to only one of these.

We have proceeded by assuming that the energy levels of the perfect crystal can be calculated from a oneparticle Schrödinger equation containing a potential which is the sum of neutral-atom pseudopotentials. The divacancy is represented by the negative of two neutralatom pseudopotentials, one for each atom missing. The use of neutral pseudopotentials is essential in our approach since we require a short-range interaction. The question "To what charge state of the divacancy do the results refer?" has some subtle aspects. We believe that the most reasonable interpretation is that they pertain to the divacancy in the same charge state as that of the atoms used in constructing the original crystal pseudopotential: the neutral charge state.

On this basis, we should compare our calculated lowest-energy level with that observed experimentally for this state with an energy about 0.25 eV above the valence band. The symmetry of this state is not determined experimentally, so we do not know immediately which of the two curves of Fig. 2 to use in order to determine $\lambda$. It is tempting, however, to suppose that the $1.8 \mu$ infrared absorption band which is associated with the divacancy might correspond to the transition between the $\Gamma_{1}$ and $\Gamma_{2}'$ levels we have calculated. This interpretation would account for the absence of photoconductivity associated with the observed absorption, and is consistent with the observed range of Fermi levels in which the transition is reported. If our interpretation is correct, the lowest level of the neutral divacancy has $\Gamma_{1}$ symmetry in the approximation in which lattice distortion is neglected and we would seem to require $\lambda=1.4$. This choice is also reasonable consistent with our calculations of an excited state at an energy of 0.7 eV above the ground state, which is in good agreement with the observed absorption band. Such good agreement, if it exists, is probably accidental.

The main conclusion that we wish to draw from this calculation is that the method of expansion in Wannier functions works about as well for the divacancy as it did for the single vacancy. While there are many possible reasons concerning the numerical approximations made in this calculation as to why exact agreement with experiment $(\lambda=1.0)$ is not obtained, the slightly larger value of $\lambda$ required in the present case (1.4 as opposed to 1.2) may possibly be attributed to the increased importance of lattice relaxation around the divacancy. We believe that this work, and that previously reported in I, serve to establish our methods as practical procedures for the study of localized states associated with neutral defects in semiconductors.

In summary, we have determined the energies of possible localized electronic states associated with the neutral divacancy in silicon. Two such states of symmetries $\Gamma_{1}$ and $\Gamma_{2}'$ in the approximation in which lattice distortion is neglected, have been found to be possible. A tentative interpretation of the observed $1.8 \mu$ infrared absorption band in irradiated silicon as due to a transition between this state has been proposed.