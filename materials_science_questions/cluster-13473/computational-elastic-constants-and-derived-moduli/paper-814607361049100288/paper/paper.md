# Can the Thermodynamic Properties of a Solid Be Mapped onto Those of a Liquid?
James F. Lutsko and Marc Baus
Campus Plaine, Case Postale 231, Universitá Libre de Bruxelles, B-1050 Brussels, Belgium
(Received 31 August 1989)

A new approximation to the density-functional theory of classical nonuniform systems is proposed and worked out for the case of the hard-sphere solid. The theory satisfies all the formal properties of the free energy and requires only the direct correlation function of the uniform system as input. The agreement with the computer simulations of the fcc hard-sphere solid is excellent: The resulting free energies, pressures, and fluid-solid coexistence data are reproduced to within the error bars of the simulations. The theory also predicts stable bcc and sc phases which could facilitate the final nucleation into the equilibrium fcc phase.

PACS numbers: 64.10.+h, 05.70.Fh, 64.70.Dv

The first-principles description of nonuniform equilibrium phases and phase existences remains one of the basic problems of equilibrium statistical mechanics. Increasing evidence has been gained in recent years¹ that it is possible to describe nonuniform phases by using only our knowledge about the uniform phase as input. If, for concreteness, we consider the liquid-solid coexistence, then it may be quite surprising to hear that the highly organized solid (the nonuniform system) can be described in terms of the liquid (the uniform system). This is nevertheless the idea which was put forward some years ago by Ramakrishnan and Yussouf.² These authors did, however, compute the properties of the solid as a perturbation of those of the coexisting liquid. The validity of this latter step was felt to be a problem since the very beginning³ while, now, the recent results of Curtin⁴ seem to call it definitively into question. Meanwhile, several authors³⁻⁷ have used the same basic idea to formulate nonperturbative theories which bypass this criticism. The present investigation is concerned with the formulation of such a nonperturbative theory which pushes to its extreme consequences the original idea of describing the thermodynamic properties of the solid in terms of those of a liquid. This theory satisfies all formal properties and yields amazingly accurate results when tested for the hard-sphere solid.

The (Helmholtz) free energy of the solid, $F[\rho]$, is a functional of the local density of the solid, $\rho(\mathbf{r})$, and the usual density-functional notation and relations will therefore be used throughout here.⁸ In general, $F$ can be written as the sum of two terms,⁹ $F=F_{\text{id}}+F_{\text{ex}}$, an ideal-gas term, $F_{\text{id}}$, and an excess term, $F_{\text{ex}}$, due to the interactions. For $F_{\text{id}}$ we have⁸
$$
\beta F_{\text{id}}[\rho]=\int d \mathbf{r} \rho(\mathbf{r})\left\{\ln \left[\lambda^{3} \rho(\mathbf{r})\right]-1\right\}, \tag{1}
$$
where $\beta=1 / k_{B} T$ is the inverse temperature and $\lambda$ is the thermal wavelength. Whereas Eq. (1) is exact, we propose here for $F_{\text{ex}}$ the following approximation:¹⁰
$$
\beta F_{\text{ex}}[\rho]=-\int d \mathbf{r} \int d \mathbf{r}^{\prime} \int_{0}^{1} d \lambda \int_{0}^{\lambda} d \lambda^{\prime} \rho(\mathbf{r}) \rho\left(\mathbf{r}^{\prime}\right) c\left(\left|\mathbf{r}-\mathbf{r}^{\prime}\right| ; \rho\left[\lambda^{\prime} \rho\right]\right), \tag{2}
$$
where $c(|\mathbf{r}| ; \hat{\rho})$ is the direct correlation function (DCF) of the liquid evaluated at a uniform density $\hat{\rho}$ which is used here to "effectively" describe the solid of local density $\rho(\mathbf{r})$. Notice that Eq. (2) differs from the exact expression⁷⁻⁸ of $F_{\text{ex}}$ only in that the DCF of the solid has been replaced by the DCF of an effective liquid of density $\hat{\rho}$. The approximation underlying Eq. (2) is thus based on the idea that it is possible to map the (density averaged) DCF of the solid [which is all that matters for Eq. (2)] onto the DCF of some equivalent liquid which we call the effective liquid resulting from this "structural" mapping. In order to uniquely specify this mapping, we will assume moreover that the effective liquid which optimizes this mapping is the one which at the same time as it maps the structure, also maps some intensive thermodynamic property of the solid, say its excess free energy per particle, $\phi_{\text{ex}}[\rho]=F_{\text{ex}}[\rho] / N$, onto that of the effective liquid, say $\phi_{\text{ex}}(\hat{\rho})$. This "thermodynamic" mapping is thus explicitly defined by the equation, $\phi_{\text{ex}}[\rho]=\phi_{\text{ex}}(\hat{\rho})$, where $\hat{\rho}$ is now the effective liquid which reproduces both the averaged DCF of the solid and its excess free energy per particle. Using then the known density-functional expressions⁷⁻⁸ one immediately obtains the following relations defining the effective density $\hat{\rho}$, viewed as a functional of $\rho(\mathbf{r})$, $\hat{\rho}=\hat{\rho}[\rho]$:
$$
\hat{\rho}[\rho]=\frac{1}{\rho_{S} V} \int d \mathbf{r} \int d \mathbf{r}^{\prime} \rho(\mathbf{r}) \rho\left(\mathbf{r}^{\prime}\right) w\left(\left|\mathbf{r}-\mathbf{r}^{\prime}\right| ;[\rho]\right), \tag{3}
$$
where $\rho_{S} V=\int d \mathbf{r} \rho(\mathbf{r})$ is the number of particles, $\rho_{S}$ being the average solid density, and $V$ the volume. Notice from Eq. (3) that $\hat{\rho}$ has the formal appearance of a doubly weighted solid density with a weighting function,

© 1990 The American Physical Society

$w(|\mathbf{r}| ;[\rho])$, explicitly defined as $^{10}$

$$
w(|\mathbf{r}| ;[\rho])=\frac{\int_{0}^{1} d \lambda \int_{0}^{1} d \lambda^{\prime} c\left(|\mathbf{r}| ; \hat{\rho}\left[\lambda^{\prime} \rho\right]\right)}{\int_{0}^{1} d \lambda \int_{0}^{1} d \lambda^{\prime} \int d \mathbf{r}^{\prime} c\left(\left|\mathbf{r}^{\prime}\right| ; \lambda^{\prime} \hat{\rho}[\rho]\right)}, \quad(4)
$$

so that the solution to Eqs. (3) and (4) defines $\hat{\rho}[\rho]$ and Eqs. (1) and (2) define then the present "generalized effective liquid approximation" (GELA) to the free energy of the solid. The previously introduced $^{7}$ self-consistent effective liquid approximation (SCELA) differs from Eqs. (1)-(4) in that $\hat{\rho}[\lambda^{\prime} \rho]$ appearing in Eqs. (2) and (4) was approximated as $\lambda^{\prime} \hat{\rho}[\rho]$. Although it was not realized at that time, this difference is quite crucial. Indeed, because Eq. (2) has now the same functional dependence on $\rho(\mathbf{r})$ as the exact $F_{\text {ex }}[\rho]$ it follows that all the functional relations between $F_{\text {ex }}$ and the DCF are preserved by Eq. (2). In particular, it follows from Eq. (2) that we have the property $(n \geq 2)$

$$
\frac{\delta^{n} \beta F_{\text {ex }}[\rho]}{\delta \rho\left(\mathbf{r}_{1}\right) \cdots \delta \rho\left(\mathbf{r}_{n}\right)}=-\frac{\delta^{n-2} c\left(\left|\mathbf{r}_{1}-\mathbf{r}_{2}\right| ; \hat{\rho}[\rho]\right)}{\delta \rho\left(\mathbf{r}_{3}\right) \cdots \delta \rho\left(\mathbf{r}_{n}\right)}, \quad(5)
$$

which for $n=2$ is nothing but the differential form of Eq. (2) and for $n>2$ defines the higher-order DCF of the solid in terms of the ordinary DCF of the effective liquid. Notice that Eq. (5) holds as such, not only in the uniform limit as assumed in some alternative theories. $^{5,6}$ It appears thus that the GELA, defined by Eqs. (1)-(4), is the most fully self-consistent realization possible of the very idea of mapping the (excess) thermodynamic properties of the solid onto those of an (effective) liquid. In this respect it may be worthwhile to observe here some of the alternative theories, based on postulating $^{6}$ the form of Eq. (3) and requiring Eq. (5) to hold in the uniform limit, $^{5,6}$ have introduced a normalized weighting function, whereas it is seen here from Eq. (4) that $w(|\mathbf{r}| ;[\rho])$ is normalized only in the uniform limit, $^{11}$ which is all that is physically required. The price we have to pay for this extreme generality of the GELA is that, because of the simultaneous appearance of $\hat{\rho}[\rho]$ and $\hat{\rho}[\lambda^{\prime} \rho]$, Eqs. (3) and (4) are more difficult to solve here than in the SCELA. $^{7}$

Since the GELA has very satisfactory formal properties we have tested it for its quantitative predictions in the particular case of the hard-sphere (HS) solid, a typical testing ground within this context. The HS implementation of the theory is very simple: For the DCF of the fluid phase we have used the well-known analytic Percus-Yevick (PY) expression $^{3,12}$ while the density of the solid has been parametrized in terms of Gaussian profiles:

$$
\rho(\mathbf{r})=\left(\frac{\alpha}{\pi}\right)^{3 / 2} \sum_{\mathbf{R}} \exp \left[-\alpha(\mathbf{r}-\mathbf{R})^{2}\right], \quad(6)
$$

with $\{\mathbf{R}\}$ denoting here the Bravais lattice vectors of the fcc crystal. In Eq. (6), the inverse width, $\alpha$, is seen to play the role of the order parameter. For large positive values of $\alpha$, Eq. (6) describes strongly localized particles, which gradually delocalize as $\alpha$ decreases, while Eq. (6) tends finally to a uniform fluid density for vanishing $\alpha$.

![](./images/814607361049100288_1.jpg)

FIG. 1. The complete phase diagram of hard spheres in the pressure $(P^{*}=\beta P \sigma^{3})$ vs density $(\eta=\rho \sigma^{3} \pi / 6)$ plane, consisting of a fluid branch, a solid branch, and a tie line separating each branch into a stable and a metastable portion. The circles correspond to the simulation results (Ref. 14), the lines to the theory [GELA, ELA (Ref. 3), and WDA (Ref. 5)]. On the scale of the figure the pressures obtained from the SCELA (Ref. 7) [MWDA (Ref. 6)] cannot be distinguished from those of the GELA (WDA), although the tie lines could (see Table I).

TABLE I. The fluid-fcc-solid coexistence data as computed from the nonperturbative density-functional theories of hardsphere freezing and compared to the Monte Carlo (MC) simulation results. Here $\eta=\frac{1}{6} \pi \sigma^{3} \rho$ is the packing fraction of the coexisting solid $(S)$ and fluid $(F)$ phases of hard spheres of diameter $\sigma$ and density $\rho$. Further, $\Delta \rho^{*}=\rho_{S}^{*}-\rho_{F}^{*}$ is the density change $(\rho^{*}=\rho \sigma^{3}), P^{*}=\beta P \sigma^{3}$ is the reduced pressure, $\Delta s$ is the change in entropy per particle, and $L$ is the Lindemann parameter (root-mean-square displacement divided by the nearest-neighbor distance). WDA denotes the weighted-density approximation and MWDA denotes the modified weighteddensity approximation.

<table>
<thead>
<tr>
<th>
</th>
<th>
$\eta_{F}$
</th>
<th>
$\eta_{S}$
</th>
<th>
$\Delta \rho^{*}$
</th>
<th>
$P^{*}$
</th>
<th>
$\Delta s/k_{B}$
</th>
<th>
$L$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
MC $^{\text{a}}$
</td>
<td>
0.494
</td>
<td>
0.545
</td>
<td>
0.097
</td>
<td>
11.7
</td>
<td>
1.16
</td>
<td>
0.126
</td>
</tr>
<tr>
<td>
GELA $^{\text{b}}$
</td>
<td>
0.495
</td>
<td>
0.545
</td>
<td>
0.095
</td>
<td>
11.9
</td>
<td>
1.15
</td>
<td>
0.100
</td>
</tr>
<tr>
<td>
SCELA $^{\text{c}}$
</td>
<td>
0.508
</td>
<td>
0.560
</td>
<td>
0.099
</td>
<td>
13.3
</td>
<td>
1.27
</td>
<td>
0.084
</td>
</tr>
<tr>
<td>
WDA $^{\text{d,e}}$
</td>
<td>
0.480
</td>
<td>
0.547
</td>
<td>
0.129
</td>
<td>
10.4
</td>
<td>
1.41
</td>
<td>
0.093
</td>
</tr>
<tr>
<td>
MWDA $^{\text{c}}$
</td>
<td>
0.476
</td>
<td>
0.542
</td>
<td>
0.126
</td>
<td>
10.1
</td>
<td>
1.35
</td>
<td>
0.097
</td>
</tr>
<tr>
<td>
ELA $^{\text{f}}$
</td>
<td>
0.520
</td>
<td>
0.567
</td>
<td>
0.090
</td>
<td>
16.1
</td>
<td>
1.36
</td>
<td>
0.074
</td>
</tr>
</tbody>
</table>

$^{\text{a}}$From Hoover and Ree (Ref. 14).
$^{\text{b}}$From this work.
$^{\text{c}}$From Baus (Ref. 7) and this work.
$^{\text{d}}$From Curtin and Ashcroft (Ref. 5).
$^{\text{e}}$From Denton and Ashcroft (Ref. 6).
$^{\text{f}}$From Baus and Colot (Ref. 3).

The spatial integrals in Eqs. (2) and (3) can be evalu- ated analytically, just as in the original effective liquid approximation (ELA). $^{3,13}$ We then solve Eqs. (3) and(4) for $\hat{\rho}=\hat{\rho}(\alpha, \rho_{S})$ , which now becomes a function of $\alpha$  and of the average solid density $\rho_{S}$ . The result yields a $\hat{\rho}(\alpha, \rho_{S})$ which is a rapidly decreasing function of $\alpha$ . As a consequence all the stable solids, corresponding to the $\alpha$ value for which the free energy is minimum, $^{1}$ can be described by values of $\hat{\rho}$ which are sufficiently low for the PY approximation to remain essentially exact. The re- sulting free energy and pressure of the perfect fcc HS crystal are within a few percent of the simulation re- sults $^{14}$ (see Fig. 1). The fcc solid first stabilizes at n=0.465, remains metastable relative to the fluid up to n=0.515, above which it becomes the thermodynamical- ly favored phase (at constant density). Here $\eta$ is the re duced density, or packing fraction, appropriate to the PY description: $\eta=\frac{1}{6} \pi \sigma^{3} \rho_{S}$ for HS of diameter $\sigma$ . The fluid-solid coexistence can then be located accurately by using for the HS fluid free energy the virtually exact Carnahan-Starling approximation. $^{12}$ The results are displayed in Table I where it is seen that the GELA pre- dictions are within the error bars of the simulation re- sults.

One exception to this rather amazing accuracy of the GELA is the Lindemann parameter which is too low. This can be understood by observing that this quantity is the most model-dependent one, so that the Gaussian- profile approximation of Eq. (6) could be responsible for this disagreement. There remains little doubt, however, that the possibility to map the solid onto some effective liquid, as described by the GELA, is a real one. It is also of interest to observe (see Table I) that the SCELA, al- though not sharing the property of Eq. (5), constitutes a good approximation to the GELA. As a topic for further research $^{15}$ we have also investigated the stability, within the GELA, of the other cubic HS crystals. We have found that the fcc phase is the most stable one, followed by the bcc phase, $^{16}$ the simple cubic (sc) phase, and the fluid phase, in this order. In each case, the free-energy gap separating the (meta)stable solid from the fluid phase increases, as does also the corresponding $\alpha$ value of the solid, according to the sc-bcc-fcc sequence. This then suggests the interesting possibility that these meta- stable HS solids could play some role, as intermediate phases, in the final nucleation of the equilibrium fcc phase.

1For recent reviews, see, e.g., A. D. J. Haymet, Annu. Rev.Phys. Chem. 38, 89 (1987); M. Baus, J. Stat. Phys. 48, 1129(1987); J. Phys. Condens. Matter (to be published).
2T. V. Ramakrishnan and M. Yussouff, Phys. Rev. B 19,2775 (1979); see also A. D. J. Haymet and D. W. Oxtoby, J. Chem. Phys. 74, 2559 (1981).
3M. Baus and J. L. Colot, Mol. Phys. 55, 653 (1985).
4W. A. Curtin, J. Chem. Phys. 88, 7050 (1988).
5W. A. Curtin and N. W. Ashcroft, Phys. Rev. A 32, 2909(1985); see also P. Tarazona, Phys. Rev. A 31, 2672 (1985).
6A. R. Denton and N. W. Ashcroft, Phys. Rev. A 39, 4701(1989).
7M. Baus, J. Phys. Condens. Matter 1, 3131 (1989).
8See, e.g., R. Evans, Adv. Phys. 28, 143 (1979).
9The contribution to the free energy of the symmetry- breaking external field which is necessary in order to properly take the thermodynamic limit will not be considered explicitly here.
 $^{10}$ Notice that the double $\lambda$ integral can always be simplified by using the identity
$$\int_{0}^{1} d \lambda \int_{0}^{\lambda} d \lambda^{\prime} h\left(\lambda^{\prime}\right)=\int_{0}^{1} d \lambda(1-\lambda) h(\lambda),$$
 valid for any $h(\lambda)$ .
"This property follows immediately by observing that Eqs.(3) and (4) imply that in the uniform limit, $\rho(r) \to \rho_{L}$ , we have $\hat{\rho}[\rho] \to \rho_{L}$ .
12See, e.g., J. P. Hansen and I. R. Mc Donald, Theory of Simple Liquids (Academic, London, 1976).
13J. L. Colot and M. Baus, Mol. Phys. 56, 807 (1985).
14B. J. Alder, W. B. Hoover, and D. A. Young, J. Chem. Phys. 49, 3688 (1968); W. J. Hoover and F. M. Ree, J. Chem.Phys. 49, 3609 (1968); K. R. Hall, J. Chem. Phys. 49, 3609(1986).
15J. F. Lutsko and M. Baus (to be published).
16See also W. A. Curtin and K. Runge, Phys. Rev. A 35,4755 (1987).