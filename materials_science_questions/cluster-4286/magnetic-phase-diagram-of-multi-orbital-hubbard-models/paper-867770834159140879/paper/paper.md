# Antiferromagnetic fluctuations and dominant $d_{xy}$-wave pairing symmetry in nickelate-based superconductors

Chao Chen, $^1$ Runyu Ma, $^1$ XueLei Sui, $^2$ Ying Liang, $^1$ Bing Huang, $^{2,1}$ and Tianxing Ma$^{1,2, *}$

$^1$Department of Physics, Beijing Normal University, Beijing 100875, China
$^2$Beijing Computational Science Research Center, Beijing 100084, China

Motivated by recent experimental studies on superconductivity found in nickelate-based materials, we study the temperature dependence of the spin correlation and the superconducting pairing interaction within an effective two-band Hubbard model by the quantum Monte Carlo method. Based on parameters extracted from first-principles calculations, our intensive numerical results reveal that the pairing with a $d_{xy}$-wave symmetry firmly dominates over other pairings at low temperature, which is mainly determined by the Ni $3d$ orbital. It is also found that the effective pairing interaction is enhanced as the on-site interaction increases, demonstrating that the superconductivity is driven by strong electron-electron correlation. Even though the $(\pi,\pi)$ antiferromagnetic correlation could be enhanced by electronic interaction, there is no evidence for long-range antiferromagnetic order exhibited in nickelate-based superconductors. Moreover, our results offer possible evidence that the pure electron correlation may not account for the charge density wave state observed in nickelates.

## I. INTRODUCTION

Understanding the mechanism of high-Tc superconductivity [1-7] and intertwining symmetry-breaking orders [8-10] has always been a central issue in condensed matter physics. Recently, the discovery of superconductivity in the family of Sr-doped $\text{RNiO}_2$ (R=Nd, La, Pr) [11-15] has attracted great research interest, which may provide a new opportunity for further understanding unconventional superconductivity [16-25]. Among them, one essential object is to identify the dominant superconducting pairing form, which remains a major challenge of today's studies on this family. In a single-particle tunneling experiment on a Sr-doped $\text{NdNiO}_2$ film surface, researchers detected singlet pairing, but they could not distinguish whether it is an $s$ wave, $d$ wave or their mixture [26]. At present, some theoretical studies of nickelate-based superconductors have been based on models with one-orbital (Ni $3d$) band structures that support these materials being captured by a one-band Hubbard model [27-29], and they have revealed a dominant $d$-wave pairing in their model [27, 28]. However, others have proposed various possibilities for multiband models [30-35]. The $t-J-K$ model, which considers the Kondo coupling, exhibits a transition between the $d$ wave and $(d+is)$ wave of the dominant pairing at large hole doping [36]. Research on the controversial pair symmetry of nickelates is necessary both experimentally and theoretically. From the theoretical viewpoint, using unbiased numerical techniques is believed to be the only opportunity to achieve this goal if the electronic correlation dominates in the system.

Besides the superconductivity, the spin density wave (SDW) [37-39] and charge density wave (CDW) [40-45], which are observed in nickelates, also attract high attention in quest of their origins. Previous theoretical works on density functional theory (DFT) [46-50] have systematically studied the characteristics of nickelate electronic structures. It is found that there are both similarities and differences compared with those of cuprates [31, 33, 48-53]. These results provide a cornerstone to study the magnetism, superconductivity and CDW in the nickelate family. According to the DFT calculation of $\text{RNiO}_2$ [48-50], the two bands near $E_F$ mainly contributed to its physical properties. One band, composed of Ni $3d_{x^2-y^2}$ and O $2p$ orbitals, has a Zhang-Rice-singlet-like character, while the contribution of oxygen in the nickelates is smaller than that in cuprates, and the other band, composed of the R $5d$ orbital, forms an important metallic electron pocket. These two orbitals hybridize, forming a two-band system, where the strongly correlated Ni layers play an important role [48-50].

![](./images/867770834159140879_1.jpg)

FIG. 1. (Color online)(a) Here, red and white circles indicate different sublattices, A and B. The nearest distance between B and B (or A and A) is 2. (b) The energy band along the high-symmetry line in the unfolded Brillouin zone. Solid blue lines: $k_z$=0; dashed red lines: $k_z=\pi$ in Table I.

To identify the superconducting pairing form of nickelate-based materials, we perform a quantum Monte Carlo study of the spin correlation and superconducting pairing interaction in an effective two-band microscopic model based on parameters extracted from first-

principles calculations. From the results of the Wannier orbitals [48, 50], a two-band model is constructed that contains two main bands near $E_F$, and this model also contains inter-orbital coupling between the Ni $3d$ orbital and the R $5d$ orbital. The calculations of the pairing correlation show that there exists an extensive $d$-wave channel that firmly dominates over other pairings at low temperature and the pairing channel is determined by the Ni $3d$ orbital. For different fillings $\langle n\rangle$=1.0, 0.9, and 0.8, the $(\pi,\pi)$ antiferromagnetic (AFM) correlation and the effective pairing interaction are both enhanced as the on-site interaction increases. Our unbiased calculations demonstrate that the superconductivity and AFM correlation in nickelate-based superconductors should be driven by electron-electron correlation. Although the $(\pi,\pi)$ antiferromagnetic correlation could be enhanced by electronic interaction, there is no evidence for long- range antiferromagnetic order exhibited in nickelate- based superconductors. Additionally, by considering the nearest-neighbor repulsion of the Ni $3d$ orbital, the CDW state exhibits a $q=(\pi,\pi)$ pattern.

## II. MODEL AND METHODS

In the two-band Hubbard model, the tight-binding part contains intralayer hopping, interlayer hopping and the strongly correlated Ni layer. Therefore, the nickel- square lattice Hamiltonian can be written as

$$
H=H_{1}+H_{2}+H_{3}+H_{4},
$$

$$
H_{1}=t_{3}^{N d-N i} \sum_{\mathbf{i} \eta \sigma}\left[a_{\mathbf{i} \sigma}^{\dagger} b_{\mathbf{i}+\eta \sigma}+h . c .\right],
$$

$$
\begin{aligned}
H_{2}= & t_{1}^{N d}\left[\sum_{\mathbf{i} \tau_{1} \sigma} a_{\mathbf{i} \sigma}^{\dagger} a_{\mathbf{i}+\tau_{1} \sigma}\right]+t_{2}^{N d}\left[\sum_{\mathbf{i} \tau_{2} \sigma} a_{\mathbf{i} \sigma}^{\dagger} a_{\mathbf{i}+\tau_{2} \sigma}\right] \\
& +t_{3}^{N d}\left[\sum_{\mathbf{i} \tau_{3} \sigma} a_{\mathbf{i} \sigma}^{\dagger} a_{\mathbf{i}+\tau_{3} \sigma}\right],
\end{aligned}
$$

$$
\begin{aligned}
H_{3}= & t_{1}^{N i}\left[\sum_{\mathbf{i} \tau_{1} \sigma} b_{\mathbf{i} \sigma}^{\dagger} b_{\mathbf{i}+\tau_{1} \sigma}\right]+t_{2}^{N i}\left[\sum_{\mathbf{i} \tau_{2} \sigma} b_{\mathbf{i} \sigma}^{\dagger} b_{\mathbf{i}+\tau_{2} \sigma}\right] \\
& +t_{3}^{N i}\left[\sum_{\mathbf{i} \tau_{3} \sigma} b_{\mathbf{i} \sigma}^{\dagger} b_{\mathbf{i}+\tau_{3} \sigma}\right],
\end{aligned}
$$

$$
H_{4}=U \sum_{\mathbf{i}} n_{b \mathbf{i} \uparrow} n_{b \mathbf{i} \downarrow}+\mu \sum_{\mathbf{i} \sigma}\left[(1+\Delta / \mu) n_{a \mathbf{i} \sigma}+n_{b \mathbf{i} \sigma}\right](1)
$$

Here, $a_{\mathbf{i} \sigma}$ ($a_{\mathbf{i} \sigma}^{\dagger}$) annihilates (creates) electrons at site $\mathbf{R_i}$ with spin $\sigma$ ($\sigma$=$\uparrow$,$\downarrow$) on sublattice A, $b_{\mathbf{i} \sigma}$ ($b_{\mathbf{i} \sigma}^{\dagger}$) annihilates (creates) electrons at site $\mathbf{R_i}$ with spin $\sigma$ ($\sigma$=$\uparrow$,$\downarrow$) on sublattice B, $n_{a \mathbf{i} \sigma}=a_{\mathbf{i} \sigma}^{\dagger} a_{\mathbf{i} \sigma}$, $n_{b \mathbf{i} \sigma}=b_{\mathbf{i} \sigma}^{\dagger} b_{\mathbf{i} \sigma}$, $\eta=(\pm 3 \hat{x}, \pm 3 \hat{y})$, $\tau_1=(\pm 2 \hat{x}, 0)$ and $(0, \pm 2 \hat{y})$, $\tau_2=(\pm 2 \hat{x}, \pm 2 \hat{y})$, and $\tau_3=(\pm 4 \hat{x}, 0)$ and $(0, \pm 4 \hat{y})$. Our first principles calculations give consistent on-site energy and hopping parameters with previous works. [48-50]. For more details about our Wannier downfolding of $\mathrm{NdNiO}_{2}$, please see Table II in the Appendix 1. For simplicity and clarity, we mainly take the parameters from Refs. [48-50] and list the hopping parameters of $\mathrm{NdNiO}_{2}$ that we use in Table I at $k_{z}$=0, $\pi/2$ and $\pi$. From the analysis of the first-principles calculations [48-50, 54, 55], $\Delta$=$\Delta_1$- $\Delta_2$ represents the on-site energy difference between the Nd $5d$ orbital and the Ni $3d$ orbital. In the following calculations, we mainly discuss the cases of $k_{z}$=0 and $k_{z}=\pi$.

<table>
<caption>Hopping parameters for the tight binding model</caption>
<tbody>
<tr>
<td colspan="2" rowspan="2">$t \setminus k_{z}$</td>
<td>0</td>
<td>$\pi/2$</td>
<td>$\pi$</td>
</tr>
<tr>
<td colspan="3">$t^{Nd}$</td>
</tr>
<tr>
<td>$\Delta_1$</td>
<td></td>
<td>0.633</td>
<td>1.305</td>
<td>1.287</td>
</tr>
<tr>
<td>$t_1$</td>
<td></td>
<td>-0.380</td>
<td>-0.028</td>
<td>0.444</td>
</tr>
<tr>
<td>$t_2$</td>
<td></td>
<td>0.084</td>
<td>-0.090</td>
<td>-0.180</td>
</tr>
<tr>
<td>$t_3$</td>
<td></td>
<td>0.003</td>
<td>0.027</td>
<td>0.051</td>
</tr>
<tr>
<td colspan="2"></td>
<td colspan="3">$t^{Ni}$</td>
</tr>
<tr>
<td>$\Delta_2$</td>
<td></td>
<td>0.242</td>
<td>0.308</td>
<td>0.374</td>
</tr>
<tr>
<td>$t_1$</td>
<td></td>
<td>-0.374</td>
<td>-0.374</td>
<td>-0.374</td>
</tr>
<tr>
<td>$t_2$</td>
<td></td>
<td>0.094</td>
<td>0.094</td>
<td>0.094</td>
</tr>
<tr>
<td>$t_3$</td>
<td></td>
<td>-0.043</td>
<td>-0.043</td>
<td>-0.043</td>
</tr>
<tr>
<td colspan="2"></td>
<td colspan="3">$t^{Nd-Ni}$</td>
</tr>
<tr>
<td>$t_3$</td>
<td></td>
<td>0.020</td>
<td>0.020</td>
<td>0.020</td>
</tr>
</tbody>
</table>

TABLE I. Hopping parameters (in units of eV) for the tight binding model from Refs.[48-50].

Our simulations are mainly performed on the lattice shown in Fig. 1(a) of $L$=8 (the total number of lattice sites is $N_s$=2$\times L^2$=128) by using the determinant quantum Monte Carlo (DQMC) method at finite temperature with periodic boundary conditions. The basic strategy of the DQMC method is to express the partition function as high-dimensional integrals on a set of random auxiliary fields. Then, the Monte Carlo techniques complete the integral. In the simulations, we use 3000 sweeps to equilibrate the system and an additional 10000-40000 sweeps to generate measurements. These measurements were split into 10 bins and provided the basis of coarse-grain averages. The errors were calculated based on the standard deviation from the average. For more technical details, please see Refs.[56-59], as well as information in the Appendix.

As magnetic excitation possibly plays a significant role in the superconductivity mechanism of electronic correlated systems, we investigate the spin susceptibility in the $z$ direction at zero frequency,

$$
\begin{array}{r}
\chi(q)=\int_{0}^{\beta} d \tau \sum_{d, d^{\prime}=a, b} \sum_{\mathbf{i}, \mathbf{j}} e^{i q \cdot\left(\mathbf{i}_{d}-\mathbf{j}_{d^{\prime}}\right)}\left\langle\mathrm{m}_{\mathbf{i}_{d}}(\tau) \cdot \mathrm{m}_{\mathbf{j}_{d^{\prime}}}(0)\right\rangle, \\
(2)
\end{array}
$$

where $\mathrm{m}_{\mathbf{i}_{a}}(\tau)$=$e^{H \tau} m_{\mathbf{i}_{a}}(0) e^{-H \tau}$ with $\mathrm{m}_{\mathbf{i}_{a}}$=$a_{\mathbf{i} \uparrow}^{\dagger} a_{\mathbf{i} \uparrow}-a_{\mathbf{i} \downarrow}^{\dagger} a_{\mathbf{i} \downarrow}$ and $\mathrm{m}_{\mathbf{i}_{b}}$=$b_{\mathbf{i} \uparrow}^{\dagger} b_{\mathbf{i} \uparrow}-b_{\mathbf{i} \downarrow}^{\dagger} b_{\mathbf{i} \downarrow}$. To study the superconducting

property of nickelate-based superconductors, we calculated the pairing susceptibility,

$$
P_{\alpha}=\frac{1}{N_{s}} \sum_{\mathbf{i}, \mathbf{j}} \int_{0}^{\beta} d \tau\left\langle\Delta_{\alpha}^{\dagger}(\mathbf{i}, \tau) \Delta_{\alpha}(\mathbf{j}, 0)\right\rangle, \tag{3}
$$

where $\alpha$ denotes the pairing symmetry. Due to the constraint of different on-site Hubbard interaction in two sublattices, pairing between the same sublattices is favored, and the corresponding order parameter $\Delta_{\alpha}^{\dagger}(\mathbf{i})$ is written as

$$
\Delta_{\alpha}^{\dagger}(\mathbf{i})=\sum_{l} f_{\alpha}^{\dagger}\left(\delta_{l}\right)\left(a_{\mathbf{i} \uparrow}^{\dagger} b_{\mathbf{i}+\delta_{l} \downarrow}-a_{\mathbf{i} \downarrow} b_{\mathbf{i}+\delta_{l} \uparrow}\right)^{\dagger},
$$

where $f_{\alpha}\left(\delta_{l}\right)$ stands for the form factor of the pairing function. The vectors $\delta_{l}(l=1,2,3,4)$ represent the nearest intersublattice connections, where $\delta$ is $( \pm \hat{x}, \pm \hat{y})$, or the nearest intrasublattice connections where $\delta^{\prime}$ is $( \pm 2 \hat{x}, 0)$ and $(0, \pm 2 \hat{y})$.

Furthermore, in order to explore the CDW state, we define the density-density correlation function[60-62],

$$
C(R)=\frac{1}{N_{s} N_{R}} \sum_{\mathbf{i}} \sum_{|\mathbf{j}-\mathbf{i}|=\mathbf{R}}\left\langle\left(n_{i}-\left\langle n_{i}\right\rangle\right)\left(n_{j}-\left\langle n_{j}\right\rangle\right)\right\rangle, \tag{4}
$$

Here, $n_{i}$ and $n_{j}$ denote the electronic number operator at site $\mathbf{R}_{\mathbf{i}}$ and $\mathbf{R}_{\mathbf{j}}$. $R$ is the distance between site $\mathrm{i}$ and site $\mathrm{j}$. The $N_{R}$ is the total number of distance $R$. And its Fourier transform can be written as,

$$
C(q)=\frac{1}{N_{s}} \sum_{\mathbf{R}} e^{i q R} C(R), \tag{5}
$$

### III. RESULTS AND DISCUSSION

To study the magnetic correlations, we calculated the spin susceptibility $\chi(\mathbf{q})$ in Fig. 2 at different $U$ and fillings $\langle n\rangle$ at temperature $T / t=1 / 10$. In Fig. 2, one can notice that there is a sharp peak at $(\pi, \pi)$, which indicates the domination of AFM correlation at both $k_{z}=0$ and $k_{z}=\pi$. In Fig. 2 (a) and Fig. 2(c), we can see that the AFM correlation is enhanced as $U$ increases, which indicates that such an AFM correlation is driven by strong electron-electron correlation. Fig. 2 (b) and Fig. 2 (d) shows that the peak is enhanced at fillings $\langle n\rangle$=0.9 and 0.8, which indicates that the AFM correlation is promoted when the system is doped away from half filling. Recently, resonant inelastic x-ray scattering experiments have revealed an AFM exchange interaction[38]. Our results here might provide evidence for the AFM exchange couplings observed in infinite-layer nickelates.

![](./images/867770834159140879_2.jpg)

FIG. 2. (Color online) Magnetic susceptibility $\chi(q)$ versus momentum $q$, (a) for different $U$ at $\langle n\rangle=1.0$, (b) for different fillings at $U / t=3.0$ (where $t=|t_{1}^{N i}|=0.374 eV$ ) and $k_{z}=0$ on a $2 \times 8^{2}$ lattice; (c) for different $U$ at $\langle n\rangle=1.0$, (d) for different fillings at $U / t=3.0$ and $k_{z}=\pi$ on a $2 \times 8^{2}$ lattice.

In Fig. 3 (a), we show the temperature dependence of the pairing susceptibilities for different pairing symmetries at half filling with $U / t=3.0$ at $k_{z}=0$. We can clearly observe that the pairing susceptibilities for various pairing symmetries increase with decreasing temperature. Most strikingly, $d_{x y}$ increases much faster than any other pairing symmetry as the temperature is lowered. This indicates that the $d_{x y}$ pairing symmetry is dominant over the other pairing symmetry at half filling. Our further results also illustrate that the $d_{x y}$ pairing symmetry is robust at different fillings and $U$.

The effective pairing interaction is a direct probe for the superconductivity. To extract the effective pairing interaction, the uncorrelated single-particle contribution $\widetilde{P}_{\alpha}(\mathbf{i}, \mathbf{j})$ is calculated, which is achieved by replacing $\langle a_{\mathbf{i} \downarrow}^{\dagger} b_{\mathbf{j} \uparrow} a_{\mathbf{i}+\delta_{l} \downarrow}^{\dagger} b_{\mathbf{j}+\delta_{l^{\prime}} \uparrow}\rangle$ in Eq. 3 with $\langle a_{\mathbf{i} \downarrow}^{\dagger} b_{\mathbf{j} \uparrow}\rangle\langle a_{\mathbf{i}+\delta_{l} \downarrow}^{\dagger} b_{\mathbf{j}+\delta_{l^{\prime}} \uparrow}\rangle$, and then we get the effective pairing interaction $P_{\alpha}-\widetilde{P}_{\alpha}$. In Fig. 3 (b) and Fig. 3 (c), it is obvious that $P_{\alpha}-\widetilde{P}_{\alpha}$ presents a very similar temperature dependence to that of $P_{\alpha}$ at $\langle n\rangle=1.0$ or $\langle n\rangle=0.8$. Moreover, the effective pairing interaction for $d_{x y}$ pairing is always positive and increases much faster than any other pairing symmetry at low temperatures. Such a temperature dependence shows that there indeed exists attraction for the $d_{x y}$ pairing at $k_{z}=0$. From Fig. 3 (d), we can find that the $d_{x y}$ pairing symmetry is also dominant at $k_{z}=\pi$. Therefore, although hopping parameters $t_{i}^{N d}$ and the on-site energy difference $\Delta$ are changed at different $k_{z}$, the investigated magnetism and pairing interaction show identical physical results. In the following, we mainly discuss hopping parameters at $k_{z}=0$ for simplicity.

Fig. 4 (a) shows the effective pairing interaction as a function of temperature for the $d_{x y}$ wave at different $U$. We can see that the effective pairing interaction of the $d_{x y}$ wave is enhanced with increasing $U$. For $U / t=1.0$,

![](./images/867770834159140879_3.jpg)

FIG. 3. (Color online) (a) Pairing susceptibility $P_{\alpha}$ and (b) the effective pairing interaction $P_{\alpha}-\tilde{P}_{\alpha}$ as a function of temperature for different pairing symmetries at $\langle n\rangle=1.0$, $U/t=3.0$ and $k_{z}=0$ on a $2\times8^{2}$ lattice. (c) The effective pairing interaction $P_{\alpha}-\tilde{P}_{\alpha}$ as a function of temperature for different pairing symmetries at $\langle n\rangle=0.8$, $U/t=3.0$ and $k_{z}=0$ on a $2\times8^{2}$ lattice, (d) at $\langle n\rangle=1.0$, $U/t=3.0$ and $k_{z}=\pi$ on a $2\times8^{2}$ lattice.

![](./images/867770834159140879_4.jpg)

FIG. 4. (Color online) (a) The effective pairing interaction $P_{d_{xy}}-\tilde{P}_{d_{xy}}$ as a function of temperature for different $U$ at $\langle n\rangle=1.0$ and $k_{z}=0$ on a $2\times8^{2}$ lattice. (b) The effective pairing interaction $P_{d_{xy}}-\tilde{P}_{d_{xy}}$ and the $(\pi,\pi)$ AFM correlation $\chi(\pi,\pi)$ as a function of fillings at $T/t=1/10$, $U/t=3.0$ and $k_{z}=0$ on a $2\times8^{2}$ lattice.

the effective pairing interaction $P_{d_{xy}}-\tilde{P}_{d_{xy}}$ is very small even in the low-temperature region, which may be due to the small AFM structure of the system in Fig. 2(a). For $U/t=3.0$ and $U/t=5.0$, remarkably, the effective pairing interaction $P_{d_{xy}}-\tilde{P}_{d_{xy}}$ tends to diverge at low temperatures, and with increasing $U$, this divergence tends to be promoted. This indicates that the $d_{xy}$ pairing superconductivity should be driven by a strong electron-electron correlation.

In Fig. 4 (b), we studied the filling dependence of the effective pairing interaction $P_{d_{xy}}-\tilde{P}_{d_{xy}}$ and the $(\pi,\pi)$ AFM correlation $\chi(\pi,\pi)$ at $T/t=1/10$, $U/t=3.0$ and $k_{z}=0$. Fig. 4 (b) indicates that the optimal electron filling is slightly below $\langle n\rangle=0.8$, where the effective pairing interaction and the AFM correlation is largest. Fig. 2 and Fig. 4 show that the increase in the peak at $(\pi,\pi)$ of spin susceptibility is correlated with the promotion of the pairing susceptibility. This directly confirms that the $(\pi,\pi)$ AFM fluctuations enhance the $d_{xy}$ pairing.

![](./images/867770834159140879_5.jpg)

FIG. 5. (Color online) (a) The AFM spin structure factor $S_{AFM}$ depends on $\beta=1/T$ with different interaction strengths and lattice sizes at $\langle n\rangle=1.0$ and $k_{z}=0$. (b) Magnetic susceptibility $\chi(q)$ versus momentum $q$ for different lattice sizes at $U/t=3.0$, $T/t=1/10$, $k_{z}=0$ for $\langle n\rangle=1.0$ and (c) $\langle n\rangle=0.8$. (d) The effective pairing interaction $P_{d_{xy}}-\tilde{P}_{d_{xy}}$ as a function of temperature for different lattice sizes at $\langle n\rangle=0.8$, $U/t=3.0$ and $k_{z}=0$.

From the above studies, we know that the system exhibits local antiferromagnetism. To further explore whether there is a long-range AFM order, we also calculate the AFM spin structure factor,

$$
S_{AFM}=\frac{1}{N_{s}}\langle\left|\sum_{r}(-1)^{r}\hat{S}_{br}^{z}\right|^{2}\rangle,\tag{6}
$$

Here, $\hat{S}_{br}^{z}$ is the $z$ component spin operator on the B sublattice. When $\lim_{N_{s}\to\infty}(S_{AFM}/N_{s})>0$, it indicates the onset of long-range AFM order. In Fig. 5 (a), we present the results of the AFM spin structure factors as a function of $\beta$ for different interaction strengths $U$ and lattice sizes $L$, which demonstrates the spin structure factor is nearly saturated at $\beta$=10. Interesting, $S_{AFM}$ decreases as the lattice size increases at low temperatures, which indicates that there is no long-range AFM order at $U/t\leq5.0$ and $\langle n\rangle=1.0$. In Fig. 5 (b) and Fig. 5 (c), it is shown that $\chi(q)$ has a very minor size dependency with lattice sizes $L$=10 and 12 at $\langle n\rangle=1.0$

![](./images/867770834159140879_6.jpg)

FIG. 6. (Color online) (a) The density-density correlations $C(R)$ of Ni $3d$ orbital as a function of distance $R$ for different $V$ at $\langle n \rangle =1.0$, $U/t=3.0$ and temperature $T/t=1/6$ on a $2 \times 12^2$ lattice. Inset: The enlarged $C(R)$ for $R \geq 4.0$. (b) The density-density correlations $C(q)$ versus momentum $q$ for different $V$ at $\langle n \rangle =1.0$, $U/t=3.0$ and $T/t=1/6$ on a $2 \times 12^2$ or $2 \times 8^2$ lattice. Inset: $C(q)$ versus momentum $q$ for different $T$ at $\langle n \rangle =1.0$, $U/t=3.0$ and $V/t=0.9$ on a $2 \times 12^2$ lattice.

or $\langle n \rangle =0.8$. Actually, it is more difficult to exhibit long-range AFM order at $\langle n \rangle =0.8$, since $\chi(q)$ decreases as the lattice size increases from $L$=8 to 10. Different from the AFM spin structure factors, as that shown in Fig. 5 (d), the effective pairing interaction increases very fast as the temperature decreases, and has a potential to diverge as the temperature is low enough. Moreover, $P_{d_{xy}} - \tilde{P}_{d_{xy}}$ increases slightly as the system size increases. These two facts, different from the magnetic order, indicate that the superconducting order with $d_{xy}$ symmetry should survive even at thermodynamic limit. Therefore, our numerical results reveal that the $d_{xy}$-wave symmetry firmly dominates over other pairings and the system may exhibit superconductivity as the temperature is low enough. Two closely related theoretical works by DMFT also report the absence of long-range AFM order and its competition with superconductivity [63, 64].

At last, to discuss the electron correlation effect on the CDW state, we consider the nearest-neighbor repulsion of the Ni $3d$ orbital in the Hamiltonian, which can be written as

$$
H_{V}=V \sum_{\mathbf{i}, \tau_{\mathbf{l}}} n_{b \mathbf{i}} n_{b\left(\mathbf{i}+\tau_{\mathbf{l}}\right)}, \tag{7}
$$

In Fig. 6 (a), we can notice the density-density correlation function $C(R)$ develops a staggered pattern as the interaction strength increases to $V=0.9t$, which indicates the onset of the CDW. Fig. 6 (b) shows that the peak of $q=(\pi,\pi)$ is quickly enhanced at $V=0.9t$, which also is a signal of the CDW's presence. Due to the serious sign problem at low temperature or high interaction, we only display the temperature effect at $T/t=1/4,1/5,1/6$ and $V=0.9t$ in the inset of Fig. 6 (b) and can see a small enhancement of charge correlations with decreasing temperature.

## IV. SUMMARY

In summary, within an effective two-band model for nickelate-based superconductors, we study the spin correlation, the superconducting pairing interaction, and the density-density correlation by using the unbiased numerical techniques of DQMC. We identify that the $d_{xy}$ wave pairing channel is dominant in nickelate-based superconductors, which might support the recent London penetration depth experiment [65]. Both the $(\pi,\pi)$ AFM and the pairings with the $d_{xy}$ symmetry are enhanced with increasing electron-electron correlation, especially in the low-temperature region. Moreover, as the system is doped away from half filling, the effective pairing interaction of $d_{xy}$ symmetry is also enhanced and reaches maximum at $\langle n \rangle \approx 0.8$. Our results also indicate that the system may not exhibit long-range AFM, which is also not observed experimentally [37-39, 66]. Although the study of charge correlations does not display a wave vector $q \approx (0.333,0)$, which has been observed in experiments [41, 42], this initial attempt reveals a more complex mechanism should be established to illustrate the CDW phase in nickelates [67]. In a further work, we simulate the effect of symmetry breaking by modifying the periodic chemical potential, which shows a different CDW pattern [68]. All in all, our work shares exact numerical results to understand the superconducting and symmetry-breaking orders of nickelate-based materials.

## ACKNOWLEDGEMENTS

We thank Huijia Dai and Jingyao Meng for useful discussions. This work was supported by NSFC (Grant No. 11974049). The numerical simulations in this work were performed at the HSCC of Beijing Normal University and Tianhe in Beijing Computational Science Research Center.

## Appendix

In this appendix, we present detailed information on hopping parameters for our Wannier downfolding, the pairing symmetries of the nickel square, correction of the Trotter error, and the sign problem.

### 1. Hopping parameters for our Wannier downfolding

In consideration of the two-band model in our Hamiltonian, we chose orbital sets of $Ni_{3d_{x^2-y^2}}$ and $Nd/La_{5d_{z^2}}$ in Wannier downfolding calculations as implemented in Wannier90 [69], which can reproduce the band structure near the Fermi level accurately.

The calculated hopping parameters for two-orbital
Wannierization are listed in Table II.

<table>
<caption>Hopping parameters for the tight binding model</caption>
<thead>
  <tr>
    <th></th>
    <th></th>
    <th></th>
    <th>$NdNiO_2$</th>
    <th>$LaNiO_2$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>i</th>
    <th>j</th>
    <th>k</th>
    <th colspan="2">$t_{[i,j,k]}^{Ni}$</th>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0.306385</td>
    <td>0.284621</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>-0.377362</td>
    <td>-0.380994</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>0.094731</td>
    <td>0.095830</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0</td>
    <td>0</td>
    <td>-0.049510</td>
    <td>-0.049076</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>-0.027912</td>
    <td>-0.032524</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>-0.001615</td>
    <td>0.000423</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0.008920</td>
    <td>0.009345</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0.001415</td>
    <td>0.000151</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>3</td>
    <td>-0.000053</td>
    <td>0.001201</td>
  </tr>
  <tr>
    <th>i</th>
    <th>j</th>
    <th>k</th>
    <th colspan="2">$t_{[i,j,k]}^{Nd/La}$</th>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>1.493987</td>
    <td>1.219156</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>-0.02938</td>
    <td>-0.068788</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>-0.157513</td>
    <td>-0.087446</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0</td>
    <td>0</td>
    <td>0.051356</td>
    <td>0.021989</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>-0.293301</td>
    <td>-0.048961</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>0.015698</td>
    <td>-0.196251</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0.004019</td>
    <td>-0.005498</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0.027121</td>
    <td>-0.099677</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>3</td>
    <td>0.006169</td>
    <td>-0.003715</td>
  </tr>
  <tr>
    <th>i</th>
    <th>j</th>
    <th>k</th>
    <th colspan="2">$t_{[i,j,k]}^{Nd/La-Ni}$</th>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0.000151</td>
    <td>-0.011252</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>-0.000239</td>
    <td>0.009664</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>-0.000037</td>
    <td>0.003106</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0</td>
    <td>0</td>
    <td>0.020577</td>
    <td>0.001579</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>-0.000157</td>
    <td>-0.006010</td>
  </tr>
  <tr>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>-0.007317</td>
    <td>0.008403</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0.000070</td>
    <td>0.006332</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>2</td>
    <td>0.000102</td>
    <td>-0.004345</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>3</td>
    <td>-0.000040</td>
    <td>-0.001681</td>
  </tr>
</tbody>
</table>

TABLE II. On-site energy and hopping parameters (eV) for two-orbital wannierization for $NdNiO_2$ and $LaNiO_2$.

## 2. The pairing symmetries of the nickel-square

We referenced four kinds of pairing forms from the iron-square lattice[58], which are pictured in Fig. 7. These singlet $s$-wave and $d$-wave pairings have the form factor
$$
\begin{aligned}
s_{xy}\text{-wave } &: f_{s_{xy}}(\delta_l')=1,\ l=1,2,3,4, \\
d_{xy}\text{-wave } &: f_{d_{xy}}(\delta_l')=1(\delta_l'=(\pm2\hat{x},0)) \\
\text{and}\ \ \ \ &f_{d_{xy}}(\delta_l')=-1(\delta_l'=(0,\pm2\hat{y})), \\
s_{x^2+y^2}\text{-wave}: &f_{s_{x^2+y^2}}(\delta_l')=1,\ l=1,2,3,4, \\
d_{x^2-y^2}\text{-wave}: &f_{d_{x^2-y^2}}(\delta_l')=1(\delta_l'=\pm(-\hat{x},\hat{y})) \\
\text{and}\ \ \ \ &f_{d_{x^2-y^2}}(\delta_l')=-1(\delta_l'=\pm(\hat{x},\hat{y})).
\end{aligned} \tag{8}
$$

![](./images/867770834159140879_7.jpg)

FIG. 7. (Color online) Phase of the $s_{xy}$, $d_{xy}$, $s_{x^2+y^2}$ and $d_{x^2-y^2}$.

![](./images/867770834159140879_8.jpg)

FIG. 8. (Color online) Influence of the imaginary time step $\Delta\tau$ to the $(\pi,\pi)$ antiferromagnetic correlation $\chi(\pi,\pi)$ for different $U$ at (a) $T/t=1/6$, $k_z=0$, (b) $T/t=1/10$, $k_z=0$, (c) $T/t=1/6$, $k_z=\pi$, (d) $T/t=1/10$, $k_z=\pi$ on a $2\times8^2$ lattice.

In experiment, by using scanning tunneling microscopy[70] or high-resolution laser-ARPES [71, 72], there may be a way to distinguish the $d_{xy}$ and $d_{x^2-y^2}$ pairings.

## 3. Correction of the Trotter error

Since the operators $H_K$ (kinetic energy) and $H_U$ (potential energy) do not commute, the DQMC algorithm employs the Trotter-Suzuki decomposition to approximate the partition function and then the imaginary-time propagator can be written as
$$
e^{-\Delta\tau H} \approx e^{-\Delta\tau H_K} e^{-\Delta\tau H_U}, \tag{9}
$$

In this process, we can correct systematic error by extrapolating the results at different time steps to the $\Delta\tau=0$ limit. In Fig. 8, we show an impact of the imaginary time step $\Delta\tau$ to the $(\pi,\pi)$ antiferromagnetic correlation $\chi(\pi,\pi)$. The figure indicates that, regardless

![](./images/867770834159140879_9.jpg)

FIG. 9. (Color online) Average sign $\langle sign\rangle$ as a function of nearest-neighbor interaction $V$ for different temperatures at $\langle n\rangle=1.0$, $U/t=3.0$ and $k_z=0$ on $2\times12^2$ or $2\times8^2$ lattice.

of the interaction strength and temperature, the $\chi(\pi,\pi)$ is essentially identical within the different time steps. Other observables can see a similar behavior. As such, Trotter errors can be negligible at the $\Delta\tau$ value used in this paper.

### 4. The Sign problem
For the finite-temperature DQMC method, the infamous sign problem prevents accuracy of results for higher interaction, lower temperature, and larger lattice. Therefore, we assess the average of sign carefully. In our simulations, the pure on-site interaction does not make the sign-problem terrible for different electron fillings even at low temperatures (and $\langle sign\rangle\approx1$). However, we found that the sign problem became worse when we consider the nearest-neighbor repulsion of the Ni $3d$ orbital to compute the charge-density-wave (CDW) state. Fig. 9 shows the effect of the nearest-neighbor interaction and the temperature on the sign problem with measurements of 10000 times. We can notice that the sign problem becomes worse with increasing interaction or decreasing temperature. Our present results are reliable because the average sign is still larger than 0.50 for $V=0.9t$, $U/t=3.0$, and $T/t=1/6$ on an $L=12$ lattice. To keep the same quality of data with $\langle sign\rangle\approx1$, much longer measurements are essential to compensate the fluctuations. In fact, the measurements should be enlarged by a factor on the order of $\langle sign\rangle^{-2}$[56, 73]. In our simulations, we have made measurement of more than 40000 times for some results. Therefore, the results with the current Monte Carlo parameters are reliable.

[1] J. Bardeen, L. N. Cooper, and J. R. Schrieffer, *Phys. Rev.* **108**, 1175 (1957).
[2] J. G. Bednorz and K. A. Müller, *Zeitschrift für Physik B Condensed Matter* **64**, 189 (1986).
[3] P. W. Anderson, *Science* **235**, 1196 (1987).
[4] J. G. Bednorz and K. A. Müller, *Rev. Mod. Phys.* **60**, 585 (1988).
[5] P. W. Anderson, P. A. Lee, M. Randeria, T. M. Rice, N. Trivedi, and F. C. Zhang, *Journal of Physics: Condensed Matter* **16**, R755 (2004).
[6] P. A. Lee, N. Nagaosa, and X.-G. Wen, *Rev. Mod. Phys.* **78**, 17 (2006).
[7] D. J. Scalapino, *Rev. Mod. Phys.* **84**, 1383 (2012).
[8] E. Fradkin, S. A. Kivelson, and J. M. Tranquada, *Rev. Mod. Phys.* **87**, 457 (2015).
[9] R. Comin and A. Damascelli, *Annual Review of Condensed Matter Physics* **7**, 369 (2016).
[10] B. Keimer, S. A. Kivelson, M. R. Norman, S. Uchida, and J. Zaanen, *Nature* **518**, 179 (2015).
[11] D. Li, K. Lee, B. Y. Wang, M. Osada, S. Crossley, H. R. Lee, Y. Cui, Y. Hikita, and H. Y. Hwang, *Nature* **572**, 624 (2019).
[12] G. A. Sawatzky, *Nature* **572**, 592 (2019).
[13] S. Zeng, C. S. Tang, X. Yin, C. Li, M. Li, Z. Huang, J. Hu, W. Liu, G. J. Omar, H. Jani, Z. S. Lim, K. Han, D. Wan, P. Yang, S. J. Pennycook, A. T. S. Wee, and A. Ariando, *Phys. Rev. Lett.* **125**, 147003 (2020).
[14] L. E. Chow, S. K. Sudheesh, P. Nandi, S. W. Zeng, Z. T. Zhang, X. M. Du, Z. S. Lim, E. E. M. Chia, and A. Ariando, (2022), arXiv:2201.10038.
[15] D. Li, B. Y. Wang, K. Lee, S. P. Harvey, M. Osada, B. H. Goodge, L. F. Kourkoutis, and H. Y. Hwang, *Phys. Rev. Lett.* **125**, 027001 (2020).
[16] M.-Y. Choi, K.-W. Lee, and W. E. Pickett, *Phys. Rev. B* **101**, 020503 (2020).
[17] L. Si, W. Xiao, J. Kaufmann, J. M. Tomczak, Y. Lu, Z. Zhong, and K. Held, *Phys. Rev. Lett.* **124**, 166402 (2020).
[18] S. Ryee, H. Yoon, T. J. Kim, M. Y. Jeong, and M. J. Han, *Phys. Rev. B* **101**, 064513 (2020).
[19] J. Krishna, H. LaBollita, A. O. Fumega, V. Pardo, and A. S. Botana, *Phys. Rev. B* **102**, 224506 (2020).
[20] M. Osada, B. Y. Wang, K. Lee, D. Li, and H. Y. Hwang, *Phys. Rev. Materials* **4**, 121801 (2020).
[21] P. Jiang, L. Si, Z. Liao, and Z. Zhong, *Phys. Rev. B* **100**, 201106 (2019).
[22] B.-X. Wang, H. Zheng, E. Krivyakina, O. Chmaissem, P. P. Lopes, J. W. Lynn, L. C. Gallington, Y. Ren, S. Rosenkranz, J. F. Mitchell, and D. Phelan, *Phys. Rev. Materials* **4**, 084409 (2020).
[23] K. Lee, B. H. Goodge, D. Li, M. Osada, B. Y. Wang, Y. Cui, L. F. Kourkoutis, and H. Y. Hwang, *APL Materials* **8**, 041107 (2020).
[24] M. Osada, B. Y. Wang, B. H. Goodge, S. P. Harvey, K. H. Lee, D. F. Li, L. F. Kourkoutis, and H. Y. Hwang, *Adv.Mater.* **33**, 2104083 (2021).
[25] S. Zeng, C. Li, L. E. Chow, Y. Cao, Z. Zhang, C. S. Tang, X. Yin, Z. S. Lim, J. Hu, P. Yang, and A. Ariando, *Science Advances* **8**, eabl9927 (2022).
[26] Q. Gu, Y. Li, S. Wan, H. Li, W. Guo, H. Yang, Q. Li, X. Zhu, X. Pan, Y. Nie, and H.-H. Wen, *Nature Communications* **11**, 6027 (2020).
[27] M. Zhang, Y. Zhang, H. Guo, and F. Yang, *Chinese Physics B* **30**, 108204 (2021).

* txma@bnu.edu.cn

[28] Y.-H. Zhang and A. Vishwanath, *Phys. Rev. Research* **2**, 023112 (2020).

[29] M. Kitatani, L. Si, O. Janson, R. Arita, Z. Zhong, and K. Held, *npj Quantum Materials* **5**, 59 (2020).

[30] P. Adhikary, S. Bandyopadhyay, T. Das, I. Dasgupta, and T. Saha-Dasgupta, *Phys. Rev. B* **102**, 100501 (2020).

[31] X. Wu, D. Di Sante, T. Schwemmer, W. Hanke, H. Y. Hwang, S. Raghu, and R. Thomale, *Phys. Rev. B* **101**, 060504 (2020).

[32] G.-M. Zhang, Y.-f. Yang, and F.-C. Zhang, *Phys. Rev. B* **101**, 020501 (2020).

[33] C. Lu, L.-H. Hu, Y. Wang, F. Yang, and C. Wu, *Phys. Rev. B* **105**, 054516 (2022).

[34] H. Sakakibara, H. Usui, K. Suzuki, T. Kotani, H. Aoki, and K. Kuroki, *Phys. Rev. Lett.* **125**, 077003 (2020).

[35] A. Kreisel, B. M. Andersen, A. T. Rømer, I. M. Eremin, and F. Lechermann, *Phys. Rev. Lett.* **129**, 077002 (2022).

[36] Z. Wang, G.-M. Zhang, Y.-f. Yang, and F.-C. Zhang, *Phys. Rev. B* **102**, 220501 (2020).

[37] R. A. Ortiz, P. Puphal, M. Klett, F. Hotz, R. K. Kremer, H. Trepka, M. Hemmida, H.-A. K. von Nidda, M. Isobe, R. Khasanov, H. Luetkens, P. Hansmann, B. Keimer, T. Schäfer, and M. Hepting, *Phys. Rev. Research* **4**, 023093 (2022).

[38] H. Lu, M. Rossi, A. Nag, M. Osada, D. F. Li, K. Lee, B. Y. Wang, M. Garcia-Fernandez, S. Agrestini, Z. X. Shen, E. M. Been, B. Moritz, T. P. Devereaux, J. Zaanen, H. Y. Hwang, K.-J. Zhou, and W. S. Lee, *Science* **373**, 213 (2021).

[39] Y. Cui, C. Li, Q. Li, X. Zhu, Z. Hu, Y. feng Yang, J. Zhang, R. Yu, H.-H. Wen, and W. Yu, *Chinese Physics Letters* **38**, 067401 (2021).

[40] M. Rossi, M. Osada, J. Choi, S. Agrestini, D. Jost, Y. Lee, H. Lu, B. Y. Wang, K. Lee, A. Nag, Y.-D. Chuang, C.-T. Kuo, S.-J. Lee, B. Moritz, T. P. Devereaux, Z.-X. Shen, J.-S. Lee, K.-J. Zhou, H. Y. Hwang, and W.-S. Lee, *Nature Physics* **18**, 869 (2022).

[41] C. C. Tam, J. Choi, X. Ding, S. Agrestini, A. Nag, M. Wu, B. Huang, H. Luo, P. Gao, M. García-Fernández, L. Qiao, and K.-J. Zhou, *Nature Materials* **21**, 1116 (2022).

[42] G. Krieger, L. Martinelli, S. Zeng, L. E. Chow, K. Kummer, R. Arpaia, M. Moretti Sala, N. B. Brookes, A. Ariando, N. Viart, M. Salluzzo, G. Ghiringhelli, and D. Preziosi, *Phys. Rev. Lett.* **129**, 027002 (2022).

[43] C. Peng, H.-C. Jiang, B. Moritz, T. P. Devereaux, and C. Jia, (2021), arXiv:2110.07593.

[44] H. Chen, Y. feng Yang, and G.-M. Zhang, (2022), arXiv:2204.12208.

[45] Y. Shen, M. Qin, and G.-M. Zhang, (2022), arXiv:2207.00266.

[46] V. I. Anisimov, D. Bukhvalov, and T. M. Rice, *Phys. Rev. B* **59**, 7901 (1999).

[47] K.-W. Lee and W. E. Pickett, *Phys. Rev. B* **70**, 165109 (2004).

[48] A. S. Botana and M. R. Norman, *Phys. Rev. X* **10**, 011024 (2020).

[49] E. Been, W.-S. Lee, H. Y. Hwang, Y. Cui, J. Zaanen, T. Devereaux, B. Moritz, and C. Jia, *Phys. Rev. X* **11**, 011050 (2021).

[50] M. Hepting, D. Li, C. J. Jia, H. Lu, E. Paris, Y. Tseng, X. Feng, M. Osada, E. Been, Y. Hikita, Y.-D. Chuang, Z. Hussain, K. J. Zhou, A. Nag, M. Garcia-Fernandez, M. Rossi, H. Y. Huang, D. J. Huang, Z. X. Shen, T. Schmitt, H. Y. Hwang, B. Moritz, J. Zaanen, T. P. Devereaux, and W. S. Lee, *Nature Materials* **19**, 381 (2020).

[51] M. Jiang, M. Berciu, and G. A. Sawatzky, *Phys. Rev. Lett.* **124**, 207004 (2020).

[52] Y. Nomura, M. Hirayama, T. Tadano, Y. Yoshimoto, K. Nakamura, and R. Arita, *Phys. Rev. B* **100**, 205138 (2019).

[53] L.-H. Hu and C. Wu, *Phys. Rev. Research* **1**, 032046 (2019).

[54] J. Karp, A. S. Botana, M. R. Norman, H. Park, M. Zingl, and A. Millis, *Phys. Rev. X* **10**, 021061 (2020).

[55] F. Lechermann, *Phys. Rev. X* **10**, 041002 (2020).

[56] R. Blankenbecler, D. J. Scalapino, and R. L. Sugar, *Phys. Rev. D* **24**, 2278 (1981).

[57] T. Ma, F. Hu, Z. Huang, and H.-Q. Lin, *Applied Physics Letters* **97**, 112504 (2010).

[58] T. Ma, H.-Q. Lin, and J. Hu, *Phys. Rev. Lett.* **110**, 107002 (2013).

[59] S. R. White, D. J. Scalapino, R. L. Sugar, E. Y. Loh, J. E. Gubernatis, and R. T. Scalettar, *Phys. Rev. B* **40**, 506 (1989).

[60] L. Wang, P. Corboz, and M. Troyer, *New Journal of Physics* **16**, 103008 (2014).

[61] Z.-X. Li, Y.-F. Jiang, and H. Yao, *Phys. Rev. B* **91**, 241117 (2015).

[62] Y.-X. Zhang, W.-T. Chiu, N. C. Costa, G. G. Batrouni, and R. T. Scalettar, *Phys. Rev. Lett.* **122**, 077602 (2019).

[63] J. Karp, A. Hampel, and A. J. Millis, *Phys. Rev. B* **105**, 205131 (2022).

[64] M. Klett, P. Hansmann, and T. Schäfer, *Frontiers in Physics* **10** (2022).

[65] S. P. Harvey, B. Y. Wang, J. Fowlie, M. Osada, K. Lee, Y. Lee, D. Li, and H. Y. Hwang, (2022), arXiv:2201.12971.

[66] M. Hayward and M. Rosseinsky, *Solid State Sciences* **5**, 839 (2003).

[67] X. Sui, J. Wang, X. Ding, K.-J. Zhou, L. Qiao, H. Lin, and B. Huang, (2022), arXiv:2202.11904.

[68] C. Chen, R. Ma, X. Sui, Y. Liang, B. Huang, and T. Ma, (unpublished).

[69] A. A. Mostofi, J. R. Yates, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, *Computer Physics Communications* **178**, 685 (2008).

[70] P. O. Sprau, A. Kostin, A. Kreisel, A. E. Böhmer, V. Taufour, P. C. Canfield, S. Mukherjee, P. J. Hirschfeld, B. M. Andersen, and J. C. S. Davis, *Science* **357**, 75 (2017).

[71] B. Béri, J. N. Kupferschmidt, C. W. J. Beenakker, and P. W. Brouwer, *Phys. Rev. B* **79**, 024517 (2009).

[72] P. Ai, Q. Gao, J. Liu, Y. Zhang, C. Li, J. Huang, C. Song, H. Yan, L. Zhao, G.-D. Liu, G.-D. Gu, F.-F. Zhang, F. Yang, Q.-J. Peng, Z.-Y. Xu, and X.-J. Zhou, *Chinese Physics Letters* **36**, 067402 (2019).

[73] R. R. d. Santos, *Braz. J. Phys.* **33**, 36 (2003).