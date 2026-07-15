
# Lattice stability of ordered Au-Cu alloys in the warm dense matter regime

Shota Ono \( ^{*} \)  and Daigo Kobayashi

Department of Electrical, Electronic and Computer Engineering, Gifu University, Gifu 501-1193, Japan

In the warm dense regime, where the electron temperature is increased to the same order of the Fermi temperature, the dynamical stability of elemental metals depends on its electronic band structure as well as its crystal structure. It has been known that phonon hardening occurs due to an enhanced internal pressure caused by electron excitations as in close-packed simple metals, whereas phonon softening occurs at a specific point in the Brillouin zone as in body-centered cubic metals. Here, we investigate the dynamical stability of binary ordered alloys (Au and Cu) in the  \( L1_{0} \)  and  \( L1_{2} \)  structures. By performing first principles calculations on phonon dispersions, we demonstrate that warm dense Au-Cu systems show phonon hardening behavior except the lowest frequency phonon mode at point R of AuCu in the  \( L1_{0} \)  structure. We show that when a phonon mode is stabilized by long-range interatomic interactions at ambient condition, such a phonon will be destabilized by the short-range nature of the warm dense matters.

## I. INTRODUCTION

Lattice dynamics in metals is determined by the interplay between the direct ion-ion and the indirect ion-electron-ion interactions. In the warm dense matter (WDM) regime realized by an incident of ultrashort laser pulse to metals, the indirect interaction is strongly modulated due to electron excitations characterized by the electron temperature  \( T_{e} \)  that is the same order of the Fermi temperature. By using the finite-temperature density-functional theory (DFT) [1], the phonon hardening has been predicted for elemental metals in the close-packed (i.e., face-centered cubic (fcc) and hexagonal close-packed) structures [2–9]. For noble metals, this is because the excitation of d electrons weakens the electron screening, in turn, yielding an increase in the internal pressure [2, 3]. For free electron metals with no d bands near the Fermi level, the internal pressure increases with the electron kinetic energy, leading to the phonon hardening again [3]. Within the free-electron approximation using the central potential model, this is understood by an increase in the force constants of the first nearest neighbor (NN) sites [9]. In contrast, the phonon softening has been predicted for the body-centered cubic (bcc) structure [5, 7–10]. This is intrinsic to the crystal structure symmetry: in the expression for the phonon frequency at point N in the Brillouin zone, a relatively small contribution from the force constants of the first NN sites is present [9, 10]. These studies imply that the phonon hardening or softening properties in WDM are determined by a combined effect of the increase in the internal pressure (weakened screening) and the crystal structure symmetry. In order to study this interplay systematically, it is useful to focus on ordered alloys that can have many crystal structures in thermal equilibrium and phase diagram as a function of ambient temperature and composition.
The ordered phases of Au-Cu alloys have been well known as described in the standard textbooks [11]: AuCu in the  \( L1_{0} \)  structure (the distorted fcc structure along the c axis) and  \( AuCu_{3} \)  and  \( CuAu_{3} \)  in the  \( L1_{2} \)  structure [12], as shown in Fig. 1. In this paper, we study the lattice dynamics of ordered Au-Cu alloys in the WDM regime. We demonstrate that the warm dense Au-Cu alloy in the  \( L1_{2} \)  structure shows the phonon hardening, whereas that in the  \( L1_{0} \)  structure is unstable against the lowest frequency phonons at point R. The former can be explained by the weakening of the electron screening effect. To explain the latter, we show that the corresponding phonon mode at point R is stabilized by long-range interatomic interactions at ambient temperature due to the crystal structure symmetry and that the short-range nature of the warm dense matters destabilizes such a phonon mode.

The origin of the phonon softening in  \( L1_{0} \)  AuCu alloy is different from that in warm dense diamond and silicon. For the latter, the phonon softening and lattice instabilities have been understood by the strengthening of the anti-bonding character between atoms created by the electron transition from the valence to the conduction bands, reducing the size of force constants significantly [13]. Recently, Yan et al. have studied the dynamical stability of warm dense tantalum nitrides (TaN) in various structures [14] using finite-temperature DFT. They have shown that under electronic excitations the unstable cubic  \( \delta \) -phase becomes stable, whereas the hexagonal phases show the phonon softening. They have explained

![](./images/867745150900634415_1.jpg)

FIG. 1: Crystal structure of  \( CuAu_{3} \)  ( \( L1_{2} \) ),  \( AuCu \)  ( \( L10 \) ), and  \( AuCu_{3} \)  ( \( L1_{2} \) ).
 

it with respect to the covalent bonding between atoms in more complicated way.

This paper is organized as follows. Section II A describes computational details for the total energy and phonon dispersion calculations based on DFT and density-functional perturbation theory (DFPT). Section II B briefly explains the theory of lattice dynamics to provide analytical expressions for phonon frequencies at point R of AuCu in the  \( L1_{0} \)  structure. Section III first investigates the equilibrium and phonon properties of Au-Cu alloys by using different exchange-correlation functionals. The phonon dispersions of Au-Cu alloys in the WDM regime is next presented, followed by a consideration of the electron screening that explains the phonon hardening behaviors. The analytical expressions of phonon frequencies derived in Sec. II B will be systematically used to explain the phonon softening at point R of  \( L1_{0} \)  AuCu in the WDM regime. Also, nonthermal solid-to-solid transformation of  \( L1_{0} \)  AuCu is discussed. We conclude the paper in Sec. IV.

## II. THEORY

## A. Computational details

We calculate the total energy and the phonon dispersions of Au-Cu alloys based on DFT and DFPT [15] implemented in Quantum ESPRESSO (QE) code [16]. In order to treat the exchange-correlation energy, we use the Perdew-Zunger (PZ) [17] functional of the local density approximation and the Perdew-Burke-Ernzerhof (PBE) [18] functionals of the generalized gradient approximation. We use the ultrasoft pseudopotentials of Au.xc-nrkjus_psl.1.0.0.UPF and Cu.xc-dn-rrkjus_psl.1.0.0.UPF (xc = pz or pbe) that are provided in pslibrary.1.0.0 [19]. The cutoff energies for the wavefunction and the charge density are 80 Ry and 800 Ry, respectively. The self-consistent field and phonon dispersion calculations are performed by using  \( 16 \times 16 \times 1 \)  k grid and  \( 4 \times 4 \times 1 \)  q grid ( \( 3 \times 3 \times 1 \)  q grid for  \( L1_{2} \) ) [20], respectively, which are enough to study the dynamical stability of warm dense alloys. The total energy and forces are converged within  \( 10^{-5} \)  Ry and  \( 10^{-4} \)  a.u., respectively in geometry optimization. For phonon calculations, the threshold parameter for self-consistency (tr2_ph) is set to  \( 10^{-14} \) . The Marzari-Vanderbilt smearing [21] with a broadening of  \( \sigma = 0.02 \)  Ry (0.27 eV) is used for the geometry optimization, while the Fermi-Dirac type smearing is used for the WDM regime (the electron temperature  \( T_{e} \)  in units of eV and the Boltzmann constant  \( k_{B} = 1 \) ). The tetrahedron method is used to calculate the electron density-of-states (DOS) [22]. For the WDM regime, the number of electronic bands to be calculated is increased to more than three times larger the sizes in the ground state calculations in order to take into account the occupation of electronic states far above the Fermi level. Imaginary phonon energies  \( \hbar\omega \)  ( \( \hbar \)  the Planck constant and  \( \omega \)  the phonon frequency) are represented by negative energies below.

## B. Analytical expressions for phonon frequencies

Below is a brief description of the basic concepts for the lattice dynamics. We derive analytical expressions for the phonon frequencies at point R in order to study the instability of  \( L1_{0} \)  AuCu in detail. The atomic motion in a crystal is regulated by [23]

 \[ M_{\kappa}\frac{d^{2}u_{\kappa\alpha}(\boldsymbol{R}_{i})}{d t^{2}}=-\sum_{\kappa^{\prime}\beta j}D_{\alpha\kappa^{\prime}}^{\kappa\kappa^{\prime}}(\boldsymbol{R}_{i},\boldsymbol{R}_{j})u_{\kappa^{\prime}\beta}(\boldsymbol{R}_{j}), \quad (1) \] 

where  \( u_{\kappa\alpha}(\mathbf{R}_{i}) \)  is the displacement components for the atom  \( \kappa \)  (=1 and 2 for Au and Cu, respectively) along the direction of  \( \alpha \)  (= x, y, z) in the unit cell characterized by the lattice vector  \( \mathbf{R}_{i} = (R_{ix}, R_{iy}, R_{iz}) \)  expanded by the primitive vectors  \( \mathbf{a}_{1} = (a, 0, 0) \) ,  \( \mathbf{a}_{2} = (0, a, 0) \) , and  \( \mathbf{a}_{3} = (0, 0, c) \) .  \( M_{\kappa} \)  is the mass of the atom  \( \kappa \)  and  \( D_{\alpha\kappa'}^{\kappa\kappa'}(\mathbf{R}_{i}, \mathbf{R}_{j}) \)  is the force constant matrix defined as

 \[ D_{\alpha\beta}^{\kappa\kappa^{\prime}}(\boldsymbol{R}_{i},\boldsymbol{R}_{j})=\frac{\partial^{2}V}{\partial X_{\kappa\alpha}(\boldsymbol{R}_{i})\partial X_{\kappa^{\prime}\beta}(\boldsymbol{R}_{j})}\bigg|_{0}, \quad (2) \] 

where  \( X_{\kappa\alpha}(\boldsymbol{R}_{i}) = R_{i\alpha} + \tau_{\kappa\alpha} \)  and  \( \tau_{\kappa\alpha}\rangle \)  is the  \( \alpha \) -component of the basis vector for  \( \kappa \) :  \( (\tau_{1x}, \tau_{1y}, \tau_{1z}) = (0, 0, 0) \)  and  \( (\tau_{2x}, \tau_{2y}, \tau_{2z}) = (a/2, a/2, c/2) \) . Assuming the plane wave solution with the wavevector q, one obtains the eigenvalue equation

 \[ \omega^{2}\epsilon_{\kappa\alpha}(q)=\sum_{\kappa^{\prime}\beta}\tilde{D}_{\alpha\beta}^{\kappa\kappa^{\prime}}(q)\epsilon_{\kappa^{\prime}\beta}(q), \quad (3) \] 

where  \( \epsilon_{\kappa\alpha} \)  is the  \( \alpha \) -component of the polarization vector of the atom  \( \kappa \) , and using the translational symmetry of the crystal, the dynamical matrix  \( \tilde{D} \)  is given by

 \[ \tilde{D}_{\alpha\beta}^{\kappa\kappa^{\prime}}(q)=\frac{1}{\sqrt{M_{\kappa}M_{\kappa^{\prime}}}}\sum_{j}D_{\alpha\beta}^{\kappa\kappa^{\prime}}(\boldsymbol{R}_{j})e^{-i q\cdot\boldsymbol{R}_{j}}, \quad (4) \] 

where we used the notation of  \( D_{\alpha\beta}^{\kappa\kappa^{\prime}}(\boldsymbol{R}_{j}) = D_{\alpha\beta}^{\kappa\kappa^{\prime}}(\boldsymbol{R}_{j}, \boldsymbol{0}) \) . Also, due to the translational symmetry, the acoustic sum rule holds:  \( \sum_{\kappa^{\prime},j} D_{\beta\kappa^{\prime}}^{\beta\kappa}(\boldsymbol{R}_{j}) = 0 \) .

We consider the force constants up to the fifth-order NN sites of  \( L1_{0} \)  AuCu: for the Au atom at the origin, the position of the first, second, third, fourth, and fifth NNs are  \( \mathrm{Cu}(a/2, a/2, c/2) \) ,  \( \mathrm{Au}(a, 0, 0) \) ,  \( \mathrm{Au}(0, 0, c) \) ,  \( \mathrm{Au}(a, 0, c) \) , and  \( \mathrm{Cu}(3a/2, a/2, c/2) \) , respectively, and these equivalent sites. The  \( 6 \times 6 \)  dynamical matrix is then expressed as

 \[ \tilde{D}(\boldsymbol{q})=\left(\begin{array}{c c}{\tilde{D}^{11}(\boldsymbol{q})}&{\tilde{D}^{12}(\boldsymbol{q})}\\ {\tilde{D}^{21}(\boldsymbol{q})}&{\tilde{D}^{22}(\boldsymbol{q})}\\ \end{array}\right), \quad (5) \] 

where the  \( 3 \times 3 \)  diagonal matrix is given by

 \[ \tilde{D}^{\kappa\kappa}(\boldsymbol{q})=\left(\begin{array}{c c c}{\tilde{D}_{\kappa\kappa}^{\kappa\kappa}(\boldsymbol{q})}&{0}&{0}\\ {0}&{\tilde{D}_{\gamma\gamma}^{\kappa\kappa}(\boldsymbol{q})}&{0}\\ {0}&{0}&{\tilde{D}_{\kappa z}^{\kappa z}(\boldsymbol{q})}\\ \end{array}\right) \quad (6) \]
 

and the  \( 3 \times 3 \)  off-diagonal matrix for  \( \kappa \neq \kappa' \)  is given by

 \[ \tilde{D}^{\kappa\kappa^{\prime}}(\boldsymbol{q})=\left(\begin{array}{c c c}{0}&{0}&{0}\\ {0}&{0}&{\tilde{D}_{y y}^{\kappa\kappa^{\prime}}(\boldsymbol{q})}\\ {0}&{\tilde{D}_{z y}^{\kappa\kappa^{\prime}}(\boldsymbol{q})}&{0}\\ \end{array}\right). \quad (7) \] 

By solving Eq. (3), one obtains the phonon energies at point R in ascending order

 \[ \begin{aligned}\omega_{1}^{2}&=\frac{1}{2}\left[\tilde{D}_{zz}^{11}(\boldsymbol{q})+\tilde{D}_{yy}^{22}(\boldsymbol{q})-\tilde{C}_{zy}(\boldsymbol{q})\right],\\\omega_{II}^{2}&=\tilde{D}_{xx}^{11}(\boldsymbol{q}),\\\omega_{III}^{2}&=\frac{1}{2}\left[\tilde{D}_{yy}^{11}(\boldsymbol{q})+\tilde{D}_{zz}^{22}(\boldsymbol{q})-\tilde{C}_{yz}(\boldsymbol{q})\right],\\\omega_{IV}^{2}&=\tilde{D}_{xx}^{22}(\boldsymbol{q}),\\\omega_{V}^{2}&=\frac{1}{2}\left[\tilde{D}_{zz}^{11}(\boldsymbol{q})+\tilde{D}_{yy}^{22}(\boldsymbol{q})+\widetilde{C}_{zy}(\boldsymbol{q})\right],\\\omega_{VI}^{2}&=\frac{1}{2}\left[\tilde{D}_{yy}^{11}(\boldsymbol{q})+\tilde{D}_{zz}^{22}(\boldsymbol{q})+\widetilde{C}_{yz}(\boldsymbol{q})\right]\end{aligned} \quad (8) \] 

with

 \[ \tilde{C}_{\alpha\beta}(\boldsymbol{q})=\sqrt{\left[\tilde{D}_{\alpha\alpha}^{11}(\boldsymbol{q})-\tilde{D}_{\beta\beta}^{22}(\boldsymbol{q})\right]^{2}+4\left[\tilde{D}_{\alpha\beta}^{12}(\boldsymbol{q})\right]^{2}}. \quad (9) \] 

Based on these expressions for  \( \omega_{k} \)  ( \( k = I \cdots VI \) ), we interpret the lattice vibrations as follows: the vibration of the Au (Cu) atoms polarized to the x direction propagates along the  \( \boldsymbol{q} = (0, \pi/a, \pi/c) \)  direction with the frequency  \( \omega_{\mathrm{II}} \)  ( \( \omega_{\mathrm{VV}} \) ); the vibration of the Au atoms polarized to the z direction is coupled with the vibration of the Cu atoms polarized to the y direction, yielding  \( \omega_{I} \)  and  \( \omega_{V} \) ; and the vibration of the Au atoms polarized to the y direction is coupled with the vibration of the Cu atoms polarized to the z direction, yielding  \( \omega_{III} \)  and  \( \omega_{VI} \) . Due to the mode mixing, a frequency gap must be present between  \( \omega_{I} \)  and  \( \omega_{V} \)  ( \( \omega_{III} \)  and  \( \omega_{VI} \) ). Negative value in the expression of  \( \omega_{I}^{2} \)  (i.e.,  \( -\tilde{C}_{zy}(\boldsymbol{q}) \) ) will be responsible for the instability of  \( L1_{0} \)  AuCu in the WDM regime. The expressions of  \( \tilde{D}_{\alpha\beta}^{\kappa\kappa^{\prime}}(\boldsymbol{q}) \)  as a function of  \( D_{\alpha\beta}^{\kappa\kappa^{\prime}}(\boldsymbol{R}_{j}) \)  are provided in the Appendix A. The values of  \( D_{\alpha\beta}^{\kappa\kappa^{\prime}}(\boldsymbol{R}_{j}) \)  are extracted from DFPT calculations described in Sec. II A.

## III. RESULTS AND DISCUSSION

## A. Functional dependence

It has been known that the cohesive energies and bulk moduli of alloys may be sensitive to the exchange-correlation functionals used [24–27]. In general, the PBE functional underestimates those values for weakly bonded systems such as Au-Cu alloys. Such a discrepancy can be improved by using the hybrid exchange-correlation functional [24] or the random phase approximation [26]. For more accuracy, it may be better to use the latter approaches [24, 26]. However, we use the standard functionals described above to reduce the computational costs in phonon dispersion calculations.

For studying numerical accuracy in the present calculations, we list the optimized lattice parameters a and c (only for  \( L1_{0} \) ) predicted by using PZ and PBE functionals in Table I. These values obtained at  \( T_{e} = 0 \)  agree with the experimental values [12]: The mean absolute error (MAE) is estimated to be less than 0.1 Å for both cases. For Au-rich phases the PZ results are in good agreement with the experimental lattice constants, while for Cu-rich phases the PBE results are better.

Figure 2 shows the phonon dispersions along the symmetry lines for Au-Cu systems: (a) fcc Au, (b) fcc Cu, (c)  \( L1_{0} \)  AuCu, (d)  \( L1z \)  CuAu \( _{3} \) , and (e)  \( L1z \)  AuCu \( _{3} \) . Overall, the values of  \( \omega \) s calculated by using the PBE functional seem to be smaller than those calculated by using the PZ. For simple metals, the PZ and PBE results agree with the experiments of Au [28] and Cu [29], respectively. This tendency is similar to the previous calculations [30]. For AuCu the lowest  \( \omega \)  at point R is sensitive to the functional used:  \( \hbar\omega = -2.3 \)  and 1.8 meV for PZ and PBE, respectively. For CuAu \( _{3} \)  the phonon softening at the point M is observed. For AuCu \( _{3} \) , the agreement between the calculated and experimental curves [31] is good when the PBE functional is used. Below we will use the PBE functional to study the dynamical stability of AuCu in detail.

## B. Phonons in the WDM regime

Figure 3 shows the phonon dispersion curves of (a) Au, (b) Cu, (c) AuCu, (d) CuAu \( _{3} \) , and (e) AuCu \( _{3} \)  in the WDM regime, where  \( T_{e} \)  is set to 0, 4, and 6 eV. For both simple metals (Au and Cu), the phonon energy increases monotonically (i.e., phonon hardening) with  \( T_{e} \) , which is consistent with the previous calculations [2, 7]. For CuAu \( _{3} \)  and AuCu \( _{3} \) , in the L1 \( _{2} \)  structure, the phonon hardening behaviors are also observed when  \( T_{e} \)  is increased, while nonmonotonic increases are

TABLE I: Lattice parameters (a and c in units of Å) of Au-Cu alloys for different functionals. The experimental values are extracted from Ref. [12].

<table><tr><td></td><td>PZ</td><td>PBE</td><td>Experiment</td></tr><tr><td>Au</td><td>4.06</td><td>4.16</td><td>4.08</td></tr><tr><td>CuAu3</td><td>3.95</td><td>4.05</td><td>3.95</td></tr><tr><td>AuCu (a)</td><td>2.80</td><td>2.88</td><td>2.85</td></tr><tr><td>AuCu (c)</td><td>3.54</td><td>3.64</td><td>3.67</td></tr><tr><td>AuCu3</td><td>3.68</td><td>3.79</td><td>3.74</td></tr><tr><td>Cu</td><td>3.53</td><td>3.63</td><td>3.62</td></tr><tr><td>MAE</td><td>0.060</td><td>0.051</td><td></td></tr></table>
 
![](./images/867745150900634415_2.jpg)

![](./images/867745150900634415_3.jpg)

![](./images/867745150900634415_4.jpg)

![](./images/867745150900634415_5.jpg)

![](./images/867745150900634415_6.jpg)

![](./images/867745150900634415_7.jpg)

FIG. 2: The phonon dispersions of (a) Au, (b) Cu, (c) AuCu, (d) CuAu \( _{3} \) , and (e) AuCu \( _{3} \)  calculated with the PZ and PBE functionals. The experimental data (circles) for (a), (b), and (e) are taken from Refs. [28], [29], and [31], respectively.

observed along the line of M-R for the transverse acoustic phonon branch. As shown in Fig. 3(c),  \( L1_{0} \)  AuCu becomes unstable against  \( T_{e} \) . While the optical phonons are hardened significantly, the transverse acoustic mode is unstable because around point R the phonon energy is imaginary.

In general, the phonon hardening is attributed to an increase in the internal pressure caused by weakened electron screening. When the screening effect is weakened, bared ions are created, leading to a peak shift and a shrinkage of the width in the electron energy spectrum. This has been illustrated by the electron DOS as a function of  \( T_{e} \)  [2]. Figure 4 shows the DOS of Au-Cu alloys for several  \( T_{e} \) s. At  \( T_{e}=0 \) , due to the presence of d bands, the high DOS is observed below the Fermi level from -2 to -7 eV, while the band width is narrow in Cu (from -2 to -5 eV). When  \( T_{e} \)  is increased, the peak position and the width become deep and small, respectively, as

![](./images/867745150900634415_8.jpg)

![](./images/867745150900634415_9.jpg)

![](./images/867745150900634415_10.jpg)

![](./images/867745150900634415_11.jpg)

![](./images/867745150900634415_12.jpg)

FIG. 3: The phonon dispersions of (a) Au, (b) Cu, (c) AuCu, (d) CuAu \( _{3} \) , and (e) AuCu \( _{3} \)  for  \( k_{B}T_{e} = 0, 4 \) , and 6 eV. The PBE functional is used.

described above. Although the variation of DOS with  \( T_{e} \)  may be correlated with the phonon hardening of Au, Cu, CuAu \( _{3} \) , and AuCu \( _{3} \)  it never explains the phonon softening observed in L1 \( _{0} \)  AuCu.

To understand the anomalous softening of AuCu in the WDM regime, let us remind that the ion-ion interac-

TABLE II: Phonon energies (in units of meV) at point R in L1₀ AuCu at  \( T_{e} = 0 \)  eV for different models.

<table><tr><td></td><td>1NN</td><td>2NN</td><td>3NN</td><td>4NN</td><td>5NN</td><td>DFPT</td></tr><tr><td>\( \omega_{\mathrm{I}} \)</td><td>-6.1</td><td>-5.6</td><td>-4.4</td><td>-3.2</td><td>0.5</td><td>1.8</td></tr><tr><td>\( \omega_{\mathrm{II}} \)</td><td>8.0</td><td>6.4</td><td>6.2</td><td>6.6</td><td>7.2</td><td>8.5</td></tr><tr><td>\( \omega_{\mathrm{III}} \)</td><td>-6.9</td><td>9.8</td><td>10.2</td><td>10.4</td><td>10.9</td><td>11.5</td></tr><tr><td>\( \omega_{\mathrm{IV}} \)</td><td>14.0</td><td>13.2</td><td>13.0</td><td>13,4</td><td>14.3</td><td>15.1</td></tr><tr><td>\( \omega_{\mathrm{V}} \)</td><td>19.0</td><td>19.8</td><td>19.9</td><td>20.1</td><td>20.5</td><td>21.0</td></tr><tr><td>\( \omega_{\mathrm{VI}} \)</td><td>22.3</td><td>23.2</td><td>23.6</td><td>23.7</td><td>24.0</td><td>24.2</td></tr></table>
 
![](./images/867745150900634415_13.jpg)

FIG. 4: The electron DOS for Au, CuAu \( _{3} \) , AuCu, AuCu \( _{3} \)  and Cu for  \( k_{B}T_{e} = 0.4 \) , and 6 eV. The electron energy is measured from the Fermi level.

tions are decomposed into the direct and indirect parts: the former is the repulsive Coulomb interaction that is independent of the magnitude of  \( T_{e} \) , while the latter is the electron-mediated attractive interaction that is significantly modified in the WDM regime. At ambient condition, the former and the latter may be partly canceled with each other, producing the repulsive and attractive

TABLE III: Same as Table II but for WDM regime at  \( T_{e} = 4 \)  eV.

<table><tr><td></td><td>1NN</td><td>2NN</td><td>3NN</td><td>4NN</td><td>5NN</td><td>DFPT</td></tr><tr><td>\( \omega_{\mathrm{I}} \)</td><td>-12.9</td><td>-8.5</td><td>-5.8</td><td>-5.7</td><td>-5.6</td><td>-5.1</td></tr><tr><td>\( \omega_{\mathrm{II}} \)</td><td>11.0</td><td>8.3</td><td>8.1</td><td>8.2</td><td>8.3</td><td>9.1</td></tr><tr><td>\( \omega_{\mathrm{III}} \)</td><td>-11.4</td><td>11.1</td><td>12.1</td><td>12,2</td><td>12.4</td><td>12.8</td></tr><tr><td>\( \omega_{\mathrm{IV}} \)</td><td>19.3</td><td>17.6</td><td>17.5</td><td>17.6</td><td>18.5</td><td></td></tr><tr><td>\( \omega_{\mathrm{V}} \)</td><td>28.0</td><td>31.8</td><td>32.0</td><td>32.0</td><td>31,2</td><td>32.3</td></tr><tr><td>\( \omega_{\mathrm{VI}} \)</td><td>31.9</td><td>33.0</td><td>33.6</td><td>33.7</td><td>33.7</td><td></td></tr></table>

interactions for the short- and long-range parts, respectively. Given small indirect contribution, the repulsive Coulomb forces are dominant for the short-range part. On the other hand, for the long-range part, the attractive forces compete with the repulsive forces, creating relatively small interaction forces. This situation is exactly realized in WDMs. We thus hypothesize that the lowest energy mode at point R of  \( L1_{0} \)  AuCu is stabilized by the long-range interaction between atoms at  \( T_{e} = 0 \)  eV. With this assumption, it is reasonable to observe the softening of the phonon mode when  \( L1_{0} \)  AuCu is in the WDM regime having weakened long-range interatomic interactions. Similarly, we can expect that when a phonon mode is stabilized by only the short-range interactions, such a mode will show hardening behavior in the WDM regime.

To demonstrate this concept, we list the values of  \( \omega_{k} \)  in Eq. (8) for several models accounting for up to the p-th NN interactions (pNN models) in Table II. As p increases, the phonons at point R are stabilized and their energies approach the DFPT results. It is noteworthy that the sizes of  \( \omega_{V} \)  and  \( \omega_{VI} \)  within the 1NN model are almost comparable to those within DFPT. This means that the optical phonon energies are well determined by only the short-range interaction between atoms. When the interatomic interactions are considered up to the second order NN,  \( \omega_{III} \)  becomes positive. However,  \( \omega_{\mathrm{I}} \)  is positive only within 5NN and DFPT. This implies that the long-range forces between Au and Cu atoms are important to yield positive  \( \omega_{\mathrm{I}} \) , i.e., the dynamical stability of  \( L1_{0} \)  AuCu. Table III also lists the values of  \( \omega_{k} \)  but for  \( T_{e} = 4 \)  eV. As in Table II,  \( \omega_{k} \)  approaches the DFPT results with the inclusion of higher order NN interactions. Again, the sizes of  \( \omega_{V} \)  and  \( \omega_{VI} \)  within the 1NN model almost agree with those within DFPT, indicating that the optical phonon hardening is due to an enhanced short-range forces. The most important fact is that the convergence of  \( \omega_{I} \)  is fast compared to the case of  \( T_{e} = 0 \)  eV:  \( \omega_{I} = -5.8 \)  meV within 3NN is already similar to -5.1 meV within DFPT. This reflects the short-range nature of WDM, leading to the instability of the  \( \omega_{I} \)  mode.

## C. Solid-to-solid transformation

The stability of AuCu in the  \( L1_{0} \)  structure can also be understood by calculating the free-energy as a function of the ratio c/a with the equilibrium volume  \( V = V_{0} \)  fixed (i.e., along the Bain path [32]): c/a = 1 and  \( \sqrt{2} \)  correspond to the bcc (or B2) and fcc structures, respectively. Figure 5(a) shows the c/a-dependence of the free-energy of AuCu for several  \( T_{e} \) s, where  \( V = V_{0} \)  is the equilibrium volume of  \( L1_{0} \)  at  \( T_{e} = 0 \)  eV. At  \( T_{e}=0 \)  eV, the free energy takes minimum values at c/a = 1.26 ( \( L1_{0} \) ) and 0.9, whereas that takes a maximum value at c/a = 1 (B2). As expected, AuCu in the B2 structure is dynamically unstable (see Fig. 5(b) (blue)). When  \( T_{e} \)  is increased, the profile of such a double-well-like curve is modified, indicating a non-thermal solid-to-solid transformation, as
 
![](./images/867745150900634415_14.jpg)

![](./images/867745150900634415_15.jpg)

FIG. 5: (a) The free-energy of L1o AuCu along the Bain path for different  \( T_{e} \) s. The free-energy is measured from the minimum value along c/a with  \( T_{e} \)  fixed. (b) The phonon dispersion curves of AuCu with c/a = 1 (i.e., B2) for  \( T_{e} = 0 \)  and 4 eV.

discussed in warm dense tungsten [5]. At  \( T_{e} = 2.5 \)  eV, the free-energy minimum at smaller c/a vanishes, while that at larger c/a shifts to c/a  \( \simeq 1.22 \) ; at  \( T_{e} = 3 \)  eV, the free-energy curve becomes relatively flat in the region of  \( c/a \in [1.0, 1.2] \)  and takes a minimum only at c/a = 1; and at higher  \( T_{e} \) s, the curvature around c/a = 1 becomes larger, stabilizing the B2 phase. Such a B2 structure is found to be dynamically stable, as shown in Fig. 5(b) (orange), where  \( T_{e} = 4 \)  eV is assumed. We hope that our prediction for the phase transformation in AuCu, before melting occurs, can be confirmed by future experiments.

## IV. CONCLUSIONS

In conclusion, we have studied the dynamical stability of Au-Cu alloys in the WDM regime by calculating the phonon dispersion curves. The phonon hardening is observed in the  \( L1_{2} \)  and  \( L1_{0} \)  structures except the lowest frequency phonon at point R of  \( L1_{0} \)  AuCu. The hardening behavior can be explained by the increase in the internal pressure caused by the d electron excitations, as observed in noble metals. The phonon softening observed is attributed to the short-range nature of WDMs because the lowest frequency phonon at point R is stabilized by long-range interactions between Au and Cu.

Although we have used analytical expressions of Eq. (8) to understand the phonon softening of  \( L1_{0} \)  AuCu, those can be applicable to other ordered alloys in the  \( L1_{0} \)  and B2 (the case of c = a) structures. It is valuable to note that  \( 51~L1_{0} \)  and  \( 325~B2 \)  alloys are found in experimental phase diagrams [33]. More investigations will lead to a deep understanding of the dynamical stability of ordered alloys.

Finally, it should be noted that the WDM is a transient phase because the excited electron energy created by a laser pulse is transferred to phonons, leading to lattice disordering or melting within a few picoseconds [34–39]. Although the phonon hardening of warm dense Au has been reported experimentally [40], its validity has been controversial [34, 38, 39]. It is thus desirable to simulate the time-evolution of lattice displacements in warm dense alloys accurately, which enables us to interpret time-resolved experiments.

## Acknowledgments

A part of numerical calculations has been done using the facilities of the Supercomputer Center, the Institute for Solid State Physics, the University of Tokyo.

## Appendix A: Dynamical matrix

The expressions of  \( \tilde{D}_{\alpha\alpha}^{\kappa\kappa^{\prime}}(\boldsymbol{q}) \)  used in the pNN model calculations are given below. The symmetry properties for the force constants [23] are used to simplify the expression of Eq. (4). For the  \( L1_{0} \)  structure, there are 16 symmetry operations including the identity, 180 degree rotation around x, y, z, and  \( [1,\pm1,0] \)  axis,  \( \pm90 \)  degree rotation around z axis, and the inversions. The list of the force constants obtained from DFPT calculations is used to check the restrictions imposed. We introduce the step function  \( U(x) \)  that takes 1 and 0 for  \( x \geq 0 \)  and x < 0, respectively. We obtain for  \( \alpha = x \)  and y,

 \[ \begin{aligned}&M_{\kappa}\tilde{D}_{\alpha\alpha}^{\kappa\kappa}(\boldsymbol{q})\\=&D_{\alpha\alpha}^{\kappa\κ}(\boldsymbol{0})U(p-1)\\&+2\left[D_{\alpha\alpha}^{\kappa\κ}(\boldsymbol{a}_{1})-D_{\alpha\alpha}^{\kappaκ}(\boldsymbol{a}_{{1}})-D_{\alpha\alpha}^{\κκ}(\boldsymbol{a}_{1})\right]U(p-2)\\&+4\left[-D_{\alpha\alpha}^{\κκ}(\boldsymbol{a}_{{1}}+\boldsymbol{a}_{3})+D_{\alpha\alpha}^{\κκ}(\boldsymbol{a}_{{2}}+\boldsymbol{a}_{3})\right]U(p-4),\\ \end{aligned} \quad (A1) \] 

and for  \( \alpha = z \) ,

 \[ \begin{align*}M_{\kappa}\tilde{D}_{\alpha\alpha}^{\kappa\kappa}(\boldsymbol{q})~&=~D_{\kappa\kappa}^{\kappa\kappa}(\boldsymbol{0})U(p-1)\\~&-2D_{\alpha\alpha}^{\kappa\kappa}(\boldsymbol{a}_{3})U(p-3).\end{align*} \quad (A2) \] 

The nonzero elements in the off-diagonal matrix for  \( (\alpha\beta) = (yz) \)  and  \( (zy) \)  are

 \[ \begin{aligned}&\sqrt{M_{1}M_{2}}\tilde{D}_{\alpha\beta}^{12}(\boldsymbol{q})\\=&8D_{\alpha\beta}^{12}(\mathbf{0})U(p-1)\\&+8\left[D_{\alpha\beta}^{12}(\mathbf{2}\boldsymbol{a}_{1})+D_{\alpha\beta}^{12}(\mathbf{2}\boldsymbol{a}_{2})\right]U(p-5).\end{aligned} \quad (A3) \]
 

The dynamical matrix is symmetric because of the relation  \( \tilde{D}_{\beta\alpha}^{21}(\boldsymbol{q})=\tilde{D}_{\alpha\beta}^{12}(\boldsymbol{q}) \) . The acoustic sum rule deter-

[1] N. D. Mermin, Thermal properties of the inhomogeneous electron gas, Phys. Rev. 137, A1441 (1965).

[2] V. Recoules, J. Clérouin, G. Zerah, P. M. Anglade, and S. Mazevet, Effect of Intense Laser Irradiation on the Lattice Stability of Semiconductors and Metals, Phys. Rev. Lett. 96, 055503 (2006).

[3] F. Bottin and G. Zerah, Formation enthalpies of monovacancies in aluminum and gold under the condition of intense laser irradiation, Phys. Rev. B 75, 174114 (2007).

[4] F. C. Kabeer, E. S. Zijlstra, and M. E. Garcia, Road of warm dense noble metals to the plasma state: Ab initio theory of the ultrafast structural dynamics in warm dense matter, Phys. Rev. B 89, 100301(R) (2014).

[5] Y. Giret, S. L. Daraszewicz, D. M. Duffy, A. L. Shluger, and K. Tanimura, Nonthermal solid-to-solid phase transitions in tungsten, Phys. Rev. B 90, 094103 (2014).

[6] D. V. Minakov and P. R. Levashov, Melting curves of metals with excited electrons in the quasiharmonic approximation, Phys. Rev. B 92, 224102 (2015).

[7] G. Q. Yan, X. L. Cheng, H. Zhang, Z. Y. Zhu, and D. H. Ren, Different effects of electronic excitation on metals and semiconductors, Phys. Rev. B 93, 214302 (2016).

[8] L. Harbour, M. W. C. Dharma-wardana, D. D. Klug, and L. J. Lewis, Equation of state, phonons, and lattice stability of ultrafast warm dense matter, Phys. Rev. E 95, 043201 (2017).

[9] S. Ono, Lattice dynamics for isochorically heated metals: A model study, J. Appl. Phys. 126, 075113 (2019).

[10] S. Ono and D. Kobayashi, Phonon softening in sodium with a stepwise electron distribution, J. Appl. Phys. 127, 165105 (2020).

[11] C. Kittel, Introduction to Solid State Physics, 8th edition (Wiley, Hoboken, NJ, 2005).

[12] H. Okamoto, D. J. Chakrabarti, D. E. Laughlin, and T. B. Massalski, The Au-Cu (Gold-Copper) System, J. Phase Equilib. 8, 454 (1987).

[13] P. Stampfli and K. H. Bennemann, Theory for the instability of the diamond structure of Si, Ge, and C induced by a dense electron-hole plasma, Phys. Rev. B 42, 7163 (1990).

[14] G. Q. Yan, X. L. Cheng, and H. Zhang, Phase stability and mechanical response of tantalum nitrides to electronic excitation effect, Mater. Res. Express 7, 066508 (2020).

[15] S. Baroni, S. Gironcoli, A. D. Corso, and P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory, Rev. Mod. Phys. 73, 515 (2001).

[16] P. Giannozzi et al., Advanced capabilities for materials modeling with Quantum ESPRESSO, J. Phys.: Condens. Matter 29, 465901 (2017).

[17] J. P. Perdew and A. Zunger, Self-interaction correction to density-functional approximations for many-electron systems, Phys. Rev. B 23, 5048 (1981).

[18] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996).

mines  \( D_{\alpha\alpha}^{\kappa\kappa}(\mathbf{0}) \)  in Eqs. (A1) and (A2), depending on the model used.

[19] A. Dal Corso, Pseudopotentials periodic table: From H to Pu, Computational Material Science 95, 337 (2014).

[20] H. J. Monkhorst and J. D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13, 5188 (1976).

[21] N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Thermal Contraction and Disordering of the Al(110) Surface, Phys. Rev. Lett. 82, 3296 (1999).

[22] P. E. Blöchl, O. Jepsen, and O. K. Andersen, Improved tetrahedron method for Brillouin-zone integrations, Phys. Rev. B 49, 16223 (1994).

[23] A. Maradudin, Theory of Lattice Dynamics in the Harmonic Approximation (Academic Press, New York, 1971).

[24] Y. Zhang, G. Kresse, and C. Wolverton, Nonlocal First-Principles Calculations in Cu-Au and Other Intermetallic Alloys, Phys. Rev. Lett. 112, 075502 (2014).

[25] E. B. Isaacs and C. Wolverton, Performance of the strongly constrained and appropriately normed density functional for solid-state materials, Phys. Rev. Materials 2, 063801 (2018).

[26] N. K. Nepal, S. Adhikari, J. E. Bates, and A. Ruzsinszky, Treating different bonding situations: Revisiting Au-Cu alloys using the random phase approximation, Phys. Rev. B 100, 045135 (2019).

[27] N. K. Nepal, S. Adhikari, B. Neupane, and A. Ruzsinszky, Formation energy puzzle in intermetallic alloys: Random phase approximation fails to predict accurate formation energies, Phys. Rev. B 102, 205121 (2020).

[28] J. W. Lynn, H. G. Smith, and R. M. Nicklow, Lattice Dynamics of Gold, Phys. Rev. B 8, 3493 (1973).

[29] R. M. Nicklow, G. Gilat, H. G. Smith, L. J. Raubenheimer, and M. K. Wilkinson, Phonon Frequencies in Copper at 49 and 298°K, Phys. Rev. 164, 922 (1967).

[30] X. Tang and B. Fultz, First-principles study of phonon linewidths in noble metals, Phys. Rev. B 84, 054303 (2011).

[31] S. Katano, M. Izumi, and Y. Noda, Lattice dynamics of  \( Cu_{3}Au \)  in the ordered and disordered states, J. Phys. F: Met. Phys. 18, 2195 (1988).

[32] G. Grimvall, B. Magyar-Köpe, V. Ozoliš, and K. A. Persson, Lattice instabilities in metallic elements, Rev. Mod. Phys. 84, 945 (2012).

[33] M. Sluiter, Some observed bcc, fcc, and hcp superstructures, Phase Transitions 80, 299 (2007).

[34] S. L. Daraszewicz, Y. Giret, N. Naruse, Y. Murooka, J. Yang, D. M. Duffy, A. L. Shluger, and K. Tanimura, Structural dynamics of laser-irradiated gold nanofilms, Phys. Rev. B 88, 184101 (2013).

[35] B. I. Cho, T. Ogitsu, K. Engelhorn, A. A. Correa, Y. Ping, J. W. Lee, L. J. Bae, D. Prendergast, R. W. Falcone, and P. A. Heimann, Measurement of electron-ion relaxation in warm dense copper, Sci. Rep. 6, 18843 (2016).

[36] N. Jourdain, L. Lecherbourg, V. Recoules, P. Renaudin, and F. Dorchies, Electron-ion thermal equilibration dynamics in femtosecond heated warm dense copper, Phys.
 

Rev. B 97, 075148 (2018).

[37] M. Z. Mo, Z. Chen, R. K. Li, M. Dunning, B. B. L. Witte, J. K. Baldwin, L. B. Fletcher, J. B. Kim, A. Ng, R. Redmer, A. H. Reid, P. Shekhar, X. Z. Shen, M. Shen, K. Sokolowski-Tinten, Y. Y. Tsui, Y. Q. Wang, Q. Zheng, X. J. Wang, and S. H. Glenzer, Heterogeneous to homogeneous melting transition visualized with ultrafast electron diffraction, Science 360, 1451 (2018).

[38] N. A. Smirnov, Copper, gold, and platinum under femtosecond irradiation: Results of first-principles calculations, Phys. Rev. B 101, 094103 (2020).

[39] N. Jourdain, L. Lecherbourg, V. Recoules, P. Renaudin, and F. Dorchies, Ultrafast Thermal Melting in Nonequilibrium Warm Dense Copper, Phys. Rev. Lett. 126, 065001 (2021).

[40] R. Ernstorfer, M. Harb, C. T. Hebeisen, G. Sciaini, T. Dartigalongue, and R. J. D. Miller, The Formation of Warm Dense Matter: Experimental Evidence for Electronic Bond Hardening in Gold, Science 323, 1033 (2009).
 
