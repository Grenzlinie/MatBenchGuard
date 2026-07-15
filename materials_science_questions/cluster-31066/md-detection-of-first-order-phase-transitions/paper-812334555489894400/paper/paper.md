# The Equation of State of Parallel Hard Squares*

W. G. RUDD* AND H. L. FRISCH

Department of Chemistry, State University of New York at Albany,
Albany, New York 12203

Received November 12, 1970

The results of the cell cluster calculation of the additive free energy constant $C$ in the asymptotic high density form of the free energy

$$F_{N \tau \to 1} \sim 2 \ln (\sqrt{\tau}-1)+C+2 \ln (\lambda / \sigma),$$

where $\tau$ is the ratio of the system area to its close-packed area, permit the prediction of a phase transition for hard squares between the free-volume solid state and the state determined by the Pade' approximant to the virial series. Molecular dynamics calculations show the free volume pressure to be correct over a considerable range of solid-state densities. The computer experiments also yield qualitative indications that there are two distinct phases in hard square systems.

## I. INTRODUCTION

Hard core systems continue to be of interest in statistical mechanics not only because they may be considered to be a rough approximation to physically more realistic systems, but also because their simplicity makes possible a direct inter-comparison of the predictions and validity of various approaches to the calculation of thermodynamic properties of such systems from fundamental principles. In this paper we report a continuation of the study initiated earlier [1] concerning systems of parallel hard squares.

First-order approximations to the properties of hard core systems at densities near the close-packed limit $\tau=V/V_0 \to 1$, where $V$ is the volume of the system whose close-packed volume is $V_0$, are readily obtainable from the free-volume theory. For example, Salsburg and Wood [2] showed that the equation of state of $N$ $\nu$-dimensional rigid spheres at absolute temperature $T$ has the asymptotic form

$$\frac{PV}{Nk_B T} \underset{\tau \to 1}{\sim} \left( \frac{PV}{NkT} \right)_{FV} \left[ 1 - \frac{1}{N} \right] + O(1), \tag{1}$$

* Research supported by the National Science Foundation through Grant GP-19881.

where the free volume result is

$$
\left(\frac{P V}{N k T}\right)_{F V}=\frac{\tau^{1 / \nu}}{\tau^{1 / \nu}-1} \tag{2}
$$

and $k_{\text{B}}$ is Boltzmann's constant.

On the other hand, the virial expansion

$$
\frac{P V}{N k T}=1+\frac{B}{\tau}+\frac{C}{\tau^{2}}+\cdots \tag{3}
$$

reformulated as a Pade' approximant of the form

$$
\frac{P V}{N k T}=\left(\frac{1+a_{1} / \tau+a_{2} / \tau^{2}+\cdots}{1+b_{1} / \tau+b_{2} / \tau^{2}+\cdots}\right) \tag{4}
$$

is known [3] to adequately predict the equation of state of hard disks and spheres throughout the fluid-phase region.

Hoover [4] showed that the free volume form is exact for finite hard square systems with rigid walls over a density range of non-zero width near close-packing, and later [5] that, as $\tau \rightarrow 1$, the Helmholtz free energy $F_{N}$ approaches the free volume limit in the thermodynamic limit:

$$
\frac{F_{N}}{N k T} \underset{\substack{\tau \rightarrow 1 \\ N, V \infty \rightarrow \\ N / V \text { const }}}{\longrightarrow}-\nu \ln \left(\tau^{1 / \nu}-1\right)+C+\nu \ln (\lambda / \sigma), \tag{5}
$$

where $C$ is a constant. In Section II we present a heuristic derivation of (5) and calculate the (3,3) Pade approximant for the hard square virial series using the seven coefficients calculated by Hoover and de Rocco [6].

The cell-cluster technique [7] has been applied [1] to the calculation of the additive free energy constant $C$ in Eq. (5). Knowledge of this constant permits the prediction of a possible solid-fluid phase transition as described in Section III. The results of molecular dynamics calculations are presented in Section IV.

## II. GENERAL THEORY

### A. High Density Equation of State

We consider a system of $N$ $\nu$-dimensional hard squares of side length $\sigma$ contained in a reduced volume $\tau=V / V_{0}$, where $V$ is the volume of the system whose close-packed volume is $V_{0}=N \sigma^{\nu}$. Rotation of the squares is prohibited and their sides are understood to be either mutually parallel or perpendicular.

In the petit canonical ensemble, the Helmoltz free energy $F_N$ is given by
$$
F_N = -k_{\mathrm{B}} T \ln Q_N(V, T)
$$
where $Q_N$ is the partition function
$$
Q_N=\lambda^{-\nu N} N!^{-1} \int_{V} \cdots \int_{V} \prod_{i<j} \varphi_{i j} d \mathbf{r}^{N}. \tag{6}
$$
$\varphi_{i j}$ is the Boltzmann factor which describes the interaction between squares $i$ and $j$ and $\lambda=(h^{2} / 2 \pi m k T)^{1 / 2}$ is the mean thermal de Broglie wavelength.

Near the close packed limit $\tau \to 1$ the squares will become localized near the sites of a regular lattice, with nearest neighbor distance $a$, so that each square may be associated with a particular site. Neglecting vacancies and other lattice imperfections, the $\nu N$-dimensional region of integration in (6) may be divided into $N!$ equivalent nonoverlapping regions $R_i$, which differ only in the choice of the question which squares are to be associated with which nominal lattice sites. Hence (6) becomes
$$
Q_{N}=\lambda^{-\nu N} \int_{R} \cdots \int \prod \varphi_{i j} d \mathbf{r}^{N}, \tag{7}
$$
where $R$ stands for any one of the $N!$ regions described above.

It is known [1] that the Boltzmann factors $\varphi_{i j}$ for squares have the form
$$
\varphi_{i j}=H\left(\xi_{i j}-\sigma\right), \tag{8}
$$
where $\xi_{i j}$ is a linear function of the components of the position vectors $\mathbf{r}_{i}$ and $\mathbf{r}_{j}$ and $H$ is either 0 or 1 depending on the sign of the argument. For example, the requirement that $i$ and $j$ do not overlap along the $x$-axis yields
$$
\varphi_{i j}=\eta\left(\left|x_{i}-x_{j}\right|-\sigma\right), \tag{9}
$$
where $\eta$ is the unit Heaviside function. It is then convenient to measure the coordinates $\mathbf{r}_{i}$ of each particle relative to those of its nominal lattice site $\mathbf{R}_{i}^{0}$:
$$
\mathbf{r}_{i}=\mathbf{R}_{i}^{0}+\boldsymbol{\rho}_{i}. \tag{10}
$$

In the high density limit under consideration, those Boltzmann factors that do not vanish then have the form
$$
\varphi_{i j}=H\left(\mu_{i j}+a-\sigma\right), \tag{11}
$$
where the $u_{i j}$ are now formed from components of $\rho_{i}$ and $\rho_{j}$. Our previous example then becomes
$$
\varphi_{i j}=\eta\left(X_{i}-X_{j}+a-\sigma\right) \eta\left(X_{j}-X_{i}+a-\sigma\right), \tag{12}
$$

where again $X_i$ and $X_j$ are measured relative to sites $i$ and $j$, respectively. The natural substitution
$$
\rho_{i}=(a-\sigma) u_{i}
\tag{13}
$$
then yields
$$
Q_{N}=\left(\frac{\sigma}{\lambda}\right)^{\nu N}\left(\tau^{1 / \nu}-1\right)^{\nu N} Z_{N},
\tag{14}
$$
where $Z_N$ is the configuration integral
$$
Z_{N}=\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \prod \varphi_{i j} d \mathbf{u}^{N}.
\tag{15}
$$

We then have the result
$$
\frac{F_{N}}{N k_{B} T}=\nu \ln \left(\frac{\lambda}{\sigma}\right)-\nu \ln \left(\tau^{1 / \nu}-1\right)-\frac{1}{N} \ln Z_{N}
\tag{16}
$$
and note that $C=-(1 / N) \ln Z_{N}$.

Use of the thermodynamic relation $P=-(\partial F / \partial V)_{T}$ then gives the high density equation of state
$$
\frac{P V}{N k T}=\frac{\tau^{1 / \nu}}{\tau^{1 / \nu}-1}
\tag{17}
$$
which is just the free volume expression.

In rigid disk and sphere systems, it has been shown [8] that in the corresponding expression
$$
\frac{P V}{N k T}=\frac{\tau^{1 / \nu}}{\tau^{1 / \nu}-1}+C_{0}+D_{0}(\tau-1)+E_{0}(\tau-1)^{2}+\cdots,
\tag{18}
$$
the coefficients $C_{0}, D_{0},...$ depend on nonvanishing density derivatives of the configuration integral. For squares, however, the $p V$ relation (17) is independent of $Z_{N}$, and indeed there are no high order corrections to the free energy. This result is in agreement with Hoover's [5] proof that the free volume form is correct for squares and cubes in the thermodynamic limit as $\tau \to 1$.

### B. Low Density Equation of State

Hoover and de Rocco [6] have calculated the first seven hard square virial coefficients. A Pade analysis using these coefficients yields
$$
\frac{P V}{N k T}=\frac{1-.98164 / \tau+.32755 / \tau^{2}-.0276113 / \tau^{3}}{1-2.98164 / \tau+3.2908 / \tau^{2}-1.3310 / \tau^{3}}.
\tag{19}
$$

Figure I shows the equations of state obtained from Eqs. (17) and (19).

![](./images/812334555489894400_1.jpg)

FIG. 1. The equations of state predicted by the various theories discussed in Sec II. —— free volume theory; —— —— (3, 3) Padé approximant; —— . —— seven-term virial series, no Padé approximant; × molecular dynamics results.

### III. POSSIBLE PHASE TRANSITION

In an earlier publication [1] the modified cell-cluster technique [7] was used to calculate the additive free energy constant $C$ in Eq. (5). Knowledge of this constant permits the prediction of a phase transition by equating the excess chemical potentials obtained by integrating under the $pV$ curves for the high and low density equations of state. We assume

(a) the Pade approximant for the fluid to be valid throughout the fluid phase,

(b) the free-volume pressure to be exact throughout the entire solid region, and

(c) the cell-cluster value $C = -2 \ln 2 - .260422$ to be the correct value.

If we let $\tau_1$ be the reduced volume of the solid phase at the transition pressure $p$,

and $\tau_{2}$ be the coexisting fluid phase volume, we then have the following condition for equilibrium between the two phases:

$$
N k T \Delta G=F_{s}\left(\tau_{1}\right)-F_{\text {virial }}\left(\tau_{2}\right)+P V_{0}\left(\tau_{1}-\tau_{2}\right)+N k T=0. \tag{20}
$$

Here

$$
\frac{F_{s}(\tau)}{N k T}=-2 \ln (\sqrt{\tau}-1)+C \tag{21}
$$

and $F_{\text {virial }}$ is obtained from

$$
\frac{F_{\text {virial }}(\tau)}{N k T}=-\int_{e_{2}}^{\infty}\left(\frac{P V_{0}}{N k T}\right)_{\text {virial }}-\frac{1}{\tau}\right) d \tau, \tag{22}
$$

where the pressure in (22) is to be obtained from the virial expansion.

Now if one integrates the virial expression for the $p$ term by a term to find $F_{\text {virial }}$ and then computes the two possible Pade approximants ((2, 3) and (3, 2)) to the resulting series, one finds that the results disagree by as much as $25 \%$ for $\tau \sim 1.5$. Hence, for the purposes of the calculations reported below, the integral in (22) was performed numerically, using Simpson's rule with a step width of .0001. The

![](./images/812334555489894400_2.jpg)

FIG. 2. The excess chemical potential difference $\Delta G$ as a function of the solid-state density $\tau_{1}$.

starting value used was $\tau = 3.1$., the last point at which the two above-mentioned Pade approximants agreed to five places.

Figure 2 shows $\Delta G$ as a function of $\tau_1$ in the neighborhood of the transition region. The transition is found to occur at a pressure $PV_0/NkT \sim 6.936$ and coexisting volumes $1.272 \leqslant \tau \leqslant 1.297$ or densities a bout $77\%$ of the close-packed density.

The intuitive feeling that there should be a definite difference in squares between a highly ordered solid state and a random fluid state for squares is supported by the above result. However, the following objections might be raised regarding the transition:

(1) The high density and virial $pV$ curves are very close together in the transition region. It is not impossible that the two curves join smoothly, with at best a second or higher order phase transition.

(2) The location of the transition region is extremely sensitive to the value of $C$ and to the exact value of $F_{\text{virial}}$. Hence, a difference of 005 in either value, which for both is probably an underestimate of the error, can change the transition pressure by as much as $5\%$, with a similar effect on the transition densities. Hence, the phase transition cannot as yet be regarded as being definitely established. Preliminary molecular dynamics calculations do furnish some qualitative evidence for the existence of the transition, as we shall see in the next section.

## IV. MOLECULAR DYNAMICS RESULTS

Table I shows the results of the molecular dynamics calculations. All calculations were carried out using periodic boundary conditions. Limitations on available computer time restricted the number of collisions to between 50 and 100 000 colli- sions for the 400 squares used throughout. A square lattice was used for the starting configuration in most instances, although in some cases the final configuration from a run was used as a starting configuration for a run at a lower density.

The high density results ($\tau \leqslant 1.4$) show excellent agreement with the free volume theory predictions. The indication is that the transition is at a lower density than that determinal in the preceding section. However, the absence of a significant increase in the standard deviations for $1.285 \leqslant \tau \leqslant 1.5$ suggests that the data in this density range represent an unequilibrated system. Considerably longer runs are required in order to preclude the possibility that the system was "locked" into a solid-like metastable state.

Hoover [4] showed that the free volume theory was exact near the close-packed limit for finite systems of squares enclosed in rigid boundaries. The present results indicate that the free volume theory is valid also for systems with periodic boundary

<table>
<caption>TABLE I<br>$PV/NlT$</caption>
<thead>
<tr>
<th>$\tau$</th>
<th>Molecular dynamics</th>
<th>Free volume</th>
<th>Virial</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.05</td>
<td>41.56 $\pm$ .05</td>
<td>41.49</td>
<td></td>
</tr>
<tr>
<td>1.1</td>
<td>21.45 $\pm$ .08</td>
<td>21.488</td>
<td>39.35</td>
</tr>
<tr>
<td>1.115</td>
<td>18.81 $\pm$ .12</td>
<td>18.87</td>
<td>28.63</td>
</tr>
<tr>
<td>1.125</td>
<td>17.42 $\pm$ .05</td>
<td>17.48</td>
<td>22.42</td>
</tr>
<tr>
<td>1.15</td>
<td>14.76 $\pm$ .04</td>
<td>14.82</td>
<td>18.40</td>
</tr>
<tr>
<td>1.175</td>
<td>12.93 $\pm$ .07</td>
<td>12.91</td>
<td>15.09</td>
</tr>
<tr>
<td>1.2</td>
<td>11.45 $\pm$ .03</td>
<td>11.47</td>
<td>12.98</td>
</tr>
<tr>
<td>1.285</td>
<td>8.55 $\pm$ .09</td>
<td>8.48</td>
<td>9.30</td>
</tr>
<tr>
<td>1.3</td>
<td>8.18 $\pm$ .06</td>
<td>8.13</td>
<td>8.91</td>
</tr>
<tr>
<td>1.4</td>
<td>6.52 $\pm$ .1</td>
<td>6.46</td>
<td>7.10</td>
</tr>
<tr>
<td>1.5</td>
<td>5.61 $\pm$ .09</td>
<td>5.45</td>
<td>6.00</td>
</tr>
<tr>
<td>1.6</td>
<td>5.13 $\pm$ .09</td>
<td>4.78</td>
<td>5.23</td>
</tr>
<tr>
<td>1.7</td>
<td>4.57 $\pm$ .11</td>
<td>4.29</td>
<td>4.66</td>
</tr>
<tr>
<td>1.8</td>
<td>4.18 $\pm$ .11</td>
<td>3.93</td>
<td>4.20</td>
</tr>
<tr>
<td>1.9</td>
<td>3.83 $\pm$ .10</td>
<td>3.64</td>
<td>3.85</td>
</tr>
<tr>
<td>2.0</td>
<td>3.57 $\pm$ .05</td>
<td>3.41</td>
<td>3.55</td>
</tr>
</tbody>
</table>

conditions and over a considerable density range. Hoover's theory predicts that 400 squares enclosed in rigid walls will obey the free-volume law for $\tau < 1.1025$. Our results indicate the exchange of neighbor cells is a negligible effect over a considerably wider density range.

Figure 3 shows a "snapshot" of a system of 400 squares at $\tau = 1.2$ after 50,000 collisions. The system appears to have remained close to its original square lattice configuration, with the exception of a sliding motion in a few rows. Other high-density position plots show this to be the general case. The indication is that

![](./images/812334555489894400_3.jpg)

FIG. 3. A snapshot of a high density, $\tau = 1.2$, system of 400 squares after 50 000 collisions.

the square lattice configuration is $a$ stable configuration, as was postulated in the cell cluster calculations.

The lower density results are not as satisfactory. Most of the runs were started from a square lattice configuration and it appears that the short runs did not allow the system to reach equilibrium from its initial solid state form. A typical run starts with a very low pressure which lasts for a time corresponding to three or four collisions per particle, after which time the pressure suddenly jumps to that predicted by the free volume theory. The pressure then slowly increases toward values slightly above the virial pressure, but, with the exception of the run at $\tau = 2$, the pressure did not level off for times long enough to be considered statistically meaningful. The values quoted for $1.5 \leqslant \tau \leqslant 1.9$ are the means for the entire run, leaving out the initial low pressure region.

With the above mentioned exceptions, the $pV$ values quoted in Table I are obtained by discarding the first 10 000 collisions and then taking the means of the pressures obtained from each 10 000 collisions thereafter. The errors are the standard deviations from these means.

Partial "snapshots" of the low density configurations show little evidence of long-range order.

These results may be considered to be qualitative evidence for the existence of a phase transition. However, the results also suggest that the transition may be difficult to locate in finite systems because of the tendency of a finite number of squares to become "locked" into a solid-like configuration.

## ACKNOWLEDGMENTS

All calculations were carried out using the Univac 1108 at the Computing Center of the State University of New York at Albany, and we thank the staff thereof for their assistance. Helpful discussions with Dr. F. H. Stillinger, Jr. and Dr. W. G. Hoover are gratefully acknowledged.

## REFERENCES

1. A. L. BEYERLEIN, W. G. RUDD, Z. W. SALSBURG, AND M. BUYNOSKI, *J. Chem. Phys.* **53** (1970), 1532.
2. Z. W. SALSBURG AND W. W. WOOD, *J. Chem. Phys.* **37** (1962), 798.
3. See, for example, F. H. REE AND W. G. HOOVER, *J. Chem. Phys.* **40** (1964), 939.
4. W. G. HOOVER, *J. Chem. Phys.* **40** (1964), 937.
5. W. G. HOOVER, *J. Chem. Phys.* **43** (1965), 371.
6. W. G. HOOVER AND A. G. DE ROCCO, *J. Chem. Phys.* **36** (1961), 3149.
7. F. H. STILLINGER, JR., Z. W. SALSBURG, AND R. L. KORNEGAY, *J. Chem. Phys.* **40** (1964), 1564.
8. W. G. RUDD, Z. W. SALSBURG, A. P. YU AND F. H. STILLINGER, JR., *J. Chem. Phys.* **49** (1968), 4857.