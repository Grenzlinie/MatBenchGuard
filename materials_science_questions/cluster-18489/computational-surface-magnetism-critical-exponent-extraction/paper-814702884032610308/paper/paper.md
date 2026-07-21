VERIFICATION OF THE THREE-CLUSTER MOLECULAR-FIELD
RENORMALIZATION GROUP APPROACH
FOR THE ISING MODEL

G. KAMIENIARZ AND G. MUSIAŁ

Computational Physics Division, Institute of Physics,
A. Mickiewicz University, ul. Umultowska 85, 61-614 Poznań, Poland

(Received 25 January 2002)

Abstract: A transfer matrix approach has been worked out to test the predictions of the three-step molecular-field renormalization group (MFRG) for square Ising clusters with linear size up to $L = 11$. The convergence of the finite-size critical couplings and the critical exponents towards the exact values is shown.

The molecular field approximation has become a valuable tool for a qualitative understanding of the phase diagrams of three-dimensional systems and for obtaining quantitative estimates of non-singular thermodynamic properties. Its most serious drawback is the prediction of classical critical exponents. A successful attempt to improve this deficiency [1-3] is the idea of MFRG which will be illustrated for the ferromagnetic nearest-neighbour Ising model on the square lattice, inasmuch as for this case the exact results are known.

Consider three square clusters consisting of $N = L^2$, $N' = L'^2$ and $N'' = L''^2$ sites, where $L$, $L'$ and $L''$ denote the linear size of a given cluster, with $L> L' > L''$. In the spirit of the mean-field theory, the border spins of the clusters are subject to the symmetry-breaking (effective) field $b$, $b'$ and $b''$, respectively. For the cluster of the size $L$, the Hamiltonian in the presence of magnetic field can be written as

$$
-\beta H \equiv \mathcal{H}_L = K \sum_{\langle i,j \rangle} S_i S_j + h \sum_{i} S_i + K b \sum_{j} n_j S_j,
$$

where $K$ stands for the coupling $\beta J$ and the parameters $h$ and $b$ denote the external and the effective field, respectively. The first sum runs over the nearest-neighbour pairs, the second over all the cluster sites and the third over the edge spins only, so that the factor $n_j$ counts the number of effective fields ($n_j = 1$ except for the corner spins where $n_j = 2$).

In the standard MFA, the self-consistency condition for the magnetization per site

$$
m(K,b,h)=b \tag{1}
$$

leads to the critical coupling $K_c$ in the limit $b = 0$.

In MFRG, the scaling behaviour of the cluster magnetisations $m$ and $m'$ under the length-rescaling factor $l_1=(N/N')^{1/d}$ is imposed [2]

$$
m'(K',h',b')=l_{1}^{d-y_{h}}m(K,h,b) \tag{2}
$$

together with the ansatz that the effective field scales like the surface field $b' = l_{1}^{y_{hs}}b$. Similar equation we have for magnetisations $m'$ and $m''$:

$$
m''(K'',h'',b'')=l_{2}^{d-y_{h}}m'(K',h',b') \tag{3}
$$

with $b''=l_{2}^{y_{hs}}b'$ and $l_{2}=(N'/N'')^{1/d}$.

A mapping $(K, h, b) \to (K', h', b')$ can be found from Eq. (2), setting $h = h' = 0$ and expanding both sites to the leading order in $b$ and $b'$. Analogously, from Eq. (3) we can find a mapping $(K',h',\ b')\to(K'',h'',b'')$. Combining Eqs (2) and (3), the set of two equations of the form

$$
\Theta'(K^{*})=l_{1}^{d-(y_{h}+y_{hs})}\Theta(K^{*}) \tag{4}
$$

and

$$
\Theta''(K^{*})=l_{2}^{d-(y_{h}+y_{hs})}\Theta'(K^{*}) \tag{5}
$$

follows for the fixed point, where

$$
\Theta(K)=\left\langle\frac{1}{N}\sum_{i}S_{i}\sum_{j}n_{j}S_{j}\right\rangle \tag{6}
$$

denotes a two-point correlation function in the limit $h = b = 0$. Once the fixed point $K^{*}$ is calculated, the thermal and the bulk and surface magnetic exponents $y_{t}, y_{h}$ and $y_{hs}$. can not uniquely be determined. From the set of Eqs (4) and (5) only $y_{h}+y_{hs}$ can be determined, whereas for critical exponents slightly different results can be obtained from the corresponding scaling fields for the mapping $(K, h, b) \to (K', h', b')$ and for $(K', h', b') \to (K'',h'',\ b'')$.

This method of computation of non-classical critical properties of lattice models is attractive due to its efficiency and simplicity and is easily applicable [4-9] to bulk critical phenomena as well as to surface, random and dynamic effects. Initially [1] the estimates of the non-classical critical exponents appeared to be inferior to the estimates of critical couplings. In a number of publications some attempts to improve this shortcoming have been undertaken by a redefinition of the rescaling factor [10], or an idea of effective fields with correlations [11], However, the validity of the basic assumptions (2) and (3) have not been confirmed so far as well as the convergence of the MFRG results has not been systematically checked by using sequences of large cluster sizes. The main difficulty arises from summation over all the $2^{L \times L}$ Ising configurations in (6), blowing up quickly with increasing $L$. With some computational effort the renormalization-group calculations have been performed up to L = 6 [4], Considering the wide range of the MFRG applications, the test of convergence in the finite-size scaling region $1/L << 1$ seems rather important.

In this paper we report a transfer matrix approach which enables the numerically exact solutions of the set of Eqs (4) and (5) for the Ising clusters up to $L = 11$ sufficient to perform asymptotic analysis of the corresponding finite-size data.

The idea is as follows. Our system consists of a square cluster of size $L$ and contains $L$ x $L$ spins $S = \pm 1$. The spins on the external edges are subject to an effective field $b$. For the $L$ x $L$ cluster and small $h$ and $b$, the partition function $Z_L$ can be expanded in a power series. The thermal expectation values $\Theta(K)$ present in Eqs (4) and (5) can be then evaluated from the ratios of the corresponding coefficients in the expansion of $Z_L$. It appears that

$$
\Theta(K)=Z_{1,1}^{(2)} / Z_{0,0}^{(0)},
$$

where

$$
Z_{m, n}^{(m+n)}=\left(\frac{\delta^{m+n} Z_{L}}{\delta h^{m} \delta b^{n}}\right)_{h, b=0}.
$$

The computations of the partition function $Z_L$ and its expansion is carried out by the powerful transfer matrix technique. If the spins belonging to the $j$-th column of the cluster are denoted as $S_j=(S_{j1}, S_{j2},..., S_{jL})$, the partition function is given by

$$
Z_{L}=\sum_{S_{1}, S_{2}} T_{L}\left(S_{1}, S_{2}\right), \tag{7}
$$

where the global transfer matrix $\mathbf{T}_L$ is defined in the $2^{L}$-dimensional manifold of all the configurations of $L$ spins $S_{jk}(k=1,..., L)$. The matrix $\mathbf{T}_L$ can be factorized into the product

$$
\mathbf{T}_{L}=\mathbf{T}_{0} \mathbf{T}^{L-1} \mathbf{T}_{0},
$$

where $\mathbf{T}_0$ is the diagonal matrix defined by

$$
T_{0}\left(S_{1}, S_{2}\right)=\exp \left(K b \sum_{k=1}^{L} S_{1 k}\right) \delta_{S_{1}, S_{2}}
$$

and $\mathbf{T}$ is a non-diagonal matrix which can be split into the product

$$
\mathbf{T}=\mathbf{T}_{v} \mathbf{T}_{h} \mathbf{T}_{v}
$$

with the diagonal matrix $\mathbf{T}_v$ expressed by

$$
T_{v}\left(S_{i}, S_{j}\right)=\exp \frac{1}{2}\left[K \sum_{k=1}^{L-1} S_{j k} S_{j, k+1}+h \sum_{k=1}^{L} S_{j k}+K b\left(S_{j 1}+S_{j, L}\right)\right] \delta_{S_{i}, S_{j}}.
$$

The corresponding matrix $\mathbf{T}_h$ is non-diagonal but can be expressed as a product of sparse matrices convenient for numerical computations.

Each contribution to the partition function (7) requires a number of successive multiplications of a given vector by T. In order to evaluate the correlations $\mathcal{O}(K)$, we keep track of the powers of $h$ and $b$ during the transfer matrix multiplications up to the second order. We note that the external field dependence is restricted to $\mathrm{T}$, whereas the effective field dependent terms are present in both diagonal matrices. This perturbative scheme is an extension of that in [12] and yields numerical values of the sums $\mathcal{O}(K)$ with an accuracy limited by the rounding effects of double-precision floating point operations.

Using our approach, we have solved the fixed point set of equations (4) and (5) for $K^{*}$ with the accuracy up to 7 decimal places for $3 \leq L \leq 11, L^{\prime}=L-1$ and $L^{\prime \prime}=L-2$. The final results for $K^{*}$ as well as for the critical exponents $y_{t}, y_{h}$ and $y_{h s}$ are given in the corresponding columns of Table 1. The values for $L \leq 5$ coincide [4] with those previously published to all the decimal placed quoted. We have used the mapping $(K, h, b) \rightarrow\left(K^{\prime}, h^{\prime}, b^{\prime}\right)$ for which one obtains slightly better results than for the mapping $\left(K^{\prime}, h^{\prime}, b^{\prime}\right) \rightarrow\left(K^{\prime \prime}, h^{\prime \prime}, b^{\prime \prime}\right)[2]$,

The series given in Table 1 have been analyzed by a number of extrapolation techniques [12, 13], yielding consistent limits for $L \rightarrow \infty$. Finally, the estimates found from the alternating $\varepsilon$-algorithm [13] are given as the extrapolated values in the last row of Table 1. The uncertainties on the last decimal places are written in parentheses.

Table 1. Estimates of the critical couplings $K^{*}$ and the critical exponents for the square clusters with linear size $L, L^{\prime}$ and $L^{\prime \prime}$

<table>
<thead>
  <tr>
    <th>$L$</th>
    <th>$L'$</th>
    <th>$L''$</th>
    <th>$K^{*}$</th>
    <th>$y_{t}$</th>
    <th>$y_{h}$</th>
    <th>$y_{h}/y_{t}$</th>
    <th>$y_{hs}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>3</td>
    <td>2</td>
    <td>1</td>
    <td>0.4127403</td>
    <td>0.81306956</td>
    <td>1.62492403</td>
    <td>1.99850555</td>
    <td>0.49868146</td>
  </tr>
  <tr>
    <td>4</td>
    <td>3</td>
    <td>2</td>
    <td>0.4248751</td>
    <td>0.86063929</td>
    <td>1.67724864</td>
    <td>1.94884043</td>
    <td>0.49307179</td>
  </tr>
  <tr>
    <td>5</td>
    <td>4</td>
    <td>3</td>
    <td>0.4300560</td>
    <td>0.88786003</td>
    <td>1.70821582</td>
    <td>1.92396973</td>
    <td>0.48975233</td>
  </tr>
  <tr>
    <td>6</td>
    <td>5</td>
    <td>4</td>
    <td>0.4329086</td>
    <td>0.90588513</td>
    <td>1.72946381</td>
    <td>1.90914251</td>
    <td>0.48798053</td>
  </tr>
  <tr>
    <td>7</td>
    <td>6</td>
    <td>5</td>
    <td>0.4346880</td>
    <td>0.91881317</td>
    <td>1.74521714</td>
    <td>1.89942547</td>
    <td>0.48703429</td>
  </tr>
  <tr>
    <td>8</td>
    <td>7</td>
    <td>6</td>
    <td>0.4358881</td>
    <td>0.92858181</td>
    <td>1.75748826</td>
    <td>1.89265850</td>
    <td>0.48654439</td>
  </tr>
  <tr>
    <td>9</td>
    <td>8</td>
    <td>7</td>
    <td>0.4367427</td>
    <td>0.93624139</td>
    <td>1.76738213</td>
    <td>1.88774193</td>
    <td>0.48632239</td>
  </tr>
  <tr>
    <td>10</td>
    <td>9</td>
    <td>8</td>
    <td>0.4373767</td>
    <td>0.94241921</td>
    <td>1.77556778</td>
    <td>1.88405304</td>
    <td>0.48626228</td>
  </tr>
  <tr>
    <td>11</td>
    <td>10</td>
    <td>9</td>
    <td>0.4378620</td>
    <td>0.94751286</td>
    <td>1.78247512</td>
    <td>1.88121470</td>
    <td>0.48630340</td>
  </tr>
  <tr>
    <td>$\infty$</td>
    <td></td>
    <td></td>
    <td>0.4406(1)</td>
    <td>0.999(2)</td>
    <td>1.879(2)</td>
    <td>1.867(2)</td>
    <td>0.486(1)</td>
  </tr>
</tbody>
</table>

According to the data in Table 1, the limit $K_{c}$ of the series for the critical couplings $K_{L L}$, * coincides with the exact Ising value 0.4406868 within the quoted error bar. The corresponding series for the thermal exponent $y_{t}$ converges towards the exact values, too. Within MFRG the ratio $y_{h} / y_{t}$ deserves special attention. This quantity is independent of the definition of the rescaling factor [4] and is expected to show the best convergence for $L \rightarrow \infty$. We do not confirm this behaviour, although the limit deviates slightly from 1.875 due to the unsufficient convergence of the magnetic exponent $y_{h}$.

The transfer matrix technique developed here was aimed at testing the convergence of the original MFRG results with increasing size of the square clusters. It can be also used in

the framework of the standard MFA to solve the self-consistent equation (1) by numerical differentiation of the partition function. Moreover, as clusters of $N \approx 100$ sites can be dealt with, the approach can be applied in MFA to some condensed matter physics problems in 3 dimensions with the length $L \sim 4 \div 5$. Our $2d$ results unambiguously show systematic improvement with increasing cluster size. We expect that the standard MFA calculations limited (with some exceptions [1,11], to $L=1$ in $3d$ can be also significantly improved for clusters with $L>1$. MFA provides a feasible approach to complicated problems and is improved in three-dimensional systems. In this interesting area our new approach is directly applicable. For the square Ising model, the MFA self-consistent equation (1) is reduced in the vicinity of the critical point to $K_{c}^{-1}=\Theta(K_{c})$ which can be dealt with our approach.

In conclusion, the transfer matrix approach has been worked out to test the predictions of MFRG for large cluster sizes. Strong numerical evidence is given for the convergence of the finite-size critical couplings and the thermal exponent y, towards the proper Ising limit. The estimated value for the critical exponent $y_{h}=1.879(2)$ only slightly differs from its exact value 1.875. It is not confirmed that the ratio $y_{h} / y_{t}$ yields a good estimate in the limit $L \to \infty$. We have obtained also reasonable estimate for the critical exponent $y_{h s}=0.486(1)$ which is close to its exact value $1 / 2$. We expect that persistent deviations of the extrapolated values of the magnetic exponents $y_{h}$ and $y_{h s}$ from their exact values can be attributed to the unsufficient system sizes $L \leq 11$.

### Acknowledgements

We would like to thank D. Tomecka for her assistance in the numerical computations as well as the Super-computing and Networking Center in Poznań for an access to Cray T3E and J916. A financial support from the Committee for the Scientific Research via grant 8 T1 IF 027 16 is also acknowledged.

### References

[1] J. O. Indekeu, A. Maritan, A. Stella, J. Phys. **A15**, L291 (1982).
[2] J. O. Indekeu, A. Maritan, A. Stella, Phys. Rev. **B35**, 305 (1987).
[3] I. P. Fittipaldi, J. Magn. Magn. Mat. **131**, 43 (1994).
[4] K. Croes, J. O. Indekeu, Mod. Phys. Lett. **B7**, 699 (1993).
[5] J. A. Plascak, W. Figueiredo, B. C. S. Grandi, Braz. J. Phys. **29**, 579 (1999).
[6] C. N. Likos, Phys. Rev. **E55**, 2001 (1997).
[7] P. Pawlicki, G. Musiał, G. Kamieniarz, J. Rogiers, Physica **A242**, 281 (1997).
[8] J. R. de Sousa, I. G. Araujo, J. A. Plascak, Physica **A278**, 181 (2000).
[9] D. P. Lara, J. A. Plascak, Int. J. Mod. Phys. **B12**, 1831 (1998).
[10] P. A. Slotte, J. Phys. **A20**, L177 (1987).
[11] G. Kamieniarz, R. Dekeyser, *Symmetry and Structural Properties of Condensed Matter*, ed. W. Florek, D. Lipiński and T. Lulek, World Scientific, Singapore 1993, p. 181.
[12] G. Kamieniarz, H. W. J. Blöte, J. Phys. **A26**, 201 (1993).
[13] M. N. Barber, *Phase Transitions and Critical Phenomena*, vol. 8, ed. C. Domb and J. L. Lebowitz, Academic Press London, 1983, p. 145.