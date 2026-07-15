# A PSEUDOPOTENTIAL CALCULATION OF THE SELF-INTERSTITIAL FORMATION ENERGY IN f.c.c. METALS

A.K. Bandyopadhyay and S.K. Sen

Department of Materials Science, Indian Association for the Cultivation of Science. Jadavpur, Calcutta: 700032, India

(Received 9 July 1987 by M. Balkanski)

VACANCIES AND INTERSTITIALS are important imperfections in crystals. Many physical properties of crystalline materials and particularly diffusion controlled processes leading to solid state reactions are dependent on them. A survey of the literature indicates that there are more theoretical and experimental studies on vacancy formation [1-3] or migration [4, 5] than interstitial formation [6, 10] and migration. The pseudopotential method which has been mostly successful for determining the stable crystal structure [7] and some lattice mechanical and electronic properties of perfect crystals [8, 9] have also been successfully applied for defect studies such as formation energy calculation of various stacking fault configurations [7] and vacancy formation [2] and migration [5] energy calculations. At present, little attention has been paid for calculations of formation of various interstitial configurations. But the necessity for such calculations is evident from the fact that in the equilibrium configuration of some fast diffuser systems, some impurities might dissolve in the interstitial position of the solvent matrix [11]. In this work, we have formulated the formation energies of different self-interstitial positions in f.c.c. metals using the pseudopotential theory and some numerical results have also been presented. All these calculations depend on the results of the differences of some relatively high numbers. So for defect study a careful attention should be paid for numerical accuracy.

The total energy of a metal per ion consists of structure dependent and volume dependent terms. Any point defect calculation reduces to the problem of determining the change in energy involved at constant volume i.e. the change in structure dependent terms of energy which consists of electrostatic and band structure terms

$$
E_{\mathrm{es}}=\frac{Z^{2} e^{2}}{2} \lim _{\eta \rightarrow x}\left[\frac{4 \pi}{\Omega_{0}} \sum_{q}^{\prime} S^{*}(\mathbf{q}) S(\mathbf{q}) \frac{\mathrm{e}^{-q^{2} 4 \eta}}{q^{2}}-2 \sqrt{\frac{\eta}{\pi}}\right],
$$

and

$$
E_{\mathrm{bs}}=\sum_{q}^{\prime} S^{*}(\mathbf{q}) S(\mathbf{q}) F(\mathbf{q}),
$$

where $Z$ is the valence, $\Omega_{0}$, the atomic volume, $\eta$ is the Ewald Fuch's convergence factor. $F(q)$ is known as energy wave number characteristics and is defined as

$$
F(q)=W^{2}(q) \chi(q) \varepsilon(q),
$$

where $w(q)$ is the pseudopotential of the host atom, $\chi$, the perturbation characteristic (or, correlation factor) and $\varepsilon$, the dielectric screening function.

The dependence of $E_{\mathrm{es}}$ and $E_{\mathrm{bs}}$ on atomic arrangements are contained in the structure factor $S(\mathbf{q})$. If we assume that there is no distortion of the remaining lattice for interstitial formation the structure factor effect is the difference of $S^{*}(\mathbf{q}) S(\mathbf{q})$ for the two configurations. Structure factor is defined as

$$
S(\mathbf{q})=\frac{1}{N} \sum_{j} \mathrm{e}^{-i \mathbf{q} \cdot \boldsymbol{r}_{j}},
$$

where $N$ represents total number of atoms and the sum is over all the filled positions $\mathbf{r}_{j}$.

Following Harrison [7], it is now useful to imagine the lattice with an interstitial defect as a perfect lattice with $(N-1)$ atoms to which the $N$-th atom has been inserted at the interstitial position $\mathbf{r}_{\text {int }}$.

In such a case

$$
S(\mathbf{q})=1+\frac{\mathrm{e}^{-i \mathbf{q} \cdot \mathbf{r}_{\mathrm{int}}}-1}{N} \quad \text { for } \mathbf{q}=\mathbf{q}_{0},
$$

and

$$
=\frac{\mathrm{e}^{-i \mathbf{q} \cdot \mathbf{r}_{\mathrm{int}}}}{N} \quad \text { for } \mathbf{q} \neq \mathbf{q}_{0},
$$

where $\mathbf{q}_{0} \mathrm{~s}$ are the lattice wave numbers.

In this case, the Brillouin zone volume has to be scaled down [7] by a factor $(N-1 / N)$ in order to allow the reduction of lattice sites to $(N-1)$ from $N$ to keep the volume constant. So, the modified lattice wavenumber $\mathbf{q}_{0}^{\prime}$ is now related to $\mathbf{q}_{0}$ as $\mathbf{q}_{0}^{\prime}=\mu \mathbf{q}_{0}$ where

$$
\mu=\left(\frac{N-1}{N}\right)^{1 / 3} \simeq 1-\frac{1}{3 N} .
$$

Incorporating these results, the electrostatic energy of

![](./images/812446069953658882_1.jpg)

Fig. 1. F.c.c. interstitial configurations: (a) body cen- tred or octahedral, (b) tetrahedral, (c) Crowdion.

the lattice with an interstitial can be written as

$$
\begin{aligned}
E_{\mathrm{cs}}^{\mathrm{int}}= & \frac{Z^{2} \mathrm{e}^{2}}{2} \lim _{\eta \rightarrow \infty}\left[\frac{4 \pi}{\Omega_{0}} \sum_{\boldsymbol{q}_{0}}^{\prime}\left\{\frac{2}{N}\left(\cos \boldsymbol{q} \cdot \boldsymbol{r}_{\mathrm{int}}-1\right)+1\right\}\right. \\
& \left.\times \frac{\mathrm{e}^{-\mu^{2} q_{0}^{2} \cdot 4 \eta}}{\mu_{2} q_{0}^{2}}-2 \sqrt{\frac{\eta}{\pi}}+\frac{2}{N} \sqrt{\frac{\eta}{\pi}}\right].
\end{aligned}
$$

In the above expression, terms for both $\boldsymbol{q}=\boldsymbol{q}_{0}$ and $\boldsymbol{q} \neq \boldsymbol{q}_{0}$ have been taken into consideration. On further simplification,

$$
\begin{aligned}
E_{\mathrm{cs}}^{\mathrm{int}}= & \frac{E_{\mathrm{cs}}}{\mu^{2}}+\frac{Z^{2} \mathrm{e}^{2}}{2} \lim _{\eta^{\prime} \rightarrow \infty}\left[\frac{4 \pi}{\Omega_{0}} \sum_{q_{0}}^{\prime} \frac{2}{N}\left(\cos \boldsymbol{q} \cdot \boldsymbol{r}_{\mathrm{int}}-1\right)\right. \\
& \left.\times \frac{\mathrm{e}^{-q_{0}^{2} \cdot 4 \eta^{\prime}}}{q_{0}^{2}}+\frac{4}{N} \sqrt{\frac{\eta^{\prime}}{\pi}}\right],
\end{aligned}
$$

where $\eta^{\prime}=\eta / \mu^{2}$, while deriving equation (7) and (8), terms which are of the order of $N^{-2}$ have been neglected. Thus the total electrostatic energy of the lattice is modified as a result of the introduction of the interstitial as

$$
\begin{aligned}
\Delta E_{\mathrm{cs}}^{\mathrm{int}}= & \left(N E_{\mathrm{cs}}\right)^{\mathrm{int}}-\left(N E_{\mathrm{cs}}\right)^{\text {ideal }}=\frac{2}{3} \\
& \times E_{\mathrm{cs}}+\frac{Z^{2} \mathrm{e}^{2}}{2} \lim _{\eta \rightarrow \infty}\left[\frac{4 \pi}{\Omega_{0}} \sum_{q_{0}}^{\prime} 2\left(\cos \boldsymbol{q} \cdot \boldsymbol{r}_{\mathrm{int}}-1\right)\right. \\
& \left.\times \frac{\mathrm{e}^{q_{0}^{2} \cdot 4 \eta^{\prime}}}{q_{0}^{2}}+4 \sqrt{\frac{\eta^{\prime}}{\pi}}\right].
\end{aligned}
$$

Similarly, the change in band structure energy as a result of the introduction of interstitial is given by

$$
\begin{aligned}
\Delta E_{\mathrm{bs}}^{\mathrm{int}}= & \sum_{q_{0}}^{\prime} 2\left(\cos \boldsymbol{q} \cdot \boldsymbol{r}_{\mathrm{int}}-1\right) F(q) \\
& -\frac{1}{3} \sum_{q_{0}} q_{0} \frac{\partial F\left(q_{0}\right)}{\partial q_{0}}+\frac{\Omega_{0}}{2 \pi^{2}} \int_{0}^{\infty} F(q) q^{2} \mathrm{~d} q. \quad(10)
\end{aligned}
$$

The self interstitial formation energy is the sum of electrostatic and band structural change in energy described in the expressions (9) and (10). In the above formulation, the structural energy change has been deduced under the condition of constant volume and the lattice distortion around the interstitial position neglected conventionally because of their great complexity.

The formation energies for three different con- figurations of the interstitial as (a) bodycentred or octahedral, (b) tetrahedral and (c) crowdion (Fig. 1) in some f.c.c. metals have been summarized in Table 1. In this calculation, we have used Ashcroft's potential [12] with Hubbard's exchange and correlation factor [13] written as

$$
W(q)=-\frac{4 \pi \mathrm{e}^{2} Z}{\Omega_{0} q^{2}} \cos q r_{c} \frac{1}{\varepsilon(q)}
$$

$$
\varepsilon(q)=1-\frac{8 \pi \mathrm{e}^{2}}{\Omega_{0} q^{2}}\left(1-\frac{q^{2} / 2}{q^{2}+K_{F}^{2}}\right) \chi(q)
$$

$$
\chi(q)=-\frac{3 Z}{4 E_{F}}\left(\frac{1}{2}+\frac{4 K_{F}^{2}-q^{2}}{8 q K_{F}} \ln \left|\frac{2 K_{F}+q}{2 K_{F}-q}\right|\right).
$$

Here $r_{c}$ is a parameter, and $K_{F}$ and $E_{F}$ are respectively Fermi wave number and Fermi energy. In order to retain the same values of $r_{c}$ for all defect calculations, they have been chosen by matching the experimental values of vacancy formation energies of the respective metals [14].

In Table 1, we have also reported the calculated values of self-interstitial formation energies in the

Table 1. Calculated formation energy values of various self-interstitial configurations in $\mathrm{Cu}, \mathrm{Ag}$ and $\mathrm{Au}$

<table>
<thead>
<tr>
<th>Metal</th>
<th>$r_{i}$ in A.U.</th>
<th>Positions of interstitials</th>
<th colspan="2">Formation $(E_{if}^{f})$ energy in eV</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>Our. Calc.</th>
<th>Previous values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu</td>
<td>1.28</td>
<td>Octahedral</td>
<td>3.40</td>
<td>$2.902^{10},3.2776^{6}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Tetrahedral</td>
<td>4.66</td>
<td>$2.914^{10},6.6356^{6}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Crowdion</td>
<td>5.46</td>
<td>—</td>
</tr>
<tr>
<td>Ag</td>
<td>1.47</td>
<td>Octahedral</td>
<td>3.04</td>
<td>$2.387^{10},3.0480^{6}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Tetrahedral</td>
<td>4.16</td>
<td>$2.409^{10},6.2996^{6}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Crowdion</td>
<td>4.86</td>
<td>—</td>
</tr>
<tr>
<td>Au</td>
<td>1.43</td>
<td>Octahedral</td>
<td>2.91</td>
<td>$4.073^{10},2.7342^{6}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Tetrahedral</td>
<td>4.05</td>
<td>$4.047^{10},5.5447^{6}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Crowdion</td>
<td>4.76</td>
<td>—</td>
</tr>
</tbody>
</table>

above positions done by previous authors [6, 10]. The previous calculations were performed using either interatomic potentials derived entirely from first principles or elastic continuum model. From the Table 1 it is evident that the agreement of our calculated values with the previous ones [6, 10] are satisfactory.

Acknowledgement — The authors gratefully acknowledge Mr. A. Ghorai for helpful discussions and suggestions during the course of the work.

## REFERENCES

1.  A. Ghorai & S.K. Sen, *J. Phys.* **F16**, 271 (1986).
2.  A.R. DuCharme & H.T. Weaver, *Phys. Rev.* **B5**, 330 (1972).
3.  S.M. Kim, J.A. Jackman & W.J.L. Buyers, *J. Phys.* **F14**, 2323 (1984).

4.  R.H. Rautioaho, *Phys. Status Solidi (b)* **115**, 95 (1983).
5.  O. Takai, M. Doyama & Y. Hisamatsu, *Point defects and interactions in metals*, (Edited by J. Takamura, M. Doyama and M. Kirtani), 117 (1982).
6.  L. Kornblit, *Phys. Rev.* **B22**, 1866 (1980).
7.  W.A. Harrison, *Pseudopotentials in the theory of metals* Benjamin, New York, (1966).
8.  D. Sen & S.K. Sen, *Phys. Status Solidi (b)* **127**, 377 (1985).
9.  D. Sen & S.K. Sarkar, *Phys. Status Solidi (b)* **107**, 559 (1981).
10. N.Q. Lam, L. Dagens & N.V. Doan, *J. Phys.* **F13**, 2503 (1983).
11. S.K. Sen, H.B. Huntington & R.S. Sokolowski, *Scripta Metall.* **17**, 569 (1983).
12. N.W. Ashcroft, *Phys. Lett.* **23**, 48 (1966).
13. L.J. Sham & J.M. Ziman, *Solid State Phys.* **15**, 221 (1963).
14. A. Ghorai & S.K. Sen — To be published.