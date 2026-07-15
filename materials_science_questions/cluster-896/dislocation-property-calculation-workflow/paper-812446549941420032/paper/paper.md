# COMPUTER SIMULATION OF LEDGE FORMATION AND LEDGE INTERACTION FOR THE SILICON (111) FREE SURFACE

H. BALAMANE, T. HALICIOĞLU and W.A. TILLER

Department of Materials Science and Engineering, Stanford, California 94305, USA

Both strip and triangular clusters, composed of $\langle 2 \overline{1} \overline{1}\rangle$ ledges, have been simulated on the Si (111) surface. The long range ledge-ledge interaction and the surface stress tensor distribution have been evaluated for these two pill-box geometries using a semi-empirical potential energy function that incorporates both two-body and three-body contributions. The consequences of the ledge-ledge interaction on two-dimensional nucleation for Si (111) has been evaluated as a function of Si adatom supersaturation and shown to differ significantly from conventional theory where such interaction is neglected.

## 1. Introduction

Calculations using a semiempirical potential energy function show that the $\langle 2 \overline{1} \overline{1}\rangle$ ledges on a Si (111) surfaces have the interesting property of providing a dilatational contribution to the total surface strain which allows an important reduc- tion to occur in the strongly compressive surface stress tensor [1]. This ledge-stress tensor interac- tion allows a long range force to develop which culminates in a long range ledge-ledge interaction allowing one to see a decreasing ledge energy with ledge separation out to separations of 50-60 $\mathring{A}$ [1,2]. This type of long range interaction also has a strong influence on the ledge reconstruction pro- cess [1,2] and thus is bound to play an important role in the nucleation and layer movement processes on Si(111) surfaces.

In the standard formula for nucleation frequency, $I$, is given by

$$
I=I_{0} \exp \left(-\Delta G^{*} / k T\right), \tag{1}
$$

where $I_{0} \sim 10^{28} \mathrm{~cm}^{-2} \mathrm{~s}^{-1}$. Two important quantities are the critical size embryo, $r^{*}$, and the critical free energy fluctuation, $\Delta G^{*}$, needed to create such an embryo. In standard nucleation treatments, the ledge energy per unit length, $\gamma_{\ell}$, involved in 2D pill-box nucleation is considered to be a constant independent of embryo size which leads, for a circular cluster of radius $r$ and height $h$, to $r^{*}=\gamma_{\ell} / h \Delta G_{\mathrm{v}}$ and $\Delta G^{*}=\pi \gamma_{\ell}^{2} / h \Delta G_{\mathrm{v}}$, where $\Delta G_{\mathrm{v}}$ is the volume free energy change. When $\partial \gamma_{\ell} / \partial r \neq 0, r^{*}$ and $\Delta G^{*}$ can be significantly different from these values depending upon the magnitude of $\partial \gamma_{\ell} / \partial r$. It is found that $\Delta G^{*}$ decreases strongly as $\partial \gamma_{\ell} / \partial r$ increases so it is important to

![](./images/812446549941420032_1.jpg)

Fig. 1. Schematic illustration of strip and triangular clusters on a Si(111) surface; (a) and (c) are top views, while (b) and (d) are side views. The ledge lines run in the $\langle 0 \overline{1} 1\rangle$ directions with $\langle 2 \overline{1} \overline{1}\rangle$ normals.

0022-0248/87/$03.50 © Elsevier Science Publishers B.V. (North-Holland Physics Publishing Division)

get a good estimate of $\partial \gamma_{\partial} / \partial r$ to determine the value of $\Delta G_{v}$ needed for effective surface nuclea- tion.

In this paper, the effect of ledge-ledge interac- tion on surface nucleation for the Si(111) free surface is considered. Two forms of $\langle 2 \overline{1} \overline{1}\rangle$ ledge interaction structures have been studied: (1) an infinite monomolecular high strip of width $d_{T}$ and(2) a triangular pill-box of dimension $d_{T}$ both sitting on the (111) plane. These two shapes are illustrated in fig. 1. Because periodic boundary conditions (PBC) of spacing $L$ were used for these computations, one is actually considering the in- teraction of a periodic array of clusters having these two geometries at a cluster spacing $(L-d_{T})$.Thus, for each case, one is interested in $\gamma_{c}(d_{T}, L)$  as a function of both $d_{T}$ and $L$.

## 2. Computational procedures
In this work we used the following potential energy function (PEF),
$$\Phi=\Phi_{2}+\Phi_{3}, \quad(2 \mathrm{a})$$
where the two-body part, $\Phi_{2}$, was calculated using a (12, 6) Mie potential
$$\Phi_{2}=\frac{1}{2} \sum_{i} \sum_{\substack{j \\ i \neq j}} \epsilon\left[\left(\frac{r_{0}}{r_{i j}}\right)^{12}-2\left(\frac{r_{0}}{r_{i j}}\right)^{6}\right], \quad(2 b)$$
and $r_{i j}=|r_{i}-r_{j}| ; r_{0}$ denotes the equilibrium dis tance and $\epsilon$ the two body-energy at $r_{i j}=r_{0}$. The three-body part, $\Phi_{3}$, was calculated using theAxilrod-Teller triple dipole potential:
$$\Phi_{3}=\frac{1}{3!} \sum_{i} \sum_{j} \sum_{\substack{k \\ i \neq j \neq k}} z\left(\frac{1+3 \cos \theta_{i} \cos \theta_{j} \cos \theta_{k}}{\left(r_{i j} r_{i k} r_{j k}\right)^{3}}\right),$$
where $\theta_{i}, \theta_{j}, \theta_{k}$ and $r_{i j}, r_{i k}, r_{j k}$ represent the angles and sides of the triangle formed by three atoms i, j and k respectively, while the three-body intensity parameter is denoted by Z [3]. The parameter set used for the calculations is given in table 1 of ref. [4]. A statics technique was used for the calculations wherein the 3 lower puckered layers of figs. 1b and 1d are held rigid while the atoms in the upper 4 layers are allowed to moveduring relaxation. Generally about 350-1500 atoms were involved in the calculations.

The four distinct $\langle 2 \overline{1} \overline{1}\rangle$ ledges on Si(111) areillustrated in fig. 2. Each of the [211] and [211] ledges have an upper and a lower member depend- ing upon the direction of the last bond at theledges (see fig. 2). The lower and upper [211] ledges have one and three broken bonds, respec- tively, while both lower and upper [211] ledges have two broken bonds. As a ledge grows out- wards, it passes through successive upper, lower, upper, etc., states. Although one may only wish to obtain a time average result, and a single jogged ledge may have segments of both upper and lower ledge along its length, it is important to develop information concerning both states.

Using the ledge geometry of fig. 1a and 1b, four different configurations have been considered by permuting $[2 \overline{1} \overline{1}]$ and $[\overline{2} 11]$ with upper and

![](./images/812446549941420032_2.jpg)

Fig. 2. Unrelaxed structure of the four basic single-height ledges on the Si(111) surface. All ledges are parallel to the closest-packed $\langle 0 \overline{1} 1\rangle$ directions in the surface. They are labeled according to their outward normal direction, either $[2 \overline{1} \overline{1}]$ or[211].

lower and with the two ledges of the strip being dissimilar. For such a system, the excess energy, $E_{\text{ex}}$, associated with formation of the pair of ledges, is given by

$$
\begin{aligned}
E_{\mathrm{ex}} & =E_{\mathrm{T}}-N \Phi_{\mathrm{B}}-A \gamma_{\mathrm{f}} & & (3 \mathrm{a}) \\
& =\left(\gamma_{\ell 1}+\gamma_{\ell 2}\right) D_{\ell}, & & (3 \mathrm{~b})
\end{aligned}
$$

where $E_{\mathrm{T}}$ is the total energy of the simulation of $N$ atoms, $\Phi_{\mathrm{B}}$ is the bulk cohesive energy per atom ($\Phi_{\mathrm{B}}=-5.469$ eV), $A$ is the total surface area, while $\gamma_{\mathrm{f}}$ is the surface free energy of the flat (111) face ($\gamma_{\mathrm{f}}=1019$ erg/cm²). $\gamma_{\ell 1}$ and $\gamma_{\ell 2}$ are the excess energies for ledge 1 and ledge 2, respectively, and $D_{\ell}$ is the length of the ledge involved in this simulation. In order to compute $\gamma_{\ell 1}$ and $\gamma_{\ell 2}$ separately, the computational cell is divided into two parts as indicated in Fig. 1b. For each part, one can write

$$
\gamma_{\ell i}=\frac{1}{D_{\ell}}\left(E_{i}-N_{i} \Phi_{\mathrm{B}}-A_{i} \gamma_{\mathrm{f}}\right), \quad i=1,2, \quad(4 \mathrm{a})
$$

with

$$
A_{1}+A_{2}=A, \quad N_{1}+N_{2}=N, \quad E_{1}+E_{2}=E_{\mathrm{T}}. \quad(4 \mathrm{~b})
$$

There obviously exists some arbitrariness concerning the position of the dividing line separating subsystem 1 from subsystem 2, so we choose the position giving $A_{1}=A_{2}=A / 2$.

For the calculations involving the triangular pill-box bounded by $\langle 2 \overline{1} \overline{1}\rangle$ ledges, only two different types of triangle are possible, the $[2 \overline{1} \overline{1}]$ and $[\overline{2} 11]$ ledge triangles. For the lower energy case, the excess energy following eq. (3a), has been calculated as a function of $d_{\mathrm{T}}$ and $L$.

## 3. Results and discussion

### 3.1. Infinite strip terrace

The relaxed configurations and surface parallel stress distributions for two ledge pairs are shown in figs. 3 and 4 and the ledge excess energies as a function of ledge spacing $d_{\mathrm{T}}$ are plotted in fig. 5. In fig. 5, the legend ledge 1/ledge 2 next to each curve means that the ledge 1 energy is being determined while the spacing to ledge 2 is changing. At large spacings, these energies converge to $-0.050,0.051,0.146$ and $0.251 \mathrm{eV} / \AA$ for the upper $[2 \overline{1} \overline{1}]$, upper $[\overline{2} 11]$, lower $[2 \overline{1} \overline{1}]$ and lower $[\overline{2} 11]$ ledge, respectively. The upper ledges are of lower energy than the lower ledges and the two $[2 \overline{1} \overline{1}]$ ledges are of lower energy than their respective $[\overline{2} 11]$ counterparts by about the same amount, e.g., $0.101 \mathrm{eV} / \AA$ for the upper ledges and $0.105 \mathrm{eV} / \AA$ for the lower ledges. The discrepancies found between these values and those of Pearson et al [1] are mainly due to the difference in convention used to define the excess ledge energy.

![](./images/812446549941420032_3.jpg)

The negative excess energy for the upper $[2 \overline{1} \overline{1}]$ ledge at large ledge spacings implies a benefical

![](./images/812446549941420032_4.jpg)

Fig. 4. (a), (b) Relaxed structures of the $[2 \overline{1} \overline{1}]_{U}$ ledge (RHS) and the $[\overline{2} 11]_{U}$ ledge (LHS) at a spacing of $29.93 \AA$. (c), (d) Same as fig. 3.

![](./images/812446549941420032_5.jpg)

Fig. 5. Ledge energies, $\gamma_{\ell}$ versus ledge spacing, $d_{T}$, for a variety of ledge pairs. The legend Ledge 1/Ledge 2 corresponds to ledge 1 energy as the spacing to ledge 2 is changed.

face reconstruction in the vicinity of the ledge compared to that found for the flat (111) surface without ledges. Spontaneous formation of such ledges cannot occur without concurrent formation of adjacent ledges to complete the cluster and this could make the net energy change positive. However, the net cluster formation energy would probably be small and such clusters would be highly favored during a surface nucleation process.

To convert the surface parallel stresses of figs. 3 and 4 to $eV / \AA^{3}$, one needs to divide by the atomic volume of silicon $(20.02 \AA^{3})$ so that $1 eV /$ atom $=$ $0.05 eV / \AA^{3}=1.15 \times 10^{6}$ psi. Only the stresses for the atoms of the first puckered layer in the region around and in the raised terrace are shown. The empty and shaded bars correspond to the upper and lower atoms of the puckered layer, respectively. The dashes in the central portion of the plots correspond to the stress on the upper and lower atoms of the first puckered layer of the ideal(111) surface, i.e., $-0.83$ and $-1.53 eV /$ atom, respectively. The stress relaxation is more important on the upper terrace than on the lower region so the ledges appear to interact with each other through these upper terrace atoms. Comparing figs. $3 b$ and $4 b$, the interaction/stress relaxation effect is seen to be more important for the upper ledges. In fig. $4 ~b$, one sees the ledge atoms stretching the upper terrace bonds in their attempt to partially bond with the atoms of the lower terrace. Since the earlier work of Pearson [2] showed that a $0.5 \%$ tensile strain applied to an ideal flat $Si(111)$ surface lowered $\gamma_{f}$ by about $5 \%$, one can expect such a stretching reaction at the ledge to lower $\gamma_{\ell}$ since any excess energy effects are associated with $\gamma_{\ell}$. All the ledge interactions presented here are repulsive in character exceptfor the lower $[\overline{2} 11]$ interacting with the upper $[2 \overline{1} \overline{1}]$  which is attractive.

In the context of crystal growth, a moving perfect ledge must pass periodically through upper

and lower states while, at the crystal growth temperature, it is likely that any ledge contains segments of upper and lower states for entropic reasons. Thus, movement of a real ledge is likely to involve only very small fluctuations in average ledge energy. For this reason, the average ledge excess energy in a particular direction is the meaningful quantity for growth processes. Neglecting configurational entropy effects, this is given by

$$
\bar{\gamma}_{\ell}^{j}=\frac{1}{2}\left(\gamma_{\ell \mathrm{U}}^{j}+\gamma_{\ell \mathrm{L}}^{j}\right), \quad(5)
$$

where the subscripts U and L refer to upper and lower, respectively. Fig. 6 shows $\bar{\gamma}_{\ell}^{j}$ versus ledge spacing for $j=[2 \overline{1} \overline{1}]$ and $[\overline{2} 11]$ ledges. The extrapolated values at large spacing are 0.050 and $0.150 \mathrm{eV} / \AA$ for the $[2 \overline{1} \overline{1}]$ and $[\overline{2} 11]$ ledges, respectively.

### 3.2. Triangular terrace

In fig. $7 \mathrm{a}$, a cluster made from the $[2 \overline{1} \overline{1}]_{\mathrm{U}}$ ledges is illustrated. The three corner atoms behave as atoms of a $[\overline{2} 11]_{\mathrm{U}}$ ledge because of their bonding configuration and thus raise the cluster energy. Allowing removal of these corner atoms as in fig. $7 \mathrm{~b}$ and surface relaxation as in fig. $7 \mathrm{c}$ leads to a completely stable $[2 \overline{1} \overline{1}]_{\mathrm{U}}$ ledge configuration for all ledge atoms around the cluster. It is interesting to note that this corner atom relaxation behavior is independent of cluster size as illustrated in figs. $7 \mathrm{~d}$ and $7 \mathrm{e}$.

![](./images/812446549941420032_6.jpg)

In this study, to determine the size effect on the formation energy of the cluster, simulations were performed at infinite cluster separation. This is accomplished by not applying the PBCs to the cluster atoms, but by applying them to all the lower atoms. It is expected that, as $d_{\mathrm{T}}$ increases, the excess energy per cluster atom should converge to some nominal value. The same behavior should be true for the ledge excess energy. For the latter, one might even expect $\gamma_{\ell}$ to converge to the value of $-0.050 \mathrm{eV} / \AA$ found in fig. 5 for the $[2 \overline{1} \overline{1}]_{\mathrm{U}}$ ledge; however, the cluster configuration keeps this from happening. In fig. 8, the excess energy, $\Delta E_{\mathrm{ex}}$, per cluster atom is plotted versus the total number of atoms, $N_{\mathrm{c}}$, in the cluster, while the ledge excess energy, $\gamma_{\ell}$, is also plotted versus the total ledge length $3 d_{\mathrm{T}}$ and one sees that this latter decreases with $N_{\mathrm{c}}$ out to $N_{\mathrm{c}} \sim 200$ atoms and converges to $\sim 0.039 \mathrm{eV} / \AA$. If $\gamma_{\ell}$ were constant, independent of cluster size, then it can be readily shown for an equilateral triangle shaped cluster that the total cluster energy, $E_{\mathrm{ex}}$, is given by

$$
E_{\mathrm{ex}}=3 d_{\mathrm{T}} \gamma_{\ell}=\frac{6}{3^{1 / 4}}\left(\frac{\Omega}{h}\right)^{1 / 2} \gamma_{\ell} N_{\mathrm{c}}^{1 / 2}=E_{0} N_{\mathrm{c}}^{1 / 2}, \quad(6)
$$

where $\Omega$ is the atomic volume. In fig. $9, E_{\mathrm{ex}}$ is plotted versus $N_{\mathrm{c}}^{1 / 2}$ and can be compared with the $E_{0}$ value which utilizes $\gamma_{\ell}(\infty)=0.039 \mathrm{eV} / \AA$. From this result one notes that, at intermediate $N_{\mathrm{c}}, E_{\mathrm{ex}}$ is larger than that expected for the $\gamma_{\ell}=$ constant case by $\sim 10 \%-15 \%$. The interesting domain occurs for small $N_{\mathrm{c}}$ where one notes that $E_{\mathrm{ex}}$ grows at a rate much faster than the $E_{0}$ curve, shown with a dashed line, up to $N_{\mathrm{c}}=6$ and then drops to a negative value at $N_{\mathrm{c}}=13$ before rising again at larger $N_{\mathrm{c}}$ values. The $N_{\mathrm{c}}=6$ and 13 cases correspond to a single and a triple hexagon-shaped cluster (non-triangle), that relax to $7 \mathrm{f}$ and $7 \mathrm{c}$, respectively. Thus the slightly negative energy for the $N_{\mathrm{c}}=13$ case arises because of the significant cluster surface reconstruction for this particular cluster size.

![](./images/812446549941420032_7.jpg)

Fig. 7. Triangular clusters on Si(111): (a) unrelaxed cluster; (b) unrelaxed cluster of (a) type with corner atoms removed; (c) relaxed cluster of (b) type; (d), (e) larger relaxed cluster of (b) type; (f) relaxed 6 atom cluster.

![](./images/812446549941420032_8.jpg)

To appreciate the importance of the $\partial \gamma_{l} / \partial d_{T}$ variations on 2D pill-box nucleation, the mathe matics is first developed in the appendix. Since the free energy fluctuation needed for 2D cluster for- mation is given by
$$\Delta G=N_{\mathrm{c}}\left(\Delta E_{\mathrm{ex}}-\Delta G_{\mathrm{v}}\right),\qquad(7)$$
the data of fig. 8 or 9 can be utilized directly to plot $\Delta G$ versus $N_{c}$ for a range of supersaturation, $\sigma$ . This result, for a temperature of 1000 K, is given in fig. 10 where one notes the existence of

Fig. 8. Calculated energies for clusters: excess energy per cluster atom, $\Delta E_{ex}$ , versus total number of cluster atoms, $N_{c}$ , and ledge energy, $\gamma_{l}$ , as a function of total cluster perimeter, $3 d_{T}$ .

![](./images/812446549941420032_9.jpg)

Fig. 9. Total cluster excess energy, $E_{\text{ex}}$, as a function of $N_{\text{c}}^{1/2}$.

![](./images/812446549941420032_10.jpg)

Fig. 10. Free energy fluctuation, $\Delta G$, for cluster formation as a function of $N_{\text{c}}^{1/2}$, for several surface adatom supersaturation, $\sigma$, at a temperature of 1000 K.

two maxima, one at $N_{\text{c}}=6$ and the second at larger $N_{\text{c}}$ depending upon the magnitude of $\sigma$. One notes also that the second maximum is equal or to less than the first provided that $\sigma \geq \sigma_{\text{c}}=\exp$ $(0.018/kT)$, e.g., 1.235 at 1000 K. Thus, for this important range of $\sigma$, the primary barrier to nucleation occurs with the formation of the $N_{\text{c}}=6$ cluster, i.e.,

$$
\Delta G^{*}=E_{\text{ex}}(6)-6kT\ \ln(\sigma). \tag{8a}
$$

This compares with the $\gamma_{\ell}=$ constant case of

$$
\Delta G^{*}=E_{0}^{2}/4kT\ \ln(\sigma). \tag{8b}
$$

Using eqs. (8a) and (8b) in eq. (1), one can compare the change in nucleation frequency due to the ledge interaction effects, i.e.,

$$
\ln\left(\frac{I_{\text{a}}}{I_{\text{b}}}\right)=\frac{E_{0}^{2}}{(2kT)^{2}\ln(\sigma)}+6\ln(\sigma)-\frac{E_{\text{ex}}^{*}(6)}{kT} \tag{9}
$$

for $\sigma > \sigma_{\text{c}}$ where the subscripts a and b refer to eqs. (8a) and (8b), respectively. In fig. $11, \ln(I_{\text{a}}/I_{\text{b}})$ is plotted versus $\sigma$ and one can see that the barrier to the formation of the hexamer cluster significantly lowers the nucleation frequency for (111) silicon.

The Si PEF used for the foregoing calculations is the simplest one available in the literature that includes three-body effects and, although it has been fairly successful in the prediction of more than 25 different Si material properties, it has a real weakness with respect to the elastic properties [2,5]. This is because it contains only three parameters. Of the alternate semiempirical PEFs available today [6-8], these involve 7 [6] to 18 [7] parameters, making them les tractable for the types of large scale computations utilized here. Of course, none of the presently available PEFs, except perhaps the Tersoff PEF [8], are able to predict the correct $(7 \times 7)$ reconstruction pattern for Si(111) as all are flawed in one way or another.

At the moment, each semiempirical PEF that one might use for the type of calculation has its strengths and weaknesses but insufficient experience is available yet to catalogue their applicability in a given situation. Perhaps it is best to look

![](./images/812446549941420032_11.jpg)

Fig. 11. Calculated relative nucleation frequency, $I_{\mathrm{a}} / I_{\mathrm{b}}$, for the $(\gamma, \neq$ constant case $) /(\gamma,=$ constant $)$ case, as a function of supersaturation, $\sigma$, for $\mathrm{Si}(111)$ at several temperatures.

at each as the analogue of a particular experimen- tal technique that provides a measurement with a certain error bar. Refinement of the technique tends to reduce the error bar.

Granted, one does not know the magnitude of the error bar generated by using a particular PEF, so numerical calculations like those presented here should be treated with caution until substantiated in some alternate fashion. Thus, although the qualitative trends of this paper are completely valid, the error bars to be placed on the numerical magnitudes are presently unknown.

## Acknowledgements

This work was supported in part by the De- fense Advanced Research Projects Agency under Contract No. MDA 903-84-K-0100, in part by NASA AMES Research Center which provided the computational facilities via Grant No. NCC2-297 and, in part by the NSF-MRC Program through the Center for Materials Research at Stanford University.

## Appendix. Two-dimensional pill-box nucleation

### A.1. Conventional case $(\gamma_{l}=$ constant $)$

The free energy fluctuation, $\Delta G$, needed for 2D cluster formation is given by

$$\Delta G=N_{\mathrm{c}}\left(\Delta E_{\mathrm{ex}}-\Delta G_{\mathrm{v}}\right) \tag{A.1a}$$

where

$$\Delta E_{\mathrm{ex}}=E_{0} N_{\mathrm{c}}^{-1 / 2}, \quad \Delta G_{\mathrm{v}}=k T \ln (\sigma), \tag{A.1b}$$

and where $\Delta E_{\mathrm{ex}}$ is the surface excess energy per cluster atom, $N_{\mathrm{c}}$ is the number of cluster atoms, $\Delta G_{\mathrm{v}}$ is the driving force for clustering and $\sigma=$ $C / C^{*}$ is the Si adatom supersaturation at con- centration $C$ and equilibrium concentration $C^{*}$. Differentiating eq. (A.1a) with respect to $N_{\mathrm{c}}$ leads to

$$N_{\mathrm{c}}^{*}=\left(\frac{E_{0}}{2 \Delta G_{\mathrm{v}}}\right)^{2}, \quad \Delta G^{*}=\frac{E_{0}^{2}}{4 \Delta G_{\mathrm{v}}}. \tag{A.1c}$$

### A.2. General case $(\gamma_{l} \neq$ constant $)$

In this case, when eq. (A.1a) is differentiated with respect to $N_{\mathrm{c}}$, a different result is obtained because now $E_{\mathrm{ex}}$ is an unknown function of $N_{\mathrm{c}}$. This leads to

$$N_{\mathrm{c}}^{*}=\frac{1}{s}\left[\Delta G_{\mathrm{v}}-\Delta E_{\mathrm{ex}}\left(N_{\mathrm{c}}^{*}\right)\right], \tag{A.2a}$$

$$\Delta G^{*}=\frac{1}{s}\left[\Delta G_{\mathrm{v}}-\Delta E_{\mathrm{ex}}\left(N_{\mathrm{c}}^{*}\right)\right]^{2}, \tag{A.2b}$$

where

$$s=\frac{\partial \Delta E_{\mathrm{ex}}}{\partial N_{\mathrm{c}}}\left(N_{\mathrm{c}}^{*}\right).$$

Considering eqs. (A.2), we note two cases; (1) $s<0$, as in $\operatorname{Si}(111)$, leads to $E_{\mathrm{ex}}\left(N_{\mathrm{c}}^{*}\right)>\Delta G_{\mathrm{v}}$ needed for $N_{\mathrm{c}}^{*}>0$ and (2) $s>0$ requires $E_{\mathrm{ex}}\left(N_{\mathrm{c}}^{*}\right)<\Delta G_{\mathrm{v}}$ and the maximum value of $\Delta G^{*}$ is $\Delta G^{*}=0$ so that spontaneous clustering will occur

for this case. For case (1), if one sets $\Delta E_{\mathrm{ex}} = E_{0}N_{\mathrm{c}}^{-m}$, then $m>1/2$ corresponds to $\mathrm{Si}(111)$ while $0<m<1/2$ appears to correspond to $\mathrm{GaAs}(00\overline{1})$.

## References

[1] E. Pearson, T. Halicioğlu and W.A. Tiller, Surface Sci. 168 (1986) 46.

[2] E. Pearson, Computer Modeling of Atomic Interaction with Applications to Silicon, PhD Thesis, Departement of Materials Science and Engineering, Stanford University (March 1985).

[3] E. Pearson, T. Takai, T. Halicioğlu and W.A. Tiller, J. Crystal Growth 70 (1984) 33.

[4] T. Takai, T. Halicioğlu and W.A. Tiller, Surface Sci. 164 (1985) 341.

[5] S. Erkoc, T. Halicioğlu and W.A. Tiller, J. Non-Crystalline Solids, in press.

[6] F. Stillinger and T. Weber, Phys. Rev. B31 (1985) 5262.

[7] R. Biswas and D.R. Hamann, Phys. Rev. Letters 55 (1985) 2001.

[8] J. Tersoff, Phys. Rev. Letters 56 (1986) 632.