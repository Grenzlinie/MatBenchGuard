The influence of the electronic specific heat on swift heavy ion irradiation simulations of silicon

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 J. Phys.: Condens. Matter 28 395201

(http://iopscience.iop.org/0953-8984/28/39/395201)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 131.156.224.67
This content was downloaded on 16/08/2016 at 08:35

Please note that terms and conditions apply.

# The influence of the electronic specific heat on swift heavy ion irradiation simulations of silicon

Galvin S Khara, Samuel T Murphy, Szymon L Daraszewicz and Dorothy M Duffy

Department of Physics and Astronomy and The London Centre for Nanotechnology,
University College London, Gower Street, London WC1E 6BT, UK

E-mail: galvin.khara.12@ucl.ac.uk, samuel.murphy@ucl.ac.uk, szymon.daraszewicz.09@ucl.ac.uk and d.duffy@ucl.ac.uk

Received 19 May 2016, revised 14 July 2016
Accepted for publication 18 July 2016
Published 9 August 2016

![](./images/811169899027103745_1.jpg)

## Abstract
The swift heavy ion (SHI) irradiation of materials is often modelled using the two-temperature model. While the model has been successful in describing SHI damage in metals, it fails to account for the presence of a bandgap in semiconductors and insulators. Here we explore the potential to overcome this limitation by explicitly incorporating the influence of the bandgap in the parameterisation of the electronic specific heat for Si. The specific heat as a function of electronic temperature is calculated using finite temperature density functional theory with three different exchange correlation functionals, each with a characteristic bandgap. These electronic temperature dependent specific heats are employed with two-temperature molecular dynamics to model ion track creation in Si. The results obtained using a specific heat derived from density functional theory showed dramatically reduced defect creation compared to models that used the free electron gas specific heat. As a consequence, the track radii are smaller and in much better agreement with experimental observations. We also observe a correlation between the width of the band gap and the track radius, arising due to the variation in the temperature dependence of the electronic specific heat.

Keywords: swift heavy ions, radiation damage, silicon, molecular dynamics, density functional theory, electronic effects

(Some figures may appear in colour only in the online journal)

## 1. Introduction

Swift heavy ions (SHI) are fast heavy projectiles ($\geqslant$1 MeV amu$^{-1}$), capable of depositing a highly localised density of energy in a target. Due to their low interaction cross section with the target nuclei, SHIs lose energy primarily by inelastic collisions with the electrons of the target material. This leads to a cylindrical region of excited electrons perpendicular to the SHI path. The electrons thermalise and energy is transferred to the nuclei via electron–phonon coupling, leading to localised heating and melting. As the energy is dissipated, defect recombination and recrystallisation occur, however, in certain materials a highly disordered region, called an ion track, can remain along the path of the SHI. Ion tracks have been experimentally observed in insulators [1–4], semiconductors [5–7], and metals [8, 9].

The ability to precisely generate nanometre sized cylindrical defect regions in a material has a broad range of applications. For example, track-etched membranes are precisely modified polymers which have been irradiated by SHIs and treated with chemicals [10, 11]. The band gaps of quantum wells and quantum dots can also be precisely modified via irradiation with SHIs [12, 13]. It has also been shown that the critical current density for superconducting in Bi-2212 can be increased by a factor of 150 when irradiated by SHIs and subjected to a magnetic field [14].

There are a number of models that attempt to describe the complex non-equilibrium physics during ion track formation. These include the Coulomb explosion model [15], where the SHI ionises the target. An alternative approach based on struc- tural relaxation was suggested by Bennemann [16]. Here the bonding characteristic of the lattice is determined by the poten- tial energy surface, and in regions of high electronic excitation this potential energy surface is modified. The most widely used model (and most likely hypothesis) is the inelastic thermal spike (iTS) model [17], where the SHI deposits energy into the elec- trons of a material, then this energy is coupled to the lattice via electron–phonon coupling, which subsequently causes the track formation. The most common way that the iTS model is form- ulated is using the two-temperature model (TTM) [18]. In the two-temperature model the electrons and lattice are described by two separate, but interacting, subsystems. This model has been widely used to simulate SHI irradiation in metals [19], semiconductors [7, 20, 21], and insulators [3, 4, 22].

Here we employ a variation of the TTM where we couple the electronic continuum subsystem to an MD supercell to generate a two-temperature molecular dynamics (2T-MD) simulation [23], where energy transfer by the electrons is represented using a heat diffusion equation. The 2T-MD approach allows energy transfer between the electron and ionic subsystem to represent electronic drag and electron–phonon coupling. The model was first devel- oped for metals, although it has also been used to study ion track formation in band gap materials [24–26]. The ability of the model to describe bandgap materials is disputed, as it does not explicitly track the motion of carriers (i.e. electrons and holes) [27, 28]. Furthermore, the traditional free electron gas (FEG) model does not account for the energy required to cross the bandgap.

In this work we propose that through an appropriate para- meterisation of the electronic specific heat the 2T-MD model may be employed for the study of bandgap materials. By cal- culating the electronic temperature dependent electronic heat capacity, $C(T_{\mathrm{e}})$, using density functional theory (DFT), we more accurately account for the band gap. In order to investi- gate the sensitivity of damage to $C_{\mathrm{e}}(T)$ we use three different exchange correlation functionals as the widely used semi-local exchange correlation functionals lead to an underestimation of the bandgap of $\approx$20–30%. We employ a hybrid DFT functional that incorporates exact exchange from Hartree–Fock, which leads to a more accurate density of states (DOS) and hence a more accurate band gap. Using these electronic specific heats we perform 2T-MD simulations of SHI irradiation in silicon and compare the resulting track radii with similar results cal- culated with a specific heat from the commonly used free elec- tron gas model [3, 20, 29]. This is particularly important as the specific heat has been shown to be a key parameter in deter- mining whether defects multiply or anneal in metals [30].

## 2. Methodology

### 2.1. Calculating the electronic specific heat

The electronic specific heat capacity for silicon was found via finite temperature DFT [31, 32] using the Vienna ab initio simulation package (VASP) [33]. Simulations employed the semi-local generalised gradient approximation (GGA) func- tional of Perdew, Burke, Ernzerhof (PBE) [34, 35], and the hybrid Heyd, Scuseria, and Ernzerhof (HSE) [36] and Perdew, Burke, Ernzerhof (PBE0) functionals [37]. Projector aug- mented wave (PAW) pseudo potentials were employed with the plane wave expansion truncated at 400 eV.

<table>
<caption>Table 1. Ground state DFT results of silicon compared with experiment [40, 41].</caption>
<thead>
<tr>
<th>Functional</th>
<th>Lattice parameter (Å)</th>
<th>Band gap (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>PBE</td>
<td>5.469</td>
<td>0.71</td>
</tr>
<tr>
<td>HSE</td>
<td>5.435</td>
<td>1.14</td>
</tr>
<tr>
<td>PBE0</td>
<td>5.430</td>
<td>1.84</td>
</tr>
<tr>
<td>Experiment</td>
<td>5.431</td>
<td>1.10</td>
</tr>
</tbody>
</table>

In all cases a 2 atom Si cell was used, with a $16\times 16\times 16$ Monkhorst–Pack [38] $k$-point grid for the integration of the Brillouin Zone. A Fock exchange grid of $16\times 16\times 16$ was chosen for HSE and PBE0 functionals and the mixing fraction of the Fock exchange for HSE was set to 0.25, with a screening parameter of $0.2\ \mathrm{\mathring{A}}^{-1}$. Results for the ground state properties of these functionals are summarised in table 1. These values are in good agreement with other published results using these functionals [39].

The electronic specific heat, $C_{\mathrm{e}}$, for each functional was calculated using,
$$
C_{\mathrm{e}}(T_{\mathrm{e}})=\frac{\partial U}{\partial T_{\mathrm{e}}}, \tag{1}
$$
where $U$ is the internal energy, and $T_{\mathrm{e}}$ is the electronic temper- ature of the system. An electronic temperature was applied to the system via Fermi–Dirac smearing according to the for- malism of Mermin [42] to an upper limit of 25 000 K. Self consistent field calculations were then carried out from 0 K to 25 000 K in increments of 250 K, and the electronic specific heat was calculated using equation (1).

### 2.2. Two temperature model

As discussed in the introduction SHI irradiation of Si is modelled using 2T-MD. Within the 2T-MD formalism energy transfer by the electrons is represented via heat diffusion equation as shown in equation (2),
$$
\frac{\partial T_{\mathrm{e}}}{\partial t}=D_{\mathrm{e}}(T_{\mathrm{e}}) \nabla^{2} T_{\mathrm{e}}-\frac{G}{C_{\mathrm{e}}(T_{\mathrm{e}})}(T_{\mathrm{e}}-T_{\mathrm{i}})+\frac{1}{C_{\mathrm{e}}(T_{\mathrm{e}})}A(r[v_{\mathrm{ion}}], t), \tag{2}
$$
where $T_{\mathrm{e}}$ and $T_{\mathrm{i}}$ are the electronic and ionic temperatures respectively, $C_{\mathrm{e}}(T_{\mathrm{e}})$ is the electronic specific heat, and $D_{\mathrm{e}}(T_{\mathrm{e}})$ is the electronic diffusivity, which in silicon is $33.6\mathrm{cm}^{2}\ \mathrm{s}^{-1}$ at room temperature [43]. The spatial variation of the elec- tronic diffusivity and electronic specific heat were ignored. We employed the temperature dependent diffusivity of Dufour et al in our simulations [44]. $G$ is the electron–phonon cou- pling term,
$$
G=\frac{3Nk_{\mathrm{B}}}{mV\tau_{p}}, \tag{3}
$$

where $N$ is the number of atoms in the relevant ionic cell, $k_{\mathrm{B}}$ is the Boltzmann constant, $m$ is the mass of the atomic species, $V$ is the volume of the ionic cell, and $\tau_{p}$ is the electron-phonon relaxation time. $\tau_{p}$ was taken to be 0.26 ps, a value obtained from femtosecond optical pump probe reflectivity experiments [45]. $A(r[v_{\text{ion}}], t)$ is a source term corresponding to the energy deposited by the SHI, and has a spatial dependence linked to the ion velocity, $v_{\text{ion}}$, and temporal dependence $t$ described below.

In the 2T-MD model, the electronic subsystem is connected to the ions via a modified Langevin thermostat [23], and the ions evolve according to modified equations of motion,

$$
m_{\mathrm{i}} \frac{\partial \mathbf{v}_{\mathrm{i}}}{\partial t}=\mathbf{F}_{\mathrm{i}}(t)-\gamma_{\mathrm{i}} \mathbf{v}_{\mathrm{i}}+\tilde{\mathbf{F}}_{\mathrm{i}}(t),
\tag{4}
$$

where $m$ and $\mathbf{v}_{\mathrm{i}}$ are the mass and velocity of atom $i$ at time $t$, $\mathbf{F}_{\mathrm{i}}(t)$ is the deterministic force on $i$ due to the interatomic potential. $\gamma_{\mathrm{i}} \mathbf{v}_{\mathrm{i}}$ is the frictional force that represents electronic drag, and $\gamma_{\mathrm{i}}=\tau_{p}^{-1}$. $\tilde{\mathbf{F}}_{\mathrm{i}}(t)$ is a stochastic force which is thermostatted at the electronic temperature. We employed the modified Tersoff potential for Si as derived by Kumagai *et al* [46] as it accurately reproduces the melting temperature, the latent heat of melting, the solid to liquid density change, and amorphous structure from quenched melting, which are all key parameters in the non equilibrium dynamics of SHI irradiation.

The simulations were run using a modified version of DL_POLY4 [47], on a 200 000 atom supercell measuring $271.99 \times 271.99 \times 54.4$ $\mathring{\mathrm{A}}^{3}$ dimension (corresponding to an 8 atom cubic unit cell multiplied by $50 \times 50 \times 10$). This simulation volume was chosen as it ensures all the energy deposited into the electronic subsystem has a corresponding ionic cell to interact with. This MD cell was periodic in all directions to simulate a bulk crystal, and was subdivided into a grid of $25 \times 25 \times 5$ coarse grained ionic temperature voxels (each $\approx 10.86$ $\mathring{\mathrm{A}}^{3}$). A $75 \times 75 \times 5$ electronic temperature voxel grid extends over the MD cell in the $xy$ direction, and this system was solved using a space centred, forward in time Euler method with a timestep of 1 as. The MD system was pre-equilibrated for 200 ps (with a 1 fs timestep) using an NPT ensemble (300 K) Nosé–Hoover thermo- and barostats. After equilibration the MD cell was connected to the continuum electronic system which was also set to 300 K, and the SHI irradiation was simulated for 20 ps (with a 1 fs timestep).

The mean absorption radius of 0.74 nm was found using Bohr’s principle of adiabatic variance [48]. We assume the SHI deposits energy via a spatial Gaussian and temporal exponential distribution with a characteristic deposition time of 1 fs [49, 50] (corresponding to a $\mathrm{C}_{60}$ carbon cluster of a specific ion energy 0.07 MeV $\mathrm{u}^{-1}$). The source term was normalised so its spatial and temporal integration equates to the energy deposited into the electronic system (the electronic stopping power, $S_{\mathrm{e}}$) [28, 49].

## 3. Results and discussion

Figure 1 shows the electronic specific heat for DFT simulations employing the different exchange correlation functionals compared with the free electron gas approximation. If one assumes that hot electrons in a band gap material behave like hot electrons in a metal [51] then the free electron gas model can be applied. For band gap materials this leads to an electronic specific heat $C_{\mathrm{e}}=\frac{3}{2} n_{\mathrm{e}} k_{\mathrm{B}}$, where $n_{\mathrm{e}}$ is the electron number density (taken to be one electron per atom [29]), and $k_{\mathrm{B}}$ is the Boltzmann constant.

![](./images/811169899027103745_2.jpg)

**Figure 1.** Electronic specific heat for Si, calculated using DFT with three different functionals compared to the free electron gas model.

The DFT results show a significant dependence of the specific heat on the choice of exchange correlation functional. As the curvatures of the DOS around the band edges are similar we conclude that the size of the bandgap is the dominant factor determining the specific heat. The larger the band gap, the higher the required electronic temperature for a non-zero internal energy, as the electrons need to first be excited across the band gap before they can subsequently contribute kinematically. Also, the larger the band gap, the lower the electronic specific heat. This can be explained by considering the DOS of our system, for a given amount of energy, a larger band gap results in occupancy of higher energy states, and thus a higher electronic temperature is achieved. Interestingly, at high electronic temperatures the electronic specific heats calculated using the three different functionals converge. These results show band gap contributions can indeed be accounted for within the 2T-MD model.

Figure 2 shows the evolution of electronic and lattice temperatures at the centre of a typical SHI simulation for each $C_{\mathrm{e}}(T_{\mathrm{e}})$. In general the SHI causes the electronic temperature to reach a maximum value in 10 fs, this energy is then transferred to the lattice, which reaches its maximum value within 0.1 ps, and both subsystems reach thermal equilibrium after a few ps. The difference between the temperatures predicted using the free electron gas and DFT specific heats are significant throughout. The FEG reaches a much higher maximum electronic temperature, cools at a slow constant rate, and reaches a significantly lower equilibrium temperature after a few ps. By contrast, the differences between functionals are less pronounced at the beginning and end of the simulation, but the regions where they diverge have a significant impact on the dynamics of the system.

The most striking differences in the temperature profiles for the different functionals occurs when the electronic

![](./images/811169899027103745_3.jpg)

Figure 2. $25\ \text{keV nm}^{-1}$ SHI irradiation temperature evolution of (a) the electronic system (b) the lattice, at the centre of the simulation cell using $C_{\text{e}}(T_{\text{e}})$ calculated with different functionals.

temperature cools to between 20 000 K and 3000 K. As PBE has the highest $C_{\text{e}}(T_{\text{e}})$ in this range, the rate of transfer to the lattice ($G/C_{\text{e}}(T_{\text{e}})$ in equation (2)) is lower, thus electronic energy spreads further from the centre of the track before being transferred to the lattice. Conversely, a larger band gap leads to a lower $C_{\text{e}}(T_{\text{e}})$, the rate of transfer to the lattice is higher, and thus the spatial region where the lattice temperature exceeds the melting threshold is more localised, leading to smaller track radii.

In a typical simulation a defect population is established within 0.1 ps. The number of defects increases as energy diffuses through the cell, reaching a maximum value at 1 ps. The lattice then cools, recrystallises, and a final defect distribution is established within 5 ps. Figures 3(a)–(d) show the evolution of local structure following SHI irradiation. Initially all atoms exhibit a perfect diamond structure (light blue), however, 0.1 ps after initialisation of the SHI there is a localised amorphous region at the centre of the simulation cell. The darker blue represents a denser region of cubic diamond which is due to the rapid expansion of the cylinder of atoms at the core. The black region is a small halo where diamond structure only extends out to the 1st and 2nd nearest neighbours. After 1 ps these compressed regions relax, and by 5 ps the final defect distribution is observed. The Wigner–Seitz defect evolution at the corresponding times are shown in figures 3(e)–(h). The Wigner–Seitz defects were calculated using Voronoi cell analysis [52], if an atom moved from its original Voronoi cell a vacancy was formed, and if an atom moved into an occupied Voronoi cell an interstitial defect was formed.

Figure 4 shows the typical evolution of Wigner–Seitz defects for a low, middle, and high value of electronic stopping power. Each case displays the same qualitative behaviour, the number of defects reaches a maximum within 1 ps, after which about 10% of the defects recombine, and the final defect distribution is formed within 5 ps.

We performed a number of simulations to determine the relationship between the size of the ion track and the energy deposited by the SHI (quantified by the electronic stopping power, $S_{\text{e}}$) for each $C_{\text{e}}(T_{\text{e}})$. We analysed the track distribution in two different ways, via track radius, and number of Wigner–Seitz defects. The track radius was determined by calculating the atomic density of each particle as a function of distance from the centre of the cell using Voronoi cell analysis. Our results suggest that there are two distinct track radii profiles, which depend on the amount of energy deposited. At relatively low stopping powers the track consisted of an overly dense amorphous region, in figure 5 this corresponds to the blue line, which is an ion track of $\approx 18\ \mathring{\text{A}}$. This is consistent with a mechanism whereby an overdense liquid core is created and subsequently quenched to form overdense amorphous Si. By contrast, at higher stopping powers the energy deposition is great enough to eject atoms from the centre of the core. This results in an underdense core, surrounded by an overdense amorphous outer track region (shown by the red line in figure 5, which is an ion track of $\approx 50\ \mathring{\text{A}}$). These different track signatures may be observable in future small angle x-ray scattering (SAXS) experiments on crystalline silicon. Previous SAXS experiments, and the corresponding MD simulations, that have characterised the damage resulting from SHI irradiation of amorphous Si [7] show an overdense core similar to our low stopping power result in figure 5.

Figure 6 shows how the electronic specific heat leads to significantly different final defect distributions and track radii. At $5\ \text{keV nm}^{-1}$ we predict the formation of an ion track with a radius of $16.9\ \mathring{\text{A}}$ using the specific heat determined by the free electron gas model. By contrast, no continuous ion tracks are formed when the specific heats from DFT are used, but there are some isolated vacancy and interstitial defects. Simulations using the free electron gas approximation were only carried out to an $S_{\text{e}}$ of $25\ \text{keV nm}^{-1}$ as higher stopping powers resulted in defect distributions that approached the boundary of our MD cell. For all stopping powers tested the number of defects and the resulting track radii calculated using $C_{\text{e}}(T_{\text{e}})$ from the free electron gas model are substantially greater than when using $C_{\text{e}}(T_{\text{e}})$ determined via DFT.

Figure 6(b) suggests that when DFT is used to parameterise the specific heat, the change in the track radius as a function of

![](./images/811169899027103745_4.jpg)

Figure 3. [0 0 1] ion track morphology at various times during a $25\ \text{keV nm}^{-1}$ SHI simulation. (a)-(d) are coloured according to local structure: light blue represents diamond structure, the darker blue is a region of compressed cubic diamond, black is 1st and 2nd neighbour diamond, and grey amorphous structure, determined via common neighbour analysis. (e)-(h) are Wigner-Seitz defects, blue representing vacancies and red representing interstitials. Both sets of images were created using OVITO [53]. (a) 0.0 ps (b) 0.1 ps (c) 1.0 ps (d) 5.0 ps (e) 0.0 ps (f) 0.1 ps (g) 1.0 ps (h) 5.0 ps.

![](./images/811169899027103745_5.jpg)

Figure 4. Evolution of Wigner-Seitz defects with time for various stopping powers using the electronic specific heat derived with the HSE functional.

![](./images/811169899027103745_6.jpg)

Figure 5. Relative atomic density as a function of distance from the centre of the simulation cell. The black dotted line corresponds to the ion track radius. Blue and red lines show the results from a $10\ \text{keV nm}^{-1}$ and $25\ \text{keV nm}^{-1}$ SHI simulations, using the PBE0 and PBE electronic specific heats respectively. The dotted vertical line marks the track radius of $18\ \mathring{\text{A}}$ for the low stopping power and $50\ \mathring{\text{A}}$ for the high stopping power.

stopping power reproduces the relationship observed in experimental studies of other semiconductors [5-7] and insulators [1-3]. The free electron model, on the other hand, shows a linear relationship between track radius and electronic stopping power. This is because the rate of energy transfer from the electrons to the lattice is constant regardless of electronic temperature, thus the spatial region of atoms which has a temperature higher than the melting threshold increases proportionally to the electronic stopping power.

A clear relationship can be observed between the sensitivity of ion track radii with different electronic specific heats, each with a characteristic density of states (and hence band gap). The larger the band gap, the more resistant the material is to damage (assuming all the other parameters in the model remain the same). An apparent relationship between the threshold stopping powers and the band gap of a semiconductor has been noted previously from experimental observations [3]. This was attributed to an inverse relationship between

![](./images/811169899027103745_7.jpg)
![](./images/811169899027103745_8.jpg)

Figure 6. Defects versus $S_e$. (a) is the total number of Wigner-Seitz defects as a function of stopping power. (b) is the track radius as a function of stopping power. Each data point is the mean value of five repeated simulations, and the error bars correspond to the standard deviation.

the electron mean free path and the band gap, although no physical justification was offered. Here we claim that it is the electronic specific heat, as opposed to the mean free path, that is related to the band gap, and the modified relaxation time for the electron ion energy transfer affects the track radii.

The HSE functional predicts a bandgap in excellent agreement with the experimental value of 1.11 eV [41]. Our track results with this functional also agree well with experimental tracks observed via the irradiation of silicon using $C_{60}$ fullerenes. Our threshold for track creation is lower than experimental observations [54, 55], but this may be explained by the fact that fast monatomic ions deposit energy more widely amongst the targets electrons, leading to less damage. We also note that we have not included the changes in the interatomic interactions due to electronic excitation [56-58], which may influence the results. The effects of these modified interactions will be investigated, using electronic temperature dependent potentials, in future work.

## 4. Conclusion

We have modelled the damage tracks resulting from swift heavy ion irradiation in silicon, using a 2T-MD model, for a range of stopping powers. We found a clear difference in track morphology for low stopping powers, where the track had an overdense core, and high stopping powers, where the tracks had a core shell structure with an underdense core and an overdense shell. We calculated the temperature dependence of the electronic specific heat, an important parameter of the 2T-MD model, using DFT with different functionals. These functionals have characteristic density of states (and thus different band gaps). This leads to distinct temperature dependent specific heats. The lower specific heat associated with larger band gaps resulted in a shorter relaxation time for the electron lattice energy transfer and corresponding smaller track radii. This provides an explanation for the observed dependence of threshold stopping power on bandgap, which has previously been attributed to the mean free path. Simulations using the specific heat with the most accurate band gap give track radii close to the those observed in experiment.

In summary, we have demonstrated that bandgap effects can be introduced into the two temperature model by an accurate representation of the temperature dependence of the electronic specific heat.

## Acknowledgments

GSK acknowledges funding from the European Office of Aerospace Research & Development, STM acknowledges funding from the Leverhulme trust (grant number RPG-2013-331). Via our membership of the UKs HPC Materials Chemistry Consortium, which is funded by EPSRC (EP/L000202), this work made use of the facilities of ARCHER, the UK's national high-performance computing service, which is funded by the Office of Science and Technology through EPSRC's High End Computing Programme. Additional computational resources were provided by the high performance computer cluster GRACE at UCL.

## References

[1] Ishikawa N, Sonoda T, Sawabe T, Sugai H and Sataka M 2013 Nucl. Instrum. Methods Phys. Res. B **314** 180-4

[2] Afra B *et al* 2013 SAXS investigations of the morphology of swift heavy ion tracks in $\alpha$-quartz **25** 045006

[3] Toulemonde M, Dufour C, Meftah A and Paumier E 2000 Nucl. Instrum. Methods Phys. Res. B **166** 903-12

[4] Lu F, Wang J, Lang M, Toulemonde M, Namavar F, Trautmann C, Zhang J, Ewing R C and Lian J 2012 Phys. Chem. Chem. Phys. **14** 12295-300

[5] Colder A, Canut B, Levalois M, Marie P, Portier X and Ramos S M M 2002 *J. Appl. Phys.* **91** 5853-7

[6] Steinbach T, Bierschenk T, Milz S, Ridgway M C and Wesch W 2014 *J. Phys. D: Appl. Phys.* **47** 065301

[7] Bierschenk T *et al* 2013 *Phys. Rev. B* **88** 174111

[8] Dunlop A, Legrand P, Lesueur D, Lorenzelli N, Morillo J, Barbu A and Bouffard S 2007 Europhys. Lett. 15 765-70

[9] Barbu A, Dunlop A, Lesurur D and Averback R S 1991 Europhys. Lett. 15 37-42

[10] Apel P 2003 Nucl. Instrum. Methods Phys. Res. B 208 11-20

[11] Vijay Y K 2009 Indian J. Phys. 83 927-35

[12] Choudhury N, Singh F and Sarma B K 2013 Radiat. Eff. Defects Solids 168 498-503

[13] Devaraju G, Sathish N, Pathak A P, Turos A, Bazzan M, Trave E, Mazzoldi P and Arora B M 2010 Nucl. Instrum. Methods Phys. Res. B 268 3001-4

[14] Wiesner J, Fueß H, Wirth G, Jäger E, Schimpf E, Wagner P, Hillmer F and Adrian H 1994 Phys. C: Supercond. 235-40 2971-2

[15] Fleischer R L, Price P B and Walker R M 1965 J. Appl. Phys. 36 3645-52

[16] Bennemann K H 2004 J. Phys.: Condens. Matter 16 R995-1056

[17] Primak W 1955 Phys. Rev. 98 1854-5

[18] Lifshits I, Kaganov M and Tanatarov L 1960 J. Nucl. Energy-Part A. React. Sci. 12 69-78

[19] Wang Z G, Dufour C, Paumier E and Toulemonde M 1994 J. Phys.: Condens. Matter 6 6733-50

[20] Chettah A, Kucal H, Wang Z, Kac M, Meftah A and Toulemonde M 2009 Nucl. Instrum. Methods Phys. Res. B 267 2719-24

[21] Kamarou A, Wesch W, Wendler E, Undisz A and Rettenmayr M 2006 Phys. Rev. B 73 184107

[22] Wang J, Lang M, Ewing R C and Becker U 2013 J. Phys.: Condens. Matter 25 135001

[23] Duffy D M and Rutherford A M 2007 J. Phys.: Condens. Matter 19 16207

[24] Leino A A, Daraszewicz S L, Pakarinen O H, Nordlund K and Djurabekova F 2015 Europhys. Lett. 110 16004

[25] Pisarev V V and Starikov S V 2014 J. Phys.: Condens. Matter 26 475401

[26] Phillips C L, Magyar R J and Crozier P S 2010 J. Chem. Phys. 133 144711

[27] Klaumuünzer S 2006 Mat.-Fys. Medd. 52 306

[28] Daraszewicz S L and Duffy D M 2013 Nucl. Instrum. Methods Phys. Res. B 303 112-5

[29] Toulemonde M, Assmann W, Dufour C, Meftah A, Studer F and Trautmann C 2006 Mat.-Fys. Medd. K. Dan. Vidensk. Selsk. 52 263

[30] Duffy D M, Itoh N, Rutherford A M and Stoneham A M 2008 J. Phys.: Condens. Matter 20 082201

[31] Hohenberg P and Kohn W 1964 Phys. Rev. 136 B864

[32] Kohn W and Sham L J 1965 Phys. Rev. 140 A1133-8

[33] Kresse G and Furthmüller J 1996 Phys. Rev. B 54 11169-86

[34] Langreth D C and Mehl M J 1983 Phys. Rev. B 28 1809-34

[35] Perdew J P, Burke K and Ernzerhof M 1996 Phys. Rev. Lett. 77 3865-8

[36] Heyd J, Scuseria G E and Ernzerhof M 2003 J. Chem. Phys. 118 8207-15

[37] Paier J, Hirschl R, Marsman M and Kresse G 2005 J. Chem. Phys. 122 234102

[38] Monkhorst H J and Pack J D 1976 Phys. Rev. B 13 5188-92

[39] Paier J, Marsman M, Hummer K, Kresse G, Gerber I C and Angyán J G 2006 J. Chem. Phys. 124 154709

[40] Becker P, Seyfried P and Siegert H 1982 Z. Phys. B: Condens. Matter 48 17-21

[41] Precker J W and da Silva M A 2002 Am. J. Phys. 70 1150

[42] Mermin N D 1965 Phys. Rev. 137 A1441-3

[43] Akkerman A and Murat M 2015 Nucl. Instrum. Methods Phys. Res. B 350 49-54

[44] Dufour C, Khomenkov V, Rizza G and Toulemonde M 2012 J. Phys. D: Appl. Phys. 45 065302

[45] Sabbah A and Riffe D 2002 Phys. Rev. B 66 1-11

[46] Kumagai T, Izumi S, Hara S and Sakai S 2007 Comput. Mater. Sci. 39 457-64

[47] Todorov I T, Smith W, Trachenko K and Dove M T 2006 J. Mater. Chem. 16 1911

[48] Mozumder A 1974 J. Chem. Phys. 60 1145

[49] Toulemonde M, Costantini J, Dufour C, Meftah A, Paumier E and Studer F 1996 Nucl. Instrum. Methods Phys. Res. B 116 37-42

[50] Gervais B and Bouffard S 1994 Nucl. Instrum. Methods Phys. Res. B 88 355-64

[51] Baranov I, Martynenko Y V, Tsepelevich S and Yavlinski Y N 1988 Sov. Phys.-Usp. 31 1015-34

[52] Rycroft C H, Grest G S, Landry J W and Bazant M Z 2006 Phys. Rev. E 74 021306

[53] Stukowski A 2009 Modelling Simul. Mater. Sci. Eng. 18 015012

[54] Toulemonde M, Dural J, Nouet G, Mary P, Hamet J F, Beaufort M F, Desoyer J C, Blanchard C and Auleytner J 1989 Phys. Status Solidi a 114 467-73

[55] Mary P, Bogdanski P, Toulemonde M, Spohr R and Vetter J 1992 Nucl. Instrum. Methods Phys. Res. B 62 391-3

[56] Shokeen L and Schelling P K 2010 Appl. Phys. Lett. 97 151907

[57] Shokeen L and Schelling P K 2011 J. Appl. Phys. 109 073503

[58] Murphy S T, Daraszewicz S L, Giret Y, Watkins M, Shluger A L, Tanimura K and Duffy D M 2015 Phys. Rev. B 92 134110