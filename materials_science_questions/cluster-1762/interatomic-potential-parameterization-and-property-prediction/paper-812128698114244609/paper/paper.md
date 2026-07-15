# Electronic structure and total energy of Si, Ge and α-Sn by the self-consistent local pseudopotential method

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1982 J. Phys. C: Solid State Phys. 15 707

(http://iopscience.iop.org/0022-3719/15/4/017)

View the table of contents for this issue, or go to the journal homepage for more

---

Download details:

IP Address: 219.92.68.119
This content was downloaded on 17/08/2015 at 06:21

Please note that terms and conditions apply.

# Electronic structure and total energy of Si, Ge and $\alpha$-Sn by the self-consistent local pseudopotential method

G P Srivastava

Physics Department, New University of Ulster, Coleraine, Northern Ireland BT52 1SA, UK

Received 10 August 1981

Abstract. We have applied the self-consistent local pseudopotential method to study the electronic structure of Si, Ge and $\alpha$-Sn. The calculated band structures and valence charge densities agree well with experiment. The momentum-space formalism of Ihm, Zunger and Cohen, based on the self-consistent local pseudopotential method, is used to calculate the total energy of these crystals. The results are in good agreement with experiment.

## 1. Introduction

The empirical local pseudopotential method (ELPM) (Cohen and Bergstresser 1966) and the empirical non-local pseudopotential method (ENLPM) (Chelikowsky and Cohen 1976) have been very successful in obtaining good band structures and interpreting optical and photoemission data on diamond and zincblende semiconductors. These methods make use of a soft-core potential, which in reciprocal space is replaced by, typically, three or four form factors $v(G)$, where $G$ is the magnitude of a reciprocal lattice vector $\boldsymbol{G}$ (see, e.g. Cohen 1979, 1980). These form factors are regarded as purely adjustable parameters. As it is the screened pseudopotential (or form factors) rather than the bare (ionic) pseudopotential that is empirically parametrised, these approaches cannot permit, without additional information on ionic pseudopotential, self-consist- ency in a band structure calculation (Zunger 1979, Zunger and Cohen 1979). The use of self-consistent pseudopotentials becomes important when dealing with defects, surfaces, interfaces and structural studies of crystals.

Although self-consistent pseudopotential calculations (in the local approximation) for solid surfaces have been available for a few years (see, e.g. Schlüter 1978), no explicit results were available for solid bulks until recently (Ihm and Cohen 1979). Since then many other self-consistent pseudopotential calculations (including non-local effects) have appeared (Zunger and Cohen 1979). The self-consistent pseudopotential method can be used at two levels. On the one hand, one can start with the empirical pseudopo- tential method (EPM) and carry out self-consistency with the aid of a model (Animalu and Heine 1965) or parametrised (Schlüter et al 1975) ionic pseudopotential. On the other hand, a first-principles pseudopotential approach, including non-local effects, can be used (Zunger and Cohen 1979).

Labour can be reduced in the development of the self-consistent local pseudopoten- tial method (SCLPM) by adopting an approach described in this paper. Rather than

considering parametrised forms for both screened and ionic pseudopotentials, one only considers a parametrised form for a local ionic pseudopotential. Within the linear screening concept, the parametrised local ionic pseudopotential leads to an analytical expression for the starting screened pseudopotential. We thus do not have the further need of parametrising the screened pseudopotential. We report our calculations of the band structure and valence charge density for Si, Ge and α-Sn and compare the results with experiment and other theoretical calculations.

The first self-consistent attempt to calculate the total energy of silicon is due to Ihm and Cohen (1979, 1980). Their work uses a momentum-space formalism, with a local pseudopotential Hamiltonian, as first presented by Ihm et al (1979). We have used their formalism, within our version of the sCLPM, to calculate the total energy of Si, Ge and α-Sn. The results are in good agreement with experiment.

## 2. Method of calculation

### 2.1. Starting Hamiltonian

The starting point of all electronic structure calculations is the construction of the one-electron Hamiltonian. In the local pseudopotential method the pseudo-Hamiltonian takes the form

$$
H=p^{2} / 2 m^{*}+V_{\mathrm{ps}}, \tag{1}
$$

where

$$
V_{\mathrm{ps}}(\boldsymbol{r})=\sum_{j} v\left(\boldsymbol{r}-\boldsymbol{R}_{j}\right) \tag{2}
$$

is a superposition of screened pseudopotentials. The pseudo-eigenfunctions are expressed in terms of plane waves

$$
\psi_{\boldsymbol{k}, n}(\boldsymbol{r})=\sum_{\boldsymbol{G}} b_{\boldsymbol{k}, n}(\boldsymbol{G}) \exp [\mathrm{i}(\boldsymbol{k}+\boldsymbol{G}) \cdot \boldsymbol{r}] \tag{3}
$$

with $n$ as a band index and $\boldsymbol{k}$ as the electron wavevector in the first Brillouin zone. The electronic band structure is obtained by solving the following eigenvalue equation:

$$
\sum_{\boldsymbol{G}}\left(H_{\boldsymbol{G}, \boldsymbol{G}^{\prime}}(\boldsymbol{k})-E_{n}(\boldsymbol{k}) \delta_{\boldsymbol{G}, \boldsymbol{G}^{\prime}}\right) b_{\boldsymbol{k}, n}\left(\boldsymbol{G}^{\prime}\right)=0. \tag{4}
$$

Standard methods of solving this equation are described in Cohen and Heine (1970).

The matrix elements in equation (4) are

$$
H_{\boldsymbol{G}, \boldsymbol{G}^{\prime}}(\boldsymbol{k})=\frac{\hbar^{2}}{2 m^{*}}|\boldsymbol{k}+\boldsymbol{G}|^{2} \delta_{\boldsymbol{G}, \boldsymbol{G}^{\prime}}+V_{\mathrm{ps}}\left(\boldsymbol{G}-\boldsymbol{G}^{\prime}\right), \tag{5}
$$

where, in the local approximation, we can write for elemental semiconductors

$$
V_{\mathrm{ps}}\left(\boldsymbol{G}-\boldsymbol{G}^{\prime}\right) \equiv V(\boldsymbol{q})=S(\boldsymbol{q}) v(\boldsymbol{q}) \tag{6}
$$

with $S(\boldsymbol{q})$ and $v(\boldsymbol{q})$ as the structure factor and the local atomic pseudopotential form factor respectively. For the origin halfway between the two atoms in the unit cell for the diamond structure, the structure factor takes the simple form $S(\boldsymbol{q})=\cos (\boldsymbol{q} \cdot \boldsymbol{\tau})$, where $\boldsymbol{\tau}=\frac{1}{8} a(1,1,1)$, $a$ being the cubic lattice constant.

In our approach we construct the starting screened atomic pseudopotential $v(q)$ in the linear screening concept

$$
v^{\mathrm{start}}(q)=v^{\mathrm{ion}}(q) / \varepsilon(q), \tag{7}
$$

where we use the Heine-Abarenkov (1964) form for the dielectric function

$$
\varepsilon(q)=1+(1-f(q)) \frac{4 \pi Z e^{2}\left(1+\alpha_{\mathrm{eff}}\right)}{\Omega_{\mathrm{at}} q^{2}} \chi\left(\frac{q}{2 k_{\mathrm{F}}}\right)
$$

with

$$
\chi(y)=\left(\frac{2}{3} E_{\mathrm{F}}\right)^{-1}\left\{\frac{1}{2}+\frac{1}{4}\left[\left(1-y^{2}\right) / y\right] \ln |(1+y) /(1-y)|\right\},
$$

$$
E_{\mathrm{F}}=\frac{\hbar^{2} k_{\mathrm{F}}^{2}}{2 m^{*}} \quad f(q)=\frac{q^{2}}{2\left(q^{2}+k_{\mathrm{F}}^{2}+k_{\mathrm{s}}^{2}\right)} \quad k_{\mathrm{s}}^{2}=2 k_{\mathrm{F}} / \pi. \tag{8}
$$

Here $Z$ is the valency, $\Omega_{\mathrm{at}}$ is the atomic volume and $\alpha_{\mathrm{eff}}$ is the orthogonality constant. The ionic pseudopotential is considered as

$$
v^{\mathrm{ion}}(q)=\left(b_{1} / q^{2}\right)\left(\cos \left(b_{2} q\right)+b_{3}\right) \exp \left(-b_{4} q^{4}\right). \tag{9}
$$

We regard $b_{i}$ as adjustable parameters such that the use of equation (4) gives a good band structure to start with. The fitted values of $b_{i}$ depend on the number of discrete $v(q)$ that one wants to include in the calculation. In the EPM one typically fits $v(q)$ for $q^{2}=3,8$, and 11 (in units of $(2 \pi / a)^{2}$ ): $v(q)$ for higher allowed $q$ are set to zero. This is done merely for the convenience of calculation. In this work we fitted $b_{i}$ for $q^{2}=3,8$, and 11 in the case of $\mathrm{Si}$ and $\mathrm{Ge}$. In fact for these elements our fitted $b_{i}$ are such that equation (7), with the help of equation (8), reproduces Cohen and Bergstresser's (1966) empirical local pseudopotential form factors for $q^{2}=3,8$, and 11. For $\alpha$-Sn, however, we have included $v(q)$ for five reciprocal-lattice vectors: those with $q^{2}=3,8,11,16$, and 19. There was no particular reason for this choice though. There is a restriction on the choice of $b_{i}$ : for large $r, v^{\text {ion }}$ should represent the potential due to $Z$ valence ions (Animalu and Heine 1965). This means that $b_{1}\left(1+b_{3}\right)=-4 \pi Z e^{2} / \Omega_{\text {at }}$. We have somewhat relaxed this constraint in our fitting procedure. Also, the use of the exponential factor in equation (9) helps to make the large- $q$ part of $v(q)$ small, which is the criterion for a soft-core pseudopotential. The fitted values of $b_{i}$ are given in table 1. Our starting Hamiltonian is semiempirical in nature, as we only parametrise $v^{\text {ion }}(q)$ and then obtain, through the use of the dielectric function, an analytical form for the screened pseudopotential. The

Table 1. Parameters used in the construction of the starting semiempirical Hamiltonian. The potential is normalised to an atomic volume.

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Si</th>
<th>Ge</th>
<th>$\alpha$-Sn</th>
</tr>
</thead>
<tbody>
<tr>
<td>$b_{1}$ (Ryd)</td>
<td>$-1.34$</td>
<td>$-1.2$</td>
<td>$-0.565$</td>
</tr>
<tr>
<td>$b_{2}$</td>
<td>$0.791$</td>
<td>$0.751$</td>
<td>$1.087$</td>
</tr>
<tr>
<td>$b_{3}$</td>
<td>$-0.352$</td>
<td>$-0.348$</td>
<td>$0.022$</td>
</tr>
<tr>
<td>$b_{4}$</td>
<td>$0.018$</td>
<td>$0.018$</td>
<td>$0.018$</td>
</tr>
<tr>
<td>$\alpha_{\mathrm{eff}}$</td>
<td>$0.006$</td>
<td>$0.008$</td>
<td>$0.032$</td>
</tr>
<tr>
<td>$k_{\mathrm{F}}$ (au)</td>
<td>$0.957$</td>
<td>$0.921$</td>
<td>$0.867$</td>
</tr>
<tr>
<td>$m^{*}/m$</td>
<td>$1.0$</td>
<td>$1.0$</td>
<td>$1.0$</td>
</tr>
<tr>
<td>$a$ ($\mathring{\mathrm{A}}$)</td>
<td>$5.43$</td>
<td>$5.65$</td>
<td>$6.49$</td>
</tr>
<tr>
<td>$\Omega_{\mathrm{at}}$ (au)</td>
<td>$135.19$</td>
<td>$152.30$</td>
<td>$230.82$</td>
</tr>
</tbody>
</table>

pseudopotential thus generated has the flexibility to be used directly (subject to volume renormalisation) in the calculation of the electronic structure of surfaces (Srivastava 1980).

### 2.2. Self-consistency procedure
Our semiempirical starting pseudopotential has a basic advantage over the EPM approach. While there is an inherent lack of a self-consistency mechanism in the EPM approach (Zunger 1979), our approach can straightforwardly be extended to achieve self-consistency in bulk and surface calculations. With the starting semiempirical pseudo- potential, equation (4) is solved for electronic eigenvalues $E_{n}$ and eigenvectors (in reciprocal space) $b_{k, n}$. Then the starting pseudo-Hamiltonian is replaced by an effective Hamiltonian

$$H_{\text {eff }}=p^{2} / 2 m^{*}+V_{\text {eff }}$$

with
$$V_{\mathrm{eff}}(\boldsymbol{q})=v^{\mathrm{ion}}(\boldsymbol{q}) S(\boldsymbol{q})+V_{\mathrm{scr}}(\boldsymbol{q}).\tag{10}$$

The screening part of the effective Hamiltonian is considered as made up of an electro- static Hartree-type potential $V_{H}$ and a local exchange-correlation potential $V_{xc}$ of Hartree-Fock-Slater type
$$V_{\mathrm{scr}}(\boldsymbol{q})=V_{\mathrm{H}}(\boldsymbol{q})+V_{\mathrm{xc}}(\boldsymbol{q}),$$
where
$$V_{\mathrm{H}}(\boldsymbol{q})=4 \pi e^{2} \rho(\boldsymbol{q}) /|\boldsymbol{q}|^{2}$$
and
$$V_{\mathrm{xc}}(\boldsymbol{q})=-\alpha(3 / 2 \pi) e^{2}\left(3 \pi^{2}\right)^{1 / 3} \rho^{1 / 3}(\boldsymbol{q}).\tag{11}$$

In the $X_{\alpha}$ approximation for the exchange-correlation potential $\alpha$ is taken as a constant (Slater 1974). We use a value of $\alpha=0.79$ in accordance with Schlüter et al (1975). This value of $\alpha$, which is larger than $\frac{2}{3}$, accounts for some correlation contributions in an approximate way. Also, this value of $\alpha$ brings the $V_{xc}$ into agreement with Wigner's interpolation formula for the average charge density of silicon (Wigner 1934).

In solving the eigenvalue equation (4) we considered about 65 plane waves in the basis set and included another about 25 plane waves through Löwdin's second-order perturbation scheme (see Cohen and Heine 1970). The Fourier coefficients $\rho(G)$ of the valence charge density were calculated using Baldereschi's (1973) special $k$-point: $k_{0}=$ $(2 \pi / a)(0.6223,0.2953,0.0)$. Then the screening potentials $V_{H}$ and $V_{xc}$ were calculated from equation (11). For the calculation of $V_{xc}$ we evaluated $\rho(\boldsymbol{r})$ on a grid of $7^{3} \boldsymbol{r}$ points in the unit cell. The cube root of $\rho(\boldsymbol{r})$ was computed at each grid point, and the result transformed back into a Fourier series $\rho^{1 / 3}(G)$, from which then $V_{\mathrm{xc}}(G)$ was calculated using equation (11).

Denoting the starting potential by $V_{\text {in }}^{(1)}$ and the resulting effective output potential by $V_{\text {out }}^{(1)}$, we form a new input potential $V_{\text {in }}^{(2)}=\beta V_{\text {in }}^{(1)}+(1-\beta) V_{\text {out }}^{(1)}$, with $\beta$ chosen in accord ance with the degree of agreement between $V_{\text {in }}^{(1)}$ and $V_{\text {out }}^{(1)}$. This feedback technique is similar to the one discussed and used by many workers (Schlüter et al 1975, Alldredge and Kleinman 1974). Four iterations were found to bring in stability of eigenvalues to within $0.01 \mathrm{eV}$ and the screening potential to within $10^{-3}$ Ryd.

### 2.3. Total energy

Ihm et al (1979) have derived a momentum-space formalism for calculating the total energy of solids. Their formalism is designed particularly for application with the self-consistent pseudopotential method. In this formalism the total energy per atom is given by

$$
\begin{aligned}
E_{\mathrm{tot}}=\Omega_{\mathrm{at}} & \left(\sum_{\boldsymbol{k}, n_{\mathrm{v}}, \boldsymbol{G}}\left|b_{n_{\mathrm{v}}}(\boldsymbol{k}+\boldsymbol{G})\right|^{2}|(\boldsymbol{k}+\boldsymbol{G})|^{2}+\frac{1}{2} \sum_{\boldsymbol{G} \neq \mathbf{0}} V_{\mathrm{H}}(\boldsymbol{G}) \rho(\boldsymbol{G})\right. \\
& \left.+\frac{3}{4} \sum_{\boldsymbol{G}} V_{\mathrm{xc}}(\boldsymbol{G}) \rho(\boldsymbol{G})+\sum_{\boldsymbol{G} \neq \mathbf{0}} S(\boldsymbol{G}) v^{\mathrm{ion}}(\boldsymbol{G}) \rho(\boldsymbol{G})\right)+\alpha_{1} Z+\gamma_{\mathrm{Ewald}},
\end{aligned}
$$

where $n_{\mathrm{v}}$ denotes the valence band index. $\alpha_{1}$ measures the degree of repulsiveness of the ionic pseudopotential and is given by

$$
\begin{aligned}
\alpha_{1} & =\lim _{\boldsymbol{G} \rightarrow \mathbf{0}}\left[v^{\mathrm{ion}}(\boldsymbol{G})+4 \pi Z e^{2} / \Omega_{\mathrm{at}} G^{2}\right] \\
& =\frac{1}{\Omega_{\mathrm{at}}} \int\left(v^{\mathrm{ion}}(r)+\frac{Z e^{2}}{r}\right) \mathrm{d}^{3} r .
\end{aligned}
$$

$\gamma_{\text {Ewald }}$ is the ion-ion Coulomb energy:

$$
\begin{aligned}
\gamma_{\text {Ewald }} & =\frac{1}{2} \sum_{j}^{\prime} \frac{Z^{2} e^{2}}{\left|\boldsymbol{R}_{j}\right|}-\frac{1}{2} \lim _{\boldsymbol{G} \rightarrow 0} \frac{4 \pi Z^{2} e^{2}}{\Omega_{\mathrm{at}} G^{2}} \\
& =\frac{1}{2}\left(\sum_{j}^{\prime} \frac{Z^{2} e^{2}}{\left|\boldsymbol{R}_{j}\right|}-\frac{1}{\Omega_{\mathrm{at}}} \int \frac{Z^{2} e^{2}}{r} \mathrm{~d}^{3} r\right),
\end{aligned}
$$

where the $\boldsymbol{R}_{j}$ are lattice vectors to ionic sites. In equation (14) the prime means that $\boldsymbol{R}_{j}=\mathbf{0}$ is excluded in the summation. An alternative form for the total energy per atom is as follows:

$$
\begin{aligned}
E_{\mathrm{tot}}=\sum_{\boldsymbol{k}, n_{\mathrm{v}}} & E_{n_{\mathrm{v}}}(\boldsymbol{k})-\Omega_{\mathrm{at}}\left(\frac{1}{2} \sum_{\boldsymbol{G} \neq \mathbf{0}} V_{\mathrm{H}}(\boldsymbol{G}) \rho(\boldsymbol{G})\right. \\
& \left.+\frac{1}{4} \sum_{\boldsymbol{G}} V_{\mathrm{xc}}(\boldsymbol{G}) \rho(\boldsymbol{G})\right)+\alpha_{1} Z+\gamma_{\mathrm{Ewald}} .
\end{aligned}
$$

The first term on the right-hand side is the sum of the electron eigenvalues of the occupied states, and the second and third terms correspond to the correction for overcounting of the electron-electron interaction. The ion-ion Coulomb energy (per atom) for the diamond structure is given by (Harrison 1966)

$$
\gamma_{\text {Ewald }}=-2.6936 Z^{2} e^{2} / a .
$$

We have used equation (15) to calculate the total energy.

## 3. Results and discussion

### 3.1. Silicon

The band structure of silicon has been calculated several times, using various approaches. However, recent self-consistent calculations (Hamann 1979, Zunger and Cohen 1979, Glötzel et al 1980, Szmulowicz 1981) are at variance with available experimental data.

![](./images/812128698114244609_1.jpg)

Figure 1. Band structure of Si using the SCLPM.

Because of this we discuss our results for silicon in some detail. Our calculated band structure of Si is shown in figure 1. The energy eigenvalues at $\Gamma$, X, and L for the valence bands and first few conduction bands are given in table 2. Also given in table 2 are results of other recent self-consistent calculations (such as a linear augmented-plane-wave method (Hamann 1979), a first-principles non-local pseudopotential approach in the density-functional formalism (Zunger and Cohen 1979), a LMTO-ASA method (Glötzel et al 1980), and a non-muffin-tin augmented-plane-wave calculation (Szmulowicz 1981)).
Let us first discuss these calculations. While all these self-consistent band-structure results agree quite well for the valence band with available experimental data, it is clear that there is in general discrepancy between the calculated conduction band and the data. The largest discrepancy exists for the conduction band states $\Gamma_{15^{\prime}}, \Gamma_{2^{\prime}}$, and $X_{1}$. In

<table>
<caption>Table 2. Comparison of the present SCLPM results for the electronic eigenvalues in Si with experiment and other self-consistent calculations. Values in eV are referred to $\Gamma_{25'}$.</caption>
<thead>
<tr>
<th></th>
<th>Present<br>calculation</th>
<th>Hamann</th>
<th>Zunger and<br>Cohen</th>
<th>Glötzel<br>et al</th>
<th>Szmulowicz</th>
<th>Experiment†</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Gamma_{1}$</td>
<td>$-12.54$</td>
<td>$-12.02$</td>
<td>$-12.20$</td>
<td>$-11.87$</td>
<td>$-11.44$</td>
<td>$-12.4\pm0.6$</td>
</tr>
<tr>
<td>$\Gamma_{15}$</td>
<td>$3.48$</td>
<td>$2.49$</td>
<td>$2.48$</td>
<td>$2.59$</td>
<td>$3.30$</td>
<td>$3.45$</td>
</tr>
<tr>
<td>$\Gamma_{2'}$</td>
<td>$4.74$</td>
<td>$3.18$</td>
<td>$2.50$</td>
<td>$3.88$</td>
<td>$2.38$</td>
<td>$4.21\pm0.02$</td>
</tr>
<tr>
<td>$\Gamma_{12'}$</td>
<td>$7.89$</td>
<td>$7.86$</td>
<td>$7.25$</td>
<td></td>
<td>$9.09$</td>
<td>$7.6$</td>
</tr>
<tr>
<td>$X_{1}$</td>
<td>$-8.20$</td>
<td>$-7.84$</td>
<td>$-8.02$</td>
<td>$-7.75$</td>
<td>$-7.66$</td>
<td></td>
</tr>
<tr>
<td>$X_{4}$</td>
<td>$-2.96$</td>
<td>$-2.82$</td>
<td>$-2.93$</td>
<td>$-2.72$</td>
<td>$-2.34$</td>
<td>$-2.9$</td>
</tr>
<tr>
<td>$X_{1}$</td>
<td>$1.23$</td>
<td>$0.55$</td>
<td>$0.52$</td>
<td>$0.62$</td>
<td>$2.28$</td>
<td>$1.13$</td>
</tr>
<tr>
<td>$X_{4}$</td>
<td>$12.21$</td>
<td>$10.32$</td>
<td>$9.97$</td>
<td>$10.10$</td>
<td>$9.73$</td>
<td></td>
</tr>
<tr>
<td>$L_{2'}$</td>
<td>$-10.12$</td>
<td>$-9.64$</td>
<td>$-9.92$</td>
<td>$-9.53$</td>
<td>$-9.42$</td>
<td>$-9.3\pm0.4$</td>
</tr>
<tr>
<td>$L_{1}$</td>
<td>$-7.22$</td>
<td>$-7.06$</td>
<td>$-7.21$</td>
<td>$-6.93$</td>
<td>$-6.33$</td>
<td>$-6.8\pm0.2$</td>
</tr>
<tr>
<td>$L_{3'}$</td>
<td>$-1.24$</td>
<td>$-1.16$</td>
<td>$-1.28$</td>
<td>$-1.05$</td>
<td>$-1.03$</td>
<td>$-1.2\pm0.2$</td>
</tr>
<tr>
<td>$L_{1}$</td>
<td>$2.36$</td>
<td>$1.40$</td>
<td>$1.13$</td>
<td>$1.15$</td>
<td>$1.95$</td>
<td>$2.04\pm0.06$</td>
</tr>
<tr>
<td>$L_{3}$</td>
<td>$4.07$</td>
<td>$3.37$</td>
<td>$3.36$</td>
<td>$3.51$</td>
<td>$4.47$</td>
<td>$3.9\pm0.1$</td>
</tr>
<tr>
<td>Band gap</td>
<td>$1.08$</td>
<td>—</td>
<td>$0.5$</td>
<td>—</td>
<td>$2.06$</td>
<td>$1.12$</td>
</tr>
</tbody>
</table>

† As compiled in Szmulowicz (1981) and Chelikowsky and Cohen (1976).

![](./images/812128698114244609_2.jpg)
![](./images/812128698114244609_3.jpg)

Figure 2. (a) The total valence charge density of Si in the (110) plane using the SCLPM. Normalisation corresponds to eight electrons per unit cell.
(b The self-consistent pseudopotential of Si in the (110) plane. Values are in Ryd normalised to zero for $r \to \infty$. Full circles represent atomic sites, and full lines connect nearest neighbours.

particular, the thermal band gap is either reduced (to 0.55 eV in Hamann and 0.52 eV in Zunger and Cohen) or opened up (to 2.28 eV in Szmulowicz). It has been suggested by Stukel and Euwema (1970) that the agreement between the calculated gap and experiment can be improved by treating the exchange-correlation coefficient $\alpha$ as an adjustable parameter. Our calculation, on the other hand, shows a very good agreement for both the valence band and the conduction band with the experiment. We have been able to achieve this possibly due to the attenuated feedback scheme in our self-consist- ency procedure.

The total valence pseudocharge density of Si in the (110) plane is shown in figure 2(a). We make a few observations here. The present calculation of $\rho(\boldsymbol{r})$ was done using the single special $\boldsymbol{k}$-point of Baldereschi (1973). We get values of 22.1, 5.6, and 11.4 electrons per unit-cell volume for the bonding, atomic, and antibonding sites respec- tively. These values are somewhat different from those obtained by Chelikowsky and Cohen (1976) and Zunger and Cohen (1979), both of whose calculations use non-local pseudopotentials and sample the charge density at two and six special $\boldsymbol{k}$-points, respec- tively. It is obvious that the use of a non-local pseudopotential piles more pseudocharge at the bonding site and leaves less charge at the atomic site. Zunger and Cohen (1979) have defined an anisotropy factor $L_{1} / L_{2}$ in the covalent bond charge density (where $L_{1}$ is the length of the bond charge parallel to the bond axis and $L_{2}$ is the length perpendicular to this axis). The present calculation yields $L_{1} / L_{2}=0.7$, which is in agreement with the value 0.8 obtained by Zunger and Cohen using a semi-empirical self-consistent local pseudopotential. The self-consistent non-local pseudopotential method of Zunger and Cohen yields $L_{1} / L_{2} \sim 1.3$, which is in good agreement with the experimental value 1.4 (Yang and Coppens 1974). It should be noted, however, that the experimentally syn- thesised valence charge density is not strictly comparable with pseudopotential calcu- lations (Zunger and Cohen 1979).

<table>
<caption>Table 3. Calculated Fourier coefficients of the self-consistent valence charge density and screening field.</caption>
<thead>
<tr>
<th></th>
<th rowspan="2">$G(a/2\pi)$</th>
<th>$\rho(G)$</th>
<th rowspan="2">$V_{\text{H}}(G)$</th>
<th rowspan="2">$V_{\text{xc}}(G)$</th>
</tr>
<tr>
<th></th>
<th>(per unit-cell volume)</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th colspan="2">(Ryd per unit-cell volume)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si</td>
<td>$(0, 0, 0)$</td>
<td>$8.0$</td>
<td>—</td>
<td>$-0.68239$</td>
</tr>
<tr>
<td></td>
<td>$(1, 1, 1)$</td>
<td>$-1.620$</td>
<td>$-0.1340$</td>
<td>$0.05362$</td>
</tr>
<tr>
<td></td>
<td>$(2, 2, 0)$</td>
<td>$0.092$</td>
<td>$0.00285$</td>
<td>$-0.00837$</td>
</tr>
<tr>
<td></td>
<td>$(3, 1, 1)$</td>
<td>$0.300$</td>
<td>$0.00677$</td>
<td>$-0.00678$</td>
</tr>
<tr>
<td></td>
<td>$(2, 2, 2)$</td>
<td>$0.400$</td>
<td>$0.00827$</td>
<td>$-0.00433$</td>
</tr>
<tr>
<td></td>
<td>$(4, 0, 0)$</td>
<td>$0.216$</td>
<td>$0.00335$</td>
<td>$-0.00144$</td>
</tr>
<tr>
<td>Ge</td>
<td>$(0, 0, 0)$</td>
<td>$8.0$</td>
<td>—</td>
<td>$-0.64888$</td>
</tr>
<tr>
<td></td>
<td>$(1, 1, 1)$</td>
<td>$-1.871$</td>
<td>$-0.14870$</td>
<td>$0.05878$</td>
</tr>
<tr>
<td></td>
<td>$(2, 2, 0)$</td>
<td>$-0.1585$</td>
<td>$-0.00472$</td>
<td>$-0.00210$</td>
</tr>
<tr>
<td></td>
<td>$(3, 1, 1)$</td>
<td>$0.1784$</td>
<td>$0.00387$</td>
<td>$-0.00422$</td>
</tr>
<tr>
<td></td>
<td>$(2, 2, 2)$</td>
<td>$0.3814$</td>
<td>$0.00758$</td>
<td>$-0.00397$</td>
</tr>
<tr>
<td></td>
<td>$(4, 0, 0)$</td>
<td>$0.1845$</td>
<td>$0.00275$</td>
<td>$-0.00153$</td>
</tr>
<tr>
<td>α-Sn</td>
<td>$(0, 0, 0)$</td>
<td>$8.0$</td>
<td>—</td>
<td>$-0.54680$</td>
</tr>
<tr>
<td></td>
<td>$(1, 1, 1)$</td>
<td>$-2.172$</td>
<td>$-0.15028$</td>
<td>$0.06265$</td>
</tr>
<tr>
<td></td>
<td>$(2, 2, 0)$</td>
<td>$-0.2906$</td>
<td>$-0.00754$</td>
<td>$-0.00116$</td>
</tr>
<tr>
<td></td>
<td>$(3, 1, 1)$</td>
<td>$0.1695$</td>
<td>$0.00320$</td>
<td>$-0.00352$</td>
</tr>
<tr>
<td></td>
<td>$(2, 2, 2)$</td>
<td>$0.4018$</td>
<td>$0.00695$</td>
<td>$-0.00128$</td>
</tr>
<tr>
<td></td>
<td>$(4, 0, 0)$</td>
<td>$0.3142$</td>
<td>$0.00408$</td>
<td>$-0.00556$</td>
</tr>
</tbody>
</table>

Figure 2(b) shows the self-consistent pseudopotential of Si in the (110) plane. Normalising to $V(\boldsymbol{q} \rightarrow \mathbf{0})=0$, the potential values (in Ryd) of $-1.33$, $+0.78$, and $-0.46$ are obtained at the bonding, atomic, and antibonding sites respectively. These values are in agreement with those of Schlüter *et al* (1975), obtained in the bulk region of a repeated slab geometry for Si (111). If one is to define the polarisation of the pseudopotential

<table>
<caption>Table 4. Calculated total (crystal) energy per atom (in Ryd) compared with experiment and the calculation of Ihm and Cohen.</caption>
<thead>
<tr>
<th></th>
<th colspan="2">Si</th>
<th rowspan="2">Ge</th>
<th rowspan="2">α-Sn</th>
</tr>
<tr>
<th></th>
<th>Present<br>calculation<br>$\alpha=0.79$</th>
<th>Ihm and<br>Cohen<br>$\alpha=0.794$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Kinetic</td>
<td>$1.7877$</td>
<td>$2.8115$</td>
<td>$1.9898$</td>
<td>$2.1643$</td>
</tr>
<tr>
<td>$\Omega_{\text{at}} \sum_{G \neq 0} S(\boldsymbol{G}) v^{\text{ion}}(\boldsymbol{G}) \rho(\boldsymbol{G})$</td>
<td>$-1.0553$</td>
<td>$-1.9156$</td>
<td>$-1.5204$</td>
<td>$-1.8370$</td>
</tr>
<tr>
<td>$\alpha_{1} Z$</td>
<td>$1.6768$</td>
<td>$1.4332$</td>
<td>$1.3536$</td>
<td>$1.3352$</td>
</tr>
<tr>
<td>$\frac{1}{2} \Omega_{\text{at}} \sum_{G \neq 0} V_{\text{H}}(\boldsymbol{G}) \rho(\boldsymbol{G})$</td>
<td>$0.4686$</td>
<td>$0.4935$</td>
<td>$0.5690$</td>
<td>$0.6878$</td>
</tr>
<tr>
<td>$\gamma^{\text{Ewald}}$</td>
<td>$-8.3974$</td>
<td>$-8.3995$</td>
<td>$-8.0705$</td>
<td>$-7.0259$</td>
</tr>
<tr>
<td>$\frac{3}{4} \Omega_{\text{at}} \sum_{G} V_{\text{xc}}(\boldsymbol{G}) \rho(\boldsymbol{G})$</td>
<td>$-2.3758$</td>
<td>$-2.3936$</td>
<td>$-2.3108$</td>
<td>$-2.0940$</td>
</tr>
<tr>
<td>Total</td>
<td>$-7.8954$</td>
<td>$-7.9705$</td>
<td>$-7.9893$</td>
<td>$-6.7696$</td>
</tr>
<tr>
<td>Experiment†</td>
<td>$-7.919$</td>
<td></td>
<td>$-7.91$</td>
<td>$-7.08$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">† Moore (1949), Kittel (1976).</td>
</tr>
</tfoot>
</table>

along the bond direction in the same way as for the bond charge, the present calculation yields an anisotropy factor 0.53, which is comparable with the calculated anisotropy factor 0.7 in the bond charge.

Zunger and Cohen (1979) have suggested that it is not the potential non-locality that is responsible for the formation of a bond-polarised charge $(L_{1}/L_{2}>1)$. The polarisation of the bond charge density along the bond direction is possibly a consequence of the more localised nature of the first-principles potential. It would seem, following Zunger and Cohen, that only the higher-momentum components $(q\gg 2k_{\mathrm{F}})$ of the first-principles pseudopotential determine the details of the anisotropy of the charge density. These components do not manifest themselves significantly in the valence band structure but might be important in determining the phonon spectra.

Table 3 presents the Fourier coefficients of the self-consistent valence charge density and the self-consistent screening field. It is interesting to note the variation of $V_{\mathrm{H}}(G)$ and $V_{\mathrm{xc}}(G)$ with $G$. For all $G$, $V_{\mathrm{xc}}(G)$ is opposite in sign to $V_{\mathrm{H}}(G)$, implying that the exchange-correlation field acts to screen the electron-electron Coulomb interactions. Also, except for the $\langle 220\rangle$ and $\langle 311\rangle$ sets $|V_{\mathrm{H}}(G)/V_{\mathrm{xc}}(G)|$ is larger than unity, implying that the major part of the screening field is Coulombic in nature.

For the total energy calculation the convergence of summation over $k$ was tested by considering evenly spaced points in the irreducible part of the Brillouin zone (1/48 of the zone). 41 points were finally considered. The convergence was found to be a little better over the use of ten special points of Chandi and Cohen (1973). In table 4 we have presented the various terms contributing to the total energy. Our calculated crystal energy per atom $-7.895$ Ryd is in excellent agreement with the experimental result $-7.919$ Ryd (Kittel 1976).

It is interesting to note that our calculated crystal energy is also in very good agreement with Ihm and Cohen's (1980) recently calculated crystal energy per atom $-7.970$ Ryd using $\alpha=0.794$ in their self-consistent pseudopotential method. Assuming that results using $\alpha=0.79$ and $\alpha=0.794$ (present calculation and Ihm and Cohen, respectively) do not appreciably differ from each other, we can compare our results term-by-term with those of Ihm and Cohen. From table 4 we see that although appreciable differences exist between our and Ihm and Cohen's results for the kinetic energy of pseudovalence electrons, the ion-valence-electron interaction energy $\Omega_{\mathrm{at}} \Sigma_{G} S(G) v^{\mathrm{ion}}(G) \rho(G)$, and the term measuring the degree of cancellation of kinetic energy in the core region $\alpha_{1} Z$, the sum of these three terms agree well in the two calculations. The difference between these individual terms reflects the use of different ionic pseudopotentials in the two calculations.

### 3.2. Germanium and grey tin
Having discussed the results for silicon in some detail, we now present only a brief discussion of an analogous study of the band structure, charge density, and total energy on germanium and grey tin. In figures 3 and 4 are shown the calculated band structures of $\mathrm{Ge}$ and $\alpha$-Sn, respectively. In table 5 are presented the energy eigenvalues at $\Gamma, \mathrm{X}$ and $\mathrm{L}$ for the valence bands and the first few conduction bands of Ge. It is clear that our band structure of Ge is in good agreement with experiment and the self-consistent calculations of Glötzel *et al* (1980) and Zunger and Cohen (1979). There are no self-consistent band structure calculations of $\alpha$-Sn available in the literature but our results in table 6 are seen to agree well with experiment, the EPM calculation of Cohen and Bergstresser (1966) and the recent model pseudopotential calculation of Mašović and

![](./images/812128698114244609_4.jpg)

Figure 3. Band structure of Ge using the SCLPM.

![](./images/812128698114244609_5.jpg)

Figure 4. Band structure of $\alpha$-Sn using the SCLPM.

Table 5. Calculated electronic eigenvalues in Ge compared with experiment and other calculations. Energies in eV are referred to $\Gamma_{25'}$.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Present calculation</th>
      <th>Glötzel et al</th>
      <th>Zunger and Cohen</th>
      <th>Mašović and Zeković</th>
      <th>Experiment†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\Gamma_1$</td>
      <td>$-12.12$</td>
      <td>$-12.50$</td>
      <td>$-12.36$</td>
      <td>—</td>
      <td>$-12.6 \pm 0.3$</td>
    </tr>
    <tr>
      <td>$\Gamma_{2'}$</td>
      <td>$0.88$</td>
      <td>$1.15$</td>
      <td>$0.77$</td>
      <td>$0.97$</td>
      <td>$0.99$</td>
    </tr>
    <tr>
      <td>$\Gamma_{15}$</td>
      <td>$3.49$</td>
      <td>$2.59$</td>
      <td>$2.59$</td>
      <td>$3.18$</td>
      <td>$3.23$</td>
    </tr>
    <tr>
      <td>$X_1$</td>
      <td>$-8.4$</td>
      <td>$-8.57$</td>
      <td>$-8.4$</td>
      <td>—</td>
      <td></td>
    </tr>
    <tr>
      <td>$X_4$</td>
      <td>$-2.56$</td>
      <td>$-3.01$</td>
      <td>$-2.85$</td>
      <td>—</td>
      <td></td>
    </tr>
    <tr>
      <td>$X_1$</td>
      <td>$1.29$</td>
      <td>$0.64$</td>
      <td>$0.95$</td>
      <td>$1.49$</td>
      <td>$1.26$</td>
    </tr>
    <tr>
      <td>$X_3$</td>
      <td>$11.77$</td>
      <td>$9.70$</td>
      <td>$8.92$</td>
      <td>—</td>
      <td></td>
    </tr>
    <tr>
      <td>$L_{2'}$</td>
      <td>$-10.13$</td>
      <td>$-10.33$</td>
      <td>$-10.09$</td>
      <td>—</td>
      <td>$-10.5 \pm 0.4$</td>
    </tr>
    <tr>
      <td>$L_1$</td>
      <td>$-7.02$</td>
      <td>$-7.46$</td>
      <td>$-7.24$</td>
      <td>—</td>
      <td>$-7.4 \pm 0.2$</td>
    </tr>
    <tr>
      <td>$L_{3'}$</td>
      <td>$-1.1$</td>
      <td>$-1.37$</td>
      <td>$-1.28$</td>
      <td>—</td>
      <td>$-1.4 \pm 0.2$</td>
    </tr>
    <tr>
      <td>$L_1$</td>
      <td>$0.73$</td>
      <td>$0.59$</td>
      <td>$0.65$</td>
      <td>$1.0$</td>
      <td>$0.84$</td>
    </tr>
    <tr>
      <td>$L_3$</td>
      <td>$4.28$</td>
      <td>$3.81$</td>
      <td>$3.95$</td>
      <td>—</td>
      <td></td>
    </tr>
    <tr>
      <td>$L_{2'}$</td>
      <td>$8.26$</td>
      <td>—</td>
      <td>$7.6$</td>
      <td>—</td>
      <td></td>
    </tr>
  </tbody>
</table>

† As presented in Chelikowsky and Cohen (1976) and Mašović and Zeković (1979).

# Electronic structure of Si, Ge and $\alpha$-Sn

Table 6. Calculated electronic eigenvalues in $\alpha$-Sn compared with experiment and the results of Mašović and Zeković and Cohen and Bergstresser. Energies in eV are referred to $\Gamma_{25'}$.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Present<br>calculation</th>
      <th>Mašović and<br>Zeković</th>
      <th>Cohen and<br>Bergstresser</th>
      <th>Experiment†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\Gamma_1$</td>
      <td>$-9.11$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\Gamma_{2'}$</td>
      <td>$0.0$</td>
      <td>$-0.2$</td>
      <td></td>
      <td>$-0.16$</td>
    </tr>
    <tr>
      <td>$\Gamma_{15}$</td>
      <td>$2.83$</td>
      <td>$2.6$</td>
      <td>$3.0$</td>
      <td>$2.9$</td>
    </tr>
    <tr>
      <td>$X_1$</td>
      <td>$-6.5$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$X_4$</td>
      <td>$-1.70$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$X_1$</td>
      <td>$1.79$</td>
      <td>$1.6$</td>
      <td>$1.1$</td>
      <td></td>
    </tr>
    <tr>
      <td>$X_3$</td>
      <td>$8.15$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$L_1$</td>
      <td>$-7.78$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$L_{2'}$</td>
      <td>$-5.25$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$L_{3'}$</td>
      <td>$-0.74$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$L_1$</td>
      <td>$0.83$</td>
      <td>$0.68$</td>
      <td>$0.6$</td>
      <td>$0.32$</td>
    </tr>
    <tr>
      <td>$L_3$</td>
      <td>$3.70$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$L_{2'}$</td>
      <td>$7.40$</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$L_3-L_1$</td>
      <td>$1.57$</td>
      <td></td>
      <td>$1.4$</td>
      <td>$1.4$</td>
    </tr>
    <tr>
      <td>$L_3-L_3$</td>
      <td>$4.44$</td>
      <td></td>
      <td>$4.4$</td>
      <td>$4.2$</td>
    </tr>
    <tr>
      <td>$X_4-X_1$</td>
      <td>$3.49$</td>
      <td></td>
      <td>$3.1$</td>
      <td>$3.5$</td>
    </tr>
  </tbody>
</table>

† As presented in Cohen and Bergstresser (1966), and Mašović and Zeković (1979).

Zeković (1979). We have ignored spin-orbit interactions in our band structure calculations for both Ge and $\alpha$-Sn.

The self-consistent pseudopotential and the total valence pseudocharge density of Ge and $\alpha$-Sn in the (110) plane are shown in figures 5 and 6. For Ge we get values of 21.6, 12.0, and 13.7 electrons per unit-cell volume for the bonding, atomic, and antibonding sites, respectively. For $\alpha$-Sn these values are 24.6, 14.4, and 15.4. The bond

![](./images/812128698114244609_6.jpg)

Figure 5. (a) The total valence charge density of Ge in the (110) plane using the SCLPM. Normalisation corresponds to eight electrons per unit cell.
(b) The self-consistent pseudopotential of Ge in the (110) plane. Values are in Ryd normalised to zero for $r \to \infty$. Full circles represent atomic sites, and full lines connect nearest neighbours.

![](./images/812128698114244609_7.jpg)
![](./images/812128698114244609_8.jpg)

Figure 6. (a) The total valence charge density of $\alpha$-Sn in the (110) plane using the SCLPM. Normalisation corresponds to eight electrons per unit cell.
(b) The self-consistent pseudopotential of $\alpha$-Sn in the (110) plane. Values are in Ryd normalised to zero for $r \rightarrow \infty$. Full circles represent atomic sites, and full lines connect nearest neighbours.

charge anisotropy factor $L_{1}/L_{2}$ is 1.06 for Ge and 1.28 for $\alpha$-Sn. Potential values (in Ryd) of $-1.15$, $-0.18$, and $-0.5$ for Ge and $-1.32$, $-0.2$, and $-0.18$ for $\alpha$-Sn are obtained at the bonding, atomic, and anti-bonding sites, respectively. The bond pseudopotential anisotropy factor is 0.88 for Ge and 1.11 for $\alpha$-Sn.

In table 3 are presented the Fourier coefficients $\rho(\boldsymbol{G})$, $V_{\mathrm{H}}(\boldsymbol{G})$ and $V_{\mathrm{xc}}(\boldsymbol{G})$. Although the observation is qualitatively similar to that in Si, we note some minute differences. In Ge, for half of the members of the $\langle 220\rangle$ set we find that $V_{\mathrm{xc}}(\boldsymbol{G})$ has the same sign as $V_{\mathrm{H}}(\boldsymbol{G})$. Also, for the $\langle 311\rangle$ set $|V_{\mathrm{xc}}(\boldsymbol{G})/V_{\mathrm{H}}(\boldsymbol{G})|$ is nearly unity. In $\alpha$-Sn, for four out of twelve members (not all shown) of the $\langle 220\rangle$ set $V_{\mathrm{xc}}(\boldsymbol{G})$ has the same sign as $V_{\mathrm{H}}(\boldsymbol{G})$. Also, $|V_{\mathrm{xc}}(\boldsymbol{G})/V_{\mathrm{H}}(\boldsymbol{G})|$ is larger than unity for the $\langle 311\rangle$ and $\langle 400\rangle$ sets.

In table 4 we have presented the various terms contributing to the total energy. The calculated crystal energy per atom of Ge $-7.99$ Ryd is in good agreement with the experimental result $-7.91$ Ryd (Moore 1949). For $\alpha$-Sn, our calculated result $-6.77$ Ryd is only in reasonable agreement with the experimental result $-7.08$ Ryd (Moore 1949). It should be noted that our calculation ignores spin-orbit interactions and non-local contributions. Such contributions are significantly larger in $\alpha$-Sn than in Si or Ge. Inclusion of these would increase the magnitude of the sum of the occupied electron eigenvalues $\Sigma_{k,n_{\mathrm{v}}} E_{n_{\mathrm{v}}}(\boldsymbol{k})$ in $\alpha$-Sn, thus bringing the calculated $E_{\mathrm{tot}}$ into closer agreement with experiment.

### 4. Conclusions

We have developed a self-consistent local pseudopotential method to calculate the electronic structure of diamond structure semiconductors Si, Ge and $\alpha$-Sn. The method can easily be extended to zincblende structure semiconductors. In this method we start with a semiempirical local pseudo-Hamiltonian and make the calculation self-consistent

within the Hartree-Fock-Slater $X_\alpha$ approximation. The advantage of this approach over other calculations (Schlüter *et al* 1975, Ihm and Cohen 1980) lies in the fact that we only need to parametrise the ionic pseudopotential (thus avoiding the additional need of parametrising the screened pseudopotential). Our calculated results for the band struc- ture and the valence charge density of Si, Ge and $\alpha$-Sn are in good agreement with experiment and recent theoretical calculations.

We have applied the momentum-space formalism of Ihm *et al*, based on our self- consistent local pseudopotential method, to calculate the total energy of Si, Ge, and $\alpha$-Sn. The result for Si is in excellent agreement with experiment and the calculation of Ihm and Cohen (1980). The results for Ge and $\alpha$-Sn are in good agreement with experiment.

## References

Alldredge G P and Kleinman L 1974 *Phys. Rev.* B **10** 559
Animalu A O E and Heine V 1965 *Phil. Mag.* **12** 1249
Baldereschi A 1973 *Phys. Rev.* B **7** 5212
Chadi D J and Cohen M L 1973 *Phys. Rev.* B **8** 5747
Chelikowsky J R and Cohen M L 1976 *Phys. Rev.* B **14** 556
Cohen M L 1979 *Phys. Today* **32** 40
--- 1980 *J. Phys. Soc. Japan Suppl.* A **49** 13
Cohen M L and Bergstresser T K 1966 *Phys. Rev.* **141** 789
Cohen M L and Heine V 1970 *Solid State Phys.* **24** 37 (New York: Academic Press)
Glötzel D, Segall B and Anderson O K 1980 *Solid State Commun.* **36** 403
Hamann D R 1979 *Phys. Rev. Lett.* **42** 662
Harrison W A 1966 *Pseudopotentials in the Theory of Metals* (New York: Benjamin)
Heine V and Abarenkov I V 1964 *Phil. Mag.* **9** 451
Ihm J and Cohen M L 1979 *Solid State Commun.* **29** 711
--- 1980 *Phys. Rev.* B **21** 1527
Ihm J, Zunger A and Cohen M L 1979 *J. Phys. C: Solid State Phys.* **12** 4409
Kittel C 1976 *Introduction to Solid State Physics* 5th edn (New York: Wiley)
Mašović D R and Zeković S 1979 *Phys. Status Solidi* (b) **96** 469
Moore C E 1949 *Atomic Energy Levels* (NBS Circular) vol 1 p 467
Schlüter M 1978 *Festkörperprobleme XVIII* (*Adv. Solid State Phys.*) p 155
Schlüter M, Chelikowsky J R, Louie S G and Cohen M L 1975 *Phys. Rev.* B **12** 4200
Slater J C 1974 *Self-consistent Field for Molecules and Solids* (New York: McGraw-Hill)
Srivastava G P 1980 *Solid State Commun.* **33** 1209
Stukel D J and Euwema R N 1970 *Phys. Rev.* B **1** 1635
Szmulowicz F 1981 *Phys. Rev.* B **23** 1652
Wigner E 1934 *Phys. Rev.* **46** 1002
Yang Y W and Coppens P 1974 *Solid State Commun.* **15** 1555
Zunger A 1979 *J. Vac. Sci. Technol.* **16** 1337
Zunger A and Cohen M L 1979 *Phys. Rev.* B **20** 4082