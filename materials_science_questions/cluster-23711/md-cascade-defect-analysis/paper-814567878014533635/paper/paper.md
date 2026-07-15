# Multiscale Modeling of Accumulation of Radiation Defects in Silicon Detectors Under Alpha Particle Irradiation

Mikhail Yu. Romashka, Alexey V. Yanilkin, Alexander I. Titov, Dmitry V. Gusin, Alexey V. Sidelev, Dmitry Yu. Mokeev

Abstract—A multiscale approach to modeling of accumulation of radiation defects in silicon alpha detectors applied in the associated particle imaging systems is developed. With this approach we calculated the dependencies of defect concentrations and leakage current on time in a detector which was irradiated by alpha particles with energy of 3.5 MeV.

Index Terms— Alpha particle irradiation, displacement damage, multiscale approach, radiation defects, silicon detectors, Stochastic Parallel PARticle Kinetic Simulator (SPPARKS).

## I. INTRODUCTION
ILICON is widely used for construction of semiconductor detectors of ionizing radiation. As all other materials, silicon is subjected to defect formation under irradiation. This leads to degradation of detector properties. That is why it is of great interest to study mechanisms of influence of the defects on detector characteristics and possible ways to increase radiation hardness of the detectors.

For theoretical modeling of change of detector properties under irradiation it is necessary to solve the following problems: (a) to calculate the dependencies of concentrations of various defects on time or irradiation dose, and (b) to calculate the influence of defects of each type on electrical properties of detectors. For solving these problems it is necessary to know properties of separate defects (such as diffusion coefficients, energy levels in the bandgap, cross sections of their interaction with charge carriers, etc). In this work FZ-silicon of n-type will be considered, with impurities of phosphorus (P), oxygen (O) and carbon (C). Concentrations of all other impurities are supposed to be negligibly small. Following [1]-[5], let us enumerate all impurities and defects that are found in silicon of such type under alpha particle irradiation:
1. Site carbon $C_s$, interstitial carbon $C_i$, oxygen $O_i$ and phosphorus $P_s$.
2. Vacancies V and vacancy clusters $V_n$.
3. Interstitials I and interstitial clusters $I_n$.
4. Complexes vacancy-oxygen VO, divacancy-oxygen $V_2O$, trivacancy-oxygen $V_3O$.
5. Vacancy-phosphorus complex VP.
6. Complexes carbon-phosphorus $C_iP_s$ (for short simply CP), carbon-carbon $C_iC_s$ (CC), carbon-oxygen $C_iO_i$ (CO).
7. Complexes with participation of interstitial ICC and ICO.

This list does not include complexes such as $VO_2$ and $V_2O_2$. This is because, in our supposition, oxygen dimer $O_2$ is absent in unirradiated silicon wafers, and single oxygen is immobile at working temperature of the detector (around $T=300$ K). So, $VO_2$ and $V_2O_2$ cannot be formed.

Electronic and diffusion properties of the defects used in our work are taken from [1]-[7]. According to [6], the most electrically active defect among listed above is the $V_2O$ complex. This complex brings major contribution to leakage current other things being equal. This is because the 0/- level of this defect lies almost strictly in the middle of the bandgap. During migration defects interact with each other. List of reactions and their capture radii used in our work are taken from [4] (see Table 1 in [4]).

The available data on defect properties can be applied for creation of a multiscale model of accumulation of defects in silicon and change of detector properties under their influence. For proton and neutron irradiation of silicon such model was described, for example, in [4]. However, we do not know works where such calculations would be carried out for alpha particle irradiation. The last is the purpose of our work.

## II. DETECTOR AND REGIME OF IRRADIATION
In this work the multi-pixel associated alpha particle silicon detector produced by All-Russia Research Institute of Automatics (VNIIA) will be considered. Detector diode structure is fabricated from high-resistivity FZ silicon and operated in full depletion mode. The detector is subjected to mixed irradiation by alpha particles and fast neutrons that have energies 3.5 MeV and 14.1 MeV correspondingly. For the central detector pixel the flux of each sort of particle falling normally on the surface is equal to $1.1\cdot10^5$ cm⁻²s⁻¹. During 1000 hours of operation under this irradiation conditions the leakage current changes from the value of order of 10 nA (for the unirradiated detector) to approximately 10 μA. Hereinafter all current values are normalized to 1 cm² of the device working area.

It is known that the main contribution to the leakage current introduce defects caused by irradiation with alpha particles,

All authors are with Federal State Unitary Enterprise "All-Russian Research Institute of Automatics n.a. N.L. Dukhov" (VNIIA), Moscow, 127055, Russia.
Corresponding author (M. Yu. Romashka) to provide e-mail: michaelromashka@gmail.com, telephone +7-916-056-1558.

978-1-5090-0232-0/15/$31.00 ©2015 IEEE

whereas the contribution of the defects created by neutrons is less than 15% for the fluences up to the order of $10^{12}\ \mathrm{cm}^{-2}$. In this regard, everywhere further we will consider only alpha particle irradiation, and will assume that the contribution of neutrons to the leakage current can be neglected.

## III. CALCULATION OF TIME DEPENDENCIES OF DEFECT CONCENTRATIONS

For calculation of dependencies of defect concentrations on time or irradiation dose a multiscale approach was used, which consists of three stages:

1.  Calculation of the number of primary knock-on atoms (PKA) per one alpha particle and energy distribution of PKA.
2.  Calculation of the numbers of *primary defects* per one alpha particle. We call primary defects the defects that appear directly by collision of projectile (alpha particle) with silicon atom and in following few picoseconds (typical time of evolution of atomic displacement cascade). Defects that recombine inside the region of the cascade are not included into the number of primary defects (i.e. only surviving defects are taken into account).
3.  Solution of the system of rate equations for concentrations of *secondary defects* (appearing as a result of long-range migration and interaction of primary defects) depending on time, with the assumptions of constant generation rate and uniform distribution of primary defects. Secondary defects are also supposed to be homogeneously distributed in the area of space, which corresponds to the Bragg peak (width of this area is assigned to be equal to the Bragg peak width).

![](./images/814567878014533635_1.jpg)

Fig. 1. Primary knock-on atoms energy distribution in the Bragg peak of $2\ \mu\mathrm{m}$ width by irradiation of silicon with alpha particles of 3.5 MeV energy. The bin width is 50 eV.

### A. Modeling of primary knock-on atoms (PKA)

At the first stage the number of PKA per one alpha particle and energy distribution of PKA were calculated with the aid of SRIM program [8]. Calculations show that alpha particles with energy of 3.5 MeV form in silicon a Bragg peak of $2\ \mu\mathrm{m}$ width with the center at a depth of $15\ \mu\mathrm{m}$. The majority of defects are created inside the Bragg peak. The amount of defects at the initial part of alpha particle trajectory is more than 3 times smaller than that of inside the peak. Energy distribution of PKA is shown in Fig. 1. The mean numbers of PKA and vacancies in Bragg peak per one alpha particle are 47 and 170 correspondingly, and the mean PKA energy is 146 eV.

### B. Calculation of the numbers of primary defects

At the second stage the number of primary defects per one alpha particle was calculated. This problem was solved in two different approaches. The first approach is connected with modeling of atomic displacement cascades by means of molecular dynamics (MD). In [9]-[12] MD was used for calculation of numbers of various defects remaining after atomic displacement cascade depending on PKA energy. With the help of distribution in Fig. 1 and data from [9]-[12] one can find the numbers of primary defects (specifically vacancies, divacancies (V₂), interstitials and diinterstitials (I₂)) per one alpha particle. There is no detailed information about larger defect clusters (in some works they are combined into one category "complex defects"). It is known that these larger clusters also appear in cascades, but in fewer amounts than V₂ and I₂. We will suppose that one can neglect formation of the larger clusters. The number $N_i$ of defects of $i$-th type is calculated as the following sum:

$$
N_{i}=\sum_{n=0}^{m} A(n) B_{i}(n), \tag{1}
$$

where $A(n)$ is the number of PKA with energies from $n\Delta E$ to $(n+1)\Delta E$ produced by one alpha particle, and $B_i(n)$ is the number of defects of $i$-th type produced by one PKA from this range of energies (data from [9]-[12]). Energy step $\Delta E$ was chosen to be 50 eV, and upper bound of energy was set to $(m+1)\ \Delta E=10\ \mathrm{keV}$.

The second method of calculation of the numbers of primary defects is based on the work [4]. The number of vacancies obtained from SRIM was multiplied by the coefficients from Table 3 of [4] for protons with energy of 10 MeV (alpha irradiation was not considered in [4], therefore we have used coefficients for protons). For calculation of the number of primary vacancies the coefficient $\mathrm{[VO]/[V]_{ini}}$ from Table 3 of [4] was used, where $\mathrm{[V]_{ini}}$ is the concentration of vacancies obtained by SRIM, and [VO] is approximately equal to the concentration of primary vacancies, because almost all of them form VO complex in terms of [4]. Corresponding coefficients for 3.5 MeV alpha particles can differ from those for 10 MeV protons. However, we have used the coefficients for protons for approximate calculation of the numbers of primary defects. Substantiation of this is that both alpha particles and protons with the stated energies produce mainly small displacement cascades of few Frenkel pairs or even one pair. Form of cascades, which determines the mentioned coefficients, is not highly different for alpha particles and for protons. The values on $N_i$ obtained by us by means of the two mentioned methods are listed in Table I.

TABLE I
MEAN NUMBERS OF PRIMARY DEFECTS PER ONE ALPHA PARTICLE

<table>
  <thead>
    <tr>
      <th>Defect</th>
      <th>$N_i$, Stillinger-Weber</th>
      <th>$N_i$, Tersoff</th>
      <th>$N_i$, Huhtinen [4]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>V</td>
      <td>38.4</td>
      <td>72.3</td>
      <td>2.26</td>
    </tr>
    <tr>
      <td>I</td>
      <td>34.8</td>
      <td>71.0</td>
      <td>2.26</td>
    </tr>
    <tr>
      <td>$V_2$</td>
      <td>1.15</td>
      <td>2.28</td>
      <td>1.62</td>
    </tr>
    <tr>
      <td>$I_2$</td>
      <td>2.92</td>
      <td>2.92</td>
      <td>1.62</td>
    </tr>
  </tbody>
</table>

We see that the computation of the number of primary V and I defects on the basis of the MD calculations gives significantly larger values than the computation based on the work [4]. It is most likely that such differences are connected with the insufficient description of recombination of defects in the first method. Defects remaining in the simulation cell at the end of the MD calculations are close to each other because they are located within the area of the cascade. Therefore, most of them can recombine during further migration. This recombination can be described on the basis of [13]. If the initial distance between V and I is $R$ and the radius of their recombination is $r$, then their recombination probability is

$$P = r/R \tag{2}$$

Our MD calculations on the basis of the Tersoff potential show that the average size of the cascade (for the mean value of PKA energy of 146 eV) is equal to 3 nm. Therefore, $R$ is approximately equal to 1.5 nm. Taking the value $r = 1.62$ nm from [4], we conclude that the probability $P$ is close to unity. This suggests that the numbers of primary V and I defects calculated by (1) are too high and must be multiplied by factor $1-P$. Everywhere below we will use the numbers of primary defects derived from [4].

### C. Calculation of the numbers of secondary defects

At the third stage we carried out calculations by means of cluster dynamics with an add-on that allows one to find concentrations of all secondary defects depending on time or irradiation fluence (the yield of the neutron generator is assumed constant throughout its operation time). The essence of cluster dynamics is solution of system of differential equations for concentrations of defects of different size (consisting of different numbers of single defects). Structure of equations of cluster dynamics is described in detail e.g. in [14], [15]. Equation for concentration $C_n$ of clusters consisting of $n$ single defects, which was used in our work, has the following form:

$$
\frac{dC_n}{dt} = G_n + \sum_{m} w_{m \to n} C_m - \sum_{m} w_{n \to m} C_n, \tag{3}
$$

where the left-hand side is time derivative of the concentration, and the right-hand side is sum of all kinds of sources and drains. Here $G_n$ is the production rate of clusters of size $n$, $w_{m \to n}$ is transition rate of clusters of size $m$ to clusters of size $n$.

We have realized stochastic approach to cluster dynamics based on the method described in the classical work [16]. Note that cluster dynamics is analogous to chemical kinetics: it solves analogous equations, but clusters of various sizes act as reactants. In [16] a new approach to chemical kinetics was proposed: instead of solution of system of equations for concentrations it was proposed to model a time evolution of number of particles in a finite volume stochastically in the framework of Monte Carlo method.

The approach to chemical kinetics described in [16] is realized in SPPARKS code [17]. If one considers point defects and their clusters as reactants, one may realize cluster dynamics, and that was done in our work. A feature of cluster dynamics is a large number of types of reactants and a large number of reactions. For automation of the setting of reactions a script generator for SPPARKS in Python language was written. All reactions considered in our realization of cluster dynamics can be divided into four types:

1.  Zero order reactions: production of primary defects of each type.
2.  First order reactions: sink of defects to the surface, grain boundaries and dislocations.
3.  Second order reactions: reactions of the form $X + Y \to Z$. These reactions include merging of defects and clusters and their recombination (including recombination of "opposite" defects, for example, single V and single I).
4.  Dissociation reactions of the form $Z \to X + Y$.

Because in silicon not only V and I clusters but also defect-impurity complexes are formed, we have developed an add-on for cluster dynamics introducing additional reactants and additional reactions on the basis of SPPARKS code.

![](./images/814567878014533635_2.jpg)

Fig. 2. The dependencies of concentrations of some of the defects on time and fluence.

The calculations were carried out for initial concentrations of phosphorus $[\text{P}] = 10^{12}$ cm⁻³, carbon $[\text{C}] = 10^{15}$ cm⁻³ and oxygen $[\text{O}] = 5{\cdot}10^{15}$ cm⁻³. We have found that major contribution to the leakage current is made by defects that are inside the Bragg peak, while the contribution of outside defects may be neglected. Also one may neglect contribution of large clusters to the leakage current. In our calculations only the case of continuous irradiation has been simulated with no post-irradiation annealing processes (nevertheless, this is not a limitation of our modeling approach). The results of calculation of concentrations of some defects are shown in Fig. 2. We see that the concentrations depend on the fluence nonlinearly, and at high fluences some concentrations enter the saturation.

[VO] enters the saturation already at the fluence of $4{\cdot}10^{11}\ \text{cm}^{-2}$, while [$V_2$O] and [$V_3$O] at approximately $6{\cdot}10^{12}\ \text{cm}^{-2}$ (not shown in the figure), and reach maximum values [$V_2$O]$_{\text{max}} = 10^{15}\ \text{cm}^{-3}$ and [$V_3$O]$_{\text{max}} = 3.75{\cdot}10^{14}\ \text{cm}^{-3}$. The largest clusters observed in the calculations consist of 15-20 defects, and the concentration of clusters of 15 defects is 6 orders of magnitude less than the concentrations of $V_2$ and $I_2$.

![](./images/814567878014533635_3.jpg)

Fig. 3. Dependence of the leakage current on time and fluence.

## IV. CALCULATION OF THE LEAKAGE CURRENT AND COMPARISON WITH EXPERIMENT

To calculate the detector leakage current at given concentrations of defects and temperature the model described e.g. in [18] was used. In this model the leakage current is induced by carrier emission from the defect levels in the bandgap. Neglecting the Poole-Frenkel effect, the leakage current is calculated by the formula

$$
I = q(\eta_1 P_1 + \eta_2 P_2 + ... ), \tag{4}
$$

where $q$ is the elementary charge, $\eta_i$ is emissivity of defects of the $i$-th type, and $P_i$ is the total number of these defects in the space charge region. Calculation of the emissivity for $V_2$O yields at $T = 300\ \text{K}$ the value $\eta = 480\ \text{s}^{-1}$, whereas for all other defects the value of $\eta$ is much less. For the unirradiated device, the leakage current is determined by "background" carrier lifetime in the detector material ($\approx 1\ \text{ms}$), which gives a generation current $I = 10\ \text{nA}$ at $300\ \text{K}$. In Fig. 3 the dependence of leakage current on time and fluence calculated by (4) for three values of temperature is shown. At the fluence of $10^{13}\ \text{cm}^{-2}$ (not shown in the figure), the leakage current enters the saturation and reaches the values of $14\ \mu\text{A}$, $22\ \mu\text{A}$, and $28\ \mu\text{A}$ at $T = 294$, 300 and $303\ \text{K}$, respectively.

Experimental I-V measurements were performed on both unirradiated and irradiated (on a cyclotron facility, in vacuum, alpha particles impinging on the chip side opposite the p-n junction as in the real device operation conditions) detectors at $T = 300\ \text{K}$. Measured and calculated currents for 250 V reverse bias are compared in Table II. It can be seen that they are in a rather good agreement.

**TABLE II**
LEAKAGE CURRENTS OBTAINED FROM MODELING AND MEASUREMENTS

<table>
  <thead>
    <tr>
      <th>Alpha fluence, $\text{cm}^{-2}$</th>
      <th colspan="2">Leakage current, $10^{-6}\ \text{A}$</th>
    </tr>
    <tr>
      <th></th>
      <th>model</th>
      <th>experiment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.010</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>$10^{12}$</td>
      <td>10.3</td>
      <td>12.5</td>
    </tr>
    <tr>
      <td>$10^{14}$</td>
      <td>22.2</td>
      <td>25.0</td>
    </tr>
  </tbody>
</table>

The developed model can be applied to predict changes in the properties of silicon detectors under alpha particle irradiation at different initial concentrations of impurities in silicon. The model also allows the calculation of the minority charge carriers lifetime depending on the irradiation fluence.

## REFERENCES

[1] G. D. Watkins, "Intrinsic defects in silicon," *Mater. Sci. Semicond. Process.*, vol. 3, pp. 227-235, 2000.

[2] V. A. Kozlov, V. V. Kozlovski, "Doping of semiconductors using radiation defects produced by irradiation with protons and alpha particles," *Semiconductors*, vol. 35, pp. 735-761, 2001.

[3] E. G. Seebauer, M. C. Kratzer, *Charged semiconductor defects*. London: Springer-Verlag London Limited, 2009.

[4] M. Huhtinen, "Simulation of non-ionizing energy loss and defect formation in silicon," *Nucl. Instr. and Meth. A*, vol. 491, pp. 194-215, 2002.

[5] D. Passeri, P. Ciampolini, G. M. Bilei, F. Moscatelli, "Comprehensive modeling of bulk-damage effects in silicon radiation detectors," *IEEE Trans. Nucl. Sci.*, vol. 48, pp. 1688-1693, Oct. 2001.

[6] M. Petasecca, F. Moscatelli, D. Passeri, G. U. Pignatel, "Numerical simulation of radiation damage effects in p-type and n-type FZ silicon detectors," *IEEE Trans. Nucl. Sci.*, vol. 53, pp. 2971-2976, Oct. 2006.

[7] P. Werner, H.-J. Gossman, D. C. Jacobson, U. Güssele, "Carbon diffusion in silicon," *Appl. Phys. Lett.*, vol. 73, pp. 2465-2467, 1998.

[8] URL: http://www.srim.org

[9] M. J. Caturla, T. D. de la Rubia, L. A. Marques, G. H. Gilmer, "Ion-beam processing of silicon at keV energies: a molecular-dynamics study," *Phys. Rev. B*, vol. 54, pp. 16683-16695, 1996.

[10] K. Nordlund, M. Ghaly, R. S. Averback, M. J. Caturla, T. D. de la Rubia, J. Tarus, "Defect production in collision cascades in elemental semiconductors and fcc metals," *Phys. Rev. B*, vol. 57, pp. 7556-7570, 1998.

[11] S. M. Foiles, "Detailed characterization of defect production in molecular dynamics simulations of cascades in Si," *Nucl. Instr. and Meth. B*, vol. 255, pp. 101-104, 2007.

[12] G. Otto, G. Hobler, K. Gartner, "Defect characterization of low-energy recoil events in silicon using classical molecular dynamics simulation," *Nucl. Instr. and Meth. B*, vol. 202, pp. 114-119, 2003.

[13] K. Schroeder, "Low density approximation for diffusion annealing," *Radiation Effects*, vol. 17, pp. 103-118, 1973.

[14] J. Dalla Torre, C. C. Fu, F. Willaime, A. Barbu, J. L. Bocquet, "Resistivity recovery simulations of electron-irradiated iron: kinetic Monte Carlo versus cluster dynamics," *J. Nucl. Mat.*, vol. 352, pp. 42-49, 2006.

[15] D. Xu, B. D. Wirth, M. Li, M. A. Kirk, "Combining in situ transmission electron microscopy irradiation experiments with cluster dynamics modeling to study nanoscale defect agglomeration in structural metals," *Acta Mater.*, vol. 60, pp. 4286-4302, 2012.

[16] D. T. Gillespie, "Exact stochastic simulation of coupled chemical reactions," *J. Phys. Chem.*, vol. 81, pp. 2340-2361, 1977.

[17] URL: http://spparks.sandia.gov

[18] P. Hazdra, K. Brand, J. Rubes, J. Vobecky, "Local lifetime control by light ion irradiation: impact on blocking capability of power P-i-N diode," *Microelectron. J.*, vol. 32, pp. 449-456, 2001.