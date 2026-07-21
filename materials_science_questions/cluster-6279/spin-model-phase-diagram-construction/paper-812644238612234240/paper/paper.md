Fluctuation-induced tetracritical point in the magnetic phase diagram of a quasi-two-dimensional XY antiferromagnet

M. L. Plumer, and A. Caillé

Citation: *Journal of Applied Physics* **69**, 6161 (1991);
View online: https://doi.org/10.1063/1.348792
View Table of Contents: http://aip.scitation.org/toc/jap/69/8
Published by the American Institute of Physics

![](./images/812644238612234240_1.jpg)

# Fluctuation-induced tetracritical point in the magnetic phase diagram of a quasi-two-dimensional XY antiferromagnet
M. L. Plumer and A. Caillé
Centre de Recherche en Physique du Solide et Départment de Physique, Université de Sherbrooke, Sherbrooke, Québec J1K 2R1 Canada

Monte Carlo simulation results of the classical antiferromagnetic planar model on a stacked triangular lattice with weak interplanar exchange coupling, and an in-plane applied magnetic field, are reported. The determined field-temperature phase diagram differs significantly from the corresponding mean-field result and shows that tetracritical behavior occurs at $H=0$, $T=T_N$, similar to that found previously for the cases of isotropic and quasi-one-dimensional magnetic interactions.

Magnetic phase transitions involving tripartite lattices have received considerable attention recently due mainly to the work of Kawamura, which has exposed a new chiral universality class. $^1$ Frustration of antiferromagnetic neighbor bonds is responsible for the occurrence of non-colinear magnetic order in such systems. $^2$ For the stacked triangular lattice with planar anisotropy, the magnetic structure takes the form of a helically polarized spin density ($120^\circ$ spin structure) with degenerate chiralities ($\pm \mathbf{Q}$) giving rise to an Ising-like ($Z_2$) character in addition to the usual $xy$ ($S_1$) symmetry and an associated phase transition with unusual critical exponents $^3$ ($\alpha \cong 0.40$, $\beta \cong 0.25$, $\gamma \cong 1.10$, $\nu \cong 0.53$). Magnetic order of this type thus exhibits discrete as well as continuous degeneracy. $^4$ An alternative point of view has recently been proposed. $^5$

Further insight into the critical behavior is gained by considering the effects of an in-plane applied magnetic field. The zero-field paramagnetic-to-helical phase transition at $T_N$ splits into two lines of second-order transitions, $^{6,7}$ as shown schematically in Fig. 1, revealing a tetracritical point $^8$ at $H=0$, $T=T_N$. Such tetracritical behavior has been observed $^{9-11}$ in the quasi-one-dimensional hexagonal antiferromagnet CsMnBr$_3$. Scaling and renormalization group analysis has been used to study crossover behavior and predicts that the 1-5A transition line belongs to the $xy$ universality class and that the 5A-7 transition line is of Ising universality. $^{12}$ Splitting of the Néel temperature by a magnetic field has also been predicted for the planar model on a two-dimensional (2D) triangular lattice. $^{13,14}$

![](./images/812644238612234240_2.jpg)

FIG. 1. Schematic of tetracritical behavior at $H=0$, $T=T_N$ where broken curves represent lines of second-order transitions. Regions labelled 1, 5A, and 7 denote paramagnetic, linearly polarized, and elliptically polarized phases, respectively.

We have recently studied the effects of varying the interplanar exchange coupling on the magnetic phase diagrams of the antiferromagnetic planar model on a stacked triangular (simple hexagonal) lattice using a mean-field theory and Monte Carlo simulations of the Hamiltonian (with $\mathbf{H} \parallel \hat{x}$)

$$
\mathscr{H}=J_{\parallel} \sum_{\langle i j\rangle} \mathbf{s}_{i} \cdot \mathbf{s}_{j}+J_{\perp} \sum_{\langle l k\rangle} \mathbf{s}_{l} \mathbf{s}_{k}-\sum_{i} H s_{i}^{x}, \tag{1}
$$

where $\mathbf{s}_{i} \perp \hat{c}$ ($\hat{c} \parallel \hat{z}$) and $J_{\parallel}, J_{\perp} > 0$ with $\langle i,j \rangle$ and $\langle k,l \rangle$ summed over nearest-neighbor sites along the $c$ axis and in the basal plane, respectively. $^{15}$ With $J_{\parallel} \equiv 1$, mean-field results for $H,T$ phase diagrams using a range of values for $J_{\perp}$ exhibit a surprisingly rich variety of structures. For the isotropic case, $J_{\parallel} = J_{\perp} = 1$, both mean-field theory and Monte Carlo simulations yield phase diagrams with the generic structure depicted in Fig. 1. Similar results are found for quasi-one-dimensional exchange interactions $^{16}$ $J_{\parallel} \gg J_{\perp}$. Of interest here are results for the quasi-two-dimensional case. The phase diagram determined by mean-field theory with $J_{\parallel} = 1$ and $J_{\perp} = 10$ is shown in Fig. 2, where phase 5C labels a linearly polarized phase (of different symmetry than 5A $^{15}$) and where the boundary between phases 5C and 7 is a line of first-order transitions. Note that the multicritical point at $H=0$, $T=T_N$ does not represent the merging of Ising and $xy$ critical lines (only one critical line with $xy$ symmetry occurs) as in Fig. 1. The present work was motivated by the possibility (discussed in Ref. 15) that this result suggests the zero-field transition is not of chiral ($Z_2 \times S_1$) symmetry, as in the cases of smaller $J_{\perp}$ values, with the concomitant implication of nonuniversal critical behavior associated with the model Hamiltonian (1).

Monte Carlo simulations were performed on the Hamiltonian (1) with $J_{\parallel} = 1$ and $J_{\perp} = 10$ to determine the magnetic phase diagram. In contrast with the isotropic and quasi-one-dimensional cases, the results differ considerably from the mean-field prediction (Fig. 2), establishing that effects due to critical fluctuations are significant in the case

![](./images/812644238612234240_3.jpg)

FIG. 2. Phase diagram from the mean-field treatment of Eq. (1) with $J_{\parallel}=1$ and $J_{\perp}=10$ as given in Ref. 15. Solid curve denotes a first-order transition line.

of weak interplanar interactions. (Related effects were also found for the 2D triangular lattice. $^{13}$ ) A new linearly po larized phase is stabilized close to $T_{N}$ and tetracritical be havior, similar to that shown in Fig. 1, is observed. Limited finite-size scaling results at $H=0$ give a value for the crit ical exponent $\beta$ consistent with the chiral universality class.

Before representing the Monte Carlo results, it is con- venient to summarize the description of magnetically or- dered phases in terms of the spin density expressed as aFourier expansion, as in Ref. 15:
$$\rho(\mathbf{r})=\mathbf{m}+\sum_{n=1}^{3}\left(\mathbf{S}_{n} e^{i \mathbf{Q}_{n} \mathbf{r}}+\mathbf{S}_{n}^{*} e^{-i \mathbf{Q}_{n} \mathbf{r}}\right),\qquad(2)$$
 where $m$ is the uniform component induced by the field, $S_{n}=S_{n a}+i S_{n b}$ (with $S_{n a}$ and $S_{n b}$ being real vectors), and
$$\mathbf{Q}_{1}=\frac{1}{2} \mathbf{G}_{\|}+\frac{1}{3} \mathbf{G}_{\perp}, \quad \mathbf{Q}_{2}=\frac{1}{2} \mathbf{G}_{\|}, \quad \mathbf{Q}_{3}=\frac{1}{3} \mathbf{G}_{\perp}, \quad(3)$$
 where, e.g., $Q_{1}=(\pi / c) \hat{z} \pm(4 \pi / 3 a) \hat{x}$ describes a period two modulation along the $c$ axis and a period-three mod ulation in the basal plane. $S_{1}$ represents the primary Fou rier component of the magnetic structures considered here. In addition to the paramagnetic phase $(S_{n}=0)$ and the ordered states 5 and 7 described in Ref. 15, two other types of magnetic order (labelled as in Ref. 7) are referred to below, as characterized by the following nonzero Fouriercomponents:
$$\begin{array}{ll}
\text { phase 6: } & m^{x}, S_{1 b}^{x}, S_{3 a}^{x}, \\
\text { phase 9: } & m^{x}, S_{1 b}^{x}, S_{1 b}^{y}, S_{3 a}^{x}, S_{3 a}^{y}.
\end{array}$$

These magnetic structures are characterized in terms of the primary Fourier component as follows. Phases 5: linear $(S_{1}^{y})$ ; phase 7: elliptical $(S_{1}^{x}, S_{1}^{y})$ ; phase 6: linear $(S_{1}^{x})$ ; phase 9: linear $(S_{1}^{x}, S_{1}^{y})$ . Note that the transitions between phases 7 and $5 C$ and between phases 6 and $5 C$ are neces sarily first order (see Ref. 15) since they each involve a spin flop from a configuration $S_{1 b} \| \hat{x}$ to $S_{1 b} \| \hat{y}$ .

The standard Metropolis method was used for the Monte Carlo simulations, as outlined in Ref. 15, with pe- riodic boundary conditions on $L \times L \times L$ lattices with $L=12$ and 18. Fourier components of the spin density
$$M_{\alpha}(\mathbf{q})=\left(1 / L^{3}\right)\left|\left(\sum_{i} s_{i \alpha} e^{-i \mathbf{q} \cdot \mathbf{R}_{i}}\right)^{2}\right|^{1 / 2}\qquad(4)$$
 were calculated where $\alpha=x, y$ and $q=0, Q_{n}$ , given by Eq.(3). Typical data illustrating the behavior of the primary order parameter $M_{\alpha} \equiv M_{\alpha}(Q_{1})$ at constant $H$ and $T$ scans are shown in Fig. 3. The zero-field results [Fig. 3(a)] show temperature dependence usually associated with a second- order transition, characterized by a point of inflection in the curves, with the ordered phase determined to be the helical $(120^{\circ})$ spin structure. Figure $3(~b)$ shows data at H= 20, giving clear indication of two second-order tran- sitions, with the phase sequence 7-6-1 occurring as thetemperature is increased. Results of the field scan at $T=3$

![](./images/812644238612234240_4.jpg)

FIG. 3. Illustrative Monte Carlo results for the primary order parameter. Arrows indicate estimated locations of second-order phase transitions as determined by points of inflection. (b) and (c) show simulations per- formed using $L=12$ . The nature of phase transitions occurring at field values near $H=35$ in (c) is ambiguous.

![](./images/812644238612234240_5.jpg)

FIG. 4. Phase diagram determined by Monte Carlo simulations of Eq. (1). Region 1 denotes the paramagnetic state and ordered phases 5C, 6, and 7 are characterized by nonzero values of the primary Fourier component $(S_{1 p}),(S_{1 x})$ , and $(S_{1 x}, S_{1 y})$ , respectively. Broken curves serve as guides to the eye and denote second-order phase transition lines. The nature of the boundary between phases 5C and 6, as well as the low- temperature region of the phase diagram, are undetermined. Points on the $T=0$ axis are from the ground-state calculation of Ref. 15 and represent a first-order 5C-7 transition at $H \cong 38$ and a second-order 1-5C transition at $H=94$.

shown in Fig. 3(c) indicate more complicated behavior. A second-order transition occurs at a lower-field value, $H \cong 29$ (a point of inflection is more clearly seen in the data for field scans at $T=4,5,6$ , and 6.5) and also at a high field value, $H \cong 79$ . One or more first- or second-order tran sitions appear to take place at field values near (and below) $H \cong 40$ . It is clear that phase 5 C is stable in the region $40 \lesssim H \lesssim 80$ and that phase 6 occurs in a small region around $H \cong 35$ . Two probable phase-sequence scenarios, with increasing field strength, are 7-6-5C-1 (with the 6-5Ctransition being first order) or 7-6-9-5C-1 (with the 6-9 and 9-5C transitions being either first or second order).

Boundary lines of the $H-T$ phase diagram determined in this way are shown in Fig. 4. The most significant result is the occurrence of the linear phase 6, with $S_{1} \| H$ , near TN (not present in the mean-field theory, Fig. 2) and theasymptotic convergence of two critical lines of $x y$ (the 1-6 boundary) and Ising (the 6-7 boundary) universality at H = 0, T = Ty, as in the previously studied cases depicted in Fig. 1. The boundary between phases 6 and 5C requires further study to determine if it is a first-order line or if the intermediate phase 9 is realized. The nature of the conver- gence of the phases 5C, 6, and 7 at low temperatures also requires further investigation. A spin-wave calculation should be well suited for this purpose.

Finally, the (limited) finite-size scaling analysis using $L=12$ and 18 data to estimate the critical exponent $\beta$ at $H=0$ was done following the method of Kawamura $^{3}$ (also see Ref. 15) where size effects are accounted for by the spin-wave correction

$$M(L)=M(\infty)+c / L,\qquad(5)$$

where $c$ is temperature dependent. Analysis of the present quasi-two-dimensional system is made somewhat compli- cated by the relatively strong size dependence of the Néel temperature. $T_{N}(L)$ was determined approximately by thepoint of inflection in the $L=12$ and 18 data of Fig. 3(a)(using cubic spline fits), and more accurately by adjust-ment to give straight-line log-log plots of $M$ vs $t=(T_{N}$  $-T) / T_{N}$ , with the results $T_{N}(12)=7.06 \pm 0.03$ and TN(18)=7.06±0.03. A significantly smaller finite-size ef- fect (approximately a factor of 10) is observed for the isotropic case, $J_{\|}=J_{\perp}=1$ . Plots of $M(L)$ vs $1 / L$ at sevenselected values of $t >rsim 0$ were made to determine $M(\infty)$  below $T_{N} \cdot^{17}$ A nearly perfect straight-line log-log plot of $M(\infty)$ vs $t$ is the result of this method, giving the estimate=0.24±0.03. Although simulations using larger lattices are required for a more accurate estimate, this result strongly suggests that the transition at $T_{N}$ of the present model belongs to the chiral universality class.

In conclusion, this work has demonstrated that critical fluctuations are responsible for the occurrence of tetracrit- ical behavior in the quasi-two-dimensional antiferromag- netic planar model on a stacked triangular lattice. Nonuni- versality, a possibility suggested by the results of Ref. 5, appears not to occur in this model for the wide range of nearest-neighbor coupling strength studied thus far.

Simulations were performed mainly at the Ontario Centre for Large Scale Computing. This work was sup- ported by the Natural Sciences and Engineering Research Council (NSERC) of Canada and Fonds pour la Forma- tion de Chercheurs et I'Aide à la Recherche (FCAR) du Québec.

'H. Kawamura, Phys. Rev. B 38, 4916 (1988); H. Kawamura, 42,2610(E)(1990); H. Kawamura, J. Appl. Phys. 63, 3086 (1988); H. Kawamura, J. Phys. Soc. Jpn. 59, 2301 (1990).
2R. S. Gekht and V. I. Ponomarev, Phase Transitions 20, 27 (1990).
3H. Kawamura, J. Phys. Soc. Jpn. 58, 584 (1989).
4J. Villain, J. Phys. (Paris) 38, 385 (1977).
5P. Azaria, B. Delamotte, and T. Jolicoeur, Phys. Rev. Lett. 64, 3175(1990).
 B. Schaub and D. Mukamel, Phys. Rev. B 32, 6385 (1985).
7M. L. Plumer, A. Caille, and K. Hood, Phys. Rev. B 39, 4489 (1989).
 $^{8}$ Two additional critical lines merge at this point from the negative $H^{2}$ ,T plane; see, e.g., A. D. Bruce and A. Aharony, Phys. Rev. B 11, 478(1975).
 B. D. Gaulin, T. E. Mason, M. F. Collins, and J. Z. Larese, Phys. Rev. Lett. 62, 1380 (1989).
10M. Poirier, M. Castonguay, A. Caille, M. L. Plumer, and B. D. Gaulin, Physica B 165&166, 171 (1990).
"M. L. Plumer and A. Caille, Phys. Rev. B 41, 2543 (1990).
12H. Kawamura, A. Caillé, and M. L. Plumer, Phys. Rev. B 41, 4416(1990).
13D. H. Lee, J. D. Joannopoulos, J. E. Negle, and D. P. Landau, Phys. Rev. Lett. 52, 433 (1984); D. H. Lee, J. D. Joannopoulos, J. E. Negle, and D. P. Landau, Phys. Rev. B 33, 450 (1986).
14H. Kawamura and S. Miyashita, J. Phys. Soc. Jpn. 54, 4530 (1985).
15M. L. Plumer and A. Caillé, Phys. Rev. B 42, 10388 (1991).
16T. E. Mason, M. F. Collins, and B. D. Gaulin, J. Appl. Phys. 67, 5421(1990).
 $^{17}$ In the work of Refs. 3 and $15,1 / L$ plots at selected values of $T$ (and not t) were made. This is an acceptable procedure if the $L$ dependence of TN is small.