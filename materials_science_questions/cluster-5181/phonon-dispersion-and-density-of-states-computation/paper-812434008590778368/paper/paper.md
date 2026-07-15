# Cardan's solution for determining the dispersion relations for monatomic crystal lattices

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1990 Eur. J. Phys. 11 372

(http://iopscience.iop.org/0143-0807/11/6/010)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 128.111.121.42
This content was downloaded on 05/09/2015 at 04:00

Please note that [terms and conditions apply].


# Cardan's solution for determining the dispersion relations for monatomic crystal lattices

W C Kok

Department of Physics, Faculty of Science, National University of Singapore, Lower Kent Ridge Road, Singapore 0511, Republic of Singapore

Received 27 July 1989, in final form 5 June 1990

Abstract. It is well known that the phonon dispersion relations for monatomic crystal lattices may be obtained from the dynamical matrix by solving the associated secular equation For general directions of propagation, Cardan's solution may be applied to avoid the use of numerical techniques (for example those for matrix diagonalisation) The present analysis allows a degeneracy parameter $T$ to be defined in simple terms if $T=0$, the transverse branches are degenerate (usually in high symmetry directions), if $T<0$, there are two distinct transverse branches (usually in non-symmetry directions) and $T>0$ corresponds to two non-physical (complex) solutions The analysis shows that only the first two cases will occur in practice (at least for cubic and tetragonal lattices) and that for these cases, the longitudinal modes have higher frequencies than the transverse modes

Resumé. Il est bien connu que les relations de dispersion des phonons pour les treillis cristaux monoatomiques peuvent être obtenues par la matrice dynamique en résolvant l'équation séculaire associée Pour les directions générales de propagation, la solution de Cardan peut être appliquée afin d'éviter l'utilisation des techniques numériques (par exemple ceux pour la diagonalisation matrice) L'analyse présente permet de définir un paramètre $T$ de dégénération en termes simples si $T=0$, les branches transversales sont dégénérées (normalement dans les directions de haute symétrie), si $T<0$, il y a deux branches transversales (normalement en directions non-symétriques) et $T>0$ correspond à deux solutions non-physiques (complexes) L'analyse montre que seul les deux premiers cas se produiront en pratique (au moins pour les treillis cubiques et tétragonaux) et que dans ces cas là, les modes longitudinaux ont de plus hautes fréquence en comparaison avec les modes entretoisés

Most physics courses devote some discussion to phonon dispersion relations, one of the standard topics covered in undergraduate solid state physics In one dimension, the dispersion relations are easily derived analytically, while in two and three dimen- sions, solutions of quadratic and cubic equations are required In the symmetry directions such as the [100], [110] and [111] directions in cubic crystals, it is well known that the corresponding dispersion relations are easily obtained Although different presentations of dispersion relations exist in several adopted texts, there is not much mention in the literature of the dispersion relations for arbitrary directions in three dimensions We suggest here that the application of Cardan's solution for cubic equations provides a use- ful tool for determining the dispersion relations in the case of arbitrary directions of propagation It is then a simple matter even for the student with limited computing ability or resources to plot the correspond- ing dispersion curves without the use of advanced numerical techniques The student can immediately appreciate that the high-symmetry directions such as [100] in cubic crystals are characterised by one longi- tudinal mode and two transverse (usually degenerate) modes while in non-symmetry directions, this degen- eracy is lost and there are three distinct branches For students who intend to do further calculations and evaluate the phonon density of states, the dispersion relations in non-symmetry directions are required although the symmetry directions are most important because of their great influence on the critical points The derivation of Cardan's solution is given here for the interested reader

Our derivation of the dispersion relations is based on the dynamical matrix as a starting point In this connection, G J Keeler [1] has written an article on undergraduate physics programs for the calculation of phonon dispersion relations of crystal lattices and density of states Ashcroft and Mermin [2] have shown that the dynamical matrix in crystals is real and sym-

Cardan's solution for determining the dispersion relations for monatomic crystal lattices

metric, in monatomic latices, this takes the form

$$
D(k)=\left[\begin{array}{lll}
A & E & F \\
E & B & G \\
F & G & C
\end{array}\right] \tag{1}
$$

where the matrix elements depend on the wave vector components $k_{x}, k_{1}$, and $k_{z}$ and the interatomic force constants For a plane wave described by $u_{\alpha(k)}=$ $A_{\alpha} \exp \left[\mathrm{i}\left(\omega t-k \cdot r_{l}\right)\right]$, where $r_{l}$ denotes the $l$ th atom, the dispersion relations are obtained by solving the eigenvalue problem

$$
\omega^{2} B=D B \tag{2}
$$

where

$$
B_{\alpha}=m^{1 / 2} A_{\alpha}
$$

in the notation of [1] The eigenvalues $\omega^{2}$ are obtained from the secular equation

$$
\operatorname{det}\left(D-\omega^{2} I\right)=0 \tag{3}
$$

which gives a cubic equation in $\omega^{2}$ For symmetry directions of propagation, the secular determinant in (3) is factorisable and analytical expressions for $\omega^{2}$ can be readily obtained For general directions of propagation, $\omega^{2}$ can be obtained by applying Cardan's solution [3] for cubic equations This does not require any iterative technique for the diagonalisation of matrices or for the solution of cubic equations and a simple computer program can be written for it

Equation (3) belongs to the class of cubic equations

$$
x^{3}+P x^{2}+Q x+R=0 \tag{4}
$$

where

$$
\begin{aligned}
& P=-(A+B+C) \\
& Q=A B+B C+C A-E^{2}-F^{2}-G^{2} \\
& R=-A B C-2 E F G+A G^{2}+B F^{2}+C E^{2}
\end{aligned}
$$

The substitution $x^{\prime}=x+\frac{1}{3} P$ enables (4) to be written in the form

$$
\left(x^{\prime}\right)^{3}+p x^{\prime}+q=0 \tag{5}
$$

where the coefficient of the $(x')^{2}$ term is now zero Then

$$
\begin{aligned}
& p=Q-\frac{1}{3} P^{2} \tag{6} \\
& q=\frac{2}{27}(P)^{3}-\frac{1}{3} P Q+R \tag{7}
\end{aligned}
$$

A further substitution $x^{\prime}=y+z$ results in (5) being transformed into

$$
y^{3}+z^{3}+(3 y z+p) x^{\prime}+q=0
$$

$y$ and $z$ can be chosen such that $3 y z+p=0$, which can be rewritten as $y^{3} z^{3}=-\frac{1}{27} p^{3}$, and on substitution the above equation $y^{3}+z^{3}=-q$ So $y^{3}$ and $z^{3}$ are roots of the quadratic equation

$$
t^{2}+q t-\frac{1}{27} p^{3}=0
$$

Hence from $x'=y+z$,

$$
\begin{aligned}
x^{\prime}= & {\left[-\frac{1}{2} q+\left(\frac{1}{4} q^{2}+\frac{1}{27} p^{3}\right)^{1 / 2}\right]^{1 / 3} } \\
& +\left[-\frac{1}{2} q^{2}-\left(\frac{1}{4} q^{2}+\frac{1}{27} p^{3}\right)^{1 / 2}\right]^{1 / 3}
\end{aligned} \tag{8}
$$

This is Cardan's solution from which the dispersion relations can be obtained using $\omega^{2}=x^{\prime}-\frac{1}{3} P$ One obtains the following roots to the cubic equation (5) depending on the value of $T=\frac{1}{4} q^{2}+\frac{1}{27} p^{3}$, the expression within the square root in (8)

(1) If $T>0$, this is the case of one real root and two complex roots To see this, we note that $y^{3}$ and $z^{3}$ are both real, denoting the real and two complex cube roots of unity by $1, w$ and $w^{2}$ respectively, the roots from (8) are then $y+z$ (real), $w y+w^{2} z$ (complex) and $w^{2} y+w z$ (complex)

(11) If $T<0$, there are three real roots Here, $y^{3}$ and $z^{3}$ are both complex of the form

$$
y^{3}=a+1 b \quad z^{3}=a-1 b
$$

where $a=-\frac{1}{2} q$ and $b=\sqrt{-T}$ Writing $(a+1 b)^{1 / 3}=$ $[r(\cos \theta+1 \sin \theta)]^{1 / 3}$, with $r=\left(a^{2}+b^{2}\right)^{1 / 2}$ and $\theta=$ $\tan ^{-1}(b / a)$ and applying de Moivre's theorem, the three cube roots are $r^{1 / 3}(\cos \theta / 3+1 \sin \theta / 3), r^{1 / 3}(\cos (\theta+2 \pi) / 3$ $+1 \sin (\theta+2 \pi) / 3)$ and $r^{1 / 3}(\cos (\theta+4 \pi) / 3+1 \sin$ $(\theta+4 \pi) / 3)$ Hence, from (8), $x'$ for practical purposes can be written as

$$
\begin{gathered}
2 r^{1 / 3} \cos \theta / 3 \quad 2 r^{1 / 3} \cos (\theta+2 \pi) / 3 \\
2 r^{1 / 3} \cos (\theta+4 \pi) / 3
\end{gathered}
$$

This implies that the first solution representing the quasi-longitudinal mode has a higher frequency than the other two solutions for the quasi-shear or 'trans- verse' [2] modes since $x^{\prime}<0$ and $-\frac{1}{3} P>0$ This is to be expected physically as the elastic constants are normally higher for compression than for shear, for example, in cubic crystals, the effective elastic con- stants for longitudinal and transverse modes are $C_{11}$ and $C_{44}(<C_{11})$ respectively in the [100] direction, $\frac{1}{3}(C_{11}+2 C_{12}+4 C_{44})$ and $\frac{1}{3}(C_{11}-C_{12}+C_{44})$ respec tively in the [111] direction

(111) If $T=0$, all the roots are real, two of them being equal Here, $y^{3}=z^{3}$ so $y=z$ and the roots from (8) become $2 y, y(w+w^{2}), y(w+w^{2})$ or $2 y,-y,-y$ These can also be obtained from the solutions in part(11) by setting $\theta=0$ (since $T=0$) Again, the longi tudinal modes have higher frequencies, in addition, the longitudinal frequencies are higher for $T$ slightly less than zero than for $T=0$ at the same wave vectors since the main variation comes from the $r$ term rather than the cosine variation for $\theta$ close to zero

We see that for $T=0$, there are only two distinct roots, one corresponding to the longitudinal branch, the other to the two transverse branches which are degenerate This occurs in certain high-symmetry direc- tions such as [100] in BCC (see figure 1) or FCC lattices -to verify $T=0$ for these cases, set $B=C \neq A$ and $E=F=G=0$ Knowing the form of the dynamical matrix $D(k)$, we can express $T$ in terms of the matrix elements and one can further show by setting to zero

![](./images/812434008590778368_1.jpg)

Figure 1. Dispersion curves for the [100] symmetry direction of a BCC crystal showing a longitudinal (L) branch and degenerate transverse (T) branches

![](./images/812434008590778368_2.jpg)

Figure 2 Dispersion curves for a slightly off-symmetry direction [1,01,02] of a BCC crystal to show a longitudinal (L) branch and two distinct transverse (T) branches These are calculated using Cardan's solution

the first partial derivatives of $T$ with respect to $k_{1}, k_{1}$, $k_{z}$ that the maximum value of $T$ is zero We have shown this for cubic and tetragonal lattices The fact that $T$ cannot be greater than zero means that there is no incidence of complex roots occurring and such unphysical solutions for $T>0$ will not occur in practice So for general directions of propagation, $T<0$, the case of three real distinct roots (see the appendix) corresponding to a 'longitudinal' wave and two'transverse' waves with no degeneracy (see figure 2) In a related context, experimental measurements [4] of sets of three velocities of ultrasonic waves correspond-ing to each selected (not necessarily high-symmetry) direction of propagation in tetragonal crystals have been made to determine the elastic constants [5]

In the computations in figures 1 and 2, the matrix elements of $D$ are drawn from the example of body centred cubic lattices, where, taking into account only first and second neighbour interactions [1],

$$A=\delta-\frac{3}{4} R c_{2 x}$$

$$B=\delta-\frac{3}{4} R c_{2},$$

$$C=\delta-\frac{3}{4} R c_{2 z}$$

$$E=s_{1} s_{1} c_{z}$$

$$F=s_{\mathrm{x}} c_{1} s_{z}$$

$$G=c_{\mathrm{x}} s_{1} s_{z}$$

where $A-G$ are all expressed in units of $8 \sigma / 3 m$, with $c_{x}=\cos k_{x} a, s_{x}=\sin k_{x} a, c_{2 x}=\cos 2 k_{x} a$, etc and $\delta=1+\frac{3}{4} R-c_{x} c_{y} c_{z}$ The cell dimension is $2 a$ and the first and second neighbour force constants are $\sigma$ and $R \sigma=08 \sigma$ respectively The analytical solutions for the [100] direction are $\omega_{longit }=\sqrt{D_{11}}, \omega_{trans }=\sqrt{D_{22}}$ The dispersion curves in the two figures show that for small wave vectors, $\omega$ varies linearly with wave vector for each mode, the slope being a measure of the velocity of sound, as is well known For wave vectors very close to zero, $A \simeq B \simeq C, E \simeq F \simeq G \simeq 0$, so $T \simeq 0$ and the transverse branches almost overlap even for arbitrary directions of propagation, an example of which is given in figure 2

## Acknowledgments
The author would like to thank the referees for their constructive suggestions Thanks are due also to Mr C M Ngin for writing the computer program and Ms T J Pang for assistance

## Appendix
We show that the roots $\omega^{2}$ of
$$x^{3}+P x^{2}+Q x+R=0$$

which is equation (4) are real if

$$
T=\frac{1}{4} q^{2}+\frac{1}{27} p^{3} \leqslant 0 \tag{A 1}
$$

$T \leqslant 0$ means that $-\frac{1}{27} p^{3} \geqslant \frac{1}{4} q^{2}$

Substituting for $p$ and $q$ from (6) and (7), (A 1) can be rewritten as

$$
\Gamma^{2}+2(2-9 \gamma) \Gamma-27 \gamma^{2}(1-4 \gamma) \leqslant 0
$$

where

$$
\gamma=Q / P^{2}
$$

and

$$
\Gamma=27 R / P^{3}
$$

For example, the high-symmetry [100] direction in BCC lattices corresponds to the degenerate case $T=0$ with

$$
P=-A-2 B<0
$$

$$
R=-A B<0
$$

since $A, B=C$ are all positive. Here the sum of roots $(\Gamma_{1}+\Gamma_{2})$ is positive, therefore

$$
2(9 \gamma-2)>0 \quad \text { or } \quad \gamma>\frac{2}{9} \tag{A 2}
$$

Similarly,

$$
\text { product of roots }=\Gamma_{1} \Gamma_{2}=27 \gamma^{2}(4 \gamma-1)>0
$$

$$
\text { or } \quad \gamma>\frac{1}{4} \tag{A 3}
$$

To satisfy (A 2) and (A 3) simultaneously,

$$
\gamma>\frac{1}{4} \quad \text { for } \quad T \leqslant 0 \tag{A 4}
$$

From (A 1) above, $T \leqslant 0$ implies that

$$
p=Q-\frac{1}{3} P^{2} \leqslant 0 \quad \text { i.e } \quad \gamma \leqslant \frac{1}{3} \tag{A 5}
$$

(a) The degenerate case $T=0$ so $b=0$ and $\cos [(\theta+2 \pi) / 3]=\cos [(\theta+4 \pi) / 3]=-\frac{1}{2}$. Then

$$
\omega^{2}=-\left|-\frac{1}{2} q\right|^{1 / 3}+\frac{1}{3}|P|=-\left|\frac{1}{3} p\right|^{1 / 2}+\frac{1}{3}|P|
$$

using (A 1)

$$
=-\left(-\frac{1}{3} Q+\frac{1}{9} P^{2}\right)^{1 / 2}+\frac{1}{3}|P| \tag{A 6}
$$

For the [100] direction in BCC crystals,

$$
Q=A B+2 B C>0
$$

The size of the negative term in (A 6) consists of two terms of opposite signs, this means that

$$
\left(-\frac{1}{3} Q+\frac{1}{9} P^{2}\right)^{1 / 2}<\frac{1}{3}|P|
$$

Hence the RHS of (A 6) is positive

(b) The non-degenerate case. The longitudinal frequencies are higher than the transverse frequencies, which have a minimum value

$$
\begin{aligned}
\omega_{\min }^{2} & =-2\left(-\frac{1}{3} Q+\frac{1}{9} P^{2}\right)^{1 / 2}+\frac{1}{3}|P| \\
& =-2|P|\left(-\frac{1}{3} \gamma+\frac{1}{9}\right)^{1 / 2}+\frac{1}{3}|P|
\end{aligned}
$$

This is positive since $\frac{1}{4}<\gamma<\frac{1}{3}$ from (A 4) and (A 5)

## References

[1] Keeler G J 1980 *Physics Programs* ed A D Boardman (New York: Wiley)

[2] Ashcroft N W and Mermin N D 1976 *Solid State Physics* (New York: Holt, Rinehart and Winston)

[3] Hall H S and Knight S R 1946 *Higher Algebra* (London: Macmillan)

[4] Alton W J and Barlow A J 1967 *J. Appl. Phys.* **38** 3817

[5] Lee W Y and Kok W C 1989 *Solid State Commun.* **70** 459