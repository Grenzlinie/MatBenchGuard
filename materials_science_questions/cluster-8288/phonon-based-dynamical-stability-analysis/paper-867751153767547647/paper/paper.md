# Large Contribution of Quasi-Acoustic Shear Phonon
## Modes to Thermal Conductivity in Novel Monolayer $\text{Ga}_2\text{O}_3$

Gang Liu$^{1\#*}$, Zhaofu Zhang$^{2\#}$, Hui Wang$^{1}$, Guo-Ling Li$^{3}$, Jian-Sheng Wang$^{4}$ and Zhibin Gao$^{5*}$

$^{1}$School of Physics and Engineering, Henan University of Science and Technology, Luoyang 471023, People's Republic of China

$^{2}$Department of Engineering, Cambridge University, Cambridge CB2 1PZ, United Kingdom

$^{3}$Chemistry and Chemical Engineering Guangdong Laboratory, Shantou 515063, People's Republic of China

$^{4}$Department of Physics, National University of Singapore, Singapore 117551, Republic of Singapore

$^{5}$State Key Laboratory for Mechanical Behavior of Materials, Xi'an Jiaotong University, Xi'an 710049, China.

## Abstract

Bulk gallium oxide ($\text{Ga}_2\text{O}_3$) has been widely used in lasers, dielectric coatings for solar cells, deep-ultraviolet transistor applications due to the large band gap over 4.5 eV. With the miniaturization of electronic devices, atomically thin $\text{Ga}_2\text{O}_3$ monolayer has been unveiled recently, which features an asymmetric configuration with a quintuple-layer atomic structure. The superior stability, the strain-tunable electronic properties, high carrier mobility and optical absorption indicate the promising applications in the electronic and photoelectronic devices. However, the strict investigation of lattice thermal conductivity ($\kappa_L$) of 2D $\text{Ga}_2\text{O}_3$ is still lacking, which has impeded the widespread use in practical applications. Here, we report the computational discovery of low $\kappa_L$ with a value of 10.28 W m$^{-1}$ K$^{-1}$ at 300 K in atomically thin $\text{Ga}_2\text{O}_3$. Unexpectedly, two quasi-acoustic shear phonon modes contribute as high as 27% to the

$\#$These authors contributed equally to this work.

*Corresponding author: Gang Liu, Email: liugang8105@gmail.com

*Corresponding author: Zhibin Gao, Email: zhibin.gao@xjtu.edu.cn

$\kappa_L$ at 300 K, leading to 37% contribution of optical phonon modes, much larger than many other 2D materials. We also find that the quasi-acoustic shear mode can emerge in the system without van der Waals interactions. This work provides new insight into the nature of thermal transport in non-van der Waals monolayer materials and predicts a new low $\kappa_L$ material of potential interest for thermal insulation in transistor applications.

# Introduction

Wide band gap semiconductor $\text{Ga}_2\text{O}_3$ has been attracting significant attention in recent years for the optoelectronic and power electronic applications $^1$. With an ultrawide band gap of about 4.8 eV $^2$, it has a high breakdown electric field of about 9 MV cm$^{-1}$, making it attractive for high voltage device applications $^{3,4}$. It also possesses unique ultraviolet (UV) transparency, implying potential application for novel UV optoelectronics $^{5,6}$. Besides the electrical and optical properties, anisotropic thermal conductivity properties of $\beta$-$\text{Ga}_2\text{O}_3$ are also investigated both experimentally and theoretically $^{7,8}$.

With the scaling-down of electronic devices, it is becoming necessary to study the low-dimensional phases of traditional bulk semiconductors. Since graphene was successfully synthesized in 2004 $^9$, two-dimensional (2D) materials have been the focus of scientific researches, such as transition metal dichalcogenides (TMDs), group-III, -V, and -VI monolayers $^{10-20}$. Compared with the bulk counterparts, 2D materials attract much research attention and exhibit interesting and outstanding properties such as strain-tunable band gap and high surface-area-to-volume ratio, benefiting to their wider application ranges $^{21,22}$. Though the physical and chemical properties of bulk $\text{Ga}_2\text{O}_3$ have been studied in-depth $^{1-8}$, the 2D $\text{Ga}_2\text{O}_3$ still needs to be explored further.

Very recently, the novel 2D $\text{Ga}_2\text{O}_3$ monolayer with 2D $\alpha$-$\text{In}_2\text{Se}_3$ geometry is

proposed and investigated by us using first-principles calculations $^{23}$. With an excellent dynamic and thermodynamic stability, the $\text{Ga}_2\text{O}_3$ monolayer is found to be a semiconductor with a wide indirect band gap of 3.16 eV. It has a high electron mobility of about $5000\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$, which can further increase to $7000\ \text{cm}^2\text{V}^{-1}\text{s}^{-1}$ by hybridization. The asymmetric configuration spontaneously introduces an intrinsic dipole within the quintuple-layer, boosting the separation of photon-excited carriers. Moreover, outstanding optical absorption ability is identified, which can be effectively tuned by strain engineering $^{23}$. These outstanding properties suggest the novel $\text{Ga}_2\text{O}_3$ monolayer has great application potentials for low-dimensional optoelectronic and power electronic device. Furthermore, the intrinsic built-in field feature contributes to further applications in energy conversion such as photocatalytic water splitting or gas sensors. However, the thermal transport properties of this novel $\text{Ga}_2\text{O}_3$ monolayer are not thoroughly understood yet.

In a practical electronic device, much power is dissipated in power switching operations, causing an increase of temperature by tens or even hundreds of degrees above the ambient environment $^{24}$. High temperatures are prone to the degradation of device performance, even destroy the device. Thus, the researches on thermal conductivity and thermal transport properties of materials are urgently required for practical applications. It should be noted that, materials with low thermal conductivity can be used as a heat insulator in practical applications, while the ones with high thermal conductivity can be used as heat dissipation materials. Thus, a thorough understanding of thermal transport properties for $\text{Ga}_2\text{O}_3$ monolayer is of technological importance.

In this work, the thermal conductivity $\kappa_L$ and thermal transport properties of $\text{Ga}_2\text{O}_3$ monolayer are systemically investigated by first-principles calculations based on the Boltzmann transport equation (BTE). It is found the monolayer has an in-plane isotropic $\kappa_L$ of $10.28\ \text{W m}^{-1}\text{K}^{-1}$ at room temperature, lower than the bulk $\beta\text{-Ga}_2\text{O}_3$ ($16\sim21\ \text{W m}^{-1}\text{K}^{-1}$) $^{7,8}$. The contributions of phonon branches to total $\kappa_L$ are investigated, showing a surprisingly large proportion of 38% for all-optical branches at 300 K, which

is a quite large proportion among 2D materials. Furthermore, we carefully examine the harmonic and anharmonic properties of $\text{Ga}_2\text{O}_3$ monolayer, to unveil the underlying physical mechanisms of the significant contribution of optical modes. The significant contribution of optical modes can be attributed to the quasi-acoustic branches with low frequency, which disperse similarly to acoustic ones. The emergence of these low-frequency quasi-acoustic shear modes results from the relatively weaker interactions within the quintuple atom layers. We investigate the effect of **quasi-acoustic shear mode** on thermal transport in materials **without** van der Waals interaction. Finally, the boundary and size effects are also studied.

# Computational and Theoretical Methods

The first-principles calculations are performed using the Vienna ab initio simulation package (VASP) $^{25,26}$, based on density functional theory (DFT). The exchange-correlation functional is chosen in the form of the Perdew-Burke-Ernzerhof (PBE) $^{27}$. A plane-wave basis set is employed with a kinetic energy cutoff of 600 eV, 50% higher than the maximum recommended cutoff for the pseudopotentials. The energy convergence value in structure optimization is selected as $10^{-8}$ eV and the maximum Hellmann-Feynman force is less than $10^{-4}$ eV $\text{\AA}^{-1}$, while the Monkhorst-Pack $^{28}$ k-mesh of $13 \times 13 \times 1$ is used to sample the Brillouin zone (BZ). The vacuum space of at least $20$ $\text{\AA}$ is kept along the z-direction, which is thick enough to avoid the interactions between periodical images.

Based on the Boltzmann transport equation (BTE), the in-plane $\kappa_L$ can be expressed by $^{29,30}$:

$$
\kappa_{\alpha \beta}=\frac{1}{V} \sum_{\lambda} C_{\lambda} v_{\lambda \alpha} v_{\lambda \beta} \tau_{\lambda}, \tag{1}
$$

where $V$ is the volume of the cell, $\lambda$ denotes a phonon mode with different wave vectors $\mathbf{q}$ and branch indexes $p$, $C_\lambda$ is the heat capacity, $v_{\lambda \alpha}$ is the group velocity along the $\alpha$

direction and $\tau_{\lambda}$ is the relaxation time, respectively. The group velocity is expressed as:

$$
v_{\lambda \alpha}=\frac{d \omega_{\lambda}}{d q_{\alpha}}. \tag{2}
$$

Eq. (1) implies the $\kappa_{L}$ is determined by the harmonic and anharmonic properties together. Based on Eq. (1), it can be found $C_{\lambda} v_{\lambda \alpha} v_{\lambda \beta} \tau_{\lambda}$ is the contribution to $\kappa_{L}$ of each phonon mode $\lambda$, while the total $\kappa_{L}$ is the sum. Coordinating with the frequency of each phonon mode, we can obtain the relation of the contribution to the phonon frequency. Similarly, with the contribution and the branch index of each phonon mode, we can obtain the relation of the contribution to each phonon branch.

To obtain the full solution to the BTE for phonon, an iteration approach is adopted widely with the following expression $^{31}$:

$$
\tau_{\lambda}=\tau_{\lambda}^{0}\left(1+\Delta_{\lambda}\right), \tag{3}
$$

where

$$
\begin{aligned}
\Delta_{\lambda} &=\frac{1}{N} \sum_{\lambda^{\prime} \lambda^{\prime \prime}}^{+} \Gamma_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{+}\left(\xi_{\lambda \lambda^{\prime \prime}} \tau_{\lambda^{\prime \prime}}-\xi_{\lambda \lambda^{\prime}} \tau_{\lambda^{\prime}}\right) \\
&+\frac{1}{N} \sum_{\lambda^{\prime} \lambda^{\prime \prime}}^{-} \frac{1}{2} \Gamma_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{-}\left(\xi_{\lambda \lambda^{\prime \prime}} \tau_{\lambda^{\prime \prime}}+\xi_{\lambda \lambda^{\prime}} \tau_{\lambda^{\prime}}\right)+\frac{1}{N} \sum_{\lambda^{\prime}} \Gamma_{\lambda \lambda^{\prime}} \xi_{\lambda \lambda^{\prime}} \tau_{\lambda^{\prime}},
\end{aligned} \tag{4}
$$

$$
\tau_{\lambda}^{0}=\frac{1}{N}\left(\sum_{\lambda^{\prime} \lambda^{\prime \prime}}^{+} \Gamma_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{+}+\sum_{\lambda^{\prime} \lambda^{\prime \prime}}^{-} \frac{1}{2} \Gamma_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{-}+\sum_{\lambda^{\prime}} \Gamma_{\lambda \lambda^{\prime}}\right). \tag{5}
$$

Here, $N$ is the number of $\mathbf{q}$ sampling in the Brillouin zone, $\xi_{\lambda \lambda^{\prime}}=\omega_{\lambda^{\prime}} v_{\lambda^{\prime}}^{z} / \omega_{\lambda} v_{\lambda}^{z}$. Note in the summation $\sum^{ \pm}$, $\lambda^{\prime \prime}=\left(p^{\prime \prime}, \mathbf{q} \pm \mathbf{q}^{\prime}+\mathbf{K}\right)$, while $\mathbf{K}$ is a reciprocal lattice vector. $\Gamma_{\lambda \lambda^{\prime}}$ is the isotopic impurity scattering probability $^{32,33}$. And the possible three-phonon transition probabilities $\Gamma_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{ \pm}$for mode $\lambda$ with modes $\lambda^{\prime}$ and $\lambda^{\prime \prime}$ can be expressed by:

$$
\Gamma_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{ \pm}=\frac{\hbar \pi}{4}\left\{\begin{array}{c}
f_{\lambda^{\prime}}-f_{\lambda^{\prime \prime}} \\
f_{\lambda^{\prime}}+f_{\lambda^{\prime \prime}}+1
\end{array}\right\} \frac{\delta\left(\omega_{\lambda}+\omega_{\lambda^{\prime}}-\omega_{\lambda^{\prime \prime}}\right)}{\omega_{\lambda} \omega_{\lambda^{\prime}} \omega_{\lambda^{\prime \prime}}}\left|V_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{ \pm}\right|^{2}, \tag{6}
$$

where $f_{\lambda}$ is the Bose-Einstein distribution function depending on the phonon angular frequency $\omega_{\lambda}$. Furthermore, $\omega_{\lambda}$, $\omega_{\lambda^{\prime}}$ and $\omega_{\lambda^{\prime \prime}}$ should satisfy the energy conservation, while $\boldsymbol{q}_{\lambda}$, $\boldsymbol{q}_{\lambda^{\prime}}$ and $\boldsymbol{q}_{\lambda^{\prime \prime}}$ satisfy the conservation of quasimomentum. The upper (lower) row in curly brackets goes with the + (-) sign for absorption (emission) processes, respectively. $V_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{ \pm}$is the scattering matrix element, depending

on the third-order (anharmonic) interatomic force constants (IFCs) $\Phi_{ijk}^{\alpha\beta\gamma}$, expressed as:

$$
V_{\lambda \lambda^{\prime} \lambda^{\prime \prime}}^{ \pm}=\sum_{i \in u . c .} \sum_{j, k} \sum_{\alpha \beta \gamma} \Phi_{i j k}^{\alpha \beta \gamma} \frac{e_{\lambda}^{\alpha}(i) e_{p^{\prime}, \pm q^{\prime}}^{\beta}(j) e_{p^{\prime \prime},-q^{\prime \prime}}^{\gamma}(k)}{\sqrt{M_{i} M_{j} M_{k}}}. \tag{7}
$$

Here, $M_i$ is the mass of atom $i$, and it runs over a unit cell only in the sum. However, $j$ and $k$ run over the whole system. $e_{\lambda}^{\alpha}(i)$ means the $\alpha$ component of the eigenvectors of phonon mode $\lambda$ for the $i$th atom.

Eq. (3) is solved numerically for $\tau_{\lambda}$ with an iterative approach. Neglecting $\Delta_{\lambda}$ in Eq. (3), we can obtain the zeroth-order solution $\tau_{\lambda}=\tau_{\lambda}^{0}$, which is equivalent to the relaxation time approximation (RTA) $^{31,34}$. Note RTA typically does not incorporate the distinction between momentum-conserving Normal processes and resistive Umklapp processes. Thus, Normal processes are also considered as resistive in RTA, always leading to lower values of $\kappa_{L}$. However, the full solution to the BTE can be performed within an iteration approach, leading to higher, more reasonable, and accurate results than RTA $^{30}$. Therefore, in this work, the discussions are always based on the results of the iteration approach, unless noted especially.

In the work, the harmonic IFCs are obtained by Phonopy $^{35}$, with a supercell of $5 \times 5 \times 1$. The meta-GGA functional SCAN is adopted for the harmonic IFCs $^{36,37}$. For anharmonic IFCs, the same size supercell is adopted while the interactions are taken into consideration up to the $8^{\text{th}}$ nearest neighbours. All DFT calculations for supercells are $\Gamma$-point only as there are 125 atoms in the supercell. Then the anharmonic IFCs are extracted by thirdorder.py script, and the thermal conductivity is calculated by ShengBTE $^{34}$. After the careful test, we chose a dense k-mesh grid of $151 \times 151 \times 1$, to ensure the convergence of thermal conductivity.

# Results and Discussions

![](./images/867751153767547647_1.jpg)

Fig. 1. Top view (a) and side view (b) of the optimized structure of the novel Ga₂O₃ monolayer. The primitive cell is marked by black solid lines in the top view. Note in (b) four types of Ga-O bonds are labeled as $d_1$, $d_2$, $d_3$, and $d_4$, respectively.

As shown in Fig. 1, the stable structure of the Ga₂O₃ monolayer belongs to $P3M1$ (156) symmetry group, also features an isotropic pattern in the 2D plane. The side view in Fig. 1(b) shows the stacked atomic layer in the sequence of O-Ga-O-Ga-O, forming the quintuple layer consisted of covalently bonded gallium and oxygen triangular lattices. The different Ga-O bond lengths are labeled as $d_1$, $d_2$, $d_3$, and $d_4$, which are 1.92, 2.21, 1.80, and 1.91 Å, respectively. The optimized lattice parameters are $a = b = 3.08$ Å, slightly larger than the previous work (3.04 Å) $^{23}$. This is owing to the cell is relaxed using PBE functional in this work, which gives a slightly larger lattice constant than hybrid functional $^{38}$.

![](./images/867751153767547647_2.jpg)

Fig. 2. Phonon dispersion (a) and PDOS (b) of Ga₂O₃ monolayer. In (a), the black, red, and green lines indicate ZA, TA, and LA modes, respectively. The quasi-acoustic optical branches are displayed by purple lines while other optical branches are represented by blue lines.

The phonon dispersions and phonon density of states (PDOS) are calculated and shown in Fig. 2(a) and (b). The stability of Ga₂O₃ monolayer is identified as there is no imaginary frequency. Since there are 5 atoms in the primitive cell, 15 phonon branches exist, including 3 acoustic and 12 optical branches. Note the out-of-plane acoustic (ZA, black curve) phonon mode is quadratic around the $\Gamma$ point, which is the feature of 2D materials owing to the membrane effect. And there are other two acoustic branches: transverse acoustic (TA, red curve) and longitudinal acoustic (LA, green curve) branches, which show linear relationships with $\boldsymbol{q}$ near the $\Gamma$ point $^{39}$. The unique frequency dependence of the three acoustic branches can be understood by the 2D continuum elasticity theory $^{40}$. Moreover, the two lowest optical branches around $\Gamma$ point (purple curves) are well separated from the other optic branches, named "quasi-acoustic" modes since they disperse very similarly to acoustic modes $^{41}$. In fact, the quasi-acoustic branches are very common in many bilayers and layered materials $^{41-44}$, due to the weak layer-layer interactions. In Fig. 2(b), it is found that the Ga atoms

dominate the low-frequency region because of their heavier mass, while the lighter O atoms contribute mainly in the high frequency. In the low-frequency range lower than 5 THz, there are three significant PDOS peaks round about 2.6, 4.4, and 4.9 THz. Note the quasi-acoustic modes are also within this frequency range and should contribute much to the PDOS. Larger PDOS indicates that more phonon modes can carry heat, hence more contribution to $\kappa_L$. And these low-frequency peaks are mainly related to heavier Ga atoms.

The Debye temperature $\theta_D$ is an important physical quantity related to the thermal properties. Usually, high $\theta_D$ means high thermal conductivity $^{45}$. However, it should be noted $\theta_D$ can not determine $\kappa_L$ separately. $\kappa_L$ is affected by several harmonic and anharmonic phonon properties, and $\theta_D$ mainly reflects the magnitude of phonon group velocity $v_g$, a harmonic property. It can be obtained by $\theta_D = h\omega_{max}/k_B$, where $\omega_{max}$ is the maximum of acoustic phonon frequency $^{46, 47}$. The calculated value is 241 K with this expression, higher than 2D SnSe (87 K), $\beta$-tellurene (106 K), stanene (198 K) and 2D SnS₂ (233 K), but lower than 2D MoS₂ (278 K) and graphene (2359 K)$^{48-51}$.

![](./images/867751153767547647_3.jpg)

Fig. 3. (a) Calculated $\kappa_L$ of Ga₂O₃ monolayer and (b) the frequency-resolved $\kappa_L$ at 300 K. The dashed line in (a) indicates the 1/T fitting of temperature-dependent $\kappa_L$.

The calculated $\kappa_L$ of iterative method is plotted in Fig. 3(a). Note the $\kappa_L$ of Ga₂O₃ monolayer is in-plane isotropic, resulting from its in-plane isotropy of structure. It should be noted that an effective thickness should be defined to calculate the $\kappa_L$ for 2D materials. The effective thickness is 7.57 Å, with the definition of the summation of the buckling height $h$ and twice of the van der Waals radii of the outermost O atoms $^{47, 48, 52}$. The $\kappa_L$ of Ga₂O₃ monolayer is 10.28 W m⁻¹ K⁻¹ at room temperature, lower than bulk β-Ga₂O₃ $^{7, 8}$. To compared $\kappa_L$ with other 2D materials, we also use the thermal sheet conductance ("2D thermal conductivity") with the unit W K⁻¹ as it is more meaningful and physical for 2D materials $^{52}$. Then we get the value of 7.77 nW K⁻¹ for Ga₂O₃ monolayer at 300 K. It is also a quite small value in 2D materials, smaller than SnS₂, MoS₂, MoSSe, and MoSe₂ monolayers $^{50, 53}$. Furthermore, we found that $\kappa_L$ of Ga₂O₃ monolayer matches well with $T^{-1}$ behavior, indicating the Umklapp process of phonon scattering dominates the thermal transport $^{54, 55}$. The RTA results are also shown in Fig. 3(a), which are lower than the results of the iterative method. For instance, the

$\kappa_L$ of RTA is 8.72 W m⁻¹ K⁻¹ at 300 K. The difference between two methods is small, in the agreement of the common criteria that Normal processes usually are relevant only for materials with high $\kappa_L$ $^{34, 56}$. It also implies the effect of Normal processes can be neglected in a rough approximation such as RTA.

To examine the contributions of phonons with different frequencies to the total $\kappa_L$, the frequency-resolved $\kappa_L$ of Ga₂O₃ monolayer at 300 K is calculated and shown in Fig. 3(b). There are two significant peaks in Fig. 3(b) locating around 0 and 3.3 THz, indicating nearby phonons contribute greatly to $\kappa_L$. It can be found most of the contributions come from phonons lower than 5 THz. As most quasi-acoustic phonons have a frequency lower than the value, it implies the optical modes should have a significant contribution to the total $\kappa_L$.

![](./images/867751153767547647_4.jpg)

Fig. 4. (a) Normalized $\kappa_L$ of phonon modes with increasing temperature. (b) shows vibrating patterns of the lowest quasi-acoustic mode near $\Gamma$ point along $\Gamma$-M direction, while the one of second-lowest quasi-acoustic mode is displayed in (c).

The normalized contribution of each phonon branch to the total $\kappa_L$ versus temperature is shown in Fig. 4(a). Note the normalizing factor is the total $\kappa_L$. The total

contribution of optical branches except for the two quasi-acoustic branches, rises with increasing temperature, while the ones of three acoustic modes decline. It results from the fact that only acoustic phonons with low frequency can be activated at low temperatures, while most optical phonons with high frequency can also be activated at high temperatures. However, the contribution of quasi-acoustic modes also declines at high temperatures, as they possess low frequency similar to acoustic modes. At 300 K, the normalized $\kappa_L$ is 0.18, 0.20, and 0.24 for ZA, TA, and LA modes, whereas the sum of the two quasi-acoustic modes is 0.27. The contribution from all the quasi-acoustic modes is quite large, resulting in a percentage up to 38% from the optical branches. The vibrating patterns of the two quasi-acoustic modes are exhibited in Fig. 4(b) and (c). It should be noted that the vibrations of the quasi-acoustic branches show remarkable layered motion. Specifically, the top three-atom layers of (001) surface vibrate together, while the bottom two-atom layers of $(00\overline{1})$ surface show the out-of-phase motion compared with the top three atom layers. The relative motions of the top O-Ga-O layer and the bottom Ga-O layer are parallel to the layer plane, similar to the shear modes in bilayer/bulk transition metal dichalcogenides, as well as other layered materials $^{43,44}$. It should be noted that quasi-acoustic modes also contribute to $\kappa_L$ significantly in bulk MoS$_2$ $^{42}$. Note there is no low-frequency quasi-acoustic mode that vibrates along the z-direction compared with bulk MoS$_2$. It is reported the quasi-acoustic mode along z-direction results from the symmetry of atomic layers along the same direction $^{43,44}$. Therefore, the atomic layers don't show symmetry along the z-direction in Ga$_2$O$_3$ monolayer, leading to the lacking of quasi-acoustic mode vibrating along this direction. Tough the acoustic modes contribute to the total $\kappa_L$ more than all the optical modes (62% compared with 38%), the proportion of contribution for optical modes is still much more than many 2D materials, such as graphene (1%) $^{29,51}$, $\alpha$-tellurene (10%) $^{57}$, MoS$_2$ monolayer (1.4%) $^{49}$, and stanene (2.1%) $^{58}$.

![](./images/867751153767547647_5.jpg)

Fig. 5. Frequency resolved heat capacity (a), phonon group velocity $v_g$ (b), and relaxation time $\tau$ (c) of $\text{Ga}_2\text{O}_3$ monolayer at 300 K.

To further reveal the underlying physics for the low $\kappa_L$ and abnormal high contribution of optical modes, the heat capacity $C_v$, phonon velocity $v_g$, and phonon relaxation time $\tau$ are investigated, as shown in Fig. 5. The frequency-resolved heat capacity at 300 K is displayed in Fig. 5(a). There are several peaks of the curves in the range of low and high frequencies, indicating phonons with low frequency and high frequency have a remarkable contribution to heat capacity at room temperature. The two peaks in the low-frequency range are near 2.5 and 4.5 THz, in reasonable agreement with the results in Fig. 2(b). In fact, at 300 K where it is higher than the Debye temperature (241 K), the heat capacity $C_v$ of each phonon branch approaches the classic value $k_B$, the Boltzmann's constant. Thus, large PDOS always indicates a significant

contribution to $C_{v}{}^{59}$. In Fig. 5(b), the dispersions of phonon group velocity $v_{g}$ are plotted. The group velocity is high in both low and high-frequency ranges. Especially, a great number of phonons with a frequency lower than 5 THz has a very high group velocity exceeding $6 \times 10^{3} \mathrm{~m} \mathrm{~s}^{-1}$. Among the three acoustic branches, LA phonons have the highest velocity, and the value of ZA phonons is the lowest in this frequency range. It is notable that the low optical phonons, i. e., the quasi-acoustic phonons, have almost the largest group velocity in the range. It is also in good agreement with Fig. 2, where the quasi-acoustic modes disperse similarly to acoustic modes, implicating the similar phonon group velocity, based on Eq. (2). Furthermore, the optical phonons in the range of about 7~10 THz and 16~19 THz also possess high group velocity. However, these high-frequency optical phonons have little contribution to the $\kappa_{L}$, as shown in Fig. 3(b).

At last, the calculated phonon relaxation time $\tau$ at 300 K is displayed in Fig. 5(c). It can be found that the acoustic phonons around $\Gamma$ point with very low frequency have relaxation time as long as $10^{3}$ ps. However, the phonon relaxation time decreases quickly with increased frequency, and it is in the order of 10 ps when the frequency is round 1 THz. Then the relaxation time declines slowly. It should be noted that most of the quasi-acoustic phonons are lower than 5 THz (Fig. 2), where the relaxation times are round the high value of 10 ps. Most phonons have a relaxation time shorter than 1 ps when the frequency is higher than 5 THz. On the whole, the relaxation time mainly determines the contributions of phonons belonging to various modes and frequency ranges to the total $\kappa_{L}$. Specifically, the phonons with a frequency lower than 5 THz

have relaxation time at least an order higher than the ones of other phonons, combining with high velocity and heat capacity, leading to the dominating contribution to $\kappa_{L}$, as shown in Fig. 3(b). Among these low-frequency phonons, a large number of quasi-acoustic phonons, which also possess high relaxation time, velocity, and remarkable heat capacity, should contribute remarkably to $\kappa_{L}$. However, there are no optical phonons with a very low frequency lower than 1 THz, where the relaxation time is higher than $10^{2}$ ps. As a result, the contribution of the optical modes is still less than acoustic modes, though their contribution is pretty significant, close to 40%. Compared with other 2D materials, the $\tau$ of Ga₂O₃ monolayer is quite low, which is the key point leading to the lower $\kappa_{L}$. For instance, though the $v_{g}$ are close to each other, the highest value of $\tau$ is on the order of $10^{3}$ and $10^{4}$ ps for Ga₂O₃ and MoS₂ monolayer respectively, leading to much lower $\kappa_{L}$ in Ga₂O₃ monolayer $^{49}$.

It can be argued reasonably that quasi-acoustic optical modes can enhance the proportion of contribution to $\kappa_{L}$ for optical branches greatly, since they possess harmonic and anharmonic properties similar to acoustic ones. Furthermore, some models such as the Slack model $^{45}$, which are extensively used to estimate $\kappa_{L}$ of materials fast and conveniently, assume that only the acoustic phonon modes participate in the heat conduction process. It should be cautious about using these models when the quasi-acoustic branches emerge, since the quasi-acoustic branches may contribute remarkably to $\kappa_{L}$.

The effect of quasi-acoustic modes on $\kappa_{L}$ is analyzed above. It is reported that

the quasi-acoustic modes usually emerge in layered materials, where the atomic layers interact through weak van der Waals interaction $^{41}$. Now we change the bond length of $d_1$, $d_2$, $d_3$, and $d_4$ separately by displacing the atoms, to examine the corresponding potential energy surfaces. First, we move atoms with a fixed step to stretch/compress the distance of bonds that we want to study, while other bonds remain unchanged. Then the total energies of these new structures are calculated, and the corresponding potential energy surfaces can be obtained. The results are plotted in Fig. 6. The potential energy surfaces of in-layer and inter-layer interactions in bulk $MoS_2$ are also calculated and displayed in Fig. 6 for comparison. We use the second-order derivatives of these curves to measure the bond strengths, which are 57, 27, 26, and $133\ \text{eV}/\mathring{\text{A}}^2$ for $d_1$, $d_2$, $d_3$, and $d_4$, respectively. Note the weakest $d_3$ bond is along the $z$-direction, while other stronger bonds are partly in-plane. Thus, the strong bonds connect the atoms in the top O-Ga-O layer of the (001) surface, forming a unit that moves together. And the same to the atoms in the bottom O-Ga layer of the $(00\overline{1})$ surface. The weakest $d_3$ bond connects the top O-Ga-O layer to the bottom O-Ga layer, resulting in the relative vibrations of the two parts (Fig. 4(b) and (c)), and the low-frequency quasi-acoustic modes emerge.

Moreover, in bulk $MoS_2$ the second-order derivative for the inter-layer van der Waals interaction is $11\ \text{eV}/\mathring{\text{A}}^2$, while the one for the in-layer bonds is $258\ \text{eV}/\mathring{\text{A}}^2$. It can be concluded quasi-acoustic modes also appear when the in-layer interactions are much stronger than the inter-layer ones, similar to $Ga_2O_3$ monolayer. Thus, we emphasize when there exists much weaker inter-layer interaction than the one of inter-layer, low-

frequency quasi-acoustic modes emerge, whereas the van der Waals interaction is not necessary for this.

![](./images/867751153767547647_6.jpg)

Fig. 6. Potential energy surfaces of $d_1$, $d_2$, $d_3$, and $d_4$ in 2D Ga₂O₃. The ones of in-layer and inter-layer interactions in bulk MoS₂ are also given for comparison. The inset shows the side view of Ga₂O₃ monolayer, where the atomic bonds $d_1$ to $d_4$ are also displayed.

In practical applications, $\kappa_L$ of materials may be significantly suppressed as all materials have finite sizes, where the additional boundary scattering can significantly affect $\kappa_L$, especially at the nanoscale. Usually, an empirical formula is used to describe the boundary scattering $\tau_{\lambda}^b$, which is expressed as: $\frac{1}{\tau_{\lambda}^b} = \frac{v_{\lambda}}{L}$, where $L$ means the size of a material $^{60}$. The normalized $\kappa_L$ as a function of sample size $L$ at room temperature is shown in Fig. 7(a). The normalized $\kappa_L$ of Ga₂O₃ monolayer declines following an exponential function of decreasing $L$ due to the stronger boundary

effect. In fact, the dependence of $L$ has been experimentally verified in suspended graphene $^{60,61}$. The normalized $\kappa_{L}$ of $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer is 0.50 at the size of 15 nm. When the $L$ is $10^{3} \mathrm{~nm}$, the normalized $\kappa_{L}$ is 0.95 , indicating the boundary effect is very weak and can be neglected. To estimate the size effect, we also evaluate the normalized cumulative $\kappa_{L}$ with respect to the phonon mean free paths (MFPs) for the monolayer, as exhibited in Fig. 7(b). The phonon MFPs contribute mainly to $\kappa_{L}$ in the range of 1 to about 200 nm. In order to obtain the characteristic length, we introduce a single parametric function $^{34}$:

$$
\kappa_{L}\left(l \leq l_{\max }\right)=\frac{\kappa_{\max }}{1+l_{0} / l_{\max }}, \tag{8}
$$

where $l_{\max }$ and $\kappa_{\max }$ are the maximum MFP and ultimately cumulative lattice thermal conductivity. Only a parameter $l_{0}$ needs to be determined in the expression, which is regarded as the representative MFP. It is found $l_{0}$ is 15 nm for $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer, corresponding to the positions of $50 \%$ of the total $\kappa_{L}$. It can be expected that the $\kappa_{L}$ will significantly decrease when the size is on the order of 10 nm. The size effect discussion provides useful reference and guidance for thermal management design in micro-/nano-electronic devices based on this novel $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer.

![](./images/867751153767547647_7.jpg)

Fig. 7. Normalized $\kappa_{L}$ as a function of sample size $L$ (a) and the MFPs dependent normalized cumulative $\kappa_{L}$ at 300 K (b). In (b) the dashed red line represents the curve of the fitting, while the vertical dashed line indicates the position of $l_{0}$ for the $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer.

## Conclusion

In summary, the lattice thermal conductivity $\kappa_{L}$ of novel $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer is investigated based on first-principles calculations. Compared to its bulk counterpart (16 $\sim 21 \mathrm{~W} \mathrm{~m}^{-1} \mathrm{~K}^{-1}$), the $\kappa_{L}$ for $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer is only $10.28 \mathrm{~W} \mathrm{~m}^{-1} \mathrm{~K}^{-1}$ at room temperature, which is a quite low $\kappa_{L}$ among various 2D materials. Though the acoustic branches dominate the thermal transport in the monolayer, optical modes contribute significantly to the total $\kappa_{L}$, close to $40 \%$ at $300 \mathrm{~K}$. The harmonic and anharmonic phonon properties determine the $\kappa_{L}$ of $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer together. It is found the relaxation time plays a vital role in the thermal transport of $\mathrm{Ga}_{2} \mathrm{O}_{3}$ monolayer. The low-

frequency quasi-acoustic phonons possess significant PDOS and heat capacity, as well as high relaxation times and phonon velocity, resulting in a considerable contribution to total $\kappa_L$. It is argued that quasi-acoustic optical modes can greatly enhance the proportion of contribution to $\kappa_L$ for optical branches. The results provide important information for the systematic understanding of the thermal transport properties of the novel Ga₂O₃ monolayer, as well as its future design in micro-/nano-devices for practical applications.

## Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Nos. 11974100, 1210040387). We acknowledge the strong support by HPC Platform, Xi'an Jiaotong University.

## References

1.  J. Y. Tsao, S. Chowdhury, M. A. Hollis, D. Jena, N. M. Johnson, K. A. Jones, R. J. Kaplar, S. Rajan, C. G. Van de Walle, E. Bellotti, C. L. Chua, R. Collazo, M. E. Coltrin, J. A. Cooper, K. R. Evans, S. Graham, T. A. Grotjohn, E. R. Heller, M. Higashiwaki, M. S. Islam, P. W. Juodawlkis, M. A. Khan, A. D. Koehler, J. H. Leach, U. K. Mishra, R. J. Nemanich, R. C. N. Pilawa-Podgurski, J. B. Shealy, Z. Sitar, M. J. Tadjer, A. F. Witulski, M. Wraback and J. A. Simmons, Advanced Electronic Materials 4 (1), 1600501 (2018).
2.  K. Sasaki, M. Higashiwaki, A. Kuramata, T. Masui and S. Yamakoshi, J. Cryst. Growth 378, 591-595 (2013).
3.  S. J. Pearton, J. Yang, P. H. Cary, F. Ren, J. Kim, M. J. Tadjer and M. A. Mastro, Applied Physics Reviews 5 (1), 011301 (2018).
4.  M. Higashiwaki and G. H. Jessen, Applied Physics Letters 112 (6), 060401 (2018).

20

5. N. Ueda, H. Hosono, R. Waseda and H. Kawazoe, Applied Physics Letters **71** (7), 933-935 (1997).

6. M. Orita, H. Ohta, M. Hirano and H. Hosono, Applied Physics Letters **77** (25), 4166-4168 (2000).

7. Z. Guo, A. Verma, X. Wu, F. Sun, A. Hickman, T. Masui, A. Kuramata, M. Higashiwaki, D. Jena and T. Luo, Applied Physics Letters **106** (11), 111909 (2015).

8. M. D. Santia, N. Tandon and J. D. Albrecht, Applied Physics Letters **107** (4), 041907 (2015).

9. K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva and A. A. Firsov, Science **306** (5696), 666-669 (2004).

10. C. Ataca, H. Şahin and S. Ciraci, The Journal of Physical Chemistry C **116** (16), 8983-8999 (2012).

11. J. N. Coleman, M. Lotya, A. O'Neill, S. D. Bergin, P. J. King, U. Khan, K. Young, A. Gaucher, S. De, R. J. Smith, I. V. Shvets, S. K. Arora, G. Stanton, H.-Y. Kim, K. Lee, G. T. Kim, G. S. Duesberg, T. Hallam, J. J. Boland, J. J. Wang, J. F. Donegan, J. C. Grunlan, G. Moriarty, A. Shmeliov, R. J. Nicholls, J. M. Perkins, E. M. Grieveson, K. Theuwissen, D. W. McComb, P. D. Nellist and V. Nicolosi, Science **331** (6017), 568 (2011).

12. A. J. Mannix, X.-F. Zhou, B. Kiraly, J. D. Wood, D. Alducin, B. D. Myers, X. Liu, B. L. Fisher, U. Santiago, J. R. Guest, M. J. Yacaman, A. Ponce, A. R. Oganov, M. C. Hersam and N. P. Guisinger, Science **350** (6267), 1513-1516 (2015).

13. L. Li, Y. Yu, G. J. Ye, Q. Ge, X. Ou, H. Wu, D. Feng, X. H. Chen and Y. Zhang, Nature Nanotechnology **9** (5), 372-377 (2014).

14. H. Liu, A. T. Neal, Z. Zhu, Z. Luo, X. Xu, D. Tománek and P. D. Ye, ACS Nano **8** (4), 4033-4041 (2014).

15. Z. Zhu and D. Tománek, Phys. Rev. Lett. **112** (17), 176802 (2014).

16. J. Ji, X. Song, J. Liu, Z. Yan, C. Huo, S. Zhang, M. Su, L. Liao, W. Wang, Z. Ni, Y. Hao and H. Zeng, Nature Communications **7** (1), 13352 (2016).

17. Z. Zhu, X. Cai, S. Yi, J. Chen, Y. Dai, C. Niu, Z. Guo, M. Xie, F. Liu, J. H. Cho, Y. Jia and Z. Zhang, Phyical Review Letters **119** (10), 106101 (2017).

18. J. Chen, Y. Dai, Y. Ma, X. Dai, W. Ho and M. Xie, Nanoscale **9** (41), 15945-15948 (2017).

19. G. Liu, Z. Gao and J. Ren, Physical Review B **99** (19), 195436 (2019).

20. Y. Yin, C. Shao, C. Zhang, Z. Zhang, X. Zhang, J. Robertson and Y. Guo, ACS Applied Materials & Interfaces **12** (19), 22378-22386 (2020).

21. P. Kang, M. C. Wang, P. M. Knapp and S. Nam, Advanced Materials **28** (23), 4639-4645 (2016).

22. J. A. Rogers, T. Someya and Y. Huang, Science **327** (5973), 1603-1607 (2010).

23. Y. Liao, Z. Zhang, Z. Gao, Q. Qian and M. Hua, ACS Applied Materials & Interfaces **12** (27), 30659-30669 (2020).

24. S. Pearton, F. Ren, M. Tadjer and J. Kim, Journal of Applied Physics **124** (22), 220901 (2018).

25. G. Kresse and J. Furthmüller, Physical Review B **54** (16), 11169-11186 (1996).

26. G. Kresse and D. Joubert, Physical Review B **59** (3), 1758-1775 (1999).

27. J. P. Perdew, K. Burke and M. Ernzerhof, Phys. Rev. Lett. **77** (18), 3865-3868 (1996).

28. H. J. Monkhorst and J. D. Pack, Physical Review B **13** (12), 5188-5192 (1976).

29. L. Lindsay, W. Li, J. Carrete, N. Mingo, D. A. Broido and T. L. Reinecke, Physical Review B **89** (15), 155426 (2014).

30. L. Lindsay, D. A. Broido and T. L. Reinecke, Physical Review B **87** (16), 165201 (2013).

31. W. Li, L. Lindsay, D. A. Broido, D. A. Stewart and N. Mingo, Physical Review B **86** (17), 174307 (2012).

32. S.-i. Tamura, Physical Review B **27** (2), 858-866 (1983).

33. A. Kundu, N. Mingo, D. A. Broido and D. A. Stewart, Physical Review B **84** (12), 125426 (2011).

34. W. Li, J. Carrete, N. A. Katcho and N. Mingo, Computer Physics Communications **185** (6), 1747-1758 (2014).

35. A. Togo, F. Oba and I. Tanaka, Physical Review B **78** (13), 134106 (2008).

36. J. Sun, A. Ruzsinszky and J. P. Perdew, Phys Rev Lett **115** (3), 036402 (2015).

37. J. Sun, R. C. Remsing, Y. Zhang, Z. Sun, A. Ruzsinszky, H. Peng, Z. Yang, A. Paul, U. Waghmare, X. Wu, M. L. Klein and J. P. Perdew, Nat Chem **8** (9), 831-836 (2016).

38. J. Heyd, J. E. Peralta, G. E. Scuseria and R. L. Martin, The Journal of Chemical Physics **123** (17), 174101 (2005).

39. J. Carrete, W. Li, L. Lindsay, D. A. Broido, L. J. Gallego and N. Mingo, Materials Research Letters **4** (4), 204-211 (2016).

40. D. Liu, A. G. Every and D. Tománek, Physical Review B **94** (16), 165432 (2016).

41. J. L. Verble and T. J. Wieting, Phys. Rev. Lett. **25** (6), 362-365 (1970).

42. A. N. Gandi and U. Schwingenschlögl, EPL (Europhysics Letters) **113** (3), 36002 (2016).

43. X. Zhang, X. F. Qiao, W. Shi, J. B. Wu, D. S. Jiang and P. H. Tan, Chemical Society Reviews **44** (9), 2757-2785 (2015).

44. P. H. Tan, W. P. Han, W. J. Zhao, Z. H. Wu, K. Chang, H. Wang, Y. F. Wang, N. Bonini, N. Marzari, N. Pugno, G. Savini, A. Lombardo and A. C. Ferrari, Nat Mater **11** (4), 294-300 (2012).

45. G. A. Slack, Journal of Physics and Chemistry of Solids **34** (2), 321-335 (1973).

46. L.-D. Zhao, S.-H. Lo, Y. Zhang, H. Sun, G. Tan, C. Uher, C. Wolverton, V. P. Dravid and M. G. Kanatzidis, Nature **508** (7496), 373-377 (2014).

47. G. Liu, Z. Gao, G.-L. Li and H. Wang, Journal of Applied Physics **127** (6), 065103 (2020).

48. Z. Gao, F. Tao and J. Ren, Nanoscale **10** (27), 12997-13003 (2018).

49. B. Peng, H. Zhang, H. Shao, Y. Xu, X. Zhang and H. Zhu, Annalen der Physik **528** (6), 504-511 (2016).

50. G. Liu, H. Wang, Z. Gao and G. L. Li, Physical Chemistry Chemical Physics **22**

(29), 16796-16803 (2020).

51. B. Peng, H. Zhang, H. Shao, Y. Xu, G. Ni, R. Zhang and H. Zhu, Physical Review B **94** (24), 245420 (2016).

52. X. Wu, V. Varshney, J. Lee, Y. Pang, A. K. Roy and T. Luo, Chem. Phys. Lett. **669**, 233-237 (2017).

53. S. D. Guo, Physical Chemistry Chemical Physics **20** (10), 7236-7242 (2018).

54. J. Ma, Y. Chen, Z. Han and W. Li, 2D Materials **3** (4), 045010 (2016).

55. L. Lindsay, D. A. Broido and T. L. Reinecke, Phys. Rev. Lett. **109** (9), 095901 (2012).

56. A. Ward, D. A. Broido, D. A. Stewart and G. Deinzer, Physical Review B **80** (12), 125203 (2009).

57. Z. Gao, G. Liu and J. Ren, ACS Applied Materials & Interfaces **10** (47), 40702-40709 (2018).

58. B. Peng, H. Zhang, H. Shao, Y. Xu, X. Zhang and H. Zhu, Scientific Reports **6** (1), 20225 (2016).

59. W. Li and N. Mingo, Physical Review B **89** (18), 184304 (2014).

60. D. L. Nika, E. P. Pokatilov, A. S. Askerov and A. A. Balandin, Physical Review B **79** (15), 155413 (2009).

61. A. A. Balandin, S. Ghosh, W. Bao, I. Calizo, D. Teweldebrhan, F. Miao and C. N. Lau, Nano Letters **8** (3), 902-907 (2008).