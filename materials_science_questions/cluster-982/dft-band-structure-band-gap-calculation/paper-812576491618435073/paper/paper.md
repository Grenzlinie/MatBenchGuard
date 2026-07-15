# Unfolding optical transition weights of impurity materials for first-principles LCAO electronic structure calculations

Yung-Ting Lee $^{\odot,1,2,*}$ Chi-Cheng Lee $^{\odot,1,3}$ Masahiro Fukuda, $^{1}$ and Taisuke Ozaki $^{1}$

$^{1}$ Institute for Solid State Physics, The University of Tokyo, 5-1-5 Kashiwanoha, Kashiwa, Chiba 277-8581, Japan
$^{2}$ Institute of Atomic and Molecular Sciences, Academia Sinica, No. 1, Roosevelt Rd., Sec. 4, Taipei 10617, Taiwan
$^{3}$ Department of Physics, Tamkang University, No. 151, Yingzhuan Rd., Tamsui Dist., New Taipei City 251301, Taiwan

![](./images/812576491618435073_1.jpg)
(Received 30 June 2020; revised 9 August 2020; accepted 13 August 2020; published 28 August 2020)

A method to analyze optical transitions is developed by combining the Kubo-Greenwood formula with the unfolding method to construct an unfolded electronic band structure with optical transition weights, which allows us to investigate how optical transitions are perturbed by imperfections such as impurity, vacancy, and structural distortions. Based on the Kubo-Greenwood formula, we first calculate frequency-dependent optical conductivity based on the first-principles electronic structure calculations using the linear combinations of atomic orbitals. Benefiting from the atomic orbital basis sets, the frequency-dependent optical conductivity can be traced back to their individual components before summations over all of $k$ points and bands. As a result, optical transition weights of the material can be put on the unfolded electronic band structure to show contributions at different $k$ points and bands. This method is especially useful to study the effects of broken symmetry in the optical transitions due to presence of impurities in the materials. As a demonstration, decomposed optical transition weights of a monolayer Si-doped graphene are shown in the electronic band structure.

DOI: 10.1103/PhysRevB.102.075143

## I. INTRODUCTION

The optical properties contain fundamental features of materials, including optical conductivity, dielectric function, refractive index, reflectivity, and transmission that can be measured by experiments [1–9], and have been widely studied for a variety of compounds, such as solids [10–13], nanoparticles [14,15], 2D materials [16–20], superconductors [21–24], and biological tissues [25]. The optical conductivity and dielectric function of materials are two important measurable quantities for understanding natural phenomena, such as current density caused by an alternating electric field, optical transitions, and energy dissipation [26–30]. To adjust light absorption capability of materials or to shift absorption energy range for designing new optical devices, fabricating different composites of materials by dopants or substitutions are possible and promising for practical applications [31–35]. Therefore, deeper understanding of the transitions described by the optical conductivity and dielectric function in impurity materials is obviously an important issue.

To analyze spectra of optical conductivity and dielectric function in a material, an electronic band structure is a useful analysis tool to examine whether transitions between occupied and unoccupied states occur [27]. Since the unfolding method has been developed, an unfolded electronic band structure of impurity materials calculated by a supercell can be constructed to ease the comparison with experimental results observed by angle-resolved photoemission spectroscopy [36–38]. However, the conventional presentation of optical conductivity of impurity materials still cannot show the direct correspondence with their band structure, although optical conductivity based on the Kubo-Greenwood formula [39,40] has been widely calculated by density functional theory (DFT) packages [41–46]. Recently, Bianco *et al.* bridged the relation between the unfolding method and the Berry curvature with Wannier functions to investigate the Berry-phase anomalous Hall conductivity of the Fe-Co alloys [47]. In order to build a connection between optical transitions and the electronic band structure, we propose to present optical conductivity with the unfolding method [37] to put optical transition weights of a material on the unfolded electronic band structure, which is called unfolding optical transition method in the following discussions.

The enhancement of optical conductivity of silicon doped graphene (SiG) with the tunable band gap in the visible region has been proposed to improve efficiency of photovoltaic cells [48,49]. In the experiments, subsequently, the graphene at a silicon-doping level of 2.7%–4.5% with opening a small band gap and without affecting the carrier concentration has been fabricated to enhance the performance of SiG/GaAs heterostructure solar cells in comparison with graphene/GaAs [50]. We apply the unfolding optical transition method to analyze contributions of optical transitions of SiGs in the unfolded electronic band structure for unveiling the silicon-doping effect in graphene.

This paper is organized as follows. In Sec. II the Kubo-Greenwood formula, partial optical transitions in an electronic band structure, and unfolding optical transition are shown. In Sec. III an example of a monolayer Si-doped graphene is given for showing changes of unfolded partial optical conductivity between Si-doped graphenes. Finally, this research work is concluded in Sec. IV.

*ytl821@gate.sinica.edu.tw*

## II. COMPUTATIONAL METHOD

In this section, based on the Kubo-Greenwood formula, we will discuss the formulation of (1) optical conductivity and momentum matrix element (MME), (2) partial optical conductivity, (3) unfolded partial optical conductivity, and (4) separation of unfolded partial optical conductivity. The computational order for the optical conductivity calculation is also discussed for the implementation with localized basis sets in Sec. II A.

### A. Optical conductivity

Based on the Kubo-Greenwood formula [39,40], the frequency-dependent optical conductivity tensor $\sigma_{\alpha\beta}(\omega)$ is calculated by

$$
\begin{aligned}
& \sigma_{\alpha \beta}(\omega) \\
& \quad=\frac{-i}{N_{k} \Omega} \sum_{K J J^{\prime}} \frac{f_{K J}-f_{K J^{\prime}}}{\epsilon_{K J}-\epsilon_{K J^{\prime}}} \frac{\left\langle K J\left|\hat{P}_{\alpha}\right| K J^{\prime}\right\rangle\left\langle K J^{\prime}\left|\hat{P}_{\beta}\right| K J\right\rangle}{\epsilon_{K J}-\epsilon_{K J^{\prime}}+\omega+i \eta}, \quad(1)
\end{aligned}
$$

where $\hat{P}_{\alpha}$ is the momentum operator along $\alpha$ direction in the atomic unit, $J$ and $J^{\prime}$ are indices of states, $f_{K J}$ is the Fermi-Dirac distribution at a $k$-point $K$ and a state $J$, $|K J\rangle$ is a Kohn-Sham eigenstate, $\epsilon$ is an eigenvalue, $\eta$ is $0^{+}$, $N_{k}$ is the total number of $k$ points, and $\Omega$ is the volume of the unit cell. When the intraband transition or the degenerate state $(\epsilon_{K J}=\epsilon_{K J^{\prime}})$ occurs, $(f_{K J}-f_{K J^{\prime}})/(\epsilon_{K J}-\epsilon_{K J^{\prime}})$ is treated as the first derivative of the occupation number with respect to the energy [37,41,42]. The MME can be evaluated by

$$
\begin{aligned}
& \left\langle K J\left|\hat{P}_{\alpha}\right| K J^{\prime}\right\rangle \\
& \quad=-i \sum_{a} \sum_{m n} C_{m}^{K J *} C_{n}^{K J^{\prime}} e^{-i \boldsymbol{K} \cdot\left(\boldsymbol{R}_{a}-\boldsymbol{R}_{0}\right)}\left\langle\phi_{m}\left(\boldsymbol{r}-\boldsymbol{R}_{a}\right)\left|\nabla_{\alpha}\right| \phi_{n}(\boldsymbol{r})\right\rangle, \\
& \quad(2)
\end{aligned}
$$

where $\alpha$ is along $x$, $y$, or $z$ direction, $R$ is a lattice vector, $a$ is an index of cells, $m$ and $n$ are atomic orbitals' indices, and $C$ is LCAO coefficient.

Here we estimate the computational order for the calculation of optical conductivity by Eq. (1). The orders of operations for calculating the MME with localized basis sets and with plane wave basis sets are $O(N)$ and $O(N^{2})$, respectively, with the number of basis functions $N$ [51-53]. After the calculation of the first MME in Eq. (1), the second MME can be obtained at the same time by the relation: $\langle K J'|\hat{P}| K J\rangle=\langle K J|\hat{P}| K J'\rangle^{*}$. Thus, the order of operations in these two MMEs with localized basis sets is $O(N)$. Furthermore, because $k$ points and two states are summation indices in Eq. (1), the orders of operations for all of $K$, $J$, and $J'$ correspond to $O(N_{k})$, $O(N)$, and $O(N)$, respectively. The total computational complexity in the frequency-dependent optical conductivity with localized basis sets is $O(N_{k}N^{3})$ in comparison with plane wave basis sets $O(N_{k}N^{4})$. Therefore, the computational effort can be reduced by utilizing localized basis sets, which is more suitable for a large-scale system.

### B. Partial optical conductivity

Since frequency-dependent optical conductivity $\sigma_{\alpha\beta}(\omega)$ is the summation over all of the $k$ points, occupied states, and unoccupied states, Eq. (1) can be rewritten as

$$
\sigma_{\alpha \beta}(\omega)=\frac{1}{N_{k}} \sum_{K J} \sigma_{\alpha \beta}(K, J, \omega),\qquad(3)
$$

where the partial optical conductivity $\sigma_{\alpha\beta}(K,J,\omega)$ is given by

$$
\begin{aligned}
& \sigma_{\alpha \beta}(K, J, \omega) \\
& \quad \equiv \frac{-i}{\Omega} \sum_{J^{\prime}} \frac{f_{K J}-f_{K J^{\prime}}}{\epsilon_{K J}-\epsilon_{K J^{\prime}}} \frac{\left\langle K J\left|\hat{P}_{\alpha}\right| K J^{\prime}\right\rangle\left\langle K J^{\prime}\left|\hat{P}_{\beta}\right| K J\right\rangle}{\epsilon_{K J}-\epsilon_{K J^{\prime}}+\omega+i \eta}. \quad(4)
\end{aligned}
$$

In Eq. (4), $\omega$ is a resonance energy to excite electrons from a state $J$ to another state $J'$. The partial optical conductivity of a material along $k$ paths in the first Brillouin zone can be calculated and put on its electronic band structure in a fat band representation we will show later on.

### C. Unfolded partial optical conductivity

To analyze how the optical conductivity $\sigma_{\alpha\beta}(\omega)$ is changed by perturbations such as impurities and structural disorders, we now combine the partial optical conductivity introduced by Eq. (4) with the unfolding method [37]. The partial optical conductivity $\sigma_{\alpha\beta}(K,J,\omega)$ of an impurity material in a supercell can be rewritten as

$$
\sigma_{\alpha \beta}(K, J, \omega)=\frac{-i}{\Omega} A_{K J, K J}^{\alpha \beta}(\omega),\qquad(5)
$$

with the spectral function tensor for the supercell defined by

$$
\begin{aligned}
& A_{K J, K J}^{\alpha \beta}(\omega) \\
& \quad \equiv\langle K J| \sum_{J^{\prime}} \frac{f_{K J}-f_{K J^{\prime}}}{\epsilon_{K J}-\epsilon_{K J^{\prime}}} \frac{\hat{P}_{\alpha}\left|K J^{\prime}\right\rangle\left\langle K J^{\prime}\right| \hat{P}_{\beta}}{\epsilon_{K J}-\epsilon_{K J^{\prime}}+\omega+i \eta}|K J\rangle. \quad(6)
\end{aligned}
$$

On the other hand, the partial optical conductivity $\sigma_{\alpha\beta}(k,j,\omega)$ of a perfect crystal as a reference system has the same expression as

$$
\begin{aligned}
\sigma_{\alpha \beta}(k, j, \omega) & =\frac{-i}{\Omega_{\mathrm{rc}}}\langle k j| \sum_{j^{\prime}} \frac{f_{k j}-f_{k j^{\prime}}}{\epsilon_{k j}-\epsilon_{k j^{\prime}}} \frac{\hat{P}_{\alpha}\left|k j^{\prime}\right\rangle\left\langle k j^{\prime}\right| \hat{P}_{\beta}}{\epsilon_{k j}-\epsilon_{k j^{\prime}}+\omega+i \eta}|k j\rangle \\
& =\frac{-i}{\Omega_{\mathrm{rc}}} A_{k j, k j}^{\alpha \beta}(\omega),
\end{aligned}
$$

where $\Omega_{\mathrm{rc}}$ is the volume of the reference cell, $|k j\rangle$ is a Kohn-Sham eigenstate at a $k$ point and a state $j$ in the reference cell, and $A_{k j,k j}^{\alpha\beta}(\omega)$ is the spectral function tensor in the reference cell. The uppercase letters in Eq. (4) and the lowercase letters in Eq. (7) stand for indices in the supercell and in the reference cell, respectively.

In order to relate partial optical conductivities between the supercell and the reference cell, the unfolding method [37] provides a refined approach to unfold the band structure of a supercell to the Brillouin zone of a reference cell via a spectral function. The spectral function tensor $A^{\alpha\beta}(\omega)$ is given by

$$
A^{\alpha \beta}(\omega)=\sum_{k j} A_{k j, k j}^{\alpha \beta}(\omega)=\sum_{k j}\left\langle k j\left|\hat{A}^{\alpha \beta}(\omega)\right| k j\right\rangle. \quad(8)
$$

By inserting closure relations $\sum_{kmn}|km\rangle S_{mn}^{-1}(k)\langle kn|=\hat{I}$ into $\langle kj|\hat{A}^{\alpha\beta}(\omega)|kj\rangle$, Eq. (8) is rewritten as
$$
\begin{aligned}
\sum_{kj} & \langle kj|\hat{A}^{\alpha\beta}(\omega)|kj\rangle \\
& =\sum_{kj}\sum_{mn}\sum_{n'm'}\langle kj|km\rangle S_{mn}^{-1}(k)\langle kn|\hat{A}^{\alpha\beta}(\omega)|kn'\rangle \\
& \quad\times S_{n'm'}^{-1}(k)\langle km'|kj\rangle \\
& =\sum_{k}\sum_{mn}\sum_{n'm'}S_{mn}^{-1}(k)\langle kn|\hat{A}^{\alpha\beta}(\omega)|kn'\rangle S_{n'm'}^{-1}(k)\langle km'|km\rangle,
\end{aligned}
\tag{9}
$$
with the definition
$$
|kn\rangle=\frac{1}{\sqrt{L}}\sum_{\mathbf{R}}e^{i\mathbf{k}\cdot\mathbf{R}}|Rn\rangle,\tag{10}
$$
where $m$ and $n$ are indices of atomic basis functions in the reference cell, $|Rn\rangle$ is an atomic basis function in the reference cell, $L$ is the number of unit cells in the Born–von Kármán boundary condition, and the closure relation $\sum_{kj}|kj\rangle\langle kj|=\hat{I}$ is required for deriving the last equation.
Due to $\sum_{m'}S_{n'm'}^{-1}(k)\langle km'|km\rangle=\delta_{n'm}(k)$, Eq. (9) becomes
$$
\sum_{kj}\langle kj|\hat{A}^{\alpha\beta}(\omega)|kj\rangle=\sum_{kmn}S_{mn}^{-1}(k)\langle kn|\hat{A}^{\alpha\beta}(\omega)|km\rangle.\quad(11)
$$

After inserting two closure relations $\sum_{KJ}|KJ\rangle\langle KJ|=\hat{I}$ in two adjacent positions of $\hat{A}^{\alpha\beta}(\omega)$ on the right-hand side of Eq. (11), we have
$$
\begin{aligned}
\sum_{kj} & \langle kj|\hat{A}^{\alpha\beta}(\omega)|kj\rangle \\
& =\sum_{kmn}\sum_{KJ}S_{mn}^{-1}(k)\langle kn|KJ\rangle\langle KJ|\hat{A}^{\alpha\beta}(\omega)|KJ\rangle\langle KJ|km\rangle \\
& =\sum_{kmn}\sum_{KJ}S_{mn}^{-1}(k)\langle kn|KJ\rangle A_{KJ,KJ}^{\alpha\beta}(\omega)\langle KJ|km\rangle,\quad(12)
\end{aligned}
$$
where
$$
\langle kn|KJ\rangle=\sum_{N}C_{N}^{KJ}\sum_{\mathbf{rR}}\frac{e^{-i\mathbf{k}\cdot\mathbf{r}}}{\sqrt{l}}\langle rn|RN\rangle\frac{e^{i\mathbf{K}\cdot\mathbf{R}}}{\sqrt{L}}\tag{13}
$$
and
$$
\langle KJ|km\rangle=\sum_{M}C_{M}^{KJ*}\sum_{\mathbf{r}'\mathbf{R}'}\frac{e^{-i\mathbf{K}\cdot\mathbf{R}'}}{\sqrt{L}}\langle R'M|r'm\rangle\frac{e^{i\mathbf{k}\cdot\mathbf{r}'}}{\sqrt{l}}.\tag{14}
$$

For simplicity, the summations in Eq. (12) over $k$, $j$, and $J$ are dropped. Thus, the spectral function tensor $A_{kj,kj}^{\alpha\beta}(\omega)$ in Eq. (8) is given by
$$
A_{kj,kj}^{\alpha\beta}(\omega)=\frac{L}{l}\sum_{KG}\delta_{k-G,K}W_{KJ}^{k}A_{KJ,KJ}^{\alpha\beta}(\omega),\tag{15}
$$
with the unfolded spectral weight
$$
W_{KJ}^{k}=\sum_{MNr}e^{i\mathbf{k}\cdot(\mathbf{r}-\mathbf{r}'(M))}C_{N}^{KJ}C_{M}^{KJ*}S_{0N,rm(M)},\tag{16}
$$
where $L$ is the number of unit cells in a supercell, $l$ is the number of unit cells in a reference cell, and $\mathbf{r}'(M)$ and $m(M)$ refer to lattice vectors and an orbital index in the representation of the reference cell, respectively. The eigenstate $j$ in the reference cell corresponds to the unfolded eigenstate $J$ in the supercell due to $\sum_{KG}\delta_{k-G,K}$. According to Eqs. (15) and (16), the weight of the spectral function tensor $A_{KJ,KJ}^{\alpha\beta}(\omega)$ is determined by the phase factor $e^{i\mathbf{k}\cdot(\mathbf{r}-\mathbf{r}'(M))}$, LCAO coefficients, and overlap matrix elements in the unfolded spectral weight $W_{KJ}^{k}$. The phase factor governs the spectral weight of unfolding electronic band structure of a material built with a supercell. In addition, the overlap matrix elements and LCAO coefficients in a doped material may cause the reduction or enhancement of the spectral weight because the presence of impurity makes symmetry breaking. Note that this unfolded spectral weight $W_{KJ}^{k}$ collects contributions over $K$ to obtain $A_{kj,kj}^{\alpha\beta}(\omega)$ in Eq. (15). Therefore, $A_{kj,kj}^{\alpha\beta}(\omega)$ only includes one unfolded spectral weight summed over $K$.

After calculating $A_{KJ,KJ}^{\alpha\beta}(\omega)$ in Eq. (6) and $W_{KJ}^{k}$ in Eq. (16), the spectral function tensor $A_{kj,kj}^{\alpha\beta}(\omega)$ for the reference cell in Eq. (15) can be evaluated. Through Eq. (15), the band structure of the supercell is unfolded into the Brillouin zone of the reference cell with the transition weights of partial optical conductivity. Subsequently, Eqs. (5) and (15) can be substituted into Eq. (7) to obtain an unfolded partial optical conductivity $\sigma_{\alpha\beta}(k,j,\omega)$ represented by the reference cell as follows:
$$
\begin{aligned}
\sigma_{\alpha\beta}(k,j,\omega) & =\frac{-i}{\Omega_{\text{rc}}}A_{kj,kj}^{\alpha\beta}(\omega) \\
& =\frac{-i}{\Omega_{\text{rc}}}\frac{L}{l}\sum_{KG}\delta_{k-G,K}W_{KJ}^{k}A_{KJ,KJ}^{\alpha\beta}(\omega) \\
& =\left(\frac{L}{l}\right)^{2}\sum_{KG}\delta_{k-G,K}W_{KJ}^{k}\sigma_{\alpha\beta}(K,J,\omega),\quad(17)
\end{aligned}
$$
where $\Omega/\Omega_{\text{rc}}=L/l$. Finally, after summing over frequencies $\omega$ on the interval $[a,b]$, the unfolded and integrated partial optical conductivity $\sigma_{\alpha\beta}(k,j,\omega(a:b))$ can be expressed as
$$
\sigma_{\alpha\beta}(k,j,\omega(a:b))\equiv\int_{a}^{b}\sigma_{\alpha\beta}(k,j,\omega)d\omega,\tag{18}
$$

The integrated unfolded partial optical conductivity gathers contributions of optical transition weights over a selected frequency range and it can be put on the unfolded electronic band structure of a material to show optical transitions at states in a fat band representation. The numerical demonstration of unfolded and integrated partial optical conductivity is provided in the Appendix.

### D. Separation of unfolded partial optical conductivity

Equation (2) for calculating MME includes two summations over individual atomic orbitals. After rearranging the order of the summation, Eq. (2) can be rewritten as
$$
\langle KJ|\hat{P}_{\alpha}|KJ'\rangle=\sum_{mn}\langle KJ|\hat{P}_{\alpha}^{mn}|KJ'\rangle,\tag{19}
$$

where $m$ and $n$ are orbitals' indices and the partial MME is defined as

$$
\begin{aligned}
&\left\langle K J\left|\hat{P}_{\alpha}^{m n}\right| K J^{\prime}\right\rangle \\
& \equiv-i \sum_{a} C_{m}^{K J *} C_{n}^{K J^{\prime}} e^{-i \boldsymbol{K} \cdot\left(\boldsymbol{R}_{a}-\boldsymbol{R}_{0}\right)}\left\langle\phi_{m}\left(\boldsymbol{r}-\boldsymbol{R}_{a}\right)\left|\nabla_{\alpha}\right| \phi_{n}(\boldsymbol{r})\right\rangle .
\end{aligned}
$$

By substituting Eq. (19) back to Eq. (4), the partial optical conductivity $\sigma_{\alpha \beta}(K, J, \omega)$ can be reexpressed as

$$
\sigma_{\alpha \beta}(K, J, \omega)=\sum_{m n n^{\prime} m^{\prime}} \sigma_{\alpha \beta}^{m n n^{\prime} m^{\prime}}(K, J, \omega),
$$

where

$$
\begin{aligned}
& \sigma_{\alpha \beta}^{m n n^{\prime} m^{\prime}}(K, J, \omega) \\
& \equiv \frac{-i}{\Omega} \sum_{J^{\prime}} \frac{f_{K J}-f_{K J^{\prime}}}{\epsilon_{K J}-\epsilon_{K J^{\prime}}} \frac{\left\langle K J\left|\hat{P}_{\alpha}^{m n}\right| K J^{\prime}\right\rangle\left\langle K J^{\prime}\left|\hat{P}_{\beta}^{n^{\prime} m^{\prime}}\right| K J\right\rangle}{\epsilon_{K J}-\epsilon_{K J^{\prime}}+\omega+i \eta} .
\end{aligned}
$$

Therefore, orbital transitions of partial optical conductivity can be evaluated by assigning four individual atomic orbitals. Similarly, by using the same rearrangement for the order of the summation in MME, orbital transitions of an unfolded partial optical conductivity can be obtained by four individual atomic orbitals. The formula of the unfolded partial optical conductivity $\sigma_{\alpha \beta}(k, j, \omega)$ in Eq. (17) can be rewritten as below to show the summation over all combinations of four individual atomic orbitals as follows:

$$
\sigma_{\alpha \beta}(k, j, \omega)=\sum_{m n n^{\prime} m^{\prime}} \sigma_{\alpha \beta}^{m n n^{\prime} m^{\prime}}(k, j, \omega),
$$

where

$$
\sigma_{\alpha \beta}^{m n n^{\prime} m^{\prime}}(k, j, \omega)=\left(\frac{L}{l}\right)^{2} \sum_{K G} \delta_{k-G, K} W_{K J}^{j k} \sigma_{\alpha \beta}^{m n n^{\prime} m^{\prime}}(K, J, \omega) .
$$

According to Eq. (24), the individual contribution of orbital transitions of an unfolded partial optical conductivity can be separated by four assigned orbitals, such as $s$, $p$, $d$, and $f$ orbitals.

## III. SI-DOPED GRAPHENE

To demonstrate this analysis method, we provide optical conductivity of a monolayer Si-doped graphene (SiG) as an example. A monolayer SiG with a band gap and without a degradation in carrier mobility at a low doping level had been synthesized for designing optoelectronic devices [50]. The electronic band structure and optical properties of a monolayer graphene sheet with different silicon-doping levels had been reported [48,54,55]. In this section we demonstrate that the transition weights of optical conductivity of SiGs can be projected to corresponding electronic band structure by using the unfolding optical transition method proposed in the paper, and discuss doping effects in a supercell of graphene.

### A. Computational details

The geometry optimizations with a regular mesh of 300 Ry in real space are performed by the OpenMX code (v3.8) based on DFT [53,56-58] with norm-conserving pseudopotentials [59] and optimized pseudoatomic orbitals [60] as basis sets. The optimized radial functions used are C-s2p2d1, Si-s2p2d1, and E-s2p2d2f1 for carbon, silicon, and ghost atoms, where the abbreviations of basis functions stand for (atomic symbol)-(number of radial functions for $s, p, d$, and $f$ orbitals), such as C-s2p2d1 represents each carbon atom with 2 s orbitals, 2 p orbitals, and 1 d orbital. The cutoff radii of optimized radial functions at each C atom, Si atom, and ghost atom are 6.0, 7.0, and 13.0 bohrs, respectively. The ghost atom is included for calculating the accurate electronic band structure of conduction levels and it is placed at the center of honeycomb ring of graphene and SiGs. The exchangecorrelation energy functional is treated by the generalized gradient approximation with the Perdew-Burke-Ernzerhof form [61]. An electronic temperature of 300 K is employed to make electrons occupy eigenstates with the Fermi-Dirac function in the calculations. For all of optimizations, the force convergence criterion is $10^{-4}$ Hartree/bohr and the electronic self-consistent field criterion is $10^{-8}$ Hartree.

The optimized lattice constants of graphenes with different Si-doping levels are listed in Table I and corresponding structures are shown in Fig. 1. By substituting a Si atom with a C atom in graphene, the structure of graphene will have a deformation due to the larger Si atomic radius [62] and the longer Si-C bond length in comparison with the C-C bond lengths [63]. Therefore, the lattice constant $a(=b)$, Si-C, and C-C(2) bond length become longer as increasing Si concentration in graphene. These structural properties are in agreement with the experimental and calculated results [54,64-67]. In addition, according to the electronic band structure calculations as shown in Fig. 2, the band gap of graphene with Si doping of $0.00 \%, 3.13 \%, 12.50 \%$, and $50.00 \%$ at $K$ point of the first Brillouin zone are 0.003, 0.211, 0.744, and 2.468 eV, respectively. As the Si-doping percentage increases, the band

<table>
<caption>Table I: The optimized lattice constants, bond lengths, and $k$ meshes of graphenes with Si doping of $0.00\%$, $3.13\%$, $12.50\%$, and $50.00\%$. $a$ and $b$ refer to lattice constants at $x$-$y$ plane. The lattice constant $c$ (along $z$ axis) in the models is set to be $18$ Å. The C-C(1) and C-C(2) bond lengths (in Å) stand for the first and second neighboring C-C bonds of the Si atom, respectively.</caption>
<thead>
  <tr>
    <th colspan="2">Si-doping percentage</th>
    <th>$a(=b)$</th>
    <th>C-C(1)</th>
    <th>C-C(2)</th>
    <th>Si-C</th>
    <th>$k$ mesh</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Graphene</td>
    <td>0.00%</td>
    <td>2.467</td>
    <td>1.423</td>
    <td>1.424</td>
    <td>–</td>
    <td>$24\times 24\times 1$</td>
  </tr>
  <tr>
    <td>SiG ($4\times 4\times 1$)</td>
    <td>3.13%</td>
    <td>2.510</td>
    <td>1.409</td>
    <td>1.470</td>
    <td>1.681</td>
    <td>$6\times 6\times 1$</td>
  </tr>
  <tr>
    <td>SiG ($2\times 2\times 1$)</td>
    <td>12.50%</td>
    <td>2.644</td>
    <td>1.437</td>
    <td>1.550</td>
    <td>1.692</td>
    <td>$12\times 12\times 1$</td>
  </tr>
  <tr>
    <td>SiG ($1\times 1\times 1$)</td>
    <td>50.00%</td>
    <td>3.102</td>
    <td>–</td>
    <td>–</td>
    <td>1.791</td>
    <td>$24\times 24\times 1$</td>
  </tr>
</tbody>
</table>

![](./images/812576491618435073_2.jpg)

FIG. 1. The top view of the optimized monolayer crystal structures by XCrySDen [70]: (a) graphene, (b) SiG ($1 \times 1 \times 1$ supercell), (c) SiG ($2 \times 2 \times 1$ supercell), and (d) SiG ($4 \times 4 \times 1$ supercell). The yellow and cyan balls represent the C atoms and the Si atoms, respectively. Note that ghost atoms located at the center of honeycomb ring are not shown.

gap of Si-doped graphene becomes larger, which is consistent with the calculated results [54].

### B. Optical conductivity of Si-doped graphenes

Electron currents of the Si-doped graphene with a small band gap can be induced by applying a voltage to penetrate through its $x$-$y$ plane from source to drain [50]. Because of the fact that electron current density is proportional to optical conductivity, i.e., $J(\omega)=\sigma(\omega)E(\omega)$, we analyze frequency-dependent optical conductivity of SiGs to investigate the Si-doping effect by comparing it with that in nondoped graphene.

![](./images/812576491618435073_3.jpg)

FIG. 2. The electronic band structures of Si-doped graphenes (SiGs) with 0.0%, 3.13%, 12.5%, and 50.0% are shown from left to right in sequence. The Fermi level is set to be 0 eV.

![](./images/812576491618435073_4.jpg)

FIG. 3. The optical conductivities $\text{Re}[\sigma(\omega)]$ of graphene and SiGs with doping level 3.13%, 12.5%, and 50.0% are shown in (a). The partial optical conductivities $\text{Re}[\sigma_{xx}(\omega)]$ of graphene and SiGs are shown in (b). The unit of conductivity $\sigma_0$ is $e^2/4\hbar$ [45,71]. The $k$ meshes of pristine graphene, SiG-($2 \times 2 \times 1$), and SiG-($4 \times 4 \times 1$), are set to be $400 \times 400 \times 1$, $200 \times 200 \times 1$, and $100 \times 100 \times 1$, respectively, in optical calculations. The resonance energy corresponds to the energy difference between two states, such as $|E_{\text{unoccupied}} - E_{\text{occupied}}|$.

Using the Kubo-Greenwood formula in Eq. (1), the frequency-dependent optical conductivity of graphene and SiGs are calculated as shown in Fig. 3(a). The real part of optical conductivity $\sigma_{xx}(\omega)[=\sigma_{yy}(\omega)]$ of graphene in $xx$/$yy$ direction is dominant at low frequencies (below 10 eV) [68,69], while the $zz$ component only appears above 10 eV. Optical conductivity of graphene at low frequencies is triggered by a low applied voltage. Therefore, the $zz$ component of optical conductivity of graphene materials has little contribution to electron currents and can be ignored.

In addition, the optical conductivity of graphene with a Si-doping level about 3.13% [SiG-($4 \times 4 \times 1$)] has a similar shape in comparison with that of graphene and its peak at around 4 eV is slightly weaker due to the substitution of a silicon atom for one of 32 carbon atoms in graphene in Fig. 3(a). As the Si-doping percentage is getting higher (more than 12.5%), Si-doped graphenes become more like insulators gradually. The arrow-pointed peaks in Fig. 3(a) indicate the band gap becomes larger since the peak of optical conductivity of SiG-($4 \times 4 \times 1$) shifts from 0.211 to 0.744 eV in SiG-($2 \times 2 \times 1$) and to 2.468 eV in SiG-($1 \times 1 \times 1$). It implies that optical conductivity of SiGs will decrease gradually at a low applied voltage as the Si-doping level increases.

Since SiG-($4 \times 4 \times 1$) has a similar optical conductivity with graphene, we analyze individual contributions of optical conductivity decomposed to C atoms, Si atom, and/or relevant orbitals. In Fig. 3(b) the partial optical conductivity contributed from C atoms is almost the same as total optical conductivity of SiG-($4 \times 4 \times 1$). As for the partial optical conductivity decomposed to the Si atom, the contribution of optical conductivity is quite low and close to zero at $\omega <$ 8 eV, which implies that electrons within the Si atom are

![](./images/812576491618435073_5.jpg)

FIG. 4. The real part of unfolded and integrated partial optical conductivity $\mathrm{Re}[\sigma_{(xx+yy)/2}(k,j,\omega(0:6\,\text{eV}))]$ of graphene with different Si-doping levels: (a) 0%, (b) 3.13%, (c) 12.5%, and (d) 50.0% are put in the corresponding (unfolded) band structure. The unit of unfolded and integrated partial optical conductivity is set to be the same as one in Fig. 3. $\eta$ is 0.05 eV. The unfolded band weights ($W$) of SiG-$(4\times4\times1)$ and SiG-$(2\times2\times1)$ are shown in (e) and (f), respectively.

not induced to move on the $x$-$y$ plane. Furthermore, after optical conductivities of graphene and SiG-$(4\times4\times1)$ were separated from all of $p_{z}$ orbitals as shown in Fig. 3(b) with gray and magenta lines, one can notice that the shapes of partial optical conductivity in both cases are similar although their magnitudes are lower than those decomposed to all orbitals in C atoms (with the orange line) about 30%.

### C. Unfolded and integrated partial optical conductivity of Si-doped graphenes

Unfolded and integrated partial conductivity $\sigma_{\alpha\beta}(k,j,\omega(a:b))$ gives an alternative way to investigate the transition weights of optical conductivity in an impurity material at different $k$ and states after summation over frequencies $\omega$ from $a=0$ eV to $b=6$ eV by Eq. (18). In order to show changes of optical transitions between graphene and SiGs, the unfolded and integrated partial optical conductivity of graphene with different Si-doping levels are calculated and shown in Fig. 4(a). First, the major transition weights of partial optical conductivity of graphene in the electronic band structure at below 6 eV come from $K$ point and $M$ point. Graphene has a large optical transition at $K$ point at $\omega\approx0$ eV. Also, optical transitions between two states in graphene take place at a flat band (close to $M$ point) and it corresponds to the sharp peak of optical conductivity in graphene at $\omega\approx4$ eV in Fig. 3(a). Second, in the case of SiG-$(4\times4\times1)$, the optical transition occurs at $K$ point at $\omega\approx0.211$ eV and at the flat band ($\omega\approx4$ eV) as shown in Fig. 4(b). Graphene and SiG-$(4\times4\times1)$ have a similar pattern of optical transitions. However, due to a low Si-doping level (3.13%), SiG-$(4\times4\times1)$ opens a small band gap and its states from $K$ point to $M$ point are slightly split. Third, as the Si-doping level increases over 12.5%, optical conductivities in SiG-$(2\times2\times1)$ and SiG-$(1\times1\times1)$ are getting small, although major optical transitions still occur at the $K\rightarrow M$ path in Figs. 4(c) and 4(d). It leads to decrease of the total optical conductivity of SiG at a high Si-doping percentage.

![](./images/812576491618435073_6.jpg)

FIG. 5. The real part of unfolded and integrated partial optical conductivity $\mathrm{Re}[\sigma_{(xx+yy)/2}(k,j,\omega(0:6\,\text{eV}))]$ of SiG-$(4\times4\times1)$ decomposed to (a) the C atoms, (b) the Si atom, and (c) C atoms' $p_{z}$ orbitals are put on in the unfolded electronic band structure. The color-box scale for the unfolded and integrated partial optical conductivity is set to be the same as one in Fig. 4. $\eta$ is 0.05 eV.

In order to investigate the Si-doping effect, the unfolded and integrated partial optical conductivity decomposed to C atoms and Si atom in the SiG-$(4\times4\times1)$ are shown in Figs. 5(a) and 5(b), respectively. In Fig. 5(a) the transition weights of optical conductivity of SiG-$(4\times4\times1)$ contributed from C atoms are almost the same as those of optical conductivity of SiG-$(4\times4\times1)$ in Fig. 4 (b). In contrast, in Fig. 5(b) the transition weights of optical conductivity of SiG-$(4\times4\times1)$ contributed from the Si atom are quite low. It implies that optical transitions of SiG-$(4\times4\times1)$ come from C atoms, not from the Si atom. Therefore, as the Si-doping level increases, optical conductivity of SiG will become less and its band gap will be getting larger. The Si-doping effect is like placing stones into a river to hinder current flow.

Furthermore, unfolded and integrated partial optical conductivity contributed from all of $p_{z}$ orbitals in C atoms in Fig. 5(c) shows the same pattern of optical transitions as one from all orbitals in C atoms in Fig. 5(a) and its contribution lowers about 30%. In addition, the $d_{xz}$ orbitals or $d_{yz}$ orbitals also involve the $\pi$-$\pi^{*}$ transition like the transition from $p_{z}$ orbitals to $p_{z}$ orbitals, but their contributions are much lower. The magnitude order of optical transition weights belonging to orbitals in SiG-$(4\times4\times1)$ is $W_{p_{z}-p_{z}}>W_{p_{z}-d_{xz/yz}}>W_{d_{xz}-d_{xz}}(=W_{d_{yz}-d_{yz}})>W_{d_{xz}-d_{yz}}(=W_{d_{yz}-d_{xz}})$. Consequently, the

![](./images/812576491618435073_7.jpg)

FIG. 6. The (unfolded) integrated partial optical conductivities Re[$\sigma_{xx+yy}(k,j,\omega(0:20$ eV))] of graphene-($1\times1\times1$) and ($2\times2\times$ 1) (with $\eta=0.05$ eV) are shown in the corresponding state of the electronic band structure. The transition weights of (unfolded) integrated partial optical conductivities are presented by size of blue/red circles. The solid line is the band structure of graphene.

most part of electrons can be driven by orbitals with $z$ components in C atoms to induce current flow when a low voltage is applied.

## IV. CONCLUSIONS
We have developed an unfolding optical transition method by combining the Kubo-Greenwood formula with the unfolding method for the band structure. This unfolding optical transition method enables us to construct an unfolded electronic band structure of a supercell to a reference cell with optical transition weights, which provides an analysis tool to understand how the optical transition is perturbed by structural imperfections such as impurities and disorders. Although we developed the unfolding optical transition method for the LCAO method, it might be straightforward to apply the ideal for other methods with Wannier functions [36,72,73]. We have applied the method to optical conductivity of graphene with different Si-doping levels for studying the silicon-doping effect. Results show that the C atoms in the SiG-($4\times4\times1$) contribute almost all of optical conductivity, whereas the Si atom has little contribution after unfolded and integrated partial optical conductivity is decomposed to C atoms and the Si atom in the SiG-($4\times4\times1$). It implies that doping Si atoms can decrease optical conductivity of SiGs and hinder current flow. Furthermore, after the decomposition to different orbitals by unfolding optical transition method, the $p_{z}$ orbitals of C atoms contribute the largest optical conductivity from $K$ point to $M$ point in the first Brillouin zone. The magnitude order of optical transition weights belonging to orbitals in the SiG-($4\times4\times1$) is $W_{p_{z}-p_{z}}>W_{p_{z}-d_{xz/yz}}>W_{d_{xz}-d_{xz}}(=W_{d_{yz}-d_{yz}})>W_{d_{xz}-d_{yz}}(=W_{d_{yz}-d_{xz}})$. These optical transitions correspond to $\pi$-$\pi^{*}$ transitions. It shows that the orbitals with $z$ components in C atoms provide main channels to make electrons flow from source to drain. Finally, in addition to the frequency-dependent optical conductivity $\sigma(\omega)$, the unfolding optical transition method provides an alternative method to present $(k,$ state)-dependent optical conductivity of an impurity material in an unfolded electronic band structure for studying defects, disorders, and doping effects.

## ACKNOWLEDGMENTS
This paper is partly based on results obtained from a project commissioned by the New Energy and Industrial Technology Development Organization of Japan (NEDO) Grant No. (P16010). C.C.L. acknowledges partial support from the Ministry of Science and Technology of Taiwan under Contract No. MOST 108-2112-M-032-010-MY2.

## APPENDIX: NUMERICAL DEMONSTRATION OF UNFOLDED AND INTEGRATED PARTIAL OPTICAL CONDUCTIVITY
To confirm that the unfolding optical transition method is valid, we take the unfolded and integrated partial optical conductivity Re[$\sigma_{xx+yy}(k,j,\omega(0:20$ eV))] of graphene-($2\times$ $2\times1$) as an example in comparison with that of graphene-($1\times1\times1$). The unfolded and integrated partial optical conductivity of graphene-($2\times2\times1$) is plotted in the electronic band structure with open circles whose size is proportional to the magnitude of the Re[$\sigma_{xx+yy}(k,j,\omega(0:20$ eV))] as shown in Fig. 6. The transition weights of the unfolded and integrated partial optical conductivity of graphene-($2\times2\times1$) are almost the same as those of graphene-($1\times1\times1$), except for $M$ point. Degenerate states with different transition weights appear, like $M$ point, after applying the unfolding method. The sum of transition weights at these degenerate states is equal to one. The sum of unfolded and integrated partial frequency-dependent optical conductivities of graphene-($2\times2\times1$) at the degenerate energy level is close to that of graphene-($1\times1\times1$). Note that the small difference of the unfolded and integrated partial optical conductivity of graphene-($2\times$ $2\times1$) in comparison with the partial optical conductivity of graphene-($1\times1\times1$) can be attributed to numerical error in the different unit cells.

[1] F. A. Jenkins and H. E. White, *Fundamentals of Optics*, 4th ed. (McGraw-Hill, New York, 1976).
[2] H. Onodera, I. Awai, and J. Ikenoue, *Appl. Opt.* **22**, 1194 (1983).
[3] B. Šantić, D. Gracin, and K. Juraić, *Appl. Opt.* **48**, 4430 (2009).
[4] J. Chen, J. Zhao, X. Huang, and Z. Huang, *Appl. Opt.* **49**, 5592 (2010).
[5] S. Singh, *Phys. Scr.* **65**, 167 (2002).
[6] M. Hébert, R. D. Hersch, and P. Emmel, *Handbook of Digital Imaging*, edited by M. Kriss (Wiley, New York, 2015), pp. 1021–1077.
[7] B. G. Ghamsari, J. Tosado, M. Yamamoto, M. S. Fuhrer, and S. M. Anlage, *Sci. Rep.* **6**, 34166 (2016)

075143-7

[8] M. Marjanović, V. Paunović, Z. Prijić, A. Prijić, D. Danković, and V. Mitić, *X International Symposium on Industrial Electron- ics - INDEL, 06-08 November 2014* (Banja Luka, Bosnia and Herzegovina, 2014), pp. 38-41.

[9] T. T. Grove, M. F. Masters, and R. E. Miers, *Am. J. Phys.* **73**, 52 (2005).

[10] C. C. Homes, J. J. Tu, J. Li, G. D. Gu, and A. Akrap, *Sci. Rep.* **3**, 3446 (2013).

[11] M. S. Dresselhaus, *Solid State Physics Part II: Optical Proper- ties of Solids* (2001), MIT Solid State Physics Course, available at http://web.mit.edu/course/6/6.732/www/6.732-pt2.pdf.

[12] M. Fox, *Optical Properties of Solids* (Oxford University Press, Oxford, 2001).

[13] S. Kasap and P. Capper, *Springer Handbook of Electronic and Photonic Materials* (Springer International, Berlin, 2017).

[14] F. Flory, L. Escoubas, and G. Berginc, *J. Nanophoton.* **5**, 052502 (2011).

[15] Y. Zhang and Y. Wang, *RSC Adv.* **7**, 45129 (2017).

[16] F. N. Xia, H. Wang, D. Xiao, M. Dubey, and A. Ramasubramaniam, *Nat. Photon.* **8**, 899 (2014).

[17] S. Wang, H. Tian, C. Ren, J. Yu, and M. Sun, *Sci. Rep.* **8**, 12009 (2018).

[18] G. G. Naumis, S. Barraza-Lopez, M. Oliva-Leyva, and H. Terrones, *Rep. Prog. Phys.* **80**, 096501 (2017).

[19] J. P. Carbotte, K. R. Bryenton, and E. J. Nicol, *Phys. Rev. B* **99**, 115406 (2019).

[20] T. Stauber, P. San-Jose, and L. Brey, *New J. Phys.* **15**, 113050 (2013).

[21] A. Charnukha, *J. Phys.: Condens. Matter* **26**, 253203 (2014).

[22] D. N. Basov and T. Timusk, *Rev. Mod. Phys.* **77**, 721 (2005).

[23] S. Tajima, *Rep. Prog. Phys.* **79**, 094001 (2016).

[24] M. Mitrano, A. Cantaluppi, D. Nicoletti, S. Kaiser, A. Perucchi, S. Lupi, P. Di Pietro, D. Pontiroli, M. Riccò, S. R. Clark, D. Jaksch, and A. Cavalleri, *Nature (London)* **530**, 461 (2016).

[25] S. L. Jacques, *Phys. Med. Biol.* **58**, R37 (2013).

[26] P. K. Nayak, C.-H. Yeh, Y.-C. Chen, and P.-W. Chiu, *ACS Appl. Mater. Interfaces* **6**, 16020 (2014).

[27] F. Hütt, A. Yaresko, M. B. Schilling, C. Shekhar, C. Felser, M. Dressel, and A. V. Pronin, *Phys. Rev. Lett.* **121**, 176601 (2018).

[28] V. Karpus, S. Tumėnas, A. Eikevičius, and H. Arwin, *Phys. Status Solidi B* **253**, 419 (2016).

[29] L. M. Malard, K. F. Mak, A. H. Castro Neto, N. M. R. Peres, and T. F. Heinz, *New J. Phys.* **15**, 015009 (2013).

[30] F. L. Bourguiba, A. Dhahri, T. Tahri, K. Taibi, J. Dhahri, and E. K. Hlil, *Bull. Mater. Sci.* **39**, 1765 (2016).

[31] I. Santoso, R. S. Singh, P. K. Gogoi, T. C. Asmara, D. Wei, W. Chen, A. T. S. Wee, V. M. Pereira, and A. Rusydi, *Phys. Rev. B* **89**, 075134 (2014).

[32] S. Luo, Y. Wang, X. Tong, and Z. Wang, *Nanoscale Res. Lett.* **10**, 1 (2015).

[33] F. Chen, S.-W. Wang, L. Yu, X. Chen, and W. Lu, *Opt. Mater. Express* **4**, 1833 (2014).

[34] A. Manjavacas, S. Thongrattanasiri, J.-J. Greffet, and F. G. Garcia de Abajo, *Appl. Phys. Lett.* **105**, 211102 (2014).

[35] F. Qian, X. Li, L. Tang, S. K. Lai, C. Lu, and S. P. Lau, *AIP Adv.* **6**, 075116 (2016).

[36] W. Ku, T. Berlijn, and C.-C. Lee, *Phys. Rev. Lett.* **104**, 216401 (2010).

[37] C.-C. Lee, Y. Yamada-Takamura, and T. Ozaki, *J. Phys.: Condens. Matter* **25**, 345501 (2013).

[38] I. Deretzis, G. Calogero, G. G. N. Angilella, and A. La Magna, *Europhys. Lett.* **107**, 27006 (2014).

[39] R. Kubo, *J. Phys. Soc. Jpn.* **12**, 570 (1957).

[40] D. Greenwood, *Proc. Phys. Soc.* **71**, 585 (1958).

[41] L. Calderín, V. V. Karasiev, and S. B. Trickey, *Comput. Phys. Commun.* **221**, 118 (2017).

[42] P. B. Allen, *Conceptual Foundations of Materials: A Standard Model for Ground- and Excited-State Properties*, Contemporary Concepts of Condensed Matter Science (Elsevier, Amsterdam, 2006), pp. 165-218.

[43] C.-C. Lee, Y.-T. Lee, M. Fukuda, and T. Ozaki, *Phys. Rev. B* **98**, 115115 (2018).

[44] D. V. Knyazev and P. R. Levashov, *Comput. Mater. Sci.* **79**, 817 (2013).

[45] L. Matthes, O. Pulci, and F. Bechstedt, *New J. Phys.* **16**, 105007 (2014).

[46] J. Clérouin, Y. Laudernet, V. Recoules, and S. Mazevet, *Phys. Rev. B* **72**, 155122 (2005).

[47] R. Bianco, R. Resta, and I. Souza, *Phys. Rev. B* **90**, 125153 (2014).

[48] M. Houmad, H. Zaari, A. Benyoussef, A. El Kenz, and H. Ez-Zahraouy, *Carbon* **94**, 1021 (2015).

[49] M. S. Sharif Azadeh, A. Kokabi, M. Hosseini, and M. Fardmanesh, *Micro Nano Lett.* **6**, 582 (2011).

[50] S. J. Zhang, S. S. Lin, X. Q. Li, X. Y. Liu, H. A. Wu, W. L. Xu, P. Wang, Z. Q. Wu, H. K. Zhong, and Z. J. Xu, *Nanoscale* **8**, 226 (2016).

[51] D. R. Bowler and T. Miyazaki, *Rep. Prog. Phys.* **75**, 036503 (2012).

[52] J. M. Soler, E. Artacho, J. D. Gale, A. García, J. Junquera, P. Ordejón, and D. Sánchez-Portal, *J. Phys.: Condens. Matter* **14**, 2745 (2002).

[53] T. Ozaki, *Phys. Rev. B* **67**, 155108 (2003).

[54] M. Shahrokhi and C. Leonard, *J. Alloys Compd.* **693**, 1185 (2017).

[55] M. Houmad, O. Dakir, A. Abbassi, A. Benyoussef, A. El Kenz, and H. Ez-Zahraouy, *Optik* **127**, 1867 (2016).

[56] T. Ozaki and H. Kino, *Phys. Rev. B* **72**, 045121 (2005).

[57] P. Hohenbergand and W. Kohn, *Phys. Rev.* **136**, B864 (1964).

[58] W. Kohn and L. J. Sham, *Phys. Rev.* **140**, A1133 (1965).

[59] I. Morrison, D. M. Bylander, and L. Kleinman, *Phys. Rev. B* **47**, 6728 (1993).

[60] T. Ozaki and H. Kino, *Phys. Rev. B* **69**, 195113 (2004).

[61] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[62] C. Kittel, *Introduction to Solid State Physics* (Wiley, New York, 2005), p. 71.

[63] Z. Shi, Z. Zhang, A. Kutana, and B. I. Yakobson, *ACS Nano* **9**, 9802 (2015).

[64] R. Ishikawa, N. R. Lugg, K. Inoue, H. Sawada, T. Taniguchi, N. Shibata, and Y. Ikuhara, *Sci. Rep.* **6**, 21273 (2016).

[65] Y. Yamada-Takamura and R. Friedlein, *Sci. Technol. Adv. Mater.* **15**, 064404 (2014).

[66] K. Takeda and K. Shiraishi, *Phys. Rev. B* **50**, 14916 (1994).

[67] T. Susi, V. Skákalová, A. Mittelberger, P. Kotrusz, M. Hulman, T. J. Pennycook, C. Mangler, J. Kotakoski, and J. C. Meyer, *Sci. Rep.* **7**, 4399 (2017).

[68] V. M. Pereira, R. M. Ribeiro, N. M. R. Peres, and A. H. Castro Neto, *Europhys. Lett.* **92**, 67001 (2010).

[69] V. H. Nguyen, A. Lherbier, and J. C. Charlier, *2D Mater.* **4**, 025041 (2017).

[70] A. Kokalj, *Comp. Mater. Sci.* **28**, 155 (2003).

[71] T. Stauber, N. M. R. Peres, and A. K. Geim, *Phys. Rev. B* **78**, 085432 (2008).

[72] N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, and D. Vanderbilt, *Rev. Mod. Phys.* **84**, 1419 (2012).

[73] F. Giustino, Jonathan R. Yates, I. Souza, M. L. Cohen, and Steven G. Louie, *Phys. Rev. Lett.* **98**, 047005 (2007).