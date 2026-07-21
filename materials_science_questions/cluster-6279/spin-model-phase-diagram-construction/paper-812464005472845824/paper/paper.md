# Global Bethe lattice consideration of the spin-1 Ising model

A Z Akheyan†‡ and N S Ananikian§
International Centre for Theoretical Physics, Trieste, Italy

Received 5 June 1995, in final form 1 November 1995

**Abstract.** The spin-1 Ising model with bilinear and biquadratic exchange interactions and single-ion crystal field is solved on the Bethe lattice using exact recursion equations. The general procedure of investigation of critical properties is discussed and a full set of phase diagrams are constructed for both positive and negative biquadratic couplings. A comparison is made with the results of other approximation schemes.

## 1. Introduction
The spin-1 Ising model with the most general up–down symmetry, known also as a Blume–Emery–Griffiths (BEG) model has recently attracted great attention as a simple model with rich and interesting phase structure. It was originally introduced [1] in order to explain the phase separation and superfluidity in the $^3$He–$^4$He mixtures and later developed to describe other multi-component physical systems, such as metamagnets, liquid crystal mixtures, microemulsions, semiconductors, etc.

The model is defined by the Hamiltonian
$$
-\beta\mathcal{H}=J\sum_{\langle ij\rangle}s_i s_j+K\sum_{\langle ij\rangle}s_i^2 s_j^2-\Delta\sum_i s_i^2
\tag{1}
$$
where $s_i$ takes the values $\pm1$, 0 at each lattice site, $\langle ij\rangle$ denotes a summation over all nearest-neighbour pairs, $J$ and $K$ correspond to the bilinear and biquadratic interaction constants, $\Delta$ is a single-ion crystal field.

The spin-1 Ising model has been solved exactly only on a two-dimensional honeycomb lattice in a subspace of interacting constants $e^K\cosh J=1$ [2–4] (recently, such a solution has been found for higher spin-$S$ models as well [5–7]) but its critical properties for positive $J,K>0$ were well established by different approximation techniques [1,8–10]. The most interesting result here was the first occurrence (in the theoretical model) of the tricritical point, at which the second-order phase transition line ($\lambda$-line) turns to a first-order one.

The picture is practically unchanged for negative bilinear couplings $J<0$. On the bipartite lattice (i.e. the lattice which can be divided into two sublattices $A$ and $B$, such that every site belonging to $A$ is surrounded only by sites belonging to $B$ and vice versa) the region $J<0$ is mapped on the region $J>0$ by redefining the spin directions on one sublattice. As a result we obtain the same phase diagrams, only where the ferromagnetic phase is replaced by the antiferromagnetic one. Hence with no loss of generality we can consider only the case $J>0$.

---
† Theoretical Department, Yerevan Physics Institute, Alikhanian Br. str. 2, 375036, Yerevan, Armenia.
‡ E-mail address: akheyan@vxc.yerphi.am
§ E-mail address: ananikian@vxc.yerphi.am

0305-4470/96/040721+11$19.50 © 1996 IOP Publishing Ltd

On the other hand, the negative values of biquadratic coupling $K$ change the situation drastically. The region $K/J < 0$ is now a subject of intense study. A new staggered quadrupolar phase also called antiquadrupolar was predicted and investigated on the square lattice by means of the mean-field approximation and by Monte Carlo simulations [11]. The direct first-order transition was found from the antiquadrupolar to the ferromagnetic phase, but it was not confirmed by the recent MC [12] and cluster variation method studies. Now it seems that a and f phases are always separated in two dimensions by a disordered phase and they meet only at $T=0$. This direct a $\leftrightarrow$ f transition was, however, established on a three-dimensional cubic lattice [14–16]. The global MFA analysis [14] on this lattice also showed a number of other remarkable features, such as doubly re-entrant behaviour at $0 > K/J > -1$ and a new staggered ferrimagnetic phase which appears between the a and f phases at $K/J < -1$. Latter investigations [16–20] mainly confirmed these results, however, a number of contradictions still remain. This makes further consideration of the model interesting, especially by applying other approximation tools.

In the present paper we consider the solution of the spin-1 Ising model on the Bethe lattice. We review both positive and negative values of biquadratic coupling $K$ and show that, though we reproduce the main details of the phase diagrams obtained by other authors, there are some essential differences, concerning the place and order of phase transitions.

The paper is organized as follows. In section 2 we introduce the model and derive some analytical expressions including the set of exact recursion equations. The procedure of investigation of critical properties based on these equations is described in section 3. Resulting phase diagrams are presented and discussed in section 4. Finally, section 5 is devoted to conclusions.

## 2. Model formulation

The BEG model is characterized by two order parameters, magnetization $m$ and quadrupolar moment $q$:

$$
m=\langle s_{i}\rangle \quad q=\langle s_{i}^{2}\rangle. \tag{2}
$$

However, to account for the possible two-sublattice structure we actually need four order parameters: $m_{A,B}=\langle s_{i}\rangle_{A,B}$ and $q_{A,B}=\langle s_{i}^{2}\rangle_{A,B}$, where $A,B$ denote sublattices. These parameters define the four different phases of the BEG model:

(i) disordered phase (d): $m_A=m_B=0$ $q_A=q_B$
(ii) ferromagnetic phase (f): $m_A=m_B\neq0$ $q_A=q_B$
(iii) antiquadrupolar phase (a): $m_A=m_B=0$ $q_A\neq q_B$
(iv) ferrimagnetic phase (i): $0\neq m_A\neq m_B\neq0$ $q_A\neq q_B$.

The Bethe lattice consideration for any model is based, in some way, on one or more exact recursion equations. We construct these equations in the following way [21]. Taking into account the shell structure of the Bethe lattice one can express the partition function $Z$ of the model on the finite $n$-shell lattice in the form

$$
Z=\sum_{\{s\}}-\beta \mathcal{H}=\sum_{s_{0}} \exp (-\Delta s_{0}^{2})[g_{n}(s_{0})]^{z} \tag{3}
$$

where $z$ is a lattice coordination number, $s_0$ denotes the central spin and $g_n(s_0)$ is a contribution to the partition function of one lattice branch, starting from the central site

![](./images/812464005472845824_1.jpg)

Figure 1. Bethe lattice with coordination number $z=3$.

with fixed spin value $s_0$. The latter is readily connected with $g_{n-1}(s_1)$:

$$
g_{n}(s_{0})=\sum_{s_{1}} \exp (J s_{0} s_{1}+K s_{0}^{2} s_{1}^{2}-\Delta s_{1}^{2})[g_{n-1}(s_{1})]^{z-1}. \tag{4}
$$

Introducing new notations:

$$
x_{n}=\frac{g_{n}(+)}{g_{n}(0)} \quad y_{n}=\frac{g_{n}(-)}{g_{n}(0)} \tag{5}
$$

and summing up over all values of central spin $s_0$ (i.e. $\pm1,0$) we obtain a set of two recursion equations:

$$
x_{n+1}=\varphi(x_{n}, y_{n}) \quad y_{n+1}=\varphi(y_{n}, x_{n})
$$

where

$$
\varphi(u, v)=\frac{\mathrm{e}^{\Delta}+\mathrm{e}^{K}\left(\mathrm{e}^{J} u^{z-1}+\mathrm{e}^{-J} v^{z-1}\right)}{\mathrm{e}^{\Delta}+u^{z-1}+v^{z-1}}. \tag{6}
$$

The values $x$ and $y$ have no direct physical sense, but one can express in terms of $x$ and $y$ all thermodynamic functions of interest. Thus order parameters (2) will be written in the form

$$
m=\frac{x^{z}-y^{z}}{\mathrm{e}^{\Delta}+x^{z}+y^{z}} \tag{7}
$$

$$
q=\frac{x^{z}+y^{z}}{\mathrm{e}^{\Delta}+x^{z}+y^{z}}. \tag{8}
$$

Using equations (3)-(6) we can also write the expression for the free energy:

$$
-\beta f=\frac{1}{N} \ln Z \tag{9}
$$

in the form

$$
-\beta f=\ln \left[1+\mathrm{e}^{-\Delta}\left(x^{z}+y^{z}\right)\right]+\frac{z}{2-z} \ln \left[1+\mathrm{e}^{-\Delta}\left(x^{z-1}+y^{z-1}\right)\right]. \tag{10}
$$

Note that all the above expressions are initially written for the central site of the lattice. We generalize these expressions to other sites, assuming that they are all equivalent. However, this assumption is valid only for the sites lying well inside the lattice. It is not true for a site near the surface, since the surface effects are not negligible on the Bethe lattice even in the thermodynamic limit. If we calculate directly the global free energy of the model on the whole Bethe lattice with free boundary conditions, we shall obtain an expression which is always analytical, and hence shall not observe any critical behaviour.

This is a well known problem arising on the Bethe lattice [23], and if we want to reproduce the results of the real 2D and 3D lattices, we must consider only the local properties of these equivalent 'internal' sites. In this case the free energy is defined by (10) and does exhibit a singular behaviour, as we shall see in the next sections.

## 3. Critical properties investigation

The equations (6) form an iteration sequence $\{x_n, y_n\}$, which in the thermodynamic limit converges to stable fixed points. Via the expressions (7)-(10) these points completely define the possible states of the system. The remarkable points of this approach are that non-staggered phases are described by the single fixed points $\{x_n, y_n\} \to \{x, y\}$, while the staggered phases appear as two-cycle doubled points [22]:

$$
\{x_n, y_n\} \to
\begin{cases}
\{x_A, y_A\} & \text{for odd } n \\
\{x_B, y_B\} & \text{for even } n .
\end{cases}
$$

This property can be explained by the fact that all sites of each individual shell of the Bethe lattice belong to the same sublattice.

Thus, noting from (7) that $m=0$ means $x=y$, we can, in our case, classify the four mentioned phases as follows

| (i) disordered phase (d):      | $x=y$ | single fixed point |
|--------------------------------|-------|--------------------|
| (ii) ferromagnetic phase (f):  | $x \neq y$ | single fixed point |
| (iii) antiquadrupolar phase (a): | $x=y$ | period doubling |
| (iv) ferrimagnetic phase (i):  | $x \neq y$ | period doubling . |

It is possible to obtain the full bifurcation picture, including chaos on some hierarchical lattices [24], but not in the bipartite case (which is the Bethe lattice with nearest-neighbour interactions). We have only first period doubling and it is well known from the theory of iteration processes [25] that all our points of interest (i.e. stable fixed points and two-cycle doubled points) can be found among the solutions of the set of four equations:

$$
\begin{aligned}
\text{(i)} \quad x_A &= \varphi(x_B, y_B, J, K, \Delta) \\
\text{(ii)} \quad y_A &= \varphi(y_B, x_B, J, K, \Delta) \\
\text{(iii)} \quad x_B &= \varphi(x_A, y_A, J, K, \Delta) \\
\text{(iv)} \quad y_B &= \varphi(y_A, x_A, J, K, \Delta) .
\end{aligned} \tag{11}
$$

The physical stable solutions of this set define the pure states of the model. As a matter of fact there is no need to solve (11) in general form. Knowing *a priori* the possible phases of the model we can separate the solutions of (11) concerning the given phase. Thus the disordered phase ($x=y$, $A=B$) can be defined by a single equation, either (i) or (ii). This phase is not degenerate. For the ferromagnetic phase ($x \neq y$, $A=B$) it is enough to consider two equations, namely (i) and (ii), and to exclude the disordered solution. This phase is doubly-degenerate ($m \leftrightarrow -m$) due to the obvious symmetry of these two equations under the ($x \leftrightarrow y$) transformation. The antiquadrupolar phase ($x=y$, $A \neq B$) again can be found from equations (i) and (iii), after excluding the disordered solution. This phase is two-fold degenerate because of the $A \leftrightarrow B$ symmetry. And only for the ferrimagnetic phase do we have to consider all four equations, but they are simplified by excluding previous solutions. The ferrimagnetic phase is four-fold degenerate due to the ($x \leftrightarrow y$) and ($A \leftrightarrow B$) symmetry. Of course, the last two phases are also infinitely degenerate with non-zero residual entropy.

Further procedures can be roughly described by the following steps.

(i) The intersections of the solutions, describing the different phases, give us, generally speaking, the points of second-order transitions.

(ii) The presence of several simultaneous solutions at the given $K$, $J$, $\Delta$ again generally speaking means co-existing phases and a first-order transition, which should be located by matching free energies (10) of these phases.

(iii) The intersections of first- and second-order critical lines give the critical and multicritical points of several types.

In figure 2 we illustrate this procedure on a simple example of the appearance of a tricritical point. The disordered and ferromagnetic solutions of (11) are shown on a crystal field $\Delta$ versus quadrupolar moment $q$ plot for different fixed temperatures $1/zJ$. In the high-temperature region the d and f solutions intersect in their stable parts and this leads to a second-order transition. At low temperature the d line does not meet the stable part of the f line and a first-order transition takes place. A tricritical point is observed in an intermediate situation.

## 4. Phase diagrams

The resulting phase diagrams for the spin-1 Ising model are constructed on the Bethe lattice with coordination number $z = 4$. As is common we plot them as distinct constant $K/J$ cross sections, on a temperature $1/zJ$ versus crystal field $\Delta/zJ$ plot. We obtain eight qualitatively different diagrams in the whole range of parameter space (figure 3).

The $0 > K/J > -1$ counterpart is characterized by the absence of doubled points of the recursion sequence $\{x_n, y_n\}$ and hence represents the non-staggered region of the BEG model with two phases d and f. The first three phase diagrams (figure 3(a)–(c)) are well known from the pioneer work of Blume *et al* [1]. Our results agree quite well with the general picture. The tricritical point does not appear for large positive $K/J$ (figure 3(a)), since the second-order line, limiting the ferromagnetic phase from above, terminates earlier at the critical point $E$ by the first-order line limiting the f phase from the right. The latter line itself terminates at critical point $C$, and in higher-temperature segments two subphases of disordered phase with different densities co-exist. For $K/J$ close to 3 (figure 3(b)) we observe a tricritical point $T$ at which the second-order line ($\lambda$-line) turns to a first-order one and also the triple point $R$, where three different first-order transitions meet. This structure disappears as $K/J$ decreases, and a simple tricritical point is seen (figure 3(c)) for $K/J$ close to 0 (from both positive and negative sides).

A very interesting critical phenomenon, called doubly-re-entrant behaviour, takes place for the values $-0.35 > K/J > -1$ (figure 3(d)). At a fixed crystal field $\Delta/zJ$ the model exhibits the disorder–ferromagnetic–disorder–ferromagnetic sequence of phases as the temperature is lowered. The dependence of order parameters versus temperature is shown for this region in figure 4. The doubly-re-entrant structure shrinks to a zero temperature and at $K/J = -1$ only the second-order line remains, which reaches the $T=0$ axes at a point $\Delta=0$ (figure 3(e)).

Comparing our results with other approximations, we note the following differences. Double re-entrance appears in our model for lower values of $K/J$ and continues until $K/J = -1$, hence we do not observe the internal critical point structure of the ferromagnetic phase. This structure was found by MFA [14] and confirmed by RG studies [18], but it was also not established by CVM [20]. Besides we would like to mention that nowhere in the region $0 > K/J > -1$ do we obtain the single re-entrant part, though it was found by other authors.

![](./images/812464005472845824_2.jpg)

The two-cycle doubled solutions of (11) appear at $K/J < -1$, and this means the emergence of new phases with broken sublattice symmetry.

At $-3 < K/J < -1$ (figure 3(f)) the *antiquadrupolar* phase is separated from the d phase by a second-order line and from the f phase by a first-order one. These two curves meet with the second-order line separating the d and f phases, at bicritical point $B$. The *ferrimagnetic* phase lies in the low-temperature region and is separated by the second-order line from the a phase and by a first-order line from the f phase. These two lines meet with the a-f first-order line at critical end point $E$ and at point $S$. The latter point is located at $T=0, \Delta/zJ=K/J+1$ and describes the macroscopically degenerated ground state with non-zero residual entropy.

As $K/J$ decreases, the point $E$ approaches the point $B$ untill they coincide, at $K/J=-3$, at the point $A$ (figure 3(g)), such that there is no direct transition from the the a to the f phase. Thus $A$ is a new multicritical point at which three second-order lines and

![](./images/812464005472845824_3.jpg)

Figure 3. Phase diagrams of the spin-1 Ising model on the Bethe lattice with coordination number $z=4$ at constant $K/J$ values: (a) 5, (b) 3, (c) $-0.1$, (d) $-0.8$, (e) $-1$, (f) $-2.5$, (g) $-3$, (h) $-3.5$. Disordered d, ferromagnetic f, antiquadrupolar a and ferrimagnetic i phases are present. Broken and full curves indicate, respectively, the first- and second-order transitions and $C, E, R, T, T'S, B, A, M$ indicate the critical and multicritical points of different types (see text). Some fine details are shown in the insets.

one first-order line meet. Note that the first-order i-f transitions are located at a straight vertical line and this locus $K/J=-3$, $\Delta/qJ=-2$ corresponds to a zero-field three-state antiferromagnetic Potts model with Hamiltonian

$$
-\beta \mathcal{H}=-2 J \sum_{\langle i j\rangle} \delta_{s_{i}, s_{j}} \quad J>0. \tag{12}
$$

At $K/J<-3$ the transitions from the i to the f phase in the high-temperature region

![](./images/812464005472845824_4.jpg)

Figure 3. Continued.

![](./images/812464005472845824_5.jpg)

Figure 3. Continued.

become second order (figure 3(h)). As a result the new tricritical point $T'$ arises inside the ordered region. The multicritical point $A$ turns to the tetracritical point $M$, at which four second-order lines meet with different slopes.

Though, in general, the last three diagrams are similar to those obtained by MFA, there is one essential difference: in our approach the transitions from the a to the i phase are of second order (first order in MFA), while the transitions from the i to the f phase are of

![](./images/812464005472845824_6.jpg)

Figure 3. Continued.

first order at least for $K/J \geqslant -3$ (always second order in MFA). This means, in particular,
that we observe another type of ferrimagnetic phase, which co-exists with the f phase and
is caused by instability of the a phase against spontaneous magnetization. Such a phase
was found by CVM [19, 20], but only in the high-temperature region, while it is the only
ferrimagnetic phase present in our consideration. We would also like to mention the very

![](./images/812464005472845824_7.jpg)

narrow region of occurrence of the ferrimagnetic phase.

## 5. Conclusion

Using the exact solution on the Bethe lattice we have constructed the full set of phase diagrams for the spin-1 Ising model for both positive and negative biquadratic coupling $K$. These diagrams feature all recently found properties of the model, including doubly-re-entrant behaviour, staggered quadrupolar and ferrimagnetic phases and a great number of different critical and multicritical points. Thus we can talk about the validity of the Bethe lattice approximation and summarize some advantages of this method. The quantitative comparison of the results has not been our purpose, but the Bethe lattice solution was shown to be more exact than MFA [26, 27]. Besides it is quite easy to use and it provides the analytical expression of all thermodynamic functions of interest, so complete information about the system under the study can be obtained.

As to the mentioned disagreements, especially in the staggered region, they may be caused by dimensionality effects [15]. The Bethe lattice is effectively infinite dimensional, but one can successfully approximate the real lattices in different dimensions by changing the coordination number (this was shown, in particular, in the global consideration of the antiferromagnetic Potts model [28]). We have constructed the phase diagrams for the Bethe lattice with coordination number $z = 4$. We do not consider the simplest case $z = 3$ since it leads to qualitatively different phase diagrams, similar to those which were obtained on two-dimensional lattices (see the introduction). Our preliminary study also shows that phase diagrams change in the case of greater coordination number. This question we are going to clarify in further work.

## Acknowledgments

This work was partly supported by the grant 211-5291YPI of the German Bundesministerium für Forschung und Technologie, ISF supplementary grant and grant INTAS-93-633. We wish

to thank R Flume, K A Oganessyan, N Sh Izmailian and E Sh Mamasakhlisov for help in work and useful discussions. We are also grateful to the International Atomic Energy Agency, UNESCO and personally to Professor S Randjbar-Daemi for hospitality at the International Centre for Theoretical Physics, Trieste, where part of this work was done.

## References

[1] Blume M, Emery V J and Griffiths R B 1971 *Phys. Rev. A* **4** 1071
[2] Horiguchi T 1986 *Phys. Lett.* **113A** 425
[3] Wu F Y 1986 *Phys. Lett.* **116A** 245
[4] Rosengren A and Häggkvist R 1989 *Phys. Rev. Lett.* **63** 660
[5] Lipowski A and Suzuki M 1994 *Physica* **193A** 141
[6] Ananikian N S and Izmailian N Sh 1994 *Phys. Rev. B* **50** 6829–32
[7] Horiguchi T 1995 *Physica* **214A** 452
[8] Mukamel D and Blume M 1974 *Phys. Rev. A* **10** 619
[9] Furman D, Dattagupta S and Griffiths R B 1977 *Phys.Rev. B* **15** 441
[10] Berker A N and Wortis M 1976 *Phys. Rev. B* **14** 4946
[11] Tanaka M and Kawabe T 1985 *J. Phys. Soc. Japan* **54** 2194
[12] Wang Y L, Lee F and Kimel J D 1987 *Phys. Rev. B* **36** 8945
[13] Rosengren A and Lapinskas S 1992 *Phys. Rev. B* **47** 2643–7
[14] Hoston W and Berker A N 1991 *Phys. Rev. Lett.* **67** 1027–30
[15] Hoston W and Berker A N 1991 *J. Appl. Phys.* **70** 6101–3
[16] Kasono K and Ono I 1992 *Z. Phys. B* **88** 205–12, 213–4
[17] Netz R R 1992 *Europhys. Lett.* **17** 373–7
[18] Netz R R and Berker A N 1993 *Phys. Rev. B* **47** 15019–22
[19] Rosengren A and Lapinskas S 1993 *Phys. Rev. Lett.* **71** 165–8
[20] Lapinskas S and Rosengren A 1994 *Phys. Rev. B* **49** 15 190–6
[21] Avakian A R, Ananikian N S and Izmailian N Sh 1990 *Phys. Lett.* **150A** 163–165
Ananikian N S, Avakian A R and Izmailian N Sh 1991 *Physica* **172A** 391–404
[22] Akheyan A Z and Ananikian N S 1994 *Phys. Lett.* **186A** 171–174; 1995 *JETP* **107** 196–208
[23] Baxter R *Exactly Solved Models in Statistical Mechanics* (New York: Academic)
[24] Ananikian N S, Lusiniants R and Oganessyan K A 1995 *JETP Lett.* **61** 482–6
[25] See, for example, Schuster H G 1984 *Deterministic Chaos* (Weinheim: Physik)
[26] Akheyan A Z and Ananikian N S 1992 *J. Phys. A: Math. Gen. A* **25** 3111
[27] Peruggi F, Liberto F di and Monroy G 1983 *J. Phys. A: Math. Gen. A* **16** 811–28
[28] Peruggi F, Liberto F di and Monroy G 1987 *Physica* **141A** 151–86