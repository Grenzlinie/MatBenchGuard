# Numerical Simulation of Thermal Conductivity of SiNW–SiGe₀.₃ Composite for Thermoelectric Applications

Ming-Yi Lee, Yiming Li, Member, IEEE, Min-Hui Chuang, Student Member, IEEE, Daisuke Ohori, and Seiji Samukawa, Fellow, IEEE

Abstract—The electron band structure and phonon energy dispersion of the silicon nanowires (SiNWs) embedded in SiGe₀.₃ (SiNW–SiGe₀.₃ composite) are simulated by using the effective mass Schrödinger equation and the elastodynamic wave equation, respectively. Then, the TE properties of the SiNW–SiGe₀.₃ composite are investigated by the Landauer approach. The simulation shows the contribution from electrons/holes on both electrical conductance and thermal conductance increases few times by introducing SiNWs, but on the other hand, lattice thermal conductance reduces around two orders. These results are consistent with the experimental measurement and indicates that much lower lattice thermal conductance dominates the TE performance of the SiNW–SiGe₀.₃ composite.

Index Terms—Landauer approach, silicon nanowire (SiNW), thermal conductivity.

## I. INTRODUCTION

THERMOELECTRIC (TE) energy-conversion materials have been attracting attention for use in solid-state power-generation devices. The dimensionless figure of merit $ZT$ is the parameter used to indicate the performance of the TE energy-conversion materials. Here, $ZT$ is given by

$$
ZT = \frac{S^2 \sigma T}{\kappa_{\text{ph}} + \kappa_{\text{el}}} \tag{1}
$$

where $S$ is the Seebeck coefficient, $\sigma$ is the electrical conductivity, $\kappa_{\text{ph}}$ is the lattice thermal conductivity from phonon, and $\kappa_{\text{el}}$ is the electronic thermal conductivity from electrons. To achieve $ZT > 1$, the first is to reduce the lattice or electronic thermal conductivity in the denominator of (1) and the other is to enhance the power factor, $S^2\sigma$, in the numerator. These properties are determined by the electron and phonon energy dispersion but not independently controlled. For example, the decrease in electron thermal conductivity would induce the decrease in electrical conductivity at the same time due to the same conducting carrier of electron so that the total amount of $ZT$ does not increase. On the other hand, recent experiments have demonstrated that the lattice thermal conductivity would be significantly reduced without suffering from the loss of power factor by using nanostructures in semiconductors, such as nanowires [2]–[5], superlattices [2], [6]–[10], and phononic crystal structures [11]–[15]. With these nanostructures, the lattice thermal conductivity can be suppressed due to the surface scattering of the phonon [16]–[18]; meanwhile, the electrical performance can be enhanced [19], [20].

In this article, the matrix material of the SiNW–SiGe₀.₃ shown in Fig. 1 is considered because of its potential of excellent TE performance [1], [21] and advantage of silicon materials that already exist in semiconductor industry. This composite film consists of silicon nanowires (SiNWs) embedded in the conductive material SiGe₀.₃ and is schematically modeled as periodic SiNW square superlattice for the following simulation.

## II. MODELING AND SIMULATION METHODOLOGY

For the periodic SiNWs, as shown in Fig. 1, the electron band structure could numerically be solved by the Schrödinger equation with the effective mass approximation under the Bloch theorem [22]

$$
\begin{aligned}
\nabla\left[-\frac{\hbar^2}{2m^*}\nabla u_{\boldsymbol{k}}(\boldsymbol{r})\right] &-\frac{i\hbar^2}{m^*}\boldsymbol{k} \cdot \nabla u_{\boldsymbol{k}}(\boldsymbol{r}) \\
&+\left[V(\boldsymbol{r})+\frac{\hbar^2k^2}{2m^*}\right]u_{\boldsymbol{k}}(\boldsymbol{r}) = E_{n,k}u_{\boldsymbol{k}}(\boldsymbol{r}) \tag{2}
\end{aligned}
$$

where $\hbar$, $m^*$, $V(\boldsymbol{r})$, $E_{n,k}$, and $u_{\boldsymbol{k}}(\boldsymbol{r})$ are the reduced Plank’s constant, the effective mass, the position-dependent potential energy, the quantum energy levels, and the corresponding wave function, respectively. On the other hand, the phonon energy

Manuscript received August 31, 2019; revised December 14, 2019; accepted February 10, 2020. This work was supported in part by the Ministry of Science and Technology, Taiwan, under Grant MOST 108-2221-E-009-008 and Grant MOST 108-3017-F-009-001, and in part by the "Center for mmWave Smart Radar Systems and Technologies" under the Featured Areas Research Center Program within the framework of the Higher Education Sprout Project by the Ministry of Education in Taiwan. The review of this article was arranged by Editor R. Venkatasubramanian. (Corresponding author: Yiming Li.)

Ming-Yi Lee and Min-Hui Chuang are with the Institute of Communications Engineering, National Chiao Tung University, Hsinchu 300, Taiwan.

Yiming Li is with the Institute of Communications Engineering, National Chiao Tung University, Hsinchu 300, Taiwan, and also with the Center for mmWave Smart Radar Systems and Technologies, National Chiao Tung University, Hsinchu 300, Taiwan (e-mail: ymli@faculty.nctu.edu.tw).

Daisuke Ohori is with the Institute of Fluid Science, Tohoku University, Sendai 980-8577, Japan.

Seiji Samukawa is with the Institute of Fluid Science, Tohoku University, Sendai 980-8577, Japan, and also with the Center for mmWave Smart Radar Systems and Technologies, National Chiao Tung University, Hsinchu 300, Taiwan.

Color versions of one or more of the figures in this article are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TED.2020.2975079

0018-9383 © 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.

![](./images/812657170733596673_1.jpg)

![](./images/812657170733596673_2.jpg)

Fig. 1. (a) Cross-sectional SEM image of a highly ordered SiNW array with nanowire with a height of 100 nm and an average diameter of 10 nm, which is formed after neural beam etching using polyethylene glycol-modified ferritin as a mask [1]. (b) SiNWs are then embedded in SiGe₀.₃ by thermal CVD techniques as schematically modeled by a square superlattice of SiNW with dimensions of height $h = 100$ nm, radius $r = 5$ nm, and space $s = 2{\sim}15$ nm. The square superlattice is described by a unit cell with primary vectors of $\boldsymbol{a_1}$ and $\boldsymbol{a_2}$.

dispersion is numerically solved by the elastodynamic wave equation [13] given by the following equation:

$$
\nabla \cdot [\boldsymbol{C} \nabla u(\boldsymbol{r})] = -\rho \omega^2 u(\boldsymbol{r}) \tag{3}
$$

and where $u$ is the displacement vector, $\rho$ is the mass density, $\omega$ is the eigenfrequency, and $\boldsymbol{C}$ is the elastic constant matrix that describes the second-order strain energy density [23]. Here, $\boldsymbol{C}$ is a $6 \times 6$ symmetric matrix that has 21 independent elements. Since the silicon has a cubic symmetry, the number of independent elastic constants reduced to three: $C_{11}$, $C_{12}$, and $C_{44}$. Due to the periodicity of the square superlattice as in Fig. 1, the eigenvalue $E(\boldsymbol{k})$ or eigenfrequency $\omega(\boldsymbol{q})$ can be calculated by a finite-element method (FEM) solver for each sampling $\boldsymbol{k}$- or $\boldsymbol{q}$-points in the irreducible Brillouin zone. The parameters used to calculate the electronic band structure and phonon energy dispersion are listed in Table I.

Based on the calculated $E(\boldsymbol{k})$ and $\omega(\boldsymbol{q})$, the Landauer approach [25], [26] is adopted to describe the electron transport and phonon transport in nanostructures and investigate the quantum effect of the nanostructure on the TE performance [27] because of its physical insight in the ballistic limit as well as the quasi-ballistic and diffusive regimes.

TABLE I
LIST OF PARAMETERS USED IN THE SIMULATION OF ELECTRONIC
BAND STRUCTURE AND PHONONIC DISPERSION [24]

<table>
 <tbody>
  <tr>
   <td rowspan="2">
    Materials
   </td>
   <td colspan="2">
    Electron mass ($m_e$)
   </td>
   <td colspan="2">
    Hole mass ($m_e$)
   </td>
   <td>
    Bandgap
   </td>
  </tr>
  <tr>
   <td>
    $m_{l}^{*}$
   </td>
   <td>
    $m_{t}^{*}$
   </td>
   <td>
    $m_{hh}^{*}$
   </td>
   <td>
    $m_{lh}^{*}$
   </td>
   <td>
    eV
   </td>
  </tr>
  <tr>
   <td>
    Si
   </td>
   <td>
    0.98
   </td>
   <td>
    0.19
   </td>
   <td>
    0.49
   </td>
   <td>
    0.16
   </td>
   <td>
    1.12
   </td>
  </tr>
  <tr>
   <td>
    SiGe₀.₃
   </td>
   <td>
    1.14
   </td>
   <td>
    0.12
   </td>
   <td>
    0.41
   </td>
   <td>
    0.10
   </td>
   <td>
    1.00
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Materials
   </td>
   <td colspan="3">
    Elastic constants (GPa)
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    $C_{11}$
   </td>
   <td>
    $C_{12}$
   </td>
   <td>
    $C_{44}$
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    Si
   </td>
   <td>
    165.8
   </td>
   <td>
    63.9
   </td>
   <td>
    79.6
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    SiGe₀.₃
   </td>
   <td>
    154.6
   </td>
   <td>
    59.2
   </td>
   <td>
    75.8
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
 </tbody>
</table>

![](./images/812657170733596673_3.jpg)

Fig. 2. Calculated electron band structure $E(k)$ of light hole for the SiNW–SiGe₀.₃ composite with a radius of SiNW $= 5$ nm and space $= 2$ nm between the SiNWs by using (2).

The coefficients of thermoelectricity in (1), such as $\sigma$, $\kappa_{\text{el}}$, and $\kappa_{\text{ph}}$, are related to the differential conductivities $\sigma^{\prime}(E)$ and $\kappa_{\text{ph}}^{\prime}(E)$ for electrons and phonons. If the length of the quantum system in the transport direction is much longer than the mean free path for backscattering, the differential conductivities are expressed as [28], [29]

$$
\sigma^{\prime}(E) = \frac{2q^2}{h} \frac{M_{\text{el}}(E)}{A} \lambda_{\text{el}}(E)\left(-\frac{\partial f_0}{\partial E}\right)
$$

$$
\kappa_{\text{ph}}^{\prime}(E) = \frac{E^2}{hT} \frac{M_{\text{ph}}(E)}{A} \lambda_{\text{ph}}(E)\left(-\frac{\partial n_0}{\partial E}\right) \tag{4}
$$

where $M_{x}(E)/A$ and $\lambda_{x}(E)$ are the number of conducting channels per unit area and the mean free path for backscattering, respectively, for carrier $x$ with energy $E$, while $f_0$ and $n_0$ denote the Fermi-Dirac and Bose-Einstein distribution for electrons and phonons, respectively.

### III. RESULTS AND DISCUSSION

Fig. 2 shows the electron band structure $E(k)$ of light hole for the SiNW–SiGe₀.₃ composite with the parameters in Table I by using (2). The lowest bounded state (the bottom red line in Fig. 2) of light hole contributes extra number of conducting channels as shown in purple dashed line in Fig. 3. Comparing with the calculated $M_{\text{el}}$ (gray lines in Fig. 3) of bulk silicon by using the same parameters in Table I, the SiNW–SiGe₀.₃ composite has more conducting channels contributed from holes due to the energy offset of the valence

![](./images/812657170733596673_4.jpg)

Fig. 3. Number of conducting channels is shown with contributions from electrons (labeled as e), heavy holes (labeled as hh), and light holes (labeled as lh) for the SiNW–SiGe₀.₃ composite with a radius of SiNW = 5 nm and space = 15 nm between the SiNWs. The gray lines show the corresponding result of bulk silicon for comparison.

![](./images/812657170733596673_5.jpg)

Fig. 4. (a) Electrical and (b) thermal conductance are shown as a function of the Fermi level for the SiNW–SiGe₀.₃ composite (red solid line) with a radius of SiNW = 5 nm and space = 15 nm between the SiNWs and a bulk silicon (blue dashed line) for comparison.

band between the SiNW and the SiGe₀.₃ matrix. Fig. 4(a) shows the electrical conductance as a function of the Fermi level using (4). It is noted that p-type SiNW–SiGe₀.₃ composite has a larger conductance than bulk p-type silicon. This is because SiGe₀.₃ has smaller bandgap energy than Si and a larger valence band offset between SiNW and SiGe₀.₃, which induces quantum confinement and more conducting channels $M_{\rm el}$, as shown in Fig. 3. On the other hand, the conduction band offset between SiNW and SiGe₀.₃ for electrons is small so that the difference between bulk silicon and SiNW–SiGe₀.₃ composite on electrical conductance is marginal. The thermal conductance from charge [Fig. 4(b)] has the same phenomenon as electrical conductance, since the carriers are also electrons and holes. Although the thermal conductance from charge is larger for the SiNW–SiGe₀.₃ composite, its effect on the TE performance $ZT$ as (1) is less, since the thermal conductance is dominated from phonon $\kappa_{\rm ph}$ (to be discussed later) and not from electron/hole $\kappa_{\rm el}$.

![](./images/812657170733596673_6.jpg)

Fig. 5. Energy dispersion for bulk silicon along with the specific symmetric $q$-points.

Using the elastodynamic wave equation (3), the phonon energy dispersion for bulk silicon is shown in Fig. 5. The result with only three independent elastic constants in Table I approximates the experimental data [23] well under the same order. With the same method applied on SiNW with radius 5 nm and space 2–5 nm embedded in SiGe₀.₃, the phonon energy dispersion is calculated and the number of conducting channels is shown in Fig. 6(a) and (b). There are less conducting channels in the SiNW–SiGe₀.₃ composite than that in bulk silicon, especially for phonons with energy > 0.01 eV. By introducing nanostructures, the number of conducting channels is reduced due to the frequent scattering between the phonons and the system boundaries [30], [31]. However, the SiNW–SiGe₀.₃ composite with a space of 2 nm shows more conducting channels than that with a space of 5 nm, which would be the reduction in the surface scattering of the SiNWs, since whole SiNW–SiGe₀.₃ composite with a space of 2 nm is more similar to a bulk silicon.

In order to calculate the lattice thermal conductivity from (4), the mean free path as a function of energy for backscattering $\lambda_{\rm ph}(E)$ or its average $\overline{\lambda_{\rm ph}}$ should be known [19]. With the calibration to the thermal conductivity of bulk silicon [3] about 150 W/mK from phonon dispersion

![](./images/812657170733596673_7.jpg)

Fig. 6. Number of conducting channels is calculated for SiNW-SiGe₀.₃ composite in radius 5 nm and varied space (a) 2 and (b) 5 nm in comparison with bulk silicon (red line).

in Fig. 5, the average mean free path for backscattering $\overline{\lambda_{\mathrm{ph}}}$ is extracted to be around 140 nm [28]. Here, $\overline{\lambda_{\mathrm{ph}}}$ is also related to the conventional mean free path $\overline{\Lambda_{\mathrm{ph}}}$ by $\overline{\lambda_{\mathrm{ph}}} = 4/3\overline{\Lambda_{\mathrm{ph}}}$, where $4/3$ comes from averaging over angle in three dimensions [19], [28]. To include further the effect of nanostructures, Matthiessen's rule is commonly used to combine different scattering mechanisms so that the mean free path is given by $1/\overline{\Lambda} = 1/\overline{\Lambda_{\text{bulk}}} + 1/\overline{\Lambda_{i}}$, where $\overline{\Lambda_{\text{bulk}}}$ is the mean free path for bulk material and $\overline{\Lambda_{i}}$ is the characteristic length for other internal scattering process [30]. With the estimated mean free path, the phonon thermal conductivity of the SiNW-SiGe₀.₃ composite is calculated through (4) and shown in Fig. 7. The simulated $\kappa_{\mathrm{ph}}$ for SiNW with density around $1.6 \times 10^{11}/\mathrm{cm}^2$ (radius 5 nm and space 15 nm) agrees with the experimental results in [1]. The results reveal that the Landauer approach (4) well describes the reduction in thermal conductivity contributed from phonons as experiments in almost two order with energy dispersion simply deduced from the elastodynamic wave equation (3) and estimation of mean free path from Matthiessen's rule.

Here, the effective mass approximation, linear elasticity, and Landauer approach with an average of mean free path approximation in Section II are adopted to reduce the complexity of computation and achieve the studies for nanostructures in this article as literatures [32], [33]. However, it is noticed that there is room for improvement, such as $k\cdot p$ method limitation [34], [35], nonlinear elasticity with the size of nanostructures [36], [37], and theory of mean-free-path distribution [38], [39].

![](./images/812657170733596673_8.jpg)

Fig. 7. Thermal conductance contributed from lattice dynamic for bulk silicon and SiNW (open symbols) agrees well with the experimental measurement [1] (solid symbols).

### IV. CONCLUSION

In this article, the Schrödinger equation within the effective mass approximation and the elastodynamic wave equation with three elastic constants for each material are used to calculate the energy dispersion of electrons and phonons. Based on these calculated energy dispersions, the Landauer approach is adopted with the approximation of average of mean free path to investigate the quantum effect on the TE properties for SiNWs embedded in SiGe₀.₃. From simulation, the impact of silicon nanowires on thermoelectricity from electrons, such as electrical and thermal conductance, is less than the thermal conductance from phonons. These results also well describe the measurements in the experiment.

### REFERENCES

[1] A. Kikuchi, A. Yao, I. Mori, T. Ono, and S. Samukawa, "Composite films of higly ordered Si nanowires embedded in SiGe₀.₃ for thermoelectric applications," *J. Appl. Phys.*, vol. 122, no. 16, Oct. 2017, Art. no. 165302.

[2] D. Li, Y. Wu, R. Fan, P. Yang, and A. Majumdar, "Thermal conductivity of Si/SiGe superlattice nanowires," *Appl. Phys. Lett.*, vol. 83, no. 15, pp. 3186-3188, Oct. 2003.

[3] A. I. Hochbaum *et al.*, "Enhanced thermoelectric performance of rough silicon nanowires," *Nature*, vol. 451, no. 7175, pp. 163-167, Jan. 2008.

[4] J. Chen, G. Zhang, and B. Li, "Tunable thermal conductivity of Si₁₋ₓGeₓ nanowires," *Appl. Phys. Lett.*, vol. 95, no. 7, 2009, Art. no. 073117.

[5] C. Blanc, A. Rajabpour, S. Volz, T. Fournier, and O. Bourgeois, "Phonon heat conduction in corrugated silicon nanowires below the Casimir limit," *Appl. Phys. Lett.*, vol. 103, no. 4, Jul. 2013, Art. no. 043109.

[6] T. C. Harman, "Quantum dot superlattice thermoelectric materials and devices," *Science*, vol. 297, no. 5590, pp. 2229-2232, Sep. 2002.

[7] G. D. Mahan, "Thermal conductivity of superlattices," in *Thermal Conductivity: Theory, Properties, and Applications*, T. M. Tritt, Ed. Boston, MA, USA: Springer, 2004, ch. 1.6, pp. 153-165.

[8] C.-K. Liu *et al.*, "Thermal conductivity of Si/SiGe superlattice films," *J. Appl. Phys.*, vol. 104, no. 11, Dec. 2008, Art. no. 114301.

[9] H. Mizuno, S. Mossa, and J.-L. Barrat, “Beating the amorphous limit in thermal conductivity by superlattices design,” *Sci. Rep.*, vol. 5, no. 1, p. 14116, Nov. 2015.

[10] P. Chakraborty, L. Cao, and Y. Wang, “Ultralow lattice thermal conduc- tivity of the random multilayer structure with lattice imperfections,” *Sci. Rep.*, vol. 7, no. 1, p. 8134, Dec. 2017.

[11] P. E. Hopkins *et al.*, “Reduction in the thermal conductivity of single crystalline silicon by phononic crystal patterning,” *Nano Lett.*, vol. 11, no. 1, pp. 107–112, Jan. 2011.

[12] N. Zen, T. A. Puurtinen, T. J. Isotalo, S. Chaudhuri, and I. J. Maasilta, “Engineering thermal conductance using a two-dimensional phononic crystal,” *Nature Commun.*, vol. 5, no. 1, p. 3435, May 2014.

[13] R. Anufriev and M. Nomura, “Thermal conductance boost in phononic crystal nanostructures,” *Phys. Rev. B, Condens. Matter*, vol. 91, no. 24, Jun. 2015, Art. no. 245417.

[14] S. Alaie, D. F. Goettler, M. Su, Z. C. Leseman, C. M. Reinke, and I. El-Kady, “Thermal transport in phononic crystals and the observation of coherent phonon scattering at room temperature,” *Nature Commun.*, vol. 6, no. 1, p. 7228, Nov. 2015.

[15] S. Gluchko, R. Anufriev, R. Yanagisawa, S. Volz, and M. Nomura, “On the reduction and rectification of thermal conduction using phononic crystals with pacman-shaped holes,” *Appl. Phys. Lett.*, vol. 114, no. 2, Jan. 2019, Art. no. 023102.

[16] P. Martin, Z. Aksamija, E. Pop, and U. Ravaioli, “Impact of phonon-surface roughness scattering on thermal conductivity of thin Si nanowires,” *Phys. Rev. Lett.*, vol. 102, no. 12, Mar. 2009, Art. no. 125503.

[17] T. Markussen, A.-P. Jauho, and M. Brandbyge, “Electron and phonon transport in silicon nanowires: Atomistic approach to thermoelectric properties,” *Phys. Rev. B, Condens. Matter*, vol. 79, no. 3, Jan. 2009, Art. no. 035415.

[18] M. Nomura, J. Nakagawa, Y. Kage, J. Maire, D. Moser, and O. Paul, “Thermal phonon transport in silicon nanowires and two-dimensional phononic crystal nanostructures,” *Appl. Phys. Lett.*, vol. 106, no. 14, Apr. 2015, Art. no. 143102.

[19] C. Jeong, R. Kim, M. Luisier, S. Datta, and M. Lundstrom, “On Landauer versus Boltzmann and full band versus effective mass evalu- ation of thermoelectric transport coefficients,” *J. Appl. Phys.*, vol. 107, no. 2, Jan. 2010, Art. no. 023707.

[20] C. Jeong, R. Kim, and M. S. Lundstrom, “On the best bandstructure for thermoelectric performance: A Landauer perspective,” *J. Appl. Phys.*, vol. 111, no. 11, Jun. 2012, Art. no. 113707.

[21] D. G. Cahill *et al.*, “Nanoscale thermal transport. II. 2003–2012,” *Appl. Phys. Rev.*, vol. 1, no. 1, 2014, Art. no. 011305.

[22] M.-Y. Lee, Y. Li, and S. Samukawa, “Miniband calculation of 3-D nanostructure array for solar cell applications,” *IEEE Trans. Electron Devices*, vol. 62, no. 11, pp. 3709–3714, Nov. 2015.

[23] W.-W. Zhang, H. Yu, S.-Y. Lei, and Q.-A. Huang, “Modelling of the elas- tic properties of crystalline silicon using lattice dynamics,” *J. Phys. D, Appl. Phys.*, vol. 44, no. 33, Aug. 2011, Art. no. 335401.

[24] F. Schaffler, “Silicon-germanium,” in *Properties of Advanced Semicon- ductor Materials: GaN, AlN, InN, BN, SiC, SiGe*, M. E. Levinshtein, S. L. Rumyantsev, and M. S. Shur, Eds. New York, NY, USA: Wiley, 2001, pp. 149–188.

[25] R. Landauer, “Spatial variation of currents and fields due to localized scatterers in metallic conduction,” *IBM J. Res. Develop.*, vol. 1, no. 3, pp. 223–231, Jul. 1957.

[26] S. Datta, *Electronic Transport in Mesoscopic Systems*. New York, NY, USA: Cambridge Univ. Press, 1997.

[27] J. Maassen and M. Lundstrom, “The Landauer approach to electron and phonon transport,” *ECS Trans.*, vol. 69, no. 9, pp. 23–36, 2015.

[28] C. Jeong, S. Datta, and M. Lundstrom, “Full dispersion versus Debye model evaluation of lattice thermal conductivity with a Landauer approach,” *J. Appl. Phys.*, vol. 109, no. 7, Apr. 2011, Art. no. 073718.

[29] C. Jeong, S. Datta, and M. Lundstrom, “Thermal conductivity of bulk and thin-film silicon: A Landauer approach,” *J. Appl. Phys.*, vol. 111, no. 9, May 2012, Art. no. 093708.

[30] A. J. H. McGaughey and A. Jain, “Nanostructure thermal conductivity prediction by Monte Carlo sampling of phonon free paths,” *Appl. Phys. Lett.*, vol. 100, no. 6, Feb. 2012, Art. no. 061911.

[31] C. Bera, N. Mingo, and S. Volz, “Marked effects of alloying on the thermal conductivity of nanoporous materials,” *Phys. Rev. Lett.*, vol. 104, no. 11, Mar. 2010, Art. no. 115502.

[32] P. Pereyra, “Why the effective-mass approximation works so well for nano-structures,” *Europhys. Lett.*, vol. 125, no. 2, p. 27003, 2019.

[33] F. Grosse, E. A. Muljarov, and R. Zimmermann, “Phonons in quantum dots and their role in exciton dephasing,” in *Semiconductor Nanostruc- tures*, M. E. Levinshtein, S. L. Rumyantsev, and M. S. Shur, Eds. Berlin, Germany: Springer, 2008, pp. 165–187.

[34] D. M. Wood and A. Zunger, “Successes and failures of the $\mathbf{k\cdot p}$ method: A direct assessment for GaAs/AlAs quantum structures,” *Phys. Rev. B, Condens. Matter*, vol. 53, no. 12, pp. 7949–7963, Mar. 1996.

[35] G. G. Guzmán-Verri and L. C. L. Y. Voon, “Electronic structure of silicon-based nanostructures,” *Phys. Rev. B, Condens. Matter*, vol. 76, no. 7, Aug. 2007, Art. no. 075131.

[36] M. Hosseini, A. Hadi, A. Malekshahi, and M. Shishesaz, “A review of size-dependent elasticity for nanostructures,” *J. Comput. Appl. Mech.*, vol. 49, no. 1, pp. 197–211, 2018.

[37] K. Choudhary, G. Cheon, E. Reed, and F. Tavazza, “Elastic properties of bulk and low-dimensional materials using van der Waals density functional,” *Phys. Rev. B, Condens. Matter*, vol. 98, no. 1, Jul. 2018, Art. no. 014107.

[38] F. Yang and C. Dames, “Mean free path spectra as a tool to understand thermal conductivity in bulk and nanostructures,” *Phys. Rev. B, Condens. Matter*, vol. 87, no. 3, Jan. 2013, Art. no. 035437.

[39] T. Hori, J. Shiomi, and C. Dames, “Effective phonon mean free path in polycrystalline nanostructures,” *Appl. Phys. Lett.*, vol. 106, no. 17, Apr. 2015, Art. no. 171901.