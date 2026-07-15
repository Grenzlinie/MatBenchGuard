# Simple models of unusual elastic properties

K. W. Wojciechowski

Institute of Molecular Physics, Polish Academy of Sciences, Smoluchowskiego 17/19, 60-179 Poznań, Poland

**Abstract.** Elastic properties of a class of two-dimensional model systems, consisted of hard cyclic multimers, are discussed. Each multimer is composed of $m=3k$ (where $k$ is a positive integer) hard discs of diameter $\sigma$ and centers forming a perfect polygon of $m$-sides, where the side length is $l$. Close packed structures of such systems, which are isotropic from the point of view of elastic properties, were solved exactly in the close packing limit at zero temperature. It was shown that the Poisson ratio, $v_{P}$, of the multimers is negative when their roughness parameter, defined as $\alpha\equiv l/(2\sigma)$, is large. In the limit $m\rightarrow\infty$ one obtains hard disc-like particles, which in contrast to the standard hard discs are *rough*. It is conjectured that the formula obtained for the Poisson ratio of the $3k$-multimers, $v_{P}=(1-2\alpha^{2})/(3-2\alpha^{2})$, is valid also for $m\neq3k$ in the limit $m\rightarrow\infty$.

## INTRODUCTION

A system of negative Poisson ratio [1] (NPR) increases its transverse dimensions when expanded longitudinally. This is in contrast to common systems which decrease the transverse dimensions at such a deformation [1], see Fig.1. This unusual property is not only of interest from the point of view of fundamental research but it is also useful for various practical applications. Hence, since manufacturing NPR structures by Lakes [2] and Evans [3], an increasing research activity is observed in this field [4,5].

![](./images/812347498805854208_1.jpg)

**FIGURE 1.** Deformation accompanying stretching of a sample of (a) a common material showing positive Poisson ratio and (b) a sample of material exhibiting negative Poisson ratio.

Structures on macro-, mezo- and microscopic level have been found which exhibit $v_{P}<0$. The structures on the microscopic level are of particular interest. One of the possibilities to obtain such structures is by using molecules which can form NPR *phases*. The first step in this direction can be done by constructing various model particles of such a property. To simplify the analysis it is meaningful to start with two-dimensional models.

Analysis of various molecules indicates that one of the crucial molecular parameters characterizing the Poisson ratio is the molecular *shape* [6]. The simplest interactions which can characterize the molecular shape are the hard-body interactions, infinite when the bodies overlap and zero otherwise. The hard-body systems have been used to model various structures of real matter and phenomena occurring in them, see e.g. [7,8] and references therein. Being athermal, the hard-body systems are convenient reference systems for fluids, liquid crystals and plastic crystals. As the hard potential is non-analytic they also constitute demanding test models for various theoretical approximations and simulation methods. In the present note a class of two-dimensional particles, interacting through the hard potential is considered in the aspect of searching for systems of negative Poisson ratio.

## HARD CYCLIC MULTIMERS IN TWO DIMENSIONS

The examples of even and odd cyclic multimers, respectively consisting of $m=9,12$ hard discs, are shown in Fig.2. The disc centers are assumed to form perfect polygons which are rigid (i.e cannot change their shape); the internal stability of the multimers is not discussed in this work.

It can be rigorously proven that, when $m=3k$ and the positive integers $k$ are even, the multimer centers form the triangular lattice at close packing [6]. Computer simulations indicate [9] that the triangular lattice of the multimer centers corresponds also to the close packed structure of the multimers when $k$ is any odd integer. Thus, when $m=3k$, the close packed structures of the cyclic multimers must show the 3-fold symmetry axis,

---

CP708, *Slow Dynamics in Complex Systems: 3rd International Symposium*, edited by M. Tokuyama and I. Oppenheim
© 2004 American Institute of Physics 0-7354-0183-7/04/$22.00

![](./images/812347498805854208_2.jpg)

FIGURE 2. Geometry of the hard cyclic multimers for (a)
$k=3$ and (b) $k=4$. In both cases the roughness parameter $\alpha$ is
equal to 1/2. It is worth to note that the multimer (a) and other
multimers with odd $k$ do not show the center of symmetry. This
is in contrast to the multimer (b) and other multimers of even $k$
which show such a symmetry.

see Fig.3.

The 3-fold symmetry axis implies that for small de-
formations the elastic properties of the system do not
depend on the direction [10], i.e. the system is elasti-
cally isotropic. As the system is isotropic, one needs only
two elastic constants (and pressure) to describe its elastic
properties [1]. This can be seen by expanding the sys-
tem elastic energy per unit volume in powers of the (La-
grange) strain components $\varepsilon_{ij}$

$$
\begin{aligned}
E_{elast}/V_{ref} & =-p\left(\varepsilon_{xx}+\varepsilon_{yy}\right)+2\lambda_{\xi\eta\xi\eta}\left(\varepsilon_{xx}+\varepsilon_{yy}\right)^{2} \\
& +\lambda_{\xi\xi\eta\eta}\left[\left(\varepsilon_{xx}-\varepsilon_{yy}\right)^{2}+4\varepsilon_{xy}^{2}\right], \quad (1)
\end{aligned}
$$

where $V_{ref}$ is the two-dimensional 'volume' (area) of the
reference state corresponding to the equilibrium state at
the pressure $p$; the linear terms in the strain components
come from the fact that the pressure can be different
from zero, in general. The bulk modulus, $B$, and the
shear modulus, $\mu$, are related to the above defined elastic
constants as follows [11]

$$
B=4\lambda_{\xi\eta\xi\eta},\ \mu=2\lambda_{\xi\xi\eta\eta}-p.\qquad(2)
$$

As the stability of the system requires positive values
of the bulk modulus and the shear modulus [1]

$$
B>0, \mu>0,\qquad(3)
$$

the Poisson ratio $v_{P}$ must fulfill the relation [12]

$$
-1 \leq v_{P} \equiv \frac{B-\mu}{B+\mu} \leq 1.\qquad(4)
$$

The simplest way to determine the elastic properties
of the static structures of the hard cyclic multimers is to
replace the (non-analytic) hard potential through which
the hard discs of different multimers interact, $u(r>\sigma)=$
$0,u(r<\sigma)=\infty$, by the limit of an analytic, $n$-inverse
power interactions between the disc centers

$$
u(r)=\lim _{n \rightarrow \infty}\left(\frac{\sigma}{r}\right)^{n}.\qquad(5)
$$

Within this approach one can restrict the interactions
to the nearest neighboring discs of different multimers
only

$$
E_{t o t} \equiv E_{e l a s t}+E_{r e f}=\sum_{1 \leq i<j \leq N} \sum_{k, l=n. n.} u\left(r_{k_{i} l_{j}}\right), \quad (6)
$$

where $N \to \infty$ is the number of the multimers in the
system, $E_{ref}$ is the energy of the reference state, and the
second summation on the right hand side concerns only
the nearest-neighboring atoms $k_{i}, l_{j}$ of the neighboring
molecules $i,j$ which are taken into account in the first
summation.

The pressure, the bulk modulus and the shear modulus
can be determined by differentiating the total energy per
unit volume $E_{tot}/V_{ref}$ with respect to the components of
the strain tensor. Differentiation with respect to $\varepsilon_{xx}$ (or
$\varepsilon_{yy}$) at the reference state, gives the pressure

$$
p=-\left.\frac{1}{v_{r e f}} \frac{\partial E}{\partial \varepsilon_{x x}}\right|_{\varepsilon=0},\qquad(7)
$$

where $\varepsilon=0$ indicates that after the differentiation all the
strain tensor components should be replaced by zero.

By double differentiation of the energy one obtains the
elastic constants:

$$
\left.\frac{1}{v_{r e f}} \frac{\partial^{2} E}{\partial \varepsilon_{x x}^{2}}\right|_{\varepsilon=0}=4 \lambda_{\xi \eta \xi \eta}+2 \lambda_{\xi \xi \eta \eta}, \quad (8)
$$

$$
\left.\frac{1}{v_{r e f}} \frac{\partial^{2} E}{\partial \varepsilon_{x x} \partial \varepsilon_{y y}}\right|_{\varepsilon=0}=4 \lambda_{\xi \eta \xi \eta}-2 \lambda_{\xi \xi \eta \eta}. \quad (9)
$$

Combining (2), (4) with (7)-(9) one gets the Poisson
ratio for the systems with even and odd $k$. The obtained
dependences show that the Poisson ratio is negative when
the roughness parameter, $\alpha=l/(2\sigma)$, is large [6].

Taking the limits $n,m \to \infty$ and using the definition
of the roughness parameter one obtains the same depen-
dence in both the cases considered above

$$
v_{P}=\frac{1-2 \alpha^{2}}{3-2 \alpha^{2}}.\qquad(10)
$$

The obtained Poisson ratio dependence on the roughness
parameter is shown in Fig. 4.

It can be seen that when the roughness parameter is
zero the Poisson ratio is equal to 1/3 which is the value
of the Poisson ratio of the static (i. e. zero temperature),
close packed structure of hard discs. It can be also seen
that the Poisson ratio decreases with increasing $\alpha$, and
for $\alpha>2^{-1/2}$ the Poisson ratio is negative, reaching its
minimum value -1 at the stability limit when $\alpha=1$.

## ROUGH DISC SYSTEM

In the above considerations the multimers which were
constituted of $m=3k+1 \equiv m^{(1)}$ and $m=3k+2 \equiv m^{(2)}$

![](./images/812347498805854208_3.jpg)

FIGURE 3. Geometry of the close packed structures of the hard cyclic multimers shown in Fig.1. It is worth to note that the structure shown in (a) exhibits the mirror symmetry with respect to the crystalline axes; the same is true for each structure with odd $k$ . This is in contrast to structures formed by multimers with even $k$ , including the structure illustrated in (b), which do not show such a symmetry, i.e. they are chiral.

![](./images/812347498805854208_4.jpg)

FIGURE 4. The Poisson ratio $v_{P}$ of the close packed rough disc system as the function of the roughness parameter $\alpha$ .

hard discs have not been taken into account. The rea- son is that the structure of close packed configurations formed by such multimers is not known and these struc- tures are not elastically isotropic for finite $m$ , in general(see e.g. the heptamers considered in the reference [8]). In the limit of $m \to \infty$ the multimer shape tends to the hard disc shape. In contrast to the standard hard discs, which are smooth, the limiting particles are rough. As the ratio of the thickness of the rough surface to the rough disc diameter tends to zero, the structure of their centers at close packing must tend to the triangular lattice.

We conjecture that the formula (10), which has been proved above for $m=3 k$ , is valid also for static struc tures with $m^{(i)} \to \infty$ , where $i=1,2$ . In other words, we conjecture that the Poisson ratio of close packed struc- ture of rough discs at the zero temperature depends on the roughness parameter in the way given by (10).

# SIMULATIONS IN THE GENERALIZED CONSTANT PRESSURE ENSEMBLE

No analytic methods are known to the present Author which allow one to study quantitatively the elastic pro- perties of the defined above hard cyclic multimers at po- sitive temperatures. These systems can be studied, how- ever, by computer simulations. One might add here that determination of the elastic properties of hard-body sys- tems is not a trivial task, in general. There are several reasons why it is so. (a) No zero-temperature harmonic approximation can be used for systems of hard bodies be- low close packing density. (b) Microscopic formulae for the elastic constants in the constant strain ensembles in- clude second derivatives of the hard-body interaction po- tential which are difficult to compute. (c) Standard com- putations in the constant stress (or thermodynamic ten- sion) ensembles require precise knowledge of the equi- librium state which is used as the reference state in the strain-fluctuation methods. When the symmetry of the structure is not known, determination of the latter state can be, however, almost as time consuming as the com- putation of the elastic constants itself.

The mentioned difficulties can be overcome within the Parrinello-Rahman (variable-shape-box) genera- lization [13, 14] of the constant pressure ensemble(NpT) [15]. Computations performed in that ensemble do neither require any harmonic approximation nor microscopic formula for the elastic constants. Moreover,

the reference state can be determined during the same run in which the elastic properties of the system are simulated [16, 8]. Although the NpT method is rather slowly convergent [8,17-19], it has been shown that for hard spheres [18] and hard discs [19] it gives results which are in a good agreement with those obtained by other, more elaborate methods.

Simplicity of the NpT method encouraged us to study elastic properties of the hard multimer systems. The si- mulations have proven the existence of thermodynami- cally stable *phases* that exhibit negative Poisson ratio. Rough molecules have been found for which such phases exist in the whole stability range of the solid, from the close packing up to melting. The results of the simula- tions will be published elsewhere [9].

# CONCLUSIONS

The hard cyclic multimer system discussed in this pa- per shows that very simple molecular interactions can be used to model rather unusual effects like negative Pois- son ratio. The hard cyclic multimer model not only in- creases the amount of known mechanisms [2-5,10-12,20-26] which can lead to $v_{P}<0$ but also offers very simple microscopic examples of chiral and non-chiral structures which properties can be studied by generalizations of the elasticity theory which include the orientational degrees of freedom of the elastic medium [27-29].

In the limit of infinitely many atoms forming the hard cyclic multimers, the latter molecules can be thought of as the rough discs. The analysis presented in this paper indicates that the Poisson ratio of static structures of the rough discs can be uniquely characterized by the roughness parameter.

Computer simulations performed for the hard cyclic multimers prove that it is possible to construct very sim- ple model molecules which form thermodynamically sta- ble solid phases exhibiting the negative Poisson ratio in a broad range of the thermodynamic parameters [9].

In three dimensions, analogous considerations can be done for globular multimers, leading to the notion of rough spheres. This will be the subject of separate works.

# ACKNOWLEDGMENTS

The Author thanks Dr. A. Alderson for careful reading of the manuscript. Part of this work was performed at the Poznań Computer and Networking Center (PCSS) in the framework of the Polish Committee for Scien- tific Research grant 4T11F 010 23. This work was also partially supported by the Centre of Excellence "Mag- netic and Molecular Materials for Future Electronics" within the European Commission contract No. G5MA- CT-2002-04049.

# REFERENCES

1. Landau, L. D., Lifshits, E. M., Kosevich, A. M., and Pitaevskii, I. P., *Theory of Elasticity*, Pergamon Press, London, 1986 pp. 1-37.
2. Lakes, R., *Science* **235**, 1038-1040 (1987).
3. Caddock, B. D., and Evans, K. E., J. Phys. D: Appl Phys. **22**, 1877-1882 (1989).
4. Lakes R., Advanced Materials **5**, 293-296 (1993).
5. Evans, K. E., and Alderson, A., Advanced Materials **12**, 617-628 (2000).
6. Wojciechowski, K. W., unpublished.
7. Allen, M. P., Evans, G. T., Frenkel, D., and B. M. Mulder, Adv. Chem. Phys. LXXXVI, 1-166 (1993).
8. Wojciechowski, K. W., Tretiakov, K. V., and Kowalik, M., Phys. Rev. **E67**, 036121 1-14 (2003).
9. Wojciechowski, K. W., and Tretiakov, K. V., unpublished.
10. Wojciechowski, K. W., J. Phys. Soc. Japan **76** 1819-1820 (2003).
11. Wojciechowski, K. W., J. Phys. A: Math. Gen. **36**, 11765-11778 (2003).
12. Wojciechowski, K. W., *Phys. Lett.* **A137**, 60-64 (1989).
13. Parrinello, M., and Rahman, A., J. Appl. Phys. **52**, 7182-7190 (1981).
14. Parrinello, M., and Rahman, A., J. Chem. Phys. **?76**, 2662-2668 (1982).
15. Wojciechowski, K. W., and Tretiakov, K. V., Computer Phys. Commun. **121-122**, 528-530 (1999).
16. Wojciechowski, K. W., *Computational Methods in Science and Technology* **8**, 77-83 (2002).
17. Tretiakov, K. V., and Wojciechowski, K. W., J. Phys.: Cond. Matter **14**, 1261-1273 (2002).
18. Wojciechowski, K. W., and Tretiakov, K. V., *Computational Methods in Science and Technology* **8**, 84-92 (2002).
19. Wojciechowski, K. W., Tretiakov, K. V., Brańka, A. C., and Kowalik, M., J. Chem. Phys. **119**, 939-946 (2003).
20. Almgren, R. F., J. Elasticity **15**, 427-430 (1985).
21. Kolpakov, A. G., Prikl. Matem. Mekh., **49**, 969-977 (1985).
22. Milton, G. W., J. Mech. Phys. Solids, **40**, 1105-1137 (1992).
23. Wojciechowski, K. W., *Mol. Phys. Reports* **10**, 129-136 (1995).
24. Novikov, V. V., and Wojciechowski, K. W., *Phys. Solid State* **41**, 1970-1975 (1999).
25. Grima, J. N., and Evans, K. E., *Journal of Material Science Letters* **19**, 1563-1565 (2000).
26. Ishibashi, Y., and Iwata, M., J. Phys. Soc. Jpn. **69**, 2702-2703, (2000).
27. Eringen, E. A. C., *Polar and Nonlocal Field Theories, vol. IV of Continuum Physics*, Academic Press, New York, 1976.
28. Vasiliev, A. A., and Dmitriev, S. V., and Ishibashi, Y., and Shigenari, T., *Phys. Rev.* **B65**, 094101 1-7 (2002).
29. Dmitriev, S.V., Vasiliev, A.A., Miroshnichenko, A.E., Shigenari, T., Liu, Y., Kagawa, Y., and Ishibashi, Y., arXiv: cond-mat/0209386.

Copyright of AIP Conference Proceedings is the property of American Institute of Physics and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.

Copyright of AIP Conference Proceedings is the property of American Institute of Physics and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.

Copyright of AIP Conference Proceedings is the property of American Institute of Physics and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.