# Analytic model of the Grüneisen parameter all densities

Leonid Burakovsky*, Dean L. Preston

Theoretical and Applied Physics, Los Alamos National Laboratory, Los Alamos, NM 87545, USA

Received 27 May 2003; revised 19 September 2003; accepted 3 October 2003

## Abstract
We model the density dependence of the Grüneisen parameter as $\gamma(\rho)=1 / 2+\gamma_{1} / \rho^{1 / 3}+\gamma_{2} / \rho^{q}$, where $\gamma_{1}, \gamma_{2}$, and $q>1$ are constants. This form is based on the assumption that $\gamma$ is an analytic function of $V^{1 / 3}$, and was designed to accurately represent the experimentally determined low-pressure behavior of $\gamma$. The numerical values of the constants are obtained for 20 elemental solids. Using the Lindemann criterion with our model for $\gamma$, we calculate melting curves for Al, Ar, Cu, Pd, and Pt and compare them to available experimental and theoretical melt data. We also determine the $Z$ (atomic number) dependence of $\gamma_{1}$.The high-compression limit of the model is shown to follow from a generalization of the Slater, Dugdale-MacDonald, and Vashchenko-Zubarevforms for the volume dependence of the Grüneisen parameter.
© 2004 Elsevier Ltd. All rights reserved.

PACS: 62.20. − x; 62.50. + p; 63.10. + a; 64.10. + h

---

## 1. Introduction
Lattice anharmonicity leads to a volume dependence of the phonon frequencies, $\omega_{i}$, that is described by the mode Grüneisen parameters [1]
$$\gamma_{i}=-\frac{\partial \ln \omega_{i}}{\partial \ln V},\tag{1}$$
and the mechanical Grüneisen parameter is defined as the average of the $\gamma_{i}$ over the first Brillouin zone, $\gamma_{m} \equiv\langle\gamma_{i}\rangle$. When the $\gamma_{i}$ are all equal it can be shown [2] that $\gamma_{m}=\gamma_{i}$ coincides with the thermodynamic Grüneisen parameter [3]
$$\gamma_{\mathrm{th}}=\frac{\alpha V B_{\mathrm{T}}}{C_{\mathrm{V}}},\tag{2}$$
where $\alpha$ is the thermal expansion coefficient, $B_{T}$ is the isothermal bulk modulus, and $C_{V}$ is the heat capacity at constant volume. If the $\gamma_{i}$ are not all equal, $\gamma_{m} \neq \gamma_{th}$ in general. As noted by Barron [3], Born has shown that, even if the $\gamma_{i}$ are not all equal, $\gamma_{m}=\gamma_{th}$ in the limit of low $(T \to 0)$ and high $(T \geq \Theta_{D})$ temperatures. The $T=0$ limiting value of $\gamma_{m}=\gamma_{th} \equiv \gamma$ is $\gamma=-d \ln \Theta_{D} / d \ln V$, where $\Theta_{D}$ is the Debye characteristic temperature, $\hbar\langle\omega_{i}^{-3}\rangle^{-1 / 3} / k_{B}$, in the limit $T \to 0$ [3]. Here both $\Theta_{D}$ and $\gamma$ are functions of volume, or density, alone. This formula is the Debye-Grüneisen definition of $\gamma$ [4], which can be rewritten in terms of density, $\rho \sim 1/V$, as
$$\gamma(\rho)=\frac{\mathrm{d} \ln \Theta_{\mathrm{D}}(\rho)}{\mathrm{d} \ln \rho}.\tag{3}$$

The Lindemann melting criterion, which asserts that the root-mean-square atomic displacement of atoms from their equilibrium positions in a solid is a fixed fraction of the interatomic distance at the melting point, can be rewritten in the form of the Gilvarry law, which relates the density derivative of the melting temperature, $T_{m}(\rho)$, to the Grüneisen parameter [5]:
$$\frac{\mathrm{d} \ln T_{\mathrm{m}}(\rho)}{\mathrm{d} \ln \rho}=2\left[\gamma(\rho)-\frac{1}{3}\right],\tag{4}$$
hence integration of $\gamma(\rho)$ yields the melt curve. Equations of state for solids can be constructed on the basis of $\gamma(\rho)$, though additional thermodynamic data are needed [6]. There is a long history of attempts to model $\gamma(\rho)$ [7]. Slater [8], Dugdale and MacDonald [9], and Vashchenko and Zubarev [10] proposed three expressions for $\gamma(\rho)$ that are summarized by the single formula [11]
$$\gamma=\frac{\frac{B^{\prime}}{2}-\frac{1}{6}-\frac{t}{3}\left(1-\frac{P}{3 B}\right)}{1-\frac{2 t}{3} \frac{P}{B}},\tag{5}$$

* Corresponding author.
E-mail address: dean@lanl.gov (L. Burakovsky).

0022-3697/$ - see front matter © 2004 Elsevier Ltd. All rights reserved.
doi:10.1016/j.jpcs.2003.10.076

where $P$ is pressure on the cold curve ( $T=0$ equation of state), and $B \equiv -V \mathrm{d}P/\mathrm{d}V$ and $B'=(\mathrm{d}B/\mathrm{d}V)/(\mathrm{d}P/\mathrm{d}V)$ are the bulk modulus and its pressure derivative at $T=0$. We will refer to Eq. (5) as the SDMVZ (Slater, Dugdale–MacDonald, Vashchenko–Zubarev) formula. Slater's derivation is based on the Debye–Grüneisen definition (3) and assumes no volume dependence of the Poisson ratio. Dugdale and MacDonald used a simplification of lattice dynamics in which the material is modeled as a lattice undergoing one-dimensional harmonic oscillations. Their derivation was improved by Vashchenko and Zubarev who considered three-dimensional oscillations of a lattice with interatomic interactions described by an anharmonic central potential. Eq. (5) reduces to the Slater, Dugdale–MacDonald, and Vaschenko–Zubarev formulas for $t=0$, 1, and 2, respectively. Eq. (5) has since been rederived by other researchers following different approaches [12–14].

## 2. An analytic model for $\boldsymbol{\gamma(\rho)}$

Melting curves and equations of state are usually based on simple functional forms for $\gamma(\rho)$. Dongquan and Wanxing [15], for example, proposed the form $\gamma(\rho)=\gamma_{0}\rho_{0}/\rho+2/3(1-\rho_{0}/\rho)^{\delta}$, which reduces to $\gamma\rho\approx$ constant at small compressions and approaches $2/3$ as very large compressions; $\gamma$ does not differ from that given by Eq. (5) by more than $10\%$ for $1\leq\delta\leq3$ [15]. For $\delta=2$ this form reduces to $\gamma(\rho)=2/3+\gamma_{1}/\rho+\gamma_{2}/\rho^{2}$, a model frequently used for the construction of equations of state and melting curves [6,16].

At very high compressions, of order 10, a solid becomes a crystallized one-component plasma, i.e. a lattice of ions in a uniform neutralizing background of electrons [17]. Several theoretical studies predict $\gamma=1/2$ for this limiting state of a solid. Kopyshev [18] calculated $\gamma(V)$ in the Thomas–Fermi approximation and found $\gamma\rightarrow1/2$ as $V\rightarrow0$. Simple dimensional arguments by Hubbard [19] also indicate that $\gamma\rightarrow1/2$ as $V\rightarrow0$. Additional theoretical studies that give $\gamma\rightarrow1/2$ include, but are not limited to, references [20–23]. Nevertheless, some researchers assume $\gamma\rightarrow2/3$ as $V\rightarrow0$ [24] because that is the limiting value of $\gamma$ as given by Eq. (5) with fixed $t$ (see below).

We now construct a simple, practical three-parameter model of $\gamma(\rho)$ that accurately fits low-compression data, is equivalent to the experimental result that $\gamma\rho^{q_{\text{eff}}}\approx$ constant, $q_{\text{eff}}\geq1$, for compressions up to 1.5, and limits to $1/2$ as $V\rightarrow0$. We assume that the Grüneisen parameter is an analytic function of $x\equiv V^{1/3}$, essentially the interatomic distance, and that the coefficient of $x$ in the Taylor–Maclaurin series expansion for $\gamma$ is non-zero. The simplest model that satisfies all of these requirements is
$$
\gamma(V)=\frac{1}{2}+c_{1}V^{1/3}+c_{2}V^{q},\ \ c_{1},c_{2},q=\text{const},\ q>1,\tag{6}
$$

Note that $\gamma(V)-1/2$ is asymptotic to $c_{1}V^{1/3}$; this is discussed in more detail in the next section. The term $c_{2}V^{q}$ represents the contribution of the quadratic and higher-order terms in $x$ which must sum to make $\gamma$ a concave-up function of $V$ at small compressions.

Eq. (6) can be rewritten in terms of density as
$$
\gamma(\rho)=\frac{1}{2}+\frac{\gamma_{1}}{\rho^{1/3}}+\frac{\gamma_{2}}{\rho^{q}},\ \ \gamma_{1},\gamma_{2},q=\text{const},\ \ q>1,\tag{7}
$$

Note that both $\gamma_{1}$ and $\gamma_{2}$ are dimensional parameters.

Eq. (7) incorporates the low-compression power-law behavior $\gamma\rho^{q_{\text{eff}}}\approx$ constant, $q_{\text{eff}}\geq1$, known from

<table>
<caption>Table 1 Numerical values of the parameters entering Eqs. (7) and (8) for 20 elemental solids. The crystal structure indicated for an element is that from which it melts at zero pressure. For Ne and Ar the entry under $\rho_{300}$ is the value of $\rho(T=0)$</caption>
<thead>
<tr>
<th>Element</th>
<th>$Z$</th>
<th>$\gamma_{1}$ (g/cc)$^{1/3}$</th>
<th>$\gamma_{2}$ (g/cc)$^{q}$</th>
<th>$\tilde{\gamma}_{1}$</th>
<th>$\tilde{\gamma}_{2}$</th>
<th>$q$</th>
<th>$\rho_{300}$ (g/cc)</th>
<th>$\rho_{\text{m}}$ (g/cc)</th>
<th>$T_{\text{m}}(\rho)_{\text{m}}$ (K)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ne (fcc)</td>
<td>10</td>
<td>1.04</td>
<td>5.17</td>
<td>0.91</td>
<td>2.10</td>
<td>2.2</td>
<td>1.507</td>
<td>1.435</td>
<td>24.6</td>
</tr>
<tr>
<td>Mg (hcp)</td>
<td>12</td>
<td>0.79</td>
<td>4.33</td>
<td>0.66</td>
<td>0.53</td>
<td>3.8</td>
<td>1.740</td>
<td>1.640</td>
<td>923</td>
</tr>
<tr>
<td>Al (fcc)</td>
<td>13</td>
<td>0.84</td>
<td>45.4</td>
<td>0.60</td>
<td>1.40</td>
<td>3.5</td>
<td>2.700</td>
<td>2.550</td>
<td>933.5</td>
</tr>
<tr>
<td>Ar (fcc)</td>
<td>18</td>
<td>1.19</td>
<td>16.3</td>
<td>0.90</td>
<td>1.86</td>
<td>3.8</td>
<td>1.771</td>
<td>1.622</td>
<td>83.8</td>
</tr>
<tr>
<td>Fe (bcc)</td>
<td>26</td>
<td>1.72</td>
<td>$2.66\times10^{3}$</td>
<td>0.86</td>
<td>0.25</td>
<td>4.5</td>
<td>7.870</td>
<td>7.270</td>
<td>1811</td>
</tr>
<tr>
<td>Co (fcc)</td>
<td>27</td>
<td>1.81</td>
<td>$6.28\times10^{4}$</td>
<td>0.88</td>
<td>0.39</td>
<td>5.5</td>
<td>8.830</td>
<td>8.180</td>
<td>1768</td>
</tr>
<tr>
<td>Ni (fcc)</td>
<td>28</td>
<td>1.85</td>
<td>$5.60\times10^{5}$</td>
<td>0.89</td>
<td>0.38</td>
<td>6.5</td>
<td>8.900</td>
<td>8.220</td>
<td>1728</td>
</tr>
<tr>
<td>Cu (fcc)</td>
<td>29</td>
<td>1.87</td>
<td>$2.31\times10^{4}$</td>
<td>0.90</td>
<td>0.78</td>
<td>4.7</td>
<td>8.930</td>
<td>8.370</td>
<td>1357.7</td>
</tr>
<tr>
<td>Zn (hcp)</td>
<td>30</td>
<td>1.91</td>
<td>$1.84\times10^{3}$</td>
<td>0.99</td>
<td>1.05</td>
<td>3.8</td>
<td>7.140</td>
<td>6.900</td>
<td>692.7</td>
</tr>
<tr>
<td>Mo (bcc)</td>
<td>42</td>
<td>2.06</td>
<td>$1.40\times10^{6}$</td>
<td>0.95</td>
<td>0.19</td>
<td>6.8</td>
<td>10.21</td>
<td>9.650</td>
<td>2896</td>
</tr>
<tr>
<td>Pd (fcc)</td>
<td>46</td>
<td>2.40</td>
<td>$3.34\times10^{6}$</td>
<td>1.05</td>
<td>0.25</td>
<td>6.6</td>
<td>12.02</td>
<td>11.29</td>
<td>1828</td>
</tr>
<tr>
<td>Ag (fcc)</td>
<td>47</td>
<td>2.23</td>
<td>$9.63\times10^{4}$</td>
<td>1.02</td>
<td>1.21</td>
<td>4.8</td>
<td>10.49</td>
<td>9.850</td>
<td>1235.1</td>
</tr>
<tr>
<td>Cd (hcp)</td>
<td>48</td>
<td>2.43</td>
<td>$2.47\times10^{4}$</td>
<td>1.18</td>
<td>0.97</td>
<td>4.7</td>
<td>8.650</td>
<td>8.420</td>
<td>594.2</td>
</tr>
<tr>
<td>In (bct)</td>
<td>49</td>
<td>2.43</td>
<td>$6.14\times10^{3}$</td>
<td>1.25</td>
<td>0.80</td>
<td>4.5</td>
<td>7.310</td>
<td>7.200</td>
<td>429.8</td>
</tr>
<tr>
<td>Sn (bct)</td>
<td>50</td>
<td>2.37</td>
<td>$2.37\times10^{3}$</td>
<td>1.22</td>
<td>0.83</td>
<td>4.0</td>
<td>7.300</td>
<td>7.200</td>
<td>505.1</td>
</tr>
<tr>
<td>Pt (fcc)</td>
<td>78</td>
<td>3.21</td>
<td>$1.13\times10^{11}$</td>
<td>1.16</td>
<td>1.01</td>
<td>8.3</td>
<td>21.45</td>
<td>20.19</td>
<td>2041</td>
</tr>
<tr>
<td>Au (fcc)</td>
<td>79</td>
<td>3.21</td>
<td>$1.97\times10^{12}$</td>
<td>1.20</td>
<td>1.62</td>
<td>9.4</td>
<td>19.30</td>
<td>18.29</td>
<td>1337.6</td>
</tr>
<tr>
<td>Tl (bcc)</td>
<td>81</td>
<td>3.17</td>
<td>$3.74\times10^{7}$</td>
<td>1.39</td>
<td>0.54</td>
<td>7.3</td>
<td>11.85</td>
<td>11.55</td>
<td>577</td>
</tr>
<tr>
<td>Pb (fcc)</td>
<td>82</td>
<td>3.09</td>
<td>$8.21\times10^{8}$</td>
<td>1.38</td>
<td>0.89</td>
<td>8.5</td>
<td>11.34</td>
<td>11.05</td>
<td>600.6</td>
</tr>
<tr>
<td>U (bcc)</td>
<td>92</td>
<td>3.39</td>
<td>$1.05\times10^{11}$</td>
<td>1.27</td>
<td>0.57</td>
<td>8.8</td>
<td>19.05</td>
<td>17.60</td>
<td>1405</td>
</tr>
</tbody>
</table>

experiment. Experimental values of $q_{\text{eff}}$ are typically in the range 1-2 [25], but may be as high as 3 [26]. The effective exponent can be defined by $q_{\text{eff}}=-\mathrm{d} \ln \gamma / \mathrm{d} \ln \rho$ since $\gamma \sim$ $\rho^{-q_{\text{eff}}}$; in our model we have $q_{\text{eff}}=\left[\gamma_{1} /\left(3 \rho^{1 / 3}\right)+\right.$ $q \gamma_{2} / \rho^{q} ] / \gamma(\rho)$. Averaging over compressions from 1 to 1.25 we find $\langle q_{\text{eff}} \rangle \leq 3$ in general. Consider, for example, gold: with the corresponding parameters from Table 1, $q_{\text{eff}}$ varies from 4.7 at $\rho=19.3$ g/cc to 1.3 at $\rho=24$ g/cc with an average value of 2.7.

With $\gamma(\rho)$ given by Eq. (7), the Lindemann Eq. (4) can be integrated to yield the melting curve

$$
\begin{aligned}
T_{\mathrm{m}}(\rho)= & T_{\mathrm{m}}\left(\rho_{\mathrm{r}}\right)\left(\frac{\rho}{\rho_{\mathrm{r}}}\right)^{1 / 3} \\
& \times \exp \left\{6 \gamma_{1}\left(\frac{1}{\left(\rho_{\mathrm{r}}\right)^{1 / 3}}-\frac{1}{\rho^{1 / 3}}\right)+\frac{2 \gamma_{2}}{q}\left(\frac{1}{\left(\rho_{\mathrm{r}}\right)^{q}}-\frac{1}{\rho^{q}}\right)\right\}, \\
& (8)
\end{aligned}
$$

where $\rho_{\mathrm{r}}$ and $T_{\mathrm{m}}(\rho_{\mathrm{r}})$ are a reference density and corresponding melting temperature.

We now demonstrate that the asymptotic form of our model for the Grüneisen parameter follows from a generalization of the SDMVZ formula.

### 3. Asymptotic $\gamma(\rho)$ from a generalization of the SDMVZ formula

Parshukov [27] studied the compression dependence of $\gamma$ for lead, indium, and tin in the pressure range 0.6-4.0 GPa and found that it is almost identical for all three metals but is not described by Eq. (5) over the entire range of pressures for $t$ a constant. He found that the Slater formula $(t=0)$ provided the most accurate fit at small compressions while the Dugdale-MacDonald one $(t=1)$ is optimal at higher compressions. He suggested that all three $(t=0,1,2)$ formulas be unified by making $t$ compression dependent. Romain et al. [28] noted that the melting curve of Al cannot be described in the Lindemann approach using the $t=0,1$, or 2 formulas for $\gamma(\rho)$. Nagayama and Mori [29] analyzed available experimental data on 16 metals and found that the data on $\gamma$ at $P=0$ are best described by the Slater formula, but at moderate compressions the data are best fit by the Dugdale-MacDonald formula which is approximately equivalent to $\gamma / V^{1.1}=$ constant, close to the relation $\gamma / V=$ constant that is routinely used in high-pressure studies. Nagayama and Mori noted that $\mathrm{d} \ln \gamma / \mathrm{d} \ln V$ decreases with increasing compression from the value given by the Slater formula $(t=0)$ through that given by the Dugdale- MacDonald formula $(t=1)$ toward the value predicted by the Vashchenko-Zubarev relation $(t=2)$. An analysis of Hugoniot data shows that $t$ follows a similar trend $(0 \rightarrow$ $1 \rightarrow 2)$ in $\mathrm{Al}, \mathrm{Cu}$, and $\mathrm{Ta}$ [30]. These analyses of experimental data indicate that the parameter $t$ is not a constant but a variable that increases with increasing compression.

Irvine and Stacey [12] generalized the Vashchenko-Zubarev formula by accounting for non-central interatomic forces. They added a term $f$ to the expression for the interatomic force constant and obtained the formula

$$
\gamma=\frac{\frac{B^{\prime}}{2}-\frac{5}{6}+\frac{2 P}{9 B}-\frac{f}{18 B}+\frac{1}{6} \frac{\mathrm{d} f}{\mathrm{~d} P}}{1-\frac{4 P}{3 B}+\frac{f}{3 B}},
$$

which reduces to the Vashchenko-Zubarev formula for $f=$ 0. By introducing the dimensionless parameter $t$ via

$$
f=2 P(2-t), \quad(10)
$$

Eq. (9) reduces to

$$
\gamma=\frac{\frac{B^{\prime}}{2}-\frac{1}{6}-\frac{t}{3}\left(1-\frac{P}{3 B}\right)+\frac{P}{3 B} V \frac{\mathrm{d} t}{\mathrm{~d} V}}{1-\frac{2 t}{3} \frac{P}{B}},
$$

which would coincide with Eq. (5) without the additional term $(P V / 3 B) \mathrm{d} t / \mathrm{d} V$ in the numerator. Hence Eq. (11) is an extension of the SDMVZ formula, Eq. (5) to the case of density-dependent $t$. We note that Eq. (11) can be cast in the form

$$
\begin{aligned}
\gamma & =\frac{1}{2} \frac{B}{B-\frac{2}{3} t P} \frac{\mathrm{d}\left(B-\frac{2}{3} t P\right)}{\mathrm{d} P}-\frac{1}{6} \\
& =-\frac{1}{2} \frac{\mathrm{d} \ln \left(B-\frac{2}{3} t P\right)}{\mathrm{d} \ln V}-\frac{1}{6},
\end{aligned}
$$

which is equivalent to Eq. (5) if $t$ is a constant. In view of the experimental evidence that $t$ is a decreasing function of $V$ we use Eq. (11) rather than Eq. (5) for our subsequent analysis.

We consider Eq. (11) at ultrahigh pressures where the $(T=0)$ equation of state is accurately given by [31,32]

$$
P=a V^{-5 / 3} \mathrm{e}^{-b V^{1 / 3}}, \quad a, b=\text { const }>0 . \quad(13)
$$

Eq. (13) includes an exponential screening correction to the equation of state of a free electron gas, namely $P=a V^{-5 / 3}$ where $a=2.337 Z^{5 / 3} \mathrm{TPa} \AA^{5}, Z$ being the atomic number [32]. It agrees with very accurate numerical Thomas- Fermi-Dirac results to within $2 \%$ over the compression range of $1-15$ with the exception of the alkali and alkalineearth metals [31]. Using the equation of state Eq. (13) in Eq. (11) we obtain

$$
\gamma=\frac{4(5-2 t)+2(4-t) b V^{1 / 3}+b^{2} V^{2 / 3}+6 V \mathrm{~d} t / \mathrm{d} V}{6\left(5-2 t+b V^{1 / 3}\right)} . \quad(14)
$$

It follows that $\gamma \rightarrow 2 / 3$ as $V \rightarrow 0$ for every asymptotic value of $t$ except $t=5 / 2$. If $t=5 / 2$ then $\gamma \rightarrow 1 / 2$ as $V \rightarrow 0$, in agreement with theoretical predictions. We conclude that $t$ is always asymptotic to $5 / 2$. Recent computer calculations

of the compression dependence of $t$ for $\gamma$-Fe [13] corroborate this conclusion and also show that $t$ can saturate at quite moderate compressions: $t=2.46 \pm 0.03$ at compressions of only 1.5-2.

The cold-curve $(T=0)$ pressure (13) is an analytic function of $x$ everywhere except at the origin (infinite compression) where it has a pole of order five. (The majority of model equations of state are analytic in $x$ except for poles at $x=0$. See Holzapfel [32] for a list of 16 examples.) Consequently, both $P / B$ and $B^{\prime}$ are analytic for $x \geq 0$. Given the analyticity of $\gamma, P / B$, and $B^{\prime}$ for $x \geq 0$, it follows from Eq. (11) that $t$ must also be an analytic function of $x$ for $x \geq 0$, hence it can be represented by the power series

$$
t=5 / 2-\sum_{i=1}^{\infty} t_{i} x^{i}. \quad (15)
$$

The first sub-leading coefficient, $t_{i}$, must be non-negative if $t$ is in fact a monotonically increasing function of compression. Substituting this series in Eq. (14) and expanding we find that the asymptotic form of $\gamma$ is

$$
\gamma=\frac{1}{2}+\frac{b^{2}+2 b t_{1}-2 t_{2}}{6 b+12 t_{1}} V^{1 / 3}+\cdots. \quad (16)
$$

It is expected that the $V^{1 / 3}$ term is always present in the series expansion of $\gamma$, i.e. $b^{2}+2 b t_{1}-2 t_{2} \neq 0$. Thus the generalized SDMVZ formula leads to $\gamma \sim 1 / 2+c_{1} x, x \rightarrow 0$, in agreement with Eq. (6).

In summary, we have (i) generalized the SDMVZ formula for $\gamma(\rho)$ to account for a density-dependent $t$, (ii) shown that $\gamma$ goes to its theoretical high-pressure limit 1/2 only if $t$ is asymptotic to $5 / 2$, and (iii) demonstrated that our model for the Grüneisen parameter and the generalized SDMVZ formula, Eq. (11), have the same asymptotic behavior provided $t$ is an analytic function of $x$, and $t(0)=5 / 2$.

## 4. Determination of model parameter values

In this section we outline the procedure for extracting the numerical values of the three model parameters $\gamma_{1}, \gamma_{2}$, and $q$ from data and determine their values for 20 elemental solids.

Ideally, one would fit our model (7) to data on $\gamma(\rho)$ and extract the values of $\gamma_{1}, \gamma_{2}$, and $q$, but such data sets are very rarely available. Alternatively, one could fit the functional form Eq. (8) to $T_{\mathrm{m}}(\rho)$ data, but such data are very rarely available either since experiment usually determines $T_{\mathrm{m}}(P)$. Typically, the only available data on $\gamma$ are $\gamma(\rho_{300}=\rho$ $(P=0, T=300 \mathrm{~K}))$, which is approximately equal to $\gamma_{\mathrm{th}}(T=300 \mathrm{~K})$, and $\gamma(\rho_{\mathrm{m}}=\rho(P=0, T=T_{\mathrm{m}}))$ which can be found by equating $\mathrm{d} T_{\mathrm{m}} / \mathrm{d} \rho$ at $P=0$ as given by the Kraut-Kennedy law [33].

$$
T_{\mathrm{m}}(\rho)=T_{\mathrm{m}}(\rho_{\mathrm{m}})\left[1+2\left(\gamma(\rho_{\mathrm{m}})-\frac{1}{3}\right)\left(\frac{\rho}{\rho_{\mathrm{m}}}-1\right)\right] \quad (17)
$$

to $\mathrm{d} T_{\mathrm{m}} / \mathrm{d} \rho=(B_{\mathrm{m}} / \rho_{\mathrm{m}}) \mathrm{d} T_{\mathrm{m}} / \mathrm{d} P$, where $B_{\mathrm{m}}$ and $\mathrm{d} T_{\mathrm{m}} / \mathrm{d} P$ at $P=$ 0 are taken from experiment. The value of $B_{\mathrm{m}}$ is obtained by calculating bulk moduli at low temperatures from measured single-crystal elastic constants and then extrapolating to $T_{\mathrm{m}}$. The pressure derivative $\mathrm{d} T_{\mathrm{m}} / \mathrm{d} P$ is obtained either directly from low-pressure melting curve data or indirectly from isobaric-heating measurements of $\Delta H$ ( $H$ is the enthalpy) and $\Delta V$ across the melting transition so that $\mathrm{d} T_{\mathrm{m}} / \mathrm{d} P=T_{\mathrm{m}}$ $\Delta V / \Delta H$ (Clausius-Clapeyron equation). Eq. (17) is obtained by expanding $T_{\mathrm{m}}(\rho)$ in a power series about $\rho_{\mathrm{m}}$ using Eqs. (4) and (7) with $\rho=\rho_{300}$ and $\rho=\rho_{\mathrm{m}}$ provides two conditions needed to determine the three parameters $\gamma_{1}, \gamma_{2}$, and $q$. The third condition comes from the ultrahigh pressure limit, which we discuss next.

The melting curve of a solid at ultrahigh pressures is described by the equation

$$
\frac{Z^{2} e^{2}}{a k_{\mathrm{B}} T_{\mathrm{m}}}=\Gamma_{\mathrm{m}}, \quad (18)
$$

where $a=(3 v / 4 \pi)^{1 / 3}$ is the Wigner-Seitz radius ( $v$ being the Wigner-Seitz volume) and $\Gamma_{\mathrm{m}}$, a dimensionless constant, is the OCP coupling parameter at melt. The value of the coupling parameter is $170-180$ for a bodycentered cubic (bcc) OCP crystal [34] (the recent calculation of $\Gamma_{\mathrm{m}}$ for a bcc crystal by Potekhin and Chabrier [35] gave $\Gamma_{\mathrm{m}}=175.0 \pm 0.4$ ), and as high as $200-210$ for a face-centered cubic (fcc) OCP crystal [36,37]. In the following analysis we make no distinction between bcc and fcc OCP crystals and take $\Gamma_{\mathrm{m}}=180$.

It follows from Eqs.(18) and (8) in the limit $\rho \rightarrow \infty$ with $\rho_{\mathrm{r}}=\rho_{\mathrm{m}}$ that

$$
T_{\mathrm{m}}(\rho_{\mathrm{m}}) v_{\mathrm{m}}^{1 / 3} \exp \left\{\frac{6 \gamma_{1}}{\rho_{\mathrm{m}}^{1 / 3}}+\frac{2 \gamma_{2}}{q \rho_{\mathrm{m}}^{q}}\right\}=\left(\frac{4 \pi}{3}\right)^{1 / 3} \frac{e^{2}}{k_{\mathrm{B}}} \frac{Z^{2}}{\Gamma_{\mathrm{m}}}, \quad (19)
$$

where $v_{\mathrm{m}}$, the Wigner-Seitz volume at the zero-pressure melting point, equals $a_{\mathrm{m}}^{3} / 2$ for a bcc and $a_{\mathrm{m}}^{3} / 4$ for a fcc crystal; $a_{\mathrm{m}}$ is the lattice constant.

![](./images/812362557573562370_1.jpg)

Fig. 1. Melting curve of Al: Eq. (8) with the Al parameters from Table 1 vs experimental data [40] and the results of calculations [42] (larger points). The experimental points have error bars of $\sim 100-150 \mathrm{~K}$ which are not shown on the plot.

![](./images/812362557573562370_2.jpg)

Fig. 2. Melting curve of Ar: Eq. (8) with the Ar parameters from Table 1 vs experimental data [43] and the results of calculations [44] (larger points).

We obtain the values of the parameters $\gamma_1, \gamma_2$ and $q$ by simultaneous solution of three non-linear equations, namely Eq. (7) for $\rho=\rho_{300}$ and $\rho=\rho_{\mathrm{m}}$, and Eq. (19) with $\Gamma_{\mathrm{m}}=180$. The value of $\gamma(\rho_{300})$, which is very rarely measured directly, can be approximated by $\gamma_{\mathrm{th}}(300)=\alpha B_{\mathrm{T}}/(\rho C_{\mathrm{V}})$ where $\alpha, B_{\mathrm{T}}$, and $C_{\mathrm{V}}$ are all measured at 300 K; the necessary room-temperature data can be found in Ref. [38] and the data on $\gamma_{\mathrm{th}}(300)$ in Ref. [39]. Parameter values for 20 elements are shown in Table 1; $\gamma_1$ and $\gamma_2$ are given to three significant figures, and $q$ to two significant figures.

The uncertainty in the value of $\gamma(\rho_{\mathrm{m}})$ is determined by the error bars on the measured melting temperatures and densities, usually a few percent. Typical uncertainties in $\alpha$, $B_{\mathrm{T}}$, and $C_{\mathrm{V}}$ result in an uncertainty of roughly $5\%$ in the value of $\gamma(\rho_{300})$ (we consider the difference between $\gamma(\rho_{300})$ and $\gamma_{\mathrm{th}}(300)$ to be negligible). These uncertainties in $\gamma(\rho_{\mathrm{m}})$ and $\gamma(\rho_{300})$ imply an uncertainty $\sim 5\%$ in $\gamma_1$, values of $q$ that are accurate to $\sim 40\%$, and order-of-magnitude uncertainties in $\gamma_2$ that are attributable to a very strong sensitivity to the value of $q$. Let us take, as an example, copper; with $\gamma(\rho_{\mathrm{m}})=2.48$ and $\gamma_{\mathrm{th}}(300)=2.19\pm 0.1$ we find, neglecting uncertainties in the density, $\gamma_1=1.84\pm 0.08, \gamma_2=430-1.95\times 10^6$, and $q=4.7\pm 2.0$.

Although the values of $\gamma_2$ have order-of-magnitude uncertainties, we note that if Eq. (7) is rewritten in a 'scaled' form, $\gamma=1/2+\tilde{\gamma}_1(\rho_{300}/\rho)^{1/3}+\tilde{\gamma}_2(\rho_{300}/\rho)^q$, the values of both $\tilde{\gamma}_1$ and $\tilde{\gamma}_2$ are of order 1, as can be seen in Table 1 where we also include the values of both $\tilde{\gamma}_1$ and $\tilde{\gamma}_2$ to three significant figures.

![](./images/812362557573562370_3.jpg)

Fig. 4. Melting curve of Pd: Eq. (8) with the Pd parameters from Table 1 vs results of calculations [48]; two larger points are the shock-melting datapoints of Ref. [48].

### 5. Melting curves

In this section we calculate melting curves using Eq. (8) with parameters determined in the previous section and compare the results with available experimental and theoretical data.

In Fig. 1 we compare our theoretical aluminum melting curve to experimental data [40]. Although the theoretical melting curve looks like a fit to the datapoints,

![](./images/812362557573562370_4.jpg)

Fig. 3. Melting curve of Cu: Eq. (8) with the Cu parameters from Table 1 vs data. The smaller points are from a new tabulated SESAME melting curve for Cu [6]. The larger points are the $P=0$ reference point at (in g/cc) $\rho=8.4$, and the shock-melting points of Ref. [45] at $\rho=10.2, 12.2$ and 14.3, and of Refs. [46,47] at $\rho=14.0$.

![](./images/812362557573562370_5.jpg)

Fig. 5. Melting curve of Pt: Eq. (8) with the Pt parameters from Table 1 vs results of calculations [48]; two larger points are the shock-melting datapoints of Ref. [48].

![](./images/812362557573562370_6.jpg)

Fig. 6. Comparison of $\gamma_{1}=(2 / 21)(\ln Z)^{7 / 3}+2 / 13$ to the $\gamma_{1}(Z)$ entries in Table 1.

the parameters $\gamma_{1}, \gamma_{2}$, and $q$ were not obtained from such a fit but rather from the zero-pressure data $\gamma(\rho_{300}=2.7$ g/cc) = 2.5 [39], $\gamma(\rho_{m}=2.55$ g/cc) = 2.83 [33], and $T_{m}(\rho_{m})=933.5$ K, and Eqs. (7) and (19). In Figs. 2-5 we compare our theoretical melting curves for argon, copper, palladium, and platinum to melting data available in the literature. Agreement between our theoretical curves and experiment and calculations is good in all five cases.

## 6. The $Z$ dependence of $\gamma_{1}$

It is evident from Table 1 that $\gamma_{1}$ is a slowly increasing function of atomic number. We have fit the forms $\gamma_{1}=C_{1} Z^{n}+C_{2}$ and $\gamma_{1}=C_{1}(\ln Z)^{n}+C_{2}$, where $C_{1}, C_{2}$ and $n$ are constants, to the table entries and found that the best fits, of comparable accuracy, are $\gamma_{1}=$ $(12 / 11) Z^{1 / 3}-11 / 7$ and $\gamma_{1}=(2 / 21)(\ln Z)^{7 / 3}+2 / 13$. These fits may be used to predict $\gamma_{1}$ in those cases where data provide only two constraints on $\gamma_{1}, \gamma_{2}$ and $q$. In Fig. 6 we plot $\gamma_{1}=(2 / 21)(\ln Z)^{7 / 3}+2 / 13$ along with the $\gamma_{1}(Z)$ entries in Table 1.

We note that the $\tilde{\gamma}_{1}$ entries in Table 1 can be fitted to the same functional form, i.e. $\tilde{\gamma}_{1}(Z)=(7 / 26) Z^{1 / 3}+7 / 59$, albeit with much lower accuracy (much higher $\chi^{2}$ ) than that of the $\gamma_{1}(Z)$ fits.

## 7. Concluding remarks

Our model for $\gamma$ accurately fits low-pressure data and agrees with theoretical predictions that $\gamma \to 1 / 2$ at ultrahigh pressures. Its accuracy cannot be determined at intermediate compressions because there are no experi- mental data. However, comparison of our calculated melting curves for aluminum and argon to the correspond- ing data in Figs. 1 and 2 demonstrates that our model is accurate up to compressions of at least 2. (Our calculated melting curve for copper, shown in Fig. 3, is in excellent agreement with a new SESAME copper melting curve [6] up to compressions $\sim 10$ ). In our model the deviation of $\gamma \rho^{q_{eff }}$ from a constant over the range of compressions from 1 to 1.5 is generally less than $10 \%$. Finally, we note that our model for $\gamma$ can be used to calculate shear moduli along the solidus using Eq. (8) and the formula $G(\rho, T_{m}(\rho)) /(\rho T_{m}(\rho))=$ constant [41].

## Acknowledgements

We wish to thank J.C. Boettger, C.W. Greeff, J.D. Johnson, and G.W. Pfeufer for helpful discussions on the subject of the Grüneisen parameter. One of us (L.B.) wishes to thank V.N. Zharkov for very useful correspon- dence on the analytic form for the Grüneisen parameter, S.V. Stankus for valuable data on the densities of solids at their normal melting points, and J.-W. Jeong for numerical data on the calculated melting curves of palladium and platinum.

## References

[1] E. Grüneisen, Ann. Phys. (Leipzig) 39 (1912) 257.
[2] L.A. Girifalco, Statistical Mechanics of Solids, Oxford University Press, Oxford, 2000, Section 5.2.
[3] T.H.K. Barron, Ann. Phys. (NY) 1 (1957) 77.
[4] J.-P. Poirier, Introduction to the Physics of the Earth's Interior, second ed., Cambridge University Press, Cambridge, 2000.
[5] O.L. Anderson, Equations of State of Solids for Geophysics and Ceramic Science, Oxford University Press, New York, 1995, p. 281.
[6] J.D. Johnson, private communication.
[7] V.N. Zharkov, V.A. Kalinin, Equations of State for Solids at High Pressures and Temperatures, Consultants Bureau, New York, 1971.
[8] J.C. Slater, Introduction to Chemical Physics, McGraw-Hill, New York, 1939, Chapter XII.
[9] J.S. Dugdale, K.C. MacDonald, Phys. Rev. 89 (1953) 832.
[10] V.Ya. Vashchenko, V.N. Zubarev, Fiz. Tv. Tela 5 (1963) 886 [Sov. Phys. Solid State, 5 (1963) 653].
[11] This formula seems to have first appeared in Ref. [10] the form
$$
\gamma=\frac{t-2}{3}-\frac{V}{2} \frac{\mathrm{d}^{2}\left(P V^{2 t / 3}\right) / \mathrm{d} V^{2}}{\mathrm{~d}\left(P V^{2 t / 3}\right) / \mathrm{d} V},
$$
which is equivalent to Eq. (5) for constant $t$.
[12] R.D. Irvine, F.D. Stacey, Phys. Earth Planet. Int. 11 (1975) 157.
[13] M.A. Barton, F.D. Stacey, Phys. Earth Planet. Int. 39 (1985) 167. F.D. Stacey, Phys. Earth Planet. Int. 89 (1995) 219. F.D. Stacey, Phys. Earth Planet. Int. 98 (1996) 65.
[14] Y. Wang, L. Li, Phys. Rev. B 62 (2000) 196.
[15] C. Dongquan, Z. Wanxing, in: C. Homan, R.K. MacCrone, E. Whalley (Eds.), High Pressure Science and Technilogy, Part III, North- Holland, Amsterdam, 1984, p. 247.
[16] D.A. Young, M. Corey, J. Appl. Phys. 78 (1995) 3748.
[17] D.A. Young, Phase Diagrams of the Elements, University of California Press, Berkeley, 1991, Chapter 17.
[18] V.P. Kopyshev, Doklady Acad. Sci. USSR 161 (1965) 1067 [Sov. Phys. Doklady, 10 (1965) 338]. It is claimed in ref that the lattice dynamics given in this paper is incorrect as it gives rise to vanishing shear waves in the high-density limit. The correct lattice dynamics is given in Refs. [21,23].
[19] W.B. Hubbard, Planetary Interiors, Van Nostrand Reinhold Co, New York, 1984, p. 34.

[20] A.C. Holt, M. Ross, Phys. Rev. B 1 (1970) 2700. M. Ross, Rep. Prog. Phys. 48 (1985) 1. M. Ross, D.A. Young, Ann. Rev. Phys. Chem. 44 (1993) 61.

[21] H. Nagara, T. Nakamura, Phys. Rev. B 31 (1985) 1844.

[22] R.M. Moore, K.H. Warren, D.A. Young, G.B. Zimmermann, Phys. Fluids 31 (1988) 3059.

[23] Yu.V. Petrov, High Press. Res. 11 (1994) 313.

[24] W.B. Holzapfel, M. Hartwig, W. Sievers, J. Phys. Chem. Ref. Data 30 (2001) 515.

[25] O.L. Anderson, Equations of State of Solids for Geophysics and Ceramic Science, Oxford University Press, New York, 1995, p. 8.

[26] G.H. Miller, T.J. Ahrens, E.M. Stolper, J. Appl. Phys. 63 (1988) 4469. O.L. Anderson, D.G. Isaak, S. Yamamoto, J. Appl. Phys. 65 (1989) 1534.

[27] A.V. Parshukov, Fiz. Tv. Tela 27 (1985) 1228 [Sov. Phys. Solid State, 27 (1985) 741].

[28] J.P.Romain,A.Migault,J.Jacquesson,J.Phys.Chem.Sol.41(1980)323.

[29] K. Nagayama, Y. Mori, J. Phys. Soc. Jpn 63 (1994) 4070.

[30] Q. Wu, F.-Q. Jing, X.-Z. Li, Chin. Phys. Lett. 19 (2002) 528.

[31] J.F. Barnes, Phys. Rev. 153 (1967) 153.

[32] W.B. Holzapfel, in: R. Pucci, G. Piccitto (Eds.), Molecular Systems Under High Pressure, North-Holland, Amsterdam, 1991, p. 61.

[33] E.A. Kraut, G.C. Kennedy, Phys. Rev. Lett. 16 (1966) 608. E.A. Kraut, G.C. Kennedy, Phys. Rev. 151 (1966) 668. The formula (17) was also derived in.J. Gilvarry, Phys. Rev. Lett. 16 (1966) 1089. S.N. Vaidya, E.S. Raja Gopal, Phys. Rev. Lett. 17 (1966) 635.

[34] L. Burakovsky, D.L. Preston, Phys. Rev. E 63 (2001) 06740 and references therein.

[35] A.Y. Potekhin, G. Chabrier, Phys. Rev. E 62 (2000) 8554.

[36] H.L. Helfer, R.L. McCory, H.M. Van Horn, J. Stat. Phys. 37 (1984) 577.

[37] F.H. Ree, in: R. Pucci, E.G. Piccitto (Eds.), Molecular Systems Under High Pressure, North-Holland, Amsterdam, 1991, p. 33.

[38] Appendices of ref. [17]; http://www.webelements.com/

[39] L.A. Girifalco, K. Kniaz, J. Mater. Res. 12 (1997) 311.

[40] A. Hänström, P. Lazor, J. Alloys Comp. 305 (2000) 209.

[41] L. Burakovsky, D.L. Preston, R.R. Silbar, J. Appl. Phys. 88 (2000) 6294.

[42] J.A. Moriarty, D.A. Young, M. Ross, Phys. Rev. B 30 (1984) 578.

[43] V.M. Cheng, W.B. Daniels, R.K. Crawford, Phys. Lett. A 43 (1973) 109.

[44] C.-S. Zha, R. Boehler, D.A. Young, M. Ross, J. Chem. Phys. 85 (1986) 1034.

[45] V.D. Urlin, Zh. Eksp. Teor. Fiz. 49 (1965) 485 [Sov. Phys. JETP, 22 (1966) 341].

[46] J.A. Moriarty, in: M. Gupta (Ed.), Shock Waves in Condensed Matter, Plenum Press, New York, 1986, p. 101.

[47] D.B. Hayes, R.S. Hixson, R.G. McQueen, in: M.D. Furnish, L.C. Chhabildas, R.S. Hixson (Eds.), Shock Compression of Condensed Matter—1999, AIP, Melville, NY, 2000, p. 483.

[48] J.-W. Jeong, K.J. Chang, J. Phys. Condens. Mater. 11 (1999) 3799.