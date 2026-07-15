A study of vibrational modes in $Na^+$ beta -alumina by molecular dynamics simulation

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1994 J. Phys.: Condens. Matter 6 1319

(http://iopscience.iop.org/0953-8984/6/7/005)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 170.140.26.180
This content was downloaded on 23/08/2015 at 16:37

Please note that terms and conditions apply.

# A study of vibrational modes in $Na^{+} \beta$-alumina by molecular dynamics simulation

Sverker Edvardsson, Lars Ojamäe and John O Thomas
Institute of Chemistry, University of Uppsala, Box 531, S-751 21 Uppsala, Sweden

Received 3 August 1993, in final form 10 November 1993

Abstract. The vibrational properties of crystalline $Na^{+} \beta$-alumina $(Na_{1.22} Al_{11} O_{17.11})$ have been studied using the molecular dynamics simulation technique. The vibrational density of states was calculated from the velocity autocorrelation function, and the infrared spectrum from the dipole-dipole autocorrelation function. Knowledge of the vibrations in different crystallographic directions for the different atomic species facilitates the assignment of spectral peaks. The sodium in-plane vibrations are 59,88 and $112 ~cm^{-1}$ , and the out-of-plane vibrations are at $146 ~cm^{-1}$ . The stoichiometric compound is also studied, and in this case the sodium in-plane vibrations are at $80 ~cm^{-1}$ and the out-of-plane vibrations at $140 ~cm^{-1}$ . The density of states is used to calculate thermodynamic properties: heat capacity, entropy and internal and free energy. The values obtained at $300 ~K$ are $C_{v}=410 ~J ~K^{-1} ~mol^{-1}, S_{v}=300 ~J ~K^{-1} ~mol^{-1}$ , $U=370 ~kJ ~mol^{-1}$ and $F=280 ~kJ ~mol^{-1}$ . The heat capacity and entropy values are in good agreement with experiment, and thus strongly support the empirical force field used in the simulation.

## 1. Introduction

The $\beta$-alumina family of compounds has been studied extensively during the last 25 years.The exceptionally high ionic conductivity of $Na^{+} \beta$ -alumina $(\sigma=1.4 \times 10^{-2} \Omega^{-1} ~cm^{-1}$  at $300 ~K$ ) was first noted by Yao and Kummer in 1967 [1], and it has since played a significant role as solid electrolyte in the development of the $Na / S$ battery. The material comprises a rigid layered framework of aluminium oxide (spinel blocks), interleaved and separated by two-dimensional layers containing a hexagonal arrangement of bridging oxygen ions $(O(5))$ , together with the mobile cations: $Na^{+}, Ag^{+}, Li^{+}$ , etc (see figure $1(a)$ ). It is within these layers that the two-dimensional fast-ion conduction can occur. In this work, we focus on non-stoichiometric $Na^{+} \beta$ -alumina with composition $Na_{1+x} Al_{11} O_{17+x / 2}$ , where $x=0.22$ . The $Na^{+}$ ions are known to occupy two sites (see, for example, [2]): $\sim 60 \%$  in so-called BR sites, and $\sim 40 \%$ between aBR and mO sites (figure $1(b)$ ). The charge compensating oxygens $(O_{i}^{2-})$ occupy $mO$ sites bonded to $Al^{3+}$ ions displaced towards O2 from their normal sites near the edge of the spinel block. The structure has the hexagonal space group $P 6_{3} / mmc$ with room-temperature lattice parameters $a=5.56 \AA$ and c = 22.56 A. The molecular dynamics (MD) simulation technique was applied to obtain the vibrational density of states (DOS), which, in turn, is used to calculate various thermodynamic quantities. The infrared (IR) spectrum was also calculated and compared with experiment[10-12]. Assignments are made of modes in different crystallographic directions, and the contributions to each mode from the different ionic species are ascertained. A complementary calculation of the stoichiometric $(x=0) \beta$ -alumina made it possible to investigate the frequency shift of sodium ions due to the interstitial oxygen $(O_{i}^{2-})$ . A number of thermodynamic properties have been calculated in the case $x=0.22$ .

![](./images/811973560019976192_1.jpg)

Figure 1. The structure of $Na^+$ $\beta$-alumina showing the spinel blocks interleaved by two- dimensional conduction planes (a), and a schematic representation of the sites in the conduction planes (b).

## 2. Molecular dynamics simulation

MD is a well established computer simulation technique used earlier to study the dynamics of the $\beta/\beta''$-alumina systems [3,4,17,20] (see also the article by Sangster and Dixon [21] for a more thorough review of MD than presented here). In the method, it is assumed that atomic motion can be treated by classical dynamics. The ions interact through appropriate potential functions, and their trajectories are obtained by the numerical solution of the coupled Newton's equations of motion of all particles. Here, the total energy $E$, the number $N$ of particles and the volume $V$ are fixed corresponding to the microcanonical ensemble of statistical mechanics. The interaction potential $V_{ij}(r)$ between two ions $i$ and $j$ was assumed to have the Born-Mayer-Huggins form:

$$
V_{ij}(r)=q_{i}q_{j}/r_{ij}+A_{ij}\exp(-r_{ij}/\rho_{ij})-C_{ij}/r_{ij}^{6}. \tag{1}
$$

The first term represents the long-range coulombic interaction; the second a repulsive short- range interaction; the third term is the weak van der Waal interaction. The $A_{ij}$, $\rho_{ij}$ and $C_{ij}$ parameters were derived by empirical fitting by Walker and Catlow [5] to reproduce bulk

crystal properties such as elastic and dielectric constants for $\text{Al}_2\text{O}_3$, and to predict correctly the lattice parameter of $\text{Na}_2\text{O}$. The MD program used in this study is a local modification of their program FUNGUS [19]. The $q$ parameters are the full ionic charges (i.e. +3, +1, $-2$ for $\text{Al}$, $\text{Na}$, $\text{O}$, respectively), and $r_{ij}$ is the distance between ions $i$ and $j$. Periodic boundary conditions are imposed to simulate an infinite system. The long-range coulombic interactions are evaluated by the Ewald summation procedure [6]. The simulation box comprised $3a \times 3b \times 1c$ unit cells involving $308\ \text{O}^{2-}$, $198\ \text{Al}^{3+}$ and $22\ \text{Na}^+$ ions, and in the stoichiometric case, $306\ \text{O}^{2-}$, $198\ \text{Al}^{3+}$ and $18\ \text{Na}^+$. The time-step used in the simulation is 2.5 fs. To attain the desired temperature (300 K), the system was equilibrated for 2000 time-steps (scaling every 100 steps); the simulation$\dagger$ then ran for 40 000 time-steps, corresponding to a simulation time of 100 ps. Both dipole moments and velocities were stored throughout for subsequent analysis.

### 3. Calculation of vibrational properties

According to linear response theory, spectral properties can be obtained from the appropriate autocorrelation functions [7]. The vibrational (DOS) spectrum is taken to be the Fourier transform of the velocity autocorrelation function:

$$
\rho(\nu) \propto \int_{0}^{\infty} \frac{\langle V(0) V(t)\rangle}{\left\langle V(0)^{2}\right\rangle} \cos 2 \pi \nu t \mathrm{~d} t \tag{2}
$$

where $V(t)$ is the velocity of an atom and the velocity autocorrelation function (VACF) is assumed to be real; $\rho(\nu)$ is normalized according to

$$
\int_{0}^{\infty} \rho(\nu) \mathrm{d} \nu=3 N \tag{3}
$$

where $N$ is the total number of particles in the simulation box:

$$
N=N_{\mathrm{Na}}+N_{\mathrm{Al}}+N_{\mathrm{O}}. \tag{4}
$$

The IR absorption line-shape function $I(\nu)$ is obtained from the dipole moment autocorrelation function of the system [7] by

$$
I(\nu) \propto \nu\left(1-\mathrm{e}^{-\beta h \nu}\right) \int_{-\infty}^{\infty}\langle\vec{\mu}(0) \vec{\mu}(t)\rangle \mathrm{e}^{-\mathrm{i} 2 \pi \nu t} \mathrm{~d} t \tag{5}
$$

where $\vec{\mu}(t)$ is the dipole moment of the system along the direction of the electric field of the incident radiation.

Velocities (for each ionic species) and the total dipole moment of the simulation box were calculated every 10 fs during the simulation, and then used to construct their autocorrelation functions; Fourier transformation gives the DOS and IR spectra, respectively. For the calculation of the DOS, we used $22\ \text{Na}^+$ (all), $20\ \text{O}^{2-}$ in the planes (all), and $20\ \text{O}^{2-}$ and $20\ \text{Al}^{3+}$ (well distributed) in the spinel blocks. All ions were included in the calculation of the IR spectra.

$\dagger$ All runs were made on a PC (EISA i486DX2-66 MHz) operating under Interactive Unix version 3.2 (Sunsoft) with five i860 processors (Microway); peak performance: 285 Mflops.

## 4. Calculation of thermodynamic properties

The calculated DOS at 300 K is used to derive a number of thermodynamic quantities. The phonon heat capacity for harmonic oscillators is given by [8]

$$
C_{v}(T)=\frac{1}{k_{\mathrm{B}}} \int_{0}^{\nu_{\max }}\left(\frac{h \nu}{\exp \left(h \nu / k_{\mathrm{B}} T\right)-1}\right)^{2} \frac{\exp \left(h \nu / k_{\mathrm{B}} T\right)}{T^{2}} \rho(\nu) \mathrm{d} v
\tag{6}
$$

where $k_{\mathrm{B}}$ is Boltzmann's constant, $\nu_{\max }$ is the highest frequency recorded in the $\rho(\nu)$ spectrum (i.e. DOS), $h$ is Planck's constant and $T$ the temperature. To compare with experimental heat capacities (usually obtained at constant pressure), we have derived $C_{p}$ from the theoretical $C_{v}$ by the relation

$$
C_{p}(T)=C_{v}(T)+\frac{\beta^{2} v T}{\kappa_{T}}
\tag{7}
$$

where $v$ is the volume of the system, $\beta$ the coefficient of volume expansion, and $\kappa_{T}$ the isothermal compressibility. These parameters were taken from experimental data [13,14].
The entropy $S$ is calculated from

$$
S_{i}(T)=\int_{0}^{T} \frac{C_{i}(\tau)}{\tau} \mathrm{d} \tau
\tag{8}
$$

where the index $i$ is replaced by $v$ or $p$ depending on whether constant volume ($v$) or constant pressure ($p$) is considered.

The expression for the internal energy $U$ is

$$
U(T)=\int_{0}^{\nu_{\max }}\left(\frac{h v}{2}+\frac{h v}{\exp \left(h \nu / k_{\mathrm{B}} T\right)-1}\right) \rho(\nu) \mathrm{d} \nu.
\tag{9}
$$

The Helmholtz free energy $F$ is given by

$$
F(T)=U(T)-T S(T).
\tag{10}
$$

The standard way to calculate heat capacity in an MD simulation is to use the expression obtained by Lebowitz et al [9], which is valid for a classical system:

$$
C_{v}(T)=\frac{3 / 2 N k_{\mathrm{B}}}{1-2\left(\left\langle E_{k}^{2}\right\rangle-\left\langle E_{k}\right\rangle^{2}\right) / 3 N k_{\mathrm{B}}^{2} T^{2}}.
\tag{11}
$$

We can note that (11) only applies at rather high temperatures (especially for $\beta$-alumina), and that it is also necessary to perform several MD simulations at different temperatures, and recalculate the kinetic energy variations in evaluating $C_{v}(T)$. This is not so for (6), since the DOS is assumed not to vary significantly with temperature (harmonic approximation), i.e., one simulation at a given temperature is sufficient to obtain $C_{v}$ at virtually any other temperature.

A number of approximations are made in our calculations. The DOS is obtained from an MD procedure, which is reasonable provided that a good set of potentials is used. Harmonic quantum oscillators are assumed; this is an appropriate approximation for temperatures as low as 300 K. The simulation box should be chosen as large as possible to provide the appropriate degrees of freedom. The statistics could be improved by using longer MD runs; and not all ions are included in the calculation of the DOS.

## 5. Results and discussion

### 5.1. Molecular dynamics

The trajectories within the lower conduction plane during 5000 time-steps of MD simulation at 300 K are shown in figure 2. The oxygen ions are seen to vibrate around their equilibrium sites. The sodium ions are much more mobile, although significant diffusion is not observed at room temperature during this small time window, i.e. 12.5 ps. It is interesting to note that most of the $Na^+$ ions are located near the BR sites, and only one is at an aBR site. The clearest examples of occupation of a site between the aBR and mO sites are the two sodiums located in the same cell as the interstitial oxygen ($O_i^{2-}$). The two column oxygens (O(5)) adjacent to $O_i^{2-}$ are somewhat displaced in the $a$ direction due to the repulsion they experience from the interstitial oxygen. These results are all in qualitative agreement with the x-ray diffraction results of Edström *et al* [2].

![](./images/811973560019976192_2.jpg)

Figure 2. The trajectories of both sodium and column oxygen (O(5)) ions in the $Na^+$ $\beta$-alumina conduction plane ($z = \frac{1}{4}$) during 5000 time-steps at 300 K. The interstitial oxygen is situated at the mO site (indicated as $O_i$). See figure 1(b) to associate trajectories with specific ions.

### 5.2. Vibrational properties

We shall here concentrate on vibrational frequencies only; intensities can be difficult to compare with experiment, since they are sensitive to the experimental conditions (stoichiometry, sample preparation, thermal history, water content, etc). In an MD simulation, we treat an ideal material usually containing perfect ions interacting through a model potential. It will be shown, nevertheless, that agreement between simulation and experiment is surprisingly good.

The far-IR spectra (5) for the stoichiometric and non-stoichiometric cases are plotted in figure 3 for both the $a(\cong b)$ and $c$ directions. The total spectra in figure 3(a, b) can be directly compared with figure 6(b, c) in the paper of Colomban *et al* [10]. In the $a$ direction, we can compare our figure 3(a) and (b) with figure 5(c) and figure 3(a) respectively, in the paper of Hayes and Holden [11]. Let us first concentrate on the non-stoichiometric case and the total spectrum ($I_{\text{tot}} = I_a + I_b + I_c$). Below $200\ \text{cm}^{-1}$, essentially six bands appear at 59, 88, 115, 146, 162 and $192\ \text{cm}^{-1}$. Colomban *et al* report experimental bands at $60\ (\text{E}_{1\text{u}})$, 100 (Frenkel defect) and $166\ (\text{A}_{2\text{u}})$ and an unidentified band around $220\ \text{cm}^{-1}$ in an IR spectrum at 300 K, although they worked with a slightly different composition ($x = 0.25$). Figure 3(a) clearly shows that the peaks seen at 59 and $88\ \text{cm}^{-1}$ correspond to in-plane vibrations, and those at 146, 162 and $192\ \text{cm}^{-1}$ to out-of-plane vibrations, whereas that at $115\ \text{cm}^{-1}$ is a mixed band. The IR spectra in the $a$ direction below $200\ \text{cm}^{-1}$ exhibit four peaks at 59, 88, 112 and $175\ \text{cm}^{-1}$. Hayes and Holden [11] observe peaks at 59 and $86\ \text{cm}^{-1}$, and some low-intensity peaks at 93, 102, 137 and $178\ \text{cm}^{-1}$, in an IR study on nearly stoichiometric $\beta$-alumina with $E \perp c$. Comparing the IR ($I_{\text{tot}}$) results for the stoichiometric and non-stoichiometric $\text{Na}^+$ $\beta$-alumina cases below $200\ \text{cm}^{-1}$ (figure 3(a, b)), we find a narrowing of the bands into only two rather well defined bands for $x = 0$, with almost equal intensities at around 80 and $140\ \text{cm}^{-1}$. Colomban *et al* [10] find frequencies at 60 and $126\ \text{cm}^{-1}$. In figure 3(a) of Hayes and Holden [11], we see a band around 60 but none around $126\ \text{cm}^{-1}$ since they use polarized light (see above). Lucazeau [12] (table 1) claims that the band at $100\ \text{cm}^{-1}$ ($x = 0.25$) is an out-of-plane oscillation of the $\text{Na}^+$ ions. Figure 3(a) indicates that this is partly true, but that there is a much larger contribution from the $a$ direction. Further, the study by Colomban *et al* of the $x = 0.6$ compound [10] assigns the peaks at both 60 and $87\ \text{cm}^{-1}$ to in-plane oscillations. For the $x = 0.25$ compound, they assign the peak at $60\ \text{cm}^{-1}$ to in-plane vibrations, but their assignment of the $100\ \text{cm}^{-1}$ band is less clear. They claim that it arises from modes associated with the interstitial oxygens and the aluminium ions (Frenkel defect), using the argument that the band is not observed for the $x = 0$ compound.

<table>
<caption>Table 1. A summary of IR spectral band assignments at room temperature (for the non-stoichiometric case) made on the basis of our MD simulations.</caption>
<thead>
<tr>
<th>Frequency ($\text{cm}^{-1}$)</th>
<th>Vibrational directions</th>
<th>Dominant atomic contributions</th>
</tr>
</thead>
<tbody>
<tr>
<td>59</td>
<td>in plane</td>
<td>Na</td>
</tr>
<tr>
<td>88</td>
<td>in plane</td>
<td>Na</td>
</tr>
<tr>
<td>115</td>
<td>in and out of plane</td>
<td>Al, Os, Na</td>
</tr>
<tr>
<td>146</td>
<td>out of plane</td>
<td>Na</td>
</tr>
<tr>
<td>162</td>
<td>out of plane</td>
<td>Na, Al</td>
</tr>
<tr>
<td>192</td>
<td>out of plane</td>
<td>Al, Os</td>
</tr>
<tr>
<td>217</td>
<td>in plane</td>
<td>Al, Os</td>
</tr>
<tr>
<td>246</td>
<td>in plane</td>
<td>Al, Os</td>
</tr>
</tbody>
</table>

In fact, the broad band between 60 and $130\ \text{cm}^{-1}$ seen in figure 3(a) transforms to a well defined peak at around $80\ \text{cm}^{-1}$ in figure 3(b) ($x = 0$). However, there might be another reason: there is a considerable temperature dependence, as studied by Hayes and Holden [11]. They report peaks at 86, 93 and $102\ \text{cm}^{-1}$, corresponding to in-plane vibrations; all decrease with increasing temperature and are hardly observed at 300 K. They proposed that $\text{Na}^+$ vacate regions associated with $\text{O}_i^{2-}$ at higher temperatures. However, if this were true, it is difficult to understand why the peaks were observed at all in the $x = 0$ compound (see their figure 3(d)); nor do we observe any such 'vacation effect' in our $x = 0.22$

![](./images/811973560019976192_3.jpg)

simulation. Room temperature (in our calculations) is clearly insufficient to induce such an effect around $O_{i}^{2-}$. By comparing the $a$ directions in the IR spectrum (figure 3(b)) and the DOS in figure 4(c) we find frequencies in the DOS at around 100 cm not seen in figure 3(b).

![](./images/811973560019976192_4.jpg)

Figure 4. The calculated contributions to the density of states (DOS) in $Na^+$ $\beta$-alumina ($x=0.22$) from different ion species and directions, in (a) the $a$ direction, (b) the $c$ direction and (c) the $a$ and $c$ direction for $Na^+$ only, in the case of $x=0$. Resolution in all plots is $8\ \text{cm}^{-1}$. The points indicate calculated values. $O_p$ denotes oxygen in the conduction planes, and $O_s$ oxygen in the spinel blocks.

We feel that the anomalous temperature effect can instead be attributed to a change in the symmetry of the modes, rendering the IR transitions forbidden at higher temperatures. Colomban et al [10] have measured the Raman spectra for the $x=0$ compound at 300 K, and they do observe an intense band at $100 \mathrm{~cm}^{-1}$.

The contributions to the DOS (2) from different ion types in both the $a$ and $c$ directions are given in figure $4(a, b)$. The in-plane frequency modes below $100 \mathrm{~cm}^{-1}$ are clearly dominated by $\mathrm{Na}^{+}$ions (figure $4(a)$ ), while figure $4(b)$ suggests that the out-of-plane band above $100 \mathrm{~cm}^{-1}$ is due to the motion of both $\mathrm{Na}^{+}$and to some extent also spinel block modes. Our band assignments below $250 \mathrm{~cm}^{-1}$, made on the basis of figures $3(a)$ and $4(a, b)$, are given in table 1 . The contributions to the DOS (2) from the $\mathrm{Na}^{+}$ions alone for the stoichiometric compound, i.e. $x=0$, in both the $a$ and $c$ directions are displayed in figure $4(c)$. A comparison of the $\mathrm{Na}^{+}$in-plane oscillations in figures $4(a)$ and $(c)$ shows that the main difference is that the band in the $100-200 \mathrm{~cm}^{-1}$ range disappears in the $x=0$ compound (in agreement with the experimental findings of Hayes and Holden [11]), whereas the band in the out-of-plane direction between 100 and $150 \mathrm{~cm}^{-1}$ (figures $4(b)$ and (c)) remains essentially unchanged.

The IR frequency range above $300 \mathrm{~cm}^{-1}$, i.e. the modes dominated by spinel block vibrations, is analysed in figure 5. In the absence of experimental data (with polarized radiation), we shall not discuss these higher-frequency modes in any detail. However, it is interesting to note that the bands at about 380 and $700 \mathrm{~cm}^{-1}$ are due to modes in the $a b$ plane, whereas those near $800 \mathrm{~cm}^{-1}$ are due to modes in the $c$ direction. The band at $500 \mathrm{~cm}^{-1}$ is mixed.

![](./images/811973560019976192_5.jpg)

Figure 5. The IR intensity, $I(v)$, calculated for $\mathrm{Na}^{+} \beta$-alumina in the range $300-1000 \mathrm{~cm}^{-1}$ for different crystallographic directions. Resolution in all plots is $8 \mathrm{~cm}^{-1}$.

The vibrational DOS for different ions and for different directions is plotted in figure $6(a, b)$ up to $1500 \mathrm{~cm}^{-1}$. The total DOS used in the calculation of thermodynamic quantities is also given in figure $6(c)$.

![](./images/811973560019976192_6.jpg)

Figure 6. The contribution to the density of states (DOS) for $Na^+$ $\beta$-alumina calculated for different ion species in the $a$ direction $(a)$ and in the $c$ direction $(b)$. The total DOS used for thermodynamic calculations is also plotted $(c)$. Resolution in all plots is $8\ \mathrm{cm}^{-1}$. $\mathrm{O_p}$ denotes oxygen in the conduction planes, and $\mathrm{O_s}$ oxygen in the spinel blocks.

![](./images/811973560019976192_7.jpg)

Figure 7. The velocity autocorrelation function (VACF) for $Na^+$, (a) using the harmonic approximation, and (b) from the MD simulation.

### 5.3. Thermodynamic properties

The difference between $C_v$ and $C_p$ is usually small in solids. This is also the case in $Na^+$ $\beta$-alumina, where the coefficient of volume expansion is rather small ($\beta = 24.5\ (MK)^{-1}$) [13]. However, at high temperatures, $C_p$ is expected to be larger than $C_v$. For a classical harmonic solid, $C_v$ is simply $3R$ (Dulong-Petit law). Using the Lebowitz equation, where no harmonic approximation is assumed, we also find (at $T = 300$ K and for 18 000 time-steps) that $C_v = 3R$ (slightly smaller). Using the definition that $C_v = (\partial E_{tot}/\partial T)_v$, we obtain the same $C_v$ value calculated for a few different temperatures. No harmonic approximation is made in the MD simulation. This, together with the fact that most ions vibrate little at $T = 300$ K (see O(5) in figure 2), seems to imply that the anharmonic contribution in $\beta$-alumina is negligible. It is believed, for example, that harmonic vibrations dominate in the spinel blocks. Uncertainties remain, however, as to the harmonicity of the vibrations for the $Na^+$ ions. We therefore derived the potential for one specific $Na^+$ ion by holding all other ions in the simulation box fixed and allowing only the $Na^+$ ion in the $a$ and then the $c$ directions to move, i.e. we calculate the total potential change in the crystal for different $Na^+$

positions (Ewald summation included). This procedure is valid only at low temperatures (here, room temperature) when both 'relaxation' effects and $Na^{+}$ migration can be neglected. The low-temperature region (up to 0.1 eV) was fitted to a harmonic potential. It is not meaningful to make this fit above 0.1 eV since at these temperatures (> 600 K), the potential is clearly anharmonic. The fit resulted in approximate force constants $k_{a}=10 ~N ~m^{-1}$ (in agreement with appendix 2 in [5]: $11.5 ~N ~m^{-1}$ ) and $k_{c}=46 ~N ~m^{-1}$ in the $a$ and $c$ directions, respectively. Applying these rough estimates of the force constants to the theory of harmonic cubic crystals (equations (7.7.37(a, b) and (7.8.1) of [18]), we can compare the VACF from this approximation (figure 7(a)) with that calculated from the MD simulation for $Na^{+}$ ions alone (figure 7(b)). It is seen that the main features (peak positions and relative heights) are rather similar. The harmonic approximation is not crucial, however, in calculating heat capacity since the system contains only $22 Na^{+}$ out of a total of 528 ions, although it can be important at higher temperatures in the low-frequency region ( $Na^{+}$ vibrations) of the DOS; note for example how the DOS changes with increasing temperature in [4]. Within the harmonic approximation, the DOS should be constant with temperature. Finally, the closely harmonic behaviour of the solid justifies the use of the quantum mechanical expression given in (6).

![](./images/811973560019976192_8.jpg)

Figure 8. The heat capacity $C_{p}$ and $C_{v}$ of $Na^{+} \beta$-alumina calculated at constant pressure and constant volume, respectively. Experimental values for $Al_{2} O_{3}$ taken from [15] are also given.

The heat capacity calculated at constant volume from (6) is plotted in figure 8; the heat capacity at constant pressure calculated from (7) is also given. The compressibility for $Na^{+}$  $\beta$-alumina was assumed to be the same as that for $Al_{2} O_{3}$ and taken as $\kappa_{T}=3.1(TPa)^{-1}$ [14]. Experimental measurements of $C_{p}$ for $Na^{+} \beta$-alumina have been made at temperatures below $300 ~K$ [15]. The values are very similar to the values for $Al_{2} O_{3}$ [16], which are also measured above $300 ~K$ . The experimental values in figure 8 are thus taken for $Al_{2} O_{3}$ (units are given per 'average particle'). The value of the heat capacity at $300 ~K$ , for example, is

![](./images/811973560019976192_9.jpg)

Figure 9. The entropy $S_p$ and $S_v$ of $Na^+$ $\beta$-alumina calculated at constant pressure and at constant volume, respectively. Experimental values for $Al_2O_3$ taken from [15] are also given.

found to be $13.9\ \text{J mol}^{-1}\ \text{K}^{-1}$. It is interesting that a calculation of the heat capacity for the $Na^+$ alone results in a value only slightly smaller than the classical result $(3Nk_\text{B})$. The $Na^+$ ions thus behave classically, which is expected since the force constants are small.

The entropies calculated from (8) as a function of temperature are displayed in figure 9, together with the experimental points for $Al_2O_3$ [16], while the corresponding internal energy and Helmholtz free energy calculated from (9) and (10) are given in figure 10.

![](./images/811973560019976192_10.jpg)

Figure 10. The internal energy $U$ and Helmholtz free energy $F$ calculated for $Na^+$ $\beta$-alumina.

Both figures 8 and 9 show a small systematic discrepancy between experimental and calculated values. This is believed to mainly be due to the following factors. (i) The harmonic approximation is less valid for higher temperatures. (ii) The experimental values above 300 K are plotted for $Al_2O_3$ (not $\beta$-alumina). (iii) There are uncertainties in the experimental parameters of (7).

## 6. Conclusions
Our calculated bands at 59, 88 and $146\ \text{cm}^{-1}$ confirm the findings of both Hayes and Holden [11] and Colomban *et al* [10] that their peaks at 59 and $\sim 100\ \text{cm}^{-1}$ are due to in-plane $\text{Na}^+$ oscillations; and that the peak of Colomban *et al* at $166\ \text{cm}^{-1}$ is due to out-of-plane $\text{Na}^+$ oscillations. In-plane $\text{Na}^+$ oscillations perturbed by the extra $\text{Al}_i-\text{O}_i-\text{Al}_i$ bridges are found both above and below $80\ \text{cm}^{-1}$. In the stoichiometric case, the in-plane frequency is found at $80\ \text{cm}^{-1}$, and the out-of-plane at $140\ \text{cm}^{-1}$. Agreement between experiment and thermodynamic calculations is demonstrated. The heat capacity at 300 K, for example, is found to be $13.9\ \text{J mol}^{-1}\ \text{K}^{-1}$. Above all, this work shows that MD can be a useful tool for interpreting experimental vibrational spectra for structurally complex materials.

## Acknowledgments
This work was supported in part by the Swedish Natural Science Research Council (NFR) and in part by the US Office of Naval Research (ONR). Thanks are also due to Professor C R A Catlow of the Royal Institute, London for giving us access to the original FUNGUS code, and to Dr M Wojcik for most interesting discussions.

## References
[1] Yao Y F Y and Kummer J T 1967 *J. Inorg. Nucl. Chem.* **29** 2453
[2] Edström K, Thomas J O and Farrington G C 1991 *Acta Crystallogr.* B **47** 210
[3] Zendejas M A and Thomas J O 1990 *Phys. Scr.* **T 33** 235
[4] Smith W and Gillan M J 1992 *J. Phys.: Condens. Matter* **4** 3215
[5] Walker J R and Catlow C R A 1982 *J. Phys. C: Solid State Phys.* **15** 6151
[6] Ewald P P 1921 *Ann. Phys.* **64** 253
[7] McQuarrie D A 1976 *Statistical Mechanics* (New York: Harper and Row)
[8] Kittel C 1986 *Introduction to Solid State Physics* (New York: Wiley)
[9] Lebowitz J L, Percus J K and Verlet L 1967 *Phys. Rev.* **153** 250
[10] Colomban Ph, Mercier R and Lucazeau G 1981 *J. Chem. Phys.* **75** 1388
[11] Hayes W and Holden L 1982 *J. Phys. C: Solid State Phys.* **15** 6141
[12] Lucazeau G 1983 *Solid State Ion.* **8** 1
[13] May G J and Henderson C M B 1979 *J. Mater. Sci.* **14** 1229
[14] Lewis G K and Drickamer H G 1966 *J. Chem. Phys.* **45** 224
[15] Lucazeau G private communication
[16] 1985 *J. Phys. Chem. Ref. Data* **14** (Supp. 1) 156
[17] Zendejas M A and Thomas J O 1987 *Solid State Ion.* **28** 46
[18] Maradudin A A, Montroll E W and Weiss G H 1963 *Theory of Lattice Dynamics in the Harmonic Approximation* (New York: Academic)
[19] Walker J R 1982 *Lecture Notes in Physics* vol 166, ed C R A Catlow and W C Mackrodt (Berlin: Springer) pp 58–66
[20] Zendejas M A and Thomas J O 1993 *Phys. Scr.* **47** 440
[21] Sangster M J and Dixon M 1976 *Adv. Phys.* **25** 247