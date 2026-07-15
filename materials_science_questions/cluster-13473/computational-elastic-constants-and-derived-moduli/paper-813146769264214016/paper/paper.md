# Percolation in Isotropic Elastic Media

R. Garcia-Molina, $^{(1)}$ F. Guinea, $^{(2)}$ and E. Louis $^{(1,3)}$

$^{(1)}$Departamento de Física Aplicada, Universidad de Alicante, E-03080 Alicante, Spain
$^{(2)}$Instituto de Ciencia de Materiales, Consejo Superior de Investigaciones Científicas, Universidad Autónoma, Cantoblanco, E-28049 Madrid, Spain
$^{(3)}$Industria Española del Aluminio, E-03080 Alicante, Spain

(Received 19 June 1987; revised manuscript received 13 November 1987)

An investigation is presented of elasticity percolation in isotropic media with arbitrary elastic constants. A model which combines the central-force potential energy and a triangular lattice with a large unit cell allows us to vary the ratio between the two Lamé coefficients. Results of numerical simulations indicate that the critical properties of the percolation transition do strongly depend on the elastic constants.

PACS numbers: 64.60.Ak, 62.90.+k

Percolation ideas $^{1}$ have been applied to many different physical phenomena. $^{2}$ In particular, the elastic properties of random networks near the percolation transition have attracted a great deal of interest in recent years. $^{3-8}$ It was first suggested by de Gennes $^{3}$ that in the special case of a nonrotationally invariant isotropic force constant, elasticity percolation was equivalent to conductivity percolation. More recently it was proposed $^{5}$ that, instead, the rotationally invariant central-force model belongs to a different universality class. All these investigations focused on the properties derived from the assumption of different forms for the potential energy without searching for a link with the macroscopic properties of the continuum elastic media. Nonetheless, it is quite clear that a given model for the potential energy univocally corresponds to a medium with a given set of elastic constants.

In this paper we adopt an entirely new point of view and seek a relationship between the critical properties of the percolation transition in isotropic elastic media, and their elastic constants. The potential energy was described by means of the rotationally invariant central-force Hamiltonian. In order to obtain the correct isotropic properties in the continuum limit, a triangular lattice was chosen; on the other hand, changing the unit cell of this lattice to $\sqrt{3} \times \sqrt{3}$ allowed us to vary continuously the elastic constants of the medium. The results indicate that the central-force model does not constitute by itself a universality class; instead what matter, as far as the percolation transition is concerned, are the elastic constants of the medium.

The equilibrium equations to be satisfied in continuum elasticity $^{9,10}$ are

$$
(\lambda+\mu) \partial_{i}\left(\sum_{j} \partial_{j} v_{j}\right)+\mu\left(\sum_{j} \partial_{j}^{2}\right) v_{i}=0, \tag{1}
$$

where $\lambda$ and $\mu$ are the two Lamé coefficients, $\mathbf{v}(\mathbf{r})$ is the displacement field, and $\partial_{i}$ is the partial derivative with respect to the $i$th component of $\mathbf{r}$. We describe the elastic potential energy by means of the central-force Hamiltonian

$$
H=\frac{1}{2} \sum_{i j} k_{i j}\left[\left(\mathbf{v}_{i}-\mathbf{v}_{j}\right) \cdot \hat{\mathbf{r}}_{i j}\right]^{2}, \tag{2}
$$

where $\hat{\mathbf{r}}_{i j}$ is a unit vector between sites $i$ and $j$, and the force constants $k_{i j}$ are finite with probability $p$ and vanish with probability $1-p$. To simulate the two Lamé coefficients in Eq. (1), we choose a triangular lattice with unit cell $\sqrt{3} \times \sqrt{3}$; more specifically, we use two force constants, one associated with the bonds which lie in a superimposed honeycomb lattice, $k_{a}$, and the other, $k_{b}$, with the rest of the bonds (Fig. 1). In the continuum limit the relation between the two Lamé coefficients and those two force constants is given by

$$
\frac{\lambda}{\mu}=\frac{4 x^{2}+3 x+2}{8 x+1}, \quad x=\frac{k_{a}}{k_{b}}. \tag{3}
$$

This result was obtained by our calculating the ratio between the longitudinal stretching and transverse compression of the system under an applied uniaxial tension. This procedure allows us to vary $\lambda/\mu$ continuously from 0.9 to infinity.

Numerical simulations were carried out on hexagons of sides in the range 10-45 (in units of bond length)

![](./images/813146769264214016_1.jpg)

FIG. 1. The $\sqrt{3} \times \sqrt{3}$ reconstruction of the triangular lattice utilized in this work.

containing 331-6211 nodes, respectively. The bulk modulus was calculated directly from the total elastic energy of the system in the following way. The boundary nodes were given fixed displacements normal to the boundary corresponding to a macroscopic strain. Then the interior nodes were allowed to relax until the equilibrium equations (1) in its discretized version were satisfied. Equations (1) were solved iteratively. The iteration process was stopped either after a fixed number of iterations or when the logarithmic derivative of the total elastic energy of the system was lower than a given value (in our calculations these were 600 and $10^{-6}$, respectively). Logarithmic derivatives of the elastic energy were always lower than $5 \times 10^{-5}$ and the maximum force on the interior nodes less than 0.005 times the initial force on the boundary nodes. In order to speed up computations, the iteration process for a given $p$ was started from the relaxed structure obtained for the preceding (larger) $p$ for a given realization. The procedure was repeated for a number of realizations which varied with the size of the hexagon (around 30 for the smaller and 10 for the larger one). More details on our numerical procedures will be given in a future publication.

To illustrate the suitability of the present model to describe the properties of the continuum, the bulk modulus of a hexagonal ring as a function of the fraction of broken bonds was calculated and compared to the analytical result obtained in the case of a circular ring, namely,
$$
B=B_{0} p /\left[1+(\lambda / \mu+1)(1-p)\right]^{-1}, \tag{4}
$$
where $1-p$ is the fraction of empty area and $B_{0}$ is the bulk modulus of the perfect elastic medium. Figure 2 shows the numerical results for a hexagon of side 30 and the analytical curves given by Eq. (4), for two values of $\lambda / \mu$. The agreement is very good, indicating that the combination of the reconstructed triangular lattice shown in Fig. 1 and the potential energy of Eq. (2) correctly describes the properties of the continuum elastic media.

![](./images/813146769264214016_2.jpg)

FIG. 2. Bulk modulus vs $p$ for a circular ring (continuous lines) and a hexagonal ring (discrete values) as given by Eq. (4) and numerical simulations, respectively, for $\lambda / \mu=1$ and 5.

The critical properties of the percolation transition were investigated by means of the generalized phenomenological renormalization method. $^{11-13}$ This method allows a very accurate determination of the percolation threshold $p_{c}$ and the ratio $\delta=f / v_{e}$, where $f$ is the percolation exponent and $v_{e}$ the correlation length exponent; the latter could also be determined within the same scheme although with much less accuracy $^{12}$ and will not be calculated in this work. As a detailed description of the method can be found elsewhere, $^{6,11-13}$ here we shall only comment on the points pertinent to the present discussion. In analogy with phenomenological renormalization, the following mapping is inferred $^{12}$:
$$
B_{L}(p)=\left(L / L^{\prime}\right)^{-\delta} B_{L^{\prime}}\left(p^{\prime}\right), \tag{5}
$$
where $L$ (or $L^{\prime}$ ) is the linear dimension of the finite network. Following Barber and Selke, we define $^{12}$
$$
\zeta_{L L^{\prime}}(p)=\ln \left[B_{L}(p) / B_{L^{\prime}}(p)\right] / \ln \left(L / L^{\prime}\right). \tag{6}
$$
Then the intersection of $\zeta_{L L^{\prime}}(p)$ and $\zeta_{L L^{\prime \prime}}(p)$ approximately gives $\left(p_{c}, \delta\right)$. The method has proved to be very efficient in the determination of both quantities. $^{12,13}$

The above procedure is illustrated in Figs. 3 and 4. Figure 3 shows the bulk modulus as a function of $p$ for $\lambda / \mu=5$ and hexagons of sides 10 and 20. Concerning Feng and Sen's calculations $^{5}$ of $p_{c}$ and $f$ directly from curves similar to those shown in Fig. 3, two comments are in order. (i) It is very difficult to decide the size

![](./images/813146769264214016_3.jpg)

FIG. 3. Bulk modulus vs $p$ for random networks. Simulations were carried out on hexagons of sides 10 and 20 (in units of bond length). $\lambda / \mu=5$.

![](./images/813146769264214016_4.jpg)

FIG. 4. Plot of the function $\zeta_{LL'}=\ln(B_L/B_{L'})/\ln(L/L')$ against $p$, for the case of $\lambda/\mu=10$.

beyond which the finite network behaves as an infinite system. (ii) The estimation of $p_{c_e}$ from these curves is very inaccurate as it requires a parallel determination of the exponent $f$. The analysis of Feng and Sen $^5$ suffers from those two drawbacks. The calculation of $p_{c_e}$ and $f/v_e$ by means of Eq. (6) is illustrated in Fig. 4. There is noted a distinct intersection of the two curves corre- sponding to the $\zeta_{LL'}(p)$ obtained with the results for the three largest sizes here considered.

Our results for the percolation threshold and $\delta$ are re- ported in Table I. First, we comment on the case $\lambda/\mu=1$ already considered by other authors. We note that our result for the percolation threshold $p_{c_e}$ is in very good agreement with the most accurate estimate reported up to now, $^{8,14}$ i.e., $p_{c_e} \approx 0.65$. On the other hand, our result for $f/v_e$ (1.1) is also consistent with that of Ref. 8, namely, $1.35 \pm 0.25$.

The results for two additional values of $\lambda/\mu$ are also given in Table I. First, we note that $p_{c_e}$ increases with $\lambda/\mu$. This is consistent with the fact that as $\mu$ tends to zero the percolation threshold should tend to unity. On the other hand, these results can be qualitatively under- stood in terms of a model of noninteracting voids. Extra- polating the small-$p$ limit in Eq. (4) to the whole range of $p$, we obtain

$$
p_{c_e}=(\lambda/\mu+1)/(\lambda/\mu+2). \tag{7}
$$

The overall dependence of $p_{c_e}$ on $\lambda/\mu$ is well described by this formula. On the other hand, a self-consistent effective-medium approximation can be developed along this line. $^7$ This theory, in its most straightforward ver- sion, predicts a value of $p_{c_e}$ independent of $\lambda/\mu$, equal to $\frac{2}{3}$. This result is not confirmed by our numerical calcu- lations. We ascribe the fact that Eq. (7) describes better our findings to the rather small fraction of voids required to reach the percolation threshold. While to obtain Eq. (7) the starting point is the perfect homogeneous system, a self-consistent theory assumes that the properties of the system are close to those of a homogeneous system with the final elastic constants. The neglect of spatial correlations implicit in this approach seems to be a more serious drawback than the assumption of no interactions between voids. This point is further confirmed by our noting that the agreement between the numerical results and Eq. (7) is better for $\lambda/\mu \simeq 1$. It is easy to check that the distribution of elastic energy around a spherical void behaves like $F(r) \sim [1+(1+\lambda/\mu)R^4/r^4]$ where $R$ is the radius of the hole. Thus, the decay of the derivative of this quantity is faster for small values of $\lambda/\mu$, leading to a weaker interaction between voids. Finally, when $\lambda/\mu \to \infty$, both Eq. (7) and the numerical simulations suggest that the percolation threshold is reached for a very small fraction of broken bonds. This is consistent with the fact that, in this case the lattice offers no resis- tance to shear deformations. As voids induce such shear stresses, even under homogeneous pressures, the lattice has a strong tendency to collapse.

<table>
<caption>TABLE I. Results for the percolation threshold and $f/v_e$ obtained in this work for three values of $\lambda/\mu$. Percolation thresholds obtained with Eq. (7) are also given.</caption>
<thead>
<tr>
<th>$\lambda/\mu$</th>
<th>Eq. (7)</th>
<th>$p_{c_e}$</th>
<th>$f/v_e$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0.67</td>
<td>0.64</td>
<td>1.1</td>
</tr>
<tr>
<td>5</td>
<td>0.86</td>
<td>0.71</td>
<td>0.50</td>
</tr>
<tr>
<td>10</td>
<td>0.92</td>
<td>0.84</td>
<td>0.15</td>
</tr>
</tbody>
</table>

Our results for $f/v_e$ are also given in Table I. A very strong dependence of $\delta$ on the elastic constants is noted: For $\lambda/\mu=10$ the ratio $f/v_e$ is reduced by a factor of $\simeq 7$ with respect to the case $\lambda/\mu=1$ previously considered by other authors. The strong dependence of the critical properties of the percolation transition on the elastic con- stants of the continuum medium suggests that the cen- tral-force model does not belong to a new universality class as suggested elsewhere. $^5$

Summarizing, in this paper we have presented a model which, by combining the central-force Hamiltonian and a triangular lattice with unit cell $\sqrt{3} \times \sqrt{3}$, has allowed us to investigate the critical properties of elasticity percola- tion as a function of the elastic components of the con- tinuum medium. Our results indicate that the critical properties do strongly depend on the elastic constants. This conclusion could have not been anticipated from previous analysis of elasticity percolation, and opens new possibilities in the field. Here we mention some ques- tions for future work: (i) calculation of the correlation length exponent, (ii) study of models capable of describ- ing media with $\lambda/\mu$ varying in a wider range (values

below 0.9), and (iii) investigation of whether or not the results depend on the form of the potential energy; this could be done by consideration of different expressions for the potential energy corresponding to media with identical elastic constants.

Partial financial support by the Comisión Asesora de Investigación Científica y Técnica (Spain) and the Gen- eralitat Valenciana is gratefully acknowledged. We are indebted to the Quantum Chemistry Theory Group of the University of Alicante for help and advice in the cal- culations.

$^{1}$Percolation Structure and Processes, edited by G. Deutsch- er, R. Zallen, and Joan Adler, Annals of the Israel Physical So- ciety Vol. 5 (Hilger, Bristol, 1983).

$^{2}$R. Zallen, in Ref. 1, p. 3.

$^{3}$P. G. de Gennes, J. Phys. (Paris), Lett. 37, L1 (1976).

$^{4}$Y. Kantor and I. Webman, Phys. Rev. Lett. 52, 1891 (1984).

$^{5}$S. Feng and P. N. Sen, Phys. Rev. Lett. 52, 216 (1984).

$^{6}$M. Sahimi and J. D. Goddard, Phys. Rev. B 32, 1869 (1985).

$^{7}$L. M. Schwartz, S. Feng, M. F. Thorpe, and P. N. Sen, Phys. Rev. B 32, 4607 (1985).

$^{8}$M. A. Lemieux, P. Breton, and A.-M. S. Tremblay, J. Phys. (Paris), Lett. 46, L1 (1985); A. R. Day, R. R. Tremblay, and A.-M. S. Tremblay, Phys. Rev. Lett. 56, 2501 (1986).

$^{9}$L. D. Landau and E. M. Lifshitz, Theory of Elasticity (Pergamon, New York, 1959).

$^{10}$N. I. Muskhelishvili, Some Basic Problems in the Theory of Elasticity (Noordhoff, Groningen, 1953).

$^{11}$M. P. Nightingale, Physica (Amsterdam) 83A, 561 (1976).

$^{12}$M. N. Barber and W. Selke, J. Phys. A 15, L617 (1982).

$^{13}$M. Sahimi, J. Phys. A 18, 3597 (1985).

$^{14}$M. Sahimi and J. D. Goddard, Phys. Rev. B 33, 7848 (1986).