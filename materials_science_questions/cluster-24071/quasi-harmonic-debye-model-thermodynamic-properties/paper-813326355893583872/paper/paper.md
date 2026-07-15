# Thermodynamic properties of magnesium oxide: a comparison of *ab initio* and empirical models

This article has been downloaded from IOPscience. Please scroll down to see the full text article.

2012 Phys. Scr. 85 045702

(http://iopscience.iop.org/1402-4896/85/4/045702)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:
IP Address: 138.87.11.21
The article was downloaded on 05/11/2012 at 11:11

Please note that [terms and conditions apply].

# Thermodynamic properties of magnesium oxide: a comparison of *ab initio* and empirical models

Ting Song¹, Xiao-Wei Sun¹,², Zi-Jiang Liu³, Bo Kong², Wei-Long Quan¹,², Zhi-Jian Fu², Jian-Feng Li¹ and Jun-Hong Tian¹

¹ School of Mathematics and Physics, Lanzhou Jiaotong University, Lanzhou 730070, People's Republic of China
² National Key Laboratory of Shock Wave and Detonation Physics, Institute of Fluid Physics, China Academy of Engineering Physics, Mianyang 621900, People's Republic of China
³ Department of Physics, Lanzhou City University, Lanzhou 730070, People's Republic of China

E-mail: songting_lzju@126.com and sunxw_lzju@126.com

Received 29 September 2011
Accepted for publication 15 February 2012
Published 13 March 2012
Online at stacks.iop.org/PhysScr/85/045702

## Abstract
The pressure–volume equation of state ($P$–$V$ EOS) and isothermal bulk modulus, the volume–temperature ($V$–$T$) EOS and thermal expansivity are investigated for magnesium oxide (MgO) by using *ab initio* density functional theory (DFT) calculations combined with the quasi-harmonic Debye (QHD) model in which the phononic effects are considered and isothermal–isobaric ensemble molecular dynamics (MD) simulations with different effective pair-wise potentials that consist of the Coulomb, dispersion and repulsion interactions.
Polarization and compression effects are considered in MD simulations through the shell model (SM) and breathing shell model (BSM), respectively. The $P$–$V$ relationship and isothermal bulk modulus $K$ of the MgO dependence of pressures up to 200 GPa at 300 K and the $V$–$T$ relationship and volume thermal expansion coefficient $\alpha$ of the MgO dependence of temperatures up to 3000 K at 0.1 MPa have been obtained from MD and DFT calculations and compared with the available experimental data and other theoretical results. Particular attention is paid to the prediction of the first and second pressure derivatives $K'$ and $K''$ of the isothermal bulk modulus of MgO at a given temperature and pressure for the first time.
Compared with the SM potential, MD simulations with the BSM and QHD models are highly successful in accurately reproducing the measured volumes of MgO. At extended pressure and temperature ranges, $K$, $K'$, $K''$, $\alpha$ and $P$–$V$–$T$ EOS have also been predicted. Detailed knowledge of the thermodynamic behavior in extreme conditions is of fundamental importance for understanding the physical properties of MgO.

PACS numbers: 71.15.Pd, 65.40.–b, 62.50.+p

(Some figures may appear in colour only in the online journal)

---

## 1. Introduction

Magnesium oxide (MgO) has been used in the past as a testing ground for models of ionic systems [1]. It is considered to be the simplest oxide and yet it is a system in which many-body interactions associated with distortions of the large oxide anion are known to be important [2–4]. It is therefore a starting point for attempts to model the many-body interactions in oxides and ionic systems in general. MgO is a system of geophysical importance. It is an important component of the Earth's lower mantle and its stability up to high pressures [5] makes it useful as a pressure calibration standard for high-pressure and -temperature experiments. Since the vast majority of compounds present in the Earth's mantle are oxides, MgO is a starting point for studies of the effects of pressure and temperature on mantle materials.

The stability and thermodynamic properties of MgO have been extensively studied theoretically and experimentally [6–14].

Investigations on high-temperature and high-pressure behavior of solids demonstrate that thermodynamic properties such as the pressure–volume ($P$–$V$) relationship and the isothermal bulk modulus $K$, especially the first and second pressure derivatives $K'$ and $K''$ of the isothermal bulk modulus at a given temperature and pressure and the volume–temperature ($V$–$T$) relationship and thermal expansivity $\alpha$ are important for earth and material science as they often occur in equations that describe many important properties of materials [15–17]. Meanwhile, thermal expansivity has been related to other thermodynamic parameters through the Grüneisen rules. It is a factor in the equations describing many important properties of solids, and it together with specific heat is essential for predicting a thermodynamic equation of state (EOS). In order to understand the nature of MgO at high temperatures and high pressures it is necessary to use some form of microscopic modeling or simulation. Many attempts have been made to study the temperature dependence of thermal expansivity by considering its linear as well as nonlinear dependence [18–20]. The formulation thus developed has been reviewed by Kushwah and Shanker [21] in the case of MgO in the temperature range 300–1800 K. They found that most of the empirical formulae reported up to then were inadequate for predicting $\alpha$ in the entire temperature range. The Suzuki equation, which is based on the Grüneisen theory of thermal expansion [22], yields good agreement with experimental data on $\alpha$ corresponding to the entire temperature range not only for MgO [21] but also for other minerals [23–25]. It is very difficult to measure $\alpha$ for a solid at high temperatures (1500–2000 K) and pressures (100–150 GPa) [26, 27]; alternative methods for calculating $\alpha(T, P)$ are therefore desirable.

In this work, our aim is to perform molecular dynamics (MD) simulations on MgO using different empirical pair potentials [28, 29] that reproduce the structural and thermodynamic data in extreme $P$–$T$ conditions. Polarization effects are considered in MD simulations through the shell model (SM). A comparison is offered by the *ab initio* plane-wave pseudopotential density functional theory (DFT) method combined with the quasi-harmonic Debye (QHD) model in which the phononic effects are considered [30]. However, it is often pointed out that non-central forces are very important for crystals containing ions with large polarizability, such as oxides and silicates [31]. In order to account for the observed large departures from the Cauchy relation of the elastic constants of MgO, the breathing shell model (BSM) is also introduced in MD simulations, in which the repulsive radii of oxygen ions are allowed to deform isotropically under the effects of other ions in the crystal, with each core and breathing shell being linked by a harmonic spring with a force constant $k$. Matsui [32] had developed an efficient but inexpensive way of performing MD simulations with BSM, and the MD-BSM had been found to be very successful in accurately reproducing the observed large Cauchy violations in both MgO and CaO crystals, as well as the measured molar volumes and three independent elastic constants of the two oxides over wide temperature ranges, at zero pressure.

This paper is organized as follows. In section 2 we describe the interatomic potentials and calculation methods used in this work, and in section 3, we present and discuss our results obtained from MD simulations with effective pair-wise interactions and DFT calculations with the QHD model, and to predict the thermodynamic properties of MgO in extreme $P$–$T$ conditions (up to 200 GPa and 3000 K) where reliable experimental data are scarce. A critical comparison between experimental and theoretical results is possible for MgO as the structural and thermodynamic parameters can be measured with a fair level of accuracy since the solid mainly adopts a simple rock-salt structure. The paper ends with the main conclusions in section 4.

## 2. Theoretical methods

### 2.1. Details of the interatomic potentials

The physical properties of a solid may be established by solving the Schrödinger equation explicitly, thereby precisely obtaining the energy surfaces associated with the interactions of electrons and nuclei within a given system. This *ab initio* approach has now been widely used to explore the structural, dynamical and electronic properties of MgO from an accurate treatment of the electronic structure using density functional theory: thus many-body and polarization effects are explicitly accounted for [33, 34]. However, even with the large computational resources available today, the size and time scales which can be probed by *ab initio* MD are usually about 100–200 atoms and 10–50 ps [35]. Within these limits, in order to probe longer time scales and examine the structure at and beyond the medium range, classical MD is still the only available approach, provided that a reliable potential can be developed.

In order to model such interatomic interactions, it is first necessary to understand the potential energy functions which describe them. This is achieved initially by considering a two-body system; many-body systems are generally prohibitively complex, computer intensive and time consuming. The potential energy function expresses the energy of an assembly of $N$ atoms or ions as a function of the nuclear coordinates $r_1, r_2, \dots, r_N$. It is commonly expanded as follows:

$$
U = \sum_{i}^{N} \sum_{j}^{N} ' u_{ij}(r_i, r_j) + \sum_{i}^{N} \sum_{j}^{N} \sum_{k}^{N} ' u_{ijk}(r_i, r_j, r_k) + \cdots,
\tag{1}
$$

where $u_{ij}$ are two-body functions that depend only on the positions of pairs of atoms $i$ and $j$; $u_{ijk}$ are the three-body terms depending explicitly on the positions of atoms $i$, $j$ and $k$. The expanded form can be extended to four-body terms $u_{ijkl}$ and higher-order terms. Moreover, it is common to approximate $U$ by including only the two-body component $u_{ij}$, which may be usefully decomposed into the Coulombic and non-Coulombic terms:

$$
u_{ij}(r_i, r_j) = \frac{1}{4\pi \varepsilon_0} \frac{Z_i Z_j \mathrm{e}^2}{r_{ij}} + u_{ij}^{\mathrm{NC}}(r_{ij}),
\tag{2}
$$

where $r_{ij}$ is the interatomic distance between ions $i$ and $j$, $Z_i$ is an effective charge of the $i$th ion. The short-range non-Coulombic interactions $u_{ij}$ predominantly affect nearest-neighbor ions, and may be represented by effective pair-wise potentials such as the Buckingham potential that takes the form

$$
u_{ij}^{\mathrm{NC}}\left(r_{ij}\right)=A_{ij} \mathrm{e}^{-r_{ij} / B_{ij}}-\frac{C_{ij}}{r_{ij}^{6}}-\frac{D_{ij}}{r_{ij}^{8}},
\tag{3}
$$

where $A_{ij}$, $B_{ij}$, $C_{ij}$ and $D_{ij}$ are constants. The first term in $u_{ij}^{\mathrm{NC}}(r_{ij})$ is that due to short-range repulsion, whereas the second term is due to van der Waals-induced dipole-dipole attraction.

### 2.2. MD simulations

MD is a technique that enables us to use the description of interatomic interactions, given in the previous section, to predict the physical properties of matter. MD simulation is a powerful technique for the study of many-particle systems. Atomic trajectories are calculated from direct integration of Newton's equations to deduce the thermodynamic properties of the system. The essence of MD calculations is the solution of Newton's laws of motion over a finite time period for a simulation box containing $N$ ions, calculating the dynamic properties iteratively as the system evolves. Normally, periodic boundary conditions (PBC) applied to the ensemble generate the required infinite system. The ions are initially assigned positions and velocities within the simulation box; their initial coordinates are usually chosen to be at the crystallographically determined sites, while their velocities, $v_i$, are chosen such that they concur with the required system temperature and are such that both energy and momentum are conserved.

In order to calculate subsequent positions and velocities, the forces acting on any individual ion must be calculated from the first derivative of the potential function, and the new position and velocity of each ion may then be calculated at each time step by solving Newton's equations of motion. Although computational capacity keeps increasing dramatically, there is always a need for a more efficient algorithm for the integration of Newton's equations of motion. For example, it is desirable that the energy of a system in a microcanonical ensemble be conserved accurately even when a rather large time step is used. For a finite time step, the equations lose their accuracy and higher powers of $\Delta t$ are required; in our calculations the equations of motion are solved using Gear's predictor-corrector algorithm [36] whereby a fifth-order Taylor series expansion of the displacements with respect to time generates predicted evolving positions which are then corrected iteratively until a convergent solution to the trajectories and velocities is obtained. Gear's predictor-corrector algorithm is generally accepted to be more accurate, but less stable, than Verlet's algorithm when the time step size is 'small' [37]. As for MgO, good energy conservation behavior of Gear's predictor-corrector algorithm has been observed during MD simulation using the existing variety of realistic potentials. Vočadlo and Price [38] have successfully performed MD calculations for the melting of MgO on a constant stress system containing 1728 ions using a variety of potential models based on Gear's predictor-corrector algorithm, and good results have been obtained.

#### 2.2.1. The SM-MD method.
The MD simulation method involving pair potentials with either a rigid-ion model or the SM has long been used with considerable success to describe the high-temperature and high-pressure thermodynamic properties of many ionic systems. In principle, an essential ingredient of a reliable empirical potential for the systems should be the large polarizability of anions and cations. In general, the inclusion of polarization effects, especially for systems with polarizable anions, can improve structural and thermodynamic properties [39]. In the aspherical ion model (AIM) developed by Madden and coworkers [40-42], polarization effects in classical MD simulations of ionic systems are accurately represented by the inclusion of ion dipoles as additional degrees of freedom in an extended Lagrangian, and the simultaneous propagation of these additional variables together with the ionic positions is analogous to the Car-Parrinello method. Scandolo and Scandolo [43-45] presented a many-body force field for ionic systems that incorporates the effect of an ion's environment on its shape and size and the impact that such ionic distortions have on the short-range repulsive interactions between ions. Another simple and consistent way to go beyond rigid-ion models and approximately include polarization effects in an empirical potential is by using the SM of Dick and Overhauser [46], which can be efficiently implemented in classical MD simulations. The more rigorous description of ionic polarization in the AIM method makes it in principle more generally applicable compared to the SM; the main advantage of an SM approach in the specific subject examined in the present work is the relatively small effort needed to obtain the appropriate results.

In the SM, atomic polarizability is accounted for by defining a core and a shell for each ion (representing the ion core with the closed shells of electrons and the valence electrons, respectively), which interact with each other through a harmonic spring (characterizing the ionic polarizability), and interact with the cores and shells of other ions via Coulombic interactions. The interactions among the valence electrons are characterized by a repulsive, exponentially decaying, pair-potential interaction between shells (the Born-Mayer term). This combination of the Born-Mayer term and the van der Waals interaction is known as the Buckingham potential. For ionic materials the short-range non-Coulombic interaction in the form of a Buckingham potential is a rather traditional model that has been shown to perform sufficiently well [15-17].

In order to obtain reasonable values for the static and high-frequency dielectric constants of MgO, it was necessary to use the SM for the oxygen ions [46]. We use the SM-LC potentials of Lewis and Catlow (LC) with formal charges $\pm 2.0$e [28]. The interatomic potentials have the usual form as shown in equation (3), and the parameters of the short-range pair potentials ($A_{ij}$, $\rho_{ij}$ and $C_{ij}$, and the shell charges, $Y$, and the spring constant, $k$, associated with the SM description of polarizability) are obtained by empirical fitting to the properties of MgO. The parameters of MgO

used in simulations are given in [28]. The potential models used here reproduce the *ab initio* static EOS calculations of Isaak *et al* [47], and the experimental data summarized in Knittle [48]. Fincham *et al* [49] have studied the $P$–$V$–$T$ relations for MgO at high pressures and temperatures, and the obtained results were compared with those of other works, and good agreement was observed. Recently, empirical potential were fitted for MgO by Ball and Grimes (BG), using partial charges $\pm 1.7$e [29]. Here we make a comparison by using the BG potential. Unless the interionic distances are very short, the effect of the differences between this potential and that of Lewis and Catlow is small, as pointed by Henkelman *et al* [29].

2.2.2. The BSM-MD method. In this section, we describe the BSM-MD method to better reproduce the thermodynamic behavior of MgO, while maintaining an accurate description of the structure. The pair-wise interactions are still represented by the combination of the Coulomb energy, repulsive exponential and attractive dispersion terms, since this formulation has proven to be effective for many different ionic materials [15–17]. The main change relates to the description of the oxygen polarization. In the BSM, the ion shell has a finite radius, $R_0$, which is allowed to deform isotropically under the influence of the other ions. Here, the ion size is coupled to the environment through the short-range repulsive potential acting upon the radius of the shell, rather than its centre. The contribution to energy from each core–shell pair $V_i = k_i r_i^2/2$ in SM is still valid to treat the core–shell dipolar contribution, but an additional potential, which has been chosen to be harmonic, describes the breathing shell:

$$
V_{i}=\frac{1}{2} K_{i}\left(R_{i}-R_{0}\right)^{2}, \tag{4}
$$

where $K_i$ is a spring constant and $(R_i-R_0)$ is the distance from the finite shell radius of the ion $i$. The most significant consequence of the introduction of a BSM is that, by introducing non-central forces, it is able to reproduce the Cauchy violation ($C_{44} \neq C_{12}$).

Obtaining transferable potentials for oxides has been an important objective of materials modelling for many years [39]. A transferable potential works over a wide range of physical conditions, describes different phases equally well and continues to apply when the material of interest is combined with another in a compound. The problem posed by oxides is that the electronic properties of an oxide ion are particularly sensitive to changes in the coordination environment, so that a potential that will work transferably must account for the resulting many-body character of the interactions. The parameters of interatomic interactions appearing in the AIM potential in MgO, CaO, SrO and BaO had been obtained from the *ab initio* MD code CASTEP on condensed phase ion configurations generated at different values of pressure, temperature and coordination environment [41, 50]. The models were shown to be transferable in the sense that they offered equally accurate descriptions of the pure materials over very wide ranges of temperature and pressure and in phases with different coordination numbers [51]. Here the optimized potential parameters of the BSM used in this work are given in [52], and they are obtained by fitting to the macroscopic elastic constants, to the dielectric constants and to infrared dispersion and neutron scattering data. This model has been successfully used by Sangster *et al* [53] to describe the bulk lattice dynamics of MgO, and is shown to give substantially better agreement with experimental results than the normal shell model.

2.3. MD simulation details

In this work, a standard constant pressure and temperature (NPT) MD calculation [54] on thermodynamic equilibrium has been performed. All simulations were started from a cubic simulation cell containing 1000 ions (500 $\text{Mg}^{2+}$ and 500 $\text{O}^{2-}$ ions) initially arranged in the NaCl-type crystal structure. The sides of the cell were in the [100], [010] and [001] directions. Normally, as is often the case in MD calculation, PBC corresponding to a cubic primary cell are applied. To facilitate the computation of the Coulomb and dispersion interactions, respectively, the Ewald sum method [55] and the convergence–acceleration technique described by Williams [56] were used. The equations of motion are solved using a fifth-order predictor–corrector algorithm with a time increment of 1.0 fs. In each MD run a sufficiently long period of 10 000 time steps (10 ps) is performed to establish equilibrium of the system under desired temperature and pressure conditions. After this, a subsequent period of 10 000 time steps is carried out to simulate structural and thermodynamic properties studied here.

2.4. Total energy electronic structure calculations

*Ab initio* calculations are performed using DFT with Vanderbilt-type ultrasoft pseudo-potentials [57] for electron–ion interactions to calculate the total energies and thermodynamic properties. In order to obtain more accurate results, here the PBEsol, a revised Perdew–Burke–Ernzerhof functional for the generalized gradient approximation (GGA) that improves equilibrium properties of densely packed solids, is presented [58]. Pseudo-atomic calculations are performed for Mg $2\text{p}^6 3\text{s}^2$ and O $2\text{s}^2 2\text{p}^4$. The energy cutoff of the plane-wave basis was chosen as 750 eV. For the Brillouin-zone sampling, we adopted the $18 \times 18 \times 18$ Monkhorst–Pack mesh [59], where the self-consistent convergence of the total energy is at $10^{-7}$ eV atom$^{-1}$. The chosen plane-wave cutoff and the number of $k$ points were carefully checked to ensure the total energy converged. For a given external hydrostatic pressure, both the parameters of the unit cell and the internal coordinates of the atoms are fully relaxed until forces had converged to less than $0.01$ eV Å$^{-1}$ and all the stress components are less than 0.02 GPa.

To investigate the thermodynamic properties of MgO, we applied here the QHD model [30], in which the non-equilibrium Gibbs function $G^{*}(V;P,T)$ is taken in the form of

$$
G^{*}(V ; P, T)=E(V)+P V+A_{\mathrm{vib}}(\Theta(V) ; T), \tag{5}
$$

where $E(V)$ is the total energy, $PV$ corresponds to the constant hydrostatic pressure condition, $\Theta$ $(V)$ is the Debye

![](./images/813326355893583872_1.jpg)

Figure 1. MD calculated molar volumes of MgO as a function of pressure at 300 K, compared with the results of DFT-GGA calculations and an XRD experiment.

temperature and the vibrational contribution $A_{\mathrm{vib}}$ can be written as [60]

$$
A_{\mathrm{vib}}(\Theta ; T)=n k T\left[\frac{9}{8} \frac{\Theta}{T}+3 \ln \left(1-\mathrm{e}^{-\Theta / T}\right)-D(\Theta / T)\right],
\tag{6}
$$

where $D(\Theta / T)$ represents the Debye integral and $n$ is the number of atoms per formula unit. By solving the following equation with respect to $V$:

$$
\left[\frac{\partial G^{*}(V ; P, T)}{\partial V}\right]_{P, T}=0,
\tag{7}
$$

one could obtain the isothermal bulk modulus $K_{T}$ and the thermal expansion coefficient $\alpha$, respectively.

## 3. Results and discussion

Figure 1 shows a comparison of our calculated $P$–$V$ relationship; the experimental data were obtained by combining synchrotron x-ray diffraction (XRD) techniques [8] for MgO. The MD-simulated 300 K isotherms are also compared with the $ab$ initio calculations and isothermal EOS such as the Rydberg–Vinet EOS calculations [61, 62]. Note that the calculated molar volumes using the BSM potential are in good agreement with the XRD experimental data in hydrostatic conditions [8]. In contrast with the excellent agreement in hydrostatic compression experiments as mentioned above, the BSM-MD simulation is less successful in reproducing the measured molar volumes of MgO at very high pressures, as shown in figure 1. The results obtained from BSM are more compressible than the SM, and the compressibility for the SM is still too small compared with the experimental data and Rydberg–Vinet EOS calculations.

The bulk modulus of MgO from the corresponding isothermal equations of the state mentioned above are obtained at 300 K, as shown in figure 2. Figure 2 shows a comparison of the present isothermal bulk modulus of the QHD model [30] calculations and MD simulations versus pressure with Sushil’s data [63] at 300 K. The simulated value 163 GPa using the BSM potential agrees well with Sushil’s EOS result 162 GPa at 300 K. Note that the calculated results using the BSM potential are in excellent agreement with the data obtained from Sushil’s EOS and the QHD model under lower pressure, and good agreement is obtained from the SM potential and the EOS data under high pressure. The isothermal bulk modulus obtained from the QHD model through the $E$–$V$ relationship of DFT-GGA and the calculated energies as a function of the primitive cell volume for MgO are shown in figure 3. In the inset, the enthalpy as a function of pressure at zero temperature is also presented.

![](./images/813326355893583872_2.jpg)

Figure 2. The isothermal bulk modulus of MgO calculated using the QHD model and MD as a function of pressure at 300 K.

![](./images/813326355893583872_3.jpg)

Figure 3. GGA-calculated energy as a function of primitive cell volume for the B1 phase of MgO. In the inset, the enthalpy as a function of pressure of MgO with B1 and B2 structures at zero temperature is presented.

The first and second pressure derivatives $K'$ and $K''$ of the isothermal bulk modulus $K$ at a given temperature and pressure are very important for high-pressure studies. From a geophysical viewpoint, $K'$ and $K''$ are parameters that are necessary for the accurate inversion of seismic data into composition, structure and texture, as well as for determining the thermal profile of the deep Earth [64] and also for determining the isothermal empirical equation of the state of materials in the deep Earth [65]. Since the variation in many of the macroproperties of solids with

![](./images/813326355893583872_4.jpg)

Figure 4. The predicted first pressure derivative of isothermal bulk modulus of MgO versus pressure at different temperatures.

![](./images/813326355893583872_5.jpg)

Figure 5. The predicted second pressure derivative of isothermal bulk modulus of MgO versus pressure at different temperatures.

temperature and pressure are closely related to $K'$ and $K''$, $K'$ and $K''$ are crucial for thermodynamic calculations of the properties at high temperatures and high pressures [66]. Thus, precise determination of the temperature dependence of $K'$ and $K''$ is significant in many fields, including geophysics, condensed matter physics and materials science. As is well known, the MgO phase transformation from the $B1$ phase (NaCl-type structure) to $B2$ phase (CsCl-type structure) occurs at high pressure when the solid becomes unstable under thermodynamic conditions. Using first-principles calculations, we have analyzed the phase stability of the $B1$ and $B2$ structures of MgO from the usual condition of equal Gibbs free energies, as shown in the inset of figure 3. It is seen that the enthalpy of $B2$ structure is always higher than that of $B1$ structure in the entire pressure range from 0 to 500 GPa at zero temperature, i.e. the transition pressure of MgO from $B1$ to $B2$ structure up to at least 500 GPa. Our calculation result is consistent with the predicted values 486 GPa calculated by Isaak et al [47] using an ab initio potential-induced breathing (PIB), 509 and 489 GPa calculated by Oganov and Dorogokupets [67] using projector augmented wave calculations, 510 GPa calculated by Mehl and Cohen [68] using linearized augmented plane-wave and 580 GPa calculated by Zhang and Bukowinski [69] using modified PIB models. We think that all these deviations are due to the different calculation methods. In the following, considering the very high phase transition pressure, we only investigate the first and second pressure derivatives $K'$ and $K''$ of the isothermal bulk modulus $K$ of the $B1$ phase of MgO through the QHD model.

Figures 4 and 5 show the predicted first and second pressure derivatives $K'$ and $K''$ of the isothermal bulk modulus $K$ of MgO with $B1$ and $B2$ structures versus pressure along isotherms 0, 500, 1000, 1500 and 2000 K. It can be seen that $K''$ increases with an increase of temperature in the entire pressure range 0–200 GPa, and the first pressure derivative $K'$ decreases with an increase of temperature when $P > 115$ GPa. The second pressure derivative $K''$ of MgO is rather steep when $P < 25$ GPa, rapidly flattens with increasing pressure and remains constant when $P > 70$ GPa. Thus, the $K''$ of MgO at high pressures is a weak function of temperature and pressure.

![](./images/813326355893583872_6.jpg)

Figure 6. MD-calculated molar volumes of MgO as a function of temperature at 0.1 MPa.

Figure 6 shows the observed [13] and simulated temperature dependences of molar volumes of MgO at zero pressure. The small error in the calculated values at low temperatures is partly due to quantum effects which are not considered in the classical MD calculations, as described by Matsui [70]. Compared with the simulated isobaric curves at zero pressure, the XRD experimental results are found to have increasing departure when the temperature is above 2000 K. We think that any dispersion might be due to the sample quality and the accuracy of experimental techniques.

Figure 7 shows the volume thermal expansivity of MgO from the corresponding isobar equations of state versus temperature at zero pressure. The present thermal expansivity of MD simulations obtained from the SM and BSM potentials are in good agreement with the results of Isaak et al's PIB electron gas model based on the fist-principles approach [47] at lower temperature, but are lower than the experiments [71] and observed results [72]. However, the results obtained from the QHD model are more scattered and we can see that the volume thermal expansion coefficient $\alpha$ increases with $T^{3}$ at low temperature $T$ and gradually increases linearly with temperature and then the increasing trend becomes gentler. It is known that the volume thermal expansion

![](./images/813326355893583872_7.jpg)

Figure 7. The volume thermal expansivity of MgO calculated using the QHD model and MD as a function of temperature up to 3000 K at zero pressure.

![](./images/813326355893583872_8.jpg)

Figure 8. The volume compression of MgO up to 200 GPa at 300, 1500 and 3000 K.

coefficient has been studied by using a number of methods and many different results obtained. The dispersion might be due to the accuracy of the experimental method. It is well known that there are certain difficulties associated with the measurement of the volume thermal expansion coefficient at high temperatures which lead to considerable uncertainties in the experimental values [26]. Each calculation method also has its own limitations related to the basic material parameters, basis sets and the precisions used, in addition to the approximations of the method itself, leading to variations in the calculated parameters. Our results are of the same order as the theoretical and experimental results when the temperature is up to 3000 K, after all.

Predicted $P-V$ relationship curves using SM-MD and BSM-MD simulations up to 200 GPa at 300, 1500 and 3000 K are shown in figure 8. For isothermal compressions, the volume is strongly affected by both pressure and temperature. The effect of increasing pressure on MgO is the same as of decreasing temperature of MgO. At a given temperature the volume decreases with an increase of pressure, and the volume at lower temperature is less than that at higher temperature for a given pressure. On the other hand, at higher temperatures and under lower pressures, the volume is strongly affected by the pressure compared with the lower temperatures and under lower pressures.

![](./images/813326355893583872_9.jpg)

Figure 9. The $T-V$ relationship curves of MgO up to 3000 K.

Predicted $V-T$ relationship curves are illustrated in figure 9. We find that, under lower pressure, the volume varies quickly as the temperature rises. Under higher pressures, it becomes moderate, and the $V-T$ relations are nearly linear. These compression behaviors may be correspond to the bonding situations in MgO, which is characterized by a strong covalent bonding in the oxygen layers, ionized magnesium atoms and a weaker interlayer metallic bonding. When pressure is increased, the atoms in the interlayers become closer and their interactions become stronger.

![](./images/813326355893583872_10.jpg)

Figure 10. MD-predicted volume thermal expansivity of MgO as a function of pressure at different temperatures.

In order to further investigate the influence of pressure on thermal expansivity of MgO, simulations were performed in the temperature range 500–3000 K and at pressures up to 200 GPa and are shown in figure 10. It can be seen that the volume thermal expansivity of MgO decreases with an increase of pressure. The curve of the volume thermal expansivity of MgO, being rather steep at lower pressures, rapidly flattens on increasing pressure. Note that the influence of temperature on thermal expansion at high pressures is very small and may be neglected at $>$ 100 GPa pressure. This is mainly because the anharmonic effects become less important at high pressure. With increasing pressure, the volume of

![](./images/813326355893583872_11.jpg)

Figure 11. MD-predicted isothermal bulk modulus of MgO plotted against temperature at different pressures.

the solid is decreased and the atoms come closer to each other, increasing the depth of the potential energy well and reducing the anharmonic nature of the potential energy curve at high temperature. Since thermal expansivity is a result of anharmonicity in the potential energy, it becomes virtually independent of pressure and temperature in the high-pressure and -temperature domain. Thus, the thermal expansivity of MgO at high pressures is a weak function of temperature. Knowledge of thermal expansivity can help us to constrain other important parameters such as Grüneisen parameters and Rayleigh number.

Figure 11 shows the predicted values of the isothermal bulk modulus dependence of temperature using three SM-MD simulations at different pressures in the range 50-200 GPa. We see that as the temperature increases, the bulk modulus $K_T$ decreases, reflecting the fact that the solid is more compressible as it is heated and, as expected, the converse is true for increased pressure. Note that there is a constant value for $\partial K_T/\partial T$ at each isobar and that it decreases as pressure increases.

## 4. Conclusions
The $P$-$V$-$T$ relationship, isothermal bulk modulus and its pressure derivatives, and the thermal expansivity of MgO have been obtained by using the QHD model and the shell and breathing shell MD methods in the pressure range 0-200 GPa and at temperatures up to 3000 K. Compared with SM and BG potentials, the MD simulation with BSM potential is very successful in reproducing accurately the measured volumes of MgO at lower pressures. The results obtained from BSM are more compressible than the SM. For isothermal compressions, at higher temperatures and under lower pressures, the volume is strongly affected by pressure. The volume varies quickly as the temperature rises under lower pressures, and the $T$-$V$ relations are nearly linear under higher pressures for the isobaric curves. It can be found that the isothermal bulk modulus of MgO decreases with increasing temperature and increases with increasing pressure. The thermal expansivity of MgO in the low pressure range is increased with increasing temperature. The influence of temperature on thermal expansivity is very small and may be neglected at above 100 GPa pressure. In extended pressure and temperature ranges, the first and second pressure derivatives $K'$ and $K''$ of isothermal bulk modulus of MgO are predicted by using the QHD model in which the phononic effects are considered. It can be found that the first pressure derivative of the isothermal bulk modulus of MgO decreases with an increase of temperature when $P > 115$ GPa. The second pressure derivative of the isothermal bulk modulus of MgO is rather steep at lower pressures and then it remains constant with increasing pressure. That is, it is a weak function of temperature and pressure at high pressures.

## Acknowledgments
We acknowledge support from the National Natural Science Foundation of China under grant numbers 11164013 and 11064007, the Natural Science Foundation of Gansu Province of China under grant number 1014RJZA046 and the Program for New Century Excellent Talents in University under grant number NCET-11-0906.

## References
[1] Rowley A, Jemmer P, Wilson M and Madden P A 1998 *J. Chem. Phys.* **108** 10209
[2] Schröder U 1996 *Solid State Commun.* **4** 347
[3] Wilson M, Madden P A, Pyper N C and Harding J H 1996 *J. Chem. Phys.* **104** 8068
[4] Boyer L L, Mehl M J, Feldman J L, Hardy J R, Flocken J W and Fong C Y 1985 *Phys. Rev. Lett.* **54** 1940
[5] Duffy T S, Hemley R J and Mao H-K 1995 *Phys. Rev. Lett.* **74** 1371
[6] Chang K J and Cohen M L 1984 *Phys. Rev. B* **30** 4774
[7] Mehl M J, Cohen R E and Krakauer H 1988 *J. Geophys. Res.* **93** 8009
[8] Fei Y 1999 *Am. Mineral.* **84** 272
[9] Sun X W, Chen Q F, Chu Y D and Wang C W 2005 *Physica B* **370** 186
[10] Sun X W, Song T, Liu Z J, Chen Q F, Liu X B and Wang C W 2007 *Physica B* **399** 9
[11] Song T, Sun X W, Liu Y X, Liu Z J, Chen Q F and Wang C W 2008 *J. Alloys Compounds* **461** 279
[12] Jaffe J E, Snyder J A, Lin Z and Hess A C 2000 *Phys. Rev. B* **62** 1660
[13] Fiquet G, Richet P and Montagnac G 1999 *Phys. Chem. Miner.* **27** 103
[14] Dewaele A, Fiquet G, Andrault D and Hausermann D 2000 *J. Geophys. Res. B* **105** 2869
[15] Sun X W, Liu Z J, Song T, Liu X B, Wang C W and Chen Q F 2007 *Chin. J. Chem. Phys.* **20** 233
[16] Sun X W, Wang X G, Song T, Li Y H, Liu Y X and Chen Q F 2008 *Physica B* **403** 3255
[17] Sun X W, Liu Z J, Chen Q F, Yu J N and Wang C W 2007 *J. Phys. Chem. Solids* **68** 249
[18] Shanker J, Kushwah S S and Kumar P 1997 *Physica B* **233** 78
[19] Thomas L M and Shanker J 1996 *Phys. Status Solidi b* **195** 361
[20] Singh K S and Chauhan R S 2002 *Physica B* **315** 74
[21] Kushwah S S and Shanker J 1996 *Physica B* **225** 283
[22] Suzuki I 1975 *J. Phys. Earth* **23** 145
[23] Suzuki I, Okajima S and Seya K 1979 *J. Phys. Earth* **27** 63
[24] Knittle E, Jeanloz R and Smith G L 1986 *Nature* **319** 214
[25] Anderson O L, Isaak D G and Oda H 1992 *Rev. Geophys.* **30** 57
[26] Anderson O L and Zou K 1989 *Phys. Chem. Miner.* **16** 642
[27] Xia X and Xiao J K 1993 *J. Phys. Chem. Solids* **54** 629

[28] Lewis G V and Catlow C R A 1985 *J. Phys. C: Solid State Phys.* **18** 1149

[29] Henkelman G, Uberuaga B P, Harris D J, Harding J H and Allan N L 2005 *Phys. Rev. B* **72** 115437

[30] Blanco M A, Francisco E and Luaña V 2004 *Comput. Phys. Commun.* **158** 57

[31] Cohen R E, Boyer L L and Mehl M J 1987 *Phys. Rev. B* **35** 5749

[32] Matsui M 1998 *J. Chem. Phys.* **108** 3304

[33] Karki B B, Bhattarai D and Stixrude L 2006 *Phys. Rev. B* **73** 174208

[34] Stackhouse S, Stixrude L and Karki B B 2010 *Phys. Rev Lett.* **104** 208501

[35] Car R and Parrinello M 1985 *Phys. Rev. Lett.* **55** 2471

[36] Gear C W 1996 The numerical integration of ordinary differential equations of various orders *Argonne National Laboratory Report* ANL 7126

[37] Sadus R J 1999 *Molecular Simulation of Fluids* (Amsterdam: Elsevier)

[38] Vočadlo L and Price G D 1996 *Phys. Chem. Miner.* **23** 42

[39] Madden P A and Wilson M 1996 *Chem. Soc. Rev.* **25** 339

[40] Wilson M and Madden P A 1993 *J. Phys.: Condens. Matter* **5** 2687

[41] Aguado A, Bernasconi L and Madden P A 2002 *Chem. Phys. Lett.* **356** 437

[42] Aguado A and Madden P A 2004 *Phys. Rev. B* **70** 245103

[43] Tangney P and Scandolo S 2003 *J. Chem. Phys.* **119** 9673

[44] Adebayo G A, Liang Y, Miranda C R and Scandolo S 2009 *J. Chem. Phys.* **131** 014506

[45] Tangney P and Scandolo S 2009 *J. Chem. Phys.* **131** 124510

[46] Dick B G and Overhauser A W 1958 *Phys. Rev.* **112** 90

[47] Isaak D J, Cohen R E and Mehl M J 1990 *J. Geophys. Res.* **95** 7055

[48] Knittle E 1995 Static compression measurements of equations of state *Mineral Physics and Crystallography: A Handbook of Physical Constants* ed T J Ahrens (Washington, DC: American Geophysical Union) pp 98–142

[49] Fincham D, Mackrodt W C and Mitchell P J 1994 *J. Phys.: Condens. Matter* **6** 393

[50] Aguado A, Bernasconi L and Madden P A 2003 *J. Chem. Phys.* **118** 5704

[51] Aguado A and Madden P A 2003 *J. Chem. Phys.* **118** 5718

[52] Catlow C R A, Faux I D and Norgett M J 1979 *J. Phys. C: Solid State Phys.* **9** 419

[53] Sangster M J L, Peckham G and Saunderson D H 1970 *J. Phys. C: Solid State Phys.* **3** 1026

[54] Allen M P and Tildesley D J 1987 *Computer Simulation of Liquids* (Oxford: Oxford University Press)

[55] Fincham D 1992 *Mol. Simul.* **8** 165

[56] Williams D E 1971 *Acta Crystallogr. A* **27** 452

[57] Vanderbilt D 1990 *Phys. Rev. B* **41** 7892

[58] Perdew J P, Ruzsinszky A, Csonka G I, Vydrov O A, Scuseria G E, Constantin L A, Zhou X and Burke K 2008 *Phys. Rev. B* **100** 136406

[59] Monkhorst H J and Pack J D 1976 *Phys. Rev. B* **13** 5188

[60] Francisco E, Sanjurjo G and Blanco M A 2001 *Phys. Rev. B* **63** 094107

[61] Vinet P, Rose J H, Ferrante J and Smith J R 1989 *J. Phys.: Condens. Matter* **1** 1941

[62] Rydberg R 1932 *Z. Phys.* **73** 376

[63] Sushil K 2005 *Physica B* **367** 114

[64] Duffy T S and Anderson D L 1989 *J. Geophys. Res.* **94** 1895

[65] Anderson O L 1995 *Equations of State of Solids for Geophysics and Ceramics Science* (New York: Oxford University Press) p 405

[66] Cynn H, Anderson O L, Isaak D G and Nicol M 1995 *J. Phys. Chem.* **99** 7813

[67] Oganov A R and Dorogokupets P I 2003 *Phys. Rev. B* **67** 224110

[68] Mehl M J and Cohen R E 1988 *J. Geophys. Res.* **93** 8009

[69] Zhang H Y and Bukowinski M S T 1991 *Phys. Rev. B* **44** 2495

[70] Matsui M 1989 *J. Chem. Phys.* **91** 489

[71] Jacobs M H G and Oonk H A J 2000 *Phys. Chem. Chem. Phys.* **2** 2641

[72] Anderson O L and Suzuki I 1983 *J. Geophys. Res.* **88** 3549