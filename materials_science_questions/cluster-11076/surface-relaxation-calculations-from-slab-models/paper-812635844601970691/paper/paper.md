# Relaxation of Al(001) and Al(110): Surface embedded Green function total-energy and force calculation

G. A Benesh and Daniel Gebreselasie
Department of Physics, Baylor University, Waco, Texas 76798
(Received 20 November 1995; revised manuscript received 15 May 1996 )

Surface total energy and force calculations have been performed for the Al(001) and Al(110) surfaces using the surface embedded Green function method. The force on each surface layer has been calculated in two ways: from a direct expression, and from the slope of the total energy versus the interlayer separation curve. Excellent agreement has been obtained between the two methods. For the Al(001) surface, the calculated surface relaxation was $-1\pm2$ %, which is in excellent agreement with experiment. For the Al(110) surface, the calculated surface relaxation of $-11\%$ is in good agreement with experiment. Errors associated with various approximations used in calculating the total energy, force, work function, and surface relaxation have also been evaluated. [S0163-1829(96)04932-6]

## I. INTRODUCTION

The surface total energy determines the stability of a given arrangement of atoms at a surface, with the surface ground-state being the minimum-energy arrangement. Be- cause density-functional theory (DFT) requires a static exter- nal field, DFT total-energy calculations are only capable of determining the electron distribution for a particular arrange- ment of atoms. A single DFT calculation reveals nothing about the stability of the atomic arrangement itself. Instead, the minimum-energy atomic arrangement is usually identi- fied by determining the total energy for many different ar- rangements.

Another approach to the problem is through the calcula- tion of surface forces. The ground-state arrangement can be more easily determined in this way, since the calculated quantity is a vector. The vector components reveal the change in position which reduces the surface energy to the greatest extent. The Hellmann-Feynman theorem has often been employed in calculating surface forces; however, the application of the theorem has not proved altogether successful. $^{1-3}$ Problems with the Hellman-Feynman ap proach have largely been attributed to the inaccuracy of available charge densities and potentials due to incomplete basis sets. To improve the technique, researchers have com- puted correction terms associated with the dependence of the basis functions on the position of the nuclei.

The earlier DFT surface total-energy calculations have been based on either the slab or slab-superlattice geometries in which multiple surfaces are present. In the present work, density-functional expressions for the total energy and force have been adapted to a semi-infinite geometry using the sur- face embedded Green function (SEGF) method. $^{4,5}$

As a test of the implementation, the surface energy and force expressions have been used to determine surface relax- ations of Al(001) and Al(110). The present results are in good to excellent agreement with experiment; and are gen- erally superior to previous theoretical results. Studies of the total energy, force, work function, and other calculated quan- tities as a function of surface relaxation for the Al(001) sur- face are also presented.

## II. THEORY

The local-density approximation (LDA) expression for the total energy is given by $^{6}$

$$
\begin{aligned}
E[\rho(\mathbf{r})]= & \sum_{i} E_{i}-\frac{1}{2} \int \rho(\mathbf{r}) V^{C}(\mathbf{r}) d \mathbf{r}+\int \rho(\mathbf{r})\left\{\epsilon^{\mathrm{xc}}(\mathbf{r})\right. \\
& \left.-V^{\mathrm{xc}}(\mathbf{r})\right\} d \mathbf{r}-\frac{1}{2} \sum_{n} Z_{n}\left[\int_{V} \rho\left(\mathbf{R}_{n}+\mathbf{r}^{\prime}\right)\right. \\
& \left.× \frac{1}{r^{\prime}}\left(1-\frac{r^{\prime}}{R}\right) d \mathbf{r}^{\prime}+\frac{1}{4 \pi} \int_{S} V_{n}^{c}\left(r^{\prime}=R\right) d \Omega^{\prime}\right],
\end{aligned}
$$

where $\rho(\mathbf{r})$ is the charge density, $V^{c}(\mathbf{r})$ is the Coulomb potential, $Z_{n}$ is the atomic number of the $n$th nucleus, $\epsilon^{\mathrm{xc}}(\mathbf{r})$ is the exchange-correlation energy per electron, $V^{\mathrm{xc}}(\mathbf{r})$ is the exchange-correlation potential, and $V_{n}^{c}(\mathbf{r})$ is the Coulomb potential without the contribution from the $n$th nucleus.

In the SEGF method, the surface layers are embedded onto a semi-infinite bulk substrate. $^{4,5}$ Thus, apart from the surface states, the valence eigenenergies are continuous within the bands. As a result, Eq. (1) is modified to

$$
\begin{aligned}
E[\rho(\mathbf{r})]= & \sum_{n} \sum_{i} E_{\mathrm{in}}+\int_{E_{0}}^{E_{f}} E \sigma(E) d E-\int \rho(\mathbf{r}) V^{\mathrm{eff}}(\mathbf{r}) d \mathbf{r} \\
& +\frac{1}{2} \int \rho(\mathbf{r}) V^{c}(\mathbf{r}) d \mathbf{r}+\int \rho(\mathbf{r}) \varepsilon^{\mathrm{xc}}[\rho(\mathbf{r})] d \mathbf{r} \\
& -\frac{1}{2} \sum_{n} Z_{n}\left[\int_{V} \rho\left(\mathbf{R}_{n}+\mathbf{r}^{\prime}\right) \frac{1}{r^{\prime}}\left(1-\frac{r^{\prime}}{R}\right) d \mathbf{r}^{\prime}\right. \\
& \left.+\frac{1}{4 \pi} \int_{S} V_{n}^{c}\left(r^{\prime}=R\right) d \Omega^{\prime}\right],
\end{aligned}
$$

where $V^{\mathrm{eff}}(\mathbf{r})$ is the sum of the Coulomb and exchange- correlation potentials, and $\sigma(E)$ is the local density of states.

The energy derivative with respect to a nuclear coordinate is given by $^{7}$

$$
\delta E=\sum_{i} \delta E_{i}-\int \rho(\mathbf{r}) \delta V^{\mathrm{eff}}(\mathbf{r}) d \mathbf{r}-\mathbf{F}_{\alpha}^{\mathrm{hf}} \cdot \delta \mathbf{r}_{\alpha}, \quad (3)
$$

where $\mathbf{F}_{\alpha}^{\mathrm{hf}}$ is the Hellmann-Feynman (electrostatic) force on the $\alpha$ th nucleus $^{1,2}$
$$
\mathbf{F}_{\alpha}^{\mathrm{hf}}=Z_{\alpha} \nabla_{\alpha} V_{\alpha}. \quad (4)
$$

The first two terms on the right side of Eq. (3) represent corrections to the Hellmann-Feynman force. The correction from the core is given by $^{7}$
$$
\mathbf{F}_{\alpha}^{\text {core }}=-\int_{\alpha} \rho^{\text {core }}\left(\mathbf{r}_{\alpha}+\mathbf{r}\right) \nabla_{\mathbf{r}} V^{\text {eff }}\left(\mathbf{r}_{\alpha}+\mathbf{r}\right) d \mathbf{r}. \quad (5)
$$

Similarly, the correction from the valence electrons is given by $^{7}$
$$
\begin{aligned}
& \sum_{i} \delta E_{i}^{\mathrm{val}}-\int \rho^{\mathrm{val}}(\mathbf{r}) \delta V^{\mathrm{eff}}(\mathbf{r}) d \mathbf{r} \\
& =\sum_{i}\left\{\left\langle\delta \psi_{i}(\mathbf{r})\left|H-E_{i}^{\mathrm{val}}\right| \psi_{i}(\mathbf{r})\right\rangle\right. \\
& \left.\quad+\left\langle\psi_{i}(\mathbf{r})\left|H-E_{i}^{\mathrm{val}}\right| \delta \psi_{i}(\mathbf{r})\right\rangle\right\}. \quad (6)
\end{aligned}
$$

Equation (6) is known as the insufficient valence basis function correction.

The variation of a single-state wave function with respect to the position dependence of the basis may be written as
$$
\delta \psi_{i}(\mathbf{r})=\sum_{\mathbf{G}} \delta c_{i}(\mathbf{G}) \varphi_{\mathbf{G}}(\mathbf{r})+\sum_{\mathbf{G}} c_{i}(\mathbf{G}) \delta \varphi_{\mathbf{G}}(\mathbf{r}), \quad (7)
$$
where the $\varphi_{\mathbf{G}}(\mathbf{r})$ 's are the basis functions, and the $c$ 's are expansion coefficients.

Most other computational methods minimize the expectation value of the Hamiltonian with respect to the expansion coefficients. As a result, the contribution from the first term on the right side of Eq. (7) is zero to first order. However, the contribution from the second term on the right side of Eq. (7) is generally nonzero. Yu, Singh, and Krakauer $^{7}$ include this term in their expression for the valence correction.

In contrast, the SEGF formalism varies the expectation value of the Hamiltonian with respect to the wave function. Thus, the contribution from the wave function variation expressed in Eq. (7) is zero to first order-and the correction required by Yu, Singh, and Krakauer is unnecessary. As a result, the entire valence correction is zero to first order:
$$
\sum_{i} \delta E_{i}^{\mathrm{val}}-\int \boldsymbol{\rho}^{\mathrm{val}}(\mathbf{r}) \delta V^{\mathrm{eff}}(\mathbf{r}) d \mathbf{r} \approx 0. \quad (8)
$$

The LDA pressure can be expressed in terms of the forces as $^{8}$
$$
P=-\frac{1}{3 V} \sum_{\alpha} \mathbf{F}_{\alpha} \cdot \mathbf{r}_{\alpha}, \quad (9)
$$
where $V$ is the volume of the unit cell and the summation runs over all nuclei in a unit cell. $\mathbf{F}_{\alpha}(=\mathbf{F}_{\alpha}^{\mathrm{hf}}+\mathbf{F}_{\alpha}^{\text {core }})$ is the sum of the Hellmann-Feynman force and core corrections [Eqs. (4) and (5)].

![](./images/812635844601970691_1.jpg)

FIG. 1. Dependence of the total energy on the surface relaxation.

## III. DISCUSSION AND RESULTS

### A. The Al(001) surface

In order to test the validity of the force calculations, the energy and force were calculated for more than 20 positions of the Al(001) surface. The negative of the energy derivative obtained from the energy curve was compared with the force as calculated directly from Eqs. (4) and (5). The energy and force results were then used to determine the surface relaxation.

The charge-density calculation was performed for two embedded layers. Eighty linearized augmented plane wave (LAPW) basis functions and 36 special $\mathbf{k}$ points from the irreducible part of the surface Brillouin zone were used. One thousand plane waves were used in expanding the interstitial charge density, and the maximum value of $l$ used in the muffin-tin spherical harmonic expansions was 6.

The charge density was calculated first for a geometry in which the surface interlayer separation was set equal to the bulk interlayer spacing. With this as a starting point, self-consistent charge densities were computed for twenty other layer spacings, representing both contractions and expansions of the bulk spacing. The lattice spacing increment was 0.02 a.u., which is about 0.5% of the bulk interlayer separation. The potential for each displaced position was converged to a root-mean-square iteration error of $10^{-10}$ hartree.

The total energy of the system is at a minimum when all the layers are in their equilibrium positions. Thus, if inner layers are not in their ideal positions, the true energy minimum will not be obtained by displacing only the surface layer. In the case of the (001) surface of aluminum, experiment predicts essentially zero relaxation in all inner layers. As a result, displacement of the outermost layer should reveal the minimum-energy position in which the total system is in equilibrium.

In Fig. 1 the surface relaxation is given as a percentage of

![](./images/812635844601970691_2.jpg)

FIG. 2. Perpendicular component of the surface force: from the total-energy curve (triangles); from the Hellmann-Feynman theorem (circles).

the bulk interlayer separation. Negative (positive) values represent contraction (expansion) of the bulk spacing, respectively. From Fig. 1, the SEGF method predicts the minimum-energy location of the surface to be at about 1% contraction, which is close to the 0% contraction predicted by experiment. It is interesting to note that, while removing an electron from the surface requires an energy of more than 4 eV, significant displacement of the surface changes the work function by only a few hundredths of an electron volt.

To calculate the derivative of this curve, so that a comparison with the force as calculated by the direct expression can be made, the curve was fit to a sixth-order polynomial. The rms error in fitting the curve was 0.26 meV.

Without core correction terms, the Hellmann-Feynman expression is not expected to accurately predict surface forces. In Fig. 2, a comparison between the Hellmann-Feynman force and the force as calculated from the derivative of our fitting function is made. Clearly, the two predictions vary widely. While the fitting function predicts zero force when the equilibrium spacing is about 1% smaller than the bulk value, the Hellmann-Feynman expression predicts contractive forces at all surface positions considered. When the Hellmann-Feynman curve is extrapolated, it predicts the equilibrium spacing will occur when the layer spacing is contracted by about 24%—a deviation of nearly 0.9 a.u. from experiment.

One reason for the error in the Hellmann-Feynman force is the exclusion of the core contribution. This occurs because the nonspherical parts of the potential and charge density have been neglected. However, the Hellmann-Feynman core contribution depends only on the (neglected) nonspherical parts. To understand this, the dependence on surface relaxation was studied by decomposing the kinetic energy into its valence and core components. Although the valence kinetic energy changes more rapidly than the core kinetic energy, the derivative of the core kinetic energy is appreciable. Thus, the predicted Hellmann-Feynman force would be significantly improved if the nonspherical parts of the core charge density and potential were included. As expected, the required correction to the Hellmann-Feynman force is positive. As Pulay³ has remarked, the chemically active valence electrons contribute more to the force than do the core electrons.

![](./images/812635844601970691_3.jpg)

FIG. 3. Perpendicular component of the surface force: from the total-energy curve (triangles); from the Hellmann-Feynman theorem with core corrections (circles).

A comparison between the force as calculated from the energy-derivative curve and the force as calculated by the Hellmann-Feynman theorem (with core correction) is shown in Fig. 3. Excellent agreement is obtained between the two methods over a wide range of layer spacing. The Hellmann-Feynman force with core corrections also predicts the zero force location at about −1.0%, which is in almost exact agreement with the energy derivative prediction.

The dependence of the work function on relaxation was also studied. As expected, the larger the layer spacing, the smaller the energy required to remove an electron from the surface. Unlike the energy, which has a turning point at the equilibrium position, there is no extremal value of the work function across the range of layer spacing considered.

Our calculated work function was 4.42±0.04 eV, compared with the experimental value of 4.41±0.03 eV.⁹ While our calculated value and 90% of the uncertainty interval fall within the experimental interval, other calculated values¹⁰⁻¹³ fall well outside the experimental uncertainty interval. An earlier SEGF calculation obtained a work function of 4.50 eV.⁵ The improved value in the present work is largely due to the increased number of special $\mathbf{k}$ points.

In the bottom row of Table I, we list our results for the work function, surface total energy, surface force, Hellmann-Feynman force (without core correction), and core corrections. For bulk aluminum, Morruzzi, Janak, and Williams¹⁴ have calculated the total energy per atom as −241.5 hartree. In view of the surface tension of aluminum (0.002

<table>
<caption>Table I. Estimated errors associated with the work function, surface total energy, surface force, Hellmann-Feynman force, and core corrections.</caption>
<thead>
<tr>
<th>Estimated errors
associated with:</th>
<th>Work function
(eV)</th>
<th>Total energy
(hartree)</th>
<th>Force
(hartree/a.u.)</th>
<th>HF force
(hartree/a.u.)</th>
<th>Core correction
(hartree/a.u.)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Number of special $\mathbf{k}$ points</td>
<td>$+0.038$</td>
<td>$-0.0018$</td>
<td>$-0.000\ 64$</td>
<td>$-0.0046$</td>
<td>$+0.0041$</td>
</tr>
<tr>
<td>Number of basis functions</td>
<td>$-0.0025$</td>
<td>$+0.000\ 26$</td>
<td>$-0.000\ 84$</td>
<td>$+0.0065$</td>
<td>$-0.0073$</td>
</tr>
<tr>
<td>Number of energy-integration points</td>
<td>$-0.0009$</td>
<td>$0.000\ 00$</td>
<td>$+0.000\ 01$</td>
<td>$0.0000$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td>Uncertainty in surface position</td>
<td>$\pm 0.012$</td>
<td>$\pm 0.000\ 05$</td>
<td>$\pm 0.001$</td>
<td>$\pm 0.002$</td>
<td>$\pm 0.0025$</td>
</tr>
<tr>
<td>Calculated values</td>
<td>$4.42\pm 0.04$</td>
<td>$-483.815\pm 0.001$</td>
<td>$0.000\pm 0.002$</td>
<td>$-0.028\pm 0.008$</td>
<td>$0.029\pm 0.008$</td>
</tr>
</tbody>
</table>

hartree/a.u.${}^2$),$^{15}$ the energy per surface atom is expected to be somewhat greater in magnitude than the bulk energy; however, the difference is expected to be less than a hartree. Thus, the present calculated total energy of $-483.815$ hartree ($-241.9$ hartree/atom) is in the expected range.

Also listed in Table I are possible sources of error within the calculation (see the Appendix). For work function and energy calculations, the error due to limiting the number of basis functions to eighty is negligible compared to the error due to the finite number of special $\mathbf{k}$ points. (Thus, to increase the accuracy of the total-energy calculation, it is necessary only to increase the number of special $\mathbf{k}$ points.) However, in force calculations both contributions are of the same order. Thus, force calculations generally require a larger number of basis functions. It should also be noted that the Hellmann-Feynman and core-correction truncation and relaxation errors are of opposite sign. Consequently, there is a smaller error in the total force than in the Hellmann-Feynman and core-correction forces separately. As expected, the error in the force is larger than the error in the total energy per atom, since the former is the derivative of the latter.

Once the error in the force was determined, the error in locating the equilibrium position of the surface could be calculated. Near equilibrium the force can be described by a linear function. The uncertainty in the surface position, $\Delta z$, is represented in terms of the uncertainty in the force, $\Delta F_{\alpha z}$, as
$$
|\Delta z|=\frac{\left|\Delta F_{\alpha z}\right|}{|m|}, \tag{10}
$$
where $m$ is the slope of the curve. This gives an error of approximately $2\%$, so that the uncertainty interval for the surface relaxation is $-1\pm 2\%$.

Table II compares our calculated surface relaxation with other experimental and theoretical results. The experimental value lies within the theoretical uncertainty interval. The present result is in excellent agreement with experiment, and represents an improvement over previous theoretical work.

<table>
<caption>Table II. Comparison of the calculated Al(001) and Al(110) surface relaxations with other experimental and theoretical values.</caption>
<thead>
<tr>
<th>
</th>
<th colspan="2">Surface relaxation</th>
</tr>
<tr>
<th>
</th>
<th>Al(001)</th>
<th>Al(110)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Present work</td>
<td>$-1\pm 2\%$</td>
<td>$-11\%$</td>
</tr>
<tr>
<td>Experiment (Refs. 16 and 17)</td>
<td>$0\%$</td>
<td>$-8.6\pm 0.8\%$</td>
</tr>
<tr>
<td>Effective-medium theory (Ref. 18)</td>
<td>$-3\%$</td>
<td>$-7\%$</td>
</tr>
<tr>
<td>Embedded-atom method (Ref. 19)</td>
<td>$-4.9\%$</td>
<td>$-10.47\%$</td>
</tr>
<tr>
<td>Finnis and Heine (Ref. 20)</td>
<td>$-4.6\%$</td>
<td>$-16\%$</td>
</tr>
<tr>
<td>First principles (LDA) (Ref. 19)</td>
<td>
</td>
<td>$-5.4\pm 0.3\%$</td>
</tr>
</tbody>
</table>

Variations of the surface total energy, work function, and force with different exchange-correlation potentials are presented in Table III. The total energy, work function, and force calculated with Kohn-Sham exchange$^{21}$ are appreciably different from those calculated with more sophisticated exchange-correlation potentials. Wigner interpolation$^{22}$ yields significantly different results for the total energy and force as compared to other schemes. Hedin-Lundqvist$^{23}$ and Ceperley-Alder$^{24}$ formulas yield similar results for all three calculated quantities. Results for the Von Barth–Hedin$^{25}$ exchange-correlation potential differ slightly from the Hedin-Lundqvist and Ceperley-Alder values.

### B. The Al(110) surface

The Al(110) calculation was also performed for two embedded layers. One hundred LAPW basis functions and 16 special $\mathbf{k}$ points from the irreducible part of the surface Brillouin zone were used. The interstitial charge density was expanded using 1000 plane waves, and the maximum value of $l$ used in the muffin-tin charge-density spherical harmonic expansion was 7.

The calculated work function was $4.21\pm 0.04$ eV. Two different experimental results have been reported: $4.28\pm 0.03$ eV (Ref. 9) and $4.06\pm 0.03$ eV (Ref. 26). Thus, our calculated work function was much closer to the higher measurement—but somewhat outside the error interval. One possible cause of the discrepancy is the multilayer nature of the surface relaxation (discussed below).

The calculated total energy per surface atom for Al(110) is $-241.8$ hartree. This result is again close to the bulk aluminum result of $-241.5$ hartree/atom of Morruzzi, Janak,

<table>
<caption>Table III. Dependence of the work function, total energy, and force for Al(001) on different types of exchange-correlation potentials.</caption>
<thead>
<tr>
<th>Exchange-
correlation type</th>
<th>Work
function (eV)</th>
<th>Total-energy
(hartree)</th>
<th>Force
(hartree/a.u.)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Kohn-Sham</td>
<td>$3.36$</td>
<td>$-481.849$</td>
<td>$-0.006\ 08$</td>
</tr>
<tr>
<td>Wigner</td>
<td>$4.45$</td>
<td>$-483.180$</td>
<td>$-0.003\ 49$</td>
</tr>
<tr>
<td>Hedin-Lundqvist</td>
<td>$4.48$</td>
<td>$-483.820$</td>
<td>$-0.000\ 37$</td>
</tr>
<tr>
<td>Von Barth-Hedin</td>
<td>$4.82$</td>
<td>$-484.279$</td>
<td>$0.000\ 55$</td>
</tr>
<tr>
<td>Ceperley-Alder</td>
<td>$4.39$</td>
<td>$-483.815$</td>
<td>$-0.000\ 23$</td>
</tr>
</tbody>
</table>

![](./images/812635844601970691_4.jpg)

FIG. 4. Pressure acting on a surface unit cell times volume versus surface relaxation for Al(110).

and Williams. $^{14}$ Furthermore, the calculated surface energy of Al(110) is smaller in magnitude than that of Al(001) as expected, due to the difference in surface tension between Al(110) and Al(001). [The total energy per atom for the Al(001) surface is $-241.9$ hartree.]

Unlike Al(001), the Al(110) surface exhibits multilayer relaxation. $^{19}$ In this work, we have only allowed the spacing between the outermost and second layers to relax. The pressure given by Eq. (9) was calculated for many different interlayer separations. Results are presented in Fig. 4, where the relaxation is given as the fractional difference from the bulk interlayer spacing. The equilibrium spacing occurs at about $11\%$ less than the bulk spacing. In Table II our results are compared with other theoretical and experimental values. The present result differs by about $2\%$ from experiment ($-11\%$ versus $-9\%$), but is much closer to the experimental value than the other LDA result. To achieve better accuracy, it is necessary to allow relaxations between several other layers.

## IV. CONCLUSION

The surface embedded Green function method has been used successfully in performing surface total energy and force calculations for the Al(001) and Al(110) surfaces. Surface relaxations predicted by these calculations are in good to excellent agreement with experiment-an improvement over previous theoretical work. Unlike other methods that make use of the LAPW basis functions, the SEGF method does not require valence basis function corrections for the force calculation. As a result, SEGF force calculations are accurate and economical when compared to other techniques.

## APPENDIX: ERROR ANALYSIS

For the first time, detailed estimates of computational error have been performed using our SEGF program. The sources of errors involved in the calculation may be classified as follows.

Iteration error and errors due to numerical techniques. True self-consistency is never really achieved. The calculation is usually concluded when the difference between input and output charge densities (or potentials) falls below some threshold. The threshold is never set to zero because of intrinsic errors that are associated with the integration and differentiation algorithms employed. In the present work, the threshold error in the potential was set at $10^{-10}$ hartree. Errors of this magnitude are negligible compared with other sources of error (discussed below).

Errors due to the number of special $\mathbf{k}$ points. Integrals over the surface Brillouin zone are approximated by a weighted sum over a set of special $\mathbf{k}$ points. The error due to this approximation was estimated by studying the dependence of the physical quantities on the number of special $\mathbf{k}$ points.

Errors due to an incomplete basis. Although basis sets are generally not complete, accurate calculations may be performed with a relatively small number of basis functions which resemble the crystal wave functions. The error due to the incomplete basis was estimated by comparing values obtained with 80 and 120 LAPW basis functions.

Errors due to the number of energy integration points. The surface Green function is energy dependent. To obtain the charge density, an energy integral must be performed over the occupied portion of the valence band. This integral is evaluated using Gauss-Chebyshev quadrature over a semicircle in the upper half plane. $^{5}$ The error due to the number of energy-integration points was obtained by comparing the values obtained with 15, 31, and 63 points.

Errors due to the uncertainty in the surface location. These errors can be approximated by studying the surface relaxation dependence and fitting to a Taylor series expansion. That is, for a function $f(z)$,
$$
|\Delta f| \approx\left|\frac{\partial f}{\partial z} \Delta z\right|, \tag{A1}
$$
where $z$ represents the position of the surface. The uncertainty in the location of the surface, $\Delta z$, is approximated by the difference between the unrelaxed and relaxed (equilibrium) positions of the surface (about 0.04 a.u.). The derivative is taken at the unrelaxed position.

The errors due to limiting the number of special $\mathbf{k}$ points, the number of basis functions, and the number of energy-integration points are monotonic (all negative or all positive). This causes the uncertainty intervals to be asymmetric about the calculated values. To express the calculated quantities and uncertainty intervals in a symmetric manner, the value in the middle of each uncertainty interval has been quoted. For example, the calculated Al(001) work function (with uncertainty interval) ranges from 4.38 to 4.46 eV, and has been written as $(4.42 \pm 0.04)$ eV.

In Table I, the largest error contribution in the work function and total energy comes from limiting the number of special $\mathbf{k}$ points in the irreducible part of the surface Bril-

louin zone to 36. For the work function, this is due to the slow decay of an oscillatory dependence upon the number of special $\mathbf{k}$ points. For surface force calculations, errors due to the incomplete basis are of the same order as those due to the special $\mathbf{k}$ points. Thus, force calculations generally require larger basis sets.

$^{1}$H. Hellmann, Einfuhrung in die Quantenchemie (Deuticke, Leibzig, 1937), p. 285.
$^{2}$R. P. Feynman, Phys. Rev. 56, 340 (1939).
$^{3}$P. Pulay, Mol. Phys. 17, 197 (1969).
$^{4}$G. A. Benesh and J. E. Inglesfield, J. Phys. C 17, 1595 (1984).
$^{5}$J. E. Inglesfield and G. A. Benesh, Phys. Rev. B 37, 6682 (1988).
$^{6}$M. Weinert, E. Wimmer, and A. J. Freeman, Phys. Rev. B 26, 4571 (1982).
$^{7}$Rici Yu, D. Singh, and H. Krakauer, Phys. Rev. B 43, 6411 (1991).
$^{8}$J. F. Janak, Phys. Rev. B 9, 3985 (1974).
$^{9}$J. K. Grepstad, P. O. Gartland, and B. J. Slagsvold, Surf. Sci. 57, 348 (1976).
$^{10}$H. Krakauer, M. Posternak, A. J. Freeman, and D. D. Koelling, Phys. Rev. B 23, 3859 (1981).
$^{11}$E. Wimmer, M. Weinert, A. J. Freeman, and H. Krakauer, Phys. Rev. B 24, 2292 (1981).
$^{12}$G. A. Benesh, H. Krakauer, D. E. Ellis, and M. Posternak, Surf. Sci. 104, 599 (1981).

$^{13}$N. D. Lang and W. Kohn, Phys. Rev. B 3, 1215 (1971).
$^{14}$V. L. Morruzzi, J. F. Janak, and A. R. Williams, Calculated Electronic Properties of Metals (Pergamon, New York, 1978).
$^{15}$W. R. Tyson and W. A. Miller, Surf. Sci. 62, 267 (1977).
$^{16}$J. R. Noonan and H. L. Davis, Phys. Rev. B 29, 4349 (1984).
$^{17}$D. W. Jepsen, P. M. Markus, and F. Jona, Phys. Rev. B 6, 3684 (1972).
$^{18}$K. W. Jacobsen, J. K. Norskov, and M. J. Puska, Phys. Rev. B 35, 7423 (1987).
$^{19}$Ning Ting, Yu Qingliang, and Ye Yiying, Surf. Sci. 206, L857 (1988).
$^{20}$M. W. Finnis and Volker Heine, J. Phys. F 4, L37 (1974).
$^{21}$W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).
$^{22}$D. Pines, Elementary Excitations in Solids (Benjamin, New York, 1963).
$^{23}$L. Hedin and B. I. Lundqvist, J. Phys. C 4, 2064 (1971).
$^{24}$D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).
$^{25}$U. Von Barth and L. Hedin, J. Phys. C 5, 1629 (1972).
$^{26}$R. M. Eastment and C. H. B. Mee, J. Phys. F 3, 1738 (1973).