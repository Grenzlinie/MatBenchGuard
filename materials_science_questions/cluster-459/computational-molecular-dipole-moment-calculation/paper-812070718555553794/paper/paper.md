BULLETIN OF THE CHEMICAL SOCIETY OF JAPAN, VOL. 45, 2429-2433 (1972)

# Dipole Moment Functions of CO and HCl

Isao Suzuki

Department of Chemistry, Faculty of Science, The University of Tokyo, Bunkyo-ku, Tokyo
(Received April 11, 1972)

A general formalism is presented for the least-squares determination of dipole moment functions of diatomic molecules in which the radial part wave functions obtained as numerical solutions of vibration and vibration-rotation Hamiltonian matrix are used. Although this approach is purely numerical, the advantage of using orthonormal basis and perturbed wave functions is retained. Attempts have been made on the determination of the cubic dipole moment functions for the CO and HCl molecules. All the available data of dipole as well as transition moments and the Herman-Wallis factors for these molecules are considered in the refinement process. The following cubic dipole moment functions are obtained (in Debye): $M(\Delta r)=0.1243-3.0722(\Delta r)+0.1909(\Delta r)^{2}+2.1856(\Delta r)^{3}$ for CO and $M(\Delta r)=1.093+0.949(\Delta r)+0.034(\Delta r)^{2}-0.78(\Delta r)^{3}$ for HCl.

Dipole moment of a diatomic molecule in a given electronic state solely depend on its internuclear distance and can be expressed as $M(r)$. It is customary to expand $M(r)$ in a power series around the equilibrium distance $r_{e}$,
$$
M(r)=\sum_{k=0} M_{k}\left(r-r_{e}\right)^{k}=\sum_{k=0} M_{k}(\Delta r)^{k} \tag{1}
$$

Equation (1) may be rewritten by using dimensionless normal coordinate $q=(\omega_{e}/2B_{e})^{1/2}(\Delta r/r_{e})$
$$
M(q)=\sum_{k=0} p_{k} q^{k}, \tag{2}
$$
where $p_{k}=M_{k}r_{e}^{\gamma 1/2}$ and $\gamma=(2B_{e}/\omega_{e})$. The diagonal matrix element
$$
\mu_{v,J}=\langle v,J|M(q)|v,J\rangle \tag{3}
$$
represents the dipole moment of a vibration-rotation state $(v,J)$, where $|v,J\rangle$ is the wave function for the radial part Schrödinger equation, while the intensity of a vibration-rotation line $(v,J\rightarrow v',J')$ is proportional to the square of matrix element
$$
R_{v,J}^{v',J'}=\langle v'J'|M(q)|v,J\rangle. \tag{4}
$$

The total intensity of a vibrational transition $(v\rightarrow v')$ is related with the rotationless matrix element
$$
R_{v}^{v'}=\langle v'|M(q)|v\rangle, \tag{5}
$$
where $|v\rangle=|v,0\rangle$. Similarly, Eq. (3) is reduced to
$$
\mu_{v}=\langle v|M(q)|v\rangle. \tag{6}
$$

Therefore, the coefficients $p_{k}$ in Eq. (2) can be determined from the measured infrared intensities or dipole moments, provided that accurate wave functions are known for the vibration-rotation states involved. In a previous paper, $^{1)}$ a method was given in which the vibration or vibration-rotation levels of a diatomic molecule are related with the harmonic and anharmonic force constants by solving the vibrational Hamiltonian numerically. It was emphasized that a set of orthonormal wave functions is readily obtained as linear combinations of the harmonic oscillator basis functions through numerical diagonalization, $^{2)}$
$$
|v\rangle=\sum_{n=0}a_{vn}|n\rangle \text{ and } \sum_{n=0}a_{vn}a_{v'n}=\delta_{vv'} \tag{7}
$$

As described in I, the coefficients $a_{v^{n}}$'s for the low lying vibrational states have been determined very accurately from the hexic and octic potential functions respective for the CO and HCl molecules. These results are combined with the recent measurements of infrared line intensities and of dipole moments to determine the dipole moment functions for these molecules. An effort has been made to collect and evaluate as many relevant data as possible.

## Determination of Dipole Moment Function

A number of attempts have been made to determine the dipole moment functions of diatomic molecules. The previous works have been summarized by Young and Eachus, $^{3)}$ who calculated the dipole moment matrix elements for the CO molecule by a purely numerical method, in which the radial part Schrödinger equation is solved by a computer program. The resultant wave functions were used to compute $R_{v}^{v'}$ and $R_{v,J}^{v',J'}$. Recently, Toth, Hunt, and Plyler $^{4)}$ have calculated the same matrix elements by

1) I. Suzuki, This Bulletin, 44, 3277 (1971); Hereafter referred to as I.
2) The indices $n$ and $m$ are used to indicate the harmonic oscillator wave functions $\varphi_{n}{}^{0}(q)$ and $\varphi_{m}{}^{0}(q)$, and $v$ and $v'$ refer to the true (perturbed) vibrational states. Symbols and notations used in this paper are given in I.
3) L. A. Young and W. J. Eachus, J. Chem. Phys., 44, 4195 (1966).
4) R. A. Toth, R. H. Hunt, and E. K. Plyler, J. Mol. Spectrosc., 32, 74, 85 (1969).

an analytical method with the cubic dipole moment function and the quintic potential function, the second- order perturbation method being used. These authors have extended their calculation to the HCl molecule, the third-order perturbation theory was used in this case.⁵) More recently, Kaiser⁶) has analyzed the molecular beam electric resonance spectra of HCl and and DCl, and obtained very precise values of dipole moments for a few vibration-rotation states. He has used the 'wave function approximation' to compute the coefficients $M_{0}-M_{4}$ from the RKR potential.

Our present approach is to use the coefficients $a_{v n}$'s ($v \leq 4$) for CO and HCl which have been determined precisely by the numerical diagonalization of the vib- rational Hamiltonian matrix. Although this method is purely numerical as the RKR approach, we can take full advantage of the orthonormal property of the basis and the perturbed wave functions. This seems to be very useful for practical purpose. It will be shown later that the radial part wave function for the vibration- rotation state $(v,J)$ is also expressed as
$$|v,J>=\sum_{n=0} b_{v n}{ }^{J}|n>.\qquad(8)$$

Equations (3)-(6) may be written by using Eqs. (7) and (8),
$$\mu_{v J}=\sum_{k=0} p_{k} \sum_{n=0} \sum_{m=0} b_{v n}{ }^{J} b_{v m}{ }^{J}\left\langle m\left|q^{k}\right| n\right\rangle,\qquad(9)$$

$$R_{v J}{ }^{v^{\prime} J^{\prime}}=\sum_{k=0} p_{k} \sum_{n=0} \sum_{m=0} b_{v n}{ }^{J} b_{v^{\prime} m}{ }^{J^{\prime}}\left\langle m\left|q^{k}\right| n\right\rangle,\qquad(10)$$

$$\mu_{v}=\sum_{k=0} p_{k} \sum_{n=0} \sum_{m=0} a_{v n} a_{v m}\left\langle m\left|q^{k}\right| n\right\rangle,\qquad(11)$$

$$R_{v}{ }^{v^{\prime}}=\sum_{k=0} p_{k} \sum_{n=0} \sum_{m=0} a_{v n} a_{v^{\prime} m}\left\langle m\left|q^{k}\right| n\right\rangle,\qquad(12)$$

The matrix element $\langle m|q^{k}|n\rangle$ is well-known (see, for example, Table A-1 in I), and its value can be generated in a computer by a subroutine OPERQ ($k \leq 8$). The coefficients $a_{v n}$ and $b_{v n}{ }^{J}$ are evaluated through numerical diagonalization, it is much simpler to use Eqs. (9)-(12) for the evaluation of the dipole and transition moments. This is the method we have used throughout this study.

Herman-Wallis Factors $C_{v}^{v^{\prime}}$ and $D_{v}^{v^{\prime}}$. It was first recognized by Herman and Wallis⁷) that the vib- ration-rotation transition moment, $R_{v J}^{v^{\prime} J^{\prime}}$ is related with the rotationless transition moment $R_{v}^{v^{\prime}}$ as
$$\begin{aligned}
\left|R_{v J}{ }^{v^{\prime} J^{\prime}}\right|^{2} & =\left|R_{v}{ }^{v^{\prime}}(m)\right|^{2}=\left|R_{v}{ }^{v^{\prime}}\right|^{2} F_{v}{ }^{v^{\prime}} \\
& =R_{v}{ }^{v^{\prime}}\left|{ }^{2}\left(1+C_{v}{ }^{v^{\prime}} m+D_{v}{ }^{v^{\prime}} m^{2}+\cdots\right),\right.
\end{aligned}\qquad(13)$$
where $m=-J$ for $P$-branch and $m=J+1$ for $R$ branch. In the present study, the Herman-Wallis factors are used as input data, instead of using numer- ous vibration-rotation transition moments.

Numerical Computations. The numerical com- putations have been carried out on a HITAC 5020E computer of the Computer Centre in the University of Tokyo, double precision arithmetic (64 bits) being used.

Input Data. For the determination of the di- pole moment function, i.e. the coefficients $M_{k}$'s, we

5) R. A. Toth, R. H. Hunt, and E. K. Plyler, J. Mol. Spectrosc., 35, 110 (1970).
6) E. W. Kaiser, J. Chem. Phys., 53, 1686 (1970).
7) R. Herman and R. F. Wallis, ibid., 23, 637 (1955).

<table><caption>Table 1. Experimental and calculated transition moments $(R_{v}^{v^{\prime}})$, dipole moments $(\mu_{v})$ and Herman-Wallis factors $(C_{v}^{v^{\prime}}: D_{v}^{v^{\prime}})$ for CO</caption>
<thead>
  <tr>
    <th></th>
    <th>Expl.</th>
    <th>Weight</th>
    <th>Calcd(1)</th>
    <th>Calcd(2)</th>
    <th>Ref.</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$R_{0}^{1}$</td>
    <td>$-0.104$</td>
    <td>0.025</td>
    <td>$-0.1035$</td>
    <td>$-0.1038$</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$R_{0}^{2}$</td>
    <td>0.00653</td>
    <td>1.0</td>
    <td>0.00632</td>
    <td>0.00624</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$R_{0}^{3}$</td>
    <td>$-0.000424$</td>
    <td>290.0</td>
    <td>$-0.000419$</td>
    <td>$-0.000611$</td>
    <td>c</td>
  </tr>
  <tr>
    <td>$\mu_{0}$</td>
    <td>0.112</td>
    <td>1.0</td>
    <td>0.112</td>
    <td>0.112</td>
    <td>d</td>
  </tr>
  <tr>
    <td>$C_{0}^{1}$</td>
    <td>0.0</td>
    <td>1.0</td>
    <td>0.0002</td>
    <td>0.0002</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$C_{0}^{2}$</td>
    <td>0.0054</td>
    <td>0.0625</td>
    <td>0.0051</td>
    <td>0.0052</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$C_{0}^{3}$</td>
    <td>0.0118</td>
    <td>0.02</td>
    <td>0.0114</td>
    <td>0.0078</td>
    <td>c</td>
  </tr>
  <tr>
    <td>$D_{0}^{1}$</td>
    <td>0.0</td>
    <td>1.0</td>
    <td>$7×10^{-6}$</td>
    <td>$7×10^{-6}$</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$D_{0}^{2}$</td>
    <td>0.00004</td>
    <td>0.02</td>
    <td>$0.00003_{4}$</td>
    <td>$0.00002_{2}$</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$D_{0}^{3}$</td>
    <td>0.00018</td>
    <td>1.0</td>
    <td>$0.00008_{8}$</td>
    <td>$0.00004_{3}$</td>
    <td>c</td>
  </tr>
</tbody>
</table>

$p_{0}=0.1243 \pm 0.0002, \quad p_{1}=-0.1465 \pm 0.0002, \quad p_{2}=0.000434 \pm$ $0.000015, p_{3}=0.000237 \pm 0.000009$ Debye.

a) Ref. 3.
b) C. L. Korb, R. H. Hunt, and E. K. Plyler, J. Chem. Phys., 48, 4252 (1968).
c) Ref. 4.
d) C. A. Burros, J. Chem. Phys., 28, 427 (1958).

<table><caption>Table 2. Experimental and calculated transition moments $(R_{v}^{v^{\prime}})$, dipole moments $(\mu_{v})$ in Debye, and Herman Wallis factors $(C_{v}^{v^{\prime}}: D_{v}^{v^{\prime}})$ for HCl and DCl</caption>
<thead>
  <tr>
    <th>HCl</th>
    <th>Expl.</th>
    <th>Weight</th>
    <th>Calcd(a)</th>
    <th>Calcd(b)</th>
    <th>Ref.</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$R_{0}^{1}$</td>
    <td>0.068</td>
    <td>0.6</td>
    <td>0.071</td>
    <td>0.071</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$R_{0}^{2}$</td>
    <td>$-0.0080$</td>
    <td>39.0</td>
    <td>$-0.0076$</td>
    <td>$-0.0083$</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$R_{0}^{3}$</td>
    <td>0.00051</td>
    <td>0.0</td>
    <td>0.00051</td>
    <td>0.00090</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$R_{1}^{2}$</td>
    <td>0.0971</td>
    <td>0.01</td>
    <td>0.0999</td>
    <td>0.0986</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$R_{2}^{3}$</td>
    <td>0.1187</td>
    <td>0.01</td>
    <td>0.1203</td>
    <td>0.1188</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$\mu_{0}$</td>
    <td>1.1085</td>
    <td>4.0</td>
    <td>1.1083</td>
    <td>1.1086</td>
    <td>c</td>
  </tr>
  <tr>
    <td>$\mu_{1}$</td>
    <td>1.1390</td>
    <td>1.0</td>
    <td>1.1386</td>
    <td>1.1373</td>
    <td>c</td>
  </tr>
  <tr>
    <td>$\mu_{2}$</td>
    <td>1.1685</td>
    <td>1.0</td>
    <td>1.1679</td>
    <td>1.1653</td>
    <td>c</td>
  </tr>
  <tr>
    <td>$C_{0}^{1}$</td>
    <td>$-0.026$</td>
    <td>0.25</td>
    <td>$-0.027$</td>
    <td>$-0.027$</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$C_{0}^{2}$</td>
    <td>$-0.0086$</td>
    <td>0.44</td>
    <td>$-0.0058$</td>
    <td>$-0.0057$</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$C_{0}^{3}$</td>
    <td>0.017</td>
    <td>0</td>
    <td>0.0102</td>
    <td>0.007</td>
    <td>a, b</td>
  </tr>
  <tr>
    <td>$D_{0}^{1}$</td>
    <td>0.00045</td>
    <td>25.0</td>
    <td>0.00027</td>
    <td>0.00024</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$D_{0}^{2}$</td>
    <td>0.00041</td>
    <td>25.0</td>
    <td>0.00036</td>
    <td>0.00023</td>
    <td>a</td>
  </tr>
  <tr>
    <td>$D_{0}^{3}$</td>
    <td>—</td>
    <td>0</td>
    <td>0.00106</td>
    <td>0.00045</td>
    <td>—</td>
  </tr>
  <tr>
    <td>DCl</td>
    <td>Expl.</td>
    <td>Weight</td>
    <td>Calcd(a)</td>
    <td>Calcd(b)</td>
    <td>Ref.</td>
  </tr>
  <tr>
    <td>$R_{0}^{1}$</td>
    <td>0.0563</td>
    <td>0.01</td>
    <td>0.0606</td>
    <td>0.0600</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$R_{0}^{2}$</td>
    <td>$-0.0050$</td>
    <td>0.01</td>
    <td>$-0.0053$</td>
    <td>$-0.0058$</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$R_{0}^{3}$</td>
    <td>0.00031</td>
    <td>0.01</td>
    <td>0.00028</td>
    <td>0.00054</td>
    <td>b</td>
  </tr>
  <tr>
    <td>$\mu_{0}$</td>
    <td>1.1033</td>
    <td>4.0</td>
    <td>1.1040</td>
    <td>1.1045</td>
    <td>c</td>
  </tr>
  <tr>
    <td>$\mu_{1}$</td>
    <td>1.1256</td>
    <td>1.0</td>
    <td>1.1258</td>
    <td>1.1252</td>
    <td>c</td>
  </tr>
  <tr>
    <td>Debye</td>
    <td colspan="2">Set(a)</td>
    <td colspan="3">Set(b)</td>
  </tr>
  <tr>
    <td>$p_{0}$</td>
    <td colspan="2">$1.0930 \pm 0.0004$</td>
    <td colspan="3">$1.0940 \pm 0.0005$</td>
  </tr>
  <tr>
    <td>$p_{1}$</td>
    <td colspan="2">$0.1018 \pm 0.0004$</td>
    <td colspan="3">$0.1008 \pm 0.0006$</td>
  </tr>
  <tr>
    <td>$p_{2}$</td>
    <td colspan="2">$0.00039 \pm 0.00033$</td>
    <td colspan="3">$-0.00099 \pm 0.00047$</td>
  </tr>
  <tr>
    <td>$p_{3}$</td>
    <td colspan="2">$-0.00096 \pm 0.00029$</td>
    <td colspan="3">$-0.00068 \pm 0.00040$</td>
  </tr>
</tbody>
</table>

a) Ref. 5. b) W.S. Benedict, R. Herman, G. E. Moore, and S. Silverman, J. Chem. Phys., 26, 1671 (1957). c) Ref.6.

have tried to use all the available data on the dipole and transition moments, those on the isotopic species being included.⁸) The data used in the present study for the CO and HCl molecules are listed respectively in Tables 1 and 2. The relative weights of these data are estimated from the quoted values of error limits and are also included in Tables 1 and 2.

Potential Functions. Throughout the present study, the results with the hexic potential function for CO (Set 9) and the octic potential function for HCl (Set 10) given in I are used. The coefficients $a_{vn}$'s were obtained numerically from the above potentials, and the matrix elements of the form
$$\langle v|q^{k}|v'\rangle=\sum_{n=0}\sum_{m=0}a_{vn}a_{v'm}\langle n|q^{k}|m\rangle\tag{14}$$
are computed. Numerical values of the relevant matrix elements are listed in Tables 3 and 4 respectively for CO and HCl, the values of force constants are re- produced at the bottom of each table.

<table>
<caption>Table 3. Matrix elements $\langle v|q^{k}|v'\rangle$ for CO</caption>
<tbody>
<tr>
<th>$v$</th>
<th>$v'$</th>
<th>$k=0$</th>
<th>$k=1$</th>
<th>$k=2$</th>
<th>$k=3$</th>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>1.0</td>
<td>0.085720</td>
<td>0.511891</td>
<td>0.159313</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>0.0</td>
<td>0.709445</td>
<td>0.203138</td>
<td>1.123690</td>
</tr>
<tr>
<td>0</td>
<td>2</td>
<td>0.0</td>
<td>$-0.040501$</td>
<td>0.697083</td>
<td>0.363200</td>
</tr>
<tr>
<td>0</td>
<td>3</td>
<td>0.0</td>
<td>0.003883</td>
<td>$-0.097995$</td>
<td>0.810633</td>
</tr>
<tr>
<td colspan="6">$\omega_{e}=2169.9191$, $k_{3}=-123.5529$, $k_{4}=8.7314$, $k_{5}=-0.46782$,<br>$k_{6}=0.01579$, $B_{e}=1.931241\ \mathrm{cm}^{-1}$.</td>
</tr>
</tbody>
</table>

Evaluation of Coefficient $b_{vn}^{J}$. In order to cal- culate $R_{vJ}^{v'J'}$ and $\mu_{vJ},b_{vn}^{J}$ in Eq. (8) must be known. This may be done by two different ways. Since the wave function $|v\rangle=|v,0\rangle$ is known, the perturbation method may be applied;
$$|v,J\rangle=|v\rangle+\sum_{v'\neq v}'H_{vv'^{(1)}}|v'\rangle/(E_{v}^{0}-E_{v'}^{0})\tag{15}$$

<table>
<caption>Table 4. Matrix elements $\langle v|q^{k}|v'\rangle$ for HCl and DCl</caption>
<tbody>
<tr>
<th></th>
<th>$v$</th>
<th>$v'$</th>
<th>$k=0$</th>
<th>$k=1$</th>
<th>$k=2$</th>
<th>$k=3$</th>
</tr>
<tr>
<td rowspan="8">HCl</td>
<td>0</td>
<td>0</td>
<td>1.0</td>
<td>0.151165</td>
<td>0.535999</td>
<td>0.288249</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1.0</td>
<td>0.459392</td>
<td>1.767420</td>
<td>1.982410</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>1.0</td>
<td>0.777172</td>
<td>3.249080</td>
<td>6.713190</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>0.0</td>
<td>0.712683</td>
<td>0.361166</td>
<td>1.254500</td>
</tr>
<tr>
<td>0</td>
<td>2</td>
<td>0.0</td>
<td>$-0.071234$</td>
<td>0.673832</td>
<td>0.634534</td>
</tr>
<tr>
<td>0</td>
<td>3</td>
<td>0.0</td>
<td>0.012203</td>
<td>$-0.166867$</td>
<td>0.691510</td>
</tr>
<tr>
<td>1</td>
<td>2</td>
<td>0.0</td>
<td>1.016060</td>
<td>1.045050</td>
<td>4.058170</td>
</tr>
<tr>
<td>2</td>
<td>3</td>
<td>0.0</td>
<td>1.254770</td>
<td>1.967090</td>
<td>8.498830</td>
</tr>
<tr>
<td rowspan="5">DCl</td>
<td>0</td>
<td>0</td>
<td>1.0</td>
<td>0.108159</td>
<td>0.377024</td>
<td>0.146278</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1.0</td>
<td>0.327420</td>
<td>1.211693</td>
<td>0.987922</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>0.0</td>
<td>0.602222</td>
<td>0.217985</td>
<td>0.727798</td>
</tr>
<tr>
<td>0</td>
<td>2</td>
<td>0.0</td>
<td>$-0.050963$</td>
<td>0.490239</td>
<td>0.326599</td>
</tr>
<tr>
<td>0</td>
<td>3</td>
<td>0.0</td>
<td>0.007398</td>
<td>$-0.102399$</td>
<td>0.450480</td>
</tr>
<tr>
<td colspan="7">$\omega_{c}=2991.8183$, $k_{3}=-299.0935$, $k_{4}=39.0356$, $k_{5}=-3.88475$,<br>$k_{6}=0.27635$, $k_{7}=-0.01859$, $k_{8}=0.00125$, $B_{e}=10.593553\ \mathrm{cm}^{-1}$.</td>
</tr>
</tbody>
</table>

where
$$
\begin{aligned}
H_{vv'^{(1)}}= & \langle v'|H_{ROT}|v\rangle=B_{e}J(J+1) \times \\
& \sum_{k=1}R_{k}\sum_{n,m=0}a_{vn}a_{v'm}\langle m|q^{k}|n\rangle,
\end{aligned}\tag{16}
$$
from which $b_{vn}^{J}$ is obtained after appropriate normalization.⁹) Another method to obtain the coefficients $b_{vn}^{J}$ is the direct diagonalization of each vibration-rotation submatrix. The coefficients are directly obtained by solving the $J$-submatrices.¹⁰) The above methods have been applied to evaluate the coefficients $b_{vn}^{J}$ for the CO and HCl molecules. The coefficients $b_{0n}^{J}$ and $b_{1n}^{J}$ calculated for the $J$=0, 10, 20, and 30 levels of the HCl molecule are listed in Table 5. Apparently, the perturbation technique breaks down about $J$=10. The coefficients obtained by the direct numerical diagonalization method are used in the present investigation. No significant discrepancies

<table>
<caption>Table 5. Radial part of vibration-rotation wave functions for HCl<br>The Coefficients $b_{vn}^{J}$'s are given (Eq. 8). $D$: Direct Method. $P$: Perturbation Method.</caption>
<tbody>
<tr>
<td>$v=0$</td>
<td>$n=$</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>10</td>
<td>11</td>
<td>12</td>
</tr>
<tr>
<td colspan="2">$J=0$</td>
<td>0.994</td>
<td>0.105</td>
<td>0.010</td>
<td>0.029</td>
<td>0.007</td>
<td>0.001</td>
<td>0.002</td>
<td>0.001</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2">$J=10$</td>
<td>$D$</td>
<td>0.988</td>
<td>0.150</td>
<td>0.020</td>
<td>0.031</td>
<td>0.009</td>
<td>0.002</td>
<td>0.002</td>
<td>0.001</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$P$</td>
<td>0.988</td>
<td>0.150</td>
<td>0.018</td>
<td>0.030</td>
<td>0.009</td>
<td>0.002</td>
<td>0.002</td>
<td>0.001</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2">$J=20$</td>
<td>$D$</td>
<td>0.960</td>
<td>0.270</td>
<td>0.062</td>
<td>0.040</td>
<td>0.018</td>
<td>0.006</td>
<td>0.003</td>
<td>0.002</td>
<td>0.001</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$P$</td>
<td>0.960</td>
<td>0.274</td>
<td>0.041</td>
<td>0.032</td>
<td>0.017</td>
<td>0.004</td>
<td>0.002</td>
<td>0.001</td>
<td>0.000</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2">$J=30$</td>
<td>$D$</td>
<td>0.880</td>
<td>0.435</td>
<td>0.166</td>
<td>0.081</td>
<td>0.042</td>
<td>0.020</td>
<td>0.010</td>
<td>0.005</td>
<td>0.003</td>
<td>0.001</td>
<td>0.001</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$P$</td>
<td>0.886</td>
<td>0.456</td>
<td>0.076</td>
<td>0.035</td>
<td>0.027</td>
<td>0.007</td>
<td>0.003</td>
<td>0.002</td>
<td>0.001</td>
<td>0.000</td>
<td>0.000</td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">$v=1$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="2">$J=0$</td>
<td>$-0.105$</td>
<td>0.949</td>
<td>0.284</td>
<td>0.058</td>
<td>0.065</td>
<td>0.028</td>
<td>0.008</td>
<td>0.006</td>
<td>0.003</td>
<td>0.001</td>
<td>0.001</td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="2">$J=10$</td>
<td>$D$</td>
<td>$-0.159$</td>
<td>0.915</td>
<td>0.350</td>
<td>0.089</td>
<td>0.073</td>
<td>0.037</td>
<td>0.013</td>
<td>0.008</td>
<td>0.004</td>
<td>0.002</td>
<td>0.001</td>
<td>0.001</td>
<td></td>
</tr>
<tr>
<td>$P$</td>
<td>$-0.159$</td>
<td>0.915</td>
<td>0.351</td>
<td>0.086</td>
<td>0.071</td>
<td>0.036</td>
<td>0.012</td>
<td>0.008</td>
<td>0.004</td>
<td>0.002</td>
<td>0.001</td>
<td>0.000</td>
<td></td>
</tr>
<tr>
<td rowspan="2">$J=20$</td>
<td>$D$</td>
<td>$-0.285$</td>
<td>0.797</td>
<td>0.483</td>
<td>0.183</td>
<td>0.107</td>
<td>0.062</td>
<td>0.029</td>
<td>0.015</td>
<td>0.009</td>
<td>0.004</td>
<td>0.002</td>
<td>0.001</td>
<td></td>
</tr>
<tr>
<td>$P$</td>
<td>$-0.280$</td>
<td>0.802</td>
<td>0.497</td>
<td>0.148</td>
<td>0.083</td>
<td>0.052</td>
<td>0.021</td>
<td>0.010</td>
<td>0.006</td>
<td>0.003</td>
<td>0.001</td>
<td>0.001</td>
<td></td>
</tr>
<tr>
<td rowspan="2">$J=30$</td>
<td>$D$</td>
<td>$-0.447$</td>
<td>0.530</td>
<td>0.580</td>
<td>0.344</td>
<td>0.204</td>
<td>0.126</td>
<td>0.073</td>
<td>0.041</td>
<td>0.024</td>
<td>0.013</td>
<td>0.007</td>
<td>0.004</td>
<td>0.002</td>
</tr>
<tr>
<td>$P$</td>
<td>$-0.416$</td>
<td>0.590</td>
<td>0.646</td>
<td>0.216</td>
<td>0.091</td>
<td>0.071</td>
<td>0.031</td>
<td>0.013</td>
<td>0.009</td>
<td>0.004</td>
<td>0.002</td>
<td>0.001</td>
<td>0.001</td>
</tr>
</tbody>
</table>

8) The treatment for the isotopic species was described in I.
9) See Eq. (4) in I. The term with $k$=0 vanishes from orthogonality.
10) The entire vibration-rotation Hamiltonian matrix is factor- ed into a number of submatrices characterized with the quantum number $J$, since no cross terms occur in $H_{ROT}$ with regard to $J$.

have been found for the coefficients of the CO mole- cule, and the both methods yield almost identical results up to $J=30$.

## Results and Discussion
It was reported by Toth et al.⁴) that their analytical method for the CO molecule gave the identical results with those calculated by the numerical method of Young and Eachus.³) We have also checked our method by feeding the $M_{k}$ values given by Young and and Eachus, and obtained the identical results for the transition moments $R_{0}^{1}, R_{0}^{2}$, and $R_{0}^{3}$. The $M_{k}$ values given by Toth et al.⁶) for the HCl molecule have also been tested. Again we can reproduce their calculated results with the exceptions of $C_{0}^{3}$ and $D_{0}^{3}$. This is, however, somewhat expected, since we included high- er order force constants in our potential, and as we reported in I, this effects is prominent in the wave function related with the $v=3$ level : $|3, J\rangle$.

The least-squares adjustment for the coefficients $p_{0}-p_{3}$ has been done for the CO and HCl molecules by using the experimental data in Tables 1 and 2, the results being included in the same tables. $^{11)}$ Table 1 shows that the four parameter dipole moment function can fit the ten experimental data of CO with an exception of $D_{0}^{3}$, to which the contributions of the neglected higher terms in the dipole moment function are large. In the last column of Table 1, indicated as calcd(2), are listed the calculated values when the $p_{3}$ term is omitted from the dipole moment function. This is done to demonstrate the effect of the $p_{3}$ term, and it is easily seen that the $p_{3}$ term contributes signi ficantly to the moments related with the $v=3$ level. The converged values of $p_{0}$ through $p_{3}$ are not very much different from those obtained previously. How- ever, one comment must be made on the value of $p_{0}$.

![](./images/812070718555553794_1.jpg)

Fig. 1. The cubic dipole moment function of CO.
$M(\Delta r)=0.1243-3.0722(\Delta r)+0.1909(\Delta r)^{2}+2.1856(\Delta r)^{3}$
$M(q)=0.1243-0.1465\ q+0.000434\ q^{2}+0.000237\ q^{3}$

The previous calculations were made on the assumption of $p_{0} \equiv \mu_{0}$ , the dipole moment of the ground vibrational state. As seen from Eq. (9) and Tables 3 and 4, this assumption is obviously incorrect, the higher coeffici- ents also contribute to $\mu_{0}$ . Consideration of this fact makes the value of $p_{0}$ about $10 \%$ higher than given previously, since $p_{1}$ has an opposite sign in CO. The dipole moment function around its equilibrium distance $r_{e}$ is plotted in Fig. 1.

In the case of HCl and DCl, we have also used the cubic dipole moment function with four parameters to fit the eighteen independent data listed in Table 2. The agreement between the calculated and experi- mental data is much improved as compared with those previously done. As expected, the discrepancies are rather large for the values of $C_{0}^{3}$ and $D_{0}$ "s to which, again, the larger contributions from the neglected higher terms are expected. The converged values of $p_{k}$ are converted to coefficients $M_{k}$ and are listed in Table 6 along with those obtained by previous work-

<table>
<caption>TABLE 6. THE COEFFICIENTS OF DIPOLE MOMENT FUNCTION, $M_{k}$, OF HCl DETERMINED BY SEVERAL INVESTIGATORS</caption>
<thead>
  <tr>
    <th></th>
    <td colspan="2">Present</td>
    <td colspan="2">Kaiser (Rcf. 6)</td>
    <td>THP</td>
  </tr>
  <tr>
    <th></th>
    <td>( a )</td>
    <td>( b )</td>
    <td>HCl</td>
    <td>DCl</td>
    <td>(Ref. 5)</td>
  </tr>
</thead>
<tbody>
  <tr>
    <th>$M_{0}(D)$</th>
    <td>1.093</td>
    <td>1.094</td>
    <td>1.093₃</td>
    <td>1.092₂</td>
    <td>1.095</td>
  </tr>
  <tr>
    <th>$M_{1}(D/A)$</th>
    <td>0.949</td>
    <td>0.939</td>
    <td>0.925</td>
    <td>0.935</td>
    <td>0.905</td>
  </tr>
  <tr>
    <th>$M_{2}(D/A^{2})$</th>
    <td>0.034</td>
    <td>--0.087</td>
    <td>0.08</td>
    <td>0.07</td>
    <td>--0.066</td>
  </tr>
  <tr>
    <th>$M_{3}(D/A^{3})$</th>
    <td>--0.78</td>
    <td>--0.55</td>
    <td>--0.64</td>
    <td>--0.63</td>
    <td>--0.73</td>
  </tr>
  <tr>
    <th>$M_{4}(D/A^{4})$</th>
    <td>—</td>
    <td>—</td>
    <td>--0.39</td>
    <td>--0.32</td>
    <td>—</td>
  </tr>
</tbody>
</table>

ers. There is a discrepancy in the previous works as to the sign of $M_{2}$ ; Toth et al. $^{5)}$ gave the value of $-0.066 D / A^{2}$ to $M_{2}$ , whereas Kaiser $^{6)}$ gave 0.08 and $0.07 D / A^{2}$ respectively for HCl and DCl. As we started the least squares procedure with $M_{0}=1.095$  $D, M_{1}=1.0 D / A, M_{2}=M_{3}=0$ , we have obtained a converged set, Set(a), given in the first column of Table6. However, if we started from the values given in Ref. 5, we obtain the second converged set, Set(b), in the second column. The calculated dipole and tran- sition moments as well as the Herman-Wallis factors are given respectively in Columns 3 and 4 in Table 2. Overall fit of the calculated results with the experiment is better in Set (a), which seems to be a natural choice. In order to draw firmer conclusion, however, more ex- perimental data are necessary, because most disagree- ments between the calcd(b) and experimental values occur in the constants to which the higher terms in the dipole moment function which are neglected in the present study may well contribute significantly. The present calculation is performed within the framework of the Born-Oppenheimer approximation, although the deviations from the Born-Oppenheimer behavior are detected in Kaiser's precise measurement of dipole moments for HCl and DCl, this effect is too small for the separate determination of dipole moment functions of both species. In addition, more complex treatment is necessary for the potential functions. $^{12)}$ The present

11) The value $p_{0}$ is taken as positive in the present calculation, since only the relative signs among the coefficients $p_{k}(M_{k})$ have physical significance.

12) P. R. Bunker, J. Mol. Spectry., 35, 306 (1970).

calculation gives the somewhat averaged results for $p_k$'s.

Finally, the dipole moment function for HCl, Set (a), is plotted against the internuclear distance in Fig. 2. Figure 3 is also the plot of the same function close to the equilibrium distance in an enlarged scale. The posi- tions of the average internuclear distances in the $v=0$,1, and 2 levels: $\langle\bar{r}\rangle_{0},\langle\bar{r}\rangle_{1}$, and $\langle\bar{r}\rangle_{2}$, and the dipole moments of $\mu_{0}, \mu_{1}$, and $\mu_{2}$ are indicated by arrows. Since in the linear dipole moment function,

![](./images/812070718555553794_2.jpg)

Fig. 2. The cubic dipole moment function of HCl, Set (a).
$M(\Delta r)=1.093+0.949(\Delta r)+0.034(\Delta r)^{2}-0.78(\Delta r)^{3}$
$M(q)=1.093+0.1018\ q+0.00039\ q^{2}-0.00096\ q^{3}$

![](./images/812070718555553794_3.jpg)

Fig. 3. The cubic dipole moment function of HCl, Set (a), around its equilibrium distance: The average internuclear distances, $\langle\bar{r}\rangle_{0},\langle\bar{r}\rangle_{1}$, and $\langle\bar{r}\rangle_{2}$, and dipole moments $\mu_{0}, \mu_{1}$, and $\mu_{2}$ of HCl are indicated by arrows.

$$
\mu_{v}=M_{0}+M_{1}(\langle\bar{r}\rangle_{v}-r_{e}), \tag{15}
$$

the mismatch of the arrows shows the effect of quadratic and cubic terms.

The author wishes to thank Prof. Takehiko Shimano- uchi for his encouragement and helpful discussion throughout this study.