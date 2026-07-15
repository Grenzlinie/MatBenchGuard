# First-Principles WDA Calculations for Ferroelectric Materials

Zhigang Wu*, Ronald E. Cohen* and David J. Singh†

*Carnegie Institution of Washington, Washington DC 20015
†Naval Research Laboratory, Washington DC 20375

Abstract. First-principles calculations within the weighted density approximation (WDA) were performed for some common ferroelectric materials. We used a plane-wave basis, the Perdew-Wang pair-distribution function, and shell partitioning. Compared with the local density approximation (LDA), the WDA significantly improves the equilibrium volume of these materials, but it overesti- mates the ferroelectric instability in $BaTiO_3$ and $PbTiO_3$. We fixed this failure by imposing a better sum rule based on shell partitioning. Because an orbital-dependent xc potential is introduced, shell partitioning complicates calculation of atomic forces. We also investigated a hybrid WDA method, in which WDA is mixed with LDA.

## I. INTRODUCTION

Since the early 1980s, first-principles calculations based on the density functional theory (DFT) [1] have been implemented to compute diverse properties of piezoelectric and ferroelectric materials. The main difficulty within DFT is how to treat the exchange- correlation (xc) energy, because the exact form of it remains unknown. The local density approximation (LDA) [1], in which the xc energy density depends only on local charge density, dominated these calculations due to its simplicity and surprising success. When performed at the experimental volume, the LDA predicts many properties of ferroelectric materials, such as phonon frequencies, ferroelectric transitions, polarization, elasticity, etc., with extraordinary accuracy [2]. The amazing success of the LDA is attributed to the partial cancellation of the errors of the exchange and correlation parts. But the LDA gives equilibrium volumes a few percent less than experiment, and ferroelectric properties are extremely sensitive to volume. For example, the ferroelectric instability in $BaTiO_3$ [3] and $KNbO_3$ [4, 5, 6, 7, 8, 9] are severely reduced, if not totally eliminated, in calculations done at the LDA zero pressure volume. Furthermore, even at the experimental volume, the LDA may incorrectly predict certain properties, e.g., overestimation of dielectric constants $\varepsilon_\infty$ [10, 11, 12], and underestimation of band gaps [13, 14].

The generalized gradient approximation (GGA) [15, 16], which uses both local the density and the local density gradients, is among several approaches beyond LDA. Generally speaking, the semi-local GGA tends to improve upon the LDA in many aspects, such as atomic energies and structural energy differences [16, 19, 20]. On the other hand, the GGA often over-corrects the LDA [21, 8]. Here we did a full relaxation of tetragonal $PbTiO_3$ within both the LDA (Hedin-Lundqvist [22]) and the GGA (PBE [16]) using the LAPW+LO method [23]. As seen in Table 1, at the experimental volume,

CP677, *Fundamental Physics of Ferroelectrics 2003*, edited by P. K. Davies and D. J. Singh
© 2003 American Institute of Physics 0-7354-0146-2/03/$20.00

<table><caption>TABLE 1. Fully relaxed structure of tetragonal $P4mm$ PbTiO$_3$ with the LDA and the GGA. Volumes are in $\AA^3$, and the numbers in parentheses are the deviations of strain (6.35%) and volume from experiment.</caption>
<tbody>
<tr>
<td>
</td>
<td>
volume (Expt.)
</td>
<td>
$c/a$
</td>
<td>
volume (Relaxed)
</td>
<td>
$c/a$
</td>
</tr>
<tr>
<td>
LDA
</td>
<td>
63.28
</td>
<td>
1.11 (+80%)
</td>
<td>
60.36 (-4.6%)
</td>
<td>
1.051(-20%)
</td>
</tr>
<tr>
<td>
GGA
</td>
<td>
63.28
</td>
<td>
1.068 (+7%)
</td>
<td>
70.3 (+11%)
</td>
<td>
1.22 (+250%)
</td>
</tr>
</tbody>
</table>

the GGA predicts a better strain than the LDA; however, the fully relaxed GGA structure seems even worse than that of the LDA. But the LDA also has problems because the LDA optimized volume is about 4.6 percent less than experiment. The failures of LDA and GGA calculations indicate that more complicated non-local functionals are needed to include the contributions beyond the semi-local approximation.

The weighted density approximation (WDA) [17, 18, 24], within which the xc energy density depends on charge density over a finite region, was advanced in the late 1970’s. The WDA assumes that any inhomogeneous electron gas can be regarded as continuously being deformed from a homogeneous electron gas, so the real pair-distribution function of the inhomogeneous gas is replaced by that of a homogeneous gas with the weighted density. By constructing a model xc hole, the weighted density at every point is determined; then the xc energy and xc potential are determined. Because it is complicated, computationally demanding, and also because of the success of the simpler LDA and GGA, the WDA has not attracted much attention until recently. However, the WDA is promising for predicting very accurate volumes so that true first-principles calculation can be done without relying on experiment. The first ferroelectric material calculated with WDA is KNbO$_3$ [9, 25]. An equilibrium volume in very good agreement with experiment was obtained in that study.

In this paper, a brief overview of WDA formalism is presented first. Then we report the successes and failures based on our first-principles WDA calculations of ground state properties of some of the most common ferroelectric materials in section III. In section IV we suggest improvements to overcome these failures. In section V, an ad hoc WDA hybrid approach is proposed and used to optimize the structure of tetragonal PbTiO$_3$.

## II. FORMALISM

The general form of the xc energy of DFT scheme can be expressed in Rydberg units as

$$
E_{\mathrm{xc}}[n]=\int n(\mathbf{r}) d \mathbf{r} \int \frac{n_{\mathrm{xc}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} d \mathbf{r}^{\prime}, \tag{1}
$$

where the xc hole density $n_{\mathrm{xc}}(\mathbf{r},\mathbf{r}')$ is defined by the pair-distribution function $g_{\mathrm{xc}}(\mathbf{r},\mathbf{r}')$,

$$
n_{\mathrm{xc}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)=n\left(\mathbf{r}^{\prime}\right)\left[g_{\mathrm{xc}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)-1\right], \tag{2}
$$

and the xc hole satisfies

$$
\int n_{\mathrm{xc}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right) d \mathbf{r}^{\prime}=-1. \tag{3}
$$

Unfortunately the form of $g_{\rm xc}(\mathbf{r},\mathbf{r}')$ is in general unknown. However, based on Monte Carlo simulations it is known with high accuracy for the uniform gas [26]. In the WDA, as mentioned, the unknown general $g_{\rm xc}(\mathbf{r},\mathbf{r}')$ is replaced by $G$ of a homogeneous gas with the weighted density $\bar{n}$,

$$
g_{\rm xc}(\mathbf{r},\mathbf{r}')-1=G[|\mathbf{r}-\mathbf{r}'|,\bar{n}(\mathbf{r})],
\tag{4}
$$

where $\bar{n}$ is fixed by the sum rule:

$$
\int n(\mathbf{r}')G[|\mathbf{r}-\mathbf{r}'|,\bar{n}(\mathbf{r})]d\mathbf{r}'=-1.
\tag{5}
$$

The corresponding WDA xc energy is

$$
E_{\rm xc}[n]=\iint \frac{n(\mathbf{r})n(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}G[|\mathbf{r}-\mathbf{r}'|,\bar{n}(\mathbf{r})]d\mathbf{r}d\mathbf{r}'.
\tag{6}
$$

Equation 5 assures lack of self-interaction in the one-electron limit. This corrects what is believed to be one of the key problems of the LDA.

The function $G$ of homogeneous gas was parametrized by Perdew and Wang (P-W) [26]. As a matter of fact, one may speculate that other choices of $G$ could be better in actual materials [28]. For example, the Gunnarsson-Jones (G-J [28]) and Gritsenko et al. (GRBA [29]) ansatz are:

$$
G^{\rm G\{{}^{J}}(r,n)=c_{1}(n)\}1-\exp(-[\frac{r}{c_{2}(n)]\{}^{5}),
\tag{7}
$$

$$
G^{\rm GRBA}(r,n)=c_{1}(n)\exp(-[\frac{r}{c_{2}(n)}]^{1-\frac{1}{3}}).
\tag{8}
$$

The parameters $c_{1}$ and $c_{2}$ can be determined from the following conditions:

$$
n\int G(r,n)d^{3}r=-1
\tag{9}
$$

$$
n\int \frac{G(r,n)}{r}d^{3}r=\varepsilon_{\rm xc}(n).
\tag{10}
$$

$\varepsilon_{\rm xc}(n)$ is the xc energy density of a uniform gas with density $n$.

The xc potential $v_{\rm xc}(\mathbf{r})$ is the functional derivative of $E_{\rm xc}$,

$$
v_{\rm xc}(\mathbf{r})=v_{1}(\mathbf{r})\ \ \ v_{2}(\mathbf{r})\ \ \ v_{3}(\mathbf{r}),
\tag{11}
$$

where

$$
v_{1}(\mathbf{r})=\int \frac{n(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}G[|\mathbf{r}-\mathbf{r}'|,\bar{n}(\mathbf{r})]d\mathbf{r}',
\tag{12}
$$

$$
v_{2}(\mathbf{r})=\int \frac{n(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}G[|\mathbf{r}-\mathbf{r}'|,\bar{n}(\mathbf{r}')]d\mathbf{r}',
\tag{13}
$$

$$
v_{3}(\mathbf{r})=\iint \frac{n\left(\mathbf{r}^{\prime}\right) n\left(\mathbf{r}^{\prime \prime}\right)}{\left|\mathbf{r}^{\prime}-\mathbf{r}^{\prime \prime}\right|} \frac{\delta G\left[\left|\mathbf{r}^{\prime}-\mathbf{r}^{\prime \prime}\right|, \bar{n}\left(\mathbf{r}^{\prime}\right)\right]}{\delta n(\mathbf{r})} d \mathbf{r}^{\prime} d \mathbf{r}^{\prime \prime}.
\tag{14}
$$

Examination of the above suggests that implementation of the WDA xc energy density and potential could be cumbersome. However, in a plane-wave representation, by using the convolution theorem, these terms can be evaluated efficiently, as detailed in Ref. [27].

One subtle issue in WDA implementations is shell partitioning [24]. In the WDA the range of integration of $G$ is similar to the size of atoms, and there is no distinction between core and valence electrons, so core and valence electrons dynamically screen valence electrons equally, which is unphysical. As a result, the inter-shell contribution to xc energy would be exaggerated. On the other hand, the LDA can give correct inter-shell contributions, since the LDA depends only on the local density, and outside the core region, the core density vanishes. Based on this observation, a shell partitioning approach was proposed [24, 27], in which the valence-valence interactions are treated with the WDA, while core-core and core-valence interactions are based on the LDA. The total xc energy and potential are

$$
E_{\mathrm{xc}}[n]=E_{\mathrm{xc}}^{\mathrm{LDA}}[n] \quad E_{\mathrm{xc}}^{\mathrm{WDA}}\left[n_{v}\right]-E_{\mathrm{xc}}^{\mathrm{LDA}}\left[n_{v}\right],
\tag{15}
$$

$$
v_{\mathrm{xc}}(\mathbf{r})=v_{\mathrm{xc}}^{\mathrm{LDA}}[n(\mathbf{r})] \quad v_{\mathrm{xc}}^{\mathrm{WDA}}\left[n_{v}(\mathbf{r})\right]-v_{\mathrm{xc}}^{\mathrm{LDA}}\left[n_{v}(\mathbf{r})\right],
\tag{16}
$$

where $n_{v}$ is the valence density and $n$ is the total density. For simplicity, the WDA sum rule of this scheme becomes

$$
\int n_{v}\left(\mathbf{r}^{\prime}\right) G\left[\left|\mathbf{r}-\mathbf{r}^{\prime}\right|, \bar{n}(\mathbf{r})\right] d \mathbf{r}^{\prime}=-1,
\tag{17}
$$

as if the valence states were separated from the core states. In this paper, the semi-core states of metal ions and the O $2s$ states are treated with LDA, the higher states with the WDA, and the lower states are pseudized.

## III. GROUND-STATE CALCULATIONS

The WDA was implemented [27] within a plane-wave basis pseudopotential method using hard Troullier-Martins pseudopotentials [30]. The semi-core states of metal ions include $3s$ and $3p$ states of K and Ti, $4s$ and $4p$ states of Nb and Sr, $5s$ and $5p$ states of Ta and Ba, and $5d$ states of Pb. Plane-wave basis sets with a cut-off of 132 Ry were used to assure convergence. A standard 3-point interpolation was employed to obtain $\bar{n}(\mathbf{r})$ with a logarithmic grid of increment $\bar{n}_{i\ +1}=1.25 \bar{n}_{i}$.

We first calculated the lattice constant of five ferroelectric materials, namely $\mathrm{KNbO}_{3}$, $\mathrm{KTaO}_{3}, \mathrm{SrTiO}_{3}, \mathrm{BaTiO}_{3}$, and $\mathrm{PbTiO}_{3}$, constrained with cubic symmetry. As mentioned before, the LDA lattice constant is about 1-2% less than experiment, and this small error makes many ferroelectric properties incorrect. As shown in Table 2, the WDA with the P-W form of $G$ dramatically improves the lattice constant over the LDA. Actually all these WDA lattice parameters are very close to experimental data except that of $\mathrm{PbTiO}_{3}$.

<table>
<caption>TABLE 2. Calculated LDA and WDA lattice constants in Å within for some ferroelectric materials in cubic state, compared with experimental data. The Perdew-Wang form of $G$ was used in WDA. Numbers in parentheses are the percentage deviations from experiment.</caption>
<tbody><tr><th>material</th><th>LDA</th><th>WDA</th><th>Expt.</th></tr>
<tr><td>KNbO₃</td><td>3.96 (-1.6)</td><td>4.02 (-0.0)</td><td>4.016</td></tr>
<tr><td>KTaO₃</td><td>3.92 (-1.6)</td><td>3.98 (-0.1)</td><td>3.983</td></tr>
<tr><td>SrTiO₃</td><td>3.86 (-1.2)</td><td>3.92 (+0.4)</td><td>3.905</td></tr>
<tr><td>BaTiO₃</td><td>3.95 (-1.2)</td><td>4.01 (+0.3)</td><td>4.000</td></tr>
<tr><td>PbTiO₃</td><td>3.98 (-2.1)</td><td>3.93 (-1.0)</td><td>3.969</td></tr>
</tbody></table>

Then we checked the ferroelectric instability in rhombohedral $KNbO_{3}$ and $BaTiO_{3}$, and tetragonal $PbTiO_{3}$. We used a $6\times 6\times 6$ special k-point sampling since the energy difference in $KNbO_{3}$ and $BaTiO_{3}$ is small, only several mRy/cell. We displaced atom positions according to the experimental distortion patterns, and we performed frozen-phonon calculations at the experimental structures within both LDA (plane-wave and LAPW) and WDA (P-W). We used cubic cells with lattice constants of $4.000$ Åand $4.016$ Åfor KNbO $_{3}$ and $BaTiO_{3}$, respectively. The rhombohedral distortion of the lattice parameters from the pseudo-cubic structure in these materials is very small, and was neglected. For tetragonal $PbTiO_{3}$, $c/a=1.0635$ and $V=63.28$ Å$^{3}$.

As mentioned, the LDA describes the ferroelectric instability very well at the experimental volume, so one may hope that the WDA retains this desired feature. Fig. 1 shows the calculated LDA and WDA energy versus ferroelectric displacement curves. For $KNbO_{3}$, the LDA and WDA curves match pretty well, although the WDA energy difference is a little too small compared with the LDA. Our present $KNbO_{3}$ results agree with previous calculations [25]. For $BaTiO_{3}$ and $PbTiO_{3}$, the soft-mode amplitudes of the WDA are about $20\%$ larger than experiment, while those of LDA agree with experiment quite well, within about $5\%$. Meanwhile, the WDA energy diference is much bigger than in the LDA. This indicates an overestimation of the ferroelectric instability in $BaTiO_{3}$ and $PbTiO_{3}$. We also tried the G-J and GRBA forms of $G$, although they predict slightly better lattice constants of $PbTiO_{3}$ (3.94 Åfor G-J and 3.95 Åfor GRBA), their frozen-phonon results are even worse. This implies some difficulty in the present WDA scheme. Fortunately, this can be fixed.

### IV. A NEW WDA SUM RULE

As mentioned in the formalism section, the present WDA method includes shell partitioning, and the sum rule of Eq. 17 is used. This simple sum rule assumes valence states are separated from core states. But in the core region, this is not true. Considering that the core-valence xc interaction is treated with the LDA and valence-valence with WDA, one may write a new and more reasonable sum rule as:

$$
\int\left\{n_{v}\left(\mathbf{r}^{\prime}\right) G\left[\left|\mathbf{r}-\mathbf{r}^{\prime}\right|, \bar{n}(\mathbf{r})\right] \quad n_{c}(\mathbf{r}) G\left[\left|\mathbf{r}-\mathbf{r}^{\prime}\right|, n(\mathbf{r})\right]\right\} d \mathbf{r}^{\prime}=-1,
\tag{18}
$$

![](./images/812389278096031745_1.jpg)

FIGURE 1. Total energy as a function of soft-mode displacement in $KNbO_3$, $BaTiO_3$ and $PbTiO_3$, with
the LDA and the WDA. In the WDA the Perdew-Wang form of $G$ was used. Energy is in mRy, and $\delta$ is
the displacement relative to experiment. Calculations were done based on experimental structures.

which is similar to that proposed by Gunnarsson et. al. in Ref. [24]. The corresponding
total xc energy is:

$$
E_{\mathrm{xc}}[n]=E_{\mathrm{xc}}^{\mathrm{LDA}}[n] \iint \frac{n_{v}(\mathbf{r}) n_{v}\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} G\left[\left|\mathbf{r}-\mathbf{r}^{\prime}\right|, \bar{n}(\mathbf{r})\right]-\frac{n_{v}^{2}(\mathbf{r})}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} G\left[\left|\mathbf{r}-\mathbf{r}^{\prime}\right|, n(\mathbf{r})\right] d \mathbf{r} d \mathbf{r}^{\prime}. \tag{19}
$$

![](./images/812389278096031745_2.jpg)

FIGURE 2. Total energy as in Fig. 1, but the results of the WDA with the new sum rule are added.

Enforcing this new sum rule, we recalculated the lattice constants and frozen-phonon curves, and the results are shown in Table 3 and Fig. 2. The new WDA method still gives very good equilibrium volumes for these materials. Comparing with the previous WDA results, we found that the new WDA method reduces lattice constants a little bit. Now the new WDA frozen-phonon curves of all the three materials match with the LDA curves very well. This suggests that it is the sum rule of Eq. 17 that causes overestimation of the ferroelectric instability in $BaTiO_3$ and $PbTiO_3$.

<table>
<caption>TABLE 3. Calculated lattice constants as in Table 2 within the WDA with previous and the new sum rules. The Perdew-Wang form of $G$ was used.</caption>
<thead>
<tr>
<th>material</th>
<th>WDA</th>
<th>WDA (new)</th>
<th>Expt.</th>
</tr>
</thead>
<tbody>
<tr>
<td>KNbO₃</td>
<td>4.02 (-0.0)</td>
<td>4.01 (-0.1)</td>
<td>4.016</td>
</tr>
<tr>
<td>KTaO₃</td>
<td>3.98 (-0.1)</td>
<td>3.97 (-0.3)</td>
<td>3.983</td>
</tr>
<tr>
<td>SrTiO₃</td>
<td>3.92 (+0.4)</td>
<td>3.91 (+0.2)</td>
<td>3.905</td>
</tr>
<tr>
<td>BaTiO₃</td>
<td>4.01 (+0.3)</td>
<td>4.00 (+0.0)</td>
<td>4.000</td>
</tr>
<tr>
<td>PbTiO₃</td>
<td>3.93 (-1.0)</td>
<td>3.93 (-1.1)</td>
<td>3.969</td>
</tr>
</tbody>
</table>

## V. A HYBRID WDA METHOD

In order to optimize structures, it is very helpful to have the ability to efficiently calculate accurate atomic forces. Unfortunately shell partitioning complicates atomic force calculations in that it introduces an orbital-dependent xc potential, as seen in Eq. 16. As a result, the xc potential is not the xc energy derivative with respect to the total charge density, and the Hellmann-Feynman theory [31] does not directly apply [32].

On the other hand, it is straightforward to obtain atomic forces in a one-window (no shell partitioning) version of the WDA. But as mentioned before, one-window WDA is incorrect, and it predicts lattice constants way too large. However, we can regard one-window WDA as overusing non-local information, while the LDA does not use any non-local information, so the real system should be something in between. The simplest way is to put WDA and LDA together, and so we propose a hybrid WDA method consisting of direct mixing of the WDA and the LDA,

$$
E_{\mathrm{xc}}[n]=(1.0-\alpha) E_{\mathrm{xc}}^{\mathrm{LDA}}[n] \quad \alpha E_{\mathrm{xc}}^{\mathrm{WDA}}[n], \tag{20}
$$

where the only parameter $\alpha$ can be determined by fitting to the lattice constant calculated from shell partitioning WDA. This scheme is very similar to Becke's hybrid method [33], in which the xc energy is a direct mixture of the exact exchange energy and the GGA xc energy. In table 4 parameters $\alpha$ computed from fitting to data in Table 3 of the new WDA method are given. Interestingly, all $\alpha$ are about 28% except for PbTiO₃, and Becke's universal mixing parameter for the exact exchange part is also about 28% [33].

We used the hybrid WDA method with $\alpha=0.19$ to relax tetragonal PbTiO₃. The optimized atom positions for the experimental structure are in good agreement with experiment, as seen in Table 5. The optimized $c/a=1.09$ (50% larger) at the experimental volume. For the fully relaxed structure, we obtained a volume of about $65.8\ \mathring{\mathrm{A}}^3$ (4% larger), and $c/a=1.12$ (90% larger). Compared with the GGA data in Table 1, the current hybrid WDA method predicts a better fully optimized structure. The partial success of the ad hoc hybrid WDA method implies that the WDA could be improved by adding a discontinuous $\delta$ function to the normally continuous function $G$, and the corresponding xc energy will have an ordinary WDA part and an additional LDA-like contribution.

<table>
<caption>Table 4. Fitting parameters $\alpha$ in the hybrid WDA scheme.</caption>
<thead>
<tr>
<th>material</th>
<th>$KNbO_3$</th>
<th>$KTaO_3$</th>
<th>$SrTiO_3$</th>
<th>$BaTiO_3$</th>
<th>$PbTiO_3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\alpha$</td>
<td>0.28</td>
<td>0.28</td>
<td>0.30</td>
<td>0.27</td>
<td>0.19</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 5. Internal coordinates of tetragonal $P4mm$ $PbTiO_3$ for the experimental volume and strain. $u_z$ are given in terms of the lattice constant $c$. In hybrid WDA, the parameter $\alpha=0.19$.</caption>
<thead>
<tr>
<th> </th>
<th>LDA (LAPW)</th>
<th>LDA (PW)</th>
<th>WDA (hybrid)</th>
<th>Expt.</th>
</tr>
</thead>
<tbody>
<tr>
<td>$u_z$(Pb)</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>$u_z$(Pb)</td>
<td>0.538</td>
<td>0.545</td>
<td>0.543</td>
<td>0.538</td>
</tr>
<tr>
<td>$u_z(O_1,O_2)$</td>
<td>0.613</td>
<td>0.628</td>
<td>0.618</td>
<td>0.612</td>
</tr>
<tr>
<td>$u_z(O_2)$</td>
<td>0.105</td>
<td>0.122</td>
<td>0.114</td>
<td>0.117</td>
</tr>
</tbody>
</table>

## VI. CONCLUSIONS

We have investigated the WDA method by ground state calculations for some of the most common ferroelectric materials. In short, with the P-W uniform electron gas form of $G$ and shell partitioning, the WDA yields much better equilibrium volumes than LDA for these materials. But because of the sum rule of Eq. 17, the WDA overestimates the ferroelectric instability in $BaTiO_3$ and $PbTiO_3$, i.e., we found that the WDA double wells are wider and deeper than the LDA ones. We present a better sum rule in Eq. 18, and with it, the corresponding frozen-phonon curves match very well with the LDA curves in $KNbO_3$, $BaTiO_3$ and $PbTiO_3$. At the same time, the new WDA still yields very good lattice constants. In order to do structural relaxation, we proposed an ad hoc hybrid WDA method, in which WDA is directly mixed with LDA, to avoid the difficulty of atomic force calculations incurred by shell partitioning. We obtained the mixing parameter $\alpha$ from fitting, and finally we relaxed tetragonal $PbTiO_3$ using the hybrid WDA method. The optimized structure agrees fairly with experiment. This suggests a possible way to get rid of shell partitioning by adding a discontinuous $\delta$ function to the function $G$.

## ACKNOWLEDGMENTS

This work was supported by the Office of Naval Research under ONR Grants N00014-02-1-0506 and N0001403WX20028. Calculations were done on the Center for Piezoelectrics by Design (CPD) computer facility, and on the Cray SV1 supported by NSF and the Keck Foundation.

## REFERENCES

1. P. Hohenberg, and W. Kohn, Phys. Rev. 136, B864 (1964). W. Kohn, and L.J. Sham, Phys. Rev. 140, A1133 (1965).

2. See e.g., *Theory of ferroelectrics: A vision for the next decade and beyond*, R.E. Cohen, J. Phys. Chem. Solids **61**, 139-146 (1999).

3. R.E. Cohen, and H. Krakauer, Phys. Rev. B **42**, 6416 (1990). R.E. Cohen, Nature (London) **358**, 136 (1992). R.E. Cohen, and H. Krakauer, Ferroelectrics **136**, 65 (1992).

4. D.J. Singh, and L.L. Boyer, Ferroelectrics **136**, 95 (1992).

5. A.V. Postnikov, T. Neumann, G. Borstel, and M. Methfessel, Phys. Rev. B **48**, 5910 (1993) A.V. Postnikov, T. Neumann, and G. Borstel, Ferroelectrics **164**, 101 (1995).

6. R. Yu, and H. Krakauer, Phys. Rev. Lett. **74**, 4067 (1995).

7. C.-Z. Wang, R. Yu, and H. Krakauer, Ferroelectrics **194**, 97 (1997).

8. D.J. Singh, Ferroelectrics **164**, 143 (1995).

9. D.J. Singh, Ferroelectrics **194**, 299 (1997).

10. A. Dal Corso, S. Baroni, and R. Resta, Phys. Rev. B **49**, 5323 (1994).

11. R. Resta, Ferroelectrics **194**, 1 (1997).

12. S. Dallolio, R. Dovesi, and R. Resta, Phys. Rev. B **56**, 10105 (1997).

13. D.R. Hamann, Phys. Rev. Lett. **42**, 662 (1979).

14. M.T. Yin, and M.L. Cohen, **26**, 5668 (1982).

15. D.C. Langreth, and M.J. Mehl, Phys. Rev. B **28**, 1809 (1983). A.D. Becke, Phys. Rev. A **38**, 3098 (1988).

16. J.P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

17. O. Gunnarsson, M. Jonson, and B.I. Lundquist, Phys. Lett. **59A**, 177 (1976). O. Gunnarsson, M. Jonson, and B.I. Lundquist, Solid State Commun. **24**, 765 (1977).

18. J.A. Alonso, and L.A. Girifalco, Phys. Rev. B **17**, 3735 (1978).

19. J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, and C. Fiolhais, Phys. Rev. B **46**, 6671 (1992); **48**, 4978(E) (1993).

20. B. Hammer, K.W. Jacobsen, and J.K. Norskov, Phys. Rev. Lett. **70**, 3971 (1993); B. Hammer, and M. Scheffler, Phys. Rev. Lett. **74**, 3487 (1995).

21. C. Filippi, D.J. Singh, and C. Umrigar, Phys. Rev. B **50**, 14947 (1993).

22. L. Hedin, and B.I. Lundqvist, I. Phys. C **4**, 2064 (1971).

23. D.J. Singh, *Planewaves, Pseudopotentials and LAPW method* (Kluwer Academic publishers, Boston, 1994).

24. O. Gunnarsson, M. Jonson, and B.I. Lundqvist, Phys. Rev. B **20**, 3136 (1979).

25. I.I. Mazin, and D.J. Singh, arXiv:cond-mat/9801301.

26. J.P. Perdew, and Yue Wang, Phys. Rev. B **46**, 12947 (1992).

27. D.J. Singh, Phys. Rev. B **48**, 14099 (1993).

28. O. Gunnarsson, and R.O. Jones, Phys. Scr. **21**, 394 (1980).

29. O.V. Gritsenko, A. Rubio, L.C. Balbás, and J.A. Alonso, Chem. Phys. Lett. **205**, 348 (1993).

30. N. Troullier, and J.L. Martins, Phys. Rev. B **43**, 1993 (1991).

31. H. Hellmann, *Einfuhrung in die Quantenchemie* (Deuieke, Leipzig, 1973), p. 285; R.P. Feynman, Phys. Rev. **56**, 340 (1939).

32. J.C. Slater, J. Chem. Phys. **57**, 2389 (1972).

33. A.D. Becke, J. Chem. Phys. **104**, 1040 (1996).

Copyright © 2003 EBSCO Publishing

Copyright of AIP Conference Proceedings is the property of American Institute of Physics and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.