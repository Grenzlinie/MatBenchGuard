# A simple environment-dependent overlap potential and Cauchy violation in solid argon

Masato Aoki and Tatsuya Kurokawa

Faculty of Engineering, Gifu University Yanagido, Gifu 501-1193, Japan

E-mail: masato@gifu-u.ac.jp

**Abstract.** We develop an analytic and environment-dependent interatomic potential for the overlap repulsion in solid argon, based on an approximate treatment of the non-orthogonal Tight-Binding theory for the closed-shell systems. The present model can well reproduce the observed elastic properties of solid argon including Cauchy violation at high pressures, yet very simple. A useful and novel analysis is given to show how the elastic properties are related to the environment-dependence incorporated into a generic pairwise potential. The present study has a close link to the broad field of computational materials science, in which the inclusion of environment dependence in short-ranged repulsive part of a potential model is sometimes crucial in predicting the elastic properties correctly.

PACS numbers: 62.50.+p, 62.20.Dc

## 1. Introduction

Recent progress of Brillouin spectroscopy at very high pressures[1, 2] has revealed that interatomic forces in fcc solid argon must be far beyond any kinds of two-body, central force model. Shimizu *et al.*[1] precisely measured a large violation of the Cauchy relation up to 70 GPa and stressed the important role of many-body forces, in order to construct good potentials for high-density noble gases, which should be crucial in understanding their behavior in planetary bodies by means of molecular simulations.

The Cauchy relation[3] for the elastic constants of cubic crystals at a hydrostatic pressure $P$ is given by $C_{12} - C_{44} - 2P = 0$, which must be satisfied in centrosymmetric cubic crystals, including the fcc solid argon, if the total energy is given by sum of purely pairwise terms. The deviation from it is therefore a measure of the many-atom nature of interatomic interactions. The Aziz-Slaman model for high pressure argon[4], which might be one of the most sophisticated yet simple ones thus far proposed, fails to reproduce any violation of Cauchy relation, simply because the model is pairwise.

On the other hand, the *ab initio* Density Functional Theory (DFT) approach using the pseudopotential planewave method[5], and that with projector-augmented wave implementation for core electrons[6], and linear muffin-tin orbital (LMTO) method[7, 8] have successfully reproduced the observed elastic constants, as well as the density of the solid argon over the measured range of the pressure. From these theoretical results, it should be a natural

![](./images/867770087329759556_1.jpg)

Figure 1. Total Cauchy violation $\delta$, decomposed into contributions from the kinetic (thin solid), electrostatic (dot-dashed), and exchange-correlation (dashed) energies.

and logical consequence that one would expect to have an simple and reasonably accurate model for the many-atom interaction in condensed argon, by coarse-graining the *ab initio* electronic models to a rather empirical atomistic model.

The importance of many-body forces in solid argon at high pressures has been examined by several authors along the idea of many-atom expansion[9, 10, 11], in which one assumes that the total energy is 'additively' decomposable into $N$-atom ($N=2,3,4\cdots$) terms plus the additional energy of zero-point vibrations, and that the expansion is well convergent. The three-atom contribution from the exchange energy was emphasized[10] because it stabilise argon in fcc structure, rather than the hcp, which is predicted by all the available pairwise models without the zero-point energy[11]. However, it is pointed out that the convergence of this type of expansion becomes worse in a situation in which many-atom effect is more important[11].

Figure 1 shows the Cauchy violation defined by

$$
\delta \equiv C_{12}-C_{44}-2 P, \tag{1}
$$

and its breakdown into the contributions from kinetic, electrostatic and exchange-correlation energies predicted[8] by using all-electron calculation within DFT[12]. Each curve is plotted as a function of the total pressure. Clearly, the central role for the observed negative $\delta$ is played by kinetic energy, which remains after the large cancellation by the opposite contributions from electrostatic and exchange-correlation. It should be noted that non-zero contribution from the electrostatic energy immediately excludes a primitive picture of overlapping frozen atomic charge-density. Therefore, it is implied that deformation of density (wavefunctions) should be relevant.

The purpose of this paper is to develop an analytic interatomic potential for solid argon, that is based on the quantum mechanics of electrons, and that can well reproduce the observed elastic properties including the Cauchy violation at high pressures, yet that is made as simple as possible. The problem we are to treat now has a close link to the broad field of computational materials science, since the inclusion of environment dependence in short-ranged repulsion is sometimes crucial[13, 14, 15, 16] in obtaining reliable and transferable models for simulations in empirical and semi-empirical approaches.

In section 2, a Tight-Binding description for overlap repulsion in closed-shell atoms, which depends on atomic environment, will be presented as the theoretical base that underpins more empirical and analytic model. General properties of repulsive potential with environment-dependent parameters are analysed, and a simple functional form for the overlap repulsion is designed for argon and proposed in section 3. The result of the fitted analytic potential is presented in section 4, followed by a concluding section 5.

## 2. Environment-dependent overlap repulsion: Tight-Binding description

A system of closed-shell atoms may be well described within the non-orthogonal Tight-
Binding Bond Model (TBBM)[17, 18], in which the total binding energy is given by

$$
E_{\mathrm{B}}=E_{\mathrm{cov}}+E_{\mathrm{ren}}+E_{\mathrm{rep}}+E_{\mathrm{vdW}}. \tag{2}
$$

The first term is the covalent energy

$$
E_{\mathrm{cov}}=2 \mathrm{Tr}\left[\mathrm{HS}^{-1}\right]-2 \mathrm{Tr}[\mathrm{H}]=-2 \mathrm{Tr}\left[\mathrm{HOS}^{-1}\right], \tag{3}
$$

where H and $S=1+O$ are the Hamiltonian and overlap matrices defined by

$$
(\mathrm{H})_{i \mu, j \nu}=\int \psi_{i \mu}^{*}(\mathbf{r}) \hat{H} \psi_{j \nu}(\mathbf{r}) \mathrm{d}^{3} r \tag{4}
$$

and

$$
(\mathrm{S})_{i \mu, j \nu}=\delta_{i, j} \delta_{\mu, \nu}+(\mathrm{O})_{i \mu, j \nu}=\int \psi_{i \mu}^{*}(\mathbf{r}) \psi_{j \nu}(\mathbf{r}) \mathrm{d}^{3} r, \tag{5}
$$

in a basis set of atomic orbitals $\psi_{i \mu}$, where $\mu$ runs over orbitals on site $i$. The spin degeneracy enters as the prefactor 2 before the usual symbol $\operatorname{Tr}$ for the trace. The Hamiltonian operator $\hat{H}$ refers to the density of superposition of frozen atomic densities[18, 17]. Note that the inverse overlap matrix, $S^{-1}$, in Eq.(3) is equivalent to the density matrix in this case of fully occupied system. The second term in Eq. (2), $E_{\mathrm{ren}}$, is defined by

$$
E_{\text {ren }}=2 \operatorname{Tr}[\mathrm{H}]-2 \operatorname{Tr}\left[\mathrm{H}_{\mathrm{fa}}\right], \tag{6}
$$

which accounts for the on-site energy shift due to the contraction or localisation of free atomic orbitals on going into a condensed environment, and $\mathrm{H}_{\mathrm{fa}}$ is a diagonal matrix of the free atomic energy levels. $E_{\text {rep }}$ represents the contribution from the change in the electrostatic and exchange-correlation energies associated with frozen atomic charge densities as they are brought together from the free space. Thus, this term is environmentally independent by construction, and usually approximated as a sum of repulsive pair-wise potentials between atoms. $E_{\mathrm{vdW}}$, added supplementarily to TBBM, denotes the van der Waals potential, which may be approximated using the empirical pair-wise inverse power function of interatomic separation, that is $-c_{6} R_{i j}^{-6}$.

In order to illustrate that Eq.(3) essentially represents the overlap repulsion, we now consider only the outermost $p$-shell states as the basis, and then the bond integral[19] part, B, may be separated from H as

$$
\mathrm{H}=\epsilon_{p} \mathrm{~S}+\mathrm{B}, \tag{7}
$$

The set of solutions is indeed environment-dependent and we see that the constant $\kappa_{i0}$ is the solution for the limiting case of infinitely separated atoms. Since the penalty due to increase in the kinetic energy is steep, $\Delta \kappa_{i}/\kappa_{i0}$ would be small enough to replace $\kappa_{i}$ in the exponential in Eq.(14) with $\kappa_{i0}$. This solves the equation to give explicit $\Delta \kappa_{i}$ that is exact to first order. The energy increase $\Delta E_{\text{ren}}$ due to this minimisation is given exactly by the sum of $3(\Delta \kappa_{i})^{2}$, which partially sets off and just halves the lowest order decrease in overlap energy $\Delta E_{\text{ovl}}$. The resultant lowering, $\frac{1}{2}\Delta E_{\text{ovl}}$, could be obtained by employing $\frac{1}{2}\Delta \kappa_{i}$ instead of $\Delta \kappa_{i}$ in the overlap energy. This treatment *eliminates* $\Delta E_{\text{ren}}$ and simplifies the functional form of the potential, which is to be proposed in the next section.

The environmental effect that we are looking at is a tendency that more contracted atomic orbitals are preferred in a denser environment. The physics behind it has been beautifully justified in the pioneering work by Skinner and Pettifor[21], who have implemented the chemical pseudopotential theory using the orbital exponent as a variational parameter within the Harris-Foulkes scheme[22, 23], and found that the orbital exponents ($\kappa$'s in our notation) of hydrogen atoms in molecule, simple cubic and fcc lattices are strongly environment-dependent as stated above.

### 3. Analytic model for solid argon

Let us first analyse some general properties of a repulsive potential that is a function of environment-dependent parameters as well as the distance.

Provided that the functional form of repulsive interatomic potential is given by
$$
\Phi_{i j}\left(R_{i j} ; \lambda_{i}+\lambda_{j}\right)
\tag{15}
$$
with the environment-dependent parameters ($\lambda$'s) that are written as a sum of pairwise functions, namely
$$
\lambda_{i}=\sum_{k(\neq i)} \rho\left(R_{i k}\right).
\tag{16}
$$

Cauchy violation can be calculated analytically for cubic lattice. The result is written[8]
$$
\delta=\frac{2}{9 \Omega}\left[\alpha_{0}^{2} \sum_{j(\neq 0)} \frac{\partial^{2} \Phi_{0 j}}{\partial \lambda_{0}^{2}}+\alpha_{0} \sum_{j(\neq 0)} R_{j} \frac{\partial^{2} \Phi_{0 j}}{\partial R_{j} \partial \lambda_{0}}\right]
\tag{17}
$$
with
$$
\alpha_{0}=\sum_{k(\neq 0)} R_{k} \rho^{\prime}\left(R_{k}\right),
\tag{18}
$$
where $\Omega$ is the atomic volume and $R_{j}=R_{0 j}=\sqrt{x_{j}^{2}+y_{j}^{2}+z_{j}^{2}}$ is the distance to atom $j$ from the central atom $i=0$ at the origin. The prime on $\rho$ denotes the distance derivative. Note that all lattice sites are equivalent under a homogeneous strain. $\alpha_{0}$ represents the strength of environmental effect on atom 0. Since $\rho(R)$ at this point is completely arbitrary, we may assume that it is a positive and monotonically decreasing function of distance in the range of interest; hence $\alpha_{0}<0$. It may also be a physically reasonable assumption that the repulsive potential $\Phi_{0 j}(>0)$ is also a monotonically decreasing function of distance in the range of

interest. We see from Eq.(17) for the case of very weak $\alpha_0$ that negative Cauchy violation occurs if $\partial^2\Phi_{0j}/\partial R_j\partial\lambda_0 > 0$. This condition is likely to be fulfilled, since an environmental effect tends to weaken the overlap repulsion to give $\partial\Phi_{0j}/\partial\lambda_0 < 0$, as we have seen in the previous section. The expression for the pressure from $\Phi$ is given by

$$
P=-\frac{1}{6 \Omega}\left[\sum_{j(\neq 0)} R_{j} \frac{\partial \Phi_{0 j}}{\partial R_{j}}+2 \alpha_{0} \sum_{j(\neq 0)} \frac{\partial \Phi_{0 j}}{\partial \lambda_{0}}\right].
\tag{19}
$$

The first term in the square bracket represents the pairwise component. We see environmental effect, the second term, causes reduction in pressure as expected.

A simple functional form of overlap repulsion that takes into account the physics of the environment effect as we have discussed is now proposed, that is,

$$
\Phi_{i j}\left(R_{i j} ; \lambda_{i}+\lambda_{j}\right)=\exp \left(-\lambda_{i}\right) \exp \left(-\lambda_{j}\right) V_{R}\left(R_{i j}\right),
\tag{20}
$$

where $V_R$ is environmentally independent pairwise function. The environmental effect on site $i$ is entering in a very simple separable form by a factor $\exp(-\lambda_i)$, which corresponds to the contraction factor $\exp(-\Delta\kappa_i R_{ij})$. However, the direct dependence on the particular length $R_{ij}$ has been dropped for simplicity. This manner of parameterisation for the environmental effect can also be seen in the 'breathing-shell model' (See Ref. [24, 25] and references therein) and 'compressible ion model'[26] for oxides, such as MgO. The both models are provided with the parameters that correspond to the variation in effective size of ionic cores, and reduction in core size causes exponential reduction as $\lambda_i$ in the present model does. It should be noted that a kind of penalty function has been eliminated from the present model as it was justified in the previous section. The contraction factor of type $\exp(-\Delta\kappa_i R_{ij})$ was modelled by Nguyen-Manh *et al.* in the form of screened Yukawa-type potential[16, 15] and it was used to explain Cauchy pressures in transition metals intermetallics within a Tight-Binding and Harris-Foulkes approaches.

It follows from the functional form proposed above that full expressions for the pressure $P$, Cauchy violation $\delta$, adiabatic bulk modulus $B$, and the cubic elastic constants $C_{11}, C_{12}, C_{44}$ are given by

$$
\begin{aligned}
P &=\frac{1}{3}\left(-v+2 u \alpha_{0}\right), \tag{21} \\
\delta &=\frac{4}{9}\left(-\alpha_{0} v+u \alpha_{0}^{2}\right), \tag{22} \\
B &=\frac{2}{3} P+\frac{1}{3} K+\delta, \tag{23} \\
C_{11} &=-P+P^{s}+K^{s}+\delta, \tag{24} \\
C_{12} &=\frac{1}{2}\left(3 P+K-P^{s}-K^{s}\right)+\delta, \tag{25} \\
C_{44} &=\frac{1}{2}\left(-P+K-P^{s}-K^{s}\right) \tag{26}
\end{aligned}
$$

with

$$
\begin{aligned}
P^{s} &=\frac{1}{3}\left(-v^{s}+2 u \alpha_{0}^{s}\right), \tag{27} \\
K &=\frac{1}{3}\left(w-2 u \beta_{0}\right), \quad K^{s}=\frac{1}{3}\left(w^{s}-2 u \beta_{0}^{s}\right), \tag{28}
\end{aligned}
$$

where $u$ equals the energy density and $v, w$ also are similar quantities determined by first- and second-order derivatives of the potential, and $u^s, v^s, w^s$ are weighted sums. These are defined

![](./images/867770087329759556_2.jpg)

Figure 2. The Cauchy violation, $\delta$, and pressure, $P$, as a function of strength of environment-dependence, $\alpha_0$, for the repulsive potential.

by

$$
u = \frac{1}{2\Omega} \sum_{j(\neq 0)} \Phi_{0j}, \quad u^s = \frac{1}{2\Omega} \sum_{j(\neq 0)} \Phi_{0j} s_j, \tag{29}
$$

$$
v = \frac{1}{2\Omega} \sum_{j(\neq 0)} R_j \Phi_{0j}^\prime, \quad v^s = \frac{1}{2\Omega} \sum_{j(\neq 0)} R_j \Phi_{0j}^\prime s_j, \tag{30}
$$

$$
w = \frac{1}{2\Omega} \sum_{j(\neq 0)} R_j^2 \Phi_{0j}^{\prime\prime}, \quad w^s = \frac{1}{2\Omega} \sum_{j(\neq 0)} R_j^2 \Phi_{0j}^{\prime\prime} s_j, \tag{31}
$$

with $s_j = (x_j^4 + y_j^4 + z_j^4)/R_j^4$. Together with $\alpha_0$, three of other quantities representing the strength of environment-dependence are defined:

$$
\alpha_0^s = \sum_{k(\neq 0)} R_k \rho^\prime(R_k) s_k, \tag{32}
$$

$$
\beta_0 = \sum_{k(\neq 0)} R_k^2 \rho^{\prime\prime}(R_k), \quad \beta_0^s = \sum_{k(\neq 0)} R_k^2 \rho^{\prime\prime}(R_k) s_k. \tag{33}
$$

Equations (21) and (22), seen as a linear and quadratic functions of $\alpha_0$ respectively, explain how the negative Cauchy violation occurs when an environment-dependence is introduced, as presented instructively in Fig. 2. It is to be noted that $\alpha_0 = v/(2u)$ is unphysical point where our 'repulsive' potential is found no longer repulsive, giving $P = 0$. Therefore, the magnitude of dimensionless parameter $\alpha_0$ should usually be much smaller than $|v/(2u)|$. An instructive example may be the case of inverse-power-law potential, $\Phi \propto R^{-n}$, in which the critical value can be easily found to be $v/(2u) = -n/2$. These analysis should be useful in understanding how the environmental dependence in repulsive worked for the problem of small or negative Cauchy pressure ($C_{12}-C_{44}$ for cubic systems, $C_{13}-C_{44}$ and $C_{12}-C_{66}$ for tetragonal or hexagonal systems) in transition metals and intermetallic compounds[16, 15]. In these covalently bonded systems at equilibrium, a negative pressure $P_{\text{bond}}$ from the attractive covalent bond energy counterbalances the positive one from the repulsion. In Fig. 2, this situation corresponds to the 'high pressure' case in which $P = |P_{\text{bond}}|$ and a negative contribution of $\delta$ with $v/(2u) < \alpha_0 < 0$.


<table>
<caption>Table 1. Fitted parameters in $V_R$ and $\rho$.</caption>
<thead>
<tr>
<th>$A$ (J)</th>
<th>$a_1$ (Å$^{-1}$)</th>
<th>$a_2$ (Å$^{-2}$)</th>
<th>$\mu_1$ (Å$^{-1}$)</th>
<th>$\mu_2$ (Å$^{-2}$)</th>
<th>$g$</th>
<th>$\nu$ (Å$^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$2.10{\times}10^{-15}$</td>
<td>$-0.5819$</td>
<td>$0.09309$</td>
<td>$3.000$</td>
<td>$-0.03996$</td>
<td>$80.0$</td>
<td>$3.60$</td>
</tr>
</tbody>
</table>

![](./images/867770087329759556_3.jpg)

Figure 3. Left: Pressure versus lattice constant. Circles denote X-ray observation. (see references in [1]) Right: Elastic constants versus pressure: The present model (solid lines) compared with experimental results by Shimizu et al. [1].

Finally, parameterisations for functions $V_R(R)$ in Eq.(20) and $\rho(R)$ in Eq.(16) must be determined. They are basically similar and described by a superposition of the square of two-center overlap integrals. Using Eqs. (11) and (14) as a guide, we employ the following functions, namely
$$
V_R(R) = A(1+a_1R+a_2R^2)\mathrm{exp}(-\mu_1R-\mu_2R^2) \tag{34}
$$
and
$$
\rho(R) = g\mathrm{exp}(-\nu R), \tag{35}
$$
where the parameters $A, \mu_1, g, \nu$ are essential, and $a_1, a_2, \mu_2$ are for flexibility of the fitting.

We do not explicitly include the pairwise $E_{\text{rep}}$ in the present model, because it is actually unknown, but may not be dominant, and therefore we may think of it as being absorbed effectively in the pairwise component of overlap repulsion unless it proves significant.

### 4. Results
Using the model of overlap repulsion plus the pairwise van der Waals potential $(-c_6R_{ij}^{-6})$ with the Lennard-Jones parameters for argon[27], i.e. $c_6 = 4\varepsilon\sigma^6$ with $\varepsilon = 1.67 \times 10^{-21}$ J and $\sigma = 3.40$ Å, the parameters are fitted to the results[8] by ab initio full-potential LMTO

calculations with the generalized gradient approximation of PW91 (GGA-PW91)[28] for the exchange-correlation, since GGA-PW91 results are remarkably in good agreement with the experimental results for solid argon. However, GGA-PW91 is known to predict always positive pressures, and a small positive pressure even at the experimental lattice constant $a = 5.13$ Åfor the equilibrium at zero pressure. The adjusted parameters are listed in Table 1.

Figure 3 shows the elastic properties of fcc solid argon predicted by the present model compared with the experimental results. The agreement is impressive. However, a negative curvature in predicted $\delta$ at very high pressures can be seen as a small deviation, which is reflected in $B$, $C_{11}$, $C_{12}$ (and not in $C_{44}$) as it can be understood from $\delta$-term (and its absence) in Eqs.(23)-(26). This will be corrected if we design more flexible function for $\rho$. But if we do so, we also need to evaluate neglected terms, for example, the higher order many-atom effects due to $(1+\mathrm{O})^{-1}$ factor, which will be handled in a separate study.

The stability problem of fcc against hcp is still very subtle even with the present environment-dependent model without zero point energy. The result is very sensitive to the cutoff. For example, using only the present repulsive model (without $E_{\mathrm{vdW}}$), the fcc–hcp difference in enthalpy is evaluated to be $-0.01$ meV at 20 GPa and $0.11$ meV at 60 GPa if we include 86 neighbours within 6 shells in fcc and equivalently within 9 shells in hcp. The difference in the zero point energy[9] would be dominant. Therefore the environmental or many-atom effect in overlap repulsion may not be a remedy for the problem of fcc stability.

## 5. Conclusion
We have developed an analytic and environment-dependent interatomic potential for the overlap repulsion in solid argon. The functional form, of environment-dependence in particular, is simple and physically transparent, being based on the non-orthogonal Tight- Binding theory for the closed-shell systems. The present model was shown to well reproduce the observed elastic properties of solid argon including the Cauchy violation at high pressures.

A useful and novel analysis has clearly demonstrated how the elastic properties are related to the environment-dependence incorporated into a generic pairwise potential. It is speculated that the present functional provides not only excellent description for elastic properties of a solid noble gas, but also useful description for the problem of small or negative Cauchy pressures in covalently bonded systems.

## 6. Acknowledgments
The authors would like to thank Dr. Duc Nguyen-Manh for useful conversations about their works on Cauchy pressure, Prof. Y. Shimizu and S. Sasaki for helpful information of their experiments, and Dr. T. Iitaka for stimulating information at the onset of the present study. MA thanks the Kogyo-Club of the Faculty of Engineering, Gifu University for financial support.

### References

[1] Shimizu, H., Tashiro, H., Kume, T. and Sasaki, S., Phys. Rev. Lett. **86**, 4568 (2001).

[2] Grimsditch, M., Loubeyre, P. and Polian, A., Phys. Rev. **B 33**, 7192 (1986).

[3] Born, M. and Huang, K., *Dynamical theory of crystal lattices*, (Oxford University Press, 1954).

[4] Aziz, R. A. and Slaman, M. J., J. Chem. Phys. **92**, 1030 (1990).

[5] Iitaka, T. and Ebisuzaki, T., Phys. Rev. **B 65**, 012103 (2002).

[6] Tse, J.S. Klug, D.D., Shpakov, V, and Rodgers, J.R., Solid State Commun., **122**, 575 (2002).

[7] Tsuchiya, T. and Kawamura, K., J. Chem. Phys. **117**, 5859 (2002), and references therein.

[8] Aoki, M., Rev. High Pressure Sci. Techn. **13** (in Japanese), 218 (2003).

[9] Rosciszewski, K., Paulus, B., Flude, P. and Stoll, H., Phys. Rev. **B 62**, 5482 (2000).

[10] Lotrich, V.F. and Szalewicz, K., Phys. Rev. Lett. **79**, 1301 (1997).

[11] Schwerdtfeger, P., Gaston, N., Krawczyk, R.P., Tonner, R. and Moyano, G.E., Phys. Rev. **B 73**, 064112 (2006).

[12] Savrasov, S.Yu. and Savrasov, D.Yu., Phys. Rev. **B 46**, 12181 (1992).

[13] Tang, M.S., Wang, C.Z., Chan, C.T. and Ho, K.M., Phys. Rev. **B 53**, 979 (1996).

[14] Haas, H., Wang, C.Z., Fahnle, M., Elsasser, C. and Ho, K.M., Phys. Rev. **B 57**, 1461 (1998).

[15] Mrovec, M., Nguyen-Manh, D., Pettifor, D.G. and Vitek, V., Phys. Rev. **B 69**, 94115 (2004).

[16] Nguyen-Manh, D., Pettifor, D.G., Znum, S. and Vitek, V., *Tight-Binding approach to computational Materials Science* , Turchi, P.E.A., Gonis, A., and Colombo, L., (Eds.) (Mater. Res. Soc. Symp. Proc. 491), pp 353-358, (MRS, 1998).

[17] M.W. Finnis, *Interatomic forces in condensed matter*, (Oxford University Press, 2003).

[18] Sutton, A.P., Finnis, M.W., Pettifor D.G. and Ohta, Y., J. Phys. **C 21**, 35 (1988).

[19] Pettifor, D.G., *Bonding and structure in molecules and solids* (Oxford University Press, 1995).

[20] Nguyen-Manh, D., Pettifor and Vitek, V., Phys. Rev. Lett. **85**, 4136 (2000).

[21] Skinner, A.J. and Pettifor, D.G., J. Phys.:Cond. Mat. **3**, 2029 (11991).

[22] Harris, J., Phys. Rev., **B 31**, 1770 (1985).

[23] Foulkes, W.M.C. and Haydock, R., Phys. Rev., **B 39**, 12520 (1989).

[24] Sangster, M.J.L., J. Phys. Chem. Solids. **34**, 355 (1973).

[25] Matsui, M., J. Chem. Phys. **108**, 3304 (1998).

[26] Marks, N. A., Finnis, M. W., Harding, J. H. and Pyper, N. C. J. Chem. Phys. **114**, 4406 (2001).

[27] Kittel, C., *Introduction to solid state physics* Eighth edition. (John Wiley & Sons, 2005)

[28] Perdew, J. P., in Electronic Structure of Solids'91, eds. Ziesche, P., Eschrig, H. (Akademie Verlag, Berlin, 1991).