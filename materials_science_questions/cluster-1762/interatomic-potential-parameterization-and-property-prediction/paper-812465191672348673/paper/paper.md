Ab-initio simulation of thermal properties of AlN ceramics

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1995 Modelling Simul. Mater. Sci. Eng. 3 521

(http://iopscience.iop.org/0965-0393/3/4/007)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 130.126.162.126
This content was downloaded on 07/09/2015 at 03:16

Please note that terms and conditions apply.

Modelling Simul. Mater. Sci. Eng. 3 (1995) 521-531. Printed in the UK

# Ab-initio simulation of thermal properties of AlN ceramics

H Kitagawa, Y Shibutani and S Ogata

Department of Mechanical Engineering, Osaka University, Osaka 565, Japan

Received 13 November 1994, accepted for publication 8 March 1995

Abstract. Aluminum nitride (AIN) ceramics are prospective materials for electronic parts, particularly LSI substrates, because of their excellent mechanical, dielectrical and thermal properties. Their high thermal conductivity is estimated to be about $320\ \text{W m}^{-1}\text{K}^{-1}$ from some theoretical and experimental considerations. However, existence of crystalline imperfections such as impurities, lattice defects or a different phase (zincblende phase) practically reduces it to only two-thirds of the theoretically predicted one. In this paper an interatomic potential of AIN which is adequate for molecular dynamics MD calculation is established on the basis of $ab$ initio molecular orbital MO analysis of an AlN cluster. Then the thermal conductivity of AIN is estimated by equilibrium MD simulation, and its dependence on crystallographic structure and lattice defects is examined. We find that the energy difference between two kinds of phase structure in AIN (the wurtzite and zincblende) is so small that they are able to coexist in the realistic material. The thermal conductivity of the zincblende is also found to be much lower than that of the wurtzite.

## 1. Introduction

AIN which belongs to the III-V group is a semiconductor material with a hexagonal wurtzite crystal [1]. Its unit cell is shown in figure 1. AlN possesses a lot of remarkable physical

![](./images/812465191672348673_1.jpg)

Figure 1. A unit cell of wurtzite type crystal structure.

properties, for example, high intrinsic thermal conductivity $(\sim320\ \text{W mK}^{-1}$ at room

temperature [2]), low thermal expansion $(\sim 2.7 \times 10^{6} \mathrm{~K}^{-1}$ [3]) and large band gap (6.3 eV [4]). Moreover, its thermal resistance and mechanical strength are excellent. This is the reason why many attempts have recently been made to make use of this ceramic as a dielectric substrate of LSI.

One of the most attractive properties is the high thermal conductivity. It is higher than most other non-metallic solids except a few materials, e.g. diamond and silicon carbide, and is comparable to the that of copper. The high thermal conductivity arises from (1) small masses of the constitutent atoms, i.e. both aluminum and nitrogen are light atoms, (2) a strong interatomic bond between aluminum and nitrogen atoms and (3) a simple crystal structure and weakly anharmonic lattice vibrations [2]. But usually the thermal conductivity of AlN supplied for practical use is considerably smaller than the ideal one predicted by Slack et al [5]. The main reason is that the phonons, the main carriers of heat in dielectric materials, are scattered by impurities (e.g. oxygen, silicon carbide, beryllium oxide [5]), lattice defects or, possibly, mixing of another AlN phase (e.g. zincblende phase). Several experimental works have been done to investigate the influence of these imperfections of the lattice structure on thermal properties [5].

Recently, thermal conductivities of several materials have been calculated by MD simulation. Young et al [6] computed the thermal conductivity of amorphous silicon ( $\alpha$-Si) using the model proposed by Wooten-Winer-Weaire with the Stillinger-Weber three-body model potential. Anthony and Moran [7] calculated it for an artificial face-centered-cubic material with a pairwise additive inverse twelfth-power potential on the basis of the Green- Kubo formula [8], and Evans and Morris developed a new MD simulation technique which includes the effect of an external force in thermal conductivity calculation of liquid materials, and applied it to a Lennard-Jones fluid at the triple point [9, 10, 11].Irrespective of non- equilibrium simulations, periodic boundary conditions can be used in the Evans method.

In the present paper, ab initio estimations of thermal properties of AlN with and without lattice imperfections are carried out. A proper functional form of the interatomic potential including three-body interaction is proposed and parameters included in the potential function are estimated from results of ab initio MO calculation [12] of an AlN model cluster. On the basis of the obtained interatomic model potential, MD simulations are performed for AlN crystals. By employing the Green-Kubo formula to estimate the energy flow carried by lattice vibrations, the temperature dependence of thermal conductivity of the perfect AlN crystal, AlN crystal with point defects and zincblende phase AlN crystal are evaluated.

## 2. Potential function for AlN crystal

### 2.1. Representation of interatomic interaction

It is well known that the bond between aluminum and nitrogen is basically not only covalent, but also an ionic property due to highly localized electric charge distribution near the nitrogen atomic site [13]. The short-ranged covalent bond is made up by $\mathrm{sp}^{3}$ hybridization electron orbitals. The bond energy depends strongly on a bond angle so that the basic local structure of AlN forms a tetrahedron. On the other hand, the ionic property gives rise to a long-ranged Coulomb interaction. Thus, combination between them produces the wurtzite structure as the most stable one for AlN.

To introduce these characteristic features in MD simulation, the interatomic model

potential of AlN is assumed to be made up of two-body and three-body terms,
$$
\Phi=\sum_{\substack{i j \\ i>j}} \phi_{2 B}\left(r_{i j}\right)+\sum_{\substack{i j k \\ i \neq j, i \neq k, j>k}} \phi_{3 B}\left(r_{i j}, r_{i k}, \theta_{j i k}\right)
\tag{1}
$$
where $r_{i j}$ is the distance between $i$ and $j$ atoms and $\theta_{j i k}$ is the angle formed between bonds of $i-j$ and $i-k$ atoms. The first term of the right-hand side of equation (1) represents the two-body interaction, which is assumed to be expressed by the Born-Mayer-Higgins-type potential function [14],
$$
\phi_{2 B}\left(r_{i j}\right)=\frac{Q_{i} Q_{j} e^{2}}{r}+\left(B_{i}+B_{j}\right) \exp \left[-\frac{a_{\imath}+a_{j}-r}{b_{i}+b_{j}}\right]-\frac{c_{i} c_{j}}{r^{6}}.
\tag{2}
$$

The first, second and third terms of the right-hand side in equation (2) represent Coulomb, repulsive and dipole moment interactions, respectively.

The second term of equation (1), which corresponds to the three-body interaction, is to be a function of the bond length and angle. The following type of function is adopted here:
$$
\phi_{3 B}\left(r_{i j}, r_{i k}, \theta_{j i k}\right)=C \exp \left[\alpha \frac{\left(r_{i j}+r_{i k}\right)}{2}\right]\left(\theta_{j i k}-\theta_{0}\right)^{2} f_{\mathrm{c}}\left(r_{i j}\right) f_{\mathrm{c}}\left(r_{i k}\right)
\tag{3}
$$
$$
f_{\mathrm{c}}(r)=\left\{\begin{array}{cc}
1 & r<R-D \\
\frac{1}{2}\left\{1-\sin \left[\frac{\pi(r-R)}{2 D}\right]\right\} & R-D<r<R+D \\
0 & r>R+D
\end{array}\right.
\tag{4}
$$
where $f_{\mathrm{c}}(r)$ is a cut-off function, which is introduced to describe the short-range property of the three-body interaction.

### 2.2. Fitting procedures of model potential
The potential parameters in equations (2)-(4) are determined by fitting to the energy surface obtained by $ab$ initio MO calculations for AlN cluster. Figure 2 shows the $\mathrm{Al}_{4} \mathrm{~N}_{4} \mathrm{H}_{18}$ model cluster used, which is part of the wurtzite crystal. Three $\mathrm{H}$ atoms are attached to each outer $\mathrm{Al}$ and $\mathrm{N}$ atom to compensate the effect of the electron configuration in bulk crystal. The energy surface is calculated by a standard MO method [12] for various atomic configurations with respect to the nearest $\mathrm{Al}-\mathrm{N}$ distance and the bond angle of the cluster. A STO-3G basis set incorporated in the GAUSSIAN80 [12] is used in the MO calculation.

Figure 3 shows the obtained energy surface of the cluster with respect to the bond length and angle. The total energy takes the minimum value at the bond length of $1.91 \AA$ and the bond angle of $107^{\circ}$. This bond length and bond angle agree well with the experimental data, $1.92 \AA$ and $107.7^{\circ}$, respectively [15].

Then the potential parameters in equations (2)-(4) are obtained so as to fit equation (1) with this energy surface, as listed in table 1.

### 2.3. Evaluation of the model potential
Variation of the total energy per atom with respect to volume change is calculated on the assumption that AlN has either wurtzite or zincblende structure. The unit cells of these structures used in the calculations are shown in figure 4 and figure 5, respectively. The energy calculations for the wurtzite structure are performed, keeping the $c / a$ ratio a constant value which has been obtained from experiment [17]. Long-range Coulomb interaction is

![](./images/812465191672348673_2.jpg)

Figure 2. An $Al_4N_4H_{18}$ cluster used for ab initio MO calculation (Distances of Al-H and N-H are fixed as 1.0 Å.)

![](./images/812465191672348673_3.jpg)

Figure 3. Energy surface of the AlN cluster obtained by ab initio MO calculation.

taken into account by the Ewald method [16]. Figure 6 shows relations of energy per atom versus atomic volume of both structures. The energy curves are similar but the energy of the zincblende structure is little higher than of the wurtzite structure in the whole range. These results may imply coexistence of these two structures in the practically used AlN.

Table 2 shows the lattice constants and bulk modulus of wurtzite structure deduced from the determined potential. The bulk modulus ($B$) is given by the second derivative of energy with respect to volume at the stable state. The estimated values for the bulk modulus

<table>
<caption>Table 1. Interatomic potential parameters. (Parameters in equations (2)-(4), being fitted to the energy surface obtained by MO analyses.)</caption>
<thead>
<tr>
<th></th>
<th>Parameter</th>
<th>Value</th>
<th>Unit</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="11">Two Body</td>
<td>$Q_{\text{Al}}$</td>
<td>0.579</td>
<td></td>
</tr>
<tr>
<td>$Q_{\text{N}}$</td>
<td>$-0.579$</td>
<td></td>
</tr>
<tr>
<td>$a_{\text{Al}}$</td>
<td>0.53721</td>
<td>$\text{\AA}$</td>
</tr>
<tr>
<td>$a_{\text{N}}$</td>
<td>0.88139</td>
<td>$\text{\AA}$</td>
</tr>
<tr>
<td>$b_{\text{Al}}$</td>
<td>0.05308</td>
<td>$\text{\AA}$</td>
</tr>
<tr>
<td>$b_{\text{N}}$</td>
<td>0.15559</td>
<td>$\text{\AA}$</td>
</tr>
<tr>
<td>$c_{\text{Al}}$</td>
<td>9.4664</td>
<td>$\text{eV}^{1/2}\ \text{\AA}^{3}$</td>
</tr>
<tr>
<td>$c_{\text{N}}$</td>
<td>15.085</td>
<td>$\text{eV}^{1/2}\ \text{\AA}^{3}$</td>
</tr>
<tr>
<td>$B_{\text{Al}}$</td>
<td>18.760</td>
<td>$\text{eV}$</td>
</tr>
<tr>
<td>$B_{\text{N}}$</td>
<td>4.8629</td>
<td>$\text{eV}$</td>
</tr>
<tr>
<td>$C$</td>
<td>0.5069</td>
<td>$\text{eV}$</td>
</tr>
<tr>
<td rowspan="4">Three Body</td>
<td>$a$</td>
<td>2.523</td>
<td>$\text{\AA}$</td>
</tr>
<tr>
<td>$R$</td>
<td>2.9</td>
<td>$\text{\AA}$</td>
</tr>
<tr>
<td>$D$</td>
<td>0.2</td>
<td>$\text{\AA}$</td>
</tr>
<tr>
<td>$\cos\theta_0$</td>
<td>$-\frac{1}{3}$</td>
<td></td>
</tr>
</tbody>
</table>

![](./images/812465191672348673_4.jpg)

Figure 4. Simulation cell of wurtzite structure; a large and a small spheres show Al and N atoms, respectively.

and lattice constant agree well with the experimental values, regardless of insufficiency of model cluster size in the ab initio MO calculation. The differences between the estimated and experimental values are less than 2% for the lattice constant, and 1-3% for the bulk modulus.

![](./images/812465191672348673_5.jpg)

Figure 5. Simulation cell of zincblende structure; two kinds of spheres are the same as in figure (4).

![](./images/812465191672348673_6.jpg)

Figure 6. Comparison of total energy per atom between wurtzite and zincblende structures of AIN.

## 3. Thermal conductivity of AIN

### 3.1. Method of estimation using the Green-Kubo formula

MD simulations are carried out in order to estimate the characteristics of energy transport due

Table 2. Comparisons of some physical properties for the wurtzite structure obtained using the present potential with the experimental data [17][18][19].

<table>
  <thead>
    <tr>
      <th></th>
      <th>Calculation</th>
      <th>Experiment [17]</th>
      <th>Error (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$a$ (m)</td>
      <td>$3.06×10^{-10}$</td>
      <td>$3.11×10^{-10}$</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>$c$ (m)</td>
      <td>$4.90×10^{-10}$</td>
      <td>$4.98×10^{-10}$</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>$B$ ($Nm^{-2}$)</td>
      <td>$2.08×10^{11}$</td>
      <td>$2.017×10^{11}$[18]</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>$2.057×10^{11}$[19]</td>
      <td>1.1</td>
    </tr>
  </tbody>
</table>

to lattice vibrations on the basis of the determined potential. By means of the Green-Kubo theory, the thermal conductivity factor $\lambda$ which is the factor of heat transport is evaluated from the decay of equilibrium fluctuations of the heat flow vector $q(t)$ as follows:

$$
\lambda=\frac{1}{k_{B} V T^{2}} \int_{0}^{\infty}\left\langle q_{z}(t) q_{z}(0)\right\rangle d t
\tag{5}
$$

where $q_{z}$, $V$, $T$ and $k_{B}$ are heat flux along the $z$ axis, volume of the system, temperature and the Boltzmann constant, respectively. The heat current vector $q$ is calculated by [8]

$$
\boldsymbol{q}=\sum_{i} E_{i} \boldsymbol{v}_{i}+\frac{1}{2} \sum_{i j} \boldsymbol{r}_{i j}\left(\boldsymbol{v}_{i} \cdot \boldsymbol{F}_{i j}\right)
\tag{6}
$$

where $E_{i}$ is the site energy of atom $i$ which is assumed to be obtained by

$$
E_{i}=\frac{1}{2} \sum_{\substack{j \\ i \neq j}} \phi_{2 B}\left(r_{i j}\right)+\sum_{\substack{j k \\ i \neq j, i \neq k, j>k}} \phi_{3 B}\left(r_{i j}, r_{i k}, \theta_{j i k}\right)+\frac{1}{2} m_{i}\left|\boldsymbol{v}_{i}\right|^{2},
\tag{7}
$$

$\boldsymbol{v}_{i}$ and $m_{i}$ are the velocity and the mass of atom $i$, respectively. $\boldsymbol{r}_{i j}$ and $\boldsymbol{F}_{i j}$ in equation (6) represent the directional vector from atom $j$ to atom $i$ and the force acting on atom $i$ due to atom $j$, respectively. $E_{i}$ should be considered to include the two- and three-body terms of the potential energy and the kinematical energy. Contributions of the three-body potential energy $\phi_{3 B}$ to $E_{i}$ are assumed to be calculated as the $i$ site energy of an atomic configuration consisting of three atoms arbitrarily taken out around atom $i$. Partition of $\phi_{3 B}$ to a particular atom is not unique, but it can be presumed to have little influence on results of the heat flux, how to participate it because the temperature gradient of the equilibrium systems is small and their temperature change is also small in a effective range of the interatomic potential [6][7].

The heat flux which is included in equation (5) is calculated from MD simulation for the equilibrium NVT ensemble. The time correlation function of the heat flux should be integrated until the time correlation becomes small enough.

### 3.2. Thermal conductivity of perfect crystal

A unit cell for the calculation of thermal conductivity contains 36 aluminum atoms and 36 nitrogen, as shown in figure 4. Periodic boundary conditions are imposed along each lattice vector direction. After the atomic system is relaxed enough to be in equilibrium under the given initial temperature, the heat flux is calculated at every time step until its time correlation becomes sufficiently small. The simulation time step $\Delta t$ employed is 0.5 fs. Figure 7 shows a typical change of the time correlation which is averaged over the total simulation time after the initial relaxed state. The decay rate of the correlation is found

to be very slow from this figure. It needs a long computational time to estimate thermal conductivity by mean of the Green-Kubo theory. In this work the simulation is done until 25 ps (at high temperature) -100 ps (at low temperature). The statistical error of the time correlation function is estimated to be less than 20% in the region over 170 K.

![](./images/812465191672348673_7.jpg)

Figure 7. An example of decay of the time correlation function of the heat flux at $T$ =282 K.

![](./images/812465191672348673_8.jpg)

Figure 8. Temperature dependence of the thermal conductivity for the wurtzite structure of AlN; a broken line shows the experimental data [5].

The thermal conductivity $\lambda$ calculated by numerical integration of equation (5) is shown in figure 8. In the high-temperature range which is higher than about 170 K, the present results are in good agreement with the experimental data indicated by the broken line [5].

It is well known that phonons are the main carriers of heat in an insulator. Therefore, the properties of phonon propagation govern almost all of the thermal conductivity. The thermal conductivity through atomic vibrations is evaluated to be $\lambda \sim \frac{1}{3} C v l$, where $C$, $v$ and $l$ are the specific heat, the sound velocity and the phonon mean free path, respectively. $C$ increases in proportion to $T^{3}$ below the Debye temperature(AlN: ~747 K [20]), and approaches to a certain value being intrinsic to the crystal above it. $v$ has little dependence on the temperature, and $l$ is regarded as being almost constant at low temperature, because phonons scatter mainly by temperature-independent factors such as surfaces or various crystal imperfections. However, at high temperatures mutual interactions of phonons are dominant and then $l$ decreases as $T^{-1}$. As the result, the thermal conductivity is considered to increase as $T^{3}$ at low temperatures and to decrease as $T^{-1}$ at high temperatures.

It is found from figure 8 that the $\lambda$ is proportional to about $T^{-1.26}$ above 800 K, which is in good agreement with the experimental data of $T^{-1.21}$. The exponent smaller than $-1$ is regarded as being the effect of high-order anharmonicities on the phonon lifetime [7].

The agreement between the MD results and the experimental are is poor at the temperature below 200 K. The reason for the discrepancy seems to come from the size of the simulation cell, simulation time and phonon quantum effects.

The effect of model size is not very large because of two canceling effects [7]. As the cell size gets larger, phonons with lower frequency may be allowed to propagate, which generally make a certain contribution to the thermal conductivity. On the other hand, the probability for phonon scattering increases, which decreases the phonon lifetime.

The effect of simulation time may be very large. The main reason for the discrepancy

in the low-temperature range is that the convergence rate of the time correlation of heat flux becomes very slow. The phonon quantum effect may also appear at low temperature [6], but it gives rise to a very small effect.

Table 3. Estimated thermal conductivities by MD simulations for the wurtzite AlN.

| Temperature $T_{\text{MD}}$ (K) | Thermal conductivity($c$-axis direction) $\lambda_{\text{MD}}$ (W m$^{-1}$K$^{-1}$) |
|----------------------------------|-------------------------------------------------------------------------------------|
| 171                              | 1342                                                                                |
| 282                              | 697                                                                                 |
| 563                              | 85.5                                                                                |
| 1130                             | 34.2                                                                                |
| 2200                             | 15.4                                                                                |

### 3.3. Crystal with point defects

One of the most familiar defects in AlN is due to oxygen which enters as a substitutional impurity in the crystal [2]. It is a well known process that oxygen replaces nitrogen and deficit vacancies are generated in the aluminum sublattice [21]. In order to estimate the effect of such a point defect(vacancy) on the thermal conductivity, MD simulations are performed for the cell containing one vacancy either at the Al or N site. The simulation cell is constructed such that one atom is removed from an Al or N site of the same cell as used for the perfect AlN crystal. Thus, the simulation cell contains 71 atoms, and the other simulation conditions are the same as used in the perfect crystal.

![](./images/812465191672348673_9.jpg)

Figure 9. Thermal conductivities of wurtzite structure AlN with a point defect, referring to the case for the perfect crystal.

![](./images/812465191672348673_10.jpg)

Figure 10. Thermal conductivity of zincblende structure, referring to the case for the wurtzite.

The obtained thermal conductivities are shown in table 4 and figure 9. The thermal conductivity decreases drastically, especially at low temperature. This result may be caused by the phonon scattering at the point defect which makes the mean free path of the phonon $l$ and thus its lifetime shorter.

The thermal conductivity for the case with a point defect at an Al site is smaller than at an N site, because the atomic weight of Al is heavier than that of N.

Slack et al [5] have experimentally estimated a thermal resistivity of an oxygen impurity at room temperature (300 K) as $\Delta W/\epsilon = 0.43$ mK W$^{-1}$ ($\epsilon$ is a number density ratio of oxygen impurities to nitrogen atoms). The thermal resistivity for the vacancy at an Al site is estimated by the MD simulation to be $\Delta W/\epsilon_{\text{pd}} = 4.2$ mK W$^{-1}$. The reason for this large discrepancy is that the existence of oxygen, which substitutes nitrogen, is not considered in the MD simulations and the density of defects is so high that mutual interactions of atoms make the possibility of phonon scattering increase.

Table 4. Comparisons of the thermal conductivity for the crystal having a point defect with one for the perfect crystal.

<table>
  <thead>
    <tr>
      <th>Temperature $T_{MD}$ ( K)</th>
      <th>Thermal conductivity (c-axis direction) $\lambda_{MD}^{\text{pd}}$ (W m$^{-1}$ K$^{-1}$)</th>
      <th>Thermal conductivity of perfect crystal $\lambda_{MD}$ (W m$^{-1}$ K$^{-1}$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1100</td>
      <td>10.1 (N site)</td>
      <td>$\approx 30$</td>
    </tr>
    <tr>
      <td>1110</td>
      <td>3.6 (Al site)</td>
      <td></td>
    </tr>
    <tr>
      <td>281</td>
      <td>17.0 (N site)</td>
      <td>$\approx 600$</td>
    </tr>
    <tr>
      <td>298</td>
      <td>8.3 (Al site)</td>
      <td></td>
    </tr>
  </tbody>
</table>

### 3.4. Zincblende phase crystal
The energy difference between wurtzite and zincblende structures has been found to be very small in the above. Thus, they are very likely to coexist in the realistic materials. The thermal conductivity of the zincblende structure is obtained using the cell shown in figure 5 and compared with the wurtzite structure in figure 10. We find that the thermal conductivity of the zincblende is much lower than that of the wurtzite. Thus, the existence of zincblende structure causes the ideal conductivity of AlN to decrease sufficiently.

Table 5. The thermal conductivity for the zincblende crystal phase.

<table>
  <thead>
    <tr>
      <th>Temperature $T_{MD}$ (K)</th>
      <th>Thermal conductivity(c-axis direction) $\lambda_{MD}^{\text{zb}}$ (W m$^{-1}$ K$^{-1}$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>161</td>
      <td>593</td>
    </tr>
    <tr>
      <td>268</td>
      <td>142</td>
    </tr>
    <tr>
      <td>546</td>
      <td>37.5</td>
    </tr>
    <tr>
      <td>1090</td>
      <td>10.2</td>
    </tr>
  </tbody>
</table>

### 4. Conclusion
We find a certain characteristic feature of the thermal conductivity of AlN by MD simulation employing a model interatomic potential determined from ab initio MO analysis. Main results obtained are the following.

(1) There is little difference of the total energy per atom between the wurtzite structure and the zincblende. This implies that they may coexist in the realistic material. Moreover,

the $\lambda$ of the zincblende is much smaller than that of the wurtzite. That may be one reason why the measured thermal conductivity of the practically used AlN lessens significantly from the predicted one.

(2) For AlN containing a vacancy, the $\lambda$ falls drastically due to the phonon scattering. Its decrease is more remarkable at an Al site vacancy than at a N site.

(3) The $\lambda$ of the wurtzite decays as $T^{-1.26}$ at high temperatures over 800 K. This result is in fairly good agreement with the experimental data of $T^{-1.21}$.

The ab initio estimation of the interatomic potential based on MO analysis for a suitable cluster is proved to be useful, even for a material with complex crystal structure. However, it seems not to be easy to estimate thermal properties by MD simulation, especially at low temperatures, because of limitation of computational time.

## Acknowledgment
The authors gratefully acknowledge support from the Ministry of Education, Science and Culture of Japan under Grant in Aid for Cooperative Research A, Project No 06302035.

## References
[1] Wyckoff R W G 1963 *Crystal Structures* 2nd edn vol 1 (New-York: Interscience)
[2] Slack G A 1973 *J. Phys. Chem. Solids* **34** 321
[3] Slack G A and Bartram S F 1975 *J. Appl. Phys.* **46** 89
[4] Perry B and Rutz R F 1978 *Appl. Phys. Lett.* **33** 319
[5] Slack G A, Tanzilli R A, Pohl R O and Vandersande J W 1987 *J. Phys. Chem. Solids* **48** 641
[6] Young H L, Biswas R, Soukoulis C M, Wang C Z, Chan C T and Ho K M 1991 *Phys. Rev. B* **43** 6573
[7] Anthony J C and Moran B 1986 *Phys. Rev. B* **34** 5058
[8] Zwanzig R W 1965 *Annu. Rev. Phys. Chem.* **16** 67
[9] Evans D J 1982 *Phys. Lett.* **91A** 457
[10] Evans D J and Morris G P 1984 *Comput. Phys. Rep.* **1** 297
[11] Evans D J and Morris G P 1990 *Statistical Mechanics of Nonequilibrium Liquids* (London: Academic)
[12] Binkley J S, Whiteside R A, Krishnan R, Seger D J, De Frees D J, Schlegel H B, Topiol S, Kahn L R and Pople J A 1981 *Gaussian80 QCPE* vol 13
[13] Ching W Y and Harmon B N 1986 *Phys. Rev. B* **34** 5305
[14] Tsuneyuki S, Tsukada M and Aoki H 1988 *Phys. Rev. Lett.* **61** 869
[15] Schulz H and Thiemann K H 1977 *Solid State Commun.* **23** 815
[16] Ewald P P 1921 *Ann. Phys.* **64** 253
[17] Yim W M and Paff R J 1974 *J. Appl. Phys.* **45** 1456
[18] Tsubouchi K, Sugai K and Mikoshiba N 1981 *Proc 1981 Ultrasonics Symp.* vol 1 375
[19] Boch P, Glandus J C, Jarrige J, Lecompte J P and Meximain J 1982 *Ceram. Int.* **8** 34
[20] Neuberger N 1971 *III-V Semiconducting Compounds: Handbook of Electronic Materials* 2 (IFI/Plenum)
[21] Slack G A and McNelly T F 1976 *J. Cryst. Growth* **34** 263