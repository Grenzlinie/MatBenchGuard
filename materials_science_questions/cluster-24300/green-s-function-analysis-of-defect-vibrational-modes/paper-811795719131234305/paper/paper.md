PHYSICAL REVIEW E 81, 041116 (2010)

# Crumpling transition of the triangular lattice without open edges:
## Effect of a modified folding rule

Yoshihiro Nishiyama (西山由弘)
Department of Physics, Faculty of Science, Okayama University, Okayama 700-8530, Japan
(Received 9 November 2009; published 16 April 2010)

Folding of the triangular lattice in a discrete three-dimensional space is investigated by means of the transfer-matrix method. This model was introduced by Bowick and co-workers as a discretized version of the polymerized membrane in thermal equilibrium. The folding rule (constraint) is incompatible with the periodic-boundary condition, and the simulation has been made under the open-boundary condition. In this paper, we propose a modified constraint, which is compatible with the periodic-boundary condition; technically, the restoration of translational invariance leads to a substantial reduction in the transfer-matrix size. Treating the cluster sizes $L \leq 7$, we analyze the singularities of the crumpling transitions for a wide range of the bending rigidity $K$. We observe a series of crumpling transitions at $K$=0.206(2), -0.32(1), and -0.76(10). At each transition point, we estimate the latent heat as $Q$=0.356(30), 0.08(3), and 0.05(5), respectively.

DOI: 10.1103/PhysRevE.81.041116
PACS number(s): 05.50.+q, 82.45.Mp, 05.10.−a, 46.70.Hg

## I. INTRODUCTION

At sufficiently low temperatures, the polymerized membrane becomes flattened macroscopically [1]; see Refs. [2–4] for a review. (The constituent molecules of the polymerized membrane have a fixed connectivity, and the in-plane strain is subjected to finite shear moduli. This character is contrastive to that of the fluid membrane [5,6], which does not support a shear.) The flat phase is characterized by the long-range orientational order of the surface normals. It is rather peculiar that such a continuous (rotational) symmetry is broken spontaneously for such a two-dimensional manifold. To clarify this issue, a good deal of theoretical analyses has been reported so far. However, it is still unclear whether the transition is critical [7–19] or belongs to a discontinuous one with an appreciable latent heat [20–22]. Actually, in numerical simulations, it is not quite obvious to rule out the possibility of a weak first-order transition [23,24]; see also Ref. [25].

Meanwhile, a discretized version of the polymerized membrane was formulated by Bowick and co-workers [26–28]. To be specific, they considered a sheet of the triangular lattice embedded in a discretized three-dimensional space (face-centered-cubic lattice); see Fig. 9(a). (Even more simplified folding model, the so-called planar folding, was studied in Refs. [29–31]) Owing to the discretization, the folding model admits an Ising-spin representation, for which a variety of techniques, such as the mean-field theory and the transfer-matrix method, are applicable. A peculiarity of this Ising magnet is that the spin variables are subjected to a local constraint (folding rule), which is incompatible with the periodic-boundary condition. Because of this difficulty, the open-boundary condition has been implemented so far [26,28,32,33]. With the full diagonalization method, the finite clusters with the sizes $L \leq 6$ were considered [26,28]. By means of the density-matrix renormalization group (DMRG) [34,35], the clusters with $L \leq 29$ and 26 were treated in Refs. [32,33], respectively. (The results are overviewed afterward.)

In this paper, we modify the local constraint, aiming to implement the periodic-boundary condition, and restore the translation invariance. Technically, the restoration of translation invariance admits a substantial reduction in the transfer-matrix size. Taking the advantage, we treat the sizes up to $L$=7 and analyze the singularities of crumpling transitions in detail.

The cluster-variation method (CVM) (based on the single-hexagon approximation) revealed a rich character of the discrete folding [27,28]. According to CVM, there appear the totally flat, octahedral, tetrahedral, and piled-up phases, as the bending rigidity $K$ changes from $\infty$ to $-\infty$. Namely, in respective phases, the triangular-lattice sheet crumples up to form a octahedron, a tetrahedron, and a triangular plaquette; see Fig. 3 of Ref. [26]. (This picture is based on a single-hexagon approximation of CVM. Beyond a mean-field level, the thermal undulations may be induced, particularly, in the vicinity of the transition point, disturbing the shape of the crumpled sheet significantly.) More specifically, the crumpling transitions separating these phases are estimated as $K$=0.185, −0.294, and −0.852; hereafter, we abbreviate the set of parameters as (0.185,−0.294,−0.852). At each transition point, the latent heat is estimated as (0.229, 0.14,0); namely, the third transition is continuous according to CVM. On the one hand, the DMRG simulation [32,33] indicates the transition point [0.195(2),−0.32(1),−0.76(1)] with the latent heat [0.365(5), 0.04(2), 0.03(2)]; the character of the third transition point is still controversial.

The rest of this paper is organized as follows. In Sec. II, we propose a modified folding rule [Eq. (1)]; the transfer-matrix formalism [26] is explicated in the Appendix. In Sec. III, we present the numerical results. The singularities of the crumpling transitions are analyzed in detail. In Sec. IV, we present the summary and discussions.

## II. MODIFICATION OF THE FOLDING RULE

In this section, we present a modified folding rule [Eq. (1)]. As mentioned in the introduction, the folding rule enforced by the prefactors in Eq. (A1), is too restrictive to adopt the periodic-boundary condition. So far, the numerical simulation has been performed under the open-boundary condition [26,28,32,33].

1539-3755/2010/81(4)/041116(6)
04116-1
©2010 The American Physical Society

To begin with, we outline the transfer-matrix formalism; an explicit algorithm is presented in the Appendix. According to Ref. [26], through a dual transformation, the triangular-lattice folding reduces to an Ising model on the hexagonal lattice [Fig. 9(a)]. A drawing of a transfer-matrix strip is presented in Fig. 9(b). A peculiarity of this reduced Ising model is that the spins surrounding each hexagon are subjected to a constraint. (The constraint originates from the folding rule.) To be specific, the prefactors $U_jV_j(=0,1)$ of the transfer-matrix element [Eq. (A1)] restrict the configuration space. As mentioned in the Introduction, this constraint is incompatible with the periodic-boundary condition. (For instance, a cylindrical paper supports a large strain, whereas an open paper is flexible.)

Aiming to restore the translational invariance, we modify the prefactors. We replace Eq. (A1) with

$$
\frac{1}{L} \sum_{l=1}^{L}\left(\prod_{j \neq l} U_{j} V_{j}\right)\left[(1-p) U_{l} V_{l}+p\right] \exp \left[-\sum_{k \neq l} H_{k}(K)-H_{l}\left(K^{\prime}\right)\right].
\tag{1}
$$

Here, the parameter $L$ denotes the system size, and the explicit formulas for the constraint $U_jV_j$ and the elastic energy $H_k(K)$ are shown in the Appendix. As compared with the original form (A1), our modified expression (1) has a defect at $l$, where the folding-rule constraint is released. Because the defect is distributing uniformly by the summation $\sum_{l=1}^{L}$ and the normalization factor $1/L$, the translational invariance is maintained. The parameter $K'$ describes the local elastic constant at the defect. The probability of the defect is controlled by the parameter $p$; at $p=0$, the original constraint $U_lV_l$ recovers, whereas at $p=1$, the constraint disappears $U_lV_l \to 1$. We stress that a single defect does not alter the thermodynamic (bulk) properties. As a by-product, two tunable parameters $p$ and $K'$ are available. The parameters are adjusted to

$$
(p, K')=(0.7,1.5 K).
\tag{2}
$$

A justification of this choice is given in Sec. III B (Fig. 2).

## III. NUMERICAL RESULTS

In this section, we present the simulation results. We employed the transfer-matrix method (Appendix) with a modified folding rule [Eq. (1)]. The numerical diagonalization was performed within a subspace specified by the wave number $k=0$ and the parity even. [In a preliminary survey, we confirmed that the dominant-eigenvalue (thermal equilibrium) state belongs to this subspace.] Here, we make use of the spin-inversion symmetry $\sigma_i,z_i \to \pm \sigma_i, \pm z_i$. (This symmetry group originates from the overall rotation of the crumpled triangular-lattice sheet.) We stress that the wave number $k$ makes sense owing to the restoration of the translational invariance [Eq. (1)].

### A. Crumpling transitions: A preliminary survey

In Fig. 1, we plot the free-energy gap,

![](./images/811795719131234305_1.jpg)

FIG. 1. The free-energy gap [Eq. (3)] is plotted for the bending rigidity $K$ and the system size $L=(+)~4$, $(\times)~5$, $(*)~6$, and $(\square)~7$. The data indicate singularities (crumpling transitions) around $K$ $\approx$0.2, $-0.3$, and $-0.8$; detailed analyses of each transition are made in Figs. 3–8.

$$
\Delta f=f_{2}-f_{1},
\tag{3}
$$

for the bending rigidity $K$. Here, the free energy per unit cell is given by $f_i=-\ln \Lambda_i/(2L)$ with the (sub)dominant eigenvalue $\Lambda_{1(2)}$ of the transfer matrix. [Here, the unit cell stands for a triangle of the original lattice rather than a hexagon of the dual lattice; see Fig. 9(a).]

As mentioned in the introduction, the triangular-lattice sheet becomes crumpled, as the rigidity $K$ changes from $\infty$ to $-\infty$. In Fig. 1, we see a number of signatures of the crumpling transitions around $K$$\approx$0.2, $-0.3$, and $-0.8$. (Note that the closure of the excitation gap indicates an onset of phase transition.) On the one hand, the CVM analysis [27,28] predicts a series of crumpling transitions at $(0.185,-0.294,$ $-0.852)$. The results appear to be consistent with those of Fig. 1, suggesting that the excitation-gap closure indicates a location of the crumpling transition. Detailed analyses of each singularity are made in Secs. III C and III D.

### B. Simulation at $p=1$ and $K'=0$

As a comparison, we provide a simulation result, setting the defect parameters to $p=1$ and $K'=0$ tentatively. This parameter set has an interpretation that a rupture (pair of open edges) distributes uniformly along the transfer-matrix strip. (This situation is an extension of the open-boundary condition, for which the rupture is static.)

In Fig. 2, we present the free-energy gap $\Delta f$ for the bending rigidity $K$; the range of $K$ is the same as that of Fig. 1. The signatures of crumpling transitions in Fig. 2 are less clear, as compared to those of Fig. 1. This result indicates that the choice of the defect parameters affects the finite-size behavior. In the preliminary stage, we surveyed a parameter space of $p$ and $K'$ and arrived at a conclusion that the above choice [Eq. (2)] is an optimal one. Note that these parameters are the byproduct of the modification of the folding rule [Eq. (1)]. Here, we make use of these redundant parameters so as to improve the finite-size behavior, aiming to take the thermodynamic limit reliably.

### C. Crumpling transition in $K>0$: Analysis of the latent heat via the Hamer method

In Sec. III A, we observed a series of crumpling transitions. In this section, we analyze the singularity of a transition in the $K>0$ side.

![](./images/811795719131234305_2.jpg)

FIG. 2. The free-energy gap [Eq. (3)] is plotted for the bending rigidity $K$ and the system size $L=(+)$ 4, $(\times)$ 5, $(*)$ 6, and $(\square)$ 7. Tentatively, the defect parameters [Eq. (1)] are set to $p$=1 and $K'$=0. The data appear to be scattered, as compared to those of Fig. 1. This result indicates that the finite-size behavior is improved by adjusting the defect parameters.

To begin with, we determine the transition point. In Fig. 3, an approximate transition point $K_c(L)$ is plotted for $1/L^2$. Here, the approximate transition point minimizes the free-energy gap
$$
\left.\partial_K \Delta f\right|_{K=K_c(L)}=0. \tag{4}
$$

The least-squares fit yields an estimate $K_c$=0.206 17(70). Similarly, as for $5 \leq L \leq 7$, we obtain an estimate $K_c$=0.205 06(99). A discrepancy between these results may be an indicator of possible systematic error. The systematic error appears to be comparable to the fitting error. Regarding both errors as the sources of error margin, we obtain
$$
K_c=0.206(2). \tag{5}
$$

Based on the transition point $K_c(L)$, we estimate the amount of latent heat. According to Ref. [36], the low-lying eigenvectors of the transfer matrix contain information on the latent heat. We explain the underlying idea and present the scheme explicitly. At the discontinuous (first-order) transition point, the low-lying spectrum of the transfer matrix exhibits a level crossing, and the discontinuity (sudden drop) of the slope reflects a release of the latent heat. However, the finite-size artifact (level repulsion) smears out the singularity. According to Ref. [36], regarding the low-lying levels as nearly degenerate, one can resort to the perturbation theory of the degenerated case and calculate the level splitting (discontinuity of slope) explicitly. To be specific, we consider the matrix
$$
V=\begin{pmatrix}
V_{11} & V_{12} \\
V_{21} & V_{22}
\end{pmatrix}, \tag{6}
$$
with $V_{ij}=\langle i|\partial_K T|j\rangle$. The matrix $T$ denotes the transfer matrix; namely, the matrix element $\partial_K T$ is given by a product of Eqs. (A1) and (A5) with $K$ dropped. The bases, $|1\rangle$ and $|2\rangle$, are the (nearly degenerate) eigenvectors of $T$ with the eigenvalues $\Lambda_{1,2}$, respectively. The states $\{|i\rangle\}$ are normalized so as to satisfy $\langle i|T|i\rangle$=1. According to the perturbation theory, the eigenvalues of Eq. (6) yield the level-splitting slopes due to $K$. Hence, the latent heat (per unit cell) is given by a product of this discontinuity and the elastic constant
$$
Q(L)=|K_c(L)|\sqrt{(V_{11}-V_{22})^2+4V_{12}V_{21}} \frac{1}{2L}, \tag{7}
$$
for the system size $L$.

![](./images/811795719131234305_3.jpg)

FIG. 3. The crumpling transition $K$$\approx$0.2 observed in Fig. 1 is analyzed in detail. The transition point $K_c(L)$ [Eq. (4)] is plotted for $1/L^2$. The least-squares fit yields an estimate $K_c$=0.206 17(70).

In Fig. 4, we plot the latent heat [Eq. (7)] for $1/L^2$. The least-squares (linear) fit yields an estimate $Q$=0.356(12) in the thermodynamic limit. Similarly, we obtain $Q$=0.3774(93) for $5 \leq L \leq 7$. Again, the systematic error appears to be comparable to the fitting error. We estimate
$$
Q=0.356(30). \tag{8}
$$

![](./images/811795719131234305_4.jpg)

FIG. 4. The latent heat $Q(L)$ [Eq. (7)] is plotted for $1/L^2$. The least-squares fit yields an estimate $Q$=0.356(12).

This is a good position to address a few remarks. First, the latent heat [Eq. (8)] agrees with that of DMRG [32] (see the introduction), whereas the transition point [Eq. (5)] lies out of the error margin. This discrepancy may indicate an existence of systematic error as to the determination of $K_c$. A peculiarity [30] of this transition is that in the $K>K_c$ side, the system becomes completely flattened; namely, there exist no thermal undulations as if the system is in the low-temperature limit $K \to \infty$. This peculiarity may give rise to a bias to $K_c$. (As a matter of fact, in Ref. [32], a pronounced hysteresis was observed.) On the contrary, we confirmed that the ambiguity of $K_c$ does not influence the latent heat $Q$ very much. (Because of this $K_c$ independence, the result $Q$ is reliable as the above-mentioned consistency with DMRG suggests.) In the next section, the remaining two transitions are analyzed in a unified manner. Second, we consider the $1/L^2$ extrapolation scheme. The finite-size data converge rapidly to the thermodynamic limit around the first-order transition

![](./images/811795719131234305_5.jpg)

FIG. 5. The crumpling transition $K\approx -0.3$ observed in Fig. 1 is analyzed in detail. The transition point $K_{c}(L)$ [Eq. (4)] is plotted for $1/L^{2}$. The least-squares fit yields an estimate $K_{c}=-0.320(12)$.

point because the correlation length (typical length scale) $\xi$ remains finite. Hence, the dominant system-size corrections should be described by $1/L^{2}$ (rather than $1/L$).

### D. Crumpling transitions in $K<0$

In this section, we analyze the remaining transitions in the $K<0$ side.

First, we analyze the transition around $K\approx -0.3$. In Fig. 5, we plot the transition point [Eq. (4)] for $1/L^{2}$. The least-squares fit to these data yields an estimate $K_{c}=-0.320(12)$. Similarly, we obtain $K_{c}=-0.316(28)$ for $5\leq L\leq 7$. The systematic error appears to be negligible, as compared to the fitting error. Considering the latter as the source of error margin, we estimate the transition point as
$$
K_{c}=-0.32(1). \tag{9}
$$

In Fig. 6, we plot the latent heat [Eq. (7)] for $1/L^{2}$. The least-squares fit yields $Q=0.077(15)$. Similarly, for $5\leq L\leq 7$, we obtain $Q=0.058(28)$. The fitting and systematic errors are comparable. Considering them as the sources of error margin, we estimate the latent heat as
$$
Q=0.08(3). \tag{10}
$$

Second, we turn to the analysis of the transition around $K\approx -0.8$. In Fig. 7, we plot the transition point [Eq. (4)] for $1/L^{2}$. The least-squares fit to these data yields an estimate $K_{c}=-0.76(10)$. Similarly, we obtain $K_{c}=-0.72(24)$ for $5\leq L\leq 7$. The fitting error dominates the systematic error. Neglecting the latter, we obtain

![](./images/811795719131234305_6.jpg)

FIG. 7. The crumpling transition $K\approx -0.8$ observed in Fig. 1 is analyzed in detail. The transition point $K_{c}(L)$ [Eq. (4)] is plotted for $1/L^{2}$. The least-squares fit yields an estimate $K_{c}=-0.76(10)$.

$$
K_{c}=-0.76(10). \tag{11}
$$

In Fig. 8, we plot the latent heat [Eq. (7)] for $1/L^{2}$. The least-squares fit yields $Q=0.049(51)$. Similarly, for $5\leq L\leq 7$, we obtain $Q=0.01(11)$. Again, the systematic error appears to be negligible. We estimate the latent heat as
$$
Q=0.05(5). \tag{12}
$$

Last, we consider a shaky character of Figs. 3-8 (in particular, Figs. 5-8). Such a shaky character is an artifact due to the cluster size. In the preliminary stage, we surveyed the planar folding [29-31] for considerably large system sizes $L\leq 14$; the configuration space of the planar folding is much restricted. As a result, we found that the finite-size behavior is irregular with respect to $L$; this irregularity is an obstacle to making an extrapolation. Roughly speaking, the finite-size behavior is categorized by $L=0$, 1, and $2\bmod 3$. Although the enlarged configuration space suppresses this irregularity, a slight irregularity for $L=6$ ($=0\bmod 3$) still remains. A slight bump of Figs. 5 and 7 may be due to this irregularity. Hence, we consider that the deviations (seemingly curved plots) in Figs. 3-8 are not systematic ones. Rather, considering them as a source of errors, we estimate the error margin by making two independent extrapolations for different sets of system sizes.

### IV. SUMMARY AND DISCUSSIONS

We proposed a modified folding rule [Eq. (1)], which enables us to simulate the discrete folding without the open

![](./images/811795719131234305_7.jpg)

FIG. 6. The latent heat $Q(L)$ [Eq. (7)] is plotted for $1/L^{2}$. The least-squares fit yields an estimate $Q=0.077(15)$.

![](./images/811795719131234305_8.jpg)

FIG. 8. The latent heat $Q(L)$ [Eq. (7)] is plotted for $1/L^{2}$. The least-squares fit yields an estimate $Q=0.049(51)$.

edges. By means of the transfer-matrix method, we investi- gated a series of the crumpling transitions. We estimate the transition point and the latent heat as $[0.206(2),-0.32(1)$, $-0.76(10)]$ and $[0.356(30), 0.08(3), 0.05(5)]$, respectively. Our result agrees with the preceding CVM and DMRG re- sults. In particular, our result is in quantitative agreement with that of DMRG.

According to Ref. [28], the third singularity (around $K$ $\approx-0.8$ ) is so subtle that it could not be captured until $L=8$. On the contrary, our data in Figs. 1 and 7 succeeds in detect- ing a signature of a crumpling transition even for $4 \leq L \leq 7$. As anticipated, the restoration of the translation invariance leads to an improvement of the finite-size behavior.

As mentioned in the Introduction, it is still unclear whether the third transition is continuous [28] or belongs to a weak-first-order transition [33]. The present result [Eq. (12)] does not exclude a possibility of a continuous transition. Ac- cording to Ref. [28], around $K \approx-0.8$, through a truncation of the configuration space, the discrete folding reduces to a simplified version of the folding model, the so-called planar folding [29-31], which exhibits a continuous transition in the $K<0$ side. An examination of this truncation process may provide valuable information on the nature of this phase transition. This problem will be addressed in the future study.

## APPENDIX: TRANSFER-MATRIX FORMALISM FOR THE DISCRETE FOLDING

In this appendix, we present the transfer-matrix formalism for the discrete folding [26]. Before commencing a math- ematical description, we explicate a basic feature of the dis- crete folding. We consider a sheet of the triangular lattice[Fig. 9(a)]. Along the edges, the sheet folds up. The fold angle $\theta$ along the edges is discretized into four possi bilities, namely, "no fold" $(\theta=\pi)$ , "complete fold" $(\theta=0)$ , "acute fold" $[\theta=\arccos (1 / 3)]$ , and "obtuse fold" $[\theta$ =arccos(-1/3)]; in other words, the triangular lattice is em- bedded in the face-centered-cubic lattice [26].

The above discretization leads to an Ising-spin represen- tation. The mapping, the so-called gauge rule, reads as fol- lows [26]. We place two types of Ising variables $\{\sigma_{i}, z_{i}\}$ at each triangle $i$ (rather than each joint); see Fig. 9(a). Hence, hereafter, we consider the a spin model on the dual (hexago- nal) lattice. The gauge rule sets the joint angle between the adjacent triangles. That is, provided that the $z$ spins are an tiparallel $(z_{1} z_{2}=-1)$ for a pair of adjacent neighbors, the jointangle is either an acute or obtuse fold. Similarly, if $\sigma_{1} \sigma_{2}$ =-1 folds, the relative angle is either a complete or obtusefold. The spins are subjected to a constraint (folding rule);The prefactors $U_{j} V_{j}$ of the transfer-matrix element [Eq. (A1)] enforces the constraint.

As a consequence, the discrete folding reduces to a two- component Ising model on the hexagon lattice. Hence, the transfer-matrix strip looks like that drawn in Fig. 9(b). The row-to-row statistical weight $T_{\{\sigma_{i}, z_{i}\},\{\sigma_{i}^{\prime}, z_{i}^{\prime}\}}$ yields the transfer matrix element. The transfer-matrix element for the stripwidth $L$ is given by [26]

![](./images/811795719131234305_9.jpg)

FIG. 9. (a) We consider a discrete folding of the triangular lat- tice. In order to specify the fold angle, we place two types of Ising variables $\{z_{i}, \sigma_{i}\}$ on each triangle $i$ rather than at each joint (gauge rule [26]). Hence, hereafter, we consider a spin model on the dual(hexagonal) lattice. (b) Construction of the transfer matrix. The row-to-row statistical weight yields the transfer-matrix element [Eq.(A1)]. So far, the open-boundary condition has been imposed. Here, we restore the translational invariance by using a modified folding rule [Eq.(1)].

$$
T_{\left\{z_{i}, \sigma_{i}\right\},\left\{z_{i}^{\prime}, \sigma_{i}^{\prime}\right\}}=\left(\prod_{j=1}^{L} U_{j} V_{j}\right) \exp (-H / T),\qquad(\mathrm{A}1)
$$

with

$$
\begin{aligned}
U_{j}=\delta\left(\sigma_{2 j-2}+\sigma_{2 j-1}+\sigma_{2 j}+\sigma_{2 j-1}^{\prime}+\sigma_{2 j}^{\prime}+\sigma_{2 j+1}^{\prime} \bmod 3,0\right)
\end{aligned}\qquad(\mathrm{A}2)
$$

and

$$
V_{j}=\prod_{c=1}^{2} \delta\left[\alpha_{c}\left(z_{2 j}, z_{2 j-1}, z_{2 j-2}, z_{2 j-1}^{\prime}, z_{2 j}^{\prime}, z_{2 j+1}^{\prime}\right) \bmod 2,0\right].\qquad(\mathrm{A}3)
$$

The factors $\{U_{j}, V_{j}\}$ enforce the constraint (folding rule) as to the spins surrounding each hexagon. Here, $\delta(m, n)$ denotes Kronecker's symbol, and $\alpha_{c}$ is given by

$$
\alpha_{c}\left(z_{1}, \ldots, z_{6}\right)=\sum_{i=1}^{6} \frac{1}{2}\left(1-z_{i} z_{i+1}\right) \delta\left(\sum_{j=1}^{i} \sigma_{j} \bmod 3,0\right).\qquad(\mathrm{A}4)
$$

The Boltzmann factor $\exp (-H / T)$ is due to the bending energy cost $H$ . Hereafter, we choose the temperature $T$ as a unit of energy; namely, we set $T=1$ . As usual, the bending energy is given by the inner product $\cos \theta_{i j}$ of the surface

041116-5

normals of adjacent triangles. Hence, the bending energy is
given by a compact formula

$$
H=\sum_{k} H_{k}(K). \tag{A5}
$$

Here, the index $k$ specifies each hexagon as in Eq. (A1). The
local energy of each hexagon $H_k$ is given by

$$
\begin{aligned}
H_{k}(K) &=-0.5 \sum_{i=1}^{6} K \cos \theta_{i, i+1} \\
&=-0.5 \sum_{i=1}^{6} \frac{1}{3} K \sigma_{i} \sigma_{i+1}\left(1+2 z_{i} z_{i+1}\right), \quad \text { (A6) }
\end{aligned}
$$

with the bending rigidity $K$. Here, the summation $\sum_{i=1}^{6}$ runs
over all vertices around the hexagon $k$. (The overall factor of
0.5 compensates the duplicated sum.)

---

[1] D. R. Nelson and L. Peliti, J. Phys. (France) **48**, 1085 (1987).
[2] D. Nelson, T. Piran, and S. Weinberg, *Statistical Mechanics of Membranes and Surfaces: Volume 5 of the Jerusalem Winter School for Theoretical Physics* (World Scientific, Singapore, 1989).
[3] P. Ginsparg, F. David, and J. Zinn-Justin, *Fluctuating Geometries in Statistical Mechanics and Field Theory* (Elsevier Science, The Netherlands, 1996).
[4] M. J. Bowick and A. Travesset, Phys. Rep. **344**, 255 (2001).
[5] P. Canham, J. Theor. Biol. **26**, 61 (1970).
[6] W. Helfrich, Z. Naturforsch. C **28**, 693 (1973).
[7] Y. Kantor, M. Kardar, and D. R. Nelson, Phys. Rev. Lett. **57**, 791 (1986).
[8] Y. Kantor, M. Kardar, and D. R. Nelson, Phys. Rev. A **35**, 3056 (1987).
[9] M. Baig, D. Espriu, and J. Wheater, Nucl. Phys. B **314**, 587 (1989).
[10] J. Ambjørn, B. Durhuus, and T. Jonsson, Nucl. Phys. B **316**, 526 (1989).
[11] R. Renken and J. Kogut, Nucl. Phys. B **342**, 753 (1990).
[12] R. Harnish and J. Wheater, Nucl. Phys. B **350**, 861 (1991).
[13] M. Baig, D. Espiu, and A. Travesset, Nucl. Phys. B **426**, 575 (1994).
[14] M. Bowick, S. Catterall, M. Falcioni, G. Thorleifsson and K. Anagnostopoulos, J. Phys. I **6**, 1321 (1996).
[15] J. F. Wheater and P. Stephenson, Phys. Lett. B **302**, 447 (1993).
[16] J. F. Wheater, Nucl. Phys. B **458**, 671 (1996).
[17] F. David and E. Guitter, Europhys. Lett. **5**, 709 (1988).
[18] P. Le Doussal and L. Radzihovsky, Phys. Rev. Lett. **69**, 1209 (1992).
[19] D. Espriu and A. Travesset, Nucl. Phys. B **468**, 514 (1996).
[20] M. Paczuski, M. Kardar, and D. R. Nelson, Phys. Rev. Lett. **60**, 2638 (1988).
[21] J.-Ph. Kownacki and H. T. Diep, Phys. Rev. E **66**, 066105 (2002).
[22] H. Koibuchi, N. Kusano, A. Nidaira, K. Suzuki, and M. Yamada, Phys. Rev. E **69**, 066139 (2004).
[23] Y. Kantor and D. R. Nelson, Phys. Rev. Lett. **58**, 2774 (1987).
[24] Y. Kantor and D. R. Nelson, Phys. Rev. A **36**, 4020 (1987).
[25] J.-P. Kownacki and D. Mouhanna, Phys. Rev. E **79**, 040101(R) (2009).
[26] M. Bowick, P. Di Francesco, O. Golinelli, and E. Guitter, Nucl. Phys. B **450**, 463 (1995).
[27] E. N. M. Cirillo, G. Gonnella, and A. Pelizzola, Phys. Rev. E **53**, 3253 (1996).
[28] M. Bowick, O. Golinelli, E. Guitter, and S. Mori, Nucl. Phys. B **495**, 583 (1997).
[29] Y. Kantor and M. V. Jarić, Europhys. Lett. **11**, 157 (1990).
[30] P. Di Francesco and E. Guitter, Phys. Rev. E **50**, 4418 (1994).
[31] E. N. M. Cirillo, G. Gonnella, and A. Pelizzola, Phys. Rev. E **53**, 1479 (1996).
[32] Y. Nishiyama, Phys. Rev. E **70**, 016101 (2004).
[33] Y. Nishiyama, Phys. Rev. E **72**, 036104 (2005).
[34] S. R. White, Phys. Rev. Lett. **69**, 2863 (1992).
[35] I. Peschel, X. Wang, M. Kaulke, and K. Hallberg, *Density-Matrix Renormalization: A New Numerical Method in Physics* (Springer-Verlag, Berlin, 1999).
[36] C. J. Hamer, J. Phys. A **16**, 3085 (1983).