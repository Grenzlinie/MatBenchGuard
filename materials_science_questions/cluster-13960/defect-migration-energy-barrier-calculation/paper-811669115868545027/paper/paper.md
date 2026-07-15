# Self-interstitial Diffusion in $\alpha$-Zirconium

W.J. Zhu, C.H. Woo $^{\circledR}$, Hanchen Huang
Department of Mechanical Engineering, The Hong Kong Polytechnic University, Kowloon, Hong Kong

## ABSTRACT
Self-interstitials diffusion in $\alpha$-Zr is studied using Molecular Dynamic (MD) and molecular static (MS) simulation using Ackland's many-body inter-atomic potential. The basal crowdion configuration is found to be the ground state. The diffusion process in Zr is complex. Four types of diffusion jumps can be identified, two in-plane and two out-of plane. The in-plane migration mechanism is dominated by one-dimensional crowdion motion along the $[11\overline{2}0]$ directions, interrupted by occasional out-of-plane and on-line or off-line jumps. The mean lifetime before rotation of the crowdion is reported as a function of temperature. The activation energies for the diffusion processes are obtained. The diffusional anisotropy factor $D_{\mathrm{c}}/D_{\mathrm{a}}$ is also obtained, and compares well with experiment results.

## INTRODUCTION
Zirconium and its alloys are important due to their extensive application in water-cooled and water-moderated reactors. Because of the anisotropic crystallographic structure of Zr, which is hexagonal close pack (HCP), irradiation damage accumulation in Zr produces effects that are different from those in cubic metals. Thus, in addition to void swelling and irradiation creep, the anisotropy of the evolving dislocation structure produces a deviatoric straining even in the absence of an external stress. Indeed, irradiation growth is the name given to the volume-conserved shape deformation that occurs in non-cubic crystalline materials under irradiation in the absence of an applied stress. Besides zirconium and its alloys [1-4], examples of irradiation growth are also found in graphite [5-8], and uranium [9].

To take into account the anisotropy of the diffusion of point defects in the kinetics of their reaction with other crystal defects, Woo and Goesele [10] generalized the rate theory for application to HCP metals like Zr, using the reaction kinetic theory of anisotropically diffusing reactants. The difference in diffusional anisotropy (DAD) [11,12] between the vacancies and interstitials was found to produce a large bias in their reaction rates with sinks. The resulting large variability of the biases for sinks adds a new dimension to the complexity of irradiation damage behaviour of the HCPs. It has been shown that DAD explains, qualitatively or semi-qualitatively, many of the anomalous behaviour of irradiation damage accumulation in zirconium [10-14].

A major difficulty in modeling irradiation damage in Zr is the lack of conclusive information on the anisotropy of the migration of both the vacancies and the interstitials [15]. Much work has focused on the configuration and associated energies of the self-interstitials. Early work by Fuse [16] and Monti [17-18] used central pair potential in their investigations of the intrinsic defect configuration and their diffusion. Since pair potential is not considered to be adequate in describing the HCPs with near-ideal $c/a$ lattice-parameter ratio, i.e.
$c/a=(8/3)^{1/2}$ [19], several many-body potentials have recently been developed, including Ackland [19], Oh and Johnson [20], Igarashi, Khantha and Vitek [21], J.R. Fernandez and A.M. Monti [22].

$^{\circledR}$ Email address: Chung.Woo@polyu.edu.hk

AA7.31.1

All computer simulation results indicate the possible existence of multiple stable and metastable configurations of the self-interstitial in Zr. In general, the basal configurations are found to be energetically favored. The diffusion of the self-interstitial shows highly anisotropic behaviour, moving faster on the basal plane than along the c-direction. In addition, intensive studies of the diffusion of interstitial clusters [23-24] and the vacancy [22] have also been carried out. Nevertheless, little is known in detail about the complex diffusion mechanisms of self- interstitials in zirconium [25], particularly under the action of a stress. Work on the vacancy in zirconium also yields inconclusive results, because of their sensitivity to the potential used.
Nevertheless, in all the cases studied, vacancy migration is much more isotropic in general [26]. Experimentally, direct measurements of migration properties of self-interstitials have not been performed, and that of vacancies is restricted to temperatures higher than $600^o$C [27]. However, even at these high temperatures, attempts to measure the diffusional anisotropy only yields results which are generally inconclusive, except that the anisotropy is perhaps small, consistent with computer simulation results [26].

In this study, we use molecular dynamic simulation (MD), supplemented by molecular static (MS) simulation, to investigate the mechanisms of self-interstitial migration in zirconium, with particular emphasis on the diffusional anisotropy. In order to mimic the dynamic behaviour of the self-interstitial, the dynamic model was emphasized. The simulation method is presented in Section 2. Results, discussions and comparison with experiments are presented in Section 3. Finally we conclude in Section 4.

## SIMULATION METHOD

We use Ackland's many-body interatomic potential [19] of the Finnis-Sinclair-type. The binding energy for this potential is given as the sum over bonds by:

$$
E_{i}=\frac{1}{2} \sum_{j} V\left(x_{i j}\right)-\rho_{i}^{1 / 2} \text { where } \rho_{i}=\sum_{j=1}^{N} \phi\left(x_{i j}\right) \tag{1}
$$

In (1), $V$ and $\phi$ are pairwise functions between atoms $i$ and $j$ separated by distance $x_{i j}$. The reliability of this potential has been tested in the calculation of configurations of point defects, displacement cascades during irradiation damage, and phase transition in the zirconium [19,23,28]. The simulation cell is composed of 1948 atoms, constituting a cubic of $35.91 \mathring{A}$, $33.94 \mathring{A}$ and $36.48 \mathring{A}$ along the $\langle 11\overline{2}0\rangle$, $\langle 1\overline{1}00\rangle$ and $\langle 0001\rangle$ directions. Periodic boundary conditions are employed in these three directions. Adding an extra zirconium atom in the simulation cell generates a self-interstitial. The formation energy of the self-interstitial atom is calculated according to $E_{f}=E_{N+1}-E_{N}-E_{sub}$, where $E_{N}$ is the energy of the reference system without the extra atom, $E_{N+1}$ is that of the defected system containing the self-interstitial atom in its fully relaxed configuration, and $E_{sub}$ is the sublimation energy of zirconium. Local minimum energy configurations determined by using dynamic quench method [28], are used to locate the stable configurations of self-interstitials.

To take into account the temperature effects, a thermal bath is simulated using Langevin forces, with a frictional coefficient that produce a temperature transition in about 1ps. This value is chosen to optimize the computational efficiency and minimize the occurrence of artifacts caused by the random force. During the dynamic simulation, forces generated by the potential determine the trajectories of atoms. The volume of the simulation cell is kept constant during the calculation, according to the micro-canonical ensemble (N,V,E). Before the simulation, the

AA7.31.2

lattice constant of zirconium as a function of temperature is determined, using the Parrinello- Rahman [29] algorithm to keep the simulated cell stress free at finite temperatures. The integration time step is one fanto-second.

## RESULTS AND DISCUSSIONS

Based on symmetry considerations, we consider the following basic interstitial configurations: the octahedral (O), basal tetrahedral ($B_T$), basal octahedral ($B_O$), basal crowdion ($B_C$), basal split ($B_S$), non-basal crowdion ($C_N$), and the c-dumbbell ($D_C$) (fig.1). In previous works, basal configurations such as $B_C$, $B_O$ and $B_S$ have been found to be the most stable. Other configurations are metastable or unstable. The formation energies obtained in this work are listed in Table 1.

![](./images/811669115868545027_1.jpg)

Figure 1. Some possible configurations of self-interstitials in the HCP structure.

Table 1. Calculated self-interstitial formation energies of the different configurations

<table>
  <thead>
    <tr>
      <th>Configuration</th>
      <th>$B_C$</th>
      <th>$B_S$</th>
      <th>$B_O$</th>
      <th>$B_T$</th>
      <th>O</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ackland (eV)</td>
      <td>3.71</td>
      <td>3.72</td>
      <td>3.93</td>
      <td>3.98</td>
      <td>4.08</td>
      <td>3.93</td>
    </tr>
    <tr>
      <td>Pasianot (eV)</td>
      <td>3.75</td>
      <td>3.76</td>
      <td>3.88</td>
      <td>4.05</td>
      <td>4.05</td>
      <td>4.03</td>
    </tr>
    <tr>
      <td></td>
      <td>Stable</td>
      <td>Unstable</td>
      <td>Metastable</td>
      <td>Unstable</td>
      <td>Unstable</td>
      <td>Unstable</td>
    </tr>
  </tbody>
</table>

We note that results from a larger model comprising 6732 atoms have been checked for convergence. In Table 1, the results of Pasianot et.al. [30] (converted according to the present definition of formation energy), using another many-body potential of the Finnis-Sinclair form, are included for comparison. It can be seen that $B_C$ is the most stable configuration, and the calculated formation energies are in good agreement with [30]. In comparison, we note that in our previous work for Ti, $B_S$ is the most stable configuration [31], and as a result, the geometry of the diffusion jumps of the two metals may be different.

From the symmetry of the HCP lattice, four migration paths for the self-interstitial are possible (Fig.2).

![](./images/811669115868545027_2.jpg)
![](./images/811669115868545027_3.jpg)
![](./images/811669115868545027_4.jpg)
![](./images/811669115868545027_5.jpg)

$J_1$
$J_2$
$J_3$
$J_4$

Figure 2. Four possible diffusion mechanisms for Zr.

AA7.31.3

The first migration path $(J_1)$ involves an in-plane, inline crowdion jump from one $B_C$ site to another, via the $B_S$ site as the saddle-point configuration. The second migration path $(J_2)$ is also in-plane, but the orientation of the $B_C$ changes. In terms of geometry, this jump has the shortest displacement, and may be considered essentially as a rotation jump. The third one $(J_3)$ is an out-of-plane jump (through $C_N$) in which the orientation of the $B_C$ remains unchanged. The fourth one $(J_4)$ is out-of-plane jump (skirts O) with the orientation changed.

MD simulation for the self-interstitial diffusion is performed for temperatures of 1100K, 1000K, 800K, 710K, 600K, 530K, and 500K respectively. The total simulation time for each case is 8 ns. To identify the interstitial, the Wigner-Seitz cell centered at the lattice sites containing more than one atom is first located. By relating the displacements of each atom in this Wigner-Seitz cell to the lattice site, we can identify the interstitial with the largest displacement. The crowdion's orientation is determined by identifying the closest atom to the interstitial. This process is repeated every 100fs, after the simulation system reaches equilibrium.

The diffusion coefficient is determined using the method initiated by Guinan [32]. The simulation time is partitioned into a number of equal-time intervals. The total square displacement of the interstitial as a function of time is calculated by $R^2 = \sum_{j} (\mathbf{r}_j - \mathbf{r}_{j-1})^2$, where $\mathbf{r}_j$ is the position of the interstitial at the end of the $j$-th interval and the summation runs over all intervals. In the present calculation, the duration of the intervals varies from 5 ps to 200 ps at 5ps increment. The diffusion coefficient $D_c$ along the $\mathbf{c}$-direction is first obtained by taking the average value of $(z_j - z_{j-1})^2 / 2\Delta t$ running over all intervals. The Arrhenius relation of $D_c$ vs $T_m/T$ is plotted in Fig.3. Since two mechanisms contribute to $D_c$, we choose a fitting line with a form that having two components. The resulting pre-factors and migration energies are $D_{co3}=6.25\times10^{-4} cm^2/s$, $E_{m3}=0.14eV$ and $D_{co4}=6.25\times10^{-4} cm^2/s$, $E_{m4}=0.14eV$ respectively.

![](./images/811669115868545027_6.jpg)

Figure 3. Arrhenius plot of the diffusion coefficient along $\mathbf{c}$ direction $(D_c)$ vs temperature. The solid circles are simulation results. The line represents the fitted function.

The diffusion coefficient on the basal plane $(D_a)$ is plotted in Fig.4. The total $D_a$ consists of four components, two of which has been determined through $D_c$. The line is the best fitted to:

$$
D_{a}=\frac{1}{4} v_{01} \exp (-E_{m 1} / \kappa T) a^{2}+\frac{1}{16} v_{02} \exp (-E_{m 2} / \kappa T) a^{2}+\frac{1}{12} v_{03} \exp (-E_{m 3} / \kappa T) a^{2}+\frac{1}{48} v_{04} \exp (-E_{m 4} / \kappa T) a^{2},
$$

AA7.31.4

where $v_{01}$, $E_{m2}$ are the fitted variables, with $E_{m1}=0.01$eV, $v_{02}=v_{03}$ . The Arrhenius plot of $D_{a}$ is presented in Fig.4.

![](./images/811669115868545027_7.jpg)

Figure 4. Arrhenius plot of the diffusion coefficient ($D_{a}$) on basal plane vs temperature. The solid circles represent the MD results. The line is the fitted function.

Note that at low temperatures, $D_{a}$ is practically independent of temperature. This is due to the dominance of the low-activation in-plane in-line crowdion jumps at these temperatures.

To confirm the dynamic calculation, we also use MS to calculate the migration energy and migration path. We restrain the movement of the interstitial on a series of planes perpendicular to the line connecting the two jump sites and let the other atoms fully relax. For $J_{1}$, a smooth migration path and the minimal migration barrier can be easily located. However, a smooth path for the other three mechanisms cannot be obtained. To simplify, we constrain the movement of interstitial to the line directly connecting the two jump-sites. We note that to prevent atoms from moving as a block following the interstitial during the relaxation, several atoms at the corners of the simulation cell are fixed in these calculations.

The prefactors and migration energies for the four mechanisms are presented in Table 2.

Table 2: Activation energies $E_{\text{m}}$ for different mechanism ($J_{1}$ … $J_{4}$) as observed by MD simulation. $D_{\text{o}}$ is pre-factor obtained from MD, and $E_{\text{s}}$ is activation energy from MS simulation.

<table>
  <thead>
    <tr>
      <th></th>
      <th>$J_{1}$</th>
      <th>$J_{2}$</th>
      <th>$J_{3}$</th>
      <th>$J_{4}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$E_{\text{m}}$ (eV)</td>
      <td>0.01</td>
      <td>0.25</td>
      <td>0.14</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td>$D_{\text{o}}$ ($\text{cm}^{2}/\text{s}$)</td>
      <td>$3.48×10^{-4}$</td>
      <td>$1.23×10^{-4}$</td>
      <td>$6.25×10^{-4}$</td>
      <td>$6.25×10^{-4}$</td>
    </tr>
    <tr>
      <td>$E_{\text{s}}$ (eV)</td>
      <td>0.01</td>
      <td>0.24</td>
      <td>0.16</td>
      <td>0.16</td>
    </tr>
  </tbody>
</table>

For in-plane diffusion, the MD results agree well with those from MS. However, for the out of plane components, the MD activation energies are slightly lower than those from MS. This may be because the diffusion paths for $J_{3}$ and $J_{4}$ are not the optimum ones in the MS calculations.

The anisotropy factor $p=(D_{c}/D_{a})^{1/6}$ for interstitial diffusion in Zr has been obtained by fitting to HVEM measured loop growth rates [15], assuming that the vacancy migration is isotropic. From the present results, the anisotropy factor $p$ is calculated and was found to agree well with those determined from experimental results.

AA7.31.5

## CONCLUSIONS

In this paper self-interstitials diffusion in $\alpha$-Zr is studied by using MD and MS with Ackland's interatomic potential. The basal crowdion configuration is found to be the ground state. Four types of diffusion jumps can be identified. The in-plane migration mechanism is dominated by one-dimensional crowdion motion, which changes direction from time to time, along the $[11\overline{2}0]$ directions. The activation energies for the diffusion process are obtained. The diffusion anisotropy factor $\mathrm{D}_{\mathrm{c}} / \mathrm{D}_{\mathrm{a}}$ is obtained and compares well with the experimental results.

## ACKNOWLEDGEMENT

The work described in this paper was supported by grants from the Research Grants Council of the Hong Kong Special Administrative Region (PolyU 5123/98E, PolyU 1/99C), and a grant from the Hong Kong PolyU (G-T055).

## REFERENCES

[1]. P.T. Nettley, H. Bridge and J.H.S. Simmons, *J. Brit. Nucl. Energy Soc.* **2**, 276 (1963).
[2]. B.T. Kelly, Second Conference On Industry Carbon and Graphite, *Society of Chemical Industry*, London (1966).
[3]. P.T. Nettley, J.E. Brocklehurst, W.H. Martin, J.H.S. Simmons, *Advanced and High-Temperature Gas Cooled Reactors* (Vienna:IAEA) (1969) p.603.
[4]. B.T. Kelly, B.S. Gray, W.H. Martin, V.C. Howard and M.J. Jenkins, *Society of Chemical Industry*, London (1966), p.499.
[5]. *Proceedings of the International Conference on Peaceful Uses of Atomic Energy*, Geneva, 1955, Volume 7, United Nations (1956).
[6]. S.N. Buckley, *Properties of Reactor Materials and Effects of Irradiation Damage*, p.413, Butterworth, London (1962).
[7]. *Fundamental Mechanisms of Radiation Induced Creep and Growth*, eds. G.J.C. Carpenter, C.E. Coleman, S.R. MacEwen, *J. Nucl. Mater.* **90** (1980).
[8]. ASTM STP 633 (1977).
[9]. *Fundamental Mechanisms of Radiation Induced Creep and Growth*, eds. C.H. Woo and R.J. McElroy, *J. Nucl. Mater.* **159** (1988).
[10]. C.H. Woo and U. Goesele, *J. Nucl. Mater.* **119**, 219 (1983).
[11]. C.H. Woo, *J. Nucl. Mater.* **159**, 237 (1988).
[12]. C.H. Woo, *ASTM STP* **955**, 70 (1987).
[13]. R.A. Holt, C.H. Woo and C.K. Chow, *J. Nucl. Mater.* **205**, 293 (1993).
[14]. C. H. Woo, R.A. Holt and M. Griffith, "Anisotropic Diffusion of Point Defects: Effects on Irradiation Deformation", *Materials Modeling: from Theory to Technology*. Institute of Physics Publishing, Bristol and Philadelphia, 1992, p.55.
[15]. C.H. Woo, *Radiation Effects and Defects in Solids*, **144**, 145 (1998).
[16]. M. Fuse, *J. Nucl. Mater.* **136**, 250 (1985).
[17]. A.M. Monti, *Mater. Sci. Forum* **15-18**, 863 (1987).
[18]. A.M. Monti, A. Sarce, N. S. Grande, *Phil. Mag.* A **63**, 925 (1991).
[19]. G.J. Ackland, S.J. Wooding and D.J. Bacon, *Phil. Mag.* A **71**, 553 (1995).
[20]. D.J. Oh and R.A. Johnson, *J. Mater. Res.* **3** (1989) 471
[21]. M. Igarashi, M. Khantha, and V. Vitek, *Phil. Mag.* B, **63**, 603 (1991).

AA7.31.6

[22]. J.R. Fernandez, A.M. Monti, and R.C. Pasianot, *J. Nucl. Mater.* **229**, 1 (1995).

[23]. S.J. Wooding and D.J. Bacon, *Phil. Mag,* **76**, 1033 (1997).

[24]. S.J. Wooding, L.M. Howe, F. Gao, A.F. Calder and D.J. Bacon, *J. Nucl. Mater.* **254**, 191 (1998).

[25]. R.C. Pasianot, A.M. Monti, *J.Nucl. Mater.* **276**, 230 (2000).

[26]. D.J. Bacon, *J. Nucl. Mater.* **159**, 176 (1988).

[27]. G.M. Hood, H. Zhou, D. Gupta, R.J. Shultz, *J.Nucl. Mater.* **233**, 122 (1995).

[28]. O.F.Sankey, D.J.Niklewsky, D.A.Drabold, J.D.Dow, *Phys. Rev.* B **41**, 12750 (1990).

[29]. M. Parrinello and A. Rahman, *J. Appl. Phys.* **52**, 7182 (1981).

[30]. R.C. Pasianot, A.M. Monti, *J. Nucl. Mater.* **264**, 198 (1999).

[31]. M. Wen, C.H. Woo and H.C. Huang, *J. Comp. Aided Mater. Design.,* **7**, 97 (2000)

[32]. A.M. Guinan, R.N. Stuart and R.J. Borg, *Phys. Rev.* B **15**, 699 (1977).

AA7.31.7