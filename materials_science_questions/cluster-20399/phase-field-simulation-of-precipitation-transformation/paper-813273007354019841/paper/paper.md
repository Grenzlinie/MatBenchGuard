![](./images/813273007354019841_1.jpg)

Available online at www.sciencedirect.com
SciVerse ScienceDirect

Acta Materialia 60 (2012) 6961-6971

![](./images/813273007354019841_2.jpg)

# Multiscale simulations on the coarsening of Cu-rich precipitates in $\alpha$-Fe using kinetic Monte Carlo, molecular dynamics and phase-field simulations

David Molnar $^{a,b,*}$, Rajdip Mukherjee $^{c,d,*}$, Abhik Choudhury $^{c}$, Alejandro Mora $^{a}$, Peter Binkele $^{a}$, Michael Selzer $^{c,d}$, Britta Nestler $^{c,d}$, Siegfried Schmauder $^{a,b}$

$^{a}$ Institute for Materials Testing, Materials Science and Strength of Materials, University of Stuttgart, Pfaffenwaldring 32, 70569 Stuttgart, Germany
$^{b}$ Stuttgart Research Center of Simulation Technology (SRC SimTech), SimTech Cluster of Excellence, University of Stuttgart, 70569 Stuttgart, Germany
$^{c}$ Institute of Applied Materials, Karlsruhe Institute of Technology (KIT), Haid-und-Neu-Str. 7, 76131 Karlsruhe, Germany
$^{d}$ Institute of Materials and Processes, Kalsruhe University of Applied Sciences, Moltkestrasse 30, 76133 Karlsruhe, Germany

Received 2 July 2012; received in revised form 21 August 2012; accepted 23 August 2012
Available online 13 October 2012

## Abstract
The coarsening kinetics of Cu-rich precipitates in an $\alpha$-Fe matrix for thermally aged Fe-Cu alloys at temperatures above $700\ ^{\circ}\text{C}$ is studied using a kinetic Monte Carlo (KMC) simulation and a phase-field method (PFM). In this work, the KMC approach adequately captures the early stage of the system evolution which involves nucleation, growth and coarsening, while the PFM provides a suitable framework for studying late-stage coarsening at large precipitate volume fraction regimes. Hence, both models complement each other by transferring the results of KMC along with precipitate-matrix interface energies from a broken-bond model to a quantitative PFM based on a grand chemical potential formulation and the CALPHAD database. Furthermore, molecular dynamics simulations provide information on the structural coherency of the precipitates and hence justify the sequential parameter transfer. We show that our PFM can be validated quantitatively for the Gibbs-Thomson effect and that it also predicts the coarsening kinetics correctly. It is found that the kinetics closely follow the LSW (Lifshitz-Slyozov-Wagner) law, whereas the coarsening rate constant increases with an increase in volume fraction of precipitates.
© 2012 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Multiscale; Precipitation; Kinetic Monte Carlo; Molecular dynamics; Phase-field methods

---

### 1. Introduction
$\alpha$-Fe alloyed with Cu among other elements finds application in many areas, e.g. as pipe material in power plants. The alloying with Cu yields an increased flow stress which can be attributed to solid-solution strength- ening and particle strengthening due to the interaction of dislocations with Cu atoms and Cu precipitates within the material, respectively [1,2]. The latter strengthening effect depends on the thermal treatment of the material as well as on the service conditions. At elevated temperatures (above $300\ ^{\circ}\text{C}$), Cu precipitates form within the Fe matrix on a relatively short timescale, yielding first a strengthening of the material. However, as the particles undergo coarsening with time, the failure mechanism due to tensile loading may change, which is undesirable for safety reasons. The computational modelling of the precipitate coarsening behaviour requires an understand- ing of the physical processes on the atomistic scale as well

* Corresponding authors. Addresses: Institute for Materials Testing, Materials Science and Strength of Materials, University of Stuttgart, Pfaffenwaldring 32, 70569 Stuttgart, Germany (D. Molnar), Institute of Applied Materials, Karlsruhe Institute of Technology (KIT), Haid-und- Neu-Str. 7, 76131 Karlsruhe, Germany (R. Mukherjee).
E-mail addresses: david.molnar@imwf.uni-stuttgart.de (D. Molnar), rajdip@gmail.com (R. Mukherjee).

1359-6454/$36.00 © 2012 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.actamat.2012.08.051

as on intermediate length scales in order to predict mate- rial properties on the macroscopic scale.

The classical theory of coarsening of precipitates due to Ostwald ripening was proposed by Lifshitz and Slyozov [3] and Wagner [4], and is hence known as LSW theory. Although the theory is valid for an infinitesimally dilute second-phase particle, both theoretically [5–9] and experi- mentally [10–14] it is found that for higher volume frac- tions of precipitates, the temporal power law is governed by a rate constant larger than predicted by theory. Further- more, the size distribution is broader and has a smaller amplitude compared to the distribution predicted by the theory. In this context, our multiscale approach is justified to predict quantitatively the coarsening kinetics for high volume fractions of precipitates along with coalescence events in Fe–Cu systems.

The precipitation of Cu in $\alpha$-Fe has been observed experimentally [15–17] by means of small-angle neutron scattering as well as by high-resolution tomography, and has also been modelled by applying a kinetic Monte Carlo (KMC) approach [18]. On the other hand, molecular dynamics (MD) simulations have been performed in order to investigate the interactions of edge dislocations with Cu atoms in a solid solution [19] as well as with Cu precipitates [20,21], confirming the experimentally observed strengthen- ing in a Cu-containing alloy [22].

Both KMC and MD simulations are limited to small sample sizes, of the order of tens of nanometers. In order to reach higher length scales and to simulate late-stage coarsening, the phase-field method (PFM) becomes a nec- essary tool. A wide range of phenomena described by phase-field methods can be found in Refs. [23–28]. Several attempts have been made to simulate microstructure evolu- tion using the PFM along with atomistic simulations [29,30], but not for the Fe–Cu precipitation system. Recently, the CALPHAD (CALculation of PHAse Dia- grams) database has been used for the thermodynamic description for PFM in order to quantitatively predict the microstructure evolution in precipitation systems. Most of these studies of coarsening kinetics have been performed in 2-D [31–33] and only a few in 3-D [34–36]. For the Fe– Cu system, limited work has been done using quantitative phase-field modelling and these studies mostly involve the spinodal regime [37–39]. In our study, the integration of KMC with the PFM makes it possible to study precipitate nucleation as well.

In the following section, a sequential multiscale approach is described in detail, followed by the modelling schemes of KMC (Section 3.1), MD (Section 3.2) and PFM (Section 3.3). In Section 4, the results of the simula- tions are discussed. Section 5 closes the paper with conclu- sions derived from the simulation results.

## 2. Multiscale approach

The multiscale approach applied within this study is of a sequential type, i.e. simulation methods are connected via appropriate parameter transfers. In this study, we have cho- sen to transfer the particle arrangement at late KMC precip- itation stages to the PFM. By coupling the two methods sequentially, their advantages can be exploited, circumvent- ing simultaneously their particular disadvantages. Interface energies derived from a broken-bond model (BBM) are fur- ther input data for the PFM. In order to provide structural information of the precipitates, MD relaxation simulations are performed since the KMC approach cannot account for this due to the rigid lattice (see Section 3.2).

## 3. Simulation methods and applied models

### 3.1. Cu precipitation: KMC simulations

The process of Cu precipitation in $\alpha$-Fe is simulated by a KMC method which is based on a thermally activated vacancy diffusion on a rigid body-centred cubic (bcc) crystal lattice model (RLM) [18]. Although in nature Cu has the face-centred cubic structure, Cu clusters with sizes smaller than 2 nm are coherently embedded on $\alpha$-Fe lattice sites [40,41], justifying the RLM. The KMC simulation used in this study was first proposed by Soisson et al. [18]. A detailed description can be found in Refs. [18,42]. As start- ing configuration of $L = 128$ lattice constants yields $N = 2L^3 = 4,194,304$ lattice sites and a cubic box with an edge length of 36.7 nm. The box surfaces have normals in the $\{100\}$ directions and periodic boundary conditions are set in all directions. Fe atoms are replaced randomly by Cu atoms to obtain Fe–Cu solid solutions with 1, 2, 5 and 10 at.% Cu, respectively. An empty site represents a sin- gle vacancy and the annealing temperature is set to $700\ ^{\circ}\text{C}$.

The chemical binding between atoms is described by first- and second-nearest neighbour pair interactions $\varepsilon_{\text{Fe-Fe}}^{(i)}$, $\varepsilon_{\text{Cu-Cu}}^{(i)}$ and $\varepsilon_{\text{Fe-Cu}}^{(i)}$ with $i \in \{1,2\}$, where $i$ denotes the $i$th-nearest neighbour (see Fig. 1). The energies $\varepsilon_{\text{Fe-Fe}}^{(i)}$ and $\varepsilon_{\text{Cu-Cu}}^{(i)}, i \in \{1,2\}$ were estimated from the cohesive energies of the pure metals assuming $\varepsilon_{\text{Fe-Fe}}^{(2)} = \varepsilon_{\text{Fe-Fe}}^{(1)}/2$ and $\varepsilon_{\text{Cu-Cu}}^{(2)} = \varepsilon_{\text{Cu-Cu}}^{(1)}/2$ (see also Ref. [43]). The thermally activated position exchange between the vacancy V and a neighbouring atom A (with A = Fe or Cu) is given by the jump frequencies:

$$
\Gamma_{\text{A,V}} = v_{\text{A}} \exp\left(-\frac{\Delta E_{\text{A,V}}}{\text{k}_{\text{B}}T}\right), \tag{1}
$$

with $T$ and $\text{k}_{\text{B}}$ being the temperature and the Boltzmann constant, respectively. $v_{\text{A}}$ denotes the attempt frequency, which is estimated using the diffusion constants of the pure metals. The activation energies for migration, which de- pend on the local configuration, are given by:

$$
\Delta E_{\text{A,V}} = E_{\text{SP,A}} - \sum_{X} \varepsilon_{\text{A-X}} - \sum_{Y} \varepsilon_{\text{V-Y}}, \tag{2}
$$

where $E_{\text{SP,A}}$ is the energy at the saddle-point between A and V, $\varepsilon_{\text{A-X}}$ are the interaction energies of the first- and sec- ond-nearest neighbours of A (X atoms), and $\varepsilon_{\text{V-Y}}$ are the

![](./images/813273007354019841_3.jpg)

Fig. 1. Schematic representation of the bcc lattice and the interaction energies used in the model (Fe = black, Cu = blue, vacancy = yellow). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

binding energies between the vacancy and its first-nearest neighbours (Y atoms) (see Fig. 1). For each first-nearest neighbour of the vacancy V, the jump frequencies $\Gamma_{1},...,\Gamma_{8}$ are calculated. Applying a rejection-free resi- dence time algorithm [1,18], one of the eight weighted jump possibilities is selected. This procedure is repeated over $10^{11}$ times during the simulation of precipitation. The real tem- poral scale is obtained from:

$$
t_{\text {real }}=\left(\frac{c_{\mathrm{V}, \mathrm{sim}}}{c_{\mathrm{V}, \text { real }}}\right) t_{\mathrm{MC}}, \text { with } t_{\mathrm{MC}}=\left(\sum_{j=1}^{8} \Gamma_{j}\right)^{-1}, \quad(3)
$$

where $c_{V, sim}$ and $c_{V, real}$ denote the vacancy concentrations in the simulation and in the real material, respectively. $t_{MC}$ is the average residence time. The energetic parameters of the KMC simulations are listed in Ref. [44]; these, in turn, are based on Refs. [43,45-47].

### 3.2. Structural coherency: MD simulations

In order to provide information on the coherency of the embedded Cu precipitates, MD relaxation simulations are carried out using the IMD (ITAP Molecular Dynamics) code [48] which allows for massively parallel computations, yielding elastic constants, stress and pressure tensors for relaxed structures. For metals, embedded atom method (EAM) potentials describe the atomic interactions as they include an additional embedding term, besides pair interac- tions $\phi_{i j}$, accounting for the local electron charge density in the lattice, i.e.

$$
V=\frac{1}{2} \sum_{i \neq j} \phi_{i j}\left(r_{i j}\right)+\sum_{i} U_{i}\left(n_{i}\right) \quad \text { with } \quad n_{i}=\sum_{i \neq j} \rho_{i j}\left(r_{i j}\right), \quad(4)
$$

where $U_{i}$ describes the energy of embedding atom $i$ in a density $n_{i}$, which is the sum of contributions $\rho_{j}$ from neigh bours $j$ at distances $r_{i j}$. To describe the Fe-Cu system, EAM potential the recently published by Bonny et al. [49] is applied. Starting from a lattice where all Fe and Cu atoms have the same lattice constant, i.e. the lattice constant of Fe, the structure is relaxed to $T \approx 0 \mathrm{~K}$ (15,000 MD steps with 2 fs per step). During relaxation, the Cu atoms tend to move into an energetically preferred configuration. In order to give the atoms more time to do so, the structure can be heated up to 300 K (50,000 MD steps) and kept at this temperature for another 50,000 MD steps before relaxation by applying the NpT ensemble (constant number of particles, constant pressure and tem- perature). In any case, the surrounding $\alpha$-Fe matrix will af- fect their relaxation depending on the size of the Cu precipitate. The results will be discussed in Section 4.2.

### 3.3. Particle coarsening: PFM

#### 3.3.1. Model description

The PFM applied for the investigation of precipitation in the Fe-Cu system is based on the grand-potential func- tional [50]:

$$
\Omega(T, \boldsymbol{\mu}, \boldsymbol{\phi})=\int_{\Omega}\left(\Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})+\left(\epsilon \tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})+\frac{1}{\epsilon} \tilde{w}(\boldsymbol{\phi})\right)\right) d \Omega,
$$

where $\Omega$ is the total grand potential, $\Psi$ is the grand chem ical potential density, $T$ is the temperature, $\boldsymbol{\mu}$ is the chemi cal potential, $\boldsymbol{\phi}=\phi_{\alpha}, \phi_{\beta} \ldots N$ is the phase-field vector consisting of the N phase-field variables and $\epsilon$ is the inter- face width. The energy densities $\tilde{a}$ and $\tilde{w}$ together represent the interface energy of the system, where the former is the gradient energy and the latter the interface potential. The phase evolution is determined by the phenomenological minimization of the grand potential functional.

The concentration fields are obtained by a mass conser- vation equation for each concentration field $c_{i}$, from the set of $K-1$ independent concentration variables, $K$ being the number of components in the system. The evolution equa- tion for the N phase-field variables $(\phi_{\alpha}, \alpha=1,..., N)$ can be written as:

$$
\begin{aligned}
\tau \epsilon \frac{\partial \phi_{\alpha}}{\partial t}= & \epsilon\left(\nabla \cdot \frac{\partial \tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})}{\partial \nabla \phi_{\alpha}}-\frac{\partial \tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})}{\partial \phi_{\alpha}}\right)-\frac{1}{\epsilon} \frac{\partial \tilde{w}(\boldsymbol{\phi})}{\partial \phi_{\alpha}} \\
& -\frac{\partial \Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})}{\partial \phi_{\alpha}}-\Lambda,
\end{aligned}
$$

where $\Lambda$ is the Lagrange parameter maintaining the con- straint $\sum_{\alpha=1}^{N} \phi_{\alpha}=1$. The gradient energy density $\tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})$ has the form:

$$
\tilde{a}(\boldsymbol{\phi}, \nabla \boldsymbol{\phi})=\sum_{\substack{\alpha, \beta=1 \\(\alpha<\beta)}}^{N, N} \gamma\left[a_{c}\left(q_{\alpha \beta}\right)\right]^{2}\left|q_{\alpha \beta}\right|^{2},
$$

where $q_{\alpha \beta}=\left(\phi_{\alpha} \nabla \phi_{\beta}-\phi_{\beta} \nabla \phi_{\alpha}\right)$ is a normal vector to the $\alpha \beta$ interface. $a_{c}\left(q_{\alpha \beta}\right)$ describes the anisotropy of the evolving

phase boundary, which for the studies in the present investigation have been assumed to be $a_c(q_{\alpha \beta})=1$ for modelling isotropic systems. The obstacle type potential $\tilde{w}(\boldsymbol{\phi})$, which was also previously described in Ref. [51,52], can be written as:
$$
\tilde{w}(\boldsymbol{\phi})=\frac{16}{\pi^{2}} \sum_{\substack{\alpha, \beta=1 \\(\alpha<\beta)}}^{N, N} \gamma \phi_{\alpha} \phi_{\beta},
$$
where $\gamma$ is the interface energy. The parameter $\tau$ in Eq. (5) is written as: $\frac{\sum_{\alpha<\beta}^{N, N} \tau_{\alpha \beta} \phi_{\alpha} \phi_{\beta}}{\sum_{\alpha<\beta}^{N, N} \phi_{\alpha} \phi_{\beta}}$, where $\tau_{\alpha \beta}$ is the relaxation constant of the $\alpha \beta$ interface. It is chosen in a manner such that the interface kinetics vanishes [50]. The evolution equation for the concentration fields can be derived as:
$$
\frac{\partial c_{i}}{\partial t}=\nabla \cdot\left(\sum_{j=1}^{K-1} M_{i j}(\boldsymbol{\phi}) \nabla \mu_{j}\right).\qquad(6)
$$

Here, $M_{i j}(\phi)$ is the mobility of the interface formulated by an interpolation of the individual phase mobilities as:
$$
M_{i j}(\boldsymbol{\phi})=\sum_{\alpha=1}^{N-1} M_{i j}^{\alpha} g_{\alpha}(\boldsymbol{\phi}).
$$

Each of the $M_{i j}^{\alpha}$ is defined using the expression:
$$
M_{i j}^{\alpha}=D_{i j}^{\alpha} \frac{\partial c_{i}^{\alpha}(\boldsymbol{\mu}, T)}{\partial \mu_{j}}.
$$

The function $g_{\alpha}(\phi)$ interpolates the mobilities. $D_{i j}^{\alpha}$ are the interdiffusivities in each phase $\alpha$. Both the evolution equations (Eqs. (5) and (6)) require information about the chemical potential $\boldsymbol{\mu}$.

We write the grand potential density $\Psi$, as an interpolation of the individual grand potential densities $\Psi_{\alpha}$, where $\Psi_{\alpha}$ are functions of the chemical potential $\boldsymbol{\mu}$ and of the temperature $\mathrm{T}$ in the system:
$$
\Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})=\sum_{\alpha=1}^{N} \Psi_{\alpha}(T, \boldsymbol{\mu}) h_{\alpha}(\boldsymbol{\phi}) \quad \text { with }\qquad(7)
$$

$$
\Psi_{\alpha}(T, \boldsymbol{\mu})=f_{\alpha}\left(c^{\alpha}(\boldsymbol{\mu}), T\right)-\sum_{i=1}^{K-1} \mu_{i} c_{i}^{\alpha}(\boldsymbol{\mu}, T),
$$
where $f_{\alpha}(c^{\alpha}(\mu), T)$ is the free energy density of the phase $\alpha$. The concentration $c_{i}^{\alpha}(\mu, T)$ is an inverse of the function $\mu_{i}^{\alpha}(c, T)$ for every phase $\alpha$ and component $i$. From Eq. (7) the following relation can be derived:
$$
c_{i}=\sum_{\alpha=1}^{N} c_{i}^{\alpha}(\boldsymbol{\mu}, T) h_{\alpha}(\boldsymbol{\phi}),\qquad(8)
$$
using $\frac{\partial \Psi(T, \boldsymbol{\mu}, \boldsymbol{\phi})}{\partial \mu_{i}}=-c_{i}$.

### 3.3.2. Calibration of CALPHAD data
For the Fe-Cu system, we reduce the system to a two- phase binary system where the independent concentration is identified by $c=c_{F e}$. Similarly, we reduce the chemical potential vector $\boldsymbol{\mu}$ to $\mu$, which defines an independent chemical potential with respect to Fe. The phase-field vector contains only two components: $\phi=(\phi_{1}, \phi_{2})$. We start the construction of free energies of the respective phases with the following type of expressions for the free energies:
$$
f^{\alpha}(T, c)=A^{\alpha}(T) c^{2}+B^{\alpha}(T) c+E^{\alpha}(T),
$$
where the coefficients $A^{\alpha}(T), B^{\alpha}(T)$ and $E^{\alpha}(T)$ are functions of temperature T. By using a polynomial formulation, we aim to fit a simplified form for the free energies utilizing the data obtained from the CALPHAD database. We can determine the terms $A^{\alpha}(T)$ as $\frac{\partial^{2} f^{\alpha}}{\partial c^{2}}|_{c_{e q}} \equiv \frac{1}{V_{m}} \frac{\partial^{2} G^{\alpha}}{\partial c^{2}}|_{c_{e q}}$, computed at the equilibrium concentration of the phase at the temperature T, where $G^{\alpha}(T, c)$ is the free energy function obtained from CALPHAD. Next we derive the chemical potential $\mu_{e q}=\frac{1}{V_{m}} \frac{\partial G^{\alpha}}{\partial c}|_{c_{e q}}$ from the database and compute $B^{\alpha}(T)$ by equating the first derivative of the constructed free energies to the chemical potential, giving:
$$
B^{\alpha}(T)=\mu_{e q}-2 A^{\alpha}(T) c_{e q}.
$$

The only term left out is $E^{\alpha}(T)$, which is fitted by equating it to the grand potential, which yields:
$$
E^{\alpha}(T)=\Psi_{e q}-A^{\alpha}(T) c_{e q}^{2},
$$
with $\Psi_{e q}=\frac{1}{V_{m}}(G^{\alpha}(T, c_{e q})-\mu_{e q} c)$. With these equations we can adequately fit all the terms in the free energies at the given temperature T. For a non-isothermal description, it is essential to derive the equations in the neighbourhood of the temperature one is simulating and perform a fitting in the temperature space. In most cases, a linear temperature fit suffices. The chemical potential can be derived in terms of the concentration $c$ and volume fractions $\phi_{1}, \phi_{2}$ of the phases by using the relation (8). The phase concentrations can be written as functions of the chemical potential as $c^{\alpha}(\mu, T)=\left(\frac{\mu-B^{\alpha}(T)}{2 A^{\alpha}(T)}\right)$. Using the constraint in Eq. (8), the following relation for $\mu$ derives:
$$
\mu=\frac{c+\sum_{\alpha=1}^{N} \frac{B^{\alpha}(T) h_{\alpha}(\boldsymbol{\phi})}{2 A^{\alpha}(T)}}{\sum_{\alpha=1}^{N} \frac{h_{\alpha}(\boldsymbol{\phi})}{2 A^{\alpha}(T)}}.\qquad(9)
$$

This value of $\mu$ is used both in the evolution equations for the phase-field and in the concentration equations.

### 3.3.3. Mobilities for diffusion
To derive the mobilities, we require the second derivatives of the free energies with respect to the concentrations. This can be realized through the diffusion equation for a binary alloy, written as:
$$
\frac{\partial c^{\alpha}}{\partial t}=\nabla \cdot\left(M^{\alpha} \nabla \mu\right),
$$
where $M^{\alpha}$ is defined as $D \frac{\partial c^{\alpha}}{\partial \mu}$, in order to derive Fick's law in the bulk. Taking the partial derivative of $c^{\alpha}(\mu, T)$ yields:
$$
\frac{\partial c^{\alpha}}{\partial \mu}=\frac{1}{2 A^{\alpha}(T)}.
$$

## 4. Simulation results

### 4.1. KMC simulations and the BBM

The KMC simulations have been performed as explained in Section 3.1 for 1, 2, 5 and 10 at.% Cu. At an annealing temperature of 700 °C, $6 \cdot 10^{11}$ KMC steps yield the formation of Cu clusters within the $\alpha$-Fe matrix. Fig. 2a shows that at the beginning of the ageing process a large number of particles forms in relatively short time due to the high annealing temperature. Hence, these clusters contain only small amounts of Cu atoms, i.e. their mean radius is small. After reaching a maximum, the number of particles decreases again. Nevertheless, the mean radius increases (Fig. 2b), a fact that can be attributed to Ostwald ripening, i.e. to the coarsening of particles. Since at the high temperatures considered here, there are almost no clusters for the case of 1 at.% Cu, the corresponding data are not considered in the following. With the KMC method, precipitates with a mean radius of 1.5 nm can be obtained in a reasonable amount of computing time (O (days)). However, reaching mean particle radii of a couple of nanometers would increase the computation time tremendously, justifying the application of PFM in the coarsening regime. Fig. 3a shows the atomic configurations at two different ageing times where “peak” denotes the states with the maximum number of particles (peaks in Fig. 2a) and “end” denotes the end states of the KMC simulations for 2, 5 and 10 at.% Cu, respectively.

Since at the peak position only small clusters have formed, they are hardly visible among the completely solved Cu atoms. In contrast, at the end of the simulation the precipitates are clearly visible. At this point, the remaining matrix has already reached thermal equilibrium, i.e. almost no further nucleation is expected and Ostwald ripening can be considered as the dominant precipitation process. Transferring information from KMC to PFM can be done in two ways. One possibility is to transfer the whole atomic configuration, i.e. the positions of all Cu atoms, at certain precipitation states to PFM simulations. By this means, no information is lost. The other way is to transfer statistical information on the atomic configuration at certain precipitation states, i.e. fitted distance distributions and radius distributions as shown in Fig. 3b,c. This study provides a means to validate transfer of an identical particle arrangement, and hence is very useful for performing large-length-scale simulations with the PFM.

### 4.1.1. Interface energies: BBM

In order to obtain the interface energy needed in the PFM simulations, the BBM is applied [53,54]. Within this model, the first- and second-nearest neighbours are considered and all atoms contribute to the interface energy whose coordination number changes when inserting an interface. Deriving the interface energies for interfaces oriented in the [100], [110] and [111] directions without relating them to a specific interface area reads:

$$
E_{[100]}^{int}=\frac{1}{2}\left(-4 \varepsilon_{\mathrm{AA}}^{1}-2 \varepsilon_{\mathrm{AA}}^{2}+8 \varepsilon_{\mathrm{AB}}^{1}+4 \varepsilon_{\mathrm{AB}}^{2}-4 \varepsilon_{\mathrm{BB}}^{1}-2 \varepsilon_{\mathrm{BB}}^{2}\right) \quad(10)
$$

$$
E_{[110]}^{int}=\frac{1}{2}\left(-2 \varepsilon_{\mathrm{AA}}^{1}-2 \varepsilon_{\mathrm{AA}}^{2}+4 \varepsilon_{\mathrm{AB}}^{1}+4 \varepsilon_{\mathrm{AB}}^{2}-2 \varepsilon_{\mathrm{BB}}^{1}-2 \varepsilon_{\mathrm{BB}}^{2}\right) \quad(11)
$$

$$
E_{[111]}^{int}=\frac{1}{2}\left(-5 \varepsilon_{\mathrm{AA}}^{1}-6 \varepsilon_{\mathrm{AA}}^{2}+10 \varepsilon_{\mathrm{AB}}^{1}+12 \varepsilon_{\mathrm{AB}}^{2}-5 \varepsilon_{\mathrm{BB}}^{1}-6 \varepsilon_{\mathrm{BB}}^{2}\right).
\tag{12}
$$

Eqs. (10) and (11) can also be found in Ref. [55]. Calculating the interface energies using the activation energies from the KMC simulations (see Section 3.1) yields the interface energies shown in Table 1. Thus the preferred interfaces of Cu clusters are {110} interfaces. This is in very good agreement with results that can be found in Refs. [18,42].

### 4.2. MD simulations

From experiments [40,41] it is known that small Cu clusters (<2 nm) are coherently embedded in the $\alpha$-Fe matrix, while bigger clusters undergo a structural change, i.e. bcc $\rightarrow$ 9R $\rightarrow$ 3R $\rightarrow$ fcc [40,41]. In this study, precipitates with radii from 2 to 14 lattice constants, i.e. with radii ranging from 0.57 to 4.00 nm are analysed in order to provide qualitative information on the necessity of embedding the structural transition into the PFM simulations. Therefore, each precipitate is sufficiently relaxed according to the modelling scheme described in Section 3.2. After

![](./images/813273007354019841_4.jpg)

Fig. 2. (a) Number of particles and (b) their mean radius, as a function of thermal ageing time. In the case of 1 at.% Cu, almost no particles form, making statistical analysis inaccurate. Therefore, the 1 at.% Cu KMC results are not further considered.

![](./images/813273007354019841_5.jpg)

Fig. 3. (a) Arrangement of Cu atoms at two distinct times for 2, 5 and 10 at.% Cu. Up to the point at which the number of particles reaches the maximum values (see Fig. 2), i.e. at the "peak" positions, very small clusters have formed and the resulting images looks nearly like solid solutions. At the "end" of the simulation, several large particles (radii > 1 nm) have formed, while the remaining solid solution is in thermal equilibrium. Fitted Gaussians represent the distance distributions (b) in lattice constants ($a=0.2867$ nm) and the "peak" positions of the radius distributions (c) for 2, 5 and 10 at.% Cu, whereas LSW distributions are assumed at the "end" positions.

Table 1
Interface energies of Fe-Cu interfaces for different orientations obtained
by evaluating Eqs. (10)-(12) for A=Fe and B=Cu. By relating the
calculated interface energies to the orientation-dependent areas per atom,
the interface energies per unit area are obtained.

<table>
<thead>
  <tr>
    <th colspan="4">Interface energies</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>orientation</td>
    <td>[100]</td>
    <td>[110]</td>
    <td>[111]</td>
  </tr>
  <tr>
    <td>$E^{int}$ [J]</td>
    <td>0.248</td>
    <td>0.149</td>
    <td>0.396</td>
  </tr>
  <tr>
    <td>area per atom</td>
    <td>$\mathrm{a}^2$</td>
    <td>$\frac{\sqrt{2}}{2}\mathrm{a}^2$</td>
    <td>$\sqrt{3}\mathrm{a}^2$</td>
  </tr>
  <tr>
    <td>$\gamma\left[\frac{\mathrm{J}}{\mathrm{m}^2}\right]$</td>
    <td>0.483</td>
    <td>0.410</td>
    <td>0.447</td>
  </tr>
</tbody>
</table>

relaxation, the neighbours of each atom within a certain distance are counted. For the bcc structure, a cut-off distance between the second- (0.2855 nm) and third- (0.4038 nm) nearest neighbour of the corresponding atom is an appropriate choice, as the first- (0.2473 nm) and second-nearest neighbours lie very close to each other. In a perfect bcc crystal, the counting would yield 14 nearest neighbours ($\mathrm{NN}=14$) in total for each atom, i.e. 8 first- and 6 second-nearest neighbours. Visualizing the relaxed structures, atoms with $\mathrm{NN}=14$ are shown as red points (see Fig. 4). Deviations are shown as spheres. The colouring is explained in Table 2. The visualization shows that small precipitates ($r\leqslant4$ lattice constants) are coherently embedded within the $\alpha$-Fe matrix, whereas bigger precipitates show severe deviations in their interiors. However, the surfaces remain approximately in the bcc structure, i.e. the coordination number of surface atoms does not change. Hence, the transition from bcc to fcc within the clusters does not have to be taken into account in this first coupling of KMC and PFM simulations and the precipitates in the PFM simulation can be assumed as perfectly coherent.

### 4.3. PFM simulations

#### 4.3.1. Data transfer to the PFM

We use a quantitative PFM based on the grand chemical potential formulation (described in Section 3.3). The model parameters used for our simulations are listed in their dimensional form in Table 3. As described in Section 4.1, the size and location of each precipitate cluster obtained in the KMC simulations are transferred as input for the PFM simulations. In PFM simulations, we use a computational box of $128^3$ grid points where the grid spacing $\Delta x$ is equal to the lattice constant resulting in the same system size as used for the KMC simulation described in Section 3.1. Assuming isothermal ageing conditions, the free energy for the $\alpha$-Fe-Cu system at 1100 K (827 °C) is obtained from the CALPHAD database. We fit this free energy data to the simplified form of the free energy functions using the procedure described in Section 3.3.2 and calculate the chemical potential $\mu$, which is the driving force for diffusion, using Eq. (9).

In our system, the compositions of equilibrium Cu-rich precipitates and Fe-rich matrix are very close to pure Cu

![](./images/813273007354019841_6.jpg)

Fig. 4. Coherency of the precipitates after relaxation at regions close to the surface. The radii range from 0.57 nm (2 lattice constants) to 4.00 nm (14 lattice constants) where the lattice constant of Fe is taken [49,56]. Small precipitates are perfectly coherent while deviations develop in bigger spheres. Nevertheless, at the precipitates' surfaces the deviations remain small. This behaviour is also found if the structure is kept at 300 K for some time before relaxation (14, 300 K). Thus, the structural transition does not necessarily have to be incorporated into the PFM simulations in this study.

Table 2
Atom colouring with respect to the number of atoms within a specified cut-off radius $r_{\mathrm{c}}$. In bcc crystals, $NN=14$ neighbours have to be found. Deviations ($NN\neq 14$) indicate defects within the single crystal. An additional identification of atoms with $NN=12$ neighbours is due to the fact that the corresponding fcc structure would have 12 neighbours within $r_{\mathrm{c}}$.

<table>
<thead>
<tr>
<th>Atom type</th>
<th>Number of neighbours</th>
<th>Colour</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu</td>
<td>$NN=14$</td>
<td>Red</td>
</tr>
<tr>
<td>Cu</td>
<td>$NN&lt;14$ &amp; $n\neq 12$</td>
<td>Orange</td>
</tr>
<tr>
<td>Cu</td>
<td>$NN&gt;14$</td>
<td>Purple</td>
</tr>
<tr>
<td>Cu</td>
<td>$NN=12$</td>
<td>Yellow</td>
</tr>
</tbody>
</table>

Table 3
Parameters used in the PFM simulations. All the parameters are defined in Section 3.3.

<table>
<thead>
<tr>
<th>Parameters</th>
<th>Values</th>
<th>Parameters</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>$A^{\alpha}$</td>
<td>$1.71\times 10^{11}\ \mathrm{J\ m^{-3}}$</td>
<td>$\tau$</td>
<td>$6.89\times 10^{18}\ \mathrm{J\ m^{-4}}$</td>
</tr>
<tr>
<td>$A^{\beta}$</td>
<td>$1.39\times 10^{11}\ \mathrm{J\ m^{-3}}$</td>
<td>$D$</td>
<td>$10^{-16}\ \mathrm{m^{2}\ s^{-1}}$</td>
</tr>
<tr>
<td>$B^{\alpha}$</td>
<td>$-3.33\times 10^{11}\ \mathrm{J\ m^{-3}}$</td>
<td>$\epsilon$</td>
<td>$7.0\times 10^{-10}\ \mathrm{m}$</td>
</tr>
<tr>
<td>$B^{\beta}$</td>
<td>$-6.43\times 10^{9}\ \mathrm{J\ m^{-3}}$</td>
<td>$\gamma$</td>
<td>$0.41\ \mathrm{J\ m^{-2}}$</td>
</tr>
<tr>
<td>$E^{\alpha}$</td>
<td>$1.13\times 10^{11}\ \mathrm{J\ m^{-3}}$</td>
<td>$\Delta x$</td>
<td>$2.8665\times 10^{-10}\ \mathrm{m}$</td>
</tr>
<tr>
<td>$E^{\beta}$</td>
<td>$-5.04\times 10^{10}\ \mathrm{J\ m^{-3}}$</td>
<td>$\Delta t$</td>
<td>$5\times 10^{-5}\ \mathrm{s}$</td>
</tr>
</tbody>
</table>

and pure Fe, respectively. From the BBM calculations (see Table 1), it is found that the lowest interface energy between a Cu cluster and the surrounding Fe matrix, among several possible interfaces, is $0.410\ \mathrm{J\ m^{-2}}$ ([110] interface). We use this interface energy value as a representative and approximated input parameter for the PFM simulations. Internal structural changes within the precipitates as discussed in Section 4.2 may affect the coarsening kinetics only towards the end of the simulation (mean radius $>$3 nm) when distortions get more severe. Hence, in the present PFM simulations we assume the absence of elastic strain fields, which will be incorporated in our future study.

In the PFM, the atomic mobility $M$ can be derived from the interdiffusivity $D$ (described in Section 3.3.3). $D$ is calculated from the self-diffusivity values of each component using Darken's equation:

$$
D=X_{Fe}D_{Cu}^{*}+X_{Cu}D_{Fe}^{*}\approx 10^{-16}\ \mathrm{m^{2}\ s^{-1}},\tag{13}
$$

where $D_{Cu}^{*}$ and $D_{Fe}^{*}$ are the self-diffusivities, and $X_{Cu}$ and $X_{Fe}$ are the mole fractions for Cu and Fe, respectively. Self-diffusivities of Fe and Cu in $\alpha$-Fe as a function of temperature are reported in the literature [57,58]. We calculate the value of $D$ at 1100 K from these available experimental data using Eq. (13).

### 4.4. Phase-field results

The equilibrium compositions of precipitate and matrix in the Fe-Cu system at a particular temperature across a flat interface can be calculated using the tie lines from the free energy CALPHAD data. These compositions change from their equilibrium values across a curved interface due to the Gibbs-Thomson effect. This shift in the surrounding matrix composition provides the driving force for precipitate coarsening. Phase-field models can adequately capture the Gibbs-Thomson effect for the precipitate-matrix microstructure [59,60]. Therefore, it is an ideal tool for studying coarsening phenomena. In our

three-dimensional domain, the precipitates are nearly spherical because of the isotropic interface energy. The shift in composition at the precipitate side $\Delta c^p$ is given by:
$$
\Delta c^{p}=\frac{2 \gamma \kappa}{\xi_{p}\left(c_{e q}^{p}-c_{e q}^{m}\right)},\qquad(14)
$$
where
$$
\xi_{p}=\left(\frac{\partial^{2} f^{\alpha}}{\partial c^{2}}\right)_{p p t}=2 A^{\alpha}(T),
$$
and the shift in composition at the matrix side $\Delta c^m$ follows as:
$$
\Delta c^{m}=\left(\xi_{p} / \xi_{m}\right) \Delta c^{p}.
$$

In the above equations, $\kappa$ is the interface curvature (inverse of radius), $c_{eq}^p$ and $c_{eq}^m$ are the equilibrium compositions across a flat interface at the precipitate and the matrix side, respectively, and $\gamma$ is the interface energy.

Phase-field simulations are performed with a single spherical precipitate in a three-dimensional domain for three different precipitate sizes. For each simulation, we use the equilibrium precipitate composition obtained from the free energy function using a common tangent construction, with a very small supersaturation in the matrix. During the simulation, the precipitate and matrix compositions with time evolution reach the composition corresponding to the equilibrium values across a curved interface.

In Fig. 5, we have plotted the shift in composition on the precipitate side from its equilibrium composition, $\Delta c^p$, as a function of interface curvature. The slope of the line is found to be $2 \gamma /\left(\xi_{p}\left(c_{e q}^{p}-c_{e q}^{m}\right)\right)$. This test confirms the ability of our model to predict the Gibbs-Thomson effect correctly.

Fig. 6 shows the precipitate-matrix microstructures at times $t=0$ s and $t=175$ s for 2,5 and 10 at. $\% \mathrm{Cu}$, respectively. Microstructures at $t=0$ s correspond to the "end" results of the KMC simulations (see Fig. 3). In all systems, the large particles grow at the expense of smaller particles.

![](./images/813273007354019841_7.jpg)

Fig. 5. Change in precipitate composition from its equilibrium composition across a flat interface $(\Delta c^{p})$ is plotted against the inverse of precipitate radius. The straight line for $\Delta c^{p}$ is given by the Gibbs Thomson equation (see Eq. (14)). The data points represent $\Delta c^{p}$ measured at the centre of the spherical precipitates obtained from three different PFM simulations.

The mean radius increases with time, while the number of particles decreases with time. During this time interval, after an initial transient, the total volume of the particles remains constant for each system, which implies that the matrix supersaturation is zero and the system is in the coarsening regime.

Fig. 7a-c shows the particle size distributions (PSDs) at $t=0$ s and $t=175$ s for the three systems. In all the cases, the size distribution shifts to its right and the distribution also broadens with time. An important aspect of LSW theory is dynamic scaling behaviour, which means the whole microstructure is self-similar during steady-state coarsening when scaled by the mean precipitate radius. The PSD predicted by LSW holds only for spherical particles in an infinitesimally small volume fraction of precipitates. As mentioned in Section 1, several modified theoretical and experimental results showed that, with a higher volume fraction of precipitate, the distribution becomes broader and has a smaller amplitude. Fig. 7d shows that the PSDs scaled by the mean radius obtained at different times, for the $Cu 5$ at.% system, follow this trend.

The mean particle radii $\bar{R}$ are obtained at different stages of coarsening for each system and are plotted as a function of ageing time in Fig. 8a. In Fig. 8b, the number of precipitates for each of these three systems is plotted as a function of time. For the 2 at. $\%$ Cu system, the number of particles in the computational domain reduces from about 55 at $t=0$ s to 27 at $t=175$ s. The small number of particles in a domain makes this system statistically unreliable for predicting the overall trend in the temporal evolution of the microstructure. Each denucleation event during evolution causes a gradual decrease in mean radius and sudden increase in the effective supersaturation in the matrix because of the small total number of particles. These events appear as steps in the mean radius vs. time plot. For the10 at.% Cu system, the initial number of particles (at $t=0$ s) is 260. However, this number decreases rapidly to126 at $t=10$ s due to a large number of coalescence events, and then decreases slowly to 30 at $t=175$ s. Denucleation events of a group of small particles appear as steps only at a later stage of evolution. For the 5 at.% Cu system, the number of particles decreases slowly from 166 at $t=0$ s to 33 at $t=175$ s. The larger number of particles than in the 2 at.% Cu composition and the smaller number of coalescence events than in the 10 at.% Cu composition make this system more favourable for studying coarsening kinetics following the LSW law.

According to the LSW theory, a cube of mean radius $\bar{R}(t)$ should increase linearly with time $t$ during coarsening regime:
$$
\overline{R}(t)=\left(\overline{R}(0)^{3}+K t\right)^{1 / 3},\qquad(15)
$$
where $\bar{R}(0)$ is the mean radius at $t=0$ s and $K$ is the coarsening rate constant. In Fig. 8c and d, we fit $\bar{R}(t)$ for the 5 and 10 at.% Cu systems, respectively, using the above equation in the time interval between $t \approx 0$ s (after the initial transient) and $t=120$ s when the simulation domain

![](./images/813273007354019841_8.jpg)

Fig. 6. Microstructures obtained at $t=0$ s (a,b,c) and $t=175$ s (d,e,f) for 2, 5 and 10 at.% Cu systems (first, second and third columns, respectively).

![](./images/813273007354019841_9.jpg)

Fig. 7. Particle size distributions (PSDs) for (a) 2, (b) 5 and (c) 10 at.% Cu at the beginning of the PFM simulations (start = red) and after 175 s (end = blue). (d) PSDs scaled by mean radius, for the Cu 5 at.% system, at three different times (0, 100, 175 s). The line shows the distribution obtained from the LSW theory. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/813273007354019841_10.jpg)

Fig. 8. (a) The precipitate mean radius $(\bar{R})$, and (b) the number of particles $(n_{p})$ is plotted as a function of time for 2,5 and 10 at. $\% Cu$ . The temporal evolution of the $\bar{R}$ for (c) 5 and (d) 10 at.\% $Cu$ , fitted with LSW kinetics at the time interval indicated by the green datapoints. Inside this time interval both systems contain sufficient precipitates for good statistics. (For interpretation of the references to colour in this figure legend, the reader is referred to theweb version of this article.)

contains a reasonable number of particles to describe the coarsening kinetics (see Fig. 8b). For the 5 at.% Cu system, the mean precipitate radius closely follows the LSW kinetics after an initial transient and the fit is good in thistime interval. We found $\bar{R}(0)=1.72 ~nm$ and $K_{L S W}=$  $0.1024 ~nm^{3} ~s^{-1}$ for this system. The value of $\bar{R}(0)$ is higher compared to the end results of KMC, because very small precipitates undergo a denucleation process during the ini- tial transient.

For the 10 at.% Cu system, the number of coalescence events is very high, which leads to an increase in $\bar{R}$ . Fur thermore, the particles do not remain spherical in shape(see Fig. 6f) during time evolution. The fit in this regime is not as good as in the 5 at.% Cu system, because the inherent assumptions of the LSW theory do not hold good for the 10 at.% Cu system. We found $\bar{R}(0)=1.86 ~nm$ and $K_{L S W}=0.2389 ~nm^{3} ~s^{-1}$ for this system. For our systems, we observe the rate constant $K$ to increase with increasing precipitate volume fraction, which is also reported in the literature.

## 5. Conclusions
In the present survey, we employ KMC and PFM simu- lations to provide a quantitative description of the different stages of precipitation by suitably using the strengths of each method. While KMC is able to model the process of early nucleation and growth adequately, late stage Ostwald ripening is more appropriately treated with the PFM.

Using this approach we are able to capture not only the coarsening regime with both models, but also the coales- cence events at high volume fractions of precipitates which are retrieved in the PFM simulations. It is found that the kinetics closely follows the LSW temporal power law in this regime, but the coarsening rate increases with an increase in volume fraction of precipitates. It is noteworthy that while analytical theories such as LSW can adequately describe ripening kinetics for specific particle morphologies and configurations, deviations from the assumptions require the employment of simulations. For this reason, computational modelling approaches such as the KMC and the PFM are useful.

## Acknowledgements
D.M. and S.S. would like to thank the German Re- search Foundation (DFG) for financial support of the pro- ject within the Cluster of Excellence in Simulation Technology (EXC 310/1) at the University of Stuttgart. A.M., P.B., S.S., R.M., A.C. and B.N. would like to thank the German Research Foundation (DFG) for financial support of the projects SCHM746/101-1 and NE822/12-1.

## References
[1] Schmauder S, Binkele P. Comp Mater Sci 2002;24:42-53.
[2] Nembach E. 1st ed. New York: John Wiley & Sons, Inc.; 1997.
[3] Lifshitz IM, Slyozov VV. J Phys Chem Solids 1961;19:35-50.
[4] Wagner C. Z Elektrochem 1961;581:65.

[5] Ardell AJ. Acta Metall 1972;20:61–71.

[6] Brailsford AD, Wynblatt P. Acta Metall 1979;27:489–97.

[7] Marqusee JA, Ross J. J Chem Phys 1984;80:536–43.

[8] Enomoto Y, Tokuyama M, Kawasaki K. Acta Metall 1986;34:2119–28.

[9] Marsh SP, Glicksman ME. Acta Mater 1996;44:3761–71.

[10] Kang CH, Yoon DN. Metall Trans A 1981;12:65–9.

[11] Bender W, Ratke L. Acta Mater 1998;46:1125–33.

[12] Snyder VA, Alkemper J, Voorhees PW. Acta Mater 2000;48:2689–701.

[13] Snyder VA, Alkemper J, Voorhees PW. Acta Mater 2001;49:699–709.

[14] Rowenhorst DJ, Kuang JP, Thornton K, Voorhees PW. Acta Mater 2006;54:2027–39.

[15] Willer D, Zies G, Kuppler D, Föhl J, Katerbau KH. Final report. MPA Stuttgart; 2001.

[16] Pan F, Ruoff H, Willer D, Katerbau KH. MPA report. MPA Stuttgart; 1996.

[17] Schick M, Wiedemann J, Willer D. Technischer Bericht. MPA Stuttgart; 1997.

[18] Soisson F, Barbu A, Martin G. Acta Mater 1996;44:3789–800.

[19] Schmauder S, Kohler C. Comp Mater Sci 2011;50:1238–43.

[20] Kohler C, Kizler P, Schmauder S. Model Simulat Mater Sci 2005;13:35–45.

[21] Bacon DJ, Osetsky YN. Philos Mag 2009;89:3333–49.

[22] Kizler P, Uhlmann D, Schmauder S. Nucl Eng Des 2000;196:175–83.

[23] Boettinger W, Warren J, Beckermann C, Karma A. Ann Rev Mater Res 2002;32:163–94.

[24] Chen LQ. Ann Rev Mater Res 2002;32:113–40.

[25] Thornton K, Ågren J, Voorhees PW. Acta Mater 2003;51:5675–710.

[26] Singer-Loginova I, Singer HM. Rep Prog Phys 2008;71:106501.

[27] Moelans N, Blanpain B, Wollants P. Calphad 2008;32:268–94.

[28] Nestler B, Choudhury A. Curr Opin Solid State Mater Sci 2011;15:93–105.

[29] Vaithyanathan V, Wolverton C, Chen LQ. Acta Mater 2004;52:2973–87.

[30] Kamachali RD, Hua J, Steinbach I, Hartmaier A. Int J Mater Res 2010;101:1332–8.

[31] Warren JA, Murray BT. Model Simulat Mater Sci 1996;4:215–29.

[32] Ode M, Suzuki T, Kim SG, Kim WT. Mater Trans 2001;42:2410–4.

[33] Wen YH, Lill JV, Chen SL, Simmons JP. Acta Mater 2010;58:875–85.

[34] Zhu JZ, Liu ZK, Vaithyanathan V, Chen LQ. Scripta Mater 2002;46:401–6.

[35] Zhu JZ, Wang T, Ardell AJ, Zhou SH, Liu ZK, Chen LQ. Acta Mater 2004;52:2837–45.

[36] Kim SG. Acta Mater 2007;55:6513–25.

[37] Koyama T, Onodera H. Mater Trans 2005;46:1187–92.

[38] Koyama T, Hashimoto K, Onodera H. Mater Trans 2006;47:2765–72.

[39] Koyama T, Onodera H. Mater Sci Forum 2007;539–543:2383–8.

[40] Pizzini S, Roberts K, Phythian W, English C, Greaves G. Philos Mag Lett 1990;61:223–9.

[41] Othen P, Jenkins M, Smith G. Philos Mag A 1994;70:1–24.

[42] Binkele P. PhD thesis, Universität Stuttgart; 2006.

[43] Soisson F, Fu CC. Solid State Phenom 2007;129:31–9.

[44] Molnar D, Binkele P, Hocker S, Schmauder S. Philos Mag 2012;92:586–607.

[45] Vincent E, Becquart CS, Domain C. J Nucl Mater 2006;351:88–99.

[46] Vincent E, Becquart CS, Domain C. Nucl Instrum Meth B 2007;255:78–84.

[47] Soisson F, Fu C. Phys Rev B 2007;76.

[48] Stadler J, Mikulla R, Trebin HR. Int J Mod Phys C 1997;8:1131–40.

[49] Bonny G, Pasianot RC, Castin N, Malerba L. Philos Mag 2009;89:3531–46.

[50] Choudhury A, Nestler B. Phys Rev E 2012;85:021602.

[51] Garcke H, Nestler B, Stinner B. SIAM J Appl Math 2004;64:775–99.

[52] Nestler B, Garcke H, Stinner B. Phys Rev E 2005;71:041609.

[53] Janssens K, Raabe D, Kozeschnik E, Miodownik MA, Nestler B. Computational materials engineering: an introduction to microstruc- ture evolution. Elsevier Academic Press; 2007.

[54] Sonderegger B, Kozeschnik E. Metall Mater Trans A 2009;40:499–510.

[55] Vincent E, Becquart C, Pareige C, Pareige P, Domain C. J Nucl Mater 2008;373:387–401.

[56] Mendelev MI, Han S, Srolovitz DJ, Ackland GJ, Sun DY, Asta M. Philos Mag 2003;83:3977–94.

[57] Buffington FS, Hirano K, Cohen M. Acta Metall 1961;9:434–9.

[58] Anand MS, Agarwala RP. J Appl Phys 1966;37:4248–51.

[59] Mukherjee R, Abinandanan TA, Gururajan MP. Acta Mater 2009;57:3947–54.

[60] Mukherjee R, Abinandanan TA, Gururajan MP. Scripta Mater 2010;62:85–8.