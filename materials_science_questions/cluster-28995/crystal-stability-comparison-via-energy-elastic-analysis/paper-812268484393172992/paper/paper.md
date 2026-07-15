JOURNAL OF THE PHYSICAL SOCIETY OF JAPAN, Vol. 45, No. 4, OCTOBER, 1978

# On the Possible Effect of the Vacancy Concentration on the Correlation Factor for Tracer Diffusion via Vacancy Mechanism

Masahiro KOIWA

The Research Institute for Iron, Steel and Other Metals,
Tohoku University, Sendai 980

(Received June 9, 1978)

The effect of the vacancy concentration on the correlation factor has been investigated quantitatively. For a given vacancy concentration $C_{\mathrm{v}}$, the number of correlated jumps of a vacancy, $n_{\mathrm{c}}$, can be defined, and this number is used for the calculation of the correlation factor. The deviation of the correlation factor from the value corresponding to an infinitely dilute vacancy concentration is less than $1\%$ for $C_{\mathrm{v}}=10^{-3}$ and less than $0.2\%$ for $C_{\mathrm{v}}=10^{-4}$. For usual experimental conditions, the correlation factor may be regarded as temperature independent.

## §1. Introduction

It is known that a vacancy mechanism is a dominant process of diffusion in a number of crystalline solids. The movement of atoms via the vacancy mechanism is not random so that the expression for the diffusion coefficient contains the correlation factor, $f$. Various methods for calculating the correlation factor have been proposed, as reviewed by Le Claire. $^{1)}$ Compaan and Haven $^{2),3)}$ first calculated the values of $f$ for various lattices to a considerable accuracy, while Montet $^{2)}$ derived more accurate values for cubic lattices; the accuracy of theoretical values is far beyond those attained experimentally. All the previous calculations, however, have been made on the assumption that the vacancy concentration is sufficiently small so that a tracer atom which exchanges with a vacancy will not make any exchange with a different vacancy until the initial vacancy is far from the tracer.

Mullen $^{5)}$ and Le Claire $^{1)}$ pointed out a possibility that a sufficiently large vacancy concentration would shift values of $f$ nearer to unity, and the correlation factor may be dependent on temperature through a change in vacancy concentration. The aim of the present paper is firstly to examine the point quantitatively.

The evaluation of the average cosine of an angle between successive jumps of a tracer atom, $\langle\cos\theta\rangle$, which determines the value of the correlation factor, has been mostly made by the matrix method. The value of $\langle\cos\theta\rangle$ is dependent on the size of the matrix. In the course of the random walk calculation reported in a previous paper $^{6)}$ (hereafter referred to as I), quantities required for the evaluation of $\langle\cos\theta\rangle$ have been calculated for various sizes of the matrix. Thus, we shall examine the convergent trend of $\langle\cos\theta\rangle$ as a function of the matrix size for the f.c.c., b.c.c. and diamond lattices.

## §2. Correlation Factor and Average Cosine

In order to highlight possible effects of vacancy concentration, it seems appropriate to describe briefly the derivation* of the correlation factor, and the procedure of calculating the average cosine, $\langle\cos\theta\rangle$.

### 2.1 Correlation factor

The diffusion constant, $D$, of a tracer is defined as $^{5)}$

$$
D=\langle X^{2}\rangle/2\tau, \tag{1}
$$

where $\langle X^{2}\rangle$ is the mean square displacement of the tracer atom in the $x$ direction after a time $\tau$. If $x_{i}$ represents the projection of the

---
* In a previous paper, $^{7)}$ the author has presented a modified derivation of the correlation factor, in which the number of exchanges made by a particular atom-vacancy pair is explicitly taken into account. In the present paper, however, we will adopt the traditional derivation, since the two derivations are equivalent.

$i$th tracer jump, along the $x$ axis, then

$$
D=\frac{1}{2 \tau}\left\langle\left(\sum_{i=1}^{n} x_{i}\right)^{2}\right\rangle. \tag{2}
$$

The mean square displacement $\langle X^{2}\rangle$ can be rewritten as

$$
\begin{aligned}
\left\langle X^{2}\right\rangle= & \sum_{i=1}^{n}\left\langle x_{i}^{2}\right\rangle+2\left\langle x_{1} x_{2}+x_{1} x_{3}+\cdots+x_{1} x_{n}\right\rangle \\
& +2\left\langle x_{2} x_{3}+\cdots+x_{2} x_{n}\right\rangle+\cdots 2\left\langle x_{n-1} x_{n}\right\rangle.
\end{aligned} \tag{3}
$$

For uncorrelated diffusion, *e.g.* diffusion of vacancies themselves, all the cross terms vanish to yield

$$
\left\langle X^{2}\right\rangle_{\mathrm{v}}=\sum_{i=1}^{n}\left\langle x_{i}^{2}\right\rangle, \tag{4}
$$

and we shall denote the diffusion coefficient by $D_{\mathrm{v}}$. For diffusion of the tracer atom via the vacancy mechanism, the cross terms do not vanish. The diffusion constant $D$ in this case may be written as

$$
D=f D_{\mathrm{v}}, \tag{5}
$$

where $f$ is the correlation factor.

It has been shown (see, for example, ref. 1) that

$$
\left\langle x_{i} x_{i+j}\right\rangle=a^{2} t_{j}, \tag{6}
$$

and

$$
t_{j}=\left(t_{1}\right)^{j}, \tag{7}
$$

where $a$ is the unit jump distance in the $x$ direction and $t_{1}=p_{+}-p_{-} ; p_{+}$is the probability that the $x$ component of the second jump of the atom is in the same direction and $p_{-}$the probability that it is in the opposite direction. By utilizing the relations (6) and (7), the correlation factor can be written as $^{8)}$

$$
f=\frac{1+t_{1}}{1-t_{1}}\left[1-\frac{2 t_{1}}{n} \frac{1-t_{1}^{n}}{1-t_{1}^{2}}\right] \tag{8}
$$

and for an infinite $n$, we obtain

$$
f_{\infty}=\frac{1+t_{1}}{1-t_{1}}. \tag{9}
$$

Here $t_{1}$ is equivalent to the average cosine $\langle\cos \theta\rangle$. The expression (9) is valid for the case of an infinitely dilute concentration of vacancies. We shall refer to the eq. (8) as the rigorous- and to (9) as the approximate formulae.

### 2.2 Average cosine
By knowing the value of the average cosine, $\langle\cos \theta\rangle$, or the quantity $t_{1}$, one can immediately obtain the value of the correlation factor by eq. (8) or (9). The method of calculating $t_{1}$ has been discussed in detail by Le Claire, $^{1)}$ and will be described here briefly.

To calculate $t_{1}$, it is necessary to evaluate the total probaility, $W(k)$, of the vacancy being on the neighbouring sites $k$ of a particular atom (p) after the first exchange with the relevant vacancy. For the f.c.c. crystal, the lattice sites near the particular atom-vacancy pair may be numbered as shown in Fig. 1, and the values of $W(k)$ should be found for sites $k=0 \sim 4$. Then, the value of $t_{1}$ is given by

$$
t_{1}=\frac{1}{12}[-W(0)-2 W(1)+2 W(3)+W(4)]. \quad(10)
$$

$W(k)$ are calculated as follows. We define $w(k, i)$ as the probability that site $k$ in the crystal is occupied by the vacancy on its $i$th jump, and with the proviso that the second tracer jump has not occurred. The total probability of the vacancy being on site $k$ is

$$
W(k)=\sum_{i=0}^{n} w(k, i). \tag{11}
$$

In matrix form, the change in vacancy distribution by the $i$th vacancy jump, $(i-1) \rightarrow i$, can be written as

$$
\boldsymbol{w}(i)=\boldsymbol{w}(i-1) \cdot \mathbf{A}, \tag{12}
$$

where $\boldsymbol{w}(i)$ is a row matrix with elements $w(k, i)$ of order $M$, for $M$ sites, and $\mathbf{A}$ is the

![](./images/812268484393172992_1.jpg)

Fig. 1. Numbering of lattice sites of the f.c.c. lattice for the calculation of the average cosine. The vacancy is at the origin and the tracer atom at a site in the first coordination shell designated as p. Smaller circles and squares are on the neighbouring (111) planes.

$M \times M$ matrix of which the element $A_{lm}$ is the probability a vacancy on $l$ will at its next jump move to $m$. If we write eq. (11) in matrix form
$$
\boldsymbol{W}=\sum_{i=0}^{n} \boldsymbol{w}(i), \tag{13}
$$
and then from eq. (12) we obtain
$$
\boldsymbol{W}=\boldsymbol{w}(0) \cdot\left(\mathbf{I}+\mathbf{A}+\mathbf{A}^{2}+\cdots+\mathbf{A}^{n}\right), \tag{14}
$$
which, for an infinite $n$, reduces to
$$
\boldsymbol{W}=\boldsymbol{w}(0) \cdot(\mathbf{I}-\mathbf{A})^{-1}. \tag{15}
$$

The components of $\boldsymbol{w}(0)$ represent the initial vacancy distribution and are all zero except for the site 0 (the origin) occupied by the vacancy immediately after the initial tracer jump.

For a finite vacancy concentration, the number of jumps of the initial vacancy to be taken into account for the calculation of $\langle\cos$ $\theta\rangle$ is not infinite; different vacancies may come in to exchange with the relevant tracer atom. In order to evaluate the correlation effect correctly, therefore, the summation in eq. (14) should be stopped at a certain value of $n$. Such values of $n$ to be determined for each vacancy concentration will be designated as $n_{\mathrm{c}}$, the subscript $\mathrm{c}$ implying the duration of correlation.

The same restriction should also be given to eqs. (3) and (8). The number of the tracer jumps via a particular vacancy cannot be larger than the number of jumps made by the relevant vacancy.

## §3. Correlation Factor and Vacancy Concentration

### 3.1 The number of vacancy jumps in the duration of correlation

Here we shall calculate the number, $n_{\mathrm{c}}$, of vacancy jumps in the duration of correlation for given vacancy concentrations. Consider a crystal lattice of unit volume which consists of $N_{\mathrm{T}}$ lattice sites and contains $N_{\mathrm{V}}$ vacancies; the vacancy concentration, $C_{\mathrm{v}}$, in atomic fraction is given by
$$
C_{\mathrm{v}}=N_{\mathrm{V}} / N_{\mathrm{T}}.
$$

As was done in a previous paper, $^{9)}$ we define a polyhedron about each vacancy with $N_{\mathrm{T}} / N_{\mathrm{V}}$ lattice sites. The polyhedron is approximated by a sphere of equivalent volume. Now we assume that the vacancy at the origin in a sphere has just finished the first exchange with a neighbouring tracer atom. The duration of the correlation between the pair of the tracer- vacancy may be considered to last as long as the vacancy remains inside the relevant sphere; once the vacancy wanders out of the sphere,

**Table I. Summary of results.**

#### a) The f.c.c. lattice
<table>
  <thead>
    <tr>
      <th>Sphere size</th>
      <th>$N_{\mathrm{p}}$</th>
      <th>$C_{\mathrm{v}}$</th>
      <th>$n_{\mathrm{c}}$</th>
      <th>$-t_{1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>19</td>
      <td>$5.26×10^{-2}$</td>
      <td>3.368</td>
      <td>—</td>
    </tr>
    <tr>
      <td>5</td>
      <td>79</td>
      <td>$1.27×10^{-2}$</td>
      <td>7.420</td>
      <td>.1227626</td>
    </tr>
    <tr>
      <td>11</td>
      <td>201</td>
      <td>$4.97×10^{-3}$</td>
      <td>12.855</td>
      <td>.1226948</td>
    </tr>
    <tr>
      <td>13</td>
      <td>249</td>
      <td>$4.02×10^{-3}$</td>
      <td>14.329</td>
      <td>.1226804</td>
    </tr>
    <tr>
      <td>26</td>
      <td>627</td>
      <td>$1.59×10^{-3}$</td>
      <td>25.528</td>
      <td>.1226797</td>
    </tr>
    <tr>
      <td>39</td>
      <td>1055</td>
      <td>$9.5 ×10^{-4}$</td>
      <td>35.426</td>
      <td>.1226797</td>
    </tr>
    <tr>
      <td>48</td>
      <td>1289</td>
      <td>$7.8 ×10^{-4}$</td>
      <td>39.869</td>
      <td>.1226801</td>
    </tr>
    <tr>
      <td>67</td>
      <td>1985</td>
      <td>$5.0 ×10^{-4}$</td>
      <td>52.618</td>
      <td>.1226800</td>
    </tr>
    <tr>
      <td>80</td>
      <td>2347</td>
      <td>$4.3 ×10^{-4}$</td>
      <td>58.604</td>
      <td>.1226801</td>
    </tr>
    <tr>
      <td>90</td>
      <td>2731</td>
      <td>$3.7 ×10^{-4}$</td>
      <td>64.549</td>
      <td>.1226800</td>
    </tr>
  </tbody>
</table>

#### b) The b.c.c. lattice
<table>
  <thead>
    <tr>
      <th>Sphere size</th>
      <th>$N_{\mathrm{p}}$</th>
      <th>$C_{\mathrm{v}}$</th>
      <th>$n_{\mathrm{c}}$</th>
      <th>$-t_{1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5</td>
      <td>59</td>
      <td>$1.69×10^{-2}$</td>
      <td>6.646</td>
      <td>.1579618</td>
    </tr>
    <tr>
      <td>11</td>
      <td>169</td>
      <td>$5.92×10^{-3}$</td>
      <td>12.269</td>
      <td>.1579912</td>
    </tr>
    <tr>
      <td>15</td>
      <td>259</td>
      <td>$3.86×10^{-3}$</td>
      <td>15.469</td>
      <td>.1579171</td>
    </tr>
    <tr>
      <td>25</td>
      <td>531</td>
      <td>$1.88×10^{-3}$</td>
      <td>24.365</td>
      <td>.1579446</td>
    </tr>
    <tr>
      <td>40</td>
      <td>941</td>
      <td>$1.06×10^{-3}$</td>
      <td>34.932</td>
      <td>.1579487</td>
    </tr>
    <tr>
      <td>53</td>
      <td>1291</td>
      <td>$7.7 ×10^{-4}$</td>
      <td>42.135</td>
      <td>.1579474</td>
    </tr>
    <tr>
      <td>62</td>
      <td>1591</td>
      <td>$6.3 ×10^{-4}$</td>
      <td>48.073</td>
      <td>.1579480</td>
    </tr>
    <tr>
      <td>71</td>
      <td>1837</td>
      <td>$5.4 ×10^{-4}$</td>
      <td>52.920</td>
      <td>.1579469</td>
    </tr>
    <tr>
      <td>80</td>
      <td>2133</td>
      <td>$4.7 ×10^{-4}$</td>
      <td>58.235</td>
      <td>.1579475</td>
    </tr>
    <tr>
      <td>90</td>
      <td>2445</td>
      <td>$4.1 ×10^{-4}$</td>
      <td>63.400</td>
      <td>.1579474</td>
    </tr>
  </tbody>
</table>

#### c) The diamond lattice
<table>
  <thead>
    <tr>
      <th>Sphere size</th>
      <th>$N_{\mathrm{p}}$</th>
      <th>$C_{\mathrm{v}}$</th>
      <th>$n_{\mathrm{c}}$</th>
      <th>$-t_{1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>17</td>
      <td>$5.88×10^{-2}$</td>
      <td>4.556</td>
      <td rowspan="10">1/3</td>
    </tr>
    <tr>
      <td>5</td>
      <td>47</td>
      <td>$2.13×10^{-2}$</td>
      <td>8.593</td>
    </tr>
    <tr>
      <td>13</td>
      <td>159</td>
      <td>$6.29×10^{-3}$</td>
      <td>17.946</td>
    </tr>
    <tr>
      <td>39</td>
      <td>525</td>
      <td>$1.90×10^{-3}$</td>
      <td>37.009</td>
    </tr>
    <tr>
      <td>49</td>
      <td>729</td>
      <td>$1.37×10^{-3}$</td>
      <td>46.114</td>
    </tr>
    <tr>
      <td>56</td>
      <td>849</td>
      <td>$1.18×10^{-3}$</td>
      <td>50.519</td>
    </tr>
    <tr>
      <td>63</td>
      <td>943</td>
      <td>$1.06×10^{-3}$</td>
      <td>53.823</td>
    </tr>
    <tr>
      <td>67</td>
      <td>1015</td>
      <td>$9.8 ×10^{-4}$</td>
      <td>56.101</td>
    </tr>
    <tr>
      <td>79</td>
      <td>1231</td>
      <td>$8.1 ×10^{-4}$</td>
      <td>64.002</td>
    </tr>
    <tr>
      <td>90</td>
      <td>1419</td>
      <td>$7.0 ×10^{-4}$</td>
      <td>70.146</td>
    </tr>
  </tbody>
</table>

$N_{\mathrm{p}}$: the number of lattice sites in the sphere.
$C_{\mathrm{v}}$: the vacancy concentration in atomic fraction.
$n_{\mathrm{c}}$: the number of vacancy jumps in the duration of correlation.
$t_{1} \equiv\langle\cos \theta\rangle$: the average cosine.

different vacancies have equal chances to come in and to exchange with the tracer atom. Therefore, it is reasonable to take $n_{\mathrm{c}}$ being equal to the mean number of jumps required for the vacancy to escape out of the sphere. The latter has been calculated in the previous paper I; the table shows the value of $n_{\mathrm{c}}$ and several other quantities for various sizes of spheres. The sphere size is expressed by the integral number $L$, which means that the sphere consists of the first to the $L$ th coordination shell. Note that the lattice sites at the same distance from the origin are regarded as belonging to different shells if they are dif- ferent in symmetry; for example, in the f.c.c. lattice, a site at $(a / 2)(3,3,0)$ is of the 9th shell while a site at $(a / 2)(4,1,1)$ of the 10th shell, where $a$ is the lattice constant.

For the case of the f.c.c. lattice, the number of correlated jumps, $n_{\mathrm{c}}$, is approximately expressed as
$$
n_{\mathrm{c}} \simeq 0.33 C_{\mathrm{v}}^{-2 / 3}. \tag{16}
$$

### 3.2 The effect of vacancy concentration on the magnitude of the correlation factor

In what follows we shall mainly concern with the case of the f.c.c. crystal. Consider first the effect of the vacancy concentrations through eq. (8). For vacancy concentrations $C_{\mathrm{v}}<10^{-2}$, the number of correlated jumps $n_{\mathrm{c}}$ is larger than 7 (see table), so that the term $t_{1}^{n}$ in eq. (8) can be neglected since $t_{1} \simeq$ $-0.1227 .{ }^{1)}$ Hence, by substituting eq. (16), the correlation factor (8) can be written as
$$
f \simeq f_{\infty}\left[1+0.755 C_{\mathrm{v}}^{2 / 3}\right]. \tag{17}
$$

Next, we will calculate the value of $t_{1}$ or $\langle\cos \theta\rangle$ with eqs. (10) and (14) for various vacancy concentrations; $f_{\infty}$ is dependent on the value of $t_{1}$. In the previous paper I, we have constructed the jump probability matrix, $\boldsymbol{K}$, for the rate equation describing the behaviour of the random walker. The matrix $\boldsymbol{A}$ in eq. (14) is related to $\boldsymbol{K}$ by
$$
\mathbf{A}=\mathbf{I}+\frac{1}{12 k} \mathbf{K}, \tag{18}
$$
where $k$ is the jump frequency of a vacancy to a neighbouring site. For the present calculation we have used the matrix of the size $91 \times 91$, corresponding to the sphere size 90 which contains total 2731 lattice sites. The values of $t_{1}$ is shown, as a function of $n$, in Fig. 2, in which the result for the sphere size $5(6 \times 6$ matrix) with 79 lattice sites is also shown for comparison. The faster convergence of the value of $\langle\cos \theta\rangle$ for sphere size 5 is due to the eariler loss of the vacancy from the sphere. For a first few jumps, the vacancy is not lost at all for both the spheres so that the values of $\langle\cos \theta\rangle$ coincide each other. The arrows indicate the mean number of jumps for the escape of the vacancy; the probability of finding the vacancy inside the sphere is approximately $0.37\left(=e^{-1}\right)$ at $n$ indicated by the arrows. Since we know the proper values of $n=n_{\mathrm{c}}$ for each vacancy concentration $C_{\mathrm{v}}$, the value of $t_{1}$ to be used for the calculation of the correlation factor can be found easily.

![](./images/812268484393172992_2.jpg)

Fig. 2. The average cosine, $\langle\cos \theta\rangle$, as a function of the number of vacancy jumps, $n$, for sphere size 90 (matrix size 91) and 5 (6).

The deviation of $f$ from the limiting value for infinite $n$, is shown in Fig. 3 as a function of the vacancy concentration (open circles). Similar calculations were also made for the diamond lattice and indicated by filled circles.

Recently, Benoist, Boucquet and Lafore $^{10)}$ have discussed, by a more sophisticated method with the use of double Laplace-Fourier trans- forms, the influence of the vacancy concentra- tion on the correlation factor through the value of $t_{1}$. Their results for the simple cubic lattice

![](./images/812268484393172992_3.jpg)

Fig. 3. The deviation of the correlation factor from the limiting value for an infinitely dilute vacancy concentration. The deviation associated with the evaluation of the average cosine is shown for the f.c.c. and the diamond lattice; the result for the simple cubic lattice by Benoist et al. $^{10)}$ is also shown for comparison. The broken line shows the difference between the rigorous (eq. (8)) and the approximate (eq. (9)) formulae for the correlation factor.

are also indicated in Fig. 3 (■); their estimation is much smaller than the present ones. Since our estimations for the two lattices, the f.c.c. and the diamond lattices, are not very different, the difference between theirs and ours does not seem to be due to the difference in the structure of the lattices but rather due to the difference in the methods of calculations.

The other effect of the vacancy concentration on the correlation factor given by eq. (17) which originates from eq. (8) is shown by the dotted line in Fig. 3. This effect, which has not been considered by Benoist et al., $^{10)}$ is much larger than that through the value of $t_{1}$; the total magnitude of the effect is given by the sum of the two.

In any event the temperature dependence of the correlation factor through the change in the vacancy concentration is negligible for usual diffusion experiments where the vacancy concentration is around $10^{-4}$ or lower.

## §4. On the Convergence of the Average Cosine as a Function of Matrix Size

The values of $W(k)$, used for calculations of $t_{1}$ by eq. (10) are usually computed by the matrix method as described above. For practical calculations, explicit account of vacancy trajectories is taken only over a limited region of the crystal, the volume of which determines the size of the matrix $\boldsymbol{A}$; the more extended the volume, the more accurate the calculation of $t_{1}$ and so $f$.

In the previous paper I, we have calculated the inverted matrix of the jump probability matrix $\boldsymbol{K}$ of various sizes for the f.c.c., the b.c.c., and the diamond lattices. Since, from eqs. (15) and (18),
$$
\boldsymbol{K}^{-1}=\frac{1}{12 k}[\mathbf{I}-\mathbf{A}]^{-1},
$$
the results of the previous calculations are immediately applicable to the calculation of the correlation factor and to the examination of its convergent trend as a function of the matrix size. The last column of the table gives the value of $-t_{1}$.

Figure 4 shows the trend in detail for the f.c.c. lattice. As seen in the figure the values show an oscillatory trend which damps away with the increase in the sphere size (≡the matrix size $-1$). As stated before, some shells are at the same distance from the origin; the arrows indicate such shells. The filled circles in the figure might better be neglected, since for such cases we regard some lattice sites as inside the sphere and the others as outside even they are at the same distance from the origin; the broken lines represent the trend more properly. The oscillatory trend still remains after the above screening, and is believed to be associated with the fact that the increase in the sphere size does not necessarily increase equally the probability of occupation of neighbouring sites of the tracer atom. It is interesting to see that $-t_{1}$ for the diamond lattice is $1/3$ independent of the sphere size; even the smallest size of the matrix of $3 \times 3$

![](./images/812268484393172992_4.jpg)

Fig. 4. The average cosine for the f.c.c. lattice as a function of the sphere size. The matrix size is larger by 1 than the sphere size.

yields the correct value. For the b.c.c. lattice, first four figures of $t_{1}$ are established at smaller matrix sizes, but the oscillatory trend seems to last longer than for the f.c.c. lattice.

In summarizing, the value of $t_{1}$ shows generally an oscillatory trend and approaches a constant value, and the rapidity of the con- vergence is different for each crystal lattice.

## §5. Conclusions and Summary
The effect of the vacancy concentration on the correlation factor has been considered in detail from the two points of view. The formula for the correlation factor conventionally used, eq. (9), is approximate in that the summation of cross terms in eq. (3) have been made to infinite $n$. The rigorous formula is given by eq. (8). The difference in numerical values by eqs. (8) and (9) is dependent on the vacancy concentration. The value of the average cosine or $t_{1}$ (eq. (10)) should also vary with the vacancy concentration.

By estimating the number of correlated jumps of vacancies for various concentrations, the deviation of the correlation factor from the value used conventionally has been estimated from the above two viewpoints. It is concluded that the correlation factor is virtually independent of the vacancy concentrations if $C_{v} \lesssim 10^{-4}$, and so is independent of temperature.

## Acknowledgements
This work was initiated during the author's stay at Chalk River Nuclear Laboratories, AECL. The author wishes to express his thanks to Professor G. V. Kidson of Brock University for stimulating discussion. The author also wishes to thank the Japan Society for Pro- motion of Science and the National Research Council of Canada for support of his stay in Chalk River.

## References
1) A. D. Le Claire: *Physical Chemistry*, ed. W. Jost (Academic Press, 1970) Vol. 10, p. 261.
2) K. Compaan and Y. Haven: Trans. Faraday Soc. **52** (1956) 786.
3) K. Compaan and Y. Haven: Trans. Faraday Soc. **54** (1958) 1498.
4) G. L. Montet: Phys. Rev. B7 (1973) 650.
5) J. G. Mullen: Phys. Rev. **124** (1961) 1723.
6) M. Koiwa: Phil. Mag. **36** (1977) 893.
7) M. Koiwa: J. Phys. Soc. Japan **45** (1978) 781.
8) G. V. Kidson: Canad. J. Phys. **53** (1975) 1054.
9) M. Koiwa: Acta metallurgica **22** (1974) 1259.
10) P. Benoist, J.-L. Bocquet and P. Lafore: Acta metallurgica **25** (1977) 265.