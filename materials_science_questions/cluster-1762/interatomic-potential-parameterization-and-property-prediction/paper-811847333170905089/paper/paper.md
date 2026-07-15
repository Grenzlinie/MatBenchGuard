# Thermal conductivity of ZnTe investigated by molecular dynamics

Hanfu Wang*, Weiguo Chu*

National Center for Nanoscience and Technology of China, Beijing 100190, China

---

## ARTICLE INFO

**Article history:**
Received 15 April 2009
Accepted 31 May 2009
Available online 6 June 2009

**Keywords:**
ZnTe
Molecular dynamics simulation
Thermal conductivity
Tersoff's potential
Green-Kubo formulism

---

## ABSTRACT

The thermal conductivity of ZnTe with zinc-blende structure has been computed by equilibrium molecular dynamics method based on Green-Kubo formalism. A Tersoff's potential is adopted in the simulation to model the atomic interactions. The calculations are performed as a function of temperature up to 800 K. The calculated thermal conductivities are in agreement with the experimental values between 150 K and 300 K, while the results above the room temperature are comparable with the Slack's equation.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Understanding thermal transport in solids is fundamentally important in developing various electronics, optoelectronics and thermoelectrics [1–3]. For intrinsic or moderate-doped semiconductors, heat transfer is mainly contributed by phonon transport, or lattice vibration, which has been addressed carefully by analytical models [4,5]. In recent years, molecular dynamics (MD) simulation has emerged to be a powerful tool to predict the lattice thermal conductivity [6–20]. One major advantage of this method is that it does not rely on too many approximations and assumptions that require a deep understanding of the detailed phonon processes. An essential ingredient of the method is the empirical potential field that describes atomic interactions within the system. In practice, the MD method falls into two categories: equilibrium molecular dynamics (EMD) [6–15] and non-equilibrium molecular dynamics (NEMD) [10,16–20]. The EMD simulation records the heat flux fluctuations and computes the thermal conductivity using the Green-Kubo fluctuation–dissipation theorem. In a NEMD simulation, the thermal conductivity is calculated from temperature gradient and heat flux across the system via the Fourier's law. The NEMD method has been used widely to characterize the heat transfer in nanostructures [19,20]. But it suffers finite-size problem when calculating bulk thermal conductivity and extrapolation of the obtained data to the infinite size of the simulation cell is typically needed [10,20]. On the other hand, the EMD method seems to be a favorable choice to obtain the bulk thermal conductivity. Although it requires longer simulation time, the convergence can be achieved at a simulation cell size that is much smaller than the phonon mean free path [11,15].

ZnTe is an important II–VI compound semiconductor which has potential applications in many important technological fields [21–23]. Theoretical investigations have been carried out by several groups to explore its structures, thermodynamics, phase transition properties [24–28]. However, only few theoretical studies have been devoted to explore the heat transfer in ZnTe and these works are mainly based on the analytical models [29,30].

In the present study, we use the EMD method to evaluate the bulk lattice thermal conductivity of ZnTe with zinc-blende structure as a function of temperature. We choose Tersoff's potential to model the atomic interactions in the ZnTe crystal and adopt a set of parameters proposed by Kanoun et al. for the potential [28]. The Tersoff's potential has been known to give satisfactory structural and energetic properties when treating covalent semiconductors [31–34]. It has also been employed to calculate the thermal conductivity of various semiconductors like β-SiC [6], Ge and Ge₄₆ clathrate [9], and ZnSe [14]. The main objective of this study is to test the possibility of extending the potential to investigate the thermal transport property of ZnTe. In the simulations, we include the temperature correction to account for the quantum effect. The thermal conductivities are evaluated over a temperature range of 100–800 K. The calculated results are in reasonable agreement with the available experimental data above 150 K. To our best knowledge, no experimental data above the room temperature is available for ZnTe. We then compare the MD results in this temperature range with the prediction of the Slack's equation [35] and find the overall agreement is quite satisfactory.

---

* Corresponding authors. Fax: +86 10 62656765.
E-mail addresses: wanghf@nanoctr.cn (H. Wang), wgchu@nanoctr.cn (W. Chu).

0925-8388/$ – see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.jallcom.2009.05.146

### 2. Computational methods

The parameters of the Tersoff's model used in this work are taken from Ref. [28]. For more details about the potential, please refer to that paper.

Before performing the MD simulations, we carry out the static lattice dynamics calculations to obtain the equilibrium lattice constant, cohesive energy, elastic constants and phonon density of states (PDOS) of ZnTe using the General Utility Lattice Program (GULP) code [36]. In the calculations, we use a $4 \times 4 \times 4$ supercell containing 512 atoms as a simulation box. The structure is optimized by the GULP code and the obtained lattice constant is taken as input parameter for the latter MD simulations. In order to get the phonon density of states, a $20 \times 20 \times 20$ Monkhorst–Pack grid [37] is employed for the Brillouin zone integration.

The MD code used in this study is modified from a Fortran program originally developed by Li and his co-workers for studying the thermal properties of $\beta$-SiC [6,34].

In a MD simulation, the system is described by the classical statistical mechanics which is inadequate to reflect the quantum effects such as the zero-point vibration that becomes dominant below the Debye temperature. In order to investigate the properties in the low temperature regime, a correction can be made to take into account of the quantum effects. In this study, the correction is done by employing a method proposed by Wang et al. [38] in which the temperature T of the "real" quantum system is scaled to the temperature $T_{\text{MD}}$ of the classical system by requiring the mean kinetic energy of both systems to be equal. The idea is expressed as

$$
T_{\mathrm{MD}}=\frac{1}{k_{\mathrm{B}}} \int_{0}^{\omega_{\mathrm{MAX}}} \hbar \omega\left(\frac{1}{2}+\frac{1}{e^{\hbar \omega / k_{\mathrm{B}} T}-1}\right) D(\omega) \mathrm{d} \omega \tag{1}
$$

where $D(\omega)$ is the PDOS obtained from the lattice dynamics calculation, $\omega$ the frequency, $\hbar$ the Planck's constant, and $k_{\text{B}}$ the Boltzmann's constant, $T$ the absolute temperature.

The MD calculations are run under the isobaric and isothermal ensemble (NPT) by applying the constant pressure algorithm of Parrinello and Rahman [39]. The temperature is maintained at the indicated value through a thermal bath. The simulations are performed with periodic boundary condition applied. The evolution of the system is controlled by solving the Newtonian equations with the Gear–Predictor–Corrector algorithm [40]. The initial velocities of the atoms are assigned according to the Maxwellian distribution. All the simulations are run at zero external pressure for total $1.7 \times 10^{7}$ steps at a time step of 0.764 fs. The system is allowed to relax to reach the equilibrium at the indicated temperature for $1.4 \times 10^{5}$ time steps in the NTP ensemble. The subsequent simulation is continued in a microcanonical (NVE) ensemble in which the instantaneous heat current $\vec{J}(\vec{t})$ [6] is decided.

$$
\vec{J}(\vec{t})=\sum_{i}\left(\left(E_{i}-h\right) \vec{v}_{i}+\sum_{j \neq i} \vec{r}_{i j}\left(\frac{\partial E_{i}}{\partial \vec{r}_{j}} \cdot \vec{v}_{j}\right)\right) \tag{2}
$$

where $E_{i}$ is the internal energy of atom $i$, $\vec{v}_{i}$ the atomic velocity, $\vec{r}_{i}$ the atomic coordinate, $h$ the average enthalpy per atom.

The MD thermal conductivity $\kappa_{\text{MD}}$ is calculated based on the Green–Kubo formula [9]:

$$
\kappa_{\mathrm{MD}}=\int_{0}^{\infty} G(t) \mathrm{d} t=\frac{1}{3 k_{\mathrm{B}} T_{\mathrm{MD}}^{2} V} \int_{0}^{\infty} \sum_{\alpha=x, y, z}\left\langle J_{\alpha}(t) J_{\alpha}(0)\right\rangle \mathrm{d} t \tag{3}
$$

where $\alpha$ denotes the three Cartesian coordinates, $\langle J_{\alpha}(t) J_{\alpha}(0)\rangle$ is the heat current autocorrelation function (HCACF), $V$ the volume. The HCACF is derived from the instantaneous heat current $\vec{J}(\vec{t})$ data at the end of MD run by employing fast Fourier-transform and spectral techniques [6,41]. Following the notation in Ref. [9], a normalized correlation function $g(t)$ can be defined as $g(t)=G(t) / G(0)$. The MD thermal conductivity $\kappa_{\text{MD}}$ is then obtained by integrating $g(t)$:

$$
\kappa_{\mathrm{MD}}=G(0) \int_{0}^{\infty} g(t) \mathrm{d} t \tag{4}
$$

To yield the thermal conductivity $\kappa$ of the real system, $\kappa_{\text{MD}}$ needs to be corrected by multiplying a temperature gradient factor $\mathrm{d}T_{\text{MD}}/\mathrm{d}T$ [6] as shown in the following:

$$
\kappa=\kappa_{\mathrm{MD}} \frac{\mathrm{d} T_{\mathrm{MD}}}{\mathrm{d} T}=G(0) \frac{\mathrm{d} T_{\mathrm{MD}}}{\mathrm{d} T} \int_{0}^{\infty} g(t) \mathrm{d} t=K(0) \int_{0}^{\infty} g(t) \mathrm{d} t \tag{5}
$$

To minimize the statistical errors, the final result of $\kappa$ is averaged from the outputs of several independent MD runs with different initial configurations.

<table>
<caption>Table 1<br>Static structural, energetic and elastic properties of zinc-blende ZnTe.</caption>
<thead>
<tr>
<th></th>
<th>GULP</th>
<th>Literature¹</th>
<th>Experimental</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lattice constant (Å)</td>
<td>6.104</td>
<td>6.117</td>
<td>6.104ᵇ</td>
</tr>
<tr>
<td>Atomic volume (Å³/atom)</td>
<td>28.433</td>
<td>–</td>
<td>28.36ᶜ</td>
</tr>
<tr>
<td>Cohesive energy (eV/atom)</td>
<td>2.284</td>
<td>2.285</td>
<td>–</td>
</tr>
<tr>
<td>Bᵉ (GPa)</td>
<td>51.42</td>
<td>50.9</td>
<td>50.9</td>
</tr>
<tr>
<td>Gᵉ (GPa)</td>
<td>15.85</td>
<td>14.2</td>
<td>23.4</td>
</tr>
<tr>
<td>C₁₁ (GPa)</td>
<td>63.44</td>
<td>64.0</td>
<td>71.3ᵈ</td>
</tr>
<tr>
<td>C₁₂ (GPa)</td>
<td>45.42</td>
<td>44.3</td>
<td>40.7ᵈ</td>
</tr>
<tr>
<td>C₄₄ (GPa)</td>
<td>23.14</td>
<td>18.1</td>
<td>31.2ᵈ</td>
</tr>
</tbody>
</table>

¹ Ref. [28].<br>
ᵇ Ref. [42].<br>
ᶜ Ref. [43]. Calculated from the density value at 4 K.<br>
ᵈ Ref. [44].<br>
ᵉ Isotropic bulk modulus and shear modulus are calculated according to the Eqs. (8) and (11), respectively.

### 3. Results and discussion

#### 3.1. Static properties

We evaluate the structural, energetic and elastic properties of the zinc-blende ZnTe structure with the GULP code and compare the results with the experimental [42–44] and theoretical [28] data. As shown in Table 1, the agreement is satisfactory, which assures us that the Tersoff's model is able to determine the static structural and energetic properties of ZnTe reasonably well.

Next we make use of the elastic constants $C_{ij}$ to estimate the Debye temperature $\Theta_{\text{D}}$ that is an important parameter for characterizing the thermodynamic behaviors of the crystals. It can be obtained from the Robie and Edwards relation [45]:

$$
\Theta_{\mathrm{D}}=\frac{\hbar}{k_{\mathrm{B}}}\left(\frac{6 \pi^{2}}{\Omega_{\mathrm{at}}}\right)^{1 / 3} \bar{v} \tag{6}
$$

where $\Omega_{\text{at}}$ is the atomic volume, $\bar{v}$ the average phonon velocity given by the following [46]:

$$
\bar{v}=\left[\frac{1}{3}\left(\frac{3 \rho}{3 B+4 G}\right)^{3 / 2}+\frac{2}{3}\left(\frac{\rho}{G}\right)^{3 / 2}\right]^{-1 / 3} \tag{7}
$$

where B is the isotropic bulk modulus, G the isotropic shear modulus, $\rho$ the density.

A cubic lattice has three independent elastic constants $C_{11}$, $C_{12}$ and $C_{44}$. In this case, the isotropic bulk modulus $B$ is equal to the single crystal bulk modulus $B_{\text{S}}$ that is given as the combination of $C_{11}$ and $C_{12}$:

$$
B_{\mathrm{S}}=\frac{1}{3}\left(C_{11}+2 C_{12}\right) \tag{8}
$$

The isotropic shear modulus $G$ is obtained by averaging the Reuss shear modulus $G_{\text{R}}$ and the Voigt shear modulus $G_{\text{V}}$ under the Reuss–Voigt–Hill approximation [46]:

$$
G_{\mathrm{R}}=\frac{5 C_{44}\left(C_{11}-C_{12}\right)}{3\left(C_{11}-C_{12}\right)+4 C_{44}} \tag{9}
$$

$$
G_{\mathrm{V}}=\frac{1}{5}\left(C_{11}-C_{12}+3 C_{44}\right) \tag{10}
$$

$$
G=\frac{1}{2}\left(G_{\mathrm{R}}+G_{\mathrm{V}}\right) \tag{11}
$$

The Debye temperature derived from the GULP $C_{ij}$ is 184 K, while the one determined from the experimental $C_{ij}$ [44] is 222 K. Since the lowest simulation temperature in our study is 100 K, the quantum effect correction is considered in the MD simulations.

![](./images/811847333170905089_1.jpg)

Fig. 1. Phonon density of states of zinc-blende ZnTe.

### 3.2. Phonon density of states and temperature scaling curve

In order to compute the temperature scaling curve, one has to know in advance the phonon density of states $D(\omega)$ which plays a central role in determining various thermodynamic properties of the crystals. Fig. 1 shows $D(\omega)$ of the zinc-blende ZnTe derived from the lattice dynamics calculation. By inserting $D(\omega)$ into Eq. (1), we obtain the temperature scaling relation between the MD temperature $T_{\text{MD}}$ and the real temperature $T$ (Fig. 2). The temperature gradient factor $\text{d}T_{\text{MD}}/\text{d}T$ is also displayed in the same figure for comparison. For the zinc-blende structure, $T=0\ \text{K}$ is corresponding to $T_{\text{MD}}=104.23\ \text{K}$, which reflects the zero-point vibration of a quantum system.

From $D(\omega)$, the heat capacity at constant volume $C_V$ can also be calculated under the harmonic approximation:

$$
C_{\mathrm{V}}=6 R \int_{0}^{\omega_{\mathrm{MAX}}}\left(\frac{\hbar \omega}{k_{\mathrm{B}} T}\right)^{2} \frac{e^{\hbar \omega / k_{\mathrm{B}} T}}{\left(e^{\hbar \omega / k_{\mathrm{B}} T}-1\right)^{2}} D(\omega) \mathrm{d} \omega \tag{12}
$$

where $R$ is the real gas constant.

Fig. 3 shows that the calculated $C_V$ curve in the low temperature region is in agreement with the experimental measurement [47]. This provides another proof that the current empirical potential is able to handle properly the energetic properties of the zinc-blende ZnTe.

![](./images/811847333170905089_2.jpg)

Fig. 2. $T_{\text{MD}}$ vs. $T$ relationship (solid line) and $\text{d}T_{\text{MD}}/\text{d}T$ vs. $T$ relationship (dashed line).

![](./images/811847333170905089_3.jpg)

Fig. 3. $C_V$ obtained from the harmonic approximation (solid line) and experimental values [47] (open circles).

### 3.3. Thermal conductivity

Fig. 4 depicts a normalized correlation function curve $g(t)$ obtained from a MD simulation run at 400 K in a $5 \times 5 \times 5$ simulation cell (1000 atoms). It shows a decay behavior over the entire time range. The thermal conductivity is calculated by performing the integration of $g(t)$ using Eq. (5). There are two typical procedures for carrying out such kind of integration [6]. The first one is to integrate $g(t)$ directly over some time range. The second one is to fit the raw $g(t)$ to an exponential decay curve over a certain time range followed by integrating the fitting curve analytically. In this work, we use the second fitting-integration method. By observing the shape of the $g(t)$ curve, we feel it can be better fitted with a double exponential decay function:

$$
g(t)=A_{1} e^{-t / \tau_{1}}+A_{2} e^{-t / \tau_{2}} \tag{13}
$$

where $A$ and $\tau$ are constants which need to be determined from the fitting procedure. By inserting Eq. (13) into Eq. (5), we have

$$
\kappa=K(0)\left(A_{1} \tau_{1}+A_{2} \tau_{2}\right) \tag{14}
$$

![](./images/811847333170905089_4.jpg)

Fig. 4. Normalized correlation function $g(t)$ at 400 K (solid line). It is fitted by a double exponential decay curve (dashed line) in the range [0–50] ps.

![](./images/811847333170905089_5.jpg)

Fig. 5. Thermal conductivity as a function of the size of the simulation cell.

The double exponential decay curve fitting method has been used previously to calculate the thermal conductivities of the diamond [8] and the argon [12] crystals.

It is known that the finite size of the simulation box affects the values of the calculated thermal conductivity to some extent when the EMD method is employed [11,15]. To test the finite-size effect, we perform the simulations at 300 K in the cubic cells of different sizes. Fig. 5 shows clearly that the thermal conductivity is converged at a cell size of 256 atoms (3 × 3 × 3 supercell). It has been reported that the thermal conductivity can achieve the convergence even the size of the simulation box is much smaller than the phonon mean free path $\lambda$ [11,15]. In our case, $\lambda$ of ZnTe can be estimated through the following expression [48]:

$$
\kappa=\frac{1}{3} C_{V} \bar{v} \lambda \quad(15)
$$

At 300 K, the thermal conductivity is taken as 18 W/m/K [49], $C_V$ as 47.51 J/(mol K) obtained from the calculation in Section 3.2, the average phonon velocity $\bar{v}$ as 2278 m/s calculated from the experimental $C_{ij}$ using Eqs. (7)-(11). The phonon mean free path is found to be $171 \AA$ which is almost one order larger than the size of a $3 \times 3 \times 3$ supercell $(18.4 \AA × 18.4 \AA × 18.4 \AA)$. The convergence with a small domain size may be due to the facts that the periodic boundary condition is utilized and the phonon energy at this temperature is mainly carried by the short wavelength phonon modes [15].

To investigate the temperature dependence of the thermal conductivity, we run all simulations in a $5 \times 5 \times 5$ simulation cell containing 1000 atoms. Fig. 6 compares the $g(t)$ curves obtained at three different temperatures. At the higher temperature, the $g(t)$ curve decay more quickly.

To obtain the thermal conductivity, the $g(t)$ curve is fitted with the double exponential decay curve within the time range $[0, t_{F}]$ ps. The value of $t_{F}$ is chosen based on the simulation temperature. At the temperature above 500 K, the $g(t)$ curve can be fitted quite well if $t_{F}$ is taken to be 30 ps. At the lower temperature, a larger $t_{F}$ should be used. After averaging the results from several independent MD runs at each temperature, the final thermal conductivities are plotted in Fig. 7. The experimental data plotted in the same figure are taken from Table 2 of Ref. [49] in which the thermal conductivities of ZnTe were measured up to 300 K. Fig. 7 demonstrates that the MD results are in reasonable agreement with the experimental results between 150 K and 300 K, while a significant deviation is observed below 150 K. The underestimation of thermal conductivity in low temperature region has previously been observed by Li et al. in studying the heat transfer of $\beta$-SiC using the EMD method [6]. They suggested that long wavelength phonons become more important in terms of heat carrying capability at low temperatures. The finite size of the simulation cell will cause the scatterings of these long wavelength phonons, which in turn decrease the thermal conductivity. Also, it will take a longer time for the phonons to reach equilibrium at low temperatures. As a result, significantly longer simulations may be needed to get reliable low temperature thermal conductivities.

![](./images/811847333170905089_6.jpg)

Fig. 6. Comparison of $g(t)$ curves (solid lines) at three different temperatures. They are fitted by the double exponential decay curves (dashed lines).

Though the experimental data above 300 K are not available to us, the calculated thermal conductivity demonstrates clearly a decay trend as the temperature increases. At higher temperature regime where the Umklapp process dominates, empirical model like Slack's equation [35] provides a good approximation for the intrinsic thermal conductivity. One assumption of this model is that optic phonon modes do not contribute to the heat transfer and the thermal conductivity is dominated by the acoustic phonon modes.

**Table 2**
The values of the Slack's equation parameters for ZnTe (Ref. [35]).

<table>
<thead>
<tr>
<th>$\theta_{a}$ (K)</th>
<th>$\gamma$</th>
<th>$\delta$ (Å)</th>
<th>$\overline{M}$ (amu)</th>
<th>$n$</th>
</tr>
</thead>
<tbody>
<tr>
<td>155</td>
<td>0.97</td>
<td>3.05</td>
<td>96.49</td>
<td>2</td>
</tr>
</tbody>
</table>

![](./images/811847333170905089_7.jpg)

Fig. 7. Thermal conductivities of ZnTe as a function of temperature.

The equation can be expressed as [35]:
$$
\kappa=A \frac{\bar{M} \theta_{\mathrm{a}}^{3} \delta^{3} n^{1 / 3}}{\gamma^{2} T} \quad T>\theta_{\mathrm{a}}
\tag{16}
$$
where $\gamma$ is the Grüneissen parameter in the high temperature, $\bar{M}$ (amu) the average atomic mass, $\theta_{\mathrm{a}}(\mathrm{K})$ the acoustic Debye temperature, $\delta^{3}\left(\AA^{3}\right)$ the average volume per atom, $n$ the number of atoms in each primitive cell, $A=2.43 \times 10^{-6} /\left(1-0.514 / \gamma+0.228 / \gamma^{2}\right)$ for thermal conductivity in $\mathrm{W} / \mathrm{m} / \mathrm{K}$.

The thermal conductivity curve calculated by the Slack's equation is displayed in Fig. 7 in comparison with the MD results and experimental data. The values for the parameters in Eq. (16) are obtained from Ref. [35] and are listed in Table 2. At 300 K, the thermal conductivity computed from the Slack's equation is 17 W/m/K, which is very close to the experimental value. Above the room temperature, the agreement between the MD results and the Slack's equation is satisfactory, especially in the temperature range above 500 K. Since the thermal conductivity of perfect crystals in the high temperature range is dominated by the Umklapp process, our calculations suggest that the current empirical potential presents a reliable description on the anharmonic phonon-phonon interactions in the ZnTe crystal.

Compared with the potential field of ZnTe that includes the two- body interactions [27], the Tersoff's model used in the present work is relatively simple. However, the calculation of the bulk thermal conductivity based on this model generates reasonable results that are comparable with the experimental data and the Slack's equation above 150 K.

## 4. Conclusions
In this work, the thermal conductivity of ZnTe in zinc-blende structure has been calculated by using the EMD approach in conjunction with the Tersoff's potential. It is found that the finite-size effects are not severe. Reasonable agreement has been achieved between the calculated thermal conductivity and the experimental data in a temperature range of 150-300 K. Above the room temperature, the MD results are consistent with the Slack's model. This suggests that the Tersoff's potential used in the current work can describe the anharmonic phonon-phonon interactions in the ZnTe crystal reliably. This lays a foundation for using the EMD method to handle the thermal transport property of ZnTe and other II-VI compounds properly.

## Acknowledgments
This work is sponsored by the Scientific Research Foundation for the Returned Overseas Chinese Scholars, State Education Ministry of China, and the National Science Foundation of China under grant no. 50672017. We also gratefully acknowledge the computational supports from the Shanghai Supercomputer Center. We especially thank Prof. Ju Li in Ohio State University, US for allowing us to modify and use the MD code developed by him and his co-workers in this work.

## References
[1] K.E. Goodson, Y.S. Ju, Annu. Rev. Mater. Sci. 29 (1999) 261.
[2] W.R. Smith, J. Appl. Phys. 87 (2000) 8276.
[3] D.T. Morelli, V. Jovovic, J.P. Heremans, Phys. Rev. Lett. 101 (2008) 035901.
[4] J. Callaway, Phys. Rev. 113 (1959) 1046.
[5] M.G. Holland, Phys. Rev. 132 (1963) 2461.
[6] J. Li, L. Porter, S. Yip, J. Nucl. Mater. 255 (1998) 139.
[7] S.G. Volz, G. Chen, Phys. Rev. B 61 (2000) 2651.
[8] J. Che, T. Çağın, W. Deng, W.A. Goddard III, J. Chem. Phys. 113 (2000) 6888.
[9] J. Dong, O.F. Sankey, C.W. Myles, Phys. Rev. Lett. 86 (2001) 2361.
[10] P.K. Schelling, S.R. Phillpot, P. Keblinski, Phys. Rev. B 65 (2002) 144306.
[11] K.V. Tretiakov, S. Scandolo, J. Chem. Phys. 120 (2004) 3765.
[12] A.J.H. McGaughey, M. Kaviany, Int. J. Heat Mass Transfer 47 (2004) 1783.
[13] A.J.H. McGaughey, M. Kaviany, Int. J. Heat Mass Transfer 47 (2004) 1799.
[14] A.K. Balasubramanian, N. Sankar, S.K. Ramakrishnan, K. Ramachandran, Cryst. Res. Technol. 39 (2004) 558.
[15] L. Sun, J.Y. Murthy, Appl. Phys. Lett. 89 (2006) 171919.
[16] F. Müller-Plathe, J. Chem. Phys. 106 (1997) 6082.
[17] P. Jund, R. Jullien, Phys. Rev. B 59 (1999) 13707.
[18] Y.-G. Yoon, R. Car, D.J. Srolovitz, Phys. Rev. B 70 (2004) 012302.
[19] C.W. Padgett, O. Shenderova, D.W. Brenner, Nano Lett. 6 (2006) 1827.
[20] N. Papanikolaou, J. Phys.: Condens. Matter 20 (2008) 135201.
[21] D. Rioux, D.W. Niles, H. Höchst, J. Appl. Phys. 73 (1993) 8381.
[22] K. Sato, M. Hanafusa, A. Noda, A. Arakawa, M. Uchida, T. Asahi, O. Oda, J. Cryst. Growth 214-215 (2000) 1080.
[23] B. Späth, J. Fritsche, F. Säuberlich, A. Klein, W. Jaegermann, Thin Solid Films 480-481 (2005) 204.
[24] G.-D. Lee, M.H. Lee, J. Ihm, Phys. Rev. B 52 (1995) 1459.
[25] G.-D. Lee, J. Ihm, Phys. Rev. B 53 (1996) R7622.
[26] M. Côté, O. Zakharov, A. Rubio, M.L. Cohen, Phys. Rev. B 55 (1997) 13025.
[27] D.S. Borges, J.P. Rino, Phys. Rev. B 72 (2005) 014107.
[28] M.B. Kanoun, A.E. Merad, H. Aourag, J. Cibert, G. Merad, Solid State Sci. 5 (2003) 1211.
[29] R.D. Bijalwan, P.N. Ram, M.D. Tiwari, J. Phys. C: Solid State Phys. 16 (1983) 2537.
[30] N. Mingo, Appl. Phys. Lett. 85 (2004) 5986.
[31] J. Tersoff, Phys. Rev. Lett. 56 (1986) 632.
[32] M. Sayed, J.H. Jefferson, A.B. Walker, A.G. Cullis, Nucl. Instr. Meth. Phys. Res. B 102 (1995) 232.
[33] L.J. Porter, S. Yip, M. Yamaguchi, H. Kaburaki, M. Tang, J. Appl. Phys. 81 (1997) 96.
[34] L.J. Porter, J. Li, S. Yip, J. Nucl. Mater. 246 (1997) 53.
[35] D.T. Morelli, G.A. Slack, in: S. Shinde, J. Goela (Eds.), High Thermal Conductivity Materials, Springer-Verlag, New York, 2005.
[36] J.D. Gale, J. Chem. Soc. Faraday Trans. 93 (1997) 629.
[37] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[38] C.Z. Wang, C.T. Chan, K.M. Ho, Phys. Rev. B 42 (1990) 11276.
[39] M. Parrinello, A. Rahman, J. Appl. Phys. 52 (1981) 7182.
[40] M.P. Allen, D.J. Tildesley, Computer Simulation of Liquids, Clarendon Press, Oxford, 1987.
[41] J. Li, J. Computer-Aided Mater. Design 12 (2005) 141.
[42] W.L. Roth, in: M. Aven, J.S. Prener (Eds.), Physics and Chemistry of II-VI Compounds, North-Holland, Amsterdam, 1967.
[43] J.G. Collins, G.K. White, J.A. Birch, T.F. Smith, J. Phys. C: Solid State Phys. 13 (1980) 1649.
[44] D. Berlincourt, H. Jaffe, L.R. Shiozawa, Phys. Rev. 129 (1963) 1009.
[45] R.A. Robie, J.L. Edwards, J. Appl. Phys. 37 (1966) 2659.
[46] H.M. Ledbetter, J. Appl. Phys. 44 (1973) 1451.
[47] J.C. Irwin, J. LaCombe, J. Appl. Phys. 45 (1974) 567.
[48] J.M. Ziman, Principles of the Theory of Solids, Cambridge University Press, Cambridge, 1972.
[49] G.A. Slack, Phys. Rev. B 6 (1972) 3791.