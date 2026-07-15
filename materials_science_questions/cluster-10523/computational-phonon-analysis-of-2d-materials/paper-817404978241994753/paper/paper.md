**Negative thermal expansion in CdSe quasi-two-dimensional nanoplatelets**

Alexander I. Lebedev*

Physics Department, Moscow State University, 119991 Moscow, Leninskie gory, Russia

![](./images/817404978241994753_1.jpg)
(Received 12 April 2019; revised manuscript received 15 June 2019; published 24 July 2019)

The in-plane coefficient of thermal expansion (CTE) for CdSe nanoplatelets with the zinc-blende structure containing from two to five monolayers is calculated from first principles within the quasiharmonic approximation. A comparison of the obtained results with those for bulk CdSe with both the zinc-blende and wurtzite structures finds a significant increase in the magnitude of negative CTE and the temperature range of its observation in nanoplatelets. The main contribution to the negative thermal expansion in CdSe nanoplatelets is given by the out-of-plane flexural ZA mode and in-plane optical $E$ modes that arise from the folding of TA phonon of bulk CdSe.

DOI: 10.1103/PhysRevB.100.035432

### I. INTRODUCTION

The physical properties of nanoplatelets are qualitatively different from those of bulk materials. In addition to the well-known size effect in semiconductors, the quasi-2D character of nanoplatelets results in changes of their vibrational spectra and associated physical properties (sound velocity, heat capacity, thermal conductivity, infrared absorption, etc.) as well as in more subtle effects associated with electron-phonon interaction, such as the temperature dependence of the forbidden band gap. Numerous experiments have shown that the temperature dependence of the forbidden band gap in nanoscale semiconductors depend on the size of nanoparticles [1–3] as well as on their shape [4]. Since one of the contributions to this dependence results from the thermal expansion, the study of this effect in nanoplatelets is an actual problem.

The nanoparticles of cadmium chalcogenides, and in particular CdSe, have attracted considerable attention due to their unique optical properties which can be controlled by the size effect or by creating nanoheterostructures. These properties are promising for various applications in nano- and optoelectronics (see Ref. [5] and references therein). It is known that the thermodynamically stable modification of bulk CdSe is the hexagonal wurtzite structure. However, CdSe can exist in a metastable cubic zinc-blende (sphalerite) structure. Due to this metastability, the experimental data on the properties of zinc-blende CdSe are limited. In particular, the thermal expansion was studied only for the hexagonal CdSe [6] (see also the preliminary data in Refs. [7,8]). At low temperature, this phase exhibits a negative thermal expansion [9]. CdSe nanoplatelets, depending on the preparation conditions, can be obtained in both the zinc-blende and wurtzite modifications [10,11].

Theoretical calculations of the thermal expansion in bulk CdSe with wurtzite [12] and zinc-blende [12,13] structures were performed earlier using the quasiharmonic Debye model. These calculations, however, can hardly be considered as reliable since the existence of the optical vibrations was neglected in them, and the anisotropy of the crystal structure was not taken into account when calculating the properties of hexagonal CdSe.

In this work, the temperature dependence of the in-plane coefficient of thermal expansion (CTE) for CdSe nanoplatelets with the zinc-blende structure and a thickness from two to five monolayers (ML) as well as for bulk CdSe crystals with both the zinc-blende and wurtzite structures are calculated from first principles within the quasiharmonic approximation. The influence on the thermal expansion of the F, Cl, and Br terminating atoms, which are used to compensate for an extra charge produced by an extra Cd layer on the surface of the nanoplatelets, was also studied. So far, the thermal expansion of quasi-2D structures was investigated using this technique for graphene [14–17], hexagonal BN [15,17], transition metal dichalcogenides [15,18,19], black and blue phosphorene [20–22], silicene [21], and germanene [21]. Molecular dynamics is another technique that was used to study the thermal expansion in quasi-2D carbon nanostructures [23–25] and BN [26].

### II. QUASIHARMONIC APPROXIMATION

The thermal vibrations of atoms in solids are not strictly harmonic. The nonlinear dependence of interatomic forces on the interatomic distances results in the appearance of anharmonicity, the interaction of different vibrational modes, and the thermal expansion of a solid. Rigorous treatment of the anharmonicity requires the use of molecular dynamics with quantum-mechanical calculation of forces acting on atoms, but often a fairly good estimate of the thermodynamic properties can be obtained using the quasiharmonic approximation (QHA).

The QHA assumes that, when the temperature is varied, the individual vibrational modes remain independent and harmonic, and the anharmonicity effects can be taken into account via the dependence of phonon frequencies $\omega_j$ on the unit cell volume $V_0$. As in ordinary thermodynamics, in this approach all the details of the microscopic interactions

*swan@scon155.phys.msu.ru

between atoms are hidden and only the consequences of these interactions (thermal expansion, changes in vibrational frequencies, etc.) are considered by expressing them using thermodynamic parameters. This enables one to predict the macroscopic properties of solids at the thermodynamic level, using such concepts as temperature $T$, pressure $P$, free energy $F$, volume $V$, etc., but remaining strictly based on first-principles calculations of phonon frequencies.

In the QHA, the free energy of a crystal unit cell is a sum of its total energy $E_{\text{tot}}$ calculated using the density functional theory and the free energy of a system of noninteracting harmonic oscillators $F_{\text{vib}}$:

$$
F(V_0, T) = E_{\text{tot}}(V_0) + F_{\text{vib}}(V_0, T), \tag{1}
$$

$$
F_{\text{vib}}(V_0, T) = \frac{1}{N_q} \sum_{j\mathbf{q}} \left[ \frac{\hbar\omega_{j\mathbf{q}}}{2} + kT \ln(1 - e^{-\hbar\omega_{j\mathbf{q}}/kT}) \right]. \tag{2}
$$

Here the sum runs over all phonon branches $j$ and all wave vectors $\mathbf{q}$ of the Brillouin zone; $N_q$ is the number of different wave vectors.

At $T \neq 0$, the thermodynamic equilibrium is reached at a volume $V_0(T)$ satisfying the condition $\partial F(V_0, T)/\partial V_0 = 0$. Taking into account Eq. (1), this condition can be rewritten as

$$
\begin{aligned}
\frac{\partial F(V_0, T)}{\partial V_0} &= \frac{dE_{\text{tot}}(V_0)}{dV_0} + \frac{\partial F_{\text{vib}}(V_0, T)}{\partial V_0} \\
&= -P(V_0) - P_{\text{vib}}(V_0, T) = 0,
\end{aligned} \tag{3}
$$

i.e., the thermodynamic equilibrium is reached at $P(V_0) = \partial F_{\text{vib}}(V_0, T)/\partial V_0$. This enables one to calculate the $V_0(T)$ dependence and find the CTE.

In anisotropic crystals whose symmetry is lower than the cubic one, the volume and derivatives with respect to volume are not correct thermodynamic parameters. In this case, an approach can be used in which independent lattice parameters are used instead of the volume (see, for example, Ref. [27]). In this work, the strain tensor $u_{ij}$ and the stress tensor $\sigma_{ij} = -(1/V_0)\partial F_{\text{vib}}/\partial u_{ij}$ are used as parameters describing the deformation effects.

### III. CALCULATION DETAILS

The calculations presented in this work were performed within the plane-wave density functional theory using the ABINIT software package. The local density approximation (LDA) and optimized norm-conserving separable pseudopotentials constructed using the RRKJ scheme [28] were used in the calculations [29]. The cutoff energy was 30 Ha (816 eV); the integration over the Brillouin zone was carried out using $8 \times 8 \times 8$ and $8 \times 8 \times 6$ Monkhorst-Pack meshes for cubic and hexagonal crystals, respectively. When modeling nanoplatelets, the $8 \times 8 \times 1$ mesh was used. The relaxation of the unit cell parameters and atomic positions was carried out until the forces acting on the atoms became less than $2 \times 10^{-6}$ Ha/Bohr (0.1 meV/Å). The accuracy of calculating the total energy was better than $10^{-10}$ Ha.

To calculate the volume dependence of the electronic contribution $E_{\text{tot}}(V)$ for bulk zinc-blende CdSe [Fig. 1(a)], we first determined the equilibrium lattice parameter $a_0$ and the dependence of a mechanical stress $\sigma_{xx} = \sigma_{yy} = \sigma_{zz}$ in the unit cell as a function of its isotropic strain $u_{xx} = u_{yy} = u_{zz} = (a - a_0)/a_0$, which was varied from $-0.01$ to $0.01$ in steps of 0.005. When calculating the stress in the unit cell, we used the ability of the ABINIT program to calculate the stress tensor using the density functional perturbation theory [30]. The obtained data were then used to calculate the coefficients in the quadratic approximation $u_{xx} \approx c_1\sigma_{xx} + c_2\sigma_{xx}^2$. After that, for $u_{xx} = -0.01$, 0, and 0.01, the exact values of phonon frequencies were calculated on the $4 \times 4 \times 4$ mesh of wave vectors (64 $\mathbf{q}$ values, eight irreducible points in the Brillouin zone). Using the anaddb program, the phonon frequencies were interpolated on the $64 \times 64 \times 64$ mesh, and the vibrational contribution to the free energy $F_{\text{vib}}(u_{xx}; T)$ was calculated in the temperature range of $T = 5$-$1000$ K in steps of 5 K. For each temperature, the obtained values of $F_{\text{vib}}(u_{xx}; T)$ were approximated by a parabola, the coefficients of its derivative $[\sigma_{\text{vib}} \equiv -(1/V_0)\partial F_{\text{vib}}/\partial u_{xx} \approx A + Bu_{xx}]$ were calculated, and finally the $u_{xx}$ values, which are solutions of a system of two nonlinear equations, $\sigma_{xx} = -A - Bu_{xx}$ and $u_{xx} = c_1\sigma_{xx} + c_2\sigma_{xx}^2$, were determined. We note that the calculated value of $\partial F_{\text{vib}}/\partial u_{xx}$ is three times larger than the true value because the strain was applied three times ($u_{xx} = u_{yy} = u_{zz}$) when calculating $F_{\text{vib}}$. The derivative $du_{xx}/dT$ is the coefficient of linear thermal expansion $\alpha(T)$ of cubic CdSe.

![](./images/817404978241994753_2.jpg)

FIG. 1. Structure of bulk CdSe with (a) zinc-blende and (b) wurtzite structure and (c) the structure of CdSe nanoplatelet with a thickness of 4 ML.

For bulk CdSe with the wurtzite structure [Fig. 1(b)], the calculation scheme was similar. After the equilibrium lattice parameters $(a_0, c_0)$ were found, the internal stresses $\sigma_{xx}$ and $\sigma_{zz}$ were calculated for 13 pairs of $(u_{xx}, u_{zz})$ values, namely (0; 0), ($\pm 0.01$; 0), (0; $\pm 0.01$), ($\pm 0.005$; $\pm 0.005$), and ($\pm 0.0025$; $\pm 0.0025$). For each strain, the value of the $z$ parameter describing the relative shift of two hexagonal sublattices in the wurtzite structure was carefully optimized. The obtained data were then approximated by

formulas

$$
\begin{aligned}
& u_{x x} \approx c_{1} \sigma_{x x}+c_{2} \sigma_{x x}^{2}+c_{3} \sigma_{z z}+c_{4} \sigma_{z z}^{2}+c_{5} \sigma_{x x} \sigma_{z z}, \\
& u_{z z} \approx d_{1} \sigma_{x x}+d_{2} \sigma_{x x}^{2}+d_{3} \sigma_{z z}+d_{4} \sigma_{z z}^{2}+d_{5} \sigma_{x x} \sigma_{z z}.
\end{aligned}
\tag{4}
$$

The free energy $F_{\mathrm{vib}}(u_{xx}, u_{zz}; T)$ was calculated for the same $(u_{xx}, u_{zz})$ pairs in the temperature range of $T=5$–1000 K in steps of 5 K. For each temperature, by approximating the obtained values of $F_{\mathrm{vib}}$ by a quadratic form $F_{\mathrm{vib}} \approx e_{0}+e_{1}u_{xx}+e_{2}u_{xx}^{2}+e_{3}u_{zz}+e_{4}u_{zz}^{2}+e_{5}u_{xx}u_{zz}$, the derivatives $\sigma_{xx}=-(1/V_{0})\partial F_{\mathrm{vib}}/\partial u_{xx}$ and $\sigma_{zz}=-(1/V_{0})\partial F_{\mathrm{vib}}/\partial u_{zz}$ were calculated. After that, taking into account Eq. (4), a system of nonlinear equations was solved and the values of $u_{xx}$ and $u_{zz}$ for each $T$ were calculated. Their derivatives with respect to temperature are the coefficients of linear thermal expansion $\alpha_{xx}(T)$ and $\alpha_{zz}(T)$ of hexagonal CdSe.

CdSe nanoplatelets studied in this work were the [001]-oriented zinc-blende platelets with a thickness from two to five monolayers, both surfaces of which were terminated with cadmium atoms [Fig. 1(c)]. In order to compensate for an extra charge produced by an extra Cd layer, the simplest way of charge compensation using F, Cl, or Br terminating atoms was considered. The modeling of the nanoplatelets was carried out on supercells to which a vacuum gap of $20$ Å was added to consider nanoplatelets as noninteracting. The symmetry of supercells is described by the tetragonal $P\bar{4}m2$ space group. In Ref. [5] it was shown that the most energetically favorable position of terminating atoms is the bridge position, in which the atoms enter the positions of missing Se atoms.

For these nanoplatelets, the $\sigma_{xx}(u_{xx})$ curves and phonon spectra were calculated for biaxial strains $u_{xx}=u_{yy}$ equal to zero, $\pm0.01$, and $\pm0.02$, with full relaxation of all atomic positions for each strain. The exact phonon frequencies calculated on the $8\times8\times1$ mesh of wave vectors $\mathbf{q}$ were then used to calculate the free energy $F_{\mathrm{vib}}(u_{xx})$ on the $64\times64\times8$ mesh of interpolated frequencies.

### IV. THERMAL EXPANSION OF BULK CdSe

The calculated temperature dependence of CTE for bulk CdSe with zinc-blende and wurtzite structures as well as the available experimental data for hexagonal CdSe [6] are shown in Fig. 2. It is seen that the calculated curves are in reasonable agreement with the experiment. A discrepancy in the behavior of the curves should not be considered negatively as an ideal agreement of the curves can hardly be expected for the used approximation. A higher CTE along the $a$ axis for hexagonal CdSe is characteristic of other semiconductors with the wurtzite structure [6]. The CTE curve for the cubic CdSe is located between two curves for the hexagonal structure.

An interesting feature of the obtained curves is the negative thermal expansion at low temperatures. This effect is well known in semiconductors with diamond, zinc-blende, and wurtzite structures [31–34]. By differentiating Eq. (1) first with respect to volume and then with respect to temperature,

![](./images/817404978241994753_3.jpg)

FIG. 2. Coefficient of linear thermal expansion for bulk CdSe crystals with zinc-blende and wurtzite structures. The points are experimental data for hexagonal CdSe [6].

the linear CTE of a crystal can be written as

$$
\begin{aligned}
\alpha & =\frac{A_{0}}{V_{0}} \frac{1}{N_{q}} \sum_{j \mathbf{q}} \gamma_{j \mathbf{q}} \hbar \omega_{j \mathbf{q}} \frac{d}{d T}\left(\frac{1}{e^{\hbar \omega_{j \mathbf{q}} / k T}-1}\right) \\
& =\frac{A_{0}}{V_{0}} \frac{k}{N_{q}} \sum_{j \mathbf{q}} \gamma_{j \mathbf{q}} \frac{\left(\hbar \omega_{j \mathbf{q}} / k T\right)^{2}}{2\left[\cosh \left(\hbar \omega_{j \mathbf{q}} / k T\right)-1\right]},
\end{aligned}
\tag{5}
$$

where $\gamma_{j\mathbf{q}}=-d\ln\omega_{j\mathbf{q}}/d\ln V_{0}$ is the Grüneisen parameter for mode $j$ with the wave vector $\mathbf{q}$ and $A_{0}=1/(3B_{0})$, where $B_{0}$ is the bulk modulus. From this formula it follows that for a negative thermal expansion to appear, it is necessary that some modes have a negative sign of $\gamma$. For most modes in crystals, the interatomic forces weaken when the lattice is stretched, and therefore the Grüneisen parameters for them are positive. An analysis of the volume dependence of the frequencies of different modes in zinc-blende semiconductors found negative $\gamma$ parameters for transverse acoustic (TA) phonons near the $X$ and $L$ points of the Brillouin zone [35]. This effect was explained by the influence of the strain on the magnitude of restoring forces that act on the atoms oscillating in a direction perpendicular to the direction of the chemical bond. The mechanism of the negative thermal expansion in wurtzite semiconductors is similar to that proposed for zinc-blende semiconductors; however, the negative Grüneisen parameter in the wurtzite structure may also appear for TO modes and even LA mode [36].

### V. PHONON SPECTRA AND THERMAL EXPANSION OF CdSe NANOPLATELETS

The phonon spectrum of a typical quasi-two-dimensional F-terminated CdSe nanoplatelet with the zinc-blende structure is shown in Fig. 3 [37]. The two-dimensional character of the phonon spectrum is confirmed by the absence of a dispersion of the phonon modes in the $q_{z}$ direction normal to the plane of the nanoplatelet.

A detailed analysis of phonon spectra of CdSe nanoplatelets was carried out in Ref. [37]. It was shown that

![](./images/817404978241994753_4.jpg)

FIG. 3. Phonon spectra of 3 ML CdSe nanoplatelet terminated with F atoms (black lines) and bulk CdSe (red lines). Blue lines show acousticlike $E$ modes with a negative Grüneisen parameter and green lines show surface modes with a negative Grüneisen parameter.

![](./images/817404978241994753_5.jpg)

FIG. 4. Coefficient of linear thermal expansion of F-terminated CdSe nanoplatelets with a thickness from 2 ML to 5 ML and for 3 ML nanoplatelets terminated with F, Cl, and Br atoms.

the phonon spectrum of a CdSe nanoplatelet with a thickness of $n$ ML consists of three types of optical modes: $n$ symmetric quasi-Lamb $A_1$ modes, $n$ antisymmetric quasi-Lamb $B_2$ modes (in both modes the atomic displacements are out of plane), and $2n$ modes of symmetry $E$ with the in-plane atomic displacements. Almost all optical modes have a mixed acoustic + optic character. The lower-energy part of these modes has an acousticlike displacement pattern, whereas the higher-energy part has an opticlike one. The acoustic vibrations are presented by one LA and one TA phonons, in which the atoms move in the plane of the nanoplatelet, and the flexural $B_2$ mode (ZA mode), in which the atoms move in the out-of-plane direction. Terminating atoms produce six surface modes. The specific feature of the phonon spectrum of nanoplatelets is a large number of modes that arise from the folding of acoustic and optical modes of bulk CdSe, as was demonstrated by the mode projection analysis.

Calculations of the thermal expansion of nanoplatelets reveal the appearance of a large negative in-plane CTE which appreciably exceeds its magnitude in bulk CdSe (compare Figs. 2 and 4). The reasons for this may be an increase in the negative values of $\gamma$ for some modes and an increase in the number of modes with negative $\gamma$ (a change in the phonon density of states).

We consider first a possible change in the phonon density of states (DOS). The phonon DOS calculated for CdSe nanoplatelets and bulk CdSe are shown in Fig. 5. Four regions with frequency ranges of 0–70, 70–160, 160–260, and 260–$400\ \text{cm}^{-1}$ are clearly seen in the figure. They correspond to regions with a predominant contribution of acoustic (ZA, TA, LA) phonons, acousticlike $E$ and quasi-Lamb modes, opticlike $E$ and quasi-Lamb modes, and vibrations of terminating atoms, respectively. An analysis shows that in going from bulk CdSe to the thinnest of nanoplatelets, the number of modes in the 0–70 and 160–260 $\text{cm}^{-1}$ regions systematically decreases, whereas the number of phonon modes in the 70–160 $\text{cm}^{-1}$ region increases by more than 1.5 times. One can see, however, that the changes in the phonon DOS are insufficient to explain the strong increase in the negative in-plane CTE in nanoplatelets.

Calculations of the Grüneisen parameters $\gamma_j = -d\ln\omega_j/d\ln a$ ($a$ is the in-plane lattice parameter of the nanoplatelet) find a large number of modes with negative $\gamma$ (Fig. 6). In contrast to bulk CdSe, in which the only mode that has a negative $\gamma$ is the TA mode (see Fig. S1 in the Supplemental Material [38]), in nanoplatelets, in addition to ZA and TA acoustic modes, there are $n$ optical $E$ modes ($n$ is the thickness of the nanoplatelet) and two surface $E$ modes which have a negative $\gamma$. All quasi-Lamb modes ($A_1$ and $B_2$) as well as the highest-energy vibrational mode of terminating halogen atoms have $\gamma > 0$. As was shown in Ref. [37], the low-frequency optical $E$ modes arise from the folding of TA phonon mode which is responsible for a negative thermal expansion in bulk CdSe. From Fig. 6 it is seen that a region with a large negative $\gamma$ for the ZA mode

![](./images/817404978241994753_6.jpg)

FIG. 5. Normalized phonon density of states for F-terminated CdSe nanoplatelets with a thickness from 2 ML to 5 ML and for bulk CdSe.

![](./images/817404978241994753_7.jpg)

FIG. 6. Grüneisen parameter of different modes in F-terminated CdSe nanoplatelet with a thickness of 3 ML as a function of wave vector.

spans over a small part of the Brillouin zone near the $\Gamma$ point, and so its contribution to the negative CTE is limited. In contrast, the region of smaller negative $\gamma$ for TA, $E$, and surface modes is located near the $\Delta$ axis and spans over a larger volume of $\mathbf{k}$ space. That is why its contribution to the negative thermal expansion may be comparable with that of the ZA mode, especially if one takes into account that the number of the optical modes with negative $\gamma$ exceeds the number of acoustic modes.

When the terminating F atoms are replaced by Cl and then by Br, the phonon DOS remains nearly unchanged (see Fig. S2 in the Supplemental Material [38]), but the magnitudes of both positive and negative values of $\gamma$ decrease. The averaged $\gamma$ value in the frequency range above $160\ \mathrm{cm}^{-1}$ decreases strongly. These changes explain the evolution of the CTE curves on Fig. 4 when increasing the mass of the terminating atom.

A comparison of the Grüneisen parameters for modes in F-terminated nanoplatelets with different thickness shows that, when increasing thickness, the magnitude of the negative $\gamma$ values in two low-frequency regions of modes decreases strongly, whereas the $\gamma$ values for modes associated with vibrations of terminating F atoms increase monotonically. From Eq. (5) it follows that, at a given temperature, the CTE value is approximately proportional to the averaged $\gamma$ value of all modes with an energy of $\hbar\omega \lesssim 3kT$. This explains all the systematic changes in the CTE curves observed in Fig. 4. A wider temperature range in which the negative thermal expansion is observed in CdSe nanoplatelets as compared to bulk CdSe (compare Figs. 2 and 4) is explained by the fact that the energy of TA phonon in bulk CdSe does not exceed $59\ \mathrm{cm}^{-1}$, whereas in the nanoplatelets the energies of modes with negative $\gamma$ reach $\sim140\ \mathrm{cm}^{-1}$ (Fig. 3).

It is interesting that, in thick nanoplatelets, the CTE values at high temperatures quickly reach the values for bulk cubic CdSe. In our opinion, the reason for this is that the mechanical structure of nanoplatelets is not as rigid as the bulk cubic structure. The calculations (Table I) show that three components of the elastic compliance tensor $S_{\mu\nu}$ for nanoplatelets change slowly with increasing their thickness and tend towards the values for the cubic phase. However, for 3D and quasi-2D systems the coefficient $A_0$ that enters Eq. (5) should be different: it is $S_{11}+2S_{12}$ for cubic crystals and $S_{11}+S_{12}$ for nanoplatelets. This difference is a consequence of the fact that one cannot control the thickness of the quasi-2D system when applying the in-plane strain. Using the data from Table I, one can show that in nanoplatelets the coefficient $A_0$ is indeed larger than in the bulk crystal and it increases with increasing the nanoplatelet thickness.

<table>
<caption>TABLE I. Elastic compliance moduli of F-terminated CdSe nanoplatelets and bulk material (in $10^{-2}\ \mathrm{GPa}^{-1}$).</caption>
<thead>
<tr>
<th>Parameter</th>
<th>2 ML</th>
<th>3 ML</th>
<th>4 ML</th>
<th>5 ML</th>
<th>6 ML</th>
<th>Bulk</th>
</tr>
</thead>
<tbody>
<tr>
<td>$S_{11}$</td>
<td>$5.477$</td>
<td>$4.707$</td>
<td>$4.395$</td>
<td>$4.218$</td>
<td>$4.105$</td>
<td>$3.607$</td>
</tr>
<tr>
<td>$S_{12}$</td>
<td>$-4.101$</td>
<td>$-3.057$</td>
<td>$-2.618$</td>
<td>$-2.372$</td>
<td>$-2.209$</td>
<td>$-1.524$</td>
</tr>
<tr>
<td>$S_{66}$</td>
<td>$3.653$</td>
<td>$3.743$</td>
<td>$3.799$</td>
<td>$3.832$</td>
<td>$3.856$</td>
<td>$4.017$</td>
</tr>
</tbody>
</table>

Another interesting effect is the negative CTE observed in the 2 ML nanoplatelet in the whole temperature range. Formally, according to Eq. (5), at high temperature this situation is possible if the sum of Grüneisen parameters over all branches and wave vectors is negative. Direct calculations show that this is the case. The physical explanation of this effect is simple: the out-of-plane thermal motion of very thin nanoplatelets results in shrinking of the nanoplatelets in the basal plane.

First-principles calculations of the negative thermal expansion in monolayer graphene [14–17], $h$-BN [15], transition metal dichalcogenides [15,19], and blue and black phosphorene [21,22] have shown that it is mainly determined by the ZA phonon—a flexural mode, which has a negative $\gamma$ value and in which atoms move normal to the monolayer. In monolayer graphene, there exists an additional optical ZO mode with a small negative $\gamma$ ($\gamma>-1$) [39], but the frequency of this mode is $\sim900\ \mathrm{cm}^{-1}$ and so its contribution to the CTE can be seen well above the room temperature. In bilayer and multilayer graphene, there appears a new optical $ZO'$ mode, in which the out-of-plane atomic displacements are in phase in the same layer and out of phase in adjacent layers. This mode has a negative $\gamma$ ($\gamma>-7$) [39]. A similar mode with a negative $\gamma$ is typical of graphite [14]. In black phosphorene, the ZO mode with a frequency of $\sim130\ \mathrm{cm}^{-1}$ is also characterized by a negative $\gamma$ [22]. We note that all the above-mentioned optical modes in monolayers are polarized normal to the nanoplatelet. In $\mathrm{MoTe}_2$ and $\mathrm{WTe}_2$, in which the monolayer consists of three atomic layers, in addition to the ZA mode with a negative $\gamma$ there appear acoustic LA and TA modes with an in-plane polarization, which also have small negative $\gamma$ values ($\gamma>-1.4$) [19]. The TA and LA modes with a negative $\gamma$ were also observed in monolayers of silicene, germanene [21], and blue and black phosphorene [22].

An analysis of Fig. 6 finds a large contribution of the ZA and TA acoustic modes to the negative thermal expansion in CdSe nanoplatelets. However, the most interesting result is that the negative $\gamma$ is also characteristic of the in-plane optical and surface modes of $E$ symmetry. It looks like this is a first

observation of negative $\gamma$ for optical modes with in-plane po- larization in quasi-2D systems. This result is not much surpris- ing if one recalls that these optical modes originate from the folding of the TA phonon mode of bulk CdSe with a negative $\gamma$. The origin of such a behavior results from the zinc-blende structure of our nanoplatelets. For an unstrained nanoplatelet, the restoring force for acousticlike optical phonons with the [110] polarization is produced by bending of Cd–Se chemi- cal bonds. However, when the nanoplatelet is stretched, the strained chemical bonds produce increased restoring forces that increase the vibrational frequencies. In our opinion, this effect can be observed in other quasi-2D multilayer systems with strong enough interaction between the layers. Indeed, our calculations for twelve quasi-2D systems (see the Sup- plemental Material [38]) find a negative $\gamma$ for in-plane optical modes in two-layer graphene, silicene, germanene, blue and black phosphorene, SiC, BN, SnS, and TiO₂.

The calculated CTE values for CdSe nanoplatelets enable one to estimate the contribution of the thermal expansion to the temperature dependence of their forbidden band gap $E_g$. Calculations show that the change in the band gap upon the bi- axial stretching is $dE_g/du_{xx}=4.06$ eV for 3 ML nanoplatelet and 3.09 eV for 5 ML one. Thus the contribution of the thermal expansion to the temperature dependence $dE_g/dT$ does not exceed $+1.2\times10^{-5}$ eV/K at 300 K. This means that the large negative $dE_g/dT$ values observed in CdSe nanoparticles result from the electron-phonon interaction.

In Refs. [40,41] it was suggested that materials that exhibit negative thermal expansion can also demonstrate pressure- induced softening, i.e., negative $B'=dB_0/dP$ values, where $B_0$ is the bulk modulus. Although quasi-two-dimensional CdSe nanoplatelets studied in this work are not bulk materials, they exhibit a negative thermal expansion and so it was inter- esting to check whether they will exhibit a pressure-induced softening. The calculations showed (see the Supplemental Material [38]) that $d(C_{11}+C_{12})/d\sigma_{xx}$ is positive in CdSe nanoplatelets and therefore they do not exhibit a pressure- induced softening. The absence of this effect is probably due to the structure of the nanoplatelets, in which tetrahedra are tightly linked together. This structure has no intermediate chains or other elements that appear in zeolites and Zn(CN)₂, in which the pressure-induced softening occurs.

## VI. CONCLUSIONS

In this work, the in-plane coefficient of thermal expansion of CdSe nanoplatelets with the zinc-blende structure con- taining from two to five monolayers is calculated from first principles within the quasiharmonic approximation. Like in other quasi-2D systems, the negative thermal expansion in CdSe nanoplatelets is more pronounced and is observed in a wider temperature range as compared to bulk CdSe. One of the origins of the negative thermal expansion is the flexural acoustic (ZA) mode, which is a common feature of all quasi- 2D systems. However, in contrast to all earlier studied quasi- 2D systems, in CdSe nanoplatelets there is another valuable contribution to the negative thermal expansion resulting from acousticlike optical $E$ phonons and surface $E$ modes. It is shown that optical modes with the in-plane polarization and negative Grüneisen parameter are also characteristic of most two-layer quasi-2D systems.

The obtained results are quite expected. The acousticlike optical modes originate from the folding of the TA mode of bulk CdSe when constructing a multilayer nanoplatelet. As this TA mode has a negative Grüneisen parameter at all $\mathbf{q}$, it is not surprising that in nanoplatelets both TA and acousticlike optical modes also have a negative Grüneisen parameter. The only difference between the acousticlike and TA modes is that in the TA mode the atomic displacements are in-phase in all layers of the nanostructure, whereas in the optical modes there are phase shifts between these displacements. These modes have comparable frequencies and Grüneisen parameters and so their contribution to the thermal expansion should be comparable. The contribution of the flexural ZA mode decreases with increasing thickness of the nanoplatelet because thick nanoplatelets are less prone to buckling. These simple reasonings explain how the evolution of the phonon spectra when going from 2D to 3D systems influences the thermal expansion.

## ACKNOWLEDGMENT

This work was supported by the Russian Foundation for Basic Research (Grant No. 17-02-01068).

[1] A. Olkhovets, R.-C. Hsu, A. Lipovskii, and F. W. Wise, *Phys. Rev. Lett.* **81**, 3539 (1998).

[2] Q. Dai, Y. Song, D. Li, H. Chen, S. Kan, B. Zou, Y. Wang, Y. Deng, Y. Hou, S. Yu, L. Chen, B. Liu, and G. Zou, *Chem. Phys. Lett.* **439**, 65 (2007).

[3] B. Pejova, B. Abay, and I. Bineva, *J. Phys. Chem. C* **114**, 15280 (2010).

[4] A. Al Salman, A. Tortschanoff, M. B. Mohamed, D. Tonti, F. van Mourik, and M. Chergui, *Appl. Phys. Lett.* **90**, 093104 (2007).

[5] R. B. Vasiliev, A. I. Lebedev, E. P. Lazareva, N. N. Shlenskaya, V. B. Zaytsev, A. G. Vitukhnovsky, Y. Yao, and K. Sakoda, *Phys. Rev. B* **95**, 165414 (2017).

[6] H. Iwanaga, A. Kunishige, and S. Takeuchi, *J. Mater. Sci.* **35**, 2451 (2000).

[7] D. Berlincourt, H. Jaffe, and L. R. Shiozawa, *Phys. Rev.* **129**, 1009 (1963).

[8] Y. S. Touloukian, R. K. Kirby, R. E. Taylor, and T. Y. R. Lee, *Thermophysical Properties of Matter—the TPRC Data Series* (IFI/Plenum, New York, 1977), Vol. 13, pp. 1185–1186.

[9] R. R. Reeber, Ph.D. thesis, Ohio State University, 1968.

[10] S. Ithurria and B. Dubertret, *J. Am. Chem. Soc.* **130**, 16504 (2008).

[11] J. S. Son, X.-D. Wen, J. Joo, J. Chae, S.-i. Baek, K. Park, J. H. Kim, K. An, J. H. Yu, S. G. Kwon, S.-H. Choi, Z. Wang, Y.-W. Kim, Y. Kuk, R. Hoffmann, and T. Hyeon, *Angew. Chem.* **48**, 6861 (2009).

[12] J.-J. Tan, Y. Cheng, W.-J. Zhu, and Q.-Q. Gou, *Commun. Theor. Phys.* **50**, 220 (2008).

035432-6

[13] S. Ouendadji, S. Ghemid, H. Meradji, and F. H. Hassan, Comput. Mater. Sci. **50**, 1460 (2011).

[14] N. Mounet and N. Marzari, *Phys. Rev. B* **71**, 205214 (2005).

[15] C. Sevik, *Phys. Rev. B* **89**, 035422 (2014).

[16] J.-W. Jiang, B.-S. Wang, J.-S. Wang, and H. S. Park, *J. Phys.: Condens. Matter* **27**, 083001 (2015).

[17] S. Mann, R. Kumar, and V. K. Jindal, *RSC Adv.* **7**, 22378 (2017).

[18] L. F. Huang, P. L. Gong, and Z. Zeng, *Phys. Rev. B* **90**, 045409 (2014).

[19] Z.-Y. Wang, Y.-L. Zhou, X.-Q. Wang, F. Wang, Q. Sun, Z.-X. Guo, and Y. Jia, *Chin. Phys. B* **24**, 026501 (2015).

[20] Y. Aierken, D. Çakir, C. Sevik, and F. M. Peeters, *Phys. Rev. B* **92**, 081408(R) (2015).

[21] X.-J. Ge, K.-L. Yao, and J.-T. Lü, *Phys. Rev. B* **94**, 165433 (2016).

[22] H. Sun, G. Liu, Q. Li, and X. Wan, *Phys. Lett. A* **380**, 2098 (2016).

[23] P. K. Schelling and P. Keblinski, *Phys. Rev. B* **68**, 035425 (2003).

[24] K. V. Zakharchenko, M. I. Katsnelson, and A. Fasolino, *Phys. Rev. Lett.* **102**, 046808 (2009).

[25] M. Pozzo, D. Alfè, P. Lacovig, P. Hofmann, S. Lizzit, and A. Baraldi, *Phys. Rev. Lett.* **106**, 135501 (2011).

[26] G. J. Slotman and A. Fasolino, *J. Phys.: Condens. Matter* **25**, 045009 (2013).

[27] S. Q. Wang, *Appl. Phys. Lett.* **88**, 061902 (2006).

[28] A. M. Rappe, K. M. Rabe, E. Kaxiras, and J. D. Joannopoulos, *Phys. Rev. B* **41**, 1227 (1990).

[29] For quasi-2D systems, the LDA approximation was shown to provide better results as compared to the GGA one [42]. Earlier, we used LDA when studying ferroelectric and piezoelectric properties of SnS mono- and multilayers [43].

[30] O. H. Nielsen and R. M. Martin, *Phys. Rev. B* **32**, 3792 (1985).

[31] D. F. Gibbons, *Phys. Rev.* **112**, 136 (1958).

[32] P. W. Sparks and C. A. Swenson, *Phys. Rev.* **163**, 779 (1967).

[33] R. R. Reeber and B. A. Kulp, *Trans. Metal. Soc. AIME* **233**, 698 (1965).

[34] H. Ibach, *Phys. Status Solidi B* **33**, 257 (1969).

[35] C. H. Xu, C. Z. Wang, C. T. Chan, and K. M. Ho, *Phys. Rev. B* **43**, 5024 (1991).

[36] Z. Wang, F. Wang, L. Wang, Y. Jia, and Q. Sun, *J. Appl. Phys.* **114**, 063508 (2013).

[37] A. I. Lebedev, *Phys. Rev. B* **96**, 184306 (2017).

[38] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.100.035432 for results of the Grüneisen parameter calculations for twelve quasi-2D systems and for bulk CdSe, comments on the calculating elastic properties for quasi-2D systems, and the influence of different terminating atoms on the phonon spectra of nanoplatelets.

[39] R. D'Souza and S. Mukherjee, *Phys. Rev. B* **95**, 085435 (2017).

[40] H. Fang and M. T. Dove, *Phys. Rev. B* **87**, 214109 (2013).

[41] H. Fang, M. T. Dove, L. H. N. Rimmer, and A. J. Misquitta, *Phys. Rev. B* **88**, 104306 (2013).

[42] A. Marini, P. García-González, and A. Rubio, *Phys. Rev. Lett.* **96**, 136404 (2006).

[43] A. I. Lebedev, *J. Appl. Phys.* **124**, 164302 (2018).